# Commons Chain - Project Information

## Navigation

- Chain
  - [Overview](#index)
  - [Release Notes](#changes-report)
  - [Cookbook](#cookbook)
- Development
  - [Issue Tracking](#issue-tracking)
  - [Building](#building)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Continuous Integration](#integration)
    - [Issue Tracking](#issue-tracking)
    - [Project Summary](#project-summary)
  - [Project Reports](#project-reports)
    - [Changes Report](#changes-report)
    - [Checkstyle](#checkstyle)
    - [Clirr](#clirr-report)
    - [FindBugs Report](#findbugs)
    - [JDepend](#jdepend-report)
    - [RAT Report](#rat-report)
    - [Surefire Report](#surefire-report)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-chain"></a>

## Commons Chain

A popular technique for organizing the execution of complex
processing flows is the "Chain of Responsibility" pattern, as
described (among many other places) in the classic "Gang of Four"
design patterns book. Although the fundamental API contracts
required to implement this design patten are extremely simple, it
is useful to have a base API that facilitates using the pattern, and (more importantly) encouraging composition of command
implementations from multiple diverse sources.

Towards that end, the Chain API models a computation as a
series of "commands" that can be combined into a "chain". The API
for a command consists of a single method
(`execute()`), which is passed a "context" parameter
containing the dynamic state of the computation, and whose return
value is a boolean that determines whether or not processing for
the current chain has been completed (true), or whether
processing should be delegated to the next command in the chain
(false).

The "context" abstraction is designed to isolate command
implementations from the environment in which they are run (such
as a command that can be used in either a Servlet or Portlet, without being tied directly to the API contracts of either of
these environments). For commands that need to allocate resources
prior to delegation, and then release them upon return (even if a
delegated-to command throws an exception), the "filter" extension
to "command" provides a `postprocess()` method for
this cleanup. Finally, commands can be stored and looked up in a
"catalog" to allow deferral of the decision on which command (or
chain) is actually executed.

To maximize the usefulness of the Chain of Responsibility
pattern APIs, the fundamental interface contracts are defined in
a manner with zero dependencies other than an appropriate JDK.
Convenience base class implementations of these APIs are
provided, as well as more specialized (but optional)
implementations for the web environment (i.e. servlets and
portlets).

Given that command implementations are designed to conform
with these recommendations, it should be feasible to utilize the
Chain of Responsibility APIs in the "front controller" of a web
application framework (such as Struts), but also be able to use
it in the business logic and persistence tiers to model complex
computational requirements via composition. In addition, separation of a computation into discrete commands that operate
on a general purpose context allows easier creation of commands
that are unit testable, because the impact of executing a command
can be directly measured by observing the corresponding state
changes in the context that is supplied.

<a id="index--documentation"></a>

## Documentation

- The [Javadoc](https://commons.apache.org/dormant/commons-chain/apidocs/index.html) of the latest Release.
- The [Cookbook](#cookbook) containing "recipes" for using the chain.
- The [SVN repository](https://commons.apache.org/dormant/commons-chain/source-repository.html) can be browsed.

<a id="index--downloading-chain"></a>

## Downloading Chain

See the [Downloads](https://commons.apache.org/dormant/commons-chain/downloads.html) page for current/previous
releases.

<a id="index--support"></a>

## Support

The [commons mailing lists](https://commons.apache.org/dormant/commons-chain/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [chain].

Issues may be reported via [ASF JIRA](#issue-tracking).

---

<a id="changes-report"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/changes-report.html -->

<!-- page_index: 2 -->

<a id="changes-report--changes-report"></a>

## Changes Report

<a id="changes-report--release-history"></a>

### Release History

| Version | Date | Description |
| --- | --- | --- |
| [1.2](#changes-report--a1.2) | 2008-06-02 | OSGi enabled / minor bug fixes |
| [1.1](#changes-report--a1.1) | 2006-06-14 |  |
| [1.0](#changes-report--a1.0) | 2004-12-09 | Initial Release |

<a id="changes-report--release-1.2-2008-06-02"></a>

### Release 1.2 - 2008-06-02

| Type | Changes | By |
| --- | --- | --- |
| add | Chain 1.2 is the first OSGi-enabled release. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| add | Add Example webapp for Servlet Mapper Commands Fixes [CHAIN-36](http://issues.apache.org/jira/browse/CHAIN-36). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| update | Upgrade Commons Logging dependency to 1.1.1 | [rahul](https://commons.apache.org/dormant/commons-chain/team-list.html#rahul) |
| update | Improve instantiation performance of ContextBase subclasses. Fixes [CHAIN-32](http://issues.apache.org/jira/browse/CHAIN-32). Thanks to Joshua Graham. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| update | Update servlet implementation classes to be aware of CatalogFactory Fixes [CHAIN-4](http://issues.apache.org/jira/browse/CHAIN-4). Thanks to Joe Germuska. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | CatalogFactory instance variable prevents ChainProcessor from being serializable. Fixes [CHAIN-44](http://issues.apache.org/jira/browse/CHAIN-44). Thanks to FindBugs. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | ChainListener URL translation does not work as expected. Fixes [CHAIN-43](http://issues.apache.org/jira/browse/CHAIN-43). Thanks to Ales Dolecek. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Various scope mappers use incorrect equalization. Fixes [CHAIN-42](http://issues.apache.org/jira/browse/CHAIN-42). Thanks to Isaac Shabtay. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Ant build fails due to usage of old Digester. Fixes [CHAIN-41](http://issues.apache.org/jira/browse/CHAIN-41). Thanks to Isaac Shabtay. | [skitching](https://commons.apache.org/dormant/commons-chain/team-list.html#skitching) |
| fix | PathInfoMapper command can not obtain the current catalog instance. Fixes [CHAIN-35](http://issues.apache.org/jira/browse/CHAIN-35). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Unbalanced tags in JavaDoc for ContextBase class. Fixes [CHAIN-34](http://issues.apache.org/jira/browse/CHAIN-34). Thanks to Mark Vedder. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Upgrade to Commons Digester 1.8 to fix bug loading webapp resources. Fixes [CHAIN-33](http://issues.apache.org/jira/browse/CHAIN-33). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Corrections to the project.xml - mark servlet, portlet and myfaces dependencies as "optional" to prevent dependency problems for maven2 users. | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |

<a id="changes-report--release-1.1-2006-06-14"></a>

### Release 1.1 - 2006-06-14

| Type | Changes | By |
| --- | --- | --- |
| fix | ServletSessionScopeMap always forces a Session to be Created. Fixes [CHAIN-30](http://issues.apache.org/jira/browse/CHAIN-30). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Portlet Map implementations' entry Set should contain Map.Entry elements. Fixes [CHAIN-31](http://issues.apache.org/jira/browse/CHAIN-31). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| add | Provide a Map of Cookies in the WebContext. Fixes [CHAIN-28](http://issues.apache.org/jira/browse/CHAIN-28). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Remove Static Log instances - see http://wiki.apache.org/commons/Logging/StaticLog Fixes [CHAIN-29](http://issues.apache.org/jira/browse/CHAIN-29). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | Modify DispatchCommand so that it will compile using JDK 1.3 (remove JDK 1.4 method). Fixes [CHAIN-11](http://issues.apache.org/jira/browse/CHAIN-11). | [niallp](https://commons.apache.org/dormant/commons-chain/team-list.html#niallp) |
| fix | DispatchCommand - fix bug in handling InvocationTargetException. | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| fix | Maven build updates. Fixes [CHAIN-9](http://issues.apache.org/jira/browse/CHAIN-9). Thanks to Wendy Smoak. | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| update | CatalogBase - add constructor which takes an already built map of commands, for easier use in dependency-injection environments. | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| fix | DispatchCommand should unwrap InvocationTargetException. Fixes [CHAIN-25](http://issues.apache.org/jira/browse/CHAIN-25). | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| update | Expose catalogFactory so that subclasses can get at it. | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| update | Decouple CatalogFactory lookup from LookupAction. Fixes [CHAIN-3](http://issues.apache.org/jira/browse/CHAIN-3). | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| fix | Make ContextBase live up to the Serializable contract that it inherits by virtue of extending HashMap. Fixes [CHAIN-12](http://issues.apache.org/jira/browse/CHAIN-12). | [craigmcc](https://commons.apache.org/dormant/commons-chain/team-list.html#craigmcc) |
| update | ChainResources - factor out the comma-delimited parsing into a separate method, fix the whitespace-skipping bugs in it. | [martinc](https://commons.apache.org/dormant/commons-chain/team-list.html#martinc) |
| update | Add support for using LookupCommand in a way which does not pass through the result from the looked up command. | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| add | Add new DispatchLookupCommand. Fixes [CHAIN-14](http://issues.apache.org/jira/browse/CHAIN-14). Thanks to Sean Schofield. | [jmitchell](https://commons.apache.org/dormant/commons-chain/team-list.html#jmitchell) |
| add | Add new test for LookupCommand. Fixes [CHAIN-26](http://issues.apache.org/jira/browse/CHAIN-26). Thanks to Sean Schofield. | [jmitchell](https://commons.apache.org/dormant/commons-chain/team-list.html#jmitchell) |
| add | Add new DispatchCommand. Fixes [CHAIN-20](http://issues.apache.org/jira/browse/CHAIN-20). | [germuska](https://commons.apache.org/dormant/commons-chain/team-list.html#germuska) |
| fix | CopyCommand does not work unless setValue is called. Fixes [CHAIN-6](http://issues.apache.org/jira/browse/CHAIN-6). | [jmitchell](https://commons.apache.org/dormant/commons-chain/team-list.html#jmitchell) |
| add | Provide a mechanism for encoding catalog and command in a single string Fixes [CHAIN-19](http://issues.apache.org/jira/browse/CHAIN-19). Thanks to Joe Germuska. | [craigmcc](https://commons.apache.org/dormant/commons-chain/team-list.html#craigmcc) |
| fix | Code fragment from 'cookbook' is incorrect. Fixes [CHAIN-1](http://issues.apache.org/jira/browse/CHAIN-1). Thanks to Sergio Moretto. | [martinc](https://commons.apache.org/dormant/commons-chain/team-list.html#martinc) |

<a id="changes-report--release-1.0-2004-12-09"></a>

### Release 1.0 - 2004-12-09

| Type | Changes | By |
| --- | --- | --- |
| fix | Make CatalogBase.getCommand() thread safe. Fixes [CHAIN-5](http://issues.apache.org/jira/browse/CHAIN-5). Thanks to Manfred Wolff. | [mardon](https://commons.apache.org/dormant/commons-chain/team-list.html#mardon) |
| update | LookupCommand should use new CatalogFactory. Fixes [CHAIN-2](http://issues.apache.org/jira/browse/CHAIN-2). Thanks to Sean Schofield. | [craigmcc](https://commons.apache.org/dormant/commons-chain/team-list.html#craigmcc) |
| fix | Sample catalog.xml missing  tag. Fixes [CHAIN-10](http://issues.apache.org/jira/browse/CHAIN-10). Thanks to Sean Schofield. | [craigmcc](https://commons.apache.org/dormant/commons-chain/team-list.html#craigmcc) |
| add | Add missing new class ConfigCatalogRule. Fixes [CHAIN-7](http://issues.apache.org/jira/browse/CHAIN-7). Thanks to Sean Schofield. | [craigmcc](https://commons.apache.org/dormant/commons-chain/team-list.html#craigmcc) |
| update | Make the impl. class of chainbase configurable. Fixes [CHAIN-21](http://issues.apache.org/jira/browse/CHAIN-21). | [craigmcc](https://commons.apache.org/dormant/commons-chain/team-list.html#craigmcc) |
| fix | Support for new CatalogFactory. Fixes [CHAIN-23](http://issues.apache.org/jira/browse/CHAIN-23). Thanks to Sean Schofield. | [craigmcc](https://commons.apache.org/dormant/commons-chain/team-list.html#craigmcc) |
| fix | tabs to spaces, Log name fix. Fixes [CHAIN-8](http://issues.apache.org/jira/browse/CHAIN-8). Thanks to Otis Gospodnetic. | [martinc](https://commons.apache.org/dormant/commons-chain/team-list.html#martinc) |
| fix | build.properties.sample should add commons-logging. Fixes [CHAIN-15](http://issues.apache.org/jira/browse/CHAIN-15). Thanks to Joe Germuska. | [husted](https://commons.apache.org/dormant/commons-chain/team-list.html#husted) |
| update | Added JavaDoc and a toString() method to CatalogBase. Fixes [CHAIN-22](http://issues.apache.org/jira/browse/CHAIN-22). Thanks to Matthew Sgarlata. | [husted](https://commons.apache.org/dormant/commons-chain/team-list.html#husted) |

---

<a id="cookbook"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/cookbook.html -->

<!-- page_index: 3 -->

<a id="cookbook--introduction"></a>

## Introduction

The essence of computing might be that for any expected input (A), we return the expected output (B). The challenge is getting from (A) to
(B). For a simple program, (A) to (B) might be a single transformation.
Say, shifting a character code 32 digits so that "a" becomes "A". In a
complex application, A to B can be a long and winding road.

We might need to confirm that the user is authorized to create (B)
from (A). We might need to find that (A) is valid input for (B). We might
need to convert (A) from another character set. We may need to insert a
preamble before writing (B). We may need to merge another resource with
(A) before creating (B). Meanwhile, if anything goes wrong during
processing, the error must be handled, and even logged. Some tasks might
be able to continue after a non-fatal error, or, if the error is fatal, all processing might need to halt.

There are many different ways programmers organize processing logic
within an application. Often, the difference between an elegant
architecture and a muddled ball-of mud is how control flows from one
process to another. To realize and retain elegance, we must organize
complex, multi-step processes so that they are easy to discover and
change.

<a id="cookbook--separate-business-logic-from-presentation-logic"></a>

## Separate "business" logic from "presentation" logic

*Problem:* You want to cleanly separate the
execution and presentation layers without complicating the design of your
application.

*Solution:* Use the
Chain of Responsibility and
Command patterns so that the presentation layer can
execute a command, or chain of commands, without needing to know how the
command is implemented.

*Discussion*: To be useful, most applications
need to run a process and then tell the client what happened. In practice, we find mixing "running" and "telling" together creates code that can be
hard to test and maintain. If we can have one component run (or execute)
the process, and another component report (or present) the result, then we
can test, create, and maintain each component separately. But, how can we
cleanly separate the execution and presentation layers without
complicating the design of an application?

Most application frameworks, especially web application frameworks, rely on the Command pattern. An incoming HTTP request is mapped to some
type of "command" object. The command object takes whatever action is
required, using information passed in the HTTP request.

In practice, there are usually commands within commands. A Command
object in a web application often looks like a sandwich. First, it does
some things for the benefit of the presentation layer, then it executes
the business logic, and then it does some more presentation layer things.
The problem many developers face is how to cleanly separate the
business logic in the middle of a web command from
other necessary tasks that are part of the request/response
transaction.

The *Chain of Responsibility* package combines the
Command pattern with the classic Chain of Responsibility
pattern to make it easy to call a business command as part of
a larger application command. (For more about the patterns, see
*Design Patterns: Elements of Reusable Object Orientated
Software* [ISBN 0-201-63361-2]).

To implement the patterns, the `Chain` package
defines five key interfaces:

- Context
- Command
- Chain
- Filter
- Catalog

*Context.* A `Context`
represents the state of an application. In the Chain package, `Context` is a marker interface for a
`java.util.Map`. The Context is an envelope
containing the attributes needed to complete a transaction. In other
words, a Context is a stateful object with member values.

*Command.* A `Command`
represents a unit of work. A Command has a single
entry method: `public boolean execute(Context
context)`. A Command acts upon the state passed to it through
a context object, but retains no state of its own. Commands may be
assembled into a Chain, so that a complex transaction can be created from
discrete units of work. If a Command returns `true`, then
other Commands in a Chain should *not* be executed. If
a Command returns `false`, then other Commands in the Chain
(if any) may execute.

*Chain.*`Chain` implements
the `Command` interface, so a
`Chain` can be used interchangeably with a
`Command`. An application doesn't need to know if
it's calling a Chain or a Command, so you can refactor from one to the
other. A Chain can nest other Chains as desired. This property is known as
the *Liskov substitution principle.*

*Filter.* Ideally, every command would be an
island. In real life, we sometimes need to allocate resources and be
assured the resources will be released no matter what happens. A
`Filter` is a specialized
`Command` that adds a
`postProcess` method. A
`Chain` is expected to call the
`postProcess` method of any filters in the chain
before returning. A Command that implements Filter can safely release any
resources it allocated through the `postProcess`
method, even if those resources are shared with other Commands.

*Catalog.* Many applications use "facades" and
"factories" and other techniques to avoid binding layers too closely
together. Layers need to interact, but often we don't want them to
interact at the classname level. A `Catalog` is a
collection of logically named Commands (or Chains) that a client can
execute, without knowing the Command's classname.

The rest of the chapter features recipes that will help you put the
Chain of Responsibility package to work in your own applications.

<a id="cookbook--test-a-command"></a>

## Test a Command

*Problem:* You want to start using
`Command` objects in your application.

*Solution:* Use Test Driven
Development to create a test for a Command, and let the test
tell you how to write the Command. When the test passes, you will have a
working Command to integrate into your application.

*Discussion:* Let's say we're working on an
application that maintains a "`Profile`" object for
each client. We need to change the state of the Profile during the
client's "session" with the application, which may span several requests.
Different application environments may preserve a Profile in different
ways. A web application may store a Profile as an attribute of the
HttpSession or as a client-side "cookie". An EJB application may maintain
a Profile as an attribute of the client's environment. Regardless, you
would like a single Command that can check to see if a client has a
Profile object, and, if not, create one. The Command does not know how the
application stores a Profile, or even if it is stored.

One reason we use Commands is because they are easy to test. In this
recipe, let's write a test for our Command. In another recipe, we will
create the corresponding Command. This approach is known as Test Driven
Development.

To test our Command, we can simply

1. Create a Context with a known state
2. Create a Command instance to test
3. Execute the Command, passing our Context
4. Confirm that our Context now contains the expected state

For the `Context`, we can use the
`ContextBase` class provided as part of the Chain
package. The `ProfileCheck` Command and Profile
object are shown in the next recipe. The remaining code for our
`TestProfileCheck` TestCase is shown as Example
1.

Testing whether a Profile object is created

```
package org.apache.commons.mailreader;

import junit.framework.TestCase;
import org.apache.commons.chain.Command;
import org.apache.commons.chain.Context;
import org.apache.commons.chain.mailreader.commands.ProfileCheck;
import org.apache.commons.chain.mailreader.commands.Profile;
import org.apache.commons.chain.impl.ContextBase;

public class ProfileCheckTest extends TestCase {

   public void testProfileCheckNeed() {

        Context context = new ContextBase();
        Command command = new ProfileCheck();
        try {
            command.execute(context);
        } catch (Exception e) {
            fail(e.getMessage());
        }

        Profile profile = (Profile) context.get(Profile.PROFILE_KEY);
        assertNotNull("Missing Profile", profile);

    }
```

Since we're using a test-first approach, we can't run or even
compile this class (yet). But we can use the test class to tell us which
other classes we need to write. The next recipe shows how to create a
Command.

<a id="cookbook--create-a-command"></a>

## Create a Command

*Problem:* You need to create a
`Command` for your application, so that a test of the
Command will succeed.

*Solution:* Use the test to tell you what code
will realize the Command's *API
contract*.

*Discussion:* A key reason for using Commands, and chains of Commands, is testability. Since Commands are designed to act
on whatever `Context` they receive, we can create a
Context with a known state to test our Command. In the preceding recipe, we created a test for a `ProfileCheck` command. Let's
implement that Command so that it passes our test.

To pass the ProfileCheck test, we need to

1. Retrieve the Profile from the Context, using Profile.PROFILE\_KEY
   as the attribute name.
2. If Profile is NULL, create a Profile and store it in the
   Context.
3. Return `false` or `true` to the
   caller.

Whether to return `false` or `true` at
step 3 is optional. You could choose to return `true`, since this Command did check the profile. Or, you could decide to return
`false`, so that the Command can be used as part of a
Chain. The return value controls whether a chain terminates or continues.
True forces a chain to end. False allows a chain to continue. For now, we'll just return `false`, so that our Command could be
used as part of a larger chain of Commands.

The code implementing our ProfileCheck Command is shown as Example
2.

A Command to create a Profile, if one doesn't exist.

```
package org.apache.commons.chain.mailreader.commands;

import org.apache.commons.chain.Command;
import org.apache.commons.chain.Context;

public class ProfileCheck implements Command {

    public Profile newProfile(Context context) { return new Profile(); }

    public boolean execute(Context context) throws Exception {
        Object profile = context.get(Profile.PROFILE_KEY);
        if (null == profile) {
            profile = newProfile(context);
            context.put(Profile.PROFILE_KEY, profile);
        }
        return false;
    }
}
```

To compile our Command and run our test, we also need a
`Profile` class. Example 3 shows the simplest
implementation of Profile that will pass our test.

The simplest Profile class that can possibly work.

```
package org.apache.commons.chain.mailreader.commands; 
public class Profile { 
    public static String PROFILE_KEY = "profile"; 
}
```

Note that we used a separate method to create the Profile object. If
we buried a call to "new Profile()" in the Execute method, we could not
reuse our CheckProfile Command to create specialized Profiles. Using
helper methods to create objects is known as the
Factory pattern.

We should now be able to compile all three classes and run our
test.

Green bar for org.apache.commons.mailreader.ProfileCheckTest
[TODO: Screen capture]

<a id="cookbook--create-a-context"></a>

## Create a Context

*Problem:* You want a
`Context` that is
*type-safe*,
*encapsulated*, or interoperable
with components that expect JavaBean
properties.

*Solution:* Extend your Context class from
`ContextBase`, and add whatever JavaBean properties
you need.

*Discussion*: Many components already use a
"context". Each of the various Java Servlet "scopes" have a context
object. The Apache Velocity product relies
on a context object. Most operating systems have a list of simple
"environment" settings that is a "context". These examples all use a "map"
or "dictionary" style context. These contexts are a simple list of
entries, where each entry is a key and a value.

Other components also use what amounts to a context but predefine
the entries as object properties. The Apache Struts framework is one
example. Developers can define a JavaBean (or
"`ActionForm`") to act as the context for a request.
Some components mix both approaches. The Servlet request and session
objects expose a Map-style context along with several predefined
properties. Struts supports a variant of the ActionForm that utilizes a
Map.

Architects will often choose a Map-style context because they are
easy to implement and *very* easy to extend. Usually, developers can add their own entries to a Map-style context at will. Of
course, every engineering decision is a
trade-off. Maps trade type-safety and encapsulation for flexibility and
extensibility. Other times, architects will decide to trade flexibility
for type-safety. Or, we may decide to trade extensibility for
encapsulation. Often, these decisions are driven by the need to
interoperate with other components that may expect either a Map or a
JavaBean.

The Apache Commons Chain of Command architects have chosen a
Map-style context as the default. The Chain Context is nothing but a
"marker interface" for the standard Java `Map`
interface.

The Context interface is a "marker" interface extending
Map.

```
public interface Context extends Map {
}
```

However, to provide developers with type-safety, encapsulation, and interoperability, Chain provides a sophisticated
`ContextBase` class that also supports JavaBean
properties.

If a developer declares a JavaBean property on a subclass of
ContextBase, this property is automatically used by the Map methods. The
Map `get` and `put` methods
of ContextBase introspect the subclass. If they find a JavaBean property
named after the key argument, the getter or setter method is called
instead.

This bit of wizardry enforces type-safety for any declared
properties, but developers can still use the context as if it were an
ordinary Map. If all needed attributes are defined as properties, then a
ContextBase can interoperate with components that expect a Map and also
with components that expect a JavaBean -- all at the same time. Everything
is transparent, and there are no special requirements for the
caller.

Let's create a test for a ContextBase subclass to prove the JavaBean
properties and Map methods are interoperable and type-safe.

To test the context for interoperability, we'll need to do four
things:

1. Assign a value to a typed property using a JavaBean
   setter
2. Retrieve the same value using the Map get method
3. Assign another value using the Map set method
4. Retrieve the update value using a JavaBean setter

To test the context for type-safety, we will also need to

1. Assign a `String` to a typed property
   using the Map get method
2. Confirm that the assignation throws a "type mismatch"
   exception

To write these tests, let's create a context with a
*Locale* property for an application named
"MailReader". The code for our `LocaleValueTest` is
shown below.LocaleValueTest proves that our context is interoperable and
type-safe.

```
package org.apache.commons.mailreader;
import junit.framework.TestCase;
import junit.framework.Assert;
import org.apache.commons.chain.mailreader.MailReader;
import java.util.Locale;

public class LocaleValueTest extends TestCase {

    MailReader context;

    public void setUp() {
        context = new MailReader();
    }

    public void testLocaleSetPropertyGetMap() {
        Locale expected = Locale.CANADA_FRENCH;
        context.setLocale(expected);
        Locale locale = (Locale) context.get(MailReader.LOCALE_KEY);
        Assert.assertNotNull(locale);
        Assert.assertEquals(expected, locale);
    }

    public void testLocalePutMapGetProperty() {
        Locale expected = Locale.ITALIAN;
        context.put(MailReader.LOCALE_KEY, expected);
        Locale locale = context.getLocale();
        Assert.assertNotNull(locale);
        Assert.assertEquals(expected, locale);
    }

    public void testLocaleSetTypedWithStringException() {
        String localeString = Locale.US.toString();
        try {
            context.put(MailReader.LOCALE_KEY, localeString);
            fail("Expected 'argument type mismatch' error");
        } catch (UnsupportedOperationException expected) {
            ;
        }
    }
}
```

A `MailReader` Context object that passes
the LocaleValueTest is shown below.The simplest MailReader object that will pass
LocalValueTest.

```
package org.apache.commons.chain.mailreader;
import org.apache.commons.chain.impl.ContextBase;
import java.util.Locale;

public class MailReader extends ContextBase {Prop
    public static String LOCALE_KEY = "locale";
    private Locale locale;
    public Locale getLocale() {
        return locale;
    }
    public void setLocale(Locale locale) {
        this.locale = locale;
    }
}
```

The MailReader object above shows how much utility is
built into ContextBase class. All we had to do was define the property.
The base class took care of the rest. Of course, there is no free lunch.
ContextBase has to go through the bother of introspection to tell if an
attribute has a property or not. The ContextBase code is written to be
efficient, but if your application can just use a Map-style context, you
could use the leaner version of a MailReader context shown below.An even simpler MailReader Context (but that would fail
LocalValueTest).

```
package org.apache.commons.chain.mailreader;
import org.apache.commons.chain.Context;
import java.util.Hashmap;

public class MailReader extends Hashmap implements Context {
    public static String LOCALE_KEY = "locale";
}
```

By extending the stock ContextBase subclass, or rolling your
own class with a HashMap, you can use whatever type of context is best for
your own artichtecture.

<a id="cookbook--create-a-catalog"></a>

## Create a Catalog

*Problem:* You want to layer your application
without creating dependencies on `Command` objects
that exist in different layers.

*Solution:* Assign each command a logical name so
that it can be called from a "catalog". A catalog moves dependency on to
the logical name and away from the Java classname or classnames. The
caller has a dependency on the catalog but not on the actual Command
classes.

*Discussion:* Context and Command objects are
usually used to join layers of an application together. How can one layer
call Commands in another layer without creating new dependencies between
the two layers?

Interlayer dependencies are a common dilemma in enterprise
applications. We want to layer our application so that it becomes robust
and cohesive, but we also need a way for the different layers to interact
with each other. The Commons Chain package offers a
`Catalog` object to help solve problems with
dependencies between layers, as well as between components on the same
layer.

A Catalog can be configured through metadata
(an XML document) and instantiated at application startup. Clients can
retrieve whatever `Commands` they need from the
Catalog at runtime. If Commands need to be refactored, new classnames can
be referenced in the metadata, with no changes to the application
code.

Let's take a look at some code that uses a Catalog. Shown below is
a method that executes a Command from a Catalog stored in a web
application's servlet context. A Catalog stores Commands that an application can lookup and
execute.

```
   boolean executeCatalogCommand(Context context,
            String name, HttpServletRequest request) 
        throws Exception {
    
        ServletContext servletContext =
                request.getSession().getServletContext();  
        Catalog catalog =
                (Catalog) servletContext.getAttribute("catalog");
        Command command = catalog.getCommand(name);
        boolean stop = command.execute(context);
        return stop;
        
    } 
```

Notice that we only pass the name of a Command into the method. Also
note that we retrieve the Command and pass it the Context without knowing
the precise type of either object. All references are to the standard
interfaces.

Shown below is an XML document that can be used to create a
Catalog, like the one called in the example above.A Catalog can be configured using metadata (an XML
document).

```
<?xml version="1.0" ?>
<catalog>
  <command 
    name="LocaleChange" 
    className="org.apache.commons.chain.mailreader.commands.LocaleChange"/>
  <command 
    name="LogonUser" 
    className="org.apache.commons.chain.mailreader.commands.LogonUser"/>
</catalog>
```

The application needs to know the name given to a Command we
want to execute, but it does not need to know the classname of the
Command. The Command could also be a `Chain` of
Commands. We can refactor Commands within the Catalog and make
zero-changes to the application. For example, we might decide to check for
a user profile before changing a user's locale setting. If we wanted to
make running a `CheckProfile` Command part of
"LocaleChange", we could change the Catalog to make "LocaleChange" a
Chain. The following example shows Catalog metadata where "LocaleChange" is a Chain.
A Catalog can be refactored with zero-changes to the
application code.

```
<catalog>
  <chain name="LocaleChange">
    <command 
      className="org.apache.commons.chain.mailreader.commands.ProfileCheck"/>
    <command 
      className="org.apache.commons.chain.mailreader.commands.LocaleChange"/>
  </chain>
  <command 
    name="LogonUser" 
    className="org.apache.commons.chain.mailreader.commands.LogonUser"/>
</catalog>
```

In the "Create a Command" recipe, we use a factory method to create
a "Profile" object. If we subclass that Command to create a specialized
Profile, we can cite the new classname in the Catalog, with zero changes
to the rest of the application.

Being able to make quick and easy changes to an application can have
a big effect on the bottom line. The recurring, annual maintenance cost of
applications can range between 25% to 50% of the initial development cost
(Gartner Group, May 2002).

<a id="cookbook--load-a-catalog-from-a-web-application"></a>

## Load a Catalog From a Web Application

*Problem:* You'd like to load a catalog
automatically when a web application starts.

*Solution:* Utilize the
`ChainListener` bundled with the Commons Chain of
Responsibility Package.

*Discussion:* A Catalog can be created
progmatically, using conventional Java statements, or by specifying the
catalog members as metadata (an XML document). For testing, it can be
easiest to create a catalog programatically. For deployment, catalogs are
much easier to maintain as metadata. The downside of using metadata is
that it needs to be parsed so that the specified objects can be created.
Happily, the Commons Chain of Responsibility package comes bundled with a
Listener that can read a Catalog metadata file and create the
corresponding object graph.

To use ChainListener in a web application, just add a reference to
your application's web.xml (yet another metadata document). One such
reference is shown below. Loading a ChainListener via a web.xml

```
<!-- Commons Chain listener to load catalogs  -->
<context-param>
  <param-name>org.apache.commons.chain.CONFIG_CLASS_RESOURCE</param-name>
  <param-value>resources/catalog.xml</param-value>
</context-param>
<listener>
  <listener-class>org.apache.commons.chain.web.ChainListener</listener-class>
</listener>
```

The elements in this example expect that there is a
"catalog.xml" file stored on the application's classpath under a directory
named "resources". Usually, this would mean that there is a "resources"
directory under "WEB-INF/classes". If you are using Maven to build your
application, Maven can copy metadata files from your source tree to the
web infrastructure tree automatically. Many teams do the same with custom
Ant build files. Shown below is a fragment of a Maven properties file
that copies `catalog.xml` from a directory under
"`src/resources/chain`" to
"`/WEB-INF/classpath/resources`" under the web
deployment directory. Managing resources in a Maven properties file

```
<!-- ... -->

<build>
  <sourceDirectory>src/java</sourceDirectory>
  <resources>
    <resource>
      <directory>${basedir}/src/resources/chain</directory>
      <targetPath>resources</targetPath>
      <includes>
        <include>catalog.xml</include>
      </includes>
    </resource>
  </resources>
</build>

<!-- ... -->
```

You can also configure ChainListener to read files from a system path
or from a JAR. See the JavaDoc for all the configuration details. There
is also a `ChainServlet` if you are using the Servlet 2.2
platform.

Using the default attribute, and given an
`HttpServletRequest` instance, you can access the
catalog by coding:

```
Catalog catalog = (Catalog) request.getSession()
        .getServletContext().getAttribute("catalog");
```

Given the catalog, you can execute a command and pass it a context, like so:

```
Command command = catalog.getCommand(commandName);  
    boolean stop = command.execute(context);
```

Of course, the hard part is populating the context and determining
which command we need to run for a given request. That work is often left
to a Front Controller, like the one implemented by Apache Struts.
Accordingly, we include a "Call a Command from Struts" recipe in this
chapter. If you like Controllers, but don't like Struts, there are also
"Create a Controller" and "Call a Command from a Servlet" recipes.

<a id="cookbook--call-a-command-from-struts"></a>

## Call a Command From Struts

*Problem:* You'd like to call Commands from
within a Struts application.

*Solution:* Use a CommandAction to call a Command
named for your ActionForm.

*Discussion:* As a Front Controller, the Apache
Struts web application framework has three primary responsibilities.

1. Validate a user request
2. Process a user request
3. Create a response to the request

The third item is usually delegated to a server page.
Struts provides framework-aware components, like JSP tag libraries, to
encourage developers to use another resource to create the response. In
this way, Struts needs only to select the resource. The actual response
creation is handled elsewhere.

Struts also bundles a component to help validate the user request.
The Struts Validator utilizes metadata to vet request values and create
user prompts should validation fail.

To discharge its responsibility to "Process a user request", Struts
provides an extension point called the "`Action`"
class. The Struts Action is a blank slate where developers can do whatever
is necessary to process the request. Some developers even make JDBC calls
from Actions, but such practices are discouraged. The Struts best practice
is for Actions to delegate business and system logic calls to another
component, such as a business facade. The Struts
Action passes appropriate values to one or methods on the facade. The
outcome is used to determine an appropriate response. Often, the outcome
of an Action is described as either "success " or "failure".

Aside from the blank Action, Struts distributes several "standard"
Actions, such as the `DispatchAction`. The standard
Actions are designed to be used several times in different ways within an
application. To allow reuse of Actions, Struts provides a
Decorator class called an
`ActionMapping`. Runtime details can be specified
through the `ActionMappings`, so that each usage of a
standard Action can be slightly different.

To solve the problem of calling a Command from Struts, we can use a
standard Action to retrieve the Catalog and call the Command. We can
specify runtime details in the ActionMapping. Our details include which
set of validations to pass and which Command to
run.

In practice, the set of validations we need to pass and the command
we need to run are closely coupled. In fact, it can be a good practice to
create a distinct set of validations for each Command. If a Command
changes, then its validations can change with it, without affecting other
Commands.

In Struts, the set of validations is coupled to the ActionForm name.
The ActionForm name is a logical identifier, separate from the ActionForm
classname. When you use the Struts Validator, the "form" name for the
Validations is the same string as the ActionForm "name" specified by the
ActionMapping. A database guru would call this a 1:1 relation; the
Validator form name and the ActionForm name are shared keys. If we want
each Command to have its own set of validations, and it's own
ActionMapping, it follows that we should use the same "key" throughout.
The Command name can be the ActionForm name as well as the Validator form
name.

The following example shows how the names line up in the three metadata files, the catalog.xml, the validation.xml, and the struts-config.xml. The token, or "key", that links the three files together is "LocaleChange"A tale of three metadata files: catalog.xml, validation.xml, and struts-config.xml

```
<!-- catalog.xml -->
<?xml version="1.0" ?>
<catalog>
    <command
        name="<em>LocaleChange</em>"
        className="org.apache.commons.chain.mailreader.commands.LocaleChange" />
</catalog>

<!-- validation.xml -->
<?xml version="1.0" ?>
<!DOCTYPE form-validation PUBLIC
    "-//Apache Software Foundation//DTD Commons Validator Rules Configuration 1.1//EN"
    "http://jakarta.apache.org/commons/dtds/validator_1_1.dtd">
<form-validation>
    <formset>
        <form name="<em>LocaleChange</em>">
            <field property="language" depends="required">
                <arg0 key="prompt.language"/>
            </field>
        </form>
    </formset>
</form-validation>

<!-- struts-config.xml -->
<?xml version="1.0" ?>
<!DOCTYPE struts-config PUBLIC
          "-//Apache Software Foundation//DTD Struts Configuration 1.2//EN"
          "http://jakarta.apache.org/struts/dtds/struts-config_1_2.dtd">
<struts-config>
    <form-beans>
        <form-bean
            name="<em>LocaleChange</em>"
            type="org.apache.struts.validator.DynaValidatorForm">
           <form-property name="language" type="java.lang.String"/>
           <form-property name="country" type="java.lang.String"/>
         </form-bean>
     </form-beans>
    <action-mappings>
        <action path="/LocaleChange"
            name="<em>LocaleChange</em>"
            type="org.apache.commons.chain.mailreader.struts.CommandAction">
        <forward name="success" path="/Welcome.do" />
        </action>
    </action-mappings>
<struts-config>
```

In the above example, we used "LocaleChange" for the Command name, the validation Form name, and the Action form-bean name. To trigger the
thread, all we need to do is define a generic Action that will use the
form-bean name as the Command name. The example below shows our
`CommandAction`. The CommandAction links the form-bean name with the Command
name

```
package org.apache.commons.chain.mailreader.struts;
import org.apache.commons.chain.Catalog;
import org.apache.commons.chain.Command;
import org.apache.commons.chain.Context;
import org.apache.commons.chain.web.servlet.ServletWebContext;
import org.apache.struts.action.Action;
import org.apache.struts.action.ActionForm;
import org.apache.struts.action.ActionForward;as the ActionForm name.
import org.apache.struts.action.ActionMapping;
import javax.servlet.ServletContext;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class CommandAction extends Action {

    protected Command getCommand(ActionMapping mapping,
                                 ActionForm form,
                                 HttpServletRequest request,
                                 HttpServletResponse response)
            throws Exception {
        Catalog catalog = (Catalog) request.getSession()
                .getServletContext().getAttribute("catalog");
        String name = mapping.getName();
        Command command = catalog.getCommand(name);
        return command;
    }

    protected Context getContext(ActionMapping mapping,
                                 ActionForm form,
                                 HttpServletRequest request,
                                 HttpServletResponse response)
            throws Exception {
        ServletContext application = request.getSession()
                .getServletContext();
        Context context = new ServletWebContext(
                application, request, response);
        return context;
    }

    protected static String SUCCESS = "success";

    protected ActionForward findLocation(ActionMapping mapping,
            boolean stop) {
        if (stop) return mapping.getInputForward(); // Something failed
        return mapping.findForward(SUCCESS);
    }

    public ActionForward execute(
            ActionMapping mapping,
            ActionForm form,
            HttpServletRequest request,
            HttpServletResponse response)
            throws Exception {
        Command command = getCommand(mapping, form, request, response);
        Context context = getContext(mapping, form, request, response);
        boolean stop = command.execute(context);
        ActionForward location = findLocation(mapping, stop);
        return location;
    }
```

The entry point to an Action class is the
`execute` method. Our execute method calls
`getCommand` and
`getContext` methods that we have defined to obtain
the Command from the catalog and to build a Context based on the web
request. Keeping life simple, we use the
`ServletWebContext` bundled with Commons Chain.
Depending on your needs, you might want to define your own specialized
Context. (See "Create a Context" Recipe.) Our execute method then calls the
command's `execute` method. We pass the return
value of command.execute to our `findLocation`
method, which determines "success" or "failure".

Another way to write CommandAction would be to use the ActionMapping
"`parameter`" property to indicate the Command name .
To do that, we'd patch `getCommand` to call
`mapping.getParameter()` instead of
`getName()`, like this:

```
  -     String name = mapping.getName();
  +     String name = mapping.getParameter();
```

(The minus sign means remove, or subtract, the line. The plus sign
means insert, or add, the line. The Unix patch program follows this
format.)

The "parameter" approach in the preceding example lets us name the
form-beans independently of the Command name. But, a consequence is that
we have to specify the Command name for each ActionMapping.
(*Bor-ring!*) You could also merge the two approaches
and return the parameter property only when it is used, like
this:

```
        String name = mapping.getParameter();
  +     if ((null==name) || (name=="")) name = mapping.getName();
```

Or you could mix and match the two approches, using CommandAction
when the formbean name and the command name match, and a
CommandParameterAction, when they do not. Struts allows you to use as many
Actions, and standard Actions, as you like.

Note that our Command is expected to do the "custom" work usually
delegated to the Action. Consequently, we do not need to create an Action
subclass for each task. We can use one or two standard Actions and have
them call the appropriate Command class. A set of related tasks (or
"story") might share an ActionForm class and a Command class, but, most
often, the Actions can be standard, reusable Actions.

Something else to note about the above example is that we use the
"LocaleChange" token as the path attribute. This
means that the story would be trigged by opening (for example) the
"/LocaleChange.do" page. Even so, the path is
*not* part of our semantic
chain. The path is not a fully logical name that we control.
The path token is shared with the container, and the container may have
its own constraints on the path. (JAAS pattern matching, for example.) The
path can't be part of our chain of keys, since it is shared with the
container's "business logic".

Having used "LocaleChange" for everything else, using it for the
path token seems natural. Most of us would do the same. But, the path can
vary as needed, without upsetting the rest of the semantic chain. If the
"path" needs to change to suit a change in the JAAS configuration, nothing
else needs to change.

Of course, there would be several other ways to call a Command from
a Struts Action. Since the request is passed to the Action, it's easy to
obtain a Catalog stored in application scope. Once you have access to the
Catalog, the rest is easy.

Other frameworks, like WebWorks and Maverick, have components
similar to Struts Actions. Any of these components can be used to create a
Context, access the Catalog, and execute a Command.

<a id="cookbook--create-a-controller"></a>

## Create a Controller

*Problem:* You want to base your application's
Controller components on the Commons Chain of
Command package.

*Solution:* Create a set of interfaces for a
Controller package that can be implemented using base classes from the
Chain of Command package.

*Warning: Since we are creating a base package, this recipe
is longer than most. Each individual component is simple enough, but there
are several components to cover. Since the components are interrelated, covering them separately would be confusing. So, sit back, loosen your
belt, and enjoy, while we whip up a "seven-course meal".*

*Discussion:* Many applications use
implementations of the Controller pattern to field user requests.
*Core J2EE Patterns: Best Practices and Design
Strategies* [ISBN 0-13-142246-4] describes a controller as a component that
"interacts with a client, controlling and managing the handling of each
request." There are several flavors of controllers, including Application
Controllers and Front Controllers. Many web application frameworks, like
Apache Struts, utilize a Front Controller.

Often, an implementation of the Controller pattern will in turn use
the Command pattern or Chain of Command pattern. How can we use the
Commons Chain of Command package to implement a Controller?

Following the general description from Core J2EE Patterns, let's
start by defining a test that passes a request to a controller and
confirms that an appropriate response is returned.

To write our test, we need to:

1. Create a Controller.
2. Add a Handler for our Request to the Controller.
3. Create a Request and pass it to the Controller.
4. Confirm that the Request returns the expected Response.

To simplify writing the test, lets make a few executive
decisions:

1. The Request and Response object have "name" properties.
2. The name of a Response matches the name of its Request (a shared
   key).
3. The test will be based on interfaces; implemented classes will
   extend Commons Chain members.
4. The Controller extends Catalog.
5. The Request and Response extend Context.
6. The Request Handler extends Command.
7. For no particular reason, we'll call our controller package
   "Agility".

The following example shows a `ProcessingTest` class with
our `testRequestResponseNames` method.Test to assert that our Controller can process a Request and
return an appropriate Response

```
package org.apache.commons.agility;

import junit.framework.TestCase; 
import org.apache.commons.agility.impl.ControllerCatalog;
import org.apache.commons.agility.impl.HandlerCommand;
import org.apache.commons.agility.impl.RequestContext;

public class ProcessingTest extends TestCase {

    public void testRequestResponseName() {
        
        String NAME = "TestProcessing"; 

        Controller controller = new ControllerCatalog();

        RequestHandler handler = new HandlerCommand(NAME);
        controller.addHandler(handler);
        Request request = new RequestContext(NAME);
        controller.process(request);
        Response response = request.getResponse();

        assertNotNull(response);
        assertEquals(NAME, response.getName());
    }
}
```

To compile the ProcessingTest class, we will need interface
members for `Controller`, `RequestHandler`, `Request`, and
`Response`, and class members for
`ControllerCatalog`, `HandlerCommand`, and
`RequestContext`. The four interfaces needed to realize ProcessingTest

To compile ProcessTest, we need to define four
interfaces.

```
// Controller.java
package org.apache.commons.agility;
public interface Controller {
    void addHandler(RequestHandler handler);
    RequestHandler getHandler(String name) throws ProcessException;
    void process(Request request) throws ProcessException;
}

// Request.java
package org.apache.commons.agility;
public interface Request {
    String getName();
    Response getResponse();
    void setResponse(Response response);
}

// Response.java
package org.apache.commons.agility;
public interface Response {
    String getName();
}

// RequestHandler.java
package org.apache.commons.agility;
public interface RequestHandler {
    String getName();
    void handle(Request request) throws ProcessException;
}

// ProcessException.java
package org.apache.commons.agility;
public class ProcessException extends Exception {
    public ProcessException(Throwable cause) {
        super(cause);
    }
}
```

With the interfaces out of the way, we can turn to the classes we
need to implement.The thee classes needed to realize ProcessingTest.

If we create the classes , and stub-out the
methods, we can get the code to compile. The test will run, but skeleton
classes won't pass muster. Let's implement each class, starting with
HandlerCommand, which is shown below.

HandlerCommand provides default behavior that subclasses can
override

```
package org.apache.commons.agility.impl;

import org.apache.commons.agility.ProcessException;
import org.apache.commons.agility.Request;
import org.apache.commons.agility.RequestHandler;
import org.apache.commons.agility.Response;
import org.apache.commons.chain.Command;
import org.apache.commons.chain.Context;

public class HandlerCommand implements Command, RequestHandler {
    String name =  null;

    public HandlerCommand(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public boolean execute(Context context) throws Exception {
        handle((Request) context);
        return true;
    }

    public void handle(Request request) throws ProcessException {
        try {
            String name = request.getName();
            Response response = new ResponseContext(name);
            request.setResponse(response);
        } catch (Exception e) {
            throw new ProcessException(e);
        }
    }
}
```

The `handle(Request)` method of
HandlerCommand realizes the prime responsibility for this class: create a
Response for the Request. The execute(Context) method is an
adapter that delegates to the handle method. Now we
can call execute or handle and achieve the same result. The constructor
assigns each instance of HandlerCommand a name so that it can be matched
with a Request.

The handle(Request) method shown here is not very useful. However, it will pass our test and prove the infrastructure is working. Subclasses
can override handle(Request) to create the appropriate Response for a
given Request. Since HandlerCommands are still Commands, we can itemize
our HandlerCommand subclasses as metadata (an XML document). This will
make it easy to handle new Requests as our application grows.

The HandlerCommand class creates a ResponseContext instance and sets
it as the Response. The ResponseContext class is shown below.

Many other implementations of ResponseContext are possible.
They just need to implement Response and extend ContextBase.

```
package org.apache.commons.agility.impl;

import org.apache.commons.agility.Response;
import org.apache.commons.chain.impl.ContextBase;

public class ResponseContext extends ContextBase implements Response {

    private String name;

    public ResponseContext(String name) {
        super();
        this.name = name;
    }

    public String getName() {
        return name;
    }
}
```

Since we're just testing the infrastructure, our
ResponseContext is rudimentary. A Front Controller for a web application
framework might define several attributes for a Response, such as the
location of a server page. The RequestHandler can create any kind of
Response object that might be needed.

Whatever RequestHandlers we need are added to the Catalog, either as
metadata or programatically. Our tests add the handler programatically, so
we need to implement the AddHandler method. The following shows our
implementation of CatalogController. RequestHandlers can be added to the CatalogController
programatically or through metadata

```
package org.apache.commons.agility.impl;

import org.apache.commons.agility.Controller;
import org.apache.commons.agility.ProcessException;
import org.apache.commons.agility.Request;
import org.apache.commons.agility.RequestHandler;
import org.apache.commons.chain.impl.CatalogBase;
import org.apache.commons.chain.Command;

public class ControllerCatalog extends CatalogBase implements Controller {
    public RequestHandler getHandler(String name) {
        return (RequestHandler) getCommand(request.getName());
    }

    public void addHandler(RequestHandler handler) {
        this.addCommand(handler.getName(), (Command) handler);
    }

    public void process(Request request) throws ProcessException {
        Handler handler = getHandler(request.getName());
        if (handler != null) handler.handle(request);
    }
}
```

The main entry point to our Controller is the
`process(Request)` method. This method could host a
great deal of functionality. We could even implement the process method as
a series of Commands or Chains of Commands. An application could then
fine-tune the request processing by specifying different Commands in a
metadata catalog. The Struts web application framework uses this approach
for its request processor.

But for now, we just want to pass our test. All the process method
needs to do is find the RequestHandler and call its handle(Request)
method. We can do that just by looking up the name of the Request in our
catalog and retrieving the matching RequestHandler (or Command).

The `addHandler(RequestHandler)` method is
another adapter that delegates to an inherited method. In this case, addHandler calls `addCommand(String,Command)`.
Since our RequestHandlers are Commands, they can be passed to the
superclass method. The `getHandler(String)` method
is yet another adapter/delegate.

Last but not least is the RequestContext class, shown below.

RequestContext ties it all together

```
package org.apache.commons.agility.impl;

import org.apache.commons.agility.Request;
import org.apache.commons.agility.Response;
import org.apache.commons.chain.impl.ContextBase;

public class RequestContext extends ContextBase implements Request {

    private String name;
    private Response response;

    public RequestContext(String name) {
        super();
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public Response getResponse() {
        return response;
    }

    public void setResponse(Response response) {
        this.response = response;
    }
}
```

Like the ResponseContext, an application could add several
properties to its Request class. A web application might wrap or transfer
attributes from the HttpServletRequest. But so long as the class
implements Request and Context, it will plug into our Controller
implementation.

Using the interfaces and base classes shown here, you can create
whatever Controllers you need.

<a id="cookbook--call-a-command-from-a-servlet"></a>

## Call a Command From a Servlet

*Problem:* You would like to call commands during
your application using a servlet.

*Solution:* Use the Listener from the "Load a
Catalog from a Web Application" recipe to setup a list of Commands, and
the Controller from the "Create a Controller" recipe to process the
request.

*Discussion: [TODO:]*

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/issue-tracking.html -->

<!-- page_index: 4 -->

<a id="issue-tracking--commons-chain-issue-tracking"></a>

## Commons Chain Issue tracking

Commons Chain uses [ASF JIRA](http://issues.apache.org/jira/) for tracking issues.
See the [Commons Chain JIRA project page](http://issues.apache.org/jira/browse/CHAIN).

To use JIRA you may need to [create an account](http://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](http://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Commons Chain please do the following:

1. [Search existing open bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310462&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/dormant/commons-chain/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310462&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](http://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310462&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Commons Chain are all unpaid volunteers

For more information on subversion and creating patches see the
[Apache Contributors Guide](http://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Commons Chain bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310462&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Commons Chain bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310462&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Commons Chain bugs](http://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310462&sorter/field=issuekey&sorter/order=DESC)

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/building.html -->

<!-- page_index: 5 -->

<a id="building--overview"></a>

## Overview

Commons Chain uses [Maven 2](http://maven.apache.org) or
[Ant](http://ant.apache.org) as a build system.

Chain 1.2 requires a minimum of JDK 1.3 to build, although the Maven 2 build
requires JDK 1.4+

<a id="building--maven-2-goals"></a>

## Maven 2 Goals

The following ***Maven 2*** commands can be used to build Chain:

- `mvn clean` - clean up
- `mvn test` - compile and run the unit tests
- `mvn site` - create the documentation
- `mvn package` - build the jar
- `mvn install` - build the jar and install in local maven repository
- `mvn site assembly:assembly` - Create the source and binary distributions

<a id="building--ant-goals"></a>

## Ant Goals

The following ***Ant*** commands can be used to build Chain:

- `ant clean` - clean up
- `ant test` - compile and run the unit tests
- `ant javadoc` - create javadocs
- `ant jar` - build the jar
- `ant dist` - Create the source and binary distributions

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/project-info.html -->

<!-- page_index: 6 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | An implementation of the GoF Chain of Responsibility pattern |
| [Continuous Integration](#integration) | This is a link to the definitions of all continuous integration processes that builds and tests code on a frequent, regular basis. |
| [Dependencies](https://commons.apache.org/dormant/commons-chain/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Mailing Lists](https://commons.apache.org/dormant/commons-chain/mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Plugin Management](https://commons.apache.org/dormant/commons-chain/plugin-management.html) | This document lists the plugins that are defined through pluginManagement. |
| [Project License](https://commons.apache.org/dormant/commons-chain/license.html) | This is a link to the definitions of project licenses. |
| [Project Plugins](https://commons.apache.org/dormant/commons-chain/plugins.html) | This document lists the build plugins and the report plugins used by this project. |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Project Team](https://commons.apache.org/dormant/commons-chain/team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Repository](https://commons.apache.org/dormant/commons-chain/source-repository.html) | This is a link to the online source repository that can be viewed via a web browser. |

---

<a id="integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/integration.html -->

<!-- page_index: 7 -->

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

<a id="project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/project-summary.html -->

<!-- page_index: 8 -->

<a id="project-summary--project-summary"></a>

## Project Summary

<a id="project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Commons Chain |
| Description | An implementation of the GoF Chain of Responsibility pattern |
| Homepage | <http://commons.apache.org/chain/> |

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
| GroupId | commons-chain |
| ArtifactId | commons-chain |
| Version | 1.3-SNAPSHOT |
| Type | jar |

---

<a id="project-reports"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/project-reports.html -->

<!-- page_index: 9 -->

<a id="project-reports--generated-reports"></a>

## Generated Reports

This document provides an overview of the various reports that are automatically generated by [Maven](http://maven.apache.org) . Each report is briefly described below.

<a id="project-reports--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [Changes Report](#changes-report) | Changes Report on Releases of the Project. |
| [Checkstyle](#checkstyle) | Report on coding style conventions. |
| [Clirr](#clirr-report) | Report on binary and source API differences between releases |
| [FindBugs Report](#findbugs) | Generates a source code report with the FindBugs Library. |
| [JavaDocs](https://commons.apache.org/dormant/commons-chain/apidocs/index.html) | JavaDoc API documentation. |
| [JDepend](#jdepend-report) | JDepend traverses Java class file directories and generates design quality metrics for each Java package. JDepend allows you to automatically measure the quality of a design in terms of its extensibility, reusability, and maintainability to manage package dependencies effectively. |
| [RAT Report](#rat-report) | Report on compliance to license related source code policies |
| [Source Xref](https://commons.apache.org/dormant/commons-chain/xref/index.html) | HTML based, cross-reference version of Java source code. |
| [Surefire Report](#surefire-report) | Report on the test results of the project. |
| [Test JavaDocs](https://commons.apache.org/dormant/commons-chain/testapidocs/index.html) | Test JavaDoc API documentation. |
| [Test Source Xref](https://commons.apache.org/dormant/commons-chain/xref-test/index.html) | HTML based, cross-reference version of Java test source code. |

---

<a id="checkstyle"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/checkstyle.html -->

<!-- page_index: 10 -->

<a id="checkstyle--checkstyle-results"></a>

## Checkstyle Results

The following document contains the results of [Checkstyle](http://checkstyle.sourceforge.net/). [![rss feed](assets/images/rss_618b31344ffa3fb0.png)](#checkstyle--checkstyle.rss)

<a id="checkstyle--summary"></a>

## Summary

| Files | Infos info | Warnings warning | Errors error |
| --- | --- | --- | --- |
| 63 | 0 | 0 | 16 |

<a id="checkstyle--files"></a>

## Files

| Files | I info | W warning | E error |
| --- | --- | --- | --- |
| [org/apache/commons/chain/web/portlet/PortletSessionScopeMap.java](#checkstyle--org.apache.commons.chain.web.portlet.portletsessionscopemap.java) | 0 | 0 | 2 |
| [org/apache/commons/chain/web/portlet/PortletWebContext.java](#checkstyle--org.apache.commons.chain.web.portlet.portletwebcontext.java) | 0 | 0 | 3 |
| [org/apache/commons/chain/web/servlet/ServletWebContext.java](#checkstyle--org.apache.commons.chain.web.servlet.servletwebcontext.java) | 0 | 0 | 3 |
| [org/apache/commons/chain/web/servlet/ServletSessionScopeMap.java](#checkstyle--org.apache.commons.chain.web.servlet.servletsessionscopemap.java) | 0 | 0 | 2 |
| [org/apache/commons/chain/web/ChainResources.java](#checkstyle--org.apache.commons.chain.web.chainresources.java) | 0 | 0 | 1 |
| [org/apache/commons/chain/impl/ContextBase.java](#checkstyle--org.apache.commons.chain.impl.contextbase.java) | 0 | 0 | 2 |
| [org/apache/commons/chain/impl/CatalogBase.java](#checkstyle--org.apache.commons.chain.impl.catalogbase.java) | 0 | 0 | 1 |
| [org/apache/commons/chain/impl/ChainBase.java](#checkstyle--org.apache.commons.chain.impl.chainbase.java) | 0 | 0 | 2 |

<a id="checkstyle--details"></a>

## Details

<a id="checkstyle--org-apache-commons-chain-web-portlet-portletsessionscopemap.java"></a>

### org/apache/commons/chain/web/portlet/PortletSessionScopeMap.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Conditional logic can be removed. | [132](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletSessionScopeMap.html#132) |
| error | Conditional logic can be removed. | [238](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletSessionScopeMap.html#238) |

<a id="checkstyle--org-apache-commons-chain-web-portlet-portletwebcontext.java"></a>

### org/apache/commons/chain/web/portlet/PortletWebContext.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Variable 'context' must be private and have accessor methods. | [81](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletWebContext.html#81) |
| error | Variable 'request' must be private and have accessor methods. | [122](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletWebContext.html#122) |
| error | Variable 'response' must be private and have accessor methods. | [135](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletWebContext.html#135) |

<a id="checkstyle--org-apache-commons-chain-web-servlet-servletwebcontext.java"></a>

### org/apache/commons/chain/web/servlet/ServletWebContext.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Variable 'context' must be private and have accessor methods. | [80](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletWebContext.html#80) |
| error | Variable 'request' must be private and have accessor methods. | [127](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletWebContext.html#127) |
| error | Variable 'response' must be private and have accessor methods. | [140](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletWebContext.html#140) |

<a id="checkstyle--org-apache-commons-chain-web-servlet-servletsessionscopemap.java"></a>

### org/apache/commons/chain/web/servlet/ServletSessionScopeMap.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Conditional logic can be removed. | [130](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletSessionScopeMap.html#130) |
| error | Conditional logic can be removed. | [233](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletSessionScopeMap.html#233) |

<a id="checkstyle--org-apache-commons-chain-web-chainresources.java"></a>

### org/apache/commons/chain/web/ChainResources.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Utility classes should not have a public or default constructor. | [39](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/ChainResources.html#39) |

<a id="checkstyle--org-apache-commons-chain-impl-contextbase.java"></a>

### org/apache/commons/chain/impl/ContextBase.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Definition of 'equals()' without corresponding definition of 'hashCode()'. | [126](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/impl/ContextBase.html#126) |
| error | '}' should be on the same line. | [181](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/impl/ContextBase.html#181) |

<a id="checkstyle--org-apache-commons-chain-impl-catalogbase.java"></a>

### org/apache/commons/chain/impl/CatalogBase.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Variable 'commands' must be private and have accessor methods. | [48](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/impl/CatalogBase.html#48) |

<a id="checkstyle--org-apache-commons-chain-impl-chainbase.java"></a>

### org/apache/commons/chain/impl/ChainBase.java

| Violation | Message | Line |
| --- | --- | --- |
| error | Variable 'commands' must be private and have accessor methods. | [118](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/impl/ChainBase.html#118) |
| error | Variable 'frozen' must be private and have accessor methods. | [125](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/impl/ChainBase.html#125) |

©
2003-2010
The Apache Software Foundation

---

<a id="clirr-report"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/clirr-report.html -->

<!-- page_index: 11 -->

<a id="clirr-report--clirr-results"></a>

## Clirr Results

The following document contains the results of [Clirr](http://clirr.sourceforge.net/).

- Current Version: 1.3-SNAPSHOT
- Comparison Version: 1.1

<a id="clirr-report--summary"></a>

## Summary

| Severity | Number |
| --- | --- |
| Error Error | 0 |
| Warning Warning | 0 |
| Info Info | 23 |

<a id="clirr-report--details"></a>

## Details

| Severity | Message | Class | Method / Field |
| --- | --- | --- | --- |
| Info | Method 'protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.generic.LookupCommand](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/generic/LookupCommand.html) | protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context) |
| Info | Method 'protected java.lang.String getCommandName(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.generic.LookupCommand](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/generic/LookupCommand.html) | protected java.lang.String getCommandName(org.apache.commons.chain.Context) |
| Info | Added org.apache.commons.chain.Filter to the set of implemented interfaces | [org.apache.commons.chain.web.servlet.PathInfoMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/PathInfoMapper.html) |  |
| Info | Added org.apache.commons.chain.generic.LookupCommand to the list of superclasses | [org.apache.commons.chain.web.servlet.PathInfoMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/PathInfoMapper.html) |  |
| Info | Method 'public boolean execute(org.apache.commons.chain.Context)' has been removed, but an inherited definition exists. | [org.apache.commons.chain.web.servlet.PathInfoMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/PathInfoMapper.html) | public boolean execute(org.apache.commons.chain.Context) |
| Info | Method 'protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.web.servlet.PathInfoMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/PathInfoMapper.html) | protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context) |
| Info | Method 'public java.lang.String getCatalogKey()' has been deprecated | [org.apache.commons.chain.web.servlet.PathInfoMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/PathInfoMapper.html) | public java.lang.String getCatalogKey() |
| Info | Method 'protected java.lang.String getCommandName(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.web.servlet.PathInfoMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/PathInfoMapper.html) | protected java.lang.String getCommandName(org.apache.commons.chain.Context) |
| Info | Method 'public void setCatalogKey(java.lang.String)' has been deprecated | [org.apache.commons.chain.web.servlet.PathInfoMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/PathInfoMapper.html) | public void setCatalogKey(java.lang.String) |
| Info | Added org.apache.commons.chain.Filter to the set of implemented interfaces | [org.apache.commons.chain.web.servlet.RequestParameterMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/RequestParameterMapper.html) |  |
| Info | Added org.apache.commons.chain.generic.LookupCommand to the list of superclasses | [org.apache.commons.chain.web.servlet.RequestParameterMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/RequestParameterMapper.html) |  |
| Info | Method 'public boolean execute(org.apache.commons.chain.Context)' has been removed, but an inherited definition exists. | [org.apache.commons.chain.web.servlet.RequestParameterMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/RequestParameterMapper.html) | public boolean execute(org.apache.commons.chain.Context) |
| Info | Method 'protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.web.servlet.RequestParameterMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/RequestParameterMapper.html) | protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context) |
| Info | Method 'protected java.lang.String getCommandName(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.web.servlet.RequestParameterMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/RequestParameterMapper.html) | protected java.lang.String getCommandName(org.apache.commons.chain.Context) |
| Info | Method 'public java.lang.String getParameter()' has been deprecated | [org.apache.commons.chain.web.servlet.RequestParameterMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/RequestParameterMapper.html) | public java.lang.String getParameter() |
| Info | Method 'public void setCatalogKey(java.lang.String)' has been deprecated | [org.apache.commons.chain.web.servlet.RequestParameterMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/RequestParameterMapper.html) | public void setCatalogKey(java.lang.String) |
| Info | Added org.apache.commons.chain.Filter to the set of implemented interfaces | [org.apache.commons.chain.web.servlet.ServletPathMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletPathMapper.html) |  |
| Info | Added org.apache.commons.chain.generic.LookupCommand to the list of superclasses | [org.apache.commons.chain.web.servlet.ServletPathMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletPathMapper.html) |  |
| Info | Method 'public boolean execute(org.apache.commons.chain.Context)' has been removed, but an inherited definition exists. | [org.apache.commons.chain.web.servlet.ServletPathMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletPathMapper.html) | public boolean execute(org.apache.commons.chain.Context) |
| Info | Method 'protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.web.servlet.ServletPathMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletPathMapper.html) | protected org.apache.commons.chain.Catalog getCatalog(org.apache.commons.chain.Context) |
| Info | Method 'public java.lang.String getCatalogKey()' has been deprecated | [org.apache.commons.chain.web.servlet.ServletPathMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletPathMapper.html) | public java.lang.String getCatalogKey() |
| Info | Method 'protected java.lang.String getCommandName(org.apache.commons.chain.Context)' has been added | [org.apache.commons.chain.web.servlet.ServletPathMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletPathMapper.html) | protected java.lang.String getCommandName(org.apache.commons.chain.Context) |
| Info | Method 'public void setCatalogKey(java.lang.String)' has been deprecated | [org.apache.commons.chain.web.servlet.ServletPathMapper](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletPathMapper.html) | public void setCatalogKey(java.lang.String) |

©
2003-2010
The Apache Software Foundation

---

<a id="findbugs"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/findbugs.html -->

<!-- page_index: 12 -->

<a id="findbugs--findbugs-bug-detector-report"></a>

## FindBugs Bug Detector Report

The following document contains the results of [FindBugs Report](http://findbugs.sourceforge.net)

FindBugs Version is *1.2.1*

Threshold is *Normal*

Effort is *Default*

<a id="findbugs--summary"></a>

## Summary

| Classes | Bugs | Errors | Missing Classes |
| --- | --- | --- | --- |
| 227 | 11 | 0 | 0 |

<a id="findbugs--files"></a>

## Files

| Class | Bugs |
| --- | --- |
| [org.apache.commons.chain.generic.DispatchCommand](#findbugs--org.apache.commons.chain.generic.dispatchcommand) | 1 |
| [org.apache.commons.chain.impl.ContextBase](#findbugs--org.apache.commons.chain.impl.contextbase) | 1 |
| [org.apache.commons.chain.impl.ContextBase$1](#findbugs--org.apache.commons.chain.impl.contextbase-1) | 1 |
| [org.apache.commons.chain.web.ChainServlet](#findbugs--org.apache.commons.chain.web.chainservlet) | 1 |
| [org.apache.commons.chain.web.faces.FacesWebContext](#findbugs--org.apache.commons.chain.web.faces.faceswebcontext) | 1 |
| [org.apache.commons.chain.web.portlet.PortletWebContext](#findbugs--org.apache.commons.chain.web.portlet.portletwebcontext) | 3 |
| [org.apache.commons.chain.web.servlet.ServletWebContext](#findbugs--org.apache.commons.chain.web.servlet.servletwebcontext) | 3 |

<a id="findbugs--org.apache.commons.chain.generic.dispatchcommand"></a>

### org.apache.commons.chain.generic.DispatchCommand

| Bug | Category | Details | Line |
| --- | --- | --- | --- |
| org.apache.commons.chain.generic.DispatchCommand.DEFAULT\_SIGNATURE should be package protected | MALICIOUS\_CODE | [MS\_PKGPROTECT](http://findbugs.sourceforge.net/bugDescriptions.html#MS_PKGPROTECT) | [49](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/generic/DispatchCommand.html#49) |

<a id="findbugs--org.apache.commons.chain.impl.contextbase"></a>

### org.apache.commons.chain.impl.ContextBase

| Bug | Category | Details | Line |
| --- | --- | --- | --- |
| org.apache.commons.chain.impl.ContextBase is Serializable; consider declaring a serialVersionUID | BAD\_PRACTICE | [SE\_NO\_SERIALVERSIONID](http://findbugs.sourceforge.net/bugDescriptions.html#SE_NO_SERIALVERSIONID) | [53-583](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/impl/ContextBase.html#53) |

<a id="findbugs--org.apache.commons.chain.impl.contextbase-1"></a>

### org.apache.commons.chain.impl.ContextBase$1

| Bug | Category | Details | Line |
| --- | --- | --- | --- |
| org.apache.commons.chain.impl.ContextBase$1 defines equals and uses Object.hashCode() | BAD\_PRACTICE | [HE\_EQUALS\_USE\_HASHCODE](http://findbugs.sourceforge.net/bugDescriptions.html#HE_EQUALS_USE_HASHCODE) | [127](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/impl/ContextBase.html#127) |

<a id="findbugs--org.apache.commons.chain.web.chainservlet"></a>

### org.apache.commons.chain.web.ChainServlet

| Bug | Category | Details | Line |
| --- | --- | --- | --- |
| org.apache.commons.chain.web.ChainServlet is Serializable; consider declaring a serialVersionUID | BAD\_PRACTICE | [SE\_NO\_SERIALVERSIONID](http://findbugs.sourceforge.net/bugDescriptions.html#SE_NO_SERIALVERSIONID) | [96-241](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/ChainServlet.html#96) |

<a id="findbugs--org.apache.commons.chain.web.faces.faceswebcontext"></a>

### org.apache.commons.chain.web.faces.FacesWebContext

| Bug | Category | Details | Line |
| --- | --- | --- | --- |
| Class org.apache.commons.chain.web.faces.FacesWebContext defines non-transient non-serializable instance field context | BAD\_PRACTICE | [SE\_BAD\_FIELD](http://findbugs.sourceforge.net/bugDescriptions.html#SE_BAD_FIELD) | [Not available](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/faces/FacesWebContext.html#-1) |

<a id="findbugs--org.apache.commons.chain.web.portlet.portletwebcontext"></a>

### org.apache.commons.chain.web.portlet.PortletWebContext

| Bug | Category | Details | Line |
| --- | --- | --- | --- |
| Class org.apache.commons.chain.web.portlet.PortletWebContext defines non-transient non-serializable instance field context | BAD\_PRACTICE | [SE\_BAD\_FIELD](http://findbugs.sourceforge.net/bugDescriptions.html#SE_BAD_FIELD) | [Not available](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletWebContext.html#-1) |
| Class org.apache.commons.chain.web.portlet.PortletWebContext defines non-transient non-serializable instance field request | BAD\_PRACTICE | [SE\_BAD\_FIELD](http://findbugs.sourceforge.net/bugDescriptions.html#SE_BAD_FIELD) | [Not available](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletWebContext.html#-1) |
| Class org.apache.commons.chain.web.portlet.PortletWebContext defines non-transient non-serializable instance field response | BAD\_PRACTICE | [SE\_BAD\_FIELD](http://findbugs.sourceforge.net/bugDescriptions.html#SE_BAD_FIELD) | [Not available](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/portlet/PortletWebContext.html#-1) |

<a id="findbugs--org.apache.commons.chain.web.servlet.servletwebcontext"></a>

### org.apache.commons.chain.web.servlet.ServletWebContext

| Bug | Category | Details | Line |
| --- | --- | --- | --- |
| Class org.apache.commons.chain.web.servlet.ServletWebContext defines non-transient non-serializable instance field context | BAD\_PRACTICE | [SE\_BAD\_FIELD](http://findbugs.sourceforge.net/bugDescriptions.html#SE_BAD_FIELD) | [Not available](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletWebContext.html#-1) |
| Class org.apache.commons.chain.web.servlet.ServletWebContext defines non-transient non-serializable instance field request | BAD\_PRACTICE | [SE\_BAD\_FIELD](http://findbugs.sourceforge.net/bugDescriptions.html#SE_BAD_FIELD) | [Not available](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletWebContext.html#-1) |
| Class org.apache.commons.chain.web.servlet.ServletWebContext defines non-transient non-serializable instance field response | BAD\_PRACTICE | [SE\_BAD\_FIELD](http://findbugs.sourceforge.net/bugDescriptions.html#SE_BAD_FIELD) | [Not available](https://commons.apache.org/dormant/commons-chain/xref/org/apache/commons/chain/web/servlet/ServletWebContext.html#-1) |

---

<a id="jdepend-report"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/jdepend-report.html -->

<!-- page_index: 13 -->

<a id="jdepend-report--metric-results"></a>

## Metric Results

[ [summary](#jdepend-report--summary) ] [ [packages](#jdepend-report--packages) ] [ [cycles](#jdepend-report--cycles) ] [ [explanations](#jdepend-report--explanations) ]
The following document contains the results of a JDepend metric analysis. The various metrics are defined at the bottom of this document.
<a id="jdepend-report--summary"></a>

## Summary

[ [summary](#jdepend-report--summary) ] [ [packages](#jdepend-report--packages) ] [ [cycles](#jdepend-report--cycles) ] [ [explanations](#jdepend-report--explanations) ]

| Package | TC | CC | AC | Ca | Ce | A | I | D | V |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.chain](#jdepend-report--org.apache.commons.chain) | 6 | 0 | 6 | 7 | 4 | 100.0% | 36.0% | 36.0% | 1 |
| [org.apache.commons.chain.config](#jdepend-report--org.apache.commons.chain.config) | 5 | 5 | 0 | 1 | 5 | 0.0% | 83.0% | 17.0% | 1 |
| [org.apache.commons.chain.generic](#jdepend-report--org.apache.commons.chain.generic) | 5 | 4 | 1 | 1 | 4 | 20.0% | 80.0% | 0.0% | 1 |
| [org.apache.commons.chain.impl](#jdepend-report--org.apache.commons.chain.impl) | 10 | 10 | 0 | 2 | 6 | 0.0% | 75.0% | 25.0% | 1 |
| [org.apache.commons.chain.web](#jdepend-report--org.apache.commons.chain.web) | 7 | 4 | 3 | 3 | 11 | 43.0% | 79.0% | 21.0% | 1 |
| [org.apache.commons.chain.web.faces](#jdepend-report--org.apache.commons.chain.web.faces) | 3 | 3 | 0 | 0 | 5 | 0.0% | 100.0% | 0.0% | 1 |
| [org.apache.commons.chain.web.portlet](#jdepend-report--org.apache.commons.chain.web.portlet) | 9 | 9 | 0 | 0 | 5 | 0.0% | 100.0% | 0.0% | 1 |
| [org.apache.commons.chain.web.servlet](#jdepend-report--org.apache.commons.chain.web.servlet) | 16 | 16 | 0 | 0 | 8 | 0.0% | 100.0% | 0.0% | 1 |

<a id="jdepend-report--packages"></a>

## Packages

[ [summary](#jdepend-report--summary) ] [ [packages](#jdepend-report--packages) ] [ [cycles](#jdepend-report--cycles) ] [ [explanations](#jdepend-report--explanations) ]
<a id="jdepend-report--org.apache.commons.chain"></a>

### org.apache.commons.chain

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 7 | 4 | 100.0% | 36.0% | 36.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| org.apache.commons.chain.Catalog org.apache.commons.chain.CatalogFactory org.apache.commons.chain.Chain org.apache.commons.chain.Command org.apache.commons.chain.Context org.apache.commons.chain.Filter | *None* | org.apache.commons.chain.config org.apache.commons.chain.generic org.apache.commons.chain.impl org.apache.commons.chain.web org.apache.commons.chain.web.faces org.apache.commons.chain.web.portlet org.apache.commons.chain.web.servlet | java.lang java.util org.apache.commons.chain.impl org.apache.commons.logging |

<a id="jdepend-report--org.apache.commons.chain.config"></a>

### org.apache.commons.chain.config

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 5 | 0.0% | 83.0% | 17.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| *None* | org.apache.commons.chain.config.ConfigCatalogRule org.apache.commons.chain.config.ConfigDefineRule org.apache.commons.chain.config.ConfigParser org.apache.commons.chain.config.ConfigRegisterRule org.apache.commons.chain.config.ConfigRuleSet | org.apache.commons.chain.web | java.lang java.net org.apache.commons.chain org.apache.commons.digester org.xml.sax |

<a id="jdepend-report--org.apache.commons.chain.generic"></a>

### org.apache.commons.chain.generic

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 4 | 20.0% | 80.0% | 0.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| org.apache.commons.chain.generic.DispatchCommand | org.apache.commons.chain.generic.CopyCommand org.apache.commons.chain.generic.DispatchLookupCommand org.apache.commons.chain.generic.LookupCommand org.apache.commons.chain.generic.RemoveCommand | org.apache.commons.chain.web.servlet | java.lang java.lang.reflect java.util org.apache.commons.chain |

<a id="jdepend-report--org.apache.commons.chain.impl"></a>

### org.apache.commons.chain.impl

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 2 | 6 | 0.0% | 75.0% | 25.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| *None* | org.apache.commons.chain.impl.CatalogBase org.apache.commons.chain.impl.CatalogFactoryBase org.apache.commons.chain.impl.ChainBase org.apache.commons.chain.impl.ContextBase org.apache.commons.chain.impl.ContextBase$1 org.apache.commons.chain.impl.ContextBase$EntrySetImpl org.apache.commons.chain.impl.ContextBase$EntrySetIterator org.apache.commons.chain.impl.ContextBase$MapEntryImpl org.apache.commons.chain.impl.ContextBase$ValuesImpl org.apache.commons.chain.impl.ContextBase$ValuesIterator | org.apache.commons.chain org.apache.commons.chain.web | java.beans java.io java.lang java.lang.reflect java.util org.apache.commons.chain |

<a id="jdepend-report--org.apache.commons.chain.web"></a>

### org.apache.commons.chain.web

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 3 | 11 | 43.0% | 79.0% | 21.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| org.apache.commons.chain.web.AbstractGetLocaleCommand org.apache.commons.chain.web.AbstractSetLocaleCommand org.apache.commons.chain.web.WebContext | org.apache.commons.chain.web.ChainListener org.apache.commons.chain.web.ChainResources org.apache.commons.chain.web.ChainServlet org.apache.commons.chain.web.MapEntry | org.apache.commons.chain.web.faces org.apache.commons.chain.web.portlet org.apache.commons.chain.web.servlet | java.io java.lang java.net java.util javax.servlet javax.servlet.http org.apache.commons.chain org.apache.commons.chain.config org.apache.commons.chain.impl org.apache.commons.digester org.apache.commons.logging |

<a id="jdepend-report--org.apache.commons.chain.web.faces"></a>

### org.apache.commons.chain.web.faces

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 0 | 5 | 0.0% | 100.0% | 0.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| *None* | org.apache.commons.chain.web.faces.FacesGetLocaleCommand org.apache.commons.chain.web.faces.FacesSetLocaleCommand org.apache.commons.chain.web.faces.FacesWebContext | *None* | java.util javax.faces.component javax.faces.context org.apache.commons.chain org.apache.commons.chain.web |

<a id="jdepend-report--org.apache.commons.chain.web.portlet"></a>

### org.apache.commons.chain.web.portlet

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 0 | 5 | 0.0% | 100.0% | 0.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| *None* | org.apache.commons.chain.web.portlet.PortletApplicationScopeMap org.apache.commons.chain.web.portlet.PortletGetLocaleCommand org.apache.commons.chain.web.portlet.PortletInitParamMap org.apache.commons.chain.web.portlet.PortletParamMap org.apache.commons.chain.web.portlet.PortletParamValuesMap org.apache.commons.chain.web.portlet.PortletRequestScopeMap org.apache.commons.chain.web.portlet.PortletSessionScopeMap org.apache.commons.chain.web.portlet.PortletSetLocaleCommand org.apache.commons.chain.web.portlet.PortletWebContext | *None* | java.lang java.util javax.portlet org.apache.commons.chain org.apache.commons.chain.web |

<a id="jdepend-report--org.apache.commons.chain.web.servlet"></a>

### org.apache.commons.chain.web.servlet

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 0 | 8 | 0.0% | 100.0% | 0.0% |

| Abstract Classes | Concrete Classes | Used by Packages | Uses Packages |
| --- | --- | --- | --- |
| *None* | org.apache.commons.chain.web.servlet.ChainProcessor org.apache.commons.chain.web.servlet.PathInfoMapper org.apache.commons.chain.web.servlet.RequestParameterMapper org.apache.commons.chain.web.servlet.ServletApplicationScopeMap org.apache.commons.chain.web.servlet.ServletCookieMap org.apache.commons.chain.web.servlet.ServletGetLocaleCommand org.apache.commons.chain.web.servlet.ServletHeaderMap org.apache.commons.chain.web.servlet.ServletHeaderValuesMap org.apache.commons.chain.web.servlet.ServletInitParamMap org.apache.commons.chain.web.servlet.ServletParamMap org.apache.commons.chain.web.servlet.ServletParamValuesMap org.apache.commons.chain.web.servlet.ServletPathMapper org.apache.commons.chain.web.servlet.ServletRequestScopeMap org.apache.commons.chain.web.servlet.ServletSessionScopeMap org.apache.commons.chain.web.servlet.ServletSetLocaleCommand org.apache.commons.chain.web.servlet.ServletWebContext | *None* | java.io java.lang java.util javax.servlet javax.servlet.http org.apache.commons.chain org.apache.commons.chain.generic org.apache.commons.chain.web |

<a id="jdepend-report--cycles"></a>

## Cycles

[ [summary](#jdepend-report--summary) ] [ [packages](#jdepend-report--packages) ] [ [cycles](#jdepend-report--cycles) ] [ [explanations](#jdepend-report--explanations) ]

| Package | Package Dependencies |
| --- | --- |
| org.apache.commons.chain | org.apache.commons.chain.impl org.apache.commons.chain |
| org.apache.commons.chain.config | org.apache.commons.chain org.apache.commons.chain.impl org.apache.commons.chain |
| org.apache.commons.chain.generic | org.apache.commons.chain org.apache.commons.chain.impl org.apache.commons.chain |
| org.apache.commons.chain.impl | org.apache.commons.chain org.apache.commons.chain.impl |
| org.apache.commons.chain.web | org.apache.commons.chain org.apache.commons.chain.impl org.apache.commons.chain |
| org.apache.commons.chain.web.faces | org.apache.commons.chain.web org.apache.commons.chain org.apache.commons.chain.impl org.apache.commons.chain |
| org.apache.commons.chain.web.portlet | org.apache.commons.chain.web org.apache.commons.chain org.apache.commons.chain.impl org.apache.commons.chain |
| org.apache.commons.chain.web.servlet | org.apache.commons.chain.web org.apache.commons.chain org.apache.commons.chain.impl org.apache.commons.chain |

<a id="jdepend-report--explanation"></a>

## Explanation

[ [summary](#jdepend-report--summary) ] [ [packages](#jdepend-report--packages) ] [ [cycles](#jdepend-report--cycles) ] [ [explanations](#jdepend-report--explanations) ]
The following explanations are for quick reference and are lifted directly from the original JDepend documentation.

| Term | Description |
| --- | --- |
| Number of Classes | The number of concrete and abstract classes (and interfaces) in the package is an indicator of the extensibility of the package. |
| Afferent Couplings | The number of other packages that depend upon classes within the package is an indicator of the package's responsibility. |
| Efferent Couplings | The number of other packages that the classes in the package depend upon is an indicator of the package's independence. |
| Abstractness | The ratio of the number of abstract classes (and interfaces) in the analyzed package to the total number of classes in the analyzed package. The range for this metric is 0 to 1, with A=0 indicating a completely concrete package and A=1 indicating a completely abstract package. |
| Instability | The ratio of efferent coupling (Ce) to total coupling (Ce / (Ce + Ca)). This metric is an indicator of the package's resilience to change. The range for this metric is 0 to 1, with I=0 indicating a completely stable package and I=1 indicating a completely instable package. |
| Distance | The perpendicular distance of a package from the idealized line A + I = 1. This metric is an indicator of the package's balance between abstractness and stability. A package squarely on the main sequence is optimally balanced with respect to its abstractness and stability. Ideal packages are either completely abstract and stable (x=0, y=1) or completely concrete and instable (x=1, y=0). The range for this metric is 0 to 1, with D=0 indicating a package that is coincident with the main sequence and D=1 indicating a package that is as far from the main sequence as possible. |
| Cycles | Packages participating in a package dependency cycle are in a deadly embrace with respect to reusability and their release cycle. Package dependency cycles can be easily identified by reviewing the textual reports of dependency cycles. Once these dependency cycles have been identified with JDepend, they can be broken by employing various object-oriented techniques. |

---

<a id="rat-report"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/rat-report.html -->

<!-- page_index: 14 -->

<a id="rat-report--rat-release-audit-tool-results"></a>

## RAT (Release Audit Tool) results

The following document contains the results of [RAT (Release Audit Tool)](http://code.google.com/p/arat/).

```

*****************************************************
Summary
-------
Notes: 5
Binaries: 2
Archives: 0
Standards: 144

Apache Licensed: 143
Generated Documents: 0

JavaDocs are generated and so license header is optional
Generated files do not required license headers

1 Unknown Licenses

*******************************

Archives (+ indicates readable, $ unreadable): 

 
*****************************************************
  Files with AL headers will be marked L
  Binary files (which do not require AL headers) will be marked B
  Compressed archives will be marked A
  Notices, licenses etc will be marked N
  AL    apps/example1/pom.xml
  N     apps/example1/README.txt
  AL    apps/example1/src/main/java/org/apache/commons/chain/apps/example/CountCommand.java
  AL    apps/example1/src/main/java/org/apache/commons/chain/apps/example/ForwardCommand.java
  AL    apps/example1/src/main/webapp/index.jsp
  AL    apps/example1/src/main/webapp/pathinfo.jsp
  AL    apps/example1/src/main/webapp/reqparam.jsp
  AL    apps/example1/src/main/webapp/servletpath.jsp
  AL    apps/example1/src/main/webapp/WEB-INF/chain-config.xml
  AL    apps/example1/src/main/webapp/WEB-INF/classes/log4j.properties
  AL    apps/example1/src/main/webapp/WEB-INF/web.xml
  AL    apps/example2/pom.xml
  N     apps/example2/README.txt
  AL    apps/example2/src/main/java/org/apache/commons/chain/apps/example/CountCommand.java
  AL    apps/example2/src/main/java/org/apache/commons/chain/apps/example/ExampleServlet.java
  AL    apps/example2/src/main/java/org/apache/commons/chain/apps/example/ForwardCommand.java
  AL    apps/example2/src/main/webapp/index.jsp
  AL    apps/example2/src/main/webapp/pathinfo.jsp
  AL    apps/example2/src/main/webapp/reqparam.jsp
  AL    apps/example2/src/main/webapp/servletpath.jsp
  AL    apps/example2/src/main/webapp/WEB-INF/chain-config.xml
  AL    apps/example2/src/main/webapp/WEB-INF/classes/log4j.properties
  AL    apps/example2/src/main/webapp/WEB-INF/web.xml
  AL    build.properties.sample
  AL    build.xml
  AL    checkstyle.xml
  AL    doap_chain.rdf
  AL    license-header.txt
  N     LICENSE.txt
  N     NOTICE.txt
  AL    pom.xml
  AL    PROPOSAL.html
  N     RELEASE-NOTES.txt
  AL    sdocbook/chapter-chain.xml
  AL    src/assembly/bin.xml
  AL    src/assembly/src.xml
  AL    src/changes/changes.xml
 !????? src/conf/MANIFEST.MF
  AL    src/main/java/org/apache/commons/chain/Catalog.java
  AL    src/main/java/org/apache/commons/chain/CatalogFactory.java
  AL    src/main/java/org/apache/commons/chain/Chain.java
  AL    src/main/java/org/apache/commons/chain/Command.java
  AL    src/main/java/org/apache/commons/chain/config/ConfigCatalogRule.java
  AL    src/main/java/org/apache/commons/chain/config/ConfigDefineRule.java
  AL    src/main/java/org/apache/commons/chain/config/ConfigParser.java
  AL    src/main/java/org/apache/commons/chain/config/ConfigRegisterRule.java
  AL    src/main/java/org/apache/commons/chain/config/ConfigRuleSet.java
  AL    src/main/java/org/apache/commons/chain/config/package.html
  AL    src/main/java/org/apache/commons/chain/Context.java
  AL    src/main/java/org/apache/commons/chain/Filter.java
  AL    src/main/java/org/apache/commons/chain/generic/CopyCommand.java
  AL    src/main/java/org/apache/commons/chain/generic/DispatchCommand.java
  AL    src/main/java/org/apache/commons/chain/generic/DispatchLookupCommand.java
  AL    src/main/java/org/apache/commons/chain/generic/LookupCommand.java
  AL    src/main/java/org/apache/commons/chain/generic/package.html
  AL    src/main/java/org/apache/commons/chain/generic/RemoveCommand.java
  AL    src/main/java/org/apache/commons/chain/impl/CatalogBase.java
  AL    src/main/java/org/apache/commons/chain/impl/CatalogFactoryBase.java
  AL    src/main/java/org/apache/commons/chain/impl/ChainBase.java
  AL    src/main/java/org/apache/commons/chain/impl/ContextBase.java
  AL    src/main/java/org/apache/commons/chain/impl/package.html
  AL    src/main/java/org/apache/commons/chain/package.html
  AL    src/main/java/org/apache/commons/chain/web/AbstractGetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/AbstractSetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/ChainListener.java
  AL    src/main/java/org/apache/commons/chain/web/ChainResources.java
  AL    src/main/java/org/apache/commons/chain/web/ChainServlet.java
  AL    src/main/java/org/apache/commons/chain/web/faces/FacesGetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/faces/FacesSetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/faces/FacesWebContext.java
  AL    src/main/java/org/apache/commons/chain/web/faces/package.html
  AL    src/main/java/org/apache/commons/chain/web/MapEntry.java
  AL    src/main/java/org/apache/commons/chain/web/package.html
  AL    src/main/java/org/apache/commons/chain/web/portlet/package.html
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletApplicationScopeMap.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletGetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletInitParamMap.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletParamMap.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletParamValuesMap.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletRequestScopeMap.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletSessionScopeMap.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletSetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/portlet/PortletWebContext.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ChainProcessor.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/package.html
  AL    src/main/java/org/apache/commons/chain/web/servlet/PathInfoMapper.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/RequestParameterMapper.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletApplicationScopeMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletCookieMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletGetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletHeaderMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletHeaderValuesMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletInitParamMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletParamMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletParamValuesMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletPathMapper.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletRequestScopeMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletSessionScopeMap.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletSetLocaleCommand.java
  AL    src/main/java/org/apache/commons/chain/web/servlet/ServletWebContext.java
  AL    src/main/java/org/apache/commons/chain/web/WebContext.java
  AL    src/main/java/overview.html
  B     src/site/resources/images/chain-logo-white.png
  B     src/site/resources/images/chain-logo-white.xcf
  AL    src/site/site.xml
  AL    src/site/xdoc/building.xml
  AL    src/site/xdoc/cookbook.xml
  AL    src/site/xdoc/download_chain.xml
  AL    src/site/xdoc/index.xml
  AL    src/site/xdoc/issue-tracking.xml
  AL    src/site/xdoc/mail-lists.xml
  AL    src/test/java/org/apache/commons/chain/config/ConfigParser2TestCase.java
  AL    src/test/java/org/apache/commons/chain/config/ConfigParserTestCase.java
  AL    src/test/java/org/apache/commons/chain/config/test-config-2.xml
  AL    src/test/java/org/apache/commons/chain/config/test-config.xml
  AL    src/test/java/org/apache/commons/chain/config/TestChain.java
  AL    src/test/java/org/apache/commons/chain/config/TestCommand.java
  AL    src/test/java/org/apache/commons/chain/generic/DispatchCommandTestCase.java
  AL    src/test/java/org/apache/commons/chain/generic/DispatchLookupCommandTestCase.java
  AL    src/test/java/org/apache/commons/chain/generic/LookupCommandTestCase.java
  AL    src/test/java/org/apache/commons/chain/impl/AddingCommand.java
  AL    src/test/java/org/apache/commons/chain/impl/CatalogBaseTestCase.java
  AL    src/test/java/org/apache/commons/chain/impl/CatalogFactoryBaseTestCase.java
  AL    src/test/java/org/apache/commons/chain/impl/ChainBaseTestCase.java
  AL    src/test/java/org/apache/commons/chain/impl/ContextBaseTestCase.java
  AL    src/test/java/org/apache/commons/chain/impl/DelegatingCommand.java
  AL    src/test/java/org/apache/commons/chain/impl/DelegatingFilter.java
  AL    src/test/java/org/apache/commons/chain/impl/ExceptionCommand.java
  AL    src/test/java/org/apache/commons/chain/impl/ExceptionFilter.java
  AL    src/test/java/org/apache/commons/chain/impl/NonDelegatingCommand.java
  AL    src/test/java/org/apache/commons/chain/impl/NonDelegatingFilter.java
  AL    src/test/java/org/apache/commons/chain/impl/TestContext.java
  AL    src/test/java/org/apache/commons/chain/impl/TestContextTestCase.java
  AL    src/test/java/org/apache/commons/chain/web/ChainResourcesTestCase.java
  AL    src/test/java/org/apache/commons/chain/web/MockEnumeration.java
  AL    src/test/java/org/apache/commons/chain/web/MockPrincipal.java
  AL    src/test/java/org/apache/commons/chain/web/portlet/MockPortletContext.java
  AL    src/test/java/org/apache/commons/chain/web/portlet/MockPortletRequest.java
  AL    src/test/java/org/apache/commons/chain/web/portlet/MockPortletSession.java
  AL    src/test/java/org/apache/commons/chain/web/portlet/PortletGetLocaleCommandTestCase.java
  AL    src/test/java/org/apache/commons/chain/web/portlet/PortletWebContextTestCase.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/ChainProcessorTestCase.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/MockHttpServletRequest.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/MockHttpServletResponse.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/MockHttpSession.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/MockServletConfig.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/MockServletContext.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/ServletGetLocaleCommandTestCase.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/ServletSetLocaleCommandTestCase.java
  AL    src/test/java/org/apache/commons/chain/web/servlet/ServletWebContextTestCase.java
  AL    WHITEBOARD.html
 
 *****************************************************
 Printing headers for files without AL header...
 
 
 =======================================================================
 ==src/conf/MANIFEST.MF
 =======================================================================
 Extension-Name: @package@
Specification-Title: Jakarta Commons Chain
Specification-Vendor: Apache Software Foundation
Specification-Version: 1.0
Implementation-Title: org.apache.commons.chain
Implementation-Vendor: Apache Software Foundation
Implementation-Version: @version@
```

©
2003-2010
The Apache Software Foundation

---

<a id="surefire-report"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-chain/surefire-report.html -->

<!-- page_index: 15 -->

<a id="surefire-report--surefire-report"></a>

## Surefire Report

<a id="surefire-report--summary"></a>

## Summary

[[Summary](#surefire-report--summary)] [[Package List](#surefire-report--package_list)] [[Test Cases](#surefire-report--test_cases)]

| Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- |
| 116 | 0 | 0 | 0 | 100% | 7.499 |

Note: failures are anticipated and checked for with assertions while errors are unanticipated.

<a id="surefire-report--package-list"></a>

## Package List

[[Summary](#surefire-report--summary)] [[Package List](#surefire-report--package_list)] [[Test Cases](#surefire-report--test_cases)]

| Package | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.chain.web](#surefire-report--org.apache.commons.chain.web) | 1 | 0 | 0 | 0 | 100% | 0.031 |
| [org.apache.commons.chain.web.portlet](#surefire-report--org.apache.commons.chain.web.portlet) | 20 | 0 | 0 | 0 | 100% | 0.469 |
| [org.apache.commons.chain.generic](#surefire-report--org.apache.commons.chain.generic) | 11 | 0 | 0 | 0 | 100% | 0.156 |
| [org.apache.commons.chain.config](#surefire-report--org.apache.commons.chain.config) | 20 | 0 | 0 | 0 | 100% | 2.922 |
| [org.apache.commons.chain.web.servlet](#surefire-report--org.apache.commons.chain.web.servlet) | 23 | 0 | 0 | 0 | 100% | 1.937 |
| [org.apache.commons.chain.impl](#surefire-report--org.apache.commons.chain.impl) | 41 | 0 | 0 | 0 | 100% | 1.984 |

Note: package statistics are not computed recursively, they only sum up all of its testsuites numbers.

<a id="surefire-report--org.apache.commons.chain.web"></a>

### org.apache.commons.chain.web

|  | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [ChainResourcesTestCase](#surefire-report--org.apache.commons.chain.webchainresourcestestcase) | 1 | 0 | 0 | 0 | 100% | 0.031 |

<a id="surefire-report--org.apache.commons.chain.web.portlet"></a>

### org.apache.commons.chain.web.portlet

|  | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [PortletGetLocaleCommandTestCase](#surefire-report--org.apache.commons.chain.web.portletportletgetlocalecommandtestcase) | 2 | 0 | 0 | 0 | 100% | 0.203 |
|  | [PortletWebContextTestCase](#surefire-report--org.apache.commons.chain.web.portletportletwebcontexttestcase) | 18 | 0 | 0 | 0 | 100% | 0.266 |

<a id="surefire-report--org.apache.commons.chain.generic"></a>

### org.apache.commons.chain.generic

|  | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [DispatchCommandTestCase](#surefire-report--org.apache.commons.chain.genericdispatchcommandtestcase) | 3 | 0 | 0 | 0 | 100% | 0.062 |
|  | [DispatchLookupCommandTestCase](#surefire-report--org.apache.commons.chain.genericdispatchlookupcommandtestcase) | 3 | 0 | 0 | 0 | 100% | 0.047 |
|  | [LookupCommandTestCase](#surefire-report--org.apache.commons.chain.genericlookupcommandtestcase) | 5 | 0 | 0 | 0 | 100% | 0.047 |

<a id="surefire-report--org.apache.commons.chain.config"></a>

### org.apache.commons.chain.config

|  | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [ConfigParser2TestCase](#surefire-report--org.apache.commons.chain.configconfigparser2testcase) | 10 | 0 | 0 | 0 | 100% | 0.641 |
|  | [ConfigParserTestCase](#surefire-report--org.apache.commons.chain.configconfigparsertestcase) | 10 | 0 | 0 | 0 | 100% | 2.281 |
|  | [TestChain](#surefire-report--org.apache.commons.chain.configtestchain) | 0 | 0 | 0 | 0 | 0% | 0 |
|  | [TestCommand](#surefire-report--org.apache.commons.chain.configtestcommand) | 0 | 0 | 0 | 0 | 0% | 0 |

<a id="surefire-report--org.apache.commons.chain.web.servlet"></a>

### org.apache.commons.chain.web.servlet

|  | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [ChainProcessorTestCase](#surefire-report--org.apache.commons.chain.web.servletchainprocessortestcase) | 1 | 0 | 0 | 0 | 100% | 1.328 |
|  | [ServletGetLocaleCommandTestCase](#surefire-report--org.apache.commons.chain.web.servletservletgetlocalecommandtestcase) | 2 | 0 | 0 | 0 | 100% | 0.031 |
|  | [ServletGetLocaleCommandTestCase](#surefire-report--org.apache.commons.chain.web.servletservletgetlocalecommandtestcase) | 2 | 0 | 0 | 0 | 100% | 0 |
|  | [ServletWebContextTestCase](#surefire-report--org.apache.commons.chain.web.servletservletwebcontexttestcase) | 18 | 0 | 0 | 0 | 100% | 0.578 |

<a id="surefire-report--org.apache.commons.chain.impl"></a>

### org.apache.commons.chain.impl

|  | Class | Tests | Errors | Failures | Skipped | Success Rate | Time |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | [CatalogBaseTestCase](#surefire-report--org.apache.commons.chain.implcatalogbasetestcase) | 3 | 0 | 0 | 0 | 100% | 0.719 |
|  | [CatalogFactoryBaseTestCase](#surefire-report--org.apache.commons.chain.implcatalogfactorybasetestcase) | 4 | 0 | 0 | 0 | 100% | 0.016 |
|  | [ChainBaseTestCase](#surefire-report--org.apache.commons.chain.implchainbasetestcase) | 17 | 0 | 0 | 0 | 100% | 0.078 |
|  | [ContextBaseTestCase](#surefire-report--org.apache.commons.chain.implcontextbasetestcase) | 7 | 0 | 0 | 0 | 100% | 1.078 |
|  | [TestContext](#surefire-report--org.apache.commons.chain.impltestcontext) | 0 | 0 | 0 | 0 | 0% | 0.062 |
|  | [TestContextTestCase](#surefire-report--org.apache.commons.chain.impltestcontexttestcase) | 10 | 0 | 0 | 0 | 100% | 0.031 |

<a id="surefire-report--test-cases"></a>

## Test Cases

[[Summary](#surefire-report--summary)] [[Package List](#surefire-report--package_list)] [[Test Cases](#surefire-report--test_cases)]

<a id="surefire-report--configparser2testcase"></a>

### ConfigParser2TestCase

|  |  |  |
| --- | --- | --- |
|  | testDefaut | 0.062 |
|  | testExecute2a | 0.109 |
|  | testExecute2b | 0.063 |
|  | testExecute2c | 0.078 |
|  | testExecute2d | 0.063 |
|  | testExecute4a | 0.062 |
|  | testExecute4b | 0.063 |
|  | testExecute4c | 0.062 |
|  | testExecute4d | 0.047 |
|  | testPristine | 0 |

<a id="surefire-report--configparsertestcase"></a>

### ConfigParserTestCase

|  |  |  |
| --- | --- | --- |
|  | testDefaut | 1.25 |
|  | testExecute2a | 0.282 |
|  | testExecute2b | 0.062 |
|  | testExecute2c | 0.047 |
|  | testExecute2d | 0.219 |
|  | testExecute4a | 0.093 |
|  | testExecute4b | 0.079 |
|  | testExecute4c | 0.125 |
|  | testExecute4d | 0.109 |
|  | testPristine | 0 |

<a id="surefire-report--dispatchcommandtestcase"></a>

### DispatchCommandTestCase

|  |  |  |
| --- | --- | --- |
|  | testMethodDispatch | 0.016 |
|  | testMethodKeyDispatch | 0 |
|  | testAlternateContext | 0.015 |

<a id="surefire-report--dispatchlookupcommandtestcase"></a>

### DispatchLookupCommandTestCase

|  |  |  |
| --- | --- | --- |
|  | testExecuteDispatchLookup\_1a | 0.031 |
|  | testExecuteDispatchLookup\_2 | 0 |
|  | testExecuteDispatchLookup\_3 | 0 |

<a id="surefire-report--lookupcommandtestcase"></a>

### LookupCommandTestCase

|  |  |  |
| --- | --- | --- |
|  | testExecuteMethodLookup\_1a | 0 |
|  | testExecuteMethodLookup\_1b | 0 |
|  | testExecuteMethodLookup\_2a | 0 |
|  | testExecuteMethodLookup\_2b | 0 |
|  | testExecuteMethodLookup\_3a | 0 |

<a id="surefire-report--catalogbasetestcase"></a>

### CatalogBaseTestCase

|  |  |  |
| --- | --- | --- |
|  | testPristine | 0.203 |
|  | testAddCommand | 0.047 |
|  | testGetCommand | 0 |

<a id="surefire-report--catalogfactorybasetestcase"></a>

### CatalogFactoryBaseTestCase

|  |  |  |
| --- | --- | --- |
|  | testPristine | 0 |
|  | testDefaultCatalog | 0 |
|  | testSpecificCatalog | 0 |
|  | testCatalogIdentifier | 0 |

<a id="surefire-report--chainbasetestcase"></a>

### ChainBaseTestCase

|  |  |  |
| --- | --- | --- |
|  | testExecute2a | 0 |
|  | testExecute2b | 0 |
|  | testExecute2c | 0 |
|  | testExecute2d | 0 |
|  | testExecute4a | 0 |
|  | testExecute4b | 0.015 |
|  | testExecute4c | 0 |
|  | testExecute4d | 0 |
|  | testCommands | 0 |
|  | testExecute1a | 0 |
|  | testExecute1b | 0 |
|  | testExecute1c | 0 |
|  | testExecute1d | 0 |
|  | testExecute3a | 0 |
|  | testExecute3b | 0 |
|  | testExecute3c | 0 |
|  | testNewInstance | 0 |

<a id="surefire-report--contextbasetestcase"></a>

### ContextBaseTestCase

|  |  |  |
| --- | --- | --- |
|  | testPristine | 0 |
|  | testAttributes | 0 |
|  | testContains | 0 |
|  | testEquals | 0.078 |
|  | testKeySet | 0 |
|  | testPutAll | 0 |
|  | testSeriaization | 0.906 |

<a id="surefire-report--testcontexttestcase"></a>

### TestContextTestCase

|  |  |  |
| --- | --- | --- |
|  | testPristine | 0 |
|  | testReadOnly | 0 |
|  | testReadWrite | 0 |
|  | testWriteOnly | 0 |
|  | testAttributes | 0 |
|  | testContains | 0 |
|  | testEquals | 0 |
|  | testKeySet | 0 |
|  | testPutAll | 0 |
|  | testSeriaization | 0 |

<a id="surefire-report--chainresourcestestcase"></a>

### ChainResourcesTestCase

|  |  |  |
| --- | --- | --- |
|  | testGetPaths | 0 |

<a id="surefire-report--portletgetlocalecommandtestcase"></a>

### PortletGetLocaleCommandTestCase

|  |  |  |
| --- | --- | --- |
|  | testDefaut | 0.078 |
|  | testConfigured | 0 |

<a id="surefire-report--portletwebcontexttestcase"></a>

### PortletWebContextTestCase

|  |  |  |
| --- | --- | --- |
|  | testPristine | 0.14 |
|  | testEquals | 0 |
|  | testApplicationScope | 0.016 |
|  | testHeader | 0 |
|  | testHeaderValues | 0 |
|  | testInitParam | 0 |
|  | testParam | 0.031 |
|  | testParamValues | 0 |
|  | testCookies | 0 |
|  | testRelease | 0 |
|  | testRequestScope | 0 |
|  | testSessionScope | 0 |
|  | testSessionScopeWithoutSession | 0 |
|  | testAttributes | 0 |
|  | testContains | 0 |
|  | testKeySet | 0 |
|  | testPutAll | 0 |
|  | testSeriaization | 0 |

<a id="surefire-report--chainprocessortestcase"></a>

### ChainProcessorTestCase

|  |  |  |
| --- | --- | --- |
|  | testSerialize | 1.187 |

<a id="surefire-report--servletgetlocalecommandtestcase"></a>

### ServletGetLocaleCommandTestCase

|  |  |  |
| --- | --- | --- |
|  | testDefaut | 0 |
|  | testConfigured | 0 |

<a id="surefire-report--servletgetlocalecommandtestcase-2"></a>

### ServletGetLocaleCommandTestCase

|  |  |  |
| --- | --- | --- |
|  | testDefaut | 0 |
|  | testConfigured | 0 |

<a id="surefire-report--servletwebcontexttestcase"></a>

### ServletWebContextTestCase

|  |  |  |
| --- | --- | --- |
|  | testPristine | 0.329 |
|  | testEquals | 0.046 |
|  | testApplicationScope | 0 |
|  | testHeader | 0 |
|  | testHeaderValues | 0 |
|  | testInitParam | 0 |
|  | testParam | 0 |
|  | testParamValues | 0 |
|  | testCookies | 0 |
|  | testRelease | 0 |
|  | testRequestScope | 0 |
|  | testSessionScope | 0 |
|  | testSessionScopeWithoutSession | 0 |
|  | testAttributes | 0 |
|  | testContains | 0 |
|  | testKeySet | 0 |
|  | testPutAll | 0 |
|  | testSeriaization | 0 |

---
