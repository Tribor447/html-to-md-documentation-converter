# Project Information

## Navigation

- Commons Daemon
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Procrun](#procrun)
  - [Jsvc](#jsvc)
  - [Native binaries](#binaries)
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

<!-- source_url: https://commons.apache.org/proper/commons-daemon/index.html -->

<!-- page_index: 1 -->

<a id="index--introduction"></a>

# Introduction

Since 1994, the Java programming language evolved and became a
valid tool to develop reliable and performant server applications as
opposed to just applets and client applications. The major disadvantage of
the Java platform is that still today the only portable way to
start a Java application relies on a single point of entry: the
`public static void
main(String[])` method.

Having a single-point of entry is a valid solution for client
applications, where interactively a user can command to the application
to quit (which can terminate the Virtual Machine process at calling the
`System.exit(int)`
method), but in those cases where the application is not interactive
(server applications) there is currently no portable way to notify
the Virtual Machine of its imminent shutdown.

A server application written in Java might have to perform several tasks
before being able to shut down the Virtual Machine process. For example
in the case of a Servlet container, before the VM process is shut down, sessions might need to be serialized to disk, and web applications need
to be destroyed.

One common solution to this problem is to create (for example) a
`ServerSocket` and wait for a particular
message to be issued. When the message is received, all operations
required to shut down the server applications are performed and at the
end the `System.exit` method is called
to terminate the Virtual Machine process. This method however, has
several disadvantages and risks:

- In case of a system-wide shutdown, the Virtual Machine process may be
  shut down directly by the operating system without notifying the running
  server application.
- If an attacker finds out the shutdown message to send to the server
  and discovers a way to send this message, he can easily interrupt
  the server's operation, bypassing all the security restrictions
  implemented in the operating system.

Most multi-user operating systems already have a way in which server
applications are started and stopped. Under Unix based operating systems
non-interactive server applications are called *daemons* and are
controlled by the operating system with a set of specified
*signals*. Under Windows such programs are called *services*
and are controlled by appropriate calls to specific functions defined in
the application binary, but although the ways of dealing with the problem
are different, in both cases the operating system can notify a server
application of its imminent shutdown, and the application has the
ability to perform certain tasks before its process of execution is
destroyed.

<a id="index--structure"></a>

# Structure

Daemon is made of 2 parts. One written in C that makes the interface to
the operating system and the other in Java that provides the
Daemon API.

<a id="index--platforms"></a>

# Platforms

Both Win32 and UNIX like platforms are supported.
For Win32 platforms use [procrun](#procrun).
For UNIX like platforms use [jsvc](#jsvc).

<a id="index--initial-source-of-the-package"></a>

# Initial Source of the Package

The original Java classes came from the Jakarta Tomcat 4.0 project.

The package name for the Daemon component is
`org.apache.commons.daemon`.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-daemon.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-daemon.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-daemon.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/security.html -->

<!-- page_index: 3 -->

<a id="security--about-security"></a>

# About Security

For information about reporting or asking questions about security, please see
[Apache Commons Security](https://commons.apache.org/security.html).

This page lists all security vulnerabilities fixed in released versions of this component.

Please note that binary patches are never provided. If you need to apply a source code patch, use the building instructions for the component version
that you are using.

If you need help on building this component or other help on following the instructions to mitigate the known vulnerabilities listed here, please send
your questions to the public
[user mailing list](https://commons.apache.org/proper/commons-daemon/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

None.

<a id="security--safe-deserialization"></a>

# Safe Deserialization

For information about safe deserialization, please see [Safe Deserialization](https://commons.apache.org/io/description.html#Safe_Deserialization).

---

<a id="procrun"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/procrun.html -->

<!-- page_index: 4 -->

<a id="procrun--introduction"></a>

# Introduction

Procrun is a set of applications that allow Windows users to wrap
(mostly) Java applications (e.g. Tomcat) as a Windows service.
The service can be set to automatically start when the machine boots
and will continue to run with no user logged onto the machine.

<a id="procrun--procrun-monitor-application"></a>

# Procrun monitor application

**Prunmgr** is a GUI application for monitoring and configuring procrun
services.

Each command line directive is in the form of **//XX[//ServiceName]**

If the `//ServiceName` parameter is omitted, then the service name is
assumed to be the name of the file.
The Prunsrv application behaves in the same way, so to allow both applications to reside in the same directory, the Prunmgr application
will remove a trailing **w** (lower-case w) from the name.
For example if the Prunmgr application is renamed as `TestService.exe`
- or as `TestServicew.exe` -
then the default service name is `TestService`.

The available command line options are:

| //ES | Edit service configuration | This is the default operation. It is called if the no option is provided. Starts the GUI application which allows the service configuration to be modified, started and stopped. |
| --- | --- | --- |
| //MS | Monitor service | Starts the GUI application and minimizes it to the system tray. |
| //MR | Monitor & run service | Starts the GUI application and minimizes it to the system tray. Start the service if it is not currently running. |
| //MQ | Monitor Quit | Stop any running monitor for the service. |

<a id="procrun--procrun-service-application"></a>

# Procrun service application

**Prunsrv** is a service application for running applications as services.
It can convert any application (not just Java applications) to run as a service.

<a id="procrun--command-line-arguments"></a>

## Command line arguments

Each command line directive is in the form of **//XX[//ServiceName]**.

If the `//ServiceName` parameter is omitted, then the service name is
assumed to be the name of the file.
For example if the application is renamed as `TestService.exe`, then the default service name is `TestService`.

The available command line options are:

| //TS | Run the service as a console application | This is the default operation. It is called if the no option is provided. |
| --- | --- | --- |
| //RS | Run the service | Called only from ServiceManager |
| //ES | Start (execute) the service |  |
| //SS | Stop the service |  |
| //US | Update service parameters |  |
| //IS | Install service |  |
| //DS | Delete service | Stops the service first if it is currently running |
| //PS | Print service | Prints the command to (re-)create the current configuration |
| //PP[//seconds] | Pause | Default is 60 seconds |
| //VS | Version | Print version and exit (since version 1.0.3) |
| //? | Help | Print usage and exit (since version 1.0.3) |

Starting with version **1.0.8** a more traditional command line can
be used in the form: **command [ServiceName]**.

| run | Run the service as a console application | This is the default operation. It is called if the no option is provided and has the same effect as calling **//TS**. |
| --- | --- | --- |
| service | Run the service | Called only from ServiceManager |
| start | Start the service | Synonym for **//ES** |
| stop | Stop the service | Synonym for **//SS** |
| update | Update service parameters | Synonym for **//US** |
| install | Install service | Synonym for **//IS** |
| delete | Delete service | Stops the service first if it is currently running |
| print | Print service | Prints the command to (re-)create the current configuration |
| pause [seconds] | Pause | Default is 60 seconds |
| version | Version | Print version and exit |
| help | Help | Print usage and exit |

<a id="procrun--command-line-parameters"></a>

## Command line parameters

Each command parameter is prefixed with **--** (or **++**, see below).
If an environment variable exists with the same name as a command line parameter but
prefixed with `PR_` it will **override** the equivalent command line parameter.
For example:

```
set PR_CLASSPATH=xx.jar
```

is equivalent to providing

```
--Classpath=xx.jar
```

as a command line parameter.

If a parameter is repeated, then normally the last value takes precedence.
However some parameters can take multiple values - for example StartParams and JvmOptions.
If these parameters are prefixed with **++**, then the value will be appended to the existing value.
For example:

```

--Startup=manual --Startup=auto --JvmOptions=-Done=1 ++JvmOptions=-Dtwo=2
```

will result in the following values being used:

```

Startup:
auto

JvmOptions:
-Done=1
-Dtwo=2
```

Only multivalued parameters support this; they are indicated in the table below by **`++`**.
If **`++`** is used for a parameter that does not support multiple values, then it is treated the same as **`--`**. No error is reported.
Configuration is overwritten in case **`--`** is used.
For example:

```

--JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=4
```

will always overwrite the JvmOptions. The resulting configuration will be:

```

Startup:
auto

JvmOptions:
-Dthree=3
-Dfour=4
```

However if on **`++`** is used the values will be appended. For example calling the
following after the first example

```

++JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=2
```

will result in the following values being used:

```

Startup:
auto

JvmOptions:
-Done=1
-Dtwo=2
-Dthree=3
-Dfour=4
```

In case you intermix the **`++`** and **`--`** options, the
last **`--`** parameter will cause option reset. For example:

```

--Startup=manual --Startup=auto --JvmOptions=-Done=1 ++JvmOptions=-Dtwo=2 --JvmOptions=-Dthree=3 ++JvmOptions=-Dfour=2
```

will result in the following values being used:

```

Startup:
auto

JvmOptions:
-Dthree=3
-Dfour=4
```

When updating a service (//US or update command), using **`--`**
will replace any existing parameter with the new setting.
For multivalued parameters, using the **`++`** option qualifier
will add the new value(s) to any existing value(s).

<table class="bodyTable">
<tr>
<th>Parameter Name  </th>
<th>Default</th>
<th>Description</th>
</tr>
<tr>
<td>--Description</td>
<td></td>
<td>Service name description (maximum 1024 characters)</td>
</tr>
<tr>
<td>--DisplayName</td>
<td>ServiceName</td>
<td>Service display name</td>
</tr>
<tr>
<td>--Install</td>
<td>procrun.exe //RS//ServiceName</td>
<td>Install image</td>
</tr>
<tr>
<td>--Startup</td>
<td>manual</td>
<td>Service startup mode can be either delayed, auto or manual</td>
</tr>
<tr>
<td>--Type</td>
<td></td>
<td>Service type can be interactive to allow the service to interact with the desktop.
    This option can only be used with the LocalSystem account.</td>
</tr>
<tr>
<td>++DependsOn</td>
<td></td>
<td>List of services that this service depends on. Services are separated
        using either # or ; characters.

<p>
Note: At installation, additional dependencies will be created
        on the services Tcpip and Afd if not explicitly
        specified. These additional dependencies will not be created
        automatically when updating the service configuration with
        --DependsOn and must be explicitly defined if required in that
        case.
        </p>
</td>
</tr>
<tr>
<td>++Environment</td>
<td></td>
<td>List of environment variables that will be provided to the service
        in the form key=value. They are separated using either
        # or ; characters.
        If you need to embed either # or ; character within a value put them inside single quotes.
    </td>
</tr>
<tr>
<td>--User</td>
<td></td>
<td>User account used for running executable. It is used only for
        StartMode Java or exe and enables running applications
        as a service under an account without the LogonAsService privilege.</td>
</tr>
<tr>
<td>--Password</td>
<td></td>
<td>Password for user account set by --User parameter</td>
</tr>
<tr>
<td>--ServiceUser</td>
<td></td>
<td>Specifies the name of the account under which the service should run.
        Use an account name in the form DomainName\UserName.
        The service process will be logged on as this user.
        if the account belongs to the built-in domain, you can specify .\UserName
        Note that the Service Control Manager does not accept localised forms of
        the standard names so to use them you need to specify
        NT Authority\LocalService, NT Authority\NetworkService or
        LocalSystem as appropriate.
    </td>
</tr>
<tr>
<td>--ServicePassword</td>
<td></td>
<td>Password for user account set by --ServiceUser parameter</td>
</tr>
<tr>
<td>--LibraryPath</td>
<td></td>
<td>Directory added to the search path used to locate the DLLs for the JVM.
        This directory is added both in front of the PATH environment variable
        and as a parameter to the SetDLLDirectory function.
    </td>
</tr>
<tr>
<td>--JavaHome</td>
<td>JAVA_HOME</td>
<td>Set a different <strong>JAVA_HOME</strong> than defined by the <strong>JAVA_HOME</strong> environment
        variable.</td>
</tr>
<tr>
<td>--Jvm</td>
<td>auto</td>
<td>Use either auto (i.e. find the JVM from the Windows registry) or specify the full path to the jvm.dll.
        You can use environment variable expansion here. When auto is specified the following search order is used:

<ol>
<li>The current Java runtime library as defined in the registry</li>
<li>The current JRE as defined in the registry</li>
<li>The explicitly configured JavaHome for the service</li>
<li>The current JDK as defined in the registry</li>
</ol></td>
</tr>
<tr>
<td>++JvmOptions</td>
<td>-Xrs</td>
<td>List of options in the form of -D or -X that will be
        passed to the JVM. The options are separated using either
        # or ; characters. If you need to embed either # or ;
        character put them inside single quotes. (Not used in exe mode.)</td>
</tr>
<tr>
<td>++JvmOptions9</td>
<td></td>
<td>List of options in the form of -D or -X that will be
        passed to the JVM when running on Java 9 or later. The options are
        separated using either # or ; characters. If you need to
        embed either # or ; character put them inside single quotes.
        (Not used in exe mode.)</td>
</tr>
<tr>
<td>--Classpath</td>
<td></td>
<td>Set the Java classpath. (Not used in exe mode.)</td>
</tr>
<tr>
<td>--JvmMs</td>
<td></td>
<td>Initial memory pool size in MB. (Not used in exe mode.)</td>
</tr>
<tr>
<td>--JvmMx</td>
<td></td>
<td>Maximum memory pool size in MB. (Not used in exe mode.)</td>
</tr>
<tr>
<td>--JvmSs</td>
<td></td>
<td>Thread stack size in KB. (Not used in exe mode.)</td>
</tr>
<tr>
<td>--StartMode</td>
<td></td>
<td>One of jvm, Java or exe.
    The modes are:

<ul>
<li>jvm - start Java in-process. Depends on jvm.dll, see --Jvm.</li>
<li>Java - same as exe, but automatically uses the default Java executable, i.e. %JAVA_HOME%\bin\java.exe.
    Make sure JAVA_HOME is set correctly, or use --JavaHome to provide the correct location.
    If neither is set, procrun will try to find the default JDK (not JRE) from the Windows registry.</li>
<li>exe - run the image as a separate process</li>
</ul>
</td>
</tr>
<tr>
<td>--StartImage</td>
<td></td>
<td>Executable that will be run. Only applies to exe mode.</td>
</tr>
<tr>
<td>--StartPath</td>
<td></td>
<td>Working path for the start image executable.</td>
</tr>
<tr>
<td>--StartClass</td>
<td>Main</td>
<td>Class that contains the startup method.
    Applies to the jvm and Java modes.  (Not used in exe mode.)
    </td>
</tr>
<tr>
<td>--StartMethod</td>
<td>main</td>
<td>Name of method to be called when service is started.
    It must be <code>static void</code> and have argument <code>(String args[])</code>.
    Only applies to jvm mode - in Java mode, the main method is always used.


Note: in <code>jvm</code> mode, the start method should not return until the stop method
    has been called.
    </td>
</tr>
<tr>
<td>++StartParams</td>
<td></td>
<td>List of parameters that will be passed to either StartImage or
        StartClass. Parameters are separated using either # or
        ; character.</td>
</tr>
<tr>
<td>--StopMode</td>
<td></td>
<td>One of jvm, Java or exe.
    See --StartMode for further details.
    </td>
</tr>
<tr>
<td>--StopImage</td>
<td></td>
<td>Executable that will be run on Stop service signal. Only applies to exe mode.</td>
</tr>
<tr>
<td>--StopPath</td>
<td></td>
<td>Working path for the stop image executable. Does not apply to jvm mode.</td>
</tr>
<tr>
<td>--StopClass</td>
<td>Main</td>
<td>Class that will be used on Stop service signal.
    Applies to the jvm and Java modes.
    </td>
</tr>
<tr>
<td>--StopMethod</td>
<td>main</td>
<td>Name of method to be called when service is stopped.
    It must be <code>static void</code> and have argument <code>(String args[])</code>.
    Only applies to jvm mode.
    In Java mode, the main method is always used.
    </td>
</tr>
<tr>
<td>++StopParams</td>
<td></td>
<td>List of parameters that will be passed to either StopImage or
        StopClass. Parameters are separated using either # or
        ; character.</td>
</tr>
<tr>
<td>--StopTimeout</td>
<td>60 seconds</td>
<td>Defines the timeout in seconds that procrun waits for service
        to stop.
        The timeout applies to the stop command and to the time service needs to stop
        Negative values are not allowed.
        Note: Make sure you use a value big enough to give time for
        procrun to stop the service. Once the time out is elapsed,
        procrun will try to kill the whole process tree the service
        has created.</td>
</tr>
<tr>
<td>--LogPath</td>
<td>%SystemRoot%\System32\LogFiles\Apache</td>
<td>Defines the path for logging. Creates the directory if necessary.</td>
</tr>
<tr>
<td>--LogPrefix</td>
<td>commons-daemon</td>
<td>Defines the service log filename prefix. The log file is created in the LogPath directory with
    <code>.YEAR-MONTH-DAY.log</code> suffix</td>
</tr>
<tr>
<td>--LogLevel</td>
<td>Info</td>
<td>Defines the logging level and can be either Error, Warn
Info, Debug, or Trace. (Case insensitive). Note
        that for all log entries, the maximum length of the message component of
        the log entry is 4096 characters.
    </td>
</tr>
<tr>
<td>--LogJniMessages</td>
<td>0</td>
<td>Set this non-zero (e.g. 1) to capture JVM jni debug messages in the procrun log file.
    Is not needed if stdout/stderr redirection is being used.

    Only applies to jvm mode.
    </td>
</tr>
<tr>
<td>--StdOutput</td>
<td></td>
<td>Redirected stdout filename. If named auto file is created
    inside LogPath with the name service-stdout.YEAR-MONTH-DAY.log.</td>
</tr>
<tr>
<td>--StdError</td>
<td></td>
<td>Redirected stderr filename. If named auto file is created
    in the LogPath directory with the name service-stderr.YEAR-MONTH-DAY.log.</td>
</tr>
<tr>
<td>--PidFile</td>
<td></td>
<td>Defines the file name for storing the running process id.
    Actual file is created in the LogPath directory</td>
</tr>
</table>

<a id="procrun--installing-services"></a>

## Installing services

To install the service, you need to use the **//IS** parameter.

<a id="procrun--install-the-service-named-testservice"></a>

#### Install the service named 'TestService'

```

prunsrv //IS//TestService --DisplayName="Test Service" \
        --Install=prunsrv.exe --Jvm=auto --StartMode=jvm --StopMode=jvm \
        --StartClass=org.apache.SomeStartClass --StartParams=arg1;arg2;arg3 \
        --StopClass=org.apache.SomeStopClass --StopParams=arg1#arg2
```

<a id="procrun--updating-services"></a>

## Updating services

To update the service parameters, you need to use the **//US** parameter.

<a id="procrun--update-the-service-named-testservice"></a>

#### Update the service named 'TestService'

```

prunsrv //US//TestService --Description="Some Dummy Test Service" \
        --Startup=auto --Classpath=%CLASSPATH%;test.jar
```

<a id="procrun--removing-services"></a>

## Removing services

To remove the service, you need to use the **//DS** parameter.
If the service is running it will be stopped and then deleted.

<a id="procrun--remove-the-service-named-testservice"></a>

#### Remove the service named 'TestService'

```
prunsrv //DS//TestService
```

<a id="procrun--debugging-services"></a>

## Debugging services

To run the service in console mode, you need to use the **//TS** parameter.
The service shutdown can be initiated by pressing **CTRL+C** or
**CTRL+BREAK**.
If you rename the prunsrv.exe to testservice.exe then you can just execute the
testservice.exe and this command mode will be executed by default.

<a id="procrun--run-the-service-named-testservice-in-console-mode"></a>

#### Run the service named 'TestService' in console mode

```
prunsrv //TS//TestService [additional arguments]
```

<a id="procrun--using-procrun-in-jvm-mode"></a>

# Using Procrun in jvm mode

To interface with the Procrun service application (prunsrv) using the **jvm** mode, you need to create a class with the appropriate method(s).
For example:

```
class MyClass; // Error handling not shown static void main(String [] args){String mode = args[0]; if ("start".equals(mode){// process service start function} etc.}
```

This should be configured as follows:

```

--Classpath MyClass.jar
--StartMode jvm --StartClass MyClass --StartParams start
--StopMode  jvm --StopClass  MyClass --StopParams  stop
```

The above example uses a single 'main' method, and uses a string parameter to specify whether the service function
is start or stop.
Alternatively, you can use different method names for the service start and stop functions:

```
class MyClass; // Error handling not shown static void start(String [] args){// process service start function} static void stop(String [] args){// process service stop function}}
```

This should be configured as follows:

```

--Classpath MyClass.jar
--StartMode jvm --StartClass MyClass --StartMethod start
--StopMode  jvm --StopClass  MyClass --StopMethod  stop
```

Note: in jvm mode, the start method should not return until the stop method has
been called. The start and stop methods are called from different threads.

<a id="procrun--using-procrun-in-java-or-exe-mode"></a>

# Using Procrun in Java or exe mode

When using the **Java** or **exe** modes, the Procrun service application (prunsrv)
launches the target application in a separate process.
The "stop" application needs to communicate somehow with the "start" application to tell it to stop.
For example, using RPC.

<a id="procrun--windows-registry-usage"></a>

# Windows Registry Usage

The basic Service definitions are maintained under the registry key:

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\<ServiceName>
```

Additional parameters are stored in the registry at:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Apache Software Foundation\ProcRun 2.0\<ServiceName>\Parameters
```

On 64-bit Windows procrun always uses 32-bit registry view for storing the configuration.
This means that parameters will be stored inside:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Apache Software Foundation\ProcRun 2.0\<ServiceName>
```

---

<a id="jsvc"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/jsvc.html -->

<!-- page_index: 5 -->

<a id="jsvc--introduction"></a>

# Introduction

Jsvc is a set of libraries and applications for making Java
applications run on UNIX more easily.
Jsvc allows the application (e.g. Tomcat) to perform some privileged operations as root
(e.g. bind to a port < 1024), and then switch identity to a non-privileged user.
It can run on Win32 via the Cygwin emulation layer (see
 [Cygwin](https://www.cygwin.com/) for more information), however Win32 users may prefer to use  [procrun](#procrun)
instead, which allows the application to run as a Windows Service.

The sources are located in the src/native/unix subdirectory.

In the future  [APR](https://apr.apache.org/)  may be used
to provide more portable platform support.

<a id="jsvc--building-from-source"></a>

# Building from source

To build under a UNIX operating system you will need:

- GNU AutoConf (at least version 2.53)
- An ANSI-C compliant compiler (GCC is good)
- GNU Make
- A Java Platform 2 compliant SDK

You need to build the "configure" program with:

```

sh support/buildconf.sh
```

(Note it is possible to replace sh by any compatible shell like bash, ksh).
The result should be something like:

```

support/buildconf.sh
support/buildconf.sh: configure script generated successfully
```

Once the configure script is generated, follow the next section.

<a id="jsvc--building-from-a-release-tarball"></a>

# Building from a release tarball

To build the binary under a UNIX operating system you will need:

- An ANSI-C compliant compiler (GCC is good)
- GNU Make
- A Java Platform 2 compliant SDK

You have to specify the `JAVA_HOME` of the SDK
either with the `--with-java=<dir>` parameter or set the `JAVA_HOME` environment
to point to your SDK installation. For example:

```

./configure --with-java=/usr/java
```

or

```

export JAVA_HOME
./configure
```

If your operating system is supported, configure will go through cleanly, otherwise it will report an error (please send us the details of your
OS/JDK, or a patch against the sources). To build the binaries and
libraries simply do:

```

make
```

This will generate the executable file `jsvc`.

<a id="jsvc--starting-jsvc"></a>

# Starting jsvc

To check the allowed parameters for the jsvc binary simply do:

```

./jsvc -help
Usage: jsvc [-options] class [args...]

Where options include:

    -help | --help | -?
        show this help page (implies -nodetach)
    -jvm <JVM name>
        use a specific Java Virtual Machine. Available JVMs:
            'client' 'server'
    -client
        use a client Java Virtual Machine.
    -server
        use a server Java Virtual Machine.
    -cp / -classpath <directories and zip/jar files>
        set search path for service classes and resouces
    -home <directory>
        set the path of your JDK or JRE installation (or set
        the JAVA_HOME environment variable)
    -version
        show the current Java environment version (to check
        correctness of -home and -jvm. Implies -nodetach)
    -showversion
        show the current Java environment version (to check
        correctness of -home and -jvm) and continue execution.
    -nodetach
        don't detach from parent process and become a daemon
    -debug
        verbosely print debugging information
    -check
        only check service (implies -nodetach)
    -user <user>
        user used to run the daemon (defaults to current user)
    -verbose[:class|gc|jni]
        enable verbose output
    -cwd </full/path>
        set working directory to given location (defaults to /)
    -outfile </full/path/to/file>
        Location for output from stdout (defaults to /dev/null)
        Use the value '&2' to simulate '1>&2'
    -errfile </full/path/to/file>
        Location for output from stderr (defaults to /dev/null)
        Use the value '&1' to simulate '2>&1'
    -pidfile </full/path/to/file>
        Location for output from the file containing the pid of jsvc
        (defaults to /var/run/jsvc.pid)
    -D<name>=<value>
        set a Java system property
    -X<option>
        set Virtual Machine specific option
    -ea[:<packagename>...|:<classname>]
    -enableassertions[:<packagename>...|:<classname>]
        enable assertions
    -da[:<packagename>...|:<classname>]
    -disableassertions[:<packagename>...|:<classname>]
        disable assertions
    -esa | -enablesystemassertions
        enable system assertions
    -dsa | -disablesystemassertions
        disable system assertions
    -agentlib:<libname>[=<options>]
        load native agent library <libname>, e.g. -agentlib:hprof
    -agentpath:<pathname>[=<options>]
        load native agent library by full pathname
    -javaagent:<jarpath>[=<options>]
        load Java programming language agent, see java.lang.instrument
    -procname <procname>
        use the specified process name (works only for Linux and FreeBSD)
    -wait <waittime>
        wait waittime seconds for the service to start
        waittime should multiple of 10 (min=10)
    -restarts <maxrestarts>
        maximum automatic restarts (integer)
        -1=infinite (default), 0=none, 1..(INT_MAX-1)=fixed restart count
    -stop
        stop the service using the file given in the -pidfile option
    -keepstdin
        does not redirect stdin to /dev/null
    --add-modules=<module name>
        Java 9 --add-modules option. Passed as it is to JVM
    --module-path=<module path>
        Java 9 --module-path option. Passed as it is to JVM
    --upgrade-module-path=<module path>
        Java 9 --upgrade-module-path option. Passed as it is to JVM
    --add-reads=<module name>
        Java 9 --add-reads option. Passed as it is to JVM
    --add-exports=<module name>
        Java 9 --add-exports option. Passed as it is to JVM
    --add-opens=<module name>
        Java 9 --add-opens option. Passed as it is to JVM
    --limit-modules=<module name>
        Java 9 --limit-modules option. Passed as it is to JVM
    --patch-module=<module name>
        Java 9 --patch-module option. Passed as it is to JVM
    --illegal-access=<value>
        Java 9 --illegal-access option. Passed as it is to JVM. Refer java help for possible values.
    --enable-preview
        Java 11 --enable-preview option. Passed as it is to JVM
    --enable-native-access=<module name>
        Java 21 --enable-native-access option. Passed as it is to JVM
```

<a id="jsvc--mac-os-x-universal-binaries"></a>

## Mac OS X universal binaries

If jsvc was build with universal binary support the proper way of
starting `jsvc` is by using Mac OS X `arch` command:

```

    arch -arch i386 ./jsvc -jvm server <original jsvc parameters>

    for running 64-bit JVM use the:
    arch -arch x86_64 ./jsvc -jvm server <original jsvc parameters>
```

Use `-jvm server` because default `client` JVM is
not present for all architectures.

<a id="jsvc--using-jsvc"></a>

# Using jsvc

There two ways to use jsvc: via a Class that implements the Daemon interface or
via calling a Class that has the required methods.
For example Tomcat-4.1.x uses the Daemon interface
whereas Tomcat-5.0.x provides a Class whose methods are called by jsvc directly.

<a id="jsvc--via-daemon-interface"></a>

## Via Daemon interface

Do the following:

- Write a Class that implements the Daemon interface (MyClass).
- Put it in a jarfile (my.jar).
- Call jsvc like:

```

./jsvc -cp commons-daemon.jar:my.jar MyClass
  
```

<a id="jsvc--directly"></a>

## Directly

Write a Class (MyClass) that implements the following methods:

- void init(String[] arguments): Here open configuration files, create a trace file, create
  ServerSockets, Threads
- void start(): Start the Thread, accept incoming connections
- void stop(): Inform the Thread to terminate the run(), close the ServerSockets
- `void destroy()`: Destroy any object created in init()

Store it in a jarfile and use as above:

```

./jsvc -cp my.jar MyClass
```

<a id="jsvc--how-jsvc-works"></a>

# How jsvc works

Jsvc uses 3 processes: a launcher process, a controller process and a controlled process.
The controlled process is also the main java thread, if the JVM crashes
the controller will restart it in the next minute.
Jsvc is a daemon process so it should be started as root and the `-user` parameter
allows to downgrade to an unprivilegded user.
When the `-wait` parameter is used, the launcher process waits until the controller says
"I am ready", otherwise it returns after creating the controller process.

<a id="jsvc--forks-in-commons-daemon"></a>

## Forks in commons-daemon

Launcher process:

```

main()
{
  fork()
  parent: wait_child(), wait until JAVA service started when the child says "I am ready".
  child: controller process.
}
```

Controller process:

```

  while (fork()) {
    parent: wait_for_child.
      if exited and restart needed continue
      else exit.
    child: exit(child()). controlled process.
  }
```

Controlled process:

```

In child(): controlled process.
  init_JVM().
  load_service().
  start_service().
  say "I am ready"
  wait for signal or poll for stop
  stop_service().
  destroy_service().
  destroy_JVM().
  exit (with different codes so that parent knows if it has to restart us).
```

Note: The controller process uses signals to stop the controlled process.

<a id="jsvc--downgrading-user"></a>

## Downgrading user

On Linux `setuid()`/`setgid()` + capabilities are used. On other Unix `setgid`/`initgroups` are used.
We have something like:

```

/* as root */
init_JVM().
load_service. /*  java_load() calls the load method */
downgrade user (set_caps() or set_user_group())
/* as the user $USER (from -user $USER parameter) */
umask()
start_service. /* java_start() calls the start method */
```

---

<a id="binaries"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/binaries.html -->

<!-- page_index: 6 -->

<a id="binaries--what-to-download"></a>

# What to download?

In the directory
[binaries](https://downloads.apache.org/commons/daemon/binaries/)
you will find subdirectories containing archives
corresponding to your operating system. Only the Windows builds are provided as a zip file.

<a id="binaries--how-do-i-get-the-executable"></a>

# How do I get the executable?

<a id="binaries--procrun"></a>

## procrun

The Windows archive (e.g. commons-daemon-x.y.z-bin-windows.zip) contains 2 different executables:

- prunsrv.exe - service application for running applications as services.
- prunmgr.exe - the GUI manager application used to monitor and configure installed services.

There is only one `prunmgr.exe` application for all architectures.
The `prunsrv.exe` executable is available in 2 different versions for different architectures.
The version in the top-level directory is for 32-bit (x86) architectures.
The lower level directories are for AMD/EMT 64-bit systems. Itanium is no longer supported.

The Windows application `prunsrv.exe` is used to install an application as a service.
Once installed, `prunmgr.exe` can be used to monitor and reconfigure the service.
(see [procrun](#procrun) for more information).
The Windows binary zip archive should be unpacked into the location from which you wish to run it, for example:
`%ProgramFiles%\Apache Commons Daemon`

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/faq.html -->

<!-- page_index: 7 -->

<a id="faq--buildconf-problems"></a>

# Buildconf problems

```

$ sh support/buildconf.sh autoconf: Undefined macros:***BUG in Autoconf--please report*** AC_PATH ***BUG in Autoconf--please report*** AC_PATH ***BUG in Autoconf--please report*** AC_PATH
```

Your version of autoconf is too old, upgrade your autoconf and retry.
Or run support/buildconf.sh in another machine and copy the daemon tree in
the machine where you want to compile jsvc.

<a id="faq--configure-problems"></a>

# Configure problems

```

configure: creating ./config.status
config.status: creating Makefile
mv: Makefile: set owner/group (was: 1670/0): Operation not permitted
config.status: creating Makedefs
mv: Makedefs: set owner/group (was: 1670/0): Operation not permitted
config.status: creating native/Makefile
mv: native/Makefile: set owner/group (was: 1670/0): Operation not permitted
*** All done ***
Now you can issue "make"
```

You should ignore those error messages they are normal in FreeBSD.
config.status creates files in /tmp and move them in the current directory.
When FreeBSD creates files it sets the group of the files to
the group of the directory where the files are created.
So if /tmp is group "wheel" the files are "wheel". When moving the files in
the current directory (if you are not member of group "wheel")
the group "wheel" cannot be set on the moved files.

<a id="faq--runtime-problems"></a>

# Runtime problems

On Linux 2.6.x jsvc does not start and write the following error:

```

jsvc.exec error: syscall failed in set_caps
jsvc.exec error: Service exit with a return value of 4
```

CONFIG\_SECURITY\_CAPABILITIES in missing in your kernel try the following in the kernel sources:

- Configure the kernel with "Default Linux Capabilities" and reboot
  (by make gconfig or make xconfig under "security options" and "Enable different security models")
- Insert the module "capability":

```

modprobe capability
```

<a id="faq--cygwin-configuration-problems"></a>

# Cygwin configuration problems

The configure of jsvc does not like spaces in directory name.
To configure with java installed in directory whose name contains a space, use the 8 characters name of the directory.
For example for java in installed in `c:\Archivos de programa\java\jdk1.5.0_06`:

```

./configure --with-java=/cygdrive/c/Archiv~1/java/jdk1.5.0_06
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/project-info.html -->

<!-- page_index: 8 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Daemon software is a set of utilities and Java support classes for running Java applications as server processes. These are commonly known as 'daemon' processes in Unix terminology (hence the name). On Windows they are called 'services'. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-daemon/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-daemon/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-daemon/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-daemon/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-daemon/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-daemon/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-daemon/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/summary.html -->

<!-- page_index: 9 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Daemon |
| Description | Apache Commons Daemon software is a set of utilities and Java support classes for running Java applications as server processes. These are commonly known as 'daemon' processes in Unix terminology (hence the name). On Windows they are called 'services'. |
| Homepage | [https://commons.apache.org/proper/commons-daemon/](#index) |

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
| GroupId | commons-daemon |
| ArtifactId | commons-daemon |
| Version | 1.6.0 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/team.html -->

<!-- page_index: 10 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg) | jfclere | Jean-Frederic Clere | [jfclere at apache.org](mailto:jfclere at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg) | remm | Remy Maucherat | [remm at apache.org](mailto:remm at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg) | yoavs | Yoav Shapira | [yoavs at apache.org](mailto:yoavs at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg) | billbarker | Bill Barker | [billbarker at apache.org](mailto:billbarker at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg) | mturk | Mladen Turk | [mturk at apache.org](mailto:mturk at apache.org) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_c020dfa6fffc44c4.jpg) | pier | Pier Fumagalli | [pier at apache.org](mailto:pier at apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/b7540f73db192bd34c6880a272d78612_1e0c169e26914241.jpg) | Nick Griffiths | [nicobrevin@gmail.com](mailto:nicobrevin@gmail.com) |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-daemon/ci-management.html -->

<!-- page_index: 11 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-daemon/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
