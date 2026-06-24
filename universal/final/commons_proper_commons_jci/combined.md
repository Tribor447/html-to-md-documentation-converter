# Apache Commons JCI - Project Information

## Navigation

- Apache Commons JCI
  - [About](#index)
  - [Usage](#usage)
  - [FAQ](#faq)
  - [Issue Tracking](#issue-tracking)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Issue Tracking](#issue-tracking)
    - [Continuous Integration](#integration)
    - [Project Modules](#modules)
    - [Project Summary](#project-summary)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-jci"></a>

## Apache Commons JCI

JCI is a java compiler interface. It can be used to either compile java (or any other language that can be
compiled to java classes like e.g. groovy or javascript) to java. It is well integrated with a filesystem
alteration monitor that can be used with the JCI compiling/reloading classloader. All the currently
supported compilers feature in-memory compilation.

The current implementation supports compilation via the following compilers:

- [Eclipse JDT compiler](http://www.eclipse.org/jdt/core/)
- [Janino](http://docs.codehaus.org/display/JANINO/Home)
- [Groovy](http://groovy.codehaus.org/)
- [Rhino](http://www.mozilla.org/rhino)

<a id="index--releases"></a>

## Releases

See the [downloads](https://commons.apache.org/proper/commons-jci/download_jci.cgi) page for information on obtaining releases.

<a id="index--documentation"></a>

## Documentation

The [Javadoc API documentation](https://commons.apache.org/proper/commons-jci/apidocs/index.html) is available online.
See the [Usage page](#usage) for some examples.

---

<a id="usage"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/usage.html -->

<!-- page_index: 2 -->

<a id="usage--compilation"></a>

## Compilation

The JavaCompiler is quite simple. You have to provide the paths to
the sources, where to get the sources from and where to store the classes. Then
you just pick one of the compilers to do the work. The result of the compilation
is returned as a CompilationResult.

```

JavaCompiler compiler = new JavaCompilerFactory().createCompiler("eclipse");
CompilationResult result = compiler.compile(sources, new FileResourceReader(sourceDir), new FileResourceStore(targetDir));

System.out.println( result.getErrors().length + " errors");
System.out.println( result.getWarnings().length + " warnings");
```

Information like line numbers of errors etc are accessible in a consistent way.
If supported by the compiler you can even get notified about error before the
end of the compilation. (see the CompilationProblemHandler) for that.
The example module provides a simple
[JSP servlet](https://commons.apache.org/proper/commons-jci/xref/org/apache/commons/jci/examples/serverpages/ServerPageServlet.html)
and a javac-like [command line interface](https://commons.apache.org/proper/commons-jci/xref/org/apache/commons/jci/examples/commandline/CommandlineCompiler.html).

<a id="usage--filesystem-monitoring"></a>

## Filesystem monitoring

A subproject of JCI provides a FilesystemAlterationMonitor that can
be used to get notified when files change on the local filesystem. If you attach
a ReloadingListener or a CompilingListener it can even
trigger the reload of a class in the ReloadingClassLoader.

```

ReloadingClassLoader classloader = new ReloadingClassLoader(this.getClass().getClassLoader());
ReloadingListener listener = new ReloadingListener();

listener.addReloadNotificationListener(classloader);

FilesystemAlterationMonitor fam = new FilesystemAlterationMonitor();
fam.addListener(directory, listener);
fam.start();
```

But you can also just implement a simple FilesystemAlterationListener
yourself and just use it to get notified about configuration files changes
[for example](https://commons.apache.org/proper/commons-jci/xref/org/apache/commons/jci/examples/configuration/ConfigurationReloading.html).
The example just extends the FileChangeListener that provides a few convenience methods.

<a id="usage--maven-artifacts"></a>

## Maven artifacts

Commons JCI is split into several modules, there is one artifact per compiler. Using the Eclipse compiler
requires to declare the following dependency in your project:

```
  <dependency>
      <groupId>org.apache.commons</groupId>
      <artifactId>commons-jci-eclipse</artifactId>
      <version>1.1</version>
  </dependency>
```

The other artifacts are commons-jci-groovy, commons-jci-janino
and commons-jci-rhino.

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/faq.html -->

<!-- page_index: 3 -->

<a id="faq--faq"></a>

## FAQ

<a id="faq--isn-t-compiler-support-integrated-with-java6-jsr199"></a>

### Isn't compiler support integrated with Java6 (JSR199)?

Yes, it is now. JSR199 in the end brought the official java compiler tools that
now come with Java 6. Progress on this had stalled for many years. This is how
JCI was born. JCI provided what was missing from the JDK. And it still provides
it also for earlier versions. The main author of JCI has later on joined the EG
and will make sure there is a bridge to the JSR199 API.

<a id="faq--doesn-t-jsr199-already-deprecate-jci"></a>

### Doesn't JSR199 already deprecate JCI?

Well, as said before ...there are no backports so far. And if you give the
the final java tools API in Java 6 a try you might well come back and
enjoy JCI :)

<a id="faq--how-well-tested-is-the-code"></a>

### How well tested is the code?

Well, there are a couple of projects out there using this code already for
quite some time in production. Drools and Cocoon to name just a few well known Open
Source projects. Code coverage is not bad at all ...but there still a few things
on the TODO list and contributions are always welcome.

<a id="faq--will-the-...-compiler-be-supported"></a>

### Will the ... compiler be supported?

There is always room for new implementations. And if the compiler supports compilation to
java bytecode, there is also a good chance it can be added. There are currently already a
few potential candidates out there. But it all comes down to the need and the time to implement.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/issue-tracking.html -->

<!-- page_index: 4 -->

<a id="issue-tracking--apache-commons-jci-issue-tracking"></a>

## Apache Commons JCI Issue tracking

Apache Commons JCI uses [ASF JIRA](http://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons JCI JIRA project page](http://issues.apache.org/jira/browse/JCI).

To use JIRA you may need to [create an account](http://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](http://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons JCI please do the following:

1. [Search existing open bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310650&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-jci/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310650&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310650&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons JCI are all unpaid volunteers

For more information on subversion and creating patches see the
[Apache Contributors Guide](http://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons JCI bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310650&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons JCI bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310650&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons JCI bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310650&sorter/field=issuekey&sorter/order=DESC)

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/project-info.html -->

<!-- page_index: 5 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons JCI is a java compiler interface. It can be used to compile Java itself, or any other language that can be compiled to Java classes (e.g. groovy or javascript). It is well integrated with a FAM (FilesystemAlterationMonitor) that can be used with the JCI compiling/reloading classloader. All the currently supported compilers feature in-memory compilation. |
| [Distribution Management](https://commons.apache.org/proper/commons-jci/distribution-management.html) | This document provides informations on the distribution management of this project. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-jci/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [Source Repository](https://commons.apache.org/proper/commons-jci/source-repository.html) | This is a link to the online source repository that can be viewed via a web browser. |
| [Mailing Lists](https://commons.apache.org/proper/commons-jci/mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Continuous Integration](#integration) | This is a link to the definitions of all continuous integration processes that builds and tests code on a frequent, regular basis. |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Dependency Management](https://commons.apache.org/proper/commons-jci/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Project Team](https://commons.apache.org/proper/commons-jci/team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Dependencies](https://commons.apache.org/proper/commons-jci/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |

---

<a id="integration"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/integration.html -->

<!-- page_index: 6 -->

<a id="integration--overview"></a>

## Overview

This project uses [Continuum](http://continuum.apache.org/).

<a id="integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
http://vmbuild.apache.org/continuum/
```

<a id="integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/modules.html -->

<!-- page_index: 7 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons JCI FileAlterationMonitor](https://commons.apache.org/proper/commons-jci/commons-jci-fam/index.html) | Commons JCI FileAlterationMonitor (FAM) to monitor local filesystems and get notified about changes. |
| [Apache Commons JCI core](https://commons.apache.org/proper/commons-jci/commons-jci-core/index.html) | Apache Commons JCI core interfaces and implementations. |
| [Apache Commons JCI compiler-eclipse](https://commons.apache.org/proper/commons-jci/compilers\commons-jci-eclipse/index.html) | Apache Commons JCI compiler implementation for the Eclipse compiler. |
| [Apache Commons JCI compiler-janino](https://commons.apache.org/proper/commons-jci/compilers\commons-jci-janino/index.html) | Apache Commons JCI compiler implementation for the Janino compiler. |
| [Apache Commons JCI compiler-groovy](https://commons.apache.org/proper/commons-jci/compilers\commons-jci-groovy/index.html) | Apache Commons JCI compiler implementation for the Groovy compiler. |
| [Apache Commons JCI compiler-rhino](https://commons.apache.org/proper/commons-jci/compilers\commons-jci-rhino/index.html) | Apache Commons JCI compiler implementation for Rhino javascript. |
| [Apache Commons JCI examples](https://commons.apache.org/proper/commons-jci/commons-jci-examples/index.html) | Apache Commons JCI examples. |

---

<a id="project-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jci/project-summary.html -->

<!-- page_index: 8 -->

<a id="project-summary--project-summary"></a>

## Project Summary

<a id="project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JCI |
| Description | Apache Commons JCI is a java compiler interface. It can be used to compile Java itself, or any other language that can be compiled to Java classes (e.g. groovy or javascript). It is well integrated with a FAM (FilesystemAlterationMonitor) that can be used with the JCI compiling/reloading classloader. All the currently supported compilers feature in-memory compilation. |
| Homepage | <http://commons.apache.org/proper/commons-jci/> |

<a id="project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-jci |
| Version | 1.1 |
| Type | pom |

---
