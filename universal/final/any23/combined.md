# Apache Any23 – Apache Any23 - Getting started

## Navigation

- Apache Any23
  - [Introduction](#index)
  - [Downloads](#download)
    - [Sources](#download--apache_any23_sources)
    - [Core](#download--apache_any23_core)
    - [Basic Crawler](#download--basic_crawler)
    - [HTML Scraper](#download--html_scraper)
    - [Office Scraper](#download--office_scraper)
    - [Service](#download--apache_any23_service)
  - [Install](#install)
- Documentation
  - [Getting Started](#getting-started)
  - [Supported Formats](#supported-formats)
  - [Extractors](#extractors)
  - [Configuration](#configuration)
  - [REST Service](#service)
  - [Any23 Plugins](#any23-plugins)
  - [Developers Guide](#developers)
    - [Build from sources](#build-src)
    - [Data Extraction](#dev-data-extraction)
    - [Data Conversion](#dev-data-conversion)
    - [Validation and Fixing](#dev-validation-fix)
    - [XPath Extractor](#dev-xpath-extractor)
    - [Microformat Extractors](#dev-microformat-extractors)
    - [Microdata Extractor](#dev-microdata-extractor)
    - [CSV Extractor](#dev-csv-extractor)
    - [HowTo Release](#release-howto)
- Project Documentation
  - Project Information
    - [CI Management](#ci-management)
    - [About](#index)
    - [Mailing Lists](#mailing-lists)
    - [Project Modules](#modules)
    - [Source Code Management](#scm)
    - [Summary](#summary)
    - [Team](#team)
- Misc
  - [Acknowledgements](#acknowledgements)
  - [PoweredBy](#poweredby)
- Other pages
  - [Apache Any23 – Apache Any23 - Plugins - HTML Scraper](#plugin-html-scraper)
  - [Apache Any23 – Apache Any23 - Plugins - Office Scraper](#plugin-office-scraper)

## Content

<a id="index"></a>

<!-- source_url: https://any23.apache.org/index.html -->

<!-- page_index: 1 -->

<a id="index--introduction-to-apache-any23"></a>

## Introduction to Apache Any23

<a id="index--library"></a>

### Library

**Anything To Triples (any23)** is a library, a web service and a command line tool that extracts structured data in RDF format from a variety of Web documents. Currently it supports the following input formats:

- [RDF/XML](http://www.w3.org/TR/REC-rdf-syntax/), [Turtle](http://www.w3.org/TeamSubmission/turtle/), [Notation 3](http://www.w3.org/DesignIssues/Notation3)
- [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/) with [RDFa1.1 prefix mechanism](http://www.w3.org/TR/2010/WD-rdfa-core-20100422/#scoping-of-prefix-mappings)
- [Microformats1](http://microformats.org/) and [Microformats2](http://microformats.org/wiki/microformats-2): hAdr, hCard, hCalendar, hEntry, hEvent, hGeo, hItem, hListing, hProduct, hProduct, hRecipie, hResume, hReview, License, Species, XFN, etc
- [JSON-LD](http://json-ld.org/): JSON for Linking Data. a lightweight Linked Data format based on the already successful JSON format and provides a way to help JSON data interoperate at Web-scale.
- [HTML5 Microdata](http://dev.w3.org/html5/md/): (such as [Schema.org](http://schema.org))
- [CSV](http://www.ietf.org/rfc/rfc4180.txt): Comma Separated Values with separator autodetection.
- Vocabularies: Extraction support for [Dublin Core Terms](http://dublincore.org/), [Description of a Career](http://www.w3.org/wiki/DescriptionOfACareerVocabulary), [Description Of A Project](https://github.com/edumbill/doap/wiki), [Friend Of A Friend](http://xmlns.com/foaf/spec/), [GEO Names](http://www.geonames.org/ontology/), [ICAL](http://www.w3.org/2002/12/cal/icaltzd#), [lkif-core](https://github.com/RinkeHoekstra/lkif-core), [Open Graph Protocol](http://ogp.me/), [BBC Programmes Ontology](http://purl.org/ontology/po/), [RDF Review Vocabulary](http://vocab.org/review/terms.html), [schema.org](http://schema.org/), [VCard](http://www.w3.org/2006/vcard/ns), [BBC Wildlife Ontology](http://purl.org/ontology/wo/) and [XHTML](http://www.w3.org/1999/xhtml/vocab/)... and more!
- [YAML](http://www.yaml.org/): human friendly data serialization standard for all programming languages.
- Additionally, as of 2.1 Any23 provides functionality to extract triples using the [Open Information Extraction (Open IE) system](https://github.com/allenai/openie-standalone). The Open IE system runs over sentences and creates extractions that represent relations in text, in the case of Any23, this results in triples.

A detailed description of available extractors is [here](#extractors).

**Apache Any23** is written in Java and licensed under the [Apache License v2.0](https://www.apache.org/licenses/LICENSE-2.0). **Apache Any23** can be used in various ways:

- As a library in Java applications that consume structured data from the Web.
- As a command-line tool for extracting and converting between the supported formats.
- As online service API available at [any23.org](http://any23.org/).

You can **download** the latest release from our [Apache Mirrors](#download).

Previous versions are available from the [Apache Archives site](http://archive.apache.org/dist/any23/).

<a id="index--documentation-content"></a>

### Documentation Content

[Introduction](#index): this page.

[Install](#install): how to install **Apache Any23** library and service.

[Getting Started](#getting-started): start using **Apache Any23** command-line tools.

[Supported Formats](#supported-formats): complete list of **Semantic Web** formats supported by **Apache Any23**.

[Configuration](#configuration): learn how to change default library and service configuration.

[REST Service](#service): discover how to use the **Apache Any23 REST Service**.

[Plugins](#any23-plugins): read how to install and configure the **Apache Any23** plugins.

[Developers](#developers): understand the **Apache Any23** code internals, how to write plugins, fixing rules and customize the code.

<a id="index--community"></a>

### Community

Questions, comments? Get in touch on the [mailing lists](https://any23.apache.org/mail-lists.html)! Bugs, feature requests, patches? Please submit to the [issue tracker](https://issues.apache.org/jira/browse/ANY23). You can access the source through Git, see the [Installation Guide](#install) for details.

---

<a id="download"></a>

<!-- source_url: https://any23.apache.org/download.html -->

<!-- page_index: 2 -->

<a id="download--download-apache-any23"></a>

## Download Apache Any23

Apache Any23 is distributed in several formats for your convenience. Use a source archive if you intend to build Apache Any23 yourself. Otherwise, simply pick a ready-made binary distribution and follow the installation instructions given inside the archives.

You will be prompted for a mirror - if the file is not found on yours, please be patient, as it may take 24 hours to reach all mirrors.

In order to guard against corrupted downloads/installations, it is highly recommended to [verify the signature](https://www.apache.org/dev/release-signing#verifying-signature) of the release bundles against the public [KEYS](https://apache.org/dist/any23/KEYS) used by the Apache Any23 developers.

Apache Any23 is distributed under the [Apache License, version 2.0](https://any23.apache.org/license.html).

<a id="download--apache-any23-maven-artifacts"></a>

### Apache Any23 Maven Artifacts

You can use Any23 as a [Maven](https://maven.apache.org) dependency. See the most recent release artifacts on [Maven Central](https://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.apache.any23%22). For example you could add the `apache-any23-core` artifact to your project POM as follows:

`<dependency>
    <groupId>org.apache.any23</groupId>
    <artifactId>apache-any23-core</artifactId>
    <version>2.7</version>
</dependency>`

Also see [dependency information](https://any23.apache.org/dependency-info.html) for defining Any23 as a dependency in other popular build systems.

<a id="download--apache-any23-sources"></a>

### Apache Any23 Sources

|  | Mirror Download | ASCII Signature | SHA512 Checksum |
| --- | --- | --- | --- |
| Apache Any23 2.7 (Source tar.gz) | [apache-any23-2.7-src.tar.gz](https://www.apache.org/dyn/closer.lua/any23/2.7/apache-any23-2.7-src.tar.gz) | [apache-any23-2.7-src.tar.gz.asc](https://www.apache.org/dist/any23/2.7/apache-any23-2.7-src.tar.gz.asc) | [apache-any23-2.7-src.tar.gz.sha512](https://www.apache.org/dist/any23/2.7/apache-any23-2.7-src.tar.gz.sha512) |
| Apache Any23 2.7 (Source zip) | [apache-any23-2.7-src.zip](https://www.apache.org/dyn/closer.lua/any23/2.7/apache-any23-2.7-src.zip) | [apache-any23-2.7-src.zip.asc](https://www.apache.org/dist/any23/2.7/apache-any23-2.7-src.zip.asc) | [apache-any23-2.7-src.zip.sha512](https://www.apache.org/dist/any23/2.7/apache-any23-2.7-src.zip.sha512) |

<a id="download--apache-any23-command-line-interface"></a>

### Apache Any23 Command Line Interface

|  | Mirror Download | ASCII Signature | SHA512 Checksum |
| --- | --- | --- | --- |
| Apache Any23 2.7 CLI (Binary tar.gz) | [apache-any23-cli-2.7.tar.gz](https://www.apache.org/dyn/closer.lua/any23/2.7/apache-any23-cli-2.7.tar.gz) | [apache-any23-cli-2.7.tar.gz.asc](https://www.apache.org/dist/any23/2.7/apache-any23-cli-2.7.tar.gz.asc) | [apache-any23-cli-2.7.tar.gz.sha512](https://www.apache.org/dist/any23/2.7/apache-any23-cli-2.7.tar.gz.sha512) |
| Apache Any23 2.7 CLI (Binary zip) | [apache-any23-cli-2.7.zip](https://www.apache.org/dyn/closer.lua/any23/2.7/apache-any23-cli-2.7.zip) | [apache-any23-cli-2.7.zip.asc](https://www.apache.org/dist/any23/2.7/apache-any23-cli-2.7.zip.asc) | [apache-any23-cli-2.7.zip.sha512](https://www.apache.org/dist/any23/2.7/apache-any23-cli-2.7.zip.sha512) |

<a id="download--apache-any23-plugins"></a>

## Apache Any23 Plugins

<a id="download--plugins"></a>

### plugins

Various plugins were made available for Any23 releases prior to 2.4. As of 2.4, this is not longer the case. Reasoning behind this relates to the size of the artifcts post introduction of the [Open Information Extraction (Open IE) module](https://github.com/apache/any23-plugins/tree/master/openie). This grew the artifacts to ~1GB which became too large to distribute across the Apache global mirror network.

Any23 plugins can be obtained by [downloading and building from source](https://github.com/apache/any23-plugins).

Plugin artifacts prior to 2.4 can be found in the [Apache Any23 Artifact Archive](http://archive.apache.org/dist/any23/).

<a id="download--apache-any23-service"></a>

## Apache Any23 Service

<a id="download--war-packages"></a>

### WAR packages

Various WAR artifacts were made available for Any23 releases prior to 2.2. Post 2.2, this is not longer the case. Reasoning behind this relates to the size of the WAR artifcts post introduction of the [Open Information Extraction (Open IE) module](https://github.com/apache/any23-plugins/tree/master/openie). This grew the artifacts to ~1GB which became too large to distribute across the Apache global mirror network.

The Any23 WAR artifact can be obtained by [downloading ans building from source](https://github.com/apache/any23-server).

WAR artifacts prior to 2.2 can be found in the [Apache Any23 Artifact Archive](http://archive.apache.org/dist/any23/).

For users merely wanting to see what the Any23 Service looks like and does, visit .

<a id="download--verify-releases"></a>

## Verify Releases

###

It is essential that you verify the integrity of the downloaded files using the PGP, and/or SHA signatures. published with every Any23 release. Please read [Verifying Apache HTTP Server Releases](http://httpd.apache.org/dev/verification.html) for more information on why you should verify our releases. We strongly recommend you verify your downloads with at least PGP Guidance for doing so is provided below.

<a id="download--pgp-signatures"></a>

### PGP Signatures

The PGP signatures can be verified using PGP or GPG. First download the [KEYS](https://www.apache.org/dist/any23/KEYS) as well as the asc signature file for the relevant distribution. **N.B.** Make sure you get these files from the main distribution directory, rather than from a mirror. Then verify the signatures using the following example

`$ gpg --import KEYS`
`$ gpg --verify apache-any23-2.7-src.tar.gz.asc apache-any23-2.7-src.tar.gz`

The files in the most recent release are signed by Lewis John McGibbney (CODE SIGNING KEY) lewismc@apache.org 48BAEBF6

<a id="download--sha512-signatures"></a>

### SHA512 Signatures

Alternatively, you can verify the SHA512 signatures on the files. A unix program called md5 or md5sum is included in many unix distributions. Use the following example

`$ sha512sum apache-any23-2.7-src.tar.gz`

... output should match the string in **apache-any23-2.7-src.tar.gz.sha512**

---

<a id="install"></a>

<!-- source_url: https://any23.apache.org/install.html -->

<!-- page_index: 3 -->

<a id="install--apache-any23-installation-guide"></a>

## Apache Any23 Installation Guide

This page describes how to install **Apache Any23**.

<a id="install--download-a-stable-distribution"></a>

### Download a Stable Distribution

Most users probably don't need to have day to day access to the source code as it changes. For these users we provide distribution packages via our  [downloads page](#download). Download either the **".zip"** or **".tar.gz"** file and extract the archive.

<a id="install--installing-the-core"></a>

## Installing the Core

<a id="install--windows-2000-xp"></a>

### Windows 2000/XP

1. Unzip the distribution archive, i.e. `apache-any23-2.8-SNAPSHOT-bin.zip` to the directory you wish to install Apache Any23 2.8-SNAPSHOT. These instructions assume you chose `C:\Program Files\Apache Software Foundation`. The subdirectory `apache-any23-2.8-SNAPSHOT` will be created from the archive.
2. Add the `ANY23_HOME` environment variable by opening up the system properties (WinKey + Pause), selecting the "Advanced" tab, and the "Environment Variables" button, then adding the `ANY23_HOME` variable in the user variables with the value `C:\Program Files\Apache Software Foundation\apache-any23-2.8-SNAPSHOT`.
3. In the same dialog, add the `ANY23` environment variable in the user variables with the value `%ANY23_HOME%\bin`.
4. Optional: In the same dialog, add the `EXTRA_JVM_ARGUMENTS` environment variable in the user variables to specify JVM properties, e.g. the value `-Xms256m -Xmx512m`. This environment variable can be used to supply extra options. By default, it is set to: `-Xms500m -Xmx500m -XX:PermSize=128m -XX:-UseGCOverheadLimit`.
5. In the same dialog, update/create the Path environment variable in the user variables and prepend the value `%ANY23%` to add Apache Any23 available in the command line.
6. In the same dialog, make sure that `JAVA_HOME` exists in your user variables or in the system variables and it is set to the location of your JDK, e.g. `C:\Program Files\Java\jdk1.5.0_02` and that `%JAVA_HOME%\bin` is in your Path environment variable.
7. Open a new command prompt (Winkey + R then type cmd) and run `any23 --version` to verify that it is correctly installed.

<a id="install--unix-based-operating-systems-linux-solaris-and-mac-os-x"></a>

### Unix-based Operating Systems (Linux, Solaris and Mac OS X)

1. Extract the distribution archive, i.e. `apache-any23-2.8-SNAPSHOT-bin.tar.gz` to the directory you wish to install Apache Any23 2.8-SNAPSHOT. These instructions assume you chose `/usr/local/apache-any23`. The subdirectory `apache-any23-2.8-SNAPSHOT` will be created from the archive.
2. In a command terminal, add the `ANY23_HOME` environment variable, e.g. `export ANY23_HOME=/usr/local/apache-any23/apache-any23-2.8-SNAPSHOT`.
3. Add the `ANY23` environment variable, e.g. `export ANY23=$ANY23_HOME/bin`.
4. Optional: Add the `EXTRA_JVM_ARGUMENTS` environment variable to specify JVM properties, e.g. `export EXTRA_JVM_ARGUMENTS="-Xms256m -Xmx512m"`. This environment variable can be used to supply extra options.
5. Add M2 environment variable to your path, e.g. `export PATH=$ANY23:$PATH`.
6. Make sure that `JAVA_HOME` is set to the location of your JDK, e.g. `export JAVA_HOME=/usr/java/jdk1.5.0_02` and that `$JAVA_HOME/bin` is in your PATH environment variable.
7. Run `any23 --version` to verify that it is correctly installed.

<a id="install--installing-a-plugin"></a>

## Installing a plugin

<a id="install--windows-2000-xp-2"></a>

### Windows 2000/XP

1. Unzip the distribution archive, i.e. `apache-$plugin.name-bin.zip` The subdirectory `apache-$plugin.name` will be created from the archive.
2. Copy the jar files under `C:\Documents and Settings<username>\.any23\plugins`

<a id="install--unix-based-operating-systems-linux-solaris-and-mac-os-x-2"></a>

### Unix-based Operating Systems (Linux, Solaris and Mac OS X)

1. Extract the distribution archive, i.e. `apache-$plugin.name-bin.tar.gz`. The subdirectory `apache-$plugin.name` will be created from the archive.
2. Copy the jar files under `~/.any23/plugins`

<a id="install--installing-the-service"></a>

## Installing the service

<a id="install--installing-the-standalone-server"></a>

### Installing the standalone server

<a id="install--windows-2000-xp-3"></a>

#### Windows 2000/XP

1. Unzip the distribution archive, i.e. `apache-any23-service-2.8-SNAPSHOT-bin-server-embedded.zip` to the directory you wish to install Apache Any23 2.8-SNAPSHOT. These instructions assume you chose `C:\Program Files\Apache Software Foundation`. The subdirectory `apache-2.8-SNAPSHOT-server-embedded` will be created from the archive.
2. Add the `ANY23_HOME` environment variable by opening up the system properties (WinKey + Pause), selecting the "Advanced" tab, and the "Environment Variables" button, then adding the `ANY23_HOME` variable in the user variables with the value `C:\Program Files\Apache Software Foundation\apache-2.8-SNAPSHOT`.
3. In the same dialog, add the `ANY23` environment variable in the user variables with the value `%ANY23_HOME%\bin`.
4. Optional: In the same dialog, add the `EXTRA_JVM_ARGUMENTS` environment variable in the user variables to specify JVM properties, e.g. the value `-Xms256m -Xmx512m`. This environment variable can be used to supply extra options. By default, it is set to: `-Xms500m -Xmx500m -XX:PermSize=128m -XX:-UseGCOverheadLimit`.
5. In the same dialog, update/create the Path environment variable in the user variables and prepend the value `%ANY23%` to add Apache Any23 available in the command line.
6. In the same dialog, make sure that `JAVA_HOME` exists in your user variables or in the system variables and it is set to the location of your JDK, e.g. `C:\Program Files\Java\jdk1.5.0_02` and that `%JAVA_HOME%\bin` is in your Path environment variable.
7. Open a new command prompt (Winkey + R then type cmd) and run `any23server` to launch the service.

<a id="install--unix-based-operating-systems-linux-solaris-and-mac-os-x-3"></a>

#### Unix-based Operating Systems (Linux, Solaris and Mac OS X)

1. Extract the distribution archive, i.e. `apache-2.8-SNAPSHOT-bin-server-embedded.tar.gz` to the directory you wish to install Apache Any23 2.8-SNAPSHOT. These instructions assume you chose `/usr/local/apache-any23`. The subdirectory `apache-2.8-SNAPSHOT-server-embedded` will be created from the archive.
2. In a command terminal, add the `ANY23_HOME` environment variable, e.g. `export ANY23_HOME=/usr/local/apache-any23/apache-2.8-SNAPSHOT-server-embedded`.
3. Add the `ANY23` environment variable, e.g. `export ANY23=$ANY23_HOME/bin`.
4. Optional: Add the `EXTRA_JVM_ARGUMENTS` environment variable to specify JVM properties, e.g. `export EXTRA_JVM_ARGUMENTS="-Xms256m -Xmx512m"`. This environment variable can be used to supply extra options.
5. Add `ANY23` environment variable to your path, e.g. `export PATH=$ANY23:$PATH`.
6. Make sure that `JAVA_HOME` is set to the location of your JDK, e.g. `export JAVA_HOME=/usr/java/jdk1.5.0_02` and that `$JAVA_HOME/bin` is in your PATH environment variable.
7. Run `any23server` to launch the service.

---

<a id="getting-started"></a>

<!-- source_url: https://any23.apache.org/getting-started.html -->

<!-- page_index: 4 -->

<a id="getting-started--getting-started-with-apache-any23"></a>

## Getting started with **Apache Any23**

**Apache Any23** can be used:

- via CLI (command line interface) from your preferred shell environment;
- as a RESTful Webservice;
- as a library.

<a id="getting-started--apache-any23-modules"></a>

### **Apache Any23** Modules

**Apache Any23** is composed of the following modules:

- `api/` The base API definitions e.g. The Any23 API.
- `core/` The core library containing all extractor functionality.
- `cli/` A command line interface enabling easy invocation of Any23 tools.
- `csvutils/` Utility code for CSV extractions.
- `encoding/` Characterset detection and encoding.
- `mime/` Media-type detection.
- `service/` The REST service.
- `plugins/` The core additional plugins.
- `openie/` Additional extractor logic for the [Open Information Extraction (Open IE) system](https://github.com/allenai/openie-standalone).

<a id="getting-started--use-the-apache-any23-cli"></a>

### Use the **Apache Any23** CLI

The command-line tools support is provided by the **cli** module.

Once **Apache Any23** has been correctly [installed](#install), if you want to use it as a command line tool, use the shell script within the `cli/target/appassembler/bin/` directory. These are provided both for Unix (Linux/OSX) and Windows.

The `any23` script provides analysis, documentation, testing and debugging utilities.

Simply running *./any23* without options will show the *usage* options.

```
$ cli/target/appassembler/bin/any23

A command must be specified.
Usage: any23 [options] [command] [command options]
  Options:
    -h, --help
       Display help information.
       Default: false
        --plugins-dir
       The Any23 plugins directory.
       Default: /Users/lmcgibbn/.any23/plugins
    -X, --verbose
       Produce execution verbose output.
       Default: false
    -v, --version
       Display version information.
       Default: false
  Commands:
    extractor      Utility for obtaining documentation about metadata extractors.
      Usage: extractor [options] Extractor name
        Options:
          -a, --all
             shows a report about all available extractors
             Default: false
          -i, --input
             shows example input for the given extractor
             Default: false
          -l, --list
             shows the names of all available extractors
             Default: false
          -o, --outut
             shows example output for the given extractor
             Default: false

    microdata      Commandline Tool for extracting Microdata from file/HTTP source.
      Usage: microdata [options] Input document URL, {http://path/to/resource.html|file:/path/to/localFile.html}

    mimes      MIME Type Detector Tool.
      Usage: mimes [options] Input document URL, {http://path/to/resource.html|file:///path/to/local.file|inline:// some inline content}

    verify      Utility for plugin management verification.
      Usage: verify [options] plugins-dir

    rover      Any23 Command Line Tool.
      Usage: rover [options] input IRIs {<url>|<file>}+
        Options:
          -d, --defaultns
             Override the default namespace used to produce statements.
          -e, --extractors
             a comma-separated list of extractors, e.g. rdf-xml,rdf-turtle
             Default: []
          -f, --format
             the output format
             Default: json
          -l, --log
             Produce log within a file.
          -n, --nesting
             Disable production of nesting triples.
             Default: false
          -t, --notrivial
             Filter trivial statements (e.g. CSS related ones).
             Default: false
          -o, --output
             Specify Output file (defaults to standard output)
             Default: java.io.PrintStream@5204062d
          -p, --pedantic
             Validate and fixes HTML content detecting commons issues.
             Default: false
          -s, --stats
             Print out extraction statistics.
             Default: false

    vocab      Prints out the RDF Schema of the vocabularies used by Any23.
      Usage: vocab [options]
        Options:
          -f, --format
             Vocabulary output format
             Default: N-Quads (mimeTypes=application/n-quads, text/x-nquads, text/nquads; ext=nq)
```

The `any23` script detects a list of available utilities within the **core** and **plugins** classpath and allows to activate them.

The *any23-core* CLI tools are:

- `extractor`: a utility for obtaining useful information about extractors.
- `microdata`: commandline parser to extract specific Microdata content from a web page (local or remote) and produce a JSON output compliant with the Microdata specification (<http://www.w3.org/TR/microdata/>).
- `mimes`: detects the MIME Type for any HTTP / file / direct input resource.
- `verify`: a utility for verifying *Apache Any23* plugins.
- `rover`: the RDF extraction tool.
- `vocab`: allows to dump all the **RDFSchema** vocabularies declared within Apache Any23.

<a id="getting-started--the-rover-tool"></a>

#### The Rover tool

Rover is the main extraction tool. It allows to extract metadata from local and remote (HTTP) resources, specify a custom list of extractors, specify the desired output format and other flags to suppress noise and generate advanced reports.

Extract metadata from an **HTML** page:

```
cli$ any23 rover http://yourdomain/yourfile
```

Extract metadata from a **local** resource:

```
cli$ any23 rover myfoaf.rdf
```

Specify the output format, use the option **"-f"** or **"--format"**: (Default output format is **TURTLE**).

```
cli$ any23 rover -f quad myfoaf.rdf
```

Filtering trivial statements

By default, **Apache Any23** will extract *HTML/head* meta information, such as links to *CSS stylesheets* or meta information like the author or the software used to create the *html*. Hence, if the user is only interested in the structured content from the *HTML/body* tag we offer a filter functionality, activated by the **"-t"** command line argument.

```
core$ any23 rover -t -f quad myfoaf.rdf
```

<a id="getting-started--the-extractordocumentation-tool"></a>

#### The ExtractorDocumentation tool

The ExtractorDocumentation returns human readable information about the registered extractors.

List all the available extractors:

```
cli$ any23 extractor --list
                      csv [org.apache.any23.extractor.csv.CSVExtractorFactory] [text/csv;q=0.1]
     html-embedded-jsonld [org.apache.any23.extractor.html.EmbeddedJSONLDExtractorFactory] [text/html;q=0.02, application/xhtml+xml;q=0.02]
           html-head-icbm [org.apache.any23.extractor.html.ICBMExtractorFactory] [text/html;q=0.01, application/xhtml+xml;q=0.01]
          html-head-links [org.apache.any23.extractor.html.HeadLinkExtractorFactory] [text/html;q=0.05, application/xhtml+xml;q=0.05]
           html-head-meta [org.apache.any23.extractor.html.HTMLMetaExtractorFactory] [text/html;q=0.02, application/xhtml+xml;q=0.02]
          html-head-title [org.apache.any23.extractor.html.TitleExtractorFactory] [text/html;q=0.02, application/xhtml+xml;q=0.02]
              html-mf-adr [org.apache.any23.extractor.html.AdrExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
              html-mf-geo [org.apache.any23.extractor.html.GeoExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
        html-mf-hcalendar [org.apache.any23.extractor.html.HCalendarExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
            html-mf-hcard [org.apache.any23.extractor.html.HCardExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
         html-mf-hlisting [org.apache.any23.extractor.html.HListingExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
          html-mf-hrecipe [org.apache.any23.extractor.html.HRecipeExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
          html-mf-hresume [org.apache.any23.extractor.html.HResumeExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
          html-mf-hreview [org.apache.any23.extractor.html.HReviewExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
html-mf-hreview-aggregate [org.apache.any23.extractor.html.HReviewAggregateExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
          html-mf-license [org.apache.any23.extractor.html.LicenseExtractorFactory] [text/html;q=0.01, application/xhtml+xml;q=0.01]
          html-mf-species [org.apache.any23.extractor.html.SpeciesExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
              html-mf-xfn [org.apache.any23.extractor.html.XFNExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
           html-microdata [org.apache.any23.extractor.microdata.MicrodataExtractorFactory] [text/html;q=0.1, application/xhtml+xml;q=0.1]
              html-rdfa11 [org.apache.any23.extractor.rdfa.RDFa11ExtractorFactory] [application/xhtml+xml;q=0.3, application/html;q=0.3, text/html;q=0.3]
               html-xpath [org.apache.any23.extractor.xpath.XPathExtractorFactory] [text/html;q=0.02, application/xhtml+xml;q=0.02]
                     ical [org.apache.any23.extractor.calendar.ICalExtractorFactory] [text/calendar]
                     jcal [org.apache.any23.extractor.calendar.JCalExtractorFactory] [application/calendar+json]
           owl-functional [org.apache.any23.extractor.rdf.FunctionalSyntaxExtractorFactory] [text/owl-functional]
           owl-manchester [org.apache.any23.extractor.rdf.ManchesterSyntaxExtractorFactory] [text/owl-manchester]
               rdf-jsonld [org.apache.any23.extractor.rdf.JSONLDExtractorFactory] [application/ld+json;q=0.1]
                   rdf-nq [org.apache.any23.extractor.rdf.NQuadsExtractorFactory] [application/n-quads, text/x-nquads;q=0.1, text/rdf+nq;q=0.1, text/nq;q=0.1, text/nquads;q=0.1, text/n-quads;q=0.1]
                   rdf-nt [org.apache.any23.extractor.rdf.NTriplesExtractorFactory] [application/n-triples;q=0.1, text/nt;q=0.1, text/ntriples;q=0.1, text/plain;q=0.1]
                 rdf-trix [org.apache.any23.extractor.rdf.TriXExtractorFactory] [application/trix]
               rdf-turtle [org.apache.any23.extractor.rdf.TurtleExtractorFactory] [text/turtle, text/rdf+n3, text/n3, application/n3, application/x-turtle, application/turtle]
                  rdf-xml [org.apache.any23.extractor.rdf.RDFXMLExtractorFactory] [application/rdf+xml, text/rdf, text/rdf+xml, application/rdf]
                     xcal [org.apache.any23.extractor.calendar.XCalExtractorFactory] [application/calendar+xml]
                     yaml [org.apache.any23.extractor.yaml.YAMLExtractorFactory] [text/x-yaml;q=0.5]
```

<a id="getting-started--the-microdataparser-tool"></a>

#### The MicrodataParser tool

The *MicrodataParser* tool allows to apply the only MicrodataExtractor on a specific input source and returns the extracted data in the JSON format declared in the Microdata specification section [JSON](http://www.w3.org/TR/microdata/#json).

```
cli$ any23 microdata http://path/to/resource.html
```

<a id="getting-started--the-vocabprinter-tool"></a>

#### The VocabPrinter tool

The VocabPrinter Tool prints out the RDFSchema declared by all the **Apache Any23** declared vocabularies.

Just launch the command below to see all the managed vocabularies.

```
cli$ any23 vocab
```

*NOTE*: **This tool is still in beta version.**

<a id="getting-started--the-mimedetector-tool"></a>

#### The MimeDetector tool

The MimeDetector Tool extracts the **MIME Type** for a given source (http:// file:// inline://).

Examples:

```
cli$ any23 mimes http://www.michelemostarda.com/foaf.rdf
application/rdf+xml
```

```
cli$ any23 mimes file://../src/test/resources/application/trix/test1.trx
application/trix
```

```
cli$ any23 mimes 'inline://<http://s> <http://p> <http://o> .'
text/n3
```

<a id="getting-started--the-pluginverifier-tool"></a>

#### The PluginVerifier tool

The PluginVerifier tool allows checking installed plugin in the specified input directory

Just launch the command below to sanity-check the input plugins directory

```
cli$ any23 verify [/path/to/plugins/dir]
```

<a id="getting-started--apache-any23-cli-plugins"></a>

### **Apache Any23** CLI *Plugins*

The **Apache Any23** ToolRunner CLI (*bin/any23*) supports the auto detection of Tool plugins within the classpath. For further details see [Plugins](#any23-plugins) section.

The default **any23** CLI plugins are enlisted below.

<a id="getting-started--crawler-plugin"></a>

#### Crawler Plugin

crawler-tool The *Crawler Plugin* provides basic site crawling and metadata extraction capabilities.

```
cli$ any23 -h
[...]
    crawler      Any23 Crawler Command Line Tool.
      Usage: crawler [options] input IRIs {<url>|<file>}+
  Options:
          -d, --defaultns          Override the default namespace used to
                                   produce statements.
          -e, --extractors         a comma-separated list of extractors, e.g.
                                   rdf-xml,rdf-turtle
                                   Default: []
          -f, --format             the output format
                                   Default: turtle
          -l, --log                Produce log within a file.
          -md, --maxdepth          Max allowed crawler depth.
                                   Default: 2147483647
          -mp, --maxpages          Max number of pages before interrupting
                                   crawl.
                                   Default: 2147483647
          -n, --nesting            Disable production of nesting triples.
                                   Default: false
          -t, --notrivial          Filter trivial statements (e.g. CSS related
                                   ones).
                                   Default: false
          -nc, --numcrawlers       Sets the number of crawlers.
                                   Default: 10
          -o, --output             Specify Output file (defaults to standard
                                   output)
                                   Default: java.io.PrintStream@2911a3a4
          -pf, --pagefilter        Regex used to filter out page URLs during
                                   crawling.
                                   Default: .*(\.(css|js|bmp|gif|jpe?g|png|tiff?|mid|mp2|mp3|mp4|wav|wma|avi|mov|mpeg|ram|m4v|wmv|rm|smil|pdf|swf|zip|rar|gz|xml|txt))$
          -p, --pedantic           Validate and fixes HTML content detecting
                                   commons issues.
                                   Default: false
          -pd, --politenessdelay   Politeness delay in milliseconds.
                                   Default: 2147483647
          -s, --stats              Print out extraction statistics.
                                   Default: false
          -sf, --storagefolder     Folder used to store crawler temporary data.
                                   Default: /var/folders/zz/9vvv_lbn1cs8dpwz859nmq080000gn/T/crawler-metadata-9ff4c650-10c2-41a1-9d99-ebeb3e7d21ce
```

A usage example:

```
cli$ any23 crawler -s -f ntriples http://www.repubblica.it 1> out.nt 2> repubblica.log
```

<a id="getting-started--use-apache-any23-as-a-restful-web-service"></a>

### Use **Apache Any23** as a RESTful Web Service

**Apache Any23** provides a Web Service that can be used to extract *RDF* from Web documents. **Apache Any23** services can be accessed through a [RESTful API](#service).

Running the server

The server command line tool is defined within the **service** module. Run the `any23server` script

```
service$ ./bin/any23server
```

from the command line in order to start up the server, then go to  to access the web interface. A live demo version of such service is running at . You can also start the server from Java by running the [Apache Any23 Servlet](https://any23.apache.org/apidocs/org/apache/any23/servlet/Servlet.html) class. Maven can be used to create a WAR file for deployment into an existing servlet container such as [Apache Tomcat](http://tomcat.apache.org/).

<a id="getting-started--use-apache-any23-as-a-library"></a>

### Use **Apache Any23** as a Library

See our [Developers guide](#developers) for more details.

---

<a id="supported-formats"></a>

<!-- source_url: https://any23.apache.org/supported-formats.html -->

<!-- page_index: 5 -->

<a id="supported-formats--supported-formats-in-apache-any23"></a>

## Supported Formats in Apache Any23

**Apache Any23** supports all the main standard formats introduced by the **Semantic Web** community.

<a id="supported-formats--input-formats"></a>

### **Input Formats**

The following list shows the accepted input formats and for each one the support level.

- **(X)HTML** with **RDFa 1.0**, **RDFa 1.1**, **Microdata** and **Microformats**. **Apache Any23** fully supports the [(X)HTML5](http://www.w3.org/TR/html5/) input format and in particular provides a set of extractors for processing embedded [RDFa 1.0](http://www.w3.org/TR/rdfa-syntax/), [RDFa 1.1](http://www.w3.org/TR/rdfa-core/), [Microformats](http://microformats.org/) and [Microdata](http://www.w3.org/TR/microdata/).
- **Turtle** **Apache Any23** fully supports the [Turtle](http://www.w3.org/TeamSubmission/turtle/) specification.
- **N-Triples** **Apache Any23** fully supports the [N-Triples](http://www.w3.org/TR/rdf-testcases/#ntriples) specification.
- **N-Quads** **Apache Any23** Version 1.1 supports the 2012 [N-Quads](https://web.archive.org/web/20150322024714/http://sw.deri.org/2008/07/n-quads/) specification (last accessed: 2016-06-17). **Apache Any23** Version 1.2 will support the current [N-Quads](https://www.w3.org/TR/n-quads/) specification.
- **RDF/XML** **Apache Any23** fully supports the [RDF/XML](http://www.w3.org/TR/rdf-syntax-grammar/) specification.
- **CSV** **Apache Any23** allows you to represent header-provided [CSV](http://www.ietf.org/rfc/rfc4180.txt) files with RDF using a specific [algorithm](#dev-csv-extractor).
- **YAML** **Apache Any23** support [YAML](http://yaml.org/spec/1.2/spec.html) a human friendly data serialization standard for all programming languages.

<a id="supported-formats--output-formats"></a>

### **Output Formats**

The supported output formats are enlisted below.

- **Turtle** **Apache Any23** is able to produce output in [Turtle](http://www.w3.org/TeamSubmission/turtle/).
- **N-Triples** **Apache Any23** is able to produce output in [N-Triples](http://www.w3.org/TR/rdf-testcases/#ntriples).
- **N-Quads** **Apache Any23** is able to produce output in the 2012 [N-Quads](https://web.archive.org/web/20150322024714/http://sw.deri.org/2008/07/n-quads/) format (last accessed: 2016-06-17). **Apache Any23** Version 1.2 will support the current [N-Quads](https://www.w3.org/TR/n-quads/) specification.
- **RDF/XML** **Apache Any23** is able to produce output in [RDF/XML](http://www.w3.org/TR/rdf-syntax-grammar/).
- **JSON-LD** **Apache Any23** is able to produce output in [JSON-LD](http://www.w3.org/TR/json-ld/).
- **JSON Statements** **Apache Any23** is able to produce output in [JSON](http://www.json.org/) . See the specific [format](#supported-formats--json-statements).
- **XML Report** **Apache Any23** is able to produce a detailed report of the latest document extraction if required. See further details [here](#service--report-format).

<a id="supported-formats--json-statements-format"></a>

### JSON Statements Format

json-statements

Apache Any23 is able to produce JSON output following the format described below.

Given the following example statements (expressed in N-Quads format):

```
_:bn1          <http://pred/1> <http://value/1>         <http://graph/1> .
<http://sub/2> <http://pred/2> "language literal"@en    <http://graph/2> .
<http://sub/3> <http://pred/3> "123"^^<http://datatype> <http://graph/3> .
```

these will be represented as:

```
{
    "quads" : [
        [
            {
                "type" : "bnode",
                "value" : "bn1"
            },
            "http://pred/1",
            {
                "type" : "uri",
                "value" : "http://value/1"
            },
            "http://graph/1"
        ],
        [
            {
                "type" : "uri",
                "value" : "http://sub/2"
            },
            "http://pred/2",
            {
                "type" : "literal",
                "value" : "language literal",
                "lang" : "en",
                "datatype" : null
            },
            "http://graph/2"
        ],
        [
            {
                "type" : "uri",
                "value" : "http://sub/3"
            },
            "http://pred/3",
            {
                "type" : "literal",
                "value" : "123",
                "lang" : null,
                "datatype" : "http://datatype"
            },
            "http://graph/3"
        ]
    ]
}
```

The **JSON object** structure is described by the following **BNF** rules, where quotes are omitted to improve readability:

```
<json-response> ::= { "quads" : <statements> }
<statements>    ::= [ <statement>+ ]
<statement>     ::= [ <subject> , <predicate> , <object> , <graph> ]
<subject>       ::= { "type" : <subject-type> , "value" : <value> }
<predicate>     ::= <uri>
<object>        ::= { "type" : <object-type> , "value" : <value> , "lang" : <lang> , "datatype" : <datatype> }
<graph>         ::= <uri> | null
<subject-type>  ::= "uri" | "bnode"
<object-type>   ::= "uri" | "bnode"| "literal"
<value>         ::= String
<lang>          ::= String | null
<datatype>      ::= <uri>  | null
<uri>           ::= String
```

---

<a id="extractors"></a>

<!-- source_url: https://any23.apache.org/extractors.html -->

<!-- page_index: 6 -->

<a id="extractors--apache-any23-extractors"></a>

## Apache Any23 Extractors

This page enlists all the Apache Any23 Extractors (see source code [package](https://any23.apache.org/apidocs/org/apache/any23/extractor/package-summary.html)).

<a id="extractors--microformat-extractors"></a>

### Microformat Extractors

The following extractors refer to the [Microformats specifications](http://microformats.org/).

Specific details about \*Microformats\* extractors can be found [here](#dev-microformat-extractors). In particular the \*Microformats Nesting\* representation policy is described [here](#dev-microformat-extractors--microformat-nesting).

[AdrExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/AdrExtractor.html)

[GeoExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/GeoExtractor.html)

[HCalendar](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HCalendarExtractor.html)

[HCard](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HCardExtractor.html)

[HListing](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HListingExtractor.html)

[HResume](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HResumeExtractor.html)

[HReview](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HReviewExtractor.html)

[SpeciesExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/SpeciesExtractor.html)

[LicenseExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/LicenseExtractor.html)

[XFNExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/XFNExtractor.html)

[HRecipeExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HRecipeExtractor.html)

<a id="extractors--rdfa-1.0-1.1"></a>

### RDFa [1.0 , 1.1]

The following extractors refer to the [RDFa 1.0](http://www.w3.org/TR/rdfa-syntax/) and [RDFa 1.1](http://www.w3.org/TR/rdfa-core/) specifications.

[RDFaExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/rdfa/RDFaExtractor.html)

<a id="extractors--microdata"></a>

### Microdata

The following extractors refer to the [Microdata specifications](http://dev.w3.org/html5/md/).

[MicrodataExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/microdata/MicrodataExtractor.html)

<a id="extractors--rdf"></a>

### RDF

[RDFXMLExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/rdf/RDFXMLExtractor.html)

[NQuadsExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/rdf/NQuadsExtractor.html)

[TurtleExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/rdf/TurtleExtractor.html)

[NTriplesExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/rdf/NTriplesExtractor.html)

<a id="extractors--metadata-extractors"></a>

### Metadata Extractors

[TitleExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/TitleExtractor.html)

[HTMLMetaExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HTMLMetaExtractor.html)

[HeadLinkExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HeadLinkExtractor.html)

[ICBMExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/ICBMExtractor.html)

[TurtleHTMLExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/TurtleHTMLExtractor.html)

<a id="extractors--content-extractors"></a>

### Content Extractors

[XPath Extractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/xpath/XPathExtractor.html) (**Experimental**)

[CSV Extractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/csv/CSVExtractor.html) (See the extraction [algorithm](#dev-csv-extractor).)

<a id="extractors--get-more-documentation"></a>

## Get more documentation

It is possible to generate the list of all the available extractors invoking the following command:

```
<any23-core>/bin$ any23tools ExtractorDocumentation -list
```

---

<a id="configuration"></a>

<!-- source_url: https://any23.apache.org/configuration.html -->

<!-- page_index: 7 -->

<a id="configuration--configuration"></a>

## Configuration

<a id="configuration--configure-the-core-module"></a>

### Configure the Core Module

The core module contains the main library code and the command-line implementation.

The main library configuration parameters are managed by the  [Configuration](https://any23.apache.org/apidocs/org/apache/any23/configuration/DefaultConfiguration.html) class. The default values are declared within the  [default-configuration.properties](https://github.com/apache/any23/blob/master/api/src/main/resources/default-configuration.properties) file. The following sections explain how to override the default configuration.

<a id="configuration--override-default-configuration-from-command-line"></a>

#### Override Default Configuration from Command-line

The default configuration can be overriden via command-line by passing to the **java** command system properties with the same name of the ones declared in configuration.

For example to override the **HTTP Max Client Connections** parameter it is sufficient to add the following option to the **java** command-line invocation:

```
-Dany23.http.client.max.connections=10
```

any23 and any23server scripts accept the variable **ANY23\_OPTS** to specify custom options. It is possible to customize the **HTTP Max Client Connections** for the **any23** script simply using:

```
cli/target/appassembler/bin/$ ANY23_OPTS="-Dany23.http.client.max.connections=10" any23 http://path/to/resource
```

<a id="configuration--override-default-configuration-programmatically"></a>

#### Override Default Configuration Programmatically

The  [Configuration](https://any23.apache.org/apidocs/org/apache/any23/configuration/Configuration.html) properties can be accessed in read-only mode just retrieving the configuration **singleton** instance. Such instance is *immutable*:

```
final Configuration immutableConf = DefaultConfiguration.singleton();
final String propertyValue = immutableConf.getProperty("propertyName", "default value");
...
```

To obtain a *modifiable*  [Configuration](https://any23.apache.org/apidocs/org/apache/any23/configuration/Configuration.html) instead it is possible to use the **copy()** method. One of the **Apache Any23** constructors accepts a **Configuration** object that allows to customize the behavior of the **Apache Any23** instance for its entire life-cycle.

```
final ModifiableConfiguration modifiableConf = DefaultConfiguration.copy();
final String oldPropertyValue = modifiableConf.setProperty("propertyName", "new property value");
final Apache Any23 any23 = new Apache Any23(modifiableConf, "extractor1", ...);
...
```

<a id="configuration--use-of-extractionparameters"></a>

### Use of ExtractionParameters

It is possible to customize the behavior of a single data extraction by providing an  [ExtractionParameters](https://any23.apache.org/apidocs/org/apache/any23/extractor/ExtractionParameters.html) instance to one the *Apache Any23#extract()* methods accepting it. **ExtractionParameters** allows to customize any *property* and *flag* other then the **specific extraction options**. If no custom parameters are specified the default configuration values are used.

```
final Any23 any23 = ...
final TripleHandler tripleHandler = ...
final ExtractionParameters extractionParameters = ExtractionParameters.getDefault();
extractionParameters.setFlag("any23.microdata.strict", true);
any23.extract(extractionParameters, "http://path/to/doc", tripleHandler);
```

<a id="configuration--apache-any23-core-module-default-configuration"></a>

### Apache Any23 Core Module Default Configuration

| Property Name | Default Property Value | Description |
| --- | --- | --- |
| any23.core.version | *current any23 core version* | String declaring the Apache Any23 Core module version. |
| any23.http.user.agent.default | Apache Any23-CLI | User Agent Name used for HTTP requests. |
| any23.http.client.timeout | 10000 (10 secs) | Timeout in milliseconds for a HTTP request. |
| any23.http.client.max.connections | 5 | Max number of concurrent HTTP connections allowed by the internal Apache Any23 HTTP client. |
| any23.rdfa.extractor.xslt | rdfa.xslt | XSLT Stylesheet to be used to perform HTML to RDF extraction of RDFa. |
| any23.extraction.metadata.timesize | off (possible values: on/off) | Activates/deactivates the generation of time and size metadata triples. |
| any23.extraction.metadata.nesting | on (possible values: on/off) | Activates/deactivates the generation of nesting triples for Microformat entities. |
| any23.extraction.metadata.domain.per.entity | on (possible values: on/off) | Activates/deactivates the generation of domain triple per entity. |
| any23.extraction.rdfa.programmatic | on (possible values: on/off) | Switches between the programmatic RDFa 1.1 Extractor and the RDFa 1.0 XSLT base one. |
| any23.extraction.context.iri | ?(means current document IRI) | Default value for extraction content IRI. |
| any23.plugin.dirs | ./plugins | Directory containing Apache Any23 plugins. |
| any23.microdata.strict | on (possible values: on/off) | Activates/deactivates the microdata strict validation. |
| any23.microdata.ns.default | http://schema.org/ | Microdata default namespace. |
| any23.extraction.head.meta | on (possible values: on/off) | Activates/deactivates the HTMLMetaExtractor. |
| any23.extraction.csv.field | , | CSVExtractor field separator. |
| any23.extraction.csv.comment | # | CSVExtractor line comment marker. |

---

<a id="service"></a>

<!-- source_url: https://any23.apache.org/service.html -->

<!-- page_index: 8 -->

<a id="service--apache-any23-rest-service"></a>

## Apache Any23 REST Service

*Apache Any23* provides REST Service module *any23-service* able to provide useful processing methods.

<a id="service--compact-api"></a>

### Compact API

HTTP GET requests can be made to IRIs of the shape:

```
http://<any23-service-host>/<output-format>/<input-uri>
```

Where *input-uri* is the input HTTP resource to be processed and *output-format* is the desired output format for the extracted RDF data.

Example requests:

```
http://any23.org/best/twitter.com/cygri
http://any23.org/rdfxml/http://data.gov
http://any23.org/ttl/http://www.w3.org/People/Berners-Lee/card
http://any23.org/?uri=http://dbpedia.org/resource/Berlin
http://any23.org/?format=nt&uri=http://dbpedia.org/resource/Berlin
```

Supported input and output formats are described  [here](#supported-formats).

Form-style GET API

HTTP GET requests can be made to the IRI http://any23.org/ with the following query parameters:

```
uri         IRI of an input document
format      Desired output format; defaults to best
```

<a id="service--direct-post-api"></a>

### Direct POST API

HTTP POSTing a document body to http://any23.org/format will convert the document to the specified output format. The media type of the input has to be specified in the Content-Type HTTP header. Depending on the servlet container, a Content-Length header specifying the length of the input document in bytes might also be required. Typical media types for supported input formats are:

```
Input format        Media type
-------------------------------
HTML        text/html
RDF/XML     application/rdf+xml
Turtle      text/turtle
N-Triples   text/plain
N-Quads     text/plain
```

Example POST request:

```
POST /rdfxml HTTP/1.0
Host: any23.org
Content-Type: text/turtle
Content-Length: 174

@prefix foaf: <http://xmlns.com/foaf/0.1/> .

[] a foaf:Person;
    foaf:name "John X. Foobar";
    foaf:mbox_sha1sum "cef817456278b70cee8e5a1611539ef9d928810e";
    .
```

<a id="service--form-style-post-api"></a>

### Form-style POST API

A document body can also be converted by HTTP POSTing form data to http://any23.org/. The Content-Type HTTP header must be set to *application/x-www-form-urlencoded*. The following parameters are supported:

type

Media type of the input, see the table above. If not present, auto-detection will be attempted.

body

Document body to be converted.

format

Desired output format; defaults to **best**.

validation

The validation level to be applied, supported values: **none** (default), **validate** and **validate-fix**.

<a id="service--output-formats"></a>

### Output Formats

Supported input and output formats are described  [here](#supported-formats).

<a id="service--error-reporting"></a>

### Error reporting

Processing errors are indicated via HTTP status codes and brief text/plain error messages. The following status codes can be returned:

```
Code                        Reason
-------------------------------------------------------------------------------------------------------------
200 OK                      Success.
400 Bad                     Request     Missing or malformed input parameter.
404 Not                     Found       Malformed request IRI.
406 Not                     Acceptable  None of the media types specified in the Accept header are supported.
415 Unsupported Media Type      Document body with unsupported media type was POSTed.
501 Not Implemented             Extraction from input was successful, but yielded zero triples.
502 Bad Gateway             Input document from a remote server could not be fetched or parsed.
```

<a id="service--xml-report-format"></a>

### XML Report Format

report-format

The *Apache Any23 Service* can optionally return an XML report and attempt error fix if the flags *fix* and *report* are activated ( *fix=on&report=on* ). The following URL shows how to use these flags.

```
http://any23.org/any23-service/any23/?format=best&uri=http%3A%2F%2Fpath%2Fto%2Fresource&validation=none&report=on
```

The *fix* functionality is described [here](#dev-validation-fix).

A report format example is listed below. In particular ath path *response/extractors/extractor* it is possible to find the list of all extractors activated during the page processing. The section *response/report/message* contains an eventual error message while the *response/report/error* section the error stack trace if available.

The result of validation is contained within the *response/report/validationReport* node. Within that node there is the list of the activated rules, the issues detected and the errors generated.

```
<?xml version="1.0" encoding="UTF-8" ?>
<response>
  <!-- List of activated extractors. -->
  <extractors>
    <extractor><!-- Extractor name. --></extractor>
    <!-- ... -->
  </extractors>
  <report>
    <message></message>
    <error></error>
    <!-- Validation specific report, contains all errors and issues detected within the document. -->
    <validationReport>
      <!-- List of errors found while validating the document. -->
      <errors>
      </errors>
      <!-- List of issues found while validating the document. -->
      <issues>
      </issues>
      <!-- List of rules activated to solve the detected issues. -->
      <ruleActivations>
      </ruleActivations>
    </validationReport>
  </report>
  <data>
  <![CDATA[
  -- Actual Data in the format specified as output. --
  ]]>
  </data>
</response>
```

---

<a id="any23-plugins"></a>

<!-- source_url: https://any23.apache.org/any23-plugins.html -->

<!-- page_index: 9 -->

<a id="any23-plugins--apache-any23-plugins"></a>

## Apache Any23 Plugins

<a id="any23-plugins--introduction"></a>

### Introduction

This section describes the *Apache Any23* plugins support.

*Apache Any23* comes with a set of predefined plugins. Such plugins are located under the *$ANY23\_HOME*/**plugins** dir.

A plugin is a standard *Maven3* module containing any implementation of

- [Extractor](https://any23.apache.org/apidocs/index.html?org%2Fapache%2Fany23%2Fextractor%2FExtractor.html=)
- [Tool](https://any23.apache.org/apidocs/org/apache/any23/cli/Tool.html)

<a id="any23-plugins--how-to-register-a-plugin"></a>

### How to Register a Plugin

A plugin can be added to the *Apache Any23 CLI* interface by:

- adding its *JAR* to the *Apache Any23* *JVM classpath*;
- adding its *JAR* to the CLASSPATH\_PREFIX environment variable as:


```
export CLASSPATH_PREFIX=../../../plugins/basic-crawler/target/any23-basic-crawler-VERSION.jar
```

- adding its *JAR* to the *$HOME/.any23/plugins* directory.

  A plugin can be added to the *Apache Any23 library API* by first creating a static instance of [Any23PluginManager](https://any23.apache.org/apidocs/org/apache/any23/plugin/Any23PluginManager.html)#getInstance(). Once this is done there is a variety of options to configure and register a plugins, etc. An example of dynamic plugin loading can be seen via the way that the OpenIE toggling is implemented within the Any23 Webservice e.g.


```
if (openie) {
    Any23PluginManager pManager = Any23PluginManager.getInstance();
    //Dynamically adding Jar's to the Classpath via the following logic
    //is absolutely dependant on the 'apache-any23-openie' directory being
    //present within the webapp /lib directory. This is specified within 
    //the maven-dependency-plugin.
    File webappClasspath = new File(getClass().getClassLoader().getResource("").getPath());
    File openIEJarPath = new File(webappClasspath.getParentFile().getPath() + "/lib/apache-any23-openie");
    boolean loadedJars = pManager.loadJARDir(openIEJarPath);
    if (loadedJars) {
        ExtractorRegistry r = ExtractorRegistryImpl.getInstance();
        try {
            pManager.getExtractors().forEachRemaining(r::register);
        } catch (IOException e) {
            LOG.error("Error during dynamic classloading of JARs from OpenIE runtime directory {}", openIEJarPath.toString(), e);
        }
        LOG.info("Successful dynamic classloading of JARs from OpenIE runtime directory {}", openIEJarPath.toString());
    }
}
```

  Any implementation of *ExtractorPlugin* will automatically registered to the [ExtractorRegistry](https://any23.apache.org/apidocs/org/apache/any23/extractor/ExtractorRegistry.html).

  Any detected implementation of *Tool* will be listed by the *ToolRunner* command-line tool in *any23-root/***cli/bin/any23** .

<a id="any23-plugins--how-to-build-a-plugin"></a>

### How to Build a Plugin

*Apache Any23* takes care to *test* and *package* plugins when distributed from its reactor *POM*. It is aways possible to rebuild a plugin using the command:

```
<plugin-dir>$ mvn clean assembly:assembly
```

<a id="any23-plugins--how-to-write-an-extractor-plugin"></a>

### How to Write an Extractor Plugin

An *Extractor Plugin* is a class:

- implementing one of the [Extractor](https://any23.apache.org/apidocs/index.html?org%2Fapache%2Fany23%2Fextractor%2FExtractor.html=) subinterfaces;
- packaged under **org.apache.any23.plugin** .

  An example of plugin is defined below.


```
@Author(name="Michele Mostarda (mostarda@fbk.eu)") public class HTMLScraperExtractor implements Extractor.ContentExtractor {
private static final Logger logger = LoggerFactory.getLogger(HTMLScraperPlugin.class);
@Override public void run(ExtractionParameters extractionParameters,ExtractionContext extractionContext,InputStream inputStream,ExtractionResult extractionResult ) throws IOException, ExtractionException {...}
@Override public ExtractorDescription getDescription() {return HTMLScraperExtractorFactory.getDescriptionInstance();}
@Override public void setStopAtFirstError(boolean b) {// Ignored.}
}
```

<a id="any23-plugins--how-to-write-a-tool-plugin"></a>

### How to Write a Tool Plugin

A *Tool Plugin* is a Java class that:

- implementing the [Tool](https://any23.apache.org/apidocs/org/apache/any23/cli/Tool.html) interface;
- CLI parameters are extracted by annotating the class members with [JCommander](http://jcommander.org/) annotations.
- have to be found using the [ServiceLoader](https://docs.oracle.com/javase/8/docs/api/java/util/ServiceLoader.html) (we usually plug the Kohsuke's [generator](http://weblogs.java.net/blog/kohsuke/archive/2009/03/my_project_of_t.html))

  An example of plugin is defined below.


```
@Parameters(commandNames = { "myexec" }, commandDescription = "Prints out XXX used by Any23.") public class MyExecutableTool implements Tool {
@Parameter(names = { "-u", "--urls" }, description = "URLs to process") private List<URL> pairs;
public void run() throws Exception;
}
}
```

So when executing `any23>>, the <<<myexec` will be available in the commands list.

<a id="any23-plugins--available-extractor-plugins"></a>

### Available Extractor Plugins

- HTML Scraper Plugin

  The *HTMLScraperPlugin* is able to scrape plain text content from any HTML page and transform it into statement literals.

  This plugin is documented [here](#plugin-html-scraper).
- Office Scraper Plugins

  The *Office Scraper Plugins* allow to extract semantic content from several *Microsoft Office* document formats.

  These plugins are documented [here](#plugin-office-scraper).
- OpenIE Extractor Plugin

  As of 2.1 Any23 provides functionality to extract triples using the [Open Information Extraction (Open IE) system](https://github.com/allenai/openie-standalone). The Open IE system runs over input sentences and creates extractions that represent relations in text, in the case of Any23, this results in triples. Se the above example on how to register a plugin to see how the OpenIE Extractor plugin is currently used within the Any23 Service.

<a id="any23-plugins--available-cli-tool-plugins"></a>

### Available CLI Tool Plugins

- Crawler CLI Tool

  The [Crawler CLI Tool](https://any23.apache.org/apidocs/org/apache/any23/cli/Crawler.html) is an extension of the [Rover CLI Tool](https://any23.apache.org/apidocs/org/apache/any23/cli/Rover.html) to add site crawling basic capabilities. More information about the *CLI* can be found at [Getting Started - Crawler Tool](#getting-started--crawler-tool) section.

---

<a id="developers"></a>

<!-- source_url: https://any23.apache.org/developers.html -->

<!-- page_index: 10 -->

<a id="developers--architectural-overview"></a>

## Architectural Overview

![](assets/images/any23-overall_31db2057b6fc15e9.png)

The informal architectural diagram above shows the **Any23** logical modules, the main data flow and the code packages implementing such modules.

The first module, **Data Fetching**, is responsible for retrieving raw data from the Web, its implementation package is **org.apache.any23.source**. The data collected by *Data Fetching* is analyzed by the **MIMEtype Detection** module, implemented in package **org.apache.any23**. Such module will determine the data encoding and the content *MIME* type. The identification of the MIME type is used to select a list of activable *Extractors* for the subsequent metadata extraction.

The next phase is performed by the **Content Validation and Patching** module (**org.apache.any23.validator**), and it is required because the most part of data exposed on the Web is affected by minor issues which compromise the correct working of some *Extractors*. To overcome such problems **Any23** introduced a mechanism to detect issues and in most cases to fix them. The detection and fixing is performed using an extensible collection of **Rules**. Currently the Validation and Patching is applied only on *DOM* based documents (*HTML*).

The **Metadata Extraction** module, implemented within the **org.apache.any23.extraction** package, applies all the *Extractors* activated by the analysis phase and generates an RDF statements stream together with an issue report. The statements produced by the *Extractor*s can be filtered to remove spurious, repeated or unwanted triples using the **Metadata Filtering** module (**org.apache.any23.filter**).

The last metadata extraction phase consists in the conversion of the filtered statements in an RDF representation format. This can be done by using one of the available RDF writers provided by the **Serialization** module (**org.apache.any23.writer**).

The other modules represented at the bottom of the diagram add auxiliary functionalities over the core application. The **Plugin Management** module (**org.apache.ay23.plugin**) is responsible for the extension of the platform through the runtime detection and registration of additional components included within the classpath. The Plugin Manager is currently able to detect and register new Extractors, Writers and CLI tools. It is foreseen the plugin support implementation for all the modules marked as (P).

The **CLI Tool** module (org.apache.any23.cli) allows to run all the available CLI tools through a unified interface.

The **Service** module (org.apache.any23.service) implements a REST service to use Any23 as a Web service implementing a *REST* interface.

<a id="developers--developers-guide"></a>

## Developers Guide

This section introduces some **Apache Any23** programming fundamentals.

<a id="developers--data-extraction"></a>

### [Data Extraction](#dev-data-extraction)

Explains how to extract RDF data from HTTP resources with **Apache Any23**.

<a id="developers--data-conversion"></a>

### [Data Conversion](#dev-data-conversion)

Shows how to perform RDF data conversion with **Apache Any23**.

<a id="developers--validation-and-fixing"></a>

### [Validation and Fixing](#dev-validation-fix)

Demonstrates how to define validation and correction rules for HTML content with **Apache Any23**.

<a id="developers--xpath-extractor"></a>

### [XPath Extractor](#dev-xpath-extractor)

Explains how to write custom scraping rules for extracting RDF data from any HTML content with **Apache Any23**.

<a id="developers--microformat-extractors"></a>

### [Microformat Extractors](#dev-microformat-extractors)

Explains how to write new Microformat extractors with **Apache Any23** and also report interesting notes on microformat nesting representation.

<a id="developers--microdata-extractor"></a>

### [Microdata Extractor](#dev-microdata-extractor)

Explains how it works the Microdata Extractor embedded in **Apache Any23**.

<a id="developers--csv-extractor"></a>

### [CSV Extractor](#dev-csv-extractor)

Explains how it works the CSV Extractor embedded in **Apache Any23**.

---

<a id="build-src"></a>

<!-- source_url: https://any23.apache.org/build-src.html -->

<!-- page_index: 11 -->

<a id="build-src--build-apache-any23-from-sources"></a>

## Build Apache Any23 from sources

This page describes how to build **Apache Any23**.

<a id="build-src--access-a-snapshot-version"></a>

### Access a Snapshot Version

For the latest snapshot please checkout the code from the public Git repository and build the library. Checkout the code from Github:

```
$ git clone https://github.com/apache/any23.git
```

<a id="build-src--build-apache-any23"></a>

### Build **Apache Any23**

The following instructions describe how to build the library with [Maven 3.x.y+](http://maven.apache.org/). For specific information about Maven see:  Go to the any23 folder:

```
$ cd any23/
```

and execute the following command:

```
any23$ mvn clean install
```

This will install the **Apache Any23** artifact and its dependencies in your local M2 repository.

<a id="build-src--generate-documentation"></a>

### Generate Documentation

To generate the project site locally execute the following command from the any23 dir:

```
any23$ MAVEN_OPTS='-Xmx1024m' mvn clean site
```

You can speed up the site generation process specifying the offline option ( -o ), but it works only if all the involved plugin dependencies has been already downloaded in the local M2 repository:

```
any23$ MAVEN_OPTS='-Xmx1024m' mvn -o clean site
```

If you're interested in generating the Javadoc enriched with navigable UML graphs, you can activate the umlgraphdoc profile. This profile relies on [Graphviz](http://www.graphviz.org/) that must be installed in your system.

```
any23$ MAVEN_OPTS='-Xmx256m' mvn -P umlgraphdoc clean site
```

---

<a id="dev-data-extraction"></a>

<!-- source_url: https://any23.apache.org/dev-data-extraction.html -->

<!-- page_index: 12 -->

<a id="dev-data-extraction--data-extraction"></a>

## Data Extraction

```
/*1*/ Any23 runner = new Any23();
/*2*/ runner.setHTTPUserAgent("test-user-agent");
/*3*/ HTTPClient httpClient = runner.getHTTPClient();
/*4*/ DocumentSource source = new HTTPDocumentSource(
         httpClient,
         "http://www.rentalinrome.com/semanticloft/semanticloft.htm"
      );
/*5*/ ByteArrayOutputStream out = new ByteArrayOutputStream();
/*6*/ TripleHandler handler = new NTriplesWriter(out);
      try {
/*7*/     runner.extract(source, handler);
      } finally {
/*8*/     handler.close();
      }
/*9*/ String n3 = out.toString("UTF-8");
```

This example demonstrates the data extraction, that is the main purpose of **Apache Any23** library. At **line 1** we define the **Apache Any23** facade instance. As described before, the constructor allows to enforce the usage of specific extractors.

The **line 2** defines the *HTTP User Agent*, used to identify the client during *HTTP* data collection. At **line 3** we use the runner to create an instance of [HTTPClient](https://any23.apache.org/apidocs/org/apache/any23/http/HTTPClient.html), used by [HTTPDocumentSource](https://any23.apache.org/apidocs/org/apache/any23/source/HTTPDocumentSource.html) for *HTTP* content fetching.

The **line 4** instantiates an [HTTPDocumentSource](https://any23.apache.org/apidocs/org/apache/any23/source/HTTPDocumentSource.html) instance, specifying the [HTTPClient](https://any23.apache.org/apidocs/org/apache/any23/http/HTTPClient.html) and the URL addressing the content to be processed.

At **line 5** we define a buffered output stream used to store data produced by the [TripleHandler](https://any23.apache.org/apidocs/org/apache/any23/writer/TripleHandler.html) defined at **line 6**.

The extraction method at **line 7** will run the metadata extraction. The produced metadata will be written within the passed [TripleHandler](https://any23.apache.org/apidocs/org/apache/any23/writer/TripleHandler.html) instance.

The [TripleHandler](https://any23.apache.org/apidocs/org/apache/any23/writer/TripleHandler.html) needs to be explicitly closed, this is done safely in a **finally** block at **line 8**.

The expected output is *UTF-8* encoded at **line 9** and is:

```
<http://www.rentalinrome.com/semanticloft/semanticloft.htm> <http://purl.org/dc/terms/title>
"Semantic Loft (beta) - Trastevere apartments | Rental in Rome - rentalinrome.com" .

<http://www.rentalinrome.com/semanticloft/semanticloft.htm#semanticloft>
<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>
<http://purl.org/goodrelations/v1#Offering> .

<http://www.rentalinrome.com>
<http://purl.org/goodrelations/v1#offers>
<http://www.rentalinrome.com/semanticloft/semanticloft.htm#semanticloft> .

<http://www.rentalinrome.com/semanticloft/semanticloft.htm#semanticloft>
<http://www.w3.org/2000/01/rdf-schema#seeAlso>
<http://rentalinrome.com/semanticloft/semanticloft.htm> .

<http://www.rentalinrome.com/semanticloft/semanticloft.htm#semanticloft>
<http://purl.org/goodrelations/v1#hasBusinessFunction>
<http://purl.org/goodrelations/v1#ProvideService> .

<http://www.rentalinrome.com/semanticloft/semanticloft.htm#semanticloft>
<http://www.w3.org/2006/vcard/ns#adr>
_:node14r93a8dex1 .

[The complete output is omitted for brevity.]
```

<a id="dev-data-extraction--filter-out-accidental-triples"></a>

## Filter Out Accidental Triples

To remove accidental triples **Apache Any23** provides a set of useful filters, located within the **org.apache.any23.filter** package.

The filter [IgnoreTitlesOfEmptyDocuments](https://any23.apache.org/apidocs/org/apache/any23/filter/IgnoreTitlesOfEmptyDocuments.html) removes triples generated by the [TitleExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/TitleExtractor.html) whether the document is empty.

The filter [IgnoreAccidentalRDFa](https://any23.apache.org/apidocs/org/apache/any23/filter/IgnoreAccidentalRDFa.html) removes accidental **CSS** related triples.

```
RDFWriter rdfWriter = ...
TripleHandler rdfWriterHandler = RDFWriterTripleHandler(rdfWriter);
TripleHandler tripleHandler = new ReportingTripleHandler(
        new IgnoreAccidentalRDFa(
                new IgnoreTitlesOfEmptyDocuments(rdfWriterHandler),
                true // if true the CSS triples will be removed in any case.
        )
);
DocumentSource documentSource = ...
any23.extract(documentSource, rdfWriterHandler);
```

---

<a id="dev-data-conversion"></a>

<!-- source_url: https://any23.apache.org/dev-data-conversion.html -->

<!-- page_index: 13 -->

<a id="dev-data-conversion--data-conversion"></a>

## Data Conversion

```
/*1*/ Any23 runner = new Any23();
/*2*/ final String content = "@prefix foo: <http://example.org/ns#> .   " +
                             "@prefix : <http://other.example.org/ns#> ." +
                             "foo:bar foo: : .                          " +
                             ":bar : foo:bar .                           ";
//    The second argument of StringDocumentSource() must be a valid IRI.
/*3*/ DocumentSource source = new StringDocumentSource(content, "http://host.com/service");
/*4*/ ByteArrayOutputStream out = new ByteArrayOutputStream();
/*5*/ TripleHandler handler = new NTriplesWriter(out);
      try {
/*6*/     runner.extract(source, handler);
      } finally {
/*7*/     handler.close();
      }
/*8*/ String nt = out.toString("UTF-8");
```

This example aims to demonstrate how to use **Apache Any23** to perform RDF data conversion. In this code we provide some input data expressed as **Turtle** and convert it in **NTriples** format.

At **line 1** we define a new instance of the **Apache Any23** facade, that provides all the methods useful for the transformation. The facade constructor accepts a list of extractor names, if specified the extraction will be done only over this list, otherwise the data *MIME Type* will detected and will be applied all the compatible extractors declared within the [ExtractorRegistry](https://any23.apache.org/apidocs/org/apache/any23/extractor/ExtractorRegistry.html).

The **line 2** defines the input string containing some [Turtle](http://www.w3.org/TeamSubmission/turtle/) data.

At **line 3** we instantiate a [StringDocumentSource](https://any23.apache.org/apidocs/org/apache/any23/source/StringDocumentSource.html), specifying a content and a the source *IRI*. The *IRI* should be the source of the content data, and must be valid. Besides the [StringDocumentSource](https://any23.apache.org/apidocs/org/apache/any23/source/StringDocumentSource.html), you can also provide input from other sources, such as *HTTP* requests and local files. See the classes in the sources [package](https://any23.apache.org/apidocs/org/apache/any23/source/package-summary.html).

The **line 4** defines a buffered output stream that will be used to store the data produced by the writer declared at **line 5**.

A writer stores the extracted triples in some destination. We use an [NTriplesWriter](https://any23.apache.org/apidocs/org/apache/any23/writer/NTriplesWriter.html) here that writes into a **ByteArrayOutputStream**. The main **RDF** formats writers are available and it is possible also to store the triples directly into an **RDF4J** repository to query them via **SPARQL**. See [RepositoryWriter](https://any23.apache.org/apidocs/org/apache/any23/writer/RepositoryWriter.html) and the writer [package](https://any23.apache.org/apidocs/org/apache/any23/writer/package-summary.html).

The extractor method invoked at **line 6** performs the metadata extraction. This method accepts as first argument a [DocumentSource](https://any23.apache.org/apidocs/org/apache/any23/source/DocumentSource.html) and as second argument a [TripleHandler](https://any23.apache.org/apidocs/org/apache/any23/writer/TripleHandler.html), that will receive the sequence parsing events generated by the applied extractors. The extract method defines also another signature where it is possible to specify a charset encoding for the input data. If **null**, the charset will be auto detected.

The [TripleHandler](https://any23.apache.org/apidocs/org/apache/any23/writer/TripleHandler.html) needs to be explicitly closed, this is done safely in a **finally** block at **line 7**.

The expected output is *UTF-8* encoded at **line 8**:

```
<http://example.org/ns#bar> <http://example.org/ns#> <http://other.example.org/ns#> .
<http://other.example.org/ns#bar> <http://other.example.org/ns#> <http://example.org/ns#bar> .
```

---

<a id="dev-validation-fix"></a>

<!-- source_url: https://any23.apache.org/dev-validation-fix.html -->

<!-- page_index: 14 -->

<a id="dev-validation-fix--validation-and-fixing"></a>

## Validation and Fixing

Introduction

**Apache Any23** Is able to detect **ill-formed HTML DOM content** and apply fixes over it.

This section will show how to write RDFa validation Rule and Fix for RDFa.

It's widely recognized that RDFa is subjected to a plethora of different and [common mistakes](http://rdfa.info/wiki/Common-publishing-mistakes). These errors may lead to a failures during RDF extraction process from HTML pages but since they are, typically, syntax errors they could be easily detected and fixed with some heuristics.

This pages describes the **Apache Any23** rule-based approach, that allows it to detect, fix and correctly extract RDF from those ill-formed RDFa in XHTML pages.

More specifically, **Apache Any23** allows you to write a [Rule](https://any23.apache.org/apidocs/org/apache/any23/validator/Rule.html) able to detect the errors, a [Fix](https://any23.apache.org/apidocs/org/apache/any23/validator/Fix.html) containing the logic to fix the problem and a [Validator](https://any23.apache.org/apidocs/org/apache/any23/validator/Validator.html) which acts as a register of rules and fixes. The Validator calls all the registered rules and when one of them is applied it calls the associated Fix.

The following code snipped shows how to programmatically detect and fix a very common data error with **Apache Any23**.

Fix Missing Prefix Mappings Declaration

Sometimes, web authors forget to declare prefix mappings. For example, you can't just use something like dcterms:title without first declaring the dcterms prefix mapping. If a prefix mapping isn't declared, the RDFa parser won't understand the prefix when it is used in your document. This may lead **Apache Any23** to don't extract such embedded RDF triples.

This:

```
<div>
  The title of this document is <span property="dcterms:title">Why RDFa is Awesome</span>.
</div>
```

Should be:

```
<div xmlns:dcterms="http://purl.org/dc/terms/">
  The title of this document is <span property="dcterms:title">Why RDFa is Awesome</span>.
</div>
```

With the **Apache Any23** [Validator](https://any23.apache.org/apidocs/org/apache/any23/validator/package-summary.html) classes it's possible to solve this problem simply implementing the [Rule](https://any23.apache.org/apidocs/org/apache/any23/validator/Rule.html) interface as described below:

```
public class MissingOpenGraphNamespaceRule implements Rule {
public String getHRName() {return "missing-opengraph-namespace-rule";}
public boolean applyOn(DOMDocument document, RuleContext context, ValidationReport validationReport) {List<Node> metas = document.getNodes("/HTML/HEAD/META"); boolean foundPrecondition = false; for (Node meta : metas) {Node propertyNode = meta.getAttributes().getNamedItem("property"); if( propertyNode != null && propertyNode.getTextContent().indexOf("og:") == 0) {foundPrecondition = true; break;}} if (foundPrecondition) {Node htmlNode = document.getNode("/HTML"); if (htmlNode.getAttributes().getNamedItem("xmlns:og") == null) {validationReport.reportIssue(ValidationReport.IssueLevel.error,"Missing OpenGraph namespace declaration.",htmlNode ); return true;}} return false;}}
```

The [MissingOpenGraphNamespaceRule](https://any23.apache.org/apidocs/org/apache/any23/validator/rule/MissingOpenGraphNamespaceRule.html) inspects the DOM structure of the HTML page and if it finds some META tags with some RDFa property (of the OpenGraph Protocol vocabulary, in this case) it looks for the declaration of that name space. If there is no declaration it return **true**, that means that an error has been detected within the document.

Writing a fix for the Rule depicted above it's quite simple:

```
public class OpenGraphNamespaceFix implements Fix {
public static final String OPENGRAPH_PROTOCOL_NS = "http://opengraphprotocol.org/schema/";
public String getHRName() {return "opengraph-namespace-fix";}
public void execute(Rule rule, RuleContext context, DOMDocument document) {document.addAttribute("/HTML", "xmlns:og", OPENGRAPH_PROTOCOL_NS);}
}
```

At this point it's enough to register the Rule and the relative Fix to the Validator:

```
validator.addRule(MissingOpenGraphNamespaceRule.class, OpenGraphNamespaceFix.class);
```

When the Rule precondition is matched, then the Fix is triggered modifying the DOM structure.

---

<a id="dev-xpath-extractor"></a>

<!-- source_url: https://any23.apache.org/dev-xpath-extractor.html -->

<!-- page_index: 15 -->

<a id="dev-xpath-extractor--xpath-extractor"></a>

## XPath Extractor

The XPath extractor is a specific extractor meant to scrape data from pages not containing RDF information. Such extractor is based on a set of configurable extraction rules activated by a regular expression over the page URL. When an extraction rule is activated all the variables it defines are evaluated and then a NQuads template is expanded for generating statements. See [Javadoc](https://any23.apache.org/apidocs/org/apache/any23/extractor/xpath/package-summary.html).

---

<a id="dev-microformat-extractors"></a>

<!-- source_url: https://any23.apache.org/dev-microformat-extractors.html -->

<!-- page_index: 16 -->

<a id="dev-microformat-extractors--microformat-extractors"></a>

## Microformat Extractors

This section describes some extractions corner-cases and their relative RDF representations. Main aim of this section is to describe how some specific cases are processed with **Apache Any23** showing the correspondences between the extracted RDF triples.

<a id="dev-microformat-extractors--microformat-nesting-nesting-different-microformats"></a>

## microformat-nesting \* Nesting different Microformats

![](TODO: add picture about microformat nesting structure.)

This section describes how **Apache Any23** represents, with RDF, the content of an HTML fragments containing different nested Microformats. **Apache Any23** performs the extraction executing different extractors for every supported Microformat on a input HTML page. There are two different possibilities to write extractors able to produce a set of RDF triples that coherently represents this nesting.

More specifically:

- Embedding explicitly the logic within the [Microformats Extractors](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/package-summary.html)
- Using the default **Apache Any23** nesting feature.

In the first case, the logic for representing the nested values, is directly embedded in the upper-level Extractor. For example, the following HTML fragment shows an hCard that contains an hAddress Microformat.

```
<span class="vcard">
  <span class="fn">L'Amourita Pizza</span>
   Located at
  <span class="adr">
    <span class="street-address">123 Main St</span>,
    <span class="locality">Albequerque</span>,
    <span class="region">NM</span>.
  </span>
  <a href="http://pizza.example.com" class="url">http://pizza.example.com</a>
</span>
```

Since, as shown below, the [HCardExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HCardExtractor.html) contains the code to handle nested hAddress,

```
foundSomething |= addSubMicroformat("adr", card, VCARD.adr);
...
private boolean addSubMicroformat(String className, Resource resource, IRI property) {List<Node> nodes = fragment.findAllByClassName(className); if (nodes.isEmpty()) return false; for (Node node : nodes) {addBNodeProperty(getDescription().getExtractorName(),node,resource, property, getBlankNodeFor(node) );} return true;}
```

it explicitly produces the triples claiming the native nesting relationship:

```
<rdf:Description rdf:nodeID="nodee2296b803cbf5c7953614ce9998c4083">
  <vcard:url rdf:resource="http://pizza.example.com"/>
  <vcard:adr rdf:nodeID="nodea8badeafb65268ab3269455dd5377a5e"/>
  <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#VCard"/>

  <rdf:Description rdf:nodeID="nodea8badeafb65268ab3269455dd5377a5e">
  <rdf:type rdf:resource="http://www.w3.org/2006/vcard/ns#Address"/>
  <vcard:street-address>123 Main St</vcard:street-address>
  <vcard:locality>Albequerque</vcard:locality>
  <vcard:region>NM</vcard:region>
</rdf:Description>
```

It is higly recommended to decorate the extractors who natively handle the nesting relatioship using the [@Includes](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/annotations/Includes.html) annotation. This annotation, if present, avoid the production of *nesting\_original* and *nesting\_structured* RDF statements.

The following example shows how the [@Includes](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/annotations/Includes.html) annotation could be used to claim the fact that [HCardExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/HCardExtractor.html) natively embedds the [AdrExtractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/html/AdrExtractor.html).

```
@Includes( extractors = AdrExtractor.class )
public class HCardExtractor extends EntityBasedMicroformatExtractor {

    // code omitted for brevity

}
```

Instead, the second manner is to leave to **Apache Any23** the responsibility of identifying nested Microformats and produce a set of descriptive RDF triples. More specifically, the following HTML fragment, provided as a reference example on the [Google Webmaster tools blog](http://www.google.com/support/webmasters/bin/answer.py?answer=146862), shows a vEvent Microformat with a nested vCard.

```
<p class="schedule vevent">
  <span class="summary">
    <span style="font-weight:bold; color: #3E4876;">
       This event is organized by
      <span class="vcard">
        <a class="url fn" href="http://tantek.com/">Tantek Celik</a>
        <span class="org">Technorati</span>
      </span>
    </span>
    <a href="/cs/web2005/view/e_spkr/1852">Tantek Celik</a>
  </span>
</p>
```

Due to the fact that the **Apache Any23** provided extractors don't explicitly foresee the possibility of nesting such two Microformats, it automatically identifies the nesting relationship and represents it with the following triples:

```
<rdf:Description rdf:nodeID="node755b2b367973b6854ec68c77bec9b3">
  <nesting_original xmlns="http://vocab.sindice.net/" rdf:resource="http://www.w3.org/2002/12/cal/icaltzd#summary"/>
  <nesting_structured xmlns="http://vocab.sindice.net/" rdf:nodeID="node985d8f2b9afb02eeddf2e72b5eeb74"/>
</rdf:Description>

<rdf:Description rdf:nodeID="node150ldsavbx29">
  <nesting xmlns="http://vocab.sindice.net/" rdf:nodeID="node755b2b367973b6854ec68c77bec9b3"/>
</rdf:Description>
```

That informally means that the vEvent Microformat has a nested hCard through the property http://www.w3.org/2002/12/cal/icaltzd#summary providing for them two blank nodes.

---

<a id="dev-microdata-extractor"></a>

<!-- source_url: https://any23.apache.org/dev-microdata-extractor.html -->

<!-- page_index: 17 -->

<a id="dev-microdata-extractor--microdata-extractor"></a>

## Microdata Extractor

The **Microdata** extractor is compliant with the **W3C** draft specification at <http://www.w3.org/TR/microdata/>.

Such extractor produces an RDF representation of the detected Microdata within an **XHTML5** document, following the algorithm at section <http://www.w3.org/TR/microdata/#rdf>.

It is possible to retrieve the **JSON** representation of the same Microdata as defined at section <http://www.w3.org/TR/microdata/#json> by using the Microdata commandline tool, see [Getting Started - Apache Any23 Tools](#getting-started--any23tools_script).

---

<a id="dev-csv-extractor"></a>

<!-- source_url: https://any23.apache.org/dev-csv-extractor.html -->

<!-- page_index: 18 -->

<a id="dev-csv-extractor--csv-extractor-algorithm"></a>

## CSV Extractor Algorithm

The [CSV Extractor](https://any23.apache.org/apidocs/org/apache/any23/extractor/csv/CSVExtractor.html) produces an RDF representation of a CSV file compliant with the [RFC 4180](http://www.ietf.org/rfc/rfc4180.txt) and that foresees an header. Such extractor relies on the presence of an header to use the named fields as RDF properties. Field delimiter could be automatically guessed or specified via [Apache Any23 Configuration](#configuration).

Given a document with URL *url*, **Apache Any23** uses the following algorithm to extract RDF:

- It tries to guess the fields delimiter and to detect the header
- for each field *name*:
  - if *name* is a valid IRI keep it as an IRI since could be derefenceable.
  - if *name* is not a valid IRI, the associated RDF Property IRI *propUri* will be in the form of: *url* concatenated *name*
  - add label statement: *propUri* rdfs:label *name*
  - add column index statement: *propUri* <http://vocab.sindice.net/csv/rowPosition> *index*
- for each *row*:
  - add RDFS type statement: <url/row/*index*> rdfs:type <http://vocab.sindice.net/csv/Row>, where *index* is the column index number.
  - for each *cell* value:
    - write statement, <url/row/<index>> *propUri* *cell* where: *cell* could be an IRI if the cell value is an IRI, or a typed literal according the value of the CSV actual value *cell*.
- add RDF statements claiming number of rows and columns.

For example, given this trivial CSV with an header and just two rows:

```
first name; last name; http://xmlns.com/foaf/0.1/knows; age
Davide; Palmisano; http://michelemostarda.com; 30; value should not appear
Michele; Mostarda; http://g1o.net;
```

the following RDF (serialized in RDF/XML) is produced:

```
<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">

  <rdf:Description rdf:about="http://bob.example.com/firstName">
    <label xmlns="http://www.w3.org/2000/01/rdf-schema#">first name</label>
    <columnPosition xmlns="http://vocab.sindice.net/csv/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">0</columnPosition>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/lastName">
    <label xmlns="http://www.w3.org/2000/01/rdf-schema#">last name</label>
    <columnPosition xmlns="http://vocab.sindice.net/csv/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1</columnPosition>
  </rdf:Description>

  <rdf:Description rdf:about="http://xmlns.com/foaf/0.1/knows">
    <columnPosition xmlns="http://vocab.sindice.net/csv/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</columnPosition>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/age">
    <label xmlns="http://www.w3.org/2000/01/rdf-schema#">age</label>
    <columnPosition xmlns="http://vocab.sindice.net/csv/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">3</columnPosition>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/row/0">
    <rdf:type rdf:resource="http://vocab.sindice.net/csv/Row"/>
    <firstName xmlns="http://bob.example.com/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Davide</firstName>
    <lastName xmlns="http://bob.example.com/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Palmisano</lastName>
    <knows xmlns="http://xmlns.com/foaf/0.1/"
    rdf:resource="http://michelemostarda.com"/
    <age xmlns="http://bob.example.com/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">30</age>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/">
    <row xmlns="http://vocab.sindice.net/csv/" rdf:resource="http://bob.example.com/row/0"/>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/row/0">
    <rowPosition xmlns="http://vocab.sindice.net/csv/">0</rowPosition>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/row/1">
    <rdf:type rdf:resource="http://vocab.sindice.net/csv/Row"/>
    <firstName xmlns="http://bob.example.com/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Michele</firstName>
    <lastName xmlns="http://bob.example.com/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#string">Mostarda</lastName>
    <knows xmlns="http://xmlns.com/foaf/0.1/" rdf:resource="http://g1o.net" />
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/">
    <row xmlns="http://vocab.sindice.net/csv/"
    rdf:resource="http://bob.example.com/row/1"/>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/row/1">
    <rowPosition xmlns="http://vocab.sindice.net/csv/">1</rowPosition>
  </rdf:Description>

  <rdf:Description rdf:about="http://bob.example.com/">
    <numberOfRows xmlns="http://vocab.sindice.net/csv/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2</numberOfRows>
    <numberOfColumns xmlns="http://vocab.sindice.net/csv/"
    rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">4</numberOfColumns>
  </rdf:Description>

</rdf:RDF>
```

---

<a id="release-howto"></a>

<!-- source_url: https://any23.apache.org/release-howto.html -->

<!-- page_index: 19 -->

<a id="release-howto--howto-release-apache-any23"></a>

## HowTo Release Apache Any23

This short guide is for volunteers that intend to cover the role of Release Manager

<a id="release-howto--prerequisites"></a>

## Prerequisites

- Install/Configure `GPG` - The artifacts that are deployed to the ASF central repository need to
  be signed. To do this you will need to have a public and private keypair. There is a very good
  [guide](http://www.sonatype.com/people/2010/01/how-to-generate-pgp-signatures-with-maven/) that will
  walk you though this.
- Install the latest version of [Apache Maven](https://maven.apache.org/download.cgi).

<a id="release-howto--configuration"></a>

## Configuration

<a id="release-howto--apache-maven"></a>

### Apache Maven

We highly recommend that you follow this
[guide](http://maven.apache.org/guides/mini/guide-encryption.html) to set your master password and
use it to encrypt your ASF password in the next section.

<a id="release-howto--asf-settings"></a>

### ASF settings

Using the instructions from the previous step encrypt your Sonatype password and add the following servers to
your `~/.m2/settings.xml` file. You may already have other servers in this file. If not just create
the file.

```
<?xml version="1.0" encoding="UTF-8"?>
<settings>
  ...
  <servers>
    <server>
      <id>apache.snapshots.https</id>
      <username>simonetripodi</username>
      <password>{put your encrypted password here}</password>
    </server>
    <server>
      <id>apache.releases.https</id>
      <username>simonetripodi</username>
      <password>{put your encrypted password here}</password>
    </server>
  </servers>
  ...
  <profiles>
    <profile>
      <id>apache</id>
      <activation>
        <activeByDefault>false</activeByDefault>
      </activation>
      <properties>
        <mavenExecutorId>forked-path</mavenExecutorId>
        <gpg.keyname>19FEA27D</gpg.keyname>\
        <!-- optional -->
        <gpg.passphrase>your-gpg-passphrase</gpg.passphrase>
      </properties>
    </profile>
  </profiles>
  ...
</settings>
```

You can find a [`settings.xml`](https://raw.githubusercontent.com/apache/any23-committers/master/maven/settings.xml)
template in our Github committers space

<a id="release-howto--release-steps"></a>

## Release steps

<a id="release-howto--prepare-the-source-for-release"></a>

### Prepare the source for release

1. Clean up JIRA so the **Fix Version** in issues resolved since the last release includes this release
   version correctly. Also, transition any **Resolved** issues to the **Closed** state.
2. Update the text files in a working copy of the project root:
   1. Update the `RELEASE-NOTES.md` based on the text release reports from JIRA.
   2. Review and update `README.md` if needed.
   3. Review and update dates in `NOTICE.txt` if needed.
   4. Commit any changes back to Git:


```
git add -A && git commit -m "updating files for release"
```

      .
3. Perform a full build and deploy the SNAPSHOT artifacts:


```
mvn clean deploy
```

<a id="release-howto--get-source-tree"></a>

### Get source tree

1. ***Only for new major releases (like 1.0.0 to 1.1.0):***
   Create a sub-branch from which to make the release.
   Releasing from a branch will allow any cosmetic changes that need to be made for the release to be
   approved to be done without preventing other more disruptive advances in the trunk from potentially
   causing problems with the release. It also provides a future maintenance branch (like 1.0.x.)
   A branch can be made by running:


```
mvn release:branch -DbranchName=1.0.x
```

2. Checkout a clean copy of the trunk/branch to release using command line Git:


```
git clone https://git-wip-us.apache.org/repos/asf/any23.git
```

<a id="release-howto--prepare-the-release"></a>

### Prepare the release

1. Do a dry run of the `release:prepare` step.


```
mvn release:prepare -DdryRun=true
```

   The dry run will not commit any changes back to SVN and gives you the opportunity to verify that the
   release process will complete as expected.

   *If you cancel a `release:prepare` before it updates the pom.xml versions, then use the
   `release:clean` goal to just remove the extra files that were created.*
2. Verify that the release process completed as expected:
   1. The release plugin will create `pom.xml.tag` files which contain the changes that would
      have been committed to SVN. The only differences between `pom.xml.tag` and its corresponding
      `pom.xml` file should be the version
      number.
   2. If other formatting changes have been made you should review the changes and then commit them:


```
git add -A && git commit -m "fixing formatting for release"
```

   3. Assuming the `.tag` files look OK you may proceed and do any other validation you feel
      necessary. The following list may be helpful:
      1. Check `release.properties` and make sure that the scm properties have the right version.
         Sometimes the scm location can be the previous version not the next version.
      2. Verify signatures: On Un\*x platforms the following command can be executed:


```
for file in `find . -type f -iname '*.asc'`
do
  gpg --verify ${file}
done
```

         You'll need to look at the output to ensure it contains only good signatures:


```
gpg: Good signature from ...
gpg: Signature made ...
```

   4. Once any failures or required updates have been committed to git, rollback the release prepare files:


```
mvn release:rollback
```

3. Run the `release:prepare` step for real this time. You'll be prompted for the same version
   information and optionally your GPG passphrase again.


```
mvn release:prepare
```

<a id="release-howto--perform-the-release"></a>

### Perform the release

1. From the directory where you have launched `release:prepare` execute (this step will create a maven staging repository):


```
mvn release:perform [-Duser.name=<your_apache_uid>]
```

   *If your local OS userid doesn't match your Apache userid, then you'll have to also override the value
   provided by the OS to Maven for the site-deploy step to work. This is known to work for Linux,
   but not for Mac and unknown for Windows.*

   1. Verify the staged artifacts in the Nexus repository:
      1. [https://repository.apache.org/](https://repository.apache.org/index.html)
      2. **Enterprise --> Staging**
      3. **Staging tab --> Name column --> org.apache.any23**
      4. Navigate through the artifact tree and make sure that all binary,
         `javadoc`,
         `sources`, and
         `tests` jars, as well as
         `pom`s, ... have
         `.asc` (GPG signature) and checksum files (see
         [Repository FAQ](http://people.apache.org/~henkp/repo/faq.html) and
         [Detached Signatures](http://www.apache.org/dev/release-signing.html#openpgp-ascii-detach-sig)).
         The `any23-sources-dist-X.Y.tar.gz` and
         `any23-sources-dist-X.Y.zip` files shall likewise have signature and checksum files.
   2. Close the Nexus staging repo:
      1. [https://repository.apache.org/](https://repository.apache.org/index.html)
      2. **Enterprise --> Staging**
      3. **Staging tab --> Name column --> org.apache.any23**
      4. Right click on the open `org.apache.any23-XXX` staging repo and select
         **Close**.
   3. Add the distribution artifacts to the dev staging area at <https://dist.apache.org/repos/dist/dev/any23/> ensuring that you provide SHA512 and ASC signatures all relevant artifacts.

<a id="release-howto--vote-the-release"></a>

### Vote the Release

1. Create a `VOTE` email thread on [dev@any23.apache.org](mailto:dev@any23.apache.org) and [user@any23.apache.org](mailto:user@any23.apache.org)
   to record votes as replies, e.g.:


```
To: "Apache Any23 Developers List" <dev@any23.apache.org>, "Apache Any23 Users List" <user@any23.apache.org>
Subject: [VOTE] Release Apache Any23 X.Y

Hi,

Please VOTE on the release candidate for Apache Any23 ${latestStableRelease}

Note, this release candidate requires JDK11 to build and run.

We solved N issues:
http://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12312323&styleName=Html&version=X.Y

Git source tag (r9999999):
https://gitbox.apache.org/repos/asf/any23.git ...

Staging repo:
https://repository.apache.org/content/repositories/orgapacheany23-[YOUR REPOSITORY ID]/

Sources and CLI binaries area:
https://dist.apache.org/repos/dist/dev/any23/${latestStableRelease}

PGP release keys (signed using ABCDEFG):
https://dist.apache.org/repos/dist/release/any23/KEYS

Vote will be open for 72 hours.

[ ] +1, Release as Apache Any23 ${latestStableRelease}
[ ] +/-0, fine, but consider to fix few issues before...
[ ] -1, nope, because... (and please explain why)
```

2. Perform a review of the release and cast your vote. For more details on Apache releases see
   <http://www.apache.org/legal/release-policy.html>.
3. A `-1` vote does not necessarily mean that the vote must be redone, however it is usually a
   good idea to rollback the release if a `-1` vote is received
   (see "Recovering from a vetoed release" below).
4. After the vote has been open for at least 72 hours, has at least three +1 PMC votes and no -1 votes, then
   post the results to the vote thread, replying to the initial email prepending `[RESULT]` to the
   original subject and include a list of every binding `+1`, `0` and `-1` vote.


```
To: "Apache Any23 Developers List" <dev@any23.apache.org>, "Apache Any23 Users List" <user@any23.apache.org>
Subject: [RESULT] [VOTE] Release Apache Any23 X.Y

Hi,
The vote has passed with the following result :

+1 (binding):

    Chris Mattmann
    Lewis John Mcgibbney
    Michele Mostarda
    Simone Tripodi

+1 (non binding):

    Mario Rossi
    John Doe

I will promote the artifacts to the central repo.
```

<a id="release-howto--finalize-the-release"></a>

### Finalize the Release

1. Promote the staged nexus artifacts:
   1. [https://repository.apache.org/](https://repository.apache.org/index.html)
   2. **Enterprise --> Staging**
   3. **Staging tab --> Name column --> org.apache.any23**
   4. Right click on the closed `org.apache.any23-XXX` staging repo and select **Release**.
2. Move the distribution artifacts from the dev staging area at <https://dist.apache.org/repos/dist/dev/any23/> to the release area at <https://dist.apache.org/repos/dist/release/any23/> ensuring that you provide SHA512 and ASC signatures all relevant artifacts.
3. Update the
   [JIRA versions](https://issues.apache.org/jira/plugins/servlet/project-config/ANY23/versions)
   page to mark the version as **Released**, and set the date to the date that
   the release was approved. You may also need to make a new release entry for the next release.
4. [Update the Any23 website](https://cwiki.apache.org/confluence/display/ANY23/Building+Apache+Any23+Website+HOW_TO)

<a id="release-howto--announce-the-release"></a>

### Announce the Release

Make an announcement about the release on the
[any23-user](mailto:user@any23.apache.org), [any23-dev](mailto:dev@any23.apache.org), [Web Data Commons - Google Group](https://groups.google.com/d/forum/web-data-commons), [nutch-dev](mailto:dev@nutch.apache.org), [camel-dev](mailto:dev@camel.apache.org), [servicemix-dev](mailto:dev@servicemix.apache.org), maybe some other relevant W3C and/or OGC groups as you see fit, and
[announce@apache.org](mailto:announce@apache.org) lists as per
[the Apache Announcement Mailing Lists page](http://www.apache.org/foundation/mailinglists.html#foundation-announce)

```
From: YOUR_APACHE_USERNAME@apache.org
To: "ASF Announcements" <announce@apache.org>, "Apache Any23 Users List" <user@any23.apache.org>
CC: "Apache Any23 Developers List" <dev@any23.apache.org>
Subject: [ANNOUNCE] Apache Any23 X.Y

The Apache Any23 Team is pleased to announce the release of Apache Any23 ${latestStableRelease}.

Apache Anything To Triples (Any23) is a library, a web service and a command line tool that extracts structured data in RDF format from a variety of Web documents.

Any23 ${latestStableRelease} requires JDK11 to build and run.

Release Notes: https://github.com/apache/any23/blob/any23-${latestStableRelease}/RELEASE-NOTES.md

Download: http://any23.apache.org/download.html

Maven Artifacts: https://s.apache.org/mwOE

DOAP: https://github.com/apache/any23-committers/blob/master/doap_Any23.rdf

Have Fun,
(Lewis), on behalf of the Apache Any23 PMC
N.B. The release artifacts can take a bit of time to reach the distribution servers, please be patient.
```

<a id="release-howto--recovering-from-a-vetoed-release"></a>

## Recovering from a vetoed release

1. Reply to the initial vote email prepending `[CANCELED]` to the original subject.
2. Rollback the version upgrades in trunk by *either*:
   1. Restore the 0.1-rc1.tar.gz and run


```
mvn release:rollback
```

      *or*
      manually revert the versions in trunk to the prior version and commit
3. Delete the git tag created by the `release:perform` step (N.B. replace ${tag\_name} with the actual tag name):


```
git tag -d ${tag_name} && git push origin :refs/tags/${tag_name}
```

4. Drop the Nexus staging repo:
   1. [https://repository.apache.org/](https://repository.apache.org/index.html)
   2. **Enterprise --> Staging**
   3. **Staging tab --> Name column --> org.apache.any23**
   4. Right click on the closed `org.apache.any23-XXX` staging repo and select **Drop**.
5. Make the required updates that caused the vote to be canceled.
6. Spin another release attempt!

---

<a id="ci-management"></a>

<!-- source_url: https://any23.apache.org/ci-management.html -->

<!-- page_index: 20 -->

<a id="ci-management--overview"></a>

## Overview

This project uses [Jenkins](https://www.jenkins.io/).

<a id="ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://ci-builds.apache.org/job/Any23/
```

<a id="ci-management--notifiers"></a>

## Notifiers

Configuration for notifying developers/users when a build is unsuccessful, including user information and notification mode.

| Type | Address | Configuration |
| --- | --- | --- |
| mail | - | address=dev@any23.apache.org |

---

<a id="mailing-lists"></a>

<!-- source_url: https://any23.apache.org/mailing-lists.html -->

<!-- page_index: 21 -->

<a id="mailing-lists--project-mailing-lists"></a>

## Project Mailing Lists

These are the mailing lists that have been established for this project. For each list, there is a subscribe, unsubscribe, and an archive link.

| Name | Subscribe | Unsubscribe | Post | Archive |
| --- | --- | --- | --- | --- |
| Dev Mailing List | [Subscribe](mailto:dev-subscribe@any23.apache.org) | [Unsubscribe](mailto:dev-unsubscribe@any23.apache.org) | [Post](mailto:dev@any23.apache.org) | [lists.apache.org](https://lists.apache.org/list.html?dev@any23.apache.org) |
| User Mailing List | [Subscribe](mailto:user-subscribe@any23.apache.org) | [Unsubscribe](mailto:user-unsubscribe@any23.apache.org) | [Post](mailto:user@any23.apache.org) | [lists.apache.org](https://lists.apache.org/list.html?user@any23.apache.org) |
| Commits Mailing List | [Subscribe](mailto:commits-subscribe@any23.apache.org) | [Unsubscribe](mailto:commits-unsubscribe@any23.apache.org) | [Post](mailto:commits@any23.apache.org) | [lists.apache.org](https://lists.apache.org/list.html?commits@any23.apache.org) |

---

<a id="modules"></a>

<!-- source_url: https://any23.apache.org/modules.html -->

<!-- page_index: 22 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Any23 :: Base API](https://any23.apache.org/api/any23-site/apache-any23-api/index.html) | Any23 library external API. |
| [Apache Any23 :: Test Resources](https://any23.apache.org/test-resources/any23-site/apache-any23-test-resources/index.html) | Anything To Triples (any23) is a library, a web service and a command line tool that extracts structured data in RDF format from a variety of Web documents. |
| [Apache Any23 :: CSV Utilities](https://any23.apache.org/csvutils/any23-site/apache-any23-csvutils/index.html) | CSV specific library. |
| [Apache Any23 :: Mime Type Detection](https://any23.apache.org/mime/any23-site/apache-any23-mime/index.html) | MIME Type detection library. |
| [Apache Any23 :: Encoding Detection](https://any23.apache.org/encoding/any23-site/apache-any23-encoding/index.html) | Encoding detection library. |
| [Apache Any23 :: Core](https://any23.apache.org/core/any23-site/apache-any23-core/index.html) | Core Any23 library implementation. |
| [Apache Any23 :: CLI](https://any23.apache.org/cli/any23-site/apache-any23-cli/index.html) | Command line interface. |

---

<a id="scm"></a>

<!-- source_url: https://any23.apache.org/scm.html -->

<!-- page_index: 23 -->

<a id="scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://github.com/apache/any23/tree/master
```

<a id="scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone --branch master http://gitbox.apache.org/repos/asf/any23.git
```

<a id="scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone --branch master https://gitbox.apache.org/repos/asf/any23.git
```

<a id="scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="summary"></a>

<!-- source_url: https://any23.apache.org/summary.html -->

<!-- page_index: 24 -->

<a id="summary--project-summary"></a>

## Project Summary

<a id="summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Any23 |
| Description | Anything To Triples (any23) is a library, a web service and a command line tool that extracts structured data in RDF format from a variety of Web documents. |
| Homepage | [https://any23.apache.org](#index) |

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
| GroupId | org.apache.any23 |
| ArtifactId | apache-any23 |
| Version | 2.8-SNAPSHOT |
| Type | pom |

---

<a id="team"></a>

<!-- source_url: https://any23.apache.org/team.html -->

<!-- page_index: 25 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | Roles |
| --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/6afcf37d03ebf6ce7bd5afa57d13026c?d=mm&s=60) | andy | Andy Seaborne | [andy@apache.org](mailto:andy@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/61688ba9d2199bd58e91c094f518e42d?d=mm&s=60) | ansell | Peter Ansell | [ansell@apache.org](mailto:ansell@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/2223df4357e259fa86baede9960ee373?d=mm&s=60) | band | Bill Anderson | [band@apache.org](mailto:band@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/40fa2c3773573856bb835c40fbc0e3ee?d=mm&s=60) | dpalmisano | Davide Palmisano | [dpalmisano@apache.org](mailto:dpalmisano@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/3a95ec4df189ddc59c2ea9ebf0f63372?d=mm&s=60) | giovanni | Giovanni Tummarello | [giovanni@apache.org](mailto:giovanni@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/3c676c438e0dd583c18203f82f3bb57a?d=mm&s=60) | hansbrende | Hans Brende | [hansbrende@apache.org](mailto:hansbrende@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/a72f46ba81459d988b1e6d0bfc251227?d=mm&s=60) | jgrzebyta | Jacek Grzebyta | [jgrzebyta@apache.org](mailto:jgrzebyta@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/c5ece8ca626d88de9431be9ca722149a?d=mm&s=60) | lewismc | Lewis John McGibbney | [lewismc@apache.org](mailto:lewismc@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/6f919a5883b854b9ae41023ef281ef85?d=mm&s=60) | mattmann | Chris Mattmann | [mattmann@apache.org](mailto:mattmann@apache.org) | Champion, Committer, PMC Member, Mentor |
| ![](https://www.gravatar.com/avatar/d4a8641cdb31fbf89ac1234178566dd7?d=mm&s=60) | mostarda | Michele Mostarda | [mostarda@apache.org](mailto:mostarda@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/01993e414e7419ecc266ec77880f9c87?d=mm&s=60) | niq | Nick Kew | [niq@apache.org](mailto:niq@apache.org) | Committer, PMC Member, Mentor |
| ![](https://www.gravatar.com/avatar/d1da8e755974b7dcb91eb9d9ee1e5ce0?d=mm&s=60) | pramirez | Paul Michael Ramirez | [pramirez@apache.org](mailto:pramirez@apache.org) | Committer, PMC Member, Mentor |
| ![](https://www.gravatar.com/avatar/0f8238df4b837e3eebb0aa13361c6ba8?d=mm&s=60) | reto | Reto Bachmann-Gmür | [reto@apache.org](mailto:reto@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/4a99d0a59538ce9eec18d41b6862d411?d=mm&s=60) | scor | Stephane Corlosquet | [scor@apache.org](mailto:scor@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/2c27249f3e6df269751ee1c5d74c7d2e?d=mm&s=60) | simonetripodi | Simone Tripodi | [simonetripodi@apache.org](mailto:simonetripodi@apache.org) | Committer, PMC Member, Mentor |
| ![](https://www.gravatar.com/avatar/0f979393a2e8106181fb0ad59ba832cc?d=mm&s=60) | szydan | Szymon Danielczyk | [szydan@apache.org](mailto:szydan@apache.org) | Committer, PMC Member |
| ![](https://www.gravatar.com/avatar/1cdf0e8e7459813d38631d18ba4f5a34?d=mm&s=60) | tommaso | Tommaso Teofili | [tommaso@apache.org](mailto:tommaso@apache.org) | Committer, PMC Member, Mentor |

<a id="team--contributors"></a>

### Contributors

There are no contributors listed for this project. Please check back again later.

---

<a id="acknowledgements"></a>

<!-- source_url: https://any23.apache.org/acknowledgements.html -->

<!-- page_index: 26 -->

<a id="acknowledgements--acknowledgments"></a>

## Acknowledgments

The original code base comes from open-sourcing the *"RDFizer"* component of the [Sindice](http://www.sindice.com) search engine. The project is supported by [DERI, NUI Galway](http://www.apache.ie/), [Web of Data - FBK](http://wed.fbk.eu/en/home) and the [OKKAM project (ICT-215032)](http://www.okkam.org/).

Initial developers who have contributed to **Any23** include (in alphabetic order): Michele Catasta, Richard Cyganiak, Michele Mostarda, Davide Palmisano, Gabriele Renzi, Juergen Umbrich. A more recent collection of contributors can be seen in the [GitHub contributors graph](https://github.com/apache/any23/graphs/contributors).

Below the initial sponsors of the *Any23* project.

![](assets/images/logo-sindice-90x30_635e75d38f0d581b.png)

[Sindice](http://sindice.com/)

Sindice is a platform to build applications on top of this data. Sindice collects Web Data in many ways, following existing web standards, and offers Search and Querying across this data, updated live every few minutes.

![](assets/images/logo-deri-90x30_bb640de90d3903a7.png)

[Digital Enterprise Research Institute](http://www.deri.ie/)

The vision of the Digital Enterprise Research Institute (DERI) is to be recognised as one of the leading international Web Science research institutes interlinking technologies, information and people to advance business and benefit society.

![](assets/images/logo-fbk-90x30_1abf11a2b88ec116.png)

[Fondazione Bruno Kessler](http://www.fbk.eu/)

FBK is a research organization of the Autonomous Province of Trento that promotes research in the areas of science, technology, and humanities. Thanks to a close network of alliances and collaborations, FBK also conducts research in theoretical nuclear physics, networking, telecommunications, and social sciences.

![](assets/images/logo-okkam-90x30_171b56bfa9d2baa1.png)

[OKKAM](http://www.okkam.org/)

The OKKAM project aims at enabling the Web of Entities, namely a virtual space where any collection of data and information about any type of entities (e.g. people, locations, organizations, events, products, ...) published on the Web can be integrated into a single virtual, decentralized, open knowledge base.

![](assets/images/logo-lod2-90x30_fce06333357bad5d.png)

[LOD2](http://lod2.eu/)

The LOD2 consortium comprises expertise in Semantic Web technologies, ontological engineering, machine learning, Web search, information retrieval, databases and knowledge stores. With CWI's reputation in the database world, LOD2 aims to substantially contribute to cross-fertilization between database and semantic web research.

---

<a id="poweredby"></a>

<!-- source_url: https://any23.apache.org/poweredby.html -->

<!-- page_index: 27 -->

<a id="poweredby--poweredby"></a>

## PoweredBy

This page collects a set of project and web initiatives which use *Apache Any23*.

![](assets/images/logo-sindice-90x30_635e75d38f0d581b.png)

Sindice was a platform to build applications on top of structured data. Sindice collected Web Data in many ways, following web standards, and offered search and querying across this data, updated live every few minutes.

![](assets/images/cc-logo_b00675ac8c062296.png)![](assets/images/ma-logo_0f97c9ff1dfb00ee.png)

[WebDataCommons](http://webdatacommons.org/)

The Web Data Commons project extracts structured data from the [Common Crawl](http://commoncrawl.org/), the largest web corpus available to the public, and provides the extracted data for public download in order to support researchers and companies in exploiting the wealth of information that is available on the Web.

![](assets/images/nutch-logo-tm_af49dccf1c03fa4f.png)

[Apache Nutch](http://nutch.apache.org)

Apache Nutch is a well matured, production ready Web crawler. Nutch enables fine grained configuration, relying on Apache Hadoop data structures, which are great for batch processing. Nutch uses Any23 within it's plugin infrastructure to extract structured data markup from Webpages. This data can then be indexed into one of the Nutch supported storage mechanisms.

![](assets/images/camel-logo_9b8056b40dcff5cb.jpg)

[Apache Camel](http://camel.apache.org)

Camel is an Open Source integration framework that empowers you to quickly and easily integrate various systems consuming or producing data.

![](assets/images/servicemix-logo_009b8b6ffc8ecc8d.png)

[Apache ServiceMix](http://servicemix.apache.org)

Apache ServiceMix is a flexible, open-source integration container that unifies the features and functionality of Apache ActiveMQ, Camel, CXF, and Karaf into a powerful runtime platform you can use to build your own integrations solutions. It provides a complete, enterprise ready ESB exclusively powered by OSGi.

---

<a id="plugin-html-scraper"></a>

<!-- source_url: https://any23.apache.org/plugin-html-scraper.html -->

<!-- page_index: 28 -->

<a id="plugin-html-scraper--html-scraper-plugin"></a>

## HTML Scraper Plugin

The HTML Scraper Plugin is meant to scrape any HTML page extracting human readable text only. Such plugin will generate a set of triples like:

```
<http://source-page-url> <http://vocab.sindice.net/pagecontent/de>  "<DE  Extractor Result>" .
<http://source-page-url> <http://vocab.sindice.net/pagecontent/ae>  "<AE  Extractor Result>" .
<http://source-page-url> <http://vocab.sindice.net/pagecontent/lce> "<LCE Extractor Result>" .
<http://source-page-url> <http://vocab.sindice.net/pagecontent/ce>  "<CE  Extractor Result>" .
```

The plugin engine is based on the  [Boilerpipe](http://code.google.com/p/boilerpipe/) library extractor. The extractors mentioned as **DE**, **AE**, **LCE** and **CE** are the ones defined within the library.

---

<a id="plugin-office-scraper"></a>

<!-- source_url: https://any23.apache.org/plugin-office-scraper.html -->

<!-- page_index: 29 -->

<a id="plugin-office-scraper--office-scraper-plugins"></a>

## Office Scraper Plugins

- *Excel Plugin*

  The [ExcelPlugin](https://any23.apache.org/apidocs/org/apache/any23/plugin/officescraper/ExcelPlugin.html) converts any **Microsoft Excel** *97-2007* document to *RDF*.

  **TODO: add conversion schema.**
- *Word Plugin*

  **NOTE: Under development.**

---
