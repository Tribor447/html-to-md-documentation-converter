# Apache CarbonData Documentation

## Navigation

- [introduction](#introduction)
- [quick start](#quick-start-guide)
- [use cases](#usecases)
- [Language Reference](#language-manual)
- [DDL](#ddl-of-carbondata)
- [DML](#dml-of-carbondata)
- [Streaming](#streaming-guide)
- [Configuration](#configuration-parameters)
- [Indexes](#index-developer-guide)
- [Data Types](#supported-data-types-in-carbondata)
- [Index Managament](#index-management)
- [Bloom Filter](#bloomfilter-index-guide)
- [Lucene](#lucene-index-guide)
- [Secondary Index](#secondary-index-guide)
- [Spatial Index](#spatial-index-guide)
- [MV](#mv-guide)
- [API](#sdk-guide)
- [Java SDK](#sdk-guide)
- [C++ SDK](#csdk-guide)
- [Performance Tuning](#performance-tuning)
- [S3 Storage](#s3-guide)
- [Index Server](#index-server)
- [PrestoDB Integration](#prestodb-guide)
- [PrestoSQL Integration](#prestosql-guide)
- [Flink Integration](#flink-integration-guide)
- [SCD & CDC](#scd-and-cdc-guide)
- [FAQ](#faq)
- [Contribute](#how-to-contribute-to-apache-carbondata)
- [Security](#security)
- [Release Guide](#release-guide)
- Other pages
  - [Apache CarbonData Documentation](#documentation)

## Content

<a id="introduction"></a>

<!-- source_url: https://carbondata.apache.org/introduction.html -->

<!-- page_index: 1 -->

<a id="introduction--what-is-carbondata"></a>

## What is CarbonData

CarbonData is a fully indexed columnar and Hadoop native data-store for processing heavy analytical workloads and detailed queries on big data with Spark SQL. CarbonData allows faster interactive queries over PetaBytes of data.

<a id="introduction--what-does-this-mean"></a>

## What does this mean

CarbonData has specially engineered optimizations like multi level indexing, compression and encoding techniques targeted to improve performance of analytical queries which can include filters, aggregation and distinct counts where users expect sub second response time for queries on TB level data on commodity hardware clusters with just a few nodes.

CarbonData has

- **Unique data organisation** for faster retrievals and minimise amount of data retrieved
- **Advanced push down optimisations** for deep integration with Spark so as to improvise the Spark DataSource API and other experimental features thereby ensure computing is performed close to the data to minimise amount of data read, processed, converted and transmitted(shuffled)
- **Multi level indexing** to efficiently prune the files and data to be scanned and hence reduce I/O scans and CPU processing

<a id="introduction--carbondata-features-functions"></a>

## CarbonData Features & Functions

CarbonData has rich set of features to support various use cases in Big Data analytics. The below table lists the major features supported by CarbonData.

<a id="introduction--table-management"></a>

### Table Management

- <a id="introduction--ddl-create-alter-drop-ctas"></a>

  ##### DDL (Create, Alter,Drop,CTAS)

  CarbonData provides its own DDL to create and manage carbondata tables. These DDL conform to Hive,Spark SQL format and support additional properties and configuration to take advantages of CarbonData functionalities.
- <a id="introduction--dml-load-insert"></a>

  ##### DML(Load,Insert)

  CarbonData provides its own DML to manage data in carbondata tables.It adds many customizations through configurations to completely customize the behavior as per user requirement scenarios.
- <a id="introduction--update-and-delete"></a>

  ##### Update and Delete

  CarbonData supports Update and Delete on Big Data.CarbonData provides the syntax similar to Hive to support IUD operations on CarbonData tables.
- <a id="introduction--segment-management"></a>

  ##### Segment Management

  CarbonData has unique concept of segments to manage incremental loads to CarbonData tables effectively.Segment management helps to easily control the table, perform easy retention, and is also used to provide transaction capability for operations being performed.
- <a id="introduction--partition"></a>

  ##### Partition

  CarbonData supports 2 kinds of partitions.1.partition similar to hive partition.2.CarbonData partition supporting hash,list,range partitioning.
- <a id="introduction--compaction"></a>

  ##### Compaction

  CarbonData manages incremental loads as segments. Compaction helps to compact the growing number of segments and also to improve query filter pruning.
- <a id="introduction--external-tables"></a>

  ##### External Tables

  CarbonData can read any carbondata file and automatically infer schema from the file and provide a relational table view to perform sql queries using Spark or any other applicaion.

<a id="introduction--index"></a>

### Index

- <a id="introduction--bloom-filter"></a>

  ##### Bloom filter

  CarbonData supports bloom filter index in order to quickly and efficiently prune the data for scanning and acheive faster query performance.
- <a id="introduction--lucene"></a>

  ##### Lucene

  Lucene is popular for indexing text data which are long.CarbonData supports lucene index so that text columns can be indexed using lucene and use the index result for efficient pruning of data to be retrieved during query.
- <a id="introduction--mv-materialized-views"></a>

  ##### MV (Materialized Views)

  MVs are kind of pre-aggregate and pre-join tables which can support efficient query re-write and processing.CarbonData provides MV which can rewrite query to fetch from any table(including non-carbondata tables). Typical usecase is to store the aggregated data of a non-carbondata fact table into carbondata and use mv to rewrite the query to fetch from carbondata.

<a id="introduction--streaming"></a>

### Streaming

- <a id="introduction--spark-streaming"></a>

  ##### Spark Streaming

  CarbonData supports streaming of data into carbondata in near-realtime and make it immediately available for query.CarbonData provides a DSL to create source and sink tables easily without the need for the user to write his application.

<a id="introduction--sdk"></a>

### SDK

- <a id="introduction--carbondata-writer"></a>

  ##### CarbonData writer

  CarbonData supports writing data from non-spark application using SDK.Users can use SDK to generate carbondata files from custom applications. Typical usecase is to write the streaming application plugged in to kafka and use carbondata as sink(target) table for storing.
- <a id="introduction--carbondata-reader"></a>

  ##### CarbonData reader

  CarbonData supports reading of data from non-spark application using SDK. Users can use the SDK to read the carbondata files from their application and do custom processing.

<a id="introduction--storage"></a>

### Storage

- <a id="introduction--s3"></a>

  ##### S3

  CarbonData can write to S3, OBS or any cloud storage confirming to S3 protocol. CarbonData uses the HDFS api to write to cloud object stores.
- <a id="introduction--hdfs"></a>

  ##### HDFS

  CarbonData uses HDFS api to write and read data from HDFS. CarbonData can take advantage of the locality information to efficiently suggest spark to run tasks near to the data.
- <a id="introduction--alluxio"></a>

  ##### Alluxio

  CarbonData also supports read and write with [Alluxio](#quick-start-guide--alluxio).

<a id="introduction--integration-with-big-data-ecosystem"></a>

## Integration with Big Data ecosystem

Refer to Integration with [Spark](#quick-start-guide--spark), [Presto](#quick-start-guide--presto) for detailed information on integrating CarbonData with these execution engines.

<a id="introduction--scenarios-where-carbondata-is-suitable"></a>

## Scenarios where CarbonData is suitable

CarbonData is useful in various analytical work loads.Some of the most typical usecases where CarbonData is being used is [documented here](#usecases).

<a id="introduction--performance-results"></a>

## Performance Results

[![Performance Results](https://github.com/apache/carbondata/blob/master/docs/images/carbondata-performance.png?raw=true)](assets/files/errorpage_d68d20be1f65d644.html)

[Top](#introduction--top)

---

<a id="quick-start-guide"></a>

<!-- source_url: https://carbondata.apache.org/quick-start-guide.html -->

<!-- page_index: 2 -->

<a id="quick-start-guide--quick-start"></a>

# Quick Start

This tutorial provides a quick introduction to use CarbonData. To follow along with this guide, download a packaged release of CarbonData from the [CarbonData website](https://dist.apache.org/repos/dist/release/carbondata/). Alternatively, it can be created following [Building CarbonData](https://github.com/apache/carbondata/tree/master/build) steps.

<a id="quick-start-guide--prerequisites"></a>

## Prerequisites

- CarbonData supports Spark versions up to 2.4. Please download Spark package from [Spark website](https://spark.apache.org/downloads.html)
- Create a sample.csv file using the following commands. The CSV file is required for loading data into CarbonData


```
cd carbondata
cat > sample.csv << EOF
id,name,city,age
1,david,shenzhen,31
2,eason,shenzhen,27
3,jarry,wuhan,35
EOF
```

<a id="quick-start-guide--integration"></a>

## Integration

<a id="quick-start-guide--integration-with-execution-engines"></a>

### Integration with Execution Engines

CarbonData can be integrated with Spark, Presto, Flink and Hive execution engines. The below documentation guides on Installing and Configuring with these execution engines.

<a id="quick-start-guide--spark"></a>

#### Spark

[Installing and Configuring CarbonData to run locally with Spark SQL CLI](#quick-start-guide--installing-and-configuring-carbondata-to-run-locally-with-spark-sql-cli)

[Installing and Configuring CarbonData to run locally with Spark Shell](#quick-start-guide--installing-and-configuring-carbondata-to-run-locally-with-spark-shell)

[Installing and Configuring CarbonData on Standalone Spark Cluster](#quick-start-guide--installing-and-configuring-carbondata-on-standalone-spark-cluster)

[Installing and Configuring CarbonData on Spark on YARN Cluster](#quick-start-guide--installing-and-configuring-carbondata-on-spark-on-yarn-cluster)

[Installing and Configuring CarbonData Thrift Server for Query Execution](#quick-start-guide--query-execution-using-carbondata-thrift-server)

<a id="quick-start-guide--presto"></a>

#### Presto

[Installing and Configuring CarbonData on Presto](#quick-start-guide--installing-and-configuring-carbondata-on-presto)

<a id="quick-start-guide--hive"></a>

#### Hive

[Installing and Configuring CarbonData on Hive](https://carbondata.apache.org/hive-guide.html)

<a id="quick-start-guide--integration-with-storage-engines"></a>

### Integration with Storage Engines

<a id="quick-start-guide--hdfs"></a>

#### HDFS

[CarbonData supports read and write with HDFS](#quick-start-guide--installing-and-configuring-carbondata-on-standalone-spark-cluster)

<a id="quick-start-guide--s3"></a>

#### S3

[CarbonData supports read and write with S3](#s3-guide)

<a id="quick-start-guide--alluxio"></a>

#### Alluxio

[CarbonData supports read and write with Alluxio](https://carbondata.apache.org/alluxio-guide.html)

<a id="quick-start-guide--installing-and-configuring-carbondata-to-run-locally-with-spark-sql-cli"></a>

## Installing and Configuring CarbonData to run locally with Spark SQL CLI

This will work with spark 2.3+ versions. In Spark SQL CLI, it uses CarbonExtensions to customize the SparkSession with CarbonData's parser, analyzer, optimizer and physical planning strategy rules in Spark.
To enable CarbonExtensions, we need to add the following configuration.

| Key | Value |
| --- | --- |
| spark.sql.extensions | org.apache.spark.sql.CarbonExtensions |

Start Spark SQL CLI by running the following command in the Spark directory:

```
./bin/spark-sql --conf spark.sql.extensions=org.apache.spark.sql.CarbonExtensions --jars <carbondata assembly jar path>
```

<a id="quick-start-guide--creating-a-table"></a>

###### Creating a Table

```
CREATE TABLE IF NOT EXISTS test_table (
  id string,
  name string,
  city string,
  age Int)
STORED AS carbondata;
```

> [!NOTE]
> : CarbonExtensions only support "STORED AS carbondata" and "USING carbondata"

<a id="quick-start-guide--loading-data-to-a-table"></a>

###### Loading Data to a Table

```
LOAD DATA INPATH '/local-path/sample.csv' INTO TABLE test_table;

LOAD DATA INPATH 'hdfs://hdfs-path/sample.csv' INTO TABLE test_table;
```

```
insert into table test_table select '1', 'name1', 'city1', 1;
```

> [!NOTE]
> : Please provide the real file path of `sample.csv` for the above script.
> If you get "tablestatus.lock" issue, please refer to [FAQ](#faq)

<a id="quick-start-guide--query-data-from-a-table"></a>

###### Query Data from a Table

```
SELECT * FROM test_table;
```

```
SELECT city, avg(age), sum(age)
FROM test_table
GROUP BY city;
```

<a id="quick-start-guide--installing-and-configuring-carbondata-to-run-locally-with-spark-shell"></a>

## Installing and Configuring CarbonData to run locally with Spark Shell

Apache Spark Shell provides a simple way to learn the API, as well as a powerful tool to analyze data interactively. Please visit [Apache Spark Documentation](http://spark.apache.org/docs/latest/) for more details on the Spark shell.

<a id="quick-start-guide--basics"></a>

#### Basics

<a id="quick-start-guide--option-1:-using-carbonsession-deprecated-since-2.0"></a>

###### Option 1: Using CarbonSession (deprecated since 2.0)

Start Spark shell by running the following command in the Spark directory:

```
./bin/spark-shell --jars <carbondata assembly jar path>
```

> [!NOTE]
> : Path where packaged release of CarbonData was downloaded or assembly jar will be available after [building CarbonData](https://github.com/apache/carbondata/blob/master/build/README.md) and can be copied from `./assembly/target/scala-2.1x/apache-carbondata_xxx.jar`

In this shell, SparkSession is readily available as `spark` and Spark context is readily available as `sc`.

In order to create a CarbonSession we will have to configure it explicitly in the following manner :

- Import the following :

```
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.CarbonSession._
```

- Create a CarbonSession :

```
val carbon = SparkSession.builder().config(sc.getConf).getOrCreateCarbonSession("<carbon_store_path>")
```

> [!NOTE]
>

- By default metastore location points to `../carbon.metastore`, user can provide own metastore location to CarbonSession like
  `SparkSession.builder().config(sc.getConf).getOrCreateCarbonSession("<carbon_store_path>", "<local metastore path>")`.
- Data storage location can be specified by `<carbon_store_path>`, like `/carbon/data/store`, `hdfs://localhost:9000/carbon/data/store` or `s3a://carbon/data/store`.

<a id="quick-start-guide--option-2:-using-sparksession-with-carbonextensions"></a>

###### Option 2: Using SparkSession with CarbonExtensions

Start Spark shell by running the following command in the Spark directory:

```
./bin/spark-shell --conf spark.sql.extensions=org.apache.spark.sql.CarbonExtensions --jars <carbondata assembly jar path>
```

> [!NOTE]
>

- In this flow, we can use the built-in SparkSession `spark` instead of `carbon`.
  We also can create a new SparkSession instead of the built-in SparkSession `spark` if need.
  It need to add "org.apache.spark.sql.CarbonExtensions" into spark configuration "spark.sql.extensions".

```
SparkSession newSpark = SparkSession
  .builder()
  .config(sc.getConf)
  .enableHiveSupport
  .config("spark.sql.extensions","org.apache.spark.sql.CarbonExtensions")
  .getOrCreate()
```

- Data storage location can be specified by "spark.sql.warehouse.dir".

<a id="quick-start-guide--executing-queries"></a>

#### Executing Queries

<a id="quick-start-guide--creating-a-table-2"></a>

###### Creating a Table

```
carbon.sql(
           s"""
              | CREATE TABLE IF NOT EXISTS test_table(
              |   id string,
              |   name string,
              |   city string,
              |   age Int)
              | STORED AS carbondata
           """.stripMargin)
```

> [!NOTE]
> :
> The following table list all supported syntax:

| create table | SparkSession with CarbonExtensions | CarbonSession |
| --- | --- | --- |
| STORED AS carbondata | yes | yes |
| USING carbondata | yes | yes |
| STORED BY 'carbondata' | no | yes |
| STORED BY 'org.apache.carbondata.format' | no | yes |

We suggest to use CarbonExtensions instead of CarbonSession.

<a id="quick-start-guide--loading-data-to-a-table-2"></a>

###### Loading Data to a Table

```
carbon.sql("LOAD DATA INPATH '/path/to/sample.csv' INTO TABLE test_table")
```

> [!NOTE]
> : Please provide the real file path of `sample.csv` for the above script.
> If you get "tablestatus.lock" issue, please refer to [FAQ](#faq)

<a id="quick-start-guide--query-data-from-a-table-2"></a>

###### Query Data from a Table

```
carbon.sql("SELECT * FROM test_table").show()

carbon.sql(
           s"""
              | SELECT city, avg(age), sum(age)
              | FROM test_table
              | GROUP BY city
           """.stripMargin).show()
```

<a id="quick-start-guide--installing-and-configuring-carbondata-on-standalone-spark-cluster"></a>

## Installing and Configuring CarbonData on Standalone Spark Cluster

<a id="quick-start-guide--prerequisites-2"></a>

### Prerequisites

- Hadoop HDFS and Yarn should be installed and running.
- Spark should be installed and running on all the cluster nodes.
- CarbonData user should have permission to access HDFS.

<a id="quick-start-guide--procedure"></a>

### Procedure

1. [Build the CarbonData](https://github.com/apache/carbondata/blob/master/build/README.md) project and get the assembly jar from `./assembly/target/scala-2.1x/apache-carbondata_xxx.jar`.
2. Copy `./assembly/target/scala-2.1x/apache-carbondata_xxx.jar` to `$SPARK_HOME/carbonlib` folder.


> [!NOTE]
> : Create the carbonlib folder if it does not exist inside `$SPARK_HOME` path.

3. Add the carbonlib folder path in the Spark classpath. (Edit `$SPARK_HOME/conf/spark-env.sh` file and modify the value of `SPARK_CLASSPATH` by appending `$SPARK_HOME/carbonlib/*` to the existing value)
4. Copy the `./conf/carbon.properties.template` file from CarbonData repository to `$SPARK_HOME/conf/` folder and rename the file to `carbon.properties`.
5. Repeat Step 2 to Step 5 in all the nodes of the cluster.
6. In Spark node[master], configure the properties mentioned in the following table in `$SPARK_HOME/conf/spark-defaults.conf` file.

| Property | Value | Description |
| --- | --- | --- |
| spark.driver.extraJavaOptions | `-Dcarbon.properties.filepath = $SPARK_HOME/conf/carbon.properties` | A string of extra JVM options to pass to the driver. For instance, GC settings or other logging. |
| spark.executor.extraJavaOptions | `-Dcarbon.properties.filepath = $SPARK_HOME/conf/carbon.properties` | A string of extra JVM options to pass to executors. For instance, GC settings or other logging. **NOTE**: You can enter multiple values separated by space. |

7. Verify the installation. For example:

```
./bin/spark-shell \
--master spark://HOSTNAME:PORT \
--total-executor-cores 2 \
--executor-memory 2G
```

> [!NOTE]
> :

- property "carbon.storelocation" is deprecated in carbondata 2.0 version. Only the users who used this property in previous versions can still use it in carbon 2.0 version.
- Make sure you have permissions for CarbonData JARs and files through which driver and executor will start.

<a id="quick-start-guide--installing-and-configuring-carbondata-on-spark-on-yarn-cluster"></a>

## Installing and Configuring CarbonData on Spark on YARN Cluster

This section provides the procedure to install CarbonData on "Spark on YARN" cluster.

<a id="quick-start-guide--prerequisites-3"></a>

### Prerequisites

- Hadoop HDFS and Yarn should be installed and running.
- Spark should be installed and running in all the clients.
- CarbonData user should have permission to access HDFS.

<a id="quick-start-guide--procedure-2"></a>

### Procedure

The following steps are only for Driver Nodes. (Driver nodes are the one which starts the spark context.)

1. [Build the CarbonData](https://github.com/apache/carbondata/blob/master/build/README.md) project and get the assembly jar from `./assembly/target/scala-2.1x/apache-carbondata_xxx.jar` and copy to `$SPARK_HOME/carbonlib` folder.


> [!NOTE]
> : Create the carbonlib folder if it does not exists inside `$SPARK_HOME` path.

2. Copy the `./conf/carbon.properties.template` file from CarbonData repository to `$SPARK_HOME/conf/` folder and rename the file to `carbon.properties`.
3. Create `tar.gz` file of carbonlib folder and move it inside the carbonlib folder.

```
cd $SPARK_HOME
tar -zcvf carbondata.tar.gz carbonlib/
mv carbondata.tar.gz carbonlib/
```

4. Configure the properties mentioned in the following table in `$SPARK_HOME/conf/spark-defaults.conf` file.

| Property | Description | Value |
| --- | --- | --- |
| spark.master | Set this value to run the Spark in yarn cluster mode. | Set yarn-client to run the Spark in yarn cluster mode. |
| spark.yarn.dist.files | Comma-separated list of files to be placed in the working directory of each executor. | `$SPARK_HOME/conf/carbon.properties` |
| spark.yarn.dist.archives | Comma-separated list of archives to be extracted into the working directory of each executor. | `$SPARK_HOME/carbonlib/carbondata.tar.gz` |
| spark.executor.extraJavaOptions | A string of extra JVM options to pass to executors. For instance **NOTE**: You can enter multiple values separated by space. | `-Dcarbon.properties.filepath = carbon.properties` |
| spark.executor.extraClassPath | Extra classpath entries to prepend to the classpath of executors. **NOTE**: If SPARK\_CLASSPATH is defined in spark-env.sh, then comment it and append the values in below parameter spark.driver.extraClassPath | `carbondata.tar.gz/carbonlib/*` |
| spark.driver.extraClassPath | Extra classpath entries to prepend to the classpath of the driver. **NOTE**: If SPARK\_CLASSPATH is defined in spark-env.sh, then comment it and append the value in below parameter spark.driver.extraClassPath. | `$SPARK_HOME/carbonlib/*` |
| spark.driver.extraJavaOptions | A string of extra JVM options to pass to the driver. For instance, GC settings or other logging. | `-Dcarbon.properties.filepath = $SPARK_HOME/conf/carbon.properties` |

5. Verify the installation.

```
./bin/spark-shell \
--master yarn-client \
--driver-memory 1G \
--executor-memory 2G \
--executor-cores 2
```

> [!NOTE]
> :

- property "carbon.storelocation" is deprecated in carbondata 2.0 version. Only the users who used this property in previous versions can still use it in carbon 2.0 version.
- Make sure you have permissions for CarbonData JARs and files through which driver and executor will start.
- If use Spark + Hive 1.1.X, it needs to add carbondata assembly jar and carbondata-hive jar into parameter 'spark.sql.hive.metastore.jars' in spark-default.conf file.

<a id="quick-start-guide--query-execution-using-carbondata-thrift-server"></a>

## Query Execution Using CarbonData Thrift Server

<a id="quick-start-guide--starting-carbondata-thrift-server."></a>

### Starting CarbonData Thrift Server.

a. cd `$SPARK_HOME`

b. Run the following command to start the CarbonData thrift server.

```
./bin/spark-submit \
--class org.apache.carbondata.spark.thriftserver.CarbonThriftServer \
$SPARK_HOME/carbonlib/$CARBON_ASSEMBLY_JAR
```

| Parameter | Description | Example |
| --- | --- | --- |
| CARBON\_ASSEMBLY\_JAR | CarbonData assembly jar name present in the `$SPARK_HOME/carbonlib/` folder. | apache-carbondata-xx.jar |

c. Run the following command to work with S3 storage.

```
./bin/spark-submit \
--class org.apache.carbondata.spark.thriftserver.CarbonThriftServer \
$SPARK_HOME/carbonlib/$CARBON_ASSEMBLY_JAR <access_key> <secret_key> <endpoint>
```

| Parameter | Description | Example |
| --- | --- | --- |
| CARBON\_ASSEMBLY\_JAR | CarbonData assembly jar name present in the `$SPARK_HOME/carbonlib/` folder. | apache-carbondata-xx.jar |
| access\_key | Access key for S3 storage |  |
| secret\_key | Secret key for S3 storage |  |
| endpoint | Endpoint for connecting to S3 storage |  |

> [!NOTE]
> : From Spark 1.6, by default the Thrift server runs in multi-session mode. Which means each JDBC/ODBC connection owns a copy of their own SQL configuration and temporary function registry. Cached tables are still shared though. If you prefer to run the Thrift server in single-session mode and share all SQL configuration and temporary function registry, please set option `spark.sql.hive.thriftServer.singleSession` to `true`. You may either add this option to `spark-defaults.conf`, or pass it to `spark-submit.sh` via `--conf`:

```
./bin/spark-submit \
--conf spark.sql.hive.thriftServer.singleSession=true \
--class org.apache.carbondata.spark.thriftserver.CarbonThriftServer \
$SPARK_HOME/carbonlib/$CARBON_ASSEMBLY_JAR
```

**But** in single-session mode, if one user changes the database from one connection, the database of the other connections will be changed too.

**Examples**

- Start with default memory and executors.

```
./bin/spark-submit \
--class org.apache.carbondata.spark.thriftserver.CarbonThriftServer \
$SPARK_HOME/carbonlib/apache-carbondata-xxx.jar
```

- Start with Fixed executors and resources.

```
./bin/spark-submit \
--class org.apache.carbondata.spark.thriftserver.CarbonThriftServer \
--num-executors 3 \
--driver-memory 20G \
--executor-memory 250G \
--executor-cores 32 \
$SPARK_HOME/carbonlib/apache-carbondata-xxx.jar
```

<a id="quick-start-guide--connecting-to-carbondata-thrift-server-using-beeline."></a>

### Connecting to CarbonData Thrift Server Using Beeline.

```
cd $SPARK_HOME
./sbin/start-thriftserver.sh
./bin/beeline -u jdbc:hive2://<thriftserver_host>:port

Example
./bin/beeline -u jdbc:hive2://10.10.10.10:10000
```

<a id="quick-start-guide--installing-and-configuring-carbondata-on-presto"></a>

## Installing and Configuring CarbonData on Presto

**NOTE:** **CarbonData tables cannot be created nor loaded from Presto. User needs to create CarbonData Table and load data into it
either with [Spark](#quick-start-guide--installing-and-configuring-carbondata-to-run-locally-with-spark-shell) or [SDK](#sdk-guide) or [C++ SDK](#csdk-guide).
Once the table is created, it can be queried from Presto.**

Please refer the presto guide linked below.

prestodb guide - [prestodb](#prestodb-guide)

prestosql guide - [prestosql](#prestosql-guide)

Once installed the presto with carbonData as per the above guide, you can use the Presto CLI on the coordinator to query data sources in the catalog using the Presto workers.

List the schemas(databases) available

```
show schemas;
```

Selected the schema where CarbonData table resides

```
use carbonschema;
```

List the available tables

```
show tables;
```

Query from the available tables

```
select * from carbon_table;
```

**Note:** Create Tables and data loads should be done before executing queries as we can not create carbon table from this interface.

[Top](#quick-start-guide--top)

---

<a id="usecases"></a>

<!-- source_url: https://carbondata.apache.org/usecases.html -->

<!-- page_index: 3 -->

<a id="usecases--use-cases"></a>

# Use Cases

CarbonData is useful in various analytical work loads.Some of the most typical usecases where CarbonData is being used is documented here.

CarbonData is used for but not limited to

- <a id="usecases--bank"></a>

  ### Bank

  - fraud detection analysis
  - risk profile analysis
  - As a zip table to update the daily balance of customers
- <a id="usecases--telecom"></a>

  ### Telecom

  - Detection of signal anamolies for VIP customers for providing improved customer experience
  - Analysis of MR,CHR records of GSM data to determine the tower load at a particular time period and rebalance the tower configuration
  - Analysis of access sites, video, screen size, streaming bandwidth, quality to determine the network quality,routing configuration
- <a id="usecases--web-internet"></a>

  ### Web/Internet

  - Analysis of page or video being accessed,server loads, streaming quality, screen size
- <a id="usecases--smart-city"></a>

  ### Smart City

  - Vehicle tracking analysis
  - Unusual behaviour analysis

These use cases can be broadly classified into below categories:

- Full scan/Detailed/Interactive queries
- Aggregation/OLAP BI queries
- Real time Ingestion(Streaming) and queries

<a id="usecases--detailed-queries-in-the-telecom-scenario"></a>

## Detailed Queries in the Telecom scenario

<a id="usecases--scenario"></a>

### Scenario

User wants to analyse all the CHR(Call History Record) and MR(Measurement Records) of the mobile subscribers in order to identify the service failures within 10 secs. Also user wants to run machine learning models on the data to fairly estimate the reasons and time of probable failures and take action ahead to meet the SLA(Service Level Agreements) of VIP customers.

<a id="usecases--challenges"></a>

### Challenges

- Data incoming rate might vary based on the user concentration at a particular period of time.Hence higher data load speeds are required
- Cluster needs to be well utilised and share the cluster among various applications for better resource consumption and savings
- Queries needs to be interactive.ie., the queries fetch small data and need to be returned in seconds
- Data Loaded into the system every few minutes.

<a id="usecases--solution"></a>

### Solution

Setup a Hadoop + Spark + CarbonData cluster managed by YARN.

Proposed the following configurations for CarbonData.(These tunings were proposed before CarbonData introduced SORT\_COLUMNS parameter using which the sort order and schema order could be different.)

Add the frequently used columns to the left of the table definition. Add it in the increasing order of cardinality. It was suggested to keep msisdn,imsi columns in the beginning of the schema. With latest CarbonData, SORT\_COLUMNS needs to be configured msisdn,imsi in the beginning.

Add timestamp column to the right of the schema as it is naturally increasing.

Create two separate YARN queues for Query and Data Loading.

Apart from these, the following CarbonData configuration was suggested to be configured in the cluster.

| Configuration for | Parameter | Value | Description |
| --- | --- | --- | --- |
| Data Loading | carbon.number.of.cores.while.loading | 12 | More cores can improve data loading speed |
| Data Loading | carbon.sort.size | 100000 | Number of records to sort at a time.More number of records configured will lead to increased memory foot print |
| Data Loading | table\_blocksize | 256 | To efficiently schedule multiple tasks during query |
| Data Loading | carbon.sort.intermediate.files.limit | 100 | Increased to 100 as number of cores are more.Can perform merging in backgorund.If less number of files to merge, sort threads would be idle |
| Data Loading | carbon.use.local.dir | TRUE | yarn application directory will be usually on a single disk.YARN would be configured with multiple disks to be used as temp or to assign randomly to applications. Using the yarn temp directory will allow carbon to use multiple disks and improve IO performance |
| Compaction | carbon.compaction.level.threshold | 6,6 | Since frequent small loads, compacting more segments will give better query results |
| Compaction | carbon.enable.auto.load.merge | true | Since data loading is small,auto compacting keeps the number of segments less and also compaction can complete in time |
| Compaction | carbon.number.of.cores.while.compacting | 4 | Higher number of cores can improve the compaction speed |
| Compaction | carbon.major.compaction.size | 921600 | Sum of several loads to combine into single segment |

<a id="usecases--results-achieved"></a>

### Results Achieved

| Parameter | Results |
| --- | --- |
| Query | < 3 Sec |
| Data Loading Speed | 40 MB/s Per Node |
| Concurrent query performance (20 queries) | < 10 Sec |

<a id="usecases--detailed-queries-in-the-smart-city-scenario"></a>

## Detailed Queries in the Smart City scenario

<a id="usecases--scenario-2"></a>

### Scenario

User wants to analyse the person/vehicle movement and behavior during a certain time period. This output data needs to be joined with a external table for Human details extraction. The query will be run with different time period as filter to identify potential behavior mismatch.

<a id="usecases--challenges-2"></a>

### Challenges

Data generated per day is very huge.Data needs to be loaded multiple times per day to accomodate the incoming data size.

Data Loading done once in 6 hours.

<a id="usecases--solution-2"></a>

### Solution

Setup a Hadoop + Spark + CarbonData cluster managed by YARN.

Since data needs to be queried for a time period, it was recommended to keep the time column at the beginning of schema.

Use table block size as 512MB.

Use local sort mode.

Apart from these, the following CarbonData configuration was suggested to be configured in the cluster.

Use all columns are no-dictionary as the cardinality is high.

| Configuration for | Parameter | Value | Description |
| --- | --- | --- | --- |
| Data Loading | enable.unsafe.sort | TRUE | Temporary data generated during sort is huge which causes GC bottlenecks. Using unsafe reduces the pressure on GC |
| Data Loading | enable.offheap.sort | TRUE | Temporary data generated during sort is huge which causes GC bottlenecks. Using offheap reduces the pressure on GC.offheap can be accessed through java unsafe.hence enable.unsafe.sort needs to be true |
| Data Loading | offheap.sort.chunk.size.in.mb | 128 | Size of memory to allocate for sorting.Can increase this based on the memory available |
| Data Loading | carbon.number.of.cores.while.loading | 12 | Higher cores can improve data loading speed |
| Data Loading | carbon.sort.size | 100000 | Number of records to sort at a time.More number of records configured will lead to increased memory foot print |
| Data Loading | table\_blocksize | 512 | To efficiently schedule multiple tasks during query. This size depends on data scenario.If data is such that the filters would select less number of blocklets to scan, keeping higher number works well.If the number blocklets to scan is more, better to reduce the size as more tasks can be scheduled in parallel. |
| Data Loading | carbon.sort.intermediate.files.limit | 100 | Increased to 100 as number of cores are more.Can perform merging in backgorund.If less number of files to merge, sort threads would be idle |
| Data Loading | carbon.use.local.dir | TRUE | yarn application directory will be usually on a single disk.YARN would be configured with multiple disks to be used as temp or to assign randomly to applications. Using the yarn temp directory will allow carbon to use multiple disks and improve IO performance |
| Data Loading | sort.inmemory.size.inmb | 92160 | Memory allocated to do inmemory sorting. When more memory is available in the node, configuring this will retain more sort blocks in memory so that the merge sort is faster due to no/very less IO |
| Compaction | carbon.major.compaction.size | 921600 | Sum of several loads to combine into single segment |
| Compaction | carbon.number.of.cores.while.compacting | 12 | Higher number of cores can improve the compaction speed.Data size is huge.Compaction need to use more threads to speed up the process |
| Compaction | carbon.enable.auto.load.merge | FALSE | Doing auto minor compaction is costly process as data size is huge.Perform manual compaction when the cluster is less loaded |
| Query | carbon.enable.vector.reader | true | To fetch results faster, supporting spark vector processing will speed up the query |
| Query | enable.unsafe.in.query.processing | true | Data that needs to be scanned in huge which in turn generates more short lived Java objects. This cause pressure of GC.using unsafe and offheap will reduce the GC overhead |
| Query | use.offheap.in.query.processing | true | Data that needs to be scanned in huge which in turn generates more short lived Java objects. This cause pressure of GC.using unsafe and offheap will reduce the GC overhead.offheap can be accessed through java unsafe.hence enable.unsafe.in.query.processing needs to be true |
| Query | enable.unsafe.columnpage | TRUE | Keep the column pages in offheap memory so that the memory overhead due to java object is less and also reduces GC pressure. |
| Query | carbon.unsafe.working.memory.in.mb | 10240 | Amount of memory to use for offheap operations, you can increase this memory based on the data size |

<a id="usecases--results-achieved-2"></a>

### Results Achieved

| Parameter | Results |
| --- | --- |
| Query (Time Period spanning 1 segment) | < 10 Sec |
| Data Loading Speed | 45 MB/s Per Node |

<a id="usecases--olap-bi-queries-in-the-web-internet-scenario"></a>

## OLAP/BI Queries in the web/Internet scenario

<a id="usecases--scenario-3"></a>

### Scenario

An Internet company wants to analyze the average download speed, kind of handsets used in a particular region/area,kind of Apps being used, what kind of videos are trending in a particular region to enable them to identify the appropriate resolution size of videos to speed up transfer, and perform many more analysis to serve th customers better.

<a id="usecases--challenges-3"></a>

### Challenges

Since data is being queried by a BI tool, all the queries contain group by, which means CarbonData need to return more records as limit cannot be pushed down to carbondata layer.

Results have to be returned faster as the BI tool would not respond till the data is fetched, causing bad user experience.

Data might be loaded less frequently(once or twice in a day), but raw data size is huge, which causes the group by queries to run slower.

Concurrent queries can be more due to the BI dashboard

<a id="usecases--goal"></a>

### Goal

1. Aggregation queries are faster
2. Concurrency is high(Number of concurrent queries supported)

<a id="usecases--solution-3"></a>

### Solution

- Use table block size as 128MB so that pruning is more effective
- Use global sort mode so that the data to be fetched are grouped together
- Create Materialized View for aggregation queries
- Reduce the Spark shuffle partitions.(In our configuration on 14 node cluster, it was reduced to 35 from default of 200)
- For columns whose cardinality is high,enable the local dictionary so that store size is less and can take dictionary benefit for scan

<a id="usecases--handling-near-realtime-data-ingestion-scenario"></a>

## Handling near realtime data ingestion scenario

<a id="usecases--scenario-4"></a>

### Scenario

Need to support storing of continously arriving data and make it available immediately for query.

<a id="usecases--challenges-4"></a>

### Challenges

When the data ingestion is near real time and the data needs to be available for query immediately, usual scenario is to do data loading in micro batches.But this causes the problem of generating many small files. This poses two problems:

1. Small file handling in HDFS is inefficient
2. CarbonData will suffer in query performance as all the small files will have to be queried when filter is on non time column

CarbonData will suffer in query performance as all the small files will have to be queried when filter is on non time column.

Since data is continously arriving, allocating resources for compaction might not be feasible.

<a id="usecases--goal-2"></a>

### Goal

1. Data is available in near real time for query as it arrives
2. CarbonData doesnt suffer from small files problem

<a id="usecases--solution-4"></a>

### Solution

- Use Streaming tables support of CarbonData
- Configure the carbon.streaming.segment.max.size property to higher value(default is 1GB) if a bit slower query performance is not a concern
- Configure carbon.streaming.auto.handoff.enabled to true so that after the carbon.streaming.segment.max.size is reached, the segment is converted into format optimized for query
- Disable auto compaction.Manually trigger the minor compaction with default 4,3 when the cluster is not busy
- Manually trigger Major compaction based on the size of segments and the frequency with which the segments are being created
- Enable local dictionary

[Top](#usecases--top)

---

<a id="language-manual"></a>

<!-- source_url: https://carbondata.apache.org/language-manual.html -->

<!-- page_index: 4 -->

<a id="language-manual--overview"></a>

# Overview

CarbonData has its own parser, in addition to Spark's SQL Parser, to parse and process certain Commands related to CarbonData table handling. You can interact with the SQL interface using the [command-line](https://spark.apache.org/docs/latest/sql-programming-guide.html#running-the-spark-sql-cli) or over [JDBC/ODBC](https://spark.apache.org/docs/latest/sql-programming-guide.html#running-the-thrift-jdbcodbc-server).

- [Data Types](#supported-data-types-in-carbondata)
- Data Definition Statements
  - [DDL:](#ddl-of-carbondata)
[Create](#ddl-of-carbondata--create-table),[Drop](#ddl-of-carbondata--drop-table),[Partition](#ddl-of-carbondata--partition),[Bucketing](#ddl-of-carbondata--bucketing),[Alter](#ddl-of-carbondata--alter-table),[CTAS](#ddl-of-carbondata--create-table-as-select),[External Table](#ddl-of-carbondata--create-external-table)
  - [Index](#index-management)
    - [Bloom](#bloomfilter-index-guide)
    - [Lucene](#lucene-index-guide)
    - [Secondary-index](#secondary-index-guide)
  - [Materialized Views](#mv-guide)
  - [Streaming](#streaming-guide)
- Data Manipulation Statements
  - [DML:](#dml-of-carbondata) [Load](#dml-of-carbondata--load-data), [Insert](#dml-of-carbondata--insert-data-into-carbondata-table), [Update](#dml-of-carbondata--update), [Delete](#dml-of-carbondata--delete)
  - [Segment Management](https://carbondata.apache.org/segment-management-on-carbondata.html)
- [CarbonData as Spark's Datasource](https://carbondata.apache.org/carbon-as-spark-datasource-guide.html)
- [Configuration Properties](#configuration-parameters)

[Top](#language-manual--top)

---

<a id="ddl-of-carbondata"></a>

<!-- source_url: https://carbondata.apache.org/ddl-of-carbondata.html -->

<!-- page_index: 5 -->

<a id="ddl-of-carbondata--carbondata-data-definition-language"></a>

# CarbonData Data Definition Language

CarbonData DDL statements are documented here,which includes:

- [CREATE TABLE](#ddl-of-carbondata--create-table)

  - [Local Dictionary](#ddl-of-carbondata--local-dictionary-configuration)
  - [Inverted Index](#ddl-of-carbondata--inverted-index-configuration)
  - [Sort Columns](#ddl-of-carbondata--sort-columns-configuration)
  - [Sort Scope](#ddl-of-carbondata--sort-scope-configuration)
  - [Table Block Size](#ddl-of-carbondata--table-block-size-configuration)
  - [Table Compaction](#ddl-of-carbondata--table-compaction-configuration)
  - [Streaming](#ddl-of-carbondata--streaming)
  - [Caching Column Min/Max](#ddl-of-carbondata--caching-minmax-value-for-required-columns)
  - [Caching Level](#ddl-of-carbondata--caching-at-block-or-blocklet-level)
  - [Hive/Parquet folder Structure](#ddl-of-carbondata--support-flat-folder-same-as-hiveparquet)
  - [Long String columns](#ddl-of-carbondata--string-longer-than-32000-characters)
  - [Compression for Table](#ddl-of-carbondata--compression-for-table)
  - [Bad Records Path](#ddl-of-carbondata--bad-records-path)
  - [Load Minimum Input File Size](#ddl-of-carbondata--load-minimum-data-size)
  - [Range Column](#ddl-of-carbondata--range-column)
  - [Index Cache Expiration Time In Seconds](#ddl-of-carbondata--index-cache-expiration-time-in-seconds)
- [CREATE TABLE AS SELECT](#ddl-of-carbondata--create-table-as-select)
- [CREATE EXTERNAL TABLE](#ddl-of-carbondata--create-external-table)

  - [External Table on Transactional table location](#ddl-of-carbondata--create-external-table-on-managed-table-data-location)
  - [External Table on non-transactional table location](#ddl-of-carbondata--create-external-table-on-non-transactional-table-data-location)
- [CREATE DATABASE](#ddl-of-carbondata--create-database)
- [TABLE MANAGEMENT](#ddl-of-carbondata--table-management)

  - [SHOW TABLE](#ddl-of-carbondata--show-table)
  - [ALTER TABLE](#ddl-of-carbondata--alter-table)
    - [RENAME TABLE](#ddl-of-carbondata--rename-table)
    - [ADD COLUMNS](#ddl-of-carbondata--add-columns)
    - [DROP COLUMNS](#ddl-of-carbondata--drop-columns)
    - [RENAME COLUMN](#ddl-of-carbondata--change-column-nametype)
    - [CHANGE COLUMN NAME/TYPE](#ddl-of-carbondata--change-column-nametype)
    - [MERGE INDEXES](#ddl-of-carbondata--merge-index)
    - [SET/UNSET](#ddl-of-carbondata--set-and-unset)
  - [DROP TABLE](#ddl-of-carbondata--drop-table)
  - [REFRESH TABLE](#ddl-of-carbondata--refresh-table)
  - [COMMENTS](#ddl-of-carbondata--table-and-column-comment)
- [PARTITION](#ddl-of-carbondata--partition)

  - [STANDARD PARTITION(HIVE)](#ddl-of-carbondata--standard-partition)
    - [INSERT OVERWRITE PARTITION](#ddl-of-carbondata--insert-overwrite)
  - [SHOW PARTITIONS](#ddl-of-carbondata--show-partitions)
  - [ADD PARTITION](#ddl-of-carbondata--add-a-new-partition)
  - [SPLIT PARTITION](#ddl-of-carbondata--split-a-partition)
  - [DROP PARTITION](#ddl-of-carbondata--drop-a-partition)
- [BUCKETING](#ddl-of-carbondata--bucketing)
- [CACHE](#ddl-of-carbondata--cache)

<a id="ddl-of-carbondata--create-table"></a>

## CREATE TABLE

This command can be used to create a CarbonData table by specifying the list of fields along with the table properties. You can also specify the location where the table needs to be stored.

```
CREATE TABLE [IF NOT EXISTS] [db_name.]table_name[(col_name data_type , ...)]
STORED AS carbondata
[TBLPROPERTIES (property_name=property_value, ...)]
[LOCATION 'path']
```

**NOTE:** CarbonData also supports "STORED AS carbondata" and "USING carbondata". Find example code at [CarbonSessionExample](https://github.com/apache/carbondata/blob/master/examples/spark/src/main/scala/org/apache/carbondata/examples/CarbonSessionExample.scala) in the CarbonData repo.

<a id="ddl-of-carbondata--usage-guidelines"></a>

### Usage Guidelines

**Supported properties:**

| Property | Description |
| --- | --- |
| [NO\_INVERTED\_INDEX](#ddl-of-carbondata--inverted-index-configuration) | Columns to exclude from inverted index generation |
| [INVERTED\_INDEX](#ddl-of-carbondata--inverted-index-configuration) | Columns to include for inverted index generation |
| [SORT\_COLUMNS](#ddl-of-carbondata--sort-columns-configuration) | Columns to include in sort and its order of sort |
| [SORT\_SCOPE](#ddl-of-carbondata--sort-scope-configuration) | Sort scope of the load.Options include no sort, local sort ,batch sort and global sort |
| [TABLE\_BLOCKSIZE](#ddl-of-carbondata--table-block-size-configuration) | Size of blocks to write onto hdfs |
| [TABLE\_BLOCKLET\_SIZE](#ddl-of-carbondata--table-blocklet-size-configuration) | Size of blocklet to write in the file |
| [TABLE\_PAGE\_SIZE\_INMB](#ddl-of-carbondata--table-page-size-configuration) | Size of page in MB; if page size crosses this value before 32000 rows, page will be cut to this many rows and remaining rows are processed in the subsequent pages. This helps in keeping page size to fit in cpu cache size |
| [MAJOR\_COMPACTION\_SIZE](#ddl-of-carbondata--table-compaction-configuration) | Size upto which the segments can be combined into one |
| [AUTO\_LOAD\_MERGE](#ddl-of-carbondata--table-compaction-configuration) | Whether to auto compact the segments |
| [COMPACTION\_LEVEL\_THRESHOLD](#ddl-of-carbondata--table-compaction-configuration) | Number of segments to compact into one segment |
| [COMPACTION\_PRESERVE\_SEGMENTS](#ddl-of-carbondata--table-compaction-configuration) | Number of latest segments that needs to be excluded from compaction |
| [ALLOWED\_COMPACTION\_DAYS](#ddl-of-carbondata--table-compaction-configuration) | Segments generated within the configured time limit in days will be compacted, skipping others |
| [STREAMING](#ddl-of-carbondata--streaming) | Whether the table is a streaming table |
| [LOCAL\_DICTIONARY\_ENABLE](#ddl-of-carbondata--local-dictionary-configuration) | Enable local dictionary generation |
| [LOCAL\_DICTIONARY\_THRESHOLD](#ddl-of-carbondata--local-dictionary-configuration) | Cardinality upto which the local dictionary can be generated |
| [LOCAL\_DICTIONARY\_INCLUDE](#ddl-of-carbondata--local-dictionary-configuration) | Columns for which local dictionary needs to be generated. Useful when local dictionary need not be generated for all string/varchar/char columns |
| [LOCAL\_DICTIONARY\_EXCLUDE](#ddl-of-carbondata--local-dictionary-configuration) | Columns for which local dictionary generation should be skipped. Useful when local dictionary need not be generated for few string/varchar/char columns |
| [COLUMN\_META\_CACHE](#ddl-of-carbondata--caching-minmax-value-for-required-columns) | Columns whose metadata can be cached in Driver for efficient pruning and improved query performance |
| [CACHE\_LEVEL](#ddl-of-carbondata--caching-at-block-or-blocklet-level) | Column metadata caching level. Whether to cache column metadata of block or blocklet |
| [FLAT\_FOLDER](#ddl-of-carbondata--support-flat-folder-same-as-hiveparquet) | Whether to write all the carbondata files in a single folder.Not writing segments folder during incremental load |
| [LONG\_STRING\_COLUMNS](#ddl-of-carbondata--string-longer-than-32000-characters) | Columns which are greater than 32K characters |
| [BUCKET\_NUMBER](#ddl-of-carbondata--bucketing) | Number of buckets to be created |
| [BUCKET\_COLUMNS](#ddl-of-carbondata--bucketing) | Columns which are to be placed in buckets |
| [LOAD\_MIN\_SIZE\_INMB](#ddl-of-carbondata--load-minimum-data-size) | Minimum input data size per node for data loading |
| [Range Column](#ddl-of-carbondata--range-column) | partition input data by range |
| [INDEX\_CACHE\_EXPIRATION\_TIME\_IN\_SECONDS](#ddl-of-carbondata--index-cache-expiration-time-in-seconds) | Table level time-based cache expiration in seconds |

Following are the guidelines for TBLPROPERTIES, CarbonData's additional table options can be set via carbon.properties.

- <a id="ddl-of-carbondata--local-dictionary-configuration"></a>

  ##### Local Dictionary Configuration

Columns for which dictionary is not generated needs more storage space and in turn more IO. Also since more data will have to be read during query, query performance also would suffer. Generating dictionary per blocklet for such columns would help in saving storage space and assist in improving query performance as carbondata is optimized for handling dictionary encoded columns more effectively.Generating dictionary internally per blocklet is termed as local dictionary. Please refer to [File structure of Carbondata](https://carbondata.apache.org/file-structure-of-carbondata.html) for understanding about the file structure of carbondata and meaning of terms like blocklet.

Local Dictionary helps in:

1. Getting more compression.
2. Filter queries and full scan queries will be faster as filter will be done on encoded data.
3. Reducing the store size and memory footprint as only unique values will be stored as part of local dictionary and corresponding data will be stored as encoded data.
4. Getting higher IO throughput.

**NOTE:**

- Following Data Types are Supported for Local Dictionary:

  - STRING
  - VARCHAR
  - CHAR
- Following Data Types are not Supported for Local Dictionary:

  - SMALLINT
  - INTEGER
  - BIGINT
  - DOUBLE
  - DECIMAL
  - TIMESTAMP
  - DATE
  - BOOLEAN
  - FLOAT
  - BYTE
  - Binary
- In case of multi-level complex dataType columns, primitive string/varchar/char columns are considered for local dictionary generation.

System Level Properties for Local Dictionary:

| Properties | Default value | Description |
| --- | --- | --- |
| carbon.local.dictionary.enable | true | By default, Local Dictionary will be enabled for the carbondata table. |
| carbon.local.dictionary.decoder.fallback | true | Page Level data will not be maintained for the blocklet. During fallback, actual data will be retrieved from the encoded page data using local dictionary. **NOTE:** Memory footprint decreases significantly as compared to when this property is set to false |

Local Dictionary can be configured using the following properties during create table command:

| Properties | Default value | Description |
| --- | --- | --- |
| LOCAL\_DICTIONARY\_ENABLE | false | Whether to enable local dictionary generation. **NOTE:** If this property is defined, it will override the value configured at system level by '***carbon.local.dictionary.enable***'.Local dictionary will be generated for all string/varchar/char columns unless LOCAL\_DICTIONARY\_INCLUDE, LOCAL\_DICTIONARY\_EXCLUDE is configured. |
| LOCAL\_DICTIONARY\_THRESHOLD | 10000 | The maximum cardinality of a column upto which carbondata can try to generate local dictionary (maximum - 100000). **NOTE:** When LOCAL\_DICTIONARY\_THRESHOLD is defined for Complex columns, the count of distinct records of all child columns are summed up. |
| LOCAL\_DICTIONARY\_INCLUDE | string/varchar/char columns | Columns for which Local Dictionary has to be generated. This property needs to be configured only when local dictionary needs to be generated for few columns, skipping others. This property takes effect only when **LOCAL\_DICTIONARY\_ENABLE** is true or **carbon.local.dictionary.enable** is true |
| LOCAL\_DICTIONARY\_EXCLUDE | none | Columns for which Local Dictionary need not be generated. This property needs to be configured only when local dictionary needs to be skipped for few columns, generating for others. This property takes effect only when **LOCAL\_DICTIONARY\_ENABLE** is true or **carbon.local.dictionary.enable** is true |

**Fallback behavior:**

- When the cardinality of a column exceeds the threshold, it triggers a fallback and the generated dictionary will be reverted and data loading will be continued without dictionary encoding.
- In case of complex columns, fallback is triggered when the summation value of all child columns' distinct records exceeds the defined LOCAL\_DICTIONARY\_THRESHOLD value.

**NOTE:** When fallback is triggered, the data loading performance will decrease as encoded data will be discarded and the actual data is written to the temporary sort files.

**Points to be noted:**

- Reduce Block size:

  Number of Blocks generated is less in case of Local Dictionary as compression ratio is high. This may reduce the number of tasks launched during query, resulting in degradation of query performance if the pruned blocks are less compared to the number of parallel tasks which can be run. So it is recommended to configure smaller block size which in turn generates more number of blocks.

<a id="ddl-of-carbondata--example:"></a>

### Example:

```
CREATE TABLE carbontable(             
  column1 string,             
  column2 string,             
  column3 LONG)
STORED AS carbondata
TBLPROPERTIES('LOCAL_DICTIONARY_ENABLE'='true','LOCAL_DICTIONARY_THRESHOLD'='1000',
'LOCAL_DICTIONARY_INCLUDE'='column1','LOCAL_DICTIONARY_EXCLUDE'='column2')
```

**NOTE:**

- We recommend to use Local Dictionary when cardinality is high but is distributed across multiple loads

- <a id="ddl-of-carbondata--inverted-index-configuration"></a>

  ##### Inverted Index Configuration

  By default inverted index is disabled as store size will be reduced, it can be enabled by using a table property. It might help to improve compression ratio and query speed, especially for low cardinality columns which are in reward position.
  Suggested use cases : For high cardinality columns, you can disable the inverted index for improving the data loading performance.


> [!NOTE]
> : Columns specified in INVERTED\_INDEX should also be present in SORT\_COLUMNS.


```
TBLPROPERTIES ('SORT_COLUMNS'='column2,column3', 'INVERTED_INDEX'='column2, column3')
```

- <a id="ddl-of-carbondata--sort-columns-configuration"></a>

  ##### Sort Columns Configuration

  This property is for users to specify which columns belong to the MDK(Multi-Dimensions-Key) index.

  - If users don't specify "SORT\_COLUMNS" property, by default no columns are sorted
  - If this property is specified but with empty argument, then the table will be loaded without sort.
  - This supports only string, date, timestamp, short, int, long, byte and boolean data types.
    Suggested use cases : Only build MDK index for required columns,it might help to improve the data loading performance.
```
TBLPROPERTIES ('SORT_COLUMNS'='column1, column3')
```


> [!NOTE]
> : Sort\_Columns for Complex datatype columns, binary, double, float, decimal data type is not supported.

- <a id="ddl-of-carbondata--sort-scope-configuration"></a>

  ##### Sort Scope Configuration

  This property is for users to specify the scope of the sort during data load, following are the types of sort scope.

  - LOCAL\_SORT: data will be locally sorted (task level sorting)
  - NO\_SORT: default scope. It will load the data in unsorted manner, it will significantly increase load performance.
  - GLOBAL\_SORT: It increases the query performance, especially high concurrent point query.
    And if you care about loading resources isolation strictly, because the system uses the spark GroupBy to sort data, the resource can be controlled by spark.

<a id="ddl-of-carbondata--example:-2"></a>

### Example:

```
CREATE TABLE IF NOT EXISTS productSchema.productSalesTable (
  productNumber INT,
  productName STRING,
  storeCity STRING,
  storeProvince STRING,
  productCategory STRING,
  productBatch STRING,
  saleQuantity INT,
  revenue INT)
STORED AS carbondata
TBLPROPERTIES ('SORT_COLUMNS'='productName,storeCity',
               'SORT_SCOPE'='LOCAL_SORT')
```

**NOTE:** CarbonData also supports "using carbondata". Find example code at [SparkSessionExample](https://github.com/apache/carbondata/blob/master/examples/spark/src/main/scala/org/apache/carbondata/examples/SparkSessionExample.scala) in the CarbonData repo.

- <a id="ddl-of-carbondata--table-block-size-configuration"></a>

  ##### Table Block Size Configuration

  This property is for setting block size of this table, the default value is 1024 MB and supports a range of 1 MB to 2048 MB.


```
TBLPROPERTIES ('TABLE_BLOCKSIZE'='512')
```

  **NOTE:** 512 or 512M both are accepted.
- <a id="ddl-of-carbondata--table-blocklet-size-configuration"></a>

  ##### Table Blocklet Size Configuration

  This property is for setting blocklet size in the carbondata file, the default value is 64 MB.
  Blocklet is the minimum IO read unit, in case of point queries reduce blocklet size might improve the query performance.

  Example usage:


```
TBLPROPERTIES ('TABLE_BLOCKLET_SIZE'='8')
```

- <a id="ddl-of-carbondata--table-page-size-configuration"></a>

  ##### Table page Size Configuration

  This property is for setting page size in the carbondata file
  and supports a range of 1 MB to 1755 MB.
  If page size crosses this value before 32000 rows, page will be cut to that many rows.
  Helps in keeping page size to fit cpu cache size.

  This property can be configured if the table has string, varchar, binary or complex datatype columns.
  Because for these columns 32000 rows in one page may exceed 1755 MB and snappy compression will fail in that scenario.
  Also if page size is huge, page cannot be fit in CPU cache.
  So, configuring smaller values of this property (say 1 MB) can result in better use of CPU cache for pages.

  Example usage:


```
TBLPROPERTIES ('TABLE_PAGE_SIZE_INMB'='5')
```

- <a id="ddl-of-carbondata--table-compaction-configuration"></a>

  ##### Table Compaction Configuration

  These properties are table level compaction configurations, if not specified, system level configurations in carbon.properties will be used.
  Following are 5 configurations:

  - MAJOR\_COMPACTION\_SIZE: same meaning as carbon.major.compaction.size, size in MB.
  - AUTO\_LOAD\_MERGE: same meaning as carbon.enable.auto.load.merge.
  - COMPACTION\_LEVEL\_THRESHOLD: same meaning as carbon.compaction.level.threshold.
  - COMPACTION\_PRESERVE\_SEGMENTS: same meaning as carbon.numberof.preserve.segments.
  - ALLOWED\_COMPACTION\_DAYS: same meaning as carbon.allowed.compaction.days.
```
TBLPROPERTIES ('MAJOR_COMPACTION_SIZE'='2048',
               'AUTO_LOAD_MERGE'='true',
               'COMPACTION_LEVEL_THRESHOLD'='5,6',
               'COMPACTION_PRESERVE_SEGMENTS'='10',
               'ALLOWED_COMPACTION_DAYS'='5')
```

- <a id="ddl-of-carbondata--streaming"></a>

  ##### Streaming

  CarbonData supports streaming ingestion for real-time data. You can create the 'streaming' table using the following table properties.


```
TBLPROPERTIES ('streaming'='true')
```

- <a id="ddl-of-carbondata--caching-min-max-value-for-required-columns"></a>

  ##### Caching Min/Max Value for Required Columns

  By default, CarbonData caches min and max values of all the columns in schema. As the load increases, the memory required to hold the min and max values increases considerably. This feature enables you to configure min and max values only for the required columns, resulting in optimized memory usage. This feature doesn't support binary data type.

  Following are the valid values for COLUMN\_META\_CACHE:

  - If you want no column min/max values to be cached in the driver.
```
COLUMN_META_CACHE=''
```

  - If you want only col1 min/max values to be cached in the driver.
```
COLUMN_META_CACHE='col1'
```

  - If you want min/max values to be cached in driver for all the specified columns.
```
COLUMN_META_CACHE='col1,col2,col3,?'
```

  Columns to be cached can be specified either while creating table or after creation of the table.
  During create table operation; specify the columns to be cached in table properties.

  Syntax:


```
CREATE TABLE [dbName].tableName (col1 String, col2 String, col3 int,?) STORED AS carbondata TBLPROPERTIES ('COLUMN_META_CACHE'='col1,col2,?')
```

  Example:


```
CREATE TABLE employee (name String, city String, id int) STORED AS carbondata TBLPROPERTIES ('COLUMN_META_CACHE'='name')
```

  After creation of table or on already created tables use the alter table command to configure the columns to be cached.

  Syntax:


```
ALTER TABLE [dbName].tableName SET TBLPROPERTIES ('COLUMN_META_CACHE'='col1,col2,?')
```

  Example:


```
ALTER TABLE employee SET TBLPROPERTIES ('COLUMN_META_CACHE'='city')
```

- <a id="ddl-of-carbondata--caching-at-block-or-blocklet-level"></a>

  ##### Caching at Block or Blocklet Level

  This feature allows you to maintain the cache at Block level, resulting in optimized usage of the memory. The memory consumption is high if the Blocklet level caching is maintained as a Block can have multiple Blocklet.

  Following are the valid values for CACHE\_LEVEL:

  *Configuration for caching in driver at Block level (default value).*


```
CACHE_LEVEL= 'BLOCK'
```

  *Configuration for caching in driver at Blocklet level.*


```
CACHE_LEVEL= 'BLOCKLET'
```

  Cache level can be specified either while creating table or after creation of the table.
  During create table operation specify the cache level in table properties.

  Syntax:


```
CREATE TABLE [dbName].tableName (col1 String, col2 String, col3 int,?) STORED AS carbondata TBLPROPERTIES ('CACHE_LEVEL'='Blocklet')
```

  Example:


```
CREATE TABLE employee (name String, city String, id int) STORED AS carbondata TBLPROPERTIES ('CACHE_LEVEL'='Blocklet')
```

  After creation of table or on already created tables use the alter table command to configure the cache level.

  Syntax:


```
ALTER TABLE [dbName].tableName SET TBLPROPERTIES ('CACHE_LEVEL'='Blocklet')
```

  Example:


```
ALTER TABLE employee SET TBLPROPERTIES ('CACHE_LEVEL'='Blocklet')
```

- <a id="ddl-of-carbondata--support-flat-folder-same-as-hive-parquet"></a>

  ##### Support Flat folder same as Hive/Parquet

  This feature allows all carbondata and index files to keep directy under tablepath. Currently all carbondata/carbonindex files written under tablepath/Fact/Part0/Segment\_NUM folder and it is not same as hive/parquet folder structure. This feature makes all files written will be directly under tablepath, it does not maintain any segment folder structure. This is useful for interoperability between the execution engines and plugin with other execution engines like hive or presto becomes easier.

  Following table property enables this feature and default value is false.


```
'flat_folder'='true'
```

  Example:


```
CREATE TABLE employee (name String, city String, id int) STORED AS carbondata TBLPROPERTIES ('flat_folder'='true')
```

- <a id="ddl-of-carbondata--string-longer-than-32000-characters"></a>

  ##### String longer than 32000 characters

  In common scenarios, the length of string is less than 32000,
  so carbondata stores the length of content using Short to reduce memory and space consumption.
  To support string longer than 32000 characters, carbondata introduces a table property called `LONG_STRING_COLUMNS`.
  For these columns, carbondata internally stores the length of content using Integer.

  You can specify the columns as 'long string column' using below tblProperties:


```
// specify col1, col2 as long string columns
TBLPROPERTIES ('LONG_STRING_COLUMNS'='col1,col2')
```

  Besides, you can also use this property through DataFrame by


```
df.format("carbondata")
  .option("tableName", "carbonTable")
  .option("long_string_columns", "col1, col2")
  .save()
```

  If you are using Carbon-SDK, you can specify the datatype of long string column as `varchar`.
  You can refer to SDKwriterTestCase for example.

  **NOTE:** The LONG\_STRING\_COLUMNS can only be string/char/varchar columns and cannot be sort\_columns/complex columns.
- <a id="ddl-of-carbondata--compression-for-table"></a>

  ##### Compression for table

  Data compression is also supported by CarbonData.
  By default, Snappy is used to compress the data. CarbonData also supports ZSTD and GZIP compressors.

  User can specify the compressor in the table property:


```
TBLPROPERTIES('carbon.column.compressor'='GZIP')
```

  or


```
TBLPROPERTIES('carbon.column.compressor'='zstd')
```

  If the compressor is configured, all the data loading and compaction will use that compressor.
  If the compressor is not configured, the data loading and compaction will use the compressor from current system property.
  In this scenario, the compressor for each load may differ if the system property is changed each time. This is helpful if you want to change the compressor for a table.
  The corresponding system property is configured in carbon.properties file as below:


```
carbon.column.compressor=snappy
```

  or


```
carbon.column.compressor=zstd
```

- <a id="ddl-of-carbondata--bad-records-path"></a>

  ##### Bad Records Path

  This property is used to specify the location where bad records would be written.
  As the table path remains the same after rename therefore the user can use this property to
  specify bad records path for the table at the time of creation, so that the same path can
  be later viewed in table description for reference.


```
TBLPROPERTIES('BAD_RECORD_PATH'='/opt/badrecords')
```

- <a id="ddl-of-carbondata--load-minimum-data-size"></a>

  ##### Load minimum data size

  This property indicates the minimum input data size per node for data loading.
  By default it is not enabled. Setting a non-zero integer value will enable this feature.
  This property is useful if you have a large cluster and only want a small portion of the nodes to process data loading.
  For example, if you have a cluster with 10 nodes and the input data is about 1GB. Without this property, each node will process about 100MB input data and result in at least 10 data files. With this property configured with 512, only 2 nodes will be chosen to process the input data, each with about 512MB input and result in about 2 or 4 files based on the compress ratio.
  Moreover, this property can also be specified in the load option.
  Notice that once you enable this feature, for load balance, carbondata will ignore the data locality while assigning input data to nodes, this will cause more network traffic.


```
TBLPROPERTIES('LOAD_MIN_SIZE_INMB'='256')
```

- <a id="ddl-of-carbondata--range-column"></a>

  ##### Range Column

  This property is used to specify a column to partition the input data by range.
  Only one column can be configured. During data loading, you can use "global\_sort\_partitions" or "scale\_factor" to avoid generating small files.
  This feature doesn't support binary data type.


```
TBLPROPERTIES('RANGE_COLUMN'='col1')
```

- <a id="ddl-of-carbondata--index-cache-expiration-time-in-seconds"></a>

  ##### Index Cache Expiration Time In Seconds

  Carbon maintains index cache in driver side and the cache will be expired after seconds indicated by this table property.


```
TBLPROPERTIES('index_cache_expiration_seconds'='1')
```

  After creation of table or on already created tables use the alter table command to configure the cache expiration time.

  Syntax:


```
 ALTER TABLE [dbName].tableName SET TBLPROPERTIES ('index_cache_expiration_seconds'='3')
```

<a id="ddl-of-carbondata--create-table-as-select"></a>

## CREATE TABLE AS SELECT

This function allows user to create a Carbon table from any of the Parquet/Hive/Carbon table. This is beneficial when the user wants to create Carbon table from any other Parquet/Hive table and use the Carbon query engine to query and achieve better query results for cases where Carbon is faster than other file formats. Also this feature can be used for backing up the data.

```
CREATE TABLE [IF NOT EXISTS] [db_name.]table_name 
STORED AS carbondata 
[TBLPROPERTIES (key1=val1, key2=val2, ...)] 
AS select_statement;
```

<a id="ddl-of-carbondata--examples"></a>

### Examples

```
carbon.sql(
           s"""
              | CREATE TABLE source_table(
              |   id INT,
              |   name STRING,
              |   city STRING,
              |   age INT)
              | STORED AS parquet
           """.stripMargin)
              
carbon.sql("INSERT INTO source_table SELECT 1,'bob','shenzhen',27")

carbon.sql("INSERT INTO source_table SELECT 2,'david','shenzhen',31")

carbon.sql(
           s"""
              | CREATE TABLE target_table
              | STORED AS carbondata
              | AS SELECT city, avg(age) 
              |    FROM source_table 
              |    GROUP BY city
           """.stripMargin)
            
carbon.sql("SELECT * FROM target_table").show

// results:
//    +--------+--------+
//    |    city|avg(age)|
//    +--------+--------+
//    |shenzhen|    29.0|
//    +--------+--------+
```

<a id="ddl-of-carbondata--create-external-table"></a>

## CREATE EXTERNAL TABLE

This function allows user to create external table by specifying location.

```
CREATE EXTERNAL TABLE [IF NOT EXISTS] [db_name.]table_name 
STORED AS carbondata LOCATION '$FilesPath'
```

<a id="ddl-of-carbondata--create-external-table-on-managed-table-data-location."></a>

### Create external table on managed table data location.

Managed table data location provided will have both FACT and Metadata folder.
This data can be generated by creating a normal carbon table and use this path as $FilesPath in the above syntax.

**Example:**

```
sql("CREATE TABLE origin(key INT, value STRING) STORED AS carbondata")
sql("INSERT INTO origin select 100,'spark'")
sql("INSERT INTO origin select 200,'hive'")
// creates a table in $storeLocation/origin

sql(
    s"""
       | CREATE EXTERNAL TABLE source
       | STORED AS carbondata
       | LOCATION '$storeLocation/origin'
    """.stripMargin)
sql("SELECT count(*) from source").show()
```

<a id="ddl-of-carbondata--create-external-table-on-non-transactional-table-data-location."></a>

### Create external table on Non-Transactional table data location.

Non-Transactional table data location will have only carbondata and carbonindex files, there will not be a metadata folder (table status and schema).
Our SDK module currently supports writing data in this format.

**Example:**

```
sql(
    s"""
       | CREATE EXTERNAL TABLE sdkOutputTable STORED AS carbondata LOCATION
       |'$writerPath'
    """.stripMargin)
```

Here writer path will have carbondata and index files.
This can be SDK output or C++ SDK output. Refer [SDK Guide](#sdk-guide) and [C++ SDK Guide](#csdk-guide).

**Note:**

1. Dropping of the external table will not delete the files present in the location.
2. When external table is created on non-transactional table data,
   external table will be registered with the schema of carbondata files.
   If multiple files have the same column with different datatypes then exception will be thrown.

<a id="ddl-of-carbondata--create-database"></a>

## CREATE DATABASE

This function creates a new database. By default the database is created in Carbon store location, but you can also specify custom location.

```
CREATE DATABASE [IF NOT EXISTS] database_name [LOCATION path];
```

<a id="ddl-of-carbondata--example"></a>

### Example

```
CREATE DATABASE carbon LOCATION "hdfs://name_cluster/dir1/carbonstore";
```

<a id="ddl-of-carbondata--table-management"></a>

## TABLE MANAGEMENT

<a id="ddl-of-carbondata--show-table"></a>

### SHOW TABLE

This command can be used to list all the tables in current database or all the tables of a specific database.

```
SHOW TABLES [IN db_Name]
```

Example:

```
SHOW TABLES
OR
SHOW TABLES IN defaultdb
```

<a id="ddl-of-carbondata--alter-table"></a>

### ALTER TABLE

The following section introduce the commands to modify the physical or logical state of the existing table(s).

- <a id="ddl-of-carbondata--rename-table"></a>

  #### RENAME TABLE

  This command is used to rename the existing table.


```
ALTER TABLE [db_name.]table_name RENAME TO new_table_name
```

  Examples:


```
ALTER TABLE carbon RENAME TO carbonTable
OR
ALTER TABLE test_db.carbon RENAME TO test_db.carbonTable
```

- <a id="ddl-of-carbondata--add-columns"></a>

  #### ADD COLUMNS

  This command is used to add a new column to the existing table.


```
ALTER TABLE [db_name.]table_name ADD COLUMNS (col_name data_type,...)
TBLPROPERTIES('DEFAULT.VALUE.COLUMN_NAME'='default_value')
```

  Examples:


```
ALTER TABLE carbon ADD COLUMNS (a1 INT, b1 STRING)
```


```
ALTER TABLE carbon ADD COLUMNS (a1 INT, b1 STRING) TBLPROPERTIES('DEFAULT.VALUE.a1'='10')
```

  **NOTE:** Add Complex datatype columns is not supported.

Users can specify which columns to include and exclude for local dictionary generation after adding new columns. These will be appended with the already existing local dictionary include and exclude columns of main table respectively.

````
 ```
 ALTER TABLE carbon ADD COLUMNS (a1 STRING, b1 STRING) TBLPROPERTIES('LOCAL_DICTIONARY_INCLUDE'='a1','LOCAL_DICTIONARY_EXCLUDE'='b1')
 ```
````

- <a id="ddl-of-carbondata--drop-columns"></a>

  #### DROP COLUMNS

  This command is used to delete the existing column(s) in a table.


```
ALTER TABLE [db_name.]table_name DROP COLUMNS (col_name, ...)
```

  Examples:


```
ALTER TABLE carbon DROP COLUMNS (b1)
OR
ALTER TABLE test_db.carbon DROP COLUMNS (b1)

ALTER TABLE carbon DROP COLUMNS (c1,d1)
```

  **NOTE:** Drop Complex child column is not supported.
- <a id="ddl-of-carbondata--change-column-name-type"></a>

  #### CHANGE COLUMN NAME/TYPE

  This command is used to change column name and the data type from INT to BIGINT or decimal precision from lower to higher.
  Change of decimal data type from lower precision to higher precision will only be supported for cases where there is no data loss.


```
ALTER TABLE [db_name.]table_name CHANGE col_old_name col_new_name column_type
```

  Valid Scenarios

  - Invalid scenario - Change of decimal precision from (10,2) to (10,5) is invalid as in this case only scale is increased but total number of digits remains the same.
  - Valid scenario - Change of decimal precision from (10,2) to (12,3) is valid as the total number of digits are increased by 2 but scale is increased only by 1 which will not lead to any data loss.
  - **NOTE:** The allowed range is 38,38 (precision, scale) and is a valid upper case scenario which is not resulting in data loss.

  Example1:Change column a1's name to a2 and its data type from INT to BIGINT.


```
ALTER TABLE test_db.carbon CHANGE a1 a2 BIGINT
```

  Example2:Changing decimal precision of column a1 from 10 to 18.


```
ALTER TABLE test_db.carbon CHANGE a1 a1 DECIMAL(18,2)
```

  Example3:Change column a3's name to a4.


```
ALTER TABLE test_db.carbon CHANGE a3 a4 STRING
```

  **NOTE:** Once the column is renamed, user has to take care about replacing the fileheader with the new name or changing the column header in csv file.
- <a id="ddl-of-carbondata--merge-index"></a>

  #### MERGE INDEX

  This command is used to merge all the CarbonData index files (.carbonindex) inside a segment to a single CarbonData index merge file (.carbonindexmerge). This enhances the first query performance.


```
ALTER TABLE [db_name.]table_name COMPACT 'SEGMENT_INDEX'
```

  Examples:


```
ALTER TABLE test_db.carbon COMPACT 'SEGMENT_INDEX'
```

  **NOTE:**

  - Merge index is not supported on streaming table.
- <a id="ddl-of-carbondata--set-and-unset"></a>

  #### SET and UNSET

  When set command is used, all the newly set properties will override the corresponding old properties if exists.

  - <a id="ddl-of-carbondata--local-dictionary-properties"></a>

    ##### Local Dictionary Properties

    Example to SET Local Dictionary Properties:


```
ALTER TABLE tablename SET TBLPROPERTIES('LOCAL_DICTIONARY_ENABLE'='false','LOCAL_DICTIONARY_THRESHOLD'='1000','LOCAL_DICTIONARY_INCLUDE'='column1','LOCAL_DICTIONARY_EXCLUDE'='column2')
```

    When Local Dictionary properties are unset, corresponding default values will be used for these properties.

    Example to UNSET Local Dictionary Properties:


```
ALTER TABLE tablename UNSET TBLPROPERTIES('LOCAL_DICTIONARY_ENABLE','LOCAL_DICTIONARY_THRESHOLD','LOCAL_DICTIONARY_INCLUDE','LOCAL_DICTIONARY_EXCLUDE')
```

    **NOTE:** For old tables, by default, local dictionary is disabled. If user wants local dictionary for these tables, user can enable/disable local dictionary for new data at their discretion.
    This can be achieved by using the alter table set command.
  - <a id="ddl-of-carbondata--sort-scope"></a>

    ##### SORT SCOPE

    Example to SET SORT SCOPE:


```
ALTER TABLE tablename SET TBLPROPERTIES('SORT_SCOPE'='NO_SORT')
```

    When Sort Scope is unset, the default values (NO\_SORT) will be used.

    Example to UNSET SORT SCOPE:


```
ALTER TABLE tablename UNSET TBLPROPERTIES('SORT_SCOPE')
```

  - <a id="ddl-of-carbondata--sort-columns"></a>

    ##### SORT COLUMNS

    Example to SET SORT COLUMNS:


```
ALTER TABLE tablename SET TBLPROPERTIES('SORT_COLUMNS'='column1')
```

    After this operation, the new loading will use the new SORT\_COLUMNS. The user can adjust
    the SORT\_COLUMNS according to the query, but it will not impact the old data directly. So
    it will not impact the query performance of the old data segments which are not sorted by
    new SORT\_COLUMNS.

    UNSET is not supported, but it can set SORT\_COLUMNS to empty string instead of using UNSET.
    NOTE: When SORT\_SCOPE is not NO\_SORT, then setting SORT\_COLUMNS to empty string is not valid.


```
ALTER TABLE tablename SET TBLPROPERTIES('SORT_COLUMNS'='')
```

    **NOTE:**

    - The "custom" compaction support re-sorting the old segment one by one in version 1.6 or later.
    - The streaming table is not supported for SORT\_COLUMNS modification.
    - If the inverted index columns are removed from the new SORT\_COLUMNS, they will not
      create the inverted index. But the old configuration of INVERTED\_INDEX will be kept.

<a id="ddl-of-carbondata--drop-table"></a>

### DROP TABLE

This command is used to delete an existing table.

```
DROP TABLE [IF EXISTS] [db_name.]table_name
```

Example:

```
DROP TABLE IF EXISTS productSchema.productSalesTable
```

<a id="ddl-of-carbondata--refresh-table"></a>

### REFRESH TABLE

This command is used to register Carbon table to HIVE meta store catalogue from existing Carbon table data.

```
REFRESH TABLE $db_NAME.$table_NAME
```

Example:

```
REFRESH TABLE dbcarbon.productSalesTable
```

**NOTE:**

- The new database name and the old database name should be same.
- Before executing this command the old table schema and data should be copied into the new database location.
- If the table is aggregate table, then all the aggregate tables should be copied to the new database location.
- For old store, the time zone of the source and destination cluster should be same.
- If old cluster used HIVE meta store to store schema, refresh will not work as schema file does not exist in file system.

<a id="ddl-of-carbondata--table-and-column-comment"></a>

### Table and Column Comment

You can provide more information on table by using table comment. Similarly you can provide more information about a particular column using column comment.
You can see the column comment of an existing table using describe formatted command.

```
CREATE TABLE [IF NOT EXISTS] [db_name.]table_name[(col_name data_type [COMMENT col_comment], ...)]
  [COMMENT table_comment]
STORED AS carbondata
[TBLPROPERTIES (property_name=property_value, ...)]
```

Example:

```
CREATE TABLE IF NOT EXISTS productSchema.productSalesTable (
                              productNumber Int COMMENT 'unique serial number for product')
COMMENT "This is table comment"
STORED AS carbondata
```

You can also SET and UNSET table comment using ALTER command.

Example to SET table comment:

```
ALTER TABLE carbon SET TBLPROPERTIES ('comment'='this table comment is modified');
```

Example to UNSET table comment:

```
ALTER TABLE carbon UNSET TBLPROPERTIES ('comment');
```

<a id="ddl-of-carbondata--partition"></a>

## PARTITION

<a id="ddl-of-carbondata--standard-partition"></a>

### STANDARD PARTITION

The partition is similar as spark and hive partition, user can use any column to build partition:

<a id="ddl-of-carbondata--create-partition-table"></a>

#### Create Partition Table

This command allows you to create table with partition.

```
CREATE TABLE [IF NOT EXISTS] [db_name.]table_name 
  [(col_name data_type , ...)]
  [COMMENT table_comment]
  [PARTITIONED BY (col_name data_type , ...)]
  [STORED AS file_format]
  [TBLPROPERTIES (property_name=property_value, ...)]
```

Example:

```
CREATE TABLE IF NOT EXISTS productSchema.productSalesTable (
                              productNumber INT,
                              productName STRING,
                              storeCity STRING,
                              storeProvince STRING,
                              saleQuantity INT,
                              revenue INT)
PARTITIONED BY (productCategory STRING, productBatch STRING)
STORED AS carbondata
```

**NOTE:** Hive partition is not supported on complex data type columns.

<a id="ddl-of-carbondata--show-partitions"></a>

#### Show Partitions

This command gets the Hive partition information of the table

```
SHOW PARTITIONS [db_name.]table_name
```

<a id="ddl-of-carbondata--drop-partition"></a>

#### Drop Partition

This command drops the specified Hive partition only.

```
ALTER TABLE table_name DROP [IF EXISTS] PARTITION (part_spec, ...)
```

Example:

```
ALTER TABLE locationTable DROP PARTITION (country = 'US');
```

<a id="ddl-of-carbondata--insert-overwrite"></a>

#### Insert OVERWRITE

This command allows you to insert or load overwrite on a specific partition.

```
INSERT OVERWRITE TABLE table_name
PARTITION (column = 'partition_name')
select_statement
```

Example:

```
INSERT OVERWRITE TABLE partitioned_user
PARTITION (country = 'US')
SELECT * FROM another_user au 
WHERE au.country = 'US';
```

<a id="ddl-of-carbondata--show-partitions-2"></a>

### Show Partitions

The following command is executed to get the partition information of the table

```
SHOW PARTITIONS [db_name.]table_name
```

<a id="ddl-of-carbondata--add-a-new-partition"></a>

### Add a new partition

```
ALTER TABLE [db_name].table_name ADD PARTITION('new_partition')
```

<a id="ddl-of-carbondata--split-a-partition"></a>

### Split a partition

```
ALTER TABLE [db_name].table_name SPLIT PARTITION(partition_id) INTO('new_partition1', 'new_partition2'...)
```

<a id="ddl-of-carbondata--drop-a-partition"></a>

### Drop a partition

Only drop partition definition, but keep data

```
ALTER TABLE [db_name].table_name DROP PARTITION(partition_id)
```

Drop both partition definition and data

```
ALTER TABLE [db_name].table_name DROP PARTITION(partition_id) WITH DATA
```

**NOTE:**

- Hash partition table is not supported for ADD, SPLIT and DROP commands.
- Partition Id: in CarbonData like the hive, folders are not used to divide partitions instead partition id is used to replace the task id. It could make use of the characteristic and meanwhile reduce some metadata.

```
SegmentDir/0_batchno0-0-1502703086921.carbonindex
          ^
SegmentDir/part-0-0_batchno0-0-1502703086921.carbondata
                   ^
```

Here are some useful tips to improve query performance of carbonData partition table:

- The partitioned column can be excluded from SORT\_COLUMNS, this will let other columns to do the efficient sorting.
- When writing SQL on a partition table, try to use filters on the partition column.

<a id="ddl-of-carbondata--bucketing"></a>

## BUCKETING

Bucketing feature can be used to distribute/organize the table/partition data into multiple files such
that similar records are present in the same file. While creating a table, user needs to specify the
columns to be used for bucketing and the number of buckets. For the selection of bucket the Hash value
of columns is used.

```
CREATE TABLE [IF NOT EXISTS] [db_name.]table_name
                  [(col_name data_type, ...)]
STORED AS carbondata
TBLPROPERTIES('BUCKET_NUMBER'='noOfBuckets',
'BUCKET_COLUMNS'='columnname')
```

**NOTE:**

- Bucketing cannot be performed for columns of Complex Data Types.
- Columns in the BUCKETCOLUMN parameter must be dimensions. The BUCKETCOLUMN parameter cannot be a measure or a combination of measures and dimensions.

Example:

```
CREATE TABLE IF NOT EXISTS productSchema.productSalesTable (
  productNumber INT,
  saleQuantity INT,
  productName STRING,
  storeCity STRING,
  storeProvince STRING,
  productCategory STRING,
  productBatch STRING,
  revenue INT)
STORED AS carbondata
TBLPROPERTIES ('BUCKET_NUMBER'='4', 'BUCKET_COLUMNS'='productName')
```

<a id="ddl-of-carbondata--cache"></a>

## CACHE

CarbonData internally uses LRU caching to improve the performance. The user can get information
about current cache used status in memory through the following command:

```
SHOW METACACHE
```

This shows the overall memory consumed in the cache by categories - index files, dictionary and
indexes. This also shows the cache usage by all the tables and children tables in the current
database.

```
 SHOW EXECUTOR METACACHE
```

This shows the overall memory consumed by the cache in each executor of the Index
Server. This command is only allowed when the carbon property `carbon.enable.index.server`
is set to true.

```
SHOW METACACHE ON TABLE tableName
```

This shows detailed information on cache usage by the table `tableName` and its carbonindex files, its dictionary files, its indexes and children tables.

This command is not allowed on child tables.

```
  DROP METACACHE ON TABLE tableName
```

This clears any entry in cache by the table `tableName`, its carbonindex files, its dictionary files, its indexes and children tables.

This command is not allowed on child tables.

<a id="ddl-of-carbondata--important-points"></a>

### Important points

1. Cache information is updated only after the select query is executed.
2. In case of alter table the already loaded cache is invalidated when any subsequent select query
   is fired.
3. Dictionary is loaded in cache only when the dictionary columns are queried upon. If we don't do
   direct query on dictionary column, cache will not be loaded.
   If we do `SELECT * FROM t1`, and even though for this case dictionary is loaded, it is loaded in
   executor and not on driver, and the final result rows are returned back to driver, and thus will
   produce no trace on driver cache if we do `SHOW METACACHE` or `SHOW METACACHE ON TABLE t1`.

[Top](#ddl-of-carbondata--top)

---

<a id="dml-of-carbondata"></a>

<!-- source_url: https://carbondata.apache.org/dml-of-carbondata.html -->

<!-- page_index: 6 -->

<a id="dml-of-carbondata--carbondata-data-manipulation-language"></a>

# CarbonData Data Manipulation Language

CarbonData DML statements are documented here,which includes:

- [LOAD DATA](#dml-of-carbondata--load-data)
- [INSERT DATA](#dml-of-carbondata--insert-data-into-carbondata-table)
- [INSERT DATA STAGE](#dml-of-carbondata--insert-data-into-carbondata-table-from-stage-input-files)
- [Load Data Using Static Partition](#dml-of-carbondata--load-data-using-static-partition)
- [Load Data Using Dynamic Partition](#dml-of-carbondata--load-data-using-dynamic-partition)
- [UPDATE AND DELETE](#dml-of-carbondata--update-and-delete)
- [COMPACTION](#dml-of-carbondata--compaction)
- [SEGMENT MANAGEMENT](https://carbondata.apache.org/segment-management-on-carbondata.html)

<a id="dml-of-carbondata--load-data"></a>

## LOAD DATA

<a id="dml-of-carbondata--load-files-to-carbondata-table"></a>

### LOAD FILES TO CARBONDATA TABLE

This command is used to load csv files to carbondata, OPTIONS are not mandatory for data loading process.

```
LOAD DATA INPATH 'folder_path'
INTO TABLE [db_name.]table_name 
OPTIONS(property_name=property_value, ...)
```

> [!NOTE]
> :
> \* Use 'file://' prefix to indicate local input files path, but it just supports local mode.
> \* If run on cluster mode, please upload all input files to distributed file system, for example 'hdfs://' for hdfs.

**Supported Properties:**

| Property | Description |
| --- | --- |
| [DELIMITER](#dml-of-carbondata--delimiter) | Character used to separate the data in the input csv file |
| [QUOTECHAR](#dml-of-carbondata--quotechar) | Character used to quote the data in the input csv file |
| [LINE\_SEPARATOR](#dml-of-carbondata--line_separator) | Characters used to specify the line separator in the input csv file. If not provided, csv parser will detect it automatically. |
| [COMMENTCHAR](#dml-of-carbondata--commentchar) | Character used to comment the rows in the input csv file. Those rows will be skipped from processing |
| [HEADER](#dml-of-carbondata--header) | Whether the input csv files have header row |
| [FILEHEADER](#dml-of-carbondata--fileheader) | If header is not present in the input csv, what is the column names to be used for data read from input csv |
| [SORT\_SCOPE](#dml-of-carbondata--sort_scope) | Sort Scope to be used for current load. |
| [MULTILINE](#dml-of-carbondata--multiline) | Whether a row data can span across multiple lines. |
| [ESCAPECHAR](#dml-of-carbondata--escapechar) | Escape character used to excape the data in input csv file.For eg.,\ is a standard escape character |
| [SKIP\_EMPTY\_LINE](#dml-of-carbondata--skip_empty_line) | Whether empty lines in input csv file should be skipped or loaded as null row |
| [COMPLEX\_DELIMITER\_LEVEL\_1](#dml-of-carbondata--complex_delimiter_level_1) | Starting delimiter for complex type data in input csv file |
| [COMPLEX\_DELIMITER\_LEVEL\_2](#dml-of-carbondata--complex_delimiter_level_2) | Ending delimiter for complex type data in input csv file |
| [COMPLEX\_DELIMITER\_LEVEL\_3](#dml-of-carbondata--complex_delimiter_level_3) | Ending delimiter for nested complex type data in input csv file of level 3. |
| [DATEFORMAT](#dml-of-carbondata--dateformattimestampformat) | Format of date in the input csv file |
| [TIMESTAMPFORMAT](#dml-of-carbondata--dateformattimestampformat) | Format of timestamp in the input csv file |
| [SORT\_COLUMN\_BOUNDS](#dml-of-carbondata--sort-column-bounds) | How to partition the sort columns to make the evenly distributed |
| [BAD\_RECORDS\_LOGGER\_ENABLE](#dml-of-carbondata--bad-records-handling) | Whether to enable bad records logging |
| [BAD\_RECORD\_PATH](#dml-of-carbondata--bad-records-handling) | Bad records logging path. Useful when bad record logging is enabled |
| [BAD\_RECORDS\_ACTION](#dml-of-carbondata--bad-records-handling) | Behavior of data loading when bad record is found |
| [IS\_EMPTY\_DATA\_BAD\_RECORD](#dml-of-carbondata--bad-records-handling) | Whether empty data of a column to be considered as bad record or not |
| [GLOBAL\_SORT\_PARTITIONS](#dml-of-carbondata--global_sort_partitions) | Number of partition to use for shuffling of data during sorting |
| [SCALE\_FACTOR](#dml-of-carbondata--scale_factor) | Control the partition size for RANGE\_COLUMN feature |

- You can use the following options to load data:

  - <a id="dml-of-carbondata--delimiter:"></a>

    ##### DELIMITER:

    Delimiters can be provided in the load command.


```
OPTIONS('DELIMITER'=',')
```

  - <a id="dml-of-carbondata--quotechar:"></a>

    ##### QUOTECHAR:

    Quote Characters can be provided in the load command.


```
OPTIONS('QUOTECHAR'='"')
```

  - <a id="dml-of-carbondata--line_separator:"></a>

    ##### LINE\_SEPARATOR:

    Line separator Characters can be provided in the load command.


```
OPTIONS('LINE_SEPARATOR'='\n')
```

  - <a id="dml-of-carbondata--commentchar:"></a>

    ##### COMMENTCHAR:

    Comment Characters can be provided in the load command if user wants to comment lines.


```
OPTIONS('COMMENTCHAR'='#')
```

  - <a id="dml-of-carbondata--header:"></a>

    ##### HEADER:

    When you load the CSV file without the file header and the file header is the same with the table schema, then add 'HEADER'='false' to load data SQL as user need not provide the file header. By default the value is 'true'.
    false: CSV file is without file header.
    true: CSV file is with file header.


```
OPTIONS('HEADER'='false') 
```

    **NOTE:** If the HEADER option exist and is set to 'true', then the FILEHEADER option is not required.
  - <a id="dml-of-carbondata--fileheader:"></a>

    ##### FILEHEADER:

    Headers can be provided in the LOAD DATA command if headers are missing in the source files.


```
OPTIONS('FILEHEADER'='column1,column2') 
```

  - <a id="dml-of-carbondata--sort_scope:"></a>

    ##### SORT\_SCOPE:

    Sort Scope to be used for the current load. This overrides the Sort Scope of Table.
    Requirement: Sort Columns must be set while creating table. If Sort Columns is null, Sort Scope is always NO\_SORT.


```
OPTIONS('SORT_SCOPE'='GLOBAL_SORT')
```

    Priority order for choosing Sort Scope is:

    - Load Data Command
    - `CARBON.TABLE.LOAD.SORT.SCOPE.<db>.<table>` session property.
    - Table level Sort Scope
    - `CARBON.OPTIONS.SORT.SCOPE` session property
    - Default Value: NO\_SORT
  - <a id="dml-of-carbondata--multiline:"></a>

    ##### MULTILINE:

    CSV with new line character in quotes.


```
OPTIONS('MULTILINE'='true') 
```

  - <a id="dml-of-carbondata--escapechar:"></a>

    ##### ESCAPECHAR:

    Escape char can be provided if user want strict validation of escape character in CSV files.


```
OPTIONS('ESCAPECHAR'='\') 
```

  - <a id="dml-of-carbondata--skip_empty_line:"></a>

    ##### SKIP\_EMPTY\_LINE:

    This option will ignore the empty line in the CSV file during the data load.


```
OPTIONS('SKIP_EMPTY_LINE'='TRUE/FALSE') 
```

  - <a id="dml-of-carbondata--complex_delimiter_level_1:"></a>

    ##### COMPLEX\_DELIMITER\_LEVEL\_1:

    Split the complex type data column in a row (eg., a\001b\001c --> Array = {a,b,c}).


```
OPTIONS('COMPLEX_DELIMITER_LEVEL_1'='\001')
```

  - <a id="dml-of-carbondata--complex_delimiter_level_2:"></a>

    ##### COMPLEX\_DELIMITER\_LEVEL\_2:

    Split the complex type nested data column in a row. Applies level\_1 delimiter & applies level\_2 based on complex data type (eg., a\002b\001c\002d --> Array> = {{a,b},{c,d}}).


```
OPTIONS('COMPLEX_DELIMITER_LEVEL_2'='\002')
```

  - <a id="dml-of-carbondata--complex_delimiter_level_3:"></a>

    ##### COMPLEX\_DELIMITER\_LEVEL\_3:

    Split the complex type nested data column in a row. Applies level\_1 delimiter, applies level\_2 and then level\_3 delimiter based on complex data type.
    Used in case of nested Complex Map type. (eg., 'a\003b\002b\003c\001aa\003bb\002cc\003dd' --> Array Of Map> = {{a -> b, b -> c},{aa -> bb, cc -> dd}}).


```
OPTIONS('COMPLEX_DELIMITER_LEVEL_3'='\003')
```

  - <a id="dml-of-carbondata--dateformat-timestampformat:"></a>

    ##### DATEFORMAT/TIMESTAMPFORMAT:

    Date and Timestamp format for specified column.


```
OPTIONS('DATEFORMAT' = 'yyyy-MM-dd','TIMESTAMPFORMAT'='yyyy-MM-dd HH:mm:ss')
```

    **NOTE:** Date formats are specified by date pattern strings. The date pattern in CarbonData is the same as in JAVA. Refer to [SimpleDateFormat](http://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html).
  - <a id="dml-of-carbondata--sort-column-bounds:"></a>

    ##### SORT COLUMN BOUNDS:

    Range bounds for sort columns.

    Suppose the table is created with 'SORT\_COLUMNS'='name,id' and the range for name is aaa to zzz, the value range for id is 0 to 1000. Then during data loading, we can specify the following option to enhance data loading performance.


```
OPTIONS('SORT_COLUMN_BOUNDS'='f,250;l,500;r,750')
```

    Each bound is separated by ';' and each field value in bound is separated by ','. In the example above, we provide 3 bounds to distribute records to 4 partitions. The values 'f','l','r' can evenly distribute the records. Inside carbondata, for a record we compare the value of sort columns with that of the bounds and decide which partition the record will be forwarded to.

    **NOTE:**

    - SORT\_COLUMN\_BOUNDS will be used only when the SORT\_SCOPE is 'local\_sort'.
    - Carbondata will use these bounds as ranges to process data concurrently during the final sort procedure. The records will be sorted and written out inside each partition. Since the partition is sorted, all records will be sorted.
    - The option works better if your CPU usage during loading is low. If your current system CPU usage is high, better not to use this option. Besides, it depends on the user to specify the bounds. If user does not know the exactly bounds to make the data distributed evenly among the bounds, loading performance will still be better than before or at least the same as before.
    - Users can find more information about this option in the description of [PR1953](https://github.com/apache/carbondata/pull/1953).
  - <a id="dml-of-carbondata--bad-records-handling:"></a>

    ##### BAD RECORDS HANDLING:

    Methods of handling bad records are as follows:

    - Load all of the data before dealing with the errors.
    - Clean or delete bad records before loading data or stop the loading when bad records are found.
```
OPTIONS('BAD_RECORDS_LOGGER_ENABLE'='true', 'BAD_RECORD_PATH'='hdfs://hacluster/tmp/carbon', 'BAD_RECORDS_ACTION'='REDIRECT', 'IS_EMPTY_DATA_BAD_RECORD'='false')
```

    **NOTE:**

    - BAD\_RECORDS\_ACTION property can have four types of actions for bad records FORCE, REDIRECT, IGNORE, and FAIL.
    - FAIL option is its Default value. If the FAIL option is used, then data loading fails if any bad records are found.
    - If the REDIRECT option is used, CarbonData will add all bad records into a separate CSV file. However, this file must not be used for subsequent data loading because the content may not exactly match the source record. You are advised to cleanse the source record for further data ingestion. This option is used to remind you which records are bad.
    - If the FORCE option is used, then it auto-converts the data by storing the bad records as NULL before Loading data.
    - If the IGNORE option is used, then bad records are neither loaded nor written to the separate CSV file.
    - In loaded data, if all records are bad records, the BAD\_RECORDS\_ACTION is invalid and the load operation fails.
    - The default maximum number of characters per column is 32000. If there are more than 32000 characters in a column, please refer to [String longer than 32000 characters](https://github.com/apache/carbondata/blob/master/docs/ddl-of-carbondata.html#string-longer-than-32000-characters) section.
    - Since Bad Records Path can be specified in create, load and carbon properties.
      Therefore, the value specified in load will have the highest priority, and value specified in carbon properties will have the least priority.

    Example:


```
LOAD DATA INPATH 'filepath.csv' INTO TABLE tablename
OPTIONS('BAD_RECORDS_LOGGER_ENABLE'='true','BAD_RECORD_PATH'='hdfs://hacluster/tmp/carbon',
'BAD_RECORDS_ACTION'='REDIRECT','IS_EMPTY_DATA_BAD_RECORD'='false')
```

  - <a id="dml-of-carbondata--global_sort_partitions:"></a>

    ##### GLOBAL\_SORT\_PARTITIONS:

    If the SORT\_SCOPE is defined as GLOBAL\_SORT, then the user can specify the number of partitions to use while shuffling data for sort using GLOBAL\_SORT\_PARTITIONS. If it is not configured, or configured less than 1, then it uses the number of map tasks as reduce tasks. It is recommended that each reduce task deals with 512MB-1GB data.
    For RANGE\_COLUMN, GLOBAL\_SORT\_PARTITIONS is used to specify the number of range partitions also.
    GLOBAL\_SORT\_PARTITIONS should be specified optimally during RANGE\_COLUMN LOAD because if a higher number is configured then the load time may be less but it will result in the creation of more files which would degrade the query and compaction performance.
    Conversely, if fewer partitions are configured then the load performance may degrade due to less use of parallelism but the query and compaction will become faster. Hence the user may choose an optimal number depending on the use case.


```
OPTIONS('GLOBAL_SORT_PARTITIONS'='2')
```

    **NOTE:**

    - GLOBAL\_SORT\_PARTITIONS should be Integer type, the range is [1,Integer.MaxValue].
    - It is only used when the SORT\_SCOPE is GLOBAL\_SORT.
  - <a id="dml-of-carbondata--scale_factor"></a>

    ##### SCALE\_FACTOR

    For RANGE\_COLUMN, SCALE\_FACTOR is used to control the number of range partitions as following.


```
  splitSize = max(blocklet_size, (block_size - blocklet_size)) * scale_factor
  numPartitions = total size of input data / splitSize
```

    The default value is 3, and the range is [1, 300].


```
  OPTIONS('SCALE_FACTOR'='10')
```

    **NOTE:**

    - If both GLOBAL\_SORT\_PARTITIONS and SCALE\_FACTOR are used at the same time, only GLOBAL\_SORT\_PARTITIONS is valid.
    - The compaction on RANGE\_COLUMN will use LOCAL\_SORT by default.

<a id="dml-of-carbondata--insert-data-into-carbondata-table"></a>

## INSERT DATA INTO CARBONDATA TABLE

This command inserts data into a CarbonData table, it is defined as a combination of two queries Insert and Select query respectively.
It inserts records from a source table into a target CarbonData table, the source table can be a Hive table, Parquet table or a CarbonData table itself.
It comes with the functionality to aggregate the records of a table by performing Select query on source table and load its corresponding resultant records into a CarbonData table.

```
INSERT INTO TABLE <CARBONDATA TABLE> SELECT * FROM sourceTableName 
[ WHERE { <filter_condition> } ]
```

User can also omit the `table` keyword and write the query as:

```
INSERT INTO <CARBONDATA TABLE> SELECT * FROM sourceTableName 
[ WHERE { <filter_condition> } ]
```

Overwrite insert data:

```
INSERT OVERWRITE TABLE <CARBONDATA TABLE> SELECT * FROM sourceTableName 
[ WHERE { <filter_condition> } ]
```

**NOTE:**

- The source table and the CarbonData table must have the same table schema.
- The data type of source and destination table columns should be same
- INSERT INTO command does not support partial success if bad records are found, it will fail.
- Data cannot be loaded or updated in source table while insert from source table to target table is in progress.

Examples

```
INSERT INTO table1 SELECT item1, sum(item2 + 1000) as result FROM table2 group by item1
```

```
INSERT INTO table1 SELECT item1, item2, item3 FROM table2 where item2='xyz'
```

```
INSERT OVERWRITE TABLE table1 SELECT * FROM TABLE2
```

<a id="dml-of-carbondata--insert-data-into-carbondata-table-from-stage-input-files"></a>

## INSERT DATA INTO CARBONDATA TABLE From Stage Input Files

Stage input files are data files written by external application (such as Flink). These files
are committed but not loaded into the table.

User can use this command to insert them into the table, thus making them visible for a query.

```
INSERT INTO <CARBONDATA TABLE> STAGE OPTIONS(property_name=property_value, ...)
```

**Supported Properties:**

| Property | Description |
| --- | --- |
| [BATCH\_FILE\_COUNT](#dml-of-carbondata--batch_file_count) | The number of stage files per processing |
| [BATCH\_FILE\_ORDER](#dml-of-carbondata--batch_file_order) | The order type of stage files in per processing |

- User can use the following options to load data:

  - <a id="dml-of-carbondata--batch_file_count:"></a>

    ##### BATCH\_FILE\_COUNT:

    The number of stage files per processing.


```
OPTIONS('batch_file_count'='5')
```

  - <a id="dml-of-carbondata--batch_file_order:"></a>

    ##### BATCH\_FILE\_ORDER:

    The order type of stage files in per processing, choices: ASC, DESC.
    The default is ASC.
    Stage files will order by the last modified time with the specified order type.


```
OPTIONS('batch_file_order'='DESC')
```

    Examples:


```
INSERT INTO table1 STAGE

INSERT INTO table1 STAGE OPTIONS('batch_file_count' = '5')
Note: This command uses the default file order, will insert the earliest stage files into the table.

INSERT INTO table1 STAGE OPTIONS('batch_file_count' = '5', 'batch_file_order'='DESC')
Note: This command will insert the latest stage files into the table.
```

<a id="dml-of-carbondata--load-data-using-static-partition"></a>

## Load Data Using Static Partition

This command allows you to load data using static partition.

```
LOAD DATA INPATH 'folder_path'
INTO TABLE [db_name.]table_name PARTITION (partition_spec) 
OPTIONS(property_name=property_value, ...)

INSERT INTO TABLE [db_name.]table_name PARTITION (partition_spec) <SELECT STATEMENT>
```

Example:

```
LOAD DATA INPATH '${env:HOME}/staticinput.csv'
INTO TABLE locationTable
PARTITION (country = 'US', state = 'CA')

INSERT INTO TABLE locationTable
PARTITION (country = 'US', state = 'AL')
SELECT <columns list excluding partition columns> FROM another_user
```

<a id="dml-of-carbondata--load-data-using-dynamic-partition"></a>

## Load Data Using Dynamic Partition

This command allows you to load data using dynamic partition. If partition spec is not specified, then the partition is considered as dynamic.

Example:

```
LOAD DATA INPATH '${env:HOME}/staticinput.csv'
INTO TABLE locationTable

INSERT INTO TABLE locationTable
SELECT <columns list excluding partition columns> FROM another_user
```

<a id="dml-of-carbondata--update-and-delete"></a>

## UPDATE AND DELETE

<a id="dml-of-carbondata--update"></a>

### UPDATE

This command will allow to update the CarbonData table based on the column expression and optional filter conditions.

```
UPDATE <table_name> 
SET (column_name1, column_name2, ... column_name n) = (column1_expression , column2_expression, ... column n_expression )
[ WHERE { <filter_condition> } ]
```

alternatively the following command can also be used for updating the CarbonData Table :

```
UPDATE <table_name>
SET (column_name1, column_name2) =(select sourceColumn1, sourceColumn2 from sourceTable [ WHERE { <filter_condition> } ] )
[ WHERE { <filter_condition> } ]
```

**NOTE:** The update command fails if multiple input rows in source table are matched with single row in destination table.

Examples:

```
UPDATE t3 SET (t3_salary) = (t3_salary + 9) WHERE t3_name = 'aaa1'
```

```
UPDATE t3 SET (t3_date, t3_country) = ('2017-11-18', 'india') WHERE t3_salary < 15003
```

```
UPDATE t3 SET (t3_country, t3_name) = (SELECT t5_country, t5_name FROM t5 WHERE t5_id = 5) WHERE t3_id < 5
```

```
UPDATE t3 SET (t3_date, t3_serialname, t3_salary) = (SELECT '2099-09-09', t5_serialname, '9999' FROM t5 WHERE t5_id = 5) WHERE t3_id < 5
```

```
UPDATE t3 SET (t3_country, t3_salary) = (SELECT t5_country, t5_salary FROM t5 FULL JOIN t3 u WHERE u.t3_id = t5_id and t5_id=6) WHERE t3_id >6
```

NOTE: Update Complex datatype columns is not supported.

<a id="dml-of-carbondata--delete"></a>

### DELETE

This command allows us to delete records from CarbonData table.

```
DELETE FROM table_name [WHERE expression]
```

Examples:

```
DELETE FROM carbontable WHERE column1  = 'china'
```

```
DELETE FROM carbontable WHERE column1 IN ('china', 'USA')
```

```
DELETE FROM carbontable WHERE column1 IN (SELECT column11 FROM sourceTable2)
```

```
DELETE FROM carbontable WHERE column1 IN (SELECT column11 FROM sourceTable2 WHERE column1 = 'USA')
```

<a id="dml-of-carbondata--delete-stage"></a>

### DELETE STAGE

This command allows us to delete the data files (stage data) which is already loaded into the table.

```
DELETE FROM TABLE [db_name.]table_name STAGE OPTIONS(property_name=property_value, ...)
```

**Supported Properties:**

| Property | Description |
| --- | --- |
| [retain\_hour](#dml-of-carbondata--retain_hour) | Data file retain time in hours |

- You can use the following options to delete data:

  - <a id="dml-of-carbondata--retain_hour:"></a>

    ##### retain\_hour:

    Data file retain time in second, the command just delete overdue files only.


```
OPTIONS('retain_hour'='1')
```

  Examples:


```
DELETE FROM TABLE carbontable STAGE
```


```
DELETE FROM TABLE carbontable STAGE OPTIONS ('retain_hour'='1')
```

<a id="dml-of-carbondata--compaction"></a>

## COMPACTION

Compaction improves the query performance significantly.

There are several types of compaction.

```
ALTER TABLE [db_name.]table_name COMPACT 'MINOR/MAJOR/CUSTOM'
```

- **Minor Compaction**

In Minor compaction, the user can specify the number of loads to be merged.
Minor compaction triggers for every data load if the parameter carbon.enable.auto.load.merge is set to true.
If any segments are available to be merged, then compaction will run parallel with data load, there are 2 levels in minor compaction:

- Level 1: Merging of the segments which are not yet compacted.
- Level 2: Merging of the compacted segments again to form a larger segment.

```
ALTER TABLE table_name COMPACT 'MINOR'
```

- **Major Compaction**

In Major compaction, multiple segments can be merged into one large segment.
User will specify the compaction size until which segments can be merged, Major compaction is usually done during the off-peak time.
Configure the property carbon.major.compaction.size with appropriate value in MB.

This command merges the specified number of segments into one segment:

```
ALTER TABLE table_name COMPACT 'MAJOR'
```

- **Custom Compaction**

In Custom compaction, user can directly specify segment ids to be merged into one large segment.
All specified segment ids should exist and be valid, otherwise compaction will fail.
Custom compaction is usually done during the off-peak time.

```
ALTER TABLE table_name COMPACT 'CUSTOM' WHERE SEGMENT.ID IN (2,3,4)
```

- **CLEAN SEGMENTS AFTER Compaction**

Clean the segments which are compacted:

```
CLEAN FILES FOR TABLE carbon_table
```

[Top](#dml-of-carbondata--top)

---

<a id="streaming-guide"></a>

<!-- source_url: https://carbondata.apache.org/streaming-guide.html -->

<!-- page_index: 7 -->

<a id="streaming-guide--carbondata-streaming-ingestion"></a>

# CarbonData Streaming Ingestion

- [Streaming Table Management](#streaming-guide--quick-example)
  - [Create table with streaming property](#streaming-guide--create-table-with-streaming-property)
  - [Alter streaming property](#streaming-guide--alter-streaming-property)
  - [Acquire streaming lock](#streaming-guide--acquire-streaming-lock)
  - [Create streaming segment](#streaming-guide--create-streaming-segment)
  - [Change Stream segment status](#streaming-guide--change-segment-status)
  - [Handoff "streaming finish" segment to columnar segment](#streaming-guide--handoff-streaming-finish-segment-to-columnar-segment)
  - [Auto handoff streaming segment](#streaming-guide--auto-handoff-streaming-segment)
  - [Stream data parser](#streaming-guide--stream-data-parser)
  - [Close streaming table](#streaming-guide--close-streaming-table)
  - [Constraints](#streaming-guide--constraint)
- [StreamSQL](#streaming-guide--streamsql)
  - [Defining Streaming Table](#streaming-guide--streaming-table)
  - [Streaming Job Management](#streaming-guide--streaming-job-management)
    - [CREATE STREAM](#streaming-guide--create-stream)
    - [DROP STREAM](#streaming-guide--drop-stream)
    - [SHOW STREAMS](#streaming-guide--show-streams)
    - [CLOSE STREAM](#streaming-guide--close-stream)

<a id="streaming-guide--quick-example"></a>

## Quick example

Download and unzip spark-2.4.5-bin-hadoop2.7.tgz, and export $SPARK\_HOME

Package carbon jar, and copy assembly/target/scala-2.11/carbondata\_2.11-2.0.0-SNAPSHOT-shade-hadoop2.7.2.jar to $SPARK\_HOME/jars

```
mvn clean package -DskipTests -Pspark-2.4
```

Start a socket data server in a terminal

```
nc -lk 9099
```

type some CSV rows as following

```
1,col1
2,col2
3,col3
4,col4
5,col5
```

Start spark-shell in new terminal, type :paste, then copy and run the following code.

```
 import java.io.File
 import org.apache.spark.sql.{CarbonEnv, SparkSession}
 import org.apache.spark.sql.CarbonSession._
 import org.apache.spark.sql.streaming.{ProcessingTime, StreamingQuery}
 import org.apache.carbondata.core.util.path.CarbonTablePath
 import org.apache.carbondata.streaming.parser.CarbonStreamParser

 val warehouse = new File("./warehouse").getCanonicalPath
 val metastore = new File("./metastore").getCanonicalPath

 val spark = SparkSession
   .builder()
   .master("local")
   .appName("StreamExample")
   .config("spark.sql.warehouse.dir", warehouse)
   .getOrCreateCarbonSession(warehouse, metastore)

 spark.sparkContext.setLogLevel("ERROR")

 // drop table if exists previously
 spark.sql(s"DROP TABLE IF EXISTS carbon_table")
 // Create target carbon table and populate with initial data
 spark.sql(
   s"""
      | CREATE TABLE carbon_table (
      | col1 INT,
      | col2 STRING
      | )
      | STORED AS carbondata
      | TBLPROPERTIES('streaming'='true')""".stripMargin)

 val carbonTable = CarbonEnv.getCarbonTable(Some("default"), "carbon_table")(spark)
 val tablePath = carbonTable.getTablePath

 // batch load
 var qry: StreamingQuery = null
 val readSocketDF = spark.readStream
   .format("socket")
   .option("host", "localhost")
   .option("port", 9099)
   .load()

 // Write data from socket stream to carbondata file
 qry = readSocketDF.writeStream
   .format("carbondata")
   .trigger(ProcessingTime("5 seconds"))
   .option("checkpointLocation", CarbonTablePath.getStreamingCheckpointDir(tablePath))
   .option("dbName", "default")
   .option("tableName", "carbon_table")
   .option(CarbonStreamParser.CARBON_STREAM_PARSER,
     CarbonStreamParser.CARBON_STREAM_PARSER_CSV)
   .start()

 // start new thread to show data
 new Thread() {
   override def run(): Unit = {
     do {
       spark.sql("select * from carbon_table").show(false)
       Thread.sleep(10000)
     } while (true)
   }
 }.start()

 qry.awaitTermination()
```

Continue to type some rows into data server, and spark-shell will show the new data of the table.

<a id="streaming-guide--create-table-with-streaming-property"></a>

## Create table with streaming property

Streaming table is just a normal carbon table with "streaming" table property, user can create
streaming table using following DDL.

```
CREATE TABLE streaming_table (
 col1 INT,
 col2 STRING
)
STORED AS carbondata
TBLPROPERTIES('streaming'='true')
```

| property name | default | description |
| --- | --- | --- |
| streaming | false | Whether to enable streaming ingest feature for this table Value range: true, false |

"DESC FORMATTED" command will show streaming property.

```
DESC FORMATTED streaming_table
```

<a id="streaming-guide--alter-streaming-property"></a>

## Alter streaming property

For an old table, use ALTER TABLE command to set the streaming property.

```
ALTER TABLE streaming_table SET TBLPROPERTIES('streaming'='true')
```

<a id="streaming-guide--acquire-streaming-lock"></a>

## Acquire streaming lock

At the begin of streaming ingestion, the system will try to acquire the table level lock of streaming.lock file. If the system isn't able to acquire the lock of this table, it will throw an InterruptedException.

<a id="streaming-guide--create-streaming-segment"></a>

## Create streaming segment

The streaming data will be ingested into a separate segment of carbondata table, this segment is termed as streaming segment. The status of this segment will be recorded as "streaming" in "tablestatus" file along with its data size. You can use "SHOW SEGMENTS FOR TABLE tableName" to check segment status.

After the streaming segment reaches the max size, CarbonData will change the segment status to "streaming finish" from "streaming", and create new "streaming" segment to continue to ingest streaming data.

| option | default | description |
| --- | --- | --- |
| carbon.streaming.segment.max.size | 1024000000 | Unit: byte max size of streaming segment |

| segment status | description |
| --- | --- |
| streaming | The segment is running streaming ingestion |
| streaming finish | The segment already finished streaming ingestion, it will be handed off to a segment in the columnar format |

<a id="streaming-guide--change-segment-status"></a>

## Change segment status

Use below command to change the status of "streaming" segment to "streaming finish" segment. If the streaming application is running, this command will be blocked.

```
ALTER TABLE streaming_table FINISH STREAMING
```

<a id="streaming-guide--handoff-streaming-finish-segment-to-columnar-segment"></a>

## Handoff "streaming finish" segment to columnar segment

Use below command to handoff "streaming finish" segment to columnar format segment manually.

```
ALTER TABLE streaming_table COMPACT 'streaming'
```

<a id="streaming-guide--auto-handoff-streaming-segment"></a>

## Auto handoff streaming segment

Config the property "carbon.streaming.auto.handoff.enabled" to auto handoff streaming segment. If the value of this property is true, after the streaming segment reaches the max size, CarbonData will change this segment to "streaming finish" status and trigger to auto handoff this segment to columnar format segment in a new thread.

| property name | default | description |
| --- | --- | --- |
| carbon.streaming.auto.handoff.enabled | true | whether to auto trigger handoff operation |

<a id="streaming-guide--stream-data-parser"></a>

## Stream data parser

Config the property "carbon.stream.parser" to define a stream parser to convert InternalRow to Object[] when write stream data.

| property name | default | description |
| --- | --- | --- |
| carbon.stream.parser | org.apache.carbondata.streaming.parser.RowStreamParserImp | the class of the stream parser |

Currently CarbonData support two parsers, as following:

**1. org.apache.carbondata.streaming.parser.CSVStreamParserImp**: This parser gets a line data(String type) from the first index of InternalRow and converts this String to Object[].

**2. org.apache.carbondata.streaming.parser.RowStreamParserImp**: This is the default stream parser, it will auto convert InternalRow to Object[] according to schema of this `DataSet`, for example:

```
 case class FileElement(school: Array[String], age: Int)
 case class StreamData(id: Int, name: String, city: String, salary: Float, file: FileElement)
 ...

 var qry: StreamingQuery = null
 val readSocketDF = spark.readStream
   .format("socket")
   .option("host", "localhost")
   .option("port", 9099)
   .load()
   .as[String]
   .map(_.split(","))
   .map { fields => {
     val tmp = fields(4).split("\\$")
     val file = FileElement(tmp(0).split(":"), tmp(1).toInt)
     StreamData(fields(0).toInt, fields(1), fields(2), fields(3).toFloat, file)
   } }

 // Write data from socket stream to carbondata file
 qry = readSocketDF.writeStream
   .format("carbondata")
   .trigger(ProcessingTime("5 seconds"))
   .option("checkpointLocation", tablePath.getStreamingCheckpointDir)
   .option("dbName", "default")
   .option("tableName", "carbon_table")
   .start()

 ...
```

<a id="streaming-guide--how-to-implement-a-customized-stream-parser"></a>

### How to implement a customized stream parser

If user needs to implement a customized stream parser to convert a specific InternalRow to Object[], it needs to implement `initialize` method and `parserRow` method of interface `CarbonStreamParser`, for example:

```
 package org.XXX.XXX.streaming.parser
 
 import org.apache.hadoop.conf.Configuration
 import org.apache.spark.sql.catalyst.InternalRow
 import org.apache.spark.sql.types.StructType
 
 class XXXStreamParserImp extends CarbonStreamParser {
 
   override def initialize(configuration: Configuration, structType: StructType): Unit = {
     // user can get the properties from "configuration"
   }
   
   override def parserRow(value: InternalRow): Array[Object] = {
     // convert InternalRow to Object[](Array[Object] in Scala) 
   }
   
   override def close(): Unit = {
   }
 }
   
```

and then set the property "carbon.stream.parser" to "org.XXX.XXX.streaming.parser.XXXStreamParserImp".

<a id="streaming-guide--close-streaming-table"></a>

## Close streaming table

Use below command to handoff all streaming segments to columnar format segments and modify the streaming property to false, this table becomes a normal table.

```
ALTER TABLE streaming_table COMPACT 'close_streaming'
```

<a id="streaming-guide--constraint"></a>

## Constraint

1. reject set streaming property from true to false.
2. reject UPDATE/DELETE command on the streaming table.
3. reject create MV on the streaming table.
4. reject add the streaming property on the table with MV.
5. if the table has dictionary columns, it will not support concurrent data loading.
6. block delete "streaming" segment while the streaming ingestion is running.
7. block drop the streaming table while the streaming ingestion is running.

<a id="streaming-guide--streamsql"></a>

## StreamSQL

<a id="streaming-guide--streaming-table"></a>

### Streaming Table

**Example**

Following example shows how to start a streaming ingest job

```
    sql(
      s"""
         |CREATE TABLE source(
         | id INT,
         | name STRING,
         | city STRING,
         | salary FLOAT,
         | tax DECIMAL(8,2),
         | percent double,
         | birthday DATE,
         | register TIMESTAMP,
         | updated TIMESTAMP
         |)
         |STORED AS carbondata
         |TBLPROPERTIES (
         | 'streaming'='source',
         | 'format'='csv',
         | 'path'='$csvDataDir'
         |)
      """.stripMargin)

    sql(
      s"""
         |CREATE TABLE sink(
         | id INT,
         | name STRING,
         | city STRING,
         | salary FLOAT,
         | tax DECIMAL(8,2),
         | percent double,
         | birthday DATE,
         | register TIMESTAMP,
         | updated TIMESTAMP
         |)
         |STORED AS carbondata
         |TBLPROPERTIES (
         |  'streaming'='true'
         |)
      """.stripMargin)

    sql(
      """
        |CREATE STREAM job123 ON TABLE sink
        |STMPROPERTIES(
        |  'trigger'='ProcessingTime',
        |  'interval'='1 seconds')
        |AS
        |  SELECT *
        |  FROM source
        |  WHERE id % 2 = 1
      """.stripMargin)

    sql("DROP STREAM job123")

    sql("SHOW STREAMS [ON TABLE tableName]")
```

In above example, two table is created: source and sink. The `source` table's format is `csv` and `sink` table format is `carbon`. Then a streaming job is created to stream data from source table to sink table.

These two tables are normal carbon tables, they can be queried independently.

<a id="streaming-guide--streaming-job-management"></a>

### Streaming Job Management

As above example shown:

- `CREATE STREAM jobName ON TABLE tableName` is used to start a streaming ingest job.
- `DROP STREAM jobName` is used to stop a streaming job by its name
- `SHOW STREAMS [ON TABLE tableName]` is used to print streaming job information

<a id="streaming-guide--create-stream"></a>

##### CREATE STREAM

When this is issued, carbon will start a structured streaming job to do the streaming ingestion. Before launching the job, system will validate:

- The format of table specified in CTAS FROM clause must be one of: csv, json, text, parquet, kafka, socket. These are formats supported by spark 2.2.0 structured streaming
- User should pass the options of the streaming source table in its TBLPROPERTIES when creating it. StreamSQL will pass them transparently to spark when creating the streaming job. For example:


```
CREATE TABLE source(
  name STRING,
  age INT
)
STORED AS carbondata
TBLPROPERTIES(
 'streaming'='source',
 'format'='socket',
 'host'='localhost',
 'port'='8888',
 'record_format'='csv', // can be csv or json, default is csv
 'delimiter'='|'
)
```

  will translate to


```
spark.readStream
	 .schema(tableSchema)
	 .format("socket")
	 .option("host", "localhost")
	 .option("port", "8888")
	 .option("delimiter", "|")
```

- The sink table should have a TBLPROPERTY `'streaming'` equal to `true`, indicating it is a streaming table.
- In the given STMPROPERTIES, user must specify `'trigger'`, its value must be `ProcessingTime` (In future, other value will be supported). User should also specify interval value for the streaming job.
- If the schema specified in sink table is different from CTAS, the streaming job will fail

For Kafka data source, create the source table by:

```
CREATE TABLE source(
  name STRING,
  age INT
)
STORED AS carbondata
TBLPROPERTIES(
 'streaming'='source',
 'format'='kafka',
 'kafka.bootstrap.servers'='kafkaserver:9092',
 'subscribe'='test'
 'record_format'='csv', // can be csv or json, default is csv
 'delimiter'='|'
)
```

- Then CREATE STREAM can be used to start the streaming ingest job from source table to sink table

```
CREATE STREAM job123 ON TABLE sink
STMPROPERTIES(
    'trigger'='ProcessingTime',
     'interval'='10 seconds'
) 
AS
   SELECT *
   FROM source
   WHERE id % 2 = 1
```

<a id="streaming-guide--drop-stream"></a>

##### DROP STREAM

When `DROP STREAM` is issued, the streaming job will be stopped immediately. It will fail if the jobName specified is not exist.

```
DROP STREAM job123
```

<a id="streaming-guide--show-streams"></a>

##### SHOW STREAMS

`SHOW STREAMS ON TABLE tableName` command will print the streaming job information as following

| Job name | status | Source | Sink | start time | time elapsed |
| --- | --- | --- | --- | --- | --- |
| job123 | Started | device | fact | 2018-02-03 14:32:42 | 10d2h32m |

`SHOW STREAMS` command will show all stream jobs in the system.

<a id="streaming-guide--alter-table-close-stream"></a>

##### ALTER TABLE CLOSE STREAM

When the streaming application is stopped, and user want to manually trigger data conversion from carbon streaming files to columnar files, one can use
`ALTER TABLE sink COMPACT 'CLOSE_STREAMING';`

[Top](#streaming-guide--top)

---

<a id="configuration-parameters"></a>

<!-- source_url: https://carbondata.apache.org/configuration-parameters.html -->

<!-- page_index: 8 -->

<a id="configuration-parameters--configuring-carbondata"></a>

# Configuring CarbonData

This guide explains the configurations that can be used to tune CarbonData to achieve better performance. Most of the properties that control the internal settings have reasonable default values. They are listed along with the properties along with explanation.

- [System Configuration](#configuration-parameters--system-configuration)
- [Data Loading Configuration](#configuration-parameters--data-loading-configuration)
- [Compaction Configuration](#configuration-parameters--compaction-configuration)
- [Query Configuration](#configuration-parameters--query-configuration)
- [Data Mutation Configuration](#configuration-parameters--data-mutation-configuration)
- [Dynamic Configuration In CarbonData Using SET-RESET](#configuration-parameters--dynamic-configuration-in-carbondata-using-set-reset)

<a id="configuration-parameters--system-configuration"></a>

## System Configuration

This section provides the details of all the configurations required for the CarbonData System.

| Property | Default Value | Description |
| --- | --- | --- |
| carbon.ddl.base.hdfs.url | (none) | To simplify and shorten the path to be specified in DDL/DML commands, this property is supported. This property is used to configure the HDFS relative path, the path configured in carbon.ddl.base.hdfs.url will be appended to the HDFS path configured in fs.defaultFS of core-site.xml. If this path is configured, then user need not pass the complete path while dataload. For example: If absolute path of the csv file is hdfs://10.18.101.155:54310/data/cnbc/2016/xyz.csv, the path "hdfs://10.18.101.155:54310" will come from property fs.defaultFS and user can configure the /data/cnbc/ as carbon.ddl.base.hdfs.url. Now while dataload user can specify the csv path as /2016/xyz.csv. |
| carbon.badRecords.location | (none) | CarbonData can detect the records not conforming to defined table schema and isolate them as bad records. This property is used to specify where to store such bad records. |
| carbon.streaming.auto.handoff.enabled | true | CarbonData supports storing of streaming data. To have high throughput for streaming, the data is written in Row format which is highly optimized for write, but performs poorly for query. When this property is true and when the streaming data size reaches ***carbon.streaming.segment.max.size***, CabonData will automatically convert the data to columnar format and optimize it for faster querying. **NOTE:** It is not recommended to keep the default value which is true. |
| carbon.streaming.segment.max.size | 1024000000 | CarbonData writes streaming data in row format which is optimized for high write throughput. This property defines the maximum size of data to be held is row format, beyond which it will be converted to columnar format in order to support high performance query, provided ***carbon.streaming.auto.handoff.enabled*** is true. **NOTE:** Setting higher value will impact the streaming ingestion. The value has to be configured in bytes. |
| carbon.segment.lock.files.preserve.hours | 48 | In order to support parallel data loading onto the same table, CarbonData sequences(locks) at the granularity of segments. Operations affecting the segment(like IUD, alter) are blocked from parallel operations. This property value indicates the number of hours the segment lock files will be preserved after dataload. These lock files will be deleted with the clean command after the configured number of hours. |
| carbon.timestamp.format | yyyy-MM-dd HH:mm:ss | CarbonData can understand data of timestamp type and process it in special manner. It can be so that the format of Timestamp data is different from that understood by CarbonData by default. This configuration allows users to specify the format of Timestamp in their data. |
| carbon.lock.type | LOCALLOCK | This configuration specifies the type of lock to be acquired during concurrent operations on table. There are following types of lock implementation: - LOCALLOCK: Lock is created on local file system as file. This lock is useful when only one spark driver (thrift server) runs on a machine and no other CarbonData spark application is launched concurrently. - HDFSLOCK: Lock is created on HDFS file system as file. This lock is useful when multiple CarbonData spark applications are launched and no ZooKeeper is running on cluster and HDFS supports file based locking. |
| carbon.lock.path | TABLEPATH | This configuration specifies the path where lock files have to be created. Recommended to configure zookeeper lock type or configure HDFS lock path(to this property) in case of S3 file system as locking is not feasible on S3. |
| enable.offheap.sort | true | Whether carbondata will use offheap or onheap memory. By default, the value is true and carbondata will use the property value from *carbon.unsafe.working.memory.in.mb* or *carbon.unsafe.driver.working.memory.in.mb* as the amount of memory; if it is false, carbondata will use the minimum value between the configured amount of unsafe memory and the 60% of JVM Heap Memory as the amount of memory. |
| carbon.unsafe.working.memory.in.mb | 512 | CarbonData supports storing data in off-heap memory for certain operations during data loading and query. This helps to avoid the Java GC and thereby improve the overall performance. The Minimum value recommeded is 512MB. Any value below this is reset to default value of 512MB. **NOTE:** The below formulas explain how to arrive at the off-heap size required.Memory Required For Data Loading per executor: (*carbon.number.of.cores.while.loading*) \* (Number of tables to load in parallel) \* (*offheap.sort.chunk.size.inmb* + *carbon.blockletgroup.size.in.mb* + *carbon.blockletgroup.size.in.mb*/3.5 ). Memory required for Query per executor: (*carbon.blockletgroup.size.in.mb* + *carbon.blockletgroup.size.in.mb* \* 3.5) \* spark.executor.cores |
| carbon.unsafe.driver.working.memory.in.mb | (none) | CarbonData supports storing data in unsafe on-heap memory in driver for certain operations like insert into, query for loading index cache. The Minimum value recommended is 512MB. If this configuration is not set, carbondata will use the value of `carbon.unsafe.working.memory.in.mb`. |
| carbon.update.sync.folder | /tmp/carbondata | CarbonData maintains last modification time entries in modifiedTime.htmlt to determine the schema changes and reload only when necessary. This configuration specifies the path where the file needs to be written. |
| carbon.invisible.segments.preserve.count | 200 | CarbonData maintains each data load entry in tablestatus file. The entries from this file are not deleted for those segments that are compacted or dropped, but are made invisible. If the number of data loads are very high, the size and number of entries in tablestatus file can become too many causing unnecessary reading of all data. This configuration specifies the number of segment entries to be maintained afte they are compacted or dropped. Beyond this, the entries are moved to a separate history tablestatus file. **NOTE:** The entries in tablestatus file help to identify the operations performed on CarbonData table and is also used for checkpointing during various data manupulation operations. This is similar to AUDIT file maintaining all the operations and its status. Hence the entries are never deleted but moved to a separate history file. |
| carbon.lock.retries | 3 | CarbonData ensures consistency of operations by blocking certain operations from running in parallel. In order to block the operations from running in parallel, lock is obtained on the table. This configuration specifies the maximum number of retries to obtain the lock for any operations other than load. **NOTE:** Data manupulation operations like Compaction,UPDATE,DELETE or LOADING,UPDATE,DELETE are not allowed to run in parallel. How ever data loading can happen in parallel to compaction. |
| carbon.lock.retry.timeout.sec | 5 | Specifies the interval between the retries to obtain the lock for any operation other than load. **NOTE:** Refer to ***carbon.lock.retries*** for understanding why CarbonData uses locks for operations. |
| carbon.fs.custom.file.provider | None | To support FileTypeInterface for configuring custom CarbonFile implementation to work with custom FileSystem. |
| carbon.timeseries.first.day.of.week | SUNDAY | This parameter configures which day of the week to be considered as first day of the week. Because first day of the week will be different in different parts of the world. |
| carbon.enable.tablestatus.backup | false | In cloud object store scenario, overwriting table status file is not an atomic operation since it uses rename API. Thus, it is possible that table status is corrupted if process crashed when overwriting the table status file. To protect from file corruption, user can enable this property. |

<a id="configuration-parameters--data-loading-configuration"></a>

## Data Loading Configuration

| Parameter | Default Value | Description |
| --- | --- | --- |
| carbon.concurrent.lock.retries | 100 | CarbonData supports concurrent data loading onto same table. To ensure the loading status is correctly updated into the system,locks are used to sequence the status updation step. This configuration specifies the maximum number of retries to obtain the lock for updating the load status. **NOTE:** This value is high as more number of concurrent loading happens,more the chances of not able to obtain the lock when tried. Adjust this value according to the number of concurrent loading to be supported by the system. |
| carbon.concurrent.lock.retry.timeout.sec | 1 | Specifies the interval between the retries to obtain the lock for concurrent operations. **NOTE:** Refer to ***carbon.concurrent.lock.retries*** for understanding why CarbonData uses locks during data loading operations. |
| carbon.csv.read.buffersize.byte | 1048576 | CarbonData uses Hadoop InputFormat to read the csv files. This configuration value is used to pass buffer size as input for the Hadoop MR job when reading the csv files. This value is configured in bytes. **NOTE:** Refer to ***org.apache.hadoop.mapreduce. InputFormat*** documentation for additional information. |
| carbon.loading.prefetch | false | CarbonData uses univocity parser to read csv files. This configuration is used to inform the parser whether it can prefetch the data from csv files to speed up the reading. **NOTE:** Enabling prefetch improves the data loading performance, but needs higher memory to keep more records which are read ahead from disk. |
| carbon.skip.empty.line | false | The csv files givent to CarbonData for loading can contain empty lines. Based on the business scenario, this empty line might have to be ignored or needs to be treated as NULL value for all columns. In order to define this business behavior, this configuration is provided. **NOTE:** In order to consider NULL values for non string columns and continue with data load, ***carbon.bad.records.action*** need to be set to **FORCE**;else data load will be failed as bad records encountered. |
| carbon.number.of.cores.while.loading | 2 | Number of cores to be used while loading data. This also determines the number of threads to be used to read the input files (csv) in parallel. **NOTE:** This configured value is used in every data loading step to parallelize the operations. Configuring a higher value can lead to increased early thread pre-emption by OS and there by reduce the overall performance. |
| enable.unsafe.sort | true | CarbonData supports unsafe operations of Java to avoid GC overhead for certain operations. This configuration enables to use unsafe functions in CarbonData. **NOTE:** For operations like data loading, which generates more short lived Java objects, Java GC can be a bottle neck. Using unsafe can overcome the GC overhead and improve the overall performance. |
| enable.offheap.sort | true | CarbonData supports storing data in off-heap memory for certain operations during data loading and query. This helps to avoid the Java GC and thereby improve the overall performance. This configuration enables using off-heap memory for sorting of data during data loading.**NOTE:** ***enable.unsafe.sort*** configuration needs to be configured to true for using off-heap |
| carbon.load.sort.scope | NO\_SORT [If sort columns are not specified while creating table] and LOCAL\_SORT [If sort columns are specified] | CarbonData can support various sorting options to match the balance between load and query performance. LOCAL\_SORT: All the data given to an executor in the single load is fully sorted and written to carbondata files. Data loading performance is reduced a little as the entire data needs to be sorted in the executor. GLOBAL SORT: Entire data in the data load is fully sorted and written to carbondata files. Data loading performance would get reduced as the entire data needs to be sorted. But the query performance increases significantly due to very less false positives and concurrency is also improved. **NOTE 1:** This property will be taken into account only when SORT COLUMNS are specified explicitly while creating table, otherwise it is always NO SORT |
| carbon.global.sort.rdd.storage.level | MEMORY\_ONLY | Storage level to persist dataset of RDD/dataframe when loading data with 'sort\_scope'='global\_sort', if user's executor has less memory, set this parameter to 'MEMORY\_AND\_DISK\_SER' or other storage level to correspond to different environment. [See detail](http://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence). |
| carbon.load.global.sort.partitions | 0 | The number of partitions to use when shuffling data for global sort. Default value 0 means to use same number of map tasks as reduce tasks. **NOTE:** In general, it is recommended to have 2-3 tasks per CPU core in your cluster. |
| carbon.sort.size | 100000 | Number of records to hold in memory to sort and write intermediate sort temp files. **NOTE:** Memory required for data loading will increase if you turn this value bigger. Besides each thread will cache this amout of records. The number of threads is configured by *carbon.number.of.cores.while.loading*. |
| carbon.options.bad.records.logger.enable | false | CarbonData can identify the records that are not conformant to schema and isolate them as bad records. Enabling this configuration will make CarbonData to log such bad records. **NOTE:** If the input data contains many bad records, logging them will slow down the over all data loading throughput. The data load operation status would depend on the configuration in ***carbon.bad.records.action***. |
| carbon.bad.records.action | FAIL | CarbonData in addition to identifying the bad records, can take certain actions on such data. This configuration can have four types of actions for bad records namely FORCE, REDIRECT, IGNORE and FAIL. If set to FORCE then it auto-corrects the data by storing the bad records as NULL. If set to REDIRECT then bad records are written to the raw CSV instead of being loaded. If set to IGNORE then bad records are neither loaded nor written to the raw CSV. If set to FAIL then data loading fails if any bad records are found. |
| carbon.options.is.empty.data.bad.record | false | Based on the business scenarios, empty("" or '' or ,,) data can be valid or invalid. This configuration controls how empty data should be treated by CarbonData. If false, then empty ("" or '' or ,,) data will not be considered as bad record and vice versa. |
| carbon.options.bad.record.path | (none) | Specifies the HDFS path where bad records are to be stored. By default the value is Null. This path must be configured by the user if ***carbon.options.bad.records.logger.enable*** is **true** or ***carbon.bad.records.action*** is **REDIRECT**. |
| carbon.blockletgroup.size.in.mb | 64 | Please refer to [file-structure-of-carbondata](https://carbondata.apache.org/file-structure-of-carbondata.html#carbondata-file-format) to understand the storage format of CarbonData. The data are read as a group of blocklets which are called blocklet groups. This parameter specifies the size of each blocklet group. Higher value results in better sequential IO access. The minimum value is 16MB, any value lesser than 16MB will reset to the default value (64MB). **NOTE:** Configuring a higher value might lead to poor performance as an entire blocklet group will have to read into memory before processing. For filter queries with limit, it is **not advisable** to have a bigger blocklet size. For aggregation queries which need to return more number of rows, bigger blocklet size is advisable. |
| carbon.sort.file.write.buffer.size | 16384 | CarbonData sorts and writes data to intermediate files to limit the memory usage. This configuration determines the buffer size to be used for reading and writing such files. **NOTE:** This configuration is useful to tune IO and derive optimal performance. Based on the OS and underlying harddisk type, these values can significantly affect the overall performance. It is ideal to tune the buffer size equivalent to the IO buffer size of the OS. Recommended range is between 10240 and 10485760 bytes. |
| carbon.sort.intermediate.files.limit | 20 | CarbonData sorts and writes data to intermediate files to limit the memory usage. Before writing the target carbondata file, the records in these intermediate files needs to be merged to reduce the number of intermediate files. This configuration determines the minimum number of intermediate files after which merged sort is applied on them sort the data. **NOTE:** Intermediate merging happens on a separate thread in the background. Number of threads used is determined by ***carbon.merge.sort.reader.thread***. Configuring a low value will cause more time to be spent in merging these intermediate merged files which can cause more IO. Configuring a high value would cause not to use the idle threads to do intermediate sort merges. Recommended range is between 2 and 50. |
| carbon.merge.sort.reader.thread | 3 | CarbonData sorts and writes data to intermediate files to limit the memory usage. When the intermediate files reaches ***carbon.sort.intermediate.files.limit***, the files will be merged in another thread pool. This value will control the size of the pool. Each thread will read the intermediate files and do merge sort and finally write the records to another file. **NOTE:** Refer to ***carbon.sort.intermediate.files.limit*** for operation description. Configuring smaller number of threads can cause merging slow down over loading process whereas configuring larger number of threads can cause thread contention with threads in other data loading steps. Hence configure a fraction of ***carbon.number.of.cores.while.loading***. |
| carbon.merge.sort.prefetch | true | CarbonData writes every ***carbon.sort.size*** number of records to intermediate temp files during data loading to ensure memory footprint is within limits. These intermediate temp files will have to be sorted using merge sort before writing into CarbonData format. This configuration enables pre fetching of data from these temp files in order to optimize IO and speed up data loading process. |
| carbon.prefetch.buffersize | 1000 | When the configuration ***carbon.merge.sort.prefetch*** is configured to true, we need to set the number of records that can be prefetched. This configuration is used specify the number of records to be prefetched.\*\*NOTE: \*\*Configuring more number of records to be prefetched increases memory footprint as more records will have to be kept in memory. |
| carbon.sort.storage.inmemory.size.inmb | 512 | CarbonData writes every ***carbon.sort.size*** number of records to intermediate temp files during data loading to ensure memory footprint is within limits. When ***enable.unsafe.sort*** configuration is enabled, instead of using ***carbon.sort.size*** which is based on rows count, size occupied in memory is used to determine when to flush data pages to intermediate temp files. This configuration determines the memory to be used for storing data pages in memory. **NOTE:** Configuring a higher value ensures more data is maintained in memory and hence increases data loading performance due to reduced or no IO. Based on the memory availability in the nodes of the cluster, configure the values accordingly. |
| carbon.load.sortmemory.spill.percentage | 0 | During data loading, some data pages are kept in memory upto memory configured in ***carbon.sort.storage.inmemory.size.inmb*** beyond which they are spilled to disk as intermediate temporary sort files. This configuration determines after what percentage data needs to be spilled to disk. **NOTE:** Without this configuration, when the data pages occupy upto configured memory, new data pages would be dumped to disk and old pages are still maintained in disk. |
| carbon.enable.calculate.size | true | **For Load Operation**: Enabling this property will let carbondata calculate the size of the carbon data file (.carbondata) and the carbon index file (.carbonindex) for each load and update the table status file. **For Describe Formatted**: Enabling this property will let carbondata calculate the total size of the carbon data files and the carbon index files for the each table and display it in describe formatted command. **NOTE:** This is useful to determine the overall size of the carbondata table and also get an idea of how the table is growing in order to take up other backup strategy decisions. |
| carbon.cutOffTimestamp | (none) | CarbonData has capability to generate the Dictionary values for the timestamp columns from the data itself without the need to store the computed dictionary values. This configuration sets the start date for calculating the timestamp. Java counts the number of milliseconds from start of "1970-01-01 00:00:00". This property is used to customize the start of position. For example "2000-01-01 00:00:00". **NOTE:** The date must be in the form ***carbon.timestamp.format***. CarbonData supports storing data for upto 68 years. For example, if the cut-off time is 1970-01-01 05:30:00, then data upto 2038-01-01 05:30:00 will be supported by CarbonData. |
| carbon.timegranularity | SECOND | The configuration is used to specify the data granularity level such as DAY, HOUR, MINUTE, or SECOND. This helps to store more than 68 years of data into CarbonData. |
| carbon.use.local.dir | true | CarbonData,during data loading, writes files to local temp directories before copying the files to HDFS. This configuration is used to specify whether CarbonData can write locally to tmp directory of the container or to the YARN application directory. |
| carbon.sort.temp.compressor | SNAPPY | CarbonData writes every ***carbon.sort.size*** number of records to intermediate temp files during data loading to ensure memory footprint is within limits. These temporary files can be compressed and written in order to save the storage space. This configuration specifies the name of compressor to be used to compress the intermediate sort temp files during sort procedure in data loading. The valid values are 'SNAPPY','GZIP','BZIP2','LZ4','ZSTD' and empty. By default, empty means that Carbondata will not compress the sort temp files. **NOTE:** Compressor will be useful if you encounter disk bottleneck. Since the data needs to be compressed and decompressed,it involves additional CPU cycles,but is compensated by the high IO throughput due to less data to be written or read from the disks. |
| carbon.load.skewedDataOptimization.enabled | false | During data loading,CarbonData would divide the number of blocks equally so as to ensure all executors process same number of blocks. This mechanism satisfies most of the scenarios and ensures maximum parallel processing for optimal data loading performance. In some business scenarios, there might be scenarios where the size of blocks vary significantly and hence some executors would have to do more work if they get blocks containing more data. This configuration enables size based block allocation strategy for data loading. When loading, carbondata will use file size based block allocation strategy for task distribution. It will make sure that all the executors process the same size of data. **NOTE:** This configuration is useful if the size of your input data files varies widely, say 1MB to 1GB. For this configuration to work effectively,knowing the data pattern and size is important and necessary. |
| enable.data.loading.statistics | false | CarbonData has extensive logging which would be useful for debugging issues related to performance or hard to locate issues. This configuration when made ***true*** would log additional data loading statistics information to more accurately locate the issues being debugged. **NOTE:** Enabling this would log more debug information to log files, there by increasing the log files size significantly in short span of time. It is advised to configure the log files size, retention of log files parameters in log4j properties appropriately. Also extensive logging is an increased IO operation and hence over all data loading performance might get reduced. Therefore it is recommended to enable this configuration only for the duration of debugging. |
| carbon.dictionary.chunk.size | 10000 | CarbonData generates dictionary keys and writes them to separate dictionary file during data loading. To optimize the IO, this configuration determines the number of dictionary keys to be persisted to dictionary file at a time. **NOTE:** Writing to file also serves as a commit point to the dictionary generated. Increasing more values in memory causes more data loss during system or application failure. It is advised to alter this configuration judiciously. |
| carbon.load.directWriteToStorePath.enabled | false | During data load, all the carbondata files are written to local disk and finally copied to the target store location in HDFS/S3. Enabling this parameter will make carbondata files to be written directly onto target HDFS/S3 location bypassing the local disk. **NOTE:** Writing directly to HDFS/S3 saves local disk IO(once for writing the files and again for copying to HDFS/S3) there by improving the performance. But the drawback is when data loading fails or the application crashes, unwanted carbondata files will remain in the target HDFS/S3 location until it is cleared during next data load or by running *CLEAN FILES* DDL command |
| carbon.options.serialization.null.format | \N | Based on the business scenarios, some columns might need to be loaded with null values. As null value cannot be written in csv files, some special characters might be adopted to specify null values. This configuration can be used to specify the null values format in the data being loaded. |
| carbon.column.compressor | snappy | CarbonData will compress the column values using the compressor specified by this configuration. Currently CarbonData supports 'snappy', 'zstd' and 'gzip' compressors. |
| carbon.minmax.allowed.byte.count | 200 | CarbonData will write the min max values for string/varchar types column using the byte count specified by this configuration. Max value is 1000 bytes(500 characters) and Min value is 10 bytes(5 characters). **NOTE:** This property is useful for reducing the store size thereby improving the query performance but can lead to query degradation if value is not configured properly. |
| carbon.merge.index.failure.throw.exception | true | It is used to configure whether or not merge index failure should result in data load failure also. |
| carbon.binary.decoder | None | Support configurable decode for loading. Two decoders supported: base64 and hex |
| carbon.local.dictionary.size.threshold.inmb | 4 | size based threshold for local dictionary in MB, maximum allowed size is 16 MB. |
| carbon.enable.bad.record.handling.for.insert | false | by default, disable the bad record and converter step during "insert into" |

<a id="configuration-parameters--compaction-configuration"></a>

## Compaction Configuration

| Parameter | Default Value | Description |
| --- | --- | --- |
| carbon.number.of.cores.while.compacting | 2 | Number of cores to be used while compacting data. This also determines the number of threads to be used to read carbondata files in parallel. |
| carbon.compaction.level.threshold | 4, 3 | Each CarbonData load will create one segment, if every load is small in size it will generate many small file over a period of time impacting the query performance. This configuration is for minor compaction which decides how many segments to be merged. Configuration is of the form (x,y). Compaction will be triggered for every x segments and form a single level 1 compacted segment. When the number of compacted level 1 segments reach y, compaction will be triggered again to merge them to form a single level 2 segment. For example: If it is set as 2, 3 then minor compaction will be triggered for every 2 segments. 3 is the number of level 1 compacted segments which is further compacted to new segment. **NOTE:** When ***carbon.enable.auto.load.merge*** is **true**, configuring higher values cause overall data loading time to increase as compaction will be triggered after data loading is complete but status is not returned till compaction is complete. But compacting more number of segments can increase query performance. Hence optimal values needs to be configured based on the business scenario. Valid values are between 0 to 100. |
| carbon.major.compaction.size | 1024 | To improve query performance and all the segments can be merged and compacted to a single segment upto configured size. This Major compaction size can be configured using this parameter. Sum of the segments which is below this threshold will be merged. This value is expressed in MB. |
| carbon.horizontal.compaction.enable | true | CarbonData supports DELETE/UPDATE functionality by creating delta data files for existing carbondata files. These delta files would grow as more number of DELETE/UPDATE operations are performed. Compaction of these delta files are termed as horizontal compaction. This configuration is used to turn ON/OFF horizontal compaction. After every DELETE and UPDATE statement, horizontal compaction may occur in case the delta (DELETE/ UPDATE) files becomes more than specified threshold. **NOTE:** Having many delta files will reduce the query performance as scan has to happen on all these files before the final state of data can be decided. Hence it is advisable to keep horizontal compaction enabled and configure reasonable values to ***carbon.horizontal.DELETE.compaction.threshold*** |
| carbon.horizontal.delete.compaction.threshold | 1 | This configuration specifies the threshold limit on number of DELETE delta files within a block of a segment. In case the number of delta files goes beyond the threshold, the DELETE delta files for the particular block of the segment becomes eligible for horizontal compaction and are compacted into single DELETE delta file. Values range between 1 to 10000. |
| carbon.update.segment.parallelism | 1 | CarbonData processes the UPDATE operations by grouping records belonging to a segment into a single executor task. When the amount of data to be updated is more, this behavior causes problems like restarting of executor due to low memory and data-spill related errors. This property specifies the parallelism for each segment during update. **NOTE:** It is recommended to set this value to a multiple of the number of executors for balance. Values range between 1 to 1000. |
| carbon.numberof.preserve.segments | 0 | If the user wants to preserve some number of segments from being compacted then he can set this configuration. Example: carbon.numberof.preserve.segments = 2 then 2 latest segments will always be excluded from the compaction. No segments will be preserved by default. **NOTE:** This configuration is useful when the chances of input data can be wrong due to environment scenarios. Preserving some of the latest segments from being compacted can help to easily delete the wrongly loaded segments. Once compacted,it becomes more difficult to determine the exact data to be deleted(except when data is incrementing according to time) |
| carbon.allowed.compaction.days | 0 | This configuration is used to control on the number of recent segments that needs to be compacted, ignoring the older ones. This configuration is in days. For Example: If the configuration is 2, then the segments which are loaded in the time frame of past 2 days only will get merged. Segments which are loaded earlier than 2 days will not be merged. This configuration is disabled by default. **NOTE:** This configuration is useful when a bulk of history data is loaded into the carbondata. Query on this data is less frequent. In such cases involving these segments also into compaction will affect the resource consumption, increases overall compaction time. |
| carbon.enable.auto.load.merge | false | Compaction can be automatically triggered once data load completes. This ensures that the segments are merged in time and thus query times does not increase with increase in segments. This configuration enables to do compaction along with data loading. **NOTE:** Compaction will be triggered once the data load completes. But the status of data load wait till the compaction is completed. Hence it might look like data loading time has increased, but thats not the case. Moreover failure of compaction will not affect the data loading status. If data load had completed successfully, the status would be updated and segments are committed. However, failure while data loading, will not trigger compaction and error is returned immediately. |
| carbon.enable.page.level.reader.in.compaction | false | Enabling page level reader for compaction reduces the memory usage while compacting more number of segments. It allows reading only page by page instead of reading whole blocklet to memory. **NOTE:** Please refer to [file-structure-of-carbondata](https://carbondata.apache.org/file-structure-of-carbondata.html#carbondata-file-format) to understand the storage format of CarbonData and concepts of pages. |
| carbon.concurrent.compaction | true | Compaction of different tables can be executed concurrently. This configuration determines whether to compact all qualifying tables in parallel or not. **NOTE:** Compacting concurrently is a resource demanding operation and needs more resources there by affecting the query performance also. This configuration is **deprecated** and might be removed in future releases. |
| carbon.compaction.prefetch.enable | false | Compaction operation is similar to Query + data load where in data from qualifying segments are queried and data loading performed to generate a new single segment. This configuration determines whether to query ahead data from segments and feed it for data loading. **NOTE:** This configuration is disabled by default as it needs extra resources for querying extra data. Based on the memory availability on the cluster, user can enable it to improve compaction performance. |
| carbon.merge.index.in.segment | true | Each CarbonData file has a companion CarbonIndex file which maintains the metadata about the data. These CarbonIndex files are read and loaded into driver and is used subsequently for pruning of data during queries. These CarbonIndex files are very small in size(few KB) and are many. Reading many small files from HDFS is not efficient and leads to slow IO performance. Hence these CarbonIndex files belonging to a segment can be combined into a single file and read once there by increasing the IO throughput. This configuration enables to merge all the CarbonIndex files into a single MergeIndex file upon data loading completion. **NOTE:** Reading a single big file is more efficient in HDFS and IO throughput is very high. Due to this the time needed to load the index files into memory when query is received for the first time on that table is significantly reduced and there by significantly reduces the delay in serving the first query. |
| carbon.enable.range.compaction | true | To configure Ranges-based Compaction to be used or not for RANGE\_COLUMN. If true after compaction also the data would be present in ranges. |
| carbon.si.segment.merge | false | Making this true degrade the LOAD performance. When the number of small files increase for SI segments(it can happen as number of columns will be less and we store position id and reference columns), user an either set to true which will merge the data files for upcoming loads or run SI refresh command which does this job for all segments. (REFRESH INDEX <index\_table>) |

<a id="configuration-parameters--query-configuration"></a>

## Query Configuration

| Parameter | Default Value | Description |
| --- | --- | --- |
| carbon.max.driver.lru.cache.size | -1 | Maximum memory **(in MB)** upto which the driver process can cache the data (BTree and dictionary values). Beyond this, least recently used data will be removed from cache before loading new set of values. Default value of -1 means there is no memory limit for caching. Only integer values greater than 0 are accepted. **NOTE:** Minimum number of entries that needs to be removed from cache in order to load the new set of data is determined and unloaded.ie.,for example if 3 cache entries qualify for pre-emption, out of these, those entries that free up more cache memory is removed prior to others. Please refer [FAQs](#faq--how-to-check-lru-cache-memory-footprint) for checking LRU cache memory footprint. |
| carbon.max.executor.lru.cache.size | -1 | Maximum memory **(in MB)** upto which the executor process can cache the data (BTree and reverse dictionary values). Default value of -1 means there is no memory limit for caching. Only integer values greater than 0 are accepted. **NOTE:** If this parameter is not configured, then the value of ***carbon.max.driver.lru.cache.size*** will be used. |
| max.query.execution.time | 60 | Maximum time allowed for one query to be executed. The value is in minutes. |
| carbon.enableMinMax | true | CarbonData maintains the metadata which enables to prune unnecessary files from being scanned as per the query conditions. To achieve pruning, Min,Max of each column is maintined.Based on the filter condition in the query, certain data can be skipped from scanning by matching the filter value against the min,max values of the column(s) present in that carbondata file. This pruning enhances query performance significantly. |
| carbon.dynamical.location.scheduler.timeout | 5 | CarbonData has its own scheduling algorithm to suggest to Spark on how many tasks needs to be launched and how much work each task need to do in a Spark cluster for any query on CarbonData. To determine the number of tasks that can be scheduled, knowing the count of active executors is necessary. When dynamic allocation is enabled on a YARN based spark cluster, executor processes are shutdown if no request is received for a particular amount of time. The executors are brought up when the requet is received again. This configuration specifies the maximum time (unit in seconds) the carbon scheduler can wait for executor to be active. Minimum value is 5 sec and maximum value is 15 sec.**NOTE:** Waiting for longer time leads to slow query response time.Moreover it might be possible that YARN is not able to start the executors and waiting is not beneficial. |
| carbon.scheduler.min.registered.resources.ratio | 0.8 | Specifies the minimum resource (executor) ratio needed for starting the block distribution. The default value is 0.8, which indicates 80% of the requested resource is allocated for starting block distribution. The minimum value is 0.1 min and the maximum value is 1.0. |
| carbon.detail.batch.size | 100 | The buffer size to store records, returned from the block scan. In limit scenario this parameter is very important. For example your query limit is 1000. But if we set this value to 3000 that means we get 3000 records from scan but spark will only take 1000 rows. So the 2000 remaining are useless. In one Finance test case after we set it to 100, in the limit 1000 scenario the performance increase about 2 times in comparison to if we set this value to 12000. **NOTE** The minimum batch size allowed is 100 and maximum batch size allowed by this property is 1000. |
| carbon.enable.vector.reader | true | Spark added vector processing to optimize cpu cache miss and there by increase the query performance. This configuration enables to fetch data as columnar batch of size 4\*1024 rows instead of fetching data row by row and provide it to spark so that there is improvement in select queries performance. |
| carbon.task.distribution | block | CarbonData has its own scheduling algorithm to suggest to Spark on how many tasks needs to be launched and how much work each task need to do in a Spark cluster for any query on CarbonData. Each of these task distribution suggestions has its own advantages and disadvantages. Based on the customer use case, appropriate task distribution can be configured.**block**: Setting this value will launch one task per block. This setting is suggested in case of concurrent queries and queries having big shuffling scenarios. **custom**: Setting this value will group the blocks and distribute it uniformly to the available resources in the cluster. This enhances the query performance but not suggested in case of concurrent queries and queries having big shuffling scenarios. **blocklet**: Setting this value will launch one task per blocklet. This setting is suggested in case of concurrent queries and queries having big shuffling scenarios. **merge\_small\_files**: Setting this value will merge all the small carbondata files upto a bigger size configured by ***spark.sql.files.maxPartitionBytes*** (128 MB is the default value,it is configurable) during querying. The small carbondata files are combined to a map task to reduce the number of read task. This enhances the performance. |
| carbon.custom.block.distribution | false | CarbonData has its own scheduling algorithm to suggest to Spark on how many tasks needs to be launched and how much work each task need to do in a Spark cluster for any query on CarbonData. When this configuration is true, CarbonData would distribute the available blocks to be scanned among the available number of cores. For Example:If there are 10 blocks to be scanned and only 3 tasks can be run(only 3 executor cores available in the cluster), CarbonData would combine blocks as 4,3,3 and give it to 3 tasks to run. **NOTE:** When this configuration is false, as per the ***carbon.task.distribution*** configuration, each block/blocklet would be given to each task. |
| enable.query.statistics | false | CarbonData has extensive logging which would be useful for debugging issues related to performance or hard to locate issues. This configuration when made ***true*** would log additional query statistics information to more accurately locate the issues being debugged. **NOTE:** Enabling this would log more debug information to log files, there by increasing the log files size significantly in short span of time. It is advised to configure the log files size, retention of log files parameters in log4j properties appropriately. Also extensive logging is an increased IO operation and hence over all query performance might get reduced. Therefore it is recommended to enable this configuration only for the duration of debugging. |
| enable.unsafe.in.query.processing | false | CarbonData supports unsafe operations of Java to avoid GC overhead for certain operations. This configuration enables to use unsafe functions in CarbonData while scanning the data during query. |
| carbon.max.driver.threads.for.block.pruning | 4 | Number of threads used for driver pruning when the carbon files are more than 100k Maximum memory. This configuration can used to set number of threads between 1 to 4. |
| carbon.heap.memory.pooling.threshold.bytes | 1048576 | CarbonData supports unsafe operations of Java to avoid GC overhead for certain operations. Using unsafe, memory can be allocated on Java Heap or off heap. This configuration controls the allocation mechanism on Java HEAP. If the heap memory allocations of the given size is greater or equal than this value,it should go through the pooling mechanism. But if set this size to -1, it should not go through the pooling mechanism. Default value is 1048576(1MB, the same as Spark). Value to be specified in bytes. |
| carbon.push.rowfilters.for.vector | false | When enabled complete row filters will be handled by carbon in case of vector. If it is disabled then only page level pruning will be done by carbon and row level filtering will be done by spark for vector. And also there are scan optimizations in carbon to avoid multiple data copies when this parameter is set to false. There is no change in flow for non-vector based queries. |
| carbon.query.prefetch.enable | true | By default this property is true, so prefetch is used in query to read next blocklet asynchronously in other thread while processing current blocklet in main thread. This can help to reduce CPU idle time. Setting this property false will disable this prefetch feature in query. |
| carbon.query.stage.input.enable | false | Stage input files are data files written by external applications (such as Flink), but have not been loaded into carbon table. Enabling this configuration makes query to include these files, thus makes query on latest data. However, since these files are not indexed, query maybe slower as full scan is required for these files. |
| carbon.driver.pruning.multi.thread.enable.files.count | 100000 | To prune in multi-thread when total number of segment files for a query increases beyond the configured value. |
| carbon.load.all.segment.indexes.to.cache | true | Setting this configuration to false, will prune and load only matched segment indexes to cache using segment metadata information such as columnid and it's minmax values, which decreases the usage of driver memory. |
| carbon.secondary.index.creation.threads | 1 | Specifies the number of threads to concurrently process segments during secondary index creation. This property helps fine tuning the system when there are a lot of segments in a table. The value range is 1 to 50. |
| carbon.si.lookup.partialstring | true | When true, it includes starts with, ends with and contains. When false, it includes only starts with secondary indexes. |

<a id="configuration-parameters--data-mutation-configuration"></a>

## Data Mutation Configuration

| Parameter | Default Value | Description |
| --- | --- | --- |
| carbon.update.persist.enable | true | Configuration to enable the dataset of RDD/dataframe to persist data. Enabling this will reduce the execution time of UPDATE operation. |
| carbon.update.storage.level | MEMORY\_AND\_DISK | Storage level to persist dataset of a RDD/dataframe. Applicable when ***carbon.update.persist.enable*** is **true**, if user's executor has less memory, set this parameter to 'MEMORY\_AND\_DISK\_SER' or other storage level to correspond to different environment. [See detail](http://spark.apache.org/docs/latest/rdd-programming-guide.html#rdd-persistence). |
| carbon.update.check.unique.value | true | By default this property is true, so update will validate key value mapping. This validation might have slight degrade in performance of update query. If user knows that key value mapping is correct, can disable this validation for better update performance by setting this property to false. |

<a id="configuration-parameters--dynamic-configuration-in-carbondata-using-set-reset"></a>

## Dynamic Configuration In CarbonData Using SET-RESET

**SET/RESET** commands are used to add, update, display, or reset the carbondata properties dynamically without restarting the driver.

**Syntax**

- **Add or Update :** This command adds or updates the value of parameter\_name.

```
SET parameter_name=parameter_value
```

- Display Property Value: This command displays the value of the specified parameter\_name.

```
SET parameter_name
```

- Display Session Parameters: This command displays all the supported session parameters.

```
SET
```

- Display Session Parameters along with usage details: This command displays all the supported session parameters along with their usage details.

```
SET -v
```

- Reset: This command clears all the session parameters.

```
RESET
```

**Parameter Description:**

| Parameter | Description |
| --- | --- |
| parameter\_name | Name of the property whose value needs to be dynamically added, updated, or displayed. |
| parameter\_value | New value of the parameter\_name to be set. |

Dynamically Configurable Properties of CarbonData

| Properties | Description |
| --- | --- |
| carbon.options.bad.records.logger.enable | To enable or disable a bad record logger. CarbonData can identify the records that are not conformant to schema and isolate them as bad records. Enabling this configuration will make CarbonData to log such bad records. **NOTE:** If the input data contains many bad records, logging them will slow down the overall data loading throughput. The data load operation status would depend on the configuration in ***carbon.bad.records.action***. |
| carbon.options.bad.records.action | This property has four types of bad record actions: FORCE, REDIRECT, IGNORE and FAIL. If set to FORCE then it auto-corrects the data by storing the bad records as NULL. If set to REDIRECT then bad records are written to the raw CSV instead of being loaded. If set to IGNORE then bad records are neither loaded nor written to the raw CSV. If set to FAIL then data loading fails if any bad records are found. |
| carbon.options.is.empty.data.bad.record | If false, then empty ("" or '' or ,,) data will not be considered as bad record and vice versa. |
| carbon.options.bad.record.path | Specifies the HDFS path where bad records needs to be stored. |
| carbon.custom.block.distribution | Specifies whether to use the Spark or Carbon block distribution feature. **NOTE:** Refer to [Query Configuration](#configuration-parameters--query-configuration)#carbon.custom.block.distribution for more details on CarbonData scheduler. |
| enable.unsafe.sort | Specifies whether to use unsafe sort during data loading. Unsafe sort reduces the garbage collection during data load operation, resulting in better performance. |
| carbon.options.date.format | Specifies the data format of the date columns in the data being loaded |
| carbon.options.timestamp.format | Specifies the timestamp format of the time stamp columns in the data being loaded |
| carbon.options.sort.scope | Specifies how the current data load should be sorted with. This sort parameter is at the table level. **NOTE:** Refer to [Data Loading Configuration](#configuration-parameters--data-loading-configuration)#carbon.sort.scope for detailed information. |
| carbon.table.load.sort.scope.<db\_name>.<table\_name> | Overrides the SORT\_SCOPE provided in CREATE TABLE. |
| carbon.options.global.sort.partitions | Specifies the number of partitions to be used during global sort. |
| carbon.options.serialization.null.format | Default Null value representation in the data being loaded. **NOTE:** Refer to [Data Loading Configuration](#configuration-parameters--data-loading-configuration)#carbon.options.serialization.null.format for detailed information. |
| carbon.number.of.cores.while.loading | Specifies number of cores to be used while loading data. **NOTE:** Refer to [Data Loading Configuration](#configuration-parameters--data-loading-configuration)#carbon.number.of.cores.while.loading for detailed information. |
| carbon.number.of.cores.while.compacting | Specifies number of cores to be used while compacting data. **NOTE:** Refer to [Data Loading Configuration](#configuration-parameters--data-loading-configuration)#carbon.number.of.cores.while.compacting for detailed information. |
| enable.offheap.sort | To enable off-heap memory usage. **NOTE:** Refer to [Data Loading Configuration](#configuration-parameters--data-loading-configuration)#enable.offheap.sort for detailed information. |
| carbon.blockletgroup.size.in.mb | Specifies the size of each blocklet group. **NOTE:** Refer to [Data Loading Configuration](#configuration-parameters--data-loading-configuration)#carbon.blockletgroup.size.in.mb for detailed information. |
| carbon.enable.auto.load.merge | To enable compaction along with data loading. **NOTE:** Refer to [Compaction Configuration](#configuration-parameters--compaction-configuration)#carbon.enable.auto.load.merge for detailed information. |
| carbon.major.compaction.size | To configure major compaction size. **NOTE:** Refer to [Compaction Configuration](#configuration-parameters--compaction-configuration)#carbon.major.compaction.size for detailed information. |
| carbon.compaction.level.threshold | To configure compaction threshold. **NOTE:** Refer to [Compaction Configuration](#configuration-parameters--compaction-configuration)#carbon.compaction.level.threshold for detailed information. |
| carbon.enable.vector.reader | To enable fetching data as columnar batch of size 4\*1024 rows instead of fetching a row at a time. **NOTE:** Refer to [Query Configuration](#configuration-parameters--query-configuration)#carbon.enable.vector.reader for detailed information. |
| enable.unsafe.in.query.processing | To enable use of unsafe functions while scanning the data during query. **NOTE:** Refer to [Query Configuration](#configuration-parameters--query-configuration)#enable.unsafe.in.query.processing for detailed information. |
| carbon.push.rowfilters.for.vector | To enable complete row filters handling by carbon in case of vector. **NOTE:** Refer to [Query Configuration](#configuration-parameters--query-configuration)#carbon.push.rowfilters.for.vector for detailed information. |
| carbon.query.stage.input.enable | To make query to include staged input files. **NOTE:** Refer to [Query Configuration](#configuration-parameters--query-configuration)#carbon.query.stage.input.enable for detailed information. |
| carbon.input.segments.<db\_name>.<table\_name> | To specify the segment ids to query from the table. segments ids are separated by comma. |
| carbon.index.visible.<db\_name>.<table\_name>.<index\_name> | To specify query on ***db\_name.table\_name*** to not use the index ***index\_name***. |
| carbon.load.indexes.parallel.<db\_name>.<table\_name> | To enable parallel index loading for a table. when db\_name.table\_name are not specified, i.e., when ***carbon.load.indexes.parallel.*** is set, it applies for all the tables of the session. |
| carbon.enable.index.server | To use index server for caching and pruning. This property can be used for a session or for a particular table with ***carbon.enable.index.server.<db\_name>.<table\_name>***. |

**Examples:**

- Add or Update:

```
SET enable.unsafe.sort =true
```

- Display Property Value:

```
SET enable.unsafe.sort
```

- Reset:

```
RESET
```

**System Response:**

- Success will be recorded in the driver log.
- Failure will be displayed in the UI.

[Top](#configuration-parameters--top)

---

<a id="index-developer-guide"></a>

<!-- source_url: https://carbondata.apache.org/index-developer-guide.html -->

<!-- page_index: 9 -->

<a id="index-developer-guide--index-developer-guide"></a>

# Index Developer Guide

<a id="index-developer-guide--introduction"></a>

### Introduction

Index is a data structure that can be used to accelerate certain query of the table. Different Index can be implemented by developers.
Currently, Carbondata supports three types of Indexes:

1. BloomFilter Index: A space-efficient probabilistic data structure that is used to test whether an element is a member of a set.
2. Lucene Index: High performance, full-featured text search engine.
3. Secondary Index: Sencondary index tables to hold blocklets are created as indexes and managed as child tables internally by Carbondata.

<a id="index-developer-guide--index-provider"></a>

### Index Provider

When user issues `CREATE INDEX index_name ON TABLE main AS 'provider'`, the corresponding IndexProvider implementation will be created and initialized.
Currently, the provider string can be:

1. class name IndexFactory implementation: Developer can implement new type of Index by extending IndexFactory

When user issues `DROP INDEX index_name ON TABLE main`, the corresponding IndexFactory class will be called.

Click for more details about [Index Management](#index-management--index-management) and supported [DSL](#index-management--overview).

[Top](#index-developer-guide--top)

---

<a id="supported-data-types-in-carbondata"></a>

<!-- source_url: https://carbondata.apache.org/supported-data-types-in-carbondata.html -->

<!-- page_index: 10 -->

<a id="supported-data-types-in-carbondata--data-types"></a>

# Data Types

<a id="supported-data-types-in-carbondata--carbondata-supports-the-following-data-types:"></a>

#### CarbonData supports the following data types:

- Numeric Types

  - SMALLINT
  - INT/INTEGER
  - BIGINT
  - DOUBLE
  - DECIMAL
  - FLOAT
  - BYTE
> [!NOTE]
> : Float and Bytes are only supported for SDK and FileFormat.

- Date/Time Types

  - TIMESTAMP
  - DATE
- String Types

  - STRING
  - CHAR
  - VARCHAR
> [!NOTE]
> : For string longer than 32000 characters, use `LONG_STRING_COLUMNS` in table property.
> Please refer to TBLProperties in [CreateTable](#ddl-of-carbondata--create-table) for more information.

- Complex Types

  - arrays: ARRAY`<data_type>`
  - structs: STRUCT`<col_name : data_type COMMENT col_comment, ...>`
  - maps: MAP`<primitive_type, data_type>`
> [!NOTE]
> : Only 2 level complex type schema is supported for now.

- Other Types

  - BOOLEAN
  - BINARY

[Top](#supported-data-types-in-carbondata--top)

---

<a id="index-management"></a>

<!-- source_url: https://carbondata.apache.org/index-management.html -->

<!-- page_index: 11 -->

<a id="index-management--carbondata-index-management"></a>

# CarbonData Index Management

- [Overview](#index-management--overview)
- [Index Management](#index-management--index-management)
- [Automatic Refresh](#index-management--automatic-refresh)
- [Manual Refresh](#index-management--manual-refresh)
- [Index Related Commands](#index-management--index-related-commands)
  - [Explain](#index-management--explain)
  - [Show Index](#index-management--show-index)

<a id="index-management--overview"></a>

## Overview

Index can be created using following DDL

```
CREATE INDEX [IF NOT EXISTS] index_name
ON TABLE [db_name.]table_name (column_name, ...)
AS carbondata/bloomfilter/lucene
[WITH DEFERRED REFRESH]
[PROPERTIES ('key'='value')]
```

Index can be refreshed using following DDL

```
REFRESH INDEX index_name ON [TABLE] [db_name.]table_name
```

Currently, there are 3 Index implementations in CarbonData.

| Index Provider | Description | Management |
| --- | --- | --- |
| secondary-index | secondary-index tables to hold blocklets as indexes and managed as child tables | Automatic |
| lucene | lucene indexing for text column | Automatic |
| bloomfilter | bloom filter for high cardinality column, geospatial column | Automatic |

<a id="index-management--index-management"></a>

## Index Management

There are two kinds of management semantic for Index.

1. Automatic Refresh
2. Manual Refresh

<a id="index-management--automatic-refresh"></a>

### Automatic Refresh

When a user creates an index on the main table without using `WITH DEFERRED REFRESH` syntax, the index will be managed by the system automatically.
For every data load to the main table, the system will immediately trigger a load to the index automatically. These two data loading (to main table and index) is executed in a transactional manner, meaning that it will be either both success or neither success.

The data loading to index is incremental based on Segment concept, avoiding an expensive total refresh.

If a user performs the following command on the main table, the system will return failure. (reject the operation)

1. Data management command: `UPDATE/DELETE/DELETE SEGMENT`.
2. Schema management command: `ALTER TABLE DROP COLUMN`, `ALTER TABLE CHANGE DATATYPE`,
   `ALTER TABLE RENAME`. Note that adding a new column is supported, and for dropping columns and
   change datatype command, CarbonData will check whether it will impact the index table, if
   not, the operation is allowed, otherwise operation will be rejected by throwing an exception.
3. Partition management command: `ALTER TABLE ADD/DROP PARTITION`.

If a user does want to perform above operations on the main table, the user can first drop the index, perform the operation, and re-create the index again.

If a user drops the main table, the index will be dropped immediately too.

We do recommend you to use this management for indexing.

<a id="index-management--manual-refresh"></a>

### Manual Refresh

When a user creates an index on the main table using `WITH DEFERRED REFRESH` syntax, the index will be created with status *disabled* and query will NOT use this index until the user issues `REFRESH INDEX` command to build the index. For every `REFRESH INDEX` command, the system will trigger a full refresh of the index. Once the refresh operation is finished, system will change index status to *enabled*, so that it can be used in query rewrite.

For every new data loading, data update, delete, the related index will be made *disabled*, which means that the following queries will not benefit from the index before it becomes *enabled* again.

If the main table is dropped by the user, the related index will be dropped immediately.

> [!NOTE]
> :

- If you are creating an index on an external table, you need to do manual management of the index.
- Currently, all types of indexes supported by carbon will be automatically refreshed by default, which means its data will get refreshed immediately after the index is created or the main table is loaded. Manual refresh on these indexes is not supported.

<a id="index-management--index-related-commands"></a>

## Index Related Commands

<a id="index-management--explain"></a>

### Explain

How can users know whether an index is used in the query?

User can set `enable.query.statistics = true` and use `EXPLAIN` command to know, it will print out something like

```
== CarbonData Profiler ==
Table Scan on default.main
+- total: 1 blocks, 1 blocklets
+- filter:
+- pruned by CG Index
   - name: index1
   - provider: lucene
   - skipped: 0 blocks, 0 blocklets
```

<a id="index-management--show-index"></a>

### Show Index

There is a SHOW INDEXES command, when this is issued, the system will read all indexes from the carbon table and print all information on screen. The current information includes:

- Name
- Provider like lucene
- Indexed Columns
- Properties
- Status (ENABLED/DISABLED)
- Sync Info - which displays Last segment Id of main table synced with index table and its load
  end time

[Top](#index-management--top)

---

<a id="bloomfilter-index-guide"></a>

<!-- source_url: https://carbondata.apache.org/bloomfilter-index-guide.html -->

<!-- page_index: 12 -->

<a id="bloomfilter-index-guide--carbondata-bloomfilter-index"></a>

# CarbonData BloomFilter Index

- [Index Management](#bloomfilter-index-guide--index-management)
- [BloomFilter Index Introduction](#bloomfilter-index-guide--bloomfilter-index-introduction)
- [Loading Data](#bloomfilter-index-guide--loading-data)
- [Querying Data](#bloomfilter-index-guide--querying-data)
- [Data Management](#bloomfilter-index-guide--data-management-with-bloomfilter-index)
- [Useful Tips](#bloomfilter-index-guide--useful-tips)

<a id="bloomfilter-index-guide--index-management"></a>

#### Index Management

Creating BloomFilter Index

```
CREATE INDEX [IF NOT EXISTS] index_name
ON TABLE main_table (city,name)
AS 'bloomfilter'
PROPERTIES ('BLOOM_SIZE'='640000', 'BLOOM_FPP'='0.00001')
```

Dropping Specified Index

```
DROP INDEX [IF EXISTS] index_name
ON [TABLE] main_table
```

Showing all Indexes on this table

```
SHOW INDEXES
ON [TABLE] main_table
```

> NOTE: Keywords given inside `[]` is optional.

Disable Index

> The index by default is enabled. To support tuning on query, we can disable a specific index during query to observe whether we can gain performance enhancement from it. This is effective only for current session.

```
// disable the index
SET carbon.index.visible.dbName.tableName.indexName = false
// enable the index
SET carbon.index.visible.dbName.tableName.indexName = true
```

<a id="bloomfilter-index-guide--bloomfilter-index-introduction"></a>

## BloomFilter Index Introduction

A Bloom filter is a space-efficient probabilistic data structure that is used to test whether an element is a member of a set.
Carbondata introduced BloomFilter as an index to enhance the performance of querying with precise value.
It is well suitable for queries that do precise matching on high cardinality columns(such as Name/ID).
Internally, CarbonData maintains a BloomFilter per blocklet for each index column to indicate that whether a value of the column is in this blocklet.
Just like the other indexes, BloomFilter index is managed along with main tables by CarbonData.
User can create BloomFilter index on specified columns with specified BloomFilter configurations such as size and probability.

For instance, main table called **index\_test** which is defined as:

```
CREATE TABLE index_test (
  id string,
  name string,
  age int,
  city string,
  country string)
STORED AS carbondata
TBLPROPERTIES('SORT_COLUMNS'='id')
```

In the above example, `id` and `name` are high cardinality columns
and we always query on `id` and `name` with precise value.
since `id` is in the sort\_columns and it is ordered, query on it will be fast because CarbonData can skip all the irrelative blocklets.
But queries on `name` may be bad since the blocklet minmax may not help, because in each blocklet the range of the value of `name` may be the same -- all from A\* to z\*.
In this case, user can create a BloomFilter Index on column `name`.
Moreover, user can also create a BloomFilter Index on the sort\_columns.
This is useful if user has too many segments and the range of the value of sort\_columns are almost the same.

User can create BloomFilter Index using the Create Index DDL:

```
CREATE INDEX dm
ON TABLE index_test (name,id)
AS 'bloomfilter'
PROPERTIES ('BLOOM_SIZE'='640000', 'BLOOM_FPP'='0.00001', 'BLOOM_COMPRESS'='true')
```

Here, (name,id) are INDEX\_COLUMNS. Carbondata will generate BloomFilter index on these columns. Queries on these columns are usually like `'COL = VAL'`.

**Properties for BloomFilter Index**

| Property | Is Required | Default Value | Description |
| --- | --- | --- | --- |
| BLOOM\_SIZE | NO | 640000 | This value is internally used by BloomFilter as the number of expected insertions, it will affect the size of BloomFilter index. Since each blocklet has a BloomFilter here, so the default value is the approximate distinct index values in a blocklet assuming that each blocklet contains 20 pages and each page contains 32000 records. The value should be an integer. |
| BLOOM\_FPP | NO | 0.00001 | This value is internally used by BloomFilter as the False-Positive Probability, it will affect the size of bloomfilter index as well as the number of hash functions for the BloomFilter. The value should be in the range (0, 1). In one test scenario, a 96GB TPCH customer table with bloom\_size=320000 and bloom\_fpp=0.00001 will result in 18 false positive samples. |
| BLOOM\_COMPRESS | NO | true | Whether to compress the BloomFilter index files. |

<a id="bloomfilter-index-guide--loading-data"></a>

## Loading Data

When loading data to main table, BloomFilter files will be generated for all the
index\_columns provided in the CREATE statement which contains the blockletId and a BloomFilter for each index column.
These index files will be written inside a folder named with Index name
inside each segment folders.

<a id="bloomfilter-index-guide--querying-data"></a>

## Querying Data

User can verify whether a query can leverage BloomFilter Index by executing `EXPLAIN` command, which will show the transformed logical plan, and thus user can check whether the BloomFilter Index can skip blocklets during the scan.
If the Index does not prune blocklets well, you can try to increase the value of property `BLOOM_SIZE` and decrease the value of property `BLOOM_FPP`.

<a id="bloomfilter-index-guide--data-management-with-bloomfilter-index"></a>

## Data Management With BloomFilter Index

Data management with BloomFilter Index has no difference with that on Lucene Index.
You can refer to the corresponding section in [CarbonData Lucene Index](#lucene-index-guide)

<a id="bloomfilter-index-guide--useful-tips"></a>

## Useful Tips

- BloomFilter Index is suggested to be created on the high cardinality columns.
  Query conditions on these columns are always simple `equal` or `in`,
  such as 'col1=XX', 'col1 in (XX, YY)'.
- We can create multiple BloomFilter Indexes on one table,
  but we do recommend you to create one BloomFilter Index that contains multiple index columns,
  because the data loading and query performance will be better.
- `BLOOM_FPP` is only the expected number from user, the actual FPP may be worse.
  If the BloomFilter Index does not work well,
  you can try to increase `BLOOM_SIZE` and decrease `BLOOM_FPP` at the same time.
  Notice that bigger `BLOOM_SIZE` will increase the size of index file
  and smaller `BLOOM_FPP` will increase runtime calculation while performing query.
- '0' skipped blocklets of BloomFilter Index in explain output indicates that
  BloomFilter Index does not prune better than Main Index.
  (For example since the data is not ordered, a specific value may be contained in many blocklets. In this case, bloom may not work better than Main Index.)
  If this occurs very often, it means that current BloomFilter is useless. You can disable or drop it.
  Sometimes we cannot see any pruning result about BloomFilter Index in the explain output,
  this indicates that the previous Index has pruned all the blocklets and there is no need to continue pruning.
- In some scenarios, the BloomFilter Index may not enhance the query performance significantly
  but if it can reduce the number of spark task,
  there is still a chance that BloomFilter Index can enhance the performance for concurrent query.
- Note that BloomFilter Index will decrease the data loading performance and may cause slight storage expansion (for index file).

[Top](#bloomfilter-index-guide--top)

---

<a id="lucene-index-guide"></a>

<!-- source_url: https://carbondata.apache.org/lucene-index-guide.html -->

<!-- page_index: 13 -->

<a id="lucene-index-guide--carbondata-lucene-index-alpha-feature"></a>

# CarbonData Lucene Index (Alpha Feature)

- [Index Management](#lucene-index-guide--index-management)
- [Lucene Index](#lucene-index-guide--lucene-index-introduction)
- [Loading Data](#lucene-index-guide--loading-data)
- [Querying Data](#lucene-index-guide--querying-data)
- [Data Management](#lucene-index-guide--data-management-with-lucene-index)

<a id="lucene-index-guide--index-management"></a>

#### Index Management

Lucene Index can be created using following DDL

```
CREATE INDEX [IF NOT EXISTS] index_name
ON TABLE main_table (index_columns)
AS 'lucene'
[PROPERTIES ('key'='value')]
```

index\_columns is the list of string columns on which lucene creates indexes.

Index can be dropped using following DDL:

```
DROP INDEX [IF EXISTS] index_name
ON [TABLE] main_table
```

To show all Indexes created, use:

```
SHOW INDEXES
ON [TABLE] main_table
```

It will show all Indexes created on the main table.

> NOTE: Keywords given inside `[]` is optional.

<a id="lucene-index-guide--lucene-index-introduction"></a>

## Lucene Index Introduction

Lucene is a high performance, full featured text search engine. Lucene is integrated to carbon as
an index and managed along with main tables by CarbonData. User can create lucene index
to improve query performance on string columns which has content of more length. So, user can
search tokenized word or pattern of it using lucene query on text content.

For instance, main table called **index\_test** which is defined as:

```
CREATE TABLE index_test (
  name string,
  age int,
  city string,
  country string)
STORED AS carbondata
```

User can create Lucene index using the Create Index DDL:

```
CREATE INDEX dm
ON TABLE index_test (name,country)
AS 'lucene'
```

**Properties**

1. FLUSH\_CACHE: size of the cache to maintain in Lucene writer, if specified then it tries to
   aggregate the unique data till the cache limit and flush to Lucene. It is best suitable for low
   cardinality dimensions.
2. SPLIT\_BLOCKLET: when made as true then store the data in blocklet wise in lucene , it means new
   folder will be created for each blocklet, thus, it eliminates storing blockletid in lucene and
   also it makes lucene small chunks of data.

<a id="lucene-index-guide--loading-data"></a>

## Loading data

When loading data to main table, lucene index files will be generated for all the
index\_columns(String Columns) given in CREATE statement which contains information about the data
location of index\_columns. These index files will be written inside a folder named with index name
inside each segment folder.

A system level configuration `carbon.lucene.compression.mode` can be added for best compression of
lucene index files. The default value is speed, where the index writing speed will be more. If the
value is compression, the index file size will be compressed.

<a id="lucene-index-guide--querying-data"></a>

## Querying data

As a technique for query acceleration, Lucene indexes cannot be queried directly.
Queries are to be made on the main table. When a query with TEXT\_MATCH('name:c10') or
TEXT\_MATCH\_WITH\_LIMIT('name:n10',10)[the second parameter represents the number of result to be
returned, if user does not specify this value, all results will be returned without any limit] is
fired, two jobs will be launched. The first job writes the temporary files in folder created at table level
which contains lucene's search results and these files will be read in second job to give faster
results. These temporary files will be cleared once the query finishes.

User can verify whether a query can leverage Lucene index or not by executing the `EXPLAIN`
command, which will show the transformed logical plan, and thus user can check whether TEXT\_MATCH()
filter is applied on query or not.

**Note:**

1. The filter columns in TEXT\_MATCH or TEXT\_MATCH\_WITH\_LIMIT must be always in lowercase and
   filter conditions like 'AND','OR' must be in upper case.

   Ex:


```
select * from index_test where TEXT_MATCH('name:*10 AND name:*n*')
```

2. Query supports only one TEXT\_MATCH udf for filter condition and not multiple udfs.

   The following query is supported:


```
select * from index_test where TEXT_MATCH('name:*10 AND name:*n*')
```

   The following query is not supported:


```
select * from index_test where TEXT_MATCH('name:*10) AND TEXT_MATCH(name:*n*')
```

Below `like` queries can be converted to text\_match queries as following:

```
select * from index_test where name='n10'

select * from index_test where name like 'n1%'

select * from index_test where name like '%10'

select * from index_test where name like '%n%'

select * from index_test where name like '%10' and name not like '%n%'
```

Lucene TEXT\_MATCH Queries:

```
select * from index_test where TEXT_MATCH('name:n10')

select * from index_test where TEXT_MATCH('name:n1*')

select * from index_test where TEXT_MATCH('name:*10')

select * from index_test where TEXT_MATCH('name:*n*')

select * from index_test where TEXT_MATCH('name:*10 -name:*n*')
```

**Note:** For lucene queries and syntax, refer to [lucene-syntax](http://www.lucenetutorial.com/lucene-query-syntax.html)

<a id="lucene-index-guide--data-management-with-lucene-index"></a>

## Data Management with lucene index

Once there is a lucene index created on the main table, following command on the main
table is not supported:

1. Data management command: `UPDATE/DELETE`.
2. Schema management command: `ALTER TABLE DROP COLUMN`, `ALTER TABLE CHANGE DATATYPE`,
   `ALTER TABLE RENAME`.

> [!NOTE]
> : Adding a new column is supported, and for dropping columns and change datatype
> command, CarbonData will check whether it will impact the lucene index, if not, the operation
> is allowed, otherwise operation will be rejected by throwing exception.

3. Partition management command: `ALTER TABLE ADD/DROP PARTITION`.

However, there is still way to support these operations on main table, in current CarbonData
release, user can do as following:

1. Remove the lucene index by `DROP INDEX` command.
2. Carry out the data management operation on main table.
3. Create the lucene index again by `CREATE INDEX` command.
   Basically, user can manually trigger the operation by refreshing the index.

[Top](#lucene-index-guide--top)

---

<a id="secondary-index-guide"></a>

<!-- source_url: https://carbondata.apache.org/secondary-index-guide.html -->

<!-- page_index: 14 -->

<a id="secondary-index-guide--carbondata-secondary-index"></a>

# CarbonData Secondary Index

- [Quick Example](#secondary-index-guide--quick-example)
- [Secondary Index Table](#secondary-index-guide--secondary-index-introduction)
- [Loading Data](#secondary-index-guide--loading-data)
- [Querying Data](#secondary-index-guide--querying-data)
- [Compaction](#secondary-index-guide--compacting-si-table)
- [DDLs on Secondary Index](#secondary-index-guide--ddls-on-secondary-index)

<a id="secondary-index-guide--quick-example"></a>

## Quick example

Start spark-sql in terminal and run the following queries,

```
CREATE TABLE maintable(a int, b string, c string) stored as carbondata;
insert into maintable select 1, 'ab', 'cd';
CREATE index index1 on table maintable(c) AS 'carbondata';
SELECT a from maintable where c = 'cd';
// NOTE: run explain query and check if query hits the SI table from the plan
EXPLAIN SELECT a from maintable where c = 'cd';
```

<a id="secondary-index-guide--secondary-index-introduction"></a>

## Secondary Index Introduction

Secondary index tables are created as indexes and managed as child tables internally by
Carbondata. Users can create a secondary index based on the column position in the main table(Recommended
for right columns) and the queries should have filter on that column to improve the filter query
performance.

Data refresh to the secondary index is always automatic. Once SI table is created, Carbondata's
CarbonOptimizer with the help of `CarbonSITransformationRule`, transforms the query plan to hit the
SI table based on the filter condition or set of filter conditions present in the query.
So the first level of pruning will be done on the SI table as it stores blocklets and main table/parent
table pruning will be based on the SI output, which helps in giving the faster query results with
better pruning.

Secondary Index table can be created with the below syntax

```
CREATE INDEX [IF NOT EXISTS] index_name
ON TABLE maintable(index_column)
AS
'carbondata'
[PROPERTIES('table_blocksize'='1')]
```

> NOTE: Keywords given inside `[]` is optional.

For instance, main table called **sales** which is defined as

```
CREATE TABLE sales (
  order_time timestamp,
  user_id string,
  sex string,
  country string,
  quantity int,
  price bigint)
STORED AS carbondata
```

User can create SI table using the Create Index DDL

```
CREATE INDEX index_sales
ON TABLE sales(user_id)
AS
'carbondata'
PROPERTIES('table_blocksize'='1')
```

<a id="secondary-index-guide--how-si-tables-are-selected"></a>

#### How SI tables are selected

When a user executes a filter query, during the query planning phase, CarbonData with the help of
`CarbonSITransformationRule`, checks if there are any index tables present on the filter column of
query. If there are any, then the filter query plan will be transformed in such a way that execution will
first hit the corresponding SI table and give input to the main table for further pruning.

For the main table **sales** and SI table **index\_sales** created above, following queries

```
SELECT country, sex from sales where user_id = 'xxx'

SELECT country, sex from sales where user_id = 'xxx' and country = 'INDIA'
```

will be transformed by CarbonData's `CarbonSITransformationRule` to query against SI table
**index\_sales** first which will be input to the main table **sales**

<a id="secondary-index-guide--loading-data"></a>

## Loading data

<a id="secondary-index-guide--loading-data-to-secondary-index-table-s-."></a>

### Loading data to Secondary Index table(s).

*case1:* When the SI table is created and the main table does not have any data. In this case every
consecutive load to the main table, will load data to the SI table once the main table data load is finished.

*case2:* When the SI table is created and the main table already contains some data, then SI creation will
also load data to the SI table with the same number of segments as the main table. Thereafter, consecutive load to
the main table will also load data to the SI table.

> [!NOTE]
> :

- In case of data load failure to the SI table, then we make the SI table disable by setting a hive serde
  property. The subsequent main table load will load the old failed loads along with current load and
  makes the SI table enable and available for query.

<a id="secondary-index-guide--querying-data"></a>

## Querying data

Direct query can be made on SI tables to check the data present in position reference columns.
When a filter query is fired, and if the filter column is a secondary index column, then plan is
transformed accordingly to hit the SI table first to make better pruning with the main table and in turn
helps for faster query results.

Users can verify whether a query can leverage the SI table or not by executing the `EXPLAIN`
command, which will show the transformed logical plan, and thus users can check whether the SI table
is selected.

<a id="secondary-index-guide--compacting-si-table"></a>

## Compacting SI table

<a id="secondary-index-guide--compacting-si-table-table-through-main-table-compaction"></a>

### Compacting SI table table through Main Table compaction

Running Compaction command (`ALTER TABLE COMPACT`)[COMPACTION TYPE-> MINOR/MAJOR] on main table will
automatically delete all the old segments of SI and creates a new segment with same name as main
table compacted segment and loads data to it.

<a id="secondary-index-guide--compacting-si-table-s-individual-segment-s-through-refresh-index-command"></a>

### Compacting SI table's individual segment(s) through REFRESH INDEX command

Where there are so many small files present in the SI table, then we can use the REFRESH INDEX command to
compact the files within an SI segment to avoid many small files.

```
REFRESH INDEX sales_index ON TABLE sales
```

This command merges data files in each segment of the SI table.

```
REFRESH INDEX sales_index ON TABLE sales WHERE SEGMENT.ID IN(1)
```

This command merges data files within a specified segment of the SI table.

<a id="secondary-index-guide--how-to-skip-secondary-index"></a>

## How to skip Secondary Index?

When Secondary indexes are created on a table(s), data fetching happens from secondary
indexes created on the main tables for better performance. But sometimes, data fetching from the
secondary index might degrade query performance in cases where the data is sparse and most of the
blocklets need to be scanned. So to avoid such secondary indexes, we use NI as a function on filters
within WHERE clause.

```
SELECT country, sex from sales where NI(user_id = 'xxx')
```

The above query ignores column `user_id` from the secondary index and fetches data from the main table.

<a id="secondary-index-guide--ddls-on-secondary-index"></a>

## DDLs on Secondary Index

<a id="secondary-index-guide--show-index-command"></a>

### Show index Command

This command is used to get information about all the secondary indexes on a table.

Syntax

```
SHOW INDEXES ON [TABLE] [db_name.]table_name
```

<a id="secondary-index-guide--drop-index-command"></a>

### Drop index Command

This command is used to drop an existing secondary index on a table

Syntax

```
DROP INDEX [IF EXISTS] index_name ON [TABLE] [db_name.]table_name
```

<a id="secondary-index-guide--register-index-command"></a>

### Register index Command

This command registers the secondary index with the main table in case of compatibility scenarios
where we have old stores.

Syntax

```
REGISTER INDEX TABLE index_name ON [TABLE] [db_name.]table_name
```

[Top](#secondary-index-guide--top)

---

<a id="spatial-index-guide"></a>

<!-- source_url: https://carbondata.apache.org/spatial-index-guide.html -->

<!-- page_index: 15 -->

<a id="spatial-index-guide--what-is-spatial-index"></a>

# What is spatial index

[A spatial index](https://gistbok.ucgis.org/topic-keywords/indexing) is a data structure that allows for accessing a spatial object efficiently. It is a common technique used by spatial databases. Without indexing, any search for a feature would require a "sequential scan" of every record in the database, resulting in much longer processing time. In a spatial index construction process, the minimum bounding rectangle serves as an object approximation. Various types of spatial indices across commercial and open-source databases yield measurable performance differences. Spatial indexing techniques are playing a central role in time-critical applications and the manipulation of spatial big data.

<a id="spatial-index-guide--how-does-carbondata-implement-spatial-index"></a>

# How does CarbonData implement spatial index

There are many open source implementations for spatial indexing and to process spatial queries. CarbonData implements a different way of spatial index. Its core idea is to use the raster data. Raster is made up of matrix of cells organized into rows and columns(called a grid). Each cell represents a coordinate. The index for the coordinate is generated using longitude and latitude, like the [Z order curve](https://en.wikipedia.org/wiki/Z-order_curve).

CarbonData rasterize the user data during data load into segments. A set of latitude and longitude represents a grid range. The size of the grid can be configured. Hence, the coordinates loaded are often discrete and not continuous.

Below figure shows the relationship between the grid and the points residing in it. Black point represents the center point of the grid, and the red points are the coordinates at the arbitrary positions inside the grid. The red points can be replaced by the center point of the grid to indicate that the points lies within the grid. During data load, CarbonData generates an index for the coordinate according to row and column of the grid(in the raster) where that coordinate lies. These indices are the same as Z order. For the detailed conversion algorithm, please refer to the design documents of spatial index.

[![File Directory Structure](https://github.com/apache/carbondata/blob/master/docs/images/spatial-index-1.png?raw=true)](assets/files/errorpage_d68d20be1f65d644.html)

Carbon supports Polygon User Defined Function(UDF) as filter condition in the query to return all the data points lying within it. Polygon UDF takes multiple points(i.e., pair of longitude and latitude) separated by a comma. Longitude and latitude in the pair are separated by a space. The first and last points in the polygon must be same to form a closed loop. CarbonData builds a quad tree using this polygon and spatial region information passed while creating a table. The nodes in the quad tree are composed of indices generated by the row and column information projected in the polygon area. When the grid center point lies within the polygon area, the grid is considered as selected. In the following figure, user selects a quadrilateral shaped polygon. The grid at the center of the region is chosen to build a quad tree. Once tree is build, all the leafs are scanned to get the list of range of indices(with each range consisting of minimum index and maximum index in the range). All the indices starting from minimum to maximum in each range forms the result.
The main reasons for faster query response are as follows :

- Data is sorted based on the index values.
- Polygon UDF filter is pushed down from engine to the carbon layer such that CarbonData scans only matched blocklets avoiding full scan.

[![File Directory Structure](https://github.com/apache/carbondata/blob/master/docs/images/spatial-index-2.png?raw=true)](assets/files/errorpage_d68d20be1f65d644.html)

<a id="spatial-index-guide--installation-and-deployment"></a>

# Installation and Deployment

Geo is a separate module in the Project. It can be included or excluded from the project build based on the requirement.

<a id="spatial-index-guide--basic-command"></a>

## Basic Command

<a id="spatial-index-guide--create-table"></a>

### Create Table

Create table with spatial index table properties

```
create table source_index(id BIGINT, latitude long, longitude long) stored by 'carbondata' TBLPROPERTIES (
'SPATIAL_INDEX'='mygeohash',
'SPATIAL_INDEX.mygeohash.type'='geohash',
'SPATIAL_INDEX.mygeohash.sourcecolumns'='longitude, latitude',
'SPATIAL_INDEX.mygeohash.originLatitude'='19.832277',
'SPATIAL_INDEX.mygeohash.gridSize'='50',
'SPATIAL_INDEX.mygeohash.minLongitude'='1.811865',
'SPATIAL_INDEX.mygeohash.maxLongitude'='2.782233',
'SPATIAL_INDEX.mygeohash.minLatitude'='19.832277',
'SPATIAL_INDEX.mygeohash.maxLatitude'='20.225281',
'SPATIAL_INDEX.mygeohash.conversionRatio'='1000000');
```

Note: `mygeohash` in the above example represent the index name.

<a id="spatial-index-guide--list-of-spatial-index-table-properties"></a>

#### List of spatial index table properties

| Name | Description |
| --- | --- |
| SPATIAL\_INDEX | Used to configure Spatial Index name. This name is appended to `SPATIAL_INDEX` in the subsequent sub-property configurations. `xxx` in the below sub-properties refer to index name. |
| SPATIAL\_INDEX.xxx.type | Type of algorithm for processing spatial data. Currently, supports only 'geohash'. |
| SPATIAL\_INDEX.xxx.sourcecolumns | longitude and latitude column names as in the table. These columns are used to generate index value for each row. |
| SPATIAL\_INDEX.xxx.gridSize | Grid size of raster data in metres. Currently, spatial index supports raster data. |
| SPATIAL\_INDEX.xxx.minLongitude | Minimum longitude of the gridded rectangular area. |
| SPATIAL\_INDEX.xxx.maxLongitude | Maximum longitude of the gridded rectangular area. |
| SPATIAL\_INDEX.xxx.minLatitude | Minimum latitude of the gridded rectangular area. |
| SPATIAL\_INDEX.xxx.maxLatitude | Maximum latitude of the gridded rectangular area. |
| SPATIAL\_INDEX.xxx.conversionRatio | Conversion factor. It allows user to translate longitude and latitude to long. For example, if the data to load is longitude = 13.123456, latitude = 101.12356. User can configure conversion ratio sub-property value as 1000000, and change data to load as longitude = 13123456 and latitude = 10112356. Operations on long is much faster compared to floating-point numbers. |
| SPATIAL\_INDEX.xxx.class | Optional user custom implementation class. Value is fully qualified class name. |

<a id="spatial-index-guide--select-query"></a>

### Select Query

Query with Polygon UDF predicate

```
select * from source_index where IN_POLYGON('16.321011 4.123503,16.137676 5.947911,16.560993 5.935276,16.321011 4.123503')
```

<a id="spatial-index-guide--reference"></a>

## Reference

```
[1] https://issues.apache.org/jira/browse/CARBONDATA-3548
[2] https://gistbok.ucgis.org/topic-keywords/indexing
[3] https://en.wikipedia.org/wiki/Z-order_curve
```

[Top](#spatial-index-guide--top)

---

<a id="mv-guide"></a>

<!-- source_url: https://carbondata.apache.org/mv-guide.html -->

<!-- page_index: 16 -->

<a id="mv-guide--carbondata-materialized-view"></a>

# CarbonData Materialized View

- [Quick Example](#mv-guide--quick-example)
- [Introduction](#mv-guide--introduction)
- [Loading Data](#mv-guide--loading-data)
- [Querying Data](#mv-guide--querying-data)
- [Compaction](#mv-guide--compacting)
- [Data Management](#mv-guide--data-management)
- [Time Series Support](#mv-guide--time-series-support)
- [Time Series RollUp Support](#mv-guide--time-series-rollup-support)

<a id="mv-guide--quick-example"></a>

## Quick example

Start spark-sql in terminal and run the following queries,

```
  CREATE TABLE maintable(a int, b string, c int) stored as carbondata;
  INSERT INTO maintable SELECT 1, 'ab', 2;
  CREATE MATERIALIZED VIEW view1 AS SELECT a, sum(b) FROM maintable GROUP BY a;
  SELECT a, sum(b) FROM maintable GROUP BY a;
  // NOTE: run explain query and check if query hits the mv table from the plan
  EXPLAIN SELECT a, sum(b) FROM maintable GROUP BY a;
```

<a id="mv-guide--introduction"></a>

## Introduction

Materialized views are created as tables from queries. Users can create limitless materialized views
to improve query performance provided the storage requirements and loading time is acceptable.

Materialized view can be refreshed on commit or on manual. Once materialized views are created, CarbonData's `MVRewriteRule` helps to select the most efficient materialized view based on
the user query and rewrite the SQL to select the data from materialized view instead of
fact tables. Since the data size of materialized view is smaller and data is pre-processed, user queries are much faster.

For instance, fact table called **sales** which is defined as.

```
  CREATE TABLE sales (
    order_time timestamp,
    user_id string,
    sex string,
    country string,
    quantity int,
    price bigint)
  STORED AS carbondata
```

Users can create a materialized view using the CREATE MATERIALIZED VIEW statement.

```
  CREATE MATERIALIZED VIEW agg_sales
  PROPERTIES('TABLE_BLOCKSIZE'='256 MB','LOCAL_DICTIONARY_ENABLE'='false')
  AS
    SELECT country, sex, sum(quantity), avg(price)
    FROM sales
    GROUP BY country, sex
```

> [!NOTE]
> :

- Group by and Order by columns has to be provided in the projection list while creating a materialized view.
- If only single fact table is involved in materialized view creation, then TableProperties of
  fact table (if not present in a aggregate function like sum(col)) listed below will be
  inherited to materialized view.
  1. SORT\_COLUMNS
  2. SORT\_SCOPE
  3. TABLE\_BLOCKSIZE
  4. FLAT\_FOLDER
  5. LONG\_STRING\_COLUMNS
  6. LOCAL\_DICTIONARY\_ENABLE
  7. LOCAL\_DICTIONARY\_THRESHOLD
  8. LOCAL\_DICTIONARY\_EXCLUDE
  9. INVERTED\_INDEX
  10. NO\_INVERTED\_INDEX
  11. COLUMN\_COMPRESSOR
- Creating materialized view with select query containing only project of all columns of fact
  table is unsupported.
  **Example:**
  If table 'x' contains columns 'a,b,c', then creating MV with below queries is not supported.
  1. `SELECT a,b,c FROM x`
  2. `SELECT * FROM x`
- TableProperties can be provided in Properties excluding LOCAL\_DICTIONARY\_INCLUDE,
  LOCAL\_DICTIONARY\_EXCLUDE, INVERTED\_INDEX, NO\_INVERTED\_INDEX, SORT\_COLUMNS, LONG\_STRING\_COLUMNS,
  RANGE\_COLUMN & COLUMN\_META\_CACHE.
- TableProperty given in Properties will be considered for materialized view creation, even though
  if same property is inherited from fact table, which allows user to provide different table
  properties for materialized view.
- Materialized view creation with limit or union all CTAS queries is unsupported.
- Materialized view does not support streaming.

<a id="mv-guide--how-materialized-views-are-selected"></a>

#### How materialized views are selected

When a user query is submitted, during the query planning phase, CarbonData will collect modular plan
candidates and process the ModularPlan based on registered summary data sets. Then, a materialized view for this query will be selected among the candidates.

For the fact table **sales** and materialized view **agg\_sales** created above, following queries

```
  SELECT country, sex, sum(quantity), avg(price) FROM sales GROUP BY country, sex
  SELECT sex, sum(quantity) FROM sales GROUP BY sex
  SELECT avg(price), country FROM sales GROUP BY country
```

will be transformed by CarbonData's query planner to query against materialized view **agg\_sales**
instead of the fact table **sales**.

However, for following queries

```
  SELECT user_id, country, sex, sum(quantity), avg(price) FROM sales GROUP BY user_id, country, sex
  SELECT sex, avg(quantity) FROM sales GROUP BY sex
  SELECT country, max(price) FROM sales GROUP BY country
```

will query against fact table **sales** only, because it does not satisfy materialized view
selection logic.

<a id="mv-guide--loading-data"></a>

## Loading data

<a id="mv-guide--loading-data-on-commit"></a>

### Loading data on commit

In case of WITHOUT DEFERRED REFRESH, for existing table with loaded data, data load to materialized
view will be triggered by the CREATE MATERIALIZED VIEW statement when user creates the materialized
view.

For incremental loads to the fact table, data to materialized view will be loaded once the
corresponding fact table load is completed.

<a id="mv-guide--loading-data-on-manual"></a>

### Loading data on manual

In case of WITH DEFERRED REFRESH, data load to materialized view will be triggered by the refresh
command. Materialized view will be in DISABLED state in below scenarios.

- when a materialized view is created.
- when data of fact table and materialized view are not in sync.

User should fire REFRESH MATERIALIZED VIEW command to sync all segments of fact table with
materialized view, which ENABLES the materialized view for query.

Command example:

```
  REFRESH MATERIALIZED VIEW agg_sales
```

<a id="mv-guide--loading-data-to-multiple-materialized-views"></a>

### Loading data to multiple materialized views

During load to fact table, if anyone of the load to materialized view fails, then that
corresponding materialized view will be DISABLED and load to other materialized views mapped
to the fact table will continue.

User can fire REFRESH MATERIALIZED VIEW command to sync or else the subsequent table load
will load the old failed loads along with current load and enable the disabled materialized view.

> [!NOTE]
> :

- In case of InsertOverwrite/Update operation on fact table, all segments of materialized view
  will be MARKED\_FOR\_DELETE and reload to mv table will happen by REFRESH MATERIALIZED VIEW,
  in case of materialized view which refresh on manual and once the InsertOverwrite/Update
  operation on fact table is finished, in case of materialized view which refresh on commit.
- In case of full scan query, Data Size and Index Size of fact table and materialized view
  will not be the same, as fact table and materialized view have different column names.

<a id="mv-guide--querying-data"></a>

## Querying data

Queries are to be made on the fact table. While doing query planning, internally CarbonData will check
for the materialized views which are associated with the fact table, and do query plan
transformation accordingly.

Users can verify whether a query can leverage materialized view or not by executing the `EXPLAIN` command, which will show the transformed logical plan, and thus the user can check whether a materialized view
is selected.

<a id="mv-guide--compacting"></a>

## Compacting

Running Compaction command (`ALTER TABLE COMPACT`)[COMPACTION TYPE-> MINOR/MAJOR] on fact table
will automatically compact the materialized view created on the fact table, once compaction
on fact table is done.

<a id="mv-guide--data-management"></a>

## Data Management

In current implementation, data consistency needs to be maintained for both fact table and
materialized views.

Once there is materialized view created on the fact table, following command on the fact
table is not supported:

1. Data management command: `DELETE SEGMENT`.
2. Schema management command: `ALTER TABLE DROP COLUMN`, `ALTER TABLE CHANGE DATATYPE`,
   `ALTER TABLE RENAME`, `ALTER COLUMN RENAME`. Note that adding a new column is supported, and for
   dropping columns and change datatype command, CarbonData will check whether it will impact the
   materialized view, if not, the operation is allowed, otherwise operation will be rejected by
   throwing exception.
3. Partition management command: `ALTER TABLE ADD/DROP PARTITION`. Note that dropping a partition
   will be allowed only if the partition column of fact table is participating in all of the table's materialized views.
   Drop Partition is not allowed, if any materialized view is associated with more than one
   fact table. Drop Partition directly on materialized view is not allowed.
4. Complex Datatype's for materialized view is not supported.

However, there is still way to support these operations on fact table, in current CarbonData
release, user can do as following:

1. Remove the materialized view by `DROP MATERIALIZED VIEW` command.
2. Carry out the data management operation on fact table.
3. Create the materialized view again by `CREATE MATERIALIZED VIEW` command.

Basically, user can manually trigger the operation by re-building the materialized view.

<a id="mv-guide--time-series-support"></a>

## Time Series Support

Time series data are simply measurements or events that are tracked, monitored, down sampled, and
aggregated over time. Materialized views with automatic refresh mode supports TimeSeries queries.

CarbonData provides built-in time-series udf with the below definition.

```
  timeseries(event_time_column, 'granularity')
```

Event time columns provided in time series udf should be of TimeStamp/Date type.

Below table describes the time hierarchy and levels that can be provided in a time-series udf, so that it supports automatic roll-up in time dimension for query.

| Granularity | Description |
| --- | --- |
| year | Data will be aggregated over year |
| month | Data will be aggregated over month |
| week | Data will be aggregated over week |
| day | Data will be aggregated over day |
| hour | Data will be aggregated over hour |
| thirty\_minute | Data will be aggregated over every thirty minutes |
| fifteen\_minute | Data will be aggregated over every fifteen minutes |
| ten\_minute | Data will be aggregated over every ten minutes |
| five\_minute | Data will be aggregated over every five minutes |
| minute | Data will be aggregated over every one minute |
| second | Data will be aggregated over every second |

Time series udf having column as Date type support's only year, month, day and week granularities.

Below is the sample data loaded to the fact table **sales**.

```
  order_time,          user_id, sex,    country, quantity, price
  2016-02-23 09:01:30, c001,    male,   xxx,     100,      2
  2016-02-23 09:01:50, c002,    male,   yyy,     200,      5
  2016-02-23 09:03:30, c003,    female, xxx,     400,      1
  2016-02-23 09:03:50, c004,    male,   yyy,     300,      5
  2016-02-23 09:07:50, c005,    female, xxx,     500,      5
```

Users can create materialized views with time series queries like the below example:

```
  CREATE MATERIALIZED VIEW agg_sales AS
  SELECT timeseries(order_time, 'minute'),avg(price)
  FROM sales
  GROUP BY timeseries(order_time, 'minute')
```

And execute the below query to check time series data. In this example, a materialized view of
the aggregated table on the price column will be created, which will be aggregated every one minute.

```
  SELECT timeseries(order_time,'minute'), avg(price)
  FROM sales
  GROUP BY timeseries(order_time,'minute')
```

Find below the result of the above query aggregated over a minute.

```
  +---------------------------------------+----------------+
  |UDF:timeseries(order_time, minute)     |avg(price)      |
  +---------------------------------------+----------------+
  |2016-02-23 09:01:00                    |3.5             |
  |2016-02-23 09:07:00                    |5.0             |
  |2016-02-23 09:03:00                    |3.0             |
  +---------------------------------------+----------------+
```

The data loading, querying, compaction command and its behavior is the same as materialized views.

<a id="mv-guide--how-data-is-aggregated-over-time"></a>

#### How data is aggregated over time?

On each load to materialized view, data will be aggregated based on the specified time interval of
granularity provided during creation and stored on each segment.

> [!NOTE]
> :

1. Retention policies for time series is not supported yet.

<a id="mv-guide--time-series-rollup-support"></a>

## Time Series RollUp Support

Time series queries can be rolled up from an existing materialized view.

<a id="mv-guide--query-rollup"></a>

### Query RollUp

Consider an example where the query is on hour level granularity, but the materialized view
with hour level granularity is not present but materialized view with minute level granularity is
present, then we can get the data from minute level and aggregate the hour level data and
give output. This is called query rollup.

Consider if user create's below time series materialized view,

```
  CREATE MATERIALIZED VIEW agg_sales
  AS
  SELECT timeseries(order_time,'minute'),avg(price)
  FROM sales
  GROUP BY timeseries(order_time,'minute')
```

and fires the below query with hour level granularity.

```
  SELECT timeseries(order_time,'hour'),avg(price)
  FROM sales
  GROUP BY timeseries(order_time,'hour')
```

Then, the above query can be rolled up from materialized view 'agg\_sales', by adding hour
level time series aggregation on minute level aggregation. Users can fire the `EXPLAIN` command
to check if a query is rolled up from an existing materialized view.

> [!NOTE]
> :
> 1. Queries cannot be rolled up, if the filter contains a time series function.
> 2. Roll up is not yet supported for queries having join clause or order by functions.

[Top](#mv-guide--top)

---

<a id="sdk-guide"></a>

<!-- source_url: https://carbondata.apache.org/sdk-guide.html -->

<!-- page_index: 17 -->

<a id="sdk-guide--sdk-guide"></a>

# SDK Guide

CarbonData provides SDK to facilitate

1. [Writing carbondata files from other application which does not use Spark](#sdk-guide--sdk-writer)
2. [Reading carbondata files from other application which does not use Spark](#sdk-guide--sdk-reader)

<a id="sdk-guide--sdk-writer"></a>

# SDK Writer

In the carbon jars package, there exist a carbondata-sdk-x.x.x-SNAPSHOT.jar, including SDK writer and reader.
If user want to use SDK, except carbondata-sdk-x.x.x-SNAPSHOT.jar, it needs carbondata-core-x.x.x-SNAPSHOT.jar, carbondata-common-x.x.x-SNAPSHOT.jar, carbondata-format-x.x.x-SNAPSHOT.jar, carbondata-hadoop-x.x.x-SNAPSHOT.jar and carbondata-processing-x.x.x-SNAPSHOT.jar.
What's more, user also can use carbondata-sdk.jar directly.

This SDK writer, writes carbondata file and carbonindex file at a given path.
External client can make use of this writer to convert other format data or live data to create carbondata and index files.
These SDK writer output contains just carbondata and carbonindex files. No metadata folder will be present.

<a id="sdk-guide--quick-example"></a>

## Quick example

<a id="sdk-guide--example-with-csv-format"></a>

### Example with csv format

```
import java.io.IOException;

import org.apache.carbondata.common.exceptions.sql.InvalidLoadOptionException;
import org.apache.carbondata.core.metadata.datatype.DataTypes;
import org.apache.carbondata.core.util.CarbonProperties;
import org.apache.carbondata.sdk.file.CarbonWriter;
import org.apache.carbondata.sdk.file.CarbonWriterBuilder;
import org.apache.carbondata.core.metadata.datatype.Field;
import org.apache.carbondata.sdk.file.Schema;

public class TestSdk {

  // pass true or false while executing the main to use offheap memory or not
  public static void main(String[] args) throws IOException, InvalidLoadOptionException {
    if (args.length > 0 && args[0] != null) {
      testSdkWriter(args[0]);
    } else {
      testSdkWriter("true");
    }
  }

  public static void testSdkWriter(String enableOffheap) throws IOException, InvalidLoadOptionException {
    String path = "./target/testCSVSdkWriter";

    Field[] fields = new Field[2];
    fields[0] = new Field("name", DataTypes.STRING);
    fields[1] = new Field("age", DataTypes.INT);

    Schema schema = new Schema(fields);

    CarbonProperties.getInstance().addProperty("enable.offheap.sort", enableOffheap);

    CarbonWriterBuilder builder = CarbonWriter.builder().outputPath(path).withCsvInput(schema).writtenBy("SDK");

    CarbonWriter writer = builder.build();

    int rows = 5;
    for (int i = 0; i < rows; i++) {
      writer.write(new String[] { "robot" + (i % 10), String.valueOf(i) });
    }
    writer.close();
  }
}
```

<a id="sdk-guide--example-with-avro-format"></a>

### Example with Avro format

```
import java.io.IOException;

import org.apache.carbondata.common.exceptions.sql.InvalidLoadOptionException;
import org.apache.carbondata.core.metadata.datatype.DataTypes;
import org.apache.carbondata.sdk.file.AvroCarbonWriter;
import org.apache.carbondata.sdk.file.CarbonWriter;
import org.apache.carbondata.core.metadata.datatype.Field;

import org.apache.avro.generic.GenericData;
import org.apache.commons.lang.CharEncoding;

import tech.allegro.schema.json2avro.converter.JsonAvroConverter;

public class TestSdkAvro {

  public static void main(String[] args) throws IOException, InvalidLoadOptionException {
    testSdkWriter();
  }


  public static void testSdkWriter() throws IOException, InvalidLoadOptionException {
    String path = "./AvroCarbonWriterSuiteWriteFiles";
    // Avro schema
    String avroSchema =
        "{" +
            "   \"type\" : \"record\"," +
            "   \"name\" : \"Acme\"," +
            "   \"fields\" : ["
            + "{ \"name\" : \"fname\", \"type\" : \"string\" },"
            + "{ \"name\" : \"age\", \"type\" : \"int\" }]" +
            "}";

    String json = "{\"fname\":\"bob\", \"age\":10}";

    // conversion to GenericData.Record
    JsonAvroConverter converter = new JsonAvroConverter();
    GenericData.Record record = converter.convertToGenericDataRecord(
        json.getBytes(CharEncoding.UTF_8), new org.apache.avro.Schema.Parser().parse(avroSchema));

    try {
      CarbonWriter writer = CarbonWriter.builder()
          .outputPath(path)
          .withAvroInput(new org.apache.avro.Schema.Parser().parse(avroSchema)).writtenBy("SDK").build();

      for (int i = 0; i < 100; i++) {
        writer.write(record);
      }
      writer.close();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

<a id="sdk-guide--example-with-json-format"></a>

### Example with Json format

```
import java.io.IOException;
 
import org.apache.carbondata.common.exceptions.sql.InvalidLoadOptionException;
import org.apache.carbondata.core.metadata.datatype.DataTypes;
import org.apache.carbondata.core.util.CarbonProperties;
import org.apache.carbondata.sdk.file.CarbonWriter;
import org.apache.carbondata.sdk.file.CarbonWriterBuilder;
import org.apache.carbondata.core.metadata.datatype.Field;
import org.apache.carbondata.sdk.file.Schema;
 
public class TestSdkJson {

   public static void main(String[] args) throws InvalidLoadOptionException {
       testJsonSdkWriter();
   }
   
   public static void testJsonSdkWriter() throws InvalidLoadOptionException {
    String path = "./target/testJsonSdkWriter";

    Field[] fields = new Field[2];
    fields[0] = new Field("name", DataTypes.STRING);
    fields[1] = new Field("age", DataTypes.INT);

    Schema CarbonSchema = new Schema(fields);

    CarbonWriterBuilder builder = CarbonWriter.builder().outputPath(path).withJsonInput(CarbonSchema).writtenBy("SDK");

    // initialize json writer with carbon schema
    CarbonWriter writer = builder.build();
    // one row of json Data as String
    String  JsonRow = "{\"name\":\"abcd\", \"age\":10}";

    int rows = 5;
    for (int i = 0; i < rows; i++) {
      writer.write(JsonRow);
    }
    writer.close();
  }
} 
```

<a id="sdk-guide--datatypes-mapping"></a>

## Datatypes Mapping

Each of SQL data types and Avro Data Types are mapped into data types of SDK. Following are the mapping:

| SQL DataTypes | Avro DataTypes | Mapped SDK DataTypes |
| --- | --- | --- |
| BOOLEAN | BOOLEAN | DataTypes.BOOLEAN |
| SMALLINT | - | DataTypes.SHORT |
| INTEGER | INTEGER | DataTypes.INT |
| BIGINT | LONG | DataTypes.LONG |
| DOUBLE | DOUBLE | DataTypes.DOUBLE |
| VARCHAR | - | DataTypes.STRING |
| BINARY | - | DataTypes.BINARY |
| FLOAT | FLOAT | DataTypes.FLOAT |
| BYTE | - | DataTypes.BYTE |
| DATE | DATE | DataTypes.DATE |
| TIMESTAMP | - | DataTypes.TIMESTAMP |
| STRING | STRING | DataTypes.STRING |
| DECIMAL | DECIMAL | DataTypes.createDecimalType(precision, scale) |
| ARRAY | ARRAY | DataTypes.createArrayType(elementType) |
| STRUCT | RECORD | DataTypes.createStructType(fields) |
| - | ENUM | DataTypes.STRING |
| - | UNION | DataTypes.createStructType(types) |
| - | MAP | DataTypes.createMapType(keyType, valueType) |
| - | TimeMillis | DataTypes.INT |
| - | TimeMicros | DataTypes.LONG |
| - | TimestampMillis | DataTypes.TIMESTAMP |
| - | TimestampMicros | DataTypes.TIMESTAMP |

**NOTE:**

1. Carbon Supports below logical types of AVRO.
   a. Date
   The date logical type represents a date within the calendar, with no reference to a particular time zone or time of day.
   A date logical type annotates an Avro int, where the int stores the number of days from the unix epoch, 1 January 1970 (ISO calendar).
   b. Timestamp (millisecond precision)
   The timestamp-millis logical type represents an instant on the global timeline, independent of a particular time zone or calendar, with a precision of one millisecond.
   A timestamp-millis logical type annotates an Avro long, where the long stores the number of milliseconds from the unix epoch, 1 January 1970 00:00:00.000 UTC.
   c. Timestamp (microsecond precision)
   The timestamp-micros logical type represents an instant on the global timeline, independent of a particular time zone or calendar, with a precision of one microsecond.
   A timestamp-micros logical type annotates an Avro long, where the long stores the number of microseconds from the unix epoch, 1 January 1970 00:00:00.000000 UTC.
   d. Decimal
   The decimal logical type represents an arbitrary-precision signed decimal number of the form *unscaled × 10-scale*.
   A decimal logical type annotates Avro bytes or fixed types. The byte array must contain the two's-complement representation of the unscaled integer value in big-endian byte order. The scale is fixed, and is specified using an attribute.
   e. Time (millisecond precision)
   The time-millis logical type represents a time of day, with no reference to a particular calendar, time zone or date, with a precision of one millisecond.
   A time-millis logical type annotates an Avro int, where the int stores the number of milliseconds after midnight, 00:00:00.000.
   f. Time (microsecond precision)
   The time-micros logical type represents a time of day, with no reference to a particular calendar, time zone or date, with a precision of one microsecond.
   A time-micros logical type annotates an Avro long, where the long stores the number of microseconds after midnight, 00:00:00.000000.

   Currently the values of logical types are not validated by carbon.
   Expect that avro record passed by the user is already validated by avro record generator tools.
2. If the string data is more than 32K in length, use withTableProperties() with "long\_string\_columns" property
   or directly use DataTypes.VARCHAR if it is carbon schema.
3. Avro Bytes, Fixed and Duration data types are not yet supported.

<a id="sdk-guide--run-sql-on-files-directly"></a>

## Run SQL on files directly

Instead of creating table and query it, you can also query that file directly with SQL.

<a id="sdk-guide--example"></a>

### Example

```
SELECT * FROM carbonfile.`$Path`
```

Find example code at [DirectSQLExample](https://github.com/apache/carbondata/blob/master/examples/spark/src/main/scala/org/apache/carbondata/examples/DirectSQLExample.scala) in the CarbonData repo.

<a id="sdk-guide--api-list"></a>

## API List

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.carbonwriterbuilder"></a>

### Class org.apache.carbondata.sdk.file.CarbonWriterBuilder

```
/**
 * Sets the output path of the writer builder
 *
 * @param path is the absolute path where output files are written
 *             This method must be called when building CarbonWriterBuilder
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder outputPath(String path);
```

```
/**
 * To set the timestamp in the carbondata and carbonindex index files
 *
 * @param UUID is a timestamp to be used in the carbondata and carbonindex index files.
 *             By default set to zero.
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder uniqueIdentifier(long UUID);
```

```
/**
 * To set the carbondata file size in MB between 1MB-2048MB
 *
 * @param blockSize is size in MB between 1MB to 2048 MB
 *                  default value is 1024 MB
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder withBlockSize(int blockSize);
```

```
/**
 * To set the blocklet size of carbondata file
 *
 * @param blockletSize is blocklet size in MB
 *                     default value is 64 MB
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder withBlockletSize(int blockletSize);
```

```
/**
 * @param enableLocalDictionary enable local dictionary  , default is false
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder enableLocalDictionary(boolean enableLocalDictionary);
```

```
/**
 * @param localDictionaryThreshold is localDictionaryThreshold,default is 10000
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder localDictionaryThreshold(int localDictionaryThreshold) ;
```

```
/**
 * Sets the list of columns that needs to be in sorted order
 *
 * @param sortColumns is a string array of columns that needs to be sorted.
 *                    If it is null or empty array, no columns are selected for sorting.
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder sortBy(String[] sortColumns);
```

```
/**
 * Sets the taskNo for the writer. SDKs concurrently running
 * will set taskNo in order to avoid conflicts in file's name during write.
 *
 * @param taskNo is the TaskNo user wants to specify.
 *               by default it is system time in nano seconds.
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder taskNo(long taskNo);
```

```
/**
 * To support the load options for sdk writer
 * @param options key,value pair of load options.
 *                supported keys values are
 *                a. bad_records_logger_enable -- true (write into separate logs), false
 *                b. bad_records_action -- FAIL, FORCE, IGNORE, REDIRECT
 *                c. bad_record_path -- path
 *                d. dateformat -- same as JAVA SimpleDateFormat
 *                e. timestampformat -- same as JAVA SimpleDateFormat
 *                f. complex_delimiter_level_1 -- value to Split the complexTypeData
 *                g. complex_delimiter_level_2 -- value to Split the nested complexTypeData
 *                h. quotechar
 *                i. escapechar
 *                
 *                Default values are as follows.
 *
 *                a. bad_records_logger_enable -- "false"
 *                b. bad_records_action -- "FAIL"
 *                c. bad_record_path -- ""
 *                d. dateformat -- "" , uses from carbon.properties file
 *                e. timestampformat -- "", uses from carbon.properties file
 *                f. complex_delimiter_level_1 -- "$"
 *                g. complex_delimiter_level_2 -- ":"
 *                h. quotechar -- "\""
 *                i. escapechar -- "\\"
 *
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder withLoadOptions(Map<String, String> options);
```

```
/**
 * To support the table properties for sdk writer
 *
 * @param options key,value pair of create table properties.
 * supported keys values are
 * a. table_blocksize -- [1-2048] values in MB. Default value is 1024
 * b. table_blocklet_size -- values in MB. Default value is 64 MB
 * c. local_dictionary_threshold -- positive value, default is 10000
 * d. local_dictionary_enable -- true / false. Default is false
 * e. sort_columns -- comma separated column. "c1,c2". Default no columns are sorted.
 * j. sort_scope -- "local_sort", "no_sort". default value is "no_sort"
 * k. long_string_columns -- comma separated string columns which are more than 32k length. 
 *                           default value is null.
 * l. inverted_index -- comma separated string columns for which inverted index needs to be
 *                      generated
 * m. table_page_size_inmb -- [1-1755] MB. 
 *
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder withTableProperties(Map<String, String> options);
```

```
/**
 * To make sdk writer thread safe.
 *
 * @param numOfThreads should number of threads in which writer is called in multi-thread scenario
 *                     default sdk writer is not thread safe.
 *                     can use one writer instance in one thread only.
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder withThreadSafe(short numOfThreads);
```

```
/**
 * To support hadoop configuration
 *
 * @param conf hadoop configuration support, can set s3a AK,SK,end point and other conf with this
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder withHadoopConf(Configuration conf)
```

```
/**
 * Updates the hadoop configuration with the given key value
 *
 * @param key   key word
 * @param value value
 * @return this object
 */
public CarbonWriterBuilder withHadoopConf(String key, String value);
```

```
/**
 * To build a {@link CarbonWriter}, which accepts row in CSV format
 *
 * @param schema carbon Schema object {org.apache.carbondata.sdk.file.Schema}
 * @return CarbonWriterBuilder
 */
public CarbonWriterBuilder withCsvInput(Schema schema);
```

```
/**
 * To build a {@link CarbonWriter}, which accepts Avro object
 *
 * @param avroSchema avro Schema object {org.apache.avro.Schema}
 * @return CarbonWriterBuilder
 */
public CarbonWriterBuilder withAvroInput(org.apache.avro.Schema avroSchema);
```

```
/**
 * To build a {@link CarbonWriter}, which accepts Json object
 *
 * @param carbonSchema carbon Schema object
 * @return CarbonWriterBuilder
 */
public CarbonWriterBuilder withJsonInput(Schema carbonSchema);
```

```
/**
 * To support writing the ApplicationName which is writing the carbondata file
 * This is a mandatory API to call, else the build() call will fail with error.
 * @param application name which is writing the carbondata files
 * @return CarbonWriterBuilder
 */
public CarbonWriterBuilder writtenBy(String appName) {
```

```
/**
 * Sets the list of columns for which inverted index needs to generated
 *
 * @param invertedIndexColumns is a string array of columns for which inverted index needs to
 * generated.
 * If it is null or an empty array, inverted index will be generated for none of the columns
 * @return updated CarbonWriterBuilder
 */
public CarbonWriterBuilder invertedIndexFor(String[] invertedIndexColumns);
```

```
/**
 * Build a {@link CarbonWriter}
 * This writer is not thread safe,
 * use withThreadSafe() configuration in multi thread environment
 * 
 * @return CarbonWriter {AvroCarbonWriter/CSVCarbonWriter/JsonCarbonWriter based on Input Type }
 * @throws IOException
 * @throws InvalidLoadOptionException
 */
public CarbonWriter build() throws IOException, InvalidLoadOptionException;
```

```
/**
 * Configure Row Record Reader for reading.
 *
 */
public CarbonReaderBuilder withRowRecordReader()
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.carbonwriter"></a>

### Class org.apache.carbondata.sdk.file.CarbonWriter

```
/**
 * Create a {@link CarbonWriterBuilder} to build a {@link CarbonWriter}
 */
public static CarbonWriterBuilder builder() {
    return new CarbonWriterBuilder();
}
```

```
/**
 * Write an object to the file, the format of the object depends on the implementation
 * If AvroCarbonWriter, object is of type org.apache.avro.generic.GenericData.Record, 
 *                      which is one row of data.
 * If CSVCarbonWriter, object is of type String[], which is one row of data
 * If JsonCarbonWriter, object is of type String, which is one row of json
 *
 * @param object
 * @throws IOException
 */
public abstract void write(Object object) throws IOException;
```

```
/**
 * Flush and close the writer
 */
public abstract void close() throws IOException;
```

<a id="sdk-guide--class-org.apache.carbondata.core.metadata.datatype.field"></a>

### Class org.apache.carbondata.core.metadata.datatype.Field

```
/**
 * Field Constructor
 *
 * @param name name of the field
 * @param type datatype of field, specified in strings.
 */
public Field(String name, String type);
```

```
/**
 * Field constructor
 *
 * @param name name of the field
 * @param type datatype of the field of class DataType
 */
public Field(String name, DataType type);  
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.schema"></a>

### Class org.apache.carbondata.sdk.file.Schema

```
/**
 * Construct a schema with fields
 *
 * @param fields
 */
public Schema(Field[] fields);
```

```
/**
 * Create a Schema using JSON string, for example:
 * [
 *   {"name":"string"},
 *   {"age":"int"}
 * ] 
 * @param json specified as string
 * @return Schema
 */
public static Schema parseJson(String json);
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.avrocarbonwriter"></a>

### Class org.apache.carbondata.sdk.file.AvroCarbonWriter

```
/**
 * Converts avro schema to carbon schema, required by carbonWriter
 *
 * @param avroSchemaString json formatted avro schema as string
 * @return carbon sdk schema
 */
public static org.apache.carbondata.sdk.file.Schema getCarbonSchemaFromAvroSchema(String avroSchemaString);
```

<a id="sdk-guide--sdk-reader"></a>

# SDK Reader

This SDK reader reads CarbonData file and carbonindex file at a given path.
External client can make use of this reader to read CarbonData files without CarbonSession.

<a id="sdk-guide--quick-example-2"></a>

## Quick example

```
// 1. Create carbon reader
String path = "./testWriteFiles";
CarbonReader reader = CarbonReader
    .builder(path, "_temp")
    .projection(new String[]{"stringField", "shortField", "intField", "longField", 
            "doubleField", "boolField", "dateField", "timeField", "decimalField"})
    .build();

// 2. Read data
long day = 24L * 3600 * 1000;
int i = 0;
while (reader.hasNext()) {
    Object[] row = (Object[]) reader.readNextRow();
    System.out.println(String.format("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t",
        i, row[0], row[1], row[2], row[3], row[4], row[5],
        new Date((day * ((int) row[6]))), new Timestamp((long) row[7] / 1000), row[8]
    ));
    i++;
}

// 3. Close this reader
reader.close();
```

Find example code at [CarbonReaderExample](https://github.com/apache/carbondata/blob/master/examples/spark/src/main/java/org/apache/carbondata/examples/sdk/CarbonReaderExample.java) in the CarbonData repo.

SDK reader also supports reading carbondata files and filling it to apache arrow vectors.
Find example code at [ArrowCarbonReaderTest](https://github.com/apache/carbondata/blob/master/sdk/sdk/src/test/java/org/apache/carbondata/sdk/file/ArrowCarbonReaderTest.java) in the CarbonData repo.

<a id="sdk-guide--api-list-2"></a>

## API List

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.carbonreader"></a>

### Class org.apache.carbondata.sdk.file.CarbonReader

```
/**
 * Return a new {@link CarbonReaderBuilder} instance
 *
 * @param tablePath table store path
 * @param tableName table name
 * @return CarbonReaderBuilder object
 */
public static CarbonReaderBuilder builder(String tablePath, String tableName);
```

```
/**
 * Return a new CarbonReaderBuilder instance
 * Default value of table name is table + tablePath + time
 *
 * @param tablePath table path
 * @return CarbonReaderBuilder object
 */
public static CarbonReaderBuilder builder(String tablePath);
```

```
/**
 * Breaks the list of CarbonRecordReader in CarbonReader into multiple
 * CarbonReader objects, each iterating through some 'carbondata' files
 * and return that list of CarbonReader objects
 *
 * If the no. of files is greater than maxSplits, then break the
 * CarbonReader into maxSplits splits, with each split iterating
 * through >= 1 file.
 *
 * If the no. of files is less than maxSplits, then return list of
 * CarbonReader with size as the no. of files, with each CarbonReader
 * iterating through exactly one file
 *
 * @param maxSplits: Int
 * @return list of CarbonReader objects
 */
public List<CarbonReader> split(int maxSplits);
```

```
/**
 * Return true if has next row
 */
public boolean hasNext();
```

```
/**
 * Read and return next row object
 */
public T readNextRow();
```

```
/**
 * Read and return next batch row objects
 */
public Object[] readNextBatchRow();
```

```
/**
 * Close reader
 */
public void close();
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.arrowcarbonreader"></a>

### Class org.apache.carbondata.sdk.file.ArrowCarbonReader

```
/**
 * Carbon reader will fill the arrow vector after reading the carbondata files.
 * This arrow byte[] can be used to create arrow table and used for in memory analytics
 * Note: create a reader at blocklet level, so that arrow byte[] will not exceed INT_MAX
 *
 * @param carbonSchema org.apache.carbondata.sdk.file.Schema
 * @return Serialized byte array
 * @throws Exception
 */
public byte[] readArrowBatch(Schema carbonSchema) throws Exception;
```

```
/**
 * Carbon reader will fill the arrow vector after reading the carbondata files.
 * This arrow byte[] can be used to create arrow table and used for in memory analytics
 * Note: create a reader at blocklet level, so that arrow byte[] will not exceed INT_MAX
 * User need to close the VectorSchemaRoot after usage by calling VectorSchemaRoot.close()
 *
 * @param carbonSchema org.apache.carbondata.sdk.file.Schema 
 * @return Arrow VectorSchemaRoot
 * @throws Exception
 */
public VectorSchemaRoot readArrowVectors(Schema carbonSchema) throws Exception;
```

```
/**
 * Carbon reader will fill the arrow vector after reading carbondata files.
 * Here unsafe memory address will be returned instead of byte[],
 * so that this address can be sent across java to python or c modules and
 * can directly read the content from this unsafe memory
 * Note:Create a carbon reader at blocklet level using CarbonReader.buildWithSplits(split) method,
 * so that arrow byte[] will not exceed INT_MAX.
 *
 * @param carbonSchema org.apache.carbondata.sdk.file.Schema
 * @return address of the unsafe memory where arrow buffer is stored
 * @throws Exception
 */
public long readArrowBatchAddress(Schema carbonSchema) throws Exception;
```

```
/**
 * Free the unsafe memory allocated , if unsafe arrow batch is used.
 *
 * @param address address of the unsafe memory where arrow bufferer is stored
 */
public void freeArrowBatchMemory(long address)
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.arrow.arrowconverter"></a>

### Class org.apache.carbondata.sdk.file.arrow.ArrowConverter

```
/**
 * To get the arrow vectors directly after filling from carbondata
 *
 * @return Arrow VectorSchemaRoot. which contains array of arrow vectors.
 */
public VectorSchemaRoot getArrowVectors() throws IOException;
```

```
/**
 * Utility API to convert back the arrow byte[] to arrow ArrowRecordBatch.
 * User need to close the ArrowRecordBatch after usage by calling ArrowRecordBatch.close()
 *
 * @param batchBytes input byte array
 * @param bufferAllocator arrow buffer allocator
 * @return ArrowRecordBatch
 * @throws IOException
 */
public static ArrowRecordBatch byteArrayToArrowBatch(byte[] batchBytes, BufferAllocator bufferAllocator) throws IOException;
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.carbonreaderbuilder"></a>

### Class org.apache.carbondata.sdk.file.CarbonReaderBuilder

```
/**
 * Construct a CarbonReaderBuilder with table path and table name
 *
 * @param tablePath table path
 * @param tableName table name
 */
CarbonReaderBuilder(String tablePath, String tableName);
```

```
/**
 * Configure the projection column names of carbon reader
 *
 * @param projectionColumnNames projection column names
 * @return CarbonReaderBuilder object
 */
public CarbonReaderBuilder projection(String[] projectionColumnNames);
```

```
/**
 * Configure the filter expression for carbon reader
 *
 * @param filterExpression filter expression
 * @return CarbonReaderBuilder object
 */
public CarbonReaderBuilder filter(Expression filterExpression);
```

```
/**
 * Sets the batch size of records to read
 *
 * @param batch batch size
 * @return updated CarbonReaderBuilder
 */
public CarbonReaderBuilder withBatch(int batch);
```

```
/**
 * To support hadoop configuration
 *
 * @param conf hadoop configuration support, can set s3a AK,SK,end point and other conf with this
 * @return updated CarbonReaderBuilder
 */
public CarbonReaderBuilder withHadoopConf(Configuration conf);
```

```
/**
 * Updates the hadoop configuration with the given key value
 *
 * @param key   key word
 * @param value value
 * @return this object
 */
public CarbonReaderBuilder withHadoopConf(String key, String value);
```

```
/**
 * Build CarbonReader
 *
 * @param <T>
 * @return CarbonReader
 * @throws IOException
 * @throws InterruptedException
 */
public <T> CarbonReader<T> build();
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.carbonschemareader"></a>

### Class org.apache.carbondata.sdk.file.CarbonSchemaReader

```
/**
 * Read schema file and return the schema
 *
 * @param schemaFilePath complete path including schema file name
 * @return schema object
 * @throws IOException
 */
@Deprecated
public static Schema readSchemaInSchemaFile(String schemaFilePath);
```

```
/**
 * Read carbondata file and return the schema
 *
 * @param dataFilePath complete path including carbondata file name
 * @return Schema object
 */
@Deprecated
public static Schema readSchemaInDataFile(String dataFilePath);
```

```
/**
 * Read carbonindex file and return the schema
 *
 * @param indexFilePath complete path including index file name
 * @return schema object
 * @throws IOException
 */
@Deprecated
public static Schema readSchemaInIndexFile(String indexFilePath);
```

```
/**
 * Read schema from path,
 * path can be folder path,carbonindex file path, and carbondata file path
 * and will not check all files schema
 *
 * @param path file/folder path
 * @return schema
 * @throws IOException
 */
public static Schema readSchema(String path);
```

```
/**
 * Read schema from path,
 * path can be folder path,carbonindex file path, and carbondata file path
 * and user can decide whether check all files schema
 *
 * @param path             file/folder path
 * @param validateSchema whether check all files schema
 * @return schema
 * @throws IOException
 */
public static Schema readSchema(String path, boolean validateSchema);
```

```
/**
 * Read schema from path,
 * path can be folder path, carbonindex file path, and carbondata file path
 * and will not check all files schema
 *
 * @param path file/folder path
 * @param conf hadoop configuration support, can set s3a AK,SK,end point and other conf with this
 * @return schema
 * @throws IOException
 */
public static Schema readSchema(String path, Configuration conf);
```

```
/**
 * Read schema from path,
 * path can be folder path, carbonindex file path, and carbondata file path
 * and user can decide whether check all files schema
 *
 * @param path           file/folder path
 * @param validateSchema whether check all files schema
 * @param conf           hadoop configuration support, can set s3a AK,SK,
 *                       end point and other conf with this
 * @return schema
 * @throws IOException
 */
public static Schema readSchema(String path, boolean validateSchema, Configuration conf);
```

```
/**
 * This method return the version details in formatted string by reading from carbondata file
 * If application name is SDK_1.0.0 and this has written the carbondata file in carbondata 1.6 project version,
 * then this API returns the String "SDK_1.0.0 in version: 1.6.0-SNAPSHOT"
 *
 * @param dataFilePath complete path including carbondata file name
 * @return string with information of who has written this file in which carbondata project version
 * @throws IOException
 */
public static String getVersionDetails(String dataFilePath);
```

<a id="sdk-guide--class-org.apache.carbondata.sdk.file.schema-2"></a>

### Class org.apache.carbondata.sdk.file.Schema

```
/**
 * Construct a schema with fields
 *
 * @param fields
 */
public Schema(Field[] fields);
```

```
/**
 * Construct a schema with List<ColumnSchema>
 *
 * @param columnSchemaList column schema list
 */
public Schema(List<ColumnSchema> columnSchemaList);
```

```
/**
 * Create a Schema using JSON string, for example:
 * [
 *   {"name":"string"},
 *   {"age":"int"}
 * ]
 * @param json specified as string
 * @return Schema
 */
public static Schema parseJson(String json);
```

```
/**
 * Sort the schema order as original order
 *
 * @return Schema object
 */
public Schema asOriginOrder();
```

<a id="sdk-guide--class-org.apache.carbondata.core.metadata.datatype.field-2"></a>

### Class org.apache.carbondata.core.metadata.datatype.Field

```
/**
 * Field Constructor
 *
 * @param name name of the field
 * @param type datatype of field, specified in strings.
 */
public Field(String name, String type);
```

```
/**
 * Construct Field from ColumnSchema
 *
 * @param columnSchema ColumnSchema, Store the information about the column meta data
 */
public Field(ColumnSchema columnSchema);
```

Find S3 example code at [SDKS3Example](https://github.com/apache/carbondata/blob/master/examples/spark/src/main/java/org/apache/carbondata/examples/sdk/SDKS3Example.java) in the CarbonData repo.

<a id="sdk-guide--common-api-list-for-carbonreader-and-carbonwriter"></a>

# Common API List for CarbonReader and CarbonWriter

<a id="sdk-guide--class-org.apache.carbondata.core.util.carbonproperties"></a>

### Class org.apache.carbondata.core.util.CarbonProperties

```
/**
 * This method will be responsible to get the instance of CarbonProperties class
 *
 * @return carbon properties instance
 */
public static CarbonProperties getInstance();
```

```
/**
 * This method will be used to add a new property
 *
 * @param key is a property name to set for carbon.
 * @param value is valid parameter corresponding to property.
 * @return CarbonProperties object
 */
public CarbonProperties addProperty(String key, String value);
```

```
/**
 * This method will be used to get the property value. If property is not
 * present, then it will return the default value.
 *
 * @param key is a property name to get user specified value.
 * @return properties value for corresponding key. If not set, then returns null.
 */
public String getProperty(String key);
```

```
/**
 * This method will be used to get the property value. If property is not
 * present, then it will return the default value.
 *
 * @param key is a property name to get user specified value..
 * @param defaultValue used to be returned by function if corrosponding key not set.
 * @return properties value for corresponding key. If not set, then returns specified defaultValue.
 */
public String getProperty(String key, String defaultValue);
```

Reference : [list of carbon properties](#configuration-parameters)

[Top](#sdk-guide--top)

---

<a id="csdk-guide"></a>

<!-- source_url: https://carbondata.apache.org/csdk-guide.html -->

<!-- page_index: 18 -->

<a id="csdk-guide--c-sdk-guide"></a>

# C++ SDK Guide

CarbonData C++ SDK provides C++ interface to write and read carbon file.
C++ SDK use JNI to invoke java SDK in C++ code.

<a id="csdk-guide--c-sdk-reader"></a>

# C++ SDK Reader

This C++ SDK reader reads CarbonData file and carbonindex file at a given path.
External client can make use of this reader to read CarbonData files in C++
code and without CarbonSession.

In the carbon jars package, there exist a carbondata-sdk.jar, including SDK reader for C++ SDK.

<a id="csdk-guide--quick-example"></a>

## Quick example

Please find example code at [main.cpp](https://github.com/apache/carbondata/blob/master/store/CSDK/test/main.cpp) of CSDK module

When users use C++ to read carbon files, users should init JVM first. Then users create
carbon reader and read data.There are some example code of read data from local disk
and read data from S3 at main.cpp of CSDK module. Finally, users need to
release the memory and destroy JVM.

C++ SDK support read batch row. User can set batch by using withBatch(int batch) before build, and read batch by using readNextBatchRow().

<a id="csdk-guide--api-list"></a>

## API List

<a id="csdk-guide--carbonreader"></a>

### CarbonReader

```
/**
 * Create a CarbonReaderBuilder object for building carbonReader,
 * CarbonReaderBuilder object  can configure different parameter
 *
 * @param env JNIEnv
 * @param path data store path
 * @param tableName table name
 * @return CarbonReaderBuilder object
 */
jobject builder(JNIEnv *env, char *path, char *tableName);
```

```
/**
 * Create a CarbonReaderBuilder object for building carbonReader,
 * CarbonReaderBuilder object can configure different parameter
 *
 * @param env JNIEnv
 * @param path data store path
 * 
 */
void builder(JNIEnv *env, char *path);
```

```
/**
 * Configure the projection column names of carbon reader
 *
 * @param argc argument counter
 * @param argv argument vector
 * @return CarbonReaderBuilder object
 */
jobject projection(int argc, char *argv[]);
```

```
/**
 * Build carbon reader with argument vector
 * it supports multiple parameters
 * like: key=value
 * for example: fs.s3a.access.key=XXXX, XXXX is user's access key value
 *
 * @param argc argument counter
 * @param argv argument vector
 * @return CarbonReaderBuilder object
 *
 */
jobject withHadoopConf(int argc, char *argv[]);
```

```
/**
 * Sets the batch size of records to read
 *
 * @param batch batch size
 * @return CarbonReaderBuilder object
 */
void withBatch(int batch);
```

```
/**
 * Configure Row Record Reader for reading.
 */
void withRowRecordReader();
```

```
/**
 * Build carbonReader object for reading data
 * it supports read data from load disk
 *
 * @return carbonReader object
 */
jobject build();
```

```
/**
 * Whether it has next row data
 *
 * @return boolean value, if it has next row, return true. if it hasn't next row, return false.
 */
jboolean hasNext();
```

```
/**
 * Read next carbonRow from data
 * @return carbonRow object of one row
 */
jobject readNextRow();
```

```
/**
 * Read Next Batch Row
 *
 * @return rows
 */
jobjectArray readNextBatchRow();
```

```
/**
 * Close the carbon reader
 *
 * @return  boolean value
 */
jboolean close();
```

<a id="csdk-guide--c-sdk-writer"></a>

# C++ SDK Writer

This C++ SDK writer writes CarbonData file and carbonindex file at a given path.
External client can make use of this writer to write CarbonData files in C++
code and without CarbonSession. C++ SDK already supports S3 and local disk.

In the carbon jars package, there exist a carbondata-sdk.jar, including SDK writer for C++ SDK.

<a id="csdk-guide--quick-example-2"></a>

## Quick example

Please find example code at [main.cpp](https://github.com/apache/carbondata/blob/master/store/CSDK/test/main.cpp) of CSDK module

When users use C++ to write carbon files, users should init JVM first. Then users create
carbon writer and write data.There are some example code of write data to local disk
and write data to S3 at main.cpp of CSDK module. Finally, users need to
release the memory and destroy JVM.

<a id="csdk-guide--api-list-2"></a>

## API List

<a id="csdk-guide--carbonwriter"></a>

### CarbonWriter

```
/**
 * Create a CarbonWriterBuilder object for building carbonWriter,
 * CarbonWriterBuilder object  can configure different parameter
 *
 * @param env JNIEnv
 * @return CarbonWriterBuilder object
 */
void builder(JNIEnv *env);
```

```
/**
 * Sets the output path of the writer builder
 *
 * @param path is the absolute path where output files are written
 * This method must be called when building CarbonWriterBuilder
 * @return updated CarbonWriterBuilder
 */
void outputPath(char *path);
```

```
/**
 * Sets the list of columns that needs to be in sorted order
 *
 * @param argc argc argument counter, the number of projection column
 * @param argv argv is a string array of columns that needs to be sorted.
 *                  If it is null or empty array, no columns are selected for sorting.
 */
void sortBy(int argc, char *argv[]);
```

```
/**
 * Configure the schema with json style schema
 *
 * @param jsonSchema json style schema
 * @return updated CarbonWriterBuilder
 */
void withCsvInput(char *jsonSchema);
```

```
/**
 * Updates the hadoop configuration with the given key value
 *
 * @param key key word
 * @param value value
 * @return CarbonWriterBuilder object
 */
void withHadoopConf(char *key, char *value);
```

```
/**
 * To support the table properties for writer
 *
 * @param key properties key
 * @param value properties value
 */
void withTableProperty(char *key, char *value);
```

```
/**
 * To support the load options for C++ sdk writer
 *
 * @param options key,value pair of load options.
 * supported keys values are
 * a. bad_records_logger_enable -- true (write into separate logs), false
 * b. bad_records_action -- FAIL, FORCE, IGNORE, REDIRECT
 * c. bad_record_path -- path
 * d. dateformat -- same as JAVA SimpleDateFormat
 * e. timestampformat -- same as JAVA SimpleDateFormat
 * f. complex_delimiter_level_1 -- value to Split the complexTypeData
 * g. complex_delimiter_level_2 -- value to Split the nested complexTypeData
 * h. quotechar
 * i. escapechar
 *
 * Default values are as follows.
 *
 * a. bad_records_logger_enable -- "false"
 * b. bad_records_action -- "FAIL"
 * c. bad_record_path -- ""
 * d. dateformat -- "" , uses from carbon.properties file
 * e. timestampformat -- "", uses from carbon.properties file
 * f. complex_delimiter_level_1 -- "$"
 * g. complex_delimiter_level_2 -- ":"
 * h. quotechar -- "\""
 * i. escapechar -- "\\"
 *
 * @return updated CarbonWriterBuilder
 */
void withLoadOption(char *key, char *value);
```

```
/**
 * Sets the taskNo for the writer. CSDKs concurrently running
 * will set taskNo in order to avoid conflicts in file's name during write.
 *
 * @param taskNo is the TaskNo user wants to specify.
 *               by default it is system time in nano seconds.
 */
void taskNo(long taskNo);
```

```
/**
 * Set the timestamp in the carbondata and carbonindex index files
 *
 * @param timestamp is a timestamp to be used in the carbondata and carbonindex index files.
 * By default set to zero.
 * @return updated CarbonWriterBuilder
 */
void uniqueIdentifier(long timestamp);
```

```
/**
 * To make c++ sdk writer thread safe.
 *
 * @param numOfThreads should number of threads in which writer is called in multi-thread scenario
 *                      default C++ sdk writer is not thread safe.
 *                      can use one writer instance in one thread only.
 */
void withThreadSafe(short numOfThreads) ;
```

```
/**
 * To set the carbondata file size in MB between 1MB-2048MB
 *
 * @param blockSize is size in MB between 1MB to 2048 MB
 * default value is 1024 MB
 */
void withBlockSize(int blockSize);
```

```
/**
 * To set the blocklet size of CarbonData file
 *
 * @param blockletSize is blocklet size in MB
 *        default value is 64 MB
 * @return updated CarbonWriterBuilder
 */
void withBlockletSize(int blockletSize);
```

```
/**
 * @param localDictionaryThreshold is localDictionaryThreshold, default is 10000
 * @return updated CarbonWriterBuilder
 */
void localDictionaryThreshold(int localDictionaryThreshold);
```

```
/**
 * @param enableLocalDictionary enable local dictionary, default is false
 * @return updated CarbonWriterBuilder
 */
void enableLocalDictionary(bool enableLocalDictionary);
```

```
/**
 * @param appName appName which is writing the carbondata files
 */
void writtenBy(char *appName);
```

```
/**
 * Build carbonWriter object for writing data
 * it support write data from load disk
 *
 * @return carbonWriter object
 */
void build();
```

```
/**
 * Write an object to the file, the format of the object depends on the
 * implementation.
 * Note: This API is not thread safe
 */
void write(jobject obj);
```

```
/**
 * close the carbon Writer
 */
void close();
```

<a id="csdk-guide--carbonschemareader"></a>

### CarbonSchemaReader

```
/**
 * Constructor with jni env
 *
 * @param env  jni env
 */
CarbonSchemaReader(JNIEnv *env);
```

```
/**
 * Read schema from path,
 * path can be folder path, carbonindex file path, and carbondata file path
 * and will not check all files schema
 *
 * @param path file/folder path
 * @return schema
 */
jobject readSchema(char *path);
```

```
/**
 * Read schema from path,
 * path can be folder path, carbonindex file path, and carbondata file path
 * and user can decide whether check all files schema
 *
 * @param path carbon data path
 * @param validateSchema whether check all files schema
 * @return schema
 */
jobject readSchema(char *path, bool validateSchema);
```

```
/**
 * Read schema from path,
 * path can be folder path, carbonindex file path, and carbondata file path
 * and will not check all files schema
 *
 * @param path file/folder path
 * @param conf           configuration support, can set s3a AK,SK,
 *                       end point and other conf with this
 * @return schema
 */
jobject readSchema(char *path, Configuration conf);
```

```
/**
 * Read schema from path,
 * path can be folder path, carbonindex file path, and carbondata file path
 * and user can decide whether check all files schema
 *
 * @param path carbon data path
 * @param validateSchema whether check all files schema
 * @param conf           configuration support, can set s3a AK,SK,
 *                       end point and other conf with this
 * @return schema
 */
jobject readSchema(char *path, bool validateSchema, Configuration conf);
```

<a id="csdk-guide--schema"></a>

### Schema

```
/**
 * Constructor with jni env and carbon schema data
 *
 * @param env jni env
 * @param schema  carbon schema data
 */
Schema(JNIEnv *env, jobject schema);
```

```
/**
 * Get fields length of schema
 *
 * @return fields length
 */
int getFieldsLength();
```

```
/**
 * Get field name by ordinal
 *
 * @param ordinal the data index of carbon schema
 * @return ordinal field name
 */
char *getFieldName(int ordinal);
```

```
/**
 * Get  field data type name by ordinal
 *
 * @param ordinal the data index of carbon schema
 * @return ordinal field data type name
 */
char *getFieldDataTypeName(int ordinal);
```

```
/**
 * Get  array child element data type name by ordinal
 *
 * @param ordinal the data index of carbon schema
 * @return ordinal array child element data type name
 */
char *getArrayElementTypeName(int ordinal);
```

<a id="csdk-guide--carbonproperties"></a>

### CarbonProperties

```
/**
 * Constructor of CarbonProperties
 *
 * @param env JNI env
 */
CarbonProperties(JNIEnv *env);
```

```
/**
 * This method will be used to add a new property
 * 
 * @param key property key
 * @param value property value
 * @return CarbonProperties object
 */
jobject addProperty(char *key, char *value);
```

```
/**
 * This method will be used to get the properties value
 *
 * @param key property key
 * @return property value
 */
char *getProperty(char *key);
```

```
/**
 * This method will be used to get the properties value
 * if property is not present then it will return the default value
 *
 * @param key  property key
 * @param defaultValue  property default Value
 * @return
 */
char *getProperty(char *key, char *defaultValue);
```

[Top](#csdk-guide--top)

---

<a id="performance-tuning"></a>

<!-- source_url: https://carbondata.apache.org/performance-tuning.html -->

<!-- page_index: 19 -->

<a id="performance-tuning--useful-tips"></a>

# Useful Tips

This tutorial guides you to create CarbonData Tables and optimize performance.
The following sections will elaborate on the below topics :

- [Suggestions to create CarbonData Table](#performance-tuning--suggestions-to-create-carbondata-table)
- [Configuration for Optimizing Data Loading performance for Massive Data](#performance-tuning--configuration-for-optimizing-data-loading-performance-for-massive-data)
- [Optimizing Query Performance](#performance-tuning--configurations-for-optimizing-carbondata-performance)
- [Compaction Configurations for Optimizing CarbonData Query Performance](#performance-tuning--compaction-configurations-for-optimizing-carbondata-query-performance)

<a id="performance-tuning--suggestions-to-create-carbondata-table"></a>

## Suggestions to Create CarbonData Table

For example, the results of the analysis for table creation with dimensions ranging from 10 thousand to 10 billion rows and 100 to 300 columns have been summarized below.
The following table describes some of the columns from the table used.

- **Table Column Description**

| Column Name | Data Type | Cardinality | Attribution |
| --- | --- | --- | --- |
| msisdn | String | 30 million | Dimension |
| BEGIN\_TIME | BigInt | 10 Thousand | Dimension |
| HOST | String | 1 million | Dimension |
| Dime\_1 | String | 1 Thousand | Dimension |
| counter\_1 | Decimal | NA | Measure |
| counter\_2 | Numeric(20,0) | NA | Measure |
| ... | ... | NA | Measure |
| counter\_100 | Decimal | NA | Measure |

- **Put the frequently-used column filter in the beginning of SORT\_COLUMNS**

For example, MSISDN filter is used in most of the query then we must put the MSISDN as the first column in SORT\_COLUMNS property.
The create table command can be modified as suggested below :

```
create table carbondata_table(
  msisdn String,
  BEGIN_TIME bigint,
  HOST String,
  Dime_1 String,
  counter_1 Decimal,
  ...
  
  )STORED AS carbondata
  TBLPROPERTIES ('SORT_COLUMNS'='msisdn, Dime_1')
```

Now the query with MSISDN in the filter will be more efficient.

- **Put the frequently-used columns in the order of low to high cardinality in SORT\_COLUMNS**

If the table in the specified query has multiple columns which are frequently used to filter the results, it is suggested to put
the columns in the order of cardinality low to high in SORT\_COLUMNS configuration. This ordering of frequently used columns improves the compression ratio and
enhances the performance of queries with filter on these columns.

For example, if MSISDN, HOST and Dime\_1 are frequently-used columns, then the column order of table is suggested as
Dime\_1>HOST>MSISDN, because Dime\_1 has the lowest cardinality.
The create table command can be modified as suggested below :

```
create table carbondata_table(
    msisdn String,
    BEGIN_TIME bigint,
    HOST String,
    Dime_1 String,
    counter_1 Decimal,
    ...
    
    )STORED AS carbondata
    TBLPROPERTIES ('SORT_COLUMNS'='Dime_1, HOST, MSISDN')
```

- **For measure type columns with non high accuracy, replace Numeric(20,0) data type with Double data type**

For columns of measure type, not requiring high accuracy, it is suggested to replace Numeric data type with Double to enhance query performance.
The create table command can be modified as below :

```
  create table carbondata_table(
    Dime_1 String,
    BEGIN_TIME bigint,
    END_TIME bigint,
    HOST String,
    MSISDN String,
    counter_1 decimal,
    counter_2 double,
    ...
    )STORED AS carbondata
    TBLPROPERTIES ('SORT_COLUMNS'='Dime_1, HOST, MSISDN')
```

The result of performance analysis of test-case shows reduction in query execution time from 15 to 3 seconds, thereby improving performance by nearly 5 times.

- **Columns of incremental character should be re-arranged at the end of dimensions**

Consider the following scenario where data is loaded each day and the begin\_time is incremental for each load, it is suggested to put begin\_time at the end of dimensions.
Incremental values are efficient in using min/max index. The create table command can be modified as below :

```
create table carbondata_table(
  Dime_1 String,
  HOST String,
  MSISDN String,
  counter_1 double,
  counter_2 double,
  BEGIN_TIME bigint,
  END_TIME bigint,
  ...
  counter_100 double
  )STORED AS carbondata
  TBLPROPERTIES ('SORT_COLUMNS'='Dime_1, HOST, MSISDN')
```

**NOTE:**

- BloomFilter can be created to enhance performance for queries with precise equal/in conditions. You can find more information about it in BloomFilter index [document](#bloomfilter-index-guide).
- Lucene index can be created on string columns which has content of more length to enhance the query performance. You can find more information about it in Lucene index [document](#lucene-index-guide).
- Secondary index can be created based on the column position in main table(Recommended for right columns) and the queries should have filter on that column to improve the filter query performance. You can find more information about it in secondary index [document](#secondary-index-guide).
- Materialized view can be created to improve query performance provided the storage requirements and loading time is acceptable. You can find more information about it in materialized view [document](#mv-guide).

<a id="performance-tuning--configuration-for-optimizing-data-loading-performance-for-massive-data"></a>

## Configuration for Optimizing Data Loading performance for Massive Data

CarbonData supports large data load, in this process sorting data while loading consumes a lot of memory and disk IO and
this can result sometimes in "Out Of Memory" exception.
If you do not have much memory to use, then you may prefer to slow the speed of data loading instead of data load failure.
You can configure CarbonData by tuning following properties in carbon.properties file to get a better performance.

| Parameter | Default Value | Description/Tuning |
| --- | --- | --- |
| carbon.number.of.cores.while.loading | Default: 2. This value should be >= 2 | Specifies the number of cores used for data processing during data loading in CarbonData. |
| carbon.sort.size | Default: 100000. The value should be >= 1000. | Threshold to write local file in sort step when loading data |
| carbon.sort.file.write.buffer.size | Default: 16384. The value should be >= 10240 and <= 10485760. | CarbonData sorts and writes data to intermediate files to limit the memory usage. This configuration determines the buffer size to be used for reading and writing such files. |
| carbon.merge.sort.reader.thread | Default: 3 | Specifies the number of cores used for temp file merging during data loading in CarbonData. |
| carbon.merge.sort.prefetch | Default: true | You may want set this value to false if you have not enough memory |

For example, if there are 10 million records, and I have only 16 cores, 64 GB memory will be loaded to CarbonData table.
Using the default configuration always fail in sort step. Modify carbon.properties as suggested below:

```
carbon.merge.sort.reader.thread=1
carbon.sort.size=5000
carbon.sort.file.write.buffer.size=5000
carbon.merge.sort.prefetch=false
```

<a id="performance-tuning--configurations-for-optimizing-carbondata-performance"></a>

## Configurations for Optimizing CarbonData Performance

Recently we did some performance POC on CarbonData for Finance and telecommunication Field. It involved detailed queries and aggregation
scenarios. After the completion of POC, some of the configurations impacting the performance have been identified and tabulated below :

| Parameter | Location | Used For | Description | Tuning |
| --- | --- | --- | --- | --- |
| carbon.sort.intermediate.files.limit | spark/carbonlib/carbon.properties | Data loading | During the loading of data, local temp is used to sort the data. This number specifies the minimum number of intermediate files after which the merge sort has to be initiated. | Increasing the parameter to a higher value will improve the load performance. For example, when we increase the value from 20 to 100, it increases the data load performance from 35MB/S to more than 50MB/S. Higher values of this parameter consumes more memory during the load. |
| carbon.number.of.cores.while.loading | spark/carbonlib/carbon.properties | Data loading | Specifies the number of cores used for data processing during data loading in CarbonData. | If you have more number of CPUs, then you can increase the number of CPUs, which will increase the performance. For example if we increase the value from 2 to 4 then the CSV reading performance can increase about 1 times |
| carbon.compaction.level.threshold | spark/carbonlib/carbon.properties | Data loading and Querying | For minor compaction, specifies the number of segments to be merged in stage 1 and number of compacted segments to be merged in stage 2. | Each CarbonData load will create one segment, if every load is small in size it will generate many small files over a period of time impacting the query performance. Configuring this parameter will merge the small segment to one big segment which will sort the data and improve the performance. For Example in one telecommunication scenario, the performance improves about 2 times after minor compaction. |
| spark.sql.shuffle.partitions | spark/conf/spark-defaults.conf | Querying | The number of task started when spark shuffle. | The value can be 1 to 2 times as much as the executor cores. In an aggregation scenario, reducing the number from 200 to 32 reduced the query time from 17 to 9 seconds. |
| spark.executor.instances/spark.executor.cores/spark.executor.memory | spark/conf/spark-defaults.conf | Querying | The number of executors, CPU cores, and memory used for CarbonData query. | In the bank scenario, we provide the 4 CPUs cores and 15 GB for each executor which can get good performance. This 2 value does not mean more the better. It needs to be configured properly in case of limited resources. For example, In the bank scenario, it has enough CPU 32 cores each node but less memory 64 GB each node. So we cannot give more CPU but less memory. For example, when 4 cores and 12GB for each executor. It sometimes happens GC during the query which impact the query performance very much from the 3 second to more than 15 seconds. In this scenario need to increase the memory or decrease the CPU cores. |
| carbon.detail.batch.size | spark/carbonlib/carbon.properties | Querying | The buffer size to store records, returned from the block scan. | In limit scenario this parameter is very important. For example your query limit is 1000. But if we set this value to 3000 that means we get 3000 records from scan but spark will only take 1000 rows. So the 2000 remaining are useless. In one Finance test case after we set it to 100, in the limit 1000 scenario the performance increase about 2 times in comparison to if we set this value to 12000. |
| carbon.use.local.dir | spark/carbonlib/carbon.properties | Data loading | Whether use YARN local directories for multi-table load disk load balance | If this is set it to true CarbonData will use YARN local directories for multi-table load disk load balance, that will improve the data load performance. |
| carbon.sort.temp.compressor | spark/carbonlib/carbon.properties | Data loading | Specify the name of compressor to compress the intermediate sort temporary files during sort procedure in data loading. | The optional values are 'SNAPPY','GZIP','BZIP2','LZ4','ZSTD', and empty. Specially, empty means that Carbondata will not compress the sort temp files. This parameter will be useful if you encounter disk bottleneck. |
| carbon.load.skewedDataOptimization.enabled | spark/carbonlib/carbon.properties | Data loading | Whether to enable size based block allocation strategy for data loading. | When loading, carbondata will use file size based block allocation strategy for task distribution. It will make sure that all the executors process the same size of data -- It's useful if the size of your input data files varies widely, say 1MB to 1GB. |

Note: If your CarbonData instance is provided only for query, you may specify the property 'spark.speculation=true' which is in conf directory of spark.

<a id="performance-tuning--compaction-configurations-for-optimizing-carbondata-query-performance"></a>

## Compaction Configurations for Optimizing CarbonData Query Performance

CarbonData provides many configurations to tune the compaction behavior so that query peformance is improved.

Based on the number of cores available in the node, it is recommended to tune the configuration ***carbon.number.of.cores.while.compacting*** appropriately.Configuring a higher value will improve the overall compaction performance.

<table>
<tbody>
<tr>
<td>No</td>
<td> Data Loading frequency</td>
<td>Data Size of each load</td>
<td>Minor Compaction configuration</td>
<td> Major compaction configuration</td>
</tr>
<tr>
<td>1</td>
<td> Batch(Once is several Hours)</td>
<td>Big</td>
<td> Not Suggested</td>
<td>Configure Major Compaction size of 3-4 load size.Perform Major compaction once in a day</td>
</tr>
<tr>
<td rowspan="2">2</td>
<td rowspan="2"> Batch(Once in few minutes) </td>
<td>Big </td>
<td>
<p> Minor compaction (2,2).</p>
<p>Enable Auto compaction, if high rate data loading speed is not required or the time between loads is sufficient to run the compaction</p>
</td>
<td>Major compaction size of 10 load size.Perform Major compaction once in a day</td>
</tr>
<tr>
<td>Small</td>
<td>
<p>Minor compaction (6,6).</p>
<p>Enable Auto compaction, if high rate data loading speed is not required or the time between loads is sufficient to run the compaction</p>
</td>
<td>Major compaction size of 10 load size.Perform Major compaction once in a day</td>
</tr>
<tr>
<td>3</td>
<td> History data loaded as single load,incremental loads matches (1) or (2)</td>
<td>Big</td>
<td>
<p> Configure ALLOWED_COMPACTION_DAYS to exclude the History load.</p>
<p>Configure Minor compaction configuration based condition (1) or (2)</p>
</td>
<td> Configure Major compaction size smaller than the history load size.</td>
</tr>
<tr>
<td>4</td>
<td> There can be error in recent data loaded.Need reload sometimes</td>
<td> (1) or (2)</td>
<td>
<p> Configure COMPACTION_PRESERVE_SEGMENTS</p>
<p>to exclude the recent few segments from compacting.</p>
<p>Configure Minor compaction configuration based condition (1) or (2)</p>
</td>
<td>Same as (1) or (2) </td>
</tr>
</tbody>
</table>

[Top](#performance-tuning--top)

---

<a id="s3-guide"></a>

<!-- source_url: https://carbondata.apache.org/s3-guide.html -->

<!-- page_index: 20 -->

<a id="s3-guide--s3-guide"></a>

# S3 Guide

Object storage is the recommended storage format in cloud as it can support storing large data
files. S3 APIs are widely used for accessing object stores. This can be
used to store or retrieve data on Amazon cloud, Huawei Cloud(OBS) or on any other object
stores conforming to S3 API.
Storing data in cloud is advantageous as there are no restrictions on the size of
data and the data can be accessed from anywhere at any time.
Carbondata can support any Object Storage that conforms to Amazon S3 API.
Carbondata relies on Hadoop provided S3 filesystem APIs to access Object stores.

<a id="s3-guide--writing-to-object-storage"></a>

# Writing to Object Storage

To store carbondata files onto Object Store, `carbon.storelocation` property will have
to be configured with Object Store path in CarbonProperties file.

For example:

```
carbon.storelocation=s3a://mybucket/carbonstore
```

If the existing store location cannot be changed or only specific tables need to be stored
onto cloud object store, it can be done so by specifying the `location` option in the create
table DDL command.

For example:

```
CREATE TABLE IF NOT EXISTS db1.table1(col1 string, col2 int) STORED AS carbondata LOCATION 's3a://mybucket/carbonstore'
```

For more details on create table, Refer [DDL of CarbonData](#ddl-of-carbondata--create-table)

<a id="s3-guide--authentication"></a>

# Authentication

Authentication properties will have to be configured to store the carbondata files on to S3 location.

Authentication properties can be set in any of the following ways:

1. Set authentication properties in core-site.xml, refer
   [hadoop authentication document](https://hadoop.apache.org/docs/stable/hadoop-aws/tools/hadoop-aws/index.html#Authentication_properties)
2. Set authentication properties in spark-defaults.conf.

Example

```
spark.hadoop.fs.s3a.secret.key=123
spark.hadoop.fs.s3a.access.key=456
```

3. Pass authentication properties with spark-submit as configuration.

Example:

```
./bin/spark-submit \
--master yarn \
--conf spark.hadoop.fs.s3a.secret.key=123 \
--conf spark.hadoop.fs.s3a.access.key=456 \
--class=xxx
```

4. Set authentication properties to hadoop configuration object in sparkContext.

Example:

```
sparkSession.sparkContext.hadoopConfiguration.set("fs.s3a.secret.key", "123")
sparkSession.sparkContext.hadoopConfiguration.set("fs.s3a.access.key","456")
```

<a id="s3-guide--recommendations"></a>

# Recommendations

1. Object Storage like S3 does not support file leasing mechanism(supported by HDFS) that is
   required to take locks which ensure consistency between concurrent operations therefore, it is
   recommended to set the configurable lock path property([carbon.lock.path](#configuration-parameters--system-configuration))
   to a HDFS directory.
2. Concurrent data manipulation operations are not supported. Object stores follow eventual consistency semantics, i.e., any put request might take some time to reflect when trying to list. This behaviour causes the data read is always not consistent or not the latest.

[Top](#s3-guide--top)

---

<a id="index-server"></a>

<!-- source_url: https://carbondata.apache.org/index-server.html -->

<!-- page_index: 21 -->

<a id="index-server--distributed-index-server"></a>

# Distributed Index Server

<a id="index-server--background"></a>

## Background

Carbon currently prunes and caches all block/blocklet index information into the driver for
normal table, for Bloom/Lucene indexes the JDBC driver will launch a job to prune and cache in executors.

This causes the driver to become a bottleneck in the following ways:

1. If the cache size becomes huge(70-80% of the driver memory) then there can be excessive GC in
   the driver which can slow down the query and the driver may even go OutOfMemory.
2. LRU has to evict a lot of elements from the cache to accommodate the new objects which would
   in turn slow down the queries.
3. For bloom there is no guarantee that the next query goes to the same executor to reuse the cache
   and hence cache could be duplicated in multiple executors.
4. Multiple JDBC drivers need to maintain their own copy of the cache.

Distributed Index Cache Server aims to solve the above mentioned problems.

<a id="index-server--distribution"></a>

## Distribution

When enabled, any query on a carbon table will be routed to the index server service in form of
a request. The request will consist of the table name, segments, filter expression and other
information used for pruning.

In IndexServer service a pruning RDD is fired which will take care of the pruning for that
request. This RDD will be creating tasks based on the number of segments that are applicable for
pruning. It can happen that the user has specified segments to access for that table, so only the
specified segments would be applicable for pruning. Refer: [query-data-with-specified-segments](https://carbondata.apache.org/segment-management-on-carbondata.html#query-data-with-specified-segments).
IndexServer driver would have 2 important tasks, distributing the segments equally among the
available executors and keeping track of the executor where the segment is cached.

To achieve this 2 separate mappings would be maintained as follows.

1. segment to executor location:
   This mapping will be maintained for each table and will enable the index server to track the
   cache location for each segment.
2. Cache size held by each executor:
   This mapping will be used to distribute the segments equally(on the basis of size) among the executors.

Once a request is received each segment would be iterated over and
checked against tableToExecutorMapping to find if a executor is already
assigned. If a mapping already exists then it means that most
probably(if not evicted by LRU) the segment is already cached in that
executor and the task for that segment has to be fired on this executor.

If mapping is not found then first check executorToCacheMapping against
the available executor list to find if any unassigned executor is
present and use that executor for the current segment. If all the
executors are assigned with some segment then find the least loaded
executor on the basis of size.

Initially the segment index size would be used to distribute the
segments fairly among the executor because the actual cache size would
be known to the driver only when the segments are cached and appropriate
information is returned to the driver.

**NOTE:** In case of legacy segment(version: 1.1) the index size is not available
therefore all the legacy segments would be processed in a round robin
fashion.

After the job is completed the tasks would return the cache size held by
each executor which would be updated to the executorToCacheMapping and
the pruned blocklets which would be further used for result fetching.

**Note:** Multiple JDBC drivers can connect to the index server to use the cache.

<a id="index-server--enabling-size-based-distribution-for-legacy-stores"></a>

## Enabling Size based distribution for Legacy stores

The default round robin based distribution causes unequal distribution of cache among the executors, which can cause any one of the executors to be bloated with too much cache resulting in performance degrade.
This problem can be solved by running the `upgrade_segment` command which will fill the data size values for each segment in the tablestatus file. Any cache loaded after this can use the traditional size based distribution.

<a id="index-server--example"></a>

#### Example

```
alter table table1 compact 'upgrade_segment';
```

<a id="index-server--reallocation-of-executor"></a>

## Reallocation of executor

In case executor(s) become dead/unavailable then the segments that were
earlier being handled by those would be reassigned to some other
executor using the distribution logic.

**Note:** Cache loading would be done again in the new executor for the
current query.

<a id="index-server--metacache-ddl"></a>

## MetaCache DDL

The show metacache DDL has a new column called cache location will indicate whether the cache is
from executor or driver. To drop cache the user has to enable/disable the index server using the
dynamic configuration to clear the cache of the desired location.

Refer: [MetaCacheDDL](#ddl-of-carbondata--cache)

<a id="index-server--fallback"></a>

## Fallback

In case of any failure the index server would fallback to embedded mode
which means that the JDBCServer would take care of distributed pruning.
A similar job would be fired by the JDBCServer which would take care of
pruning using its own executors. If for any reason the embedded mode
also fails to prune the indexes then the job would be passed on to
driver.

**NOTE:** In case of embedded mode a job would be fired after pruning to clear the
cache as data cached in JDBCServer executors would be of no use.

<a id="index-server--writing-splits-to-a-file"></a>

## Writing splits to a file

If the response is too huge then it is better to write the splits to a file so that the driver can
read this file and create the splits. This can be controlled using the property 'carbon.index.server
.inmemory.serialization.threshold.inKB'. By default, the minimum value for this property is 0, meaning that no matter how small the splits are they would be written to the file. Maximum is
102400KB which will mean if the size of the splits for a executor cross this value then they would
be written to file.

The user can set the location for these files by using 'carbon.indexserver.temp.path'. By default
the files are written in the path /tmp/indexservertmp.

<a id="index-server--prepriming"></a>

## Prepriming

As each query is responsible for caching the pruned indexes, thus a lot of execution time is wasted in reading the
files and caching the datmaps for the first query.
To avoid this problem we have introduced Pre-Priming which allows each data manipulation command like load, insert etc
to fire a request to the index server to load the corresponding segments into the index server.
When index server receives a request it checks whether the request is for pre-priming, if it is then the request is
processed in a new thread, and a dummy response is immediately returned to the client.
Since pre-priming acts as an async call, it does not have any negative performance impacts.

The user can enable prepriming by using 'carbon.indexserver.enable.prepriming' = 'true/false'. By default this is set as false.

<a id="index-server--configurations"></a>

## Configurations

<a id="index-server--carbon.properties-jdbcserver"></a>

##### carbon.properties(JDBCServer)

| Name | Default Value | Description |
| --- | --- | --- |
| carbon.enable.index.server | false | Enable the use of index server for pruning for the whole application. |
| carbon.index.server.ip | NA | Specify the IP/HOST on which the server is started. Better to specify the private IP. |
| carbon.index.server.port | NA | The port on which the index server is started. |
| carbon.disable.index.server.fallback | false | Whether to enable/disable fallback for index server. Should be used for testing purposes only. Refer: [Fallback](#index-server--fallback) |
| carbon.index.server.max.jobname.length | NA | The max length of the job to show in the index server service UI. For bigger queries this may impact performance as the whole string would be sent from JDBCServer to IndexServer. |
| carbon.indexserver.enable.prepriming | false | Enable the use of prepriming in the Index Server to improve the performance of first time query. |

<a id="index-server--carbon.properties-indexserver"></a>

##### carbon.properties(IndexServer)

| Name | Default Value | Description |
| --- | --- | --- |
| carbon.index.server.ip | NA | Specify the IP/HOST on which the server would be started. Better to specify the private IP. |
| carbon.index.server.port | NA | The port on which the index server has to be started. |
| carbon.index.server.max.worker.threads | 500 | Number of RPC handlers to open for accepting the requests from JDBC driver. Max accepted value is Integer.Max. Refer: [Hive configuration](https://github.com/apache/hive/blob/master/common/src/java/org/apache/hadoop/hive/conf/HiveConf.java#L3441) |
| carbon.max.executor.lru.cache.size | NA | Maximum memory **(in MB)** upto which the executor process can cache the data (Indexes and reverse dictionary values). Only integer values greater than 0 are accepted. **NOTE:** Mandatory for the user to set. |
| carbon.index.server.max.jobname.length | 50 | The max length of the job to show in the index server application UI. For bigger queries this may impact performance as the whole string would be sent from JDBCServer to IndexServer. |
| carbon.max.executor.threads.for.block.pruning | 4 | max executor threads used for block pruning. |
| carbon.index.server.inmemory.serialization.threshold.inKB | 300 | Max in memory serialization size after reaching threshold data will be written to file. Min value that the user can set is 0KB and max is 102400KB. |
| carbon.indexserver.temp.path | /tmp/indexservertmp folder | The folder to write the split files if in memory index cache size for network transfers crossed the 'carbon.index.server.inmemory.serialization.threshold.inKB' limit. |

<a id="index-server--spark-defaults.conf-only-for-secure-mode"></a>

##### spark-defaults.conf(only for secure mode)

| Name | Default Value | Description |
| --- | --- | --- |
| spark.dynamicAllocation.enabled | true | Set to false, so that spark does not kill the executor, If executors are killed, cache would be lost. Applicable only for Index Server. |
| spark.yarn.principal | NA | Should be set to the same user used for JDBCServer. Required only for IndexServer. |
| spark.yarn.keytab | NA | Should be set to the same as JDBCServer. |

<a id="index-server--spark-defaults.conf-non-secure-mode"></a>

##### spark-defaults.conf(non-secure mode)

| Name | Default Value | Description |
| --- | --- | --- |
| spark.dynamicAllocation.enabled | true | Set to false, so that spark does not kill the executor, If executors are killed, cache would be lost. Applicable only for Index Server. |

**NOTE:** Its better to create a new user for indexserver principal, that will authenticate the user to access the index server and no other service.

<a id="index-server--core-site.xml"></a>

##### core-site.xml

| Name | Default Value | Description |
| --- | --- | --- |
| ipc.client.rpc-timeout.ms | NA | Set the above property to some appropriate value based on your estimated query time. The best option is to set this to the same value as spark.network.timeout. |
| hadoop.security.authorization | false | Property to enable the hadoop security which is required only on the server side. |
| hadoop.proxyuser.<indexserver\_user>.users | NA | Property to set Proxy User list for which IndexServer permission were to be given ,check <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/Superusers.html> |
| hadoop.proxyuser.<indexserver\_user>.hosts | NA | Property to set hosts list for which IndexServer permission were to be given ,check <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/Superusers.html> |
| hadoop.proxyuser.<indexserver\_user>.groups | NA | Property to set groups list for which IndexServer permission to be given ,check <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/Superusers.html> |
| security.indexserver.protocol.acl | \* | Property to set List of User to be Authorized for Other than proxy Spark Application |

<a id="index-server--dynamic-properties-set-command"></a>

##### dynamic-properties(set command)

| Name | Default Value | Description |
| --- | --- | --- |
| carbon.enable.index.server | false | Enable the use of index server for pruning for the current session. |
| carbon.enable.index.server.dbName.tableName | false | Enable the use of index server for the specified table in the current session. |

<a id="index-server--starting-the-server"></a>

## Starting the Server

```
./bin/spark-submit --master [yarn/local] --[optional parameters] --class org.apache.carbondata.indexserver.IndexServer [path to carbondata-spark-<version>.jar]
```

Or

```
./sbin/start-indexserver.sh --master yarn --num-executors 2 /<absolute path>/carbondata-spark-<version>.jar
```

<a id="index-server--faq"></a>

## FAQ

Q. **Index Server is throwing Large response size exception.**

A. The exception would show the size of response it is trying to send over the
network. Use ipc.maximum.response.length to a value bigger than the
response size.

Q. **Unable to connect to index server**

A. Check whether the carbon.properties configurations are set in JDBCServer as well as the index
server.

Q. **IndexServer is throwing FileNotFoundException for index files.**

A. Check whether the Index server and JDBCServer are connected to the
same namenode or not. And the store should be shared by both

Q. **OutOfMemoryException in DirectMemoryBuffer**

A. Increase -XX:MaxDirectMemorySize in driver.extraJavaOptions to
accommodate the large response in driver.

[Top](#index-server--top)

---

<a id="prestodb-guide"></a>

<!-- source_url: https://carbondata.apache.org/prestodb-guide.html -->

<!-- page_index: 22 -->

<a id="prestodb-guide--prestodb-guide"></a>

# Prestodb guide

This tutorial provides a quick introduction to using current integration/presto module.

[Presto Multinode Cluster Setup for Carbondata](#prestodb-guide--presto-multinode-cluster-setup-for-carbondata)

[Presto Single Node Setup for Carbondata](#prestodb-guide--presto-single-node-setup-for-carbondata)

<a id="prestodb-guide--presto-multinode-cluster-setup-for-carbondata"></a>

## Presto Multinode Cluster Setup for Carbondata

<a id="prestodb-guide--installing-presto"></a>

### Installing Presto

To know about which version of presto is supported by this version of carbon, visit
<https://github.com/apache/carbondata/blob/master/pom.xml>
and look for `<presto.version>` inside `prestodb` profile.

*Example:*
`<presto.version>0.217</presto.version>`
This means current version of carbon supports presto 0.217 version.

*Note:*
Currently carbondata supports only one version of presto, cannot handle multiple versions at same time. If user wish to use older version of presto, then need to use older version of carbon (other old branches, say branch-1.5 and check the supported presto version in it's pom.xml file in integration/presto/)

1. Download that version of Presto (say 0.217) using below command:

```
wget https://repo1.maven.org/maven2/com/facebook/presto/presto-server/0.217/presto-server-0.217.tar.gz
```

2. Extract Presto tar file: `tar zxvf presto-server-0.217.tar.gz`.
3. Download the Presto CLI of the same presto server version (say 0.217) for the coordinator and name it presto.

```
  wget https://repo1.maven.org/maven2/com/facebook/presto/presto-cli/0.217/presto-cli-0.217-executable.jar

  mv presto-cli-0.217-executable.jar presto

  chmod +x presto
```

<a id="prestodb-guide--create-configuration-files"></a>

### Create Configuration Files

1. Create `etc` folder in presto-server-0.217 directory.
2. Create `config.properties`, `jvm.config`, `log.properties`, and `node.properties` files.
3. Install uuid to generate a node.id.


```
sudo apt-get install uuid

uuid
```

<a id="prestodb-guide--contents-of-your-node.properties-file"></a>

##### Contents of your node.properties file

```
node.environment=production
node.id=<generated uuid>
node.data-dir=/home/ubuntu/data
```

<a id="prestodb-guide--contents-of-your-jvm.config-file"></a>

##### Contents of your jvm.config file

```
-server
-Xmx16G
-XX:+UseG1GC
-XX:G1HeapRegionSize=32M
-XX:+UseGCOverheadLimit
-XX:+ExplicitGCInvokesConcurrent
-XX:+HeapDumpOnOutOfMemoryError
-XX:OnOutOfMemoryError=kill -9 %p
```

<a id="prestodb-guide--contents-of-your-log.properties-file"></a>

##### Contents of your log.properties file

```
com.facebook.presto=INFO
```

The default minimum level is `INFO`. There are four levels: `DEBUG`, `INFO`, `WARN` and `ERROR`.

<a id="prestodb-guide--coordinator-configurations"></a>

## Coordinator Configurations

<a id="prestodb-guide--contents-of-your-config.properties"></a>

##### Contents of your config.properties

```
coordinator=true
node-scheduler.include-coordinator=false
http-server.http.port=8086
query.max-memory=5GB
query.max-total-memory-per-node=5GB
query.max-memory-per-node=3GB
memory.heap-headroom-per-node=1GB
discovery-server.enabled=true
discovery.uri=<coordinator_ip>:8086
```

The options `node-scheduler.include-coordinator=false` and `coordinator=true` indicate that the node is the coordinator and tells the coordinator not to do any of the computation work itself and to use the workers.

> [!NOTE]
> : We recommend setting `query.max-memory-per-node` to half of the JVM config max memory, though if your workload is highly concurrent, you may want to use a lower value for `query.max-memory-per-node`.

Also relation between below two configuration-properties should be like:
If, `query.max-memory-per-node=30GB`
Then, `query.max-memory=<30GB * number of nodes>`.

<a id="prestodb-guide--worker-configurations"></a>

### Worker Configurations

<a id="prestodb-guide--contents-of-your-config.properties-2"></a>

##### Contents of your config.properties

```
coordinator=false
http-server.http.port=8086
query.max-memory=5GB
query.max-memory-per-node=2GB
discovery.uri=<coordinator_ip>:8086
```

> [!NOTE]
> : `jvm.config` and `node.properties` files are same for all the nodes (worker + coordinator). All the nodes should have different `node.id`.

<a id="prestodb-guide--catalog-configurations"></a>

### Catalog Configurations

1. Create a folder named `catalog` in etc directory of presto on all the nodes of the cluster including the coordinator.

<a id="prestodb-guide--configuring-carbondata-in-presto"></a>

##### Configuring Carbondata in Presto

1. Create a file named `carbondata.properties` in the `catalog` folder and set the required properties on all the nodes.
2. As carbondata connector extends hive connector all the configurations(including S3) is same as hive connector.
   Just replace the connector name in hive configuration and copy same to carbondata.properties
   `connector.name = carbondata`

<a id="prestodb-guide--add-plugins"></a>

### Add Plugins

1. Create a directory named `carbondata` in plugin directory of presto.
2. Copy all the jars from ../integration/presto/target/carbondata-presto-X.Y.Z-SNAPSHOT to `plugin/carbondata` directory on all nodes.

<a id="prestodb-guide--start-presto-server-on-all-nodes"></a>

### Start Presto Server on all nodes

```
./presto-server-0.217/bin/launcher start
```

To run it as a background process.

```
./presto-server-0.217/bin/launcher run
```

To run it in foreground.

<a id="prestodb-guide--start-presto-cli"></a>

### Start Presto CLI

To connect to carbondata catalog use the following command:

```
./presto --server <coordinator_ip>:8086 --catalog carbondata --schema <schema_name>
```

Execute the following command to ensure the workers are connected.

```
select * from system.runtime.nodes;
```

Now you can use the Presto CLI on the coordinator to query data sources in the catalog using the Presto workers.

<a id="prestodb-guide--presto-single-node-setup-for-carbondata"></a>

## Presto Single Node Setup for Carbondata

<a id="prestodb-guide--config-presto-server"></a>

### Config presto server

- Download presto server (0.217 is suggested and supported) : <https://repo1.maven.org/maven2/com/facebook/presto/presto-server/>
- Finish presto configuration following <https://prestodb.io/docs/current/installation/deployment.html>.
  A configuration example:

**config.properties**

```
coordinator=true
node-scheduler.include-coordinator=true
http-server.http.port=8086
query.max-memory=5GB
query.max-total-memory-per-node=5GB
query.max-memory-per-node=3GB
memory.heap-headroom-per-node=1GB
discovery-server.enabled=true
discovery.uri=http://localhost:8086
task.max-worker-threads=4
optimizer.dictionary-aggregation=true
optimizer.optimize-hash-generation = false  
```

**jvm.config**

```
-server
-Xmx4G
-XX:+UseG1GC
-XX:G1HeapRegionSize=32M
-XX:+UseGCOverheadLimit
-XX:+ExplicitGCInvokesConcurrent
-XX:+HeapDumpOnOutOfMemoryError
-XX:OnOutOfMemoryError=kill -9 %p
-XX:+TraceClassLoading
-Dcarbon.properties.filepath=<path>/carbon.properties
```

`carbon.properties.filepath` property is used to set the carbon.properties file path and it is recommended to set otherwise some features may not work. Please check the above example.

**log.properties**

```
com.facebook.presto=DEBUG
com.facebook.presto.server.PluginManager=DEBUG
```

**node.properties**

```
node.environment=carbondata
node.id=ffffffff-ffff-ffff-ffff-ffffffffffff
node.data-dir=/Users/apple/DEMO/presto_test/data
```

- Config carbondata-connector for presto

  Firstly: Compile carbondata, including carbondata-presto integration module


```
$ git clone https://github.com/apache/carbondata
$ cd carbondata
$ mvn -DskipTests -P{spark-version} -P{prestodb/prestosql} -Dspark.version={spark-version-number} -Dhadoop.version={hadoop-version-number} clean package
```

  Replace the spark and hadoop version with the version used in your cluster.
  For example, use prestodb profile and
  if you are using Spark 2.4.5, you would like to compile using:


```
mvn -DskipTests -Pspark-2.4 -Pprestodb -Dspark.version=2.4.5 -Dhadoop.version=2.7.2 clean package
```

  Secondly: Create a folder named 'carbondata' under $PRESTO\_HOME$/plugin and
  copy all jars from carbondata/integration/presto/target/carbondata-presto-x.x.x-SNAPSHOT
  to $PRESTO\_HOME$/plugin/carbondata

  **NOTE:** Copying assemble jar alone will not work, need to copy all jars from integration/presto/target/carbondata-presto-x.x.x-SNAPSHOT

  Thirdly: Create a carbondata.properties file under $PRESTO\_HOME$/etc/catalog/ containing the following contents:


```
connector.name=carbondata
hive.metastore.uri=thrift://<host>:<port>
```

  Carbondata becomes one of the supported format of presto hive plugin, so the configurations and setup is similar to hive connector of presto.
  Please refer <https://prestodb.io/docs/current/connector/hive.html> for more details.


> [!NOTE]
> : Since carbon can work only with hive metastore, it is necessary that spark also connects to same metastore db for creating tables and updating tables.
> All the operations done on spark will be reflected in presto immediately.
> It is mandatory to create Carbon tables from spark using CarbonData 1.5.2 or greater version since input/output formats are updated in carbon table properly from this version.

<a id="prestodb-guide--connecting-to-carbondata-store-on-s3"></a>

#### Connecting to carbondata store on s3

- In case you want to query carbonstore on S3 using S3A api put following additional properties inside $PRESTO\_HOME$/etc/catalog/carbondata.properties


```
 Required properties

 hive.s3.aws-access-key={value}
 hive.s3.aws-secret-key={value}
 
 Optional properties
 
 hive.s3.endpoint={value}
```

  Please refer <https://prestodb.io/docs/current/connector/hive.html> for more details on S3 integration.

<a id="prestodb-guide--generate-carbondata-file"></a>

### Generate CarbonData file

Please refer to quick start: <https://github.com/apache/carbondata/blob/master/docs/quick-start-guide.html>.
Load data statement in Spark can be used to create carbondata tables. And then you can easily find the created
carbondata files.

<a id="prestodb-guide--query-carbondata-in-cli-of-presto"></a>

### Query carbondata in CLI of presto

- Download presto cli client of version 0.217 : <https://repo1.maven.org/maven2/com/facebook/presto/presto-cli>
- Start CLI:


```
$ ./presto --server localhost:8086 --catalog carbondata --schema default
```

  Replace the hostname, port and schema name with your own.

<a id="prestodb-guide--supported-features-of-presto-carbon"></a>

### Supported features of presto carbon

Presto carbon only supports reading the carbon table which is written by spark carbon or carbon SDK.
During reading, it supports the non-distributed indexes like block index and bloom index.
It doesn't support Materialized View as it needs query plan to be changed and presto does not allow it.
Also, Presto carbon supports streaming segment read from streaming table created by spark.

[Top](#prestodb-guide--top)

---

<a id="prestosql-guide"></a>

<!-- source_url: https://carbondata.apache.org/prestosql-guide.html -->

<!-- page_index: 23 -->

<a id="prestosql-guide--prestosql-guide"></a>

# Prestosql guide

This tutorial provides a quick introduction to using current integration/presto module.

[Presto Multinode Cluster Setup for Carbondata](#prestosql-guide--presto-multinode-cluster-setup-for-carbondata)

[Presto Single Node Setup for Carbondata](#prestosql-guide--presto-single-node-setup-for-carbondata)

<a id="prestosql-guide--presto-multinode-cluster-setup-for-carbondata"></a>

## Presto Multinode Cluster Setup for Carbondata

<a id="prestosql-guide--installing-presto"></a>

### Installing Presto

To know about which version of presto is supported by this version of carbon, visit
<https://github.com/apache/carbondata/blob/master/pom.xml>
and look for `<presto.version>` inside `prestosql` profile.

*Example:*
`<presto.version>316</presto.version>`
This means current version of carbon supports presto 316 version.

*Note:*
Currently carbondata supports only one version of presto, cannot handle multiple versions at same time. If user wish to use older version of presto, then need to use older version of carbon (other old branches, say branch-1.5 and check the supported presto version in it's pom.xml file in integration/presto/)

1. Download that version of Presto (say 316) using below command:

```
wget https://repo1.maven.org/maven2/io/prestosql/presto-server/316/presto-server-316.tar.gz
```

2. Extract Presto tar file: `tar zxvf presto-server-316.tar.gz`.
3. Download the Presto CLI of the same presto server version (say 316) for the coordinator and name it presto.

```
  wget https://repo1.maven.org/maven2/io/prestosql/presto-cli/316/presto-cli-316-executable.jar

  mv presto-cli-316-executable.jar presto

  chmod +x presto
```

<a id="prestosql-guide--create-configuration-files"></a>

### Create Configuration Files

1. Create `etc` folder in presto-server-316 directory.
2. Create `config.properties`, `jvm.config`, `log.properties`, and `node.properties` files.
3. Install uuid to generate a node.id.


```
sudo apt-get install uuid

uuid
```

<a id="prestosql-guide--contents-of-your-node.properties-file"></a>

##### Contents of your node.properties file

```
node.environment=production
node.id=<generated uuid>
node.data-dir=/home/ubuntu/data
```

<a id="prestosql-guide--contents-of-your-jvm.config-file"></a>

##### Contents of your jvm.config file

```
-server
-Xmx16G
-XX:+UseG1GC
-XX:G1HeapRegionSize=32M
-XX:+UseGCOverheadLimit
-XX:+ExplicitGCInvokesConcurrent
-XX:+HeapDumpOnOutOfMemoryError
-XX:OnOutOfMemoryError=kill -9 %p
```

<a id="prestosql-guide--contents-of-your-log.properties-file"></a>

##### Contents of your log.properties file

```
io.prestosql=INFO
```

The default minimum level is `INFO`. There are four levels: `DEBUG`, `INFO`, `WARN` and `ERROR`.

<a id="prestosql-guide--coordinator-configurations"></a>

## Coordinator Configurations

<a id="prestosql-guide--contents-of-your-config.properties"></a>

##### Contents of your config.properties

```
coordinator=true
node-scheduler.include-coordinator=false
http-server.http.port=8086
query.max-memory=5GB
query.max-total-memory-per-node=5GB
query.max-memory-per-node=3GB
memory.heap-headroom-per-node=1GB
discovery-server.enabled=true
discovery.uri=<coordinator_ip>:8086
```

The options `node-scheduler.include-coordinator=false` and `coordinator=true` indicate that the node is the coordinator and tells the coordinator not to do any of the computation work itself and to use the workers.

> [!NOTE]
> : We recommend setting `query.max-memory-per-node` to half of the JVM config max memory, though if your workload is highly concurrent, you may want to use a lower value for `query.max-memory-per-node`.

Also relation between below two configuration-properties should be like:
If, `query.max-memory-per-node=30GB`
Then, `query.max-memory=<30GB * number of nodes>`.

<a id="prestosql-guide--worker-configurations"></a>

### Worker Configurations

<a id="prestosql-guide--contents-of-your-config.properties-2"></a>

##### Contents of your config.properties

```
coordinator=false
http-server.http.port=8086
query.max-memory=5GB
query.max-memory-per-node=2GB
discovery.uri=<coordinator_ip>:8086
```

> [!NOTE]
> : `jvm.config` and `node.properties` files are same for all the nodes (worker + coordinator). All the nodes should have different `node.id`.

<a id="prestosql-guide--catalog-configurations"></a>

### Catalog Configurations

1. Create a folder named `catalog` in etc directory of presto on all the nodes of the cluster including the coordinator.

<a id="prestosql-guide--configuring-carbondata-in-presto"></a>

##### Configuring Carbondata in Presto

1. Create a file named `carbondata.properties` in the `catalog` folder and set the required properties on all the nodes.
2. As carbondata connector extends hive connector all the configurations(including S3) is same as hive connector.
   Just replace the connector name in hive configuration and copy same to carbondata.properties
   `connector.name = carbondata`

<a id="prestosql-guide--add-plugins"></a>

### Add Plugins

1. Create a directory named `carbondata` in plugin directory of presto.
2. Copy all the jars from ../integration/presto/target/carbondata-presto-X.Y.Z-SNAPSHOT to `plugin/carbondata` directory on all nodes.

<a id="prestosql-guide--start-presto-server-on-all-nodes"></a>

### Start Presto Server on all nodes

```
./presto-server-316/bin/launcher start
```

To run it as a background process.

```
./presto-server-316/bin/launcher run
```

To run it in foreground.

<a id="prestosql-guide--start-presto-cli"></a>

### Start Presto CLI

To connect to carbondata catalog use the following command:

```
./presto --server <coordinator_ip>:8086 --catalog carbondata --schema <schema_name>
```

Execute the following command to ensure the workers are connected.

```
select * from system.runtime.nodes;
```

Now you can use the Presto CLI on the coordinator to query data sources in the catalog using the Presto workers.

<a id="prestosql-guide--presto-single-node-setup-for-carbondata"></a>

## Presto Single Node Setup for Carbondata

<a id="prestosql-guide--config-presto-server"></a>

### Config presto server

- Download presto server (316 is suggested and supported) : <https://repo1.maven.org/maven2/io/prestosql/presto-server/>
- Finish presto configuration following <https://prestosql.io/docs/current/installation/deployment.html>.
  A configuration example:

**config.properties**

```
coordinator=true
node-scheduler.include-coordinator=true
http-server.http.port=8086
query.max-memory=5GB
query.max-total-memory-per-node=5GB
query.max-memory-per-node=3GB
memory.heap-headroom-per-node=1GB
discovery-server.enabled=true
discovery.uri=http://localhost:8086
task.max-worker-threads=4
optimizer.dictionary-aggregation=true
optimizer.optimize-hash-generation = false  
```

**jvm.config**

```
-server
-Xmx4G
-XX:+UseG1GC
-XX:G1HeapRegionSize=32M
-XX:+UseGCOverheadLimit
-XX:+ExplicitGCInvokesConcurrent
-XX:+HeapDumpOnOutOfMemoryError
-XX:OnOutOfMemoryError=kill -9 %p
-XX:+TraceClassLoading
-Dcarbon.properties.filepath=<path>/carbon.properties
```

`carbon.properties.filepath` property is used to set the carbon.properties file path and it is recommended to set otherwise some features may not work. Please check the above example.

**log.properties**

```
io.prestosql=DEBUG
io.prestosql.server.PluginManager=DEBUG
```

**node.properties**

```
node.environment=carbondata
node.id=ffffffff-ffff-ffff-ffff-ffffffffffff
node.data-dir=/Users/apple/DEMO/presto_test/data
```

- Config carbondata-connector for presto

  Firstly: Compile carbondata, including carbondata-presto integration module


```
$ git clone https://github.com/apache/carbondata
$ cd carbondata
$ mvn -DskipTests -P{spark-version} -P{prestodb/prestosql} -Dspark.version={spark-version-number} -Dhadoop.version={hadoop-version-number} clean package
```

  Replace the spark and hadoop version with the version used in your cluster.
  For example, use prestosql profile and
  if you are using Spark 2.4.5, you would like to compile using:


```
mvn -DskipTests -Pspark-2.4 -Pprestosql -Dspark.version=2.4.5 -Dhadoop.version=2.7.2 clean package
```

  Secondly: Create a folder named 'carbondata' under $PRESTO\_HOME$/plugin and
  copy all jars from carbondata/integration/presto/target/carbondata-presto-x.x.x-SNAPSHOT
  to $PRESTO\_HOME$/plugin/carbondata

  **NOTE:** Copying assemble jar alone will not work, need to copy all jars from integration/presto/target/carbondata-presto-x.x.x-SNAPSHOT

  Thirdly: Create a carbondata.properties file under $PRESTO\_HOME$/etc/catalog/ containing the following contents:


```
connector.name=carbondata
hive.metastore.uri=thrift://<host>:<port>
```

  Carbondata becomes one of the supported format of presto hive plugin, so the configurations and setup is similar to hive connector of presto.
  Please refer <https://prestosql.io/docs/current/connector/hive.html> for more details.


> [!NOTE]
> : Since carbon can work only with hive metastore, it is necessary that spark also connects to same metastore db for creating tables and updating tables.
> All the operations done on spark will be reflected in presto immediately.
> It is mandatory to create Carbon tables from spark using CarbonData 1.5.2 or greater version since input/output formats are updated in carbon table properly from this version.

<a id="prestosql-guide--connecting-to-carbondata-store-on-s3"></a>

#### Connecting to carbondata store on s3

- In case you want to query carbonstore on S3 using S3A api put following additional properties inside $PRESTO\_HOME$/etc/catalog/carbondata.properties


```
 Required properties

 hive.s3.aws-access-key={value}
 hive.s3.aws-secret-key={value}
 
 Optional properties
 
 hive.s3.endpoint={value}
```

  Please refer <https://prestosql.io/docs/current/connector/hive.html> for more details on S3 integration.

<a id="prestosql-guide--generate-carbondata-file"></a>

### Generate CarbonData file

Please refer to quick start: <https://github.com/apache/carbondata/blob/master/docs/quick-start-guide.html>.
Load data statement in Spark can be used to create carbondata tables. And then you can easily find the created
carbondata files.

<a id="prestosql-guide--query-carbondata-in-cli-of-presto"></a>

### Query carbondata in CLI of presto

- Download presto cli client of version 316 : <https://repo1.maven.org/maven2/io/prestosql/presto-cli/>
- Start CLI:


```
$ ./presto --server localhost:8086 --catalog carbondata --schema default
```

  Replace the hostname, port and schema name with your own.

<a id="prestosql-guide--supported-features-of-presto-carbon"></a>

### Supported features of presto carbon

Presto carbon only supports reading the carbon table which is written by spark carbon or carbon SDK.
During reading, it supports the non-distributed index like block index and bloom index.
It doesn't support Materialized View as it needs query plan to be changed and presto does not allow it.
Also, Presto carbon supports streaming segment read from streaming table created by spark.

[Top](#prestosql-guide--top)

---

<a id="flink-integration-guide"></a>

<!-- source_url: https://carbondata.apache.org/flink-integration-guide.html -->

<!-- page_index: 24 -->

<a id="flink-integration-guide--carbon-flink-integration-guide"></a>

# Carbon Flink Integration Guide

<a id="flink-integration-guide--usage-scenarios"></a>

## Usage scenarios

The CarbonData flink integration module is used to connect Flink and Carbon. The module provides
a set of Flink BulkWriter implementations (CarbonLocalWriter and CarbonS3Writer). The data is processed
by the Flink, and finally written into the stage directory of the target table by the CarbonXXXWriter.

By default, those data in table stage directory, can not be immediately queried, those data can be queried
after the `INSERT INTO $tableName STAGE` command is executed.

Since the flink data written to carbon is endless, in order to ensure the visibility of data
and the controllable amount of data processed during the execution of each insert form stage command, the user should execute the insert from stage command in a timely manner.

The execution interval of the insert form stage command should take the data visibility requirements
of the actual business and the flink data traffic. When the data visibility requirements are high
or the data traffic is large, the execution interval should be appropriately shortened.

A typical scenario is that the data is cleaned and preprocessed by Flink, and then written to Carbon, for subsequent analysis and queries.

<a id="flink-integration-guide--usage-description"></a>

## Usage description

<a id="flink-integration-guide--writing-process"></a>

### Writing process

Typical flink stream: `Source -> Process -> Output(Carbon Writer Sink)`

Pseudo code and description:

```
  // Import dependencies.
  import java.util.Properties
  import org.apache.carbon.flink.CarbonWriterFactory
  import org.apache.carbon.flink.ProxyFileSystem
  import org.apache.carbondata.core.constants.CarbonCommonConstants
  import org.apache.flink.api.common.restartstrategy.RestartStrategies
  import org.apache.flink.core.fs.Path
  import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment
  import org.apache.flink.streaming.api.functions.sink.filesystem.StreamingFileSink
 
  // Specify database name.
  val databaseName = "default"
 
  // Specify target table name.
  val tableName = "test"
  // Table path of the target table.
  val tablePath = "/data/warehouse/test"
  // Specify local temporary path.
  val dataTempPath = "/data/temp/"
 
  val tableProperties = new Properties
  // Set the table properties here.
 
  val writerProperties = new Properties
  // Set the writer properties here, such as temp path, commit threshold, access key, secret key, endpoint, etc.
 
  val carbonProperties = new Properties
  // Set the carbon properties here, such as date format, store location, etc.
   
  // Create carbon bulk writer factory. Two writer types are supported: 'Local' and 'S3'.
  val writerFactory = CarbonWriterFactory.builder("Local").build(
    databaseName,
    tableName,
    tablePath,
    tableProperties,
    writerProperties,
    carbonProperties
  )
   
  // Build a flink stream and run it.
  // 1. Create a new flink execution environment.
  val environment = StreamExecutionEnvironment.getExecutionEnvironment
  // Set flink environment configuration here, such as parallelism, checkpointing, restart strategy, etc.
 
  // 2. Create flink data source, may be a kafka source, custom source, or others.
  // The data type of source should be Array[AnyRef].
  // Array length should equals to table column count, and values order in array should matches table column order.
  val source = ...
  // 3. Create flink stream and set source.
  val stream = environment.addSource(source)
  // 4. Add other flink operators here.
  // ...
  // 5. Set flink stream target (write data to carbon with a write sink).
  stream.addSink(StreamingFileSink.forBulkFormat(new Path(ProxyFileSystem.DEFAULT_URI), writerFactory).build)
  // 6. Run flink stream.
  try {
    environment.execute
  } catch {
    case exception: Exception =>
      // Handle execute exception here.
  }
```

<a id="flink-integration-guide--writer-properties"></a>

### Writer properties

<a id="flink-integration-guide--local-writer"></a>

#### Local Writer

| Property | Name | Description |
| --- | --- | --- |
| CarbonLocalProperty.DATA\_TEMP\_PATH | carbon.writer.local.data.temp.path | Usually is a local path, data will write to temp path first, and move to target data path finally. |
| CarbonLocalProperty.COMMIT\_THRESHOLD | carbon.writer.local.commit.threshold | While written data count reach the threshold, data writer will flush and move data to target data path. |

<a id="flink-integration-guide--s3-writer"></a>

#### S3 Writer

| Property | Name | Description |
| --- | --- | --- |
| CarbonS3Property.ACCESS\_KEY | carbon.writer.s3.access.key | Access key of s3 file system |
| CarbonS3Property.SECRET\_KEY | carbon.writer.s3.secret.key | Secret key of s3 file system |
| CarbonS3Property.ENDPOINT | carbon.writer.s3.endpoint | Endpoint of s3 file system |
| CarbonS3Property.DATA\_TEMP\_PATH | carbon.writer.s3.data.temp.path | Usually is a local path, data will write to temp path first, and move to target data path finally. |
| CarbonS3Property.COMMIT\_THRESHOLD | carbon.writer.s3.commit.threshold | While written data count reach the threshold, data writer will flush and move data to target data path. |

<a id="flink-integration-guide--insert-from-stage"></a>

### Insert from stage

Refer [Grammar Description](#dml-of-carbondata--insert-data-into-carbondata-table-from-stage-input-files) for syntax.

<a id="flink-integration-guide--usage-example-code"></a>

## Usage Example Code

Create target table.

```
  CREATE TABLE test (col1 string, col2 string, col3 string) STORED AS carbondata
```

Writing flink data to local carbon table.

```
  import java.util.Properties
  import org.apache.carbon.flink.CarbonLocalProperty
  import org.apache.carbon.flink.CarbonWriterFactory
  import org.apache.carbon.flink.ProxyFileSystem
  import org.apache.carbondata.core.constants.CarbonCommonConstants
  import org.apache.flink.api.common.restartstrategy.RestartStrategies
  import org.apache.flink.core.fs.Path
  import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment
  import org.apache.flink.streaming.api.functions.sink.filesystem.StreamingFileSink
  import org.apache.flink.streaming.api.functions.source.SourceFunction

  val databaseName = "default"
  val tableName = "test"
  val tablePath = "/data/warehouse/test"
  val dataTempPath = "/data/temp/"

  val tableProperties = new Properties

  val writerProperties = new Properties
  writerProperties.setProperty(CarbonLocalProperty.DATA_TEMP_PATH, dataTempPath)

  val carbonProperties = new Properties
  carbonProperties.setProperty(CarbonCommonConstants.CARBON_TIMESTAMP_FORMAT, CarbonCommonConstants.CARBON_TIMESTAMP_DEFAULT_FORMAT)
  carbonProperties.setProperty(CarbonCommonConstants.CARBON_DATE_FORMAT, CarbonCommonConstants.CARBON_DATE_DEFAULT_FORMAT)
  carbonProperties.setProperty(CarbonCommonConstants.UNSAFE_WORKING_MEMORY_IN_MB, "1024")

  val writerFactory = CarbonWriterFactory.builder("Local").build(
    databaseName,
    tableName,
    tablePath,
    tableProperties,
    writerProperties,
    carbonProperties
  )

  val environment = StreamExecutionEnvironment.getExecutionEnvironment
  environment.setParallelism(1)
  environment.enableCheckpointing(2000L)
  environment.setRestartStrategy(RestartStrategies.noRestart)

  // Define a custom source.
  val source = new SourceFunction[Array[AnyRef]]() {
    override
    def run(sourceContext: SourceFunction.SourceContext[Array[AnyRef]]): Unit = {
      // Array length should equals to table column count, and values order in array should matches table column order.
      val data = new Array[AnyRef](3)
      data(0) = "value1"
      data(1) = "value2"
      data(2) = "value3"
      sourceContext.collect(data)
    }

    override 
    def cancel(): Unit = {
      // do something.
    }
  }

  val stream = environment.addSource(source)
  val streamSink = StreamingFileSink.forBulkFormat(new Path(ProxyFileSystem.DEFAULT_URI), writerFactory).build

  stream.addSink(streamSink)

  try {
    environment.execute
  } catch {
    case exception: Exception =>
      // TODO
      throw new UnsupportedOperationException(exception)
  }
```

Insert into table from stage directory.

```
  INSERT INTO test STAGE
```

[Top](#flink-integration-guide--top)

---

<a id="scd-and-cdc-guide"></a>

<!-- source_url: https://carbondata.apache.org/scd-and-cdc-guide.html -->

<!-- page_index: 25 -->

<a id="scd-and-cdc-guide--upsert-into-a-carbon-dataset-using-merge"></a>

# Upsert into a Carbon DataSet using Merge

<a id="scd-and-cdc-guide--scd-and-cdc-scenarios"></a>

## SCD and CDC Scenarios

Change Data Capture (CDC), is to apply all data changes generated from an external data set
into a target dataset. In other words, a set of changes (update/delete/insert) applied to an external
table needs to be applied to a target table.

Slowly Changing Dimensions (SCD), are the dimensions in which the data changes slowly, rather
than changing regularly on a time basis.

SCD and CDC data changes can be merged to a carbon dataset online using the data frame level `MERGE` API.

<a id="scd-and-cdc-guide--merge-api"></a>

#### MERGE API

Below API merges the datasets online and applies the actions as per the conditions.

```
  targetDS.merge(sourceDS, <condition>)
          .whenMatched(<condition>)
          .updateExpr(updateMap)
          .insertExpr(insertMap_u)
          .whenNotMatched(<condition>)
          .insertExpr(insertMap)
          .whenNotMatchedAndExistsOnlyOnTarget(<condition>)
          .delete()
          .execute()
```

<a id="scd-and-cdc-guide--merge-api-operation-semantics"></a>

#### MERGE API Operation Semantics

Below is the detailed description of the `merge` API operation.

- `merge` will merge the datasets based on a condition.
- `whenMatched` clauses are executed when a source row matches a target table row based on the match condition.
  These clauses have the following semantics.
  - `whenMatched` clauses can have at most one updateExpr and one delete action. The `updateExpr` action in merge only updates the specified columns of the matched target row. The `delete` action deletes the matched row.
  - If there are two `whenMatched` clauses, then they are evaluated in order they are specified. The first clause must have a clause condition (otherwise the second clause is never executed).
  - If both `whenMatched` clauses have conditions and neither of the conditions are true for a matching source-target row pair, then the matched target row is left unchanged.
- `whenNotMatched` clause is executed when a source row does not match any target row based on the match condition.
  - `whenNotMatched` clause can have only the `insertExpr` action. The new row is generated based on the specified column and corresponding expressions. Users do not need to specify all the columns in the target table. For unspecified target columns, NULL is inserted.
- `whenNotMatchedAndExistsOnlyOnTarget` clause is executed when row does not match source and exists only in target. This clause can have only delete action.

**NOTE:** SQL syntax for merge is not yet supported.

<a id="scd-and-cdc-guide--example-code-to-implement-cdc-scd-scenario"></a>

##### Example code to implement cdc/scd scenario

Please refer example class [MergeTestCase](https://github.com/apache/carbondata/blob/master/integration/spark/src/test/scala/org/apache/carbondata/spark/testsuite/merge/MergeTestCase.scala) to understand and implement scd and cdc scenarios.

[Top](#scd-and-cdc-guide--top)

---

<a id="faq"></a>

<!-- source_url: https://carbondata.apache.org/faq.html -->

<!-- page_index: 26 -->

<a id="faq--faqs"></a>

# FAQs

- [What are Bad Records?](#faq--what-are-bad-records)
- [Where are Bad Records Stored in CarbonData?](#faq--where-are-bad-records-stored-in-carbondata)
- [How to enable Bad Record Logging?](#faq--how-to-enable-bad-record-logging)
- [How to ignore the Bad Records?](#faq--how-to-ignore-the-bad-records)
- [How to specify store location while creating carbon session?](#faq--how-to-specify-store-location-while-creating-carbon-session)
- [What is Carbon Lock Type?](#faq--what-is-carbon-lock-type)
- [How to resolve Abstract Method Error?](#faq--how-to-resolve-abstract-method-error)
- [How Carbon will behave when execute insert operation in abnormal scenarios?](#faq--how-carbon-will-behave-when-execute-insert-operation-in-abnormal-scenarios)
- [Why all executors are showing success in Spark UI even after Dataload command failed at Driver side?](#faq--why-all-executors-are-showing-success-in-spark-ui-even-after-dataload-command-failed-at-driver-side)
- [Why different time zone result for select query output when query SDK writer output?](#faq--why-different-time-zone-result-for-select-query-output-when-query-sdk-writer-output)
- [How to check LRU cache memory footprint?](#faq--how-to-check-lru-cache-memory-footprint)
- [How to deal with the trailing task in query?](#faq--how-to-deal-with-the-trailing-task-in-query)

<a id="faq--troubleshooting"></a>

# TroubleShooting

- [Getting tablestatus.lock issues When loading data](#faq--getting-tablestatuslock-issues-when-loading-data)
- [Failed to load thrift libraries](#faq--failed-to-load-thrift-libraries)
- [Failed to launch the Spark Shell](#faq--failed-to-launch-the-spark-shell)
- [Failed to execute load query on cluster](#faq--failed-to-execute-load-query-on-cluster)
- [Failed to execute insert query on cluster](#faq--failed-to-execute-insert-query-on-cluster)
- [Failed to connect to hiveuser with thrift](#faq--failed-to-connect-to-hiveuser-with-thrift)
- [Failed to read the metastore db during table creation](#faq--failed-to-read-the-metastore-db-during-table-creation)
- [Failed to load data on the cluster](#faq--failed-to-load-data-on-the-cluster)
- [Failed to insert data on the cluster](#faq--failed-to-insert-data-on-the-cluster)
- [Failed to execute Concurrent Operations(Load,Insert,Update) on table by multiple workers](#faq--failed-to-execute-concurrent-operations-on-table-by-multiple-workers)
- [Failed to create\_index and drop index is also not working](#faq--failed-to-create-index-and-drop-index-is-also-not-working)

##

<a id="faq--what-are-bad-records"></a>

## What are Bad Records?

Records that fail to get loaded into the CarbonData due to data type incompatibility or are empty or have incompatible format are classified as Bad Records.

<a id="faq--where-are-bad-records-stored-in-carbondata"></a>

## Where are Bad Records Stored in CarbonData?

The bad records are stored at the location set in carbon.badRecords.location in carbon.properties file.
By default **carbon.badRecords.location** specifies the following location `/opt/Carbon/Spark/badrecords`.

<a id="faq--how-to-enable-bad-record-logging"></a>

## How to enable Bad Record Logging?

While loading data we can specify the approach to handle Bad Records. In order to analyse the cause of the Bad Records the parameter `BAD_RECORDS_LOGGER_ENABLE` must be set to value `TRUE`. There are multiple approaches to handle Bad Records which can be specified by the parameter `BAD_RECORDS_ACTION`.

- To pass the incorrect values of the csv rows with NULL value and load the data in CarbonData, set the following in the query :

```
'BAD_RECORDS_ACTION'='FORCE'
```

- To write the Bad Records without passing incorrect values with NULL in the raw csv (set in the parameter **carbon.badRecords.location**), set the following in the query :

```
'BAD_RECORDS_ACTION'='REDIRECT'
```

<a id="faq--how-to-ignore-the-bad-records"></a>

## How to ignore the Bad Records?

To ignore the Bad Records from getting stored in the raw csv, we need to set the following in the query :

```
'BAD_RECORDS_ACTION'='IGNORE'
```

<a id="faq--how-to-specify-store-location-while-creating-carbon-session"></a>

## How to specify store location while creating carbon session?

The store location specified while creating carbon session is used by the CarbonData to store the meta data like the schema, dictionary files, dictionary meta data and sort indexes.

Try creating `carbonsession` with `storepath` specified in the following manner :

```
val carbon = SparkSession.builder().config(sc.getConf).getOrCreateCarbonSession(<carbon_store_path>)
```

Example:

```
val carbon = SparkSession.builder().config(sc.getConf).getOrCreateCarbonSession("hdfs://localhost:9000/carbon/store")
```

<a id="faq--what-is-carbon-lock-type"></a>

## What is Carbon Lock Type?

The Apache CarbonData acquires lock on the files to prevent concurrent operation from modifying the same files. The lock can be of the following types depending on the storage location, for HDFS we specify it to be of type HDFSLOCK. By default it is set to type LOCALLOCK.
The property carbon.lock.type configuration specifies the type of lock to be acquired during concurrent operations on table. This property can be set with the following values :

- **LOCALLOCK** : This Lock is created on local file system as file. This lock is useful when only one spark driver (thrift server) runs on a machine and no other CarbonData spark application is launched concurrently.
- **HDFSLOCK** : This Lock is created on HDFS file system as file. This lock is useful when multiple CarbonData spark applications are launched and no ZooKeeper is running on cluster and the HDFS supports, file based locking.

<a id="faq--how-to-resolve-abstract-method-error"></a>

## How to resolve Abstract Method Error?

In order to build CarbonData project it is necessary to specify the spark profile. The spark profile sets the Spark Version. You need to specify the `spark version` while using Maven to build project.

<a id="faq--how-carbon-will-behave-when-execute-insert-operation-in-abnormal-scenarios"></a>

## How Carbon will behave when execute insert operation in abnormal scenarios?

Carbon support insert operation, you can refer to the syntax mentioned in [DML Operations on CarbonData](#dml-of-carbondata).
First, create a source table in spark-sql and load data into this created table.

```
CREATE TABLE source_table(
id String,
name String,
city String)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ",";
```

```
SELECT * FROM source_table;
id  name    city
1   jack    beijing
2   erlu    hangzhou
3   davi    shenzhen
```

**Scenario 1** :

Suppose, the column order in carbon table is different from source table, use script "SELECT \* FROM carbon table" to query, will get the column order similar as source table, rather than in carbon table's column order as expected.

```
CREATE TABLE IF NOT EXISTS carbon_table(
id String,
city String,
name String)
STORED AS carbondata;
```

```
INSERT INTO TABLE carbon_table SELECT * FROM source_table;
```

```
SELECT * FROM carbon_table;
id  city    name
1   jack    beijing
2   erlu    hangzhou
3   davi    shenzhen
```

As result shows, the second column is city in carbon table, but what inside is name, such as jack. This phenomenon is same with insert data into hive table.

If you want to insert data into corresponding column in carbon table, you have to specify the column order same in insert statement.

```
INSERT INTO TABLE carbon_table SELECT id, city, name FROM source_table;
```

**Scenario 2** :

Insert operation will be failed when the number of column in carbon table is different from the column specified in select statement. The following insert operation will be failed.

```
INSERT INTO TABLE carbon_table SELECT id, city FROM source_table;
```

**Scenario 3** :

When the column type in carbon table is different from the column specified in select statement. The insert operation will still success, but you may get NULL in result, because NULL will be substitute value when conversion type failed.

<a id="faq--why-all-executors-are-showing-success-in-spark-ui-even-after-dataload-command-failed-at-driver-side"></a>

## Why all executors are showing success in Spark UI even after Dataload command failed at Driver side?

Spark executor shows task as failed after the maximum number of retry attempts, but loading the data having bad records and BAD\_RECORDS\_ACTION (carbon.bad.records.action) is set as "FAIL" will attempt only once but will send the signal to driver as failed instead of throwing the exception to retry, as there is no point to retry if bad record found and BAD\_RECORDS\_ACTION is set to fail. Hence the Spark executor displays this one attempt as successful but the command has actually failed to execute. Task attempts or executor logs can be checked to observe the failure reason.

<a id="faq--why-different-time-zone-result-for-select-query-output-when-query-sdk-writer-output"></a>

## Why different time zone result for select query output when query SDK writer output?

SDK writer is an independent entity, hence SDK writer can generate carbondata files from a non-cluster machine that has different time zones. But at cluster when those files are read, it always takes cluster time-zone. Hence, the value of timestamp and date datatype fields are not original value.
If wanted to control timezone of data while writing, then set cluster's time-zone in SDK writer by calling below API.

```
TimeZone.setDefault(timezoneValue)
```

**Example:**

```
cluster timezone is Asia/Shanghai
TimeZone.setDefault(TimeZone.getTimeZone("Asia/Shanghai"))
```

<a id="faq--how-to-check-lru-cache-memory-footprint"></a>

## How to check LRU cache memory footprint?

To observe the LRU cache memory footprint in the logs, configure the below properties in log4j.properties file.

```
log4j.logger.org.apache.carbondata.core.cache.CarbonLRUCache = DEBUG
```

This property will enable the DEBUG log for the CarbonLRUCache and UnsafeMemoryManager which will print the information of memory consumed using which the LRU cache size can be decided. **Note:** Enabling the DEBUG log will degrade the query performance. Ensure carbon.max.driver.lru.cache.size is configured to observe the current cache size.

**Example:**

```
18/09/26 15:05:29 DEBUG CarbonLRUCache: main Required size for entry /home/target/store/default/stored_as_carbondata_table/Fact/Part0/Segment_0/0_1537954529044.carbonindexmerge :: 181 Current cache size :: 0
18/09/26 15:05:30 INFO CarbonLRUCache: main Removed entry from InMemory lru cache :: /home/target/store/default/stored_as_carbondata_table/Fact/Part0/Segment_0/0_1537954529044.carbonindexmerge
```

**Note:** If `Removed entry from InMemory LRU cache` are frequently observed in logs, you may have to increase the configured LRU size.

To observe the LRU cache from heap dump, check the heap used by CarbonLRUCache class.

<a id="faq--how-to-deal-with-the-trailing-task-in-query"></a>

## How to deal with the trailing task in query?

When tuning query performance, user may found that a few tasks slow down the overall query progress. To improve performance in such case, user can set spark.locality.wait and spark.speculation=true to enable speculation in spark, which will launch multiple task and get the result the one of the task which is finished first. Besides, user can also consider following configurations to further improve performance in this case.

**Example:**

```
spark.locality.wait = 500
spark.speculation = true
spark.speculation.quantile = 0.75
spark.speculation.multiplier = 5
spark.blacklist.enabled = false
```

**Note:**

spark.locality control data locality the value of 500 is used to shorten the waiting time of spark.

spark.speculation is a group of configuration, that can monitor trailing tasks and start new tasks when conditions are met.

spark.blacklist.enabled, avoid reduction of available executors due to blacklist mechanism.

<a id="faq--getting-tablestatus.lock-issues-when-loading-data"></a>

## Getting tablestatus.lock issues When loading data

**Symptom**

```
17/11/11 16:48:13 ERROR LocalFileLock: main hdfs:/localhost:9000/carbon/store/default/hdfstable/tablestatus.lock (No such file or directory)
java.io.FileNotFoundException: hdfs:/localhost:9000/carbon/store/default/hdfstable/tablestatus.lock (No such file or directory)
	at java.io.FileOutputStream.open0(Native Method)
	at java.io.FileOutputStream.open(FileOutputStream.java:270)
	at java.io.FileOutputStream.<init>(FileOutputStream.java:213)
	at java.io.FileOutputStream.<init>(FileOutputStream.java:101)
```

**Possible Cause**
If you use `<hdfs path>` as store path when creating carbonsession, may get the errors,because the default is LOCALLOCK.

**Procedure**
Before creating carbonsession, sets as below:

```
import org.apache.carbondata.core.util.CarbonProperties
import org.apache.carbondata.core.constants.CarbonCommonConstants
CarbonProperties.getInstance().addProperty(CarbonCommonConstants.LOCK_TYPE, "HDFSLOCK")
```

<a id="faq--failed-to-load-thrift-libraries"></a>

## Failed to load thrift libraries

**Symptom**

Thrift throws following exception :

```
thrift: error while loading shared libraries:
libthriftc.so.0: cannot open shared object file: No such file or directory
```

**Possible Cause**

The complete path to the directory containing the libraries is not configured correctly.

**Procedure**

Follow the Apache thrift docs at <https://thrift.apache.org/docs/install> to install thrift correctly.

<a id="faq--failed-to-launch-the-spark-shell"></a>

## Failed to launch the Spark Shell

**Symptom**

The shell prompts the following error :

```
org.apache.spark.sql.CarbonContext$$anon$$apache$spark$sql$catalyst$analysis
$OverrideCatalog$_setter_$org$apache$spark$sql$catalyst$analysis
$OverrideCatalog$$overrides_$e
```

**Possible Cause**

The Spark Version and the selected Spark Profile do not match.

**Procedure**

1. Ensure your spark version and selected profile for spark are correct.
2. Use the following command :

```
mvn -Pspark-2.4 -Dspark.version={yourSparkVersion} clean package
```

Note : Refrain from using "mvn clean package" without specifying the profile.

<a id="faq--failed-to-execute-load-query-on-cluster"></a>

## Failed to execute load query on cluster

**Symptom**

Load query failed with the following exception:

```
Dictionary file is locked for updation.
```

**Possible Cause**

The carbon.properties file is not identical in all the nodes of the cluster.

**Procedure**

Follow the steps to ensure the carbon.properties file is consistent across all the nodes:

1. Copy the carbon.properties file from the master node to all the other nodes in the cluster.
   For example, you can use ssh to copy this file to all the nodes.
2. For the changes to take effect, restart the Spark cluster.

<a id="faq--failed-to-execute-insert-query-on-cluster"></a>

## Failed to execute insert query on cluster

**Symptom**

Load query failed with the following exception:

```
Dictionary file is locked for updation.
```

**Possible Cause**

The carbon.properties file is not identical in all the nodes of the cluster.

**Procedure**

Follow the steps to ensure the carbon.properties file is consistent across all the nodes:

1. Copy the carbon.properties file from the master node to all the other nodes in the cluster.
   For example, you can use scp to copy this file to all the nodes.
2. For the changes to take effect, restart the Spark cluster.

<a id="faq--failed-to-connect-to-hiveuser-with-thrift"></a>

## Failed to connect to hiveuser with thrift

**Symptom**

We get the following exception :

```
Cannot connect to hiveuser.
```

**Possible Cause**

The external process does not have permission to access.

**Procedure**

Ensure that the Hiveuser in mysql must allow its access to the external processes.

<a id="faq--failed-to-read-the-metastore-db-during-table-creation"></a>

## Failed to read the metastore db during table creation

**Symptom**

We get the following exception on trying to connect :

```
Cannot read the metastore db
```

**Possible Cause**

The metastore db is dysfunctional.

**Procedure**

Remove the metastore db from the carbon.metastore in the Spark Directory.

<a id="faq--failed-to-load-data-on-the-cluster"></a>

## Failed to load data on the cluster

**Symptom**

Data loading fails with the following exception :

```
Data Load failure exception
```

**Possible Cause**

The following issue can cause the failure :

1. The core-site.xml, hive-site.xml, yarn-site and carbon.properties are not consistent across all nodes of the cluster.
2. Path to hdfs ddl is not configured correctly in the carbon.properties.

**Procedure**

Follow the steps to ensure the following configuration files are consistent across all the nodes:

1. Copy the core-site.xml, hive-site.xml, yarn-site, carbon.properties files from the master node to all the other nodes in the cluster.
   For example, you can use scp to copy this file to all the nodes.

   Note : Set the path to hdfs ddl in carbon.properties in the master node.
2. For the changes to take effect, restart the Spark cluster.

<a id="faq--failed-to-insert-data-on-the-cluster"></a>

## Failed to insert data on the cluster

**Symptom**

Insertion fails with the following exception :

```
Data Load failure exception
```

**Possible Cause**

The following issue can cause the failure :

1. The core-site.xml, hive-site.xml, yarn-site and carbon.properties are not consistent across all nodes of the cluster.
2. Path to hdfs ddl is not configured correctly in the carbon.properties.

**Procedure**

Follow the steps to ensure the following configuration files are consistent across all the nodes:

1. Copy the core-site.xml, hive-site.xml, yarn-site, carbon.properties files from the master node to all the other nodes in the cluster.
   For example, you can use scp to copy this file to all the nodes.

   Note : Set the path to hdfs ddl in carbon.properties in the master node.
2. For the changes to take effect, restart the Spark cluster.

<a id="faq--failed-to-execute-concurrent-operations-on-table-by-multiple-workers"></a>

## Failed to execute Concurrent Operations on table by multiple workers

**Symptom**

Execution fails with the following exception :

```
Table is locked for updation.
```

**Possible Cause**

Concurrency not supported.

**Procedure**

Worker must wait for the query execution to complete and the table to release the lock for another query execution to succeed.

<a id="faq--failed-to-create-index-and-drop-index-is-also-not-working"></a>

## Failed to create index and drop index is also not working

**Symptom**

Execution fails with the following exception :

```
HDFS Quota Exceeded
```

**Possible Cause**

HDFS Quota is set, and it is not letting carbondata write or modify any files.

**Procedure**

Drop that particular index using Drop Index command so as to clear the stale folders.

[Top](#faq--top)

---

<a id="how-to-contribute-to-apache-carbondata"></a>

<!-- source_url: https://carbondata.apache.org/how-to-contribute-to-apache-carbondata.html -->

<!-- page_index: 27 -->

<a id="how-to-contribute-to-apache-carbondata--how-to-contribute-to-apache-carbondata"></a>

# How to contribute to Apache CarbonData

The Apache CarbonData community welcomes all kinds of contributions from anyone with a passion for
faster data format! Apache CarbonData is a new file format for faster interactive query using
advanced columnar storage, index, compression and encoding techniques to improve computing
efficiency,in turn it will help speedup queries an order of magnitude faster over PetaBytes of data.

We use a review-then-commit workflow in CarbonData for all contributions.

- Engage -> Design -> Code -> Review -> Commit

<a id="how-to-contribute-to-apache-carbondata--engage"></a>

## Engage

<a id="how-to-contribute-to-apache-carbondata--mailing-list-s"></a>

### Mailing list(s)

We discuss design and implementation issues on [dev@carbondata.apache.org](mailto:dev@carbondata.apache.org) Join by
emailing [dev-subscribe@carbondata.apache.org](mailto:dev-subscribe@carbondata.apache.org)

<a id="how-to-contribute-to-apache-carbondata--apache-jira"></a>

### Apache JIRA

We use [Apache JIRA](https://issues.apache.org/jira/browse/CARBONDATA) as an issue tracking and
project management tool, as well as a way to communicate among a very diverse and distributed set
of contributors. To be able to gather feedback, avoid frustration, and avoid duplicated efforts all
CarbonData-related work should be tracked there.

If you do not already have an Apache JIRA account, sign up [here](https://issues.apache.org/jira/).

If a quick search doesn?t turn up an existing JIRA issue for the work you want to contribute, create it. Please discuss your proposal with a committer or the component lead in JIRA or, alternatively, on the developer mailing list([dev@carbondata.apache.org](mailto:dev@carbondata.apache.org)).

If there?s an existing JIRA issue for your intended contribution, please comment about your
intended work. Once the work is understood, a committer will assign the issue to you.
(If you don?t have a JIRA role yet, you?ll be added to the "contributor" role.) If an issue is
currently assigned, please check with the current assignee before reassigning.

For moderate or large contributions, you should not start coding or writing a design doc unless
there is a corresponding JIRA issue assigned to you for that work. Simple changes, like fixing typos, do not require an associated issue.

<a id="how-to-contribute-to-apache-carbondata--design"></a>

### Design

To clearly express your thoughts and get early feedback from other community members, we encourage you to clearly scope, document the design of non-trivial contributions and discuss with the CarbonData community before you start coding.

Generally, the JIRA issue is the best place to gather relevant design docs, comments, or references. It?s great to explicitly include relevant stakeholders early in the conversation. For designs that may be generally interesting, we also encourage conversations on the developer?s mailing list.

<a id="how-to-contribute-to-apache-carbondata--code"></a>

### Code

We use GitHub?s pull request functionality to review proposed code changes.
If you do not already have a personal GitHub account, sign up [here](https://github.com).

<a id="how-to-contribute-to-apache-carbondata--git-config"></a>

### Git config

Ensure to finish the below config(user.email, user.name) before starting PR works.

```
$ git config --global user.email "you@example.com"
$ git config --global user.name "Your Name"
```

<a id="how-to-contribute-to-apache-carbondata--fork-the-repository-on-github"></a>

#### Fork the repository on GitHub

Go to the [Apache CarbonData GitHub mirror](https://github.com/apache/carbondata) and
fork the repository to your account.
This will be your private workspace for staging changes.

<a id="how-to-contribute-to-apache-carbondata--clone-the-repository-locally"></a>

#### Clone the repository locally

You are now ready to create the development environment on your local machine.
Clone CarbonData?s read-only GitHub mirror.

```
$ git clone https://github.com/apache/carbondata.git
$ cd carbondata
```

Add your forked repository as an additional Git remote, where you?ll push your changes.

```
$ git remote add <GitHub_user> https://github.com/<GitHub_user>/carbondata.git
```

You are now ready to start developing!

<a id="how-to-contribute-to-apache-carbondata--create-a-branch-in-your-fork"></a>

#### Create a branch in your fork

You?ll work on your contribution in a branch in your own (forked) repository. Create a local branch, initialized with the state of the branch you expect your changes to be merged into.
Keep in mind that we use several branches, including master, feature-specific, and
release-specific branches. If you are unsure, initialize with the state of the master branch.

```
$ git fetch --all
$ git checkout -b <my-branch> origin/master
```

At this point, you can start making and committing changes to this branch in a standard way.

<a id="how-to-contribute-to-apache-carbondata--syncing-and-pushing-your-branch"></a>

#### Syncing and pushing your branch

Periodically while you work, and certainly before submitting a pull request, you should update
your branch with the most recent changes to the target branch.

```
$ git pull --rebase
```

Remember to always use --rebase parameter to avoid extraneous merge commits.

To push your local, committed changes to your (forked) repository on GitHub, run:

```
$ git push <GitHub_user> <my-branch>
```

<a id="how-to-contribute-to-apache-carbondata--testing"></a>

#### Testing

All code should have appropriate unit testing coverage. New code should have new tests in the
same contribution. Bug fixes should include a regression test to prevent the issue from reoccurring.

For contributions to the Java code, run unit tests locally via Maven.

```
$ mvn clean verify
```

<a id="how-to-contribute-to-apache-carbondata--review"></a>

### Review

Once the initial code is complete and the tests pass, it?s time to start the code review process.
We review and discuss all code, no matter who authors it. It?s a great way to build community, since you can learn from other developers, and they become familiar with your contribution.
It also builds a strong project by encouraging a high quality bar and keeping code consistent
throughout the project.

<a id="how-to-contribute-to-apache-carbondata--create-a-pull-request"></a>

#### Create a pull request

Organize your commits to make your reviewer?s job easier. Use the following command to
re-order, squash, edit, or change description of individual commits.

```
$ git rebase -i origin/master
```

Navigate to the CarbonData GitHub mirror to create a pull request. The title of the pull request
should be strictly in the following format:

```
[CARBONDATA-JiraTicketNumer][FeatureName] Description of pull request    
```

Please include a descriptive pull request message to help make the reviewer?s job easier:

```
 - The root cause/problem statement
 - What is the implemented solution
```

If you know a good committer to review your pull request, please make a comment like the following.
If not, don?t worry, a committer will pick it up.

```
Hi @<committer/reviewer name>, can you please take a look?
```

<a id="how-to-contribute-to-apache-carbondata--code-review-and-revision"></a>

#### Code Review and Revision

During the code review process, don?t rebase your branch or otherwise modify published commits, since this can remove existing comment history and be confusing to the reviewer, When you make a revision, always push it in a new commit.

Our GitHub mirror automatically provides pre-commit testing coverage using Jenkins.
Please make sure those tests pass,the contribution cannot be merged otherwise.

<a id="how-to-contribute-to-apache-carbondata--lgtm"></a>

#### LGTM

Once the reviewer is happy with the change, they?ll respond with an LGTM ("looks good to me!").
At this point, the committer will take over, possibly make some additional touch ups, and merge your changes into the codebase.

In the case both the author and the reviewer are committers, either can merge the pull request.
Just be sure to communicate clearly whose responsibility it is in this particular case.

Thank you for your contribution to Apache CarbonData!

<a id="how-to-contribute-to-apache-carbondata--deleting-your-branch-optional"></a>

#### Deleting your branch(optional)

Once the pull request is merged into the Apache CarbonData repository, you can safely delete the
branch locally and purge it from your forked repository.

From another local branch, run:

```
$ git fetch --all
$ git branch -d <my-branch>
$ git push <GitHub_user> --delete <my-branch>
```

[Top](#how-to-contribute-to-apache-carbondata--top)

---

<a id="security"></a>

<!-- source_url: https://carbondata.apache.org/security.html -->

<!-- page_index: 28 -->

<a id="security--apache-carbondata-security"></a>

# Apache CarbonData Security

The Apache Software Foundation takes a rigorous standpoint in annihilating the security issues
in its software projects. Apache CarbonData is highly sensitive and forthcoming to issues
pertaining to its features and functionality.

If you have apprehensions regarding CarbonData’s security or you discover vulnerability or
potential threat, don’t hesitate to get in touch with the Apache Security Team by dropping a
mail at  [security@apache.org](mailto:security@apache.org). In the mail, specify the
project name CarbonData with the description of the issue or potential threat. You are also
urged to recommend the way to reproduce and replicate the issue. The security team and the
CarbonData community will get back to you after assessing and analysing the findings.

PLEASE PAY ATTENTION to report the security issue on the security email before disclosing it on
public domain.

The ASF Security Team maintains a page with the description of how vulnerabilities and potential
threats are handled, check their [Web
page](http://www.apache.org/security/) for more Details.

---

<a id="release-guide"></a>

<!-- source_url: https://carbondata.apache.org/release-guide.html -->

<!-- page_index: 29 -->

<a id="release-guide--apache-carbondata-release-guide"></a>

# Apache CarbonData Release Guide

Apache CarbonData periodically declares and publishes releases.

Each release is executed by a *Release Manager*, who is selected among the CarbonData committers.
This document describes the process that the Release Manager follows to perform a release. Any
changes to this process should be discussed and adopted on the
[dev@ mailing list](mailto:dev@carbondata.apache.org).

Please remember that publishing software has legal consequences. This guide complements the
foundation-wide [Product Release Policy](http://www.apache.org/dev/release.html) and [Release
Distribution Policy](http://www.apache.org/dev/release-distribution).

<a id="release-guide--decide-to-release"></a>

## Decide to release

Deciding to release and selecting a Release Manager is the first step of the release process.
This is a consensus-based decision of the entire community.

Anybody can propose a release on the dev@ mailing list, giving a solid argument and nominating a
committer as the Release Manager (including themselves). There's no formal process, no vote
requirements, and no timing requirements. Any objections should be resolved by consensus before
starting the release.

*Checklist to proceed to next step:*

1. Community agrees to release
2. Community selects a Release Manager

<a id="release-guide--prepare-for-the-release"></a>

## Prepare for the release

Before your first release, you should perform one-time configuration steps. This will set up your
security keys for signing the artifacts and access release repository.

To prepare for each release, you should audit the project status in the Jira, and do necessary
bookkeeping. Finally, you should tag a release.

<a id="release-guide--one-time-setup-instructions"></a>

### One-time setup instructions

<a id="release-guide--gpg-key"></a>

#### GPG Key

You need to have a GPG key to sign the release artifacts. Please be aware of the ASF-wide
[release signing guidelines](https://www.apache.org/dev/release-signing.html). If you don't have
a GPG key associated with your Apache account, please create one according to the guidelines.

Determine your Apache GPG key and key ID, as follows:

```
gpg --list-keys
```

This will list your GPG keys. One of these should reflect your Apache account, for example:

```
pub   2048R/845E6689 2016-02-23
uid                  Nomen Nescio <anonymous@apache.org>
sub   2048R/BA4D50BE 2016-02-23
```

Here, the key ID is the 8-digit hex string in the `pub` line: `845E6689`.

Now, add your Apache GPG key to the CarbonData's `KEYS` file in `dev` and `release` repositories
at `dist.apache.org`. Follow the instructions listed at the top of these files.

Configure `git` to use this key when signing code by giving it your key ID, as follows:

```
git config --global user.signingkey 845E6689
```

You may drop the `--global` option if you'd prefer to use this key for the current repository only.

You may wish to start `gpg-agent` to unlock your GPG key only once using your passphrase.
Otherwise, you may need to enter this passphrase several times. The setup of `gpg-agent` varies
based on operating system, but may be something like this:

```
eval $(gpg-agent --daemon --no-grab --write-env-file $HOME/.gpg-agent-info)
export GPG_TTY=$(tty)
export GPG_AGENT_INFO
```

<a id="release-guide--access-to-apache-nexus"></a>

#### Access to Apache Nexus

Configure access to the [Apache Nexus repository](https://repository.apache.org), used for
staging repository and promote the artifacts to Maven Central.

1. You log in with your Apache account.
2. Confirm you have appropriate access by finding `org.apache.carbondata` under `Staging Profiles`.
3. Navigate to your `Profile` (top right dropdown menu of the page).
4. Choose `User Token` from the dropdown, then click `Access User Token`. Copy a snippet of the
   Maven XML configuration block.
5. Insert this snippet twice into your global Maven `settings.xml` file, typically `${HOME]/ .m2/settings.xml`. The end result should look like this, where `TOKEN_NAME` and `TOKEN_PASSWORD`
   are your secret tokens:

```
 <settings>
   <servers>
     <server>
       <id>apache.releases.https</id>
       <username>TOKEN_NAME</username>
       <password>TOKEN_PASSWORD</password>
     </server>
     <server>
       <id>apache.snapshots.https</id>
       <username>TOKEN_NAME</username>
       <password>TOKEN_PASSWORD</password>
     </server>
   </servers>
 </settings>
```

<a id="release-guide--create-a-new-version-in-jira"></a>

#### Create a new version in Jira

When contributors resolve an issue in Jira, they are tagging it with a release that will contain
their changes. With the release currently underway, new issues should be resolved against a
subsequent future release. Therefore, you should create a release item for this subsequent
release, as follows:

1. In Jira, navigate to `CarbonData > Administration > Versions`.
2. Add a new release: choose the next minor version number compared to the one currently
   underway, select today's date as the `Start Date`, and choose `Add`.

<a id="release-guide--triage-release-blocking-issues-in-jira"></a>

#### Triage release-blocking issues in Jira

There could be outstanding release-blocking issues, which should be triaged before proceeding to
build the release. We track them by assigning a specific `Fix Version` field even before the
issue is resolved.

The list of release-blocking issues is available at the [version status page](https://issues.apache.org/jira/browse/CARBONDATA/?selectedTab=com.atlassian.jira.jira-projects-plugin:versions-panel).
Triage each unresolved issue with one of the following resolutions:

- If the issue has been resolved and Jira was not updated, resolve it accordingly.
- If the issue has not been resolved and it is acceptable to defer until the next release, update
  the `Fix Version` field to the new version you just created. Please consider discussing this
  with stakeholders and the dev@ mailing list, as appropriate.
- If the issue has not been resolved and it is not acceptable to release until it is fixed, the
  release cannot proceed. Instead, work with the CarbonData community to resolve the issue.

<a id="release-guide--review-release-notes-in-jira"></a>

#### Review Release Notes in Jira

Jira automatically generates Release Notes based on the `Fix Version` applied to the issues.
Release Notes are intended for CarbonData users (not CarbonData committers/contributors). You
should ensure that Release Notes are informative and useful.

Open the release notes from the [version status page](https://issues.apache.org/jira/browse/CARBONDATA/?selectedTab=com.atlassian.jira.jira-projects-plugin:versions-panel)
by choosing the release underway and clicking Release Notes.

You should verify that the issues listed automatically by Jira are appropriate to appear in the
Release Notes. Specifically, issues should:

- Be appropriate classified as `Bug`, `New Feature`, `Improvement`, etc.
- Represent noteworthy user-facing changes, such as new functionality, backward-incompatible
  changes, or performance improvements.
- Have occurred since the previous release; an issue that was introduced and fixed between
  releases should not appear in the Release Notes.
- Have an issue title that makes sense when read on its own.

Adjust any of the above properties to the improve clarity and presentation of the Release Notes.

<a id="release-guide--verify-that-a-release-build-works"></a>

#### Verify that a Release Build works

Run `mvn clean install -Prelease` to ensure that the build processes that are specific to that
profile are in good shape.

*Checklist to proceed to the next step:*

1. Release Manager's GPG key is published to `dist.apache.org`.
2. Release Manager's GPG key is configured in `git` configuration.
3. Release Manager has `org.apache.carbondata` listed under `Staging Profiles` in Nexus.
4. Release Manager's Nexus User Token is configured in `settings.xml`.
5. Jira release item for the subsequent release has been created.
6. There are no release blocking Jira issues.
7. Release Notes in Jira have been audited and adjusted.

<a id="release-guide--build-a-release"></a>

### Build a release

Use Maven release plugin to tag and build release artifacts, as follows:

```
mvn release:prepare
```

Use Maven release plugin to stage these artifacts on the Apache Nexus repository, as follows:

```
mvn release:perform
```

Review all staged artifacts. They should contain all relevant parts for each module, including
`pom.xml`, jar, test jar, source, etc. Artifact names should follow
[the existing format](https://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.apache.carbondata%22)
in which artifact name mirrors directory structure. Carefully review any new artifacts.

Close the staging repository on Nexus. When prompted for a description, enter "Apache CarbonData
x.x.x release".

<a id="release-guide--stage-source-release-on-dist.apache.org"></a>

### Stage source release on dist.apache.org

Copy the source release to dev repository on `dist.apache.org`.

1. If you have not already, check out the section of the `dev` repository on `dist.apache.org` via Subversion. In a fresh directory:

```
svn co https://dist.apache.org/repos/dist/dev/carbondata
```

2. Make a directory for the new release:

```
mkdir x.x.x
```

3. Copy the CarbonData source distribution, hash, and GPG signature:

```
cp apache-carbondata-x.x.x-source-release.zip x.x.x
```

4. Add and commit the files:

```
svn add x.x.x
svn commit
```

5. Verify the files are [present](https://dist.apache.org/repos/dist/dev/carbondata).

<a id="release-guide--propose-a-pull-request-for-website-updates"></a>

### Propose a pull request for website updates

The final step of building a release candidate is to propose a website pull request.

This pull request should update the following page with the new release:

- `src/main/webapp/index.html`
- `src/main/webapp/docs/latest/mainpage.html`

*Checklist to proceed to the next step:*

1. Maven artifacts deployed to the staging repository of
   [repository.apache.org](https://repository.apache.org)
2. Source distribution deployed to the dev repository of
   [dist.apache.org](https://dist.apache.org/repos/dist/dev/carbondata/)
3. Website pull request to list the release.

<a id="release-guide--vote-on-the-release-candidate"></a>

## Vote on the release candidate

Once you have built and individually reviewed the release candidate, please share it for the
community-wide review. Please review foundation-wide [voting guidelines](http://www.apache.org/foundation/voting.html)
for more information.

Start the review-and-vote thread on the dev@ mailing list. Here's an email template; please
adjust as you see fit:

```
From: Release Manager
To: dev@carbondata.apache.org
Subject: [VOTE] Apache CarbonData Release x.x.x

Hi everyone,
Please review and vote on the release candidate for the version x.x.x, as follows:

[ ] +1, Approve the release
[ ] -1, Do not approve the release (please provide specific comments)

The complete staging area is available for your review, which includes:
* JIRA release notes [1],
* the official Apache source release to be deployed to dist.apache.org [2], which is signed with the key with fingerprint FFFFFFFF [3],
* all artifacts to be deployed to the Maven Central Repository [4],
* source code tag "x.x.x" [5],
* website pull request listing the release [6].

The vote will be open for at least 72 hours. It is adopted by majority approval, with at least 3 PMC affirmative votes.

Thanks,
Release Manager

[1] link
[2] link
[3] https://dist.apache.org/repos/dist/dist/carbondata/KEYS
[4] link
[5] link
[6] link
```

If there are any issues found in the release candidate, reply on the vote thread to cancel the vote.
There?s no need to wait 72 hours. Proceed to the `Cancel a Release (Fix Issues)` step below and
address the problem.
However, some issues don?t require cancellation.
For example, if an issue is found in the website pull request, just correct it on the spot and the
vote can continue as-is.

If there are no issues, reply on the vote thread to close the voting. Then, tally the votes in a
separate email. Here?s an email template; please adjust as you see fit.

```
From: Release Manager
To: dev@carbondata.apache.org
Subject: [RESULT][VOTE] Apache CarbonData Release x.x.x

I'm happy to announce that we have unanimously approved this release.

There are XXX approving votes, XXX of which are binding:
* approver 1
* approver 2
* approver 3
* approver 4

There are no disapproving votes.

Thanks everyone!
```

While in incubation, the Apache Incubator PMC must also vote on each release, using the same
process as above. Start the review and vote thread on the `general@incubator.apache.org` list.

*Checklist to proceed to the final step:*

1. Community votes to release the proposed release
2. While in incubation, Apache Incubator PMC votes to release the proposed release

<a id="release-guide--cancel-a-release-fix-issues"></a>

## Cancel a Release (Fix Issues)

Any issue identified during the community review and vote should be fixed in this step.

To fully cancel a vote:

- Cancel the current release and verify the version is back to the correct SNAPSHOT:

```
mvn release:cancel
```

- Drop the release tag:

```
git tag -d x.x.x
git push --delete apache x.x.x
```

- Drop the staging repository on Nexus ([repository.apache.org](https://repository.apache.org))

Verify the version is back to the correct SNAPSHOT.

Code changes should be proposed as standard pull requests and merged.

Once all issues have been resolved, you should go back and build a new release candidate with
these changes.

<a id="release-guide--finalize-the-release"></a>

## Finalize the release

Once the release candidate has been reviewed and approved by the community, the release should be
finalized. This involves the final deployment of the release to the release repositories, merging the website changes, and announce the release.

<a id="release-guide--deploy-artifacts-to-maven-central-repository"></a>

### Deploy artifacts to Maven Central repository

On Nexus, release the staged artifacts to Maven Central repository. In the `Staging Repositories`
section, find the relevant release candidate `orgapachecarbondata-XXX` entry and click `Release`.

<a id="release-guide--deploy-source-release-to-dist.apache.org"></a>

### Deploy source release to dist.apache.org

Copy the source release from the `dev` repository to `release` repository at `dist.apache.org`
using Subversion.

<a id="release-guide--merge-website-pull-request"></a>

### Merge website pull request

Merge the website pull request to list the release created earlier.

<a id="release-guide--mark-the-version-as-released-in-jira"></a>

### Mark the version as released in Jira

In Jira, inside [version management](https://issues.apache.org/jira/plugins/servlet/project-config/CARBONDATA/versions)
, hover over the current release and a settings menu will appear. Click `Release`, and select
today's state.

*Checklist to proceed to the next step:*

1. Maven artifacts released and indexed in the
   [Maven Central repository](https://search.maven.org/#search%7Cga%7C1%7Cg%3A%22org.apache.carbondata%22)
2. Source distribution available in the release repository of
   [dist.apache.org](https://dist.apache.org/repos/dist/release/carbondata/)
3. Website pull request to list the release merged
4. Release version finalized in Jira

<a id="release-guide--promote-the-release"></a>

## Promote the release

Once the release has been finalized, the last step of the process is to promote the release
within the project and beyond.

<a id="release-guide--apache-mailing-lists"></a>

### Apache mailing lists

Announce on the dev@ mailing list that the release has been finished.

Announce on the user@ mailing list that the release is available, listing major improvements and
contributions.

While in incubation, announce the release on the Incubator's general@ mailing list.

*Checklist to declare the process completed:*

1. Release announced on the user@ mailing list.
2. Release announced on the Incubator's general@ mailing list.
3. Completion declared on the dev@ mailing list.

[Top](#release-guide--top)

---

<a id="documentation"></a>

<!-- source_url: https://carbondata.apache.org/documentation.html -->

<!-- page_index: 30 -->

<a id="documentation--apache-carbondata-documentation"></a>

# Apache CarbonData Documentation

Apache CarbonData is a new big data file format for faster interactive query using advanced columnar storage, index, compression and encoding techniques to improve computing efficiency, which helps in speeding up queries by an order of magnitude faster over PetaBytes of data.

<a id="documentation--getting-started"></a>

## Getting Started

**File Format Concepts:** Start with the basics of understanding the [CarbonData file format](https://carbondata.apache.org/file-structure-of-carbondata.html#carbondata-file-format) and its [storage structure](https://carbondata.apache.org/file-structure-of-carbondata.html). This will help to understand other parts of the documentation, including deployment, programming and usage guides.

**Quick Start:** [Run an example program](#quick-start-guide--installing-and-configuring-carbondata-to-run-locally-with-spark-shell) on your local machine or [study some examples](https://github.com/apache/carbondata/tree/master/examples/spark/src/main/scala/org/apache/carbondata/examples).

**CarbonData SQL Language Reference:** CarbonData extends the Spark SQL language and adds several [DDL](#ddl-of-carbondata) and [DML](#dml-of-carbondata) statements to support operations on it. Refer to the [Reference Manual](#language-manual) to understand the supported features and functions.

**Programming Guides:** You can read our guides about [Java APIs supported](#sdk-guide) or [C++ APIs supported](#csdk-guide) to learn how to integrate CarbonData with your applications.

<a id="documentation--integration"></a>

## Integration

- CarbonData can be integrated with popular execution engines like [Spark](#quick-start-guide--spark) , [Presto](#quick-start-guide--presto) and [Hive](#quick-start-guide--hive).
- CarbonData can be integrated with popular storage engines like HDFS, Huawei Cloud(OBS) and [Alluxio](#quick-start-guide--alluxio).
  Refer to the [Installation and Configuration](#quick-start-guide--integration) section to understand all modes of Integrating CarbonData.

<a id="documentation--contributing-to-carbondata"></a>

## Contributing to CarbonData

The Apache CarbonData community welcomes all kinds of contributions from anyone with a passion for
faster data format.Contributing to CarbonData doesn?t just mean writing code. Helping new users on the mailing list, testing releases, and improving documentation are also welcome.Please follow the [Contributing to CarbonData guidelines](#how-to-contribute-to-apache-carbondata) before proposing a design or code change.

**Compiling CarbonData:** This [guide](https://github.com/apache/carbondata/tree/master/build) will help you to compile and generate the jars for test.

<a id="documentation--external-resources"></a>

## External Resources

**Wiki:** You can read the [Apache CarbonData wiki](https://cwiki.apache.org/confluence/display/CARBONDATA/CarbonData+Home) page for upcoming release plan, blogs and training materials.

**Summit:** Presentations from past summits and conferences can be found [here](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=66850609).

**Blogs:** Blogs by external users can be found [here](https://cwiki.apache.org/confluence/pages/viewpage.action?pageId=67635497).

**Performance reports:** TPC-H performance reports can be found [here](https://cwiki.apache.org/confluence/display/CARBONDATA/Performance+-+TPCH+Report+of+CarbonData+%281.2+version%29+and+Parquet+on+Spark+Execution+Engine).

**Trainings:** Training records on design and code flows can be found [here](https://cwiki.apache.org/confluence/display/CARBONDATA/CarbonData+Training+Materials).

[Top](#documentation--top)

---
