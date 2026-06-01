# Apache DVSL - DVSL

## Navigation

- DVSL
  - [General](#index)
- Documentation
  - [User Guide](#users-guide)
  - [Ant Task Reference](#ant_task_reference)
  - [More Resources](#more-resources)

## Content

<a id="index"></a>

<!-- source_url: https://velocity.apache.org/dvsl/1.0/ -->

<!-- page_index: 1 -->

<a id="index--dvsl-:-declarative-xml-transformation-and-templating"></a>

## DVSL : Declarative XML Transformation and Templating

DVSL (Declarative Velocity Style Language) is a tool modeled after
XSLT and is intended for general XML transformations using the
Velocity Template Language as the templating language for the
transformations. The key
differences are that it
incorporates easy access to Java objects and allows you to use
the Velocity template language and it's features for expressing the
transformation templates.

 **Similarities to XSLT**

DVSL steals two of the best features of XSLT:

- It uses a declarative syntax like XSLT.
- Document control and selection is based on XPath.

**Differences From XSLT**

DVSL differs from XSLT in a few ways

- DVSL's template language is Velocity, so conventional Velocity syntax is
  used to get and set data, to perform looping and flow control, etc. All
  features of VTL are available.
- Because DVSL is based on Velocity, it offers a very tight binding to
  Java objects. This means that it's easy to access other data sources
  from within the DVSL stylesheet, using conventional method call syntax,
  allowing you to integrate, collect, and
  transform with and to outside data like databases, calculation libraries, etc

<a id="index--current-status"></a>

## Current Status

DVSL is now mature and usable in production environments.

<a id="index--nightly-snapshots"></a>

## Nightly Snapshots

Nightly snapshots of the DVSL Subversion are available
[here](http://cvs.apache.org/snapshots/velocity/dvsl/).

<a id="index--subversion-access"></a>

## Subversion Access

Access to the DVSL Subversion repository is available :

- [Online](http://svn.apache.org/viewvc/velocity/dvsl/trunk/) in your browser.
- Using a [Subversion client](http://www.apache.org/dev/version-control.html)

---

<a id="users-guide"></a>

<!-- source_url: https://velocity.apache.org/dvsl/1.0/users-guide.html -->

<!-- page_index: 2 -->

<a id="users-guide--dvsl-user-guide"></a>

## DVSL User Guide

DVSL (Declarative Velocity Style Language) is a tool modeled after
XSLT and is intended for general XML transformations.
DVSL steals two of the best features of XSLT:

- It uses a declarative syntax like XSLT.
- Document control and selection is based on XPath.

DVSL's template language is [Velocity](http://velocity.apache.org/engine/devel/vtl-reference-guide.html), so conventional Velocity syntax is
used to get and set data, to perform looping and flow control, etc.
Anything that you can normally do in a Velocity template can be done
in DVSL templates.

<a id="users-guide--getting-started-:-building-and-using"></a>

## Getting Started : Building and Using

**Where to Get DVSL**

Before you use DVSL, you must get the source and build the tool.
Currently, there is no release, so you must either get a
nightly snapshot, or download directly from Subversion.

**How to Build**

Building DVSL is very simple. All dependency jars that are required
are included in the distribution. However, we do require that
[Apache Ant](http://ant.apache.org) is installed.

Once ant is installed, you simply need to change to the project
root directory and invoke ant with the 'jar' target :

```

$ cd dvsl
$ ant jar
```

This will build the dvsl jar in the project root directory.

**Using DVSL**

While DVSL is also a tool that can be integrated into your applications, DVSL is able to be used without any programming.

The first way is via command line, where you can use it to transform a single file, or as a filter.
The usage is :

`java org.apache.dvsl.DVSL -STYLE stylesheet [-IN infile] [-OUT outfile ]`

Note that the stylesheet is the only required element, and the input and output then default to
`stdin` and `stdout`.
By adding the appropriate stuff in your classpath (that would be all the jars in the project
`lib` directory ), you can use it :

```

java org.apache.dvsl.DVSL -STYLE src/stylesheets/site.dvsl -IN xdocs/index.xml > out.stuff
java org.apache.dvsl.DVSL -STYLE src/stylesheets/site.dvsl -OUT out.html < xdocs/index.html
java org.apache.dvsl.DVSL -STYLE src/stylesheets/site.dvsl < xdocs/index.xml
```

You can also use DVSL right from ant using the included Ant task. The Ant task supports the toolbox.

```

<target name="docs">

   <taskdef name="dvsl" classname="org.apache.dvsl.DVSLTask">
     <classpath>
       <pathelement location="${project.name}-${project.version}.jar"/>
       <path refid="classpath"/>
     </classpath>
   </taskdef>

 <dvsl
   basedir="${docs.src}"
   destdir="${docs.dest}/"
   toolboxfile="${docs.src}/toolbox.props"
   extension=".html"
   style="${source.home}/stylesheets/site.dvsl"
   excludes="**/project.xml"
   includes="**/*.xml"
 />
</target>
```

For more information on using DVSL from Ant, please see the
[Ant Task Reference](#ant_task_reference).

<a id="users-guide--starting-with-examples"></a>

## Starting with Examples

A few examples are provided with the current distribution, in the `examples`
directory in the distribution, and the examples that follow were originally taken
from there.

**Simple Example**

To begin, we will start with a simple example. Here is a basic XML document:

```


<?xml version="1.0"?>

<document>
    <section name="foo">
        <p>
           Hello from section foo
        </p>
    </section>
    <section name="bar">
        <p>
           Hello from section bar
        </p>
    </section>
</document>
```

A simple DVSL stylesheet to transform this into HTML might look like :

```

#match("document")
<html>
  <body>
$context.applyTemplates()
  </body>
</html>
#end

#match("section")
  <hr>
  <b>Section:</b> $attrib.name
  $context.applyTemplates("p")
#end

#match("p")
  <blockquote>
  $node.copy($node.children())
  </blockquote>
#end
```

With the resulting output of

```

<html>
  <body>
    <hr>
    <b>Section:</b> foo
    <blockquote>

    Hello from section foo

    </blockquote>

    <hr>
    <b>Section:</b> bar
    <blockquote>

    Hello from section bar

    </blockquote>

  </body>
</html>
```

This can be found in examples/simple and is example1.xml and example1.dvsl.

**Now Add Some External Tools**

A more interesting example involves specifying and using tools. We'll give an
example and explain the toolbox later on.

A simple toolbox example is included, in examples/toolbox. First, you must
define the tools and values in a properties file

```

toolbox.contextname = toolbox
toolbox.tool.footool = Footool
toolbox.string.mystring = Hello there!
toolbox.integer.myint = 7
```

Here we do a couple of things :

1. `toolbox.contextname = toolbox` :
   defines 'toolbox' as the name we will use in the template
   to access the tools.
2. `toolbox.tool.footool = Footool` : defines that an instance
   of the class 'Footool' will be placed in the context under the key 'footool'.
3. `toolbox.string.mystring = Hello there!` : defines that a
   `java.lang.String`
   "Hello there!" will be placed in the context under the key 'mystring'
4. `toolbox.integer.myint = 7` : defines that a
   `java.lang.Integer` will be placed in the context under the
   key 'myint'.

You specify the toolbox in the <dvsl> task in the ant script as
such :

```

<dvsl
    basedir="${docs.src}"
    destdir="${docs.dest}/"
    extension=".html"
    style="${docs.src}/site.dvsl"
    excludes="**/project.xml"
    toolboxfile="toolbox.props"
    includes="**/*.xml
/>
```

To use the tools, this is the stylesheet that has an example :

```

#match("document")

    Hello from the document node.

    From the toolbox :

    Method : $context.toolbox.footool.getFoo()
    String : $context.toolbox.mystring
    Int : $context.toolbox.myint

    #foreach( $data in $context.toolbox.footool.getList() )
        Item $velocityCount : $data
    #end
#end
```

With an input of :

```

<?xml version="1.0"?>

<document value="5">

   Data in &lt;document&gt; node

</document>
```

And with the class Footool

```
import java.util.List;
public class Footool {public String getFoo() {return "Hello from Foo!";}
public List getList() {List list = new java.util.ArrayList();
list.add("red"); list.add("blue"); list.add("green");
return list;}}
```

You get the output

```

Hello from the document node.

From the toolbox :

Method : Hello from Foo!
String : Hello there!
Int : 7

    Item 1 : red
    Item 2 : blue
    Item 3 : green
```

This can be found in `examples/toolbox`.

Also, the `examples/velocitydocs` example shows how to grab
and use the HTMLEscape class from the Velocity jar as a tool to do
escaping.

<a id="users-guide--the-template-api"></a>

## The 'Template API'

Writing templates is very simple. The basic template definition uses the directive

```

#match(<XPath Expression >)
    < template content >
#end
```

This directive declares that when a node matches the `<XPath Expression >`
then the body of the directive is to be rendered to the ouput.
In the body, you would place any static content you wish to go to
the output, and also get data from the XML document you are working in.

*Future plans include a #name() directive, and optional arguments to the #match()
and #name() directives to support modes and namsepaces.*

**The Node API**

During processing, when a match occurs and a template is invoked, a few objects are placed in the
Context for you to access. These elements are read-only and cannot be modified via #set().

The most important is the current Node, which is accessible via the reference
`$node`. The `$node` is the current node that matched
the template XPath expression (or name).

You can use the $node object two ways. First, you can use the Velocity property formalism to access
child nodes in the document tree rooted at the current node. So with a document such as :

```

<?xml version="1.0"?>
<document>
  <section name="first">
   <p>
      <code>foo</code>
   </p>
   <p>
      <code>bar</code>
   </p>
  </section>
</document>
```

you could use references like

```

     $node.section.p.code
  
```

to access elements and atributes in the subtree, assuming that $node was the 'document' element.
Further, you can of course call methods on the
sub-elements :

```

$node.section.children()
```

As for methods, `$node` has the following API
for you to use :

| Reference | Methods | Description |
| --- | --- | --- |
| $node |  | Current node for this template match. |
|  | $node.name() | Element name of node - ex 'table' |
|  | $node.value() | Text content of node |
|  | $node.attrib("name") | Returns attribute of node if appropriate. |
|  | $node.selectNodes(xpathexpr) | Returns an iteratable list of nodes that satisfy the XPath expression |
|  | $node.selectSingleNode(xpathexpr) | Returns the first node that satisfies the XPath expression |
|  | $node.get(xpathexpr) | Returns the first node that satisfies the XPath expression |
|  | $node.children() | Returns a List of all children of this node |
|  | $node.copy() | Does a 'deep copy' of this node's subtree to the output |
|  | $node.copy(List) | Does a 'deep copy' of the specified nodelist to the output. |
|  | $node.valueOf(xpathexpr) | Returns the result of the specified XPath as a Object |

The next node-specific reference is `$attrib`. This
corresponds to a collection of the current nodes attributes (if appropriate - for
example, an attribute doesn't itself have attributes) which you can use
to quickly get the values using Velocity's property reference formalism.
So with the example above, if you matched the 'section' node
you could find the value of the 'name' attribute via

```

$attrib.name
```

Which would return 'first'.

The final reference available is `$context`. This object offers the
following API :

| Reference | Methods | Description |
| --- | --- | --- |
| $context |  | Utility context. |
|  | $context.applyTemplates() | Applies all templates in the subtree against the ruleset. |
|  | $context.applyTemplates(xpathexpr) | Applies templates to all nodes in the subtree that match the given XPath expression. Ex. `$context.applyTemplates("*\|@*")` |
|  | $context.applyTemplates(Node) | Applies templates to the specified node. First match is applied. |
|  | $context.applyTemplates(Node, xpathexpr) | Applies the XPath expression to the specified node, and applies templates to the resulting nodeset. |
|  | $context.applyTemplates(Node, xpathexpr) | Applies the XPath expression to the specified node, and applies templates to the resulting nodeset. |
|  | $context.getAppValue(Object key) | Returns the application value for this key. For example, Ant will place the current input file name under the key "infilename". |

<a id="users-guide--default-template-rules"></a>

## Default Template Rules

DVSL has default patterns to drive the transformation engine just like
XSLT does. These patterns currently are modeled after the XSLT default
behavior. DVLS differs in that it will offer you the abillity to
override the default patterns w/o having to change your stylesheet.
The patterns are :

```

#match("/")$context.applyTemplates()#end

#match("*")$context.applyTemplates()#end
```

These patterns are registered in the matching engine first, so any
patterns specified in the stylesheet will override these definitions.

What this means for the user is that DVSL will automatically start with
the root of the document (in the XSL sense, the the 'properly formed
document sense') and try to match each element that it finds.
Because it has a default rule for elements ("\*") it will appply templates
to all nodes in each element that it finds. Further it will print out the
value of each text ndoes, and each attribute node.

These rules are copied from the XSLT spec. There are two more rules
that have been commented out :

```

#match("text()")$node.value()#end

#match("@*")$node.value()#end
```

which should be there for XSLT spec compliance. If you want them, just
uncomment in `org.apache.dvsl.resource.defaultroot.dvsl`
and rebuild the jar.

They are currently left out as they don't seem to be desireable, and it
doesn't appear that xalan respects the rules either.

---

<a id="ant_task_reference"></a>

<!-- source_url: https://velocity.apache.org/dvsl/1.0/ant_task_reference.html -->

<!-- page_index: 3 -->

<a id="ant_task_reference--dvsl-ant-task-reference"></a>

## DVSL Ant Task Reference

Processes a set of XML documents using a stylesheet written in DVSL
(Declarative Velocity Style Language).

This is useful for building views of XML based documentation, or for generating code, etc. Conceptually, this task performs the same
function as the <style> task included with the Ant distribution
but using a stylesheet with DVSL syntax instead of XSLT.

As DVSL has a tight binding with Java objects, access is provided to
the "Toolbox" which loads properties and objects which are then exposed to
the stylesheet in a transparent manner.

Since DVSL utilizes Velocity for rendering its output, access is
provided to allow configuring the Velocity runtime environment from within
this task.

It is possible to refine the set of files that are being processed. This
can be done with the *includes*, *includesfile*, *excludes*,
*excludesfile* and *defaultexcludes* attributes. With the *includes*
or *includesfile* attribute you specify the files you want to have included
by using patterns. The *exclude* or *excludesfile* attribute is used
to specify the files you want to have excluded. This is also done with patterns.
And finally with the *defaultexcludes* attribute, you can specify whether you
want to use default exclusions or not. See the section on [directory based tasks](https://velocity.apache.org/dvsl/dirtasks.html#directorybasedtasks), on how the
inclusion/exclusion of files works, and how to write patterns.

This task forms an implicit [FileSet](https://velocity.apache.org/dvsl/CoreTypes/fileset.html) and supports all
attributes of `<fileset>` (`dir` becomes `basedir`)
as well as the nested `<include>`, `<exclude>`
and `<patternset>` elements.

DVSL supports the use of a <tool> element which is used to pass values
to the DVSL toolbox configuration.

All Velocity messages are routed through Ant's logging system but
will only be output if their level exceeds that of Ant's current logging
level. By default, this means Velocity informational messages are
suppressed while warning and error messages are output. The following
table shows the mapping between Ant logging options and the corresponding
levels of Velocity messages which are output.

| **Ant Logging Option** | **Velocity Messages Output** |
| --- | --- |
| `-quiet` | errors |
| `no option` | errors, warnings |
| `-verbose` | errors, warnings, informational |
| `-debug` | errors, warnings, informational, debug |

If the `logfile` attribute is specified to this task, all Velocity messages are written to the specified log file without
regard to any logging option specified to Ant.

<a id="ant_task_reference--parameters"></a>

## Parameters

| **Attribute** | **Description** | **Required** |
| --- | --- | --- |
| basedir | where to find the source XML file, default is the project's basedir. | No |
| destdir | directory in which to store the results. | Yes, unless in and out have been specified. |
| extension | desired file extension to be used for the targets. If not specified, the default is ".html". | No |
| style | name of the stylesheet to use - given either relative to the project's basedir or as an absolute path | Yes |
| classpath | classpath to use when loading toolbox and velocity configuration classes. | No |
| classpathref | the classpath to use, given as [reference](https://velocity.apache.org/dvsl/using.html#references) to a path defined elsewhere. | No |
| force | Recreate target files, even if they are newer than their corresponding source files or the stylesheet. | No |
| includes | comma separated list of patterns of files that must be included. All files are included when omitted. | No |
| includesfile | the name of a file. Each line of this file is taken to be an include pattern | No |
| excludes | comma separated list of patterns of files that must be excluded. No files (except default excludes) are excluded when omitted. | No |
| excludesfile | the name of a file. Each line of this file is taken to be an exclude pattern | No |
| defaultexcludes | indicates whether default excludes should be used or not ("yes"/"no"). Default excludes are used when omitted. | No |
| in | specifies a single XML document to be styled. Should be used with the out attribute. | No |
| out | specifies the output name for the styled result from the in attribute. | No |
| outputencoding | encoding to be used for output files. If not specified, the default is UTF-8. | No |
| logfile | log file for Velocity messages. The default is to log through Ant's logging system but limit output based on Ant's logging level. Specifying this attribute causes all Velocity messages to be sent to the specified file instead. | No |
| toolboxfile | specifies the toolbox properties file name. | No |
| velocityconfigclass | specifies a class to load which sets Velocity properties. The class must implement the `java.util.Map` interface. | No |
| validatingparser | specifies that the parser for the input XML should validate. Boolean valued, default is `false` | No |

<a id="ant_task_reference--parameters-specified-as-nested-elements"></a>

## Parameters specified as nested elements

<a id="ant_task_reference--classpath"></a>

### classpath

Classpath to use when loading toolbox and velocity configuration
classes. This is defined using a
[path](https://velocity.apache.org/dvsl/using.html#path)-like structure.

<a id="ant_task_reference--tool"></a>

### tool

Set a toolbox property. Properties specified with this nested element
override those defined in a properties file specified by the
`toolboxfile` attribute.

**Parameters**

| **Attribute** | **Description** | **Required** |
| --- | --- | --- |
| name | Name of the toolbox property | Yes |
| value | Value of the toolbox property. | Yes |

<a id="ant_task_reference--velconfig"></a>

### velconfig

Velconfig is used to set a Velocity configuration property. Properties
specified with this nested element override those defined in a class loaded
via the `velocityconfigclass` attribute.

**Parameters**

| **Attribute** | **Description** | **Required** |
| --- | --- | --- |
| name | Name of the Velocity configuration property | Yes |
| value | Value of the Velocity configuration property. | Yes |

<a id="ant_task_reference--application-values"></a>

## Application Values

DVSL as of v0.43, supports applications making application specific values
available via the $context API. (Please see DVSL User Guide.) When using
Ant and DVSL, the following values are accessable :

- **infilename** : the current input file name, sans path. Ex. 'input.xml'.
  This can be accessed via `$context.getAppValue('infilename')`
- **outfilename** : the current output file name, sans path.
  Ex. 'output.html'.
  This can be accessed via `$context.getAppValue('outfilename')`

<a id="ant_task_reference--declaring-the-dvsl-task-in-the-build-file"></a>

## Declaring the DVSL Task in the build file

This task as with any other task not shipped with Ant must be defined
in the build file using a `<taskdef>` declaration. For
example, the following declaration associates a task named <dvsl>
with the class `org.apache.dvsl.DVSLTask`. In addition, the required jars for DVSL support are specified in classpath using a
FileSet.

```

<taskdef name="dvsl" classname="org.apache.dvsl.DVSLTask">
  <classpath>
    <fileset dir="${lib.dir}">
      <include name="velocity-dvsl-*.jar" />
      <include name="velocity-dep-*.jar" />
      <include name="dom4j-*.jar" />
    </fileset>
  </classpath>
</taskdef>
```

<a id="ant_task_reference--examples"></a>

## Examples

**Simple case running a transformation on all files in a
directory:**

```

<dvsl basedir="doc" destdir="build/doc"
      extension=".html" style="style/apache.dvsl" />
```

**Using parameters to set Toolbox and Velocity
properties:**

```

<dvsl basedir="doc" destdir="build/doc"
      extension=".html" style="style/apache.xsl"
      classpath=".">
  <tool name="toolbox.string.mystring" value="Some arbitrary text" />
  <tool name="toolbox.tool.footool" value="Footool" />
  <velconfig name="runtime.log" value="${basedir}/dvsl.log" />
</dvsl>
```

---

<a id="more-resources"></a>

<!-- source_url: https://velocity.apache.org/dvsl/1.0/more-resources.html -->

<!-- page_index: 4 -->

<a id="more-resources--more-information"></a>

## More Information

For a good basic tutorial on XPath, see
[this site](http://www.zvon.org/xxl/XPathTutorial/General/examples.html) at [Zvon.org](http://www.zvon.org)

---
