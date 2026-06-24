# Apache Anakia - Anakia

## Navigation

- Anakia
  - [General](#index)
- Developers
  - [Resolved Issues](#jira-report)
- Project Documentation
  - Project Reports
    - [Change Log](#changelog)
    - [Developer Activity](#dev-activity)
    - [File Activity](#file-activity)
    - [Jira Report](#jira-report)

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
SAXBuilder builder; Document root = null;
try {builder = new SAXBuilder("org.apache.xerces.parsers.SAXParser" ); root = builder.build( file );} catch( Exception E ) {System.out.println( ...  );}
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
| $escape.getText($string) | This context object will convert HTML Entities in the $string that is passed into it and it will return the converted String. This is good for dealing with CDATA. The entities that are converted are: " -> &quot; \| < -> &lt; \| > -> &gt; \| & - > &amp; |
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

<a id="jira-report"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/jira-report.html -->

<!-- page_index: 2 -->

<a id="jira-report--jira-report"></a>

## Jira Report

| Key | Summary | Status | Resolution | By |
| --- | --- | --- | --- | --- |
| [ANAKIA-1](https://issues.apache.org:443/jira/browse/ANAKIA-1 ) | Remove Anakia and Texen from Engine distribution | Open | Unresolved | Unassigned |
| [ANAKIA-2](https://issues.apache.org:443/jira/browse/ANAKIA-2 ) | Add FileMapper support to Anakia to allow arbitrary file name mapping | Open | Unresolved | Unassigned |
| [ANAKIA-3](https://issues.apache.org:443/jira/browse/ANAKIA-3 ) | Add equivalent to < style > ' s xmlcatalog nested elements | Open | Unresolved | Unassigned |
| [ANAKIA-4](https://issues.apache.org:443/jira/browse/ANAKIA-4 ) | Setting xpath namespace bindings? | Open | Unresolved | Unassigned |

---

<a id="changelog"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/changelog.html -->

<!-- page_index: 3 -->

<a id="changelog--change-log-report"></a>

## Change Log Report

Total number of changed sets: 1

<a id="changelog--changes-between-sun-apr-01-13:24:37-gmt-00:00-2007-to-wed-may-02-13:24:37-gmt-00:00-2007"></a>

### Changes between Sun Apr 01 13:24:37 GMT+00:00 2007 to Wed May 02 13:24:37 GMT+00:00 2007

Total commits: 21 Total number of files changed: 22

| Timestamp | Author | Details |
| --- | --- | --- |
| 2007-04-28 00:00:00 | wglass | [/velocity/anakia/tags/Anakia-1.0 (from /velocity/anakia/branches/Anakia-1.0:533437)](http://svn.apache.org/viewvc/velocity/anakia/tags/Anakia-1.0 (from /velocity/anakia/branches/Anakia-1.0:533437)) [v 533438](http://svn.apache.org/viewvc/velocity/anakia/tags/Anakia-1.0 (from /velocity/anakia/branches/Anakia-1.0:533437)?rev=533438&content-type=text/vnd.viewcvs-markup) Release Anakia 1.0 |
| 2007-04-22 00:00:00 | wglass | [/velocity/anakia/branches/Anakia-1.0 (from /velocity/anakia/trunk:531143)](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0 (from /velocity/anakia/trunk:531143)) [v 531144](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0 (from /velocity/anakia/trunk:531143)?rev=531144&content-type=text/vnd.viewcvs-markup) made a copy |
| 2007-04-22 00:00:00 | wglass | [/velocity/anakia/branches/Anakia-1.0/src/changes/changes.xml](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/src/changes/changes.xml) [v 531181](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/src/changes/changes.xml?content-type=text%2Fvnd.viewcvs-markup&rev=531181) set release date to next wed in changelog |
| 2007-04-22 00:00:00 | wglass | [/velocity/anakia/branches/Anakia-1.0/build/build.properties](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/build/build.properties) [v 531187](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/build/build.properties?rev=531187&content-type=text/vnd.viewcvs-markup) [/velocity/anakia/branches/Anakia-1.0/pom.xml](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/pom.xml) [v 531187](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/pom.xml?content-type=text%2Fvnd.viewcvs-markup&rev=531187) fix version number |
| 2007-04-22 00:00:00 | wglass | [/velocity/anakia/branches/Anakia-1.0/xdocs/docs/index.xml](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/xdocs/docs/index.xml) [v 531190](http://svn.apache.org/viewvc/velocity/anakia/branches/Anakia-1.0/xdocs/docs/index.xml?content-type=text%2Fvnd.viewcvs-markup&rev=531190) minor typo |
| 2007-04-10 00:00:00 | henning | [/velocity/anakia/trunk/build/build.properties](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.properties) [v 527183](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.properties?rev=527183&content-type=text/vnd.viewcvs-markup) [/velocity/anakia/trunk/build/download.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/download.xml) [v 527183](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/download.xml?content-type=text%2Fvnd.viewcvs-markup&rev=527183) don't need antlr, log4j and logkit for anakia. |
| 2007-04-10 00:00:00 | henning | [/velocity/anakia/trunk](http://svn.apache.org/viewvc/velocity/anakia/trunk) [v 527187](http://svn.apache.org/viewvc/velocity/anakia/trunk?rev=527187&content-type=text/vnd.viewcvs-markup) Ignore mvn target directory. |
| 2007-04-10 00:00:00 | henning | [/velocity/anakia/trunk/pom.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/pom.xml) [v 527188](http://svn.apache.org/viewvc/velocity/anakia/trunk/pom.xml?content-type=text%2Fvnd.viewcvs-markup&rev=527188) update dependencies and JIRA tracking for Anakia. |
| 2007-04-10 00:00:00 | henning | [/velocity/anakia/trunk/src/changes](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/changes) [v 527189](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/changes?rev=527189&content-type=text/vnd.viewcvs-markup) [/velocity/anakia/trunk/src/changes/changes.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/changes/changes.xml) [v 527189](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/changes/changes.xml?content-type=text%2Fvnd.viewcvs-markup&rev=527189) [/velocity/anakia/trunk/src/site](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site) [v 527189](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site?rev=527189&content-type=text/vnd.viewcvs-markup) [/velocity/anakia/trunk/src/site/resources](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources) [v 527189](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources?rev=527189&content-type=text/vnd.viewcvs-markup) [/velocity/anakia/trunk/src/site/resources/images](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources/images) [v 527189](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources/images?rev=527189&content-type=text/vnd.viewcvs-markup) [/velocity/anakia/trunk/src/site/resources/images/velocity-logo.png](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources/images/velocity-logo.png) [v 527189](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/resources/images/velocity-logo.png?content-type=text%2Fvnd.viewcvs-markup&rev=527189) [/velocity/anakia/trunk/src/site/site.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/site.xml) [v 527189](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/site.xml?content-type=text%2Fvnd.viewcvs-markup&rev=527189) Add site skeleton. |
| 2007-04-10 00:00:00 | henning | [/velocity/anakia/trunk/src/site/site.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/site.xml) [v 527198](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/site/site.xml?content-type=text%2Fvnd.viewcvs-markup&rev=527198) Add docbook link |
| 2007-04-10 00:00:00 | henning | [/velocity/anakia/trunk/build/build.properties](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.properties) [v 527204](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.properties?rev=527204&content-type=text/vnd.viewcvs-markup) [/velocity/anakia/trunk/build/download.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/download.xml) [v 527204](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/download.xml?content-type=text%2Fvnd.viewcvs-markup&rev=527204) [/velocity/anakia/trunk/pom.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/pom.xml) [v 527204](http://svn.apache.org/viewvc/velocity/anakia/trunk/pom.xml?content-type=text%2Fvnd.viewcvs-markup&rev=527204) Anakia does need antlr through xpath. Re-Add it. |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/build/build.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.xml) [v 525394](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.xml?content-type=text%2Fvnd.viewcvs-markup&rev=525394) delete velocity.log file created during xdocs / test |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/build/build.properties](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.properties) [v 525401](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.properties?rev=525401&content-type=text/vnd.viewcvs-markup) name the project Anakia, not Velocity Anakia |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/build/build.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.xml) [v 525402](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.xml?content-type=text%2Fvnd.viewcvs-markup&rev=525402) make build file generic by removing Anakia project name from comment |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/src/test/org/apache/anakia/AnakiaTestCase.java](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/test/org/apache/anakia/AnakiaTestCase.java) [v 525405](http://svn.apache.org/viewvc/velocity/anakia/trunk/src/test/org/apache/anakia/AnakiaTestCase.java?rev=525405&content-type=text/vnd.viewcvs-markup) fix comment |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/xdocs/stylesheets/project.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/project.xml) [v 525414](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/project.xml?content-type=text%2Fvnd.viewcvs-markup&rev=525414) fix name of project |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/xdocs/stylesheets/site.vsl](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/site.vsl) [v 525416](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/site.vsl?rev=525416&content-type=text/vnd.viewcvs-markup) fix erroneous reference |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/xdocs/stylesheets/site.vsl](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/site.vsl) [v 525439](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/stylesheets/site.vsl?rev=525439&content-type=text/vnd.viewcvs-markup) fix bug with escaping in tables |
| 2007-04-04 00:00:00 | wglass | [/velocity/anakia/trunk/build/build.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.xml) [v 525443](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/build.xml?content-type=text%2Fvnd.viewcvs-markup&rev=525443) apparently, you can't use a parameter for the build file name |
| 2007-04-04 00:00:00 | nbubna | [/velocity/anakia/trunk/xdocs/docs/index.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/docs/index.xml) [v 525621](http://svn.apache.org/viewvc/velocity/anakia/trunk/xdocs/docs/index.xml?content-type=text%2Fvnd.viewcvs-markup&rev=525621) s/velocity.anakia/anakia |
| 2007-04-02 00:00:00 | nbubna | [/velocity/anakia/trunk/build/download.xml](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/download.xml) [v 524870](http://svn.apache.org/viewvc/velocity/anakia/trunk/build/download.xml?content-type=text%2Fvnd.viewcvs-markup&rev=524870) fix typo in commons-collections download |

---

<a id="dev-activity"></a>

<!-- source_url: https://velocity.apache.org/anakia/1.0/dev-activity.html -->

<!-- page_index: 4 -->

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

<!-- page_index: 5 -->

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
