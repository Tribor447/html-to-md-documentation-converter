# Apache Anakia - Anakia

## Navigation

- Anakia
  - [General](#index)
- Developers
  - [Changes](#changes-report)
  - [Resolved Issues](#jira-report)
- Project Documentation
  - [Project Reports](#project-reports)
    - [Changes Report](#changes-report)
    - [Developer Activity](#dev-activity)
    - [File Activity](#file-activity)
    - [Jira Report](#jira-report)
    - [Tag List](#taglist)

## Content

<a id="index"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/ -->

<!-- page_index: 1 -->

<a id="index--what-is-anakia"></a>

## What Is Anakia?

Essentially an XML transformation tool, Anakia uses [JDOM](http://www.jdom.org) and [Velocity](http://velocity.apache.org/) to transform
XML documents into the format of your choice. It provides an alternative to
using Ant's <style> task and
[XSL](http://xml.apache.org/xalan/) to process XML
files.

The basic model that AnakiaTask uses is pretty straightforward :

1. Parse your XML into a JDOM Document:


```

SAXBuilder builder;
Document root = null;

try
{
    builder = new SAXBuilder(
        "org.apache.xerces.parsers.SAXParser" );
    root = builder.build( file );
}
catch( Exception E )
{
    System.out.println( ...  );
}
```

2. Stuff the Document (or root Element) into the context:


```

context.put("root", root );
```

3. Render a template using Velocity. Within the template, one
   can use JDOM's methods to access the data contained in the
   XML document.

Anakia is potentially easier to learn than XSL, but it maintains a
similar level of functionality. Learning cryptic <xsl:> tags
is unnecessary; you only need to know how to use the provided
Context objects, JDOM, and Velocity's simple directives. Anakia
seems to perform much faster than Xalan's XSL processor at creating
pages. (23 pages are generated in 7-8 seconds on a PIII 500mhz
running Win98 and JDK 1.3 with client Hotspot. A similar system
using Ant's <style> task took 14-15 seconds -- nearly a 2x
speed improvement.)

Anakia -- intended to replace Stylebook, which was originally used
to generate simple, static web sites in which all pages had the same
look and feel -- is great for documentation/project web sites, such
as the sites on [www.apache.org](http://www.apache.org/)
and [jakarta.apache.org](http://jakarta.apache.org). As it
is more targeted to a specific purpose, it does not provide some of
XSL's "extra" functionality.

The example in the `examples/anakia` directory
provides a good introduction to Anakia. You should find it quite
simple to use.

Anakia creates a Context, which contains a JDOM Document object of
the .xml page, as well as an (optional) JDOM Document object of your
project.xml page. In addition to the project.xml based context, additional
xml contexts can be added through context nested elements. The
.vsl page is executed (using Velocity) with the Context. You can then
navigate your .xml file and pull information out of it by simply executing
methods on the JDOM Document object.

Anakia is being used to create the documentation for this
website. You can view the source for this website in the "xdocs" folder
in the Velocity source distribution.

<a id="index--installation-example"></a>

## Installation/Example

Before reviewing the `examples/anakia` directory, you must [build Velocity](https://velocity.apache.org/engine/devel/build.html).

After building Velocity, `cd` into the
`examples/anakia/build` directory and run 'ant'.

Output from running ant, in this case HTML files, is placed
into the `examples/anakia/docs/` directory.

The `examples/anakia/xdocs/` directory has all of the
.xml source code. The xdocs/stylesheets directory contains the .vsl
file, in which most of the magic happens. Understanding [Velocity Template Language](https://velocity.apache.org/engine/devel/user-guide.html) and
[JDOM](http://www.jdom.org/) is
necessary to understand how the .vsl file works.

<a id="index--how-does-it-work"></a>

## How Does It Work?

Anakia is an Ant task that executes from an Ant build file. The
build file looks something like this:

```

    <project name="build-site" default="docs" basedir=".">
    <property name="docs.src" value="../xdocs"/>
    <property name="docs.dest" value="../docs"/>

    <target name="prepare">
        <available classname="org.apache.anakia.AnakiaTask"
        property="AnakiaTask.present"/>
    </target>

    <target depends="prepare" name="prepare-error"
                            unless="AnakiaTask.present">
        <echo>
            AnakiaTask is not present! Please check to make sure that
            velocity.jar is in your classpath.
        </echo>
    </target>

    <target name="docs" depends="prepare-error"
                        if="AnakiaTask.present">
        <taskdef name="anakia"
                 classname="org.apache.anakia.AnakiaTask"/>
        <anakia basedir="${docs.src}" destdir="${docs.dest}/"
             extension=".html" style="./site.vsl"
             projectFile="./stylesheets/project.xml"
             excludes="**/stylesheets/**"
             includes="**/*.xml"
             lastModifiedCheck="false"
             velocityPropertiesFile="velocity.properties">
        </anakia>

        <copy todir="${docs.dest}/images" filtering="no">
            <fileset dir="${docs.src}/images">
                <include name="**/*.gif"/>
                <include name="**/*.jpeg"/>
                <include name="**/*.jpg"/>
            </fileset>
        </copy>
    </target>
</project>
```

| Name | Description |
| --- | --- |
| basedir | Specifies the path to the directory location of your .xml files. |
| destdir | Specifies the path to the directory where the output files should go. |
| extension | This is the extension that is appended to the end of your .xml file. For example, with an extension of ".html", index.xml would be converted into index.html. By default, the extension is .html. |
| style | This is the path (relative to Velocity's template.loader.1.template.path) to the VelocityStyleTemplate to process. This file is the equivalent to the .xsl file in Ant's style task. |
| projectFile | This is the path to a "project" file. This file is an XML file that can be used as a "navigation" file. If you have used Stylebook or Struts system for generation of the web site documentation, you will understand the purpose of this file. **It is an optional task argument.** If you look at the Anakia example in the `examples/anakia` directory, you can see the project.xml file being used in the .vsl file. |
| excludes | This is the standard Ant excludes attribute. Specify any files or directories that you do not want Anakia to try to process. |
| includes | This is the standard Ant includes attribute. Specify any files or directories that you do want Anakia to try to process. |
| lastModifiedCheck | This turns on or off the ability to check the last modified date on files in order to determine whether or not they need to be re-rendered or not. The value of this attribute can be "true, false, yes, no". By default, it is true, meaning that the last modified date should be checked and if the original .xml file, project file, or .vsl file have not changed, then don't process the page. This accelerates processing because pages that have not changed will not get reprocessed. |
| templatePath | This is the path to the templateRoot which is the directory where your site.vsl file is located. This can be defined in the Velocity.properties or it can be defined here. It it an optional argument if it is defined in the Velocity properties file already. However, if defined, this value will override the path defined in the Velocity.properties file. |
| velocityPropertiesFile | This is the path to the velocity.properties file. It is an optional argument and by default is set to find the properties file in the same directory that the JVM was started in. |

<a id="index--predefined-context-objects"></a>

## Predefined Context Objects

The Anakia Ant task places several objects into the Context for you.

| Name | Value |
| --- | --- |
| $root | This contains the JDOM root Element to your .xml document. When this (or any other variable containing an element) are simply placed into template output, their XML form is rendered. |
| $project | This contains the JDOM root Element to your project.xml document. If you have not specified a project.xml document, then this variable will not be in the context. |
| $escape.getText($string) | This context object will convert HTML Entities in the $string that is passed into it and it will return the converted String. This is good for dealing with CDATA. The entities that are converted are: " -> &quot; | < -> &lt; | > -> &gt; | & - > &amp; |
| . | This contains a String which is the relative path to your .xml document from the baseDir that was specified in your Ant task attributes. Please see the examples/anakia .vsl document for example usage of this String. |
| $xmlout | This contains an class which extends the instance of the JDOM XMLOutputter() object. This allows you to easily create String output out of your JDOM element objects. $xmlout.outputString(Element). Again, please look at the examples for more information on how to use this object. NOTE: this object is obsoleted as simply specifying $element will output the XML serialized form of the element. |
| $xmlout.outputString(Element, true) | This contains an class which extends the instance of the JDOM XMLOutputter() object. The difference between this .outputString() and the one in XMLOutputter is that it will output all of the Elements **within** the passed in Element. So, if you pass in a <td> Element, you will get everything inside the <td> </td>, but not the actual <td> </td>. NOTE: this object is obsoleted as simply specifying $element.content will produce the desired output. |
| $treeWalk.allElements($element) | This will allow you to walk a tree of JDOM Element objects starting at $element. The point of this context object is to allow you to build an XSLT type system where you can look at each Element node conditionally and set its content and attribute values. This is probably one of the more "ugly" aspects of Anakia, but it does do the job and suggestions for improvement are appreciated. This context object is still under development and more documentation will follow soon. NOTE: this object is obsolete and is kept for backward compatibility only. You can use $element.selectNodes("//\*") to achieve the same effect. |
| $xpath.applyTo("document/properties/@title", $root) | The W3C XPath Specification <http://www.w3.org/TR/xpath/> refers to NodeSets repeatedly, but this implementation simply uses java.util.List to hold all Nodes. A 'Node' is any object in a JDOM object tree, such as an org.jdom.Element, org.jdom.Document, or org.jdom.Attribute. Please see the .vsl example file and the org.apache.anakia.XPathTool javadoc for more information. NOTE: this object is obsolete and is kept for backward compatibility only. You can use $element.selectNodes("document/properties/@title") to achieve the same effect with a more intuitive syntax. |
| $date | This is a new java.util.Date object. Useful for putting the current date/time into a page. |

All node lists returned from Anakia objects through $element.selectNodes,
$element.content, and $element.children, as well as through obsoleted
$treeWalk.allElements and $xpath.applyTo have two special features:

- they support the selectNodes method just as a single element does
  that applies an XPath expression to all nodes in the list, and
- when inserted into template output by simply specifying $list, they
  produce the XML fragment consisting of all nodes they contain. This
  eliminates much of the #foreach code in templates.

<a id="index--customizing-the-anakia-context"></a>

## Customizing the Anakia Context

The Anakia context can be customized by using one or more context nested
elements.

```

<anakia ...>
    <context name="customContext" file="./customContext.xml"/>
</anakia>
```

The context file must be an xml file and is an instance of a JDOM
root element similar to $project. There are two attributes for the context:

| Name | Description |
| --- | --- |
| name | This sets the name of the context within the velocity context. It cannot be one of the predefined context objects. |
| file | The location of the custom file relative to the anakia basedir. This must be an XML file. |

Within the velocity template the context can be accessed using the standard
velocity template language.

```

#set ($customMenus = $xpath.applyTo("body/menu",$customContext))
#foreach($customMenu in $customMenus)
  <strong>$customMenu.getAttributeValue("name")</strong>
  <ul>
  #foreach ($customItem in $customMenu.getChildren() )
    #set ($name = $customItem.getAttributeValue("name"))
    <li>#projectanchor($name $customItem.getAttributeValue("href"))</li>
  #end
  </ul>
#end
```

<a id="index--credits"></a>

## Credits

Anakia was originally conceptualized and implemented by
[Jon S. Stevens](mailto:jon@latchkey.com).

The name [Anakia](http://www.kabalarians.com/female/anakia.htm) is a
cool name that I think fits this project quite nicely. "The name of
Anakia has given you the desire for creative, artistic or musical
expression in an original way. You strive to be different and have
the self-confidence to implement your ideas because you have the
perseverance necessary to see something through, despite obstacles."

Further help and assistance was provided by Jason van Zyl and Geir
Magnusson Jr. XPath support was added by Bob McWhirter. The more
intuitive syntax achieved through selectNodes() and self-rendering
elements and node lists was added by Attila Szegedi. The custom context
nested element was added by Peter Ryan.

---

<a id="changes-report"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/changes-report.html -->

<!-- page_index: 2 -->

<a id="changes-report--changes-report"></a>

## Changes Report

<a id="changes-report--release-history"></a>

### Release History

| Version | Date | Description |
| --- | --- | --- |
| [1.0](#changes-report--a1.0) | 2007-04-25 |  |

<a id="changes-report--release-1.0-2007-04-25"></a>

### Release 1.0 - 2007-04-25

| Type | Changes | By |
| --- | --- | --- |
| add | Pull Anakia Code out of main Velocity distribution. Fixes [ANAKIA-1](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=ANAKIA-1). | [wglass](http://velocity.apache.org/who-we-are.html#wglass) |

---

<a id="jira-report"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/jira-report.html -->

<!-- page_index: 3 -->

<a id="jira-report--jira-report"></a>

## Jira Report

| Key | Summary | Status | Resolution | By |
| --- | --- | --- | --- | --- |
| [ANAKIA-1](https://issues.apache.org:443/jira/browse/ANAKIA-1 ) | Remove Anakia and Texen from Engine distribution | Open | Unresolved | Unassigned |
| [ANAKIA-2](https://issues.apache.org:443/jira/browse/ANAKIA-2 ) | Add FileMapper support to Anakia to allow arbitrary file name mapping | Open | Unresolved | Unassigned |
| [ANAKIA-3](https://issues.apache.org:443/jira/browse/ANAKIA-3 ) | Add equivalent to < style > ' s xmlcatalog nested elements | Open | Unresolved | Unassigned |
| [ANAKIA-4](https://issues.apache.org:443/jira/browse/ANAKIA-4 ) | Setting xpath namespace bindings? | Open | Unresolved | Unassigned |

---

<a id="project-reports"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/project-reports.html -->

<!-- page_index: 4 -->

<a id="project-reports--generated-reports"></a>

## Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](http://maven.apache.org) Each report is briefly described below.

<a id="project-reports--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [Change Log](https://velocity.apache.org/anakia/1.0/changelog.html) | Generated change log report from SCM. |
| [Changes Report](#changes-report) | Changes Report on Releases of the Project. |
| [Developer Activity](#dev-activity) | Generated developer activity report from SCM. |
| [File Activity](#file-activity) | Generate file activity report from SCM. |
| [JavaDocs](https://velocity.apache.org/anakia/1.0/apidocs/index.html) | JavaDoc API documentation. |
| [Jira Report](#jira-report) | Report on Issues from the JIRA Issue Tracking System. |
| [Source Xref](https://velocity.apache.org/anakia/1.0/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Tag List](#taglist) | Report on various tags found in the code. |
| [Test Source Xref](https://velocity.apache.org/anakia/1.0/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |

---

<a id="dev-activity"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/dev-activity.html -->

<!-- page_index: 5 -->

<a id="dev-activity--developer-activity-report"></a>

## Developer Activity Report

<a id="dev-activity--sun-apr-01-13:24:37-gmt-00:00-2007-to-wed-may-02-13:24:37-gmt-00:00-2007"></a>

### Sun Apr 01 13:24:37 GMT+00:00 2007 to Wed May 02 13:24:37 GMT+00:00 2007

Range: Sun Apr 01 13:24:37 GMT+00:00 2007 to Wed May 02 13:24:37 GMT+00:00 2007, Total commits:21, Total Number of Files Changed:22

| Developer | Total commits | Total Number of Files Changed |
| --- | --- | --- |
| [Will Glass-Husain](https://velocity.apache.org/anakia/1.0/team-list.html#wglass) | 13 | 11 |
| [Henning P. Schmiedehausen](https://velocity.apache.org/anakia/1.0/team-list.html#henning) | 6 | 11 |
| [Nathan Bubna](https://velocity.apache.org/anakia/1.0/team-list.html#nbubna) | 2 | 2 |

---

<a id="file-activity"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/file-activity.html -->

<!-- page_index: 6 -->

<a id="file-activity--file-activity-report"></a>

## File Activity Report

<a id="file-activity--changes-between-sun-apr-01-13:24:37-gmt-00:00-2007-to-wed-may-02-13:24:37-gmt-00:00-2007"></a>

### Changes between Sun Apr 01 13:24:37 GMT+00:00 2007 to Wed May 02 13:24:37 GMT+00:00 2007

Range: Sun Apr 01 13:24:37 GMT+00:00 2007 to Wed May 02 13:24:37 GMT+00:00 2007, Total commits:21, Total Number of Files Changed:22

| Filename | Number of Times Changed |
| --- | --- |
| [/velocity/anakia/trunk/build/build.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.xml) | 3 |
| [/velocity/anakia/trunk/build/build.properties](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.properties) | 3 |
| [/velocity/anakia/trunk/build/download.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/download.xml) | 3 |
| [/velocity/anakia/trunk/xdocs/stylesheets/site.vsl](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/site.vsl) | 2 |
| [/velocity/anakia/trunk/src/site/site.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/site.xml) | 2 |
| [/velocity/anakia/trunk/pom.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/pom.xml) | 2 |
| [/velocity/anakia/trunk/src/test/org/apache/anakia/AnakiaTestCase.java](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/test/org/apache/anakia/AnakiaTestCase.java) | 1 |
| [/velocity/anakia/trunk/xdocs/stylesheets/project.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/project.xml) | 1 |
| [/velocity/anakia/trunk/xdocs/docs/index.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/docs/index.xml) | 1 |
| [/velocity/anakia/trunk](http://svn.apache.org/viewvc/velocity/anakia/trunk) | 1 |
| [/velocity/anakia/trunk/src/changes](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/changes) | 1 |
| [/velocity/anakia/trunk/src/changes/changes.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/changes/changes.xml) | 1 |
| [/velocity/anakia/trunk/src/site](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site) | 1 |
| [/velocity/anakia/trunk/src/site/resources](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources) | 1 |
| [/velocity/anakia/trunk/src/site/resources/images](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources/images) | 1 |
| [/velocity/anakia/trunk/src/site/resources/images/velocity-logo.png](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources/images/velocity-logo.png) | 1 |
| [/velocity/anakia/branches/Anakia-1.0](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0) | 1 |
| [/velocity/anakia/branches/Anakia-1.0/src/changes/changes.xml](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/src/changes/changes.xml) | 1 |
| [/velocity/anakia/branches/Anakia-1.0/build/build.properties](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/build/build.properties) | 1 |
| [/velocity/anakia/branches/Anakia-1.0/pom.xml](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/pom.xml) | 1 |
| [/velocity/anakia/branches/Anakia-1.0/xdocs/docs/index.xml](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/xdocs/docs/index.xml) | 1 |
| [/velocity/anakia/tags/Anakia-1.0](http://svn.apache.org/viewvc/velocity/anakia/tags/Anakia-1.0) | 1 |

---

<a id="taglist"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/taglist.html -->

<!-- page_index: 7 -->

<a id="taglist--tag-list-report"></a>

## Tag List Report

The following document contains the listing of user tags found in the code. Below is the summary of the occurences per tag.

| Tag | Total number of occurences |
| --- | --- |
| [@todo](#taglist--todo) | 0 |
| [TODO](#taglist--todo) | 0 |

Each tag is detailed below:

<a id="taglist--todo"></a>

### @todo

**Number of occurences found in the code: 0**

<a id="taglist--todo-2"></a>

### TODO

**Number of occurences found in the code: 0**

---
