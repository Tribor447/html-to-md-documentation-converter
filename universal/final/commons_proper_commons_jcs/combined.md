# JCS – Project Information

## Navigation

- JCS
  - [Overview](#index)
  - [JCS and JCACHE](#jcsandjcache)
  - [FAQ](#faq)
- Development
  - [Upgrading from 1.3 to 2.0](#upgradingfrom13)
  - [Upgrading from 2.x to 3.0](#upgradingfrom2x)
  - [Issue Tracking](#issue-tracking)
  - [Source Repository](#scm)
- Getting Started
  - [Overview](#getting_started-intro)
  - [Basic JCS Config](#basicjcsconfiguration)
  - [Plugin Overview](#jcsplugins)
  - [Basic Web Example](#usingjcsbasicweb)
- JCS User's Guide
  - [Core](#localcacheconfig)
    - [Basic JCS Config](#basicjcsconfiguration)
    - [Element Config](#elementattributes)
    - [Element Event Handling](#elementeventhandling)
    - [Region Properties](#regionproperties)
    - [Basic Web Example](#usingjcsbasicweb)
    - [Project History](#projecthistory)
  - [Auxiliary](#jcsplugins)
    - [Cache Event Logging](#cacheeventlogging)
    - [Element Serializers](#elementserializers)
    - [Indexed Disk Cache](#indexeddiskauxcache)
    - [Indexed Disk Properties](#indexeddiskcacheproperties)
    - [Block Disk Cache](#blockdiskcache)
    - [JDBC Disk Cache](#jdbcdiskcache)
    - [JDBC Disk Properties](#jdbcdiskcacheproperties)
    - [MySQL Disk Properties](#mysqldiskcacheproperties)
    - [Remote Cache](#remoteauxcache)
    - [Remote Cache Properties](#remotecacheproperties)
    - [Remote Http Cache Properties](#remotehttpcacheproperties)
    - [Lateral TCP Cache](#lateraltcpauxcache)
    - [Lateral TCP Properties](#lateraltcpproperties)
    - [Lateral UDP Discovery](#lateraludpdiscovery)
- Modules
  - [Apache Commons JCS :: Core](#commons-jcs3-core)
  - [Apache Commons JCS :: JCache](#commons-jcs3-jcache)
  - [Apache Commons JCS :: JCache TCK](#commons-jcs3-jcache-tck)
  - [Apache Commons JCS :: JCache Extras](#commons-jcs3-jcache-extras)
  - [Apache Commons JCS :: JCache OpenJPA](#commons-jcs3-jcache-openjpa)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Project Modules](#modules)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Other pages
  - [JCS – JCS vs EHCache Performance](#jcsvsehcache)
  - [Apache Commons JCS :: Core – CI Management](#commons-jcs3-core-ci-management)
  - [Apache Commons JCS :: Core – Source Code Management](#commons-jcs3-core-scm)
  - [Apache Commons JCS :: Core – Project Summary](#commons-jcs3-core-summary)
  - [Apache Commons JCS :: Core – Project Team](#commons-jcs3-core-team)
  - [Apache Commons JCS :: JCache Extras – CI Management](#commons-jcs3-jcache-extras-ci-management)
  - [Apache Commons JCS :: JCache Extras – Source Code Management](#commons-jcs3-jcache-extras-scm)
  - [Apache Commons JCS :: JCache Extras – Project Summary](#commons-jcs3-jcache-extras-summary)
  - [Apache Commons JCS :: JCache Extras – Project Team](#commons-jcs3-jcache-extras-team)
  - [Apache Commons JCS :: JCache OpenJPA – CI Management](#commons-jcs3-jcache-openjpa-ci-management)
  - [Apache Commons JCS :: JCache OpenJPA – Source Code Management](#commons-jcs3-jcache-openjpa-scm)
  - [Apache Commons JCS :: JCache OpenJPA – Project Summary](#commons-jcs3-jcache-openjpa-summary)
  - [Apache Commons JCS :: JCache OpenJPA – Project Team](#commons-jcs3-jcache-openjpa-team)
  - [Apache Commons JCS :: JCache TCK – CI Management](#commons-jcs3-jcache-tck-ci-management)
  - [Apache Commons JCS :: JCache TCK – Source Code Management](#commons-jcs3-jcache-tck-scm)
  - [Apache Commons JCS :: JCache TCK – Project Summary](#commons-jcs3-jcache-tck-summary)
  - [Apache Commons JCS :: JCache TCK – Project Team](#commons-jcs3-jcache-tck-team)
  - [Apache Commons JCS :: JCache – CI Management](#commons-jcs3-jcache-ci-management)
  - [Apache Commons JCS :: JCache – Source Code Management](#commons-jcs3-jcache-scm)
  - [Apache Commons JCS :: JCache – Project Summary](#commons-jcs3-jcache-summary)
  - [Apache Commons JCS :: JCache – Project Team](#commons-jcs3-jcache-team)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/index.html -->

<!-- page_index: 1 -->

<a id="index--java-caching-system"></a>

## Java Caching System

JCS is a distributed caching system written in Java. It is intended
to speed up applications by providing a means to manage cached data
of various dynamic natures. Like any caching system, JCS is
[most useful](#usingjcsbasicweb)
for high read, low put applications. Latency times drop sharply and
bottlenecks move away from the database in an effectively cached
system.
[Learn how to start using JCS.](#getting_started-intro)

The JCS goes beyond simply caching objects in memory. It provides
numerous additional features:

- Memory management
- Disk overflow (and defragmentation)
- Thread pool controls
- Element grouping
- Minimal dependencies
- Quick nested categorical removal
- Data expiration (idle time and max life)
- Extensible framework
- Fully configurable runtime parameters
- Region data separation and configuration
- Fine grained element configuration options
- Remote synchronization
- Remote store recovery
- Non-blocking "zombie" (balking facade) pattern
- Lateral distribution of elements via HTTP, TCP, or UDP
- UDP Discovery of other caches
- Element event handling
- Remote server chaining (or clustering) and failover
- Custom event logging hooks
- Custom event queue injection
- Custom object serializer injection
- Key pattern matching retrieval
- Network efficient multi-key retrieval

JCS 3.x works on JDK versions 1.8 and up. It has no
mandatory external dependencies. See the document about
[upgrading](#upgradingfrom2x).

JCS 2.x works on JDK versions 1.6 and up. It only has a
dependency on Commons Logging. See the document about
[upgrading](#upgradingfrom13).

<a id="index--jcs-is-a-composite-cache"></a>

## JCS is a Composite Cache

The foundation of JCS is the Composite Cache, which is the
[pluggable](#jcsplugins)
controller for a cache region. Four types of caches can be plugged
into the Composite Cache for any given region: (1) Memory, (2) Disk, (3) Lateral, and (4) Remote. The Composite Cache orchestrates access
to the various caches configured for use in a region.

The JCS jar provides production ready implementations of each of
the four types of caches. In addition to the core four, JCS also
provides additional plugins of each type.

<a id="index--lru-memory-cache"></a>

### LRU Memory Cache

The LRU Memory Cache is an extremely fast, highly configurable
 [memory cache](#regionproperties)
. It uses a Least Recently Used algorithm to manage the number of
items that can be stored in memory. The LRU Memory Cache uses its
own LRU Map implementation that is significantly faster than both
the commons LRUMap implementation and the LinkedHashMap that is
provided with JDK1.4 up. This makes JCS faster than its
[competitors](#jcsvsehcache)
.

<a id="index--indexed-disk-cache"></a>

### Indexed Disk Cache

The
[Indexed Disk Cache](#indexeddiskauxcache)
is a fast, reliable, and
 [highly configurable](#indexeddiskcacheproperties)
swap for cached data. The indexed disk cache follows the fastest
pattern for disk swapping. Cache elements are written to disk via a
continuous queue-based process. The length of the item is stored in
the first few bytes of the entry. The offset is stored in memory
and can be reference via the key. When items are removed from the
disk cache, the location and size are recorded and reused when
possible. Every aspect of the disk cache is configurable, and a
thread pool can be used to reduce the number of queue worker
threads across the system.

<a id="index--jdbc-disk-cache"></a>

### JDBC Disk Cache

The
[JDBC Disk Cache](#jdbcdiskcache)
is a fast, reliable, and
 [highly configurable](#jdbcdiskcacheproperties)
disk cache. It stores both the keys and elements in a JDBC
compatible database. The JDBC disk cache stores elements in
a database as BLOBs. Periodically, the table is swept to remove
expired elements. Multiple instances can be configured to use a
common connection pool. A thread pool can be used to reduce the
number of queue worker threads across the system. The
[MySQL version of the JDBC Disk Cache](#mysqldiskcacheproperties)
can optimize and repair tables.

<a id="index--tcp-lateral-cache"></a>

### TCP Lateral Cache

The
[TCP Lateral Cache](#lateraltcpauxcache)
provides an easy way to distribute cached data to multiple servers.
It comes with a
[UDP discovery](#lateraludpdiscovery)
mechanism, so you can add nodes without having to reconfigure the
entire farm. The TCP Lateral Cache works by establishing
connections with socket server running on other nodes. Each node
maintains a connection to every other. Only one server is needed
for any number of regions. The client is able to re-establish
connections if it looses its connection with another server. The
TCP Lateral is
 [highly configurable](#lateraltcpproperties)
. You can choose to only send data, to not look for data on other
servers, to send removes instead of puts, and to filter removes
based on hash codes.

<a id="index--rmi-remote-cache"></a>

### RMI Remote Cache

JCS also provides an RMI based
[Remote Cache Server](#remoteauxcache)
. Rather than having each node connect to every other node, you can
use the remote cache server as the connection point. Each node
connects to the remove server, which then broadcasts events to the
other nodes. To maintain consistency across a cluster without
incurring the overhead of serialization, you can decide to send
invalidation messages to the other locals rather than send the
object over the wire. The remote cache server holds a serialized
version of your objects, so it does not need to be deployed with
your class libraries. The remote servers can be chained and a list
of failover servers can be configured on the client.

<a id="index--what-jcs-is-not"></a>

## What JCS is not

JCS is not a tag library or a web specific application. JCS is a
general purpose caching system that can be used in web applications, services, and stand alone Java applications.

JCS is not a transactional distribution mechanism. Transactional
distributed caches are not scalable. JCS is a cache not a database.
The distribution mechanisms provided by JCS can scale into the tens
of servers. In a well-designed service oriented architecture, JCS
can be used in a high demand service with numerous nodes. This would
not be possible if the distribution mechanism were transactional.

JCS does not use AOP. JCS is a high performance, non-invasive
cache. It does not manipulate your objects so it can just send a
field or two fewer over the wire.

JCS is not a fork, an offshoot, a branch, or any other derivation
of JCS. Nor is JCS named after another library. JCS is a mature
project that has been under development and in use since 2001. Over
the years JCS has incorporated numerous bug fixes and has added
dozens of features, making it the best designed and most feature
rich caching solution available.

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jcsandjcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/JCSandJCACHE.html -->

<!-- page_index: 2 -->

<a id="jcsandjcache--jcache-jsr-107"></a>

## JCACHE (JSR-107)

Since version 2.x, Apache Commons JCS implements
JCache specification (and a few more providing some basic utilities
in its extras module and a basic integration with Apache OpenJPA).

The next section is about the main differences between the JCache design and the original JCS one.
These are still globally valid and are kept to let you get a bit more food for thoughts
on Caching and JCS.

<a id="jcsandjcache--jcs-and-jcache-jsr-107"></a>

## JCS and JCACHE (JSR-107)

The JCS is an attempt to build a system close to JCACHE , [JSR-107](http://jcp.org/jsr/detail/107.jsp), a
description of the caching system used in Oracle9i. JCS grew
out of my work over the past two years to build an enterprise
level caching system. Though it is replete with good ideas, there are some aspects of the JCACHE architecture that could
lead to inefficiency (ex, the lateral distribution and net
searches) and a few programming preferences that I found
cumbersome (ex, the use of exceptions to report the common
place). Subsequently there are a few differences between the
two systems. In some cases I have moved my original system
closer to the JCACHE model where it presented a better idea.
Briefly:

<a id="jcsandjcache--element-vs.-region-attributes"></a>

### Element vs. Region Attributes

My original cache was regionally defined. Each entry required
a very minimal wrapper. The osc4j specification is an element
driven model where each element is fully configurable. This
could lead to a slight performance penalty, but it is a richer
model, where elements can inherit or have their own
attributes. So, I converted the entire system into element
centered framework.

<a id="jcsandjcache--lateral-broadcast-vs.-remote-consistency"></a>

### Lateral Broadcast vs. Remote Consistency

The oracle model is a laterally distributed framework with no
centralized control. The JCS model has the option for lateral
broadcast (which will need to be made more efficient) and a
remote store that coordinates consistency. In the JCS Local
caches send data to the remote store which then notifies other
local caches of changes to "regions" (caches) that are
registered. In JCACHE's lateral model an update is never
broadcast from the remote, rather updates come via the lateral
caches. If you broadcast changes to all servers then every
server must be ready for every user. The usage patterns of a
user on one box can affect the whole. Also, the lateral model
can make it difficult to synchronize combinations of updates
and invalidations.

With a remote store the local caches are primed to take on
similar patterns by talking to the remote store, but aren't
flooded with the elements from another machine. This
significantly cuts down on traffic. This way each local cache
is a relatively separate realm with remotely configurable
regions that stay in synch without overriding the user habits
of any machine. It also allows for an efficient mechanism of
retrieval, where searching for an element involves, at
maximum, only as many steps as there are remote servers in the
cluster. In the lateral model a failed net search could take
an extremely long time to complete, making it necessary for
the programmer to decide how long of a wait is acceptable.

Though this is by and large a poor model, the JCS will include
the ability to perform full lateral searches. A more
important feature is remote failover and remote server
clustering. With clustering any concerns about the remote
server being a single point of failure vanish and the remote
server model is significantly more robust.

<a id="jcsandjcache--put-vs.-replace"></a>

### Put vs. Replace

The difference between put and replace is not present in the
JCS by default. The overhead associated with this distinction
is tremendous. However, there will be an alternate "safe-put"
method to deal with special caches.

<a id="jcsandjcache--nulls-vs.-errors"></a>

### Nulls vs. Errors

I started to support `ObjectNotFoundExceptions` for
failed gets but the overhead and cumbersome coding needed to
surround a simple get method is ridiculous. Instead the JCS
returns null.

<a id="jcsandjcache--cache-loaders"></a>

### Cache Loaders

I'm not supporting cache loaders at this time. They seem
unnecessary, but may be useful in a smart portal.

<a id="jcsandjcache--groups-vs.-hierarchy"></a>

### Groups vs. Hierarchy

The JCS provides feature rich grouping mechanism, where groups
of elements can be invalidated and whose attributes can be
listed. The grouping feature is much like the session API.
In addition, the JCS provides a mechanism for hierarchical
removal without the overhead of keeping track of all the
elements of a group across machines. Element keys with
"`:`" separators (a value that will be fully
configurable) can be arranged in a hierarchy. A remove
command ending in a "`:`" will issue a removal of
all child elements. I can associate search and menu drop down
lists for a particular company in a multi-company system by
starting each key in disparate caches with the company id
followed by "`:`" and then the normal key.
Invalidating this data when a change is made to data affecting
something falling under that company can be removed by simply
calling `cacheAccess.remove(comp_id + ":")`.

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="faq"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/faq.html -->

<!-- page_index: 3 -->

# JCS – Frequently Asked Questions

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="upgradingfrom13"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/UpgradingFrom13.html -->

<!-- page_index: 4 -->

<a id="upgradingfrom13--upgrading-from-jcs-1.3-to-2.0"></a>

## Upgrading from JCS 1.3 to 2.0

This document lists a number of things that changed in Commons JCS
2.0.

<a id="upgradingfrom13--package-names-and-maven-coordinates"></a>

### Package Names and Maven Coordinates

The main difference is the move to the Apache Commons project
which lead to the change of the package names and Maven coordinates.
So in all your code replace

```

import org.apache.jcs.*;
```

with

```

import org.apache.commons.jcs.*;
```

The Maven coordinates change from

```

<dependency>
    <groupId>org.apache.jcs</groupId>
    <artifactId>jcs</artifactId>
    <version>1.3</version>
</dependency>
```

to

```

<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-jcs-core</artifactId>
    <version>2.0</version>
</dependency>
```

<a id="upgradingfrom13--change-cache-access-object"></a>

### Change Cache Access Object

JCS now uses different cache access objects depending on
if you want to use cache groups or not. This was necessary
because the cache access objects are now generic which saves
you all the casts but doesn't allow different objects in the
same cache anymore. You now use

```

import org.apache.commons.jcs.JCS;
import org.apache.commons.jcs.access.CacheAccess;
import org.apache.commons.jcs.access.GroupCacheAccess;

CacheAccess<String, City> cityCache = JCS.getInstance( "city" );
GroupCacheAccess<String, Country> countryCache = JCS.getGroupCacheInstance( "country" );
```

<a id="upgradingfrom13--adjusting-the-configuration"></a>

### Adjusting the Configuration

Here again, change all package names in configuration entries
from e.g.

```

jcs.default.cacheattributes=org.apache.jcs.engine.CompositeCacheAttributes
```

to

```

jcs.default.cacheattributes=org.apache.commons.jcs.engine.CompositeCacheAttributes
```

and all `MaxLifeSeconds` lines to `MaxLife`
like

```

jcs.default.elementattributes.MaxLifeSeconds=7
```

to

```

jcs.default.elementattributes.MaxLife=7
```

The `IndexedDiskCache` recycle bin is no longer limited in size.
So remove all references to `MaxRecycleBinSize` from the configuration files.

---

<a id="upgradingfrom2x"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/UpgradingFrom2x.html -->

<!-- page_index: 5 -->

<a id="upgradingfrom2x--upgrading-from-jcs-2.x-to-3.0"></a>

## Upgrading from JCS 2.x to 3.0

This document lists a number of things that changed in Commons JCS
3.0.

<a id="upgradingfrom2x--minimum-java-requirements"></a>

### Minimum Java Requirements

JCS 3.x requires Java 8 to run. It was tested successfully with JDK 14.

<a id="upgradingfrom2x--package-names-and-maven-coordinates"></a>

### Package Names and Maven Coordinates

The Apache Commons project requires a change of the package names
and Maven coordinates on a major release.
So in all your code replace

```

import org.apache.commons.jcs.*;
```

with

```

import org.apache.commons.jcs3.*;
```

The Maven coordinates change from

```

<dependency>
    <groupId>org.apache.commons.jcs</groupId>
    <artifactId>commons-jcs-core</artifactId>
    <version>2.2.1</version>
</dependency>
```

to

```

<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-jcs3-core</artifactId>
    <version>3.0</version>
</dependency>
```

<a id="upgradingfrom2x--adjusting-the-configuration"></a>

### Adjusting the Configuration

Here again, change all package names in configuration entries
from e.g.

```

jcs.default.cacheattributes=org.apache.commons.jcs.engine.CompositeCacheAttributes
```

to

```

jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
```

<a id="upgradingfrom2x--logging-abstraction"></a>

### Logging Abstraction

JCS 3.0 uses its own log abstraction layer. As newer and better
log systems become available, JCS is no longer limited to
commons-logging. As a result, JCS now uses java.util.logging as
default and does not depend on commons-logging anymore.

Optionally, JCS can use Log4j2 as a log system. You can activate
it by providing log4j-core as a dependency, a log configuration
such as log4j2.xml and a system property

```

-Djcs.logSystem=log4j2
```

As log initialization occurs very early in the startup process, be sure to add this property before accessing any of JCS' classes.

JCS uses the Java SPI mechanism to find its log systems. If you want
to roll your own, you will need to implement a
`org.apache.commons.jcs.log.Log` object and a
`org.apache.commons.jcs.log.LogFactory`
and provide the implementation class in a text file
`META-INF/services/org.apache.commons.jcs.log.LogFactory`
in your code. Choose a name for your log system and activate it via
the system property as described above.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/issue-tracking.html -->

<!-- page_index: 6 -->

<a id="issue-tracking--apache-commons-jcs-issue-tracking"></a>

## Apache Commons JCS Issue tracking

Apache Commons JCS uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons JCS JIRA project page](https://issues.apache.org/jira/browse/JCS).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons JCS please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=${commons.jira.pid}&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-jcs/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=${commons.jira.pid}&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=${commons.jira.pid}&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons JCS are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons JCS bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=${commons.jira.pid}&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons JCS bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=${commons.jira.pid}&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons JCS bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=${commons.jira.pid}&sorter/field=issuekey&sorter/order=DESC)

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/scm.html -->

<!-- page_index: 7 -->

<a id="scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-jcs.git
```

<a id="scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch commons-jcs3-3.2.1-rc3 http://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch commons-jcs3-3.2.1-rc3 https://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="getting_started-intro"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/getting_started/intro.html -->

<!-- page_index: 8 -->

<a id="getting_started-intro--getting-started"></a>

## Getting Started

To start using JCS you need to (1) understand the core
concepts, (2) download JCS, (3) get the required
dependencies, (4) configure JCS, and (5) then start
programming to it. The purpose of the getting started
guide is to help you get up and running with JCS as
quickly as possible. In depth documentation on the
various features of JCS is provided in the User's Guide.

<a id="getting_started-intro--step-1:-understand-the-core-concepts"></a>

## STEP 1: Understand the Core Concepts

In order to use JCS, you must understand a few core
concepts, most importantly you need to know the
difference between "elements," "regions," and
"auxiliaries".

JCS is an object cache. You can put objects, or
"elements," into JCS and reference them via a key, much
like a hashtable.

You can think of JCS as a collection of maps that
you reference by name. Each of these maps is
called a "region," and each region can be configured
independently of the others. For instance, I may have a
region called Cities where I cache City objects that
change infrequently. I may also define a region called
Products where I cache product data that changes more
frequently. I would configure the volatile Product
region to expire elements more quickly than the City
region.

"Auxiliaries" are optional plugins that a region can
use. The core auxiliaries are the Indexed Disk Cache, the TCP Lateral Cache, and the Remote Cache Server. The
Disk Cache, for example, allows you to swap items onto
disk when a memory threshold is reached. You can read
more about the available auxiliaries
[HERE](#jcsplugins)
.

<a id="getting_started-intro--step-2:-download-jcs"></a>

## STEP 2: Download JCS

Download the latest version of JCS. The latest JCS
builds are located
[HERE](http://www.apache.org/dist/commons/jcs/)

If you would like to build JCS yourself, check it out
from Subversion and build it as you would any other
project built by Maven. The location of the
repository is documented in the project info pages that
are linked via the left nav.

<a id="getting_started-intro--step-3:-get-the-required-dependencies"></a>

## STEP 3: Get the Required Dependencies

Beginning with version 2.0 the core of JCS (the LRU memory
cache, the indexed disk cache, the TCP lateral, and the
RMI remote server) requires only commons-logging.

Beginning with version 1.2.7.0 and up to version 1.3, the core of
JCS (the LRU memory
cache, the indexed disk cache, the TCP lateral, and the
RMI remote server) requires only two other jars.

[concurrent](http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/util/concurrent/intro.html)

commons-logging

Versions 1.2.6.9 and below also require the following
two additional jars:

commons-collections

commons-lang

All of the other dependencies listed on the project info
page are for optional plugins.

<a id="getting_started-intro--step-4:-configure-jcs"></a>

## STEP 4: Configure JCS

JCS is configured from a properties file called
"cache.ccf". There are alternatives to using this file, but they are beyond the scope of the getting started
guide.

The cache configuration has three parts: default, regions, and auxiliaries. You can think of the
auxiliaries as log4j appenders and the regions as log4j
categories. For each region (or category) you can
specify and auxiliary (or appender to use). If you don't
define a region in the cache.ccf, then the default
settings are used. The difference between JCS and log4j
is that in JCS, pre-defined regions do not inherent
auxiliaries from the default region.

The following cache.ccf file defines one region called
"testCache1" and uses the Indexed Disk Cache, here
called "DC" by default. The LRU Memory Cache is selected
as the memory manager.

```

                
# DEFAULT CACHE REGION
jcs.default=DC
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=1000
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.cacheattributes.UseMemoryShrinker=false
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=21600
jcs.default.elementattributes.IdleTime=1800
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true

# PRE-DEFINED CACHE REGIONS
jcs.region.testCache1=DC
jcs.region.testCache1.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.testCache1.cacheattributes.MaxObjects=1000
jcs.region.testCache1.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.region.testCache1.cacheattributes.UseMemoryShrinker=false
jcs.region.testCache1.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.region.testCache1.cacheattributes.ShrinkerIntervalSeconds=60
jcs.region.testCache1.cacheattributes.MaxSpoolPerRun=500
jcs.region.testCache1.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.region.testCache1.elementattributes.IsEternal=false

# AVAILABLE AUXILIARY CACHES
jcs.auxiliary.DC=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory
jcs.auxiliary.DC.attributes=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=${user.dir}/jcs_swap
jcs.auxiliary.DC.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.DC.attributes.MaxKeySize=1000000
jcs.auxiliary.DC.attributes.OptimizeAtRemoveCount=300000
jcs.auxiliary.DC.attributes.ShutdownSpoolTimeLimit=60

            
```

Basic JCS configuration is described in more detail
[HERE](#basicjcsconfiguration)

Element level configuration is described in more detail
[HERE](#elementattributes)

For more information on advanced configuration options
and the available plugins, see the User's Guide.

<a id="getting_started-intro--step-5:-programming-to-jcs"></a>

## STEP 5: Programming to JCS

JCS provides a few convenient classes that should meet all
your needs.

To get a cache region you simply ask JCS for the region
by name. If you wanted to use JCS for City objects, you
would do something like this:

```
import java.io.Serializable; import org.apache.commons.jcs3.JCS; import org.apache.commons.jcs3.access.CacheAccess; import org.apache.commons.jcs3.access.exception.CacheException;
public class JcsExample {public static void main( String[] args ) {JcsExample example = new JcsExample(); example.testCache();}
private CacheAccess<String, City> cache = null;
public JcsExample() {try {cache = JCS.getInstance( "default" );} catch ( CacheException e ) {System.out.println( String.format( "Problem initializing cache: %s", e.getMessage() ) );}}
public void putInCache( City city ) {String key = city.name; try {cache.put( key, city );} catch ( CacheException e ) {System.out.println( String.format( "Problem putting city %s in the cache, for key %s%n%s",city.name, key, e.getMessage() ) );}}
public City retrieveFromCache( String cityKey ) {return cache.get( cityKey );}
public void testCache() {City zurich = new City( "Zürich", "Switzerland", 366765 ); putInCache( zurich );
City berlin = new City( "Berlin", "Germany", 3502000 ); putInCache( berlin );
City johannesburg = new City( "Johannesburg", "South Africa", 12200000 ); putInCache( johannesburg );
City retrievedCity1 = retrieveFromCache( "Berlin" ); if ( retrievedCity1 != null ) {System.out.println( retrievedCity1.toString() );} else {System.out.println( "No object was found in the cache for the key \"Berlin\"" );}
City retrievedCity2 = retrieveFromCache( "New York" ); if ( retrievedCity2 != null ) {System.out.println( retrievedCity2.toString() );} else {System.out.println( "No object was found in the cache for the key \"New York\"" );}}
// defined as a nested inner class to reduce number of .java files in the example public class City implements Serializable {private static final long serialVersionUID = 6392376146163510146L; public String name; public String country; public int population;
public City( String name, String country, int population ) {this.name = name; this.country = country; this.population = population;}
@Override public String toString() {return String.format( "%s is a city in the country %s with a population of %d", name, country, population );}}}
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="basicjcsconfiguration"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/BasicJCSConfiguration.html -->

<!-- page_index: 9 -->

<a id="basicjcsconfiguration--basic-jcs-configuration"></a>

## Basic JCS Configuration

The following document illustrates several basic JCS
configurations. As you'll see, using JCS can be as simple as
creating a single memory cache for you application. However, with a few configuration changes, you can quickly enable some
distributed caching features that can scale your application
even further.

<a id="basicjcsconfiguration--building-a-cache.ccf-file"></a>

### Building a cache.ccf file

Configuring the JCS can be as simple as your needs. The most
basic configuration would be a pure memory cache where every
region takes the default values. The complete configuration
file (cache.ccf) could look like this:

```

# DEFAULT CACHE REGION

jcs.default=
jcs.default.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=1000
jcs.default.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
        
```

If you want to add memory shrinking then you can add these
lines:

```

jcs.default.cacheattributes.UseMemoryShrinker=true
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.cacheattributes.MaxSpoolPerRun=500
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
        
```

Adding a [disk cache](#indexeddiskauxcache) is
as simple as telling it what folder to use. It is recommended
that you add a disk cache. If you want to add a disk cache to
your default parameters, then (1) add this to the bottom of
the file to create the auxiliary:

```

jcs.auxiliary.DC=
    org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory
jcs.auxiliary.DC.attributes=
    org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=g:/dev/jcs/raf
        
```

and (2) change the first line to:

```

jcs.default=DC
        
```

If you want to predefine a specific region, say called
`testCache1`, then add these lines:

```

jcs.region.testCache1=DC
jcs.region.testCache1.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.testCache1.cacheattributes.MaxObjects=1000
jcs.region.testCache1.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.region.testCache1.cacheattributes.UseMemoryShrinker=true
jcs.region.testCache1.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.region.testCache1.cacheattributes.ShrinkerIntervalSeconds=60
jcs.region.testCache1.cacheattributes.MaxSpoolPerRun=500
jcs.region.testCache1.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.region.testCache1.elementattributes.IsEternal=false

        
```

If you want to add a lateral cache for distribution (the [TCP Lateral Auxiliary](#lateraltcpauxcache) is
recommended), then add these lines to the bottom of the file
to define the auxiliary:

```

jcs.auxiliary.LTCP=
    org.apache.commons.jcs3.auxiliary.lateral.LateralCacheFactory
jcs.auxiliary.LTCP.attributes=
    org.apache.commons.jcs3.auxiliary.lateral.LateralCacheAttributes
jcs.auxiliary.LTCP.attributes.TransmissionTypeName=TCP
jcs.auxiliary.LTCP.attributes.TcpServers=localhost:1111
jcs.auxiliary.LTCP.attributes.TcpListenerPort=1110
jcs.auxiliary.LTCP.attributes.PutOnlyMode=false
        
```

See the TCP Lateral documentation for more information. If you
want to set up `testCache1` to use this, then change
the definition to:

```

jcs.region.testCache1=DC,LTCP
        
```

<a id="basicjcsconfiguration--a-few-comments-on-configuration"></a>

### A few comments on configuration

Auxiliary definitions are like log4j appenders, they are defined
and then associated with a region like a log4j category.

The order of configuration file is unimportant, though you
should try to keep it organized for your own sake.

Configuration is being refactored and is subject to change. It
should only become easier.

<a id="basicjcsconfiguration--the-complete-file"></a>

### The complete file

The complete file from above would look like this:

```

# DEFAULT CACHE REGION

jcs.default=DC,LTCP
jcs.default.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=1000
jcs.default.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache

# PRE-DEFINED CACHE REGIONS

jcs.region.testCache1=DC,LTCP
jcs.region.testCache1.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.testCache1.cacheattributes.MaxObjects=1000
jcs.region.testCache1.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.region.testCache1.cacheattributes.UseMemoryShrinker=true
jcs.region.testCache1.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.region.testCache1.cacheattributes.ShrinkerIntervalSeconds=60
jcs.region.testCache1.cacheattributes.MaxSpoolPerRun=500
jcs.region.testCache1.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.region.testCache1.elementattributes.IsEternal=false


# AVAILABLE AUXILIARY CACHES jcs.auxiliary.DC=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory jcs.auxiliary.DC.attributes=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=g:/dev/jcs/raf
jcs.auxiliary.DC.attributes.maxKeySize=100000

jcs.auxiliary.LTCP=
    org.apache.commons.jcs3.auxiliary.lateral.LateralCacheFactory
jcs.auxiliary.LTCP.attributes=
    org.apache.commons.jcs3.auxiliary.lateral.LateralCacheAttributes
jcs.auxiliary.LTCP.attributes.TransmissionTypeName=TCP
jcs.auxiliary.LTCP.attributes.TcpServers=localhost:1111
jcs.auxiliary.LTCP.attributes.TcpListenerPort=1110
jcs.auxiliary.LTCP.attributes.PutOnlyMode=false
        
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jcsplugins"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/JCSPlugins.html -->

<!-- page_index: 10 -->

<a id="jcsplugins--jcs-plugin-overview"></a>

## JCS Plugin Overview

JCS provides multiple auxiliaries which can be plugged into a
cache region, in a manner similar to adding Log4j appenders to a
logger. JCS auxiliaries are defined in the cache.ccf file. You can
specify which plugins a particular cache region should use.

There are four types of auxiliaries: (1) memory, (2) disk, (3)
lateral, and (4) remote. Each region is required to have one and
only one memory auxiliary. No other auxiliaries are required and any
possible combination of disk, lateral, and remote auxiliaries is
allowed. If you do not want to store items in memory, then the
maximum size for the memory caches can be set to 0 on a per region
basis.

<a id="jcsplugins--memory-plugins"></a>

## Memory Plugins

Currently, JCS provides five memory management options: (1)
LRUMemoryCache, (2) LHMLRUMemoryCache, (3) MRUMemoryCache, (5)
FIFOMemoryCache, and (5) ARCMemoryCache. All memory caches restrict
the number of items that can be stored in memory per region. If a
disk cache is configured for the region, the items will be spooled
to disk when the memory capacity is reached. JCS enforces
configurable parameters such as time to live and maximum idle time.
Expired elements can be cleaned up by the ShrinkerThread, otherwise
they will be removed at the next retrieval attempt or when the
capacity is reached.

The LRUMemoryCache is the currently recommended plugin. Upon
misconfiguration it is used as the default. The LRUMemoryCache
removes the least recently used items when the cache is full.

The ARCMemoryCache is currently experimental. It implements an
adaptive replacement caching algorithm that combines an LRU and an
LFU that adapt to usage patterns.

<a id="jcsplugins--disk-plugins"></a>

## Disk Plugins

JCS provides several disk swap options: indexed disk, HSQL, JISP, and Berkeley DB JE. The IndexedDiskCache is the recommended disk
cache. It maintains the cached data on disk and the keys in memory
for the fastest possible lookup times. Writing to disk is done
asynchronously. Items are typically put in purgatory and queued for
background disk writing. While in purgatory, the items remain
available.

In addition, JCS provides a disk auxiliary that uses the Berkeley
DB Java Edition for disk storage. JCS can effectively function as an
expiration manager and distribution mechanism on top of a Berkeley
DB JE.

<a id="jcsplugins--lateral-plugins"></a>

## Lateral Plugins

JCS provides two recommended lateral distribution options: TCP
socket server distribution and JGroups (or JavaGroups). There are
also several other experimental lateral distribution auxiliaries
using servlets, UDP, and xmlrpc.

<a id="jcsplugins--remote-plugins"></a>

## Remote Plugins

JCS provides both an RMI and HTTP remote servers to manage
distribution of cached data. These can be paired for failover.

---

<a id="usingjcsbasicweb"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/UsingJCSBasicWeb.html -->

<!-- page_index: 11 -->

<a id="usingjcsbasicweb--using-jcs:-some-basics-for-the-web"></a>

## Using JCS: Some basics for the web

The primary bottleneck in most dynamic web-based applications is
the retrieval of data from the database. While it is relatively
inexpensive to add more front-end servers to scale the serving
of pages and images and the processing of content, it is an
expensive and complex ordeal to scale the database. By taking
advantage of data caching, most web applications can reduce
latency times and scale farther with fewer machines.

JCS is a front-tier cache that can be configured to maintain
consistency across multiple servers by using a centralized
remote server or by lateral distribution of cache updates.
Other caches, like the Javlin EJB data cache, are basically
in-memory databases that sit between your EJB's and your
database. Rather than trying to speed up your slow EJB's, you
can avoid most of the network traffic and the complexity by
implementing JCS front-tier caching. Centralize your EJB access
or your JDBC data access into local managers and perform the
caching there.

<a id="usingjcsbasicweb--what-to-cache"></a>

### What to cache?

The data used by most web applications varies in its
dynamicity, from completely static to always changing at every
request. Everything that has some degree of stability can be
cached. Prime candidates for caching range from the list data
for stable dropdowns, user information, discrete and
infrequently changing information, to stable search results
that could be sorted in memory.

Since JCS is distributed and allows updates and invalidations
to be broadcast to multiple listeners, frequently changing
items can be easily cached and kept in sync through your data
access layer. For data that must be 100% up to date, say an
account balance prior to a transfer, the data should directly
be retrieved from the database. If your application allows
for the viewing and editing of data, the data for the view
pages could be cached, but the edit pages should, in most
cases, pull the data directly from the database.

<a id="usingjcsbasicweb--how-to-cache-discrete-data"></a>

### How to cache discrete data

Let's say that you have an e-commerce book store. Each book
has a related set of information that you must present to the
user. Let's say that 70% of your hits during a particular day
are for the same 1,000 popular items that you advertise on key
pages of your site, but users are still actively browsing your
catalog of over a million books. You cannot possibly cache
your entire database, but you could dramatically decrease the
load on your database by caching the 1,000 or so most popular
items.

For the sake of simplicity let's ignore tie-ins and
user-profile based suggestions (also good candidates for
caching) and focus on the core of the book detail page.

A simple way to cache the core book information would be to
create a value object for book data that contains the
necessary information to build the display page. This value
object could hold data from multiple related tables or book
subtype table, but lets say that you have a simple table
called `BOOK` that looks something like this:

```

  Table BOOK
  BOOK_ID_PK
  TITLE
  AUTHOR
  ISBN
  PRICE
  PUBLISH_DATE
        
```

We could create a value object for this table called
`BookVObj` that has variables with the same
names as the table columns that might look like this:

```
package com.genericbookstore.data;
import java.util.Date;
public class BookVObj implements Serializable {public int bookId = 0; public String title; public String author; public String ISBN; public String price; public Date publishDate;
public BookVObj() {}}
```

Then we can create a manager called
`BookVObjManager` to store and retrieve
`BookVObj`'s. All access to core book data
should go through this class, including inserts and
updates, to keep the caching simple. Let's make
`BookVObjManager` a singleton that gets a
JCS access object in initialization. The start of the
class might look like:

```
package com.genericbookstore.data;
import org.apache.commons.jcs3.JCS; import org.apache.commons.jcs3.access.CacheAccess; // in case we want to set some special behavior import org.apache.commons.jcs3.engine.behavior.IElementAttributes;
public class BookVObjManager {private static BookVObjManager instance; private static int checkedOut = 0; private static CacheAccess<String, BookVObj> bookCache;
private BookVObjManager() {try {bookCache = JCS.getInstance("bookCache");} catch (Exception e) {// Handle cache region initialization failure}
// Do other initialization that may be necessary, such as getting // references to any data access classes we may need to populate // value objects later}
/** * Singleton access point to the manager.*/ public static BookVObjManager getInstance() {synchronized (BookVObjManager.class) {if (instance == null) {instance = new BookVObjManager();}}
synchronized (instance) {instance.checkedOut++;}
return instance;}
```

To get a `BookVObj` we will need some access
methods in the manager. We should be able to get a
non-cached version if necessary, say before allowing an
administrator to edit the book data. The methods might
look like:

```
/** * Retrieves a BookVObj.  Default to look in the cache.*/ public BookVObj getBookVObj(int id) {return getBookVObj(id, true);}
/** * Retrieves a BookVObj. Second argument decides whether to look * in the cache. Returns a new value object if one can't be * loaded from the database. Database cache synchronization is * handled by removing cache elements upon modification.*/ public BookVObj getBookVObj(int id, boolean fromCache) {BookVObj vObj = null;
// If requested, attempt to load from cache if (fromCache) {vObj = bookCache.get("BookVObj" + id, () -> loadvObj(id));} else {// otherwise, load directly vObj = loadvObj(id);}
return  vObj;}
/** * Creates a BookVObj based on the id of the BOOK table.  Data * access could be direct JDBC, some or mapping tool, or an EJB.*/ public BookVObj loadBookVObj(int id) {BookVObj vObj = new BookVObj();
vObj.bookID = id;
try {boolean found = false;
// load the data and set the rest of the fields // set found to true if it was found
found = true;
// cache the value object if found
if (found) {// could use the defaults like this // bookCache.put( "BookVObj" + id, vObj ); // or specify special characteristics
// put to cache
bookCache.put("BookVObj" + id, vObj);}
} catch (Exception e) {// Handle failure putting object to cache}
return vObj;}
```

We will also need a method to insert and update book data. To
keep the caching in one place, this should be the primary way
core book data is created. The method might look like:

```
/** * Stores BookVObj's in database.  Clears old items and caches * new.*/ public int storeBookVObj(BookVObj vObj) {try {// since any cached data is no longer valid, we should // remove the item from the cache if it an update.
if (vObj.bookID != 0) {bookCache.remove("BookVObj" + vObj.bookID);}
// put the new object in the cache
bookCache.put("BookVObj" + id, vObj);} catch (Exception e) {// Handle failure removing object or putting object to cache.}}}
```

As elements are placed in the cache via `put`, it
is possible to specify custom attributes for those elements
such as its maximum lifetime in the cache, whether or not it
can be spooled to disk, etc. It is also possible (and easier)
to define these attributes in the configuration file as
demonstrated later. We now have the basic infrastructure for
caching the book data.

<a id="usingjcsbasicweb--selecting-the-appropriate-auxiliary-caches"></a>

### Selecting the appropriate auxiliary caches

The first step in creating a cache region is to determine the
makeup of the memory cache. For the book store example, I
would create a region that could store a bit over the minimum
number I want to have in memory, so the core items always
readily available. I would set the maximum memory size to
`1200`. In addition, I might want to have all
objects in this cache region expire after `7200`
seconds. This can be configured in the element attributes on
a default or per-region basis as illustrated in the
configuration file below.

For most cache regions you will want to use a disk
cache if the data takes over about .5 milliseconds to
create. The [indexed
disk cache](#indexeddiskauxcache) is the most efficient disk caching
auxiliary, and for normal usage it is recommended.

The next step will be to select an appropriate
distribution layer. If you have a back-end server
running an appserver or scripts or are running multiple
webserver VMs on one machine, you might want to use
the centralized [remote
cache](#remoteauxcache). The lateral cache would be fine, but since
the lateral cache binds to a port, you'd have to configure
each VM's lateral cache to listen to a different port on
that machine.

If your environment is very flat, say a few
load-balanced webservers and a database machine or one
webserver with multiple VMs and a database machine, then the lateral cache will probably make more sense.
The [TCP lateral
cache](#lateraltcpauxcache) is recommended.

For the book store configuration I will set up a region
for the `bookCache` that uses the LRU memory
cache, the indexed disk auxiliary cache, and the remote
cache. The configuration file might look like this:

```

# DEFAULT CACHE REGION

# sets the default aux value for any non configured caches
jcs.default=DC,RFailover
jcs.default.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=1000
jcs.default.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=3600
jcs.default.elementattributes.IdleTime=1800
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true


# CACHE REGIONS AVAILABLE

# Regions preconfigured for caching
jcs.region.bookCache=DC,RFailover
jcs.region.bookCache.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.bookCache.cacheattributes.MaxObjects=1200
jcs.region.bookCache.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.region.bookCache.elementattributes.IsEternal=false
jcs.region.bookCache.elementattributes.MaxLife=7200
jcs.region.bookCache.elementattributes.IdleTime=1800
jcs.region.bookCache.elementattributes.IsSpool=true
jcs.region.bookCache.elementattributes.IsRemote=true
jcs.region.bookCache.elementattributes.IsLateral=true

# AUXILIARY CACHES AVAILABLE

# Primary Disk Cache -- faster than the rest because of memory key storage jcs.auxiliary.DC=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory jcs.auxiliary.DC.attributes=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=/usr/opt/bookstore/raf
jcs.auxiliary.DC.attributes.MaxPurgatorySize=10000
jcs.auxiliary.DC.attributes.MaxKeySize=10000
jcs.auxiliary.DC.attributes.OptimizeAtRemoveCount=300000

# Remote RMI Cache set up to failover jcs.auxiliary.RFailover=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheFactory jcs.auxiliary.RFailover.attributes=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes
jcs.auxiliary.RFailover.attributes.RemoteTypeName=LOCAL
jcs.auxiliary.RFailover.attributes.FailoverServers=scriptserver:1102
jcs.auxiliary.RFailover.attributes.GetOnly=false
        
```

I've set up the default cache settings in the above
file to approximate the `bookCache`
settings. Other non-preconfigured cache regions will
use the default settings. You only have to configure
the auxiliary caches once. For most caches you will
not need to pre-configure your regions unless the size
of the elements varies radically. We could easily put
several hundred thousand `BookVObj`'s in
memory. The `1200` limit was very
conservative and would be more appropriate for a large
data structure.

To get running with the book store example, I will also
need to start up the remote cache server on the
scriptserver machine. The
[remote cache
documentation](#remoteauxcache) describes the configuration.

I now have a basic caching system implemented for my book
data. Performance should improve immediately.

---

<a id="localcacheconfig"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/LocalCacheConfig.html -->

<!-- page_index: 12 -->

<a id="localcacheconfig--configuring-the-local-cache"></a>

## Configuring the Local Cache

This document is intended to provide various answers to
questions regarding the configuration of a local cache. The
document is presented in a question / answer format.

<a id="localcacheconfig--where-is-the-configuration-information"></a>

### Where is the configuration information?

Configuration of local caches involves editing the cache
configuration file, named `cache.ccf`. The
classpath should include the directory where this file is
located or the file should be placed at the root of the
classpath, since it is discovered automatically.

<a id="localcacheconfig--what-is-in-the-cache.ccf-file"></a>

### What is in the cache.ccf file?

The `cache.ccf` file contains default configuration
information for cache regions and specific configuration
information for regions that you predefine. Regions not using
default behaviors should generally be configured via the
`cache.ccf` file. If you can put configuration
information in a class, you can edit a props file just as
easily. This makes modification of the regional setting more
efficient and allows for startup error checking.

There are three main sections of the `cache.ccf`
file:

- the default and system settings
- the region specific settings
- the auxiliary cache definitions

<a id="localcacheconfig--how-do-i-set-up-default-values-for-regions"></a>

### How do I set up default values for regions?

You can establish default values that any non-preconfigured
region will inherit. The non-predefined region will be
created when you call
`CacheAccess.getAccess("cacheName")`. The default
setting look like this:

```

# DEFAULT CACHE REGION

# sets the default aux value for any non configured caches
jcs.default=DC,RFailover
jcs.default.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=1000
        
```

The most important line is
`jcs.default=DC,Rfailover`. This tells the cache
what auxiliary caches should be used. Auxiliary caches are
configured in the third section of the `cache.ccf`
and are referenced in a comma separated list. You can add as
many auxiliary caches as you want, but the behavior of remote
and lateral auxiliaries may conflict. This allows you to
define different configurations for auxiliary caches and to
use these different configurations for different regions.

<a id="localcacheconfig--how-do-i-define-a-region"></a>

### How do I define a region?

Defining a region involves specifying which auxiliary caches
it will use and how many objects it will store in memory. A
typical region definition looks like:

```

jcs.region.testCache=DC,RFailover
jcs.region.testCache.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.testCache.cacheattributes.MaxObjects=1000
        
```

The region name is `testCache`. It will have a
1000 item memory limit and will use the DC and RFailover
auxiliary caches. If a typical element for this region was
very large, you might want to lower the number of items stored
in memory. The size of the memory storage is dependent on the
priority of the cache, the size of its elements, and the
amount of RAM on the machine.

<a id="localcacheconfig--how-do-i-configure-an-auxiliary-cache"></a>

### How do I configure an auxiliary cache?

Each auxiliary cache is created through a factory that passes
an attribute object to the constructor. The attributes are
set via reflection and should be fairly simple to understand.
Each auxiliary cache will be fully documented. Plugging in
your own auxiliary cache become a simple matter given the
reflexive manner of initialization.

The most important settings for common usage are the disk path
and the remote cache location. It is recommended that only
disk and remote auxiliaries be used. The lateral caches are
functional but not as efficient.

The default configuration code above specifies that
non-preconfigured caches use the auxiliary cache by the name
DC. This cache is defined in the third section of the file:

```

jcs.auxiliary.DC=
    org.apache.commons.jcs3.auxiliary.disk.DiskCacheFactory
jcs.auxiliary.DC.attributes=
    org.apache.commons.jcs3.auxiliary.disk.DiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=c:/dev/cache/raf
        
```

The only thing that needs to be set here is the
`DiskPath` value. Change it to wherever you want
the cache to persist unused items.

The default region is also set to use an auxiliary called
`RFailover`. This is a remote cache that is
designed to failover to other remote servers in a cluster:

```

jcs.auxiliary.RFailover=
    org.apache.commons.jcs3.auxiliary.remote.RemoteCacheFactory
jcs.auxiliary.RFailover.attributes=
    org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes
jcs.auxiliary.RFailover.attributes.RemoteTypeName=LOCAL
jcs.auxiliary.RFailover.attributes.FailoverServers=
    localhost:1102,localhost:1101
        
```

If you don't have more than one remote server running, just
specify it by itself in the `FailoverServers`
attribute.

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="elementattributes"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/ElementAttributes.html -->

<!-- page_index: 13 -->

<a id="elementattributes--element-attribute-configuration"></a>

## Element Attribute Configuration

The following document describes the various
configuration options available for cache elements. Each
element put into the cache can be configured
independently. You can define element behavior in three
ways: as a default setting, as a region setting, or at
the element level.

<a id="elementattributes--setting-the-defaults"></a>

### Setting the defaults

The configuration below can be put in the cache.ccf
configuration file. It establishes the default
behavior for all regions. A region can override
these defaults and an individual element can override
these defaults and the region settings.

```

					
# DEFAULT CACHE REGION

jcs.default=DC
jcs.default.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=1000
jcs.default.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.cacheattributes.UseMemoryShrinker=true
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=700
jcs.default.elementattributes.IdleTime=1800
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true
        
				
```

The default and region configuration settings have
three components. They define what auxiliaries are
available, how the cache should control the memory, and how the elements should behave. This
configuration tells all regions to use an auxiliary
called DC by default. It also establishes several
settings for memory management (see
[Basic JCS Configuration](#basicjcsconfiguration)
for more information on the cacheattribute
settings). In addition, by default all regions will
take these element configuration settings.

These settings specify that elements are not
eternal, i.e. they can expire. By default elements
are considered eternal.

You can define the maximum life of an item by
setting the
`MaxLife`
parameter. If an item has been in the cache for
longer than the set number of seconds it will not be
retrieved on a get request. If you use the memory
shrinker the item will be actively removed from
memory. Currently there is no background disk
shrinker, but the disk cache does allow for a
maximum number of keys (see
[Indexed Disk Cache](#indexeddiskauxcache)
for more information on the disk cache settings).

You can define the maximum time an item can live
without being accessed by setting the
`IdleTime`
parameter. This is different than the
`MaxMemoryIdleTimeSeconds`
parameter, which just specifies how long an object
can be in memory before it is subjected to removal
or being spooled to a disk cache if it is available.
Note: the
`IdleTime`
parameter may not function properly for items
retrieved from disk, if you have a memory size of 0.

`IsSpool`
determines whether or not the element can go to disk, if
a disk cache is configured for the region.

`IsRemote`
determines whether or not the element can be sent to a
remote server, if one is configured for the region.

`IsLateral`
determines whether or not the element can be laterally
distributed, if a lateral auxiliary is configured for
the region.

<a id="elementattributes--programmatic-configuration"></a>

### Programmatic Configuration

Every element put into the cache has its own set of
attributes. By default elements are given a copy of
the default element attributes associated with a
region. You can also specify the attributes to use
for an element when you put it in the cache.

```

				
    CacheAccess<String, String> jcs = JCS.getInstance( "myregion" );

    . . .

    // jcs.getDefaultElementAttributes returns a copy not a reference
    IElementAttributes attributes = jcs.getDefaultElementAttributes();

    // set some special value
    attributes.setIsEternal( true );
    jcs.put( "key", "data", attributes );
        		
				
```

You can also programmatically modify the default
element attributes.

```

					
    CacheAccess<String, String> jcs = JCS.getInstance( "myregion" );

    . . .

    // jcs.getDefaultElementAttributes returns a copy not a reference
    IElementAttributes attributes = jcs.getDefaultElementAttributes();

    // set some special value
    attributes.setIsEternal( true );
    jcs.setDefaultElementAttributes( attributes );
        		
				
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="elementeventhandling"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/ElementEventHandling.html -->

<!-- page_index: 14 -->

<a id="elementeventhandling--element-event-handling"></a>

## Element Event Handling

JCS allows you to attach event handlers to elements in
the local memory cache.

There are several events that you can listen for. All of
the events are local memory related events. Element
event handlers are not transmitted to other caches via
lateral or remote auxiliaries, nor are they spooled to
disk.

You can register multiple handlers for a single item.
Although the handlers are associated with particular
items, you can also setup default handlers for any
region. Each item put into the region, that will take
the default element attributes, will be assigned the
event default event handlers.

The various events that you can handle have all been
assigned integer codes. The codes are defined in the
org.apache.commons.jcs3.engine.control.event.behavior.IElementEventConstants
interface. The events are named descriptively and
include:

| Name | Description |
| --- | --- |
| ELEMENT\_EVENT\_EXCEEDED\_MAXLIFE\_BACKGROUND | The element exceeded its max life. This was detected in a background cleanup. |
| ELEMENT\_EVENT\_EXCEEDED\_MAXLIFE\_ONREQUEST | The element exceeded its max life. This was detected on request. |
| ELEMENT\_EVENT\_EXCEEDED\_IDLETIME\_BACKGROUND | The element exceeded its max idle. This was detected in a background cleanup. |
| ELEMENT\_EVENT\_EXCEEDED\_IDLETIME\_ONREQUEST | The element exceeded its max idle time. This was detected on request. |
| ELEMENT\_EVENT\_SPOOLED\_DISK\_AVAILABLE | The element was pushed out of the memory store, there is a disk store available for the region, and the element is marked as spoolable. |
| ELEMENT\_EVENT\_SPOOLED\_DISK\_NOT\_AVAILABLE | The element was pushed out of the memory store, and there is not a disk store available for the region. |
| ELEMENT\_EVENT\_SPOOLED\_NOT\_ALLOWED | The element was pushed out of the memory store, there is a disk store available for the region, but the element is marked as not spoolable. |

To create an event handler you must implement the
org.apache.commons.jcs3.engine.control.event.behavior.IElementEventHandler
interface. This interface contains only one method:

```

				
    public void handleElementEvent( IElementEvent event );
        		
			
```

The IElementEvent object contains both the event code
and the source. The source is the element for which the
event occurred. The code is the type of event. If you
have an event handler registered, it will be called
whenever any event occurs. It is up to the handler to
decide what it would like to do for the particular
event. Since there are not that many events, this does
not create too much activity. Also, the event handling
is done asynchronously. Events are added to an event
queue and processed by background threads.

Here is how to extract the event and source from the
IElementEvent:

```
public void handleElementEvent( IElementEvent event ) {int eventType = event.getElementEvent(); CacheElement element = (CacheElement)((EventObject)event).getSource(); . . .}
```

Once you have an IElementEventHandler implementation, you can attach it to an element via the Element
Attributes. You can either add it to the element
attributes when you put an item into the cache, add it
to the attributes of an item that exist in the cache
(which just results in a re-put), or add the event
handler to the default element attributes for a region.
If you add it to the default attributes, then all
elements subsequently added to the region that do not
define their own element attributes will be assigned the
default event handlers.

```

				
    CacheAccess<String, String> jcs = JCS.getInstance( "myregion" );

    . . .

    MyEventHandler meh = new MyEventHandler();

    // jcs.getDefaultElementAttributes returns a copy not a reference
    IElementAttributes attributes = jcs.getDefaultElementAttributes();
    attributes.addElementEventHandler( meh );
    jcs.put( "key", "data", attributes );
        		
			
```

Here is how to setup an event handler as a default
setting for a region:

```

				
    CacheAccess<String, String> jcs = JCS.getInstance( "myregion" );

    . . .

    MyEventHandler meh = new MyEventHandler();

    // this should add the event handler to all items as
    //they are created.
    // jcs.getDefaultElementAttributes returns a copy not a reference
    IElementAttributes attributes = jcs.getDefaultElementAttributes();
    attributes.addElementEventHandler( meh );
    jcs.setDefaultElementAttributes( attributes );
        		
			
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="regionproperties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/RegionProperties.html -->

<!-- page_index: 15 -->

<a id="regionproperties--cache-region-configuration"></a>

## Cache Region Configuration

The following properties apply to any cache region. They
can be specified as default values and specified on a
region by region basis. There are three types of
settings: auxiliary, cache, and element. The cache
settings define the memory management for the region.
The element settings define default element behavior
within the region.

<a id="regionproperties--region-auxiliary-properties"></a>

### Region (Auxiliary) Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
|  | You can specify the list of auxiliaries that regions can use. This has no attribute name. The list can be empty, otherwise it should be comma delimited. | Y | n/a |

<a id="regionproperties--region-cache-properties"></a>

### Region (Cache) Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| MaxObjects | The maximum number of items allowed in memory. Eviction of elements in excess of this number is determined by the memory cache. By default JCS uses the LRU memory cache. | Y | n/a |
| MemoryCacheName | This property allows you to specify what memory manager you would like to use. You can create your own memory manager by implementing the org.apache.commons.jcs3.engine.memory.MemoryCache interface. Alternatively, you can extend the org.apache.commons.jcs3.engine.memory.AbstractMemoryCache class. Several different memory caches are available: two LRU implementations, an LFU, and an adaptive replacement algorithm. | N | org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache |
| UseMemoryShrinker | By default, the memory shrinker is shared by all regions that use the LRU memory cache. The memory shrinker iterates through the items in memory, looking for items that have expired or that have exceeded their max memory idle time. | N | false |
| MaxMemoryIdleTimeSeconds | This is only used if you are using the memory shrinker. If this value is set above -1, then if an item has not been accessed in this number of seconds, it will be spooled to disk if the disk is available. You can register an event handler on this event. | N | 7200 |
| ShrinkerIntervalSeconds | This specifies how often the shrinker should run, if it has been activated. If you set UseMemoryShrinker to false, then this setting has no effect. | N | 30 |
| DiskUsagePatternName | SWAP is the default. Under the swap pattern, data is only put to disk when the max memory size is reached. Since items puled from disk are put into memory, if the memory cache is full and you get an item off disk, the lest recently used item will be spooled to disk. If you have a low memory hit ration, you end up thrashing. The UPDATE usage pattern allows items to go to disk on an update. It disables the swap. This allows you to persist all items to disk. If you are using the JDBC disk cache for instance, you can put all the items on disk while using the memory cache for performance, and not worry about losing data from a system crash or improper shutdown. Also, since all items are on disk, there is no need to swap to disk. This prevents the possibility of thrashing. | N | SWAP |

<a id="regionproperties--region-element-properties"></a>

### Region (Element) Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| IsEternal | If an element is specified as eternal, then it will never be subject to removal for exceeding its max life. | N | true |
| MaxLife | If you specify that elements within a region are not eternal, then you can set the max life seconds. If this is exceeded the elements will be removed passively when a client tries to retrieve them. If you are using a memory shrinker, then the items can be removed actively. | N | -1 |
| IsSpool | By default, can elements in this region be sent to a disk cache if one is available. | N | true |
| IsLateral | By default, can elements in this region be sent to a lateral cache if one is available. | N | true |
| IsRemote | By default, can elements in this region be sent to a remote cache if one is available. | N | true |

<a id="regionproperties--example-configuration"></a>

### Example Configuration

```

					
jcs.default=
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=200001
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.cacheattributes.UseMemoryShrinker=true
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=700
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true

# optional region "testCache1" specific configuration settings jcs.region.testCache1=
jcs.region.testCache1.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.testCache1.cacheattributes.MaxObjects=123456
jcs.region.testCache1.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.region.testCache1.cacheattributes.UseMemoryShrinker=true
jcs.region.testCache1.cacheattributes.ShrinkerIntervalSeconds=30
jcs.region.testCache1.cacheattributes.MaxMemoryIdleTimeSeconds=300
jcs.region.testCache1.cacheattributes.MaxSpoolPerRun=100
jcs.region.testCache1.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.region.testCache1.elementattributes.IsEternal=false
jcs.region.testCache1.elementattributes.MaxLife=60000
jcs.region.testCache1.elementattributes.IsSpool=true
jcs.region.testCache1.elementattributes.IsLateral=true
jcs.region.testCache1.elementattributes.IsRemote=true
        
				
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="projecthistory"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/ProjectHistory.html -->

<!-- page_index: 16 -->

<a id="projecthistory--project-history"></a>

## Project History

Project was created in 2002. It was first released under
maven coordinates org.apache.jcs:jcs[:1.3].

Since 2014 and its version 2 it is released under coordinates
org.apache.commons:commons-jcs-[core|jcache|\*][:2.x].

---

<a id="cacheeventlogging"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/CacheEventLogging.html -->

<!-- page_index: 17 -->

<a id="cacheeventlogging--cache-event-logging"></a>

## Cache Event Logging

JCS allows you to implement custom event loggers. Most of the
auxiliaries will log ICacheEvents (eg. update, get, getMultiple, remove, removeAll, and dispose) to an injected event logger. By default the
log calls balk. But if you inject a logger, you can add monitoring
to any auxiliary. Most auxiliaries also log key application events
and critical errors to the same logger.

To inject a custom event logger, you simply need to implement the
`org.apache.commons.jcs3.engine.logging.behavior.ICacheEventLogger`
interface and add a couple of lines to the cache.ccf file.

During configuration, JCS will look for event loggers configured
for each auxiliary. JCS will set any custom properties. For
instance, to add debug event logging to a remote cache client, you
could do the following:

```

			. . .
			jcs.auxiliary.RC=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheFactory
jcs.auxiliary.RC.attributes=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes
jcs.auxiliary.RC.attributes.FailoverServers=localhost:1101,localhost:1102
jcs.auxiliary.RC.attributes.LocalPort=1201
jcs.auxiliary.RC.attributes.RemoveUponRemotePut=false
# jcs.auxiliary.RC.attributes.RemoteServiceName=RemoteCache
# -1 means no timeout, this is the default
# if the timeout is -1, no threadpool will be used.
jcs.auxiliary.RC.attributes.GetTimeoutMillis=500
jcs.auxiliary.RC.attributes.ThreadPoolName=remote_cache_client
jcs.auxiliary.RC.attributes.GetOnly=false
jcs.auxiliary.RC.cacheeventlogger=org.apache.commons.jcs3.engine.logging.CacheEventLoggerDebugLogger
jcs.auxiliary.RC.cacheeventlogger.attributes.logCategoryName=test.RCCEventLogCategory
			. . .
        
```

The attribute "logCateoryName" is a property of this
implementation. You can configure any properties on your
implementation in the same way.

---

<a id="elementserializers"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/ElementSerializers.html -->

<!-- page_index: 18 -->

<a id="elementserializers--serializing-and-de-serializing-cache-objects"></a>

## Serializing and De-serializing Cache Objects

When using auxiliary caches, cache elements need to be serialized
into a byte stream in order to be stored on disk or transported
through a network. For reading from these caches, bytes must be
de-serialized into objects. By default, JCS uses the standard JDK
methods for serializing and de-serializing objects. However, all
of the auxiliaries also support setting a custom serializer to
have finer control of the behavior.

This document describes the built-in serializers and their
configuration.

<a id="elementserializers--compressing-serializer"></a>

## Compressing Serializer

The `CompressingSerializer` gzips the bytes
after serializing the cache object the default way. For reading, the bytes will be de-compressed first and then de-serialized into
a Java object. The class can also be used as a wrapper around an
arbitrary class implementing `IElementSerializer`.

The configuration for a typical application looks like this:

```

                
# Block Disk Cache
jcs.auxiliary.blockDiskCache=org.apache.commons.jcs3.auxiliary.disk.block.BlockDiskCacheFactory
jcs.auxiliary.blockDiskCache.attributes=org.apache.commons.jcs3.auxiliary.disk.block.BlockDiskCacheAttributes
jcs.auxiliary.blockDiskCache.attributes.DiskPath=target/test-sandbox/block-disk-cache
jcs.auxiliary.blockDiskCache.serializer=org.apache.commons.jcs3.utils.serialization.CompressingSerializer
                
            
```

<a id="elementserializers--encrypting-serializer"></a>

## Encrypting Serializer

The `EncryptingSerializer` uses AES to encrypt the bytes
after serializing the cache object the default way. For reading, the bytes will be decrypted first and then de-serialized into
a Java object. The class can also be used as a wrapper around an
arbitrary class implementing `IElementSerializer`.

The implementation uses a symmetrical pre-shared key phrase for
encrypting and decrypting the data. The key is salted separately
for each object and the salt is stored together with the serialized
data.

The configuration for a typical application looks like this:

```

                
# Block Disk Cache
jcs.auxiliary.blockDiskCache2=org.apache.commons.jcs3.auxiliary.disk.block.BlockDiskCacheFactory
jcs.auxiliary.blockDiskCache2.attributes=org.apache.commons.jcs3.auxiliary.disk.block.BlockDiskCacheAttributes
jcs.auxiliary.blockDiskCache2.attributes.DiskPath=target/test-sandbox/block-disk-cache2
jcs.auxiliary.blockDiskCache2.serializer=org.apache.commons.jcs3.utils.serialization.EncryptingSerializer
jcs.auxiliary.blockDiskCache2.serializer.attributes.preSharedKey=my_secret
                
            
```

The AES cipher transformation default is AES/ECB/PKCS5Padding as this
algorithm must be supported by every JDK 8, according to the
[docs](https://docs.oracle.com/javase/8/docs/api/javax/crypto/Cipher.html).
Special handling is provided for the AES/GCM/NoPadding algorithm which
can be activated like this:

```

                
jcs.auxiliary.blockDiskCache2.serializer.attributes.aesCipherTransformation=AES/GCM/NoPadding
                
            
```

The encryption code uses the default constructor of SecureRandom() to create
a random number generator. Depending on your security requirements, you should
configure a SecureRandom that works for your environment, giving preference to
the ones with good randomness (given that your environment generates entropy fast
enough, we saw problems with Linux).

---

<a id="indexeddiskauxcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/IndexedDiskAuxCache.html -->

<!-- page_index: 19 -->

<a id="indexeddiskauxcache--indexed-disk-auxiliary-cache"></a>

## Indexed Disk Auxiliary Cache

The Indexed Disk Auxiliary Cache is an optional plugin
for the JCS. It is primarily intended to provide a
secondary store to ease the memory burden of the cache.
When the memory cache exceeds its maximum size it tells
the cache hub that the item to be removed from memory
should be spooled to disk. The cache checks to see if
any auxiliaries of type "disk" have been configured for
the region. If the "Indexed Disk Auxiliary Cache" is
used, the item will be spooled to disk.

<a id="indexeddiskauxcache--disk-indexing"></a>

### Disk Indexing

The Indexed Disk Auxiliary Cache follows the fastest
pattern of disk caching. Items are stored at the end
of a file dedicated to the cache region. The first
byte of each disk entry specifies the length of the
entry. The start position in the file is saved in
memory, referenced by the item's key. Though this
still requires memory, it is insignificant given the
performance trade off. Depending on the key size, 500,000 disk entries will probably only require
about 3 MB of memory. Locating the position of an
item is as fast as a map lookup and the retrieval of
the item only requires 2 disk accesses.

When items are removed from the disk cache, the
location of the available block on the storage file
is recorded in skip list set. This allows the disk
cache to reuse empty spots, thereby keeping the file
size to a minimum.

<a id="indexeddiskauxcache--purgatory"></a>

### Purgatory

Writing to the disk cache is asynchronous and made
efficient by using a memory staging area called
purgatory. Retrievals check purgatory then disk for
an item. When items are sent to purgatory they are
simultaneously queued to be put to disk. If an item
is retrieved from purgatory it will no longer be
written to disk, since the cache hub will move it
back to memory. Using purgatory insures that there
is no wait for disk writes, unnecessary disk writes
are avoided for borderline items, and the items are
always available.

<a id="indexeddiskauxcache--persistence"></a>

### Persistence

When the disk cache is properly shutdown, the memory
index is written to disk and the value file is
defragmented. When the cache starts up, the disk
cache can be configured to read or delete the index
file. This provides an unreliable persistence
mechanism.

<a id="indexeddiskauxcache--size-limitation"></a>

### Size limitation

There are two ways to limit the cache size: using element
count and element size. When using element count, in disk
store there will be at most MaxKeySize elements. When using
element size, there will be at most KeySize kB of elements
stored in the data file. The file can be bigger due to
fragmentation. The limit does not cover the size of key file
so the total space occupied by the cache might be a bit bigger.
The mode is chosen using DiskLimitType. Allowed values are:
COUNT and SIZE.

<a id="indexeddiskauxcache--configuration"></a>

### Configuration

Configuration is simple and is done in the
auxiliary cache section of the
`cache.ccf`
configuration file. In the example below, I created
an Indexed Disk Auxiliary Cache referenced by
`DC`
. It uses files located in the "DiskPath" directory.

The Disk indexes are equipped with an LRU storage
limit. The maximum number of keys is configured by
the maxKeySize parameter. If the maximum key size is
less than 0, no limit will be placed on the number
of keys. By default, the max key size is 5000.

```

jcs.auxiliary.DC=
    org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory
jcs.auxiliary.DC.attributes=
    org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=g:\dev\jakarta-turbine-stratum\raf
jcs.auxiliary.DC.attributes.MaxKeySize=100000
```

<a id="indexeddiskauxcache--additional-configuration-options"></a>

### Additional Configuration Options

The indexed disk cache provides some additional
configuration options.

The purgatory size of the Disk cache is equipped
with an LRU storage limit. The maximum number of
elements allowed in purgatory is configured by the
MaxPurgatorySize parameter. By default, the max
purgatory size is 5000.

Initial testing indicates that the disk cache
performs better when the key and purgatory sizes are
limited.

```

jcs.auxiliary.DC.attributes.MaxPurgatorySize=10000
```

Slots in the data file become empty when items are
removed from the disk cache. The indexed disk cache
keeps track of empty slots in the data file, so they
can be reused. The slot locations are stored in the
recycle bin.

If all the items put on disk are the same size, then
the recycle bin will always return perfect matches.
However, if the items are of various sizes, the disk
cache will use the free spot closest in size but not
smaller than the item being written to disk. Since
some recycled spots will be larger than the items
written to disk, unusable gaps will result.
Optimization is intended to remove these gaps.

The Disk cache can be configured to defragment the
data file at runtime. Since defragmentation is only
necessary if items have been removed, the
deframentation interval is determined by the number
of removes. Currently there is no way to schedule
defragmentation to run at a set time. If you set the
OptimizeAtRemoveCount to -1, no optimizations of the
data file will occur until shutdown. By default the
value is -1.

In version 1.2.7.9 of JCS, the optimization routine
was significantly improved. It now occurs in place, without the aid of a temporary file.

```

jcs.auxiliary.DC.attributes.OptimizeAtRemoveCount=30000
```

<a id="indexeddiskauxcache--a-complete-configuration-example"></a>

### A Complete Configuration Example

In this sample cache.ccf file, I configured the
cache to use a disk cache, called DC, by default.
Also, I explicitly set a cache region called
myRegion1 to use DC. I specified custom settings for
all of the Indexed Disk Cache configuration
parameters.

```

##############################################################
##### Default Region Configuration
jcs.default=DC
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=100
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache

##############################################################
##### CACHE REGIONS
jcs.region.myRegion1=DC
jcs.region.myRegion1.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.myRegion1.cacheattributes.MaxObjects=1000
jcs.region.myRegion1.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache

##############################################################
##### AUXILIARY CACHES
# Indexed Disk Cache
jcs.auxiliary.DC=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory
jcs.auxiliary.DC.attributes=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=target/test-sandbox/indexed-disk-cache
jcs.auxiliary.DC.attributes.MaxPurgatorySize=10000
jcs.auxiliary.DC.attributes.MaxKeySize=10000
jcs.auxiliary.DC.attributes.OptimizeAtRemoveCount=300000
jcs.auxiliary.DC.attributes.OptimizeOnShutdown=true
jcs.auxiliary.DC.attributes.DiskLimitType=COUNT
```

<a id="indexeddiskauxcache--using-thread-pools-to-reduce-threads"></a>

### Using Thread Pools to Reduce Threads

The Indexed Disk Cache allows you to use fewer
threads than active regions. By default the disk
cache will use the standard cache event queue which
has a dedicated thread. Although the standard queue
kills its worker thread after a minute of
inactivity, you may want to restrict the total
number of threads. You can accomplish this by using
a pooled event queue.

The configuration file below defines a disk cache
called DC2. It uses an event queue of type POOLED.
The queue is named disk\_cache\_event\_queue. The
disk\_cache\_event\_queue is defined in the bottom of
the file.

```

##############################################################
################## DEFAULT CACHE REGION  #####################
# sets the default aux value for any non configured caches
jcs.default=DC2
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=200001
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.cacheattributes.UseMemoryShrinker=false
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=700
jcs.default.elementattributes.IdleTime=1800
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true

##############################################################
################## AUXILIARY CACHES AVAILABLE ################

# Disk Cache Using a Pooled Event Queue -- this allows you
# to control the maximum number of threads it will use.
# Each region uses 1 thread by default in the SINGLE model.
# adding more threads than regions does not help performance.
# If you want to use a separate pool for each disk cache, either use
# the single model or define a different auxiliary for each region and use the Pooled type.
# SINGLE is generally best unless you have a huge # of regions.
jcs.auxiliary.DC2=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory
jcs.auxiliary.DC2.attributes=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC2.attributes.DiskPath=target/test-sandbox/raf
jcs.auxiliary.DC2.attributes.MaxPurgatorySize=10000
jcs.auxiliary.DC2.attributes.MaxKeySize=10000
jcs.auxiliary.DC2.attributes.OptimizeAtRemoveCount=300000
jcs.auxiliary.DC2.attributes.OptimizeOnShutdown=true
jcs.auxiliary.DC2.attributes.EventQueueType=POOLED
jcs.auxiliary.DC2.attributes.EventQueuePoolName=disk_cache_event_queue

##############################################################
################## OPTIONAL THREAD POOL CONFIGURATION ########

# Disk Cache Event Queue Pool
thread_pool.disk_cache_event_queue.useBoundary=false
thread_pool.disk_cache_event_queue.maximumPoolSize=15
thread_pool.disk_cache_event_queue.minimumPoolSize=1
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.startUpSize=1
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="indexeddiskcacheproperties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/IndexedDiskCacheProperties.html -->

<!-- page_index: 20 -->

<a id="indexeddiskcacheproperties--indexed-disk-auxiliary-cache-configuration"></a>

## Indexed Disk Auxiliary Cache Configuration

The following properties apply to the Indexed Disk Cache plugin.

<a id="indexeddiskcacheproperties--indexed-disk-configuration-properties"></a>

### Indexed Disk Configuration Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| DiskPath | The directory where the disk cache should write its files. | Y | n/a |
| MaxPurgatorySize | The maximum number of items allowed in the queue of items to be written to disk. | N | 5000 |
| MaxKeySize | The maximum number of keys that the indexed disk cache can have. Since the keys are stored in memory, you may want to limit this number to something reasonable. The default is a bit small. | N | 5000 |
| OptimizeAtRemoveCount | At how many removes should the cache try to defragment the data file. Since we recycle empty spots, defragmentation is usually not needed. To prevent the cache from defragmenting the data file, you can set this to -1. This is the default value. | N | -1 |
| OptimizeOnShutdown | By default the Indexed Disk Cache will optimize on shutdown if the free data size is greater than 0. If you want to prevent this behavior, you can set this parameter to false. | N | true |
| ClearDiskOnStartup | By default the Indexed Disk Cache will use items found on disk on startup. If you set this value to true, the old key and data files will be cleared. | N | false |

<a id="indexeddiskcacheproperties--example-configuration"></a>

### Example Configuration

```

					
jcs.auxiliary.DC=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory
jcs.auxiliary.DC.attributes=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=target/test-sandbox/indexed-disk-cache
jcs.auxiliary.DC.attributes.MaxPurgatorySize=10000
jcs.auxiliary.DC.attributes.MaxKeySize=10000
jcs.auxiliary.DC.attributes.OptimizeAtRemoveCount=300000
jcs.auxiliary.DC.attributes.OptimizeOnShutdown=true
jcs.auxiliary.DC.attributes.ClearDiskOnStartup=false
        
				
```

<a id="indexeddiskcacheproperties--indexed-disk-event-queue-configuration"></a>

### Indexed Disk Event Queue Configuration

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| EventQueueType | This should be either SINGLE or POOLED. By default the single style pool is used. The single style pool uses a single thread per event queue. That thread is killed whenever the queue is inactive for 30 seconds. Since the disk cache uses an event queue for every region, if you have many regions and they are all active, you will be using many threads. To limit the number of threads, you can configure the disk cache to use the pooled event queue. Using more threads than regions will not add any benefit for the indexed disk cache, since only one thread can read or write at a time for a single region. | N | SINGLE |
| EventQueuePoolName | This is the name of the pool to use. It is required if you choose the POOLED event queue type, otherwise it is ignored. | Y | n/a |

<a id="indexeddiskcacheproperties--example-configuration-using-thread-pool"></a>

### Example Configuration Using Thread Pool

```

					
jcs.auxiliary.DC=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheFactory
jcs.auxiliary.DC.attributes=org.apache.commons.jcs3.auxiliary.disk.indexed.IndexedDiskCacheAttributes
jcs.auxiliary.DC.attributes.DiskPath=target/test-sandbox/indexed-disk-cache
jcs.auxiliary.DC.attributes.MaxPurgatorySize=10000
jcs.auxiliary.DC.attributes.MaxKeySize=10000
jcs.auxiliary.DC.attributes.OptimizeAtRemoveCount=300000
jcs.auxiliary.DC.attributes.OptimizeOnShutdown=true
jcs.auxiliary.DC.attributes.EventQueueType=POOLED
jcs.auxiliary.DC.attributes.EventQueuePoolName=disk_cache_event_queue

# Disk Cache pool
thread_pool.disk_cache_event_queue.boundarySize=50
thread_pool.disk_cache_event_queue.useBoundary=true
thread_pool.disk_cache_event_queue.maximumPoolSize=15
thread_pool.disk_cache_event_queue.minimumPoolSize=1
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.startUpSize=1
thread_pool.disk_cache_event_queue.whenBlockedPolicy=RUN
        
				
```

---

<a id="blockdiskcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/BlockDiskCache.html -->

<!-- page_index: 21 -->

<a id="blockdiskcache--block-disk-auxiliary-cache"></a>

## Block Disk Auxiliary Cache

The Block Disk Cache stores cached values on disk. Like
the Indexed Disk Cache, the Block Disk Cache keeps the
keys in memory. The Block Disk Cache stores the values
in a group of fixed size blocks, whereas the Indexed
Disk Cache writes items to disk in one chunk.

The Block Disk Cache has advantages over the normal
indexed model for regions where the size of the items
varies. Since all the blocks are the same size, the
recycle bin is very simple. It is just a list of block
numbers. Also, the Block Disk Cache will never need to
be optimized. Once the maximum number of keys is
reached, blocks will be reused.

<a id="blockdiskcache--size-limitation"></a>

## Size limitation

There are two ways to limit the cache size: using element
count and element size. When using element count, in disk
store there will be at most MaxKeySize elements (not disk
blocks). When using element size, there will be at most
KeySize kB of elements stored in the data file. As the Block
Disk Cache doesn't need optimization, the data file
will be not longer than specified. The limit does not
cover the key file size. The mode is chosen using DiskLimitType.
Allowed values are: COUNT and SIZE.

<a id="blockdiskcache--example-cache.ccf"></a>

### Example cache.ccf

```

					
##############################################################
##### DEFAULT REGION  ########################################

jcs.default=blockDiskCache
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=0
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache

##############################################################
##### AUXILIARY CACHES  ######################################

# Block Disk Cache
jcs.auxiliary.blockDiskCache=org.apache.commons.jcs3.auxiliary.disk.block.BlockDiskCacheFactory
jcs.auxiliary.blockDiskCache.attributes=org.apache.commons.jcs3.auxiliary.disk.block.BlockDiskCacheAttributes
jcs.auxiliary.blockDiskCache.attributes.DiskPath=target/test-sandbox/block-disk-cache-huge
jcs.auxiliary.blockDiskCache.attributes.MaxPurgatorySize=300000
jcs.auxiliary.blockDiskCache.attributes.MaxKeySize=1000000
jcs.auxiliary.blockDiskCache.attributes.blockSizeBytes=500
jcs.auxiliary.blockDiskCache.attributes.EventQueueType=SINGLE
#jcs.auxiliary.blockDiskCache.attributes.EventQueuePoolName=disk_cache_event_queue

##############################################################
################## THREAD POOL CONFIGURATION #################

# Default thread pool config
thread_pool.default.boundarySize=2000
thread_pool.default.maximumPoolSize=150
thread_pool.default.minimumPoolSize=4
thread_pool.default.keepAliveTime=350000
#RUN ABORT WAIT BLOCK DISCARDOLDEST
thread_pool.default.whenBlockedPolicy=RUN
thread_pool.default.startUpSize=4

# Disk Cache pool
thread_pool.disk_cache_event_queue.useBoundary=false
thread_pool.disk_cache_event_queue.minimumPoolSize=2
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.startUpSize=10
        
				
```

---

<a id="jdbcdiskcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/JDBCDiskCache.html -->

<!-- page_index: 22 -->

<a id="jdbcdiskcache--jdbc-disk-auxiliary-cache"></a>

## JDBC Disk Auxiliary Cache

The JDBC disk cache uses a relational database such as MySQL as a
persistent store. It works with Oracle, MySQL and HSQL. The cache
elements are serialized and written into a BLOB. Multiple regions
can share a single table. You can define multiple, differently
configured JDBC disk caches in one JCS instance. This allows you to
use different tables for different cache regions.

If you want to use numerous JDBC disk cache instances that talk
to the same database, you can configure them to share a connection
pool. You might want to use several different tables to partition
the data. Some operations, such as index building on a MyISAM
storage engine take longer if there are more items in the table.

<a id="jdbcdiskcache--example-1-cache.ccf-mysql"></a>

### Example #1 cache.ccf (MySQL)

```

					
##############################################################
################## DEFAULT CACHE REGION  #####################
# sets the default aux value for any non configured caches
jcs.default=MYSQL,RCluster
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=5000
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.cacheattributes.UseMemoryShrinker=true
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=7200
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=14400
jcs.default.elementattributes.IdleTime=14400
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true

##############################################################
################## CACHE REGIONS AVAILABLE ###################

##############################################################
################## AUXILIARY CACHES AVAILABLE ################
# MYSQL disk cache used for flight options
jcs.auxiliary.MYSQL=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheFactory
jcs.auxiliary.MYSQL.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheAttributes
jcs.auxiliary.MYSQL.attributes.userName=myUsername
jcs.auxiliary.MYSQL.attributes.password=myPassword
jcs.auxiliary.MYSQL.attributes.url=jdbc:mysql://localhost:3306/YOURDBNAME?autoReconnect=true
jcs.auxiliary.MYSQL.attributes.driverClassName=com.mysql.jdbc.Driver
jcs.auxiliary.MYSQL.attributes.tableName=JCS_STORE
jcs.auxiliary.MYSQL.attributes.testBeforeInsert=false
jcs.auxiliary.MYSQL.attributes.maxActive=100
jcs.auxiliary.MYSQL.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.MYSQL.attributes.UseDiskShrinker=true
jcs.auxiliary.MYSQL.attributes.ShrinkerInterval=1800
jcs.auxiliary.MYSQL.attributes.allowRemoveAll=false
jcs.auxiliary.MYSQL.attributes.EventQueueType=POOLED
jcs.auxiliary.MYSQL.attributes.EventQueuePoolName=disk_cache_event_queue

##############################################################
################## OPTIONAL THREAD POOL CONFIGURATION #########
# Disk Cache pool
thread_pool.disk_cache_event_queue.useBoundary=true
thread_pool.disk_cache_event_queue.boundarySize=1000
thread_pool.disk_cache_event_queue.maximumPoolSize=50
thread_pool.disk_cache_event_queue.minimumPoolSize=10
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.whenBlockedPolicy=RUN
thread_pool.disk_cache_event_queue.startUpSize=10
        
				
```

<a id="jdbcdiskcache--example-2-cache.ccf-mysql"></a>

### Example #2 cache.ccf (MySQL)

This example uses two JDBC Disk Cache instances and a shared connection pool.

```

					
jcs.default=JDBC_0
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=100
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.cacheattributes.UseMemoryShrinker=false
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=700
jcs.default.elementattributes.IdleTime=1800
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true

# #############################################################
# ################# CONFIGURED REGIONS ########################

jcs.region.testCache1=JDBC_1
jcs.region.testCache1.cacheattributes.MaxObjects=10000

# #############################################################
# ################# AUXILIARY CACHES AVAILABLE ################
# JDBC disk cache
jcs.auxiliary.JDBC_0=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheFactory
jcs.auxiliary.JDBC_0.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheAttributes
jcs.auxiliary.JDBC_0.attributes.tableName=JCS_STORE_0
jcs.auxiliary.JDBC_0.attributes.testBeforeInsert=false
jcs.auxiliary.JDBC_0.attributes.allowRemoveAll=true
jcs.auxiliary.JDBC_0.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.JDBC_0.attributes.connectionPoolName=MySharedPool
jcs.auxiliary.JDBC_0.attributes.EventQueueType=POOLED
jcs.auxiliary.JDBC_0.attributes.EventQueuePoolName=disk_cache_event_queue

jcs.auxiliary.JDBC_1=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheFactory
jcs.auxiliary.JDBC_1.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheAttributes
jcs.auxiliary.JDBC_1.attributes.tableName=JCS_STORE_1
jcs.auxiliary.JDBC_1.attributes.testBeforeInsert=false
jcs.auxiliary.JDBC_1.attributes.allowRemoveAll=true
jcs.auxiliary.JDBC_1.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.JDBC_1.attributes.connectionPoolName=MySharedPool
jcs.auxiliary.JDBC_1.attributes.EventQueueType=POOLED
jcs.auxiliary.JDBC_1.attributes.EventQueuePoolName=disk_cache_event_queue

# #############################################################
# ######## OPTIONAL SHARED CONNECTION POOL CONFIGURATION ######
# My Shared Pool

jcs.jdbcconnectionpool.MySharedPool.attributes.userName=sa
jcs.jdbcconnectionpool.MySharedPool.attributes.password=
jcs.jdbcconnectionpool.MySharedPool.attributes.url=jdbc:hsqldb:target/cache_hsql_db
jcs.jdbcconnectionpool.MySharedPool.attributes.driverClassName=org.hsqldb.jdbcDriver
jcs.jdbcconnectionpool.MySharedPool.attributes.maxActive=15

# #############################################################
# ################# OPTIONAL THREAD POOL CONFIGURATION #########
# Disk Cache pool
thread_pool.disk_cache_event_queue.useBoundary=false
thread_pool.disk_cache_event_queue.boundarySize=500
thread_pool.disk_cache_event_queue.maximumPoolSize=15
thread_pool.disk_cache_event_queue.minimumPoolSize=10
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.whenBlockedPolicy=RUN
thread_pool.disk_cache_event_queue.startUpSize=10
        
				
```

<a id="jdbcdiskcache--example-3-cache.ccf-jndi"></a>

### Example #3 cache.ccf (JNDI)

This example uses the two JDBC Disk Cache instances from the example above and a JNDI data source.

```

                    
jcs.default=JDBC_0
jcs.default.cacheattributes=org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=100
jcs.default.cacheattributes.MemoryCacheName=org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
jcs.default.cacheattributes.UseMemoryShrinker=false
jcs.default.cacheattributes.MaxMemoryIdleTimeSeconds=3600
jcs.default.cacheattributes.ShrinkerIntervalSeconds=60
jcs.default.elementattributes=org.apache.commons.jcs3.engine.ElementAttributes
jcs.default.elementattributes.IsEternal=false
jcs.default.elementattributes.MaxLife=700
jcs.default.elementattributes.IdleTime=1800
jcs.default.elementattributes.IsSpool=true
jcs.default.elementattributes.IsRemote=true
jcs.default.elementattributes.IsLateral=true

# #############################################################
# ################# CONFIGURED REGIONS ########################

jcs.region.testCache1=JDBC_1
jcs.region.testCache1.cacheattributes.MaxObjects=10000

# #############################################################
# ################# AUXILIARY CACHES AVAILABLE ################
# JDBC disk cache
jcs.auxiliary.JDBC_0=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheFactory
jcs.auxiliary.JDBC_0.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheAttributes
jcs.auxiliary.JDBC_0.attributes.tableName=JCS_STORE_0
jcs.auxiliary.JDBC_0.attributes.testBeforeInsert=false
jcs.auxiliary.JDBC_0.attributes.allowRemoveAll=true
jcs.auxiliary.JDBC_0.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.JDBC_0.attributes.connectionPoolName=JNDI
jcs.auxiliary.JDBC_0.attributes.EventQueueType=POOLED
jcs.auxiliary.JDBC_0.attributes.EventQueuePoolName=disk_cache_event_queue

jcs.auxiliary.JDBC_1=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheFactory
jcs.auxiliary.JDBC_1.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheAttributes
jcs.auxiliary.JDBC_1.attributes.tableName=JCS_STORE_1
jcs.auxiliary.JDBC_1.attributes.testBeforeInsert=false
jcs.auxiliary.JDBC_1.attributes.allowRemoveAll=true
jcs.auxiliary.JDBC_1.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.JDBC_1.attributes.connectionPoolName=JNDI
jcs.auxiliary.JDBC_1.attributes.EventQueueType=POOLED
jcs.auxiliary.JDBC_1.attributes.EventQueuePoolName=disk_cache_event_queue

# #############################################################
# ######## OPTIONAL JNDI CONNECTION POOL CONFIGURATION ######
# JNDI Pool

jcs.jdbcconnectionpool.JNDI.attributes.jndiPath=java:comp/env/jdbc/MyDB
jcs.jdbcconnectionpool.JNDI.attributes.jndiTTL=300000

# #############################################################
# ################# OPTIONAL THREAD POOL CONFIGURATION #########
# Disk Cache pool
thread_pool.disk_cache_event_queue.useBoundary=false
thread_pool.disk_cache_event_queue.boundarySize=500
thread_pool.disk_cache_event_queue.maximumPoolSize=15
thread_pool.disk_cache_event_queue.minimumPoolSize=10
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.whenBlockedPolicy=RUN
thread_pool.disk_cache_event_queue.startUpSize=10
        
                
```

<a id="jdbcdiskcache--table-creation-script-mysql"></a>

### Table Creation Script (MySQL)

```

					
drop TABLE JCS_STORE;

CREATE TABLE JCS_STORE
(
  CACHE_KEY                   VARCHAR(250)          NOT NULL,
  REGION                      VARCHAR(250)          NOT NULL,
  ELEMENT                     BLOB,
  CREATE_TIME                 DATETIME,
  CREATE_TIME_SECONDS         BIGINT,
  MAX_LIFE_SECONDS            BIGINT,
  SYSTEM_EXPIRE_TIME_SECONDS  BIGINT,
  IS_ETERNAL                  CHAR(1),
  PRIMARY KEY (CACHE_KEY, REGION)
);

alter table JCS_STORE MAX_ROWS = 10000000;

alter table JCS_STORE AVG_ROW_LENGTH = 2100;

create index JCS_STORE_DELETE_IDX on JCS_STORE (SYSTEM_EXPIRE_TIME_SECONDS,IS_ETERNAL,REGION);
        
				
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="jdbcdiskcacheproperties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/JDBCDiskCacheProperties.html -->

<!-- page_index: 23 -->

<a id="jdbcdiskcacheproperties--jdbc-disk-auxiliary-cache-configuration"></a>

## JDBC Disk Auxiliary Cache Configuration

The following properties apply to the JDBC Disk Cache
plugin.

<a id="jdbcdiskcacheproperties--jdbc-disk-configuration-properties"></a>

### JDBC Disk Configuration Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| MaxPurgatorySize | The maximum number of items allowed in the queue of items to be written to disk. | N | 5000 |
| url | The database url. The database name will be added to this value to create the full database url. | N |  |
| database | This is appended to the url. | N |  |
| driverClassName | The class name of the driver to talk to your database. | N |  |
| userName | The database user name. | N |  |
| password | The database user password. | N |  |
| jndiPath | The JNDI lookup path in the form `java:comp/env/jdbc/MyDB`. This entry is preferred over the set of `url`, `driverClassName`, `userName` and `password`. | N |  |
| jndiTTL | The time between two JNDI lookups in ms. | N | 0 |
| tableName | The name of the table. | N | JCS\_STORE |
| testBeforeInsert | Should the disk cache do a select before trying to insert new element on update, or should it try to insert and handle the error. | N | true |
| maxActive | This sets the maximum number of connections allowed. | Y |  |
| allowRemoveAll | Should the disk cache honor remove all (i.e. clear) requests. You might set this to false to prevent someone from accidentally clearing out an entire database. | N | true |
| UseDiskShrinker | Should the disk cache try to delete expired items from the database. | N | true |
| ShrinkerInterval | How often should the disk shrinker run (in seconds). | N | 300 |

<a id="jdbcdiskcacheproperties--example-configuration"></a>

### Example Configuration

```

					
##############################################################
################## AUXILIARY CACHES AVAILABLE ################
# JDBC disk cache
jcs.auxiliary.JDBC=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheFactory
jcs.auxiliary.JDBC.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheAttributes
jcs.auxiliary.JDBC.attributes.userName=sa
jcs.auxiliary.JDBC.attributes.password=
jcs.auxiliary.JDBC.attributes.url=jdbc:hsqldb:
jcs.auxiliary.JDBC.attributes.database=target/cache_hsql_db
jcs.auxiliary.JDBC.attributes.driverClassName=org.hsqldb.jdbcDriver
jcs.auxiliary.JDBC.attributes.tableName=JCS_STORE2
jcs.auxiliary.JDBC.attributes.testBeforeInsert=false
jcs.auxiliary.JDBC.attributes.maxActive=15
jcs.auxiliary.JDBC.attributes.allowRemoveAll=true
jcs.auxiliary.JDBC.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.JDBC.attributes.UseDiskShrinker=true
jcs.auxiliary.JDBC.attributes.ShrinkerInterval=300
        
				
```

<a id="jdbcdiskcacheproperties--jdbc-disk-event-queue-configuration"></a>

### JDBC Disk Event Queue Configuration

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| EventQueueType | This should be either SINGLE or POOLED. By default the single style pool is used. The single style pool uses a single thread per event queue. That thread is killed whenever the queue is inactive for 30 seconds. Since the disk cache uses an event queue for every region, if you have many regions and they are all active, you will be using many threads. To limit the number of threads, you can configure the disk cache to use the pooled event queue. Using more threads than regions will not add any benefit for the indexed disk cache, since only one thread can read or write at a time for a single region. | N | SINGLE |
| EventQueuePoolName | This is the name of the pool to use. It is required if you choose the POOLED event queue type, otherwise it is ignored. | Y | n/a |

<a id="jdbcdiskcacheproperties--example-configuration-using-thread-pool"></a>

### Example Configuration Using Thread Pool

```

					
##############################################################
################## AUXILIARY CACHES AVAILABLE ################
# JDBC disk cache
jcs.auxiliary.JDBC=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheFactory
jcs.auxiliary.JDBC.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.JDBCDiskCacheAttributes
jcs.auxiliary.JDBC.attributes.userName=sa
jcs.auxiliary.JDBC.attributes.password=
jcs.auxiliary.JDBC.attributes.url=jdbc:hsqldb:
jcs.auxiliary.JDBC.attributes.database=target/cache_hsql_db
jcs.auxiliary.JDBC.attributes.driverClassName=org.hsqldb.jdbcDriver
jcs.auxiliary.JDBC.attributes.tableName=JCS_STORE2
jcs.auxiliary.JDBC.attributes.testBeforeInsert=false
jcs.auxiliary.JDBC.attributes.maxActive=15
jcs.auxiliary.JDBC.attributes.allowRemoveAll=true
jcs.auxiliary.JDBC.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.JDBC.attributes.UseDiskShrinker=true
jcs.auxiliary.JDBC.attributes.ShrinkerInterval=300
jcs.auxiliary.JDBC.attributes.EventQueueType=POOLED
jcs.auxiliary.JDBC.attributes.EventQueuePoolName=disk_cache_event_queueue

##############################################################
################## OPTIONAL THREAD POOL CONFIGURATION #########
# Disk Cache pool
thread_pool.disk_cache_event_queue.useBoundary=false
thread_pool.disk_cache_event_queue.boundarySize=500
thread_pool.disk_cache_event_queue.maximumPoolSize=15
thread_pool.disk_cache_event_queue.minimumPoolSize=10
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.whenBlockedPolicy=RUN
thread_pool.disk_cache_event_queue.startUpSize=10
        
				
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="mysqldiskcacheproperties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/MySQLDiskCacheProperties.html -->

<!-- page_index: 24 -->

<a id="mysqldiskcacheproperties--mysql-disk-auxiliary-cache-configuration"></a>

## MySQL Disk Auxiliary Cache Configuration

The MySQL Disk Cache uses all of the JDBC Disk Cache
properties. It adds a few of its own. The following
properties only apply to the MySQL Disk Cache plugin.

<a id="mysqldiskcacheproperties--mysql-disk-configuration-properties"></a>

### MySQL Disk Configuration Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| optimizationSchedule | For now this is a simple comma delimited list of HH:MM:SS times to optimize the table. If none is supplied, then no optimizations will be performed. In the future we can add a cron like scheduling system. This was created to meet a pressing need to optimize fragmented MyISAM tables. When the table becomes fragmented, it starts to take a long time to run the shrinker that deletes expired elements. Setting the value to "03:01,15:00" will cause the optimizer to run at 3 am and at 3 pm. | N | null |
| balkDuringOptimization | If this is true, then when JCS is optimizing the table it will return null from get requests and do nothing for put requests. If you are using the remote cache and have a failover server configured in a remote cache cluster, and you allow clustered gets, the primary server will act as a proxy to the failover. This way, optimization should have no impact for clients of the remote cache. | N | true |

<a id="mysqldiskcacheproperties--example-configuration"></a>

### Example Configuration

```

					
##############################################################
################## AUXILIARY CACHES AVAILABLE ################
# MYSQL disk cache
jcs.auxiliary.MYSQL=org.apache.commons.jcs3.auxiliary.disk.jdbc.mysql.MySQLDiskCacheFactory
jcs.auxiliary.MYSQL.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.mysql.MySQLDiskCacheAttributes
jcs.auxiliary.MYSQL.attributes.userName=sa
jcs.auxiliary.MYSQL.attributes.password=
jcs.auxiliary.MYSQL.attributes.url=jdbc:hsqldb:target/cache_hsql_db
jcs.auxiliary.MYSQL.attributes.driverClassName=org.hsqldb.jdbcDriver
jcs.auxiliary.MYSQL.attributes.tableName=JCS_STORE_MYSQL
jcs.auxiliary.MYSQL.attributes.testBeforeInsert=false
jcs.auxiliary.MYSQL.attributes.maxActive=15
jcs.auxiliary.MYSQL.attributes.allowRemoveAll=true
jcs.auxiliary.MYSQL.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.MYSQL.attributes.optimizationSchedule=12:34:56,02:34:54
jcs.auxiliary.MYSQL.attributes.balkDuringOptimization=true
        
				
```

<a id="mysqldiskcacheproperties--mysql-disk-event-queue-configuration"></a>

### MySQL Disk Event Queue Configuration

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| EventQueueType | This should be either SINGLE or POOLED. By default the single style pool is used. The single style pool uses a single thread per event queue. That thread is killed whenever the queue is inactive for 30 seconds. Since the disk cache uses an event queue for every region, if you have many regions and they are all active, you will be using many threads. To limit the number of threads, you can configure the disk cache to use the pooled event queue. Using more threads than regions will not add any benefit for the indexed disk cache, since only one thread can read or write at a time for a single region. | N | SINGLE |
| EventQueuePoolName | This is the name of the pool to use. It is required if you choose the POOLED event queue type, otherwise it is ignored. | Y | n/a |

<a id="mysqldiskcacheproperties--example-configuration-using-thread-pool"></a>

### Example Configuration Using Thread Pool

```

					
##############################################################
################## AUXILIARY CACHES AVAILABLE ################
# MYSQL disk cache
jcs.auxiliary.MYSQL=org.apache.commons.jcs3.auxiliary.disk.jdbc.mysql.MySQLDiskCacheFactory
jcs.auxiliary.MYSQL.attributes=org.apache.commons.jcs3.auxiliary.disk.jdbc.mysql.MySQLDiskCacheAttributes
jcs.auxiliary.MYSQL.attributes.userName=sa
jcs.auxiliary.MYSQL.attributes.password=
jcs.auxiliary.MYSQL.attributes.url=jdbc:hsqldb:target/cache_hsql_db
jcs.auxiliary.MYSQL.attributes.driverClassName=org.hsqldb.jdbcDriver
jcs.auxiliary.MYSQL.attributes.tableName=JCS_STORE_MYSQL
jcs.auxiliary.MYSQL.attributes.testBeforeInsert=false
jcs.auxiliary.MYSQL.attributes.maxActive=15
jcs.auxiliary.MYSQL.attributes.allowRemoveAll=true
jcs.auxiliary.MYSQL.attributes.MaxPurgatorySize=10000000
jcs.auxiliary.MYSQL.attributes.optimizationSchedule=12:34:56,02:34:54
jcs.auxiliary.MYSQL.attributes.balkDuringOptimization=true
jcs.auxiliary.MYSQL.attributes.EventQueueType=POOLED
jcs.auxiliary.MYSQL.attributes.EventQueuePoolName=disk_cache_event_queue

##############################################################
################## OPTIONAL THREAD POOL CONFIGURATION #########
# Disk Cache pool
thread_pool.disk_cache_event_queue.useBoundary=false
thread_pool.disk_cache_event_queue.boundarySize=500
thread_pool.disk_cache_event_queue.maximumPoolSize=15
thread_pool.disk_cache_event_queue.minimumPoolSize=10
thread_pool.disk_cache_event_queue.keepAliveTime=3500
thread_pool.disk_cache_event_queue.whenBlockedPolicy=RUN
thread_pool.disk_cache_event_queue.startUpSize=10
        
				
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="remoteauxcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/RemoteAuxCache.html -->

<!-- page_index: 25 -->

<a id="remoteauxcache--remote-auxiliary-cache-client-server"></a>

## Remote Auxiliary Cache Client / Server

The Remote Auxiliary Cache is an optional plug in for
JCS. It is intended for use in multi-tiered systems to
maintain cache consistency. It uses a highly reliable
RMI client server framework that currently allows for
any number of clients. Using a listener id allows
multiple clients running on the same machine to connect
to the remote cache server. All cache regions on one
client share a listener per auxiliary, but register
separately. This minimizes the number of connections
necessary and still avoids unnecessary updates for
regions that are not configured to use the remote cache.

Local remote cache clients connect to the remote cache
on a configurable port and register a listener to
receive cache update callbacks at a configurable port.

If there is an error connecting to the remote server or
if an error occurs in transmission, the client will
retry for a configurable number of tries before moving
into a failover-recovery mode. If failover servers are
configured the remote cache clients will try to register
with other failover servers in a sequential order. If a
connection is made, the client will broadcast all
relevant cache updates to the failover server while
trying periodically to reconnect with the primary
server. If there are no failovers configured the client
will move into a zombie mode while it tries to
re-establish the connection. By default, the cache
clients run in an optimistic mode and the failure of the
communication channel is detected by an attempted update
to the server. A pessimistic mode is configurable so
that the clients will engage in active status checks.

The remote cache server broadcasts updates to listeners
other than the originating source. If the remote cache
fails to propagate an update to a client, it will retry
for a configurable number of tries before de-registering
the client.

The cache hub communicates with a facade that implements
a zombie pattern (balking facade) to prevent blocking.
Puts and removals are queued and occur asynchronously in
the background. Get requests are synchronous and can
potentially block if there is a communication problem.

By default client updates are light weight. The client
listeners are configured to remove elements form the
local cache when there is a put order from the remote.
This allows the client memory store to control the
memory size algorithm from local usage, rather than
having the usage patterns dictated by the usage patterns
in the system at large.

When using a remote cache the local cache hub will
propagate elements in regions configured for the remote
cache if the element attributes specify that the item to
be cached can be sent remotely. By default there are no
remote restrictions on elements and the region will
dictate the behavior. The order of auxiliary requests is
dictated by the order in the configuration file. The
examples are configured to look in memory, then disk, then remote caches. Most elements will only be retrieved
from the remote cache once, when they are not in memory
or disk and are first requested, or after they have been
invalidated.

<a id="remoteauxcache--client-configuration"></a>

### Client Configuration

The configuration is fairly straightforward and is
done in the auxiliary cache section of the
`cache.ccf`
configuration file. In the example below, I created
a Remote Auxiliary Cache Client referenced by
`RFailover`
.

This auxiliary cache will use
`localhost:1102`
as its primary remote cache server and will attempt
to failover to
`localhost:1103`
if the primary is down.

Setting
`RemoveUponRemotePut`
to
`false`
would cause remote puts to be translated into put
requests to the client region. By default it is
`true`
, causing remote put requests to be issued as
removes at the client level. For groups the put
request functions slightly differently: the item
will be removed, since it is no longer valid in its
current form, but the list of group elements will be
updated. This way the client can maintain the
complete list of group elements without the burden
of storing all of the referenced elements. Session
distribution works in this half-lazy replication
mode.

Setting
`GetOnly`
to
`true`
would cause the remote cache client to stop
propagating updates to the remote server, while
continuing to get items from the remote store.

```

					
# Remote RMI Cache set up to failover jcs.auxiliary.RFailover=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheFactory jcs.auxiliary.RFailover.attributes=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes jcs.auxiliary.RFailover.attributes.FailoverServers=localhost:1102,localhost:1103
jcs.auxiliary.RFailover.attributes.RemoveUponRemotePut=true
jcs.auxiliary.RFailover.attributes.GetOnly=false
        
				
```

This cache region is setup to use a disk cache and
the remote cache configured above:

```

					
#Regions preconfigured for caching
jcs.region.testCache1=DC,RFailover
jcs.region.testCache1.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.region.testCache1.cacheattributes.MaxObjects=1000
jcs.region.testCache1.cacheattributes.MemoryCacheName=
    org.apache.commons.jcs3.engine.memory.lru.LRUMemoryCache
        
				
```

<a id="remoteauxcache--server-configuration"></a>

### Server Configuration

The remote cache configuration is growing. For now, the configuration is done at the top of the
`remote.cache.ccf`
file. The
`startRemoteCache`
script passes the configuration file name to the
server when it starts up. The configuration
parameters below will create a remote cache server
that listens to port
`1102`
and performs call backs on the
`jcs.remotecache.serverattributes.servicePort`
, also specified as port
`1102`
.

```

					
# Registry used to register and provide the
# IRemoteCacheService service.
registry.host=localhost
registry.port=1102
# call back port to local caches.
jcs.remotecache.serverattributes.servicePort=1102
# rmi socket factory timeout
jcs.remotecache.serverattributes.rmiSocketFactoryTimeoutMillis=5000
# cluster setting
jcs.remotecache.serverattributes.LocalClusterConsistency=true
jcs.remotecache.serverattributes.AllowClusterGet=true
        
				
```

Remote servers can be chained (or clustered). This
allows gets from local caches to be distributed
between multiple remote servers. Since gets are the
most common operation for caches, remote server
chaining can help scale a caching solution.

The
`LocalClusterConsistency`
setting tells the remote cache server if it should
broadcast updates received from other cluster
servers to registered local caches.

The
`AllowClusterGet`
setting tells the remote cache server whether it
should allow the cache to look in non-local
auxiliaries for items if they are not present.
Basically, if the get request is not from a cluster
server, the cache will treat it as if it originated
locally. If the get request originated from a
cluster client, then the get will be restricted to
local (i.e. memory and disk) auxiliaries. Hence, cluster gets can only go one server deep. They
cannot be chained. By default this setting is true.

To use remote server clustering, the remote cache
will have to be told what regions to cluster. The
configuration below will cluster all
non-preconfigured regions with
`RCluster1`
.

```

					
# sets the default aux value for any non configured caches
jcs.default=DC,RCluster1
jcs.default.cacheattributes=
    org.apache.commons.jcs3.engine.CompositeCacheAttributes
jcs.default.cacheattributes.MaxObjects=1000

jcs.auxiliary.RCluster1=
    org.apache.commons.jcs3.auxiliary.remote.RemoteCacheFactory
jcs.auxiliary.RCluster1.attributes=
    org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes
jcs.auxiliary.RCluster1.attributes.RemoteTypeName=CLUSTER
jcs.auxiliary.RCluster1.attributes.RemoveUponRemotePut=false
jcs.auxiliary.RCluster1.attributes.ClusterServers=localhost:1103
jcs.auxiliary.RCluster1.attributes.GetOnly=false
        
				
```

RCluster1 is configured to talk to a remote server
at
`localhost:1103`
. Additional servers can be added in a comma
separated list.

If we startup another remote server listening to
port 1103, (ServerB) then we can have that server
talk to the server we have been configuring, listening at 1102 (ServerA). This would allow us to
set some local caches to talk to ServerA and some to
talk to ServerB. The two remote servers will
broadcast all puts and removes between themselves, and the get requests from local caches could be
divided. The local caches do not need to know
anything about the server chaining configuration, unless you want to use a standby, or failover
server.

We could also use ServerB as a hot standby. This can
be done in two ways. You could have all local caches
point to ServerA as a primary and ServerB as a
secondary. Alternatively, you can set ServerA as the
primary for some local caches and ServerB for the
primary for some others.

The local cache configuration below uses ServerA as
a primary and ServerB as a backup. More than one
backup can be defined, but only one will be used at
a time. If the cache is connected to any server
except the primary, it will try to restore the
primary connection indefinitely, at 20 second
intervals.

```

					
# Remote RMI Cache set up to failover jcs.auxiliary.RFailover=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheFactory jcs.auxiliary.RFailover.attributes=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes jcs.auxiliary.RFailover.attributes.FailoverServers=localhost:1102,localhost:1103
	jcs.auxiliary.RC.attributes.RemoveUponRemotePut=true
	jcs.auxiliary.RFailover.attributes.GetOnly=false
	        
				
```

<a id="remoteauxcache--server-startup-shutdown"></a>

### Server Startup / Shutdown

It is highly recommended that you embed the Remote
Cache Server in a Servlet container such as Tomcat.
Running inside Tomcat allows you to use the
JCSAdmin.jsp page. It also takes care of the
complexity of creating working startup and shutdown
scripts.

JCS provides a convenient startup servlet for this
purpose. It will start the registry and bind the
JCS server to the registry. To use the startup
servlet, add the following to the web.xml file and
make sure you have the cache.ccf file in the
WEB-INF/classes directly of your war file.

```

					
    <servlet>
        <servlet-name>JCSRemoteCacheStartupServlet</servlet-name>
        <servlet-class>
             org.apache.commons.jcs3.auxiliary.remote.server.RemoteCacheStartupServlet
        </servlet-class>
        <load-on-startup>1</load-on-startup>
    </servlet>


    <servlet-mapping>
        <servlet-name>JCSRemoteCacheStartupServlet</servlet-name>
        <url-pattern>/jcs</url-pattern>
    </servlet-mapping>

				
```

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="remotecacheproperties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/RemoteCacheProperties.html -->

<!-- page_index: 26 -->

<a id="remotecacheproperties--remote-auxiliary-cache-configuration"></a>

## Remote Auxiliary Cache Configuration

The following properties apply to the Remote Cache
plugin.

<a id="remotecacheproperties--remote-client-configuration-properties"></a>

### Remote Client Configuration Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| FailoverServers | This is a comma separated list of remote servers to use. They should be specified in the host:port format. The first server in the list will be used as the primary server. If the connection is lost with the primary, the cache will try to connect to the next server in the list. If a connection is successfully established with a failover server, then the cache will attempt to restore the conenction with the primary server. | Y | n/a |
| LocalPort | This is the port on which the client will receive callbacks from the remote server. If it is not specified, then some port in the default range used by RMI will be the callback port. | N | default RMI port range |
| RemoveUponRemotePut | If you configure the cache to remove upon a remote put, this means that the client will translate updates into removes. The client will remove any local copy it has of the object rather than storing the new version. If you have sticky load balancing across your client servers, then it would make sense to set RemoveUponRemotePut to true if the data is mostly client specific. If the data is re-usable, the you should most likely set this option to false, which is the default. | N | true |
| RmiSocketFactoryTimeoutMillis | If this is greater than 0, then a custom socket factory will be installed in the VM. It will then use this timeout for all RMI communication. | N | 5000 |
| GetOnly | GetOnly is somewhat misnamed. If it is set to true, then the client will not send updates or removes to the remote server. It can still receive updates and removes. | N | false |
| Receive | By default Receive is set to true. This means that the remote client will receive updates and removes from the remote server. If you set Receive to false, the remote client will not register a listener with the remote server. This means that the client can send update and remove requests to the server, and it can get from the server, but it will never receive notifications from the server. You might configure Receive to false if you just want to use the remote server as a data store. For instance, you may back the Remote Cache Server with the JDBC disk cache and set Receive=false when you have a high put and low read region. | N | true |
| ZombieQueueMaxSize | The number of elements the zombie queue will hold. This queue is used to store events if we lose our connection with the server. | N | 1000 |

<a id="remotecacheproperties--example-configuration"></a>

### Example Configuration

```

					
# This remote client does not receive
jcs.auxiliary.RC=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheFactory
jcs.auxiliary.RC.attributes=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes
jcs.auxiliary.RC.attributes.FailoverServers=localhost:1101,localhost:1102
jcs.auxiliary.RC.attributes.LocalPort=1201
jcs.auxiliary.RC.attributes.RemoveUponRemotePut=false
jcs.auxiliary.RC.attributes.RmiSocketFactoryTimeoutMillis=5000
jcs.auxiliary.RC.attributes.GetOnly=false
jcs.auxiliary.RC.attributes.Receive=false
        
				
```

---

<a id="remotehttpcacheproperties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/RemoteHttpCacheProperties.html -->

<!-- page_index: 27 -->

<a id="remotehttpcacheproperties--remote-auxiliary-http-cache-configuration"></a>

## Remote Auxiliary Http Cache Configuration

The following properties apply to the Remote Http Cache plugin.

<a id="remotehttpcacheproperties--remote-http-client-configuration-properties"></a>

### Remote Http Client Configuration Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| url | This is the full url for the http service. | Y | n/a |
| maxConnectionsPerHost | Maximum simultaneous connections per host. | N | 100 |
| socketTimeoutMillis | Read timeout. | N | 3000 |
| connectionTimeoutMillis | Connection timeout. | N | 5000 |
| httpVersion | The http version to use. | N | 1.1 |
| includeCacheNameAsParameter | Should the cache name be appended to the url. | N | true |
| includeKeysAndPatternsAsParameter | Should the key be appended to the url. | N | true |
| includeRequestTypeasAsParameter | Should the request type be appended to the url. | N | true |
| remoteHttpClientClassName | This allows you to specify your own client implementation. | N | RemoteHttpCacheClient.class.getName() |
| ZombieQueueMaxSize | The number of elements the zombie queue will hold. This queue is used to store events if we lose our connection with the server. | N | 1000 |

<a id="remotehttpcacheproperties--example-configuration"></a>

### Example Configuration

```

					
# This remote client does not receive
jcs.auxiliary.RC=org.apache.commons.jcs3.auxiliary.remote.http.client.RemoteCacheFactory
jcs.auxiliary.RC.attributes=org.apache.commons.jcs3.auxiliary.remote.RemoteCacheAttributes
jcs.auxiliary.RC.attributes.FailoverServers=localhost:1101,localhost:1102
jcs.auxiliary.RC.attributes.LocalPort=1201
jcs.auxiliary.RC.attributes.RemoveUponRemotePut=false
jcs.auxiliary.RC.attributes.RmiSocketFactoryTimeoutMillis=5000
jcs.auxiliary.RC.attributes.GetOnly=false
jcs.auxiliary.RC.attributes.Receive=false
        
				
```

---

<a id="lateraltcpauxcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/LateralTCPAuxCache.html -->

<!-- page_index: 28 -->

<a id="lateraltcpauxcache--lateral-tcp-auxiliary-cache"></a>

## Lateral TCP Auxiliary Cache

The TCP Lateral Auxiliary Cache is an optional plug in for the
JCS. It is primarily intended to broadcast puts and removals to
other local caches, though it can also get cached objects. It
functions by opening up a `SocketServer` that
listens to a configurable port and by creating
`Socket` connections with other local cache
`SocketServers`. It can be configured to connect to
any number of servers.

If there is an error connecting to another server or if an error
occurs in transmission, it will move into a recovery mode. In
recovery mode the TCP Lateral Auxiliary Cache will continue to
communicate with healthy servers while it tries to restore the
connection with the server that is in error.

The cache hub communicates with a facade that implements a
zombie pattern (balking facade) to prevent blocking. Puts and
removals are queued and occur synchronously in the background.
Get requests are synchronous and can potentially block for a
configurable interval if there is a communication problem.

<a id="lateraltcpauxcache--non-udp-discovery-configuration"></a>

### Non-UDP Discovery Configuration

The configuration is fairly straightforward and is done in the
auxiliary cache section of the `cache.ccf`
configuration file. In the example below, I created a TCP
Lateral Auxiliary Cache referenced by `LTCP`. It
connects to two servers defined in a comma separated list in
the `TcpServers` attribute. It listens to port
`1110` and does `AllowGet`.
Setting `AllowGet`
equal to `false` would cause the auxiliary cache to
return `null` from any get request. In most cases this
attribute should be set to `false`, since if the
lateral caches were properly configured, the elements in one
would be present in all.

```

jcs.auxiliary.LTCP=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.LateralTCPCacheFactory
jcs.auxiliary.LTCP.attributes=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.TCPLateralCacheAttributes
jcs.auxiliary.LTCP.attributes.TcpServers=localhost:1111,localhost:1112
jcs.auxiliary.LTCP.attributes.TcpListenerPort=1110
jcs.auxiliary.LTCP.attributes.AllowGet=true
        
```

A mostly configurationless mode is available for the TCP
lateral cache if you use the [UDP Discovery](#lateraludpdiscovery)
mechanism.

<a id="lateraltcpauxcache--send-only-configuration"></a>

### Send Only Configuration

You can configure the TCP lateral cache to operate
in send only mode by setting the `Receive` attribute
to false. By default the receive attribute is true.
When it is set to false, the lateral cache will not
establish a socket server.

Setting receive to false allows you to broadcast puts
and removes, but not receive any. This is useful for
nodes of an application that produce data, but are not
involved in data retrieval.

The configuration below is the same as above, except the
`Receive` attribute is set to false. It also uses UDP
discovery to find the servers, rather than listing them in the
servers attribute.

```

jcs.auxiliary.LTCP=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.LateralTCPCacheFactory
jcs.auxiliary.LTCP.attributes=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.TCPLateralCacheAttributes
#jcs.auxiliary.LTCP.attributes.TcpServers=
jcs.auxiliary.LTCP.attributes.TcpListenerPort=1118
jcs.auxiliary.LTCP.attributes.UdpDiscoveryAddr=228.5.6.8
jcs.auxiliary.LTCP.attributes.UdpDiscoveryPort=6780
jcs.auxiliary.LTCP.attributes.UdpDiscoveryEnabled=true
jcs.auxiliary.LTCP.attributes.Receive=true
jcs.auxiliary.LTCP.attributes.AllowGet=false
jcs.auxiliary.LTCP.attributes.IssueRemoveOnPut=false
jcs.auxiliary.LTCP.attributes.FilterRemoveByHashCode=false
        
```

<a id="lateraltcpauxcache--potential-issues"></a>

### Potential Issues

The TCP Lateral Auxiliary Cache can provide a high level of
consistency but it does not guarantee consistency between
caches. A put for the same object could be issued in two
different local caches. Since the transmission is queued, a
situation could occur where the item put last in one cache is
overridden by a put request from another local cache. The two
local caches could potentially have different versions of the
same item. Like most caches, this is intended for high get
and low put utilization, and this occurrence would hint at
improper usage. The RMI Remote cache makes this situation a
bit less likely to occur, since the default behavior is to
remove local copies on put operations. If either local cache
needed the item put in the above situation, it would have to
go remote to retrieve it. Both local copies would have been
expired and would end up using the same version, though it is
possible that the version stored remotely would not be the
last version created. The OCS4J tries to implement a locking
system to prevent this from occurring, but the locking system
itself could suffer from similar problems (when granting locks
from two roughly simultaneous lock requests) and it would
create a significant burden on all the caches involved. Since
this situation would be extremely rare and is nearly
impossible to solve practically, for now JCS will not offer
any type of locking.

<a id="lateraltcpauxcache--recent"></a>

### Recent

I added a `IssueRemoveOnPut` attribute that
causes the lateral cache to remove an element from the
cache rather than inserting it when a put. This allows the local caches to
dictate their own memory usage pattern.

Copyright © 2002-2024
[The Apache Software Foundation](https://www.apache.org/).
All Rights Reserved.

Apache Commons, Apache Commons JCS, Apache, the Apache feather logo, and the Apache Commons project logos are trademarks of The Apache Software Foundation.
All other marks mentioned may be trademarks or registered trademarks of their respective owners.

---

<a id="lateraltcpproperties"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/LateralTCPProperties.html -->

<!-- page_index: 29 -->

<a id="lateraltcpproperties--lateral-tcp-auxiliary-cache-configuration"></a>

## Lateral TCP Auxiliary Cache Configuration

The following properties apply to the TCP Lateral Cache plugin.

<a id="lateraltcpproperties--tcp-configuration-properties"></a>

### TCP Configuration Properties

| Property | Description | Required | Default Value |
| --- | --- | --- | --- |
| TcpServers | This is the list of servers this cache should try to connect to. With UDP discovery this is not necessary. | N | none |
| TcpListenerHost | This is the host this cache should listen on (for multi-homed hosts). | N | listen on all interfaces |
| TcpListenerPort | This is the port this cache should listen on. | Y | n/a |
| AllowGet | Should this cache be allowed to get from other laterals. False means that it can only put, i.e. send updates and remove requests to other laterals. Lateral gets are not recommended for performance reasons. This used to be controlled by the attribute PutOnlyMode. | N | true |
| Receive | Should this cache receive or only send to other laterals. You may want to set receive to false if you just need to broadcast to other caches. If you have a feed data parser, that doesn't need to receive updates, but you do want it to send invalidation messages, then you would set receive to false. If receive is false, the discovery service, if enabled, will only listen. | N | true |
| IssueRemoveOnPut | If this is set to true, then the lateral client will send a remove command rather than a put command to any registered listeners. | N | false |
| FilterRemoveByHashCode | If this is true, and IssueRemoveOnPut is true, the client will include the hashCode of the element to remove. If it is also true on the receiving end, the receiver will check to see if the element exists. If the element exists, and the hashCodes are the same, the item will not be removed. | N | false |
| SocketTimeOut | This allows you to set the socket (read) timeout. | N | 1000 |
| OpenTimeOut | This allows you to set the socket open timeout. | N | 2000 |
| UdpDiscoveryAddr | The address the UDP discovery process should broadcast messages to. | N | 228.5.6.7 |
| UdpDiscoveryPort | The port the UDP discovery process should send messages to. | N | 6789 |
| UdpTTL | The time-to-live for the UDP multicast packets (number of hops allowed). | N | 0 (use Java default) |
| UdpDiscoveryEnabled | Whether or not the UDP discovery service should be used to locate other lateral caches. | N | true |
| ZombieQueueMaxSize | The number of elements the zombie queue will hold. This queue is used to store events if we lose our connection with the server. | N | 1000 |

<a id="lateraltcpproperties--example-configuration"></a>

### Example Configuration

```

jcs.auxiliary.LTCP=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.LateralTCPCacheFactory
jcs.auxiliary.LTCP.attributes=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.TCPLateralCacheAttributes
#jcs.auxiliary.LTCP.attributes.TcpServers=
jcs.auxiliary.LTCP.attributes.TcpListenerPort=1118
jcs.auxiliary.LTCP.attributes.UdpDiscoveryAddr=228.5.6.8
jcs.auxiliary.LTCP.attributes.UdpDiscoveryPort=6780
jcs.auxiliary.LTCP.attributes.UdpDiscoveryEnabled=true
jcs.auxiliary.LTCP.attributes.Receive=true
jcs.auxiliary.LTCP.attributes.AllowGet=false
jcs.auxiliary.LTCP.attributes.IssueRemoveOnPut=false
jcs.auxiliary.LTCP.attributes.FilterRemoveByHashCode=false
jcs.auxiliary.LTCP.attributes.SocketTimeOut=1001
jcs.auxiliary.LTCP.attributes.OpenTimeOut=2002
jcs.auxiliary.LTCP.attributes.ZombieQueueMaxSize=2000
        
```

---

<a id="lateraludpdiscovery"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/LateralUDPDiscovery.html -->

<!-- page_index: 30 -->

<a id="lateraludpdiscovery--lateral-udp-discovery"></a>

## Lateral UDP Discovery

Rather than list all the other lateral servers in the configuration
file, you can configure the TCP lateral to use UDP
discovery. In discovery mode, lateral TCP caches will broadcast
to a multicast address and port, letting all listeners know where they are.

On startup each lateral will issue a special message requesting a
broadcast from the other caches. Normal broadcasts occur every
15 seconds. (This is to be made configurable.) Regions that don't
receive, are running in send only mode, don't broadcast anything but requests.

The normal broadcasts publish the address and port of the service.
This can be configured as `TcpListenerHost` and
`TcpListenerPort`, respectively. If the service address
is not set, the service tries to detect a suitable address using the
same interface as the one that is used for multicast. If the multicast
uses IPv6, a link-local IPv6 address is selected if one exists.
Otherwise, a site-local IPv4 address is chosen. If that attempt also
fails, the first address on any non-loopback interface is used.

When a lateral receives a discovery message it will try to add
the lateral to the nowait facade for the region. If it already exists
nothing happens. If a region is not configured to send laterally, nothing
happens, since it doesn't have a no wait.

This allows you to have the same configuration on every machine.

<a id="lateraludpdiscovery--configuration"></a>

### Configuration

The configuration is fairly straightforward and is done in the
auxiliary cache section of the `cache.ccf`
configuration file. In the example below, a TCP
Lateral Auxiliary Cache referenced by `LTCP` is created. It uses
UDP Discovery to locate other servers. It broadcasts to
multicast address `228.5.6.8` and port `6780`.
It listens to port `1110`. The UDP datagram time-to-live
is 4 hops.

```

jcs.auxiliary.LTCP=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.LateralTCPCacheFactory
jcs.auxiliary.LTCP.attributes=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.TCPLateralCacheAttributes
jcs.auxiliary.LTCP.attributes.TcpListenerPort=1110
jcs.auxiliary.LTCP.attributes.PutOnlyMode=true
jcs.auxiliary.LTCP.attributes.UdpDiscoveryAddr=228.5.6.8
jcs.auxiliary.LTCP.attributes.UdpDiscoveryPort=6780
jcs.auxiliary.LTCP.attributes.UdpDiscoveryEnabled=true
jcs.auxiliary.LTCP.attributes.UdpTTL=4
        
```

<a id="lateraludpdiscovery--multi-homed-hosts"></a>

### Multi-homed hosts

On machines that have several network interfaces, it might be
desirable to fix the interface that is used for multicast.
For this purpose, the network interface can be specified in the
configuration (see below).

If the network interface is not specified, JCS tries to detect a
suitable interface. The selected interface is logged on INFO level.
Search for the message "Using network interface" in your log file.

```

jcs.auxiliary.LTCP=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.LateralTCPCacheFactory
jcs.auxiliary.LTCP.attributes=org.apache.commons.jcs3.auxiliary.lateral.socket.tcp.TCPLateralCacheAttributes
jcs.auxiliary.LTCP.attributes.TcpListenerPort=1110
jcs.auxiliary.LTCP.attributes.PutOnlyMode=true
jcs.auxiliary.LTCP.attributes.UdpDiscoveryInterface=en0
jcs.auxiliary.LTCP.attributes.UdpDiscoveryAddr=228.5.6.8
jcs.auxiliary.LTCP.attributes.UdpDiscoveryPort=6780
jcs.auxiliary.LTCP.attributes.UdpDiscoveryEnabled=true
jcs.auxiliary.LTCP.attributes.UdpTTL=4
        
```

---

<a id="commons-jcs3-core"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-core/index.html -->

<!-- page_index: 31 -->

<a id="commons-jcs3-core--about-apache-commons-jcs-::-core"></a>

## About Apache Commons JCS :: Core

Apache Commons JCS is a distributed, versatile caching system.

---

<a id="commons-jcs3-jcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache/index.html -->

<!-- page_index: 32 -->

<a id="commons-jcs3-jcache--about-apache-commons-jcs-::-jcache"></a>

## About Apache Commons JCS :: JCache

Apache Commons JCS is a distributed, versatile caching system.

---

<a id="commons-jcs3-jcache-tck"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-tck/index.html -->

<!-- page_index: 33 -->

<a id="commons-jcs3-jcache-tck--about-apache-commons-jcs-::-jcache-tck"></a>

## About Apache Commons JCS :: JCache TCK

Apache Commons JCS is a distributed, versatile caching system.

---

<a id="commons-jcs3-jcache-extras"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-extras/index.html -->

<!-- page_index: 34 -->

<a id="commons-jcs3-jcache-extras--about-apache-commons-jcs-::-jcache-extras"></a>

## About Apache Commons JCS :: JCache Extras

Apache Commons JCS is a distributed, versatile caching system.

---

<a id="commons-jcs3-jcache-openjpa"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-openjpa/index.html -->

<!-- page_index: 35 -->

<a id="commons-jcs3-jcache-openjpa--about-apache-commons-jcs-::-jcache-openjpa"></a>

## About Apache Commons JCS :: JCache OpenJPA

Apache Commons JCS is a distributed, versatile caching system.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/project-info.html -->

<!-- page_index: 36 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons JCS is a distributed, versatile caching system. |
| [Summary](#summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-jcs/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-jcs/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependency Information](https://commons.apache.org/proper/commons-jcs/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-jcs/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-jcs/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-jcs/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/summary.html -->

<!-- page_index: 37 -->

<a id="summary--project-summary"></a>

## Project Summary

<a id="summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JCS |
| Description | Apache Commons JCS is a distributed, versatile caching system. |
| Homepage | [http://commons.apache.org/proper/commons-jcs/](#index) |

<a id="summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-jcs3 |
| Version | 3.2.1 |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/modules.html -->

<!-- page_index: 38 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons JCS :: Core](#commons-jcs3-core) | Apache Commons JCS is a distributed, versatile caching system. |
| [Apache Commons JCS :: JCache](#commons-jcs3-jcache) | Apache Commons JCS is a distributed, versatile caching system. |
| [Apache Commons JCS :: JCache TCK](#commons-jcs3-jcache-tck) | Apache Commons JCS is a distributed, versatile caching system. |
| [Apache Commons JCS :: JCache Extras](#commons-jcs3-jcache-extras) | Apache Commons JCS is a distributed, versatile caching system. |
| [Apache Commons JCS :: JCache OpenJPA](#commons-jcs3-jcache-openjpa) | Apache Commons JCS is a distributed, versatile caching system. |
| [Apache Commons JCS :: Distribution](https://commons.apache.org/proper/commons-jcs/commons-jcs3-dist/index.html) | Creates the Apache Commons JCS multimodule distribution. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/team.html -->

<!-- page_index: 39 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Organization |
| --- | --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/c29e6cd984090ee94208c9f8d4d29b3c?d=mm&s=60) | asmuts | Aaron Smuts | [asmuts@apache.org](mailto:asmuts@apache.org) | - |
| ![](http://www.gravatar.com/avatar/89b9b232a5da0064e413b4fc026ee073?d=mm&s=60) | jtaylor | James Taylor | [james@jamestaylor.org](mailto:james@jamestaylor.org) | - |
| ![](http://www.gravatar.com/avatar/af30a55941f915aa1cae51c8524ce8b6?d=mm&s=60) | hchar | Hanson Char | [hchar@apache.org](mailto:hchar@apache.org) | - |
| ![](http://www.gravatar.com/avatar/0c84c954651d516b0bb1352cd2f1fb33?d=mm&s=60) | tsavo | Travis Savo | [tsavo@ifilm.com](mailto:tsavo@ifilm.com) | IFilm |
| ![](http://www.gravatar.com/avatar/6de10ef7d733d31c0e3e2d131b96d201?d=mm&s=60) | tv | Thomas Vandahl | [tv@apache.org](mailto:tv@apache.org) | - |
| ![](http://www.gravatar.com/avatar/3183d91957cfbe06163853d6da2a965e?d=mm&s=60) | rmannibucau | Romain Manni-Bucau | [rmannibucau@apache.org](mailto:rmannibucau@apache.org) | - |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](http://www.gravatar.com/avatar/ce472655bd6e818fe8b5fd0ae57e45af?d=mm&s=60) | Scott Eade | [seade@backstagetech.com.au](mailto:seade@backstagetech.com.au) |
| ![](http://www.gravatar.com/avatar/6ff497ac0ccd83efab57361b4004f8a7?d=mm&s=60) | Michael Stevens | [mstevens@etla.org](mailto:mstevens@etla.org) |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/ci-management.html -->

<!-- page_index: 40 -->

<a id="ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="jcsvsehcache"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/JCSvsEHCache.html -->

<!-- page_index: 41 -->

<a id="jcsvsehcache--jcs-vs-ehcache-memory-performance"></a>

## JCS vs EHCache Memory Performance

<a id="jcsvsehcache--initial-test-results"></a>

### Initial Test Results

I just built both EHCache (1.2-beta4) and JCS
(1.2.7.0) from head, configured both similarly and
ran 20 rounds of 50,000 puts and gets, that is
1,000,000 puts and gets in total. Using the default
LRU Memory Cache, the same algorithm that EHCache
uses by default,
**JCS proved to be nearly twice as fast as EHCache**
in multiple trials for both puts and gets. I have
the log levels for both set at info. I would like to
further verify my results, since they completely
contradict the information on the EHCache site.

From what I can tell so far, JCS is significantly
faster than EHCache when you are retrieving items
that exist in the cache and when you are putting
items into a cache that has not reached its size
limit.

Additional testing shows that when the size limit it
reached, JCS and EHCache perform similarly for puts
and gets. Although JCS gets are significantly faster
when the items are present, they are almost exactly
the same when the items are not in the cache. My
initial tests revealed a less than 1% difference, but subsequent runs showed JCS as 20% faster. More
tests are needed before the results are conclusive.

Since, neither cache will be a relevant bottleneck
in any application where a cache would be useful, the differences in performance may be beside the
point. Nevertheless, it is important to note that
the EHCache web site provides, what appears to be, false test data.

The peculiar result is that a few years back EHCache
took the JCS source code, removed most of its
features, and ended up with something that performs
worse.

<a id="jcsvsehcache--test-data"></a>

### Test Data

Here is the data from the first test:

JCS put time for 50000 = 651; millis per = 0.01302
JCS get time for 50000 = 160; millis per = 0.0032
EHCache put time for 50000 = 481; millis per =
0.00962 EHCache get time for 50000 = 110; millis per
= 0.0022

JCS put time for 50000 = 240; millis per = 0.0048
JCS get time for 50000 = 90; millis per = 0.0018
EHCache put time for 50000 = 491; millis per =
0.00982 EHCache get time for 50000 = 120; millis per
= 0.0024

JCS put time for 50000 = 241; millis per = 0.00482
JCS get time for 50000 = 80; millis per = 0.0016
EHCache put time for 50000 = 551; millis per =
0.01102 EHCache get time for 50000 = 110; millis per
= 0.0022

JCS put time for 50000 = 240; millis per = 0.0048
JCS get time for 50000 = 90; millis per = 0.0018
EHCache put time for 50000 = 481; millis per =
0.00962 EHCache get time for 50000 = 130; millis per
= 0.0026

JCS put time for 50000 = 230; millis per = 0.0046
JCS get time for 50000 = 181; millis per = 0.00362
EHCache put time for 50000 = 520; millis per =
0.0104 EHCache get time for 50000 = 101; millis per
= 0.00202

JCS put time for 50000 = 220; millis per = 0.0044
JCS get time for 50000 = 90; millis per = 0.0018
EHCache put time for 50000 = 641; millis per =
0.01282 EHCache get time for 50000 = 110; millis per
= 0.0022

JCS put time for 50000 = 250; millis per = 0.0050
JCS get time for 50000 = 121; millis per = 0.00242
EHCache put time for 50000 = 590; millis per =
0.0118 EHCache get time for 50000 = 101; millis per
= 0.00202

JCS put time for 50000 = 260; millis per = 0.0052
JCS get time for 50000 = 100; millis per = 0.0020
EHCache put time for 50000 = 581; millis per =
0.01162 EHCache get time for 50000 = 100; millis per
= 0.0020

JCS put time for 50000 = 290; millis per = 0.0058
JCS get time for 50000 = 121; millis per = 0.00242
EHCache put time for 50000 = 570; millis per =
0.0114 EHCache get time for 50000 = 121; millis per
= 0.00242

JCS put time for 50000 = 210; millis per = 0.0042
JCS get time for 50000 = 120; millis per = 0.0024
EHCache put time for 50000 = 561; millis per =
0.01122 EHCache get time for 50000 = 130; millis per
= 0.0026

JCS put time for 50000 = 250; millis per = 0.0050
JCS get time for 50000 = 151; millis per = 0.00302
EHCache put time for 50000 = 560; millis per =
0.0112 EHCache get time for 50000 = 111; millis per
= 0.00222

JCS put time for 50000 = 250; millis per = 0.0050
JCS get time for 50000 = 100; millis per = 0.0020
EHCache put time for 50000 = 711; millis per =
0.01422 EHCache get time for 50000 = 100; millis per
= 0.0020

JCS put time for 50000 = 251; millis per = 0.00502
JCS get time for 50000 = 90; millis per = 0.0018
EHCache put time for 50000 = 511; millis per =
0.01022 EHCache get time for 50000 = 90; millis per
= 0.0018

JCS put time for 50000 = 220; millis per = 0.0044
JCS get time for 50000 = 100; millis per = 0.0020
EHCache put time for 50000 = 491; millis per =
0.00982 EHCache get time for 50000 = 90; millis per
= 0.0018

JCS put time for 50000 = 230; millis per = 0.0046
JCS get time for 50000 = 80; millis per = 0.0016
EHCache put time for 50000 = 201; millis per =
0.00402 EHCache get time for 50000 = 390; millis per
= 0.0078

JCS put time for 50000 = 201; millis per = 0.00402
JCS get time for 50000 = 120; millis per = 0.0024
EHCache put time for 50000 = 180; millis per =
0.0036 EHCache get time for 50000 = 411; millis per
= 0.00822

JCS put time for 50000 = 210; millis per = 0.0042
JCS get time for 50000 = 100; millis per = 0.0020
EHCache put time for 50000 = 210; millis per =
0.0042 EHCache get time for 50000 = 381; millis per
= 0.00762

JCS put time for 50000 = 240; millis per = 0.0048
JCS get time for 50000 = 90; millis per = 0.0018
EHCache put time for 50000 = 211; millis per =
0.00422 EHCache get time for 50000 = 410; millis per
= 0.0082

JCS put time for 50000 = 221; millis per = 0.00442
JCS get time for 50000 = 80; millis per = 0.0016
EHCache put time for 50000 = 210; millis per =
0.0042 EHCache get time for 50000 = 411; millis per
= 0.00822

JCS put time for 50000 = 220; millis per = 0.0044
JCS get time for 50000 = 80; millis per = 0.0016
EHCache put time for 50000 = 190; millis per =
0.0038 EHCache get time for 50000 = 411; millis per
= 0.00822

Finished 20 loops of 50000 gets and puts

Put average for JCS = 256 Put average for EHCache =
447 JCS puts took 0.57270694 times the EHCache , the
goal is less than 1.0x

Get average for JCS = 107 Get average for EHCache =
196 JCS gets took 0.54591835 times the EHCache , the
goal is less than 1.0x

<a id="jcsvsehcache--a-test-class"></a>

### A Test Class

Here is the test class:

```
package org.apache.commons.jcs;
import junit.framework.TestCase; import net.sf.ehcache.Cache; import net.sf.ehcache.CacheManager; import net.sf.ehcache.Element;
import org.apache.commons.logging.Log; import org.apache.commons.logging.LogFactory; import org.apache.commons.jcs3.engine.CompositeCacheAttributes; import org.apache.commons.jcs3.engine.behavior.ICompositeCacheAttributes; import org.apache.commons.jcs3.utils.struct.LRUMap;
/** * Compare JCS vs ehcache performance.* * @author Aaron Smuts * */ public class JCSvsEHCachePerformanceTest extends TestCase {
float ratioPut = 0;
float ratioGet = 0;
// the jcs to competitor float target = 1.0f;
int loops = 20;
int tries = 50000;
/** * Compare performance between JCS and EHCache. Fail if JCS is not as fast.* Print the ratio.* * @throws Exception * */ public void testJCSvsEHCache() throws Exception {
Log log = LogFactory.getLog( LRUMap.class ); if ( log.isDebugEnabled() ) {System.out.println( "The log level must be at info or above for the a performance test." ); return;}
doWork();
assertTrue( this.ratioPut < target ); assertTrue( this.ratioGet < target );
}
/** * This runs a series of gets and puts for both JCS and EHCache. The test * will fail if JCS is not faster.* * @throws Exception * */ public void doWork() throws Exception {
int maxSize = 1000000;
// create the two caches.CacheManager ehMgr = CacheManager.getInstance(); // Create an ehcache with a max size of maxSize, no swap, with items // that can expire, with maximum idle time to live of 500 seconds, and // maximum idel time of 500 seconds.Cache eh = new Cache( "testJCSvsEHCache", maxSize, false, false, 500, 500 ); ehMgr.addCache( eh );
// Create a similarly configured JCS that uses the LRU memory cache.// maxSize elements that are not eternal. No disk cache is configured.ICompositeCacheAttributes cattr = new CompositeCacheAttributes(); cattr.setMaxObjects( maxSize ); CacheAccess<String, String> jcs = JCS.getInstance( "testJCSvsEHCache", cattr );
// run settings long start = 0; long end = 0; long time = 0; float tPer = 0;
long putTotalJCS = 0; long getTotalJCS = 0; long putTotalEHCache = 0; long getTotalEHCache = 0;
String jcsDisplayName = "JCS"; String ehCacheDisplayName = "";
try {for ( int j = 0; j < loops; j++ ) {
jcsDisplayName = "JCS      "; start = System.currentTimeMillis(); for ( int i = 0; i < tries; i++ ) {jcs.put( "key:" + i, "data" + i );} end = System.currentTimeMillis(); time = end - start; putTotalJCS += time; tPer = Float.intBitsToFloat( (int) time ) / Float.intBitsToFloat( tries ); System.out .println( jcsDisplayName + " put time for " + tries + " = " + time + "; millis per = " + tPer );
start = System.currentTimeMillis(); for ( int i = 0; i < tries; i++ ) {jcs.get( "key:" + i );} end = System.currentTimeMillis(); time = end - start; getTotalJCS += time; tPer = Float.intBitsToFloat( (int) time ) / Float.intBitsToFloat( tries ); System.out .println( jcsDisplayName + " get time for " + tries + " = " + time + "; millis per = " + tPer );
// ///////////////////////////////////////////////////////////// ehCacheDisplayName = "EHCache  ";
start = System.currentTimeMillis(); for ( int i = 0; i < tries; i++ ) {Element ehElm = new Element( "key:" + i, "data" + i );
eh.put( ehElm );} end = System.currentTimeMillis(); time = end - start; putTotalEHCache += time; tPer = Float.intBitsToFloat( (int) time ) / Float.intBitsToFloat( tries ); System.out.println( ehCacheDisplayName + " put time for " + tries + " = " + time + "; millis per = " + tPer );
start = System.currentTimeMillis(); for ( int i = 0; i < tries; i++ ) {eh.get( "key:" + i );} end = System.currentTimeMillis(); time = end - start; getTotalEHCache += time; tPer = Float.intBitsToFloat( (int) time ) / Float.intBitsToFloat( tries ); System.out.println( ehCacheDisplayName + " get time for " + tries + " = " + time + "; millis per = " + tPer );
System.out.println( "\n" );}
} catch ( Exception e ) {e.printStackTrace( System.out ); System.out.println( e );}
long putAvJCS = putTotalJCS / loops; long getAvJCS = getTotalJCS / loops; long putAvHashtable = putTotalEHCache / loops; long getAvHashtable = getTotalEHCache / loops;
System.out.println( "Finished " + loops + " loops of " + tries + " gets and puts" );
System.out.println( "\n" ); System.out.println( "Put average for " + jcsDisplayName + "  = " + putAvJCS ); System.out.println( "Put average for " + ehCacheDisplayName + " = " + putAvHashtable ); ratioPut = Float.intBitsToFloat( (int) putAvJCS ) / Float.intBitsToFloat( (int) putAvHashtable ); System.out.println( jcsDisplayName + " puts took " + ratioPut + " times the " + ehCacheDisplayName + ", the goal is <" + target + "x" );
System.out.println( "\n" ); System.out.println( "Get average for  " + jcsDisplayName + "  = " + getAvJCS ); System.out.println( "Get average for " + ehCacheDisplayName + " = " + getAvHashtable ); ratioGet = Float.intBitsToFloat( (int) getAvJCS ) / Float.intBitsToFloat( (int) getAvHashtable ); System.out.println( jcsDisplayName + " gets took " + ratioGet + " times the " + ehCacheDisplayName + ", the goal is <" + target + "x" );
}
}
```

---

<a id="commons-jcs3-core-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-core/ci-management.html -->

<!-- page_index: 42 -->

<a id="commons-jcs3-core-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-jcs3-core-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-jcs3-core-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-jcs3-core-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-core/scm.html -->

<!-- page_index: 43 -->

<a id="commons-jcs3-core-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-jcs3-core-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-jcs.git
```

<a id="commons-jcs3-core-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch commons-jcs3-3.2.1-rc3 http://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-core-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch commons-jcs3-3.2.1-rc3 https://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-core-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-jcs3-core-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-core/summary.html -->

<!-- page_index: 44 -->

<a id="commons-jcs3-core-summary--project-summary"></a>

## Project Summary

<a id="commons-jcs3-core-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JCS :: Core |
| Description | Apache Commons JCS is a distributed, versatile caching system. |
| Homepage | <http://commons.apache.org/proper/commons-jcs/commons-jcs3-core/> |

<a id="commons-jcs3-core-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-jcs3-core-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-jcs3-core |
| Version | 3.2.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-jcs3-core-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-core/team.html -->

<!-- page_index: 45 -->

<a id="commons-jcs3-core-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-jcs3-core-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Organization |
| --- | --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/c29e6cd984090ee94208c9f8d4d29b3c?d=mm&s=60) | asmuts | Aaron Smuts | [asmuts@apache.org](mailto:asmuts@apache.org) | - |
| ![](http://www.gravatar.com/avatar/89b9b232a5da0064e413b4fc026ee073?d=mm&s=60) | jtaylor | James Taylor | [james@jamestaylor.org](mailto:james@jamestaylor.org) | - |
| ![](http://www.gravatar.com/avatar/af30a55941f915aa1cae51c8524ce8b6?d=mm&s=60) | hchar | Hanson Char | [hchar@apache.org](mailto:hchar@apache.org) | - |
| ![](http://www.gravatar.com/avatar/0c84c954651d516b0bb1352cd2f1fb33?d=mm&s=60) | tsavo | Travis Savo | [tsavo@ifilm.com](mailto:tsavo@ifilm.com) | IFilm |
| ![](http://www.gravatar.com/avatar/6de10ef7d733d31c0e3e2d131b96d201?d=mm&s=60) | tv | Thomas Vandahl | [tv@apache.org](mailto:tv@apache.org) | - |
| ![](http://www.gravatar.com/avatar/3183d91957cfbe06163853d6da2a965e?d=mm&s=60) | rmannibucau | Romain Manni-Bucau | [rmannibucau@apache.org](mailto:rmannibucau@apache.org) | - |

<a id="commons-jcs3-core-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](http://www.gravatar.com/avatar/ce472655bd6e818fe8b5fd0ae57e45af?d=mm&s=60) | Scott Eade | [seade@backstagetech.com.au](mailto:seade@backstagetech.com.au) |
| ![](http://www.gravatar.com/avatar/6ff497ac0ccd83efab57361b4004f8a7?d=mm&s=60) | Michael Stevens | [mstevens@etla.org](mailto:mstevens@etla.org) |

---

<a id="commons-jcs3-jcache-extras-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-extras/ci-management.html -->

<!-- page_index: 46 -->

<a id="commons-jcs3-jcache-extras-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-jcs3-jcache-extras-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-jcs3-jcache-extras-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-jcs3-jcache-extras-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-extras/scm.html -->

<!-- page_index: 47 -->

<a id="commons-jcs3-jcache-extras-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-jcs3-jcache-extras-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-jcs.git
```

<a id="commons-jcs3-jcache-extras-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch commons-jcs3-3.2.1-rc3 http://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-extras-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch commons-jcs3-3.2.1-rc3 https://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-extras-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-jcs3-jcache-extras-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-extras/summary.html -->

<!-- page_index: 48 -->

<a id="commons-jcs3-jcache-extras-summary--project-summary"></a>

## Project Summary

<a id="commons-jcs3-jcache-extras-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JCS :: JCache Extras |
| Description | Apache Commons JCS is a distributed, versatile caching system. |
| Homepage | <http://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-extras/> |

<a id="commons-jcs3-jcache-extras-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-jcs3-jcache-extras-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-jcs3-jcache-extras |
| Version | 3.2.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-jcs3-jcache-extras-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-extras/team.html -->

<!-- page_index: 49 -->

<a id="commons-jcs3-jcache-extras-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-jcs3-jcache-extras-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Organization |
| --- | --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/c29e6cd984090ee94208c9f8d4d29b3c?d=mm&s=60) | asmuts | Aaron Smuts | [asmuts@apache.org](mailto:asmuts@apache.org) | - |
| ![](http://www.gravatar.com/avatar/89b9b232a5da0064e413b4fc026ee073?d=mm&s=60) | jtaylor | James Taylor | [james@jamestaylor.org](mailto:james@jamestaylor.org) | - |
| ![](http://www.gravatar.com/avatar/af30a55941f915aa1cae51c8524ce8b6?d=mm&s=60) | hchar | Hanson Char | [hchar@apache.org](mailto:hchar@apache.org) | - |
| ![](http://www.gravatar.com/avatar/0c84c954651d516b0bb1352cd2f1fb33?d=mm&s=60) | tsavo | Travis Savo | [tsavo@ifilm.com](mailto:tsavo@ifilm.com) | IFilm |
| ![](http://www.gravatar.com/avatar/6de10ef7d733d31c0e3e2d131b96d201?d=mm&s=60) | tv | Thomas Vandahl | [tv@apache.org](mailto:tv@apache.org) | - |
| ![](http://www.gravatar.com/avatar/3183d91957cfbe06163853d6da2a965e?d=mm&s=60) | rmannibucau | Romain Manni-Bucau | [rmannibucau@apache.org](mailto:rmannibucau@apache.org) | - |

<a id="commons-jcs3-jcache-extras-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](http://www.gravatar.com/avatar/ce472655bd6e818fe8b5fd0ae57e45af?d=mm&s=60) | Scott Eade | [seade@backstagetech.com.au](mailto:seade@backstagetech.com.au) |
| ![](http://www.gravatar.com/avatar/6ff497ac0ccd83efab57361b4004f8a7?d=mm&s=60) | Michael Stevens | [mstevens@etla.org](mailto:mstevens@etla.org) |

---

<a id="commons-jcs3-jcache-openjpa-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-openjpa/ci-management.html -->

<!-- page_index: 50 -->

<a id="commons-jcs3-jcache-openjpa-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-jcs3-jcache-openjpa-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-jcs3-jcache-openjpa-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-jcs3-jcache-openjpa-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-openjpa/scm.html -->

<!-- page_index: 51 -->

<a id="commons-jcs3-jcache-openjpa-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-jcs3-jcache-openjpa-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-jcs.git
```

<a id="commons-jcs3-jcache-openjpa-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch commons-jcs3-3.2.1-rc3 http://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-openjpa-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch commons-jcs3-3.2.1-rc3 https://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-openjpa-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-jcs3-jcache-openjpa-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-openjpa/summary.html -->

<!-- page_index: 52 -->

<a id="commons-jcs3-jcache-openjpa-summary--project-summary"></a>

## Project Summary

<a id="commons-jcs3-jcache-openjpa-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JCS :: JCache OpenJPA |
| Description | Apache Commons JCS is a distributed, versatile caching system. |
| Homepage | <http://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-openjpa/> |

<a id="commons-jcs3-jcache-openjpa-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-jcs3-jcache-openjpa-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-jcs3-jcache-openjpa |
| Version | 3.2.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-jcs3-jcache-openjpa-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-openjpa/team.html -->

<!-- page_index: 53 -->

<a id="commons-jcs3-jcache-openjpa-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-jcs3-jcache-openjpa-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Organization |
| --- | --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/c29e6cd984090ee94208c9f8d4d29b3c?d=mm&s=60) | asmuts | Aaron Smuts | [asmuts@apache.org](mailto:asmuts@apache.org) | - |
| ![](http://www.gravatar.com/avatar/89b9b232a5da0064e413b4fc026ee073?d=mm&s=60) | jtaylor | James Taylor | [james@jamestaylor.org](mailto:james@jamestaylor.org) | - |
| ![](http://www.gravatar.com/avatar/af30a55941f915aa1cae51c8524ce8b6?d=mm&s=60) | hchar | Hanson Char | [hchar@apache.org](mailto:hchar@apache.org) | - |
| ![](http://www.gravatar.com/avatar/0c84c954651d516b0bb1352cd2f1fb33?d=mm&s=60) | tsavo | Travis Savo | [tsavo@ifilm.com](mailto:tsavo@ifilm.com) | IFilm |
| ![](http://www.gravatar.com/avatar/6de10ef7d733d31c0e3e2d131b96d201?d=mm&s=60) | tv | Thomas Vandahl | [tv@apache.org](mailto:tv@apache.org) | - |
| ![](http://www.gravatar.com/avatar/3183d91957cfbe06163853d6da2a965e?d=mm&s=60) | rmannibucau | Romain Manni-Bucau | [rmannibucau@apache.org](mailto:rmannibucau@apache.org) | - |

<a id="commons-jcs3-jcache-openjpa-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](http://www.gravatar.com/avatar/ce472655bd6e818fe8b5fd0ae57e45af?d=mm&s=60) | Scott Eade | [seade@backstagetech.com.au](mailto:seade@backstagetech.com.au) |
| ![](http://www.gravatar.com/avatar/6ff497ac0ccd83efab57361b4004f8a7?d=mm&s=60) | Michael Stevens | [mstevens@etla.org](mailto:mstevens@etla.org) |

---

<a id="commons-jcs3-jcache-tck-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-tck/ci-management.html -->

<!-- page_index: 54 -->

<a id="commons-jcs3-jcache-tck-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-jcs3-jcache-tck-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-jcs3-jcache-tck-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-jcs3-jcache-tck-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-tck/scm.html -->

<!-- page_index: 55 -->

<a id="commons-jcs3-jcache-tck-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-jcs3-jcache-tck-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-jcs.git
```

<a id="commons-jcs3-jcache-tck-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch commons-jcs3-3.2.1-rc3 http://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-tck-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch commons-jcs3-3.2.1-rc3 https://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-tck-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-jcs3-jcache-tck-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-tck/summary.html -->

<!-- page_index: 56 -->

<a id="commons-jcs3-jcache-tck-summary--project-summary"></a>

## Project Summary

<a id="commons-jcs3-jcache-tck-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JCS :: JCache TCK |
| Description | Apache Commons JCS is a distributed, versatile caching system. |
| Homepage | <http://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-tck/> |

<a id="commons-jcs3-jcache-tck-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-jcs3-jcache-tck-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-jcs3-jcache-tck |
| Version | 3.2.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-jcs3-jcache-tck-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache-tck/team.html -->

<!-- page_index: 57 -->

<a id="commons-jcs3-jcache-tck-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-jcs3-jcache-tck-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Organization |
| --- | --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/c29e6cd984090ee94208c9f8d4d29b3c?d=mm&s=60) | asmuts | Aaron Smuts | [asmuts@apache.org](mailto:asmuts@apache.org) | - |
| ![](http://www.gravatar.com/avatar/89b9b232a5da0064e413b4fc026ee073?d=mm&s=60) | jtaylor | James Taylor | [james@jamestaylor.org](mailto:james@jamestaylor.org) | - |
| ![](http://www.gravatar.com/avatar/af30a55941f915aa1cae51c8524ce8b6?d=mm&s=60) | hchar | Hanson Char | [hchar@apache.org](mailto:hchar@apache.org) | - |
| ![](http://www.gravatar.com/avatar/0c84c954651d516b0bb1352cd2f1fb33?d=mm&s=60) | tsavo | Travis Savo | [tsavo@ifilm.com](mailto:tsavo@ifilm.com) | IFilm |
| ![](http://www.gravatar.com/avatar/6de10ef7d733d31c0e3e2d131b96d201?d=mm&s=60) | tv | Thomas Vandahl | [tv@apache.org](mailto:tv@apache.org) | - |
| ![](http://www.gravatar.com/avatar/3183d91957cfbe06163853d6da2a965e?d=mm&s=60) | rmannibucau | Romain Manni-Bucau | [rmannibucau@apache.org](mailto:rmannibucau@apache.org) | - |

<a id="commons-jcs3-jcache-tck-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](http://www.gravatar.com/avatar/ce472655bd6e818fe8b5fd0ae57e45af?d=mm&s=60) | Scott Eade | [seade@backstagetech.com.au](mailto:seade@backstagetech.com.au) |
| ![](http://www.gravatar.com/avatar/6ff497ac0ccd83efab57361b4004f8a7?d=mm&s=60) | Michael Stevens | [mstevens@etla.org](mailto:mstevens@etla.org) |

---

<a id="commons-jcs3-jcache-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache/ci-management.html -->

<!-- page_index: 58 -->

<a id="commons-jcs3-jcache-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-jcs3-jcache-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-jcs3-jcache-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-jcs3-jcache-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache/scm.html -->

<!-- page_index: 59 -->

<a id="commons-jcs3-jcache-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-jcs3-jcache-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-jcs.git
```

<a id="commons-jcs3-jcache-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch commons-jcs3-3.2.1-rc3 http://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch commons-jcs3-3.2.1-rc3 https://gitbox.apache.org/repos/asf/commons-jcs.git
```

<a id="commons-jcs3-jcache-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-jcs3-jcache-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache/summary.html -->

<!-- page_index: 60 -->

<a id="commons-jcs3-jcache-summary--project-summary"></a>

## Project Summary

<a id="commons-jcs3-jcache-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons JCS :: JCache |
| Description | Apache Commons JCS is a distributed, versatile caching system. |
| Homepage | <http://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache/> |

<a id="commons-jcs3-jcache-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-jcs3-jcache-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-jcs3-jcache |
| Version | 3.2.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-jcs3-jcache-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-jcs/commons-jcs3-jcache/team.html -->

<!-- page_index: 61 -->

<a id="commons-jcs3-jcache-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-jcs3-jcache-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Organization |
| --- | --- | --- | --- | --- |
| ![](http://www.gravatar.com/avatar/c29e6cd984090ee94208c9f8d4d29b3c?d=mm&s=60) | asmuts | Aaron Smuts | [asmuts@apache.org](mailto:asmuts@apache.org) | - |
| ![](http://www.gravatar.com/avatar/89b9b232a5da0064e413b4fc026ee073?d=mm&s=60) | jtaylor | James Taylor | [james@jamestaylor.org](mailto:james@jamestaylor.org) | - |
| ![](http://www.gravatar.com/avatar/af30a55941f915aa1cae51c8524ce8b6?d=mm&s=60) | hchar | Hanson Char | [hchar@apache.org](mailto:hchar@apache.org) | - |
| ![](http://www.gravatar.com/avatar/0c84c954651d516b0bb1352cd2f1fb33?d=mm&s=60) | tsavo | Travis Savo | [tsavo@ifilm.com](mailto:tsavo@ifilm.com) | IFilm |
| ![](http://www.gravatar.com/avatar/6de10ef7d733d31c0e3e2d131b96d201?d=mm&s=60) | tv | Thomas Vandahl | [tv@apache.org](mailto:tv@apache.org) | - |
| ![](http://www.gravatar.com/avatar/3183d91957cfbe06163853d6da2a965e?d=mm&s=60) | rmannibucau | Romain Manni-Bucau | [rmannibucau@apache.org](mailto:rmannibucau@apache.org) | - |

<a id="commons-jcs3-jcache-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](http://www.gravatar.com/avatar/ce472655bd6e818fe8b5fd0ae57e45af?d=mm&s=60) | Scott Eade | [seade@backstagetech.com.au](mailto:seade@backstagetech.com.au) |
| ![](http://www.gravatar.com/avatar/6ff497ac0ccd83efab57361b4004f8a7?d=mm&s=60) | Michael Stevens | [mstevens@etla.org](mailto:mstevens@etla.org) |

---
