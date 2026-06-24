# Concepts

## Navigation

- [Previous Pinot Storage Model chevron-left](#concepts-pinot-storage-model)
- [Next Components chevron-right](#components)
- [Previous Concepts chevron-left](#concepts)
- [Next Architecture chevron-right](#concepts-architecture)
- hashtag Operator reference
  - [Cluster chevron-right](#components-cluster)
- [Controller chevron-right](#components-cluster-controller)
- [Broker chevron-right](#components-cluster-broker)
- [Server chevron-right](#components-cluster-server)
- [Minion chevron-right](#components-cluster-minion)
- [Tenant chevron-right](#components-cluster-tenant)
- hashtag Developer reference
  - [Table chevron-right](#components-table)
- [Schema chevron-right](#components-table-schema)
- [Segment chevron-right](#components-table-segment)
- [Previous Architecture chevron-left](#concepts-architecture)
- [Next Cluster chevron-right](#components-cluster)
- [Pinot Data Explorer](#components-exploring-pinot)
- [Concepts chevron-right](#concepts)
  - [Pinot Storage Model](#concepts-pinot-storage-model)
  - [Architecture](#concepts-architecture)
- [Components chevron-right](#components)
- Other pages
  - [Logical Table](#components-table-logical-table)
  - [Deep Store](#components-table-segment-deep-store)
  - [Segment Retention](#components-table-segment-segment-retention)
  - [Segment Threshold](#components-table-segment-segment-threshold)
  - [Time Boundary](#components-table-time-boundary)

## Content

<a id="concepts-pinot-storage-model"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/concepts/pinot-storage-model -->

<!-- page_index: 1 -->

# Pinot Storage Model

- [Table](#concepts-pinot-storage-model--table)
- [Segment](#concepts-pinot-storage-model--segment)
- [Tenant](#concepts-pinot-storage-model--tenant)
- [Cluster](#concepts-pinot-storage-model--cluster)
- [Physical architecture](#concepts-pinot-storage-model--physical-architecture)
- [Controller](#concepts-pinot-storage-model--controller)
- [Server](#concepts-pinot-storage-model--server)
- [Broker](#concepts-pinot-storage-model--broker)
- [Pinot minion](#concepts-pinot-storage-model--pinot-minion)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

---

<a id="components"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components -->

<!-- page_index: 2 -->

# Components

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

---

<a id="concepts"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/concepts -->

<!-- page_index: 3 -->

# Concepts

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

---

<a id="concepts-architecture"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/concepts/architecture -->

<!-- page_index: 4 -->

# Architecture

- [Distributed design principles](#concepts-architecture--distributed-design-principles)
- [Core components](#concepts-architecture--core-components)
- [Apache Helix and ZooKeeper](#concepts-architecture--apache-helix-and-zookeeper)
- [Controller](#concepts-architecture--controller)
- [Server](#concepts-architecture--server)
- [Minion](#concepts-architecture--minion)
- [Data ingestion overview](#concepts-architecture--data-ingestion-overview)
- [Offline (batch) ingest](#concepts-architecture--offline-batch-ingest)
- [Real-time ingest](#concepts-architecture--real-time-ingest)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
//This is an example ZNode config for EXTERNAL VIEW in Helix
{
  "id" : "baseballStats_OFFLINE",
  "simpleFields" : {
    ...
  },
  "mapFields" : {
    "baseballStats_OFFLINE_0" : {
      "Server_10.1.10.82_7000" : "ONLINE"
    }
  },
  ...
}
```

Copy

```
// Query: select count(*) from baseballStats limit 10

// RESPONSE
// ========
{
    "resultTable": {
        "dataSchema": {
            "columnDataTypes": ["LONG"],
            "columnNames": ["count(*)"]
        },
        "rows": [
            [97889]
        ]
    },
    "exceptions": [],
    "numServersQueried": 1,
    "numServersResponded": 1,
    "numSegmentsQueried": 1,
    "numSegmentsProcessed": 1,
    "numSegmentsMatched": 1,
    "numConsumingSegmentsQueried": 0,
    "numDocsScanned": 97889,
    "numEntriesScannedInFilter": 0,
    "numEntriesScannedPostFilter": 0,
    "numGroupsLimitReached": false,
    "totalDocs": 97889,
    "timeUsedMs": 5,
    "segmentStatistics": [],
    "traceInfo": {},
    "minConsumingFreshnessTimeMs": 0
}
```

---

<a id="components-cluster"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/cluster -->

<!-- page_index: 5 -->

# Cluster

- [Cluster configuration](#components-cluster--cluster-configuration)
- [Cluster components](#components-cluster--cluster-components)
- [Participant](#components-cluster--participant)
- [Controller](#components-cluster--controller)
- [Logical view](#components-cluster--logical-view)
- [Set up a Pinot cluster](#components-cluster--set-up-a-pinot-cluster)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

---

<a id="components-cluster-controller"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/cluster/controller -->

<!-- page_index: 6 -->

# Controller

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
curl -X GET "http://localhost:9000/periodictask/run?taskname=SegmentStatusChecker&tableName=jsontypetable&type=OFFLINE" -H "accept: application/json"

{
  "Log Request Id": "api-09630c07",
  "Controllers notified": true
}
```

Copy

```
docker run \
    --network=pinot-demo \
    --name pinot-controller \
    -p 9000:9000 \
    -d ${PINOT_IMAGE} StartController \
    -zkAddress pinot-zookeeper:2181
```

Copy

```
bin/pinot-admin.sh StartController \
  -zkAddress localhost:2181 \
  -clusterName PinotCluster \
  -controllerPort 9000
```

---

<a id="components-cluster-broker"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/cluster/broker -->

<!-- page_index: 7 -->

# Broker

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
docker run \
    --network=pinot-demo \
    --name pinot-broker \
    -d ${PINOT_IMAGE} StartBroker \
    -zkAddress pinot-zookeeper:2181
```

Copy

```
bin/pinot-admin.sh StartBroker \
  -zkAddress localhost:2181 \
  -clusterName PinotCluster \
  -brokerPort 7000
```

---

<a id="components-cluster-server"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/cluster/server -->

<!-- page_index: 8 -->

# Server

- [Offline](#components-cluster-server--offline)
- [Real-time](#components-cluster-server--real-time)
- [Starting a server](#components-cluster-server--starting-a-server)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
Usage: StartServer
	-serverHost               <String>                      : Host name for controller. (required=false)
	-serverPort               <int>                         : Port number to start the server at. (required=false)
	-serverAdminPort          <int>                         : Port number to serve the server admin API at. (required=false)
	-dataDir                  <string>                      : Path to directory containing data. (required=false)
	-segmentDir               <string>                      : Path to directory containing segments. (required=false)
	-zkAddress                <http>                        : Http address of Zookeeper. (required=false)
	-clusterName              <String>                      : Pinot cluster name. (required=false)
	-configFileName           <Config File Name>            : Broker Starter Config file. (required=false)
	-help                                                   : Print this message. (required=false)
```

Copy

```
docker run \
    --network=pinot-demo \
    --name pinot-server \
    -d ${PINOT_IMAGE} StartServer \
    -zkAddress pinot-zookeeper:2181
```

Copy

```
bin/pinot-admin.sh StartServer \
    -zkAddress localhost:2181
```

---

<a id="components-cluster-minion"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/cluster/minion -->

<!-- page_index: 9 -->

# Minion

- [Starting a minion](#components-cluster-minion--starting-a-minion)
- [Interfaces](#components-cluster-minion--interfaces)
- [Pinot task generator](#components-cluster-minion--pinot-task-generator)
- [PinotTaskExecutorFactory](#components-cluster-minion--pinottaskexecutorfactory)
- [MinionEventObserverFactory](#components-cluster-minion--minioneventobserverfactory)
- [Built-in tasks](#components-cluster-minion--built-in-tasks)
- [SegmentGenerationAndPushTask](#components-cluster-minion--segmentgenerationandpushtask)
- [RealtimeToOfflineSegmentsTask](#components-cluster-minion--realtimetoofflinesegmentstask)
- [MergeRollupTask](#components-cluster-minion--mergerolluptask)
- [PurgeTask](#components-cluster-minion--purgetask)
- [RefreshSegmentTask](#components-cluster-minion--refreshsegmenttask)
- [UpsertCompactionTask](#components-cluster-minion--upsertcompactiontask)
- [UpsertCompactMergeTask](#components-cluster-minion--upsertcompactmergetask)
- [Enable tasks](#components-cluster-minion--enable-tasks)
- [Schedule tasks](#components-cluster-minion--schedule-tasks)
- [Auto-schedule](#components-cluster-minion--auto-schedule)
- [Manual schedule](#components-cluster-minion--manual-schedule)
- [Schedule task on specific instances](#components-cluster-minion--schedule-task-on-specific-instances)
- [Task level advanced configs](#components-cluster-minion--task-level-advanced-configs)
- [allowDownloadFromServer](#components-cluster-minion--allowdownloadfromserver)
- [Plug-in custom tasks](#components-cluster-minion--plug-in-custom-tasks)
- [Task Manager UI](#components-cluster-minion--task-manager-ui)
- [Task-related metrics](#components-cluster-minion--task-related-metrics)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```

{% hint style="warning" %}
**Duplicate Keys in Configuration File**

Starting from Apache Pinot 1.3.0, duplicate keys in the minion configuration file will cause a `ConfigurationException` to be thrown during startup. Previously, duplicate keys would be silently merged into a list. If you encounter this error, ensure that each configuration property appears only once in your configuration file. The exception will include the exact file path, duplicate key name, and the line numbers where the duplicates were found.

Example error:
```

Copy

```
{% endhint %}

public interface PinotTaskGenerator {

  /**
   * Initializes the task generator.
   */
  void init(ClusterInfoAccessor clusterInfoAccessor);

  /**
   * Returns the task type of the generator.
   */
  String getTaskType();

  /**
   * Generates a list of tasks to schedule based on the given table configs.
   */
  List<PinotTaskConfig> generateTasks(List<TableConfig> tableConfigs);

  /**
   * Returns the timeout in milliseconds for each task, 3600000 (1 hour) by default.
   */
  default long getTaskTimeoutMs() {
    return JobConfig.DEFAULT_TIMEOUT_PER_TASK;
  }

  /**
   * Returns the maximum number of concurrent tasks allowed per instance, 1 by default.
   */
  default int getNumConcurrentTasksPerInstance() {
    return JobConfig.DEFAULT_NUM_CONCURRENT_TASKS_PER_INSTANCE;
  }

  /**
   * Performs necessary cleanups (e.g. remove metrics) when the controller leadership changes.
   */
  default void nonLeaderCleanUp() {
  }
}
```

Copy

```
public interface PinotTaskExecutorFactory {

  /**
   * Initializes the task executor factory.
   */
  void init(MinionTaskZkMetadataManager zkMetadataManager);

  /**
   * Returns the task type of the executor.
   */
  String getTaskType();

  /**
   * Creates a new task executor.
   */
  PinotTaskExecutor create();
}
```

Copy

```
public interface PinotTaskExecutor {

  /**
   * Executes the task based on the given task config and returns the execution result.
   */
  Object executeTask(PinotTaskConfig pinotTaskConfig)
      throws Exception;

  /**
   * Tries to cancel the task.
   */
  void cancel();
}
```

Copy

```
public interface MinionEventObserverFactory {

  /**
   * Initializes the task executor factory.
   */
  void init(MinionTaskZkMetadataManager zkMetadataManager);

  /**
   * Returns the task type of the event observer.
   */
  String getTaskType();

  /**
   * Creates a new task event observer.
   */
  MinionEventObserver create();
}
```

Copy

```
public interface MinionEventObserver {

  /**
   * Invoked when a minion task starts.
   *
   * @param pinotTaskConfig Pinot task config
   */
  void notifyTaskStart(PinotTaskConfig pinotTaskConfig);

  /**
   * Invoked when a minion task succeeds.
   *
   * @param pinotTaskConfig Pinot task config
   * @param executionResult Execution result
   */
  void notifyTaskSuccess(PinotTaskConfig pinotTaskConfig, @Nullable Object executionResult);

  /**
   * Invoked when a minion task gets cancelled.
   *
   * @param pinotTaskConfig Pinot task config
   */
  void notifyTaskCancelled(PinotTaskConfig pinotTaskConfig);

  /**
   * Invoked when a minion task encounters exception.
   *
   * @param pinotTaskConfig Pinot task config
   * @param exception Exception encountered during execution
   */
  void notifyTaskError(PinotTaskConfig pinotTaskConfig, Exception exception);
}
```

Copy

```
  "ingestionConfig": {
    "batchIngestionConfig": {
      "segmentIngestionType": "APPEND",
      "segmentIngestionFrequency": "DAILY",
      "batchConfigMaps": [
        {
          "input.fs.className": "org.apache.pinot.plugin.filesystem.S3PinotFS",
          "input.fs.prop.region": "us-west-2",
          "input.fs.prop.secretKey": "....",
          "input.fs.prop.accessKey": "....",
          "inputDirURI": "s3://my.s3.bucket/batch/airlineStats/rawdata/",
          "includeFileNamePattern": "glob:**/*.avro",
          "excludeFileNamePattern": "glob:**/*.tmp",
          "inputFormat": "avro"
        }
      ]
    }
  },
  "task": {
    "taskTypeConfigsMap": {
      "SegmentGenerationAndPushTask": {
        "schedule": "0 */10 * * * ?",
        "tableMaxNumTasks": "10"
      }
    }
  }
```

Copy

```
{
  ...
  "task": {
    "taskTypeConfigsMap": {
      "myTask": {
        "myProperty1": "value1",
        "myProperty2": "value2"
      }
    }
  }
}
```

Copy

```
{
  ...
  "task": {
    "concurrentSchedulingEnabled": true,
    "taskTypeConfigsMap": {
      "myTask": {
        "myProperty1": "value1"
      }
    }
  }
}
```

Copy

```
Using "POST /cluster/configs" API on CLUSTER tab in Swagger, with this payload
{
	"RealtimeToOfflineSegmentsTask.timeoutMs": "600000",
	"RealtimeToOfflineSegmentsTask.numConcurrentTasksPerInstance": "4"
}
```

Copy

```
controller.task.enableDistributedLocking=true
controller.task.concurrentSchedulingEnabled=true
```

Copy

```
  "task": {
    "taskTypeConfigsMap": {
      "RealtimeToOfflineSegmentsTask": {
        "bucketTimePeriod": "1h",
        "bufferTimePeriod": "1h",
        "schedule": "0 * * * * ?"
      }
    }
  },
```

Copy

```
  "task": {
    "taskTypeConfigsMap": {
      "RealtimeToOfflineSegmentsTask": {
        "bucketTimePeriod": "1h",
        "bufferTimePeriod": "1h",
        "schedule": "0 * * * * ?",
        "minionInstanceTag": "tag1_MINION"
      }
    }
  },
```

---

<a id="components-cluster-tenant"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/cluster/tenant -->

<!-- page_index: 10 -->

# Tenant

- [Tenant configuration](#components-cluster-tenant--tenant-configuration)
- [Create a tenant](#components-cluster-tenant--create-a-tenant)
- [Server tenant](#components-cluster-tenant--server-tenant)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
"tenants": {
  "broker": "brokerTenantName",
  "server": "serverTenantName"
}
```

Copy

```
{
     "tenantRole" : "BROKER",
     "tenantName" : "sampleBrokerTenant",
     "numberOfInstances" : 3
}
```

Copy

```
bin/pinot-admin.sh AddTenant \
    -name sampleBrokerTenant 
    -role BROKER 
    -instanceCount 3 -exec
```

Copy

```
curl -i -X POST -H 'Content-Type: application/json' -d @sample-broker-tenant.json localhost:9000/tenants
```

Copy

```
{
     "tenantRole" : "SERVER",
     "tenantName" : "sampleServerTenant",
     "offlineInstances" : 1,
     "realtimeInstances" : 1
}
```

Copy

```
bin/pinot-admin.sh AddTenant \
    -name sampleServerTenant \
    -role SERVER \
    -offlineInstanceCount 1 \
    -realtimeInstanceCount 1 -exec
```

Copy

```
curl -i -X POST -H 'Content-Type: application/json' -d @sample-server-tenant.json localhost:9000/tenants
```

---

<a id="components-table"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table -->

<!-- page_index: 11 -->

# Table

- [Segments](#components-table--segments)
- [Indexing](#components-table--indexing)
- [Pre-aggregation](#components-table--pre-aggregation)
- [Tenants](#components-table--tenants)
- [Hybrid table](#components-table--hybrid-table)
- [Examples](#components-table--examples)
- [Offline table creation](#components-table--offline-table-creation)
- [Streaming table creation](#components-table--streaming-table-creation)
- [Logical table](#components-table--logical-table)
- [Hybrid table creation](#components-table--hybrid-table-creation)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
    "tableIndexConfig": { 
      "noDictionaryColumns": ["metric1", "metric2"],
      "aggregateMetrics": true,
      ...
    }
```

Copy

```
  "broker": "brokerTenantName",
  "server": "serverTenantName",
  "tagOverrideConfig" : {
    "realtimeConsuming" : "serverTenantName_REALTIME"
    "realtimeCompleted" : "serverTenantName_OFFLINE"
  }
}
```

Copy

```
docker run \
    --network=pinot-demo \
    --name pinot-batch-table-creation \
    ${PINOT_IMAGE} AddTable \
    -schemaFile examples/batch/airlineStats/airlineStats_schema.json \
    -tableConfigFile examples/batch/airlineStats/airlineStats_offline_table_config.json \
    -controllerHost pinot-controller \
    -controllerPort 9000 \
    -exec
```

Copy

```
Executing command: AddTable -tableConfigFile examples/batch/airlineStats/airlineStats_offline_table_config.json -schemaFile examples/batch/airlineStats/airlineStats_schema.json -controllerHost pinot-controller -controllerPort 9000 -exec
Sending request: http://pinot-controller:9000/schemas to controller: a413b0013806, version: Unknown
{"status":"Table airlineStats_OFFLINE succesfully added"}
```

Copy

```
bin/pinot-admin.sh AddTable \
    -schemaFile examples/batch/airlineStats/airlineStats_schema.json \
    -tableConfigFile examples/batch/airlineStats/airlineStats_offline_table_config.json \
    -exec
```

Copy

```
# add schema curl -F schemaName=@airlineStats_schema.json localhost:9000/schemas

# add table curl -i -X POST -H 'Content-Type: application/json' \ -d @airlineStats_offline_table_config.json localhost:9000/tables
```

Copy

```
docker run \
    --network pinot-demo --name=kafka \
    -e KAFKA_NODE_ID=1 \
    -e KAFKA_PROCESS_ROLES=broker,controller \
    -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092,CONTROLLER://0.0.0.0:9093 \
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://kafka:9092 \
    -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER \
    -e KAFKA_LISTENER_SECURITY_PROTOCOL_MAP=CONTROLLER:PLAINTEXT,PLAINTEXT:PLAINTEXT \
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@kafka:9093 \
    -e KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR=1 \
    -e CLUSTER_ID=MkU3OEVBNTcwNTJENDM2Qk \
    -d apache/kafka:4.0.0
```

Copy

```
docker exec \
  -t kafka \
  /opt/kafka/bin/kafka-topics.sh \
  --bootstrap-server kafka:9092 \
  --partitions=1 --replication-factor=1 \
  --create --topic flights-realtime
```

Copy

```
docker run \
    --network=pinot-demo \
    --name pinot-streaming-table-creation \
    ${PINOT_IMAGE} AddTable \
    -schemaFile examples/stream/airlineStats/airlineStats_schema.json \
    -tableConfigFile examples/docker/table-configs/airlineStats_realtime_table_config.json \
    -controllerHost pinot-controller \
    -controllerPort 9000 \
    -exec
```

Copy

```
Executing command: AddTable -tableConfigFile examples/docker/table-configs/airlineStats_realtime_table_config.json -schemaFile examples/stream/airlineStats/airlineStats_schema.json -controllerHost pinot-controller -controllerPort 9000 -exec
Sending request: http://pinot-controller:9000/schemas to controller: 8fbe601012f3, version: Unknown
{"status":"Table airlineStats_REALTIME succesfully added"}
```

Copy

```
bin/pinot-admin.sh StartZookeeper -zkPort 2181
```

Copy

```
bin/pinot-admin.sh  StartKafka -zkAddress=localhost:2181/kafka -port 19092
```

Copy

```
bin/pinot-admin.sh AddTable \
    -schemaFile examples/stream/airlineStats/airlineStats_schema.json \
    -tableConfigFile examples/stream/airlineStats/airlineStats_realtime_table_config.json \
    -exec
```

Copy

```
"OFFLINE": {
    "tableName": "pinotTable", 
    "tableType": "OFFLINE", 
    "segmentsConfig": {
      ... 
    }, 
    "tableIndexConfig": { 
      ... 
    },  
    "tenants": {
      "broker": "myBrokerTenant", 
      "server": "myServerTenant"
    },
    "metadata": {
      ...
    }
  },
  "REALTIME": { 
    "tableName": "pinotTable", 
    "tableType": "REALTIME", 
    "segmentsConfig": {
      ...
    }, 
    "tableIndexConfig": { 
      ... 
      "streamConfigs": {
        ...
      },  
    },  
    "tenants": {
      "broker": "myBrokerTenant", 
      "server": "myServerTenant"
    },
    "metadata": {
    ...
    }
  }
}
```

---

<a id="components-table-schema"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table/schema -->

<!-- page_index: 12 -->

# Schema

- [Categories](#components-table-schema--categories)
- [Date and time fields](#components-table-schema--date-and-time-fields)
- [Creating a schema](#components-table-schema--creating-a-schema)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
{
  "schemaName": "flights",
  "enableColumnBasedNullHandling": true,
  "dimensionFieldSpecs": [
    {
      "name": "flightNumber",
      "dataType": "LONG",
      "notNull": true
    },
    {
      "name": "tags",
      "dataType": "STRING",
      "singleValueField": false,
      "defaultNullValue": "null"
    }
  ],
  "metricFieldSpecs": [
    {
      "name": "price",
      "dataType": "DOUBLE",
      "notNull": true,
      "defaultNullValue": 0
    }
  ],
  "dateTimeFieldSpecs": [
    {
      "name": "millisSinceEpoch",
      "dataType": "LONG",
      "format": "EPOCH",
      "granularity": "15:MINUTES"
    },
    {
      "name": "hoursSinceEpoch",
      "dataType": "INT",
      "notNull": true,
      "format": "EPOCH|HOURS",
      "granularity": "1:HOURS"
    },
    {
      "name": "dateString",
      "dataType": "STRING",
      "format": "SIMPLE_DATE_FORMAT|yyyy-MM-dd",
      "granularity": "1:DAYS"
    }
  ]
}
```

Copy

```
bin/pinot-admin.sh AddSchema -schemaFile flights-schema.json -exec

OR

bin/pinot-admin.sh AddTable -schemaFile flights-schema.json -tableFile flights-table.json -exec
```

Copy

```
curl -F [email protected]  localhost:9000/schemas
```

---

<a id="components-table-segment"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table/segment -->

<!-- page_index: 13 -->

# Segment

- [Creating a segment](#components-table-segment--creating-a-segment)
- [Load data in streaming](#components-table-segment--load-data-in-streaming)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
executionFrameworkSpec:
  name: 'standalone'
  segmentGenerationJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentGenerationJobRunner'
  segmentTarPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentTarPushJobRunner'
  segmentUriPushJobRunnerClassName: 'org.apache.pinot.plugin.ingestion.batch.standalone.SegmentUriPushJobRunner'

jobType: SegmentCreationAndTarPush
inputDirURI: 'examples/batch/baseballStats/rawdata'
includeFileNamePattern: 'glob:**/*.csv'
excludeFileNamePattern: 'glob:**/*.tmp'
outputDirURI: 'examples/batch/baseballStats/segments'
overwriteOutput: true

pinotFSSpecs:
  - scheme: file
    className: org.apache.pinot.spi.filesystem.LocalPinotFS

recordReaderSpec:
  dataFormat: 'csv'
  className: 'org.apache.pinot.plugin.inputformat.csv.CSVRecordReader'
  configClassName: 'org.apache.pinot.plugin.inputformat.csv.CSVRecordReaderConfig'
  configs:

tableSpec:
  tableName: 'baseballStats'
  schemaURI: 'http://localhost:9000/tables/baseballStats/schema'
  tableConfigURI: 'http://localhost:9000/tables/baseballStats'
  
segmentNameGeneratorSpec:

pinotClusterSpecs:
  - controllerURI: 'http://localhost:9000'

pushJobSpec:
  pushParallelism: 2
  pushAttempts: 2
  pushRetryIntervalMillis: 1000
```

Copy

```
docker run \
    --network=pinot-demo \
    --name pinot-data-ingestion-job \
    ${PINOT_IMAGE} LaunchDataIngestionJob \
    -jobSpecFile examples/docker/ingestion-job-specs/airlineStats.yaml
```

Copy

```
SegmentGenerationJobSpec:
!!org.apache.pinot.spi.ingestion.batch.spec.SegmentGenerationJobSpec
excludeFileNamePattern: null
executionFrameworkSpec: {extraConfigs: null, name: standalone, segmentGenerationJobRunnerClassName: org.apache.pinot.plugin.ingestion.batch.standalone.SegmentGenerationJobRunner,
  segmentTarPushJobRunnerClassName: org.apache.pinot.plugin.ingestion.batch.standalone.SegmentTarPushJobRunner,
  segmentUriPushJobRunnerClassName: org.apache.pinot.plugin.ingestion.batch.standalone.SegmentUriPushJobRunner}
includeFileNamePattern: glob:**/*.avro
inputDirURI: examples/batch/airlineStats/rawdata
jobType: SegmentCreationAndTarPush
outputDirURI: examples/batch/airlineStats/segments
overwriteOutput: true
pinotClusterSpecs:
- {controllerURI: 'http://pinot-controller:9000'}
pinotFSSpecs:
- {className: org.apache.pinot.spi.filesystem.LocalPinotFS, configs: null, scheme: file}
pushJobSpec: {pushAttempts: 2, pushParallelism: 1, pushRetryIntervalMillis: 1000,
  segmentUriPrefix: null, segmentUriSuffix: null}
recordReaderSpec: {className: org.apache.pinot.plugin.inputformat.avro.AvroRecordReader,
  configClassName: null, configs: null, dataFormat: avro}
segmentNameGeneratorSpec: null
tableSpec: {schemaURI: 'http://pinot-controller:9000/tables/airlineStats/schema',
  tableConfigURI: 'http://pinot-controller:9000/tables/airlineStats', tableName: airlineStats}

Trying to create instance for class org.apache.pinot.plugin.ingestion.batch.standalone.SegmentGenerationJobRunner
Initializing PinotFS for scheme file, classname org.apache.pinot.spi.filesystem.LocalPinotFS
Finished building StatsCollector!
Collected stats for 403 documents
Created dictionary for INT column: FlightNum with cardinality: 386, range: 14 to 7389
Using fixed bytes value dictionary for column: Origin, size: 294
Created dictionary for STRING column: Origin with cardinality: 98, max length in bytes: 3, range: ABQ to VPS
Created dictionary for INT column: Quarter with cardinality: 1, range: 1 to 1
Created dictionary for INT column: LateAircraftDelay with cardinality: 50, range: -2147483648 to 303
......
......
Pushing segment: airlineStats_OFFLINE_16085_16085_29 to location: http://pinot-controller:9000 for table airlineStats
Sending request: http://pinot-controller:9000/v2/segments?tableName=airlineStats to controller: a413b0013806, version: Unknown
Response for pushing table airlineStats segment airlineStats_OFFLINE_16085_16085_29 to location http://pinot-controller:9000 - 200: {"status":"Successfully uploaded segment: airlineStats_OFFLINE_16085_16085_29 of table: airlineStats"}
Pushing segment: airlineStats_OFFLINE_16084_16084_30 to location: http://pinot-controller:9000 for table airlineStats
Sending request: http://pinot-controller:9000/v2/segments?tableName=airlineStats to controller: a413b0013806, version: Unknown
Response for pushing table airlineStats segment airlineStats_OFFLINE_16084_16084_30 to location http://pinot-controller:9000 - 200: {"status":"Successfully uploaded segment: airlineStats_OFFLINE_16084_16084_30 of table: airlineStats"}
```

Copy

```
bin/pinot-admin.sh LaunchDataIngestionJob \
    -jobSpecFile examples/batch/airlineStats/ingestionJobSpec.yaml
```

Copy

```
inputDirURI: 'examples/batch/airlineStats/rawdata/${year}/${month}/${day}'
outputDirURI: 'examples/batch/airlineStats/segments/${year}/${month}/${day}'
```

Copy

```
docker run \
    --network=pinot-demo \
    --name pinot-data-ingestion-job \
    ${PINOT_IMAGE} LaunchDataIngestionJob \
    -jobSpecFile examples/docker/ingestion-job-specs/airlineStats.yaml
    -values year=2014 month=01 day=03
```

Copy

```
docker run \
  --network pinot-demo \
  --name=loading-airlineStats-data-to-kafka \
  ${PINOT_IMAGE} StreamAvroIntoKafka \
  -avroFile examples/stream/airlineStats/sample_data/airlineStats_data.avro \
  -kafkaTopic flights-realtime -kafkaBrokerList kafka:9092 -zkAddress pinot-zookeeper:2181/kafka
```

Copy

```
bin/pinot-admin.sh StreamAvroIntoKafka \
  -avroFile examples/stream/airlineStats/sample_data/airlineStats_data.avro \
  -kafkaTopic flights-realtime -kafkaBrokerList localhost:19092 -zkAddress localhost:2181/kafka
```

---

<a id="components-exploring-pinot"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/exploring-pinot -->

<!-- page_index: 14 -->

# Pinot Data Explorer

- [Cluster Manager](#components-exploring-pinot--cluster-manager)
- [Table management](#components-exploring-pinot--table-management)
- [Logical table management](#components-exploring-pinot--logical-table-management)
- [Query Console](#components-exploring-pinot--query-console)
- [Time-series query execution](#components-exploring-pinot--time-series-query-execution)
- [REST API](#components-exploring-pinot--rest-api)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
select playerName, max(hits)
from baseballStats
group by playerName
order by max(hits) desc
```

Copy

```
select sum(hits), sum(homeRuns), sum(numberOfGames)
from baseballStats
where yearID > 2010
```

Copy

```
select *
from baseballStats
order by league
```

---

<a id="components-table-logical-table"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table/logical-table -->

<!-- page_index: 15 -->

# Logical Table

- [Overview](#components-table-logical-table--overview)
- [How It Works](#components-table-logical-table--how-it-works)
- [Segment Pruning Optimization](#components-table-logical-table--segment-pruning-optimization)
- [Logical Table Configuration](#components-table-logical-table--logical-table-configuration)
- [Configuration Properties](#components-table-logical-table--configuration-properties)
- [Example Configuration](#components-table-logical-table--example-configuration)
- [Hybrid Logical Table Configuration](#components-table-logical-table--hybrid-logical-table-configuration)
- [Creating a Logical Table](#components-table-logical-table--creating-a-logical-table)
- [Step 1: Create the Schema](#components-table-logical-table--step-1-create-the-schema)
- [Step 2: Create the Logical Table](#components-table-logical-table--step-2-create-the-logical-table)
- [Managing Logical Tables](#components-table-logical-table--managing-logical-tables)
- [List Logical Tables](#components-table-logical-table--list-logical-tables)
- [Get Logical Table Configuration](#components-table-logical-table--get-logical-table-configuration)
- [Update Logical Table](#components-table-logical-table--update-logical-table)
- [Delete Logical Table](#components-table-logical-table--delete-logical-table)
- [Querying Logical Tables](#components-table-logical-table--querying-logical-tables)
- [Time Boundary Configuration](#components-table-logical-table--time-boundary-configuration)
- [Available Strategies](#components-table-logical-table--available-strategies)
- [Configuration Example](#components-table-logical-table--configuration-example)
- [Query Configuration](#components-table-logical-table--query-configuration)
- [Quota Configuration](#components-table-logical-table--quota-configuration)
- [Managing Logical Tables via the Controller UI](#components-table-logical-table--managing-logical-tables-via-the-controller-ui)
- [Accessing Logical Tables](#components-table-logical-table--accessing-logical-tables)
- [Supported Operations](#components-table-logical-table--supported-operations)
- [Quick Start Example](#components-table-logical-table--quick-start-example)
- [Validation Rules](#components-table-logical-table--validation-rules)
- [Limitations](#components-table-logical-table--limitations)
- [Pluggable LogicalTableConfig Serialization](#components-table-logical-table--pluggable-logicaltableconfig-serialization)
- [When to Use This](#components-table-logical-table--when-to-use-this)
- [See Also](#components-table-logical-table--see-also)

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
SELECT * FROM orders ORDER BY createdTime DESC LIMIT 10
```

Copy

```
{
  "tableName": "orders",
  "brokerTenant": "DefaultTenant",
  "physicalTableConfigMap": {
    "ordersUS_OFFLINE": {},
    "ordersEU_OFFLINE": {},
    "ordersAPAC_OFFLINE": {}
  },
  "refOfflineTableName": "ordersUS_OFFLINE"
}
```

Copy

```
{
  "tableName": "events",
  "brokerTenant": "DefaultTenant",
  "physicalTableConfigMap": {
    "eventsHistorical_OFFLINE": {},
    "eventsRecent_OFFLINE": {},
    "eventsLive_REALTIME": {}
  },
  "refOfflineTableName": "eventsHistorical_OFFLINE",
  "refRealtimeTableName": "eventsLive_REALTIME",
  "timeBoundaryConfig": {
    "boundaryStrategy": "min",
    "parameters": {
      "includedTables": ["eventsRecent_OFFLINE"]
    }
  }
}
```

Copy

```
{
  "schemaName": "orders",
  "dimensionFieldSpecs": [
    { "name": "orderId", "dataType": "STRING" },
    { "name": "customerId", "dataType": "STRING" },
    { "name": "region", "dataType": "STRING" },
    { "name": "productId", "dataType": "STRING" },
    { "name": "status", "dataType": "STRING" }
  ]
}
```

Copy

```
curl -F schemaName=@orders_schema.json localhost:9000/schemas
```

Copy

```
curl -X POST -H 'Content-Type: application/json' \
  -d '{
    "tableName": "orders",
    "brokerTenant": "DefaultTenant",
    "physicalTableConfigMap": {
      "ordersUS_OFFLINE": {},
      "ordersEU_OFFLINE": {},
      "ordersAPAC_OFFLINE": {}
    },
    "refOfflineTableName": "ordersUS_OFFLINE"
  }' \
  http://localhost:9000/logicalTables
```

Copy

```
curl http://localhost:9000/logicalTables
```

Copy

```
curl http://localhost:9000/logicalTables/{tableName}
```

Copy

```
curl -X PUT -H 'Content-Type: application/json' \
  -d '{
    "tableName": "orders",
    "brokerTenant": "DefaultTenant",
    "physicalTableConfigMap": {
      "ordersUS_OFFLINE": {},
      "ordersEU_OFFLINE": {},
      "ordersAPAC_OFFLINE": {},
      "ordersANZ_OFFLINE": {}
    },
    "refOfflineTableName": "ordersUS_OFFLINE"
  }' \
  http://localhost:9000/logicalTables/orders
```

Copy

```
curl -X DELETE http://localhost:9000/logicalTables/{tableName}
```

Copy

```
-- Query the logical table
SELECT COUNT(*) FROM orders

-- Filter by region
SELECT orderId, customerId, region, status
FROM orders
WHERE region = 'us'
LIMIT 10

-- Aggregate across all regions
SELECT region, COUNT(*) as orderCount
FROM orders
GROUP BY region
ORDER BY region
```

Copy

```
{
  "timeBoundaryConfig": {
    "boundaryStrategy": "min",
    "parameters": {
      "includedTables": ["eventsRecent_OFFLINE"]
    }
  }
}
```

Copy

```
{
  "tableName": "orders",
  "brokerTenant": "DefaultTenant",
  "physicalTableConfigMap": { ... },
  "refOfflineTableName": "ordersUS_OFFLINE",
  "query": {
    "timeoutMs": 30000,
    "disableGroovy": true,
    "maxServerResponseSizeBytes": 1000000,
    "maxQueryResponseSizeBytes": 5000000
  }
}
```

Copy

```
{
  "tableName": "orders",
  "brokerTenant": "DefaultTenant",
  "physicalTableConfigMap": { ... },
  "refOfflineTableName": "ordersUS_OFFLINE",
  "quota": {
    "maxQueriesPerSecond": 100
  }
}
```

Copy

```
docker run \
    -p 9000:9000 \
    apachepinot/pinot:latest QuickStart \
    -type LOGICAL_TABLE
```

Copy

```
./bin/pinot-admin.sh QuickStart -type LOGICAL_TABLE
```

Copy

```
public class MyCustomSerDe implements LogicalTableConfigSerDe {
    @Override
    public byte[] serialize(LogicalTableConfig config) { /* ... */ }

    @Override
    public LogicalTableConfig deserialize(byte[] bytes) { /* ... */ }
}
```

Copy

```
META-INF/services/org.apache.pinot.spi.config.table.logical.LogicalTableConfigSerDeProvider
```

---

<a id="components-table-segment-deep-store"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table/segment/deep-store -->

<!-- page_index: 16 -->

# Deep Store

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

---

<a id="components-table-segment-segment-retention"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table/segment/segment-retention -->

<!-- page_index: 17 -->

# Segment Retention

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

---

<a id="components-table-segment-segment-threshold"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table/segment/segment-threshold -->

<!-- page_index: 18 -->

# Segment Threshold

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

---

<a id="components-table-time-boundary"></a>

<!-- source_url: https://docs.pinot.apache.org/architecture-and-concepts/components/table/time-boundary -->

<!-- page_index: 19 -->

# Time Boundary

Was this helpful?

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

<svg fill="none" height="18" viewbox="0 0 18 18" width="18" xmlns="http://www.w3.org/2000/svg"><circle></circle><path></path></svg>

Copy

```
SELECT count(*)
FROM events
```

Copy

```
SELECT count(*)
FROM events_OFFLINE
WHERE timeColumn <= $timeBoundary
```

Copy

```
SELECT count(*)
FROM events_REALTIME
WHERE timeColumn > $timeBoundary
```

---
