# Project Information

## Navigation

- Commons Daemon
  - [About](#index)
  - [Release History](#changes)
  - [Sources](#scm)
  - [Security](#security)
  - [Procrun](#procrun)
  - [Jsvc](#jsvc)
  - [Native binaries](#binaries)
  - [FAQ](#faq)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
  - [Project Reports](#project-reports)
    - [Rat Report](#rat-report)
    - [japicmp](#japicmp)
    - [Surefire](#surefire)
- [Daemon](#japicmp)
  - [Overview](#index)
  - [Procrun](#procrun)
  - [Jsvc](#jsvc)
  - [Native binaries](#binaries)
  - [FAQ](#faq)
- Development
  - [Issue Tracking](#issue-tracking)
  - [Source Repository](#scm)
- Other pages
  - [JIRA Report](#jira-changes)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/index.html -->

<!-- page_index: 1 -->

<a id="index--introduction"></a>

# Introduction

Since 1994, the Java programming language evolved and became a
valid tool to develop reliable and performant server applications as
opposed to just applets and client applications. The major disadvantage of
the Java platform is that still today the only portable way to
start a Java application relies on a single point of entry: the
`public static void
main(String[])` method.

Having a single-point of entry is a valid solution for client
applications, where interactively a user can command to the application
to quit (which can terminate the Virtual Machine process at calling the
`System.exit(int)`
method), but in those cases where the application is not interactive
(server applications) there is currently no portable way to notify
the Virtual Machine of its imminent shutdown.

A server application written in Java might have to perform several tasks
before being able to shut down the Virtual Machine process. For example
in the case of a Servlet container, before the VM process is shut down, sessions might need to be serialized to disk, and web applications need
to be destroyed.

One common solution to this problem is to create (for example) a
`ServerSocket` and wait for a particular
message to be issued. When the message is received, all operations
required to shut down the server applications are performed and at the
end the `System.exit` method is called
to terminate the Virtual Machine process. This method however, has
several disadvantages and risks:

- In case of a system-wide shutdown, the Virtual Machine process may be
  shut down directly by the operating system without notifying the running
  server application.
- If an attacker finds out the shutdown message to send to the server
  and discovers a way to send this message, he can easily interrupt
  the server's operation, bypassing all the security restrictions
  implemented in the operating system.

Most multi-user operating systems already have a way in which server
applications are started and stopped. Under Unix based operating systems
non-interactive server applications are called *daemons* and are
controlled by the operating system with a set of specified
*signals*. Under Windows such programs are called *services*
and are controlled by appropriate calls to specific functions defined in
the application binary, but although the ways of dealing with the problem
are different, in both cases the operating system can notify a server
application of its imminent shutdown, and the application has the
ability to perform certain tasks before its process of execution is
destroyed.

<a id="index--structure"></a>

# Structure

Daemon is made of 2 parts. One written in C that makes the interface to
the operating system and the other in Java that provides the
Daemon API.

<a id="index--platforms"></a>

# Platforms

Both Win32 and UNIX like platforms are supported.
For Win32 platforms use [procrun](#procrun).
For UNIX like platforms use [jsvc](#jsvc).

<a id="index--initial-source-of-the-package"></a>

# Initial Source of the Package

The original Java classes came from the Jakarta Tomcat 4.0 project.

The package name for the Daemon component is
`org.apache.commons.daemon`.

---

<a id="changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/changes.html -->

<!-- page_index: 2 -->

<a id="changes--apache-commons-daemon-release-notes"></a>

# Apache Commons Daemon Release Notes

<a id="changes--release-history"></a>

## Release History

| Version | Date | Description |
| --- | --- | --- |
| [1.5.1](#changes--a1.5.1) | 2025-12-16 | Bug fix release |
| [1.5.0](#changes--a1.5.0) | 2025-11-26 | This is a maintenance release. Java 8 or later is required. |
| [1.4.1](#changes--a1.4.1) | 2025-01-13 | Bug fix release |
| [1.4.0](#changes--a1.4.0) | 2024-05-24 | Bug fix release |
| [1.3.4](#changes--a1.3.4) | 2023-05-12 | Bug fix release |
| [1.3.3](#changes--a1.3.3) | 2022-11-29 | Bug fix release |
| [1.3.2](#changes--a1.3.2) | 2022-10-10 | Bug fix release |
| [1.3.1](#changes--a1.3.1) | 2022-05-09 | Bug fix release |
| [1.3.0](#changes--a1.3.0) | 2022-03-18 | Feature and bug fix release |
| [1.2.4](#changes--a1.2.4) | 2021-01-21 | Bug fix release |
| [1.2.3](#changes--a1.2.3) | 2020-09-01 | Bug fix release |
| [1.2.2](#changes--a1.2.2) | 2019-10-04 | Bug fix release |
| [1.2.1](#changes--a1.2.1) | 2019-09-09 | Bug fix release |
| [1.2.0](#changes--a1.2.0) | 2019-07-02 | Feature and bug fix release |
| [1.1.0](#changes--a1.1.0) | 2017-11-15 | Feature and bug fix release |

<a id="changes--release-1.5.1-2025-12-16"></a>

## Release 1.5.1 – 2025-12-16

| Type | Changes | By |
| --- | --- | --- |
| Fix | jsvc. Fix compilation warnings. | [markt](#team--markt) |
| Add | Procun. Build binaries for Windows using the static hybrid CRT strategy by default. | [markt](#team--markt) |

<a id="changes--release-1.5.0-2025-11-26"></a>

## Release 1.5.0 – 2025-11-26

| Type | Changes | By |
| --- | --- | --- |
| Fix | Remove -nouses directive from maven-bundle-plugin. OSGi package imports now state 'uses' definitions for package imports, this doesn't affect JPMS (from org.apache.commons:commons-parent:80). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Document --enable-preview | [michaelo](#team--michaelo) |
| Fix | Fix first appearance of --enable-native-access | [michaelo](#team--michaelo) |
| Fix | Procrun. Fix redirection issues on some OS versions by using recommended method to redirect stdout and stderr. Fixes [DAEMON-398](https://issues.apache.org/jira/browse/DAEMON-398). | [jfclere](#team--jfclere) |
| Fix | Procrun. Fix updating of startup mode to 'Automatic (delayed)' being incorrectly processed as an update to 'Manual'. Fixes [DAEMON-439](https://issues.apache.org/jira/browse/DAEMON-439). | [markt](#team--markt) |
| Fix | Procrun. Fix timeout handling #238. Fixes [DAEMON-468](https://issues.apache.org/jira/browse/DAEMON-468). Thanks to Jean-Frederic Clere, Mark Thomas, Sebb, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Procrun. Replace RTF version of license header with plain text version of full license in about box for monitor application. Fixes [DAEMON-472](https://issues.apache.org/jira/browse/DAEMON-472). | [markt](#team--markt) |
| Fix | Procrun. Service should be marked as stopped if the service worker crashes. Fixes [DAEMON-475](https://issues.apache.org/jira/browse/DAEMON-475). | [markt](#team--markt) |
| Add | Add support for --enable-native-access Java startup option in jsvc. Fixes [DAEMON-471](https://issues.apache.org/jira/browse/DAEMON-471). | [michaelo](#team--michaelo) |
| Add | Add tests for prunsrv on Windows #260. Thanks to Jean-Frederic Clere, Gary Gregory, Mark Thomas. | [ggregory](#team--ggregory) |
| Add | Add Java API compatibility report to the site (JApiCmp). Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump org.apache.commons:commons-parent from 78 to 91 #253, #255, #287. Thanks to Gary Gregory, Dependabot. | [ggregory](#team--ggregory) |
| Update | Update to use new ASF logo | [markt](#team--markt) |

<a id="changes--release-1.4.1-2025-01-13"></a>

## Release 1.4.1 – 2025-01-13

| Type | Changes | By |
| --- | --- | --- |
| Fix | Fix several issues around Java OS and header files location detection. | [michaelo](#team--michaelo) |
| Fix | Correct several log messages where an incorrect placeholder led to truncation of the inserted values. | [markt](#team--markt) |
| Add | Add protection to avoid high CPU usage for applications running in JVM mode that do not wait for the stop method to be called before the start method returns. Fixes [DAEMON-460](https://issues.apache.org/jira/browse/DAEMON-460). | [markt](#team--markt) |
| Update | Bump org.apache.commons:commons-parent from 71 to 78 #189, #196, #198, #204, #207, #210, #216. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Remove autogenerated files and rely on autoreconf only. | [michaelo](#team--michaelo) |

<a id="changes--release-1.4.0-2024-05-24"></a>

## Release 1.4.0 – 2024-05-24

| Type | Changes | By |
| --- | --- | --- |
| Fix | [StepSecurity] ci: Harden GitHub Actions #95. Thanks to step-security-bot, Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Procrun. Enable Control Flow Guard for Windows binaries. Fixes [DAEMON-429](https://issues.apache.org/jira/browse/DAEMON-429). | [markt](#team--markt) |
| Fix | Procrun. Better label for command used to start service shown in Prunmgr.exe. Fixes [DAEMON-461](https://issues.apache.org/jira/browse/DAEMON-461). | [markt](#team--markt) |
| Fix | jsvc. Fix warnings when running support/buildconf.sh | [markt](#team--markt) |
| Fix | jsvc. Fix compilation issue with newer compilers. Fixes [DAEMON-463](https://issues.apache.org/jira/browse/DAEMON-463). Thanks to michaelo. | [markt](#team--markt) |
| Fix | Procrun. Refactor UAC support so that elevation is only requested for actions that require administrator privileges. | [markt](#team--markt) |
| Add | Procrun. Add support for hybrid CRT builds. | [markt](#team--markt) |
| Add | jsvc. Add support for LoongArch64 support #92. Thanks to huajingyun. | [markt](#team--markt) |
| Update | Bump commons-parent from 57 to 69 #155. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | The minimum support Java version has been upgraded from Java 7 to Java 8. | [markt](#team--markt) |
| Update | Procrun. The minimum Windows versions supported are now Windows 10 and Windows Server 2016. | [markt](#team--markt) |
| Update | Bump commons-parent from 69 to 70. | [markt](#team--markt) |

<a id="changes--release-1.3.4-2023-05-12"></a>

## Release 1.3.4 – 2023-05-12

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Configured stack size now applies to the main thread when running in JVM mode. Fixes [DAEMON-451](https://issues.apache.org/jira/browse/DAEMON-451). Thanks to kkolinko. | [markt](#team--markt) |
| Fix | Procrun. If the specified log directory does not exist, attempt to create any missing parent directories, as well as the specified directory, when the service starts. Fixes [DAEMON-452](https://issues.apache.org/jira/browse/DAEMON-452). | [markt](#team--markt) |
| Fix | Procrun. Allow Windows service dependencies to be managed by Procrun or by 'sc config ...'. Fixes [DAEMON-458](https://issues.apache.org/jira/browse/DAEMON-458). | [markt](#team--markt) |
| Fix | jsvc. Fix DaemonController.reload() only working the first time it is called. Fixes [DAEMON-459](https://issues.apache.org/jira/browse/DAEMON-459). Thanks to Klaus Malorny. | [markt](#team--markt) |
| Fix | jsvc. Remove incorrent definition 'supported\_os' which defined in psupport.m4 file to fix jsvc build error on riscv64. Thanks to Eastdong. | [markt](#team--markt) |
| Update | Bump commons-parent from 54 to 57 #71, #91. Thanks to Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.3.3-2022-11-29"></a>

## Release 1.3.3 – 2022-11-29

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Fix creation of duplicate ACL entries on some Windows platforms. Fixes [DAEMON-450](https://issues.apache.org/jira/browse/DAEMON-450). Thanks to Norimasa Yamamoto. | [markt](#team--markt) |
| Fix | Procrun. Follow-up to ensure all child processes are cleaned up if the service does not stop cleanly. #64 Thanks to jfclere. | [markt](#team--markt) |
| Update | Bump actions/cache from 3.0.8 to 3.0.11 #60. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/checkout from 3.0.2 to 3.1.0 #59. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump actions/setup-java from 3.5.1 to 3.6.0 #63. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.7.2.0 to 4.7.3.0 #61, #66. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 55 to 56 #76 Thanks to Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.3.2-2022-10-10"></a>

## Release 1.3.2 – 2022-10-10

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Remove noisy INFO log message that triggered logging once per minute while the service was running. | [markt](#team--markt) |
| Fix | Fix typos in Javadoc and comments #50, #51. Thanks to Marc Wrobel. | [ggregory](#team--ggregory) |
| Fix | Procrun. The DependsOn parameter is no longer ignored when updating the service configuration. Fixes [DAEMOM-446](https://issues.apache.org/jira/browse/DAEMOM-446). | [markt](#team--markt) |
| Fix | Procrun. Fix crash and provide an error level log message when the user attempts to start the service without configuring a JVM and none is available via the registry. Fixes [DAEMOM-448](https://issues.apache.org/jira/browse/DAEMOM-448). | [markt](#team--markt) |
| Update | Bump actions/cache from 3.0.3 to 3.0.8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/checkout from 3 to 3.0.2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 53 to 54 #55. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.6.0.0 to 4.7.2.0 #48, #52, #53. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump jacoco-maven-plugin from 0.8.7 to 0.8.8. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump japicmp-maven-plugin from 0.15.4 to 0.16.0. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump JUnit 4 to 5 vintage. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |

<a id="changes--release-1.3.1-2022-05-09"></a>

## Release 1.3.1 – 2022-05-09

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Take account of LogLevel setting when logging to standard error so the user can opt to see messages at Info level and below. Fixes [DAEMON-441](https://issues.apache.org/jira/browse/DAEMON-441). | [markt](#team--markt) |
| Fix | Procrun. Clear expected errors when checking for environment variables to prevent the expected errors from polluting subsequent log messages. Fixes [DAEMON-441](https://issues.apache.org/jira/browse/DAEMON-441). | [markt](#team--markt) |
| Fix | Procrun. Only configure the logging to be written to a file when running as a service. Fixes [DAEMON-441](https://issues.apache.org/jira/browse/DAEMON-441). | [markt](#team--markt) |
| Fix | Procrun. Clear logged error on service installation failure to prevent the error polluting subsequent log messages. Fixes [DAEMON-441](https://issues.apache.org/jira/browse/DAEMON-441). | [markt](#team--markt) |
| Fix | Procrun. When configuring permissions for the logging path, use the default path if no explicit logging path is specified. Fixes [DAEMON-441](https://issues.apache.org/jira/browse/DAEMON-441). | [markt](#team--markt) |
| Fix | Procrun. When logging issues configuring permissions for the logging path, explicitly state when default values are being used rather than logging blank values. Fixes [DAEMON-441](https://issues.apache.org/jira/browse/DAEMON-441). | [markt](#team--markt) |
| Fix | Procrun. Increase the size limit on the message component of log entries to 4096 characters. Fixes [DAEMON-442](https://issues.apache.org/jira/browse/DAEMON-442). | [markt](#team--markt) |
| Fix | Procrun. Ensure child processes are cleaned up if the service does not stop cleanly. #39 Thanks to jfclere. | [markt](#team--markt) |
| Fix | Refactor multiple if statements to use switch. #45 Thanks to Arturo Bernal. | [markt](#team--markt) |
| Update | Bump actions/cache from 2.1.7 to 3.0.3 #41. Thanks to Dependabot, Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/setup-java from 2 to 3.5.1 #43. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.5.3.0 to 4.6.0.0 #42. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons-parent from 52 to 53 #44. Thanks to Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.3.0-2022-03-18"></a>

## Release 1.3.0 – 2022-03-18

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. --StopTimeout can be used to define the time that procrun waits for service to exit, but INFINITE timeout was using instead. Fixes [DAEMON-430](https://issues.apache.org/jira/browse/DAEMON-430). | [jfclere](#team--jfclere) |
| Fix | Minor improvements to Java code #22, #31. Thanks to Arturo Bernal. | [ggregory](#team--ggregory) |
| Fix | Procrun. Minor improvement that allows to have WINVER nmake variable directly defined at compile time as ABI version in hexadecimal format. | [mturk](#team--mturk) |
| Fix | Procrun. Log at Trace instead of Debug when a service reports its state from the prunsrv app. This avoids the Debug log filling up as it adds two events per minute. You can then stay in Debug logging to capture register, start, stop, and unregister Debug events. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Procrun. Miscellaneous logging improvements. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Procrun. Log the prunsrv function names at the Trace level. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Fix | Procrun. Only redirect stderr and stdout to files for the running service. Output from commands executed on the command line will not be redirected. Fixes [DAEMON-437](https://issues.apache.org/jira/browse/DAEMON-437). | [markt](#team--markt) |
| Fix | Procrun. Ensure that the user configured to run the service is also granted access to the log file directory. Fixes [DAEMON-437](https://issues.apache.org/jira/browse/DAEMON-437). | [markt](#team--markt) |
| Fix | Procrun. Ensure Trace is included in the logging levels exposed in the GUI. | [markt](#team--markt) |
| Fix | Procrun. Support --Startup=delayed for service installation as well as service update. Fixes [DAEMON-439](https://issues.apache.org/jira/browse/DAEMON-439). | [markt](#team--markt) |
| Add | Enable Dependabot #20. Thanks to John Patrick. | [ggregory](#team--ggregory) |
| Add | Procrun. reportServiceStatusE() shows scale of dwWaitHint as millisecond in logging. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Procrun. reportServiceStatusE() shows a short description for dwCurrentState in logging. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Procrun. Add support for a new log level called Trace, lower-level than Debug. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Procrun. Add logging when failing to obtain a service's description from the registry. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Add | Procrun. Add logging when failing to set the options of a service. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump actions/cache from v2 to v2.1.7 #24, #30, #36. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump build actions/setup-java from v1.4.3 to v2. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons.jacoco.version from 0.8.5 to 0.8.7. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump commons.japicmp.version from 0.14.3 to 0.15.4. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump junit from 4.13.1 to 4.13.2 #25. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Bump commons.daemon.javaversion 1.6 -> 1.7. Thanks to Gary Gregory. | [ggregory](#team--ggregory) |
| Update | Bump spotbugs-maven-plugin from 4.4.2.2 to 4.5.2.0 #37. Thanks to Dependabot. | [ggregory](#team--ggregory) |
| Update | Update the release build instructions to use CMSC 15.0.44. | [markt](#team--markt) |
| Update | Bump actions/checkout from 2 to 3 #40. Thanks to Dependabot. | [ggregory](#team--ggregory) |

<a id="changes--release-1.2.4-2021-01-21"></a>

## Release 1.2.4 – 2021-01-21

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Ensure that log messages written to stdout and stderr are not lost during start-up. Fixes [DAEMON-424](https://issues.apache.org/jira/browse/DAEMON-424). Thanks to Bernhard Scholz. | [markt](#team--markt) |
| Fix | Procrun. Correct a regression introduced in 1.2.3. Enable the service to start if the Options value is not present in the registry. Fixes [DAEMON-425](https://issues.apache.org/jira/browse/DAEMON-425). | [markt](#team--markt) |
| Fix | jsvc. Don't fail if the CAP\_DAC\_READ\_SEARCH capability is not available. Fall back to using argv[0] rather than /proc/self/exe to determine the path for the current binary. Fixes [DAEMON-426](https://issues.apache.org/jira/browse/DAEMON-426). | [markt](#team--markt) |
| Fix | Procrun. Remove some unnecessary code. Fixes [DAEMON-428](https://issues.apache.org/jira/browse/DAEMON-428). | [markt](#team--markt) |

<a id="changes--release-1.2.3-2020-09-01"></a>

## Release 1.2.3 – 2020-09-01

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Correct multiple issues related to enabling a service to interact with the desktop. Provide a better error message if this option is used with an invalid user, install the service with the option enabled if requested and correctly save the setting if it is enabled in the GUI. Fixes [DAEMON-411](https://issues.apache.org/jira/browse/DAEMON-411). | [markt](#team--markt) |
| Fix | jsvc. Update the list of paths searched for libjvm.so to include the path used by OpenJDK 11. Fixes [DAEMON-410](https://issues.apache.org/jira/browse/DAEMON-410). Thanks to Richard Morrell. | [markt](#team--markt) |
| Add | Procrun. Add additional debug logging for Java start mode. | [markt](#team--markt) |
| Fix | jsvc. Remove incorrect definition 'supported\_os' which defined in psupport.m4 file to fix jsvc build error on s390, arm, aarch64, mipsel and mips. Thanks to Ray Wang. | [markt](#team--markt) |
| Add | Procrun. More debug logging in prunsrv.c and javajni.c. | [ggregory](#team--ggregory) |
| Add | jsvc. Update arguments.c to support Java 11 --enable-preview #18. Fixes [DAEMON-419](https://issues.apache.org/jira/browse/DAEMON-419). Thanks to mads1980. | [ggregory](#team--ggregory) |
| Add | jsvc and Procrun. Add support for Java native memory tracking. Fixes [DAEMON-412](https://issues.apache.org/jira/browse/DAEMON-412). | [markt](#team--markt) |
| Add | Procrun. Add a new command, print, that outputs the command to (re-)configure the service with the current settings. This is intended to be used to save settings such as before an upgrade. Fixes [DAEMON-422](https://issues.apache.org/jira/browse/DAEMON-422). | [markt](#team--markt) |

<a id="changes--release-1.2.2-2019-10-04"></a>

## Release 1.2.2 – 2019-10-04

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Correct a regression in the fix for DAEMON-401 that prevented the service from starting unless support for the universal C runtime had been installed. Fixes [DAEMON-408](https://issues.apache.org/jira/browse/DAEMON-408). | [markt](#team--markt) |
| Update | Update Commons-Parent to version 49. | [markt](#team--markt) |
| Fix | Procrun. Fix compiler warnings for unreferenced formal parameters. | [markt](#team--markt) |
| Fix | Procrun. Switch code to use more secure versions of Windows API calls to resolve warnings reported by newer versions of Visual Studio. | [markt](#team--markt) |
| Fix | Correct the source assembly definitions to add README.md, CONTRIBUTING.md and HOWTO-RELEASE.txt, remove references to the deleted Ant build files and exclude the working directories of Windows binary builds. | [markt](#team--markt) |
| Add | More startup on Windows logging in javajni.c. #14. | [ggregory](#team--ggregory) |

<a id="changes--release-1.2.1-2019-09-09"></a>

## Release 1.2.1 – 2019-09-09

| Type | Changes | By |
| --- | --- | --- |
| Fix | jsvc. Correct debug log message that reports change in umask. Fixes [DAEMON-403](https://issues.apache.org/jira/browse/DAEMON-403). Thanks to Charles. | [markt](#team--markt) |
| Fix | Procrun. Correct a regression in the previous fix for this issue that caused 32-bit services to crash on start-up. Fixes [DAEMON-401](https://issues.apache.org/jira/browse/DAEMON-401). Thanks to Norimasa Yamamoto. | [markt](#team--markt) |
| Fix | Procrun. Correct a regression in the fix for DAEMON-391 that caused the GUI to mix up the WARN and INFO logging levels. Fixes [DAEMON-407](https://issues.apache.org/jira/browse/DAEMON-407). | [markt](#team--markt) |
| Fix | Procrun. Expand the search for a valid Java runtime library to include the current JDK home defined in the Windows registry. Fully document the search algorithm used to find the Java runtime library. Fixes [DAEMON-404](https://issues.apache.org/jira/browse/DAEMON-404). | [markt](#team--markt) |

<a id="changes--release-1.2.0-2019-07-02"></a>

## Release 1.2.0 – 2019-07-02

| Type | Changes | By |
| --- | --- | --- |
| Fix | Procrun. Add to OPT\_LFLAGS rather than overwrite OPT\_LFLAGS when setting /OPT:REF in the make file for Windows. Thanks to mturk. | [markt](#team--markt) |
| Fix | Procrun. Only set the global shutdown event if the event is created. Thanks to mturk. | [markt](#team--markt) |
| Fix | Unable to build with Java 9 using ant; dropped Ant build files. Fixes [DAEMON-379](https://issues.apache.org/jira/browse/DAEMON-379). | [sebb](#team--sebb) |
| Fix | Procrun. prunsrv stopping with error due to hard-coded timeout. Fixes [DAEMON-384](https://issues.apache.org/jira/browse/DAEMON-384). Thanks to blassmegod. | [ggregory](#team--ggregory) |
| Fix | Update config.guess and config.sub. Fixes [DAEMON-385](https://issues.apache.org/jira/browse/DAEMON-385). | [markt](#team--markt) |
| Fix | Jsvc. Set the sun.java.command system property when starting via jsvc so that tools like jconsole show something meaningful for the process name. Fixes [DAEMON-388](https://issues.apache.org/jira/browse/DAEMON-388). | [markt](#team--markt) |
| Fix | Procrun. Correct the level name used in the GUI for WARN so that changes made via the GUI are recognised. Order the log levels in the drop-down from ERROR to DEBUG. Fixes [DAEMON-391](https://issues.apache.org/jira/browse/DAEMON-391). Thanks to Thorsten Schöning. | [markt](#team--markt) |
| Fix | Procrun. Correct reversed code comments for JRE and JDK locations in the registry. Fixes [DAEMON-393](https://issues.apache.org/jira/browse/DAEMON-393). Thanks to Daniel Hofmann. | [ggregory](#team--ggregory) |
| Fix | Procrun. Undefined behavior in registry.c dwRegKey = dwRegKey++. Fixes [DAEMON-392](https://issues.apache.org/jira/browse/DAEMON-392). Thanks to Daniel Hofmann. | [ggregory](#team--ggregory) |
| Fix | Procrun. Fix a bug that meant a value provided for LibraryPath replaced the value of the PATH environment variable rather than prepended to it. Fixes [DAEMON-396](https://issues.apache.org/jira/browse/DAEMON-396). Thanks to Gerwin. | [markt](#team--markt) |
| Fix | Procrun. Ensure that JAVA\_HOME/bin is on the path when running in jvm mode so that additional DLLs, such as awt.dll, can be found if required. Fixes [DAEMON-396](https://issues.apache.org/jira/browse/DAEMON-396). Thanks to Gerwin. | [markt](#team--markt) |
| Fix | Procrun. Ensure that the java.library.path environment variable is correctly configured when running on a JRE that depends on the Universal CRT. Fixes [DAEMON-396](https://issues.apache.org/jira/browse/DAEMON-396). | [markt](#team--markt) |
| Add | Procrun. Log the error code returned if JVM creation fails to aid debugging. | [markt](#team--markt) |
| Add | Harden the Windows binaries against DLL hijacking in the directory where the binaries are located. | [markt](#team--markt) |
| Fix | Procrun. Ensure that environment variables set via prunsrv are visible to native libraries that depend on the Universal CRT. Fixes [DAEMON-401](https://issues.apache.org/jira/browse/DAEMON-401). Thanks to Jonathan Gallimore. | [markt](#team--markt) |
| Add | Procrun. Add 'NT Authority\LocalService' and 'NT Authority\NetworkService' as options to the Log On user interface. | [markt](#team--markt) |
| Update | Procrun. Change the default service user from LocalSystem to 'NT Authority\LocalService'. | [markt](#team--markt) |
| Fix | Procrun. Avoid a crash on shutdown if multiple WM\_CLOSE messages are received. Fixes [DAEMON-402](https://issues.apache.org/jira/browse/DAEMON-402). Thanks to Iode Leroy. | [markt](#team--markt) |
| Fix | Procrun. Ignore blank lines inserted into the Java Options and/or Java 9 Options text areas. This prevents settings after the first blank line from being lost when saved to the registry. Fixes [DAEMON-394](https://issues.apache.org/jira/browse/DAEMON-394). | [markt](#team--markt) |
| Fix | Procrun. Remove the code that removed quotes from configured Java and Java 9 Options. Fixes [DAEMON-399](https://issues.apache.org/jira/browse/DAEMON-399). | [markt](#team--markt) |
| Fix | Procrun. Ensure that vfprintf is the first parameter passed when using JNI to create the JVM as a workaround for startup error messages not being visible on stdout or stderr. Fixes [DAEMON-398](https://issues.apache.org/jira/browse/DAEMON-398). | [markt](#team--markt) |
| Add | Procrun. Add an option to configure the service to use the 'Automatic (Delayed Start)' startup mode. Fixes [DAEMON-303](https://issues.apache.org/jira/browse/DAEMON-303). | [markt](#team--markt) |
| Add | Procrun. When running in jre mode, if the standard Java registry entries for JavaHome and RuntimeLib are not present, attempt to use the Procrun JavaHome key to find the runtime library. Fixes [DAEMON-329](https://issues.apache.org/jira/browse/DAEMON-329). | [markt](#team--markt) |
| Add | jsvc. Include the full path to the jsvc executable in the debug log. Fixes [DAEMON-297](https://issues.apache.org/jira/browse/DAEMON-297). | [markt](#team--markt) |
| Add | jsvc. Improve search for libjli.dylib on macOS when using custom-built OpenJDK binaries. Fixes [DAEMON-397](https://issues.apache.org/jira/browse/DAEMON-397). Thanks to Petr Hadraba. | [markt](#team--markt) |
| Fix | Procrun. Improve log messages for interactions with the Windows service. Thanks to ggregory. | [markt](#team--markt) |
| Fix | jsvc. Improve mips detection. Thanks to YunQiang Su. | [markt](#team--markt) |

<a id="changes--release-1.1.0-2017-11-15"></a>

## Release 1.1.0 – 2017-11-15

| Type | Changes | By |
| --- | --- | --- |
| Add | Add DEBUG and ERROR logging to help diagnose problems when starting a Windows Service. Fixes [DAEMON-368](https://issues.apache.org/jira/browse/DAEMON-368). | [ggregory](#team--ggregory) |
| Update | Update the minimum Java requirement from version 5 to 6. Fixes [DAEMON-371](https://issues.apache.org/jira/browse/DAEMON-371). | [ggregory](#team--ggregory) |
| Update | Increase minimum Java version to Java 5. | [markt](#team--markt) |
| Update | Add AArch64 support to src/native/unix/support/apsupport.m4. Fixes [DAEMON-347](https://issues.apache.org/jira/browse/DAEMON-347). Thanks to Ganesh Raju. | [ggregory](#team--ggregory) |
| Fix | Compile the Windows binaries with the /DYNAMICBASE and /NXCOMPAT switches. Fixes [DAEMON-346](https://issues.apache.org/jira/browse/DAEMON-346). | [markt](#team--markt) |
| Fix | Remove calls to explicit garbage collection during daemon start and stop. Fixes [DAEMON-333](https://issues.apache.org/jira/browse/DAEMON-333). | [markt](#team--markt) |
| Fix | Update config.guess and config.sub to add support, amongst others, for the 64-bit PowerPC Little-Endian architecture. Fixes [DAEMON-343](https://issues.apache.org/jira/browse/DAEMON-343). | [markt](#team--markt) |
| Fix | Ensure that the PID file on Windows, if used, is readable by other processes. Fixes [DAEMON-332](https://issues.apache.org/jira/browse/DAEMON-332). | [markt](#team--markt) |
| Update | Update Commons-Parent to version 41. | [markt](#team--markt) |
| Fix | Update apsupport.m4 add support for 64-bit PowerPC architectures. Fixes [DAEMON-358](https://issues.apache.org/jira/browse/DAEMON-358). Thanks to Gustavo Romero. | [markt](#team--markt) |
| Fix | Suppress spurious "The data area passed to a system call is too small" error message in the log when Procrun fails to stop the service. Fixes [DAEMON-282](https://issues.apache.org/jira/browse/DAEMON-282). | [markt](#team--markt) |
| Update | Move attributions from @author in Javadocs to POM. Fixes [DAEMON-370](https://issues.apache.org/jira/browse/DAEMON-370). Thanks to Amey Jadiye. | [ggregory](#team--ggregory) |
| Fix | Enable jsvc to start when running on Java 9. Fixes [DAEMON-373](https://issues.apache.org/jira/browse/DAEMON-373). | [markt](#team--markt) |
| Fix | Fix a resource leak opening the JVM configuration file. Fixes [DAEMON-324](https://issues.apache.org/jira/browse/DAEMON-324). | [markt](#team--markt) |
| Fix | Improve the jsvc code that restarts the process if the JVM crashes so that if the JVM crashes after a signal has been received to shut down jsvc does not attempt to restart the JVM. Fixes [DAEMON-339](https://issues.apache.org/jira/browse/DAEMON-339). Thanks to John Wehle. | [markt](#team--markt) |
| Fix | Ensure that the child process is started with the correct umask. Fixes [DAEMON-318](https://issues.apache.org/jira/browse/DAEMON-318). Thanks to Markus Schneider. | [markt](#team--markt) |
| Fix | Correct conflicting information for the behavior of Procrun when using jvm mode. Fixes [DAEMON-309](https://issues.apache.org/jira/browse/DAEMON-309). | [markt](#team--markt) |
| Fix | Ensure that, when using Procrun in java or exe mode, the service process waits for the stop process to complete before starting clean-up to avoid a crash in the stop process. Fixes [DAEMON-372](https://issues.apache.org/jira/browse/DAEMON-372). Thanks to Sérgio Ozaki. | [markt](#team--markt) |
| Fix | Enable jsvc to find the jvm when running on AIX. Fixes [DAEMON-310](https://issues.apache.org/jira/browse/DAEMON-310). Thanks to John Wehle. | [markt](#team--markt) |
| Fix | Ensure that Procrun treats JVM crashes as service failures so the recovery options will apply. Fixes [DAEMON-302](https://issues.apache.org/jira/browse/DAEMON-302). | [markt](#team--markt) |
| Fix | Ensure that the //MQ command closes the prunmgr process even if the configuration dialog is open when the //MQ command is used. Fixes [DAEMON-312](https://issues.apache.org/jira/browse/DAEMON-312). | [markt](#team--markt) |
| Fix | When looking in the Windows registry for JRE and JDK installation locations, additionally check the registry keys used by IBM provided JREs and JDKs. Do this after checking the keys used by Oracle provided JREs and JDKs. Fixes [DAEMON-311](https://issues.apache.org/jira/browse/DAEMON-311). | [markt](#team--markt) |
| Fix | When looking in the Windows registry for JRE and JDK installation locations, additionally check the registry keys used by Oracle provided Java 9 and later JREs and JDKs. Do this after checking the keys used by Oracle provided Java 8 and earlier JREs and JDKs. Fixes [DAEMON-376](https://issues.apache.org/jira/browse/DAEMON-376). | [markt](#team--markt) |
| Fix | Add support for Java 9 command line arguments to jsvc. Fixes [DAEMON-374](https://issues.apache.org/jira/browse/DAEMON-374). Thanks to Rashmi Ranjan Mohanty. | [markt](#team--markt) |
| Add | Add a restarts options to jsvc to control the number of permitted restarts after a system crash. Fixes [DAEMON-334](https://issues.apache.org/jira/browse/DAEMON-334). Thanks to Brett Delle Grazie. | [markt](#team--markt) |
| Remove | Remove support for building Procrun for the Itanium platform. | [markt](#team--markt) |
| Update | Make Windows XP the minimum support target platform. | [markt](#team--markt) |
| Add | Add support to Procrun for separate JVM options for use when running on Java 9 and above. | [markt](#team--markt) |
| Fix | Fix race conditions in PID file handling in jsvc. Fixes [DAEMON-377](https://issues.apache.org/jira/browse/DAEMON-377). Thanks to Rustam Abdullaev. | [markt](#team--markt) |

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/scm.html -->

<!-- page_index: 3 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-daemon.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-daemon.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-daemon.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/security.html -->

<!-- page_index: 4 -->

<a id="security--about-security"></a>

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html).

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-daemon/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

None.

---

<a id="procrun"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/procrun.html -->

<!-- page_index: 5 -->

<a id="procrun--introduction"></a>

# Introduction

Procrun is a set of applications that allow Windows users to wrap
(mostly) Java applications (e.g. Tomcat) as a Windows service.
The service can be set to automatically start when the machine boots
and will continue to run with no user logged onto the machine.

<a id="procrun--procrun-monitor-application"></a>

# Procrun monitor application

**Prunmgr** is a GUI application for monitoring and configuring procrun
services.

Each command line directive is in the form of **//XX[//ServiceName]**

If the `//ServiceName` parameter is omitted, then the service name is
assumed to be the name of the file.
The Prunsrv application behaves in the same way, so to allow both applications to reside in the same directory, the Prunmgr application
will remove a trailing **w** (lower-case w) from the name.
For example if the Prunmgr application is renamed as `TestService.exe`
- or as `TestServicew.exe` -
then the default service name is `TestService`.

The available command line options are:

|  |  |  |
| --- | --- | --- |
| //ES | Edit service configuration | This is the default operation. It is called if the no option is provided. Starts the GUI application which allows the service configuration to be modified, started and stopped. |
| //MS | Monitor service | Starts the GUI application and minimizes it to the system tray. |
| //MR | Monitor & run service | Starts the GUI application and minimizes it to the system tray. Start the service if it is not currently running. |
| //MQ | Monitor Quit | Stop any running monitor for the service. |

<a id="procrun--procrun-service-application"></a>

# Procrun service application

**Prunsrv** is a service application for running applications as services.
It can convert any application (not just Java applications) to run as a service.

<a id="procrun--command-line-arguments"></a>

## Command line arguments

Each command line directive is in the form of **//XX[//ServiceName]**.

If the `//ServiceName` parameter is omitted, then the service name is
assumed to be the name of the file.
For example if the application is renamed as `TestService.exe`, then the default service name is `TestService`.

The available command line options are:

|  |  |  |
| --- | --- | --- |
| //TS | Run the service as a console application | This is the default operation. It is called if the no option is provided. |
| //RS | Run the service | Called only from ServiceManager |
| //ES | Start (execute) the service |  |
| //SS | Stop the service |  |
| //US | Update service parameters |  |
| //IS | Install service |  |
| //DS | Delete service | Stops the service first if it is currently running |
| //PS | Print service | Prints the command to (re-)create the current configuration |
| //PP[//seconds] | Pause | Default is 60 seconds |
| //VS | Version | Print version and exit (since version 1.0.3) |
| //? | Help | Print usage and exit (since version 1.0.3) |

Starting with version **1.0.8** a more traditional command line can
be used in the form: **command [ServiceName]**.

|  |  |  |
| --- | --- | --- |
| run | Run the service as a console application | This is the default operation. It is called if the no option is provided and has the same effect as calling **//TS**. |
| service | Run the service | Called only from ServiceManager |
| start | Start the service | Synonym for **//ES** |
| stop | Stop the service | Synonym for **//SS** |
| update | Update service parameters | Synonym for **//US** |
| install | Install service | Synonym for **//IS** |
| delete | Delete service | Stops the service first if it is currently running |
| print | Print service | Prints the command to (re-)create the current configuration |
| pause [seconds] | Pause | Default is 60 seconds |
| version | Version | Print version and exit |
| help | Help | Print usage and exit |

<a id="procrun--command-line-parameters"></a>

## Command line parameters

Each command parameter is prefixed with **--** (or **++**, see below).
If an environment variable exists with the same name as a command line parameter but
prefixed with `PR_` it will **override** the equivalent command line parameter.
For example:

```
set PR_CLASSPATH=xx.jar
```

is equivalent to providing

```
--Classpath=xx.jar
```

as a command line parameter.

If a parameter is repeated, then normally the last value takes precedence.
However some parameters can take multiple values - for example StartParams and JvmOptions.
If these parameters are prefixed with **++**, then the value will be appended to the existing value.
For example:

```

--Startup=manual --Startup=auto --JvmOptions=-Done=1 ++JvmOptions=-Dtwo=2
```

will result in the following values being used:

```

Startup:
auto

JvmOptions:
-Done=1
-Dtwo=2
```

Only multivalued parameters support this; they are indicated in the table below by **`++`**.
If **`++`** is used for a parameter that does not support multiple values, then it is treated the same as **`--`**. No error is reported.
Configuration is overwritten in case **`--`** is used.
For example:

```

--JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=4
```

will always overwrite the JvmOptions. The resulting configuration will be:

```

Startup:
auto

JvmOptions:
-Dthree=3
-Dfour=4
```

However if on **`++`** is used the values will be appended. For example calling the
following after the first example

```

++JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=2
```

will result in the following values being used:

```

Startup:
auto

JvmOptions:
-Done=1
-Dtwo=2
-Dthree=3
-Dfour=4
```

In case you intermix the **`++`** and **`--`** options, the
last **`--`** parameter will cause option reset. For example:

```

--Startup=manual --Startup=auto --JvmOptions=-Done=1 ++JvmOptions=-Dtwo=2 --JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=2
```

will result in the following values being used:

```

Startup:
auto

JvmOptions:
-Dthree=3
-Dfour=4
```

When updating a service (//US or update command), using **`--`**
will replace any existing parameter with the new setting.
For multivalued parameters, using the **`++`** option qualifier
will add the new value(s) to any existing value(s).

<table class="bodyTable">
<tr>
<th>Parameter Name  </th>
<th>Default</th>
<th>Description</th>
</tr>
<tr>
<td>--Description</td>
<td></td>
<td>Service name description (maximum 1024 characters)</td>
</tr>
<tr>
<td>--DisplayName</td>
<td>ServiceName</td>
<td>Service display name</td>
</tr>
<tr>
<td>--Install</td>
<td>procrun.exe //RS//ServiceName</td>
<td>Install image</td>
</tr>
<tr>
<td>--Startup</td>
<td>manual</td>
<td>Service startup mode can be either <b>delayed</b>, <b>auto</b> or <b>manual</b></td>
</tr>
<tr>
<td>--Type</td>
<td></td>
<td>Service type can be <b>interactive</b> to allow the service to interact with the desktop.
    This option can only be used with the <i>LocalSystem</i> account.</td>
</tr>
<tr>
<td>++DependsOn</td>
<td></td>
<td>List of services that this service depends on. Services are separated
        using either <b>#</b> or <b>;</b> characters.

<p>
<b>Note:</b> At installation, additional dependencies will be created
        on the services <i>Tcpip</i> and <i>Afd</i> if not explicitly
        specified. These additional dependencies will not be created
        automatically when updating the service configuration with
        <i>--DependsOn</i> and must be explicitly defined if required in that
        case.
        </p>
</td>
</tr>
<tr>
<td>++Environment</td>
<td></td>
<td>List of environment variables that will be provided to the service
        in the form <b>key=value</b>. They are separated using either
        <b>#</b> or <b>;</b> characters.
        If you need to embed either # or ; character within a value put them inside single quotes.
    </td>
</tr>
<tr>
<td>--User</td>
<td></td>
<td>User account used for running executable. It is used only for
        StartMode <b>Java</b> or <b>exe</b> and enables running applications
        as a service under an account without the LogonAsService privilege.</td>
</tr>
<tr>
<td>--Password</td>
<td></td>
<td>Password for user account set by --User parameter</td>
</tr>
<tr>
<td>--ServiceUser</td>
<td></td>
<td>Specifies the name of the account under which the service should run.
        Use an account name in the form <i>DomainName\UserName</i>.
        The service process will be logged on as this user.
        if the account belongs to the built-in domain, you can specify <i>.\UserName</i>
        Note that the Service Control Manager does not accept localised forms of
        the standard names so to use them you need to specify
        <i>NT Authority\LocalService</i>, <i>NT Authority\NetworkService</i> or
        <i>LocalSystem</i> as appropriate.
    </td>
</tr>
<tr>
<td>--ServicePassword</td>
<td></td>
<td>Password for user account set by --ServiceUser parameter</td>
</tr>
<tr>
<td>--LibraryPath</td>
<td></td>
<td>Directory added to the search path used to locate the DLLs for the JVM.
        This directory is added both in front of the <b>PATH</b> environment variable
        and as a parameter to the <b>SetDLLDirectory</b> function.
    </td>
</tr>
<tr>
<td>--JavaHome</td>
<td>JAVA_HOME</td>
<td>Set a different <strong>JAVA_HOME</strong> than defined by the <strong>JAVA_HOME</strong> environment
        variable.</td>
</tr>
<tr>
<td>--Jvm</td>
<td>auto</td>
<td>Use either <b>auto</b> (i.e. find the JVM from the Windows registry) or specify the full path to the <b>jvm.dll</b>.
        You can use environment variable expansion here. When auto is specified the following search order is used:

<ol>
<li>The current Java runtime library as defined in the registry</li>
<li>The current JRE as defined in the registry</li>
<li>The explicitly configured JavaHome for the service</li>
<li>The current JDK as defined in the registry</li>
</ol></td>
</tr>
<tr>
<td>++JvmOptions</td>
<td>-Xrs</td>
<td>List of options in the form of <b>-D</b> or <b>-X</b> that will be
        passed to the JVM. The options are separated using either
        <b>#</b> or <b>;</b> characters. If you need to embed either # or ;
        character put them inside single quotes. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>++JvmOptions9</td>
<td></td>
<td>List of options in the form of <b>-D</b> or <b>-X</b> that will be
        passed to the JVM when running on Java 9 or later. The options are
        separated using either <b>#</b> or <b>;</b> characters. If you need to
        embed either # or ; character put them inside single quotes.
        (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--Classpath</td>
<td></td>
<td>Set the Java classpath. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--JvmMs</td>
<td></td>
<td>Initial memory pool size in MB. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--JvmMx</td>
<td></td>
<td>Maximum memory pool size in MB. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--JvmSs</td>
<td></td>
<td>Thread stack size in KB. (Not used in <b>exe</b> mode.)</td>
</tr>
<tr>
<td>--StartMode</td>
<td></td>
<td>One of <b>jvm</b>, <b>Java</b> or <b>exe</b>.
    The modes are:

<ul>
<li>jvm - start Java in-process. Depends on jvm.dll, see <b>--Jvm</b>.</li>
<li>Java - same as exe, but automatically uses the default Java executable, i.e. %JAVA_HOME%\bin\java.exe.
    Make sure JAVA_HOME is set correctly, or use --JavaHome to provide the correct location.
    If neither is set, procrun will try to find the default JDK (not JRE) from the Windows registry.</li>
<li>exe - run the image as a separate process</li>
</ul>
</td>
</tr>
<tr>
<td>--StartImage</td>
<td></td>
<td>Executable that will be run. Only applies to <b>exe</b> mode.</td>
</tr>
<tr>
<td>--StartPath</td>
<td></td>
<td>Working path for the start image executable.</td>
</tr>
<tr>
<td>--StartClass</td>
<td>Main</td>
<td>Class that contains the startup method.
    Applies to the <b>jvm</b> and <b>Java</b> modes.  (Not used in <b>exe</b> mode.)
    </td>
</tr>
<tr>
<td>--StartMethod</td>
<td>main</td>
<td>Name of method to be called when service is started.
    It must be <code>static void</code> and have argument <code>(String args[])</code>.
    Only applies to <b>jvm</b> mode - in <b>Java</b> mode, the <b>main</b> method is always used.


<b>Note:</b> in <code>jvm</code> mode, the start method should not return until the stop method
    has been called.
    </td>
</tr>
<tr>
<td>++StartParams</td>
<td></td>
<td>List of parameters that will be passed to either StartImage or
        StartClass. Parameters are separated using either <b>#</b> or
        <b>;</b> character.</td>
</tr>
<tr>
<td>--StopMode</td>
<td></td>
<td>One of <b>jvm</b>, <b>Java</b> or <b>exe</b>.
    See <b>--StartMode</b> for further details.
    </td>
</tr>
<tr>
<td>--StopImage</td>
<td></td>
<td>Executable that will be run on Stop service signal. Only applies to <b>exe</b> mode.</td>
</tr>
<tr>
<td>--StopPath</td>
<td></td>
<td>Working path for the stop image executable. Does not apply to <b>jvm</b> mode.</td>
</tr>
<tr>
<td>--StopClass</td>
<td>Main</td>
<td>Class that will be used on Stop service signal.
    Applies to the <b>jvm</b> and <b>Java</b> modes.
    </td>
</tr>
<tr>
<td>--StopMethod</td>
<td>main</td>
<td>Name of method to be called when service is stopped.
    It must be <code>static void</code> and have argument <code>(String args[])</code>.
    Only applies to <b>jvm</b> mode.
    In <b>Java</b> mode, the <b>main</b> method is always used.
    </td>
</tr>
<tr>
<td>++StopParams</td>
<td></td>
<td>List of parameters that will be passed to either StopImage or
        StopClass. Parameters are separated using either <b>#</b> or
        <b>;</b> character.</td>
</tr>
<tr>
<td>--StopTimeout</td>
<td>60 seconds</td>
<td>Defines the timeout in seconds that procrun waits for service
        to stop.
        <b>The timeout applies to the stop command and to the time service needs to stop</b>
        Negative values are not allowed.
        Note: Make sure you use a value big enough to give time for
        procrun to stop the service. Once the time out is elapsed,
        procrun will try to kill the whole process tree the service
        has created.</td>
</tr>
<tr>
<td>--LogPath</td>
<td>%SystemRoot%\System32\LogFiles\Apache</td>
<td>Defines the path for logging. Creates the directory if necessary.</td>
</tr>
<tr>
<td>--LogPrefix</td>
<td>commons-daemon</td>
<td>Defines the service log filename prefix. The log file is created in the LogPath directory with
    <code>.YEAR-MONTH-DAY.log</code> suffix</td>
</tr>
<tr>
<td>--LogLevel</td>
<td>Info</td>
<td>Defines the logging level and can be either <b>Error</b>, <b>Warn</b>
<b>Info</b>, <b>Debug</b>, or <b>Trace</b>. (Case insensitive). Note
        that for all log entries, the maximum length of the message component of
        the log entry is 4096 characters.
    </td>
</tr>
<tr>
<td>--LogJniMessages</td>
<td>0</td>
<td>Set this non-zero (e.g. 1) to capture JVM jni debug messages in the procrun log file.
    Is not needed if stdout/stderr redirection is being used.

    Only applies to <b>jvm</b> mode.
    </td>
</tr>
<tr>
<td>--StdOutput</td>
<td></td>
<td>Redirected stdout filename. If named <b>auto</b> file is created
    inside <b>LogPath</b> with the name <b>service-stdout.YEAR-MONTH-DAY.log</b>.</td>
</tr>
<tr>
<td>--StdError</td>
<td></td>
<td>Redirected stderr filename. If named <b>auto</b> file is created
    in the <b>LogPath</b> directory with the name <b>service-stderr.YEAR-MONTH-DAY.log</b>.</td>
</tr>
<tr>
<td>--PidFile</td>
<td></td>
<td>Defines the file name for storing the running process id.
    Actual file is created in the <b>LogPath</b> directory</td>
</tr>
</table>

<a id="procrun--installing-services"></a>

## Installing services

To install the service, you need to use the **//IS** parameter.

<a id="procrun--install-the-service-named-testservice"></a>

#### Install the service named 'TestService'

```

prunsrv //IS//TestService --DisplayName="Test Service" \
        --Install=prunsrv.exe --Jvm=auto --StartMode=jvm --StopMode=jvm \
        --StartClass=org.apache.SomeStartClass --StartParams=arg1;arg2;arg3 \
        --StopClass=org.apache.SomeStopClass --StopParams=arg1#arg2
```

<a id="procrun--updating-services"></a>

## Updating services

To update the service parameters, you need to use the **//US** parameter.

<a id="procrun--update-the-service-named-testservice"></a>

#### Update the service named 'TestService'

```

prunsrv //US//TestService --Description="Some Dummy Test Service" \
        --Startup=auto --Classpath=%CLASSPATH%;test.jar
```

<a id="procrun--removing-services"></a>

## Removing services

To remove the service, you need to use the **//DS** parameter.
If the service is running it will be stopped and then deleted.

<a id="procrun--remove-the-service-named-testservice"></a>

#### Remove the service named 'TestService'

```
prunsrv //DS//TestService
```

<a id="procrun--debugging-services"></a>

## Debugging services

To run the service in console mode, you need to use the **//TS** parameter.
The service shutdown can be initiated by pressing **CTRL+C** or
**CTRL+BREAK**.
If you rename the prunsrv.exe to testservice.exe then you can just execute the
testservice.exe and this command mode will be executed by default.

<a id="procrun--run-the-service-named-testservice-in-console-mode"></a>

#### Run the service named 'TestService' in console mode

```
prunsrv //TS//TestService [additional arguments]
```

<a id="procrun--using-procrun-in-jvm-mode"></a>

# Using Procrun in jvm mode

To interface with the Procrun service application (prunsrv) using the **jvm** mode, you need to create a class with the appropriate method(s).
For example:

```

class MyClass;
// Error handling not shown
static void main(String [] args){
    String mode = args[0];
    if ("start".equals(mode){
        // process service start function
    }
    etc.
}
```

This should be configured as follows:

```

--Classpath MyClass.jar
--StartMode jvm --StartClass MyClass --StartParams start
--StopMode  jvm --StopClass  MyClass --StopParams  stop
```

The above example uses a single 'main' method, and uses a string parameter to specify whether the service function
is start or stop.
Alternatively, you can use different method names for the service start and stop functions:

```

class MyClass;
// Error handling not shown
static void start(String [] args){
        // process service start function
    }
static void stop(String [] args){
        // process service stop function
    }
}
```

This should be configured as follows:

```

--Classpath MyClass.jar
--StartMode jvm --StartClass MyClass --StartMethod start
--StopMode  jvm --StopClass  MyClass --StopMethod  stop
```

Note: in jvm mode, the start method should not return until the stop method has
been called. The start and stop methods are called from different threads.

<a id="procrun--using-procrun-in-java-or-exe-mode"></a>

# Using Procrun in Java or exe mode

When using the **Java** or **exe** modes, the Procrun service application (prunsrv)
launches the target application in a separate process.
The "stop" application needs to communicate somehow with the "start" application to tell it to stop.
For example, using RPC.

<a id="procrun--windows-registry-usage"></a>

# Windows Registry Usage

The basic Service definitions are maintained under the registry key:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<ServiceName>
```

Additional parameters are stored in the registry at:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Apache Software Foundation\ProcRun 2.0\<ServiceName>\Parameters
```

On 64-bit Windows procrun always uses 32-bit registry view for storing the configuration.
This means that parameters will be stored inside:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\ProcRun 2.0\<ServiceName>
```

---

<a id="jsvc"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/jsvc.html -->

<!-- page_index: 6 -->

<a id="jsvc--introduction"></a>

# Introduction

Jsvc is a set of libraries and applications for making Java
applications run on UNIX more easily.
Jsvc allows the application (e.g. Tomcat) to perform some privileged operations as root
(e.g. bind to a port < 1024), and then switch identity to a non-privileged user.
It can run on Win32 via the Cygwin emulation layer (see
 [Cygwin](https://www.cygwin.com/) for more information), however Win32 users may prefer to use  [procrun](#procrun)
instead, which allows the application to run as a Windows Service.

The sources are located in the src/native/unix subdirectory.

In the future  [APR](https://apr.apache.org/)  may be used
to provide more portable platform support.

<a id="jsvc--building-from-source"></a>

# Building from source

To build under a UNIX operating system you will need:

- GNU AutoConf (at least version 2.53)
- An ANSI-C compliant compiler (GCC is good)
- GNU Make
- A Java Platform 2 compliant SDK

You need to build the "configure" program with:

```

sh support/buildconf.sh
```

(Note it is possible to replace sh by any compatible shell like bash, ksh).
The result should be something like:

```

support/buildconf.sh
support/buildconf.sh: configure script generated successfully
```

Once the configure script is generated, follow the next section.

<a id="jsvc--building-from-a-release-tarball"></a>

# Building from a release tarball

To build the binary under a UNIX operating system you will need:

- An ANSI-C compliant compiler (GCC is good)
- GNU Make
- A Java Platform 2 compliant SDK

You have to specify the `JAVA_HOME` of the SDK
either with the `--with-java=<dir>` parameter or set the `JAVA_HOME` environment
to point to your SDK installation. For example:

```

./configure --with-java=/usr/java
```

or

```

export JAVA_HOME
./configure
```

If your operating system is supported, configure will go through cleanly, otherwise it will report an error (please send us the details of your
OS/JDK, or a patch against the sources). To build the binaries and
libraries simply do:

```

make
```

This will generate the executable file `jsvc`.

<a id="jsvc--starting-jsvc"></a>

# Starting jsvc

To check the allowed parameters for the jsvc binary simply do:

```

./jsvc -help
Usage: jsvc [-options] class [args...]

Where options include:

    -help | --help | -?
        show this help page (implies -nodetach)
    -jvm <JVM name>
        use a specific Java Virtual Machine. Available JVMs:
            'client' 'server'
    -client
        use a client Java Virtual Machine.
    -server
        use a server Java Virtual Machine.
    -cp / -classpath <directories and zip/jar files>
        set search path for service classes and resouces
    -home <directory>
        set the path of your JDK or JRE installation (or set
        the JAVA_HOME environment variable)
    -version
        show the current Java environment version (to check
        correctness of -home and -jvm. Implies -nodetach)
    -showversion
        show the current Java environment version (to check
        correctness of -home and -jvm) and continue execution.
    -nodetach
        don't detach from parent process and become a daemon
    -debug
        verbosely print debugging information
    -check
        only check service (implies -nodetach)
    -user <user>
        user used to run the daemon (defaults to current user)
    -verbose[:class|gc|jni]
        enable verbose output
    -cwd </full/path>
        set working directory to given location (defaults to /)
    -outfile </full/path/to/file>
        Location for output from stdout (defaults to /dev/null)
        Use the value '&2' to simulate '1>&2'
    -errfile </full/path/to/file>
        Location for output from stderr (defaults to /dev/null)
        Use the value '&1' to simulate '2>&1'
    -pidfile </full/path/to/file>
        Location for output from the file containing the pid of jsvc
        (defaults to /var/run/jsvc.pid)
    -D<name>=<value>
        set a Java system property
    -X<option>
        set Virtual Machine specific option
    -ea[:<packagename>...|:<classname>]
    -enableassertions[:<packagename>...|:<classname>]
        enable assertions
    -da[:<packagename>...|:<classname>]
    -disableassertions[:<packagename>...|:<classname>]
        disable assertions
    -esa | -enablesystemassertions
        enable system assertions
    -dsa | -disablesystemassertions
        disable system assertions
    -agentlib:<libname>[=<options>]
        load native agent library <libname>, e.g. -agentlib:hprof
    -agentpath:<pathname>[=<options>]
        load native agent library by full pathname
    -javaagent:<jarpath>[=<options>]
        load Java programming language agent, see java.lang.instrument
    -procname <procname>
        use the specified process name (works only for Linux)
    -wait <waittime>
        wait waittime seconds for the service to start
        waittime should multiple of 10 (min=10)
    -restarts <maxrestarts>
        maximum automatic restarts (integer)
        -1=infinite (default), 0=none, 1..(INT_MAX-1)=fixed restart count
    -stop
        stop the service using the file given in the -pidfile option
    -keepstdin
        does not redirect stdin to /dev/null
    --add-modules=<module name>
        Java 9 --add-modules option. Passed as it is to JVM
    --module-path=<module path>
        Java 9 --module-path option. Passed as it is to JVM
    --upgrade-module-path=<module path>
        Java 9 --upgrade-module-path option. Passed as it is to JVM
    --add-reads=<module name>
        Java 9 --add-reads option. Passed as it is to JVM
    --add-exports=<module name>
        Java 9 --add-exports option. Passed as it is to JVM
    --add-opens=<module name>
        Java 9 --add-opens option. Passed as it is to JVM
    --limit-modules=<module name>
        Java 9 --limit-modules option. Passed as it is to JVM
    --patch-module=<module name>
        Java 9 --patch-module option. Passed as it is to JVM
    --illegal-access=<value>
        Java 9 --illegal-access option. Passed as it is to JVM. Refer java help for possible values.
    --enable-preview
        Java 11 --enable-preview option. Passed as it is to JVM
    --enable-native-access=<module name>
        Java 21 --enable-native-access option. Passed as it is to JVM
```

<a id="jsvc--mac-os-x-universal-binaries"></a>

## Mac OS X universal binaries

If jsvc was build with universal binary support the proper way of
starting `jsvc` is by using Mac OS X `arch` command:

```

    arch -arch i386 ./jsvc -jvm server <original jsvc parameters>

    for running 64-bit JVM use the:
    arch -arch x86_64 ./jsvc -jvm server <original jsvc parameters>
```

Use `-jvm server` because default `client` JVM is
not present for all architectures.

<a id="jsvc--using-jsvc"></a>

# Using jsvc

There two ways to use jsvc: via a Class that implements the Daemon interface or
via calling a Class that has the required methods.
For example Tomcat-4.1.x uses the Daemon interface
whereas Tomcat-5.0.x provides a Class whose methods are called by jsvc directly.

<a id="jsvc--via-daemon-interface"></a>

## Via Daemon interface

Do the following:

- Write a Class that implements the Daemon interface (MyClass).
- Put it in a jarfile (my.jar).
- Call jsvc like:

```

./jsvc -cp commons-daemon.jar:my.jar MyClass
  
```

<a id="jsvc--directly"></a>

## Directly

Write a Class (MyClass) that implements the following methods:

- void init(String[] arguments): Here open configuration files, create a trace file, create
  ServerSockets, Threads
- void start(): Start the Thread, accept incoming connections
- void stop(): Inform the Thread to terminate the run(), close the ServerSockets
- `void destroy()`: Destroy any object created in init()

Store it in a jarfile and use as above:

```

./jsvc -cp my.jar MyClass
```

<a id="jsvc--how-jsvc-works"></a>

# How jsvc works

Jsvc uses 3 processes: a launcher process, a controller process and a controlled process.
The controlled process is also the main java thread, if the JVM crashes
the controller will restart it in the next minute.
Jsvc is a daemon process so it should be started as root and the `-user` parameter
allows to downgrade to an unprivilegded user.
When the `-wait` parameter is used, the launcher process waits until the controller says
"I am ready", otherwise it returns after creating the controller process.

<a id="jsvc--forks-in-commons-daemon"></a>

## Forks in commons-daemon

Launcher process:

```

main()
{
  fork()
  parent: wait_child(), wait until JAVA service started when the child says "I am ready".
  child: controller process.
}
```

Controller process:

```

  while (fork()) {
    parent: wait_for_child.
      if exited and restart needed continue
      else exit.
    child: exit(child()). controlled process.
  }
```

Controlled process:

```

In child(): controlled process.
  init_JVM().
  load_service().
  start_service().
  say "I am ready"
  wait for signal or poll for stop
  stop_service().
  destroy_service().
  destroy_JVM().
  exit (with different codes so that parent knows if it has to restart us).
```

Note: The controller process uses signals to stop the controlled process.

<a id="jsvc--downgrading-user"></a>

## Downgrading user

On Linux `setuid()`/`setgid()` + capabilities are used. On other Unix `setgid`/`initgroups` are used.
We have something like:

```

/* as root */
init_JVM().
load_service. /*  java_load() calls the load method */
downgrade user (set_caps() or set_user_group())
/* as the user $USER (from -user $USER parameter) */
umask()
start_service. /* java_start() calls the start method */
```

---

<a id="binaries"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/binaries.html -->

<!-- page_index: 7 -->

<a id="binaries--what-to-download"></a>

# What to download?

In the directory
[binaries](https://downloads.apache.org/commons/daemon/binaries/)
you will find subdirectories containing archives
corresponding to your operating system. Only the Windows builds are provided as a zip file.

<a id="binaries--how-do-i-get-the-executable"></a>

# How do I get the executable?

<a id="binaries--procrun"></a>

## procrun

The Windows archive (e.g. commons-daemon-x.y.z-bin-windows.zip) contains 2 different executables:

- prunsrv.exe - service application for running applications as services.
- prunmgr.exe - the GUI manager application used to monitor and configure installed services.

There is only one `prunmgr.exe` application for all architectures.
The `prunsrv.exe` executable is available in 2 different versions for different architectures.
The version in the top-level directory is for 32-bit (x86) architectures.
The lower level directories are for AMD/EMT 64-bit systems. Itanium is no longer supported.

The Windows application `prunsrv.exe` is used to install an application as a service.
Once installed, `prunmgr.exe` can be used to monitor and reconfigure the service.
(see [procrun](#procrun) for more information).
The Windows binary zip archive should be unpacked into the location from which you wish to run it, for example:
`%ProgramFiles%\Apache Commons Daemon`

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/faq.html -->

<!-- page_index: 8 -->

<a id="faq--buildconf-problems"></a>

# Buildconf problems

```

$ sh support/buildconf.sh autoconf: Undefined macros:***BUG in Autoconf--please report*** AC_PATH ***BUG in Autoconf--please report*** AC_PATH ***BUG in Autoconf--please report*** AC_PATH
```

Your version of autoconf is too old, upgrade your autoconf and retry.
Or run support/buildconf.sh in another machine and copy the daemon tree in
the machine where you want to compile jsvc.

<a id="faq--configure-problems"></a>

# Configure problems

```

configure: creating ./config.status
config.status: creating Makefile
mv: Makefile: set owner/group (was: 1670/0): Operation not permitted
config.status: creating Makedefs
mv: Makedefs: set owner/group (was: 1670/0): Operation not permitted
config.status: creating native/Makefile
mv: native/Makefile: set owner/group (was: 1670/0): Operation not permitted
*** All done ***
Now you can issue "make"
```

You should ignore those error messages they are normal in FreeBSD.
config.status creates files in /tmp and move them in the current directory.
When FreeBSD creates files it sets the group of the files to
the group of the directory where the files are created.
So if /tmp is group "wheel" the files are "wheel". When moving the files in
the current directory (if you are not member of group "wheel")
the group "wheel" cannot be set on the moved files.

<a id="faq--runtime-problems"></a>

# Runtime problems

On Linux 2.6.x jsvc does not start and write the following error:

```

jsvc.exec error: syscall failed in set_caps
jsvc.exec error: Service exit with a return value of 4
```

CONFIG\_SECURITY\_CAPABILITIES in missing in your kernel try the following in the kernel sources:

- Configure the kernel with "Default Linux Capabilities" and reboot
  (by make gconfig or make xconfig under "security options" and "Enable different security models")
- Insert the module "capability":

```

modprobe capability
```

<a id="faq--cygwin-configuration-problems"></a>

# Cygwin configuration problems

The configure of jsvc does not like spaces in directory name.
To configure with java installed in directory whose name contains a space, use the 8 characters name of the directory.
For example for java in installed in `c:\Archivos de programa\java\jdk1.5.0_06`:

```

./configure --with-java=/cygdrive/c/Archiv~1/java/jdk1.5.0_06
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/project-info.html -->

<!-- page_index: 9 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Daemon software is a set of utilities and Java support classes for running Java applications as server processes. These are commonly known as 'daemon' processes in Unix terminology (hence the name). On Windows they are called 'services'. |
| [Summary](https://commons.apache.org/proper/commons-daemon/summary.html) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-daemon/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-daemon/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-daemon/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-daemon/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-daemon/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-daemon/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-daemon/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/team.html -->

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
|  | jfclere | Jean-Frederic Clere | [jfclere at apache.org](mailto:jfclere at apache.org) | - | - | - | - | - |
|  | remm | Remy Maucherat | [remm at apache.org](mailto:remm at apache.org) | - | - | - | - | - |
|  | yoavs | Yoav Shapira | [yoavs at apache.org](mailto:yoavs at apache.org) | - | - | - | - | - |
|  | billbarker | Bill Barker | [billbarker at apache.org](mailto:billbarker at apache.org) | - | - | - | - | - |
|  | mturk | Mladen Turk | [mturk at apache.org](mailto:mturk at apache.org) | - | - | - | - | - |
|  | pier | Pier Fumagalli | [pier at apache.org](mailto:pier at apache.org) | - | - | - | - | - |
|  | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
|  | Nick Griffiths | [nicobrevin@gmail.com](mailto:nicobrevin@gmail.com) |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/ci-management.html -->

<!-- page_index: 11 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-daemon/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/project-reports.html -->

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
| [Javadoc](https://commons.apache.org/proper/commons-daemon/apidocs/index.html) | Javadoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-daemon/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-daemon/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire](#surefire) | Report on the test results of the project. |
| [RAT Report](#rat-report) | Report on compliance to license related source code policies |
| [JaCoCo](https://commons.apache.org/proper/commons-daemon/jacoco/index.html) | JaCoCo Coverage Report. |
| [japicmp](#japicmp) | Comparing source compatibility of commons-daemon-1.5.1.jar against commons-daemon-1.5.0.jar |

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/rat-report.html -->

<!-- page_index: 13 -->

<a id="rat-report--rat-release-audit-tool-results"></a>

# RAT (Release Audit Tool) results

The following document contains the results of [RAT (Release Audit Tool)](https://creadur.apache.org/rat/apache-rat-plugin/) Apache Creadur RAT::Plugin4Maven 0.17 (Apache Software Foundation).

```
*****************************************************
Summary
*****************************************************
Generated at: 2025-12-16T13:35:58Z
    by Apache Creadur RAT::Core 0.17 (Apache Software Foundation)

-----------------------------------------------------
Counters
-----------------------------------------------------
    (Entries starting with '!' exceed the minimum or maximum values)
  Approved:           117    A count of approved licenses.
  Archives:           0    A count of archive files.
  Binaries:           27    A count of binary files.
  Document types:     4    A count of distinct document types.
  Ignored:            11    A count of ignored files.
  License categories: 1    A count of distinct license categories.
  License names:      1    A count of distinct license names.
  Notices:            7    A count of notice files.
  Standards:          117    A count of standard files.
  Unapproved:         0    A count of unapproved licenses.
  Unknown:            0    A count of unknown file types.


-----------------------------------------------------
Licenses detected
-----------------------------------------------------

Apache License 2.0: 117 

-----------------------------------------------------
License Categories detected
-----------------------------------------------------

AL   : 117 

-----------------------------------------------------
Document Types detected
-----------------------------------------------------

BINARY: 27 
IGNORED: 11 
NOTICE: 7 
STANDARD: 117 

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

  /.git
  I         application/octet-stream     (directory)

  /.gitattributes
  I         application/octet-stream    

  /.github
  I         application/octet-stream     (directory)

  /.gitignore
  I         application/octet-stream    

  /CODE_OF_CONDUCT.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /CONTRIBUTING.md
  S         text/x-web-markdown    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /HOWTO-RELEASE.txt
  S         text/plain    ISO-8859-1
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

  /src/assembly/bin.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/native-src.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/src.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/assembly/win.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/changes/changes.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/docs/daemon.css
  S         text/css    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/docs/daemon.html
  S         text/html    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/Daemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonContext.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonController.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonInitException.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonListener.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonPermission.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/DaemonUserSignal.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/support/DaemonConfiguration.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/support/DaemonLoader.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/main/java/org/apache/commons/daemon/support/DaemonWrapper.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/media/commons-logo-component-100.xcf
  B         image/x-xcf    

  /src/media/commons-logo-component.xcf
  B         image/x-xcf    

  /src/media/logo.png
  B         image/png    

  /src/native/unix/INSTALL.txt
  N         text/plain    ISO-8859-1

  /src/native/unix/Makedefs.in
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/Makefile.in
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/autom4te.cache
  I         application/octet-stream     (directory)

  /src/native/unix/configure
  I         application/octet-stream    

  /src/native/unix/configure.ac
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/man/README.txt
  N         text/plain    ISO-8859-1

  /src/native/unix/man/fetch.sh
  B         application/x-sh    

  /src/native/unix/man/jsvc.1.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/.indent.pro
  S         text/x-prolog    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/Makefile.in
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/arguments.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/arguments.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/debug.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/debug.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/dso-dlfcn.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/dso-dyld.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/dso.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/help.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/help.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/home.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/home.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/java.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/java.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/jsvc-unix.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/jsvc.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/location.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/location.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/locks.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/locks.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/replace.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/replace.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/signals.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/signals.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/native/version.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/apfunctions.m4
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/apjava.m4
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/apsupport.m4
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/unix/support/buildconf.sh
  B         application/x-sh    

  /src/native/unix/support/config.guess
  I         application/octet-stream    

  /src/native/unix/support/config.sub
  I         application/octet-stream    

  /src/native/windows/README.txt
  N         text/plain    ISO-8859-1

  /src/native/windows/apps/prunmgr/Makefile
  S         text/x-makefile    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.manifest
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunmgr/prunmgr.rc
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/Makefile
  S         text/x-makefile    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.manifest
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/prunsrv.rc
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/apps/prunsrv/test/scripts/cleanstd.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/deleteservice.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/isemptystd.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/mybanner.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/startservice.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/stopservice.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/test.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/testservice.bat
  B         application/x-bat    

  /src/native/windows/apps/prunsrv/test/scripts/waituntilstop.bat
  B         application/x-bat    

  /src/native/windows/include/Makefile.inc
  S         text/plain    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/apxwin.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/cmdline.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/console.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/gui.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/handles.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/javajni.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/log.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/registry.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/rprocess.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/security.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/include/service.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/resources/commons.bmp
  B         image/bmp    

  /src/native/windows/resources/procrunr.ico
  B         image/vnd.microsoft.icon    

  /src/native/windows/resources/procruns.ico
  B         image/vnd.microsoft.icon    

  /src/native/windows/resources/procrunw.ico
  B         image/vnd.microsoft.icon    

  /src/native/windows/resources/susers.bmp
  B         image/bmp    

  /src/native/windows/src/cmdline.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/console.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/gui.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/handles.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/javajni.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/log.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/mclib.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/mclib.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/private.h
  S         text/x-chdr    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/registry.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/rprocess.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/security.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/service.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/src/utils.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/native/windows/xdocs/index.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/AloneDaemon.sh
  B         application/x-sh    

  /src/samples/AloneService.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/Native.c
  S         text/x-csrc    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/Native.sh
  B         application/x-sh    

  /src/samples/ProcrunService.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/ProcrunServiceInstall.cmd
  B         application/x-bat    

  /src/samples/ProcrunServiceRemove.cmd
  B         application/x-bat    

  /src/samples/README.txt
  N         text/plain    ISO-8859-1

  /src/samples/ServiceDaemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/ServiceDaemon.sh
  B         application/x-sh    

  /src/samples/ServiceDaemonReadThread.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/SimpleApplication.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/SimpleApplication.sh
  B         application/x-sh    

  /src/samples/SimpleDaemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/samples/SimpleDaemon.sh
  B         application/x-sh    

  /src/samples/build.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/resources/download_daemon.cgi
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

  /src/site/xdoc/binaries.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/download_daemon.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/faq.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/index.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/issue-tracking.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/jsvc.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/mail-lists.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/procrun.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/site/xdoc/security.xml
  S         application/xml    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/daemon/DaemonInitExceptionTest.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/daemon/ProcrunDaemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /src/test/java/org/apache/commons/daemon/SimpleDaemon.java
  S         text/x-java-source    ISO-8859-1
    AL       AL2.0         Apache License 2.0

  /target
  I         application/octet-stream     (directory)
```

---

<a id="japicmp"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/japicmp.html -->

<!-- page_index: 14 -->

# Daemon –

|  |  |
| --- | --- |
|  |  |

Copyright © 2002-2019
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

---

<a id="surefire"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/surefire.html -->

<!-- page_index: 15 -->

<a id="surefire--surefire-report"></a>

# Surefire Report

<a id="surefire--summary"></a>

## Summary

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| 1 | 0 | 0 | 0 | 100% | 0.064 s |

Note: failures are anticipated and checked for with assertions while errors are unanticipated.

<a id="surefire--package-list"></a>

## Package List

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

| Package | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.daemon](#surefire--org.apache.commons.daemon) | 1 | 0 | 0 | 0 | 100% | 0.064 s |

Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.

<a id="surefire--org.apache.commons.daemon"></a>

### org.apache.commons.daemon

| - | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [DaemonInitExceptionTest](#surefire--org.apache.commons.daemon.daemoninitexceptiontest) | 1 | 0 | 0 | 0 | 100% | 0.064 s |

<a id="surefire--test-cases"></a>

## Test Cases

[[Summary](#surefire--summary)] [[Package List](#surefire--package_list)] [[Test Cases](#surefire--test_cases)]

<a id="surefire--daemoninitexceptiontest"></a>

### DaemonInitExceptionTest

|  |  |  |
| --- | --- | --- |
|  | test | 0.033 s |

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/issue-tracking.html -->

<!-- page_index: 16 -->

<a id="issue-tracking--apache-commons-daemon-issue-tracking"></a>

# Apache Commons Daemon Issue tracking

Apache Commons Daemon uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons Daemon JIRA project page](https://issues.apache.org/jira/browse/DAEMON).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons Daemon please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310468&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-daemon/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310468&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310468&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons Daemon are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons Daemon bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310468&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons Daemon bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310468&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons Daemon bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310468&sorter/field=issuekey&sorter/order=DESC)

---

<a id="jira-changes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/jira-changes.html -->

<!-- page_index: 17 -->

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
<td><a href="https://issues.apache.org/jira/browse/DAEMON-416">DAEMON-416</a></td>
<td>-</td>
<td>prunsrv.exe adding special character while executing in windows 2019</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-475">DAEMON-475</a></td>
<td>Procrun</td>
<td>EXE MODE - Apache Commons Daemon Child process exit code 1 - Service Still Running</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-474">DAEMON-474</a></td>
<td>prunsrv</td>
<td>Logging doesn't work on 1.40./1.4.1 - Regression of 1.3.4 (worked perfectly)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-439">DAEMON-439</a></td>
<td>prunsrv</td>
<td>prunsrv '--Startup=delayed' sets manual mode instead</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-398">DAEMON-398</a></td>
<td>Procrun, prunsrv</td>
<td>Java 11 jvm.dll startup messages not available on stdout/stderr using Windows 10/2016</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-472">DAEMON-472</a></td>
<td>-</td>
<td>replace license.rtf with plain text</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-471">DAEMON-471</a></td>
<td>Jsvc</td>
<td>Add support for --enable-native-access Java startup option in jsvc</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.5.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-468">DAEMON-468</a></td>
<td>prunsrv</td>
<td>Fix timeout handling in procrun</td>
<td>Task</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-466">DAEMON-466</a></td>
<td>prunsrv</td>
<td>Service crashes with 1067 when stopping</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-460">DAEMON-460</a></td>
<td>prunsrv</td>
<td>High CPU usage in prunsrv.exe since Daemon 1.3.3</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-463">DAEMON-463</a></td>
<td>Jsvc</td>
<td>Daemon fails to build on macOS with XCode 15.3</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-429">DAEMON-429</a></td>
<td>Procrun, prunsrv</td>
<td>prunsrv.exe, and prunmgr.exe improper binary protection</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.4.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-461">DAEMON-461</a></td>
<td>Procrun</td>
<td>Improve "Path to executable:" label on service manager General tab</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-459">DAEMON-459</a></td>
<td>Jsvc</td>
<td>Restart only works once (regression)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-458">DAEMON-458</a></td>
<td>Procrun</td>
<td>The changes in DAEMON-446 cause existing DependsOn values to be removed</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-451">DAEMON-451</a></td>
<td>Procrun</td>
<td>Prunsrv does not use configured stack size for the main thread in jvm mode</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-452">DAEMON-452</a></td>
<td>prunsrv</td>
<td>Should we create the target folder before apxSecurityGrantFileAccessToUser?</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-450">DAEMON-450</a></td>
<td>prunsrv</td>
<td>Invoked "bin\tomcat9 //US/Tomcat9", logs directory will be inserted unwanted two ACLs</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.2</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-448">DAEMON-448</a></td>
<td>prunsrv</td>
<td>Service start fails with default Eclipse Temurin install</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.2</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-446">DAEMON-446</a></td>
<td>Procrun</td>
<td>Update service (//US) does not change DependsOn</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-443">DAEMON-443</a></td>
<td>-</td>
<td>prunsrv writes gigabytes of null bytes to stderr</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.3.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-442">DAEMON-442</a></td>
<td>Procrun</td>
<td>ProcRun classpath limitation of 1010 characters truncates the classpath string for many libraries on the classpath</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-441">DAEMON-441</a></td>
<td>-</td>
<td>When installing a Windows service using Commons Daemon 1.3.0 the errorlevel is -1073741819</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-437">DAEMON-437</a></td>
<td>prunsrv</td>
<td>prunsrv: Better not to redirect stdout/stderr during service installation?</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.3.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-430">DAEMON-430</a></td>
<td>Procrun</td>
<td>prunsrv stop timeout not honored</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-428">DAEMON-428</a></td>
<td>prunsrv</td>
<td> apxMultiSzToArrayW has incorrect use of IS_INVALID_HANDLE</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-426">DAEMON-426</a></td>
<td>Jsvc</td>
<td>CAP_DAC_READ_SEARCH not allowed in containers by default</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-425">DAEMON-425</a></td>
<td>Procrun</td>
<td>Crash if Java Options parameter is missing</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.4</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-424">DAEMON-424</a></td>
<td>prunsrv</td>
<td>stderr logfile is corrupted when running Tomcat 8.5 as Windows service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-412">DAEMON-412</a></td>
<td>Procrun</td>
<td>Tomcat started as windows service does not support Java Native Memory Tracking feature probably because of improper JVM initialization by Procrun</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-410">DAEMON-410</a></td>
<td>Jsvc</td>
<td>jsvc fails to find OpenJDK11 libjvm.so on a raspberry 4 (buster)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-422">DAEMON-422</a></td>
<td>Procrun</td>
<td>Add "dump configuration" mode of operation which generates a .BAT file capabile of re-creating the dumped service</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-419">DAEMON-419</a></td>
<td>Jsvc</td>
<td>jsvc support for Java 12+ preview features with --enable-preview</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-414">DAEMON-414</a></td>
<td>prunsrv</td>
<td>prunsrv uses its log is before it is initialized.</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.3</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-314">DAEMON-314</a></td>
<td>Jsvc</td>
<td>[daemon] feature request: jsvc stop with force option</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.2</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-408">DAEMON-408</a></td>
<td>Procrun</td>
<td>PROCRUN 1.2.x x64 crash on Windows Server 2008 R2</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-407">DAEMON-407</a></td>
<td>Procrun</td>
<td>Prunmgr displays incorrect logging level.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-404">DAEMON-404</a></td>
<td>Procrun</td>
<td>Crash: Openjdk not detected from registry</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-403">DAEMON-403</a></td>
<td>Jsvc</td>
<td>umask log is wrong</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-399">DAEMON-399</a></td>
<td>Procrun</td>
<td>apxStrUnQuoteInplaceA removes needed quotes</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.2.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-394">DAEMON-394</a></td>
<td>Procrun</td>
<td>Monitor application will update multi-string values in Windows registry with blank lines</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-402">DAEMON-402</a></td>
<td>Procrun</td>
<td>frequent crash in prunsrv when stopping service in 'java' mode</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1, 1.2.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-401">DAEMON-401</a></td>
<td>-</td>
<td>Environment variables set on service not available in JNI dll</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-396">DAEMON-396</a></td>
<td>Procrun</td>
<td>LibraryPath is broken for Java 11 using Windows 10/2016</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-393">DAEMON-393</a></td>
<td>-</td>
<td>Revered code comments for JRE and JDK locations in the registry</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-392">DAEMON-392</a></td>
<td>-</td>
<td>Undefined behaviour in registry.c dwRegKey = dwRegKey++</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-391">DAEMON-391</a></td>
<td>Procrun</td>
<td>Log level set by Tomcat-GUI under Windows not recognized.</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-388">DAEMON-388</a></td>
<td>Jsvc</td>
<td>jsvc does not play nice with JMX</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-385">DAEMON-385</a></td>
<td>Jsvc</td>
<td>commons-daemon-1.1.0 not supported with AIX 7</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-384">DAEMON-384</a></td>
<td>Procrun</td>
<td>prunsrv stopping with error due to hardcoded timeout</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-379">DAEMON-379</a></td>
<td>-</td>
<td>Unable to build with Java 9 using Ant</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-329">DAEMON-329</a></td>
<td>Procrun</td>
<td>Can procrun detect the JVM without consulting the registry</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-297">DAEMON-297</a></td>
<td>-</td>
<td>Show jsvc path in debug output</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-151">DAEMON-151</a></td>
<td>Procrun</td>
<td>Enable/Disable fields on the Start/Stop panels according to which Mode is selected</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-303">DAEMON-303</a></td>
<td>Procrun</td>
<td>prunsrv --Startup should offer "Automatic (Delayed Start)" option for service startup</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.1</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-397">DAEMON-397</a></td>
<td>Jsvc</td>
<td>jsvc on macOS cannot find libjli.dylib when home is OpenJDK 10 or 11</td>
<td>Wish</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-377">DAEMON-377</a></td>
<td>-</td>
<td>Race in PID file handing in jsvc resulting in Tomcat running without a pidfile</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-376">DAEMON-376</a></td>
<td>-</td>
<td>Update Daemon to also search registry for JRE with Java 9 JRE location</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-374">DAEMON-374</a></td>
<td>Jsvc</td>
<td>Add support for Java 9 command-line arguments</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-373">DAEMON-373</a></td>
<td>Jsvc</td>
<td>Daemon does not start with JDK9</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-372">DAEMON-372</a></td>
<td>Procrun</td>
<td>create shutdown event for shutdown process</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-358">DAEMON-358</a></td>
<td>Jsvc</td>
<td>PPC64: jsvc fails to find JVM jvm.cfg file and shared objects due to wrong path</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-347">DAEMON-347</a></td>
<td>Jsvc</td>
<td>Add AArch64 support to src/native/unix/support/apsupport.m4</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-339">DAEMON-339</a></td>
<td>Jsvc</td>
<td>Patch for commons-daemon 1.0.15 to avoid shutdown failures</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-333">DAEMON-333</a></td>
<td>Jsvc</td>
<td>Stop abusing System.gc() on Commons Daemon jsvc shutdown</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-332">DAEMON-332</a></td>
<td>Procrun</td>
<td>pid file not readable on Windows 7/8/2008</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-324">DAEMON-324</a></td>
<td>-</td>
<td>[home.c:130]: (error) Resource leak: cfgf</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-319">DAEMON-319</a></td>
<td>-</td>
<td>Add mips ABI n32, n64 support </td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-318">DAEMON-318</a></td>
<td>Jsvc</td>
<td>children (controller) process doesnt use correct umask value</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-312">DAEMON-312</a></td>
<td>Procrun</td>
<td>prunmgr: //MQ fails to kill multiple instances</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-311">DAEMON-311</a></td>
<td>Procrun</td>
<td>Commons Daemon procrun failed with exit value: 5 (Failed to start service)</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-310">DAEMON-310</a></td>
<td>Jsvc</td>
<td>jsvc fails on AIX 5.3</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-309">DAEMON-309</a></td>
<td>Procrun</td>
<td>Documentation for start method in JVM mode is conflicting</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-302">DAEMON-302</a></td>
<td>Procrun</td>
<td>Service recovery options do not work when a JNI crash brings down the JVM</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-282">DAEMON-282</a></td>
<td>Procrun</td>
<td>Failed to stop 'xx' service: The data area passed to a system call is too small</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-395">DAEMON-395</a></td>
<td>Jsvc</td>
<td>Fix hash links on download page</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-368">DAEMON-368</a></td>
<td>Procrun</td>
<td>Add DEBUG and ERROR logging to help diagnose problems when starting a Windows Service</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-343">DAEMON-343</a></td>
<td>-</td>
<td>Add 64-bit POWERPC-LE (ppc64le) support</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-334">DAEMON-334</a></td>
<td>Jsvc</td>
<td>Specify a maximum limit for automatic restarts</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-308">DAEMON-308</a></td>
<td>-</td>
<td>Add 64-bit ARM (aarch64) support</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-289">DAEMON-289</a></td>
<td>-</td>
<td>Integrate Debian patches</td>
<td>Improvement</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-243">DAEMON-243</a></td>
<td>Procrun</td>
<td>Support for Failure Recovery</td>
<td>New Feature</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-371">DAEMON-371</a></td>
<td>-</td>
<td>Update Java requirement from version 5 to 6.</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-370">DAEMON-370</a></td>
<td>-</td>
<td>Move attributions from @author in Javadocs to POM</td>
<td>Task</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-346">DAEMON-346</a></td>
<td>Procrun</td>
<td>Compile PROCRUN with Data Execution Prevention (DEP) flag</td>
<td>Wish</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.15</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-292">DAEMON-292</a></td>
<td>Procrun</td>
<td>Thread dump does not work</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.15</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-291">DAEMON-291</a></td>
<td>Jsvc</td>
<td>jsvc cores on Linux</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.15</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-288">DAEMON-288</a></td>
<td>Procrun</td>
<td>Hang while stopping procrun service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-287">DAEMON-287</a></td>
<td>Procrun</td>
<td>procrun's CloseHandle(_service_status_handle) not needed and causes exception</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-286">DAEMON-286</a></td>
<td>Procrun</td>
<td>Race condition during stopping service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-284">DAEMON-284</a></td>
<td>-</td>
<td>Service configuration corruption on install</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-283">DAEMON-283</a></td>
<td>Jsvc</td>
<td>DaemonWrapper cannot start launch methods with private constructors</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14, 1.1.0</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-281">DAEMON-281</a></td>
<td>Jsvc</td>
<td>Jsvc not loading correct shared lib for Java 7 on MacOS</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-280">DAEMON-280</a></td>
<td>Jsvc</td>
<td>jsvc umask comparison wrong - fix attached</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.14</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-278">DAEMON-278</a></td>
<td>Procrun</td>
<td>procrunsrv windows ++Environment doesn't work for java type</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.13</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-276">DAEMON-276</a></td>
<td>-</td>
<td>commons-daemon.log blows up when stopping Windows service</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.13</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-275">DAEMON-275</a></td>
<td>-</td>
<td>Website says that non-Windows binaries may be provided</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.12</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-274">DAEMON-274</a></td>
<td>Procrun</td>
<td>procrun ignores shutdown</td>
<td>Bug</td>
<td>Fixed</td>
<td>Closed</td></tr>
<tr>
<td>1.0.12</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-272">DAEMON-272</a></td>
<td>Jsvc</td>
<td>jsvc ignores -home option</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr>
<tr>
<td>1.0.12</td>
<td><a href="https://issues.apache.org/jira/browse/DAEMON-268">DAEMON-268</a></td>
<td>Jsvc</td>
<td>jsvc fails to find java home on centos</td>
<td>Bug</td>
<td>Fixed</td>
<td>Resolved</td></tr></table></section>
</td>
</tr>
</table>

Copyright © 2002-2025
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons Daemon, Apache, the Apache logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---
