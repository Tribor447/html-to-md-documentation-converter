# Project Information

## Navigation

- Commons VFS
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Build](#build)
  - [Using the API](#api)
  - [File Systems](#filesystems)
  - [Ant Tasks](#anttasks)
  - [Testing](#testing)
- Commons VFS Modules
  - [VFS Ant](#commons-vfs2-ant)
  - [VFS Core](#commons-vfs2)
  - [VFS Examples](#commons-vfs2-examples)
  - [VFS HDFS](#commons-vfs2-hdfs)
  - [VFS Jackrabbit 1.x](#commons-vfs2-jackrabbit1)
  - [VFS Jackrabbit 2.x](#commons-vfs2-jackrabbit2)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Project Modules](#modules)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Other pages
  - [Overview](#commons-vfs2-ant-ci-management)
  - [Overview](#commons-vfs2-ant-scm)
  - [Project Summary](#commons-vfs2-ant-summary)
  - [Project Team](#commons-vfs2-ant-team)
  - [Overview](#commons-vfs2-bom-ci-management)
  - [About Apache Commons VFS Bill of Materials](#commons-vfs2-bom)
  - [Overview](#commons-vfs2-bom-scm)
  - [Project Summary](#commons-vfs2-bom-summary)
  - [Project Team](#commons-vfs2-bom-team)
  - [Overview](#commons-vfs2-distribution-ci-management)
  - [About Apache Commons VFS Distribution](#commons-vfs2-distribution)
  - [Overview](#commons-vfs2-distribution-scm)
  - [Project Summary](#commons-vfs2-distribution-summary)
  - [Project Team](#commons-vfs2-distribution-team)
  - [Overview](#commons-vfs2-examples-ci-management)
  - [Overview](#commons-vfs2-examples-scm)
  - [Project Summary](#commons-vfs2-examples-summary)
  - [Project Team](#commons-vfs2-examples-team)
  - [Overview](#commons-vfs2-hdfs-ci-management)
  - [Overview](#commons-vfs2-hdfs-scm)
  - [Project Summary](#commons-vfs2-hdfs-summary)
  - [Project Team](#commons-vfs2-hdfs-team)
  - [Overview](#commons-vfs2-jackrabbit1-ci-management)
  - [Overview](#commons-vfs2-jackrabbit1-scm)
  - [Project Summary](#commons-vfs2-jackrabbit1-summary)
  - [Project Team](#commons-vfs2-jackrabbit1-team)
  - [Overview](#commons-vfs2-jackrabbit2-ci-management)
  - [Overview](#commons-vfs2-jackrabbit2-scm)
  - [Project Summary](#commons-vfs2-jackrabbit2-summary)
  - [Project Team](#commons-vfs2-jackrabbit2-team)
  - [Overview](#commons-vfs2-ci-management)
  - [Overview](#commons-vfs2-scm)
  - [Project Summary](#commons-vfs2-summary)
  - [Project Team](#commons-vfs2-team)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-virtual-file-system"></a>

# Commons Virtual File System

Commons VFS provides a single API for accessing
various different file systems. It presents a uniform view of
the files from various different sources, such as the files on
local disk, on an HTTP server, or inside a Zip archive.

Some of the features of Commons VFS are:

- A single consistent API for accessing files of different
  types.
- Support for numerous
  [file system types](#filesystems)
  .
- Caching of file information. Caches information in-JVM,
  and optionally can cache remote file information on the
  local file system (replicator).
- Event delivery.
- Support for logical file systems made up of files from
  various different file systems.
- Utilities for integrating Commons VFS into applications,
  such as a VFS-aware ClassLoader and URLStreamHandlerFactory.
- A set of VFS-enabled [Ant tasks](#anttasks).

<a id="index--requirements"></a>

# Requirements

Many of the file systems require that optional components be present in order for the protocol to be
enabled. See the [download and build](https://commons.apache.org/proper/commons-vfs/download.html) page for information on the optional
dependencies.

| Apache Commons VFS Version | Java Version |
| --- | --- |
| 2.10.0 | 8 |
| 2.9.0 | 8 |
| 2.8.0 | 8 |
| 2.7.0 | 8 |
| 2.6.0 | 8 |
| 2.5.0 | 8 |
| 2.4.x | 8 |
| 2.3 | 8 |
| 2.2 | 7 |
| 2.1 | 6 |
| 2.0 | 5 |
| 1.0 | 1.3 |

<a id="index--news"></a>

# News

Apache Commons VFS 2.10.0 is a new features and bug fix release. Version 2.10.0 adds the modules
[`commons-vfs2-ant`](#commons-vfs2-ant), [`commons-vfs2-bom`](#commons-vfs2-bom) and
[`commons-vfs2-hdfs`](#commons-vfs2-bom)
containing classes previously delivered in [`commons-vfs2`](#commons-vfs2)

Apache Commons VFS 2.5.0 is a new features and bug fix release. Version 2.5.0 adds the modules
[`commons-vfs2-jackrabbit1`](#commons-vfs2-jackrabbit1)
and
[`commons-vfs2-jackrabbit2`](#commons-vfs2-jackrabbit2).
The module [`commons-vfs2-jackrabbit1`](#commons-vfs2-jackrabbit1)
contains WebDAV classes previously delivered in [`commons-vfs2`](#commons-vfs2)

Apache Commons VFS 2.4.1 is a bug fix release.

Apache Commons VFS 2.4 is a new features and bug fix release.

Apache Commons VFS 2.3 is a new features and bug fix release.

Apache Commons VFS 2.2 is a new features and bug fix release.

Apache Commons VFS 2.1 is a bugfix release to VFS 2.0. If you meet the requirements you should be able
to replace 2.0 with 2.1 without the need for changes to API consumers. VFS 2.1 has introduced some now
methods for provider interfaces (like `FileObject`). If you implement a VFS provider and use the
corresponding `Abstract*` or `Default*` classes, there should be no need to modify
the code or recompile the provider. The TarFileProvider is one known exception to compatibility with 2.0.
See the [Release Notes](https://dist.apache.org/repos/dist/release/commons/vfs/RELEASE-NOTES.txt)
and the [Clirr Report](https://commons.apache.org/proper/commons-vfs/commons-vfs2/clirr-report.html) for details. VFS 2.1 adds a new read-only
provider for the Apache Hadoop (HDFS) File system.

Apache Commons VFS 2.0 adds support for FTPS and WebDav have been added in addition to many bugs
being fixed. Version 2.0 is not binary compatible with version 1.0. To ensure that both 1.0 and 2.0 can
coexist version 2.0 has had its Maven groupId changed to org.apache.commons, its Maven artifact changed
to commons-vfs2, and the package names are now org.apache.commons.vfs2. The API changes are fairly minor
and will mostly impact provider implementations.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/security.html -->

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
[user mailing list](https://commons.apache.org/proper/commons-vfs/mail-lists.html).

If you have encountered an unlisted security vulnerability or other unexpected behavior that has security impact, or if the descriptions here are
incomplete, please report them privately to the Apache Security Team. Thank you.

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

- [CVE-2025-27553](https://www.cve.org/CVERecord?id=CVE-2025-27553): Apache Commons VFS: Possible path traversal issue when using NameScope.DESCENDENT
- [CVE-2025-30474](https://www.cve.org/CVERecord?id=CVE-2025-30474): Apache Commons VFS: Failing to find an FTP file can reveal the URI's password in an error message

---

<a id="build"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/build.html -->

<!-- page_index: 4 -->

<a id="build--download"></a>

# Download

The latest release (binaries and source) of Commons VFS can be found
[here](https://commons.apache.org/proper/commons-vfs/download_vfs.cgi).

You will also need to download the [dependencies](https://commons.apache.org/proper/commons-vfs/commons-vfs2/dependencies.html) (jars) used by Apache Commons VFS.
You can download the jars from the list below; with Apache Maven dependency resolution is automatic.

| Dependency | Required For |
| --- | --- |
| [Apache Commons Logging](https://commons.apache.org/proper/commons-logging/) | All |
| [Apache Commons Lang](https://commons.apache.org/proper/commons-lang/) | All |
| [Apache Commons Collections](https://commons.apache.org/proper/commons-collections/) | LRU Cache (optional) |
| [Apache Commons Compress](https://commons.apache.org/proper/commons-compress/) | TAR, Bzip2 |
| [Apache Commons Net](https://commons.apache.org/proper/commons-net/) | FTP |
| [Apache Commons Httpclient](https://hc.apache.org/httpclient-legacy/) Requires [Commons Codec](https://commons.apache.org/proper/commons-codec/) | WebDAV, HTTP, URI Utils |
| [Apache Jackrabbit WebDAV Library](https://jackrabbit.apache.org/jcr/components/jackrabbit-webdav-library.html) Requires [Jackrabbit JCR Commons](https://jackrabbit.apache.org/jcr/components/jackrabbit-jcr-commons.html) and [SLF4J](https://www.slf4j.org) (Api and Impl). | WebDAV |
| [JSch](http://www.jcraft.com/jsch/) | SFTP |
| [Apache Hadoop Common](https://hadoop.apache.org/docs/stable/) [Apache Hadoop HDFS Common](https://hadoop.apache.org/docs/stable/) This requires a number of dependencies, use `$HADOOP_HOME/bin/hadoop classpath` command. | HDFS |
| [jCIFS](https://jcifs.samba.org/) | CIFS (VFS sandbox) |
| [javamail](https://javaee.github.io/javamail/) | mime (VFS sandbox) |

<a id="build--building-commons-vfs"></a>

# Building Commons VFS

To build Commons VFS, get the [sources](#scm) and use [Apache Maven](https://maven.apache.org/) 3.2.5 or later.
You need to use Java 8 or later. Production builds can be done with the
`-Pjava-1.8` profile from Commons Parent (which will compile and test with a JDK
from the JAVA\_1\_8\_HOME environment variable).

Use `mvn clean verify` to locally build and test the `core` and
`examples` modules. This will build the core JAR files in
`commons-vfs/core/target/commons-vfs2-<version>.jar`.

If you want to build the additional sandbox file systems as well, use
`mvn -Pinclude-sandbox clean verify`. This will also create the sandbox
components in `commons-vfs/sandbox/target/commons-vfs2-sandbox-<version>.jar`.

See the [commons-vfs2-example](https://commons.apache.org/proper/commons-vfs/commons-vfs2-example/index.html) Module on how
to use VFS Example Shell to verify the result.

---

<a id="api"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/api.html -->

<!-- page_index: 5 -->

<a id="api--using-the-api"></a>

# Using The API

The
[FileSystemManager](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/FileSystemManager.html)
interface provides access to Commons VFS. Using this interface
you can locate files and create file systems.
There are a
[number of ways](#api--configuring_commons_vfs)
to obtain a
`FileSystemManager` instance.
The simplest is to use the static
[VFS.getManager()](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/VFS.html#getManager.28.29)
method, which returns the default Commons VFS implementation.

Once you have a
`FileSystemManager`, you can use its
`resolveFile()` methods to locate a file by name.
For example:

```

FileSystemManager fsManager = VFS.getManager();
FileObject jarFile = fsManager.resolveFile("jar:lib/aJarFile.jar");
```

Each file is represented by a
[FileObject](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/FileObject.html)
instance. Using this interface you can create or delete the
file, list its children, read or write its content, and so on.
For example:

```

// Locate the Jar file
FileSystemManager fsManager = VFS.getManager();
FileObject jarFile = fsManager.resolveFile("jar:lib/aJarFile.jar");

// List the children of the Jar file
FileObject[] children = jarFile.getChildren();
System.out.println("Children of " + jarFile.getName().getURI());
for (int i = 0; i < children.length; i++) {
    System.out.println(children[i].getName().getBaseName());
}
```

In some cases you might want to explicitly free resources allocated by the filesystem.
You can do this by calling
[VFS.getManager().closeFileSystem(fs)](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/FileSystemManager.html#closeFileSystem).
If you use VFS as singleton (as described above) you should take care that this will close the filesystem for
all threads.
In other words, do not close any globally used filesystem like the one for local files.

See the
[FileObject](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/FileObject.html)
Javadocs for more detail.

<a id="api--cache"></a>

## Cache

Commons VFS uses a [SoftRefFilesCache](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/cache/SoftRefFilesCache.html) to release memory if a file is no longer used by the application.

This cache will return the same instance for a file as long as it is "strongly reachable" e.g. you
hold a reference to this object. If the FileObject is no longer reachable, and the jvm needs some memory, it will be released.

There is also an internal cache of each file object avoid the need to access the network layer. Now it's possible
to configure this behaviour through the use of [CacheStrategy](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/CacheStrategy.html).
Do this on the DefaultFileSystemManager. For example:
`((DefaultFileSystemManager) VFS.getManager()).setCacheStrategy(CacheStrategy.ON_CALL)`

<a id="api--user-authentication"></a>

## User Authentication

You can put the credentials into the url, but the drawback here is, that it is
easily possible to get access to the password.

To solve you can use the
[UserAuthenticator](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/UserAuthenticator.html)

For example:

```

StaticUserAuthenticator auth = new StaticUserAuthenticator("domain", "username", "password");
FileSystemOptions opts = new FileSystemOptions();
DefaultFileSystemConfigBuilder.getInstance().setUserAuthenticator(opts, auth);

FileObject fo = VFS.getManager().resolveFile("smb://host/anyshare/dir", opts);
```

Internally the UserAuthenticator uses char arrays which will be zeroed before it is
freed for garbage collection.Unhappily none of the current libraries use char
arrays and so VFS has to create a string. Thus, the main advantage
of this solution - security - is lost, but hey, that's not VFS fault ;-)

VFS calls `UserAuthenticator.requestAuthentication` each time it
requires credentials, it depends on the filesystem implementation how often
this might be. For example, with FTP this is on every connection, in SMB/JCIFS
this is for EVERY OBJECT. It is up to you how long you will cache credentials
of if you would like to provide a "save credentials" checkbox.

<a id="api--examples"></a>

## Examples

For an example of using the API, take a look at the classes
in the
[example](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/example/package-summary.html)
package.

<a id="api--configuring-commons-vfs"></a>

# Configuring Commons VFS

Commons VFS is represented using the
[FileSystemManager](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/FileSystemManager.html)
interface. There are a number of ways to create and configure a
`FileSystemManager` instance.

The simplest method is to use the static
[VFS.getManager()](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/VFS.html#getManager.28.29)
method, which returns the default Commons VFS implementation.

This method will also automatically scan the classpath for a /META-INF/vfs-providers.xml file
(also in jar files).
If such a file is found Commons VFS uses it in addition to the default providers.xml.
This allows you to start using a new filesystem by simply drop its implementation into the classpath.
The configuration file format is described below.
**Notice:** Currently it is not allowed to override an already configured filesystem. Commons VFS throws
an exception if there is already a filesystem for a scheme.

To configure Commons VFS programmatically, you can create an
instance of
[DefaultFileSystemManager](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/impl/DefaultFileSystemManager.html)
and configure it manually. The default constructor
`DefaultFileSystemManager` creates a manager that
is completely empty. You will have to add file providers to it
to make it do anything useful.

Here are the steps for using
`DefaultFileSystemManager`:

1. Create a new instance.
2. Set the logger for the manager and all its components,
   using
   `setLogger()`. This step is
   optional, and if skipped, the manager will use the default
   logger provided by Commons Logging.
3. Add file providers, using
   `addProvider()`.
4. Set the default provider, using
   `setDefaultProvider()`. This step is optional.
   See
   [UrlFileProvider](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/provider/url/UrlFileProvider.html)
   for a useful default provider.
5. Set the file replicator, using
   `setReplicator()`.
   This step is optional.
6. Set the temporary file store, using
   `setTemporaryFileStore()`.
   This step is optional.
7. Set the base file using
   `setBaseFile()`. The
   base file is used to resolve relative URI passed to
   `resolveFile()`. This step is optional.
8. Initialise the manager using
   `init()`.

You should make sure that you call
`close()` on the
manager when you are finished with it.

The third method for configuring Commons VFS, is to configure
it from a file. Create an instance of
[StandardFileSystemManager](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/impl/StandardFileSystemManager.html), and use its
`setConfiguration()` method to set the
location of the configuration file to use. The configuration
file format is described below.

`StandardFileSystemManager` is a subclass of
`DefaultFileSystemManager`, so you can also
configure it programmatically, as described above.

<a id="api--configuration-file"></a>

## Configuration File

The configuration file is an XML file. The root element
of the configuration file should be a
`<providers>` element.
The
`<providers>` element may contain:

- Zero or more
  `<provider>` elements.
- An optional
  `<default-provider>` element.
- Zero or more
  `<extension-map>` elements.
- Zero or more
  `<mime-type-map>` elements.

**`<provider>`**

The
`<provider>` element defines a file
provider. It must have a
`class-name` attribute, which specifies the fully-qualified name of the provider
class. The provider class must be public, and must have a
public constructor with an FileSystemManager argument which
allows the systems to pass the used filesystem manager.

The
`<provider>` element may contain
zero or more
`<scheme>` elements, and zero or more
`<if-available>` elements.

The
`<scheme>` element defines a URI scheme
that the provider will handle. It must have a
`name` attribute, which specifies the URI scheme.

The
`<if-available>` elements is used to
disable the provider if certain classes are not present in
the class-path.
It must have a
`class-name` attribute, which
specifies the fully qualified name of a class to test for.
If the class cannot be found, the provider is not registered.

**`<default-provider>`**

The
`<default-provider>` element defines
the default provider. It has the same format as the
`<provider>` element.

**`<extension-map>`**

The
`<extension-map>` element defines
a mapping from a file's extension to the provider that
should handle files with that extension.
It must have an
`extension` attribute, which
specifies the extension, and a
`scheme` attribute, which specifies the URI scheme of the provider.

**`<mime-type-map>`**

The
`<mime-type-map>` element defines
a mapping from a file's MIME type to the provider that
should handle files with that MIME type.
It must have an
`mime-type` attribute, which
specifies the MIME type, and a
`scheme` attribute, which specified the URI scheme of the provider.

Below is an example configuration file:

```

<providers>
    <provider class-name="org.apache.commons.vfs2.provider.zip.ZipFileProvider">
        <scheme name="zip"/>
    </provider>
    <extension-map extension="zip" scheme="zip"/>
    <mime-type-map mime-type="application/zip" scheme="zip"/>
    <provider class-name="org.apache.commons.vfs2.provider.ftp.FtpFileProvider">
        <scheme name="ftp"/>
        <if-available class-name="org.apache.commons.net.ftp.FTPFile"/>
    </provider>
    <default-provider class-name="org.apache.commons.vfs2.provider.url.UrlFileProvider"/>
</providers>
```

---

<a id="filesystems"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/filesystems.html -->

<!-- page_index: 6 -->

<a id="filesystems--supported-file-systems"></a>

# Supported File Systems

Commons VFS directly supports the following file systems with the listed
[capabilities](https://commons.apache.org/proper/commons-vfs/commons-vfs2/apidocs/org/apache/commons/vfs2/Capability.html):

| File System | Directory Contents | Authentication | Read | Write | Create/Delete | Random | Version | Rename |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [BZIP2](#filesystems--gzip_and_bzip2) | No | No | Yes | Yes | No | No | No | No |
| [File](#filesystems--local_files) | No | No | Yes | Yes | Yes | Read/Write | No | Yes |
| [FTP](#filesystems--ftp) | No | Yes | Yes | Yes | Yes | Read | No | Yes |
| [FTPS](#filesystems--ftps) | No | Yes | Yes | Yes | Yes | Read | No | Yes |
| [GZIP](#filesystems--gzip_and_bzip2) | No | No | Yes | Yes | No | No | No | No |
| [HDFS](#filesystems--hdfs) | Yes | No | Yes | No | No | Read | No | No |
| [HTTP](#filesystems--http_and_https) | Yes | Yes | Yes | No | No | Read | No | No |
| [HTTPS](#filesystems--http_and_https) | Yes | Yes | Yes | No | No | Read | No | No |
| [Jar](#filesystems--zip.2c_jar_and_tar) | No | No | Yes | No | No | No | No | No |
| [RAM](#filesystems--ram) | No | No | Yes | Yes | Yes | Read/Write | No | Yes |
| [RES](#filesystems--res) | No | No | Yes | Yes | Yes | Read/Write | No | Yes |
| [SFTP](#filesystems--sftp) | No | Yes | Yes | Yes | Yes | Read | No | Yes |
| [Tar](#filesystems--zip.2c_jar_and_tar) | No | No | Yes | No | No | No | No | No |
| [Temp](#filesystems--temporary_fils) | No | No | Yes | Yes | Yes | Read/Write | No | Yes |
| [WebDAV](#filesystems--webdav) | Yes | Yes | Yes | Yes | Yes | Read/Write | Yes | Yes |
| [Zip](#filesystems--zip.2c_jar_and_tar) | No | No | Yes | No | No | No | No | No |

<a id="filesystems--things-from-the-sandbox"></a>

# Things from the sandbox

The following file systems are in development:

| File System | Directory Contents | Authentication | Read | Write | Create/Delete | Random | Version | Rename |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [CIFS](#filesystems--cifs) | No | Yes | Yes | Yes | Yes | Read/Write | No | Yes |
| [mime](#filesystems--mime) | No | No | Yes | No | No | No | No | No |

<a id="filesystems--naming"></a>

# Naming

All filenames are treated as URIs. One of the consequences of this is you have to encode the '%'
character using `%25`.
Depending on the filesystem additional characters are encoded if needed. This is done automatically, but
might be reflected in the filename.

**Examples**

- `file:///somedir/some%25file.txt`

Many file systems accept a userid and password as part of the url. However, storing
a password in clear text in a file is usually unacceptable. To help with that
Commons VFS provides a mechanism to encrypt the password. It should be noted though, that this is not completely secure since the password needs to be unencrypted
before Commons VFS can use it.

To create an encrypted password do:

 `java -cp commons-vfs-2.0.jar org.apache.commons.vfs2.util.EncryptUtil encrypt mypassword`

where *mypassword* is the password you want to encrypt. The result of this will be a
single line of output containing uppercase hex characters. For example,

`java -cp commons-vfs-2.0.jar org.apache.commons.vfs2.util.EncryptUtil encrypt WontUBee9
D7B82198B272F5C93790FEB38A73C7B8`

Then cut the output returned and paste it into the URL as:

`https://testuser:{D7B82198B272F5C93790FEB38A73C7B8}@myhost.com/svn/repos/vfstest/trunk`

VFS treats a password enclosed in {} as being encrypted and will decrypt the password
before using it.

<a id="filesystems--local-files"></a>

# Local Files

Provides access to the files on the local physical file system.

**URI Format**

`[file://]
absolute-path`

Where
`absolute-path` is a valid absolute
file name for the local platform. UNC names are supported
under Windows.

**Examples**

- `file:///home/someuser/somedir`
- `file:///C:/Documents and Settings`
- `file://///somehost/someshare/afile.txt`
- `/home/someuser/somedir`
- `c:\program files\some dir`
- `c:/program files/some dir`

<a id="filesystems--zip-jar-and-tar"></a>

# Zip, Jar and Tar

Provides read-only access to the contents of Zip, Jar and Tar files.

**URI Format**

`zip://
arch-file-uri[!
absolute-path]`

`jar://
arch-file-uri[!
absolute-path]`

`tar://
arch-file-uri[!
absolute-path]`

`tgz://
arch-file-uri[!
absolute-path]`

`tbz2://
arch-file-uri[!
absolute-path]`

Where
`arch-file-uri` refers to a file of any
supported type, including other zip files. Note: if you would like
to use the ! as normal character it must be escaped
using `%21`.
`tgz` and `tbz2` are convenience for `tar:gz` and `tar:bz2`.

**Examples**

- `jar:../lib/classes.jar!/META-INF/manifest.mf`
- `zip:http://somehost/downloads/somefile.zip`
- `jar:zip:outer.zip!/nested.jar!/somedir`
- `jar:zip:outer.zip!/nested.jar!/some%21dir`
- `tar:gz:http://anyhost/dir/mytar.tar.gz!/mytar.tar!/path/in/tar/README.txt`
- `tgz:file://anyhost/dir/mytar.tgz!/somepath/somefile`

<a id="filesystems--gzip-and-bzip2"></a>

# gzip and bzip2

Provides read-only access to the contents of gzip and bzip2 files.

**URI Format**

`gz://
compressed-file-uri`

`bz2://
compressed-file-uri`

Where
`compressed-file-uri` refers to a file of any
supported type. There is no need to add a `!` part to the URI if
you read the content of the file you always will get the uncompressed
version.

**Examples**

- `gz:/my/gz/file.gz`

<a id="filesystems--hdfs"></a>

# HDFS

Provides (read-only) access to files in an Apache Hadoop File System (HDFS).
On Windows the [integration test](#testing) is disabled by default, as it
requires binaries.

**URI Format**

`hdfs://
hostname[:
port][
absolute-path]`

**Examples**

- `hdfs://somehost:8080/downloads/some_dir`
- `hdfs://somehost:8080/downloads/some_file.ext`

<a id="filesystems--http-and-https"></a>

# HTTP and HTTPS

Provides access to files on an HTTP server.

**URI Format**

`http://[
username[:
password]@]
hostname[:
port][
absolute-path]`

`https://[
username[:
password]@]
hostname[:
port][
absolute-path]`

**File System Options**

- **proxyHost** The proxy host to connect through.
- **proxyPort** The proxy port to use.
- **proxyScheme** The proxy scheme (http/https) to use.
- **cookies** An array of Cookies to add to the request.
- **maxConnectionsPerHost** The maximum number of connections allowed to
  a specific host and port. The default is 5.
- **maxTotalConnections** The maximum number of connections allowed to
  all hosts. The default is 50.
- **keystoreFile** The keystore file for SSL connections.
- **keystorePass** The keystore password.
- **keystoreType** The keystore type.

**Examples**

- `http://somehost:8080/downloads/somefile.jar`
- `http://myusername@somehost/index.html`

<a id="filesystems--webdav"></a>

# WebDAV

Provides access to files on a WebDAV server through the modules
[`commons-vfs2-jackrabbit1`](#commons-vfs2-jackrabbit1)
and
[`commons-vfs2-jackrabbit2`](#commons-vfs2-jackrabbit2).

**URI Format**

`webdav://[
username[:
password]@]
hostname[:
port][
absolute-path]`

**File System Options**

- **versioning** true if versioning should be enabled
- **creatorName** the user name to be identified with changes to a file. If
  not set the user name used to authenticate will be used.

**Examples**

- `webdav://somehost:8080/dist`

<a id="filesystems--ftp"></a>

# FTP

Provides access to the files on an FTP server.

**URI Format**

`ftp://[
username[:
password]@]
hostname[:
port][
relative-path]`

**Examples**

- `ftp://myusername:mypassword@somehost/pub/downloads/somefile.tgz`

By default, the path is relative to the user's home directory. This can be changed with:

`FtpFileSystemConfigBuilder.getInstance().setUserDirIsRoot(options, false);`

<a id="filesystems--ftps"></a>

# FTPS

Provides access to the files on an FTP server over SSL.

**URI Format**

`ftps://[
username[:
password]@]
hostname[:
port][
absolute-path]`

**Examples**

- `ftps://myusername:mypassword@somehost/pub/downloads/somefile.tgz`

<a id="filesystems--sftp"></a>

# SFTP

Provides access to the files on an SFTP server (that is, an SSH
or SCP server).

**URI Format**

`sftp://[
username[:
password]@]
hostname[:
port][
relative-path]`

**Examples**

- `sftp://myusername:mypassword@somehost/pub/downloads/somefile.tgz`

By default, the path is relative to the user's home directory. This can be changed with:

`FtpFileSystemConfigBuilder.getInstance().setUserDirIsRoot(options, false);`

<a id="filesystems--cifs"></a>

# CIFS

The CIFS (sandbox) filesystem provides access to a CIFS server, such as
a Samba server, or a Windows share.

**URI Format**

`smb://[
username[:
password]@]
hostname[:
port][
absolute-path]`

**Examples**

- `smb://somehost/home`

<a id="filesystems--temporary-files"></a>

# Temporary Files

Provides access to a temporary file system, or scratchpad, that is deleted when Commons VFS shuts down. The temporary file
system is backed by a local file system.

**URI Format**

`tmp://[
absolute-path]`

**Examples**

- `tmp://dir/somefile.txt`

<a id="filesystems--resource"></a>

# Resource

This is not really a filesystem, it just tries to look up a resource using javas `ClassLoader.getResource()`
and creates a VFS url for further processing.

**URI Format**

`res://[
path]`

**Examples**

- `res://path/in/classpath/image.png`
  might result in
  `jar:file://my/path/to/images.jar!/path/in/classpath/image.png`

<a id="filesystems--ram"></a>

# RAM

A filesystem which stores all the data in memory (one byte array for each file content).

**URI Format**

`ram://[
path]`

**File System Options**

- **maxsize** Maximum filesystem size (total bytes of all file contents).

**Examples**

- `ram:///any/path/to/file.txt`

<a id="filesystems--mime"></a>

# MIME

This (sandbox) filesystem can read mails and its attachements like archives.
If a part in the parsed mail has no name, a dummy name will be generated.
The dummy name is: \_body\_part\_X where X will be replaced by the part number.

**URI Format**

`mime://
mime-file-uri[!
absolute-path]`

**Examples**

- `mime:file:///your/path/mail/anymail.mime!/`
- `mime:file:///your/path/mail/anymail.mime!/filename.pdf`
- `mime:file:///your/path/mail/anymail.mime!/_body_part_0`

---

<a id="anttasks"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/anttasks.html -->

<!-- page_index: 7 -->

<a id="anttasks--ant-tasks"></a>

# Ant Tasks

Commons VFS includes several Ant tasks that can be used
to create, delete, copy and move files of any supported type.
The tasks are:

- [`<v-copy>`](#anttasks--v-copy)
  .
  Copies a set of source folders and files to a destination
  folder.
- [`<v-delete>`](#anttasks--v-delete)
  .
  Deletes a file or folder.
- [`<v-mkdir>`](#anttasks--v-mkdir)
  .
  Creates a folder.
- [`<v-move>`](#anttasks--v-move)
  .
  Moves a set of source folders and files to a destination
  folder.
- [`<v-sync>`](#anttasks--v-sync)
  .
  Synchronises a destination folder with a set of source
  folder and files.

All file name attributes support relative and absolute local
file names, and
[absolute URI](#filesystems)
.
File names are interpreted relative to the Ant project's base
directory.

<a id="anttasks--using-the-tasks"></a>

## Using the Tasks

To use the Ant tasks, copy commons-vfs.jar and its
dependencies into the
`$ANT_HOME/lib`
directory, and use the following in your Ant script to define the tasks:

```

<taskdef resource="org/apache/commons/vfs2/tasks/tasks.properties"/>
                    
```

Alternatively, you can provide an explicit classpath when
you define the tasks:

```

<taskdef resource="org/apache/commons/vfs2/tasks/tasks.properties">
    <classpath> ... </classpath>
</taskdef>
                    
```

You can also use antlib:
**Notice: VFS tasks registered that way do not have te "v-" prefix.**
If you migrate to antlib simply replace "v-" by e.g. "vfs:" or whatever
namespace you use.

```

<project ... xmlns:vfs="antlib:org.apache.commons.vfs2.tasks">
    <target name="dosomething">
        <vfs:copy .../>
    </target>
</project>
                    
```

<a id="anttasks--v-copy"></a>

# V-Copy

Copies a set of files to a destination folder. Does not copy
source files where the destination file exists and is newer than
the source file. The copy task takes the following attributes:

<table class="bodyTable">
<tr>
<th>Name</th>
<th>Description</th>
<th>Required</th>
</tr>
<tr>
<td>destdir</td>
<td>The destination folder. This folder is created if it
                        does not exist.</td>
<td rowspan="2">One only</td>
</tr>
<tr>
<td>destfile</td>
<td>The destination file. Can only be used if there is a
                        single source file.</td>
</tr>
<tr>
<td>srcdir</td>
<td>The source folder. If used the includes and destdir
                        attributes should be specified.</td>
<td>No</td>
</tr>
<tr>
<td>includes</td>
<td>A comma or space separated list of files. The files
                        are resolved in combination with the specified
                        srcdir attribute.</td>
<td>Only if srcdir is specified.</td>
</tr>
<tr>
<td>overwrite</td>
<td>Always copy files, ignoring the last-modified time of
                        the destination file.</td>
<td>No, default is
                        <code>false</code>
                        .
                    </td>
</tr>
<tr>
<td>preservelastmodified</td>
<td>Set the last-modified time of destination files to
                        the same value as the source files. May not be supported
                        by the destination file system.</td>
<td>No, default is
                        <code>true</code>
                        .
                    </td>
</tr>
<tr>
<td>srcdirisbase</td>
<td>Set whether the source directory should be used as base directory.
                        If set to true, the subdirectories of the specified directories will be copied as well.</td>
<td>No, default is
                        <code>false</code>
                        .
                    </td>
</tr>
<tr>
<td>src</td>
<td>A source file or folder to copy. Copies all descendants
                        of a folder.</td>
<td>No</td>
</tr>
</table>

<a id="anttasks--nested-elements"></a>

## Nested Elements

**`<src>`**

Defines a source file or folder to copy. It takes the
following attributes:

| Name | Description | Required |
| --- | --- | --- |
| file | The source file. | Yes |

<a id="anttasks--v-move"></a>

# V-Move

Moves a set of files to a destination folder. Has the same
attributes and elements as the copy task and following attributes:

| Name | Description | Required |
| --- | --- | --- |
| tryRename | The destination folder. This folder is created if it does not exist. | No, default is `false` |

<a id="anttasks--v-sync"></a>

# V-Sync

Synchronises a destination folder with a set of source files.
Has the same attributes and elements as the copy task.

<a id="anttasks--v-delete"></a>

# V-Delete

Deletes a file or folder. It takes the following attributes:

<table class="bodyTable">
<tr>
<th>Name</th>
<th>Description</th>
<th>Required</th>
</tr>
<tr>
<td>file</td>
<td>The file or folder to delete. All descendants of
                        the folder are deleted.</td>
<td rowspan="2">One only</td>
</tr>
<tr>
<td>srcdir</td>
<td>The source folder. If used the includes attribute
                        should be specified.</td>
</tr>
<tr>
<td>includes</td>
<td>A comma or space separated list of files. The files
                        are resolved in combination with the specified
                        srcdir attribute.</td>
<td>Only if srcdir is specified.</td>
</tr>
</table>

<a id="anttasks--v-mkdir"></a>

# V-Mkdir

Creates a folder. It takes the following attributes:

| Name | Description | Required |
| --- | --- | --- |
| dir | The folder create. | Yes |

---

<a id="testing"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/testing.html -->

<!-- page_index: 8 -->

<a id="testing--vfs-test-suite"></a>

# VFS Test Suite

Apache Commons VFS comes with a suite of (nearly 2000) tests (in `core/src/test`). The JUnit framework
is used, and executed at build time via the Maven
[Surefire plugin](https://maven.apache.org/surefire/maven-surefire-plugin/) by the `mvn test` goal.
If you plan to contribute a patch for a bug or feature, make sure to also provide a test
which can reproduce the bug or exercise the new feature. Also run the whole test suite against the patched code.

The [JUnit](https://junit.org) tests will execute unit, compile but also integration tests to test the API and the implementation.
The local file provider is tested in a directory of the local file system. Virtual providers (compression and archive)
and resource access is based on this test directory as well. For testing the other providers some test servers are started.
The following table described the details (for versions have a look in the
[dependency report](https://commons.apache.org/proper/commons-vfs/commons-vfs2/dependencies.html#test)):

| Provider | Tested Against | External |
| --- | --- | --- |
| ftp | [Apache FtpServer](https://mina.apache.org/ftpserver-project/) | -Pftp -Dtest.ftp.uri=ftp://test:test@localhost:123 |
| ftps | [Apache FtpServer](https://mina.apache.org/ftpserver-project/) | -Pftps -Dtest.ftps.uri=ftps://test:test@localhost:123 |
| hdfs | Apache Hadoop HDFS ([MiniDFSCluster](https://web.archive.org/web/20170706071449/https%3A//wiki.apache.org/hadoop/HowToDevelopUnitTests)) | -P!no-test-hdfs (see below) |
| http | NHttpServer (local adaption of org.apache.http.examples.nio.NHttpServer) | -Phttp -Dtest.http.uri=http://localhost:123 |
| https | (not tested) | N/A |
| jar | Local File Provider | N/A |
| local | Local File system | N/A |
| ram | In Memory test | N/A |
| res | Local File Provider / JAR Provider | N/A |
| sftp | [Apache SSHD](https://mina.apache.org/sshd-project/index.html) | -Psftp -Dtest.sftp.uri=sftp://testtest@localhost:123 |
| tmp | Local File system | N/A |
| url | NHttpServer (local adaption of org.apache.http.examples.nio.NHttpServer) Local File system | -Phttp -Dtest.http.uri=http://localhost:128 |
| webdav | [Apache Jackrabbit Standalone Server](https://jackrabbit.apache.org/jcr/standalone-server.html) | -Pwebdav -Dtest.webdav.uri=webdav://admin@localhost:123/repository/default |
| zip | Local File Provider | N/A |
| smb (sandbox) | (not tested) | -Psmb -Dtest.smb.uri=smb://DOMAIN\User:Pass@host/C$/commons-vfs2/core/target/test-classes/test-data |

Some tests are operating-system specific. Some Windows File Name tests are only run on Windows
and the HDFS test is skipped in case of Windows (because it requires additional binaries). It is therefore
a good idea to run the tests at least on Windows and Linux/Unix before release. The `smb` provider
from the sandbox is not tested unless you specify a `-Dtest.smb.uri` and the `-Psmb` profile.

<a id="testing--running-hdfs-tests-on-windows"></a>

# Running HDFS tests on Windows

The HDFS integration tests use the HDFS MiniCluster. This does not work on Windows without special preparation:
you need to build and provide the (2.6.0) native binary (`winutils.exe`) and library (`hadoop.dll`) for the
MiniCluster used in the test cases. Both files are not part of the Hadoop Commons 2.6.0
distribution ([HADOOP-10051](https://issues.apache.org/jira/browse/HADOOP-10051)). After you built
a compatible version, put them on your Windows `PATH` and then run the tests
by disabling the `no-test-hdfs` profile, or by requesting explicitly the excluded tests:

```

> set VFS=C:\commons-vfs2-project\core
> cd %VFS%\core
> mkdir bin\
> copy \temp\winutils.exe \temp\hadoop.dll bin\
> set HADOOP_HOME=%VFS%\core
> set PATH=%VFS%\core\bin;%PATH%
> winutils.exe systeminfo 8518668288,8520572928,4102033408,4544245760,8,1600000,6042074
> mvn -P!no-test-hdfs clean test     # runs all test and HDFS tests
> mvn clean test -Dtest=org.apache.commons.vfs2.provider.hdfs.test.HdfsFileProviderTest,org.apache.commons.vfs2.provider.hdfs.test.HdfsFileProviderTestCase... Tests run: 13, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 13.006 sec - in org.apache.commons.vfs2.provider.hdfs.test.HdfsFileProviderTest Tests run: 77, Failures: 0, Errors: 0, Skipped: 0, Time elapsed: 11.728 sec - in org.apache.commons.vfs2.provider.hdfs.test.HdfsFileProviderTestCase
```

<a id="testing--running-smb-tests-against-windows"></a>

# Running SMB tests against Windows

The SMB provider from the sandbox project cannot be tested automatically. You need to prepare a CIFS/SMB server
to test it manually. If you develop on Windows, the following procedure uses the Windows File Sharing and does
not require to prepare the data directory (as you can directly point to your workspace):

```

> set VFS=C:\commons-vfs2-project
> cd %VFS%
> mvn clean install -Pinclude-sandbox -DskipTests  # prepares test data and parent
> cd %VFS%\sandbox
> mvn test -Psmb -Dtest.smb.url=smb//Domain\User:Pass@yourhost/C$/commons-vfs2-project/core/target/test-classes/test-data... Tests run: 82, Failures: 0, Errors: 1, Skipped: 0
```

Note: there is a known test failure in this case, see
[VFS-562](https://issues.apache.org/jira/browse/VFS-562) on the JIRA bug tracker if you want
to help.

<a id="testing--running-tests-with-external-servers"></a>

# Running tests with external servers

In order to test VFS for compatibility with other implementations (or in case of SMB to
test it manually) some of the integration tests can be configured to connect to custom URL.
This generally involves preparing the server, selecting a profile and specifying the URL in
a system property (see table above).

<a id="testing--preparing-external-servers"></a>

## Preparing external Servers

If you want to run the tests against external servers, run `mvn install`.
This will compile all the source and test source and then run all the tests
for providers that use the local file system.
After running the maven build, the test data can be found in
`core/target/test-classes/test-data/`.

Each repository/server should contain the following list of files for the tests to
complete successfully.

```

code/sealed/AnotherClass.class
code/ClassToLoad.class
largefile.tar.gz
nested.jar
nested.tar
nested.tbz2
nested.tgz
nested.zip
read-tests/dir1/file1.txt
read-tests/dir1/file2.txt
read-tests/dir1/file3.txt
read-tests/dir1/subdir1/file1.txt
read-tests/dir1/subdir1/file2.txt
read-tests/dir1/subdir1/file3.txt
read-tests/dir1/subdir2/file1.txt
read-tests/dir1/subdir2/file2.txt
read-tests/dir1/subdir2/file3.txt
read-tests/dir1/subdir3/file1.txt
read-tests/dir1/subdir3/file2.txt
read-tests/dir1/subdir3/file3.txt
read-tests/empty.txt
read-tests/file1.txt
read-tests/file space.txt
read-tests/file%.txt
test-hash-#test.txt
test.jar
test.mf
test.policy
test.tar
test.tbz2
test.tgz
test.zip
write-tests/
```

The Apache Commons Wiki contains a list of configuration examples for external servers.
Please consider contributing if you have set up a specific scenario:
<https://wiki.apache.org/commons/VfsTestServers>.

---

<a id="commons-vfs2-ant"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-ant/index.html -->

<!-- page_index: 9 -->

<a id="commons-vfs2-ant--about-apache-commons-vfs-ant-tasks"></a>

# About Apache Commons VFS Ant Tasks

Apache Commons VFS Ant Tasks.

---

<a id="commons-vfs2"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2/index.html -->

<!-- page_index: 10 -->

<a id="commons-vfs2--about-apache-commons-vfs-core"></a>

# About Apache Commons VFS Core

This is the core module containing the Apache Commons VFS API, implementation as well as various
[file system providers](#filesystems).

The documentation on how to use the API can be found in the
[parent module](#api).

---

<a id="commons-vfs2-examples"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-examples/index.html -->

<!-- page_index: 11 -->

<a id="commons-vfs2-examples--about-apache-commons-vfs-examples"></a>

# About Apache Commons VFS Examples

This example module contains sample
[source code](https://commons.apache.org/proper/commons-vfs/commons-vfs2-examples/xref/index.html) for learning how to use Apache
Commons VFS in the `org.apache.commons.vfs2.example` package.

The `org.apache.commons.vfs2.libcheck` package contains some Java
classes to exercise some of the functionality of the libraries (dependencies)
used by Apache Commons VFS. This is mainly for the maintainers of VFS providers.

<a id="commons-vfs2-examples--commons-vfs-shell-example"></a>

# Commons VFS Shell Example

The Commons VFS Shell is an example for a command line shell.
It can be used to play with different providers and to verify
an installation.

Check out the page [VfsExampleShell](https://wiki.apache.org/commons/VfsExampleShell)
on the Apache Commons Wiki for a number of examples. In particular you can use the `info`
command to list the schemes which are auto discovered by the `StandardFileSystemManager`.

The following examples assume an environment variable REP which points to a populated local Maven
repository. As an alternative you can [download](https://commons.apache.org/proper/commons-vfs/download.html) the required
[dependencies](https://commons.apache.org/proper/commons-vfs/commons-vfs2/dependencies.html) manually. (The commons-collection4
dependency is not needed for the VFS Shell as it does not use `LRUFilesCache`.) Because
of licensing restrictions the sandbox component must be
[built locally](https://commons.apache.org/proper/commons-vfs/commons-vfs2-sandbox/index.html) and then installed into the repository.

<a id="commons-vfs2-examples--starting-vfs-shell-on-linux-unix"></a>

## Starting VFS Shell on Linux/Unix

```

REP=~/.m2/repository
LIB=$REP/commons-logging/commons-logging/1.2/commons-logging-1.2.jar
LIB=$LIB:$REP/commons-net/commons-net/3.6/commons-net-3.6.jar
# LIB=$LIB:$REP/org/apache/commons/commons-collections4/4.1/commons-collection-4.1.jar
LIB=$LIB:$REP/commons-httpclient/commons-httpclient/3.1/commons-httpclient-3.1.jar:$REP/commons-codec/commons-codec/1.2/commons-codec-1.2.jar
LIB=$LIB:$REP/com/jcraft/jsch/0.1.54/jsch-0.1.54.jar
# next 3 lines are for webdav
LIB=$LIB:$REP/org/apache/jackrabbit/jackrabbit-webdav/1.6.5/jackrabbit-webdav-1.6.5.jar
LIB=$LIB:$REP/org/slf4j/slf4j-api/1.5.11/slf4j-api-1.5.11.jar:$REP/org/slf4j/slf4j-simple/1.5.3/slf4j-simple-1.5.3.jar
LIB=$LIB:$REP/org/apache/jackrabbit/jackrabbit-jcr-commons/1.6.5/jackrabbit-jcr-commons-1.6.5.jar
# LIB=$LIB:$REP/org/apache/commons/commons-vfs2-sandbox/2.3/commons-vfs2-sandbox-2.3.jar:$REP/jcifs/jcifs/0.8.3/jcifs-0.8.3.jar
LIB=$LIB:$REP/org/apache/commons/commons-vfs2-examples/2.3/commons-vfs2-examples-2.3.jar
LIB=$LIB:$REP/org/apache/commons/commons-vfs2/2.3/commons-vfs2-2.3.jar
java -cp $LIB org.apache.commons.vfs2.example.Shell
```

<a id="commons-vfs2-examples--starting-vfs-shell-on-windows"></a>

## Starting VFS Shell on Windows

```

set REP=%USERPROFILE%\.m2\repository
set LIB=%REP%\commons-logging\commons-logging\1.2\commons-logging-1.2.jar
set LIB=%LIB%;%REP%\commons-net\commons-net\2.2\commons-net-2.2.jar
REM # set LIB=%LIB%;%REP%\org\apache\commons\commons-collections4\4.1\commons-collection-4.1.jar
set LIB=%LIB%;%REP%\commons-httpclient\commons-httpclient\3.1\commons-httpclient-3.1.jar;%REP%\commons-codec\commons-codec\1.2\commons-codec-1.2.jar
set LIB=%LIB%;%REP%\com\jcraft\jsch\0.1.54\jsch-0.1.54.jar
REM # next 3 lines are for webdav
set LIB=%LIB%;%REP%\org\apache\jackrabbit\jackrabbit-webdav\1.6.5\jackrabbit-webdav-1.6.5.jar
set LIB=%LIB%;%REP%\org\slf4j\slf4j-api\1.5.11\slf4j-api-1.5.11.jar;%REP%\org\slf4j\slf4j-simple\1.5.3\slf4j-simple-1.5.3.jar
set LIB=%LIB%;%REP%\org\apache\jackrabbit\jackrabbit-jcr-commons\1.6.5\jackrabbit-jcr-commons-1.6.5.jar
REM # set LIB=%LIB%;%REP%\org\apache\commons\commons-vfs2-sandbox\2.3\commons-vfs2-sandbox-2.3.jar;%REP%\jcifs\jcifs\0.8.3\jcifs-0.8.3.jar
set LIB=%LIB%;%REP%\org\apache\commons\commons-vfs2-examples\2.3\commons-vfs2-examples-2.3.jar
set LIB=%LIB%;%REP%\org\apache\commons\commons-vfs2\2.3\commons-vfs2-2.3.jar
java -cp %LIB% org.apache.commons.vfs2.example.Shell
```

---

<a id="commons-vfs2-hdfs"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-hdfs/index.html -->

<!-- page_index: 12 -->

<a id="commons-vfs2-hdfs--about-apache-commons-vfs-hdfs"></a>

# About Apache Commons VFS HDFS

Apache Commons VFS is a Virtual File System library - Apache Hadoop HDFS provider.

---

<a id="commons-vfs2-jackrabbit1"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit1/index.html -->

<!-- page_index: 13 -->

<a id="commons-vfs2-jackrabbit1--about-apache-commons-vfs-jackrabbit-1.x"></a>

# About Apache Commons VFS Jackrabbit 1.x

Apache Commons VFS is a Virtual File System library - Jackrabbit-based WebDAV provider.

---

<a id="commons-vfs2-jackrabbit2"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit2/index.html -->

<!-- page_index: 14 -->

<a id="commons-vfs2-jackrabbit2--about-apache-commons-vfs-jackrabbit-2.x"></a>

# About Apache Commons VFS Jackrabbit 2.x

Apache Commons VFS is a Virtual File System library - Jackrabbit2-based WebDAV provider.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/project-info.html -->

<!-- page_index: 15 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons VFS is a Virtual File System library. |
| [Summary](#summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-vfs/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-vfs/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-vfs/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-vfs/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-vfs/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-vfs/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/summary.html -->

<!-- page_index: 16 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS Project |
| Description | Apache Commons VFS is a Virtual File System library. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/](#index) |

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
| ArtifactId | commons-vfs2-project |
| Version | 2.11.0-SNAPSHOT |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/modules.html -->

<!-- page_index: 17 -->

<a id="modules--project-modules"></a>

# Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons VFS](#commons-vfs2) | Apache Commons VFS is a Virtual File System library. |
| [Apache Commons VFS Ant Tasks](#commons-vfs2-ant) | Apache Commons VFS Ant Tasks. |
| [Apache Commons VFS HDFS](#commons-vfs2-hdfs) | Apache Commons VFS is a Virtual File System library - Apache Hadoop HDFS provider. |
| [Apache Commons VFS Jackrabbit 1.x](#commons-vfs2-jackrabbit1) | Apache Commons VFS is a Virtual File System library - Jackrabbit-based WebDAV provider. |
| [Apache Commons VFS Jackrabbit 2.x](#commons-vfs2-jackrabbit2) | Apache Commons VFS is a Virtual File System library - Jackrabbit2-based WebDAV provider. |
| [Apache Commons VFS Examples](#commons-vfs2-examples) | Apache Commons VFS is a Virtual File System library - Examples. |
| [Apache Commons VFS Bill of Materials](#commons-vfs2-bom) | This Bill of Materials POM can be used to ease dependency management when referencing multiple artifacts using Maven. |
| [Apache Commons VFS Distribution](#commons-vfs2-distribution) | Apache Commons VFS is a Virtual File System library - Distribution archives. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/team.html -->

<!-- page_index: 18 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/ci-management.html -->

<!-- page_index: 19 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-ant-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-ant/ci-management.html -->

<!-- page_index: 20 -->

<a id="commons-vfs2-ant-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-ant-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-ant-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-ant-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-ant/scm.html -->

<!-- page_index: 21 -->

<a id="commons-vfs2-ant-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-ant-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2-ant
```

<a id="commons-vfs2-ant-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-ant-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-ant-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-ant-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-ant/summary.html -->

<!-- page_index: 22 -->

<a id="commons-vfs2-ant-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-ant-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS Ant Tasks |
| Description | Apache Commons VFS Ant Tasks. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/commons-vfs2-ant/](#commons-vfs2-ant) |

<a id="commons-vfs2-ant-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-ant-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2-ant |
| Version | 2.11.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-vfs2-ant-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-ant/team.html -->

<!-- page_index: 23 -->

<a id="commons-vfs2-ant-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-ant-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-ant-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="commons-vfs2-bom-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-bom/ci-management.html -->

<!-- page_index: 24 -->

<a id="commons-vfs2-bom-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-bom-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-bom-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-bom"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-bom/index.html -->

<!-- page_index: 25 -->

<a id="commons-vfs2-bom--about-apache-commons-vfs-bill-of-materials"></a>

# About Apache Commons VFS Bill of Materials

This Bill of Materials POM can be used to ease dependency management when referencing multiple artifacts using Maven.

---

<a id="commons-vfs2-bom-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-bom/scm.html -->

<!-- page_index: 26 -->

<a id="commons-vfs2-bom-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-bom-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2-bom
```

<a id="commons-vfs2-bom-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-bom-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-bom-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-bom-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-bom/summary.html -->

<!-- page_index: 27 -->

<a id="commons-vfs2-bom-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-bom-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS Bill of Materials |
| Description | This Bill of Materials POM can be used to ease dependency management when referencing multiple artifacts using Maven. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/commons-vfs2-bom/](#commons-vfs2-bom) |

<a id="commons-vfs2-bom-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-bom-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2-bom |
| Version | 2.11.0-SNAPSHOT |
| Type | pom |

---

<a id="commons-vfs2-bom-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-bom/team.html -->

<!-- page_index: 28 -->

<a id="commons-vfs2-bom-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-bom-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-bom-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="commons-vfs2-distribution-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-distribution/ci-management.html -->

<!-- page_index: 29 -->

<a id="commons-vfs2-distribution-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-distribution-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-distribution-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-distribution"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-distribution/index.html -->

<!-- page_index: 30 -->

<a id="commons-vfs2-distribution--about-apache-commons-vfs-distribution"></a>

# About Apache Commons VFS Distribution

Apache Commons VFS is a Virtual File System library - Distribution archives.

---

<a id="commons-vfs2-distribution-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-distribution/scm.html -->

<!-- page_index: 31 -->

<a id="commons-vfs2-distribution-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-distribution-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2-distribution
```

<a id="commons-vfs2-distribution-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-distribution-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-distribution-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-distribution-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-distribution/summary.html -->

<!-- page_index: 32 -->

<a id="commons-vfs2-distribution-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-distribution-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS Distribution |
| Description | Apache Commons VFS is a Virtual File System library - Distribution archives. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/commons-vfs2-distribution/](#commons-vfs2-distribution) |

<a id="commons-vfs2-distribution-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-distribution-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2-distribution |
| Version | 2.11.0-SNAPSHOT |
| Type | pom |

---

<a id="commons-vfs2-distribution-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-distribution/team.html -->

<!-- page_index: 33 -->

<a id="commons-vfs2-distribution-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-distribution-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-distribution-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="commons-vfs2-examples-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-examples/ci-management.html -->

<!-- page_index: 34 -->

<a id="commons-vfs2-examples-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-examples-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-examples-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-examples-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-examples/scm.html -->

<!-- page_index: 35 -->

<a id="commons-vfs2-examples-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-examples-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2-examples
```

<a id="commons-vfs2-examples-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-examples-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-examples-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-examples-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-examples/summary.html -->

<!-- page_index: 36 -->

<a id="commons-vfs2-examples-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-examples-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS Examples |
| Description | Apache Commons VFS is a Virtual File System library - Examples. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/commons-vfs2-examples/](#commons-vfs2-examples) |

<a id="commons-vfs2-examples-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-examples-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2-examples |
| Version | 2.11.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-vfs2-examples-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-examples/team.html -->

<!-- page_index: 37 -->

<a id="commons-vfs2-examples-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-examples-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-examples-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="commons-vfs2-hdfs-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-hdfs/ci-management.html -->

<!-- page_index: 38 -->

<a id="commons-vfs2-hdfs-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-hdfs-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-hdfs-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-hdfs-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-hdfs/scm.html -->

<!-- page_index: 39 -->

<a id="commons-vfs2-hdfs-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-hdfs-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2-hdfs
```

<a id="commons-vfs2-hdfs-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-hdfs-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-hdfs-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-hdfs-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-hdfs/summary.html -->

<!-- page_index: 40 -->

<a id="commons-vfs2-hdfs-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-hdfs-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS HDFS |
| Description | Apache Commons VFS is a Virtual File System library - Apache Hadoop HDFS provider. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/commons-vfs2-hdfs/](#commons-vfs2-hdfs) |

<a id="commons-vfs2-hdfs-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-hdfs-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2-hdfs |
| Version | 2.11.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-vfs2-hdfs-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-hdfs/team.html -->

<!-- page_index: 41 -->

<a id="commons-vfs2-hdfs-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-hdfs-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-hdfs-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="commons-vfs2-jackrabbit1-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit1/ci-management.html -->

<!-- page_index: 42 -->

<a id="commons-vfs2-jackrabbit1-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-jackrabbit1-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-jackrabbit1-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-jackrabbit1-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit1/scm.html -->

<!-- page_index: 43 -->

<a id="commons-vfs2-jackrabbit1-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-jackrabbit1-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2-jackrabbit1
```

<a id="commons-vfs2-jackrabbit1-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-jackrabbit1-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-jackrabbit1-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-jackrabbit1-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit1/summary.html -->

<!-- page_index: 44 -->

<a id="commons-vfs2-jackrabbit1-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-jackrabbit1-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS Jackrabbit 1.x |
| Description | Apache Commons VFS is a Virtual File System library - Jackrabbit-based WebDAV provider. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit1/](#commons-vfs2-jackrabbit1) |

<a id="commons-vfs2-jackrabbit1-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-jackrabbit1-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2-jackrabbit1 |
| Version | 2.11.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-vfs2-jackrabbit1-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit1/team.html -->

<!-- page_index: 45 -->

<a id="commons-vfs2-jackrabbit1-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-jackrabbit1-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-jackrabbit1-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="commons-vfs2-jackrabbit2-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit2/ci-management.html -->

<!-- page_index: 46 -->

<a id="commons-vfs2-jackrabbit2-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-jackrabbit2-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-jackrabbit2-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-jackrabbit2-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit2/scm.html -->

<!-- page_index: 47 -->

<a id="commons-vfs2-jackrabbit2-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-jackrabbit2-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2-jackrabbit2
```

<a id="commons-vfs2-jackrabbit2-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-jackrabbit2-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-jackrabbit2-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-jackrabbit2-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit2/summary.html -->

<!-- page_index: 48 -->

<a id="commons-vfs2-jackrabbit2-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-jackrabbit2-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS Jackrabbit 2.x |
| Description | Apache Commons VFS is a Virtual File System library - Jackrabbit2-based WebDAV provider. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit2/](#commons-vfs2-jackrabbit2) |

<a id="commons-vfs2-jackrabbit2-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-jackrabbit2-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2-jackrabbit2 |
| Version | 2.11.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-vfs2-jackrabbit2-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2-jackrabbit2/team.html -->

<!-- page_index: 49 -->

<a id="commons-vfs2-jackrabbit2-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-jackrabbit2-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-jackrabbit2-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---

<a id="commons-vfs2-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2/ci-management.html -->

<!-- page_index: 50 -->

<a id="commons-vfs2-ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-vfs2-ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-vfs2-ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-vfs2-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2/scm.html -->

<!-- page_index: 51 -->

<a id="commons-vfs2-scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="commons-vfs2-scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-vfs.git/commons-vfs2
```

<a id="commons-vfs2-scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-vfs.git
```

<a id="commons-vfs2-scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-vfs2-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2/summary.html -->

<!-- page_index: 52 -->

<a id="commons-vfs2-summary--project-summary"></a>

# Project Summary

<a id="commons-vfs2-summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons VFS |
| Description | Apache Commons VFS is a Virtual File System library. |
| Homepage | [https://commons.apache.org/proper/commons-vfs/](#index) |

<a id="commons-vfs2-summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-vfs2-summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-vfs2 |
| Version | 2.11.0-SNAPSHOT |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-vfs2-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-vfs/commons-vfs2/team.html -->

<!-- page_index: 53 -->

<a id="commons-vfs2-team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-vfs2-team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/1a19c3930f70b17fc4ed15d13dd00393?d=mm&s=60) | adammurdoch | Adam Murdoch | [adammurdoch -at- apache.org](mailto:adammurdoch -at- apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/87cdde4918ff4a330dc7efca24e6d6ee?d=mm&s=60) | jstrachan | James Strachan | [jstrachan -at- apache.org](mailto:jstrachan -at- apache.org) | - | SpiritSoft, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/932f560d750363e6e9e5bac05475507a?d=mm&s=60) | imario | Mario Ivankovits | [imario -at- apache.org](mailto:imario -at- apache.org) | - | OPS EDV Gmbh | - | - | - |
| ![](https://www.gravatar.com/avatar/b3911b7e92ac3dea34f136738746fb45?d=mm&s=60) | rahul | Rahul Akolkar | [rahul -at- apache.org](mailto:rahul -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/8b2639b4e79355fe0d17b43b192cb54c?d=mm&s=60) | jcarman | James Carman | [jcarman -at- apache.org](mailto:jcarman -at- apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://www.gravatar.com/avatar/5eaafbb82222ea121d754224fb34fae3?d=mm&s=60) | rgoers | Ralph Goers | [rgoers -at- apache.org](mailto:rgoers -at- apache.org) | - | Intuit | - | - | - |
| ![](https://www.gravatar.com/avatar/fb955c564722e64613fdc64ac348d9d9?d=mm&s=60) | joehni | Joerg Schaible | [joehni -at- apache.org](mailto:joehni -at- apache.org) | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |
| ![](https://www.gravatar.com/avatar/99dfc628a38b21e414c8e236f20dfe81?d=mm&s=60) | ecki | Bernd Eckenfels | [ecki -at- apache.org](mailto:ecki -at- apache.org) | <https://bernd.eckenfels.net> | - | - | - | +1 |

<a id="commons-vfs2-team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/e11d1a693ab3a16d5045d9a03b6b095a?d=mm&s=60) | Rami Ojares | [rami.ojares -at- elisa.fi](mailto:rami.ojares -at- elisa.fi) |
| ![](https://www.gravatar.com/avatar/4f8b3c0a6490c0e5c1cfa8db28a77344?d=mm&s=60) | Anthony Goubard | [anthony.goubard -at- japplis.com](mailto:anthony.goubard -at- japplis.com) |
| ![](https://www.gravatar.com/avatar/fce99aec5d2acd47c7342076e6347778?d=mm&s=60) | Christopher Ottley | [xknight -at- users.sourceforge.net](mailto:xknight -at- users.sourceforge.net) |
| ![](https://www.gravatar.com/avatar/2c70485de7834f8148e830c5466517be?d=mm&s=60) | Dave Marion | [dlmarion -at- apache.org](mailto:dlmarion -at- apache.org) |
| ![](https://www.gravatar.com/avatar/c995dfb641776958a6ed62068736699d?d=mm&s=60) | Scott Bjerstedt | [jcottbjer -at- gmail.com](mailto:jcottbjer -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/412e6beac89850507f1c4d21169af0cd?d=mm&s=60) | Jose Juan Montiel | [josejuan.montiel -at- gmail.com](mailto:josejuan.montiel -at- gmail.com) |
| ![](https://www.gravatar.com/avatar/851f7e1cb473c4d97f6e8783ca22b292?d=mm&s=60) | Otto Fowler | [otto -at- apache.org](mailto:otto -at- apache.org) |

---
