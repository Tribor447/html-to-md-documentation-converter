# Project Information

## Navigation

- Commons Exec
  - [About](#index)
  - [Sources](#scm)
  - [Tutorial](#tutorial)
  - [Command Line](#commandline)
  - [FAQ](#faq)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-exec"></a>

# Apache Commons Exec

<a id="index--rationale"></a>

## Rationale

Executing external processes from Java is a well-known problem area. It is inherently platform dependent and requires the developer to know and test for platform specific behaviors, for example using cmd.exe on Windows or limited buffer sizes causing deadlocks. The JRE support for this is very limited, albeit better with the Java SE 1.5 ProcessBuilder class.

Reliably executing external processes can also require knowledge of the environment variables before or after the command is executed. In J2SE 1.1-1.4 there is not support for this, since the method, `System.getenv()`, for retrieving environment variables is deprecated.

There are currently several different libraries that for their own purposes have implemented frameworks around `Runtime.exec()` to handle the various issues outlined above. The proposed project should aim at coordinating and learning from these initiatives to create and maintain a simple, reusable and well-tested package. Since some of the more problematic platforms are not readily available, it is our hope that the broad Apache community can be a great help.

<a id="index--scope-of-the-package"></a>

## Scope of the package

The package shall create and maintain a process execution package written in the Java language to be distributed under the ASF license. The Java code might also be complemented with scripts (e.g. Perl scripts) to fully enable execution on some operating systems. The package should aim for supporting a wide range of operating systems while still having a consistent API for all platforms.

<a id="index--releases"></a>

## Releases

- Version 1.4.0 requires Java 8 or above.
- Version 1.3 is JDK 1.5 compatible.
- Version 1.2 is JDK 1.3 compatible.
- Version 1.1 is JDK 1.3 compatible.
- See the [Apache Archive](https://archive.apache.org/dist/commons/exec/).

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-exec
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-exec
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-exec
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="tutorial"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/tutorial.html -->

<!-- page_index: 3 -->

<a id="tutorial--apache-commons-exec"></a>

# Apache Commons Exec

<a id="tutorial--the-first-encounter"></a>

## The First Encounter

At this point we can safely assume that you would like to start some subprocesses from within your Java application and you spent some time here to do it properly. You look at Commons Exec and think "Wow - calling Runtime.exec() is easy and the Apache folks are wasting their and my time with tons of code".

Well, we learned it the hard way (in my case more than once) that using plain Runtime.exec() can be a painful experience. Therefore you are invited to delve into commons-exec and have a look at the hard lessons the easy way ...

<a id="tutorial--taming-your-first-process"></a>

## Taming Your First Process

Let's look at a real example - we would like to print PDF documents from within your Java application. After googling a while it turns out to be a minor headache and using Adobe Acrobat seems to be a good option.

The command line under Windows should look like "AcroRd32.exe /p /h file" assuming that the Acrobat Reader is found in the path.

```
String line = "AcroRd32.exe /p /h " + file.getAbsolutePath();
CommandLine cmdLine = CommandLine.parse(line);
DefaultExecutor executor = DefaultExecutor.builder().get();
int exitValue = executor.execute(cmdLine);
```

You successfully printed your first PDF document but at the end an exception is thrown - what happened? Oops, Acrobat Reader returned an exit value of '1' on success which is usually considered as an execution failure. So we have to tweak our code to fix this odd behavior - we define the exit value of "1" to be considered as successful execution.

```
String line = "AcroRd32.exe /p /h " + file.getAbsolutePath();
CommandLine cmdLine = CommandLine.parse(line);
DefaultExecutor executor = DefaultExecutor.builder().get();
executor.setExitValue(1);
int exitValue = executor.execute(cmdLine);
```

<a id="tutorial--to-watchdog-or-not-to-watchdog"></a>

## To Watchdog Or Not To Watchdog

You happily printed for a while but now your application blocks - your printing subprocess hangs for some obvious or not so obvious reason. Starting is easy but what to do with a run-away Acrobat Reader telling you that printing failed due to a lack of paper?! Luckily commons-exec provides a watchdog which does the work for you. Here is the improved code which kills a run-away process after sixty seconds.

```
String line = "AcroRd32.exe /p /h " + file.getAbsolutePath();
CommandLine cmdLine = CommandLine.parse(line);
DefaultExecutor executor = DefaultExecutor.builder().get();
executor.setExitValue(1);
ExecuteWatchdog watchdog = ExecuteWatchdog.builder().setTimeout(Duration.ofSeconds(60)).get();
executor.setWatchdog(watchdog);
int exitValue = executor.execute(cmdLine);
```

<a id="tutorial--quoting-is-your-friend"></a>

## Quoting Is Your Friend

Well, the code worked for quite a while until a new customer complained that no documents are printed. It took half a day to find out that the following file 'C:\Document And Settings\documents\432432.pdf' could not be printed. Due to the spaces and without further quoting the command line fell literally apart into the following snippet

```
> AcroRd32.exe /p /h C:\Document And Settings\documents\432432.pdf
```

As a quick fix we added double quotes which tells commons-exec to handle the file as a single command line argument instead of splitting it into parts.

```
String line = "AcroRd32.exe /p /h \"" + file.getAbsolutePath() + "\"";
CommandLine cmdLine = CommandLine.parse(line);
DefaultExecutor executor = DefaultExecutor.builder().get();
executor.setExitValue(1);
ExecuteWatchdog watchdog = ExecuteWatchdog.builder().setTimeout(Duration.ofSeconds(60)).get();
executor.setWatchdog(watchdog);
int exitValue = executor.execute(cmdLine);
```

<a id="tutorial--build-the-command-line-incrementally"></a>

## Build the Command Line Incrementally

The previous problem stems from the fact that commons-exec tried to split a single command line string into a string array considering single and double quotes. At the end of the day this is error-prone so we recommend building the command line incrementally - according to the same reasoning the Ant documentation does not recommend passing a single command line to the *exec* target (see deprecated command attribute for [exec](https://ant.apache.org/manual/CoreTasks/exec.html) task)

```
Map map = new HashMap();
map.put("file", new File("invoice.pdf"));
CommandLine cmdLine = new CommandLine("AcroRd32.exe");
cmdLine.addArgument("/p");
cmdLine.addArgument("/h");
cmdLine.addArgument("${file}");
cmdLine.setSubstitutionMap(map);
DefaultExecutor executor = DefaultExecutor.builder().get();
executor.setExitValue(1);
ExecuteWatchdog watchdog = ExecuteWatchdog.builder().setTimeout(Duration.ofSeconds(60)).get();
executor.setWatchdog(watchdog);
int exitValue = executor.execute(cmdLine);
```

Please note that we are passing an 'java.io.File' instance for expanding the command line arguments - this allows to convert the resulting file name on the fly to match your OS.

<a id="tutorial--unblock-your-execution"></a>

## Unblock Your Execution

Up to now we have a working example but it would not be good enough for production - because it is blocking.

Your worker thread will block until the print process has finished or was killed by the watchdog. Therefore executing the print job asynchronously will do the trick. In this example we create an instance of 'ExecuteResultHandler' and pass it to the 'Executor' instance in order to execute the process asynchronously. The 'resultHandler' picks up any offending exception or the process exit code.

```
CommandLine cmdLine = new CommandLine("AcroRd32.exe");
cmdLine.addArgument("/p");
cmdLine.addArgument("/h");
cmdLine.addArgument("${file}");
HashMap map = new HashMap();
map.put("file", new File("invoice.pdf"));
cmdLine.setSubstitutionMap(map);

DefaultExecuteResultHandler resultHandler = new DefaultExecuteResultHandler();

ExecuteWatchdog watchdog = ExecuteWatchdog.builder().setTimeout(Duration.ofSeconds(60)).get();
Executor executor = DefaultExecutor.builder().get();
executor.setExitValue(1);
executor.setWatchdog(watchdog);
executor.execute(cmdLine, resultHandler);

// some time later the result handler callback was invoked so we
// can safely request the exit value
resultHandler.waitFor();
int exitValue = resultHandler.getExitValue();
```

<a id="tutorial--get-your-hands-dirty"></a>

## Get Your Hands Dirty

A tutorial is nice but executing the tutorial code is even nicer. You find the ready-to-run tutorial under [src/test/java/org/apache/commons/exec/TutorialTest.java](https://commons.apache.org/exec/xref-test/org/apache/commons/exec/TutorialTest.html).

---

<a id="commandline"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/commandline.html -->

<!-- page_index: 4 -->

<a id="commandline--building-the-command-line"></a>

# Building the command line

<a id="commandline--you-have-two-ways-to-create-the-command-line-to-be-executed"></a>

# You have two ways to create the command line to be executed

- parsing the entire command line string
- building the command line incrementally

<a id="commandline--general-considerations"></a>

## General Considerations

No matter which approach you are using commons-exec does change your command line arguments in the following two cases

- when the executable contains forward or backward slashes
- when a command line argument contains an unquoted string

The following executable arguments

```
./bin/vim
```

will be translated under Windows to

```
.\\bin\\vim
```

<a id="commandline--parsing-the-entire-command-line-string"></a>

## Parsing the entire command line string

Parsing the command line string is easy to use but you might run into problems when tackling complex scenarios. Therefore this functionality was deprecated in the [Ant Exec task](https://ant.apache.org/manual/Tasks/exec.html).

Let's have a look at few examples you would like to stick to parsing entire command line strings

<a id="commandline--spaces-in-command-line-arguments"></a>

### Spaces in command line arguments

Here we would like to invoke a batch file which contains spaces in the path

```
cmd.exe /C c:\was51\Web Sphere\AppServer\bin\versionInfo.bat
```

Due to the space in the file name we have to quote the file name either with single or double quotes otherwise it falls apart into two command line arguments *c:\was51\Web* and *Sphere\AppServer\bin\versionInfo.bat*.

```
String line = "cmd.exe /C 'c:\\was51\\Web Sphere\\AppServer\\bin\\versionInfo.bat'";
```

<a id="commandline--building-the-command-line-incrementally"></a>

## Building the Command Line Incrementally

This is the recommended approach and caters also for pre-quoted command line argument.

<a id="commandline--a-simple-example"></a>

### A simple example

Now we would like to build the following command line

```
runMemorySud.cmd 10 30 -XX:+UseParallelGC -XX:ParallelGCThreads=2
```

using the following code snippet

```
CommandLine cmdl = new CommandLine("runMemorySud.cmd");
cmdl.addArgument("10");
cmdl.addArgument("30");
cmdl.addArgument("-XX:+UseParallelGC");
cmdl.addArgument("-XX:ParallelGCThreads=2");
```

<a id="commandline--a-complex-example"></a>

### A complex example

Now let's have a look at the following command line found somewhere in the internet

```
dotnetfx.exe /q:a /c:"install.exe /l ""\Documents and Settings\myusername\Local Settings\Temp\netfx.log"" /q"
```

The following code snippet builds the command line using pre-quoted arguments and variable expansion

```
File file = new File("/Documents and Settings/myusername/Local Settings/Temp/netfx.log");
Map map = new HashMap();
map.put("FILE", file);

cmdl = new CommandLine("dotnetfx.exe");
cmdl.setSubstitutionMap(map);
cmdl.addArgument("/q:a", false);
cmdl.addArgument("/c:\"install.exe /l \"\"${FILE}\"\" /q\"", false);
```

<a id="commandline--for-the-desperate"></a>

## For the Desperate

When crafting a command line it would be really helpful to see what happens to your command line arguments. The following scripts can be invoked to print your command line arguments for Unix

```
while [ $# -gt 0 ]
do
    echo "$1"
    shift
done
```

and for Windows

```
:Loop
IF [%1]==[] GOTO Continue
    @ECHO "%1"
SHIFT
GOTO Loop
:Continue
```

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/faq.html -->

<!-- page_index: 5 -->

<a id="faq--frequently-asked-questions"></a>

# Frequently Asked Questions

**General**

1. [How mature is it?](#faq--maturity)
2. [How do I create a complex command line using single and double quotes?](#faq--complex-quoting)
3. [Are child processes automatically killed?](#faq--killing-child-processes)
4. [Does commons-exec support java-gcj?](#faq--gcj-support)
5. [Why is the regression test broken on my Unix box](#faq--environment-testing)

<a id="faq--general"></a>

# General

How mature is it?
:   The code was ported from [Apache Ant](https://ant.apache.org/) and extensively
    tested on various platforms. So there is no reason not to use it and it is very likely
    better than any home-grown library.

    [[top]](#faq--top)

    ---

How do I create a complex command line using single and double quotes?
:   It is recommended to use CommandLine.addArgument() instead of CommandLine.parse(). Using
    CommandLine.parse() the implementation tries to figure out the correct quoting using your
    arguments and file names containing spaces. With CommandLine.addArgument() you can
    enable/disable quoting depending on your requirements. Having said that this is the
    recommended approach using Ant anyway.

    [[top]](#faq--top)

    ---

Are child processes automatically killed?
:   This functionality is largely depend on the operating system - on Unix it works
    mostly and under Windows not at all (see [Bug 4770092](https://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4770092)). In terms of stability and cross-platform support try to start your applications directly and
    avoid various wrapper scripts.

    [[top]](#faq--top)

    ---

Does commons-exec support java-gcj?
:   Well - one out of 55 regression tests fails. The
    EnvironmentUtilTest.testGetProcEnvironment() test fails because it detects no environment
    variables for the current process but there must be one since we require JAVA\_HOME to be
    set. Not sure if this is a plain bug in java-gcj-4.2.1 or requires a work around in
    commons-exec

    [[top]](#faq--top)

    ---

Why is the regression test broken on my Unix box
:   Please check if the shell scripts under "./src/test/script" are executable - assuming
    that they are not executable the "testExecute\*" and "testExecuteAsync\*" test will
    fail. We try very hard to keep the executable bit but they have somehow the tendency
    to be lost ...

    [[top]](#faq--top)

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/project-info.html -->

<!-- page_index: 6 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Exec is a library that reliably executes external processes from within the JVM. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-exec/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-exec/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-exec/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-exec/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-exec/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-exec/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-exec/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/summary.html -->

<!-- page_index: 7 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Exec |
| Description | Apache Commons Exec is a library that reliably executes external processes from within the JVM. |
| Homepage | [https://commons.apache.org/proper/commons-exec/](#index) |

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
| ArtifactId | commons-exec |
| Version | 1.6.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/team.html -->

<!-- page_index: 8 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_67b49f0dabb59814.jpg) | brett | Brett Porter | - | - | Apache | - | - | +10 |
| ![](assets/images/00000000000000000000000000000000_67b49f0dabb59814.jpg) | trygvis | Trygve Laugstøl | - | - | Apache | - | - | +1 |
| ![](assets/images/00000000000000000000000000000000_67b49f0dabb59814.jpg) | sgoeschl | Siegfried Goeschl | - | - | Apache | - | - | +1 |
| ![](assets/images/00000000000000000000000000000000_67b49f0dabb59814.jpg) | sebb | Sebastian Bazley | - | - | Apache | - | - | +1 |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Niklas Gustavsson

Benjamin Bentmann

Marco Ferrante

Jerome Lacoste

Milos Kleint

Pablo Hoertner

Niall Pemberton

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-exec/ci-management.html -->

<!-- page_index: 9 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-exec/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
