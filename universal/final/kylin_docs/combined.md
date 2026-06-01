# Overview

## Navigation

- [Overview](#overview)
- [Quick Start](#quickstart-intro)
  - [Kylin Tutorial](#quickstart-tutorial)
- [Deployment](#deployment-intro)
  - [Prerequisite](#deployment-prerequisite)
    - [Use MySQL as Metadata DB](#deployment-rdbms_metastore-use_mysql_as_metadb)
    - [Use PostgreSQL as Metadata DB](#deployment-rdbms_metastore-usepg_as_metadb)
  - [Single Node Mode](#deployment-single_node_mode)
  - [Cluster Mode](#deployment-cluster_mode)
  - [Read/Write Separation Deployment](#deployment-rw_separation)
  - [Configuration](#configuration-intro)
    - [Basic Configuration](#configuration-config)
    - [Gluten Configuration](#configuration-gluten_config)
    - [Hadoop Queue](#configuration-hadoop_queue_config)
    - [HTTPS Connection](#configuration-https)
    - [Log Rotate](#configuration-log_rotate)
    - [Query Cache](#configuration-query_cache)
    - [Spark Dynamic Allocation](#configuration-spark_dynamic_allocation)
    - [Spark RPC Encryption](#configuration-spark_rpc_encryption)
- [Datasource](#datasource-intro)
  - [Use Hive as Data Source](#datasource-import_hive)
  - [Data Sampling](#datasource-data_sampling)
  - [Logical View](#datasource-logical_view)
- [Internal Table](#internaltable-intro)
  - [Table Management](#internaltable-internal_table_management)
  - [Data Loading](#internaltable-load_data_into_internal_table)
  - [Querying Internal Tables](#internaltable-query_internal_table)
- [Model](#model-intro)
  - [Manual Modeling](#model-manual-modeling)
    - [Aggregate Index](#model-manual-aggregation_group)
    - [Table Index](#model-manual-table_index)
    - [Computed Column](#model-manual-computed_column)
  - [Recommendation](#model-rec-intro)
    - [Imported SQL Modeling](#model-rec-sql_modeling)
    - [Query History Recommendation](#model-rec-optimize_by_qh)
    - [Index Optimization](#model-rec-index_optimization)
  - [Management](#model-manage-model_info)
    - [Model Information](#model-manage-model_info)
    - [Model Operation](#model-manage-model_operation)
    - [Import and Export](#model-manage-import_export)
    - [Data Loading](#model-manage-data_loading)
    - [Segment](#model-manage-segment)
  - [Table Snapshot](#model-snapshot)
  - [Advanced Features](#model-features-measures-intro)
    - [Measures](#model-features-measures-intro)
      - [Top-N (Approximate) (Beta)](#model-features-measures-topn)
      - [Count Distinct (Precise)](#model-features-measures-count_distinct_bitmap)
      - [Count Distinct (Approximate)](#model-features-measures-count_distinct_hllc)
      - [Percentile (Approximate)](#model-features-measures-percentile_approx)
      - [CORR](#model-features-measures-corr)
      - [COLLECT SET](#model-features-measures-collect_set)
    - [SCD2](#model-features-scd2)
    - [Runtime Join](#model-features-runtime_join)
    - [Multilevel Partitioning](#model-features-multi_partitioning)
    - [Scalar Subquery](#model-features-scalar_subquery)
    - [Fast Bitmap Index](#model-features-fast_bitmap)
    - [Dictionary Encoding](#model-features-integer_encoding)
  - [Streaming](#model-streaming-intro)
    - [Prerequisite](#model-streaming-prerequisite)
    - [Work with Kylin Real-time](#model-streaming-real-time)
    - [Streaming Message Parser](#model-streaming-custom-parser)
- [Query](#query-insight)
  - [SQL Specification](#query-specification-sql_spec)
    - [Data Types](#query-specification-data_type)
    - [Operators](#query-specification-operators)
    - [Basic Functions](#query-specification-functions)
    - [Advanced Functions](#query-specification-window_function)
      - [Window Functions](#query-specification-window_function)
      - [Multi-Dimension Analysis](#query-specification-grouping_function)
      - [Bitmap Functions](#query-specification-bitmap_function)
      - [Intersect Functions](#query-specification-intersect_function)
  - [Query Tuning](#query-tuning-data_skipping)
    - [Data Skipping](#query-tuning-data_skipping)
    - [Query Specific Model](#query-tuning-model_priority)
    - [Sum Expression](#query-tuning-sum_expression)
    - [Count-distinct Expression](#query-tuning-count_distinct_expr)
    - [Equivalent Semantics Query](#query-tuning-query_enhanced)
  - [Pushdown](#query-push_down)
  - [Query History](#query-history-query_history)
    - [Guide](#query-history-query_history)
    - [Table Schema](#query-history-query_history_fields)
  - [Asynchronous Query](#query-async_query)
- [Maintenance Guide](#operations-intro)
  - [Overview](#operations-overview)
  - [Project Managing](#operations-project-managing-intro)
    - [Project Management](#operations-project-managing-project_management)
    - [Project Settings](#operations-project-managing-project_settings)
    - [Tool Bar](#operations-project-managing-toolbar)
    - [Job Status Alert](#operations-project-managing-alerting)
  - [Access Control](#operations-access-control-intro)
    - [User Management](#operations-access-control-user_management)
    - [User Group Management](#operations-access-control-group_management)
    - [Data Access Control](#operations-access-control-data-access-control-intro)
      - [Project Access Control](#operations-access-control-data-access-control-project_acl)
  - [System Operation](#operations-system-operation-intro)
    - [Diagnosis](#operations-system-operation-diagnosis-intro)
      - [System, Job and Query Diagnosis](#operations-system-operation-diagnosis)
      - [Query Flame Graph](#operations-system-operation-diagnosis-query_flame_graph)
      - [Build Flame Graph](#operations-system-operation-diagnosis-build_flame_graph)
    - [Update Session Table Tool](#operations-system-operation-update-session-table)
    - [CLI Operation Tool](#operations-system-operation-cli_tool-intro)
      - [Environment Check](#operations-system-operation-cli_tool-environment_check)
      - [Diagnostic Package](#operations-system-operation-cli_tool-diagnosis)
      - [Metadata Operation](#operations-system-operation-cli_tool-metadata_operation)
      - [Rollback Tool](#operations-system-operation-cli_tool-rollback)
    - [Kylin Guardian Process](#operations-system-operation-guardian)
    - [Junk File Cleanup](#operations-system-operation-junk_file_clean)
    - [Limit query current capacity, protect query stability](#operations-system-operation-limit_query)
  - [Job Monitoring](#operations-job-monitoring-intro)
    - [Job Concept and Settings](#operations-job-monitoring-job_concept_settings)
    - [Job Operations](#operations-job-monitoring-job_operations)
    - [Job Diagnosis](#operations-job-monitoring-job_diagnosis)
    - [Common Job Error Causes and Solutions](#operations-job-monitoring-job_exception_resolve)
  - [System Monitoring](#operations-system-monitoring-intro)
    - [InfluxDB](#operations-system-monitoring-influxdb-intro)
      - [Use InfluxDB as Time-Series Database](#operations-system-monitoring-influxdb)
      - [InfluxDB Maintenance](#operations-system-monitoring-influxdb-influxdb_maintenance)
    - [Metrics Monitoring](#operations-system-monitoring-metrics_intro)
    - [Service Monitoring](#operations-system-monitoring-service)
  - [Logs](#operations-logs-intro)
    - [System Log](#operations-logs-system_log)
    - [Audit Log](#operations-logs-audit_log)
- [Integration](#integration-intro)
  - [Kylin JDBC Driver](#integration-jdbc)
- [Rest API](#restapi-intro)
  - [Access and Authentication](#restapi-authentication)
  - [Project Management](#restapi-project_api)
  - [Model Management](#restapi-model_api-intro)
    - [Model Data Loading](#restapi-model_api-model_build_api)
    - [Model Import & Export](#restapi-model_api-model_import_and_export_api)
    - [Multi-level Partitioning](#restapi-model_api-model_multilevel_partitioning_api)
  - [Segment Management](#restapi-segment_management_api)
  - [Snapshot Management](#restapi-snapshot_management_api)
  - [Query](#restapi-query_api)
  - [Data Source](#restapi-data_source_api)
  - [Custom Parser Jar Management](#restapi-custom_jar_manager_api)
  - [Async Query](#restapi-async_query_api)
  - [Job Management](#restapi-job_api)
  - [ACL Management API](#restapi-acl_api-intro)
    - [User Management](#restapi-acl_api-user_api)
    - [User Group Management](#restapi-acl_api-user_group_api)
    - [Project ACL](#restapi-acl_api-project_acl_api)
  - [Use callback API to monitor job status](#restapi-callback_api)

## Content

<a id="overview"></a>

<!-- source_url: https://kylin.apache.org/docs/overview/ -->

<!-- page_index: 1 -->

# Overview

Version: 5.0.2

Apache Kylin is a leading open source OLAP engine for Big Data capable for sub-second query latency on trillions of records. Since being created and open sourced by eBay in 2014, and graduated to Top Level Project of Apache Software Foundation in 2015.
Kylin has quickly been adopted by thousands of organizations world widely as their critical analytics application for Big Data.

Kylin has following key strengths:

- High qerformance, high concurrency, sub-second query latency
- Unified big data warehouse architecture
- Seamless integration with BI tools
- Comprehensive and enterprise-ready capabilities

Kylin now support internal table, which is designed for flexible query and lakehouse scenarios.

> More details, please refer to [Internal Table](#internaltable-intro)

With recommendation engine, you don't have to be an expert of modeling. Kylin now can auto modeling and optimizing indexes from you query history.
You can also create model by importing sql text.

> More details, please refer to [Auto Modeling](#model-rec-sql_modeling) and [Index Optimization](https://kylin.apache.org/docs/model/rec/optimize_index/intro)

Start from version 5.0, Kylin has integrated Gluten-Clickhosue Backend(incubating in apache software foundation) as native compute engine. And use Gluten mergetree as the default storage format of internal table.
Which can bring 2~4x performance improvement compared with vanilla spark. Both model and internal table queries can get benefits from the Gluten integration.

> Know more about [Gluten-Clickhosue Backend](https://github.com/apache/incubator-gluten)

Kylin now support Apache Kafka as streaming data source of model building. Users can create a fusion model to implement streaming-batch hybrid analysis.

In Kylin 5.0, we have refactored the metadata storage structure and the transaction process, removed the project lock and Epoch mechanism. This has significantly improved transaction interface performance and system concurrency capabilities.

To upgrade from 5.0 alpha, beta, follow the [Metadata Migration Guide](#operations-system-operation-cli_tool-metadata_operation--migration)

The metadata migration tool for upgrading from Kylin 4.0 is not tested, please contact kylin user or dev mailing list for help.

Please refer to [Release Notes](https://kylin.apache.org/docs/release_notes) for more details.

---

<a id="quickstart-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/quickstart/intro/ -->

<!-- page_index: 2 -->

# Quick Start

Version: 5.0.2

In this guide, we will explain how to quickly install and start Kylin 5. Before you begin, ensure you have met the [Prerequisites](#deployment-prerequisite).

To explore new features in Kylin 5 on a laptop, we recommend pulling the Docker image and checking the [Apache Kylin Standalone Image on Docker Hub](https://hub.docker.com/r/apachekylin/apache-kylin-standalone) (For amd64 platform).

```shell
docker run -d \ 
    --name Kylin5-Machine \ 
    --hostname localhost \ 
    -e TZ=UTC \ 
    -m 10G \ 
    -p 7070:7070 \ 
    -p 8088:8088 \ 
    -p 9870:9870 \ 
    -p 8032:8032 \ 
    -p 8042:8042 \ 
    -p 2181:2181 \ 
    apachekylin/apache-kylin-standalone:5.0.2-GA 
```

1. Check the version of `curl`.

   Since `check-env.sh` needs to rely on the support of GSS-Negotiate during the installation process, it is recommended that you check the relevant components of your curl first. You can use the following commands in your environment:


```shell
curl --version 
```

   If GSS-Negotiate is displayed in the interface, the curl version is available. If not, you can reinstall curl or add GSS-Negotiate support.
   ![Check GSS-Negotiate dependency](assets/images/gss-negotiate-17cf6c5ee24cabf516a51e2cec2c3635_2736d62ce5576292.png)
2. Start Kylin with the startup script.
   Run the following command to start Kylin. When it is first started, the system will run a series of scripts to check whether the system environment has met the requirements. For details, please refer to the [Environment Dependency Check](#operations-system-operation-cli_tool-environment_check) chapter.


```shell
${KYLIN_HOME}/bin/kylin.sh start 
```

   >
> [!NOTE]
> ：If you want to observe the detailed startup progress, run:

   >
   >
```shell
tail -f $KYLIN_HOME/logs/kylin.log 
```

Once the startup is completed, you will see information prompt in the console. Run the command below to check the Kylin process at any time.

```shell
ps -ef | grep kylin 
```

3. Get login information.

   After the startup script has finished, the random password of the default user `ADMIN` will be displayed on the console. You are highly recommended to save this password. If this password is accidentally lost, please refer to [ADMIN User Reset Password](#operations-access-control-user_management).

After Kylin is started, open web GUI at `http://{host}:7070/kylin`. Please replace `host` with your host name, IP address, or domain name. The default port is `7070`.

The default user name is `ADMIN`. The random password generated by default will be displayed on the console when Kylin is started for the first time. After the first login, please reset the administrator password according to the password rules.

- At least 8 characters.
- Contains at least one number, one letter, and one special character `` (~!@#$%^&*(){}|:"<>?[];',./`) ``.

Kylin uses the open source **SSB** (Star Schema Benchmark) dataset for star schema OLAP scenarios as a test dataset. You can verify whether the installation is successful by running a script to import the SSB dataset into Hive. The SSB dataset is from multiple CSV files.

**Import Sample Data**

Run the following command to import the sample data:

```shell
$KYLIN_HOME/bin/sample.sh 
```

The script will create 1 database **SSB** and 6 Hive tables then import data into it.

After running successfully, you should be able to see the following information in the console:

```shell
Sample hive tables are created successfully 
```

We will be using SSB dataset as the data sample to introduce Kylin in several sections of this product manual. The SSB dataset simulates transaction data for the online store, see more details in [Sample Dataset](#quickstart-tutorial--ssb). Below is a brief introduction.

| Table | Description | Introduction |
| --- | --- | --- |
| CUSTOMER | customer information | includes customer name, address, contact information .etc. |
| DATES | order date | includes a order's specific date, week, month, year .etc. |
| LINEORDER | order information | includes some basic information like order date, order amount, order revenue, supplier ID, commodity ID, customer Id .etc. |
| PART | product information | includes some basic information like product name, category, brand .etc. |
| P\_LINEORDER | view based on order information table | includes all content in the order information table and new content in the view |
| SUPPLIER | supplier information | includes supplier name, address, contact information .etc. |

**Validate Product Functions**

You can create a sample project and model according to [Kylin 5 Tutorial](#quickstart-tutorial). The project should validate basic features such as source table loading, model creation, index build etc.

On the **Data Asset -> Model** page, you should see an example model with some storage over 0.00 KB, this indicates the data has been loaded for this model.

![model list](assets/images/list-937cf4c5daadc5064e0704069c2aaf72_eb966d91cda01d89.png)

On the **Monitor** page, you can see all jobs have been completed successfully in **Batch Job** pages.

![job monitor](assets/images/job-08ffdf6b9f8c88274d88ee2dcb727e82_9222294570a53bd0.png)

**Validate Query Analysis**

When the metadata is loaded successfully, at the **Insight** page, 6 sample hive tables would be shown at the left panel. User could input query statements against these tables. For example, the SQL statement queries different product group by order date, and in descending order by total revenue:

```sql
SELECT LO_PARTKEY, SUM(LO_REVENUE) AS TOTAL_REVENUE 
FROM SSB.P_LINEORDER 
WHERE LO_ORDERDATE between '1993-06-01' AND '1994-06-01' 
group by LO_PARTKEY 
order by SUM(LO_REVENUE) DESC 
```

The query result will be displayed at the **Insight** page, showing that the query hit the sample model.

![query result](assets/images/installation-query-result-e225144d2aaf61c06c73717590e3fda5_7f99cf0320ddcba8.png)

You can also use the same SQL statement to query on Hive to verify the result and performance.

Run the following command to stop Kylin:

```shell
$KYLIN_HOME/bin/kylin.sh stop 
```

You can run the following command to check if the Kylin process has stopped.

```shell
ps -ef | grep kylin 
```

**Q: How do I change the service default port?**

You can modify the following configuration in the `$KYLIN_HOME/conf/kylin.properties`, here is an example for setting the server port to 7070.

```properties
server.port=7070 
```

**Q: Is the query pushdown engine turned on by default?**

Yes, if you want to turn it off, please refer to [Pushdown to SparkSQL](#query-push_down).

---

<a id="quickstart-tutorial"></a>

<!-- source_url: https://kylin.apache.org/docs/quickstart/tutorial/ -->

<!-- page_index: 3 -->

# Kylin Tutorial

Version: 5.0.2

In this section, we will show you how to create and optimize model.

1. You are able to design your own models to fulfill your analysis demands and load data for your models. You can design the index manually and let the system continue to improve the index according your query habits and data characteristics.
2. We will use the SSB (Star Schema Benchmark) sample data to introduce the project. You can find out how to import the sample data in the [Import Data from Hive](#datasource-import_hive) section.

Project is the primary management unit of Kylin. In a project, you can design multiple models and perform query analysis.

In Kylin toolbar, click the **+** (Add Project) button to the right of the item list to add a project, and fill in the project name and description. The project name is mandatory; the project description is optional. A good project description will help with the maintenance of the project in the future.

At this point, you have completed the creation project. The interface stays in the **Data Asset -> Data Source** page, ready to add data sources for the next step.

Once the project is created, you need to add a data source table to the project. The data source tables added here will be used during model creation stage and/or query analysis.

When you add a data source, the metadata of the source table is synchronized. The metadata of a table is the data that describes the characteristics of the table e.g. table names, column names, types etc.

1. **Import Table Metadata**

   In the **Data Asset -> Data Source** interface, click the **Add data source** button at the top left to add a data source table for your project.

   - Select data source type: Hive.
   - Select the target data source table: Expand the database list and select the target data source table.

   For more information on data source operations, please see the [Data Source](#datasource-intro) section.
2. **Table Sampling**

   During the table metadata synchronization process, the data sampling is turned on by default. You can view the auto-launched **sample table data** job in the **Monitor -> Job** page. Once the job has been executed, you can view the sample data from the source table in the **Data Asset -> Data Source** interface. You can find out more in the [Data Sampling](#datasource-data_sampling)) section.

   In general, table sampling will answer questions like those listed below. Understanding these will help with the subsequent model design.

   - How many rows are there in the table?
   - What is the cardinality of each column? That is, the amount of data that is not repeated.
   - What are the characteristics of the column values for each column?
3. **Data Source Interface**

   As shown in the following diagram, we added all the tables in the sample SSB dataset in Hive. The data source area is on the left and the information of the specified source table is on the right.

   You can view the source table information on the right side, where **all columns** are the feature information of the source table field, **sampled data** shows the data of each column in the source table.

   ![Data Source](assets/images/datasource-72cc42dd54d72596a254a7e81ee3af14_b0c1a47dcf0957af.png)

Model design is one of the core functions of Kylin. Good model design can help achieve a better data analysis experience.

1. **Principles of Model Design**

   The model is the semantic layer. A good model can help users visualize the business relationships between the source tables.

   In Kylin, you can view the data source tables in a single panel, complete model design, add dimensions and metrics, and design a model that fits your business logic. Basic principles in a model design:

   - Fact Table: Generally a table with quantifiable measures. For example, the order table is a suitable fact table. There are columns like the order quantity, order amount can be quantified.
   - Dimension Table: A table that represents a perspective looking into the quantifiable measures. For example, the product information table is suitable as a dimension table, and there are product categories and product trademarks, which can be angles to analyze business. Schedules are often used as dimension tables to partition business data by day/week/month/quarter/year.
   - Dimensions: Represents a business angle that can be analyzed, such as the order date indicating the time dimension and the item ID indicating the product dimension.
   - Metrics: Quantifiable numerical information such as total sales, total sales, etc. Usually quantifiable columns are used with functions such as SUM, COUNT, TOP\_N, and so on.
2. **Method of Model Design**

   Please create a model in the **Data Asset -> Model** interface and enter the model editing interface to visually complete the creation of the multidimensional model. The specific method of model design will be described in detail in the [Model Design Basics](#model-intro) section. Here is a brief introduction to the following steps:

   - Design Model: Select the source table according to the business logic and set the association between the tables. Then set the fact table and dimension tables.
   - Add Dimensions: Identify dimensions from table columns for business analysis.
   - Add Measures: Identify metrics and their aggregate functions for business analytics. You can see the detailed methods in the [Measures](#model-features-measures-intro) section.

   As shown in the following diagram, we built the model using the source tables in the SSB dataset.

   ![Model Design](assets/images/model-cfa237b22396c105ccea136117e124aa_98ec6b1540aaa848.png)

After the model is created, you need to define the index in the model; this should be based on the business analysis you are interested in. Good index design can improve system efficiency and save storage space. When you save a model design, you will often be reminded to add an index.

1. **Principles of designing an index**

   Not every dimension combination is needed for business analysis. In this case, pre-calculating all the dimension combinations will bring a large workload and can result in a long indexing time and a large data storage space. We can improve this by adding aggregate index and table index.

   - Aggregate Index: A group of dimension combinations customized to a particular business analysis. For example, an online store analyst needs to analyze the purchasing power of male and female customers in different cities, and the dimension combination in the index is `[city, customer gender]`. At this time, other dimensions are not needed in the index. If you do not need to analyze the product category, then there is no need to include it in any index. You can find out more in the [Aggregate Index](#model-manual-aggregation_group) section.
   - Table Index: Table index supports efficient querying of detailed data records. For example, an online store analyst needs to query the detailed order data, they can add `[OrderKey, OrderDate, PartKey, CustomerKey, OrderQuantity, OrderAmount]` in a table index. After building the index and loading the data, they can query the detailed data records efficiently. You can find out more in the [Table Index](#model-manual-table_index) section.
2. **How to design an index**

   - Edit aggregate group: On the left navigation bar, click **Data Asset -> Model**. In the **Model List** page, click one model to enter the specific model page, click **Index**. In the **Index Overview** tab, click **+ Index -> Aggregate Group**. The diagram below shows an aggregation group in the built-in demo. There are basically four concepts in an aggregation group in order to control the combination of dimensions:

     - Included Dimensions: Select the dimensions that need to appear in the index from the list of dimensions in the model.
     - Mandatory Dimension: The dimension corresponding to the business angle that must be analyzed e.g. customer statistics.
     - Hierarchy Dimensions: Dimensions with hierarchical relationships e.g. countries, provinces, and cities.
     - Joint Dimensions: Dimensions that must appear together e.g. the supplier and the order date

     ![Edit Aggregate Index](assets/images/agg-group-c4e02cdd2ead5f7bf43269a3247393f1_d07561345cf34243.png)
   - Add table index: On the left navigation bar, click **Data Asset -> Model**. In the **Model List** page, click one model to enter the specific model page, click **Index**. In the **Index Overview** tab, click **+ Index -> Table Index**. You can select the dimensions you need in the table index and build the index.

Kylin applies pre-calculation technology to achieve sub-second query response time in the big data era. After creating the model and editing the index, you need to load the data for the model. The process of loading data is also the pre-calculation process for the pre-defined index. Models that do not have data loaded cannot serve queries. You can find out more about how to load data from the [Load Data](#model-manage-data_loading) section.

1. **Principle of Loading Data**

   - Set time partition column: The data in the fact table in the model generally increases over time, such as new orders grow over time in the order table. Then the order date can be the time partition column to partition orders into daily incremental batches. Setting the time partition column occurs after saving the model design.
   - Full load: When the model does not have a time partition column, then data in fact table is loaded fully every time. If you need to load the latest week of data in the order table, all data will be reloaded because the model does not have a time partition column. You can find out more in the [Full Load](#model-manage-data_loading--full-load) section.
   - Incremental load: When the model has been built and put into business analysis, and the model has a time partition column, you can still incrementally load new data while serving queries. For example, new data in the order table can be loaded incrementally daily. Incremental loading eliminates the need to reload pre-calculated data, this increases productivity and saves resources. Learn more [Model Incremental Loading](#model-manage-data_loading--incremental-load).
2. **How to Load Data**

   There are a few options to load data and build the index.

   - Load data: On the left navigation bar, click **Data Asset -> Model**, choose to load the data of a model. If the model has a time partition column, you can choose a time range for this data load. The system will launch a new job to load the data of specified time period and build the index at the same time.
   - Build index: On the left navigation bar, click **Data Asset -> Model**. In the **Model List** page, click one model to enter the specific model page, click **Index**. You can edit and modify the aggregate index or detail index of the specified model in the **Index Overview** tab , and select which indexes need to be built to the specified data range.
3. **View Storage Size**

   To view storage size, click **Data Asset -> Model** in the left navigation bar. Then you can check the **Storage** column to view the storage size. If the number is 0.00 KB, the model has no data. If the storage size is larger than 0.00 KB, it means that the model has been loaded with data.

   As shown in the following diagram, the model named *Model3* has loaded data, and the model named *Model* is empty. Queries can't hit the model *Model*.

   ![Model List](assets/images/dataload-25a7749d0de2bc638be8993365c1671f_b0538129dffd625f.png)

You can submit a query to analyze your business data and experience the sub-second response time that Kylin offers.

1. **Query Analysis Principles**

   Kylin supports standard SQL queries. After you add a data source table, the query is already pushed down to the Hive data source. You can immediately query the data; however, we do not recommend doing so at this time. Doing so immediately, especially when the data volume is high or the query is complex, can cause the query execution to take a long time.

   Once you have the model and index created and have data loaded in the model, new queries can then hit the model and the pre-calculated data saved in the model will be used to answer queries. This accelerated query execution method can be 10x to 100x faster. You can read the [Query Analysis](https://kylin.apache.org/docs/query/principles/precalculation) section for a detailed explanation of SQL statements.

   Your history query will be saved in the **Query -> History** page, you can view the [Query History](#query-history-query_history) section for more information.
2. **Query Analysis Example**

   After you import the SSB test dataset, you can navigate to the **Query -> Insight** page, in the **SQL Editor** enter the following SQL statement. The data source we use is the SSB dataset simulating the transactions of an online store. The SQL statement is to query the revenue of different items within the specified order time range, and the results are sorted in descending order of revenue.


```sql
SELECT LO_PARTKEY, SUM(LO_REVENUE) AS TOTAL_REVENUE 
FROM SSB.P_LINEORDER 
WHERE LO_ORDERDATE between '1993-06-01' AND '1994-06-01'  
group by LO_PARTKEY 
order by SUM(LO_REVENUE) DESC 
```

   The result of the query is shown in the diagram below. You can find the query object in the query information as *test\_model*, which is the model created in the built-in demo. The results of the example query above shows the revenue of different products in the online store.

   ![Query result](assets/images/query-result-9d98b286e3080cecbcf06d3f88930f85_5411ed2fac449227.png)

Different jobs are triggered during the process of using Kylin, such as the job of building index, loading data, and sampling table. You can view the job list in the navigation bar **Monitor -> Job** interface. For more detailed instructions, please see the [Monitor Job](#operations-system-monitoring-intro) section.

Job monitoring can help you effectively manage the use of Kylin. You can check the status of the job to determine whether the operation is complete, whether the operating environment is stable, and so on. The following diagram shows the job monitoring interface in the built-in demo where all jobs are successfully completed.

![Job Monitoring](assets/images/job-08ffdf6b9f8c88274d88ee2dcb727e82_9222294570a53bd0.png)

Kylin is embedded with a standard SSB dataset (approximately 5.9 MB) for testing or trying out different functions. This SSB dataset contains 5 tables and 1 view. LINEORDER serves as a central fact table with 60,175 rows of data.

The following table lists the 5 tables and 1 view of SSB sample dataset.

| **Table** | **Type** | **Description** |
| --- | --- | --- |
| **LINEORDER** | Fact table | Contain detailed information about sales orders. Each row holds order information such as customer, supplier, order amount, and order date. |
| **P\_LINEORDER** | View based on fact table | Contain details about sales orders and a pre-calculated row (V\_REVENUE) with same transaction records as in LINEORDER. |
| **CUSTOMER** | Dimension table | Contain customer information, such as customer name, customer address, and customer city. |
| **SUPPLIER** | Dimension table | Contain supplier information, such as supplier name, supplier address, and supplier city. |
| **DATES** | Dimension table | Contain information about the dates of 7 years, such as beginning date of the year, beginning date of the month, and beginning date of the week. |
| **PART** | Dimension table | Contain part information, such as part name, part category, part color, and part type. |

The 5 tables together constitute the structure of the entire star data model. Below is an entity-relationship (E-R) diagram.

![Entity-relationship diagram](assets/images/dataset-d22cdf576e3d87e0f1a2b4531b6a5d60_82abfe5a8b6993d5.png)

Join Relationships:

```sql
P_LINEORDER INNER JOIN DATES ON P_LINEORDER.LO_ORDERDATE=DATES.D_DATEKEY 
P_LINEORDER INNER JOIN CUSTOMER ON P_LINEORDER.LO_CUSTKEY=CUSTOMER.C_CUSTKEY 
P_LINEORDER INNER JOIN PART ON P_LINEORDER.LO_PARTKEY=PART.P_PARTKEY 
P_LINEORDER INNER JOIN SUPPLIER ON P_LINEORDER.LO_SUPPKEY=SUPPLIER.S_SUPPKEY 
```

1. Log on to the server command line, and run the following command to import the SSB sample dataset:


```shell
$KYLIN_HOME/bin/sample.sh 
```

   > [!NOTE]
   >
   > Replace `KYLIN_HOME` with the actual path of Kylin.
2. To check sample dataset:

   1. In the terminal, run `hive` command to enter Hive CLI.
   2. Run the following commands sequentially to check information about databases and tables.


```sql
## List all databases 
show databases; 
## Enter database SSB 
use ssb; 
## List all tables in database SSB  
show tables; 
## Query the number of records in table SUPPLIER  
select count(*) from SUPPLIER; 
```

| Column | Description |
| --- | --- |
| LO\_ORDERKEY | Order ID |
| LO\_CUSTKEY | Customer ID |
| LO\_PARTKEY | Part ID |
| LO\_SUPPKEY | Supplier ID |
| LO\_ORDERDATE | Order date |
| LO\_ORDERPRIORITY | Order priority |
| LO\_SHIPPRIORITY | Ship priority |
| LO\_LINENUMBER | Compound primary key: L\_ORDERKEY, L\_LINENUMBER |
| LO\_QUANTITY | Number of purchased goods |
| LO\_EXTENDEDPRICE | Extended price of order |
| LO\_ORDTOTALPRICE | Total price of order |
| LO\_DISCOUNT | Order discount |
| LO\_REVENUE | Order revenue |
| LO\_SUPPLYCOST | Supplier cost |
| LO\_TAX | Tax |
| LO\_COMMITDATE | Commit date |
| LO\_SHIPMODE | Ship mode |

| Column | Description |
| --- | --- |
| C\_CUSTKEY | Customer ID |
| C\_NAME | Customer name |
| C\_ADDRESS | Customer address |
| C\_CITY | Customer city |
| C\_NATION\_PREFIX | Nation prefix |
| C\_NATION | Customer nation |
| C\_REGION | Customer region |
| C\_PHONE | Customer phone number |
| C\_MKTSEGMENT | Market segment |

| Column | Description |
| --- | --- |
| S\_SUPPKEY | Supplier ID |
| S\_NAME | Supplier name |
| S\_ADDRESS | Supplier address |
| S\_CITY | Supplier city |
| S\_NATION\_PREFIX | Nation prefix |
| S\_NATION | Supplier nation |
| S\_REGION | Supplier region |
| S\_PHONE | Supplier phone number |

| Column | Description |
| --- | --- |
| D\_DATEKEY | Date ID |
| D\_DATE | Date |
| D\_DAYOFWEEK | Day of week |
| D\_MONTH | Month |
| D\_YEAR | Year |
| D\_YEARMONTHNUM | Num of year and month |
| D\_YEARMONTH | Year and month |
| D\_DAYNUMINWEEK | Num of days in a week |
| D\_DAYNUMINMONTH | Num of days in a month |
| D\_DAYNUMINYEAR | Num of days in a year |
| D\_MONTHINYEAR | Num of months in a year |
| D\_WEEKNUMINYEAR | Num of weeks in a year |
| D\_SELLINGSEASON | Selling season |
| D\_LASTDAYINWEEKFL | Last day in one fiscal week |
| D\_LASTDAYINMONTHFL | Last day in one fiscal month |
| D\_HOLIDAYFL | Holiday in one fiscal year |
| D\_WEEKDAYFL | Weekday in one fiscal year |

| Column | Description |
| --- | --- |
| P\_PARTKEY | Part ID |
| P\_NAME | Part name |
| P\_MFGR | Part manufacturer |
| P\_CATEGORY | Part category |
| P\_BRAND | Part brand |
| P\_COLOR | Part color |
| P\_TYPE | Part type |
| P\_SIZE | Part size |
| P\_CONTAINER | Part container |

---

<a id="deployment-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/deployment/intro/ -->

<!-- page_index: 4 -->

# Deployment Overview

Version: 5.0.2

This chapter will introduce how to deploy kylin on different mode.

To get started, let's first understand the main components of Kylin:

Kylin support using MySQL or PostgresQL as metadata database. It stores all the metadata of Kylin System, including projects, tables, models, indexes, jobs, users etc.

Besides, some user's data like query history and audit log are also stored in the metadata database.

Kylin support using HDFS or S3 compatible file system as the data storage engine.

Though you can re-use your data source hadoop cluster, we recommend using an independent HDFS cluster as the data storage component to get better performance.

From version 5.0, Kylin support internal table and using Apache Gluten(Clickhouse backend) as native compute engine, which relies on local cache to accelerate query performance.

The soft affinity of local cache is enabled by default, which means Kylin will automatically distribute the cached data files evenly across all the spark worker nodes in the cluster.

We recommend using SSD disk for local cache storage to get better performance.

Kylin uses the built-in Apache Spark as the data compute engine. It can run on Yarn or Standalone mode.

You can find the download script in the `${KYLIN_HOME}/sbin` directory.

As we introduced above in [2.1 Local Cache](#deployment-intro--21-local-cache), Gluten use local cache to accelerate query performance. To reduce the cache loading time in first time launching, we recommend to set up an independent Spark Standalone cluster as the query compute cluster. So that Kylin(Gluten) can re-use the old cache data after a restart.

We don't recommend to run on hadoop yarn because the yarn container allocation is not under controlled. So the local cache re-use is not supported on yarn mode.

While for data loading job, it's free for you to run on yarn or standalone cluster since it doesn't need cache re-use.

Kylin Server is the front-end service and query client of Kylin. It provides a web UI for users to manage tables, design models, trigger jobs and maintain the configurations.

It has three server modes:

| Server Mode | Description |
| --- | --- |
| query | query node only provides query service, all the job and transaction request will be transferd to job or all nodes. |
| job | job node don't provide query service, but only served for job and transaction request. |
| all | all node can serve all the query, job and transaction service. |

you can configure the `server.mode` property in the `kylin.properties` file.

One Kylin query node has a built-in spark application, which is named as 'Sparder'. Its driver runs inside the Kylin JVM and executors run on query cluster(Yarn or Spark Standalone).

Kylin data loading job support both yarn client or cluster mode. The difference is in client mode the driver process run on the Kylin node and will utilize some local resources accordingly.

---

<a id="deployment-prerequisite"></a>

<!-- source_url: https://kylin.apache.org/docs/deployment/prerequisite/ -->

<!-- page_index: 5 -->

# Prerequisite

Version: 5.0.2

To ensure system performance and stability, we recommend you run Kylin on a dedicated Hadoop cluster.

Prior to installing Kylin, please check the following prerequisites are met.

- Environment
  - [Supported Hadoop Distributions](#deployment-prerequisite--hadoop)
  - [Java Environment](#deployment-prerequisite--java)
  - [Account Authority](#deployment-prerequisite--account)
  - [Metastore Configuration](#deployment-prerequisite--metadata)
  - [Check Zookeeper](#deployment-prerequisite--zookeeper)
  - [Network Port Requirements](#deployment-prerequisite--ports)
- Recommended Resource and Configuration
  - [Hadoop Cluster Resource Allocation](#deployment-prerequisite--resource)
  - [Recommended Hardware Configuration](#deployment-prerequisite--hardware)
  - [Recommended Linux Distribution](#deployment-prerequisite--linux)
  - [Recommended Client Configuration](#deployment-prerequisite--client)

The following Hadoop distributions are verified to run on Kylin.

- Apache Hadoop 3.2.1

Kylin requires some components, please make sure each server has the following components.

- Hive
- HDFS
- Yarn
- ZooKeeper

First, **make sure you allocate sufficient resources for the environment**. Please refer to [Prerequisites](#deployment-prerequisite) for detailed resource requirements for Kylin. Moreover, please ensure that `HDFS`, `YARN`, `Hive`, `ZooKeeper` and other components are in normal state without any warning information.

Add the following two configurations in `$KYLIN_HOME/conf/kylin.properties`:

- `kylin.env.apache-hadoop-conf-dir` Hadoop conf directory in Hadoop environment
- `kylin.env.apache-hive-conf-dir` Hive conf directory in Hadoop environment

In Apache Hadoop 3.2.1, you also need to prepare the MySQL JDBC driver in the operating environment of Kylin.

Download MySQL 8.0 JDBC driver：<https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/mysql-connector-java-8.0.30.jar>.
Please place the JDBC driver in the `$KYLIN_HOME/lib/ext` directory.

Kylin requires:

- Requires your environment's default JDK version is 8 （JDK 1.8\_162 or above small version）

```shell
java -version 
```

You can use the following command to check the JDK version of your existing environment, for example, the following figure shows JDK 8

![JDK version](assets/images/jdk-021e7c9b0cde81e0d262d91e63d524a0_f078896a5e0531bd.png)

The Linux account running Kylin must have the required access permissions to the cluster. These permissions include:

- Read/Write permission of HDFS
- Create/Read/Write permission of Hive table

Verify the user has access to the Hadoop cluster with account `KyAdmin`. Test using the steps below:

1. Verify the user has HDFS read and write permissions

   Assuming the HDFS storage path for model data is `/kylin`, set it in `conf/kylin.properties` as:


```properties
kylin.env.hdfs-working-dir=/kylin 
```

   The storage folder must be created and granted with permissions. You may have to switch to HDFS administrator (usually the `hdfs` user), to do this:


```shell
su hdfs 
hdfs dfs -mkdir /kylin 
hdfs dfs -chown KyAdmin /kylin 
hdfs dfs -mkdir /user/KyAdmin  
hdfs dfs -chown KyAdmin /user/KyAdmin 
```

   Verify the `KyAdmin` user has read and write permissions


```shell
hdfs dfs -put <any_file> /kylin 
hdfs dfs -put <any_file> /user/KyAdmin    
```

2. Verify the `KyAdmin` user has Hive read and write permissions

   Let's say you want to store a Hive table `t1` in Hive database `kylinDB`, The `t1` table contains two fields `id, name`.

   Then verify the Hive permissions:


```shell
#hive 
hive> show databases; 
hive> use kylinDB; 
hive> show tables; 
hive> insert into t1 values(1, "kylin"); 
hive> select * from t1; 
```

A configured metastore is required for this product.

We recommend using PostgreSQL 10.7 as the metastore, which is provided in our package. Please refer to [Use PostgreSQL as Metastore (Default)](#deployment-rdbms_metastore-usepg_as_metadb) for installation steps and details.

If you want to use your own PostgreSQL database, the supported versions are below:

- PostgreSQL 9.1 or above

You can also choose to use MySQL but we currently don't provide a MySQL installation package or JDBC driver. Therefore, you need to finish all the prerequisites before setting up. Please refer to [Use MySQL as Metastore](#deployment-rdbms_metastore-use_mysql_as_metadb) for installation steps and details. The supported MySQL database versions are below:

- MySQL 5.1-5.7
- MySQL 5.7 (recommended)

The following steps can be used to quickly verify the connectivity between ZooKeeper and Kylin after Kerberos is enabled.

1. Find the ZooKeeper working directory on the node where the ZooKeeper Client is deployed
2. Add or modify the Client section to the `conf/jaas.conf` file:


```shell
Client { 
  com.sun.security.auth.module.Krb5LoginModule required 
  useKeyTab=true 
  keyTab="/path/to/keytab_assigned_to_kylin" 
  storeKey=true 
  useTicketCache=false 
  principal="principal_assigned_to_kylin"; 
}; 
```

3. `export JVMFLAGS="-Djava.security.auth.login.config=/path/to/jaas.conf"`
4. `bin/zkCli.sh -server ${kylin.env.zookeeper-connect-string}`
5. Verify that the ZooKeeper node can be viewed normally, for example: `ls /`
6. Clean up the new Client section in step 2 and the environment variables `unset JVMFLAGS` declared in step 3

If you download ZooKeeper from the non-official website, you can consult the operation and maintenance personnel before performing the above operations.

Kylin needs to communicate with different components. The following are the ports that need to be opened to Kylin. This table only includes the default configuration of the Hadoop environment, and does not include the configuration differences between Hadoop platforms.

| Component | Port | Function | Required |
| --- | --- | --- | --- |
| SSH | 22 | SSH to connect to the port of the virtual machine where Kylin is located | Y |
| Kylin | 7070 | Kylin access port | Y |
| Kylin | 7443 | Kylin HTTPS access port | N |
| HDFS | 8020 | HDFS receives client connection RPC port | Y |
| HDFS | 50010 | Access HDFS DataNode, data transmission port | Y |
| Hive | 10000 | HiveServer2 access port | N |
| Hive | 9083 | Hive Metastore access port | Y |
| Zookeeper | 2181 | Zookeeper access port | Y |
| Yarn | 8088 | Yarn Web UI access port | Y |
| Yarn | 8090 | Yarn Web UI HTTPS access port | N |
| Yarn | 8050 / 8032 | Yarn ResourceManager communication port | Y |
| Spark | 4041 | Kylin query engine Web UI default port | Y |
| Spark | 18080 | Spark History Server port | N |
| Spark | (1024, 65535] | The ports occupied by Spark Driver and Executor are random | Y |
| Influxdb | 8086 | Influxdb HTTP port | N |
| Influxdb | 8088 | Influxdb RPC port | N |
| PostgreSQL | 5432 | PostgreSQL access port | Y |
| MySQL | 3306 | MySQL access port | Y |

To ensure Kylin works efficiently, please ensure the Hadoop cluster configurations satisfy the following conditions:

- `yarn.nodemanager.resource.memory-mb` larger than 8192 MB
- `yarn.scheduler.maximum-allocation-mb` larger than 4096 MB
- `yarn.scheduler.maximum-allocation-vcores` larger than 5

If you need to run Kylin in a sandbox or other virtual machine environment, please make sure the virtual machine environment has the following resources:

- No less than 4 processors
- Memory is no less than 10 GB
- The value of the configuration item `yarn.nodemanager.resource.cpu-vcores` is no less than 8

We recommend the following hardware configuration to install Kylin:

- 16 vCore, 64 GB memory
- At least 500GB disk
- For network port requirements, please refer to the [Network Port Requirements](#deployment-prerequisite--ports) chapter.

We recommend using the following version of the Linux operating system:

- Ubuntu 18.04 and above (recommend LTS version)
- Red Hat Enterprise Linux 6.4+ and above
- CentOS 6.4+ and above

- Operating System: macOS / Windows 7 and above
- RAM: 8G or above
- Browser version:
  - Chrome 45 or above
  - Internet Explorer 11 or above

---

<a id="deployment-rdbms_metastore-use_mysql_as_metadb"></a>

<!-- source_url: https://kylin.apache.org/docs/deployment/rdbms_metastore/use_mysql_as_metadb/ -->

<!-- page_index: 6 -->

# Use MySQL as Metadata DB

Version: 5.0.2

Kylin support using MySQL as Metastore DB, this chapter will introduce how to install and configure MySQL as Metastore DB.

1. Supported MySQL versions are:

   - MySQL 5.1 to 5.7, MySQL 5.7 is recommended
   - MySQL 8
2. JDBC driver of MySQL is needed in the Kylin running environment.
3. You can download the JDBC driver jar package of MySQL 8 via the link below, that compatible with the version after 5.6:

   <https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.28/mysql-connector-java-8.0.28.jar>

   For other versions, you will have to prepare independently.
4. Please put the corresponding MySQL's JDBC driver to directory `$KYLIN_HOME/lib/ext`.

The followings are the steps for a `non root` user `abc` installing MySQL 5.7 on CentOS 7( apply to `root` users as well).

1. Create a new directory `/home/abc/mysql`, and locate MySQL intallation package in the directory, excute the following command to unzip the package of `rpm`:


```shell
cd /home/abc/mysql 
tar -xvf mysql-5.7.37-1.el7.x86_64.rpm-bundle.tar 
```

   Then you will have the RPM installment package:

   `mysql-community-common-5.7.37-1.el7.x86_64.rpm`
   `mysql-community-libs-5.7.37-1.el7.x86_64.rpm`
   `mysql-community-client-5.7.37-1.el7.x86_64.rpm`
   `mysql-community-server-5.7.37-1.el7.x86_64.rpm`
   `mysql-community-devel-5.7.37-1.el7.x86_64.rpm`

   > **Note:** please prepare MySQL installaion package by yourself
2. To check if the other version MySQL was already installed in your system environment


```shell
For example 1:  
rpm -qa | grep mysql 
yum -y remove MySQL-server-5.5.61-1.el6.x86_64 
 
For example 2: 
rpm -qa | grep mariadb 
yum -y remove mariadb-libs-5.5.68-1.el7.x86_64 
```

3. Excute the command as the following order to Unzip package of `rpm` following


```shell
rpm2cpio mysql-community-common-5.7.37-1.el7.x86_64.rpm | cpio -idmv 
rpm2cpio mysql-community-libs-5.7.37-1.el7.x86_64.rpm | cpio -idmv 
rpm2cpio mysql-community-client-5.7.37-1.el7.x86_64.rpm | cpio -idmv 
rpm2cpio mysql-community-server-5.7.37-1.el7.x86_64.rpm | cpio -idmv 
```

4. Excute `vi ~/mysql/etc/my.cnf` to edit configuration file, and please add the configuration informationn as follows


```properties
[client] 
port = 3306 
socket=/home/abc/socket/mysql.sock 
[mysql] 
no-auto-rehash 
socket=/home/abc/socket/mysql.sock 
[mysqld] 
user=abc 
basedir=/home/abc/mysql/usr 
datadir=/home/abc/sql_data 
socket=/home/abc/socket/mysql.sock 
secure-file-priv=/home/abc/mysql_files 
port=3306 
```

   Please create folders corresponding to the configuration informantion above :

   - Create folder `usr` in the path of `/home/abc/mysql`
   - Create folder `sql_data` in the path of `/home/abc`
   - Create folder `socket` in the path of `/home/abc`
   - Create folder `mysql_files` in the path of `/home/abc`

   Then, excute the following command in the path of `/home/abc/mysql`


```sh
./usr/bin/mysql_install_db --defaults-file=etc/my.cnf --user=abc --basedir=/home/abc/mysql/usr --datadir=/home/abc/sql_data 
```

5. Excute following command to start MySQL in the path of `/home/abc/mysql`:


```sh
./usr/sbin/mysqld --defaults-file=etc/my.cnf & 
```

6. To check the default password of MySQL 5.7


```sh
cat ./home/abc/.mysql_secret 
```

   Login MySQL 5.7 by using default password


```sh
usr/bin/mysql -u root -p 
```

The following steps illustrate how to connect MySQL as metastore. Here is an example for MySQL 5.7 .

1. Create database `kylin` in MySQL
2. Set configuration item `kylin.metadata.url = {metadata_name}@jdbc` in `$KYLIN_HOME/conf/kylin.properties`,
   please replace `{metadata_name}` with your metadata name in MySQL, for example, `kylin_default_instance@jdbc`, the maximum length of `{metadata_name}` allowed is 29.

   >
> [!NOTE]
> : If the metadata name doesn't exist, it will be automatically created in MySQL. Otherwise, Kylin will use the existing one.

   For example:


```properties
kylin.metadata.url={metadata_name}@jdbc,driverClassName=com.mysql.jdbc.Driver,url=jdbc:mysql://{host}:{port}/kylin?useUnicode=true&characterEncoding=utf8,username={user},password={password},maxTotal=50,maxIdle=8 
```

   The meaning of each parameter is as below, `url`, `username`, and `password` are required parameters. For others, default values will be used if they are not indicated.

   - **driverClassName**: JDBC's driver class name, default value is `com.mysql.jdbc.Driver`;
   - **url**: JDBC's url;
     - **host**：MySQL ip address, whose default value is `localhost`;
     - **port**：MySQL port, whose default value is `3306`. Please use the actual port to replace.
     - **kylin**: Metabase name. Make sure this database `kylin` has been created in MySQL;
   - **username**: JDBC's username;
   - **password**: JDBC's password;
   - **maxTotal**: max number of database's connection number, default value is 50;
   - **maxIdle**: max number of database's waiting connection number, default value is 8;

>
> [!NOTE]
> : if your query SQL contains chinese, please configure the character encoding to utf8 in kylin.metadata.url to avoid confusing query history: useunicode = true & character encoding = utf8

3. Encrypt JDBC password

   If you need to encrypt JDBC's password, you can do it like this：

   **i.** run following commands in `${KYLIN_HOME}`, it will print encrypted password


```shell
./bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s <password> 
```

   **ii.** config properties kylin.metadata.url's password like this


```properties
password=ENC('${encrypted_password}') 
```

   For example, the following assumes that the JDBC password is kylin:

   First, we need to encrypt kylin using the following command


```shell
${KYLIN_HOME}/bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s kylin 
AES encrypted password is:  
YeqVr9MakSFbgxEec9sBwg== 
```

   Then, config kylin.metadata.url like this：


```properties
kylin.metadata.url={metadata_name}@jdbc,driverClassName=com.mysql.jdbc.Driver,url=jdbc:mysql://{host}:{port}/kylin?useUnicode=true&characterEncoding=utf8,username={user},password=ENC('YeqVr9MakSFbgxEec9sBwg=='),maxTotal=20,maxIdle=20 
```

4. If you need to use MySQL cluster deployment, please add `replication` or `loadbalance` in url with `"`. For example:


```properties
#use replication in cluster deployment        
kylin.metadata.url=kylin_default_instance@jdbc,driverClassName=com.mysql.jdbc.Driver,url="jdbc:mysql:replication://localhost:3306,localhost:3307/kylin?useUnicode=true&characterEncoding=utf8",username=root,password=,maxTotal=20,maxIdle=20 
    
#use loadbalance in cluster deployment 
kylin.metadata.url=kylin_default_instance@jdbc,driverClassName=com.mysql.jdbc.Driver,url="jdbc:mysql:loadbalance://localhost:3306,localhost:3307/kylin?useUnicode=true&characterEncoding=utf8",username=root,password=,maxTotal=20,maxIdle=20 
```

5. Make sure that the storage engine used with MySQL is **InnoDB** is not **MyISAM** and that the default storage engine is modified as follows:


```properties
[mysqld] 
default-storage-engine=InnoDB 
```

\*\*Q: After the JDK is upgraded to jdk 8u261, the startup of Kylin fails, indicating that the creation of the admin user failed, what should I do? \*\*

A: When you use JDK 8u261 and use MySQL 5.6 or 5.7 as metastore. Since the version before TLS 1.2 has been disabled since the JDK 8u261, and MySQL 5.6 and 5.7 use TLS 1.0 or TLS 1.1 by default, and MySQL must establish an SSL connection by default, which causes conflicts with the TLS protocol, resulting in the startup of Kylin fails, you will see the error message on the terminal as `Create Admin user failed`.

You have 2 solutions:

Method 1: Modify the metadata configuration parameters and add `useSSL=false`

```properties
kylin.metadata.url={metadata_name}@jdbc,driverClassName=com.mysql.jdbc.Driver,url=jdbc:mysql://{host}:{port}/kylin?useSSL=false,useUnicode=true&characterEncoding=utf8,username={user},password={password},maxTotal=50,maxIdle=8 
```

Method 2: Modify the java security file `java.security`, find the following configuration, delete TLSv1, TLSv1.1

```sh
#  jdk.tls.disabledAlgorithms=MD5, SSLv3, DSA, RSA keySize < 2048
jdk.tls.disabledAlgorithms=SSLv3, TLSv1, TLSv1.1, RC4, DES, MD5withRSA, DH keySize < 1024, EC keySize < 224, 3DES_EDE_CBC, anon, NULL, include jdk.disabled.namedCurves 
```

---

<a id="deployment-rdbms_metastore-usepg_as_metadb"></a>

<!-- source_url: https://kylin.apache.org/docs/deployment/rdbms_metastore/usepg_as_metadb/ -->

<!-- page_index: 7 -->

# Install PostgreSQL

Version: 5.0.2

Kylin supports to use PostgreSQL as Metastore, this chapter will discuss how to:

1. For Kylin, we recommend using PostgreSQL as the default metastore database. The PostgreSQL 10.7 installation package is located in the product package root directory `postgresql`.
2. If using other versions of PostgreSQL, please choose a version above PostgreSQL 9.1.
3. The PostgreSQL installation package currently supports installation in CentOS system, the correspondence is as follows:

   - `rhel6.x86_64.rpm` -> CentOS 6
   - `rhel7.x86_64.rpm` -> CentOS 7
   - `rhel8.x86_64.rpm` -> CentOS 8

   Please check out Linux version before choosing the installation package. You should be able to see your Linux core version by running `uname -a` or `cat /etc/issue`.

   > Note: other system compatible package please refer to [PostgreSQL Website](https://www.postgresql.org/download/).
4. In this section, we will go through a PostgreSQL installation and configuration on CentOS 6.

1. After unzipping the Kylin package, enter the root directory `sbin` and run following commands in order to download PostgreSQL.


```shell
./download_postgresql.sh 
```

2. After unzipping the Kylin package, enter the root directory `postgresql` and run following commands in order to install PostgreSQL.


```shell
rpm -ivh postgresql10-libs-10.7-1PGDG.rhel6.x86_64.rpm 
rpm -ivh postgresql10-10.7-1PGDG.rhel6.x86_64.rpm 
rpm -ivh postgresql10-server-10.7-1PGDG.rhel6.x86_64.rpm 
```

3. Initialize PostgreSQL

   The OS has installed Initscripts services, Please run:


```sh
service postgresql-10 initdb 
```

   The OS not has installed Initscripts services, Please run in the PostgreSQL bin directory:


```sh
$PGSQL_HOME/pgsql-10/bin/postgresql-10-setup initdb 
for example: /user/pgsql-10/bin/postgresql-10-setup initdb 
```

4. Modify two PostgreSQL configuration files, the files are in `/var/lib/pgsql/10/data/`:

   - `pg_hba.conf`: mainly used to store the authentication information of the client.
   - `postgresql.conf`

   **i.** Run `vi pg_hba.conf` to open the file and you can see the following initial setting:


```properties
host    all             all             127.0.0.1/32            ident 
```

   Please the change the above setting to the following:


```properties
host    all             all             127.0.0.1/32            md5 
```

   > **tips**: The above modification makes you match any users in localhost (IP address is `localhost` or `127.0.0.1`) to connect any databases and validate user password via `md5`.

   At the same time, please append a new line at the end of this file:


```properties
host    all             all             0.0.0.0/0               md5 
```

   > **tips**: The above modification makes you match any user in any IPV4 address to connect any databases, and validate user password via `md5`.

   **Fields Explanation:**

   - `host`: The connect way, `host` means connecting via TCP / IP;
   - First `all`: Match all databases;
   - Second `all`: Match all users;
   - `0.0.0.0/0`: Match all IPV4 address;
   - `md5`: Validate via `md5`.
   > **tips**: You can set corresponding match rules according to your cases.

   **ii.** Run `vi postgresql.conf` to open another configuration file and modify the following properties:


```sh
listen_addresses = '*' 
```

   **Field Explanation:**

   - `listen_addresses`: Specify the TCP / IP address listened by server. It is represented by multiple hostnames seperated by comma, for intance, `listen_addresses = host1,host2,host3` or `listen_address = 10.1.1.1,10.1.1.2,10.1.1.3`. The special symbol `*` matches all IP addresses. You can modify the property on demands.
   - `port`: The default value is `5432`. If `5432` is taken, please replace it with an avaliable port.
5. Run `service postgresql-10 start` to launch PostgreSQL
6. Log in to PostgreSQL and create the database

   **i.** Run `su - postgres` to switch to `postgres` user.

   > **Tip:** `postgres` is automatically created by Linux user in the process of PostgreSQL installation.

   **ii.** Run `/usr/pgsql-10/bin/psql` to connect PostgreSQL server.

   The command above will connect to port `5432` by default. If you have changed port number in configuration file `postgresql.conf`, please use `-p` option indicating the port number you set before. For instance, say you set port number as `5433` in `postgresql.conf` file, please run as `/usr/pgsql-10/bin/psql -p 5433`.

   **iii.** Kylin uses `postgres` as user name to connect PostgreSQL by default, you are required to set password for user `postgres`. Run `ALTER USER postgres PASSWORD 'kylin';` to set user password to `kylin`.

   > **Note:** Please do not forget `;` at the end of the command.

   **iv.** Run `create database kylin;` to create the metadata database, named as `kylin` by default.

   > **Note:** Please do not forget `;` at the end of the command.

   **v.** Run `\l` to check if the database was created successfully. If you see picture as below, you have just created a database named `kylin`.

   ![check kylin database](assets/images/installation-create-postgresqldb-25e8cced19c4105e687b040f5a6845b2_4c89a5aa5c995ec8.jpg)

The following example is that Linux user `abc` installs and configures PostgreSQL.

1. Create a new directory `/home/abc/postgresql`, then unzip the PostgreSQL installation package.


```sh
rpm2cpio postgresql10-libs-10.7-1PGDG.rhel6.x86_64.rpm | cpio -idmv 
rpm2cpio postgresql10-10.7-1PGDG.rhel6.x86_64.rpm | cpio -idmv 
rpm2cpio postgresql10-server-10.7-1PGDG.rhel6.x86_64.rpm | cpio -idmv 
```

   >
> [!NOTE]
> : please make sure user `abc` has **read** and **write** privileges.

2. Edit `~/.bash_profile` file, append `export LD_LIBRARY_PATH=/home/abc/postgresql/usr/pgsql-10/lib` at the end of the file, then run `source ~/.bash_profile` to make it take effect.
3. Configure database

   **i.** Run the following command to initialize database:


```sh
~/postgresql/usr/pgsql-10/bin/initdb -A md5 -U postgres -W -D ~/postgresql/var/lib/pgsql/10/data/ 
```

   **Fields explanation:**

   - **-A md5**: validate user password via `md5`
   - **-U postgres**: specify user `postgres`
   - **-W**: set password for user `postgres`
   - **-D ~/postgresql/var/lib/pgsql/10/data/**: specify the path where the configuration file is located

   As the picture shows below, input password after run the command above, the password is the password for user `postgres`, say the password is `kylin`.

   ![initialize postgresql](assets/images/install-initialize-postgresql-09f919be6b06d3b877059f14a9830889_557903782c532d84.png)

   **ii.** Edit configuration file

   **Step 1:** Create the directory for Unix Socket communication via the command below:


```sh
mkdir ~/postgresql/socket 
```

   **Step 2:** Modify the configuration file `~/postgresql/var/lib/pgsql/10/data/postgresql.conf`:


```properties
listen_addresses = '*' 
unix_socket_directories = '/home/abc/postgresql' 
#port = 5432 
```

   >
> [!NOTE]
> : please make sure current user has **read** and **write** privileges on Unit Socket communication directory `/home/abc/postgresql`.

   **Step 3:** Please append the following line at the end of `~/postgresql/var/lib/pgsql/10/data/pg_hba.conf`  configuration file:


```properties
	host    all             all             0.0.0.0/0               md5 
```

4. Run the following command to launch PostgreSQL:


```sh
~/postgresql/usr/pgsql-10/bin/pg_ctl -D ~/postgresql/var/lib/pgsql/10/data/ -l ~/postgresql/var/lib/pgsql/10/pgstartup.log start 
```

5. Run the following command to connect PostgreSQL:


```sh
~/postgresql/usr/pgsql-10/bin/psql -U postgres -h localhost 
```

   The above command will connects to `5432` port. If you modified the setting in configuration, please add `-p` option and set the port. Say you set the port number in `postgresql.conf` to `5436`, please run following command:


```sh
~/postgresql/usr/pgsql-10/bin/psql -U postgres -h localhost -p 5436 
```

   After that, please input password as prompted.
6. Run the following command to create a database named `kylin`:


```sql
create database kylin; 
```

   > **Note:**
   >
   > - Please do not forget to append `;` at the end of the command.
   > - You can check if `kylin` database was created successfully via `\l` command in PostgreSQL client.

Now, we will introduce how to configure PostgreSQL as the metastore DB of Kylin.

1. Set the metadata url in the configuration file `$KYLIN_HOME/conf/kylin.properties`. The property is `kylin.metadata.url = {metadata_name}@jdbc`, please replace `{metadata_name}` with the table name you would like, for instance, `kylin_metadata@jdbc`, the maximum length of `{metadata_name}` allowed is 28. See the example below:


```properties
kylin.metadata.url={metadata_name}@jdbc,driverClassName=org.postgresql.Driver,url=jdbc:postgresql://{host}:{port}/kylin,username={user},password={password} 
```

   The meaning of each configuration item is as follows, `url`, `username` and `password` are required, other fields will use the default value if not set:

   - **url**: JDBC url:
     - **host**: The IP address of PostgreSQL server, the default value is `localhost`;
     - **port**: The port of PostgreSQL server, the default value is `5432`, you can set it with available port number.
     - **kylin**: Metabase name. Make sure this database `kylin` has been created in PostgreSQL;
   - **username**: JDBC user name, the default value is `postgres`;
   - **password**: JDBC password, the default value is void, please set it according to your actual password;
   - **driverClassName**: JDBC driver name, the default value is `org.postgresql.Driver`;

   **vi.** If you need to configure the cluster deployment, please use comma `,` to split among server addresses. Meanwhile, the url should use `"` to quote the url. For example:


```properties
kylin.metadata.url=kylin_metadata@jdbc,driverClassName=org.postgresql.Driver,url="jdbc:postgresql://{ip}:{port},{ip}:{port}.../kylin",username=postgres,password=kylin 
```

2. If you need to encrypt JDBC's password, please follow undermentioned instructions：

   **i.** To obtain encrypted password, please run the command under the path of `${KYLIN_HOME}`


```shell
./bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s <password> 
```

   **ii.** Configure the password in the `kylin.metadata.url` like this


```properties
password=ENC('${encrypted_password}') 
```

   For example, the following assumes that the JDBC password is kylin:

   First, we need to encrypt kylin using the following command


```shell
${KYLIN_HOME}/bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s kylin 
AES encrypted password is:  
YeqVr9MakSFbgxEec9sBwg== 
```

   Then, configure `kylin.metadata.url` like this：


```properties
kylin.metadata.url=kylin_metadata@jdbc,driverClassName=org.postgresql.Driver,url="jdbc:postgresql://{host}:{port},{ip}:{port}.../kylin",username=postgres,password=ENC('YeqVr9MakSFbgxEec9sBwg==') 
```

**Q: How to solve the error `libicu18n.so.42: cannot open shared object file: no such file or directory` when a non-root user initializes PostgreSQL?**

There are two solutions:

Solution 1: Make sure that the node installing PostgreSQL can access the external network, and then enter the command `yum install libicu-devel` in the terminal to download libicui18n.

Solution 2: Visit the website <https://pkgs.org/download/libicu> and download the required packages. Please choose the appropriate version according to the system kernel, such as `libicu-4.2.1-1.el6.x86_64.rpm` for CentOS 6. Then use the command `rpm2cpio libicu-4.2.1-14.el6.x86_64.rpm | cpio -idmv` to decompress the binary package and place the decompressed content in  `$LD_LIBRARY_PATH`. If you don't know `$LD_LIBRARY_PATH`, please refer to the second step of [`Non root` User Installation And Configuration](#deployment-rdbms_metastore-usepg_as_metadb--not_root) above.

---

<a id="deployment-single_node_mode"></a>

<!-- source_url: https://kylin.apache.org/docs/deployment/single_node_mode/ -->

<!-- page_index: 8 -->

# Single Node Mode

Version: 5.0.2

Create a KYLIN\_HOME path and a Linux account for Kylin.

> [!NOTE]
> **Example**
> - The installation location is `/usr/local/`
> - Linux account to run Kylin is `KyAdmin`.

follow the [Prerequisite](#deployment-prerequisite) and finish the environment preparation.

Please download official release binary from [Download Page](https://kylin.apache.org/docs/download) .

If you want to package from source code, please refer to [How To Package](https://kylin.apache.org/docs/development/how_to_package).

Copy and unzip Kylin package to your target server.

> [!NOTE]
> **Example**
> cd /usr/local
> tar -zxvf apache-kylin-[Version].tar.gz

The decompressed directory should be exported as `$KYLIN_HOME` on your server.

> [!NOTE]
> **Example**
> export KYLIN\_HOME=/usr/local/apache-kylin-[Version]/

> [!NOTE]
> **Example**
> bash $KYLIN\_HOME/sbin/download-spark-user.sh

There will be a `spark` directory under `$KYLIN_HOME` .

You can use either MySQL or PostgresQL as a metadata DB.

- [Use PostgreSQL as Metastore](#deployment-rdbms_metastore-usepg_as_metadb).
- [Use MySQL as Metastore](#deployment-rdbms_metastore-use_mysql_as_metadb).

For production environments, we recommend setting up a dedicated metadata DB to ensure reliability.

The default working directory is `/kylin`. Also ensure the Linux account has access to its home directory on HDFS. Meanwhile, create directory `/kylin/spark-history` to store the spark log files.

```sh
hadoop fs -mkdir -p /kylin 
hadoop fs -chown root /kylin 
hadoop fs -mkdir -p /kylin/spark-history 
hadoop fs -chown root /kylin/spark-history 
```

You can modify working directory in `$KYLIN_HOME/conf/kylin.properties`.

> [!NOTE]
> **Example**
> kylin.env.hdfs-working-dir=`hdfs://${nameservice}/kylin`

> [!NOTE]
> If you do not have the permission to create `/kylin/spark-history`, you can configure `kylin.engine.spark-conf.spark.eventLog.dir` and `kylin.engine.spark-conf.spark.history.fs.logDirectory` with an available directory.

In the `conf` directory under the root directory of the installation package, you should configure the parameters in the file `kylin.properties` as follows:

1. According to the PostgreSQL configuration, configure the following metadata parameters. Pay attention to replace the corresponding `{metadata_name}`, `{host}` , `{port}`, `{user}`, `{password}` value, the maximum length of `metadata_name` allowed is 28.


> [!NOTE]
> **Example**
> kylin.metadata.url=`{metadata_name}@jdbc,driverClassName=org.postgresql.Driver,url=jdbc:postgresql://{host}:{port}/kylin,username={user},password={password}`

   For more PostgreSQL configuration, please refer to [Use PostgreSQL as Metastore](#deployment-rdbms_metastore-usepg_as_metadb). For information for MySQL configuration, please refer to [Use MySQL as Metastore](#deployment-rdbms_metastore-use_mysql_as_metadb).


> [!NOTE]
> please name the `{metadata_name}` with characters, numbers, or underscores.
> The name should start with characters.

2. When executing jobs, Kylin will submit the build task to Yarn. You can set and replace `{queue}` in the following parameters as the queue you actually use, and require the build task to be submitted to the specified queue.


> [!NOTE]
> **Example**
> kylin.engine.spark-conf.spark.yarn.queue=`{queue_name}`

3. Configure ZooKeeper.

   Kylin uses ZooKeeper for service discovery, pleaser refer to [Service Discovery](#deployment-cluster_mode--sd) for more details.

   Configure property in `${KYLIN_HOME}\conf\kylin.properties(.override)`.


> [!NOTE]
> **Example**
> kylin.env.zookeeper-connect-string=10.1.2.1:2181,10.1.2.2:2181,10.1.2.3:2181

   If you use ACL for Zookeeper, need setting the follow configuration


| Properties | Description |
| --- | --- |
| kylin.env.zookeeper-acl-enabled | Whether to enable Zookeeper ACL. The default value is disabled. |
| kylin.env.zookeeper.zk-auth | The user password and authentication method used by Zookeeper. The default value is empty. |
| kylin.env.zookeeper.zk-acl | ACL permission setting. The default value is `world:anyone:rwcda`. By default, all users can perform all operations. |

   If you need to encrypt kylin.env.zookeeper.zk-auth , you can do it like this：

   1. run following commands in `${KYLIN_HOME}`, it will print encrypted value
> [!NOTE]
> **Example**
> ./bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s `<value>`

   2. Add the property in `${KYLIN_HOME}\conf\kylin.properties(.override)`


```text
kylin.env.zookeeper.zk-auth=ENC('${encrypted_value}') 
```

4. Configure Gluten
   Apache Gluten is required by internal table feature, it's enabled by default. Add the following config to your `${KYLIN_HOME}\conf\kylin.properties(.override)`


> [!NOTE]
> **Example**
> **gluten for query**
> kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime\_config.storage\_configuration.disks.hdfs.endpoint=hdfs://olivernameservice/
> **gluten for build**
> kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime\_config.storage\_configuration.disks.hdfs.endpoint=hdfs://olivernameservice/

5. Configure Query & Build Cluster on Spark Standalone


```properties
# Query on Stand Alone 
kylin.storage.columnar.spark-conf.spark.master=spark://${SPARK_MASTER_HOST}:7077 
kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.libhdfs3_conf={path for hdfs-site.xml} 
kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.executor.libpath={path for libch.so} 
kylin.storage.columnar.spark-conf.spark.executorEnv.LD_PRELOAD={path for libch.so} 
kylin.storage.columnar.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.reuse_disk_cache=false （worker 不能保证只有一个 app） 
kylin.storage.columnar.spark-conf.spark.gluten.sql.executor.jar.path={path for gluten.jar} 
# Build on Stand Alone 
kylin.engine.spark-conf.spark.master=spark://${SPARK_MASTER_HOST}:7077 
kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.hdfs.libhdfs3_conf={path for hdfs-site.xml} 
kylin.engine.spark-conf.spark.gluten.sql.columnar.executor.libpath={path for libch.so} 
kylin.engine.spark-conf.spark.executorEnv.LD_PRELOAD={path for libch.so} 
kylin.engine.spark-conf.spark.gluten.sql.columnar.backend.ch.runtime_config.reuse_disk_cache=false (worker 不能保证只有一个 app) 
kylin.engine.spark-conf.spark.gluten.sql.driver.jar.path={path for gluten.jar} 
kylin.engine.spark-conf.spark.gluten.sql.executor.jar.path={path for gluten.jar} 
```

6. (optional) Configure Spark Client node information
   Since Spark is started in yarn-client mode, if the IP information of Kylin is not configured in the hosts file of the Hadoop cluster, please add the following configurations in `kylin.properties`:
   `kylin.storage.columnar.spark-conf.spark.driver.host={hostIp}`
   `kylin.engine.spark-conf.spark.driver.host={hostIp}`

You can modify the `{hostIp}` according to the following example:

```properties
kylin.storage.columnar.spark-conf.spark.driver.host=10.1.3.71 
kylin.engine.spark-conf.spark.driver.host=10.1.3.71 
```

---

<a id="deployment-cluster_mode"></a>

<!-- source_url: https://kylin.apache.org/docs/deployment/cluster_mode/ -->

<!-- page_index: 9 -->

# Cluster Mode

Version: 5.0.2

> [!NOTE]
> Please replace the IP address with actual IP address on each server.

---

<a id="deployment-rw_separation"></a>

<!-- source_url: https://kylin.apache.org/docs/deployment/rw_separation/ -->

<!-- page_index: 10 -->

# Read/Write Separation Deployment

Version: 5.0.2

Kylin's tasks based on Hadoop are mainly divided into two types: build and query. If these two tasks use the same set of Hadoop resources, resource preemption may occur between the build and the query, which makes them not stable and fast.

Kylin allows you to finish building and query tasks on different Hadoop clusters. There are many write operations in the former, known as the **Build Cluster**, while the latter is dominated by read-only operations, called **Query Cluster**. The build task will be sent to the build cluster. After the build is completed, the system will send the data into the query cluster so as to executing query tasks.

With a read/write separation deployment, you can completely isolate both build and query workloads, allowing them to run independently, avoiding improper interactions between them and possible performance instability.

Due to the involvement of two Hadoop environments, please read and comply with the following environmental checks.

1. Please confirm the Hadoop versions of build cluster and query cluster are identical, and they're supported version by Kylin.
2. Please confirm that the Hadoop client of build cluster and query cluster is installed and configured on the **Kylin server**. Check commands like `hdfs`、`hive` are all working properly and can access cluster resources.
3. If the two clusters have enabled the HDFS NameNode HA, please check and make sure their HDFS nameservice names are different. If they are the same, please change one of them to avoid conflict.
4. Please check the two clusters can access each other without manually inputting any user credential.

> [!NOTE]
> **Tips**
> As a test, on any build cluster try to copy some HDFS files from/to the query cluster. The copy must succeed without any extra manual interaction.

5. Please make sure the network latency between the two clusters is low enough, as there will be a large number of data moved back and forth during model build process.
6. If Kerberos is enabled, please check the following:

   - The build cluster and the query cluster belong to different realms.
   - The cross-realm trust between the two clusters is configured properly.

You can follow the below instructions to finish Kylin read/write separation deployment based on hadoop clusters.

1. First of all, on **Kylin server**, uncompress Kylin software package to the same location. This location will be referenced as `$KYLIN_HOME` later.
2. Secondly, you should prepare the hadoop conf file of the two clusters. The hadoop configuration of query cluster should be put into `$KYLIN_HOME/hadoop_conf` directory, while that of build query will be put into `$KYLIN_HOME/write_hadoop_conf` directory. What's more, the `hive-site.xml` of the build cluster should be put into the above two directories, make two copies of hive-site.xml and name them hiveserver2-site.xml and hivemetastore-site.xml respectively.

   If Kerberos authentication enabled, you need to copy the krb5.conf file of build cluster to the `$KYLIN_HOME/write_hadoop_conf` directory and copy the krb5.conf file of query cluster to the `$KYLIN_HOME/hadoop_conf` directory.
3. Set the configuration:


```properties
kylin.engine.submit-hadoop-conf-dir=$KYLIN_HOME/write_hadoop_conf 
 
## Working path of Kylin instance on HDFS. Please replace {working_dir} with the real working path, and use the absolute path, such as hdfs://kylin 
kylin.env.hdfs-working-dir={working_dir} 
```

4. If Kerberos is enabled, you will need to do additional configuration:


```properties
kylin.storage.columnar.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://writecluster 
kylin.engine.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://writecluster 
```

5. If the Kerberos authentication mechanism enabled, the following checks need to be done to avoid errors in the segment build job:


```text
java.lang.IllegalArgumentException: Can't get Kerberos realm 
... 
Caused by: KrbException: Cannot locate default realm 
```

   1. Make sure the `keytab` file and `krb5.conf` file required for authentication exist in the directory `$KYLIN_HOME/conf`
   2. If the directory `$KYLIN_HOME/hadoop_conf` exists, make sure there is a `krb5.conf` file in this directory
   3. If the directory `$KYLIN_HOME/write_hadoop_conf` exists, make sure there is a `krb5.conf` file in this directory

Now read/write separation deployment is configured.

> [!NOTE]
> - `$KYLIN_HOME/bin/check-env.sh` and `$KYLIN_HOME/bin/sample.sh` are not available in this deployment mode.
> - In this mode, `kylin.engine.spark-conf.spark.yarn.queue` in `kylin.properties` should be configured as the queue of the build cluster.

---

<a id="configuration-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/intro/ -->

<!-- page_index: 11 -->

# Overview

Version: 5.0.2

After deploying Kylin on your cluster, configure Kylin to enable seamless interaction with Apache Hadoop and Apache Hive. Additionally, optimize Kylin's performance by tailoring its configuration to your specific environment, ensuring a finely-tuned setup that meets your unique needs.
This chapter introduces some configurations for Kylin.

| Component | File | Description |
| --- | --- | --- |
| Kylin | conf/kylin.properties | This is the global configuration file, with all configuration properties about Kylin in it. Details will be discussed in the subsequent chapter [Basic Configuration](#configuration-config). |
| Hadoop | hadoop\_conf/core-site.xml | Global configuration file used by Hadoop, which defines system-level parameters such as HDFS URLs and Hadoop temporary directories, etc. |
| Hadoop | hadoop\_conf/hdfs-site.xml | HDFS configuration file, which defines HDFS parameters such as the storage location of NameNode and DataNode and the number of file copies, etc. |
| Hadoop | hadoop\_conf/yarn-site.xml | Yarn configuration file,which defines Hadoop cluster resource management system parameters, such as ResourceManager, NodeManager communication port and web monitoring port, etc. |
| Hadoop | hadoop\_conf/mapred-site.xml | Map Reduce configuration file used in Hadoop,which defines the default number of reduce tasks, the default upper and lower limits of the memory that the task can use, etc. |
| Hive | hadoop\_conf/hive-site.xml | Hive configuration file, which defines Hive parameters such as hive data storage directory and database address, etc. |

Unless otherwise specified, all references to `kylin.properties` in this manual point to the configuration file listed in the [Kylin Configuration File List](#configuration-intro--kylin-configuration-file-list) section.

---

<a id="configuration-config"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/config/ -->

<!-- page_index: 12 -->

# Basic Configuration

Version: 5.0.2

This chapter provides an in-depth look at frequently used configurations in Kylin. The following sections outline the main topics covered:

The `kylin.properties` file is a crucial configuration file in Kylin, containing key settings that impact the application's behavior. This section provides an in-depth explanation of commonly used properties, enabling you to optimize your Kylin setup.

| Properties | Description |
| --- | --- |
| kylin.circuit-breaker.threshold.model | The maximum number of models allowed to be created in a single project, the default value is `100` |
| kylin.circuit-breaker.threshold.project | The maximum number of projects allowed to be created, the default value is `100` |
| kylin.circuit-breaker.threshold.query-result-row-count | This parameter is the maximum number of rows in the result set returned by the SQL query. The default is `2000000`. If the maximum number of rows is exceeded, the backend will throw an exception |
| kylin.diag.task-timeout | The subtask timeout time for the diagnostic package, whose default value is 3 minutes |
| kylin.diag.task-timeout-black-list | Diagnostic package subtask timeout blacklist (the values are separated by commas). The subtasks in the blacklist will be skipped by the timeout settings and will run until it finished. The default value is `METADATA`, `LOG` The optional value is as below: METADATA, AUDIT\_LOG, CLIENT, JSTACK, CONF, HADOOP\_CONF, BIN, HADOOP\_ENV, CATALOG\_INFO, SYSTEM\_METRICS, MONITOR\_METRICS, SPARK\_LOGS, SPARDER\_HISTORY, KG\_LOGS, LOG, JOB\_TMP, JOB\_EVENTLOGS |
| kylin.diag.obf.level | The desensitization level of the diagnostic package. `RAW` means no desensitization, `OBF` means desensitization. Configuring `OBF` will desensitize sensitive information such as usernames and passwords in the `kylin.properties` file (please refer to the [Diagnosis Kit Tool](#operations-system-operation-cli_tool-diagnosis) chapter), The default value is `OBF`. |
| kylin.engine.sanity-check-enabled | Configure Kylin whether to open Sanity Check during indexes building. The default value is `true` |
| kylin.engine.spark-conf.spark.driver.host | Configure the IP of the node where the Kylin is located |
| kylin.engine.spark-conf.spark.sql.view-truncate-enabled=true | Allow spark view to lose precision during construction, the default value is false |
| kylin.env | The usage of the Kylin instance is specified by this property. Optional values include `DEV`, `PROD` and `QA`, among them `PROD` is the default one. In `DEV` mode some developer functions are enabled. |
| kylin.env.ip-address | When the network address of the node where the Kylin service is located has the ipv6 format, you can specify the ipv4 format through this configuration item. The default is `0.0.0.0` |
| kylin.env.hdfs-working-dir | Working path of Kylin instance on HDFS is specified by this property. The default value is `/kylin` on HDFS, with table name in metadata path as the sub-directory. For example, suppose the metadata path is `kylin_metadata@jdbc`, the HDFS default path should be `/kylin/kylin_metadata`. Please make sure the user running Kylin instance has read/write permissions on that directory. |
| kylin.env.zookeeper-connect-string | This parameter specifies the address of ZooKeeper. There is no default value. **This parameter must be manually configured before starting Kylin instance**, otherwise Kylin will not start. |
| kylin.garbage.storage.cuboid-layout-survival-time-threshold | This property specifies the threshold of invalid files on HDFS. When executing the command line tool to clean up the garbage, invalid files on HDFS that exceed this threshold will be cleaned up. The default value is `7d`, which means 7 days. Invalid files on HDFS include expired indexes, expired snapshots, expired dictionaries, etc. At the same time, indexes with lower cost performance will be cleaned up according to the index optimization strategy. |
| kylin.garbage.storage.executable-survival-time-threshold | This property specifies the threshold for the expired job. The metadata of jobs that have exceeded this threshold and have been completed will be cleaned up. The default is `30d`, which means 30 days. |
| kylin.influxdb.address | This property specifies the address of InfluxDB. The default is `localhost:8086`. |
| kylin.influxdb.password | This property specifiess the password of InfluxDB. The default is `root`. |
| kylin.influxdb.username | This property specifies the username of InfluxDB. The defaul is `root`. |
| kylin.job.finished-notifier-url | When the building job is completed, the job status information will be sent to the url via HTTP request |
| kylin.job.max-concurrent-jobs | Kylin has a default concurrency limit of **20** for jobs in a single project. If there are already too many running jobs reaching the limit, the new submitted job will be added into job queue. Once one running job finishes, jobs in the queue will be scheduled using FIFO mechanism. |
| kylin.job.retry | This property specifies the auto retry times for error jobs. The default value is 0, which means job will not auto retry when it's in error. Set a value greater than 0 to enable this property and it applies on every step within a job and it will be reset if that step is finished. |
| kylin.job.retry-interval | This property specifies the time interval to retry an error job and the default value is `30000` ms. This property is valid only when the job retry property is set to be 1 or above. |
| kylin.metadata.url | Kylin metadata path is specified by this property. The default value is `kylin_metadata` table in PostgreSQL while users can customize it to store metadata into any other table. When deploying multiple Kylin instances on a cluster, it's necessary to specify a unique path for each of them to guarantee the isolation among them. For example, the value of this property for Production instance could be `kylin_metadata_prod`, while that for staging instance could be `kylin_metadata_staging`, so that Production instance wouldn't be interfered by operations on staging instance. |
| kylin.metadata.ops-cron | This parameter specifies the timing task cron expression for timed backup metadata and garbage cleanup. The default value is `0 0 0 * * *`. |
| kylin.metadata.audit-log.max-size | This parameter specifies the maximum number of rows in the audit-log. The default value is `500000`. |
| kylin.metadata.compress.enabled | This parameter specifies whether to compress the contents of metadata and audit log. The default value is `true`. |
| kylin.metrics.influx-rpc-service-bind-address | If the property `# bind-address = "127.0.0.1:8088"` was modified in the influxdb's configuration file, the value of this should be modified at the same time. This parameter will influence whether the diagnostic package can contain system metrics. |
| kylin.query.async-query.max-concurrent-jobs | When configuring the asynchronous query queue, the maximum number of asynchronous query jobs. When the number of jobs reaches the limit, the asynchronous query reports an error. The default value is 0, which means there is no limit to the number of asynchronous query jobs. |
| kylin.query.auto-model-view-enabled | Automatically generate views for model. When the config is on, a view will be generated for each model and user can query on that view. The view will be named with {project\_name}.{model\_name} and contains all the tables defined in the model and all the columns referenced by the dimension and measure of the table. |
| kylin.query.convert-create-table-to-with | Some BI software will send Create Table statement to create a permanent or temporary table in the data source. If this setting is set to `true`, the create table statement in the query will be converted to a with statement, when a later query utilizes the table that the query created in the previous step, the create table statement will be converted into a subquery, which can hit on an index if there is one to serve the query. |
| kylin.query.engine.spark-scheduler-mode | The scheduling strategy of query engine whose default is FAIR (Fair scheduler). The optional value is SJF (Smallest Job First scheduler). Other value is illegal and FAIR strategy will be used as the default strategy. |
| kylin.query.force-limit | Some BI tools always send query like `select * from fact_table`, but the process may stuck if the table size is extremely large. `LIMIT` clause helps in this case, and setting the value of this property to a positive integer make Kylin append `LIMIT` clause if there's no one. For instance the value is `1000`, query `select * from fact_table` will be transformed to `select * from fact_table limit 1000`. This configuration can be overridden at **project** level. |
| kylin.query.init-sparder-async | The default value is `true`，which means that sparder will start asynchronously. Therefore, the Kylin web service and the query spark service will start separately; If set to `false`, the Kylin web service will be only available after the sparder service has been started. |
| kylin.query.layout.prefer-aggindex | The default value is `true`, which means that when index comparison selections are made for aggregate indexes and detail indexes, aggregate indexes are preferred. |
| kylin.query.match-partial-inner-join-model | The default value is `false`, which means that the multi-table inner join model does not support the SQL which matches the inner join part partially. For example: Assume there are three tables A, B, and C . By default, the SQL `A inner join B` can only be answered by the model of A inner join B or the model of A inner join B left join C. The model of A inner join B inner join C cannot answer it. If this parameter is set to `true`, the SQL of A inner join B can be answered with the model of A inner join B or A inner join B left join C, or it can also be answered with the model of A inner join B inner join C. |
| kylin.query.match-partial-non-equi-join-model | default to `false` ，currently if the model contains non-equi joins, the query can be matched with the model only if it contains all the non-equi joins defined in the model. If the config is set to `true`, the query is allowed to contain only part of the non-equi joins. e.g. model: A left join B non-equi left join C. When the config is set to `false`, only query with the complete join relations of the model can be matched with the model. When the config is set to `true`, query like A left join B can also be matched with the model. |
| kylin.query.max-result-rows | This property specifies the maximum number of rows that a query can return. This property applies on all ways of executing queries, including Web UI, Asynchronous Query, JDBC Driver and ODBC Driver. This configuration can be overridden at **project** level. For this property to take effect, it needs to be a positive integer less than or equal to 2147483647. The default value is 0, meaning no limit on the result. Below is the priority: SQL limit > min(前端 limit, kylin.query.max-result-rows) > kylin.query.force-limit |
| kylin.query.memory-limit-during-collect-mb | Limit the memory usage when getting query result in Kylin，the unit is megabytes, defaults to 5400mb |
| kylin.query.queryhistory.max-size | The total number of records in the query history of all projects, the default is 10000000 |
| kylin.query.queryhistory.project-max-size | The number of records in the query history retained of a single project, the default is 1000000 |
| kylin.query.queryhistory.survival-time-threshold | The number of records in the query history retention time of all items, the default is 30d, which means 30 days, and other units are also supported: millisecond ms, microsecond us, minute m or min, hour h |
| kylin.query.realization.chooser.thread-core-num | The number of core threads of the model matching thread pool in the query engine, the default is 5. It should be noted that when the number of core threads is set to less than 0, this thread pool will be unavailable, which will cause the entire query engine to be unavailable |
| kylin.query.realization.chooser.thread-max-num | The maximum number of threads in the model matching thread pool in the query engine, the default is 50. It should be noted that when the maximum number of threads is set to be less than or equal to 0 or less than the number of core threads, this thread pool will be unavailable, which will cause the entire query engine to be unavailable |
| kylin.query.replace-count-column-with-count-star | The default value is `false` , which means that COUNT(column) measure will hit a model only after it has been set up in the model. If COUNT(column) measure is called in SQL while not having been set up in the model, this parameter value can be set to `true`, then the system will use COUNT(constant) measure to replace COUNT(column) measure approximately. COUNT(constant) measure takes all Null value into calculation. |
| kylin.query.replace-dynamic-params-enabled | Whether to enable dynamic parameter binding for JDBC query, the default value is false, which means it is not enabled. |
| kylin.query.spark-job-trace-enabled | Enable the job tracking log of spark. Record additional information about spark: Submission waiting time, execution waiting time, execution time and result acquisition time are displayed in the timeline of history. |
| kylin.query.spark-job-trace-timeout-ms | Only for the job tracking log of spark. The longest waiting time of query history. If it exceeds, the job tracking log of spark will not be recorded. |
| kylin.query.spark-job-trace-cache-max | Only for the job tracking log of spark. The maximum number of job tracking log caches in spark. The elimination strategy is LRU，TTL is kylin.query.spark-job-trace-timeout-ms + 20000 ms. |
| kylin.query.spark-job-trace-parallel-max | Only for the job tracking log of spark. Spark's job tracks the concurrency of log processing, "Additional information about spark" will be lost if the concurrency exceeds this limit. |
| kylin.query.timeout-seconds | Query timeout, in seconds. The default value is `300` seconds. If the query execution time exceeds 300 seconds, an error will be returned: `Query timeout after: 300s`. The minimum value is `30` seconds, and the configured value less than `30` seconds also takes effect according to `30` seconds. |
| kylin.query.use-tableindex-answer-non-raw-query | The default value is `false`, which means that the aggregate query can only be answered with the aggregate index. If the parameter is set to `true`, the system allows the corresponding table index to be used to answer the aggregate query. |
| kylin.scheduler.schedule-job-timeout-minute | Job execution timeout period. The default is `0` minute. This property is valid only when the it is set to be 1 or above. When the job execution exceeds the timeout period, it will change to the Error status. |
| kylin.security.user-password-encoder | Encryption algorithm of user password. The default is the BCrypt algorithm. If you want to use the Pbkdf2 algorithm, configure the value to org.springframework.security.crypto. password.Pbkdf2PasswordEncoder. Note: Please do not change this configuration item arbitrarily, otherwise the user may not be able to log in |
| kylin.server.cors.allow-all | allow all corss origin requests(CORS). `true` for allowing any CORS request, `false` for refusing all CORS requests. Default to `false`. |
| kylin.server.cors.allowed-origin | Specify a whitelist that allows cross-domain, default all domain names (\*), use commas (,) to separate multiple domain names. This parameter is valid when `kylin.server.cors.allow-all`=true |
| kylin.server.mode | There are three modes in Kylin, `all` , `query` and `job`, and you can change it by modifying the property. The default value is `all`. For `query` mode, it can only serves queries. For`job` mode, it can run building jobs and execute metadata operations and cannot serve queries. `all` mode can handle both of them. |
| kylin.source.hive.databases | Configure the database list loaded by the data source. There is no default value. Both the system level and the project level can be configured. The priority of the project level is greater than the system level. |
| kylin.storage.columnar.spark-conf.spark.sql.view-truncate-enabled | Allow spark view to lose precision when loading tables and queries, the default value is false |
| kylin.storage.columnar.spark-conf.spark.yarn.queue | This property specifies the yarn queue which is used by spark query cluster. |
| kylin.storage.columnar.spark-conf.spark.master | Spark deployment is normally divided into **Spark on YARN**, **Spark on Mesos**, and **standalone**. We usually use Spark on YARN as default. This property enables Kylin to use standalone deployment, which could submit jobs to the specific spark-master-url. |
| kylin.storage.columnar.spark-conf.spark.driver.host | Configure the IP of the node where the Kylin is located |
| kylin.storage.columnar.spark-conf.spark.sql.cartesianPartitionNumThreshold | Threshold for Cartesian Partition number in Spark Execution Plan. Query will be terminated if Cartesian Partition number reaches or exceeds the threshold. If this value is set to empty or negative, the threshold will be set to spark.executor.cores \* spark.executor.instances \* 100. |
| kylin.storage.quota-in-giga-bytes | This property specifies the storage quota for each project. The default is `10240`, in gigabytes. |
| kylin.web.timezone | Time zone used for Kylin Rest service is specified by this property. The default value is the time zone of the local machine's system. You can change it according to the requirement of your application. For more details, please refer to <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones> with the `TZ database name` column. |
| kylin.web.export-allow-admin | Whether to allow Admin user to export query results to a CSV file, the default is true. |
| kylin.web.export-allow-other | Whether to allow non-Admin user to export query results to a CSV file, the default is true. |
| kylin.web.stack-trace.enabled | The error prompts whether the popup window displays details. The default value is false. Introduced in: 4.1.1 |
| kylin.web.session.secure-random-create-enabled | The default is false. Use UUID to generate sessionId, and use JDK's SecureRandom random number to enable sessionId after MD5 encryption, please use the upgrade session table tool to upgrade the session table first otherwise the user will report an error when logging in. |
| kylin.web.session.jdbc-encode-enabled | The default is false, sessionId is saved directly into the database without encryption, and sessionId will be encrypted and saved to the database after opening. Note: If the encryption function is configured, Please use the upgrade session table tool to upgrade the session table first, otherwise the user will report an error when logging in. |
| server.port | This parameter specifies the port used by the Kylin service. The default is `7070`. |
| server.address | This parameter specifies the address used by the Kylin service. The default is `0.0.0.0`. |

To override default configurations, create a `kylin.properties.override` file in the `$KYLIN_HOME/conf` directory. This file allows you to customize settings at runtime.

**Best Practice:** During system upgrades, retain the `kylin.properties.override` file with the new `kylin.properties` version to ensure a seamless transition.

**Important Note:** Parameters defined in `kylin.properties` or `kylin.properties.override` are global and loaded by default when Kylin starts. After modifying these files, restart Kylin for the changes to take effect.

In the `$KYLIN_HOME/conf/setenv.sh.template` file, you'll find a sample setting for the `KYLIN_JVM_SETTINGS` environment variable. This default setting uses relatively little memory, but you can adjust it according to your own environment. The default JVM configuration is as follows:

```properties
export KYLIN_JVM_SETTINGS="-server -Xms1g -Xmx8g -XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:G1HeapRegionSize=16m -XX:+PrintFlagsFinal -XX:+PrintReferenceGC -verbose:gc -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintGCDateStamps -XX:+PrintAdaptiveSizePolicy -XX:+UnlockDiagnosticVMOptions -XX:+G1SummarizeConcMark  -Xloggc:$KYLIN_HOME/logs/kylin.gc.$$  -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=10 -XX:GCLogFileSize=64M -XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=${KYLIN_HOME}/logs" 
```

If you want to modify this configuration, you need to create a copy of the template file, name it `setenv.sh`, and place it in the `$KYLIN_HOME/conf/` directory. You can then modify the configuration in the new file as needed.

The parameter `-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=${KYLIN_HOME}/logs` generates logs when an `OutOfMemory` error occurs. The default log file path is `${KYLIN_HOME}/logs`, but you can modify it if required.

```bash
export JAVA_VM_XMS=1g        #The initial memory of the JVM when kylin starts. 
export JAVA_VM_XMX=8g        #The maximum memory of the JVM when kylin starts. 
export JAVA_VM_TOOL_XMS=1g   #The initial memory of the JVM when the tool class is started. 
export JAVA_VM_TOOL_XMX=8g   #The maximum memory of the JVM when the tool class is started. 
```

The `JAVA_VM_TOOL_XMS` and `JAVA_VM_TOOL_XMX` environment variables control the initial and maximum memory of the JVM when running tool classes. If these variables are not set, they will default to the values of `JAVA_VM_XMS` and `JAVA_VM_XMX`, respectively.

Please note that some special tool classes, such as `guardian.sh`, `check-2100-hive-acl.sh`, and `get-properties.sh`, are not affected by these configurations. To take advantage of these new configurations, you need to manually set the `JAVA_VM_TOOL_XMS` and `JAVA_VM_TOOL_XMX` variables when upgrading from an older version.

Kylin relies heavily on Apache Spark for both query and job building. To customize Spark configurations, use the following prefixes:

- `kylin.storage.columnar.spark-conf` for queries
- `kylin.engine.spark-conf` for builds

These prefixes can be used to customize various Spark settings, such as memory allocation, execution parameters, and more. For a detailed explanation of Spark configuration, please refer to the official documentation: [Spark Configuration](https://spark.apache.org/docs/latest/configuration.html).

**1. Query-Related Configurations**

```shell
kylin.storage.columnar.spark-conf.executor.instances 
kylin.storage.columnar.spark-conf.executor.cores 
kylin.storage.columnar.spark-conf.executor.memory 
kylin.storage.columnar.spark-conf.executor.memoryOverhead 
kylin.storage.columnar.spark-conf.sql.shuffle.partitions 
kylin.storage.columnar.spark-conf.driver.memory 
kylin.storage.columnar.spark-conf.driver.memoryOverhead 
kylin.storage.columnar.spark-conf.driver.cores 
```

**2. Job Building-Related Configurations**

```shell
kylin.engine.spark-conf.spark.executor.instances 
kylin.engine.spark-conf.spark.executor.cores 
kylin.engine.spark-conf.spark.executor.memory 
kylin.engine.spark-conf.spark.executor.memoryOverhead 
kylin.engine.spark-conf.spark.sql.shuffle.partitions 
kylin.engine.spark-conf.spark.driver.memory 
kylin.engine.spark-conf.spark.driver.memoryOverhead 
kylin.engine.spark-conf.spark.driver.cores 
```

**3. Switching to Minimal Configurations**

Under **$KYLIN\_HOME/conf/**, there are two sets of configurations ready for use: `production` and `minimal`. The former is the default configuration, recommended for production environments. The latter uses minimal resources, suitable for sandbox or single-node environments with limited resources. To switch to `minimal` configurations, please uncomment the following configuration items in `$KYLIN_HOME/conf/kylin.properties` and restart Kylin to take effect:

```shell
# Kylin provides two configuration profiles: minimal and production(by default).
# To switch to minimal: uncomment the properties #kylin.storage.columnar.spark-conf.spark.driver.memory=512m #kylin.storage.columnar.spark-conf.spark.executor.memory=512m #kylin.storage.columnar.spark-conf.spark.executor.memoryOverhead=512m #kylin.storage.columnar.spark-conf.spark.executor.extraJavaOptions=-Dhdp.version=current -Dlog4j.configurationFile=spark-executor-log4j.xml -Dlog4j.debug -Dkylin.hdfs.working.dir=${kylin.env.hdfs-working-dir} -Dkap.metadata.identifier=${kylin.metadata.url.identifier} -Dkap.spark.category=sparder -Dkap.spark.project=${job.project} -XX:MaxDirectMemorySize=512M #kylin.storage.columnar.spark-conf.spark.yarn.am.memory=512m #kylin.storage.columnar.spark-conf.spark.executor.cores=1 #kylin.storage.columnar.spark-conf.spark.executor.instances=1 #kylin.storage.columnar.spark-conf.spark.sql.adaptive.coalescePartitions.minPartitionNum=1
```

Sparder Canary is a health monitoring component for the Sparder application, which is the Spark engine used for querying in Kylin. It periodically checks the status of the running Sparder instance and automatically initiates the creation of a new instance if any abnormalities are detected, such as unexpected termination or loss of responsiveness. This ensures that the Sparder application remains in a healthy and functional state at all times.

| Properties | Description |
| --- | --- |
| kylin.canary.sqlcontext-enabled | Whether to enable the Sparder Canary function, the default is `false` |
| kylin.canary.sqlcontext-threshold-to-restart-spark | When the number of abnormal detection times exceeds this threshold, restart spark context |
| kylin.canary.sqlcontext-period-min | Check interval, default is `3` minutes |
| kylin.canary.sqlcontext-error-response-ms | Single detection timeout time, the default is `3` minutes, if single detection timeout means no response from spark context |
| kylin.canary.sqlcontext-type | The detection method, the default is `file`, this method confirms whether the spark context is still running normally by writing a parquet file to the directory configured by `kylin.env.hdfs-working-dir` . It can also be configured as `count` to confirm whether the spark context is running normally by performing an accumulation operation |

---

<a id="configuration-gluten_config"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/gluten_config/ -->

<!-- page_index: 13 -->

# Gluten Configuration

Version: 5.0.2

> [!IMPORTANT]
> In Kylin both query and build use Apache Spark as compute engine, but they use different configurations.
> For query engine, you should add the prefix `kylin.storage.columnar.spark-conf`.
> For build engine, add prefix `kylin.engine.spark-conf`.

---

<a id="configuration-hadoop_queue_config"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/hadoop_queue_config/ -->

<!-- page_index: 14 -->

# Hadoop Queue

Version: 5.0.2

In a multi-tenant environment, sharing a large cluster securely requires each tenant to have allocated resources in a timely manner, within the constraints of their allocated capacities. To achieve this, each Kylin instance or project can be configured to utilize a separate YARN queue, enabling efficient computing resource allocation and separation.

To achieve this, first create a new YARN capacity scheduler queue. By default, the job sent out by Kylin will go to the default YARN queue.

In the screenshot below, a new YARN queue `learn_kylin` has been set up.

![](assets/images/1-28c9d8bfe8f50475011fa16f4f7c00fb_db73b460ec923527.png)

To configure the YARN queue used in Kylin, modify the `kylin.properties` file by replacing `YOUR_QUEUE_NAME` with the name of your YARN queue. This setting applies to both building and querying operations.

```shell
### Building configuration 
kylin.engine.spark-conf.spark.yarn.queue=YOUR_QUEUE_NAME 
 
### Querying configuration 
kylin.storage.columnar.spark-conf.spark.yarn.queue=YOUR_QUEUE_NAME 
```

![](assets/images/2-69a5a2598d009ed029eadc43f6633f4b_43d8b10ecf6e4195.png)

In this example, the queue for querying has been changed to `learn_kylin` (as shown above). You can test this change by triggering a querying job.

Now, go to YARN Resource Manager on the cluster. You will see this job has been submitted under queue `learn_kylin`.

![](assets/images/3-6115abf84ad32f70409a18db427e4689_53d0dab448f17397.png)

Similarly, you may set up YARN queue for other Kylin instances to achieve computing resource separation.

The system admin user can set the YARN Application Queue of the project in **Setting -> Advanced Settings -> YARN Application Queue**, please refer to the [Project Settings](#operations-project-managing-project_settings) for more information.

---

<a id="configuration-https"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/https/ -->

<!-- page_index: 15 -->

# HTTPS Connection

Version: 5.0.2

Kylin 5.0 offers a secure HTTPS connection, which is disabled by default. To enable it, follow the step-by-step instructions outlined below.

Kylin ships a HTTPS certificate. If you want to enable this function with the default certificate, you just need to add or modify the following properties in `$KYLIN_HOME/conf/kylin.properties`.

```properties
# enable HTTPS connection 
kylin.server.https.enable=true 
# port number 
kylin.server.https.port=7443 
```

The default port is `7443`, please check the port has not been taken by other processes. You can run the command below to check. If the port is in use, please use an available port number.

```text
netstat -tlpn | grep 7443 
```

After modifying the above properties, please restart Kylin for the changes to take effect. Assuming you set the https port to 7443, the access url would be `https://localhost:7443/kylin/index.html`.

**Note:** Because the certificate is generated automatically, you may see a browser notice about certificate installation when you access the url. Please ignore it.

Kylin also supports third-party certificates, you just need to provide the certificate file and make the following changes in the `$KYLIN_HOME/conf/kylin.properties` file:

```properties
# enable HTTPS connection 
kylin.server.https.enable=true 
# port number 
kylin.server.https.port=7443 
# format of keystore, Tomcat 8 supports JKS, PKCS11 or PKCS12 format 
kylin.server.https.keystore-type=JKS 
# location of your certificate file 
kylin.server.https.keystore-file=${KYLIN_HOME}/server/.keystore 
# password 
kylin.server.https.keystore-password=changeit 
# alias name for keystore entry, which is optional. Please skip it if you don't need. 
kylin.server.https.key-alias=tomcat 
```

If you need to encrypt `kylin.server.https.keystore-password`, you can do it like this：

i.run following commands in `${KYLIN_HOME}`, it will print encrypted password

```shell
./bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s <password> 
```

ii.config `kylin.server.https.keystore-password` like this

```properties
kylin.server.https.keystore-password=ENC('${encrypted_password}') 
```

After modifying the properties above, please restart Kylin for the changes to take effect. Assuming you set the https port to 7443, the access url would be `https://localhost:7443/kylin/index.html`.

>
> [!NOTE]
> : If you are not using the default SSL certificate and put your certificate under `$KYLIN_HOME`. Please backup your certificate before upgrading your instance, and specify the file path in the new Kylin configuration file. We recommend putting the certificate under an independent path.

---

<a id="configuration-log_rotate"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/log_rotate/ -->

<!-- page_index: 16 -->

# Log Rotate

Version: 5.0.2

Kylin's log rotation is configured to manage the three log files: `shell.stderr`, `shell.stdout`, and `kylin.out` located in the `$KYLIN_HOME/logs/` directory.
**Any changes to the configurations below require a restart to take effect.**

| Property | Description | Default Value | Options |
| --- | --- | --- | --- |
| `kylin.env.max-keep-log-file-number` | Maximum number of log files to keep | 10 |  |
| `kylin.env.max-keep-log-file-threshold-mb` | Log file rotation threshold (in MB) | 256 |  |
| `kylin.env.log-rotate-check-cron` | Crontab time configuration for log rotation | `33 * * * *` |  |
| `kylin.env.log-rotate-enabled` | Enable log rotation using crontab | `true` | `false` |

To use the default log rotation strategy:

1. Set `kylin.env.log-rotate-enabled` to `true` (default).
2. Ensure users running Kylin can use the `logrotate` and `crontab` commands to add a scheduled task.

Kylin will:

- Add or update crontab tasks according to `kylin.env.log-rotate-check-cron` on startup or restart.
- Remove added crontab tasks on exit.

- If the default log rotation policy conditions are not met, Kylin will only perform log rolling checks at startup. This means that log files will be rotated based on the `kylin.env.max-keep-log-file-number` and `kylin.env.max-keep-log-file-threshold-mb` parameters every time the `kylin.sh start` command is executed. Note that prolonged Kylin runtime may result in excessively large log files.
- Using `crontab` to control log rotation may result in log loss during rotation if the log file is too large.

---

<a id="configuration-query_cache"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/query_cache/ -->

<!-- page_index: 17 -->

# Query Cache

Version: 5.0.2

> [!WARNING]
> **Caution**
> Redis passwords can be encrypted, please refer to: [Use MySQL as Metastore](#deployment-rdbms_metastore-use_mysql_as_metadb)

---

<a id="configuration-spark_dynamic_allocation"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/spark_dynamic_allocation/ -->

<!-- page_index: 18 -->

# Spark Dynamic Allocation

Version: 5.0.2

In Spark, the fundamental resource unit is the executor, which is similar to containers in YARN. When running Spark on YARN, you can specify the number of executors using the `num-executors` parameter. Additionally, `executor-memory` and `executor-cores` parameters limit the memory and virtual CPU cores allocated to each executor.

Consider a Kylin instance as an example. When using a fixed resource allocation strategy with `num-executor` set to 3, each Kylin instance will occupy 4 YARN containers (1 for the application master and 3 for executors) until the user logs out. In contrast, Dynamic Resource Allocation enables Spark to dynamically adjust the number of executors based on the Kylin query engine workload, resulting in significant resource savings.

For more information on Spark Dynamic Allocation, please refer to the official Spark documentation: <http://spark.apache.org/docs/2.4.1/job-scheduling.html#dynamic-resource-allocation>

Configuring Spark Dynamic Allocation involves two key components:

1. **Resource Management**: This varies depending on the cluster's resource manager, which can be YARN, Mesos, or Standalone.
2. **spark-defaults.conf**: This configuration file is environment-agnostic and applies universally.

1. For CDH

   Log into Cloudera Manager, choose YARN configuration and find NodeManager Advanced Configuration Snippet(Safety Valve) for `yarn-site.xml`, config as following：


```text
<property> 
 <name>yarn.nodemanager.aux-services</name> 
 <value>mapreduce_shuffle,spark_shuffle</value> 
</property> 
<property> 
 <name>yarn.nodemanager.aux-services.spark_shuffle.class</name> 
 <value>org.apache.spark.network.yarn.YarnShuffleService</value> 
</property> 
```

   Copy the `$KYLIN_HOME/spark/yarn/spark-<version>-yarn-shuffle.jar` and put it under path `/opt/lib/kylin/` of Hadoop node. Find NodeManager Environment Advanced Configuration Snippet (Safety Valve) in Cloudera Manager, Config:


```shell
YARN_USER_CLASSPATH=/opt/lib/kylin/* 
```

   Then `yarn-shuffle.jar` will be added into the Node Manager's startup classpath. To apply the changes, save the configuration, restart the Node Manager, and then deploy the client configuration in Cloudera Manager. Finally, restart all services to ensure the updates take effect.
2. For HDP

   Log into Ambari management page, navigate to **Yarn -> Configs -> Advanced**, use the filter to find the following configurations and update them as needed:


```shell
yarn.nodemanager.aux-services.spark_shuffle.class=org.apache.spark.network.yarn.YarnShuffleService 
```

   To apply the changes, save the configuration, and restart all services to ensure the updates take effect.

To enable the Spark Dynamic Allocation, we will need to add some configuration items in Spark config files. Since we can override spark configuraion in kylin.properties, we will add following configuration items in it:

```shell
kylin.storage.columnar.spark-conf.spark.dynamicAllocation.enabled=true 
kylin.storage.columnar.spark-conf.spark.dynamicAllocation.maxExecutors=5 
kylin.storage.columnar.spark-conf.spark.dynamicAllocation.minExecutors=1 
kylin.storage.columnar.spark-conf.spark.shuffle.service.enabled=true 
kylin.storage.columnar.spark-conf.spark.dynamicAllocation.initialExecutors=3 
```

More configurations please refer to:
<http://spark.apache.org/docs/latest/configuration.html#dynamic-allocation>

After completing the configurations, start the Kylin service and navigate to the Spark Executor page to monitor the current executor numbers. Observe how the executor count adjusts dynamically based on the defined settings.

![](assets/images/spark-executor-original-66b7a7f7047f2240fd0e66d87062f3c6_cf2198a42218afd7.jpg)

The executors will keep idle, so they will be reduced after a while until reaching the minimum number in configuration item.

![](assets/images/spark-executor-min-4c8c2fcdeadd80073a3659eaf882807f_792acfb703219b0e.jpg)

Submit multi-thread queries to Kylin via Restful API. The executors will be increase but never exceed the maximum number in configuration item.

![](assets/images/spark-executor-max-96b44912eecd37cd8886b3e70cfd9450_55262b3f0b2bfca8.jpg)

---

<a id="configuration-spark_rpc_encryption"></a>

<!-- source_url: https://kylin.apache.org/docs/configuration/spark_rpc_encryption/ -->

<!-- page_index: 19 -->

# Spark RPC Encryption

Version: 5.0.2

Kylin supports enabling communication encryption between Spark nodes, which enhances the security of internal communication and prevents specific security attacks. This feature is disabled by default. To enable it, follow the steps below:

Ensure that RPC communication encryption is enabled in the Spark cluster by referring to the [Spark Security documentation](https://spark.apache.org/docs/latest/security.html#authentication).

Add the following configurations in the `$KYLIN_HOME/conf/kylin.properties` file to enable Kylin nodes and Spark cluster communication encryption:

```properties
### spark rpc encryption for build jobs 
kylin.storage.columnar.spark-conf.spark.authenticate=true 
kylin.storage.columnar.spark-conf.spark.authenticate.secret=kylin 
kylin.storage.columnar.spark-conf.spark.network.crypto.enabled=true 
kylin.storage.columnar.spark-conf.spark.network.crypto.keyLength=256 
kylin.storage.columnar.spark-conf.spark.network.crypto.keyFactoryAlgorithm=PBKDF2WithHmacSHA256 
 
### spark rpc encryption for query jobs 
kylin.engine.spark-conf.spark.authenticate=true 
kylin.engine.spark-conf.spark.authenticate.secret=kylin 
kylin.engine.spark-conf.spark.network.crypto.enabled=true 
kylin.engine.spark-conf.spark.network.crypto.keyLength=256 
kylin.engine.spark-conf.spark.network.crypto.keyFactoryAlgorithm=PBKDF2WithHmacSHA256 
```

After completing the configuration, restart Kylin and verify that both query and build tasks are executed successfully.

---

<a id="datasource-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/datasource/intro/ -->

<!-- page_index: 20 -->

# Load data source

Version: 5.0.2

The Kylin supports the integration of multiple data sources, such as Hive. You can connect different data sources to the platform and expose a unified query interface using Kylin, which shields the technical details of different data sources. It also creates a uniform business semantic layer that frees users from concerns about the technical complexity and implementation of the underlying data source.

Click the links below to learn how to load different types of data sources.

- [Use Hive as Data Source](#datasource-import_hive)
- [Data Sampling](#datasource-data_sampling)

---

<a id="datasource-import_hive"></a>

<!-- source_url: https://kylin.apache.org/docs/datasource/import_hive/ -->

<!-- page_index: 21 -->

# Use Hive as Data Source

Version: 5.0.2

In the context of digital transformation, companies need to dig out the most valuable data to support their business decisions and growth, which is really hard to achieve with traditional data warehouses, as they can only provide minute-level or even hour-level query latency when dealing with massive data.

Leveraging the capability of Apache Hive, Kylin has effectively solved the query latency issue with its sub-second query response time on PB-level data.

Apache Hive is a distributed, fault-tolerant data warehouse software that enables analytics at a massive scale. With Apache Hive to map structured data into tables and precomputation offered by Kylin, you can easily identify and manage your business' most valuable data, and uncover new insights from any size dataset, at any time, and from anywhere.

This article introduces how to load Hive data source to a Kylin [project](#operations-project-managing-project_management) for [model designing](#model-intro) and [data analysis](#query-insight).

- Hive data types including Map, Array, Struct, and Binary are not supported. Columns of these data types will be skipped during data loading.
- Views with user-defined functions (UDF) in Hive 3 are not supported.

1. Log in to Kylin as any of the following roles:

   - System admin
   - Management of the target project or Admin
2. In the project list at the top of the page, select the target project.

   Create a new project if you have not created any projects yet. For more information, see [Create project](#operations-project-managing-project_management).
3. In the left navigation panel, click **Data Assets** > **Data Source**.
4. Click **Add data source**. In the **Add New Source** dialog box, select **Hive** and click **Next**.

   ![](assets/images/hive-datasource-09f6f02d8840444645208aea161c104a_6836c612c6cc7f39.png)
5. Select the target database/table (use the filter to quickly locate), and then click **Load**.
6. Below we will use Kylin's [sample dataset](#quickstart-tutorial) to show how to load Hive data source.

   ![](assets/images/select-dataset-1d2579cff10f777f3fb0783a82241929_2bc1207c78a3c591.png)

   > [!NOTE]
   >
   > [Data sampling](#datasource-data_sampling) is enabled at the table level by default. Kylin uses table sampling to collect statistical information of source tables, such as column cardinality and formats, so you can check the distribution for column values for better model designing.

- Question: Why cannot I find the Hive database/table prepared in advance during data loading?

  Answer: Kylin will obtain the source table metadata periodically. If a table cannot be found during data loading, it's likely that the source table metadata is changed. To solve this issue, click **Refresh now** so the system can get the latest metadata information.
- Question: How to load Hive transactional tables?

  Answer: Before loading, you need to add `kylin.build.resource.read-transactional-table-enabled=true` to the configuration file, and configure parameter `kylin.source.hive.beeline-params`. For more information, see [Configure basic parameters](#configuration-config).
- Question: Besides Hive data source, what other data sources does Kylin support?

  Answer: Kylin current only supports Hive.

[Model](#model-intro)

---

<a id="datasource-data_sampling"></a>

<!-- source_url: https://kylin.apache.org/docs/datasource/data_sampling/ -->

<!-- page_index: 22 -->

# Data Sampling

Version: 5.0.2

Kylin provides the data sampling function to facilitate table data analysis. With data sampling, you can collect table characteristics, such as cardinality, max value, and min value for each column, to improve [model designing](#model-intro).

Kylin supports data sampling during data loading. If you want to manually sample data, follow the steps below:

1. Log in to Kylin as any of the following roles:

   - System admin
   - Management of the target project or Admin
2. In the project list at the top of the page, select the target project.

   Create a project if you have not created any projects yet. For more information, see [Create project](#operations-project-managing-project_management).
3. In the left navigation panel, click **Data Assets** > **Data Source**.
4. In the **Data Source** section, select the target table, and click ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAHwSURBVHgB1VVBUuMwEJxRzHnzBO8PyAsW/2BrN3t3dh8QU8megSNFIOEFEWcC5R+Q/MA/QE/wnURDy8SO5XIKOOTAVLksS63WzPSMTHQg43LwM066AXWO20BrCkyqL019zuGP6CgUst2Fvl7uJf4zGD0LcUjtlq9l/T3Vs7zA/hsNxdI5tnffSMSI8O1CT2blBlUOClKxp46g/pBIhOUqml/x/1gsz0TUnVtn4Z4VWoF92o/HSckX+O538lTfmEbIAO1gHbZnINIPepLUYPHveETMfIbxzPP4I4ZDQhcZ8nfXspy6yBzm08SwIsdw7dt7mE8Rb8Vb4kmaawo5xisrBfZybJX9AXH8DSTd+jfEOhW2T66KSFSRT2GJBTiIGZW4ilhEbpl4yAA1vUHJZGvaZG54r68y5LEHQec4BcSSgzljUlGqrw19Was6r/93PEXISTtIzItsek6Y/mD8hKmTPXzLxXwS+cSDMdIsWkit6shCPKc4OhB5NgEHEE0uLCnjH26P0SDDbeubwCdRK4ij63Ou4CHUtOnZo75a1if68egEr+GO60D29Yi9HIvaVJfIDtAJm5vQDGETJ7iAeA9xBuZpwKoplNuWu4rAIC8udaZ54Pu0PVCMqwiP2PX5/l/Tprpc4GnUFoWzl23bH9ReAflH5KVEjSXiAAAAAElFTkSuQmCC) in the right corner of the page.

   ![](assets/images/target-table-8ee21166f1d46043c180a8ed10f193e7_411b69c0c5c808cd.png)
5. In the pop-up dialog box, enter the number of rows for sampling (from 10,000 to 20,000,000) and click **Submit**.

   The accuracy of sampled results will depend on the number of rows that are sampled, but more rows will also request more resources and time. You can set the row number based on the actual requirements. To check the progress of the sampling job, click **Monitor** > **Batch Job** in the left navigation panel.
6. (Optional) View sampled results.

   - Click the **Columns** tab to view statistical information, such as the number of sampled rows (estimated value), and the cardinality, min value and max value for each sampled column.

     ![](assets/images/ssb-column-183c04e50b8e076b0233d8d890281a18_85255cf3c645e4e0.png)
   - Click the **Sample Data** tab to view the detailed information of the first 10 records.

     ![](assets/images/sample-data-ecdef866beca16a094a19b7b132f74d4_65809a196bf80724.png)

Question: Why are the Chinese comments garbled in the sampled results?

Answer: This issue is often caused by improper encoding settings. Please confirm whether any Chinese comments in the source Hive table are garbled via the Hive client. If yes, please modify the encoding in MySQL metabase. Below we use [Apache Hadoop](#deployment-intro) platform as an example to show how to modify encoding:

1. Log in to the server.
2. Run the `mysql -uroot -p` command and enter your password.
3. Run the `use metastore;` command to enter the Metastore database.
4. Modify the encoding of the following columns to utf8:
   - Column COMMENT in COLUMNS\_V2
   - Column PARAM\_VALUE in TABLE\_PARAMS
   - Column PKEY\_COMMENT in PARTITION\_KEYS

For more information about commands, see [ALTER TABLE Statement](https://dev.mysql.com/doc/refman/5.7/en/alter-table.html).

[Model](#model-intro)

---

<a id="datasource-logical_view"></a>

<!-- source_url: https://kylin.apache.org/docs/datasource/logical_view/ -->

<!-- page_index: 23 -->

# Logical View

Version: 5.0.2

- Logical view is a special view maintained only in KYLIN rather than a real view in hive. Once created, you can use it like a normal Hive view.
- Logical view feature is turned off by default, you can set `kylin.source.ddl.logical-view.enabled=true` to turn this feature on.
- All logical views are in the same database, you can set the database name by the following parameters, be careful not to have the same name as the normal Hive database:
  - `kylin.source.ddl.logical-view.database=KYLIN_LOGICAL_VIEW`

1. Log in to KYLIN, and the login account must be:

- System admin.
- Have the Administrator or Project Administrator role for the target project.
- User has Management Role.

2. Click Data Assets - > Logical View to go to the main page of the logical view, you can enter SQL statements in the text box, and there are three tabs which can respectively manage the logical view tables, load the data source and display the syntax rules.
3. Enter the `Create Logical View as...` statement in the SQL text box to create the logical view, noting that the database name is not required.
4. After the view is created, you need to load the source table for Modeling to use. Since the logical view is newly created, you need to click "Refresh Now" first, then find the newly created logical view and then complete the loading.

1. On the main page of the logical view, you can enter SQL statement on the left: `DROP LOGICAL VIEW logical_view_db.your_logical_view;` to delete the logical view. Pay attention that the database name is needed.

1. In the main interface of the logical view, click the 'Logical View Chart' (L) tab, you can see all the created logical views, those of current project will be pinned to the top, and those belonging to other projects will be grey out.
2. Click the pencil icon next to the view to enter view/edit page.
3. On this page, you can view the create view statement.
4. To edit the table definition, click the 'create - > replace' icon
5. You can see that `Create Logical View` in the edit box is replaced with `Replace Logical View`, and then you can modify the previous create table statement. In the following example, the condition of `where 1 = 1` is added.
6. Click Save to complete the editing of the logical view.

1. Logical views must be created under the same virtual database. (The database name can be determined through the parameter above.)
2. In order to prevent users from overriding existing project permissions with the help of logical views, the source table used in logical views needs to be loaded into the data source, and users can only load/edit logical views created under the same project.
3. Logical views currently do not support RDBMS JDBC data sources. It only support Hive data sources.

---

<a id="internaltable-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/internaltable/intro/ -->

<!-- page_index: 24 -->

# Internal Table Overview

Version: 5.0.2

This chapter introduces new feature of Kylin, what is internal table and how it works.

Kylin's pre-calculated technology can help you achieve a sub-second query experience in scenarios with large amounts of data and high concurrency by defining models and indexes. However, not all query and analysis scenarios can be predefined, and from the perspective of construction and storage costs, it is not suitable to pre-calculate indexes for all combinations of dimensions.

Before the business analysis model is fixed, analysts often need to explore flexibly to mine the value and patterns of data, or to prepare for making fixed reports. Due to the variability of analysis dimensions and measures, a limited number of pre-calculated indexes cannot fully cover all query scenarios, and at this time, the on-the-fly calculation capability based on the internal table can come into play.

An internal table refers to a table that is directly managed by Kylin in terms of data and metadata.
Compared with the original data source table that only imports table metadata for modeling, the internal table not only saves metadata but also directly manages user data. Like traditional RDBMS and most data warehouse software, you only need to import data into the internal table to perform query analysis.

You don't have to write DDL statements by yourself. Just click the "Create Internal Table" button on the page of the imported data source table and complete the relevant table property settings to complete the creation of the internal table.
For details, please refer to the [Manage Internal Tables](#internaltable-internal_table_management) page.

There is no need to distinguish between data source tables and internal tables during the query. You can consider them as one table in Kylin, which only has one database name and one table name. The difference lies in that when the internal table function is not turned on or the internal table is not created, the table does not directly manage data and is only used for modeling.

You only need to go to the project settings page, click on the "Internal Table Settings" tab, and turn on the switch for the internal table feature.

After turning on the internal table switch, you can see the "Internal Table" tab in the side navigation bar. Click on it to enter the internal table management page.

In Kylin 4.x and earlier, the system supports the creation of snapshot tables. Starting from Kylin 5.x, when the internal table function is turned on, the snapshot feature will no longer be supported.

---

<a id="internaltable-internal_table_management"></a>

<!-- source_url: https://kylin.apache.org/docs/internaltable/internal_table_management/ -->

<!-- page_index: 25 -->

# Table Management

Version: 5.0.2

> [!NOTE]
> When creating internal tables in batch, the system will not set partition columns or other information by default. If you need to set partition columns, sort columns, etc. please update them later on the internal table management page.

---

<a id="internaltable-load_data_into_internal_table"></a>

<!-- source_url: https://kylin.apache.org/docs/internaltable/load_data_into_internal_table/ -->

<!-- page_index: 26 -->

# Data Loading

Version: 5.0.2

All internal tables, whether partitioned or not, support full data import.
Full import is suitable for tables with a moderate amount of data. If the table has a particularly large amount of data and a time partition column is set, it is recommended to use incremental import.
Hover your mouse over the table you want to import data into and click the data import button. ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAIKSURBVHgBpZNdSFNhGMd/Z7iz4zSvopbmTEeZddGnUJMS6qYuyy4iipIS+9KkMkqltIgC0xIrg9TMPm4Moy6iD5AIAquLIWIfbMasoEtRtuPO1nZ6NzDYdrYu/MF78z4P//d5/u/zSAEtpDMHTOmCkUiE/5GRKuAZn6DjVh9mOYOqyt2UFDsM86TEFqKv9vQNMPzRxbHqfWjBIF3dj9ha7mTXzu1kWTNJ2cLo2DeqjjYgSXChsZahd8O8ePmW8+dqCP0JUVd/iZHRL8YCU9M+rl3v5mz9YRbZFtDY0o6jMB+ncx1XWu8wLzuL46Ki9s57TIvcJA9Uv4rVqvDz12/aOnq4fPEUG0pXi2qkWNlNzW00N53Aqij4VJWcnOx4gVlm1ABlzrXc7OrH5RrDL4Td3yfYUr4RVcQSMfzGlSXLuH+3lYAWRFZkbt9oYXlxkVFqsoBFseDxeAlHdBxFdgrti2M/4xZ3ihBL5F8LSqaFmYBGQX4un7+6OdNwFdvC+WhaiMHnr9nkXM9SxxJ8fj+ZwodZ4ubgzdB7Hj5+SsWObRTY82KDZJFlao7sZ9z7g8Fnrziwt4LNZaUxc5MEokxOTtH74Alut5eTtZWifJ1OYWhero3TdQeR5fg2JKNl0nWdD59G6O0fwCReqj60hzWrVmCElG4bo+aFw2HMZnOqlNTLFMVkMsVOOv4CkhvDinDSvBsAAAAASUVORK5CYII=)

For full import, there is no need to select a time range, the system will import all data from the data source table into the internal table.

Only tables with a time partition column set support incremental import. When performing incremental import, you can set the start and end times for the import. The system will pull data from the data source within this time range and import it into the internal table.

Please note: Internal tables do not have unique key constraints or duplicate data checks. If the time range of the data you import overlaps, duplicate data may occur. If you wish to update certain partition data, you can delete the data of that partition and re-import it.

After submitting the data import task request, you can view the running data import tasks and their progress, status, and logs in "Monitoring" -> "Batch Data Tasks".

![](assets/images/full-load-task-6239bf76404a44e7b282625fb06ad7a4_7aa3b37aafb347b3.png)

---

<a id="internaltable-query_internal_table"></a>

<!-- source_url: https://kylin.apache.org/docs/internaltable/query_internal_table/ -->

<!-- page_index: 27 -->

# Querying Internal Tables

Version: 5.0.2

There is no difference in the query interface between internal table queries and model queries. For details, refer to [SQL Queries](#query-insight).

You do not need to rewrite any SQL, but you must ensure that all tables you are querying have had internal tables created and have imported data.

In the Kylin query interface, you can check the "Query Internal Table" option to skip the model matching phase. If you are certain that your query is a flexible query that cannot be answered through the pre-calculated indexes of the model, checking "Direct Query Internal Table" can save model matching time and thus improve query response speed.

![](assets/images/query-directly-e438069c7080dc77fd6f2ced35101cfb_5e1a283198824f87.png)

By default, "Query Internal Table" is not checked. At this time, the query engine will first prioritize model matching with pre-calculated indexes. When it cannot be answered through the pre-calculated indexes, it will switch to direct querying of the internal table.
If part of a complex query can be answered through the model index and part cannot, the system will attempt to answer through a combination of model indexes and internal table joins.

After the internal table feature is enabled, regardless of whether the tables in the query have been created as internal tables or whether data has been imported, the query will no longer be pushed down to the data source.

---

<a id="model-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/model/intro/ -->

<!-- page_index: 28 -->

# Model

Version: 5.0.2

Kylin utilizes multidimensional modeling theory to build star or snowflake schemas based on tables, making it a powerful tool for large-scale data analysis. The **model** is Kylin's core component, consisting of three key aspects: *model design*, *index design*, and *data loading*. By carefully designing the model, optimizing indexes, and pre-computed data, queries executed on Kylin can avoid scanning the entire dataset, potentially reducing response times to mere seconds, even for petabyte-scale data.

- **Model design** refers to establishing relationships between data tables to enable fast extraction of key information from multidimensional data. The core elements of model design are computed columns, dimensions, measures, and join relations.
- **Index design** refers to creating indexes (CUBEs) within the model to precompute query results, thereby reducing query response time. Well-designed indexes not only improve query performance but also help minimize the storage and data-loading costs associated with precomputation.
- **Data loading** refers to the process of importing data into the model, enabling queries to utilize the pre-built indexes rather than scanning the entire dataset. This allows for faster query responses by leveraging the model's optimized structure.

- **Dimension**: A perspective of viewing data, which can be used to describe object attributes or characteristics, for example, product category.
- **Measure**: An aggregated sum, which is usually a continuous value, for example, product sales.
- **Pre-computation**: The process of aggregating data based on model dimension combinations and of storing the results as indexes to accelerate data query.
- **Index**: Also called CUBE, which is used to accelerate data query. Indexes are divided into:

  - **Aggregate Index**: An aggregated combination of multiple dimensions and measures, and can be used to answer aggregate queries such as total sales for a given year.
  - **Table Index**: A multilevel index in a wide table and can be used to answer detailed queries such as the last 100 transactions of a certain user.

- **Low Query Latency vs. Large Volume**

  When analyzing massive data, there are some techniques to speed up computing and storage, but they cannot change the time complexity of query, that is, query latency and data volume are linearly dependent.

  If it takes 1 minute to query 100 million entries of data records, querying 10 billion data entries will take about 1 hour and 40 minutes. When companies want to analyze all business data piled up over the years or to add complexity to query, say, with more dimensions, queries will be running extremely slow or even time out.

  ![Response Time vs. Data Volume](assets/images/volume-per-time-5c703faf474c956998a461b67470e86c_5f59af49ff70fff0.png)
- **Pre-computation vs. Runtime Computation**

  Pre-computation and runtime computation are two approaches to calculating results in data processing and analytics. **Pre-computation** involves calculating and storing results in advance, so they can be quickly retrieved when a query is run. In contrast, **runtime computation** dynamically computes results during query execution, processing raw data and applying aggregations, filters, or transformations as needed for each query.

  Kylin primarily focuses on **pre-computation** to enhance query performance. However, we also offer advanced features that partially support runtime computation. For more details, please refer to [Table Snapshot](#model-snapshot), [Runtime Join](#model-features-runtime_join), and [Internal Table](#internaltable-intro).
- **Manual Modeling vs. Recommendation**

  Before Kylin 5.0, model design had to be done manually, which was a tedious process requiring extensive knowledge of multidimensional modeling. However, this changed with the introduction of Kylin 5.0. We now offer a new approach to model design, called **recommendation**, which allows models to be created by importing SQL, along with an automatic way to remove unnecessary indexes. Additionally, the system can leverage query history to generate index recommendations, further optimizing query performance. For more details, please refer to [Recommendation](#model-rec-intro).
- **Batch Data vs. Streaming Data**

  In the OLAP field, data has traditionally been processed in batches. However, this is changing as more companies are now required to handle both batch and streaming data to meet their business objectives. The ability to process data in real-time has become increasingly critical for applications such as real-time analytics, monitoring, and event-driven decision-making.

  To address these evolving needs, we have introduced support for streaming data in the new version. This allows users to efficiently process and analyze data as it is generated, complementing the traditional batch processing capabilities. For more details, please refer to [Streaming](#model-streaming-intro).

---

<a id="model-manual-modeling"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manual/modeling/ -->

<!-- page_index: 29 -->

# Manual Modeling

Version: 5.0.2

This chapter explains how to design a manual model in Kylin. In this example, we use the [SSB dataset](#quickstart-tutorial), which is based on real-world business applications, to analyze product and supplier information across various dimensions such as *year*, *city*, *supplier*, and *brand*.

Before starting, ensure that you have created a project and loaded tables from the data source. If you haven't done so yet, please refer to the [Quickstart](#quickstart-intro) chapter for detailed instructions.

First, we will outline some key operations to ensure you have a clear understanding of the manual modeling process. These steps will help guide you through the creation and configuration of a model in Kylin.

| **Main Step Content** | **Description** |
| --- | --- |
| Define the fact table and dimension tables | Tables are the basis for data analysis. Kylin only supports one fact table, therefore kylin only support star or snowflake model. |
| Create the join relations | Join relations is linked by the paired foreign keys and primary keys. Manual modeling only supports inner or left join. |
| Add computed columns | Computed columns are expressions without aggregations. They can be utilized by dimensions and measures. More details please refer to [Computed Column](#model-manual-computed_column) |
| Add the dimensions and measures | Dimensions and measures will be used for generating indexes. They constraint the scope of indexes. |
| Specify the way of data loading | Choose increment data loading or full data loading. Increment loading needs setting date partition column. |
| Save the model | Save the model and set the loading method. |

Log in to Kylin with a role that has model management permissions. In the left navigation panel, click **Data Asset** > **Model**. You will then be directed to a page displaying the list of models, as shown below.

![model_list.png](assets/images/model-list-8d256b51f17271daa6a86840ad0bbcca_5f3ecaa7861824f1.png)

Click the **![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Qm94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHZlcnNpb249IjEuMSI+CiAgICA8cGF0aCBkPSJNOCAydjEyTTIgOGgxMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgoK) New** button to create a new model. In the pop-up dialog box, enter a name and description for the model, then click the **Create** button. You will be redirected to the model editing page where you can begin configuring your new model.

![model_list.png](assets/images/modeling1-780d6abfc1a9fc2a5364474189f510ad_7333240c22b49fe9.png)

> [!TIP]
> **Tips**
> Model name can be any combination of numbers, letters, and underscores (\_).

On the model editing page, you can drag and drop tables onto the canvas. The system will automatically recommend the first table you drag as the fact table. You can either confirm this by selecting **Switch to Fact Table** or set the fact table later. In this example, the fact table is **P\_LINEORDER**.

![](assets/images/set-fact-table-65c7e03d9c7c879eb3da1752d2a884d3_6c4a5aba0b5a0a34.png)

> [!TIP]
> **Tips**
> If there is no table in the **Data Source** on the model editing page, please [load data source](#datasource-intro) first.

You can create either a single-table model or a multi-table model. For a multi-table model, you'll need to add additional tables and define the join relationships between them. Besides the fact table, the other tables will serve as dimension tables, also known as lookup tables. Dimension tables typically store recurring attributes of the fact table, such as dates or geographic locations. Including dimension tables in the model helps reduce the size of the fact table and improves the efficiency of dimension management. After adding all the necessary tables, the model page will look like the following.

![](assets/images/added-tables-ebc72ef18086cea932a2ed74f3bd7a27_cb1391b0739f5947.png)

At this stage, the tables are ready to be joined. You can drag the foreign keys from the fact table to the corresponding primary keys in the dimension tables to establish the relationships. In a **star schema**, all foreign keys originate from the fact table, whereas in a **snowflake schema**, foreign keys can come from dimension tables as well. In this example, we are working with a star schema. The following GIF demonstrates the process in detail.

![](assets/images/create-join-relations-86583e446bba33b7aed878395d356b77_530af12a45a936ca.gif)

In the **Add Join Relationship** dialog box, follow the steps below to configure the join relationships:

- **Join Relationship for Tables**: This section contains three drop-down lists for specifying the primary table, foreign table, and join type. Kylin supports **LEFT** joins and **INNER** joins only.
- **Table Relationship**: Defines the mapping between foreign keys and primary keys, which can be **One-to-One or Many-to-One**, **One-to-Many or Many-to-Many**.
- **Precompute Join Relationship**: Indicates whether the join between the primary table and foreign table is precomputed. By default, the primary table is precomputed. For more information on this advanced feature, refer to [Runtime Join](#model-features-runtime_join).
- **Join Relationship for Columns**: This section consists of three drop-down lists to define the primary column, foreign column, and comparison operator. You can specify multiple pairs of primary and foreign keys, which will be combined with an *AND* operator. The default comparison operator is **=**, indicating an equal join. For non-equal joins, refer to the advanced feature [SCD2](#model-features-scd2) for further details.

![](assets/images/add-join-relations-ab3f202aff20a7cdfdf6fb7653d9711b_aaf5e44208a494b4.png)

> [!TIP]
> **Tips**
> Join relations should meet the following requirements:
>
> - Do not define more than one join relation for the same column; two tables could only be joined by the same condition for one time
> - Join relations for columns should include at least one equal-join condition (=)
> - Join relations ≥ and < must be used in pairs, and the column in between must be the same. Example: B ≥ A, C < A

After the tedious process, you can get a model with four join relations as shown below.

![](assets/images/joined-tables-880a42123397d2992e8d97b689174200_6c0b8319986f5b2a.png)

This model can also be created directly using the following SQL statement. While this approach is straightforward, it leverages a new feature. For more information, please refer to [Modeling by SQL](#model-rec-sql_modeling).

```sql
SELECT 
    1 
FROM SSB.P_LINEORDER 
         LEFT JOIN SSB.DATES ON P_LINEORDER.LO_ORDERDATE = DATES.D_DATEKEY 
         LEFT JOIN SSB.CUSTOMER ON P_LINEORDER.LO_CUSTKEY = CUSTOMER.C_CUSTKEY 
         LEFT JOIN SSB.SUPPLIER ON P_LINEORDER.LO_SUPPKEY = SUPPLIER.S_SUPPKEY 
         LEFT JOIN SSB.PART ON P_LINEORDER.LO_PARTKEY = PART.P_PARTKEY 
```

This section of content is optional and may seem a bit complex, so we will cover it in the chapter of [Computed Column](#model-manual-computed_column).

On the model editing page, there are two ways to add dimensions:

1. Drag the desired column from the joined tables to the **Dimension** card.
2. Click the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIj4KICAgIDxwYXRoIGQ9Ik03ODkuMzMzMzMzIDEwNi42NjY2NjdhMTE3LjMzMzMzMyAxMTcuMzMzMzMzIDAgMCAxIDExNy4yNDggMTEyLjYxODY2NmwwLjA4NTMzNCA0LjcxNDY2N3Y0MDUuMzMzMzMzYTExNy4zMzMzMzMgMTE3LjMzMzMzMyAwIDAgMS0xMTIuNjE4NjY3IDExNy4yNDhMNzg5LjMzMzMzMyA3NDYuNjY2NjY3aC0xMC42NjY2NjZ2NDIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEtODUuMzMzMzM0IDg1LjMzMzMzNGgtNDY5LjMzMzMzM2E4NS4zMzMzMzMgODUuMzMzMzMzIDAgMCAxLTg1LjMzMzMzMy04NS4zMzMzMzRWMzIwYTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzMzLTg1LjMzMzMzM2g0Mi42NjY2Njd2LTEwLjY2NjY2N2ExMTcuMzMzMzMzIDExNy4zMzMzMzMgMCAwIDEgMTEyLjYxODY2Ni0xMTcuMjQ4TDM4NCAxMDYuNjY2NjY3aDQwNS4zMzMzMzN6IG0tOTYgMTkyaC00NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMjEuMTg0IDE4LjgzNzMzM0wyMDIuNjY2NjY3IDMyMHY0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMTguODM3MzMzIDIxLjE4NEwyMjQgODEwLjY2NjY2N2g0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMjEuMTg0LTE4LjgzNzMzNEw3MTQuNjY2NjY3IDc4OS4zMzMzMzNWMzIwYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMTguODM3MzM0LTIxLjE4NEw2OTMuMzMzMzMzIDI5OC42NjY2Njd6IG0tMjM0LjY2NjY2NiA5NmEzMiAzMiAwIDAgMSAzMS44NTA2NjYgMjguOTI4TDQ5MC42NjY2NjcgNDI2LjY2NjY2N3Y5Nmg5NmEzMiAzMiAwIDAgMSAzLjA3MiA2My44NTA2NjZsLTMuMDcyIDAuMTQ5MzM0SDQ5MC42NjY2NjdWNjgyLjY2NjY2N2EzMiAzMiAwIDAgMS02My44NTA2NjcgMy4wNzJMNDI2LjY2NjY2NyA2ODIuNjY2NjY3di05NmgtOTZhMzIgMzIgMCAwIDEtMy4wNzItNjMuODUwNjY3bDMuMDcyLTAuMTQ5MzMzSDQyNi42NjY2NjdWNDI2LjY2NjY2N2EzMiAzMiAwIDAgMSAzMi0zMnpNNzg5LjMzMzMzMyAxNzAuNjY2NjY3SDM4NGE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwLTUzLjIyNjY2NyA0OS44MzQ2NjZsLTAuMTA2NjY2IDMuNDk4NjY3djEwLjY2NjY2N2gzNjIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzM0IDg1LjMzMzMzM3YzNjIuNjY2NjY3aDEwLjY2NjY2NmE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwIDUzLjIyNjY2Ny00OS44MzQ2NjdsMC4xMDY2NjctMy40OTg2Njd2LTQwNS4zMzMzMzNhNTMuMzMzMzMzIDUzLjMzMzMzMyAwIDAgMC00OS44MzQ2NjctNTMuMjI2NjY3TDc4OS4zMzMzMzMgMTcwLjY2NjY2N3oiCiAgICAgICAgICBmaWxsPSIjNDA0MzRFIj48L3BhdGg+Cjwvc3ZnPgo=) button in the **Dimension** card. When you hover over the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIj4KICAgIDxwYXRoIGQ9Ik03ODkuMzMzMzMzIDEwNi42NjY2NjdhMTE3LjMzMzMzMyAxMTcuMzMzMzMzIDAgMCAxIDExNy4yNDggMTEyLjYxODY2NmwwLjA4NTMzNCA0LjcxNDY2N3Y0MDUuMzMzMzMzYTExNy4zMzMzMzMgMTE3LjMzMzMzMyAwIDAgMS0xMTIuNjE4NjY3IDExNy4yNDhMNzg5LjMzMzMzMyA3NDYuNjY2NjY3aC0xMC42NjY2NjZ2NDIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEtODUuMzMzMzM0IDg1LjMzMzMzNGgtNDY5LjMzMzMzM2E4NS4zMzMzMzMgODUuMzMzMzMzIDAgMCAxLTg1LjMzMzMzMy04NS4zMzMzMzRWMzIwYTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzMzLTg1LjMzMzMzM2g0Mi42NjY2Njd2LTEwLjY2NjY2N2ExMTcuMzMzMzMzIDExNy4zMzMzMzMgMCAwIDEgMTEyLjYxODY2Ni0xMTcuMjQ4TDM4NCAxMDYuNjY2NjY3aDQwNS4zMzMzMzN6IG0tOTYgMTkyaC00NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMjEuMTg0IDE4LjgzNzMzM0wyMDIuNjY2NjY3IDMyMHY0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMTguODM3MzMzIDIxLjE4NEwyMjQgODEwLjY2NjY2N2g0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMjEuMTg0LTE4LjgzNzMzNEw3MTQuNjY2NjY3IDc4OS4zMzMzMzNWMzIwYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMTguODM3MzM0LTIxLjE4NEw2OTMuMzMzMzMzIDI5OC42NjY2Njd6IG0tMjM0LjY2NjY2NiA5NmEzMiAzMiAwIDAgMSAzMS44NTA2NjYgMjguOTI4TDQ5MC42NjY2NjcgNDI2LjY2NjY2N3Y5Nmg5NmEzMiAzMiAwIDAgMSAzLjA3MiA2My44NTA2NjZsLTMuMDcyIDAuMTQ5MzM0SDQ5MC42NjY2NjdWNjgyLjY2NjY2N2EzMiAzMiAwIDAgMS02My44NTA2NjcgMy4wNzJMNDI2LjY2NjY2NyA2ODIuNjY2NjY3di05NmgtOTZhMzIgMzIgMCAwIDEtMy4wNzItNjMuODUwNjY3bDMuMDcyLTAuMTQ5MzMzSDQyNi42NjY2NjdWNDI2LjY2NjY2N2EzMiAzMiAwIDAgMSAzMi0zMnpNNzg5LjMzMzMzMyAxNzAuNjY2NjY3SDM4NGE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwLTUzLjIyNjY2NyA0OS44MzQ2NjZsLTAuMTA2NjY2IDMuNDk4NjY3djEwLjY2NjY2N2gzNjIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzM0IDg1LjMzMzMzM3YzNjIuNjY2NjY3aDEwLjY2NjY2NmE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwIDUzLjIyNjY2Ny00OS44MzQ2NjdsMC4xMDY2NjctMy40OTg2Njd2LTQwNS4zMzMzMzNhNTMuMzMzMzMzIDUzLjMzMzMzMyAwIDAgMC00OS44MzQ2NjctNTMuMjI2NjY3TDc4OS4zMzMzMzMgMTcwLjY2NjY2N3oiCiAgICAgICAgICBmaWxsPSIjNDA0MzRFIj48L3BhdGg+Cjwvc3ZnPgo=) button, a tooltip labeled **Batch Add** appears, indicating that you can add multiple dimensions simultaneously.

The following GIF illustrates these ways in detail.

![](assets/images/add-dimension-a75fab2a511446068d868677f4b39058_ec36298c4a7be792.gif)

By default, the dimension name matches the column name. However, if duplicate columns share the same name, the system will automatically modify the dimension name by appending the table alias, separated by an underscore (*\_*). Additionally, you can manually specify the dimension name, which can include any combination of letters, numbers, spaces, and special characters such as `_ -()%?`.

In our example, we add the columns *LO\_CUSTKEY* and *LO\_SUPPKEY* from the table *P\_LINEORDER* as dimensions.

Deleting dimensions is similar to adding them. However, if a dimension is being used by any indexes, you must delete the associated indexes first. Otherwise, the deletion operation will fail.

On the model editing page, there are three ways to add measures:

1. Drag the desired column from the joined tables to the **Measure** card.
2. Click the left ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Qm94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHZlcnNpb249IjEuMSI+CiAgICA8cGF0aCBkPSJNOCAydjEyTTIgOGgxMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgoK) button in the **Measure** card. When you hover over the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Qm94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHZlcnNpb249IjEuMSI+CiAgICA8cGF0aCBkPSJNOCAydjEyTTIgOGgxMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgoK) button, a tooltip labeled **Add** appears, indicating that you can add one measure. Click the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiB2aWV3Qm94PSIwIDAgMTYgMTYiIGZpbGw9Im5vbmUiIHZlcnNpb249IjEuMSI+CiAgICA8cGF0aCBkPSJNOCAydjEyTTIgOGgxMiIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgoK) button, it will pop up the **Add Measure** dialog box to guide you what to do next.
3. Click the middle ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIj4KICAgIDxwYXRoIGQ9Ik03ODkuMzMzMzMzIDEwNi42NjY2NjdhMTE3LjMzMzMzMyAxMTcuMzMzMzMzIDAgMCAxIDExNy4yNDggMTEyLjYxODY2NmwwLjA4NTMzNCA0LjcxNDY2N3Y0MDUuMzMzMzMzYTExNy4zMzMzMzMgMTE3LjMzMzMzMyAwIDAgMS0xMTIuNjE4NjY3IDExNy4yNDhMNzg5LjMzMzMzMyA3NDYuNjY2NjY3aC0xMC42NjY2NjZ2NDIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEtODUuMzMzMzM0IDg1LjMzMzMzNGgtNDY5LjMzMzMzM2E4NS4zMzMzMzMgODUuMzMzMzMzIDAgMCAxLTg1LjMzMzMzMy04NS4zMzMzMzRWMzIwYTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzMzLTg1LjMzMzMzM2g0Mi42NjY2Njd2LTEwLjY2NjY2N2ExMTcuMzMzMzMzIDExNy4zMzMzMzMgMCAwIDEgMTEyLjYxODY2Ni0xMTcuMjQ4TDM4NCAxMDYuNjY2NjY3aDQwNS4zMzMzMzN6IG0tOTYgMTkyaC00NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMjEuMTg0IDE4LjgzNzMzM0wyMDIuNjY2NjY3IDMyMHY0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMTguODM3MzMzIDIxLjE4NEwyMjQgODEwLjY2NjY2N2g0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMjEuMTg0LTE4LjgzNzMzNEw3MTQuNjY2NjY3IDc4OS4zMzMzMzNWMzIwYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMTguODM3MzM0LTIxLjE4NEw2OTMuMzMzMzMzIDI5OC42NjY2Njd6IG0tMjM0LjY2NjY2NiA5NmEzMiAzMiAwIDAgMSAzMS44NTA2NjYgMjguOTI4TDQ5MC42NjY2NjcgNDI2LjY2NjY2N3Y5Nmg5NmEzMiAzMiAwIDAgMSAzLjA3MiA2My44NTA2NjZsLTMuMDcyIDAuMTQ5MzM0SDQ5MC42NjY2NjdWNjgyLjY2NjY2N2EzMiAzMiAwIDAgMS02My44NTA2NjcgMy4wNzJMNDI2LjY2NjY2NyA2ODIuNjY2NjY3di05NmgtOTZhMzIgMzIgMCAwIDEtMy4wNzItNjMuODUwNjY3bDMuMDcyLTAuMTQ5MzMzSDQyNi42NjY2NjdWNDI2LjY2NjY2N2EzMiAzMiAwIDAgMSAzMi0zMnpNNzg5LjMzMzMzMyAxNzAuNjY2NjY3SDM4NGE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwLTUzLjIyNjY2NyA0OS44MzQ2NjZsLTAuMTA2NjY2IDMuNDk4NjY3djEwLjY2NjY2N2gzNjIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzM0IDg1LjMzMzMzM3YzNjIuNjY2NjY3aDEwLjY2NjY2NmE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwIDUzLjIyNjY2Ny00OS44MzQ2NjdsMC4xMDY2NjctMy40OTg2Njd2LTQwNS4zMzMzMzNhNTMuMzMzMzMzIDUzLjMzMzMzMyAwIDAgMC00OS44MzQ2NjctNTMuMjI2NjY3TDc4OS4zMzMzMzMgMTcwLjY2NjY2N3oiCiAgICAgICAgICBmaWxsPSIjNDA0MzRFIj48L3BhdGg+Cjwvc3ZnPgo=) button in the **Measure** card. When you hover over the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIj4KICAgIDxwYXRoIGQ9Ik03ODkuMzMzMzMzIDEwNi42NjY2NjdhMTE3LjMzMzMzMyAxMTcuMzMzMzMzIDAgMCAxIDExNy4yNDggMTEyLjYxODY2NmwwLjA4NTMzNCA0LjcxNDY2N3Y0MDUuMzMzMzMzYTExNy4zMzMzMzMgMTE3LjMzMzMzMyAwIDAgMS0xMTIuNjE4NjY3IDExNy4yNDhMNzg5LjMzMzMzMyA3NDYuNjY2NjY3aC0xMC42NjY2NjZ2NDIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEtODUuMzMzMzM0IDg1LjMzMzMzNGgtNDY5LjMzMzMzM2E4NS4zMzMzMzMgODUuMzMzMzMzIDAgMCAxLTg1LjMzMzMzMy04NS4zMzMzMzRWMzIwYTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzMzLTg1LjMzMzMzM2g0Mi42NjY2Njd2LTEwLjY2NjY2N2ExMTcuMzMzMzMzIDExNy4zMzMzMzMgMCAwIDEgMTEyLjYxODY2Ni0xMTcuMjQ4TDM4NCAxMDYuNjY2NjY3aDQwNS4zMzMzMzN6IG0tOTYgMTkyaC00NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMjEuMTg0IDE4LjgzNzMzM0wyMDIuNjY2NjY3IDMyMHY0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMTguODM3MzMzIDIxLjE4NEwyMjQgODEwLjY2NjY2N2g0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMjEuMTg0LTE4LjgzNzMzNEw3MTQuNjY2NjY3IDc4OS4zMzMzMzNWMzIwYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMTguODM3MzM0LTIxLjE4NEw2OTMuMzMzMzMzIDI5OC42NjY2Njd6IG0tMjM0LjY2NjY2NiA5NmEzMiAzMiAwIDAgMSAzMS44NTA2NjYgMjguOTI4TDQ5MC42NjY2NjcgNDI2LjY2NjY2N3Y5Nmg5NmEzMiAzMiAwIDAgMSAzLjA3MiA2My44NTA2NjZsLTMuMDcyIDAuMTQ5MzM0SDQ5MC42NjY2NjdWNjgyLjY2NjY2N2EzMiAzMiAwIDAgMS02My44NTA2NjcgMy4wNzJMNDI2LjY2NjY2NyA2ODIuNjY2NjY3di05NmgtOTZhMzIgMzIgMCAwIDEtMy4wNzItNjMuODUwNjY3bDMuMDcyLTAuMTQ5MzMzSDQyNi42NjY2NjdWNDI2LjY2NjY2N2EzMiAzMiAwIDAgMSAzMi0zMnpNNzg5LjMzMzMzMyAxNzAuNjY2NjY3SDM4NGE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwLTUzLjIyNjY2NyA0OS44MzQ2NjZsLTAuMTA2NjY2IDMuNDk4NjY3djEwLjY2NjY2N2gzNjIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzM0IDg1LjMzMzMzM3YzNjIuNjY2NjY3aDEwLjY2NjY2NmE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwIDUzLjIyNjY2Ny00OS44MzQ2NjdsMC4xMDY2NjctMy40OTg2Njd2LTQwNS4zMzMzMzNhNTMuMzMzMzMzIDUzLjMzMzMzMyAwIDAgMC00OS44MzQ2NjctNTMuMjI2NjY3TDc4OS4zMzMzMzMgMTcwLjY2NjY2N3oiCiAgICAgICAgICBmaWxsPSIjNDA0MzRFIj48L3BhdGg+Cjwvc3ZnPgo=) button, a tooltip labeled **Batch Add** appears, indicating that you can add multiple measures. Click it, it will pop up the **Quick Add Measure** dialog box to let you define measures more easily.

The following GIF illustrates these ways in detail.

![](assets/images/add-measure-22b14615dbc64b78aaf9180d791dd60e_831e8558bca636c2.gif)

In the **Add Measure** dialog box, you can adjust the following properties if needed:

- **Name**: By default, it is the column name. It can be any combination of letters, numbers, spaces, and special characters such as `_ -()%?`.
- **Function**: Defaults to *SUM (column)*. Kylin supports a variety of built-in aggregation functions, including Count Distinct and TopN. If you want to know advanced measures like *TopN*, refer to [Advanced measures](#model-features-measures-intro).
- **Column**: Specifies the column of measure. If using the first way, this is set automatically. If you're using the second way, you'll need to select the column that serves as the parameter for the measure.
- **Comment** (Optional): Adding a comment to explain the measure’s purpose can be helpful for who cares about the meaning.

In the **Quick Add Measure** dialog box, you can create measures using *SUM*, *COUNT*, *MIN*, *MAX*, and *COUNT DISTINCT* functions. When using this option, the measure name is generated automatically, and you cannot modify the name or add a comment.

In our example, we added three measures to the model:

- *SUM(LO\_QUANTITY)* with the name **LO\_QUANTITY**.
- *SUM(LO\_EXTENDEDPRICE)* with the name **mea1**.
- *MAX(LO\_ORDERDATE)* with the name **LO\_ORDERDATE\_MAX**.

> [!TIP]
> **Warning**
> Ensure that the measure name is different from the column name, as this may cause issues when integrating with BI tools.

Deleting measures is similar to adding them. However, if a measure is being used by any indexes, you must delete the associated indexes first. Otherwise, the deletion operation will fail.

When saving the model, there are several steps to be completed: setting the data loading method, configuring the data filter condition, and adding base indexes.

After adding dimensions and measures, you need to set the data loading method by clicking the **Save** button in the upper right corner of the model editing page. When you click this button, the **Save Model** dialog box will appear. In this dialog box, you'll be prompted to choose between **Incremental Load Recommended** and **Full Load** options for data loading.

![data_loading_ways.png](assets/images/data-loading-ways-0af0d898a57d12ebd79383b069918cee_70d90886323e93a1.png)

- **Full Load**: This option loads and pre-computes all data from the source table based on the different combinations of dimensions and measures.
- **Incremental Load**: This option loads and pre-computes only the data within a specified time range, according to the combinations of dimensions and measures. If this option is selected, you will need to specify the following parameters:

  - **Partition Table**: The fact table (default and cannot be changed).
  - **Time Partition Column**: Select a column of the time type from the partition table.
  - **Time Format**: Choose the appropriate time format, or click the ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ij4KICAgIDxwYXRoIGQ9Ik03NC42NjY2NjcgNDA1LjMzMzMzM2EzMiAzMiAwIDAgMSAzMi0zMmg4MTAuNjY2NjY2YTMyIDMyIDAgMCAxIDMyIDMydjI5OC42NjY2NjdhMzIgMzIgMCAwIDEtNjQgMHYtMjY2LjY2NjY2N0gxMzguNjY2NjY3Vjg3NC42NjY2NjdjMCA1Ljg4OCA0Ljc3ODY2NyAxMC42NjY2NjcgMTAuNjY2NjY2IDEwLjY2NjY2Nkg1MTJhMzIgMzIgMCAwIDEgMCA2NEgxNDkuMzMzMzMzYTc0LjY2NjY2NyA3NC42NjY2NjcgMCAwIDEtNzQuNjY2NjY2LTc0LjY2NjY2NnYtNDY5LjMzMzMzNHoiCiAgICAgICAgICBmaWxsPSIjMzYzQTNBIj48L3BhdGg+CiAgICA8cGF0aCBkPSJNMTQ5LjMzMzMzMyAyMDIuNjY2NjY3YTEwLjY2NjY2NyAxMC42NjY2NjcgMCAwIDAtMTAuNjY2NjY2IDEwLjY2NjY2NnYxNjBoNzQ2LjY2NjY2NlYyMTMuMzMzMzMzYTEwLjY2NjY2NyAxMC42NjY2NjcgMCAwIDAtMTAuNjY2NjY2LTEwLjY2NjY2NmgtNzI1LjMzMzMzNHpNNzQuNjY2NjY3IDIxMy4zMzMzMzNjMC00MS4yMTYgMzMuNDUwNjY3LTc0LjY2NjY2NyA3NC42NjY2NjYtNzQuNjY2NjY2aDcyNS4zMzMzMzRjNDEuMjE2IDAgNzQuNjY2NjY3IDMzLjQ1MDY2NyA3NC42NjY2NjYgNzQuNjY2NjY2djE5MmEzMiAzMiAwIDAgMS0zMiAzMmgtODEwLjY2NjY2NmEzMiAzMiAwIDAgMS0zMi0zMlYyMTMuMzMzMzMzeiIKICAgICAgICAgIGZpbGw9IiMzNjNBM0EiPjwvcGF0aD4KICAgIDxwYXRoIGQ9Ik0zNDEuMzMzMzMzIDc0LjY2NjY2N2EzMiAzMiAwIDAgMSAzMiAzMnYxNzAuNjY2NjY2YTMyIDMyIDAgMCAxLTY0IDB2LTE3MC42NjY2NjZBMzIgMzIgMCAwIDEgMzQxLjMzMzMzMyA3NC42NjY2Njd6TTY4Mi42NjY2NjcgNzQuNjY2NjY3YTMyIDMyIDAgMCAxIDMyIDMydjE3MC42NjY2NjZhMzIgMzIgMCAwIDEtNjQgMHYtMTcwLjY2NjY2NmEzMiAzMiAwIDAgMSAzMi0zMnpNNjQwIDU2NS4zMzMzMzNhMTE3LjMzMzMzMyAxMTcuMzMzMzMzIDAgMSAwIDAgMjM0LjY2NjY2NyAxMTcuMzMzMzMzIDExNy4zMzMzMzMgMCAwIDAgMC0yMzQuNjY2NjY3ek00NTguNjY2NjY3IDY4Mi42NjY2NjdhMTgxLjMzMzMzMyAxODEuMzMzMzMzIDAgMSAxIDM2Mi42NjY2NjYgMCAxODEuMzMzMzMzIDE4MS4zMzMzMzMgMCAwIDEtMzYyLjY2NjY2NiAweiIKICAgICAgICAgIGZpbGw9IiMzNjNBM0EiPjwvcGF0aD4KICAgIDxwYXRoIGQ9Ik03NDMuNDI0IDc2OC44NTMzMzNhMzIgMzIgMCAwIDEgNDUuMDU2LTQuMDk2bDEyOCAxMDYuNjY2NjY3YTMyIDMyIDAgMSAxLTQwLjk2IDQ5LjE1MmwtMTI4LTEwNi42NjY2NjdhMzIgMzIgMCAwIDEtNC4wOTYtNDUuMDU2eiIKICAgICAgICAgIGZpbGw9IiMzNjNBM0EiPjwvcGF0aD4KPC9zdmc+Cg==) icon, and Kylin will automatically detect and fill in the time format.

![](assets/images/incremental-loading-ed86696ce1a3ebe911d98d4706f603d5_b4c5a6af651b4ddb.png)

As shown in the picture above, there is an **Advanced Setting** card. By expanding this card, you can set the **data filter condition**, which is useful for filtering out null values or data that meets specific criteria. You can use the *AND* and *OR* operators to combine multiple filters. For example, you might use a condition like *BUYER\_ID <> 0001 AND COUNT\_ITEM > 1000 OR TOTAL\_PRICE = 1000*.

Base indexes are beneficial for business scenarios where users are aware of the dimensions and measures but may not know how to organize them into indexes by aggregate groups. Adding base indexes to the model is optional and is disabled by default. You can enable this feature by checking the boxes next to **Base Aggregate Index** and **Base Table Index**.

- **Base Aggregate Index**: This index includes all model dimensions and measures.
- **Base Table Index**: This index includes all columns associated with the model dimensions and measures.

After clicking the **Save** button, a dialog box will appear, allowing you to add indexes.

![redirect_to_add_index.png](assets/images/redirect-to-add-index-8f381a89b1bdf8f29c7c94d6933e1d02_ce9516f8d700366e.png)

You can select the **Not Now** button to be redirected to the **Model List** page, as shown below.

![finished_modeling.png](assets/images/finished-modeling-63baea8f1af4824ebe3af170ef8a9a39_8aa8388f55deb505.png)

We have now completed the model design. The next step is to add [aggregate indexes](#model-manual-aggregation_group) and [table indexes](#model-manual-table_index), and then proceed to [build them](#model-manage-data_loading). After completing these steps, you can query the **Insight** page, where the SQL generated by the model will be displayed on the results page.

> [!NOTE]
> When the time format is customized as *yyyyMMddHHmmss*, the corresponding column in the Hive table should be strings, or Kylin may fail to recognize column data.

---

<a id="model-manual-aggregation_group"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manual/aggregation_group/ -->

<!-- page_index: 30 -->

# Aggregate Index

Version: 5.0.2

Kylin is renowned for enhancing query performance by pre-calculated aggregate groups, which represent various combinations of all dimensions, also known as cuboids. However, it faces the well-known challenge of the **curse of dimensionality**—as the number of dimensions increases, the number of possible indices grows exponentially (2^n - 1). For example, with 3 dimensions, there are 7 possible indices, but with 10 dimensions, the number of cuboids surges to 1023.

To address this challenge, Kylin employs an **aggregation group mechanism** that optimizes the management of high-dimensional data, helping to reduce the complexity and significantly improve query performance.

To create aggregate indexes, it is important to understand the following key concepts:

- **Aggregate Group**: Defines specific sets of dimensions that should be aggregated together, limiting the scope of combinations to what is most relevant for queries.
- **Joint Dimension**: Groups dimensions that are frequently queried together, helping to optimize index creation for common query patterns.
- **Hierarchy Dimension**: Establishes a hierarchy among dimensions, ensuring that when one dimension is queried, all related dimensions are considered, reducing unnecessary combinations.
- **Mandatory Dimension**: Marks certain dimensions as essential, ensuring they are always included in index combinations, which helps avoid generating irrelevant cuboids.

These settings are crucial for optimizing the index-building process, as they minimize both storage and computation costs while maintaining efficient query performance.

In this chapter, we will first guide you through the process of designing an **Aggregation Group**. Following that, we will delve into the principles behind aggregation groups, equipping you with the knowledge to design them effectively.

The following GIF demonstrates how to navigate to the Aggregation Group page.

![agg_group_page.gif](assets/images/to-agg-group-page-0018a29e8c2fbb0061ce4dd4421e5211_b2eca7016d881657.gif)

On the **Aggregation Group** page, when you hover over the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICAgIDxwYXRoIGQ9Ik0xIDFoMTR2MTRIMXoiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8cGF0aCBkPSJNOCA0djhNNCA4aDgiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgo=) button, a tooltip will appear displaying **Add Aggregate Group**. By clicking this button, you will be redirected to the page for adding an aggregate group, as shown below.

![Edit Aggregate Index](assets/images/add-agg-group-4090597cd894bbd93bd92ffbb00f5b8e_b34c4877c1aac51c.png)

Alternatively, you can navigate to the same page by clicking the **![add_icon2.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIKICAgICB3aWR0aD0iMTAiIGhlaWdodD0iMTAiPgogICAgPGNpcmNsZSBjeD0iNjUwIiBjeT0iNjUwIiByPSIzNTAiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS13aWR0aD0iNjQiLz4KICAgIDxwYXRoIGQ9Ik02NTAgMzI1djY1ME0zMjUgNjUwaDY1MCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSI2NCIvPgo8L3N2Zz4K)Aggregate Group** button. Both methods will take you to the interface where you can define the dimensions and measures for the aggregation group, and configure advanced settings such as **Mandatory**, **Hierarchy**, and **Joint** dimensions. Additionally, there is an option to set the **Max Dimension Combination**, which limits the maximum number of dimension combinations allowed for the aggregation group, helping to optimize performance and manage storage effectively.

When you click the **![add_icon2.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIKICAgICB3aWR0aD0iMTAiIGhlaWdodD0iMTAiPgogICAgPGNpcmNsZSBjeD0iNjUwIiBjeT0iNjUwIiByPSIzNTAiIHN0cm9rZT0iYmxhY2siIGZpbGw9Im5vbmUiIHN0cm9rZS13aWR0aD0iNjQiLz4KICAgIDxwYXRoIGQ9Ik02NTAgMzI1djY1ME0zMjUgNjUwaDY1MCIgc3Ryb2tlPSJibGFjayIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSI2NCIvPgo8L3N2Zz4K)Add** button on the **Include** sub-page, a dialog box labeled **Edit Included Dimensions** will appear. This dialog allows you to select the dimensions for the aggregate group. In this example, we will select all available dimensions and then click the **OK** button to confirm the selection.

![Dimension Setting](assets/images/include-dimensions-14c63dd1c9447556222398508fd5ec1b_ce362b21a1b80f78.png)

After selecting the dimensions to be included, the next step is to configure the **Mandatory Dimensions**, **Hierarchy Dimensions**, and **Joint Dimensions**. Tooltips are available to assist in understanding these settings—when the icon ![info_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICAgIDxjaXJjbGUgY3g9IjgiIGN5PSI4IiByPSI3IiBmaWxsPSJkYXJrZ3JheSIgLz4KICAgIDxnIHRyYW5zZm9ybT0icm90YXRlKDE4MCwgOCwgOCkiPgogICAgICAgIDxwYXRoIGQ9Ik04IDR2NSIgc3Ryb2tlPSJ3aGl0ZSIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiLz4KICAgICAgICA8Y2lyY2xlIGN4PSI4IiBjeT0iMTEuNSIgcj0iMSIgZmlsbD0id2hpdGUiLz4KICAgIDwvZz4KPC9zdmc+Cg==) was clicked, they provide explanatory messages. For instance, the tooltip for **mandatory dimension** shows: "If a dimension is set as a mandatory dimension, only the index with this dimension will be calculated."

In our example:

- *LO\_ORDERDATE* is designated as a mandatory dimension, ensuring that any query using the aggregation group must include this dimension.
- *LO\_CUSTKEY* and *LO\_SUPPKEY* are configured as joint dimensions, indicating that these dimensions are frequently queried together and should be optimized accordingly.
- *D\_DATE*, *D\_MONTH*, and *D\_YEAR* are set as hierarchy dimensions, establishing a parent-child relationship that allows for drill-down queries, such as from year to month to date.

![include_dimensions.png](assets/images/defined-agg-group-25a75829237433bbdcba547453b3ded3_a9582507f8c8d1d5.png)

At the bottom of the page, you'll notice a label of *Max Dimension Combination*. This setting applies globally to all aggregation groups within the model, meaning it defines the maximum number of dimension combinations allowed for the entire model. Each individual aggregation group also has its own setting, which works independently for that specific group.

In our example, the max dimension combination for the model is set to 4, meaning the maximum number of dimension combinations across all aggregation groups cannot exceed this limit. However, for the aggregation group *Aggregate-Group-1*, the limit is set to 3, meaning this particular group can only combine up to 3 dimensions.

When you choose the page of **Measure**, you can define all the measures of this aggregate group. By default, all the measures of model are included in the aggregate group, if you don't need all of them, you can edit the content.

![include_dimensions.png](assets/images/include-measures-831f56786812ebca9362bb488b7c32cc_19c223c89875093a.png)

After completing all the steps mentioned above, you'll have an aggregation group ready to be saved, as shown in the picture above. If you want to add more aggregation groups, simply click the **Add Aggregate Group** button. In this example, we have defined just one aggregation group. Once you're done, click the **Save** button, and you will be directed back to the **Aggregation Group** page as follows.

![include_dimensions.png](assets/images/agg-group-page-45df7064048bb615bd34b20a374e34aa_5249b137a03a313d.png)

You may notice the **Text Recognition** button, which is particularly useful when your model contains a large number of dimensions. This feature allows you to prepare the dimensions in advance, paste them into the provided text box, and then execute the process. Kylin will automatically extract the correct dimensions from the input. In this example, we just manually input the desired dimensions into the text box, separating each dimension with a comma, as shown below.

![include_dimensions.gif](assets/images/recognize-51ee445961fa0e44d5a4d8008153417b_4e4179649117e335.gif)

If you want to know the indexes generated by the aggregate group, you should navigate to the **Index Overview** page. This page gives you all the information of index, we will introduce them in the chapter of [model info](#model-manage-model_info).

![index_view.png](assets/images/index-view-9c1c7a73310652d20a65441f03456a03_0f1803370d9f963b.png)

On the **Aggregate Group** page, you’ll notice an icon (![settings_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgICAgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIKICAgICB2ZXJzaW9uPSIxLjEiCiAgICAgd2lkdGg9IjE2IgogICAgIGhlaWdodD0iMTYiPgogICAgPHBhdGggZD0iTTM1OS44OTMzMzMgMTMyLjIwMjY2N0E2NCA2NCAwIDAgMSA0MjEuNTQ2NjY3IDg1LjMzMzMzM2gxODAuOTA2NjY2YTY0IDY0IDAgMCAxIDYxLjY1MzMzNCA0Ni44NjkzMzRsMjEuODI0IDc4LjU0OTMzMyA3OC45MzMzMzMtMjAuMzk0NjY3YTY0IDY0IDAgMCAxIDcxLjQyNCAyOS45NzMzMzRsOTAuNDUzMzMzIDE1Ni42NzJhNjQgNjQgMCAwIDEtOS43NzA2NjYgNzYuODQyNjY2TDg1OS44ODI2NjcgNTEybDU3LjA4OCA1OC4xNTQ2NjdhNjQgNjQgMCAwIDEgOS43NzA2NjYgNzYuODQyNjY2bC05MC40NTMzMzMgMTU2LjY3MmE2NCA2NCAwIDAgMS03MS40MjQgMjkuOTczMzM0bC03OC45MzMzMzMtMjAuMzk0NjY3LTIxLjgwMjY2NyA3OC41NDkzMzNBNjQgNjQgMCAwIDEgNjAyLjQ1MzMzMyA5MzguNjY2NjY3aC0xODAuOTA2NjY2YTY0IDY0IDAgMCAxLTYxLjY1MzMzNC00Ni44NjkzMzRsLTIxLjgyNC03OC41MjgtNzguOTMzMzMzIDIwLjM3MzMzNEE2NCA2NCAwIDAgMSAxODcuNzMzMzMzIDgwMy42NjkzMzNsLTkwLjQ1MzMzMy0xNTYuNjcyYTY0IDY0IDAgMCAxIDkuNzQ5MzMzLTc2Ljg0MjY2NkwxNjQuMTM4NjY3IDUxMmwtNTcuMTA5MzM0LTU4LjE1NDY2N2E2NCA2NCAwIDAgMS05Ljc0OTMzMy03Ni44NDI2NjZsOTAuNDUzMzMzLTE1Ni42NzJhNjQgNjQgMCAwIDEgNzEuNDI0LTI5Ljk3MzMzNGw3OC45MTIgMjAuMzczMzM0IDIxLjgwMjY2Ny03OC41MDY2Njd6TTQzNy43NiAxNzAuNjY2NjY3bC0yMy4wODI2NjcgODMuMDkzMzMzYTY0IDY0IDAgMCAxLTc3LjY1MzMzMyA0NC44NDI2NjdsLTgzLjQ5ODY2Ny0yMS41NDY2NjctNzQuMjQgMTI4LjU3NiA2MC40MTYgNjEuNTI1MzMzYTY0IDY0IDAgMCAxIDAgODkuNjg1MzM0bC02MC40MTYgNjEuNTI1MzMzIDc0LjI0IDEyOC41OTczMzMgODMuNDk4NjY3LTIxLjU0NjY2NmE2NCA2NCAwIDAgMSA3Ny42NTMzMzMgNDQuODIxMzMzTDQzNy43NiA4NTMuMzMzMzMzaDE0OC40OGwyMy4wODI2NjctODMuMDkzMzMzYTY0IDY0IDAgMCAxIDc3LjY1MzMzMy00NC44NDI2NjdsODMuNTIgMjEuNTQ2NjY3IDc0LjI0LTEyOC41NzYtNjAuNDM3MzMzLTYxLjUyNTMzM2E2NCA2NCAwIDAgMSAwLTg5LjY4NTMzNGw2MC40MzczMzMtNjEuNTI1MzMzLTc0LjI0LTEyOC41OTczMzMtODMuNTIgMjEuNTY4YTY0IDY0IDAgMCAxLTc3LjY1MzMzMy00NC44NDI2NjdMNTg2LjI0IDE3MC42NjY2NjdoLTE0OC40OHpNNTEyIDQyNi42NjY2NjdhODUuMzMzMzMzIDg1LjMzMzMzMyAwIDEgMCAwIDE3MC42NjY2NjYgODUuMzMzMzMzIDg1LjMzMzMzMyAwIDAgMCAwLTE3MC42NjY2NjZ6IG0tMTcwLjY2NjY2NyA4NS4zMzMzMzNhMTcwLjY2NjY2NyAxNzAuNjY2NjY3IDAgMSAxIDM0MS4zMzMzMzQgMCAxNzAuNjY2NjY3IDE3MC42NjY2NjcgMCAwIDEtMzQxLjMzMzMzNCAweiIvPgo8L3N2Zz4K)). Clicking this icon will navigate you to the **Advanced Setting** page. Here, you can specify columns as **ShardBy** as needed.

The **ShardBy** column is typically one of the filter or grouping dimensions that are frequently used in queries. While you can designate more than one shard by dimensions, only the first one will be applied during queries. Therefore, it’s important to choose this column wisely, balancing factors such as column cardinality. Cardinality information is generated via [table sampling](#datasource-data_sampling).

This setting applies to all aggregate groups. If an aggregate group does not contain the specified shard by dimensions, the system will automatically bypass them when generating aggregate indexes.

![Advanced Settings](assets/images/advanced-settings-8f0616a51026a599efbba426c109b3a0_c0db070a72436854.gif)

Based on your business scenario, you can decide whether to add an index that includes the dimensions and measures defined across all aggregate groups. This index can support queries that span multiple aggregate groups but may not achieve the optimal query performance. Besides, incorporating this index comes with higher storage and building costs. How to set this configuration, please refer to the [configuration](https://kylin.apache.org/docs/model/manage/configuration) chapter.

```shell
# generating base cuboid of all aggregate groups, by default this is true
kylin.cube.aggrgroup.is-base-cuboid-always-valid=true 
```

Please note, this is different from the **Base Index**. The dimensions and measures in the aggregate groups may not cover everything in the model, and the base table index will not be generated in this context.

Now that we have completed the design of the aggregation group, we will delve deeper into the underlying principles in this section. Understanding these principles will help you optimize the performance and management of aggregation groups in Kylin, ensuring efficient query processing and resource utilization.

You can categorize the combinations of dimensions and measures into several groups, referred to as **Aggregate Groups**. For instance, as illustrated at the beginning of this chapter, if you only require the dimension combinations of *[A B M1]* and *[C D M2]*, the aggregate index group can be segmented into two distinct aggregate groups: *A B-M1* and *C D-M2*. This approach effectively reduces the total number of indexes from 15 to 7, optimizing storage and improving query performance.

![Aggregate Group](assets/images/agg-group-p1-b57e87da1c437e98a27164557dcc3ffd_8ed2a702f00ef43d.png)

The aggregate groups required by end users may contain overlapping dimensions. For instance, consider aggregate group ABC and aggregate group BCD, both of which include dimensions B and C. If these two aggregate groups share the same measures, they will generate identical indexes; for example, both aggregate group ABC and aggregate group BCD will derive the index BC. However, Kylin ensures that an index is not generated multiple times. If an index can be derived from more than one aggregate group, it will only be created once, as illustrated below.

![Derive same index](assets/images/agg-group-p2-2be1a1c05bad60951daf5d193a89fe40_d4dce767c422820a.png)

When you want to focus your analysis on one or more specific dimensions that must be included in every query, you can designate these dimensions as **Mandatory Dimensions**. This setting ensures that only indexes containing the mandatory dimension will be calculated and considered for queries.

For instance, if we take the aggregate index example from earlier in the chapter, where there were originally 15 possible indexes based on various combinations of dimensions, and we set dimension **A** as mandatory, the result would be a reduced set of indexes. In this case, only those indexes that include dimension **A** will be calculated, effectively limiting the combinations and simplifying the number of indexes from 15 to 8.
![Reduce dimension combinations with Mandatory Dimension](assets/images/mandatory-p1-9607bac4796edca8cd7902243bde1048_61573a0ccc3e63f0.png)

![Aggregate index group after reducing dimension combinations](assets/images/mandatory-p2-1cc152c9950a3035a47e61f1acb18346_1316382dba6e80e5.png)

End users typically utilize dimensions with hierarchical relationships, such as country, province, and city. In this context, a hierarchical relationship can be defined as a **Hierarchy Dimension**. From top to bottom, the hierarchy consists of a one-to-many relationship: country, province, and city. These three dimensions can be grouped into the following combinations:

1. Group by country.
2. Group by country and province (equivalent to grouping by province).
3. Group by country, province, and city (equivalent to grouping by country and city, or simply by city).

In the aggregate index group outlined below, let dimension A represent Country, dimension B represent Province, and dimension C represent City. Here, dimensions A, B, and C can be configured as a hierarchical dimension. Consequently, the following index relationships hold true:

- Index [A, C, D] is equivalent to index [A, B, C, D].
- Index [B, D] is equivalent to index [A, B, D].

Thus, indexes [A, C, D] and [B, D] can be pruned effectively.

![Hierarchy Dimension](assets/images/hierarchy-p1-5d0a190a9c4eea58249d5fda6e7e998a_eb4e94a3ab6a0c0a.png)

As the diagram below illustrates, based on the method above, Kylin can prune redundant index, hence reducing index from 15 to 7.

![Reduce dimension combinations with Hierachy Dimension](assets/images/hierarchy-p2-146842116088f64ec6148493437173f7_f03bf1b9d9b48eac.png)

Sometimes you don’t need details of all possible combination dimensions. For example, you might query dimension A, B, C together in most cases but not dimension A, C or dimension C alone. To enhance performance in this case, **Join Dimension** can be used. If A, B, and C are defined as Joint Dimension, Kylin will only build index ABC but not index AB, BC and A. Finally, indices will be built as below. The number of indices can then be reduced from 15 to 3.

![Joint Dimension](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQQAAAD9CAIAAADVgJ44AAAAAXNSR0IArs4c6QAAAAlwSFlzAAALEwAACxMBAJqcGAAAAdVpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IlhNUCBDb3JlIDUuNC4wIj4KICAgPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4KICAgICAgPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iPgogICAgICAgICA8dGlmZjpDb21wcmVzc2lvbj41PC90aWZmOkNvbXByZXNzaW9uPgogICAgICAgICA8dGlmZjpQaG90b21ldHJpY0ludGVycHJldGF0aW9uPjI8L3RpZmY6UGhvdG9tZXRyaWNJbnRlcnByZXRhdGlvbj4KICAgICAgICAgPHRpZmY6T3JpZW50YXRpb24+MTwvdGlmZjpPcmllbnRhdGlvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CrDjMt0AABrhSURBVHgB7Z13zBVFF8ZRqpRPimBAkSJNOgLSRRARkKJSDQQSRZCE0CQSmkgoEV9RSKRXBYFA6EoTBekgoQuiBJVegwgCKuj341u93G/fW/bunbtl9rx/wO7szJkzz9lnp95z7vv7778z6PX3yy+/NGnSZM+ePX/++adeLfNWa65cuZI7d25v6ZScNvcnV9yLpfPkyVO4cOGbN2/Cc/lLBQK3b99u06YNXxwvmj8Jne4DrCSKe7Hofffdh7UyZszoReV00enOnTsPPPDAH3/8oUuD7rZDTzLox3APvnN8dDTDWcNhkgffG1HJFwgIGXxhJlHSCQSEDE6gLHX4AgEhgy/MJEo6gYCQwQmUpQ5fICBk8IWZREknEBAyOIGy1OELBIQMvjCTKOkEAkIGJ1CWOnyBgJDBF2YSJZ1AQMjgBMpShy8QEDL4wkyipBMICBmcQFnq8AUCQgZfmEmUdAIBIYMTKEsdvkBAyOALM4mSTiAgZHACZanDFwgIGXxhJlHSCQSEDE6gLHX4AgEhgy/MJEo6gUAmJyqROuwigPuJI0eO4IeiSJEiWbNmtStGyllCQHoGSzC98847OIN48803LeXOkOHixYvkD/3df//9uXLlqlGjxvbt2y1KOHbs2NNPP50zZ87KlSuXLl26QIECQ4cOxQVO3OLPPPNMqF4qffLJJ7t27XrixIm4BSWDbt4+sCivgloXJkgrUaJEpkyZrl69eurUKS7ivjeQgdf3jTfeePHFF8n8119/nTlzZuzYsSdPnvzxxx8feuih2BLgDC66ypQpM3z48GrVqh09enTJkiUffPDBa6+9Nn369NhlIQO1k5lsN27coGOZO3fuTz/9tGjRohdeeCF22YSeKsc5odpTkhlLa/YHTGpbtGnTJgy/Y8cO/v3ss8+sCL9w4QJqjBs3Ljzztm3bSOSlDE+MeE0fwhf9t99+C3/avn17itNjhCemv65fv36dOnXC069fv04ng5dBLsLTk7xWjnOS+iRfXIZJ2DTO38cff1yvXj1e0Nq1a3MdJ3f0x8YgJ263sGHDhp07dw4aNCh79uzhwuhYBg8eTO8UnmjlOkeOHAzz6JRWrFhhJX9g8wgZ4pgen618y42vcrt27XifcLgbp0ykx4cOHXr33XcZbtWqVSvS83tpBw4c4KZp06b3kv539cgjj4wcOZIew5Ru5RYyM2/54YcfrGQObB4hQxzTL126lOEKfnbJx7949l6wYEGcMv8+fvvttwv+7w9fyBUqVNi6dStf/biLQgyE6D1M3cK/Im3+zzyHOQwzB5vlg1Es/lwwGDhEbSXjooYNG/ImkaNQoUJ169YlpUePHlELhD1gpM7IykjAUf6yZcsaNGiwePHiihUrhuUyXzL2/f33382pSd8jUzMP8klDYhYgZDAjEn5/+vTp9evXk5IlSxYjHe/TLA199913LPWE54x43ahRo969e4ce0VGUL19+4sSJkydPDiWmvyhevPi1a9eYGzz44IPhTyHJkCFDmB83btw4PN3KNVNnRnfMoa1kDmweIUMs07MomTlz5vHjx7OOZOSDDL169frkk09Gjx4dq2SkZ0xkq1SpsnHjxkgP76VBGG7oRrp06XIvNUOG77//nkorVaoUnmjxGmnktFfWYhU6ZEt+QcprErCKKpXKli378ssvm6SxA/Doo4/CClN6+G3EpVUGKkweGCmF50x/Tc8DH8qVK0fnEP60e/fubEWfP38+PDH9dfqlVYo8/vjj7Fekz5xMikKck1FDYVll741CnZIUpcpI33zzDaIY4pv0MVZX161bx1vLt5bvtykDtwYZ2HRb8+/fjBkzmG8gkI80GWKU5emqVauYZ9ONfP755+yg0Sf069eP3iktLc2oq3///lRNLcZt+L+QAQ4b1a5cuZLOhDl8/vz5mb6HZ0v+WhXOyWuiSoKQISqSPXv2ZNR+69YtUw4+2NmyZevYsSMvNC+EaYfLyGyQgaehP17uqlWrLly40MgQo6yRYffu3ZCB9VBDQt68eZlshLqj1q1bk86utkk3biFDqNL//Oc/bI8w3Y/bn6SXEzeFWuLm8VcG3doD+k4aiZV7Ri/2TG6lLBNfOiiWRCGPqRZm5+kTTXlSeuskziltSEi47DOEPqN2Lhi9cF7ITskMGayUZc7NWJ8jq6EZvFHXhx9+CBlMifbUkFIhBBSfaQvJdfGCVwSuO6PApUuX4h6viKaJW2Wj6ZNoupM4J6qbvfzOvTf29LNRSj8j2QDBgSL64SzDJAdeG6nCHwgIGfxhJ9HSAQSEDA6ALFX4AwEhgz/sJFo6gICQwQGQpQp/ICBk8IedREsHEBAyOACyVOEPBIQM/rCTaOkAAkIGB0CWKvyBgJDBH3YSLR1AQMjgAMhShT8QEDL4w06ipQMICBkcAFmq8AcCQgZ/2Em0dAABIYMDIEsV/kBAyOAPO4mWDiAgZHAAZKnCHwhoSAbcfuFFwh/w+1ZLLRHWkAx4WMFptpbW8gh3wLZDhw4eUUahGhq6l1y7di2O66zE11GIY6BE0ffyxbHnmt/LQGnYM+BrOuQJJ9UXeKsvVarU/PnzU11RbPn4zS9WrNivv/4aO5uqp4RdJJyKfj69NfSO4eS3p1u3bnhQTSacjyptcWUJM+fMmaNKYADlaNgzOGZFgg5++eWXEyZMcKzGGBXhVmzXrl30UTHyyKPYCEjPEBufqE8J+0lEKRwDV69ePWomZx/s37//2WefxUlr0aJFna1Zk9qkZ7BjSJyc4ngY/5DeYQLNwC83ERBfeeUVWUmzY9QMGYQMdnAjVCH+sd966y07hVNZpk+fPngOJ3p0KivRVrYMkxI2LUPz5s2b7927l/CbCRdOfQG8z1euXBnf90T4TH1tWtUgPUNi5iTaGvtNU6dO9SYTaMzDDz88c+ZMRnGEVEysbYHPLT1DYq9A586diSU1ZcqUxIo5npvAimfPnqV/cLxmH1coPUMCxps3bx5jpHHjxiVQxqWs77333pEjR2bNmuVS/b6sVnoGq2YjfA5xQ9hY8EvMzMOHDxOIevv27SVLlrTayGDnk57Bkv2No2mEYfYLE2gVYQ5HjBjBDOfPP/+01MjAZ5KewdIrQDxzBkirV68mQoelAp7J1LJlyyeeeGLMmDGe0ci7iggZ4ttm8+bN7dq127dvHws18XN7LMfly5crVKhAdPeGDRt6TDXPqSPDpDgmYYGSZUoWK/3IBNqWL18+mNCpUydYEaepgX8sPUOcV6Bt27ZsKfhiBSlGSwYMGMDi0ooVK2LkkUfSM8R6B+gQjh49qsGAe+TIkadPn540aVKs1gb+mfQMUV8BgpbXrFlzy5YtTECjZvLPA5pTq1atTZs2scrkH60d1VR6hshwsxzJD6lHjRqlBxNoJLsNaWlpNIpfI0Vuc+BTpWeI/ApwIpUB0vLlyyM/9m0qy2IFCxYcP368b1uQQsWFDBHAZZuZM0gHDhxgKSbCYz8nsThWsWJFzlY1bdrUz+1Iie5CBjOsly5dYpuZHxPrujDv620Ts7WU3gsZzHC2aNGiXLly/HzH/ECje/9uqKfUCDKB/j94J06cyMlnjvT8X6p2N8OGDWO8JDMHk2GlZ8hw8uTJwoULg8u3335bv379HTt2lChRwgSTfremQ7jsQnj250rOga/KsZRP5WzYsAGsp02bduvWLUZH/ADApw2xoTY/z8AD2o0bN2bPng0I69atsyFEpyJB7xlat26N+6Ps2bMXKFCAnw7jms6575AHauKANz3hxYsXoUSzZs3wfOMBpVxTIehkwJcEXhmBP0uWLLly5YIMderUwfOFawZxqmK+6NCgVatWNN/YhuOLcP36dd+dUVcImP5WjwHWwYMHQy6G8B/KuU5+GsboOUYRbR7hNrh27dr0CaEN6YwZM+7Zs0ebBtpoSKDJwCg5RAawy5EjB2PonDlz2sDRd0XoCTlpQpNDmsOKNWvWhG4DeBFoMixevJh5M1ZnbJAtW7ZBgwZxzhl39kF4D+D8oUOH2HDA2YcxLKRvZPoUhLZHa2Nw5wzYnheCA3l8HYsUKQIxypQpEw0mjdM5zcoqwvHjx3HiTeCFq1evQg+N2xujacHtGTibzSgZww8cOJBjSMFkAm8Gp1n5RevQoUOBAkC+/vrrGK+L3o80jNxj0WCsnDBGwp+KNoe0LTY8fTaGSfwU7qWXXmrcuLGxtpY+TxBSgjtMwpM2y4t8C4NgZottBBNWFBgsWcyvWzZeCFbZatSoEVwInDIpONvYrxXrOGMfcL7bM7CW0qZNmwULFshnMkW4Gz7IOATFPleiVYh1EkUs0fwh6/xDhtu3bwsTEgUxofwgzgyVJayESpEZMoh1EgUt0fyGdf4hA/1DouUlf6II8FrbwNleqUR1k/zgHNylVTG/IGBCQMhgAkRug4uAkCG4tpeWmxAQMpgAkdvgIiBkCK7tpeUmBIQMJkDkNrgICBmCa3tpuQkBIYMJELkNLgJChuDaXlpuQkDIYAJEboOLgJAhuLaXlpsQEDKYAJHb4CIgZAiu7aXlJgSEDCZA5Da4CAgZgmt7abkJASGDCRC5DS4CQobg2l5abkJAyGACRG6Di4CQIbi2l5abEBAymACR2+AiECyPejinwLUwXipwrpo1a9bgml1aHgkBd3oGoqfhjKBo0aIWvUUQRoD8oT/cIRJYBMdn27dvj9SoCGnHjh0j9gKehgnPU7p0aeL04F0UFywRskpS4ghMmDAhZB280eG/tXnz5nj8T1ySmyXcIcMnn3wCXidOnNi4caP11r/xxhsEEOCPaEvjxo27du0avkEJ2xxXApypWrUq8QdWrFgBr3A53LVr15EjRyIwblnJYB2BTz/9FOssX768d+/eUOL555/v0aOH9eLu5zS+zfzr2B/f40KFChF3lcgxnTt3tlLvhQsXQAoChGfetm0biYsWLQpPjHhNH/Lkk0/icj38afv27SlOjxGemNJrqrMh314pGxUlU+Sjjz5CzzNnzoQLMWJpr1+/PjzRs9fo70LPADrnzp1r27Ztu3btiIqAN2z0sPFnDHIeeuih2GWJ57lz504CkRCzLDzn2LFjBw8eTDiC8ES5VohA3759+eoZPFEoNnWiXCDDxx9/zPC9YMGC8IEgk/DBRvOIOsOHh4DNtWrVil2c2AtkaNq0qSkbYY8ZKdFjmNLlVhUCRMrCOvS9qgSmWo7TZMD9/7Jly4i4SsP4bNStWxduWGwkMZegEH9EmqpQocLWrVv56sddFMIY9B6mbsFijZItSQQwMdHXkxTiWHGnl1YXLlxI5CjiJhktZKTUq1evn3/+mbXOuG2mP2GaYWT75ZdfIFWDBg3oWCpWrBijLIPUUEDLGNnkUSoQAHmCC6dCcipkOk0G1pGMCbTRGGM6RSILnXGb16hRI5YpQtnoKMqXLz9x4sTJkyeHEtNfFC9enHUn5gYmq1D1kCFD6tevz5JU+lKSogQBFgwfe+wxJaIcEOIoGYiit3nz5p49ezLICbVt2rRpFskQKmJcEJiwSpUqcRdnIQz56Ua6dOkSLuH7778fPXp0pUqVwhPlWiEChP8gQpwJdoXy1YviA4lQ4wud6n+HDRvG7i/f6fCKZsyYgQKs/Ycnmq4jLq3SBTN5YKRkymy6JTQTfChXrhydQ/ij7t27o8z58+fDE1N6bQ9ne6VS2pD0wiMurb766qsE/SCaaPr8HkwB57s0cAZuXspixYoxdTYBwfeDZYfXX3+d9P79+/Op5tU35THIENp0Y2cHCjH5RnM++WRGOAX5CJkKGrerVq1ink03wm4dm270Cf369WPHNC0tLWL+FCXaw9leqRQ1IZpYgwzGptvq1aunT59er149DgqMGDEiWhGvpYOzc2QwYqquXLkyPQqtWrViQH/z5k1jYm3auyG/QYa76v77x8vNpjLTcUMaZOBJnTp10gs3Unbv3g0ZjOjf5MybNy+TDeK1RMufinTqtSHWXikbFSVTJHwzgb1nAqhiyk2bNiUj0+Gy4Oy5yD3PPfccZ1r4bKNcQn8sob7//vuxJ9NsQnNQL3/+/MzqbFSRkD7pM1MjBk6fHjvFXqnYMuVpegTA2dEJdHoNTCkffvghS0b2XlNGPnGXpJhzV6tWzVSp3AoCBgLe6hk4dRf3eEU0yyVTNppMten2vvH2SqnVPAjSwNlbZNAbdHuvtb1SeiOZitaBs9PHMVLRDJEpCChBQMigBEYRogMCQgYdrChtUIKAkEEJjCJEBwSEDDpYUdqgBAEhgxIYRYgOCAgZdLCitEEJAkIGJTCKEB0QEDLoYEVpgxIEhAxKYBQhOiAgZNDBitIGJQgIGZTAKEJ0QEDIoIMVpQ1KEBAyKIFRhOiAgJBBBytKG5QgIGRQAqMI0QEBIYMOVpQ2KEHgLhlwZ4CfCCXiREg0BGwjLNaJBqnCdMM6d8mADxWCFdi2lkKddBUFtoavZRsNFOvYAC2hIvesg/MS3HglVFgyJ4oAX/ennnoKnG34AhLrJIp2ovlD1rHj1sqGRb1WZOnSpbj3wz++1xRzVx/8SpUqVWr+/PnuquFW7XbcWiXKPG/mx1kltp8zZ4431XNFq27duuHB1nrEDFeUTF2lwV1NwmHZrl27+AqmDlx/SV6yZMmXX35J3E5/qa1Q2+D2DIC4f//+Z599FjesBOFViKkfRZ06dYqIXjhmrl69uh/1V6JzcHsG4MNxNzEOX3nllYCvpOG2uWPHjvjnDDITeB8CTQba36dPHxyADx8+XMmnxadCCBWJf/K33nrLp/qrUjvQwyQDROKVVK5cGe/2hBRQBauP5DBxat68+d69ewl/6iO1U6Fq0HsGMH344YdnzpzJOIGgiamA2MsyiaLEbuDUqVOFCZhJeoZ/3lVCJ549e5b+wcvvrnLdOnfuTCyvKVOmKJfsR4HSM/xjtffee484JrNmzfKjFe3pPG/ePMZI48aNs1dcv1LSM9yz6eHDhwk1vX379pIlS95L1fSKWOXEbWFjQeKdhiwsPUMIigxly5YlIB9jaMK230vV8co4mkYYbGFCuHmlZwhH4+51y5Ytic83ZswY8wON7oknzwCJsJxE6NCoWck2RchgRvDy5cvEbJ87d27Dhg3Nz7S4Jy59u3bt9u3bxzKaFg1S1ggZJpmhzJcvH0zo1KkTrDA/8/89y8csIrOULExIb0zpGdJjcjdlwIABLC6tWLEi8mPfprZt25YtBVlBimhA6RkiwpJh5MiRp0+fnjRpUuTH/kylQzh69Kje06FkLCM9Q1T0fvjhh1q1ahHmnlWmqJn884Dm1KxZc8uWLSwP+EdrRzWVniEq3Ow2pKWl8etwfu8SNZNPHrBYTENGjRolTIhhMekZYoBz9xELLwULFhw/fnycfN5+zIlUBkjLly/3tpouaydkiGMAll8qVqzI6Z2mTZvGyerVx2wzcwbpwIEDLJR5VUdP6CVkiG8GXy/MX7p0iW1mfuqt67ZJfPtZziFksASVf7dsW7RoUa5cOX6+Y6mdwc4kE2hL9h82bBjjJd/NHCZOnMi5dA5cWWpk4DNJz2D1FTAd82QXwps/iDl58mThwoVp1bffflu/fv0dO3aUKFHCaiMDns8th01+rJcfAOBj68aNG7Nnz+a1WbdunddasWHDBhSbNm3arVu3GB3x8wyvaehlfaRnSOxjyAFvvrUXL16EEs2aNcO3SmLlU5y7devWuD/Knj17gQIF+GE3jgNTXKFW4oUMVs3JJw0atGrVCqeUxjYc79z169c9dQoaTx+oR5OyZMmSK1cuyFCnTh08X1htZLDzCUxW7Y8D4Nq1a9MnhDakM2bMuGfPHqvlU5/v4MGDIQdQf/zxB6du+eEec5vU16xJDUIGq4bkW8tZhhw5coQKwIo1a9aEbl2/YA4TIgPKoCoznJw5c7qumF8UEDJYtRRv1aFDh9hwwJ2EMfDg68sA3Wr51OdbvHgx82bqYeSWLVu2QYMGcQo9T548qa9ZkxpkzpCwITn+yTz1+PHjOPHGtf/Vq1ehR8JSVBeAmdCVA3l0CEWKFIEYZcqUUV2J5vKkZ0jYwJxm5TeTQ4cOhQNMG77++uuERaSgAGezUQaVBg4cyDEkYYINjDPZKCNFGCbxU7iXXnqpcePGxuqN65iwrsUYCW83ckjbti1kmGQbursF8V/NnJXBUlJSVBRGExZ/6RxUCAuoDA17Bg4RNWnShEVP7d0fufvOstacO3dud3VQW7uGcwbWTzicc/PmTS/v/Ptat9u3b7dp04Yvjtp30XVpGg6TWFjEWjJgSOm7xeCQyTpLWCmtxWHhepKB767DOAawOj46muGs4TApgO+lNFkJAkIGJTCKEB0QEDLoYEVpgxIEhAxKYBQhOiAgZNDBitIGJQgIGZTAKEJ0QEDIoIMVpQ1KEBAyKIFRhOiAgJBBBytKG5QgIGRQAqMI0QEBIYMOVpQ2KEFAyKAERhGiAwJCBh2sKG1QgoCQQQmMIkQHBIQMOlhR2qAEASGDEhhFiA4ICBl0sKK0QQkCQgYlMIoQHRAQMuhgRWmDEgSEDEpgFCE6ICBk0MGK0gYlCAgZlMCYlJAuXbrs3LkzKRFSWAUCQgYVKNqVQWw4HBifO3fuq6++at++PZFQ7EqScgoQEDIoANG2iLZt2+I+/osvvli0aFHfvn3z589vW5QUTB4BIUPyGNqXQCyFo0ePDh48GBGEYLMvSEqqQEBDx8MqYHFORtmyZTt16vTiiy+Km2TnQI9Sk24eAmmmfm4Po9jO5WT9cJZhksuvlFTvHQSEDN6xhWjiMgJCBpcNINV7BwEhg3dsIZq4jICQwWUDSPXeQUDI4B1biCYuIyBkcNkAUr13EBAyeMcWoonLCAgZXDaAVO8dBIQM3rGFaOIyAkIGlw0g1XsHASGDd2whmriMgJDBZQNI9d5BQMjgHVuIJi4jIGRw2QBSvXcQEDJ4xxaiicsICBlcNoBU7x0EhAzesYVo4jICQgaXDSDVewcBIYN3bCGauIyAkMFlA0j13kFAyOAdW4gmLiMgZHDZAFK9dxAQMnjHFqKJywgIGVw2gFTvHQSEDN6xhWjiMgJCBpcNINV7BwENyZA5c+Y7d+54B2ItNdESYQ3JUKVKFQJ/aGktj/AKbDt06OARZRSqoaFL+rVr1+bJkydTJg2bptDwyYii7+WLc+XKlWSEeLDsfwF+Kvm/W2/x9QAAAABJRU5ErkJggg==)

\*\*Dimensional cardinality product \*\*

The *Dimensional Cardinality Product* refers to the product of the cardinalities of each dimension field within a joint dimension. This cardinality data is derived from the sampling results of the source data table. The dimensional cardinality product represents the maximum number of possible permutations and combinations of dimensions in the joint index (i.e., the maximum number of records for that index).

Although the dimensional cardinality product does not directly participate in the index creation process, it serves as a useful reference when defining the union dimension of an aggregate group. To ensure optimal query performance, it is generally recommended that the dimensional cardinality product of a union dimension does not exceed 100,000. In special cases, where dimensions in the union dimension must always be queried together, this value can be less of a concern.

In some cases, subqueries within a join may match two indexes. When this happens, Kylin retrieves data from both indexes and performs the join operation. However, if the cardinality of the subquery is high, the join operation may become time-consuming. To optimize this, users can set the *ShardBy* column to the join key.

```shell
kylin.storage.columnar.expose-sharding-trait=true 
```

This feature is enabled by default, Kylin will expose the sharding information to Spark. Normally, joining two large datasets in Spark requires a data shuffle beforehand to achieve hash partitioning. However, if the *ShardBy* column has already partitioned the data, the shuffle stage can be skipped, significantly speeding up the join operation.

> [!NOTE]
> **Limitations**
> Since there can only be one **ShardBy** column for a model, the optimization applies exclusively to joins that involve this single **ShardBy** column. For joins on other columns, the optimization will not take effect, and a data shuffle will still be required in Spark. Therefore, it’s important to choose the **ShardBy** column carefully, particularly when frequent joins occur on that specific column.

The use of aggregate groups helps prevent index explosion, but achieving optimal index performance requires a solid understanding of the data model, which can be challenging for junior modelers.

This section introduces a simple index pruning tool called **Max Dimension Combination (MDC)**. The MDC specifies the maximum number of dimensions allowed in a single index, preventing the creation of indexes with excessive dimensions during the index-building process. The MDC is especially useful when most queries interact with no more than N dimensions, where N is the configurable MDC threshold. This helps streamline index creation and improve query performance by focusing on the most relevant dimensions.

The following graph illustrates a scenario with 7 dimensions, with some details hidden for clarity:

- When the MDC is set to 4, indexes with more than 4 dimensions, such as *ABCDEF*, *ABCDEG*, *ABCDE*, and *ABCDF*, will be pruned.
- When the MDC is set to 3, indexes like *ABCDEF*, *ABCDEG*, *ABCD*, and *ABCE* will be excluded.

![sprouting graph](assets/images/mdc-p1-2cd817f56dbf874b59d54db2a0896cc6_cfe1b52e84b4f6ea.png)

To optimize index building, creating an index that includes dimensions and measures from all aggregate groups ensures it won't be pruned. Remember that joint dimensions and hierarchy dimensions are counted as a single dimension, while mandatory dimensions are ignored. When using the **Max Dimension Combination (MDC)** tool, consider the actual number of dimensions in the index, especially with joint or hierarchy dimensions, to ensure effective pruning aligned with query performance.

The MDC dimension pruning tool significantly reduces the number of indexes and storage size. However, complex queries that involve more dimensions may encounter larger indexes, which can slow down query responses due to online calculations. Like other optimization tools, this involves a trade-off. If most of your queries touch fewer dimensions, using MDC is beneficial.

Laboratory tests have shown that when the number of dimensions in the aggregate group is large, checking the index count can take several minutes, potentially causing web UI lags. Here are some test results for reference:

- **1 aggregate group with 1000 dimensions**: MDC set to 1, average check time is **3.1 minutes**.
- **1 aggregate group with 1500 dimensions**: MDC set to 1, average check time is **13.9 minutes**.
- **3 aggregate groups with 500 dimensions each**: MDC set to 1, average check time is **3 minutes**.

Please consider these results as general guidance and assess based on your specific scenario.

Next, let’s discuss how to count the number of dimensions in a query. This count refers to the dimensions represented in the corresponding index.

- For ordinary dimensions, each counts as one dimension.
- A group of joint dimensions or hierarchy dimensions is treated as a single dimension.
- Mandatory dimensions are ignored.

For example, in the following SQL query:

```sql
SELECT  
    COUNT(*)  
FROM  
    table  
GROUP BY  
    column_mandatory,  
    column_joint1,  
    column_joint2,  
    column_hierarchy1,  
    column_hierarchy2,  
    column_normal; 
```

We can analyze the dimensions as follows:

- **1** mandatory dimension.
- **2** dimensions from a single joint dimension.
- **2** dimensions from a single hierarchy dimension.
- **1** normal dimension.

Thus, for index pruning, this query is considered to involve **three dimensions**. This counting method helps ensure that the index pruning mechanism effectively limits the number of dimensions in the created indexes.

In this chapter, we covered how to create aggregate groups and the principles behind them. However, designing effective indexes seems quite complex, especially for beginners. If you're looking for a simpler approach, please refer to the [recommendation](#model-rec-intro) for more details.

---

<a id="model-manual-table_index"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manual/table_index/ -->

<!-- page_index: 31 -->

# Table Index

Version: 5.0.2

In the previous chapter, we discussed how to create an Aggregate Group. Now, we'll focus on its counterpart, the Table Index. A Table Index looks like a table in a data source, but unlike standard tables, it is derived from a flat-table resulting from a join operation. The columns used in a Table Index are from dimensions and measures already defined in the model.

- **Advantages**: Eliminates the overhead of joining tables at query time, resulting in faster query performance.
- **Disadvantages**: When the join relationship is one-to-many, the amount of data can increase significantly. To solve this issue, please refer to the [runtime join](#model-features-runtime_join) chapter for more details.

Now, let's introduce how to create a Table Index. The following GIF demonstrates how to navigate to the **Table Index** page.

![to_tableindex_page.gif](assets/images/to-tableindex-page-7cc8d1b381eac41340ba8d05f79bb5e3_4b7493ecfb397963.gif)

Click the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICAgIDxwYXRoIGQ9Ik0xIDFoMTR2MTRIMXoiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8cGF0aCBkPSJNOCA0djhNNCA4aDgiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgo=) button on the Table Index page to open a new window titled **Add Table Index**. This window allows you to create a table index by selecting the columns to include or searching the columns quickly. The available name of columns, along with their types, are displayed on this page.

![Add Table Index](assets/images/add-table-index-1e471e86101a5f7c9fe72e7e9fedc875_18bac5562b979ef8.png)

After selecting the columns, you can set the shardBy columns and adjust the column order. Choosing an appropriate ShardBy column can distribute raw data into multiple shards, which helps increase concurrency and improve query performance. It's recommended to select columns with relatively large cardinality as the shardBy column to avoid uneven data distribution. Similar to aggregate groups, only one shardBy column will be utilized during queries, and this is optional for the table index too.

You should also arrange the columns in the order of their frequency as filter conditions, as this arrangement can significantly impact query performance.

Currently, you can only add one table index at a time. If you wish to add another, click the ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICAgIDxwYXRoIGQ9Ik0xIDFoMTR2MTRIMXoiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8cGF0aCBkPSJNOCA0djhNNCA4aDgiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgo=) button on the Table Index page and repeat the steps above. Please note that having more table indexes will increase job building and storage costs.

After creating the table index, you can return to the **Table Index** page to view the indexes you just added. In this example, we successfully added two as follows.

- [*LO\_ORDERDATE*, *LO\_SUPPKEY*, *LO\_QUANTITY*, *LO\_EXTENDEDPRICE*], *LO\_ORDERDATE* as shardBy column
- [*D\_DATE*, *LO\_ORDERDATE*, *LO\_CUSTKEY*, *D\_MONTH*, *D\_YEAR*, *LO\_EXTENDEDPRICE*]

![View Table Index](assets/images/table-index-list-812b9b6a72802a97b32f41d279f03cd8_3a5c22ef38f24e51.png)

If you want to know the indexes generated by the aggregate group, you should navigate to the **Index Overview** page. This page gives you all the information of index, we will introduce them in the chapter of [model info](http://localhost:3000/latest/docs/model/manage/model_info).

![index_overview.png](assets/images/index-overview-348555eff761d4a84cd2a9151cb04d8b_8fa3b2cbd8927a3c.png)

In this chapter, we covered how to create table index. However, designing effective indexes seems quite complex, especially for beginners. If you're looking for a simpler approach, please refer to the [recommendation](#model-rec-intro) for more details.

---

<a id="model-manual-computed_column"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manual/computed_column/ -->

<!-- page_index: 32 -->

# Computed Column

Version: 5.0.2

A **Computed Column** allows you to define actions such as data transformation and calculations directly within your models. This feature enhances data semantic abstraction tailored to various business scenarios. By shifting runtime calculations to offline index construction, Kylin effectively leverages its pre-calculation capabilities, resulting in significantly improved query performance. Additionally, computed columns support Hive UDFs, enabling the reuse of existing business logic and code.

- **Naming Convention**: Computed column names may only include letters, digits, and underscores. Names cannot consist solely of digits or start with an underscore.
- **Expression**: This refers to the logic used for calculations. The expression for a computed column can incorporate columns from both the fact table and a lookup table within the current model.
- **Reuse and Reference**:

  - Computed columns are tied to a specific model and fact table, meaning one expression cannot create multiple computed columns across different models with varying names.
  - Strictly speaking, computed columns cannot be reused across models in the same project. To reuse a computed column in another model, you must define a new computed column with the same name and expression.
  - Nested computed columns are supported, allowing you to utilize existing computed columns to create new ones.
  - A single expression cannot generate multiple computed columns across different models that share the same fact table. For example, if you have two models, *model1* and *model2*, both using the fact table *LINEORDER*, and you wish to use the expression *LINEORDER.PRICE \* LINEORDER.QUANTITY* to create computed columns in both models, the system will require you to use the same name, such as *T\_PRICE*. Additionally, the name *T\_PRICE* cannot be used for any other expressions within these models.


> [!TIP]
> **Tips**
> - Computed columns can only be defined on the fact table. Once created, only the column expression can be modified.
> - Avoid naming conflicts with other columns to prevent unexpected errors.
> - Aggregate functions such as *SUM*, *MIN*, *MAX*, etc., are not permitted in computed column expressions.
> - Creating a computed column with an expression that consists solely of constants is not recommended, such as *POWER(CAST(2 AS DOUBLE), 2)*.
> - Avoid using keywords in computed column expressions. Refer to the [SQL Specification](#query-specification-sql_spec) for a list of keywords.
> - If an expression references identifiers that start with non-letter characters or include special characters, enclose the name in double quotes. For example: *"KYLIN\_SALES"."100\_PRICE" \* "1\_KYLIN\_SALES"."ITEM\_COUNT"*.

To help you master the creation of a computed column, we will demonstrate an example scenario below. Assume you have a fact table named *P\_LINEORDER* with the following columns:

- *LO\_EXTENDEDPRICE*: Transaction price
- *LO\_QUANTITY*: Transaction quantity
- *LO\_ORDERDATE*: Transaction date

We want to define two computed columns on this fact table: *T\_PRICE\_PER\_ITEM* to calculate the total transaction price for each item, and *YEAR\_OF\_ORDER* to indicate the year of the order. The corresponding expressions are as follows:

- *T\_PRICE\_PER\_ITEM* ::= *P\_LINEORDER.LO\_EXTENDEDPRICE \* P\_LINEORDER.LO\_QUANTITY*
- *NEXT\_ORDER\_DAY* ::= *P\_LINEORDER.LO\_ORDERDATE + 1*

**Step 1**: Click the button ![add_cc_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCIgdmlld0JveD0iMCAwIDEwMCAxMDAiPgogICAgPGNpcmNsZSBjeD0iNTAiIGN5PSI1MCIgcj0iNDUiIGZpbGw9ImdyYXkiIC8+CiAgICA8dGV4dCB4PSI1MCUiIHk9IjUwJSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZHk9Ii4zNWVtIiBmb250LWZhbWlseT0iQXJpYWwiIGZvbnQtc2l6ZT0iNDAiIGZpbGw9IndoaXRlIj5DQzwvdGV4dD4KPC9zdmc+Cg==) marked in the picture. A window for **Computed Column** will pop up.

![Add a computed column](assets/images/where-is-cc-fd2e0deeaa0e255768a45387981f088e_3450539a2e6c899c.png)

**Step 2**: Click the button ![rect_add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICAgIDxwYXRoIGQ9Ik0xIDFoMTR2MTRIMXoiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8cGF0aCBkPSJNOCA0djhNNCA4aDgiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgo=) in this window, and a dialog box titled **Add Computed Column** will appear. Please fill in the following information:

- *Column name*: Defines the name of the computed column.
- *Expression*: Specifies the calculation logic for the column.

![Define a computed column](assets/images/add-cc-page-dd1b6f57c0fb7059cdd091d39642a815_79d34501232d4764.png)

**Step 3**: Click the **Submit** button. The system will verify the legality of the name and expression of the computed column. If any issues arise, the system will provide feedback, allowing you to correct it and resubmit. Once the computed column is created, it will be visible in the fact table. For example, *T\_PRICE\_PER\_ITEM* will appear in the fact table *P\_LINEORDER*.

![Display a computed column](assets/images/cc-on-table-b64fb190f8080469c40f0c8e09c53e46_74fed6c46e18c31d.png)

**Step 4**: After creating the computed column, click the button ![add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIj4KICAgIDxwYXRoIGQ9Ik03ODkuMzMzMzMzIDEwNi42NjY2NjdhMTE3LjMzMzMzMyAxMTcuMzMzMzMzIDAgMCAxIDExNy4yNDggMTEyLjYxODY2NmwwLjA4NTMzNCA0LjcxNDY2N3Y0MDUuMzMzMzMzYTExNy4zMzMzMzMgMTE3LjMzMzMzMyAwIDAgMS0xMTIuNjE4NjY3IDExNy4yNDhMNzg5LjMzMzMzMyA3NDYuNjY2NjY3aC0xMC42NjY2NjZ2NDIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEtODUuMzMzMzM0IDg1LjMzMzMzNGgtNDY5LjMzMzMzM2E4NS4zMzMzMzMgODUuMzMzMzMzIDAgMCAxLTg1LjMzMzMzMy04NS4zMzMzMzRWMzIwYTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzMzLTg1LjMzMzMzM2g0Mi42NjY2Njd2LTEwLjY2NjY2N2ExMTcuMzMzMzMzIDExNy4zMzMzMzMgMCAwIDEgMTEyLjYxODY2Ni0xMTcuMjQ4TDM4NCAxMDYuNjY2NjY3aDQwNS4zMzMzMzN6IG0tOTYgMTkyaC00NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMjEuMTg0IDE4LjgzNzMzM0wyMDIuNjY2NjY3IDMyMHY0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMTguODM3MzMzIDIxLjE4NEwyMjQgODEwLjY2NjY2N2g0NjkuMzMzMzMzYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAgMjEuMTg0LTE4LjgzNzMzNEw3MTQuNjY2NjY3IDc4OS4zMzMzMzNWMzIwYTIxLjMzMzMzMyAyMS4zMzMzMzMgMCAwIDAtMTguODM3MzM0LTIxLjE4NEw2OTMuMzMzMzMzIDI5OC42NjY2Njd6IG0tMjM0LjY2NjY2NiA5NmEzMiAzMiAwIDAgMSAzMS44NTA2NjYgMjguOTI4TDQ5MC42NjY2NjcgNDI2LjY2NjY2N3Y5Nmg5NmEzMiAzMiAwIDAgMSAzLjA3MiA2My44NTA2NjZsLTMuMDcyIDAuMTQ5MzM0SDQ5MC42NjY2NjdWNjgyLjY2NjY2N2EzMiAzMiAwIDAgMS02My44NTA2NjcgMy4wNzJMNDI2LjY2NjY2NyA2ODIuNjY2NjY3di05NmgtOTZhMzIgMzIgMCAwIDEtMy4wNzItNjMuODUwNjY3bDMuMDcyLTAuMTQ5MzMzSDQyNi42NjY2NjdWNDI2LjY2NjY2N2EzMiAzMiAwIDAgMSAzMi0zMnpNNzg5LjMzMzMzMyAxNzAuNjY2NjY3SDM4NGE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwLTUzLjIyNjY2NyA0OS44MzQ2NjZsLTAuMTA2NjY2IDMuNDk4NjY3djEwLjY2NjY2N2gzNjIuNjY2NjY2YTg1LjMzMzMzMyA4NS4zMzMzMzMgMCAwIDEgODUuMzMzMzM0IDg1LjMzMzMzM3YzNjIuNjY2NjY3aDEwLjY2NjY2NmE1My4zMzMzMzMgNTMuMzMzMzMzIDAgMCAwIDUzLjIyNjY2Ny00OS44MzQ2NjdsMC4xMDY2NjctMy40OTg2Njd2LTQwNS4zMzMzMzNhNTMuMzMzMzMzIDUzLjMzMzMzMyAwIDAgMC00OS44MzQ2NjctNTMuMjI2NjY3TDc4OS4zMzMzMzMgMTcwLjY2NjY2N3oiCiAgICAgICAgICBmaWxsPSIjNDA0MzRFIj48L3BhdGg+Cjwvc3ZnPgo=) in the **Dimension** window to add a new dimension based on the computed column *NEXT\_ORDER\_DAY*, as shown below:

![Add a dimension relies on computed column](assets/images/add-dim-of-cc-228c10039a88006beb38ffc87aa90b94_29dd25a632ed519e.png)

Additionally, click the button ![rect_add_icon.svg](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgaGVpZ2h0PSIxNiIgdmlld0JveD0iMCAwIDE2IDE2Ij4KICAgIDxwYXRoIGQ9Ik0xIDFoMTR2MTRIMXoiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+CiAgICA8cGF0aCBkPSJNOCA0djhNNCA4aDgiIHN0cm9rZT0iZ3JheSIgZmlsbD0ibm9uZSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjwvc3ZnPgo=) in the **Measure** window to add a new measure, *TOTAL\_PRICE*, based on the computed column *T\_PRICE\_PER\_ITEM*, as illustrated below:

![Add a measure relies on computed column](assets/images/add-measure-of-cc-3cdfb383a83e3a7b698935fb3dd3069f_d81e3df07573fb2a.png)

In certain situations, it may be necessary to change the expression to adapt to evolving business requirements. You can modify the expressions of computed columns directly by editing the model.

![edit computed column](assets/images/cc-editing-5ca8e9c1bca88d885166adce262e3daa_df37b586fd0f3172.gif)

> [!NOTE]
> **Warning**
> However, there are a few limitations and considerations to keep in mind. Please review the following limitations carefully before using them:
>
> - Modifying the name of a computed column is not supported.
> - Modifying nested computed columns is not allowed. If a computed column has been utilized as a nested computed column, attempting to modify its expression will result in a failure, accompanied by the message: *model [model\_name] nested computed column [column\_name] still contains computed column [column\_name]*.
> - Changes may require rebuilding **related indexes** under the model, prompting a message for user confirmation.
> - Changes may cause measures to become invalid, necessitating the deletion of related measures, aggregation groups, and layouts, which will also trigger a message for user confirmation.

Now that we have defined two computed columns in our model and created a new dimension and a new measure, we can leverage the pre-calculation capabilities of indexes. You can use computed columns in either an aggregate index or a table index. Let's walk through an example.

![Use computed column](assets/images/cc-for-index-283e717fb8ad456be1bf6850d5d855c4_3d62942bf263431b.gif)

After a successful submission, we have completed the basic usage of computed columns, including:

- Creating a computed column.
- Creating dimensions and measures based on computed columns.
- Defining computed columns in the index.

A computed column is logically appended to the table's column list after creation. You can query the computed column as if it were a normal column, provided it is pre-calculated in an index.

To improve query performance with computed columns, ensure that you define them when creating an index.

1. **Query Pushdown**

   If a computed column is not used as a dimension or defined in indices, query performance will not be enhanced. However, if **QUERY PUSHDOWN** is enabled, users can still utilize this computed column. In this scenario, Kylin will analyze and translate the query into a SQL statement that the calculation engine can process.

   For example, if a computed column named *T\_PRICE\_PER\_ITEM* is defined with the expression *LO\_EXTENDEDPRICE \* LO\_QUANTITY*, executing the following SQL:


```sql
SELECT SUM(T_PRICE_PER_ITEM) FROM SSB.P_LINEORDER 
```

   will be translated to:


```sql
SELECT SUM(LO_EXTENDEDPRICE * LO_QUANTITY) FROM SSB.P_LINEORDER 
```

   This query will then be pushed down to the calculation engine.


> [!TIP]
> **Tips**
> If you wish to query the computed column, you must supply the complete join relations defined in the model that contains the computed column in your SQL.

2. **Explicit Query**

   If the name of a computed column appears as a field or a parameter of functions in a SQL statement, this is termed an **Explicit Query**. For example:


```sql
SELECT SUM(T_PRICE_PER_ITEM) FROM SSB.P_LINEORDER 
```

3. **Implicit Query:**

   If the expression of a computed column appears as a field or a parameter of functions in a SQL statement, this is termed an **Implicit Query**. For example:


```sql
SELECT SUM(LO_EXTENDEDPRICE * LO_QUANTITY) FROM SSB.P_LINEORDER 
```

   In Kylin 4.x, the expression *LO\_EXTENDEDPRICE \* LO\_QUANTITY* will be converted to *T\_PRICE\_PER\_ITEM*. Consequently, the original query will be translated to:


```sql
SELECT SUM(T_PRICE_PER_ITEM) FROM SSB.P_LINEORDER 
```

   If the measure *SUM(T\_PRICE\_PER\_ITEM)* has been pre-calculated in an Aggregate Index, query performance will be greatly enhanced.

Computed columns can reference other computed columns as part of their expression, allowing for flexibility in data transformations. This means you can build complex calculations on top of existing ones. However, keep in mind the limitations regarding nested computed columns when modifying them, as detailed in the modification section.

![nested_cc.png](assets/images/nested-cc-779a429fd4f25f732a3de0cfc69bccaa_8b21350185373425.png)

- **QA: Can the computed columns be used in joins?**

  Yes, computed columns can be utilized in joins, as long as they are defined in the model and pre-calculated in an index.
- **QA: What happens if a computed column's expression references a non-existent column?**

  The query will fail, and an error message will indicate that the column does not exist.
- **QA: Are computed columns supported in all data types?**

  Computed columns are limited to specific data types. Ensure compatibility when defining expressions.
- **QA: How can I optimize the performance of queries using computed columns?**

  To optimize performance, define computed columns on the model, use them in index and query them in your SQL to leverage pre-calculation benefits.
- **QA: Can I use UDFs in computed column expressions?**

  Yes, computed columns can utilize Hive UDFs, enabling the reuse of existing business logic.

Computed columns in Kylin provide a powerful mechanism for enhancing data processing and query performance. By understanding their usage, properties, and potential limitations, you can leverage computed columns to optimize your analytics and data transformations effectively.

---

<a id="model-rec-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/model/rec/intro/ -->

<!-- page_index: 33 -->

# Recommendation

Version: 5.0.2

Following the manual modeling section, it’s evident that the work involved can be tedious and labor-intensive, relying heavily on the expertise of data modelers. In this chapter, we will introduce an easier way to accomplish this work in Kylin 5.0 through a feature called **Recommendation**. Note that this type of recommendation differs from the its counterpart in machine learning, but it significantly improves your efficiency. We will cover the following topics:

- **[Imported SQL Modeling](#model-rec-sql_modeling)**: The Kylin recommendation engine can recognize input SQL statements, extract dimensions, measures, and other critical information, and automatically translate this data into models and indexes. This means you do not need in-depth knowledge to create models that meet your needs, allowing you to focus more on your business.
- **[Query History Recommendation](#model-rec-optimize_by_qh)**: The Kylin recommendation engine periodically analyzes query history records and transforms them into recommendations. You just need to review the proposed recommendations and make any necessary adjustments to the configuration to achieve your desired outcomes. Once you approve them, query performance can be significantly accelerated.
- **[Index Optimization](#model-rec-index_optimization)**: The Kylin recommendation engine analyzes the relationships among existing indexes to identify those that are useless or ineffective. It then generates recommendations for deletion, helping you save time on building and managing indexes as well as conserving storage space.

Before the journey, you should turn on the recommendation function in the project setting page.

![turn_on_recommendation.gif](assets/images/turn-on-recommendation-98eec60a46f84468ee1b0145dd34cb9b_154e184448b8a85b.gif)

Now, let’s embark on this journey.

---

<a id="model-rec-sql_modeling"></a>

<!-- source_url: https://kylin.apache.org/docs/model/rec/sql_modeling/ -->

<!-- page_index: 34 -->

# Imported SQL Modeling

Version: 5.0.2

This chapter we will show you how to create model and index by SQL.

- [Load data source](#datasource-intro). This article takes this [SSB sample dataset](#quickstart-tutorial) as an example to build model and indexes.
- Save the SQL statements as a *.txt* or *.sql* file. The following SQL statement is used in this article.


> [!TIP]
> **Tips**
> The file size should be no larger than 5 MB. If there are multiple SQL statements, separate them by semicolons (;).

- Create a project if you have not created any projects yet. For more details, refer to [Create project](#operations-project-managing-project_management).
- Turn on recommendation function in the project setting page, this has been introduced in the chapter [Recommendation](#model-rec-intro).

The following figure shows the entrance to SQL modeling. Please select **From SQL**, and the system will prompt you to upload the file. After the upload is completed, please click Next.

![](assets/images/from-sql-9eee675d0f2ccf644e41d7d51f4ea71f_1c8c282ec9c2d34c.png)

In this example, we use the SQL statements as following.

```sql
-- valid sql 
select 1 from SSB.CUSTOMER; 
select C_CUSTKEY from SSB.CUSTOMER; 
 
-- invalid sql, T_PRICE_PER_ITEM looks like a computed column name 
select sum(T_PRICE_PER_ITEM) from SSB.P_LINEORDER; 
 
-- valid sql 
select  
    CUSTOMER.C_NATION,  
    CUSTOMER.C_CITY, 
    sum(P_LINEORDER.LO_SUPPLYCOST + 1),  
    sum(P_LINEORDER.LO_REVENUE) 
from  
    SSB.P_LINEORDER 
left join SSB.CUSTOMER on P_LINEORDER.LO_CUSTKEY = CUSTOMER.C_CUSTKEY 
left join SSB.PART  on P_LINEORDER.LO_PARTKEY = PART.P_PARTKEY 
group by  
    CUSTOMER.C_NATION,  
    CUSTOMER.C_CITY; 
 
-- valid sql, but useless, will be ignored by the engine 
select 1; 
 
-- invalid sql, bail out 
select AAA from CCB.TABLE1; 
```

After the SQL has been analyzed, you will see a screen similar to the one shown below. In this example, there are two invalid SQL statements. You can safely ignore these and proceed to the next step.

![](assets/images/imported-sql-c1adcc77949d40570e6d62e3b030bbbd_ec3e1684797a868f.png)

The **Preview** dialog box displays the model created from the SQL input. You will see two proposed models, along with their respective computed columns, dimensions, and measures. Although the indexes for the models are also generated, they are not displayed here, as the focus is primarily on the model itself.
![](assets/images/preview-models-e5af3aeb04676b81288cd086a1e59a3a_572583731811d04c.png)

- **Model Name**: It is automatically generated and takes the format `AUTO_MODEL_FACT TABLE NAME_NUMBER`. You can also manually adjust the model name. It can be any combination of numbers, letters, and underscores (`_`). The maximum length of the model name is 127 characters. When the fact table name is too long, the system will automatically truncate the fact table name from the end to ensure that the automatically generated model name is less than or equal to 127 characters. When truncated, the model name format is `AUTO_MODEL_TRUNCATED FACT TABLE NAME_NUMBER`.
- **Fact Table**: The fact table of model.
- **SQL**: The sql related to the model. Similar SQL statements will be merged when generating models.
- **Add Base Indexes**: Basic indexes include base aggregated indexes and base table indexes. Base aggregated indexes contain all model dimensions and measures, and base table indexes contain columns used in all model dimensions and measures. It's recommended to keep it selected to avoid frequent [query push-down](#query-push_down) which may increase query response times. By default, base indexes will automatically update with model changes.

If you click the **OK** button, these two models will be added to the system. Then you can go to model list page, you will see a page as follows.

![model_list.png](assets/images/model-list-347ba1080f3c582e9d9c573314c1fe0c_a2867044e266e6f4.png)

In this section, we'll demonstrate another case of creating indexes using SQL. Before proceeding, we need to bring the model *AUTO\_MODEL\_CUSTOMER\_1* online. Once the model is online, we can import the following SQL statement, which will result in the following outcome.

```sq
select C_CITY from SSB.CUSTOMER group by C_CITY; 
```

You have two options:

- **Create New Models**: This option will add a new model to the system based on the SQL input.
- **Convert to Recommendations**: This option will provide recommendations on the existing model and propose new indexes based on the query patterns.

![create_or_convert.png](assets/images/create-or-convert-2492e1479b0c2273cde6f8591f540acb_4df252e40de3ce63.png)

After selecting **Convert to Recommendations** and accepting the proposed result on the **Preview** page, you should see a confirmation indicating success. This means the recommended indexes have been successfully generated.

To verify this, navigate to the **Index Overview** page, where you will be able to view the newly created indexes. This step allows you to confirm that the system has applied the optimizations and recommendations to improve query performance based on your model's structure.

![convert_success.png](assets/images/convert-success-e6274be304c3cb2e2c5fa59379e5e175_c42b4bcc0fd17e05.png)

As shown in the picture, there is a **Recommended Aggregate Index** whose content is *[C\_CICTY, COUNT\_ALL]* corresponding to our input sql statement. Besides, the base indexes has been updated, you can check on your system.

![show_accepted_index.png](assets/images/show-accepted-index-0b7256be0f1c6638bb8968ef5e4ce8e4_032e424a42faf5b9.png)

When you select **Create New Models**, the system will generate a new model, such as *AUTO\_MODEL\_CUSTOMER\_2*, with *SSB.CUSTOMER* as the fact table. However, we against doing this, as it may lead to the creation of numerous similar models. Managing a large number of models can become difficult and inefficient.

![create_new_model.png](assets/images/create-new-model-b47a575114416ef9319114e3f85fe048_3026469050f94ed8.png)

---

<a id="model-rec-optimize_by_qh"></a>

<!-- source_url: https://kylin.apache.org/docs/model/rec/optimize_by_qh/ -->

<!-- page_index: 35 -->

# Query History Recommendation

Version: 5.0.2

In the previous chapter, we introduced [imported SQL modeling](#model-rec-sql_modeling). Here, we will explore another feature—\*
*optimizing indexes using query history*\* in the Kylin Engine. This capability allows the system to recognize and
propose the most valuable indexes based on past queries, helping to accelerate query performance. It simplifies the
process of selecting indexes.

This chapter will cover the following:

1. **Settings to Enable Query History Optimization**: How to configure the system to recognize valuable indexes from
   query history.
2. **Generating Recommendations**: The process for generating index recommendations based on historical query data.
3. **Approving Recommendations**: How to review and approve these recommendations to create the appropriate indexes for
   optimized performance.

After enable the recommendation engine, the **Recommendation Preferences** panel will appear, the page as follows. You
can set user rules, duration rules, hit rules, and limit of Recommendations for Adding Index.

- **User Rules:** Turn on the toggle switch if you only want to generate recommendations for selected users and/or user
  groups. Then you can select users and/or user groups in the following field(s).
- **Duration Rule:** Generate recommendations for queries within certain duration. Then you can customize the query
  duration. Default: 5 to 3600 second(s).

- **Hit Rules**: Set the parameters below to filter out indexes that are frequently hit by queries, that is, the indexes
  of high value.
  For example, if the **Time Window** is set to 2 and **Number of Hits** is set to 30, the system will only prompt
  recommendations with at least 30 query hits in the past 2 days.

  - **Time Window**: Set the number of days to be calculated for the query hits, starting from today, default: 2 days.
  - **Number of Hits**: Set the number of query hits (default: 30 hits). This hit count can later be modified based on
    the recommendations.
- **Limit of Recommendations for Adding Index**: Set how many recommendations will be prompted and the push frequency.
  This parameter is only valid for recommendations based on query history.

  - **Number of recommendations**: Set the number of recommendations that will be pushed. Recommendations will be
    ranked based on the query hit rates (from highest to lowest); the default value is 20, indicating only the top 20
    recommendations will be prompted.
  - **Recommendation Frequency**: Set the frequency (in days) to push the recommendations, default: 2 days.

![rec_rules.png](assets/images/rec-rules-9120fdc5dc0588a4a65a9dddf1099468_7b9b587f01c53944.png)

The generation of index suggestions is handled as a background task. This task runs at regular intervals, generating
recommendations and storing them in the recommendation table of the database. At this stage, all suggestions remain
invisible. When multiple query histories result in the same recommendation, the system accumulates the recommendation's
statistical frequency on a daily basis.

To configure the task's running frequency, you can refer to the following configuration items. These settings allow you
to control how often the system scans query history and updates recommendations based on usage patterns.

```shell
# This parameter is used for controlling the maximum queries
# processed by each scheduled task.
# Since the query history table may contain too many records,
# each task will process at most 1000000 queries by default.
# The engine does not handle all query history items in a single
# batch due to memory constraints.
# Instead, it processes them in smaller batches. By default,
# each batch handles 1,000 queries.
# The task interval is 60 minutes by default.
 
kylin.favorite.query-history-accelerate-max-size=1000000 
kylin.favorite.query-history-accelerate-batch-size=1000 
kylin.favorite.query-history-accelerate-interval=60m 
```

In addition, there is a scheduled task in the system that calculates how often a recommended index is "hit" during a
specific **Time Window**. When the **Number of Hits** exceeds the configured threshold, the system exposes the
recommendation to the user, who can then choose whether to accept it. The frequency at which the system generates these
suggestions is controlled by the **Recommendation Frequency** configuration.

> [!TIP]
> **Tips**
> Ensure that you have sufficient memory available before modifying the configurations mentioned above.
> Complex queries typically demand more memory, so if needed, you can adjust the memory limit by modifying
> the `conf/setenv.sh` file.
>
> - export JAVA\_VM\_TOOL\_XMS=1g
> - export JAVA\_VM\_TOOL\_XMX=8g

To quickly verify the ability of the system to generate index recommendations, follow these steps:

1. **Execute the Query**: Go to the **Insight** page and run many query statements.
2. **Adjust Configuration Parameters**: Modify the recommended configuration settings to match the values shown in the
   figure.

![adjust_rec_conf.png](assets/images/adjust-rec-conf-3bc442f68ac7b22526f75561071110f7_868b6460ec83afa5.png)

By running the query and adjusting the parameters, the executing the following API request to trigger the generation of recommendations. After executing the request successfully, you should be able to see recommendations generated based on query history.

```shell
curl -X PUT 'http://localhost:7070/kylin/api/recommendations/acceleration?project=learn_kylin' \ 
    -H 'Accept-Encoding: gzip, deflate, br' \ 
    -H 'Accept: application/vnd.apache.kylin-v4+json' \ 
    -H 'Content-Type: application/json;charset=UTF-8' \ 
    -H 'Accept-Language: en' 
```

![recommendations.png](assets/images/recommendations-0ebd25de4912e09bd1f9cadf74bddb4e_b3f096317c781f40.png)

On the **Recommendation** page, you have the option to review and manage the suggested indexes. You can take the following actions:

- **Accept**: If you choose to accept the recommendation, it will be converted into an index. The index will be applied to the model to improve query performance.
- **Delete**: If you choose to delete the recommendation, it will not be physically removed from the system but will be marked as deleted (logical deletion) and remain in the recommendation table for record-keeping purposes.

- Question: At which level will the **Recommendations Preferences** be effective?

  Answer: At the project level. To exclude certain tables at the model level, that is, this table will not be calculated
  during the pre-computation and indexing, please deselect the **Precompute Join Relationships** checkbox in the **Add
  Join Relationship** dialog box.

---

<a id="model-rec-index_optimization"></a>

<!-- source_url: https://kylin.apache.org/docs/model/rec/index_optimization/ -->

<!-- page_index: 36 -->

# Index Optimization

Version: 5.0.2

Kylin recommendation engine includes index optimization as one of its core capabilities. Besides recommending new high value indexes to reduce query response times, Kylin also recommends deleting low value indexes discovered following index optimization strategies to help reduce index building pressure and storage costs. This article introduces index optimization strategies.

When the Kylin recommendation engine detects an inclusion relationship among indexes, it generates recommendations to delete these indexes. These recommendations do not impact query efficiency.

- **For table indexes**, the inclusion relationship must satisfy **all** of the following conditions:

  - There is an inclusion relationship among dimensions, and the dimensions are in the same order. For example, if A, B, and C represent three dimensions, then the table index **[A, B, C]** has an inclusion relationship with the table indexes **[A, C]** and **[B, C]**, but not with **[C, A]** or **[C, B]**.
  - The table indexes share the same `ShardBy` column.
- **For aggregate indexes**, the inclusion relationship must satisfy **all** of the following conditions:

  - The dimensions are exactly the same, and there is an inclusion relationship between the measure sets. For example, if A, B, and C represent three dimensions, and m1, m2, and m3 represent three measures, then the aggregate index **[A, B, C, m1, m2, m3]** has an inclusion relationship with the aggregate indexes **[A, B, C, m1]** and **[A, B, C, m2, m3]**, but not with **[A, C, m2]** or **[A, C, m1, m3]**.
  - The aggregate indexes share the same `ShardBy` column.

> [!NOTE]
>
> There is no inclusion relation between table indexes and aggregate indexes.

When the Kylin recommendation engine detects similarities among aggregate indexes, it will generate a recommendation to optimize these indexes. This recommendation may affect query efficiency.

**Similar indexes** must satisfy **all** of the following conditions:

- **Parent-Child Relationship**: Aggregate indexes generated by aggregate groups must have a parent-child relationship, meaning their dimensions have an inclusion relation. For example, if A, B, and C represent three dimensions, and m1 and m2 represent two measures, then the aggregate index **[A, B, C, m1, m2]** has a parent-child relationship with **[A, C, m1, m2]**.
- **Row Number Ratio**: The ratio of the row number of child indexes to that of the parent indexes must exceed a certain threshold. By default, this threshold is 0.9. You can adjust the threshold by modifying the `kylin.index.similarity-ratio-threshold` parameter.
- **Row Number Difference**: The difference in row numbers between parent and child indexes must be smaller than a defined threshold. By default, this threshold is 100 million. You can change the threshold by modifying the `kylin.index.beyond-similarity-bias-threshold` parameter.
- **Shared ShardBy Column**: Parent and child indexes must share the same `ShardBy` column.

The Kylin recommendation engine automatically analyzes how often an index is hit within a specific time range, such as daily or weekly. If the number of hits is below a certain threshold, it generates a recommendation to delete the index. This recommendation may affect query efficiency.

To adjust the low-frequency strategy, log in to Kylin, click the project \*\*Setting \*\*page, and modify the strategy in the **Index Optimization** section.

![](assets/images/low-usage-def42679ed508439b05d2db4a9f3ba8f_6a4555bc91d30402.png)

You can modify the `kylin.index.optimization-level` parameter to apply different optimization strategies for both custom indexes and those recommended by the recommendation engine.

The following table lists all the parameter values supported by Kylin and their corresponding index optimization strategies.

| **Parameter value** | **Description** |
| --- | --- |
| 0 | Custom indexes or indexes recommended by the recommendation engine will not be evaluated for optimization. |
| 1 | Custom indexes will not be evaluated for optimization. Indexes recommended by the recommendation engine will be evaluated for optimization using the inclusion strategy. |
| 2 (default) | Custom indexes will not be evaluated for optimization. Indexes recommended by the recommendation engine will be evaluated for optimization using the inclusion and low-frequency strategies. |
| 3 | Custom indexes will be evaluated for optimization using the similarity strategy. Indexes recommended by the recommendation engine will be evaluated for optimization using the inclusion and low-frequency strategies. |

- **Question:** After approving indexes recommended by the recommendation engine, I also created the same indexes by modifying an aggregate group. Will Kylin store both indexes?

  **Answer:** No. To avoid additional storage costs from duplicate index builds, Kylin only retains the indexes recommended by the recommendation engine and changes their source to custom indexes.
- **Question:** If I followed a recommendation to delete indexes, are there any other files I need to delete?

  **Answer:** This operation only deletes the index metadata and does not remove the index data stored in HDFS or other storage engine. You can clean these files either automatically or manually. For more details, see [Junk File Clean](#operations-system-operation-junk_file_clean).
- **Question:** What is a ShardBy column?

  **Answer:** ShardBy columns are used to evenly distribute data across multiple shards, increasing concurrency and query efficiency. Typically, columns with relatively high cardinality are chosen as ShardBy columns.

---

<a id="model-manage-model_info"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manage/model_info/ -->

<!-- page_index: 37 -->

# Model Information

Version: 5.0.2

You can create and design models manually. Below are the main content of model list:

1. Log in to Web UI, switch to a project.
2. Navigate to **Data Asset -> Model** page, where models are shown in a list. The picture below is the index group list:

   ![Model List](assets/images/model-list-7242de31cd8789791d5cf52dcc07c7c6_ecf061eb8c3f50c2.png)

   **Fields Explanation:**

   - **Model Name**: Model's name.

     - **Status**: There are four statuses.
     - *ONLINE* indicates this model is online and is able to answer queries.
       - *OFFLINE* indicates this model is offline and not available to answer queries. We recommend using offline when you need to edit the model.
       - *BROKEN* indicates this model is broken and not available. Mostly happens when the schemas of related source tables have changed, for instance, a related source table is deleted.
       - *WARNING* indicates this model is warning and can only server parts of queries. Mostly happens when the segments exist holes or indexes are waiting to build.
     - **Last Updated Time**: The lastest time to update model.
   - **More Actions**: The **More Actions** button will appear when you are hovering on model name area, please refer to [Model Operations](#model-manage-model_operation) for details.
   - **Owner**: The user who created this model.
   - **Description**: Model description.
   - **Fact Table**: The fact table of this model.
   - **Types**: Model types, which include *Batch Model*
   - **Usage**: Hit count by SQL statements in the last 30 days. Update every 30 minutes.
   - **Rows**: The rows of loaded data in this model.
   - **Storage**: The storage size of loaded data in this model, which combines the storage size of all Segments data.

     > Tip: When the tiered storage is turned on, the total storage size of the data loaded into the tiered storage (ClickHouse) will be displayed.
   - **Expansion Rate**: The ratio of the storage size of the built data to the storage size of the corresponding source table data under the model. Expansion Rate = Storage Size / Source Table Size.
   > Notice: The expansion rate won't show if the storage size is less than 1GB.

   - **Index Amount**: The amount of indexes in this model.

After expanding the model information, you can see the model overview page, which will help you to quickly get the model information.

![Model Overview](assets/images/unfold-model-f42cadeb37c62d962b4d09f0c17818cd_bf78c0faa4eb310f.png)

On this page, you can view the ER diagram of the model.

![View ER Diagram](assets/images/er-6c7a7d261e1c62026605e37c1f54b631_636d661df0a5398d.png)

What's more, you can view the dimensions and measures information contained in the model.

![View Dimensions Information](assets/images/dimensions-d79e8844288b9673a359f1c7eabf6bb2_ab14b820cdfc201b.png)

![View Measures Information](assets/images/measures-f4f138380bc040133d742000e6b51679_bef205d12c2c4d2e.png)

Models contain Segments and indexes. You can click model name to unfold the detailed information, as shown below:

![Details](assets/images/modellist-more-info-17dc538831608d61f5c0e3d039d0c854_76e96aca4b04941d.png)

---

<a id="model-manage-model_operation"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manage/model_operation/ -->

<!-- page_index: 38 -->

# Model Operation

Version: 5.0.2

> [!NOTE]
> 1. Locked Indexes will not be included in exported and cloned model
> 2. If the model is in *BROKEN* status, only the **delete** operation is allowed.

---

<a id="model-manage-import_export"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manage/import_export/ -->

<!-- page_index: 39 -->

# Import and Export

Version: 5.0.2

Kylin is stateless service. All state information is stored in metadata. The model is the core asset of the Kylin cluster. The model metadata describes the content of the model information in detail.

The movement of models in different environments is an important process of actual production. Therefore, importing and exporting metadata is a crucial link in operation and maintenance. Kylin provides import and export model metadata functions.

In many companies, in order to ensure the stability of the production environment, the release and change of models in the production environment is very strict. Users often need to deploy an additional independent development environment for data development and test verification (and possibly there is still a test environment), and migrating the data model from the development environment to the production environment is the process of model release. At the same time, this process needs to undergo rigorous review to ensure that the model is complete and accurate in the migration. The export and import of metadata is a crucial part of the migration.

![](assets/images/model-publish-7d8c28b0234c7f317afd65207a00df19_c294bef84ff0954f.png)

Model metadata export, you can export single or multiple models to a compressed package in zip format.

The exported model metadata range:

- Include: model definition information, such as the tables referenced by the model, table relationships, partition columns, calculable columns, filter conditions, measures, dimensions, aggregation groups, index content, etc.
- Not include: Segment information, building data, index status, etc.
- You can choose whether to include recommendations, model rewrite settings and sub-partition values in multi-level partitioning models. After selecting export, if the target system has a model with the same name, the recommendations, model rewrite settings and sub-partition values of the target model will be directly overwritten during import.

Notes:

- To ensure the integrity of the file, please do not unzip the file or modify the content of the file. The second half of the file name is the file integrity check code. If you need to modify the file name to increase recognition, please keep the check code unchanged.

- Export a single model

  Click **Data Asset->Model** in the left navigation bar to enter the **Model List** page. Through\*\*...(More Actions) - Export Model\*\* of a single model, the specified model can be exported in the format of a zip compressed package.
- Export multiple models

  - You can click the **Export Model** button on the **Model List Page**, select multiple models and export.
  - Or click the **Admin** button on the right of the status bar at the top of the page, in the project list page, in a single project **Actions - More Actions - Export Model**, select multiple models and export.

![](assets/images/model-export-efc9d7bbe267c4e9d7bb55aa0261097f_f0a65b4165471fce.png)

- On the **Model List** page, click the drop-down button behind **+Model**, select **Import Model**, and upload the model metadata compression package.
- Or enter the **Admin** page, on the project list page, select the project to import the model metadata, in **Action - ...(More Actions) - Import Model**, upload the model metadata compression package.

  ![](assets/images/model-upload-0e9a5c79e319bf3d21afb16793ad0a0c_86859ae6eece46d3.png)

When parsing the metadata package, the system will use **model name** as the unique identifier to distinguish the model, and match the target system with the model metadata in the metadata package. After the model is parsed by the system, there will be three operations to choose from: **Replace**, **Add New**, **Not Import**, the following will introduce in detail the default appearance of these three operations and whether they can be used as the next operation conditions of:

- **Not import**

  - Operation instructions: The system cannot import the model, or the user actively chooses not to continue importing the model.
  - The condition that appears by default: **cannot find a table or column in the target system data source in the model to be imported, or the data type of the column is inconsistent**.
  - Whether it can be switched to other operations:No.
- **Replace**

  - Operation instructions: A model with the same name already exists in the target system, and **the model has no major changes**, the system recommends using the model in the metadata package to replace the model with the same name in the target system.

    The criteria for no major changes in the model are:

    - The fact table and the dimension table are exactly the same.
    - The table relationship is completely consistent, including table connection conditions, table relationships, and column join conditions.
    - The partition column and format are exactly the same, including the model loading method (full and incremental), excluding multi-level partition sub-partition value differences.
    - The data filter conditions are completely consistent.
  - Condition of appearance by default: A model with the same name already exists in the target system, and there is no major change in the model.
  - Whether it can be switched to other operations: it can be switched to 'add new' or 'not import'. When manually switching to 'add new', please also change the model name to a name that does not exist in the target system to avoid model name conflicts.
  - **Note: Replacing may result in the deletion of part of the built data. Please backup and double check before importing.**
- **Add New**

  - Operation instructions: There is no model with the same name in the target system, and the model to be imported has the **table and column in the target system data source, and the column data type is consistent**. Or there is a model with the same name in the target system, and the model has major changes. For major changes in the model, refer to the above description of the replace operation.
  - Conditions that appear by default: the same as the two conditions in the operating instructions.
  - Whether it can be switched to other operations: it can be switched to not import.

When the model to be imported is selected, the model to be imported will be displayed on the right side, the difference between the model with the same name and the data source in the current project. Differences will be divided into four categories: **Not found**, **Add**, **Delete**, **Change** display.

After the model is imported, it may be necessary to build the newly added index before it can serve queries.

![](assets/images/model-check-0ad6f5a6178314ca0ff8e9f3dde7dc64_39961810147df441.png)

Different environments may have different requirements for model rewrite settings. When you export a model, you can choose whether to export the model rewrite settings at the same time. Later, when you import the model, the model settings of the target system with the same name will be overwrited.

Different environments generally have different values of multi-level partition sub-partitions. For models that use the multi-level partition, you can choose whether to export the multi-level sub-partition values at the same time when exporting the model. When importing the model, the multi-level partition sub-partition values will be overwrited in the target system. The building data corresponding sub-partition value will be deleted while importing.

You can also export and import model metadata through API. For details, please refer to: [Model Import and Export API](#restapi-model_api-model_import_and_export_api)

- **After the model is imported, it cannot be undone. Please make a backup of the model in advance**.
- Only supports export and import between the first two versions of the same version number. For example, the model metadata package exported by Kylin 4.x does not support importing in Kylin 5.x.

---

<a id="model-manage-data_loading"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manage/data_loading/ -->

<!-- page_index: 40 -->

# Data Loading

Version: 5.0.2

Load data calculates the source data based on the model and index definition. This chapter takes the sample data as an example to introduce two data load methods and processes:

- full load
- incremental load by date/time

This chapter also introduces segment operations and settings, which are used to manage Segments.

- Segment operation and settings
  - Segment Merge

If you want to load all the data in the source table, you can choose full load. The main contents are as follows:

If you do not set a time partition column for your model, it will be full load each time.

You cannot merge segments in a full load type model since there should be only one segment.

Here we will introduce how to do a full load in the Web UI:

1. Select the model that needs the full load in the model list. Click the **Build Index** button.

   ![Load Data](assets/images/load-data-2d3aa0b9b163001f3535a883050efd0e_48878c42405a0a6c.png)
2. You will be prompted to load all data, including the data already loaded in the model.

   ![Notice](assets/images/notice-ba1868589b20efe3ef30c0ca40ee2925_78107bbe17b22aab.png)

   >
> [!NOTE]
> : If you load data for a model for the first time, the storage size in the above prompt will be 0.00 KB because the model has not been loaded (there is no data in the model).

3. After that, you can view the build index job via the **Monitor -> Job** page.
4. When the data is loaded, you can view the details in the model list. There is only one Segment in the **Segment** tag, and it is marked as full load.

   ![Full Load](assets/images/full-load-3e150eef64c838425aae84e6e607a9b5_003f2f242d501884.png)

As your business data grows over time, you can choose to load data by date / time. The main contents are as follows:

If you have set a time partition column for your model, you can load data by date / time each time on the **Data Asset -> Model** page.

1. **First Load**
   Open Kylin web UI and access the project. Select the model that needs to load in the model list page.

   **Step 1:** Click the **Build Index** button.

   ![Load Data](assets/images/load-data-2d3aa0b9b163001f3535a883050efd0e_48878c42405a0a6c.png)

   **Step 2:** Select the load range in the pop-up window and click the **Incremental Load** button. This action will trigger the job of **Load Data**.

   >
> [!NOTE]
> :

   > - You can click the icon on the right side of the load range to automatically detect the latest available range. When your mouse is hovering over the Icon **Detect available range** is displayed.
   > - When you load historical data at the first time and the data volume is too large, it may lead to a long loading time. Please be sure to set the load range according to your data volume, model complexity, and available resources.

   ![Load Range](assets/images/notice-2-a4eab0fcdb294c5c198fc99aeeaa4394_6225fbb34bb32dec.png)

The start time range of Segment should greater than `1970-01-02`.

**Step 3:** After submission, go to the **Monitor -> Job** page, a list of running jobs will be displayed. The first job is the job we just submitted and **Data Range** is displayed as the selected load range in step 2.

**Step 4:** When all steps are complete, the status of the job will become **Finished**. You can view the details in the model list. There is a Segment in the **Segment** tag and it is marked the **Start Time** and **End Time**.

![Load Data](assets/images/load-ok-b28980bf5dc9a9d87de8557b0e73fea8_2d51034b086b9926.png)

2. **Incremental Load**

   After the first segment is built, we can build more segments incrementally to accommodate new data. The time range of two segments cannot overlap.

   The steps for incremental load are consistent with the steps described above. Click the **Build Index** button then select the load range in the pop-up window. To ensure continuity, a new segment always starts from the end of the last segment.

   When load completes, go to the model detail page and check there are two segments under the model.

   ![Load by Date/Time](assets/images/load-twice-1c1d531f9d541880fa32248e0536f9f2_4c739d1d3d0ce9f4.png)
3. **Add Segment**

   Besides the above methods, you can also increase the model data range by adding a new segment. Click the **+ Segment** button under segment list. Then click the **Incremental Build** button in the pop-up window. After that, a building job will be submitted and the third segment will be shown when the job is finished.

   Note: If you want to use this function, you need to enable **Creating Reserved Segments**. Please refer to [Project Settings](#operations-project-managing-project_settings) for more information.

   ![Add segment](assets/images/add-segment-d7e9631fedac6a9330f4b163aceececa_3232663c46e7e937.png)
   ![Segment list](assets/images/model-list-3-f811f5bebc1156b8dc6c196a8512409a_bb10ce79c46020ee.png)

As the business scenario changes, some of the indexes in the model need to be retained only in latest months for saving building and storage costs. Therefore, Kylin provides a more flexible way to build indexes since the 5.0 released.

In the **Index Overview** tab, we can see the index list and some basic information. In the **Index List**, we can filter some indexes by the keyword or ids and then only build them in selected segments. For example, some new columns are added in the source table because of the business demands. Therefore, we need to add some new indexes for those columns in the latest one month for analysis and cost saving. As shown in the figure below, we can select all the new and NO BUILD indexes, and then click the **Build Index** button.

![Build Index](assets/images/build-index-1d00cdad9208a04576d04b7b906f81cd_1af6bcca11bb5105.png)

After that, please select the segment with the latest month and click the Build Index button to generate the building job. If you want to build the segments concurrently to improve the efficiency, you can also check the **Generate multiple segments in parallel** box. Then, the system will generate multiple jobs according to the number of selected segments.

![Build Index](assets/images/build-index-by-segment-8697d19b6746ba797ebd026bd52beb4b_626fdceba2e75b5a.png)

Similar to the building index, you can also delete some indexes in selected segments. For example, deleting some low frequent usage indexes in last year. As shown below, we can choose some of the indexes and click the **Delete** button to choose delete from all segments or parts of them.

Note: If the indexes are deleted from segments, it may influence the query performance because some of query may route to the pushdown engine due to the lack of index.

![Delete Index](assets/images/delete-index-8899e9a18c0933d5f316ef8fbb07fc83_dd981683f297a6f3.png)

To support more flexible index building, it may expect that different indexes will be included in different segments. In order to ensure the stable query performance, we recommend you build all index among all segments after a period of time. Therefore, if the index is incomplete, we can quickly build all indexes by clicking the icon after the index data range.

![Build All Index](assets/images/build-all-index-5a2fd557e1efb1373038d4d0f3824131_ee693585c9a68105.png)

As shown below, all the segments with incomplete indexes will be shown after clicked the icon. Then, you can select all the segments and click **Build Index** to ensure segments with all indexes.

![Build All Index](assets/images/build-all-index2-ff4a0be58554e678ab38fe27f2e9b1f2_673aecea381e01b4.png)

---

<a id="model-manage-segment"></a>

<!-- source_url: https://kylin.apache.org/docs/model/manage/segment/ -->

<!-- page_index: 41 -->

# Segment

Version: 5.0.2

Model (index group) consists of one or more segments. Each segment contains a range of data. Segment is created by building index or loading data with a selected data range on the partition columns.

The main contents are as follows:

User can access the Segment management interface by following these steps:

1. Open **Data Asset -> Model** page, and click the model (index group) name.
2. Select **Segment** tag.

The model list page in the project is shown as below.

![segment](assets/images/segment-81200245523cf0b121332d152aa594bb_dd0373e6c676fc7b.png)

Field description of the Segment list:

- Start time: The start time of the data in the Segment. If it is loaded in full **"Full Load"** is displayed.
- End time: The end time of the data in the Segment. If it is loaded in full **"Full Load"** is displayed.
- Index: Indexes in this segment / Total indexes
- Status: Segment status. You can find a detailed introduction [Segment Status](#model-manage-segment--status) section.
- Last Updated Time: Segment last updated time.
- Source Records: The source records of the data in the segment.
- Storage: The storage size of the data in the segment.

  > Tip: When the tiered storage is turned on, the storage size of the data loaded into the tiered storage (ClickHouse) will be displayed.
- Actions: The operation of the segment. Currently only **Show Detail** is supported.

You can view the segment status in the segment list. There are 6 types of segment statuses. See below:

- **ONLINE**: Segment can serve the query by indexes loaded data or pushdown engine.

> [!WARNING]
> - : The data in the segment has been loaded and can serve the query. However, the source data might be changed which might cause the data inconsistent. It's highly recommended to refresh all indexes within this segment.
- **LOCKED**: Segments that are refreshing or merging will be locked.
- **LOADING**: The data in the segment is loading.
- **REFRESHING**: A new segment is automatically generated when you refresh the specified segment. This new segment is marked as *REFRESHING*. When the refresh is complete the old segment will be automatically deleted.
- **MERGING**: A new segment is automatically generated when you merge the specified segments. This new segment is marked as *MERGING*. When the merge is complete the old segment will be automatically deleted.

You have 6 types of segment operations on the \*\*Data Asset -> model \*\*page.

- **+ Segment**: Add segments to define the model’s data range for serving queries. Queries within the range could be answered by indexes or pushdown engine. Queries out of the range would have no results. The button is located above the segment list.

> **Note:** In **Setting -> Basic Settings -> Segment Settings**, enable **Creating Reserved Segments**, then the **+ Segment** operation button will appear.

- **Show Detail**: You can click the icon on the right side of the segment list. When your mouse is hovering over the icon **Show Detail** is displayed. You can view details such as storage size, the data range and more.
- **Refresh**: Refresh the data in the segment. This operation supports batch refresh. The **Refresh** button is located above the segment list.

  >
> [!NOTE]
> : Only ONLINE and WARNING status segments can be refreshed.

- **Merge**：Merge multiple segments as a new one. The **Merge** button is located above the segment list.

  >
> [!NOTE]
> : Only ONLINE and WARNING status segments can be merged.

- **Delete**: Delete the segment. This operation supports batch deletion. The **Delete** button is located above the segment list.
- **Fix**: Fix the discontinuous segments. This button will be only displayed above the Segment list when the holes exists in Segment ranges.

You can set some to manage segments automatically in the **Setting -> Segment Settings** page. Please refer to [Project Settings](#operations-project-managing-project_settings) for the specific requirements.

In the incremental build mode, as the number of segments increases, the system may need to aggregate multiple segments to serve the query, which degrades the query performance and the query performance decreases. At the same time, a large number of small files will put pressure on the HDFS Namenode and affect the HDFS performance. Apache Kylin provides a mechanism to control the number of segments - \*\*Segments Merge \*\*.

You can merge multiple Segments in the Web GUI or using **Segment Manage API**.

In the web GUI

1. In the Data Assets -> Model -> Segment list, select the Segments to be merged.
2. Click "Merge" in the drop-down list, check that three conditions are met (consistent indexes, consistent sub-partition values, and continuous time ranges) , and submit the merge task.
   The system submits a task of type "Merge Data". Until the task is completed, the original segment is still available. After the task is completed, it will be replaced by a new segment. To save system resources, the original segments will be recycled and cleaned up.

Merging Segments is very simple, but requires manual triggering of the merge from time to time. When there are multiple projects and models in the production environment, it becomes very cumbersome to trigger the merge operation one by one. Therefore, Apache Kylin provides a segment automatic merging solution.

- [Auto-Merge settings](#model-manage-segment--setting)
- [Auto-merge strategy](#model-manage-segment--strategy)
- [Choose Segment](#model-manage-segment--choose)
- [Try Merge](#model-manage-segment--trymerge)
- [Notice](#model-manage-segment--notice)

According to different business needs, it supports the automatic merging of project and model settings respectively. If the two merge strategies are different, the system adopts the model-level settings.

- Project-level: Used for all models in a project, with the same merge strategy.
- Model-level: used for multiple models in a project, with different automatic merging strategies.

Please refer to **Segment Settings** and **Model/Index Group Rewrite Settings** of [Project Settings](#operations-project-managing-project_settings) for the specific requirements.

- Merge Timing: The system triggers an automatic merge attempt every time a new segment in the project becomes complete. To ensure query performance, all segments will not be merged at once.
- Time Threshold: Allows the user to set a time threshold of up to 6 layers. The larger the layer, the larger the time threshold. The user can select multiple levels (eg week, month).
  Note: day, week and month represent natural day, natural week and natural month respectively.


| level | Time Threshold |
| --- | --- |
| 1 | hour |
| 2 | day |
| 3 | week |
| 4 | month |
| 5 | quarter |
| 6 | year |

When triggering an Auto-Merge, the system attempts to start from maximum layer time threshold, skips segments whose time length is greater than or equal to the threshold, select remaining eligible Segments (consistent indexes, consistent sub-partition values, and continuous time ranges).

When the total time length of the segments reaches the time threshold, they will be merged. After the merge task is completed, the system will trigger an Auto- Merge attempt again; otherwise, the system repeats the search process using the time threshold for the next level. Stop trying until all the selected levels have no segment that meets the condition .

- The Auto-Merge of week is constrained by month, that is, if a natural week spans months/quarters/years, they are merged separately. (see example 2).
- During the process of merging segments, the HDFS storage space may exceed the threshold limit, causing the merging to fail.

- [Example 1](#model-manage-segment--ex1)
- [Example 2](#model-manage-segment--ex2)

The switch for Auto-Merge is turned on, and the specified time thresholds are week and month. There are six consecutive Segments A~F.

| Segment (Initial) | Time Range | Time Length |
| --- | --- | --- |
| A | 2022-01-01 ~ 2022-01-31 | 1 month |
| B | 2022-02-01 ~ 2022-02-06 | 1 week |
| C | 2022-02-07 ~ 2022-02-13 | 1 week |
| D | 2022-02-14 ~ 2022-02-20 | 1 week |
| E | 2022-02-21 ~2022-02-25 | 5 days |
| F | 2022-02-26 Saturday | 1 day |

Segment G was added later (Sunday 2022-02-27).

- Now there are 7 segments A~G, the system first tries to merge by month, since Segment A's time length is greater than or equal to the threshold (1 month), it will be excluded. The following segments B-G add up to less than 1 month, do not meet the time threshold (1 month), and therefore cannot be merged by month.
- The system will try the next level of time thresholds (i.e. merged by week). The system rescans all segments, finds that A, B, C, and D are all greater than or equal to the threshold (1 week), so they are skipped. The following segments E-G add up to the threshold (1 week) and merge into Segment X.
- With the addition of segment X, the system will be triggered to restart the merge attempt, but the attempt will be terminated because the conditions for automatic merge have not been met.

| Segment(Add G, Trigger Auto-Merge） | Time Range | Time Length |
| --- | --- | --- |
| A | 2022-01-01 ~ 2022-01-31 | 1 month |
| B | 2022-02-01 ~ 2022-02-06 | 1 week |
| C | 2022-02-07 ~ 2022-02-13 | 1 week |
| D | 2022-02-14 ~ 2022-02-20 | 1 week |
| X（Orignal E-G) | 2022-02-21 ~ 2022-02-27 | 1 week |

Add Segment H ( 2022-02-28)

- Trigger the system to try to merge by month, all segments except A add up to the threshold (1 month), so B-H are merged into Segment Y.
- With the addition of Segment Y, the system will trigger the merge attempt again, but the conditions for Auto-Merge have not been met, and the attempt is terminated.

| Segment（Add H, Trigger Auto-Merge） | Time Range | Time Length |
| --- | --- | --- |
| A | 2022-01-01 ~ 2022-01-31 | 1 week |
| Y （Orignal B-H） | 2022-02-01 ~ 2022-02-28 | 1 week |

There are six consecutive segments A~F, and their own time lengt are all 1 day. At this time, turn on the "auto merge" switch, specify the time threshold as weeks.

| Segment (Initial) | Time Range |
| --- | --- |
| A | Monday 2021-12-27 |
| B | Tuesday 2021-12-28 |
| C | Wednesday 2021-12-29 |
| D | Thursday 2021-12-30 |
| E | Friday 2021-12-31 |
| FS | Saturday 2022-01-01 |

Then Segment G was added (Sunday 2022-01-02) with a duration of 1 day.

- At this point there are 7 consecutive Segments, forming a natural week spanning 2 years. The system tries to merge by week, A-E is merged into a new Segment X.

| Segment（Add G, Trigger 1st Auto-Merge） | Time Range |
| --- | --- |
| X（Orignal A-E） | Monday to Friday (2021-12-27 ~ 2021-12-31) |
| F | Saturday 2022-01-01 |
| G | Sunday 2022-01-02 |

- With the addition of Segment X, the system will be triggered to merge by week, so F-G will be merged into a new Segment Y.

| Segment（Add X, Trigger 2nd Auto-Merge） | Time Range |
| --- | --- |
| X（Orignal A-E） | Monday to Friday (2021-01-27 ~ 2021-01-31) |
| Y（Orignal F-G） | Saturday to Sunday (2022-02-01 ~ 2022-02-02) |

- With the addition of Segment Y, the attempt to merge the system by week is triggered again. Now there are no segments with a duration of 1 week (in each year), so the attempt stops.

---

<a id="model-snapshot"></a>

<!-- source_url: https://kylin.apache.org/docs/model/snapshot/ -->

<!-- page_index: 42 -->

# Table Snapshot

Version: 5.0.2

The dimension table snapshot is a read-only static view of a source dimension table, which can be used in the following scenarios:

- Support independent query of dimension table. The dimension table snapshot will be used first to answer such queries.
- The dimensions on the dimension table can also serve the query by adding the join key to the aggregate group without generating an index, thereby avoiding the problem of dimension explosion

By default, snapshots are automatically generated by the system when loading data, building indexes, and refreshing/merging segments, and are used to store the data of the dimension tables in the model. Kylin 5.0 and later versions provide the function of independent management of snapshots.

After the snapshot management function is enabled, the system will **no longer** automatically manage snapshots. The building, refreshing, and deletion of snapshots must be manually managed.

The snapshot management is disabled by default. You can enable it in advanced settings.

1. Navigate to **Settings -> Advanced Settings -> Snapshot Management**, turn on **Support Snapshot Management**.

   ![Enable Snapshot Management](assets/images/snapshot-1-252c32a7229c5a3e8f3405ad05165998_d3fe2fae02e3d9f4.png)

   ![switch on](assets/images/snapshot-2-36a4bb3b6b48be8446bb89cd5850fdd9_88429e1fcc403354.png)

   ![switch off](assets/images/snapshot-3-9a6ea7cc4d86071a52c94b4c083af60f_23d8a1abe5415fec.png)

> [!NOTE]
> :

- After the snapshot management function is enabled, the system will **no longer** automatically manage snapshots. Following are the details:
  - If a table has already built a snapshot in the system, it will be displayed in the snapshot list. When the data changes, you need to manually refresh the snapshot
  - If a table has not built a snapshot in the system, it will not be displayed in the snapshot list, and you need to build it manually

1. After snapshot management is enabled, you can find **Snapshot** under **Data Asset**.
2. Navigate to **Data Asset -> Snapshot**, the snapshot list will be displayed, as shown below:

   ![Snapshot List](assets/images/snapshot-4-2d6a5226854d0feddda695560d0dff2d_7eaea6d7f2ac2fce.png)

   **Fields Explanation:**

   - **Table Name**：name of table.
   - **Database Name**：name of database.
   - **Partition Column**: partition column used in building snapshot.
   - **Usage**：usage of snapshot in querying. Update every 30 minutes.
   - **Status**：There are four statuses..
     - *LOADING* indicate the snapshot is loading and not able to serve queries.
     - *ONLINE* indicate the snapshot is online and able to serve queries.
     - *REFRESHING* indicate the snapshot is refreshing and able to serve queries with last built snapshots.
     - *BROKEN* indicate that the snapshot is damaged. When the source table has a structural change and is reloaded, the corresponding snapshot will change to this state and cannot serve the query at this time.
   - **Storage**：The storage of the snapshot ( Snappy compressed Parquet file format size ).
   - **Lookup Model Amount**：Indicate the number of models which use this table as lookup table.
   - **Fact Model Amount**：Indicate the number of models which use this table as fact table.
   - **Last Updated Time**：The last update/refresh time.

Above the snapshot lis are the operation buttons. Specific actions are listed below:

- **Add Snapshots**：Select tables or databases to build snapshots. Click **Next** to set partition columns.

  ![Add Snapshot](assets/images/snapshot-5-3cf18e32e56ae355410476cd22dde087_ad4e8b6b716b8781.png)

  Next, set the snapshot partition columns. Setting snapshot partition columns can improve the building speed by building partitions in parallel to a certain extent. By default, the system will build in a non-partitioned manner. Users can also set or detect partition columns , Also support specified partition value refresh.

  >
> [!NOTE]
> :

  > - The snapshot partition column can only be set as the Hive partition column. If the wrong partition column is used, the building task will get wrong;
  > - Building in partitions can only increase the speed of the building task, and the result of the built snapshot is still full data.

  ![Set Partition Column](assets/images/snapshot-6-ff1d3aba5b2b79e4cf6abdc3a244ac22_ed9bfb841665e9bc.png)
- **Refresh Snapshots**：Select snapshots to refresh.

  - Full refresh: The refresh operation at this time builds the latest and full snapshot.
  - Incremental refresh: For snapshots with source table partitions set, only the newly added partition value data will be refreshed (the built historical data will not be refreshed). It is recommended to select when the historical data is not updated.
  - Custom partition value refresh: Specify single or multiple partition values for data refresh.

  ![Refresh Snapshot](assets/images/snapshot-7-615be5c492f39b2fc23ab77464f16453_ce4e2631f271e0d4.png)
- **Delete Snapshots**：Select snapshots to delete. It will discard all jobs related to the snapshots.

  ![delete](assets/images/snapshot-8-7e7c96bf39e53196142a093de3eb6590_b3177497b18de699.png)
- **Repair Snapshots**: When the source table has a structural change and is reloaded, the corresponding snapshot will change to "BROKEN" and can be repaired.

  ![repair](assets/images/snapshot-9-355947afba43dc2bd4d439436b759d61_54b8987dc4450e42.png)

According building tasks of snapshot，you can configure spark related configurations in `kylin.properties` to achieve more fine-grained control.（These configuration can be overridden at project level）

The configuration starts with `kylin.engine.snapshot.spark-conf`, as shown below:

```text
kylin.engine.snapshot.spark-conf.spark.executor.instances=5 
kylin.engine.snapshot.spark-conf.spark.executor.cores=2 
kylin.engine.snapshot.spark-conf.spark.executor.memory=12288m 
kylin.engine.snapshot.spark-conf.spark.executor.memoryOverhead=3072m 
kylin.engine.snapshot.spark-conf.spark.sql.shuffle.partitions=200 
kylin.engine.snapshot.spark-conf.spark.driver.memory=4096m 
kylin.engine.snapshot.spark-conf.spark.driver.memoryOverhead=3072m 
kylin.engine.snapshot.spark-conf.spark.driver.cores=2 
```

---

<a id="model-features-measures-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/measures/intro/ -->

<!-- page_index: 43 -->

# Measures

Version: 5.0.2

This section introduces how to design measures in project.

Kylin provides basic measures such as SUM, MAX, MIN, COUNT and also advanced measures including TopN, precise count distinct, approximate count distinct, and approximate Percentile.

In the model editing page, there are three ways to add measures:

>
> [!NOTE]
> : It's highly recommended to finish the basic model design before add measures. You can click the **M** button on the right side in the model editing page to popup the measure list.

- Drag&Drop: drag the column that you want to define as a measure from the model to the measure list area, and then edit the measure in the pop-up window.
- Add Measure: click the first button **+ (Add)** on the measure list, and then edit the measure in the pop-up window.
- Add Measure in Batch: click the button **+ (Batch Add)** in the middle of the measure list, and then add multiple measures in the pop-up window.

  >
> [!NOTE]
> : The Batch Add only includes SUM, MAX, MIN, and COUNT. If you need to add advanced measure, please choose the first two ways.

When the calculated column type of the SUM measure is `decimal(P,D)`, the precision is `P + 10`, the maximum precision is 38, and custom precision is not supported.

---

<a id="model-features-measures-topn"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/measures/topn/ -->

<!-- page_index: 44 -->

# Top-N (Approximate) (Beta)

Version: 5.0.2

Finding the Top-N entities from a dataset is a frequent use case in data mining. We often read the reports or news titles like “Top 100 companies in the world”, “Most popular 20 electronics” and so forth. So exploring and analyzing the top entities are quite valuable and an essential part of many analyses.

As both the raw dataset and the number of entities increase in the big data era, this need is getting stronger than ever before. Without pre-calculation, retrieving the Top-K entities among a distributed big dataset may take a long time, making the pushdown query inefficient.

In v2.1 and higher, Apache Kylin introduces the “Top-N” measure, aiming to pre-calculate the top entities during the index build phase. In the query phase, Apache Kylin can quickly fetch and return the top records. The performance will be much better than a model without “Top-N” and give the user more power to analzye data.

In the project of Kylin 5 the Top-N measure is customizable.

>
> [!NOTE]
> : this Top-N measure is an approximate realization, to use it properly you should have a solid understanding of the algorithm as well as the data distribution.

Let’s use the project created in the chapter [Tutorial](#quickstart-tutorial) as an example to introduce Top-N measure settings. This project uses the SSB Dataset and needs to complete the model design and index build (including data load). A model won't be able to serve any queries if it has no index and data. You can read [Model Design Basics](#model-intro) to understand more about the methods used in model design.

We will use the fact table `SSB.P_LINEORDER`. This is a mockup of transactions that can happen in an online marketplace. It has a couple of dimension and measure columns. For easy understanding, we use only use four columns: `LO_ORDERDATE`, `LO_SUPPKEY`, `LO_PARTKEY` and `LO_ORDTOTALPRICE`. The table below gives an introduction to these columns.

| Column | Description | Cardinality |
| --- | --- | --- |
| LO\_ORDERDATE | Transaction Date | 2384 |
| LO\_SUPPKEY | Supplier ID, 1 represents ‘Supplier#000000001’ | 20 |
| LO\_PARTKEY | Part ID | 2023 |
| LO\_ORDTOTALPRICE | Sold amount | - |

*Method 1*: Oftentimes this e-commerce company needs to identify the Top-N (say top 100) in a given period for some suppliers. Please click **Query -> Insight** on the left navigation bar and enter. the following query statements in the **SQL Editor** :

```sql
SELECT LO_PARTKEY, SUM(LO_ORDTOTALPRICE) AS TOTAL_AMOUNT 
FROM SSB.P_LINEORDER 
WHERE LO_ORDERDATE between '1993-06-01' AND '1994-06-01'  
AND LO_SUPPKEY in (1)  
group by LO_PARTKEY 
order by SUM(LO_ORDTOTALPRICE) DESC  
limit 100 
```

It returns multiple records. See below:

![Query Result](assets/images/topn-result-a3e9f64c6831ad68ec5601bbdc482e9e_bed99847dc1a2e63.png)

*Method 2*: In order to get the desired query performance on a massive dataset, we recommend creating a Top-N measure for the target column and pre-calculating it when building the index. Please add a measure in the model editing page as follows. Fill in the measure **Name** for example `TOTAL_AMOUNT`, select **Function** as **TOP\_N**, select **Function Parameter** as **Top 100**, and finally select the target column from the dropdown list.

![Add Top-N Measure](assets/images/topn-measure-edit-fea291b999ba9af5bec9da0808c40045_1460b8d20b1bb1eb.png)

Once the measure is added and the model is saved, you need to go to the **Edit Aggregate Index** page, add the corresponding dimensions and measures to the appropriate aggregate group according to your business scenario, and the new aggregate index will be generated after submission. In this example, the new index will contain the dimension `LO_ORDERDATE`, `LO_SUPPKEY`, `LO_PARTKEY` and the measure `SUM(LO_ORDTOTALPRICE)`, you need to build index and load data to complete the precomputation of the target column. Apache Kylin will automatically rebuild the index and load data to complete the pre-calculation of the target column. You can check the job status of the Build Index in the **Job Monitor** page. After the index is built, you can use the **Top-N** measure to query the best-selling products.

---

<a id="model-features-measures-count_distinct_bitmap"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/measures/count_distinct_bitmap/ -->

<!-- page_index: 45 -->

# Count Distinct (Precise)

Version: 5.0.2

Count Distinct is a frequently used function for many data analysts. We implement precise Count Distinct based on bitmap. For the data with type tiny int(byte), small int(short) and int, the value projects onto the bitmap directly. For the data with type long, string, and others, encode the value as String onto a dict and project the dict id onto the bitmap. The resulting measure is the serialized data of the bitmap, not just the count value. This ensures results are always correct within any segment, even roll-up across segments.

In the project of Kylin 5, the Count Distinct (Precise) measure is customizable.

Before using the Count Distinct query, you need to clarify if the target column is ready. Click **Data Asset->Model**, select a model and click **Edit** to enter the model edit page. Then click **M** in the top right page to extend **Measure** table. You can get measure information in this table. If the measure desired has been pre-calculated on precise Count Distinct syntax (here requires both `Function` to be count\_distinct and `Return Type` to be bitmap) then this measure is ready for the Count Distinct query. Otherwise, you need to add a new measure Count Distinct (Precise) first.

Let’s use the project created in the chapter [Tutorial](#quickstart-tutorial) as an example to introduce count distinct precision measure settings. This project uses the SSB Dataset and needs to complete the model design and index build (including data load). A model won't be able to serve any queries if it has no index and data. You can read [Model Design Basics](#model-intro) to understand more about the methods used in model design.

Please add a measure in the model editing page as follows. Please fill in the measure **Name**, such as `DISTINCT_CUSTOMER`, select **Function** as **COUNT\_DISTINCT**, select accuracy requirement from **Function Parameter**, and finally select the target column from the drop-down list.

Kylin offers both approximate Count Distinct function and precise Count Distinct function. To get the pre-calculated precise Count Distinct value, select the `Function Parameter: Precisely` based on the bitmap, it will return a no error result if the storage resource is sufficient. For instance, when the Count Distinct is value over millions, the one result size might be hundreds of megabytes.

> **Note:** The query of precise Count Distinct is based on bitmap, so it will consume more resources.

![Add precisely COUNT_DISTINCT measure](assets/images/cd-measures-add-precisely-f8b0e648a01ad0ed7e268d09f7dc253d_2655b966e5f36e21.png)

Once the measure is added and the model is saved, you need to go to the **Edit Aggregate Index** page, add the corresponding dimensions and measures to the appropriate aggregate group according to your business scenario, and the new aggregate index will be generated after submission. You need to build index and load data to complete the precomputation of the target column. You can check the job of Build Index in the Job Monitor page. After the index is built, you can use the **Count Distinct (Precise)** measure to do some querying.

If you need to create a model from the very beginning and add a Count Distinct (Precise) measure, please add some indices and load data into the model. A model won't be able to serve any query if it has no index and data. You can read this chapter [Model Design Basics](#model-intro) to understand the methods used in model design.

For more information about approximate Count Distinct function, please refer to [Count Distinct (Approximate)](#model-features-measures-count_distinct_hllc) Introduction.

---

<a id="model-features-measures-count_distinct_hllc"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/measures/count_distinct_hllc/ -->

<!-- page_index: 46 -->

# Count Distinct (Approximate)

Version: 5.0.2

Count Distinct is a frequently used function for many data analysts, which is used to calculate the number of unique elements in a (multiple) set. However, it will spend lots of resources to calculate the exact Count Distinct value in big data scenario. Since v2.1, this product implements approximately Count Distinct using [HyperLogLog](https://hal.inria.fr/hal-00406166/document) algorithm, offers serveral precisions, with the error rates from 9.75% to 1.22% to support different query needs.

> **Note:** If you don't require a particularly precise result, this approximate Count Distinct query will return a good approximation with limited storage resources.

In the project of Kylin 5, you can customize Count Distinct (Approximate) measure with 5 accurracy options:

- Error Rate < 9.75%
- Error Rate < 4.88%
- Error Rate < 2.44%
- Error Rate < 1.72%
- Error Rate < 1.22%

Let’s use the project created in the chapter [Tutorial](#quickstart-tutorial) as an example to introduce approximate count distinct measure settings. This project uses the SSB Dataset and needs to complete the model design and index build (including data load). A model won't be able to serve any queries if it has no index and data. You can read [Model Design Basics](#model-intro) to understand more about the methods used in model design.

Before using Count Distinct query, you need to check the target column is ready. You can get measure information in the model editing page. If the desire measure has been pre-calculated on approximate Count Distinct syntax (requires both `Function` to be count\_distinct and `Return Type` to be hllc), then this measure is ready for Count Distinct querying. Otherwise, you need to add a new measure Count Distinct (Approximate) first.

Please add a measure in the model editing page as follows. Please fill in the measure **Name**, such as `DISTINCT_SHIPPRIOTITY`, select **Function** as **COUNT\_DISTINCT**, select accuracy requirement from **Function Parameter**, and finally select the target column from the drop-down list.

![Add approximate COUNT_DISTINCT measure](assets/images/cd-measures-edit-94000dd252413bb8854a7b6a5b680df2_b86bcdc0073deb0f.png)

Once the measure is added and the model is saved, click **Add Index** in the pop-up window to enter the **Model Index** page. You need to click **+**（Add Aggregate Group) under the **Aggregate Group** tab, add the corresponding dimensions and measures to the appropriate aggregate group according to your business scenario, and the new aggregate index will be generated after submission. You need to build index and load data to complete the precomputation of the target column. You can check the job of Build Index in the **Job Monitor** page. After the index is built, you can use the **Count Distinct (Approximate)** measure in queries, such as the query below:

```sql
SELECT COUNT(DISTINCT P_LINEORDER.LO_SHIPPRIOTITY) 
FROM SSB.P_LINEORDER 
```

If you need to create a model from the very beginning and add a Count Distinct (Approximate) measure, please add some indices and load data into the model. A model won't be able to serve any query if it has no index and data. You can read this chapter [Model Design Basics](#model-intro) to understand the method of model design.

More information about precise Count Distinct function, please refer to [Count Distinct (Approximate)](#model-features-measures-count_distinct_bitmap) Introduction.

---

<a id="model-features-measures-percentile_approx"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/measures/percentile_approx/ -->

<!-- page_index: 47 -->

# Percentile (Approximate)

Version: 5.0.2

This product supports the function **percentile**. Some previous versions refer to it as **percentile\_approx**. They have the same algorithm (thus result). If the percentile measure is predefined, the SQL query will enable sub-second query latency.

This function has three return types: 'percentile(100)', 'percentile(1000)' and 'percentile(10000)'. The higher return value means higher accuracy and higher storage resources are occupied. We recommend using percentile(100) in most scenarios.

In the project of Kylin 5 the Percentile (Approximate) measure is customizable.

Percentile\_approx returns the value of below which a given percentage of observations in a group of observations fall. For example, the 20th percentile is the value below which 20% of the observations may be found. Its syntax is as below:

- `percentile_approx({measure},p,B)`

*measure* is the measure to query. *p* is number between 0 and 1, inclusive. *B* controls the Approximate Accuracy. The higher the value, the higher the accuracy of the result. percentile\_approx uses the interpolation method to determine the value of the nth percentile.

Let’s use the project created in the chapter [Tutorial](#quickstart-tutorial) as an example to introduce percentile\_approx measure settings. This project uses the SSB Dataset and needs to complete the model design and index build (including data load). A model won't be able to serve any queries if it has no index and data. You can read [Model Design Basics](#model-intro) to understand more about the methods used in model design.

We will use the fact table `SSB.P_LINEORDER`. This sample table is a mockup of transactions that can happen in an online marketplace. It has a couple of dimension and measure columns. For easy undersatning, we will only use two columns: `LO_SUPPKEY` and `LO_ORDTOTALPRICE`. The table below gives an introduction to these columns.

| Column | Description |
| --- | --- |
| LO\_SUPPKEY | Supplier ID |
| LO\_ORDTOTALPRICE | Sold amount |

We want to query the value of the 50th percentage for each supplier's sold amount. The query example is below:

```sql
SELECT LO_SUPPKEY, percentile_approx(LO_ORDTOTALPRICE, 0.5) AS ORDER_TOTAL_PRICE 
FROM SSB.P_LINEORDER 
GROUP BY LO_SUPPKEY 
```

Before the **PERCENTILE\_APPROX** measure is added, the system will pushdown the query to Hive if the query pushdown function is enabled.
![Percentile Query Result](assets/images/percentile-result-hive-0983fa0d8b88c4634b3c4aa71df3a0f9_7e5286ab2422ff4b.png)

Please add a measure in the model editing page as follows. Please fill in the measure **Name** for example `PERCENTILE_ORDTOTALPRICE`, select **Function** as **PERCENTILE\_APPROX**, select **Function Parameter** as 'percentile(100)', 'percentile(1000)' or 'percentile(10000)' on demand. The Function Parameter means B listed in the above syntax. Higher value means higher accuracy and higher storage resources are occupied. Finally select the target column from the dropdown list.

![Add Percentile Measure](assets/images/percentile-approximate-13c5a50da48aa33692011b93868af516_ddc2e1a040d310bf.png)

Once the measure is added and the model is saved, click **Add Index** in the pop-up window to enter the **Model Index** page. You need to click **+**（Add Aggregate Group) under the **Aggregate Group** tab, add the dimensions and measures to the aggregate groups according to your business scenario, and the new aggregate indices will be generated after submission. In this example, the new index will contain the dimension `LO_SUPPKEY` and the measure `percentile_approx(LO_ORDTOTALPRICE, p, 100)`, you need to build index to make the indices available. You can check the job status in **Job Monitor** page. After the index is built, you can use the **PERCENTILE\_APPROX** measure for querying.

Resubmit the above SQL query in the **Query -> Insight** page, and you will find the result returns the value of the 50th percentage for each supplier's sold amount.

![Percentile Query Result](assets/images/percentile-result-9c5ce1404fbfa91293334f85c653c9a9_2ce5948b8f183ef0.png)

---

<a id="model-features-measures-corr"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/measures/corr/ -->

<!-- page_index: 48 -->

# CORR

Version: 5.0.2

> [!NOTE]
> **info**
> `corr({col1},{col2})`, col1, col2 is the column to calculate the correlation. It should note that, in the current version, the parameter return type for function CORR must be one of *real*, *bigint*, *integer*, *int4*, *long8*, *tinyint*, *smallint*, *decimal*, *double*, *float* and *numeric*. Date column is not supported to calculate now.

---

<a id="model-features-measures-collect_set"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/measures/collect_set/ -->

<!-- page_index: 49 -->

# COLLECT_SET

Version: 5.0.2

From Kylin 5, Kylin supports the COLLECT\_SET function, which returns a set of unique elements as an array. The syntax is `COLLECT_SET(column)`. The COLLECT\_SET measure is customizable.

Let’s use the project created in the chapter [Tutorial](#quickstart-tutorial) as an example to introduce COLLECT\_SET measure settings. This project uses the SSB Dataset and needs to complete the model design and index build (including data load). A model won't be able to serve any queries if it has no index and data. You can read [Model Design Basics](#model-intro) to understand more about the methods used in model design.

We will use the fact table `SSB.P_LINEORDER`. This sample table is a mockup of transactions that can happen in an online marketplace. It has a couple of dimension and measure columns. For easy understanding, we will only use two columns: `LO_CUSTKEY` and `LO_ORDERDATE`. The table below gives an introduction of these columns.

| Column | Description |
| --- | --- |
| LO\_CUSTKEY | Customer ID |
| LO\_ORDERDATE | Order Date |

We want to query the order date combination of each customer. The order date will be returned as an array with deduplicated values. The query example is below:

```sql
SELECT LO_CUSTKEY, COLLECT_SET(LO_ORDERDATE) 
FROM SSB.P_LINEORDER  
GROUP BY LO_CUSTKEY 
```

Before the **COLLECT\_SET** measure is added, the query will pushdown to Hive. According to the data amount of source tables, the result may return in several minutes or more.

Please add a measure in the model editing page as follows. Please fill in the measure **Name**, for example `COLLECT_SET_ORDERDATE`, select **Function** as **COLLECT\_SET**. Finally select the target column from the dropdown list, for example `P_LINEORDER.LO_ORDERDATE`.

![Add Collect_Set Measure](assets/images/add-collect-set-de018e22b8a5056d6b168a4afab6fafd_4b2a6e39d69702ef.png)

Once the measure is added and the model is saved, click **Add Index** in the pop-up window to enter the **Model Index** page. You need to click **+**（Add Aggregate Group) under the **Aggregate Group** tab, add the corresponding dimensions and measures to the appropriate aggregate group according to your business scenario, and the new aggregate index will be generated after submission. In this example, the new index will contain the dimension `LO_CUSTKEY` and the measure `COLLECT_SET(LO_ORDERDATE)`, you need to build index and load data to complete the precomputation of the target column. You can check the job of Build Index in the **Job Monitor** page. After the index is built, you can use the **COLLECT\_SET** measure in the query and use the precomputation data.

Resubmit the above SQL query in the **Query -> Insight** page, and you will find the result as below:

![Query Result](assets/images/collect-result-bdf00afd697631c7b585ec0f631a078c_0dd7d0c2238eb57b.png)

If you need to create a model from the very beginning and add a COLLECT\_SET measure, please add some indexes and load data into the model. A model won't be able to serve any query if it has no index and data. You can read this chapter [Model Design Basics](#model-intro) to understand the method of model design.

In actual application scenarios, you can use the COLLECT\_SET function in combination with other functions to apply more analysis scenarios. For example, the following query combines the CONCAT\_WS function, which the values in the array of order date into a string and splits it with `;`:

```sql
SELECT LO_CUSTKEY, CONCAT_WS(';', COLLECT_SET(LO_ORDERDATE)) 
FROM SSB.P_LINEORDER  
GROUP BY LO_CUSTKEY 
```

![Query Result](assets/images/concatws-result-0fa69b235a915830b903496e6e57b52d_c36de829e7f284f8.png)

>
> [!NOTE]
> : The CONCAT\_WS function is only supported in conjunction with the COLLECT\_SET function when querying.

---

<a id="model-features-scd2"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/scd2/ -->

<!-- page_index: 50 -->

# SCD2

Version: 5.0.2

In most multi-dimensional OLAP scenarios, lookup table might change unpredictably, rather than according to a regular schedule. For example product category of one specific product might get changed in product table, or segmentation of some customers might be changed in customer table. As product category or customer segmentation are modeled as dimensions in a cube, they are so called **Slowly Changing Dimension**, or SCD in short. Detailed introduction reference [wikipedia](https://en.wikipedia.org/wiki/Slowly_changing_dimension#Type_0:_retain_original)。

Dealing with this issue involves SCD management methodologies referred to as Type 0 through 6. But the most commonly seen are **Type 1** and **Type 2**:

- Type 1: overwrite. This methodology overwrites old with new data, and therefore does not track historical data. This is also called "latest status".
- Type 2: add new row. This method tracks historical data by creating multiple records for a given natural key in the dimensional tables with separate surrogate keys and/or different version numbers. Unlimited history is preserved for each insert. This is also called "historical truth".

For SCD Type 2（subsequently referred to as "SCD2"), Only supports the model based on the History Table, Below screen-shot illustrates the basics:

![SCD2 Model](assets/images/model-scd2-5x-b8d9aa8d63ac9e18e7d1c3666e3b2078_3d5da1094a455225.png)

The History Table stores the basic information of the record and the life cycle of each record. Changes to the record will add a new row and modify the life cycle of the historical record. Through the life cycle of the record, you can query historical records, and you can also query the latest records.

For example, in the SCD2\_SALES table below, the time interval of the salesperson in the corresponding business area (SALES\_DPT) is [START\_DATE,END\_DATE).

| SALES\_PK | SALES\_ID | SALES\_NAME | SALES\_DPT | START\_DATE | END\_DATE |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | Zhang San | Sourth area | 1992/1/1 | 1993/1/1 |
| 2 | 2 | Li Si | North area | 1992/1/1 | 1994/1/2 |
| 3 | 3 | Wang Wu | East area | 1992/1/1 | 1995/1/3 |
| 4 | 1 | Zhang San | North area | 1993/1/1 | 1994/1/1 |
| 5 | 2 | Li Si | East area | 1994/1/2 | 9999/1/1 |
| 6 | 3 | Wang Wu | Sourth area | 1995/1/3 | 9999/1/1 |
| 7 | 1 | Zhang San | West area | 1994/1/1 | 9999/1/1 |

It can be seen from the table that Zhang San:

- Worked in sourth area from 1992/1/1 to 1993/1/1
- Worked in the north area from 1993/1/1 to 1994/1/1
- And he has been working in the West area since 1994/1/1

Every time Zhang San change his work location, the History Table adds a new line of records and modifies the END\_DATE of the previous record.

In order to be able to query the historical information of the History Table, the fact table is often used to filter the start and end dates of the History Table records, like`LO_ORDERDATE>=START_DATE AND LO_ORDERDATE<END_DATE`
As shown below:

![model_historical_dimension_table_scd2_join](assets/images/model-historical-dimension-table-scd2-join-c12ff633c01b4c09fad77490f5ff3921_7d2cb6d6a91d9d40.png)

In order to use the History Table to meet the demand for slow dimensions, you can click **Setting -> Advanced Settings -> Support History Table** to turn on the function of supporting History Table. As shown below:

![historical_dimension_table_switch](assets/images/historical-dimension-table-switch-0cdb8c048e2004cc3d4d9aaf0c95afca_d2989e8b666a87d2.png)

- **When it is turned on, you can use non-equal join conditions `(≥，<)` could be used for modeling, building and queries.**
- **When it is turned off, the old SCD2 model will be offline**

The current join conditions based on the History Table have the following restrictions:

- **Can’t define multiple join conditions for the same columns**
- **Join condition ≥ and < must be used in pairs, and same column must be joint in both conditions**
- **Join condition for columns should include at least one equal-join condition (=)**
- **Two tables could only be joined by the same condition for one time**
- **Currently, recommendations are not supported for the History Table model**
- **By default, even if you use LEFT JOIN, you need to exactly match the model before you can use the model that contains the History Table to answer queries.**

For SCD2 model, the purpose of historical traceability can be achieved through the join conditions based on the History Table.
As shown in the figure below, in order to query the total sales revenue of the seller at each work location, the order date is associated with the working time interval.
![historical_dimension_table_scd2](assets/images/model-historical-dimension-table-scd2-aba85d757e78752a4e4681b6c1204aa7_c14643fe6468c12d.png)
![historical_dimension_table_scd2 join](assets/images/model-historical-dimension-table-scd2-join-c12ff633c01b4c09fad77490f5ff3921_7d2cb6d6a91d9d40.png)

For seller Zhang San, the total sales revenue of orders in different area from 1992 to the present can be queried, as shown in the following table:

| D\_YEAR | SALES\_NAME | SALES\_DPT | TOTAL\_REVENUE |
| --- | --- | --- | --- |
| 1992 | Zhang San | Sourth area | 3711706590 |
| 1993 | Zhang San | North area | 3882401031 |
| 1994 | Zhang San | West area | 3626302199 |
| 1995 | Zhang San | West area | 3733096229 |
| 1996 | Zhang San | West area | 3487903587 |
| 1997 | Zhang San | West area | 3725031606 |
| 1998 | Zhang San | West area | 2101112606 |

---

<a id="model-features-runtime_join"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/runtime_join/ -->

<!-- page_index: 51 -->

# Runtime Join

Version: 5.0.2

Pre-computation of the join relations refers to the process of expanding the joined tables of a model into a flat table based on mappings, and then building indexes based on the flat table. Kylin will precompute each join relation and generate a flat table that contains dimensions, measures and columns referenced by [computed columns](#model-manual-computed_column) by default. This article will cover the principles and features of **Precompute** **Join Relationships**.

This article takes *Fact* as the fact table and *Dim* as the dimension table to introduce how **Precompute Join Relationships** will affect the generation of a flat table. Suppose the table structures and data are as follows:

- Table *Fact*

| col1 | col2 | col3 |
| --- | --- | --- |
| 1 | a | AAA |
| 2 | b | BBB |
| 3 | c | CCC |

- Table *DIM*

| col1 | col2 | col3 |
| --- | --- | --- |
| 1 | A1 | AAAA |
| 1 | A2 | BBBB |
| 2 | B1 | CCCC |
| 3 | C1 | DDDD |

If *Fact* inner joins *Dim* and **Precompute Join Relationships** is enabled, it will generate a flat table as below:

| Fact.col1 | Fact.col2 | Fact.col3 | Dim.col1 | Dim.col2 | Dim.col3 |
| --- | --- | --- | --- | --- | --- |
| 1 | a | AAA | 1 | A1 | AAAA |
| 1 | a | AAA | 1 | A2 | BBBB |
| 2 | b | BBB | 2 | B1 | CCCC |
| 3 | c | CCC | 3 | C1 | DDDD |

If *Fact* inner joins *Dim* and **Precompute Join Relationships** is disabled, the flat table generated will be:

| Fact.col1 | Fact.col2 | Fact.col3 |
| --- | --- | --- |
| 1 | a | AAA |
| 2 | b | BBB |
| 3 | c | CCC |

> [!NOTE]
>
> In this scenario, the generation of a flat table does not rely on the dimension table and it will be stored as a snapshot in Kylin during the building process.

To strike the right balance between performance and cost, you can choose whether to enable **Precompute Join Relationships** based on your business needs and data characteristics when [designing a model](#model-manual-modeling). The following table compares the features of enabling and disabling **Precompute Join Relationships**.

| **Precompute Join Relationships** | **Query performance** | **Building duration** | **Storage costs** | **Adaptability to new query scenarios** | **Impact** |
| --- | --- | --- | --- | --- | --- |
| Enable | Good | Longer | Higher | Fair | ● All columns in dimension tables can be set as dimensions, or defined as measures or computed columns. |
| Disable | Fair | Shorter | Lower | Good | ● Columns in dimension tables cannot be set as dimensions, or defined as measures or computed columns, which means they cannot be referenced by indexes. ● Indexes and corresponding dimension snapshots will be hit by queries simultaneously, so users can get the query results through real-time join queries. In snowflake models, if a foreign key corresponds to a dimension table, and the table is set as an excluded table or **Precompute Join Relationships** is disabled, the dimension table will not be referenced when generating indexes. |

- Question: If **Precompute Join Relationships** is enabled in a model, what will happen if I disable it?

  Answer: If **Precompute Join Relationships** is disabled, Kylin will automatically delete all related indexes, dimensions, measures, and computed columns. Please use caution when you perform this operation.
- Question: If the table relationship is one-to-many or many-to-many, is there anything I should be aware of before enabling **Precompute Join Relationships**?

  Answer: In such a scenario, derived dimension queries will be disabled. If columns of the joined tables are not set as dimensions, these columns will not be referenced when generating indexes, or aggregate indexes or table indexes to accelerate queries.
- Question: If a table is excluded, will it affect precomputing the join relations?

  Answer: Even if **Precompute Join Relationships** is enabled, this table will not be used to generate a flat table or referenced when generating indexes.
- Question: What's the difference between excluding tables and disabling **Precompute Join Relationships**?

  Answer: The table below summarizes the main differences.

| Category | Effective level | Applicable scenario |
| --- | --- | --- |
| Exclude tables | Project-level | Often used when returning the latest data for queries is required. The corresponding foreign keys of the join relations, instead of the columns of the excluded tables, will be solidified into the indexes. |
| Disable Precompute Join Relationships | Model-level | Often used to reduce storage costs and improve building effeciency, for example, in one-to-many or many-to-many relationships. |

> [!NOTE]
>
> When designing a model, please do not use the columns of the excluded tables as dimensions, or else the index building job may fail.

---

<a id="model-features-multi_partitioning"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/multi_partitioning/ -->

<!-- page_index: 52 -->

# Multilevel Partitioning

Version: 5.0.2

Kylin multi-level partitioning means that in addition to partition management based on **time partition column**, the model can also be partitioned based on **sub-partition**.

In some analysis scenarios, in addition to partition management based on date or time, it is also necessary to perform partition management based on other dimensions, such as region, branch, etc. We call this sub-partition. For example, for some users who conduct business across regions, the time for data preparation varies in different regions due to differences of business end time. Users can set a region as a sub-region. When the data in a certain region is completed, the data in the current region can be constructed immediately, and the query and analysis of the region can be served after the construction is completed. This reduces the interdependence between sub-partitions, and makes data construction and query more flexible.

Kylin multi-level partition currently only supports two level partition.

You can enable or disable support for multi-level partitioning in the model **Settings-Advanced Settings-Multi-level Partitioning**.

![Set Multilevel Partitioning](assets/images/multilevel-partitioning-set-e8283ab6e5a1f6504b5108d83170deec_1b9aad4da06d5aea.png)

**Note:** When the multi-level partitioning of the model is closed, the model using the multi-level partitioning will be automatically offline. If you need to go online, you need to delete the sub-partition before going online or turn on this option.

![Turn off Multilevel Partitioning](assets/images/multilevel-partitioning-close-07629fcc148fad7ac1b86ec48fd1fa50_b743cd9f0585e0bb.png)

After enabling multi-level partitioning, you can create a model in **Data Asset- Model- +Model**. Then you can choose to add sub-partition columns when saving the model, and the types currently supported as sub-partition columns are **tinyint,smallint,int/integer,bigint,double,decimal,timestamp,date,varchar,char,boolean**.

![](assets/images/multilevel-partitioning-model-save-3e32c44849addb1b24cce69db514bebb_40ed67c5e6bec67e.png)

Or you can adjust the sub-partition column in **Model List-...(More Actions)-Model Partition**.

You can also add, delete or search for sub-partition values in **Model List-...(More Actions)-Manage Sub-Partition Values**.

When adding sub-partition values, the system does not check the correctness. The system allows adding sub-partition values that do not yet exist. When querying, the sub-partition value must be exactly the same with the sub-partition value to match (case sensitive, wildcards matching is not supported). Please ensure that the added sub-partition value meets your expectations.

![](assets/images/multilevel-partitioning-subp-value-3994fc55bcec5fa75dbcd27d2e897db2_b750434175516609.png)

When constructing a Segment of a new time range, you can click **Model List-Build Index** and specify the sub-partition value during construction

![](assets/images/multilevel-partioning-build-subp-first-592984ec14082e4c28710ef4e438598c_eb65f2992afcfdf1.png)

When the segment already exists, but only some sub-partitions under the segment have been constructed, you can click the model name to enter the model information page. You can click **Segment** to view the constructed sub-partitions in **Subpartition**, or continue to build sub-partitions that have not been constructed

![](assets/images/multilevel-partioning-build-subp-second-0-294f6412669c7086a11ce56432870ccb_f8271c0b4f38581a.png)

![](assets/images/multilevel-partioning-build-subp-second-1-624ea4f841961f8c0222343c24470b40_fe472117e2d8175f.png)

![](assets/images/multilevel-partioning-build-subp-second-3afa3076116261e60379256e647f21d1_7354ca78b247b00f.png)

If you need to merge Segments, you need to ensure that the sub-partition values are consistent.

The sub-partition has three states, namely:

- **ONLINE**: indicates that the construction has been completed and can serve the query
- **LOADING**: means under construction
- **REFRESHING**: indicates that it is being refreshed, and it can still serve the query during refreshing

When Kylin system answers queries, there are mainly the following rules:

- Segment time range defines the time range that the model can answer. When the query specifies an undefined time range, this part of the data returns empty.
- Segment sub-partition defines the range of sub-partition values that the model can answer. If the query specifies a sub-partition value that is not defined by the model, this part of the data returns empty. If the query specifies a sub-partition that is not built under the included time range, query pushdown will be used.
- If the index is in the time range and sub-partition value range in the Segment, if all of them can be satisfied and serve the query, the index will be used first, and if all of them cannot be satisfied, the pushdown query will be used (prerequisite for enabling pushdown).

The following common cases help understand. Suppose there are 4 Segments in the model, and the project has been opened for query pushdown

- Segment 1, the time range is [2015-2016), the sub-partitions constructed are Partition 1, Partition 2, including indexes Index A and Index B
- Segment 2, the time range is [2016-2017), and the sub-partitions constructed are Partition 1, Partition 2, Partition 3, including indexes Index A and Index C
- Segment 3, the time range is [2017-2018), and the sub-partitions constructed are Partition 1, Partition 2, Partition 4, including indexes Index A ,Index B and Index C
- Segment 4, the time range is [2018-2019), does not exist in the system, for ease of understanding, the code is Segment 4
- Segment 5, the time range is [2019-2020), reserved Segment, does not include subpartitions and indexes

![](assets/images/multilevel-partitioning-query-c8fa199d6abd6cde7a6fe02cb0498243_930bdf21dad69197.png)

When there are the following modes of query, the system will answer the query in this way:

**Case 1: Query without any time partition conditions**

The system will answer the query results of the total time range of all Segments, in this example the time range of Segment 1, Segment 2, Segment 3, Segment 5

**Case 2: The query specified a specific time partition [2015-2016), but did not specify any model sub-partition value**

The system will judge whether Index A and Index B can answer the query, if they can be answered, the index will answer, otherwise the query will be answered by the pushdown query engine

**Case3: The query specifies a specific time partition [2015-2017), and specifies that the model sub-partition value is Partition 1, Partition 2**

The system will judge whether Index A, Index B, Index C can answer the query, if it can be answered, the index will answer, otherwise the query will be answered by the pushdown query engine

**Case4: The query specifies a specific time partition [2015-2016), and specifies that the model sub-partition value is equal to Partition 3**

The query specifies Partition 3 that is not built under Segment 1, and the system will need to answer through the pushdown query engine

**Case5: The query specifies a specific time partition [2015-2018), and the model sub-partition value is equal to Partition 5**

**Partition 5** is not defined in the model, the system will return No Data

**Case6: The query specifies a specific time partition [2015-2019), and the model sub-partition value is equal to Partition 1**

At this time, the query contains an undefined time range [2018-2019), and this part of the data is empty. According to the range of 2015-2018, within the range of Partition 1, whether Index A, Index B, and Index C can answer the query, and how it can be answered will be answered by the index, otherwise the query pressure engine will answer.

**Case7: The query specifies a specific time partition [2015-2020), and the model sub-partition value is equal to Partition 1**

The query contains a segment that has not built any index data. It can be judged that the index must not fully meet the time range included in the query, and the system will answer through the pushdown query engine.

- Kylin multi-level partition currently only supports two le partition.
- If you need to merge Segments, you need to ensure that the sub-partition values are consistent.
- Please control the number of sub-partition values within 2000. If the number of partition values or the average length of which is too large, when submitting the building job or making other operations, the packet size limit during metastore communication may be exceeded and an error will be reported. For more detailed information, please refer to the FAQ below.

\*\*Q: When there are too many sub-partition values, errors related to `max_allowed_packet` or `innodb_log_file_size` may occur, then what should I do? \*\*

Error One:

Prompt: `The result packet of MySQL exceeds the limit. Please contact the admin to adjust the value of “max_allowed_packet“ as 256M in MySQL.`.

Reason: The default value of metastore MySQL configuration `max_allowed_packet` is small, which will limit the data packet size when Kylin node communicates with MySQL. When the number of sub-partition values is too large, the packet size in actual communication will exceed this limit.
For more information, please refer to Mysql [Official Document](https://dev.mysql.com/doc/refman/8.0/en/packet-too-large.html)

Solution: You can adjust MySQL configuration as `max_allowed_packet=256M` to avoid this problem.

Error Two:

Prompt: The build fails. The *kylin.log* prompts `The size of BLOB/TEXT data inserted in one transaction is greater than 10% of redo log size. Increase the redo log size using innodb_log_file_size`

Reason: The amount of data written to mysql redo log in a single transaction exceeds 10% of innodb\_log\_file\_size.

Solution: Refer to Mysql [official document](https://dev.mysql.com/doc/refman/8.0/en/innodb-parameters.html#sysvar_innodb_log_file_size) to increase the configuration item of `innodb_log_file_size`. You need to restart the mysqld service, please be cautious.

---

<a id="model-features-scalar_subquery"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/scalar_subquery/ -->

<!-- page_index: 53 -->

# Scalar Subquery

Version: 5.0.2

In many business data analysis scenarios, constant subquery is a common SQL usage.
You can start the recommended optimization for scenarios where constant subqueries are included in SQL join relationships through the following configuration. This parameter supports to configure at system-level or project-level:

```properties
## The default value of the parameter is false, which means the function is not enabled. 
kylin.query.scalar-subquery-join-enabled = true 
```

The following takes the sample data set of Kylin as an example. For more information about the sample data set, please refer to [Sample Dataset](#quickstart-tutorial).

```sql
SELECT D_DATEKEY, DATE_TIME, count(*), sum(D_YEAR) sy 
FROM (SELECT '1995-03-01' AS DATE_TIME 
      UNION ALL 
      SELECT '1995-03-02' AS DATE_TIME 
      UNION ALL 
      SELECT '1995-03-03' AS DATE_TIME) t1 
         LEFT JOIN SSB.DATES t2 ON t2.D_DATEKEY <= t1.DATE_TIME  
         AND t2.D_DATEKEY >= CONCAT(SUBSTR(t1.DATE_TIME, 1, 8), '01') 
GROUP BY D_DATEKEY, DATE_TIME 
```

Kylin can not generate an index containing the measure `SUM(D_YEAR)` through recommendation engine. However, with the switch turned on, an index containing the dimension `D_DATEKEY` and the measure `SUM(D_YEAR)`, `count(*)` can be generated, achieving SQL acceleration.

1. When the aggregate function is `count distinct`, index recommendation and SQL modeling are not currently supported. For example, when `sum(D_YEAR)` becomes `count(distinct D_YEAR)` in the above example, it cannot be recommended;
2. When the parameter of the aggregate function is an expression, index recommendation and SQL modeling are not currently supported. For example, when `sum(D_YEAR)` becomes `sum(D_YEAR+1)` in the above example, it cannot be recommended.

---

<a id="model-features-fast_bitmap"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/fast_bitmap/ -->

<!-- page_index: 54 -->

# Fast Bitmap Index

Version: 5.0.2

Since Kylin 5, the system has enhanced the optimization of queries that hit the index exactly (the query contains dimensions that are exactly the same as the dimensions of the selected index), and it also improves the performance in count distinct scenario.

With the following settings, optimization of precise count distinct queries can be applied:

1. Build a model that contains precise count distinct measure.
2. Modify the configuration in model level and add custom settings:
   `kylin.query.fast-bitmap-enabled = true`
3. Build the model
4. Query the SQL statements with exact indexes

This configuration is only available at the model level.

Taking Kylin's sample data set TPC-H as an example, the fact table LINEITEM simulates the recording of transaction data. The following query gets the number of orders under different sales dates.

```sql
SELECT  COUNT(distinct LINEITEM.L_ORDERKEY), 
        LINEITEM.L_SHIPDATE 
FROM TPCH_FLAT_ORC_50.LINEITEM 
JOIN TPCH_FLAT_ORC_50.ORDERS 
ON TPCH_FLAT_ORC_50.LINEITEM.L_ORDERKEY = TPCH_FLAT_ORC_50.ORDERS.O_ORDERKEY 
GROUP BY  LINEITEM.L_SHIPDATE 
```

1. Create the model:

   ![Create Model](assets/images/model-cdd97564178fca2952d84ea33b34eb94_3da3a936ce3bc294.png)
2. Switch to the **Model Settings** interface:

   ![Settings](assets/images/model-config-1-0ff4cc28a598695b090b974d018c9b9f_9dc27b0470f26046.png)
3. Enter the configuration to enable the function:

   ![Settings](assets/images/model-config-2-48d028a0c48f6414279810327413139c_188e9b0a50431718.png)
4. Add indexes:

   ![Add Index](assets/images/add-index-7d2087a6601a7940ecc2e766bb9ec4bd_1bdcf8df14323444.png)
5. After building successfully, the query performance is improved a lot when the query exactly matches index.

   ![Query before optimization](assets/images/query-old-145154582e08bb7395041866606cb40f_97319fb5dcfbeee5.png)

   ![Query after optimization](assets/images/query-new-caa4cf1e4c9d5b32f8c52314ab04711e_8878a2d3995e50e7.png)
6. Compare the execution plans before and after optimization

   ![Queries before optimization](assets/images/spark-plan-old-31e6308e32d067e930c7482c234380a4_ae72727e71fbbc71.png)

   ![Optimized query](assets/images/spark-plan-new-749cf1f43a0737200a0cd38c76d6b6ec_39c3a37feef8baad.png)

1. This operation will lead to a longer build time and almost double storage cost.
2. The indexes need to be refreshed when enabling this function.

---

<a id="model-features-integer_encoding"></a>

<!-- source_url: https://kylin.apache.org/docs/model/features/integer_encoding/ -->

<!-- page_index: 55 -->

# Dictionary Encoding

Version: 5.0.2

Starting from Kylin 5, the system supports no dictionary encoding for integer types

With the following settings, optimization of precise deduplication queries can be started:

1. Build a model that contains precise deduplication metrics
2. Modify the configuration of the model and add custom settings to the model in the settings interface:
   `kylin.query.skip-encode-integer-enabled = true`
3. Build the model

This configuration is only available at the model level

1. This operation can improve the build performance, if the data hash is serious, it may cause the inflation rate to be too high
2. If the value of this parameter changes, you need to re-brush the entire model

---

<a id="model-streaming-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/model/streaming/intro/ -->

<!-- page_index: 56 -->

# Real-time Function

Version: 5.0.2

Real-Time is an advanced feature that supports querying real-time streaming data, which achieves lower latency from data loading to query.

![](assets/images/real-time-arch1-0d9b5b1eb88dbfec9a3a1958851ddc33_f81523d5df99bc21.png)

Nowadays more and more users begin to apply real-time analytics in different use cases for better user experience, service quality and informed decision-making. This can be achieved by introducing a streaming real-time data platform. However, the addition of a platform may bring problems like data inconsistency, high costs, and managing difficulties.

Kylin empowers users with a single platform to handle both offline and real-time data. This low-threshold platform makes it easy for companies to unify data semantics, unlock data insights, and accelerate business decision-making in response to market changes.

- **Low latency and high concurrency**

  Kylin Real-Time meets the requirements of low latency and high concurrency for OLAP analysis.
- **From T+1 to T+0**

  Kylin Real-Time shortens the query processing cycle from T+1 to T+0. Users can achieve sub-second query response against data with minute-level latency, bringing down development and managing costs for real-time analytics scenarios.
- **High performance and low TCO**

  Kylin Real-Time empowers users with an OLAP solution for real-time analytics scenarios with better performance at a lower cost.

- [Hardware and software requirements](#model-streaming-prerequisite)
- [Work with Kylin Real-time](#model-streaming-real-time)

---

<a id="model-streaming-prerequisite"></a>

<!-- source_url: https://kylin.apache.org/docs/model/streaming/prerequisite/ -->

<!-- page_index: 57 -->

# Prerequisite

Version: 5.0.2

> [!NOTE]
> **info**
> If there's no DNS server in LAN, you need to manually add the IP address and Hostname of Kafka nodes to the `/etc/hosts` file of the Kylin server.

---

<a id="model-streaming-real-time"></a>

<!-- source_url: https://kylin.apache.org/docs/model/streaming/real-time/ -->

<!-- page_index: 58 -->

# Work with Kylin Real-time

Version: 5.0.2

Kylin Real-Time is an advanced feature that supports querying real-time streaming data, which achieves lower latency from data loading to query.

This article discusses how to work with Kylin Real-Time, including how to load streaming data source (Kafka data source) and how to use this feature in models and indexes.

- See [Hardware and software requirements](#model-streaming-prerequisite).
- Prepare Kafka data.

1. Log in to Kylin platform.
2. (Optional) Load dimension table (for scenarios with both batch and streaming data processing). For more information, see [Load Hive Table](#datasource-import_hive).

   3. Load fact table.

      1. In the left navigation, click **Data Assets** > **Data Source**.
      2. Click ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAACeSURBVHgB7ZIxDoJAFETnrxzEA1jsASw4gonYoxewEGt7L4G0XsLKXgt7j4AHWEchkFBs8SGhINnX/cybqT4QaJhpxWSXnRZ2OX897k+Nb6CFiB1drNX1wz0Jw+MPS/fYpMc9hSu/SvuXS0LevtTAXK75uWjvqBs6uI/QXxSBredJb151MYRkm93W6SHX+uErJjwcacUvpRCYEoG+/ABKESg81rHKRAAAAABJRU5ErkJggg==).
      3. In the pop-up dialog box, choose **Kafka** and click **Next**.
      4. Enter Kafka broker information `{IP address}:{port number}` (for example 10.1.0.8:9092). Then click **Get Cluster Information**.
      5. Select the target Kafka topic and the sample data of the topic will show up on the right side panel. Click **Next**.

         ![](assets/images/load-tables-1-en-2e4663dfc8c1c9accfa93d3f20936fc1_462115195312162b.png)
      6. Follow the instructions below to specify the source table(s). Then click **Load**.

         ![](assets/images/load-tables-2-en-d6662eda838d47672618ec53b433bb48_e0284ec1cbf26512.png)

   [NOTE]

   Please pay attention that **timestamp** datatype doesn't support format as 1668009600000.
   For such data,please choose string or int.
   Timestamp supports formats as yyyy-MM-dd,yyyy/MM/dd,yyyyMMdd,yyyy-MM-dd HH:mm:ss and yyyy-MM-dd HH:mm:ss.SSSS.

   - **Database and Table Name**: Specify a name for the database and table.
   - **Attach a Hive Table**: Turn on/off this toggle switch based on the data type to analyze.

     - For both batch and streaming data processing: Keep the default turned on status, then select the target Hive table to attach. The system will transform the field types of Kafka topic to be the same as Hive column types.
     > [NOTE]
     >
     > The partition columns of Hive table must be the **timestamp** type; Hive column number and name must be consistent with Kafka topic.
   - For streaming data processing only: Turn off the toggle switch and specify the partition column type as **timestamp**.
3. Build the model. For more information, see [Model Design](#model-intro). When building the model, you can use the data just loaded from Kafka data source as the fact table.
4. Build indexes. For more information, see [Aggregate Index](#model-manual-aggregation_group) and [Table Index](#model-manual-table_index).

   If you turned on the **Attach a Hive Table** toggle switch when loading the fact table, you can further specify data range for index building:

   ![](assets/images/index-data-range-en-34c905e0f76b3e626c0d76eae925f974_c1379be39bbaab71.png)

   - **Batch**: Build indexes with Hive table.
   - **Streaming**: Build indexes with Kafka topic.
   - **Fusion**: Build indexes with both Hive table and Kafka topic.
5. Query data.

   After index building, specify a time range for query and then streaming indexes will be used to respond to your query.

   ![](assets/images/real-time-query-streaming-data-c65fb756ea675a303de76e15bf63c794_a61871ee394aef9f.png)

- Question: When using Kylin Real-Time, is it a must that both batch and streaming data are included in the fact table?

  Answer: No, the fact table can be a Kafka or Hive table.
- Question: Does Kafka support dimension data?

  Answer: No. For now, dimension data can only be stored in Hive tables.
- Question: How to check the status of streaming data jobs?

  Answer: In the left navigation panel, click **Monitor** > **Streaming Job** to check job status. You can customize job parameters by clicking ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABYAAAAWCAYAAADEtGw7AAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAEoSURBVHgB7ZPNTcNAEIXfrO27S3AJ6YCkAszfORsqAEURNUQQARV4uYIPSQWYDtIBW4Lv2B5mCSb8JSERiRQp38Eev5Ge3+7OAjvWDf0mxvoi8qlMCBQxOC/YOxiavsUqxm9mKPREpT15NsB8S4Q2g3KpR4vMCpRmaG6sq/1aDFCFgGq7mqUmqPwFhfHhy0+4Qe+9eYhZJi/7JfFnjnW3Kakf628F1vfJ4A5LQLMasT6TrfEil/zBXI6xJIQVcCuqoCKFyqZmkP2L8aHuaUWcTBUvTpP+aKbx932dCyNLzVXrpNN7lnGMpjq36hV8TIWMylhx0FnkqYB9EDePTrsJcxUywzDUk+tVKOyPxH9lcqjBtcQLJa0tUZ7L7ObYFLsrnWFrr/T28Qp7YJn14Fq8CwAAAABJRU5ErkJggg==) of the target job. To learn more about parameters, see [Basic Configuration](#configuration-config).
- Question: If a query can be answered with data from either Kafka or Hive tables, will there be any data duplication?

  Answer: No. Kylin applies the following query logics to avoid data duplication:

  - If a query hits both batch and streaming indexes, batch indexes will be used to answer the query; only when data is not within the range of the batch indexes, streaming indexes will be used to answer the query.
  - If a query hits only batch or streaming indexes, the indexes hit will return data.
  - If a query hits neither batch nor streaming indexes, no data will be returned.
- Question: If dimension table changes, will these changes be synced to related models?

  Answer: Yes. You can set the refresh interval for dimension tables with the following steps:

  1. In the left navigation panel, click **Setting**.
  2. Click the **Advanced Settings** tab. In the **Custom Project Configuration** section at the end of the tab, click **+ Configuration**.
  3. In the **Add Custom Project Configuration** dialog box, set the configuration and parameter value. Then click **OK**.

     - **Configuration**: Enter kylin.streaming.table-refresh-interval.
     - **Value**: Set the refresh interval. For example, if you want to refresh data every hour, set the value to **1h**. The unit of **d** (day), **h** (hour), and **m** (minute) are supported.

       ![](assets/images/custom-project-configuration-en-0810c86f3e6aadf7d4e0d439719d61e7_3cb87c8f3a2f6968.png)
- Question: How to deal with Segments with overlapping time ranges in the model?

  Answer: For models that contain Segments with overlapping time ranges, they will be marked as broken in the model list. To ensure data accuracy, the model cannot be repaired. You need to re-create the model and refresh the data. Loss of checkpoint files may cause this problem (checkpoint files are used to record the building progress of Segment). You can avoid abnormal deletion of checkpoint files by configuring the parameter `kylin.engine.streaming-checkpoint-location={hdfsWorkingDir}/_streaming`.

---

<a id="model-streaming-custom-parser"></a>

<!-- source_url: https://kylin.apache.org/docs/model/streaming/custom-parser/ -->

<!-- page_index: 59 -->

# Streaming Message Parser

Version: 5.0.2

Real time function access Kafka supports user-defined parser to process multi-layer nested JSON, CSV structure and other data, and customize addition and deletion fields.

See the parser usage details [Real-time custom parser SDK](https://kylin.apache.org/docs/model/streaming/streaming_sdk/)

For details on managing parser Jar packages, see [Custom Parser Jar Package Management API](#restapi-custom_jar_manager_api)

---

<a id="query-insight"></a>

<!-- source_url: https://kylin.apache.org/docs/query/insight/ -->

<!-- page_index: 60 -->

# Query Insight

Version: 5.0.2

Kylin’s Intelligent OLAP Platform simplifies complex multidimensional analytics on massive datasets, achieving sub-second query response times through precomputation and index-building jobs. Unlike traditional methods that rely on real-time calculations, Kylin uses precalculated data to answer queries, significantly boosting performance. This innovative approach eliminates the need for real-time processing, delivering ultra-fast results and making Kylin an ideal solution for high-speed analytics.

This document describes how to use the Query Insight feature in Kylin.

To access Kylin's Web UI, click on **Query -> Insight** in the navigation bar. All queryable tables will appear on the left side of the page. You can enter your SQL query in the text box on the right, and the query results will be displayed in the text box below.

![Insight page](assets/images/insight-list-tables-f20f7a8c54c6c22ce2e1a81ba368c6bd_ee4c2c8fd865863c.png)

To execute a query, enter a `SELECT` statement and click **Run Query** to view the results. You will notice a **Limit** field in the bottom right corner. If your SQL statement does not include a `LIMIT` clause, the system will automatically impose a default limit of 500 rows. To disable this limit entirely, you can uncheck the checkbox next to the limit field.

After the query results are successfully returned, you will notice that the query execution time is approximately 0.24 seconds, and the query has hit the model. Additionally, the query ID is followed by an arrow. Clicking this arrow will take you to the query's page in the Spark UI. On this page, you can easily observe the SQL execution details within Spark, providing insight into how the query was processed.

![Execute SQL Queries](assets/images/insight-input-query-62310cb613c01cb3e90626d6df8b4b58_7c3b966fe8bc4033.png)

When optimizing slow queries, it's essential to analyze the specific execution steps to identify the root causes. To do this, hover your mouse over the **Durations** of the query. This action will display detailed execution steps along with their respective durations, helping you pinpoint the steps that may be contributing to the slow performance. By examining these details, you can better understand where optimization is needed.

![Query Duration](assets/images/insight-step-duration-de0b7e61413c43aae97f8ed973e25104_ad39eb291a1816af.png)

> [!TIP]
> **Notices**
> 1. Only query starts with **SELECT** or **EXPLAIN** are supported.
> 2. When query pushdown is enabled, queries that cannot be answered by the model (index group) will be routed to the pushdown engine for execution. In such cases, the query may take longer to return and could be executed by datasource(maybe Hive). Please refer to [Pushdown](#query-push_down) for more details.
> 3. If the query does not require Spark computation, such as hitting the query cache or involves constant queries, there will be no arrow next to the query ID.

After clicking the **Run Query** button, you can stop the query by clicking the **Stop Query** button, which will appear in the same position. In this example, the query is pushed down to the Hive datasource. For more information, please refer to the [Pushdown](#query-push_down) documentation.

![](assets/images/insight-stop-query-69641b9e52b162e8e943810fbeb003ae_52c4c1db251ab5f8.png)

After the query is stopped, query ID and error message will be displayed.

![](assets/images/insight-stop-query-result-685bcf82ef34da7dd07fe26c0fd5da50_d20b3351108a7234.png)

On the **SQL Editor** page, users can save queries by clicking the **Save** button in the bottom left corner. This action will trigger a pop-up window where you can enter a **Query Name** and a **Description**. Once you've filled in the details, click the **Submit** button to finish the saving process.

![Save Query](assets/images/insight-save-query-2edae87ca68cc59f4080ee941aee65fd_1941fb0e718f1290.png)

By default, Kylin displays query results in a table format. You can perform a fuzzy search for specific content using the Filter box at the top right of the query result. For example, if you enter "1992," each row in the query results that contains "1992" will be displayed, such as the daily order volume for the year 1992. Additionally, you have the option to export the query results to a CSV file.

![Query Result](assets/images/insight-show-result-356a54647e8d2e6a8a3c1c9c6e5b3823_9278a4cf48c0a042.png)

However, you can click the **Visualization** button on the results page to display the query results in a chart format. The available chart types include line chart, bar chart, and pie chart. Below is an example of the query results displayed in a line chart format. You can also choose different dimensions and metrics to customize the data shown in the chart.

![Visualization](assets/images/insight-visualization-94066b554ae9cb02934201b4aa357ec0_73662d31b01ba870.png)

Click the **Saved Queries** button at the top right of the SQL Editor to view all saved queries. A pop-up window will display a list of saved queries. By default, each query item is collapsed. To view the SQL, click the **Details** button next to the desired query. You can also check the box in front of a query and click the **Run Query** button to re-execute it.

![Saved Query](assets/images/insight-list-history-edb7896b129369300001a29f0c0456ee_81ffd955f49be97e.png)

---

<a id="query-specification-sql_spec"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/sql_spec/ -->

<!-- page_index: 61 -->

# SQL Specification

Version: 5.0.2

> [!NOTE]
> The implementation details may vary across different versions. For any questions or concerns, please reach out to the Kylin Community for assistance.

---

<a id="query-specification-data_type"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/data_type/ -->

<!-- page_index: 62 -->

# Data Types

Version: 5.0.2

> [!NOTE]
> When working with double type data, there is a potential issue with precision accuracy. This is due to the way floating-point numbers are represented in computer systems, which can lead to rounding errors or small inaccuracies in calculations, especially when dealing with very large or very small values. It's important to be mindful of this limitation when performing operations that require high precision, and consider alternative data types such as `decimal` for cases where exact accuracy is critical.

---

<a id="query-specification-operators"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/operators/ -->

<!-- page_index: 63 -->

# Operators

Version: 5.0.2

This chapter will introduce operators that applicable to SQL statements.

| Operator | Description | Syntax | Example |
| --- | --- | --- | --- |
| + | Plus operator | A + B | Cost + Profit |
| - | Minus operator | A - B | Revenue - Cost |
| \* | Multiply operator | A \* B | Unit\_Price \* Quantity |
| / | Divide operator | A / B | Total\_Sale / Quantity |

| Operator | Description | Syntax | Example |
| --- | --- | --- | --- |
| < | Less than | A < B | col1 < col2 |
| <= | Less than or equal | A <= B | col1 <= col2 |
| > | Greater than | A >= B | col1 > col2 |
| >= | Greater than or equal | A >= B | col1 >= col2 |
| <> | Not Equal | A <> B | col1 <> col2 |
| IS NULL | Whether *value* is null | value IS NULL | col1 IS NULL |
| IS NOT NULL | Whether *value* is not null | value IS NOT NULL | col1 IS NOT NULL |
| IS DISTINCT FROM | Whether two values are not equal, treating null values as the same | value1 IS DISTINCT FROM value2 | col1 IS DISTINCT FROM col2 |
| IS NOT DISTINCT FROM | Whether two values are equal, treating null values as the same | value1 IS NOT DISTINCT FROM value2 | col1 IS NOT DISTINCT FROM col2 |
| BETWEEN | Return true if the specified value is greater than or equal to value1 and less than or equal to value2 | A BETWEEN value1 AND value2 | col1 BETWEEN '2016-01-01' AND '2016-12-30' |
| NOT BETWEEN | Whether *value1* is less than *value2* or greater than *value3* | value1 NOT BETWEEN value2 AND value3 | col1 NOT BETWEEN '2016-01-01' AND '2016-12-30' |
| LIKE | Whether *string1* matches pattern *string2*, *string1* and *string2* are string types | string1 LIKE string2 | col1 LIKE '%frank%' |
| NOT LIKE | Whether *string1* does not match pattern *string2*, *string1* and *string2* are string types | string1 NOT LIKE string2 [ ESCAPE string3 ] | col1 NOT LIKE '%frank%' |
| SIMILAR TO | Whether *string1* matches *string2* in regular expression | string1 SIMILAR TO string2 | col1 SIMILAR TO 'frank' |
| NOT SIMILAR TO | Whether *string1* does not match *string2* in regular expression | string1 NOT SIMILAR TO string2 | col1 NOT SIMILAR TO 'frank' |

Limitations

- The current SIMILAR TO ESCAPE syntax is limited to scenarios that support adding and hitting the model in SQL statements, and other scenarios such as adding computable columns.
- The string literals including specific symbols need to be escaped by default and the escape character is `\`. For example, to match `\kylin` , it should be using `\\kylin`. For `SIMILAR TO` and `NOT SIMILAR TO` function, the functions use regex match and there is an escaped process. For example, for `\\\\kylin`, the result will be `true` when using `SIMILAR TO` to compare with `\kylin` and `\\kylin`.

This section introduces the logical operators supported by Apache Kylin. The values of logical propositions are TRUE, FALSE, and UNKNOWN. The following `boolean` refers to a logical proposition.

| Operator | Description | Syntax | Example |
| --- | --- | --- | --- |
| AND | Whether *boolean1* and *boolean2* are both TRUE | boolean1 AND boolean2 | Name ='frank' AND gender='M' |
| OR | Whether *boolean1* is TRUE or *boolean2* is TRUE | boolean1 OR boolean2 | Name='frank' OR Name='Hentry' |
| NOT | Whether *boolean* is not TRUE; returns UNKNOWN if *boolean* is UNKNOWN | NOT boolean | NOT (NAME ='frank') |
| IS FALSE | Whether *boolean* is FALSE; returns FALSE if *boolean* is UNKNOWN | boolean IS FALSE | Name ='frank' IS FALSE |
| IS NOT FALSE | Whether *boolean* is not FALSE; returns TRUE if *boolean* is UNKNOWN | boolean IS NOT FALSE | Name ='frank' IS NOT FALSE |
| IS TRUE | Whether *boolean* is TRUE; returns FALSE if *boolean* is UNKNOWN | boolean IS TRUE | Name ='frank' IS TRUE |
| IS NOT TRUE | Whether *boolean* is not TRUE; returns TRUE if *boolean* is UNKNOWN | boolean IS NOT TRUE | Name ='frank' IS NOT TRUE |

| Operator | Description | Syntax | Example |
| --- | --- | --- | --- |
| \| | Concatenates two strings or string columns | A \|\| B | First\_name \|\| Last\_name |

---

<a id="query-specification-functions"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/functions/ -->

<!-- page_index: 64 -->

# Basic Functions

Version: 5.0.2

> [!NOTE]
> If the parameter of the **POWER** function is a constant conversion, like *CAST(2 AS DOUBLE)*, it may fail to be recommended as computed column.

---

<a id="query-specification-window_function"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/window_function/ -->

<!-- page_index: 65 -->

# Window Functions

Version: 5.0.2

Window functions are a powerful tool that can simplify complex queries and improve performance. They allow you to perform calculations on a set of rows that are related to the current row, such as finding the sum or average of values in a specific range.

**Window functions are not supported for defining or recommending computed columns.**

The basic syntax for using a window function is as follows:

```sql
function(value) OVER window 
```

A window consists of three clauses:

- `partition by`: a group clause that defines the calculation range of the window function.
- `order by`: a sort clause that specifies the sorting method within the group after partition.
- `rows/range`: a window clause that determines a sliding data window within the group.


```sql
-- rows is a physical window that selects a fixed number of rows before and after  
-- the current row number, based on the `order by` clause. The result is independent  
-- of the current row's value, but rather its sorted row number. 
sum(columnA) rows between 1 preceding and 2 following; 
-- Explain: If the current row's `columnA` has a sorted row number of 3, this clause   
-- selects rows with sequence numbers between 2 and 5. 
 
 
-- range is a logical window that selects a fixed number of rows before and after  
-- the current row's value. The result is independent of the sorted row number, but  
-- rather the row's value. 
sum(columnA) range between 1 preceding and 2 following; 
-- Explain: If the current row's `columnA` value is 3, this clause selects rows with   
-- values between 2 and 5. 
 
```

If an **order by** clause is specified without a window clause, the default window clause is equivalent to **range between unbounded preceding and current row**.

1. **ROW\_NUMBER()**: Returning the position of the current row in its partition, the sequence numbers are not repeated.
2. **RANK()**: Returning the position of the current row in its partition, possibly with sequence gaps.
3. **DENSE\_RANK()**: Returning the position of the current row in its partition, with no sequence gaps.
4. **NTILE(value)**: Returning an integer ranging from 1 to value, dividing the partition as equally possible.
5. **FIRST\_VALUE(value)**: Returning value evaluated at the row that is the first row of the window frame.
6. **LAST\_VALUE(value)**: Returning value evaluated at the row that is the last row of the window frame.
7. **LAG(value, offset, default)**: Returning the forward offset of the current row in the partition. *value* represents the field as the column value, *offset* represents the number that needs to be looked up in the offset row forwards based on the current value, *default* represents the value returned by default when there is no eligible value, and null is returned by default if not filled.
8. **LEAD(value, offset, default)**: Returning the offset row backwards from the current row in the partition. *value* represents the column as the current value, *offset* represents the number that needs to be searched for the offset row backwards based on the current value, and *default* represents the value returned by default when there is no eligible value, and null is returned by default if not filled.

The following examples demonstrate the usage of window functions with the *P\_LINEORDER* table from the [sample dataset](#quickstart-tutorial). This dataset includes field descriptions for reference.

Using **RANK ()**, **DENSE\_RANK ()**, and **ROW\_NUMBER ()** in a single query to retrieve the first five orders with the least number of items purchased by each buyer. The query is as follows:

```sql
SELECT * 
FROM ( 
SELECT  
    ROW_NUMBER() OVER w AS ROW_NUM, 
    RANK() OVER w AS _RANK, 
    DENSE_RANK() OVER w AS D_RANK, 
    LO_ORDERKEY, 
    LO_CUSTKEY, 
    LO_QUANTITY, 
    LO_PARTKEY 
    FROM SSB.P_LINEORDER  
    WINDOW w AS (PARTITION BY LO_CUSTKEY ORDER BY LO_QUANTITY) 
    ) T 
WHERE ROW_NUM <= 5; 
```

![](assets/images/rank-and-drank-521f3112ae598702bb385bbfdd26f616_27b57b4b1e8be115.png)

For a buyer with id '1', the following ranking scenarios are observed:

- **row\_number() Function**

  - Orders with *LO\_QUANTITY* = 1 are ranked sequentially: 1, 2, 3, 4
  - The order with *LO\_QUANTITY* = 2 is ranked as 5
- **rank() Function**

  - Orders with *LO\_QUANTITY* = 1 are ranked equally: 1, 1, 1, 1
  - The order with *LO\_QUANTITY* = 2 is ranked as 5, resulting in sequence gaps
- **dense\_rank() Function**

  - Orders with *LO\_QUANTITY* = 1 are ranked equally: 1, 1, 1, 1
  - The order with *LO\_QUANTITY* = 2 is ranked as 2, with no sequence gaps

The orders of each buyer are divided into 3 groups according to the number of purchased products. In order to display the search results completely, the orders with the number of products greater than or equal to 48 are selected for grouping.

```sql
SELECT  
    NTILE(3) OVER w AS N_3, 
    LO_ORDERKEY, 
    LO_CUSTKEY, 
    LO_QUANTITY, 
    LO_PARTKEY 
FROM SSB.P_LINEORDER 
WHERE LO_QUANTITY >= 48 
WINDOW w AS (PARTITION BY LO_CUSTKEY ORDER BY LO_QUANTITY); 
```

![NTILE Response Examle](assets/images/ntile-599775ed2bb9c11d3dcd38262776d9b0_27361cf5784a0580.png)

Query the first order and the last order with the highest total price sorted by date.

```sql
SELECT  
    FIRST_VALUE(TOTAL1) OVER W AS FIRST_VALUE_A, 
    LAST_VALUE(TOTAL1) OVER W AS LAST_VALUE_A, 
    TOTAL1, 
    LO_ORDERDATE 
FROM ( 
	SELECT  
	    SUM(LO_ORDTOTALPRICE) AS TOTAL1, 
	    LO_ORDERDATE 
	FROM SSB.P_LINEORDER 
	GROUP BY LO_ORDERDATE 
	) T WINDOW W AS ( 
		ORDER BY LO_ORDERDATE ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING 
		) 
ORDER BY LO_ORDERDATE DESC 
```

![](assets/images/first-last-value-7251a6d4c7d4a13d225400a808ee80e1_ff3719d290bb3714.png)

Query the time of last order and next order based on current order.

```sql
SELECT 
  LO_ORDERKEY, 
  LO_CUSTKEY, 
  LO_QUANTITY, 
  LO_ORDERDATE, 
  LEAD(LO_ORDERDATE, 1) OVER W AS NEXT_DT, 
  LAG(LO_ORDERDATE, 1) OVER W AS LAST_DT 
FROM SSB.P_LINEORDER 
WINDOW W AS (PARTITION BY LO_CUSTKEY ORDER BY LO_ORDERDATE) 
```

![](assets/images/lead-lag-802d46a64ca3008385fc9c997af09b6b_80e4fd0e2d08a620.png)

---

<a id="query-specification-grouping_function"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/grouping_function/ -->

<!-- page_index: 66 -->

# Multi-Dimension Analysis

Version: 5.0.2

Users can utilize grouping functions to aggregate data by different keys within a single SQL statement. ROLLUP, CUBE, and GROUPING SETS are commonly used grouping and aggregate methods. CUBE and ROLLUP functions can be considered special cases of GROUPING SETS.

**Note that, in the current version, grouping functions are not supported as computed columns.**

In a result set, you sometimes need to aggregate columns A and B separately, and also aggregate the two columns together. The implementation method is often to use multiple UNION ALL statements. However, the GROUPING SETS function can use different grouping settings for aggregate queries at the same time. It can replace multiple UNION ALL statements, making SQL statements more convenient and efficient.

The GROUPING SETS function is often used in the GROUP BY clause. The expression is filled with the combination of dimensions that need to be grouped. For example, GROUPING SETS ((A, B), (C), ()) means to do aggregation with both columns A and B, aggregation with column C and aggregation with no grouping.

For example:

```sql
SELECT LO_CUSTKEY, LO_ORDERKEY, SUM(LO_ORDTOTALPRICE) AS PRICE 
FROM SSB.P_LINEORDER 
GROUP BY GROUPING SETS((LO_CUSTKEY,LO_ORDERKEY),(LO_ORDERKEY),()); 
 
-- the equivalent sql 
SELECT LO_CUSTKEY, LO_ORDERKEY, SUM(LO_ORDTOTALPRICE) AS PRICE 
FROM SSB.P_LINEORDER 
GROUP BY LO_CUSTKEY, LO_ORDERKEY 
 
UNION ALL 
SELECT NULL AS LO_CUSTKEY, LO_ORDERKEY, SUM(LO_ORDTOTALPRICE) AS PRICE 
FROM SSB.P_LINEORDER 
GROUP BY LO_ORDERKEY 
 
UNION ALL 
SELECT NULL AS LO_CUSTKEY, NULL AS LO_ORDERKEY, SUM(LO_ORDTOTALPRICE) AS PRICE 
FROM SSB.P_LINEORDER; 
 
```

![GROUPING SETS Function](assets/images/grouping-sets-function-d990b1022bf7f5640b9b80a5c6ecda88_e47f20740879ffc2.png)

In the results generated by grouping functions, `NULL` is used as a placeholder. As a result, it can be difficult to distinguish between `NULL` as a placeholder and `NULL` as part of the original data.

The `GROUPING` function helps differentiate between these two cases. It identifies whether a `NULL` value in the result set is a placeholder or actual data.

The columns involved in grouping can be passed into the `GROUPING` function. If the function returns `0`, the `NULL` value in the corresponding row comes from the original data. If it returns `1`, the `NULL` is a placeholder introduced by the grouping function.

For example:

```sql
SELECT  
	LO_CUSTKEY, 
	LO_ORDERKEY, 
	SUM(LO_ORDTOTALPRICE) AS PRICE, 
	GROUPING(LO_CUSTKEY) AS GC, 
	GROUPING(LO_ORDERKEY) AS GM 
FROM SSB.P_LINEORDER 
GROUP BY  
	GROUPING SETS((LO_CUSTKEY,LO_ORDERKEY),(LO_ORDERKEY),()); 
```

You can see that the result of the GROUPING function in both columns in the first row is 1, indicating that the NULL in the two columns LO\_CUSTKEY and LO\_ORDERKEY in this row are placeholders due to the GROUPING SETS function.

![](assets/images/grouping-c49f3782714c3cac205bd8a72fa9887d_0d7f391b428ae2d4.png)

`CUBE` performs group aggregation on all specified columns and ultimately provides the overall total aggregation result. The columns used in the expression are expanded into all possible combinations. For example, `GROUP BY CUBE (a, b, c)` is equivalent to `GROUPING SETS ((a, b, c), (a, b), (a, c), (b, c), (a), (b), (c), ())`.

`ROLLUP` performs group aggregation starting with the first column and ultimately provides the overall total aggregation. The columns in the expression are broken down into hierarchical combinations. For example, `GROUP BY ROLLUP (a, b, c)` is equivalent to `GROUPING SETS ((a, b, c), (a, b), (a), ())`.

For example:

```sql
SELECT 
  LO_CUSTKEY, 
  LO_ORDERKEY, 
  SUM(LO_ORDTOTALPRICE) AS PRICE 
FROM SSB.P_LINEORDER 
GROUP BY 
  ROLLUP(LO_CUSTKEY, LO_ORDERKEY); 
```

![ROLLUP Function](assets/images/rollup-function-1d6b2fa3838f39fa797ccbd3ceb691d6_359ce71aadb2fe68.png)

---

<a id="query-specification-bitmap_function"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/bitmap_function/ -->

<!-- page_index: 67 -->

# Bitmap Functions

Version: 5.0.2

Users can use bitmap functions to operate de-duplication based on bitmap. Then find the intersection of the result bitmaps.

Syntax: BITMAP\_UUID(column\_to\_count)

Description: Returning a string which points to a hidden serialized bitmap. The bitmap contains de-duplicated values and can be an input to other bitmap functions.

Parameters:

- `column_to_count`, the column to be calculated and applied on distinct value, required to be added as **Precise count distinct** measure.

For example:

```sql
-- Return a string which points to a hidden serialized bitmap. The bitmap result is  
-- the de-duplicated seller id set of online transactions on New Year's Day. The bitmap  
-- can be used as an input to other bitmap functions. 
 
select bitmap_uuid(LO_CUSTKEY)  
from SSB.P_LINEORDER  
where LO_ORDERDATE = date '2012-01-01' 
```

![](assets/images/bitmap-uuid-1-8bdb17d2b25999936f2f4d892433038e_d66d5c76e0df9198.png)

Syntax: INTERSECT\_BITMAP\_UUID(column\_to\_count, column\_to\_filter, filter\_value\_list)

Description: Returning a string which points to a hidden serialized bitmap. The bitmap contains the result of finding intersection based on filter column, and then de-duplicating based on count column.

Parameters:

- `column_to_count` , the column to be calculated and applied on distinct value required to be added as **Precise count distinct** measure.
- `column_to_filter`, the varied dimension.
- `filter_value_list`, the value of the varied dimensions listed in `array[]`, When `column_to_filter` is of type varchar, A single element in an array can map multiple values. By default, the '|' is split. You can set `kylin.query.intersect.separator` in `kylin.properties` to configure the separator, Can take value '|' or ',', default is '|'(Currently this parameter does not support the use of subquery results as parameters).

For example:

```sql
-- LSTG_FORMAT_NAME is a column of VARCHAR(4096) varied dimension. 
-- 
-- Return a string which points to a hidden serialized bitmap.  
-- The bitmap result is the de-duplicated seller id set who have transactions  
-- in either type 'FP-GTC' and 'Others', or type 'FP-non GTC' or 'Others'  
-- on New Year's Day. The bitmap can be used as an input to other bitmap functions. 
 
select intersect_bitmap_uuid( 
      LO_CUSTKEY, LO_SHIPMODE, 
      array['AIR', 'Others']) 
from SSB.P_LINEORDER 
```

![](assets/images/intersect-bitmap-uuid-1-6cbb0eef60b401144519a32b1f65741e_77b8291c45c0f04c.png)

When the data type of varied dimension is not varchar or integer, the values in 'filter\_value\_list' need to be explicitly cast, for example:

```sql
-- case 1 
select  
    intersect_bitmap_uuid(column_to_count,  
                          column_to_filter,  
                          array[cast(3.53 as double), cast(5.79 as double)])  
from TABLE_NAME; 
 
-- case 2 
select  
    intersect_bitmap_uuid(column_to_count,  
                          column_to_filter,  
                          array[TIMESTAMP'2012-01-02 11:23:45', TIMESTAMP'2012-01-01 11:23:45'])  
from TABLE_NAME; 
```

Syntax: intersect\_bitmap\_uuid\_v2(column\_to\_count, column\_to\_filter, filter\_value\_list, filter\_type)

Description: Return a string which points to a hidden serialized bitmap. The bitmap contains the result of finding intersection based on filter column, and then de-duplicating based on count column. Support Regexp in condition.

Parameters:

- `column_to_count` , the column to be calculated and applied on distinct value required to be added as **Precise count distinct** measure.
- `column_to_filter`, the varied dimension.
- `filter_value_list`, the value of the varied dimensions listed in `array[]`,
- `filter_type`, the data type is String, which identifies the filter mode. There are currently two optional values "RAWSTRING" and "REGEXP". When the parameter value is "RAWSTRING", the filtering mode is precise filtering. When `column_to_filter` is a Varchar type, A single element in the array can be mapped with multiple values. By default, it is separated by '|'. You can use `kylin.query.intersect.separator` to configure the separator. And only support configuration in the `kylin.properties` file. (currently this parameter does not support using the results of subqueries as parameters). When the parameter value is "REGEXP", the filtering mode is regular matching, and only the value of the regular expression in column\_to\_filter that can match the filter\_value\_list will be filtered.

For example:

```sql
-- LSTG_FORMAT_NAME is a column of VARCHAR(4096) varied dimension. 
-- 
-- Return a string which points to a hidden serialized bitmap.  
-- The regular expression can match 'FP-GTC', 'FP-non GTC' and 'Others',  
-- The bitmap result is the de-duplicated seller id set who have transactions  
-- in either type 'FP-GTC' and 'Others', or type 'FP-non GTC' or 'Others'  
-- on New Year's Day. The bitmap can be used as an input to other bitmap functions. 
 
select intersect_bitmap_uuid_v2( 
      LO_CUSTKEY, LO_SHIPMODE, 
      array['A*R', 'Other.*'], 'REGEXP') 
from SSB.P_LINEORDER 
```

![](assets/images/intersect-bitmap-uuid2-1-fa6443491b3fdd1c49bd5e88105eab11_43684eb8af36499a.png)

When the filter\_type is "RAWSTRING" and the data type of varied dimension is not varchar or integer, the values in 'filter\_value\_list' need to be explicitly cast, for example:

```sql
-- case 1 
select  
    intersect_bitmap_uuid_v2(column_to_count,  
                             column_to_filter,  
                             array[cast(3.53 as double), cast(5.79 as double)], 'RAWSTRING')  
from TEST_TABLE; 
 
-- case 2 
select  
    intersect_bitmap_uuid_v2(column_to_count,  
                             column_to_filter,  
                             array[TIMESTAMP'2012-01-02 11:23:45',  
                                   TIMESTAMP'2012-01-01 11:23:45'], 'RAWSTRING')  
from TEST_TABLE; 
```

Syntax: intersect\_count\_by\_col(Array[t1.c1,t2.c2 ...])

Description: Find the intersection of the serialized input bitmaps. Then return the distinct count.

Parameters:

- `t1.c1, t2.c2 ...`, the list of input columns. Each column points to a serialized bitmap hidden from users. Function `bitmap_uuid` and `intersect_bitmap_uuid` and `intersect_bitmap_uuid_v2` can return the bitmap.

For example:

```sql
-- Function `bitmap_uuid` and `intersect_bitmap_uuid` return two serialized bitmap.  
-- `intersect_count_by_col` then find the intersection on two bitmaps  
-- and return distinct count. 
 
select intersect_count_by_col(Array[t1.a1, t2.a2]) 
from (select bitmap_uuid(LO_CUSTKEY) as a1 from SSB.P_LINEORDER) t1, 
     (select intersect_bitmap_uuid(LO_CUSTKEY, LO_SHIPMODE, array['AIR', 'Others']) as a2 
      from SSB.P_LINEORDER) t2 
```

![](assets/images/intersect-count-by-col-1-2588f82071a6a68f49ecf04923305ead_359e278db63eb5dc.png)

**All the above functions don't support pushdown query**

---

<a id="query-specification-intersect_function"></a>

<!-- source_url: https://kylin.apache.org/docs/query/specification/intersect_function/ -->

<!-- page_index: 68 -->

# Intersect Functions

Version: 5.0.2

Users can use intersection function to calculate the value of the intersection of two data sets, with some same dimensions and one varied dimension, to analyze the retention or conversion rates.

kylin supports the following intersection function,

Syntax: intersect\_count(column\_to\_count, column\_to\_filter, filter\_value\_list)

Description: Returns the distinct count of the intersection of multiple result sets in different conditions

Parameters:

- `column_to_count`, the column to be calculated and applied on distinct count, required to be added as **Precise count distinct** measure
- `column_to_filter`, the varied dimension
- `filter_value_list`, the value of the varied dimensions listed in `array[]`, When `column_to_filter` is of type varchar, A single element in an array can map multiple values. By default, the '|' is split. You can set `kylin.query.intersect.separator` in `kylin.properties` to configure the separator, Can take value '|' or ',', default is '|'(Currently this parameter does not support the use of subquery results as parameters).

Example 1:

```sql
-- The result shows that there is no seller keeps trading constantly during this period. 
 
select LO_SHIPMODE, 
       intersect_count(LO_CUSTKEY, LO_ORDERDATE, array[date '1992-01-01'])    as first_day, 
       intersect_count(LO_CUSTKEY, LO_ORDERDATE, array[date '1992-01-02'])    as second_day, 
       intersect_count(LO_CUSTKEY, LO_ORDERDATE, array[date '1992-01-03'])    as third_day, 
       intersect_count(LO_CUSTKEY, LO_ORDERDATE,  
                       array[date '1992-01-01', date '1992-01-02'])           as retention_oneday, 
       intersect_count(LO_CUSTKEY, LO_ORDERDATE,  
                       array[date '1992-01-01', date '1992-01-02',  
                             date '1992-01-03'])                              as retention_twoday 
from SSB.P_LINEORDER 
where LO_ORDERDATE in (date '1992-01-01', date '1992-01-02', date '1992-01-03') 
group by LO_SHIPMODE 
```

![](assets/images/intersect-count-1-92206aa17ba311c4336c2e0bf44f7596_08b038adfac880e3.png)

Example 2:

```sql
select  
     intersect_count(LO_CUSTKEY, LO_SHIPMODE,  
                     array['RAIL|SHIP|TRUCK', 'TRUCK']) as test_column 
from SSB.P_LINEORDER 
```

![](assets/images/intersect-count-2-945e50b3d9963e4932e8becf045ba6af_58097da2a39ddb7b.png)

When the data type of varied dimension is not varchar or integer, the values in 'filter\_value\_list' need to be explicitly cast, for example:

```sql
-- case 1: 
select intersect_count(column_to_count,  
                       column_to_filter,  
                       array[cast(3.53 as double), cast(5.79 as double)])  
from TEST_TABLE; 
 
-- case 2: 
select intersect_count(column_to_count,  
                       column_to_filter,  
                       array[TIMESTAMP'2012-01-02 11:23:45', TIMESTAMP'2012-01-01 11:23:45'])  
from TEST_TABLE; 
 
```

Description: Returns the values of the intersection of multiple result sets in different conditions. If the returned result is large, it may cause the analysis page browser to crash.

Syntax: intersect\_value(column\_to\_count, column\_to\_filter, filter\_value\_list)

Parameters:

- `column_to_count`, the column to be calculated and applied on distinct value required to be added as **Precise count distinct** measure. **And only columns of type tinyint, smallint, or integer are supported**.
- `column_to_filter`, the varied dimension
- `filter_value_list`, the value of the varied dimensions listed in `array[]`, When `column_to_filter` is of type varchar, A single element in an array can map multiple values. By default, the '|' is split. You can set `kylin.query.intersect.separator` in `kylin.properties` to configure the separator, Can take value '|' or ',', default is '|'(Currently this parameter does not support the use of subquery results as parameters).

Example 1:

```sql
-- Fact table `SSB.P_LINEORDER` simulates the online transaction data.  
-- And data type of `LO_CUSTKEY` column is `integer`. The following query  
-- can return the ids of sellers who are trading day by day during 1992.01.01 to 1992.01.03.		 
   
-- The result shows that set of keeping trading constantly's sellerId during this period. 
 
select LO_SHIPMODE,	 
intersect_value(LO_CUSTKEY, LO_ORDERDATE, array[date'1992-01-01']) as first_day, 
intersect_value(LO_CUSTKEY, LO_ORDERDATE, array[date'1992-01-02']) as second_day, 
intersect_value(LO_CUSTKEY, LO_ORDERDATE, array[date'1992-01-03']) as third_day, 
intersect_value(LO_CUSTKEY, LO_ORDERDATE, array[date'1992-01-01',date'1992-01-02']) as retention_oneday, 	 
intersect_value(LO_CUSTKEY, LO_ORDERDATE, array[date'1992-01-01',date'1992-01-02',date'1992-01-03']) as retention_twoday 	 
from SSB.P_LINEORDER 
where PART_DT in (date'1992-01-01',date'1992-01-02',date'1992-01-03') 
group by LO_SHIPMODE 
```

![](assets/images/intersect-value-1-5dfb41e703b05f7a63db42b351b81cb4_17ffb4707028d606.png)

Example 2:

```sql
select  
    intersect_count(LO_CUSTKEY, LO_SHIPMODE,  
                    array['RAIL|SHIP|TRUCK', 'TRUCK']) as test_column 
from SSB.P_LINEORDER 
```

![](assets/images/intersect-value-2-5a022bc863b9b79d4f0776091a1e0b5d_922ef2d7a339a5ba.png)

When the data type of varied dimension is not varchar or integer, the values in 'filter\_value\_list' need to be explicitly cast, for example:

```sql
-- case 1 
select intersect_value(column_to_count, column_to_filter,  
                       array[cast(3.53 as double), cast(5.79 as double)])  
from TEST_TABLE 
   
-- case 2 
select intersect_value(column_to_count, column_to_filter,  
                       array[TIMESTAMP'2012-01-02 11:23:45', TIMESTAMP'2012-01-01 11:23:45'])  
from TEST_TABLE; 
```

Syntax: intersect\_count\_v2(column\_to\_count, column\_to\_filter, filter\_value\_list, filter\_type)

Description: Returns the distinct count of the intersection of multiple result sets in different conditions. Support Regexp in condition.

Parameters:

- `column_to_count`, the column to be calculated and applied on distinct count, required to be added as **Precise count distinct** measure
- `column_to_filter`, the varied dimension
- `filter_value_list`, the value of the varied dimensions listed in `array[]`,
- `filter_type`, the data type is String, which identifies the filter mode. There are currently two optional values "RAWSTRING" and "REGEXP". When the parameter value is "RAWSTRING", the filtering mode is precise filtering. When `column_to_filter` is a Varchar type, A single element in the array can be mapped with multiple values. By default, it is separated by '|'. You can use `kylin.query.intersect.separator` to configure the separator. And only support configuration in the `kylin.properties` file. (currently this parameter does not support using the results of subqueries as parameters). When the parameter value is "REGEXP", the filtering mode is regular matching, and only the value of the regular expression in column\_to\_filter that can match the filter\_value\_list will be filtered.

For example:

```sql
select intersect_count_v2( 
    LO_CUSTKEY, LO_SHIPMODE,  
    array['R*L', 'TRU.*'], 'SHIP') 
from SSB.P_LINEORDER 
```

![](assets/images/intersect-count2-1-388cb29dfffc188a9c5fdba73622c875_6425add500d4e05c.png)

When the filter\_type is "RAWSTRING" and the data type of a varied dimension is not varchar or integer, the values in 'filter\_value\_list' need to be explicitly cast, for example:

```sql
-- case 1 
select intersect_count_v2(column_to_count, column_to_filter,  
                          array[cast(3.53 as double), cast(5.79 as double)], 'RAWSTRING')  
from TEST_TABLE 
 
 
-- case 2 
select intersect_count_v2(column_to_count, column_to_filter,  
                          array[TIMESTAMP'2012-01-02 11:23:45', TIMESTAMP'2012-01-01 11:23:45'], 'RAWSTRING')  
from TEST_TABLE; 
```

Syntax: intersect\_value\_v2(column\_to\_count, column\_to\_filter, filter\_value\_list, filter\_type)

Description: Returns the values of the intersection of multiple result sets in different conditions. If the returned result is large, it may cause the analysis page browser to crash. Support Regexp in condition.

Parameters:

- `column_to_count`, the column to be calculated and applied on distinct value required to be added as **Precise count distinct** measure.
  **Only when type of column is one of integer family(tinyint、smallint、integer、bigint) and override model properties `kylin.query.skip-encode-integer-enabled=true`, the values returned is actual. Otherwise, encoded value will be returned.**
- `column_to_filter`, the varied dimension
- `filter_value_list`, the value of the varied dimensions listed in `array[]`,
- `filter_type`, the data type is String, which identifies the filter mode. There are currently two optional values "RAWSTRING" and "REGEXP". When the parameter value is "RAWSTRING", the filtering mode is precise filtering. When `column_to_filter` is a Varchar type, A single element in the array can be mapped with multiple values. By default, it is separated by '|'. You can use `kylin.query.intersect.separator` to configure the separator. And only support configuration in the `kylin.properties` file. (currently this parameter does not support using the results of subqueries as parameters). When the parameter value is "REGEXP", the filtering mode is regular matching, and only the value of the regular expression in column\_to\_filter that can match the filter\_value\_list will be filtered.

For example:

```sql
select intersect_value_v2( 
    LO_CUSTKEY, LO_SHIPMODE,  
    array['R*L', 'TRU.*'], 'SHIP') 
from SSB.P_LINEORDER 
```

![](assets/images/intersect-value2-1-ee6694708347ca72b4dc410bb41dad7b_06c900a4d9477ecc.png)

When the filter\_type is "RAWSTRING" and the data type of varied dimension is not varchar or integer, the values in 'filter\_value\_list' need to be explicitly cast, for example:

```sql
-- case 1 
select intersect_value_v2(column_to_count, column_to_filter,  
                          array[cast(3.53 as double), cast(5.79 as double)], 'RAWSTRING')  
from TEST_TABLE; 
 
-- case 2 
select intersect_value_v2(column_to_count, column_to_filter,  
                          array[TIMESTAMP'2012-01-02 11:23:45', TIMESTAMP'2012-01-01 11:23:45'], 'RAWSTRING')  
from TEST_TABLE; 
```

- All the above functions don't support pushdown query
- All the above functions don't support detailed index answers (even with the switch kylin.query.use-tableindex-answer-non-raw-query = true)

---

<a id="query-tuning-data_skipping"></a>

<!-- source_url: https://kylin.apache.org/docs/query/tuning/data_skipping/ -->

<!-- page_index: 69 -->

# Data Skipping

Version: 5.0.2

Starting from Kylin 5.0, we support the calculation of the dimension value range (maximum and minimum) of all dimensions when building the Segment, so we can prune segment during queries, reducing the scanning range of the segment to optimize some query performance.

This optimization is enabled by default. Under normal circumstances, you do not need to pay attention to this optimization. In some extreme cases, system-level or project-level shutdown is supported.

To disable it on the system level, configure the parameters in `$KYLIN_HOME/conf/kylin.properties` . To disable it on project level, add the configuration in **Setting -> Advanced Settings -> Custom Project Configuration**.

`kylin.storage.columnar.dimension-range-filter-enabled=false`

1. Currently, only the query filter conditions including `=, in, >, >=, <, <=, and, or` support pruning segment. Filters including `not, is null` are not supported.
2. This optimization will slightly increase the building time, but it is basically negligible compared to the total building time.
3. The historical data that has been built will not use this optimization. If you want the historical data to apply this optimization, you need to refresh the Segment.
4. The multi-level partition models are not supported.

---

<a id="query-tuning-model_priority"></a>

<!-- source_url: https://kylin.apache.org/docs/query/tuning/model_priority/ -->

<!-- page_index: 70 -->

# Query Specific Model

Version: 5.0.2

Query Hint is an advanced feature that enables users to specify **model priority**. When multiple models can answer a query, Kylin automatically selects the best one. However, users can override this default behavior by using a model priority hint in their SQL queries, allowing them to choose specific models for specific queries.

```sql
SELECT /*+ MODEL_PRIORITY(model1, model2) */ col1, col2 
from table; 
```

The hint starts with `/*+` and ends with `*/`. And the hint must be placed right after the `SELECT` clause.

`MODEL_PRIORITY(model1, model2, ...)` specifies the model priorities, `MODEL_PRIORITY(...)` accept a list of model names with descending priority. The model that doesn't appear in the hint will be assigned with the lowest priority.
The model priority hint will be valid for the entire query. Only the first hint occurred in the SQL will be valid.

During the model matching, if multiple model is capable to answer the query. kylin will use the model with the highest priority specified in the model priority hint

Supported starts from kylin 5.0

```sql
SELECT /*+ MODEL_PRIORITY(model1, model2) */ col1, col2  
from table; 
```

If both model1 and model2 is capable to answer the query, model1 will be the chosen for this query.

---

<a id="query-tuning-sum_expression"></a>

<!-- source_url: https://kylin.apache.org/docs/query/tuning/sum_expression/ -->

<!-- page_index: 71 -->

# Sum Expression

Version: 5.0.2

Sum(expression) is a common usage in SQL and is often needed by various data analysis scenarios.

In the previous versions, table index or computed column is required for sum(expression) to work. Since v5, Kylin can answer some kind of sum(expression) using model.

This feature is off by default. To enable it, please set the configuration in `$KYLIN_HOME/conf/kylin.properties`.

```properties
kylin.query.convert-sum-expression-enabled=true 
```

Currently, four kinds of sum (expression) usages are supported, namely

- sum(case when)
- sum(column\*constant)
- sum(constant)
- sum(cast(case when))

We will use the sample dataset to introduce the usage. Read more about the [Sample Dataset](#quickstart-tutorial).

**sum(case when) function**

For example:

```sql
select 
    sum(case when LO_ORDERPRIOTITY='1-URGENT' then LO_ORDTOTALPRICE else null end) 
from SSB.LO_LINEORDER 
```

In order to run this SQL, set your model as below in addition to enable sum(expression):

- Define all columns in the `when` clause as dimensions, like the `LO_ORDERPRIOTITY` in this example.
- Define all columns in the `then` clause as Sum measure, like the `sum(LO_ORDTOTALPRICE)` in this example.

Then, the model will be able to run the above SQL.

**sum(column\*constant) function**

For example:

```sql
select sum(LO_ORDTOTALPRICE * 3) from SSB.LO_LINEORDER 
```

In order to run this SQL, set your model as below in addition to enable sum(expression):

- Define the column in the `sum` function as Sum measure, like the `sum(LO_ORDTOTALPRICE)` in this example.

Then, the model will be able to run the above SQL.

**sum(constant) function**

For example:

```sql
select sum(3) from P_LINEORDER 
```

In order to run this SQL, just enable the sum(expression) feature. No other setting on model is needed.

**sum(cast(case when)) function**

For example:

```sql
select  
    sum(cast((case when LO_ORDERPRIOTITY='1-URGENT' then LO_ORDTOTALPRICE else null end) as bigint))  
from SSB.P_LINEORDER 
```

In order to run this SQL, set your model as below in addition to enable sum(expression):

- Define all columns in the `when` clause as dimensions, like the `ORDERPRIOTITY` in this example.
- Define all columns in the `then` clause as Sum measure, like the `sum(ORDTOTALPRICE)` in this example.

Then, the model will be able to run the above SQL.

1. Due to the complexity of `null` value, `sum(column+column)` and `sum(column+constant)` are not supported yet. If you need use the above syntax, please use computed column or table index.
2. In the current version, `topN` is not supported to use together with `sum(case when)`. `count(distinct)`, `collect_set`, `percentile` can be used with `sum(case when)`，but they can not be answered by single index.

---

<a id="query-tuning-count_distinct_expr"></a>

<!-- source_url: https://kylin.apache.org/docs/query/tuning/count_distinct_expr/ -->

<!-- page_index: 72 -->

# Count-distinct Expression

Version: 5.0.2

In some data analysis scenarios, you maybe encounter the SQL usage of Count Distinct Case When Expression.

In previous versions, if you want to speed up such queries through model pre-calculation, you need to set Case When Expression as a computable column, and then set the Count Distinct Computed Column metric to answer such queries.

Starting from Kylin V5, we have provided special optimizations for this type of query, allowing users to only set the Count (Distinct Column) measure, the system uses the pre-calculated results and adds some Case When Expression online calculations to fully answer the query, reducing the complexity of model settings and improving user experience.

1. Enable optimization

This function is disable by default, and it can be enabled on the system or project level.

To enable it on the system level, configure the parameters in `$KYLIN_HOME/conf/kylin.properties` . To enable it on project level, add the configuration in **Setting-Advanced Settings-Custom Project Configuration**.

```sql
kylin.query.convert-count-distinct-expression-enabled=true 
```

2. Supported Count Distinct Case When Expression syntax

```sql
count(distinct case when {condition} then {column} else null end) 
```

Notice:

a. `{condition}` is dimension column expression, for example `cal_dt = '2012-01-01'`.

b. The `{column}` must be set to the `count (distinct column)` measure.

c.When selecting the error option in the function parameter, the return type must be selected: precisely, otherwise the optimization of this syntax cannot be triggered

After the function is enabled, queries that conform to the above grammar can be answered by indexes that include **dimension column** and `count(distinct column)`**measure** in the `condition` expression.

Example:

```sql
count(distinct (case when cal_dt = date'2012-01-01' then price else null end)) 
```

It can be answered by indexes including `cal_dt` dimension and `count(distinct price)` measure.

1. Else can only be with null, constants are not supported temporarily, such as `case when ... then column1 else 1 end`.
   Starting from Kylin 5.0 version, after else can be cast(null as `type`), such as `case when ... then column1 else cast(null as double) end`.
   It should be noted that `type` should be as close as possible to `column1` The type is the same or the same category,
   otherwise it may not conform to the sql syntax and an error will be reported, or this function cannot be applied.
   The major category refers to the same numeric type, date type, Boolean type, etc.
2. Only one pair of `when .. then ..` is supported after case, and multiple pairs are not supported for now, such as `case when .. then column1 when ... then column2 else null end`.

---

<a id="query-tuning-query_enhanced"></a>

<!-- source_url: https://kylin.apache.org/docs/query/tuning/query_enhanced/ -->

<!-- page_index: 73 -->

# Equivalent Semantics Query

Version: 5.0.2

By default, in Kylin, the relationship between tables in the query SQL must be consistent with the relationship between the fact tables and dimension tables defined in the model, that is, the model of `Left Join` cannot answer the query of `Inner Join`.

But in some cases, part of `Left Join` queries can be semantically equivalently transformed into `Inner Join` queries, so we provide configuration parameters that allow users to use `Left Join` model to answer equivalent semantics `Inner Join` query.

The configuration parameters starts to take effect from version of Kylin 5.0, which is closed by default.

`[Table A] Left Join [Table B] Inner Join [Table C]` is semantically equivalent to `[Table A] Inner Join [Table B] Inner Join [Table C]`.

The reason is that when `Inner Join` is performed after `Left Join`, the rows that do not match the last right table will be filtered out, so the above two expressions are semantically equivalent.

Using the `kylin.query.join-match-optimization-enabled=true` configuration, Kylin can support `Left Join` models to answer the above equivalent semantic `Inner Join` queries.

The model is defined as `KYLIN_SALES Left Join KYLIN_ACCOUNT Inner Join KYLIN_COUNTRY`

The SQL is as follows:

```sql
select kylin_country.name 
from kylin_sales inner join kylin_account on kylin_sales.buyer_id = kylin_account.account_id 
inner join kylin_country on kylin_account.account_country = kylin_country.country 
```

The above model can answer this SQL.

The model is defined as `[Table A] Left Join [Table B] Left Join [Table C] Inner Join [Table D] Left Join [Table E]`

The SQL is as follows:
`[Table A] Inner Join [Table B] Inner Join [Table C] Inner Join [Table D] Left Join [Table E]`

The above model can answer this SQL.

SQL has the following characteristics: `[Table A] Left Join [Table B]` and any column of `[Table B]` in the filter condition has a non-null constraint, then the SQL semantics is equivalent to `[Table A] Inner Join [Table B]`.

Using `kylin.query.join-match-optimization-enabled=true` configuration, Kylin can support `Left Join` model to answer the above equivalent semantic `Inner Join` query.

The columns with non-null constraints need to meet the condition: they should be `isNotNull` filter conditions, `isNotNull` corresponds to common comparison operators: `=`, `<>`, `>`, `<`, `<=`, `>=`, `like`, `In`, `not like`, `not in` etc.

`isNull` filter conditions like `IS NULL` do not have non-null constraint.

At the same time, the filter conditions `IS DISTINCT FROM` and `CASE WHEN` is not supported for the time being, thus will be automatically ignored. See the known limitation 1.

The model is defined as: `TEST_ACCOUNT left join TEST_ORDER left join TEST_ACCOUNT`

There are SQL as follows, which can hit the above model because there is a non-null constraint filter condition.

```sql
select SUM(a.ITEM_COUNT) as SUM_ITEM_COUNT 
from TEST_KYLIN_FACT a 
left join TEST_ORDER b on a.ORDER_ID = b.ORDER_ID 
inner join TEST_ACCOUNT c on b.BUYER_ID = c.ACCOUNT_ID 
where c.ACCOUNT_COUNTRY ='CN' and (c.ACCOUNT_COUNTRY like'%US' or c.ACCOUNT_COUNTRY is null) 
```

The model is defined as: `[Table A] inner join [Table B]`

There are SQL as follows that can hit this model:

```sql
A left join B where B.nonfk = '123' and B.col1 in ('ab','ac') 
A left join B where A.col is null and B.col1 like 'xxx' 
A left join B where B.col between 100 and 100000 
A left join B where A.fk is null and B.col1 ='something' 
A left join B where b.col ='something' and (b.col ='xxx' or b.col is null) 
A left join B where abs(b.col) = 123 
A left join B where floor(b.col) = 123 
```

The following SQL cannot hit this model:

```sql
A left join B where B.col1 = 'xx' or A.col2 = 'yy' 
A left join B where B.col1 = 'xx' or B.col2 is null 
```

Now there is the model `[Table A] Left Join [Table B] left join [Table C]`.

The following SQL is as follows, you can hit this model:

```sql
A inner join B inner join C where C.col ='abc' 
```

The reason is that the columns in table C have non-null constraints, so the query can be equivalent to:

```sql
A LEFT_OR_INNER join B LEFT_OR_INNER join C where C.col ='abc' 
```

Scene three is a mixture of scene one and scene two.

1. For Scene two, judgment of non-null constraints don't include `NOT SIMILAR TO`, `CASE WHEN` expressions.
2. Also for scene two, judgment of non-null constraints don't include aggregation functions like `HAVING SUM(PRICE)>0`.

---

<a id="query-push_down"></a>

<!-- source_url: https://kylin.apache.org/docs/query/push_down/ -->

<!-- page_index: 74 -->

# Pushdown

Version: 5.0.2

Kylin integrates a Smart Pushdown engine which works SQL on Hadoop engine like SparkSQL.

For queries which cannot be answered by Kylin, they can be routed into Pushdown Query Engine when necessary.

Kylin uses pre-calculation instead of online calculation to achieve sub-second query latency on big data. In general, the model with pre-calculated data is able to serve the most frequently-used queries. But if a query is beyond the model's definition, the system will route it to the Kylin smart pushdown engine. The embedded pushdown engine is Spark SQL.

>
> [!NOTE]
> : In order to ensure data consistency, query cache is not available in pushdown.

Kylin 5.x has an embedded Spark engine, so no 3rd party dependency is required to enable query pushdown. You can query on source tables directly after loading the data source (at least one table loaded).

By default, the query pushdown is turned on in a new project. If you need to turn it off, there are two ways:

**At project level:** As shown below, click the left navigation bar **Setting** tab and in the **Basic Settings -> Pushdown Setting** part, you can turn off the Pushdown Engine in the red frame. If this setting has never been modified at project level, it takes instance level setting as default value.

![Turn off Query Pushdown at Project Level](assets/images/pushdown-8fb5ca04cc407cc948a16496aef30522_6e599ab67d2d9af9.png)

**At instance level:** Query pushdown is turned on by default, which corresponds to the configuration item `kylin.query.pushdown-enabled=true` in the configuration file `${KYLIN_HOME}/conf/kylin.properties`. To turn it off, add `kylin.query.pushdown-enabled=false` into the configuration file.

If you submit the query when there is no online model, the query pushdown will work. If your data source is HIVE, the query pushdown will show the result from HIVE, such as: `Answered By: HIVE`.

>
> [!TIP]
> : If the query answered by models, the query history will be displayed as: `Answered By: {model_name}`.

There are 2 things to notice when pushdown query has filter for `float` type column of datasource: literal type and precision.

- Literal Type: Specify literal data type manually with the same type as column like `'123.4f'`, for example:

```sql
SELECT * FROM table1 WHERE col1 > '123.4f' 
```

- Precision: Do not exceed the precision range of `float / double` type

For example, datasource table `table1` has `float` type column `col1`, data in table:

```text
|-------| | col1  | |-------| | 1.2   | | 5.67  | | 123.4 | | 130.1 | |-------|
```

A pushdown query which is:

```sql
SELECT * FROM table1 WHERE col1 > 123.4 
```

Will get the following result:

```text
|-------| 
| col1  | 
|-------| 
| 123.4 | 
| 130.1 | 
|-------| 
```

As you can see the line `123.4` appears in the result even the `WHERE` filter uses the operation grater than (`>`).

The reason causes it is the two different data types between two sides of the filter operator, and it hits a rule of Spark optimizer:

`col1` is the type of `float`, and lteral value `123.4` is the type of `double` by default.

And this Spark optimizer will transform the filter in such a way (Notice the operator `>=` after transformation):

```text
cast(col1 to double) > 123.4  ===>  col1 >= cast(123.4 to float) 
```

That causes the line `123.4` return.

The correct way is to specify **literal type** manually like the following:

```sql
SELECT * FROM table1 WHERE col1 > '123.4f' 
```

And the result looks good now:

```text
|-------| 
| col1  | 
|-------| 
| 130.1 | 
|-------| 
```

For **literal precision**, check out the following pushdown query:

```sql
SELECT * FROM table1 WHERE col1 > '123.3999f' 
```

Which returns a correct result:

```text
|-------| 
| col1  | 
|-------| 
| 123.4 | 
| 130.1 | 
|-------| 
```

But the next pushdown query which has an unsuitable numeric precision may cause an unexpected result:

```sql
SELECT * FROM table1 WHERE col1 > '123.39999999999f' 
```

The unexpected result:

```text
|-------| 
| col1  | 
|-------| 
| 130.1 | 
|-------| 
```

---

<a id="query-history-query_history"></a>

<!-- source_url: https://kylin.apache.org/docs/query/history/query_history/ -->

<!-- page_index: 75 -->

# Guide

Version: 5.0.2

All the queries that you executed in Kylin will be saved in query history, you can check it out on the left side navigation bar **Query -> History**.
This page saves the basic information of queries, such as query time, SQL statement, query user, etc. This helps you to record query behaviors, which enables you to better manage and optimize the models. This chapter will presents you the content of query history page.

1. Before introducing **Query History** page, we recommend you to execute several SQL statements.
2. Take the model we built in the quick start as an example. After you complete the quick start, and all the jobs in **Monitor -> Job** are finished, you can execute the following queries in **Query -> Insight** page.

- Query 1：query total revenue.


```sql
-- column *LO_REVENUE* 's SUM measure exists. 
 
select SUM(LO_REVENUE) as TOTAL_REVENUE from SSB.P_LINEORDER 
```

- Query 2：query total order price.


```sql
-- column *LO_ORDTOTALPRICE* 's SUM measure not exists. 
 
select SUM(LO_ORDTOTALPRICE) from SSB.P_LINEORDER 
```

- Query 3：query name of commodities.


```sql
-- this is a wrong query，because column *P_NAME* does not exist in table *P_LINEORDER*. 
 
select P_NAME from SSB.P_LINEORDER 
```

Please enter the query history page by clicking **Query -> History** in the navigator bar, after executing the above SQL statements, you will see the following content.

![Query History](assets/images/history1-329ed2f3de41cea74b0c118766a3fbc6_b873b6eda71887b7.png)

Each line in the picture is a query history record. The meaning of the columns are as follows:

- **Start time**: The time the query was submitted.
- **Duration**: The time taken to complete the query. If the query fails, it is displayed as blank.
- **Query ID**: A unique ID number for each query, which is an automatically generated sequence number.
- **SQL Statement**: SQL statement that was executed.
- **Answered By**: There are four query objects. The blue name indicates the query hit model (index group). As shown in the diagram, the model name is *test\_model\_name1578277468526*, *HIVE* indicates that the query is pushed down to Hive, and *CONSTANTS* indicates Query constant, blank indicates that the query failed.

  There are four types of query objects that a query hits： All Models, HIVE, CONSTANTS, Model Name.

  - All Models： Indicates that the query hits the model
  - Hive： Indicates that the query is pushed down to Hive
  - CONSTANTS： Indicates query constant
  - Model Name： Represents the name of the model hit by the query
- **Query Status**: There are two query statuses. Queries that hit the model and push down show *Succeeded* and queries that have syntax errors, unsupported syntax, and timeouts show *Failed*.
- **Query Node**: The hostname : port of query node.
- **Submitter**: User who submits the query to Kylin.
- **Actions**: Download the query diagnostic package.

When you click on the icon to the left of a query, the execution details of the query will be displayed, as shown below:

![Query Execution Detail](assets/images/history2-6b71e86e3f78733e16a08e3dfab6e408_4995addf98d91ac0.png)

On the left is the SQL statement, you can copy and paste and then query. The fields on the right have the following meanings:

- **Query ID**: A unique ID number for each query, which is an automatically generated sequence number.
- **Duration**: The time taken to complete the query. If the query fails, it is displayed as *Failed*. When you need to optimize for slow queries, you should analyze the query's specific execution steps and locate the reasons. It would help if you hovered the mouse over the duration to see the current query's detailed execution steps and duration.
- **Answered By**: The entity who answered the query.
- **Index ID**: The index who answered the query.
- **Total Scan Count**: Total scanned lines of the query.
- **Total Scan Bytes**: Total scanned bytes of the query.
- **Result Row Count**: Total lines of the query result.
- **If Hit Cache**: Whether the query hits the cache.
- **Cache Type**: When the query hits the cache, it displays the type of cache hit. `EHCACHE` stands for EHCACHE cache, `REDIS` stands for REDIS distributed cache.

When you click on the error details to the right of a query failure, the exception details of that query are displayed，as shown below:

![Query Exception Message](assets/images/history5-9c83704d2eeed7462113bed4d51d63bc_383ef9ea17eeb63b.png)

>
> [!NOTE]
> : When SQL does not wrap, only the first 100 lines of SQL can be seen in the query execution details. When SQL wraps, the details display the first 2000 characters. You can click the copy button in the upper right corner of the SQL statement box to copy the complete SQL statement.

Kylin uses the built-in RDBMS to save information about queries. You can refer to all fields and meanings related to query history in the appendix [Query History Fields Table](#query-history-query_history_fields).

In order to ensure the read and write performance of the query history and database stability, Kylin sets a default retention limit for the query history:
You can set the query history retention limit in the **kylin.properties** file.

```shell
### default total number of retained records 
kylin.query.queryhistory.max-size=10000000 
 
### default number of retained records in one project 
kylin.query.queryhistory.project-max-size=1000000 
 
### total retention time 
kylin.query.queryhistory.survival-time-threshold=30 
```

The query history can be exported as a csv file, as shown in the figure below, the export result is the filtered data.
![Export query history](assets/images/history3-6046edbc0ed1656969f85b93bc8e2e8f_23e30016a94e864c.png)

You can also export the sql in the query history as a text file separately, as shown in the figure below, the export result is also the filtered data.
![Export SQL](assets/images/history4-8b2cc01a01a00edd5cd75cff4780122e_0ff76643f5aae070.png)

Query history support configuration export upper limit, the default value is 100000.

```shell
kylin.query.query-history-download-max-size=100000 
```

---

<a id="query-history-query_history_fields"></a>

<!-- source_url: https://kylin.apache.org/docs/query/history/query_history_fields/ -->

<!-- page_index: 76 -->

# Table Schema

Version: 5.0.2

Starting from Kylin 5.0, the system uses RDBMS to store query history. And each metadata will store two tables related to query history:

- *query\_history* : information for each query
- *query\_history\_realization* : each index that hit by query

| Field Name | Description |
| --- | --- |
| id | auto increment primary key |
| cache\_hit | whether the query hits the cache |
| duration | duration of query execution |
| engine\_type | four query objects, the blue name indicates the query hits model (index group), *HIVE* indicates that the query is pushed down to Hive, *CONSTANTS* indicates the query constant, and the blank indicates that the query failed. |
| error\_type | error message when error occurs during query execution |
| server | if hostname exists, use hostname of query node, otherwise use IP address of query node |
| index\_hit | whether the query hits index or not |
| is\_agg\_index\_used | whether the query hits the aggregate index or not |
| is\_table\_index\_used | whether the query hits table index or not |
| is\_table\_snapshot\_used | whether the query hits the dimension table |
| month | the month in which the query is submitted, which is needed to count the history of the query by month. |
| query\_first\_day\_of\_month | the initial time of the month in which the query time is located. This field is required when statistically querying the history by month |
| query\_first\_day\_of\_week | the initial time of the week in which the query time is located. This field is required when statistically querying the history by month |
| query\_day | the initial time of the day in which the query time is located. This field is required when statistically querying the history by month |
| query\_id | query identity |
| query\_status | two query statuses, *SUCCEEDED* indicates that the query was successful, *FAILED* indicates that the query was abnormal |
| query\_time | query start time |
| realizations | a string concatenated by the model ID number, Layout ID number, and index type，which format is *modelId#layoutId#indexType* |
| result\_row\_count | number of query results |
| sql\_text | SQL statement that was submitted |
| sql\_pattern | the sql pattern of SQL statement that was submitted . This field is needed when sql is accelerated. |
| submitter | user who submits the query |
| total\_scan\_bytes | total scanned lines of the query |
| total\_scan\_count | total scanned bytes of the query |
| project\_name | project name |
| reserved\_field\_1 | reserved field, currently unused |
| reserved\_field\_2 | reserved field, currently unused |
| reserved\_field\_3 | This field is used to record the reason why the index cannot be recommended |
| reserved\_field\_4 | reserved field, currently unused |

| Field Name | Description |
| --- | --- |
| query\_time | unix timestamp of query start time (when query start to execute) |
| duration | duration of query execution |
| index\_type | three index types, *Table Index* for table index, *Agg Index* for aggregate index, and *Table Snapshot* for dimension table |
| layout\_id | ID of layout |
| model | ID of model |
| query\_id | ID of query |
| project\_name | Project name |

---

<a id="query-async_query"></a>

<!-- source_url: https://kylin.apache.org/docs/query/async_query/ -->

<!-- page_index: 77 -->

# Asynchronous Query

Version: 5.0.2

Asynchronous query supports users to execute SQL queries asynchronously and provides a more efficient way to export data. For example, if the result set of a SQL query
Too large (million results) or SQL execution time is too long, through asynchronous query, the query result set can be exported efficiently to realize self-service data retrieval
Various application scenarios.

Currently, asynchronous query only supports calling REST API. For how to use asynchronous query API, please read-[Asynchronous Query API](#restapi-async_query_api).

Asynchronous query supports the following configuration in `kylin.properties`:

- `kylin.query.async.result-retain-days=7d`: The retention time of asynchronous query results on HDFS. The default is 7 days, that is, asynchronous query results and related files older than 7 days will be cleaned up.

In general, the same cluster queue can be used for asynchronous query and normal query. In some advanced scenarios, if you want to prevent asynchronous queries from affecting ordinary queries, you can deploy a separate queue for asynchronous queries. The specific configuration method is as follows:

1. Enable asynchronous query to deploy a separate cluster queue setting. Set `kylin.query.unique-async-query-yarn-queue-enabled` to `true`. Support project-level configuration and system-level configuration. The priority of project-level configuration is higher than system-level configuration. If neither is configured, asynchronous query and normal query use the same cluster queue.
2. Specify the queue used for asynchronous queries. Three levels are supported for designation, the priority from high to low is as follows:

   - Query level, specified by API request parameter `spark_queue`
   - Project level, specified by setting `kylin.query.async-query.spark-conf.spark.yarn.queue`
   - System level, specified by setting `kylin.query.async-query.spark-conf.spark.yarn.queue` in the configuration file `/conf/kylin.properties`
   >
> [!TIP]
> : If none of the three are configured, the default queue is `default`

3. Set configuration: `kylin.query.async-query.submit-hadoop-conf-dir=$KYLIN_HOME/async_query_hadoop_conf`
4. Put the hadoop configuration of the asynchronous query cluster into the `$KYLIN_HOME/async_query_hadoop_conf` directory, and put the hive-site.xml for building the cluster into this directory.
   If Kerberos authentication is enabled, you need to copy the `krb5.conf` file to the `$KYLIN_HOME/async_query_hadoop_conf` directory.
5. If Kerberos authentication is enabled between asynchronous query cluster, query cluster, and build cluster, the following additional configuration is required:


```text
 kylin.storage.columnar.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncquerycluster,hdfs://writecluster 
 kylin.query.async-query.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncquerycluster,hdfs://writecluster 
 kylin.engine.spark-conf.spark.yarn.access.hadoopFileSystems=hdfs://readcluster,hdfs://asyncquerycluster,hdfs://writecluster 
```

6. In general, the above configuration can meet the requirements. In some more advanced scenarios, you can configure spark related configurations in `kylin.properties` to achieve more fine-grained control with guidance of Kylin expert.

   The configuration starts with `kylin.query.async-query.spark-conf`, as shown below:

```text
kylin.query.async-query.spark-conf.spark.yarn.queue=default 
kylin.query.async-query.spark-conf.spark.executor.extraJavaOptions=-Dhdp.version=current -Dlog4j.configuration=spark-executor-log4j.properties -Dlog4j.debug -Dkylin.hdfs.working.dir=$ {kylin.env.hdfs-working-dir} -Dkap.metadata.identifier=${kylin.metadata.url.identifier} -Dkap.spark.category=sparder -Dkap.spark.project=${job.project}- Dkap.spark.mountDir=${kylin.tool.mount-spark-log-dir} -XX:MaxDirectMemorySize=896M 
kylin.query.async-query.spark-conf.spark.yarn.am.extraJavaOptions=-Dhdp.version=current 
kylin.query.async-query.spark-conf.spark.driver.extraJavaOptions=-Dhdp.version=current 
kylin.query.async-query.spark-conf.spark.port.maxRetries=128 
kylin.query.async-query.spark-conf.spark.driver.memory=4096m 
kylin.query.async-query.spark-conf.spark.sql.driver.maxCollectSize=3600m 
kylin.query.async-query.spark-conf.spark.executor.memory=12288m 
kylin.query.async-query.spark-conf.spark.executor.memoryOverhead=3072m 
kylin.query.async-query.spark-conf.spark.yarn.am.memory=1024m 
kylin.query.async-query.spark-conf.spark.executor.cores=5 
kylin.query.async-query.spark-conf.spark.executor.instances=4 
kylin.query.async-query.spark-conf.spark.task.maxFailures=1 
kylin.query.async-query.spark-conf.spark.ui.port=4041 
kylin.query.async-query.spark-conf.spark.locality.wait=0s 
kylin.query.async-query.spark-conf.spark.sql.dialect=hiveql 
kylin.query.async-query.spark-conf.spark.sql.constraintPropagation.enabled=false 
kylin.query.async-query.spark-conf.spark.ui.retainedStages=300 
kylin.query.async-query.spark-conf.spark.hadoop.yarn.timeline-service.enabled=false 
kylin.query.async-query.spark-conf.spark.hadoop.hive.exec.scratchdir=${kylin.env.hdfs-working-dir}/hive-scratch 
kylin.query.async-query.spark-conf.hive.execution.engine=MR 
kylin.query.async-query.spark-conf.spark.sql.crossJoin.enabled=true 
kylin.query.async-query.spark-conf.spark.broadcast.autoClean.enabled=true 
kylin.query.async-query.spark-conf.spark.sql.objectHashAggregate.sortBased.fallbackThreshold=1 
kylin.query.async-query.spark-conf.spark.sql.hive.caseSensitiveInferenceMode=NEVER_INFER 
kylin.query.async-query.spark-conf.spark.sql.sources.bucketing.enabled=false 
kylin.query.async-query.spark-conf.spark.yarn.stagingDir=${kylin.env.hdfs-working-dir} 
kylin.query.async-query.spark-conf.spark.eventLog.enabled=true 
kylin.query.async-query.spark-conf.spark.history.fs.logDirectory=${kylin.env.hdfs-working-dir}/sparder-history 
kylin.query.async-query.spark-conf.spark.eventLog.dir=${kylin.env.hdfs-working-dir}/sparder-history 
kylin.query.async-query.spark-conf.spark.eventLog.rolling.enabled=true 
kylin.query.async-query.spark-conf.spark.eventLog.rolling.maxFileSize=100m 
kylin.query.async-query.spark-conf.spark.sql.cartesianPartitionNumThreshold=-1 
kylin.query.async-query.spark-conf.parquet.filter.columnindex.enabled=false 
kylin.query.async-query.spark-conf.spark.master=yarn 
kylin.query.async-query.spark-conf.spark.submit.deployMode=client 
```

- Asynchronous query does not support query cache.
- When the select column of SQL contains `,;{}()=`, these characters will be converted to `_` in the result file.

---

<a id="operations-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/intro/ -->

<!-- page_index: 78 -->

# Maintenance Guide

Version: 5.0.2

This Maintenance Guide will introduce a suite of capabilities that can help you to manage your Kylin projects, do system maintenance, work with logs.

---

<a id="operations-overview"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/overview/ -->

<!-- page_index: 79 -->

# Overview

Version: 5.0.2

As Kylin system administrator, typical daily operations include:

- To ensure **Kylin** service running smoothly, system administrator should monitor system logs on a regular basis.
- To ensure building jobs run successfully, system administrator needs to monitor jobs execution status via email notification or system web UI.
- To ensure there are enough cluster resources for **Kylin**, system administrator should check the YARN queue and storage utilization frequently.
- To prevent any data loss or system failure, system administrator should make plans for system backup and disaster recovery.

---

<a id="operations-project-managing-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/project-managing/intro/ -->

<!-- page_index: 80 -->

# Project Managing

Version: 5.0.2

The following sections introduce how to manage your projects in Kylin.

Project is the primary management unit of Kylin. In a project, you can design multiple models and perform query analysis.

System settings are isolated at the project level, so you can set different operational preferences for different projects.

Query is isolated at project level, which means models and tables in different projects cannot be queried in one SQL.

---

<a id="operations-project-managing-project_management"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/project-managing/project_management/ -->

<!-- page_index: 81 -->

# Project Management

Version: 5.0.2

This chapter introduces how to manage projects in Kylin.

After the system administrator logs in to Kylin, click the **Admin** button in the top toolbar to enter the system management page, and click the **Porject** field to enter the Project Management page.

> [!NOTE]
> : if no project exist, you will not be allowed to access the **Admin** page. Please add a project firstly and then enter the **Admin** page.

On the project management page, the system administrator can view the project information in the project list, and can also add projects, delete projects, backup projects, or grant user access permissions.

![Project List](assets/images/project-list-b3e881f433107bba561464cc8cf31c69_deda523b5d32252c.png)

The system administrator has two ways to add a new project:

- On the **Admin -> Project Management** page, click the **+ Project** button above the project list.
- On the product normal page, click the **+**（Add Project) button at the top toolbar.

Fill in the project name and description in the pop-up window. The project name is mandatory; the project description is optional. A good project description will help with the maintenance of the project in the future.

![Add Projects](assets/images/add-project-d097dda0c04d27a819196b3f5bac968e_666f313dff2148af.png)

> **tips:** project name is case insensitive, so duplicate names with existing project names are not allowed.

On the Project Management page, select a project to be deleted, click the **...**(More Actions) button under the **Actions** bar on the right, then click **Delete**.

The system administrator can confirm to delete a project in the prompted window. After the project is deleted, it will not be restored and the related data will be cleared.

If there are jobs in **RUNNING, PENDING, or PAUSED** status in the project, it is needed to terminate the jobs before deleting the project.

On the Project Management page, select a project to change owner, click the **...**(More Actions) button under the **Actions** bar on the right, then click **Change Owner**. Only the system administrator has permission to change the project owner.

On the Project Management page, select a project to authorizer, click the **Authorization** button under the **Actions** bar on the right and set permissions for the project. You can find out more at the [Project ACL](#operations-access-control-data-access-control-project_acl) section.

---

<a id="operations-project-managing-project_settings"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/project-managing/project_settings/ -->

<!-- page_index: 82 -->

# Project Settings

Version: 5.0.2

On the left side navigation bar of the page, click **Setting**，you can adjust some settings at the project level on your business demands.

![project settings](assets/images/project-settings-9489dd9650aaf5f00cab4e6535b4a790_b59e6bcbb2dacacd.png)

All settings are composed of three main parts:

- [Project Settings](#operations-project-managing-project_settings--project-settings)
  - [Basic Settings](#operations-project-managing-project_settings--basic-settings)
  - [Advanced Settings](#operations-project-managing-project_settings--advanced-settings)
  - [Model/Index Group Rewrite Settings](#operations-project-managing-project_settings--modelindex-group-rewrite-settings)

In this part, you can check current project's name and description, also, you can modify project description.

![general information](assets/images/project-settings-basic-general-0a7f58d59c9f1e8d55274b7c00e4c16c_763e74b7f3a7fde0.png)

If you don't have any models or there is no avaliable models to answer your queries, you can use **pushdown** to get results for a more flexible user experience, and your queries will be pushdown to Spark SQL by default. This setting is turned on by default.

![pushdown setting](assets/images/project-settings-pushdown-7ff8e06e15b2b9a144257e21ec57de5e_4e66d941ef09cc19.png)

This part is about settings of segment, including Segment Merge, Retention Threshold and Creating Reserved Segments.

**Segment Merge** means the system will automatically merge segments when those segments match the rules and contain the same indexes. Below is how to define the rules.

- **Auto-Merge**: You can choose to automatically merge segments within the time range in 1 hour / 1 day / 1 week / 1 month / 1 quarter / 1 year （natural concepts）.

  > Example of natural concept: Natural week means Monday to Sunday. Natural month means the first day of a month to the last day of the month. Civil year means the first day of a year to the last day of the year.
- **Volatile Range**: The system will delay for a period of time (i.e. Volatile Range) to trigger automatic merging of Segments. You can set the time range to N hour(s), day(s), week(s), month(s), quarter(s), and year(s), where day(s), week(s), and month(s) are natural concepts. N is an integer, and the default value is 0.

  - Usage scenario: In actual business, due to the delay of the ETL process, for example, the business often needs to refresh the data of the past N days every day. During auto-merge, in order to reduce resource waste, you can set Volatile Range to prevent the system from automatically merging segments to be refreshed for the past N days.

> For example: If you build a segment every day and you set the auto-merge time range as 1 week, then you will have 7 segments no.01-07 over last week.
>
> - Volatile range is 0 day , the system will automatically merge 7 segments.
> - Volatile range is 1 day(i.e. the business needs to refresh no.07 Segment on the next day), therefore, the system will not merge no.01-07 segments; the system will not merge the 01-07 segments until the segment no.08 is added in the second week.
> - Volatile range is 2 days(i.e. the business needs to refresh no.06-07 Segments on the next day), therefore, the system will not merge no.01-07 segments until the segments no.08-09 are added in the second week.

**Retention Threshold** sets the oldest segment time range. Support setting day, month, or year as units. By default, Kylin only keeps segments for 1 year, segments beyond 1 year will be deleted automatically.

**Creating Reserved Segments** With this switch ON, you may create a segment with no index (reserved segment). Please note that queries would be answered by pushdown engine when they hit reserved segments.

The picture below is the segment setting page.

![segment settings](assets/images/project-settings-segment-f1a1276d82c30670092b718c44442eba_bb644a34cc443f50.png)

This module includes 5 parts mainly: default database, job notification, YARN application queue, computed column exposure and custom project configuration.

After setting the default database, the database name can be omitted in SQL statements when executing a query or importing a SQL file. Modifying the default database may result in saved queries or SQL files being unavailable, historical queries cannot hit the models. Please modify the default database prudently.

The picture below is the default database setting page:

![default database](assets/images/project-settings-default-database-36fb47c9158a357b96f8095c7d9a6b3a_513868e4b5eb727e.png)

If you want to receive notification of abnormal jobs, you can add your email addresses in this page, once there is any job which loads empty data or gets failed, the system will send you a notification email, the example email goes like this:

![job notification](assets/images/project-settings-job-notification-a9f471e3c8dae5f322087c0ea0a3d701_250107e54d4cd0e1.png)

For specific configuration, please refer to [Job Status Alert](#operations-project-managing-alerting) for more details.

The system admin user can set the YARN Application Queue of the project. After setting the queue, the jobs will be submitted to the specified queue to achieve computing resources allocation and separation between projects. This queue resource is used for non-query jobs such as refreshing data, merging segments, building indexes, loading data and sampling table.

The system will submit the job to the **default** queue of YARN by default. The name of YARN queue is case sensitive. Please make sure the queue you set is available, otherwise the jobs may fail to execute or be submitted to the default queue according to the current **Scheduler Policy** of YARN.

The picture below is the yarn queue setting page:

![yarn_queue](assets/images/project-settings-yarn-queue-6b6cd6aea51a5b45f83da34f9025c051_e34e16a6b194a1a8.png)

This config will control the exposure of the computed columns in current project. If this config is on, Kylin will add computed columns of current project to the table schemas returned. Otherwise, computed columns are hidden from the table schema. This config will influence the table schemas in JDBC, ODBC or BI tools.
You may not want to change this config frequently as it might break the project in your BI tools.

![computed_column_exposure](assets/images/project-settings-cc-expose-dad3b89a9abebb1a0b34f1ed4d00cb41_249dafa0ce41874a.png)

Administrators can add additional project configuration items needed by customizing the project configuration. You can click the **+ Configuration** button, enter the configuration item and parameter value in the pop-up window, and then click **OK**. If you need to modify or delete the added configuration items, you can click the **Edit** or **Delete** button on the right side of the list. These operations take effect immediately.

![computed_column_exposure](assets/images/project-settings-custom-config-9d87610a6518ea335ea6d23c3fcad50e_5889b0c0c1f43611.png)

Kylin supports rewriting some specific properties at level, including Auto-Merge, Volatile Range, Retention Threshold, spark executor resource size and Custom Settings.

Click **+** button (Add Setting Item) under the right **Actions** tab:

![model rewrite](assets/images/project-settings-model-rewrite-4646fd30dedafc5ea8ae5049d1086aca_2519020e64178b43.png)

---

<a id="operations-project-managing-toolbar"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/project-managing/toolbar/ -->

<!-- page_index: 83 -->

# Tool Bar

Version: 5.0.2

The toolbar of Kylin system is as shown in the following figure.

![Toolbar](assets/images/toolbar-e8f0cdaf1ce95d6ea2cb0c12af57ab7c_b9e8a256a5e1bb93.png)

Project list is located on the left side of the toolbar, and the current project is selected. If it is the first time to start Kylin, current project would be empty. The icon on the left side of this list is used for expand and collapse the navigation bar. The button of `+` on the right side is used for adding new project. The newly added project will be set as the current project.

After the system admin logs into Kylin, click **Admin** on the top bar to enter the administration mode. For details, please refer to the [Project Management](#operations-project-managing-project_management) chapter.

The colored dot indicates the status of the service status for the current project. Clicking on it will prompt a dialog shown as follow. The first line in the figure shows the current time of the system. The second line shows the currently used node information, and the icon on the right `>` can expand to view the detailed node information.

![Service Status](assets/images/service-status-1d5209f23b02e2e34bb405829de1839b_028c4360106b3084.png)

The current login user information is displayed on the far right. Click to modify the password and log out.

---

<a id="operations-project-managing-alerting"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/project-managing/alerting/ -->

<!-- page_index: 84 -->

# Job Status Alert

Version: 5.0.2

Kylin provides *Job Status Alert* feature that sends emails to system administrator if any job loads empty data or failed. It is very convenient for follow-ups like troubleshooting or incremental building.

Job status alert by email can be enabled by the following steps,

**Step one**: You need to additionally set following properties in the configuration file `$KYLIN_HOME/conf/kylin.properties`,

```properties
kylin.job.notification-enabled=true|false  # set to true to enable the feature 
kylin.job.notification-mail-enable-starttls=true|false  
kylin.job.notification-mail-host=your-smtp-server  # address of SMTP server 
kylin.job.notification-mail-port=your-smtp-port  # port of SMTP server 
kylin.job.notification-mail-username=your-smtp-account  # SMTP account username 
kylin.job.notification-mail-password=your-smtp-pwd  # SMTP account password 
kylin.job.notification-mail-sender=your-sender-address  # sender address  
```

>
> [!NOTE]
> : If you need to encrypt `kylin.job.notification-mail-password`, you can do it like this：

>
> i. run following commands in `${KYLIN_HOME}`, it will print encrypted password
>
>
```shell
./bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s <password> 
```

>
> ii. config `kylin.job.notification-mail-password` like this
>
>
```properties
 kylin.job.notification-mail-password=ENC('${encrypted_password}') 
```

Please **Restart Kylin** to make configurations take effect.

**Step two**: Set in the project settings page,

- Modelers and Analysts need to fill in the **Advanced Settings** --> **Email Notification** with your email addresses.

![job notification](assets/images/project-settings-job-notification-page-20e36c4ae00df6e33adc58ba932bd565_a276913d735ec441.png)

---

<a id="operations-access-control-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/access-control/intro/ -->

<!-- page_index: 85 -->

# Access Control

Version: 5.0.2

This chapter will describe how to grant roles to users/groups in Kylin to control their access rights, and how to perform fine-grained data access control, it will cover:

- [User Management](#operations-access-control-user_management)
- [User Group Management](#operations-access-control-group_management)
- [Data Access Control](#operations-access-control-data-access-control-intro)

  - [Project Access Control](#operations-access-control-data-access-control-project_acl)

---

<a id="operations-access-control-user_management"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/access-control/user_management/ -->

<!-- page_index: 86 -->

# User Management

Version: 5.0.2

This chapter introduces what a user is and how a user can be managed.

To use Kylin, a user must log in to the system using a user name and corresponding password. Every user is unique in a Kylin instance, which is to say, it is not necessary to create the same user for every project in a single instance.
By default, Kylin initializes one user, namely `ADMIN`. The user `ADMIN` is a built-in system administrator, and the system administrator has all the permissions of the entire system.

After the system administrator logs in to Kylin, click the **Admin** button in the top toolbar to enter the system management page, and click the **User** field to enter the User Management page.

> [!NOTE]
> :

1. Except for the system administrator, simply creating a user does not give the user access to any project.
2. Except for the system administrator, other users need to be given access at the project level.

On the User Management page, the system administrator can click the **+User** button to add new users. In the pop-up window, please fill in the user name, password, confirm new password, select whether the user role is a system administrator or a normal user, and click **OK**.

> **tips:** username is case insensitive, so duplicate names with existing user names are not allowed.

On the User Management page, select a user to be edited, click the **...** (More Actions) button under the **Actions** bar on the right. Then click **Edit Role**.

In the pop-up window, the system administrator can modify user role to administrator or user.

On the User Management page, select a user to be deleted, click the **...** (More Actions) button under the **Actions** bar on the right. Then click **Delete**. The system administrator can confirm to delete a user in the prompted window. User can not be restored after deleting, and user's access permission on all projects will be removed.

On the User Management page, select a user, and click the **...** (More Actions) button under the **Actions** bar on the right. Then click **Enable / Disable**. The system administrator can enable or disable a user, and disabled users cannot login to the system.

On the User Management page, select a user, click **Reset Password** under the **Actions** bar on the right.

In the pop-up window, the system administrator can change the password and need to enter the new password twice.

The initial ADMIN account password needs to be modified after the first login. To reset the password, you can execute the following command. After successful execution, the ADMIN account will regenerate a random password and display it on the console. When you log in, you need to change the password:

```sh
$KYLIN_HOME/bin/admin-tool.sh admin-password-reset 
```

When the parameter `kylin.metadata.random-admin-password.enabled=false`, it will not regenerate a random password but the fixed password `KYLIN`. If the parameter `kylin.metadata.random-admin-password.enabled` is set from `false` to `true` , it will regenerate a random password and display it on the console after all the Kylin nodes restarted.

Click `username` --> `Setup` in the top right corner of the navigation bar. In the pop-up window, user need to provide the old password and repeat the new password twice to reset password.

To assign a user to a group, please do the followings:

1. On the User Management page, select a user to be grouped.
2. Click **Assign to Group** under the **Actions** bar on the right.
3. Select a group to assign the user to under **Candidates**, and then click the right arrow **>**. The group will enter into **Selected**.
4. Click **OK** and the user will be in the selected group.

To modify user group, please do the following steps:

1. On the User Management page, select a user to modify the group membership.
2. Click **Assign to Group** under the **Actions** bar on the right.
3. Select the group to be modified under **Selected**, and then click the left arrow `<`. The group will enter into **Candidates**.
4. Click **OK** and the user group membership will be modified.

---

<a id="operations-access-control-group_management"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/access-control/group_management/ -->

<!-- page_index: 87 -->

# User Group Management

Version: 5.0.2

This chapter provides an overview of what a user group is and how a user group can be managed.

A user group is a collection of users, and users in a user group share the same ACL. By default, Kylin initializes four user groups, namely **ALL\_USERS**, **ROLE\_ADMIN**, **ROLE\_ANALYST**, and **ROLE\_MODELER**. And **ALL\_USERS** group is a default user group, all users are included in the **ALL\_USERS** user group. **ALL\_USERS** and **ROLE\_ADMIN** user group cannot be modified or deleted. System administrators can add or remove users in user groups except ALL\_USERS, or add a user to multiple groups except **ALL\_USERS**. User groups cannot be renamed throughout the Kylin instance.

The system administrator can grant the project-level access permissions to a user group. When a user group has been granted the project-level permissions, users in this group will inherit the corresponding permissions from the group.

When a user belongs to multiple groups, the user will inherit the project-level permissions from the groups he/she belongs to.

After the system administrator logs in to Kylin, click the **Admin** button in the top toolbar to enter the system management page, and click the **Group** field to enter the User Group Management page.

On the User Group Management page, click **+ User Group** button to create a new group. In the pop-up window, the system administrator can fill in the group name and click **OK** to save a new user group.

On the User Group Management page, select a user to be deleted, click the **Drop** button under the **Actions** bar on the right. In the pop-up window, the system administrator can confirm to delete a user group, once a user group is deleted, users in this user group will not be deleted and permission grant to this user group will be removed.

1. On the User Group Management page, select the user group to be assigned users to.
2. Click **Assign Users** under the **Actions** bar on the right.
3. In the pop-up window, check the users who need to be assigned to the group, click the right arrow **>**, the user will be assigned to the **Assigned Users**.
4. Click **OK** and the user will be assigned to this group.

Please refer to [User Management](#operations-access-control-user_management).

---

<a id="operations-access-control-data-access-control-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/access-control/data-access-control/intro/ -->

<!-- page_index: 88 -->

# Data Access Control

Version: 5.0.2

Kylin provides a rich set of access control features for big enterprise. Start from Kylin 5, every action from user must satisfy both **Operation Permission** and **Data Access Permission**, before the action can perform.

- Operation Permission: Defined at project level, specifies what operations a user can perform within a project. User can have one of the four permissions, from weak to powerful:

  - *QUERY*: Allows to run query in a project.
  - *OPERATION*: Allows to operate models, like building, refreshing, and managing Segments. Implies the QUERY permission.
  - *MANAGEMENT*: Allows to manage models and cubes, like create and edit. Implies the OPERATION permission.
  - *ADMIN*: Project level administrator permission, allows to manage source tables, and all other operations in a project.

  See [Project ACL](#operations-access-control-data-access-control-project_acl) for more details.

To perform an action, user must have operation permission. Below is few examples.

- To edit a model, user must have the MANAGEMENT permission and have access to all the tables and columns in the model.

- The system administrator is not restricted by the data access controls by default, he/she has access to all data.
- The system does not provide operation permissions at model level yet.

---

<a id="operations-access-control-data-access-control-project_acl"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/access-control/data-access-control/project_acl/ -->

<!-- page_index: 89 -->

# Project Access Control

Version: 5.0.2

Project ACLs determines whether a user/user group can access a certain project in Kylin. Kylin has four built-in project level permissions, *Admin*, *Management*, *Operation* and *Query*. *Admin* includes the other three permissions, *Management* includes *Operation* and *Query* permissions, *Operation* includes *Query* permissions.

- *QUERY*: Permission to query tables/models in the project. If pushdown is enabled, user/group can query tables loaded to the project when there's no ready model to answer the query.
- *OPERATION*: Permission to build a model in the project, including rebuild a segment, resume or discard jobs.
- *MANAGEMENT*: Permission to edit/delete models in the project.
- *ADMIN*: Permission to manage data sources, models in the project.

After the system administrator logs in to Kylin, click the **Admin** button in the global toolbar to enter the system management page, and click the **Project** field to enter the Project Management page.

After the system administrator assigns project access permission to a group, users in the group will inherit the access permission on data source, models and segments accordingly.

1. Select the project and click the **Authorization** icon under the **Actions** column on the right to enter the authorization page.
2. Expand a project on the project list.
3. Click **+ User / Group** to grant access for a user / user group.
4. Select the grant type : by **User** or by **User Group**. Then select the user / user group and access permission to be granted, and click **Submit**.

![Grant Project ACL](assets/images/acl-5-9254856ca3008220b718dfd93011da5c_29fbd83b133eabda.png)

1. Select the project and click the **Authorization** icon under the **Actions** column on the right to enter the authorization page.
2. Select the user / user group in the list and click the **Edit** icon under the **Actions** column on the right.
3. Modify user / user group's access permission and click **Submit**.

1. Select the project and click the **Authorization** icon under the **Actions** column on the right to enter the authorization page.
2. Select the user / user group in the list and click the **Delete** icon under the **Actions** column on the right.

---

<a id="operations-system-operation-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/intro/ -->

<!-- page_index: 90 -->

# System Operation

Version: 5.0.2

This chapter introduces how to do system operation.

---

<a id="operations-system-operation-diagnosis-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/diagnosis/intro/ -->

<!-- page_index: 91 -->

# Diagnosis

Version: 5.0.2

Kylin provides a diagnosis function to help users solve problems they may encounter, such as job failure, SQL query failure, SQL query overtime, etc.

---

<a id="operations-system-operation-diagnosis"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/diagnosis/ -->

<!-- page_index: 92 -->

# System, Job and Query Diagnosis

Version: 5.0.2

Kylin users may face with many problems during usage, such as job failure, SQL query failure, SQL query overtime, etc. In order to help solve these problems efficiently, Kylin provides a *Diagnosis* function on Web UI to pack related information into a zip package to help operation staff and Kylin Community to analyze the root cause.

Diagnosis function includes System, Job and Query Diagnosis. In addition to the method of generating diagnostic package on web UI described in this chapter, you can also generate the diagnostic package through the bash script. For details, please refer to [Diagnosis Tool](#operations-system-operation-cli_tool-diagnosis).

System diagnostic package includes all diagnostic information of a Kylin instance, and users can generate system diagnostic package on Web UI following the following steps:

![Generate System Diagnostic Package in Web UI](assets/images/diagnosis-web-c3de4f4968924668a8d999cfc038fe8a_643f9d5e57b3c5f3.png)

1. Enter the **Admin** page and click the **Diagnosis** button in the lower left corner.

   >
> [!NOTE]
> : Only the system administrator can generate the system diagnostic package in web ui for the time being.

2. Select **Time Range**: You can select *last one hour*, *last one day*, *last three days* and *last one month*, or self-defined.

   > **Note:** The selected time range must include the period of incidents.
3. Select **Server**.

   > **Note:** If Kylin is deployed on multiple nodes, please locate the specific node on which your issue happened by selecting the right server name, otherwise the generated system diagnostic package may not include useful information about the issue.
4. Click **Generate and Download** button: After the diagnostic package is generated, the downloads will be triggered automatically. If the diagnostic package generation fails, you can view the details of the failure on the interface.

Job diagnostic package includes all diagnostic information of a specific job, and users can generate job diagnostic package on Web UI by following the following steps:

![Generate Job Diagnostic Package in Web UI](assets/images/job-diagnosis-web-01-1fd091ffdd8203e6d4e942a987110d4d_6c202a285c537fdb.png)

![Generate Job Diagnostic Package in Web UI](assets/images/job-diagnosis-web-02-96a075df7a175a4ebde1c72ee2e6d76a_4ffdbdd10c25abb7.png)

1. After logging in to Kylin, click **Monitor** in the left navigation bar. In the action bar of a job on the **Jobs List** page, click the **Download Job Diagnostic Package** button.
2. Select **Server**.
3. Click **Generate and Download** button: After the diagnostic package is generated, the downloads will be triggered automatically. If the diagnostic package generation fails, you can view the details of the failure on the interface.

Query diagnosis package includes all diagnostic information of a specific query, and users can generate query diagnosis package on Web UI by following the following steps:

![Generate Query Diagnosis Package in Web UI](assets/images/query-diagnosis-web-01-79dc26620287f131084065d10287a7d6_2030ba8258d14c0a.png)

![Generate Query Diagnosis Package in Web UI](assets/images/query-diagnosis-web-02-4681ef06eaa22d791b563030ef1bd81f_08358dec4d223627.png)

1. After logging in to Kylin, click **Query** in the left navigation bar. In the action bar of a query on the **History** page, click the **Download Query Diagnostic Package** button in **Action**.
2. Click **Generate and Download** button: After the diagnosis package is generated, the downloads will be triggered automatically. If the diagnosis package generation fails, you can view the details of the failure on the interface.

By default, all users with project query permissions can download the query diagnostic package to facilitate query problem diagnosis.
Since the query diagnostic package contains some configuration information, if you want to reduce the relevant permissions for downloading the query diagnostic package, you can add configuration `kylin.security.allow-non-admin-generate-query-diag-package=false` in `$KYLIN_HOME/conf/kylin.properties`, only system administrators and users with project ADMIN permissions are allowed to download the query diagnostic package.

**Q: What are the differences in the contents of the three diagnostic packages?**

For the contents of the three diagnostic packages, please refer to [Diagnosis Package Tool](#operations-system-operation-cli_tool-diagnosis).

**Q: If I failed to generate diagnostic packages because of timeout.**

Please change parameter `kylin.diag.package.timeout-seconds`(in seconds, the default value is one hour) in `$KYLIN_HOME/conf/kylin.properties` and restart Kylin.

**Q: What should I do if the page does not download the diagnostic package automatically after the packaging is completed?**

If the system has generated the diagnostic package successfully but fails to download it automatically, you can click **Download Manually** at the bottom left, select the diagnostic package you want to download, and then click the download button to download manually.

**Q: What should I do if the hostname used by Kylin contains an underscore (`_`) and generates a diagnostic package has exception?**

Please add service discovery parameter `spring.cloud.zookeeper.discovery.instance-host=IP` in `$KYLIN_HOME/kylin.properties.override` and restart Kylin.

---

<a id="operations-system-operation-diagnosis-query_flame_graph"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/diagnosis/query_flame_graph/ -->

<!-- page_index: 93 -->

# Query Flame Graph

Version: 5.0.2

Kylin has built-in async-profiler. When flame graphs are needed to diagnose query performance, users can generate query flame graphs for Spark Driver and Executor by calling the API interface.

Since the flame graph is generated at the system level, it will affect all projects. Only the Admin user has the authority to use this function.

| Config | Comment |
| --- | --- |
| kylin.query.async-profiler-enabled | enable the profiling feature (default to TRUE). After enables, you can trigger the generation and download of the flame graph by calling the API |
| kylin.query.async-profiler-result-timeout | the timeout for the result collection (default to 60s) |
| kylin.query.async-profiler-profile-timeout | the timeout for the profiling (default to 5min) |

invoke the below HTTP API to start generating flame graph

- GET `http://host:port/kylin/api/query/profile/start?params={params}`
- URL Parameters

  - `params`, Optional, String, specify async-profiler params to start profiling, default to `start,event=cpu` (profile the cpu only), ref to <https://github.com/jvm-profiling-tools/async-profiler> for more parameters
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`

invoke the below HTTP API to stop generating flame graph and download flame graph

- GET `http://host:port/kylin//api/query/profile/dump?params={params}`
- URL Parameters

  - `params`, Optional, String, specify async-profiler params to start profiling, default to `flamegraph` (dump the result as flamegraph), ref to <https://github.com/jvm-profiling-tools/async-profiler> for more parameters
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`

1. Current async-profiler version comes with Kylin is Linux x64 (glibc): async-profiler-2.5-linux-x64.tar.gz, Other platforms are not supported.
2. The profiling may have some impact on the performance of Kylin, avoid doing a long time profiling in production.
3. The flame graph result can only be downloaded once.

---

<a id="operations-system-operation-diagnosis-build_flame_graph"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/diagnosis/build_flame_graph/ -->

<!-- page_index: 94 -->

# Build Flame Graph

Version: 5.0.2

Kylin has built-in async-profiler. When flame graphs are needed to diagnose build tasks performance, users can generate query flame graphs for Spark Driver and Executor by calling the API interface.

Since the flame graph is generated at the system level, it will affect all projects. Only the Admin user has the authority to use this function.

| Config | Comment |
| --- | --- |
| kylin.engine.async-profiler-enabled | enable the profiling feature (default to FALSE). After enables, you can trigger the generation and download of the flame graph by calling the API |
| kylin.engine.async-profiler-result-timeout | the timeout for the result collection (default to 60s) |
| kylin.engine.async-profiler-profile-timeout | the timeout for the profiling (default to 5min) |

invoke the below HTTP API to start generating flame graph

- HTTP Header
  - `Accept: application/vnd.apache.kylin-v4-public+json`
    - `Accept-Language: en`
    - `Accept-Language: zh`
  - `Content-Type: application/json;charset=utf-8`

**There are two ways to generate**

- GET `http://host:port/kylin/api/jobs/profile/start_project?project={projectName}&step_id={jobStepId}&params={params}`

  - URL Parameters
    - `project`, Required, String, specifies the projectName where the current build task is located, no default value
    - `step_id`, Required, String, specifies the jobStepId of the current build task, which can be found in the YARN interface, copying the rest of its Name except `job_step_`.
    - `params`, Optional, String, specify async-profiler parameter, default is `start,event=cpu` (profile cpu usage)
- GET `http://host:port/kylin/api/jobs/profile/start_appid?app_id={yarnAppId}&params={params}`

  - URL Parameters
    - `app_id`, Required, String, specifies the Application ID of the current build task submitted to YARN
    - `params`, Optional, String, specify async-profiler parameter, default is `start,event=cpu` (profile cpu usage)

invoke the below HTTP API to stop generating flame graph and download flame graph

- HTTP Header
  - `Accept: application/vnd.apache.kylin-v4-public+json`
    - `Accept-Language: en`
    - `Accept-Language: zh`
  - `Content-Type: application/json;charset=utf-8`

**There are two ways to get it**

- GET `http://host:port/kylin/api/jobs/profile/dump_project?project={projectName}&step_id={jobStepId}&params={params}`

  - URL Parameters
    - `project`, Required, String, specifies the projectName where the current build task is located, no default value
    - `step_id`, Required, String, specifies the jobStepId of the current build task, which can be found in the YARN interface, copying the rest of its Name except `job_step_`.
    - `params`, Optional, String, specify the async-profiler parameter, default is `flamegraph` (collects the results as a flame graph)
- GET `http://host:port/kylin/api/jobs/profile/dump_appid?app_id={yarnAppId}&params={params}`

  - URL Parameters
    - `app_id`, Required，String，specify the Application ID of the current build task submitted to YARN
    - `params`, Optional, String, specify the async-profiler parameter, the default is `flamegraph` (collects the results as a flame graph)

1. Current async-profiler version comes with Kylin is Linux x64 (glibc): async-profiler-2.5-linux-x64.tar.gz, Other platforms are not supported.
2. The profiling may have some impact on the performance of Kylin, avoid doing a long time profiling in production.
3. The parameters involved in building the flame chart are system level parameters, please do not set them at other levels as they may cause abnormal behavior.
4. The `params` support configuration parameters can be found at <https://github.com/jvm-profiling-tools/async-profiler>
5. On some machines, the required native libraries may fail to load when the `/tmp` disk has the noexec attribute, causing Spark initialization to fail and affecting normal build tasks, so this feature is disabled by default.

---

<a id="operations-system-operation-update-session-table"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/update-session-table/ -->

<!-- page_index: 95 -->

# Update Session Table Tool

Version: 5.0.2

When configured `kylin.web.session.secure-random-create-enabled=true` or `kylin.web.session.jdbc-encode-enabled=true`, the session table needs to be upgraded, otherwise the user cannot log in.

**How to Use**

- Use tools to update


```bash
  $KYLIN_HOME/bin/kylin.sh org.apache.kylin.tool.upgrade.UpdateSessionTableCLI 
```

> Note: During the upgrade process, the update may fail due to permission reasons. At this time, the operation and maintenance personnel need to manually execute the statement to update the session table.

**Use PostgreSQL as Metastore**

```sql
ALTER TABLE spring_session ALTER COLUMN SESSION_ID TYPE VARCHAR(180) , ALTER COLUMN SESSION_ID SET NOT NULL; 
 
ALTER TABLE spring_session_ATTRIBUTES ALTER COLUMN SESSION_ID TYPE VARCHAR(180) , ALTER COLUMN SESSION_ID SET NOT NULL; 
```

**Use MySQL as Metastore**

```sql
ALTER TABLE spring_session MODIFY COLUMN SESSION_ID VARCHAR(180) NOT NULL; 
 
ALTER TABLE spring_session_ATTRIBUTES MODIFY COLUMN SESSION_ID VARCHAR(180) NOT NULL; 
```

---

<a id="operations-system-operation-cli_tool-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/cli_tool/intro/ -->

<!-- page_index: 96 -->

# CLI Operation Tool

Version: 5.0.2

This chapter introduces how to use the Command-Line Interface tool to do daily operation work. Such as environment dependency checking tool, metadata tool, and diagnostic package.

---

<a id="operations-system-operation-cli_tool-environment_check"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/cli_tool/environment_check/ -->

<!-- page_index: 97 -->

# Environment Check

Version: 5.0.2

Before you start Kylin, we provide an environment dependency checking tool to help you spot the potential problems in advance. This tool will be automatically executed by startup script when you run Kylin at the first time.

As said above, if you start Kylin at the first time, the startup script will automatically run this tool. If it check failed, this tool will be executed again when you start this product. Once successfully passed this check, the tool will not be executed automatically.

If you need to check the environment dependency manually, just run the below command:

```sh
$KYLIN_HOME/bin/check-env.sh 
```

The following table describes what will be checked in the tool.

| Check Item | Description |
| --- | --- |
| Kerberos | To check whether user enable Kerberos in the settings. If not, the check will be skipped. Otherwise, it will execute the following operations: 1. check if Kerberos command exists 2. initialize Kerberos |
| OS version and command | Kylin only supports Linux operating systems. Besides operating system, this tool will also check if `hadoop` and `yarn` commands exist. If these two commands are not available, please make sure Hadoop cluster whether is available. |
| Hadoop configuration files | Kylin copies Hadoop configuration files to Kylin installation directory `$KYLIN_HOME/hadoop_conf`. For instance, `core-site.xml`, `hdfs-site.xml`, `yarn-site.xml`, `hive-site.xml`, etc. This tool will check if `$KYLIN_HOME/hadoop_conf` exists and contains necessary configuration files. |
| HDFS working directory | 1. Check if HDFS working directory exists 2. If yes, check whether current user has write privilege |
| Java version | Currently, we only support Java versions above 1.8 |
| Server port | Check if the port is in use |
| Spark | 1. Check if the configured resource size exceeds the cluster's actual resource size, such as, executor cores and executor instances. 2. Check if Spark is available 3. Check if the configured yarn queues for submitting query jobs and build jobs are legal 4. Check if the configured driver host address is legal |
| Spark log directory | Users can configure a HDFS directory to store Spark logs, so it checks if the directory exists and current user has read and write privileges. |
| Metastore | Check if the metastore is accessible and current user can perform necessary operations on metadata. |
| InfluxDB | 1. Check if InfluxDB is accessible 2. Check if current user has read and write privileges |
| ZooKeeper | Check if the service discovery is available. |
| KylinConfig | Checking kylin config, must starts with kylin / spring / server. |
| Query history | Check whether the current user has permissions of reading and writing on the `query_history` and `query_history_realization` tables in the RDBMS database |

---

<a id="operations-system-operation-cli_tool-diagnosis"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/cli_tool/diagnosis/ -->

<!-- page_index: 98 -->

# Diagnostic Package

Version: 5.0.2

Kylin users may face with many problems during usage, such as failure in creating a model or query errors. Kylin provides a cli tool to pack related information into a zip package to help system administrator to better analyze the root cause of these problems.
Diagnosis function including System Diagnosis、Job Diagnosis and Query Diagnosis.

- Generate system diagnostic package
  Execute `$KYLIN_HOME/bin/diag.sh [-startTime <START_TIMESTAMP> -endTime <END_TIMESTAMP>] [-destDir <DESTINATION_DIR>]` to generate the system diagnostic package. The default time range is last 1 day, START\_TIMESTAMP and END\_TIMESTAMP is in unix timestamp. You may get the current unix timestamp by run `` echo $((`date +%s`*1000)) `` in Linux.
- Generate job diagnostic package
  Execute `$KYLIN_HOME/bin/diag.sh -job <jobid> [-destDir <DESTINATION_DIR>]` to generate the job diagnostic package with replacing `<jobid>` with the job ID number.
- Generate query diagnostic package
  Execute `$KYLIN_HOME/bin/diag.sh -project <project> -query <queryid> [-destDir <DESTINATION_DIR>]` to generate the query diagnostic package with replacing `<queryid>` with the actual query ID number and `<project>` with the name of the project in which the actual query is made.
- Diagnostic package storage location
  Diagnostic packages generated by scripts are stored under `$KYLIN_HOME/diag_dump/` by default, you can specify the location by configuring `-destDir` parameter.

  > Note: In order to avoid the diagnostic package occupying a lot of storage, please clean up the `$KYLIN_HOME/diag_dump/` directory in time.
- Skip metadata files
  If you want to exclude metadata files, please specify `-includeMeta false`.
- Skip audit log files
  If you want to exclude audit log files, please specify `-includeAuditLog false` or add configuration `kylin.diag.include-auditlog=false` in the `kylin.properties`

- `/conf`: configuration information under the `$KYLIN_HOME/conf` directory.
- `/hadoop_conf`: configuration information under the `$KYLIN_HOME/hadoop_conf` directory.
- `/metadata`: metadata files.
- `/logs`: all the logs in the specified time range, 1 day is by default.
- `/spark_logs`: all Spark executor logs and Spark executor GC logs of query in the specified time range. The Spark executor logs of job are not included. If you need related logs, please generate the corresponding job diagnostic package.
- `/sparder_history`：all Sparder logs of query in the specified time range.
- `/system_metrics`: all system metrics in the specified time range.
- `/audit_log`: all audit logs of metdata in the specified time range.
- `/job_tmp`: the optimization suggestions log.
- `/client`: operating system resources occupied information, Hadoop version and Kerberos information.
- `/bin`: program execute and manager binary files.
- `/monitor_metrics`: System monitoring statistics.
- `/write_hadoop_conf`：`$KYLIN_HOME/write_hadoop_conf`, Hadoop configuration of the build cluster. This directory will not be available when Read/Write separation deployment is not configured.
- file `catalog_info`: directory structure of install package.
- file `commit_SHA1`: git-commit version.
- file `hadoop_env`: hadoop environment information.
- file `info`: license，package and hostname.
- file `kylin_env`: Kylin version, operating system information, Java related information, git-commit information.
- file `time_used_info`: Time statistics of each file generated in the diagnostic package.

- `/conf`: configuration information under the `$KYLIN_HOME/conf` directory.
- `/hadoop_conf`: configuration information under the `$KYLIN_HOME/hadoop_conf` directory.
- `/job_history`：Job execution history information mainly includes the execution information of yarn application.
- `/metadata`: metadata files.
- `/logs`: the logs generated during the execution of the job.
- `/spark_logs`: all spark executor logs generated during job execution.
- `/system_metrics`: the system metrics generated during the execution.
- `/audit_log`: the audit logs generated during the execution.
- `/job_tmp`: the temporary files, logs and optimization suggestions log of job.
- `/yarn_application_log`: specifies the logs of yarn application of job.
- `/client`: operating system resources occupied information, Hadoop version and Kerberos information.
- `/bin`: program execute and manager binary files.
- `/monitor_metrics`: System monitoring statistics.
- `/write_hadoop_conf`：`$KYLIN_HOME/write_hadoop_conf`, Hadoop configuration of the build cluster. This directory will not be available when Read/Write separation deployment is not configured.
- file `catalog_info`: directory structure of install package.
- file `commit_SHA1`: git-commit version.
- file `hadoop_env`: hadoop environment information.
- file `info`: license, package and hostname.
- file `kylin_env`：Kylin version, operating system information, Java related information, git-commit information.
- file `time_used_info`: Time statistics of each file generated in the diagnostic package.

- `/conf`: configuration information under the `$KYLIN_HOME/conf` directory.
- `/hadoop_conf`: configuration information under the `$KYLIN_HOME/hadoop_conf` directory.
- `/metadata`：specify the metadata for all models under the project.
- `/logs`：`$KYLIN_HOME/logs/kylin.log`，specify the log of the query.
- `/spark_logs`：all Spark executor logs and Spark executor GC logs within the time range are included in the query diagnostic package.
- `/sparder_history`：all Sparder logs within the time range are included in the query diagnostic package.
- `/client`：operating system resource usage, Version information for Hadoop, and Kerberos information.
- file `catalog_info`: directory structure of install package.
- file `commit_SHA1`: git-commit version.
- file `hadoop_env`: hadoop environment information.
- file `info`: license, package and hostname.
- file `kylin_env`：Kylin version, operating system information, Java related information, git-commit information.
- file `time_used_info`: Time statistics of each file generated in the diagnostic package.

At present, there is no API to know which nodes are in the cluster. You need to record the deployed nodes by yourself, and then go to each node to generate diagnostic package separately. The method of generating the diagnostic package is the same as the above.

The diagnostic package desensitization function can hide sensitive information in the diagnostic package, such as user names, passwords, etc. While helping users solve problems, it can meet users' data security requirements.

You can enable the diagnostic package desensitization function through the following configuration item:

```properties
## The desensitization level of the diagnostic package. RAW stands for no desensitization, OBF stands for desensitization 
kylin.diag.obf.level=OBF 
```

After the configuration is enabled, the diagnostic package generated through the Web UI or through the terminal CLI tool will be desensitized. The system will desensitize all files starting with `kylin.properties` in the `KYLIN_HONE/conf` directory. All configuration items including `password`, `user`, `zookeeper.zk-auth`,  `The configuration items of source.jdbc.pass` will be desensitized. The desensitization method is to replace the value of the configuration item with `<hidden>`.

**Q: Why is the system diagnostic package log content incomplete?**

A: The extraction of the log is a text-based match (based on the minute-level time string). If the content is found to be incomplete, it may be that the specified timestamp is not converted to the corresponding one when converted to a time string. You can try to modify the time range and re-generate the diagnostic package.

**Q: Why is the `system_metrics` directory missing content in diagnostic package?**

A: `system_metrics` contains system metrics, which are stored in InfluxDB. You need to specify an RPC port when using InfluxDB to back up the data, so please verify whether the configuration item `kylin.metrics.influx-rpc-service-bind-address` in the file `$KYLIN_HOME/conf/kylin.properties` is correct.

**Q: How to deal with Out of Memory (OOM) problem that happens during diagnostic package generating?**

A: Please check the value of `JAVA_VM_XMX` in `conf/setenv.sh`, which is recommended to be adjusted to more than 4 times the size of metadata. For example, if the size of metadata is 1G, please set the value to 4G or above.

\*\*Q: Why is the file of the exported model optimization suggestion 0KB? \*\*

A: If the model has no optimization suggestions, then the optimization suggestions generated by the corresponding model will be 0KB.

---

<a id="operations-system-operation-cli_tool-metadata_operation"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/cli_tool/metadata_operation/ -->

<!-- page_index: 99 -->

# Metadata Operation

Version: 5.0.2

Kylin instances are stateless services, and all state information is stored in metadata. Therefore, backing up and restoring metadata is a crucial part of operation and maintenance.

Metadata is divided into system level and project level.

In general, it is a good practice to back up metadata before each failure recovery or system upgrade. This can guarantee the possibility of rollback after the operation fails, and still maintain the stability of the system in the worst case.

In addition, metadata backup is also a tool for fault finding. When the system fails, the frontend frequently reports errors. By downloading and viewing metadata, it is often helpful to determine whether there is a problem with the metadata or not.

Metadata can be backed up via the command line, as follows:

- Metadata backup via **command line**

  Kylin provides a command line tool for backing up metadata, using the following methods:

  - Backup **system level** metadata


```sh
$KYLIN_HOME/bin/metastore.sh backup METADATA_BACKUP_PATH 
```

    Parameter Description:

    - `METADATA_BACKUP_PATH` - optional, represents the metadata storage path of the backup, the default value is `${KYLIN_HOME}/meta_backups/`
  - Backup **project level** metadata


```sh
$KYLIN_HOME/bin/metastore.sh backup-project PROJECT_NAME METADATA_BACKUP_PATH 
```

    Parameter Description:

    - `PROJECT_NAME` - required, the name of the project to be backed up, such as learn\_kylin
    - `METADATA_BACKUP_PATH` - optional, represents the metadata storage path of the backup, the default value is `${KYLIN_HOME}/meta_backups/`

Metadata recovery is required in Kylin with the **command line**.

- Restore **system level** metadata


```sh
$KYLIN_HOME/bin/metastore.sh restore METADATA_BACKUP_PATH [--after-truncate] 
```

  Example:


```sh
./bin/metastore.sh restore meta_backups/2019-12-19-14-18-01_backup/ 
```

  Parameter Description:

  - `METADATA_BACKUP_PATH` - required, represents the metadata path that are going to be recovered, the default value is `${KYLIN_HOME}/meta_backups/`
  - `--after-truncate` - optional, if this parameter is added, the system metadata will be completely restored, otherwise only the deleted and modified metadata will be restored, and the new metadata will still be retained.
- Restore **project level** metadata


```sh
$KYLIN_HOME/bin/metastore.sh restore-project PROJECT_NAME METADATA_BACKUP_PATH [--after-truncate] 
```

  Example:


```sh
./bin/metastore.sh restore-project projectA meta_backups/2019-12-19-14-18-01_backup/ 
```

  Parameter Description:

  - `PROJECT_NAME` - required, represents the project name
  - `METADATA_BACKUP_PATH` - required, represents the metadata path that are going to be recovered, the default value is `${KYLIN_HOME}/meta_backups/`
  - `--after-truncate` - optional, if this parameter is added, the project metadata will be completely restored, otherwise only the deleted and modified metadata will be restored, and the new metadata will still be retained.

Since Kylin 5.0-alpha and Kylin 5.0.0 underwent a metadata refactoring, you will need to use this tool to perform a metadata migration on versions prior to 5.0.0. The steps for migration are as follows:

- Backup the metadata


```shell
$KYLIN_HOME/bin/metastore.sh backup METADATA_BACKUP_PATH 
```

- Perform metadata conversion


```shell
$KYLIN_HOME/bin/kylin.sh org.apache.kylin.common.persistence.metadata.MigrateKEMetadataTool  {inputPath} {outputPath} 
```

- Restore the metadata


```shell
$KYLIN_HOME/bin/metastore.sh restore METADATA_RESTORE_PATH 
```

> [!TIP]
> **Tips**
> - Configure the new KE and ensure it starts normally. Ensure that at least the following parameters are configured: `metadata_url`, `zookeeper`, other required parameters. If the metadata were stored in MySQL, provide the MySQL-related JAR package.
> - During metadata migration and import, a large number of intermediate values may be stored in memory. If you encounter OutOfMemory (OOM) issues, adjust the memory parameters and try again.

---

<a id="operations-system-operation-cli_tool-rollback"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/cli_tool/rollback/ -->

<!-- page_index: 100 -->

# Rollback Tool

Version: 5.0.2

When a user error causes metadata or data loss, or when Kylin is unavailable due to an unknown issue, you can roll back to a specified moment with the rollback tool to ensure production stability.

> Note: The rollback tool is used in some emergency cases, please use this before read the materials carefully.

**How to Use**

- Stop all Kylin services.
- Use tools to roll back


```bash
$KYLIN_HOME/bin/rollback.sh  --project project_example --time '2020-09-01 15:20:19' 
```

- Observe logs to identify differences of metadata such as project, model, user, Segment, task, etc.
- Complete the interaction and confirmation to ensure that you are aware of the impact of the rollback.
- After completed the rollback, start Kylin service.

- `-p，--project <arg>` : Project name [optional], `<arg>` is the project name.
- `-t, --time <arg>`: Historical time point to roll back [required]. `<arg>` is the specific time to roll back to, the format is  `yyyy-MM-dd HH: mm: ss`. The available value is the time point from the earliest backup version time to date.
- `--skip-check-data`: Skip checking whether the resource file is available [optional].

Kylin now offers metadata backup and restore tools that go some way to protecting metadata from loss. However, the tool has some limitations.

- There is no way to rewind to the specified moment, you can only rewind to the version that has been backed up in the past.
- The metadata backup tool is straightforward, and it is possible that metadata may not be available after being backed up. For example, some files are cleaned up as garbage because the metadata does not exist, and the corresponding backup metadata is not available.

The premise of using the rollback tool is that the resource data (cube data, dictionary data, snapshot data, etc.) must be guaranteed not to be deleted within the rollback time range. The retention period of the resource data involves two configurations

- `kylin.storage.time-machine-enabled` After this configuration is enabled, the resources in the retention period will not be deleted in the Kylin service. After being enabled, the snapshot data retention time will be the same as the time configured in `kylin.storage.resource-survival-time-threshold`, the default value is False.
- `kylin.storage.resource-survival-time-threshold` Resource data retention time, the default value is `7d`, unit description: `d` (day), `h` (hour), `m` (minute).

The following are some errors and points of attention that may be encountered during the use of the tool

**Points to take attention**

- Using the rollback tool will roll back the state of the task execution to the state of the historical moment, and will restart the execution after the Kylin service is started.
- After the rollback tool configuration is turned on, more garbage files may be saved and more storage space may be token up. Using the garbage cleaning tool during the retention period cannot clean up the expired resource data during the retention period.
- During the execution of the tool, if it is run multiple times, each run will keep a backup of the current metadata in the `{working-dir}/_current_backup` directory, the file names are distinguished by time.
- The time specified by the user cannot be greater than the current time.
- All service nodes must be shut down before using the tool, otherwise it will cause data inconsistency.
- If the user manually deletes the dictionary data of the project and then regenerates the dictionary data again, using the rollback tool will cause the dictionary data and the index data to be inconsistent.
- After opening the `kylin.storage.time-machine-enabled` configuration after upgrading, users need to wait for a configured retention period before they can be rolled back.
- The user rolls back to the historical moment, and the snapshot data used is also the snapshot data of the historical moment instead of using the latest snapshot data.
- If the rollback time specified by the user is less than the minimum time of the metadata backup, the rollback cannot be performed.

**Possible error results**

- Using the rollback tool reverts the state of the task execution back to the historical moment, and the execution is triggered again when the Kylin is started.
- Turning on the time machine causes more junk files to be saved, taking up more storage space, and using the junk cleanup tool during the retention period does not clean up resource data that has expired during the retention period.
- During tool execution, if there are multiple runs, each run keeps a backup of the current metadata in the `{working-dir}/_current_backup` directory, distinguishing the file name by time.
- The time specified by the user cannot be greater than the current time.
- All service nodes must be turned off before using the tool, otherwise data inconsistencies will result.
- If a user manually deletes the dictionary data for an item and then regenerates the dictionary data, using the rollback tool can cause inconsistencies between the dictionary data and CUBE data.
- A user who has just upgraded a `kylin.storage.time-machine-enabled` configuration needs to wait until a configuration's retention period has passed before being guaranteed to roll back any time within the retention period.
- The user rolls back to the historical moment and the snapshot data used is also the snapshot data for the historical moment, not the latest snapshot data used.
- If the user-specified rollback time is less than the minimum time for metadata backup, it cannot be rolled back.
- `dectect port available failed` -> Failure to detect user ports requires shutting down the service nodes of the cluster.
- `check storage data available failed` -> Failed to detect resource file, user can use `--skip-check-data` parameter to force rollback。
- `restore current metadata failed, please restore the metadata database manually` -> The metadata rollback fails, and overwriting with the current backup also fails. Manual intervention is required to solve the problem. This situation must be handled carefully to avoid loss of metadata.
- The rollback scope of the rollback tool does not include historical recommendations and projects manually deleted by the user.

The following is a detailed process for the tool to perform rollback.

- Backup metadata
- Check if the cluster is stopped
- Find the snapshot file of metadata from the backup directory, and then replay the `auditlog` log to the time specified by the user
- Compare the metadata differences and remind the user
- Wait for confirmation
- Check if the resource referenced to by metadata is available
- Roll back the metadata. If the rollback fails, it will be overwritten with a backup of the current metadata

---

<a id="operations-system-operation-guardian"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/guardian/ -->

<!-- page_index: 101 -->

# Kylin Guardian Process

Version: 5.0.2

Since Kylin 5.0, the system added a function of a daemon process for monitoring the health state of Kylin. This function is called **Kylin Guardian Process**. If the Kylin Guardian Process detects Kylin is in an unhealthy state, it will restart Kylin server or downgrade service.

Kylin Guardian Process is **disabled** by default. If you want to enable it, you need to add the configuration `kylin.guardian.enabled = true` in the global configuration file `$KYLIN_HOME/conf/kylin.properties`.

>
> [!NOTE]
> : All the following configurations take effect if `kylin.guardian.enabled = true`

If Kylin Guardian Process is enabled, a daemon process will be automatically started after starting Kylin. This process is bound to environment variable `KYLIN_HOME`, which means each Kylin instance has only one Kylin Guardian Process corresponding to it.

Kylin Guardian Process description:

- The process ID is recorded in `$KYLIN_HOME/kgid`.
- The log of the process is output in `$KYLIN_HOME/logs/guardian.log`.
- Kylin Guardian Process will periodically check the health status of Kylin. The time delay of the first check is configured by the parameter `kylin.guardian.check-init-delay` (Unit: minutes), the default is 5 minutes, and the check interval is set by the parameter `kylin.guardian.check-interval` (Unit: minutes), the default is 1 minute.

Kylin Guardian Process currently checks the following 4 aspects of Kylin instance's health.

- Kylin process status

  If the process number file `$KYLIN_HOME/pid` exists and the corresponding process does not exist, it means Kylin server is in an abnormal down state, and Kylin Guardian Process will restart it.
- Spark Context restart failure check

  If the number of Spark Context restart failure times is greater than or equals to the value of configuration `kylin.guardian.restart-spark-fail-threshold`, which is 3 times by default, Kylin Guardian Process will restart Kylin. This function is enabled by default. If you want to disable it, please add the configuration `kylin.guardian.restart-spark-fail-restart-enabled = false` in `$KYLIN_HOME/conf/kylin.properties`.
- **Bad Query** canceled failed check

  >
> [!NOTE]
> : Some queries will be forcibly closed due to abnormal reasons. At this time, the query is **Bad Query**, and the common case is a timeout query.

  If Kylin Guardian Process detects the number of Bad Query cancellation times is greater than or equals to the value of configuration `kylin.guardian.kill-slow-query-fail-threshold`, which is 3 times by default, Kylin Guardian Process will restart Kylin. It is enabled by default. If you want to disable it, you can add the configuration `kylin.guardian.kill-slow-query-fail-restart-enabled = false` in `$KYLIN_HOME/conf/kylin.properties`.
- Full GC(Garbage Collection, Garbage collection mechanism in Java) duration check

  If the Full GC duration ratio in most recent period (default is value of `kylin.guardian.full-gc-check-factor` \* value of `kylin.guardian.check-interval`) is greater than or equals to the value of configuration `kylin.guardian.full-gc-duration-ratio-threshold` which is 75% by default, Kylin Guardian Process will restart Kylin. It is enabled by default. If you want to disable it, you can add the configuration `kylin.guardian.full-gc-duration-ratio-restart-enabled = false` in `$KYLIN_HOME/conf/kylin.properties`.

To ensure the high availability of Kylin Guardian Process, Kylin will also periodically check the status of Kylin Guardian Process. If Kylin detects the Kylin Guardian Process does not exist, it will automatically start it. The feature is enabled by default. If you want to disable it, you can add the configuration `kylin.guardian.ha-enabled=false` in `$$KYLIN_HOME/conf/kylin.properties`. The time delay of the first check is configured by the parameter `kylin.guardian.ha-check-init-delay` (Unit: minutes) which is 5 minutes by default, and the check interval is set by the parameter `kylin.guardian.ha-check-interval` (Unit: minutes) which is 1 minute by default.

Kylin Guardian Process supports restarting Kylin when the JVM of Kylin appears OOM.

---

<a id="operations-system-operation-junk_file_clean"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/junk_file_clean/ -->

<!-- page_index: 102 -->

# Junk File Cleanup

Version: 5.0.2

After Kylin runs for a period of time, the system may generate a certain number of junk files, which may occupy a large amount of storage space. At this time, junk cleaning is required.

Junk file cleaning can improve the stability and performance of the Kylin system. Effective junk file cleaning can not only save storage space, but also ensure the ecological health of the cluster where Kylin is located.

By default, the system will automatically clean up junk every day at 0:00 AM.

- To modify the time and frequency of regular junk file cleaning, adjust the parameters in `$KYLIN_HOME/conf/kylin.properties`. The default configuration is `kylin.metadata.ops-cron=0 0 0 * * *`, which refers to junk file cleaning at 0:00 a.m. every day. The parameters from left to right in the configuration items represent: seconds, minutes, hours, Day, month, day of the week. By modifying the cron configuration, users can customize the junk file cleaning time, for example, every Saturday at 11 pm, the corresponding configuration should be changed to `kylin.metadata.ops-cron=0 0 23 * * 6`.
- The default 4-hour timeout for automatic junk file cleaning, and it will automatically terminate after the timeout. The default configuration is `kylin.metadata.ops-cron-timeout=4h`.
- Before the system regularly cleans up junk files, the metadata will be automatically backed up to the HDFS path `{kylin.env.hdfs-working-dir}/{MetadataIdentitiy}/_backup/{yyyy-MM-dd-HH-mm-ss}_backup/ metadata.zip`.
- The system regularly cleans up junk files and will not enter system maintenance mode.
- For more details on cron configuration, please refer to [Introduction to CronTrigger](http://www.quartz-scheduler.org/documentation/quartz-2.3.0/tutorials/crontrigger.html).

The scope of junk file cleanup includes:

- Invalid or expired metadata:

  - Query history.
    - The total number of query history for all projects. The query history that exceeds this threshold number `kylin.query.queryhistory.project-max-size=10000000` (default) will be cleared.
    - The query history of a single project exceeds this threshold `kylin.query.queryhistory.project-max-size=1000000` (default) The query history will be cleared.
    - The query history time of all projects. The query history that exceeds this threshold `kylin.query.queryhistory.survival-time-threshold=30d` (default 30 days) will be cleared. This configuration also supports units: milliseconds ms, microseconds us, minutes m or min, hours h.
  - Invalid optimization suggestion table data.
  - Expired capacity billing metadata. Capacity billing information that exceeds this threshold `kylin.garbage.storage.sourceusage-survival-time-threshold=90d` (default 90 days) will be cleaned up.
  - Invalid or out-of-date item-related metadata.
    - `kylin.garbage.storage.executable-survival-time-threshold=30d` (default 30 days) above this threshold and completed metadata tasks are cleaned up.
  - Audit log. Audit logs that exceed this threshold `kylin.metadata.audit-log.max-size=500000` (default) will be cleaned up.
- Invalid or expired HDFS data:

  - Asynchronous query result file. HDFS asynchronous query result files that exceed this threshold `kylin.query.async.result-retain-days=7d` (default 7 days) will be cleaned up.
  - Invalid or expired files on HDFS. Include invalid or expired indexes, snapshots, dictionaries, etc.
    - Invalid files on HDFS that exceed this threshold `kylin.garbage.storage.cuboid-layout-survival-time-threshold=7d` (default 7 days) are cleaned up.
  - Low Usage indexes on HDFS.
    - Low usage storage refers to indexes whose usage frequency is lower than a certain threshold and data built under them within a certain time interval. You can configure the definition of low usage storage under a project in the project's Settings > Basic Settings > Index Optimization > Low Usage Storage .
    - If recommendation is turned off, indexes with low cost performance will be cleaned according to the index optimization strategy during junk file cleaning. You can also manually clean up by clicking the **Clear** button under **Dashboard > Storage Quota > Low Usage Storage**.
    - If recommendation is turned on, the cleanup of Low Usage storage will no longer be triggered during junk file cleaning, and the corresponding inefficient index will be converted to **model optimization suggestions**, and the button to clean up junk file will not appear in the dashboard.
  > Note: The default timed junk file cleaning method starts from Kylin 5.0 and later, will clean up invalid or expired HDFS data.

> Note: In order to be compatible with the command-line tool cleanup that has been provided in history, the behavior of the previously provided tools has not changed. Users who have used this method can gradually abandon this method according to the actual situation. Users who are not using this tool could not pay attention to this section.

Kylin provides a junk file cleaning command line tool for checking and cleaning HDFS data, so as to ensure that the system is in a good running state. Please execute the following command in the terminal:

```sh
$KYLIN_HOME/bin/kylin.sh org.apache.kylin.tool.routine.RoutineTool 
```

When executing this command without any parameters, it will only list the data in HDFS that can be cleaned, but will not perform the actual cleaning action.

This command supports standard short and long parameters. The parameter descriptions are as follows:

- `-m, --metadata`: Perform metadata junk file cleaning.
- `-c, --cleanup`: Perform data junk file cleanup. Without this parameter, the tool will not make any modification to the HDFS data.
- `-p [project...], --projects=[project...]`: Specifies the projects to clean. When specifying multiple items, separate them with commas. Without this parameter, the tool will clean up all items.
- `-h, --help`: Print help information.
- `-r number`: The number of requests per second when accessing cloud environment object storage. `-r 10` means 10 requests per second. You can use this parameter to limit the frequency of requests for object storage in the cloud environment by the junk file cleaning tool to avoid errors due to exceeding the request frequency limit.
- `-t number`: The number of request retries when accessing the cloud environment object storage fails. `-t 3` means to retry 3 times.

In addition, from Kylin 5, the new command line tool `FastRoutineTool`

```sh
$KYLIN_HOME/bin/kylin.sh org.apache.kylin.tool.routine.FastRoutineTool 
```

The only difference compared to `RoutineTool` is that when performing data junk file cleaning with the `-c` parameter, it does not enter maintenance mode. Maintenance mode is still entered when performing metadata junk file cleanup via -m.

---

<a id="operations-system-operation-limit_query"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-operation/limit_query/ -->

<!-- page_index: 103 -->

# Limit query current capacity, protect query stability

Version: 5.0.2

Query resources are usually limited. During certain periods of time, the query volume suddenly increases, or when a small number of large queries occupy too many resources, query resource competition may occur, resulting in large fluctuations in overall query performance.

In order to avoid the above situation, we can adopt the query current capacity limiting strategy, by rejecting or limiting the performance of part of large queries, to ensure that most of the small queries are not affected, and to ensure the overall stability of the query.

Through long-term observation, we can roughly divide queries into two categories: large queries and small queries. They have different typical characteristics:

- **Big query**: The number is small and the resources are occupied. The fluctuation of the big query has a great impact on the overall stability of the query.
- **Small queries**: The number is large, each small query occupies less resources, protecting small queries can effectively ensure the overall stability of the query.

According to the characteristics of these two types of queries, we have designed different query current limiting strategies, which can be selected as needed. For details, see **two query current limiting strategies** below.

At the same time, for the judgment of large and small queries, we also provide parameters, allowing users to fine-tune according to the actual situation. See below for **Determination of Large Query**.

**Strategy 1: Small query priority scheduling strategy**

After enabling the priority scheduling policy for small queries, small queries will be scheduled first, and large queries will be scheduled later.

Set `kylin.query.query-limit-enabled = true` in `kylin.properties`, the default value is **false**. Also configure Ops Plan to enable large query rejection policy.

**Strategy 2: Large query rejection strategy**

Different from the post-scheduling of large queries in strategy 1, when strategy 2 is used, large queries will be rejected directly after reaching the upper limit of Spark task load. Spark task load refers to the ratio of the number of tasks in the Pending state to the number of tasks in the Running state in the Spark cluster. This strategy requires the cooperation of the Ops Plan to collect the task load indicator, and when the indicator value reaches the upper limit, it triggers the rejection of large queries.

Set `kylin.query.share-state-switch-implement=jdbc` in `kylin.properties`, and configure Ops Plan to enable large query rejection policy. The default value is **close**.

Among them, the default value of Spark task load is 50. Generally, it is not recommended to modify it.

An important factor that affects the effect of the above query current limiting strategy is the determination of large queries. We provide both default values and allow flexible adjustments based on actual queries and system conditions.

**Main principle:**

The system mainly uses **data scan rows** as the basis for judging whether it is a large query. The sum of the number of rows scanned for a query data, when this value exceeds the threshold, it is determined as a large query, otherwise it is a small query. This value may be different from the "Number of records scanned by query" displayed on the page of the query result. This number of rows refers to the number of rows of the parquet file scanned after **pruning**.

**Judgment settings for large queries:**

The system provides the initial threshold setting for determining whether it is a large query and the number of data scan rows, and also provides a mechanism to automatically update this threshold. The configuration of related parameters will be described in detail below.

To adjust, adjust the following parameters in `kylin.properties`:

- `kylin.query.big-query-source-scan-rows-threshold`: Determines whether it is a big query, the initial threshold of the number of rows to be scanned. The default value is `-1` , which means that the user does not specify, and the system automatically calculates the initial threshold at startup. In addition, this threshold can be automatically updated to suit the cluster environment by collecting query information during system operation.
- `kylin.query.auto-adjust-big-query-rows-threshold-enabled`: Whether to automatically update the above thresholds. The default value is false, set to true to enable automatic update.
- `kylin.query.big-query-threshold-update-interval-second`: Interval to automatically update the above threshold. The default value is 10800, in seconds.
- `kylin.query.big-query-second`: The time limit that the big query needs to meet when the above threshold is automatically updated, the default value is 10, in seconds.

In addition, when the query contains limit, the following optimizations can also be enabled to make the automatic update threshold more accurate and avoid misjudgment of large queries.

- `kylin.query.apply-limit-info-to-source-scan-rows-enabled`: Whether to apply limit information to optimize scan row count estimation. The default value is false.

---

<a id="operations-job-monitoring-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/job-monitoring/intro/ -->

<!-- page_index: 104 -->

# Monitor Job

Version: 5.0.2

Kylin introduces a **job monitor** module that allows users to view relevant information and execute jobs on the list.

The job is built in the process of using Kylin, such as building an index and refreshing the source table data, etc.

For a clearer understanding of how to trigger a job, we recommend reading the following sections before continuing with this chapter.

- [Data Source](#datasource-intro)
- [SQL Query](#query-insight)
- [Model](#model-intro)

---

<a id="operations-job-monitoring-job_concept_settings"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/job-monitoring/job_concept_settings/ -->

<!-- page_index: 105 -->

# Job Concept and Settings

Version: 5.0.2

You will build different jobs as you work with Kylin. In this section, we will introduce the types and settings of jobs. The main contents are as follows:

Kylin has these types of jobs：

- Build Index: Job for building new Index.
- Load Data: Job for incrementally loading data on existing models/indices.
- Merge Data: Job for merging segments.
- Refresh Data: Job for refreshing segments.
- Sample Table: Job for table sampling.
- Build Snapshot: Job for building new Snapshots.
- Refresh Snapshot: Job for refreshing snapshots.
- Build Sub-partitions Data: Job for loading sub-partition data of Multi-level partition model.
- Refresh Sub-partitions Data: Job for refreshing sub-partition data of Multi-level partition model.

You can view the job details in the navigation bar **Monitor -> Job**. As shown below, We have created various kinds of jobs.

![Job List](assets/images/job-type-31f94753b4c3f4ea95c0549a034d5bb3_a34d6f1c5a43198c.png)

1. **Build Index**: Job for building new index and loading data.

   - In the navigation bar **Data Asset -> Model**, creating new models will trigger this job.

     > **Tips**: For details on how to build an index, please see [Aggregate Index](#model-manual-aggregation_group).
2. **Load Data**: Job for incrementally loading data on existing models/indices.

   > **Attention**: The start time of loading data must be greater than the end time of the loaded data.

   - In the navigation bar **Data Asset -> Model**, loading data within a time range of the model will trigger the job.
3. **Merge Data**: When the system detects a sufficient number of segments, it will automatically trigger the job of merging data. You can set the parameters of merging segments in the navigation bar **Setting -> Segment Settings**. For detailed message, you can refer to [Segment Operation and Settings](#model-manage-segment).
4. **Refresh Data**: Job for refreshing segments.

   - In the navigation bar **Data Asset -> Model**, refreshing data of a specified segment in the specified model will trigger the job.

     > **Attention**：If you refresh n segments at the same time, it will trigger n jobs to refresh the data, and arrange them in the job queue according to the chronological order of original segments. You can view them in the **Monitor -> Job** bar.
5. **Sample Table**: Job for data sampling of a table. This job can obtain characteristics of the table data. Table sampling jobs can be triggered automatically or manually.

   - Automatically: The job is automatically triggered when you add a data source in the navigation bar **Data Asset -> Data Source**.

     > **Attention**: Table sampling is enabled by default. If you manually turn it off, this job will not be triggered.
   - Manually: You can trigger a table sampling job in the navigation bar **Data Asset -> Data Source**. Click on the **Sample** button or **Reload** button to trigger this kind of jobs.

     > **Attention**：The "Reload" button will reload the data from the table.
6. **Build Snapshot**：Job for building new Snapshots. This job only appears when you manually add a snapshot after snapshot management is enabled.
7. **Refresh Snapshot**：Job for refreshing snapshots. This job only appears when you manually refresh a snapshot after snapshot management is enabled.
8. **Build Sub-partitions Data**: Enable multi-level partition, and the model is a multi-level partition model, job for loading sub-partition data.
9. **Refresh Sub-partitions Data**:Enable multi-level partition, and the model is a multi-level partition model, job for refreshing sub-partition data.

In the navigation bar **Monitor -> Job**, click the triangle button on the left to expand and view the job details.
Some of the elements include job steps, waiting time and executing time, log output and job parameters, etc:

1. **Job Steps**:
   According to job type, the job is subdivided into the first and second level job steps, so that users can better understand the job execution.

   Take the job of building index and loading data type as an example, the first-level job steps are:

   - Detect Resource
   - Load Data to Index
   - Update Metadata
   - Upload Data to Tiered Storage

   The **Load Data to Index** step is subdivided into second-level job steps:

   - Waiting for yarn resources
   - Build or refresh snapshot
   - Materialize fact table view
   - Generate global dictionary
   - Generate flat table
   - Get flat table statistics
   - Build indexes by layer
   - Update flat table statistics

   Note: Depending on the actual situation, the job may only perform some of the above steps.
2. **Waiting time and Executing time**:

   Job waiting time is the waiting time due to concurrency restrictions or resource restrictions.

   Job executing time is the actual execution time of the job, excluding the job suspension time.
3. **Log output**: The job-related logs in `kylin.log`, it can assist in the diagnosis of job abnormalities.
4. **Job parameters**: Spark parameters related to the job, it can assist in the diagnosis of job abnormalities.

> Tip: Subdivided second-level job steps and job parameters have been introduced since Kylin version 4.5.3.

You can modify settings about **Email Notification** in the navigation bar **Setting -> Advanced Settings**, as shown below:

![Job Notification](assets/images/job-settings-c1c02a2f777b3ff8e3ceba196feb1d64_ff3b0988ed75b5f2.png)

You can fill in your email and choose to open different types of job notification.

> **Tips**: You can make different job notifications for different projects.

**Q: Why is my job suspended without error?**

We set the priority of jobs according to the influence of different types of jobs on the actual business, and the details is as follows:

- High priority job: Loading Data
- Secondary priority job: Building Index, Merging Data, Refreshing Data

When a job with a secondary priority reports an error, other jobs with the same priority of this model/index will be suspended. However, jobs of different models/indices will not be affected.

**Q: Why did my previously completed jobs disappear from the job list?**

Up to 30 days of job records are kept in the Kylin. Job records more than 30 days can be queried in the deployment file of the installation package.

**Q: Is there a limit on the number of concurrent jobs for Kylin? What should I do if I exceed the number of concurrency allowed by the system when submitting a job?**

By default, Kylin automatically controls the number of concurrency based on the system resources available. You can turn it off by modifying the parameter `kylin.job.auto-set-concurrent-jobs` in the system configuration file `kylin.properties`.

When auto-control is turned off, the maximum concurrency in a single project is **20** by default, which can be changed by modifying the parameter `kylin.job.max-concurrent-jobs` in the system configuration file `kylin.properties`.

When submitting a new job, if the number of concurrency exceeds what is allowed, this job will enter the job queue. When a running job is finished, Kylin will schedule a job in the queue to execute in a first-in-first-out (FIFO) manner.

---

<a id="operations-job-monitoring-job_operations"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/job-monitoring/job_operations/ -->

<!-- page_index: 106 -->

# Job Operations

Version: 5.0.2

You can perform job operations on Kylin's job monitor page. In this section we will tell you about the status and meaning of jobs. The main contents are as follows:

The job has the following 6 states：

- **PENDING**：The status of the job waits for scheduled execution.
- **RUNNING**：The status of the job means running normally. You can view the progress of the execution and the progress is shown in percentage.
- **PAUSED**：The status of the job suspends normal execution.
-
> [!CAUTION]
> **ERROR**
> ：When the job encountered a problem that cannot be continued, the interface displays the status of the error.

- **DISCARDED**：The job is reported to terminate the execution status. And the terminated job will immediately stop and release all resources.

  > Prompt：When the job's execution object no longer exists or changes, the system will automatically terminate the job.
- **FINISHED**：The status of the job is completed normally.

You can view the job status information in the **Monitor -> Job** interface of navigation bar. As shown below:

![Job Status](assets/images/job-status-cf1717b044b64156147cd66dd3cdb9d1_7a4b73edb320593c.png)

- Label 1: Execution status.
- Label 2: Pause status.
- Label 3: Finished status.
- Label 4: Error Status.
- Label 5: Termination Status.
- Label 6: Batch operation for selected jobs.
- Label 7: Operation for a single job.

- **Resume**：Start with an intermediate step in the job and continue with the job.

  > Note：If a job is in error status. After the user troubleshoots or solves the problem of the job. The user can retry this execution through this operation.
- **Restart**：Abandon the results of the intermediate steps and re-execute jobs from the beginning.

  > Note：For jobs in error status, if the execution subjects have changed, for instance, the schema of a source table has changed, we'll recommend user to restart the job. And records of jobs before this time will be removed and restart a new job.
- **Pause**：Pause the current job and release all related resources.
- **Discard**: Discard jobs and release all related resources.

  > Note: After discarded the jobs, it cannot be undone or restored by restart operation.
- **Delete**：Delete jobs.
- **Refresh** ：Refresh job list information.

In the job monitor page, ADMIN users can view all job information via **Select All** option in the project list. After selecting that, the **Project** column will appear in the job list and you can operate the jobs in batches across projects.

---

<a id="operations-job-monitoring-job_diagnosis"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/job-monitoring/job_diagnosis/ -->

<!-- page_index: 107 -->

# Job Diagnosis

Version: 5.0.2

Job diagnosis may encounter various problems during execution. To help solve these problems efficiently, Kylin provides a task diagnostic function, which can package related problems' log information into a compressed package for operations or Apache Community supports to analyze problems and ascertain the cause.

You can view the job execution log in the  `Monitor -> Batch Job` interface. As shown below, you can click the **Open Job Steps** button at the position 1, and then click the **Log Output** button in the job details to view the first and the last 100 lines of job execution log in a popup window. You can download the full log by clicking the link **download the full log** at the position 3.

>
> [!TIP]
> : If there are multiple steps in a job, you can view the execution log for each step.

![Job Log](assets/images/job-log-f2db1a5907661e2d9f384441f440290f_66d94c442e91c7fe.png)

In FusionInsight, you need to execute the command `source /opt/hadoopclient/bigdata_env` first. The `hadoopclient` is a variable.

You can execute `$KYLIN_HOME/bin/diag.sh -job <jobid>` to generate the job diagnostic package and <jobid> need to be replaced with the actual job ID number. You can view the job ID number in the  `Monitor -> Batch Job` interface. You can also click the icon in the position 1 as shown picture below to expand the specified job details that is in the position 2 on the right.

![Job ID](assets/images/job-id-3e4c054f3ae5b0ac08081d163d4b7b3c_a0a9cef056d34869.png)

The diagnostic package is stored by default in the `$KYLIN_HOME/diag_dump/` directory.

After extracting the diagnostic package, you can view the diagnostic package information in the appropriate directory or file.

- `/conf`: configuration information under the `$KYLIN_HOME/conf` directory.
- `/hadoop_conf`: configuration information under the `$KYLIN_HOME/hadoop_conf` directory.
- `/metadata`: metadata files.
- `/logs`: specifies the logs generated during the execution of job.
- `/spark_logs`: specifies all spark executor logs generated during job execution.
- `/system_metrics`: specifies the system metrics during the execution of job.
- `/audit_log`: specifies the audit logs during the execution of job.
- `/job_tmp`: specifies the temporary files, logs and optimization suggestions log of job.
- `/yarn_application_log`: specifies the logs of yarn application of job.
- `/client`: operating system resources occupied information, hadoop version and kerberos information.
- `/monitor_metrics`：The node monitoring log of the specified task.
- `/write_hadoop_conf`：`$KYLIN_HOME/write_hadoop_conf`, Hadoop configuration of the build cluster. This directory will not be available when Read/Write separation deployment is not configured.
- file `catalog_info`: directory structure of install package.
- file `commit_SHA1`: git-commit version.
- file `hadoop_env`: hadoop environment information.
- file `info`: license, package and hostname.
- file `kylin_env`: Kylin version, operating system information, Java related information, git-commit information.

> **Tips**: If you want to exclude metadata files, please specify `-includeMeta false`.

Job diagnostic package includes all diagnostic information of a specific job, and users can generate job diagnostic package on Web UI by following the following steps:

![Generate Job Diagnostic Package in Web UI](assets/images/job-diagnosis-web-53e5190c6c4d4c14be30c8820be751f0_79517ecec237c3c2.png)

1. In the action bar of a job on the **Jobs List** page, click the **Download Job Diagnostic Package** button in **Actions**.
2. Select **Server**.
3. Click **Generate and Download** button: After the diagnostic package is generated, the downloads will be triggered automatically. If the diagnostic package generation fails, you can view the details of the failure on the interface.

---

<a id="operations-job-monitoring-job_exception_resolve"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/job-monitoring/job_exception_resolve/ -->

<!-- page_index: 108 -->

# Common Job Error Causes and Solutions

Version: 5.0.2

Various problems may occur during the execution of building jobs which cause the job to fail. Usually, the brief error cause and description are directly displayed in the job details. This article will summarize some common error causes and solutions to assist solving problems.

- **ErrorCode：** KE-030001003
- **Description：**

  In the time partition setting of model, the time format of the time partition column is inconsistent with the actual time format in the data source. The key information in the log is:`date format not match`。
- **Solution：**

  1. Modify the time format of the model time partition column to be consistent with the actual time format in the data source:

     Please refer to [Design a Data Model](#model-manual-modeling--save-model). Save the model and set the loading method\* modify the time format of the model time partition column。
  2. 2. If you insist on using this format, you can choose to disable checking the time partition column by modifying the system parameter in `kylin.properties` to `kylin.engine.check-partition-col-enabled=false`.
        Notice: Although this method can bypass the time format verification here, it may cause other problems. Please use it with caution.

- **ErrorCode：** KE-030001004
- **Description：** Spark Driver/Executor has OOM during building. The key information in the log is: `OutOfMemoryError`.
- **Solution：**

  1. Adjust spark.sql.shuffle.partitions

     During the build process, if there are MetadataFetchFailedException, executor lost, oom problems, you can try to adjust the following parameters:

     - kylin.engine.spark-conf.spark.sql.shuffle.partitions

     This parameter determines the number of partitions during aggregate or join execution, and the default is 200.
  2. Improve build resources

     In general, using more resources can significantly improve performance and fault tolerance by tuning cores and memory used by builds with the following parameter :

     - kylin.engine.spark-conf.spark.executor.instances
     - kylin.engine.spark-conf.spark.executor.cores
     - kylin.engine.spark-conf.spark.executor.memory
     - kylin.engine.spark-conf.spark.executor.memoryOverhead

- **ErrorCode：** KE-030001005
- **Description：** The building job reports an error: no space left on device. The key information in the log is: `No space left on device`.
- **Solution：**

  1. Please check Kylin and the cluster disk space used for building, clean up invalid files or expand capacity in time.
  2. Try to clean up Kylin's inefficient storage.
  3. For `shuffle no left space on device` problem, you can appropriately increase the number of executor instances to use more computing resources.

     - spark.executor.cores
     - spark.executor.instances

- **ErrorCode：** KE-030001006
- **Description：** The class was not found during building. The key information in the log is: `ClassNotFoundException`.
- **Solution：**

  1. Missing Mysql driver(`java.lang.ClassNotFoundException: com.mysql.jdbc.Driver`)

     Please refer to [Use MySQL as Metastore](#deployment-rdbms_metastore-use_mysql_as_metadb) set up Mysql as metabase.

- **ErrorCode：** KE-030001007
- **Description：** Kerberos is not configured correctly, resulting Kerberos realm being not found. The key information in the log is: `Can't get Kerberos realm`.
- **Solution：**

  1. Double check Kerberos configuration
     1. For both Yarn Cluster and Yarn Client modes, the krb5.conf file in `{KYLIN_HOME}/conf/` and `{KYLIN_HOME}/hadoop_conf/` should be checked to prevent any failure related to Kerberos realm.
     2. If Yarn Cluster mode is chosen, please pay more attention to the Kerberos config in `{KYLIN_HOME}/spark/conf/spark-env.sh` file.

---

<a id="operations-system-monitoring-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-monitoring/intro/ -->

<!-- page_index: 109 -->

# System Monitoring

Version: 5.0.2

This chapter will introduce how to enable system monitoring.

---

<a id="operations-system-monitoring-influxdb-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-monitoring/influxdb/intro/ -->

<!-- page_index: 110 -->

# InfluxDB

Version: 5.0.2

Kylin supports to use InfluxDB as its time series database, this chapter will cover:

- [Use InfluxDB as Time-Series Database](#operations-system-monitoring-influxdb)
- [InfluxDB Maintenance](#operations-system-monitoring-influxdb-influxdb_maintenance)

---

<a id="operations-system-monitoring-influxdb"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-monitoring/influxdb/ -->

<!-- page_index: 111 -->

# Use InfluxDB as Time-Series Database

Version: 5.0.2

Starting with Kylin 5.0, the system uses RDBMS to store query history, which only use InfluxDB to record the monitoring information of the system.

If you need this information, you need to configure the time series database InfluxDB in advance to store data such as the monitoring information of the system.

We recommend you to use InfluxDB v1.6.4, which can download by the script `$KYLIN_HOME/sbin/download-influxdb.sh`.

The InfluxDB installation package, `influxdb-1.6.4.x86_64.rpm` will be under the `influxdb` directory in the installation directory of Kylin.

If you need to use the existed InfluxDB database in your environment, please use the versions below:

- InfluxDB 1.6.4 or above

You can use the following command to check the version of InfluxDB in your current environment.

```shell
service influxdb version 
```

The following steps are using InfluxDB 1.6.4 as an example.

1. Run command to check if InfluxDB is installed already.


```shell
service influxdb status 
```

   If not, you can download the influxdb and go to the directory where the InfluxDB installation package is located and install InfluxDB.


```shell
# download influxDB $KYLIN_HOME/sbin/download-influxdb.sh
 
# go to influxDB directory and install it cd $KYLIN_HOME/influxdb rpm -ivh influxdb-1.6.4.x86_64.rpm
```

2. Launch InfluxDB.


```sh
service influxdb start 
```

   By default, you can find InfluxDB's log at `/var/log/influxdb`.
3. If your InfluxDB server port is in use, you can modify the InfluxDB configuration file to change the server port.


```sh
vi /etc/influxdb/influxdb.conf 
```

   Please note the following three points:

   - Modify RPC port: The initial property is `bind-address = "127.0.0.1:8088"`, you can change `8088` to an available port, for instance, `18087`.
   - Modify HTTP port: The initial property is `bind-address = ":8086"`, you can change `8086` to available port, for instance, `18086`.
   - Set `reporting-disabled = true`, which means that the InfluxDB will not send reports to [influxdata.com](https://www.influxdata.com/) regularly.
4. InfluxDB is accessible without a user name and password by default. If you want to strengthen the security level, you can set a password with the following steps:
5. log in InfluxDB.

```sh
influx -port 18086  
```

**Tips:** Please replace `18086` with an actually available port number.

2. Manage admin user and password.


```mariadb
CREATE USER admin WITH PASSWORD 'admin' WITH ALL PRIVILEGES 
```

3. Open the configuration file and modify  `[http] auth-enabled = true` to enable authorization.


```sh
vi /etc/influxdb/influxdb.conf  
```

4. Restart InfluxDB to take effect and login InfluxDB.


```sh
service influxdb restart 
influx -port 18086 -username admin -password admin  
```

5. Open the property file `kylin.properties` and modify the InfluxDB configurations. Please replace `ip:http_port`, `user`, `pwd`, `ip:rpc_port` with real values.

```properties
 vi $KYLIN_HOME/conf/kylin.properties  
  
 ### Modify the following properties 
  
 kylin.influxdb.address=ip:http_port 
 kylin.influxdb.username=user 
 kylin.influxdb.password=pwd 
 kylin.metrics.influx-rpc-service-bind-address=ip:rpc_port 
```

> [!NOTE]
> : If more than one Kylin instances are deployed, you should configure the above configurations in `kylin.properties` for each Kylin node and let them point to the same Influxdb instance.

6. Encrypt influxdb password

   If you need to encrypt influxdb's password, you can do it like this：

   **i.** run following commands in `${KYLIN_HOME}`, it will print encrypted password


```shell
./bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s <password> 
```

   **ii.** config kylin.influxdb.password like this


```properties
kylin.influxdb.password=ENC('${encrypted_password}') 
```

   **iii.** Here is an example, assuming influxdb's password is kylin

   First, we need to encrypt kylin using the following command


```shell
${KYLIN_HOME}/bin/kylin.sh org.apache.kylin.tool.general.CryptTool -e AES -s kylin 
AES encrypted password is: 
YeqVr9MakSFbgxEec9sBwg== 
```

   Then, config kylin.metadata.url like this：


```properties
kylin.influxdb.password=ENC('YeqVr9MakSFbgxEec9sBwg==') 
```

7. start Kylin.

The following steps are using InfluxDB 1.6.4 as an example.

1. Suppose you install as user `abc` . Then create a directory `home/abc/influx` to copy the InfluxDB installation package, `influxdb-1.6.4.x86_64.rpm` ,from `$KYLIN_HOME/influxdb` to this directory after executing download influxDB script.


```sh
# download influxDB $KYLIN_HOME/sbin/download-influxdb.sh
 
mkdir /home/abc/influx 
cp $KYLIN_HOME/influxdb/influxdb-1.6.4.x86_64.rpm /home/abc/influx 
cd /home/abc/influx 
rpm2cpio influxdb-1.6.4.x86_64.rpm | cpio -idmv 
```

2. Edit the InfluxDB configuration file and replace `/var/lib` with `/home/abc/influx` globally. Also, you can modify `bind-address` property according to your case.


```sh
vi /home/abc/influx/etc/influxdb/influxdb.conf 
```

3. Run following command to launch InfluxDB.

```sh
 nohup ./usr/bin/influxd run -config /home/abc/influx/etc/influxdb/influxdb.conf & 
```

By default, you can find InfluxDB's log at `/home/abc/influx/var/log/influxdb`.

4. As for other configurations, please refer to the second part in this section [`root` User Installation And Configuration](#operations-system-monitoring-influxdb--root). Note that if you want to restart influxdb, you need to execute the following commands. Using `service influxdb restart` will not work since it requires root permission.


```sh
ps -ef | grep influxdb 
kill {pid} 
```

5. Launch Kylin.

To ensure the connectivity of InfluxDB service, it is recommended that you perform some tests after starting InfluxDB.

- Log in to InfluxDB by entering the command line in the terminal:


```sh
/home/abc/influx/usr/bin/influx -port 18086 -username ${username} -password ${pwd} 
```

  If the login fails, you can set `auth-enabled = true` in the configuration file `influxdb.conf` and try to login again.
- After successful login , you can execute some simple queries to check if InfluxDB is configured correctly:


```sql
show databases; 
```

  If the query fails and the message `authorization failed` is displayed, please confirm whether the user has sufficient permissions.

For more information about InfluxDB connectivity, please refer to the [InfluxDB Maintenance](#operations-system-monitoring-influxdb-influxdb_maintenance) section.

Before using HTTPS to connect to InfluxDB, you need to enable InfluxDB's HTTPS connection. To enable HTTPS for InfluxDB please refer to the official documentation: [Enabling HTTPS with InfluxDB](https://docs.influxdata.com/influxdb/v1.6/administration/https_setup/)。

If the InfluxDB you are using has enabled HTTPS connection, please set the following parameters in the `$KYLIN_HOME/conf/kylin.properties` configuration file:

```text
kylin.influxdb.https.enabled=true 
```

---

<a id="operations-system-monitoring-influxdb-influxdb_maintenance"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-monitoring/influxdb/influxdb_maintenance/ -->

<!-- page_index: 112 -->

# InfluxDB Maintenance

Version: 5.0.2

This chapter introduces the basic maintenance of InfluxDB.

When InfluxDB is not accessible, you can locate the problem from the following aspects:

1. Check if InfluxDB is running normally by executing `service influxdb status`. If it is not running, please check log files of `/var/log/influxdb/influxd.log` or `/var/log/messages` to find out the reason, at the same time, run `service influxdb restart` to restart InfluxDB service and make sure the service can be launched normally by observing the logs. (You should be able to login InfluxDB via `influx -host ? -port ?` command)
2. If you find the port has been taken in the starting process, run `netstat -anp | grep influxdb_port` to get the process id, and execute `ps -ef | grep pid` to get the specific process. You can choose to kill the process if you do not need it or to change InfluxDB's server port to another.
3. If you are having your Kylin and InfluxDB installed in different nodes, please execute `telnet influxdb_ip influxdb_port` on Kylin node to check if two nodes can communicate normally, if not, please make sure the Firewall service is not turned on on InfluxDB node via `service iptables status` command or contact the system admin to check the network condition.

- **Log Configuration**

  - By default, InfluxDB writes standard error to log. InfluxDB redirects stderr to `/var/log/influxdb/influxd.log` file when it is started. If you would like to change the log path, please modify the property in the configuration file `/etc/default/influxdb` to `STDERR=/path/to/influxdb.log`, and restart the service via `service influxdb restart` command.
  - InfluxDB enables HTTP access log by default. Generally, HTTP access log is quite large, you can modify the property `[http] log-enabled=false` to disable the log output.
- **Log Clean**

  InfluxDB itself does not clean its log regularly, it uses **logrotate** to manage log, which is installed on Linux system by default. The configuration file of **logrotate** is located at `/etc/logrotate.d/influxdb`, the log rotates by day, and the retention is 7 days.

InfluxDB provides the availability to do backup and restore.

- **Backup**


```sh
influxd backup -portable -database KYLIN_METRIC -host 127.0.0.1:8089 /path/to/backup 
```

- **Restore**

  Please make sure that the database exists, otherwise the restore will be failed.


```sh
influxd restore -portable -database KYLIN_METRIC -host 127.0.0.1:8089 /path/to/backup 
```

> **note:** Please replace KYLIN\_METRIC with the actual database name, replace 127.0.0.1:8089 with the actual IP and port, replace `/path/to/backup` with the path you would like to set.

- **Memory Monitoring**

  - Check runtime

    Run following command to check GC, memory usage, etc.
    `influx -database KYLIN_METRIC -execute "show stats for 'runtime'"`

    Please focus on these important arguments:

    - *HeapAlloc* -> Heap allocation size
    - *Sys* -> The total number of bytes of memory obtained from the system
    - *NumGC* -> GC times
    - *PauseTotalNs* -> The total GC pause time
  - Check the memory usage of InfluxDB index

    `show stats for 'indexes'`
  - Monitor InfluxDB memory usage

    Run following command:

    `pidstat -rh -p PID 5`

    If the memory usage is too high or GC is too frequent, please increase memory.

    > **tips:** It is recommended to install InfluxDB on a separate machine with high memory allocation, because data read and write speed are dependent on the indexes, and the indexes are stored in memory.
- **Disk Monitoring**

  Run following command to check disk situation:


```sh
pidstat -d -p PID 5 
```

  When the disk read/write load is found to be too high, you can consider mapping the WAL directory and the data directory to different disks to reduce the interaction between read and write operations.

  1. Run `vi /etc/default/influxdb` to edit the configuration file.
  2. Modify the properties `[data] dir = "/var/lib/influxdb/data"` and `wal-dir = "/var/lib/influxdb/wal"` to point WAL directory and data directory to different disk.
- **Read/Write Response Time**

  1. Write:


```sql
SELECT non_negative_derivative(percentile("writeReqDurationNs", 99)) / non_negative_derivative(max("writeReq")) / (1000 * 1000) AS "Write Request"  
FROM "_internal".."httpd"  
WHERE time > now() - 10d  
GROUP BY time(1h) fill(0) 
```

  2. Read:


```sql
  SELECT non_negative_derivative(percentile("queryReqDurationNs", 99)) / non_negative_derivative(max("queryReq")) / (1000 * 1000) AS "Query Request"  
  FROM "_internal".."httpd"  
  WHERE time > now() - 10d  
  GROUP BY time(1h) 
```

---

<a id="operations-system-monitoring-metrics_intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-monitoring/metrics_intro/ -->

<!-- page_index: 113 -->

# Metrics Monitoring

Version: 5.0.2

By default, the system collects metric data every minute, including storage, query, job, metadata, and cleanup mechanism. The monitoring data is stored in the specified [InfluxDB](https://www.influxdata.com/time-series-platform/) and displayed through [Grafana](https://grafana.com/grafana). It can help administrators to understand the health of the system in order to take necessary actions.

>
> [!NOTE]
> : Since Grafana depends on **InfluxDB**, please make sure that InfluxDB is correctly configured and started according to [Use InfluxDB as Time-Series Database](#operations-system-monitoring-influxdb) and download **Grafana** before you use Grafana.

```shell
# Download Grafana $KYLIN_HOME/sbin/download-grafana.sh
```

>
> [!NOTE]
> : The Grafana installation path, will be under the `grafana` directory in the installation directory of Kylin.

1. **Working Directory**:  `$KYLIN_HOME/grafana`
2. **Configuration Directory**: `$KYLIN_HOME/grafana/conf`
3. **Start Grafana Command**: `$ KYLIN_HOME/bin/grafana.sh start`
4. **Stop Grafana Command**:  `$ KYLIN_HOME/bin/grafana.sh stop`

> Changing grafana configuration please refer to [Configuration](https://grafana.com/docs/installation/configuration/).

After the startup is successful, you may access Grafana through web browser with default port: 3000, username: admin, password: admin

![metrics_dashboard](assets/images/dashboard-b39976d1ab16ecc3cddc654e6b15ef20_5b73d1987946e4f5.jpg)

Default Dashboard: `Kylin 5.0`

The dashboard consists of 10 modules: Cluster, Summaries, Models, Queries, Favorites, Jobs, Cleanings, Metadata Operations, Transactions, among which Summaries module is automatically displayed in detail. Read more details about the modules, please refer to [Metrics Explanation](#operations-system-monitoring-metrics_intro--explanation). If you want to make some changes for the dashboard, please refer to Grafana official website manual [Provisioning Grafana](https://grafana.com/docs/administration/provisioning/).

Each indicator monitor corresponds to a specific panel.

In the upper right corner of the dashboard, choose the time range. Time range: the time interval in which the indicator was observed.
![metrics_interval](assets/images/interval-7eb11b0b7b0a4d52dd8ed72da8a595da_a2c6efca159710d0.png)

Located in the upper left corner of the dashboard, the data granularity: auto, 1m, 5m, 10m, 30m, 1h, 6h, 12h, 1d, 7d, 14d, 30d ('auto' is automatically adjusted according to the time range, such as the time range '30min' corresponding granularity 5min, and the granularity corresponding to the time range of 24h is 4h).

- [**Cluster**: Cluster overiew](#operations-system-monitoring-metrics_intro--cluster)
- [**Summaries**: Global overview](#operations-system-monitoring-metrics_intro--summaries)
- [**Models**: Model related metrics](#operations-system-monitoring-metrics_intro--models)
- [**Queries**: Query related metrics](#operations-system-monitoring-metrics_intro--queries)
- [**Favorites**: Favorite Query related metrics](#operations-system-monitoring-metrics_intro--favorites)
- [**Jobs**: Job related metrics](#operations-system-monitoring-metrics_intro--jobs)
- [**Cleanings**: Cleanup mechanisms related metrics](#operations-system-monitoring-metrics_intro--cleanings)
- [**Metadata Operations**: Metadata operations related metrics](#operations-system-monitoring-metrics_intro--metadata)
- [**Transactions**: Transaction mechanisms related metrics](#operations-system-monitoring-metrics_intro--transactions)

> \*\*Tip \*\*: “Project related” in the following table indicates whether the metric is related to the project, “Y” indicates that the metric is related to the project, and “N” indicates that the metric is not related to the project. "Host related" in the following table indicates whether the metric is related to Kylin nodes, "Y" indicates that the metric is related to the Kylin nodes, "N" indicates that the metric is not related to the host. "all", "job", "query" is Kylin nodes' server mode.

| Name | Meaning | Project related |
| --- | --- | --- |
| build\_unavailable\_duration | the unavailable time of building | N |
| query\_unavailable\_duration | the unavailable time of query | N |

**Summaries**: Global overview

| Name | Meaning | Project related | Host related | Remark |
| --- | --- | --- | --- | --- |
| summary\_exec\_total\_times | Times of all indicators collected | N | Y(all, job, query) | The cost of collecting indicators |
| summary\_exec\_total\_duration | Duration of all indicators collected | N | Y(all, job, query) | The cost of collecting indicators |
| num\_of\_projects | Total project number | N | N | - |
| storage\_size\_gauge | Storage used of the system | Y | N | - |
| num\_of\_users | Total user number | N | N | - |
| num\_of\_hive\_tables | Total data table number | Y | N | - |
| num\_of\_hive\_databases | Total database number | Y | N | - |
| summary\_of\_heap | The heap size of Kylin | N | Y(all, job, query) | - |
| usage\_of\_heap | The ratio of heap of Kylin | N | Y(all, job, query) | - |
| count\_of\_garbage\_collection | The count of garbage collection | N | Y(all, job, query) | - |
| time\_of\_garbage\_collection | The total time of garbage collection | N | Y(all, job, query) | - |
| garbage\_size\_gauge | Storage used of garbage | Y | N | Refer to the definition of "Garbage" |
| sparder\_restart\_total\_times | "Sparder" restart times | N | Y(all, job, query) | "Sparder" is the internal query engine |
| query\_load | spark sql load | N | Y(all, query) | - |
| cpu\_cores | The number of cup cores for query configured in kylin.properties | N | Y(all, query) | Refer "Spark-related Configuration" |

| Name | Meaning | Project related | Host related |
| --- | --- | --- | --- |
| model\_num\_gauge | "Model number: curve with time | Y | N |
| non\_broken\_model\_num\_gauge | "Healthy model number" curve with time | Y | N |
| last\_query\_time\_of\_models | The last query time of models | Y | N |
| hit\_count\_of\_models | The query hit count of models | Y | N |
| storage\_of\_models | The storage of models | Y | N |
| segments\_num\_of\_models | The num of segments of models | Y | N |
| model\_build\_duration | Total build time of models | Y | N |
| model\_wait\_duration | Total wait time of models | Y | N |
| number\_of\_indexes | indexes number of models | Y | N |
| expansion\_rate\_of\_models | Expansion rate of models | Y | N |
| model\_build\_duration (avg) | Avg build time of models | Y | N |

| Name | Meaning | Project related | Host related | Remark |
| --- | --- | --- | --- | --- |
| count\_of\_queries | Total count of queries | Y | Y(all, query) | - |
| num\_of\_query\_per\_host | The num of query per host | N | Y(all, query) | - |
| count\_of\_queries\_hitting\_agg\_index | The count of queries hitting agg index | Y | Y(all, query) | - |
| ratio\_of\_queries\_hitting\_agg\_index | The ratio of queries hitting agg index | Y | Y(all, query) | - |
| count\_of\_queries\_hitting\_table\_index | The count of queries hitting table index | Y | Y(all, query) | - |
| ratio\_of\_queries\_hitting\_table\_index | The ratio of queries hitting table index | Y | Y(all, query) | - |
| count\_of\_pushdown\_queries | The count of pushdown queries | Y | Y(all, query) | - |
| ratio\_of\_pushdown\_queries | The ratio of pushdown queries | Y | Y(all, query) | - |
| count\_of\_queries\_hitting\_cache | The count of queries hitting cache | Y | Y(all, query) | - |
| ratio\_of\_queries\_hitting\_cache | The ratio of queries hitting cache | Y | Y(all, query) | - |
| count\_of\_queries\_less\_than\_1s | Total count of queries when duration is less than 1 second | Y | Y(all, query) | - |
| ratio\_of\_queries\_less\_than\_1s | The ratio of queries when duration is less than 1 second | Y | Y(all, query) | - |
| count\_of\_queries\_between\_1s\_and\_3s | Total count of queries when duration is between 1 second and 3 seconds | Y | Y(all, query) | - |
| ration\_of\_queries\_between\_1s\_and\_3s | The ratio of queries when duration is between 1 second and 3 seconds | Y | Y(all, query) | - |
| count\_of\_queries\_between\_3s\_and\_5s | Total count of queries when duration is between 3 seconds and 5 seconds | Y | Y(all, query) | - |
| ratio\_of\_queries\_between\_3s\_and\_5s | The ratio of queries when duration is between 3 seconds and 5 seconds | Y | Y(all, query) | - |
| count\_of\_queries\_between\_5s\_and\_10s | Total count of queries when duration is between 5 seconds and 10 seconds | Y | Y(all, query) | - |
| ratio\_of\_queries\_between\_5s\_and\_10s | The ratio of queries when duration is between 5 seconds and 10 seconds | Y | Y(all, query) | - |
| count\_of\_queries\_greater\_than\_10s | Total count of queries when duration exceeding 10 seconds | Y | Y(all, query) | - |
| ratio\_of\_queries\_greater\_than\_10s | The ratio of queries when duration exceeding 10 seconds | Y | Y(all, query) | - |
| count\_of\_timeout\_queries | The count of timeout queries | Y | Y(all, query) | - |
| count\_of\_failed\_queries | The count of failed queries | Y | Y(all, query) | - |
| mean\_time\_of\_query\_per\_host | The mean time of queries per host | N | Y(all, query) | - |
| 99%\_of\_query\_latency | Query duration 99-percentile | Y | Y(all, query) | - |
| gt10s\_query\_rate\_5-minute | Query duration exceeding 10s per second over 5 minutes | Y | Y(all, query) | - |
| failed\_query\_rate\_5-minute | Failed queries per second over 5 minutes | Y | Y(all, query) | - |
| pushdown\_query\_rate\_5-minute | Pushdown queries per second over 5 minutes | Y | Y(all, query) | - |
| scan\_bytes\_of\_99%\_queries | Query scan bytes 99-percentile | Y | Y(all, query) | - |
| query\_scan\_bytes\_of\_host | Query scan bytes per host | N | Y(all, query) | - |
| mean\_scan\_bytes\_of\_queries | The mean scan bytes of queries | Y | Y(all, query) | - |

| Name | Meaning | Project related | Host related | Remark |
| --- | --- | --- | --- | --- |
| fq\_accepted\_total\_times | Favorite Query user submitted total times | Y | Y(all, job, query) | - |
| fq\_proposed\_total\_times | Favorite Query system triggered total times | Y | N | - |
| fq\_proposed\_total\_duration | Favorite Query system triggered total duration | Y | N | - |
| failed\_fq\_proposed\_total\_times | Favorite Query system triggered failed total times | Y | N | Refer to the definition of "pushdown" |
| fq\_adjusted\_total\_times | Favorite Query system adjusted total times | Y | Y(all, job, query) | - |
| fq\_adjusted\_total\_duration | Favorite Query system adjusted total duration | Y | Y(all, job, query) | - |
| fq\_update\_usage\_total\_times | Favorite Query usage updated total times | Y | N | - |
| fq\_update\_usage\_total\_duration | Favorite Query usage updated total duration | Y | N | - |
| failed\_fq\_update\_usage\_total\_times | Favorite Query usage updated failed total times | Y | N | - |
| fq\_tobeaccelerated\_num\_gauge | Favorite Query to be accelerated | Y | N | - |
| fq\_accelerated\_num\_gauge | Favorite Query accelerated | Y | N | - |
| fq\_failed\_num\_gauge | Favorite Query accelerated failed times | Y | N | - |
| fq\_accelerating\_num\_gauge | Favorite Query accelerating | Y | N | - |
| fq\_pending\_num\_gauge | Favorite Query pending | Y | N | Favorite Query lacks of necessary conditions, such as missing column names, requiring user intervention |
| fq\_blacklist\_num\_gauge | Favorite Query in blacklist | Y | N | Refer to the definition of "Blacklist" |

| Name | Meaning | Project related | Host related |
| --- | --- | --- | --- |
| num\_of\_jobs\_created | Jobs created total number | Y | Y(all, job) |
| num\_of\_jobs\_finished | Jobs finished total number | Y | Y(all, job) |
| num\_of\_running\_jobs | The num of running jobs currently | Y | N |
| num\_of\_pending\_jobs | The num of pending jobs currently | Y | N |
| num\_of\_error\_jobs | The num of error jobs currently | Y | N |
| count\_of\_error\_jobs | The total count of error | Y | Y(all, job) |
| finished\_jobs\_total\_duration | Jobs finished total duration | Y | Y(all, job) |
| job\_duration\_99p | Jobs duration 99-percentile | Y | Y(all, job) |
| job\_step\_attempted\_total\_times | Jobs step attempted total times | Y | Y(all, job) |
| failed\_job\_step\_attempted\_total\_times | Jobs step attempted failed total times | Y | Y(all, job) |
| job\_resumed\_total\_times | Jobs resumed total times | Y | Y(all, job) |
| job\_discarded\_total\_times | Jobs discarded total times | Y | Y(all, job) |
| job\_duration | The build duration of job | Y | Y(all, job) |
| job\_wait\_duration | The wait duration of job | Y | Y(all, job) |

| Name | Meaning | Project related | Host related |
| --- | --- | --- | --- |
| storage\_clean\_total\_times | Storage cleanup total times | N | Y(all, job, query) |
| storage\_clean\_total\_duration | Storage cleanup total duration | N | Y(all, job, query) |
| failed\_storage\_clean\_total\_times | Storage cleanup failed total times | N | Y(all, job, query) |

| Name | Meaning | Project related | Host related | Remark |
| --- | --- | --- | --- | --- |
| metadata\_clean\_total\_times | Metadata cleanup total times | Y | Y(all, job, query) | - |
| metadata\_backup\_total\_times | Metadata backup total times | Y | Y(all, job, query) | Differentiate projects and global |
| metadata\_backup\_total\_duration | Metadata backup total duration | Y | Y(all, job, query) | Differentiate projects and global |
| failed\_metadata\_backup\_total\_times | Metadata backup failed total times | Y | Y(all, job, query) | Differentiate projects and global |
| metadata\_ops\_total\_times | Metadata daily operations total times | N | Y(all, job, query) | Fixed time per day (configurable): automatically backup metadata; rotate audit\_log; cleanup metadata and storage space; adjust FQ; cleanup query histories. |
| metadata\_success\_ops\_total\_times | Metadata daily operations failed total times | N | Y(all, job, query) | - |

| Name | Meaning | Project related | Host related | Remark |
| --- | --- | --- | --- | --- |
| transaction\_retry\_total\_times | Transactions retried total times | Y | Y(all, job, query) | Differentiate projects, and, global |
| transaction\_latency\_99p | Transactions duration 99-percentile | Y | Y(all, job, query) | Differentiate projects, and, global |

---

<a id="operations-system-monitoring-service"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/system-monitoring/service/ -->

<!-- page_index: 114 -->

# Service Monitoring

Version: 5.0.2

Kylin provides the service monitoring for main components to help administrators obtain the service status and maintain instances.

Currently, we provide the following methods to monitor the core components in Kylin:

1. Query: each Query node will records its service status in InfluxDB
2. Build: each All node will records the service status and job status in InfluxDB

Two Rest APIs are provided to monitor and obtain the service status so that customers can integrate it with their own monitor platform.

- Get the Kylin cluster status by monitor query and building services. If the status is `WARNING` or `CRASH`, it means the cluster is unstable.
- Get the service unavailable time with the specified time range and some detailed monitor data to help admins to track and retrospect.

**Get Cluster Status**

`GET http://host:port/kylin/api/monitor/status`

- HTTP Header

  - Accept: application/vnd.apache.kylin-v4-public+json
  - Accept-Language: en
  - Content-Type: application/json;charset=utf-8
- Curl Request Example


```text
curl -X GET \ 
'http://host:port/kylin/api/monitor/status' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8'  
```

- Response Details

  - `active_instances` number of active instances in current cluster.
  - `query_status` query service status. It could be GOOD / WARNING / CRASH
  - `job_status` building service status. It could be GOOD / WARNING / CRASH.
  - `Job` job instance status. It will show the instance details and status.
  - `query` query instance status. It will show the instance details and status.
- Response Example


```json
{"code": "000","data": {"active_instances": 1,"query_status": "GOOD","job_status": "GOOD","job": [{"instance": "sandbox.hortonworks.com:7070","status": "GOOD"} ],"query": [{"instance": "sandbox.hortonworks.com:7070","status": "GOOD"}] },"msg": ""}
```

**Get Cluster Status with Specific Time Range**

`GET http://host:port/kylin/api/monitor/status/statistics`

- HTTP Header

  - Accept: application/vnd.apache.kylin-v4-public+json
  - Accept-Language: en
  - Content-Type: application/json;charset=utf-8
- URL Parameters

  - `start` - `required` `Long` timestamp. Get the monitor data greater than or equal to the timestamp.
  - `end` - `reuquired` `Long` timestamp. Get the monitor data smaller than the timestamp.
- Curl Example


```text
curl -X GET \ 
  'http://host:port/kylin/api/monitor/status/statistics?start=1583562358466&end=1583562358466' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Details

  - `Start` start time of monitoring. It will be rounded down based on the interval of monitoring data. If the interval is 1 minute, it will only record data in minute level. For example, if the argument is `1587353550000`, it will be recognized as `1587353520000`. Therefore, the data might be inaccurate.
  - `end` end time of monitoring. It will be rounded down based on the interval of monitoring data. If the interval is 1 minute, it will only record data in minute level. For example, if the argument is `1587353550000`, it will be recognized as `1587353520000`. Therefore, the data might be inaccurate.
  - `interval` interval of monitor data, default value is 60000 ms (1 min)
  - `job` job instance status. It will show the instance details and status, which includes unavailable time and counts. The time unit of unavailable time is ms.
  - `query` query instance status. It will show the instance details and status, which includes unavailable time and counts. The time unit of unavailable time is ms.
- Response Example


```text
{ 
    "code":"000", 
    "data":{ 
        "start":1584151560000, 
        "end":1584151680000, 
        "interval":60000, 
        "job":[ 
            { 
                "instance":"sandbox.hortonworks.com:7070", 
                "details":[ 
                    { 
                        "time":1584151572650, 
                        "status":"GOOD" 
                    }, 
                    { 
                        "time":1584151632770, 
                        "status":"GOOD" 
                    } 
                ], 
                "unavailable_time":0, 
                "unavailable_count":0 
            } 
        ], 
        "query":[ 
            { 
                "instance":"sandbox.hortonworks.com:7070", 
                "details":[ 
                    { 
                        "time":1584151609142, 
                        "status":"GOOD" 
                    }, 
                    { 
                        "time":1584151669142, 
                        "status":"GOOD" 
                    } 
                ], 
                "unavailable_time":0, 
                "unavailable_count":0 
            } 
        ] 
    }, 
    "msg":"" 
} 
```

1. The detected query is constant query which will not scan HDFS files.
2. InfluxDB is not high available now. Hence, some monitor data will be lost if the InfluxDB service is down.
3. The job status will be inaccurate if deleting or discarding plenty of jobs.
4. Since system monitoring depends on InfluxDB, if the system monitoring is still enabled (enabled by default) when InfluxDB is not configured, some useless errors may appear in the log. So when InfluxDB is not configured, it is recommended to configure `kylin.monitor.enabled = false` in `kylin.properties` to turn off the system monitoring function.

---

<a id="operations-logs-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/logs/intro/ -->

<!-- page_index: 115 -->

# Logs

Version: 5.0.2

This chapter mainly introduces different log types:

- [System Log](#operations-logs-system_log)
- [Audit Log](#operations-logs-audit_log)

---

<a id="operations-logs-system_log"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/logs/system_log/ -->

<!-- page_index: 116 -->

# System Log

Version: 5.0.2

After being successfully started, Kylin will create a directory named `logs/` by default, all logs generated during Kylin runtime will be stored in this directory.

Log files generated by Kylin is as followings.

This file is Kylin's main log file, whose default logging level is DEBUG.

The standard output of Kylin process will be redirected to this file, including the output of Tomcat and Hive.

This file is the GC(Garbage Collection) log of Kylin Java process. And it appends pid as filename suffix to avoid being overwritten.

This file stores the Tomcat access log. It records all HTTP request response information.For example, User-Agent, access URL, etc.

This file records Java stack traces of Java threads of Kylin, which is used to record some threads running status. To avoid the storage overused, only 20 log files can be kept. The new file will replace the oldest one, when exceeding the maximum number.

> Note:Because the execution of jstack depends on the .java\_pid file written by jvm in the /tmp directory, if the file is deleted (for example, a scheduled clean up script), it will cause the jstack to not run properly, so that the jstack.timed .log will not be generated

The standard output of executing `check-env.sh` script will be redirected to this file.

The error message of executing `check-env.sh` script will be redirected to this file.

The result of running command lines will be stored in this file.

The standard output of running command lines will be redirected to this file.

The log of system start, stop, upgrade, login and logout will be redirected to this file.

> Notes: When using LDAP service to implement user authentication, two logs will be recorded for each login failure. Because when using the LDAP service, if the login fails, another method will be used for authentication.

This file records logs related to task scheduling, whose default logging level is DEBUG.

This file records query related logs, whose default logging level is DEBUG.

This file records build-related logs, whose default logging level is DEBUG.

This file records metadata and transaction operations related logs, whose default logging level is DEBUG.

When Out of Memory (OOM) occurs in Kylin, it will dump the entire heap, which is convenient for checking the cause.

> Note: When you have a large memory setting and Out of Memory OOM occurs, the file dump.hprof will occupy a large storage space, which may cause your disk space to be insufficient and the node to be abnormal. You can manually clean up the historical file.

Take query as an example, submitting a query on Web UI, and we'll see the following information in `kylin.query.log`

```text
==========================[QUERY]=============================== 
Query Id: 8586e718-67b4-c840-61b4-a8898415a154 
SQL: select lo_revenue as from p_lineorder; 
User: ADMIN 
Success: true 
Duration: 1.243 
Project: ssb100_10 
Realization Names: [P_LINEORDER_1] 
Index Layout Ids: [30001] 
Snapshot Names: [] 
Is Partial Match Model: [false] 
Scan rows: [35000] 
Total Scan rows: 35000 
Scan bytes: [246530] 
Total Scan Bytes: 246530 
Result Row Count: 280 
Shuffle partitions: 1 
Hit Exception Cache: false 
Storage Cache Used: false 
Storage Cache Type: null 
Is Query Push-Down: false 
Is Prepare: false 
Is Timeout: false 
Time Line Schema: massage,end calcite parse sql,end_convert_to_relnode,end_calcite_optimize,end_plan,collect_olap_context_info,end select realization,end_rewrite,to_spark_plan,seg_pruning,fetch_file_status,shard_pruning,executed_plan,collect_result 
Time Line: 6,1,4,11,0,0,1,1,14,6,0,0,1,1198 
Message: null 
Is forced to Push-Down: false 
User Agent: null 
Scan Segment Count: 1 
Scan File Count: 1 
Is Refused: false 
==========================[QUERY]=============================== 
```

The main fields in the above clip are described as follows:

- `Query Id`： Query id
- `SQL`： Query statement
- `User`： The user name to execute the query
- `Success`： Status flag of query result, true execution succeeded, false execution failed
- `Duration`： Query time (unit: seconds)
- `Project`： The name of the project used in the query
- `Realization Names`： The name of the model hit by the query
- `Index Layout Ids`： ID of the layout hit by the query
- `Snapshot Names`： Query the hit snapshot
- `Is Partial Match Model`： Partial match model, such as a left B, you can check table a alone
- `Scan rows`： Query the number of data rows scanned
- `Total Scan rows`： Total rows of data scanned by query
- `Scan bytes`： Query the number of data bytes scanned
- `Total Scan Bytes` ： Query the total number of bytes of scanned data
- `Result Row Count`： The number of data rows returned by the query
- `Shuffle partitions`： A spark query parameter that affects how many partitions / tasks are generated after a shuffle. It is calculated by kylin.query.engine.sparkl-sql-shuffle-parittions or dynamic calculation. The calculation formula is min (the estimated value of data size and the total number of cores of spark cluster)
- `Hit Exception Cache`： Whether to hit the cache of failed queries
- `Storage Cache Used`： Whether to hit the cache successfully queried
- `Storage Cache Type`： The cache type of the hit query
- `Is Query Push-Down`： Is it a push down query
- `Is Prepare`： Whether it is a probe query (this item will be true for the query sent by BI)
- `Is Timeout`： Whether to timeout
- `Time Line Schema`： Steps in query module
- `Time Line`： Time spent in each step of the query module (MS)
- `Message`：Query the prompt information on the page. The query is successful. This item is null
- `Is forced to Push-Down`： Whether to force down
- `User Agent`： The environment information used to submit the query
- `Scan Segment Count`： Number of scanned segments
- `Scan File Count`： Number of scanned files
- `Is Refused`: Whether to refuse to query

Kylin uses log4j2 to configure logs. Users can edit the `kylin-server-log4j.xml` file in the `$KYLIN_HOME/server/conf/` directory to modify the log level, path, etc.
After modification, you need to restart Kylin for the configuration to take effect.

The configuration of all logs starting with kylin and ending with log is in `kylin-server-log4j.xml`, the configuration code is as follows.

```xml
        <Routing name="routing"> 
            <Routes pattern="$${ctx:logCategory}"> 
                <Route> 
                    <RollingFile name="rolling-${ctx:logCategory}" 
                                 fileName="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.log" 
                                 filePattern="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.log.%i"> 
                        <Policies> 
                            <SizeBasedTriggeringPolicy size="268435456"/> 
                        </Policies> 
                        <DefaultRolloverStrategy max="10"/> 
                        <PatternLayout pattern="%d{ISO8601} %-5p %X{request.project}[%t] %c{2} : %mask{%m}%n"/> 
                    </RollingFile> 
                </Route> 
 
                <Route ref="server" key="$${ctx:logCategory}"/> 
            </Routes> 
        </Routing> 
 
```

In the default configuration, log rolling is triggered when the log file reaches 256MB, keeping the last 10 log files.

If you need to configure one of the log files (such as kylin.query.log) separately, you need to add a new Route under the Routes configuration in the above configuration code, and configure the key as the corresponding log file name (query, schedule).
It should be noted that the new route needs to be configured before the existing route, otherwise it will not take effect.

The following is an example, modify the rolling strategy of kylin.query.log to trigger at 0:00 every day, back up the last 5 logs.

```xml
<Route key="query"> 
    <RollingFile name="rolling-${ctx:logCategory}" fileName="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.log" filePattern="${env:KYLIN_HOME}/logs/kylin.${ctx:logCategory}.log.%i"> 
        <Policies> 
            <CronTriggeringPolicy schedule="0 0 0 * * ?"/> 
        </Policies> 
        <DefaultRolloverStrategy max="5" /> 
        <PatternLayout pattern="%d{ISO8601} %-5p %X{request.project}[%t] %c{2} : %mask{%m}%n" /> 
    </RollingFile> 
</Route> 
```

If you need to configure kylin.log, you can modify the RollingRandomAccessFile configuration, for example, change the number of reserved files to 5

```xml
<RollingRandomAccessFile name="server" fileName="${env:KYLIN_HOME}/logs/kylin.log" append="true" 
                         filePattern="${env:KYLIN_HOME}/logs/kylin.log.%i" immediateFlush="false" > 
    <Policies> 
        <SizeBasedTriggeringPolicy size="268435456"/> 
    </Policies> 
    <DefaultRolloverStrategy max="5"/> 
    <PatternLayout pattern="%d{ISO8601} %-5p %X{request.project}[%t] %c{2} : %mask{%m}%n"/> 
</RollingRandomAccessFile> 
```

The format of log error code is KE-AABBBCCC, AA refers to the error reporting module, BBB refers to the more detailed business error reporting and CCC refers to the error number.

| AA | Description |
| --- | --- |
| 00 | common |
| 10 | server |
| 20 | query |
| 30 | build |
| 40 | system |
| 50 | tool |

| BBB | Description |
| --- | --- |
| 000 | general |
| 001 | project |
| 002 | model |
| 003 | user |
| 004 | user group |
| 005 | password |
| 006 | column |
| 007 | table |
| 008 | database |
| 009 | measure |
| 010 | dimension |
| 011 | cc |
| 012 | index |
| 013 | job |
| 014 | sql expression |
| 015 | license |
| 016 | email |
| 017 | file |
| 018 | kerberos |
| 019 | catalog |
| 020 | recommendation |
| 021 | server |
| 022 | segment |
| 023 | diag |
| 024 | auth |
| 025 | shell |
| 026 | metadata |
| 027 | frequency query |
| 028 | json |

---

<a id="operations-logs-audit_log"></a>

<!-- source_url: https://kylin.apache.org/docs/operations/logs/audit_log/ -->

<!-- page_index: 117 -->

# Audit Log

Version: 5.0.2

In the database, Audit Log is mainly used to monitor and record the operating behavior of data, which is simply understood as a log.

Kylin instances are stateless services. All state information is stored in metadata. All operations that change data will create or modify metadata. Changes to metadata are included in a database transaction. At the same time, every time Modifications to metadata are recorded in the audit log, which is equivalent to a snapshot of each version of the metadata. Audit Log mechanism can not only monitor metadata through the Audit Log, but also help disaster recovery.

> Caution：The Audit Log can only be considered as a log of metadata, used to monitor and troubleshoot problems, and can be used to repair some metadata. If you want to ensure the stability of the system, you need to ensure that the metadata is correct and back up the metadata in a timely manner.

When Kylin is started for the first time, according to the metadata table name you filled in for the configuration item `kylin.metadata.url` in the configuration file `kylin.properties`, create a file named `{identifier} _audit_log` in the metadata database. The audit table has a suffix `_audit_log` compared to the metadata table.

e.g：

`kylin.metadata.url=kylin_metadata@jdbc,driverClassName=org.postgresql.Driver,url=jdbc:postgresql://sandbox:5432/kylin,username=postgres,password=`

The metadata is named `kylin`, the metadata table is named `kylin_metadata`, and the Audit Log table is named `kylin_metadata_audit_log`.

In Kylin, PostgreSQL is used as the metastore by default, and PostgreSQL is used as an example later.

**Audit Log table field descriptions**

| name | type（postgresql） | type(mysql) | description |
| --- | --- | --- | --- |
| id | bigserial | bigint | Auto incremental id |
| meta\_key | varchar(255) | varchar(255) | The key of metadata, corresponding to the META\_TABLE\_KEY field in the metadata table |
| meta\_content | bytea | longblob | The content of the current metadata, when the operation is deletion, the value is NULL |
| meta\_ts | bigint | bigint | Update timestamp, when the operation is deletion, the value is NULL |
| meta\_mvcc | bigint | bigint | The version of the current metadata, when the operation is deletion, the value is NULL |
| unit\_id | varchar(255) | varchar(255) | Transaction id |
| operator | varchar(255) | varchar(255) | The username of operator |
| instance | varchar | varchar | The instance of operator |

The `meta_table_key` field in the metadata table is associated with the `meta_key` in the audit log table.

- Metadata version: In the metadata table, the `meta_table_mvcc` field records the latest version number of each item of metadata;
- Audit log version: In the audit log table, the `meta_mvcc` field records the version number. You can filter and view all historical versions of a certain metadata according to the `meta_key` field;

The following functions can be implemented through audit logs:

- View the change history of all / a certain metadata and the corresponding operation user
- View the change of metadata in a transaction
- View the audit log over a period of time
- Facilitates metadata disaster recovery

**Tool**

PostgreSQL client tool：DBeaver

**Table description**

![metadata table](assets/images/metadata-table-f55118883aeada64d52346a23a7c4c02_7e9121e5fc7e2d63.png)

As shown in the table, the meta\_key field is a metadata item and meta\_content is a metadata value. The meta\_key value starts with `/ _global` to indicate global metadata, `/ project_name` starts to indicate metadata for a project, and `/ UUID` is a globally unique identifier, which serves as an identifier for a piece of metadata.

e.g：

- `_global/user/ADMIN` Represents metadata information of ADMIN users, the specific information is in the meta\_content field;
- `_global/project/kylin.json` Represents metadata information for a project named kylin;
- `/${project_name}/model_desc/${model_id}` Model description information representing a project;

**Basic Operations**

1. View the history of an item of metadata


```text
select * from kylin_metadata_audit_log where meta_key = '/_global/project/default.json'; 
```

2. View the history of a model


```text
select * from kylin_metadata_audit_log where meta_key = '/project/model_desc/49529000-c161-4013-bb80-9a78f4f0248d.json'  
```

3. View the change of metadata in a transaction


```text
select * from kylin_metadata_audit_log where unit_id = '6090bfb5-2401-4176-8475-fe6fd82bc439'; 
```

4. View audit logs for metadata over a period of time


```text
select * from kylin_metadata_audit_log where meta_ts > 1325376000000 and meta_ts < 1328054400000 ; 
```

5. Associate the metadata table to view the history changes of a user


```text
select a.meta_mvcc, a.meta_content, b.meta_table_mvcc, b.meta_table_content from kylin_metadata_audit_log a left join kylin_metadata b on a.meta_key = b.meta_table_key where a.meta_key = '/_global/user/ADMIN' 
```

**Examples of actual scenarios**

- Monitor if user password is changed

  The ADMIN user is very important. It is not allowed to modify the password by anyone other than the system administrator. You can monitor the content of meta\_content whose meta\_key is `/_global/user/ADMIN`. One of the fields is password. If this value changes, explained the password modified.

  The meta\_mvcc field version number increases before and after the password is changed, the password value in the meta\_content field changes, and the value of default\_password also changes from true to false:

  ![metadata](assets/images/before-update-pwd-a0f9cea1736202db276298527b8171c8_d983a1696a35a366.png)

  ![metadata](assets/images/after-update-pwd-063dc661aacd434720d5e8a83c2e63af_eeb248c1341b158e.png)
- Monitor if the model has been modified

  Assume that the project name is kylin, and the table connection relationship of model name test\_model is not allowed to be modified. You can view the JSON format of a model on the Kylin model page, where uuid represents the model id, then the corresponding meta\_key is `/kylin/model_desc/${model_id}` , monitor whether the corresponding meta\_mvcc field value increases, if there is a change, the model is modified.

  The second record is to change the format of the time partition column of the model, and the unit\_id field value of the two records is different, indicating that the two changes were made in different transactions, and the user who checked the operator field was ADMIN:

  ![metadata](assets/images/before-update-model-9712b446ce68ea2571a9d539985ee173_45a1e5ba4f120ff1.png)

  ![metadata](assets/images/after-update-model-722571e5924fbb4244521c81f335c618_c0bfb4fb69b5975b.png)

In the Kylin configuration file `kylin.properties`, there are the following configuration items about the audit log, which can be modified as needed. **Please make sure the disk space of the audit log node is always sufficient.**

- `kylin.metadata.audit-log.max-size=500000` The audit log stores the latest 500,000 rows by default. By default, the redundant operation log is cleared every morning. You can modify this configuration item to adjust it.

The Audit Log is stored in the database. You can use the tools provided by Kylin to export the data within the specified time range to the local for backup, or export it as an attachment to the Kylin ticket when encountering problems, which is convenient for technology support personnel to locate the problem.

There are two ways to execute commands on the Kylin node:

1. Use the diagnostic package command: `$ {KYLIN_HOME}/bin/diag.sh`

   - -The Audit Log of the last 3 days will be obtained by default and stored in the `audit_log/${starttime}_${endtime}.jsonl` file in the diagnostic package directory;
2. Using the AuditLogTool tool: `${KYLIN_HOME}/bin/kylin.sh org.apache.kylin.tool.AuditLogTool -startTime ${starttime} -endTime ${endtime} -dir ${target_dir}`

   - `${starttime}` and `${endtime}` Retrieves the specified range of Audit Log. The format is timestamp in milliseconds: e.g `1579868382749`;
   - `${target_dir}` specifies the directory where your Audit Log files are stored. The generated Audit Log is stored in the `${target_dir}/${starttime}_${endtime}` file;

If you have the Audit Log file exported locally and want to view and analyze it through the database, you can use the following methods to import.

On a machine that already has a Kylin environment, use the AuditLogTool tool: `${KYLIN_HOME}/kylin.sh org.apache.kylin.tool.AuditLogTool -restore -table ${target_table_name} -dir ${auditlog_dir}`

- The `$ {target_table_name}` parameter specifies the name of the Audit Log table to be generated. Be careful not to duplicate the name of the Audit Log table already in the Kylin environment.
- The `$ {auditlog_dir}` parameter specifies the directory where the Audit Log file is located;

After the execution of the command is completed, the Audit Log table is generated under the metastore specified by the configuration item `kylin.metadata.url` in the `$ {KYLIN_HOME}/conf/kylin.properties` file.

---

<a id="integration-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/integration/intro/ -->

<!-- page_index: 118 -->

# Integrate with BI Tools

Version: 5.0.2

This chapter introduces how Kylin can be integrated with BI tools.

---

<a id="integration-jdbc"></a>

<!-- source_url: https://kylin.apache.org/docs/integration/jdbc/ -->

<!-- page_index: 119 -->

# Kylin JDBC Driver

Version: 5.0.2

Kylin provides JDBC driver, which enables BI or other applications with JDBC interface to access Kylin instance.

There are two methods to get JDBC Driver:

1. **(Recommended)** You can get Kylin JDBC driver from Kylin's installation directory's subdirectory `./lib` , and placed in the BI or other third party applications specified path.
2. You can get Kylin JDBC driver by executing the scripts from `${KYLIN CODES HOME}/build/release/jdbc_package.sh` to generate a full JDBC driver tar package and unzip it to get driver.

> **Note：**
>
> Support connecting to Kylin 5.0 and higher versions

Kylin JDBC driver follows the JDBC standard interface, users can specify the Kylin service to which the JDBC connection is made via the URL and the URL form is:

```text
jdbc:kylin://<hostname>:<port>/<project_name> 
```

URL parameter description is as follows:

- `<hostname>`: If Kylin service start SSL, then JDBC should use the HTTPS port of the Kylin service
- `<port>`：If port has not been specified, then JDBC driver would use default port of HTTP and HTTPS
- `<project_name>`: Required. users have to ensure the project exist in Kylin service

Besides, users need to specify username, password and whether SSL would be true for connection, these properties are as follow:

- `<user>`: username to login Kylin service
- `<password>`: password to login Kylin service
- `<ssl>`: enable ssl parameter. Set up string type "true" / "false", the default setting for this parameter is "false". If the value is "true", all accesses to Kylin are based on HTTPS
- `<timeout>`: timeout in milliseconds for requests for Kylin. Default to 0 (no timeout)

Here lists an example of Connection:

```java
Driver driver = (Driver) Class.forName("org.apache.kylin.jdbc.Driver").newInstance(); 
Properties info = new Properties(); 
info.put("user", "ADMIN"); 
info.put("password", "KYLIN"); 
//info.put("ssl","true"); 
Connection conn = driver.connect("jdbc:kylin://localhost:7070/kylin_project_name", info); 
```

The following sections describe how two JAVA programs can connect to JDBC

Here lists an example of Query based on Statement：

```java
Driver driver = (Driver) Class.forName("org.apache.kylin.jdbc.Driver").newInstance(); 
Properties info = new Properties(); 
info.put("user", "ADMIN"); 
info.put("password", "KYLIN"); 
//info.put("ssl","true"); 
Connection conn = driver.connect("jdbc:kylin://localhost:7070/kylin_project_name", info); 
Statement state = conn.createStatement(); 
ResultSet resultSet = state.executeQuery("select * from test_table"); 
while (resultSet.next()) { 
    System.out.println(resultSet.getString(1)); 
    System.out.println(resultSet.getString(2)); 
    System.out.println(resultSet.getString(3)); 
} 
```

Here lists an example of Query based on Prepared Statement：

```java
Driver driver = (Driver) Class.forName("org.apache.kylin.jdbc.Driver").newInstance(); 
Properties info = new Properties(); 
info.put("user", "ADMIN"); 
info.put("password", "KYLIN"); 
//info.put("ssl","true"); 
Connection conn = driver.connect("jdbc:kylin://localhost:7070/kylin_project_name", info); 
PreparedStatement state = conn.prepareStatement("select * from test_table where id=?"); 
state.setInt(1, 10); 
ResultSet resultSet = state.executeQuery(); 
while (resultSet.next()) { 
    System.out.println(resultSet.getString(1)); 
    System.out.println(resultSet.getString(2)); 
    System.out.println(resultSet.getString(3)); 
} 
```

Among them, Prepared Statement supports assignment for the following types:

- setString
- setInt
- setShort
- setLong
- setDouble
- setBoolean
- setByte
- setDate
- setTimestamp

**Prepared Statement Known Limitation**

- Query pushdown is not supported when using Prepared Statement.
- Dynamic param cannot follow with **'-'**, e.g. `SUM(price - ?)`
- Dynamic param cannot use in **case when**, e.g. `case when xxx then ? else ? end`

It's recommended to use dynamic param in filters only, e.g. `where id = ?`.

We also provide a way to bind dynamic parameter values. To enable this functionality, you need to add `kylin.query.replace-dynamic-params-enabled=true` in your kylin property file.

Then the dynamic parameter limitations converges to:

- Column names and time units cannot be used as dynamic parameters.
- Type conversion functions `date` and `timestamp` are not supported, only `cast as` is supported.
- Some functions such as subtract\_count support array parameter. The parameters in array also support dynamic parameters, such as `array['FP-GTC|FP-non GTC ', ?]`, but dynamic parameters are not supported in single quotes, such as `array['?|?', ?]`.

In Kylin 5.0 and later version, you can use a authenticated user and delegate requests to another user by enabling Tableau Server to pass an Execute as user to the Kylin. As a result of this, the query will run on Kylin with the privileges of the Executed as user.

The following chapters introduce two ways of setting User Delegation,

```java
Driver driver = (Driver) Class.forName("org.apache.kylin.jdbc.Driver").newInstance(); 
Properties info = new Properties(); 
info.put("user", "ADMIN"); 
info.put("password", "KYLIN"); 
info.put("EXECUTE_AS_USER_ID","EXECUTE_AS_NON_ADMIN"); 
Connection conn = driver.connect("jdbc:kylin://localhost:7070/kylin_project_name", info); 
```

Bind the param in connect string:
`jdbc:kylin:EXECUTE_AS_USER_ID=EXECUTE_AS_NON_ADMIN;//localhost:7070/kylin_project_name`

To make sure User Delegation is set successfully, you can observe this INFO level log in the JDBC log file: "Found the parameter EXECUTE\_AS\_USER\_ID in the connection string. The query will be executed as the user defined in this connection string." And then the query user will be switched to EXECUTE\_AS\_NON\_ADMIN.

You can enable logging in the driver to track activity and troubleshoot issues.

**Important:** Only enable logging long enough to capture an issue. Logging decreases performance and can consume a large quantity of disk space.

1. Open the driver logging configuration file in a text editor.
   For example, you would open the `{JDBC installed path}/kylin-jdbc.properties`

   >
> [!NOTE]
> ：kylin-jdbc.properties is the default configuration file that needs to be placed in the same path as the JDBC jar package

2. Set log level. Information on all of the Log Levels is listed below.Trace is best in most cases.

   - **OFF** disables all logging.
   - **FATAL** logs very severe error events that might lead the driver to abort.

> [!CAUTION]
> **ERROR**
> - logs error events that might still allow the driver to continue running.
- **WARN** logs potentially harmful situations.

> [!NOTE]
> **INFO**
> - logs general information that describes the progress of the driver.
- **DEBUG** logs detailed information that is useful for debugging the driver.
   - **TRACE** logs more detailed information than log level DEBUG.

   For example: **LogLevel=TRACE**
3. Set the Log Path and file name.Set the **LogPath** attribute to the full path to the folder where you want to save log files. This directory must exist and be writable, including being writable by other users if the application using the driver runs as a specific user.
   For example: **LogPath=/usr/local/KylinJDBC.log**
4. Set the **MaxBackupIndex** attribute to the maximum number of log files to keep.
   For example: **MaxBackupIndex=10**

   >
> [!NOTE]
> : After the maximum number of log files is reached, each time an additional file is created, the driver deletes the oldest file.

5. Set the **MaxFileSize** attribute to the maximum size of each log file in bytes.
   For example: **MaxFileSize=268435456**

   > **Note:** After the maximum file size is reached, the driver creates a new file and continues logging.
6. Save the driver configuration file.


```text
# Set log level 
LogLevel=TRACE 
 
# Set log path and file name 
LogPath=/usr/local/KylinJDBC.log 
 
# Set maximum number of log files to keep 
MaxBackupIndex=10 
 
# Set maximum size of each log file in bytes 
MaxFileSize=268435456 
```

7. Restart the application you are using the driver with.Configuration changes will not be picked up by the application until it reloads the driver.

**Q: How to upgrade the JDBC Driver?**

Remove the Kylin JDBC Driver package for BI or other third-party applications，and replace it with a new JDBC driver package.

---

<a id="restapi-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/intro/ -->

<!-- page_index: 120 -->

# Rest API

Version: 5.0.2

Kylin provides various REST APIs, which can be used to execute queries, trigger a build job and so on. With those APIs, the third-party system could integrate with Kylin system seamlessly.

---

<a id="restapi-authentication"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/authentication/ -->

<!-- page_index: 121 -->

# Access and Authentication

Version: 5.0.2

The access prefix of all Kylin APIs is `/kylin/api`. This prefix is required regardless of which module API is accessed. For example, accessing model uses API of `/kylin/api/models`, and the correspondingly complete path is `http://host:port/kylin/api/models`.

All APIs in Kylin are based on [Basic Authentication](http://en.wikipedia.org/wiki/Basic_access_authentication) authentication mechanism. Basic Authentication is a simple access control mechanism, which encodes account and password information based on Base64. Adding these information as request headers to HTTP request commands, the back-end will decode the account and password information from the request header for authentication. Take the account and password `ADMIN:KYLIN` as an example, after encoding, the corresponding authentication information would be `Basic QURNSU46S1lMSU4=`, and the corresponding HTTP header information is `Authorization: Basic QURNSU46S1lMSU4=`.

- Add `Authorization` to HTTP header
  - Or users could get authorized through `POST http://host:port/kylin/api/user/authentication`. Once the authentication passes, the authentication information would be stored in cookie files for the following visit.

- HTTP Header

  - `Authorization:Basic QURNSU46S1lMSU4=`
  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/user/authentication' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
  { 
      "code":"000", 
      "data":{ 
          "username":"ADMIN", 
          "authorities":[{"authority": "ROLE_ADMIN"}, {"authority": "ALL_USERS"}], 
          "disabled":false, 
          "locked":false, 
          "uuid":"0205dac6-215a-4454-84ae-3dcc85b9675c", 
          "last_modified":1574756819619, 
          "create_time":1563346648008, 
          "version":"4.0.0.0", 
          "mvcc":24, 
          "locked_time":0, 
          "wrong_time":2, 
          "first_login_failed_time":1574756817981 
      }, 
      "msg":"" 
  } 
```

> Note: You can download "jquery.base64.js" at <https://github.com/yckart/jquery.base64.js>

```javascript
var authorizationCode = $.base64('encode', 'NT_USERNAME' + ":" + 'NT_PASSWORD');
$.ajaxSetup({headers: {'Authorization': "Basic " + authorizationCode,'Content-Type': 'application/json;charset=utf-8','Accept': 'application/vnd.apache.kylin-v4-public+json'} });
```

```javascript
$.ajaxSetup({headers: {'Authorization': "Basic eWFu**********X***ZA==",'Content-Type': 'application/json;charset=utf-8','Accept': 'application/vnd.apache.kylin-v4-public+json' } // use your own authorization code here }); var request = $.ajax({url: "http://host:port/kylin/api/query",type: "POST",data: '{"sql":"select count(*) from SUMMARY;","offset":0,"limit":50000,"acceptPartial":true,"project":"test"}',dataType: "json" }); request.done(function( msg ) {alert(msg); }); request.fail(function( jqXHR, textStatus ) {alert( "Request failed: " + textStatus ); });
```

---

<a id="restapi-project_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/project_api/ -->

<!-- page_index: 122 -->

# Project Management

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- `POST http://host:port/kylin/api/projects`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `name` - `required` `string`, project name.
  - `description` - `optional` `string`, project description.
  - `maintain_model_type` - `required` `string`, project type, `MANUAL_MAINTAIN` for default.
- Curl Request Example


```sh
curl -X POST \ 
'http://host:port/kylin/api/projects' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
  "name": "a", 
  "description": "", 
  "maintain_model_type": "MANUAL_MAINTAIN" 
}' 
```

- Response Example


```json
{"code":"000","data":{"uuid":"c7713bea-7df5-49d5-9713-f0094addbafe","last_modified":1574389912687,"create_time":1574389912687,"version":"4.0.0.0","mvcc":0,"name":"a","owner":"ADMIN","status":"ENABLED","create_time_utc":1574389912687,"default_database":"DEFAULT","description":"","ext_filters":[
],"maintain_model_type":"AUTO_MAINTAIN","override_kylin_properties":{
},"segment_config":{"auto_merge_enabled":true,"auto_merge_time_ranges":["WEEK","MONTH","QUARTER","YEAR" ],"volatile_range":{"volatile_range_number":0,"volatile_range_enabled":false,"volatile_range_type":"DAY" },"retention_range":{"retention_range_number":1,"retention_range_enabled":false,"retention_range_type":"MONTH"}} },"msg":""}
```

- `DELETE http://host:port/kylin/api/projects/{project}`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
'http://host:port/kylin/api/projects/b' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code":"000", 
    "data":null, 
    "msg":"" 
} 
```

- `PUT http://host:port/kylin/api/projects/{project}/push_down_config`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Header

  - `Content-Type: application/json;charset=utf-8`
  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
- HTTP Body: JSON Object

  - `push_down_enabled` - `required` `boolean`, whether to turn on query pushdown, `true` for turning on, `false` for turning off.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/projects/b/push_down_config' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
 "push_down_enabled":true 
}' 
```

- Response Example


```json
{ 
    "code":"000", 
    "data":"", 
    "msg":"" 
} 
```

- `PUT http://host:port/kylin/api/projects/{project}/push_down_project_config`
- URL Parameters

  - `project` - `required` `string`，project name。
- HTTP Header

  - `Content-Type: application/json;charset=utf-8`
  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
- HTTP Body: JSON Object
- `runner_class_name` - `required` `string`，project config property `kylin.query.pushdown.runner-class-name`. To specify the query engine when query pushdown. For default, when pushdown to the native Spark, the value is `org.apache.kylin.query.pushdown.PushDownRunnerSparkImpl`.
- `converter_class_names` - `required` `string`，project config SQL conversion property `kylin.query.pushdown.converter-class-names`.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/projects/b/push_down_project_config' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
 "project": "project_name", 
 "runner_class_name":"org.apache.kylin.query.pushdown.PushDownRunnerSparkImpl", 
 "converter_class_names":"org.apache.kylin.query.security.HackSelectStarWithColumnACL,org.apache.kylin.query.util.SparkSQLFunctionConverter" 
}'  
```

- Response Example


```json
{ 
    "code":"000", 
    "data":"", 
    "msg":"" 
} 
```

- `PUT http://host:port/kylin/api/projects/{project}/segment_config`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `auto_merge_enabled` - `required` `boolean`, whether to turn on segment auto-merge, `true` for turning on, `false` for turning off.
  - `auto_merge_time_ranges` - `required` `array`, the period of segment auto-merge and the unit of retentio threshold. Optional values: `DAY`, `WEEK`, `MONTH`, `QUARTER`, `YEAR`. For example, you can set auto-merge the segments in 1 week.
  - `volatile_range` - `optional` `json`, the volatile range of auto-merge, which means 'Auto-Merge' will not merge latest [Volatile Range] days segment. For example, If you set 10 days, it means that segments within 10 days will not be merged automatically.
    - `volatile_range_number` - `optional` `int`，The time of volatile range. The default value is `0`. Optional values: positive integer and `0`.
    - `volatile_range_type` - `optional` `string`，The time unit of the volatile range. The default value is `Day`. Optional values: `DAY`, `WEEK`, `MONTH`.
  - `retention_range` - `optional` `json`, retention threshold, which means to retain the segments in the retention threshold. If you set 1 year, that means the segments exceed the 1 year will be removed by the system automatically.
    - `retention_range_enabled` - `optional` `boolean`, whether to turn on the retention threshold, `true` for turning on, `false` for turning off, and the default value is `false`.
    - `retention_range_number` - `optional` `int`，The time to retention threshold. The default value is `1`. Optional values: positive integer and `0`.
    - `create_empty_segment_enabled` - `optional` `boolean`, whether to allow add new segment. `true` for turning on, `false` for turning off, and the default value is `false`.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/projects/b/segment_config' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
        "auto_merge_time_ranges":[ 
            "WEEK", 
            "MONTH", 
            "QUARTER", 
            "DAY", 
            "YEAR" 
        ], 
        "auto_merge_enabled":true, 
        "volatile_range":{ 
            "volatile_range_number":0, 
            "volatile_range_type":"DAY" 
        }, 
        "retention_range":{ 
            "retention_range_number":2, 
            "retention_range_enabled":false 
        } 
    }' 
```

> **Notes：**
>
> - `auto_merge_time_ranges` : array contains at least one value.
> - The time unit of `retention_range` is equal to the maximum time unit in the `auto_merge_time_ranges` array. If `"auto_merge_time_ranges":["DAY",MONTH"]`, then the time unit of `retention_range` is `MONTH`. If `"auto_merge_time_ranges":["YEAR",WEEK"]`, then the time unit of `retention_range` is `YEAR`.

- Response Example


```json
  { 
      "code":"000", 
      "data":"", 
      "msg":"" 
  } 
```

- `PUT http://host:port/kylin/api/projects/{project}/default_database`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object
- `default_database` - `required` `string`, default database name.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/projects/b/default_database' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
        "default_database":"EDW" 
    }' 
```

- Response Example


```json
  { 
      "code":"000", 
      "data":"", 
      "msg":"" 
  } 
```

- `PUT http://host:port/kylin/api/projects/{project}/job_notification_config`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `data_load_empty_notification_enabled` - `required` `boolean`, whether to turn on empty data load notification. `True` means to notify user if there is an empty data load job.
  - `job_error_notification_enabled` - `required` `boolean`, whether to turn on error job notification. `True` means to notify user if there is an error job.
  - `job_notification_emails` - `required` `array`，email address for the job notification. Email format: `xx@xx.xx`.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/projects/b/job_notification_config' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
        "data_load_empty_notification_enabled":true, 
        "job_error_notification_enabled":false, 
        "job_notification_emails":[ 
            "nnnn@yourmail.io","tttt@yourmail.io" 
        ] 
    }' 
```

- Response Example


```json
  { 
      "code":"000", 
      "data":"", 
      "msg":"" 
  } 
```

- `PUT http://host:port/kylin/api/projects/{project}/yarn_queue`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `queue_name` - `required` `string`, the name of YARN application queue.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/projects/b/yarn_queue' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
        "queue_name":"yarnqueue" 
    }' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

The Low Usage Storage, Segment Settings, Storage Quota and Job Notification can be reset to the default values. Only one of the settings can be reset each time.

- `PUT http://host:port/kylin/api/projects/{project}/project_config`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `reset_item` - `required` `string`, reset project settings item. Optional values: `job_notification_config`, `query_accelerate_threshold`, `garbage_cleanup_config`, `segment_config`, `storage_quota_config`.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/projects/a/project_config' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{ 
        "reset_item":"job_notification_config" 
    }' 
```

- Response Example


```json
 { 
     "code":"000", 
     "data":{ 
         "project":"a", 
         "description":"", 
         "maintain_model_type":"MANUAL_MAINTAIN", 
         "default_database":"EDW", 
         "semi_automatic_mode":false, 
         "storage_quota_size":10995116277760, 
         "push_down_enabled":true, 
         "auto_merge_enabled":true, 
         "auto_merge_time_ranges":[ 
             "WEEK", 
             "MONTH", 
             "QUARTER", 
             "YEAR" 
         ], 
         "volatile_range":{ 
             "volatile_range_number":0, 
             "volatile_range_enabled":true, 
             "volatile_range_type":"DAY" 
         }, 
         "retention_range":{ 
             "retention_range_number":1, 
             "retention_range_enabled":false, 
             "retention_range_type":"YEAR" 
         }, 
         "job_error_notification_enabled":false, 
         "data_load_empty_notification_enabled":false, 
         "job_notification_emails":[ 
  
         ], 
         "threshold":20, 
         "tips_enabled":true, 
         "frequency_time_window":"MONTH", 
         "low_frequency_threshold":5 
     }, 
     "msg":"" 
 } 
```

- The default values for Low Usage Strage:

  - `"frequency_time_window":"MONTH"`
  - `"low_frequency_threshold":0`
- The default values for Segment Settings:

  - `"auto_merge_enabled":true`
    - `"auto_merge_time_ranges":["DAY", "MONTH", "QUARTER", "YEAR"]`
  - `"volatile_range"`
    - `"volatile_range_number":0`
    - `"volatile_range_type":"DAY"`
  - `retention_range`
    - `"retention_range_enabled":false`
    - `"retention_range_number":1`
- `"create_empty_segment_enabled":false`
- The default values for Job Notification:

  - `"data_load_empty_notification_enabled":false`
  - `"job_error_notification_enabled":false`
  - `"job_notification_emails"` is null

---

<a id="restapi-model_api-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/model_api/intro/ -->

<!-- page_index: 123 -->

# Model Management

Version: 5.0.2

Kylin provides REST APIs on checking model information, index build and model management.

> - On how authentication works, see [Access and Authentication REST API](#restapi-authentication).
> - On Curl command line, don't forget to quote the URL if it contains the special char `&`.
> - On Curl command line, escape `%25` if it contains the special char `%`.

- `POST http://host:port/kylin/api/models`
- Request Permission: MANAGEMENT permission and above
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name
  - `fact_table` - `required` `string`, fact table name
  - `uuid` - `optional` `string`, model ID, default auto generated
  - `alias` - `required` `string`, model alias name
  - `management_type` - `required` `string`, for model creation please use: MODEL\_BASED
  - `simplified_measures` - `required` `JSON Object[]`, measures
    - `name` - `required` `string`, measure name
    - `expression` - `required` `string`, function, including: SUM,MIN,MAX,TOP\_N,COUNT,COUNT\_DISTINCT,CORR,PERCENTILE\_APPROX,COLLECT\_SET
    - `parameter_value` - `required` `JSON Object[]`, measure parameters

      - `type` - `required` `string`, parameter type: constant,column
      - `value` - `required` `int|string`, parameter value (Set value 1 when 'expression' is 'COUNT' and 'type' is 'constant', while others should be: TABLE.COLUMN)
    - `return_type` - `required` `string`, function return type with arguments including: topn(10)、topn(100)、percentile(100) etc., using empty string("") when no return type needed


```text
Supported return_type values: 
 
TOP_N: 
  * Top 10: topn(10) 
  * Top 100: topn(100) 
  * Top 1000: topn(1000) 
 
COUNT_DISTINCT: 
  * Error Rate < 9.75%: hllc(10) 
  * Error Rate < 4.88%: hllc(12) 
  * Error Rate < 2.44%: hllc(14) 
  * Error Rate < 1.72%: hllc(15) 
  * Error Rate < 1.22%: hllc(16) 
  * Precisely: bitmap 
 
PERCENTILE_APPROX: 
  * percentile(100) 
  * percentile(1000) 
  * percentile(10000) 
```

    - `comment` - `optional` `string`, comments
  - `simplified_dimensions` - `required` `JSON Object[]`, dimensions info
    - `column` - `required` `string`, format: TABLE.COLUMN
    - `name` - `required` `string`, column alias, may set the same as column name
    - `status` - `required` `string`, fixed value: DIMENSION
  - `computed_columns` - `optional` `JSON Object[]`, computed columns info
    - `columnName` - `required` `string`, the new column name
    - `expression` - `required` `string`, expression
    - `datatype` - `required` `string`, data type: VARCHAR,INT,BIGINT ...standard sql types
    - `tableIdentity` - `required` `string`, format: SCHEMA.TABLE
    - `tableAlias` - `required` `string`, table alias
  - `join_tables` - `required` `JSON Object[]`, join info
    - `table` - `required` `string`, table name
    - `join` - `required` `JSON Object`, join info
      - `type` - `required` `string`, join type: INNER,LEFT
      - `foreign_key` - `required` `string[]`, foreign key
      - `primary_key` - `required` `string[]`, primary key
      - `simplified_non_equi_join_conditions` - `optional` `JSON Object`, non-equivalent join conditions

        (note1: The support of this settings should have 'Support History Table' enabled in advance. Seeing [Slowly Changing Dimension](https://kylin.apache.org/docs/model/model_design/scd2)

        (note2: Join relationship >= and < must be used in pairs, and same column must be joint in both conditions)

        - `foreign_key` - `string`, foreign key
        - `primary_key` - `string`, primary key
        - `op` - `string`, join relationship: LESS\_THAN,GREATER\_THAN\_OR\_EQUAL
    - `kind` - `optional` `string`, table kind: FACT,LOOKUP, default: LOOKUP
    - `alias` - `optional` `string`, alias
    - `flattenable` - `required` `string`, precomputing associations(precomputing: flatten, no-precomputing: normalized), flatten is suggested
    - `join_relation_type` - `optional` `string`, join type: MANY\_TO\_ONE,MANY\_TO\_MANY, default: MANY\_TO\_ONE
  - `partition_desc` - `optional` `JSON Object`, partition columns info
    - `partition_date_column` - `required` `string`, partition date column, format: TABLE.COLUMN
    - `partition_date_format` - `required` `string`, partition date column format, including: yyyy-MM-dd, yyyyMMdd... Supported date format please check "[Model Design Basics](#model-intro)"
    - `partition_type` - `optional` `string`, partition type, including: APPEND, default: APPEND
  - `owner` - `optional` `string`, the owner of model, default current user
  - `description` - `optional` `string`, model description
  - `capacity` - `optional` `string`, model capacity, including: SMALL,MEDIUM,LARGE, default: MEDIUM
  - `filter_condition` - `optional` `string`, data filter condition. Data filter condition is an additional data filter during data loading.
  - `with_base_index` - `optional` `boolean`, adding base indexes or not, including base aggregate index and base table index. Base indexes include all dimensions and measures of the model and automatically update as the model changes by default. default: false; It is recommended to use `base_index_type` after version 4.6.6, `with_base_index` does not take effect after configuring `base_index_type`
  - `base_index_type` - `optional` `Array[String]`, select the base index type to be added, optional values `BASE_AGG_INDEX`, `BASE_TABLE_INDEX`, effective version: 4.6.6
    - `[BASE_AGG_INDEX, BASE_TABLE_INDEX]` Both the base aggregate index and the base table index are added
    - `[BASE_AGG_INDEX]` only add the base aggregate index
    - `[BASE_TABLE_INDEX]` only add the base table index
    - `[]` does not add base indexes
- Curl Request Example


```sh
curl -X POST \ 'http://host:port/kylin/api/models' \ -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ -H 'Accept-Language: en' \ -H 'Authorization: Basic QURNSU46S1lMSU4=' \ -H 'Content-Type: application/json;charset=utf-8' \
### Stringify the following JSON Object when use
-d '{"project": "pj01","fact_table": "SSB.P_LINEORDER","alias": "test_model_01","management_type": "MODEL_BASED","simplified_measures": [{"name": "COUNT_ALL","expression": "COUNT","parameter_value": [{"type": "constant","value": 1} ],"return_type": ""} ],"simplified_dimensions": [{"column": "P_LINEORDER.LO_ORDERKEY","name": "LO_ORDERKEY","status": "DIMENSION" },{"column": "P_LINEORDER.LO_CUSTKEY","name": "LO_CUSTKEY","status": "DIMENSION" },{"column": "P_LINEORDER.LO_ORDERDATE","name": "LO_ORDERDATE","status": "DIMENSION" },{"column": "P_LINEORDER.LO_ORDERPRIOTITY","name": "LO_ORDERPRIOTITY","status": "DIMENSION" },{"column": "P_LINEORDER.V_REVENUE","name": "V_REVENUE","status": "DIMENSION" },{"column": "DATES.D_YEAR","name": "D_YEAR","status": "DIMENSION" },{"column": "CUSTOMER.C_NAME","name": "C_NAME","status": "DIMENSION" },{"column": "CUSTOMER.C_PHONE","name": "C_PHONE","status": "DIMENSION"} ],"join_tables": [{"table": "SSB.DATES","join": {"type": "LEFT","foreign_key": ["P_LINEORDER.LO_ORDERDATE" ],"primary_key": ["DATES.D_DATE"] },"alias": "DATES","flattenable": "flatten","join_relation_type": "MANY_TO_ONE" },{"table": "SSB.CUSTOMER","join": {"type": "LEFT","foreign_key": ["P_LINEORDER.LO_CUSTKEY" ],"primary_key": ["CUSTOMER.C_CUSTKEY"] },"alias": "CUSTOMER","flattenable": "flatten","join_relation_type": "MANY_TO_ONE"} ],"with_base_index": true,"base_index_type": ["BASE_AGG_INDEX", "BASE_TABLE_INDEX"] }'
```

- Response Details

  - `code` - `string`, response code, succeed: `000`, failed: `999`
  - `msg` - `string`, response message
  - `data` - `JSON Object`, response data
    - `base_table_index` - `JSON Object`, base index info
      - `dimension_count` - `int`, dimension count
      - `measure_count` - `int`, measure count
      - `layout_id` - `long`, layout id
      - `operate_type` - `string`, operation type, including: UPDATE,CREATE
    - `base_agg_index` - `JSON Object`, base aggregation index info, same structure as `base_table_index`
    - `warn_code` - `string`, warning code message
- Response Example


```json
{"code": "000","msg": "","data": {"base_table_index": {"dimension_count": 8,"measure_count": 0,"layout_id": 20000000001,"operate_type": "CREATE" },"base_agg_index": {"dimension_count": 8,"measure_count": 1,"layout_id": 1,"operate_type": "CREATE" },"warn_code": null}}
```

- Failed Response Example


```json
{"code": "999","data": null,"msg": "KE-010001002(Empty Project Name):Can’t find project information. Please select a project.","stacktrace": "KE-010001002(Empty Project Name) \norg.apache.kylin.common.exception.KylinException: KE-010001002(Empty Project Name):Can’t find project information. ...","exception": "KE-010001002(Empty Project Name):Can’t find project information. Please select a project.","url": "http://host:port/kylin/api/models"}
```

- Error Code (Specific error message please check real api return.)

  - `KE-010001001`: Project Not Exist
  - `KE-010001002`: Empty Project Name
  - `KE-010006002`: Invalid Partition Column
  - `KE-010000003`: Invalid Parameter
  - `KE-010000002`: Invalid Range
  - `KE-010000004`: Invalid Name
  - `KE-010006005`: Timestamp Column Not Exist
  - `KE-010002010`: Failed to Add Models
  - `KE-010011001`: Duplicate Computed Column Name
  - `KE-010007001`: Table Not Exist

> Call this API to get a list of models under specified project that satisfies certain conditions.

- `GET http://host:port/kylin/api/models`
- URL Parameters

  - `project` - `required`, `string`, project name.
  - `page_offset` - `optional`, `int`, offset of returned result, `0` by default.
  - `page_size` - `optional`, `int`, quantity of returned result per page, `10` by default.
  - `status` - `optional`, `string`, model status.
  - `model_name` - `optional`, `string`, model name.
  - `exact` - `optional`, `boolean`, whether exactly match the model name, `true` by default.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/models?project=doc_expert' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Details

  - `Code`: `String`, response code. **Returned value**: `000` (request processing success), `999`  (request processing failed)
  - `data`: `JSON`, returned data
    - `value`: details of the returned data, which consists of:
      - `name`: `String`, model name
      - `lookups`: `JSON`, detailed list of all dimension tables
      - `size_kb`: `Long`, total size of all segments of the models
      - `input_records_count`: `Long`, number of flattened tables within all segments
      - `input_records_size`: `Long`, size of flattened tables within all segments
      - `project`: `String`, project name
      - `uuid`: `String`, model ID
      - `last_modified`: `Long`, last modified time of the model
      - `create_time`: `Long`, model creation time
      - `mvcc`: `Long`, version number with metadata modified
      - `alias`: `String`, model alias
      - `owner`: `String`, model owner
      - `config_last_modifier`: `String`, last user who modified the configuration
      - `fact_table`: `String`, fact table (one model contains only one fact table)
      - `fact_table_alias`: `String`, fact table alias
      - `join_tables`: `JSON`, joined tables
      - `partition_desc`:`JSON`, partition column
      - `all_measures`: `JSON`, all measures within the model
      - `multi_partition_desc`: `JSON`, multiple partitions
      - `computed_columns`: `JSON`, computed columns
      - `canvas`: `JSON`, position of model canvas
      - `status`: `String`, model status; **Returned value**: `online`, `offline`, `broken`, `warning`
      - `last_build_end`: `String`, building time of the last segment
      - `storage`: `Long`, total storage size of the model; **Unit:** byte
      - `source`: `Long`, sourceByte sum of all segments in the model
      - `expansion_rate`: `String`, model expansion rate; **Unit:** %
      - `usage`: `Long`, queried times of the model
      - `model_broken`: `Boolean`, if the model is broken or not
      - `root_fact_table_deleted`: `Boolean`, if the fact table is deleted
      - `segments`: `JSON`, segment lists
      - `recommendations_count`: `Integer`, number of recommendations
      - `simplified_measures`: `JSON`, measure list of the models
      - `simplified_dimensions`: `JSON`, dimension list of the models
      - `simplified_tables`: `JSON`, all tables in the model
  - `offset`: page number
  - `limit`: models listed in each page
  - `total_size`: total number of models
- Response Example


```json
  { 
      "code":"000", 
      "data":{ 
          "value":[ 
              { 
                  "name":"Model_03", 
                  "lookups":Array[1], 
                  "is_streaming":false, 
                  "size_kb":0, 
                  "input_records_count":0, 
                  "input_records_size":0, 
                  "project":null, 
                  "uuid":"0464241b-fd7d-49a9-a3c9-b4f7e32cf489", 
                  "last_modified":1574750372949, 
                  "create_time":1574761225505, 
                  "version":"4.0.0.0", 
                  "mvcc":4, 
                  "alias":"Model_03", 
                  "owner":"ADMIN", 
                  "config_last_modifier":null, 
                  "config_last_modified":0, 
                  "description":"", 
                  "fact_table":"SSB.LINEORDER", 
                  "fact_table_alias":null, 
                  "management_type":"MODEL_BASED", 
                  "join_tables":Array[1], 
                  "filter_condition":"", 
                  "partition_desc":Object{...}, 
                  "capacity":"MEDIUM", 
                  "segment_config":Object{...}, 
                  "data_check_desc":null, 
                  "semantic_version":0, 
                  "all_named_columns":Array[26], 
                  "all_measures":Array[2], 
                  "column_correlations":Array[0], 
                  "multilevel_partition_cols":Array[0], 
                  "computed_columns":Array[0], 
                  "canvas":Object{...}, 
                  "status":"ONLINE", 
                  "last_build_end":"902016000000", 
                  "storage":24694, 
                  "source":5585164, 
                  "expansion_rate":"0.44", 
                  "usage":0, 
                  "model_broken":false, 
                  "root_fact_table_deleted":false, 
                  "segments":null, 
                  "recommendations_count":0, 
                  "simplified_measures":Array[2], 
                  "simplified_dimensions":Array[9], 
                  "simplified_tables":Array[2], 
                  "multi_partition_desc": { 
                    "columns": ["KYLIN_SALES.LSTG_SITE_ID"], 
                    "partitions": [ 
                        { 
                            "id": 0, 
                            "values": [ 
                                "1" 
                            ] 
                        }, 
                        { 
                            "id": 1, 
                            "values": [ 
                                "2" 
                            ] 
                        } 
                    ], 
                    "max_partition_id": 1 
                  } 
              }, 
              Object{...}, 
              Object{...} 
          ], 
          "offset":0, 
          "limit":10, 
          "total_size":3 
      }, 
      "msg":"" 
  } 
```

> Call this API to get the descriptions of a model, for example, dimension, measure, fact table, and table join relations.

- `GET http://host:port/kylin/api/models/{project}/{model_name}/model_desc`

  > The API response does not contain dimensions and indexes recommended by the system.
- URL Parameters

  - `project` - `required` `string`, project name.
  - `model_name` - `required` `string`, model name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/models/Kylin/AUTO_MODEL/model_desc'\ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Details

  - `code`: `String`, response code. **Returned value**: `000` (request processing success), `999`  (request processing failed)
    - `data`: `JSON`, returned data
      - `uuid`: `String`, model ID
      - `last_modified`: `Long`, last modified time of the model
      - `name`: `String`, model name
      - `project`: `String`, project name
      - `dimensions`: `JSON`, dimension information
      - `id`: `Integer`, dimension ID
      - `name`: `String`, dimension name
      - `column`: `String`, column name
      - `status`: `String`, status
      - `derived`: `Boolean`, if the column is derived dimension
      - `measures`: `JSON`, measure information
      - `name`: `String`, measure name
      - `function`: `JSON`, functions
        - `expression`: `String`, expressions
        - `parameters`: `JSON`, parameters
          - `type`: `String`, parameter type
          - `value`: `String`, parameter value
      - `returntype`: `String`, returned type
      - `id`: `Integer`, measure ID
      - `aggregation_groups`: `JSON`, aggregation groups
      - `includes`: `JSON`, columns in aggregation groups
      - `select_rule`: `JSON`, type of aggregation groups
        - `hierarchy_dims`: `JSON`, dimension hierarchy
        - `mandatory_dims`: `JSON`, required hierarchy
        - `joint_dims`: `JSON`, joint dimensions
        - `computed_columns`: `JSON`, ([What is Computed Column?](#model-manual-computed_column))
        - `tableIdentity`: `String`, table ID
        - `tableAlias`: `String`, table alias
        - `columnName`: `String`, column name
        - `expression`: `String`, expression of computed columns
        - `datatype`: `String`, column type
        - `comment`: `String`, notes of the columns
        - `rec_uuid`: `String`, primary key of the column
        - `fact_table`: `String`, fact table
        - `join_tables`: `JSON`, joined tables
          - `table`: `String`, table name
          - `kind`: `String`, table type; **Returned Value**: `FACT`, `LOOKUP`
          - `alias`: `String`, table alias
          - `join`: `String`, join relation
            - `type`: `String`, join type; **Returned Value**: `INNER`, `LEFT`, `RIGHT`, `OUTER`
            - `primary_key`: `JSON`, column that is a reference to other tables **Data Type**: JSON
            - `foreign_key`: `JSON`, columns in table that are joined with this table
            - `non_equi_join_condition`: `JSON`, non-equi join conditions (object)
            - `primary_table`: `String`, current table
            - `foreign_table`: `String`, tables joined to current table
          - `flattenable`: `String`, if dimension tables are flattened tables, **Data Type**: String
        - `join_relation_type`: `String`, join relations; **Returned Value**: `MANY_TO_ONE`, `ONE_TO_ONE`, `ONE_TO_MANY`, `MANY_TO_MANY`
- Response Example


```json
 { 
    "code":"000", 
    "data":{ 
        "uuid":"24dc8eae-e613-40ce-b601-26f065f24070", 
        "last_modified":1577436020423, 
        "version":"4.0.0.0", 
        "name":"Kylin", 
        "project":"test_gy", 
        "description":"", 
        "dimensions":[ 
            { 
                "id":8, 
                "name":"P_LINEORDER_LO_CUSTKEY", 
                "column":"P_LINEORDER.LO_CUSTKEY", 
                "status":"DIMENSION", 
                "derived":false 
            } 
        ], 
        "measures":[ 
            { 
                "name":"COUNT_ALL", 
                "function":{ 
                    "expression":"COUNT", 
                    "parameters":[ 
                        { 
                            "type":"constant", 
                            "value":"1" 
                        } 
                    ], 
                    "returntype":"bigint" 
                }, 
                "id":100000 
            }, 
            { 
                "name":"TEST", 
                "function":{ 
                    "expression":"SUM", 
                    "parameters":[ 
                        { 
                            "type":"column", 
                            "value":"P_LINEORDER.LO_QUANTITY" 
                        } 
                    ], 
                    "returntype":"bigint" 
                }, 
                "id":100001 
            } 
        ], 
        "aggregation_groups":[ 
            { 
                "includes":[ 
                    "P_LINEORDER.LO_CUSTKEY" 
                ], 
                "select_rule":{ 
                    "hierarchy_dims":[ 
 
                    ], 
                    "mandatory_dims":[ 
 
                    ], 
                    "joint_dims":[ 
 
                    ] 
                } 
            } 
        ], 
        "computed_columns": [{ 
          "tableIdentity": "SSB.P_LINEORDER", 
          "tableAlias": "P_LINEORDER", 
          "columnName": "CASTCOL", 
          "expression": "CAST(P_LINEORDER.LO_PARTKEY as bigint)", 
          "innerExpression": "CAST(`P_LINEORDER`.`LO_PARTKEY` as bigint)", 
          "datatype": "BIGINT", 
          "comment": null, 
          "rec_uuid": null 
        },{...}], 
        "fact_table": "SSB.P_LINEORDER", 
        "join_tables": [{ 
          "table": "SSB.CUSTOMER", 
          "kind": "LOOKUP", 
          "alias": "CUSTOMER", 
          "join": { 
              "type": "INNER", 
              "primary_key": [ 
                  "CUSTOMER.C_CUSTKEY" 
              ], 
              "foreign_key": [ 
                  "P_LINEORDER.LO_CUSTKEY" 
              ], 
              "non_equi_join_condition": null, 
              "primary_table": null, 
              "foreign_table": null 
          }, 
          "flattenable": "flatten", 
          "join_relation_type": "MANY_TO_ONE" 
        },{...}] 
    }, 
    "msg":"" 
} 
```

> Call this API to set partition columns for certain model of certain project. To enable incremental building for a model, you should first define a partition column for this model. After this operation, Kylin will complete incremental building.

- `PUT http://host:port/kylin/api/models/{model_name}/partition`
- URL Parameters

  - `model_name` - `required` `string`, model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`，project name.
  - `partition_desc` - `optional`， partition colunm information

    - `partition_date_column` - `optional` `string`, partition colunm
    - `partition_date_format` - `optional` `string`，partition format
  - `multi_partition_desc` - `optional`, multi-level partitioning model sub-partition colunm information

    - `columns` - `array[string]`, multi-level partitioning model sub-partition colunm
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
  http://host:port/kylin/api/models/multi_partition_model/partition \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json' \ 
  -d '{ 
    "project": "multi_partition", 
    "partition_desc": { 
        "partition_date_column": "KYLIN_SALES.PART_DT", 
        "partition_date_format": "yyyy-MM-dd" 
    }, 
    "multi_partition_desc": { 
        "columns": [ 
            "KYLIN_SALES.LSTG_SITE_ID" 
        ] 
    } 
}' 
```

- Response Example


```json
{ 
    "code":"000", 
    "data":"", 
    "msg":"" 
} 
```

> Get indexes of given model.

- `GET http://host:port/kylin/api/models/{model_name}/indexes`
- URL Parameters

  - `project` - `required` `string`, project name
  - `model_name` - `required`  `string`，model alias
  - `status` - `optional` `string`, index status，support `NO_BUILD`, `BUILDING`, `LOCKED`, `ONLINE`, empty by default
  - `page_offset` - `optional` `int`, offset of returned result, `0` by default.
  - `page_size` - `optional` `int`, quantity of returned result per page, `10` by default.
  - `sources` - `optional` `string`, type of index，support `RECOMMENDED_AGG_INDEX`, `RECOMMENDED_TABLE_INDEX`, `CUSTOM_AGG_INDEX`, `CUSTOM_TABLE_INDEX`, empty by default
  - `sort_by` - `optional` `string`, sort by field，support `last_modified`, `usage`, `data_size`, `last_modified` by default
  - `reverse` - `optional` `boolean`, whether sort reverse, `true` by default
  - `batch_index_ids` - `optional` `array[long]`,specify indexId, empty by default
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```shell
curl -X GET 'http://host:port/kylin/api/models/m1/indexes?project=ssb&batch_index_ids=1,10001,20001' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Details

  - `absent_batch_index_ids`, not found indexId
  - `indexes`, index list
    - `related_tables`, index related table
- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "project": "ssb", 
        "uuid": "383cd655-89f4-4986-85cf-1d299e287e84", 
        "model_name": "m1", 
        "total_size": 2, 
        "offset": 0, 
        "limit": 10, 
        "owner": "ADMIN", 
        "absent_batch_index_ids": [20001], 
        "indexes": [ 
            { 
                "id": 1, 
                "status": "NO_BUILD", 
                "source": "CUSTOM_AGG_INDEX", 
                "col_order": [ 
                    { 
                        "key": "LINEORDER.LO_ORDERKEY", 
                        "value": "column", 
                        "cardinality": null 
                    }, 
                    { 
                        "key": "LINEORDER.LO_LINENUMBER", 
                        "value": "column", 
                        "cardinality": null 
                    }, 
                    { 
                        "key": "COUNT_ALL", 
                        "value": "measure", 
                        "cardinality": null 
                    } 
                ], 
                "shard_by_columns": [], 
                "sort_by_columns": [], 
                "data_size": 0, 
                "usage": 0, 
                "last_modified": 1610462519405, 
                "related_tables": ["SSB.LINEORDER"], 
                "storage_type": 20 
            }, 
            { 
                "id": 10001, 
                "status": "NO_BUILD", 
                "source": "CUSTOM_AGG_INDEX", 
                "col_order": [ 
                    { 
                        "key": "LINEORDER.LO_ORDERKEY", 
                        "value": "column", 
                        "cardinality": null 
                    }, 
                    { 
                        "key": "COUNT_ALL", 
                        "value": "measure", 
                        "cardinality": null 
                    } 
                ], 
                "shard_by_columns": [], 
                "sort_by_columns": [], 
                "data_size": 0, 
                "usage": 0, 
                "last_modified": 1610462519405, 
                "related_tables": ["SSB.LINEORDER"], 
                "storage_type": 20 
            } 
        ] 
    }, 
    "msg": "" 
} 
```

- `POST http://host:port/kylin/api/models/model_suggestion`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `sqls` - `required` `array`, queries to create models
  - `with_segment` - `optional`, `bool`, create an empty segment, default is true
  - `with_model_online` - `optional`, `bool`, model online or not, default is false

- Curl Request Example


```sh
curl -X POST \ 
  'http://localhost:7070/kylin/api/models/model_suggestion' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"ssb", "sqls":["select count(*) from ssb.P_LINEORDER", "SELECT 1"]}' 
```

- Response Details

  - `models`, model details
    - `uuid`, model UUID
    - `alias`, model name
    - `version`, model version
    - `rec_items`, new model information. Please note that there will be some model detail info such as dimensions or measure shown as a recommendation, but it will not truly generate such a recommendation.
      - `sqls`, sqls used by one recommendation item
      - `index_id`, reused index id, if the value is -1, a new model created
      - `dimensions`, all dimensions used, `new` used to indicate whether it is newly created or reused
      - `measues`, all measures used, `new` used to indicate whether it is newly created or reused
      - `computed_columns`, all computed\_columns used, `new` used to indicate whether it is newly created or reused
  - `error_sqls`, failed SQLs
- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "models": [ 
            { 
                "uuid": "364e4485-433c-4fe2-be57-02c59170b5d4", 
                "alias": "AUTO_MODEL_P_LINEORDER_1", 
                "version": "4.0.0.0", 
                "rec_items": [ 
                    { 
                        "sqls": [ 
                            "select count(*) from ssb.P_LINEORDER" 
                        ], 
                        "index_id": -1, 
                        "dimensions": [], 
                        "measures": [ 
                            { 
                                "measure": { 
                                    "name": "COUNT_ALL", 
                                    "function": { 
                                        "expression": "COUNT", 
                                        "parameters": [ 
                                            { 
                                                "type": "constant", 
                                                "value": "1" 
                                            } 
                                        ], 
                                        "returntype": "bigint" 
                                    }, 
                                    "id": 100000 
                                }, 
                                "new": true 
                            } 
                        ], 
                        "computed_columns": [] 
                    } 
                ] 
            } 
        ], 
        "error_sqls": [ 
            "SELECT 1" 
        ] 
    }, 
    "msg": "" 
} 
```

- `DELETE http://host:port/kylin/api/models/{model_name}`
- Request Permission: MANAGEMENT permission and above
- Introduced in: 5.0
- URL Parameters

  - `model_name` - `required` `string`, model name
- Request Parameters

  - `project` - `required` `string`, project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
'http://host:port/kylin/api/models/{model_name}?project=test' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code":"000", 
    "data":"", 
    "msg":"" 
} 
```

- `GET http://host:port/kylin/api/models/{model_name}/export`
- URL Parameters

  - `model_name` - `required` `string`, the model name
  - `project` - `required` `string`, the project name
  - `export_as` - `required` `string`, the format to export to
    - `TABLEAU_ODBC_TDS` export as Tableau TDS with Kylin ODBC datasource
    - `TABLEAU_CONNECTOR_TDS` export as Tableau TDS with Kylin Tableau Connector as the datasource
  - `element` - `string` `optional` the model elements to export
    - `AGG_INDEX_COL` (default) export only dimensions and meausres defined in Aggregate Groups
    - `AGG_INDEX_AND_TABLE_INDEX_COL` export only dimensions and meausres defined in Aggregate Groups or Table Indexes
    - `ALL_COLS` export all dimensions and measures defined in the model
  - `server_host` - `string` `optional`, the host name of the exported Kylin datasource, default to the current requesting host
  - `server_port` - `string` `optional`, the port of the export Kylin datasource, default to the current requesting port
- HTTP Header

  - Accept:application/vnd.apache.kylin-v4-public+json
  - Accept-Language: en
  - Content-Type: application/json;charset=utf-8
- Curl Request Example

```sh
curl -X GET \ 
  'http://host:port/kylin/api/models/a3/export?project=test_project&export_as=TABLEAU_ODBC_TDS&element=AGG_INDEX_COL&server_host=host&server_port=7080' \ 
  -H 'accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
 
```

- `PUT http://host:port/kylin/api/models/{model_name}/name`
- Introduced in: 5.0
- URL Parameters

  - `model_name` - `required` `string`，model name。
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: cn`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `project_name` - `required` `string`, project name.
  - `new_model_name` - `required` `string`, the new name of the model.
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/models/test_model/name' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: cn' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-d '{"project":"ssb", "new_model_name":"testNewName"}' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- `PUT http://host:port/kylin/api/models/{model_name}/status`
- Request Permission: MANAGEMENT permission and above
- Introduced in: 5.0
- URL Parameters

  - `model_name` - `required` `string`, model name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - project - `required` `string`, project name
  - status - `required` `string`, update model status, including: ONLINE,OFFLINE
- Curl Request Example


```sh
curl -X PUT \ 
'http://host:port/kylin/api/models/model_test1/status' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' 
-d '{"project": "pj01", "status": "OFFLINE"}' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- Failed Response Example


```json
{"code": "999","data": null,"msg": "KE-010001002(Empty Project Name):Can’t find project information. Please select a project.","stacktrace": "KE-010001002(Empty Project Name) \norg.apache.kylin.common.exception.KylinException: KE-010001002(Empty Project Name):Can’t find project information. ...","exception": "KE-010001002(Empty Project Name):Can’t find project information. Please select a project.","url": "http://host:port/kylin/api/models"}
```

- Error Code (Specific error message please check real api return.)

  - `KE-010001001`: Project Not Exist
  - `KE-010001002`: Empty Project Name
  - `KE-010000003`: Invalid Parameter

- `GET http://host:port/kylin/api/models/bi_export`
- URL Parameters

  - `model_name` - `required` `string`, the model name
  - `project` - `required` `string`, the project name
  - `export_as` - `required` `string`, the format to export to
    - `TABLEAU_ODBC_TDS` export as Tableau TDS with Kylin ODBC datasource
    - `TABLEAU_CONNECTOR_TDS` export as Tableau TDS with Kylin Tableau Connector as the datasource
  - `element` - `string` `optional` the model elements to export
    - `AGG_INDEX_COL` (default) export only dimensions and meausres defined in Aggregate Groups based on user rights
    - `AGG_INDEX_AND_TABLE_INDEX_COL` export only dimensions and meausres defined in Aggregate Groups or Table Indexes based on user rights
    - `ALL_COLS` export all dimensions and measures defined in the model based on user rights
    - `CUSTOM_COLS` export custom dimensions and measures defined in the model based on user rights, When using this method, the `dimensions`,  `measures` parameter must be add
  - `server_host` - `string` `optional`, the host name of the exported Kylin datasource, default to the current requesting host
  - `server_port` - `string` `optional`, the port of the export Kylin datasource, default to the current requesting port
  - `dimensions` - `List<String>` `optional`, An exported dimension list in the format of `${table_alias}.${columnName1},${table_alias}.${columnName2}` , Parameter takes effect of `element=CUSTOM_COLS`
  - `measures` - `List<String>` `optional`, An exported measures list in the format of `${measureName1},${measureName2`, Parameter takes effect of `element=CUSTOM_COLS`
- HTTP Header

  - `Accept:application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example

```sh
curl -X GET \ 
  'http://{host}:{port}/kylin/api/models/bi_export?model_name={modelName}&project={project}&export_as=TABLEAU_ODBC_TDS&server_host=localhost&server_port=8080&dimensions=CUSTOMER.C_NAME,CUSTOMER.CC_6,CUSTOMER.CC_7,CUSTOMER.CC_9,LINEORDER_1.LO_CUSTKEY&measures=m_aa&element=CUSTOM_COLS' \ 
  -H 'accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'authorization: Basic QURNSU46S1lMSU4=' \ 
```

- Failed Response Example(When all columns in the model have no permissions or table-joined columns have no permissions)

```json
{"code": "999","data": null,"msg": "KE-010002022(The table not contains unauthenticated columns):Please add permissions to columns in the table!","stacktrace": "KE-010002022(The table not contains unauthenticated columns) \norg.apache.kylin.common.exception.KylinException: KE-010002022(The table not contains unauthenticated columns):Please add permissions to columns in the table!8)...。","exception": "KE-010002022(The table not contains unauthenticated columns):Please add permissions to columns in the table!","url": "http://host:port/kylin/api/models/bi_export"}
```

- Error Code (Specific error message please check real api return.)
  - `KE-010002022`: Please add permissions to columns in the table
- Successful Code (exported as TDS file contents)

```xml
<?xml version='1.0' encoding='UTF-8'?> 
<datasource formatted-name="federated.0e6gjbn18cj0a41an9pi309itkyi" inline="true" source-platform="win" version="10.0"> 
    <connection class="federated"> 
        <named-connections> 
            <named-connection caption="localhost" name="genericodbc.11du78x0szfyb51b703es1ocv315"> 
                <connection class="genericodbc" dbname="" odbc-connect-string-extras="PROJECT=KE_36166;CUBE=test_model_3_cc" odbc-dbms-name="MySQL" odbc-driver="KylinODBCDriver" odbc-dsn="" odbc-suppress-connection-pooling="" odbc-use-connection-pooling="" port="8080" schema="DEFAULT" server="localhost" username="ADMIN"/> 
            </named-connection> 
        </named-connections> 
        <relation join="inner" type="join"> 
            <clause type="join"> 
                <expression op="="> 
                    <expression op="[CUSTOMER].[C_CUSTKEY]"/> 
                    <expression op="[CUSTOMER_1].[C_CUSTKEY]"/></expression> 
            </clause> 
            <relation join="inner" type="join"> 
                <clause type="join"> 
                    <expression op="="> 
                        <expression op="[CUSTOMER].[C_CUSTKEY]"/> 
                        <expression op="[LINEORDER_1].[LO_CUSTKEY]"/></expression> 
                </clause> 
                <relation type="table" connection="genericodbc.11du78x0szfyb51b703es1ocv315" name="CUSTOMER" table="[SSB].[CUSTOMER]"/> 
                <relation type="table" connection="genericodbc.11du78x0szfyb51b703es1ocv315" name="LINEORDER_1" table="[SSB].[LINEORDER]"/></relation> 
            <relation type="table" connection="genericodbc.11du78x0szfyb51b703es1ocv315" name="CUSTOMER_1" table="[SSB1].[CUSTOMER]"/></relation> 
        <cols> 
            <map key="[LO_ORDERPRIOTITY]" value="[LINEORDER_1].[LO_ORDERPRIOTITY]"/> 
            <map key="[C_ADDRESS (CUSTOMER_1)]" value="[CUSTOMER_1].[C_ADDRESS]"/> 
            <map key="[C_NAME (CUSTOMER_1)]" value="[CUSTOMER_1].[C_NAME]"/> 
            <map key="[C_REGION (CUSTOMER_1)]" value="[CUSTOMER_1].[C_REGION]"/> 
            <map key="[C_NATION (CUSTOMER)]" value="[CUSTOMER].[C_NATION]"/> 
            <map key="[C_CUSTKEY (CUSTOMER)]" value="[CUSTOMER].[C_CUSTKEY]"/> 
            <map key="[C_MKTSEGMENT (CUSTOMER)]" value="[CUSTOMER].[C_MKTSEGMENT]"/> 
            <map key="[LO_PARTKEY]" value="[LINEORDER_1].[LO_PARTKEY]"/> 
            <map key="[C_CITY (CUSTOMER)]" value="[CUSTOMER].[C_CITY]"/> 
            <map key="[LO_LINENUMBER]" value="[LINEORDER_1].[LO_LINENUMBER]"/> 
            <map key="[C_REGION (CUSTOMER)]" value="[CUSTOMER].[C_REGION]"/> 
            <map key="[LO_ORDERKEY]" value="[LINEORDER_1].[LO_ORDERKEY]"/> 
            <map key="[C_PHONE (CUSTOMER)]" value="[CUSTOMER].[C_PHONE]"/> 
            <map key="[CC_10]" value="[CUSTOMER].[CC_10]"/> 
            <map key="[C_ADDRESS (CUSTOMER)]" value="[CUSTOMER].[C_ADDRESS]"/> 
            <map key="[CC_4]" value="[CUSTOMER].[CC_4]"/> 
            <map key="[LO_SHIPMODE]" value="[LINEORDER_1].[LO_SHIPMODE]"/> 
            <map key="[C_CITY (CUSTOMER_1)]" value="[CUSTOMER_1].[C_CITY]"/> 
            <map key="[CC_6]" value="[CUSTOMER].[CC_6]"/> 
            <map key="[C_NATION (CUSTOMER_1)]" value="[CUSTOMER_1].[C_NATION]"/> 
            <map key="[CC_5]" value="[CUSTOMER].[CC_5]"/> 
            <map key="[C_PHONE (CUSTOMER_1)]" value="[CUSTOMER_1].[C_PHONE]"/> 
            <map key="[CC_7]" value="[CUSTOMER].[CC_7]"/> 
            <map key="[CC_9]" value="[CUSTOMER].[CC_9]"/> 
            <map key="[LO_QUANTITY]" value="[LINEORDER_1].[LO_QUANTITY]"/> 
            <map key="[LO_SUPPLYCOST]" value="[LINEORDER_1].[LO_SUPPLYCOST]"/> 
            <map key="[C_CUSTKEY (CUSTOMER_1)]" value="[CUSTOMER_1].[C_CUSTKEY]"/> 
            <map key="[LO_CUSTKEY]" value="[LINEORDER_1].[LO_CUSTKEY]"/> 
            <map key="[LO_ORDTOTALPRICE]" value="[LINEORDER_1].[LO_ORDTOTALPRICE]"/> 
            <map key="[C_NAME (CUSTOMER)]" value="[CUSTOMER].[C_NAME]"/> 
            <map key="[LO_COMMITDATE]" value="[LINEORDER_1].[LO_COMMITDATE]"/> 
            <map key="[LO_EXTENDEDPRICE]" value="[LINEORDER_1].[LO_EXTENDEDPRICE]"/> 
            <map key="[LO_REVENUE]" value="[LINEORDER_1].[LO_REVENUE]"/> 
            <map key="[LO_DISCOUNT]" value="[LINEORDER_1].[LO_DISCOUNT]"/> 
            <map key="[LO_SHIPPRIOTITY]" value="[LINEORDER_1].[LO_SHIPPRIOTITY]"/> 
            <map key="[LO_SUPPKEY]" value="[LINEORDER_1].[LO_SUPPKEY]"/> 
            <map key="[LO_TAX]" value="[LINEORDER_1].[LO_TAX]"/> 
            <map key="[LO_ORDERDATE]" value="[LINEORDER_1].[LO_ORDERDATE]"/> 
            <map key="[C_MKTSEGMENT (CUSTOMER_1)]" value="[CUSTOMER_1].[C_MKTSEGMENT]"/> 
        </cols> 
    </connection> 
    <aliases enabled="yes"/> 
    <column caption="LO_ORDERPRIOTITY" datatype="string" name="[LO_ORDERPRIOTITY]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="C_ADDRESS_CUSTOMER_1" datatype="string" name="[C_ADDRESS (CUSTOMER_1)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="C_NAME_CUSTOMER_1" datatype="string" name="[C_NAME (CUSTOMER_1)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="C_REGION_CUSTOMER_1" datatype="string" name="[C_REGION (CUSTOMER_1)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="C_NATION" datatype="string" name="[C_NATION (CUSTOMER)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="C_CUSTKEY" datatype="integer" name="[C_CUSTKEY (CUSTOMER)]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_MKTSEGMENT" datatype="string" name="[C_MKTSEGMENT (CUSTOMER)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="LO_PARTKEY" datatype="integer" name="[LO_PARTKEY]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_CITY" datatype="string" name="[C_CITY (CUSTOMER)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="LO_LINENUMBER" datatype="integer" name="[LO_LINENUMBER]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_REGION" datatype="string" name="[C_REGION (CUSTOMER)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="LO_ORDERKEY" datatype="integer" name="[LO_ORDERKEY]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_PHONE" datatype="string" name="[C_PHONE (CUSTOMER)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="CC_10" datatype="integer" name="[CC_10]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_ADDRESS" datatype="string" name="[C_ADDRESS (CUSTOMER)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="CC_4" datatype="integer" name="[CC_4]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_SHIPMODE" datatype="string" name="[LO_SHIPMODE]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="C_CITY_CUSTOMER_1" datatype="string" name="[C_CITY (CUSTOMER_1)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="CC_6" datatype="integer" name="[CC_6]" role="dimension" type="ordinal"/> 
    <column caption="C_NATION_CUSTOMER_1" datatype="string" name="[C_NATION (CUSTOMER_1)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="CC_5" datatype="integer" name="[CC_5]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_PHONE_CUSTOMER_1" datatype="string" name="[C_PHONE (CUSTOMER_1)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="CC_7" datatype="integer" name="[CC_7]" role="dimension" type="ordinal"/> 
    <column caption="CC_9" datatype="integer" name="[CC_9]" role="dimension" type="ordinal"/> 
    <column caption="LO_QUANTITY" datatype="integer" name="[LO_QUANTITY]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_SUPPLYCOST" datatype="integer" name="[LO_SUPPLYCOST]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_CUSTKEY_CUSTOMER_1" datatype="integer" name="[C_CUSTKEY (CUSTOMER_1)]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_CUSTKEY" datatype="integer" name="[LO_CUSTKEY]" role="dimension" type="ordinal"/> 
    <column caption="LO_ORDTOTALPRICE" datatype="integer" name="[LO_ORDTOTALPRICE]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_NAME_1" datatype="string" name="[C_NAME (CUSTOMER)]" role="dimension" type="nominal"/> 
    <column caption="LO_COMMITDATE" datatype="date" name="[LO_COMMITDATE]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_EXTENDEDPRICE" datatype="integer" name="[LO_EXTENDEDPRICE]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_REVENUE" datatype="integer" name="[LO_REVENUE]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_DISCOUNT" datatype="integer" name="[LO_DISCOUNT]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_SHIPPRIOTITY" datatype="integer" name="[LO_SHIPPRIOTITY]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_SUPPKEY" datatype="integer" name="[LO_SUPPKEY]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_TAX" datatype="integer" name="[LO_TAX]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="LO_ORDERDATE" datatype="date" name="[LO_ORDERDATE]" role="dimension" type="ordinal" hidden="true"/> 
    <column caption="C_MKTSEGMENT_CUSTOMER_1" datatype="string" name="[C_MKTSEGMENT (CUSTOMER_1)]" role="dimension" type="nominal" hidden="true"/> 
    <column caption="COUNT_ALL" datatype="integer" name="[COUNT_ALL]" role="measure" type="quantitative" hidden="true"> 
        <calculation class="tableau" formula="COUNT(1)"/> 
    </column> 
    <column caption="" datatype="integer" name="[m_aa]" role="measure" type="quantitative"> 
        <calculation class="tableau" formula="SUM([CC_4])"/> 
    </column> 
    <column caption="" datatype="integer" name="[m_bb]" role="measure" type="quantitative" hidden="true"> 
        <calculation class="tableau" formula="SUM([CC_5])"/> 
    </column> 
    <column caption="" datatype="integer" name="[m_cc]" role="measure" type="quantitative" hidden="true"> 
        <calculation class="tableau" formula="SUM([C_CUSTKEY (CUSTOMER)])"/> 
    </column> 
    <column caption="" datatype="integer" name="[m_dd]" role="measure" type="quantitative" hidden="true"> 
        <calculation class="tableau" formula="SUM([CC_10])"/> 
    </column> 
    <drill-paths> 
        <drill-path name="[C_ADDRESS (CUSTOMER)], [C_NATION (CUSTOMER)], [CC_7]"> 
            <field>[C_ADDRESS (CUSTOMER)]</field> 
            <field>[C_NATION (CUSTOMER)]</field> 
            <field>[CC_7]</field> 
        </drill-path> 
    </drill-paths> 
    <semantic-values> 
        <semantic-value key="[Country].[Name]" value="&quot;美国&quot;"/> 
    </semantic-values> 
</datasource> 
```

- `PUT http://host:port/kylin/api/index_plans/agg_groups`
- Introduced in: 5.0
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name
  - `model` - `required` `string`, model name
  - `aggregation_groups` - `required` `JSON Object[]`, agg group json array, can add multiple agg groups
    - `dimensions` - `required` `array[string]`, dimension array, must be in database.table format, and the added dimension must have been added as a dimension in the model
    - `measures` - `optional` `array[string]`, measure array, the added measure name is the measure name defined in the model, case-sensitive
    - `mandatory_dims` - `optional` `array[string]`, mandatory dimension array, the dimensions that must be included in the index generated by the aggregate group
    - `hierarchy_dims` - `optional` `array[array[string]]`, hierarchy dimension array, the dimensions that can be optimized according to the hierarchical relationship in the index generated by the aggregate group, a set of hierarchy dimensions in an array
    - `joint_dims` - `optional` `array[array[string]]`, joint dimension array, the dimensions that must also be included in the index generated by the aggregate group, a set of joint dimensions in an array
    > **NOTICE**： `mandatory_dims` 、`hierarchy_dims` 、`joint_dims` must be in `dimensions`, and any dimension can only be set once in mandatory dimension, hierarchy dimension or joint dimension.

    - `dim_cap` - `optional` `int`, Maximum number of dimension combinations(MDC) for a single aggregate group, positive integer
  - `global_dim_cap` - `optional` `int`, global MDC in this request, priority global\_dim\_cap < dim\_cap
  - `restore_deleted_index` - `optional` `boolean`, When the indexes generated by the aggregate group have been deleted, whether to generate these indexes again when adding the aggregate group, the default is false, which means not to add.
- Curl Request Example


```sh
curl -X PUT \ 'http://localhost:7070/kylin/api/index_plans/agg_groups' \ -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ -H 'Accept-Language: cn' \ -H 'Authorization: Basic QURNSU46S1lMSU4=' \ -H 'Content-Type: application/json;charset=utf-8' -d '{"project":"ssb","model":"testNewName","aggregation_groups":[{"dimensions":["CUSTOMER_DETAILS.IMei","CUSTOMER_DETAILS.REGION","CUSTOMER_DETAILS.BALANCE" ],"measures":["ME2" ],"mandatory_dims":["CUSTOMER_DETAILS.reGION" ],"hierarchy_dims":[["CUSTOMER_DETAILS.Imei"] ],"joint_dims":[["CUSTOMER_DETAILS.BALANCE"] ],"dim_cap": 4} ],"global_dim_cap":3,"restore_deleted_index":false }'
```

- Response Details

  - code - string, response code, succeed: 000, failed: 999
  - removed\_layouts\_size - The number of indexes to delete
  - added\_layouts\_size - The number of indexes to add
  - recovered\_layouts\_size - The number of deleted indexes in the generated indexes, when restore\_deleted\_index = true, these indexes will be added
- Response Example


```json
{"code": "000","data": {"removed_layouts_size": 0,"added_layouts_size": 3,"recovered_layouts_size": 0 },"msg": ""}
```

---

<a id="restapi-model_api-model_build_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/model_api/model_build_api/ -->

<!-- page_index: 124 -->

# Model Data Loading

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- `POST http://host:port/kylin/api/models/{model_name}/segments`
- URL Parameters

  - `model_name` - `required` `string`, model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `start` - `optional` `string`, when the model is built in full, it is not required, and it is required when the model is incrementally built. start time of segment (partition column exist), type: timestamp, unit: ms. For example, `694195200000` means `1992-01-01 00:00:00`.
  - `end` - `optional` `string`, when the model is built in full, it is not required, and it is required when the model is incrementally built. end time of segment (partition column exist), type: timestamp, unit: ms. For example, `883584000000` means `1998-01-01 00:00:00`.
  - `build_all_indexes` - `optional` `boolean`, build all indexes in the new segment, default value is `true`
  - `sub_partition_values` - `optional` `Array` , sub-partition value, used for multi-level partition model. the default is empty. For multi-leve partition model, when `build_all_indexes` is `true` (all indexes need to be built), this value is required. When `build_all_indexes` is `false`(when creating an empty segment), the value must be empty.
  - `priority` - `optional` `int`, set job priority with range `0-4` which indicates the priority from high to low. Default value is `3`
  - `build_all_sub_partitions` - `optional` `boolean`, build all sub partition values for multi-level partition model,default value is `false`
  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)
  - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/models/SSB_LINEORDER/segments' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"doc_expert", "start": "694195200000", "end": "883584000000","build_all_indexes":true,"sub_partition_values":[["1"],["2"]],"build_all_sub_partitions":false}' 
```

- Response Example


```json
{"code": "000","data": {"jobs": [{"job_name": "INC_BUILD","job_id": "61f4d697-e648-4ace-8e52-155829417b2a" },{"job_name": "INDEX_BUILD","job_id": "0217b970-4525-468b-ba25-58bbb168d612"}] },"msg": ""}
```

---

<a id="restapi-model_api-model_import_and_export_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/model_api/model_import_and_export_api/ -->

<!-- page_index: 125 -->

# Model Import & Export

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- `GET http://host:port/kylin/api/metastore/previews/models?project=test&model_names=model1,model2`
- URL Parameters

  - `project` - `required` `string`, project name.
  - `model_names` - `optional` `array[string]`, model's name, separated by commas.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl --location --request GET 'http://host:port/kylin/api/metastore/previews/models?project=target_project&model_names=model_index' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example

  - Field description
    - `code` - `string`, return code, `000` Means successful import, `999` Means import failed.
    - `data` - `json`, return data
      - `uuid` - `string` uuid;
      - `name` - `string` model's name;
      - `status` - `string` model's status;
      - `has_recommendations` - `boolean` whether model has recommendations;
      - `has_override_props` - `boolean` whether model has override properties;
      - `has_multiple_partition_values` - `boolean` whether model has multiple columns;


```json
{"code": "000","data": [{"uuid": "10d5eb7c-d854-4f72-9e4b-9b1f3c65bcda","name": "model_index","status": "ONLINE","has_recommendations": true,"has_override_props": true,"has_multiple_partition_values": true,"tables": [{"name": "SSB.P_LINEORDER","kind": "FACT" },{"name": "SSB.CUSTOMER","kind": "LOOKUP"}]} ],"msg": ""}
```

- `POST http://host:port/kylin/api/metastore/backup/models?project=test`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Body: JSON Object

  - `names` - `required` `array[string]`, model name list.
  - `export_recommendations` - `optional` `boolean`, true/false, default value is false,whether export model's recommendations.
  - `export_over_props` - `optional` `boolean`, true/false, default value is false, whether export model's override props.
  - `export_multiple_partition_values` - `optional` `boolean`, true/false, default is false, whether export model's multiple partition values.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl --remote-name --remote-header-name --location --request POST 'http://host:port/kylin/api/metastore/backup/models?project=original_project' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
--data '{ 
    "names": [ 
        "ssb_model" 
    ], 
    "export_recommendations": true, 
    "export_over_props": true, 
    "export_multiple_partition_values": true 
}' 
```

- Response Example

  return zip file on success

> Note: The remote-header-name parameter is available in curl 7.20.0 and above

- `POST http://host:port/kylin/api/metastore/validation/models?project=test`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Body: form-data

  - `file` - `required` `MultipartFile`, model metadata file.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
- Curl Request Example


```sh
curl --location --request POST 'http://host:port/kylin/api/metastore/validation/models?project=original_project' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
--form 'file=@metadata.zip' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "models": { 
            "ssb_model": { 
                "differences": 3, 
                "missing_items": [], 
                "new_items": [], 
                "update_items": [], 
                "reduce_items": [ 
                    { 
                        "reason": null, 
                        "attributes": { 
                            "name": "LO_SUPPLYCOST", 
                            "alias_dot_column": "P_LINEORDER.LO_SUPPLYCOST" 
                        }, 
                        "detail": "LO_SUPPLYCOST", 
                        "type": "MODEL_DIMENSION", 
                        "model_alias": "ssb_model", 
                        "importable": true, 
                        "creatable": true, 
                        "overwritable": true 
                    }, 
                    { 
                        "reason": null, 
                        "attributes": { 
                            "col_orders": [ 
                                "P_LINEORDER.LO_CUSTKEY", 
                                "P_LINEORDER.LO_DISCOUNT", 
                                "P_LINEORDER.LO_LINENUMBER", 
                                "P_LINEORDER.LO_ORDERDATE", 
                                "P_LINEORDER.LO_ORDERKEY", 
                                "P_LINEORDER.LO_PARTKEY", 
                                "P_LINEORDER.LO_QUANTITY", 
                                "P_LINEORDER.LO_SUPPKEY", 
                                "P_LINEORDER.LO_SUPPLYCOST" 
                            ] 
                        }, 
                        "detail": "20000050001", 
                        "type": "WHITE_LIST_INDEX", 
                        "model_alias": "ssb_model", 
                        "importable": true, 
                        "creatable": true, 
                        "overwritable": true 
                    }, 
                    { 
                        "reason": null, 
                        "attributes": { 
                            "col_orders": [ 
                                "P_LINEORDER.LO_CUSTKEY", 
                                "P_LINEORDER.LO_QUANTITY", 
                                "P_LINEORDER.LO_SUPPKEY", 
                                "LO_SUPPKEY_SUM", 
                                "COUNT_ALL" 
                            ] 
                        }, 
                        "detail": "180001", 
                        "type": "WHITE_LIST_INDEX", 
                        "model_alias": "ssb_model", 
                        "importable": true, 
                        "creatable": true, 
                        "overwritable": true 
                    } 
                ], 
                "importable": true, 
                "overwritable": true, 
                "creatable": true 
            } 
        } 
    }, 
    "msg": "" 
} 
```

  - Field description

    - `code` - `string`, return code, `000` Means successful import, `999` Means import failed.
    - `data` - `json`, return data
      - `models` - `array[object]`, validate information of each import model
        - `key` - `string`, model's name
          - `differences` - `int`, the total differences of model metadata between zip file and target model
          - `missing_items` - `array[object]`, table or table column is required but target project didn't have
          - `new_items` - `array[object]`, the new items between import and target model
          - `reduce_items` - `array[object]`, the reduced items between import and target model
          - `update_items` - `array[object]`, the updated items between import and target model
          - `has_same_name` - `boolean`, whether has same name model
          - `importable` - `boolean`, whether the model can import
          - `overwritable` - `boolean`, whether the model can overwrite target model
          - `creatable` - `boolean`, whether the model can create a new model

- `POST http://host:port/kylin/api/metastore/import/models?project=test`
- URL Parameters

  - `project` - `required` `string`, project name.
- HTTP Body: form-data

  - `file` - `required` `MultipartFile`, model metadata file.
  - `request` - `required` `MultipartFile`, json file. file content is:


```text
{"models":[{"original_name":"ssb_model","target_name":"ssb_model","import_type":"OVERWRITE"}]}
```

    - `original_name` -`string` original model's name
    - `target_name` -`string` target model's name, set value while import\_type is NEW
    - `import_type` - `string` optional values are `NEW`, `OVERWRITE`, `UN_IMPORT`. `NEW` means create new model, `OVERWRITE` means overwrite existing model, `UN_IMPORT` means not import model.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
- Curl Request Example


```sh
curl --location --request POST 'http://host:port/kylin/api/metastore/import/models?project=original_project' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
--form 'file=@metadata.zip;type=application/octet-stream' \ 
--form 'request=@request.json;type=application/json' 
```

- Response Example


```json
{ 
      "code":"000", 
      "data":"", 
      "msg":"" 
} 
```

---

<a id="restapi-model_api-model_multilevel_partitioning_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/model_api/model_multilevel_partitioning_api/ -->

<!-- page_index: 126 -->

# Multi-level Partitioning

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

For multi-level partition model define partition column, please refer to [Define Partition Column](#restapi-model_api-intro) directly.

You can add it by specifying `sub_partition_values` when [Load Segment](#restapi-model_api-model_build_api) directly or execute following API.

- `POST http://host:port/kylin/api/models/{model_name}/segments/multi_partition/sub_partition_values`
- URL Parameters

  - `model_name` - `required` `string`,model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`,project name.
  - `sub_partition_values` - `required` `array`,sub-partition values.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
    http://host:port/kylin/api/models/multi_level_partition/segments/multi_partition/sub_partition_values \ 
    -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
    -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
    -H 'Content-Type: application/json;charset=utf-8' \ 
    -d '{ 
      "project":"multi_level_partition", 
      "sub_partition_values":[["5"]] 
  }' 
```

- Response Example


```json
{ 
     "code": "000", 
     "data": "", 
     "msg": "" 
} 
```

For building multi-level partition model, please refer directly to [Load Segment API](#restapi-model_api-model_build_api).

- `POST http://host:port/kylin/api/models/{model_name}/segments/multi_partition`
- URL Parameters

  - `model_name` - `required` `string`,model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`,project name.
  - `segment_id` - `required` `string`,Segment id.
  - `sub_partition_values` - `required` `array`,sub-partition values.
  - `parallel_build_by_segment` - `optional` `boolean`, whether to build concurrently,the default value is `false`.
  - `build_all_sub_partitions` - `optional` `boolean` whether to build all sub-partition values,the default value is `false`.
  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)
  - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  http://host:port/kylin/api/models/multi_partition_model/segments/multi_partition \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
    "project": "multi_partition_project", 
    "segment_id": "983904fa-d573-4944-acb8-558c59598a48", 
    "sub_partition_values": [ 
        [ 
            "5" 
        ] 
    ], 
    "parallel_build_by_segment": false, 
    "build_all_sub_partitions": false 
}' 
```

- Response Example


```json
{"code": "000","data": {"jobs": [{"job_name": "SUB_PARTITION_BUILD","job_id": "0282e2c9-63e3-46b0-85f6-6e74ca5bf984"}] },"msg": ""}
```

- `DELETE http://host:port/kylin/api/models/segments/multi_partition`
- URL Parameters

  - `project` - `required` `string`,project name.
  - `model` - `required` `string`,model name.
  - `segment_id` - `required` `string`, Segment Id.
  - `sub_partition_values` - `required` `string`, sub-partition values.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/models/segments/multi_partition?project=multi_partition_project&model=multi_partition_model&segment_id=ff839b0b-2c23-4420-b332-0df70e36c343&sub_partition_values=0,1' \ 
  -H 'accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- `PUT http://host:port/kylin/api/models/{model_name}/segments/multi_partition`
- URL Parameters

  - `model_name` - `required` `string`,model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`,project name.
  - `segment_id` - `required` `string`,Segment id.
  - `sub_partition_values` - `required` `array`,sub-partition values.
  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)
  - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
  http://host:port/kylin/api/models/SSB_LINEORDER/segments/multi_partition \ 
  -H 'accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"default","segment_id":"60615c5e-2ae1-4ee9-b88d-f00f1f101a8a","sub_partition_values":[["1"], ["2"]]}' 
```

- Response Example


```json
{"code": "000","data": {"jobs": [{"job_name": "SUB_PARTITION_REFRESH","job_id": "4fa1a0a1-6a97-4be9-bdf6-8957c5f80114"}] },"msg": ""}
```

Please refer to [Get Segment List](#restapi-segment_management_api) for multi-level partition model to get Segment list.

- `GET http://host:port/kylin/api/models/{model_name}/segments/multi_partition`
- URL Parameters

  - `project` - `required` `string`, project name.
  - `segment_id` - `required` `string`, Segment Id.
  - `page_offset` - `optional` `int`, pagination page, the default value is 0.
  - `page_size` - `optional` `int`, page size, the default value is 10.
  - `model_name` - `required` `string`, model name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
 'http://host:port/kylin/api/models/multi_partition_model/segments/multi_partition?project=multi_partition_project&segment_id=ffdfc037-7c63-4499-986d-9b680276161e' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Authorization: Basic QURNSU46a3lsaW5AMjAxOQ==' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "value": [ 
            { 
                "id": 2, 
                "values": [ 
                    "3" 
                ], 
                "status": "ONLINE", 
                "last_modified_time": 1609213843048, 
                "source_count": 0, 
                "bytes_size": 3747 
            }, 
            { 
                "id": 3, 
                "values": [ 
                    "4" 
                ], 
                "status": "ONLINE", 
                "last_modified_time": 1609213843048, 
                "source_count": 0, 
                "bytes_size": 3747 
            } 
        ], 
        "offset": 0, 
        "limit": 10, 
        "total_size": 2 
    }, 
    "msg": "" 
} 
```

- `PUT http://host:port/kylin/api/models/{model_name}/multi_partition/mapping`
- URL Parameters

  - `model_name` - `required` `string`,model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`,project name.
  - `alias_columns` - `required`,`array<string>`, The corresponding column name that the sub-partition column needs to be mapped to
  - `multi_partition_columns` - `required`,`array<string>`, sub-partition column names
  - `value_mapping` - `required`,`array<object>`, partition value mapping

    - `origin` - `required`,`array<string>`, sub-partition column value
    - `target` - `required`, `array<string>`, sub-partition column value mapping value
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ http://host:port/kylin/api/models/test_multi/multi_partition/mapping \ -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ -H 'Authorization: Basic QURNSU46a3lsaW5AMjAxOQ==' \ -H 'Content-Type: application/json;charset=utf-8' \ -d '{"project": "multi_partition_project","alias_columns": ["KYLIN_SALES.LEAF_CATEG_ID"],"multi_partition_columns": ["KYLIN_SALES.LSTG_SITE_ID"],"value_mapping": [{"origin": ["Beijing"],"target":["North"] },{"origin":["Shanghai"],"target":["South"]}] }'
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

---

<a id="restapi-segment_management_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/segment_management_api/ -->

<!-- page_index: 127 -->

# Segment Management

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

> Call this API to acquire the Segment list of certain model. After calling the "Replenish Indexes among Segments" API, use this API to confirm if segments are successfully built.

- `GET http://host:port/kylin/api/models/{model_name}/segments`
- URL Parameters

  - `model_name` - `required` `string`, model name.
  - `project` - `required` `string`, project name.
  - `page_offset` - `optional` `int`, offset of returned result, `0` by default.
  - `page_size` - `optional` `int`, quantity of returned result per page, `10` by default.
  - `start` - `optional` `string`, start time of segments, `1` by default, type: timestamp, unit: ms.
  - `end` - `optional` `string` , end time of segments, `9223372036854775806` by default, type: timestamp, unit: ms.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/models/SSB_LINEORDER/segments?project=doc_expert' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "value": [ 
            { 
                "id": "99c547b7-1bc1-4b57-b62a-127c080e1fd2", 
                "name": "20120101000000_20130101000000", 
                "create_time_utc": 1609209524110, 
                "status": "READY", 
                "segRange": { 
                    "@class": "org.apache.kylin.metadata.model.SegmentRange$TimePartitionedSegmentRange", 
                    "date_range_start": 1325347200000, 
                    "date_range_end": 1356969600000 
                }, 
                "timeRange": null, 
                "parameters": null, 
                "dictionaries": null, 
                "snapshots": null, 
                "last_build_time": 1609209642839, 
                "source_count": 2, 
                "source_bytes_size": 798009, 
                "column_source_bytes": {}, 
                "ori_snapshot_size": {}, 
                "additionalInfo": { 
                    "segment_path": "hdfs://nameservice1/kylin/jrc_kylin/multi_partition/parquet/d5b94380-f84f-481f-b4bb-ffa3f6b3b391/99c547b7-1bc1-4b57-b62a-127c080e1fd2", 
                    "file_count": "14" 
                }, 
                "is_encoding_data_skew": false, 
                "is_snapshot_ready": false, 
                "is_dict_ready": false, 
                "is_flat_table_ready": false, 
                "is_fact_view_ready": false, 
                "multi_partitions": [], 
                "max_bucket_id": 13, 
                "bytes_size": 12520, 
                "hit_count": 0, 
                "status_to_display": "ONLINE", 
                "index_count": 7, 
                "index_count_total": 7, 
                "multi_partition_count": 2, 
                "multi_partition_count_total": 2, 
                "row_count": 13, 
                "second_storage_nodes":[ 
                    { 
                        "name":"sandbox.hortonworks.com", 
                        "ip":"10.1.2.55", 
                        "port":9500 
                    } 
                ], 
                "second_storage_size":12989, 
                "has_base_table_index":true, 
                "has_base_agg_index":true, 
                "has_base_table_index_data":true, 
                "last_modified_time": 1609209642839 
            } 
        ], 
        "offset": 0, 
        "limit": 10, 
        "total_size": 1 
    }, 
    "msg": "" 
} 
```

> Call this API to refresh segments or merge consecutive segments. Use this API to refresh Segment when there are index changes, or to merge multiple consecutive small segments to control file number and improve query performance.

- `PUT http://host:port/kylin/api/models/{model_name}/segments`
- URL Parameters

  - `model_name` - `required` `string`, model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `type` - `optional` `string`, refresh segments or merge continuous segments, the optional value should be either `REFRESH` or  `MERGE` and the default value is `REFRESH`.
  - `ids` - `optional` `array[string]`, segment id list.
  - `names` - `optional` `array[string]`, segment name list.
  > **Notice:** For `ids` and `names`, one of them must be set, and both cannot be set at the same time or both are empty at the same time.
  >
  > - `priority` - `optional` `int`, set job priority with range `0-4` which indicates the priority from high to low. Default value is `3`

  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)
- `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
  'http://host:port/kylin/api/models/SSB_LINEORDER/segments' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"doc_expert", "ids":["8f3b4040-aa75-4e74-9730-6bf1cae61745"], "type":"REFRESH"}' 
```

- Response Example


```json
  { 
      "code":"000", 
      "data":"", 
      "msg":"" 
  } 
```

- `DELETE http://host:port/kylin/api/models/{model_name}/segments`
- URL Parameters

  - `model_name` - `required` `string`, model name.
  - `project` - `required` `string`, project name.
  - `purge` - `required` `boolean`, whether purge all segments or not.
  - `ids` - `optional` `array[string]`, segment id list.
  - `names` - `optional` `array[string]`, segment name list.
  - `force` - `optional` `boolean`, whether force to delete, default value is "false".

> **Reminders**：
>
> 1.if `purge` is `false`, for `ids` and `names`, one of them must be set, and both cannot be set at the same time or both are empty at the same time.
>
> 2.Because the http protocol has a limit on the size of the request header, it is recommended that the count of the `ids` or `names` is less than 100.

- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/models/SSB_LINEORDER/segments?project=doc_expert&ids=291b9926-eaba-42d1-9d70-0a587992bea7&purge=false' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
  { 
      "code":"000", 
      "data":"", 
      "msg":"" 
  } 
```

> Verify whether there are overlapping segments within the model

- `POST http://host:port/kylin/api/models/{model_name}/segments/check`
- Request Permission: Operation permission and above
- Effective Versions: 4.1.1 and above
- URL Parameters

  - `model_name` - `required` `string`, model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `start` - `required` `string`, start time, type: timestamp, unit: ms.
  - `end` - `required` `string`, end time, type: timestamp, unit: ms.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/models/ssb_model/segments/check' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
      	"project":"ssb", 
      	"start":"775785600000", 
      	"end":"775789200000" 
      }' 
```

- Response Example


```json
{"code": "000","data": {"segments_overlap": [{"segment_id": "17df7def-f06b-4b67-81d8-4c8368e714dc","segment_name": "19920101000000_19980802000000" },{"segment_id": "1a9c070b-3847-48c6-b938-7109379eef9b","segment_name": "19980802000000_19980803000000" },{"segment_id": "5cece637-daef-47f5-88e9-85b6a247d357","segment_name": "19980803000000_19980804000000"}] },"msg": ""}
```

> Note：Specify the model, build all the missing indexes for all Segments of the model

- `POST http://host:port/kylin/api/models/{model_name}/indexes`
- URL Parameters

  - `model_name` - `required` `string`, model name.
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `priority` - `optional` `int`, set job priority with range `0-4` which indicates the priority from high to low. Default value is `3`
  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)
  - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/models/ssb_test/indexes' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"ssb"}' 
```

- Response Details

  - `type`, job type
    - NORM\_BUILD, Build normally
    - NO\_LAYOUT, All indexes to be completed are not online
    - NO\_SEGMENT, All segments to be completed are not online
  - `job_id`, the job id will be returned if the type is NORM\_BUILD. Otherwise this value will be empty if there is no index or segment.
- Response Example


```json
{"code":"000","data":{"type":"NORM_BUILD","job_id":"e3aa809b-5e73-42a5-a1e1-649d53b16e2c" },"msg":""}
```

- `POST http://host:port/kylin/api/models/{model_name}/segments/completion`
- URL Parameters

  - `model_name` - `required` `string`, model name
  - `project` - `required` `string`, project name
  - `parallel` - `optional` `boolean`, whether build with parallel tasks, by default it is false
  - `ids` - `optional` `array[string]`, segment id list
  - `names` - `optional` `array[string]`, segment name list
  > **Notice:** For `ids` and `names`, one of them must be set, and both cannot be set at the same time or both are empty at the same time.

  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)
  - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
'http://host:port/kylin/api/models/m1/segments/completion?project=ssb&names=19900101000000_19950101000000,19950101000000_19970101000000' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{"code": "000","data": {"jobs": [{"job_name": "INDEX_BUILD","job_id": "74e28420-e317-42a9-a221-a7b381b5aeea"} ],"failed_segments": [] },"msg": ""}
```

---

<a id="restapi-snapshot_management_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/snapshot_management_api/ -->

<!-- page_index: 128 -->

# Snapshot Management

Version: 5.0.2

> Note:
>
> 1. Before reading, please finish the [Access and Authentication REST API](#restapi-authentication) chapter to understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

>
> [!NOTE]
> : When the Snapshot Management API is enabled, the system will no longer build or refresh snapshots automatically, please manually manage snapshots according to the snapshot list.

- `PUT http://host:port/kylin/api/projects/{project}/snapshot_config`
- Request Permission: ADMIN permission and above
- Introduced in: 5.0
- URL Parameters
  - `project` - `required` `string`, project name.
- HTTP Body: JSON Object
  - `snapshot_manual_management_enabled` - `optional` `boolean`, whether to enable snapshot management. The default value is false.
- HTTP Header
  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example

```sh
curl -X PUT \ 
  'http://host:port/kylin/api/projects/gc_test/snapshot_config' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ "snapshot_manual_management_enabled": true }' 
```

- Response

```json
{ 
    "code": "000",  
    "data": "",  
    "msg": "" 
} 
```

- `POST http://host:port/kylin/api/snapshots`
- Request Permission: OPERATION permission and above
- Introduced in: 5.0 (Partition building: since 5.0)
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `tables` - `optional` `array[string]`, load tables with the format `DB.TABLE`
  - `databases` - `optional` `array[string]`, load all the tables under this database
    **Note:** The above two parameters `databases` and `tables` cannot be empty at the same time, which means you must use one of them to load tables.
  - `priority` - `optional` `integer`, set job priority with range `0-4` which indicates the priority from high to low. Default value is `3`
  - `options` - `optional` `map[string:args]`, mapping from table (`DB.TABLE`) to argument set, `args` can be set as follows：
    - `partition_col` - `optional` `string` partition column of responding table, null by default.
    - `partitions_to_build` - `optional` `string` only refresh the special partitions
  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)

> [!NOTE]
> - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. The maximum size of value is 1 KB.
>   : If the loaded table already exists in the system, it will be reloaded.

- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example

```sh
curl -X POST \ 
  'http://host:port/kylin/api/snapshots' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"gc_test",  "tables": ["SSB.P_LINEORDER",  "DEFAULT.TEST_KYLIN_FACT"], "options":{"DEFAULT.TEST_KYLIN_FACT":{"partition_col":"CAL_DT","incremental_build":"true","partitions_to_build":["2012-03-01","2012-03-04"]}}}' 
```

- Curl Response Example

```json
{"code": "000","data": {"jobs": [{"job_name": "SNAPSHOT_BUILD","job_id": "65b3b0a4-d4d2-4a5b-af29-b190ca420543" },  {"job_name": "SNAPSHOT_BUILD","job_id": "24aafb93-1cde-43d1-a627-8cd592f51cfe" }] },"msg": ""}
```

- `POST http://host:port/kylin/api/snapshots/config`
- Request Permission: OPERATION permission and above
- Introduced in: 5.0
- HTTP Body: JSON Object
  - `project` - `required` `string`, project name.
  - `table_partition_col` - `required` `map[string:string]` The mapping from table (DB.TABLE) to chosen partition column.
- HTTP Header
  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example

```sh
 curl -X POST \ 
   'http://host:port/kylin/api/snapshots/config' \ 
   -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
   -H 'Accept-Language: en' \ 
   -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
   -H 'Content-Type: application/json;charset=utf-8' \ 
   -d '{"project":"gc_test","table_partition_col":{"DEFAULT.TEST_KYLIN_FACT":"CAL_DT"}}' 
```

- Response

```json
 { 
     "code": "000", 
     "data": "", 
     "msg": "" 
 } 
```

- `PUT http://host:port/kylin/api/snapshots`
- Request Permission: OPERATION permission and above
- Introduced in: 5.0 (Partition building: since 5.0)
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `tables` - `optional` `array[string]`, load tables with the format `DB.TABLE`
  - `databases` - `optional` `array[string]`, load all the tables under this database

    **Note:** The above two parameters `databases` and `tables` cannot be empty at the same time, which means you must use one of them to load tables.
  - `priority` - `optional` `int`, set job priority with range `0-4` which indicates the priority from high to low. Default value is `3`
  - `options` - `required` `map[string:args]`, mapping from table (`DB.TABLE`) to arguments, `args` can be set as follows：

    - `partition_col` - `required` `string`, partition column of responding table, null by default. If you have set partition columns for tables to be refreshed, here **need to enter the corresponding partition column**
    - `incremental_build` - `optional` `boolean`, whether keep the built partitions, false by default.
    - `partitions_to_build` - `optional` `array[string]`, only refresh the special partitions.
- `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)

  - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
> [!NOTE]
> :

  - If the loaded table already exists in the system, it will be reloaded
  - The `partition_col` in the parameter `options` is temporarily **required**. If the interface for setting the partition column has been called before, the correct parameter value must also be filled here
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example

```sh
curl -X PUT \ 
  'http://host:port/kylin/api/snapshots' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"gc_test",  "tables": ["SSB.P_LINEORDER",  "DEFAULT.TEST_KYLIN_FACT"],"options":{"DEFAULT.TEST_KYLIN_FACT":{"partition_col":"CAL_DT","incremental_build":true,"partitions_to_build":["2012-03-01","2012-03-04"]}}}' 
```

- Curl Response Example

```json
{"code": "000","data": {"jobs": [{"job_name": "SNAPSHOT_REFRESH","job_id": "65b3b0a4-d4d2-4a5b-af29-b190ca420543" },  {"job_name": "SNAPSHOT_REFRESH","job_id": "24aafb93-1cde-43d1-a627-8cd592f51cfe" }] },"msg": ""}
```

- `DELETE http://host:port/kylin/api/snapshots`
- Request Permission: OPERATION permission and above
- Introduced in: 5.0
- URL Parameters
  - `project` - `required` `string`, project name.
  - `tables` - `required` `array[string]`, snapshot tables to be deleted, for example：DB.TABLE, multiple tables are splitted by comma. Because the http protocol has a limit on the size of the request header, it is recommended that the length of url is less than 100.
- HTTP Header
  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example

```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/snapshots?project=gc_test&tables=SSB.P_LINEORDER%2CDEFAULT.TEST_KYLIN_FACT' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example

```json
{"code":"000","data": {"affected_jobs":[{"database": "DEFAULT","table": "KYLIN_CAL","job_id": "e3aa809b-5e73-42a5-a1e1-649d53b16e2c" },{"database": "DEFAULT","table": "P_LINEORDER","job_id": "e3aa809b-5e73-42a5-a1e1-649d53b16e2b"}] },"msg":""}
```

- `GET http://host:port/kylin/api/snapshots`
- Request Permission: QUERY permission and above
- Introduced in: 5.0
- URL Parameters

  - `project` - `required` `string`, project name.
  - `table` - `optional` `string`, search key word. Default value is an empty string, will display all the snapshots.
  - `page_offset` -`optional` `int`, offset of returned result, `0` by default.
  - `page_size` -`optional` `int`, quantity of returned result per page, `10` by default.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example

```sh
curl -X GET \ 
  'http://host:port/kylin/api/snapshots?project=gc_test' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example

```json
{"code":"000","data":{"value":[{"table":"P_LINEORDER","database":"SSB","usage": 5,"storage": 8555,"fact_table_count": 2 "lookup_table_count": 2,"last_modified_time": 1602315332279,"status": "REFRESHING" },Object{...},Object{...},Object{...} ],"offset":0,"limit":10,"total_size":4 },"msg":""}
```

---

<a id="restapi-query_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/query_api/ -->

<!-- page_index: 129 -->

# Query

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- `POST http://host:port/kylin/api/query`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `sql` - `required` `string`, SQL statement
  - `project` - `required` `string`, project name
  - `offset` - `optional` `int`, offset of query result. Must be used in conjunction with `limit`.
  - `limit` - `optional` `int`, limit on the quantity of returned query result
  - `forcedToPushDown` - `optional` `boolean`, whether to force queries to pushdown engine, `false` by default. You are not able to force queries to pushdown when the pushdown setting is turned off.
  - `partialMatchIndex` - `optional` `boolean`, `false` by default, whether to force queries the segments with proper index, when not all segment can answer the query
  - `forced_to_index` - `optional` `boolean`, whether to force the query to use index, default to `false`. When set to `true`, the query will return the result as normal if a matching index is found, otherwise, an error will be thrown and the query will not be pushded down.
  - `forcedToTieredStorage` - `optional` `int`, whether the query is forced to use tiered storage, the default value is `0`, which means that when the tiered storage cannot answer, it will be answered by the base table index on HDFS, configured as `1` indicates that when the tiered storage cannot answer the query, the query will be pushdown, configured as `2`, indicates that the query fails when the tiered storage cannot answer the query. When `forcedToPushDown` is `true`, this parameter doesn't take effect. When `forced_to_index` is `true`, this value `1` doesn't take effect.
  - Parameters `forcedToPushDown` and `forced_to_index` cannot be `true` at the same time, an error will be reported.
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/query' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ "sql":"select count(*) from SSB.P_LINEORDER", "project":"ssb", "partialMatchIndex":"true"}' 
```

- Response Example


```json
{"code":"000","data":{"columnMetas":[{"isNullable":0,"displaySize":19,"label":"EXPR$0","name":"EXPR$0","schemaName":null,"catelogName":null,"tableName":null,"precision":19,"scale":0,"columnType":-5,"columnTypeName":"BIGINT NOT NULL","caseSensitive":false,"autoIncrement":false,"currency":false,"definitelyWritable":false,"signed":true,"writable":false,"searchable":false,"readOnly":false} ],"results":[["60175"] ],"affectedRowCount":0,"exceptionMessage":null,"duration":129,"scanRows":[2519 ],"totalScanRows":2519,"scanBytes":[6118 ],"totalScanBytes":6118,"resultRowCount":1,"shufflePartitions":1,"hitExceptionCache":false,"storageCacheUsed":false,"queryStatistics":null,"traceUrl":null,"queryId":"738fad53-57a9-43fc-a186-b25d0993dfcb","server":"client134.kcluster:7470","suite":null,"signature":"1593670148521;1592230756490_1595228217256_1595228217256_1595228217256_1595228217257","engineType":"NATIVE","exception":false,"prepare":false,"timeout":false,"partial":false,"isException":false,"appMasterURL":"/kylin/sparder/SQL/execution/?id=27391","pushDown":false,"is_prepare":false,"is_timeout":false,"realizations":[{"modelId":"c7a7a1d0-71c6-4d42-bbc3-76167e5d2d10","modelAlias":"ssb_cube","layoutId":80001,"indexType":"Agg Index","valid":true,"partialMatchModel":false} ],"traces" : [{"name": "GET_ACL_INFO","group": "PREPARATION","duration": 10 },{"name" : "SQL_TRANSFORMATION","group" : "PREPARATION","duration" : 3 },{"name" : "SQL_PARSE_AND_OPTIMIZE","group" : "PREPARATION","duration" : 9 },{"name" : "MODEL_MATCHING","group" : "PREPARATION","duration" : 2 },{"name" : "PREPARE_AND_SUBMIT_JOB","group" : null,"duration" : 64 },{"name" : "WAIT_FOR_EXECUTION","group" : null,"duration" : 2 },{"name" : "EXECUTION","group" : null,"duration" : 26 },{"name" : "FETCH_RESULT","group" : null,"duration" : 7 }] },"msg":""}
```

- Response Information

  - `columnMetas` - metadata information of the columns
  - `results` - query results
  - `resultRowCount` - row count of query results
  - `isException` - whether the query returns exception
  - `exceptionMessage` - exception message
  - `queryId` - query ID
  - `duration` - query duration
  - `totalScanRows` - total scan count
  - `totalScanBytes` - total scan bytes
  - `hitExceptionCache` - whether hit the result cache of an exception query
  - `storageCacheUsed` - whether hit the result cache of a success query
  - `server` - which server executed this query
  - `timeout` - whether query is timeout
  - `pushDown` - whether query push down to other engine
  - `traces` - the trace information for each query execution stage
    - `name` - the stage name
    - `duration` - duration in milliseconds
    - `group` - the stage group

Calling this API will refresh the table cache of the Spark SQL Context for all query nodes. Application scenario: Query pushdown fails after the update of data source table.

- `PUT http://host:port/kylin/api/tables/catalog_cache`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `tables` - `required` `string`,specify the table you want to load, in the format: DB.TABLE, separate multiple tables with commas
- Curl Request Example


```sh
curl -X PUT \ 
  'http://host:port/kylin/api/tables/catalog_cache' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"tables":["SSB.LINEORDER","SSB.SUPPLIER"]}' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "nodes": [ 
            { 
                "server": "slave104.tnt:18001", 
                "refreshed": [ 
                    "SSB.LINEORDER", 
                    "SSB.SUPPLIER" 
                ], 
                "failed": [] 
            }, 
            { 
                "server": "slave104.tnt:18003", 
                "refreshed": [ 
                    "SSB.LINEORDER", 
                    "SSB.SUPPLIER" 
                ], 
                "failed": [] 
            } 
        ] 
    }, 
    "msg": "" 
} 
```

- Response Information

  - `nodes` - Refresh results of different nodes
  - `server` - Node information
  - `refreshed` - Table that refreshed successfully
  - `failed` - Table that failed to refresh
  - `msg` - Reasons for refresh failure

- `GET http://host:port/kylin/api/query/query_histories`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- URL Parameters

  - `project` - `required` `string`，project name
  - `page_offset` - `optional` `int`, offset of returned result, 0 by default
  - `page_size` - `optional` `int`, quantity of returned result per page, 10 by default
  - `start_time_from` - `optional` `string`，timestamp of query history start, cannot be used alone with start\_time\_to
  - `start_time_to` - `optional` `string`，timestamp of query history end, cannot be used alone with start\_time\_from
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/query/query_histories?project=kylin_demo&page_offset=5&page_size=1&start_time_from=1656864000000&start_time_to=1656950400000' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example

```json
{"code": "000","data": {"size": 79,"query_histories": [{"queryRealizations": null,"query_id": "4bfbc8f1-ffcb-ae86-c5f1-2b78c73cb802","query_history_info": {"exactly_match": true,"scan_segment_num": 1,"state": "FAILED","execution_error": false,"error_msg": null,"query_snapshots": [],"realization_metrics": [{"queryId": "4bfbc8f1-ffcb-ae86-c5f1-2b78c73cb802","duration": 568,"layoutId": "1","indexType": "Agg Index","modelId": "118ae12b-5198-ade2-ecd9-b7e5f64318a2","queryTime": 1656914360898,"projectName": "kylin_demo","snapshots": [],"secondStorage": false,"streamingLayout": false },{"queryId": "4bfbc8f1-ffcb-ae86-c5f1-2b78c73cb802","duration": 568,"layoutId": "1","indexType": "Agg Index","modelId": "6cf4a660-e217-add5-87f4-04493c8df21e","queryTime": 1656914360898,"projectName": "kylin_demo","snapshots": [],"secondStorage": false,"streamingLayout": false} ],"traces": [{"name": "HTTP_RECEPTION","group": null,"duration": 29 },{"name": "GET_ACL_INFO","group": "PREPARATION","duration": 1 },{"name": "SQL_TRANSFORMATION","group": "PREPARATION","duration": 12 },{"name": "SQL_PARSE_AND_OPTIMIZE","group": "PREPARATION","duration": 125 },{"name": "MODEL_MATCHING","group": "PREPARATION","duration": 10 },{"name": "PREPARE_AND_SUBMIT_JOB","group": "JOB_EXECUTION","duration": 277 },{"name": "WAIT_FOR_EXECUTION","group": "JOB_EXECUTION","duration": 13 },{"name": "EXECUTION","group": "JOB_EXECUTION","duration": 90 },{"name": "FETCH_RESULT","group": "JOB_EXECUTION","duration": 11} ],"cache_type": null,"query_msg": null },"sql_text": "SELECT *\nFROM\n  (SELECT PICKUP_DATE,\n          TAXI_ORDER_NUMBER,\n          PEOPLE_POSITIVE_NEW_CASES_COUNT,\n          round(TAXI_ORDER_NUMBER / PEOPLE_POSITIVE_NEW_CASES_COUNT, 2) AS COVID_IMPACT_INDEX\n   FROM\n     (SELECT PICKUP_DATE,\n             MONTH_START,\n             ZONE,\n             TAXI_ORDER_NUMBER\n      FROM\n        (SELECT PICKUP_DATE,\n                MONTH_START,\n                ZONE,\n                sum(TOTAL_AMOUNT) AS TAXI_PRICE_AMOUNT ,\n                count(TOTAL_AMOUNT) AS TAXI_ORDER_NUMBER\n         FROM\n           (SELECT PICKUP_DATE,\n                   MONTH_START,\n                   ZONE,\n                   TOTAL_AMOUNT,\n                   trip_distance\n            FROM KYLIN_DEMO.TAXI_TRIP_RECORDS_VIEW t_f\n            LEFT JOIN KYLIN_DEMO.NEWYORK_ZONE t_z ON t_f.PULOCATIONID = t_z.LOCATIONID\n            LEFT JOIN KYLIN_DEMO.LOOKUP_CALENDAR t_c ON t_f.PICKUP_DATE = t_c.DAY_START) t_merge\n         GROUP BY PICKUP_DATE,\n                  MONTH_START,\n                  ZONE)\n      WHERE ZONE = 'East New York') t_l\n   LEFT JOIN\n     (SELECT REPORT_DATE,\n             MONTH_START,\n             PROVINCE_STATE_NAME,\n             PEOPLE_POSITIVE_NEW_CASES_COUNT\n      FROM\n        (SELECT REPORT_DATE,\n                MONTH_START,\n                PROVINCE_STATE_NAME,\n                sum(PEOPLE_POSITIVE_NEW_CASES_COUNT) AS PEOPLE_POSITIVE_NEW_CASES_COUNT\n         FROM KYLIN_DEMO.COVID_19_ACTIVITY t_f\n         LEFT JOIN KYLIN_DEMO.LOOKUP_CALENDAR t_c ON t_f.REPORT_DATE = t_c.DAY_START\n         GROUP BY REPORT_DATE,\n                  MONTH_START,\n                  PROVINCE_STATE_NAME)\n      WHERE PROVINCE_STATE_NAME = 'New York') t_r ON t_l.PICKUP_DATE=t_r.REPORT_DATE) tt\nWHERE PICKUP_DATE >= '2020-01-01'\n  AND PICKUP_DATE <= '2020-12-31'\nLIMIT 50000","query_time": 1656914360898,"duration": 568,"server": "snoopy-gw07.kylin.com:7095","submitter": "ADMIN","index_hit": true,"query_status": "SUCCEEDED","result_row_count": 366,"id": 296,"engine_type": "NATIVE","total_scan_count": 122839,"project_name": "kylin_demo","realizations": [{"modelId": "118ae12b-5198-ade2-ecd9-b7e5f64318a2","modelAlias": "AUTO_MODEL_TAXI_TRIP_RECORDS_VIEW_1","layoutId": 1,"indexType": "Agg Index","snapshots": [],"valid": true,"partialMatchModel": false },{"modelId": "6cf4a660-e217-add5-87f4-04493c8df21e","modelAlias": "AUTO_MODEL_COVID_19_ACTIVITY_1","layoutId": 1,"indexType": "Agg Index","snapshots": [],"valid": true,"partialMatchModel": false} ],"total_scan_bytes": 849962,"error_type": null,"cache_hit": false}] },"msg": ""}
```

- Response Information
  - `query_id` - query ID
  - `query_history_info` - Query history infomation
    - `exactly_match` - whether the query returns exception
    - `scan_segment_num` - scan segments
    - `state` - the flag whether the query satisfied query recommendation
    - `execution_error` - whether the query failed
    - `error_msg` - error message
    - `query_snapshots` - query snapshots
    - `realization_metrics`
      - `queryId` - query ID
      - `duration` - query duration(ms)
      - `layoutId` - index ID
      - `indexType` - index type
      - `modelId` - model ID
      - `queryTime` - timestamp of when query executed
      - `projectName` - project name
      - `snapshots` - snapshots
      - `secondStorage` - whether Tied Storage was used
      - `streamingLayout` - whether hit streaming index
    - `traces`
      - `name` - the stage name
      - `duration` - duration in milliseconds
      - `group` - the stage group
    - `cache_type` - cache type
    - `query_msg` - exception message
    - `sql_text` - SQL
    - `query_time` - timestamp of when query executed
    - `duration` - duration in milliseconds
    - `server` - which server executed this query
    - `submitter` - username
    - `index_hit` - whether the query hit index
    - `query_status` - query status
    - `result_row_count` - row count of query results
    - `engine_type` - engine type
    - `total_scan_count` - total scan counts
    - `project_name` - project name
    - `realizations`
      - `modelId` - model ID
      - `modelAlias` - model name
      - `layoutId` - index ID
      - `indexType` - index type
      - `snapshots` - snapshots
      - `valid` - whether the model is valid
      - `partialMatchModel` - whether using partial match
      - `total_scan_bytes` - total scan bytes
      - `error_type` - error type
      - `cache_hit` - whether hit cache

- `GET http://host:port/kylin/api/query/download_query_histories`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- URL Parameters

  - `project` - `required` `string`, project name.
  - `timezone_offset_hour` - `required` `int`, query the time zone offset of history, the number of hours different from GMT, for example, East 8 is passed in 8, note that only the integer between [-18,18] can be taken.
  - `start_time_from` - `optional` `string`, query history start time timestamp, units ms, it work only when used together with start\_time\_to. For example, 1617206400000, if you enter a number other than a number, it will return empty.
  - `start_time_to` - `optional` `string`, query the end of history timestamp, units ms, it work only when used together with start\_time\_from. For example, 1620662400000, if you enter a number other than a number, it will return to null.
  - `latency_from` - `optional` `string`, query delay is greater than latency\_from, units s, it work only when used together with latency\_to. For example, 10, if you enter a number other than a number, it will return to null.
  - `latency_to` - `optional` `string`, query delay is less than latency\_to, units s, it work only when used together with latency\_from. For example, 20, if you enter a number other than a number, it will return to null.
  - `query_status` - `optional` `List<String>` query status, such as SUCCEEDED、FAILED. If you enter values other than these, it will return empty.
  - `sql` - `optional` `string`, used to fuzzy match user SQL or query ID.
  - `realization` - `optional` `List<string>` to query object.
  - `server` - `optional` `string`, the hostname and port of query node, e.g. myhost:7072 .
  - `submitter` - `optional` `List<string>` to query user.
- Example of curl request


```text
curl -X GET \ 
' http://host:port/kylin/api/query/download_query_histories?timezone_offset_hour=8&realization=&query_status=&submitter=&project=default&start_time_from=&start_time_to=&latency_from=&latency_to=&sql=' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-o query_history.csv 
```

- `GET http://host:port/kylin/api/query/download_query_histories_sql`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- URL Parameters

  - `project` - `required` `string`, project name
  - `start_time_from` - `optional` `string`, query history start time timestamp, units ms, it work only when used together with start\_time\_to. For example, 1617206400000, if you enter a number other than a number, it will return empty.
  - `start_time_to` - `optional` `string`, query the end of history timestamp, units ms, it work only when used together with start\_time\_from. For example, 1620662400000, if you enter a number other than a number, it will return to null.
  - `latency_from` - `optional` `string`, query delay is greater than latency\_from, units s, it work only when used together with latency\_to. For example, 10, if you enter a number other than a number, it will return to null.
  - `latency_to` - `optional` `string`, query delay is less than latency\_to, units s, it work only when used together with latency\_from. For example, 20, if you enter a number other than a number, it will return to null.
  - `query_status` - `optional` `List<string>` query status, such as succeeded and failed. If you enter values other than these, it will return null.
  - `sql` - `optional` `string`, used to fuzzy match user SQL or query ID.
  - `realization` - `optional` `List<string>` to query the object.
  - `server` - `optional` `string`, query node.
  - `submitter` - `optional` `List<string>` to query the user.
- Example of curl request


```text
curl -X GET \ 
' http://host:port/kylin/api/query/download_query_histories_sql?timezone_offset_hour=8&realization=&query_status=&submitter=&project=default&start_time_from=&start_time_to=&latency_from=&latency_to=&sql=' \ 
-H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
-H 'Accept-Language: en' \ 
-H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
-H 'Content-Type: application/json;charset=utf-8' \ 
-o query_history.sql 
```

---

<a id="restapi-data_source_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/data_source_api/ -->

<!-- page_index: 130 -->

# Data Source

Version: 5.0.2

> Reminder:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

> Call this API to load Hive table metadata to Kylin. By default, when a new Hive table is added, the table metadata will not be loaded to Kylin.

- `POST http://host:port/kylin/api/tables`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name
  - `need_sampling` - `required` `boolean`, whether to enable table sampling
  - `sampling_rows` - `optional` `integer`, indicates the max number of sampling rows and the range is [10,000 - 20,000,000] .

    > Note: if you enable need\_sampling, this parameter will be required.
  - `databases` - `optional` `[string]`, load all the tables under this database
  - `tables` - `optional` `[string]`, load tables with the format `DB.TABLE`

    **Note:**

    - If the loaded table already exists in the system, it will be reloaded.
    - The above two parameters `databases` and `tables` cannot be empty at the same time, which means you must use one of them to load tables.
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/tables' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"ssb","tables":["SSB.LINEORDER"],"need_sampling":false}' 
```

- Response Details

  - `loaded`, successfully loaded tables
  - `failed`, failed to load tables
- Response Example


```json
{"code": "000","data": {"loaded":["SSB.LINEORDER"],"failed":[] },"msg": ""}
```

> Call this API to compare the Hive table metadata in Kylin and that in the data source. For Hive table already loaded to Kylin and already used in model and index building, if some columns are deleted, Kylin will return a failure when reading these columns. Use this API to find the metadata differences and evaluate whether to update the metadata in Kylin by reloading the Hive table.

- `GET http://host:port/kylin/api/tables/pre_reload`
- Introduced in: 5.0
- URL Parameters

  - `project` - `required` `string`，project name
  - `table` - `required` `string`， reload table with the format `DB.TABLE`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/tables/pre_reload?project=ssb&table=SSB.LINEORDER' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Details
- `has_datasource_changed`, source table structure has changed

  - `has_effected_jobs`, has unfinished jobs related to the table
  - `has_duplicated_columns`, has duplicated columns
  - `add_column_count`, number of new columns
  - `remove_column_count`, number of reduce columns
  - `data_type_change_column_count`, number of column type changes
  - `broken_model_count`, number of broken models
  - `remove_measures_count`, number of impact measures
  - `remove_dimensions_count`, number of dimensions affected
  - `remove_layouts_count`, number of deleted indexes
  - `add_layouts_count`, increased number of indexes
  - `refresh_layouts_count`, number of indexes refreshed
  - `snapshot_deleted`, snapshot is deleted
  - `duplicated_columns`, duplicate column whose format is database.table.column
  - `effected_jobs`，effected Job ID
- Response Example


```json
{ 
    "code": "000", 
    "data": { 
      "has_datasource_changed": false, 
      "has_effected_jobs": true, 
      "has_duplicated_columns": true, 
      "add_column_count": 0, 
      "remove_column_count": 0, 
      "data_type_change_column_count": 0, 
      "broken_model_count": 0, 
      "remove_measures_count": 0, 
      "remove_dimensions_count": 0, 
      "remove_layouts_count": 0, 
      "add_layouts_count": 0, 
      "refresh_layouts_count": 0, 
      "snapshot_deleted": true, 
      "dumplicated_columns": ["SSB.LINEORDER.PROFIT", "SSB.LINEORDER.LO_DISCOUNT"], 
      "effected_jobs": ["266c9086-7ffe-44a1-9d5e-f9f9941b891d", "f42e5dd3-78e6-43f8-9bcb-edcb2c09312d"]  
    }, 
    "msg": "" 
} 
```

- `POST http://host:port/kylin/api/tables/reload`
- Request Permission: MANAGEMENT permission and above
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name
  - `table` - `required` `string`, specify the table, format：DB.TABLE
  - `need_sampling` - `required` `boolean`, whether to enable table sampling
  - `sampling_rows` - `optional` `integer`, indicates the max number of sampling rows and the range is [10,000 - 20,000,000]

    > Note: if you enable need\_sampling, this parameter will be required
  - `need_building` - `optional` `boolean`, whether to build a new index, `true` means to build, `false` means not to build, default value is `false`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/tables/reload' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"ssb","table":"SSB.LINEORDER","need_sampling":false,"need_building":false}' 
```

- Response Field

  - `sampling_id`, ids of table sampling jobs
  - `job_ids`, ids of the building jobs
- Response Example


```json
{"code": "000","data": {"sampling_id":"","job_ids":["1234","1234"] },"msg": ""}
```

> Call this API to evaluate the risks of unloading Hive table metadata. There are cases where you need to offline some Hive tables from Kylin. Use this API to evaluate the impact of unloading Hive table metadata on related Kylin models and jobs.

- `GET http://host:port/kylin/api/tables/{database}/{table}/prepare_unload`
- URL Parameters

  - `database` - `required` `string`，database name of the table to be deleted
  - `table` - `required` `string`，table name to be deleted
  - `project` - `required` `string`，project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/tables/SSB/LINEORDER/prepare_unload?project=ssb' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Field

  - `has_job`, whether there are running jobs of sampling or building snapshot in the current table
  - `has_model`, is the current table used by the model
  - `has_snapshot`, does the current table have a snapshot
  - `storage_size`, storage size of the current table snapshot (Byte)
  - `models`, model list
- Response Example


```json
{"code": "000","data": {"has_job": false,"has_model": true,"has_snapshot": true,"storage_size": 16616,"models": ["model"] },"msg": ""}
```

> Call this API to unload Hive table metadata from Kylin. After the API call, Hive table metadata will be unloaded from Kylin, and Kylin can no longer read the table data, or update the index data related to the table. It's recommended calling the "Prepare Unload Table" API before calling this API.

- `DELETE http://host:port/kylin/api/tables/{database}/{table}`
- URL Parameters

  - `database` - `required` `string`, database name of the table to be deleted
  - `table` - `required` `string`, table name to be deleted
  - `project` - `required` `string`, project name
  - `cascade` - `optional` `boolean`, delete all. default value is `false`

    - true: Delete this source table with the snapshot, attached Kafka/Hive table, the referenced models, and stop/delete related jobs.
    - false: Only delete this source table with the snapshot, and stop related jobs. While the referenced models will be kept (BROKEN, can be fixed by reloading the table).
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/tables/SSB/LINEORDER?project=ssb' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Field

  - `date`, deleted table name
- Response Example


```json
{ 
    "code": "000", 
    "data": "SSB.LINEORDER", 
    "msg": "" 
} 
```

> Call this API to enable data sampling to reflect the characteristics of Hive table data.

- `POST http://host:port/kylin/api/tables/sampling_jobs`
- Request Permission: MANAGEMENT permission and above
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name
  - `qualified_table_name` - `required` `string`,specify the table,format:DB.TABLE
  - `rows` - `required` `integer`, indicates the max number of sampling rows and the range is [10,000 - 20,000,000]
  - `priority` - `optional` `integer`, set job priority with range `0-4` which indicates the priority from high to low. Default value is `3`
  - `yarn_queue` - `optional` `string`, specify the YARN queue used by the job, it can be set after these two parameters were set: kylin.engine-yarn.queue.in.task.enabled (whether to allow set specified YARN queue for build task, default value is false), kylin.engine-yarn.queue.in.task.available (available YARN queues, separate them with English commas)
  - `tag` - `optional` `object`, job tag, if the field is set, when calling the [Get Job List](#restapi-job_api) API, the field will be the same back when returning the job. It can be used for system integration, mark the job and deal with it accordingly. By default, the maximum size of value is 1024 KB , which can be set by the configure kylin.job.tag-max-size=1024.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/tables/sampling_jobs' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{"project":"ssb","qualified_table_name":"SSB.LINEORDER","rows":20000,"priority":0}' 
```

- Response Example


```json
{ 
    "code":"000", 
    "data":"", 
    "msg":"" 
} 
```

> When a column is used as a partition column in a model in Kylin, get the partition format of the column.

- `GET http://host:port/kylin/api/tables/column_format`
- Request Permission: Operation permission and above
- Introduced in: 5.0
- Request Parameters

  - `project` - `required` `string`, project name
  - `table` - `required` `string`, table name, format as DB.TABLE
  - `column_name` - `required` `string`, column name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/tables/column_format?project=test&table=DEFAULT.KYLIN_SALES&column_name=PART_DT' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Field

  - `column_name` , column name
  - `column_format` , column format
- Response Example


```json
{"code": "000","data": {"partition_column": "PART_DT","format": "yyyy-MM-dd" },"msg": ""}
```

> Call this API to get the metadata of a specified Hive table.

- `GET http://host:port/kylin/api/tables`
- Request Permission: READ permission and above.
- Introduced in: 5.0
- Request Parameters

  - `project` - `required` `string`, project name
  - `database` - `optional` `string`, database name, case sensitive
  - `table` - `optional` `string`, table name, case sensitive
  - `is_fuzzy` - `optional` `boolean`, whether to enable fuzzy matching for table names, `true` means to enable, `false` means to close, default value is `false`
  - `ext` - `optional` `boolean`, specify whether the table's extension information is returned, `true` means to enable, `false` means to close, default value is `true`
  - `page_offset` - `optional` `int`, offset of returned result, `0` by default
  - `page_size` - `optional` `int`, quantity of returned result per page, `10` by default
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/tables?project=test&database=SSB&table=KYLIN_SALES' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "value": [ 
            { 
                "uuid": "6e638305-1a44-42dc-a161-5e06338dcb14", 
                "last_modified": 1600335525521, 
                "create_time": 1600335525522, 
                "version": "4.0.0.0", 
                "mvcc": 0, 
                "name": "KYLIN_SALES", 
                "columns": [ 
                    { 
                        "id": "1", 
                        "name": "TRANS_ID", 
                        "datatype": "bigint", 
                        "cardinality": null, 
                        "min_value": null, 
                        "max_value": null, 
                        "null_count": null 
                    } 
                ], 
                "source_type": 9, 
                "kafka_bootstrap_servers": null, 
                "subscribe": null, 
                "starting_offsets": null, 
                "table_type": "MANAGED", 
                "top": false, 
                "increment_loading": false, 
                "last_snapshot_path": null, 
                "database": "DEFAULT", 
                "exd": { 
                    "owner": "root", 
                    "create_time": "1524213799000", 
                    "total_file_size": "0", 
                    "hive_inputFormat": "org.apache.hadoop.mapred.TextInputFormat", 
                    "hive_outputFormat": "org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat", 
                    "location": "hdfs://sandbox.hortonworks.com:8020/apps/hive/warehouse/kylin_sales", 
                    "partition_column": "", 
                    "total_file_number": "0", 
                    "last_access_time": "0" 
                }, 
                "root_fact": false, 
                "lookup": false, 
                "primary_key": [], 
                "foreign_key": [], 
                "partitioned_column": null, 
                "partitioned_column_format": null, 
                "segment_range": null, 
                "storage_size": -1, 
                "total_records": 0, 
                "sampling_rows": [], 
                "last_build_job_id": null 
            } 
        ], 
        "offset": 0, 
        "limit": 10, 
        "total_size": 3 
    }, 
    "msg": "" 
} 
```

> Note: the `total_size` value is adjusted to the total number of all loaded tables in the project and no longer correlates to the actual table permissions the requesting user has in the project.

---

<a id="restapi-custom_jar_manager_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/custom_jar_manager_api/ -->

<!-- page_index: 131 -->

# Custom Parser Jar Management

Version: 5.0.2

> Reminder:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- [Load Jar](#restapi-custom_jar_manager_api--load-jar)
- [Delete Jar](#restapi-custom_jar_manager_api--delete-jar)
- [Get Parser List](#restapi-custom_jar_manager_api--get-parser-list)
- [Delete Parser](#restapi-custom_jar_manager_api--delete-parser)

- `POST http://host:port/kylin/api/custom/jar`
- HTTP Body: form-data

  - `project` - `required` `string`, project name
  - `file` - `required` `File`, jar file needs to be loaded
  - `jar_type` - `required` `string`, jar file type

    > Note: jar\_type is only "STREAMING\_CUSTOM\_PARSER" for the parser.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: multipart/form-data`
- Curl Request Example


```sh
  curl -X POST \ 
    'http://host:port/kylin/api/custom/jar' \ 
    -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
    -H 'Accept-Language: en' \ 
    -H 'Content-Type: multipart/form-data' \ 
    -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
    -F 'file=@"/**/**/custom_parser.jar"' \ 
    -F 'project="TestProject"' \ 
    -F 'jar_type="STREAMING_CUSTOM_PARSER"' 
```

- Response Details

  - `data`, Successfully loaded parser full path array
- Response Example


```json
{"code": "000","data": ["org.apache.kylin.parser.JsonDataParser1","org.apache.kylin.parser.JsonDataParser2" ],"msg": ""}
```

- `DELETE http://host:port/kylin/api/custom/jar`
- URL Parameters

  - `project` - `required` `string`, project name
  - `jar_name` - `required` `string`, The file name of the JAR to delete
  - `jar_type` - `required` `string`, jar file type

    > Note: jar\_type is only "STREAMING\_CUSTOM\_PARSER" for the parser.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
  curl -X DELETE \ 
    'http://host:port/kylin/api/custom/jar?project=TestProject&jar_name=custom_parser1.jar&jar_type="STREAMING_CUSTOM_PARSER' \ 
    -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
    -H 'Accept-Language: en' \ 
    -H 'Content-Type: application/json;charset=utf-8' \ 
    -H 'Authorization: Basic QURNSU46S1lMSU4=' 
```

- Response Details

  - `data`, Jar file name successfully deleted
- Response Example


```json
  { 
      "code": "000", 
      "data": "custom_parser1.jar", 
      "msg": "" 
  } 
```

- `GET http://host:port/kylin/api/kafka/parsers`
- URL Parameters

  - `project` - `必选` `string`, project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
  curl -X GET \ 
    'http://host:port/kylin/api/kafka/parsers?project=TestProject' \ 
    -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
    -H 'Accept-Language: en' \ 
    -H 'Content-Type: application/json;charset=utf-8' \ 
    -H 'Authorization: Basic QURNSU46S1lMSU4=' 
```

- Response Details

  - `data`, Loaded parser array
- Response Example


```json
{"code": "000","data": ["org.apache.kylin.parser.CsvDataParser2","org.apache.kylin.parser.JsonDataParser2","org.apache.kylin.parser.TimedJsonStreamParser" ],"msg": ""}
```

- `DELETE http://host:port/kylin/api/kafka/parser`
- URL Parameters

  - `project` - `必选` `string`, project name
  - `className` - `必选` `string`, The full path of the parser needs to be deleted
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
  curl -X DELETE \ 
    'http://host:port/kylin/api/kafka/parser?project=TestProject&className=org.apache.kylin.parser.JsonDataParser1' \ 
    -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
    -H 'Accept-Language: en' \ 
    -H 'Content-Type: application/json;charset=utf-8' \ 
    -H 'Authorization: Basic QURNSU46S1lMSU4=' 
```

- Response Details

  - `data`, Parser full path successfully deleted
- Response Example


```json
  { 
      "code": "000", 
      "data": "org.apache.kylin.parser.JsonDataParser1", 
      "msg": "" 
  } 
```

---

<a id="restapi-async_query_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/async_query_api/ -->

<!-- page_index: 132 -->

# Async Query

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.
> 3. In this chapter， all get requests and delete by ID request are forward compatible, that is, if the project parameter is not transferred to the URL, the request can also be successful if the project parameter is transferred to the request body.
> 4. Due to the requirements of the parquet format, the naming of the column can not contain characters such as ",; () \ n\ t =", so you need to display the definition alias in the SQL query, and the alias does not contain these special characters.
> 5. The earlier versions of hive do not support reading the parquet date type field, so you can replace the original table data type with timestamp, or upgrade hive to the versions after 1.2 .
> 6. In order to solve performance problem, we move the `include_header` parameter to Submit Async Query API, the `include_header` parameter in Download Query Result API doesn't work now.

- `POST http://host:port/kylin/api/async_query`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- HTTP Body: JSON Object

  - `sql` - `required` `string`, SQL statement
  - `separator` - `optional` `string`, separator of the exported result, which is `,` by default. Other separators such as `#`, `$`, `@`, `|` are also supported.
  - `offset` - `optional` `int`, offset of query result
  - `limit` - `optional` `int` , limit on the quantity of query result
  - `project` - `required` `string`, project name
  - `format` - `optional` `string`，file format, the default value is "csv", other optional values are "json", "xlsx", "parquet"
    > Note: When the file format is "xlsx" or "json", specifying the separator separator is not supported. When the file format is "parquet", it is currently not supported to download the result file through the [Download Query Result](#restapi-async_query_api--download-query-result) API, and can only be obtained directly from HDFS. File format "xlsx" may cause performance issue, therefore is not recommended.
  - `encode` - `optional` `string`，file encoding, the default value is "utf-8", other optional values are "gbk"
  - `file_name` - `optional` `string`，file name, Chinese is not supported temporarily, the default value is "result"
  - `spark_queue` - `optional` `string`, the cluster queue specified, the default value is "default". It will take effect after enabling `kylin.query.unique-async-query-yarn-queue-enabled`
  - `include_header` - `optional` `boolean`, whether the result includes header, the default value is `false`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/async_query' \ 
  -H 'Accept: application/vnd.apache.kylin-v4+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ "sql":"select * from KYLIN_SALES limit 100", "project":"learn_kylin" }' 
```

- Response Example


```json
{"code": "000","data": {"query_id": "eb3e837f-d826-4670-aac7-2b92fcd0c8fe","status": "RUNNING","info": "query still running" },"msg": ""}
```

- Response Information

  - `query_id` - Query ID of the Async Query
  - `status` - Status, ie., "SUCCESSFUL", "FAILED", "RUNNING"
  - `info` - Detailed information about the status

- `GET http://host:port/kylin/api/async_query/{query_id}/status?project=learn_kylin`
- URL Parameters

  - `query_id` - `required` `string`, Query ID of the Async Query
  - `project` `required` `string`, project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/async_query/{query_id}/status?project=learn_kylin' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{"code": "000","data": {"query_id": "eb3e837f-d826-4670-aac7-2b92fcd0c8fe","status": "SUCCESSFUL","info": "await fetching results" },"msg": ""}
```

- Response Information

  - `query_id` - Query ID of the Async Query
  - `status` - Status, ie., "SUCCESSFUL" , "RUNNING", "FAILED" and "MISSING"
  - `info` - Detailed information about the status

- `GET http://host:port/kylin/api/async_query/{query_id}/metadata?project=learn_kylin`
- URL Parameters

  - `query_id` - `required` `string`, Query ID of the Async Query
  - `project` `required` `string`, project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/async_query/{query_id}/metadata?project=learn_kylin' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": [ 
        [ 
            "TRANS_ID", 
            "PART_DT" 
        ], 
        [ 
            "BIGINT", 
            "DATE" 
        ] 
    ], 
    "msg": "" 
} 
```

- Response Information

  - `data` - data includes two list, the first list is the column name, and the second list is the corresponding data type of the column

- `GET http://host:port/kylin/api/async_query/{query_id}/file_status?project=learn_kylin`
- URL Parameters

  - `query_id` - `required` `string`, Query ID of the Async Query
  - `project` `required` `string`, project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/async_query/{query_id}/file_status?project=learn_kylin`' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": 7611, 
    "msg": "" 
} 
```

- Response Information

  - `data` - total size of the result

> Note: Please make sure the query status is "SUCCESSFUL" before calling this API.

- `GET http://host:port/kylin/api/async_query/{query_id}/result_download?include_header=true&project=learn_kylin`
- URL Parameters

  - `query_id` - `required` `string`, Query ID of the Async Query
  - `project` `required` `string`, project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/async_query/{query_id}/result_download?include_header=true&project=learn_kylin' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -o result.csv 
```

- Response Example

  - returns a document named `result.csv`.

- `GET http://host:port/kylin/api/async_query/{query_id}/result_path?project=learn_kylin`
- URL Parameters

  - `query_id` - `required` `string`, Query ID of the Async Query
  - `project` `required` `string`, project name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/async_query/{query_id}/result_path?project=learn_kylin' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "hdfs://host:8020/{kylin_working_dir}/{kylin_metadata_url}/{project}/async_query_result/{query_id}", 
    "msg": "" 
} 
```

- Response Information

  - `data` - the HDFS Path in which stores the result file

- `DELETE http://host:port/kylin/api/async_query`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/async_query' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": true, 
    "msg": "" 
} 
```

> Tip: This interface may delete queries that have not yet obtained results.

- `DELETE http://host:port/kylin/api/async_query?project={project}&older_than={time}`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- URL Parameters

  - `project`-`required` `string`, the query result file of which project needs to be deleted
  - `Older_than`-`required` `string`, the earliest retention time, the asynchronous query result file whose last\_modify is earlier than this time will be deleted, the time format is `yyyy-MM-dd HH:mm:ss`, no need to bring it quotation marks. Note: When using Curl request, it needs to perform url escaping by replacing spaces with `%20`.
- Curl request example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/async_query?project=learn_kylin&older_than=2021-04-26%2010:00:00' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response example


```json
{ 
    "code": "000", 
    "data": true, 
    "msg": "" 
} 
```

- Response information

  - `data`-Returns true if all old query result files are successfully deleted, otherwise false

- `DELETE http://host:port/kylin/api/async_query/{query_id}?project=learn_kylin`
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- URL Parameters

  - `query_id`-`required`  `string`, Query ID for asynchronous query
  - `project`-`required` `string`, project name
- Curl request example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/async_query/{query_id}?project=learn_kylin' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response example


```json
{ 
    "code": "000", 
    "data": true, 
    "msg": "" 
} 
```

- Response information

  - `data`-Return true if the query result file corresponding to `query_id` is successfully deleted, otherwise false

- When the column name contains a comma `,`, if the separator `separator` is specified, the comma `,` in the column name of the header of the download result table will be replaced by the separator.
- When column names contain separator, the file format may be parsed incorrectly.

---

<a id="restapi-job_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/job_api/ -->

<!-- page_index: 133 -->

# Job Management

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- [Get Job List](#restapi-job_api--get-job-list)
- [Operate Job](#restapi-job_api--operate-job)

- `GET http://host:port/kylin/api/jobs`
- URL Parameters

  - `time_filter` - `required` `int`

    ![](assets/images/job-api-053440202aa7f2b6d6f9cf9e8e7da806_0e09ba5a42532f56.png)
  - `project` - `optional` `string`, project name
  - `statuses` - `optional` `string`，job status，Optional values：`PENDING`,`RUNNING`,`FINISHED`,`ERROR`,`DISCARDED`,`STOPPED`,Separate multiple values with commas
  - `page_offset` - `optional` `int`, offset of returned result, 0 by default
  - `page_size` - `optional` `int`, quantity of returned result per page, 10 by default
  - `sort_by` - `optional` `string`, sort field, optional values：`last_modified` by default, `project id`,`job_name`,`target_subject`,`create_time`,`total_duration`
  - `reverse` - `optional` `boolean`, whether sort reverse, "true" by default
  - `key` - `optional` `string`, filter field, support job id or object name
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/jobs?time_filter=0&page_size=1' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code":"000", 
    "data":{ 
        "value":[ 
            { 
                "id":"232bf69f-6cdf-4dcc-a3aa-b6ca7651e98c", 
                "last_modified":0, 
                "duration":91020, 
                "exec_start_time":1577764731199, 
                "steps":null, 
                "job_status":"FINISHED", 
                "job_name":"INDEX_BUILD", 
                "data_range_start":0, 
                "data_range_end":9223372036854775807, 
                "target_model":"5b54898a-dd75-4146-abbe-de77c0cf77fb", 
                "target_segments":[ 
                    "3344c9bb-83fa-4128-803b-e18f27b0ccf8" 
                ], 
                "step_ratio":1, 
                "create_time":1577764730069, 
                "wait_time":1130, 
                "target_subject":"AUTO_MODEL_KYLIN_ACCOUNT_1", 
                "target_subject_error":false, 
                "project":"test", 
                "submitter":"ADMIN", 
                "exec_end_time":1577764822219, 
                "tag":"mark" 
            } 
        ], 
        "offset":0, 
        "limit":1, 
        "total_size":1364 
    }, 
    "msg":"" 
} 
```

- `PUT http://host:port/kylin/api/jobs/status`
- URL Parameters

  - `action` - `required` `string`, action types for jobs. Optional values are below:

    - `RESUME`, resume selected jobs from paused/error status
    - `DISCARD`, discard selected jobs
    - `PAUSE`, pause selected jobs
    - `RESTART`, restart selected jobs
  - `project` - `optional` `string`, project name. If only `project` is defined, it will operate all jobs under this project. Note: `project` and `job_ids` cannot be empty at the same time.
  - `job_ids` - `optional` `array<string>`, job id. If only `job_ids` is defined, it will operate all jobs with those ids. Note: `project` and `job_ids` cannot be empty at the same time.
  - - `statuses` - `optional` `array<string>`, filter jobs by statuses based on the filtering results of `project` and `job_ids`.
      - `PENDING`, pending jobs
      - `RUNNING`, running jobs
      - `FINISHED`, finished jobs
      - `ERROR`, error jobs
      - `DISCARDED`, discarded jobs
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
  'http://host:port/kylin/api/jobs/status' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
         "action" : "PAUSE", 
         "job_ids" : [ 
            "d7e4a098-10b6-4961-85b4-9eebfe29eb25", 
            "80f4d168-1074-4218-875c-4c70a4334029" 
         ], 
         "project" : "ssb" 
      }' 
```

- Response Example


```json
{ 
    "code":"000", 
    "data":"", 
    "msg":"" 
} 
```

---

<a id="restapi-acl_api-intro"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/acl_api/intro/ -->

<!-- page_index: 134 -->

# ACL Management

Version: 5.0.2

Kylin provides REST APIs on Access Control List Management to help users strictly manage the ACL on projects, tables, users, user group and so on.

---

<a id="restapi-acl_api-user_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/acl_api/user_api/ -->

<!-- page_index: 135 -->

# User Management

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- `GET http://host:port/kylin/api/user`
- Introduced in: 5.0
- Request Parameters

  - `name` - `optional` `string`, username.
  - `is_case_sensitive` - `optional` `boolean`, whether case sensitive on user name and `false` is by default.
  - `page_offset` - `optional` `int`, offset of returned result, 0 by default.
  - `page_size` - `optional` `int`, quantity of returned result per page, 10 by default.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/user' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "value": [ 
            { 
                "username": "test", 
                "authorities": [ 
                    { 
                        "authority": "ALL_USERS" 
                    } 
                  	... 
                ], 
                "disabled": false, 
                "default_password": false, 
                "locked": false, 
                "uuid": "af11440a-8e9d-4801-8508-5d0ce0e04a2f", 
                "last_modified": 1592296833935, 
                "create_time": 1592296833844, 
                "locked_time": 0, 
                "wrong_time": 0, 
                "first_login_failed_time": 0 
            } 
          	... 
        ], 
        "offset": 0, 
        "limit": 10, 
        "total_size": 3 
    }, 
    "msg": "" 
} 
```

- `POST http://host:port/kylin/api/user`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `username` - `required` `string`, username.
  - `password` - `required` `string`, password.
  - `disabled` - `required` `boolean`, enable the user or not, `true` means the user is disabled and `false` means the user is enabled.
  - `authorities` - `required` `array[string]`, the user belongs which user group.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/user' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
	"username": "test", 
	"password": "Password@123", 
	"disabled": "false", 
	"authorities":["ALL_USERS"] 
	}' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

**Note:** Modifying a user will overwrite the user group values.

- `PUT http://host:port/kylin/api/user`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `username` - `required` `string`, username.
  - `authorities` - `required` `array[string]`, the user belongs which user group.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
  'http://host:port/kylin/api/user' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
	"username": "createuser", 
	"authorities":["ALL_USERS"] 
	}' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- `PUT http://host:port/kylin/api/user/password`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `username` - `required` `string`, username.
  - `password` - `required` `string`, original password.
  - `new_password` - `required` `string`, new password.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
  'http://host:port/kylin/api/user' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
    "username": "test", 
    "password": "Password@123", 
    "new_password": "Password@1234" 
	}' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- `DELETE http://host:port/kylin/api/user`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `username` - `required` `string`, username.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/user' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
  -d '{ 
	"username": "testuser" 
	}' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- `GET http://host:port/kylin/api/access/acls`
- Introduced in: 5.0
- Request Parameters

  - `type` - `required` `string`, represents users or user groups, optional values are `user` or `group`.
  - `name` - `required` `string`, user or group name.
  - `project` - `optional` `string`, project name, fill in the value to get all the permissions of a user or user group in the specified project.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/access/acls?type=user&name=ADMIN' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": [ 
        { 
            "project_name": "test", 
            "project_permission": "ADMIN", 
            "acl_info": [ 
                { 
                    "tables": [ 
                        { 
                            "authorized": true, 
                            "columns": [ 
                                { 
                                    "authorized": true, 
                                    "column_name": "C_ADDRESS" 
                                } 
                              	... 
                            ], 
                            "rows": [], 
                            "table_name": "CUSTOMER", 
                            "authorized_column_num": 8, 
                            "total_column_num": 8 
                        } 
                      	... 
                    ], 
                    "authorized_table_num": 6, 
                    "total_table_num": 6, 
                    "database_name": "SSB" 
                } 
              	... 
            ] 
        } 
      	... 
    ], 
    "msg": "" 
} 
```

---

<a id="restapi-acl_api-user_group_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/acl_api/user_group_api/ -->

<!-- page_index: 136 -->

# User Group Management

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains `&` or other special chars.

- `GET http://host:port/kylin/api/user_group/groups`
- Introduced in: 5.0
- Request Parameters

  - `group_name` - `optional` `string`, group name.
  - `is_case_sensitive` - `optional` `boolean`, whether case-sensitive on user group name. The default value is  `false`.
  - `page_offset` - `optional` `int`, offset of returned result, 0 by default.
  - `page_size` - `optional` `int`, quantity of returned result per page, 10 by default.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/user_group/groups`' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{"code": "000","data": {"value": ["ALL_USERS","ROLE_ADMIN","ROLE_ANALYST","ROLE_MODELER" ...],"offset": 0,"limit": 10,"total_size": 7 },"msg": ""}
```

- `GET http://host:port/kylin/api/user_group/group_members/{group_name}`
- Introduced in: 5.0
- URL Parameters

  - `group_name` - `required` `string`, group name.
- Request Parameters

  - `username` - `optional` `string`, username.
  - `page_offset` - `optional` `int`, offset of returned result, 0 by default.
  - `page_size` - `optional` `int`, quantity of returned result per page, 10 by default.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/user_group/group_members/test' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "value": [ 
            { 
                "username": "ADMIN", 
                "authorities": [ 
                    { 
                        "authority": "ROLE_ADMIN" 
                    }, 
                    { 
                        "authority": "ALL_USERS" 
                    } 
                ], 
                "disabled": false, 
                "default_password": false, 
                "locked": false, 
                "uuid": "aaf02c5d-1605-42fa-abf9-9b0bb5715a6a", 
                "last_modified": 1592555313558, 
                "create_time": 1586744927779, 
                "locked_time": 0, 
                "wrong_time": 0, 
                "first_login_failed_time": 0 
            } 
          	... 
        ], 
        "offset": 0, 
        "limit": 10, 
        "total_size": 10 
    }, 
    "msg": "" 
} 
```

- `POST http://host:port/kylin/api/user_group`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `group_name` - `required` `string`, group name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/user_group' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
    "group_name": "test_group" 
	}' 
```

- Response Example


```json
{ 
    "code": "000",  
    "data": "",  
    "msg": "add user group" 
} 
```

**Note:** Updating group will overwrite the original user list.

- `PUT http://host:port/kylin/api/user_group/users`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `group_name` - `required` `string`, group name.
  - `users` - `required` `array[string]`, list of users in group.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
  'http://host:port/kylin/api/user_group/users' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
	"group_name": "test",  
	"users":["ANALYST",  "MODELER"] 
	}' 
```

- Response Example


```json
{ 
    "code": "000",  
    "data": "",  
    "msg": "modify users in user group" 
} 
```

- `DELETE http://host:port/kylin/api/user_group`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `group_name` - `required` `string`, group name.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
  'http://host:port/kylin/api/user_group' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
  -d '{ 
    "group_name": "test_group" 
	}' 
```

- Response Example


```json
{ 
    "code": "000",  
    "data": "",  
    "msg": "del user group" 
} 
```

---

<a id="restapi-acl_api-project_acl_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/acl_api/project_acl_api/ -->

<!-- page_index: 137 -->

# Project ACL

Version: 5.0.2

> Reminders:
>
> 1. Please read [Access and Authentication REST API](#restapi-authentication) and understand how authentication works.
> 2. On Curl command line, don't forget to quote the URL if it contains the special char `&`.

- `GET http://host:port/kylin/api/access/project`
- Introduced in: 5.0
- Request Parameters

  - `project` - `required` `string`, project name.
  - `name` - `optional` `string`, user or group name.
  - `page_offset` - `optional` `int`, offset of returned result, 0 by default.
  - `page_size` - `optional` `int`, quantity of returned result per page, 10 by default.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X GET \ 
  'http://host:port/kylin/api/access/project?project=learn_kylin' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": { 
        "value": [ 
            { 
                "type": "user", 
                "name": "ADMIN", 
                "permission": "ADMIN" 
            }, 
            { 
                "type": "group", 
                "name": "TEST_GROUP", 
                "permission": "QUERY" 
            } 
          	... 
        ], 
        "offset": 0, 
        "limit": 10, 
        "total_size": 4 
    }, 
    "msg": "" 
} 
```

- `POST http://host:port/kylin/api/access/project`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `type` - `required` `string`, represents users or user groups, optional values are `user` or `group`.
  - `permission` - `required` `string`, represents users or user groups permission, optional values are `QUERY`, `OPERATION`, `MANAGEMENT` and `ADMIN`.
  - `names` - `required` `array[string]`, name of user or user group.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X POST \ 
  'http://host:port/kylin/api/access/project' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
    "project": "Kylin", 
    "type": "user", 
    "permission": "QUERY", 
    "names":["test"] 
    }' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- `PUT http://host:port/kylin/api/access/project`
- Introduced in: 5.0
- HTTP Body: JSON Object

  - `project` - `required` `string`, project name.
  - `type` - `required` `string`, represents users or user groups, optional values are `user` or `group`.
  - `permission` - `required` `string`, represents users or user groups permission, optional values are `QUERY`, `OPERATION`, `MANAGEMENT` and `ADMIN`.
  - `name` - `required` `string`, name of user or user group.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X PUT \ 
   'http://host:port/kylin/api/access/project' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' \ 
  -d '{ 
    "project": "Kylin", 
    "type": "user", 
    "permission": "ADMIN", 
    "name": "test" 
    }' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

- `DELETE http://host:port/kylin/api/access/project`
- Introduced in: 5.0
- Request Parameters

  - `project` - `required` `string`, project name.
  - `type` - `required` `string`, Represents users or user groups, optional are `user` or `group`.
  - `name` - `required` `string`, name of user or user group.
- HTTP Header

  - `Accept: application/vnd.apache.kylin-v4-public+json`
  - `Accept-Language: en`
  - `Content-Type: application/json;charset=utf-8`
- Curl Request Example


```sh
curl -X DELETE \ 
   'http://host:port/kylin/api/access/project?project=learn_kylin&type=user&name=test' \ 
  -H 'Accept: application/vnd.apache.kylin-v4-public+json' \ 
  -H 'Accept-Language: en' \ 
  -H 'Authorization: Basic QURNSU46S1lMSU4=' \ 
  -H 'Content-Type: application/json;charset=utf-8' 
```

- Response Example


```json
{ 
    "code": "000", 
    "data": "", 
    "msg": "" 
} 
```

---

<a id="restapi-callback_api"></a>

<!-- source_url: https://kylin.apache.org/docs/restapi/callback_api/ -->

<!-- page_index: 138 -->

# Use callback API to monitor job status

Version: 5.0.2

The success returned by calling the required job API only indicates the job is successfully started. Kylin supports callback API to confirm the job execution state, it will return success if the job is successfully completed; it will return error if the job fails and also the error code to help troubleshooting.

Deploy an online service that accepts POST requests and add the configuration parameter `kylin.job.finished-notifier-url` to kylin.properties with the service URL as its parameter value.

Suppose the value of parameter `kylin.job.finished-notifier-url` is set to `http://127.0.0.1:7777`. When Kylin finishes the job, it will send the following message to `http://127.0.0.1:7777`.

**Header**

```sh
Content-Type: application/json 
Content-Length: 262 
Host: 127.0.0.1:7777 
Connection: Keep-Alive 
User-Agent: Apache-HttpClient/4.5.3 (Java/1.8.0_171) 
Accept-Encoding: gzip,deflate 
```

**Body**

```sh
{"job_id": "6044ac09-27bc-4968-a6b0-881c4c0abf89","project": "test","model_id": "91402da4-b991-4cd8-b164-7f62b9e91b69","segment_ids": ["9e5a89b9-00f1-4296-adc4-139113030e83","f26dcbc9-b786-4112-a4f6-94280bf10265","f3dc9864-0e1a-417b-a46d-3255e8cb6473" ],"index_ids": [20001,10001 ],"duration": 27699,"job_state": "ERROR","job_type": "INDEX_BUILD","segment_time_range": [{"segment_id": "9e5a89b9-00f1-4296-adc4-139113030e83","data_range_start": 1338480000000,"data_range_end": 1354291200000 },{"segment_id": "f26dcbc9-b786-4112-a4f6-94280bf10265","data_range_start": 1325347200000,"data_range_end": 1338480000000 },{"segment_id": "f3dc9864-0e1a-417b-a46d-3255e8cb6473","data_range_start": 1354291200000,"data_range_end": 1370016000000} ],"segment_partition_info": [{"segment_id": "9e5a89b9-00f1-4296-adc4-139113030e83","partition_info": [{"id": 0,"values": ["674"],"status": "ONLINE","last_modified_time": 1623390508821,"source_count": 34,"bytes_size": 1772 }, {"id": 1,"values": ["22"],"status": "ONLINE","last_modified_time": 1623390508821,"source_count": 30,"bytes_size": 1800 }] }],"snapshot_job_info":null,"err_code":"KE-060100201","msg":"KE-060100201: An Exception occurred outside Kylin.","suggestion":"Please check whether the external environment(other systems, components, etc.) is normal.","start_time":1656604800000,"end_time":1656608400000,"tag":null,"code":"999","stacktrace":"KE-060100201: An Exception occurred outside Kylin. org.apache...."}
```

- HTTP method: POST
- Content-Type: application/json
- URL Parameters
  - `project` - `string`, project name
  - `job_id - String`, job ID
  - `model_id` - `string`, model UUID
  - `segment_ids` - `list<string>`, segment UUID
  - `index_ids` - `list<string>`, index UUID
  - `duration` - `long`, build duration in milliseconds
  - `job_state` - `string`, job state when the job ends, value: `SUCCEED` if the job succeeds, `DISCARDED` if the job is discarded, `ERROR` if the job fails, or `PAUSED` if the job is paused
  - `job_type` - `string`，job type，including：`INDEX_BUILD`、`INDEX_REFRESH`、`INDEX_MERGE`、`INC_BUILD`、`SUB_PARTITION_BUILD`、`SUB_PARTITION_REFRESH`、`SNAPSHOT_BUILD`、`SNAPSHOT_REFRESH`
  - `segment_time_range` - `list`，segment time range
    - `segment_id` - `string`，segment UUID
    - `data_range_start` - `long`, timestamp in milliseconds, start time of segment build
    - `date_range_end` - `long`, timestamp in milliseconds, end time of segment build
  - `segment_partition_info` - `list`, information about segment under partition including:
    - `segment_id`:  `string`, segment UUID
    - `partition_info`: `list`, partition information
      - `id`: `long`, partition ID
      - `values`: `list<long>`, partition values
      - `status`: `string`, partition status, value:`ONLINE` if the partition is online,`LOADING` if the partition is being built, or `REFRESHING` if the partition is being refreshed
      - `last_modified_time`: `long`, timestamp in milliseconds, last modified time
      - `source_count`: `long`, number of rows
      - `bytes_size`: `long`, storage capacity
  - `snapshot_job_info` - `object`，information about snapshot job, including:
    - `table`：`string`，table name of the snapshot
    - `database`：`string`，database name of the snapshot
    - `total_rows`：`long`，total rows of the snapshot
    - `storage`： `long`，disk space of the snapshot
    - `last_modified_time`：timestamp, last time the snapshot was built
    - `status`：status of the snapshot, value: `ONLINE` and `OFFLINE`
    - `select_partition_col`：partition column of the snapshot, it takes effect only for incremental snapshots and `null` for full snapshots
  - `msg` - `string` , job error message
  - `error_code` - `string` , error code in Kylin
  - `suggestion` - `string`, suggestion on how to solve the issue
  - `start_time` - long, timestamp in milliseconds, the start time of the task
  - `end_time` - long, timestamp in milliseconds, the end time of the task
  - `tag` - string，customized tag, used for system integration
  - `code` - string，status code，value: `null` if job succeeds, `401` if unauthorized, `999` other unrecognized status
  - `stacktrace` - string，stack information of exceptions

- For a job in PAUSED or ERROR state, if the job is canceled directly, the job state will be changed to DISCARDED, but the job state change will not be reported via the callback API.
- If a job in PAUSED or ERROR state is rerun and then canceled when running, the job state change will be reported via the callback API.

---
