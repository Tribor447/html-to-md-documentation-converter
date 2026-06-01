# Apache Gora™ - Gora Module Overview

## Navigation

- Introduction
  - [First if you haven't already done so, make sure to check the](#quickstart)
  - [You can also take a look at the](#api-javadoc)
- Gora Modules
  - [gora-compiler](#compiler)
  - [gora-compiler-cli](#compiler-cli)
  - [gora-core](#gora-core)
  - [gora-accumulo](#gora-accumulo)
  - [camel-gora](#gora-camel)
  - [gora-cassandra](#gora-cassandra)
  - [gora-dynamodb](#gora-dynamodb)
  - [gora-hbase](#gora-hbase)
  - [gora-jcache](#gora-jcache)
  - [gora-couchdb](#gora-couchdb)
  - [gora-metamodel](#gora-metamodel)
  - [gora-mongodb](#gora-mongodb)
  - [gora-solr](#gora-solr)
  - [gora-aerospike](#gora-aerospike)
  - [gora-ignite](#gora-ignite)
  - [gora-kudu](#gora-kudu)
  - [gora-pig](#gora-pig)
  - [gora-tutorial](#tutorial)
  - [gora-sql](#gora-sql)
- Data store specific settings
  - [Gora Core Module](#gora-core)
  - [Gora HBase Module](#gora-hbase)
  - [Gora Cassandra Module](#gora-cassandra)
  - [Gora Solr Module](#gora-solr)
  - [Gora Accumulo Module](#gora-accumulo)
  - [Gora DynamoDB Module](#gora-dynamodb)
  - [Gora MongoDB Module](#gora-mongodb)
- [Gora Java Documentation](#api-javadoc)
- [Current Documentation](#index)
- [JavaDoc Documentation](#api-javadoc)
- [Gora Tutorial](#tutorial)
- Other pages
  - [Apache Gora™ - Gora Configuration](#gora-conf)
  - [Apache Gora™ - Gora Module Overview](#overview)

## Content

<a id="quickstart"></a>

<!-- source_url: https://gora.apache.org/current/quickstart.html -->

<!-- page_index: 1 -->

<a id="quickstart--introduction"></a>

# Introduction

This is a quick start guide to help you setup the project.

<a id="quickstart--download"></a>

## Download

First you need to check out the most stable Gora release through the official
Apache Gora [release page](https://gora.apache.org/downloads.html).
For those who would like to use a development version Gora or simply wish to
work with the bleeding edge, instructions for how to check out the source
code using svn or git can be found on the [version control](https://gora.apache.org/version_control.html) documentation.

<a id="quickstart--setting-up-your-project"></a>

## Setting up your project

More recently Gora began using Maven to manage it's dependencies and build lifecycle.
Stable Gora releases are available on the central maven repository or ivy repositories
and Gora-SNAPSHOT OSGi bundle artifacts are now pushed to
[Apache Nexus](https://repository.apache.org/index.html#nexus-search;quick~gora).

<a id="quickstart--compiling-and-installing-the-project"></a>

## Compiling and Installing the project

If you have the source code for Gora, you can install the project using

```
$ cd gora
$ mvn clean install
```

You can also install individual modules by cd'ing to the module directory and running

```
$ mvn clean install
```

If you want to use Gora as a dependency, you can manage it in a few ways.

<a id="quickstart--using-ivy-to-manage-gora"></a>

## Using ivy to manage Gora

If your project already uses ivy, then you can include gora dependencies
to your ivy by adding the following lines to your ivy.xml file:

```
  <dependency org="org.apache.gora" name="gora-core" rev="${version}" conf="*->compile" changing="true">
  <dependency org="org.apache.gora" name="gora-dynamodb" rev="${version}" conf="*->compile" changing="true">
  <dependency org="org.apache.gora" name="gora-hbase" rev="${version}" conf="*->compile" changing="true">      
  ...etc
```

Note: The ${version} variable should be replaced by the most stable Gora release.

Only add the modules that you will use, and set the conf to point to the
configurations (of your project) that you want to depend on Gora. The
changing="true" attribute states that, Gora artifacts
should not be cached, which is required if you want to change Gora's
source and use the recompiled version.

Add the following to your ivysettings.xml

```
<resolvers> ...<chain name="internal"> <resolver ref="local"> </chain> ...</resolvers> <modules> ...<module organisation="org.apache.gora" name=".*" resolver="internal"> ...</modules>
```

This forces Gora to be built locally rather than look for it in other repositories.

<a id="quickstart--using-maven-to-manage-gora"></a>

## Using Maven to manage Gora

If your project however uses maven, then you can include Gora dependencies
to your project by adding the following lines to your pom.xml file:

```
<dependency>
	<groupId>org.apache.gora</groupId>
	<artifactId>gora-core</artifactId>
	<version>${version}</version>
 </dependency>

<dependency>
	<groupId>org.apache.gora</groupId>
	<artifactId>gora-accumulo</artifactId>
	<version>${version}</version>
</dependency>

...etc
```

N.B. The ${version} variable should be replaced by the most stable Gora release.

Again, only add the modules that you will use.

<a id="quickstart--specifying-gora-snapshot-dependencies"></a>

## Specifying Gora SNAPSHOT dependencies

If you want to depend on Gora development snapshots, e.g. to get access to recent bug fixes, you should add the following to your pom.xml:

```
<repository>
  <id>apache-repo-snapshots</id>
  <url>https://repository.apache.org/content/repositories/snapshots/</url>
  <releases>
    <enabled>false</enabled>
  </releases>
  <snapshots>
    <enabled>true</enabled>
  </snapshots>
</repository>
```

<a id="quickstart--managing-gora-jars-manually"></a>

## Managing Gora Jars Manually

You can include Gora jars manually, if you prefer so. After installing Gora
first and generating the desired artifacts, copy all the jars in gora-[modulename]/lib/
and gora-[modulename]/target/gora-${modulename}.jar dir's to your desired
location. Finally copy all the jars in gora-core/lib/ since all of the
modules depend on gora-core.

<a id="quickstart--whats-next"></a>
<a id="quickstart--what-s-next"></a>

## What's Next?

After setting up Gora, you might want to check out the documentation.
Most of the current documentation is linked to from the [overview](#index)
or is available on the [wiki](https://cwiki.apache.org/confluence/display/GORA/Index).

---

<a id="api-javadoc"></a>

<!-- source_url: https://gora.apache.org/current/api/javadoc.html -->

<!-- page_index: 2 -->

# Gora Java Documentation ¶

---

---

<a id="compiler"></a>

<!-- source_url: https://gora.apache.org/current/compiler.html -->

<!-- page_index: 3 -->

<a id="compiler--introduction"></a>

# Introduction

The Gora compiler converts JSON files (the schema(s)) into persistent Java classes/data beans.
You can then use those classes to interact with a variety of data storage software e.g. the Gora datastore implementations.

The compiler is very simple to run. But first you should add the Gora installation directory to your path.

<a id="compiler--usage"></a>

# Usage

```
 $ bin/gora goracompiler
```

results in:

```
$ Usage: GoraCompiler <schema file> <output dir> [-license <id>] <schema file> - individual avsc file to be compiled or a directory path containing avsc files <output dir> - output directory for generated Java files [-license <id>] - the preferred license header to add to the generated Java file. Current options include; ASLv2 (Apache Software License v2.0) AGPLv3 (GNU Affero General Public License) CDDLv1 (Common Development and Distribution License v1.0) FDLv13 (GNU Free Documentation License v1.3) GPLv1 (GNU General Public License v1.0) GPLv2 (GNU General Public License v2.0) GPLv3 (GNU General Public License v3.0) LGPLv21 (GNU Lesser General Public License v2.1) LGPLv3 (GNU Lesser General Public License v2.1)
```

so for example, one would typically enter:

```
 $ bin/gora goracompiler gora-tutorial/src/main/avro/pageview.json gora-tutorial/src/main/java/
```

The schema file is a single JSON file or a directory containing JSON files.

The output directory is the destination for the generated Java source files. For example, if you specific src/main/java then the
generate source is placed into src/main/java/generated. It's generally a good idea to ignore the generate directory in whatever
version control software you're using. You are using version control, right?

Finally, the license parameter tells the compile to add a license header to each generated file. Current header options include:

- ASLv2 ([Apache Software License v2.0](http://www.apache.org/licenses/LICENSE-2.0.html))
- AGPLv3 ([GNU Affero General Public License](http://www.gnu.org/licenses/agpl.html))
- CDDLv1 ([Common Development and Distribution License v1.0](http://opensource.org/licenses/CDDL-1.0))
- FDLv13 (<a href-"[http://www.gnu.org/copyleft/fdl.html">GNU](http://www.gnu.org/copyleft/fdl.html%22%3EGNU) Free Documentation License v1.3)
- GPLv1 ([GNU General Public License v1.0](http://www.gnu.org/licenses/gpl-1.0.html))
- GPLv2 ([GNU General Public License v2.0](http://www.gnu.org/licenses/gpl-2.0.html))
- GPLv3 ([GNU General Public License v3.0](http://www.gnu.org/licenses/gpl-3.0.html))
- LGPLv21 ([GNU Lesser General Public License v2.1](http://www.gnu.org/licenses/lgpl-2.1.html))
- LGPLv3 ([GNU Lesser General Public License v3](http://www.gnu.org/licenses/lgpl-3.0.html))

It should be noted that if no license header argument is passed, by default the ASLv2 license profile is selected.

---

<a id="compiler-cli"></a>

<!-- source_url: https://gora.apache.org/current/compiler-cli.html -->

<!-- page_index: 4 -->

<a id="compiler-cli--introduction"></a>

# Introduction

The Gora compiler-cli is a simple utility dependency which provides a command line interface used to invoke the [Gora Compiler](#compiler)
It exists separate from the Gora Compiler enabling us to distinguish between usability and functionality. It does however depend upon the Gora Compiler.

The compiler-cli is trivial to invoke but also provides a useful usage statement when invoked incorrectly

<a id="compiler-cli--usage"></a>

# Usage

```
$ Usage: GoraCompilerCLI or
 $ Uage: GoraCompilerCLI -h
```

results in:

```
 $ Usage: gora-compiler ( -h | --help ) | (<input> [<input>...] <output>)
```

so for example, if you wished to compile one schema file, you could enter:

```
 $ bin/gora gora-compiler gora-tutorial/src/main/avro/pageview.json gora-tutorial/src/main/java/
```

if however for example you wished to compile more than one schema file, you could enter:

```
 $ bin/gora gora-compiler gora-tutorial/src/main/avro/pageview.json gora-core/src/examples/avro/webpage.json gora-tutorial/src/main/avro/metricdatum.json gora-tutorial/src/main/java/
```

The schema file is a single JSON file or a string array of JSON files.

The output directory is the destination for the generated Java source files. For example, if you specific `src/main/java` then the
generate source is placed into `src/main/java/` under the package naming convention used within the JSON schema.

---

<a id="gora-core"></a>

<!-- source_url: https://gora.apache.org/current/gora-core.html -->

<!-- page_index: 5 -->

<a id="gora-core--overview"></a>

# Overview

This is the main documentation for DataStore's contained within the
`gora-core` module which (as it's name implies)
holds most of the core functionality for the gora project.

Every module
in gora depends on gora-core therefore most of the generic documentation
about the project is gathered here as well as the documentation for `AvroStore`, `DataFileAvroStore` and `MemStore`. In addition to this, gora-core holds all of the
core **MapReduce**, **GoraSparkEngine**, **Persistency**, **Query**, **DataStoreBase** and **Utility** functionality.

<a id="gora-core--avrostore"></a>

# AvroStore

<a id="gora-core--description"></a>

## Description

AvroStore can be used for binary-compatible Avro serializations. It supports Binary and JSON serializations.

<a id="gora-core--goraproperties"></a>
<a id="gora-core--gora.properties"></a>

## gora.properties

| Property Key | Property Value | Required | Description |
| --- | --- | --- | --- |
| gora.datastore.default= | org.apache.gora.avro.store.AvroStore | Yes | Implementation of the persistent Java storage class |
| gora.avrostore.input.path= | \*hdfs://uri/path/to/hdfs/input/path\* \|\| \*file:///uri/path/to/local/input/path\* | Yes | This value should point to the input directory on hdfs (if running Gora in a distributed Hadoop environment) or to some location input directory on the local file system (if running Gora locally). |
| gora.avrostore.output.path= | \*hdfs://uri/path/to/hdfs/output/path\* \|\| \*file:///uri/path/to/local/output/path\* | Yes | This value should point to the output directory on hdfs (if running Gora in a distributed Hadoop environment) or to some location output location on the local file system (if running Gora locally). |
| gora.avrostore.codec.type= | BINARY \|\| JSON | No | The property key specifying avro encoder/decoder type to use. Can take values `BINARY` or `JSON` but resolves to BINARY is one is not supplied. |

<a id="gora-core--avrostore-xml-mappings"></a>

## AvroStore XML mappings

In the stores covered within the gora-core module, no physical mappings are required.

<a id="gora-core--datafileavrostore"></a>

# DataFileAvroStore

<a id="gora-core--description_1"></a>
<a id="gora-core--description-2"></a>

## Description

DataFileAvroStore is file based store which extends <codeAvroStore to use Avro's `DataFile{Writer,Reader}`'s as a backend.
This datastore supports MapReduce.

<a id="gora-core--goraproperties_1"></a>
<a id="gora-core--gora.properties-2"></a>

## gora.properties

DataFileAvroStore would be configured exactly the same as in AvroStore above with the following exception

| Property Key | Property Value | Required | Description |
| --- | --- | --- | --- |
| gora.datastore.default= | org.apache.gora.avro.store.DataFileAvroStore | Yes | Implementation of the persistent Java storage class |

<a id="gora-core--gora-core-mappings"></a>

## Gora Core mappings

In the stores covered within the gora-core module, no physical mappings are required.

<a id="gora-core--memstore"></a>

# MemStore

<a id="gora-core--description_2"></a>
<a id="gora-core--description-3"></a>

## Description

Essentially this store is a ConcurrentSkipListMap in which operations run as follows

- put(K key, T Object) - expect average log(n)
- get(K key, String [] fields) - expect average log(n)
- delete(K key) - expect average log(n)

<a id="gora-core--goraproperties_2"></a>
<a id="gora-core--gora.properties-3"></a>

## gora.properties

MemStore would be configured exactly the same as in AvroStore above with the following exception

| Property Key | Property Value | Required | Description |
| --- | --- | --- | --- |
| gora.datastore.default= | org.apache.gora.memory.store.MemStore | Yes | Implementation of the Java class used to hold data in memory |

<a id="gora-core--memstore-xml-mappings"></a>

## MemStore XML mappings

In the stores covered within the gora-core module, no physical mappings are required.

<a id="gora-core--gorasparkengine"></a>

# GoraSparkEngine

<a id="gora-core--description_3"></a>
<a id="gora-core--description-4"></a>

## Description

GoraSparkEngine is Spark backend of Gora. Assume that input and output data stores are:

```
DataStore<K1, V1> inStore;
DataStore<K2, V2> outStore;
```

First step of using GoraSparkEngine is to initialize it:

```
GoraSparkEngine<K1, V1> goraSparkEngine = new GoraSparkEngine<>(K1.class, V1.class);
```

Construct a `JavaSparkContext`. Register input data store’s value class as Kryo class:

```
SparkConf sparkConf = new SparkConf().setAppName("Gora Spark Integration Application").setMaster("local");
Class[] c = new Class[1];
c[0] = inStore.getPersistentClass();
sparkConf.registerKryoClasses(c);
JavaSparkContext sc = new JavaSparkContext(sparkConf);
```

JavaPairRDD can be retrieved from input data store:

```
JavaPairRDD<Long, Pageview> goraRDD = goraSparkEngine.initialize(sc, inStore);
```

After that, all Spark functionality can be applied. For example running count can be done as follows:

```
long count = goraRDD.count();
```

Map and Reduce functions can be run on a `JavaPairRDD` as well. Assume that this is the variable after map/reduce is applied:

```
JavaPairRDD<String, MetricDatum> mapReducedGoraRdd;
```

Result can be written as follows:

```
Configuration sparkHadoopConf = goraSparkEngine.generateOutputConf(outStore);
mapReducedGoraRdd.saveAsNewAPIHadoopDataset(sparkHadoopConf);
```

---

<a id="gora-accumulo"></a>

<!-- source_url: https://gora.apache.org/current/gora-accumulo.html -->

<!-- page_index: 6 -->

<a id="gora-accumulo--overview"></a>

## Overview

This is the main documentation for the gora-accumulo module which
enables [Apache Accumulo](http://accumulo.apache.org) backend support for Gora.

<a id="gora-accumulo--goraproperties"></a>
<a id="gora-accumulo--gora.properties"></a>

## gora.properties

- `gora.datastore.default`=org.apache.gora.accumulo.store.AccumuloStore - Implementation of the storage class
- `gora.accumulo.mapping.file`=gora-accumulo-mapping.xml - The XML mapping file to be used
- `gora.datastore.accumulo.mock`=true - Mock Accumulo supplies mock implementations for much of the client API. It presently does not enforce users, logins, permissions, etc. It does support Iterators and Combiners. Note that MockAccumulo holds all data in memory, and will not retain any data or settings between runs.
- `gora.datastore.accumulo.instance`=a14 - An identifier for the Accumulo instance
- `gora.datastore.accumulo.zookeepers`=localhost - This value should specify the host:port for a running Zookeeper server or node. In this case the server happens to be running on localhost which is the default server configuration.
- `gora.datastore.accumulo.user`=root - This relates to the name of the client which will be communicating with Accumulo. This is also used for authentication purposes.
- `gora.datastore.accumulo.password`=secret - This relates to the password of the client which will be communicating with Accumulo. This is also used for authentication purposes.

<a id="gora-accumulo--gora-accumulo-mappings"></a>

## Gora Accumulo mappings

Say we wished to map some Employee data and store it into the AccumuloStore.

```
<gora-otd>
  <table name="Employee">
    <family name="info" />
    <config key="table.file.compress.blocksize" value="32K"/>
  </table>

  <class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" table="Employee" 
      encoder="org.apache.gora.accumulo.encoders.BinaryEncoder">
    <field name="name" family="info" qualifier="nm"/>
    <field name="dateOfBirth" family="info" qualifier="db"/>
    <field name="ssn" family="info" qualifier="sn"/>
    <field name="salary" family="info" qualifier="sl"/>
    <field name="boss" family="info" qualifier="bs"/>
    <field name="webpage" family="info" qualifier="wp"/>
  </class>
</gora-otd>
```

Here you can see that we require the definition of two child elements within the `gora-otd` mapping configuration, namely;

The **table** element; where we specify:

1. a parameter relating to the Accumulo table name (String) e.g. name="Employee", 2. a nested element containing the type and definition of any families we wish to create within Accumulo. In this case we create one family *info* which could have a combination of any of the following parameters;

   a **name** (String): family name e.g. info

   a **config** (key:value): which is a typical key/value-type configuration for Accumulo runtime configuration. A fully comprehensive list of options can be found [here](http://accumulo.apache.org/1.5/accumulo_user_manual.html#_table_configuration)

The **class** element where we specify of persistent fields which values should map to. This contains;

1. a parameter containing the Persistent class **name** e.g. `org.apache.gora.examples.generated.Employee`, 2. a parameter containing the **keyClass** e.g. `java.lang.String` which specifies the keys which map to the field values, 3. a parameter containing the Table **name** e.g. `Employee` which matches to the above Table definition, 4. a parameter containing the **Encoder** to be used e.g. `org.apache.gora.accumulo.encoders.BinaryEncoder` which defines an appropriate [encoder](https://github.com/apache/gora/tree/master/gora-accumulo/src/main/java/org/apache/gora/accumulo/encoders) for for object field values.
5. finally nested child element(s) mapping fields which are to be persisted into Accumulo. These fields need to be configured such that they receive;

   a parameter containing the **name** e.g. (name, dateOfBirth, ssn and salary respectively),

   a parameter containing the column **family** to which they belong e.g. (all info in this case),

   an optional parameter **qualifier**, which enables more granular control over the data to be persisted into HBase.

---

<a id="gora-camel"></a>

<!-- source_url: https://gora.apache.org/current/gora-camel.html -->

<!-- page_index: 7 -->

<a id="gora-camel--introduction"></a>

# Introduction

**Camel-Gora** is an [Apache Camel](http://camel.apache.org/) component that allows you to work with NoSQL databases using the
[Apache Gora](http://gora.apache.org/) framework.

**N.B.** Camel-Gora is NOT a Gora module... but instead a Camel one. This documentation exists to provide detail on how
Gora is being used in different settings.

**Available as of Camel 2.14**

<a id="gora-camel--maven-configuration"></a>

## Maven Configuration

Maven users will need to add the following dependency to their pom.xml for this component:

```
<dependency>
    <groupId>org.apache.camel</groupId>
    <artifactId>camel-gora</artifactId>
    <version>x.x.x</version>
    <!-- use the same version as your Camel core version -->
</dependency>
```

<a id="gora-camel--uri-format"></a>

## URI format

```
gora:instanceName[?options]
```

Hbase examples with mandatory options :

*XML*

```
<to uri="gora:foobar?keyClass=java.lang.Long&amp;valueClass=org.apache.camel.component.gora.generated.Pageview&amp;dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

*Java DSL*

```
to("gora:foobar?keyClass=java.lang.Long&valueClass=org.apache.camel.component.gora.generated.Pageview&dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

<a id="gora-camel--configuratiion"></a>

## Configuratiion

Using camel-gora needs some configuration. This mainly involve to configure the `AvroStore` through the `gora.properties` file and to define the relevant mappings as part of the *[gora-core](#gora-core)* module.

Extensive information for this configuration can be found in the apache [gora documentation](#index) and the [gora-conf](#gora-conf) page.

<a id="gora-camel--supported-gora-operations"></a>

## Supported Gora Operations

Supported operations include : ***put**, **get**, **delete**, **getSchemaName**, **deleteSchema**, **createSchema**, **query**, **deleteByQuery**, **schemaExists***.

Some of the operations require arguments while some others no. The arguments to operations could be either the *body* of the *in* message or defined in a header property. Below there is a list with some additional info for each operation.

| Property | Description |
| --- | --- |
| `put` \*Inserts the persistent object with the given key.\* |  |
| `get` \*Returns the object corresponding to the given key fetching all the fields.\* |  |
| `delete` \*Deletes the object with the given key.\* |  |
| `getSchemaName` \*Returns the schema name given to this DataStore.\* |  |
| `deleteSchema` \*Deletes the underlying schema or table (or similar) in the datastore that holds the objects.\* |  |
| `createSchema` \*Creates the optional schema or table (or similar) in the datastore to hold the objects.\* |  |
| `query` \*Executes the given query and returns the results.\* |  |
| `deleteByQuery` \*Deletes all the objects matching the query.\* |  |
| `schemaExists` \*Returns whether the schema that holds the data exists in the datastore.\* |  |

<a id="gora-camel--options"></a>

## Options

<a id="gora-camel--gora-headers"></a>

### Gora Headers

| Property | Description |
| --- | --- |
| `GoraOperation` \*Used in order to define the operation to execute.\* |  |
| `GoraKey` \*Used in order to define the datum key for the operations need it.\* |  |

<a id="gora-camel--gora-configuration-attributes"></a>

### Gora Configuration attributes

| Property | Type | Description |
| --- | --- | --- |
| `keyClass` | \_String\_ | \*Key type.\* \* |
| `valueClass` | \_String\_ | \*Value type.\* \* |
| `dataStoreClass` | \_String\_ | \*DataStore type\* \* |
| `hadoopConfiguration` | \_Configuration\_ | \*Hadoop Configuration\* |
| `concurrentConsumers` | \_int\_ | \*Concurrent Consumers (used only by consumers).\* |
| `flushOnEveryOperation` | \_boolean\_ | \*Flush on every operation (used only by producers).\* |

*NOTE: the gora configuration properties marked with asterisk are mandatory*

<a id="gora-camel--gora-query-attributes"></a>

### Gora Query attributes

| Property | Type | Description |
| --- | --- | --- |
| `startTime` | \_long\_ | \*Start Time attribute.\* |
| `endTime` | \_long\_ | \*End Time attribute.\* |
| `timeRangeFrom` | \_long\_ | \*Time Range From attribute.\* |
| `timeRangeTo` | \_long\_ | \*Time Range To attribute.\* |
| `limit` | \_long\_ | \*Gora Query Limit attribute.\* |
| `timestamp` | \_long\_ | \*Timestamp attribute.\* |
| `startKey` | \_Object\_ | \*Start Key attribute.\* |
| `endKey` | \_Object\_ | \*End Key attribute.\* |
| `keyRangeFrom` | \_Object\_ | \*Key Range From attribute.\* |
| `keyRangeTo` | \_Object\_ | \*Key Range To attribute.\* |
| `fields` | \_String\_ | \*Fields attribute.\* |

<a id="gora-camel--usage-examples"></a>

### Usage examples

**Create Schema** *(XML DSL)*:

```
<setHeader headerName="GoraOperation">
   <constant>CreateSchema</constant>
</setHeader>

<to uri="gora:foobar?keyClass=java.lang.Long&amp;valueClass=org.apache.camel.component.gora.generated.Pageview&amp;dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

**SchemaExists** *(XML DSL)*:

```
  <setHeader headerName="GoraOperation">
  	<constant>SchemaExists</constant>
  </setHeader>
  
  <to uri="gora:foobar?keyClass=java.lang.Long&amp;valueClass=org.apache.camel.component.gora.generated.Pageview&amp;dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

**Put** *(XML DSL)*:

```
  <setHeader headerName="GoraOperation">
    <constant>put</constant>
  </setHeader>
       
  <setHeader headerName="GoraKey">
    <constant>22222</constant>
  </setHeader>

  <to uri="gora:foo?keyClass=java.lang.Long&amp;valueClass=org.apache.camel.component.gora.generated.Pageview&amp;dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

**Get** *(XML DSL)*:

```
<setHeader headerName="GoraOperation">
   <constant>GET</constant>
</setHeader>

<setHeader headerName="GoraKey">
   <constant>10101</constant>
</setHeader>

<to uri="gora:bar?keyClass=java.lang.Long&amp;valueClass=org.apache.camel.component.gora.generated.Pageview&amp;dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

**Delete** *(XML DSL)*:

```
<setHeader headerName="GoraOperation">
  <constant>DELETE</constant>
</setHeader>

<setHeader headerName="GoraKey">
  <constant>22222</constant>
</setHeader>

<to uri="gora:bar?keyClass=java.lang.Long&amp;valueClass=org.apache.camel.component.gora.generated.Pageview&amp;dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

**Query** *(XML DSL)*:

```
<to uri="gora:foobar?keyClass=java.lang.Long&amp;valueClass=org.apache.camel.component.gora.generated.Pageview&amp;dataStoreClass=org.apache.gora.hbase.store.HBaseStore"/>
```

The full usage examples in the form of integration tests can be found at [camel-gora-examples](https://github.com/ipolyzos/camel-gora-examples/) repository.

<a id="gora-camel--more-resources"></a>

### More resources

For more please information and in depth configuration refer to the [Apache Gora Documentation](#overview) and the [Apache Gora Tutorial](#tutorial).

---

<a id="gora-cassandra"></a>

<!-- source_url: https://gora.apache.org/current/gora-cassandra.html -->

<!-- page_index: 8 -->

<a id="gora-cassandra--overview"></a>

## Overview

This is the main documentation for the gora-cassandra module which
enables [Apache Cassandra](http://cassandra.apache.org) backend support for Gora.

<a id="gora-cassandra--goraproperties"></a>
<a id="gora-cassandra--gora.properties"></a>

## gora.properties

| Property Key | Property Value | Required | Description |
| --- | --- | --- | --- |
| gora.datastore.default= | org.apache.gora.cassandra.store.CassandraStore | Yes | Implementation of the persistent Java storage class |
| gora.cassandrastore.mapping.file= | /path/to/gora-cassandra-mapping.xml | No | The XML mapping file to be used. If no value is used this defaults to `gora-cassandra-mapping.xml` |
| gora.cassandrastore.cassandraServers= | localhost | Yes | This value should specify the host for a running Cassandra server or node. In this case the server happens to be running on localhost which is the default Cassandra server configuration. |
| gora.cassandrastore.port= | 9042 | Yes | This value should specify the cql port for a running Cassandra server or node. In this case the server happens to be running on 9042 port which is the default Cassandra server configuration. |
| gora.cassandrastore.clusterName= | Test Cluster | No | This value should specify the cassandra cluster name for a running Cassandra server or node. In this case the server has configured to run with Cassandra cluster name as 'Test Cluster' which is the default Cassandra server configuration. |
| gora.cassandrastore.username= | ${username} | No | The authentication details for passing a **username** to the CassandraHostConfigurator. This will be required if security is required for Cassandra reads and writes. |
| gora.cassandrastore.password= | ${password} | No | The authentication details for passing a **password** to the CassandraHostConfigurator. This will be required if security is required for Cassandra reads and writes. |
| gora.cassandrastore.cassandraSerializationType= | AVRO/NATIVE | No | The serialization type for persist into the cassandra data store. default value is Native serialization type |

<a id="gora-cassandra--gora-cassandra-mappings"></a>

## Gora Cassandra mappings

Say we wished to map some CassandraRecord data and store it into the CassandraStore.

```
<gora-otd>

    <keyspace name="RecordKeySpace" durableWrite="false">
        <placementStrategy name="SimpleStrategy" replication_factor="1"/>
    </keyspace>

    <class name="org.apache.gora.cassandra.example.generated.AvroSerialization.CassandraRecord"
           keyClass="org.apache.gora.cassandra.example.generated.AvroSerialization.CassandraKey"
           keyspace="RecordKeySpace"
           table="CassandraRecord" allowFiltering="true" id="5a1c395e-b41f-11e5-9f22-ba0be0483c18">
        <field name="name" column="name" type="text"/>
        <field name="dataInt" column="age" type="int"/>
        <field name="salary" column="salary" type="bigint"/>
        <field name="dataDouble" column="testDouble" type="double"/>
        <field name="dataBytes" column="quotes" type="blob"/>
        <field name="arrayInt" column="listInt" type="list(int)"/>
        <field name="arrayString" column="listString" type="list(text)"/>
        <field name="arrayLong" column="listLong" type="list(bigint)"/>
        <field name="arrayDouble" column="listDouble" type="list(double)"/>
        <field name="mapInt" column="mapInt" type="map(text,int)"/>
        <field name="mapString" column="mapString" type="map(text,text)"/>
        <field name="mapLong" column="mapLong" type="map(text,bigint)"/>
        <field name="mapDouble" column="mapDouble" type="map(text,double)"/>
    </class>

    <cassandraKey name="org.apache.gora.cassandra.example.generated.AvroSerialization.CassandraKey">
        <partitionKey>
            <field name="url" column="urlData" type="text"/>
            <field name="timestamp" column="timestampData" type="bigint"/>
        </partitionKey>
        <clusterKey>
            <key column="timestampData" order="desc"/>
        </clusterKey>
    </cassandraKey>

</gora-otd>
```

Here you can see that we require the definition of two child elements within the
`gora-otd` mapping configuration, namely;

The **keyspace** element; where we specify:

1. a parameter containing the Cassandra keyspace schema name e.g. **RecordKeySpace**, 2. a parameter containing the durable write enabled property in the Cassandra keyspace e.g. **false**, More about durable write can be found [here](http://docs.datastax.com/en/cassandra/2.1/cassandra/dml/dml_durability_c.html).
3. the child element **placementStrategy** containing the Cassandra placementStrategy details, a parameter containing the Cassandra placement strategy name, e.g. **SimpleStrategy**, gora-cassandra will use SimpleStrategy by default if no value for this attribute is specified. More about placement strategies can be found [here](http://docs.datastax.com/en/archived/cassandra/2.0/cassandra/architecture/architectureDataDistributeReplication_c.html).
4. a parameter containing a **replicationFactor** attribute with value integer. Again the replicationFactor value associated with the Keyspace tag
   will only apply if Gora creates the Keyspace and will have no effect if this is being used against
   an existing keyspace. the default value for 'replicationFactor' is '1'.

The **class** element specifying persistent fields which values should map to. This element contains;

1. a parameter containing the Persistent class name e.g. **org.apache.gora.cassandra.example.generated.AvroSerialization.CassandraRecord**, 2. a parameter containing the keyClass e.g. **org.apache.gora.cassandra.example.generated.AvroSerialization.CassandraKey** which specifies the keys which map to the field values, 3. a parameter containing the keyspace e.g. **RecordKeySpace** which matches to the above keyspace definition, 4. a parameter containing the table name e.g. **CassandraRecord**, 5. a parameter containing the allow filtering e.g. **true**, More about allow filtering can be found [here](https://www.datastax.com/dev/blog/allow-filtering-explained-2).
6. a child element(s) **field** which represent fields which are to be persisted into Cassandra. These need to be configured such that they receive the following;

   finally a parameter **name** e.g. (name, dateOfBirth, ssn and salary respectively) which map to Gora field name,

   a parameter containing the column name e.g. **name**,

   a parameter containing the data type of the column e.g. **text**,

   an optional parameter **primarykey**, which indicates the primary key.

The **cassandraKey** element specifying composite key fields which is used in keyClass, This is optional, this element should be added only when composite keys are available;

1. a child element(s) **partitionKey** which represent cassandra partition key

   a child element(s) **compositeKey** which represent cassandra composite partition key

   a child element(s) **field** which represent partition key fields which are to be persisted into Cassandra. These need to be configured such that they receive the following;

   a parameter **name** e.g. (name, dateOfBirth, ssn and salary respectively) which map to Gora field name,

   a parameter containing the column name e.g. **name**,

   a parameter containing the data type of the column **text**, 2. a child element(s) **clusterKey** which represent cassandra cluster key

   a child element(s) **key** which represents column key fields which needs to be add clustered key.

   a parameter containing the column name e.g. **name**,

   a parameter containing the Order type of the column to be applied e.g. **desc**,

---

---

<a id="gora-dynamodb"></a>

<!-- source_url: https://gora.apache.org/current/gora-dynamodb.html -->

<!-- page_index: 9 -->

<a id="gora-dynamodb--overview"></a>

## Overview

This is the main documentation for the gora-dynamodb module.
gora-dynamodb module enables [Amazon DynamoDB](http://aws.amazon.com/dynamodb/) backend support for Gora.

<a id="gora-dynamodb--gora-dynamodb-properties-goraproperties"></a>
<a id="gora-dynamodb--gora-dynamodb-properties-gora.properties"></a>

## Gora DynamoDB Properties - gora.properties

```
gora.datastore.default=org.apache.gora.dynamodb.store.DynamoDBStore
gora.datastore.autocreateschema=true
preferred.schema.name=Person
gora.dynamodb.mapping.file=/path/to/gora-dynamodb-mapping.xml
gora.dynamodb.client=sync
gora.dynamodb.consistent.reads=true
gora.dynamodb.endpoint=http://dynamodb.ap-northeast-1.amazonaws.com/
gora.dynamodb.serialization.type=dynamo
```

| Property Key | Property Value | Required | Description |
| --- | --- | --- | --- |
| gora.datastore.default | org.apache.gora.dynamodb.store.DynamoDBStore | Yes | Implementation of the storage class |
| gora.datastore.autocreateschema | true | No | Create the table if it doesn’t exist |
| preferred.schema.name | Person | Yes | Name of the DynamoDB table/schema |
| gora.dynamodb.mapping.file | /path/to/gora-dynamodb-mapping.xml | No | The XML mapping file to be used. Defaults to gora-dynamodb-mapping.xml |
| gora.dynamodb.client | sync | No | DynamoDB client type. It could be sync or async. |
| gora.dynamodb.consistent.reads | true | No | Default is eventual consistence i.e. false. |
| gora.dynamodb.endpoint | http://dynamodb.us-east-1.amazonaws.com/ | Yes | Set to geographically closest service endpoint. For accepted list, see [here](#gora-dynamodb--accepted) |
| gora.dynamodb.serialization.type | dynamo | No | Data store serialization type. It could be 'dynamo' or 'avro' |

<a id="gora-dynamodb--accepted-list-of-endpoints"></a>

#### Accepted list of endpoints

- http://dynamodb.ap-northeast-1.amazonaws.com/
- http://dynamodb.ap-northeast-2.amazonaws.com/
- http://dynamodb.eu-west-1.amazonaws.com/
- http://dynamodb.us-east-1.amazonaws.com/
- http://dynamodb.us-west-1.amazonaws.com/
- http://dynamodb.us-west-2.amazonaws.com/

<a id="gora-dynamodb--gora-dynamodb-mapppings-gora-dynamodb-mappingxml"></a>
<a id="gora-dynamodb--gora-dynamodb-mapppings-gora-dynamodb-mapping.xml"></a>

## Gora DynamoDB mapppings - gora-dynamodb-mapping.xml

Say we wished to map some user data and store it into DynamoDB.

```
<gora-otd>
    <table name="Person" readcunit="1" writecunit="1" package="org.apache.gora.dynamodb.example.generated">
    <attribute name="ssn" type="N" key="hash"/>
    <attribute name="date" type="S" key="hashrange"/>
    <attribute name="firstName" type="S"/>
    <attribute name="lastName" type="S"/>
    <attribute name="salary" type="N"/>
    <attribute name="visitedplaces" type="SS"/>
</gora-otd>
```

Within the `gora-otd` mapping configuration, only the 'table' child element is required.

<a id="gora-dynamodb--table"></a>

### Table

- a parameter containing the DynamoDB table `name` (String) e.g. Person
- a parameter containing the read capacity - `readcunit` (Number) e.g. 1 More about them [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#default-limits-throughput)
- a parameter containing the write capacity - `writecunit` (Number) e.g. 1
- a parameter containing the name of the `package` having the table (String)

<a id="gora-dynamodb--attributes"></a>

### Attributes

- a parameter containing the `name` e.g. name, dateOfBirth, ssn and salary
- a parameter containing the column `type` to which they belong e.g. (B/L/M/N/S/SS). For more, refer [here](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_AttributeValue.html)
- an optional parameter `key`. The key can be a hash key (partition key/primary key) or a hashrange key (sort key) (in case of composite primary key). The key parameter is left blank for non-key attributes. For more, refer [here](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html#HowItWorks.CoreComponents.PrimaryKey)

---

<a id="gora-hbase"></a>

<!-- source_url: https://gora.apache.org/current/gora-hbase.html -->

<!-- page_index: 10 -->

<a id="gora-hbase--overview"></a>

## Overview

This is the main documentation for the gora-hbase module. gora-hbase
module enables [Apache HBase](http://hbase.apache.org) backend support for Gora.

<a id="gora-hbase--goraproperties"></a>
<a id="gora-hbase--gora.properties"></a>

## gora.properties

- `gora.datastore.default=org.apache.gora.hbase.store.HBaseStore` - Implementation of the storage class
- `gora.datastore.autocreateschema=true` - Create the table if doesn't exist
- `gora.datastore.scanner.caching=1000` - HBase client cache that improves the scan in HBase (default 0)
- `hbase.client.autoflush.default=false` - HBase autoflushing. Enabling autoflush decreases write performance. Available since Gora 0.2. Defaults to disabled.

<a id="gora-hbase--gora-hbase-mappings"></a>

## Gora HBase mappings

Say we wished to map some Employee data and store it into the HBaseStore.

```
<gora-otd>
  <table name="Employee">
    <family name="info" 
            compression="$$$" 
            blockCache="$$$" 
            blockSize="$$$" 
            bloomFilter="$$$" 
            maxVersions="$$$" 
            timeToLive="$$$" 
            inMemory="$$$" />
  </table> 

  <class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" table="Employee">
    <field name="name" family="info" qualifier="nm"/>
    <field name="dateOfBirth" family="info" qualifier="db"/>
    <field name="ssn" family="info" qualifier="sn"/>
    <field name="salary" family="info" qualifier="sl"/>
    <field name="boss" family="info" qualifier="bs"/>
    <field name="webpage" family="info" qualifier="wp"/>
  </class>
</gora-otd>
```

Here you can see that we require the definition of two child elements within the
`gora-otd` mapping configuration, namely;

The table element; where we specify:

1. a parameter relating to the HBase table name (String) e.g. name=**"Employee"**, 2. a nested element containing the type and definition of families we wish to create within HBase. In this case we create one family **info** which could have a combination of any of the following parameters;

   **name** (String): family name e.g. info

   **compression** (String): the compression option to use in HBase. Please see [HBase documentation](http://hbase.apache.org/book/compression.html).

   **blockCache** (boolean): an LRU cache that contains three levels of block priority to allow for scan-resistance and in-memory ColumnFamilies. Please see [HBase documentation](https://hbase.apache.org/book/regionserver.arch.html#block.cache).

   **blockSize** (Integer): The blocksize can be configured for each ColumnFamily in a table, and this defaults to 64k. Larger cell values require larger blocksizes. There is an inverse relationship between blocksize and the resulting StoreFile indexes (i.e., if the blocksize is doubled then the resulting indexes should be roughly halved). Please see [HBase documentation](http://hbase.apache.org/book/perf.schema.html#schema.cf.blocksize).

   **bloomFilter** (String): Bloom Filters can be enabled per-ColumnFamily. We use `HColumnDescriptor.setBloomFilterType(NONE | ROW | ROWCOL)` to enable blooms per Column Family. Default = NONE for no bloom filters. If ROW, the hash of the row will be added to the bloom on each insert. If ROWCOL, the hash of the row + column family name + column family qualifier will be added to the bloom on each key insert. Please see [HBase documentation](http://hbase.apache.org/book/perf.schema.html#schema.bloom).

   **maxVersions** (Integer): The maximum number of row versions to store is configured per column family via `HColumnDescriptor`. The default for max versions is **3**. This is an important parameter because HBase does not overwrite row values, but rather stores different values per row by time (and qualifier). Excess versions are removed during major compaction's. The number of max versions may need to be increased or decreased depending on application needs. Please see [HBase documentation](http://hbase.apache.org/book/schema.versions.html).

   **timeToLive** (Integer): ColumnFamilies can set a TTL length in seconds, and HBase will automatically delete rows once the expiration time is reached. This applies to all versions of a row - even the current one. The TTL time encoded in the HBase for the row is specified in UTC. Please see [HBase documentation](https://hbase.apache.org/book/ttl.html).

   **inMemory** (Boolean): ColumnFamilies can optionally be defined as in-memory. Data is still persisted to disk, just like any other ColumnFamily. In-memory blocks have the highest priority in the Block Cache, but it is not a guarantee that the entire table will be in memory. Please see [HBase documentation](http://hbase.apache.org/book/perf.schema.html#cf.in.memory).

The class element where we specify of persistent fields which values should map to. This contains;

1. a parameter containing the Persistent class name e.g. **org.apache.gora.examples.generated.Employee**, 2. a parameter containing the keyClass e.g. **java.lang.String** which specifies the keys which map to the field values, 3. a parameter containing the Table name e.g. **Employee** which matches to the above Table definition, 4. finally nested child element(s) mapping fields which are to be persisted into HBase. These fields need to be configured such that they receive;

   a parameter containing the **name** e.g. (name, dateOfBirth, ssn and salary respectively),

   a parameter containing the column **family** to which they belong e.g. (all info in this case),

   an optional parameter **qualifier**, which enables more granular control over the data to be persisted into HBase.

---

<a id="gora-jcache"></a>

<!-- source_url: https://gora.apache.org/current/gora-jcache.html -->

<!-- page_index: 11 -->

<a id="gora-jcache--overview"></a>

## Overview

This is the main documentation for the gora-jcache module. gora-jcache
module enables [Hazelcast JCache](https://hazelcast.com/use-cases/caching/jcache-provider) caching support for Gora.
This implementation is based on Hazelcast JCache provider. This dataStore can act as wrapped caching layer for any other
persistent Apache Gora persistent dataStore.

<a id="gora-jcache--goraproperties"></a>
<a id="gora-jcache--gora.properties"></a>

## gora.properties

- `gora.cache.datastore.default` `( Mandatory )` - Caching dataStore to be used with persistent dataStore. If JCache dataStore is used as caching store
  assigned value should be **org.apache.gora.jcache.store.JCacheStore**
- `gora.datastore.default` `( Mandatory )` - Persistent back-end dataStore to be used with JCache caching dataStore.
- `gora.datastore.jcache.provider` `( Mandatory )` - Two possible values, whether to start JCache dataStore in Server mode or Client mode,

  - Server Mode
    **com.hazelcast.cache.impl.HazelcastServerCachingProvider**
  - Client Mode
    **com.hazelcast.client.cache.impl.HazelcastClientCachingProvider**
- `gora.datastore.jcache.hazelcast.config` - If JCache datastore is started in,

  - Server Mode
    This property to should point to Hazelcast Cluster member network configuration file related to
    forming Hazelcast cluster using members. Please see [Network configuration](http://docs.hazelcast.org/docs/3.5/manual/html/networkconfiguration.html).
  - Client Mode
    This property to should point s to Hazelcast client configuration file related to connecting related to already formed Hazelcast cluster.
    Please see [Client configuration](http://docs.hazelcast.org/docs/3.5/manual/html/javaclientconfiguration.html#java-client-configuration) `( Mandatory )`
- `jcache.auto.create.cache` - Whether force creating the cache at time JCache dataStore creation. Default is set to **false**.
- `jcache.cache.inmemory.format` - In memory for format for persistent bean resides in cache. Possible values,
  **BINARY, OBJECT, NATIVE** Please see [In memory format](http://docs.hazelcast.org/docs/3.5/manual/html/map-inmemoryformat.html).
- `jcache.read.through.enable` - Whether to fetch a missing cache entry from backend persistent dataStore. Default value is **true**.
- `jcache.write.through.enable` - Whether to push change of a cache entry to backend persistent dataStore. Default value is **true**.
- `jcache.statistics.enable` - Statistics like cache hits and misses are collected. Default value is **false**.
- `jcache.management.enable` - JMX beans are enabled and collected statistics are exposed over the beans.It doesn't automatically enables statistics collection.
  Default is set to false. Default JMX port opens on **9999**.
- `jcache.store.by.value.enable` - Whether to store key and values of data beans in means of store by value or store by reference. Default is **true** that means store by **value**.
- `jcache.cache.namespace` - Cache manager scope URI. This will allow different cache manager instances to share data among them if they are aligned with same scope.
  On opposite having two different scopes means such that each cache manager can isolate each other’s owned caches without any conflict.
  Please see [Scopes and Namespaces](http://docs.hazelcast.org/docs/3.5/manual/html/jcache-icache.html)
- `jcache.expire.policy` - Cache entry expiry policy. Possible values  **ACCESSED, CREATED, MODIFIED, TOUCHED**
  Please see [JCache expiry policy](http://docs.hazelcast.org/docs/3.5/manual/html/jcache-expirepolicy.html)
- `jcache.expire.policy.duration` - Cache entry expiry timeout in seconds.
- `jcache.eviction.policy` - Cache entry eviction policy. Possible values  **LRU, LFU, NONE, RANDOM**
  Please see [Hazelcast eviction policy](http://docs.hazelcast.org/docs/3.5/manual/html/jcache-eviction.html)
- `jcache.eviction.max.size.policy` - Measure of maximum cache size to apply eviction policy.
   **ENTRY\_COUNT, USED\_NATIVE\_MEMORY\_SIZE, USED\_NATIVE\_MEMORY\_PERCENTAGE, FREE\_NATIVE\_MEMORY\_SIZE, FREE\_NATIVE\_MEMORY\_PERCENTAGE**
- `jcache.eviction.size` - Maximum size as integer as a measure of max size policy criteria.

---

<a id="gora-couchdb"></a>

<!-- source_url: https://gora.apache.org/current/gora-couchdb.html -->

<!-- page_index: 12 -->

<a id="gora-couchdb--overview"></a>

## Overview

This is the main documentation for the gora-couchdb module. gora-couchdb module enables [Apache CouchDB](http://couchdb.apache.org/) backend support for Gora.

<a id="gora-couchdb--goraproperties"></a>
<a id="gora-couchdb--gora.properties"></a>

## gora.properties

- `gora.datastore.default=org.apache.gora.couchdb.store.CouchDBStore` - Implementation of the storage class
- `gora.datastore.couchdb.server=localhost` - Property pointing to the host where the server is running
- `gora.datastore.couchdb.port=5984` - Property pointing to the port where the server is running
- `gora.datastore.mapping.file=gora-couchdb-mapping.xml` - The XML mapping file to be used. If no value is used this defaults to.

<a id="gora-couchdb--gora-couchdb-mappings"></a>

## Gora CouchDB mappings

You should then create a gora-couchdb-mapping.xml which will describe how you want to store each of your Gora persistent objects:

```
<gora-otd>
    <class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" table="Employee">
   		<field name="name"/>
		<field name="dateOfBirth"/>
		<field name="ssn"/>
		<field name="salary"/>
		<field name="boss"/>
		<field name="webpage"/>
	</class>		
</gora-otd>		
```

Here you can see that we require the definition of two child elements within the `gora-otd` mapping configuration, namely;

The class element where we specify of persistent fields which values should map to. This contains;

1. a parameter containing the Persistent class name e.g. : **org.apache.gora.examples.generated.Employee** , 2. a parameter containing the keyClass e.g. **java.lang.String** which specifies the keys which map to the field values, 3. finally nested child element(s) mapping fields which are to be persisted into CouchDB. These fields need to be configured such that they receive; a parameter containing the name e.g. (name, dateOfBirth, ssn and salary respectively),

---

---

<a id="gora-metamodel"></a>

<!-- source_url: https://gora.apache.org/current/gora-metamodel.html -->

<!-- page_index: 13 -->

<a id="gora-metamodel--overview"></a>

## Overview

This is the main documentation for the gora-metamodel module. gora-metamodel
module enables [Apache MetaModel](http://metamodel.incubator.apache.org/) backend support for Gora.

MetaModel is a data access framework, providing a common interface for exploration
and querying of different types of datastores. This module aims to significantly
enhance Gora's query support and functionality in an attempt to query data regardless
of it's location.

<a id="gora-metamodel--goraproperties"></a>
<a id="gora-metamodel--gora.properties"></a>

## gora.properties

TODO

<a id="gora-metamodel--gora-metamodel-mappings"></a>

## Gora MetaModel mappings

TODO

---

---

<a id="gora-mongodb"></a>

<!-- source_url: https://gora.apache.org/current/gora-mongodb.html -->

<!-- page_index: 14 -->

<a id="gora-mongodb--overview"></a>

## Overview

This is the main documentation for the gora-mongodb module. gora-mongodb
module enables [MongoDB](http://www.mongodb.org) backend support for Gora.

This module has been tested with MongoDB Server [2.4.x](http://docs.mongodb.org/master/release-notes/2.4/)
and [2.6.x](http://docs.mongodb.org/master/release-notes/2.6/) series.
It will connect to remote MongoDB server(s) using standard [Java MongoDB Driver](http://docs.mongodb.org/ecosystem/drivers/java/)

<a id="gora-mongodb--goraproperties"></a>
<a id="gora-mongodb--gora.properties"></a>

## gora.properties

Here is a following sample `gora.properties` file to enable MongoStore:

```
# MongoDBStore properties
gora.datastore.default=org.apache.gora.mongodb.store.MongoStore
gora.mongodb.override_hadoop_configuration=false
gora.mongodb.mapping.file=/gora-mongodb-mapping.xml
gora.mongodb.servers=localhost
gora.mongodb.db=sample
```

Description of supported properties:

| Property | Example value | Required ? | Description |
| --- | --- | --- | --- |
| gora.datastore.default | org.apache.gora.mongodb.store.MongoStore | Yes | Implementation of the persistent Java storage class for MongoDB |
| gora.mongodb.override\_hadoop\_configuration | false | No | If true, it will allow properties to be overriden by configuration coming from Hadoop |
| gora.mongodb.mapping.file | /gora-mongodb-mapping.xml | No | The XML mapping file to be used. If no value is used this defaults to gora-mongodb-mapping.xml |
| gora.mongodb.servers | localhost:27017 | Yes | This value should specify the host:port for a running MongoDB node. Multiple values have to be separated by a coma character. |
| gora.mongodb.db | mytestdatabase | Yes | This value should specify the database for storage of documents. |
| gora.mongodb.login | login | No | Login that will be used to authenticate against MongoDB server. If blank, driver won't try authentication. |
| gora.mongodb.secret | password | No | Secret that will be used to authenticate against MongoDB server. |
| gora.mongodb.authentication.type | SCRAM-SHA-1 | No | Authentication mechanism type that will be used to authenticate against MongoDB server. |

<a id="gora-mongodb--gora-mongodb-mappings"></a>

## Gora MongoDB mappings

You should then create a `gora-mongodb-mapping.xml` which will describe **how** you want to
store each of your Gora persistent objects:

```
<gora-otd>

    <class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" document="employees">
        <field name="name" docfield="name" type="string"/>
        <field name="dateOfBirth" docfield="dateOfBirth" type="int64"/>
        <field name="ssn" docfield="ssn" type="string"/>
        <field name="salary" docfield="salary" type="int32"/>
        <field name="boss" docfield="boss" type="document"/>
        <field name="webpage" docfield="webpage" type="document"/>
    </class>

</gora-otd>
```

Each **class** element specifying persistent fields which values should map to. This element contains;

1. a parameter containing the Persistent class name e.g. **org.apache.gora.examples.generated.Employee**, 2. a parameter containing the keyClass e.g. **java.lang.String** which specifies the keys which map to the field values, 3. a parameter containing the MongoDB collection e.g. **employees** which will be used to persist each Gora object, 4. finally a child element(s) **field** which represent all fields which are to be persisted into MongoDB.
   These need to be configured such that they receive the following;

   a **name** attribute e.g. (name, dateOfBirth, ssn and salary respectively) which map to Gora field name,

   a **docfield** attribute containing the field's name in mapped Mongo document,

   a **type** attribute which allow transformation of Gora types into native MongoDB types.
   MongoDB use [BSON](https://gora.apache.org/current/bsonspec.org) is a binary serialization format to store documents
   and make remote procedure calls.

   Description of supported **type** values:

| Type value | Description |
| --- | --- |
| BINARY | Store as binary data |
| BOOLEAN | Store as boolean value |
| INT32 | Store as signed 32-bit integer |
| INT64 | Store as signed 64-bit integer |
| DOUBLE | Store as floating point |
| STRING | Store as UTF-8 string |
| DATE | Store as UTC datetime (ISODate) |
| LIST | Store as Array |
| DOCUMENT | Store as embedded document |
| OBJECTID | Store as ObjectId (12-byte) |

---

<a id="gora-solr"></a>

<!-- source_url: https://gora.apache.org/current/gora-solr.html -->

<!-- page_index: 15 -->

<a id="gora-solr--overview"></a>

## Overview

This is the main documentation for the gora-solr module. gora-solr
module enables [Apache Solr](http://lucene.apache.org/solr) backend support for Gora.

<a id="gora-solr--goraproperties"></a>
<a id="gora-solr--gora.properties"></a>

## gora.properties

- `gora.datastore.default=org.apache.gora.solr.store.SolrStore` - Implementation of the storage class
- `gora.datastore.autocreateschema=true` - Create the table if doesn't exist
- `gora.solrstore.solr.url=http://localhost:9876/solr` - The URL of the Solr server.
- `gora.solrstore.solr.config` - The `solrconfig.xml` file to be used.
- `gora.solrstore.solr.schema` - The `schema.xml` file to be used.
- `gora.solrstore.solr.batchSize` - A batch size unit (ArrayList) of SolrDocument's to be used for writing to Solr. A default value of **100** is used if this value is absent. This value must be of type **Integer**.
- `gora.solrstore.solr.solrjserver` - The solrj implementation to use. This has a default value of **http** for *HttpSolrServer*. Available options include **http** (*[HttpSolrServer](http://lucene.apache.org/solr/4_8_1/solr-solrj/index.html?org/apache/solr/client/solrj/impl/HttpSolrServer.html)*), **cloud** (*[CloudSolrServer](http://lucene.apache.org/solr/4_8_1/solr-solrj/index.html?org/apache/solr/client/solrj/impl/CloudSolrServer.html)*), **concurrent** (*[ConcurrentUpdateSolrServer](http://lucene.apache.org/solr/4_8_1/solr-solrj/index.html?org/apache/solr/client/solrj/impl/ConcurrentUpdateSolrServer.html)*) and **loadbalance** (*[LBHttpSolrServer](http://lucene.apache.org/solr/4_8_1/solr-solrj/index.html?org/apache/solr/client/solrj/impl/LBHttpSolrServer.html)*). This value must be of type **String**.
- `gora.solrstore.solr.commitWithin` - A batch commit unit for SolrDocument's used when making (commit) calls to Solr. A default value of 1000 is used if this value is absent. This value must be of type **Integer**.
- `gora.solrstore.solr.resultsSize` - The maximum number of results to return when we make a call to `org.apache.gora.solr.store.SolrStore#execute(Query)`. This value must be of type **Integer**.

<a id="gora-solr--gora-solr-mappings"></a>

## Gora Solr mappings

Say we wished to map some Employee data and store it into the SolrStore.

```
<gora-otd>
    <class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" table="Employee">
      <primarykey column="ssn"/>
      <field name="name" column="name"/>
      <field name="dateOfBirth" column="dateOfBirth"/>
      <field name="salary" column="salary"/>
      <field name="boss" column="boss"/>
      <field name="webpage" column="webpage"/>
    </class>
</gora-otd>
```

Here you can see that we require the definition of only one child element within the
`gora-otd` mapping configuration, namely;

The class element where we specify of persistent fields which values should map to. This contains;

1. a parameter containing the Persistent class **name** e.g. `org.apache.gora.examples.generated.Employee`, 2. a parameter containing the **keyClass** e.g. `java.lang.String` which specifies the keys which map to the field values, 3. a parameter containing the **Table name** e.g. `Employee`, 4. finally nested child element(s) mapping fields which are to be persisted into Solr. **We must provide a primary key for each object that we wish to persist into Solr.** Additional object fields need to be configured such that they receive;

   a parameter containing the **name** e.g. (name, dateOfBirth, ssn, salary, boss and webpage respectively),

   a parameter containing the **column family** to which they belong e.g. (all info in this case),

<a id="gora-solr--solr-schemaxml"></a>
<a id="gora-solr--solr-schema.xml"></a>

## Solr Schema.xml

`schema.xml` is an essential aspect of defining a storage and query model for your Solr data.

The Solr community maintain their own documentation relating to schema.xml, this can be found at <http://wiki.apache.org/solr/SchemaXml>.

```
<schema name="testexample" version="1.5">

  <fields>

    <!-- Common Fields -->
    <field name="_version_" type="long" indexed="true" stored="true"/>

    <!-- Employee Fields -->
    <field name="ssn"         type="string" indexed="true" stored="true" required="true" multiValued="false" /> 
    <field name="name"        type="string" indexed="true" stored="true" />
    <field name="dateOfBirth" type="long" stored="true" /> 
    <field name="salary"      type="int" stored="true" /> 
    <field name="boss"        type="binary" stored="true" />
    <field name="webpage"     type="binary" stored="true" />

  </fields>

  <uniqueKey>ssn</uniqueKey>

  <types>

    <fieldType name="string" class="solr.StrField" sortMissingLast="true" />
    <fieldType name="int" class="solr.TrieIntField" precisionStep="0" positionIncrementGap="0"/>
    <fieldType name="long" class="solr.TrieLongField" precisionStep="0" positionIncrementGap="0"/>
    <fieldtype name="binary" class="solr.BinaryField"/>

  </types>  

</schema>
```

<a id="gora-solr--solr-solrconfigxml"></a>
<a id="gora-solr--solr-solrconfig.xml"></a>

## Solr solrconfig.xml

Similar to `schema.xml` above, `solrconfig.xml` documentation is also maintained by the Solr community.

Please see an example configuration below but also please refer to <http://wiki.apache.org/solr/SolrConfigXml>.

```
<config>
  <luceneMatchVersion>LUCENE_40</luceneMatchVersion>
  <dataDir>${solr.data.dir:}</dataDir>
  <directoryFactory name="DirectoryFactory" 
                class="${solr.directoryFactory:solr.NRTCachingDirectoryFactory}"/> 
  <codecFactory class="solr.SchemaCodecFactory"/>
  <schemaFactory class="ClassicIndexSchemaFactory"/>
  <indexConfig>
    <lockType>${solr.lock.type:native}</lockType>
  </indexConfig>

  <jmx />

  <updateHandler class="solr.DirectUpdateHandler2">
    <updateLog>
      <str name="dir">${solr.ulog.dir:}</str>
    </updateLog>
  </updateHandler>

  <query>
    <maxBooleanClauses>1024</maxBooleanClauses>
    <filterCache class="solr.FastLRUCache"
             size="512"
             initialSize="512"
             autowarmCount="0"/>
    <queryResultCache class="solr.LRUCache"
                 size="512"
                 initialSize="512"
                 autowarmCount="0"/>
    <documentCache class="solr.LRUCache"
               size="512"
               initialSize="512"
               autowarmCount="0"/>
    <enableLazyFieldLoading>true</enableLazyFieldLoading>
    <queryResultWindowSize>20</queryResultWindowSize>
    <queryResultMaxDocsCached>200</queryResultMaxDocsCached>
    <listener event="newSearcher" class="solr.QuerySenderListener">
      <arr name="queries">
      </arr>
    </listener>
    <listener event="firstSearcher" class="solr.QuerySenderListener">
      <arr name="queries">
        <lst>
          <str name="q">static firstSearcher warming in solrconfig.xml</str>
        </lst>
      </arr>
    </listener>
    <useColdSearcher>false</useColdSearcher>
    <maxWarmingSearchers>2</maxWarmingSearchers>
  </query>

  <requestDispatcher handleSelect="false" >
    <requestParsers enableRemoteStreaming="true" 
                multipartUploadLimitInKB="2048000"
                formdataUploadLimitInKB="2048"
                addHttpRequestToContext="false"/>
    <httpCaching never304="true" />
  </requestDispatcher>

  <requestHandler name="/select" class="solr.SearchHandler">
    <lst name="defaults">
      <str name="echoParams">explicit</str>
      <int name="rows">10</int>
      <str name="df">ssn</str>
    </lst>
  </requestHandler>

  <requestHandler name="/query" class="solr.SearchHandler">
    <lst name="defaults">
      <str name="echoParams">explicit</str>
      <str name="wt">json</str>
      <str name="indent">true</str>
      <str name="df">ssn</str>
    </lst>
  </requestHandler>

  <requestHandler name="/get" class="solr.RealTimeGetHandler">
    <lst name="defaults">
      <str name="omitHeader">true</str>
    </lst>
  </requestHandler>

  <requestHandler name="/update" class="solr.UpdateRequestHandler">
  </requestHandler>
</config>
```

---

---

<a id="gora-aerospike"></a>

<!-- source_url: https://gora.apache.org/current/gora-aerospike.html -->

<!-- page_index: 16 -->

<a id="gora-aerospike--overview"></a>

## Overview

This is the main documentation for the gora-aerospike module. **gora-aerospike** module enables [Aerospike](http://www.aerospike.com/) backend support for Gora.

<a id="gora-aerospike--goraproperties"></a>
<a id="gora-aerospike--gora.properties"></a>

## gora.properties

- `gora.datastore.default=org.apache.gora.aerospike.store.AerospikeStore` - Implementation of the persistent Java storage class for Aerospike
- `gora.aerospikestore.server.ip=localhost` - Property pointing to the host where the server is running
- `gora.aerospikestore.server.port=3000` - Property pointing to the port where the server is running
- `gora.datastore.mapping.file=gora-aerospike-mapping.xml` - The XML mapping file to be used. If no value is used this defaults to gora-aerospike-mapping.xml
- `gora.aerospikestore.server.username=user_name` - An optional property defining the username of the server if available
- `gora.aerospikestore.server.password=password` - An optional property defining the password of the server if available

<a id="gora-aerospike--gora-aerospike-mappings"></a>

## Gora Aerospike mappings

You should then create a gora-aerospike-mapping.xml which will describe how you want to store each of your Gora persistent objects along with the read and write policies in Aerospike:

```
<gora-otd>
	<policy name="write" gen="NONE" recordExists="UPDATE" commitLevel="COMMIT_ALL" durableDelete="false"/>
	<policy name="read" priority="DEFAULT" consistencyLevel="CONSISTENCY_ONE" replica="SEQUENCE" maxRetries="2"/>

	<class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" set="Employee" namespace = "test">
		<field name="name" bin="name"/>
		<field name="dateOfBirth" bin="dateOfBirth"/>
		<field name="ssn" bin="ssn"/>
		<field name="salary" bin="salary"/>
		<field name="boss" bin="boss"/>
		<field name="webpage" bin="webpage"/>
	</class>		
</gora-otd>		
```

Here you can see that we require the definition of child elements within the `gora-otd` mapping configuration. We can define the classes and the policies.

Each **class** element should contain the following elements;

1. a parameter defining the Persistent class name e.g. **org.apache.gora.examples.generated.Employee**, 2. a parameter defining the keyClass e.g. **java.lang.String** which specifies the key which maps to the field values, 3. a parameter defining the Aerospike set e.g. **Employee** which will be used to persist each Gora object, 4. a parameter defining the Aerospike namespace e.g. **test** which will be used to persist each Gora object,

In addition, within the class field we should specify the fields and for which bin each field value maps to. We do not need to explicitly specify the type of each field, as the type is automatically detected in Aerospike server when creating the bin values. Thus each **field** should contain the field name and the corresponding bin it gets mapped to. e.g.  **name="webpage" bin="webpage"**

Further, we can define the policies on reading and writing data from/to the server.

Write policy can have following fields and each field values are the default values supported by [Aerospike Write Policy API](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/WritePolicy.html)

1. gen - [generation policy](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/GenerationPolicy.html) (values: EXPECT\_GEN\_EQUAL, EXPECT\_GEN\_GT, NONE)
2. recordExists - [record exists action](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/RecordExistsAction.html) (values: CREATE\_ONLY, REPLACE, REPLACE\_ONLY, UPDATE, UPDATE\_ONLY)
3. commitLevel - [commit level](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/CommitLevel.html) (values: COMMIT\_ALL, COMMIT\_MASTER)
4. durableDelete - [durable delete](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/WritePolicy.html#durableDelete) (values: true, false)
5. expiration - [record expiration](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/WritePolicy.html#expiration) (values: 0, 10)

Read policy can have following fields and each field values are the default values supported by [Aerospike Read Policy API](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/Policy.html)

1. priority - [priority policy](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/Priority.html) (values: DEFAULT, HIGH, LOW, MEDIUM)
2. consistencyLevel - [consistency level](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/ConsistencyLevel.html) (values: CONSISTENCY\_ALL, CONSISTENCY\_ONE)
3. replica - [replica](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/Replica.html) (values: MASTER, MASTER\_PROLES, RANDOM, SEQUENCE)
4. socketTimeout - [socket timeout](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/Policy.html#socketTimeout) (values: timeout in milliseconds)
5. totalTimeout - [total timeout](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/Policy.html#totalTimeout) (values: timeout in milliseconds)
6. timeoutDelay - [timeout delay](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/Policy.html#timeoutDelay) (values: timeout in milliseconds)
7. maxRetries - [max retries](https://www.aerospike.com/apidocs/java/com/aerospike/client/policy/Policy.html#maxRetries) (values: int of max num of retries)

---

<a id="gora-ignite"></a>

<!-- source_url: https://gora.apache.org/current/gora-ignite.html -->

<!-- page_index: 17 -->

<a id="gora-ignite--overview"></a>

## Overview

This is the main documentation for the gora-ignite module. **gora-ignite** module enables [Apache Ignite](https://ignite.apache.org/) backend support for Gora.

<a id="gora-ignite--gora-ignite-properties-goraproperties"></a>
<a id="gora-ignite--gora-ignite-properties-gora.properties"></a>

## Gora Ignite Properties - gora.properties

- `gora.datastore.default=org.apache.gora.ignite.store.IgniteStore` - Implementation of the persistent Java storage class for Ignite
- `gora.datastore.ignite.schema=PUBLIC` - Property pointing to the Schema of the Ignite instance
- `gora.datastore.ignite.host=localhost` - Property pointing to the host where the server is running
- `gora.datastore.ignite.port=10800` - Property pointing to the port where the server is running
- `gora.datastore.ignite.user=username` - An optional property defining the username of the server if available
- `gora.datastore.ignite.password=password` - An optional property defining the password of the server if available
- `gora.datastore.ignite.additionalConfigurations=` - An optional property defining additional configurations for the Ignite connection, format and available parameters: [Ignite JDBC Parameters](https://apacheignite-sql.readme.io/docs/jdbc-driver#section-parameters)

<a id="gora-ignite--gora-ignite-mappings-gora-ignite-mappingxml"></a>
<a id="gora-ignite--gora-ignite-mappings-gora-ignite-mapping.xml"></a>

## Gora Ignite mappings - gora-ignite-mapping.xml

You should then create a gora-ignite-mapping.xml which will describe how you want to store each of your Gora persistent objects and which primary keys you want to use:

```
<gora-otd>
  <class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" table="Employee">
    <primarykey column="pkssn" type="VARCHAR" />
    <field name="ssn" column="ssn" type="VARCHAR"/>
    <field name="name" column="name" type="VARCHAR"/>
    <field name="dateOfBirth" column="dateOfBirth" type="BIGINT"/>
    <field name="salary" column="salary" type="INT"/>
    <field name="boss" column="boss" type="BINARY"/>
    <field name="webpage" column="webpage" type="BINARY"/>
  </class>
</gora-otd>
```

Here you can see that we require the definition of child elements within the `gora-otd` mapping configuration.

Each **class** element should contain the following elements;

1. a parameter defining the Persistent class name e.g. **org.apache.gora.examples.generated.Employee**, 2. a parameter defining the keyClass e.g. **java.lang.String** which specifies the key which maps to the field values, 3. a parameter defining the table e.g. **Employee** which will be used to persist each Gora object

In addition, within the class element we should define two type of child elements: a primary key (**primarykey** tag) and some fields (**field** tag).

The primary key element defines which column is used by Ignite to identify the records stored in the DataStore. It has two costumizable parameters: **column** which defines the column's name of the table to be used as identifier for the records. And **type** which defines the data type of the aforementioned column.

The fields elements define the actual mapping between persistent object's attributes and the table's columns. These mapping have three customizable parameters: **name** which correspond to the object attribute's name. **column** which defines the column's name of the table to be assosiated with the attribute. And **type** which defines the data type of that column.

Notice that complex structures such 3-union fields are mapped using Binary fields through [Avro](https://avro.apache.org/) serialization.

<a id="gora-ignite--supported-data-types"></a>

## Supported Data types

Description of supported **type** values:

| Type value | Description |
| --- | --- |
| BINARY | Store as Byte[] |
| BOOLEAN | Store as Boolean |
| INT | Store as Integer |
| TINYINT | Store as Byte |
| SMALLINT | Store as Short |
| BIGINT | Store as Long |
| DECIMAL | Store as BigDecimal |
| DOUBLE | Store as Double |
| REAL | Store as Float |
| VARCHAR | Store as Unicode string |

A more detailed list of data types supported by Ignite and its equivalents in Java refer to [Ignite JDBC Data types](https://apacheignite-sql.readme.io/docs/data-types)

---

<a id="gora-kudu"></a>

<!-- source_url: https://gora.apache.org/current/gora-kudu.html -->

<!-- page_index: 18 -->

<a id="gora-kudu--overview"></a>

## Overview

This is the main documentation for the gora-kudu module. **gora-kudu** module enables [Apache Kudu](https://kudu.apache.org) backend support for Gora.

<a id="gora-kudu--gora-kudu-properties-goraproperties"></a>
<a id="gora-kudu--gora-kudu-properties-gora.properties"></a>

## Gora Kudu Properties - gora.properties

- `gora.datastore.default=org.apache.gora.kudu.store.KuduStore` - Implementation of the persistent Java storage class for Kudu
- `gora.datastore.kudu.masterAddresses=localhost:7051` - Comma-separated list of "host:port" pairs of the Kudu masters
- `gora.datastore.kudu.flushMode=AUTO_FLUSH_SYNC` - Flush mode for the Kudu-client session. More details here: <https://kudu.apache.org/apidocs/org/apache/kudu/client/SessionConfiguration.FlushMode.html>.
- `gora.datastore.kudu.flushInterval=1000` - Flush interval in ms, which will be used for the next scheduling.
- `gora.datastore.kudu.bossCount=1` - Maximum number of boss threads. Optional. If not provided, 1 is used.
- `gora.datastore.kudu.defaultAdminOperationTimeoutMs=1000` - Default timeout used for administrative operations (e.g. createTable, deleteTable, etc). Optional. If not provided, defaults to 30s. A value of 0 disables the timeout.
- `gora.datastore.kudu.defaultOperationTimeoutMs=1000` - Default timeout used for user operations (using sessions and scanners). Optional. If not provided, defaults to 30s. A value of 0 disables the timeout.
- `gora.datastore.kudu.defaultSocketReadTimeoutMs=10000` - Default timeout to use when waiting on data from a socket. Optional. If not provided, defaults to 10s. A value of 0 disables the timeout.
- `gora.datastore.kudu.clientStatistics=true` - Client's collection of statistics. Statistics are enabled by default.
- `gora.datastore.kudu.workerCount=2` - Maximum number of worker threads. Optional. If not provided, (2 \* the number of available processors) is used.

<a id="gora-kudu--gora-kudu-mappings-gora-kudu-mappingxml"></a>
<a id="gora-kudu--gora-kudu-mappings-gora-kudu-mapping.xml"></a>

## Gora Kudu mappings - gora-kudu-mapping.xml

You should then create a gora-kudu-mapping.xml which will describe how you want to store each of your Gora persistent objects and which primary keys you want to use:

```
<gora-otd>
	<table name ="Employee">
		<primaryKey column="pkssn" type="STRING" />
		<hashPartition numBuckets="8"/>
	</table>
	<class name="org.apache.gora.examples.generated.Employee" keyClass="java.lang.String" table="Employee">
		<field name="ssn" column="ssn" type="STRING"/>
		<field name="value" column="value" type="STRING"/>
		<field name="name" column="name" type="STRING"/>
		<field name="dateOfBirth" column="dateOfBirth" type="INT64"/>
		<field name="salary" column="salary" type="INT32"/>
		<field name="boss" column="boss" type="BINARY"/>
		<field name="webpage" column="webpage" type="BINARY"/>
	</class>
</gora-otd>
```

Here you can see that we require the definition of two child elements within the `gora-otd` mapping configuration: a class and a table.

<a id="gora-kudu--class"></a>

### Class

Each **class** element should contain the following elements;

1. a parameter defining the Persistent class name e.g. **org.apache.gora.examples.generated.Employee**, 2. a parameter defining the keyClass e.g. **java.lang.String** which specifies the key which maps to the field values, 3. a parameter defining the table e.g. **Employee** which will be used to persist each Gora object

In addition, within the class element we should define the fields to be mapped (field tag). The fields elements define the actual mapping between persistent object's attributes and the table's columns. These mapping have three customizable parameters: name which correspond to the object attribute's name. column which defines the column's name of the table to be associated with the attribute. And type which defines the data type of that column.

- The DECIMAL data type is parameterizable, so two additional attributes might be used in the XML mapping, scale and precision. Example:


```
  <field name="value" column="value" type="DECIMAL" scale=”1” precision=”1”/>
```

<a id="gora-kudu--table"></a>

### Table

Each **table** element should contain the following elements;

1. A **`primaryKey`** element defining which column is used by Kudu to identify the records stored in the DataStore. It has two attributes: **`column`** which defines the column's name of the table to be used as identifier for the records, and **`type`** which defines the data type of the aforementioned column.
2. A partition definition for the table, which could be either a hash partition or a range partition. For more information about Partitioning in Kudu refer to <https://kudu.apache.org/docs/schema_design.html#partitioning>

asdhfjalkjhf

Example for Hash partition:

```
    <hashPartition numBuckets="8"/>
```

The numBuckets attribute specifies the number of hash buckets to be used as partitions.

Example for Range partition:

```
    <rangePartition lower="" upper ="1000"/>

    <rangePartition lower="1000" upper =""/>
```

The lower and upper attributes define the boundaries of each partition. This partition is applied only on the primary key column of the table. Take into consideration that the lower bound is inclusive and the upper one is not.

<a id="gora-kudu--supported-data-types"></a>

## Supported Data types

Description of supported **type** values:

| Kudu datatype | Java datatype |
| --- | --- |
| BOOL | boolean |
| INT8 | byte |
| INT32 | short |
| INT16 | int |
| INT64 | long |
| UNIXTIME\_MICROS | java.sql.Timestamp |
| FLOAT | float |
| DOUBLE | double |
| DECIMAL | BigDecimal |
| STRING | String |
| BINARY | byte[] |

For more details about supported data types refer to <https://kudu.apache.org/docs/schema_design.html#column-design>

---

<a id="gora-pig"></a>

<!-- source_url: https://gora.apache.org/current/gora-pig.html -->

<!-- page_index: 19 -->

<a id="gora-pig--overview"></a>

## Overview

This is the main documentation for the gora-pig module. gora-pig module enables loading/storing data through Apache Gora in Pig scripts.

<a id="gora-pig--introduction"></a>

## Introduction

Apache Pig is a platform for analyzing large data sets that consists of a high-level language for expressing data analysis programs. With the module gora-pig we allow to operate on the data from Pig scripts using Apache Gora as storage.
The objective of this document is to describe the approach taken to implement a Pig adapter for Gora and show how to load/store the data.

Warning: Not all Gora modules are adapted to be used under Pig, since they have to implement loading the mapping defined from gora properties with the key "gora.mapping". At this moment are adapted **gora-hbase** and **gora-kudu**.

<a id="gora-pig--data-models"></a>

### Data models

Apache Gora is an Object Datastore Mapper which has its own data model inheriting Avro data types, and Apache Pig has its own data model. Because of this, it is needed an adaptation between both data models.

The following tables shows the different types and a possible conversions between Gora and Pig types.

<a id="gora-pig--primitivesimple-types"></a>
<a id="gora-pig--primitive-simple-types"></a>

#### Primitive/Simple types

| Gora | Pig |
| --- | --- |
| null | null |
| boolean | boolean |
| int (32-bit) | int (32-bit) |
| long (64-bit) | long (64-bit) |
| float (32-bit) | float (32-bit) |
| double (64-bit) | double (64-bit) |
| bytes (8-bit) | bytearray |
| string (unicode) | chararray (string UTF-8) |
| - | datetime |
| - | biginteger |
| - | bigdecimal |

<a id="gora-pig--complex-types"></a>

#### Complex types

| Gora | Pig |
| --- | --- |
| record | tuple |
| enum | int |
| array | bag |
| map<String, 'b> | map<chararray, 'b> |
| union | [the non-null type] |
| fixed | - |

Since `datetime`, `biginteger` and `bigdecimal` aren't handled by Apache Gora, it isn't possible to persist those types.

For unions, only nullable fields (`union:[null, type]`) are handled. Fixed type is not handled.

Notice that Gora's records are converted into Pig's tuples, and arrays into bags (index matters). When persisting, those types are the expected when checking the schemas.

##Reading from datastores

The storage GoraStorage is the responsible for loading and persisting entities. The simplest syntax to load data is the following:

```
    register gora/*.jar;
    webpage = LOAD '.' USING org.apache.gora.pig.GoraStorage('{
      "persistentClass": "admin.WebPage",
      "fields": "baseUrl,status,content"
    }') ;
```

It loads the fields `baseUrl`, `status` and `content` **(must not have spaces!)** for the entity `WebPage`.

The files `gora.properties`, `gora-xxx-mapping.xml` and support files are provided through the classpath to Pig client. They must be included inside one of the registered `*.jar` files.

The complete `LOAD` options allows to configure the options for each storage and avoid using the global configuration files when multiple different stores are used:

```
    webpage = LOAD '.' USING org.apache.gora.pig.GoraStorage('{
      "persistentClass": "admin.WebPage",
      "keyClass": "java.lang.String",
      "fields": "*",
      "goraProperties": "",
      "mapping": "",
      "configuration": {}
    }') ;
```

<a id="gora-pig--full-options-for-load"></a>

### Full options for LOAD

The configuration options are the following:

- **persistentClass** (mandatory): The full name of the persistent class including the namespace.
- **keyClass**: The full name of the key class. **By now only `java.lang.String` is supported**.
- **fields** (mandatory): Comma-separated list of field names (without spaces!) or '\*' to load all fields.
- **goraProperties**: String with gora.properties configuration. Each line must be separated by \n.
- **mapping**: XML mapping for the entities loaded. Each line must be separated by \n and escaped quotes as \"
- **configuration**: object with a map from keys to values that will be added to the configuration.

In JSON Strings, line feeds must be escaped as \n.

An example of Gora properties value is:

```
    "gora.datastore.default=org.apache.gora.hbase.store.HBaseStore\\ngora.datastore.autocreateschema=true\\ngora.hbasestore.scanner.caching=4"
```

An example of mapping is:

```
    "<?xml version=\\"1.0\\" encoding=\\"UTF-8\\"?>\\n<gora-odm>\\n<table name=\\"webpage\\">\\n<family name=\\"f\\" maxVersions=\\"1\\"/>\\n</table>\\n<class table=\\"webpage\\" keyClass=\\"java.lang.String\\" name=\\"admin.WebPage\\">\\n<field name=\\"baseUrl\\" family=\\"f\\" qualifier=\\"bas\\"/>\\n<field name=\\"status\\" family=\\"f\\" qualifier=\\"st\\"/>\\n<field name=\\"content\\" family=\\"f\\" qualifier=\\"cnt\\"/>\\n</class>\\n</gora-odm>"
```

The configuration options is a JSON object with string key-values like this:

```
    {
      "hbase.zookeeper.quorum": "hdp4,hdp1,hdp3",
      "zookeeper.znode.parent": "/hbase-unsecure"
    }
```

<a id="gora-pig--writing-to-datastores"></a>

## Writing to datastores

To write a Pig relation to a datastore, the command is:

```
    STORE webpages INTO '.' USING org.apache.gora.pig.GoraStorage('{
      "persistentClass": "",
      "fields": "",
      "goraProperties": "",
      "mapping": "",
      "configuration": {}
    }') ;
```

All the fields listed in "fields" will be persisted. If a field listed is missing in the relation the process will fail with an exception. Only the fields listed will be updated if the element already exists.

<a id="gora-pig--deleting-elements"></a>

## Deleting elements

To delete elements of a collection is `GoraDeleteStorage`. Given a relation with schema `(key:chararray)` rows, the following will delete all rows with that keys:

```
    STORE webpages INTO '.' USING org.apache.gora.pig.GoraDeleteStorage('{
      "persistentClass": "",
      "goraProperties": "",
      "mapping": "",
      "configuration": {}
    }') ;
```

---

<a id="tutorial"></a>

<!-- source_url: https://gora.apache.org/current/tutorial.html -->

<!-- page_index: 20 -->

<a id="tutorial--gora-tutorial"></a>

# Gora Tutorial

Author : Enis Söztutar, enis [at] apache [dot] org

<a id="tutorial--introduction"></a>

## Introduction

This is the official tutorial for Apache Gora. For this tutorial, we
will be implementing a system to store our web server logs in Apache HBase, and analyze the results using Apache Hadoop and store the results either in HSQLDB or MySQL.

In this tutorial we will first look at how to set up the environment and
configure Gora and the data stores. Later, we will go over the data we will use and
define the data beans that will be used to interact with the persistency layer.
Next, we will go over the API of Gora to do some basic tasks such as storing objects, fetching and querying objects, and deleting objects. Last, we will go over an example
program which uses Hadoop MapReduce to analyze the web server logs, and discuss the Gora
MapReduce API in some detail.

<a id="tutorial--table-of-content"></a>

## Table of Content

<a id="tutorial--introduction-to-gora"></a>

## Introduction to Gora

The Apache Gora open source framework provides an in-memory data
model and persistence for big data. Gora supports persisting to
column stores, key value stores, document stores and RDBMSs, and
analyzing the data with extensive Apache Hadoop MapReduce support. In Avro, the
beans to hold the data and RPC interfaces are defined using a JSON
schema. In mapping the data beans to data store specific settings, Gora depends on mapping files, which are specific to each data store.
Unlike other OTD (Object-to-Datastore) mapping implementations, in Gora the data bean to data store
specific schema mapping is explicit. This has the advantage that, when using data models such as HBase and Cassandra, you can always
know how the values are persisted.

Gora has a modular architecture. Most of the data stores in Gora, has it's own module, such as gora-hbase, gora-cassandra, and gora-sql. In your projects, you need to only include
the artifacts from the modules you use. You can consult the [quick start](#quickstart)
for setting up your project.

<a id="tutorial--setting-up-gora"></a>

## Setting up Gora

As a first step, we need to download and compile the Gora source code. The source codes
for the tutorial is in the gora-tutorial module. If you have
already downloaded Gora, that's cool, otherwise, please go
over the steps at the [quickstart](#quickstart) guide for
how to download and compile Gora.

Now, after the source code for Gora is at hand, let's have a look at the files under the
directory gora-tutorial.

```
$ cd gora-tutorial
$ tree

|-- conf
|   |-- gora-hbase-mapping.xml
|   |-- gora-sql-mapping.xml
|   `-- gora.properties
|
|-- pom.xml
| 
`-- src
    |-- examples
    |   `-- java
    |-- main
    |   |-- avro
    |   |   |-- metricdatum.json
    |   |   `-- pageview.json
    |   |-- java
    |   |   `-- org
    |   |       `-- apache
    |   |           `-- gora
    |   |               `-- tutorial
    |   |                   `-- log
    |   |                       |-- KeyValueWritable.java
    |   |                       |-- LogAnalytics.java
    |   |                       |-- LogAnalyticsSpark.java
    |   |                       |-- LogManager.java
    |   |                       |-- TextLong.java
    |   |                       `-- generated
    |   |                           |-- MetricDatum.java
    |   |                           `-- Pageview.java
    |   `-- resources
    |       `-- access.log.tar.gz
    `-- test
        |-- conf
        `-- java
```

Since gora-tutorial is a top level module of Gora, it depends on the directory
structure imposed by Gora's main build scripts (pom.xml for Maven). The Java source code resides in directory
`src/main/java/`, avro schemas in `src/main/avro/`, and data in `src/main/resources/`.

<a id="tutorial--setting-up-hbase"></a>

## Setting up HBase

For this tutorial we will be using [HBase](http://hbase.apache.org) to
store the logs. For those of you not familiar with HBase, it is a NoSQL
column store with an architecture very similar to Google's BigTable.

If you don't already have already HBase setup, you can go over the steps at
[HBase Overview](http://hbase.apache.org/book/quickstart.html)
documentation. Gora aims to support the most recent HBase versions however if you
find compatibility problems please [get in touch](https://gora.apache.org/mailing_lists.html).
So download an [HBase release](http://www.apache.org/dyn/closer.cgi/hbase/).
After extracting the file, cd to the hbase-${dist} directory and start the HBase server.

```
$ bin/start-hbase.sh
```

and make sure that HBase is available by using the Hbase shell.

```
$ bin/hbase shell
```

<a id="tutorial--configuring-gora"></a>

## Configuring Gora

Gora is configured through a file in the classpath named gora.properties.
We will be using the following file `gora-tutorial/conf/gora.properties`

```
  gora.datastore.default=org.apache.gora.hbase.store.HBaseStore
  gora.datastore.autocreateschema=true
```

This file states that the default store will be HBaseStore, and schemas(tables) should be automatically created.
More information for configuring different settings in `gora.properties`
can be found [here](#gora-conf).

<a id="tutorial--modeling-the-data"></a>

## Modeling the data

For this tutorial, we will be parsing and storing the logs of a web server.
Some example logs are at `src/main/resources/access.log.tar.gz`, which
belongs to the (now shutdown) server at <http://www.buldinle.com/>.
Example logs contain 10,000 lines, between dates 2009/03/10 - 2009/03/15.
The first thing, we need to do is to extract the logs.

```
$ tar zxvf src/main/resources/access.log.tar.gz -C src/main/resources/
```

You can also use your own log files, given that the log
format is [Combined Log Format](http://httpd.apache.org/docs/current/logs.html).
Some example lines from the log are:

```
88.254.190.73 - - [10/Mar/2009:20:40:26 +0200] "GET / HTTP/1.1" 200 43 "http://www.buldinle.com/" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; GTB5; .NET CLR 2.0.50727; InfoPath.2)
78.179.56.27 - - [11/Mar/2009:00:07:40 +0200] "GET /index.php?i=3&amp;a=1__6x39kovbji8&amp;k=3750105 HTTP/1.1" 200 43 "http://www.buldinle.com/index.php?i=3&amp;a=1__6X39Kovbji8&amp;k=3750105" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; OfficeLiveConnector.1.3; OfficeLivePatch.0.0)
78.163.99.14 - - [12/Mar/2009:18:18:25 +0200] "GET /index.php?a=3__x7l72c&amp;k=4476881 HTTP/1.1" 200 43 "http://www.buldinle.com/index.php?a=3__x7l72c&amp;k=4476881" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; InfoPath.1)
```

The first fields in order are: User's ip, ignored, ignored, Date and
time, HTTP method, URL, HTTP Method, HTTP status code, Number of bytes
returned, Referrer, and User Agent.

<a id="tutorial--defining-data-beans"></a>

## Defining data beans

Data beans are the main way to hold the data in memory and persist in Gora. Gora
needs to explicitly keep track of the status of the data in memory, so
we use [Apache Avro](http://avro.apache.org) for defining the beans. Using
Avro gives us the possibility to explicitly keep track of an object's persistent state
and a way to serialize an object's data.
Defining data beans is a very easy task, but for the exact syntax please
consult the [Avro Specification](http://avro.apache.org/docs/current/spec.html).
First, we need to define the bean Pageview to hold a
single URL access in the logs. Let's go over the class at `src/main/avro/pageview.json`

```
 {
  "type": "record",
  "name": "Pageview",
  "namespace": "org.apache.gora.tutorial.log.generated",
  "fields" : [
    {"name": "url", "type": "string"},
    {"name": "timestamp", "type": "long"},
    {"name": "ip", "type": "string"},
    {"name": "httpMethod", "type": "string"},
    {"name": "httpStatusCode", "type": "int"},
    {"name": "responseSize", "type": "int"},
    {"name": "referrer", "type": "string"},
    {"name": "userAgent", "type": "string"}
  ]
}
```

Avro schemas are declared in JSON.
[Records](http://avro.apache.org/docs/current/spec.html#schema_record)
are defined with type "record", with a name as the name of the class, and a
namespace which is mapped to the package name in Java. The fields
are listed in the "fields" element. Each field is given with its type.

<a id="tutorial--compiling-avro-schemas"></a>

## Compiling Avro Schemas

The next step after defining the data beans is to compile the schemas
into Java classes. For that we will use the [GoraCompiler](#compiler).
Invoke the Gora compiler from the top-level Gora directory with:

```
$ bin/gora goracompiler
```

results in:

```
$ Usage: GoraCompiler <schema file> <output dir> [-license <id>] <schema file> - individual avsc file to be compiled or a directory path containing avsc files <output dir> - output directory for generated Java files [-license <id>] - the preferred license header to add to the generated Java file. Current options include; ASLv2 (Apache Software License v2.0) AGPLv3 (GNU Affero General Public License) CDDLv1 (Common Development and Distribution License v1.0) FDLv13 (GNU Free Documentation License v1.3) GPLv1 (GNU General Public License v1.0) GPLv2 (GNU General Public License v2.0) GPLv3 (GNU General Public License v3.0) LGPLv21 (GNU Lesser General Public License v2.1) LGPLv3 (GNU Lesser General Public License v2.1)
```

so we will issue :

```
$ bin/gora goracompiler gora-tutorial/src/main/avro/pageview.json gora-tutorial/src/main/java/
```

to compile the Pageview class into `gora-tutorial/src/main/java/org/apache/gora/tutorial/log/generated/Pageview.java`.
This will use the default license header which is ASLv2 for licensing the generated data beans.
However, the tutorial java classes are already committed and present within SVN, so you do not need to do that now.

The Gora compiler extends Avro's SpecificCompiler to convert a JSON definition
into a Java class. Generated classes extend the Persistent interface.
Most of the methods of the Persistent interface deal with bookkeeping for
persistence and state tracking, so most of the time they are not used explicitly by the
user. Now, let's look at the internals of the generated class Pageview.java.

```
public class Pageview extends PersistentBase {

private Utf8 url;
private long timestamp;
private Utf8 ip;
private Utf8 httpMethod;
private int httpStatusCode;
private int responseSize;
private Utf8 referrer;
private Utf8 userAgent;

...

public static final Schema _SCHEMA = Schema.parse("{\"type\":\"record\", ... ");
  public static enum Field {
  URL(0,"url"),
  TIMESTAMP(1,"timestamp"),
  IP(2,"ip"),
  HTTP_METHOD(3,"httpMethod"),
  HTTP_STATUS_CODE(4,"httpStatusCode"),
  RESPONSE_SIZE(5,"responseSize"),
  REFERRER(6,"referrer"),
  USER_AGENT(7,"userAgent"),
  ;
  private int index;
  private String name;
  Field(int index, String name) {this.index=index;this.name=name;}
  public int getIndex() {return index;}
  public String getName() {return name;}
  public String toString() {return name;}
  };
public static final String[] _ALL_FIELDS = {"url","timestamp","ip","httpMethod"
  ,"httpStatusCode","responseSize","referrer","userAgent",};

...
}
```

We can see the actual field declarations in the class. Note that Avro uses Utf8
class as a placeholder for string fields. We can also see the embedded Avro
Schema declaration and an inner enum named Field. The enum and
the \_ALL\_FIELDS fields will come in handy when we query the datastore for specific fields.

<a id="tutorial--defining-data-store-mappings"></a>

## Defining data store mappings

Gora is designed to flexibly work with various types of data modeling, including column stores(such as HBase, Cassandra, etc), SQL databases, flat files(binary, JSON, XML encoded), and key-value stores. The mapping between the data bean and
the data store is thus defined in XML mapping files. Each data store has its own
mapping format, so that data-store specific settings can be leveraged more easily.
The mapping files declare how the fields of the classes declared in Avro schemas
are serialized and persisted to the data store.

<a id="tutorial--hbase-mappings"></a>

### HBase mappings

HBase mappings are stored at file named `gora-hbase-mapping.xml`.
For this tutorial we will be using the file `gora-tutorial/conf/gora-hbase-mapping.xml`.

```
<gora-otd>
  <table name="Pageview"> <!-- optional descriptors for tables -->
    <family name="common"> <!-- This can also have params like compression, bloom filters -->
    <family name="http"/>
    <family name="misc"/>
  </table>

  <class name="org.apache.gora.tutorial.log.generated.Pageview" keyClass="java.lang.Long" table="Pageview">
   <field name="url" family="common" qualifier="url"/>
   <field name="timestamp" family="common" qualifier="timestamp"/>
   <field name="ip" family="common" qualifier="ip" />
   <field name="httpMethod" family="http" qualifier="httpMethod"/>
   <field name="httpStatusCode" family="http" qualifier="httpStatusCode"/>
   <field name="responseSize" family="http" qualifier="responseSize"/>
   <field name="referrer" family="misc" qualifier="referrer"/>
   <field name="userAgent" family="misc" qualifier="userAgent"/>
  </class>

  ...

</gora-otd>  
```

Every mapping file starts with the top level element `<gora-otd>`.
Gora HBase mapping files can have two type of child elements, table and
class declarations. All of the table and class definitions should be
listed at this level.

The table declaration is optional and most of the time, Gora infers the table
declaration from the class sub elements. However, some of the HBase
specific table configuration such as compression, blockCache, etc can be given here, if Gora is used to auto-create the tables. The exact syntax for the file can be found
[here](#gora-hbase).

In Gora, data store access is always
done in a key-value data model, since most of the target backends support this model.
DataStore API expects to know the class names of the key and persistent classes, so that
they can be instantiated. The key value pair is declared in the class element.
The name attribute is the fully qualified name of the class, and the keyClass attribute is the fully qualified class name of the key class.

Children of the `class` element are `field`
elements. Each field element has a name and family attribute, and
an optional qualifier attribute. name attribute contains the name
of the field in the persistent class, and family declares the column family
of the HBase data model. If the qualifier is not given, the name of the field is used
as the column qualifier. Note that map and array type fields are stored in unique column
families, so the configuration should be list unique column families for each map and
array type, and no qualifier should be given. The exact data model is discussed further
at the [gora-hbase](#gora-hbase) documentation.

<a id="tutorial--basic-api"></a>

## Basic API

<a id="tutorial--parsing-the-logs"></a>

### Parsing the logs

Now that we have the basic setup, we can see Gora API in action. As you can notice below the API
is pretty simple to use. We will be using the class LogManager (which is located at
`gora-tutorial/src/main/java/org/apache/gora/tutorial/log/LogManager.java`) for parsing
and storing the logs, deleting some lines and querying.

First of all, let us look at the constructor. The only real thing it does is to call the
init() method. init() method constructs the
DataStore instance so that it can be used by the LogManager's methods.

```
public LogManager() {try {init(); } catch (IOException ex) {throw new RuntimeException(ex);}} private void init() throws IOException {dataStore = DataStoreFactory.getDataStore(Long.class, Pageview.class, new Configuration());}
```

DataStore is probably the most important class in the Gora API.
DataStore handles actual object persistence. Objects can be persisted, fetched, queried or deleted by the DataStore methods. Every data store that Gora supports, defines its own subclass
of the DataStore class. For example gora-hbase module defines HBaseStore, and
gora-sql module defines SqlStore. However, these subclasses are not explicitly
used by the user.

DataStores always have associated key and value(persistent) classes. Key class is the class of the keys of the
data store, and the value is the actual data bean's class. The value class is almost always generated by
Avro schema definitions using the Gora compiler.

Data store objects are created by DataStoreFactory. It is necessary to
provide the key and value class. The datastore class is optional, and if not specified it will be read from the configuration (`gora.properties`).

For this tutorial, we have already defined the avro schema to use and compiled
our data bean into Pageview class. For keys in the data store, we will be using Longs.
The keys will hold the line of the pageview in the data file.

Next, let's look at the main function of the LogManager class.

```
public static void main(String[] args) throws Exception {
  if(args.length > 2) {
    System.err.println(USAGE);
    System.exit(1);
  }

  LogManager manager = new LogManager();

  if("-parse".equals(args[0])) {
    manager.parse(args[1]);
  } else if("-query".equals(args[0])) {
  if(args.length == 2) 
    manager.query(Long.parseLong(args[1]));
  else 
    manager.query(Long.parseLong(args[1]), Long.parseLong(args[2]));
  } else if("-delete".equals(args[0])) {
    manager.delete(Long.parseLong(args[1]));
  } else if("-deleteByQuery".equalsIgnoreCase(args[0])) {
    manager.deleteByQuery(Long.parseLong(args[1]), Long.parseLong(args[2]));
  } else {
    System.err.println(USAGE);
    System.exit(1);
  }

  manager.close();
}
```

We can use the example log manager program from the command line (in the top level Gora directory):

```
$ bin/gora logmanager
```

which lists the usage as:

```
LogManager -parse <input_log_file>
       -get <lineNum>
       -query <lineNum>
       -query <startLineNum> <endLineNum>
       -delete <lineNum>
       -deleteByQuery <startLineNum> <endLineNum>
```

So to parse and store our logs located at `gora-tutorial/src/main/resources/access.log`, we will issue:

```
$ bin/gora logmanager -parse gora-tutorial/src/main/resources/access.log
```

This should output something like:

```
10/09/30 18:30:17 INFO log.LogManager: Parsing file:gora-tutorial/src/main/resources/access.log
10/09/30 18:30:23 INFO log.LogManager: finished parsing file. Total number of log lines:10000
```

Now, let's look at the code which parses the data and stores the logs.

```
private void parse(String input) throws IOException, ParseException {
  BufferedReader reader = new BufferedReader(new FileReader(input));
  long lineCount = 0;
  try {
    String line = reader.readLine();
    do {
      Pageview pageview = parseLine(line);
    
      if(pageview != null) {
        //store the pageview 
        storePageview(lineCount++, pageview);
      }
    
      line = reader.readLine();
    } while(line != null);
  
  } finally {
  reader.close();  
  }
}
```

The file is iterated line-by-line. Notice that the parseLine(line)
function does the actual parsing converting the string to a Pageview object
defined earlier.

```
private Pageview parseLine(String line) throws ParseException {StringTokenizer matcher = new StringTokenizer(line); //parse the log line String ip = matcher.nextToken(); ...
//construct and return pageview object Pageview pageview = new Pageview(); pageview.setIp(new Utf8(ip)); pageview.setTimestamp(timestamp); ...
return pageview;}
```

parseLine() uses standard StringTokenizers for the job
and constructs and returns a Pageview object.

<a id="tutorial--storing-objects-in-the-datastore"></a>

### Storing objects in the DataStore

If we look back at the parse() method above, we can see that the
Pageview objects returned by parseLine() are stored via
storePageview() method.

The storePageview() method is where magic happens, but if we look at the code, we can see that it is dead simple.

```
/** Stores the pageview object with the given key */
private void storePageview(long key, Pageview pageview) throws IOException {
  dataStore.put(key, pageview);
}
```

All we need to do is to call the put() method, which expects a long as key and an instance of Pageview
as a value.

<a id="tutorial--closing-the-datastore"></a>

### Closing the DataStore

DataStore implementations can do a lot of caching for performance.
However, this means that data is not always flushed to persistent storage all the times.
So we need to make sure that upon finishing storing objects, we need to close the datastore
instance by calling it's close() method.
LogManager always closes it's datastore in it's own close() method.

```
private void close() throws IOException {
  //It is very important to close the datastore properly, otherwise
  //some data loss might occur.
  if(dataStore != null)
  dataStore.close();
}
```

If you are pushing a lot of data, or if you want your data to be accessible before closing
the data store, you can also the flush()
method which, as expected, flushes the data to the underlying data store. However, the actual flush
semantics can vary by the data store backend. For example, in SQL flush calls commit()
on the jdbc Connection object, whereas in Hb=Base, `HTable#flush()` is called.
Also note that even if you call flush() at the end of all data manipulation operations, you still need to call the close() on the datastore.

<a id="tutorial--persisted-data-in-hbase"></a>

## Persisted data in HBase

Now that we have stored the web access log data in HBase, we can look at
how the data is stored at HBase. For that, start the HBase shell.

```
$ cd ../hbase-${version}
$ bin/hbase shell
```

If you have a fresh HBase installation, there should be one table.

```
hbase(main):010:0> list

AccessLog                                                                                                     
1 row(s) in 0.0470 seconds
```

Remember that AccessLog is the name of the table we specified at
gora-hbase-mapping.xml. Looking at the contents of the table:

```
hbase(main):010:0> scan 'AccessLog', {LIMIT=>1}

ROW                          COLUMN+CELL                                                                      
 \x00\x00\x00\x00\x00\x00\x0 column=common:ip, timestamp=1285860617341, value=88.240.129.183                  
 0\x00                                                                                                        
 \x00\x00\x00\x00\x00\x00\x0 column=common:timestamp, timestamp=1285860617341, value=\x00\x00\x01\x1F\xF1\xAEl
 0\x00                       P                                                                                
 \x00\x00\x00\x00\x00\x00\x0 column=common:url, timestamp=1285860617341, value=/index.php?a=1__wwv40pdxdpo&amp;k=2
 0\x00                       18978                                                                            
 \x00\x00\x00\x00\x00\x00\x0 column=http:httpMethod, timestamp=1285860617341, value=GET                       
 0\x00                                                                                                        
 \x00\x00\x00\x00\x00\x00\x0 column=http:httpStatusCode, timestamp=1285860617341, value=\x00\x00\x00\xC8      
 0\x00                                                                                                        
 \x00\x00\x00\x00\x00\x00\x0 column=http:responseSize, timestamp=1285860617341, value=\x00\x00\x00+           
 0\x00                                                                                                        
 \x00\x00\x00\x00\x00\x00\x0 column=misc:referrer, timestamp=1285860617341, value=http://www.buldinle.com/inde
 0\x00                       x.php?a=1__WWV40pdxdpo&amp;k=218978                                                  
 \x00\x00\x00\x00\x00\x00\x0 column=misc:userAgent, timestamp=1285860617341, value=Mozilla/4.0 (compatible; MS
 0\x00                       IE 6.0; Windows NT 5.1)
```

The output shows all the columns matching the first line with key 0. We can see
the columns common:ip, common:timestamp, common:url, etc. Remember that
these are the columns that we have described in the `gora-hbase-mapping.xml` file.

You can also count the number of entries in the table to make sure that all the records
have been stored.

```
hbase(main):010:0> count 'AccessLog'
  ... 
  10000 row(s) in 1.0580 seconds
```

<a id="tutorial--fetching-objects-from-data-store"></a>

## Fetching objects from data store

Fetching objects from the data store is as easy as storing them. There are essentially
two methods for fetching objects. First one is to fetch a single object given it's key. The
second method is to run a query through the data store.

To fetch objects one by one, we can use one of the overloaded
`get()` methods.
The method with signature `get(K key)` returns the object corresponding to the given key fetching all the
fields. On the other hand `get(K key, String[] fields)` returns the object corresponding to the
given key, but fetching only the fields given as the second argument.

When run with the argument -get LogManager class fetches the pageview object
from the data store and prints the results.

```
/** Fetches a single pageview object and prints it*/
private void get(long key) throws IOException {
  Pageview pageview = dataStore.get(key);
  printPageview(pageview);
}
```

To display the 42nd line of the access log :

```
$ bin/gora logmanager -get 42

org.apache.gora.tutorial.log.generated.Pageview@321ce053 {
  "url":"/index.php?i=0&amp;a=1__rntjt9z0q9w&amp;k=398179"
  "timestamp":"1236710649000"
  "ip":"88.240.129.183"
  "httpMethod":"GET"
  "httpStatusCode":"200"
  "responseSize":"43"
  "referrer":"http://www.buldinle.com/index.php?i=0&amp;a=1__RnTjT9z0Q9w&amp;k=398179"
  "userAgent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"
}
```

<a id="tutorial--querying-objects"></a>

## Querying objects

DataStore API defines a Query interface to query the objects at the data store.
Each data store implementation can use a specific implementation of the Query interface. Queries are
instantiated by calling `DataStore#newQuery()`. When the query is run through the datastore, the results
are returned via the Result interface. Let's see how we can run a query and display the results below in the
the LogManager class.

```
/** Queries and prints pageview object that have keys between startKey and endKey*/
private void query(long startKey, long endKey) throws IOException {
  Query<Long, Pageview> query = dataStore.newQuery();
  //set the properties of query
  query.setStartKey(startKey);
  query.setEndKey(endKey);

  Result<Long, Pageview> result = query.execute();

  printResult(result);
}
```

After constructing a Query, its properties
are set via the setter methods. Then calling `query.execute()` returns
the `Result` object.

Result interface allows us to iterate the results one by one by calling the
`next()` method. The `getKey()` method returns the current key and `get()`
returns current persistent object.

```
private void printResult(Result<Long, Pageview> result) throws IOException {

  while(result.next()) { //advances the Result object and breaks if at end
    long resultKey = result.getKey(); //obtain current key
    Pageview resultPageview = result.get(); //obtain current value object
  
    //print the results
    System.out.println(resultKey + ":");
    printPageview(resultPageview);
  }

  System.out.println("Number of pageviews from the query:" + result.getOffset());
}
```

With these functions defined, we can run the Log Manager class, to query the
access logs at HBase. For example, to display the log records between lines 10 and 12
we can use:

```
bin/gora logmanager -query 10 12
```

Which results in:

```
10:
org.apache.gora.tutorial.log.generated.Pageview@d38d0eaa {
  "url":"/"
  "timestamp":"1236710442000"
  "ip":"144.122.180.55"
  "httpMethod":"GET"
  "httpStatusCode":"200"
  "responseSize":"43"
  "referrer":"http://buldinle.com/"
  "userAgent":"Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Firefox/3.0.6"
}
11:
org.apache.gora.tutorial.log.generated.Pageview@b513110a {
  "url":"/index.php?i=7&amp;a=1__gefuumyhl5c&amp;k=5143555"
  "timestamp":"1236710453000"
  "ip":"85.100.75.104"
  "httpMethod":"GET"
  "httpStatusCode":"200"
  "responseSize":"43"
  "referrer":"http://www.buldinle.com/index.php?i=7&amp;a=1__GeFUuMyHl5c&amp;k=5143555"
  "userAgent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7"
}
```

<a id="tutorial--deleting-objects"></a>

## Deleting objects

Just like fetching objects, there are two main methods to delete
objects from the data store. The first one is to delete objects one by
one using the `DataStore#delete(K key)` method, which takes the key of the object.
Alternatively we can delete all of the data that matches a given query by
calling the `DataStore#deleteByQuery(Query query)` method. By using `#deleteByQuery`, we can
do fine-grain deletes, for example deleting just a specific field
from several records.
Continueing from the LogManager class, the api's for both are given below.

```
/**Deletes the pageview with the given line number */
private void delete(long lineNum) throws Exception {
  dataStore.delete(lineNum);
  dataStore.flush(); //write changes may need to be flushed before they are committed 
}

/** This method illustrates delete by query call */
private void deleteByQuery(long startKey, long endKey) throws IOException {
  //Constructs a query from the dataStore. The matching rows to this query will be deleted
  Query<Long, Pageview> query = dataStore.newQuery();
  //set the properties of query
  query.setStartKey(startKey);
  query.setEndKey(endKey);

  dataStore.deleteByQuery(query);
}    
```

And from the command line :

```
bin/gora logmanager -delete 12
bin/gora logmanager -deleteByQuery 40 50
```

<a id="tutorial--mapreduce-support"></a>

## MapReduce Support

Gora has first class MapReduce support for [Apache Hadoop](http://hadoop.apache.org).
Gora data stores can be used as inputs and outputs of jobs. Moreover, the objects can
be serialized, and passed between tasks keeping their persistency state. For the
serialization, Gora extends Avro DatumWriters.

<a id="tutorial--log-analytics-in-mapreduce"></a>

### Log analytics in MapReduce

For this part of the tutorial, we will be analyzing the logs that have been
stored at HBase earlier. Specifically, we will develop a MapReduce program to
calculate the number of daily pageviews for each URL in the site.

We will be using the LogAnalytics class to analyze the logs, which can
be found at `gora-tutorial/src/main/java/org/apache/gora/tutorial/log/LogAnalytics.java`.
For computing the analytics, the mapper takes in pageviews, and outputs tuples of
<URL, timestamp> pairs, with 1 as the value. The timestamp represents the day
in which the pageview occurred, so that the daily pageviews are accumulated.
The reducer just sums up the values, and outputs MetricDatum objects
to be sent to the output Gora data store.

<a id="tutorial--setting-up-the-environment"></a>

### Setting up the environment

We will be using the logs stored at HBase by the LogManager class.
We will push the output of the job to an HSQL database, since it has a zero conf
set up. However, you can also use MySQL or HBase for storing the analytics results.
If you want to continue with HBase, you can skip the next sections.

<a id="tutorial--setting-up-the-database"></a>

### Setting up the database

First we need to download HSQL dependencies. For that, ensure that the hsqldb
dependency is available in the Maven pom.xml.
Ofcourse MySQL users should uncomment the mysql dependency instead.

```
<!--<dependency org="org.hsqldb" name="hsqldb" rev="2.0.0" conf="*->default"/>-->
```

Then we need to run Maven so that the new dependencies can be downloaded.

```
$ mvn
```

If you are using Mysql, you should also setup the database server, create the database
and give necessary permissions to create tables, etc so that Gora can run properly.

<a id="tutorial--configuring-gora_1"></a>
<a id="tutorial--configuring-gora-2"></a>

### Configuring Gora

We will put the configuration necessary to connect to the database to
`gora-tutorial/conf/gora.properties`.

<a id="tutorial--jdbc-properties-for-gora-sql-module-using-hsql"></a>

#### JDBC properties for gora-sql module using HSQL

```
gora.sqlstore.jdbc.driver=org.hsqldb.jdbcDriver
gora.sqlstore.jdbc.url=jdbc:hsqldb:hsql://localhost/goratest
```

<a id="tutorial--jdbc-properties-for-gora-sql-module-using-mysql"></a>

#### JDBC properties for gora-sql module using MySQL

```
gora.sqlstore.jdbc.driver=com.mysql.jdbc.Driver
gora.sqlstore.jdbc.url=jdbc:mysql://localhost:3306/goratest
gora.sqlstore.jdbc.user=root
gora.sqlstore.jdbc.password=      
```

As expected the jdbc.driver property is the JDBC driver class, and jdbc.url is the JDBC connection URL. Moreover jdbc.user
and jdbc.password can be specific is needed. More information for these
parameters can be found at [gora-sql](#gora-sql) documentation.

<a id="tutorial--modelling-the-data-data-beans-for-analytics"></a>

### Modelling the data - Data Beans for Analytics

For web site analytics, we will be using a generic MetricDatum
data structure. It holds a string metricDimension, a long
timestamp, and a long metric fields. The first two fields
are the dimensions of the web analytics data, and the last is the actual aggregate
metric value. For example we might have an instance {metricDimension="/index", timestamp=101, metric=12}, representing that there have been 12 pageviews to
the URL "/index" for the given time interval 101.

The avro schema definition for MetricDatum can be found at
`gora-tutorial/src/main/avro/metricdatum.json`, and the compiled source
code at `gora-tutorial/src/main/java/org/apache/gora/tutorial/log/generated/MetricDatum.java`.

```
{"type": "record","name": "MetricDatum","namespace": "org.apache.gora.tutorial.log.generated","fields" : [{"name": "metricDimension", "type": "string"},{"name": "timestamp", "type": "long"},{"name": "metric", "type" : "long"}]}
```

<a id="tutorial--data-store-mappings"></a>

### Data store mappings

We will be using the SQL backend to store the job output data, just to
demonstrate the SQL backend.

Similar to what we have seen with HBase, gora-sql plugin reads configuration from the
`gora-sql-mappings.xml` file.
Specifically, we will use the `gora-tutorial/conf/gora-sql-mappings.xml` file.

```
<gora-otd>
  ...
  <class name="org.apache.gora.tutorial.log.generated.MetricDatum" keyClass="java.lang.String" table="Metrics">
    <primarykey column="id" length="512"/>
    <field name="metricDimension" column="metricDimension" length="512"/>
    <field name="timestamp" column="ts"/>
    <field name="metric" column="metric/>
  </class>
</gora-otd>
```

SQL mapping files contain one or more class elements as the children of gora-orm.
The key value pair is declared in the class element. The name attribute is the
fully qualified name of the class, and the keyClass attribute is the fully qualified class
name of the key class.

Children of the class element are field elements and one
primaryKey element. Each field element has a name
and column attribute, and optional jdbc-type, length and scale attributes.
name attribute contains the name of the field in the persistent class, and
column attribute is the name of the
column in the database. The primaryKey holds the actual key as the primary key field. Currently, Gora only supports tables with one primary key.

<a id="tutorial--constructing-the-job"></a>

## Constructing the job

In constructing the job object for Hadoop, we need to define whether we will use
Gora as job input, output or both. Gora defines
its own GoraInputFormat, and GoraOutputFormat, which
uses DataStore's as input sources and output sinks for the jobs.
Gora{In|Out}putFormat classes define static methods to set up the job properly.
However, if the mapper or reducer extends Gora's mapper and reducer classes, you can use the static methods defined in GoraMapper and
GoraReducer since they are more convenient.

For this tutorial we will use Gora as both input and output. As can be seen from the
`createJob()` function, quoted below, we create the job
as normal, and set the input parameters via
`GoraMapper#initMapperJob()`, and `GoraReducer#initReducerJob()`.

`GoraMapper#initMapperJob()` takes a store and an optional query to fetch the data from.
When a query is given, only the results of the query is used as the input of the job, if not all the records are used.
The actual Mapper, map output key and value classes are passed to `initMapperJob()`
function as well. `GoraReducer#initReducerJob()` accepts
the data store to store the job's output as well as the actual reducer class.
initMapperJob and initReducerJob functions have also overriden methods that take the data store class
rather than data store instances.

```
  public Job createJob(DataStore<Long, Pageview> inStore
      , DataStore<String, MetricDatum> outStore, int numReducer) throws IOException {
    Job job = new Job(getConf());

    job.setJobName("Log Analytics");
    job.setNumReduceTasks(numReducer);
    job.setJarByClass(getClass());

    /* Mappers are initialized with GoraMapper.initMapper() or 
     * GoraInputFormat.setInput()*/
    GoraMapper.initMapperJob(job, inStore, TextLong.class, LongWritable.class
        , LogAnalyticsMapper.class, true);

    /* Reducers are initialized with GoraReducer#initReducer().
     * If the output is not to be persisted via Gora, any reducer 
     * can be used instead. */
    GoraReducer.initReducerJob(job, outStore, LogAnalyticsReducer.class);

    return job;
  }
```

<a id="tutorial--gora-mappers-and-using-gora-an-input"></a>

### Gora mappers and using Gora an input

Typically, if Gora is used as job input, the Mapper class extends
GoraMapper. However, currently this is not forced by the API so other class hierarchies can be used instead.
The mapper receives the key value pairs that are the results of the input query, and emits
the results of the custom map task. Note that output records from map are independent
from the input and output data stores, so any Hadoop serializable key value class can be used.
However, Gora persistent classes are also Hadoop serializable. Hadoop serialization is
handled by the PersistentSerialization class. Gora also defines a StringSerialization class, to serialize strings easily.

Coming back to the code for the tutorial, we can see that LogAnalytics
class defines an inner class LogAnalyticsMapper which extends
GoraMapper. The map function receives Long keys which are the line
numbers, and Pageview values as read from the input data store. The map simply
rolls up the timestamp up to the day (meaning that only the day of the timestamp is used), and outputs the key as a tuple of <URL,day>.

```
private TextLong tuple;

protected void map(Long key, Pageview pageview, Context context) 
  throws IOException ,InterruptedException {
  
  Utf8 url = pageview.getUrl();
  long day = getDay(pageview.getTimestamp());
  
  tuple.getKey().set(url.toString());
  tuple.getValue().set(day);
  
  context.write(tuple, one);
};
```

<a id="tutorial--gora-reducers-and-using-gora-as-output"></a>

### Gora reducers and using Gora as output

Similar to the input, typically, if Gora is used as job output, the Reducer extends
GoraReducer. The values emitted by the reducer are persisted to the output data store
as a result of the job.

For this tutorial, the LogAnalyticsReducer inner class, which extends GoraReducer, is used as the reducer. The reducer
just sums up all the values that correspond to the <URL,day> tuple.
Then the metric dimension object is constructed and emitted, which
will be stored at the output data store.

```
protected void reduce(TextLong tuple
    , Iterable<LongWritable> values, Context context) 
  throws IOException ,InterruptedException {
  
  long sum = 0L; //sum up the values
  for(LongWritable value: values) {
    sum+= value.get();
  }
  
  String dimension = tuple.getKey().toString();
  long timestamp = tuple.getValue().get();
  
  metricDatum.setMetricDimension(new Utf8(dimension));
  metricDatum.setTimestamp(timestamp);
  
  String key = metricDatum.getMetricDimension().toString();
  metricDatum.setMetric(sum);
  
  context.write(key, metricDatum);
};
```

<a id="tutorial--running-the-job"></a>

### Running the job

Now that the job is constructed, we can run the Hadoop job as usual. Note that the run function
of the LogAnalytics class parses the arguments and runs the job. We can run the program by

```
$ bin/gora loganalytics [<input data store> [<output data store>]]
```

<a id="tutorial--running-the-job-with-sql"></a>

### Running the job with SQL

Now, let's run the log analytics tools with the SQL backend(either Hsql or MySql). The input data store will be

```
org.apache.gora.hbase.store.HBaseStore 
```

and output store will be

```
org.apache.gora.sql.store.SqlStore
```

Remember that we have already configured the database
connection properties and which database will be used at the Setting up the environment section.

```
$ bin/gora loganalytics org.apache.gora.hbase.store.HBaseStore  org.apache.gora.sql.store.SqlStore
```

Now we should see some logging output from the job, and whether it finished with success. To check out the output
if we are using HSQLDB, below command can be used.

```
$ java -jar gora-tutorial/lib/hsqldb-2.0.0.jar
```

In the connection URL, the same URL that we have provided in gora.properties should be used. If on the other hand
MySQL is used, than we should be able to see the output using the mysql command line utility.

The results of the job are stored at the table Metrics, which is defined at the `gora-sql-mapping.xml`
file. Running a select query over this data confirms that the daily pageview metrics for the web site is indeed stored.
To see the most popular pages, run:

> SELECT METRICDIMENSION, TS, METRIC FROM metrics order by metric desc

| METRICDIMENSION | TS | METRIC |
| --- | --- | --- |
| / | 1236902400000 | 220 |
| / | 1236988800000 | 212 |
| / | 1236816000000 | 191 |
| / | 1237075200000 | 155 |
| / | 1241395200000 | 111 |
| / | 1236643200000 | 110 |
| / | 1236729600000 | 95 |
| /index.php?a=3\_\_x8g0vi&k=5508310 | 1236816000000 | 45 |
| /index.php?a=1\_\_5kf9nvgrzos&k=208773 | 1236816000000 | 37 |
| ... | ... | ... |

As you can see, the home page (/) for various days and some other pages are listed.
In total 3033 rows are present at the metrics table.

<a id="tutorial--running-the-job-with-hbase"></a>

### Running the job with HBase

Since HBaseStore is already defined as the default data store at `gora.properties`
we can run the job with HBase as:

```
$ bin/gora loganalytics
```

The outputs of the job will be saved in the Metrics table, whose layout is defined at
`gora-hbase-mapping.xml` file. To see the results:

```
hbase(main):010:0> scan 'Metrics', {LIMIT=>1}

ROW                          COLUMN+CELL
 /?a=1__-znawtuabsy&amp;k=96804_ column=common:metric, timestamp=1289815441740, value=\x00\x00\x00\x00\x00\x00\x00
 1236902400000               \x09
 /?a=1__-znawtuabsy&amp;k=96804_ column=common:metricDimension, timestamp=1289815441740, value=/?a=1__-znawtuabsy&amp;
 1236902400000               k=96804
 /?a=1__-znawtuabsy&amp;k=96804_ column=common:ts, timestamp=1289815441740, value=\x00\x00\x01\x1F\xFD \xD0\x00
 1236902400000
1 row(s) in 0.0490 seconds
```

<a id="tutorial--spark-backend"></a>

## Spark Backend

Log analytics example will be implemented via GoraSparkEngine at this tutorial to explain Spark backend of Gora.
Data will be read from Hbase, map/reduce methods will be run and result will be written into Solr (version: 4.10.3).
All the process will be done over Spark.

Persist data into Hbase as described at [Log analytics in MapReduce](#tutorial--log-analytics-in-mapreduce).

To write result into Solr, create a schemaless core named as Metrics. To do it easily, you can rename default core of collection1 to Metrics which is at
`solr-4.10.3/example/example-schemaless/solr` folder and edit `solr-4.10.3/example/example-schemaless/solr/Metrics/core.properties` as follows:

```
name=Metrics
```

Then run start command for Solr:

```
solr-4.10.3/example$ java -Dsolr.solr.home=example-schemaless/solr/ -jar start.jar
```

Read data from Hbase, generate some metrics and write results into Solr with Spark via Gora. Here is how to initialize in and out data stores:

```
public int run(String[] args) throws Exception {DataStore<Long, Pageview> inStore; DataStore<String, MetricDatum> outStore; Configuration hadoopConf = new Configuration(); if (args.length > 0) {String dataStoreClass = args[0]; inStore = DataStoreFactory.getDataStore(dataStoreClass, Long.class, Pageview.class, hadoopConf); if (args.length > 1) {dataStoreClass = args[1];} outStore = DataStoreFactory.getDataStore(dataStoreClass, String.class, MetricDatum.class, hadoopConf); } else {inStore = DataStoreFactory.getDataStore(Long.class, Pageview.class, hadoopConf); outStore = DataStoreFactory.getDataStore(String.class, MetricDatum.class, hadoopConf);} ...}
```

Pass input data store’s key and value classes and instantiate a GoraSparkEngine:

```
GoraSparkEngine<Long, Pageview> goraSparkEngine = new GoraSparkEngine<>(Long.class, Pageview.class);
```

Construct a JavaSparkContext. Register input data store’s value class as Kryo class:

```
SparkConf sparkConf = new SparkConf().setAppName("Gora Spark Integration Application").setMaster("local");
Class[] c = new Class[1];
c[0] = inStore.getPersistentClass();
sparkConf.registerKryoClasses(c);
JavaSparkContext sc = new JavaSparkContext(sparkConf);
```

You can get JavaPairRDD from input data store:

```
JavaPairRDD<Long, Pageview> goraRDD = goraSparkEngine.initialize(sc, inStore);
```

When you get it, you can work on it as like you are writing a code for Spark! For example:

```
long count = goraRDD.count();
System.out.println("Total Log Count: " + count);
```

These are the functions of map and reduce phases for this example:

```
/** The number of milliseconds in a day */ private static final long DAY_MILIS = 1000 * 60 * 60 * 24;
/** * map function used in calculation */ private static Function<Pageview, Tuple2<Tuple2<String, Long>, Long>> mapFunc = new Function<Pageview, Tuple2<Tuple2<String, Long>, Long>>() {@Override public Tuple2<Tuple2<String, Long>, Long> call(Pageview pageview) throws Exception {String url = pageview.getUrl().toString(); Long day = getDay(pageview.getTimestamp()); Tuple2<String, Long> keyTuple = new Tuple2<>(url, day); return new Tuple2<>(keyTuple, 1L);} };
/** * reduce function used in calculation */ private static Function2<Long, Long, Long> redFunc = new Function2<Long, Long, Long>() {@Override public Long call(Long aLong, Long aLong2) throws Exception {return aLong + aLong2;} };
/** * metric function used after map phase */ private static PairFunction<Tuple2<Tuple2<String, Long>, Long>, String, MetricDatum> metricFunc = new PairFunction<Tuple2<Tuple2<String, Long>, Long>, String, MetricDatum>() {@Override public Tuple2<String, MetricDatum> call(Tuple2<Tuple2<String, Long>, Long> tuple2LongTuple2) throws Exception {String dimension = tuple2LongTuple2._1()._1(); long timestamp = tuple2LongTuple2._1()._2(); MetricDatum metricDatum = new MetricDatum(); metricDatum.setMetricDimension(dimension); metricDatum.setTimestamp(timestamp); String key = metricDatum.getMetricDimension().toString(); key += "_" + Long.toString(timestamp); metricDatum.setMetric(tuple2LongTuple2._2()); return new Tuple2<>(key, metricDatum);} };
/** * Rolls up the given timestamp to the day cardinality, so that data can be aggregated daily */ private static long getDay(long timeStamp) {return (timeStamp / DAY_MILIS) * DAY_MILIS;}
```

Here is how to run map and reduce functions at existing JavaPairRDD:

```
JavaRDD<Tuple2<Tuple2<String, Long>, Long>> mappedGoraRdd = goraRDD.values().map(mapFunc);
JavaPairRDD<String, MetricDatum> reducedGoraRdd = JavaPairRDD.fromJavaRDD(mappedGoraRdd).reduceByKey(redFunc).mapToPair(metricFunc);
```

When you want to persist result into output data store, (in our example it is Solr), you should do it as follows:

```
Configuration sparkHadoopConf = goraSparkEngine.generateOutputConf(outStore);
reducedGoraRdd.saveAsNewAPIHadoopDataset(sparkHadoopConf);
```

That’s all! You can check Solr to verify the result.

<a id="tutorial--jcache-caching-datastore"></a>

## JCache caching dataStore

This tutorial is about exposing Apache Gora persistent dataStore over Apache Gora default caching dataStore JCache. This sample exhibits how caching can reduce read latency
for consecutive reads when data beans are retrieved from intermediate cache as opposite to directly through the backend for consecutive iteration.

Start HBase.

```
/hbase-0.98.19-hadoop2/bin$ ./start-hbase.sh
```

Start DistributedLogManager. ( Expose HBase dataStore over JCache dataStore )

```
/gora/bin$ ./gora distributedlogmanager 
```

Persist Log Databeans to HBase either via the path  **JCache DataStore -> HBase DataStore -> HBase**  either via direct path  **HBase DataStore -> HBase**

```
-parse persistent|cache <-input_log_file-> - 
```

Benchmark dataBean read latency for two paths, path via  **JCache DataStore <- HBase DataStore <- HBase**  and path via  **HBase DataStore <- HBase**

```
-benchmark <-startLineNum-> <-endLineNum-> <-iterations->
```

<a id="tutorial--more-examples"></a>

## More Examples

Other than this tutorial, there are several places that you can find
examples of Gora in action.

The first place to look at is the examples directories
under various Gora modules. All the modules have a `/src/examples/` directory
under which some example classes can be found. Especially, there are some classes that are used for tests under
`gora-core/src/examples/`

Second, various unit tests of Gora modules can be referred to see the API in use. The unit tests can be found
at `gora-core/src/test/`.

The source code for the projects using Gora can also be checked out as a reference. [Apache Nutch](http://nutch.apache.org) is
one of the first class users of Gora; so looking into how Nutch uses Gora is always a good idea. Gora is however also in use
in other Apache projects such as [Apache Giraph](http://giraph.apache.org)

Please feel free to grab our [poweredBy](assets/images/powered-by-gora_1aac3517e0bd5618.png) sticker and embedded it in anything backed by Apache Gora.

<a id="tutorial--feedback"></a>

## Feedback

At last, thanks for trying out Gora. If you find any bugs or you have suggestions for improvement, do not hesitate to give feedback on the [dev@gora.apache.org](mailto:dev@gora.apache.org) [mailing list](https://gora.apache.org/mailing_lists.html).

---

---

<a id="gora-sql"></a>

<!-- source_url: https://gora.apache.org/current/gora-sql.html -->

<!-- page_index: 21 -->

<a id="gora-sql--overview"></a>

## Overview

This is the main documentation for the gora-sql module.

Currently the [**gora-sql-0.1.1-incubating**](http://search.maven.org/#artifactdetails|org.apache.gora|gora-sql|0.1.1-incubating|jar)
module is deprecated, however [**work is planned**](https://issues.apache.org/jira/browse/GORA-86‎)
to use [JOOQ](http://jooq.org) as a mechanism for providing SQL backend support for Gora.

In the deprecated gora-sql-0.1.1-incubating artifact [MySQL](htp://www.mysql.com) and [HSQLDB](http://www.hsqldb.org) are supported.

<a id="gora-sql--goraproperties"></a>
<a id="gora-sql--gora.properties"></a>

## gora.properties

Coming soon

<a id="gora-sql--gora-sql-mappings"></a>

## Gora SQL mappings

Coming soon

---

---

<a id="index"></a>

<!-- source_url: https://gora.apache.org/current/index.html -->

<!-- page_index: 22 -->

# Apache Gora™ - Gora Module Overview

---

---

<a id="gora-conf"></a>

<!-- source_url: https://gora.apache.org/current/gora-conf.html -->

<!-- page_index: 23 -->

<a id="gora-conf--goraproperties"></a>
<a id="gora-conf--gora.properties"></a>

## gora.properties

Gora reads necessary configuration from a properties file name
`gora.properties`.

The file is searched in the classpath, which is
obtained using the `ClassLoader` of the [DataStoreFactory](http://gora.apache.org/current/api/apidocs-0.4/index.html?org%2Fapache%2Fgora%2Fstore%2FDataStoreFactory.html=)
class.

The following properties are recognized:

<a id="gora-conf--common-properties"></a>

## Common Properties

| Property | Required | Default | Explanation |
| --- | --- | --- | --- |
| `gora.datastore.default` | No | – | The full classname of the default data store implementation to use |
| `gora.datastore.autocreateschema` | No | true | Whether to create schemas automatically |

`gora.datastore.default` is perhaps the most important property in this file.
This property configures the default [DataStore](http://gora.apache.org/current/api/apidocs-0.4/index.html?org%2Fapache%2Fgora%2Fstore%2FDataStore.html=) implementation to use.
However, other data stores can still be instantiated thorough the API.
Data store implementation in Gora distribution include:

| DataStore Implementation | Full Class Name | Module Name | Explanation |
| --- | --- | --- | --- |
| **AvroStore** | `org.apache.gora.avro.store.AvroStore` | gora-core | An adapter DataStore for binary-compatible Apache Avro serializations. AvroDataStore supports Binary and JSON serializations. |
| **DataFileAvroStore** | `org.apache.gora.avro.store.DataFileAvroStore` | gora-core | DataFileAvroStore is file based store which uses Avro's DataFile{Writer,Reader}'s as a backend. This datastore supports mapreduce. |
| **AccumuloStore** | `org.apache.gora.accumulo.store.AccumuloStore` | gora-accumulo | DataStore for Apache Accumulo. |
| **HBaseStore** | `org.apache.gora.hbase.store.HBaseStore` | gora-hbase | DataStore for Apache HBase. |
| **CassandraStore** | `org.apache.gora.cassandra.store.CasssandraStore` | gora-cassandra | DataStore for Apache Cassandra. |
| **SolrStore** | `org.apache.gora.solr.store.SolrStore` | gora-solr | A DataStore implementation for Apache Solr. |
| **MemStore** | `org.apache.gora.memory.store.MemStore` | gora-core | Memory based DataStore implementation for tests. |
| **Dynamodb** | `org.apache.gora.dynamodb.store.DyanmoDBStore` | gora-dynamodb | Webservices-based datastore implementation for Amazon's DynamoDB. |
| **MongoStore** | `org.apache.gora.mongodb.store.MongoStore` | gora-mongodb | A DataStore implementation for MongoDB document storage. |

Some of the properties can be customized per datastore. The format of these
properties is as follows: `gora.<data_store_class>.<property_name>`.

Note that `<data_store_class>` is the classname of the datastore
implementation w/o the package name, for example `HbaseStore`.
You can also use the string datastore instead of the specific
data store class name, in which case, the property setting is effective
to all data stores. The following properties can be set per data store.

<a id="gora-conf--per-datastore-properties"></a>

## Per DataStore Properties

| Property | Required | Default Value | Explanation |
| --- | --- | --- | --- |
| `gora.<data_store_class>.autocreateschema` No true Whether to create schemas automatically for the specific data store |  |  |  |
| `gora.<data_store_class>.mapping.file` No gora-{accumulo\|hbase\|cassandra\|sql\|dynamodb}-mapping.xml The name of the mapping file |  |  |  |

<a id="gora-conf--data-store-specific-settings"></a>

## Data store specific settings

Other than the properties above, some of the data stores have their
own configurations. These properties are listed at the module documentations:

- [Gora Core Module](#gora-core) (incl. AvroStore, DataFileAvroStore and MemStore)
- [Gora HBase Module](#gora-hbase)
- [Gora Cassandra Module](#gora-cassandra)
- [Gora Solr Module](#gora-solr)
- [Gora Accumulo Module](#gora-accumulo)
- [Gora DynamoDB Module](#gora-dynamodb)
- [Gora MongoDB Module](#gora-mongodb)

---

<a id="overview"></a>

<!-- source_url: https://gora.apache.org/current/overview.html -->

<!-- page_index: 24 -->

<a id="overview--introduction"></a>

## Introduction

This is the main entry point for Gora documentation. Here are some pointers for further info:

- First if you haven't already done so, make sure to check the [quick start guide](#quickstart).
- Basic information about gora modules can be found below.
- You can also take a look at the [API Documentation](#api-javadoc) which contains the javadoc
  for all of the modules combined. We are always looking for [Documentation contributions](https://gora.apache.org/contribute.html).

You can find an abstract overview of how to configure Gora [here](#gora-conf).

<a id="overview--gora-modules"></a>

## Gora Modules

Gora source code is organized in a modular architecture. The gora-core module
is the main module which contains the core of the code. All other modules depend
on the gora-core module.
Each datastore backend in Gora resides in it's own module. The documentation for
the specific module can be found at the module's documentation directory.

It is wise so start with going over the documentation for the gora-core
module and then the specific data store module(s) you want to use. The
following modules are currently implemented in gora.

- [gora-compiler](#compiler): A page dedicated to the GoraCompiler; a critical part of the Gora workflow.
- [gora-core](#gora-core): Module containing core functionality, AvroStore and DataFileAvroStore stores;
- [gora-accumulo](#gora-accumulo): Module for [Apache Accumulo](http://accumulo.apache.org) backend and AccumuloStore implementation;
- [gora-cassandra](#gora-cassandra): Module for [Apache Cassandra](http://cassandra.apacheorg) backend and CassandraStore implementation;
- [gora-dynamodb](#gora-dynamodb): Module for [Amazon DynamoDB](http://aws.amazon.com/dynamodb/) backend and DynamoDBStore implementation;
- [gora-hbase](#gora-hbase): Module for [Apache HBase](http://hbase.apache.org) backend and HBaseStore implementation;
- [gora-sql](#gora-sql): Module for [HSQLDB](http://hsqldb.org/) and [MySQL](http://www.mysql.com/) backend and SqlStore implementation;
- [gora-mongodb](#gora-mongodb): Module for [MongoDB](http://www.mongodb.org/) backend and MongoStore implementation;
- [gora-aerospike](#gora-aerospike): Module for [Aerospike](http://www.aerospike.com/) backend and Aerospike implementation;

---
