# Apache Commons BSF™ - Project Information

## Navigation

- BSF
  - [About](#index)
  - [News](#bsfnews)
  - [Documentation](#manual)
  - [FAQ](#faq)
  - [Related projects](#projects)
  - [Resources](#resources)
  - [Having a problem?](#problems)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Continuous Integration](#integration)
    - [Issue Tracking](#issue-tracking)
    - [Project Summary](#project-summary)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/index.html -->

<!-- page_index: 1 -->

<a id="index--bean-scripting-framework"></a>

## Bean Scripting Framework

Bean Scripting Framework (BSF) is a set of Java classes which provides scripting
language support within Java applications, and access to Java
objects and methods from scripting languages. BSF allows one to
write JSPs in languages other than Java while providing access to the Java
class library. In addition, BSF permits any Java application to be implemented
in part (or dynamically extended) by a language that is embedded within it.
This is achieved by providing an API that permits calling scripting
language engines from within Java, as well as an object registry that exposes
Java objects to these scripting language engines.

There are now two different versions of Apache BSF. These have different APIs.
The original version of BSF is represented by the BSF 2.x releases (current version 2.4), and uses an API which was originally developed at IBM.
The new version of Apache BSF is represent by the 3.x releases.
The 3.x version uses the API defined as part of JSR-223 (javax.script), which is included in Java 1.6 onwards.
However BSF 3.x will run on Java 1.4+, allowing access to JSR-223 scripting
for Java 1.4 and Java 1.5.
Apache BSF 3.x is also useful for Java 1.6 as it contains a command-line utility for
testing JSR-223 scripts as well as some utility classes for working with XML.

<a id="index--supported-languages-2.x"></a>

## Supported Languages - 2.x

BSF 2.x supports several scripting languages currently:

- [Javascript (using Rhino ECMAScript, from the Mozilla project)](http://www.mozilla.org/rhino/)
- [NetRexx](http://www-306.ibm.com/software/awdtools/netrexx/) (an extension of the IBM REXX scripting language in Java)
- [Commons JEXL](http://commons.apache.org/jexl/)
- [Python (using Jython)](http://jython.sourceforge.net/)
- [Tcl (using Jacl)](http://tcljava.sourceforge.net/)
- [XSLT Stylesheets (as a component of Apache XML project's Xalan and Xerces)](http://xalan.apache.org)

In addition, the following languages are supported with their own BSF engines:

- Java (using [BeanShell](http://www.beanshell.org/), from the BeanShell project)
- [Groovy](http://groovy.codehaus.org/)
- [Groovy Monkey](http://groovy.codehaus.org/Groovy+Monkey)
- [JLog](http://www.ulfdittmer.com/jlog/index.html) ([PROLOG implemented in Java](http://jlogic.sourceforge.net/))
- [JRuby](http://jruby.codehaus.org/)
- [JudoScript](http://www.judoscript.org)
- [ObjectScript](http://objectscript.sourceforge.net/)
- [ooRexx (Open Object Rexx)](http://www.oorexx.org/), using
  [BSF4ooRexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/).

Information on where to obtain scripting languages for use with BSF is
available on the [Related Projects](#projects) page.

<a id="index--documentation-2.x"></a>

## Documentation (2.x)

You can view the [documentation for BSF 2.4](#manual).

Documentation and examples are included in the source and binary distributions.

<a id="index--documentation-3.x"></a>

## Documentation (3.x)

The following references describe the standard API (javax.script) which is implemented by BSF 3.x:

- [JSR-223 Scripting for the Java Platform](http://jcp.org/aboutJava/communityprocess/final/jsr223/index.html) - specification (PDF)
- [Javadoc for javax.script classes](http://java.sun.com/javase/6/docs/api/javax/script/package-summary.html) in Java 1.6
- [Scripting for the Java platform (Sun technical article)](http://java.sun.com/developer/technicalArticles/J2SE/Desktop/scripting/)

Apache BSF 3.x includes an implementation of JSR-223 (javax.script) and runs on Java 1.4 and Java 1.5.
(Java 1.6 includes javax.script as standard.)
Note that although the implementation follows the JSR-223 specification, it has not been tested against
the JSR-223 TCK.
Apache BSF 3.x can therefore not strictly be described as a compatible implementation of JSR-223, however it is believed to be complete.

Apache BSF 3.x also includes some utility classes for working with XML.
These can be used with any used with any implementation of the javax.scripting package, including the one in Java 1.6+.

There is also a command-line utility which can be used to run scripts in any language engine which supports JSR-223.

Note that Apache BSF does not contain any language engines; these have to be downloaded separately.
Version 3.0 was shipped with a set of engine factories, however this is no longer present in later versions of BSF.
This is because many languages are now provided with their own factories.
Also, having all the factories in a single jar can cause problems at run-time.
If other jars contain factories that implement a different version of the same language
it may be difficult or impossible to choose which version is loaded.
If the language implementation is not present, the factory class may fail to load;
with some implementations of javax.script (e.g. Sun Java 1.6) this may prevent any factories from loading.

An example language which includes the necessary engine factory is:
[Apache Jexl 2.0](http://commons.apache.org/jexl/) (requires Java 1.5).
Some other scripting languages also come with their own factories already included.
For example [Groovy](http://groovy.codehaus.org/) and [JRuby](http://jruby.org/).

Many other languages are supported by the 3rd party engine factories available at
<https://scripting.dev.java.net/>.
This provides a combined archive from which the appropriate jar for the language can be extracted.

---

<a id="bsfnews"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/bsfnews.html -->

<!-- page_index: 2 -->

<a id="bsfnews--bsf-3.0"></a>

## BSF 3.0

<a id="bsfnews--october-9th-2009-bsf-3.0-final-release-available"></a>

### October 9th 2009 - BSF 3.0 Final Release Available

The release of BSF 3.0 Final is now available for
[download](http://jakarta.apache.org/site/downloads/downloads_bsf.cgi). If you have any feedback on this release, feel free to
join the discussion on the bsf-dev and bsf-user mailing lists.

<a id="bsfnews--bsf-3.0-beta-3"></a>

## BSF 3.0 Beta 3

<a id="bsfnews--april-5th-2009-bsf-3.0-beta3-release-available"></a>

### April 5th 2009 - BSF 3.0 Beta3 Release Available

The third beta release of BSF 3.0 is now available for
[download](http://jakarta.apache.org/site/downloads/downloads_bsf.cgi). If you have any feedback on this release, feel free to
join the discussion on the bsf-dev and bsf-user mailing lists.

<a id="bsfnews--bsf-3.0-beta-2"></a>

## BSF 3.0 Beta 2

<a id="bsfnews--november-9-2007-bsf-3.0-beta2-release-available"></a>

### November, 9, 2007 - BSF 3.0 Beta2 Release Available

The second beta release of BSF 3.0 is now available for
[download](http://jakarta.apache.org/site/downloads/downloads_bsf.cgi). If you have any feedback on this release, feel free to
join the discussion on the bsf-dev and bsf-user mailing lists.

<a id="bsfnews--bsf-3.0-beta-1"></a>

## BSF 3.0 Beta 1

<a id="bsfnews--april-16-2007-bsf-3.0-beta1-release-available"></a>

### April, 16, 2007 - BSF 3.0 Beta1 Release Available

The first beta release of BSF 3.0 is now available for
[download](http://jakarta.apache.org/site/downloads/downloads_bsf.cgi). If you have any feedback on this release, feel free to
join the discussion on the bsf-dev and bsf-user mailing lists.

<a id="bsfnews--bsf-2.4.0"></a>

## BSF 2.4.0

<a id="bsfnews--october-06-2006-bsf-2.4.0-available"></a>

### October, 06, 2006 - BSF 2.4.0 Available

The release of BSF 2.4 from Apache Jakarta is now available for
[download](http://jakarta.apache.org/site/downloads/downloads_bsf.cgi). If you have any feedback on this release, feel free to
join the discussion on the bsf-dev and bsf-user mailing lists.

<a id="bsfnews--interested"></a>

## Interested?

If you want to participate in developing BSF, join the
[bsf-dev mailing list](http://commons.apache.org/bsf/mail-lists.html) and contribute your ideas.

---

<a id="manual"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/manual.html -->

<!-- page_index: 3 -->

<a id="manual--bean-scripting-framework"></a>

## Bean Scripting Framework

Bean Scripting Framework (BSF) is a set of Java classes which provides
scripting language support within Java applications, and
access to Java objects and methods from scripting languages.

<a id="manual--bsf-architectural-overview"></a>

## BSF Architectural Overview

The two primary components of BSF are the BSFManager
and the BSFEngine.

The BSFManager handles all scripting execution engines
running under its control, and maintains the object registry that permits
scripts access to Java objects. By creating an instance of the
BSFManager class, a Java application can gain access to
scripting services.

The BSFEngine provides an interface that must be
implemented for a language to be used by BSF. This interface provides
an abstraction of the scripting language's capabilities that permits
generic handling of script execution and object registration within
the execution context of the scripting language engine.

An application can instantiate a single BSFManager, and execute several different scripting languages identically via the
BSFEngine interface. Furthermore, all of the scripting
languages handled by the BSFManager are aware of the
objects registered with that BSFManager, and the execution
state of those scripting languages is maintained for the lifetime of
the BSFManager.

<a id="manual--installation"></a>

## Installation

BSF can be used standalone, as a class library, or as part of an
application server. In order to be used as a class library or as
a standalone system, you simply download a copy of the bsf.jar
file from the
[BSF web site](http://commons.apache.org/bsf/index.html)
and include it in your classpath, along with any required classes
or jar files for desired languages.

In order to use BSF as part of the
[Tomcat](http://tomcat.apache.org/tomcat/)
servlet engine, you must currently download patches from the BSF
web site that permit Jasper to call BSF. Instructions for this will be
posted on the website, and will soon be accompanied by prebuilt binaries.
We hope that these changes will be merged into Tomcat in the near
future.

<a id="manual--using-bsf"></a>

## Using BSF

<a id="manual--bsf-and-jsps"></a>

### BSF and JSPs

After you set up an application server that is BSF enabled, you can write
JSPs using any of the supported scripting languages. JSPs using scripting
languages differ only slightly from those using Java.

First, you must set the language attribute of the page directive
in the JSP to the desired language. For example,

<%@ page language="javascript" %>

sets the language used for the JSP to Javascript; any
scriptlets or expressions within the JSP
will be handed off to BSF, which will in turn hand the code over to
Rhino for execution.

The standard set of JSP implicit objects is available within BSF.
These implicit objects must be used for input and output with respect
to the generated page, since the scripting languages do not have any
awareness of having been called within a JSP. For example, in order to
print a line of text into the page generated by the JSP, one must use the
println() method of the out implicit object.

Multiple languages can be supported within a given JSP; this is
accomplished by using the BSF taglibs, which are available from the
[Jakarta Taglibs](http://tomcat.apache.org/taglibs/index.html)
project. BSF taglib provides two tags: scriptlet and
expression. Both of these have a required language attribute, which is used to specify the language used on a per scriptlet
or expression basis.

<a id="manual--servlets-and-other-applications"></a>

### Servlets and Other Applications

Using BSF in servlets or applications is also quite simple. In order
to provide an application with scripting support, you need to
import the BSF class hierarchy and instantiate a BSFManager
object. After instantiating the BSFManager, you
register or declare any Java objects to be made available within the
scripting engine. Then call either one of the eval()
or exec() BSFManager methods (depending on whether you want to
evaluate a script and have the value of the evaluation returned, or
execute a script). Alternatively, you can call the
loadScriptingEngine() method in order to get an object
implementing the BSFEngine interface for the desired
scripting language. You can then call the exec() or
eval() methods of BSFEngine to run the script.

Additionally, BSF declares an object named bsf within a
scripting engine's execution context, which represents the
BSFManager that is associated with the scripting engine.
This object provides all of the methods and properties
associated with the BSFManager to the script.
However, the most used method within scripts is usually
lookupBean(), which is used to access objects
in BSF's object registry.

The most important methods within the BSFManager are:

- BSFManager() - the BSFManager
  constructor
- eval() - used to evaluate a script and return
  its value
- exec() - used to execute a script
- loadScriptingEngine() - used to return a
  BSFEngine for the desired scripting language
- registerBean() - adds an object to BSF's object
  registry
- lookupBean() - retrieves an object from BSF's
  object registry
- declareBean() - creates an implicit object in
  the context of any loaded scripting language, which does not have
  to be accessed via lookupBean()

Other, less often used methods within the BSFManager are:

- apply() - used to call anonymous functions
- compileExpr() - used to compile an expression into a
  CodeBuffer object
- compileScript() - similar to compile expression, used to
  compile scripts into CodeBuffer objects
- compileApply() - similar to both of the above - used to
  compile anonymous functions into CodeBuffer objects

For the curious, the CodeBuffer is a class provided by BSF for
storing generated Java code.

The BSFManager exec(), eval(), and apply() methods (as well as their compile counterparts)
are wrappers over the equivalent methods presented by the
BSFEngine interface. If the programmer explicitly
loads a scripting engine via loadScriptingEngine(), they
can use the exec() or eval() methods of the
resulting BSFEngine as appropriate.

<a id="manual--adding-bsf-support-for-a-scripting-language"></a>

## Adding BSF Support for a Scripting Language

In order to incorporate your own scripting language into BSF, you must first
write a class implementing the BSFEngine interface for the
language; examples are available in the BSF source distribution.

Usually, a scripting language author extends the
BSFEngineImpl class, which implements BSFEngine, and only requires the scripting language author to implement the
eval() method. However, the following methods specified by
the BSFEngine interface are the most commonly implemented:

- initialize() - used to set up the underlying scripting
  language engine
- call() - used to call functions or methods within the
  scripting engine
- eval() - used to evaluate a script
- exec() - used to execute a script
- declareBean() - used to create an implicit object within
  the scripting language
- undeclareBean() - used to remove an implicit object
  from the scripting language

Once you have implemented the wrapper for your language engine, you
instantiate a BSFManager in your application, and register your
engine with it via the registerScriptingEngine() method.
Afterward, you may use your language within the application through the
usual BSF semantics.

<a id="manual--standalone-scripts"></a>

## Standalone Scripts

BSF provides a facility for running scripting languages itself. Simply running
java org.apache.bsf.Main will produce a help message, with
instructions on how to run these scripts.

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/faq.html -->

<!-- page_index: 4 -->

<a id="faq--about-this-faq"></a>

## About this FAQ

<a id="faq--latest-version"></a>

### latest-version

Where do I find the latest version of this
document?

The latest version can always be found at BSF's homepage
<http://commons.apache.org/bsf/faq.html>.

<a id="faq--adding-faqs"></a>

### adding-faqs

How can I contribute to this FAQ?

The page you are looking it is generated from
[this](http://cvs.apache.org/viewcvs.cgi/~checkout~/jakarta-bsf/xdocs/faq.xml)
document. If you want to add a new question, please submit
a patch against this document to one of BSF's mailing lists;
hopefully, the structure is self-explanatory.

If you don't know how to create a patch, see the patches
section of [this
page](http://jakarta.apache.org/site/source.html).

<a id="faq--creating-faq"></a>

### creating-faq

How do you create the HTML version of this
FAQ?

We use
[Anakia](http://jakarta.apache.org/velocity/anakia.html)
to render the HTML version from the original XML file.

The Velocity stylesheets used to process the XML files can
be found in the xdocs/stylesheets subdirectory of
BSF's CVS repository - the build file docs.xml is
used to drive Anakia. This file assumes that you have the
jakarta-site2 module checked out from CVS as
well, but if you follow the instruction from Anakia's
homepage, you should get it to work without that. Just make
sure all required jars are in the task's classpath.

<a id="faq--general"></a>

## General

<a id="faq--what-is-bsf"></a>

### what-is-bsf

What is Bean Scripting Framework?

Bean Scripting Framework (BSF) is a set of Java classes which provides
scripting language support within Java applications. It also provides
access to Java objects and methods from supported scripting languages.
BSF allows one to write JSPs in languages other than Java while
providing access to the Java class library. In addition, BSF permits
any Java application to be implemented in part (or dynamically
extended) by a language that is embedded within it. This is achieved
by providing an API that permits calling scripting language engines
from within Java, as well as an object registry that exposes Java
objects to these scripting language engines.

<a id="faq--bsf-name"></a>

### bsf-name

Why do you call it BSF?

It's the beanage. Beans were the cool thing when BSF was first being
designed, and BSF contains several flavors.

<a id="faq--history"></a>

### history

Tell us a little bit about BSF's history.

BSF began life in 1999 as a research project of Sanjiva Weerawarana
at IBM's T.J. Watson Research Center. The initial intent had been
to provide access to JavaBeans from scripting language environments
(though there is nothing limiting access only to Java Beans). It was
soon moved to IBM's AlphaWorks developer site, where significant
interest (both internal and external to IBM) led to its being
moved to IBM's developerWorks site, where BSF could operate as an
open source project. During this time, significant development was
done by Matt Duftler and Sam Ruby, and BSF was incorporated into
both IBM products (Websphere) and Apache projects (Xalan). It was
this interest on the part of the Apache Software Foundation that
ultimately led to BSF's acceptance as a subproject of Jakarta in
2002.

During the process of moving BSF to Jakarta, development continued
within IBM, with further improvements to BSF's integration with
Jasper being made by John Shin and the addition of debugging support
for the Javascript language (a team effort, resulting from the work
of IBM researchers Olivier Gruber, Jason Crawford, and John Ponzo, and IBM software developers Chuck Murcko and Victor Orlikowski).

It is the current version, 2.3, that has been donated to Apache
Software Foundation from IBM.

<a id="faq--installation"></a>

## Installation

<a id="faq--no-gnu-tar"></a>

### no-gnu-tar

I get checksum errors when I try to extract the
tar.gz distribution file. Why?

BSF's distribution contains file names that are longer
than 100 characters, which is not supported by the standard
tar file format. Several different implementations of tar use
different and incompatible ways to work around this
restriction.

BSF's <tar> task can create tar archives that use
the GNU tar extension, and this has been used when putting
together the distribution. If you are using a different
version of tar (for example, the one shipping with Solaris), you cannot use it to extract the archive.

The solution is to either install GNU tar, which can be
found [here](http://www.gnu.org/software/tar/tar.html), or use the zip archive instead (you can extract it using
jar xf).

<a id="faq--how-do-i-..."></a>

## How do I ...

<a id="faq--doh"></a>

### doh

How do I install BSF?

BSF can be used standalone, as a class library, or as part of an
application server. In order to be used as a class library or as
a standalone system, one simply downloads a copy of the bsf.jar
file from the
[BSF web site](http://commons.apache.org/bsf/index.html)
and includes it in their classpath, along with any required classes
or jar files for the desired languages.

In order to use BSF as part of the
[Tomcat](http://tomcat.apache.org/tomcat/)
servlet engine, one must currently download patches from the BSF
web site that permit Jasper to call BSF. Instructions for this will be
posted on the website, and will be accompanied by prebuilt binaries.
We hope that these changes will be merged into Tomcat in the near
future.

<a id="faq--it-doesn-t-work-as-expected"></a>

## It doesn't work (as expected)

<a id="faq--winzip-lies"></a>

### winzip-lies

BSF creates JAR files with a lower-case
meta-inf directory.

No it doesn't.

You may have seen these lower-case directory names in
WinZIP, but WinZIP is trying to be helpful (and fails). If
WinZIP encounters a filename that is all upper-case, it
assumes it has come from an old DOS box andchanges the case to
all lower-case for you.

If you extract (or just check) the archive with jar, you
will see that the names have the correct case.

<a id="faq--advanced-issues"></a>

## Advanced Issues

<a id="faq--tbd2"></a>

### TBD2

To be added

To be added

<a id="faq--known-problems"></a>

## Known Problems

<a id="faq--javadoc-cannot-execute"></a>

### javadoc-cannot-execute

JavaDoc failed: java.io.IOException: javadoc: cannot execute

There is a bug in the Solaris reference implementation of
the JDK (see <http://developer.java.sun.com/developer/bugParade/bugs/4230399.html>).
This also appears to be true under Linux. Moving the JDK to
the front of the PATH fixes the problem.

---

<a id="projects"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/projects.html -->

<!-- page_index: 5 -->

<a id="projects--related-projects-alphabetical-order"></a>

## Related Projects (Alphabetical Order)

Nothing listed here is directly supported by the BSF
developers. If you encounter any problems with them, please use
the contact information. Failing that, a query to the bsf-users
mailing list may help.

<a id="projects--beanshell-interpretative-java"></a>

### BeanShell (Interpretative Java)

"BeanShell is a small, free, embeddable, Java source interpreter
with object scripting language features, written in Java. BeanShell
executes standard Java statements and expressions, in addition to
obvious scripting commands and syntax. BeanShell supports scripted
objects as simple method closures like those in Perl and
JavaScript(tm)."

| Compatibility: | BSF 2.2 and above |
| --- | --- |
| URL: | <http://www.beanshell.org/> |
| Contact: | [project mailing lists](http://www.beanshell.org/contact.html) |
| License: | Dual Licensed: [Sun Public License](http://www.opensource.org/licenses/sunpublic.php) / [Gnu Lesser Public License](http://www.opensource.org/licenses/lgpl-license.php) |

<a id="projects--groovy"></a>

### Groovy

"Groovy is a powerful scripting language for the JVM which compiles down to Java bytecode and implements
various high level features for Java developers such as dynamic typing, powerful closures for neat object navigation, native syntax for Maps and Lists, operator overloading, new extended JDK methods, AOP hooks and auto-boxing.
Groovy also features a markup language for working with structured data (XML, DOM, SAX, Ant tasks, Swing etc).
"

| Compatibility: | BSF 2.3 and above |
| --- | --- |
| URL: | <http://groovy.codehaus.org/> |
| Contact: | [Mailing lists](http://groovy.codehaus.org/mail-lists.html) |
| License: | [BSD](http://www.opensource.org/licenses/bsd-license.php) (Apache-like) License |

<a id="projects--groovy-monkey"></a>

### Groovy Monkey

"[Groovy Monkey](http://groovy.codehaus.org/Groovy+Monkey) is a
dynamic scripting tool for the Eclipse Platform/RCP that enables you to
automate tasks, explore the Eclipse API and engage in rapid prototyping.
Groovy Monkey makes use of the BSF framework to allow users to write scripts
in Beanshell, Groovy or the Ruby language. If you have ever wanted to be
able to quickly experiment with or write simple automation tasks for the
Eclipse environment, this is the tool for you.
"

| Compatibility: | BSF 2.3 and above |
| --- | --- |
| URL: | <http://groovy.codehaus.org/Groovy+Monkey> |

<a id="projects--jacl-tcl"></a>

### Jacl (Tcl)

"Jacl, which stands for Java Command Language, is a Java implementation
of TCL 8.x."

| Compatibility: | Jacl 1.2.6, with BSF 2.2 and above |
| --- | --- |
| URL: | <http://tcl.activestate.com/software/java/> |
| Contact: | [Tcl/Java Mailing Lists](http://tcljava.sourceforge.net/docs/website/mail.html) |
| License: | Sun, ORO, and UCB licenses (see source) |

<a id="projects--jexl"></a>

### JEXL

"Java Expression Language (JEXL) is an expression language engine which
can be embedded in applications and frameworks."

| Compatibility: | Commons JEXL 1.1, with BSF version 2.4 |
| --- | --- |
| URL: | <http://commons.apache.org/jexl/> |
| Contact: | [Commons Mailing Lists](http://commons.apache.org/jexl/mail-lists.html) |
| License: | [Apache v2.0](http://www.opensource.org/licenses/apache2.0.php) |

<a id="projects--javascript-rhino-javascript-in-java"></a>

### JavaScript/Rhino (JavaScript in Java)

"JavaScript/Rhino is an open-source implementation of JavaScript written
entirely in Java. It is typically embedded into Java applications
to provide scripting to end users."

| Compatibility: | Rhino with BSF 2.4 and above, early versions of Rhino (up to and including version 1.5.3) with BSF 2.3 |
| --- | --- |
| URL: | <http://www.mozilla.org/rhino/> |
| Contact: | [Rhino Contact Page](http://www.mozilla.org/rhino/help.html) |
| License: | [Mozilla Public License, version 1.1](http://www.opensource.org/licenses/mozilla1.1.php) |

<a id="projects--jlog-prolog-in-java"></a>

### JLog (PROLOG in Java)

"Prolog is a logic-oriented language based on predicate calculus. While it is not
really a scripting language, there is a range of problems that are much easier to
express in it than in Java, and for these cases a Prolog BSF engine comes in handy.
It is also useful for adding a GUI to Prolog programs.
The underlying Prolog interpreter is JLog, which can be run as an applet, an application
or embedded through an API, and can be found at <http://sf.net/projects/jlogic/>."

| Compatibility: | BSF 2.3 and above |
| --- | --- |
| URL: | <http://www.ulfdittmer.com/jlog/> |
| Contact: | [Ulf Dittmer](mailto:udittmer@yahoo.com) |
| License: | [GPL](http://www.opensource.org/licenses/gpl-license.php) (same as JLog itself) |

<a id="projects--jruby-ruby-in-java"></a>

### JRuby (Ruby in Java)

"JRuby is a pure Java implementation of the Ruby interpreter, being developed by Jan Arne Petersen and others."

| Compatibility: | BSF 2.2 and above |
| --- | --- |
| URL: | <http://jruby.sourceforge.net/> |
| Contact: | [Jan Arne Petersen](mailto:jpeterson@uni-bonn.de) |
| License: | dual [GPL](http://www.opensource.org/licenses/gpl-license.php)/[LGPL](http://www.opensource.org/licenses/lgpl-license.php) |

<a id="projects--judoscript"></a>

### JudoScript

"Judoscript is a 3GL-and-4GL; it retains 3GL's powerful
programmability, and extends its reach into many of today's popular
applications areas with 4GL approach (figuratively, "WYSIWYG
programming"), making their uses easy, effective and elegant."

| Compatibility: | BSF 2.2 and above |
| --- | --- |
| URL: | <http://www.judoscript.com/> |
| Contact: | [James Huang](mailto:judoscript@hotmail.com) |
| License: | [LGPL](http://www.opensource.org/licenses/lgpl-license.php) |

<a id="projects--jython-python-in-java"></a>

### Jython (Python in Java)

"Jython is an implementation of the high-level, dynamic, object-oriented language Python written in 100% Pure Java, and
seamlessly integrated with the Java platform. It thus allows you
to run Python on any Java platform."

| Compatibility: | Jython 2.1, with BSF 2.2 and above |
| --- | --- |
| URL: | <http://www.jython.org/> |
| Contact: | [Jython Mailing lists](http://sourceforge.net/mail/?group_id=12867) |
| License: | Jython Software License |

<a id="projects--netrexx-rexx-like-java"></a>

### NetRexx (Rexx-like Java)

"NetRexx is a *human-oriented* programming language which makes
writing and using Java classes quicker and easier than writing in
Java."

| Compatibility: | NetRexx 2.0.2, with BSF 2.2 and above |
| --- | --- |
| URL: | <http://www2.hursley.ibm.com/netrexx/> |
| Contact: | [NetRexx 2 mailing list](http://www-306.ibm.com/software/awdtools/netrexx/mailinglist.html) |
| License: | IBM License Agreement for IBM Employee-Written Software |

<a id="projects--objectrexx-rexx"></a>

### ObjectRexx/Rexx

"Open Object Rexx (ooRexx, <http://www.ooRexx.org>) is a free
and opensource language, which was originally developed by IBM, and made available for opensourcing and further
developing it.
The non-profit SIG Rexx Language Association (<http://www.RexxLA.org>)
received the source code from IBM at the end of 2004 and released an opensource version
to the community in the spring of 2005.
[The BSF engine for ooRexx (BSF4ooRexx)](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/)  comes with an ooRexx wrapper
program (BSF.CLS) which camouflages Java as ooRexx, easying programming
considerably (e.g. no need for type information/casting)."

| Relates to: | *ooRexx* |
| --- | --- |
| Compatibility: | BSF 2.3 and above |
| Contact: | [President of RexxLA](mailto:president@rexxla.org) |
| URL: | <http://www.ooRexx.org> |
| License: | [IBM's opensource license CPL v 1.0](http://www.opensource.org/licenses/cpl1.0.php) (hence you can bundle this freely with commercial software as well) |
| Relates to: | *BSF4ooRexx* |
| Compatibility: | BSF 2.3 and above |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/> (temporary home) |
| (future) URL: | [http://bsf4rexx.sourceforge.net](http://bsf4rexx.sourceforge.net/) (planned home) |
| Contact: | [Rony G. Flatscher](mailto:ronyf@apache.org) |
| License: | [Apache v2.0](http://www.opensource.org/licenses/apache2.0.php) (hence you can bundle this freely with commercial software as well) |

<a id="projects--objectscript"></a>

### ObjectScript

"ObjectScript is a general purpose object-oriented programming language. It is designed to
be simple to learn, easy to use, yet still powerful, combining the convenience of an
interactive interpreter with many of the features of Java, plus operator overloading, regular expressions, closures, XML-RPC support, etc. And a behind the scenes compiler
compiles script code to JVM bytecode for faster execution."

| Compatibility: | BSF 2.3 and above |
| --- | --- |
| URL: | <http://objectscript.sourceforge.net/> |
| Contact: | [Rob Clark](mailto:rob@ti.com) |
| License: | [LGPL](http://www.opensource.org/licenses/lgpl-license.php) |

<a id="projects--xalan-xslt"></a>

### Xalan/XSLT

"Xalan-Java is an XSLT processor for transforming XML documents into
HTML, text, or other XML document types. It implements the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath). It can be used from the command line, in an applet
or a servlet, or as a module in other program.

*Hint:*
Starting with Sun's Java 1.4SE a W3C compliant set of classes for XSLT is part
of the runtime environment.", *however*, with other versions of
Java or newer versions of Xalan distributions you *may* need to explicitly extract the
archive
*xalan.jar* and put it into the CLASSPATH
environment variable or alternatively, copy it into the Java *endorsed* or
*ext*ension directory of your
Java distribution (usually in $(JAVA\_JRE\_HOME)/jre/lib/{endorsed|ext}). The download
site of Xalan (Java version) is at: <http://xml.apache.org/xalan-j/downloads.html>
(You can determine quite easily whether you need to do that: just try to run the xslt sample
of the BSF distribution. If you encounter the error  'Could not compile stylesheet', then
you need to explicitly supply the xalan.jar from the Xalan distribution.)

| Compatibility: | Xalan 2.2 and above (XSLT), with BSF 2.3 and above |
| --- | --- |
| URL: | <http://xml.apache.org/xalan-j/index.html> |
| Contact: | [Apache XML Project "Get Involved" page](http://xml.apache.org/overview.html) |
| License: | [Apache v2.0](http://www.opensource.org/licenses/apache2.0.php) |

---

<a id="resources"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/resources.html -->

<!-- page_index: 6 -->

<a id="resources--faqs"></a>

## FAQs

<a id="resources--at-bsf-s-website"></a>

### At BSF's website

Starting with the release of BSF 2.3 the BSF's FAQ is
bundled with the distribution, the most recent version can
always be found at the website.

FAQ:

[http://commons.apache.org/bsf/faq.html](#faq)

<a id="resources--articles-and-presentations"></a>

## Articles and Presentations

The following sections list articles and presentations written about BSF. If
you've written something that should be included, please post it to one
of the mailing lists.

<a id="resources--articles"></a>

## Articles

<a id="resources--using-javascript-with-ant"></a>

### Using JavaScript with Ant

A tutorial about using BSF, JavaScript, and XSLT with Ant.

| Author: | Dylan Schiemann |
| --- | --- |
| URL: | <http://www.sitepen.com/ant/javascript.html> |

<a id="resources--script-javabeans-with-the-bean-scripting-framework"></a>

### Script JavaBeans with the Bean Scripting Framework

Add scripts to your JavaBeans or JavaBeans to your scripts

| Author: | [Mark Johnson](http://www.javaworld.com/feedback) |
| --- | --- |
| URL: | <http://www.javaworld.com/javaworld/jw-03-2000/jw-03-beans.html> |

<a id="resources--xalan-java-extensions"></a>

### Xalan-Java Extensions

For extensions written in languages other than Java, Xalan-Java uses
the Bean Scripting Framework (BSF), an architecture for incorporating
scripting into Java applications and applets.

| Author: | [Apache XML Xalan developers](http://xml.apache.org/xalan-j/index.html) |
| --- | --- |
| URL: | <http://xml.apache.org/xalan-j/extensions.html> |

<a id="resources--using-javascript-rhino-with-bsf-and-apache"></a>

### Using JavaScript/Rhino with BSF and Apache

The Bean Scripting Framework (or BSF) was originally developed by
IBM and now published as open source. It provides a framework for
using a number of scripting languages with Java. Rhino is one of the
supported languages.

| Author: | [Norris Boyd](mailto:nboyd@atg.com) |
| --- | --- |
| URL: | <http://www.mozilla.org/rhino/bsf.html> |

<a id="resources--extending-your-applications-with-bean-scripting-framework"></a>

### Extending Your Applications with Bean Scripting Framework

BSF brings standard support for many programming languages to the
Java platform.

| Author: | [Rick Hightower](mailto:rick_m_hightower@hotmail.com) |
| --- | --- |
| URL: | <http://jdj.sys-con.com/read/36422.htm> |

<a id="resources--embed-judoscript-in-java"></a>

### Embed JudoScript in Java

Two ways to embed JudoScript in Java: through its support of Bean
Scripting Framework and its own, simpler engine interface.

| Author: | [James Huang](mailto:judoscript@hotmail.com) |
| --- | --- |
| URL: | <http://www.judoscript.com/articles/embed.html> |

<a id="resources--jruby-documentation"></a>

### JRuby Documentation

Using JRuby with BSF

| Author: | [Jan Arne Petersen](mailto:jpeterson@users.sourceforge.net) |
| --- | --- |
| URL: | <http://jruby.sourceforge.net/doc-bsf.shtml> |

<a id="resources--embed-objectscript-in-java"></a>

### Embed ObjectScript in Java

ObjectScript can be embedded either through it's own native interface, or through BSF.

| Author: | [Rob Clark](mailto:rob@ti.com) |
| --- | --- |
| URL: | <http://objectscript.sourceforge.net/?docs/embedding.html> |

<a id="resources--the-augsburg-version-of-bsf4rexx"></a>

### The Augsburg Version of BSF4Rexx

["BSF4ooRexx", the Bean Scripting Framework for Rexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/), allows one to use the Rexx
and Object Rexx programming languages with the open source Bean Scripting
Framework (BSF) which enables Java programs to easily invoke scripts and
programs written in another language than Java. This article introduces the
"Augsburg version" of BSF4Rexx which incorporates numerous changes and as a
main feature the ability to start Java from Rexx programs. This way all of Java can
be viewed as a huge external Rexx function library from the perspective of Rexx, available on any platform Rexx is available. This paper gives a bird eyes view of
BSF4Rexx concentrating on this latter ability and introducing Rexx programmers
informally to Java and to the most important object-oriented terms such that the
unacquainted Rexx and Object Rexx programmer becomes able to read the Java
documentation and as a result apply BSF4Rexx to allow (Object) Rexx to use and
drive Java.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/orx14/orx14_bsf4rexx-av.pdf> |

<a id="resources--camouflaging-java-as-object-rexx"></a>

### Camouflaging Java as Object REXX

The Java runtime environment (JRE) is available for practical every operating system in
the world and installed on most computers. The functionality of the Java classes that
build the JRE has been constantly updated to reflect the advances in the software
technology thereby making bleeding edge software concepts available to Java
programmers. For that reason the JRE has been an attractive target for making its
functionality available to Rexx programs in the form of external Rexx functions, notably
with the
["BSF4ooRexx" (Bean Scripting Framework for ooRexx)](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/)
(old: ["BSF4Rexx"
(Bean Scripting Framework for Rexx)](http://wi.wu-wien.ac.at/rgf/rexx/bsf4rexx/current/)) technology introduced at
past International Rexx Symposiae. BSF4[oo]Rexx supplies a procedural interface to Java, such that Rexx programs need to simply use CALL-statements or function-calls to
bridge into Java.

As Object Rexx is object-oriented an object-oriented interface to Java may be desirable
as this may reduce the complexity to refer to Java. This article introduces and
discusses the architecture and the implementation of Object Rexx wrapper classes that
hide the procedural interfaces from Object Rexx programmers by embedding the
procedural interfaces of BSF4ooRexx in Object Rexx methods, allowing e.g. the
invocation of Java methods transparently via Object Rexx messages.

Among other things it will be demonstrated, how Java objects are created and sent
messages to interactively via a keyboard using the Rexx "rexxtry.rex" program in a
command line interface.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/orx15/2004_orx15_bsf-orx-layer.pdf> |

<a id="resources--automating-openoffice.org-with-oorexx:-architecture-gluing-to-rexx-using-bsf4rexx"></a>

### Automating OpenOffice.Org with ooRexx: Architecture, Gluing to Rexx using BSF4Rexx

The opensource Microsoft Office clone ["OpenOffice"](http://www.OpenOffice.org) is available on
multiple plat-forms, from Windows, over Linux to OS/2. It can read/write
Microsoft office file-formats, such as Word, Excel or PowerPoint. Its
scripting architecture is radically dif-ferent from what Microsoft has
come up with and appears to be more systematic, al-though there is a
rather steep learning curve to it.

The architecture of OpenOffice is exposed via the UNO (Uniform Network
Objects) interface, which allows C, C++ and Python programs to exploit
OpenOffice. On the Windows platform there is an ActiveX/OLE-interface
supplied, such that ActiveX-script languages like VBS, JS, as well as
[ooRexx](http://www.ooRexx.org) can be used for scripting purposes, but such programs will lock-in
the company into the Windows operating system.

For the programming language Java, OpenOffice supplies a Java interface to
UNO, which can also be exploited in rather innovative ways, e.g. using
[BSF4ooRexx (Bean Scripting Framework for ooRexx)](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/) to bridge between OpenOffice
and ooRexx. Such a solution would allow for the driving/scripting of
OpenOffice in a platform independent way, allowing customers to eventually
break out of possibly undesired lock-ins (e.g. Windows operating system
and/or ActiveX/OLE-technology).

This article gives a conceptual overview of OpenOffice UNO and explains in
detail how UNO can get instantiated and interfaced with by ooRexx.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/orx16/2005_orx16_Gluing2ooRexx_OOo.pdf> |

<a id="resources--automating-openoffice.org-with-oorexx:-oorexx-nutshell-examples-for-write-and-calc"></a>

### Automating OpenOffice.Org with ooRexx: ooRexx, Nutshell Examples For Write and Calc

This article will give numerous little "nutshell" examples of driving [OpenOffice.org](http://www.OpenOffice.org) via [ooRexx](http://www.ooRexx.org). All the examples will run unaltered under Linux and Windows.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/orx16/2005_orx16_NutShell_OOo.pdf> |

<a id="resources--automating-subversion-an-open-object-rexx-approach"></a>

### Automating Subversion - An Open Object Rexx Approach

This work explores and implements scripts which allow driving the source
code version control system "subversion" from [ooRexx](http://www.ooRexx.org). As there are Java
implementations for subversion it is possible to employ [BSF4ooRexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/) to drive
the application.

| Author: | Bernhard Hoisl |
| --- | --- |
| URL (Text):: | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2005/200507_Subversion_Hoisl/200507_AutomatingSubversion.pdf> |
| URL\_(Examples): | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2005/200507_Subversion_Hoisl/200507_examples.zip> |

<a id="resources--openoffice.org-automation:-object-model-scripting-languages-nutshell-examples"></a>

### OpenOffice.org Automation: Object Model, Scripting Languages, "Nutshell"-Examples

This work explores and demonstrates how [OpenOffice.org](http://www.OpenOffice.org) can be automated
via Object REXX by using the Java programming interfaces of OpenOffice.org
and [BSF4ooRexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/).

This time specific [ooRexx](http://www.ooRexx.org) support for OpenOffice (module "UNO.CLS" by
Rony G. Flatscher, derived from OOO.CLS which is based on the Java
interface to the UNO component technology of OpenOffice) is used, which
cuts down the necessary code dramatically and makes those programs easy
ledgible and understandable (looks almost like pseudo-code).

| Author: | Andreas Ahammer |
| --- | --- |
| URL (Text):: | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2005/200511_OOo-Ahammer/200511_OOoAutomation.pdf> |
| URL\_(Examples): | http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2005/200511\_OOo-Ahammer/20051106\_examples.zip |

<a id="resources--openoffice.org-automatisation-with-object-rexx"></a>

### OpenOffice.org Automatisation with Object Rexx

This work builds on the work of Mr. Ahammer (above). It explores and
demonstrates how [OpenOffice.org](http://www.OpenOffice.org) can be automated via Object REXX by using
the Java programming interfaces of OpenOffice.org and [BSF4ooRexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/).

This time the OpenOffice.org 2.0 scripting framework (written in Java) is
used, which allows to deploy the scripts as OpenOffice.org/StarOffice
macros, in a platform independent manner.

| Author: | Martin Burger |
| --- | --- |
| URL (Text): | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2006/200605_Burger/Bakk_Arbeit_Burger20060519.pdf> |
| URL\_(Examples): | http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2006/200605\_Burger/Bakk\_Arbeit\_BurgerExamples\_All\_20060519.zip |

<a id="resources--bsf4rexx-and-openoffice.org-nutshell-examples"></a>

### BSF4Rexx and OpenOffice.org Nutshell-Examples

This seminar paper introduces the easy to learn syntax of [Open Object Rexx
(ooRexx)](http://www.ooRexx.org) and the [BSF4ooRexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/) external Rexx function package, which allows the
weakly typed language ooRexx to interface with (strictly typed) Java.

It defines and explains numerous small (nutshell) examples where the
functionality of Java class libraries is used for ooRexx. In addition, the students create examples for automating/scripting the opensource
office package [OpenOffice.org (OOo)](http://www.OpenOffice.org) in an openplatform way using the OOo
Java interface for that purpose.

Some of the OpenOffice related nutshell examples can be retrieved from the
official OOo ["Snippet"](http://codesnippets.services.openoffice.org/) homepage.

| Author: | Gerhard Görlich, Åsmund Realfsen, David Spanberger |
| --- | --- |
| URL (Text): | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/Seminararbeiten/2006s_wu/20060628_BSF4RexxSnippets_version_4.pdf> |
| URL\_(Examples): | http://wi.wu-wien.ac.at/rgf/diplomarbeiten/Seminararbeiten/2006s\_wu/20060628\_BSF4RexxSnippets\_code.zip |

<a id="resources--openoffice.org-automatisation-with-object-rexx-calc"></a>

### OpenOffice.org Automatisation with Object Rexx (Calc)

This paper gives an introduction to the [OpenOffice.org](http://www.OpenOffice.org) architecture and
explains how the OpenOffice.org Calc component can be automated by using
the scripting language [Open Object Rexx (ooRexx)](http://www.ooRexx.org). This components are
open sourced and can be downloaded free of charge from the internet.

The paper is divided into a theoretical and a practical part. In the
theoretical part, the main components, ooRexx, OpenOffice.org and the Bean
Scripting Framework for ooRexx, will be described and it explains how the
single components can work together. At the end of this part you can find
an short installation guide, which shows you how to retrieve and install
the single components. The practical part provides some nutshell
examples, that should demonstrate how the OpenOffice.org Calc component
can be automated. The concluding part should give a short summary of the
paper.

| Author: | Michael Hinz |
| --- | --- |
| URL (Text): | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2006/200607_Hinz/20060712_OOo_calc_automation.pdf> |
| URL\_(Examples): | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2006/200607_Hinz/20060629_OOo_calc_examples.zip> |

<a id="resources--oorexx-snippets-for-openoffice.org-writer"></a>

### ooRexx Snippets for OpenOffice.org Writer

This paper deals with the use of [ooRexx](http://www.ooRexx.org) as a scripting language for
automation of [OpenOffice.org](http://www.OpenOffice.org) Writer.

At first, there will be an introduction to the technical requirements, which include the software that has to be installed. Concerning ooRexx
there is also a sub chapter about its syntax and common instructions, to
give a feeling for this programming language.

The next chapter is about the architectural approach behind ooRexx and
OpenOffice.org. It is described how OpenOffice.org can be accessed using
ooRexx.

Chapter four is a small installation guide, which shows how to set up the
different software programmes and configure them correctly. Chapter five
and six show how the automation of OpenOffice.org Writer can be done.
Small snippets, which are code examples, demonstrate different tasks. At
last the conclusion gives a small summary and an outlook.

| Author: | Matthias Prem |
| --- | --- |
| URL (Text): | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2006/200607_Prem/20060724_ooRexxSnippetsOOoWriter_2.1_odt.pdf> |
| URL\_(Examples): | <http://wi.wu-wien.ac.at/rgf/diplomarbeiten/BakkStuff/2006/200607_Prem/ooRexxSnippetsOOoWriter_oorexx_snippets.zip> |

<a id="resources--presentations"></a>

## Presentations

<a id="resources--an-introduction-to-bsf"></a>

### An Introduction to BSF

This article is a short introduction into the basic
concepts of BSF. To be presented at ApacheCon 2002.

| Author: | [Victor Orlikowski](mailto:victor.j.orlikowski@alumni.duke.edu) |
| --- | --- |
| URL: | <http://www.dulug.duke.edu/~vjo/papers/ApacheCon_US_2002/> |

<a id="resources--the-vienna-version-of-bsf4rexx"></a>

### The Vienna Version of "BSF4Rexx"

This presentation introduces the "The Vienna Version of [BSF4ooRexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4orexx/current/)", International Rexx Symposium 2006, Austin, Texas.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/orx17/2006_orx17_BSF_ViennaEd.pdf> |

<a id="resources--uno.cls:-an-open-object-rexx-module-for-universal-network-objects"></a>

### UNO.CLS: An (Open) Object Rexx Module for Universal Network Objects

"The Vienna Version of [BSF4ooRexx](http://wi.wu-wien.ac.at/rgf/rexx/bsf4oorexx/current/)", allows open-platform scripting of
[OpenOffice.org (OOo)](http://www.OpenOffice.org) with the help of BSF. This is done by using the Java APIs of OOo via BSF to
address the OOo "Universal Network Objects (UNO)" components, which are used to assemble OOo.
Presented at the International Rexx Symposium 2006, Austin, Texas.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/orx17/2006_orx17_UNO.pdf> |

<a id="resources--bsf4rexx:-camouflaging-java"></a>

### BSF4Rexx: Camouflaging Java

This presentation shows what one is able to do with BSF as well, presented at [ApacheCon Asia 2006](http://asia.apachecon.com), Sri Lanka.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://asia.apachecon.com/wp-content/presentations/ApacheConAsia2006-08-16-Flatscher-BSF4Rexx.pdf> |

<a id="resources--the-2009-edition-of-bsf4rexx"></a>

### The 2009 Edition of BSF4Rexx

With the advent of the ooRexx 4.0 in the summer of 2009 a new, fully object-oriented kernel has been made available, which allows
to close an important gap between ooRexx and Java, namely synchroneous callbacks from Java into ooRexx and allowing Java
methods to be implemented in Rexx.

The article ["The 2009 Edition of BSF4Rexx"](http://wi.wu.ac.at/rgf/rexx/orx20/2009_orx20_BSF4Rexx-20091031-article.pdf)
gives an overview of the new features made available in the
BSF4*oo*Rexx package (note the change in the name of the package from
"BSF4Rexx" to "BSF4*oo*Rexx"). Self-explanatory
nutshell examples are used to stress the discussed features.

| Author: | [Rony G. Flatscher](mailto:rony@apache.org) |
| --- | --- |
| URL: | <http://wi.wu-wien.ac.at/rgf/rexx/orx17/2006_orx17_BSF_ViennaEd.pdf> |

---

<a id="problems"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/problems.html -->

<!-- page_index: 7 -->

<a id="problems--having-problems"></a>

## Having Problems?

This page details some steps you can take to try and resolve
any problems you may be having with BSF. If you find you can't
resolve the problem, then this page will help you collect some of
the relevant information to provide in a bug report. This information
will help the BSF developers understand and resolve the problem.
Of course, not all the steps here will make sense for every problem
you may encounter - these are just some suggestions to point
you in the right direction.

<a id="problems--read-the-manual"></a>

### Read the Manual

The first step to take when you have a problem with BSF is to read
the [manual](#manual) entry for the task or
concept that is giving you trouble. In particular, check the
meaning of a task's attributes and nested elements. Perhaps an
attribute is available that would provide the behavior you require.
If you have problems with the manual itself, you can submit a
documentation bug report (see below) to help us improve the BSF
documentation.

<a id="problems--examine-trace-output"></a>

### Examine Trace Output

If you're still having a problem, the next step is to try and
gather additional information about what BSF is doing.

The trace output from a BSF run is helpful in determining
causes of failure, and is useful in bug reports.

<a id="problems--has-it-been-reported"></a>

### Has It Been Reported?

It is
possible that someone else has reported the issue. It is time to
look at the
[Apache Bug Database (JIRA)](http://issues.apache.org/jira/browse/BSF). This system is easy to use, and it will
let you search the
[currently open](https://issues.apache.org/jira/secure/IssueNavigator.jspa?mode=hide&requestId=12312131) and resolved bugs to see if your problem has
already been reported. If your problem has been reported, you can
see whether any of the developers have commented, suggesting
workarounds, or the reason for the bug, etc. Or you may have
information to add (see about creating and modifying bug reports
below), in which case, go right ahead and add the information.
If you don't have any additional information, you may just want
to vote for this bug, and perhaps
add yourself to the CC list to follow the progress
of this bug.

<a id="problems--filing-a-bug-report"></a>

### Filing a Bug Report

By this time, you may have decided that there is an unreported
bug in BSF. You have a few choices at this point. You can send
an email to the bsf-user mailing list
to see if
others have encountered your issue and find out how they may
have worked around it. If after some discussion, you feel it
is time to create
a bug report, this is a simple operation in the bug database.
Please try to provide as much information as possible in order
to assist the developers in resolving the bug. Please try to enter
correct values for the various inputs when creating the bug, such
as which version of BSF you are running, and on which platform, etc. Once the bug is created, you can also add attachments to
the bug report.

What information should you include in your bug report? The
easiest bugs to fix are those that are most easily reproducible, so it is really helpful if you can produce a small test case that
exhibits the problem. In this case, you would attach the build file
and any other files necessary to reproduce the problem, probably
packed together in an archive. If you can't produce a test case, you should try to include a snippet from your build file and the
relevant sections from the verbose or debug output from BSF. Try
to include the header information where BSF states the version, the OS and VM information, etc. As debug output is likely to be
very large, it's best to remove any output that is not
relevant. Once the bug is entered into the bug database, you
will be kept informed by email about progress on the bug. If
you receive email asking for further information, please try to
respond, as it will aid in the resolution of your bug.

<a id="problems--asking-for-an-enhancement"></a>

### Asking for an Enhancement

Sometimes, you may find that BSF just doesn't do what you need it
to. It isn't a bug, as such, since BSF is working the way it is
supposed to work. Perhaps it is some additional functionality for
a task that hasn't been thought of yet, or maybe a completely new
task. For these situations, you will
want to raise an *enhancement request*. Enhancement requests
are managed using the same Apache Bug Database described above.
These are just a different type of bug report. If you look in the
bug database, you will see that one of the severity settings for
a bug is "Enhancement". Just fill the bug report in, set the severity of the bug to "Enhancement", and
state in the description how you would like to have BSF enhanced.
Again, you should first check whether there are any existing
enhancment requests that cover your needs. If so, just add your
vote to these.

<a id="problems--fixing-the-bug"></a>

### Fixing the Bug

If you aren't satisfied with just filing a bug report, you can
try to find the cause of the problem and provide a fix yourself.
The best way to do that is by working with the latest code from SVN.
Alternatively, you can work with the source code available from the
source distributions. If you
are going to tackle the problem at this level, you may want to
discuss some details first on the bsf-dev
mailing list. Once you have a fix for the problem, you may submit
the fix as a *patch* to either the
bsf-dev mailing
list, or enter the bug database as described above and attach the
patch to the bug report. Using the bug database has the advantage
of being able to track the progress of your patch.

If you have a patch to submit and are sending it to the
bsf-dev mailing list, prefix "[PATCH]"
to your message subject. Please include any relevant bug numbers.
Patch files should be created with the -u
option of the
diff or cvs diff command. For
example:
diff -u Javac.java.orig Javac.java > javac.diffs
or, if you have source from SVN:
svn diff Javac.java > javac.diffs
Note: You should give your patch files meaningful names.
This makes it easier for developers who need to apply a number
of different patch files.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/project-info.html -->

<!-- page_index: 8 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Software Foundation provides support for the Apache community of open-source software projects. The Apache projects are characterized by a collaborative, consensus based development process, an open and pragmatic software license, and a desire to create high quality software that leads the way in its field. We consider ourselves not simply a group of projects sharing a server, but rather a community of developers and users. |
| [Continuous Integration](#integration) | This is a link to the definitions of all continuous integration processes that builds and tests code on a frequent, regular basis. |
| [Dependencies](https://commons.apache.org/proper/commons-bsf/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Distribution Management](https://commons.apache.org/proper/commons-bsf/distribution-management.html) | This document provides informations on the distribution management of this project. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Mailing Lists](https://commons.apache.org/proper/commons-bsf/mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Plugin Management](https://commons.apache.org/proper/commons-bsf/plugin-management.html) | This document lists the plugins that are defined through pluginManagement. |
| [Project License](https://commons.apache.org/proper/commons-bsf/license.html) | This is a link to the definitions of project licenses. |
| [Project Plugins](https://commons.apache.org/proper/commons-bsf/plugins.html) | This document lists the build plugins and the report plugins used by this project. |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Project Team](https://commons.apache.org/proper/commons-bsf/team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Repository](https://commons.apache.org/proper/commons-bsf/source-repository.html) | This is a link to the online source repository that can be viewed via a web browser. |

---

<a id="integration"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/integration.html -->

<!-- page_index: 9 -->

<a id="integration--overview"></a>

## Overview

This project uses [Continuum](http://maven.apache.org/continuum/).

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

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/issue-tracking.html -->

<!-- page_index: 10 -->

<a id="issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
http://issues.apache.org/jira/browse/BSF
```

---

<a id="project-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-bsf/project-summary.html -->

<!-- page_index: 11 -->

<a id="project-summary--project-summary"></a>

## Project Summary

<a id="project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons BSF (Bean Scripting Framework) |
| Description | The Apache Software Foundation provides support for the Apache community of open-source software projects. The Apache projects are characterized by a collaborative, consensus based development process, an open and pragmatic software license, and a desire to create high quality software that leads the way in its field. We consider ourselves not simply a group of projects sharing a server, but rather a community of developers and users. |
| Homepage | <http://commons.apache.org/bsf> |

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
| GroupId | bsf |
| ArtifactId | bsf |
| Version | 2.5.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.3 |

---
