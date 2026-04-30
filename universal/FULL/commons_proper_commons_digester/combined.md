# Digester - Project Information

## Navigation

- Digester
  - [Overview](#index)
  - [Issue Tracking](#issue-tracking)
- Developers Guide
  - [Core APIs](#guide-core)
  - [Rules Binder](#guide-binder)
  - [Constructor based rule (new)](#guide-constructor)
  - [Async parser](#guide-async)
  - [Substitution](#guide-substitution)
  - [XML Rules](#guide-xmlrules)
  - [Annotations](#guide-annotations)
  - [FAQ](#guide-faq)
- Release 2.1
  - [Guide](#commons-digester-2.1-core)
    - [Core APIs](#commons-digester-2.1-core)
    - [Substitution](#commons-digester-2.1-substitution)
    - [XML Rules](#commons-digester-2.1-xmlrules)
    - [Annotations](#commons-digester-2.1-annotations)
    - [FAQ](#commons-digester-2.1-faq)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Project Summary](#project-summary)
    - [Project Modules](#modules)
    - [Issue Tracking](#issue-tracking)
    - [Continuous Integration](#integration)
  - [Project Reports](#project-reports)
    - [Changes Report](#changes-report)
    - [JIRA Report](#jira-report)
    - [Surefire Report](#surefire-report)
    - [RAT Report](#rat-report)
    - [CPD Report](#cpd)
    - [PMD Report](#pmd)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/index.html -->

<!-- page_index: 1 -->

<a id="index--the-digester-component"></a>

## The Digester Component

Many projects read XML configuration files to provide initialization
of various Java objects within the system. There are several ways of doing
this, and the *Digester* component was designed to provide a common
implementation that can be used in many different projects.

Basically, the *Digester* package lets you configure an XML ->
Java object mapping module, which triggers certain actions called
*rules* whenever a particular pattern of nested XML elements is
recognized. A rich set of predefined *rules* is available for your
use, or you can also create your own.

<a id="index--documentation"></a>

## Documentation

User documentation is available in the website, you can start reading the
[Core APIs](http://commons.apache.org/digester/guide/core.html).

The [Release Notes](assets/files/release-notes_906864802b624968.txt) document the new features and bug fixes that have been
included in this release.

The "examples" directory in the source code repository contains code which
demonstrates the basic functionality. In particular, you should read the
AddressBook example in the "api" subdirectory. You can view the examples
directly from the Subversion repository via [the web-based repository browser](http://svn.apache.org/viewvc/commons/proper/digester/trunk/src/examples/) web site, or can use subversion to
download the files.

For the FAQ and other digester-related information, see
[the Digester wiki page](http://wiki.apache.org/commons/Digester).

<a id="index--releases"></a>

## Releases

<a id="index--digester-3.2-december-2011"></a>

### Digester 3.2 (December 2011)

The Digester 3.2 release is a maintenance release that adds the most innovating feature ever, providing the
objects [Constructor](#guide-constructor) feature.

Take a look at Digester 3.2 release [changes list](#changes-report--a3.2) for more details.

Digester 3.2 **requires a minimum of JDK 1.5**.

The recommended dependency set for Digester 3.2 is:

<table border="0" class="bodyTable">
<tr>
<th colspan="4">Recommended Dependency Set</th>
</tr>
<tr>
<td><b>Digester</b></td>
<td>+Logging 1.1.1</td>
<td>+BeanUtils 1.8.3</td>
<td>+CGLIB 2.2.2</td>
</tr>
</table>

Since dependencies increased by number, since 3.2 release, Digester is distributed also in a single artifact
with shaded dependencies.

Maven users that want to switch over shaded artifact, must use the with-deps classifier:

```
<dependency>
  <groupId>org.apache.commons</groupId>
  <artifactId>commons-digester3</artifactId>
  <version>3.2</version>
  <classifier>with-deps</classifier>
</dependency>
```

<a id="index--digester-3.1-release-october-2011"></a>

### Digester 3.1 Release (October 2011)

The Digester 3.1 release is a maintenance release that adds the
[Asynchronous parser](#guide-async) feature.

<a id="index--digester-3.0-release-july-2011"></a>

### Digester 3.0 Release (July 2011)

The Digester 3.0 is an almost complete rewrite of the original Digester implementation, which offers:

- A universal loader: core features and extensions became not so easy to maintain, since every contribution was created
  with a different approach; a fresh new architecture is able to load modules that allow users write and include easily
  their own extensions;
- Reusability of Digester configurations: what was missing is a way to
  *describe*
  how the Digester instances have to be built and not how to set rules given an existing instance;
- Rules are now expressed via EDSL: the key feature of Digester3 is expressing rule bindings using a fluent APIs
  collection, that speak more in English rather than in a programming language;
- Improved errors reporting: rules binding debug operations have made easier, a detailed errors list of wrong binding is
  reported just when the loader attempts to create a new Digester instance, and not when running it.

*Acknowledgements*: The Digester 3 has been inspired by special people:

- Rahul Akolkar, for mentoring;
- James Carman, who had the initial idea of building a Digester with fluent APIs;
- Matt Benson, for having influenced on DSL;
- Daniele Testa [mrwolfgraphics AT gmail DOT com], who provided the Digester3 logo.

<a id="index--resources"></a>

## Resources

- Jul 11, 2011 - The online magazine JaxEnter interviews Commons PMC Member Simone Tripodi asking
  [What's New in Apache Commons Digester 3.0?](http://jaxenter.com/what-s-new-in-apache-commons-digester-3-0-36817.html).
- [The Apache wiki page for the commons digester component](http://wiki.apache.org/commons/Digester).
- Jan 6, 2005 - [O'Reilly article](http://www.onjava.com/pub/a/onjava/2004/12/22/jakarta-gems-1.html) by Timothy M. O'Brien about jakarta commons in general, including info on Digester.
- Jun 2, 2003 - [IBM developerWorks article](http://www-106.ibm.com/developerworks/java/library/j-lucene/) by Otis Gospodnetic about parsing, indexing and searching XML with Digester and Lucene.
- Oct 25, 2002 - [JavaWorld](http://www.javaworld.com) has an
  article on Digester entitled [Simplify XML file processing with the Apache Commons Digester](http://www.javaworld.com/javaworld/jw-10-2002/jw-1025-opensourceprofile.html).
- Oct 23, 2002 - [OnJava](http://www.onjava.com) has an article
  on Digester entitled
  [Learning and using Jakarta Digester](http://www.onjava.com/pub/a/onjava/2002/10/23/digester.html).

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/issue-tracking.html -->

<!-- page_index: 2 -->

<a id="issue-tracking--commons-digester-issue-tracking"></a>

## Commons Digester Issue tracking

Commons Digester uses [ASF JIRA](http://issues.apache.org/jira/) for tracking issues.
See the [Commons Digester JIRA project page](http://issues.apache.org/jira/browse/DIGESTER).

To use JIRA you may need to [create an account](http://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](http://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Commons Digester please do the following:

1. [Search existing open bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310471&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-digester/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310471&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310471&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Commons Digester are all unpaid volunteers

For more information on subversion and creating patches see the
[Apache Contributors Guide](http://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Commons Digester bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310471&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Commons Digester bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310471&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Commons Digester bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310471&sorter/field=issuekey&sorter/order=DESC)

---

<a id="guide-core"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/core.html -->

<!-- page_index: 3 -->

<a id="guide-core--external-dependencies"></a>

## External Dependencies

The *Digester* component Version 2.0 is dependent upon implementations of the following
standard libraries:

- **XML Parser** compatible with the JAXP/1.3 specification.
  Compatible implementations are included in JDKs 1.5 and above.

It is also dependent on a compatible set of
[Apache Commons](http://commons.apache.org/) library components.
The recommended dependency set is:

>
<table border="1" cellpadding="3" cellspacing="2" class="bodyTable">
<tr><th colspan="3">Recommended Dependency Set</th></tr>
<tr><td>Digester</td><td>+Logging 1.1.1</td><td>+BeanUtils 1.8.3</td></tr>
</table>

It is also possible to use Logging 1.0.x or BeanUtils 1.8.0 instead.

<a id="guide-core--introduction"></a>

## Introduction

In many application environments that deal with XML-formatted data, it is
useful to be able to process an XML document in an "event driven" manner, where particular Java objects are created (or methods of existing objects
are invoked) when particular patterns of nested XML elements have been
recognized. Developers familiar with the Simple API for XML Parsing (SAX)
approach to processing XML documents will recognize that the Digester provides
a higher level, more developer-friendly interface to SAX events, because most
of the details of navigating the XML element hierarchy are hidden -- allowing
the developer to focus on the processing to be performed.

In order to use a Digester, the following basic steps are required:

- Create a new instance of the
  org.apache.commons.digester3.Digester class. Previously
  created Digester instances may be safely reused, as long as you have
  completed any previously requested parse, and you do not try to utilize
  a particular Digester instance from more than one thread at a time.
- Set any desired [configuration properties](#guide-core--doc.properties)
  that will customize the operation of the Digester when you next initiate
  a parse operation.
- Optionally, push any desired initial object(s) onto the Digester's
  [object stack](#guide-core--doc.stack).
- Register all of the [element matching patterns](#guide-core--doc.patterns)
  for which you wish to have [processing rules](#guide-core--doc.rules)
  fired when this pattern is recognized in an input document. You may
  register as many rules as you like for any particular pattern. If there
  is more than one rule for a given pattern, the rules will be executed in
  the order that they were listed.
- Call the digester.parse() method, passing a reference to the
  XML document to be parsed in one of a variety of forms. See the
  [Digester.parse()](https://commons.apache.org/proper/commons-digester/apidocs/Digester.html#parsejava.io.File)
  documentation for details. Note that you will need to be prepared to
  catch any IOException or SAXException that is
  thrown by the parser, or any runtime expression that is thrown by one of
  the processing rules.

Alternatively a Digester may be used as a sax event hander, as follows:

- Create an instance of a sax parser (using the JAXP APIs or otherwise).
- Set any desired configuration properties on that parser object.
- Create an instance of org.apache.commons.digester3.Digester.
- Optionally, push any desired initial object(s) onto the Digester's
  [object stack](#guide-core--doc.stack).
- Register patterns and rules with the digester instance.
- Call parser.parse(inputSource, digester).

For example code, see  [the usage
examples](#guide-core--doc.usage), and  [the FAQ](#guide-core--doc.faq.examples) .

<a id="guide-core--configuration-properties"></a>

## Configuration Properties

A org.apache.commons.digester3.Digester instance contains several
configuration properties that can be used to customize its operation. These
properties **must** be configured before you call one of the
parse() variants, in order for them to take effect on that
parse.

>
| Property | Description |
| --- | --- |
| classLoader | You can optionally specify the class loader that will be used to load classes when required by the ObjectCreateRule and FactoryCreateRule rules. If not specified, application classes will be loaded from the thread's context class loader (if the useContextClassLoader property is set to true) or the same class loader that was used to load the Digester class itself. |
| errorHandler | You can optionally specify a SAX ErrorHandler that is notified when parsing errors occur. By default, any parsing errors that are encountered are logged, but Digester will continue processing as well. |
| namespaceAware | A boolean that is set to true to perform parsing in a manner that is aware of XML namespaces. Among other things, this setting affects how elements are matched to processing rules. See [Namespace Aware Parsing](#guide-core--doc.namespace) for more information. |
| xincludeAware | A boolean that is set to true to perform parsing in a manner that is aware of XInclude W3C specification. This setting is only effective if the parsing is already configured to be namespace aware. |
| ruleNamespaceURI | The public URI of the namespace for which all subsequently added rules are associated, or null for adding rules that are not associated with any namespace. See [Namespace Aware Parsing](#guide-core--doc.namespace) for more information. |
| rules | The Rules component that actually performs matching of Rule instances against the current element nesting pattern is pluggable. By default, Digester includes a Rules implementation that behaves as described in this document. See [Pluggable Rules Processing](#guide-core--doc.pluggable) for more information. |
| useContextClassLoader | A boolean that is set to true if you want application classes required by FactoryCreateRule and ObjectCreateRule to be loaded from the context class loader of the current thread. By default, classes will be loaded from the class loader that loaded this Digester class. **NOTE** - This property is ignored if you set a value for the classLoader property; that class loader will be used unconditionally. |
| validating | A boolean that is set to true if you wish to validate the XML document against a Document Type Definition (DTD) that is specified in its DOCTYPE declaration. The default value of false requests a parse that only detects "well formed" XML documents, rather than "valid" ones. |

In addition to the scalar properties defined above, you can also register
a local copy of a Document Type Definition (DTD) that is referenced in a
DOCTYPE declaration. Such a registration tells the XML parser
that, whenever it encounters a DOCTYPE declaration with the
specified public identifier, it should utilize the actual DTD content at the
registered system identifier (a URL), rather than the one in the
DOCTYPE declaration.

For example, the Struts framework controller servlet uses the following
registration in order to tell Struts to use a local copy of the DTD for the
Struts configuration file. This allows usage of Struts in environments that
are not connected to the Internet, and speeds up processing even at Internet
connected sites (because it avoids the need to go across the network).

```

    URL url = new URL( "/org/apache/struts/resources/struts-config_1_0.dtd" );
    digester.register
      ( "-//Apache Software Foundation//DTD Struts Configuration 1.0//EN",
       url.toString() );
```

As a side note, the system identifier used in this example is the path
that would be passed to java.lang.ClassLoader.getResource()
or java.lang.ClassLoader.getResourceAsStream(). The actual DTD
resource is loaded through the same class loader that loads all of the Struts
classes -- typically from the struts.jar file.

<a id="guide-core--the-object-stack"></a>

## The Object Stack

One very common use of org.apache.commons.digester3.Digester
technology is to dynamically construct a tree of Java objects, whose internal
organization, as well as the details of property settings on these objects, are configured based on the contents of the XML document. In fact, the
primary reason that the Digester package was created (it was originally part
of Struts, and then moved to the Commons project because it was recognized
as being generally useful) was to facilitate the
way that the Struts controller servlet configures itself based on the contents
of your application's struts-config.xml file.

To facilitate this usage, the Digester exposes a stack that can be
manipulated by processing rules that are fired when element matching patterns
are satisfied. The usual stack-related operations are made available, including the following:

- [clear()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Digester.html#clear) - Clear the current contents
  of the object stack.
- [peek()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Digester.html#peek) - Return a reference to the top
  object on the stack, without removing it.
- [pop()](https://commons.apache.org/proper/commons-digester/apidocs/Digester.html#pop) - Remove the top object from the
  stack and return it.
- [push()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Digester.html#pushT) - Push a new
  object onto the top of the stack.

A typical design pattern, then, is to fire a rule that creates a new object
and pushes it on the stack when the beginning of a particular XML element is
encountered. The object will remain there while the nested content of this
element is processed, and it will be popped off when the end of the element
is encountered. As we will see, the standard "object create" processing rule
supports exactly this functionalility in a very convenient way.

Several potential issues with this design pattern are addressed by other
features of the Digester functionality:

- *How do I relate the objects being created to each other?* - The
  Digester supports standard processing rules that pass the top object on
  the stack as an argument to a named method on the next-to-top object on
  the stack (or vice versa). This rule makes it easy to establish
  parent-child relationships between these objects. One-to-one and
  one-to-many relationships are both easy to construct.
- *How do I retain a reference to the first object that was created?*
  As you review the description of what the "object create" processing rule
  does, it would appear that the first object you create (i.e. the object
  created by the outermost XML element you process) will disappear from the
  stack by the time that XML parsing is completed, because the end of the
  element would have been encountered. However, Digester will maintain a
  reference to the very first object ever pushed onto the object stack,
  and will return it to you
  as the return value from the parse() call. Alternatively,
  you can push a reference to some application object onto the stack before
  calling parse(), and arrange that a parent-child relationship
  be created (by appropriate processing rules) between this manually pushed
  object and the ones that are dynamically created. In this way,
  the pushed object will retain a reference to the dynamically created objects
  (and therefore all of their children), and will be returned to you after
  the parse finishes as well.

<a id="guide-core--element-matching-patterns"></a>

## Element Matching Patterns

A primary feature of the org.apache.commons.digester3.Digester
parser is that the Digester automatically navigates the element hierarchy of
the XML document you are parsing for you, without requiring any developer
attention to this process. Instead, you focus on deciding what functions you
would like to have performed whenver a certain arrangement of nested elements
is encountered in the XML document being parsed. The mechanism for specifying
such arrangements are called *element matching patterns*.

The Digester can be configured to use different pattern-matching algorithms
via the Digester.setRules method. However for the vast majority of cases, the
default matching algorithm works fine. The default pattern matching behaviour
is described below.

A very simple element matching pattern is a simple string like "a". This
pattern is matched whenever an <a> top-level element is
encountered in the XML document, no matter how many times it occurs. Note that
nested <a> elements will **not** match this
pattern -- we will describe means to support this kind of matching later.

The next step up in matching pattern complexity is "a/b". This pattern will
be matched when a <b> element is found nested inside a
top-level <a> element. Again, this match can occur as many
times as desired, depending on the content of the XML document being parsed.
You can use multiple slashes to define a hierarchy of any desired depth that
will be matched appropriately.

For example, assume you have registered processing rules that match patterns
"a", "a/b", and "a/b/c". For an input XML document with the following
contents, the indicated patterns will be matched when the corresponding element
is parsed:

```

  <a>         -- Matches pattern "a"
    <b>       -- Matches pattern "a/b"
      <c/>    -- Matches pattern "a/b/c"
      <c/>    -- Matches pattern "a/b/c"
    </b>
    <b>       -- Matches pattern "a/b"
      <c/>    -- Matches pattern "a/b/c"
      <c/>    -- Matches pattern "a/b/c"
      <c/>    -- Matches pattern "a/b/c"
    </b>
  </a>
```

It is also possible to match a particular XML element, no matter how it is
nested (or not nested) in the XML document, by using the "\*" wildcard character
in your matching pattern strings. For example, an element matching pattern
of "\*/a" will match an <a> element at any nesting position
within the document.

It is quite possible that, when a particular XML element is being parsed, the pattern for more than one registered processing rule will be matched
because you registered more than one processing rule with the exact same
matching pattern.

When this occurs, the corresponding processing rules will all be fired in
order. Rule methods begin (and body) are executed in
the order that the Rules were initially registered with the
Digester, whilst end method calls are executed in
reverse order. In other words - the order is first in, last out.

Note that wildcard patterns are ignored if an explicit match can be found
(and when multiple wildcard patterns match, only the longest, ie most
explicit, pattern is considered a match). The result is that rules can be
added for "an <a> tag anywhere", but then for that behaviour to be
explicitly overridden for specific cases, eg "but not an <a> that is a
direct child of an <x>". Therefore if you have rules A and B registered for
pattern "\*/a" then want to add an additional rule C for pattern "x/a" only, then what you need to do is add \*three\* rules for "x/a": A, B and C. Note
that by using:

```

  Rule ruleA = new ObjectCreateRule();
  Rule ruleB = new SetNextRule();
  Rule ruleC = new SetPropertiesRule();

  digester.addRule("*/a", ruleA);
  digester.addRule("*/a", ruleB);
  digester.addRule("x/a", ruleA);
  digester.addRule("x/a", ruleB);
  digester.addRule("x/a", ruleC);
```

you have associated the same rule instances A and B with multiple patterns, thus avoiding creating extra rule object instances.

<a id="guide-core--processing-rules"></a>

## Processing Rules

The [previous section](#guide-core--doc.patterns) documented how you identify
**when** you wish to have certain actions take place. The purpose
of processing rules is to define **what** should happen when the
patterns are matched.

Formally, a processing rule is a Java class that subclasses the
[org.apache.commons.digester3.Rule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Rule.html) interface. Each Rule
implements one or more of the following event methods that are called at
well-defined times when the matching patterns corresponding to this rule
trigger it:

- [begin()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Rule.html#beginjava.lang.String_java.lang.String_org.xml.sax.Attributes) - Called when the beginning of the matched XML element is encountered. A
  data structure containing all of the attributes corresponding to this
  element are passed as well.
- [body()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Rule.html#bodyjava.lang.String_java.lang.String_java.lang.String) - Called when nested content (that is not itself XML elements) of the
  matched element is encountered. Any leading or trailing whitespace will
  have been removed as part of the parsing process.
- [end()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Rule.html#endjava.lang.String_java.lang.String) - Called
  when the ending of the matched XML element is encountered. If nested XML elements that matched other
  processing rules was included in the body of this element, the appropriate
  processing rules for the matched rules will have already been completed
  before this method is called.
- [finish()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Rule.html#finish) - Called when the parse has
  been completed, to give each rule a chance to clean up any temporary data
  they might have created and cached.

As you are configuring your digester, you can call the
addRule() method to register a specific element matching pattern, along with an instance of a Rule class that will have its event
handling methods called at the appropriate times, as described above. This
mechanism allows you to create Rule implementation classes
dynamically, to implement any desired application specific functionality.

In addition, a set of processing rule implementation classes are provided, which deal with many common programming scenarios. These classes include the
following:

- [ObjectCreateRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/ObjectCreateRule.html) - When the
  begin() method is called, this rule instantiates a new
  instance of a specified Java class, and pushes it on the stack. The
  class name to be used is defaulted according to a parameter passed to
  this rule's constructor, but can optionally be overridden by a classname
  passed via the specified attribute to the XML element being processed.
  When the end() method is called, the top object on the stack
  (presumably, the one we added in the begin() method) will
  be popped, and any reference to it (within the Digester) will be
  discarded.
- [FactoryCreateRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/FactoryCreateRule.html) - A variation of
  ObjectCreateRule that is useful when the Java class with
  which you wish to create an object instance does not have a no-arguments
  constructor, or where you wish to perform other setup processing before
  the object is handed over to the Digester.
- [SetPropertiesRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/SetPropertiesRule.html) - When the
  begin() method is called, the digester uses the standard
  Java Reflection API to identify any JavaBeans property setter methods
  (on the object at the top of the digester's stack)
  who have property names that match the attributes specified on this XML
  element, and then call them individually, passing the corresponding
  attribute values. These natural mappings can be overridden. This allows
  (for example) a class attribute to be mapped correctly.
  It is recommended that this feature should not be overused - in most cases,
  it's better to use the standard BeanInfo mechanism.
  A very common idiom is to define an object create
  rule, followed by a set properties rule, with the same element matching
  pattern. This causes the creation of a new Java object, followed by
  "configuration" of that object's properties based on the attributes
  of the same XML element that created this object.
- [SetPropertyRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/SetPropertyRule.html) - When the
  begin() method is called, the digester calls a specified
  property setter (where the property itself is named by an attribute)
  with a specified value (where the value is named by another attribute),
  on the object at the top of the digester's stack.
  This is useful when your XML file conforms to a particular DTD, and
  you wish to configure a particular property that does not have a
  corresponding attribute in the DTD.
- [SetNextRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/SetNextRule.html) - When the
  end() method is called, the digester analyzes the
  next-to-top element on the stack, looking for a property setter method
  for a specified property. It then calls this method, passing the object
  at the top of the stack as an argument. This rule is commonly used to
  establish one-to-many relationships between the two objects, with the
  method name commonly being something like "addChild".
- [SetTopRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/SetTopRule.html) - When the
  end() method is called, the digester analyzes the
  top element on the stack, looking for a property setter method for a
  specified property. It then calls this method, passing the next-to-top
  object on the stack as an argument. This rule would be used as an
  alternative to a SetNextRule, with a typical method name "setParent",
  if the API supported by your object classes prefers this approach.
- [CallMethodRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/CallMethodRule.html) - This rule sets up a
  method call to a named method of the top object on the digester's stack,
  which will actually take place when the end() method is
  called. You configure this rule by specifying the name of the method
  to be called, the number of arguments it takes, and (optionally) the
  Java class name(s) defining the type(s) of the method's arguments.
  The actual parameter values, if any, will typically be accumulated from
  the body content of nested elements within the element that triggered
  this rule, using the CallParamRule discussed next.
- [CallParamRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/CallParamRule.html) - This rule identifies
  the source of a particular numbered (zero-relative) parameter for a
  CallMethodRule within which we are nested. You can specify that the
  parameter value be taken from a particular named attribute, or from the
  nested body content of this element.
- [NodeCreateRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/NodeCreateRule.html) - A specialized rule
  that converts part of the tree into a DOM Node and then
  pushes it onto the stack.

You can create instances of the standard Rule classes and
register them by calling digester.addRule(), as described above.
However, because their usage is so common, shorthand registration methods are
defined for each of the standard rules, directly on the Digester
class. For example, the following code sequence:

```

    Rule rule = new SetNextRule( digester, "addChild",
                                 "com.mycompany.mypackage.MyChildClass" );
    digester.addRule( "a/b/c", rule );
```

can be replaced by:

```

    digester.addSetNext( "a/b/c", "addChild",
                         "com.mycompany.mypackage.MyChildClass" );
```

<a id="guide-core--logging"></a>

## Logging

Logging is a vital tool for debugging Digester rulesets. Digester can log
copious amounts of debugging information. So, you need to know how logging
works before you start using Digester seriously.

Digester uses
[Apache Commons
Logging](http://commons.apache.org/logging). This component is not really a logging framework - rather
an extensible, configurable bridge. It can be configured to swallow all log
messages, to provide very basic logging by itself or to pass logging messages
on to more sophisticated logging frameworks. Commons-Logging comes with
connectors for many popular logging frameworks. Consult the commons-logging
documentation for more information.

Two main logs are used by Digester:

- SAX-related messages are logged to
  **org.apache.commons.digester3.Digester.sax**.
  This log gives information about the basic SAX events received by
  Digester.
- **org.apache.commons.digester3.Digester** is used
  for everything else. You'll probably want to have this log turned up during
  debugging but turned down during production due to the high message
  volume.

Complete documentation of how to configure Commons-Logging can be found
in the Commons Logging package documentation. However, as a simple example, let's assume that you want to use the SimpleLog implementation
that is included in Commons-Logging, and set up Digester to log events from
the Digester logger at the DEBUG level, while you want to log
events from the Digester.log logger at the INFO level. You can
accomplish this by creating a commons-logging.properties file
in your classpath (or setting corresponding system properties on the command
line that starts your application) with the following contents:

```

  org.apache.commons.logging.Log=org.apache.commons.logging.impl.SimpleLog
  org.apache.commons.logging.simplelog.log.org.apache.commons.digester3.Digester=debug
  org.apache.commons.logging.simplelog.log.org.apache.commons.digester3.Digester.sax=info
```

<a id="guide-core--usage-example"></a>

## Usage Example

<a id="guide-core--creating-a-simple-object-tree"></a>

### Creating a Simple Object Tree

Let's assume that you have two simple JavaBeans, Foo and
Bar, with the following method signatures:

```

  package mypackage;

  public class Foo
  {

    public void addBar( Bar bar );

    public Bar findBar( int id );

    public Iterator getBars();

    public String getName();

    public void setName( String name );

  }


  package mypackage;

  public class Bar
  {

    public int getId();

    public void setId( int id );

    public String getTitle();

    public void setTitle( String title );

  }
```

and you wish to use Digester to parse the following XML document:

```

  <foo name="The Parent">
    <bar id="123" title="The First Child" />
    <bar id="456" title="The Second Child" />
  </foo>
```

A simple approach will be to use the following Digester in the following way
to set up the parsing rules, and then process an input file containing this
document:

```

  Digester digester = new Digester();
  digester.setValidating( false );
  digester.addObjectCreate( "foo", "mypackage.Foo" );
  digester.addSetProperties( "foo" );
  digester.addObjectCreate( "foo/bar", "mypackage.Bar" );
  digester.addSetProperties( "foo/bar" );
  digester.addSetNext( "foo/bar", "addBar", "mypackage.Bar" );
  Foo foo = digester.parse();
```

In order, these rules do the following tasks:

1. When the outermost <foo> element is encountered,
   create a new instance of mypackage.Foo and push it
   on to the object stack. At the end of the <foo>
   element, this object will be popped off of the stack.
2. Cause properties of the top object on the stack (i.e. the Foo
   object that was just created and pushed) to be set based on the values
   of the attributes of this XML element.
3. When a nested <bar> element is encountered,
   create a new instance of mypackage.Bar and push it
   on to the object stack. At the end of the <bar>
   element, this object will be popped off of the stack (i.e. after the
   remaining rules matching foo/bar are processed).
4. Cause properties of the top object on the stack (i.e. the Bar
   object that was just created and pushed) to be set based on the values
   of the attributes of this XML element. Note that type conversions
   are automatically performed (such as String to int for the id
   property), for all converters registered with the ConvertUtils
   class from commons-beanutils package.
5. Cause the addBar method of the next-to-top element on the
   object stack (which is why this is called the "set *next*" rule)
   to be called, passing the element that is on the top of the stack, which
   must be of type mypackage.Bar. This is the rule that causes
   the parent/child relationship to be created.

Once the parse is completed, the first object that was ever pushed on to the
stack (the Foo object in this case) is returned to you. It will
have had its properties set, and all of its child Bar objects
created for you.

<a id="guide-core--processing-a-struts-configuration-file"></a>

### Processing A Struts Configuration File

As stated earlier, the primary reason that the
Digester package was created is because the
Struts controller servlet itself needed a robust, flexible, easy to extend
mechanism for processing the contents of the struts-config.xml
configuration that describes nearly every aspect of a Struts-based application.
Because of this, the controller servlet contains a comprehensive, real world, example of how the Digester can be employed for this type of a use case.
See the initDigester() method of class
org.apache.struts.action.ActionServlet for the code that creates
and configures the Digester to be used, and the initMapping()
method for where the parsing actually takes place.

(Struts binary and source distributions can be acquired at
<http://struts.apache.org>.)

The following discussion highlights a few of the matching patterns and
processing rules that are configured, to illustrate the use of some of the
Digester features. First, let's look at how the Digester instance is
created and initialized:

```

    Digester digester = new Digester();
    digester.push( this ); // Push controller servlet onto the stack
    digester.setValidating( true );
```

We see that a new Digester instance is created, and is configured to use
a validating parser. Validation will occur against the struts-config\_1\_0.dtd
DTD that is included with Struts (as discussed earlier). In order to provide
a means of tracking the configured objects, the controller servlet instance
itself will be added to the digester's stack.

```

    digester.addObjectCreate( "struts-config/global-forwards/forward",
                              forwardClass, "className" );
    digester.addSetProperties( "struts-config/global-forwards/forward" );
    digester.addSetNext( "struts-config/global-forwards/forward",
                         "addForward",
                         "org.apache.struts.action.ActionForward" );
    digester.addSetProperty( "struts-config/global-forwards/forward/set-property",
                             "property", "value");
```

The rules created by these lines are used to process the global forward
declarations. When a <forward> element is encountered, the following actions take place:

- A new object instance is created -- the ActionForward
  instance that will represent this definition. The Java class name
  defaults to that specified as an initialization parameter (which
  we have stored in the String variable forwardClass), but can
  be overridden by using the "className" attribute (if it is present in the
  XML element we are currently parsing). The new ActionForward
  instance is pushed onto the stack.
- The properties of the ActionForward instance (at the top of
  the stack) are configured based on the attributes of the
  <forward> element.
- Nested occurrences of the <set-property> element
  cause calls to additional property setter methods to occur. This is
  required only if you have provided a custom implementation of the
  ActionForward class with additional properties that are
  not included in the DTD.
- The addForward() method of the next-to-top object on
  the stack (i.e. the controller servlet itself) will be called, passing
  the object at the top of the stack (i.e. the ActionForward
  instance) as an argument. This causes the global forward to be
  registered, and as a result of this it will be remembered even after
  the stack is popped.
- At the end of the <forward> element, the top element
  (i.e. the ActionForward instance) will be popped off the
  stack.

Later on, the digester is actually executed as follows:

```

    InputStream input =
      getServletContext().getResourceAsStream( config );
    ...
    try
    {
        digester.parse( input );
        input.close();
    }
    catch ( SAXException e )
    {
        ... deal with the problem ...
    }
```

As a result of the call to parse(), all of the configuration
information that was defined in the struts-config.xml file is
now represented as collections of objects cached within the Struts controller
servlet, as well as being exposed as servlet context attributes.

<a id="guide-core--parsing-body-text-in-xml-files"></a>

### Parsing Body Text In XML Files

The Digester module also allows you to process the nested body text in an
XML file, not just the elements and attributes that are encountered. The
following example is based on an assumed need to parse the web application
deployment descriptor (/WEB-INF/web.xml) for the current web
application, and record the configuration information for a particular
servlet. To record this information, assume the existence of a bean class
with the following method signatures (among others):

```

  package com.mycompany;

  public class ServletBean
  {

    public void setServletName( String servletName );

    public void setServletClass( String servletClass );

    public void addInitParam( String name, String value );

  }
```

We are going to process the web.xml file that declares the
controller servlet in a typical Struts-based application (abridged for
brevity in this example):

```

  <web-app>
    ...
    <servlet>
      <servlet-name>action</servlet-name>
      <servlet-class>org.apache.struts.action.ActionServlet<servlet-class>
      <init-param>
        <param-name>application</param-name>
        <param-value>org.apache.struts.example.ApplicationResources<param-value>
      </init-param>
      <init-param>
        <param-name>config</param-name>
        <param-value>/WEB-INF/struts-config.xml<param-value>
      </init-param>
    </servlet>
    ...
  </web-app>
```

Next, lets define some Digester processing rules for this input file:

```

  digester.addObjectCreate( "web-app/servlet",
                            "com.mycompany.ServletBean" );
  digester.addCallMethod( "web-app/servlet/servlet-name", "setServletName", 0 );
  digester.addCallMethod( "web-app/servlet/servlet-class",
                          "setServletClass", 0 );
  digester.addCallMethod( "web-app/servlet/init-param",
                          "addInitParam", 2 );
  digester.addCallParam( "web-app/servlet/init-param/param-name", 0 );
  digester.addCallParam( "web-app/servlet/init-param/param-value", 1 );
```

Now, as elements are parsed, the following processing occurs:

- *<servlet>* - A new com.mycompany.ServletBean
  object is created, and pushed on to the object stack.
- *<servlet-name>* - The setServletName() method
  of the top object on the stack (our ServletBean) is called,
  passing the body content of this element as a single parameter.
- *<servlet-class>* - The setServletClass() method
  of the top object on the stack (our ServletBean) is called,
  passing the body content of this element as a single parameter.
- *<init-param>* - A call to the addInitParam
  method of the top object on the stack (our ServletBean) is
  set up, but it is **not** called yet. The call will be
  expecting two String parameters, which must be set up by
  subsequent call parameter rules.
- *<param-name>* - The body content of this element is assigned
  as the first (zero-relative) argument to the call we are setting up.
- *<param-value>* - The body content of this element is assigned
  as the second (zero-relative) argument to the call we are setting up.
- *</init-param>* - The call to addInitParam()
  that we have set up is now executed, which will cause a new name-value
  combination to be recorded in our bean.
- *<init-param>* - The same set of processing rules are fired
  again, causing a second call to addInitParam() with the
  second parameter's name and value.
- *</servlet>* - The element on the top of the object stack
  (which should be the ServletBean we pushed earlier) is
  popped off the object stack.

<a id="guide-core--namespace-aware-parsing"></a>

## Namespace Aware Parsing

For digesting XML documents that do not use XML namespaces, the default
behavior of Digester, as described above, is generally sufficient.
However, if the document you are processing uses namespaces, it is often
convenient to have sets of Rule instances that are *only*
matched on elements that use the prefix of a particular namespace. This
approach, for example, makes it possible to deal with element names that are
the same in different namespaces, but where you want to perform different
processing for each namespace.

Digester does not provide full support for namespaces, but does provide
sufficient to accomplish most tasks. Enabling digester's namespace support
is done by following these steps:

1. Tell Digester that you will be doing namespace
   aware parsing, by adding this statement in your initalization
   of the Digester's properties:


```

    digester.setNamespaceAware( true );
    
```

2. Declare the public namespace URI of the namespace with which
   following rules will be associated. Note that you do *not*
   make any assumptions about the prefix - the XML document author
   is free to pick whatever prefix they want:


```

    digester.setRuleNamespaceURI( "http://www.mycompany.com/MyNamespace" );
    
```

3. Add the rules that correspond to this namespace, in the usual way,
   by calling methods like addObjectCreate() or
   addSetProperties(). In the matching patterns you specify,
   use only the *local name* portion of the elements (i.e. the
   part after the prefix and associated colon (":") character:


```

    digester.addObjectCreate( "foo/bar", "com.mycompany.MyFoo" );
    digester.addSetProperties( "foo/bar");
    
```

4. Repeat the previous two steps for each additional public namespace URI
   that should be recognized on this Digester run.

Now, consider that you might wish to digest the following document, using
the rules that were set up in the steps above:

```

<m:foo
   xmlns:m="http://www.mycompany.com/MyNamespace"
   xmlns:y="http://www.yourcompany.com/YourNamespace">

  <m:bar name="My Name" value="My Value"/>

  <y:bar id="123" product="Product Description"/>L

</x:foo>
```

Note that your object create and set properties rules will be fired for the
*first* occurrence of the bar element, but not the
*second* one. This is because we declared that our rules only matched
for the particular namespace we are interested in. Any elements in the
document that are associated with other namespaces (or no namespaces at all)
will not be processed. In this way, you can easily create rules that digest
only the portions of a compound document that they understand, without placing
any restrictions on what other content is present in the document.

You might also want to look at [Encapsulated
Rule Sets](#guide-core--doc.rulesets) if you wish to reuse a particular set of rules, associated
with a particular namespace, in more than one application context.

<a id="guide-core--using-namespace-prefixes-in-pattern-matching"></a>

### Using Namespace Prefixes In Pattern Matching

Using rules with namespaces is very useful when you have orthogonal rulesets.
One ruleset applies to a namespace and is independent of other rulesets applying
to other namespaces. However, if your rule logic requires mixed namespaces, then
matching namespace prefix patterns might be a better strategy.

When you set the NamespaceAware property to false, digester uses
the qualified element name (which includes the namespace prefix) rather than the
local name as the patten component for the element. This means that your pattern
matches can include namespace prefixes as well as element names. So, rather than
create namespace-aware rules, create pattern matches including the namespace
prefixes.

For example, (with NamespaceAware false), the pattern
'foo:bar' will match a top level element named 'bar' in the
namespace with (local) prefix 'foo'.

<a id="guide-core--limitations-of-digester-namespace-support"></a>

#### Limitations of Digester Namespace support

Digester does not provide general "xpath-compliant" matching;
only the namespace attached to the *last* element in the match path
is involved in the matching process. Namespaces attached to parent
elements are ignored for matching purposes.

<a id="guide-core--pluggable-rules-processing"></a>

## Pluggable Rules Processing

By default, Digester selects the rules that match a particular
pattern of nested elements as described under
[Element Matching Patterns](#guide-core--doc.patterns). If you prefer to use
different selection policies, however, you can create your own implementation
of the [org.apache.commons.digester3.Rules](https://commons.apache.org/proper/commons-digester/apidocs/Rules.html) interface, or subclass the corresponding convenience base class
[org.apache.commons.digester3.RulesBase](https://commons.apache.org/proper/commons-digester/apidocs/RulesBase.html).
Your implementation of the match() method will be called when the
processing for a particular element is started or ended, and you must return
a List of the rules that are relevant for the current nesting
pattern. The order of the rules you return **is** significant, and should match the order in which rules were initally added.

Your policy for rule selection should generally be sensitive to whether
[Namespace Aware Parsing](#guide-core--doc.namespace) is taking place. In
general, if namespaceAware is true, you should select only rules
that:

- Are registered for the public namespace URI that corresponds to the
  prefix being used on this element.
- Match on the "local name" portion of the element (so that the document
  creator can use any prefix that they like).

<a id="guide-core--extendedbaserules"></a>

### ExtendedBaseRules

[ExtendedBaseRules](https://commons.apache.org/proper/commons-digester/apidocs/ExtendedBaseRules.html), adds some additional expression syntax for pattern matching
to the default mechanism, but it also executes more slowly. See the
JavaDocs for more details on the new pattern matching syntax, and suggestions
on when this implementation should be used. To use it, simply do the
following as part of your Digester initialization:

```

  Digester digester = ...
  ...
  digester.setRules( new ExtendedBaseRules() );
  ...
```

<a id="guide-core--regexrules"></a>

### RegexRules

[RegexRules](https://commons.apache.org/proper/commons-digester/apidocs/RegexRules.html) is an advanced Rules
implementation which does not build on the default pattern matching rules.
It uses a pluggable [RegexMatcher](https://commons.apache.org/proper/commons-digester/apidocs/RegexMatcher.html) implementation to test
if a path matches the pattern for a Rule. All matching rules are returned
(note that this behaviour differs from longest matching rule of the default
pattern matching rules). See the Java Docs for more details.

Example usage:

```

  Digester digester = ...
  ...
  digester.setRules( new RegexRules( new SimpleRegexMatcher() ) );
  ...
```

<a id="guide-core--regexmatchers"></a>

### RegexMatchers

Digester ships only with one RegexMatcher
implementation: [SimpleRegexMatcher](https://commons.apache.org/proper/commons-digester/apidocs/SimpleRegexMatcher.html).
This implementation is unsophisticated and lacks many good features
lacking in more power Regex libraries. There are some good reasons
why this approach was adopted. The first is that SimpleRegexMatcher
is simple, it is easy to write and runs quickly. The second has to do with
the way that RegexRules is intended to be used.

There are many good regex libraries available. (For example
[Jakarta ORO](http://jakarta.apache.org/oro/index.html), [Jakarta Regex](http://jakarta.apache.org/regexp/index.html), [GNU Regex](http://www.cacas.org/java/gnu/regexp/) and
[Java 1.4 Regex](http://java.sun.com/j2se/1.4.2/docs/api/java/util/regex/package-summary.html))
Not only do different people have different personal tastes when it comes to
regular expression matching but these products all offer different functionality
and different strengths.

The pluggable RegexMatcher is a thin bridge
designed to adapt other Regex systems. This allows any Regex library the user
desires to be plugged in and used just by creating one class.
Digester does not (currently) ship with bridges to the major
regex (to allow the dependencies required by Digester
to be kept to

<a id="guide-core--withdefaultsruleswrapper"></a>

### WithDefaultsRulesWrapper

[WithDefaultsRulesWrapper](https://commons.apache.org/proper/commons-digester/guide/apidocsWithDefaultsRulesWrapper.html) allows
default Rule instances to be added to any existing
Rules implementation. These default Rule instances
will be returned for any match for which the wrapped implementation does not
return any matches.

For example,

```

    Rule alpha;
    ...
    WithDefaultsRulesWrapper rules = new WithDefaultsRulesWrapper( new BaseRules() );
    rules.addDefault( alpha );
    ...
    digester.setRules( rules );
    ...
```

when a pattern does not match any other rule, then rule alpha will be called.

WithDefaultsRulesWrapper follows the *Decorator* pattern.

<a id="guide-core--encapsulated-rule-sets"></a>

## Encapsulated Rule Sets

All of the examples above have described a scenario where the rules to be
processed are registered with a Digester instance immediately
after it is created. However, this approach makes it difficult to reuse the
same set of rules in more than one application environment. Ideally, one
could package a set of rules into a single class, which could be easily
loaded and registered with a Digester instance in one easy step.

The [RuleSet](https://commons.apache.org/proper/commons-digester/apidocs/RuleSet.html) interface (and the convenience base
class [RuleSetBase](https://commons.apache.org/proper/commons-digester/apidocs/RuleSetBase.html)) make it possible to do this.
In addition, the rule instances registered with a particular
RuleSet can optionally be associated with a particular namespace, as described under [Namespace Aware Processing](#guide-core--doc.namespace).

An example of creating a RuleSet might be something like this:

```

public class MyRuleSet
  extends RuleSetBase {

  public MyRuleSet()
  {
    this("");
  }

  public MyRuleSet(String prefix)
  {
    super();
    this.prefix = prefix;
    this.namespaceURI = "http://www.mycompany.com/MyNamespace";
  }

  protected String prefix = null;

  public void addRuleInstances(Digester digester)
  {
    digester.addObjectCreate( prefix + "foo/bar",
      "com.mycompany.MyFoo" );
    digester.addSetProperties( prefix + "foo/bar" );
  }

}
```

You might use this RuleSet as follow to initialize a
Digester instance:

```

  Digester digester = new Digester();
  ... configure Digester properties ...
  digester.addRuleSet( new MyRuleSet( "baz/" ) );
```

A couple of interesting notes about this approach:

- The application that is using these rules does not need to know anything
  about the fact that the RuleSet being used is associated
  with a particular namespace URI. That knowledge is emedded inside the
  RuleSet class itself.
- If desired, you could make a set of rules work for more than one
  namespace URI by providing constructors on the RuleSet to
  allow this to be specified dynamically.
- The MyRuleSet example above illustrates another technique
  that increases reusability -- you can specify (as an argument to the
  constructor) the leading portion of the matching pattern to be used.
  In this way, you can construct a Digester that recognizes
  the same set of nested elements at different nesting levels within an
  XML document.

<a id="guide-core--using-named-stacks-for-inter-rule-communication"></a>

## Using Named Stacks For Inter-Rule Communication

Digester is based on Rule instances working together
to process xml. For anything other than the most trival processing, communication between Rule instances is necessary. Since Rule
instances are processed in sequence, this usually means storing an Object
somewhere where later instances can retrieve it.

Digester is based on SAX. The most natural data structure to use with
SAX based xml processing is the stack. This allows more powerful processes to be
specified more simply since the pushing and popping of objects can mimic the
nested structure of the xml.

Digester uses two basic stacks: one for the main beans and the other
for parameters for method calls. These are inadequate for complex processing
where many different Rule instances need to communicate through
different channels.

In this case, it is recommended that named stacks are used. In addition to the
two basic stacks, Digester allows rules to use an unlimited number
of other stacks referred to by an identifying string (the name). (That's where
the term *named stack* comes from.) These stacks are
accessed through calls to:

- [void push(String stackName, Object value)](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Digester.html#pushjava.lang.String_T)
- [Object pop(String stackName)](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Digester.html#popjava.lang.String)
- [Object peek(String stackName)](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Digester.html#peekjava.lang.String)

**Note:** all stack names beginning with org.apache.commons.digester
are reserved for future use by the Digester component. It is also recommended
that users choose stack names prefixed by the name of their own domain to avoid conflicts
with other Rule implementations.

<a id="guide-core--registering-dtds"></a>

## Registering DTDs

<a id="guide-core--brief-but-still-too-long-introduction-to-system-and-public-identifiers"></a>

### Brief (But Still Too Long) Introduction To System and Public Identifiers

A definition for an external entity comes in one of two forms:

1. SYSTEM *system-identifier*
2. PUBLIC *public-identifier* *system-identifier*

The *system-identifier* is an URI from which the resource can be obtained
(either directly or indirectly). Many valid URIs may identify the same resource.
The *public-identifier* is an additional free identifier which may be used
(by the parser) to locate the resource.

In practice, the weakness with a *system-identifier* is that most parsers
will attempt to interprete this URI as an URL, try to download the resource directly
from the URL and stop the parsing if this download fails. So, this means that
almost always the URI will have to be an URL from which the declaration
can be downloaded.

URLs may be local or remote but if the URL is chosen to be local, it is likely only
to function correctly on a small number of machines (which are configured precisely
to allow the xml to be parsed). This is usually unsatisfactory and so a universally
accessable URL is preferred. This usually means an internet URL.

To recap, in practice the *system-identifier* will (most likely) be an
internet URL. Unfortunately downloading from an internet URL is not only slow
but unreliable (since successfully downloading a document from the internet
relies on the client being connect to the internet and the server being
able to satisfy the request).

The *public-identifier* is a freely defined name but (in practice) it is
strongly recommended that a unique, readable and open format is used (for reasons
that should become clear later). A Formal Public Identifier (FPI) is a very
common choice. This public identifier is often used to provide a unique and location
independent key which can be used to subsistute local resources for remote ones
(hint: this is why ;).

By using the second (PUBLIC) form combined with some form of local
catalog (which matches *public-identifiers* to local resources) and where
the *public-identifier* is a unique name and the *system-identifier*
is an internet URL, the practical disadvantages of specifying just a
*system-identifier* can be avoided. Those external entities which have been
store locally (on the machine parsing the document) can be identified and used.
Only when no local copy exists is it necessary to download the document
from the internet URL. This naming scheme is recommended when using Digester.

<a id="guide-core--external-entity-resolution-using-digester"></a>

### External Entity Resolution Using Digester

SAX factors out the resolution of external entities into an EntityResolver.
Digester supports the use of custom EntityResolver
but ships with a simple internal implementation. This implementation allows local URLs
to be easily associated with *public-identifiers*.

For example:

```

    digester.register( "-//Example Dot Com //DTD Sample Example//EN", "assets/sample.dtd" );
```

will make digester return the relative file path assets/sample.dtd
whenever an external entity with public id
-//Example Dot Com //DTD Sample Example//EN is needed.

**Note:** This is a simple (but useful) implementation.
Greater sophistication requires a custom EntityResolver.

<a id="guide-core--troubleshooting"></a>

## Troubleshooting

<a id="guide-core--debugging-exceptions"></a>

### Debugging Exceptions

Digester is based on [SAX](http://www.saxproject.org).
Digestion throws two kinds of Exception:

- java.io.IOException
- org.xml.sax.SAXException

The first is rarely thrown and indicates the kind of fundemental IO exception
that developers know all about. The second is thrown by SAX parsers when the processing
of the XML cannot be completed. So, to diagnose the cause a certain familiarity with
the way that SAX error handling works is very useful.

<a id="guide-core--diagnosing-sax-exceptions"></a>

### Diagnosing SAX Exceptions

This is a short, potted guide to SAX error handling strategies. It's not intended as a
proper guide to error handling in SAX.

When a SAX parser encounters a problem with the xml (well, ok - sometime after it
encounters a problem) it will throw a
[SAXParseException](http://www.saxproject.org/apidoc/org/xml/sax/SAXParseException.html). This is a subclass of SAXException and contains
a bit of extra information about what exactly when wrong - and more importantly, where it went wrong. If you catch an exception of this sort, you can be sure that
the problem is with the XML and not Digester or your rules.
It is usually a good idea to catch this exception and log the extra information
to help with diagnosing the reason for the failure.

General [SAXException](http://www.saxproject.org/apidoc/org/xml/sax/SAXException.html) instances may wrap a causal exception. When exceptions are
throw by Digester each of these will be wrapped into a
SAXException and rethrown. So, catch these and examine the wrapped
exception to diagnose what went wrong.

<a id="guide-core--extensions"></a>

## Extensions

Three extension packages are included within the Digester distribution.
These provide extra functionality extending the core Digester concepts.
Detailed descriptions are contained within their own package documentation.

- [plugins](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/plugins/package-summary.html) provides a framework for the easy
  dynamic addition of rules during a Digestion. Rules can trigger the dynamic addition
  of other rules in an intuitive fashion.
- [substitution](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/substitution/package-summary.html) provides for
  manipulation of attributes and element body text before it is processed by the rules.
- [xmlrules](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/xmlrules/package-summary.html) package contains a
  system allowing digester rule configurations to be specifed through an xml file.
- [annotations](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/annotations/package-summary.html) package contains a
  system allowing digester rule configurations to be specifed through Java5 Annotations.

<a id="guide-core--known-limitations"></a>

## Known Limitations

<a id="guide-core--accessing-public-methods-in-a-default-access-superclass"></a>

### Accessing Public Methods In A Default Access Superclass

There is an issue when invoking public methods contained in a default access superclass.
Reflection locates these methods fine and correctly assigns them as public.
However, an IllegalAccessException is thrown if the method is invoked.

MethodUtils contains a workaround for this situation.
It will attempt to call setAccessible on this method.
If this call succeeds, then the method can be invoked as normal.
This call will only succeed when the application has sufficient security privilages.
If this call fails then a warning will be logged and the method may fail.

Digester uses MethodUtils and so there may be an issue accessing methods
of this kind from a high security environment. If you think that you might be experiencing this
problem, please ask on the mailing list.

---

<a id="guide-binder"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/binder.html -->

<!-- page_index: 4 -->

<a id="guide-binder--rules-binder-new"></a>

## Rules Binder (new)

The Digester 3 design aims to eliminate all the Digester boilerplate without sacrificing maintainability.

With Digester 3, you implement modules, the
[DigesterLoader](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/DigesterLoader.html)
passes a [RulesBinder](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/RulesBinder.html) to your module, and your
module uses the binder to map patterns to [Rule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/Rule.html)s.
We can break Digester's 3 architecture down into two distinct stages: startup and runtime.
You build a DigesterLoader during startup and use it to obtain Digester instances at
runtime.

<a id="guide-binder--startup"></a>

### Startup

You configure the Digester by implementing [RulesModule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/RulesModule.html).
You pass [DigesterLoader](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/DigesterLoader.html) a module, the
DigesterLoader passes your module a [RulesBinder](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/RulesBinder.html), and your module uses the binder to configure *patterns/rules* bindings. A binding most commonly consist of a mapping
between a pattern and one or more [Rule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/Rule.html). For example:

```

class EmployeeModule
    implements RulesModule
{

    protected void configure( RulesBinder rulesBinder )
    {
        rulesBinder.forPattern( "employee" ).createObject().ofType( Employee.class );
        rulesBinder.forPattern( "employee/firstName" ).setBeanProperty();
        rulesBinder.forPattern( "employee/lastName" ).setBeanProperty();

        rulesBinder.forPattern( "employee/address" )
            .createObject().ofType( Address.class )
            .then()
            .setNext( "addAddress" );
        rulesBinder.forPattern( "employee/address/type" ).setBeanProperty();
        rulesBinder.forPattern( "employee/address/city" ).setBeanProperty();
        rulesBinder.forPattern( "employee/address/state" ).setBeanProperty();
    }

}
```

DRY (Don't Repeat Yourself): Repeating "rulesBinder" over and over for each binding can get a little tedious.
The Digester package provides a module support class named
[AbstractRulesModule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/binder/AbstractRulesModule.html) which
implicitly gives you access to RulesBinder's methods. For example, we could extend
AbstractRulesModule and rewrite the above binding as:

```

class EmployeeModule
    extends AbstractRulesModule
{

    @Override
    protected void configure()
    {
        forPattern( "employee" ).createObject().ofType( Employee.class );
        forPattern( "employee/firstName" ).setBeanProperty();
        forPattern( "employee/lastName" ).setBeanProperty();

        forPattern( "employee/address" )
            .createObject().ofType( Address.class )
            .then()
            .setNext( "addAddress" );
        forPattern( "employee/address/type" ).setBeanProperty();
        forPattern( "employee/address/city" ).setBeanProperty();
        forPattern( "employee/address/state" ).setBeanProperty();
    }

}
```

We'll use this syntax throughout the rest of the guide.

Creating a Digester entails the following steps:

1. First, create an instance of your module and pass it to DigesterLoader.newLoader().
2. The DigesterLoader creates a RulesBinder and passes it to your module.
3. Your module uses the binder to define bindings.
4. Set any desired [configuration properties](#guide-core--doc.properties)
   that will customize the operation of the Digester when you next initiate
   a parse operation.
5. Based on the bindings you specified, DigesterLoader creates a Digester by invoking
   DigesterLoader.newDigester() and returns it to you.
6. Optionally, push any desired initial object(s) onto the Digester's [object stack](#guide-core--doc.stack).
7. Call the digester.parse() method, passing a reference to the
   XML document to be parsed in one of a variety of forms. See the
   [Digester.parse()](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/Digester.html#parsejava.io.File)
   documentation for details. Note that you will need to be prepared to
   catch any IOException or SAXException that is
   thrown by the parser, or any runtime expression that is thrown by one of
   the processing rules.
8. Please remember that previously
   created Digester instances may be safely reused, as long as you have
   completed any previously requested parse, and you do not try to utilize
   a particular Digester instance from more than one thread at a time.

<a id="guide-binder--new-digester-fluent-apis"></a>

## New Digester fluent APIs

The main difference between Digester *1.X*, *2.X* and *3.X* is that the
while the first follows the approach *"given a Digester instance, then configure it"*, the new Digester instead follows the opposite approach *"given one (or more) configuration(s), create
multiple Digester instances" or "configure once, create everywhere".*

Why? Even if both approaches sound complementary, the core concept is given by the assumption that every
Digester instance is not thread-safe, that implies that in a multi-thread application users have often
to reinstantiate the Digester and reconfigure it, i.e in a Servlet:

```
public class EmployeeServlet
  extends HttpServlet
{

    public void doGet(HttpServletRequest req, HttpServletResponse res)
        throws ServletException, IOException
    {
        Digester digester = new Digester();
        digester.setNamespaceAware( true );
        digester.setXIncludeAware( true );
        digester.addObjectCreate( "employee", Employee.class );
        digester.addCallMethod( "employee/firstName", "setFirstName", 0 );
        digester.addCallMethod( "employee/lastName", "setLastName", 0 );

        digester.addObjectCreate( "employee/address", Address.class );
        digester.addCallMethod( "employee/address/type", "setType", 0 );
        digester.addCallMethod( "employee/address/city", "setCity", 0 );
        digester.addCallMethod( "employee/address/state", "setState", 0 );
        digester.addSetNext( "employee/address", "addAddress" );

        Employee employee = digester.parse( openStream( req.getParameter( "employeeId" ) ) );
        ...
}
```

Nothing wrong with that approach but configuration is not reusable; the *RuleSet*
interface fills in some way the reuse of configurations lack:

```
public class EmployeeRuleSet
  implements RuleSet
{

    public void addRuleInstances( Digester digester )
    {
        digester.addObjectCreate( "employee", Employee.class );
        digester.addCallMethod( "employee/firstName", "setFirstName", 0 );
        digester.addCallMethod( "employee/lastName", "setLastName", 0 );

        digester.addObjectCreate( "employee/address", Address.class );
        digester.addCallMethod( "employee/address/type", "setType", 0 );
        digester.addCallMethod( "employee/address/city", "setCity", 0 );
        digester.addCallMethod( "employee/address/state", "setState", 0 );
        digester.addSetNext( "employee/address", "addAddress" );
    }

}
```

then, in our sample servlet

```
public class EmployeeServlet
  extends HttpServlet
{

    private final RuleSet employeeRuleSet = new EmployeeRuleSet();

    public void doGet(HttpServletRequest req, HttpServletResponse res)
        throws ServletException, IOException
    {
        Digester digester = new Digester();
        digester.setNamespaceAware( true );
        digester.setXIncludeAware( true );

        employeeRuleSet.addRuleInstances( digester );

        Employee employee = digester.parse( openStream( req.getParameter( "employeeId" ) ) );
        ...
    }

}
```

Nothing wrong again, but:

1. RuleSet is not really a configuration, it just sets rules to given Digester instance;
2. Digester instance creation is totally delegated to clients;
3. Rules that match to the same pattern, need to specify this last *n* times for how many
   rules match, that violates the DRY principle;
4. Rules semantic is not intuitive, since their creation is strictly related to
   methods/constructors arguments.

In the new Digester, *RuleSet* has been suppressed in favor of *RulesModule*

```
class EmployeeModule
    extends AbstractRulesModule
{

    @Override
    protected void configure()
    {
        forPattern( "employee" ).createObject().ofType( Employee.class );
        forPattern( "employee/firstName" ).setBeanProperty();
        forPattern( "employee/lastName" ).setBeanProperty();

        forPattern( "employee/address" )
            .createObject().ofType( Address.class )
            .then()
            .setNext( "addAddress");
        forPattern( "employee/address/type" ).setBeanProperty();
        forPattern( "employee/address/city" ).setBeanProperty();
        forPattern( "employee/address/state" ).setBeanProperty();
    }

}
```

Then, our sample Servlet become:

```
public class EmployeeServlet
    extends HttpServlet
{

    private final DigesterLoader loader = newLoader( new EmployeeModule() )
        .setNamespaceAware( true )
        .setXIncludeAware( true );

    public void doGet(HttpServletRequest req, HttpServletResponse res)
        throws ServletException, IOException
    {
        Digester digester = loader.newDigester()

        Employee employee = digester.parse( openStream( req.getParameter("employeeId") ) );
        ...
    }

}
```

As you can notice, the *RulesModule* implements rules via fluent APIs, making rules semantic simpler, and the effort of configuration is moved to the startup;
the *DigesterLoader* indeed will analyze all the *RulesModule* instances
and will be ready to create new Digester instances with pre-filled rules.

<a id="guide-binder--one-single-configuration-point-one-single-universal-loader"></a>

## One single configuration point, one single universal loader

As shown above, basic Digester2.X usage would be creating a Digester then setting the rules:

```
Digester digester = new Digester();
digester.addObjectCreate( "root", "org.apache.commons.digester.SimpleTestBean" );
digester.addBeanPropertySetter( "root", "alpha" );
digester.addBeanPropertySetter( "root/alpha", "beta" );
digester.addBeanPropertySetter( "root/delta", "delta" );
```

Alternatively, users can create the Rules instance, set the rules and pass it to the Digester:

```
ExtendedBaseRules rules = new ExtendedBaseRules();
rules.addRule( "root", new ObjectCreateRule( "org.apache.commons.digester.SimpleTestBean" ) );
rules.addRule( "root", new BeanPropertySetterRule( "alpha" ) );
rules.addRule( "root/alpha", new BeanPropertySetterRule( "beta" ) );
rules.addRule( "root/delta", new BeanPropertySetterRule( "delta" ) );

Digester digester = new Digester();
digester.setRules( rules );
```

Last, but not least, special loader classes have been created to gain more benefits from RuleSet:
like the annotations package DigesterLoader, to avoid scanning class elements each time
users want to create a new Digester instance to parse Channel type:

```
import org.apache.commons.digester.annotations.*;

DigesterLoader digesterLoader = new DigesterLoaderBuilder()
    .useDefaultAnnotationRuleProviderFactory()
    .useDefaultDigesterLoaderHandlerFactory();
Digester digester = digesterLoader.createDigester( Channel.class );
```

In Digester3 there is just one universal loader that aggregates all the power of the components described above, configurations are expressed via (Abstract)RulesModule

```
class SimpleTestBeanModule
  extends AbstractRulesModule
{

    @Override
    protected void configure()
    {
        forPattern( "root" )
            .createObject().ofType( "org.apache.commons.digester.SimpleTestBean" )
            .then()
            .setBeanProperty( "alpha" );
        forPattern( "root/alpha" ).setBeanProperty( "beta" );
        forPattern( "root/delta" ).setBeanProperty( "delta" );
    }

}
```

Users can simply create new Digester instances:

```
DigesterLoader loader = newLoader(new SimpleTestBeanModule());
...
Digester digester = loader.newDigester();
```

Users can create new Digester instances on top of different Rules types:

Digester digester = loader.newDigester(new ExtendedBaseRules());

An, by the nature of the universal loader, auxiliary optimizations are not needed:

```
DigesterLoader loader = newLoader( new FromAnnotationsRuleModule()
    {

        @Override
        protected void configureRules()
        {
            bindRulesFrom( Channel.class );
        }

    } );
...
Digester digester = loader.newDigester();
...
digester = loader.newDigester(); // Channel.class won't be analyzed again!
```

<a id="guide-binder--extensions-optimization"></a>

## Extensions optimization

As shown above, the universal DigesterLoader introduces a set of optimizations not or partially
introduced in the previous Digester releases: the FromXmlRuleSet, for example, parses the XML Digester rules each time the Digester creation is performed:

```
FromXmlRuleSet ruleSet = new FromXmlRuleSet( MyClass.class.getResource( "myrule.xml" ) );
Digester digester = new Digester();
ruleSet.addRuleInstances( digester ); // myrule.xml will be parsed
...
Digester newDigester = new Digester();
ruleSet.addRuleInstances( newDigester ); // myrule.xml will be parsed again!
```

In Digester3 there's only one RulesModules loading, so in the case of
FromXmlRulesModule, the XML rules will be parsed only once:

```
DigesterLoader loader = newLoader( new FromXmlRulesModule()
    {

        @Override
        protected void loadRules()
        {
            loadXMLRulesFromText( MyClass.class.getResource( "myrule.xml" ) );
        }

    } );
...
Digester digester = loader.newDigester(); // myrule.xml already parsed
...
Digester newDigester = loader.newDigester(); // myrule.xml won't be parsed again!
```

<a id="guide-binder--startup-checks-and-improved-error-reporting"></a>

## Startup checks and improved error reporting

The new Digester tries as much as possible to check patterns/rules binding errors during the
DigesterLoader bootstrap, avoiding exceptions during the parsing operations.

Let's suppose for example the following Digester

```
Digester digester = new Digester();
  digester.addObjectCreate( "root", "com.acme.InOtherClassLoader" );
  ....
  digester.addObjectCreate( "root/child", "foo.bar.DoesNotExist" );
  ...
```

is using a wrong ClassLoader to resolve types, or declared types are in the wrong
package; a runtime error will be thrown as soon as the *root* pattern will match.

Let's suppose users debug their application and fix the ClassLoader problem, a new
runtime error will be thrown as soon as the *root/child* pattern will match, and so on.

The new Digester tries to report all patterns/rules binding error in one single detailed report, i.e.

```
class SampleModule
    extends AbstractRulesModule
{

    @Override
    protected void configure()
    {
        forPattern( "root" ).createObject().ofType( "com.acme.InOtherClassLoader" );
        ...
        forPattern( "root/child" ).createObject().ofType( "foo.bar.DoesNotExist" );
        ...
    }

}
```

The DigesterLoader will report problems in the following way:

```
Exception in thread "XXX" org.apache.commons.digester3.DigesterLoadingException: Digester creation errors:

1) { forPattern( "root" ).createObject().ofType( String ) } class 'com.acme.InOtherClassLoader' cannot be load (SampleModule.java:5)

2) { forPattern( "root/child" ).createObject().ofType( String ) } class 'foo.bar.DoesNotExist' cannot be load (SampleModule.java:10)

2 errors
```

So, users have at least an overview to debug their applications.

---

<a id="guide-constructor"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/constructor.html -->

<!-- page_index: 5 -->

<a id="guide-constructor--constructor-based-rule"></a>

## Constructor based rule

One of the missing features of the old Digester releases is that the
[ObjectCreateRule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/ObjectCreateRule.html) works just with
the default empty constructor.

One limit that cannot be exceeded is the fact that constructor arguments cannot be extracted from inner
XML elements; that's because the ObjectCreateRule creates the object when the related XML
element begins, otherwise properties could not be set when parsing nested elements.

That is no longer true :) Constructor arguments can be extracted from *attributes* and
*nested elements* of the matching XML element for whom the ObjectCreateRule is triggered.

**NOTE** this feature is available since release 3.2.

<a id="guide-constructor--using-plain-old-digester-apis"></a>

### Using plain old Digester APIs

ObjectCreateRule has new APIs to configure the constructor arguments types; given for example
the XML snippet below:

```
<root>
  <bean super="true">
    <rate>9.99<rate/>
  </bean>
</root>
```

That has to be mapped to the bean:

```
class MyBean
{

    public MyBean( Double rate, Boolean super )
    {
        ...
    }

}
```

Then the Digester instance can be configured as below:

```
ObjectCreateRule createRule = new ObjectCreateRule( MyBean.class );
createRule.setConstructorArgumentTypes( boolean.class, double.class );

Digester digester = new Digester();
digester.addRule( "root/bean", createRule );
digester.addCallParam( "root/bean", 1, "super" );
digester.addCallParam( "root/bean/rate", 0 );
```

<a id="guide-constructor--using-the-rulesbinder-apis"></a>

### Using the RulesBinder APIs

The Binder APIs just allow expressing the same rule in a fluent way:

```
DigesterLoader loader = ( new AbstractRulesModule()
{

    @Override
    protected void configure()
    {
        forPattern( "root/bean" )
            .createObject().ofType( MyBean.class ).usingConstructor( boolean.class, double.class )
            .then()
            .callParam().fromAttribute( "super" ).ofIndex( 1 );
        forPattern( "root/bean/rate" ).callParam().ofIndex( 0 );
    }

} );
```

<a id="guide-constructor--using-the-annotations"></a>

### Using the annotations

Since 3.2, [ObjectCreate](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/annotations/rules/ObjectCreate.html)
can be used to annotate constructors as well; with the introduction of
[Attribute](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/annotations/rules/Attribute.html) annotation, constructor based rules can be expressed like:

```
class MyBean
{

    @ObjectCreate( pattern = "root/bean" )
    public MyBean( @CallParam( pattern = "root/bean/rate" ) Double rate,
                   @CallParam( pattern = "root/bean", attributeName = "super" ) Boolean super )
    {
        ...
    }

}
```

<a id="guide-constructor--using-the-xml-meta-descriptor"></a>

### Using the XML meta-descriptor

The XML ruleset supports as well the new constructor rule, <object-create-rule> supports
a new inner element <constructor-argument>:

```
<digester-rules>
  <pattern value="root/bean">
    <object-create-rule classname="MyBean
          paramtypes="java.lang.Double,java.lang.Boolean">
      <constructor-argument attrname="rate" type="java.lang.Double" />
      <call-param-rule paramnumber="0" pattern="rate" />
      <call-param-rule paramnumber="1" attrname="super" />
    </object-create-rule>
  </pattern>
</digester-rules>
```

<a id="guide-constructor--default-constructor-arguments"></a>

## Default constructor arguments

In order to provide that feature, Digester relies on CGLIB that needs to proxy the class of the
target object, to avoid constructors issues users can use the
ObjectCreateRule#setDefaultConstructorArguments(Object...) method to give safe construction
params to the constructor when creating the proxy; that method could be useful also when one parameter needs to
take a static value while the other is handled with a CallParam rule. If these are not specified, the super constructor is called with nulls for Objects and default values for primitives.

---

<a id="guide-async"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/async.html -->

<!-- page_index: 6 -->

<a id="guide-async--asynchronous-digester"></a>

## Asynchronous Digester

Since version 3.1 the Digester component offers asynchronous parse() methods.

Users can take advantage from that feature when need to process large XML streams without mapping to
intermediary POJOs. Take in consideration applications that need to import data from XML documents
- maybe obtained by a REST invocation - and transfer to a DataBase.
Putting the data processor in a non-blocking executor would help clients on:

- increasing the number of parse operations at the same time;

**Note** keep always in mind the every single Digester instance is NOT thread-safety, so please use the *asynchronous* feature carefully!!!

<a id="guide-async--using-digester-loader"></a>

### Using Digester Loader

First of all, setup the DigesterLoader with java.util.concurrent.ExecutorService:

```
final DigesterLoader digesterLoader = newLoader( new AbstractRulesModule()
    {

        @Override
        protected void configure()
        {
            forPattern( "employee" ).createObject().ofType( Employee.class );
            ...
        }

    } ).setExecutorService( java.util.concurrent.Executors.newFixedThreadPool( 10 ) );
```

Then create the Digester and run the parse method asynchronously:

```
Digester digester = digesterLoader.newDigester();
...
Future<Employee> future = digester.asyncParse( new URL( "http://my.rest.server/employees/10" ) );
```

<a id="guide-async--using-directly-with-the-digester"></a>

### Using directly with the Digester

First of all, setup the Digester with java.util.concurrent.ExecutorService:

```
Digester digester = new Digester();
digester.addObjectCreate( "employee", Employee.class);
...
digester.setExecutorService( java.util.concurrent.Executors.newFixedThreadPool( 10 ) );
```

Then run the parse method asynchronously:

```
Future<Employee> future = digester.asyncParse( new URL( "http://my.rest.server/employees/10" ) );
```

---

<a id="guide-substitution"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/substitution.html -->

<!-- page_index: 7 -->

<a id="guide-substitution--package-documentation-for-org.apache.commons.digester3.substitution-package"></a>

## Package Documentation for org.apache.commons.digester3.substitution Package

Provides for manipulation of xml attributes and element body text before
the data is processed by any Rule objects.

The class org.apache.commons.digester3.Substitutor defines an abstract
interface for mechanisms which manipulate xml attributes and body text.
The Digester method setSubstitutor can be used to define a concrete
substitutor that will be applied to the data before it is passed to the
matching rules.

This package provides some useful concrete implementations of the abstract
Substitutor class. In particular, it provides an implementation that allows
the application to define "variables" which the input data can reference
using a syntax such as ${user.name}.

Here's an example of setting up the VariableSubstitutor:

```

  // set up the variables the input xml can reference
  Map<String, Object> vars = new HashMap<String, Object>();
  vars.put( "user.name", "me" );
  vars.put( "os", "Linux" );

  // map ${varname} to the entries in the var map
  MultiVariableExpander expander = new MultiVariableExpander();
  expander.addSource( "$", vars );

  // allow expansion in both xml attributes and element text
  Substitutor substitutor = new VariableSubstitutor( expander );

  Digester digester = new Digester();
  digester.setSubstitutor( substitutor );
```

---

<a id="guide-xmlrules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/xmlrules.html -->

<!-- page_index: 8 -->

<a id="guide-xmlrules--documentation-for-org.apache.commons.digester3.xmlrules"></a>

## Documentation for org.apache.commons.digester3.xmlrules

The xmlrules package provides for XML-based definition of
rules for Digester. This improves maintainability of Java code, as rules are now defined in XML and read into Digester at run-time.

<a id="guide-xmlrules--introduction"></a>

### Introduction

This is a brief overview of the digester-rules-in-XML feature. Briefly, this feature lets you define Digester rules in XML, instead of
creating and initializing the Rules objects programmatically, which can become
tedious. In addition, it allows for including of one XML rules file within
another, inclusion of programmatically created rule sets within an XML file
(via reflection), and recursively nested matching pattern specifications.

<a id="guide-xmlrules--overview-of-digester-rules.dtd"></a>

### Overview of digester-rules.dtd

A DTD, named digester-rules.dtd has been defined to help in the
understanding of how the loader operates.

The DTD is distributed in the commons-digester3-3.0.jar. It can be found at
org/apache/commons/digester3/xmlrules/digester-rules.dtd.

Digester input documents wishing to cite this DTD should include the
following DOCTYPE declaration:

```

<!DOCTYPE digester-rules PUBLIC
  "-//Apache Commons //DTD digester-rules XML V1.0//EN"
  "http://commons.apache.org/digester/dtds/digester-rules-3.0.dtd">
```

<a id="guide-xmlrules--rule-elements"></a>

### Rule elements

The DTD defines an element type corresponding to each predefined Digester
rule. Each rule element type includes attributes for values needed to
initialize the rule, and an optional pattern attribute
specifying the pattern to associate with the rule.

The DigesterLoader adds the rules to the digester in the order in
which they occur in the XML.

The use of each rule element type should be self-explanatory, if you compare
them to the API documentation for the Digester rules classes.

<a id="guide-xmlrules--defining-matching-patterns"></a>

### Defining matching patterns

The matching pattern is a simple, xpath-like string which the
Digester uses to determine which elements to apply each rule to.
See the Digester [documentation](#guide-core) for
more details.

There are two methods for associating patterns to rules in the XML file. One
is for each rule element to directly define its pattern in a
pattern attribute. An example would like something like:

```

<digester-rules>
  <object-create-rule pattern="*/foo" classname="Foo" />
  <set-properties-rule pattern="*/foo" />
</digester-rules>
```

In the above example, an ObjectCreateRule is created and
associated with the pattern "\*/foo"; then a SetPropertiesRule is
created and associated with the pattern "\*/foo".

The other method is to nest rules elements inside a
<pattern> element. In this way, the same pattern can be
defined for a group of rules. The following example has the same effect as the
previous example:

```

<digester-rules>
  <pattern value="*/foo">
    <object-create-rule classname="Foo" />
    <set-properties-rule />
  </pattern>
</digester-rules>
```

Pattern elements can be recursively nested. If patterns are nested, the pattern
string is formed by concatenating all the patterns together. Example:

```

<digester-rules>
  <pattern value="*/foo">
    <pattern value="bar">
      <object-create-rule classname="Foobar" />
      <set-properties-rule />
    </pattern>
  </pattern>
</digester-rules>
```

In the above example, an ObjectCreateRule and a
SetPropertiesRule are associated with the matching pattern
"\*/foo/bar".

The use of pattern elements and the use of the pattern attribute inside rules
elements can be freely mixed. The next example has the same effect as the
previous example:

```

<digester-rules>
  <pattern value="*/foo">
    <object-create-rule pattern="bar" classname="Foobar" />
    <set-properties-rule pattern="bar" />
  </pattern>
</digester-rules>
```

<a id="guide-xmlrules--including-rules-xml-files-within-other-rules-xml-files"></a>

### Including rules XML files within other rules XML files

The <include> element lets you include one rules file within
another. With respect to pattern concatenation, the DigesterLoader
behaves as if the include file was 'macro-expanded'. Example:

```

File rules1.xml:

<?xml version="1.0"?>
<!DOCTYPE digester-rules PUBLIC
  "-//Apache Commons //DTD digester-rules XML V1.0//EN"
  "http://commons.apache.org/digester/dtds/digester-rules-3.0.dtd">
<digester-rules>
  <pattern value="root/foo">
    <object-create-rule classname="Foo" />

    <include url="classpath:/rules2.xml" />
  </pattern>
</digester-rules>



File rules2.xml:

<?xml version="1.0"?>
<!DOCTYPE digester-rules PUBLIC
  "-//Apache Commons //DTD digester-rules XML V1.0//EN"
  "http://commons.apache.org/digester/dtds/digester-rules-3.0.dtd">
<digester-rules>
  <pattern value="bar">
    <object-create-rule classname="Bar" />
  </pattern>
</digester-rules>
```

Note that the *url* attribute accepts any valid URL, plus the the meta classpath URL, that points to a any valid resource present in the ClassPath; the ClassLoader used to load the resources
is the same users set to resolve classes during the parse-time.

Parsing rule1.xml would result in a Digester initialized with these
pattern/rule pairs:

```

root/foo -> ObjectCreateRule(Foo)

root/foo/bar -> ObjectCreateRule(Bar)
```

Note that the pattern for the bar rule has been prepended with the root/foo
pattern. If rule2.xml was parsed by itself, it would yield a Digester
initialized with this pattern/rule:

```

bar -> ObjectCreateRule(Bar)
```

<a id="guide-xmlrules--including-programmatically-created-rules"></a>

### Including programmatically-created rules

Sometimes rules cannot be easily defined via XML. Rule sets that are created
programmatically can still be included within a digester-rules XML file. This
is done by using an <include> element with a
class attribute, containing the name of a class that implements
org.apache.commons.digester3.binder.RulesModule.
The pattern concatenation works exactly as if the rules had been included from an XML file, i.e.:

```

File rules3.xml:

<?xml version="1.0"?>
<!DOCTYPE digester-rules PUBLIC
  "-//Apache Commons //DTD digester-rules XML V1.0//EN"
  "http://commons.apache.org/digester/dtds/digester-rules-3.0.dtd">
<digester-rules>
  <pattern value="root/foo">
    <object-create-rule classname="Foo" />

    <include class="BarRuleModule" />
  </pattern>
</digester-rules>
```

BarRuleCreator class definition:

```

public class BarRuleModule
    extends AbstractRulesModule
{

    @Override
    public void configure()
    {
        forPattern( "bar" ).objectCreate().ofType( Bar.class );
    }

}
```

Parsing rules3.xml yields the same results as rules1.xml above:

```

root/foo -> ObjectCreateRule(Foo)

root/foo/bar -> ObjectCreateRule(Bar)
```

<a id="guide-xmlrules--creating-a-digester-from-xml"></a>

### Creating a digester from XML

[FromXmlRulesModule](https://commons.apache.org/proper/commons-digester/apidocs/org/apache/commons/digester3/xmlrules/FromXmlRulesModule.html) is a RulesModule implementation that
initializes its Digester from rules defined in one or more XML files. The
path to the XML files are passed in the configure() method, i.e.

```

public class MyRulesModule
    extends FromXmlRulesModule
{

    @Override
    protected void loadRules()
    {
        loadXMLRules( new URL( "http://www.acme.com/shared/config/digester-rules.xml" ) );
        loadXMLRules( new File( "/etc/digester-rules.xml" ) );
    }

}
```

The MyRulesModule can be reused now by the DigesterLoader
to create Digester instances:

```
import static org.apache.commons.digester3.binder.DigesterLoader.newLoader;

import org.apache.commons.digester3.Digester;
import org.apache.commons.digester3.binder.DigesterLoader;
...
DigesterLoader loader = newLoader( new MyRulesModule() );
...
Digester digester= loader.newDigester();
```

---

<a id="guide-annotations"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/annotations.html -->

<!-- page_index: 9 -->

<a id="guide-annotations--annotations"></a>

## Annotations

The annotations package provides for Java5 Annotations
meta-data based definition of rules for Digester.
This improves maintainability of both Java code and XML documents, as
rules are now defined in POJOs and generating Digester
parsers at run-time, avoiding manual updates.

<a id="guide-annotations--introduction"></a>

### Introduction

This is a brief overview of the digester-rules-in-Java5 Annotations
feature. Inspired by the basic idea behind the JPA, BeanValidation and
JAXB's specifications, this feature lets you define Digester rules
directly in target POJOs, instead of creating and initializing the Rules
objects programmatically, which can become tedious.

<a id="guide-annotations--annotation-rules"></a>

### Annotation Rules

A digester rule on a POJO is expressed through one or more annotations.
An annotation is considered a digester rule definition if its retention
policy contains RUNTIME and if the annotation itself is annotated with
org.apache.commons.digester3.annotations.DigesterRule.

The DigesterRule is defined by the combination of:

- the reflected Class<? extends org.apache.commons.digester3.Rule>
  by the annotation;
- the org.apache.commons.digester3.annotations.AnnotationHandler
  class that has to be invoked during the target class traversal.

Digester annotations can target any of the following ElementTypes:

- FIELD for Digester rules concerning attributes;
- METHOD for Digester rules concerning methods calls;
- PARAMETER for Digester rules concerning methods parameters setting;
- TYPE for Digester rules concerning types creation.

While other ElementTypes are not forbidden, the Digester
annotations processor does not have to recognize and process annotation
rules placed on such types.

Every Digester rule annotation **must** define a *pattern*
element of type String that represents the element matching
path pattern, and the *namespaceURI* for which the Rule is relevant.

```
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@CreationRule
@DigesterRule(
    reflectsRule = ObjectCreateRule.class,
    providedBy = ObjectCreateRuleProvider.class
)
public @interface ObjectCreate
{

    String pattern();

    String namespaceURI() default "";

}
```

<a id="guide-annotations--applying-multiple-annotation-rule-of-the-same-type"></a>

### Applying multiple annotation rule of the same type

It is often useful to declare the same annotation rule more than once
to the same target, with different properties. To support this requirement, the Digester annotation processor treats annotations annotated by
@org.apache.commons.digester3.annotations.DigesterRuleList
whose value element has a return type of an array of rule
annotations in a special way. Each element in the value array are processed
by the Digester annotation processor as regular annotation rule annotations.
This means that each Digester rule specified in the value
element is applied to the target. The annotation must have retention
RUNTIME and can be applied on a type, field, method or
method parameter. It is recommended to use the same set of targets as
the initial Digester annotation rule.

Note to designers: each Digester annotation rule should be coupled
with its corresponding multi-valued annotation.
It is recommended, though not mandated, the definition of
an inner annotation named List.

```
@Documented
@Retention( RetentionPolicy.RUNTIME )
@Target( ElementType.TYPE )
@CreationRule
@DigesterRule(
    reflectsRule = ObjectCreateRule.class,
    handledBy = ObjectCreateHandler.class
)
public @interface ObjectCreate
{

    String pattern();

    String namespaceURI() default "";

    @Documented
    @Retention( RetentionPolicy.RUNTIME )
    @Target( ElementType.TYPE )
    @DigesterRuleList
    @interface List
    {
        ObjectCreate[] value();
    }

}
```

<a id="guide-annotations--annotationhandler-implementation"></a>

### AnnotationHandler implementation

An AnnotationHandler implementation performs the rule binding
of a given annotation for a given annotated element. The implementation
classes are specified by the handledBy element of the
@DigesterRule annotation that decorates the rule annotation
definition. The rule provider implementation implements the
org.apache.commons.digester3.annotations.AnnotationHandler<A extends Annotation, E extends AnnotatedElement>
interface.

```
class ObjectCreateHandler
    implements AnnotationHandler<ObjectCreate, Class<?>>
{

    public void handle( ObjectCreate annotation, Class<?> element, RulesBinder rulesBinder )
    {
        rulesBinder.forPattern( annotation.pattern() )
            .withNamespaceURI( annotation.namespaceURI() )
            .createObject()
                .ofType( element )
                .ofTypeSpecifiedByAttribute( annotation.attributeName() != null ? annotation.attributeName() : null );
    }

}
```

<a id="guide-annotations--notes"></a>

##### Notes

A new instance of the AnnotationHandler will be created each time the Digester
annotations processor will meet the relative rule that requests it.

To supply the missing AnnotatedElement for methods
PARAMETERs, the Digester annotation processor come with the
org.apache.commons.digester.annotations.reflect.MethodArgument
class.

<a id="guide-annotations--built-in-rules"></a>

### Built-in Rules

All built-in annotation rules are in the package
org.apache.commons.digester3.annotations.rules.
Here is the list of annotations and their usage.

<a id="guide-annotations--type-annotations"></a>

#### TYPE annotations

| Annotation | Reflect rule |
| --- | --- |
| @ObjectCreate | org.apache.commons.digester3.ObjectCreateRule |
| @FactoryCreate | org.apache.commons.digester3.FactoryCreateRule |

<a id="guide-annotations--field-annotations"></a>

#### FIELD annotations

| Annotation | Reflect rule |
| --- | --- |
| @BeanPropertySetter | org.apache.commons.digester3.BeanPropertySetterRule |
| @SetProperty | org.apache.commons.digester3.SetPropertiesRule |

<a id="guide-annotations--method-annotations"></a>

#### METHOD annotations

| Annotation | Reflect rule |
| --- | --- |
| @CallMethod | org.apache.commons.digester3.CallMethodRule |
| @SetNext | org.apache.commons.digester3.SetNextRule |
| @SetRoot | org.apache.commons.digester3.SetRootRule |
| @SetTop | org.apache.commons.digester3.SetTopRule |

<a id="guide-annotations--parameter-annotations"></a>

#### PARAMETER annotations

| Annotation | Reflect rule |
| --- | --- |
| @CallParam | org.apache.commons.digester3.rule.CallParamRule |

<a id="guide-annotations--bootstrapping"></a>

### Bootstrapping

The core of Digester annotations rules processor is the
org.apache.commons.digester3.annotations.FromAnnotationsRuleModule class, a specialization of
org.apache.commons.digester3.RulesModule.

A FromAnnotationsRuleModule
instance is able to analyze Class<?> graphs and builds
the relative rule bindings to create
org.apache.commons.digester3.Digester instances.

An org.apache.commons.digester3.annotations.AnnotationHandlerFactory
implementation performs the creation of
org.apache.commons.digester3.annotations.AnnotationHandler<A extends Annotation, E extends AnnotatedElement>
instances; the default implementation is limited to create the handler
by invoking the default empty constructor of the required class, but
users are free to give their implementation if they need a more complex
factory, i.e. providers requires components that could be injected from a
context, etc. etc.

Said that, to obtain a fresh new
org.apache.commons.digester3.binder.DigesterLoader instance
with default factories, it is enough extending the
org.apache.commons.digester3.annotations.FromAnnotationsRuleModule class:

```
class MyModule
    extends FromAnnotationsRuleModule
{

    @Override
    protected void configureRules()
    {
        bindRulesFrom( MyType1.class );
        bindRulesFrom( MyType2.class );
        bindRulesFrom( MyType3.class );
        ...
    }

}
```

Otherwise, if users need specify their custom factory:

```
class MyModule
    extends FromAnnotationsRuleModule
{

    @Override
    protected void configureRules()
    {
        useAnnotationHandlerFactory( new MyAnnotationHandlerFactory() );
        ...
        bindRulesFrom( MyType1.class );
        bindRulesFrom( MyType2.class );
        bindRulesFrom( MyType3.class );
        ...
    }

}
```

<a id="guide-annotations--example:-a-simple-rss-parser"></a>

### Example: a simple RSS parser

Let's assume there is the need to parse the following (simplified)
XML/RSS feed:

```
<rss version="2.0">
  <channel>

    <title>Apache</title>
    <link>http://www.apache.org</link>
    <description>The Apache Software Foundation</description>
    <language>en-US</language>
    <rating>(PICS-1.1 "http://www.rsac.org/ratingsv01.html"
      2 gen true comment "RSACi North America Server"
      for "http://www.rsac.org" on "1996.04.16T08:15-0500"
      r (n 0 s 0 v 0 l 0))</rating>

    <image>
      <title>Apache</title>
      <url>http://jakarta.apache.org/images/jakarta-logo.gif</url>
      <link>http://jakarta.apache.org</link>
      <width>505</width>
      <height>480</height>
      <description>The Jakarta project. Open source, serverside java.</description>
    </image>

    <item>
      <title>Commons Attributes 2.1 Released</title>
      <link>http://jakarta.apache.org/site/news/news-2004-2ndHalf.html#20040815.1</link>
      <description>The Apache Commons team is happy to announce the release of Commons Attributes 2.1.
      This is the first release of the new Commons-Attributes code.</description>
    </item>

    <item>
      <title>Cloudscape Becomes Apache Derby</title>
      <link>http://jakarta.apache.org/site/news/elsewhere-2004-2ndHalf.html#20040803.1</link>
      <description>IBM has submitted a proposal to the Apache DB project for a Java-based package to be called 'Derby'.</description>
    </item>

    <item>
      <title>Commons BeanUtils 1.7 Released</title>
      <link>http://jakarta.apache.org/site/news/news-2004-2ndHalf.html#20040802.1</link>
      <description/>
    </item>

    <item>
      <title>Commons JXPath 1.2 Released</title>
      <link>http://jakarta.apache.org/site/news/news-2004-2ndHalf.html#20040801.2</link>
      <description/>
    </item>
  </channel>
</rss>
```

So, let's define the Java entities and annotate them; first the Channel entity:

```
@ObjectCreate( pattern = "rss/channel" )
class Channel
{

    private final List<Item> items = new ArrayList<Item>();

    @BeanPropertySetter( pattern = "rss/channel/title" )
    private String title;

    @BeanPropertySetter( pattern = "rss/channel/link" )
    private String link;

    @BeanPropertySetter( pattern = "rss/channel/description" )
    private String description;

    @BeanPropertySetter( pattern = "rss/channel/language" )
    private String language;

    private Image image;

    // getters and setters

    @SetNext
    public void setImage( Image image )
    {
        this.image = image;
    }

    @SetNext
    public void addItem( Item item )
    {
        this.items.add( item );
    }

}
```

Then the Image entity:

```
@ObjectCreate( pattern = "rss/channel/image" )
class Image
{

    @BeanPropertySetter( pattern = "rss/channel/image/description" )
    private String description;

    @BeanPropertySetter( pattern = "rss/channel/image/width" )
    private int width;

    @BeanPropertySetter( pattern = "rss/channel/image/height" )
    private int height;

    @BeanPropertySetter( pattern = "rss/channel/image/link" )
    private String link;

    @BeanPropertySetter( pattern = "rss/channel/image/title" )
    private String title;

    @BeanPropertySetter( pattern = "rss/channel/image/url" )
    private String url;

    // getters and setters

}
```

and finally the Item entity:

```
@ObjectCreate( pattern = "rss/channel/item" )
class Item
{

    @BeanPropertySetter( pattern = "rss/channel/item/description" )
    private String description;

    @BeanPropertySetter( pattern = "rss/channel/item/link" )
    private String link;

    @BeanPropertySetter( pattern = "rss/channel/item/title" )
    private String title;

    // getters and setters

}
```

It is now possible to create the Digester instance and parse the XML:

```
import static org.apache.commons.digester3.binder.DigesterLoader.newLoader;

import org.apache.commons.digester3.Digester;
import org.apache.commons.digester3.binder.DigesterLoader;
...
DigesterLoader loader = newLoader( new FromAnnotationsRuleModule()
    {

        @Override
        protected void configureRules()
        {
            bindRulesFrom( Channel.class );
        }

    } );
...
Digester digester = digesterLoader.newDigester();
try
{
    Channel channel = digester.parse( new URL( "http://www.myfeedprovider.com/rss.xml" ).openStream() );
}
catch (Exception e)
{
    // do something
}
    
```

---

<a id="guide-faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/guide/faq.html -->

<!-- page_index: 10 -->

<a id="guide-faq--frequently-asked-questions"></a>

## Frequently Asked Questions

1. [Why do I get warnings when using a JAXP 1.1 parser?](#guide-faq--jaxp_1_1_warnings)
2. [Why Doesn't Schema Validation Work With Parser XXX Out Of The Box?](#guide-faq--schema_validation_out_box)
3. [Help!
   I'm Validating Against Schema But Digester Ignores Errors!](#guide-faq--help)
4. [Where Can I Find Example Code?](#guide-faq--example_code)
5. [When Are You Going To Support *Rich Site Summary* Version x.y.z?](#guide-faq--support_rich_site)
6. [Does my old Digester 2.X code continue working once upgraded to Digester 3?](#guide-faq--upgrade_digester3)

Why do I get warnings when using a JAXP 1.1 parser?
:   If you're using a JAXP 1.1 parser, you might see the following warning (in your log):


```

[WARN] Digester - -Error: JAXP SAXParser property not recognized: http://java.sun.com/xml/jaxp/properties/schemaLanguage
```

    This property is needed for JAXP 1.2 (XML Schema support) as required
    for the Servlet Spec. 2.4 but is not recognized by JAXP 1.1 parsers.
    This warning is harmless.

    ---

Why Doesn't Schema Validation Work With Parser XXX Out Of The Box?
:   Schema location and language settings are often need for validation using schemas.
    Unfortunately, there isn't a single standard approach to how these properties are
    configured on a parser.
    Digester tries to guess the parser being used and configure it appropriately
    but it's not infallible.
    You might need to grab an instance, configure it and pass it to Digester.

    If you want to support more than one parser in a portable manner,
    then you'll probably want to take a look at the
    org.apache.commons.digester.parsers package
    and add a new class to support the particular parser that's causing problems.

    ---

Help! I'm Validating Against Schema But Digester Ignores Errors!
:   Digester is based on [SAX](http://www.saxproject.org). The convention for
    SAX parsers is that all errors are reported (to any registered
    ErrorHandler) but processing continues. Digester (by default)
    registers its own ErrorHandler implementation. This logs details
    but does not stop the processing (following the usual convention for SAX
    based processors).

    This means that the errors reported by the validation of the schema will appear in the
    Digester logs but the processing will continue. To change this behaviour, call
    digester.setErrorHandler with a more suitable implementation.

    ---

Where Can I Find Example Code?
:   Digester ships with a sample application: a mapping for the *Rich Site
    Summary* format used by many newsfeeds. Download the source distribution
    to see how it works.

    Digester also ships with a set of examples demonstrating most of the
    features described in this document. See the "src/examples" subdirectory
    of the source distribution.

    ---

When Are You Going To Support *Rich Site Summary* Version x.y.z?
:   The *Rich Site Summary* application is intended to be a sample application.
    It works but we have no plans to add support for other versions of the format.

    We would consider donations of standard digester applications but it's unlikely that
    these would ever be shipped with the base digester distribution.
    If you want to discuss this, please post to [commons dev mailing list](http://commons.apache.org/mail-lists.html)

    ---

Does my old Digester 2.X code continue working once upgraded to Digester 3?
:   No, class imports have to be updated to org.apache.commons.digester3 otherwise Digester and Rule classes won't be found.
    Old XML Rules and Annotations rule extensions are not 100% compatible, please refer to related documentation.

---

<a id="commons-digester-2.1-core"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/commons-digester-2.1/core.html -->

<!-- page_index: 11 -->

<a id="commons-digester-2.1-core--external-dependencies"></a>

## External Dependencies

The *Digester* component Version 2.0 is dependent upon implementations of the following
standard libraries:

- **XML Parser** compatible with the JAXP/1.3 specification.
  Compatible implementations are included in JDKs 1.5 and above.

It is also dependent on a compatible set of
[Apache Commons](http://commons.apache.org/) library components.
The recommended dependency set is:

>
| Recommended Dependency Set |
| --- |
| Digester | +Logging 1.1.1 | +BeanUtils 1.8.3 |

It is also possible to use Logging 1.0.x or BeanUtils 1.8.0 instead.

<a id="commons-digester-2.1-core--introduction"></a>

## Introduction

In many application environments that deal with XML-formatted data, it is
useful to be able to process an XML document in an "event driven" manner, where particular Java objects are created (or methods of existing objects
are invoked) when particular patterns of nested XML elements have been
recognized. Developers familiar with the Simple API for XML Parsing (SAX)
approach to processing XML documents will recognize that the Digester provides
a higher level, more developer-friendly interface to SAX events, because most
of the details of navigating the XML element hierarchy are hidden -- allowing
the developer to focus on the processing to be performed.

In order to use a Digester, the following basic steps are required:

- Create a new instance of the
  `org.apache.commons.digester.Digester` class. Previously
  created Digester instances may be safely reused, as long as you have
  completed any previously requested parse, and you do not try to utilize
  a particular Digester instance from more than one thread at a time.
- Set any desired [configuration properties](#commons-digester-2.1-core--doc.properties)
  that will customize the operation of the Digester when you next initiate
  a parse operation.
- Optionally, push any desired initial object(s) onto the Digester's
  [object stack](#commons-digester-2.1-core--doc.stack).
- Register all of the [element matching patterns](#commons-digester-2.1-core--doc.patterns)
  for which you wish to have [processing rules](#commons-digester-2.1-core--doc.rules)
  fired when this pattern is recognized in an input document. You may
  register as many rules as you like for any particular pattern. If there
  is more than one rule for a given pattern, the rules will be executed in
  the order that they were listed.
- Call the `digester.parse()` method, passing a reference to the
  XML document to be parsed in one of a variety of forms. See the
  [Digester.parse()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#parse(java.io.File))
  documentation for details. Note that you will need to be prepared to
  catch any `IOException` or `SAXException` that is
  thrown by the parser, or any runtime expression that is thrown by one of
  the processing rules.

Alternatively a Digester may be used as a sax event hander, as follows:

- Create an instance of a sax parser (using the JAXP APIs or otherwise).
- Set any desired configuration properties on that parser object.
- Create an instance of `org.apache.commons.digester.Digester`.
- Optionally, push any desired initial object(s) onto the Digester's
  [object stack](#commons-digester-2.1-core--doc.stack).
- Register patterns and rules with the digester instance.
- Call parser.parse(inputSource, digester).

For example code, see  [the usage
examples](#commons-digester-2.1-core--doc.usage), and  [the FAQ](#commons-digester-2.1-core--doc.faq.examples) .

<a id="commons-digester-2.1-core--configuration-properties"></a>

## Configuration Properties

A `org.apache.commons.digester.Digester` instance contains several
configuration properties that can be used to customize its operation. These
properties **must** be configured before you call one of the
`parse()` variants, in order for them to take effect on that
parse.

>
| Property | Description |
| --- | --- |
| classLoader | You can optionally specify the class loader that will be used to load classes when required by the `ObjectCreateRule` and `FactoryCreateRule` rules. If not specified, application classes will be loaded from the thread's context class loader (if the `useContextClassLoader` property is set to `true`) or the same class loader that was used to load the `Digester` class itself. |
| errorHandler | You can optionally specify a SAX `ErrorHandler` that is notified when parsing errors occur. By default, any parsing errors that are encountered are logged, but Digester will continue processing as well. |
| namespaceAware | A boolean that is set to `true` to perform parsing in a manner that is aware of XML namespaces. Among other things, this setting affects how elements are matched to processing rules. See [Namespace Aware Parsing](#commons-digester-2.1-core--doc.namespace) for more information. |
| xincludeAware | A boolean that is set to `true` to perform parsing in a manner that is aware of XInclude W3C specification. This setting is only effective if the parsing is already configured to be namespace aware. |
| ruleNamespaceURI | The public URI of the namespace for which all subsequently added rules are associated, or `null` for adding rules that are not associated with any namespace. See [Namespace Aware Parsing](#commons-digester-2.1-core--doc.namespace) for more information. |
| rules | The `Rules` component that actually performs matching of `Rule` instances against the current element nesting pattern is pluggable. By default, Digester includes a `Rules` implementation that behaves as described in this document. See [Pluggable Rules Processing](#commons-digester-2.1-core--doc.pluggable) for more information. |
| useContextClassLoader | A boolean that is set to `true` if you want application classes required by `FactoryCreateRule` and `ObjectCreateRule` to be loaded from the context class loader of the current thread. By default, classes will be loaded from the class loader that loaded this `Digester` class. **NOTE** - This property is ignored if you set a value for the `classLoader` property; that class loader will be used unconditionally. |
| validating | A boolean that is set to `true` if you wish to validate the XML document against a Document Type Definition (DTD) that is specified in its `DOCTYPE` declaration. The default value of `false` requests a parse that only detects "well formed" XML documents, rather than "valid" ones. |

In addition to the scalar properties defined above, you can also register
a local copy of a Document Type Definition (DTD) that is referenced in a
`DOCTYPE` declaration. Such a registration tells the XML parser
that, whenever it encounters a `DOCTYPE` declaration with the
specified public identifier, it should utilize the actual DTD content at the
registered system identifier (a URL), rather than the one in the
`DOCTYPE` declaration.

For example, the Struts framework controller servlet uses the following
registration in order to tell Struts to use a local copy of the DTD for the
Struts configuration file. This allows usage of Struts in environments that
are not connected to the Internet, and speeds up processing even at Internet
connected sites (because it avoids the need to go across the network).

```

    URL url = new URL("/org/apache/struts/resources/struts-config_1_0.dtd");
    digester.register
      ("-//Apache Software Foundation//DTD Struts Configuration 1.0//EN",
       url.toString());
```

As a side note, the system identifier used in this example is the path
that would be passed to `java.lang.ClassLoader.getResource()`
or `java.lang.ClassLoader.getResourceAsStream()`. The actual DTD
resource is loaded through the same class loader that loads all of the Struts
classes -- typically from the `struts.jar` file.

<a id="commons-digester-2.1-core--the-object-stack"></a>

## The Object Stack

One very common use of `org.apache.commons.digester.Digester`
technology is to dynamically construct a tree of Java objects, whose internal
organization, as well as the details of property settings on these objects, are configured based on the contents of the XML document. In fact, the
primary reason that the Digester package was created (it was originally part
of Struts, and then moved to the Commons project because it was recognized
as being generally useful) was to facilitate the
way that the Struts controller servlet configures itself based on the contents
of your application's `struts-config.xml` file.

To facilitate this usage, the Digester exposes a stack that can be
manipulated by processing rules that are fired when element matching patterns
are satisfied. The usual stack-related operations are made available, including the following:

- [clear()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#clear()) - Clear the current contents
  of the object stack.
- [peek()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#peek()) - Return a reference to the top
  object on the stack, without removing it.
- [pop()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#pop()) - Remove the top object from the
  stack and return it.
- [push()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#push(java.lang.Object)) - Push a new
  object onto the top of the stack.

A typical design pattern, then, is to fire a rule that creates a new object
and pushes it on the stack when the beginning of a particular XML element is
encountered. The object will remain there while the nested content of this
element is processed, and it will be popped off when the end of the element
is encountered. As we will see, the standard "object create" processing rule
supports exactly this functionalility in a very convenient way.

Several potential issues with this design pattern are addressed by other
features of the Digester functionality:

- *How do I relate the objects being created to each other?* - The
  Digester supports standard processing rules that pass the top object on
  the stack as an argument to a named method on the next-to-top object on
  the stack (or vice versa). This rule makes it easy to establish
  parent-child relationships between these objects. One-to-one and
  one-to-many relationships are both easy to construct.
- *How do I retain a reference to the first object that was created?*
  As you review the description of what the "object create" processing rule
  does, it would appear that the first object you create (i.e. the object
  created by the outermost XML element you process) will disappear from the
  stack by the time that XML parsing is completed, because the end of the
  element would have been encountered. However, Digester will maintain a
  reference to the very first object ever pushed onto the object stack,
  and will return it to you
  as the return value from the `parse()` call. Alternatively,
  you can push a reference to some application object onto the stack before
  calling `parse()`, and arrange that a parent-child relationship
  be created (by appropriate processing rules) between this manually pushed
  object and the ones that are dynamically created. In this way,
  the pushed object will retain a reference to the dynamically created objects
  (and therefore all of their children), and will be returned to you after
  the parse finishes as well.

<a id="commons-digester-2.1-core--element-matching-patterns"></a>

## Element Matching Patterns

A primary feature of the `org.apache.commons.digester.Digester`
parser is that the Digester automatically navigates the element hierarchy of
the XML document you are parsing for you, without requiring any developer
attention to this process. Instead, you focus on deciding what functions you
would like to have performed whenver a certain arrangement of nested elements
is encountered in the XML document being parsed. The mechanism for specifying
such arrangements are called *element matching patterns*.

The Digester can be configured to use different pattern-matching algorithms
via the Digester.setRules method. However for the vast majority of cases, the
default matching algorithm works fine. The default pattern matching behaviour
is described below.

A very simple element matching pattern is a simple string like "a". This
pattern is matched whenever an `<a>` top-level element is
encountered in the XML document, no matter how many times it occurs. Note that
nested `<a>` elements will **not** match this
pattern -- we will describe means to support this kind of matching later.

The next step up in matching pattern complexity is "a/b". This pattern will
be matched when a `<b>` element is found nested inside a
top-level `<a>` element. Again, this match can occur as many
times as desired, depending on the content of the XML document being parsed.
You can use multiple slashes to define a hierarchy of any desired depth that
will be matched appropriately.

For example, assume you have registered processing rules that match patterns
"a", "a/b", and "a/b/c". For an input XML document with the following
contents, the indicated patterns will be matched when the corresponding element
is parsed:

```

  <a>         -- Matches pattern "a"
    <b>       -- Matches pattern "a/b"
      <c/>    -- Matches pattern "a/b/c"
      <c/>    -- Matches pattern "a/b/c"
    </b>
    <b>       -- Matches pattern "a/b"
      <c/>    -- Matches pattern "a/b/c"
      <c/>    -- Matches pattern "a/b/c"
      <c/>    -- Matches pattern "a/b/c"
    </b>
  </a>
```

It is also possible to match a particular XML element, no matter how it is
nested (or not nested) in the XML document, by using the "\*" wildcard character
in your matching pattern strings. For example, an element matching pattern
of "\*/a" will match an `<a>` element at any nesting position
within the document.

It is quite possible that, when a particular XML element is being parsed, the pattern for more than one registered processing rule will be matched
because you registered more than one processing rule with the exact same
matching pattern.

When this occurs, the corresponding processing rules will all be fired in
order. Rule methods `begin` (and `body`) are executed in
the order that the `Rules` were initially registered with the
`Digester`, whilst `end` method calls are executed in
reverse order. In other words - the order is first in, last out.

Note that wildcard patterns are ignored if an explicit match can be found
(and when multiple wildcard patterns match, only the longest, ie most
explicit, pattern is considered a match). The result is that rules can be
added for "an <a> tag anywhere", but then for that behaviour to be
explicitly overridden for specific cases, eg "but not an <a> that is a
direct child of an <x>". Therefore if you have rules A and B registered for
pattern "\*/a" then want to add an additional rule C for pattern "x/a" only, then what you need to do is add \*three\* rules for "x/a": A, B and C. Note
that by using:

```

  Rule ruleA = new ObjectCreateRule();
  Rule ruleB = new SetNextRule();
  Rule ruleC = new SetPropertiesRule();

  digester.addRule("*/a", ruleA);
  digester.addRule("*/a", ruleB);
  digester.addRule("x/a", ruleA);
  digester.addRule("x/a", ruleB);
  digester.addRule("x/a", ruleC);
```

you have associated the same rule instances A and B with multiple patterns, thus avoiding creating extra rule object instances.

<a id="commons-digester-2.1-core--processing-rules"></a>

## Processing Rules

The [previous section](#commons-digester-2.1-core--doc.patterns) documented how you identify
**when** you wish to have certain actions take place. The purpose
of processing rules is to define **what** should happen when the
patterns are matched.

Formally, a processing rule is a Java class that subclasses the
[org.apache.commons.digester.Rule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Rule.html) interface. Each Rule
implements one or more of the following event methods that are called at
well-defined times when the matching patterns corresponding to this rule
trigger it:

- [begin()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Rule.html#begin(org.xml.sax.AttributeList)) -
  Called when the beginning of the matched XML element is encountered. A
  data structure containing all of the attributes corresponding to this
  element are passed as well.
- [body()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Rule.html#body(java.lang.String)) -
  Called when nested content (that is not itself XML elements) of the
  matched element is encountered. Any leading or trailing whitespace will
  have been removed as part of the parsing process.
- [end()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Rule.html#end()) - Called when the ending of the matched
  XML element is encountered. If nested XML elements that matched other
  processing rules was included in the body of this element, the appropriate
  processing rules for the matched rules will have already been completed
  before this method is called.
- [finish()](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Rule.html#finish()) - Called when the parse has
  been completed, to give each rule a chance to clean up any temporary data
  they might have created and cached.

As you are configuring your digester, you can call the
`addRule()` method to register a specific element matching pattern, along with an instance of a `Rule` class that will have its event
handling methods called at the appropriate times, as described above. This
mechanism allows you to create `Rule` implementation classes
dynamically, to implement any desired application specific functionality.

In addition, a set of processing rule implementation classes are provided, which deal with many common programming scenarios. These classes include the
following:

- [ObjectCreateRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/ObjectCreateRule.html) - When the
  `begin()` method is called, this rule instantiates a new
  instance of a specified Java class, and pushes it on the stack. The
  class name to be used is defaulted according to a parameter passed to
  this rule's constructor, but can optionally be overridden by a classname
  passed via the specified attribute to the XML element being processed.
  When the `end()` method is called, the top object on the stack
  (presumably, the one we added in the `begin()` method) will
  be popped, and any reference to it (within the Digester) will be
  discarded.
- [FactoryCreateRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/FactoryCreateRule.html) - A variation of
  `ObjectCreateRule` that is useful when the Java class with
  which you wish to create an object instance does not have a no-arguments
  constructor, or where you wish to perform other setup processing before
  the object is handed over to the Digester.
- [SetPropertiesRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/SetPropertiesRule.html) - When the
  `begin()` method is called, the digester uses the standard
  Java Reflection API to identify any JavaBeans property setter methods
  (on the object at the top of the digester's stack)
  who have property names that match the attributes specified on this XML
  element, and then call them individually, passing the corresponding
  attribute values. These natural mappings can be overridden. This allows
  (for example) a `class` attribute to be mapped correctly.
  It is recommended that this feature should not be overused - in most cases,
  it's better to use the standard `BeanInfo` mechanism.
  A very common idiom is to define an object create
  rule, followed by a set properties rule, with the same element matching
  pattern. This causes the creation of a new Java object, followed by
  "configuration" of that object's properties based on the attributes
  of the same XML element that created this object.
- [SetPropertyRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/SetPropertyRule.html) - When the
  `begin()` method is called, the digester calls a specified
  property setter (where the property itself is named by an attribute)
  with a specified value (where the value is named by another attribute),
  on the object at the top of the digester's stack.
  This is useful when your XML file conforms to a particular DTD, and
  you wish to configure a particular property that does not have a
  corresponding attribute in the DTD.
- [SetNextRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/SetNextRule.html) - When the
  `end()` method is called, the digester analyzes the
  next-to-top element on the stack, looking for a property setter method
  for a specified property. It then calls this method, passing the object
  at the top of the stack as an argument. This rule is commonly used to
  establish one-to-many relationships between the two objects, with the
  method name commonly being something like "addChild".
- [SetTopRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/SetTopRule.html) - When the
  `end()` method is called, the digester analyzes the
  top element on the stack, looking for a property setter method for a
  specified property. It then calls this method, passing the next-to-top
  object on the stack as an argument. This rule would be used as an
  alternative to a SetNextRule, with a typical method name "setParent",
  if the API supported by your object classes prefers this approach.
- [CallMethodRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/CallMethodRule.html) - This rule sets up a
  method call to a named method of the top object on the digester's stack,
  which will actually take place when the `end()` method is
  called. You configure this rule by specifying the name of the method
  to be called, the number of arguments it takes, and (optionally) the
  Java class name(s) defining the type(s) of the method's arguments.
  The actual parameter values, if any, will typically be accumulated from
  the body content of nested elements within the element that triggered
  this rule, using the CallParamRule discussed next.
- [CallParamRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/CallParamRule.html) - This rule identifies
  the source of a particular numbered (zero-relative) parameter for a
  CallMethodRule within which we are nested. You can specify that the
  parameter value be taken from a particular named attribute, or from the
  nested body content of this element.
- [NodeCreateRule](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/NodeCreateRule.html) - A specialized rule
  that converts part of the tree into a `DOM Node` and then
  pushes it onto the stack.

You can create instances of the standard `Rule` classes and
register them by calling `digester.addRule()`, as described above.
However, because their usage is so common, shorthand registration methods are
defined for each of the standard rules, directly on the `Digester`
class. For example, the following code sequence:

```

    Rule rule = new SetNextRule(digester, "addChild",
                                "com.mycompany.mypackage.MyChildClass");
    digester.addRule("a/b/c", rule);
```

can be replaced by:

```

    digester.addSetNext("a/b/c", "addChild",
                        "com.mycompany.mypackage.MyChildClass");
```

<a id="commons-digester-2.1-core--logging"></a>

## Logging

Logging is a vital tool for debugging Digester rulesets. Digester can log
copious amounts of debugging information. So, you need to know how logging
works before you start using Digester seriously.

Digester uses
[Apache Commons
Logging](http://commons.apache.org/logging). This component is not really a logging framework - rather
an extensible, configurable bridge. It can be configured to swallow all log
messages, to provide very basic logging by itself or to pass logging messages
on to more sophisticated logging frameworks. Commons-Logging comes with
connectors for many popular logging frameworks. Consult the commons-logging
documentation for more information.

Two main logs are used by Digester:

- SAX-related messages are logged to
  **`org.apache.commons.digester.Digester.sax`**.
  This log gives information about the basic SAX events received by
  Digester.
- **`org.apache.commons.digester.Digester`** is used
  for everything else. You'll probably want to have this log turned up during
  debugging but turned down during production due to the high message
  volume.

Complete documentation of how to configure Commons-Logging can be found
in the Commons Logging package documentation. However, as a simple example, let's assume that you want to use the `SimpleLog` implementation
that is included in Commons-Logging, and set up Digester to log events from
the `Digester` logger at the DEBUG level, while you want to log
events from the `Digester.log` logger at the INFO level. You can
accomplish this by creating a `commons-logging.properties` file
in your classpath (or setting corresponding system properties on the command
line that starts your application) with the following contents:

```

  org.apache.commons.logging.Log=org.apache.commons.logging.impl.SimpleLog
  org.apache.commons.logging.simplelog.log.org.apache.commons.digester.Digester=debug
  org.apache.commons.logging.simplelog.log.org.apache.commons.digester.Digester.sax=info
```

<a id="commons-digester-2.1-core--usage-example"></a>

## Usage Example

<a id="commons-digester-2.1-core--creating-a-simple-object-tree"></a>

### Creating a Simple Object Tree

Let's assume that you have two simple JavaBeans, `Foo` and
`Bar`, with the following method signatures:

```

  package mypackage;
  public class Foo {
    public void addBar(Bar bar);
    public Bar findBar(int id);
    public Iterator getBars();
    public String getName();
    public void setName(String name);
  }

  package mypackage;
  public class Bar {
    public int getId();
    public void setId(int id);
    public String getTitle();
    public void setTitle(String title);
  }
```

and you wish to use Digester to parse the following XML document:

```

  <foo name="The Parent">
    <bar id="123" title="The First Child"/>
    <bar id="456" title="The Second Child"/>
  </foo>
```

A simple approach will be to use the following Digester in the following way
to set up the parsing rules, and then process an input file containing this
document:

```

  Digester digester = new Digester();
  digester.setValidating(false);
  digester.addObjectCreate("foo", "mypackage.Foo");
  digester.addSetProperties("foo");
  digester.addObjectCreate("foo/bar", "mypackage.Bar");
  digester.addSetProperties("foo/bar");
  digester.addSetNext("foo/bar", "addBar", "mypackage.Bar");
  Foo foo = (Foo) digester.parse();
```

In order, these rules do the following tasks:

1. When the outermost `<foo>` element is encountered,
   create a new instance of `mypackage.Foo` and push it
   on to the object stack. At the end of the `<foo>`
   element, this object will be popped off of the stack.
2. Cause properties of the top object on the stack (i.e. the `Foo`
   object that was just created and pushed) to be set based on the values
   of the attributes of this XML element.
3. When a nested `<bar>` element is encountered,
   create a new instance of `mypackage.Bar` and push it
   on to the object stack. At the end of the `<bar>`
   element, this object will be popped off of the stack (i.e. after the
   remaining rules matching `foo/bar` are processed).
4. Cause properties of the top object on the stack (i.e. the `Bar`
   object that was just created and pushed) to be set based on the values
   of the attributes of this XML element. Note that type conversions
   are automatically performed (such as String to int for the `id`
   property), for all converters registered with the `ConvertUtils`
   class from `commons-beanutils` package.
5. Cause the `addBar` method of the next-to-top element on the
   object stack (which is why this is called the "set *next*" rule)
   to be called, passing the element that is on the top of the stack, which
   must be of type `mypackage.Bar`. This is the rule that causes
   the parent/child relationship to be created.

Once the parse is completed, the first object that was ever pushed on to the
stack (the `Foo` object in this case) is returned to you. It will
have had its properties set, and all of its child `Bar` objects
created for you.

<a id="commons-digester-2.1-core--processing-a-struts-configuration-file"></a>

### Processing A Struts Configuration File

As stated earlier, the primary reason that the
`Digester` package was created is because the
Struts controller servlet itself needed a robust, flexible, easy to extend
mechanism for processing the contents of the `struts-config.xml`
configuration that describes nearly every aspect of a Struts-based application.
Because of this, the controller servlet contains a comprehensive, real world, example of how the Digester can be employed for this type of a use case.
See the `initDigester()` method of class
`org.apache.struts.action.ActionServlet` for the code that creates
and configures the Digester to be used, and the `initMapping()`
method for where the parsing actually takes place.

(Struts binary and source distributions can be acquired at
<http://struts.apache.org>.)

The following discussion highlights a few of the matching patterns and
processing rules that are configured, to illustrate the use of some of the
Digester features. First, let's look at how the Digester instance is
created and initialized:

```

    Digester digester = new Digester();
    digester.push(this); // Push controller servlet onto the stack
    digester.setValidating(true);
```

We see that a new Digester instance is created, and is configured to use
a validating parser. Validation will occur against the struts-config\_1\_0.dtd
DTD that is included with Struts (as discussed earlier). In order to provide
a means of tracking the configured objects, the controller servlet instance
itself will be added to the digester's stack.

```

    digester.addObjectCreate("struts-config/global-forwards/forward",
                             forwardClass, "className");
    digester.addSetProperties("struts-config/global-forwards/forward");
    digester.addSetNext("struts-config/global-forwards/forward",
                        "addForward",
                        "org.apache.struts.action.ActionForward");
    digester.addSetProperty
      ("struts-config/global-forwards/forward/set-property",
       "property", "value");
```

The rules created by these lines are used to process the global forward
declarations. When a `<forward>` element is encountered, the following actions take place:

- A new object instance is created -- the `ActionForward`
  instance that will represent this definition. The Java class name
  defaults to that specified as an initialization parameter (which
  we have stored in the String variable `forwardClass`), but can
  be overridden by using the "className" attribute (if it is present in the
  XML element we are currently parsing). The new `ActionForward`
  instance is pushed onto the stack.
- The properties of the `ActionForward` instance (at the top of
  the stack) are configured based on the attributes of the
  `<forward>` element.
- Nested occurrences of the `<set-property>` element
  cause calls to additional property setter methods to occur. This is
  required only if you have provided a custom implementation of the
  `ActionForward` class with additional properties that are
  not included in the DTD.
- The `addForward()` method of the next-to-top object on
  the stack (i.e. the controller servlet itself) will be called, passing
  the object at the top of the stack (i.e. the `ActionForward`
  instance) as an argument. This causes the global forward to be
  registered, and as a result of this it will be remembered even after
  the stack is popped.
- At the end of the `<forward>` element, the top element
  (i.e. the `ActionForward` instance) will be popped off the
  stack.

Later on, the digester is actually executed as follows:

```

    InputStream input =
      getServletContext().getResourceAsStream(config);
    ...
    try {
        digester.parse(input);
        input.close();
    } catch (SAXException e) {
        ... deal with the problem ...
    }
```

As a result of the call to `parse()`, all of the configuration
information that was defined in the `struts-config.xml` file is
now represented as collections of objects cached within the Struts controller
servlet, as well as being exposed as servlet context attributes.

<a id="commons-digester-2.1-core--parsing-body-text-in-xml-files"></a>

### Parsing Body Text In XML Files

The Digester module also allows you to process the nested body text in an
XML file, not just the elements and attributes that are encountered. The
following example is based on an assumed need to parse the web application
deployment descriptor (`/WEB-INF/web.xml`) for the current web
application, and record the configuration information for a particular
servlet. To record this information, assume the existence of a bean class
with the following method signatures (among others):

```

  package com.mycompany;
  public class ServletBean {
    public void setServletName(String servletName);
    public void setServletClass(String servletClass);
    public void addInitParam(String name, String value);
  }
```

We are going to process the `web.xml` file that declares the
controller servlet in a typical Struts-based application (abridged for
brevity in this example):

```

  <web-app>
    ...
    <servlet>
      <servlet-name>action</servlet-name>
      <servlet-class>org.apache.struts.action.ActionServlet<servlet-class>
      <init-param>
        <param-name>application</param-name>
        <param-value>org.apache.struts.example.ApplicationResources<param-value>
      </init-param>
      <init-param>
        <param-name>config</param-name>
        <param-value>/WEB-INF/struts-config.xml<param-value>
      </init-param>
    </servlet>
    ...
  </web-app>
```

Next, lets define some Digester processing rules for this input file:

```

  digester.addObjectCreate("web-app/servlet",
                           "com.mycompany.ServletBean");
  digester.addCallMethod("web-app/servlet/servlet-name", "setServletName", 0);
  digester.addCallMethod("web-app/servlet/servlet-class",
                         "setServletClass", 0);
  digester.addCallMethod("web-app/servlet/init-param",
                         "addInitParam", 2);
  digester.addCallParam("web-app/servlet/init-param/param-name", 0);
  digester.addCallParam("web-app/servlet/init-param/param-value", 1);
```

Now, as elements are parsed, the following processing occurs:

- *<servlet>* - A new `com.mycompany.ServletBean`
  object is created, and pushed on to the object stack.
- *<servlet-name>* - The `setServletName()` method
  of the top object on the stack (our `ServletBean`) is called,
  passing the body content of this element as a single parameter.
- *<servlet-class>* - The `setServletClass()` method
  of the top object on the stack (our `ServletBean`) is called,
  passing the body content of this element as a single parameter.
- *<init-param>* - A call to the `addInitParam`
  method of the top object on the stack (our `ServletBean`) is
  set up, but it is **not** called yet. The call will be
  expecting two `String` parameters, which must be set up by
  subsequent call parameter rules.
- *<param-name>* - The body content of this element is assigned
  as the first (zero-relative) argument to the call we are setting up.
- *<param-value>* - The body content of this element is assigned
  as the second (zero-relative) argument to the call we are setting up.
- *</init-param>* - The call to `addInitParam()`
  that we have set up is now executed, which will cause a new name-value
  combination to be recorded in our bean.
- *<init-param>* - The same set of processing rules are fired
  again, causing a second call to `addInitParam()` with the
  second parameter's name and value.
- *</servlet>* - The element on the top of the object stack
  (which should be the `ServletBean` we pushed earlier) is
  popped off the object stack.

<a id="commons-digester-2.1-core--namespace-aware-parsing"></a>

## Namespace Aware Parsing

For digesting XML documents that do not use XML namespaces, the default
behavior of `Digester`, as described above, is generally sufficient.
However, if the document you are processing uses namespaces, it is often
convenient to have sets of `Rule` instances that are *only*
matched on elements that use the prefix of a particular namespace. This
approach, for example, makes it possible to deal with element names that are
the same in different namespaces, but where you want to perform different
processing for each namespace.

Digester does not provide full support for namespaces, but does provide
sufficient to accomplish most tasks. Enabling digester's namespace support
is done by following these steps:

1. Tell `Digester` that you will be doing namespace
   aware parsing, by adding this statement in your initalization
   of the Digester's properties:


```

    digester.setNamespaceAware(true);
    
```

2. Declare the public namespace URI of the namespace with which
   following rules will be associated. Note that you do *not*
   make any assumptions about the prefix - the XML document author
   is free to pick whatever prefix they want:


```

    digester.setRuleNamespaceURI("http://www.mycompany.com/MyNamespace");
    
```

3. Add the rules that correspond to this namespace, in the usual way,
   by calling methods like `addObjectCreate()` or
   `addSetProperties()`. In the matching patterns you specify,
   use only the *local name* portion of the elements (i.e. the
   part after the prefix and associated colon (":") character:


```

    digester.addObjectCreate("foo/bar", "com.mycompany.MyFoo");
    digester.addSetProperties("foo/bar");
    
```

4. Repeat the previous two steps for each additional public namespace URI
   that should be recognized on this `Digester` run.

Now, consider that you might wish to digest the following document, using
the rules that were set up in the steps above:

```

<m:foo
   xmlns:m="http://www.mycompany.com/MyNamespace"
   xmlns:y="http://www.yourcompany.com/YourNamespace">

  <m:bar name="My Name" value="My Value"/>

  <y:bar id="123" product="Product Description"/>L

</x:foo>
```

Note that your object create and set properties rules will be fired for the
*first* occurrence of the `bar` element, but not the
*second* one. This is because we declared that our rules only matched
for the particular namespace we are interested in. Any elements in the
document that are associated with other namespaces (or no namespaces at all)
will not be processed. In this way, you can easily create rules that digest
only the portions of a compound document that they understand, without placing
any restrictions on what other content is present in the document.

You might also want to look at [Encapsulated
Rule Sets](#commons-digester-2.1-core--doc.rulesets) if you wish to reuse a particular set of rules, associated
with a particular namespace, in more than one application context.

<a id="commons-digester-2.1-core--using-namespace-prefixes-in-pattern-matching"></a>

### Using Namespace Prefixes In Pattern Matching

Using rules with namespaces is very useful when you have orthogonal rulesets.
One ruleset applies to a namespace and is independent of other rulesets applying
to other namespaces. However, if your rule logic requires mixed namespaces, then
matching namespace prefix patterns might be a better strategy.

When you set the `NamespaceAware` property to false, digester uses
the qualified element name (which includes the namespace prefix) rather than the
local name as the patten component for the element. This means that your pattern
matches can include namespace prefixes as well as element names. So, rather than
create namespace-aware rules, create pattern matches including the namespace
prefixes.

For example, (with `NamespaceAware` false), the pattern `'foo:bar'` will match a top level element named `'bar'` in the
namespace with (local) prefix `'foo'`.

<a id="commons-digester-2.1-core--limitations-of-digester-namespace-support"></a>

#### Limitations of Digester Namespace support

Digester does not provide general "xpath-compliant" matching;
only the namespace attached to the *last* element in the match path
is involved in the matching process. Namespaces attached to parent
elements are ignored for matching purposes.

<a id="commons-digester-2.1-core--pluggable-rules-processing"></a>

## Pluggable Rules Processing

By default, `Digester` selects the rules that match a particular
pattern of nested elements as described under
[Element Matching Patterns](#commons-digester-2.1-core--doc.patterns). If you prefer to use
different selection policies, however, you can create your own implementation
of the [org.apache.commons.digester.Rules](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Rules.html) interface, or subclass the corresponding convenience base class
[org.apache.commons.digester.RulesBase](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/RulesBase.html).
Your implementation of the `match()` method will be called when the
processing for a particular element is started or ended, and you must return
a `List` of the rules that are relevant for the current nesting
pattern. The order of the rules you return **is** significant, and should match the order in which rules were initally added.

Your policy for rule selection should generally be sensitive to whether
[Namespace Aware Parsing](#commons-digester-2.1-core--doc.namespace) is taking place. In
general, if `namespaceAware` is true, you should select only rules
that:

- Are registered for the public namespace URI that corresponds to the
  prefix being used on this element.
- Match on the "local name" portion of the element (so that the document
  creator can use any prefix that they like).

<a id="commons-digester-2.1-core--extendedbaserules"></a>

### ExtendedBaseRules

[ExtendedBaseRules](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/ExtendedBaseRules.html), adds some additional expression syntax for pattern matching
to the default mechanism, but it also executes more slowly. See the
JavaDocs for more details on the new pattern matching syntax, and suggestions
on when this implementation should be used. To use it, simply do the
following as part of your Digester initialization:

```

  Digester digester = ...
  ...
  digester.setRules(new ExtendedBaseRules());
  ...
```

<a id="commons-digester-2.1-core--regexrules"></a>

### RegexRules

[RegexRules](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/RegexRules.html) is an advanced `Rules`
implementation which does not build on the default pattern matching rules.
It uses a pluggable [RegexMatcher](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/RegexMatcher.html) implementation to test
if a path matches the pattern for a Rule. All matching rules are returned
(note that this behaviour differs from longest matching rule of the default
pattern matching rules). See the Java Docs for more details.

Example usage:

```

  Digester digester = ...
  ...
  digester.setRules(new RegexRules(new SimpleRegexMatcher()));
  ...
```

<a id="commons-digester-2.1-core--regexmatchers"></a>

### RegexMatchers

`Digester` ships only with one `RegexMatcher`
implementation: [SimpleRegexMatcher](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/SimpleRegexMatcher.html).
This implementation is unsophisticated and lacks many good features
lacking in more power Regex libraries. There are some good reasons
why this approach was adopted. The first is that `SimpleRegexMatcher`
is simple, it is easy to write and runs quickly. The second has to do with
the way that `RegexRules` is intended to be used.

There are many good regex libraries available. (For example
[Jakarta ORO](http://jakarta.apache.org/oro/index.html), [Jakarta Regex](http://jakarta.apache.org/regexp/index.html), [GNU Regex](http://www.cacas.org/java/gnu/regexp/) and
[Java 1.4 Regex](http://java.sun.com/j2se/1.4.2/docs/api/java/util/regex/package-summary.html))
Not only do different people have different personal tastes when it comes to
regular expression matching but these products all offer different functionality
and different strengths.

The pluggable `RegexMatcher` is a thin bridge
designed to adapt other Regex systems. This allows any Regex library the user
desires to be plugged in and used just by creating one class.
`Digester` does not (currently) ship with bridges to the major
regex (to allow the dependencies required by `Digester`
to be kept to

<a id="commons-digester-2.1-core--withdefaultsruleswrapper"></a>

### WithDefaultsRulesWrapper

[WithDefaultsRulesWrapper](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocsWithDefaultsRulesWrapper.html) allows
default `Rule` instances to be added to any existing
`Rules` implementation. These default `Rule` instances
will be returned for any match for which the wrapped implementation does not
return any matches.

For example,

```

    Rule alpha;
    ...
    WithDefaultsRulesWrapper rules = new WithDefaultsRulesWrapper(new BaseRules());
    rules.addDefault(alpha);
    ...
    digester.setRules(rules);
    ...
```

when a pattern does not match any other rule, then rule alpha will be called.

`WithDefaultsRulesWrapper` follows the *Decorator* pattern.

<a id="commons-digester-2.1-core--encapsulated-rule-sets"></a>

## Encapsulated Rule Sets

All of the examples above have described a scenario where the rules to be
processed are registered with a `Digester` instance immediately
after it is created. However, this approach makes it difficult to reuse the
same set of rules in more than one application environment. Ideally, one
could package a set of rules into a single class, which could be easily
loaded and registered with a `Digester` instance in one easy step.

The [RuleSet](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/RuleSet.html) interface (and the convenience base
class [RuleSetBase](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/RuleSetBase.html)) make it possible to do this.
In addition, the rule instances registered with a particular
`RuleSet` can optionally be associated with a particular namespace, as described under [Namespace Aware Processing](#commons-digester-2.1-core--doc.namespace).

An example of creating a `RuleSet` might be something like this:

```

public class MyRuleSet extends RuleSetBase {

  public MyRuleSet() {
    this("");
  }

  public MyRuleSet(String prefix) {
    super();
    this.prefix = prefix;
    this.namespaceURI = "http://www.mycompany.com/MyNamespace";
  }

  protected String prefix = null;

  public void addRuleInstances(Digester digester) {
    digester.addObjectCreate(prefix + "foo/bar",
      "com.mycompany.MyFoo");
    digester.addSetProperties(prefix + "foo/bar");
  }

}
```

You might use this `RuleSet` as follow to initialize a
`Digester` instance:

```

  Digester digester = new Digester();
  ... configure Digester properties ...
  digester.addRuleSet(new MyRuleSet("baz/"));
```

A couple of interesting notes about this approach:

- The application that is using these rules does not need to know anything
  about the fact that the `RuleSet` being used is associated
  with a particular namespace URI. That knowledge is emedded inside the
  `RuleSet` class itself.
- If desired, you could make a set of rules work for more than one
  namespace URI by providing constructors on the `RuleSet` to
  allow this to be specified dynamically.
- The `MyRuleSet` example above illustrates another technique
  that increases reusability -- you can specify (as an argument to the
  constructor) the leading portion of the matching pattern to be used.
  In this way, you can construct a `Digester` that recognizes
  the same set of nested elements at different nesting levels within an
  XML document.

<a id="commons-digester-2.1-core--using-named-stacks-for-inter-rule-communication"></a>

## Using Named Stacks For Inter-Rule Communication

`Digester` is based on `Rule` instances working together
to process xml. For anything other than the most trival processing, communication between `Rule` instances is necessary. Since `Rule`
instances are processed in sequence, this usually means storing an Object
somewhere where later instances can retrieve it.

`Digester` is based on SAX. The most natural data structure to use with
SAX based xml processing is the stack. This allows more powerful processes to be
specified more simply since the pushing and popping of objects can mimic the
nested structure of the xml.

`Digester` uses two basic stacks: one for the main beans and the other
for parameters for method calls. These are inadequate for complex processing
where many different `Rule` instances need to communicate through
different channels.

In this case, it is recommended that named stacks are used. In addition to the
two basic stacks, `Digester` allows rules to use an unlimited number
of other stacks referred to by an identifying string (the name). (That's where
the term *named stack* comes from.) These stacks are
accessed through calls to:

- [void push(String stackName, Object value)](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#push(java.lang.String, java.lang.Object))
- [Object pop(String stackName)](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#pop(java.lang.String))
- [Object peek(String stackName)](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/Digester.html#peek(java.lang.String))

**Note:** all stack names beginning with `org.apache.commons.digester`
are reserved for future use by the `Digester` component. It is also recommended
that users choose stack names prefixed by the name of their own domain to avoid conflicts
with other `Rule` implementations.

<a id="commons-digester-2.1-core--registering-dtds"></a>

## Registering DTDs

<a id="commons-digester-2.1-core--brief-but-still-too-long-introduction-to-system-and-public-identifiers"></a>

### Brief (But Still Too Long) Introduction To System and Public Identifiers

A definition for an external entity comes in one of two forms:

1. `SYSTEM system-identifier`
2. `PUBLIC public-identifiersystem-identifier`

The `system-identifier` is an URI from which the resource can be obtained
(either directly or indirectly). Many valid URIs may identify the same resource.
The `public-identifier` is an additional free identifier which may be used
(by the parser) to locate the resource.

In practice, the weakness with a `system-identifier` is that most parsers
will attempt to interprete this URI as an URL, try to download the resource directly
from the URL and stop the parsing if this download fails. So, this means that
almost always the URI will have to be an URL from which the declaration
can be downloaded.

URLs may be local or remote but if the URL is chosen to be local, it is likely only
to function correctly on a small number of machines (which are configured precisely
to allow the xml to be parsed). This is usually unsatisfactory and so a universally
accessable URL is preferred. This usually means an internet URL.

To recap, in practice the `system-identifier` will (most likely) be an
internet URL. Unfortunately downloading from an internet URL is not only slow
but unreliable (since successfully downloading a document from the internet
relies on the client being connect to the internet and the server being
able to satisfy the request).

The `public-identifier` is a freely defined name but (in practice) it is
strongly recommended that a unique, readable and open format is used (for reasons
that should become clear later). A Formal Public Identifier (FPI) is a very
common choice. This public identifier is often used to provide a unique and location
independent key which can be used to subsistute local resources for remote ones
(hint: this is why ;).

By using the second (`PUBLIC`) form combined with some form of local
catalog (which matches `public-identifiers` to local resources) and where
the `public-identifier` is a unique name and the `system-identifier`
is an internet URL, the practical disadvantages of specifying just a
`system-identifier` can be avoided. Those external entities which have been
store locally (on the machine parsing the document) can be identified and used.
Only when no local copy exists is it necessary to download the document
from the internet URL. This naming scheme is recommended when using `Digester`.

<a id="commons-digester-2.1-core--external-entity-resolution-using-digester"></a>

### External Entity Resolution Using Digester

SAX factors out the resolution of external entities into an `EntityResolver`.
`Digester` supports the use of custom `EntityResolver`
but ships with a simple internal implementation. This implementation allows local URLs
to be easily associated with `public-identifiers`.

For example:

```

    digester.register("-//Example Dot Com //DTD Sample Example//EN", "assets/sample.dtd");
```

will make digester return the relative file path `assets/sample.dtd`
whenever an external entity with public id
`-//Example Dot Com //DTD Sample Example//EN` is needed.

**Note:** This is a simple (but useful) implementation.
Greater sophistication requires a custom `EntityResolver`.

<a id="commons-digester-2.1-core--troubleshooting"></a>

## Troubleshooting

<a id="commons-digester-2.1-core--debugging-exceptions"></a>

### Debugging Exceptions

`Digester` is based on [SAX](http://www.saxproject.org).
Digestion throws two kinds of `Exception`:

- `java.io.IOException`
- `org.xml.sax.SAXException`

The first is rarely thrown and indicates the kind of fundemental IO exception
that developers know all about. The second is thrown by SAX parsers when the processing
of the XML cannot be completed. So, to diagnose the cause a certain familiarity with
the way that SAX error handling works is very useful.

<a id="commons-digester-2.1-core--diagnosing-sax-exceptions"></a>

### Diagnosing SAX Exceptions

This is a short, potted guide to SAX error handling strategies. It's not intended as a
proper guide to error handling in SAX.

When a SAX parser encounters a problem with the xml (well, ok - sometime after it
encounters a problem) it will throw a
[SAXParseException](http://www.saxproject.org/apidoc/org/xml/sax/SAXParseException.html). This is a subclass of `SAXException` and contains
a bit of extra information about what exactly when wrong - and more importantly, where it went wrong. If you catch an exception of this sort, you can be sure that
the problem is with the XML and not `Digester` or your rules.
It is usually a good idea to catch this exception and log the extra information
to help with diagnosing the reason for the failure.

General [SAXException](http://www.saxproject.org/apidoc/org/xml/sax/SAXException.html) instances may wrap a causal exception. When exceptions are
throw by `Digester` each of these will be wrapped into a
`SAXException` and rethrown. So, catch these and examine the wrapped
exception to diagnose what went wrong.

<a id="commons-digester-2.1-core--extensions"></a>

## Extensions

Three extension packages are included within the Digester distribution.
These provide extra functionality extending the core Digester concepts.
Detailed descriptions are contained within their own package documentation.

- [plugins](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/plugins/package-summary.html) provides a framework for the easy
  dynamic addition of rules during a Digestion. Rules can trigger the dynamic addition
  of other rules in an intuitive fashion.
- [substitution](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/substitution/package-summary.html) provides for
  manipulation of attributes and element body text before it is processed by the rules.
- [xmlrules](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/xmlrules/package-summary.html) package contains a
  system allowing digester rule configurations to be specifed through an xml file.
- [annotations](https://commons.apache.org/proper/commons-digester/commons-digester-2.1/apidocs/annotations/package-summary.html) package contains a
  system allowing digester rule configurations to be specifed through Java5 Annotations.

<a id="commons-digester-2.1-core--known-limitations"></a>

## Known Limitations

<a id="commons-digester-2.1-core--accessing-public-methods-in-a-default-access-superclass"></a>

### Accessing Public Methods In A Default Access Superclass

There is an issue when invoking public methods contained in a default access superclass.
Reflection locates these methods fine and correctly assigns them as public.
However, an `IllegalAccessException` is thrown if the method is invoked.

`MethodUtils` contains a workaround for this situation.
It will attempt to call `setAccessible` on this method.
If this call succeeds, then the method can be invoked as normal.
This call will only succeed when the application has sufficient security privilages.
If this call fails then a warning will be logged and the method may fail.

`Digester` uses `MethodUtils` and so there may be an issue accessing methods
of this kind from a high security environment. If you think that you might be experiencing this
problem, please ask on the mailing list.

---

<a id="commons-digester-2.1-substitution"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/commons-digester-2.1/substitution.html -->

<!-- page_index: 12 -->

<a id="commons-digester-2.1-substitution--package-documentation-for-org.apache.commons.digester.substitution-package"></a>

## Package Documentation for org.apache.commons.digester.substitution Package

Provides for manipulation of xml attributes and element body text before
the data is processed by any Rule objects.

The class org.apache.commons.digester.Substitutor defines an abstract
interface for mechanisms which manipulate xml attributes and body text.
The Digester method setSubstitutor can be used to define a concrete
substitutor that will be applied to the data before it is passed to the
matching rules.

This package provides some useful concrete implementations of the abstract
Substitutor class. In particular, it provides an implementation that allows
the application to define "variables" which the input data can reference
using a syntax such as "${user.name}".

Here's an example of setting up the VariableSubstitutor:

```

  // set up the variables the input xml can reference
  Map vars = new HashMap();
  vars.put("user.name", "me");
  vars.put("os", "Linux");

  // map ${varname} to the entries in the var map
  MultiVariableExpander expander = new MultiVariableExpander();
  expander.addSource("$", vars);

  // allow expansion in both xml attributes and element text
  Substitutor substitutor = new VariableSubstitutor(expander);

  Digester digester = new Digester();
  digester.setSubstitutor(substitutor);
```

---

<a id="commons-digester-2.1-xmlrules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/commons-digester-2.1/xmlrules.html -->

<!-- page_index: 13 -->

<a id="commons-digester-2.1-xmlrules--documentation-for-org.apache.commons.digester.xmlrules"></a>

## Documentation for org.apache.commons.digester.xmlrules

The `xmlrules` package provides for XML-based definition of
rules for `Digester`. This improves maintainability of Java code, as rules are now defined in XML and read into `Digester` at run-time.

<a id="commons-digester-2.1-xmlrules--introduction"></a>

### Introduction

This is a brief overview of the digester-rules-in-XML feature. Briefly, this feature lets you define Digester rules in XML, instead of
creating and initializing the Rules objects programmatically, which can become
tedious. In addition, it allows for including of one XML rules file within
another, inclusion of programmatically created rule sets within an XML file
(via reflection), and recursively nested matching pattern specifications.

<a id="commons-digester-2.1-xmlrules--overview-of-digester-rules.dtd"></a>

### Overview of digester-rules.dtd

A DTD, named `digester-rules.dtd` has been defined to help in the
understanding of how the loader operates.

The DTD is distributed in the `commons-digester.jar`. It can be found at
`org/apache/commons/digester/xmlrules/digester-rules.dtd`. It is not available
for download from the Apache website since users are best advised to use a copy stored
on their local system.

Digester input documents wishing to cite this DTD should include the
following DOCTYPE declaration:

```

  <!DOCTYPE digester-rules PUBLIC
   "-//Jakarta Apache //DTD digester-rules XML V1.0//EN"
   "digester-rules.dtd">
```

<a id="commons-digester-2.1-xmlrules--rule-elements"></a>

### Rule elements

The DTD defines an element type corresponding to each predefined Digester
rule. Each rule element type includes attributes for values needed to
initialize the rule, and an optional `pattern` attribute
specifying the pattern to associate with the rule.

The `DigesterLoader` adds the rules to the digester in the order in
which they occur in the XML.

The use of each rule element type should be self-explanatory, if you compare
them to the API documentation for the `Digester` rules classes.

<a id="commons-digester-2.1-xmlrules--defining-matching-patterns"></a>

### Defining matching patterns

The matching pattern is a simple, xpath-like string which the
`Digester` uses to determine which elements to apply each rule to.
See the `Digester`[documentation](https://commons.apache.org/core.html) for
more details.

There are two methods for associating patterns to rules in the XML file. One
is for each rule element to directly define its pattern in a
`pattern` attribute. An example would like something like:

```

      <digester-rules>
        <object-create-rule pattern="*/foo" classname="Foo"/>
        <set-properties-rule pattern="*/foo"/>
      </digester-rules>
```

In the above example, an `ObjectCreateRule` is created and
associated with the pattern "\*/foo"; then a `SetPropertiesRule` is
created and associated with the pattern "\*/foo".

The other method is to nest rules elements inside a
`<pattern>` element. In this way, the same pattern can be
defined for a group of rules. The following example has the same effect as the
previous example:

```

       <digester-rules>
         <pattern value="*/foo">
           <object-create-rule classname="Foo"/>
           <set-properties-rule/>
         </pattern>
       </digester-rules>
```

Pattern elements can be recursively nested. If patterns are nested, the pattern
string is formed by concatenating all the patterns together. Example:

```

       <digester-rules>
         <pattern value="*/foo">
           <pattern value="bar">
             <object-create-rule classname="Foobar"/>
             <set-properties-rule/>
           </pattern>
         </pattern>
       </digester-rules>
```

In the above example, an `ObjectCreateRule` and a
`SetPropertiesRule` are associated with the matching pattern
"\*/foo/bar".

The use of pattern elements and the use of the pattern attribute inside rules
elements can be freely mixed. The next example has the same effect as the
previous example:

```

       <digester-rules>
         <pattern value="*/foo">
           <object-create-rule pattern="bar" classname="Foobar"/>
           <set-properties-rule pattern="bar"/>
         </pattern>
       </digester-rules>
```

<a id="commons-digester-2.1-xmlrules--including-rules-xml-files-within-other-rules-xml-files"></a>

### Including rules XML files within other rules XML files

The `<include>` element lets you include one rules file within
another. With respect to pattern concatenation, the `DigesterLoader`
behaves as if the include file was 'macro-expanded'. Example:

```

      File rules1.xml:
         <?xml version="1.0"?>
         <!DOCTYPE digester-rules SYSTEM "digester-rules.dtd">

         <digester-rules>
           <pattern value="root/foo">
             <object-create-rule classname="Foo"/>

             <include path="rules2.xml"/>
           </pattern>
         </digester-rules>


      File rules2.xml:
         <?xml version="1.0"?>
         <!DOCTYPE digester-rules SYSTEM "digester-rules.dtd">

         <digester-rules>
           <pattern value="bar">
             <object-create-rule classname="Bar"/>
           </pattern>
         </digester-rules>
```

Parsing rule1.xml would result in a `Digester` initialized with these
pattern/rule pairs:

```

    root/foo -> ObjectCreateRule(Foo)

    root/foo/bar -> ObjectCreateRule(Bar)
```

Note that the pattern for the 'bar' rule has been prepended with the 'root/foo'
pattern. If rule2.xml was parsed by itself, it would yield a `Digester`
initialized with this pattern/rule:

```

    bar -> ObjectCreateRule(Bar)
```

<a id="commons-digester-2.1-xmlrules--including-programmatically-created-rules"></a>

### Including programmatically-created rules

Sometimes rules cannot be easily defined via XML. Rule sets that are created
programmatically can still be included within a digester-rules XML file. This
is done by using an `<include>` element with a
`class` attribute, containing the name of a class that implements
`org.apache.commons.digester.xmlrules.DigesterRulesSource`.
This interface defines one method, `getRules(Digester)`, which
creates rules and adds them to the supplied Digester. The pattern concatenation
works exactly as if the rules had been included from an XML file. Example:

```

      File rules3.xml:
         <?xml version="1.0"?>
         <!DOCTYPE digester-rules SYSTEM "digester-rules.dtd">

         <digester-rules>
           <pattern value="root/foo">
             <object-create-rule classname="Foo"/>

             <include class="BarRuleCreator"/>
           </pattern>
         </digester-rules>
```

BarRuleCreator class definition:

```

          public class BarRuleCreator implements DigesterRulesSource {
              public void getRules(Digester digester) {
                  digester.addObjectCreate("bar", "Bar");
              }
          }
```

Parsing rules3.xml yields the same results as rules1.xml above:

```

    root/foo -> ObjectCreateRule(Foo)

    root/foo/bar -> ObjectCreateRule(Bar)
```

<a id="commons-digester-2.1-xmlrules--creating-a-digester-from-xml"></a>

### Creating a digester from XML

`FromXmlRuleSet` is a `RuleSet` implementation that
initializes its `Digester` from rules defined in an XML file. The
path to the XML file is passed to constructor.

Alternatively, the convenience class `DigesterLoader` defines a
static method, `Digester createDigester(String rulesXml) throws DigesterLoaderException`".
When passing the name of the file that contains your digester rules, this
method returns a `Digester` instance initialized with the rules.

To add your own rules, you need to:

- Update the DTD
  You should add an element type for your rule. The
  element should have an attribute corresponding to each of the rule's
  initialization parameters.
- Define an `ObjectCreationFactory`
- Extend `DigesterRuleParser`
  `DigesterRuleParser`
  is a `RuleSet` for parsing a rules XML file. You should extend this,
  and override the `addRuleInstances()` method to add the rules for
  parsing your new element. Look in DigesterRuleParser.java to see how its done.

---

<a id="commons-digester-2.1-annotations"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/commons-digester-2.1/annotations.html -->

<!-- page_index: 14 -->

<a id="commons-digester-2.1-annotations--annotations"></a>

## Annotations

The `annotations` package provides for Java5 Annotations
meta-data based definition of rules for `Digester`.
This improves maintainability of both Java code and XML documents, as
rules are now defined in POJOs and generating `Digester`
parsers at run-time, avoiding manual updates.

<a id="commons-digester-2.1-annotations--introduction"></a>

### Introduction

This is a brief overview of the digester-rules-in-Java5 Annotations
feature. Inspired by the basic idea behind the JPA, BeanValidation and
JAXB's specifications, this feature lets you define Digester rules
directly in target POJOs, instead of creating and initializing the Rules
objects programmatically, which can become tedious.

<a id="commons-digester-2.1-annotations--annotation-rules"></a>

### Annotation Rules

A digester rule on a POJO is expressed through one or more annotations.
An annotation is considered a digester rule definition if its retention
policy contains RUNTIME and if the annotation itself is annotated with
`org.apache.commons.digester.annotations.DigesterRule`.

The `DigesterRule` is defined by the combination of:

- the reflected `Class<? extends org.apache.commons.digester.Rule>`
  by the annotation;
- the `org.apache.commons.digester.annotations.DigesterLoaderHandler`
  class that has to be invoked during the target class traversal
  (if not specifyied, the annotation processor will supply the
  `org.apache.commons.digester.annotations.handlers.DefaultLoaderHandler`);
- the `org.apache.commons.digester.annotations.AnnotationRuleProvider`
  provider that produces the `pattern, rule` pair.

Digester annotations can target any of the following `ElementType`s:

- `FIELD` for Digester rules concerning attributes;
- `METHOD` for Digester rules concerning methods calls;
- `PARAMETER` for Digester rules concerning methods parameters setting;
- `TYPE` for Digester rules concerning types creation.

While other `ElementType`s are not forbidden, the Digester
annotations processor does not have to recognize and process annotation
rules placed on such types.

Every Digester rule annotation **must** define a *pattern*
element of type `String` that represents the element matching
path pattern.

```
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@CreationRule
@DigesterRule(
        reflectsRule = ObjectCreateRule.class,
        providedBy = ObjectCreateRuleProvider.class
)
public @interface ObjectCreate {

    String pattern();

}
```

<a id="commons-digester-2.1-annotations--applying-multiple-annotation-rule-of-the-same-type"></a>

### Applying multiple annotation rule of the same type

It is often useful to declare the same annotation rule more than once
to the same target, with different properties. To support this requirement, the Digester annotation processor treats annotations annotated by
`@org.apache.commons.digester.annotations.DigesterRuleList`
whose `value` element has a return type of an array of rule
annotations in a special way. Each element in the value array are processed
by the Digester annotation processor as regular annotation rule annotations.
This means that each Digester rule specified in the `value`
element is applied to the target. The annotation must have retention
`RUNTIME` and can be applied on a type, field, method or
method parameter. It is recommended to use the same set of targets as
the initial Digester annotation rule.

Note to designers: each Digester annotation rule should be coupled
with its corresponding multi-valued annotation.
It is recommended, though not mandated, the definition of
an inner annotation named `List`.

```
@Documented
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@CreationRule
@DigesterRule(
    reflectsRule = ObjectCreateRule.class,
    providedBy = ObjectCreateRuleProvider.class
)
public @interface ObjectCreate {

    String pattern();

    @Documented
    @Retention(RetentionPolicy.RUNTIME)
    @Target(ElementType.TYPE)
    @DigesterRuleList
    @interface List {
        ObjectCreate[] value();
    }

}
```

<a id="commons-digester-2.1-annotations--rule-provider-implementation"></a>

### Rule provider implementation

A Digester rule provider implementation performs the rule creation
of a given annotation for a given annotated element. The implementation
classes are specified by the `providedBy` element of the
`@DigesterRule` annotation that decorates the rule annotation
definition. The rule provider implementation implements the
`org.apache.commons.digester.annotations.AnnotationRuleProvider<A extends Annotation, E extends AnnotatedElement, R extends Rule>`
interface.

```
class ObjectCreateRuleProvider implements AnnotationRuleProvider<ObjectCreate, Class<?>, ObjectCreateRule> {

    private Class element) {
        this.clazz = element;
    }

    public ObjectCreateRule get() {
        return new ObjectCreateRule(this.clazz);
    }

}
```

<a id="commons-digester-2.1-annotations--notes"></a>

##### Notes

A new instance of the provider will be created each time the Digester
annotations processor will meet the relative rule that requests it.

To supply the missing `AnnotatedElement` for methods
`PARAMETER`s, the Digester annotation processor come with the
`org.apache.commons.digester.annotations.reflect.MethodArgument`
class.

<a id="commons-digester-2.1-annotations--digester-loader-handler-implementation"></a>

### Digester loader handler implementation

The Digester loader handler is an `AnnotatedElement`
interceptor invoked when meeting a particular Digester rule annotation
while analyzing the target class.

By default, the Digester annotations processor, when meeting a
Digester annotation rule, extracts the rule pattern and the relative
rule provider to store it in the
`org.apache.commons.digester.annotations.FromAnnotationsRuleSet`, an `org.apache.commons.digester.RuleSet` implementation.

If designers have the need of a more elaborate annottaion processing, they can specify the `handledBy` element of the
`@DigesterRule` annotation that decorates the rule annotation
definition. The Digester loader handler implementation implements the
`DigesterLoaderHandler<A extends Annotation, E extends AnnotatedElement>`
interface. Follows below an example:

```
class SetPropertiesLoaderHandler implements DigesterLoaderHandler<SetProperty, Field> {

    public void handle(SetProperty annotation, Field element, FromAnnotationsRuleSet ruleSet) {
        SetPropertiesRuleProvider ruleProvider = ruleSet.getProvider(annotation.pattern(), SetPropertiesRuleProvider.class);

        if (ruleProvider == null) {
            ruleProvider = new SetPropertiesRuleProvider();
            ruleSet.addRuleProvider(annotation.pattern(), ruleProvider);
        }

        ruleProvider.addAlias(annotation, element);
    }

}
```

<a id="commons-digester-2.1-annotations--built-in-rules"></a>

### Built-in Rules

All built-in annotation rules are in the package
`org.apache.commons.digester.annotations.rules`.
Here is the list of annotations and their usage.

<a id="commons-digester-2.1-annotations--type-annotations"></a>

#### `TYPE` annotations

| Annotation | Reflect rule |
| --- | --- |
| @ObjectCreate | org.apache.commons.digester.ObjectCreateRule |
| @FactoryCreate | org.apache.commons.digester.FactoryCreateRule |

<a id="commons-digester-2.1-annotations--field-annotations"></a>

#### `FIELD` annotations

| Annotation | Reflect rule |
| --- | --- |
| @BeanPropertySetter | org.apache.commons.digester.BeanPropertySetterRule |
| @SetProperty | org.apache.commons.digester.SetPropertiesRule |

<a id="commons-digester-2.1-annotations--method-annotations"></a>

#### `METHOD` annotations

| Annotation | Reflect rule |
| --- | --- |
| @CallMethod | org.apache.commons.digester.CallMethodRule |
| @SetNext | org.apache.commons.digester.SetNextRule |
| @SetRoot | org.apache.commons.digester.SetRootRule |
| @SetTop | org.apache.commons.digester.SetTopRule |

<a id="commons-digester-2.1-annotations--parameter-annotations"></a>

#### `PARAMETER` annotations

| Annotation | Reflect rule |
| --- | --- |
| @AttributeCallParam | org.apache.commons.digester.Digester#addCallParam(String, int, String) |
| @CallParam | org.apache.commons.digester.Digester#addCallParam(String, int) |
| @PathCallParam | org.apache.commons.digester.Digester#addCallParamPath(String, int) |
| @StackCallParam | org.apache.commons.digester.Digester#addCallParam(String, int, int) |

<a id="commons-digester-2.1-annotations--bootstrapping"></a>

### Bootstrapping

The core of Digester annotations rules processor is the
`org.apache.commons.digester.annotations.DigesterLoader` class.

A `org.apache.commons.digester.annotations.DigesterLoader`
instance is able to analyze `Class<?>` graphs and builds
the relative `org.apache.commons.digester.RuleSet` to create
`org.apache.commons.digester.Digester` instances.

The bootstrap sequence has been designed to be as simple as possible, all that's needed is creating a new
`org.apache.commons.digester.annotations.DigesterLoaderBuilder`
instance, plugging the desired
`org.apache.commons.digester.annotations.spi.AnnotationRuleProviderFactory` and
`org.apache.commons.digester.annotations.spi.DigesterLoaderHandlerFactory`.
using a chaining builders pattern.

An `org.apache.commons.digester.annotations.spi.AnnotationRuleProviderFactory`
implementation performs the creation of
`org.apache.commons.digester.annotations.AnnotationRuleProvider<A extends Annotation, E extends AnnotatedElement, R extends Rule>`
instances; the default implementation is limited to create the provider
by invoking the default empty constructor of the required class, but
users are free to give their implementation if they need a more complex
factory, i.e. providers requires components that could be injected from a
context, etc. etc.

<a id="commons-digester-2.1-annotations--note"></a>

##### Note

It is strongly descouraged caching `AnnotationRuleProvider`
instances!!!

Same thing for the `org.apache.commons.digester.annotations.spi.DigesterLoaderHandlerFactory`, which implementation performs the creation of
`DigesterLoaderHandler<A extends Annotation, E extends AnnotatedElement>`
instances; the default implementation is limited to create the handler
by invoking the default empty constructor of the required class, but
users are free to give their implementation if they need a more complex
factory, i.e. providers requires components that could be injected from a
context, etc. etc.

Said that, to obtain a fresh new
`org.apache.commons.digester.annotations.DigesterLoader` instance
with default factories, it is enough invoking the default empty constructor:

```
DigesterLoader digesterLoader = new DigesterLoaderBuilder()
                                    .useDefaultAnnotationRuleProviderFactory()
                                    .useDefaultDigesterLoaderHandlerFactory();
```

Otherwise, if users need specify theyr custom factories:

```
DigesterLoader digesterLoader = new DigesterLoaderBuilder()
                                    .useAnnotationRuleProviderFactory(new MyAnnotationRuleProviderFactory())
                                    .useDigesterLoaderHandlerFactory(new MyDigesterLoaderHandlerFactory());
```

<a id="commons-digester-2.1-annotations--example:-a-simple-rss-parser"></a>

### Example: a simple RSS parser

Let's assume there is the need to parse the following (simplified)
XML/RSS feed:

```
<rss version="2.0">
    <channel>

        <title>Apache</title>
        <link>http://www.apache.org</link>
        <description>The Apache Software Foundation</description>
        <language>en-US</language>
        <rating>(PICS-1.1 "http://www.rsac.org/ratingsv01.html"
            2 gen true comment "RSACi North America Server"
            for "http://www.rsac.org" on "1996.04.16T08:15-0500"
            r (n 0 s 0 v 0 l 0))</rating>

        <image>
            <title>Apache</title>
            <url>http://jakarta.apache.org/images/jakarta-logo.gif</url>
            <link>http://jakarta.apache.org</link>
            <width>505</width>
            <height>480</height>
            <description>The Jakarta project. Open source, serverside java.</description>
        </image>

        <item>
            <title>Commons Attributes 2.1 Released</title>
            <link>http://jakarta.apache.org/site/news/news-2004-2ndHalf.html#20040815.1</link>
            <description>The Apache Commons team is happy to announce the release of Commons Attributes 2.1.
            This is the first release of the new Commons-Attributes code.</description>
        </item>

        <item>
            <title>Cloudscape Becomes Apache Derby</title>
            <link>http://jakarta.apache.org/site/news/elsewhere-2004-2ndHalf.html#20040803.1</link>
            <description>IBM has submitted a proposal to the Apache DB project for a Java-based package to be called 'Derby'.</description>
        </item>

        <item>
            <title>Commons BeanUtils 1.7 Released</title>
            <link>http://jakarta.apache.org/site/news/news-2004-2ndHalf.html#20040802.1</link>
            <description/>
        </item>

        <item>
            <title>Commons JXPath 1.2 Released</title>
            <link>http://jakarta.apache.org/site/news/news-2004-2ndHalf.html#20040801.2</link>
            <description/>
        </item>
    </channel>
</rss>
```

So, let's define the Java entities and annotate them; first the `Channel` entity:

```
@ObjectCreate(pattern = "rss/channel")
class Channel {

    private final List<Item> items = new ArrayList<Item>();

    @BeanPropertySetter(pattern = "rss/channel/title")
    private String title;

    @BeanPropertySetter(pattern = "rss/channel/link")
    private String link;

    @BeanPropertySetter(pattern = "rss/channel/description")
    private String description;

    @BeanPropertySetter(pattern = "rss/channel/language")
    private String language;

    private Image image;

    // getters and setters

    @SetNext
    public void setImage(Image image) {
        this.image = image;
    }

    @SetNext
    public void addItem(Item item) {
        this.items.add(item);
    }

}
```

Then the `Image` entity:

```
@ObjectCreate(pattern = "rss/channel/image")
class Image {

    @BeanPropertySetter(pattern = "rss/channel/image/description")
    private String description;

    @BeanPropertySetter(pattern = "rss/channel/image/width")
    private int width;

    @BeanPropertySetter(pattern = "rss/channel/image/height")
    private int height;

    @BeanPropertySetter(pattern = "rss/channel/image/link")
    private String link;

    @BeanPropertySetter(pattern = "rss/channel/image/title")
    private String title;

    @BeanPropertySetter(pattern = "rss/channel/image/url")
    private String url;

    // getters and setters

}
```

and finally the `Item` entity:

```
@ObjectCreate(pattern = "rss/channel/item")
class Item {

    @BeanPropertySetter(pattern = "rss/channel/item/description")
    private String description;

    @BeanPropertySetter(pattern = "rss/channel/item/link")
    private String link;

    @BeanPropertySetter(pattern = "rss/channel/item/title")
    private String title;

    // getters and setters

}
```

It is now possible to create the `Digester` instance and parse the XML:

```
DigesterLoader digesterLoader = new DigesterLoaderBuilder()
                                    .useDefaultAnnotationRuleProviderFactory()
                                    .useDefaultDigesterLoaderHandlerFactory();
...
Digester digester = digesterLoader.createDigester(Channel.class);
try {
    Channel channel = (Channel) digester.parse(new URL("http://www.myfeedprovider.com/rss.xml").openStream());
} catch (Exception e) {
    // do something
}
    
```

<a id="commons-digester-2.1-annotations--notes-2"></a>

##### Notes

If asking to the `DigesterLoader` instance more then twice the
`Digester` for the same `Class<?>`, the
`DigesterLoader` won't analize the target class for each request, but rather will reuse cached results.

The same `DigesterLoader` instance can be reused to create
other `Digester` instances.

---

<a id="commons-digester-2.1-faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/commons-digester-2.1/faq.html -->

<!-- page_index: 15 -->

<a id="commons-digester-2.1-faq--frequently-asked-questions"></a>

## Frequently Asked Questions

1. [Why do I get warnings when using a JAXP 1.1 parser?](#commons-digester-2.1-faq--jaxp_1_1_warnings)
2. [Why Doesn't Schema Validation Work With Parser XXX Out Of The Box?](#commons-digester-2.1-faq--schema_validation_out_box)
3. [Help!
   I'm Validating Against Schema But Digester Ignores Errors!](#commons-digester-2.1-faq--help)
4. [Where Can I Find Example Code?](#commons-digester-2.1-faq--example_code)
5. [When Are You Going To Support *Rich Site Summary* Version x.y.z?](#commons-digester-2.1-faq--support_rich_site)

Why do I get warnings when using a JAXP 1.1 parser?
:   If you're using a JAXP 1.1 parser, you might see the following warning (in your log):


```

[WARN] Digester - -Error: JAXP SAXParser property not recognized: http://java.sun.com/xml/jaxp/properties/schemaLanguage
```

    This property is needed for JAXP 1.2 (XML Schema support) as required
    for the Servlet Spec. 2.4 but is not recognized by JAXP 1.1 parsers.
    This warning is harmless.

    ---

Why Doesn't Schema Validation Work With Parser XXX Out Of The Box?
:   Schema location and language settings are often need for validation using schemas.
    Unfortunately, there isn't a single standard approach to how these properties are
    configured on a parser.
    Digester tries to guess the parser being used and configure it appropriately
    but it's not infallible.
    You might need to grab an instance, configure it and pass it to Digester.

    If you want to support more than one parser in a portable manner,
    then you'll probably want to take a look at the
    `org.apache.commons.digester.parsers` package
    and add a new class to support the particular parser that's causing problems.

    ---

Help! I'm Validating Against Schema But Digester Ignores Errors!
:   Digester is based on [SAX](http://www.saxproject.org). The convention for
    SAX parsers is that all errors are reported (to any registered
    `ErrorHandler`) but processing continues. Digester (by default)
    registers its own `ErrorHandler` implementation. This logs details
    but does not stop the processing (following the usual convention for SAX
    based processors).

    This means that the errors reported by the validation of the schema will appear in the
    Digester logs but the processing will continue. To change this behaviour, call
    `digester.setErrorHandler` with a more suitable implementation.

    ---

Where Can I Find Example Code?
:   Digester ships with a sample application: a mapping for the *Rich Site
    Summary* format used by many newsfeeds. Download the source distribution
    to see how it works.

    Digester also ships with a set of examples demonstrating most of the
    features described in this document. See the "src/examples" subdirectory
    of the source distribution.

    ---

When Are You Going To Support *Rich Site Summary* Version x.y.z?
:   The *Rich Site Summary* application is intended to be a sample application.
    It works but we have no plans to add support for other versions of the format.

    We would consider donations of standard digester applications but it's unlikely that
    these would ever be shipped with the base digester distribution.
    If you want to discuss this, please post to [commons dev mailing list](http://commons.apache.org/mail-lists.html)

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/project-info.html -->

<!-- page_index: 16 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons Digester package lets you configure an XML to Java object mapping module which triggers certain actions called rules whenever a particular pattern of nested XML elements is recognized. |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Project Team](https://commons.apache.org/proper/commons-digester/team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Repository](https://commons.apache.org/proper/commons-digester/source-repository.html) | This is a link to the online source repository that can be viewed via a web browser. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Mailing Lists](https://commons.apache.org/proper/commons-digester/mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependencies](https://commons.apache.org/proper/commons-digester/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-digester/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [Continuous Integration](#integration) | This is a link to the definitions of all continuous integration processes that builds and tests code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-digester/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="project-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/project-summary.html -->

<!-- page_index: 17 -->

<a id="project-summary--project-summary"></a>

## Project Summary

<a id="project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Digester |
| Description | The Apache Commons Digester package lets you configure an XML to Java object mapping module which triggers certain actions called rules whenever a particular pattern of nested XML elements is recognized. |
| Homepage | <http://commons.apache.org/digester/> |

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
| ArtifactId | commons-digester3-parent |
| Version | 3.3-SNAPSHOT |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/modules.html -->

<!-- page_index: 18 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons Digester :: Core](https://commons.apache.org/proper/commons-digester/commons-digester3/index.html) | - |
| [Apache Commons Digester :: Examples](https://commons.apache.org/proper/commons-digester/commons-digester3-samples-parent/index.html) | - |
| [Apache Commons Digester :: Distribution Packages](https://commons.apache.org/proper/commons-digester/commons-digester3-dist/index.html) | - |

---

<a id="integration"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/integration.html -->

<!-- page_index: 19 -->

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

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/project-reports.html -->

<!-- page_index: 20 -->

<a id="project-reports--generated-reports"></a>

## Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](http://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [Changes Report](#changes-report) | Changes Report on Releases of the Project. |
| [JIRA Report](#jira-report) | Report on Issues from the JIRA Issue Tracking System. |
| [JavaDocs](https://commons.apache.org/proper/commons-digester/apidocs/index.html) | JavaDoc API documentation. |
| [Test JavaDocs](https://commons.apache.org/proper/commons-digester/testapidocs/index.html) | Test JavaDoc API documentation. |
| [Source Xref](https://commons.apache.org/proper/commons-digester/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Test Source Xref](https://commons.apache.org/proper/commons-digester/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |
| [Surefire Report](#surefire-report) | Report on the test results of the project. |
| [RAT Report](#rat-report) | Report on compliance to license related source code policies |
| [CPD Report](#cpd) | Duplicate code detection. |
| [PMD Report](#pmd) | Verification of coding rules. |

---

<a id="changes-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/changes-report.html -->

<!-- page_index: 21 -->

<a id="changes-report--apache-commons-digester-changes"></a>

## Apache Commons Digester Changes

<a id="changes-report--release-history"></a>

### Release History

| Version | Date | Description |
| --- | --- | --- |
| [3.3](#changes-report--a3.3) | 201?-??-?? | Maintenance release. |
| [3.2](#changes-report--a3.2) | 2011-12-13 | Maintenance release. |
| [3.1](#changes-report--a3.1) | 2011-10-29 | New features release. |
| [3.0](#changes-report--a3.0) | 2011-07-06 | New major release. |

<a id="changes-report--release-3.3-201"></a>

### Release 3.3 - 201?-??-??

| Type | Changes | By |
| --- | --- | --- |
| fix | Regression: DigesterTestCase#testPopNamedStackNotPushed expects EmptyStackException Fixes [DIGESTER-175](http://issues.apache.org/jira/browse/DIGESTER-175). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Inner List Annotation has wrong @Target for most of the predefined annotation rules Fixes [DIGESTER-174](http://issues.apache.org/jira/browse/DIGESTER-174). Thanks to Andreas Sahlbach. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | No way to enable schema validation from DigesterLoader Fixes [DIGESTER-173](http://issues.apache.org/jira/browse/DIGESTER-173). Thanks to Ivan Diana. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Even with custom ErrorHandler, SAX errors are still written to stderr Fixes [DIGESTER-172](http://issues.apache.org/jira/browse/DIGESTER-172). Thanks to Ivan Diana. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Digester.pop(String) throws EmptyStackException where API doc says it returns null Fixes [DIGESTER-170](http://issues.apache.org/jira/browse/DIGESTER-170). Thanks to Dale Wijnand. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Problem when including rules XML file with "classpath:" URL prefix Fixes [DIGESTER-169](http://issues.apache.org/jira/browse/DIGESTER-169). Thanks to Eugene Fedotov. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Groundless "Circular file inclusion detected" exception when including rules XML file Fixes [DIGESTER-167](http://issues.apache.org/jira/browse/DIGESTER-167). Thanks to Eugene Fedotov. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | BinderClassLoader does not override getResource Fixes [DIGESTER-165](http://issues.apache.org/jira/browse/DIGESTER-165). Thanks to Dirk Schaube. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | RulesBase performance optimization. Fixes [DIGESTER-164](http://issues.apache.org/jira/browse/DIGESTER-164). Thanks to Frank David Martinez. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | ConcurrentModificationException creating a new Digester via loaderInstance.newDigester() Fixes [DIGESTER-163](http://issues.apache.org/jira/browse/DIGESTER-163). Thanks to Torsten Krah. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | ObjectCreateRule doesn't allow create objects which type is specified in attributeName only Fixes [DIGESTER-162](http://issues.apache.org/jira/browse/DIGESTER-162). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Document thread-safety in javadoc of Rule class Fixes [DIGESTER-161](http://issues.apache.org/jira/browse/DIGESTER-161). Thanks to Eduard Papa. | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |

<a id="changes-report--release-3.2-2011-12-13"></a>

### Release 3.2 - 2011-12-13

| Type | Changes | By |
| --- | --- | --- |
| fix | provide an additional artifact with shaded dependencies Fixes [DIGESTER-160](http://issues.apache.org/jira/browse/DIGESTER-160). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | \*/object-param-rule is not managed in the XML rules Fixes [DIGESTER-159](http://issues.apache.org/jira/browse/DIGESTER-159). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Improve Set(Nested)PropertiesRuleAlias performances in the XML ruleset while binding rules. Fixes [DIGESTER-157](http://issues.apache.org/jira/browse/DIGESTER-157). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Make (Nested|Set)PropertiesBuilder#addAlias() fluent. Fixes [DIGESTER-156](http://issues.apache.org/jira/browse/DIGESTER-156). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | ClassLoader reference set to DigesterLoader not set in produced Digester instances Fixes [DIGESTER-155](http://issues.apache.org/jira/browse/DIGESTER-155). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | The DigesterBinder is not able to load primitive classes by name Fixes [DIGESTER-154](http://issues.apache.org/jira/browse/DIGESTER-154). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | Add Constructor support to ObjectCreateRule Fixes [DIGESTER-153](http://issues.apache.org/jira/browse/DIGESTER-153). | [mbenson](https://commons.apache.org/proper/commons-digester/team-list.html#mbenson) |
| add | The org.apache.commons.digester3.binder.DigesterLoader doesn't allow binding a default org.xml.sax.Locator Fixes [DIGESTER-152](http://issues.apache.org/jira/browse/DIGESTER-152). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | The org.apache.commons.digester3.binder.DigesterLoader doesn't allow binding a default org.xml.sax.ErrorHandler. Fixes [DIGESTER-151](http://issues.apache.org/jira/browse/DIGESTER-151). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |

<a id="changes-report--release-3.1-2011-10-29"></a>

### Release 3.1 - 2011-10-29

| Type | Changes | By |
| --- | --- | --- |
| add | Use Java5 Concurrent APIs to asynchronous parse() Fixes [DIGESTER-150](http://issues.apache.org/jira/browse/DIGESTER-150). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |

<a id="changes-report--release-3.0-2011-07-06"></a>

### Release 3.0 - 2011-07-06

| Type | Changes | By |
| --- | --- | --- |
| fix | Default ClassLoader policy unusable in EAR archive Fixes [DIGESTER-28](http://issues.apache.org/jira/browse/DIGESTER-28). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | Allow SetNextRule to fire on begin Fixes [DIGESTER-72](http://issues.apache.org/jira/browse/DIGESTER-72). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | Include filename or uri if Digester.parse(File file or String uri throws a SAXException Fixes [DIGESTER-85](http://issues.apache.org/jira/browse/DIGESTER-85). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | xmlrules does not support setNamespaceURI Fixes [DIGESTER-90](http://issues.apache.org/jira/browse/DIGESTER-90). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | xmlrules does not support NodeCreateRule Fixes [DIGESTER-103](http://issues.apache.org/jira/browse/DIGESTER-103). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | Need to process [attribute id="name"]somename[/attribute] Fixes [DIGESTER-105](http://issues.apache.org/jira/browse/DIGESTER-105). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | ObjectCreateRule shouldn't keep className as a field. Fixes [DIGESTER-118](http://issues.apache.org/jira/browse/DIGESTER-118). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | xmlrules dtd does not define xmlattrs for node-create-rule Fixes [DIGESTER-123](http://issues.apache.org/jira/browse/DIGESTER-123). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | Allow DigesterLoader to accept an instance of a preconfigured Digester Fixes [DIGESTER-127](http://issues.apache.org/jira/browse/DIGESTER-127). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | Allow recursive match in ExtendedBaseRules. Fixes [DIGESTER-131](http://issues.apache.org/jira/browse/DIGESTER-131). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| add | Add a CompoundSubstitutor to support more than one Substitutors at a time. Fixes [DIGESTER-132](http://issues.apache.org/jira/browse/DIGESTER-132). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| fix | Bug in SetPropertyRule. Fixes [DIGESTER-134](http://issues.apache.org/jira/browse/DIGESTER-134). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |
| update | Public/protected static fields which intended as constants, but which are not marked final. Fixes [DIGESTER-137](http://issues.apache.org/jira/browse/DIGESTER-137). | [simonetripodi](https://commons.apache.org/proper/commons-digester/team-list.html#simonetripodi) |

---

<a id="jira-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/jira-report.html -->

<!-- page_index: 22 -->

<a id="jira-report--jira-report"></a>

## JIRA Report

| Fix Version | Key | Component | Summary | Type | Resolution | Status |
| --- | --- | --- | --- | --- | --- | --- |

---

<a id="surefire-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/surefire-report.html -->

<!-- page_index: 23 -->

<a id="surefire-report--surefire-report"></a>

## Surefire Report

<a id="surefire-report--summary"></a>

## Summary

| Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 0 | 0% | 0 |

Note: failures are anticipated and checked for with assertions while errors are unanticipated.

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/rat-report.html -->

<!-- page_index: 24 -->

<a id="rat-report--rat-release-audit-tool-results"></a>

## RAT (Release Audit Tool) results

The following document contains the results of [RAT (Release Audit Tool)](http://incubator.apache.org/rat/apache-rat-plugin).

```

*****************************************************
Summary
-------
Generated at: 2013-01-11T06:55:11-05:00
Notes: 3
Binaries: 2
Archives: 0
Standards: 20

Apache Licensed: 20
Generated Documents: 0

JavaDocs are generated and so license header is optional
Generated files do not required license headers

0 Unknown Licenses

*******************************

Unapproved licenses:


*******************************

Archives:

*****************************************************
  Files with Apache License headers will be marked AL
  Binary files (which do not require AL headers) will be marked B
  Compressed archives will be marked A
  Notices, licenses etc will be marked N
  N     /scratch/jenkins/workspace/commons-site-deploy/commons-lib/RELEASE-NOTES.txt
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/pom.xml
  N     /scratch/jenkins/workspace/commons-site-deploy/commons-lib/LICENSE.txt
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/PROPOSAL.html
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/doap_digester.rdf
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/resources/dtds/digester-rules-3.0.dtd
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/resources/dtds/digester-rules.dtd
  B     /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/resources/images/logo.png
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/site.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/fml/guide/faq.fml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/issue-tracking.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/index.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/download_digester.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/mail-lists.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/constructor.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/plugins.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/core.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/xmlrules.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/binder.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/substitution.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/annotations.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/site/xdoc/guide/async.xml
  AL    /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/changes/changes.xml
  B     /scratch/jenkins/workspace/commons-site-deploy/commons-lib/src/media/logo.xcf
  N     /scratch/jenkins/workspace/commons-site-deploy/commons-lib/NOTICE.txt
 
 *****************************************************
 Printing headers for files without AL header...
 
 
```

---

<a id="cpd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/cpd.html -->

<!-- page_index: 25 -->

<a id="cpd--cpd-results"></a>

## CPD Results

The following document contains the results of PMD's [CPD](http://pmd.sourceforge.net/cpd.html) 4.1.

<a id="cpd--duplications"></a>

## Duplications

CPD found no problems in your source code.

---

<a id="pmd"></a>

<!-- source_url: https://commons.apache.org/proper/commons-digester/pmd.html -->

<!-- page_index: 26 -->

<a id="pmd--pmd-results"></a>

## PMD Results

The following document contains the results of [PMD](http://pmd.sourceforge.net/) 4.1.

<a id="pmd--files"></a>

## Files

PMD found no problems in your source code.

---
