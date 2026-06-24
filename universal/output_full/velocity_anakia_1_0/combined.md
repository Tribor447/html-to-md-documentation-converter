# Apache Anakia - Anakia

## Navigation

- Anakia
  - [General](#index_2)
  - [Download](https://velocity.apache.org/download.cgi)
- Developers
  - [License](#license)
  - [Javadoc](https://velocity.apache.org/anakia/1.0/apidocs/index.html)
  - [Changes](#changes-report)
  - [Resolved Issues](#jira-report)
  - [Source Code Repository](http://svn.apache.org/viewvc/velocity/anakia/trunk/)
- Community
  - [Wiki](http://wiki.apache.org/velocity/)
  - [Get Involved](http://wiki.apache.org/velocity/GetInvolved)
  - [Mailing Lists](https://velocity.apache.org/contact.html)
- Velocity Development
  - [Coding Standards](http://wiki.apache.org/velocity/CodeStandards)
  - [Documentation Guidelines](http://wiki.apache.org/velocity/DocumentationGuidelines)
  - [Issues](https://issues.apache.org/jira/browse/ANAKIA)
  - [Who we are](https://velocity.apache.org/who-we-are.html)
- Project Documentation
  - [Project Information](#project-info)
    - [Dependencies](#dependencies)
    - [Issue Tracking](#issue-tracking)
    - [Project License](#license)
    - [Project Summary](#project-summary)
    - [Source Repository](#source-repository)
  - [Project Reports](#project-reports)
    - [Change Log](https://velocity.apache.org/anakia/1.0/changelog.html)
    - [Changes Report](#changes-report)
    - [Developer Activity](#dev-activity)
    - [File Activity](#file-activity)
    - [JavaDocs](https://velocity.apache.org/anakia/1.0/apidocs/index.html)
    - [Jira Report](#jira-report)
    - [Source Xref](https://velocity.apache.org/anakia/1.0/xref/index.html)
    - [Tag List](#taglist)
    - [Test Source Xref](https://velocity.apache.org/anakia/1.0/xref-test/index.html)
- [Apache Velocity](https://velocity.apache.org/)
- [Velocity News Feed](https://velocity.apache.org/rss/news.rss)
- Other pages
  - [Apache Anakia - Anakia](#index)

## Content

<a id="index_2"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/index.html -->

<!-- page_index: 1 -->

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

<a id="license"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/license.html -->

<!-- page_index: 2 -->

## Overview

Typically the licenses listed for the project are that of the project itself, and not of dependencies.

## Project License

### The Apache Software License, Version 2.0

```

                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

---

<a id="changes-report"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/changes-report.html -->

<!-- page_index: 3 -->

## Changes Report

### Release History

| Version | Date | Description |
| --- | --- | --- |
| [1.0](#changes-report--a1.0) | 2007-04-25 |  |

### Release 1.0 - 2007-04-25

| Type | Changes | By |
| --- | --- | --- |
| add | Pull Anakia Code out of main Velocity distribution. Fixes [ANAKIA-1](https://issues.apache.org/jira/browse/ViewIssue.jspa?key=ANAKIA-1). | [wglass](http://velocity.apache.org/who-we-are.html#wglass) |

---

<a id="jira-report"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/jira-report.html -->

<!-- page_index: 4 -->

## Jira Report

| Key | Summary | Status | Resolution | By |
| --- | --- | --- | --- | --- |
| [ANAKIA-1](https://issues.apache.org:443/jira/browse/ANAKIA-1 ) | Remove Anakia and Texen from Engine distribution | Open | Unresolved | Unassigned |
| [ANAKIA-2](https://issues.apache.org:443/jira/browse/ANAKIA-2 ) | Add FileMapper support to Anakia to allow arbitrary file name mapping | Open | Unresolved | Unassigned |
| [ANAKIA-3](https://issues.apache.org:443/jira/browse/ANAKIA-3 ) | Add equivalent to < style > ' s xmlcatalog nested elements | Open | Unresolved | Unassigned |
| [ANAKIA-4](https://issues.apache.org:443/jira/browse/ANAKIA-4 ) | Setting xpath namespace bindings? | Open | Unresolved | Unassigned |

---

<a id="project-info"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/project-info.html -->

<!-- page_index: 5 -->

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

### Overview

| Document | Description |
| --- | --- |
| [Dependencies](#dependencies) | This document lists the projects dependencies and provides information on each dependency. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Project License](#license) | This is a link to the definitions of project licenses. |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Source Repository](#source-repository) | This is a link to the online source repository that can be viewed via a web browser. |

---

<a id="dependencies"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/dependencies.html -->

<!-- page_index: 6 -->

## Project Dependencies

### compile

The following is a list of compile dependencies for this project. These dependencies are required to compile and run the application:

| GroupId | ArtifactId | Version | Classifier | Type | Optional |
| --- | --- | --- | --- | --- | --- |
| antlr | antlr | 2.7.5 | - | jar |  |
| commons-collections | commons-collections | 3.1 | - | jar |  |
| commons-lang | commons-lang | 2.1 | - | jar |  |
| jdom | jdom | 1.0 | - | jar |  |
| velocity | velocity | 1.5 | - | jar |  |
| werken-xpath | werken-xpath | 0.9.4 | - | jar |  |

### provided

The following is a list of provided dependencies for this project. These dependencies are required to compile the application, but should be provided by default when using the library:

| GroupId | ArtifactId | Version | Classifier | Type | Optional |
| --- | --- | --- | --- | --- | --- |
| ant | ant | 1.6 | - | jar |  |

## Project Transitive Dependencies

The following is a list of transitive dependencies for this project. Transitive dependencies are the dependencies of the project dependencies.

### compile

The following is a list of compile dependencies for this project. These dependencies are required to compile and run the application:

| GroupId | ArtifactId | Version | Classifier | Type | Optional |
| --- | --- | --- | --- | --- | --- |
| oro | oro | 2.0.8 | - | jar |  |

## Project Dependency Graph

### Dependency Tree

- [org.apache.anakia:anakia:jar](#dependencies--org.apache.anakia:anakia:jar)
  - [commons-lang:commons-lang:jar](#dependencies--commons-lang:commons-lang:jar)
  - [commons-collections:commons-collections:jar](#dependencies--commons-collections:commons-collections:jar)
  - [jdom:jdom:jar](#dependencies--jdom:jdom:jar)
  - [werken-xpath:werken-xpath:jar](#dependencies--werken-xpath:werken-xpath:jar)
  - [ant:ant:jar](#dependencies--ant:ant:jar)
  - [velocity:velocity:jar](#dependencies--velocity:velocity:jar)
    - [oro:oro:jar](#dependencies--oro:oro:jar)

- [antlr:antlr:jar](#dependencies--antlr:antlr:jar)

### Dependency Listings

**Anakia**

Anakia uses Apache Velocity to generate documents based on XML source files.

<http://velocity.apache.org/anakia/releases/anakia-1.0>

**Lang**

Commons.Lang, a package of Java utility classes for the
classes that are in java.lang's hierarchy, or are considered to be so
standard as to justify existence in java.lang.

<http://jakarta.apache.org/commons/${pom.artifactId.substring(8)}/>

**Unnamed - commons-collections:commons-collections:jar:3.1**

Types that extend and augment the Java Collections Framework.

**Unnamed - jdom:jdom:jar:1.0**

**Unnamed - werken-xpath:werken-xpath:jar:0.9.4**

**Ant**

**Apache Velocity**

Apache Velocity is a general purpose template engine.

<http://velocity.apache.org/engine/releases/velocity-1.5/>

**Unnamed - oro:oro:jar:2.0.8**

**Unnamed - antlr:antlr:jar:2.7.5**

---

<a id="issue-tracking"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/issue-tracking.html -->

<!-- page_index: 7 -->

## Overview

This project uses [Jira](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/ANAKIA
```

---

<a id="project-summary"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/project-summary.html -->

<!-- page_index: 8 -->

## Project Summary

### Project Information

| Field | Value |
| --- | --- |
| Name | Anakia |
| Description | Anakia uses Apache Velocity to generate documents based on XML source files. |
| Homepage | <http://velocity.apache.org/anakia/releases/anakia-1.0> |

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.anakia |
| ArtifactId | anakia |
| Version | 1.0 |
| Type | jar |

---

<a id="source-repository"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/source-repository.html -->

<!-- page_index: 9 -->

## Overview

This project uses [Subversion](http://subversion.tigris.org/) to manage its source code. Instructions on Subversion use can be found at <http://svnbook.red-bean.com/>.

## Web Access

The following is a link to the online source repository.

```
http://svn.apache.org/viewvc/velocity/anakia/tags/Anakia-1.0
```

## Anonymous access

The source can be checked out anonymously from SVN with this command:

```
$ svn checkout http://svn.apache.org/repos/asf/velocity/anakia/tags/Anakia-1.0 anakia
```

## Developer access

Everyone can access the Subversion repository via HTTPS, but Committers must checkout the Subversion repository via HTTPS.

```
$ svn checkout https://svn.apache.org/repos/asf/velocity/anakia/tags/Anakia-1.0 anakia
```

To commit changes to the repository, execute the following command to commit your changes (svn will prompt you for your password)

```
$ svn commit --username your-username -m "A message"
```

## Access from behind a firewall

For those users who are stuck behind a corporate firewall which is blocking http access to the Subversion repository, you can try to access it via the developer connection:

```
$ svn checkout https://svn.apache.org/repos/asf/velocity/anakia/tags/Anakia-1.0 anakia
```

## Access through a proxy

The Subversion client can go through a proxy, if you configure it to do so. First, edit your "servers" configuration file to indicate which proxy to use. The files location depends on your operating system. On Linux or Unix it is located in the directory "~/.subversion". On Windows it is in "%APPDATA%\Subversion". (Try "echo %APPDATA%", note this is a hidden directory.)

There are comments in the file explaining what to do. If you don't have that file, get the latest Subversion client and run any command; this will cause the configuration directory and template files to be created.

Example : Edit the 'servers' file and add something like :

```
[global]
http-proxy-host = your.proxy.name
http-proxy-port = 3128
```

---

<a id="project-reports"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/project-reports.html -->

<!-- page_index: 10 -->

## Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](http://maven.apache.org) Each report is briefly described below.

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

<!-- page_index: 11 -->

## Developer Activity Report

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

<!-- page_index: 12 -->

## File Activity Report

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

<!-- page_index: 13 -->

## Tag List Report

The following document contains the listing of user tags found in the code. Below is the summary of the occurences per tag.

| Tag | Total number of occurences |
| --- | --- |
| [@todo](#taglist--todo) | 0 |
| [TODO](#taglist--todo) | 0 |

Each tag is detailed below:

### @todo

**Number of occurences found in the code: 0**

### TODO

**Number of occurences found in the code: 0**

---

<a id="index"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/ -->

<!-- page_index: 14 -->

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
