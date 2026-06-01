# Project Information

## Navigation

- Commons Pool
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Examples](#examples)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-pool"></a>

# Apache Commons Pool

The Apache Commons Pool open source software library provides
an object-pooling API and a number of object pool implementations.
Version 2 of Apache Commons Pool contains a completely re-written
pooling implementation compared to the 1.x series. In addition to
performance and scalability improvements, version 2 includes robust
instance tracking and pool monitoring.

- Version 2.7.x and up requires Java 8 or above.
- Version 2.6.x requires Java 7 or above.
- Version 2.5.x requires Java 7 or above.
- Version 2.0 requires 6 or above.

<a id="index--releases"></a>

# Releases

See the [downloads](https://commons.apache.org/download_pool.cgi) page for information
on obtaining releases.

<a id="index--features"></a>

# Features

The
[org.apache.commons.pool2](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/package-summary.html)
package defines a handful of pooling interfaces and some base classes
that may be useful when creating new pool implementations.

<a id="index--pooledobjectfactory"></a>

## PooledObjectFactory

[`PooledObjectFactory`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/PooledObjectFactory.html)
provides a generic interface for managing the lifecycle of a pooled object:

```

public interface PooledObjectFactory<T> {
    activateObject(PooledObject<T>)
    destroyObject(PooledObject<T>)
    destroyObject(PooledObject<T>, DestroyMode)
    makeObject()
    passivateObject(PooledObject<T>)
    validateObject(PooledObject<T>)
}
```

Users of 1.x versions of Commons Pool will notice that while the `PoolableObjectFactory`s used by
1.x pools create and manage pooled objects directly, version 2 `PooledObjectFactory`s create and
manage
[`PooledObject`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/PooledObject)s. These object wrappers
maintain object pooling state, enabling `PooledObjectFactory` methods to have access to data such
as instance creation time or time of last use. A
[`DefaultPooledObject`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/DefaultPooledObject) is
provided, with natural implementations for pooling state methods. The simplest way to implement a
`PoolableObjectFactory` is to have it extend
[`BasePooledObjectFactory`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/BasePooledObjectFactory.html).
This factory provides a `makeObject()` that returns `wrap(create())`
where `create` and `wrap` are abstract. You provide an implementation of `create`
to create the underlying objects that you want to manage in the pool and `wrap` to wrap created
instances in `PooledObject`s. To use `DefaultPooledObject` wrappers, use

```

@Override
 public PooledObject<Foo> wrap(Foo foo) {
    return new DefaultPooledObject<Foo>(foo);
 }
 
```

where `Foo` is the type of the objects being pooled (the return type of `create()`).

[`KeyedPooledObjectFactory`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/KeyedPooledObjectFactory.html)
defines a similar interface for `KeyedObjectPool`s:

```

public interface KeyedPooledObjectFactory<K,V> {
    PooledObject<V> makeObject(K key);
    void activateObject(K key, PooledObject<V> obj);
    void passivateObject(K key, PooledObject<V> obj);
    boolean validateObject(K key, PooledObject<V> obj);
    void destroyObject(K key, PooledObject<V> obj);
}
```

[`BaseKeyedPooledObjectFactory`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/BaseKeyedPooledObjectFactory.html)
provides an abstract base implementation of `KeyedPooledObjectFactory`.

The
[org.apache.commons.pool2.impl](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/package-summary.html)
package provides some *Pool* implementations.

<a id="index--genericobjectpool"></a>

## GenericObjectPool

[`GenericObjectPool`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/GenericObjectPool.html)
provides a wide variety of configuration options, including the ability to cap the number of idle or
active instances, to evict instances as they sit idle in the pool, etc. As of version 2, `GenericObjectPool`
also provides abandoned instance tracking and removal.

[`GenericKeyedObjectPool`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/GenericKeyedObjectPool.html)
offers the same behavior for keyed pools.

<a id="index--softreferenceobjectpool"></a>

## SoftReferenceObjectPool

[`SoftReferenceObjectPool`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/SoftReferenceObjectPool.html)
can grow as needed, but allows the garbage collector to evict idle instances from the pool as needed.

<a id="index--migrating-from-pool-2.x-to-pool-2.y"></a>

# Migrating from Pool 2.x to Pool 2.y

Client code that uses a Pool 2.x release should require no code
changes to work with a later Pool 2.x release.

New Pool 2.x releases may include support for new configuration
attributes. These will be listed in the change log. Note that the
MBean interfaces (those with names ending in MXBean or MBean) such as
[`DefaultPooledObjectInfoMBean`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/DefaultPooledObjectInfoMBean.html), [`GenericKeyedObjectPoolMXBean`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/GenericKeyedObjectPoolMXBean.html) or
[`GenericKeyedObjectPoolMXBean`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/impl/GenericKeyedObjectPoolMXBean.html)
may change from one release to the next to support these new
attributes. These interfaces should, therefore, not be implemented by
client as the changes will not be backwards compatible.

<a id="index--migrating-from-pool-1.x-to-pool-2.x"></a>

# Migrating from Pool 1.x to Pool 2.x

The migration from Apache Commons Pool 1.x to 2.x will require some
code changes. The most significant changes are the changes in package
name from `org.apache.commons.pool` to
`org.apache.commons.pool2` and the change in the implementation
classes to use `PooledObjectFactory`s, as described above.

The key implementation classes (`GenericObjectPool` and
`GenericKeyedObjectPool`) have retained their names so no
changes should be required there although a number of attributes have
been renamed to improve consistency and ensure attributes with the
same name in different pools have the same meaning. It is likely that
some changes will be required to use the new attribute names.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-pool.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-pool.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-pool.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/security.html -->

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
[user mailing list](https://commons.apache.org/proper/commons-pool/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

None.

---

<a id="examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/examples.html -->

<!-- page_index: 4 -->

<a id="examples--a-simple-pool-client"></a>

# A Simple Pool Client

Suppose you're writing a set of `java.io.Reader` utilities, and would like to
provide a method for dumping the contents of a `Reader` to a `String`.
Here's the code for the `ReaderUtil`, implemented without an `ObjectPool`:

```
import java.io.Reader; import java.io.IOException;
public class ReaderUtil {public ReaderUtil() {}
/** * Dumps the contents of the {@link Reader} to a * String, closing the {@link Reader} when done.*/ public String readToString(Reader in) throws IOException {StringBuffer buf = new StringBuffer(); try {for (int c = in.read(); c != -1; c = in.read()) {buf.append((char)c);} return buf.toString(); } catch (IOException e) {throw e; } finally {try {in.close(); } catch (Exception e) {// ignored}}}}
```

For the sake of this example, let's assume we want to pool the `StringBuffer`s
used to buffer the `Reader`'s contents. (A pool of `StringBuffer`s
may or may not be useful in practice. We're just using it as a simple example here.)

Let's further assume that a complete pool implementation will be provided via
a constructor. (We'll show you how to create such an implementation in just a moment.)
Then to use the pool we simply call `borrowObject` to obtain the buffer, and
then call `returnObject` when we're done with it.
Then a `ReaderUtil` implementation using a pool of `StringBuffer`s might look
like this:

```
import java.io.IOException; import java.io.Reader; import org.apache.commons.pool2.ObjectPool;
public class ReaderUtil {
private ObjectPool<StringBuffer> pool;
public ReaderUtil(ObjectPool<StringBuffer> pool) {this.pool = pool;}
/** * Dumps the contents of the {@link Reader} to a String, closing the {@link Reader} when done.*/ public String readToString(Reader in) throws IOException {StringBuffer buf = null; try {buf = pool.borrowObject(); for (int c = in.read(); c != -1; c = in.read()) {buf.append((char) c);} return buf.toString(); } catch (IOException e) {throw e; } catch (Exception e) {throw new RuntimeException("Unable to borrow buffer from pool" + e.toString()); } finally {try {in.close(); } catch (Exception e) {// ignored} try {if (null != buf) {pool.returnObject(buf);} } catch (Exception e) {// ignored}}}}
```

Since we've constrained ourselves to the `ObjectPool` interface, an arbitrary pool
implementation (returning, in our case, `StringBuffer`s) can be used. When a different
or "better" pool implementation comes along, we can simply drop it into our `ReaderUtil`
without changing a line of code.

<a id="examples--a-pooledobjectfactory"></a>

# A PooledObjectFactory

The implementations provided in pool2 wrap pooled objects in `PooledObject`
wrappers for internal use by the pool and object factories. The `PooledObjectFactory`
interface defines lifecycle methods for pooled objects. The simplest way to implement a
`PoolableObjectFactory` is to extend
[`BasePooledObjectFactory`](https://commons.apache.org/proper/commons-pool/apidocs/org/apache/commons/pool2/BasePooledObjectFactory.html).

Here's a `PooledObjectFactory` implementation that creates
`StringBuffer`s as used above.

```
import org.apache.commons.pool2.BasePooledObjectFactory; import org.apache.commons.pool2.PooledObject; import org.apache.commons.pool2.impl.DefaultPooledObject;
public class StringBufferFactory extends BasePooledObjectFactory<StringBuffer> {
@Override public StringBuffer create() {return new StringBuffer();}
/** * Use the default PooledObject implementation.*/ @Override public PooledObject<StringBuffer> wrap(StringBuffer buffer) {return new DefaultPooledObject<StringBuffer>(buffer);}
/** * When an object is returned to the pool, clear the buffer.*/ @Override public void passivateObject(PooledObject<StringBuffer> pooledObject) {pooledObject.getObject().setLength(0);}
// for all other methods, the no-op implementation // in BasePooledObjectFactory will suffice}
```

We can, for example, use this factory with the `GenericObjectPool` to instantiate our
`ReaderUtil` as follows:

```
ReaderUtil readerUtil = new ReaderUtil(new GenericObjectPool<StringBuffer>(new StringBufferFactory()));
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/project-info.html -->

<!-- page_index: 5 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons Object Pooling Library. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-pool/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-pool/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-pool/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-pool/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-pool/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-pool/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-pool/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/summary.html -->

<!-- page_index: 6 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Pool |
| Description | The Apache Commons Object Pooling Library. |
| Homepage | [https://commons.apache.org/proper/commons-pool/](#index) |

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
| GroupId | org.apache.commons |
| ArtifactId | commons-pool2 |
| Version | 2.13.1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/team.html -->

<!-- page_index: 7 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | morgand | Morgan Delagrange | [-](mailto:) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | geirm | Geir Magnusson | [-](mailto:) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | craigmcc | Craig McClanahan | [-](mailto:) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | rwaldhoff | Rodney Waldhoff | [-](mailto:) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | dweinr1 | David Weinrich | [-](mailto:) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | dirkv | Dirk Verbeeck | [-](mailto:) | - | - | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | rdonkin | Robert Burrell Donkin | [-](mailto:) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | sandymac | Sandy McArthur | [-](mailto:) | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | simonetripodi | Simone Tripodi | - | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | mattsicker | Matt Sicker | - | - | The Apache Software Foundation | - | - | - |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | psteitz | Phil Steitz | - | - | The Apache Software Foundation | - | - | - |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | Todd Carmichael | [toddc@concur.com](mailto:toddc@concur.com) |
| ![](assets/images/00000000000000000000000000000000_b77a9d2e9d900b37.jpg) | Arturo Bernal | - |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-pool/ci-management.html -->

<!-- page_index: 8 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-pool/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---
