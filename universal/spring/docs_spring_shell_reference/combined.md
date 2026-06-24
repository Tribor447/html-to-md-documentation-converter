# Spring Shell

## Navigation

- Overview
  
- [Overview](#index)
  
- [Getting Started](#getting-started)
  
- [Upgrading](#upgrading)
  
- [Basics](#basics)
    
- [Reading Docs](#basics-reading)
  
- [Commands](#commands)
    
- [Command Registration](#commands-registration)
    
- [Organizing Commands](#commands-organize)
    
- [Command Syntax](#commands-syntax)
    
- [Option Validation](#commands-validation)
    
- [Option Help](#commands-help)
    
- [Command Context](#commands-context)
    
- [Command Availability](#commands-availability)
    
- [Command Completion](#commands-completion)
    
- [Reading Input](#commands-reading)
    
- [Writing Output](#commands-writing)
    
- [Exception Handling](#commands-exception-handling)
    
- [Built-In Commands](#commands-builtin)
      
- [Help](#commands-builtin-help)
      
- [Clear](#commands-builtin-clear)
      
- [Exit](#commands-builtin-exit)
      
- [Version](#commands-builtin-version)
      
- [Script](#commands-builtin-script)
  
- [Building](#building)
  
- [Components](#components)
    
- [Flow](#components-flow)
    
- [Flow Components](#components-ui)
      
- [Component Render](#components-ui-render)
      
- [String Input](#components-ui-stringinput)
      
- [Number Input](#components-ui-numberinput)
      
- [Path Input](#components-ui-pathinput)
      
- [Path Search](#components-ui-pathsearch)
      
- [Confirmation](#components-ui-confirmation)
      
- [Single Select](#components-ui-singleselect)
      
- [Multi Select](#components-ui-multiselect)
  
- [Terminal UI](#tui)
    
- [Introduction](#tui-intro)
      
- [TerminalUI](#tui-intro-terminalui)
    
- [Views](#tui-views)
      
- [AppView](#tui-views-app)
      
- [BoxView](#tui-views-box)
      
- [ButtonView](#tui-views-button)
      
- [DialogView](#tui-views-dialog)
      
- [GridView](#tui-views-grid)
      
- [InputView](#tui-views-input)
      
- [ListView](#tui-views-list)
      
- [MenuView](#tui-views-menu)
      
- [MenuBarView](#tui-views-menubar)
      
- [ProgressView](#tui-views-progress)
      
- [StatusBarView](#tui-views-statusbar)
    
- [Events](#tui-events)
      
- [EventLoop](#tui-events-eventloop)
      
- [Key Handling](#tui-events-key)
      
- [Mouse Handling](#tui-events-mouse)
  
- [Customization](#customization)
    
- [Theming](#customization-styling)
    
- [Context Close](#customization-contextclose)
    
- [Custom Prompt](#customization-custom-prompt)
  
- [Execution](#execution)
  
- [Testing](#testing)
  - Appendices
    
- [Technical Introduction](#appendices-techintro)
      
- [Command Parser](#appendices-techintro-parser)
      
- [Command Execution](#appendices-techintro-execution)
      
- [Theming](#appendices-techintro-theming)
      
- [Search Algorithms](#appendices-techintro-searchalgorithm)
    
- [Debugging](#appendices-debugging)
    
- [Terminal UI](#appendices-tui)
      
- [View Development](#appendices-tui-viewdev)
  
- [Javadoc](#api)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/index.html -->

<!-- page_index: 1 -->

# Spring Shell

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="index--page-title"></a>
<a id="index--spring-shell"></a>

# Spring Shell

**4.0.2**

Not all applications need a fancy web user interface. Sometimes, interacting with an application through an interactive terminal is the most appropriate way to get things done.

Spring Shell lets you create such a runnable application, where the user enters textual commands that are run until the program terminates. The Spring Shell project provides the infrastructure to create such a REPL (Read, Eval, Print Loop) application, letting you concentrate on implementing commands by using the familiar Spring programming model.

Spring Shell includes advanced features (such as parsing, tab completion, colorization of output, fancy ASCII-art table display, input conversion, and validation), freeing you to focus on core command logic.

[Getting Started](#getting-started)

---

<a id="getting-started"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/getting-started.html -->

<!-- page_index: 2 -->

# Getting Started

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="getting-started--page-title"></a>
<a id="getting-started--getting-started"></a>

# Getting Started

To see what Spring Shell has to offer, we will write a trivial *hello world*
shell application that has a simple command.

<a id="getting-started--creating-a-project"></a>

## Creating a Project

For the purpose of this quick tutorial, clone and build the project with the following commands:

```shell
$>git clone [email protected]:spring-projects/spring-shell.git
$>cd spring-shell
$>./mvnw install -DskipTests
```

<a id="getting-started--using-spring-shell-your-first-command"></a>
<a id="getting-started--your-first-command"></a>

## Your First Command

In your favorite IDE, open the `org.springframework.shell.samples.helloworld.SpringShellApplication`:

```java
@EnableCommand(SpringShellApplication.class) public class SpringShellApplication {
public static void main(String[] args) throws Exception {ApplicationContext context = new AnnotationConfigApplicationContext(SpringShellApplication.class); ShellRunner runner = context.getBean(ShellRunner.class); runner.run(args);}
@Command(name = "hello", description = "Say hello to a given name", group = "Greetings",help = "A command that greets the user with 'Hello ${name}!'. Usage: hello [-n | --name]=<name>") public void sayHello(@Option(shortName = 'n', longName = "name", description = "the name of the person to greet",defaultValue = "World") String name) {System.out.println("Hello " + name + "!");}
}
```

This class defines a single command named `hello`, that takes an optional argument, `name`, and prints a greeting message to the standard output.

The main method bootstraps a Spring application context and runs the shell. To run the application, execute the `SpringShellApplication` class with the following command:

```shell
./mvnw -pl org.springframework.shell:spring-shell-sample-hello-world exec:java -Dexec.mainClass=org.springframework.shell.samples.helloworld.SpringShellApplication
```

This will start the shell, and you should see a prompt and be able to type commands like this:

```text
$>help
Available commands:
Built-In Commands
	clear: Clear the terminal screen
	help: Display help about available commands
	version: Show version info
Greetings
	hello: Say hello to a given name

$>hello --name=foo
Hello foo!
$>exit
Exiting the shell
```

Congratulations, you have created and run your first Spring Shell application!

<a id="getting-started--next-steps"></a>

## Next Steps

The rest of this document delves deeper into the whole Spring Shell programming model.

[Overview](#index)
[Upgrading](#upgrading)

---

<a id="upgrading"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/upgrading.html -->

<!-- page_index: 3 -->

<a id="upgrading--page-title"></a>
<a id="upgrading--upgrading"></a>

# Upgrading

Instructions for how to upgrade from earlier versions of Spring Shell are
provided on the project [wiki](https://github.com/spring-projects/spring-shell/wiki).
Follow the links in the release notes section.

[Getting Started](#getting-started)
[Basics](#basics)

---

<a id="basics"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/basics/index.html -->

<!-- page_index: 4 -->

# Basics

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="basics--page-title"></a>
<a id="basics--basics"></a>

# Basics

This section covers the basics of Spring Shell. Before going on to define actual commands and options, we need to go through some of the fundamental concepts of Spring Shell.

Essentially, a few things needs to happen before you have a working Spring Shell application:

- Create a Spring (Boot) application.
- Define commands and options.
- Package the application.
- Run the application, either interactively or non-interactively.

You can get a fully working Spring Shell application without defining any user-level commands
as some basic built-in commands (such as `help` and `clear`) are provided.

<a id="basics--section-summary"></a>

## Section Summary

- [Reading Docs](#basics-reading)

[Upgrading](#upgrading)
[Reading Docs](#basics-reading)

---

<a id="basics-reading"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/basics/reading.html -->

<!-- page_index: 5 -->

<a id="basics-reading--page-title"></a>
<a id="basics-reading--reading-docs"></a>

# Reading Docs

Throughout this documentation, we make references to configuring something by using
annotations or programmatic examples.

The annotation model relates to the use of `@Command` annotation. The programmatic model relates to creating commands using APIs such as `Command.Builder`.

These two approaches can be mixed in the same application.

[Basics](#basics)
[Commands](#commands)

---

<a id="commands"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/index.html -->

<!-- page_index: 6 -->

# Commands

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands--page-title"></a>
<a id="commands--commands"></a>

# Commands

In this section, we go through the actual command definition and parsing rules.

<a id="commands--section-summary"></a>

## Section Summary

- [Command Registration](#commands-registration)
- [Organizing Commands](#commands-organize)
- [Command Syntax](#commands-syntax)
- [Option Validation](#commands-validation)
- [Option Help](#commands-help)
- [Command Context](#commands-context)
- [Command Availability](#commands-availability)
- [Command Completion](#commands-completion)
- [Reading Input](#commands-reading)
- [Writing Output](#commands-writing)
- [Exception Handling](#commands-exception-handling)
- [Built-In Commands](#commands-builtin)

[Reading Docs](#basics-reading)
[Command Registration](#commands-registration)

---

<a id="commands-registration"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/registration.html -->

<!-- page_index: 7 -->

# Command Registration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-registration--page-title"></a>
<a id="commands-registration--command-registration"></a>

# Command Registration

There are two different ways to define a command, through an annotation model and through a programmatic model:

- In the annotation model, you define your methods in a `@Component` class and the methods with specific annotations.
- In the programmatic model, you use a more low level approach, defining commands as beans.

> [!IMPORTANT]
> With the annotation model, the class containing command definitions should **not** be excluded from component scanning, otherwise the commands will not be registered. This is a common mistake when using `@ComponentScan` with `excludeFilters` and excluding the package containing command classes.

<a id="commands-registration--commands-registration-annotation"></a>
<a id="commands-registration--annotation-based-registration"></a>

## Annotation-Based Registration

The `@Command` annotation marks a method as a candidate for command registration.
In below example a command `example` is defined.

```java
@Component class MyCommands {
@Command(name = "example") public String example() {return "Hello";}
}
```

> [!TIP]
> The command name optional, if not provided the method name will be used as command name.
> When the command returns a value, it will be printed to the shell output.

Using a `@Command` will not automatically register command targets, instead it is required to use
`@EnableCommand` annotations. This model is familiar from other parts of Spring umbrella and
provides better flexibility for a user being inclusive rather than exclusive for command targets.

You can define target classes using `@EnableCommand`. It will get picked from all *Configuration*
classes.

```java
@EnableCommand({ MyCommands.class })
class App {

}
```

> [!TIP]
> `@EnableCommand` is not required in a Spring Boot application, as Spring Boot auto-configuration
> will take care of that.

<a id="commands-registration--commands-registration-programmatic"></a>
<a id="commands-registration--programmatic-registration"></a>

## Programmatic Registration

In the programmatic model, commands can be defined as beans of type `Command`:

```java
@Bean
Command myCommand() {
	return Command.builder().name("mycommand").execute(context -> {
		context.outputWriter().println("This is my command!");
	});
}
```

You can also use the `AbstractCommand` class to simplify command definitions:

```java
@Bean Command myCommand() {return new AbstractCommand("mycommand", "This is my command") {@Override public ExitStatus doExecute(CommandContext commandContext) {println("This is my command!", commandContext); return ExitStatus.OK;} };}
```

`AbstractCommand` provides some utility methods to simplify command creation like
handling help options (`-h` and `--help`) and printing messages to the shell output.

<a id="commands-registration--command-registry"></a>

## Command Registry

The `CommandRegistry` interface holds the set of commands known to the Shell application.
It is possible to dynamically register and unregister commands.

By default, Spring Shell will populate the `CommandRegistry` with commands defined in the
application context.

[Commands](#commands)
[Organizing Commands](#commands-organize)

---

<a id="commands-organize"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/organize.html -->

<!-- page_index: 8 -->

# Organizing Commands

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-organize--page-title"></a>
<a id="commands-organize--organizing-commands"></a>

# Organizing Commands

When your shell starts to provide a lot of functionality, you may end up
with a lot of commands, which could be confusing for your users. By typing `help`, they would see a daunting list of commands, organized in alphabetical order, which may not always be the best way to show the available commands.

To alleviate this possible confusion, Spring Shell provides the ability to group commands together, with reasonable defaults. Related commands would then end up in the same group (for example, `User Management Commands`)
and be displayed together in the help screen and other places.

Commands can be grouped by specifying a `group` attribute in the `@Command` annotation:

```java
@Command(name = "example", group = "My Commands")
public String example() {
    return "Hello";
}
```

The group can also be specified programmatically when using the programmatic registration model
using the `Command.Builder.group(String)` method:

```java
@Bean Command myCommand() {return Command.builder() .name("mycommand") .group("My Commands") .execute(context -> {System.out.println("This is my command!"); });}
```

Typically, related commands are defined in the same class (to easily share state between commands), and the group name and prefix are specified at the class level, which means that all commands defined in that class will belong to the same group. Here is an example of how to do that:

```java
@CommandGroup(name = "Authentication Commands", prefix = "auth")
public class AuthenticationCommands {

	private boolean authenticated = false;

	@Command(name = "login", description = "Log in to the system")
	public void login() {
        // Authentication logic here
        authenticated = true;
        System.out.println("Logged in successfully!");
    }

    @Command(name = "logout", description = "Log out of the system")
    public void logout() {
        // Logout logic here
        authenticated = false;
        System.out.println("Logged out successfully!");
    }
}
```

In this example, both the `login` and `logout` commands belong to the `Authentication Commands` group, and they will be displayed together in the help screen under that group. The `prefix` attribute specifies a common prefix for all commands in that group, which can be used to invoke the commands (e.g., `auth login` and `auth logout`).

> [!NOTE]
> If a command provides a `group` attribute, it will take precedence over the group specified at the class level. This allows you to override the group for specific commands if needed.

[Command Registration](#commands-registration)
[Command Syntax](#commands-syntax)

---

<a id="commands-syntax"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/syntax.html -->

<!-- page_index: 9 -->

# Command Syntax

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-syntax--page-title"></a>
<a id="commands-syntax--command-syntax"></a>

# Command Syntax

<a id="commands-syntax--_options_and_arguments"></a>
<a id="commands-syntax--options-and-arguments"></a>

## Options and arguments

Command options and arguments can be defined using method parameters:

```java
@Component
class GreetingCommands {

	@Command(name = "hi", description = "Say hi to a given name", group = "greetings",
			help = "A command that greets the user with 'Hi ${name}!' with a configurable suffix. Example usage: hi -s=! John")
	public void sayHi(
			@Argument(index = 0, description = "the name of the person to greet",
					defaultValue = "world") String name,
			@Option(shortName = 's', longName = "suffix", description = "the suffix of the greeting message",
					defaultValue = "!") String suffix) {
		System.out.println("Hi " + name + suffix);
	}

}
```

Options are defined using `@Option` annotation, while arguments are defined using `@Argument` annotation.
Options are named, while arguments are positional. Options can have short names (single character) and long names (multi-character).

Options can be validated using the Bean Validation API by adding validation annotations to the method parameters, see the [Validating Command Options](#commands-validation) section for more details.

Multi-valued arguments can be defined by using the `@Arguments` annotation on an array or a collection type (e.g., `List`, `Set`) as the method parameter type. In this case, all the remaining command line tokens will be collected into the collection:

```java
@Component
class ArgumentsCommands {

	@Command(name = "hi", description = "Say hi to given names", group = "greetings",
			help = "A command that greets users with a configurable suffix. Example usage: hi -s=! Foo Bar")
	public void sayHi(@Option(shortName = 's', longName = "suffix",
			description = "the suffix of the greeting message", defaultValue = "!") String suffix,
			@Arguments String[] names) {
		System.out.println("Hi " + String.join(", ", names) + suffix);
	}

}
```

The `@Arguments` annotation provides an attribute called `arity` that allows you to specify the number of arguments to be collected into the collection.
By default, the arity is not bound, which means that all remaining tokens will be collected. If you set the arity to a specific number, only that many tokens will be collected, and the rest will be treated as separate arguments or options.
Here is an example of using the `arity` attribute:

```java
@Component class ArgumentsWithArityCommands {
/** * Real part of (a + bi)(c + di) = ac − bd.*/ @Command(name = "real-part", description = "Calculate the real part of the product of two complex numbers",group = "math",help = "Calculate the real part of the product of two complex numbers. Example usage: real-part 1 2 3 4") public double realPartOfComplexProduct(@Arguments(arity = 2) double[] realParts,@Arguments(arity = 2) double[] imaginaryParts) {return realParts[0] * realParts[1] - imaginaryParts[0] * imaginaryParts[1];}
}
```

<a id="commands-syntax--_parsing_rules"></a>
<a id="commands-syntax--parsing-rules"></a>

## Parsing rules

Spring Shell follows the same parsing rules as Spring Boot, with enhanced capabilities following the POSIX style.
Options can be specified in the long form of `--key=value` or `--key value` as well in the short form of `-k=value` or `-k value`.
Options and arguments can be specified in any order. Arguments are 0-based indexed among other arguments:

```shell
CommandSyntax  ::= CommandName [SubCommandName]* [Option | Argument]*
CommandName    ::= String
SubCommandName ::= String
Option         ::= ShortOption | LongOption
ShortOption    ::= '-' Char ['='|' ']? String
LongOption     ::= '--' String ['='|' ']? String
Argument       ::= String
```

For example:

```shell
$>mycommand mysubcommand --optionA=value1 arg1 -b=value2 arg2 --optionC value3 -d value4
```

> [!IMPORTANT]
> When an option is specified, it is always expected to have a value for that option, even if it is a boolean one. This is necessary to be able to distinguish option values from arguments. Moreover, short options cannot be grouped (e.g., `-abc` is not supported).

> [!TIP]
> To avoid ambiguity, named options should be preferred over positional arguments whenever possible, especially when subcommands are involved (see [Command Line Interface Guidelines](https://clig.dev/#arguments-and-flags)).

<a id="commands-syntax--_customizing_parsing_rules"></a>
<a id="commands-syntax--customizing-parsing-rules"></a>

## Customizing parsing rules

Spring Shell 4 provides a new API called `CommandParser` that allows you to customize the command parsing rules.
If the default parsing rules do not fit your needs, you can implement your own parser by implementing the `CommandParser` interface.
Once the custom parser is implemented, you can register it as a bean in the application context, and Spring Shell will use it for parsing commands.

[Organizing Commands](#commands-organize)
[Option Validation](#commands-validation)

---

<a id="commands-validation"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/validation.html -->

<!-- page_index: 10 -->

# Option Validation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-validation--page-title"></a>
<a id="commands-validation--option-validation"></a>

# Option Validation

Spring Shell integrates with the [Bean Validation API](https://beanvalidation.org/) to support
automatic and self-documenting constraints on command parameters.

Annotations found on command parameters are honored and trigger validation prior to the command executing.
Consider the following command:

```java
@Command(name = "change-password", description = "Change password", group = "User Management",
		help = "A command that changes the user password. Usage: change-password [-p | --password]=<password>")
public String changePassword(
		@Option(shortName = 'p', longName = "password") @Size(min = 8, max = 40) String password) {
	return "Password successfully set to " + password;
}
```

From the preceding example, you get the following behavior for free:

```bash
$>change-password --password=hello
The following constraints were not met:
	--password: size must be between 8 and 40
Error while executing command change-password: USAGE_ERROR
```

[Command Syntax](#commands-syntax)
[Option Help](#commands-help)

---

<a id="commands-help"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/help.html -->

<!-- page_index: 11 -->

<a id="commands-help--page-title"></a>
<a id="commands-help--option-help"></a>

# Option Help

It’s common in many CLI frameworks for every command having options *--help* and *-h*
to print out command help. *Spring Shell* has a built-in `help` command.

Extensions of `AbstractCommand` will get help functionality (ie handling options
*--help* and *-h*), which if present in a given command will automatically
short circuit command execution into an existing `help` command regardless
what other command-line options are typed.

[Option Validation](#commands-validation)
[Command Context](#commands-context)

---

<a id="commands-context"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/context.html -->

<!-- page_index: 12 -->

# Command Context

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-context--page-title"></a>
<a id="commands-context--command-context"></a>

# Command Context

The `CommandContext` interface gives you access to the context of the currently running
command. It provides access to the parsed command input, command registry, and
other useful information.

```java
@Command(name = "hello")
public void sayHello(CommandContext commandContext) {
	// use command context to get options, arguments and output writer
}
```

If you need to read input from the shell, you can get the `InputReader` from the
`CommandContext` and use it to read input. You can find more details about reading
from a shell in the [Reading Input](#commands-reading) section.

If you need to print something into a shell, you can get a `PrintWriter` from
the `CommandContext` and use it to print text. You can find more details about
writing into a shell in the [Writing Output](#commands-writing) section.

[Option Help](#commands-help)
[Command Availability](#commands-availability)

---

<a id="commands-availability"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/availability.html -->

<!-- page_index: 13 -->

# Command Availability

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-availability--page-title"></a>
<a id="commands-availability--command-availability"></a>

# Command Availability

Registered commands do not always make sense, due to the internal state of the application.
For example, there may be a `download` command, but it only works once the user has used `connect` on a remote
server. Now, if the user tries to use the `download` command, the shell should explain that
the command exists but that it is not available at the time.
Spring Shell lets you do that, even letting you provide a short explanation of the reason for
the command not being available.

<a id="commands-availability--_programmatic"></a>
<a id="commands-availability--programmatic"></a>

## Programmatic

With programmatic registration you can use the `availabilityProvider` method which takes
an `AvailabilityProvider`.

```java
private boolean connected;
@Bean public AbstractCommand connect() {return org.springframework.shell.core.command.Command.builder().name("connect").execute(ctx -> {CommandOption connectedOption = ctx.getOptionByName("connected"); this.connected = Boolean.parseBoolean(connectedOption.value()); });}
@Bean public AbstractCommand download() {return org.springframework.shell.core.command.Command.builder() .name("download") .availabilityProvider(() -> connected ? Availability.available() : Availability.unavailable("you are not connected")) .execute(ctx -> {// do something });}
```

<a id="commands-availability--_annotation"></a>
<a id="commands-availability--annotation"></a>

## Annotation

With annotation based commands you can use the `availabilityProvider` attribute to specify
the name of the `AvailabilityProvider` bean to use.

```java
@Component class MyCommands {
private boolean connected;
@Command(name = "connect") public void connect(String user, String password) {connected = true;}
@Command(name = "download", availabilityProvider = "downloadAvailability") public void download() {// do something}
@Bean public AvailabilityProvider downloadAvailability() {return () -> connected ? Availability.available() : Availability.unavailable("you are not connected");}
}
```

The `connect` method is used to connect to the server (details omitted), altering the state
of the command through the `connected` boolean when done.
The `download` command will be unavailable until the user has connected.
The availability provider returns an instance of `Availability`, constructed with one of the two factory methods.
If the command is not available, an explanation has to be provided.
Now, if the user tries to invoke the command while not being connected, here is what happens:

```none
shell:>download
Command 'download' exists but is not currently available because you are not connected.
```

> [!TIP]
> The reason provided when the command is not available should read nicely if appended after “because”.
> You should not start the sentence with a capital or add a final period

> [!TIP]
> Spring Shell does not impose many constraints on how to write commands and how to organize classes.
> However, it is often good practice to put related commands in the same class, and the availability indicators
> can benefit from that.

[Command Context](#commands-context)
[Command Completion](#commands-completion)

---

<a id="commands-completion"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/completion.html -->

<!-- page_index: 14 -->

# Command Completion

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-completion--page-title"></a>
<a id="commands-completion--command-completion"></a>

# Command Completion

Spring Shell provides a powerful command completion mechanism that helps users
discover available commands and their options. Command completion is available
with the JLine-based Shell and can be triggered by pressing the `Tab` key while
typing a command.

By default, command completion suggests available commands and options based on
the current input. However, you can also customize the completion behavior for
your own commands by implementing the `CompletionProvider` interface.
This interface allows you to define how completion suggestions are generated based
on the current input.

Spring Shell provides several built-in completion providers, such as:

- `FileNameCompletionProvider`: Suggests file and directory names based on the current directory.
- `EnumCompletionProvider`: Suggests values from a specified enum type.
- `CompositeCompletionProvider`: Combines multiple completion providers into one.

To use a custom completion provider, you need to declare it as a bean and set it on your command
method with the `completionProvider` attribute of the `@Command` annotation. For example:

```java
public enum Gender {
	MALE, FEMALE
}

@Command(name = "hello", description = "Say hello to a given name", group = "Greetings",
		help = "A command that greets the user with 'Hello [Mr.|Ms.] ${name}!'. Usage: hello [-n | --name]=<name> [-g | --gender]=<gender>",
		completionProvider = "helloCompletionProvider")
public void sayHello(
		@Option(shortName = 'n', longName = "name", description = "the name of the person to greet", defaultValue = "World") String name,
		@Option(shortName = 'g', longName = "gender", description = "the gender of the person to greet") Gender gender) {
	String prefix = switch (gender) {
		case MALE -> "Mr. ";
		case FEMALE -> "Ms. ";
	};
	System.out.println("Hello " + prefix + name + "!");
}

@Bean
public CompletionProvider helloCompletionProvider() {
	EnumCompletionProvider genderCompletionProvider = new EnumCompletionProvider(Gender.class, "--gender");
	CompletionProvider nameCompletionProvider = completionContext -> List.of(new CompletionProposal("--name=Bob"), new CompletionProposal("--name=Alice"));
	return new CompositeCompletionProvider(nameCompletionProvider, genderCompletionProvider);
}
```

With the programmatic approach, you can set the completion provider on the command using the `Command.Builder.completionProvider` API.

[Command Availability](#commands-availability)
[Reading Input](#commands-reading)

---

<a id="commands-reading"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/reading.html -->

<!-- page_index: 15 -->

<a id="commands-reading--page-title"></a>
<a id="commands-reading--reading-input"></a>

# Reading Input

When you need to read input from the shell in your command implementation, you can do it
by using the `InputReader` obtained from the command context:

```java
@Command
public void example(CommandContext ctx) throws Exception {
	String name = ctx.inputReader().readInput("Enter your name: ");
	char[] chars = ctx.inputReader().readPassword("Enter new password: ");
	// do something with name and password
}
```

[Command Completion](#commands-completion)
[Writing Output](#commands-writing)

---

<a id="commands-writing"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/writing.html -->

<!-- page_index: 16 -->

<a id="commands-writing--page-title"></a>
<a id="commands-writing--writing-output"></a>

# Writing Output

When something needs to get written into your console you can always
use JDK’s `System.out` which then goes directly into JDK’s own streams.
The recommended way is to use `PrintWriter` obtained from command context
and use it for writing:

```java
@Command
public void example(CommandContext ctx) {
	ctx.outputWriter().println("hi");
	ctx.outputWriter().flush();
}
```

[Reading Input](#commands-reading)
[Exception Handling](#commands-exception-handling)

---

<a id="commands-exception-handling"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/exception-handling.html -->

<!-- page_index: 17 -->

# Exception Handling

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-exception-handling--page-title"></a>
<a id="commands-exception-handling--exception-handling"></a>

# Exception Handling

When writing commands, it is important to handle exceptions properly to ensure that your application behaves predictably in the face of errors.
Spring Shell allows you to manage exceptions effectively and map them to specific exit codes and user-friendly messages thanks to the `ExitStatusExceptionMapper` interface.

The `ExitStatusExceptionMapper` interface provides a way to map exceptions thrown during command execution to specific exit codes and messages.
By implementing this interface, you can define custom behavior for different types of exceptions, allowing you to provide meaningful feedback to users and control the exit status of your application.

<a id="commands-exception-handling--_implementing_exitstatusexceptionmapper"></a>
<a id="commands-exception-handling--implementing-exitstatusexceptionmapper"></a>

## Implementing ExitStatusExceptionMapper

The `ExitStatusExceptionMapper` is a functional interface that extends `java.util.Function`, and which takes an `Exception` as input and returns an `ExitStatus`.
You can implement this method to handle specific exceptions and return appropriate exit codes and messages. For example:

```java
@Bean
public ExitStatusExceptionMapper myCustomExceptionMapper() {
	return exception -> new ExitStatus(42, "42! The answer to life, the universe and everything!");
}
```

<a id="commands-exception-handling--_registering_the_mapper"></a>
<a id="commands-exception-handling--registering-the-mapper"></a>

## Registering the Mapper

<a id="commands-exception-handling--_programmatic_registration"></a>
<a id="commands-exception-handling--programmatic-registration"></a>

### Programmatic Registration

When registering commands programmatically, you can set the `ExitStatusExceptionMapper` using the `exitStatusExceptionMapper` method on the `Command.Builder`. For example:

```java
@Bean
public Command sayHello() {
	return Command.builder()
			.name("hello")
			.description("Say hello to a given name")
			.group("Greetings")
			.help("A command that greets the user with 'Hello ${name}!'. Usage: hello [-n | --name]=<name>")
			.exitStatusExceptionMapper(exception -> new ExitStatus(42, "42! The answer to life, the universe and everything!"))
			.execute(context -> {
				String name = context.getOptionByName("name").value();
				if (name.equals("42")) {
					throw new RuntimeException("Error!");
				}
				System.out.println("Hello " + name + "!");
			});
}
```

<a id="commands-exception-handling--_annotation_based_registration"></a>
<a id="commands-exception-handling--annotation-based-registration"></a>

### Annotation-Based Registration

When using annotation-based command registration, you can specify the custom `ExitStatusExceptionMapper` by using the `exitStatusExceptionMapper` attribute of the `@Command` annotation. For example:

```java
@Command(name = "hello", description = "Say hello to a given name", group = "Greetings",help = "A command that greets the user with 'Hello ${name}!'. Usage: hello [-n | --name]=<name>",exitStatusExceptionMapper = "myCustomExceptionMapper") public void sayHello(@Option(shortName = 'n', longName = "name", description = "the name of the person to greet",defaultValue = "World") String name) {if (name.equals("42")) {throw new RuntimeException("Error!");} System.out.println("Hello " + name + "!");}
@Bean public ExitStatusExceptionMapper myCustomExceptionMapper() {return exception -> new ExitStatus(42, "42! The answer to life, the universe and everything!");}
```

The custom mapper should be defined as a Spring bean so that it can be referenced by name in the `@Command` annotation.

[Writing Output](#commands-writing)
[Built-In Commands](#commands-builtin)

---

<a id="commands-builtin"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/builtin/index.html -->

<!-- page_index: 18 -->

# Built-In Commands

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-builtin--page-title"></a>
<a id="commands-builtin--built-in-commands"></a>

# Built-In Commands

<a id="commands-builtin--section-summary"></a>

## Section Summary

- [Help](#commands-builtin-help)
- [Clear](#commands-builtin-clear)
- [Exit](#commands-builtin-exit)
- [Version](#commands-builtin-version)
- [Script](#commands-builtin-script)

[Exception Handling](#commands-exception-handling)
[Help](#commands-builtin-help)

---

<a id="commands-builtin-help"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/builtin/help.html -->

<!-- page_index: 19 -->

# Help

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-builtin-help--page-title"></a>
<a id="commands-builtin-help--help"></a>

# Help

Running a shell application often implies that the user is in a graphically limited
environment. This is why it is important that the shell commands are correctly self-documented, and this is where the `help`
command comes in.

Typing `help` + `ENTER` lists all the commands known to the shell and a short description of what they do, similar to the following:

```bash
my-shell:>help
Available commands:

Built-In Commands
       clear: Clear the terminal screen
	   help: Show help about available commands
       version: Show version info
```

Typing `<command> -h` or `<command> --help` shows the short help string for the given command. For more details about a command, like available parameters, their
type, whether they are mandatory or not, use the `help <command>` syntax:

```bash
my-shell:>help version
NAME
	version - Show version info

SYNOPSIS
	version  --help

OPTIONS
	--help or -h
	help for version
	[Optional]
```

[Built-In Commands](#commands-builtin)
[Clear](#commands-builtin-clear)

---

<a id="commands-builtin-clear"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/builtin/clear.html -->

<!-- page_index: 20 -->

<a id="commands-builtin-clear--page-title"></a>
<a id="commands-builtin-clear--clear"></a>

# Clear

The `clear` command clears the screen, resetting the prompt
in the top left corner.

[Help](#commands-builtin-help)
[Exit](#commands-builtin-exit)

---

<a id="commands-builtin-exit"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/builtin/exit.html -->

<!-- page_index: 21 -->

<a id="commands-builtin-exit--page-title"></a>
<a id="commands-builtin-exit--exit"></a>

# Exit

The `quit` command (also aliased as `exit`) requests the shell to quit, gracefully
closing the Spring application context. If not overridden, a JLine `History` bean writes a history of all
commands to disk, so that they are available again on the next launch.

[Clear](#commands-builtin-clear)
[Version](#commands-builtin-version)

---

<a id="commands-builtin-version"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/builtin/version.html -->

<!-- page_index: 22 -->

<a id="commands-builtin-version--page-title"></a>
<a id="commands-builtin-version--version"></a>

# Version

The `version` command shows the current version of Spring Shell being used.

[Exit](#commands-builtin-exit)
[Script](#commands-builtin-script)

---

<a id="commands-builtin-script"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/commands/builtin/script.html -->

<!-- page_index: 23 -->

# Script

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="commands-builtin-script--page-title"></a>
<a id="commands-builtin-script--script"></a>

# Script

The `script` command allows you to execute a series of commands from a specified script file. This is useful for automating repetitive tasks or setting up an environment quickly.

This command expects a file absolute path as an option, which points to the script file containing the commands to be executed. For example:

```shell
$>script --file /absolute/path/to/your/script.txt
```

The script file should contain one command per line, and the commands will be executed in the order they appear in the file. Comments can be added to the script file by starting a line with `//` characters.

[Version](#commands-builtin-version)
[Building](#building)

---

<a id="building"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/building.html -->

<!-- page_index: 24 -->

# Building

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="building--page-title"></a>
<a id="building--building"></a>

# Building

This section covers how to build a Spring Shell application.

<a id="building--_starters"></a>
<a id="building--starters"></a>

## Starters

1. Spring Shell Starters

| Name | Description |
| --- | --- |
| spring-shell-starter | Basic Spring Shell modules |
| spring-shell-starter-jansi | With JLine jansi provider |
| spring-shell-starter-jni | With JLine jni provider |
| spring-shell-starter-jna | With JLine jna provider |
| spring-shell-starter-ffm | With JLine ffm provider (requires JDK22+) |
| spring-shell-starter-test | Spring Shell testing support |

All Spring Shell starters import *spring-boot-starter*, so there is no need to
import *spring-boot-starter* when using a Spring Shell starter.

<a id="building--_terminal_providers"></a>
<a id="building--terminal-providers"></a>

## Terminal Providers

Interacting with an underlying terminal where your program is running has
traditionally been relatively complex process while it may look like
there’s not that much happening as it’s all just text.

Remember all those old manual typewriters or matrix printers?
A character is printed then a cursor needs to be moved
if printing in a different position. In a nutshell that’s how current
terminal emulators work.

To access and understand existing terminal emulators environment better, JLine can use native code via its own shared libraries. JLine detects
which providers are present and then makes a choice which one to use.
Traditionally there’s been 3 providers, `jansi`, `jni` and `jna` which
should all provide same functionalities.

Our starters can be used to specifically pick some of these JLine
providers.

<a id="building--_ffm"></a>
<a id="building--ffm"></a>

## FFM

With `JDK22` a *Foreign Function and Memory API* came out from a preview
which is supposed to be a replacement for `JNI` providing much better
and safer native API.

Starting from `3.4.x` we’ve added a support to compile Spring Shell
application with `JLine` `ffm` terminal provider. This obviously mean
that application needs to be run with `JDK22+`. There is a new JDK
intermediate release every 6 months and long term support(LTS) release
every 2 years. Until there’s an existing LTS release Spring Shell can
align with Spring Framework we will use latest JDK release. Obviously
this means that you may need to upgrade your JDK in an inconvenient
time if you choose to use `ffm`. We’re also bound to JDK version
`JLine` itself uses to compile its `ffm` parts.

FFM itself will cause jvm to print warnings when some part of it are
used. These warnings are obviously annoying with terminal applications
as it may interfere and cause a little bit of a mess. In future JDK
versions these warnings will also be added for an older JNI modules and
at some point these warnings will be changed into hard errors. User will
be required to enable these native "unsafe" parts manually.

JVM option for this in a command line is:

```bash
--enable-native-access=ALL-UNNAMED
```

If you have a jar file you can have this setting in its `META-INF/MANIFEST.MF`.

```none
Enable-Native-Access: ALL-UNNAMED
```

Which can be added during a build i.e. if using gradle:

```groovy
tasks.named("bootJar") {
    manifest {
        attributes 'Enable-Native-Access': 'ALL-UNNAMED'
    }
}
```

> [!IMPORTANT]
> What comes for enabling native parts in a JDK, JLine has been
> proactive and already has a check for this and will throw error if
> native access is not enabled.

<a id="building--native"></a>
<a id="building--native-support"></a>

## Native Support

Support for compiling *Spring Shell* application into a *GraalVM* binary
mostly comes from *Spring Framework* and *Spring Boot* where feature is
called *AOT*. Ahead of Time means that application context is prepared
during the compilation time to being ready for *GraalVM* generation.

Building atop of *AOT* features from a framework *Spring Shell* has its
own *GraalVM* configuration providing hints what should exist in
a binary. Usually trouble comes from a 3rd party libraries which doesn’t
yet contain *GraalVM* related configurations or those configurations
are incomplete.

> [!IMPORTANT]
> It is requred to use *GraalVM Reachability Metadata Repository* which
> provides some missing hints for 3rd party libraries. Also you need to have
> *GraalVM* installed and `JAVA_HOME` pointing to that.

For *gradle* add graalvm’s native plugin and configure metadata repository.

```groovy
plugins {id 'org.graalvm.buildtools.native' version '0.9.16'}
graalvmNative {metadataRepository {enabled = true}}
```

When gradle build is run with `./gradlew nativeCompile` you should get binary
under `build/native/nativeCompile` directory.

For `maven` use `spring-boot-starter-parent` as parent and you’ll get `native`
profile which can be used to do a native compilation. You need to configure metadata repository:

```xml
<build>
    <pluginManagement>
        <plugins>
            <plugin>
                <groupId>org.graalvm.buildtools</groupId>
                <artifactId>native-maven-plugin</artifactId>
                <configuration>
                    <metadataRepository>
                        <enabled>true</enabled>
                    </metadataRepository>
                </configuration>
            </plugin>
        </plugins>
    </pluginManagement>
</build>
```

> [!NOTE]
> If you rely on `spring-boot-starter-parent` it manages `native-maven-plugin`
> version which is kept up to date.

When maven build is run with `./mvnw native:compile -Pnative` you should get binary
under `target` directory.

If everything went well this binary can be run as is instead of executing
boot application jar via jvm.

[Script](#commands-builtin-script)
[Components](#components)

---

<a id="components"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/index.html -->

<!-- page_index: 25 -->

<a id="components--page-title"></a>
<a id="components--components"></a>

# Components

Components are a set of features which are either built-in or something
you can re-use or extend for your own needs. Components in question are
either built-in *commands* or UI side components providing higher level
features within commands itself.

<a id="components--section-summary"></a>

## Section Summary

- [Flow](#components-flow)
- [Flow Components](#components-ui)

[Building](#building)
[Flow](#components-flow)

---

<a id="components-flow"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/flow/index.html -->

<!-- page_index: 26 -->

# Flow

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-flow--page-title"></a>
<a id="components-flow--flow"></a>

# Flow

When you use [Flow Components](#components-ui) to build something that involves
use of a multiple components, your implementation may become a bit cluttered.
To ease these use cases, we added a
`ComponentFlow` that can hook multiple component executions together
as a “flow”.

The following listings show examples of flows and their output in a shell:

```java
static class FlowSampleComplex {

	@Autowired
	private ComponentFlow.Builder componentFlowBuilder;

	public void runFlow() {
		List<SelectItem> single1SelectItems = Arrays.asList(SelectItem.of("key1", "value1"),
				SelectItem.of("key2", "value2"));
		List<SelectItem> multi1SelectItems = Arrays.asList(SelectItem.of("key1", "value1"),
				SelectItem.of("key2", "value2"), SelectItem.of("key3", "value3"));
		ComponentFlow flow = componentFlowBuilder.clone()
			.reset()
			.withStringInput("field1")
			.name("Field1")
			.defaultValue("defaultField1Value")
			.and()
			.withStringInput("field2")
			.name("Field2")
			.and()
			.withNumberInput("number1")
			.name("Number1")
			.and()
			.withNumberInput("number2")
			.name("Number2")
			.defaultValue(20.5)
			.numberClass(Double.class)
			.and()
			.withConfirmationInput("confirmation1")
			.name("Confirmation1")
			.and()
			.withPathInput("path1")
			.name("Path1")
			.and()
			.withSingleItemSelector("single1")
			.name("Single1")
			.selectItems(single1SelectItems)
			.and()
			.withMultiItemSelector("multi1")
			.name("Multi1")
			.selectItems(multi1SelectItems)
			.and()
			.build();
		flow.run();
	}

}
```

> [!NOTE]
> Normal execution order of a components is same as defined with a builder.

It’s possible to conditionally choose where to jump in a flow by using a `next`
function and returning target *component id*. If this returned id is either *null*
or doesn’t exist flow is essentially stopped right there.

```java
static class FlowSampleConditional {

	@Autowired
	private ComponentFlow.Builder componentFlowBuilder;

	public void runFlow() {
		Map<String, String> single1SelectItems = new HashMap<>();
		single1SelectItems.put("Field1", "field1");
		single1SelectItems.put("Field2", "field2");
		ComponentFlow flow = componentFlowBuilder.clone()
			.reset()
			.withSingleItemSelector("single1")
			.name("Single1")
			.selectItems(single1SelectItems)
			.next(ctx -> ctx.getResultItem().get().getItem())
			.and()
			.withStringInput("field1")
			.name("Field1")
			.defaultValue("defaultField1Value")
			.next(ctx -> null)
			.and()
			.withStringInput("field2")
			.name("Field2")
			.defaultValue("defaultField2Value")
			.next(ctx -> null)
			.and()
			.build();
		flow.run();
	}

}
```

> [!TIP]
> The result from running a flow returns `ComponentFlowResult`, which you can
> use to do further actions.

[Components](#components)
[Flow Components](#components-ui)

---

<a id="components-ui"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/index.html -->

<!-- page_index: 27 -->

# Flow Components

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui--page-title"></a>
<a id="components-ui--flow-components"></a>

# Flow Components

Starting from version 2.1.x, a new component model provides an
easier way to create higher-level user interaction for the usual use cases, such as asking for input in various forms. These usually are just plain text
input or choosing something from a list.

Templates for built-in components are in the
`org/springframework/shell/component` classpath.

Built-in components generally follow this logic:

1. Enter a run loop for user input.
2. Generate component-related context.
3. Render the runtime status of a component state.
4. Exit.
5. Render the final status of a component state.

> [!NOTE]
> [Flow](#components-flow) gives better interface for defining the flow of
> components that are better suited for defining interactive command flows.

[Flow](#components-flow)
[Component Render](#components-ui-render)

---

<a id="components-ui-render"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/render.html -->

<!-- page_index: 28 -->

# Component Render

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-render--page-title"></a>
<a id="components-ui-render--component-render"></a>

# Component Render

You can implement component rendering in either of two ways: fully
programmatically or by using a *ANTLR Stringtemplate*.
Strictly speaking, there is a simple `Function` renderer interface
that takes `Context` as an input and outputs a list of `AttributedString`.
This lets you choose between templating and code.

Templating is a good choice if you do not need to do anything complex or
you just want to slightly modify existing component layouts. Rendering
through code then gives you flexibility to do whatever you need.

The programmatic way to render is to create a `Function`:

```java
class StringInputCustomRenderer implements Function<StringInputContext, List<AttributedString>> {
@Override public List<AttributedString> apply(StringInputContext context) {AttributedStringBuilder builder = new AttributedStringBuilder(); builder.append(context.getName()); builder.append(" "); if (context.getResultValue() != null) {builder.append(context.getResultValue());} else {String input = context.getInput(); if (StringUtils.hasText(input)) {builder.append(input);} else {builder.append("[Default " + context.getDefaultValue() + "]");}} return Arrays.asList(builder.toAttributedString());}
}
```

Then you can hook it to a component:

```java
@Command(name = "component stringcustom", description = "String input", group = "Components")
public String stringInputCustom(boolean mask) {
	StringInput component = new StringInput(getTerminal(), "Enter value", "myvalue",
			new StringInputCustomRenderer());
	ResourceLoader resourceLoader = null; // getResourceLoader();
	TemplateExecutor templateExecutor = null; // getTemplateExecutor();
	component.setResourceLoader(resourceLoader);
	component.setTemplateExecutor(templateExecutor);
	if (mask) {
		component.setMaskCharacter('*');
	}
	StringInputContext context = component.run(StringInputContext.empty());
	return "Got value " + context.getResultValue();
}
```

Components have their own context but usually share some functionality
from a parent component types. The following tables show those context variables:

| Key | Description |
| --- | --- |
| `resultValue` | The value after a component renders its result. |
| `name` | The name of a component — that is, its title. |
| `message` | The possible message set for a component. |
| `messageLevel` | The level of a message — one of `INFO`, `WARN`, or `ERROR`. |
| `hasMessageLevelInfo` | Return `true` if level is `INFO`. Otherwise, false. |
| `hasMessageLevelWarn` | Return `true` if level is `WARN`. Otherwise, false. |
| `hasMessageLevelError` | Return `true` if level is `ERROR`. Otherwise, false. |
| `input` | The raw user input. |

| Key | Description |
| --- | --- |
| `name` | The name of a component — that is, its title. |
| `input` | The raw user input — mostly used for filtering. |
| `itemStates` | The full list of item states. |
| `itemStateView` | The visible list of item states. |
| `isResult` | Return `true` if the context is in a result mode. |
| `cursorRow` | The current cursor row in a selector. |

| Key | Description |
| --- | --- |
| `terminalWidth` | The width of terminal, type is *Integer* and defaults to *NULL* if not set. |

[Flow Components](#components-ui)
[String Input](#components-ui-stringinput)

---

<a id="components-ui-stringinput"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/stringinput.html -->

<!-- page_index: 29 -->

# String Input

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-stringinput--page-title"></a>
<a id="components-ui-stringinput--string-input"></a>

# String Input

The string input component asks a user for simple text input, optionally masking values
if the content contains something sensitive. The input can also be required (at least 1 char).
The following listing shows an example:

```java
public class ComponentCommands {

	@Command(name = "component string", description = "String input", group = "Components")
	public String stringInput(boolean mask) {
		StringInput component = new StringInput(getTerminal(), "Enter value", "myvalue");
		ResourceLoader resourceLoader = null; // getResourceLoader();
		TemplateExecutor templateExecutor = null; // getTemplateExecutor();
		component.setResourceLoader(resourceLoader);
		component.setTemplateExecutor(templateExecutor);
		if (mask) {
			component.setMaskCharacter('*');
		}
		StringInputContext context = component.run(StringInputContext.empty());
		return "Got value " + context.getResultValue();
	}

}
```

The following screencast shows typical output from a string input component:

The context object is `StringInputContext`. The following table lists its context variables:

| Key | Description |
| --- | --- |
| `defaultValue` | The default value, if set. Otherwise, null. |
| `maskedInput` | The masked input value |
| `maskedResultValue` | The masked result value |
| `maskCharacter` | The mask character, if set. Otherwise, null. |
| `hasMaskCharacter` | `true` if a mask character is set. Otherwise, false. |
| `required` | `true` if the input is required. Otherwise, false. |
| `model` | The parent context variables (see [TextComponentContext Template Variables](#components-ui-render--textcomponentcontext-template-variables)). |

[Component Render](#components-ui-render)
[Number Input](#components-ui-numberinput)

---

<a id="components-ui-numberinput"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/numberinput.html -->

<!-- page_index: 30 -->

# Number Input

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-numberinput--page-title"></a>
<a id="components-ui-numberinput--number-input"></a>

# Number Input

The number input component asks a user for simple number input. It can be configured to use any implementation of Number.class. The following listing shows an example:

```java
NumberInput component = new NumberInput(getTerminal(), "Enter value", 99.9, Double.class);
ResourceLoader resourceLoader = null; // getResourceLoader();
TemplateExecutor templateExecutor = null; // getTemplateExecutor();
component.setResourceLoader(resourceLoader);
component.setTemplateExecutor(templateExecutor);

NumberInputContext context = component.run(NumberInputContext.empty());
return "Got value " + context.getResultValue();
```

The following image shows typical output from a number input component:

The context object is `NumberInputContext`. The following table lists its context variables:

| Key | Description |
| --- | --- |
| `defaultValue` | The default value, if set. Otherwise, null. |
| `defaultClass` | The default number class to use, if set. Otherwise, Integer.class. |
| `required` | `true` if the input is required. Otherwise, false. |
| `model` | The parent context variables (see [TextComponentContext Template Variables](#components-ui-render--textcomponentcontext-template-variables)). |

[String Input](#components-ui-stringinput)
[Path Input](#components-ui-pathinput)

---

<a id="components-ui-pathinput"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/pathinput.html -->

<!-- page_index: 31 -->

# Path Input

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-pathinput--page-title"></a>
<a id="components-ui-pathinput--path-input"></a>

# Path Input

The path input component asks a user for a `Path` and gives additional information about a path itself.

```java
public class ComponentCommands {

	@Command(name = "component path input", description = "Path input", group = "Components")
	public String pathInput() {
		PathInput component = new PathInput(getTerminal(), "Enter value");
		ResourceLoader resourceLoader = null; // getResourceLoader();
		TemplateExecutor templateExecutor = null; // getTemplateExecutor();
		component.setResourceLoader(resourceLoader);
		component.setTemplateExecutor(templateExecutor);
		PathInputContext context = component.run(PathInputContext.empty());
		return "Got value " + context.getResultValue();
	}

}
```

The following screencast shows typical output from a path input component:

The context object is `PathInputContext`. The following table describes its context variables:

| Key | Description |
| --- | --- |
| `model` | The parent context variables (see [TextComponentContext Template Variables](#components-ui-render--textcomponentcontext-template-variables)). |

[Number Input](#components-ui-numberinput)
[Path Search](#components-ui-pathsearch)

---

<a id="components-ui-pathsearch"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/pathsearch.html -->

<!-- page_index: 32 -->

# Path Search

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-pathsearch--page-title"></a>
<a id="components-ui-pathsearch--path-search"></a>

# Path Search

The path search component asks base directory for scan and optional search expression.
Results are shown in a single select list where user can pick a path.
`PathSearchConfig` can be used to customise component behaviour.

```java
PathSearchConfig config = new PathSearch.PathSearchConfig();
config.setMaxPathsShow(5);
config.setMaxPathsSearch(100);
config.setSearchForward(true);
config.setSearchCaseSensitive(false);
config.setSearchNormalize(false);

PathSearch component = new PathSearch(getTerminal(), "Enter value", config);
ResourceLoader resourceLoader = null; // getResourceLoader();
TemplateExecutor templateExecutor = null; // getTemplateExecutor();
component.setResourceLoader(resourceLoader);
component.setTemplateExecutor(templateExecutor);

PathSearchContext context = component.run(PathSearchContext.empty());
return "Got value " + context.getResultValue();
```

> [!NOTE]
> Logic for search is passed as is into algorithms documented
> in [Search Algorithms](#appendices-techintro-searchalgorithm).

The following screencast shows typical output from a path search component:

The context object is `PathSearchContext`. The following table describes its context variables:

| Key | Description |
| --- | --- |
| `pathViewItems` | The items available for rendering search results. |
| `model` | The parent context variables (see [TextComponentContext Template Variables](#components-ui-render--textcomponentcontext-template-variables)). |

[Path Input](#components-ui-pathinput)
[Confirmation](#components-ui-confirmation)

---

<a id="components-ui-confirmation"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/confirmation.html -->

<!-- page_index: 33 -->

# Confirmation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-confirmation--page-title"></a>
<a id="components-ui-confirmation--confirmation"></a>

# Confirmation

The confirmation component asks a user for a simple confirmation. It is essentially a
yes-or-no question.

```java
public class ComponentCommands {

	@Command(name = "component confirmation", description = "Confirmation input", group = "Components")
	public String confirmationInput(boolean no) {
		ConfirmationInput component = new ConfirmationInput(getTerminal(), "Enter value", !no);
		ResourceLoader resourceLoader = null; // getResourceLoader();
		TemplateExecutor templateExecutor = null; // getTemplateExecutor();
		component.setResourceLoader(resourceLoader);
		component.setTemplateExecutor(templateExecutor);
		ConfirmationInputContext context = component.run(ConfirmationInputContext.empty());
		return "Got value " + context.getResultValue();
	}

}
```

The following screencast shows the typical output from a confirmation component:

The context object is `ConfirmationInputContext`. The following table describes its context variables:

| Key | Description |
| --- | --- |
| `defaultValue` | The default value — either `true` or `false`. |
| `model` | The parent context variables (see [TextComponentContext Template Variables](#components-ui-render--textcomponentcontext-template-variables)). |

[Path Search](#components-ui-pathsearch)
[Single Select](#components-ui-singleselect)

---

<a id="components-ui-singleselect"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/singleselect.html -->

<!-- page_index: 34 -->

# Single Select

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-singleselect--page-title"></a>
<a id="components-ui-singleselect--single-select"></a>

# Single Select

A single select component asks a user to choose one item from a list. It is similar to a simple
dropbox implementation. The following listing shows an example:

```java
public class ComponentCommands {

	@Command(name = "component single", description = "Single selector", group = "Components")
	public String singleSelector() {
		SelectorItem<String> i1 = SelectorItem.of("key1", "value1");
		SelectorItem<String> i2 = SelectorItem.of("key2", "value2");
		List<SelectorItem<String>> items = Arrays.asList(i1, i2);
		SingleItemSelector<String, SelectorItem<String>> component = new SingleItemSelector<>(getTerminal(),
				items, "testSimple", null);
		ResourceLoader resourceLoader = null; // getResourceLoader();
		TemplateExecutor templateExecutor = null; // getTemplateExecutor();
		component.setResourceLoader(resourceLoader);
		component.setTemplateExecutor(templateExecutor);
		SingleItemSelectorContext<String, SelectorItem<String>> context = component
			.run(SingleItemSelectorContext.empty());
		String result = context.getResultItem().flatMap(si -> Optional.ofNullable(si.getItem())).get();
		return "Got value " + result;
	}

}
```

The following screencast shows typical output for a single select component:

The context object is `SingleItemSelectorContext`. The following table describes its context variables:

| Key | Description |
| --- | --- |
| `value` | The returned value when the component exists. |
| `rows` | The visible items, where rows contains maps of name and selected items. |
| `model` | The parent context variables (see [SelectorComponentContext Template Variables](#components-ui-render--selectorcomponentcontext-template-variables)). |

You can pre-select an item by defining it to get exposed. This is
useful if you know the default and lets the user merely press `Enter` to make a choice.
The following listing sets a default:

```java
SelectorItem<String> i1 = SelectorItem.of("key1", "value1");
SelectorItem<String> i2 = SelectorItem.of("key2", "value2");
List<SelectorItem<String>> items = Arrays.asList(i1, i2);
SingleItemSelector<String, SelectorItem<String>> component = new SingleItemSelector<>(getTerminal(),
		items, "testSimple", null);
component.setDefaultExpose(i2);
```

[Confirmation](#components-ui-confirmation)
[Multi Select](#components-ui-multiselect)

---

<a id="components-ui-multiselect"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/components/ui/multiselect.html -->

<!-- page_index: 35 -->

# Multi Select

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="components-ui-multiselect--page-title"></a>
<a id="components-ui-multiselect--multi-select"></a>

# Multi Select

The multi select component asks a user to select multiple items from a list.
The following listing shows an example:

```java
public class ComponentCommands {

	@Command(name = "component multi", description = "Multi selector", group = "Components")
	public String multiSelector() {
		List<SelectorItem<String>> items = new ArrayList<>();
		items.add(SelectorItem.of("key1", "value1"));
		items.add(SelectorItem.of("key2", "value2", false, true));
		items.add(SelectorItem.of("key3", "value3"));
		MultiItemSelector<String, SelectorItem<String>> component = new MultiItemSelector<>(getTerminal(),
				items, "testSimple", null);
		ResourceLoader resourceLoader = null; // getResourceLoader();
		TemplateExecutor templateExecutor = null; // getTemplateExecutor();
		component.setResourceLoader(resourceLoader);
		component.setTemplateExecutor(templateExecutor);
		MultiItemSelectorContext<String, SelectorItem<String>> context = component
			.run(MultiItemSelectorContext.empty());
		String result = context.getResultItems()
			.stream()
			.map(si -> si.getItem())
			.collect(Collectors.joining(","));
		return "Got value " + result;
	}

}
```

The following screencast shows a typical multi-select component:

The context object is `MultiItemSelectorContext`. The following table describes its context variables:

| Key | Description |
| --- | --- |
| `values` | The values returned when the component exists. |
| `rows` | The visible items, where rows contain maps of name, selected, on-row, and enabled items. |
| `model` | The parent context variables (see [SelectorComponentContext Template Variables](#components-ui-render--selectorcomponentcontext-template-variables)). |

[Single Select](#components-ui-singleselect)
[Terminal UI](#tui)

---

<a id="tui"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/index.html -->

<!-- page_index: 36 -->

<a id="tui--page-title"></a>
<a id="tui--terminal-ui"></a>

# Terminal UI

> [!NOTE]
> This feature is experimental and is subject to breaking changes until foundation
> and related concepts around framework are getting more stable.

*Terminal UI Framework* is a toolkit to build rich console apps. This section is
for those using existing features as is. If you’re planning to go deeper possibly
by creating your own components, then check [Terminal UI Appendix](#appendices-tui)
for more detailed documentation.

<a id="tui--section-summary"></a>

## Section Summary

- [Introduction](#tui-intro)
- [Views](#tui-views)
- [Events](#tui-events)

[Multi Select](#components-ui-multiselect)
[Introduction](#tui-intro)

---

<a id="tui-intro"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/intro/index.html -->

<!-- page_index: 37 -->

# Introduction

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-intro--page-title"></a>
<a id="tui-intro--introduction"></a>

# Introduction

Let’s start with a simple app which prints "hello world" in a view.

```java
@Autowired
TerminalUIBuilder builder;

void sample() {
	TerminalUI ui = builder.build();
	BoxView view = new BoxView();
	ui.configure(view);
	view.setDrawFunction((screen, rect) -> {
		screen.writerBuilder().build().text("Hello World", rect, HorizontalAlign.CENTER, VerticalAlign.CENTER);
		return rect;
	});
	ui.setRoot(view, true);
	ui.run();
}
```

There is not much to see here other than `TerminalUI` is a class handling
all logic around views and uses `View` as it’s root view.

<a id="tui-intro--section-summary"></a>

## Section Summary

- [TerminalUI](#tui-intro-terminalui)

[Terminal UI](#tui)
[TerminalUI](#tui-intro-terminalui)

---

<a id="tui-intro-terminalui"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/intro/terminalui.html -->

<!-- page_index: 38 -->

# TerminalUI

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-intro-terminalui--page-title"></a>
<a id="tui-intro-terminalui--terminalui"></a>

# TerminalUI

`TerminalUI` is a main implementation to drive ui execution logic.

<a id="tui-intro-terminalui--_create_terminalui"></a>
<a id="tui-intro-terminalui--create-terminalui"></a>

## Create TerminalUI

You can build `TerminalUI` manually but the recommended way is to use `TerminalUIBuilder`
which is autoconfigured for you and will set needed services.

```java
@Autowired
TerminalUIBuilder builder;

void sample() {
	TerminalUI ui = builder.build();
	// do something with ui
}
```

<a id="tui-intro-terminalui--_configuring_views"></a>
<a id="tui-intro-terminalui--configuring-views"></a>

## Configuring Views

`TerminalUI` has a helper method *configure(View)* which can be used to set
needed integrations into *eventloop* and other services.

```java
TerminalUI ui;

void sample() {
	BoxView view = new BoxView();
	ui.configure(view);
}
```

<a id="tui-intro-terminalui--_running_ui_loop"></a>
<a id="tui-intro-terminalui--running-ui-loop"></a>

## Running UI Loop

Running `TerminalUI` execution loop is a blocking operation. You’re going to need
a way to exit from a loop, for example [Exiting App](#tui-intro-terminalui--_exiting_app).

```java
TerminalUI ui;

void sample() {
	ui.run();
}
```

<a id="tui-intro-terminalui--_exiting_app"></a>
<a id="tui-intro-terminalui--exiting-app"></a>

## Exiting App

If you want to exit from an app using normal *CTRL-Q* key combination, then
you need to register a listener for events and request to *interrupt* the execution.

```java
@Autowired
Terminal terminal;

void sample() {
	TerminalUI ui = new TerminalUI(terminal);
	BoxView view = new BoxView();
	ui.configure(view);
	ui.setRoot(view, true);
	EventLoop eventLoop = ui.getEventLoop();
	eventLoop.keyEvents().subscribe(event -> {
		if (event.getPlainKey() == Key.q && event.hasCtrl()) {
			eventLoop.dispatch(ShellMessageBuilder.ofInterrupt());
		}
	});
	ui.run();
}
```

<a id="tui-intro-terminalui--_modal_view"></a>
<a id="tui-intro-terminalui--modal-view"></a>

## Modal View

`TerminalUI` supports having one active modal view. Modal view is placed
on top of all other views and takes all input events.

```java
TerminalUI ui;

void sample() {
	DialogView dialog = new DialogView();
	// set modal
	ui.setModal(dialog);
	// clear modal
	ui.setModal(null);
}
```

> [!NOTE]
> As views should not directly know anything about `TerminalUi` and
> interface `ViewService` exposes modal related functions.

[Introduction](#tui-intro)
[Views](#tui-views)

---

<a id="tui-views"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/index.html -->

<!-- page_index: 39 -->

# Views

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views--page-title"></a>
<a id="tui-views--views"></a>

# Views

Spring Shell provides a built-in views which are documented below.

<a id="tui-views--section-summary"></a>

## Section Summary

- [AppView](#tui-views-app)
- [BoxView](#tui-views-box)
- [ButtonView](#tui-views-button)
- [DialogView](#tui-views-dialog)
- [GridView](#tui-views-grid)
- [InputView](#tui-views-input)
- [ListView](#tui-views-list)
- [MenuView](#tui-views-menu)
- [MenuBarView](#tui-views-menubar)
- [ProgressView](#tui-views-progress)
- [StatusBarView](#tui-views-statusbar)

[TerminalUI](#tui-intro-terminalui)
[AppView](#tui-views-app)

---

<a id="tui-views-app"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/app.html -->

<!-- page_index: 40 -->

# AppView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-app--page-title"></a>
<a id="tui-views-app--appview"></a>

# AppView

*AppView* is a base implementation providing functionality to draw opinionated *application view*.
This view inherits from [BoxView](#tui-views-box).

The generic idea is to have menu and status views which typically are [MenuBarView](#tui-views-menubar) and
[StatusBarView](#tui-views-statusbar) respectively. Main content view is then whatever user want to show
in it.

```text
┌──────────────────────────┐
│           Menu           │
├──────────────────────────┤
│                          │
│           Main           │
│                          │
├──────────────────────────┤
│          Status          │
└──────────────────────────┘
```

<a id="tui-views-app--_key_handling"></a>
<a id="tui-views-app--key-handling"></a>

## Key Handling

If menu has a focus key handling is processed there, then main is consulted for handling.
Lastly cursor left/right are processed to dispatch *AppViewEvent*.

<a id="tui-views-app--_hotkey_handling"></a>
<a id="tui-views-app--hotkey-handling"></a>

## HotKey Handling

Hotkeys are processed in order of *main*, *menu* and *status*.

<a id="tui-views-app--_events"></a>
<a id="tui-views-app--events"></a>

## Events

| Event | Description |
| --- | --- |
| AppViewEvent | Direction for a next selection. |

[Views](#tui-views)
[BoxView](#tui-views-box)

---

<a id="tui-views-box"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/box.html -->

<!-- page_index: 41 -->

# BoxView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-box--page-title"></a>
<a id="tui-views-box--boxview"></a>

# BoxView

*BoxView* is a base implementation providing functionality to draw into a
bounded *Rectangle*. Only direct use of it is its `drawFunction` which
allows to do simple things without implementing a full custom `View`.

```java
BoxView view = new BoxView();
view.setDrawFunction((screen, rect) -> {
	screen.writerBuilder().build().text("hi", 0, 0);
	return rect;
});
```

<a id="tui-views-box--_customisation"></a>
<a id="tui-views-box--customisation"></a>

## Customisation

*BoxView* is mostly being a base class that contains some useful features
like if it should draw a border and what are its paddings.
Border can have a title and its color and focused color can be
defined. It’s also possible to explicitly set a background color
which will override one from styling.

<a id="tui-views-box--_default_bindings"></a>
<a id="tui-views-box--default-bindings"></a>

## Default Bindings

Does not have any default bindings.

<a id="tui-views-box--_events"></a>
<a id="tui-views-box--events"></a>

## Events

Does not have any events.

[AppView](#tui-views-app)
[ButtonView](#tui-views-button)

---

<a id="tui-views-button"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/button.html -->

<!-- page_index: 42 -->

# ButtonView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-button--page-title"></a>
<a id="tui-views-button--buttonview"></a>

# ButtonView

*ButtonView* is a base implementation providing functionality to draw a button.
*ButtonView* inherits from [BoxView](#tui-views-box).

```text
┌──────┐
│ text │
└──────┘
```

You can set a text for a button and action to do when button is selected.

```java
ButtonView view = new ButtonView();
view.setText("text");
view.setAction(() -> {
	// do something when selected
});
```

<a id="tui-views-button--_default_bindings"></a>
<a id="tui-views-button--default-bindings"></a>

## Default Bindings

Default *key bindings* are:

| Command | Description |
| --- | --- |
| Enter | Selects a button |

Default *mouse bindings* are:

| Command | Description |
| --- | --- |
| Released \| Button1 | Selects a button |

<a id="tui-views-button--_events"></a>
<a id="tui-views-button--events"></a>

## Events

| Event | Description |
| --- | --- |
| ButtonViewSelectEvent | Button is selected. |

[BoxView](#tui-views-box)
[DialogView](#tui-views-dialog)

---

<a id="tui-views-dialog"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/dialog.html -->

<!-- page_index: 43 -->

<a id="tui-views-dialog--page-title"></a>
<a id="tui-views-dialog--dialogview"></a>

# DialogView

*DialogView* is a base implementation providing functionality to draw a dialog.
*DialogView* inherits from [BoxView](#tui-views-box).

```text
┌──────────────────┐
│                  │
│  <Main content>  │
│                  │
├──────────────────┤
│    <Buttons>     │
└──────────────────┘
```

<a id="tui-views-dialog--_default_bindings"></a>
<a id="tui-views-dialog--default-bindings"></a>

## Default Bindings

Does not have any default bindings.

<a id="tui-views-dialog--_events"></a>
<a id="tui-views-dialog--events"></a>

## Events

Events are sent depending on a used list type.

| Event | Description |
| --- | --- |
| DialogViewCloseEvent | Dialog requested to get closed. |

[ButtonView](#tui-views-button)
[GridView](#tui-views-grid)

---

<a id="tui-views-grid"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/grid.html -->

<!-- page_index: 44 -->

# GridView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-grid--page-title"></a>
<a id="tui-views-grid--gridview"></a>

# GridView

*GridView* is a special type of view and its purpose is to layout other views
using a grid layout algorithms. *GridView* inherits from [BoxView](#tui-views-box).

```java
GridView grid = new GridView();
grid.setShowBorders(true);
grid.setRowSize(0, 0);
grid.setColumnSize(0, 0);

grid.addItem(new BoxView(), 0, 0, 1, 1, 0, 0);
grid.addItem(new BoxView(), 0, 1, 1, 1, 0, 0);
grid.addItem(new BoxView(), 1, 0, 1, 1, 0, 0);
grid.addItem(new BoxView(), 1, 1, 1, 1, 0, 0);
```

Will result layout of:

```text
┌───┬───┐
│   │   │
│   │   │
├───┼───┤
│   │   │
│   │   │
└───┴───┘
```

<a id="tui-views-grid--_default_bindings"></a>
<a id="tui-views-grid--default-bindings"></a>

## Default Bindings

Does not have any default bindings.

<a id="tui-views-grid--_events"></a>
<a id="tui-views-grid--events"></a>

## Events

Does not have any events.

[DialogView](#tui-views-dialog)
[InputView](#tui-views-input)

---

<a id="tui-views-input"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/input.html -->

<!-- page_index: 45 -->

# InputView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-input--page-title"></a>
<a id="tui-views-input--inputview"></a>

# InputView

*InputView* is a base implementation providing functionality to draw and modify
text in a bounded *Rectangle*.

```java
InputView input = new InputView();
String text = input.getInputText();
```

<a id="tui-views-input--_default_bindings"></a>
<a id="tui-views-input--default-bindings"></a>

## Default Bindings

Default *view commands* are:

| Command | Description |
| --- | --- |
| LEFT | Cursor moves left |
| RIGHT | Cursor moves right |
| DELETE\_CHAR\_LEFT | Delete character left |
| DELETE\_CHAR\_RIGHT | Delete character right |

Default *key bindings* are:

| Command | Description |
| --- | --- |
| CursorLeft | Bound ViewCommand LEFT |
| CursorRight | Bound ViewCommand RIGHT |
| Backspace | Bound ViewCommand DELETE\_CHAR\_LEFT |
| Delete | Bound ViewCommand DELETE\_CHAR\_RIGHT |

<a id="tui-views-input--_events"></a>
<a id="tui-views-input--events"></a>

## Events

Events are sent depending on a used list type.

| Event | Description |
| --- | --- |
| InputViewTextChangeEvent | Input text has changed |

[GridView](#tui-views-grid)
[ListView](#tui-views-list)

---

<a id="tui-views-list"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/list.html -->

<!-- page_index: 46 -->

# ListView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-list--page-title"></a>
<a id="tui-views-list--listview"></a>

# ListView

*ListView* is a base implementation providing functionality to draw a list of
*items*. *ListView* inherits from [BoxView](#tui-views-box).

*ListView<T>* is typed as its *item* and can take any object. Further *item*
processing happens in a *CellFactory*. For convenience, there is a support
for generic higher level list feature showing checked states as normal
*check* and *radio* types. Essentially what you can have is a list of
items which are shown as is, shown where any items can have a checked
state or only one item can have a checked state.

```java
ListView<String> view = new ListView<>();
view.setItems(List.of("item1", "item2"));
```

Default *item style* is nocheck but can be changed.

Supports `` NOCHECK, `CHECK and `RADIO` ``

```java
ListView<String> view = new ListView<>(ItemStyle.CHECKED);
```

<a id="tui-views-list--_customisation"></a>
<a id="tui-views-list--customisation"></a>

## Customisation

How individual cells are shown depends on a *CellFactory*. Default implementation
simply shows *item* using its `toString()` method.

It can be customised by modifying a used *CellFactory*.

```java
record ExampleData(String name) {};
static class ExampleListCell extends AbstractListCell<ExampleData> {
public ExampleListCell(ExampleData item) {super(item);}
@Override public void draw(Screen screen) {Rectangle rect = getRect(); Writer writer = screen.writerBuilder().style(getStyle()).build(); writer.text(getItem().name(), rect.x(), rect.y()); writer.background(rect, getBackgroundColor());}
}
```

And set it as a factory:

```java
ListView<ExampleData> view = new ListView<>();
view.setCellFactory((list, item) -> new ExampleListCell(item));
```

<a id="tui-views-list--_default_bindings"></a>
<a id="tui-views-list--default-bindings"></a>

## Default Bindings

Default *view commands* are:

| Command | Description |
| --- | --- |
| LINE\_UP | Selection moves up. |
| LINE\_DOWN | Selection moves down. |

Default *key bindings* are:

| Command | Description |
| --- | --- |
| CursorUp | Bound ViewCommand LINE\_UP |
| CursorDown | Bound ViewCommand LINE\_DOWN |
| Enter | Choose active item. |
| Space | Change active item selection state. |

Default *mouse bindings* are:

| Command | Description |
| --- | --- |
| Wheel \| WheelUp | Bound ViewCommand LINE\_UP |
| Wheel \| WheelDown | Bound ViewCommand LINE\_DOWN |
| Released \| Button1 | Choose item |

<a id="tui-views-list--_events"></a>
<a id="tui-views-list--events"></a>

## Events

Events are sent depending on a used list type.

| Event | Description |
| --- | --- |
| ListViewOpenSelectedItemEvent | Active item is requested to get opened. |
| ListViewSelectedItemChangedEvent | Active item is changed. |

[InputView](#tui-views-input)
[MenuView](#tui-views-menu)

---

<a id="tui-views-menu"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/menu.html -->

<!-- page_index: 47 -->

# MenuView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-menu--page-title"></a>
<a id="tui-views-menu--menuview"></a>

# MenuView

*MenuView* is a base implementation providing functionality to draw a menu.
*MenuView* inherits from [BoxView](#tui-views-box).

<a id="tui-views-menu--_default_bindings"></a>
<a id="tui-views-menu--default-bindings"></a>

## Default Bindings

Default *key bindings* are:

| Command | Description |
| --- | --- |
| CursorUp | Move selection up |
| CursorDown | Move selection down |
| Enter | Choose active item. |

Default *mouse bindings* are:

| Command | Description |
| --- | --- |
| Wheel \| WheelUp | Move selection up |
| Wheel \| WheelDown | Move selection down |
| Released \| Button1 | Choose item |

<a id="tui-views-menu--_events"></a>
<a id="tui-views-menu--events"></a>

## Events

Events are sent depending on a used list type.

| Event | Description |
| --- | --- |
| MenuViewOpenSelectedItemEvent | Active item is requested to get opened. |
| MenuViewSelectedItemChangedEvent | Active item is changed. |

[ListView](#tui-views-list)
[MenuBarView](#tui-views-menubar)

---

<a id="tui-views-menubar"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/menubar.html -->

<!-- page_index: 48 -->

# MenuBarView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-menubar--page-title"></a>
<a id="tui-views-menubar--menubarview"></a>

# MenuBarView

*MenuBarView* is a base implementation providing functionality to draw a menu bar.
*MenuBarView* inherits from [BoxView](#tui-views-box).

```text
┌─────────────────────────────┐
│ File Help                   │
└─────────────────────────────┘
```

*MenuBarView* is constructed with instances of *MenuBarItem*. *MenuBarItem* itself
takes instances of *MenuItem*. *MenuItem* can define its style and action.
*MenuBarItem* can also define a hot key which is used to active particular menu.

```java
Runnable quitAction = () -> {}; Runnable aboutAction = () -> {}; MenuBarView menuBar = MenuBarView.of(MenuBarItem.of("File", MenuItem.of("Quit", MenuItemCheckStyle.NOCHECK, quitAction)) .setHotKey(Key.f | KeyMask.AltMask),MenuBarItem.of("Help", MenuItem.of("About", MenuItemCheckStyle.NOCHECK, aboutAction)));
```

<a id="tui-views-menubar--_default_bindings"></a>
<a id="tui-views-menubar--default-bindings"></a>

## Default Bindings

Default *key bindings* are:

| Command | Description |
| --- | --- |
| CursorLeft | Move selection left |
| CursorRight | Move selection right |

Default *mouse bindings* are:

| Command | Description |
| --- | --- |
| Released \| Button1 | Choose item |

<a id="tui-views-menubar--_events"></a>
<a id="tui-views-menubar--events"></a>

## Events

Does not have any events.

[MenuView](#tui-views-menu)
[ProgressView](#tui-views-progress)

---

<a id="tui-views-progress"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/progress.html -->

<!-- page_index: 49 -->

# ProgressView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-progress--page-title"></a>
<a id="tui-views-progress--progressview"></a>

# ProgressView

*ProgressView* is a base implementation providing functionality to draw a progress information.
*ProgressView* inherits from [BoxView](#tui-views-box).

*ProgressView* draws its content using concepts described below:

- *ProgressState* contains various info about a runtime state

  - *tickStart*: Lower bound of tick value
  - *tickEnd*: Upper bound of tick value
  - *tickValue*: Current tick value
  - *running*: Running state, either true or false
  - *startTime*: Start time in millis when progress was started
  - *updateTime*: Last known time in millis when progress has updated
- *ProgressContext* is a context used with *ProgressViewItem*

  - *description*: The description given to progress
  - *state*: The *ProgressState*
  - *view*: The owning *ProgressView*
  - *spinner*: The *Spinner* representation used with *ProgressView*
  - Other methods to help with item drawing
- *ProgressViewItem*: is a representation of a cell used in *ProgressView*

There are few build-in items namely `text`, `spinner` and `percent`.

Default *ProgressView* gives you `text`, `spinner` and `percent`.

```java
ProgressView view = new ProgressView();
view.start();
```

And looks like:

<a id="tui-views-progress--_customisation"></a>
<a id="tui-views-progress--customisation"></a>

## Customisation

Here are some examples for various customisations:

```java
ProgressView view = new ProgressView(ProgressViewItem.ofText(10, HorizontalAlign.LEFT),
		ProgressViewItem.ofSpinner(3, HorizontalAlign.LEFT),
		ProgressViewItem.ofPercent(0, HorizontalAlign.RIGHT));
view.start();
```

Align `text` and `spinner` to left and give them less space. Align `percent` to right
and give it remaining space.

<a id="tui-views-progress--_default_bindings"></a>
<a id="tui-views-progress--default-bindings"></a>

## Default Bindings

Does not have any default bindings.

<a id="tui-views-progress--_events"></a>
<a id="tui-views-progress--events"></a>

## Events

Events are sent depending on a state of a progress.

| Event | Description |
| --- | --- |
| ProgressViewStartEvent | Progress tracking has started |
| ProgressViewEndEvent | Progress tracking has stopped |
| ProgressViewStateChangeEvent | Progress tracking state has changed |

[MenuBarView](#tui-views-menubar)
[StatusBarView](#tui-views-statusbar)

---

<a id="tui-views-statusbar"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/views/statusbar.html -->

<!-- page_index: 50 -->

# StatusBarView

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-views-statusbar--page-title"></a>
<a id="tui-views-statusbar--statusbarview"></a>

# StatusBarView

*StatusBarView* is a base implementation providing functionality to draw a status bar.
*StatusBarView* inherits from [BoxView](#tui-views-box).

```text
┌─────────────────────────────┐
│ Item1 | Item2 | Item3       │
└─────────────────────────────┘
```

You can create a simple status bar with an item:

```java
StatusItem item1 = new StatusBarView.StatusItem("Item1");
StatusBarView statusBar = new StatusBarView(List.of(item1));
```

The constructor can take array form which allows to lay out simple
item definitions in a *dsl* style:

```java
new StatusBarView(new StatusItem[] { StatusItem.of("Item1"), StatusItem.of("Item2").setAction(() -> {
}), StatusItem.of("Item3").setAction(() -> {
}).setHotKey(Key.f10) });
```

Items support runnable actions which generally are executed when
item is selected. It can also get attached to a hot key.

```java
StatusItem item1 = StatusBarView.StatusItem.of("Item1");
Runnable action1 = () -> {}; StatusItem item2 = StatusBarView.StatusItem.of("Item2", action1);
Runnable action2 = () -> {}; StatusItem item3 = StatusBarView.StatusItem.of("Item3", action2, KeyEvent.Key.f10);
StatusBarView statusBar = new StatusBarView(); statusBar.setItems(List.of(item1, item2, item3));
```

<a id="tui-views-statusbar--_events"></a>
<a id="tui-views-statusbar--events"></a>

## Events

| Event | Description |
| --- | --- |
| StatusBarViewOpenSelectedItemEvent | StatusItem is selected. |

[ProgressView](#tui-views-progress)
[Events](#tui-events)

---

<a id="tui-events"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/events/index.html -->

<!-- page_index: 51 -->

<a id="tui-events--page-title"></a>
<a id="tui-events--events"></a>

# Events

This section contains information about event handling.

<a id="tui-events--section-summary"></a>

## Section Summary

- [EventLoop](#tui-events-eventloop)
- [Key Handling](#tui-events-key)
- [Mouse Handling](#tui-events-mouse)

[StatusBarView](#tui-views-statusbar)
[EventLoop](#tui-events-eventloop)

---

<a id="tui-events-eventloop"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/events/eventloop.html -->

<!-- page_index: 52 -->

# EventLoop

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="tui-events-eventloop--page-title"></a>
<a id="tui-events-eventloop--eventloop"></a>

# EventLoop

`EventLoop` is a central place where all eventing will be orchestrated for
a lifecycle of a component. Orchestration is usually needed around timings
of redraws and component state updates.

Everything in an event loop is represented as a Spring Message:

```java
TerminalUI ui = new TerminalUI(terminal);
EventLoop eventLoop = ui.getEventLoop();
Flux<? extends Message<?>> events = eventLoop.events();
events.subscribe();
```

Selecting key events use a built-in filtering method *keyEvents()*.

```java
TerminalUI ui = new TerminalUI(terminal);
EventLoop eventLoop = ui.getEventLoop();
eventLoop.keyEvents().doOnNext(event -> {
	// do something with key event
}).subscribe();
```

[Events](#tui-events)
[Key Handling](#tui-events-key)

---

<a id="tui-events-key"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/events/key.html -->

<!-- page_index: 53 -->

<a id="tui-events-key--page-title"></a>
<a id="tui-events-key--key-handling"></a>

# Key Handling

Views have their own default bindings which can be changed.

You can subscribe to all key events:

```java
eventLoop.keyEvents().subscribe((KeyEvent event) -> {
	// do something with key event
});
```

`KeyEvent` is a record containing information about a binding coming out
from a terminal.

Some views allow you to register hot keys which are processed before
normal key handling. More about this can be found in
[Register Bindings](#appendices-tui-viewdev--register-bindings).

[EventLoop](#tui-events-eventloop)
[Mouse Handling](#tui-events-mouse)

---

<a id="tui-events-mouse"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/tui/events/mouse.html -->

<!-- page_index: 54 -->

<a id="tui-events-mouse--page-title"></a>
<a id="tui-events-mouse--mouse-handling"></a>

# Mouse Handling

You can subscribe to all mouse events:

```java
eventLoop.mouseEvents().subscribe((MouseEvent event) -> {
	// do something with mouse event
});
```

`MouseEvent` is a record wrapping *X* and *Y* coordinates and
`org.jline.terminal.MouseEvent` from JLine library.

[Key Handling](#tui-events-key)
[Customization](#customization)

---

<a id="customization"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/customization/index.html -->

<!-- page_index: 55 -->

<a id="customization--page-title"></a>
<a id="customization--customization"></a>

# Customization

This section describes how you can customize the shell.

<a id="customization--section-summary"></a>

## Section Summary

- [Theming](#customization-styling)
- [Context Close](#customization-contextclose)
- [Custom Prompt](#customization-custom-prompt)

[Mouse Handling](#tui-events-mouse)
[Theming](#customization-styling)

---

<a id="customization-styling"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/customization/styling.html -->

<!-- page_index: 56 -->

# Theming

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="customization-styling--page-title"></a>
<a id="customization-styling--theming"></a>

# Theming

Current terminal implementations are rich in features and can usually show
something else that just plain text. For example, a text can be styled to be
*bold* or have different colors. It’s also common for terminals to be able
to show various characters from a unicode table like emoji’s which are usually
used to make shell output more pretty.

Spring Shell supports these via it’s theming framework which contains two parts.
Firstly, *styling* can be used to change text type and secondly, *figures* are used
to customize how characters are shown. These two parts are then combined as a *theme*.

For more detail about *theming* internals, refer to see [Theming](#appendices-techintro-theming).

> [!NOTE]
> Default theme is named `default` but can be changed using the property
> `spring.shell.theme.name`. There is also another built-in theme named `dump`
> that uses no styling for colors and tries to not use any special figures.

You can modify existing styles and figures by overriding the default settings:

```java
static class MyStyleSettings extends StyleSettings {
@Override public String highlight() {return super.highlight();}
}
```

```java
static class MyFigureSettings extends FigureSettings {
@Override public String error() {return super.error();}
}
```

You can also create a new theme, by creating a `ThemeSettings` and provide your own *style*
and *figure* implementations:

```java
static class MyThemeSettings extends ThemeSettings {
@Override public StyleSettings styles() {return new MyStyleSettings();}
@Override public FigureSettings figures() {return new MyFigureSettings();}
}
```

Register a new bean `Theme` where you can return your custom `ThemeSettings`
and a *theme* name.

```java
@Configuration static class CustomThemeConfig {
@Bean Theme myTheme() {return new Theme() {@Override public String getName() {return "mytheme";}
@Override public ThemeSettings getSettings() {return new MyThemeSettings();} };}
}
```

You can use `ThemeResolver` to resolve *styles* if you want to create
JLine-styled strings programmatically and *figures* if you want to
theme characters for being more pretty.

```java
@Autowired
private ThemeResolver resolver;

void resolve() {
	String resolvedStyle = resolver.resolveStyleTag(StyleSettings.TAG_TITLE);
	// bold,fg:bright-white

	AttributedStyle style = resolver.resolveStyle(resolvedStyle);
	// jline attributed style from expression above

	String resolvedFigure = resolver.resolveFigureTag(FigureSettings.TAG_ERROR);
	// character i.e. U+2716 Heavy Multiplication X Emoji, cross
}
```

[Customization](#customization)
[Context Close](#customization-contextclose)

---

<a id="customization-contextclose"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/customization/contextclose.html -->

<!-- page_index: 57 -->

# Context Close

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="customization-contextclose--page-title"></a>
<a id="customization-contextclose--context-close"></a>

# Context Close

Command execution logic happens via Spring Boot’s `ApplicationRunner` beans.
Normally Spring `ApplicationContext` closes automatically after these runner
beans has been processed unless there is something what keeps it alive like
use of `@EnableScheduling` or generally speaking there are threads which
don’t die automatically.

It is possible to add configuration property `spring.shell.context.close`
which registers `ApplicationListener` for `ApplicationReadyEvent` and requests
context close after shell has completed its execution logic.

```yaml
spring:
  shell:
    context:
      close: true
```

> [!NOTE]
> This setting is not enabled by default.

[Theming](#customization-styling)
[Custom Prompt](#customization-custom-prompt)

---

<a id="customization-custom-prompt"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/customization/custom-prompt.html -->

<!-- page_index: 58 -->

# Custom Prompt

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="customization-custom-prompt--page-title"></a>
<a id="customization-custom-prompt--custom-prompt"></a>

# Custom Prompt

Spring Shell provides various ways to customize the shell prompt and output appearance.

When using the JLine-based shell with Spring Boot, you can customize the shell prompt by implementing the `PromptProvider` interface. This allows you to define your own prompt format.

Here is an example of how to create a custom prompt in a Spring Boot application:

```java
@SpringBootApplication static class SpringShellApplication {
@Command public void hi() {System.out.println("Hello world!");}
@Bean public PromptProvider myPromptProvider() {return () -> new AttributedString("myprompt:>", AttributedStyle.DEFAULT.foreground(AttributedStyle.YELLOW));}
}
```

Adding the above `PromptProvider` bean will change the shell prompt to "myprompt:>" displayed in yellow color.

[Context Close](#customization-contextclose)
[Execution](#execution)

---

<a id="execution"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/execution.html -->

<!-- page_index: 59 -->

# Execution

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="execution--page-title"></a>
<a id="execution--execution"></a>

# Execution

This section describes how to set up a Spring Shell to work in interactive mode.

<a id="execution--using-shell-execution-interactionmode"></a>
<a id="execution--interaction-mode"></a>

## Interaction Mode

Version 2.1.x introduced built-in support to distinguish between interactive
and non-interactive modes. This makes it easier to use the shell as a
simple command-line tool without requiring customization.

Currently, interactive mode is entered if any command line options are passed when starting
or running a shell from a command line. This works especially well when a shell application
is compiled with [Native Support](#building--native).

Some commands may not have any useful meanings when they run in interactive mode
or (conversely) in non-interactive mode. For example, a built-in `exit` command would
have no meaning in non-interactive mode, because it is used to exit interactive mode.

<a id="execution--using-shell-execution-shellrunner"></a>
<a id="execution--shell-runners"></a>

## Shell Runners

`ShellRunner` is the main interface to run a shell. There can be only one `ShellRunner`
per application context.

Three `ShellRunner` implementations exist, named `SystemShellRunner`, `JLineShellRunner` and `NonInteractiveShellRunner`. By default, it is
the interactive `SystemShellRunner` that is used.

To enable non-interactive mode, you can set the `spring.shell.interactive.enabled`
property to `false`. This will switch the `ShellRunner` implementation to
`NonInteractiveShellRunner`.

> [!NOTE]
> In a Spring Boot application, Spring Shell registers an `ApplicationRunner` bean named `springShellApplicationRunner`
> that runs the interactive shell runner. If you want to use a different `ShellRunner` implementation, you need to override the default `ApplicationRunner`.

<a id="execution--debug-mode"></a>

## Debug Mode

Spring Shell provides a debug mode that can be enabled by setting the
`spring.shell.debug.enabled` property to `true`. When enabled, this mode
provides additional debugging information for command execution by printing
stack traces of errors, which can be useful for troubleshooting and development purposes.

[Custom Prompt](#customization-custom-prompt)
[Testing](#testing)

---

<a id="testing"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/testing.html -->

<!-- page_index: 60 -->

# Testing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="testing--page-title"></a>
<a id="testing--testing"></a>

# Testing

Spring Shell provides several utilities to facilitate testing of shell applications. These utilities help simulate user input, capture output, and verify command behavior in a controlled environment.

<a id="testing--_test_assertions"></a>
<a id="testing--test-assertions"></a>

## Test assertions

Spring Shell offers the following test assertion APIs to validate command execution and output:

- `ShellScreen`: This class represents the shell screen and allows you to capture and analyze the output displayed to the user.
- `ShellAssertions`: This class provides static methods to assert the results of shell command executions.
- `ShellTestClient`: This class allows you to simulate user input and execute shell commands programmatically.

Here is an example of how to use these APIs in a test:

```java
@ExtendWith(SpringExtension.class)
class ShellTestClientTests {

	@Test
	void testCommandExecution(@Autowired ShellTestClient shellTestClient) throws Exception {
		// when
		ShellScreen shellScreen = shellTestClient.sendCommand("test");

		// then
		ShellAssertions.assertThat(shellScreen).containsText("Test command executed");
	}
}
```

<a id="testing--_test_annotations"></a>
<a id="testing--test-annotations"></a>

## Test annotations

Spring Shell provides the `@ShellTest` annotation which is used to indicate that a test class is a Spring Shell test. It sets up the necessary context for testing shell commands. This annotation is defined in the `spring-shell-test-autoconfigure` module, and is designed to be used with Spring Boot applications.

Once you define your Spring Boot application class, you can create a test class annotated with `@ShellTest` to test your shell commands. Here is an example:

```java
@SpringBootApplication public class ExampleShellApplication {
@Command(name = "hi", description = "Says hello") public String hello() {return "hello";}
}
@ShellTest @ContextConfiguration(classes = ExampleShellApplication.class) class ShellTestIntegrationTests {
@Test void testCommandExecution(@Autowired ShellTestClient client) throws Exception {// when ShellScreen shellScreen = client.sendCommand("hi");
// then ShellAssertions.assertThat(shellScreen).containsText("hello");}
@Test void testUnknownCommandExecution(@Autowired ShellTestClient client) {Assertions.assertThatThrownBy(() -> client.sendCommand("foo")) .isInstanceOf(CommandNotFoundException.class);}
}
```

Spring Shell also provides the `ShellInputProvider` API which can be used to provide custom input for testing purposes. This allows you to simulate user input (clear texts and passwords) in a more flexible way.

For example, if your command expects input as follows:

```java
@Bean public Command ask() {return new AbstractCommand("ask", "Ask for user input") {@Override public ExitStatus doExecute(CommandContext commandContext) throws Exception {String message = commandContext.inputReader().readInput(); commandContext.outputWriter().println("You said: " + message); return ExitStatus.OK;} };}
```

then you can simulate the user’s input by using `ShellInputProvider` to supply the necessary input during testing:

```java
@Test
void testCommandExecutionWithReadingInput(@Autowired ShellTestClient client) throws Exception {
    // given
    ShellInputProvider inputProvider = ShellInputProvider.providerFor("ask").withInput("hi").build();

    // when
    ShellScreen screen = client.sendCommand(inputProvider);

    // then
    ShellAssertions.assertThat(screen).containsText("You said: hi");
}
```

<a id="testing--_end_to_end_testing"></a>
<a id="testing--end-to-end-testing"></a>

## End-to-End Testing

For end-to-end (ie black-box) testing of shell applications without using Spring Shell testing facilities, you can use the test utilities provided by Spring Boot. Once you have defined your Spring Boot application class, you can create a test class annotated with `@SpringBootTest` to test your shell commands. Here is an example:

```java
@SpringBootApplication public class MyShellApplication {
public static void main(String[] args) {SpringApplication.run(MyShellApplication.class, args);}
@Command public void hi() {System.out.println("Hello world!");}
}
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.NONE,useMainMethod = SpringBootTest.UseMainMethod.ALWAYS,classes = { MyShellApplication.class },properties = { "spring.shell.interactive.enabled=false" },args = "hi") @ExtendWith(OutputCaptureExtension.class) public class ShellApplicationEndToEndTests {
@Test void testCommandOutput(CapturedOutput output) {assertThat(output).contains("Hello world!");}
}
```

This example demonstrates how to run a Spring Shell application in a test context and verify the output of a command using Spring Boot’s `OutputCaptureExtension`.

The caveat with this approach is that it is not convenient for testing multiple commands in the same test class due to the fact that the command is passed through the `args` property of the `@SpringBootTest` annotation. For testing multiple commands, it is recommended to use the Spring Shell testing utilities as described in the previous sections. Here is an example of how to test multiple commands using the Spring Shell testing utilities:

```java
@SpringBootApplication
public class GreetingShellApplication {

	public static void main(String[] args) {
		SpringApplication.run(GreetingShellApplication.class, args);
	}

	@Command
	public void hi(CommandContext context) {
		context.outputWriter().println("Hello world!");
	}

	@Command
	public void bye(CommandContext context) {
		context.outputWriter().println("Goodbye world!");
	}

}

@ShellTest
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.NONE,
		useMainMethod = SpringBootTest.UseMainMethod.ALWAYS, classes = { GreetingShellApplication.class },
		properties = { "spring.shell.interactive.enabled=false" })
public class ShellApplicationEndToEndMultipleCommandsTests {

	@Test
	void testCommandExecution(@Autowired ShellTestClient client) throws Exception {
		// when
		ShellScreen shellScreen = client.sendCommand("help");

		// then
		ShellAssertions.assertThat(shellScreen).containsText("AVAILABLE COMMANDS");
	}

	@Test
	void testHiCommandExecution(@Autowired ShellTestClient client) throws Exception {
		// when
		ShellScreen shellScreen = client.sendCommand("hi");

		// then
		ShellAssertions.assertThat(shellScreen).containsText("Hello world!");
	}

	@Test
	void testByeCommandExecution(@Autowired ShellTestClient client) throws Exception {
		// when
		ShellScreen shellScreen = client.sendCommand("bye");

		// then
		ShellAssertions.assertThat(shellScreen).containsText("Goodbye world!");
	}

}
```

[Execution](#execution)
[Technical Introduction](#appendices-techintro)

---

<a id="appendices-techintro"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/techintro/index.html -->

<!-- page_index: 61 -->

<a id="appendices-techintro--page-title"></a>
<a id="appendices-techintro--technical-introduction"></a>

# Technical Introduction

This appendix contains information for developers and others who would like to know more about how Spring Shell
works internally and what its design decisions are.

<a id="appendices-techintro--section-summary"></a>

## Section Summary

- [Command Parser](#appendices-techintro-parser)
- [Command Execution](#appendices-techintro-execution)
- [Theming](#appendices-techintro-theming)
- [Search Algorithms](#appendices-techintro-searchalgorithm)

[Testing](#testing)
[Command Parser](#appendices-techintro-parser)

---

<a id="appendices-techintro-parser"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/techintro/parser.html -->

<!-- page_index: 62 -->

<a id="appendices-techintro-parser--page-title"></a>
<a id="appendices-techintro-parser--command-parser"></a>

# Command Parser

Before a command can be executed, we need to parse the command and whatever options the user may have provided. Parsing
comes between command registration and command execution.

[Technical Introduction](#appendices-techintro)
[Command Execution](#appendices-techintro-execution)

---

<a id="appendices-techintro-execution"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/techintro/execution.html -->

<!-- page_index: 63 -->

<a id="appendices-techintro-execution--page-title"></a>
<a id="appendices-techintro-execution--command-execution"></a>

# Command Execution

When command parsing has done its job and command registration has been resolved, command execution
does the hard work of running the code.

[Command Parser](#appendices-techintro-parser)
[Theming](#appendices-techintro-theming)

---

<a id="appendices-techintro-theming"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/techintro/theming.html -->

<!-- page_index: 64 -->

# Theming

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendices-techintro-theming--page-title"></a>
<a id="appendices-techintro-theming--theming"></a>

# Theming

Styling in a theming is provided by a use of a *AttributedString* from `JLine`.
Unfortunately styling in `JLine` is mostly undocumented but we try to go through
some of its features here.

In `JLine` a style spec is a string having a special format. Spec can be given
multiple times if separated by a comma. A spec will either define a color for
foreground, background or its mode. Special format `<spec>:=<spec>` allows to
define a default within latter spec if former for some reason is invalid.

If spec contains a colon its former part indicates either foreground or background
and possible values are `foreground`, `fg`, `f`, `background`, `bg`, `b`, `foreground-rgb`, `fg-rgb`, `f-rgb`, `background-rgb`, `bg-rgb` or `b-rgb`. Without rbg a color value
is name from an allowable colors `black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan` or `white`. Colors have their short formats `k`, `r`, `g`, `y`, `b`, `m`, `c` and `w`
respectively. If color is prefixed with either `!` or `bright-`, bright mode is automatically
applied. Prefixing with `~` will resolve from JLine internal bsd color table.

If rgb format is expected and prefixed with either `x` or `#` a normal
hex format is used.

```text
fg-red
fg-r
fg-rgb:red
fg-rgb:xff3333
fg-rgb:#ff3333
```

If spec contains special names `default`, `bold`, `faint`, `italic`, `underline`, `blink`, `inverse`, `inverse-neg`, `inverseneg`, `conceal`, `crossed-out`, `crossedout` or `hidden`
a style is changed accordingly with an existing color.

```text
bold
bold,fg:red
```

If spec is a number or numbers separated with semicolon, format is a plain part of an ansi
ascii codes.

```text
31
31;1
```

> [!NOTE]
> JLine special mapping format which would resolve spec starting with dot can’t be
> used as we don’t yet map those into Spring Shell styling names.

[Command Execution](#appendices-techintro-execution)
[Search Algorithms](#appendices-techintro-searchalgorithm)

---

<a id="appendices-techintro-searchalgorithm"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/techintro/searchalgorithm.html -->

<!-- page_index: 65 -->

# Search Algorithms

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="appendices-techintro-searchalgorithm--page-title"></a>
<a id="appendices-techintro-searchalgorithm--search-algorithms"></a>

# Search Algorithms

`SearchMatch` is an interface to match *text* with a *pattern*. Match
results are in a returned value `SearchMatchResult`. Match result
contains info about match positions and overall score of a match.

[fzf](https://github.com/junegunn/fzf).

<a id="appendices-techintro-searchalgorithm--implementations"></a>

## Implementations

**FuzzyMatchV2Search**

Port of *fzf FuzzyMatchV2Search* algorithm. Does a fast fuzzy search and is good
quickly finding paths.

**ExactMatchNaive**

Port of *fzf ExactMatchNaive* algorithm. Simple exact match works more accurately
if you know what to search.

<a id="appendices-techintro-searchalgorithm--searchmatch"></a>

## SearchMatch

Algorithms and default syntax are hidden inside package protected classes
as we don’t want to fully open these until we know API’s are good to go
for longer support. You need to construct `SearchMatch` via its
build-in builder.

```java
SearchMatch searchMatch = SearchMatch.builder().caseSensitive(false).normalize(false).forward(true).build();
```

It’s possible to configure *case sensitivity*, on what *direction* search
happens or if text should be *normilized* before search happens. Normalization
is handy when different languages have sligh variation for same type
of characters.

Search algorithm is selected based on a search syntax shown in
below table.

| Token | Match type | Description |
| --- | --- | --- |
| `hell` | fuzzy-match | Items that match `hello` |
| `'stuff` | exact-match | Items that include `stuff` |

<a id="appendices-techintro-searchalgorithm--examples"></a>

## Examples

```java
SearchMatch searchMatch = SearchMatch.builder().caseSensitive(false).normalize(false).forward(true).build();

SearchMatchResult result = searchMatch.match("foo bar baz", "fbb");

result.getStart();
// 0 - start position inclusive
result.getEnd();
// 9 - end position exclusive
result.getPositions();
// 0,4,8 - positions, inclusive
result.getScore();
// 112 - score
result.getAlgorithm();
// FuzzyMatchV2SearchMatchAlgorithm - resolved algo
```

[Theming](#appendices-techintro-theming)
[Debugging](#appendices-debugging)

---

<a id="appendices-debugging"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/debugging/index.html -->

<!-- page_index: 66 -->

<a id="appendices-debugging--page-title"></a>
<a id="appendices-debugging--debugging"></a>

# Debugging

Please find more info about debugging from [project wiki](https://github.com/spring-projects/spring-shell/wiki/Debugging).

[Search Algorithms](#appendices-techintro-searchalgorithm)
[Terminal UI](#appendices-tui)

---

<a id="appendices-tui"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/tui/index.html -->

<!-- page_index: 67 -->

<a id="appendices-tui--page-title"></a>
<a id="appendices-tui--terminal-ui"></a>

# Terminal UI

This is a technical introduction to the *UI Framework*.

The *UI Framework* is a toolkit to build rich console apps.

<a id="appendices-tui--section-summary"></a>

## Section Summary

- [View Development](#appendices-tui-viewdev)

[Debugging](#appendices-debugging)
[View Development](#appendices-tui-viewdev)

---

<a id="appendices-tui-viewdev"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/appendices/tui/viewdev.html -->

<!-- page_index: 68 -->

<a id="appendices-tui-viewdev--page-title"></a>
<a id="appendices-tui-viewdev--view-development"></a>

# View Development

While a *view* just needs to implement `View`, it’s usually convenient to just
use `BoxView` as a parent.

<a id="appendices-tui-viewdev--register-bindings"></a>

## Register Bindings

In an `AbstractView` use variants of *registerKeyBinding*, *registerHotKeyBinding*
and *registerMouseBinding*.

[Terminal UI](#appendices-tui)
[Javadoc](#api)

---

<a id="api"></a>

<!-- source_url: https://docs.spring.io/spring-shell/reference/api/index.html -->

<!-- page_index: 69 -->

<a id="api--spring-shell-4.0.2-api"></a>

# Spring Shell 4.0.2 API

Packages

Package

Description

[org.springframework.shell.core](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/package-summary.html)

Contains core classes for Spring Shell, irrespective of the way commands are actually
implemented.

[org.springframework.shell.core.autoconfigure](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/autoconfigure/package-summary.html)

[org.springframework.shell.core.command](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/command/package-summary.html)

[org.springframework.shell.core.command.adapter](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/command/adapter/package-summary.html)

[org.springframework.shell.core.command.annotation](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/command/annotation/package-summary.html)

[org.springframework.shell.core.command.annotation.support](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/command/annotation/support/package-summary.html)

[org.springframework.shell.core.command.availability](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/command/availability/package-summary.html)

[org.springframework.shell.core.command.completion](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/command/completion/package-summary.html)

[org.springframework.shell.core.command.exit](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/command/exit/package-summary.html)

[org.springframework.shell.core.config](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/config/package-summary.html)

[org.springframework.shell.core.utils](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/core/utils/package-summary.html)

[org.springframework.shell.jline](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/package-summary.html)

Contains classes that leverage the JLine library to hook into the Spring Shell REPL.

[org.springframework.shell.jline.command](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/command/package-summary.html)

[org.springframework.shell.jline.tui.component](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/package-summary.html)

[org.springframework.shell.jline.tui.component.context](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/context/package-summary.html)

[org.springframework.shell.jline.tui.component.flow](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/flow/package-summary.html)

[org.springframework.shell.jline.tui.component.message](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/message/package-summary.html)

[org.springframework.shell.jline.tui.component.support](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/support/package-summary.html)

[org.springframework.shell.jline.tui.component.view](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/view/package-summary.html)

[org.springframework.shell.jline.tui.component.view.control](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/view/control/package-summary.html)

[org.springframework.shell.jline.tui.component.view.control.cell](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/view/control/cell/package-summary.html)

[org.springframework.shell.jline.tui.component.view.event](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/view/event/package-summary.html)

[org.springframework.shell.jline.tui.component.view.event.processor](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/view/event/processor/package-summary.html)

[org.springframework.shell.jline.tui.component.view.screen](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/component/view/screen/package-summary.html)

[org.springframework.shell.jline.tui.geom](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/geom/package-summary.html)

[org.springframework.shell.jline.tui.style](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/style/package-summary.html)

[org.springframework.shell.jline.tui.support.search](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/support/search/package-summary.html)

[org.springframework.shell.jline.tui.table](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/jline/tui/table/package-summary.html)

Allows the creation of tables that can be rendered using ASCII art.

[org.springframework.shell.test](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/test/package-summary.html)

[org.springframework.shell.test.autoconfigure](https://docs.spring.io/spring-shell/reference/api/org/springframework/shell/test/autoconfigure/package-summary.html)

---
