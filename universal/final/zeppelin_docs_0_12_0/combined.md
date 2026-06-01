# What is Apache Zeppelin?

## Navigation

- Quick Start
  - [Install](#quickstart-install)
  - [Explore UI](#quickstart-explore_ui)
  - [Tutorial](#quickstart-tutorial)
  - [Kubernetes](#quickstart-kubernetes)
  - [Docker](#quickstart-docker)
  - [Yarn](#quickstart-yarn)
  - [Spark with Zeppelin](#quickstart-spark_with_zeppelin)
  - [Flink with Zeppelin](#quickstart-flink_with_zeppelin)
  - [SQL with Zeppelin](#quickstart-sql_with_zeppelin)
  - [Python with Zeppelin](#quickstart-python_with_zeppelin)
  - [R with Zeppelin](#quickstart-r_with_zeppelin)
- Usage
  - [Dynamic Form](#usage-dynamic_form-intro)
  - [What is Dynamic Form?](#usage-dynamic_form-intro)
  - [Text Display](#usage-display_system-basic--text)
  - [HTML Display](#usage-display_system-basic--html)
  - [Table Display](#usage-display_system-basic--table)
  - [Network Display](#usage-display_system-basic--network)
  - [Angular Display using Backend API](#usage-display_system-angular_backend)
  - [Angular Display using Frontend API](#usage-display_system-angular_frontend)
  - [Interpreter](#usage-interpreter-dependency_management)
  - [Overview](#usage-interpreter-overview)
  - [Interpreter Binding Mode](#usage-interpreter-interpreter_binding_mode)
  - [User Impersonation](#usage-interpreter-user_impersonation)
  - [Dependency Management](#usage-interpreter-dependency_management)
  - [Installing Interpreters](#usage-interpreter-installation)
  - [Execution Hooks (Experimental)](#usage-interpreter-execution_hooks)
  - [Publishing Paragraphs](#usage-other_features-publishing_paragraphs)
  - [Personalized Mode](#usage-other_features-personalized_mode)
  - [Customizing Zeppelin Homepage](#usage-other_features-customizing_homepage)
  - [Notebook Actions](#usage-other_features-notebook_actions)
  - [Cron Scheduler](#usage-other_features-cron_scheduler)
  - [Zeppelin Context](#usage-other_features-zeppelin_context)
  - [REST API](#usage-rest_api-zeppelin_server)
  - [Interpreter API](#usage-rest_api-interpreter)
  - [Zeppelin Server API](#usage-rest_api-zeppelin_server)
  - [Notebook API](#usage-rest_api-notebook)
  - [Notebook Repository API](#usage-rest_api-notebook_repository)
  - [Configuration API](#usage-rest_api-configuration)
  - [Credential API](#usage-rest_api-credential)
  - [Helium API](#usage-rest_api-helium)
  - [Client API](#usage-zeppelin_sdk-client_api)
  - [Session API](#usage-zeppelin_sdk-session_api)
- Setup
  - [How to Build Zeppelin](#setup-basics-how_to_build)
  - [Hadoop Integration](#setup-basics-hadoop_integration)
  - [Multi-user Support](#setup-basics-multi_user_support)
  - [Spark Cluster Mode: Standalone](#setup-deployment-spark_cluster_mode--spark-standalone-mode)
  - [Spark Cluster Mode: YARN](#setup-deployment-spark_cluster_mode--spark-on-yarn-mode)
  - [Spark Cluster Mode: Mesos](#setup-deployment-spark_cluster_mode--spark-on-mesos-mode)
  - [Zeppelin with Flink, Spark Cluster](#setup-deployment-flink_and_spark_cluster)
  - [Zeppelin on CDH](#setup-deployment-cdh)
  - [Zeppelin on VM: Vagrant](#setup-deployment-virtual_machine)
  - [HTTP Basic Auth using NGINX](#setup-security-authentication_nginx)
  - [Shiro Authentication](#setup-security-shiro_authentication)
  - [Notebook Authorization](#setup-security-notebook_authorization)
  - [Data Source Authorization](#setup-security-datasource_authorization)
  - [HTTP Security Headers](#setup-security-http_security_headers)
  - [Configuration](#setup-operation-configuration)
  - [Monitoring](#setup-operation-monitoring)
  - [Proxy Setting](#setup-operation-proxy_setting)
  - [Upgrading](#setup-operation-upgrading)
- Interpreter
  - [Interpreters](#usage-interpreter-installation)
  - [Overview](#usage-interpreter-overview)
  - [Spark](#interpreter-spark)
  - [Flink](#interpreter-flink)
  - [JDBC](#interpreter-jdbc)
  - [Python](#interpreter-python)
  - [R](#interpreter-r)
  - [Alluxio](#interpreter-alluxio)
  - [BigQuery](#interpreter-bigquery)
  - [Cassandra](#interpreter-cassandra)
  - [Elasticsearch](#interpreter-elasticsearch)
  - [Groovy](#interpreter-groovy)
  - [HBase](#interpreter-hbase)
  - [HDFS](#interpreter-hdfs)
  - [Hive](#interpreter-hive)
  - [influxDB](#interpreter-influxdb)
  - [Java](#interpreter-java)
  - [Jupyter](#interpreter-jupyter)
  - [Livy](#interpreter-livy)
  - [Mahout](#interpreter-mahout)
  - [Markdown](#interpreter-markdown)
  - [MongoDB](#interpreter-mongodb)
  - [Neo4j](#interpreter-neo4j)
  - [Postgresql, HAWQ](#interpreter-postgresql)
  - [Shell](#interpreter-shell)
  - [Sparql](#interpreter-sparql)
- More
  - [Writing Zeppelin Interpreter](#development-writing_zeppelin_interpreter)
  - [Overview](#development-helium-overview)
  - [Writing Helium Application](#development-helium-writing_application)
  - [Writing Helium Spell](#development-helium-writing_spell)
  - [Writing Helium Visualization: Basics](#development-helium-writing_visualization_basic)
  - [Writing Helium Visualization: Transformation](#development-helium-writing_visualization_transformation)
  - [How to Build Zeppelin](#setup-basics-how_to_build)
  - [Useful Developer Tools](#development-contribution-useful_developer_tools)
  - [How to Contribute (code)](#development-contribution-how_to_contribute_code)
  - [How to Contribute (website)](#development-contribution-how_to_contribute_website)
- Other pages
  - [What is Apache Zeppelin?](#index)
  - [./bin/zeppelin-systemd-service.sh disable](#setup-basics-systemd)

## Content

<a id="quickstart-install"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/install.html -->

<!-- page_index: 1 -->

<a id="quickstart-install--install"></a>

# Install

Welcome to Apache Zeppelin! On this page are instructions to help you get started.

<a id="quickstart-install--requirements"></a>

## Requirements

Apache Zeppelin officially supports and is tested on the following environments:

| Name | Value |
| --- | --- |
| Java | JDK 11 (set `JAVA_HOME`) |
| OS | Mac OSX Ubuntu 18.04 Ubuntu 20.04 |

<a id="quickstart-install--downloading-binary-package"></a>

### Downloading Binary Package

Two binary packages are available on the [download page](http://zeppelin.apache.org/download.html). Only difference between these two binaries is whether all the interpreters are included in the package file.

- **all interpreter package**: unpack it in a directory of your choice and you're ready to go.
- **net-install interpreter package**: only spark, python, markdown and shell interpreter included. Unpack and follow [install additional interpreters](#usage-interpreter-installation) to install other interpreters. If you're unsure, just run `./bin/install-interpreter.sh --all` and install all interpreters.

<a id="quickstart-install--building-zeppelin-from-source"></a>

### Building Zeppelin from source

Follow the instructions [How to Build](#setup-basics-how_to_build), If you want to build from source instead of using binary package.

<a id="quickstart-install--starting-apache-zeppelin"></a>

## Starting Apache Zeppelin

<a id="quickstart-install--starting-apache-zeppelin-from-the-command-line"></a>

#### Starting Apache Zeppelin from the Command Line

On all unix like platforms:

```
bin/zeppelin-daemon.sh start
```

After Zeppelin has started successfully, go to <http://localhost:8080> with your web browser.

By default Zeppelin is listening at `127.0.0.1:8080`, so you can't access it when it is deployed on another remote machine.
To access a remote Zeppelin, you need to change `zeppelin.server.addr` to `0.0.0.0` in `conf/zeppelin-site.xml`.

Check log file at `ZEPPELIN_HOME/logs/zeppelin-server-*.log` if you can not open Zeppelin.

<a id="quickstart-install--stopping-zeppelin"></a>

#### Stopping Zeppelin

```
bin/zeppelin-daemon.sh stop
```

<a id="quickstart-install--using-the-official-docker-image"></a>

## Using the official docker image

Make sure that [docker](https://www.docker.com/community-edition) is installed in your local machine.

Use this command to launch Apache Zeppelin in a container.

```bash
docker run -p 8080:8080 --rm --name zeppelin apache/zeppelin:0.10.0
```

To persist `logs` and `notebook` directories, use the [volume](https://docs.docker.com/engine/reference/commandline/run/#mount-volume--v-read-only) option for docker container.

```bash
docker run -u $(id -u) -p 8080:8080 --rm -v $PWD/logs:/logs -v $PWD/notebook:/notebook \
           -e ZEPPELIN_LOG_DIR='/logs' -e ZEPPELIN_NOTEBOOK_DIR='/notebook' \
           --name zeppelin apache/zeppelin:0.10.0
```

`-u $(id -u)` is to make sure you have the permission to write logs and notebooks.

For many interpreters, they require other dependencies, e.g. Spark interpreter requires Spark binary distribution
and Flink interpreter requires Flink binary distribution. You can also mount them via docker volumn. e.g.

```bash
docker run -u $(id -u) -p 8080:8080 --rm -v /mnt/disk1/notebook:/notebook \
-v /usr/lib/spark-current:/opt/spark -v /mnt/disk1/flink-1.12.2:/opt/flink -e FLINK_HOME=/opt/flink  \
-e SPARK_HOME=/opt/spark  -e ZEPPELIN_NOTEBOOK_DIR='/notebook' --name zeppelin apache/zeppelin:0.10.0
```

If you have trouble accessing `localhost:8080` in the browser, Please clear browser cache.

<a id="quickstart-install--start-apache-zeppelin-with-a-service-manager"></a>

## Start Apache Zeppelin with a service manager

> **Note :** The below description was written based on Ubuntu.

Apache Zeppelin can be auto-started as a service with an init script, using a service manager like **upstart**.

This is an example upstart script saved as `/etc/init/zeppelin.conf`
This allows the service to be managed with commands such as

```
sudo service zeppelin start
sudo service zeppelin stop
sudo service zeppelin restart
```

Other service managers could use a similar approach with the `upstart` argument passed to the `zeppelin-daemon.sh` script.

```
bin/zeppelin-daemon.sh upstart
```

**zeppelin.conf**

```aconf
description "zeppelin"

start on (local-filesystems and net-device-up IFACE!=lo)
stop on shutdown

# Respawn the process on unexpected termination
respawn

# respawn the job up to 7 times within a 5 second period.
# If the job exceeds these values, it will be stopped and marked as failed.
respawn limit 7 5

# zeppelin was installed in /usr/share/zeppelin in this example
chdir /usr/share/zeppelin
exec bin/zeppelin-daemon.sh upstart
```

<a id="quickstart-install--next-steps"></a>

## Next Steps

Congratulations, you have successfully installed Apache Zeppelin! Here are a few steps you might find useful:

<a id="quickstart-install--new-to-apache-zeppelin..."></a>

#### New to Apache Zeppelin...

- For an in-depth overview, head to [Explore Zeppelin UI](#quickstart-explore_ui).
- And then, try run Tutorial Notebooks shipped with your Zeppelin distribution.
- And see how to change [configurations](#setup-operation-configuration) like port number, etc.

<a id="quickstart-install--spark-flink-sql-python-r-and-more"></a>

#### Spark, Flink, SQL, Python, R and more

- [Spark support in Zeppelin](#quickstart-spark_with_zeppelin), to know more about deep integration with [Apache Spark](http://spark.apache.org/).
- [Flink support in Zeppelin](#quickstart-flink_with_zeppelin), to know more about deep integration with [Apache Flink](http://flink.apache.org/).
- [SQL support in Zeppelin](#quickstart-sql_with_zeppelin) for SQL support
- [Python support in Zeppelin](#quickstart-python_with_zeppelin), for Matplotlib, Pandas, Conda/Docker integration.
- [R support in Zeppelin](#quickstart-r_with_zeppelin)
- [All Available Interpreters](#index--available-interpreters)

<a id="quickstart-install--multi-user-support-..."></a>

#### Multi-user support ...

- Check [Multi-user support](#setup-basics-multi_user_support)

---

---

<a id="quickstart-explore_ui"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/explore_ui.html -->

<!-- page_index: 2 -->

<a id="quickstart-explore_ui--explore-apache-zeppelin-ui-classic-ui"></a>

# Explore Apache Zeppelin UI (Classic UI)

<a id="quickstart-explore_ui--how-to-enable-and-switch-to-the-classic-ui"></a>

## How to Enable and Switch to the Classic UI

Starting from Zeppelin 0.12.0, this UI has become optional. To use this UI, please build with the following profile:

```
-Pweb-classic
```

Afterward, you can switch to the classic UI via the `Swtich to Classic UI` button in the settings menu of the new UI app.

![](assets/images/switch-to-classic-ui_b60c840ea64d5a20.png)

<a id="quickstart-explore_ui--configuring-the-default-ui"></a>

### Configuring the default UI

Zeppelin allows you to configure the default, especially for users who prefer the classic UI.

To set the default UI to classic, add the following property to the `zeppelin-site.xml` file:

```xml
<property>
  <name>zeppelin.default.ui</name>
  <value>classic</value>
  <description>Default UI for Zeppelin. Options: classic or new. Default configuration is 'new'</description>
</property>
```

<a id="quickstart-explore_ui--main-home"></a>

## Main home

The first time you connect to Zeppelin ([default installations start on http://localhost:8080](http://localhost:8080/)), you'll land at the main page similar to the below screen capture.

![](assets/images/homepage_1912f5dd505b90c5.png)

On the left of the page are listed all existing notes. Those notes are stored by default in the `$ZEPPELIN_HOME/notebook` folder.

You can filter them by name using the input text form. You can also create a new note, refresh the list of existing notes
(in case you manually copy them into the `$ZEPPELIN_HOME/notebook` folder) and import a note.

![](assets/images/notes-management_9d6b0dde79e9f23d.png)

When clicking on `Import Note` link, a new dialog open. From there you can import your note from local disk or from a remote location
if you provide the URL.

![](assets/images/note-import-dialog_30632806d1f7cdf0.png)

By default, the name of the imported note is the same as the original note but you can override it by providing a new name.

<a id="quickstart-explore_ui--menus"></a>

## Menus

<a id="quickstart-explore_ui--notebook"></a>

### Notebook

The `Notebook` menu proposes almost the same features as the note management section in the home page. From the drop-down menu you can:

1. Open a selected note
2. Filter node by name
3. Create a new note

![](assets/images/notebook-menu_2b4fd513e83b3549.png)

<a id="quickstart-explore_ui--settings"></a>

### Settings

This menu gives you access to settings and displays information about Zeppelin. User name is set to `anonymous` if you use default shiro configuration. If you want to set up authentification, see [Shiro Authentication](#setup-security-shiro_authentication).

![](assets/images/settings-menu_14ad7d12970d55b7.png)

<a id="quickstart-explore_ui--about-zeppelin"></a>

#### About Zeppelin

You can check Zeppelin version in this menu.

![](assets/images/about-menu_ffa7d83052a938d5.png)

<a id="quickstart-explore_ui--interpreter"></a>

#### Interpreter

In this menu you can:

1. Configure existing **interpreter instance**
2. Add/remove **interpreter instances**

![](assets/images/interpreter-menu_e69cf8e28462f948.png)

<a id="quickstart-explore_ui--credential"></a>

#### Credential

This menu allows you to save credentials for data sources which are passed to interpreters.

![](assets/images/credential-menu_511f42da1b39178b.png)

<a id="quickstart-explore_ui--configuration"></a>

#### Configuration

This menu displays all the Zeppelin configuration that are set in the config file `$ZEPPELIN_HOME/conf/zeppelin-site.xml`

![](assets/images/configuration-menu_4365f6fb449b7fb5.png)

<a id="quickstart-explore_ui--note-layout"></a>

## Note Layout

Each Zeppelin note is composed of 1 .. N paragraphs. The note can be viewed as a paragraph container.

![](assets/images/note-paragraph-layout_5cc5cfd878504dc2.png)

<a id="quickstart-explore_ui--paragraph"></a>

### Paragraph

Each paragraph consists of 2 sections: `code section` where you put your source code and `result section` where you can see the result of the code execution.

![](assets/images/paragraph-layout_7ea2ed057ade2015.png)

On the top-right corner of each paragraph there are some commands to:

- execute the paragraph code
- hide/show `code section`
- hide/show `result section`
- configure the paragraph

To configure the paragraph, just click on the gear icon:

![](assets/images/paragraph-configuration-dialog_f0cc89d84df09e38.png)

From this dialog, you can (in descending order):

- find the **paragraph id** ( **20150924-163507\_134879501** )
- control paragraph width. Since Zeppelin is using the grid system of **Twitter Bootstrap**, each paragraph width can be changed from 1 to 12
- move the paragraph 1 level up
- move the paragraph 1 level down
- create a new paragraph
- change paragraph title
- show/hide line number in the `code section`
- disable the run button for this paragraph
- export the current paragraph as an **iframe** and open the **iframe** in a new window
- clear the `result section`
- delete the current paragraph

<a id="quickstart-explore_ui--note-toolbar"></a>

### Note toolbar

At the top of the note, you can find a toolbar which exposes command buttons as well as configuration, security and display options.

![](assets/images/note-toolbar_2a1749372bafbd73.png)

On the far right is displayed the note name, just click on it to reveal the input form and update it.

In the middle of the toolbar you can find the command buttons:

- execute all the paragraphs **sequentially**, in their display order
- hide/show `code section` of all paragraphs
- hide/show `result section` of all paragraphs
- clear the `result section` of all paragraphs
- clone the current note
- export the current note to a JSON file. \_Please note that the `code section` and `result section` of all paragraphs will be exported. If you have heavy data in the `result section` of some paragraphs, it is recommended to clean them before exporting
- commit the current node content
- delete the note
- schedule the execution of **all paragraph** using a CRON syntax

![](assets/images/note-commands_1ad596ac377a795d.png)

On the right of the note tool bar you can find configuration icons:

- display all the keyboard shorcuts
- configure the interpreters binding to the current note
- configure the note permissions
- switch the node display mode between `default`, `simple` and `report`

![](assets/images/note-configuration_a3b3f5237cf4e7eb.png)

---

---

<a id="quickstart-tutorial"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/tutorial.html -->

<!-- page_index: 3 -->

<a id="quickstart-tutorial--zeppelin-tutorial"></a>

# Zeppelin Tutorial

This tutorial walks you through some of the fundamental Zeppelin concepts. We will assume you have already installed Zeppelin. If not, please see [here](#quickstart-install) first.

Current main backend processing engine of Zeppelin is [Apache Spark](https://spark.apache.org). If you're new to this system, you might want to start by getting an idea of how it processes data to get the most out of Zeppelin.

<a id="quickstart-tutorial--tutorial-with-local-file"></a>

## Tutorial with Local File

<a id="quickstart-tutorial--data-refine"></a>

### Data Refine

Before you start Zeppelin tutorial, you will need to download [bank.zip](http://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip).

First, to transform csv format data into RDD of `Bank` objects, run following script. This will also remove header using `filter` function.

```scala

val bankText = sc.textFile("yourPath/bank/bank-full.csv")

case class Bank(age:Integer, job:String, marital : String, education : String, balance : Integer)

// split each line, filter out header (starts with "age"), and map it into Bank case class
val bank = bankText.map(s=>s.split(";")).filter(s=>s(0)!="\"age\"").map(
    s=>Bank(s(0).toInt,
            s(1).replaceAll("\"", ""),
            s(2).replaceAll("\"", ""),
            s(3).replaceAll("\"", ""),
            s(5).replaceAll("\"", "").toInt
        )
)

// convert to DataFrame and create temporal table
bank.toDF().registerTempTable("bank")
```

<a id="quickstart-tutorial--data-retrieval"></a>

### Data Retrieval

Suppose we want to see age distribution from `bank`. To do this, run:

```sql
%sql select age, count(1) from bank where age < 30 group by age order by age
```

You can make input box for setting age condition by replacing `30` with `${maxAge=30}`.

```sql
%sql select age, count(1) from bank where age < ${maxAge=30} group by age order by age
```

Now we want to see age distribution with certain marital status and add combo box to select marital status. Run:

```sql
%sql select age, count(1) from bank where marital="${marital=single,single|divorced|married}" group by age order by age
```

<a id="quickstart-tutorial--tutorial-with-streaming-data"></a>

## Tutorial with Streaming Data

<a id="quickstart-tutorial--data-refine-2"></a>

### Data Refine

Since this tutorial is based on Twitter's sample tweet stream, you must configure authentication with a Twitter account. To do this, take a look at [Twitter Credential Setup](https://databricks-training.s3.amazonaws.com/realtime-processing-with-spark-streaming.html#twitter-credential-setup). After you get API keys, you should fill out credential related values(`apiKey`, `apiSecret`, `accessToken`, `accessTokenSecret`) with your API keys on following script.

This will create a RDD of `Tweet` objects and register these stream data as a table:

```scala
import org.apache.spark.streaming._
import org.apache.spark.streaming.twitter._
import org.apache.spark.storage.StorageLevel
import scala.io.Source
import scala.collection.mutable.HashMap
import java.io.File
import org.apache.log4j.Logger
import org.apache.log4j.Level
import sys.process.stringSeqToProcess

/** Configures the Oauth Credentials for accessing Twitter */
def configureTwitterCredentials(apiKey: String, apiSecret: String, accessToken: String, accessTokenSecret: String) {
  val configs = new HashMap[String, String] ++= Seq(
    "apiKey" -> apiKey, "apiSecret" -> apiSecret, "accessToken" -> accessToken, "accessTokenSecret" -> accessTokenSecret)
  println("Configuring Twitter OAuth")
  configs.foreach{ case(key, value) =>
    if (value.trim.isEmpty) {
      throw new Exception("Error setting authentication - value for " + key + " not set")
    }
    val fullKey = "twitter4j.oauth." + key.replace("api", "consumer")
    System.setProperty(fullKey, value.trim)
    println("\tProperty " + fullKey + " set as [" + value.trim + "]")
  }
  println()
}

// Configure Twitter credentials
val apiKey = "xxxxxxxxxxxxxxxxxxxxxxxxx"
val apiSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
val accessToken = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
val accessTokenSecret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
configureTwitterCredentials(apiKey, apiSecret, accessToken, accessTokenSecret)

import org.apache.spark.streaming.twitter._
val ssc = new StreamingContext(sc, Seconds(2))
val tweets = TwitterUtils.createStream(ssc, None)
val twt = tweets.window(Seconds(60))

case class Tweet(createdAt:Long, text:String)
twt.map(status=>
  Tweet(status.getCreatedAt().getTime()/1000, status.getText())
).foreachRDD(rdd=>
  // Below line works only in spark 1.3.0.
  // For spark 1.1.x and spark 1.2.x,
  // use rdd.registerTempTable("tweets") instead.
  rdd.toDF().registerAsTable("tweets")
)

twt.print

ssc.start()
```

<a id="quickstart-tutorial--data-retrieval-2"></a>

### Data Retrieval

For each following script, every time you click run button you will see different result since it is based on real-time data.

Let's begin by extracting maximum 10 tweets which contain the word **girl**.

```sql
%sql select * from tweets where text like '%girl%' limit 10
```

This time suppose we want to see how many tweets have been created per sec during last 60 sec. To do this, run:

```sql
%sql select createdAt, count(1) from tweets group by createdAt order by createdAt
```

You can make user-defined function and use it in Spark SQL. Let's try it by making function named `sentiment`. This function will return one of the three attitudes( positive, negative, neutral ) towards the parameter.

```scala
def sentiment(s:String) : String = {
    val positive = Array("like", "love", "good", "great", "happy", "cool", "the", "one", "that")
    val negative = Array("hate", "bad", "stupid", "is")

    var st = 0;

    val words = s.split(" ")
    positive.foreach(p =>
        words.foreach(w =>
            if(p==w) st = st+1
        )
    )

    negative.foreach(p=>
        words.foreach(w=>
            if(p==w) st = st-1
        )
    )
    if(st>0)
        "positivie"
    else if(st<0)
        "negative"
    else
        "neutral"
}

// Below line works only in spark 1.3.0.
// For spark 1.1.x and spark 1.2.x,
// use sqlc.registerFunction("sentiment", sentiment _) instead.
sqlc.udf.register("sentiment", sentiment _)
```

To check how people think about girls using `sentiment` function we've made above, run this:

```sql
%sql select sentiment(text), count(1) from tweets where text like '%girl%' group by sentiment(text)
```

---

---

<a id="quickstart-kubernetes"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/kubernetes.html -->

<!-- page_index: 4 -->

<a id="quickstart-kubernetes--zeppelin-on-kubernetes"></a>

# Zeppelin on Kubernetes

Zeppelin can run on clusters managed by [Kubernetes](https://kubernetes.io/). When Zeppelin runs in Pod, it creates pods for individual interpreter. Also Spark interpreter auto configured to use Spark on Kubernetes in client mode.

Key benefits are

- Interpreter scale-out
- Spark interpreter auto configure Spark on Kubernetes
- Able to customize Kubernetes yaml file
- Spark UI access

<a id="quickstart-kubernetes--prerequisites"></a>

## Prerequisites

- Zeppelin >= 0.9.0 docker image
- Spark >= 2.4.0 docker image (in case of using Spark Interpreter)
- A running Kubernetes cluster with access configured to it using [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [Kubernetes DNS](https://kubernetes.io/docs/concepts/services-networking/dns-pod-service/) configured in your cluster
- Enough cpu and memory in your Kubernetes cluster. We recommend 4CPUs, 6g of memory to be able to start Spark Interpreter with few executors.

  - If you're using [minikube](https://kubernetes.io/docs/setup/minikube/), check your cluster capacity (`kubectl describe node`) and increase if necessary


```
 $ minikube delete    # otherwise configuration won't apply
 $ minikube config set cpus <number>
 $ minikube config set memory <number in MB>
 $ minikube start
 $ minikube config view
```

<a id="quickstart-kubernetes--quickstart"></a>

## Quickstart

Let's first clone the Zeppelin repository from GitHub:

```sh
git clone https://github.com/apache/zeppelin.git
cd zeppelin
# you can check out to your desired version/branch
# git checkout tags/v0.10.1
# just make sure you check the version inside "./pom.xml"
```

Now we are going to create the `zeppelin-distribution` image. This may take some time and this image will be used as a base for the upcoming required images:

```sh
docker build -t zeppelin-distribution:latest -f ./Dockerfile .
```

Next, we will build our `zeppelin-server` image:

```sh
cd scripts/docker/zeppelin-server
# Looking at the "./pom.xml" we can see the version is 0.12.0
# Let's set the correct version in our Dockerfile:
# vi Dockerfile
# ARG version="0.12.0"
# Once you saved the Dockerfile with the correct version we can build our image:docker build -t zeppelin-server:0.12.0 -f ./Dockerfile .
```

The last image we build is `zeppelin-interpreter`:

```sh
cd scripts/docker/zeppelin-interpreter
docker build -t zeppelin-interpreter:0.12.0 -f ./Dockerfile .
```

So we should now have the following images:

```sh
# sudo if you are on Linux and Docker requires root
$ docker images

REPOSITORY                    TAG               IMAGE ID       CREATED          SIZE
zeppelin-interpreter          0.12.0   4f77fe989eed   3 minutes ago    622MB
zeppelin-server               0.12.0   4f77fe989eed   3 minutes ago    622MB
zeppelin-distribution         latest            bd2fb4b321d2   40 minutes ago   1.27GB
```

Reminder: Please adjust the images in the YAML-File of `zeppelin-server.yaml`

Start zeppelin on Kubernetes cluster,

```sh
kubectl apply -f zeppelin-server.yaml
```

Port forward Zeppelin server port,

```sh
kubectl port-forward zeppelin-server 8080:80
```

and browse [localhost:8080](http://localhost:8080).
Try running some paragraphs and see if each interpreter is running as a Pod (using `kubectl get pods`), instead of a local process.

To shut down,

```sh
kubectl delete -f zeppelin-server.yaml
```

<a id="quickstart-kubernetes--spark-interpreter"></a>

## Spark Interpreter

Build spark docker image to use Spark Interpreter.
Download spark binary distribution and run following command.
Spark 2.4.0 or later version is required.

```
# if you're using minikube, set docker-env
$ eval $(minikube docker-env)

# build docker image
$ <spark-distribution>/bin/docker-image-tool.sh -m -t 2.4.0 build
```

Run `docker images` and check if `spark:2.4.0` is created.
Configure `sparkContainerImage` of `zeppelin-server-conf` ConfigMap in `zeppelin-server.yaml`.

Create note and configure executor number (default 1)

```
%spark.conf
spark.executor.instances  5
```

And then start your spark interpreter

```
%spark
sc.parallelize(1 to 100).count
...
```

While `spark.master` property of SparkInterpreter starts with `k8s://` (default `k8s://https://kubernetes.default.svc` when Zeppelin started using zeppelin-server.yaml), Spark executors will be automatically created in your Kubernetes cluster.
Spark UI is accessible by clicking `SPARK JOB` on the Paragraph.

Check [here](https://spark.apache.org/docs/latest/running-on-kubernetes.html) to know more about Running Spark on Kubernetes.

<a id="quickstart-kubernetes--build-zeppelin-image-manually"></a>

## Build Zeppelin image manually

To build your own Zeppelin image, first build Zeppelin project with `-Pbuild-distr` flag.

```
$ ./mvnw package -DskipTests -Pbuild-distr <your flags>
```

Binary package will be created under `zeppelin-distribution/target` directory. Move created package file under `scripts/docker/zeppelin/bin/` directory.

```
$ mv zeppelin-distribution/target/zeppelin-*-bin.tgz scripts/docker/zeppelin/bin/
```

`scripts/docker/zeppelin/bin/Dockerfile` downloads package from internet. Modify the file to add package from filesystem.

```
...

# Find following section and comment out #RUN echo "$LOG_TAG Download Zeppelin binary" && \
#    wget -O /tmp/zeppelin-${Z_VERSION}-bin-all.tgz "https://www.apache.org/dyn/closer.lua/zeppelin/zeppelin-${Z_VERSION}/zeppelin-${Z_VERSION}-bin-all.tgz?action=download" && \
#    tar -zxvf /tmp/zeppelin-${Z_VERSION}-bin-all.tgz && \
#    rm -rf /tmp/zeppelin-${Z_VERSION}-bin-all.tgz && \
#    mv /zeppelin-${Z_VERSION}-bin-all ${ZEPPELIN_HOME}

# Add following lines right after the commented line above ADD zeppelin-${Z_VERSION}.tar.gz /RUN ln -s /zeppelin-${Z_VERSION} /zeppelin...
```

Then build docker image.

```
# configure docker env, if you're using minikube
$ eval $(minikube docker-env)

# change directory
$ cd scripts/docker/zeppelin/bin/

# build image. Replace <tag>.
$ docker build -t <tag> .
```

Finally, set custom image `<tag>` just created to `image` and `ZEPPELIN_K8S_CONTAINER_IMAGE` env variable of `zeppelin-server` container spec in `zeppelin-server.yaml` file.

Currently, single docker image is being used in both Zeppelin server and Interpreter pods. Therefore,

| Pod | Number of instances | Image | Note |
| --- | --- | --- | --- |
| Zeppelin Server | 1 | Zeppelin docker image | User creates/deletes with kubectl command |
| Zeppelin Interpreters | n | Zeppelin docker image | Zeppelin Server creates/deletes |
| Spark executors | m | Spark docker image | Spark Interpreter creates/deletes |

Currently, size of Zeppelin docker image is quite big. Zeppelin project is planning to provides lightweight images for each individual interpreter in the future.

<a id="quickstart-kubernetes--how-it-works"></a>

## How it works

<a id="quickstart-kubernetes--zeppelin-on-kubernetes-2"></a>

### Zeppelin on Kubernetes

`k8s/zeppelin-server.yaml` is provided to run Zeppelin Server with few sidecars and configurations.
Once Zeppelin Server is started in side Kubernetes, it auto configure itself to use `K8sStandardInterpreterLauncher`.

The launcher creates each interpreter in a Pod using templates located under `k8s/interpreter/` directory.
Templates in the directory applied in alphabetical order. Templates are rendered by [jinjava](https://github.com/HubSpot/jinjava)
and all interpreter properties are accessible inside the templates.

<a id="quickstart-kubernetes--spark-on-kubernetes"></a>

### Spark on Kubernetes

When interpreter group is `spark`, Zeppelin sets necessary spark configuration automatically to use Spark on Kubernetes.
It uses client mode, so Spark interpreter Pod works as a Spark driver, spark executors are launched in separate Pods.
This auto configuration can be overrided by manually setting `spark.master` property of Spark interpreter.

<a id="quickstart-kubernetes--accessing-spark-ui-or-service-running-in-interpreter-pod"></a>

### Accessing Spark UI (or Service running in interpreter Pod)

Zeppelin server Pod has a reverse proxy as a sidecar, and it splits traffic to Zeppelin server and Spark UI running in the other Pods.
It assume both `<your service domain>` and `*.<your service domain>` point the nginx proxy address.
`<your service domain>` is directed to ZeppelinServer, `*.<your service domain>` is directed to interpreter Pods.

`<port>-<interpreter pod svc name>.<your service domain>` is convention to access any application running in interpreter Pod.

For example, When your service domain name is `local.zeppelin-project.org` Spark interpreter Pod is running with a name `spark-axefeg` and Spark UI is running on port 4040,

```
4040-spark-axefeg.local.zeppelin-project.org
```

is the address to access Spark UI.

Default service domain is `local.zeppelin-project.org:8080`. `local.zeppelin-project.org` and `*.local.zeppelin-project.org` configured to resolve `127.0.0.1`.
It allows access Zeppelin and Spark UI with `kubectl port-forward zeppelin-server 8080:80`.

If you like to use your custom domain

1. Configure [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) in Kubernetes cluster for `http` port of the service `zeppelin-server` defined in `k8s/zeppelin-server.yaml`.
2. Configure DNS record that your service domain and wildcard subdomain point the IP Addresses of your Ingress.
3. Modify `serviceDomain` of `zeppelin-server-conf` ConfigMap in `k8s/zeppelin-server.yaml` file.
4. Apply changes (e.g. `kubectl apply -f k8s/zeppelin-server.yaml`)

<a id="quickstart-kubernetes--persist-notebook-and-conf-directory"></a>

## Persist /notebook and /conf directory

Notebook and configurations are not persisted by default. Please configure volume and update `k8s/zeppelin-server.yaml`
to use the volume to persiste /notebook and /conf directory if necessary.

<a id="quickstart-kubernetes--customization"></a>

## Customization

<a id="quickstart-kubernetes--zeppelin-server-pod"></a>

### Zeppelin Server Pod

Edit `k8s/zeppelin-server.yaml` and apply.

<a id="quickstart-kubernetes--interpreter-pod"></a>

### Interpreter Pod

Since Interpreter Pod is created/deleted by ZeppelinServer using templates under `k8s/interpreter` directory, to customize,

1. Prepare `k8s/interpreter` directory with customization (edit or create new yaml file), in a Kubernetes volume.
2. Modify `k8s/zeppelin-server.yaml` and mount prepared volume dir `k8s/interpreter` to `/zeppelin/k8s/interpreter/`.
3. Apply modified `k8s/zeppelin-server.yaml`.
4. Run a paragraph will create an interpreter using modified yaml files.

The interpreter pod can also be customized through the interpreter settings. Here are some of the properties:

| Property Name | Default Value | Description |
| --- | --- | --- |
| `zeppelin.k8s.interpreter.namespace` | `default` | Specify the namespace of the current interpreter. Users can set different namespaces for different interpreters. In order to minimize permissions, the interpreter pod can only be created in the `default` namespace by default. If users need to create an interpreter pod in other namespaces, they need to add the corresponding `rolebinding` in `k8s/zeppelin-server.yaml`. |
| `zeppelin.k8s.interpreter.serviceAccount` | `default` | The Kubernetes service account to use. |
| `zeppelin.k8s.interpreter.container.image` | `apache/zeppelin:<ZEPPELIN_VERSION>` | The interpreter image to use. |
| `zeppelin.k8s.interpreter.cores` | (optional) | The number of cpu cores to use. |
| `zeppelin.k8s.interpreter.memory` | (optional) | The memory to use, e.g., `1g`. |
| `zeppelin.k8s.interpreter.gpu.type` | (optional) | Set the type of gpu to request when the interpreter pod is required to schedule gpu resources, e.g., `nvidia.com/gpu`. |
| `zeppelin.k8s.interpreter.gpu.nums` | (optional) | Tne number of gpu to use. |
| `zeppelin.k8s.interpreter.imagePullSecrets` | (optional) | Set the comma-separated list of Kubernetes secrets while pulling images, e.g., `mysecret1,mysecret2` |
| `zeppelin.k8s.interpreter.container.imagePullPolicy` | (optional) | Set the pull policy of the interpreter image, e.g., `Always` |
| `zeppelin.k8s.spark.container.imagePullPolicy` | (optional) | Set the pull policy of the spark image, e.g., `Always` |
| `zeppelin.spark.uiWebUrl` | `//-.` | The URL for user to access Spark UI. The default value is a [jinjava](https://github.com/HubSpot/jinjava) template that contains three variables. |
| `zeppelin.k8s.spark.useIngress` | (optional) | If true, the [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) will be created when creating the spark interpreter. So users can access the Spark UI through Ingress. |
| `zeppelin.k8s.spark.ingress.host` | `-.` | If `zeppelin.k8s.spark.useIngress` is `true`, it configures the `host` value of the Ingress. The default value is a [jinjava](https://github.com/HubSpot/jinjava) template that contains three variables. Users can access the Spark UI through a customized `zeppelin.k8s.spark.ingress.host`. |

<a id="quickstart-kubernetes--future-work"></a>

## Future work

- Smaller interpreter docker image.
- Blocking communication between interpreter Pod.
- Spark Interpreter Pod has Role CRUD for any pod/service in the same namespace. Which should be restricted to only Spark executors Pod.
- Per note interpreter mode by default when Zeppelin is running on Kubernetes

<a id="quickstart-kubernetes--development"></a>

## Development

Instead of build Zeppelin distribution package and docker image everytime during development, Zeppelin can run locally (such as inside your IDE in debug mode) and able to run Interpreter using [K8sStandardInterpreterLauncher](https://github.com/apache/zeppelin/blob/master/zeppelin-plugins/launcher/k8s-standard/src/main/java/org/apache/zeppelin/interpreter/launcher/K8sStandardInterpreterLauncher.java) by configuring following environment variables.

| Environment variable | Value | Description |
| --- | --- | --- |
| `ZEPPELIN_RUN_MODE` | `k8s` | Make Zeppelin run interpreter on Kubernetes |
| `ZEPPELIN_K8S_PORTFORWARD` | `true` | Enable port forwarding from local Zeppelin instance to Interpreters running on Kubernetes |
| `ZEPPELIN_K8S_CONTAINER_IMAGE` | `<image>:<version>` | Zeppelin interpreter docker image to use |
| `ZEPPELIN_K8S_SPARK_CONTAINER_IMAGE` | `<image>:<version>` | Spark docker image to use |
| `ZEPPELIN_K8S_NAMESPACE` | `<k8s namespace>` | Kubernetes namespace to use |
| `KUBERNETES_AUTH_TOKEN` | `<token>` | Kubernetes auth token to create resources |

---

---

<a id="quickstart-docker"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/docker.html -->

<!-- page_index: 5 -->

<a id="quickstart-docker--zeppelin-interpreter-on-docker"></a>

# Zeppelin Interpreter on Docker

Zeppelin service runs on local server. Zeppelin is able to run the interpreter in the docker container, Isolating the operating environment of the interpreter through the docker container. Zeppelin can be easily used without having to install python, spark, etc. on the local node.

Key benefits are

- Interpreter environment isolating
- Not need to install python, spark, etc. environment on the local node
- Docker does not need to pre-install zeppelin binary package, Automatically upload local zeppelin interpreter lib files to the container
- Automatically upload local configuration files (such as spark-conf, hadoop-conf-dir, keytab file, ...) to the container, so that the running environment in the container is exactly the same as the local.
- Zeppelin server runs locally, making it easier to manage and maintain

<a id="quickstart-docker--prerequisites"></a>

## Prerequisites

- apache/zeppelin docker image
- Spark >= 2.2.0 docker image (in case of using Spark Interpreter)
- Docker 1.6+ [Install Docker](https://docs.docker.com/v17.12/install/)
- Use docker's host network, so there is no need to set up a network specifically

<a id="quickstart-docker--docker-configuration"></a>

### Docker Configuration

Because `DockerInterpreterProcess` communicates via docker's tcp interface.

By default, docker provides an interface as a sock file, so you need to modify the configuration file to open the tcp interface remotely.

vi `/etc/docker/daemon.json`, Add `tcp://0.0.0.0:2375` to the `hosts` configuration item.

```json
{
    ...
    "hosts": ["tcp://0.0.0.0:2375","unix:///var/run/docker.sock"]
}
```

`hosts` property reference: https://docs.docker.com/engine/reference/commandline/dockerd/

<a id="quickstart-docker--security-warning"></a>

#### Security warning

Making the Docker daemon available over TCP is potentially dangerous: as you
can read [here](https://docs.docker.com/engine/security/#docker-daemon-attack-surface), the docker daemon typically has broad privileges, so only trusted users should
have access to it. If you expose the daemon over TCP, you must use firewalling
to make sure only trusted users can access the port. This also includes making
sure the interpreter docker containers that are started by Zeppelin do not have
access to this port.

<a id="quickstart-docker--quickstart"></a>

## Quickstart

1. Modify these 2 configuration items in `zeppelin-site.xml`.

```xml
 <property>
   <name>zeppelin.run.mode</name>
   <value>docker</value>
   <description>'auto|local|k8s|docker'</description>
 </property>

 <property>
   <name>zeppelin.docker.container.image</name>
   <value>apache/zeppelin</value>
   <description>Docker image for interpreters</description>
 </property>
```

1. set timezone in zeppelin-env.sh

Set to the same time zone as the zeppelin server, keeping the time zone in the interpreter docker container the same as the server. E.g, `"America/New_York"` or `"Asia/Shanghai"`

```bash
 export ZEPPELIN_DOCKER_TIME_ZONE="America/New_York"
```

<a id="quickstart-docker--build-zeppelin-image-manually"></a>

## Build Zeppelin image manually

To build Zeppelin image, support Kerberos certification & install spark binary.

Use the `/scripts/docker/interpreter/Dockerfile` to build the image.

```
FROM apache/zeppelin:0.8.0
MAINTAINER Apache Software Foundation <dev@zeppelin.apache.org>

ENV SPARK_VERSION=2.3.3
ENV HADOOP_VERSION=2.7

# support Kerberos certification RUN export DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -yq krb5-user libpam-krb5 && apt-get clean

RUN apt-get update && apt-get install -y curl unzip wget grep sed vim tzdata && apt-get clean

# auto upload zeppelin interpreter lib RUN rm -rf /zeppelin

RUN rm -rf /spark
RUN wget https://www-us.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN tar zxvf spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
RUN mv spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} spark
RUN rm spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
```

Then build docker image.

```
# build image. Replace <tag>.
$ docker build -t <tag> .
```

<a id="quickstart-docker--how-it-works"></a>

## How it works

<a id="quickstart-docker--zeppelin-interpreter-on-docker-2"></a>

### Zeppelin interpreter on Docker

Zeppelin service runs on local server, it auto configure itself to use `DockerInterpreterLauncher`.

`DockerInterpreterLauncher` via `DockerInterpreterProcess` launcher creates each interpreter in a container using docker image.

`DockerInterpreterProcess` uploads the binaries and configuration files of the local zeppelin service to the container:

- ${ZEPPELIN\_HOME}/bin
- ${ZEPPELIN\_HOME}/lib
- ${ZEPPELIN\_HOME}/interpreter/${interpreterGroupName}
- ${ZEPPELIN\_HOME}/conf/zeppelin-site.xml
- ${ZEPPELIN\_HOME}/conf/log4j.properties
- ${ZEPPELIN\_HOME}/conf/log4j\_yarn\_cluster.properties
- HADOOP\_CONF\_DIR
- SPARK\_CONF\_DIR
- /etc/krb5.conf
- Keytab file configured in the interpreter properties
  - zeppelin.shell.keytab.location
  - spark.yarn.keytab
  - zeppelin.jdbc.keytab.location
  - zeppelin.server.kerberos.keytab

All file paths uploaded to the container, Keep the same path as the local one. This will ensure that all configurations are used correctly.

<a id="quickstart-docker--spark-interpreter-on-docker"></a>

### Spark interpreter on Docker

When interpreter group is `spark`, Zeppelin sets necessary spark configuration automatically to use Spark on Docker.
Supports all running modes of `local[*]`, `yarn-client`, and `yarn-cluster` of zeppelin spark interpreter.

<a id="quickstart-docker--spark_conf_dir"></a>

#### SPARK\_CONF\_DIR

1. Configuring in the zeppelin-env.sh

Because there are only spark binary files in the interpreter image, no spark conf files are included.
The configuration file in the `spark-<version>/conf/` local to the zeppelin service needs to be uploaded to the `/spark/conf/` directory in the spark interpreter container.
So you need to setting `export SPARK_CONF_DIR=/spark-<version>-path/conf/` in the `zeppelin-env.sh` file.

1. Configuring in the spark Properties

You can also configure it in the spark interpreter properties.

| properties name | Value | Description |
| ----- | ----- | ----- |
| SPARK\_CONF\_DIR | /spark--path.../conf/ | Spark--path/conf/ path local on the zeppelin service |

<a id="quickstart-docker--hadoop_conf_dir"></a>

#### HADOOP\_CONF\_DIR

1. Configuring in the zeppelin-env.sh

Because there are only spark binary files in the interpreter image, no configuration files are included.
The configuration file in the `hadoop-<version>/etc/hadoop` local to the zeppelin service needs to be uploaded to the spark interpreter container.
So you need to setting `export HADOOP_CONF_DIR=hadoop-<version>-path/etc/hadoop` in the `zeppelin-env.sh` file.

1. Configuring in the spark Properties

You can also configure it in the spark interpreter properties.

| properties name | Value | Description |
| ----- | ----- | ----- |
| HADOOP\_CONF\_DIR | hadoop--path/etc/hadoop | hadoop--path/etc/hadoop path local on the zeppelin service |

<a id="quickstart-docker--accessing-spark-ui-or-service-running-in-interpreter-container"></a>

#### Accessing Spark UI (or Service running in interpreter container)

Because the zeppelin interpreter container uses the host network, the spark.ui.port port is automatically allocated, so do not configure `spark.ui.port=xxxx` in `spark-defaults.conf`

<a id="quickstart-docker--future-work"></a>

## Future work

- Configuring container resources that can be used by different interpreters by configuration.

<a id="quickstart-docker--development"></a>

## Development

Instead of build Zeppelin distribution package and docker image everytime during development, Zeppelin can run locally (such as inside your IDE in debug mode) and able to run Interpreter using [DockerInterpreterLauncher](https://github.com/apache/zeppelin/blob/master/zeppelin-plugins/launcher/docker/src/main/java/org/apache/zeppelin/interpreter/launcher/DockerInterpreterLauncher.java) by configuring following environment variables.

1. zeppelin-site.xml

| Configuration variable | Value | Description |
| --- | --- | --- |
| `ZEPPELIN_RUN_MODE` | `docker` | Make Zeppelin run interpreter on Docker |
| `ZEPPELIN_DOCKER_CONTAINER_IMAGE` | `<image>:<version>` | Zeppelin interpreter docker image to use |

---

---

<a id="quickstart-yarn"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/yarn.html -->

<!-- page_index: 6 -->

<a id="quickstart-yarn--zeppelin-interpreter-on-yarn"></a>

# Zeppelin Interpreter on Yarn

Zeppelin is able to run interpreter process in yarn container. The key benefit is the scalability, you won't run out of memory
of the zeppelin server host if you run large amount of interpreter processes.

<a id="quickstart-yarn--prerequisites"></a>

## Prerequisites

The following is required for yarn interpreter mode.

- Hadoop client (both 2.x and 3.x are supported) is installed.
- `$HADOOP_HOME/bin` is put in `PATH`. Because internally zeppelin will run command `hadoop classpath` to get all the hadoop jars and put them in the classpath of Zeppelin.
- Set `USE_HADOOP` as `true` in `zeppelin-env.sh`.

<a id="quickstart-yarn--configuration"></a>

## Configuration

Yarn interpreter mode needs to be set for each interpreter. You can set `zeppelin.interpreter.launcher` to be `yarn` to run it in yarn mode.
Besides that, you can also specify other properties as following table.

| Name | Default Value | Description |
| --- | --- | --- |
| zeppelin.interpreter.yarn.resource.memory | 1024 | memory for interpreter process, unit: mb |
| zeppelin.interpreter.yarn.resource.memoryOverhead | 384 | Amount of non-heap memory to be allocated per interpreter process in yarn interpreter mode, in MiB unless otherwise specified. This is memory that accounts for things like VM overheads, interned strings, other native overheads, etc. |
| zeppelin.interpreter.yarn.resource.cores | 1 | cpu cores for interpreter process |
| zeppelin.interpreter.yarn.queue | default | yarn queue name |
| zeppelin.interpreter.yarn.node.label.expression |  | yarn node label expression specified for interpreter process |

<a id="quickstart-yarn--differences-with-non-yarn-interpreter-mode-local-mode"></a>

## Differences with non-yarn interpreter mode (local mode)

There're several differences between yarn interpreter mode with non-yarn interpreter mode (local mode)

- New yarn app will be allocated for the interpreter process.
- Any local path setting won't work in yarn interpreter process. E.g. if you run python interpreter in yarn interpreter mode, then you need to make sure the python executable of `zeppelin.python` exist in all the nodes of yarn cluster.
  Because the python interpreter may launch in any node.
- Don't use it for spark interpreter. Instead use spark's built-in yarn-client or yarn-cluster which is more suitable for spark interpreter.

---

---

<a id="quickstart-spark_with_zeppelin"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/spark_with_zeppelin.html -->

<!-- page_index: 7 -->

<a id="quickstart-spark_with_zeppelin--spark-support-in-zeppelin"></a>

# Spark support in Zeppelin

For a brief overview of Apache Spark fundamentals with Apache Zeppelin, see the following guide:

- **built-in** Apache Spark integration.
- With [Spark Scala](https://spark.apache.org/docs/latest/quick-start.html) [SparkSQL](http://spark.apache.org/sql/), [PySpark](https://spark.apache.org/docs/latest/api/python/), [SparkR](https://spark.apache.org/docs/latest/sparkr.html)
- Inject [SparkContext](https://spark.apache.org/docs/latest/api/java/org/apache/spark/SparkContext.html), [SQLContext](https://spark.apache.org/docs/latest/sql-programming-guide.html) and [SparkSession](https://spark.apache.org/docs/latest/sql-programming-guide.html) automatically
- Canceling job and displaying its progress
- Supports different modes: local, standalone, yarn(client & cluster), k8s
- Dependency management
- Supports [different context per user / note](#usage-interpreter-interpreter_binding_mode)
- Sharing variables among PySpark, SparkR and Spark through [ZeppelinContext](#interpreter-spark--zeppelincontext)
- [Livy Interpreter](#interpreter-livy)

For the further information about Spark support in Zeppelin, please check

- [Spark Interpreter](#interpreter-spark)

---

---

<a id="quickstart-flink_with_zeppelin"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/flink_with_zeppelin.html -->

<!-- page_index: 8 -->

<a id="quickstart-flink_with_zeppelin--flink-support-in-zeppelin"></a>

# Flink support in Zeppelin

For a brief overview of Apache Flink fundamentals with Apache Zeppelin, see the following guide:

- **built-in** Apache Flink integration.
- With [Flink Scala Scala](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/deployment/repls/scala_shell/) [PyFlink Shell](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/deployment/repls/python_shell/), [Flink SQL](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/dev/table/sql/overview/)
- Inject ExecutionEnvironment, StreamExecutionEnvironment, BatchTableEnvironment, StreamTableEnvironment.
- Canceling job and displaying its progress
- Supports different modes: local, remote, yarn, yarn-application
- Dependency management
- Streaming Visualization

For the further information about Flink support in Zeppelin, please check

- [Flink Interpreter](#interpreter-flink)

---

---

<a id="quickstart-sql_with_zeppelin"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/sql_with_zeppelin.html -->

<!-- page_index: 9 -->

# SQL support in Zeppelin

---

---

<a id="quickstart-python_with_zeppelin"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/python_with_zeppelin.html -->

<!-- page_index: 10 -->

<a id="quickstart-python_with_zeppelin--python-support-in-zeppelin"></a>

# Python support in Zeppelin

The following guides explain how to use Apache Zeppelin that enables you to write in Python:

- supports [vanilla python](#interpreter-python--vanilla-python-interpreter-python) and [ipython](#interpreter-python--ipython-interpreter-pythonipython-recommended)
- supports flexible python environments using [conda](#interpreter-python--conda), [docker](#interpreter-python--docker)
- can query using [PandasSQL](#interpreter-python--sql-over-pandas-dataframes)
- also, provides [PySpark](#interpreter-spark)
- [run python interpreter in yarn cluster](#interpreter-python--run-python-in-yarn-cluster) with customized conda python environment.
- with [matplotlib integration](#interpreter-python--matplotlib-integration)
- can create results including **UI widgets** using [Dynamic Form](#interpreter-python--using-zeppelin-dynamic-forms)

For the further information about Python support in Zeppelin, please check

- [Python Interpreter](#interpreter-python)

---

---

<a id="quickstart-r_with_zeppelin"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/quickstart/r_with_zeppelin.html -->

<!-- page_index: 11 -->

<a id="quickstart-r_with_zeppelin--r-support-in-zeppelin"></a>

# R support in Zeppelin

The following guides explain how to use Apache Zeppelin that enables you to write in R:

- Supports [vanilla R](#interpreter-r--how-to-use-r-interpreter) and [IRkernel](#interpreter-r--how-to-use-r-interpreter)
- Visualize R dataframe via [ZeppelinContext](#interpreter-r--zshow)
- [Run R interpreter in yarn cluster](#interpreter-r--run-r-in-yarn-cluster) with customized conda R environment.
- [Make R Shiny App](#interpreter-r--make-shiny-app-in-zeppelin)

For the further information about R support in Zeppelin, please check

- [R Interpreter](#interpreter-r)

---

---

<a id="usage-dynamic_form-intro"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/dynamic_form/intro.html -->

<!-- page_index: 12 -->

<a id="usage-dynamic_form-intro--what-is-dynamic-form"></a>

# What is Dynamic Form?

Apache Zeppelin dynamically creates input forms. Depending on language backend, there're two different ways to create dynamic form.
Custom language backend can select which type of form creation it wants to use. Forms can have different scope (paragraph or note).
Forms with scope "note" available in all paragraphs regardless of which paragraph has code to create these forms.

<a id="usage-dynamic_form-intro--using-form-templates-scope:-paragraph"></a>

## Using form Templates (scope: paragraph)

This mode creates form using simple template language. It's simple and easy to use. For example Markdown, Shell, Spark SQL language backend uses it.

<a id="usage-dynamic_form-intro--text-input-form"></a>

### Text input form

To create text input form, use `${formName}` templates.

for example

![](assets/images/form-input_990939bfb348fe28.png)

Also you can provide default value, using `${formName=defaultValue}`.

![](assets/images/form-input-default_453c834dbbd91b77.png)

<a id="usage-dynamic_form-intro--password-form"></a>

### Password form

To create password form, use `${password:formName}` templates.

for example

![](assets/images/form-password_a301e822c6ed8091.png)

<a id="usage-dynamic_form-intro--select-form"></a>

### Select form

To create select form, use `${formName=defaultValue,option1|option2...}`

for example

![](assets/images/form-select_dc73889842c039d0.png)

Also you can separate option's display name and value, using `${formName=defaultValue,option1(DisplayName)|option2(DisplayName)...}`

![](assets/images/form-select-displayname_f909fcb0c49de6f3.png)

The paragraph will be automatically run after you change your selection by default.
But in case you have multiple types dynamic form in one paragraph, you might want to run the paragraph after changing all the selections.
You can control this by unchecking the below **Run on selection change** option in the setting menu.

Even if you uncheck this option, still you can run it by pressing `Enter`.

![](assets/images/selectform-checkbox_0648344476d01198.png)

<a id="usage-dynamic_form-intro--checkbox-form"></a>

### Checkbox form

For multi-selection, you can create a checkbox form using `${checkbox:formName=defaultValue1|defaultValue2...,option1|option2...}`. The variable will be substituted by a comma-separated string based on the selected items. For example:

![](assets/images/form-checkbox_46d0aac426481b58.png)

You can specify the delimiter using `${checkbox(delimiter):formName=...}`:

![](assets/images/form-checkbox-delimiter_9ebf41a7ab2cb093.png)

Like [select form](#usage-dynamic_form-intro--select-form), the paragraph will be automatically run after you change your selection by default.
But in case you have multiple types dynamic form in one paragraph, you might want to run the paragraph after changing all the selections.
You can control this by unchecking the below **Run on selection change** option in the setting menu.

Even if you uncheck this option, still you can run it by pressing `Enter`.

![](assets/images/selectform-checkbox_0648344476d01198.png)

<a id="usage-dynamic_form-intro--using-form-templates-scope:-note"></a>

## Using form Templates (scope: note)

Has a same syntax but starts with two symbols `$`. (for ex. input `$${forName}`)

<a id="usage-dynamic_form-intro--creates-programmatically-scope:-paragraph"></a>

## Creates Programmatically (scope: paragraph)

Some language backends can programmatically create forms. For example [ZeppelinContext](#interpreter-spark--zeppelincontext) provides a form creation API

Here are some examples:

<a id="usage-dynamic_form-intro--text-input-form-2"></a>

### Text input form

```scala
%spark
println("Hello "+z.textbox("name"))
```

```python
%pyspark
print("Hello "+z.textbox("name"))
```

![](assets/images/form-input-prog_92d6795b11eab87c.png)

Use `z.input()` instead in version 0.7.3 or prior. `z.input()` is deprecated in 0.8.0.

<a id="usage-dynamic_form-intro--text-input-form-with-default-value"></a>

### Text input form with default value

```scala
%spark
println("Hello "+z.textbox("name", "sun")) 
```

```python
%pyspark
print("Hello "+z.textbox("name", "sun"))
```

![](assets/images/form-input-default-prog_0cfb8ad058c5b348.png)

Use `z.input()` instead in version 0.7.3 or prior. `z.input()` is deprecated in 0.8.0.

<a id="usage-dynamic_form-intro--password-form-2"></a>

### Password form

```scala
%spark
print("Password is "+ z.password("my_password"))
```

```python
%pyspark
print("Password is "+ z.password("my_password"))
```

![](assets/images/form-password-prog_36d1ee7210422a29.png)

<a id="usage-dynamic_form-intro--select-form-2"></a>

### Select form

```scala
%spark
println("Hello "+z.select("day", Seq(("1","mon"),
                                    ("2","tue"),
                                    ("3","wed"),
                                    ("4","thurs"),
                                    ("5","fri"),
                                    ("6","sat"),
                                    ("7","sun"))))
```

```python
%pyspark
print("Hello "+z.select("day", [("1","mon"),
                                ("2","tue"),
                                ("3","wed"),
                                ("4","thurs"),
                                ("5","fri"),
                                ("6","sat"),
                                ("7","sun")]))
```

![](assets/images/form-select-prog_563f69b7608a276b.png)

<a id="usage-dynamic_form-intro--checkbox-form-2"></a>

#### Checkbox form

```scala
%spark
val options = Seq(("apple","Apple"), ("banana","Banana"), ("orange","Orange"))
println("Hello "+z.checkbox("fruit", options).mkString(" and "))
```

```python
%pyspark
options = [("apple","Apple"), ("banana","Banana"), ("orange","Orange")]
print("Hello "+ " and ".join(z.checkbox("fruit", options, ["apple"])))
```

![](assets/images/form-checkbox-prog_cee6b093e43954e2.png)

<a id="usage-dynamic_form-intro--creates-programmatically-scope:-note"></a>

## Creates Programmatically (scope: note)

The difference in the method names:

| Scope paragraph | Scope note |
| --- | --- |
| input (or textbox) | noteTextbox |
| select | noteSelect |
| checkbox | noteCheckbox |

---

---

<a id="usage-display_system-basic"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/display_system/basic.html -->

<!-- page_index: 13 -->

<a id="usage-display_system-basic--basic-display-system-in-apache-zeppelin"></a>

# Basic Display System in Apache Zeppelin

<a id="usage-display_system-basic--text"></a>

## Text

By default, Apache Zeppelin prints interpreter response as a plain text using `text` display system.

![](assets/images/display-text_10bc8c610e7a621d.png)

You can explicitly say you're using `text` display system.

![](assets/images/display-text1_2e085ab79cb7ad6c.png)

<a id="usage-display_system-basic--html"></a>

## Html

With `%html` directive, Zeppelin treats your output as HTML

![](assets/images/display-html_5324bf8843b8b8f6.png)

<a id="usage-display_system-basic--markdown"></a>

## Markdown

You can render your output as markdown with the `%markdown` directive.

<a id="usage-display_system-basic--mathematical-expressions"></a>

### Mathematical expressions

HTML display system automatically formats mathematical expression using [MathJax](https://www.mathjax.org/). You can use
`\\( INLINE EXPRESSION \\)` and `$$ EXPRESSION $$` to format. For example

![](assets/images/display-formula_8a0284b20a5d014a.png)

<a id="usage-display_system-basic--table"></a>

## Table

If you have data that row separated by `\n` (newline) and column separated by `\t` (tab) with first row as header row, for example

![](assets/images/display-table_ff4eedf29c1b702f.png)

You can simply use `%table` display system to leverage Zeppelin's built in visualization.

![](assets/images/display-table1_e97af76871eca7c6.png)

If table contents start with `%html`, it is interpreted as an HTML.

![](assets/images/display-table-html_6d5b7bf57015e125.png)

> **Note :** Display system is backend independent.

<a id="usage-display_system-basic--network"></a>

## Network

With the `%network` directive, Zeppelin treats your output as a graph. Zeppelin can leverage the Property Graph Model.

<a id="usage-display_system-basic--what-is-the-labelled-property-graph-model"></a>

### What is the Labelled Property Graph Model?

A [Property Graph](https://github.com/tinkerpop/gremlin/wiki/Defining-a-Property-Graph) is a graph that has these elements:

- a set of vertices
  - each vertex has a unique identifier.
  - each vertex has a set of outgoing edges.
  - each vertex has a set of incoming edges.
  - each vertex has a collection of properties defined by a map from key to value
- a set of edges
  - each edge has a unique identifier.
  - each edge has an outgoing tail vertex.
  - each edge has an incoming head vertex.
  - each edge has a label that denotes the type of relationship between its two vertices.
  - each edge has a collection of properties defined by a map from key to value.

![](https://github.com/tinkerpop/gremlin/raw/master/doc/images/graph-example-1.jpg)

A [Labelled Property Graph](https://neo4j.com/developer/graph-database/#property-graph) is a Property Graph where the nodes can be tagged with **labels** representing their different roles in the graph model

![](http://s3.amazonaws.com/dev.assets.neo4j.com/wp-content/uploads/property_graph_model.png)

<a id="usage-display_system-basic--what-are-the-apis"></a>

### What are the APIs?

The new NETWORK visualization is based on json with the following params:

- "nodes" (mandatory): list of nodes of the graph every node can have the following params:
  - "id" (mandatory): the id of the node (must be unique);
  - "label": the main Label of the node;
  - "labels": the list of the labels of the node;
  - "data": the data attached to the node;
- "edges": list of the edges of the graph;
  - "id" (mandatory): the id of the edge (must be unique);
  - "source" (mandatory): the id of source node of the edge;
  - "target" (mandatory): the id of target node of the edge;
  - "label": the main type of the edge;
  - "data": the data attached to the edge;
- "labels": a map (K, V) where K is the node label and V is the color of the node;
- "directed": (true/false, default false) wich tells if is directed graph or not;
- "types": a *distinct* list of the edge types of the graph

If you click on a node or edge on the bottom of the paragraph you find a list of entity properties

![](assets/images/display-network_ee564de20e8b540e.png)

This kind of graph can be easily *flatten* in order to support other visualization formats provided by Zeppelin.

![](assets/images/display-network-flatten_c9cb6a1fcd67526a.png)

<a id="usage-display_system-basic--how-to-use-it"></a>

### How to use it?

An example of a simple graph

```scala
%spark
print(s"""
%network {
    "nodes": [
        {"id": 1},
        {"id": 2},
        {"id": 3}
    ],
    "edges": [
        {"source": 1, "target": 2, "id" : 1},
        {"source": 2, "target": 3, "id" : 2},
        {"source": 1, "target": 2, "id" : 3},
        {"source": 1, "target": 2, "id" : 4},
        {"source": 2, "target": 1, "id" : 5},
        {"source": 2, "target": 1, "id" : 6}
    ]
}
""")
```

that will look like:

![](assets/images/display-simple-network_694d3da9eb30e69c.png)

A little more complex graph:

```scala
%spark
print(s"""
%network {
    "nodes": [{"id": 1, "label": "User", "data": {"fullName":"Andrea Santurbano"}},{"id": 2, "label": "User", "data": {"fullName":"Lee Moon Soo"}},{"id": 3, "label": "Project", "data": {"name":"Zeppelin"}}],
    "edges": [{"source": 2, "target": 1, "id" : 1, "label": "HELPS"},{"source": 2, "target": 3, "id" : 2, "label": "CREATE"},{"source": 1, "target": 3, "id" : 3, "label": "CONTRIBUTE_TO", "data": {"oldPR": "https://github.com/apache/zeppelin/pull/1582"}}],
    "labels": {"User": "#8BC34A", "Project": "#3071A9"},
    "directed": true,
    "types": ["HELPS", "CREATE", "CONTRIBUTE_TO"]
}
""")
```

that will look like:

![](assets/images/display-complex-network_5b0236f353081350.png)

---

---

<a id="usage-display_system-angular_backend"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/display_system/angular_backend.html -->

<!-- page_index: 14 -->

<a id="usage-display_system-angular_backend--backend-angular-api-in-apache-zeppelin"></a>

# Backend Angular API in Apache Zeppelin

<a id="usage-display_system-angular_backend--overview"></a>

## Overview

Angular display system treats output as a view template for [AngularJS](https://angularjs.org/).
It compiles templates and displays them inside of Apache Zeppelin. Zeppelin provides a gateway between your interpreter and your compiled **AngularJS view** templates.
Therefore, you can not only update scope variables from your interpreter but also watch them in the interpreter, which is JVM process.

<a id="usage-display_system-angular_backend--basic-usage"></a>

## Basic Usage

<a id="usage-display_system-angular_backend--print-angularjs-view"></a>

### Print AngularJS view

To use angular display system, you should start with `%angular`.
![](assets/images/display-angular_e47d082cb36cf80f.png)

Since `name` is not defined, `Hello` will display `Hello`.

> **Please Note:** Display system is backend independent.

<a id="usage-display_system-angular_backend--bind-unbind-variables"></a>

### Bind / Unbind Variables

Through **ZeppelinContext**, you can bind / unbind variables to **AngularJS view**. Currently, it only works in **Spark Interpreter ( scala )**.

```scala
// bind my 'object' as angular scope variable 'name' in current notebook.
z.angularBind(String name, Object object)

// bind my 'object' as angular scope variable 'name' in all notebooks related to current interpreter.
z.angularBindGlobal(String name, Object object)

// unbind angular scope variable 'name' in current notebook.
z.angularUnbind(String name)

// unbind angular scope variable 'name' in all notebooks related to current interpreter.
z.angularUnbindGlobal(String name)
```

Using the above example, let's bind `world` variable to `name`. Then you can see **AngularJs view** is immediately updated.

![](assets/images/display-angular1_78c23125c1941368.png)

<a id="usage-display_system-angular_backend--watch-unwatch-variables"></a>

### Watch / Unwatch Variables

Through **ZeppelinContext**, you can watch / unwatch variables in **AngularJs view**. Currently, it only works in **Spark Interpreter ( scala )**.

```scala
// register for angular scope variable 'name' (notebook)
z.angularWatch(String name, (before, after) => { ... })

// unregister watcher for angular variable 'name' (notebook)
z.angularUnwatch(String name)

// register for angular scope variable 'name' (global)
z.angularWatchGlobal(String name, (before, after) => { ... })

// unregister watcher for angular variable 'name' (global)
z.angularUnwatchGlobal(String name)
```

Let's make a button. When it is clicked, the value of `run` will be increased 1 by 1.

![](assets/images/display-angular2_0e51a5fcbb4d9d8a.png)

`z.angularBind("run", 0)` will initialize `run` to zero. And then, it will be also applied to `run` in `z.angularWatch()`.
When the button is clicked, you'll see both `run` and `numWatched` are incremented by 1.

![](assets/images/display-angular3_7adf1ef05c1562cb.png)

<a id="usage-display_system-angular_backend--let-s-make-it-simpler-and-more-intuitive"></a>

## Let's make it Simpler and more Intuitive

In this section, we will introduce a simpler and more intuitive way of using **Angular Display System** in Zeppelin.

Here are some usages.

<a id="usage-display_system-angular_backend--import"></a>

### Import

```scala
// In notebook scope
import org.apache.zeppelin.display.angular.notebookscope._
import AngularElem._

// In paragraph scope
import org.apache.zeppelin.display.angular.paragraphscope._
import AngularElem._
```

<a id="usage-display_system-angular_backend--display-element"></a>

### Display Element

```scala
// automatically convert to string and print with %angular display system directive in front.
<div></div>.display
```

<a id="usage-display_system-angular_backend--event-handler"></a>

### Event Handler

```scala
// on click
<div></div>.onClick(() => {
   my callback routine
}).display

// on change
<div></div>.onChange(() => {
  my callback routine
}).display

// arbitrary event
<div></div>.onEvent("ng-click", () => {
  my callback routine
}).display
```

<a id="usage-display_system-angular_backend--bind-model"></a>

### Bind Model

```scala
// bind model
<div></div>.model("myModel").display

// bind model with initial value
<div></div>.model("myModel", initialValue).display
```

<a id="usage-display_system-angular_backend--interact-with-model"></a>

### Interact with Model

```scala
// read model
AngularModel("myModel")()

// update model
AngularModel("myModel", "newValue")
```

<a id="usage-display_system-angular_backend--example:-basic-usage"></a>

### Example: Basic Usage

Using the above basic usages, you can apply them like below examples.

<a id="usage-display_system-angular_backend--display-elements"></a>

#### Display Elements

```scala
<div style="color:blue">
  <h4>Hello Angular Display System</h4>
</div>.display
```

<a id="usage-display_system-angular_backend--onclick-event"></a>

#### OnClick Event

```scala
<div class="btn btn-success">
  Click me
</div>.onClick{() =>
  // callback for button click
}.display
```

<a id="usage-display_system-angular_backend--bind-model-2"></a>

#### Bind Model

```scala
  <div>{{{{myModel}}}}</div>.model("myModel", "Initial Value").display
```

<a id="usage-display_system-angular_backend--interact-with-model-2"></a>

#### Interact With Model

```scala
// read the value
AngularModel("myModel")()

// update the value
AngularModel("myModel", "New value")
```

![](assets/images/basic-usage-angular_37c26e1bf3dcc054.png)

<a id="usage-display_system-angular_backend--example:-string-converter"></a>

### Example: String Converter

Using below example, you can convert the lowercase string to uppercase.

```scala
// clear previously created angular object.
AngularElem.disassociate

val button = <div class="btn btn-success btn-sm">Convert</div>.onClick{() =>
  val inputString = AngularModel("input")().toString
  AngularModel("title", inputString.toUpperCase)
}

<div>
  { <h4> {{{{title}}}}</h4>.model("title", "Please type text to convert uppercase") }
   Your text { <input type="text"></input>.model("input", "") }
  {button}
</div>.display
```

![](assets/images/string-converter-angular_25cee39290d462eb.gif)

---

---

<a id="usage-display_system-angular_frontend"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/display_system/angular_frontend.html -->

<!-- page_index: 15 -->

<a id="usage-display_system-angular_frontend--frontend-angular-api-in-apache-zeppelin"></a>

# Frontend Angular API in Apache Zeppelin

<a id="usage-display_system-angular_frontend--basic-usage"></a>

## Basic Usage

In addition to the [backend Angular API](#usage-display_system-angular_backend) to handle Angular objects binding, Apache Zeppelin also exposes a simple AngularJS `z` object on the front-end side to expose the same capabilities.
This `z` object is accessible in the Angular isolated scope for each paragraph.

<a id="usage-display_system-angular_frontend--bind-unbind-variables"></a>

### Bind / Unbind Variables

Through the **`z`**, you can bind / unbind variables to **AngularJS view**.
Bind a value to an angular object and a **mandatory** target paragraph:

```html

%angular

<form class="form-inline">
  <div class="form-group">
    <label for="superheroId">Super Hero: </label>
    <input type="text" class="form-control" id="superheroId" placeholder="Superhero name ..." ng-model="superhero"></input>
  </div>
  <button type="submit" class="btn btn-primary" ng-click="z.angularBind('superhero',superhero,'20160222-232336_1472609686')"> Bind</button>
</form>
```

![](assets/images/z-angularbind_8c7cd9699a89aa04.gif)

---

Unbind/remove a value from angular object and a **mandatory** target paragraph:

```html

%angular

<form class="form-inline">
  <button type="submit" class="btn btn-primary" ng-click="z.angularUnbind('superhero','20160222-232336_1472609686')"> UnBind</button>
</form>
```

![](assets/images/z-angularunbind_fe1e57fbb6b5303b.gif)

The signature for the **`z.angularBind() / z.angularUnbind()`** functions are:

```javascript
// Bind
z.angularBind(angularObjectName, angularObjectValue, paragraphId);

// Unbind
z.angularUnbind(angularObjectName, angularObjectValue, paragraphId);
```

All the parameters are mandatory.

<a id="usage-display_system-angular_frontend--run-paragraph"></a>

### Run Paragraph

You can also trigger paragraph execution by calling **`z.runParagraph()`** function passing the appropriate paragraphId:

```html

%angular

<form class="form-inline">
  <div class="form-group">
    <label for="paragraphId">Paragraph Id: </label>
    <input type="text" class="form-control" id="paragraphId" placeholder="Paragraph Id ..." ng-model="paragraph"></input>
  </div>
  <button type="submit" class="btn btn-primary" ng-click="z.runParagraph(paragraph)"> Run Paragraph</button>
</form>
```

![](assets/images/z-runparagraph_60426da906599a2f.gif)

<a id="usage-display_system-angular_frontend--overriding-dynamic-form-with-angular-object"></a>

## Overriding dynamic form with Angular Object

The front-end Angular Interaction API has been designed to offer richer form capabilities and variable binding. With the existing **Dynamic Form** system you can already create input text, select and checkbox forms but the choice is rather limited and the look & feel cannot be changed.

The idea is to create a custom form using plain HTML/AngularJS code and bind actions on this form to push/remove Angular variables to targeted paragraphs using this new API.

Consequently if you use the **Dynamic Form** syntax in a paragraph and there is a bound Angular object having the same name as the `${formName}`, the Angular object will have higher priority and the **Dynamic Form** will not be displayed. Example:

![](assets/images/z-angularjs-overriding-dynamic-form_d06923c572ec7916.gif)

<a id="usage-display_system-angular_frontend--feature-matrix-comparison"></a>

## Feature matrix comparison

How does the front-end AngularJS API compares to the [backend Angular API](#usage-display_system-angular_backend)? Below is a comparison matrix for both APIs:

| Actions | Front-end API | Back-end API |
| --- | --- | --- |
| Initiate binding | z.angularbind(var, initialValue, paragraphId) | z.angularBind(var, initialValue) |
| Update value | same to ordinary angularjs scope variable, or z.angularbind(var, newValue, paragraphId) | z.angularBind(var, newValue) |
| Watching value | same to ordinary angularjs scope variable | z.angularWatch(var, (oldVal, newVal) => ...) |
| Destroy binding | z.angularUnbind(var, paragraphId) | z.angularUnbind(var) |
| Executing Paragraph | z.runParagraph(paragraphId) | z.run(paragraphId) |
| Executing Paragraph (Specific paragraphs in other notes) ( |  | z.run(noteid, paragraphId) |
| Executing note |  | z.runNote(noteId) |

Both APIs are pretty similar, except for value watching where it is done naturally by AngularJS internals on the front-end and by user custom watcher functions in the back-end.

There is also a slight difference in term of scope. Front-end API limits the Angular object binding to a paragraph scope whereas back-end API allows you to bind an Angular object at the global or note scope. This restriction has been designed purposely to avoid Angular object leaks and scope pollution.

---

---

<a id="usage-interpreter-dependency_management"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/interpreter/dependency_management.html -->

<!-- page_index: 16 -->

<a id="usage-interpreter-dependency_management--dependency-management-for-interpreter"></a>

## Dependency Management for Interpreter

You can include external libraries to interpreter by setting dependencies in interpreter menu.

To be noticed, this approach doesn't work for spark and flink interpreters. They have their own dependency management, please refer their doc for details.

When your code requires external library, instead of doing download/copy/restart Zeppelin, you can easily do following jobs in this menu.

- Load libraries recursively from Maven repository
- Load libraries from local filesystem
- Add additional maven repository

---

[![](assets/images/interpreter-dependency-loading_1fd4399e4825813a.png)](assets/images/interpreter-dependency-loading_1fd4399e4825813a.png)

**Load Dependencies to Interpreter**

1. Click 'Interpreter' menu in navigation bar.
2. Click 'edit' button of the interpreter which you want to load dependencies to.
3. Fill artifact and exclude field to your needs.
   You can enter not only groupId:artifactId:version but also local file in artifact field.
4. Press 'Save' to restart the interpreter with loaded libraries.

---

[![](assets/images/interpreter-add-repo1_39b8b0c8b78be6ec.png)](assets/images/interpreter-add-repo1_39b8b0c8b78be6ec.png)
[![](assets/images/interpreter-add-repo2_f1a0bd0804c1deb8.png)](assets/images/interpreter-add-repo2_f1a0bd0804c1deb8.png)

**Add repository for dependency resolving**

1. Press  icon in 'Interpreter' menu on the top right side.
   It will show you available repository lists.
2. If you need to resolve dependencies from other than central maven repository or
   local ~/.m2 repository, hit  icon next to repository lists.
3. Fill out the form and click 'Add' button, then you will be able to see that new repository is added.
4. Optionally, if you are behind a corporate firewall, you can specify also all proxy settings so that Zeppelin can download the dependencies using the given credentials

---

---

<a id="usage-interpreter-overview"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/interpreter/overview.html -->

<!-- page_index: 17 -->

<a id="usage-interpreter-overview--interpreter-in-apache-zeppelin"></a>

# Interpreter in Apache Zeppelin

<a id="usage-interpreter-overview--overview"></a>

## Overview

In this section, we will explain the role of interpreters, interpreter groups and interpreter settings in Zeppelin.
The concept of Zeppelin interpreters allows any language or data-processing backend to be plugged into Zeppelin.
Currently, Zeppelin supports many interpreters such as Scala (with Apache Spark), Python (with Apache Spark), Spark SQL, Hive, JDBC, Markdown, Shell and so on.

<a id="usage-interpreter-overview--what-are-zeppelin-interpreters"></a>

## What are Zeppelin Interpreters ?

A Zeppelin interpreter is a plug-in which enables Zeppelin users to use a specific language/data-processing-backend. For example, to use Scala code in Zeppelin, you would use the `%spark` interpreter.

When you click the `+Create` button on the interpreter page, the interpreter drop-down list box will show all the available interpreters on your server.

![](assets/images/interpreter-create_379bfd8db9f3fcd9.png)

You can create multiple interpreters for the same engine with different interpreter setting. e.g. You can create `spark2` for Spark 2.x and create `spark1` for Spark 1.x.

For each paragraph you write in Zeppelin, you need to specify its interpreter first via `%interpreter_group.interpreter_name`. e.g. `%spark.pyspark`, `%spark.r`.

If you specify interpreter, you can also pass local properties to it (if it needs them). This is done by providing a set of key/value pairs, separated by comma, inside the round brackets right after the interpreter name. If key or value contain characters like `=`, or `,`, then you can either escape them with `\` character, or wrap the whole value inside the double quotes For example:

```
%cassandra(outputFormat=cql, dateFormat="E, d MMM yy", timeFormat=E\, d MMM yy)
```

<a id="usage-interpreter-overview--what-are-the-interpreter-settings"></a>

## What are the Interpreter Settings?

The interpreter settings are the configuration of a given interpreter on the Zeppelin server. For example, certain properties need to be set for the Apache Hive JDBC interpreter to connect to the Hive server.

![](assets/images/interpreter-setting_8272dc4553b27f81.png)

Properties are exported as environment variables on the system if the property name consists of upper-case characters, numbers or underscores ([A-Z*0-9]). Otherwise, the property is set as a common interpreter property.
e.g. You can define `SPARK*HOME`and`HADOOP*CONF*DIR` in spark's interpreter setting, they are be passed to Spark interpreter process as environment variable which is used by Spark.

You may use parameters from the context of the interpreter by adding #{contextParameterName} in the interpreter property value. The parameter can be of the following types: string, number, boolean.

<a id="usage-interpreter-overview--context-parameters"></a>

### Context Parameters

| Name | Type |
| --- | --- |
| user | string |
| noteId | string |
| replName | string |
| className | string |

If the context parameter is null, then it is replaced by an empty string. The following screenshot is one example where we make the user name as the property value of `default.user`.

![](assets/images/interpreter-setting-with-context-parameters_d86008b2cb427114.png)

<a id="usage-interpreter-overview--what-are-interpreter-groups"></a>

## What are Interpreter Groups ?

Every interpreter belongs to an **Interpreter Group**. Interpreter Groups are units of interpreters that run in one single JVM process and can be started/stopped together.
By default, every interpreter belongs to a separate group, but the group might contain more interpreters. For example, the Spark interpreter group includes Scala Spark, PySpark, IPySpark, SparkR and Spark SQL.

Technically, Zeppelin interpreters from the same group run within the same JVM. For more information about this, please consult [the documentation on writing interpreters](https://zeppelin.apache.org/docs/0.12.0/usage/development/writing_zeppelin_interpreter.html).

Each interpreter belongs to a single group and is registered together. All relevant properties are listed in the interpreter setting as in the below example.

![](assets/images/interpreter-setting-spark_99b182c173c79ab5.png)

<a id="usage-interpreter-overview--interpreter-binding-mode"></a>

## Interpreter Binding Mode

In the Interpreter Settings, one can choose one of the `shared`, `scoped`, or `isolated` interpreter binding modes.
In `shared` mode, every note/user using this interpreter will share a single interpreter instance.
`scoped` and `isolated` mode can be used under 2 dimensions: `per user` or `per note`.
e.g. In `scoped per note` mode, each note will create a new interpreter instance in the same interpreter process. In `isolated per note` mode, each note will create a new interpreter process.

For more information, please consult [Interpreter Binding Mode](#usage-interpreter-interpreter_binding_mode).

![](assets/images/interpreter-persession_b8780189d4fef900.png)

<a id="usage-interpreter-overview--interpreter-lifecycle-management"></a>

## Interpreter Lifecycle Management

Before 0.8.0, Zeppelin doesn't have lifecycle management for interpreters. Users had to shut down interpreters explicitly via the UI. Starting from 0.8.0, Zeppelin provides a new interface
`LifecycleManager` to control the lifecycle of interpreters. For now, there are two implementations: `NullLifecycleManager` and `TimeoutLifecycleManager`.

`NullLifecycleManager` will do nothing, i.e., the user needs to control the lifecycle of interpreter by themselves as before. `TimeoutLifecycleManager` will shut down interpreters after an interpreter remains idle for a while. By default, the idle threshold is 1 hour.
Users can change this threshold via the `zeppelin.interpreter.lifecyclemanager.timeout.threshold` setting. `NullLifecycleManager` is the default lifecycle manager, and users can change it via `zeppelin.interpreter.lifecyclemanager.class`.

<a id="usage-interpreter-overview--inline-generic-configuration"></a>

## Inline Generic Configuration

Zeppelin's interpreter setting is shared by all users and notes, if you want to have different settings, you have to create a new interpreter, e.g. you can create `spark_jar1` for running Spark with dependency `jar1` and `spark_jar2` for running Spark with dependency `jar2`.
This approach works, but is not convenient. Inline generic configuration can provide more fine-grained control on interpreter settings and more flexibility.

`ConfInterpreter` is a generic interpreter that can be used by any interpreter. You can use it just like defining a java property file.
It can be used to make custom settings for any interpreter. However, `ConfInterpreter` needs to run before that interpreter process is launched. When that interpreter process is launched is determined by the interpreter binding mode setting.
So users need to understand the [interpreter binding mode setting](https://zeppelin.apache.org/docs/0.12.0/usage/usage/interpreter/interpreter_bindings_mode.html) of Zeppelin and be aware of when the interpreter process is launched. E.g., if we set the Spark interpreter setting as isolated per note, then under this setting, each note will launch one interpreter process.
In this scenario, users need to put `ConfInterpreter` as the first paragraph as in the below example. Otherwise, the customized setting cannot be applied (actually it would report `ERROR`).

![](assets/images/conf-interpreter_436ae51e17a2e3ed.png)

<a id="usage-interpreter-overview--precode"></a>

## Precode

Snippet of code (language of interpreter) that executes after initialization of the interpreter depends on [Binding mode](#usage-interpreter-overview--interpreter-binding-mode). To configure, add a parameter with the class of the interpreter (`zeppelin.<ClassName>.precode`) except JDBCInterpreter ([JDBC precode](#interpreter-jdbc--usage-precode)).

![](assets/images/interpreter-precode_70107338d4a6b969.png)

<a id="usage-interpreter-overview--credential-injection"></a>

## Credential Injection

Credentials from the credential manager can be injected into Notebooks. Credential injection works by replacing the following patterns in Notebooks with matching credentials for the Credential Manager: `{CREDENTIAL_ENTITY.user}` and `{CREDENTIAL_ENTITY.password}`. However, credential injection must be enabled per Interpreter, by adding a boolean `injectCredentials` setting in the Interpreters configuration. Injected passwords are removed from Notebook output to prevent accidentally leaking passwords.

**Credential Injection Setting**
![](assets/images/credential-setting-injection_37dd502d5715b2fc.png)

**Credential Entry Example**
![](assets/images/credential-entry_69fb633c33819373.png)

**Credential Injection Example**

```scala
val password = "{SOME_CREDENTIAL_ENTITY.password}"

val username = "{SOME_CREDENTIAL_ENTITY.user}"
```

<a id="usage-interpreter-overview--interpreter-process-recovery-experimental"></a>

## Interpreter Process Recovery (Experimental)

Before 0.8.0, shutting down Zeppelin also meant to shutdown all the running interpreter processes. Usually, an administrator will shutdown the Zeppelin server for maintenance or upgrades, but would not want to shut down the running interpreter processes.
In such cases, interpreter process recovery is necessary. Starting from 0.8.0, users can enable interpreter process recovery via the setting `zeppelin.recovery.storage.class` as
`org.apache.zeppelin.interpreter.recovery.FileSystemRecoveryStorage` or other implementations if available in the future. By default it is `org.apache.zeppelin.interpreter.recovery.NullRecoveryStorage`, which means recovery is not enabled. `zeppelin.recovery.dir` is used for specify where to store the recovery metadata.
Enabling recovery means shutting down Zeppelin would not terminate interpreter processes, and when Zeppelin is restarted, it would try to reconnect to the existing running interpreter processes. If you want to kill all the interpreter processes after terminating Zeppelin even when recovery is enabled, you can run `bin/stop-interpreter.sh`.

In 0.8.x, Zeppelin server would reconnect to the running interpreter process only when you run paragraph again, but it won't recover the running paragraph. E.g. if you restart zeppelin server when some paragraph is still running, then when you restart Zeppelin, although the interpreter process is still running, you won't see the paragraph is running in frontend. In 0.9.x, we fix it by recovering the running paragraphs.
Here's one screenshot of how one running paragraph of flink interpreter works.

![](assets/images/flink-recovery_99c0604db6a19d9f.gif)

<a id="usage-interpreter-overview--choose-interpreters"></a>

## Choose Interpreters

By default, Zeppelin will register and display all the interpreters under folder `$ZEPPELIN_HOME/interpreters`.
But you can configure property `zeppelin.interpreter.include` to specify what interpreters you want to include or `zeppelin.interpreter.exclude` to specify what interpreters you want to exclude.
Only one of them can be specified, you can not specify them together.

---

---

<a id="usage-interpreter-interpreter_binding_mode"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/interpreter/interpreter_binding_mode.html -->

<!-- page_index: 18 -->

<a id="usage-interpreter-interpreter_binding_mode--interpreter-binding-mode"></a>

# Interpreter Binding Mode

<a id="usage-interpreter-interpreter_binding_mode--overview"></a>

## Overview

![](assets/images/interpreter-binding-per-note-user_7804721244c2796c.png)
![](assets/images/interpreter-binding-scoped-isolated_8a3ac243f4b84845.png)

Interpreter Process is a JVM process that communicates with Zeppelin daemon using thrift.
Each interpreter process has a single interpreter group, and this interpreter group can have one or more instances of an interpreter.
(See [here](#development-writing_zeppelin_interpreter) to understand more about its internal structure.)

Zeppelin provides 3 different modes to run interpreter process: **shared**, **scoped** and **isolated**.
Also, the user can specify the scope of these modes: **per user** or **per note**.
These 3 modes give flexibility to fit Zeppelin into any type of use cases.

In this documentation, we mainly discuss the **per note** scope in combination with the **shared**, **scoped** and **isolated** modes.

<a id="usage-interpreter-interpreter_binding_mode--shared-mode"></a>

## Shared Mode

![](assets/images/interpreter-binding-mode-shared_b4207204d917fb6a.png)

In **Shared** mode, single JVM process and a single session serves all notes. As a result, `note A` can access variables (e.g python, scala, ..) directly created from other notes..

<a id="usage-interpreter-interpreter_binding_mode--scoped-mode"></a>

## Scoped Mode

![](assets/images/interpreter-binding-mode-scoped_855f0c1d16679bce.png)

In **Scoped** mode, Zeppelin still runs a single interpreter JVM process but, in the case of **per note** scope, each note runs in its own dedicated session.
(Note it is still possible to share objects between these notes via [ResourcePool](#interpreter-spark--object-exchange))

<a id="usage-interpreter-interpreter_binding_mode--isolated-mode"></a>

## Isolated Mode

![](assets/images/interpreter-binding-mode-isolated_c3701151f71b9b5c.png)

**Isolated** mode runs a separate interpreter process for each note in the case of **per note** scope.
So, each note has an absolutely isolated session. (But it is still possible to share objects via [ResourcePool](#interpreter-spark--object-exchange))

<a id="usage-interpreter-interpreter_binding_mode--which-mode-should-i-use"></a>

## Which mode should I use?

| Mode | Each notebook... | Benefits | Disadvantages | Sharing objects |
| --- | --- | --- | --- | --- |
| **shared** | Shares a single session in a single interpreter process (JVM) | Low resource utilization and it's easy to share data between notebooks | All notebooks are affected if the interpreter process dies | Can share directly |
| **scoped** | Has its own session in the same interpreter process (JVM) | Less resource utilization than isolated mode | All notebooks are affected if the interpreter process dies | Can't share directly, but it's possible to share objects via [ResourcePool](#interpreter-spark--object-exchange) |
| **isolated** | Has its own Interpreter Process | One notebook is not affected directly by other notebooks (**per note**) | Can't share data between notebooks easily (**per note**) | Can't share directly, but it's possible to share objects via [ResourcePool](#interpreter-spark--object-exchange) |

In the case of the **per user** scope (available in a multi-user environment), Zeppelin manages interpreter sessions on a per user basis rather than a per note basis. For example:

- In **scoped + per user** mode, `User A`'s notes **might** be affected by `User B`'s notes. (e.g JVM dies, ...) Because all notes are running on the same JVM
- On the other hand, **isolated + per user** mode, `User A`'s notes will not be affected by others' notes which running on separated JVMs

Each Interpreter implementation may have different characteristics depending on the back end system that they integrate. And 3 interpreter modes can be used differently.
Let’s take a look how Spark Interpreter implementation uses these 3 interpreter modes with **per note** scope, as an example.
Spark Interpreter implementation includes 4 different interpreters in the group: Spark, SparkSQL, Pyspark and SparkR.
SparkInterpreter instance embeds Scala REPL for interactive Spark API execution.

![](assets/images/interpreter-binding-mode-example-spark-shared_6ad33aaac61c9d89.png)

In **Shared** mode, a SparkContext and a Scala REPL is being shared among all interpreters in the group.
So every note will be sharing single SparkContext and single Scala REPL.
In this mode, if `Note A` defines variable ‘a’ then `Note B` not only able to read variable ‘a’ but also able to override the variable.

![](assets/images/interpreter-binding-mode-example-spark-scoped_45d59da032de4c33.png)

In **Scoped** mode, each note has its own Scala REPL.
So variable defined in a note can not be read or overridden in another note.
However, a single SparkContext still serves all the sessions.
And all the jobs are submitted to this SparkContext and the fair scheduler schedules the jobs.
This could be useful when user does not want to share Scala session, but want to keep single Spark application and leverage its fair scheduler.

In **Isolated** mode, each note has its own SparkContext and Scala REPL.

![](assets/images/interpreter-binding-mode-example-spark-isolated_d821f758438aed57.png)

---

---

<a id="usage-interpreter-user_impersonation"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/interpreter/user_impersonation.html -->

<!-- page_index: 19 -->

<a id="usage-interpreter-user_impersonation--impersonation"></a>

# Impersonation

User impersonation enables to run zeppelin interpreter process as a web frontend user

<a id="usage-interpreter-user_impersonation--setup"></a>

## Setup

<a id="usage-interpreter-user_impersonation--linux-user"></a>

### Linux User

<a id="usage-interpreter-user_impersonation--1.-enable-shiro-auth-in-conf-shiro.ini"></a>

#### 1. Enable Shiro auth in `conf/shiro.ini`

```
[users]
user1 = password1, role1
user2 = password2, role2
```

<a id="usage-interpreter-user_impersonation--2.-enable-password-less-ssh-for-the-user-you-want-to-impersonate-say-user1-."></a>

#### 2. Enable password-less ssh for the user you want to impersonate (say user1).

```bash
adduser user1
#ssh-keygen (optional if you don't already have generated ssh-key.
ssh user1@localhost mkdir -p .ssh
cat ~/.ssh/id_rsa.pub | ssh user1@localhost 'cat >> .ssh/authorized_keys'
```

Alternatively instead of password-less, user can override ZEPPELIN*IMPERSONATE*CMD in zeppelin-env.sh

```bash
export ZEPPELIN_IMPERSONATE_CMD=(sudo -H -u "${ZEPPELIN_IMPERSONATE_USER}" bash -c)
```

<a id="usage-interpreter-user_impersonation--4.-restart-zeppelin-server."></a>

#### 4. Restart zeppelin server.

```bash
# for OSX, linux bin/zeppelin-daemon restart

# for windows bin\zeppelin.cmd
```

<a id="usage-interpreter-user_impersonation--5.-configure-impersonation-for-interpreter"></a>

#### 5. Configure impersonation for interpreter

[![](assets/images/user-impersonation_18cbf959fbc818b8.gif)](assets/images/user-impersonation_18cbf959fbc818b8.gif)

Go to interpreter setting page, and enable "User Impersonate" in any of the interpreter (in my example its shell interpreter)

<a id="usage-interpreter-user_impersonation--6.-test-with-a-simple-paragraph"></a>

#### 6. Test with a simple paragraph

```bash
%sh
whoami
```

Note that usage of "User Impersonate" option will enable Spark interpreter to use `--proxy-user` option with current user by default. If you want to disable `--proxy-user` option, then refer to `ZEPPELIN_IMPERSONATE_SPARK_PROXY_USER` variable in `conf/zeppelin-env.sh`

<a id="usage-interpreter-user_impersonation--ldap-user-with-kerberized-hdfs"></a>

### LDAP User with kerberized HDFS

<a id="usage-interpreter-user_impersonation--1.-set-the-user-zeppelin-to-be-enable-to-set-proxyuser-in-core-site.xml"></a>

#### 1. Set the user(zeppelin) to be enable to set proxyuser in `core-site.xml`

```bash
<property>
  <name>hadoop.proxyuser.zeppelin.groups</name>
  <value>*</value>
</property>
<property>
  <name>hadoop.proxyuser.zeppelin.users</name>
  <value>*</value>
</property>
<property>
  <name>hadoop.proxyuser.zeppelin.hosts</name>
  <value>*</value>
</property>
```

<a id="usage-interpreter-user_impersonation--2.-set-the-group-to-be-enable-to-connect-hive-metastore-in-core-site.xml"></a>

#### 2. Set the group to be enable to connect Hive metastore in 'core-site.xml'

```bash
<property>
  <name>hadoop.proxyuser.hive.groups</name>
  <value>zeppelin</value>
</property>
```

<a id="usage-interpreter-user_impersonation--3.-enable-kerberos-setting-in-zeppelin-site.xml"></a>

#### 3. Enable Kerberos setting in `zeppelin-site.xml`

```bash
<property>
  <name>zeppelin.server.kerberos.keytab</name>
  <value>zeppelin.keytab</value>
</property>

<property>
  <name>zeppelin.server.kerberos.principal</name>
  <value>zeppelin@principal</value>
</property>
```

<a id="usage-interpreter-user_impersonation--4.-restart-zeppelin-server.-2"></a>

#### 4. Restart zeppelin server.

```bash
# for OSX, linux bin/zeppelin-daemon restart

# for windows bin\zeppelin.cmd
```

<a id="usage-interpreter-user_impersonation--5.-configure-impersonation-for-interpreter-2"></a>

#### 5. Configure impersonation for interpreter

Option

The interpreter will be instantiated *Per User* in *isolated* process

*User impersonate*

---

---

<a id="usage-interpreter-installation"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/interpreter/installation.html -->

<!-- page_index: 20 -->

<a id="usage-interpreter-installation--installing-interpreters"></a>

# Installing Interpreters

Apache Zeppelin provides **Interpreter Installation** mechanism for whom downloaded Zeppelin `netinst` binary package, or just want to install another 3rd party interpreters.

<a id="usage-interpreter-installation--community-managed-interpreters"></a>

## Community managed interpreters

Apache Zeppelin provides several interpreters as [community managed interpreters](#usage-interpreter-installation--available-community-managed-interpreters).
If you downloaded `netinst` binary package, you need to install by using below commands.

<a id="usage-interpreter-installation--install-all-community-managed-interpreters"></a>

#### Install all community managed interpreters

```bash
./bin/install-interpreter.sh --all
```

<a id="usage-interpreter-installation--install-specific-interpreters"></a>

#### Install specific interpreters

```bash
./bin/install-interpreter.sh --name md,shell,jdbc,python
```

You can get full list of community managed interpreters by running

```bash
./bin/install-interpreter.sh --list
```

Once you have installed interpreters, you need to restart Zeppelin. And then [create interpreter setting](#usage-interpreter-overview--what-is-zeppelin-interpreter) and [bind it with your notebook](#usage-interpreter-overview--what-is-zeppelin-interpreter-setting).

<a id="usage-interpreter-installation--3rd-party-interpreters"></a>

## 3rd party interpreters

You can also install 3rd party interpreters located in the maven repository by using below commands.

<a id="usage-interpreter-installation--install-3rd-party-interpreters"></a>

#### Install 3rd party interpreters

```bash
./bin/install-interpreter.sh --name interpreter1 --artifact groupId1:artifact1:version1
```

The above command will download maven artifact `groupId1:artifact1:version1` and all of its transitive dependencies into `interpreter/interpreter1` directory.

After restart Zeppelin, then [create interpreter setting](#usage-interpreter-overview--what-is-zeppelin-interpreter) and [bind it with your note](#usage-interpreter-overview--what-is-interpreter-setting).

<a id="usage-interpreter-installation--install-multiple-3rd-party-interpreters-at-once"></a>

#### Install multiple 3rd party interpreters at once

```bash
./bin/install-interpreter.sh --name interpreter1,interpreter2 --artifact groupId1:artifact1:version1,groupId2:artifact2:version2
```

`--name` and `--artifact` arguments will recieve comma separated list.

<a id="usage-interpreter-installation--available-community-managed-interpreters"></a>

## Available community managed interpreters

You can also find the below community managed interpreter list in `conf/interpreter-list` file.

| Name | Maven Artifact | Description |
| --- | --- | --- |
| alluxio | org.apache.zeppelin:zeppelin-alluxio:0.12.0 | Alluxio interpreter |
| angular | org.apache.zeppelin:zeppelin-angular:0.12.0 | HTML and AngularJS view rendering |
| bigquery | org.apache.zeppelin:zeppelin-bigquery:0.12.0 | BigQuery interpreter |
| cassandra | org.apache.zeppelin:zeppelin-cassandra:0.12.0 | Cassandra interpreter |
| elasticsearch | org.apache.zeppelin:zeppelin-elasticsearch:0.12.0 | Elasticsearch interpreter |
| file | org.apache.zeppelin:zeppelin-file:0.12.0 | HDFS file interpreter |
| flink | org.apache.zeppelin:zeppelin-flink:0.12.0 | Flink interpreter |
| hbase | org.apache.zeppelin:zeppelin-hbase:0.12.0 | Hbase interpreter |
| groovy | org.apache.zeppelin:zeppelin-groovy:0.12.0 | Groovy interpreter |
| java | org.apache.zeppelin:zeppelin-java:0.12.0 | Java interpreter |
| jdbc | org.apache.zeppelin:zeppelin-jdbc:0.12.0 | Jdbc interpreter |
| livy | org.apache.zeppelin:zeppelin-livy:0.12.0 | Livy interpreter |
| md | org.apache.zeppelin:zeppelin-markdown:0.12.0 | Markdown support |
| neo4j | org.apache.zeppelin:zeppelin-neo4j:0.12.0 | Neo4j interpreter |
| python | org.apache.zeppelin:zeppelin-python:0.12.0 | Python interpreter |
| shell | org.apache.zeppelin:zeppelin-shell:0.12.0 | Shell command |
| sparql | org.apache.zeppelin:zeppelin-sparql:0.12.0 | Sparql interpreter |

---

---

<a id="usage-interpreter-execution_hooks"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/interpreter/execution_hooks.html -->

<!-- page_index: 21 -->

<a id="usage-interpreter-execution_hooks--interpreter-execution-hooks-experimental"></a>

# Interpreter Execution Hooks (Experimental)

<a id="usage-interpreter-execution_hooks--overview"></a>

## Overview

Apache Zeppelin allows for users to specify additional code to be executed by an interpreter at pre and post-paragraph code execution.
This is primarily useful if you need to run the same set of code for all of the paragraphs within your notebook at specific times.
Currently, this feature is only available for the spark and pyspark interpreters.
To specify your hook code, you may use `z.registerHook()`.
For example, enter the following into one paragraph:

```python
%pyspark
z.registerHook("post_exec", "print 'This code should be executed before the parapgraph code!'")
z.registerHook("pre_exec", "print 'This code should be executed after the paragraph code!'")
```

These calls will not take into effect until the next time you run a paragraph.

In another paragraph, enter

```python
%pyspark
print "This code should be entered into the paragraph by the user!"
```

The output should be:

```
This code should be executed before the paragraph code!
This code should be entered into the paragraph by the user!
This code should be executed after the paragraph code!
```

If you ever need to know the hook code, use `z.getHook()`:

```python
%pyspark
print z.getHook("post_exec")

print 'This code should be executed after the paragraph code!'
```

Any call to `z.registerHook()` will automatically overwrite what was previously registered.
To completely unregister a hook event, use `z.unregisterHook(eventCode)`.
Currently only `"post_exec"` and `"pre_exec"` are valid event codes for the Zeppelin Hook Registry system.

Finally, the hook registry is internally shared by other interpreters in the same group.
This would allow for hook code for one interpreter REPL to be set by another as follows:

```scala
%spark
z.unregisterHook("post_exec", "pyspark")
```

The API is identical for both the spark (scala) and pyspark (python) implementations.

<a id="usage-interpreter-execution_hooks--caveats"></a>

### Caveats

Calls to `z.registerHook("pre_exec", ...)` should be made with care. If there are errors in your specified hook code, this will cause the interpreter REPL to become unable to execute any code pass the pre-execute stage making it impossible for direct calls to `z.unregisterHook()` to take into effect. Current workarounds include calling `z.unregisterHook()` from a different interpreter REPL in the same interpreter group (see above) or manually restarting the interpreter group in the UI.

---

---

<a id="usage-other_features-publishing_paragraphs"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/other_features/publishing_paragraphs.html -->

<!-- page_index: 22 -->

<a id="usage-other_features-publishing_paragraphs--how-can-you-publish-your-paragraphs"></a>

# How can you publish your paragraphs?

Apache Zeppelin provides a feature for publishing your notebook paragraph results. Using this feature, you can show Zeppelin notebook paragraph results in your own website.
It's very straightforward. Just use `<iframe>` tag in your page.

<a id="usage-other_features-publishing_paragraphs--copy-a-paragraph-link"></a>

## Copy a Paragraph Link

A first step to publish your paragraph result is **Copy a Paragraph Link**.

- After running a paragraph in your Zeppelin notebook, click a gear button located on the right side. Then, click **Link this Paragraph** menu like below image.
  ![](assets/images/link-the-paragraph_6478d9e37f733ca7.png)
- Just copy the provided link.
  ![](assets/images/copy-the-link_18dcd211ae5ebce7.png)

<a id="usage-other_features-publishing_paragraphs--embed-the-paragraph-to-your-website"></a>

## Embed the Paragraph to Your Website

For publishing the copied paragraph, you may use `<iframe>` tag in your website page.
For example,

```
<iframe src="http://< ip-address >:< port >/#/notebook/2B3QSZTKR/paragraph/...?asIframe" height="" width="" ></iframe>
```

Finally, you can show off your beautiful visualization results in your website.
![](assets/images/your-website_0b54e538726fa04b.png)

>
> [!NOTE]
> : To embed the paragraph in a website, Apache Zeppelin needs to be reachable by that website. And please use this feature with caution and in a trusted environment only, as Zeppelin entire Webapp could be accessible by whoever visits your website.

---

---

<a id="usage-other_features-personalized_mode"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/other_features/personalized_mode.html -->

<!-- page_index: 23 -->

<a id="usage-other_features-personalized_mode--what-is-personalized-mode"></a>

# What is Personalized Mode?

Personalize your analysis result by switching the note to Personal Mode.

This enables two different users to change the view of the same paragraph's result with different view even owner change paragraph and run it again.

Currently, this feature is experimental. If you find any issues, please report them in
[Apache Zeppelin JIRA](https://issues.apache.org/jira/browse/ZEPPELIN)

---

---

<a id="usage-other_features-customizing_homepage"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/other_features/customizing_homepage.html -->

<!-- page_index: 24 -->

<a id="usage-other_features-customizing_homepage--customizing-apache-zeppelin-homepage"></a>

# Customizing Apache Zeppelin homepage

Apache Zeppelin allows you to use one of the notes you create as your Zeppelin Homepage.
With that you can brand your Zeppelin installation, adjust the instruction to your users needs and even translate to other languages.

<a id="usage-other_features-customizing_homepage--how-to-set-a-note-as-your-zeppelin-homepage"></a>

## How to set a note as your Zeppelin homepage

The process for creating your homepage is very simple as shown below:

1. Create a note using Zeppelin
2. Set the note id in the config file
3. Restart Zeppelin

<a id="usage-other_features-customizing_homepage--create-a-note-using-zeppelin"></a>

### Create a note using Zeppelin

Create a new note using Zeppelin, you can use `%md` interpreter for markdown content or any other interpreter you like.
You can also use the display system to generate [text](#usage-display_system-basic--text), [html](#usage-display_system-basic--html), [table](#usage-display_system-basic--table) or
Angular ([backend API](#usage-display_system-angular_backend), [frontend API](#usage-display_system-angular_frontend)).

Run (shift+Enter) the note and see the output. Optionally, change the note view to report to hide
the code sections.

<a id="usage-other_features-customizing_homepage--set-the-note-id-in-the-config-file"></a>

### Set the note id in the config file

To set the note id in the config file, you should copy it from the last word in the note url.
For example,

![](assets/images/homepage-notebook-id_a66ffcb3ccb6183e.png)

Set the note id to the `ZEPPELIN_NOTEBOOK_HOMESCREEN` environment variable
or `zeppelin.notebook.homescreen` property.

You can also set the `ZEPPELIN_NOTEBOOK_HOMESCREEN_HIDE` environment variable
or `zeppelin.notebook.homescreen.hide` property to hide the new note from the note list.

<a id="usage-other_features-customizing_homepage--restart-zeppelin"></a>

### Restart Zeppelin

Restart your Zeppelin server

```bash
./bin/zeppelin-daemon stop
./bin/zeppelin-daemon start
```

That's it! Open your browser and navigate to Apache Zeppelin and see your customized homepage.

<a id="usage-other_features-customizing_homepage--show-note-list-in-your-custom-homepage"></a>

## Show note list in your custom homepage

If you want to display the list of notes on your custom Apache Zeppelin homepage all
you need to do is use our %angular support.

Add the following code to a paragraph in your Apache Zeppelin note and run it.

```javascript
%spark

println(
"""%angular
  <div ng-include="'app/home/notebook.html'"></div>
""")
```

After running the paragraph, you will see output similar to this one:

![](assets/images/homepage-custom-notebook-list_7c0901fec11642b9.png)

That's it! Voila! You have your note list.

---

---

<a id="usage-other_features-notebook_actions"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/other_features/notebook_actions.html -->

<!-- page_index: 25 -->

<a id="usage-other_features-notebook_actions--revisions-comparator"></a>

# Revisions comparator

Apache Zeppelin allows you to compare revisions of notebook.
To see which paragraphs have been changed, removed or added.
This action becomes available if your notebook has more than one revision.

![](assets/images/revisions-comparator-button_ed92a270cd8025d2.png)
<a id="usage-other_features-notebook_actions--how-to-compare-two-revisions"></a>

## How to compare two revisions

For compare two revisions need open dialog of comparator (by click button) and click on any revision in the table.

![](assets/images/revisions-comparator-table_9d3641b812066809.png)

Or choose two revisions into comboboxes.

![](assets/images/revisions-comparator-comboboxes_48c955ba119ac4e7.png)

After click on any revision in the table or selecting the second revision will see the result of the comparison.

![](assets/images/revisions-comparator-diff_bf40c5139f2bced9.png)
<a id="usage-other_features-notebook_actions--how-to-read-the-result-of-the-comparison"></a>

## How to read the result of the comparison

Result it is list of paragraphs which was in both revisions. If paragraph was added in second revision ("Head")
then so it will be marked as *added*, if was deleted then it will be marked as
*deleted*. If paragraph exists in both revisions then it marked as *there are differences*.
To view the comparison click on the section.

![](assets/images/revisions-comparator-paragraph_6a3ba22077379166.png)

Сhanges in the text of the paragraph are highlighted in green and red. Red it is line (block of lines) which was deleted, green it is line (block of lines) which was added).

---

---

<a id="usage-other_features-cron_scheduler"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/other_features/cron_scheduler.html -->

<!-- page_index: 26 -->

<a id="usage-other_features-cron_scheduler--running-a-notebook-on-a-given-schedule-automatically"></a>

# Running a Notebook on a Given Schedule Automatically

Apache Zeppelin provides a cron scheduler for each notebook. You can run a notebook on a given schedule automatically by setting up a cron scheduler on the notebook.

<a id="usage-other_features-cron_scheduler--setting-up-a-cron-scheduler-on-a-notebook"></a>

## Setting up a cron scheduler on a notebook

Click the clock icon on the tool bar and open a cron scheduler dialog box.

![](assets/images/cron-scheduler-dialog-box_a8eb00ed3baaffce.png)

There are the following items which you can input or set:

<a id="usage-other_features-cron_scheduler--preset"></a>

### Preset

You can set a cron schedule easily by clicking each option such as `1m` and `5m`. The login user is set as a cron executing user automatically. You can also clear the cron schedule settings by clicking `None`.

<a id="usage-other_features-cron_scheduler--cron-expression"></a>

### Cron expression

You can set the cron schedule by filling in this form. Please see [Cron Trigger Tutorial](https://www.quartz-scheduler.org/documentation/quartz-2.2.2/tutorials/tutorial-lesson-06.html) for the available cron syntax.

<a id="usage-other_features-cron_scheduler--cron-executing-user-it-is-removed-from-0.8-where-it-enforces-the-cron-execution-user-to-be-the-note-owner-for-security-purpose"></a>

### Cron executing user (It is removed from 0.8 where it enforces the cron execution user to be the note owner for security purpose)

You can set the cron executing user by filling in this form and press the enter key.

<a id="usage-other_features-cron_scheduler--after-execution-stop-the-interpreter"></a>

### After execution stop the interpreter

When this checkbox is set to "on", the interpreters which are binded to the notebook are stopped automatically after the cron execution. This feature is useful if you want to release the interpreter resources after the cron execution.

>
> [!NOTE]
> : A cron execution is skipped if one of the paragraphs is in a state of `RUNNING` or `PENDING` no matter whether it is executed automatically (i.e. by the cron scheduler) or manually by a user opening this notebook.

<a id="usage-other_features-cron_scheduler--enable-cron"></a>

### Enable cron

Set property **zeppelin.notebook.cron.enable** to **true** in `$ZEPPELIN_HOME/conf/zeppelin-site.xml` to enable Cron feature.

<a id="usage-other_features-cron_scheduler--run-cron-selectively-on-folders"></a>

### Run cron selectively on folders

In `$ZEPPELIN_HOME/conf/zeppelin-site.xml` make sure the property **zeppelin.notebook.cron.enable** is set to **true**, and then set property **zeppelin.notebook.cron.folders** to the desired folder as comma-separated values, e.g. `/cron,/test/cron`.

---

---

<a id="usage-other_features-zeppelin_context"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/other_features/zeppelin_context.html -->

<!-- page_index: 27 -->

<a id="usage-other_features-zeppelin_context--zeppelin-context"></a>

# Zeppelin-Context

The zeppelin-context is a system-wide container for common utility functions and
user-specific data. It implements functions for data input, data display, etc. that are
often needed but are not uniformly available in all interpreters.
Its single per-user instance is accessible across all of the user's notebooks and cells, enabling data exchange between cells - even in different notebooks.
But the way in which the zeppelin-context is used, and the functionality available differs
depending on whether or not the associated interpreter is based on a programming language.
Details of how the zeppelin-context is used for different purposes and in different
environments is described below.

<a id="usage-other_features-zeppelin_context--usage-in-programming-language-cells"></a>

## Usage in Programming Language Cells

In many programming-language interpreters (e.g. Apache Spark, Python, R) the zeppelin-context is available
as a predefined variable `z` that can be used by directly invoking its methods.
The methods available on the `z` object are described below.
Other interpreters based on programming languages. also provide the predefined variable `z`.

<a id="usage-other_features-zeppelin_context--exploring-spark-dataframes"></a>

### Exploring Spark DataFrames

In the Apache Spark interpreter, the zeppelin-context provides a `show` method, which, using Zeppelin's `table` feature, can be used to nicely display a Spark DataFrame:

```scala
df = spark.read.csv('/path/to/csv')
z.show(df)
```

This display functionality using the `show` method is planned to be extended uniformly to
other interpreters that can access the `z` object (Flink already support to show table too).

<a id="usage-other_features-zeppelin_context--object-exchange"></a>

### Object Exchange

`ZeppelinContext` extends map and it's shared between the Apache Spark and Python environments.
So you can put some objects using Scala (in an Apache Spark cell) and read it from Python, and vice versa.

```scala
// Put/Get object from scala
%spark

val myObject = "hello"
z.put("objName", myObject)
z.get("objName")
```

```python
# Put/Get object from python
%spark.pyspark

val myObject = "hello"
z.put("objName", myObject)
myObject = z.get("objName")

# df is Python pandas DataFrame
# "table_name" must be table type. Currently only sql interpreter (%spark.sql or %jdbc) result is supported.
df = z.getAsDataFrame("table_name")
```

```python
# Get/Put object from R
%spark.r

z.put("objName", myObject)
myObject <- z.get("objName")

# df is R DataFrame
# "table_name" must be table type. Currently only sql interpreter (%spark.sql or %jdbc) result is supported.
df <- z.getAsDataFrame("table_name")
```

Currently, there're two types of data could be shared across interpreters:

- String Data
- Table Data

<a id="usage-other_features-zeppelin_context--share-string-object"></a>

#### Share String Object

Here's one example we share one String object `maxAge` between Spark interpreter and jdbc interpreter.

```scala
%spark

z.put("maxAge", 83)
```

```sql
%jdbc(interpolate=true)

select * from bank where age = {maxAge}
```

![](assets/images/zeppelin-context-share-string_e02d6aaf774840b5.png)

<a id="usage-other_features-zeppelin_context--share-table-object"></a>

#### Share Table Object

Here's one example we share one Table object between jdbc interpreter and python interpreter.

```sql
%jdbc(saveAs=bank)

select * from bank
```

```python
%python.ipython

%matplotlib inline

import warnings
warnings.filterwarnings("ignore")
from plotnine import ggplot, geom_histogram, aes, facet_wrap

bank = z.getAsDataFrame('bank')
(ggplot(bank, aes(x='age'))
```

![](assets/images/zeppelin-context-share-table_a1fce514117bc142.png)

<a id="usage-other_features-zeppelin_context--form-creation"></a>

### Form Creation

`ZeppelinContext` provides functions for creating forms.
In Scala and Python environments, you can create forms programmatically.

```scala
%spark

/* Create text input form */
z.input("input_1")

/* Create text input form with default value */
z.input("input_2", "defaultValue")

/* Create select form */
z.select("select_1", Seq(("option1", "option1DisplayName"),
                         ("option2", "option2DisplayName")))

/* Create select form with default value*/
z.select("select_2", "option1", Seq(("option1", "option1DisplayName"),
                                    ("option2", "option2DisplayName")))
```

```python
%spark.pyspark

# Create text input form
z.input("input_1")

# Create text input form with default value
z.input("input_2", "defaultValue")

# Create select form
z.select("select_1", [("option1", "option1DisplayName"),
                      ("option2", "option2DisplayName")])

# Create select form with default value
z.select("select_2", [("option1", "option1DisplayName"),
                      ("option2", "option2DisplayName")], "option1")
```

Patterns of the form ${ ... } are used to dynamically create additional HTML elements
for requesting user input (that replaces the corresponding pattern in the paragraph text).
Currently only [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/text), [select](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) with
[options](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option), and
[checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox) are supported.

Dynamic forms are described in detail here: [Dynamic Form](https://zeppelin.apache.org/docs/0.12.0/usage/usage/dynamic_form/intro.html).

In sql environment, you can create dynamic form in simple template.

```sql
%spark.sql

select * from ${table=defaultTableName} where text like '%${search}%'
```

To learn more about dynamic form, checkout [Dynamic Form](https://zeppelin.apache.org/docs/0.12.0/usage/usage/dynamic_form/intro.html).

<a id="usage-other_features-zeppelin_context--usage-with-embedded-commands"></a>

## Usage with Embedded Commands

In certain interpreters (see table below) zeppelin-context features may be invoked by embedding
command strings into the paragraph text. Such embedded command strings are used to invoke
dynamic-forms and object-interpolation as described below.

Interpreters that use Embedded Commands

spark.sql (\*), bigquery, cassandra, elasticsearch, file, hbase, jdbc (\*), livy, markdown, neo4j, python, shell (\*), zengine

Dynamic forms are available in all of the interpreters in the table above, but object interpolation is only available in a small, but growing, list of interpreters
(marked with an asterisk in the table above).
Both these zeppelin-context features are described below.

<a id="usage-other_features-zeppelin_context--object-interpolation"></a>

### Object Interpolation

Some interpreters can interpolate object values from `z` into the paragraph text by using the
`{variable-name}` syntax. The value of any object previously `put` into `z` can be
interpolated into a paragraph text by using such a pattern containing the object's name.
The following example shows one use of this facility:

<a id="usage-other_features-zeppelin_context--in-scala-cell:"></a>

#### In Scala cell:

```scala
%spark

z.put("minAge", 35)
```

<a id="usage-other_features-zeppelin_context--in-later-sql-cell:"></a>

#### In later SQL cell:

```sql
%spark.sql

select * from members where age >= {minAge}
```

The interpolation of a `{var-name}` pattern is performed only when `z` contains an object with the specified name.
But the pattern is left unchanged if the named object does not exist in `z`.
Further, all `{var-name}` patterns within the paragraph text must be translatable for any interpolation to occur --
translation of only some of the patterns in a paragraph text is never done.

In some situations, it is necessary to use { and } characters in a paragraph text without invoking the
object interpolation mechanism. For these cases an escaping mechanism is available --
doubled braces should be used. The following example shows the use of for passing a
regular expression containing just { and } into the paragraph text.

```sql
%spark.sql

select * from members where name rlike '[aeiou]{{3}}'
```

To summarize, patterns of the form `{var-name}` within the paragraph text will be interpolated only if a predefined
object of the specified name exists. Additionally, all such patterns within the paragraph text should also
be translatable for any interpolation to occur. Patterns of the form `{{any-text}}` are translated into `{any-text}`.
These translations are performed only when all occurrences of `{`, `}`, `{{`, and `}}` in the paragraph text conform
to one of the two forms described above. Paragraph text containing `{` and/or `}` characters used in any other way
(than `{var-name}` and `{{any-text}}` ) is used as-is without any changes.
No error is flagged in any case. This behavior is identical to the implementation of a similar feature in
Jupyter's shell invocation using the `!` magic command.

This feature is disabled by default, and must be explicitly turned on for each interpreter independently
by setting the value of an interpreter-specific property to `true`.
Consult the *Configuration* section of each interpreter's documentation
to find out if object interpolation is implemented, and the name of the parameter that must be set to `true` to
enable the feature. The name of the parameter used to enable this feature is different for each interpreter.
For example, the SparkSQL and Shell interpreters use the parameter names `zeppelin.spark.sql.interpolation` and
`zeppelin.shell.interpolation` respectively.

At present only the SparkSQL, JDBC, and Shell interpreters support object interpolation.

<a id="usage-other_features-zeppelin_context--interpreter-specific-functions"></a>

### Interpreter-Specific Functions

Some interpreters use a subclass of `BaseZepplinContext` augmented with interpreter-specific functions.
Such interpreter-specific functions are described within each interpreter's documentation.

---

<a id="usage-rest_api-zeppelin_server"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/rest_api/zeppelin_server.html -->

<!-- page_index: 28 -->

<a id="usage-rest_api-zeppelin_server--apache-zeppelin-server-rest-api"></a>

# Apache Zeppelin Server REST API

<a id="usage-rest_api-zeppelin_server--overview"></a>

## Overview

Apache Zeppelin provides several REST APIs for interaction and remote activation of zeppelin functionality.
All REST APIs are available starting with the following endpoint `http://[zeppelin-server]:[zeppelin-port]/api`.
Note that Apache Zeppelin REST APIs receive or return JSON objects, it is recommended for you to install some JSON viewers such as [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).

If you work with Apache Zeppelin and find a need for an additional REST API, please [file an issue or send us an email](http://zeppelin.apache.org/community.html).

<a id="usage-rest_api-zeppelin_server--zeppelin-server-rest-api-list"></a>

## Zeppelin Server REST API list

<a id="usage-rest_api-zeppelin_server--get-zeppelin-version"></a>

### Get Zeppelin version

| Description | This `GET` method returns Zeppelin version |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/version` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK","message": "Zeppelin version","body": [{"version": "0.8.0","git-commit-id": "abc0123","git-timestamp": "2017-01-02 03:04:05"}]}
```

<a id="usage-rest_api-zeppelin_server--change-the-log-level-of-zeppelin-server"></a>

### Change the log level of Zeppelin Server

| Description | This `PUT` method is used to update the root logger's log level of the server. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/log/level/<LOG_LEVEL>` |
| Success code | 200 |
| Fail code | 406 |
| sample JSON response |  |

```json
{
  "status": "OK"
}
```

|  |  |
| --- | --- |
| sample error JSON response |  |

```json
{
  "status":"NOT_ACCEPTABLE",
  "message":"Please check LOG level specified. Valid values: DEBUG, ERROR, FATAL, INFO, TRACE, WARN"
}
```

---

---

<a id="usage-rest_api-interpreter"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/rest_api/interpreter.html -->

<!-- page_index: 29 -->

<a id="usage-rest_api-interpreter--apache-zeppelin-interpreter-rest-api"></a>

# Apache Zeppelin Interpreter REST API

<a id="usage-rest_api-interpreter--overview"></a>

## Overview

Apache Zeppelin provides several REST APIs for interaction and remote activation of zeppelin functionality.
All REST APIs are available starting with the following endpoint `http://[zeppelin-server]:[zeppelin-port]/api`.
Note that Apache Zeppelin REST APIs receive or return JSON objects, it is recommended for you to install some JSON viewers such as [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).

If you work with Apache Zeppelin and find a need for an additional REST API, please [file an issue or send us an email](http://zeppelin.apache.org/community.html).

<a id="usage-rest_api-interpreter--interpreter-rest-api-list"></a>

## Interpreter REST API List

The role of registered interpreters, settings and interpreters group are described in [here](#usage-interpreter-overview).

<a id="usage-rest_api-interpreter--list-of-registered-interpreters"></a>

### List of registered interpreters

<table class="table-configuration">
<col width="200"/>
<tr>
<td>Description</td>
<td>This <code>GET</code> method returns all the registered interpreters available on the server.</td>
</tr>
<tr>
<td>URL</td>
<td><code>http://[zeppelin-server]:[zeppelin-port]/api/interpreter</code></td>
</tr>
<tr>
<td>Success code</td>
<td>200</td>
</tr>
<tr>
<td>Fail code</td>
<td> 500 </td>
</tr>
<tr>
<td>Sample JSON response</td>
<td></td></tr></table>

```json
{"status": "OK","message": "","body": {"md.md": {"name": "md","group": "md","className": "org.apache.zeppelin.markdown.Markdown","properties": {},"path": "/zeppelin/interpreter/md" },"spark.spark": {"name": "spark","group": "spark","className": "org.apache.zeppelin.spark.SparkInterpreter","properties": {"spark.executor.memory": {"name": "spark.executor.memory","defaultValue": "1g","description": "Executor memory per worker instance. ex) 512m, 32g","type": "string" },"spark.cores.max": {"defaultValue": "","description": "Total number of cores to use. Empty value uses all available core.","type": "number" },},"path": "/zeppelin/interpreter/spark" },"spark.sql": {"name": "sql","group": "spark","className": "org.apache.zeppelin.spark.SparkSqlInterpreter","properties": {"zeppelin.spark.maxResult": {"name": "zeppelin.spark.maxResult","defaultValue": "1000","description": "Max number of Spark SQL result to display.","type": "number"} },"path": "/zeppelin/interpreter/spark"}}}
```

<a id="usage-rest_api-interpreter--list-of-registered-interpreter-settings"></a>

### List of registered interpreter settings

<table class="table-configuration">
<col width="200"/>
<tr>
<td>Description</td>
<td>This <code>GET</code> method returns all the interpreters settings registered on the server.</td>
</tr>
<tr>
<td>URL</td>
<td><code>http://[zeppelin-server]:[zeppelin-port]/api/interpreter/setting</code></td>
</tr>
<tr>
<td>Success code</td>
<td>200</td>
</tr>
<tr>
<td>Fail code</td>
<td> 500 </td>
</tr>
<tr>
<td>Sample JSON response</td>
<td></td></tr></table>

```json
{"status": "OK","message": "","body": [{"id": "2AYUGP2D5","name": "md","group": "md","properties": {"_empty_": "" },"interpreterGroup": [{"class": "org.apache.zeppelin.markdown.Markdown","name": "md"} ],"dependencies": [] },{"id": "2AY6GV7Q3","name": "spark","group": "spark","properties": {"spark.cores.max": {"name": "","value": "spark.cores.max","type": "number" },"spark.executor.memory": {"name": "spark.executor.memory","value": "1g","type": "string"} },"interpreterGroup": [{"class": "org.apache.zeppelin.spark.SparkInterpreter","name": "spark" },{"class": "org.apache.zeppelin.spark.SparkSqlInterpreter","name": "sql"} ],"dependencies": [{"groupArtifactVersion": "com.databricks:spark-csv_2.10:1.3.0"}]}]}
```

<a id="usage-rest_api-interpreter--get-a-registered-interpreter-setting-by-the-setting-id"></a>

### Get a registered interpreter setting by the setting id

| Description | This `GET` method returns a registered interpreter setting on the server. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/setting/[setting ID]` |
| Success code | 200 |
| Fail code | 400 if such interpreter setting id does not exist 500 for any other errors |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": {"id": "2AYW25ANY","name": "Markdown setting name","group": "md","properties": {"propname": {"name": "propname","value": "propvalue","type": "textarea"} },"interpreterGroup": [{"class": "org.apache.zeppelin.markdown.Markdown","name": "md"} ],"dependencies": [{"groupArtifactVersion": "groupId:artifactId:version","exclusions": ["groupId:artifactId"]}]}}
```

<a id="usage-rest_api-interpreter--create-a-new-interpreter-setting"></a>

### Create a new interpreter setting

Description

This `POST` method adds a new interpreter setting using a registered interpreter to the server.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/interpreter/setting`

Success code

200

Fail code

400 if the input json is empty
500 for any other errors

Sample JSON input

```json
{"name": "Markdown setting name","group": "md","properties": {"propname": {"name": "propname","value": "propvalue","type": "textarea" },"interpreterGroup": [{"class": "org.apache.zeppelin.markdown.Markdown","name": "md"} ],"dependencies": [{"groupArtifactVersion": "groupId:artifactId:version","exclusions": ["groupId:artifactId"]}]}
```

|  |  |
| --- | --- |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": {"id": "2AYW25ANY","name": "Markdown setting name","group": "md","properties": {"propname": {"name": "propname","value": "propvalue","type": "textarea" },"interpreterGroup": [{"class": "org.apache.zeppelin.markdown.Markdown","name": "md"} ],"dependencies": [{"groupArtifactVersion": "groupId:artifactId:version","exclusions": ["groupId:artifactId"]}]}}
```

<a id="usage-rest_api-interpreter--update-an-interpreter-setting"></a>

### Update an interpreter setting

| Description | This `PUT` method updates an interpreter setting with new properties. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/setting/[interpreter ID]` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON input |  |

```json
{"name": "Markdown setting name","group": "md","properties": {"propname": {"name": "propname","value": "Otherpropvalue","type": "textarea" },"interpreterGroup": [{"class": "org.apache.zeppelin.markdown.Markdown","name": "md"} ],"dependencies": [{"groupArtifactVersion": "groupId:artifactId:version","exclusions": ["groupId:artifactId"]}]}
```

|  |  |
| --- | --- |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": {"id": "2AYW25ANY","name": "Markdown setting name","group": "md","properties": {"propname": {"name": "propname","value": "Otherpropvalue","type": "textarea" },"interpreterGroup": [{"class": "org.apache.zeppelin.markdown.Markdown","name": "md"} ],"dependencies": [{"groupArtifactVersion": "groupId:artifactId:version","exclusions": ["groupId:artifactId"]}]}}
```

<a id="usage-rest_api-interpreter--delete-an-interpreter-setting"></a>

### Delete an interpreter setting

| Description | This `DELETE` method deletes an given interpreter setting. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/setting/[interpreter ID]` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-interpreter--restart-an-interpreter"></a>

### Restart an interpreter

| Description | This `PUT` method restarts the given interpreter id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/setting/restart/[interpreter ID]` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON input (Optional) |  |

```json
{
  "noteId": "2AVQJVC8N"
}
```

|  |  |
| --- | --- |
| Sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-interpreter--add-a-new-repository-for-dependency-resolving"></a>

### Add a new repository for dependency resolving

| Description | This `POST` method adds new repository. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/repository` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON input |  |

```json
{
  "id": "securecentral",
  "url": "https://repo1.maven.org/maven2",
  "snapshot": false
}
```

|  |  |
| --- | --- |
| Sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-interpreter--delete-a-repository-for-dependency-resolving"></a>

### Delete a repository for dependency resolving

| Description | This `DELETE` method delete repository with given id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/repository/[repository ID]` |
| Success code | 200 |
| Fail code | 500 |

<a id="usage-rest_api-interpreter--get-available-types-for-property"></a>

### Get available types for property

| Description | This `GET` method returns available types for interpreter property. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/property/types` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{
  "status": "OK",
  "body": [ "textarea", "string", ...
  ]
}
```

<a id="usage-rest_api-interpreter--get-interpreter-settings-metadata-info"></a>

### Get interpreter settings metadata info

| Description | This `GET` method returns interpreter settings metadata info. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/interpreter/metadata/[setting ID]` |
| Success code | 200 |
| Fail code | 500 |

---

---

<a id="usage-rest_api-notebook"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/rest_api/notebook.html -->

<!-- page_index: 30 -->

<a id="usage-rest_api-notebook--apache-zeppelin-notebook-rest-api"></a>

# Apache Zeppelin Notebook REST API

<a id="usage-rest_api-notebook--overview"></a>

## Overview

Apache Zeppelin provides several REST APIs for interaction and remote activation of zeppelin functionality.
All REST APIs are available starting with the following endpoint `http://[zeppelin-server]:[zeppelin-port]/api`.
Note that Apache Zeppelin REST APIs receive or return JSON objects, it is recommended for you to install some JSON viewers such as [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).
If you work with Apache Zeppelin and find a need for an additional REST API, please [file an issue or send us an email](http://zeppelin.apache.org/community.html).

Notebooks REST API supports the following operations: List, Create, Get, Delete, Clone, Run, Export, Import as detailed in the following tables.

<a id="usage-rest_api-notebook--note-operations"></a>

## Note operations

<a id="usage-rest_api-notebook--list-of-the-notes"></a>

### List of the notes

Description

This `GET` method lists the available notes on your server.
Notebook JSON contains the `name` and `id` of all notes.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook`

Success code

200

Fail code

500

sample JSON response

```json
{"status": "OK","message": "","body": [{"path":"Homepage","id":"2AV4WUEMK" },{"path":"Zeppelin Tutorial","id":"2A94M5J1Z"}]}
```

<a id="usage-rest_api-notebook--create-a-new-note"></a>

### Create a new note

Description

This `POST` method creates a new note using the given name or default name if none given.
The body field of the returned JSON contains the new note id.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook`

Success code

200

Fail code

500

sample JSON input (without paragraphs)

```json
{"name": "name of new note"}
```

|  |  |
| --- | --- |
| sample JSON input (with initial paragraphs) |  |

```json
{"name": "name of new note","paragraphs": [{"title": "paragraph title1","text": "paragraph text1" },{"title": "paragraph title2","text": "paragraph text2","config": {"title": true,"colWidth": 6.0,"results": [{"graph": {"mode": "scatterChart","optionOpen": true}}]}}]}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{
  "status": "OK",
  "message": "",
  "body": "2AZPHY918"
}
```

<a id="usage-rest_api-notebook--get-the-status-of-all-paragraphs"></a>

### Get the status of all paragraphs

Description

This `GET` method gets the status of all paragraphs by the given note id.
The body field of the returned JSON contains of the array that compose of the paragraph id, paragraph status, paragraph finish date, paragraph started date.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/job/[noteId]`

Success code

200

Fail code

500

sample JSON response

```json
{"status": "OK","body": [{"id":"20151121-212654\_766735423","status":"FINISHED","finished":"Tue Nov 24 14:21:40 KST 2015","started":"Tue Nov 24 14:21:39 KST 2015" },{"progress":"1","id":"20151121-212657\_730976687","status":"RUNNING","finished":"Tue Nov 24 14:21:35 KST 2015","started":"Tue Nov 24 14:21:40 KST 2015"}]}
```

<a id="usage-rest_api-notebook--get-an-existing-note-information"></a>

### Get an existing note information

Description

This `GET` method retrieves an existing note's information using the given id.
The body field of the returned JSON contain information about paragraphs in the note.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]`

Success code

200

Fail code

500

sample JSON response

```json
{"status": "OK","message": "","body": {"paragraphs": [{"text": "%sql \nselect age, count(1) value\nfrom bank \nwhere age < 30 \ngroup by age \norder by age","config": {"colWidth": 4,"graph": {"mode": "multiBarChart","height": 300,"optionOpen": false,"keys": [{"name": "age","index": 0,"aggr": "sum"} ],"values": [{"name": "value","index": 1,"aggr": "sum"} ],"groups": [],"scatter": {"xAxis": {"name": "age","index": 0,"aggr": "sum" },"yAxis": {"name": "value","index": 1,"aggr": "sum"}}} },"settings": {"params": {},"forms": {} },"jobName": "paragraph\_1423500782552\_-1439281894","id": "20150210-015302\_1492795503","results": {"code": "SUCCESS","msg": [{"type": "TABLE","data": "age\tvalue\n19\t4\n20\t3\n21\t7\n22\t9\n23\t20\n24\t24\n25\t44\n26 \t77\n27\t94\n28\t103\n29\t97\n"}] },"dateCreated": "Feb 10, 2015 1:53:02 AM","dateStarted": "Jul 3, 2015 1:43:17 PM","dateFinished": "Jul 3, 2015 1:43:23 PM","status": "FINISHED","progressUpdateIntervalMs": 500} ],"name": "Zeppelin Tutorial","id": "2A94M5J1Z","angularObjects": {},"config": {"looknfeel": "default" },"info": {}}}
```

<a id="usage-rest_api-notebook--delete-a-note"></a>

### Delete a note

| Description | This `DELETE` method deletes a note by the given note id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK","message": ""}
```

<a id="usage-rest_api-notebook--clone-a-note"></a>

### Clone a note

Description

This `POST` method clones a note by the given id and create a new note using the given name
or default name if none given. If what you want to copy is a certain version of note, you need
to specify the revisionId.
The body field of the returned JSON contains the new note id.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]`

Success code

200

Fail code

500

sample JSON input

```json
{
  "name": "name of new note",
  "revisionId": "revisionId of note to be copied (optional)"
}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{
  "status": "OK",
  "message": "",
  "body": "2AZPHY918"
}
```

<a id="usage-rest_api-notebook--rename-a-note"></a>

### Rename a note

| Description | This `PUT` method renames a note by the given id using the given name. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/rename` |
| Success code | 200 |
| Bad Request code | 400 |
| Fail code | 500 |
| sample JSON input |  |

```json
{"name": "new name of a note"}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-notebook--export-a-note"></a>

### Export a note

| Description | This `GET` method exports a note by the given id and gernerates a JSON |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/export/[noteId]` |
| Success code | 201 |
| Fail code | 500 |

```json
{"paragraphs": [{"text": "%md This is my new paragraph in my new note","dateUpdated": "Jan 8, 2016 4:49:38 PM","config": {"enabled": true },"settings": {"params": {},"forms": {} },"jobName": "paragraph\_1452300578795\_1196072540","id": "20160108-164938\_1685162144","dateCreated": "Jan 8, 2016 4:49:38 PM","status": "READY","progressUpdateIntervalMs": 500} ],"name": "source note for export","id": "2B82H3RR1","angularObjects": {},"config": {},"info": {}}
```

<a id="usage-rest_api-notebook--import-a-note"></a>

### Import a note

| Description | This `POST` method imports a note from the note JSON input |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/import` |
| Success code | 201 |
| Fail code | 500 |
| sample JSON input |  |

```json
{"paragraphs": [{"text": "%md This is my new paragraph in my new note","dateUpdated": "Jan 8, 2016 4:49:38 PM","config": {"enabled": true },"settings": {"params": {},"forms": {} },"jobName": "paragraph\_1452300578795\_1196072540","id": "20160108-164938\_1685162144","dateCreated": "Jan 8, 2016 4:49:38 PM","status": "READY","progressUpdateIntervalMs": 500} ],"name": "source note for export","id": "2B82H3RR1","angularObjects": {},"config": {},"info": {}}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{
  "status": "OK",
  "message": "",
  "body": "2AZPHY918"
}
```

<a id="usage-rest_api-notebook--run-all-paragraphs"></a>

### Run all paragraphs

Description

This `POST` method runs all paragraphs in the given note id.
If you can not find Note id 404 returns.
If there is a problem with the interpreter returns a 412 error.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/job/[noteId]`

Success code

200

Fail code

404 or 412

sample JSON response

```json
{"status": "OK"}
```

|  |  |
| --- | --- |
| sample JSON error response |  |

```json
{
  "status": "NOT_FOUND",
  "message": "note not found."
}
```

```json
{
  "status": "PRECONDITION_FAILED",
  "message": "paragraph_1469771130099_-278315611 Not selected or Invalid Interpreter
 bind"
}
```

<a id="usage-rest_api-notebook--stop-all-paragraphs"></a>

### Stop all paragraphs

| Description | This `DELETE` method stops all paragraphs in the given note id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/job/[noteId]` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-notebook--clear-all-paragraph-result"></a>

### Clear all paragraph result

| Description | This `PUT` method clear all paragraph results from note of given id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/clear` |
| Success code | 200 |
| Forbidden code | 401 |
| Not Found code | 404 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK"}
```

<a id="usage-rest_api-notebook--paragraph-operations"></a>

## Paragraph operations

<a id="usage-rest_api-notebook--create-a-new-paragraph"></a>

### Create a new paragraph

Description

This `POST` method create a new paragraph using JSON payload.
The body field of the returned JSON contain the new paragraph id.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/paragraph`

Success code

201

Fail code

500

sample JSON input (add to the last)

```json
{
  "title": "Paragraph insert revised",
  "text": "%spark\nprintln(\"Paragraph insert revised\")"
}
```

|  |  |
| --- | --- |
| sample JSON input (add to specific index) |  |

```json
{
  "title": "Paragraph insert revised",
  "text": "%spark\nprintln(\"Paragraph insert revised\")",
  "index": 0
}
```

|  |  |
| --- | --- |
| sample JSON input (providing paragraph config) |  |

```json
{"title": "paragraph title2","text": "paragraph text2","config": {"title": true,"colWidth": 6.0,"results": [{"graph": {"mode": "pieChart","optionOpen": true}}]}}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{
  "status": "OK",
  "message": "",
  "body": "20151218-100330\_1754029574"
}
```

<a id="usage-rest_api-notebook--get-a-paragraph-information"></a>

### Get a paragraph information

Description

This `GET` method retrieves an existing paragraph's information using the given id.
The body field of the returned JSON contain information about paragraph.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/paragraph/[paragraphId]`

Success code

200

Fail code

500

sample JSON response

```json
{"status": "OK","message": "","body": {"title": "Paragraph2","text": "%spark\n\nprintln(\"it's paragraph2\")","dateUpdated": "Dec 18, 2015 7:33:54 AM","config": {"colWidth": 12,"graph": {"mode": "table","height": 300,"optionOpen": false,"keys": [],"values": [],"groups": [],"scatter": {} },"enabled": true,"title": true,"editorMode": "ace/mode/scala" },"settings": {"params": {},"forms": {} },"jobName": "paragraph\_1450391574392\_-1890856722","id": "20151218-073254\_1105602047","results": {"code": "SUCCESS","msg": [{"type": "TEXT","data": "it's paragraph2\n"}] },"dateCreated": "Dec 18, 2015 7:32:54 AM","dateStarted": "Dec 18, 2015 7:33:55 AM","dateFinished": "Dec 18, 2015 7:33:55 AM","status": "FINISHED","progressUpdateIntervalMs": 500}}
```

<a id="usage-rest_api-notebook--get-the-status-of-a-single-paragraph"></a>

### Get the status of a single paragraph

Description

This `GET` method gets the status of a single paragraph by the given note and paragraph id.
The body field of the returned JSON contains of the array that compose of the paragraph id, paragraph status, paragraph finish date, paragraph started date.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/job/[noteId]/[paragraphId]`

Success code

200

Fail code

500

sample JSON response

```json
{"status": "OK","body": {"id":"20151121-212654\_766735423","status":"FINISHED","finished":"Tue Nov 24 14:21:40 KST 2015","started":"Tue Nov 24 14:21:39 KST 2015"}}
```

<a id="usage-rest_api-notebook--update-paragraph"></a>

### Update paragraph

<table class="table-configuration">
<col width="200"/>
<tr>
<td>Description</td>
<td>This <code>PUT</code> method update paragraph contents using given id, e.g. <code>{"text": "hello"}</code>
</td>
</tr>
<tr>
<td>URL</td>
<td><code>http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/paragraph/[paragraphId]</code></td>
</tr>
<tr>
<td>Success code</td>
<td>200</td>
</tr>
<tr>
<td>Bad Request code</td>
<td>400</td>
</tr>
<tr>
<td>Forbidden code</td>
<td>403</td>
</tr>
<tr>
<td>Not Found code</td>
<td>404</td>
</tr>
<tr>
<td>Fail code</td>
<td>500</td>
</tr>
<tr>
<td>sample JSON input</td>
<td></td></tr></table>

```json
{
  "title": "Hello world",
  "text": "println(\"hello world\")"
}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{
  "status": "OK",
  "message": ""
}
```

<a id="usage-rest_api-notebook--update-paragraph-configuration"></a>

### Update paragraph configuration

Description

This `PUT` method update paragraph configuration using given id so that user can change paragraph setting such as graph type, show or hide editor/result and paragraph size, etc. You can update certain fields you want, for example you can update `colWidth` field only by sending request with payload `{"colWidth": 12.0}`.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/paragraph/[paragraphId]/config`

Success code

200

Bad Request code

400

Forbidden code

403

Not Found code

404

Fail code

500

sample JSON input

```json
{"colWidth": 6.0,"graph": {"mode": "lineChart","height": 200.0,"optionOpen": false,"keys": [{"name": "age","index": 0.0,"aggr": "sum"} ],"values": [{"name": "value","index": 1.0,"aggr": "sum"} ],"groups": [],"scatter": {} },"editorHide": true,"editorMode": "ace/mode/markdown","tableHide": false}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{"status":"OK","message":"","body":{"text":"%sql \nselect age, count(1) value\nfrom bank \nwhere age \u003c 30 \ngroup by age \norder by age","config":{"colWidth":6.0,"graph":{"mode":"lineChart","height":200.0,"optionOpen":false,"keys":[{"name":"age","index":0.0,"aggr":"sum"} ],"values":[{"name":"value","index":1.0,"aggr":"sum"} ],"groups":[],"scatter":{} },"tableHide":false,"editorMode":"ace/mode/markdown","editorHide":true },"settings":{"params":{},"forms":{} },"apps":[],"jobName":"paragraph_1423500782552_-1439281894","id":"20150210-015302_1492795503","results":{"code":"SUCCESS","msg": [{"type":"TABLE","data":"age\tvalue\n19\t4\n20\t3\n21\t7\n22\t9\n23\t20\n24\t24\n25\t44\n26\t77 \n27\t94\n28\t103\n29\t97\n"}] },"dateCreated":"Feb 10, 2015 1:53:02 AM","dateStarted":"Jul 3, 2015 1:43:17 PM","dateFinished":"Jul 3, 2015 1:43:23 PM","status":"FINISHED","progressUpdateIntervalMs":500}}
```

<a id="usage-rest_api-notebook--delete-a-paragraph"></a>

### Delete a paragraph

| Description | This `DELETE` method deletes a paragraph by the given note and paragraph id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/paragraph/[paragraphId]` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK","message": ""}
```

<a id="usage-rest_api-notebook--run-a-paragraph-asynchronously"></a>

### Run a paragraph asynchronously

Description

This `POST` method runs the paragraph asynchronously by given note and paragraph id. This API always return SUCCESS even if the execution of the paragraph fails later because the API is asynchronous

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/job/[noteId]/[paragraphId]`

Success code

200

Fail code

500

sample JSON input (optional, only needed when if you want to update dynamic form's value)

```json
{
  "name": "name of new note",
  "params": {
    "formLabel1": "value1",
    "formLabel2": "value2"
  }
}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{"status": "OK"}
```

<a id="usage-rest_api-notebook--run-a-paragraph-synchronously"></a>

### Run a paragraph synchronously

Description

This `POST` method runs the paragraph synchronously by given note and paragraph id. This API can return SUCCESS or ERROR depending on the outcome of the paragraph execution

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/run/[noteId]/[paragraphId]`

Success code

200

Fail code

500

sample JSON input (optional, only needed when if you want to update dynamic form's value)

```json
{
  "name": "name of new note",
  "params": {
    "formLabel1": "value1",
    "formLabel2": "value2"
  }
}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{"status": "OK"}
```

|  |  |
| --- | --- |
| sample JSON error |  |

```json
{"status": "INTERNAL\_SERVER\_ERROR","body": {"code": "ERROR","type": "TEXT","msg": "bash: -c: line 0: unexpected EOF while looking for matching ``'\nbash: -c:line 1: syntax error: unexpected end of file\nExitValue: 2"}}
```

<a id="usage-rest_api-notebook--stop-a-paragraph"></a>

### Stop a paragraph

| Description | This `DELETE` method stops the paragraph by given note and paragraph id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/job/[noteId]/[paragraphId]` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK"}
```

<a id="usage-rest_api-notebook--move-a-paragraph-to-the-specific-index"></a>

### Move a paragraph to the specific index

<table class="table-configuration">
<col width="200"/>
<tr>
<td>Description</td>
<td>This <code>POST</code> method moves a paragraph to the specific index (order) from the note.
      </td>
</tr>
<tr>
<td>URL</td>
<td><code>http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/paragraph/[paragraphId]/move/[newIndex]</code></td>
</tr>
<tr>
<td>Success code</td>
<td>200</td>
</tr>
<tr>
<td> Fail code</td>
<td> 500 </td>
</tr>
<tr>
<td> sample JSON response </td>
<td></td></tr></table>

```json
{"status": "OK","message": ""}
```

<a id="usage-rest_api-notebook--full-text-search-through-the-paragraphs-in-all-notes"></a>

### Full text search through the paragraphs in all notes

| Description | `GET` request will return list of matching paragraphs |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/search?q=[query]` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status": "OK","body": [{"id": "<noteId>/paragraph/<paragraphId>","name":"Note Name","snippet":"","text":""}]}
```

<a id="usage-rest_api-notebook--cron-jobs"></a>

## Cron jobs

<a id="usage-rest_api-notebook--add-cron-job"></a>

### Add Cron Job

Description

This `POST` method adds cron job by the given note id.
Default value of `releaseResource` is `false`.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/cron/[noteId]`

Success code

200

Fail code

500

sample JSON input

```json
{"cron": "cron expression of note", "releaseResource": "false"}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{"status": "OK"}
```

<a id="usage-rest_api-notebook--remove-cron-job"></a>

### Remove Cron Job

| Description | This `DELETE` method removes cron job by the given note id. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/cron/[noteId]` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK"}
```

<a id="usage-rest_api-notebook--get-cron-job"></a>

### Get Cron Job

Description

This `GET` method gets cron job expression of given note id.
The body field of the returned JSON contains the cron expression and `releaseResource` flag.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/notebook/cron/[noteId]`

Success code

200

Fail code

500

sample JSON response

```json
{
   "status": "OK",
   "body": {
      "cron": "0 0/1 * * * ?",
      "releaseResource": true
   }
}
```

<a id="usage-rest_api-notebook--permission"></a>

## Permission

<a id="usage-rest_api-notebook--get-a-note-permission-information"></a>

### Get a note permission information

| Description | This `GET` method gets a note authorization information. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/permissions` |
| Success code | 200 |
| Forbidden code | 403 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status":"OK","message":"","body":{"readers":["user2" ],"owners":["user1" ],"runners":["user2" ],"writers":["user2"]}}
```

<a id="usage-rest_api-notebook--set-note-permission"></a>

### Set note permission

| Description | This `PUT` method set note authorization information. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/permissions` |
| Success code | 200 |
| Forbidden code | 403 |
| Fail code | 500 |
| sample JSON input |  |

```json
{"readers": ["user1" ],"owners": ["user2" ],"runners":["user2" ],"writers": ["user1"]}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{
  "status": "OK"
}
```

<a id="usage-rest_api-notebook--version-control"></a>

## Version control

<a id="usage-rest_api-notebook--get-revisions-of-a-note"></a>

### Get revisions of a note

| Description | This `GET` method gets the revisions of a note. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/revision` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK","body": [{"id": "f97ce5c7f076783023d33623ad52ca994277e5c1","message": "first commit","time": 1645712061 },{"id": "e9b964bebdecec6a59efe085f97db4040ae333aa","message": "second commit","time": 1645693163}]}
```

<a id="usage-rest_api-notebook--save-a-revision-for-a-note"></a>

### Save a revision for a note

| Description | This `POST` method saves a revision for a note. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/revision` |
| Success code | 200 |
| Bad Request code | 400 |
| Fail code | 500 |
| sample JSON input |  |

```json
{
  "commitMessage": "first commit"
}
```

|  |  |
| --- | --- |
| sample JSON response |  |

```json
{
  "status": "OK",
  "message": "",
  "body": "6a5879218dfb797b013bcd24a594808045e34875"
}
```

<a id="usage-rest_api-notebook--get-a-revision-of-a-note"></a>

### Get a revision of a note

| Description | This `GET` method gets a revision of a note. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/revision/{revisionId}` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{"status": "OK","message": "","body": {"paragraphs": [{"text": "%sql \nselect age, count(1) value\nfrom bank \nwhere age < 30 \ngroup by age \norder by age","config": {"colWidth": 4,"graph": {"mode": "multiBarChart","height": 300,"optionOpen": false,"keys": [{"name": "age","index": 0,"aggr": "sum"} ],"values": [{"name": "value","index": 1,"aggr": "sum"} ],"groups": [],"scatter": {"xAxis": {"name": "age","index": 0,"aggr": "sum" },"yAxis": {"name": "value","index": 1,"aggr": "sum"}}} },"settings": {"params": {},"forms": {} },"jobName": "paragraph\_1423500782552\_-1439281894","id": "20150210-015302\_1492795503","results": {"code": "SUCCESS","msg": [{"type": "TABLE","data": "age\tvalue\n19\t4\n20\t3\n21\t7\n22\t9\n23\t20\n24\t24\n25\t44\n26 \t77\n27\t94\n28\t103\n29\t97\n"}] },"dateCreated": "Feb 10, 2015 1:53:02 AM","dateStarted": "Jul 3, 2015 1:43:17 PM","dateFinished": "Jul 3, 2015 1:43:23 PM","status": "FINISHED","progressUpdateIntervalMs": 500} ],"name": "Zeppelin Tutorial","id": "2A94M5J1Z","angularObjects": {},"config": {"looknfeel": "default" },"info": {}}}
```

<a id="usage-rest_api-notebook--revert-a-note-to-a-specified-version"></a>

### Revert a note to a specified version

| Description | This `PUT` method reverts a note to a specified version |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook/[noteId]/revision/{revisionId}` |
| Success code | 200 |
| Fail code | 500 |
| sample JSON response |  |

```json
{
  "status": "OK"
}
```

---

---

<a id="usage-rest_api-notebook_repository"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/rest_api/notebook_repository.html -->

<!-- page_index: 31 -->

<a id="usage-rest_api-notebook_repository--apache-zeppelin-notebook-repository-api"></a>

# Apache Zeppelin Notebook Repository API

<a id="usage-rest_api-notebook_repository--overview"></a>

## Overview

Apache Zeppelin provides several REST APIs for interaction and remote activation of zeppelin functionality.
All REST APIs are available starting with the following endpoint `http://[zeppelin-server]:[zeppelin-port]/api`.
Note that Apache Zeppelin REST APIs receive or return JSON objects, it is recommended for you to install some JSON viewers such as [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).

If you work with Apache Zeppelin and find a need for an additional REST API, please [file an issue or send us an email](http://zeppelin.apache.org/community.html).

<a id="usage-rest_api-notebook_repository--notebook-repository-rest-api-list"></a>

## Notebook Repository REST API List

<a id="usage-rest_api-notebook_repository--list-all-available-notebook-repositories"></a>

### List all available notebook repositories

| Description | This `GET` method returns all the available notebook repositories. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook-repositories` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": [{"name": "GitNotebookRepo","className": "org.apache.zeppelin.notebook.repo.GitNotebookRepo","settings": [{"type": "INPUT","value": [],"selected": "ZEPPELIN_HOME/zeppelin/notebook/","name": "Notebook Path"}]}]}
```

<a id="usage-rest_api-notebook_repository--reload-a-notebook-repository"></a>

### Reload a notebook repository

| Description | This `GET` method triggers reloading and broadcasting of the note list. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook-repositories/reload` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{
  "status": "OK",
  "message": ""
}
```

<a id="usage-rest_api-notebook_repository--update-a-specific-notebook-repository"></a>

### Update a specific notebook repository

| Description | This `PUT` method updates a specific notebook repository. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/notebook-repositories` |
| Success code | 200 |
| Fail code | 404 when the specified notebook repository doesn't exist 406 for invalid payload 500 for any other errors |
| Sample JSON input |  |

```json
{
  "name":"org.apache.zeppelin.notebook.repo.GitNotebookRepo",
  "settings":{
    "Notebook Path":"/tmp/notebook/"
  }
}
```

|  |  |
| --- | --- |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": {"name": "GitNotebookRepo","className": "org.apache.zeppelin.notebook.repo.GitNotebookRepo","settings": [{"type": "INPUT","value": [],"selected": "/tmp/notebook/","name": "Notebook Path"}]}}
```

---

---

<a id="usage-rest_api-configuration"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/rest_api/configuration.html -->

<!-- page_index: 32 -->

<a id="usage-rest_api-configuration--apache-zeppelin-configuration-rest-api"></a>

# Apache Zeppelin Configuration REST API

<a id="usage-rest_api-configuration--overview"></a>

## Overview

Apache Zeppelin provides several REST APIs for interaction and remote activation of zeppelin functionality.
All REST APIs are available starting with the following endpoint `http://[zeppelin-server]:[zeppelin-port]/api`.
Note that Apache Zeppelin REST APIs receive or return JSON objects, it is recommended for you to install some JSON viewers such as [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).

If you work with Apache Zeppelin and find a need for an additional REST API, please [file an issue or send us an email](http://zeppelin.apache.org/community.html).

<a id="usage-rest_api-configuration--configuration-rest-api-list"></a>

## Configuration REST API list

<a id="usage-rest_api-configuration--list-all-key-value-pair-of-configurations"></a>

### List all key/value pair of configurations

Description

This `GET` method return all key/value pair of configurations on the server.
Note: For security reason, some pairs would not be shown.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/configurations/all`

Success code

200

Fail code

500

sample JSON response

```json
{
  "status": "OK",
  "message": "",
  "body": {
    "zeppelin.war.tempdir": "webapps",
    "zeppelin.notebook.homescreen.hide": "false",
    "zeppelin.interpreter.remoterunner": "bin/interpreter.sh",
    "zeppelin.notebook.s3.user": "user",
    "zeppelin.server.port": "8089",
    "zeppelin.dep.localrepo": "local-repo",
    "zeppelin.ssl.truststore.type": "JKS",
    "zeppelin.ssl.keystore.path": "keystore",
    "zeppelin.notebook.s3.bucket": "zeppelin",
    "zeppelin.server.addr": "0.0.0.0",
    "zeppelin.ssl.client.auth": "false",
    "zeppelin.server.context.path": "/",
    "zeppelin.ssl.keystore.type": "JKS",
    "zeppelin.ssl.truststore.path": "truststore",
    "zeppelin.ssl": "false",
    "zeppelin.notebook.autoInterpreterBinding": "true",
    "zeppelin.notebook.homescreen": "",
    "zeppelin.notebook.storage": "org.apache.zeppelin.notebook.repo.VFSNotebookRepo",
    "zeppelin.interpreter.connect.timeout": "30000",
    "zeppelin.server.allowed.origins":"*",
    "zeppelin.encoding": "UTF-8"
  }
}
```

<a id="usage-rest_api-configuration--list-all-prefix-matched-key-value-pair-of-configurations"></a>

### List all prefix matched key/value pair of configurations

Description

This `GET` method return all prefix matched key/value pair of configurations on the server.
Note: For security reason, some pairs would not be shown.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/configurations/prefix/[prefix]`

Success code

200

Fail code

500

sample JSON response

```json
{"status": "OK","message": "","body": {"zeppelin.ssl.keystore.type": "JKS","zeppelin.ssl.truststore.path": "truststore","zeppelin.ssl.truststore.type": "JKS","zeppelin.ssl.keystore.path": "keystore","zeppelin.ssl": "false","zeppelin.ssl.client.auth": "false"}}
```

---

---

<a id="usage-rest_api-credential"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/rest_api/credential.html -->

<!-- page_index: 33 -->

<a id="usage-rest_api-credential--apache-zeppelin-credential-rest-api"></a>

# Apache Zeppelin Credential REST API

<a id="usage-rest_api-credential--overview"></a>

## Overview

Apache Zeppelin provides several REST APIs for interaction and remote activation of zeppelin functionality.
All REST APIs are available starting with the following endpoint `http://[zeppelin-server]:[zeppelin-port]/api`.
Note that Apache Zeppelin REST APIs receive or return JSON objects, it is recommended for you to install some JSON viewers such as [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).

If you work with Apache Zeppelin and find a need for an additional REST API, please [file an issue or send us an email](http://zeppelin.apache.org/community.html).

<a id="usage-rest_api-credential--credential-rest-api-list"></a>

## Credential REST API List

<a id="usage-rest_api-credential--list-credential-information"></a>

### List Credential information

Description

This `GET` method returns all key/value pairs of the credential information on the server.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/credential`

Success code

200

Fail code

500

sample JSON response

```json
{"status": "OK","message": "","body": {"userCredentials":{"entity1":{"username":"user1","password":"password1" },"entity2":{"username":"user2","password":"password2"}}}}
```

<a id="usage-rest_api-credential--create-an-credential-information"></a>

### Create an Credential Information

| Description | This `PUT` method creates the credential information with new properties. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/credential/` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON input |  |

```json
{
  "entity": "e1",
  "username": "user",
  "password": "password"
}
```

|  |  |
| --- | --- |
| Sample JSON response |  |

```json
{
  "status": "OK"
}
```

<a id="usage-rest_api-credential--delete-all-credential-information"></a>

### Delete all Credential Information

| Description | This `DELETE` method deletes the credential information. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/credential` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-credential--delete-an-credential-entity"></a>

### Delete an Credential entity

| Description | This `DELETE` method deletes a given credential entity. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/credential/[entity]` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status":"OK"}
```

---

---

<a id="usage-rest_api-helium"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/rest_api/helium.html -->

<!-- page_index: 34 -->

<a id="usage-rest_api-helium--apache-zeppelin-helium-rest-api"></a>

# Apache Zeppelin Helium REST API

<a id="usage-rest_api-helium--overview"></a>

## Overview

Apache Zeppelin provides several REST APIs for interaction and remote activation of zeppelin functionality.
All REST APIs are available starting with the following endpoint `http://[zeppelin-server]:[zeppelin-port]/api`.
Note that Apache Zeppelin REST APIs receive or return JSON objects, it is recommended for you to install some JSON viewers such as [JSONView](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).

If you work with Apache Zeppelin and find a need for an additional REST API, please [file an issue or send us an email](http://zeppelin.apache.org/community.html).

<a id="usage-rest_api-helium--helium-rest-api-list"></a>

## Helium REST API List

<a id="usage-rest_api-helium--get-all-available-helium-packages"></a>

### Get all available helium packages

Description

This `GET` method returns all the available helium packages in configured registries.

URL

`http://[zeppelin-server]:[zeppelin-port]/api/helium/package`

Success code

200

Fail code

500

Sample JSON response

```json
{"status": "OK","message": "","body": {"zeppelin.clock": [{"registry": "local","pkg": {"type": "APPLICATION","name": "zeppelin.clock","description": "Clock (example)","artifact": "zeppelin-examples\/zeppelin-example-clock\/target\/zeppelin-example -clock-0.7.0-SNAPSHOT.jar","className": "org.apache.zeppelin.example.app.clock.Clock","resources": [[":java.util.Date"] ],"icon": "icon" },"enabled": false}]}}
```

<a id="usage-rest_api-helium--get-all-enabled-helium-packages"></a>

### Get all enabled helium packages

| Description | This `GET` method returns all enabled helium packages in configured registries. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/enabledPackage` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": {"zeppelin.clock": [{"registry": "local","pkg": {"type": "APPLICATION","name": "zeppelin.clock","description": "Clock (example)","artifact": "zeppelin-examples\/zeppelin-example-clock\/target\/zeppelin-example -clock-0.7.0-SNAPSHOT.jar","className": "org.apache.zeppelin.example.app.clock.Clock","resources": [[":java.util.Date"] ],"icon": "icon" },"enabled": false}]}}
```

<a id="usage-rest_api-helium--get-single-helium-package"></a>

### Get single helium package

| Description | This `GET` method returns specified helium package information |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/package/[Package Name]` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": {"zeppelin.clock": [{"registry": "local","pkg": {"type": "APPLICATION","name": "zeppelin.clock","description": "Clock (example)","artifact": "zeppelin-examples\/zeppelin-example-clock\/target\/zeppelin-example -clock-0.7.0-SNAPSHOT.jar","className": "org.apache.zeppelin.example.app.clock.Clock","resources": [[":java.util.Date"] ],"icon": "icon" },"enabled": false}]}}
```

<a id="usage-rest_api-helium--suggest-helium-package-on-a-paragraph"></a>

### Suggest Helium package on a paragraph

| Description | This `GET` method returns suggested helium package for the paragraph. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/suggest/[Note ID]/[Paragraph ID]` |
| Success code | 200 |
| Fail code | 404 on note or paragraph not exists 500 |
| Sample JSON response |  |

```json
{"status": "OK","message": "","body": {"available": [{"registry": "local","pkg": {"type": "APPLICATION","name": "zeppelin.clock","description": "Clock (example)","artifact": "zeppelin-examples\/zeppelin-example-clock\/target\/zeppelin-example -clock-0.7.0-SNAPSHOT.jar","className": "org.apache.zeppelin.example.app.clock.Clock","resources": [[":java.util.Date"] ],"icon": "icon" },"enabled": true}]}}
```

<a id="usage-rest_api-helium--load-helium-package-on-a-paragraph"></a>

### Load Helium package on a paragraph

| Description | This `POST` method loads helium package to target paragraph. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/load/[Note ID]/[Paragraph ID]` |
| Success code | 200 |
| Fail code | 404 on note or paragraph not exists 500 |
| Sample JSON response |  |

```json
{
  "status": "OK",
  "message": "",
  "body": "app_2C5FYRZ1E-20170108-040449_2068241472zeppelin_clock"
}
```

<a id="usage-rest_api-helium--load-bundled-visualization-script"></a>

### Load bundled visualization script

Description

This `GET` method returns bundled helium visualization javascript. When refresh=true (optional) is provided, Zeppelin rebuilds bundle. Otherwise, it's provided from cache

URL

`http://[zeppelin-server]:[zeppelin-port]/api/helium/bundle/load/[Package Name][?refresh=true]`

Success code

200 reponse body is executable javascript

Fail code

200 reponse body is error message string starts with ERROR:

<a id="usage-rest_api-helium--enable-package"></a>

### Enable package

Description

This `POST` method enables a helium package. Needs artifact name in input payload

URL

`http://[zeppelin-server]:[zeppelin-port]/api/helium/enable/[Package Name]`

Success code

200

Fail code

500

Sample input

```

zeppelin-examples/zeppelin-example-clock/target/zeppelin-example-clock-0.7.0-SNAPSHOT.jar
        
```

Sample JSON response

```json
{"status":"OK"}
```

<a id="usage-rest_api-helium--disable-package"></a>

### Disable package

| Description | This `POST` method disables a helium package. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/disable/[Package Name]` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-helium--get-visualization-display-order"></a>

### Get visualization display order

| Description | This `GET` method returns display order of enabled visualization packages. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/order/visualization` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON response |  |

```json
{"status":"OK","body":["zeppelin_horizontalbar","zeppelin-bubblechart"]}
```

<a id="usage-rest_api-helium--set-visualization-display-order"></a>

### Set visualization display order

| Description | This `POST` method sets visualization packages display order. |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/order/visualization` |
| Success code | 200 |
| Fail code | 500 |
| Sample JSON input |  |

```json
["zeppelin-bubblechart", "zeppelin_horizontalbar"]
```

|  |  |
| --- | --- |
| Sample JSON response |  |

```json
{"status":"OK"}
```

<a id="usage-rest_api-helium--get-configuration-for-all-helium-packages"></a>

### Get configuration for all Helium packages

| Description | This `GET` method returns configuration for all Helium packages |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/config` |
| Success code | 200 |
| Fail code | 500 |

### Get configuration for specific package

Description

This `GET` method returns configuration for the specified package name and artifact

URL

`http://[zeppelin-server]:[zeppelin-port]/api/helium/config/[Package Name]/[Artifact]`

Success code

200

Fail code

500

<a id="usage-rest_api-helium--set-configuration-for-specific-package"></a>

### Set configuration for specific package

| Description | This `POST` method updates configuration for specified package name and artifact |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/config/[Package Name]/[Artifact]` |
| Success code | 200 |
| Fail code | 500 |

### Get Spell configuration for single package

| Description | This `GET` method returns specified package Spell configuration |
| --- | --- |
| URL | `http://[zeppelin-server]:[zeppelin-port]/api/helium/spell/config/[Package Name]` |
| Success code | 200 |
| Fail code | 500 |

---

---

<a id="usage-zeppelin_sdk-client_api"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/zeppelin_sdk/client_api.html -->

<!-- page_index: 35 -->

<a id="usage-zeppelin_sdk-client_api--apache-zeppelin-sdk-zeppelin-client-api"></a>

# Apache Zeppelin SDK - Zeppelin Client API

<a id="usage-zeppelin_sdk-client_api--overview"></a>

## Overview

Zeppelin client api is a lower level java api which encapsulates Zeppelin's rest api so that you can easily integrate Zeppelin
with your system. You can use zeppelin client api to do most of the things in notebook ui in a programmatic way, such as create/delete note/paragraph, run note/paragraph and etc.

<a id="usage-zeppelin_sdk-client_api--how-to-use-zeppelin-client-api"></a>

## How to use Zeppelin Client API

The entry point of zeppelin client api is class `ZeppelinClient`. All the operations is via this class, e.g. in the following example, we use `ZeppelinClient` to run the spark tutorial note programmatically.

```java
ClientConfig clientConfig = new ClientConfig("http://localhost:8080");
ZeppelinClient zClient = new ZeppelinClient(clientConfig);

String zeppelinVersion = zClient.getVersion();
System.out.println("Zeppelin version: " + zeppelinVersion);

// execute note 2A94M5J1Z paragraph by paragraph
try {
  ParagraphResult paragraphResult = zClient.executeParagraph("2A94M5J1Z", "20150210-015259_1403135953");
  System.out.println("Execute the 1st spark tutorial paragraph, paragraph result: " + paragraphResult);

  paragraphResult = zClient.executeParagraph("2A94M5J1Z", "20150210-015302_1492795503");
  System.out.println("Execute the 2nd spark tutorial paragraph, paragraph result: " + paragraphResult);

  Map<String, String> parameters = new HashMap<>();
  parameters.put("maxAge", "40");
  paragraphResult = zClient.executeParagraph("2A94M5J1Z", "20150212-145404_867439529", parameters);
  System.out.println("Execute the 3rd spark tutorial paragraph, paragraph result: " + paragraphResult);

  parameters = new HashMap<>();
  parameters.put("marital", "married");
  paragraphResult = zClient.executeParagraph("2A94M5J1Z", "20150213-230422_1600658137", parameters);
  System.out.println("Execute the 4th spark tutorial paragraph, paragraph result: " + paragraphResult);
} finally {
  // you need to stop interpreter explicitly if you are running paragraph separately.
  zClient.stopInterpreter("2A94M5J1Z", "spark");
}
```

Here we list some importance apis of ZeppelinClient, for the completed api, please refer its javadoc.

```java
public String createNote(String notePath) throws Exception

public void deleteNote(String noteId) throws Exception

public NoteResult executeNote(String noteId) throws Exception

public NoteResult executeNote(String noteId,
                              Map<String, String> parameters) throws Exception

public NoteResult queryNoteResult(String noteId) throws Exception

public NoteResult submitNote(String noteId) throws Exception

public NoteResult submitNote(String noteId,
                             Map<String, String> parameters) throws Exception

public NoteResult waitUntilNoteFinished(String noteId) throws Exception

public String addParagraph(String noteId,
                           String title,
                           String text) throws Exception

public void updateParagraph(String noteId,
                            String paragraphId,
                            String title,
                            String text) throws Exception

public ParagraphResult executeParagraph(String noteId,
                                        String paragraphId,
                                        String sessionId,
                                        Map<String, String> parameters) throws Exception

public ParagraphResult submitParagraph(String noteId,
                                       String paragraphId,
                                       String sessionId,
                                       Map<String, String> parameters) throws Exception

public void cancelParagraph(String noteId, String paragraphId)

public ParagraphResult queryParagraphResult(String noteId, String paragraphId)

public ParagraphResult waitUtilParagraphFinish(String noteId, String paragraphId)
```

<a id="usage-zeppelin_sdk-client_api--examples"></a>

## Examples

For more detailed usage of zeppelin client api, you can check the examples in module `zeppelin-client-examples`

- [ZeppelinClientExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/ZeppelinClientExample.java)
- [ZeppelinClientExample2](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/ZeppelinClientExample2.java)

---

---

<a id="usage-zeppelin_sdk-session_api"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/usage/zeppelin_sdk/session_api.html -->

<!-- page_index: 36 -->

<a id="usage-zeppelin_sdk-session_api--apache-zeppelin-sdk-session-api"></a>

# Apache Zeppelin SDK - Session API

<a id="usage-zeppelin_sdk-session_api--overview"></a>

## Overview

Session api is a high level api for zeppelin. There's no zeppelin concept (note, paragraph) in this api. The most important thing is a ZSession which represent a running interpreter process.
It is pretty to create a ZSession and its api is very straightforward, we can see a concret examples below.

<a id="usage-zeppelin_sdk-session_api--how-to-use-zsession"></a>

## How to use ZSession

It is very easy to create a ZSession, you need to provide ClientConfig, interpreter and also you can customize your ZSession by specificy its interpreter properties.

After you can create ZSession, you need to start it before running any code.
ZSession's lifecycle is under your control, you need to call stop method expclitly, otherwise the interpreter processs will keep running.

```java
ZSession session = null;
try {
  ClientConfig clientConfig = new ClientConfig("http://localhost:8080");
  Map<String, String> intpProperties = new HashMap<>();
  intpProperties.put("spark.master", "local[*]");

  session = ZSession.builder()
          .setClientConfig(clientConfig)
          .setInterpreter("spark")
          .setIntpProperties(intpProperties)
          .build();

  session.start();
  System.out.println("Spark Web UI: " + session.getWeburl());

  // scala (single result)
  ExecuteResult result = session.execute("println(sc.version)");
  System.out.println("Spark Version: " + result.getResults().get(0).getData());

  // scala (multiple result)
  result = session.execute("println(sc.version)\n" +
          "val df = spark.createDataFrame(Seq((1,\"a\"), (2,\"b\")))\n" +
          "z.show(df)");

  // The first result is text output
  System.out.println("Result 1: type: " + result.getResults().get(0).getType() +
          ", data: " + result.getResults().get(0).getData() );
  // The second result is table output
  System.out.println("Result 2: type: " + result.getResults().get(1).getType() +
          ", data: " + result.getResults().get(1).getData() );
  System.out.println("Spark Job Urls:\n" + StringUtils.join(result.getJobUrls(), "\n"));

  // error output
  result = session.execute("1/0");
  System.out.println("Result status: " + result.getStatus() +
          ", data: " + result.getResults().get(0).getData());

  // pyspark
  result = session.execute("pyspark", "df = spark.createDataFrame([(1,'a'),(2,'b')])\n" +
          "df.registerTempTable('df')\n" +
          "df.show()");
  System.out.println("PySpark dataframe: " + result.getResults().get(0).getData());

  // matplotlib
  result = session.execute("ipyspark", "%matplotlib inline\n" +
          "import matplotlib.pyplot as plt\n" +
          "plt.plot([1,2,3,4])\n" +
          "plt.ylabel('some numbers')\n" +
          "plt.show()");
  System.out.println("Matplotlib result, type: " + result.getResults().get(0).getType() +
          ", data: " + result.getResults().get(0).getData());

  // sparkr
  result = session.execute("r", "df <- as.DataFrame(faithful)\nhead(df)");
  System.out.println("Sparkr dataframe: " + result.getResults().get(0).getData());

  // spark sql
  result = session.execute("sql", "select * from df");
  System.out.println("Spark Sql dataframe: " + result.getResults().get(0).getData());

  // spark invalid sql
  result = session.execute("sql", "select * from unknown_table");
  System.out.println("Result status: " + result.getStatus() +
          ", data: " + result.getResults().get(0).getData());
} catch (Exception e) {
  e.printStackTrace();
} finally {
  if (session != null) {
    try {
      session.stop();
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}
```

Here's a list of apis of `ZSession`.

```java
public void start() throws Exception

public void start(MessageHandler messageHandler) throws Exception

public void stop() throws Exception

public ExecuteResult execute(String code) throws Exception

public ExecuteResult execute(String subInterpreter,
                             Map<String, String> localProperties,
                             String code,
                             StatementMessageHandler messageHandler) throws Exception

public ExecuteResult submit(String code) throws Exception

public ExecuteResult submit(String subInterpreter,
                            Map<String, String> localProperties,
                            String code,
                            StatementMessageHandler messageHandler) throws Exception

public void cancel(String statementId) throws Exception

public ExecuteResult queryStatement(String statementId) throws Exception

public ExecuteResult waitUntilFinished(String statementId) throws Exception
```

<a id="usage-zeppelin_sdk-session_api--examples"></a>

## Examples

For more detailed usage of session api, you can check the examples in module `zeppelin-client-examples`

- [SparkExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/SparkExample.java)
- [SparkAdvancedExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/SparkAdvancedExample.java)
- [FlinkExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/FlinkExample.java)
- [FlinkAdvancedExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/FlinkAdvancedExample.java)
- [FlinkAdvancedExample2](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/FlinkAdvancedExample2.java)
- [HiveExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/HiveExample.java)
- [PythonExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/PythonExample.java)
- [RExample](https://github.com/apache/zeppelin/blob/master/zeppelin-client-examples/src/main/java/org/apache/zeppelin/client/examples/RExample.java)

---

---

<a id="setup-basics-how_to_build"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/basics/how_to_build.html -->

<!-- page_index: 37 -->

<a id="setup-basics-how_to_build--how-to-build-zeppelin-from-source"></a>

## How to Build Zeppelin from Source

<a id="setup-basics-how_to_build--0.-requirements"></a>

#### 0. Requirements

If you want to build from source, you must first install the following dependencies:

| Name | Value |
| --- | --- |
| Git | (Any Version) |
| Maven | 3.6.3 or higher |
| OpenJDK or Oracle JDK | 1.8 (151+) (set JAVA\_HOME) |

If you haven't installed Git and Maven yet, check the [Build requirements](#setup-basics-how_to_build--build-requirements) section and follow the step by step instructions from there.

<a id="setup-basics-how_to_build--1.-clone-the-apache-zeppelin-repository"></a>

#### 1. Clone the Apache Zeppelin repository

```bash
git clone https://github.com/apache/zeppelin.git
```

<a id="setup-basics-how_to_build--2.-build-source"></a>

#### 2. Build source

You can build Zeppelin with following maven command:

```bash
./mvnw clean package -DskipTests [Options]
```

Check [build-profiles](#setup-basics-how_to_build--build-profiles) section for further build options.
If you are behind proxy, follow instructions in [Proxy setting](#setup-basics-how_to_build--proxy-setting-optional) section.

If you're interested in contribution, please check [Contributing to Apache Zeppelin (Code)](#development-contribution-how_to_contribute_code) and [Contributing to Apache Zeppelin (Website)](#development-contribution-how_to_contribute_website).

<a id="setup-basics-how_to_build--3.-done"></a>

#### 3. Done

You can directly start Zeppelin by running the following command after successful build:

```bash
./bin/zeppelin-daemon.sh start
```

<a id="setup-basics-how_to_build--build-profiles"></a>

### Build profiles

<a id="setup-basics-how_to_build--spark-interpreter"></a>

#### Spark Interpreter

To be noticed, the spark profiles here only affect the unit test (no need to specify `SPARK_HOME`) of spark interpreter.
Zeppelin doesn't require you to build with different spark to make different versions of spark work in Zeppelin.
You can run different versions of Spark in Zeppelin as long as you specify `SPARK_HOME`. Actually Zeppelin supports all the versions of Spark from 3.3 to 3.5.

To build with a specific Spark version or scala versions, define one or more of the following profiles and options:

<a id="setup-basics-how_to_build--pspark-version"></a>

##### `-Pspark-[version]`

Set spark major version

Available profiles are

```
-Pspark-3.5
-Pspark-3.4
-Pspark-3.3
```

minor version can be adjusted by `-Dspark.version=x.x.x`

<a id="setup-basics-how_to_build--pspark-scala-version-optional"></a>

##### `-Pspark-scala-[version] (optional)`

To be noticed, these profiles also only affect the unit test (no need to specify `SPARK_HOME`) of Spark interpreter.
Actually Zeppelin supports all the versions of scala (2.12, 2.13) in Spark interpreter as long as you specify `SPARK_HOME`.

Available profiles are

```
-Pspark-scala-2.12
-Pspark-scala-2.13
```

<a id="setup-basics-how_to_build--build-hadoop-with-zeppelin"></a>

#### Build hadoop with Zeppelin

To be noticed, hadoop profiles only affect Zeppelin server, it doesn't affect any interpreter.
Zeppelin server use hadoop in some cases, such as using hdfs as notebook storage. You can check this [page](#setup-basics-hadoop_integration) for more details about how to configure hadoop in Zeppelin.

Hadoop version can be adjusted by `-Dhadoop.version=x.x.x`

<a id="setup-basics-how_to_build--pvendor-repo-optional"></a>

##### `-Pvendor-repo` (optional)

enable 3rd party vendor repository (Cloudera, Hortonworks)

<a id="setup-basics-how_to_build--pexamples-optional"></a>

#### -Pexamples (optional)

Build examples under zeppelin-examples directory

<a id="setup-basics-how_to_build--build-command-examples"></a>

### Build command examples

Here are some examples with several options:

```bash
# build with spark-3.5, spark-scala-2.12./mvnw clean package -Pspark-3.5 -Pspark-scala-2.12 -DskipTests

# build with spark-3.5, spark-scala-2.13./mvnw clean package -Pspark-3.5 -Pspark-scala-2.13 -DskipTests
```

Ignite Interpreter

```bash
./mvnw clean package -Dignite.version=1.9.0 -DskipTests
```

<a id="setup-basics-how_to_build--optional-configurations"></a>

### Optional configurations

Here are additional configurations that could be optionally tuned using the trailing `-D` option for maven commands

Spark package

```bash
spark.archive # default spark-${spark.version}
spark.src.download.url # default http://d3kbcqa49mib13.cloudfront.net/${spark.archive}.tgz
spark.bin.download.url # default http://d3kbcqa49mib13.cloudfront.net/${spark.archive}-bin-without-hadoop.tgz
```

Py4J package

```bash
python.py4j.version # default 0.10.9.7
pypi.repo.url # default https://pypi.python.org/packages
python.py4j.repo.folder # default /64/5c/01e13b68e8caafece40d549f232c9b5677ad1016071a48d04cc3895acaa3
```

final URL location for Py4J package will be produced as following:

`${pypi.repo.url}${python.py4j.repo.folder}py4j-${python.py4j.version}.zip`

Frontend Maven Plugin configurations

```
plugin.frontend.nodeDownloadRoot # default https://nodejs.org/dist/
plugin.frontend.npmDownloadRoot # default https://registry.npmjs.org/npm/-/
plugin.frontend.yarnDownloadRoot # default https://github.com/yarnpkg/yarn/releases/download/
```

<a id="setup-basics-how_to_build--build-requirements"></a>

## Build requirements

<a id="setup-basics-how_to_build--install-requirements"></a>

### Install requirements

If you don't have requirements prepared, install it.
(The installation method may vary according to your environment, example is for Ubuntu.)

```bash
sudo apt-get update
sudo apt-get install git
sudo apt-get install openjdk-8-jdk
sudo apt-get install npm
sudo apt-get install libfontconfig
sudo apt-get install r-base-dev
sudo apt-get install r-cran-evaluate
```

*Notes:*
- Ensure node is installed by running `node --version`
- Ensure maven is running version 3.6.3 or higher with `./mvnw -version`
- Configure maven to use more memory than usual by `export MAVEN_OPTS="-Xmx2g -XX:MaxMetaspaceSize=512m"`

<a id="setup-basics-how_to_build--proxy-setting-optional"></a>

## Proxy setting (optional)

If you're behind the proxy, you'll need to configure maven and npm to pass through it.

First of all, configure maven in your `~/.m2/settings.xml`.

```xml
<settings>
  <proxies>
    <proxy>
      <id>proxy-http</id>
      <active>true</active>
      <protocol>http</protocol>
      <host>localhost</host>
      <port>3128</port>
      <!-- <username>usr</username>
      <password>pwd</password> -->
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
    <proxy>
      <id>proxy-https</id>
      <active>true</active>
      <protocol>https</protocol>
      <host>localhost</host>
      <port>3128</port>
      <!-- <username>usr</username>
      <password>pwd</password> -->
      <nonProxyHosts>localhost|127.0.0.1</nonProxyHosts>
    </proxy>
  </proxies>
</settings>
```

Then, next commands will configure npm.

```bash
npm config set proxy http://localhost:3128
npm config set https-proxy http://localhost:3128
npm config set registry "http://registry.npmjs.org/"
npm config set strict-ssl false
```

Configure git as well

```bash
git config --global http.proxy http://localhost:3128
git config --global https.proxy http://localhost:3128
git config --global url."http://".insteadOf git://
```

To clean up, set `active false` in Maven `settings.xml` and run these commands.

```bash
npm config rm proxy
npm config rm https-proxy
git config --global --unset http.proxy
git config --global --unset https.proxy
git config --global --unset url."http://".insteadOf
```

*Notes:*
- If you are behind NTLM proxy you can use [Cntlm Authentication Proxy](http://cntlm.sourceforge.net/).
- Replace `localhost:3128` with the standard pattern `http://user:pwd@host:port`.

<a id="setup-basics-how_to_build--package"></a>

## Package

To package the final distribution including the compressed archive, run:

```sh
./mvnw clean package -Pbuild-distr
```

To build a distribution with specific profiles, run:

```sh
./mvnw clean package -Pbuild-distr -Pspark-3.5
```

The profiles `-Pspark-3.5` can be adjusted if you wish to build to a specific spark versions.

The archive is generated under *`zeppelin-distribution/target`* directory

<a id="setup-basics-how_to_build--run-end-to-end-tests"></a>

## Run end-to-end tests

Zeppelin comes with a set of end-to-end acceptance tests driving headless selenium browser

```sh
# assumes zeppelin-server running on localhost:8080 (use -Durl=.. to override) mvn verify

# or take care of starting/stoping zeppelin-server from packaged zeppelin-distribuion/target mvn verify -P using-packaged-distr
```

---

---

<a id="setup-basics-hadoop_integration"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/basics/hadoop_integration.html -->

<!-- page_index: 38 -->

<a id="setup-basics-hadoop_integration--integrate-with-hadoop"></a>

# Integrate with hadoop

Hadoop is an optional component of zeppelin unless you need the following features

- Use hdfs to store notes.
- Use hdfs to store interpreter configuration
- Use hdfs to store recovery data
- Launch interpreter in yarn mode

<a id="setup-basics-hadoop_integration--requirements"></a>

## Requirements

Zeppelin 0.9 doesn't ship with hadoop dependencies, you need to include hadoop jars by yourself via the following steps

- Hadoop client (both 2.x and 3.x are supported) is installed.
- `$HADOOP_HOME/bin` is put in `PATH`. Because internally zeppelin will run command `hadoop classpath` to get all the hadoop jars and put them in the classpath of Zeppelin.
- Set `USE_HADOOP` as `true` in `zeppelin-env.sh`.

---

---

<a id="setup-basics-multi_user_support"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/basics/multi_user_support.html -->

<!-- page_index: 39 -->

<a id="setup-basics-multi_user_support--multi-user-support"></a>

# Multi-user Support

This page describes about multi-user support.

- multiple users login / logout using [Shiro Authentication](#setup-security-shiro_authentication)
- managing [Notebook Permission](#setup-security-notebook_authorization)
- how to setup [impersonation for interpreters](#usage-interpreter-user_impersonation)
- different contexts per user / note using [Interpreter Binding Mode](#usage-interpreter-interpreter_binding_mode)
- a paragraph in a notebook can be [Personalized](#usage-other_features-personalized_mode)
- propagates changes in notebooks through websocket in real-time

---

---

<a id="setup-deployment-spark_cluster_mode"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/deployment/spark_cluster_mode.html -->

<!-- page_index: 40 -->

<a id="setup-deployment-spark_cluster_mode--apache-zeppelin-on-spark-cluster-mode"></a>

# Apache Zeppelin on Spark Cluster Mode

<a id="setup-deployment-spark_cluster_mode--overview"></a>

## Overview

[Apache Spark](http://spark.apache.org/) has supported three cluster manager types([Standalone](http://spark.apache.org/docs/latest/spark-standalone.html), [Apache Mesos](http://spark.apache.org/docs/latest/running-on-mesos.html) and [Hadoop YARN](http://spark.apache.org/docs/latest/running-on-yarn.html)) so far.
This document will guide you how you can build and configure the environment on 3 types of Spark cluster manager with Apache Zeppelin using [Docker](https://www.docker.com/) scripts.
So [install docker](https://docs.docker.com/engine/installation/) on the machine first.

<a id="setup-deployment-spark_cluster_mode--spark-standalone-mode"></a>

## Spark standalone mode

[Spark standalone](http://spark.apache.org/docs/latest/spark-standalone.html) is a simple cluster manager included with Spark that makes it easy to set up a cluster.
You can simply set up Spark standalone environment with below steps.

> **Note :** Since Apache Zeppelin and Spark use same `8080` port for their web UI, you might need to change `zeppelin.server.port` in `conf/zeppelin-site.xml`.

<a id="setup-deployment-spark_cluster_mode--1.-build-docker-file"></a>

### 1. Build Docker file

You can find docker script files under `scripts/docker/spark-cluster-managers`.

```bash
cd $ZEPPELIN_HOME/scripts/docker/spark-cluster-managers/spark_standalone
docker build -t "spark_standalone" .
```

<a id="setup-deployment-spark_cluster_mode--2.-run-docker"></a>

### 2. Run docker

```bash
docker run -it \
-p 8080:8080 \
-p 7077:7077 \
-p 8888:8888 \
-p 8081:8081 \
-h sparkmaster \
--name spark_standalone \
spark_standalone bash;
```

Note that `sparkmaster` hostname used here to run docker container should be defined in your `/etc/hosts`.

<a id="setup-deployment-spark_cluster_mode--3.-configure-spark-interpreter-in-zeppelin"></a>

### 3. Configure Spark interpreter in Zeppelin

Set Spark master as `spark://<hostname>:7077` in Zeppelin **Interpreters** setting page.

![](assets/images/standalone-conf_abeda13808cb9d97.png)

<a id="setup-deployment-spark_cluster_mode--4.-run-zeppelin-with-spark-interpreter"></a>

### 4. Run Zeppelin with Spark interpreter

After running single paragraph with Spark interpreter in Zeppelin, browse `https://<hostname>:8080` and check whether Spark cluster is running well or not.

![](assets/images/spark-ui_cadee25558b1a357.png)

You can also simply verify that Spark is running well in Docker with below command.

```bash
ps -ef | grep spark
```

<a id="setup-deployment-spark_cluster_mode--spark-on-yarn-mode"></a>

## Spark on YARN mode

You can simply set up [Spark on YARN](http://spark.apache.org/docs/latest/running-on-yarn.html) docker environment with below steps.

> **Note :** Since Apache Zeppelin and Spark use same `8080` port for their web UI, you might need to change `zeppelin.server.port` in `conf/zeppelin-site.xml`.

<a id="setup-deployment-spark_cluster_mode--1.-build-docker-file-2"></a>

### 1. Build Docker file

You can find docker script files under `scripts/docker/spark-cluster-managers`.

```bash
cd $ZEPPELIN_HOME/scripts/docker/spark-cluster-managers/spark_yarn_cluster
docker build -t "spark_yarn" .
```

<a id="setup-deployment-spark_cluster_mode--2.-run-docker-2"></a>

### 2. Run docker

```bash
docker run -it \
 -p 5000:5000 \
 -p 9000:9000 \
 -p 9001:9001 \
 -p 8088:8088 \
 -p 8042:8042 \
 -p 8030:8030 \
 -p 8031:8031 \
 -p 8032:8032 \
 -p 8033:8033 \
 -p 8080:8080 \
 -p 7077:7077 \
 -p 8888:8888 \
 -p 8081:8081 \
 -p 50010:50010 \
 -p 50075:50075 \
 -p 50020:50020 \
 -p 50070:50070 \
 --name spark_yarn \
 -h sparkmaster \
 spark_yarn bash;
```

Note that `sparkmaster` hostname used here to run docker container should be defined in your `/etc/hosts`.

<a id="setup-deployment-spark_cluster_mode--3.-verify-running-spark-on-yarn."></a>

### 3. Verify running Spark on YARN.

You can simply verify the processes of Spark and YARN are running well in Docker with below command.

```bash
ps -ef
```

You can also check each application web UI for HDFS on `http://<hostname>:50070/`, YARN on `http://<hostname>:8088/cluster` and Spark on `http://<hostname>:8080/`.

<a id="setup-deployment-spark_cluster_mode--4.-configure-spark-interpreter-in-zeppelin"></a>

### 4. Configure Spark interpreter in Zeppelin

Set following configurations to `conf/zeppelin-env.sh`.

```bash
export HADOOP_CONF_DIR=[your_hadoop_conf_path]
export SPARK_HOME=[your_spark_home_path]
```

`HADOOP_CONF_DIR`(Hadoop configuration path) is defined in `/scripts/docker/spark-cluster-managers/spark_yarn_cluster/hdfs_conf`.

Don't forget to set Spark `spark.master` as `yarn-client` in Zeppelin **Interpreters** setting page like below.

![](assets/images/zeppelin-yarn-conf_0d443a3748ff0b3f.png)

<a id="setup-deployment-spark_cluster_mode--5.-run-zeppelin-with-spark-interpreter"></a>

### 5. Run Zeppelin with Spark interpreter

After running a single paragraph with Spark interpreter in Zeppelin, browse `http://<hostname>:8088/cluster/apps` and check Zeppelin application is running well or not.

![](assets/images/yarn-applications_b447f58ae279583a.png)

<a id="setup-deployment-spark_cluster_mode--spark-on-mesos-mode"></a>

## Spark on Mesos mode

You can simply set up [Spark on Mesos](http://spark.apache.org/docs/latest/running-on-mesos.html) docker environment with below steps.

<a id="setup-deployment-spark_cluster_mode--1.-build-docker-file-3"></a>

### 1. Build Docker file

```bash
cd $ZEPPELIN_HOME/scripts/docker/spark-cluster-managers/spark_mesos
docker build -t "spark_mesos" .
```

<a id="setup-deployment-spark_cluster_mode--2.-run-docker-3"></a>

### 2. Run docker

```bash
docker run --net=host -it \
-p 8080:8080 \
-p 7077:7077 \
-p 8888:8888 \
-p 8081:8081 \
-p 8082:8082 \
-p 5050:5050 \
-p 5051:5051 \
-p 4040:4040 \
-h sparkmaster \
--name spark_mesos \
spark_mesos bash;
```

Note that `sparkmaster` hostname used here to run docker container should be defined in your `/etc/hosts`.

<a id="setup-deployment-spark_cluster_mode--3.-verify-running-spark-on-mesos."></a>

### 3. Verify running Spark on Mesos.

You can simply verify the processes of Spark and Mesos are running well in Docker with below command.

```bash
ps -ef
```

You can also check each application web UI for Mesos on `http://<hostname>:5050/cluster` and Spark on `http://<hostname>:8080/`.

<a id="setup-deployment-spark_cluster_mode--4.-configure-spark-interpreter-in-zeppelin-2"></a>

### 4. Configure Spark interpreter in Zeppelin

```bash
export MESOS_NATIVE_JAVA_LIBRARY=[PATH OF libmesos.so]
export SPARK_HOME=[PATH OF SPARK HOME]
```

Don't forget to set Spark `spark.master` as `mesos://127.0.1.1:5050` in Zeppelin **Interpreters** setting page like below.

![](assets/images/zeppelin-mesos-conf_87647424452d2de7.png)

<a id="setup-deployment-spark_cluster_mode--5.-run-zeppelin-with-spark-interpreter-2"></a>

### 5. Run Zeppelin with Spark interpreter

After running a single paragraph with Spark interpreter in Zeppelin, browse `http://<hostname>:5050/#/frameworks` and check Zeppelin application is running well or not.

![](assets/images/mesos-frameworks_59bf8eb06f6c7195.png)

<a id="setup-deployment-spark_cluster_mode--troubleshooting-for-spark-on-mesos"></a>

### Troubleshooting for Spark on Mesos

- If you have problem with hostname, use `--add-host` option when executing `dockerrun`

```
## use `--add-host=moby:127.0.0.1` option to resolve
## since docker container couldn't resolve `moby`

: java.net.UnknownHostException: moby: moby: Name or service not known
        at java.net.InetAddress.getLocalHost(InetAddress.java:1496)
        at org.apache.spark.util.Utils$.findLocalInetAddress(Utils.scala:789)
        at org.apache.spark.util.Utils$.org$apache$spark$util$Utils$$localIpAddress$lzycompute(Utils.scala:782)
        at org.apache.spark.util.Utils$.org$apache$spark$util$Utils$$localIpAddress(Utils.scala:782)
```

- If you have problem with mesos master, try `mesos://127.0.0.1` instead of `mesos://127.0.1.1`

```
I0103 20:17:22.329269   340 sched.cpp:330] New master detected at master@127.0.1.1:5050
I0103 20:17:22.330749   340 sched.cpp:341] No credentials provided. Attempting to register without authentication
W0103 20:17:22.333531   340 sched.cpp:736] Ignoring framework registered message because it was sentfrom 'master@127.0.0.1:5050' instead of the leading master 'master@127.0.1.1:5050'
W0103 20:17:24.040252   339 sched.cpp:736] Ignoring framework registered message because it was sentfrom 'master@127.0.0.1:5050' instead of the leading master 'master@127.0.1.1:5050'
W0103 20:17:26.150250   339 sched.cpp:736] Ignoring framework registered message because it was sentfrom 'master@127.0.0.1:5050' instead of the leading master 'master@127.0.1.1:5050'
W0103 20:17:26.737604   339 sched.cpp:736] Ignoring framework registered message because it was sentfrom 'master@127.0.0.1:5050' instead of the leading master 'master@127.0.1.1:5050'
W0103 20:17:35.241714   336 sched.cpp:736] Ignoring framework registered message because it was sentfrom 'master@127.0.0.1:5050' instead of the leading master 'master@127.0.1.1:5050'
```

---

---

<a id="setup-deployment-flink_and_spark_cluster"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/deployment/flink_and_spark_cluster.html -->

<!-- page_index: 41 -->

# Install with Flink and Spark cluster

This document is outdated, it is not verified in the latest Zeppelin.

<a id="setup-deployment-flink_and_spark_cluster--install-with-flink-and-spark-cluster"></a>

# Install with Flink and Spark cluster

This tutorial is extremely entry-level. It assumes no prior knowledge of Linux, git, or other tools. If you carefully type what I tell you when I tell you, you should be able to get Zeppelin running.

<a id="setup-deployment-flink_and_spark_cluster--installing-zeppelin-with-flink-and-spark-in-cluster-mode"></a>

## Installing Zeppelin with Flink and Spark in cluster mode

This tutorial assumes the user has a machine (real or [virtual](https://www.virtualbox.org/wiki/Downloads) with a fresh, minimal installation of [Ubuntu 14.04.3 Server](http://www.ubuntu.com/download/server).

**Note:** On the size requirements of the Virtual Machine, some users reported trouble when using the default virtual machine sizes, specifically that the hard drive needed to be at least 16GB- other users did not have this issue.

There are many good tutorials on how to install Ubuntu Server on a virtual box, [here is one of them](http://ilearnstack.com/2013/04/13/setting-ubuntu-vm-in-virtualbox/)

<a id="setup-deployment-flink_and_spark_cluster--required-programs"></a>

### Required Programs

Assuming the minimal install, there are several programs that we will need to install before Zeppelin, Flink, and Spark.

- git
- openssh-server
- OpenJDK 11
- Maven

For git, openssh-server, and OpenJDK 7 we will be using the apt package manager.

<a id="setup-deployment-flink_and_spark_cluster--git"></a>

##### git

From the command prompt:

```bash
sudo apt-get install git
```

<a id="setup-deployment-flink_and_spark_cluster--openssh-server"></a>

##### openssh-server

```bash
sudo apt-get install openssh-server
```

<a id="setup-deployment-flink_and_spark_cluster--openjdk-11"></a>

##### OpenJDK 11

```bash
sudo apt-get install openjdk-11-jdk
```

<a id="setup-deployment-flink_and_spark_cluster--installing-zeppelin"></a>

### Installing Zeppelin

This provides a quick overview of Zeppelin installation from source, however the reader is encouraged to review the [Zeppelin Installation Guide](#quickstart-install)

From the command prompt:
Clone Zeppelin.

```bash
git clone https://github.com/apache/zeppelin.git
```

Enter the Zeppelin root directory.

```bash
cd zeppelin
```

Package Zeppelin.

```bash
./mvnw clean package -DskipTests -Pspark-3.5 -Pflink-1.17
```

`-DskipTests` skips build tests- you're not developing (yet), so you don't need to do tests, the clone version *should* build.

`-Pspark-3.5` tells maven to build a Zeppelin with Spark 3.5. This is important because Zeppelin has its own Spark interpreter and the versions must be the same.

`-Pflink-1.17` tells maven to build a Zeppelin with Flink 1.17.

**Note:** You can build against any version of Spark that has a Zeppelin build profile available. The key is to make sure you check out the matching version of Spark to build. At the time of this writing, Spark 3.5 was the most recent Spark version available.

**Note:** On build failures. Having installed Zeppelin close to 30 times now, I will tell you that sometimes the build fails for seemingly no reason.
As long as you didn't edit any code, it is unlikely the build is failing because of something you did. What does tend to happen, is some dependency that maven is trying to download is unreachable. If your build fails on this step here are some tips:

- Don't get discouraged.
- Scroll up and read through the logs. There will be clues there.
- Retry (that is, run the `./mvnw clean package -DskipTests -Pspark-3.5` again)
- If there were clues that a dependency couldn't be downloaded wait a few hours or even days and retry again. Open source software when compiling is trying to download all of the dependencies it needs, if a server is off-line there is nothing you can do but wait for it to come back.
- Make sure you followed all of the steps carefully.
- Ask the community to help you. Go [here](http://zeppelin.apache.org/community.html) and join the user mailing list. People are there to help you. Make sure to copy and paste the build output (everything that happened in the console) and include that in your message.

Start the Zeppelin daemon.

```bash
bin/zeppelin-daemon.sh start
```

Use `ifconfig` to determine the host machine's IP address. If you are not familiar with how to do this, a fairly comprehensive post can be found [here](http://www.cyberciti.biz/faq/how-to-find-out-the-ip-address-assigned-to-eth0-and-display-ip-only/).

Open a web-browser on a machine connected to the same network as the host (or in the host operating system if using a virtual machine). Navigate to http://`yourip`:8080, where yourip is the IP address you found in `ifconfig`.

See the [Zeppelin tutorial](#quickstart-tutorial) for basic Zeppelin usage. It is also advised that you take a moment to check out the tutorial notebook that is included with each Zeppelin install, and to familiarize yourself with basic notebook functionality.

<a id="setup-deployment-flink_and_spark_cluster--flink-test"></a>

##### Flink Test

Create a new notebook named "Flink Test" and copy and paste the following code.

```scala
%flink  // let Zeppelin know what interpreter to use.

val text = benv.fromElements("In the time of chimpanzees, I was a monkey",   // some lines of text to analyze
"Butane in my veins and I'm out to cut the junkie",
"With the plastic eyeballs, spray paint the vegetables",
"Dog food stalls with the beefcake pantyhose",
"Kill the headlights and put it in neutral",
"Stock car flamin' with a loser in the cruise control",
"Baby's in Reno with the Vitamin D",
"Got a couple of couches, sleep on the love seat",
"Someone came in sayin' I'm insane to complain",
"About a shotgun wedding and a stain on my shirt",
"Don't believe everything that you breathe",
"You get a parking violation and a maggot on your sleeve",
"So shave your face with some mace in the dark",
"Savin' all your food stamps and burnin' down the trailer park",
"Yo, cut it")

/*  The meat and potatoes:
        this tells Flink to iterate through the elements, in this case strings,
        transform the string to lower case and split the string at white space into individual words
        then finally aggregate the occurrence of each word.

        This creates the count variable which is a list of tuples of the form (word, occurances)

counts.collect().foreach(println(_))  // execute the script and print each element in the counts list

*/
val counts = text.flatMap{ _.toLowerCase.split("\\W+") }.map { (_,1) }.groupBy(0).sum(1)

counts.collect().foreach(println(_))  // execute the script and print each element in the counts list
```

Run the code to make sure the built-in Zeppelin Flink interpreter is working properly.

<a id="setup-deployment-flink_and_spark_cluster--spark-test"></a>

##### Spark Test

Create a new notebook named "Spark Test" and copy and paste the following code.

```scala
%spark // let Zeppelin know what interpreter to use.

val text = sc.parallelize(List("In the time of chimpanzees, I was a monkey",  // some lines of text to analyze
"Butane in my veins and I'm out to cut the junkie",
"With the plastic eyeballs, spray paint the vegetables",
"Dog food stalls with the beefcake pantyhose",
"Kill the headlights and put it in neutral",
"Stock car flamin' with a loser in the cruise control",
"Baby's in Reno with the Vitamin D",
"Got a couple of couches, sleep on the love seat",
"Someone came in sayin' I'm insane to complain",
"About a shotgun wedding and a stain on my shirt",
"Don't believe everything that you breathe",
"You get a parking violation and a maggot on your sleeve",
"So shave your face with some mace in the dark",
"Savin' all your food stamps and burnin' down the trailer park",
"Yo, cut it"))


/*  The meat and potatoes:
        this tells spark to iterate through the elements, in this case strings,
        transform the string to lower case and split the string at white space into individual words
        then finally aggregate the occurrence of each word.

        This creates the count variable which is a list of tuples of the form (word, occurances)
*/
val counts = text.flatMap { _.toLowerCase.split("\\W+") }
                 .map { (_,1) }
                 .reduceByKey(_ + _)

counts.collect().foreach(println(_))  // execute the script and print each element in the counts list
```

Run the code to make sure the built-in Zeppelin Flink interpreter is working properly.

Finally, stop the Zeppelin daemon. From the command prompt run:

```bash
bin/zeppelin-daemon.sh stop
```

<a id="setup-deployment-flink_and_spark_cluster--installing-clusters"></a>

### Installing Clusters

<a id="setup-deployment-flink_and_spark_cluster--flink-cluster"></a>

##### Flink Cluster

<a id="setup-deployment-flink_and_spark_cluster--download-binaries"></a>

###### Download Binaries

Building from source is recommended where possible, for simplicity in this tutorial we will download Flink and Spark Binaries.

To download the Flink Binary use `wget`

```bash
wget -O flink-1.17.1-bin-scala_2.12.tgz "https://www.apache.org/dyn/closer.lua/flink/flink-1.17.1/flink-1.17.1-bin-scala_2.12.tgz?action=download"
tar -xzvf flink-1.17.1-bin-scala_2.12.tgz
```

This will download Flink 1.17.1.

Start the Flink Cluster.

```bash
flink-1.17.1/bin/start-cluster.sh
```

<a id="setup-deployment-flink_and_spark_cluster--building-from-source"></a>

###### Building From source

If you wish to build Flink from source, the following will be instructive. Note that if you have downloaded and used the binary version this should be skipped. The changing nature of build tools and versions across platforms makes this section somewhat precarious. For example, Java8 and Maven 3.0.3 are recommended for building Flink, which are not recommended for Zeppelin at the time of writing. If the user wishes to attempt to build from source, this section will provide some reference. If errors are encountered, please contact the Apache Flink community.

See the [Flink Installation guide](https://github.com/apache/flink/blob/master/README.md) for more detailed instructions.

Return to the directory where you have been downloading, this tutorial assumes that is `$HOME`. Clone Flink, check out release-1.17.1, and build.

```bash
cd $HOME
git clone https://github.com/apache/flink.git
cd flink
git checkout release-1.17.1
mvn clean install -DskipTests
```

Start the Flink Cluster in stand-alone mode

```bash
build-target/bin/start-cluster.sh
```

<a id="setup-deployment-flink_and_spark_cluster--ensure-the-cluster-is-up"></a>

###### Ensure the cluster is up

In a browser, navigate to http://`yourip`:8082 to see the Flink Web-UI. Click on 'Task Managers' in the left navigation bar. Ensure there is at least one Task Manager present.

![alt text](/docs/0.12.0/assets/themes/zeppelin/img/screenshots/flink-webui.png "The Flink Web-UI")

If no task managers are present, restart the Flink cluster with the following commands:

(if binaries)

```bash
flink-1.17.1/bin/stop-cluster.sh
flink-1.17.1/bin/start-cluster.sh
```

(if built from source)

```bash
build-target/bin/stop-cluster.sh
build-target/bin/start-cluster.sh
```

<a id="setup-deployment-flink_and_spark_cluster--spark-cluster"></a>

##### Spark Cluster

<a id="setup-deployment-flink_and_spark_cluster--download-binaries-2"></a>

###### Download Binaries

Building from source is recommended where possible, for simplicity in this tutorial we will download Flink and Spark Binaries.

Using binaries is also

To download the Spark Binary use `wget`

```bash
wget -O spark-3.5.2-bin-hadoop3.tgz "https://www.apache.org/dyn/closer.lua/spark/spark-3.5.2/spark-3.5.2-bin-hadoop3.tgz?action=download"
tar -xzvf spark-3.5.2-bin-hadoop3.tgz
mv spark-3.5.2-bin-hadoop3 spark
```

This will download Spark 3.5.2, compatible with Hadoop 3. You do not have to install Hadoop for this binary to work, but if you are using Hadoop, please change `3` to your appropriate version.

<a id="setup-deployment-flink_and_spark_cluster--building-from-source-2"></a>

###### Building From source

Spark is an extraordinarily large project, which takes considerable time to download and build. It is also prone to build failures for similar reasons listed in the Flink section. If the user wishes to attempt to build from source, this section will provide some reference. If errors are encountered, please contact the Apache Spark community.

See the [Spark Installation](https://github.com/apache/spark/blob/master/README.md) guide for more detailed instructions.

Return to the directory where you have been downloading, this tutorial assumes that is $HOME. Clone Spark, check out branch-3.5, and build.

```bash
cd $HOME
```

Clone, check out, and build Spark version 3.5.x.

```bash
git clone https://github.com/apache/spark.git
cd spark
git checkout branch-3.5
mvn clean package -DskipTests
```

<a id="setup-deployment-flink_and_spark_cluster--start-the-spark-cluster"></a>

###### Start the Spark cluster

Return to the `$HOME` directory.

```bash
cd $HOME
```

Start the Spark cluster in stand alone mode, specifying the webui-port as some port other than 8080 (the webui-port of Zeppelin).

```bash
spark/sbin/start-master.sh --webui-port 8082
```

**Note:** Why `--webui-port 8082`? There is a digression toward the end of this document that explains this.

Open a browser and navigate to http://`yourip`:8082 to ensure the Spark master is running.

![alt text](/docs/0.12.0/assets/themes/zeppelin/img/screenshots/spark-master-webui1.png "It should look like this...")

Toward the top of the page there will be a *URL*: spark://`yourhost`:7077. Note this URL, the Spark Master URI, it will be needed in subsequent steps.

Start the slave using the URI from the Spark master WebUI:

```bash
spark/sbin/start-slave.sh spark://yourhostname:7077
```

Return to the root directory and start the Zeppelin daemon.

```bash
cd $HOME

zeppelin/bin/zeppelin-daemon.sh start
```

<a id="setup-deployment-flink_and_spark_cluster--configure-interpreters"></a>

##### Configure Interpreters

Open a web browser and go to the Zeppelin web-ui at http://yourip:8080.

Now go back to the Zeppelin web-ui at http://`yourip`:8080 and this time click on *anonymous* at the top right, which will open a drop-down menu, select *Interpreters* to enter interpreter configuration.

In the Spark section, click the edit button in the top right corner to make the property values editable (looks like a pencil).
The only field that needs to be edited in the Spark interpreter is the `spark.master` field. Change this value from `local[*]` to the URL you used to start the slave, mine was `spark://ubuntu:7077`.

Click *Save* to update the parameters, and click *OK* when it asks you about restarting the interpreter.

Now scroll down to the Flink section. Click the edit button and change the value of *host* from `local` to `localhost`. Click *Save* again.

Reopen the examples and execute them again (I.e. you need to click the play button at the top of the screen, or the button on the paragraph .

You should be able check the Flink and Spark webuis (at something like http://`yourip`:8081, http://`yourip`:8082, http://`yourip`:8083) and see that jobs have been run against the clusters.

**Digression** Sorry to be vague and use terms such as 'something like', but exactly what web-ui is at what port is going to depend on what order you started things.
What is really going on here is you are pointing your browser at specific ports, namely 8081, 8082, and 8083. Flink and Spark all want to put their web-ui on port 8080, but are
well behaved and will take the next port available. Since Zeppelin started first, it will get port 8080. When Flink starts (assuming you started Flink first), it will try to bind to
port 8080, see that it is already taken, and go to the next one available, hopefully 8081. Spark has a webui for the master and the slave, so when they start they will try to bind to 8080
already taken by Zeppelin), then 8081 (already taken by Flink's webui), then 8082. If everything goes smoothy and you followed the directions precisely, the webuis should be 8081 and 8082.
It *is* possible to specify the port you want the webui to bind to (at the command line by passing the `--webui-port <port>` flag when you start the Flink and Spark, where `<port>` is the port
you want to see that webui on. You can also set the default webui port of Spark and Flink (and Zeppelin) in the configuration files, but this is a tutorial for novices and slightly out of scope.

<a id="setup-deployment-flink_and_spark_cluster--next-steps"></a>

### Next Steps

Check out the [tutorial](#quickstart-tutorial) for more cool things you can do with your new toy!

[Join the community](http://zeppelin.apache.org/community.html), ask questions and contribute! Every little bit helps.

---

---

<a id="setup-deployment-cdh"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/deployment/cdh.html -->

<!-- page_index: 42 -->

<a id="setup-deployment-cdh--apache-zeppelin-on-cdh"></a>

# Apache Zeppelin on CDH

<a id="setup-deployment-cdh--1.-import-cloudera-quickstart-docker-image"></a>

### 1. Import Cloudera QuickStart Docker image

> [Cloudera](http://www.cloudera.com/) has officially provided CDH Docker Hub in their own container. Please check [this guide page](https://hub.docker.com/r/cloudera/quickstart/) for more information.

You can import the Docker image by pulling it from Cloudera Docker Hub.

```bash
docker pull cloudera/quickstart:latest
```

<a id="setup-deployment-cdh--2.-run-docker"></a>

### 2. Run docker

```bash
docker run -it \
 -p 80:80 \
 -p 4040:4040 \
 -p 8020:8020 \
 -p 8022:8022 \
 -p 8030:8030 \
 -p 8032:8032 \
 -p 8033:8033 \
 -p 8040:8040 \
 -p 8042:8042 \
 -p 8088:8088 \
 -p 8480:8480 \
 -p 8485:8485 \
 -p 8888:8888 \
 -p 9083:9083 \
 -p 10020:10020 \
 -p 10033:10033 \
 -p 18088:18088 \
 -p 19888:19888 \
 -p 25000:25000 \
 -p 25010:25010 \
 -p 25020:25020 \
 -p 50010:50010 \
 -p 50020:50020 \
 -p 50070:50070 \
 -p 50075:50075 \
 -h quickstart.cloudera --privileged=true \
 agitated_payne_backup /usr/bin/docker-quickstart;
```

<a id="setup-deployment-cdh--3.-verify-running-cdh"></a>

### 3. Verify running CDH

To verify the application is running well, check the web UI for HDFS on `http://<hostname>:50070/` and YARN on `http://<hostname>:8088/cluster`.

<a id="setup-deployment-cdh--4.-configure-spark-interpreter-in-zeppelin"></a>

### 4. Configure Spark interpreter in Zeppelin

Set following configurations to `conf/zeppelin-env.sh`.

```bash
export HADOOP_CONF_DIR=[your_hadoop_conf_path]
export SPARK_HOME=[your_spark_home_path]
```

`HADOOP_CONF_DIR`(Hadoop configuration path) is defined in `/scripts/docker/spark-cluster-managers/cdh/hdfs_conf`.

Don't forget to set Spark `spark.master` as `yarn-client` in Zeppelin **Interpreters** setting page like below.

![](assets/images/zeppelin-yarn-conf_0d443a3748ff0b3f.png)

<a id="setup-deployment-cdh--5.-run-zeppelin-with-spark-interpreter"></a>

### 5. Run Zeppelin with Spark interpreter

After running a single paragraph with Spark interpreter in Zeppelin,

![](assets/images/zeppelin-with-cdh_3e91925d117b97d7.png)

browse `http://<hostname>:8088/cluster/apps` to check Zeppelin application is running well or not.

![](assets/images/cdh-yarn-applications_44805d381105aea9.png)

---

---

<a id="setup-deployment-virtual_machine"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/deployment/virtual_machine.html -->

<!-- page_index: 43 -->

<a id="setup-deployment-virtual_machine--apache-zeppelin-on-vagrant-virtual-machine"></a>

# Apache Zeppelin on Vagrant Virtual Machine

<a id="setup-deployment-virtual_machine--overview"></a>

## Overview

Apache Zeppelin distribution includes a script directory `scripts/vagrant/zeppelin-dev`

This script creates a virtual machine that launches a repeatable, known set of core dependencies required for developing Zeppelin. It can also be used to run an existing Zeppelin build if you don't plan to build from source.
For PySpark users, this script includes several helpful [Python Libraries](#setup-deployment-virtual_machine--python-extras).
For SparkR users, this script includes several helpful [R Libraries](#setup-deployment-virtual_machine--r-extras).

<a id="setup-deployment-virtual_machine--prerequisites"></a>

### Prerequisites

This script requires three applications, [Ansible](https://www.ansible.com/ "Ansible"), [Vagrant](http://www.vagrantup.com "Vagrant") and [Virtual Box](https://www.virtualbox.org/ "Virtual Box"). All of these applications are freely available as Open Source projects and extremely easy to set up on most operating systems.

<a id="setup-deployment-virtual_machine--create-a-zeppelin-ready-vm"></a>

## Create a Zeppelin Ready VM

If you are running Windows and don't yet have python installed, [install Python 2.7.x](https://www.python.org/downloads/release/python-2710/) first.

1. Download and Install Vagrant: [Vagrant Downloads](http://www.vagrantup.com/downloads.html)
2. Install Ansible: [Ansible Python pip install](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#pip-install)


```bash
sudo easy_install pip
sudo pip install ansible
ansible --version
```

   After then, please check whether it reports **ansible version 1.9.2 or higher**.
3. Install Virtual Box: [Virtual Box Downloads](https://www.virtualbox.org/ "Virtual Box")
4. Type `vagrant up` from within the `/scripts/vagrant/zeppelin-dev` directory

Thats it ! You can now run `vagrant ssh` and this will place you into the guest machines terminal prompt.

If you don't wish to build Zeppelin from scratch, run the z-manager installer script while running in the guest VM:

```bash
curl -fsSL https://raw.githubusercontent.com/NFLabs/z-manager/master/zeppelin-installer.sh | bash
```

<a id="setup-deployment-virtual_machine--building-zeppelin"></a>

## Building Zeppelin

You can now

```bash
git clone git://git.apache.org/zeppelin.git
```

into a directory on your host machine, or directly in your virtual machine.

Cloning Zeppelin into the `/scripts/vagrant/zeppelin-dev` directory from the host, will allow the directory to be shared between your host and the guest machine.

Cloning the project again may seem counter intuitive, since this script likely originated from the project repository. Consider copying just the vagrant/zeppelin-dev script from the Zeppelin project as a stand alone directory, then once again clone the specific branch you wish to build.

Synced folders enable Vagrant to sync a folder on the host machine to the guest machine, allowing you to continue working on your project's files on your host machine, but use the resources in the guest machine to compile or run your project. *[(1) Synced Folder Description from Vagrant Up](https://docs.vagrantup.com/v2/synced-folders/index.html)*

By default, Vagrant will share your project directory (the directory with the Vagrantfile) to `/vagrant`. Which means you should be able to build within the guest machine after you
`cd /vagrant/zeppelin`

<a id="setup-deployment-virtual_machine--what-s-in-this-vm"></a>

## What's in this VM?

Running the following commands in the guest machine should display these expected versions:

- `node --version` should report *v0.12.7*

The virtual machine consists of:

- Ubuntu Server 14.04 LTS
- Node.js 0.12.7
- npm 2.11.3
- ruby 1.9.3 + rake, make and bundler (only required if building jekyll documentation)
- Maven 3.3.9
- Git
- Unzip
- libfontconfig to avoid phatomJs missing dependency issues
- openjdk-7-jdk
- Python addons: pip, matplotlib, scipy, numpy, pandas
- [R](https://www.r-project.org/) and R Packages required to run the R Interpreter and the related R tutorial notebook, including: Knitr, devtools, repr, rCharts, ggplot2, googleVis, mplot, htmltools, base64enc, data.table

<a id="setup-deployment-virtual_machine--how-to-build-run-zeppelin"></a>

## How to build & run Zeppelin

This assumes you've already cloned the project either on the host machine in the zeppelin-dev directory (to be shared with the guest machine) or cloned directly into a directory while running inside the guest machine. The following build steps will also include Python and R support via PySpark and SparkR:

```bash
cd /zeppelin
./mvnw clean package -Pspark-1.6 -Phadoop-2.4 -DskipTests
./bin/zeppelin-daemon.sh start
```

On your host machine browse to `http://localhost:8080/`

If you [turned off port forwarding](#setup-deployment-virtual_machine--tweaking-the-virtual-machine) in the `Vagrantfile` browse to `http://192.168.51.52:8080`

<a id="setup-deployment-virtual_machine--tweaking-the-virtual-machine"></a>

## Tweaking the Virtual Machine

If you plan to run this virtual machine along side other Vagrant images, you may wish to bind the virtual machine to a specific IP address, and not use port fowarding from your local host.

Comment out the `forward_port` line, and uncomment the `private_network` line in Vagrantfile. The subnet that works best for your local network will vary so adjust `192.168.*.*` accordingly.

```
#config.vm.network "forwarded_port", guest: 8080, host: 8080
config.vm.network "private_network", ip: "192.168.51.52"
```

`vagrant halt` followed by `vagrant up` will restart the guest machine bound to the IP address of `192.168.51.52`.
This approach usually is typically required if running other virtual machines that discover each other directly by IP address, such as Spark Masters and Slaves as well as Cassandra Nodes, Elasticsearch Nodes, and other Spark data sources. You may wish to launch nodes in virtual machines with IP addresses in a subnet that works for your local network, such as: 192.168.51.53, 192.168.51.54, 192.168.51.53, etc..

<a id="setup-deployment-virtual_machine--extras"></a>

## Extras

<a id="setup-deployment-virtual_machine--python-extras"></a>

### Python Extras

With Zeppelin running, **Numpy**, **SciPy**, **Pandas** and **Matplotlib** will be available. Create a pyspark notebook, and try the below code.

```python
%pyspark

import numpy
import scipy
import pandas
import matplotlib

print "numpy " + numpy.__version__
print "scipy " + scipy.__version__
print "pandas " + pandas.__version__
print "matplotlib " + matplotlib.__version__
```

To Test plotting using Matplotlib into a rendered `%html` SVG image, try

```python
%pyspark

import matplotlib
matplotlib.use('Agg')   # turn off interactive charting so this works for server side SVG rendering
import matplotlib.pyplot as plt
import numpy as np
import StringIO

# clear out any previous plots on this note
plt.clf()

def show(p):
    img = StringIO.StringIO()
    p.savefig(img, format='svg')
    img.seek(0)
    print "%html <div style='width:600px'>" + img.buf + "</div>"

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

plt.barh(y_pos, performance, xerr=error, align='center', alpha=0.4)
plt.yticks(y_pos, people)
plt.xlabel('Performance')
plt.title('How fast do you want to go today?')

show(plt)
```

<a id="setup-deployment-virtual_machine--r-extras"></a>

### R Extras

With zeppelin running, an R Tutorial notebook will be available. The R packages required to run the examples and graphs in this tutorial notebook were installed by this virtual machine.
The installed R Packages include: `knitr`, `devtools`, `repr`, `rCharts`, `ggplot2`, `googleVis`, `mplot`, `htmltools`, `base64enc`, `data.table`.

---

---

<a id="setup-security-authentication_nginx"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/security/authentication_nginx.html -->

<!-- page_index: 44 -->

<a id="setup-security-authentication_nginx--authentication-for-nginx"></a>

# Authentication for NGINX

[Build in authentication mechanism](#setup-security-shiro_authentication) is recommended way for authentication. In case of you want authenticate using NGINX and [HTTP basic auth](https://en.wikipedia.org/wiki/Basic_access_authentication), please read this document.

<a id="setup-security-authentication_nginx--http-basic-authentication-using-nginx"></a>

## HTTP Basic Authentication using NGINX

> **Quote from Wikipedia:** NGINX is a web server. It can act as a reverse proxy server for HTTP, HTTPS, SMTP, POP3, and IMAP protocols, as well as a load balancer and an HTTP cache.

So you can use NGINX server as proxy server to serve HTTP Basic Authentication as a separate process along with Zeppelin server.
Here are instructions how to accomplish the setup NGINX as a front-end authentication server and connect Zeppelin at behind.

This instruction based on Ubuntu 14.04 LTS but may work with other OS with few configuration changes.

1. Install NGINX server on your server instance

   You can install NGINX server with same box where zeppelin installed or separate box where it is dedicated to serve as proxy server.


```bash
$ apt-get install nginx
```

   > **NOTE :** On pre 1.3.13 version of NGINX, Proxy for Websocket may not fully works. Please use latest version of NGINX. See: [NGINX documentation](https://www.nginx.com/blog/websocket-nginx/).
2. Setup init script in NGINX

   In most cases, NGINX configuration located under `/etc/nginx/sites-available`. Create your own configuration or add your existing configuration at `/etc/nginx/sites-available`.


```bash
$ cd /etc/nginx/sites-available
$ touch my-zeppelin-auth-setting
```

   Now add this script into `my-zeppelin-auth-setting` file. You can comment out `optional` lines If you want serve Zeppelin under regular HTTP 80 Port.


```
upstream zeppelin {
    server [YOUR-ZEPPELIN-SERVER-IP]:[YOUR-ZEPPELIN-SERVER-PORT];   # For security, It is highly recommended to make this address/port as non-public accessible
}

# Zeppelin Website server {listen [YOUR-ZEPPELIN-WEB-SERVER-PORT]; listen 443 ssl; # optional, to serve HTTPS connection server_name [YOUR-ZEPPELIN-SERVER-HOST]; # for example: zeppelin.mycompany.com

    ssl_certificate [PATH-TO-YOUR-CERT-FILE];            # optional, to serve HTTPS connection
    ssl_certificate_key [PATH-TO-YOUR-CERT-KEY-FILE];    # optional, to serve HTTPS connection

    if ($ssl_protocol = "") {
        rewrite ^ https://$host$request_uri? permanent;  # optional, to force use of HTTPS
    }

    location / {    # For regular websever support
        proxy_pass http://zeppelin;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X-NginX-Proxy true;
        proxy_redirect off;
        auth_basic "Restricted";
        auth_basic_user_file /etc/nginx/.htpasswd;
    }

    location /ws {  # For websocket support
        proxy_pass http://zeppelin/ws;
        proxy_http_version 1.1;
        proxy_set_header Upgrade websocket;
        proxy_set_header Connection upgrade;
        proxy_read_timeout 86400;
    }
}
```

   Then make a symbolic link to this file from `/etc/nginx/sites-enabled/` to enable configuration above when NGINX reloads.


```bash
$ ln -s /etc/nginx/sites-enabled/my-zeppelin-auth-setting /etc/nginx/sites-available/my-zeppelin-auth-setting
```

3. Setup user credential into `.htpasswd` file and restart server

   Now you need to setup `.htpasswd` file to serve list of authenticated user credentials for NGINX server.


```bash
$ cd /etc/nginx
$ htpasswd -c htpasswd [YOUR-ID] NEW passwd: [YOUR-PASSWORD] RE-type new passwd: [YOUR-PASSWORD-AGAIN]
```

   Or you can use your own apache `.htpasswd` files in other location for setting up property: `auth_basic_user_file`

   Restart NGINX server.


```bash
$ service nginx restart
```

   Then check HTTP Basic Authentication works in browser. If you can see regular basic auth popup and then able to login with credential you entered into `.htpasswd` you are good to go.
4. More security consideration

- Using HTTPS connection with Basic Authentication is highly recommended since basic auth without encryption may expose your important credential information over the network.
- Using [Shiro Security feature built-into Zeppelin](#setup-security-shiro_authentication) is recommended if you prefer all-in-one solution for authentication but NGINX may provides ad-hoc solution for re-use authentication served by your system's NGINX server or in case of you need to separate authentication from zeppelin server.
- It is recommended to isolate direct connection to Zeppelin server from public internet or external services to secure your zeppelin instance from unexpected attack or problems caused by public zone.

<a id="setup-security-authentication_nginx--another-option"></a>

## Another option

Another option is to have an authentication server that can verify user credentials in an LDAP server.
If an incoming request to the Zeppelin server does not have a cookie with user information encrypted with the authentication server public key, the user
is redirected to the authentication server. Once the user is verified, the authentication server redirects the browser to a specific URL in the Zeppelin server which sets the authentication cookie in the browser.
The end result is that all requests to the Zeppelin web server have the authentication cookie which contains user and groups information.

---

---

<a id="setup-security-shiro_authentication"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/security/shiro_authentication.html -->

<!-- page_index: 45 -->

<a id="setup-security-shiro_authentication--apache-shiro-authentication-for-apache-zeppelin"></a>

# Apache Shiro authentication for Apache Zeppelin

<a id="setup-security-shiro_authentication--overview"></a>

## Overview

[Apache Shiro](http://shiro.apache.org/) is a powerful and easy-to-use Java security framework that performs authentication, authorization, cryptography, and session management. In this documentation, we will explain step by step how Shiro works for Zeppelin notebook authentication.

When you connect to Apache Zeppelin, you will be asked to enter your credentials. Once you logged in, then you have access to all notes including other user's notes.

<a id="setup-security-shiro_authentication--important-note"></a>

## Important Note

By default, Zeppelin allows anonymous access. It is strongly recommended that you consider setting up Apache Shiro for authentication (as described in this document, see 2 Secure the Websocket channel), or only deploy and use Zeppelin in a secured and trusted environment.

<a id="setup-security-shiro_authentication--security-setup"></a>

## Security Setup

You can setup **Zeppelin notebook authentication** in some simple steps.

<a id="setup-security-shiro_authentication--1.-enable-shiro"></a>

### 1. Enable Shiro

By default in `conf`, you will find `shiro.ini.template`, this file is used as an example and it is strongly recommended
to create a `shiro.ini` file by doing the following command line

```bash
cp conf/shiro.ini.template conf/shiro.ini
```

For the further information about `shiro.ini` file format, please refer to [Shiro Configuration](http://shiro.apache.org/configuration.html#Configuration-INISections).

<a id="setup-security-shiro_authentication--2.-start-zeppelin"></a>

### 2. Start Zeppelin

```bash
bin/zeppelin-daemon.sh start #(or restart)
```

Then you can browse Zeppelin at <http://localhost:8080>.

<a id="setup-security-shiro_authentication--3.-login"></a>

### 3. Login

Finally, you can login using one of the below **username/password** combinations.

![](assets/images/zeppelin-login_197c761b5b68e72c.png)

```
[users]

admin = password1, admin
user1 = password2, role1, role2
user2 = password3, role3
user3 = password4, role2
```

You can set the roles for each users next to the password.

<a id="setup-security-shiro_authentication--groups-and-permissions-optional"></a>

## Groups and permissions (optional)

In case you want to leverage user groups and permissions, use one of the following configuration for LDAP or AD under `[main]` segment in `shiro.ini`.

```
activeDirectoryRealm = org.apache.zeppelin.realm.ActiveDirectoryGroupRealm
activeDirectoryRealm.systemUsername = userNameA
activeDirectoryRealm.systemPassword = passwordA
activeDirectoryRealm.searchBase = CN=Users,DC=SOME_GROUP,DC=COMPANY,DC=COM
activeDirectoryRealm.url = ldap://ldap.test.com:389
activeDirectoryRealm.groupRolesMap = "CN=aGroupName,OU=groups,DC=SOME_GROUP,DC=COMPANY,DC=COM":"group1"
activeDirectoryRealm.authorizationCachingEnabled = false
activeDirectoryRealm.principalSuffix = @corp.company.net

ldapRealm = org.apache.zeppelin.realm.LdapGroupRealm
# search base for ldap groups (only relevant for LdapGroupRealm):ldapRealm.contextFactory.environment[ldap.searchBase] = dc=COMPANY,dc=COM
ldapRealm.contextFactory.url = ldap://ldap.test.com:389
ldapRealm.userDnTemplate = uid={0},ou=Users,dc=COMPANY,dc=COM
ldapRealm.contextFactory.authenticationMechanism = simple
```

also define roles/groups that you want to have in system, like below;

```
[roles]
admin = *
hr = *
finance = *
group1 = *
```

<a id="setup-security-shiro_authentication--configure-realm-optional"></a>

## Configure Realm (optional)

Realms are responsible for authentication and authorization in Apache Zeppelin. By default, Apache Zeppelin uses **IniRealm** (users and groups are configurable in `conf/shiro.ini` file under `[user]` and `[group]` section). You can also leverage Shiro Realms like **JndiLdapRealm**, **JdbcRealm** or create **AuthorizingRealm**.
To learn more about Apache Shiro Realm, please check [this documentation](https://shiro.apache.org/realm.html).

We also provide community custom Realms.

> [!NOTE]
> : When using any of the below realms the default
> password-based (IniRealm) authentication needs to be disabled.

<a id="setup-security-shiro_authentication--active-directory"></a>

### Active Directory

```
activeDirectoryRealm = org.apache.zeppelin.realm.ActiveDirectoryGroupRealm
activeDirectoryRealm.systemUsername = userNameA
activeDirectoryRealm.systemPassword = passwordA
activeDirectoryRealm.hadoopSecurityCredentialPath = jceks://file/user/zeppelin/conf/zeppelin.jceks
activeDirectoryRealm.searchBase = CN=Users,DC=SOME_GROUP,DC=COMPANY,DC=COM
activeDirectoryRealm.url = ldap://ldap.test.com:389
activeDirectoryRealm.groupRolesMap = "CN=aGroupName,OU=groups,DC=SOME_GROUP,DC=COMPANY,DC=COM":"group1"
activeDirectoryRealm.authorizationCachingEnabled = false
activeDirectoryRealm.principalSuffix = @corp.company.net
```

Also instead of specifying systemPassword in clear text in shiro.ini administrator can choose to specify the same in "hadoop credential".
Create a keystore file using the hadoop credential commandline, for this the hadoop commons should be in the classpath
`hadoop credential create activeDirectoryRealm.systempassword -provider jceks://file/user/zeppelin/conf/zeppelin.jceks`

Change the following values in the Shiro.ini file, and uncomment the line:
`activeDirectoryRealm.hadoopSecurityCredentialPath = jceks://file/user/zeppelin/conf/zeppelin.jceks`

<a id="setup-security-shiro_authentication--ldap"></a>

### LDAP

Two options exist for configuring an LDAP Realm. The simpler to use is the LdapGroupRealm. How ever it has limited
flexibility with mapping of ldap groups to users and for authorization for user groups. A sample configuration file for
this realm is given below.

```
ldapRealm = org.apache.zeppelin.realm.LdapGroupRealm
# search base for ldap groups (only relevant for LdapGroupRealm):ldapRealm.contextFactory.environment[ldap.searchBase] = dc=COMPANY,dc=COM
ldapRealm.contextFactory.url = ldap://ldap.test.com:389
ldapRealm.userDnTemplate = uid={0},ou=Users,dc=COMPANY,dc=COM
ldapRealm.contextFactory.authenticationMechanism = simple
```

The other more flexible option is to use the LdapRealm. It allows for mapping of ldapgroups to roles and also allows for
role/group based authentication into the zeppelin server. Sample configuration for this realm is given below.

```
[main]
ldapRealm=org.apache.zeppelin.realm.LdapRealm

ldapRealm.contextFactory.authenticationMechanism = simple
ldapRealm.contextFactory.url = ldap://localhost:33389
ldapRealm.userDnTemplate = uid={0},ou=people,dc=hadoop,dc=apache,dc=org
# Ability to set ldap paging Size if needed default is 100
ldapRealm.pagingSize = 200
ldapRealm.authorizationEnabled = true
ldapRealm.searchBase = dc=hadoop,dc=apache,dc=org
ldapRealm.userSearchBase = dc=hadoop,dc=apache,dc=org
ldapRealm.groupSearchBase = ou=groups,dc=hadoop,dc=apache,dc=org
ldapRealm.groupObjectClass = groupofnames
# Allow userSearchAttribute to be customized
# If userSearchAttributeName was configured, Zeppelin would use userObjectClass and userSearchAttributeName to search for an actual user DN
# Otherwise, memberAttributeValueTemplate would be used to construct the user DN.
ldapRealm.userSearchAttributeName = sAMAccountName
ldapRealm.memberAttribute = member
# force usernames returned from ldap to lowercase useful for AD
ldapRealm.userLowerCase = true
# ability set searchScopes subtree (default), one, base
ldapRealm.userSearchScope = subtree;
ldapRealm.groupSearchScope = subtree;
ldapRealm.memberAttributeValueTemplate = cn={0},ou=people,dc=hadoop,dc=apache,dc=org
ldapRealm.contextFactory.systemUsername = uid=guest,ou=people,dc=hadoop,dc=apache,dc=org
ldapRealm.contextFactory.systemPassword = S{ALIAS=ldcSystemPassword}
# enable support for nested groups using the LDAP_MATCHING_RULE_IN_CHAIN operator
ldapRealm.groupSearchEnableMatchingRuleInChain = true
# optional mapping from physical groups to logical application roles
ldapRealm.rolesByGroup = LDN_USERS: user_role, NYK_USERS: user_role, HKG_USERS: user_role, GLOBAL_ADMIN: admin_role
# optional list of roles that are allowed to authenticate. Incase not present all groups are allowed to authenticate (login).
# This changes nothing for url specific permissions that will continue to work as specified in [urls].
ldapRealm.allowedRolesForAuthentication = admin_role,user_role
ldapRealm.permissionsByRole = user_role = *:ToDoItemsJdo:*:*, *:ToDoItem:*:*; admin_role = *
securityManager.sessionManager = $sessionManager
securityManager.realms = $ldapRealm
```

Also instead of specifying systemPassword in clear text in `shiro.ini` administrator can choose to specify the same in "hadoop credential".
Create a keystore file using the hadoop credential command line:
`hadoop credential create ldapRealm.systemPassword -provider jceks://file/user/zeppelin/conf/zeppelin.jceks`

> [!WARNING]
> **Caution**
> Add the following line in the `shiro.ini` file:
> `ldapRealm.hadoopSecurityCredentialPath = jceks://file/user/zeppelin/conf/zeppelin.jceks`
> due to a bug in LDAPRealm only `ldapRealm.pagingSize` results will be fetched from LDAP. In big directory Trees this may cause missing Roles. Try limiting the search Scope using `ldapRealm.groupSearchBase` or narrow down the required Groups using `ldapRealm.groupSearchFilter`

<a id="setup-security-shiro_authentication--pam"></a>

### PAM

[PAM](https://en.wikipedia.org/wiki/Pluggable_authentication_module) authentication support allows the reuse of existing authentication
modules on the host where Zeppelin is running. On a typical system modules are configured per service for example sshd, passwd, etc. under `/etc/pam.d/`. You can
either reuse one of these services or create your own for Zeppelin. Activating PAM authentication requires two parameters:
1. realm: The Shiro realm being used
2. service: The service configured under `/etc/pam.d/` to be used. The name here needs to be the same as the file name under `/etc/pam.d/`

```
[main]
 pamRealm=org.apache.zeppelin.realm.PamRealm
 pamRealm.service=sshd
```

<a id="setup-security-shiro_authentication--knox-sso"></a>

### Knox SSO

[KnoxSSO](https://knox.apache.org/books/knox-0-13-0/dev-guide.html#KnoxSSO+Integration) provides an abstraction for integrating any number of authentication systems and SSO solutions and enables participating web applications to scale to those solutions more easily. Without the token exchange capabilities offered by KnoxSSO each component UI would need to integrate with each desired solution on its own.

When Knox SSO is enabled for Zeppelin, the [Apache Hadoop Groups Mapping](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/GroupsMapping.html) configuration will used internally to determine the group memberships of the user who is trying to log in. Role-based access permission can be set based on groups as seen by Hadoop.

To enable this, apply the following change in `conf/shiro.ini` under `[main]` section.

```
### A sample for configuring Knox JWT Realm
knoxJwtRealm = org.apache.zeppelin.realm.jwt.KnoxJwtRealm
## Domain of Knox SSO
knoxJwtRealm.providerUrl = https://domain.example.com/
## Url for login
knoxJwtRealm.login = gateway/knoxsso/knoxauth/login.html
## Url for logout
knoxJwtRealm.logout = gateway/knoxssout/api/v1/webssout
knoxJwtRealm.redirectParam = originalUrl
knoxJwtRealm.cookieName = hadoop-jwt
knoxJwtRealm.publicKeyPath = /etc/zeppelin/conf/knox-sso.pem
# This is required if KNOX SSO is enabled, to check if "knoxJwtRealm.cookieName" cookie was expired/deleted.
authc = org.apache.zeppelin.realm.jwt.KnoxAuthenticationFilter
```

<a id="setup-security-shiro_authentication--http-spnego-authentication"></a>

### HTTP SPNEGO Authentication

HTTP SPNEGO (Simple and Protected GSS-API NEGOtiation) is the standard way to support Kerberos Ticket based user authentication for Web Services. Based on [Apache Hadoop Auth](https://hadoop.apache.org/docs/current/hadoop-auth/index.html), Zeppelin supports ability to authenticate users by accepting and validating their Kerberos Ticket.

When HTTP SPNEGO Authentication is enabled for Zeppelin, the [Apache Hadoop Groups Mapping](https://hadoop.apache.org/docs/r2.8.0/hadoop-project-dist/hadoop-common/GroupsMapping.html) configuration will used internally to determine the group memberships of the user who is trying to log in. Role-based access permission can be set based on groups as seen by Hadoop.

To enable this, apply the following change in `conf/shiro.ini` under `[main]` section.

```
krbRealm = org.apache.zeppelin.realm.kerberos.KerberosRealm
krbRealm.principal=HTTP/zeppelin.fqdn.domain.com@EXAMPLE.COM
krbRealm.keytab=/etc/security/keytabs/spnego.service.keytab
krbRealm.nameRules=DEFAULT
krbRealm.signatureSecretFile=/etc/security/http_secret
krbRealm.tokenValidity=36000
krbRealm.cookieDomain=domain.com
krbRealm.cookiePath=/
authc = org.apache.zeppelin.realm.kerberos.KerberosAuthenticationFilter
```

For above configuration to work, user need to do some more configurations outside Zeppelin.

1. A valid SPNEGO keytab should be available on the Zeppelin node and should be readable by 'zeppelin' user. If there is a SPNEGO keytab already available (because of another Hadoop service), it can be reused here without generating a new keytab.
   An example of working SPNEGO keytab could be:

```
$ klist -kt /etc/security/keytabs/spnego.service.keytab Keytab name: FILE:/etc/security/keytabs/spnego.service.keytab KVNO Timestamp Principal ---- ------------------- ------------------------------------------------------2 11/26/2018 16:58:38 HTTP/zeppelin.fqdn.domain.com@EXAMPLE.COM 2 11/26/2018 16:58:38 HTTP/zeppelin.fqdn.domain.com@EXAMPLE.COM 2 11/26/2018 16:58:38 HTTP/zeppelin.fqdn.domain.com@EXAMPLE.COM 2 11/26/2018 16:58:38 HTTP/zeppelin.fqdn.domain.com@EXAMPLE.COM
```

Ensure that the keytab premissions are sufficiently strict while still readable by the 'zeppelin' user:

```
$ ls -l /etc/security/keytabs/spnego.service.keytab -r--r-----. 1 root hadoop 346 Nov 26 16:58 /etc/security/keytabs/spnego.service.keytab
```

Note that for the above example, the 'zeppelin' user can read the keytab because they are a member of the 'hadoop' group.

1. A secret signature file must be present on Zeppelin node, readable by 'zeppelin' user. This file contains the random binary numbers which is used to sign 'hadoop.auth' cookie, generated during SPNEGO exchange. If such a file is already generated and available on the Zeppelin node, it should be used rather than generating a new file.
   Commands to generate a secret signature file (if required):

```
dd if=/dev/urandom of=/etc/security/http_secret bs=1024 count=1
chown hdfs:hadoop /etc/security/http_secret
chmod 440 /etc/security/http_secret
```

<a id="setup-security-shiro_authentication--secure-cookie-for-zeppelin-sessions-optional"></a>

## Secure Cookie for Zeppelin Sessions (optional)

Zeppelin can be configured to set `HttpOnly` flag in the session cookie. With this configuration, Zeppelin cookies can
not be accessed via client side scripts thus preventing majority of Cross-site scripting (XSS) attacks.

To enable secure cookie support via Shiro, add the following lines in `conf/shiro.ini` under `[main]` section, after
defining a `sessionManager`.

```
cookie = org.apache.shiro.web.servlet.SimpleCookie
cookie.name = JSESSIONID
cookie.secure = true
cookie.httpOnly = true
sessionManager.sessionIdCookie = $cookie
```

<a id="setup-security-shiro_authentication--secure-your-zeppelin-information-optional"></a>

## Secure your Zeppelin information (optional)

By default, anyone who defined in `[users]` can share **Interpreter Setting**, **Credential** and **Configuration** information in Apache Zeppelin.
Sometimes you might want to hide these information for your use case.
Since Shiro provides **url-based security**, you can hide the information by commenting or uncommenting these below lines in `conf/shiro.ini`.

```
[urls]

/api/interpreter/** = authc, roles[admin]
/api/configurations/** = authc, roles[admin]
/api/credential/** = authc, roles[admin]
```

In this case, only who have `admin` role can see **Interpreter Setting**, **Credential** and **Configuration** information.
If you want to grant this permission to other users, you can change **roles[ ]** as you defined at `[users]` section.

<a id="setup-security-shiro_authentication--apply-multiple-roles-in-shiro-configuration"></a>

### Apply multiple roles in Shiro configuration

By default, Shiro will allow access to a URL if only user is part of "**all the roles**" defined like this:

```
[urls]

/api/interpreter/** = authc, roles[admin, role1]
```

<a id="setup-security-shiro_authentication--apply-multiple-roles-or-user-in-shiro-configuration"></a>

### Apply multiple roles or user in Shiro configuration

If there is a need that user with "**any of the defined roles or user itself**" should be allowed, then following Shiro configuration can be used:

```
[main]
anyofrolesuser = org.apache.zeppelin.utils.AnyOfRolesUserAuthorizationFilter

[urls]

/api/interpreter/** = authc, anyofrolesuser[admin, user1]
/api/configurations/** = authc, roles[admin]
/api/credential/** = authc, roles[admin]
```

> **NOTE :** All of the above configurations are defined in the `conf/shiro.ini` file.

<a id="setup-security-shiro_authentication--faq"></a>

## FAQ

Zeppelin sever is configured as form-based authentication but is behind proxy configured as basic-authentication for example [NGINX](#setup-security-authentication_nginx--http-basic-authentication-using-nginx) and don't want Zeppelin-Server to clear authentication headers.

> Set `zeppelin.server.authorization.header.clear` to `false` in zeppelin-site.xml

<a id="setup-security-shiro_authentication--other-authentication-methods"></a>

## Other authentication methods

- [HTTP Basic Authentication using NGINX](#setup-security-authentication_nginx)

---

---

<a id="setup-security-notebook_authorization"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/security/notebook_authorization.html -->

<!-- page_index: 46 -->

<a id="setup-security-notebook_authorization--zeppelin-notebook-authorization"></a>

# Zeppelin Notebook Authorization

<a id="setup-security-notebook_authorization--overview"></a>

## Overview

We assume that there is an **Shiro Authentication** component that associates a user string and a set of group strings with every NotebookSocket.
If you don't set the authentication components yet, please check [Shiro authentication for Apache Zeppelin](#setup-security-shiro_authentication) first.

<a id="setup-security-notebook_authorization--authorization-setting"></a>

## Authorization Setting

You can set Zeppelin notebook permissions in each notebooks. Of course only **notebook owners** can change this configuration.
Just click **Lock icon** and open the permission setting page in your notebook.

As you can see, each Zeppelin notebooks has 3 entities :

- Owners ( users or groups )
- Readers ( users or groups )
- Writers ( users or groups )
- Runners ( users or groups )

![](assets/images/permission-setting_df9a142d64328fb6.png)

Fill out the each forms with comma seperated **users** and **groups** configured in `conf/shiro.ini` file.
If the form is empty (\*), it means that any users can perform that operation.

If someone who doesn't have **read** permission is trying to access the notebook or someone who doesn't have **write** permission is trying to edit the notebook, or someone who doesn't have **run** permission is trying to run a paragraph Zeppelin will ask to login or block the user.

By default, owners and writers have **write** permission, owners, writers and runners have **run** permission, owners, writers, runners and readers have **read** permission

![](assets/images/insufficient-privileges_c3fac2519cf9fd45.png)
<a id="setup-security-notebook_authorization--separate-notebook-workspaces-public-vs.-private"></a>

## Separate notebook workspaces (public vs. private)

By default, the authorization rights allow other users to see the newly created note, meaning the workspace is `public`. This behavior is controllable and can be set through either `ZEPPELIN_NOTEBOOK_PUBLIC` variable in `conf/zeppelin-env.sh`, or through `zeppelin.notebook.public` property in `conf/zeppelin-site.xml`. Thus, in order to make newly created note appear only in your `private` workspace by default, you can set either `ZEPPELIN_NOTEBOOK_PUBLIC` to `false` in your `conf/zeppelin-env.sh` as follows:

```bash
export ZEPPELIN_NOTEBOOK_PUBLIC="false"
```

or set `zeppelin.notebook.public` property to `false` in `conf/zeppelin-site.xml` as follows:

```xml
<property>
  <name>zeppelin.notebook.public</name>
  <value>false</value>
  <description>Make notebook public by default when created, private otherwise</description>
</property>
```

Behind the scenes, when you create a new note only the `owners` field is filled with current user, leaving `readers`, `runners` and `writers` fields empty. All the notes with at least one empty authorization field are considered to be in `public` workspace. Thus when setting `zeppelin.notebook.public` (or corresponding `ZEPPELIN_NOTEBOOK_PUBLIC`) to false, newly created notes have `readers`, `runners`, `writers` fields filled with current user, making note appear as in `private` workspace.

<a id="setup-security-notebook_authorization--how-it-works"></a>

## How it works

In this section, we will explain the detail about how the notebook authorization works in backend side.

<a id="setup-security-notebook_authorization--notebookserver"></a>

### NotebookServer

The [NotebookServer](https://github.com/apache/zeppelin/blob/master/zeppelin-server/src/main/java/org/apache/zeppelin/socket/NotebookServer.java) classifies every notebook operations into three categories: **Read**, **Run**, **Write**, **Manage**.
Before executing a notebook operation, it checks if the user and the groups associated with the `NotebookSocket` have permissions.
For example, before executing a **Read** operation, it checks if the user and the groups have at least one entity that belongs to the **Reader** entities.

<a id="setup-security-notebook_authorization--notebook-rest-api-call"></a>

### Notebook REST API call

Zeppelin executes a [REST API call](https://github.com/apache/zeppelin/blob/master/zeppelin-server/src/main/java/org/apache/zeppelin/rest/NotebookRestApi.java) for the notebook permission information.
In the backend side, Zeppelin gets the user information for the connection and allows the operation if the users and groups
associated with the current user have at least one entity that belongs to owner entities for the notebook.

---

---

<a id="setup-security-datasource_authorization"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/security/datasource_authorization.html -->

<!-- page_index: 47 -->

<a id="setup-security-datasource_authorization--data-source-authorization-in-apache-zeppelin"></a>

# Data Source Authorization in Apache Zeppelin

<a id="setup-security-datasource_authorization--overview"></a>

## Overview

Data source authorization involves authenticating to the data source like a Mysql database and letting it determine user permissions.
Apache Zeppelin allows users to use their own credentials to authenticate with **Data Sources**.

For example, let's assume you have an account in the Vertica databases with credentials.
You might want to use this account to create a JDBC connection instead of a shared account with all users who are defined in `conf/shiro.ini`.
In this case, you can add your credential information to Apache Zeppelin and use them with below simple steps.

<a id="setup-security-datasource_authorization--how-to-save-the-credential-information"></a>

## How to save the credential information?

You can add new credentials in the dropdown menu for your data source which can be passed to interpreters.

![](assets/images/credential-tab_572e6b76f21b1922.png)

**Entity** can be the key that distinguishes each credential sets.(We suggest that the convention of the **Entity** is `Interpreter Name`.)

Type **Username & Password** for your own credentials. ex) Mysql user & password of the JDBC Interpreter.

![](assets/images/add-credential_a69c81481908eb8a.png)

The credentials saved as per users defined in `conf/shiro.ini`.
If you didn't activate [shiro authentication in Apache Zeppelin](#setup-security-shiro_authentication), your credential information will be saved as `anonymous`.
All credential information also can be found in `conf/credentials.json`.

<a id="setup-security-datasource_authorization--jdbc-interpreter"></a>

#### JDBC interpreter

You need to maintain per-user connection pools.
The interpret method takes the user string as a parameter and executes the jdbc call using a connection in the user's connection pool.

<a id="setup-security-datasource_authorization--presto"></a>

#### Presto

You don't need a password if the Presto DB server runs backend code using HDFS authorization for the user.

<a id="setup-security-datasource_authorization--vertica-and-mysql"></a>

#### Vertica and Mysql

You have to store the password information for users.

<a id="setup-security-datasource_authorization--please-note"></a>

## Please note

As a first step of data source authentication feature, [ZEPPELIN-828](https://issues.apache.org/jira/browse/ZEPPELIN-828) was proposed and implemented in Pull Request [#860](https://github.com/apache/zeppelin/pull/860).
Currently, only customized 3rd party interpreters can use this feature. We are planning to apply this mechanism to [the community managed interpreters](#usage-interpreter-installation--available-community-managed-interpreters) in the near future.
Please keep track [ZEPPELIN-1070](https://issues.apache.org/jira/browse/ZEPPELIN-1070).

---

---

<a id="setup-security-http_security_headers"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/security/http_security_headers.html -->

<!-- page_index: 48 -->

<a id="setup-security-http_security_headers--setting-up-http-response-headers-for-zeppelin"></a>

# Setting up HTTP Response Headers for Zeppelin

Apache Zeppelin can be configured to include HTTP Headers which aids in preventing Cross Site Scripting (XSS), Cross-Frame Scripting (XFS) and also enforces HTTP Strict Transport Security. Apache Zeppelin also has configuration available to set the Application Server Version to desired value.

<a id="setup-security-http_security_headers--setting-up-http-strict-transport-security-hsts-response-header"></a>

## Setting up HTTP Strict Transport Security (HSTS) Response Header

Enabling HSTS Response Header prevents Man-in-the-middle attacks by automatically redirecting HTTP requests to HTTPS when Zeppelin Server is running on SSL. Read on how to configure SSL for Zeppelin [here](#setup-operation-configuration). Even if web page contains any resource which gets served over HTTP or any HTTP links, it will automatically be redirected to HTTPS for the target domain.
It also prevents MITM attack by not allowing User to override the invalid certificate message, when Attacker presents invalid SSL certificate to the User.

The following property needs to be updated in the zeppelin-site.xml in order to enable HSTS. You can choose appropriate value for "max-age".

```xml
<property>
  <name>zeppelin.server.strict.transport</name>
  <value>max-age=631138519</value>
  <description>The HTTP Strict-Transport-Security response header is a security feature that lets a web site tell browsers that it should only be communicated with using HTTPS, instead of using HTTP. Enable this when Zeppelin is running on HTTPS. Value is in Seconds, the default value is equivalent to 20 years.</description>
</property>
```

Possible values are:

- max-age=<expire-time>
- max-age=<expire-time>; includeSubDomains
- max-age=<expire-time>; preload

Read more about HSTS [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security).

<a id="setup-security-http_security_headers--setting-up-x-xss-protection-header"></a>

## Setting up X-XSS-PROTECTION Header

The HTTP X-XSS-Protection response header is a feature of Internet Explorer, Chrome and Safari Web browsers that initiates configured action when they detect reflected cross-site scripting (XSS) attacks.

The below property to set X-XSS-Protection header is enabled with default value of "1; mode=block" in the zeppelin-site.xml

```xml
<property>
  <name>zeppelin.server.xxss.protection</name>
  <value>1; mode=block</value>
  <description>The HTTP X-XSS-Protection response header is a feature of Internet Explorer, Chrome and Safari that stops pages from loading when they detect reflected cross-site scripting (XSS) attacks. When value is set to 1 and a cross-site scripting attack is detected, the browser will sanitize the page (remove the unsafe parts).</description>
</property>
```

You can choose appropriate value from below to update the configuration if required.

- 0 (Disables XSS filtering)
- 1 (Enables XSS filtering. If a cross-site scripting attack is detected, the browser will sanitize the page.)
- 1; mode=block (Enables XSS filtering. The browser will prevent rendering of the page if an attack is detected.)

Read more about HTTP X-XSS-Protection response header [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection).

<a id="setup-security-http_security_headers--setting-up-x-frame-options-header"></a>

## Setting up X-Frame-Options Header

The X-Frame-Options HTTP response header can indicate browser to avoid clickjacking attacks, by ensuring that their content is not embedded into other sites in a `<frame>`,`<iframe>` or `<object>`.

The below property to set X-Frame-Options header is enabled with default value of "SAMEORIGIN" in the zeppelin-site.xml

```xml
<property>
  <name>zeppelin.server.xframe.options</name>
  <value>SAMEORIGIN</value>
  <description>The X-Frame-Options HTTP response header can be used to indicate whether or not a browser should be allowed to render a page in a frame/iframe/object.</description>
</property>
```

You can choose appropriate value from below to update the configuration if required.

- `DENY`
- `SAMEORIGIN`
- `ALLOW-FROM uri`

<a id="setup-security-http_security_headers--setting-up-x-content-type-options-header"></a>

## Setting up X-Content-Type-Options Header

The HTTP X-Content-Type-Options response header helps to prevent MIME type sniffing attacks. It directs the browser to honor the type specified in the Content-Type header, rather than trying to determine the type from the content itself. The default value `nosniff` is really the only meaningful value. This header is supported on all browsers except Safari and Safari on iOS.

The below property to set X-Content-Type-Options header is enabled with default value of "nosniff" in the zeppelin-site.xml

```xml
<property>
  <name>zeppelin.server.xcontent.type.options</name>
  <value>nosniff</value>
  <description>The HTTP X-Content-Type-Options response header helps to prevent MIME type sniffing attacks.</description>
</property>
```

<a id="setup-security-http_security_headers--setting-up-server-header"></a>

## Setting up Server Header

Security conscious organisations does not want to reveal the Application Server name and version to prevent finding this information easily by Attacker while fingerprinting the Application. The exact version number can tell an Attacker if the current Application Server is patched for or vulnerable to certain publicly known CVE associated to it.

The below property to mask Jetty server version is enabled by default and configured with value of " " (one whitespace char) in the zeppelin-site.xml

```xml
<property>
    <name>zeppelin.server.jetty.name</name>
    <value> </value>
    <description>Hardcoding Application Server name to Prevent Fingerprinting</description>
</property>
```

The value can be any "String". Removing this property from configuration will cause Zeppelin to send correct Jetty server version.

Also, it can be removed the from response headers and from 300/400/500 HTTP response pages.

```xml
<property>
    <name>zeppelin.server.send.jetty.name</name>
    <value>false</value>
    <description>If set to false, will not show the Jetty version to prevent Fingerprinting</description>
</property>
```

---

---

<a id="setup-operation-configuration"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/operation/configuration.html -->

<!-- page_index: 49 -->

<a id="setup-operation-configuration--apache-zeppelin-configuration"></a>

# Apache Zeppelin Configuration

<a id="setup-operation-configuration--zeppelin-properties"></a>

## Zeppelin Properties

Zeppelin can be configured via several sources.

Sources descending by priority:
- environment variables can be defined `conf/zeppelin-env.sh`(`conf\zeppelin-env.cmd` for Windows).
- system properties
- configuration file can be defined in `conf/zeppelin-site.xml`

> Mouse hover on each property and click  then you can get a link for that.

| zeppelin-env.sh | zeppelin-site.xml | Default value | Description |
| --- | --- | --- | --- |
| <a id="setup-operation-configuration--zeppelin_addr"></a>

 ###### ZEPPELIN\_ADDR | <a id="setup-operation-configuration--zeppelin.server.addr"></a>

 ###### zeppelin.server.addr | 127.0.0.1 | Zeppelin server binding address |
| <a id="setup-operation-configuration--zeppelin_port"></a>

 ###### ZEPPELIN\_PORT | <a id="setup-operation-configuration--zeppelin.server.port"></a>

 ###### zeppelin.server.port | 8080 | Zeppelin server port Note: Please make sure you're not using the same port with [Zeppelin web application development port](https://zeppelin.apache.org/contribution/webapplication.html#dev-mode) (default: 9000). |
| <a id="setup-operation-configuration--zeppelin_ssl_port"></a>

 ###### ZEPPELIN\_SSL\_PORT | <a id="setup-operation-configuration--zeppelin.server.ssl.port"></a>

 ###### zeppelin.server.ssl.port | 8443 | Zeppelin Server ssl port (used when ssl environment/property is set to true) |
| <a id="setup-operation-configuration--zeppelin_server_rpc_portrange"></a>

 ###### ZEPPELIN\_SERVER\_RPC\_PORTRANGE | <a id="setup-operation-configuration--zeppelin.server.rpc.portrange"></a>

 ###### zeppelin.server.rpc.portRange | : | Specifies the port range for the Zeppelin Interpreter Event Server. Format: `<startPort>:<endPort>` If the `<startPort>` is omitted, the range will begin at 1024. If the `<endPort>` is omitted, the range will extend up to 65535. Note: If `zeppelin.server.rpc.port` is set, this property will be ignored. |
| <a id="setup-operation-configuration--zeppelin_interpreter_rpc_portrange"></a>

 ###### ZEPPELIN\_INTERPRETER\_RPC\_PORTRANGE | <a id="setup-operation-configuration--zeppelin.interpreter.rpc.portrange"></a>

 ###### zeppelin.interpreter.rpc.portRange | : | Specifies the port range for the Zeppelin Interpreter. Format: `<startPort>:<endPort>` If the `<startPort>` is omitted, the range will begin at 1024. If the `<endPort>` is omitted, the range will extend up to 65535. |
| <a id="setup-operation-configuration--zeppelin_server_rpc_port"></a>

 ###### ZEPPELIN\_SERVER\_RPC\_PORT | <a id="setup-operation-configuration--zeppelin.server.rpc.port"></a>

 ###### zeppelin.server.rpc.port |  | Port for the Zeppelin Interpreter Event Server. If not set, an available port will be used automatically. |
| <a id="setup-operation-configuration--zeppelin_jmx_enable"></a>

 ###### ZEPPELIN\_JMX\_ENABLE | <a id="setup-operation-configuration--zeppelin.jmx.enable"></a>

 ###### zeppelin.jmx.enable | false | Enable JMX by defining "true" |
| <a id="setup-operation-configuration--zeppelin_jmx_port"></a>

 ###### ZEPPELIN\_JMX\_PORT | <a id="setup-operation-configuration--zeppelin.jmx.port"></a>

 ###### zeppelin.jmx.port | 9996 | Port number which JMX uses |
| <a id="setup-operation-configuration--zeppelin_mem"></a>

 ###### ZEPPELIN\_MEM | N/A | -Xmx1024m -XX:MaxMetaspaceSize=512m | JVM mem options |
| <a id="setup-operation-configuration--zeppelin_intp_mem"></a>

 ###### ZEPPELIN\_INTP\_MEM | N/A | ZEPPELIN\_MEM | JVM mem options for interpreter process |
| <a id="setup-operation-configuration--zeppelin_java_opts"></a>

 ###### ZEPPELIN\_JAVA\_OPTS | N/A |  | JVM options |
| <a id="setup-operation-configuration--zeppelin_allowed_origins"></a>

 ###### ZEPPELIN\_ALLOWED\_ORIGINS | <a id="setup-operation-configuration--zeppelin.server.allowed.origins"></a>

 ###### zeppelin.server.allowed.origins | \* | Enables a way to specify a ',' separated list of allowed origins for REST and websockets. e.g. http://localhost:8080 |
| <a id="setup-operation-configuration--zeppelin_credentials_persist"></a>

 ###### ZEPPELIN\_CREDENTIALS\_PERSIST | <a id="setup-operation-configuration--zeppelin.credentials.persist"></a>

 ###### zeppelin.credentials.persist | true | Persist credentials on a JSON file (credentials.json) |
| <a id="setup-operation-configuration--zeppelin_credentials_encrypt_key"></a>

 ###### ZEPPELIN\_CREDENTIALS\_ENCRYPT\_KEY | <a id="setup-operation-configuration--zeppelin.credentials.encryptkey"></a>

 ###### zeppelin.credentials.encryptKey |  | If provided, encrypt passwords on the credentials.json file (passwords will be stored as plain-text otherwise |
| <a id="setup-operation-configuration--zeppelin_server_context_path"></a>

 ###### ZEPPELIN\_SERVER\_CONTEXT\_PATH | <a id="setup-operation-configuration--zeppelin.server.context.path"></a>

 ###### zeppelin.server.context.path | / | Context path of the web application |
| <a id="setup-operation-configuration--zeppelin_notebook_collaborative_mode_enable"></a>

 ###### ZEPPELIN\_NOTEBOOK\_COLLABORATIVE\_MODE\_ENABLE | <a id="setup-operation-configuration--zeppelin.notebook.collaborative.mode.enable"></a>

 ###### zeppelin.notebook.collaborative.mode.enable | true | Enable basic opportunity for collaborative editing. Does not change the logic of operation if the note is used by one person. |
| <a id="setup-operation-configuration--zeppelin_ssl"></a>

 ###### ZEPPELIN\_SSL | <a id="setup-operation-configuration--zeppelin.ssl"></a>

 ###### zeppelin.ssl | false |  |
| <a id="setup-operation-configuration--zeppelin_ssl_client_auth"></a>

 ###### ZEPPELIN\_SSL\_CLIENT\_AUTH | <a id="setup-operation-configuration--zeppelin.ssl.client.auth"></a>

 ###### zeppelin.ssl.client.auth | false |  |
| <a id="setup-operation-configuration--zeppelin_ssl_keystore_path"></a>

 ###### ZEPPELIN\_SSL\_KEYSTORE\_PATH | <a id="setup-operation-configuration--zeppelin.ssl.keystore.path"></a>

 ###### zeppelin.ssl.keystore.path | keystore |  |
| <a id="setup-operation-configuration--zeppelin_ssl_keystore_type"></a>

 ###### ZEPPELIN\_SSL\_KEYSTORE\_TYPE | <a id="setup-operation-configuration--zeppelin.ssl.keystore.type"></a>

 ###### zeppelin.ssl.keystore.type | JKS |  |
| <a id="setup-operation-configuration--zeppelin_ssl_keystore_password"></a>

 ###### ZEPPELIN\_SSL\_KEYSTORE\_PASSWORD | <a id="setup-operation-configuration--zeppelin.ssl.keystore.password"></a>

 ###### zeppelin.ssl.keystore.password |  |  |
| <a id="setup-operation-configuration--zeppelin_ssl_key_manager_password"></a>

 ###### ZEPPELIN\_SSL\_KEY\_MANAGER\_PASSWORD | <a id="setup-operation-configuration--zeppelin.ssl.key.manager.password"></a>

 ###### zeppelin.ssl.key.manager.password |  |  |
| <a id="setup-operation-configuration--zeppelin_ssl_truststore_path"></a>

 ###### ZEPPELIN\_SSL\_TRUSTSTORE\_PATH | <a id="setup-operation-configuration--zeppelin.ssl.truststore.path"></a>

 ###### zeppelin.ssl.truststore.path |  |  |
| <a id="setup-operation-configuration--zeppelin_ssl_truststore_type"></a>

 ###### ZEPPELIN\_SSL\_TRUSTSTORE\_TYPE | <a id="setup-operation-configuration--zeppelin.ssl.truststore.type"></a>

 ###### zeppelin.ssl.truststore.type |  |  |
| <a id="setup-operation-configuration--zeppelin_ssl_truststore_password"></a>

 ###### ZEPPELIN\_SSL\_TRUSTSTORE\_PASSWORD | <a id="setup-operation-configuration--zeppelin.ssl.truststore.password"></a>

 ###### zeppelin.ssl.truststore.password |  |  |
| <a id="setup-operation-configuration--zeppelin_ssl_pem_key"></a>

 ###### ZEPPELIN\_SSL\_PEM\_KEY | <a id="setup-operation-configuration--zeppelin.ssl.pem.key"></a>

 ###### zeppelin.ssl.pem.key |  | This directive points to the PEM-encoded private key file for the server. |
| <a id="setup-operation-configuration--zeppelin_ssl_pem_key_password"></a>

 ###### ZEPPELIN\_SSL\_PEM\_KEY\_PASSWORD | <a id="setup-operation-configuration--zeppelin.ssl.pem.key.password"></a>

 ###### zeppelin.ssl.pem.key.password |  | Password of the PEM-encoded private key. |
| <a id="setup-operation-configuration--zeppelin_ssl_pem_cert"></a>

 ###### ZEPPELIN\_SSL\_PEM\_CERT | <a id="setup-operation-configuration--zeppelin.ssl.pem.cert"></a>

 ###### zeppelin.ssl.pem.cert |  | This directive points to a file with certificate data in PEM format. |
| <a id="setup-operation-configuration--zeppelin_ssl_pem_ca"></a>

 ###### ZEPPELIN\_SSL\_PEM\_CA | <a id="setup-operation-configuration--zeppelin.ssl.pem.ca"></a>

 ###### zeppelin.ssl.pem.ca |  | This directive sets the all-in-one file where you can assemble the Certificates of Certification Authorities (CA) whose clients you deal with. These are used for Client Authentication. Such a file is simply the concatenation of the various PEM-encoded Certificate files. |
| <a id="setup-operation-configuration--zeppelin_notebook_homescreen"></a>

 ###### ZEPPELIN\_NOTEBOOK\_HOMESCREEN | <a id="setup-operation-configuration--zeppelin.notebook.homescreen"></a>

 ###### zeppelin.notebook.homescreen |  | Display note IDs on the Apache Zeppelin homescreen e.g. 2A94M5J1Z |
| <a id="setup-operation-configuration--zeppelin_notebook_homescreen_hide"></a>

 ###### ZEPPELIN\_NOTEBOOK\_HOMESCREEN\_HIDE | <a id="setup-operation-configuration--zeppelin.notebook.homescreen.hide"></a>

 ###### zeppelin.notebook.homescreen.hide | false | Hide the note ID set by `ZEPPELIN_NOTEBOOK_HOMESCREEN` on the Apache Zeppelin homescreen. For the further information, please read [Customize your Zeppelin homepage](https://zeppelin.apache.org/docs/0.12.0/setup/usage/other_features/customizing_homepage.html). |
| <a id="setup-operation-configuration--zeppelin_war_tempdir"></a>

 ###### ZEPPELIN\_WAR\_TEMPDIR | <a id="setup-operation-configuration--zeppelin.war.tempdir"></a>

 ###### zeppelin.war.tempdir | webapps | Location of the jetty temporary directory |
| <a id="setup-operation-configuration--zeppelin_default_ui"></a>

 ###### ZEPPELIN\_DEFAULT\_UI | <a id="setup-operation-configuration--zeppelin.default.ui"></a>

 ###### zeppelin.default.ui | new | Default UI for Zeppelin. Options: `classic` or `new` |
| <a id="setup-operation-configuration--zeppelin_notebook_dir"></a>

 ###### ZEPPELIN\_NOTEBOOK\_DIR | <a id="setup-operation-configuration--zeppelin.notebook.dir"></a>

 ###### zeppelin.notebook.dir | notebook | The root directory where notebook directories are saved |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_bucket"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_BUCKET | <a id="setup-operation-configuration--zeppelin.notebook.s3.bucket"></a>

 ###### zeppelin.notebook.s3.bucket | zeppelin | S3 Bucket where notebook files will be saved |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_user"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_USER | <a id="setup-operation-configuration--zeppelin.notebook.s3.user"></a>

 ###### zeppelin.notebook.s3.user | user | User name of an S3 bucket e.g. `bucket/user/notebook/2A94M5J1Z/note.json` |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_endpoint"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_ENDPOINT | <a id="setup-operation-configuration--zeppelin.notebook.s3.endpoint"></a>

 ###### zeppelin.notebook.s3.endpoint | s3.amazonaws.com | Endpoint for the bucket |
| N/A | <a id="setup-operation-configuration--zeppelin.notebook.s3.timeout"></a>

 ###### zeppelin.notebook.s3.timeout | 120000 | Bucket endpoint request timeout in msec |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_kms_key_id"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_KMS\_KEY\_ID | <a id="setup-operation-configuration--zeppelin.notebook.s3.kmskeyid"></a>

 ###### zeppelin.notebook.s3.kmsKeyID |  | AWS KMS Key ID to use for encrypting data in S3 (optional) |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_emp"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_EMP | <a id="setup-operation-configuration--zeppelin.notebook.s3.encryptionmaterialsprovider"></a>

 ###### zeppelin.notebook.s3.encryptionMaterialsProvider |  | Class name of a custom S3 encryption materials provider implementation to use for encrypting data in S3 (optional) |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_sse"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_SSE | <a id="setup-operation-configuration--zeppelin.notebook.s3.sse"></a>

 ###### zeppelin.notebook.s3.sse | false | Save notebooks to S3 with server-side encryption enabled |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_canned_acl"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_CANNED\_ACL | <a id="setup-operation-configuration--zeppelin.notebook.s3.cannedacl"></a>

 ###### zeppelin.notebook.s3.cannedAcl |  | Save notebooks to S3 with the given [Canned ACL](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/s3/model/CannedAccessControlList.html) which determines the S3 permissions. |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_path_style_access"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_PATH\_STYLE\_ACCESS | <a id="setup-operation-configuration--zeppelin.notebook.s3.pathstyleaccess"></a>

 ###### zeppelin.notebook.s3.pathStyleAccess | false | Access S3 bucket using path style |
| <a id="setup-operation-configuration--zeppelin_notebook_s3_signeroverride"></a>

 ###### ZEPPELIN\_NOTEBOOK\_S3\_SIGNEROVERRIDE | <a id="setup-operation-configuration--zeppelin.notebook.s3.signeroverride"></a>

 ###### zeppelin.notebook.s3.signerOverride |  | Optional override to control which signature algorithm should be used to sign AWS requests |
| <a id="setup-operation-configuration--zeppelin_notebook_azure_connection_string"></a>

 ###### ZEPPELIN\_NOTEBOOK\_AZURE\_CONNECTION\_STRING | <a id="setup-operation-configuration--zeppelin.notebook.azure.connectionstring"></a>

 ###### zeppelin.notebook.azure.connectionString |  | The Azure storage account connection string e.g. `DefaultEndpointsProtocol=https; AccountName=<accountName>; AccountKey=<accountKey>` |
| <a id="setup-operation-configuration--zeppelin_notebook_azure_share"></a>

 ###### ZEPPELIN\_NOTEBOOK\_AZURE\_SHARE | <a id="setup-operation-configuration--zeppelin.notebook.azure.share"></a>

 ###### zeppelin.notebook.azure.share | zeppelin | Azure Share where the notebook files will be saved |
| <a id="setup-operation-configuration--zeppelin_notebook_azure_user"></a>

 ###### ZEPPELIN\_NOTEBOOK\_AZURE\_USER | <a id="setup-operation-configuration--zeppelin.notebook.azure.user"></a>

 ###### zeppelin.notebook.azure.user | user | Optional user name of an Azure file share e.g. `share/user/notebook/2A94M5J1Z/note.json` |
| <a id="setup-operation-configuration--zeppelin_notebook_storage"></a>

 ###### ZEPPELIN\_NOTEBOOK\_STORAGE | <a id="setup-operation-configuration--zeppelin.notebook.storage"></a>

 ###### zeppelin.notebook.storage | org.apache.zeppelin.notebook.repo.GitNotebookRepo | Comma separated list of notebook storage locations |
| <a id="setup-operation-configuration--zeppelin_notebook_one_way_sync"></a>

 ###### ZEPPELIN\_NOTEBOOK\_ONE\_WAY\_SYNC | <a id="setup-operation-configuration--zeppelin.notebook.one.way.sync"></a>

 ###### zeppelin.notebook.one.way.sync | false | If there are multiple notebook storage locations, should we treat the first one as the only source of truth? |
| <a id="setup-operation-configuration--zeppelin_notebook_public"></a>

 ###### ZEPPELIN\_NOTEBOOK\_PUBLIC | <a id="setup-operation-configuration--zeppelin.notebook.public"></a>

 ###### zeppelin.notebook.public | true | Make notebook public (set only `owners`) by default when created/imported. If set to `false` will add `user` to `readers` and `writers` as well, making it private and invisible to other users unless permissions are granted. |
| <a id="setup-operation-configuration--zeppelin_interpreter_dir"></a>

 ###### ZEPPELIN\_INTERPRETER\_DIR | <a id="setup-operation-configuration--zeppelin.interpreter.dir"></a>

 ###### zeppelin.interpreter.dir | interpreter | Interpreter directory |
| <a id="setup-operation-configuration--zeppelin_interpreter_dep_mvnrepo"></a>

 ###### ZEPPELIN\_INTERPRETER\_DEP\_MVNREPO | <a id="setup-operation-configuration--zeppelin.interpreter.dep.mvnrepo"></a>

 ###### zeppelin.interpreter.dep.mvnRepo | https://repo1.maven.org/maven2/,https://repo2.maven.org/maven2/ | Remote principal repository for interpreter's additional dependency loading |
| <a id="setup-operation-configuration--zeppelin_interpreter_output_limit"></a>

 ###### ZEPPELIN\_INTERPRETER\_OUTPUT\_LIMIT | <a id="setup-operation-configuration--zeppelin.interpreter.output.limit"></a>

 ###### zeppelin.interpreter.output.limit | 102400 | Output message from interpreter exceeding the limit will be truncated |
| <a id="setup-operation-configuration--zeppelin_interpreter_connect_timeout"></a>

 ###### ZEPPELIN\_INTERPRETER\_CONNECT\_TIMEOUT | <a id="setup-operation-configuration--zeppelin.interpreter.connect.timeout"></a>

 ###### zeppelin.interpreter.connect.timeout | 600s | Interpreter process connect timeout. Default time unit is msec |
| <a id="setup-operation-configuration--zeppelin_dep_localrepo"></a>

 ###### ZEPPELIN\_DEP\_LOCALREPO | <a id="setup-operation-configuration--zeppelin.dep.localrepo"></a>

 ###### zeppelin.dep.localrepo | local-repo | Local repository for dependency loader. ex)visualiztion modules of npm. |
| <a id="setup-operation-configuration--zeppelin_helium_node_installer_url"></a>

 ###### ZEPPELIN\_HELIUM\_NODE\_INSTALLER\_URL | <a id="setup-operation-configuration--zeppelin.helium.node.installer.url"></a>

 ###### zeppelin.helium.node.installer.url | https://nodejs.org/dist/ | Remote Node installer url for Helium dependency loader |
| <a id="setup-operation-configuration--zeppelin_helium_npm_installer_url"></a>

 ###### ZEPPELIN\_HELIUM\_NPM\_INSTALLER\_URL | <a id="setup-operation-configuration--zeppelin.helium.npm.installer.url"></a>

 ###### zeppelin.helium.npm.installer.url | http://registry.npmjs.org/ | Remote Npm installer url for Helium dependency loader |
| <a id="setup-operation-configuration--zeppelin_helium_yarnpkg_installer_url"></a>

 ###### ZEPPELIN\_HELIUM\_YARNPKG\_INSTALLER\_URL | <a id="setup-operation-configuration--zeppelin.helium.yarnpkg.installer.url"></a>

 ###### zeppelin.helium.yarnpkg.installer.url | https://github.com/yarnpkg/yarn/releases/download/ | Remote Yarn package installer url for Helium dependency loader |
| <a id="setup-operation-configuration--zeppelin_websocket_max_text_message_size"></a>

 ###### ZEPPELIN\_WEBSOCKET\_MAX\_TEXT\_MESSAGE\_SIZE | <a id="setup-operation-configuration--zeppelin.websocket.max.text.message.size"></a>

 ###### zeppelin.websocket.max.text.message.size | 1024000 | Size(in characters) of the maximum text message that can be received by websocket. |
| <a id="setup-operation-configuration--zeppelin_server_default_dir_allowed"></a>

 ###### ZEPPELIN\_SERVER\_DEFAULT\_DIR\_ALLOWED | <a id="setup-operation-configuration--zeppelin.server.default.dir.allowed"></a>

 ###### zeppelin.server.default.dir.allowed | false | Enable directory listings on server. |
| <a id="setup-operation-configuration--zeppelin_notebook_git_remote_url"></a>

 ###### ZEPPELIN\_NOTEBOOK\_GIT\_REMOTE\_URL | <a id="setup-operation-configuration--zeppelin.notebook.git.remote.url"></a>

 ###### zeppelin.notebook.git.remote.url |  | GitHub's repository URL. It could be either the HTTP URL or the SSH URL. For example git@github.com:apache/zeppelin.git |
| <a id="setup-operation-configuration--zeppelin_notebook_git_remote_username"></a>

 ###### ZEPPELIN\_NOTEBOOK\_GIT\_REMOTE\_USERNAME | <a id="setup-operation-configuration--zeppelin.notebook.git.remote.username"></a>

 ###### zeppelin.notebook.git.remote.username | token | GitHub username. By default it is `token` to use GitHub's API |
| <a id="setup-operation-configuration--zeppelin_notebook_git_remote_access_token"></a>

 ###### ZEPPELIN\_NOTEBOOK\_GIT\_REMOTE\_ACCESS\_TOKEN | <a id="setup-operation-configuration--zeppelin.notebook.git.remote.access-token"></a>

 ###### zeppelin.notebook.git.remote.access-token | token | GitHub access token to use GitHub's API. If username/password combination is used and not GitHub API, then this value is the password |
| <a id="setup-operation-configuration--zeppelin_notebook_git_remote_origin"></a>

 ###### ZEPPELIN\_NOTEBOOK\_GIT\_REMOTE\_ORIGIN | <a id="setup-operation-configuration--zeppelin.notebook.git.remote.origin"></a>

 ###### zeppelin.notebook.git.remote.origin | token | GitHub remote name. Default is `origin` |
| <a id="setup-operation-configuration--zeppelin_run_mode"></a>

 ###### ZEPPELIN\_RUN\_MODE | <a id="setup-operation-configuration--zeppelin.run.mode"></a>

 ###### zeppelin.run.mode | auto | Run mode. 'auto\|local\|k8s'. 'auto' autodetect environment. 'local' runs interpreter as a local process. k8s runs interpreter on Kubernetes cluster |
| <a id="setup-operation-configuration--zeppelin_k8s_portforward"></a>

 ###### ZEPPELIN\_K8S\_PORTFORWARD | <a id="setup-operation-configuration--zeppelin.k8s.portforward"></a>

 ###### zeppelin.k8s.portforward | false | Port forward to interpreter rpc port. Set 'true' only on local development when zeppelin.k8s.mode 'on'. Don't use 'true' on production environment |
| <a id="setup-operation-configuration--zeppelin_k8s_container_image"></a>

 ###### ZEPPELIN\_K8S\_CONTAINER\_IMAGE | <a id="setup-operation-configuration--zeppelin.k8s.container.image"></a>

 ###### zeppelin.k8s.container.image | apache/zeppelin:0.12.0 | Docker image for interpreters |
| <a id="setup-operation-configuration--zeppelin_k8s_spark_container_image"></a>

 ###### ZEPPELIN\_K8S\_SPARK\_CONTAINER\_IMAGE | <a id="setup-operation-configuration--zeppelin.k8s.spark.container.image"></a>

 ###### zeppelin.k8s.spark.container.image | apache/spark:latest | Docker image for Spark executors |
| <a id="setup-operation-configuration--zeppelin_k8s_template_dir"></a>

 ###### ZEPPELIN\_K8S\_TEMPLATE\_DIR | <a id="setup-operation-configuration--zeppelin.k8s.template.dir"></a>

 ###### zeppelin.k8s.template.dir | k8s | Kubernetes yaml spec files |
| <a id="setup-operation-configuration--zeppelin_k8s_service_name"></a>

 ###### ZEPPELIN\_K8S\_SERVICE\_NAME | <a id="setup-operation-configuration--zeppelin.k8s.service.name"></a>

 ###### zeppelin.k8s.service.name | zeppelin-server | Name of the Zeppelin server service resources |
| <a id="setup-operation-configuration--zeppelin_k8s_timeout_during_pending"></a>

 ###### ZEPPELIN\_K8S\_TIMEOUT\_DURING\_PENDING | <a id="setup-operation-configuration--zeppelin.k8s.timeout.during.pending"></a>

 ###### zeppelin.k8s.timeout.during.pending | true | Value to enable/disable timeout handling when starting Interpreter Pods. Caution: This can lead to an infinity loop |
| <a id="setup-operation-configuration--zeppelin_metric_enable_prometheus"></a>

 ###### ZEPPELIN\_METRIC\_ENABLE\_PROMETHEUS | <a id="setup-operation-configuration--zeppelin.metric.enable.prometheus"></a>

 ###### zeppelin.metric.enable.prometheus | false | Value to enable/disable Prometheus metric endpoint on /metric |
| <a id="setup-operation-configuration--zeppelin_notebook_cron_enable"></a>

 ###### ZEPPELIN\_NOTEBOOK\_CRON\_ENABLE | <a id="setup-operation-configuration--zeppelin.notebook.cron.enable"></a>

 ###### zeppelin.notebook.cron.enable | false | Value to enable/disable Cron support in Notes |
| <a id="setup-operation-configuration--zeppelin_notebook_cron_folders"></a>

 ###### ZEPPELIN\_NOTEBOOK\_CRON\_FOLDERS | <a id="setup-operation-configuration--zeppelin.notebook.cron.folders"></a>

 ###### zeppelin.notebook.cron.folders |  | comma-separated list of folder, where cron is allowed |
| <a id="setup-operation-configuration--zeppelin_note_cache_threshold"></a>

 ###### ZEPPELIN\_NOTE\_CACHE\_THRESHOLD | <a id="setup-operation-configuration--zeppelin.note.cache.threshold"></a>

 ###### zeppelin.note.cache.threshold | 50 | Threshold for the number of notes in the cache before an eviction occurs. |
| <a id="setup-operation-configuration--zeppelin_notebook_versioned_mode_enable"></a>

 ###### ZEPPELIN\_NOTEBOOK\_VERSIONED\_MODE\_ENABLE | <a id="setup-operation-configuration--zeppelin.notebook.versioned.mode.enable"></a>

 ###### zeppelin.notebook.versioned.mode.enable | true | Value to enable/disable version control support in Notes. |

<a id="setup-operation-configuration--ssl-configuration"></a>

## SSL Configuration

Enabling SSL requires a few configuration changes. First, you need to create certificates and then update necessary configurations to enable server side SSL and/or client side certificate authentication.

<a id="setup-operation-configuration--creating-and-configuring-the-certificates"></a>

### Creating and configuring the Certificates

Information how about to generate certificates and a keystore can be found [here](https://wiki.eclipse.org/Jetty/Howto/Configure_SSL).

A condensed example can be found in the top answer to this [StackOverflow post](http://stackoverflow.com/questions/4008837/configure-ssl-on-jetty).

The keystore holds the private key and certificate on the server end. The trustore holds the trusted client certificates. Be sure that the path and password for these two stores are correctly configured in the password fields below. They can be obfuscated using the Jetty password tool. After Maven pulls in all the dependency to build Zeppelin, one of the Jetty jars contain the Password tool. Invoke this command from the Zeppelin home build directory with the appropriate version, user, and password.

```bash
java -cp ./zeppelin-server/target/lib/jetty-all-server-<version>.jar \
org.eclipse.jetty.util.security.Password <user> <password>
```

If you are using a self-signed, a certificate signed by an untrusted CA, or if client authentication is enabled, then the client must have a browser create exceptions for both the normal HTTPS port and WebSocket port. This can by done by trying to establish an HTTPS connection to both ports in a browser (e.g. if the ports are 443 and 8443, then visit https://127.0.0.1:443 and https://127.0.0.1:8443). This step can be skipped if the server certificate is signed by a trusted CA and client auth is disabled.

<a id="setup-operation-configuration--configuring-server-side-ssl"></a>

### Configuring server side SSL

The following properties needs to be updated in the `zeppelin-site.xml` in order to enable server side SSL.

```xml
<property>
  <name>zeppelin.server.ssl.port</name>
  <value>8443</value>
  <description>Server ssl port. (used when ssl property is set to true)</description>
</property>

<property>
  <name>zeppelin.ssl</name>
  <value>true</value>
  <description>Should SSL be used by the servers?</description>
</property>

<property>
  <name>zeppelin.ssl.keystore.path</name>
  <value>keystore</value>
  <description>Path to keystore relative to Zeppelin configuration directory</description>
</property>

<property>
  <name>zeppelin.ssl.keystore.type</name>
  <value>JKS</value>
  <description>The format of the given keystore (e.g. JKS or PKCS12)</description>
</property>

<property>
  <name>zeppelin.ssl.keystore.password</name>
  <value>change me</value>
  <description>Keystore password. Can be obfuscated by the Jetty Password tool</description>
</property>

<property>
  <name>zeppelin.ssl.key.manager.password</name>
  <value>change me</value>
  <description>Key Manager password. Defaults to keystore password. Can be obfuscated.</description>
</property>
```

<a id="setup-operation-configuration--enabling-client-side-certificate-authentication"></a>

### Enabling client side certificate authentication

The following properties needs to be updated in the `zeppelin-site.xml` in order to enable client side certificate authentication.

```xml
<property>
  <name>zeppelin.server.ssl.port</name>
  <value>8443</value>
  <description>Server ssl port. (used when ssl property is set to true)</description>
</property>

<property>
  <name>zeppelin.ssl.client.auth</name>
  <value>true</value>
  <description>Should client authentication be used for SSL connections?</description>
</property>

<property>
  <name>zeppelin.ssl.truststore.path</name>
  <value>truststore</value>
  <description>Path to truststore relative to Zeppelin configuration directory. Defaults to the keystore path</description>
</property>

<property>
  <name>zeppelin.ssl.truststore.type</name>
  <value>JKS</value>
  <description>The format of the given truststore (e.g. JKS or PKCS12). Defaults to the same type as the keystore type</description>
</property>

<property>
  <name>zeppelin.ssl.truststore.password</name>
  <value>change me</value>
  <description>Truststore password. Can be obfuscated by the Jetty Password tool. Defaults to the keystore password</description>
</property>
```

<a id="setup-operation-configuration--storing-user-credentials"></a>

### Storing user credentials

In order to avoid having to re-enter credentials every time you restart/redeploy Zeppelin, you can store the user credentials. Zeppelin supports this via the ZEPPELIN*CREDENTIALS*PERSIST configuration.

Please notice that passwords will be stored in *plain text* by default. To encrypt the passwords, use the ZEPPELIN*CREDENTIALS*ENCRYPT\_KEY config variable. This will encrypt passwords using the AES-128 algorithm.

You can generate an appropriate encryption key any way you'd like - for instance, by using the openssl tool:

```bash
openssl enc -aes-128-cbc -k secret -P -md sha1
```

*Important*: storing your encryption key in a configuration file is *not advised*. Depending on your environment security needs, you may want to consider utilizing a credentials server, storing the ZEPPELIN*CREDENTIALS*ENCRYPT\_KEY as an OS env variable, or any other approach that would not colocate the encryption key and the encrypted content (the credentials.json file).

<a id="setup-operation-configuration--obfuscating-passwords-using-the-jetty-password-tool"></a>

### Obfuscating Passwords using the Jetty Password Tool

Security best practices advise to not use plain text passwords and Jetty provides a password tool to help obfuscating the passwords used to access the KeyStore and TrustStore.

The Password tool documentation can be found [here](http://www.eclipse.org/jetty/documentation/current/configuring-security-secure-passwords.html).

After using the tool:

```bash
java -cp $ZEPPELIN_HOME/zeppelin-server/target/lib/jetty-util-9.2.15.v20160210.jar \
         org.eclipse.jetty.util.security.Password  \
         password

2016-12-15 10:46:47.931:INFO::main: Logging initialized @101ms
password
OBF:1v2j1uum1xtv1zej1zer1xtn1uvk1v1v
MD5:5f4dcc3b5aa765d61d8327deb882cf99
```

update your configuration with the obfuscated password :

```xml
<property>
  <name>zeppelin.ssl.keystore.password</name>
  <value>OBF:1v2j1uum1xtv1zej1zer1xtn1uvk1v1v</value>
  <description>Keystore password. Can be obfuscated by the Jetty Password tool</description>
</property>
```

<a id="setup-operation-configuration--create-github-access-token"></a>

### Create GitHub Access Token

When using GitHub to track notebooks, one can use GitHub's API for authentication. To create an access token, please use the following link https://github.com/settings/tokens.
The value of the access token generated is set in the `zeppelin.notebook.git.remote.access-token` property.

**Note:** After updating these configurations, Zeppelin server needs to be restarted.

---

---

<a id="setup-operation-monitoring"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/operation/monitoring.html -->

<!-- page_index: 50 -->

<a id="setup-operation-monitoring--apache-zeppelin-monitoring"></a>

# Apache Zeppelin Monitoring

<a id="setup-operation-monitoring--monitoring-options"></a>

## Monitoring Options

Apache Zeppelin is using [Micrometer](https://micrometer.io/) - a vendor-neutral application metrics facade.

<a id="setup-operation-monitoring--prometheus-monitoring"></a>

### Prometheus Monitoring

[Prometheus](https://prometheus.io/) is the leading monitoring solution for [Kubernetes](https://kubernetes.io/). The Prometheus endpoint can be activated with the configuration property `zeppelin.metric.enable.prometheus`. The metrics are accessible via the unauthenticated endpoint `/metrics`.
For [Grafana](https://grafana.com/) a good starting point for a dashboard can be found in our [Github Repository](https://github.com/apache/zeppelin/blob/grafana/examples/dashboard.json).

<a id="setup-operation-monitoring--jmx-monitoring"></a>

### JMX Monitoring

[JMX](https://en.wikipedia.org/wiki/Java_Management_Extensions) is a general solution for monitoring Java applications. JMX can be activated with the configuration property `zeppelin.jmx.enable`. The default port 9996 can be changed with the configuration property `zeppelin.jmx.port`.

<a id="setup-operation-monitoring--healthcheck-probe"></a>

## Healthcheck Probe

Apache Zeppelin has two healthcheck related unauthenticated endpoints (`/health/readiness`, `/health/liveness`) that could be used for proxy and/or cloud setups.

---

---

<a id="setup-operation-proxy_setting"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/operation/proxy_setting.html -->

<!-- page_index: 51 -->

<a id="setup-operation-proxy_setting--proxy-setting"></a>

# Proxy Setting

<a id="setup-operation-proxy_setting--how-to-configure-proxies"></a>

## How to Configure Proxies?

Set `http_proxy` and `https_proxy` env variables. (See [more](https://wiki.archlinux.org/index.php/proxy_settings))

Currently, Proxy is supported only for these features.

- Helium: downloading `helium.json`, installing `npm`, `node`, `yarn`

---

---

<a id="setup-operation-upgrading"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/operation/upgrading.html -->

<!-- page_index: 52 -->

<a id="setup-operation-upgrading--manual-upgrade-procedure-for-zeppelin"></a>

# Manual upgrade procedure for Zeppelin

Basically, newer version of Zeppelin works with previous version notebook directory and configurations.
So, copying `notebook` and `conf` directory should be enough.

<a id="setup-operation-upgrading--instructions"></a>

## Instructions

1. Stop Zeppelin: `bin/zeppelin-daemon.sh stop`
2. Copy your `notebook` and `conf` directory into a backup directory
3. Download newer version of Zeppelin and Install. See [Install Guide](#quickstart-install--install).
4. Copy backup `notebook` and `conf` directory into newer version of Zeppelin `notebook` and `conf` directory
5. Start Zeppelin: `bin/zeppelin-daemon.sh start`

<a id="setup-operation-upgrading--migration-guide"></a>

## Migration Guide

<a id="setup-operation-upgrading--upgrading-from-zeppelin-0.9-0.10-to-0.11"></a>

### Upgrading from Zeppelin 0.9, 0.10 to 0.11

- From 0.11, The type of `Pegdown` for parsing markdown was deprecated ([ZEPPELIN-5529](https://issues.apache.org/jira/browse/ZEPPELIN-2619)). It will use `Flexmark` instead.

<a id="setup-operation-upgrading--upgrading-from-zeppelin-0.8-to-0.9"></a>

### Upgrading from Zeppelin 0.8 to 0.9

- From 0.9, we changed the notes file name structure ([ZEPPELIN-2619](https://issues.apache.org/jira/browse/ZEPPELIN-2619)). So when you upgrading zeppelin to 0.9, you need to upgrade note files. Here's steps you need to follow:
  1. Backup your notes file, in case the upgrade fails
  2. Call `bin/upgrade-note.sh -d` to upgrade notes, `-d` option means to delete the old note file, missing this option will keep the old file.
- From 0.9, the Zeppelin server binds to `127.0.0.1` by default, instead of `0.0.0.0`. Configure `zeppelin.server.addr` property or `ZEPPELIN_ADDR` env variable to change it to `0.0.0.0` if you want to access it remotely.
- From 0.9, we have removed `zeppelin.anonymous.allowed` ([ZEPPELIN-4489](https://issues.apache.org/jira/browse/ZEPPELIN-4489)). So, when you upgrade Zeppelin to 0.9 and if `shiro.ini` file does not exist in conf path then all the Zeppelin-Users runs as anonymous.
- From 0.9, we use `{crendential_entry.user}` and `{crendential_entry.password}` for credential injection, while before 0.9 we use `{user.crendential_entry}` and `{password.crendential_entry}`

<a id="setup-operation-upgrading--upgrading-from-zeppelin-0.8.1-and-before-to-0.8.2-and-later"></a>

### Upgrading from Zeppelin 0.8.1 (and before) to 0.8.2 (and later)

- From 0.8.2, the Zeppelin server binds to `127.0.0.1` by default, instead of `0.0.0.0`. Configure the `zeppelin.server.addr` property or `ZEPPELIN_ADDR` env variable to change this.

<a id="setup-operation-upgrading--upgrading-from-zeppelin-0.7-to-0.8"></a>

### Upgrading from Zeppelin 0.7 to 0.8

- From 0.8, we recommend using `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` instead of `zeppelin.pyspark.python` as `zeppelin.pyspark.python` only affects driver. You can use `PYSPARK_PYTHON` and `PYSPARK_DRIVER_PYTHON` as using them in spark.
- From 0.8, depending on your device, the keyboard shortcut `Ctrl-L` or `Command-L` which goes to the line somewhere user wants is not supported.

<a id="setup-operation-upgrading--upgrading-from-zeppelin-0.6-to-0.7"></a>

### Upgrading from Zeppelin 0.6 to 0.7

- From 0.7, we don't use `ZEPPELIN_JAVA_OPTS` as default value of `ZEPPELIN_INTP_JAVA_OPTS` and also the same for `ZEPPELIN_MEM`/`ZEPPELIN_INTP_MEM`. If user want to configure the jvm opts of interpreter process, please set `ZEPPELIN_INTP_JAVA_OPTS` and `ZEPPELIN_INTP_MEM` explicitly. If you don't set `ZEPPELIN_INTP_MEM`, Zeppelin will set it to `-Xms1024m -Xmx1024m -XX:MaxMetaspaceSize=512m` by default.
- Mapping from `%jdbc(prefix)` to `%prefix` is no longer available. Instead, you can use %[interpreter alias] with multiple interpreter setttings on GUI.
- Usage of `ZEPPELIN_PORT` is not supported in ssl mode. Instead use `ZEPPELIN_SSL_PORT` to configure the ssl port. Value from `ZEPPELIN_PORT` is used only when `ZEPPELIN_SSL` is set to `false`.
- The support on Spark 1.1.x to 1.3.x is deprecated.
- From 0.7, we uses `pegdown` as the `markdown.parser.type` option for the `%md` interpreter. Rendered markdown might be different from what you expected
- From 0.7 note.json format has been changed to support multiple outputs in a paragraph. Zeppelin will automatically convert old format to new format. 0.6 or lower version can read new note.json format but output will not be displayed. For the detail, see [ZEPPELIN-212](http://issues.apache.org/jira/browse/ZEPPELIN-212) and [pull request](https://github.com/apache/zeppelin/pull/1658).
- From 0.7 note storage layer will utilize `GitNotebookRepo` by default instead of `VFSNotebookRepo` storage layer, which is an extension of latter one with versioning capabilities on top of it.

---

---

<a id="interpreter-spark"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/spark.html -->

<!-- page_index: 53 -->

<a id="interpreter-spark--spark-interpreter-for-apache-zeppelin"></a>

# Spark Interpreter for Apache Zeppelin

<a id="interpreter-spark--overview"></a>

## Overview

[Apache Spark](http://spark.apache.org) is a fast and general-purpose cluster computing system.
It provides high-level APIs in Java, Scala, Python and R, and an optimized engine that supports general execution graphs.
Apache Spark is supported in Zeppelin with Spark interpreter group which consists of following interpreters.

| Name | Class | Description |
| --- | --- | --- |
| %spark | SparkInterpreter | Creates a SparkContext/SparkSession and provides a Scala environment |
| %spark.pyspark | PySparkInterpreter | Provides a Python environment |
| %spark.ipyspark | IPySparkInterpreter | Provides a IPython environment |
| %spark.r | SparkRInterpreter | Provides an vanilla R environment with SparkR support |
| %spark.ir | SparkIRInterpreter | Provides an R environment with SparkR support based on Jupyter IRKernel |
| %spark.shiny | SparkShinyInterpreter | Used to create R shiny app with SparkR support |
| %spark.sql | SparkSQLInterpreter | Provides a SQL environment |

<a id="interpreter-spark--main-features"></a>

## Main Features

| Feature | Description |
| --- | --- |
| Support multiple versions of Spark | You can run different versions of Spark in one Zeppelin instance |
| Support multiple versions of Scala | You can run different Scala versions (2.12/2.13) of Spark in on Zeppelin instance |
| Support multiple languages | Scala, SQL, Python, R are supported, besides that you can also collaborate across languages, e.g. you can write Scala UDF and use it in PySpark |
| Support multiple execution modes | Local \| Standalone \| Yarn \| K8s |
| Interactive development | Interactive development user experience increase your productivity |
| Inline Visualization | You can visualize Spark Dataset/DataFrame vis Python/R's plotting libraries, and even you can make SparkR Shiny app in Zeppelin |

<a id="interpreter-spark--play-spark-in-zeppelin-docker"></a>

## Play Spark in Zeppelin docker

For beginner, we would suggest you to play Spark in Zeppelin docker.
In the Zeppelin docker image, we have already installed
miniconda and lots of [useful python and R libraries](https://github.com/apache/zeppelin/blob/branch-0.10/scripts/docker/zeppelin/bin/env_python_3_with_R.yml)
including IPython and IRkernel prerequisites, so `%spark.pyspark` would use IPython and `%spark.ir` is enabled.
Without any extra configuration, you can run most of tutorial notes under folder `Spark Tutorial` directly.

First you need to download Spark, because there's no Spark binary distribution shipped with Zeppelin.
e.g. Here we download Spark 3.1.2 to`/mnt/disk1/spark-3.1.2`, and we mount it to Zeppelin docker container and run the following command to start Zeppelin docker container.

```bash
docker run -u $(id -u) -p 8080:8080 -p 4040:4040 --rm -v /mnt/disk1/spark-3.1.2:/opt/spark -e SPARK_HOME=/opt/spark  --name zeppelin apache/zeppelin:0.10.0
```

After running the above command, you can open `http://localhost:8080` to play Spark in Zeppelin. We only verify the spark local mode in Zeppelin docker, other modes may not work due to network issues.
`-p 4040:4040` is to expose Spark web ui, so that you can access Spark web ui via `http://localhost:8081`.

<a id="interpreter-spark--configuration"></a>

## Configuration

The Spark interpreter can be configured with properties provided by Zeppelin.
You can also set other Spark properties which are not listed in the table. For a list of additional properties, refer to [Spark Available Properties](http://spark.apache.org/docs/latest/configuration.html#available-properties).

| Property | Default | Description |
| --- | --- | --- |
| `SPARK_HOME` |  | Location of spark distribution |
| spark.master | local[\*] | Spark master uri. e.g. spark://master*host:7077* |
| spark.submit.deployMode |  | The deploy mode of Spark driver program, either "client" or "cluster", Which means to launch driver program locally ("client") or remotely ("cluster") on one of the nodes inside the cluster. |
| spark.app.name | Zeppelin | The name of spark application. |
| spark.driver.cores | 1 | Number of cores to use for the driver process, only in cluster mode. |
| spark.driver.memory | 1g | Amount of memory to use for the driver process, i.e. where SparkContext is initialized, in the same format as JVM memory strings with a size unit suffix ("k", "m", "g" or "t") (e.g. 512m, 2g). |
| spark.executor.cores | 1 | The number of cores to use on each executor |
| spark.executor.memory | 1g | Executor memory per worker instance. e.g. 512m, 32g |
| spark.executor.instances | 2 | The number of executors for static allocation |
| spark.files |  | Comma-separated list of files to be placed in the working directory of each executor. Globs are allowed. |
| spark.jars |  | Comma-separated list of jars to include on the driver and executor classpaths. Globs are allowed. |
| spark.jars.packages |  | Comma-separated list of Maven coordinates of jars to include on the driver and executor classpaths. The coordinates should be groupId:artifactId:version. If spark.jars.ivySettings is given artifacts will be resolved according to the configuration in the file, otherwise artifacts will be searched for in the local maven repo, then maven central and finally any additional remote repositories given by the command-line option --repositories. |
| `PYSPARKPYTHON`</td> <td>python</td> <td>Python binary executable to use for PySpark in both driver and executors (default is <code>python</code>). Property <code>spark.pyspark.python</code> take precedence if it is set</td> </tr> <tr> <td>`PYSPARK*DRIVER*PYTHON`</td> <td>python</td> <td>Python binary executable to use for PySpark in driver only (default is`PYSPARK*PYTHON`). Property <code>spark.pyspark.driver.python</code> take precedence if it is set</td> </tr> <tr> <td>zeppelin.pyspark.useIPython</td> <td>false</td> <td>Whether use IPython when the ipython prerequisites are met in`%spark.pyspark`* |  |  |
| zeppelin.R.cmd | R | R binary executable path. |
| zeppelin.spark.concurrentSQL | false | Execute multiple SQL concurrently if set true. |
| zeppelin.spark.concurrentSQL.max | 10 | Max number of SQL concurrently executed |
| zeppelin.spark.maxResult | 1000 | Max number rows of Spark SQL result to display. |
| zeppelin.spark.run.asLoginUser | true | Whether run spark job as the zeppelin login user, it is only applied when running spark job in hadoop yarn cluster and shiro is enabled. |
| zeppelin.spark.printREPLOutput | true | Print scala REPL output |
| zeppelin.spark.useHiveContext | true | Use HiveContext instead of SQLContext if it is true. Enable hive for SparkSession |
| zeppelin.spark.enableSupportedVersionCheck | true | Do not change - developer only setting, not for production use |
| zeppelin.spark.sql.interpolation | false | Enable ZeppelinContext variable interpolation into spark sql |
| zeppelin.spark.uiWebUrl |  | Overrides Spark UI default URL. Value should be a full URL (ex: http://{hostName}/{uniquePath}. In Kubernetes mode, value can be Jinja template string with 3 template variables PORT, SERVICENAME and SERVICE*DOMAIN . (e.g.: http://{{PORT}}-{{SERVICE*NAME}}.{{SERVICE*DOMAIN}} ). In yarn mode, value could be a knox url with {{applicationId}} as placeholder, (e.g.: https://knox-server:8443/gateway/yarnui/yarn/proxy/{{applicationId}}/)* |
| spark.webui.yarn.useProxy | false | whether use yarn proxy url as Spark weburl, e.g. http://localhost:8088/proxy/application1583396598068\_0004 |

Without any configuration, Spark interpreter works out of box in local mode. But if you want to connect to your Spark cluster, you'll need to follow below two simple steps.

- Set SPARK\_HOME
- Set master

<a id="interpreter-spark--set-spark_home"></a>

### Set SPARK\_HOME

There are several options for setting `SPARK_HOME`.

- Set `SPARK_HOME` in `zeppelin-env.sh`
- Set `SPARK_HOME` in interpreter setting page
- Set `SPARK_HOME` via [inline generic configuration](#usage-interpreter-overview--inline-generic-confinterpreter)

<a id="interpreter-spark--set-spark_home-in-zeppelin-env.sh"></a>

#### Set `SPARK_HOME` in `zeppelin-env.sh`

If you work with only one version of Spark, then you can set `SPARK_HOME` in `zeppelin-env.sh` because any setting in `zeppelin-env.sh` is globally applied.

e.g.

```bash
export SPARK_HOME=/usr/lib/spark
```

You can optionally set more environment variables in `zeppelin-env.sh`

```bash
# set hadoop conf dir export HADOOP_CONF_DIR=/usr/lib/hadoop
```

<a id="interpreter-spark--set-spark_home-in-interpreter-setting-page"></a>

#### Set `SPARK_HOME` in interpreter setting page

If you want to use multiple versions of Spark, then you need to create multiple Spark interpreters and set `SPARK_HOME` separately. e.g.
Create a new Spark interpreter `spark33` for Spark 3.3 and set its `SPARK_HOME` in interpreter setting page, Create a new Spark interpreter `spark34` for Spark 3.4 and set its `SPARK_HOME` in interpreter setting page.

<a id="interpreter-spark--set-spark_home-via-inline-generic-configuration"></a>

#### Set `SPARK_HOME` via [inline generic configuration](#usage-interpreter-overview--inline-generic-confinterpreter)

Besides setting `SPARK_HOME` in interpreter setting page, you can also use inline generic configuration to put the
configuration with code together for more flexibility. e.g.
![](assets/images/spark-inline-configuration_4e805175d08fe40c.png)

<a id="interpreter-spark--set-master"></a>

### Set master

After setting `SPARK_HOME`, you need to set **spark.master** property in either interpreter setting page or inline configuartion. The value may vary depending on your Spark cluster deployment type.

For example,

- **local[\*]** in local mode
- **spark://master:7077** in standalone cluster
- **yarn-client** in Yarn client mode (Not supported in Spark 3.x, refer below for how to configure yarn-client in Spark 3.x)
- **yarn-cluster** in Yarn cluster mode (Not supported in Spark 3.x, refer below for how to configure yarn-cluster in Spark 3.x)
- **mesos://host:5050** in Mesos cluster

That's it. Zeppelin will work with any version of Spark and any deployment type without rebuilding Zeppelin in this way.
For the further information about Spark & Zeppelin version compatibility, please refer to "Available Interpreters" section in [Zeppelin download page](https://zeppelin.apache.org/download.html).

Note that without setting `SPARK_HOME`, it's running in local mode with included version of Spark. The included version may vary depending on the build profile. And this included version Spark has limited function, so it
is always recommended to set `SPARK_HOME`.

Yarn client mode and local mode will run driver in the same machine with zeppelin server, this would be dangerous for production. Because it may run out of memory when there's many Spark interpreters running at the same time. So we suggest you
only allow yarn-cluster mode via setting `zeppelin.spark.only_yarn_cluster` in `zeppelin-site.xml`.

<a id="interpreter-spark--configure-yarn-mode-for-spark-3.x"></a>

#### Configure yarn mode for Spark 3.x

Specifying `yarn-client` & `yarn-cluster` in `spark.master` is not supported in Spark 3.x any more, instead you need to use `spark.master` and `spark.submit.deployMode` together.

| Mode | spark.master | spark.submit.deployMode |
| --- | --- | --- |
| Yarn Client | yarn | client |
| Yarn Cluster | yarn | cluster |

<a id="interpreter-spark--interpreter-binding-mode"></a>

## Interpreter binding mode

The default [interpreter binding mode](#usage-interpreter-interpreter_binding_mode) is `globally shared`. That means all notes share the same Spark interpreter.

So we recommend you to use `isolated per note` which means each note has own Spark interpreter without affecting each other. But it may run out of your machine resource if too many
Spark interpreters are created, so we recommend to always use yarn-cluster mode in production if you run Spark in hadoop cluster. And you can use [inline configuration](#usage-interpreter-overview--inline-generic-configuration) via `%spark.conf` in the first paragraph to customize your spark configuration.

You can also choose `scoped` mode. For `scoped` per note mode, Zeppelin creates separated scala compiler/python shell for each note but share a single `SparkContext/SqlContext/SparkSession`.

<a id="interpreter-spark--sparkcontext-sqlcontext-sparksession-zeppelincontext"></a>

## SparkContext, SQLContext, SparkSession, ZeppelinContext

SparkContext, SparkSession and ZeppelinContext are automatically created and exposed as variable names `sc`, `spark` and `z` respectively, in Scala, Python and R environments.

> Note that Scala/Python/R environment shares the same SparkContext, SQLContext, SparkSession and ZeppelinContext instance.

<a id="interpreter-spark--yarn-mode"></a>

## Yarn Mode

Zeppelin support both yarn client and yarn cluster mode (yarn cluster mode is supported from 0.8.0). For yarn mode, you must specify `SPARK_HOME` & `HADOOP_CONF_DIR`.
Usually you only have one hadoop cluster, so you can set `HADOOP_CONF_DIR` in `zeppelin-env.sh` which is applied to all Spark interpreters. If you want to use spark against multiple hadoop cluster, then you need to define
`HADOOP_CONF_DIR` in interpreter setting or via inline generic configuration.

<a id="interpreter-spark--k8s-mode"></a>

## K8s Mode

Regarding how to run Spark on K8s in Zeppelin, please check [this doc](#quickstart-kubernetes).

<a id="interpreter-spark--pyspark"></a>

## PySpark

There are 2 ways to use PySpark in Zeppelin:

- Vanilla PySpark
- IPySpark

<a id="interpreter-spark--vanilla-pyspark-not-recommended"></a>

### Vanilla PySpark (Not Recommended)

Vanilla PySpark interpreter is almost the same as vanilla Python interpreter except Spark interpreter inject SparkContext, SQLContext, SparkSession via variables `sc`, `sqlContext`, `spark`.

By default, Zeppelin would use IPython in `%spark.pyspark` when IPython is available (Zeppelin would check whether ipython's prerequisites are met), Otherwise it would fall back to the vanilla PySpark implementation.

<a id="interpreter-spark--ipyspark-recommended"></a>

### IPySpark (Recommended)

You can use `IPySpark` explicitly via `%spark.ipyspark`. IPySpark interpreter is almost the same as IPython interpreter except Spark interpreter inject SparkContext, SQLContext, SparkSession via variables `sc`, `sqlContext`, `spark`.
For the IPython features, you can refer doc [Python Interpreter](#interpreter-python--ipython-interpreter-pythonipython-recommended)

<a id="interpreter-spark--sparkr"></a>

## SparkR

Zeppelin support SparkR via `%spark.r`, `%spark.ir` and `%spark.shiny`. Here's configuration for SparkR Interpreter.

| Spark Property | Default | Description |
| --- | --- | --- |
| zeppelin.R.cmd | R | R binary executable path. |
| zeppelin.R.knitr | true | Whether use knitr or not. (It is recommended to install knitr and use it in Zeppelin) |
| zeppelin.R.image.width | 100% | R plotting image width. |
| zeppelin.R.render.options | out.format = 'html', comment = NA, echo = FALSE, results = 'asis', message = F, warning = F, fig.retina = 2 | R plotting options. |
| zeppelin.R.shiny.iframe\_width | 100% | IFrame width of Shiny App |
| zeppelin.R.shiny.iframe\_height | 500px | IFrame height of Shiny App |
| zeppelin.R.shiny.portRange | : | Shiny app would launch a web app at some port, this property is to specify the portRange via format ':', e.g. '5000:5001'. By default it is ':' which means any port |

Refer [R doc](#interpreter-r) for how to use R in Zeppelin.

<a id="interpreter-spark--sparksql"></a>

## SparkSql

Spark sql interpreter share the same SparkContext/SparkSession with other Spark interpreters. That means any table registered in scala, python or r code can be accessed by Spark sql.
For examples:

```scala
%spark

case class People(name: String, age: Int)
var df = spark.createDataFrame(List(People("jeff", 23), People("andy", 20)))
df.createOrReplaceTempView("people")
```

```sql

%spark.sql

select * from people
```

You can write multiple sql statements in one paragraph. Each sql statement is separated by semicolon.
Sql statement in one paragraph would run sequentially.
But sql statements in different paragraphs can run concurrently by the following configuration.

1. Set `zeppelin.spark.concurrentSQL` to true to enable the sql concurrent feature, underneath zeppelin will change to use fairscheduler for Spark. And also set `zeppelin.spark.concurrentSQL.max` to control the max number of sql statements running concurrently.
2. Configure pools by creating `fairscheduler.xml` under your `SPARK_CONF_DIR`, check the official spark doc [Configuring Pool Properties](http://spark.apache.org/docs/latest/job-scheduling.html#configuring-pool-properties)
3. Set pool property via setting paragraph local property. e.g.

```
 %spark(pool=pool1)

 sql statement
```

This pool feature is also available for all versions of scala Spark, PySpark. For SparkR, it is only available starting from 2.3.0.

<a id="interpreter-spark--dependency-management"></a>

## Dependency Management

For Spark interpreter, it is not recommended to use Zeppelin's [Dependency Management](#usage-interpreter-dependency_management) for managing
third party dependencies (`%spark.dep` is removed from Zeppelin 0.9 as well). Instead, you should set the standard Spark properties as following:

| Spark Property | Spark Submit Argument | Description |
| --- | --- | --- |
| spark.files | --files | Comma-separated list of files to be placed in the working directory of each executor. Globs are allowed. |
| spark.jars | --jars | Comma-separated list of jars to include on the driver and executor classpaths. Globs are allowed. |
| spark.jars.packages | --packages | Comma-separated list of Maven coordinates of jars to include on the driver and executor classpaths. The coordinates should be groupId:artifactId:version. If spark.jars.ivySettings is given artifacts will be resolved according to the configuration in the file, otherwise artifacts will be searched for in the local maven repo, then maven central and finally any additional remote repositories given by the command-line option --repositories. |

As general Spark properties, you can set them in via inline configuration or interpreter setting page or in `zeppelin-env.sh` via environment variable `SPARK_SUBMIT_OPTIONS`.
For examples:

```bash
export SPARK_SUBMIT_OPTIONS="--files <my_file> --jars <my_jar> --packages <my_package>"
```

To be noticed, `SPARK_SUBMIT_OPTIONS` is deprecated and will be removed in future release.

<a id="interpreter-spark--zeppelincontext"></a>

## ZeppelinContext

Zeppelin automatically injects `ZeppelinContext` as variable `z` in your Scala/Python environment. `ZeppelinContext` provides some additional functions and utilities.
See [Zeppelin-Context](#usage-other_features-zeppelin_context) for more details. For Spark interpreter, you can use z to display Spark `Dataset/Dataframe`.

![](/docs/0.12.0/assets/themes/zeppelin/img/docs-img/spark_zshow.png)

<a id="interpreter-spark--setting-up-zeppelin-with-kerberos"></a>

## Setting up Zeppelin with Kerberos

Logical setup with Zeppelin, Kerberos Key Distribution Center (KDC), and Spark on YARN:

![](assets/images/kdc-zeppelin_6226bb4854890eac.png)

There are several ways to make Spark work with kerberos enabled hadoop cluster in Zeppelin.

1. Share one single hadoop cluster.
   In this case you just need to specify `zeppelin.server.kerberos.keytab` and `zeppelin.server.kerberos.principal` in zeppelin-site.xml, Spark interpreter will use these setting by default.
2. Work with multiple hadoop clusters.
   In this case you can specify `spark.yarn.keytab` and `spark.yarn.principal` to override `zeppelin.server.kerberos.keytab` and `zeppelin.server.kerberos.principal`.

<a id="interpreter-spark--configuration-setup"></a>

### Configuration Setup

1. On the server that Zeppelin is installed, install Kerberos client modules and configuration, krb5.conf.
   This is to make the server communicate with KDC.
2. Add the two properties below to Spark configuration (`[SPARK_HOME]/conf/spark-defaults.conf`):


```
spark.yarn.principal
spark.yarn.keytab
```

> **NOTE:** If you do not have permission to access for the above spark-defaults.conf file, optionally, you can add the above lines to the Spark Interpreter setting through the Interpreter tab in the Zeppelin UI.

1. That's it. Play with Zeppelin!

<a id="interpreter-spark--user-impersonation"></a>

## User Impersonation

In yarn mode, the user who launch the zeppelin server will be used to launch the Spark yarn application. This is not a good practise.
Most of time, you will enable shiro in Zeppelin and would like to use the login user to submit the Spark yarn app. For this purpose, you need to enable user impersonation for more security control. In order the enable user impersonation, you need to do the following steps

**Step 1** Enable user impersonation setting hadoop's `core-site.xml`. E.g. if you are using user `zeppelin` to launch Zeppelin, then add the following to `core-site.xml`, then restart both hdfs and yarn.

```xml
<property>
  <name>hadoop.proxyuser.zeppelin.groups</name>
  <value>*</value>
</property>
<property>
  <name>hadoop.proxyuser.zeppelin.hosts</name>
  <value>*</value>
</property>
```

**Step 2** Enable interpreter user impersonation in Spark interpreter's interpreter setting. (Enable shiro first of course)
![](assets/images/spark-user-impersonation_98b5864720c97871.png)

**Step 3(Optional)** If you are using kerberos cluster, then you need to set `zeppelin.server.kerberos.keytab` and `zeppelin.server.kerberos.principal` to the user(aka. user in Step 1) you want to
impersonate in `zeppelin-site.xml`.

<a id="interpreter-spark--community"></a>

## Community

[Join our community](http://zeppelin.apache.org/community.html) to discuss with others.

---

---

<a id="interpreter-flink"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/flink.html -->

<!-- page_index: 54 -->

<a id="interpreter-flink--flink-interpreter-for-apache-zeppelin"></a>

# Flink interpreter for Apache Zeppelin

<a id="interpreter-flink--overview"></a>

## Overview

[Apache Flink](https://flink.apache.org) is a framework and distributed processing engine for stateful computations over unbounded and bounded data streams.
Flink has been designed to run in all common cluster environments, perform computations at in-memory speed and at any scale.

In Zeppelin 0.9, we refactor the Flink interpreter in Zeppelin to support the latest version of Flink. **Currently, only Flink 1.15+ is supported, old versions of flink won't work.**
Apache Flink is supported in Zeppelin with the Flink interpreter group which consists of the five interpreters listed below.

| Name | Class | Description |
| --- | --- | --- |
| %flink | FlinkInterpreter | Creates ExecutionEnvironment/StreamExecutionEnvironment/BatchTableEnvironment/StreamTableEnvironment and provides a Scala environment |
| %flink.pyflink | PyFlinkInterpreter | Provides a python environment |
| %flink.ipyflink | IPyFlinkInterpreter | Provides an ipython environment |
| %flink.ssql | FlinkStreamSqlInterpreter | Provides a stream sql environment |
| %flink.bsql | FlinkBatchSqlInterpreter | Provides a batch sql environment |

<a id="interpreter-flink--main-features"></a>

## Main Features

| Feature | Description |
| --- | --- |
| Support multiple versions of Flink | You can run different versions of Flink in one Zeppelin instance |
| Support multiple languages | Scala, Python, SQL are supported, besides that you can also collaborate across languages, e.g. you can write Scala UDF and use it in PyFlink |
| Support multiple execution modes | Local \| Remote \| Yarn \| Yarn Application |
| Support Hive | Hive catalog is supported |
| Interactive development | Interactive development user experience increase your productivity |
| Enhancement on Flink SQL | \* Support both streaming sql and batch sql in one notebook \* Support sql comment (single line comment/multiple line comment) \* Support advanced configuration (jobName, parallelism) \* Support multiple insert statements |

<a id="interpreter-flink--play-flink-in-zeppelin-docker"></a>

## Play Flink in Zeppelin docker

For beginner, we would suggest you to play Flink in Zeppelin docker.
First you need to download Flink, because there's no Flink binary distribution shipped with Zeppelin.
e.g. Here we download Flink 1.12.2 to`/mnt/disk1/flink-1.12.2`, and we mount it to Zeppelin docker container and run the following command to start Zeppelin docker.

```bash
docker run -u $(id -u) -p 8080:8080 -p 8081:8081 --rm -v /mnt/disk1/flink-1.12.2:/opt/flink -e FLINK_HOME=/opt/flink  --name zeppelin apache/zeppelin:0.10.0
```

After running the above command, you can open `http://localhost:8080` to play Flink in Zeppelin. We only verify the flink local mode in Zeppelin docker, other modes may not due to network issues.
`-p 8081:8081` is to expose Flink web ui, so that you can access Flink web ui via `http://localhost:8081`.

Here's screenshot of running note `Flink Tutorial/5. Streaming Data Analytics`

![](assets/images/flink-docker-tutorial_86b59d3cab8e8b42.gif)

You can also mount notebook folder to replace the built-in zeppelin tutorial notebook.
e.g. Here's a repo of Flink sql cookbook on Zeppelin: <https://github.com/zjffdu/flink-sql-cookbook-on-zeppelin/>

You can clone this repo and mount it to docker,

```
docker run -u $(id -u) -p 8080:8080 --rm -v /mnt/disk1/flink-sql-cookbook-on-zeppelin:/notebook -v /mnt/disk1/flink-1.12.2:/opt/flink -e FLINK_HOME=/opt/flink  -e ZEPPELIN_NOTEBOOK_DIR='/notebook' --name zeppelin apache/zeppelin:0.10.0
```

<a id="interpreter-flink--prerequisites"></a>

## Prerequisites

Download Flink 1.15 or afterwards (Only Scala 2.12 is supported)

<a id="interpreter-flink--version-specific-notes-for-flink"></a>

### Version-specific notes for Flink

Flink 1.15 is scala free and has changed its binary distribution, the following extra steps is required.
\* Move FLINK*HOME/opt/flink-table-planner*2.12-1.15.0.jar to FLINK*HOME/lib
\* Move FLINK*HOME/lib/flink-table-planner-loader-1.15.0.jar to FLINK*HOME/opt
\* Download flink-table-api-scala-bridge*2.12-1.15.0.jar and flink-table-api-scala*2.12-1.15.0.jar to FLINK*HOME/lib

Flink 1.16 introduces new `ClientResourceManager` for sql client, you need to move `FLINK_HOME/opt/flink-sql-client-1.16.0.jar` to `FLINK_HOME/lib`

<a id="interpreter-flink--flink-on-zeppelin-architecture"></a>

## Flink on Zeppelin Architecture

![](assets/images/flink-architecture_7854c505366286e9.png)

The above diagram is the architecture of Flink on Zeppelin. Flink interpreter on the left side is actually a Flink client
which is responsible for compiling and managing Flink job lifecycle, such as submit, cancel job, monitoring job progress and so on. The Flink cluster on the right side is the place where executing Flink job.
It could be a MiniCluster (local mode), Standalone cluster (remote mode), Yarn session cluster (yarn mode) or Yarn application session cluster (yarn-application mode)

There are 2 important components in Flink interpreter: Scala shell & Python shell

- Scala shell is the entry point of Flink interpreter, it would create all the entry points of Flink program, such as ExecutionEnvironment，StreamExecutionEnvironment and TableEnvironment. Scala shell is responsible for compiling and running Scala code and sql.
- Python shell is the entry point of PyFlink, it is responsible for compiling and running Python code.

<a id="interpreter-flink--configuration"></a>

## Configuration

The Flink interpreter can be configured with properties provided by Zeppelin (as following table).
You can also add and set other Flink properties which are not listed in the table. For a list of additional properties, refer to [Flink Available Properties](https://ci.apache.org/projects/flink/flink-docs-master/ops/config.html).

| Property | Default | Description |
| --- | --- | --- |
| `FLINK_HOME` |  | Location of Flink installation. It is must be specified, otherwise you can not use Flink in Zeppelin |
| `HADOOP_CONF_DIR` |  | Location of hadoop conf, this is must be set if running in yarn mode |
| `HIVE_CONF_DIR` |  | Location of hive conf, this is must be set if you want to connect to hive metastore |
| flink.execution.mode | local | Execution mode of Flink, e.g. local \| remote \| yarn \| yarn-application |
| flink.execution.remote.host |  | Host name of running JobManager. Only used for remote mode |
| flink.execution.remote.port |  | Port of running JobManager. Only used for remote mode |
| jobmanager.memory.process.size | 1024m | Total memory size of JobManager, e.g. 1024m. It is official [Flink property](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/deployment/config/) |
| taskmanager.memory.process.size | 1024m | Total memory size of TaskManager, e.g. 1024m. It is official [Flink property](https://ci.apache.org/projects/flink/flink-docs-release-1.13/docs/deployment/config/) |
| taskmanager.numberOfTaskSlots | 1 | Number of slot per TaskManager |
| local.number-taskmanager | 4 | Total number of TaskManagers in local mode |
| yarn.application.name | Zeppelin Flink Session | Yarn app name |
| yarn.application.queue | default | queue name of yarn app |
| zeppelin.flink.uiWebUrl |  | User specified Flink JobManager url, it could be used in remote mode where Flink cluster is already started, or could be used as url template, e.g. https://knox-server:8443/gateway/cluster-topo/yarn/proxy/{{applicationId}}/ where {{applicationId}} is placeholder of yarn app id |
| zeppelin.flink.run.asLoginUser | true | Whether run Flink job as the Zeppelin login user, it is only applied when running Flink job in hadoop yarn cluster and shiro is enabled |
| flink.udf.jars |  | Flink udf jars (comma separated), Zeppelin will register udf in these jars automatically for user. These udf jars could be either local files or hdfs files if you have hadoop installed. The udf name is the class name. |
| flink.udf.jars.packages |  | Packages (comma separated) that would be searched for the udf defined in `flink.udf.jars`. Specifying this can reduce the number of classes to scan, otherwise all the classes in udf jar will be scanned. |
| flink.execution.jars |  | Additional user jars (comma separated), these jars could be either local files or hdfs files if you have hadoop installed. It can be used to specify Flink connector jars or udf jars (no udf class auto-registration like `flink.udf.jars`) |
| flink.execution.packages |  | Additional user packages (comma separated), e.g. `org.apache.flink:flink-json:1.10.0` |
| zeppelin.flink.concurrentBatchSql.max | 10 | Max concurrent sql of Batch Sql (`%flink.bsql`) |
| zeppelin.flink.concurrentStreamSql.max | 10 | Max concurrent sql of Stream Sql (`%flink.ssql`) |
| zeppelin.pyflink.python | python | Python binary executable for PyFlink |
| table.exec.resource.default-parallelism | 1 | Default parallelism for Flink sql job |
| zeppelin.flink.scala.color | true | Whether display Scala shell output in colorful format |
| zeppelin.flink.scala.shell.tmp*dir* |  | Temp folder for storing scala shell compiled jar |
| zeppelin.flink.enableHive | false | Whether enable hive |
| zeppelin.flink.hive.version | 2.3.7 | Hive version that you would like to connect |
| zeppelin.flink.module.enableHive | false | Whether enable hive module, hive udf take precedence over Flink udf if hive module is enabled. |
| zeppelin.flink.maxResult | 1000 | max number of row returned by sql interpreter |
| `zeppelin.flink.job.checkinterval`</td> <td>1000</td> <td>Check interval (in milliseconds) to check Flink job progress</td> </tr> <tr> <td>`flink.interpreter.close.shutdown*cluster`</td> <td>true</td> <td>Whether shutdown Flink cluster when closing interpreter</td> </tr> <tr> <td>`zeppelin.interpreter.close.cancel*job` | true | Whether cancel Flink job when closing interpreter |

<a id="interpreter-flink--interpreter-binding-mode"></a>

## Interpreter Binding Mode

The default [interpreter binding mode](#usage-interpreter-interpreter_binding_mode) is `globally shared`. That means all notes share the same Flink interpreter which means they share the same Flink cluster.
In practice, we would recommend you to use `isolated per note` which means each note has own Flink interpreter without affecting each other (Each one has his own Flink cluster).

<a id="interpreter-flink--execution-mode"></a>

## Execution Mode

Flink in Zeppelin supports 4 execution modes (`flink.execution.mode`):

- Local
- Remote
- Yarn
- Yarn Application

<a id="interpreter-flink--local-mode"></a>

### Local Mode

Running Flink in local mode will start a MiniCluster in local JVM. By default, the local MiniCluster use port 8081, so make sure this port is available in your machine, otherwise you can configure `rest.port` to specify another port. You can also specify `local.number-taskmanager` and `flink.tm.slot` to customize the number of TM and number of slots per TM.
Because by default it is only 4 TM with 1 slot in this MiniCluster which may not be enough for some cases.

<a id="interpreter-flink--remote-mode"></a>

### Remote Mode

Running Flink in remote mode will connect to an existing Flink cluster which could be standalone cluster or yarn session cluster. Besides specifying `flink.execution.mode` to be `remote`, you also need to specify
`flink.execution.remote.host` and `flink.execution.remote.port` to point to Flink job manager's rest api address.

<a id="interpreter-flink--yarn-mode"></a>

### Yarn Mode

In order to run Flink in Yarn mode, you need to make the following settings:

- Set `flink.execution.mode` to be `yarn`
- Set `HADOOP_CONF_DIR` in Flink's interpreter setting or `zeppelin-env.sh`.
- Make sure `hadoop` command is on your `PATH`. Because internally Flink will call command `hadoop classpath` and load all the hadoop related jars in the Flink interpreter process

In this mode, Zeppelin would launch a Flink yarn session cluster for you and destroy it when you shutdown your Flink interpreter.

<a id="interpreter-flink--yarn-application-mode"></a>

### Yarn Application Mode

In the above yarn mode, there will be a separated Flink interpreter process on the Zeppelin server host. However, this may run out of resources when there are too many interpreter processes.
So in practise, we would recommend you to use yarn application mode if you are using Flink 1.11 or afterwards (yarn application mode is only supported after Flink 1.11).
In this mode Flink interpreter runs in the JobManager which is in yarn container.
In order to run Flink in yarn application mode, you need to make the following settings:

- Set `flink.execution.mode` to be `yarn-application`
- Set `HADOOP_CONF_DIR` in Flink's interpreter setting or `zeppelin-env.sh`.
- Make sure `hadoop` command is on your `PATH`. Because internally flink will call command `hadoop classpath` and load all the hadoop related jars in Flink interpreter process

<a id="interpreter-flink--flink-scala"></a>

## Flink Scala

Scala is the default language of Flink on Zeppelin（`%flink`), and it is also the entry point of Flink interpreter. Underneath Flink interpreter will create Scala shell
which would create several built-in variables, including ExecutionEnvironment，StreamExecutionEnvironment and so on.
So don't create these Flink environment variables again, otherwise you might hit weird issues. The Scala code you write in Zeppelin will be submitted to this Scala shell.
Here are the builtin variables created in Flink Scala shell.

- senv (StreamExecutionEnvironment),
- benv (ExecutionEnvironment)
- stenv (StreamTableEnvironment for blink planner (aka. new planner))
- btenv (BatchTableEnvironment for blink planner (aka. new planner))
- z (ZeppelinContext)

<a id="interpreter-flink--blink-flink-planner"></a>

### Blink/Flink Planner

After Zeppelin 0.11, we remove the support of flink planner (aka. old planner) which is also removed after Flink 1.14.

<a id="interpreter-flink--stream-wordcount-example"></a>

### Stream WordCount Example

You can write whatever Scala code in Zeppelin.

e.g. in the following example, we write a classical streaming wordcount example.

![](assets/images/flink-streaming-wordcount_a3234d695c702ff4.png)

<a id="interpreter-flink--code-completion"></a>

### Code Completion

You can type tab for code completion.

![](assets/images/flink-scala-codecompletion_67ea4d453571b7c6.png)

<a id="interpreter-flink--zeppelincontext"></a>

### ZeppelinContext

`ZeppelinContext` provides some additional functions and utilities.
See [Zeppelin-Context](#usage-other_features-zeppelin_context) for more details.
For Flink interpreter, you can use `z` to display Flink `Dataset/Table`.

e.g. you can use `z.show` to display DataSet, Batch Table, Stream Table.

- z.show(DataSet)

![](assets/images/flink-z-dataset_1cdb9b93185f7b68.png)

- z.show(Batch Table)

![](assets/images/flink-z-batch-table_7e74bfc5ed31fefa.png)

- z.show(Stream Table)

![](assets/images/flink-z-stream-table_e4f30002432eb403.gif)

<a id="interpreter-flink--flink-sql"></a>

## Flink SQL

In Zeppelin, there are 2 kinds of Flink sql interpreter you can use

- `%flink.ssql`
  Streaming Sql interpreter which launch Flink streaming job via `StreamTableEnvironment`
- `%flink.bsql`
  Batch Sql interpreter which launch Flink batch job via `BatchTableEnvironment`

Flink Sql interpreter in Zeppelin is equal to Flink Sql-client + many other enhancement features.

<a id="interpreter-flink--enhancement-sql-features"></a>

### Enhancement SQL Features

<a id="interpreter-flink--support-batch-sql-and-streaming-sql-together."></a>

#### Support batch SQL and streaming sql together.

In Flink Sql-client, either you run streaming sql or run batch sql in one session. You can not run them together.
But in Zeppelin, you can do that. `%flink.ssql` is used for running streaming sql, while `%flink.bsql` is used for running batch sql.
Batch/Streaming Flink jobs run in the same Flink session cluster.

<a id="interpreter-flink--support-multiple-statements"></a>

#### Support multiple statements

You can write multiple sql statements in one paragraph, each sql statement is separated by semicolon.

<a id="interpreter-flink--comment-support"></a>

#### Comment support

2 kinds of sql comments are supported in Zeppelin:

- Single line comment start with `--`
- Multiple line comment around with `/* */`

![](assets/images/flink-sql-comment_3fa5329609ac2a8d.png)

<a id="interpreter-flink--job-parallelism-setting"></a>

#### Job parallelism setting

You can set the sql parallelism via paragraph local property: `parallelism`

![](assets/images/flink-sql-parallelism_1cc301ec65d3c98e.png)

<a id="interpreter-flink--support-multiple-insert"></a>

#### Support multiple insert

Sometimes you have multiple insert statements which read the same source, but write to different sinks. By default, each insert statement would launch a separated Flink job, but you can set paragraph local property: `runAsOne` to be `true` to run them in one single Flink job.

![](assets/images/flink-sql-multiple-insert_edaa5e7eecdb8a3b.png)

<a id="interpreter-flink--set-job-name"></a>

#### Set job name

You can set Flink job name for insert statement via setting paragraph local property: `jobName`. To be noticed, you can only set job name for insert statement. Select statement is not supported yet.
And this kind of setting only works for single insert statement. It doesn't work for multiple insert we mentioned above.

![](assets/images/flink-sql-jobname_615c85fc8e8e2434.png)

<a id="interpreter-flink--streaming-data-visualization"></a>

### Streaming Data Visualization

Zeppelin can visualize the select sql result of Flink streaming job. Overall it supports 3 modes:

- Single
- Update
- Append

<a id="interpreter-flink--single-mode"></a>

#### Single Mode

Single mode is for the case when the result of sql statement is always one row, such as the following example. The output format is HTML, and you can specify paragraph local property `template` for the final output content template.
You can use `{i}` as placeholder for the `ith` column of result.

![](assets/images/flink-single-mode_3957b3d183c3ee7a.gif)

<a id="interpreter-flink--update-mode"></a>

#### Update Mode

Update mode is suitable for the case when the output is more than one rows, and will always be updated continuously.
Here’s one example where we use group by.

![](assets/images/flink-update-mode_442f3bdead700bf3.gif)

<a id="interpreter-flink--append-mode"></a>

#### Append Mode

Append mode is suitable for the scenario where output data is always appended.
E.g. the following example which use tumble window.

![](assets/images/flink-append-mode_f0246366189b4321.gif)

<a id="interpreter-flink--pyflink"></a>

## PyFlink

PyFlink is Python entry point of Flink on Zeppelin, internally Flink interpreter will create Python shell which
would create Flink's environment variables (including ExecutionEnvironment, StreamExecutionEnvironment and so on).
To be noticed, the java environment behind Pyflink is created in Scala shell.
That means underneath Scala shell and Python shell share the same environment.
These are variables created in Python shell.

- `s_env` (StreamExecutionEnvironment),
- `b_env` (ExecutionEnvironment)
- `st_env` (StreamTableEnvironment for blink planner (aka. new planner))
- `bt_env` (BatchTableEnvironment for blink planner (aka. new planner))

<a id="interpreter-flink--configure-pyflink"></a>

### Configure PyFlink

There are 3 things you need to configure to make Pyflink work in Zeppelin.

- Install pyflink
  e.g. ( pip install apache-flink==1.11.1 ).
  If you need to use Pyflink udf, then you to install pyflink on all the task manager nodes. That means if you are using yarn, then all the yarn nodes need to install pyflink.
- Copy `python` folder under `${FLINK_HOME}/opt` to `${FLINK_HOME/lib`.
- Set `zeppelin.pyflink.python` as the python executable path. By default, it is the python in `PATH`. In case you have multiple versions of python installed, you need to configure `zeppelin.pyflink.python` as the python version you want to use.

<a id="interpreter-flink--how-to-use-pyflink"></a>

### How to use PyFlink

There are 2 ways to use PyFlink in Zeppelin

- `%flink.pyflink`
- `%flink.ipyflink`

`%flink.pyflink` is much simple and easy, you don't need to do anything except the above setting, but its function is also limited. We suggest you to use `%flink.ipyflink` which provides almost the same user experience like jupyter.

<a id="interpreter-flink--configure-ipyflink"></a>

### Configure IPyFlink

If you don't have anaconda installed, then you need to install the following 3 libraries.

```
pip install jupyter
pip install grpcio
pip install protobuf
```

If you have anaconda installed, then you only need to install following 2 libraries.

```
pip install grpcio
pip install protobuf
```

`ZeppelinContext` is also available in PyFlink, you can use it almost the same as in Flink Scala.

Check the [Python doc](#interpreter-python) for more features of IPython.

<a id="interpreter-flink--third-party-dependencies"></a>

## Third party dependencies

It is very common to have third party dependencies when you write Flink job in whatever languages (Scala, Python, Sql).
It is very easy to add dependencies in IDE (e.g. add dependency in pom.xml), but how can you do that in Zeppelin ? Mainly there are 2 settings you can use to add third party dependencies

- flink.execution.packages
- flink.execution.jars

<a id="interpreter-flink--flink.execution.packages"></a>

### flink.execution.packages

This is the recommended way of adding dependencies. Its implementation is the same as adding
dependencies in `pom.xml`. Underneath it would download all the packages and its transitive dependencies
from maven repository, then put them on the classpath. Here's one example of how to add kafka connector of Flink 1.10 via [inline configuration](#usage-interpreter-overview--inline-generic-configuration).

```
%flink.conf

flink.execution.packages  org.apache.flink:flink-connector-kafka_2.11:1.10.0,org.apache.flink:flink-connector-kafka-base_2.11:1.10.0,org.apache.flink:flink-json:1.10.0
```

The format is `artifactGroup:artifactId:version`, if you have multiple packages, then separate them with comma. `flink.execution.packages` requires internet accessible.
So if you can not access internet, you need to use `flink.execution.jars` instead.

<a id="interpreter-flink--flink.execution.jars"></a>

### flink.execution.jars

If your Zeppelin machine can not access internet or your dependencies are not deployed to maven repository, then you can use `flink.execution.jars` to specify the jar files you depend on (each jar file is separated with comma)

Here's one example of how to add kafka dependencies(including kafka connector and its transitive dependencies) via `flink.execution.jars`

```
%flink.conf

flink.execution.jars /usr/lib/flink-kafka/target/flink-kafka-1.0-SNAPSHOT.jar
```

<a id="interpreter-flink--flink-udf"></a>

## Flink UDF

There are 4 ways you can define UDF in Zeppelin.

- Write Scala UDF
- Write PyFlink UDF
- Create UDF via SQL
- Configure udf jar via flink.udf.jars

<a id="interpreter-flink--scala-udf"></a>

### Scala UDF

```scala
%flink

class ScalaUpper extends ScalarFunction {
  def eval(str: String) = str.toUpperCase
}

btenv.registerFunction("scala_upper", new ScalaUpper())
```

It is very straightforward to define scala udf almost the same as what you do in IDE.
After creating udf class, you need to register it via `btenv`.
You can also register it via `stenv` which share the same Catalog with `btenv`.

<a id="interpreter-flink--python-udf"></a>

### Python UDF

```python

%flink.pyflink

class PythonUpper(ScalarFunction):
  def eval(self, s):
    return s.upper()

bt_env.register_function("python_upper", udf(PythonUpper(), DataTypes.STRING(), DataTypes.STRING()))
```

It is also very straightforward to define Python udf almost the same as what you do in IDE.
After creating udf class, you need to register it via `bt_env`.
You can also register it via `st_env` which share the same Catalog with `bt_env`.

<a id="interpreter-flink--udf-via-sql"></a>

### UDF via SQL

Some simple udf can be written in Zeppelin. But if the udf logic is very complicated, then it is better to write it in IDE, then register it in Zeppelin as following

```sql
%flink.ssql

CREATE FUNCTION myupper AS 'org.apache.zeppelin.flink.udf.JavaUpper';
```

But this kind of approach requires the udf jar must be on `CLASSPATH`, so you need to configure `flink.execution.jars` to include this udf jar on `CLASSPATH`, such as following:

```
%flink.conf

flink.execution.jars /usr/lib/flink-udf-1.0-SNAPSHOT.jar
```

<a id="interpreter-flink--flink.udf.jars"></a>

### flink.udf.jars

The above 3 approaches all have some limitations:

- It is suitable to write simple Scala udf or Python udf in Zeppelin, but not suitable to write very complicated udf in Zeppelin. Because notebook doesn't provide advanced features compared to IDE, such as package management, code navigation and etc.
- It is not easy to share the udf between notes or users, you have to run the paragraph of defining udf in each flink interpreter.

So when you have many udfs or udf logic is very complicated and you don't want to register them by yourself every time, then you can use `flink.udf.jars`

- Step 1. Create a udf project in your IDE, write your udf there.
- Step 2. Set `flink.udf.jars` to point to the udf jar you build from your udf project

For example,

```
%flink.conf

flink.execution.jars /usr/lib/flink-udf-1.0-SNAPSHOT.jar
```

Zeppelin would scan this jar, find out all the udf classes and then register them automatically for you.
The udf name is the class name. For example, here's the output of show functions after specifing the above udf jars in `flink.udf.jars`

![](assets/images/flink-udf-jars_5c875a249d0c5689.png)

By default, Zeppelin would scan all the classes in this jar, so it would be pretty slow if your jar is very big specially when your udf jar has other dependencies.
So in this case we would recommend you to specify `flink.udf.jars.packages` to specify the package to scan, this can reduce the number of classes to scan and make the udf detection much faster.

<a id="interpreter-flink--how-to-use-hive"></a>

## How to use Hive

In order to use Hive in Flink, you have to make the following settings.

- Set `zeppelin.flink.enableHive` to be true
- Set `zeppelin.flink.hive.version` to be the hive version you are using.
- Set `HIVE_CONF_DIR` to be the location where `hive-site.xml` is located. Make sure hive metastore is started and you have configured `hive.metastore.uris` in `hive-site.xml`
- Copy the following dependencies to the lib folder of flink installation.
  - flink-connector-hive\_2.11–\*.jar
  - flink-hadoop-compatibility\_2.11–\*.jar
  - hive-exec-2.x.jar (for hive 1.x, you need to copy hive-exec-1.x.jar, hive-metastore-1.x.jar, libfb303–0.9.2.jar and libthrift-0.9.2.jar)

<a id="interpreter-flink--paragraph-local-properties"></a>

## Paragraph local properties

In the section of `Streaming Data Visualization`, we demonstrate the different visualization type via paragraph local properties: `type`.
In this section, we will list and explain all the supported local properties in Flink interpreter.

| Property | Default | Description |
| --- | --- | --- |
| type |  | Used in %flink.ssql to specify the streaming visualization type (single, update, append) |
| refreshInterval | 3000 | Used in `%flink.ssql` to specify frontend refresh interval for streaming data visualization. |
| template | {0} | Used in `%flink.ssql` to specify html template for `single` type of streaming data visualization, And you can use `{i}` as placeholder for the {i}th column of the result. |
| parallelism |  | Used in %flink.ssql & %flink.bsql to specify the flink sql job parallelism |
| maxParallelism |  | Used in %flink.ssql & %flink.bsql to specify the flink sql job max parallelism in case you want to change parallelism later. For more details, refer this [link](https://ci.apache.org/projects/flink/flink-docs-release-1.10/dev/parallel.html#setting-the-maximum-parallelism) |
| savepointDir |  | If you specify it, then when you cancel your flink job in Zeppelin, it would also do savepoint and store state in this directory. And when you resume your job, it would resume from this savepoint. |
| execution.savepoint.path |  | When you resume your job, it would resume from this savepoint path. |
| resumeFromSavepoint |  | Resume flink job from savepoint if you specify savepointDir. |
| resumeFromLatestCheckpoint |  | Resume flink job from latest checkpoint if you enable checkpoint. |
| runAsOne | false | All the insert into sql will run in a single flink job if this is true. |

<a id="interpreter-flink--tutorial-notes"></a>

## Tutorial Notes

Zeppelin is shipped with several Flink tutorial notes which may be helpful for you. You can check for more features in the tutorial notes.

<a id="interpreter-flink--community"></a>

## Community

[Join our community](http://zeppelin.apache.org/community.html) to discuss with others.

---

---

<a id="interpreter-jdbc"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/jdbc.html -->

<!-- page_index: 55 -->

<a id="interpreter-jdbc--generic-jdbc-interpreter-for-apache-zeppelin"></a>

# Generic JDBC Interpreter for Apache Zeppelin

<a id="interpreter-jdbc--overview"></a>

## Overview

JDBC interpreter lets you create a JDBC connection to any data sources seamlessly.

Inserts, Updates, and Upserts are applied immediately after running each statement.

By now, it has been tested with:

![](assets/images/tested-databases_59b8a0c7bfabfe5b.png)

- [Postgresql](http://www.postgresql.org/) -
  [JDBC Driver](https://jdbc.postgresql.org/)
- [Mysql](https://www.mysql.com/) -
  [JDBC Driver](https://dev.mysql.com/downloads/connector/j/)
- [MariaDB](https://mariadb.org/) -
  [JDBC Driver](https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/)
- [Redshift](https://aws.amazon.com/documentation/redshift/) -
  [JDBC Driver](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html)
- [Apache Hive](https://hive.apache.org/) -
  [JDBC Driver](https://cwiki.apache.org/confluence/display/Hive/HiveServer2+Clients#HiveServer2Clients-JDBC)
- [Presto/Trino](https://trino.io/) -
  [JDBC Driver](https://trino.io/docs/current/installation/jdbc.html)
- [Impala](https://impala.apache.org/) -
  [JDBC Driver](https://impala.apache.org/docs/build/html/topics/impala_jdbc.html)
- [Apache Phoenix](https://phoenix.apache.org/) itself is a JDBC driver
- [Apache Drill](https://drill.apache.org/) -
  [JDBC Driver](https://drill.apache.org/docs/using-the-jdbc-driver)
- [Apache Tajo](http://tajo.apache.org/) -
  [JDBC Driver](https://tajo.apache.org/docs/current/jdbc_driver.html)

If you are using other databases not in the above list, please feel free to share your use case. It would be helpful to improve the functionality of JDBC interpreter.

<a id="interpreter-jdbc--create-a-new-jdbc-interpreter"></a>

## Create a new JDBC Interpreter

First, click `+ Create` button at the top-right corner in the interpreter setting page.

![](assets/images/click-create-button_5eb0bfe622dda524.png)

Fill `Interpreter name` field with whatever you want to use as the alias(e.g. mysql, mysql2, hive, redshift, and etc..).
Please note that this alias will be used as `%interpreter_name` to call the interpreter in the paragraph.
Then select `jdbc` as an `Interpreter group`.

![](assets/images/select-name-and-group_81d524fbfa37e59f.png)

The default driver of JDBC interpreter is set as `PostgreSQL`. It means Zeppelin includes `PostgreSQL` driver jar in itself.
So you don't need to add any dependencies(e.g. the artifact name or path for `PostgreSQL` driver jar) for `PostgreSQL` connection.
The JDBC interpreter properties are defined by default like below.

| Name | Default Value | Description |
| --- | --- | --- |
| common.max\_count | 1000 | The maximun number of SQL result to display |
| default.driver | org.postgresql.Driver | JDBC Driver Name |
| default.password |  | The JDBC user password |
| default.url | jdbc:postgresql://localhost:5432/ | The URL for JDBC |
| default.user | gpadmin | The JDBC user name |
| default.precode |  | Some SQL which executes every time after initialization of the interpreter (see [Binding mode](#usage-interpreter-overview--interpreter-binding-mode)) |
| default.statementPrecode |  | SQL code which executed before the SQL from paragraph, in the same database session (database connection) |
| default.completer.schemaFilters |  | Сomma separated schema (schema = catalog = database) filters to get metadata for completions. Supports '%' symbol is equivalent to any set of characters. (ex. prod\_v\_%,public%,info) |
| default.completer.ttlInSeconds | 120 | Time to live sql completer in seconds (-1 to update everytime, 0 to disable update) |

If you want to connect other databases such as `Mysql`, `Redshift` and `Hive`, you need to edit the property values.
You can also use [Credential](#setup-security-datasource_authorization) for JDBC authentication.
If `default.user` and `default.password` properties are deleted(using X button) for database connection in the interpreter setting page, the JDBC interpreter will get the account information from [Credential](#setup-security-datasource_authorization).

The below example is for `Mysql` connection.

![](assets/images/edit-properties_9f67eafad7d71230.png)

The last step is **Dependency Setting**. Since Zeppelin only includes `PostgreSQL` driver jar by default, you need to add each driver's maven coordinates or JDBC driver's jar file path for the other databases.

![](assets/images/edit-dependencies_3b983b3aaff67169.png)

That's it. You can find more JDBC connection setting examples([MySQL](#interpreter-jdbc--mysql), [MariaDB](#interpreter-jdbc--mariadb), [Redshift](#interpreter-jdbc--redshift), [Apache Hive](#interpreter-jdbc--apache-hive), [Presto/Trino](#interpreter-jdbc--prestotrino), [Impala](#interpreter-jdbc--impala), [Apache Kyuubi](#interpreter-jdbc--apache-kyuubi), [Apache Phoenix](#interpreter-jdbc--apache-phoenix), and [Apache Tajo](#interpreter-jdbc--apache-tajo)) in [this section](#interpreter-jdbc--examples).

<a id="interpreter-jdbc--jdbc-interpreter-datasource-pool-configuration"></a>

## JDBC Interpreter Datasource Pool Configuration

The Jdbc interpreter uses the connection pool technology, and supports users to do some personal configuration of the connection pool. For example, we can configure `default.validationQuery='select 1'` and `default.testOnBorrow=true` in the Interpreter configuration to avoid the "Invalid SessionHandle" runtime error caused by Session timeout when connecting to HiveServer2 through JDBC interpreter.

The Jdbc Interpreter supports the following database connection pool configurations:

| Property Name | Default | Description |
| --- | --- | --- |
| testOnBorrow | false | The indication of whether objects will be validated before being borrowed from the pool. If the object fails to validate, it will be dropped from the pool, and we will attempt to borrow another. |
| testOnCreate | false | The indication of whether objects will be validated after creation. If the object fails to validate, the borrow attempt that triggered the object creation will fail. |
| testOnReturn | false | The indication of whether objects will be validated before being returned to the pool. |
| testWhileIdle | false | The indication of whether objects will be validated by the idle object evictor (if any). If an object fails to validate, it will be dropped from the pool. |
| timeBetweenEvictionRunsMillis | -1L | The number of milliseconds to sleep between runs of the idle object evictor thread. When non-positive, no idle object evictor thread will be run. |
| maxWaitMillis | -1L | The maximum number of milliseconds that the pool will wait (when there are no available connections) for a connection to be returned before throwing an exception, or -1 to wait indefinitely. |
| maxIdle | 8 | The maximum number of connections that can remain idle in the pool, without extra ones being released, or negative for no limit. |
| minIdle | 0 | The minimum number of connections that can remain idle in the pool, without extra ones being created, or zero to create none. |
| maxTotal | -1 | The maximum number of active connections that can be allocated from this pool at the same time, or negative for no limit. |
| validationQuery | show database | The SQL query that will be used to validate connections from this pool before returning them to the caller. If specified, this query MUST be an SQL SELECT statement that returns at least one row. If not specified, connections will be validation by calling the isValid() method. |

<a id="interpreter-jdbc--more-properties"></a>

## More properties

There are more JDBC interpreter properties you can specify like below.

| Property Name | Description |
| --- | --- |
| common.max\_result | Max number of SQL result to display to prevent the browser overload. This is common properties for all connections |
| zeppelin.jdbc.auth.type | Types of authentications' methods supported are `SIMPLE`, and `KERBEROS` |
| zeppelin.jdbc.principal | The principal name to load from the keytab |
| zeppelin.jdbc.keytab.location | The path to the keytab file |
| zeppelin.jdbc.auth.kerberos.proxy.enable | When auth type is Kerberos, enable/disable Kerberos proxy with the login user to get the connection. Default value is true. |
| default.jceks.file | jceks store path (e.g: jceks://file/tmp/zeppelin.jceks) |
| default.jceks.credentialKey | jceks credential key |
| zeppelin.jdbc.interpolation | Enables ZeppelinContext variable interpolation into paragraph text. Default value is false. |
| zeppelin.jdbc.maxConnLifetime | Maximum of connection lifetime in milliseconds. A value of zero or less means the connection has an infinite lifetime. |

You can also add more properties by using this [method](http://docs.oracle.com/javase/7/docs/api/java/sql/DriverManager.html#getConnection%28java.lang.String,%20java.util.Properties%29).
For example, if a connection needs a schema parameter, it would have to add the property as follows:

| name | value |
| --- | --- |
| default.schema | schema\_name |

<a id="interpreter-jdbc--how-to-use"></a>

## How to use

<a id="interpreter-jdbc--run-the-paragraph-with-jdbc-interpreter"></a>

### Run the paragraph with JDBC interpreter

To test whether your databases and Zeppelin are successfully connected or not, type `%jdbc_interpreter_name`(e.g. `%mysql`) at the top of the paragraph and run `show databases`.

```sql
%jdbc_interpreter_name

show databases
```

If the paragraph is `FINISHED` without any errors, a new paragraph will be automatically added after the previous one with `%jdbc_interpreter_name`.
So you don't need to type this prefix in every paragraphs' header.

![](assets/images/run-paragraph-with-jdbc_4049ef0878b4e1b7.png)

<a id="interpreter-jdbc--multiple-sql-statements"></a>

### Multiple SQL statements

You can write multiple sql statements in one paragraph, just separate them with semi-colon. e.g

```sql
%jdbc_interpreter_name

USE zeppelin_demo;

CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20),
       species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
```

<a id="interpreter-jdbc--sql-comment"></a>

### SQL Comment

2 kinds of SQL comments are supported:

- Single line comment start with `--`
- Multiple line comment around with `/* ... */`

```sql

%jdbc_interpreter_name

-- single line comment
show tables;
/* multiple
   line
   comment
 */
select * from test_1;
```

<a id="interpreter-jdbc--apply-zeppelin-dynamic-forms"></a>

### Apply Zeppelin Dynamic Forms

You can leverage [Zeppelin Dynamic Form](#usage-dynamic_form-intro) inside your queries. You can use both the `text input` and `select form` parametrization features.

<a id="interpreter-jdbc--run-sql-continuously"></a>

### Run SQL Continuously

By default, sql statements in one paragraph are executed only once. But you can run it continuously by specifying local property `refreshInterval` (unit: milli-seconds), So that the sql statements are executed every interval of `refreshInterval` milli-seconds. This is useful when your data in database is updated continuously by external system, and you can build dynamic dashboard in Zeppelin via this approach.

e.g. Here we query the mysql which is updated continuously by other external system.

![](assets/images/jdbc-refresh_64b598aacd9ea9f7.gif)

<a id="interpreter-jdbc--usage-precode"></a>

### Usage *precode*

You can set *precode* for each data source. Code runs once while opening the connection.

<a id="interpreter-jdbc--properties"></a>

##### Properties

An example settings of interpreter for the two data sources, each of which has its *precode* parameter.

| Property Name | Value |
| --- | --- |
| default.driver | org.postgresql.Driver |
| default.password | 1 |
| default.url | jdbc:postgresql://localhost:5432/ |
| default.user | postgres |
| default.precode | set search\_path='test\_path' |

| default.driver | com.mysql.jdbc.Driver |
| --- | --- |
| default.password | 1 |
| default.url | jdbc:mysql://localhost:3306/ |
| default.user | root |
| default.precode | set @v=12 |

<a id="interpreter-jdbc--usage"></a>

##### Usage

Test of execution *precode* for each data source.

```sql
%jdbc

show search_path
```

Returns value of `search_path` which is set in the default jdbc (use postgresql) interpreter's *default.precode*.

```sql
%mysql

select @v
```

Returns value of `v` which is set in the mysql interpreter's *default.precode*.

<a id="interpreter-jdbc--examples"></a>

## Examples

Here are some examples you can refer to. Including the below connectors, you can connect every databases as long as it can be configured with it's JDBC driver.

<a id="interpreter-jdbc--postgres"></a>

### Postgres

![](assets/images/postgres-setting_c9cf8b4c9e419d4a.png)

<a id="interpreter-jdbc--properties-2"></a>

##### Properties

| Name | Value |
| --- | --- |
| default.driver | org.postgresql.Driver |
| default.url | jdbc:postgresql://localhost:5432/ |
| default.user | pg\_user |
| default.password | pg\_password |

[Postgres JDBC Driver Docs](https://jdbc.postgresql.org/documentation/documentation.html)

<a id="interpreter-jdbc--dependencies"></a>

##### Dependencies

| Artifact | Excludes |
| --- | --- |
| org.postgresql:postgresql:42.3.3 |  |

[Maven Repository: org.postgresql:postgresql](https://mvnrepository.com/artifact/org.postgresql/postgresql)

<a id="interpreter-jdbc--mysql"></a>

### Mysql

![](assets/images/mysql-setting_e7325a57c145e6b3.png)

<a id="interpreter-jdbc--properties-3"></a>

##### Properties

| Name | Value |
| --- | --- |
| default.driver | com.mysql.jdbc.Driver |
| default.url | jdbc:mysql://localhost:3306/ |
| default.user | mysql\_user |
| default.password | mysql\_password |

[Mysql JDBC Driver Docs](https://dev.mysql.com/downloads/connector/j/)

<a id="interpreter-jdbc--dependencies-2"></a>

##### Dependencies

| Artifact | Excludes |
| --- | --- |
| mysql:mysql-connector-java:5.1.38 |  |

[Maven Repository: mysql:mysql-connector-java](https://mvnrepository.com/artifact/mysql/mysql-connector-java)

<a id="interpreter-jdbc--mariadb"></a>

### MariaDB

![](assets/images/mariadb-setting_5d3e1c801d03ff97.png)

<a id="interpreter-jdbc--properties-4"></a>

##### Properties

| Name | Value |
| --- | --- |
| default.driver | org.mariadb.jdbc.Driver |
| default.url | jdbc:mariadb://localhost:3306 |
| default.user | mariadb\_user |
| default.password | mariadb\_password |

[MariaDB JDBC Driver Docs](https://mariadb.com/kb/en/mariadb/about-mariadb-connector-j/)

<a id="interpreter-jdbc--dependencies-3"></a>

##### Dependencies

| Artifact | Excludes |
| --- | --- |
| org.mariadb.jdbc:mariadb-java-client:1.5.4 |  |

[Maven Repository: org.mariadb.jdbc:mariadb-java-client](https://mvnrepository.com/artifact/org.mariadb.jdbc/mariadb-java-client)

<a id="interpreter-jdbc--redshift"></a>

### Redshift

![](assets/images/redshift-setting_66ad9b097cee0144.png)

<a id="interpreter-jdbc--properties-5"></a>

##### Properties

| Name | Value |
| --- | --- |
| default.driver | com.amazon.redshift.jdbc42.Driver |
| default.url | jdbc:redshift://your-redshift-instance-address.redshift.amazonaws.com:5439/your-database |
| default.user | redshift\_user |
| default.password | redshift\_password |

[AWS Redshift JDBC Driver Docs](http://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html)

<a id="interpreter-jdbc--dependencies-4"></a>

##### Dependencies

| Artifact | Excludes |
| --- | --- |
| com.amazon.redshift:redshift-jdbc42:2.1.0.18 |  |

[Maven Repository: com.amazon.redshift:redshift-jdbc42](https://mvnrepository.com/artifact/com.amazon.redshift/redshift-jdbc42)

<a id="interpreter-jdbc--apache-hive"></a>

### Apache Hive

Zeppelin just connect to `hiveserver2` to run hive sql via hive jdbc. There are 2 cases of connecting with Hive:

- Connect to Hive without KERBEROS
- Connect to Hive with KERBEROS

Each case requires different settings.

<a id="interpreter-jdbc--connect-to-hive-without-kerberos"></a>

##### Connect to Hive without KERBEROS

In this scenario, you need to make the following settings at least. By default, hive job run as user of `default.user`.
Refer [impersonation](#interpreter-jdbc--impersonation) if you want hive job run as the Zeppelin login user when authentication is enabled.

| Name | Value |
| --- | --- |
| default.driver | org.apache.hive.jdbc.HiveDriver |
| default.url | jdbc:hive2://localhost:10000 |
| default.user | hive\_user |

| Artifact | Excludes |
| --- | --- |
| org.apache.hive:hive-jdbc:2.3.4 |  |

<a id="interpreter-jdbc--connect-to-hive-with-kerberos"></a>

##### Connect to Hive with KERBEROS

In this scenario, you need to make the following settings at least. By default, hive job run as user of client principal (`zeppelin.jdbc.principal`).
Refer [impersonation](#interpreter-jdbc--impersonation) if you want hive job run as the Zeppelin login user when authentication is enabled.

| Name | Value |
| --- | --- |
| default.driver | org.apache.hive.jdbc.HiveDriver |
| default.url | jdbc:hive2://emr-header-1:10000/default;principal={hive\_server2\_principal} |
| zeppelin.jdbc.auth.type | KERBEROS |
| zeppelin.jdbc.keytab.location | keytab of client |
| zeppelin.jdbc.principal | principal of client |

| Artifact | Excludes |
| --- | --- |
| org.apache.hive:hive-jdbc:2.3.4 |  |
| org.apache.hive:hive-exec:2.3.4 |  |

[Maven Repository : org.apache.hive:hive-jdbc](https://mvnrepository.com/artifact/org.apache.hive/hive-jdbc)

<a id="interpreter-jdbc--impersonation"></a>

##### Impersonation

When Zeppelin server is running with authentication enabled, then the interpreter can utilize Hive's user proxy feature
i.e. send extra parameter for creating and running a session ("hive.server2.proxy.user=": "${loggedInUser}").
This is particularly useful when multiple users are sharing a notebook.

To enable this set following:

- `default.proxy.user.property` as `hive.server2.proxy.user`

See [User Impersonation in interpreter](#usage-interpreter-user_impersonation) for more information.

<a id="interpreter-jdbc--sample-configuration"></a>

##### Sample configuration

| Name | Value |
| --- | --- |
| default.driver | org.apache.hive.jdbc.HiveDriver |
| default.url | jdbc:hive2://hive-server-host:2181/;serviceDiscoveryMode=zooKeeper;zooKeeperNamespace=hiveserver2 |
| default.proxy.user.property | default.server2.proxy.user |
| zeppelin.jdbc.auth.type | SIMPLE |

See [Hive Interpreter](#interpreter-hive) for more properties about Hive interpreter.

<a id="interpreter-jdbc--presto-trino"></a>

### Presto/Trino

Properties

| Name | Value |
| --- | --- |
| default.driver | io.prestosql.jdbc.PrestoDriver |
| default.url | jdbc:presto://presto-server:9090/hive |
| default.user | presto\_user |

[Trino JDBC Driver Docs](https://trino.io/docs/current/installation/jdbc.html)
[Presto JDBC Driver Docs](https://prestodb.io/docs/current/installation/jdbc.html)

Dependencies

| Artifact | Excludes |
| --- | --- |
| io.prestosql:presto-jdbc:350 |  |

<a id="interpreter-jdbc--impala"></a>

### Impala

Properties

| Name | Value |
| --- | --- |
| default.driver | org.apache.hive.jdbc.HiveDriver |
| default.url | jdbc:hive2://emr-header-1.cluster-47080:21050/;auth=noSasl |

Dependencies

| Artifact | Excludes |
| --- | --- |
| org.apache.hive:hive-jdbc:2.3.4 |  |

[Impala JDBC Driver Docs](https://impala.apache.org/docs/build/html/topics/impala_jdbc.html)

Dependencies

| Artifact | Excludes |
| --- | --- |
| io.prestosql:presto-jdbc:350 |  |

<a id="interpreter-jdbc--apache-kyuubi"></a>

### Apache Kyuubi

Zeppelin connect to Kyuubi to run SQL via [Kyuubi JDBC Driver](https://kyuubi.readthedocs.io/en/master/client/jdbc/kyuubi_jdbc.html). There are 2 cases of connecting with Kyuubi:

- Connect to Kyuubi without KERBEROS
- Connect to Kyuubi with KERBEROS

Each case requires different settings.

<a id="interpreter-jdbc--connect-to-kyuubi-without-kerberos"></a>

##### Connect to Kyuubi without KERBEROS

In this scenario, you need to make the following settings at least. Kyuubi engine run as user of `default.user`.

Properties

| Name | Value |
| --- | --- |
| default.driver | org.apache.kyuubi.jdbc.KyuubiHiveDriver |
| default.url | jdbc:kyuubi://kyuubi-server:10009 |

Dependencies

| Artifact | Excludes |
| --- | --- |
| org.apache.kyuubi:kyuubi-hive-jdbc-shaded:1.9.0 |  |

<a id="interpreter-jdbc--connect-to-kyuubi-with-kerberos"></a>

##### Connect to Kyuubi with KERBEROS

In this scenario, you need to make the following settings at least. Kyuubi engine run as user of client principal (`zeppelin.jdbc.principal`).

Properties

| Name | Value |
| --- | --- |
| default.driver | org.apache.kyuubi.jdbc.KyuubiHiveDriver |
| default.url | jdbc:kyuubi://kyuubi-server:10009/default;principal={kyuubi\_server\_principal} |
| zeppelin.jdbc.auth.type | KERBEROS |
| zeppelin.jdbc.keytab.location | keytab of client |
| zeppelin.jdbc.principal | principal of client |

Dependencies

| Artifact | Excludes |
| --- | --- |
| org.apache.kyuubi:kyuubi-hive-jdbc-shaded:1.9.0 |  |
| org.apache.hadoop:hadoop-client-api:3.3.6 |  |
| org.apache.hadoop:hadoop-client-runtime:3.3.6 |  |

<a id="interpreter-jdbc--apache-phoenix"></a>

### Apache Phoenix

Phoenix supports `thick` and `thin` connection types:

- [Thick client](#interpreter-jdbc--thick-client-connection) is faster, but must connect directly to ZooKeeper and HBase RegionServers.
- [Thin client](#interpreter-jdbc--thin-client-connection) has fewer dependencies and connects through a [Phoenix Query Server](http://phoenix.apache.org/server.html) instance.

Use the appropriate `default.driver`, `default.url`, and the dependency artifact for your connection type.

<a id="interpreter-jdbc--thick-client-connection"></a>

#### Thick client connection

![](assets/images/phoenix-thick-setting_edcb9cafac08b688.png)

<a id="interpreter-jdbc--properties-6"></a>

##### Properties

| Name | Value |
| --- | --- |
| default.driver | org.apache.phoenix.jdbc.PhoenixDriver |
| default.url | jdbc:phoenix:localhost:2181:/hbase-unsecure |
| default.user | phoenix\_user |
| default.password | phoenix\_password |

<a id="interpreter-jdbc--dependencies-5"></a>

##### Dependencies

| Artifact | Excludes |
| --- | --- |
| org.apache.phoenix:phoenix-core:4.4.0-HBase-1.0 |  |

[Maven Repository: org.apache.phoenix:phoenix-core](https://mvnrepository.com/artifact/org.apache.phoenix/phoenix-core)

<a id="interpreter-jdbc--thin-client-connection"></a>

#### Thin client connection

![](assets/images/phoenix-thin-setting_30263b407d1656c0.png)

<a id="interpreter-jdbc--properties-7"></a>

##### Properties

| Name | Value |
| --- | --- |
| default.driver | org.apache.phoenix.queryserver.client.Driver |
| default.url | jdbc:phoenix:thin:url=http://localhost:8765;serialization=PROTOBUF |
| default.user | phoenix\_user |
| default.password | phoenix\_password |

<a id="interpreter-jdbc--dependencies-6"></a>

##### Dependencies

Before Adding one of the below dependencies, check the Phoenix version first.

| Artifact | Excludes | Description |
| --- | --- | --- |
| org.apache.phoenix:phoenix-server-client:4.7.0-HBase-1.1 |  | For Phoenix `4.7` |
| org.apache.phoenix:phoenix-queryserver-client:4.8.0-HBase-1.2 |  | For Phoenix `4.8+` |

[Maven Repository: org.apache.phoenix:phoenix-queryserver-client](https://mvnrepository.com/artifact/org.apache.phoenix/phoenix-queryserver-client)

<a id="interpreter-jdbc--apache-tajo"></a>

### Apache Tajo

![](assets/images/tajo-setting_ea7d5169e7d98dc7.png)

<a id="interpreter-jdbc--properties-8"></a>

##### Properties

| Name | Value |
| --- | --- |
| default.driver | org.apache.tajo.jdbc.TajoDriver |
| default.url | jdbc:tajo://localhost:26002/default |

[Apache Tajo JDBC Driver Docs](https://tajo.apache.org/docs/current/jdbc_driver.html)

<a id="interpreter-jdbc--dependencies-7"></a>

##### Dependencies

| Artifact | Excludes |
| --- | --- |
| org.apache.tajo:tajo-jdbc:0.11.0 |  |

[Maven Repository: org.apache.tajo:tajo-jdbc](https://mvnrepository.com/artifact/org.apache.tajo/tajo-jdbc)

<a id="interpreter-jdbc--object-interpolation"></a>

## Object Interpolation

The JDBC interpreter also supports interpolation of `ZeppelinContext` objects into the paragraph text.
The following example shows one use of this facility:

<a id="interpreter-jdbc--in-scala-cell:"></a>

#### In Scala cell:

```scala
z.put("country_code", "KR")
    // ...
```

<a id="interpreter-jdbc--in-later-jdbc-cell:"></a>

#### In later JDBC cell:

```sql
%jdbc_interpreter_name

select * from patents_list where
priority_country = '{country_code}' and filing_date like '2015-%'
```

Object interpolation is disabled by default, and can be enabled for all instances of the JDBC interpreter by
setting the value of the property `zeppelin.jdbc.interpolation` to `true` (see *More Properties* above).
More details of this feature can be found in the Spark interpreter documentation under
[Zeppelin-Context](#usage-other_features-zeppelin_context)

<a id="interpreter-jdbc--bug-reporting"></a>

## Bug reporting

If you find a bug using JDBC interpreter, please create a [JIRA](https://issues.apache.org/jira/browse/ZEPPELIN) ticket.

---

---

<a id="interpreter-python"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/python.html -->

<!-- page_index: 56 -->

<a id="interpreter-python--python-2-3-interpreter-for-apache-zeppelin"></a>

# Python 2 & 3 Interpreter for Apache Zeppelin

<a id="interpreter-python--overview"></a>

## Overview

Zeppelin supports python language which is very popular in data analytics and machine learning.

| Name | Class | Description |
| --- | --- | --- |
| %python | PythonInterpreter | Vanilla python interpreter, with least dependencies, only python environment installed is required, `%python` will use IPython if its prerequisites are met |
| %python.ipython | IPythonInterpreter | Provide more fancy python runtime via IPython, almost the same experience like Jupyter. It requires more things, but is the recommended interpreter for using python in Zeppelin, see below for more details |
| %python.sql | PythonInterpreterPandasSql | Provide sql capability to query data in Pandas DataFrame via `pandasql`, it can access dataframes in `%python` |

<a id="interpreter-python--main-features"></a>

## Main Features

| Feature | Description |
| --- | --- |
| Support vanilla Python and IPython | Vanilla Python only requires python install, IPython provides almost the same user experience like Jupyter, like inline plotting, code completion, magic methods and etc. |
| Built-in ZeppelinContext Support | You can use ZeppelinContext to visualize pandas dataframe |
| Support SQL on Pandas dataframe | You can use Sql to query dataframe which is defined in Python |
| Run Python in yarn cluster with customized Python runtime | You can run Python in yarn cluster with customized Python runtime without affecting each other |

<a id="interpreter-python--play-python-in-zeppelin-docker"></a>

## Play Python in Zeppelin docker

For beginner, we would suggest you to play Python in Zeppelin docker first.
In the Zeppelin docker image, we have already installed
miniconda and lots of [useful python libraries](https://github.com/apache/zeppelin/blob/branch-0.10/scripts/docker/zeppelin/bin/env_python_3_with_R.yml)
including IPython's prerequisites, so `%python` would use IPython.

Without any extra configuration, you can run most of tutorial notes under folder `Python Tutorial` directly.

```bash
docker run -u $(id -u) -p 8080:8080 --rm --name zeppelin apache/zeppelin:0.10.0
```

After running the above command, you can open `http://localhost:8080` to play Python in Zeppelin.

<a id="interpreter-python--configuration"></a>

## Configuration

| Property | Default | Description |
| --- | --- | --- |
| zeppelin.python | python | Path of the installed Python binary (could be python2 or python3). You should set this property explicitly if python is not in your `$PATH`(example: /usr/bin/python). |
| zeppelin.python.maxResult | 1000 | Max number of dataframe rows to display. |
| zeppelin.python.useIPython | true | When this property is true, `%python` would be delegated to `%python.ipython` if IPython is available, otherwise IPython is only used in `%python.ipython`. |
| zeppelin.yarn.dist.archives |  | Used for ipython in yarn mode. It is a general zeppelin interpreter configuration, not python specific. For Python interpreter it is used to specify the conda env archive file which could be on local filesystem or on hadoop compatible file system. |
| zeppelin.interpreter.conda.env.name |  | Used for ipython in yarn mode. conda environment name, aka the folder name in the working directory of interpreter yarn container. |

<a id="interpreter-python--vanilla-python-interpreter-python"></a>

## Vanilla Python Interpreter (`%python`)

The vanilla python interpreter provides basic python interpreter feature, only python installed is required.

<a id="interpreter-python--matplotlib-integration"></a>

### Matplotlib integration

The vanilla python interpreter can display matplotlib figures inline automatically using the `matplotlib`:

```python
%python

import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

The output of this command will by default be converted to HTML by implicitly making use of the `%html` magic. Additional configuration can be achieved using the builtin `z.configure_mpl()` method. For example,

```python

z.configure_mpl(width=400, height=300, fmt='svg')
plt.plot([1, 2, 3])
```

Will produce a 400x300 image in SVG format, which by default are normally 600x400 and PNG respectively.
In the future, another option called `angular` can be used to make it possible to update a plot produced from one paragraph directly from another
(the output will be `%angular` instead of `%html`). However, this feature is already available in the `pyspark` interpreter.
More details can be found in the included "Zeppelin Tutorial: Python - matplotlib basic" tutorial notebook.

If Zeppelin cannot find the matplotlib backend files (which should usually be found in `$ZEPPELIN_HOME/interpreter/lib/python`) in your `PYTHONPATH`, then the backend will automatically be set to agg, and the (otherwise deprecated) instructions below can be used for more limited inline plotting.

If you are unable to load the inline backend, use `z.show(plt)`:

```python
%python

import matplotlib.pyplot as plt
plt.figure()
(.. ..)
z.show(plt)
plt.close()
```

The `z.show()` function can take optional parameters to adapt graph dimensions (width and height) as well as output format (png or optionally svg).

```python
%python

z.show(plt, width='50px')
z.show(plt, height='150px', fmt='svg')
```

![](assets/images/pythonmatplotlib_89e3f71cdc8c8414.png)

<a id="interpreter-python--ipython-interpreter-python.ipython-recommended"></a>

## IPython Interpreter (`%python.ipython`) (recommended)

IPython is more powerful than the vanilla python interpreter with extra functionality. This is what we recommend you to use instead of vanilla python interpreter. You can use IPython with Python2 or Python3 which depends on which python you set in `zeppelin.python`.

<a id="interpreter-python--prerequisites"></a>

### Prerequisites

- For non-anaconda environment, You need to install the following packages

```
pip install jupyter
pip install grpcio
pip install protobuf
```

- For anaconda environment (`zeppelin.python` points to the python under anaconda)

```
pip install grpcio
pip install protobuf
```

Zeppelin will check the above prerequisites when using `%python`, if IPython prerequisites are met, `%python` would use IPython interpreter, otherwise it would use vanilla Python interpreter in `%python`.

In addition to all the basic functions of the vanilla python interpreter, you can use all the IPython advanced features as you use it in Jupyter Notebook.
Take a look at tutorial note `Python Tutorial/1. IPython Basic` and `Python Tutorial/2. IPython Visualization Tutorial` for how to use IPython in Zeppelin.

<a id="interpreter-python--use-ipython-magic"></a>

### Use IPython magic

```
%python.ipython

#python help
range?

#timeit
%timeit range(100)
```

<a id="interpreter-python--use-matplotlib"></a>

### Use matplotlib

```
%python.ipython

%matplotlib inline
import matplotlib.pyplot as plt

print("hello world")
data=[1,2,3,4]
plt.figure()
plt.plot(data)
```

<a id="interpreter-python--run-shell-command"></a>

### Run shell command

```
%python.ipython

!pip install pandas
```

<a id="interpreter-python--colored-text-output"></a>

### Colored text output

![](assets/images/ipython-error_d9abfc6208c54df2.png)

<a id="interpreter-python--more-types-of-visualization"></a>

### More types of visualization

e.g. You can use hvplot in the same way as in Jupyter, Take a look at tutorial note `Python Tutorial/2. IPython Visualization Tutorial` for more visualization examples.

![](assets/images/ipython-hvplot_82dba46fe4353818.png)

<a id="interpreter-python--better-code-completion"></a>

### Better code completion

Type `tab` can give you all the completion candidates just like in Jupyter.

![](assets/images/ipython-code-completion_d76f19481e9f5c1b.png)

<a id="interpreter-python--pandas-integration"></a>

## Pandas Integration

Apache Zeppelin [Table Display System](#usage-display_system-basic--table) provides built-in data visualization capabilities.
Python interpreter leverages it to visualize Pandas DataFrames via `z.show()` API.

For example:

![](assets/images/python-zshow-df_a49cbec87894d867.png)

By default, `z.show` only display 1000 rows, you can configure `zeppelin.python.maxResult` to adjust the max number of rows.

<a id="interpreter-python--sql-over-pandas-dataframes"></a>

## SQL over Pandas DataFrames

There is a convenience `%python.sql` interpreter that matches Apache Spark experience in Zeppelin and
enables usage of SQL language to query [Pandas DataFrames](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) and
visualization of results through built-in [Table Display System](#usage-display_system-basic--table).
`%python.sql` can access dataframes defined in `%python`.

**Prerequisites**

- Pandas `pip install pandas`
- PandaSQL `pip install -U pandasql`

Here's one example:

- first paragraph

```python
%python
import pandas as pd
rates = pd.read_csv("bank.csv", sep=";")
```

- next paragraph

```sql
%python.sql
SELECT * FROM rates WHERE age < 40
```

![](assets/images/python-pandas-sql_df399e25f3a4197b.png)

<a id="interpreter-python--using-zeppelin-dynamic-forms"></a>

## Using Zeppelin Dynamic Forms

You can leverage [Zeppelin Dynamic Form](#usage-dynamic_form-intro) inside your Python code.

Example :

```python
%python

### Input form
print(z.input("f1","defaultValue"))

### Select form
print(z.select("f2",[("o1","1"),("o2","2")],"o1"))

### Checkbox form
print("".join(z.checkbox("f3", [("o1","1"), ("o2","2")],["o1"])))
```

<a id="interpreter-python--zeppelincontext-api"></a>

## ZeppelinContext API

Python interpreter create a variable `z` which represent `ZeppelinContext` for you. User can use it to do more fancy and complex things in Zeppelin.

| API | Description |
| --- | --- |
| z.put(key, value) | Put object `value` with identifier `key` to distributed resource pool of Zeppelin, so that it can be used by other interpreters |
| z.get(key) | Get object with identifier `key` from distributed resource pool of Zeppelin |
| z.remove(key) | Remove object with identifier `key` from distributed resource pool of Zeppelin |
| z.getAsDataFrame(key) | Get object with identifier `key` from distributed resource pool of Zeppelin and converted into pandas dataframe. The object in the distributed resource pool must be table type, e.g. jdbc interpreter result. |
| z.angular(name, noteId = None, paragraphId = None) | Get the angular object with identifier `name` |
| z.angularBind(name, value, noteId = None, paragraphId = None) | Bind value to angular object with identifier `name` |
| z.angularUnbind(name, noteId = None) | Unbind value from angular object with identifier `name` |
| z.show(p) | Show python object `p` in Zeppelin, if it is pandas dataframe, it would be displayed in Zeppelin's table format, others will be converted to string |
| z.textbox(name, defaultValue="") | Create dynamic form Textbox `name` with defaultValue |
| z.select(name, options, defaultValue="") | Create dynamic form Select `name` with options and defaultValue. options should be a list of Tuple(first element is key, the second element is the displayed value) e.g. `z.select("f2",[("o1","1"),("o2","2")],"o1")` |
| z.checkbox(name, options, defaultChecked=[]) | Create dynamic form Checkbox `name` with options and defaultChecked. options should be a list of Tuple(first element is key, the second element is the displayed value) e.g. `z.checkbox("f3", [("o1","1"), ("o2","2")],["o1"])` |
| z.noteTextbox(name, defaultValue="") | Create note level dynamic form Textbox |
| z.noteSelect(name, options, defaultValue="") | Create note level dynamic form Select |
| z.noteCheckbox(name, options, defaultChecked=[]) | Create note level dynamic form Checkbox |
| z.run(paragraphId) | Run paragraph |
| z.run(noteId, paragraphId) | Run paragraph |
| z.runNote(noteId) | Run the whole note |

<a id="interpreter-python--run-python-interpreter-in-yarn-cluster"></a>

## Run Python interpreter in yarn cluster

Zeppelin supports to [run interpreter in yarn cluster](#quickstart-yarn) which means the python interpreter can run in a yarn container.
This can achieve better multi-tenant for python interpreter especially when you already have a hadoop yarn cluster.

But there's one critical problem to run python in yarn cluster: how to manage the python environment in yarn container. Because hadoop yarn cluster is a distributed cluster environment
which is composed of many nodes, and your python interpreter can start in any node. It is not practical to manage python environment in each node beforehand.

So in order to run python in yarn cluster, we would suggest you to use conda to manage your python environment, and Zeppelin can ship your
conda environment to yarn container, so that each python interpreter can have its own python environment without affecting each other.

Python interpreter in yarn cluster only works for IPython, so make sure IPython's prerequisites are met. So make sure including the following packages in Step 1.

- python
- jupyter
- grpcio
- protobuf

<a id="interpreter-python--step-1"></a>

### Step 1

We would suggest you to use [conda-pack](https://conda.github.io/conda-pack/) to create archive of conda environment, and ship it to yarn container. Otherwise python interpreter
will use the python executable file in PATH of yarn container.

Here's one example of yaml file which could be used to create a conda environment with python 3 and some useful python libraries.

- Create yaml file for conda environment, write the following content into file `python_3_env.yml`

```text
name: python_3_env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - jupyter
  - grpcio
  - protobuf
  - pycodestyle
  - numpy
  - pandas
  - scipy
  - pandasql
  - panel
  - pyyaml
  - seaborn
  - plotnine
  - hvplot
  - intake
  - intake-parquet
  - intake-xarray
  - altair
  - vega_datasets
  - pyarrow
```

- Create conda environment via this yml file using either [conda](https://docs.conda.io/en/latest/) or [mamba](https://github.com/mamba-org/mamba)

```bash

conda env create -f python_3_env.yml
```

```bash

mamba env create -f python_3_env
```

- Pack the conda environment using `conda`

```bash

conda pack -n python_3_env
```

<a id="interpreter-python--step-2"></a>

### Step 2

Specify the following properties to enable yarn mode for python interpreter.

```
%python.conf

zeppelin.interpreter.launcher yarn
zeppelin.yarn.dist.archives /home/hadoop/python_3_env.tar.gz#environment
zeppelin.interpreter.conda.env.name environment
```

Setting `zeppelin.interpreter.launcher` as `yarn` will launch python interpreter in yarn cluster.

`zeppelin.yarn.dist.archives` is the python conda environment tar which is created in step 1.
This tar will be shipped to yarn container and untar in the working directory of yarn container.
`environment` in `/home/hadoop/python_3.tar.gz#environment` is the folder name after untar.

This folder name should be the same as `zeppelin.interpreter.conda.env.name`. Usually we name it as `environment` here.

<a id="interpreter-python--python-environments-used-for-vanilla-python-interpreter-in-non-yarn-mode"></a>

## Python environments (used for vanilla python interpreter in non-yarn mode)

<a id="interpreter-python--default"></a>

### Default

By default, PythonInterpreter will use python command defined in `zeppelin.python` property to run python process.
The interpreter can use all modules already installed (with pip, easy\_install...)

<a id="interpreter-python--conda"></a>

### Conda

[Conda](http://conda.pydata.org/) is an package management system and environment management system for python.
`%python.conda` interpreter lets you change between environments.

<a id="interpreter-python--usage"></a>

#### Usage

- get the Conda Information:


```
%python.conda info
```

- list the Conda environments:


```
%python.conda env list
```

- create a conda enviornment:


```
%python.conda create --name [ENV NAME]
```

- activate an environment (python interpreter will be restarted):


```
%python.conda activate [ENV NAME]
```

- deactivate


```
%python.conda deactivate
```

- get installed package list inside the current environment


```
%python.conda list
```

- install package


```
%python.conda install [PACKAGE NAME]
```

- uninstall package


```
%python.conda uninstall [PACKAGE NAME]
```

<a id="interpreter-python--docker"></a>

### Docker

`%python.docker` interpreter allows PythonInterpreter creates python process in a specified docker container.

<a id="interpreter-python--usage-2"></a>

#### Usage

- activate an environment


```
%python.docker activate [Repository]
%python.docker activate [Repository:Tag]
%python.docker activate [Image Id]
```

- deactivate


```
%python.docker deactivate
```

Here is an example

```
# activate latest tensorflow image as a python environment %python.docker activate gcr.io/tensorflow/tensorflow:latest
```

<a id="interpreter-python--community"></a>

## Community

[Join our community](http://zeppelin.apache.org/community.html) to discuss with others.

---

---

<a id="interpreter-r"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/r.html -->

<!-- page_index: 57 -->

<a id="interpreter-r--r-interpreter-for-apache-zeppelin"></a>

# R Interpreter for Apache Zeppelin

<a id="interpreter-r--overview"></a>

## Overview

[R](https://www.r-project.org) is a free software environment for statistical computing and graphics.

To run R code and visualize plots in Apache Zeppelin, you will need R on your zeppelin server node (or your dev laptop).

- For Centos: `yum install R R-devel libcurl-devel openssl-devel`
- For Ubuntu: `apt-get install r-base`

Validate your installation with a simple R command:

```
R -e "print(1+1)"
```

To enjoy plots, install additional libraries with:

- devtools with

```bash
  R -e "install.packages('devtools', repos = 'http://cran.us.r-project.org')"
```

- knitr with

```bash
  R -e "install.packages('knitr', repos = 'http://cran.us.r-project.org')"
```

- ggplot2 with

```bash
  R -e "install.packages('ggplot2', repos = 'http://cran.us.r-project.org')"
```

- Other visualization libraries:

```bash
  R -e "install.packages(c('devtools','mplot', 'googleVis'), repos = 'http://cran.us.r-project.org');
  require(devtools); install_github('ramnathv/rCharts')"
```

We recommend you to also install the following optional R libraries for happy data analytics:

- glmnet
- pROC
- data.table
- caret
- sqldf
- wordcloud

<a id="interpreter-r--supported-interpreters"></a>

## Supported Interpreters

Zeppelin supports R language in 3 interpreters

| Name | Class | Description |
| --- | --- | --- |
| %r.r | RInterpreter | Vanilla r interpreter, with least dependencies, only R environment and knitr are required. It is always recommended to use the fully qualified interpreter name `%r.r`, because `%r` is ambiguous, it could mean `%spark.r` when current note's default interpreter is `%spark` and `%r.r` when the default interpreter is `%r` |
| %r.ir | IRInterpreter | Provide more fancy R runtime via [IRKernel](https://github.com/IRkernel/IRkernel), almost the same experience like using R in Jupyter. It requires more things, but is the recommended interpreter for using R in Zeppelin. |
| %r.shiny | ShinyInterpreter | Run Shiny app in Zeppelin |

If you want to use R with Spark, it is almost the same via `%spark.r`, `%spark.ir` & `%spark.shiny` . You can refer Spark interpreter docs for more details.

<a id="interpreter-r--configuration"></a>

## Configuration

| Property | Default | Description |
| --- | --- | --- |
| zeppelin.R.cmd | R | Path of the installed R binary. You should set this property explicitly if R is not in your `$PATH`(example: /usr/bin/R). |
| zeppelin.R.knitr | true | Whether to use knitr or not. It is recommended to install [knitr](https://yihui.org/knitr/) |
| zeppelin.R.image.width | 100% | Image width of R plotting |
| zeppelin.R.shiny.iframe\_width | 100% | IFrame width of Shiny App |
| zeppelin.R.shiny.iframe\_height | 500px | IFrame height of Shiny App |
| zeppelin.R.shiny.portRange | : | Shiny app would launch a web app at some port, this property is to specify the portRange via format 'start':'end', e.g. '5000:5001'. By default it is ':' which means any port. |
| zeppelin.R.maxResult | 1000 | Max number of dataframe rows to display when using z.show |

<a id="interpreter-r--play-r-in-zeppelin-docker"></a>

## Play R in Zeppelin docker

For beginner, we would suggest you to play R in Zeppelin docker first. In the Zeppelin docker image, we have already installed R and lots of useful R libraries including IRKernel's prerequisites, so `%r.ir` is available.

Without any extra configuration, you can run most of tutorial notes under folder `R Tutorial` directly.

```
docker run -u $(id -u) -p 8080:8080 -p:6789:6789 --rm --name zeppelin apache/zeppelin:0.10.0
```

After running the above command, you can open `http://localhost:8080` to play R in Zeppelin.
The port `6789` exposed in the above command is for R shiny app. You need to make the following 2 interpreter properties to enable shiny app accessible as iframe in Zeppelin docker container.

- `zeppelin.R.shiny.portRange` to be `6789:6789`
- Set `ZEPPELIN_LOCAL_IP` to be `0.0.0.0`

![](assets/images/r-shiny-app_856da94cfecb57fb.gif)

<a id="interpreter-r--interpreter-binding-mode"></a>

## Interpreter binding mode

The default [interpreter binding mode](#usage-interpreter-interpreter_binding_mode) is `globally shared`. That means all notes share the same R interpreter.
So we would recommend you to ues `isolated per note` which means each note has own R interpreter without affecting each other. But it may run out of your machine resource if too many R
interpreters are created. You can [run R in yarn mode](#interpreter-r--run-r-in-yarn-cluster) to avoid this problem.

<a id="interpreter-r--how-to-use-r-interpreter"></a>

## How to use R Interpreter

There are two different implementations of R interpreters: `%r.r` and `%r.ir`.

- Vanilla R Interpreter(`%r.r`) behaves like an ordinary REPL and use SparkR to communicate between R process and JVM process. It requires `knitr` to be installed.
- IRKernel R Interpreter(`%r.ir`) behaves like using IRKernel in Jupyter notebook. It is based on [jupyter interpreter](#interpreter-jupyter). Besides jupyter interpreter's prerequisites, [IRkernel](https://github.com/IRkernel/IRkernel) needs to be installed as well.

Take a look at the tutorial note `R Tutorial/1. R Basics` for how to write R code in Zeppelin.

<a id="interpreter-r--r-basic-expressions"></a>

### R basic expressions

R basic expressions are supported in both `%r.r` and `%r.ir`.

![](assets/images/r-basic_d4ddbb38021f9dd5.png)

<a id="interpreter-r--r-base-plotting"></a>

### R base plotting

R base plotting is supported in both `%r.r` and `%r.ir`.

![](assets/images/r-plotting_c8401e7f07cae7a0.png)

<a id="interpreter-r--other-plotting"></a>

### Other plotting

Besides R base plotting, you can use other visualization libraries in both `%r.r` and `%r.ir`, e.g. `ggplot` and `googleVis`

![](assets/images/r-ggplot_4782f21b49c49e98.png)

![](assets/images/r-googlevis_e751be428a8a0e75.png)

<a id="interpreter-r--z.show"></a>

### z.show

`z.show()` is only available in `%r.ir` to visualize R dataframe, e.g.

![](assets/images/r-zshow_84279651e70b35d0.png)

By default, `z.show` would only display 1000 rows, you can specify the maxRows via `z.show(df, maxRows=2000)`

<a id="interpreter-r--make-shiny-app-in-zeppelin"></a>

## Make Shiny App in Zeppelin

[Shiny](https://shiny.rstudio.com/tutorial/) is an R package that makes it easy to build interactive web applications (apps) straight from R.
`%r.shiny` is used for developing R shiny app in Zeppelin notebook. It only works when IRKernel Interpreter(`%r.ir`) is enabled.
For developing one Shiny App in Zeppelin, you need to write at least 3 paragraphs (server type paragraph, ui type paragraph and run type paragraph)

- Server type R shiny paragraph

```r

%r.shiny(type=server)

# Define server logic to summarize and view selected dataset ----
server <- function(input, output) {

    # Return the requested dataset ----
    datasetInput <- reactive({
        switch(input$dataset,
        "rock" = rock,
        "pressure" = pressure,
        "cars" = cars)
    })

    # Generate a summary of the dataset ----
    output$summary <- renderPrint({
        dataset <- datasetInput()
        summary(dataset)
    })

    # Show the first "n" observations ----
    output$view <- renderTable({
        head(datasetInput(), n = input$obs)
    })
}
```

- UI type R shiny paragraph

```r
%r.shiny(type=ui)

# Define UI for dataset viewer app ----
ui <- fluidPage(

    # App title ----
    titlePanel("Shiny Text"),

    # Sidebar layout with a input and output definitions ----
    sidebarLayout(

        # Sidebar panel for inputs ----
        sidebarPanel(

        # Input: Selector for choosing dataset ----
        selectInput(inputId = "dataset",
        label = "Choose a dataset:",
        choices = c("rock", "pressure", "cars")),

        # Input: Numeric entry for number of obs to view ----
        numericInput(inputId = "obs",
        label = "Number of observations to view:",
        value = 10)
        ),

        # Main panel for displaying outputs ----
        mainPanel(

        # Output: Verbatim text for data summary ----
        verbatimTextOutput("summary"),

        # Output: HTML table with requested number of observations ----
        tableOutput("view")

        )
    )
)
```

- Run type R shiny paragraph

```r

%r.shiny(type=run)
```

After executing the run type R shiny paragraph, the shiny app will be launched and embedded as iframe in paragraph.
Take a look at the tutorial note `R Tutorial/2. Shiny App` for how to develop R shiny app.

![](assets/images/r-shiny_0b153a33ceca6b58.png)

<a id="interpreter-r--run-multiple-shiny-apps"></a>

### Run multiple shiny apps

If you want to run multiple shiny apps, you can specify `app` in paragraph local property to differentiate different shiny apps.

e.g.

```r
%r.shiny(type=ui, app=app_1)
```

```r
%r.shiny(type=server, app=app_1)
```

```r
%r.shiny(type=run, app=app_1)
```

<a id="interpreter-r--run-r-in-yarn-cluster"></a>

## Run R in yarn cluster

Zeppelin support to [run interpreter in yarn cluster](#quickstart-yarn). But there's one critical problem to run R in yarn cluster: how to manage the R environment in yarn container.
Because yarn cluster is a distributed cluster which is composed of many nodes, and your R interpreter can start in any node.
It is not practical to manage R environment in each node.

So in order to run R in yarn cluster, we would suggest you to use conda to manage your R environment, and Zeppelin can ship your
R conda environment to yarn container, so that each R interpreter can have its own R environment without affecting each other.

To be noticed, you can only run IRKernel interpreter(`%r.ir`) in yarn cluster. So make sure you include at least the following prerequisites in the below conda env:

- python
- jupyter
- grpcio
- protobuf
- r-base
- r-essentials
- r-irkernel

`python`, `jupyter`, `grpcio` and `protobuf` are required for [jupyter interpreter](#interpreter-jupyter), because IRKernel interpreter is based on [jupyter interpreter](#interpreter-jupyter). Others are for R runtime.

Following are instructions of how to run R in yarn cluster. You can find all the code in the tutorial note `R Tutorial/3. R Conda Env in Yarn Mode`.

<a id="interpreter-r--step-1"></a>

### Step 1

We would suggest you to use conda pack to create archive of conda environment.

Here's one example of yaml file which is used to generate a conda environment with R and some useful R libraries.

- Create a yaml file for conda environment, write the following content into file `r_env.yml`

```text
name: r_env
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - jupyter
  - grpcio
  - protobuf
  - r-base=3
  - r-essentials
  - r-evaluate
  - r-base64enc
  - r-knitr
  - r-ggplot2
  - r-irkernel
  - r-shiny
  - r-googlevis
```

- Create conda environment via this yaml file using either `conda` or `mamba`

```bash

conda env create -f r_env.yml
```

```bash

mamba env create -f r_env.yml
```

- Pack the conda environment using `conda`

```bash

conda pack -n r_env
```

<a id="interpreter-r--step-2"></a>

### Step 2

Specify the following properties to enable yarn mode for R interpreter via [inline configuration](#usage-interpreter-overview--inline-generic-configuration)

```
%r.conf

zeppelin.interpreter.launcher yarn
zeppelin.yarn.dist.archives hdfs:///tmp/r_env.tar.gz#environment
zeppelin.interpreter.conda.env.name environment
```

`zeppelin.yarn.dist.archives` is the R conda environment tar file which is created in step 1. This tar will be shipped to yarn container and untar in the working directory of yarn container.
`hdfs:///tmp/r_env.tar.gz` is the R conda archive file you created in step 2. `environment` in `hdfs:///tmp/r_env.tar.gz#environment` is the folder name after untar.
This folder name should be the same as `zeppelin.interpreter.conda.env.name`.

<a id="interpreter-r--step-3"></a>

### Step 3

Now you can use run R interpreter in yarn container and also use any R libraries you specify in step 1.

---

---

<a id="interpreter-alluxio"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/alluxio.html -->

<!-- page_index: 58 -->

<a id="interpreter-alluxio--alluxio-interpreter-for-apache-zeppelin"></a>

# Alluxio Interpreter for Apache Zeppelin

<a id="interpreter-alluxio--overview"></a>

## Overview

[Alluxio](http://alluxio.org/) is a memory-centric distributed storage system enabling reliable data sharing at memory-speed across cluster frameworks.

<a id="interpreter-alluxio--configuration"></a>

## Configuration

| Name | Class | Description |
| --- | --- | --- |
| alluxio.master.hostname | localhost | Alluxio master hostname |
| alluxio.master.port | 19998 | Alluxio master port |

<a id="interpreter-alluxio--enabling-alluxio-interpreter"></a>

## Enabling Alluxio Interpreter

In a notebook, to enable the **Alluxio** interpreter, click on the **Gear** icon and select **Alluxio**.

<a id="interpreter-alluxio--using-the-alluxio-interpreter"></a>

## Using the Alluxio Interpreter

In a paragraph, use `%alluxio` to select the **Alluxio** interpreter and then input all commands.

```bash
%alluxio
help
```

> **Tip :** Use ( Ctrl + . ) for autocompletion.

<a id="interpreter-alluxio--interpreter-commands"></a>

## Interpreter Commands

The **Alluxio** interpreter accepts the following commands.

| Operation | Syntax | Description |
| --- | --- | --- |
| cat | cat "path" | Print the content of the file to the console. |
| chgrp | chgrp "group" "path" | Change the group of the directory or file. |
| chmod | chmod "permission" "path" | Change the permission of the directory or file. |
| chown | chown "owner" "path" | Change the owner of the directory or file. |
| copyFromLocal | copyFromLocal "source path" "remote path" | Copy the specified file specified by "source path" to the path specified by "remote path". This command will fail if "remote path" already exists. |
| copyToLocal | copyToLocal "remote path" "local path" | Copy the specified file from the path specified by "remote path" to a local destination. |
| count | count "path" | Display the number of folders and files matching the specified prefix in "path". |
| du | du "path" | Display the size of a file or a directory specified by the input path. |
| fileInfo | fileInfo "path" | Print the information of the blocks of a specified file. |
| free | free "path" | Free a file or all files under a directory from Alluxio. If the file/directory is also in under storage, it will still be available there. |
| getCapacityBytes | getCapacityBytes | Get the capacity of the AlluxioFS. |
| getUsedBytes | getUsedBytes | Get number of bytes used in the AlluxioFS. |
| load | load "path" | Load the data of a file or a directory from under storage into Alluxio. |
| loadMetadata | loadMetadata "path" | Load the metadata of a file or a directory from under storage into Alluxio. |
| location | location "path" | Display a list of hosts that have the file data. |
| ls | ls "path" | List all the files and directories directly under the given path with information such as size. |
| mkdir | mkdir "path1" ... "pathn" | Create directory(ies) under the given paths, along with any necessary parent directories. Multiple paths separated by spaces or tabs. This command will fail if any of the given paths already exist. |
| mount | mount "path" "uri" | Mount the underlying file system path "uri" into the Alluxio namespace as "path". The "path" is assumed not to exist and is created by the operation. No data or metadata is loaded from under storage into Alluxio. After a path is mounted, operations on objects under the mounted path are mirror to the mounted under storage. |
| mv | mv "source" "destination" | Move a file or directory specified by "source" to a new location "destination". This command will fail if "destination" already exists. |
| persist | persist "path" | Persist a file or directory currently stored only in Alluxio to the underlying file system. |
| pin | pin "path" | Pin the given file to avoid evicting it from memory. If the given path is a directory, it recursively pins all the files contained and any new files created within this directory. |
| report | report "path" | Report to the master that a file is lost. |
| rm | rm "path" | Remove a file. This command will fail if the given path is a directory rather than a file. |
| setTtl | setTtl "time" | Set the TTL (time to live) in milliseconds to a file. |
| tail | tail "path" | Print the last 1KB of the specified file to the console. |
| touch | touch "path" | Create a 0-byte file at the specified location. |
| unmount | unmount "path" | Unmount the underlying file system path mounted in the Alluxio namespace as "path". Alluxio objects under "path" are removed from Alluxio, but they still exist in the previously mounted under storage. |
| unpin | unpin "path" | Unpin the given file to allow Alluxio to evict this file again. If the given path is a directory, it recursively unpins all files contained and any new files created within this directory. |
| unsetTtl | unsetTtl | Remove the TTL (time to live) setting from a file. |

<a id="interpreter-alluxio--how-to-test-it-s-working"></a>

## How to test it's working

Be sure to have configured correctly the Alluxio interpreter, then open a new paragraph and type one of the above commands.

Below a simple example to show how to interact with Alluxio interpreter.
Following steps are performed:

- using sh interpreter a new text file is created on local machine
- using Alluxio interpreter:
  - is listed the content of the afs (Alluxio File System) root
  - the file previously created is copied to afs
  - is listed again the content of the afs root to check the existence of the new copied file
  - is showed the content of the copied file (using the tail command)
  - the file previously copied to afs is copied to local machine
- using sh interpreter it's checked the existence of the new file copied from Alluxio and its content is showed

![Alluxio Interpreter Example](/docs/0.12.0/assets/themes/zeppelin/img/docs-img/alluxio-example.png)

---

---

<a id="interpreter-bigquery"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/bigquery.html -->

<!-- page_index: 59 -->

<a id="interpreter-bigquery--bigquery-interpreter-for-apache-zeppelin"></a>

# BigQuery Interpreter for Apache Zeppelin

<a id="interpreter-bigquery--overview"></a>

## Overview

[BigQuery](https://cloud.google.com/bigquery/what-is-bigquery) is a highly scalable no-ops data warehouse in the Google Cloud Platform. Querying massive datasets can be time consuming and expensive without the right hardware and infrastructure. Google BigQuery solves this problem by enabling super-fast SQL queries against append-only tables using the processing power of Google's infrastructure. Simply move your data into BigQuery and let us handle the hard work. You can control access to both the project and your data based on your business needs, such as giving others the ability to view or query your data.

<a id="interpreter-bigquery--configuration"></a>

## Configuration

| Name | Default Value | Description |
| --- | --- | --- |
| zeppelin.bigquery.project\_id |  | Google Project Id |
| zeppelin.bigquery.wait\_time | 5000 | Query Timeout in Milliseconds |
| zeppelin.bigquery.max\_no\_of\_rows | 100000 | Max result set size |
| zeppelin.bigquery.sql\_dialect |  | BigQuery SQL dialect (standardSQL or legacySQL). If empty, [query prefix](https://cloud.google.com/bigquery/docs/reference/standard-sql/enabling-standard-sql#sql-prefix) like '#standardSQL' can be used. |
| zeppelin.bigquery.region |  | BigQuery dataset region (Needed for single region dataset) |

<a id="interpreter-bigquery--bigquery-api"></a>

## BigQuery API

Zeppelin is built against BigQuery API version v2-rev265-1.21.0 - [API Javadocs](https://developers.google.com/resources/api-libraries/documentation/bigquery/v2/java/latest/)

<a id="interpreter-bigquery--enabling-the-bigquery-interpreter"></a>

## Enabling the BigQuery Interpreter

In a notebook, to enable the **BigQuery** interpreter, click the **Gear** icon and select **bigquery**.

<a id="interpreter-bigquery--provide-application-default-credentials"></a>

### Provide Application Default Credentials

Within Google Cloud Platform (e.g. Google App Engine, Google Compute Engine), built-in credentials are used by default.

Outside of GCP, follow the Google API authentication instructions for [Zeppelin Google Cloud Storage](https://zeppelin.apache.org/docs/latest/setup/storage/storage.html#notebook-storage-in-google-cloud-storage)

<a id="interpreter-bigquery--using-the-bigquery-interpreter"></a>

## Using the BigQuery Interpreter

In a paragraph, use `%bigquery.sql` to select the **BigQuery** interpreter and then input SQL statements against your datasets stored in BigQuery.
You can use [BigQuery SQL Reference](https://cloud.google.com/bigquery/query-reference) to build your own SQL.

For Example, SQL to query for top 10 departure delays across airports using the flights public dataset

```bash
%bigquery.sql
SELECT departure_airport,count(case when departure_delay>0 then 1 else 0 end) as no_of_delays
FROM [bigquery-samples:airline_ontime_data.flights]
group by departure_airport
order by 2 desc
limit 10
```

Another Example, SQL to query for most commonly used java packages from the github data hosted in BigQuery

```bash
%bigquery.sql
SELECT
  package,
  COUNT(*) count
FROM (
  SELECT
    REGEXP_EXTRACT(line, r' ([a-z0-9\._]*)\.') package,
    id
  FROM (
    SELECT
      SPLIT(content, '\n') line,
      id
    FROM
      [bigquery-public-data:github_repos.sample_contents]
    WHERE
      content CONTAINS 'import'
      AND sample_path LIKE '%.java'
    HAVING
      LEFT(line, 6)='import' )
  GROUP BY
    package,
    id )
GROUP BY
  1
ORDER BY
  count DESC
LIMIT
  40
```

<a id="interpreter-bigquery--technical-description"></a>

## Technical description

For in-depth technical details on current implementation please refer to [bigquery/README.md](https://github.com/apache/zeppelin/blob/master/bigquery/README.md).

---

---

<a id="interpreter-cassandra"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/cassandra.html -->

<!-- page_index: 60 -->

<a id="interpreter-cassandra--cassandra-cql-interpreter-for-apache-zeppelin"></a>

# Cassandra CQL Interpreter for Apache Zeppelin

| Name | Class | Description |
| --- | --- | --- |
| %cassandra | CassandraInterpreter | Provides interpreter for Apache Cassandra CQL query language |

<a id="interpreter-cassandra--enabling-cassandra-interpreter"></a>

## Enabling Cassandra Interpreter

In a notebook, to enable the **Cassandra** interpreter, click on the **Gear** icon and select **Cassandra**

![Interpreter Binding](assets/images/cassandra-interpreterbinding_2b45ca726f972a29.png)

![Interpreter Selection](assets/images/cassandra-interpreterselection_794bf18dff28c0cd.png)

<a id="interpreter-cassandra--using-the-cassandra-interpreter"></a>

## Using the Cassandra Interpreter

In a paragraph, use ***%cassandra*** to select the **Cassandra** interpreter and then input all commands.

To access the interactive help, type **HELP;**

![Interactive Help](assets/images/cassandra-interactivehelp_42a93c45ca48154c.png)

<a id="interpreter-cassandra--interpreter-commands"></a>

## Interpreter Commands

The **Cassandra** interpreter accepts the following commands

| Command Type | Command Name | Description |
| --- | --- | --- |
| Help command | `HELP` | Display the interactive help menu |
| Schema commands | `DESCRIBE KEYSPACE`, `DESCRIBE CLUSTER`, `DESCRIBE TABLES` ... | Custom commands to describe the Cassandra schema |
| Option commands | `@consistency`, `@fetchSize` ... | Inject runtime options to all statements in the paragraph |
| Prepared statement commands | `@prepare`, `@bind`, `@remove\_prepared` | Let you register a prepared command and re-use it later by injecting bound values |
| Native CQL statements | All CQL-compatible statements (`SELECT`, `INSERT`, `CREATE`, ...) | All CQL statements are executed directly against the Cassandra server |

<a id="interpreter-cassandra--cql-statements"></a>

## CQL statements

This interpreter is compatible with any CQL statement supported by Cassandra. Ex:

```sql

INSERT INTO users(login,name) VALUES('jdoe','John DOE');
SELECT * FROM users WHERE login='jdoe';
```

Each statement should be separated by a semi-colon ( **;** ) except the special commands below:

1. `@prepare`
2. `@bind`
3. `@remove_prepare`
4. `@consistency`
5. `@serialConsistency`
6. `@timestamp`
7. `@fetchSize`
8. `@requestTimeOut`

Multi-line statements as well as multiple statements on the same line are also supported as long as they are separated by a semi-colon. Ex:

```sql

USE spark_demo;

SELECT * FROM albums_by_country LIMIT 1; SELECT * FROM countries LIMIT 1;

SELECT *
FROM artists
WHERE login='jlennon';
```

Batch statements are supported and can span multiple lines, as well as DDL (`CREATE`/`ALTER`/`DROP`) statements:

```sql

BEGIN BATCH
    INSERT INTO users(login,name) VALUES('jdoe','John DOE');
    INSERT INTO users_preferences(login,account_type) VALUES('jdoe','BASIC');
APPLY BATCH;

CREATE TABLE IF NOT EXISTS test(
    key int PRIMARY KEY,
    value text
);
```

CQL statements are **case-insensitive** (except for column names and values). This means that the following statements are equivalent and valid:

```sql

INSERT INTO users(login,name) VALUES('jdoe','John DOE');
Insert into users(login,name) vAlues('hsue','Helen SUE');
```

The complete list of all CQL statements and versions can be found below:

| Cassandra Version | Documentation Link |
| --- | --- |
| **3.x** | <https://docs.datastax.com/en/archived/cql/3.3/cql/cqlIntro.html> |
| **2.2** | <https://docs.datastax.com/en/archived/cql/3.3/cql/cqlIntro.html> |
| **2.1** | <http://docs.datastax.com/en/cql/3.1/cql/cql_intro_c.html> |

<a id="interpreter-cassandra--comments-in-statements"></a>

## Comments in statements

It is possible to add comments between statements. Single line comments start with the **hash sign** (`#`), **double slashes** (`//`), **double dash** (`--`). Multi-line comments are enclosed between `/**` and `**/`. Ex:

```sql
# Single line comment style 1 INSERT INTO users(login,name) VALUES('jdoe','John DOE');
// Single line comment style 2
// Single line comment style 3
/** Multi line comments **/ Insert into users(login,name) vAlues('hsue','Helen SUE');
```

<a id="interpreter-cassandra--syntax-validation"></a>

## Syntax Validation

The interpreters is shipped with a built-in syntax validator. This validator only checks for basic syntax errors.

All CQL-related syntax validation is delegated directly to **Cassandra**

Most of the time, syntax errors are due to **missing semi-colons** between statements or **typo errors**.

<a id="interpreter-cassandra--schema-commands"></a>

## Schema commands

To make schema discovery easier and more interactive, the following commands are supported:

| Command | Description |
| --- | --- |
| **DESCRIBE CLUSTER;** | Show the current cluster name and its partitioner |
| **DESCRIBE KEYSPACES;** | List all existing keyspaces in the cluster and their configuration (replication factor, durable write ...) |
| **DESCRIBE TABLES;** | List all existing keyspaces in the cluster and for each, all the tables name |
| **DESCRIBE TYPES;** | List all existing keyspaces in the cluster and for each, all the user-defined types name |
| **DESCRIBE FUNCTIONS;** | List all existing keyspaces in the cluster and for each, all the functions name |
| **DESCRIBE AGGREGATES;** | List all existing keyspaces in the cluster and for each, all the aggregates name |
| **DESCRIBE MATERIALIZED VIEWS;** | List all existing keyspaces in the cluster and for each, all the materialized views name |
| **DESCRIBE KEYSPACE <keyspace\_name>;** | Describe the given keyspace configuration and all its table details (name, columns, ...) |
| **DESCRIBE TABLE (<keyspace\_name>).<table\_name>;** | Describe the given table. If the keyspace is not provided, the current logged in keyspace is used. If there is no logged in keyspace, the default system keyspace is used. If no table is found, an error message is raised |
| **DESCRIBE TYPE (<keyspace\_name>).<type\_name>;** | Describe the given type(UDT). If the keyspace is not provided, the current logged in keyspace is used. If there is no logged in keyspace, the default system keyspace is used. If no type is found, an error message is raised |
| **DESCRIBE FUNCTION (<keyspace\_name>).<function\_name>;** | Describe the given function. If the keyspace is not provided, the current logged in keyspace is used. If there is no logged in keyspace, the default system keyspace is used. If no function is found, an error message is raised |
| **DESCRIBE AGGREGATE (<keyspace\_name>).<aggregate\_name>;** | Describe the given aggregate. If the keyspace is not provided, the current logged in keyspace is used. If there is no logged in keyspace, the default system keyspace is used. If no aggregate is found, an error message is raised |
| **DESCRIBE MATERIALIZED VIEW (<keyspace\_name>).<view\_name>;** | Describe the given view. If the keyspace is not provided, the current logged in keyspace is used. If there is no logged in keyspace, the default system keyspace is used. If no view is found, an error message is raised |

The schema objects (cluster, keyspace, table, type, function and aggregate) are displayed in a tabular format.
There is a drop-down menu on the top left corner to expand objects details. On the top right menu is shown the Icon legend.

![Describe Schema](/docs/0.12.0/assets/themes/zeppelin/img/docs-img/cassandra-DescribeSchema.png)
<a id="interpreter-cassandra--runtime-execution-parameters"></a>

## Runtime Execution Parameters

Sometimes you want to be able to pass runtime query parameters to your statements.

Those parameters are not part of the CQL specs and are specific to the interpreter.

Below is the list of all parameters:

| Parameter | Syntax | Description |
| --- | --- | --- |
| Consistency Level | **@consistency=*value*** | Apply the given consistency level to all queries in the paragraph |
| Serial Consistency Level | **@serialConsistency=*value*** | Apply the given serial consistency level to all queries in the paragraph |
| Timestamp | **@timestamp=*long value*** | Apply the given timestamp to all queries in the paragraph. Please note that timestamp value passed directly in CQL statement will override this value |
| Fetch Size | **@fetchSize=*integer value*** | Apply the given fetch size to all queries in the paragraph |
| Request Time Out | **@requestTimeOut=*integer value*** | Apply the given request timeout **in millisecs** to all queries in the paragraph |

Some parameters only accept restricted values:

| Parameter | Possible Values |
| --- | --- |
| Consistency Level | **ALL, ANY, ONE, TWO, THREE, QUORUM, LOCAL\_ONE, LOCAL\_QUORUM, EACH\_QUORUM** |
| Serial Consistency Level | **SERIAL, LOCAL\_SERIAL** |
| Timestamp | Any long value |
| Fetch Size | Any integer value |

> Please note that you should **not** add semi-colon ( **;** ) at the end of each parameter statement

Some examples:

```sql

CREATE TABLE IF NOT EXISTS spark_demo.ts(
    key int PRIMARY KEY,
    value text
);
TRUNCATE spark_demo.ts;

// Timestamp in the past
@timestamp=10

// Force timestamp directly in the first insert
INSERT INTO spark_demo.ts(key,value) VALUES(1,'first insert') USING TIMESTAMP 100;

// Select some data to make the clock turn
SELECT * FROM spark_demo.albums LIMIT 100;

// Now insert using the timestamp parameter set at the beginning(10)
INSERT INTO spark_demo.ts(key,value) VALUES(1,'second insert');

// Check for the result. You should see 'first insert'
SELECT value FROM spark_demo.ts WHERE key=1;
```

Some remarks about query parameters:

> 1. **many** query parameters can be set in the same paragraph
> 2. if the **same** query parameter is set many time with different values, the interpreter only take into account the first value
> 3. each query parameter applies to **all CQL statements** in the same paragraph, unless you override the option using plain CQL text (like forcing timestamp with the `USING` clause)
> 4. the order of each query parameter with regard to CQL statement does not matter

<a id="interpreter-cassandra--runtime-formatting-parameters"></a>

## Runtime Formatting Parameters

Sometimes you want to be able to format output of your statement. Cassandra interpreter allows to specify different parameters as local properties of the paragraph. Below is the list of all formatting parameters:

| Parameter | Syntax | Description |
| --- | --- | --- |
| Output Format | **outputFormat=*value*** | Controls, should we output data as CQL literals, or in human-readable form. Possible values: **cql, human** (default: **human** |
| Locale | **locale=*value*** | Locale for formatting of numbers & time-related values. Could be any locale supported by JVM (default: **en\_US**) |
| Timezone | **timezone=*value*** | Timezone for formatting of time-related values. Could be any timezone supported by JVM (default: **UTC**) |
| Float precision | **floatPrecision=*value*** | Precision when formatting float values. Any positive integer value, or `-1` to show everything |
| Double precision | **doublePrecision=*value*** | Precision when formatting double values. Any positive integer value, or `-1` to show everything |
| Decimal precision | **decimalPrecision=*value*** | Precision when formatting decimal values. Any positive integer value, or `-1` to show everything |
| Timestamp Format | **timestampFormat=*value*** | Format string for timestamp values. Should be valid [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) pattern |
| Time Format | **timeFormat=*value*** | Format string for time values. Should be valid [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) pattern |
| Date Format | **dateFormat=*value*** | Format string for date values. Should be valid [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) pattern |

Some examples:

```sql
create table if not exists zep.test_format (
  id int primary key,
  text text,
  date date,
  timestamp timestamp,
  time time,
  double double,
  float float
);

insert into zep.test_format(id, text, date, timestamp, time, double, float)
  values (1, 'text', '2019-01-29', '2020-06-16T23:59:59.123Z', '04:05:00.234',
  10.0153423453425634653463466346543, 20.0303443);
```

```
%cassandra(outputFormat=human, locale=de_DE, floatPrecision=2, doublePrecision=4, timeFormat=hh:mma, timestampFormat=MM/dd/yy HH:mm, dateFormat="E, d MMM yy", timezone=Etc/GMT+2)
select id, double, float, text, date, time, timestamp from zep.test_format;
```

will output data formatted according to settings, including German locale:

```
id  double   float  text  date           time     timestamp
1   10,0153  20,03  text  Di, 29 Jan 19  04:05AM  06/16/20 21:59
```

while with `outputFormat=cql`, data is formatted as CQL literals:

```
id double              float       text    date        time                  timestamp
1  10.015342345342564  20.030344  'text'  '2019-01-29' '04:05:00.234000000'  '2020-06-17T01:59:59.123+02:00'
```

<a id="interpreter-cassandra--support-for-prepared-statements"></a>

## Support for Prepared Statements

For performance reason, it is better to prepare statements before-hand and reuse them later by providing bound values.

This interpreter provides 3 commands to handle prepared and bound statements:

1. **@prepare**
2. **@bind**
3. **@remove\_prepared**

Example:

```
@prepare[statement-name]=...

@bind[statement-name]=’text’, 1223, ’2015-07-30 12:00:01’, null, true, [‘list_item1’, ’list_item2’]

@bind[statement-name-with-no-bound-value]

@remove_prepare[statement-name]
```

<a id="interpreter-cassandra--prepare"></a>

#### @prepare

You can use the syntax *"@prepare[statement-name]=SELECT..."* to create a prepared statement.
The *statement-name* is **mandatory** because the interpreter prepares the given statement with the Java driver and
saves the generated prepared statement in an **internal hash map**, using the provided *statement-name* as search key.

> Please note that this internal prepared statement map is shared with **all notebooks** and **all paragraphs** because
> there is only one instance of the interpreter for Cassandra
>
> If the interpreter encounters **many** `@prepare` for the **same *statement-name* (key)**, only the **first** statement will be taken into account.

Example:

```
@prepare[select]=SELECT * FROM spark_demo.albums LIMIT ?

@prepare[select]=SELECT * FROM spark_demo.artists LIMIT ?
```

For the above example, the prepared statement is `SELECT * FROM spark_demo.albums LIMIT ?`.
`SELECT * FROM spark_demo.artists LIMIT ?` is ignored because an entry already exists in the prepared statements map with the key *select*.

In the context of **Zeppelin**, a notebook can be scheduled to be executed at regular interval, thus it is necessary to **avoid re-preparing many time the same statement (considered an anti-pattern)**.

<a id="interpreter-cassandra--bind"></a>

#### @bind

Once the statement is prepared (possibly in a separated notebook/paragraph). You can bind values to it:

```
@bind[select_first]=10
```

Bound values are not mandatory for the **@bind** statement. However if you provide bound values, they need to comply to some syntax:

- String values should be enclosed between simple quotes (**'**)
- Date values should be enclosed between simple quotes (**'**) and respect the formats (full list is in the [documentation](https://docs.datastax.com/en/cql/3.3/cql/cql_reference/timestamp_type_r.html)):
  1. yyyy-MM-dd HH:MM:ss
  2. yyyy-MM-dd HH:MM:ss.SSS
  3. yyyy-mm-dd'T'HH:mm:ss.SSSZ
- **null** is parsed as-is
- **boolean** (`true`|`false`) are parsed as-is
- collection values must follow the **[standard CQL syntax](http://docs.datastax.com/en/cql/3.1/cql/cql_using/use_collections_c.html)**:
  - list: ['list*item1', 'list*item2', ...]
  - set: {'set*item1', 'set*item2', …}
  - map: {'key1': 'val1', 'key2': 'val2', …}
- **tuple** values should be enclosed between parenthesis (see **[Tuple CQL syntax](http://docs.datastax.com/en/cql/3.1/cql/cql_reference/tupleType.html)**): ('text', 123, true)
- **udt** values should be enclosed between brackets (see **[UDT CQL syntax](http://docs.datastax.com/en/cql/3.1/cql/cql_using/cqlUseUDT.html)**): {stree*name: 'Beverly Hills', number: 104, zip*code: 90020, state: 'California', …}

> It is possible to use the @bind statement inside a batch:
>
>
```sql
BEGIN BATCH
   @bind[insert_user]='jdoe','John DOE'
   UPDATE users SET age = 27 WHERE login='hsue';
APPLY BATCH;
```

<a id="interpreter-cassandra--remove_prepare"></a>

#### @remove\_prepare

To avoid for a prepared statement to stay forever in the prepared statement map, you can use the
**@remove\_prepare[statement-name]** syntax to remove it.
Removing a non-existing prepared statement yields no error.

<a id="interpreter-cassandra--using-dynamic-forms"></a>

## Using Dynamic Forms

Instead of hard-coding your CQL queries, it is possible to use **[Zeppelin dynamic form]** syntax to inject simple value or multiple choices forms.

The legacy mustache syntax ( **{{ }}** ) to bind input text and select form is still supported but is deprecated and will be removed in future releases.

> **Legacy**
> The syntax for simple parameter is: **{{input\_Label=default value}}**. The default value is mandatory because the first time the paragraph is executed,
> we launch the CQL query before rendering the form so at least one value should be provided.
>
> The syntax for multiple choices parameter is: **{{input\_Label=value1 | value2 | … | valueN }}**. By default the first choice is used for CQL query
> the first time the paragraph is executed.

Example:

```
#Secondary index on performer style
SELECT name, country, performer
FROM spark_demo.performers
WHERE name='${performer=Sheryl Crow|Doof|Fanfarlo|Los Paranoia}'
AND styles CONTAINS '${style=Rock}';
```

In the above example, the first CQL query will be executed for `performer='Sheryl Crow' AND style='Rock'`.
For subsequent queries, you can change the value directly using the form.

> Please note that we enclosed the **${ }** block between simple quotes ( **'** ) because Cassandra expects a String here.
> We could have also use the **${style='Rock'}** syntax but this time, the value displayed on the form is ***'Rock'*** and not ***Rock***.

It is also possible to use dynamic forms for **prepared statements**:

```
@bind[select]=='${performer=Sheryl Crow|Doof|Fanfarlo|Los Paranoia}', '${style=Rock}'
```

<a id="interpreter-cassandra--shared-states"></a>

## Shared states

It is possible to execute many paragraphs in parallel. However, at the back-end side, we're still using synchronous queries.
*Asynchronous execution* is only possible when it is possible to return a `Future` value in the `InterpreterResult`.
It may be an interesting proposal for the **Zeppelin** project.

Recently, **Zeppelin** allows you to choose the level of isolation for your interpreters (see **[Interpreter Binding Mode]** ).

Long story short, you have 3 available bindings:

- **shared** : *same JVM* and *same Interpreter instance* for all notes
- **scoped** : *same JVM* but *different Interpreter instances*, one for each note
- **isolated**: *different JVM* running a *single Interpreter instance*, one JVM for each note

Using the **shared** binding, the same `com.datastax.driver.core.Session` object is used for **all** notes and paragraphs.
Consequently, if you use the `USE keyspace_name;` statement to log into a keyspace, it will change the keyspace for
**all current users** of the **Cassandra** interpreter because we only create 1 `com.datastax.driver.core.Session` object
per instance of **Cassandra** interpreter.

The same remark does apply to the **prepared statement hash map**, it is shared by **all users** using the same instance of **Cassandra** interpreter.

When using **scoped** binding, in the *same JVM* **Zeppelin** will create multiple instances of the Cassandra interpreter, thus
multiple `com.datastax.driver.core.Session` objects. **Beware of resource and memory usage using this binding !**

The **isolated** mode is the most extreme and will create as many JVM/`com.datastax.driver.core.Session` object as there are distinct notes.

<a id="interpreter-cassandra--interpreter-configuration"></a>

## Interpreter Configuration

To configure the **Cassandra** interpreter, go to the **Interpreter** menu and scroll down to change the parameters.
The **Cassandra** interpreter is using the official **[Datastax Java Driver for Apache Cassandra](https://docs.datastax.com/en/developer/java-driver/latest/)®** and most of the parameters are used to configure the Java driver

Below are the configuration parameters supported by interpreter and their default values.

| Property Name | Description | Default Value |
| --- | --- | --- |
| `cassandra.cluster` | Name of the Cassandra cluster to connect to | Test Cluster |
| `cassandra.compression.protocol` | On wire compression. Possible values are: `NONE`, `SNAPPY`, `LZ4` | `NONE` |
| `cassandra.credentials.username` | If security is enable, provide the login | none |
| `cassandra.credentials.password` | If security is enable, provide the password | none |
| `cassandra.hosts` | Comma separated Cassandra hosts (DNS name or IP address). Ex: `192.168.0.12,node2,node3` | `localhost` |
| `cassandra.interpreter.parallelism` | Number of concurrent paragraphs(queries block) that can be executed | 10 |
| `cassandra.keyspace` | Default keyspace to connect to. **It is strongly recommended to let the default value and prefix the table name with the actual keyspace in all of your queries** | `system` |
| `cassandra.load.balancing.policy` | Load balancing policy. Default = `DefaultLoadBalancingPolicy` To Specify your own policy, provide the *fully qualify class name (FQCN)* of your policy. At runtime the driver will instantiate the policy using class name. | DEFAULT |
| `cassandra.max.schema.agreement.wait.second` | Cassandra max schema agreement wait in second | 10 |
| `cassandra.pooling.connection.per.host.local` | Protocol V3 and above default = 1 | 1 |
| `cassandra.pooling.connection.per.host.remote` | Protocol V3 and above default = 1 | 1 |
| `cassandra.pooling.heartbeat.interval.seconds` | Cassandra pool heartbeat interval in secs | 30 |
| `cassandra.pooling.max.request.per.connection` | Protocol V3 and above default = 1024 | 1024 |
| `cassandra.pooling.pool.timeout.millisecs` | Cassandra pool time out in millisecs | 5000 |
| `cassandra.protocol.version` | Cassandra binary protocol version (`V3`, `V4`, ...) | `DEFAULT` (detected automatically) |
| cassandra.query.default.consistency | Cassandra query default consistency level Available values: `ONE`, `TWO`, `THREE`, `QUORUM`, `LOCAL_ONE`, `LOCAL_QUORUM`, `EACH_QUORUM`, `ALL` | `ONE` |
| `cassandra.query.default.fetchSize` | Cassandra query default fetch size | 5000 |
| `cassandra.query.default.serial.consistency` | Cassandra query default serial consistency level Available values: `SERIAL`, `LOCAL_SERIAL` | `SERIAL` |
| `cassandra.reconnection.policy` | Cassandra Reconnection Policy. Default = `ExponentialReconnectionPolicy` To Specify your own policy, provide the *fully qualify class name (FQCN)* of your policy. At runtime the driver will instantiate the policy using class name. | DEFAULT |
| `cassandra.retry.policy` | Cassandra Retry Policy. Default = `DefaultRetryPolicy` To Specify your own policy, provide the *fully qualify class name (FQCN)* of your policy. At runtime the driver will instantiate the policy using class name. | DEFAULT |
| `cassandra.socket.connection.timeout.millisecs` | Cassandra socket default connection timeout in millisecs | 500 |
| `cassandra.socket.read.timeout.millisecs` | Cassandra socket read timeout in millisecs | 12000 |
| `cassandra.socket.tcp.no_delay` | Cassandra socket TCP no delay | true |
| `cassandra.speculative.execution.policy` | Cassandra Speculative Execution Policy. Default = `NoSpeculativeExecutionPolicy` To Specify your own policy, provide the *fully qualify class name (FQCN)* of your policy. At runtime the driver will instantiate the policy using class name. | DEFAULT |
| `cassandra.ssl.enabled` | Enable support for connecting to the Cassandra configured with SSL. To connect to Cassandra configured with SSL use **true** and provide a truststore file and password with following options. | false |
| `cassandra.ssl.truststore.path` | Filepath for the truststore file to use for connection to Cassandra with SSL. |  |
| `cassandra.ssl.truststore.password` | Password for the truststore file to use for connection to Cassandra with SSL. |  |
| `cassandra.format.output` | Output format for data - strict CQL (`cql`), or human-readable (`human`) | `human` |
| `cassandra.format.locale` | Which locale to use for output (any locale supported by JVM could be specified) | `en_US` |
| `cassandra.format.timezone` | For which timezone format time/date-related types (any timezone supported by JVM could be specified) | `UTC` |
| `cassandra.format.timestamp` | Format string for `timestamp` columns (any valid [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) pattern could be used) | `yyyy-MM-dd'T'HH:mm:ss.SSSXXX` |
| `cassandra.format.time` | Format string for `time` columns (any valid [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) pattern could be used) | `HH:mm:ss.SSS` |
| `cassandra.format.date` | Format string for `date` columns (any valid [DateTimeFormatter](https://docs.oracle.com/javase/8/docs/api/java/time/format/DateTimeFormatter.html) pattern could be used) | `yyyy-MM-dd` |
| `cassandra.format.float_precision` | Precision when formatting values of `float` type | `5` |
| `cassandra.format.double_precision` | Precision when formatting values of `double` type | `12` |
| `cassandra.format.decimal_precision` | Precision when formatting values of `decimal` type | `-1` (show everything) |

Besides these parameters, it's also possible to set other driver parameters by adding them into interpreter configuration. The configuration key should have full form with `datastax-java-driver` prefix, as [described in documentation](https://docs.datastax.com/en/developer/java-driver/latest/manual/core/configuration/). For example, to specify 5 seconds request timeout, you can use `datastax-java-driver.basic.request.timeout` with value of `5 seconds`. Full list of available configuration options is [available in documentation](https://docs.datastax.com/en/developer/java-driver/latest/manual/core/configuration/reference/). Additional options may override the options that are specified by the interpreter's configuration parameters.

<a id="interpreter-cassandra--change-log"></a>

## Change Log

**4.0** *(Zeppelin 0.12.0)* :

- Refactor to use unified Java driver 4.7 ([ZEPPELIN-4378](https://issues.apache.org/jira/browse/ZEPPELIN-4378):
  - changes in configuration were necessary, as new driver has different architecture, and configuration options
  - interpreter got support for DSE-specific data types, and other extensions
  - support for `@retryPolicy` is removed, as only single retry policy is shipped with driver
  - allow to specify any configuration option of Java driver
  - dropped support for Cassandra 1.2 & 2.0, that isn't supported by driver anymore
- added support for formatting options, both interpreter & cell level

**3.1** *(Zeppelin 0.12.0)* :

- Upgrade Java driver to 3.7.2 ([ZEPPELIN-4331](https://issues.apache.org/jira/browse/ZEPPELIN-4331);

**3.0** *(Zeppelin 0.12.0)* :

- Update documentation
- Update interactive documentation
- Add support for binary protocol **V4**
- Implement new `@requestTimeOut` runtime option
- Upgrade Java driver version to **3.0.1**
- Allow interpreter to add dynamic forms programmatically when using FormType.SIMPLE
- Allow dynamic form using default Zeppelin syntax
- Fixing typo on FallThroughPolicy
- Look for data in AngularObjectRegistry before creating dynamic form
- Add missing support for `ALTER` statements

**2.0** *(Zeppelin 0.12.0)* :

- Update help menu and add changelog
- Add Support for **User Defined Functions**, **User Defined Aggregates** and **Materialized Views**
- Upgrade Java driver version to **3.0.0-rc1**

**1.0** *(Zeppelin 0.5.5-incubating)* :

- Initial version

<a id="interpreter-cassandra--bugs-contacts"></a>

## Bugs & Contacts

If you encounter a bug for this interpreter, please create a **[JIRA](https://issues.apache.org/jira/browse/ZEPPELIN)** ticket.

[Zeppelin Dynamic Form](#usage-dynamic_form-intro)
[Interpreter Binding Mode](#usage-interpreter-interpreter_binding_mode)

---

---

<a id="interpreter-elasticsearch"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/elasticsearch.html -->

<!-- page_index: 61 -->

<a id="interpreter-elasticsearch--elasticsearch-interpreter-for-apache-zeppelin"></a>

# Elasticsearch Interpreter for Apache Zeppelin

<a id="interpreter-elasticsearch--overview"></a>

## Overview

[Elasticsearch](https://www.elastic.co/products/elasticsearch) is a highly scalable open-source full-text search and analytics engine.
It allows you to store, search, and analyze big volumes of data quickly and in near real time.
It is generally used as the underlying engine/technology that powers applications that have complex search features and requirements.

<a id="interpreter-elasticsearch--configuration"></a>

## Configuration

| Property | Default | Description |
| --- | --- | --- |
| elasticsearch.cluster.name | elasticsearch | Cluster name |
| elasticsearch.host | localhost | Host of a node in the cluster |
| elasticsearch.port | 9300 | Connection port **( Important: it depends on the client type, transport or http)** |
| elasticsearch.client.type | transport | The type of client for Elasticsearch (transport or http)**( Important: the port depends on this value)** |
| elasticsearch.basicauth.username |  | Username for a basic authentication (http) |
| elasticsearch.basicauth.password |  | Password for a basic authentication (http) |
| elasticsearch.result.size | 10 | The size of the result set of a search query |

![Interpreter configuration](/docs/0.12.0/assets/themes/zeppelin/img/docs-img/elasticsearch-config.png)
> **Note #1 :** You can add more properties to configure the Elasticsearch client.
>
> **Note #2 :** If you use Shield, you can add a property named `shield.user` with a value containing the name and the password ( format: `username:password` ). For more details about Shield configuration, consult the [Shield reference guide](https://www.elastic.co/guide/en/shield/current/_using_elasticsearch_java_clients_with_shield.html). Do not forget, to copy the shield client jar in the interpreter directory (`ZEPPELIN_HOME/interpreters/elasticsearch`).

<a id="interpreter-elasticsearch--enabling-the-elasticsearch-interpreter"></a>

## Enabling the Elasticsearch Interpreter

In a notebook, to enable the **Elasticsearch** interpreter, click the **Gear** icon and select **Elasticsearch**.

<a id="interpreter-elasticsearch--using-the-elasticsearch-interpreter"></a>

## Using the Elasticsearch Interpreter

In a paragraph, use `%elasticsearch` to select the Elasticsearch interpreter and then input all commands.
To get the list of available commands, use `help`.

```bash
%elasticsearch
help

Elasticsearch interpreter:
General format: <command> /<indices>/<types>/<id> <option> <JSON>
  - indices: list of indices separated by commas (depends on the command)
  - types: list of document types separated by commas (depends on the command)
Commands:
  - search /indices/types <query>
    . indices and types can be omitted (at least, you have to provide '/')
    . a query is either a JSON-formatted query, nor a lucene query
  - size <value>
    . defines the size of the result set (default value is in the config)
    . if used, this command must be declared before a search command
  - count /indices/types <query>
    . same comments as for the search
  - get /index/type/id
  - delete /index/type/id
  - index /index/type/id <json-formatted document>
    . the id can be omitted, elasticsearch will generate one
```

> **Tip :** Use ( Ctrl + . ) for autocompletion.

<a id="interpreter-elasticsearch--get"></a>

### Get

With the `get` command, you can find a document by id. The result is a JSON document.

```bash
%elasticsearch
get /index/type/id
```

Example:
![Elasticsearch - Get](assets/images/elasticsearch-get_6bda2ed033942783.png)

<a id="interpreter-elasticsearch--search"></a>

### Search

With the `search` command, you can send a search query to Elasticsearch. There are two formats of query:

- You can provide a JSON-formatted query, that is exactly what you provide when you use the REST API of Elasticsearch.
  - See [Elasticsearch search API reference document](https://www.elastic.co/guide/en/elasticsearch/reference/current/search.html) for more details about the content of the search queries.
- You can also provide the content of a `query_string`.
  - This is a shortcut to a query like that: `{ "query": { "query_string": { "query": "__HERE YOUR QUERY__", "analyze_wildcard": true } } }`
  - See [Elasticsearch query string syntax](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-query-string-query.html#query-string-syntax) for more details about the content of such a query.

```bash
%elasticsearch
search /index1,index2,.../type1,type2,...  <JSON document containing the query or query_string elements>
```

If you want to modify the size of the result set, you can add a line that is setting the size, before your search command.

```bash
%elasticsearch
size 50
search /index1,index2,.../type1,type2,...  <JSON document containing the query or query_string elements>
```

> A search query can also contain [aggregations](https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html).
> If there is at least one aggregation, the result of the first aggregation is shown, otherwise, you get the search hits.

Examples:

- With a JSON query:

```bash
  %elasticsearch
  search / { "query": { "match_all": { } } }

  %elasticsearch
  search /logs { "query": { "query_string": { "query": "request.method:GET AND status:200" } } }

  %elasticsearch
  search /logs { "aggs": {
    "content_length_stats": {
      "extended_stats": {
        "field": "content_length"
      }
    }
  } }
```

- With query\_string elements:

```bash
  %elasticsearch
  search /logs request.method:GET AND status:200

  %elasticsearch
  search /logs (404 AND (POST OR DELETE))
```

>
> [!IMPORTANT]
> : a document in Elasticsearch is a JSON document, so it is hierarchical, not flat as a row in a SQL table.
> For the Elastic interpreter, the result of a search query is flattened.

Suppose we have a JSON document:

```
{"date": "2015-12-08T21:03:13.588Z","request": {"method": "GET","url": "/zeppelin/4cd001cd-c517-4fa9-b8e5-a06b8f4056c4","headers": [ "Accept: *.*", "Host: apache.org"] },"status": "403","content_length": 1234}
```

The data will be flattened like this:

| content\_length | date | request.headers[0] | request.headers[1] | request.method | request.url | status |
| --- | --- | --- | --- | --- | --- | --- |
| 1234 | 2015-12-08T21:03:13.588Z | Accept: \*.\* | Host: apache.org | GET | /zeppelin/4cd001cd-c517-4fa9-b8e5-a06b8f4056c4 | 403 |

Examples:

- With a table containing the results:
  ![Elasticsearch - Search - table](assets/images/elasticsearch-search-table_93fedfd70bd9b1b9.png)
- You can also use a predefined diagram:
  ![Elasticsearch - Search - diagram](assets/images/elasticsearch-search-pie_485df00ccf0400a3.png)
- With a JSON query:
  ![Elasticsearch - Search with query](assets/images/elasticsearch-search-json-query-table_ea1b54444771e043.png)
- With a JSON query containing a `fields` parameter (for filtering the fields in the response): in this case, all the fields values in the response are arrays, so, after flattening the result, the format of all the field names is `field_name[x]`
  ![Elasticsearch - Search with query and a fields param](assets/images/elasticsearch-query-with-fields-param_9ff05c72a2519c69.png)
- With a query string:
  ![Elasticsearch - Search with query string](assets/images/elasticsearch-query-string_340b90cc063b1cce.png)
- With a query containing a multi-value metric aggregation:
  ![Elasticsearch - Search with aggregation (multi-value metric)](assets/images/elasticsearch-agg-multi-value-metric_8791dddafbce50a3.png)
- With a query containing a multi-bucket aggregation:
  ![Elasticsearch - Search with aggregation (multi-bucket)](assets/images/elasticsearch-agg-multi-bucket-pie_b3fe92fb402d9d4c.png)

<a id="interpreter-elasticsearch--count"></a>

### Count

With the `count` command, you can count documents available in some indices and types. You can also provide a query.

```bash
%elasticsearch
count /index1,index2,.../type1,type2,... <JSON document containing the query OR a query string>
```

Examples:

- Without query:
  ![Elasticsearch - Count](assets/images/elasticsearch-count_86a9f7693ef4c31b.png)
- With a query:
  ![Elasticsearch - Count with query](assets/images/elasticsearch-count-with-query_835d04a8fc6d8f1c.png)

<a id="interpreter-elasticsearch--index"></a>

### Index

With the `index` command, you can insert/update a document in Elasticsearch.

```bash
%elasticsearch
index /index/type/id <JSON document>

%elasticsearch
index /index/type <JSON document>
```

<a id="interpreter-elasticsearch--delete"></a>

### Delete

With the `delete` command, you can delete a document.

```bash
%elasticsearch
delete /index/type/id
```

<a id="interpreter-elasticsearch--apply-zeppelin-dynamic-forms"></a>

### Apply Zeppelin Dynamic Forms

You can leverage [Zeppelin Dynamic Form](#usage-dynamic_form-intro) inside your queries. You can use both the `text input` and `select form` parameterization features.

```bash
%elasticsearch
size ${limit=10}
search /index/type { "query": { "match_all": { } } }
```

---

---

<a id="interpreter-groovy"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/groovy.html -->

<!-- page_index: 62 -->

<a id="interpreter-groovy--groovy-interpreter-for-apache-zeppelin"></a>

# Groovy Interpreter for Apache Zeppelin

<a id="interpreter-groovy--samples"></a>

### Samples

```groovy
%groovy
//get a parameter defined as z.angularBind('ngSearchParam', value, 'paragraph_id')
//g is a context object for groovy to avoid mix with z object
def param = g.angular('ngSearchParam')
//send request https://www.googleapis.com/customsearch/v1?q=ngSearchParam_value
def r = HTTP.get(
  //assume you defined the groovy interpreter property
  //   `search_baseurl`='https://www.googleapis.com/customsearch/v1'
  //in groovy object o.getProperty('A') == o.'A' == o.A == o['A']
  url : g.search_baseurl,
  query: [ q: param ],
  headers: [
    'Accept':'application/json',
    //'Authorization:' : g.getProperty('search_auth'),
  ],
  ssl : g.getProperty('search_ssl') // assume groovy interpreter property search_ssl = HTTP.getNaiveSSLContext()
)
//check response code
if( r.response.code==200 ) {
  g.html().with{
    //g.html() renders %angular to output and returns groovy.xml.MarkupBuilder
    h2("the response ${r.response.code}")
    span( r.response.body )
    h2("headers")
    pre( r.response.headers.join('\n') )
  }
} else {
  //just to show that it's possible to use println with multiline groovy string to render output
  println("""%angular
    <script> alert ("code=${r.response.code} \n msg=${r.response.message}") </script>
  """)
}
```

```groovy
%groovy
//renders a table with headers a, b, c  and two rows g.table([['a','b','c'],['a1','b1','c1'],['a2','b2','c2'],])
```

<a id="interpreter-groovy--the-g-object"></a>

### the `g` object

- `g.angular(String name)`

Returns angular object by name. Look up notebook scope first and then global scope.

- `g.angularBind(String name, Object value)`

Assign a new `value` into angular object `name`

- `java.util.Properties g.getProperties()`

returns all properties defined for this interpreter

- `String g.getProperty('PROPERTY_NAME')`

```groovy
   g.PROPERTY_NAME
   g.'PROPERTY_NAME'
   g['PROPERTY_NAME']
   g.getProperties().getProperty('PROPERTY_NAME')
```

All above the accessor to named property defined in groovy interpreter.
In this case with name `PROPERTY_NAME`

- `groovy.xml.MarkupBuilder g.html()`

Starts or continues rendering of `%angular` to output and returns [groovy.xml.MarkupBuilder](http://groovy-lang.org/processing-xml.html#_markupbuilder)
MarkupBuilder is usefull to generate html (xml)

- `void g.table(obj)`

starts or continues rendering table rows.

obj: List(rows) of List(columns) where first line is a header

- `g.input(name, value )`

Creates `text` input with value specified. The parameter `value` is optional.

- `g.select(name, default, Map<Object, String> options)`

Creates `select` input with defined options. The parameter `default` is optional.

`g.select('sex', 'm', ['m':'man', 'w':'woman'])`

- `g.checkbox(name, Collection checked, Map<Object, String> options)`

Creates `checkbox` input.

- `g.get(name, default)`

Returns interpreter-based variable. Visibility depends on interpreter scope. The parameter `default` is optional.

- `g.put(name, value)`

Stores new value into interpreter-based variable. Visibility depends on interpreter scope.

---

---

<a id="interpreter-hbase"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/hbase.html -->

<!-- page_index: 63 -->

<a id="interpreter-hbase--hbase-shell-interpreter-for-apache-zeppelin"></a>

# HBase Shell Interpreter for Apache Zeppelin

<a id="interpreter-hbase--overview"></a>

## Overview

[HBase Shell](http://hbase.apache.org/book.html#shell) is a JRuby IRB client for Apache HBase. This interpreter provides all capabilities of Apache HBase shell within Apache Zeppelin. The interpreter assumes that Apache HBase client software has been installed and it can connect to the Apache HBase cluster from the machine on where Apache Zeppelin is installed.
To get start with HBase, please see [HBase Quickstart](https://hbase.apache.org/book.html#quickstart).

<a id="interpreter-hbase--hbase-release-supported"></a>

## HBase release supported

By default, Zeppelin is built against HBase 1.0.x releases. To work with HBase 1.1.x releases, use the following build command:

```bash
# HBase 1.1.4./mvnw clean package -DskipTests -Phadoop-2.6 -Dhadoop.version=2.6.0 -P build-distr -Dhbase.hbase.version=1.1.4 -Dhbase.hadoop.version=2.6.0
```

To work with HBase 1.2.0+, use the following build command:

```bash
# HBase 1.2.0./mvnw clean package -DskipTests -Phadoop-2.6 -Dhadoop.version=2.6.0 -P build-distr -Dhbase.hbase.version=1.2.0 -Dhbase.hadoop.version=2.6.0
```

<a id="interpreter-hbase--configuration"></a>

## Configuration

| Property | Default | Description |
| --- | --- | --- |
| hbase.home | /usr/lib/hbase | Installation directory of HBase, defaults to HBASE\_HOME in environment |
| hbase.ruby.sources | lib/ruby | Path to Ruby scripts relative to 'hbase.home' |
| zeppelin.hbase.test.mode | false | Disable checks for unit and manual tests |

If you want to connect to HBase running on a cluster, you'll need to follow the next step.

<a id="interpreter-hbase--export-hbase_home"></a>

### Export HBASE\_HOME

In `conf/zeppelin-env.sh`, export `HBASE_HOME` environment variable with your HBase installation path. This ensures `hbase-site.xml` can be loaded.

For example

```bash
export HBASE_HOME=/usr/lib/hbase
```

or, when running with CDH

```bash
export HBASE_HOME="/opt/cloudera/parcels/CDH/lib/hbase"
```

You can optionally export `HBASE_CONF_DIR` instead of `HBASE_HOME` should you have custom HBase configurations.

<a id="interpreter-hbase--enabling-the-hbase-shell-interpreter"></a>

## Enabling the HBase Shell Interpreter

In a notebook, to enable the **HBase Shell** interpreter, click the **Gear** icon and select **HBase Shell**.

<a id="interpreter-hbase--using-the-hbase-shell-interpreter"></a>

## Using the HBase Shell Interpreter

In a paragraph, use `%hbase` to select the **HBase Shell** interpreter and then input all commands. To get the list of available commands, use `help`.

```bash
%hbase
help
```

For example, to create a table

```bash
%hbase
create 'test', 'cf'
```

And then to put data into that table

```bash
%hbase
put 'test', 'row1', 'cf:a', 'value1'
```

For more information on all commands available, refer to [HBase shell commands](https://learnhbase.wordpress.com/2013/03/02/hbase-shell-commands/).

---

---

<a id="interpreter-hdfs"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/hdfs.html -->

<!-- page_index: 64 -->

<a id="interpreter-hdfs--hdfs-file-system-interpreter-for-apache-zeppelin"></a>

# HDFS File System Interpreter for Apache Zeppelin

<a id="interpreter-hdfs--overview"></a>

## Overview

[Hadoop File System](http://hadoop.apache.org/) is a distributed, fault tolerant file system part of the hadoop project and is often used as storage for distributed processing engines like [Hadoop MapReduce](http://hadoop.apache.org/) and [Apache Spark](http://spark.apache.org/) or underlying file systems like [Alluxio](http://www.alluxio.org/).

<a id="interpreter-hdfs--configuration"></a>

## Configuration

| Property | Default | Description |
| --- | --- | --- |
| hdfs.url | http://localhost:50070/webhdfs/v1/ | The URL for WebHDFS |
| hdfs.user | hdfs | The WebHDFS user |
| hdfs.maxlength | 1000 | Maximum number of lines of results fetched |

This interpreter connects to HDFS using the HTTP WebHDFS interface.
It supports the basic shell file commands applied to HDFS, it currently only supports browsing.

- You can use *ls [PATH]* and *ls -l [PATH]* to list a directory. If the path is missing, then the current directory is listed. *ls*  supports a *-h* flag for human readable file sizes.
- You can use *cd [PATH]* to change your current directory by giving a relative or an absolute path.
- You can invoke *pwd* to see your current directory.

> **Tip :** Use ( Ctrl + . ) for autocompletion.

<a id="interpreter-hdfs--create-interpreter"></a>

## Create Interpreter

In a notebook, to enable the **HDFS** interpreter, click the **Gear** icon and select **HDFS**.

<a id="interpreter-hdfs--webhdfs-rest-api"></a>

## WebHDFS REST API

You can confirm that you're able to access the WebHDFS API by running a curl command against the WebHDFS end point provided to the interpreter.

Here is an example:

```bash
$> curl "http://localhost:50070/webhdfs/v1/?op=LISTSTATUS"
```

---

---

<a id="interpreter-hive"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/hive.html -->

<!-- page_index: 65 -->

<a id="interpreter-hive--hive-interpreter-for-apache-zeppelin"></a>

# Hive Interpreter for Apache Zeppelin

<a id="interpreter-hive--important-notice"></a>

## Important Notice

Hive Interpreter has been deprecated and merged into JDBC Interpreter.
You can use Hive Interpreter by using JDBC Interpreter with same functionality.
See the example below of settings and dependencies.

<a id="interpreter-hive--properties"></a>

### Properties

| Property | Value |
| --- | --- |
| default.driver | org.apache.hive.jdbc.HiveDriver |
| default.url | jdbc:hive2://localhost:10000 |
| default.user | hiveUser |
| default.password | hivePassword |

<a id="interpreter-hive--dependencies"></a>

### Dependencies

| Artifact | Exclude |
| --- | --- |
| org.apache.hive:hive-jdbc:0.14.0 |  |
| org.apache.hadoop:hadoop-common:2.6.0 |  |

<a id="interpreter-hive--configuration"></a>

### Configuration

| Property | Default | Description |
| --- | --- | --- |
| default.driver | org.apache.hive.jdbc.HiveDriver | Class path of JDBC driver |
| default.url | jdbc:hive2://localhost:10000 | Url for connection |
| default.user |  | **( Optional )** Username of the connection |
| default.password |  | **( Optional )** Password of the connection |
| default.xxx |  | **( Optional )** Other properties used by the driver |
| zeppelin.jdbc.hive.timeout.threshold | 60000 | Timeout for hive job timeout |
| zeppelin.jdbc.hive.monitor.query\_interval | 1000 | Query interval for hive statement |
| zeppelin.jdbc.hive.engines.tag.enable | true | Set application tag for applications started by hive engines |

<a id="interpreter-hive--overview"></a>

## Overview

The [Apache Hive](https://hive.apache.org/) ™ data warehouse software facilitates querying and managing large datasets
residing in distributed storage. Hive provides a mechanism to project structure onto
this data and query the data using a SQL-like language called HiveQL.
At the same time this language also allows traditional map/reduce programmers to
plug in their custom mappers and reducers when it is inconvenient or inefficient to express this logic in HiveQL.

<a id="interpreter-hive--how-to-use"></a>

## How to use

Basically, you can use

```sql
%hive
select * from my_table;
```

You can also run multiple queries up to 10 by default. Changing these settings is not implemented yet.

<a id="interpreter-hive--apply-zeppelin-dynamic-forms"></a>

### Apply Zeppelin Dynamic Forms

You can leverage [Zeppelin Dynamic Form](#usage-dynamic_form-intro) inside your queries.
You can use both the `text input` and `select form` parameterization features.

```sql
%hive
SELECT ${group_by}, count(*) as count
FROM retail_demo.order_lineitems_pxf
GROUP BY ${group_by=product_id,product_id|product_name|customer_id|store_id}
ORDER BY count ${order=DESC,DESC|ASC}
LIMIT ${limit=10};
```

---

---

<a id="interpreter-influxdb"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/influxdb.html -->

<!-- page_index: 66 -->

<a id="interpreter-influxdb--influxdb-interpreter-for-apache-zeppelin"></a>

# InfluxDB Interpreter for Apache Zeppelin

<a id="interpreter-influxdb--overview"></a>

## Overview

[InfluxDB](https://v2.docs.influxdata.com/v2.0/) is an open-source time series database (TSDB) developed by InfluxData. It is written in Go and optimized for fast, high-availability storage and retrieval of time series data in fields such as operations monitoring, application metrics, Internet of Things sensor data, and real-time analytics.
This interpreter allows to perform queries in [Flux Language](https://v2.docs.influxdata.com/v2.0/reference/flux/) in Zeppelin Notebook.

<a id="interpreter-influxdb--notes"></a>

### Notes

- This interpreter is compatible with InfluxDB 1.8+ and InfluxDB 2.0+ (v2 API, Flux language)
- Code complete and syntax highlighting is not supported for now

<a id="interpreter-influxdb--example-notebook"></a>

### Example notebook

![InfluxDB notebook](assets/images/influxdb1_0d0dd65cfcd95ad6.png)

<a id="interpreter-influxdb--configuration"></a>

### Configuration

| Property | Default | Value |
| --- | --- | --- |
| influxdb.url | http://localhost:9999 | InfluxDB API connection url |
| influxdb.org | my-org | organization name, Organizations are supported in InfluxDB 2.0+, use "-" as org for InfluxDB 1.8 |
| influxdb.token | my-token | authorization token for InfluxDB API, token are supported in InfluxDB 2.0+, for InfluxDB 1.8 use 'username:password' as a token. |
| influxdb.logLevel | NONE | InfluxDB client library verbosity level (for debugging purpose) |

<a id="interpreter-influxdb--example-configuration"></a>

#### Example configuration

![InfluxDB notebook](assets/images/influxdb2_5419b61598ca1518.png)

<a id="interpreter-influxdb--overview-2"></a>

## Overview

<a id="interpreter-influxdb--how-to-use"></a>

## How to use

Basically, you can use

```
%influxdb
from(bucket: "my-bucket")
  |> range(start: -1h)
  |> filter(fn: (r) => r._measurement == "cpu")
  |> filter(fn: (r) => r.cpu == "cpu-total")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
```

In this example we use data collected by `[[inputs.cpu]]` [Telegraf](https://github.com/influxdata/telegraf) input plugin.

The result of Flux command can contain more one or more tables. In the case of multiple tables, each
table is rendered as a separate %table structure. This example uses `pivot`
function to collect values from multiple tables into single table.

<a id="interpreter-influxdb--how-to-run-influxdb-2.0-using-docker"></a>

## How to run InfluxDB 2.0 using docker

```bash
docker pull quay.io/influxdb/influxdb:nightly
docker run --name influxdb -p 9999:9999 quay.io/influxdb/influxdb:nightly

## Post onBoarding request, to setup initial user (my-user@my-password), org (my-org) and bucketSetup (my-bucket)"
curl -i -X POST http://localhost:9999/api/v2/setup -H 'accept: application/json' \
    -d '{
            "username": "my-user",
            "password": "my-password",
            "org": "my-org",
            "bucket": "my-bucket",
            "token": "my-token"
        }'
```

---

---

<a id="interpreter-java"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/java.html -->

<!-- page_index: 67 -->

<a id="interpreter-java--java-interpreter-for-apache-zeppelin"></a>

# Java interpreter for Apache Zeppelin

<a id="interpreter-java--how-to-use"></a>

## How to use

Basically, you can write normal java code. You should write the main method inside a class because the interpreter invoke this main to execute the code. Unlike Zeppelin normal pattern, each paragraph is considered as a separate job, there isn't any relation to any other paragraph. For example, a variable defined in one paragraph cannot be used in another one as each paragraph is a self contained java main class that is executed and the output returned to Zeppelin.

The following is a demonstration of a word count example with data represented as a java Map and displayed leveraging Zeppelin's built in visualization using the utility method `JavaInterpreterUtils.displayTableFromSimpleMap`.

```java
%java
import java.util.HashMap;
import java.util.Map;
import org.apache.zeppelin.java.JavaInterpreterUtils;

public class HelloWorld {

    public static void main(String[] args) {

        Map<String, Long> counts = new HashMap<>();
        counts.put("hello",4L);
        counts.put("world",5L);

        System.out.println(JavaInterpreterUtils.displayTableFromSimpleMap("Word","Count", counts));

    }

}
```

---

---

<a id="interpreter-jupyter"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/jupyter.html -->

<!-- page_index: 68 -->

<a id="interpreter-jupyter--jupyter-interpreter-for-apache-zeppelin"></a>

# Jupyter Interpreter for Apache Zeppelin

<a id="interpreter-jupyter--overview"></a>

## Overview

Project [Jupyter](https://jupyter.org/) exists to develop open-source software, open-standards, and services for interactive computing across dozens of programming languages.
Zeppelin's Jupyter interpreter is a bridge/adapter between Zeppelin interpreter and Jupyter kernel. You can use any of jupyter kernel as long as you installed the necessary dependencies.

<a id="interpreter-jupyter--configuration"></a>

## Configuration

To run any Jupyter kernel in Zeppelin you first need to install the following prerequisite:

- pip install jupyter-client
- pip install grpcio
- pip install protobuf

Then you need install the jupyter kernel you want to use. In the following sections, we will talk about how to use the following 3 jupyter kernels in Zeppelin:

- ipython
- ir
- julia

<a id="interpreter-jupyter--jupyter-python-kernel"></a>

## Jupyter Python kernel

In order to use Jupyter Python kernel in Zeppelin, you need to install `ipykernel` first.

```bash

pip install ipykernel
```

Then you can run python code in Jupyter interpreter like following.

```python

%jupyter(kernel=python)

%matplotlib inline
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

![](assets/images/ipython-kernel_e180f145bfb5e7e8.png)

<a id="interpreter-jupyter--jupyter-r-kernel"></a>

## Jupyter R kernel

In order to use [IRKernel](https://github.com/IRkernel/IRkernel), you need to first install `IRkernel` package in R.

```r
install.packages('IRkernel')
IRkernel::installspec()  # to register the kernel in the current R installation
```

Then you can run r code in Jupyter interpreter like following.

```r
%jupyter(kernel=ir)

library(ggplot2)
ggplot(mpg, aes(x = displ, y = hwy)) +
  geom_point()
```

![](assets/images/ir-kernel_17b70d27bb52d82d.png)

<a id="interpreter-jupyter--jupyter-julia-kernel"></a>

## Jupyter Julia kernel

In order to use Julia in Zeppelin, you first need to install [IJulia](https://github.com/JuliaLang/IJulia.jl) first

```julia
using Pkg
Pkg.add("IJulia")
```

Then you can run julia code in Jupyter interpreter like following.

```julia

%jupyter(kernel=julia-1.3)

using Pkg
Pkg.add("Plots")
using Plots
plotly() # Choose the Plotly.jl backend for web interactivity
plot(rand(5,5),linewidth=2,title="My Plot")
Pkg.add("PyPlot") # Install a different backend
pyplot() # Switch to using the PyPlot.jl backend
plot(rand(5,5),linewidth=2,title="My Plot")
```

![](assets/images/julia-kernel_0ab173a26411e9b5.png)

<a id="interpreter-jupyter--use-any-other-kernel"></a>

## Use any other kernel

For any other jupyter kernel, you can follow the below steps to use it in Zeppelin.

1. Install the specified jupyter kernel. you can find all the available jupyter kernels [here](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels)
2. Find its kernel name by run the following command
   `bash
   jupyter kernelspec list`
3. Run the kernel as following

```python

%jupyter(kernel=kernel_name)

code
```

---

---

<a id="interpreter-livy"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/livy.html -->

<!-- page_index: 69 -->

<a id="interpreter-livy--livy-interpreter-for-apache-zeppelin"></a>

# Livy Interpreter for Apache Zeppelin

<a id="interpreter-livy--overview"></a>

## Overview

[Livy](http://livy.io/) is an open source REST interface for interacting with Spark from anywhere. It supports executing snippets of code or programs in a Spark context that runs locally or in YARN.

- Interactive Scala, Python and R shells
- Batch submissions in Scala, Java, Python
- Multi users can share the same server (impersonation support)
- Can be used for submitting jobs from anywhere with REST
- Does not require any code change to your programs

<a id="interpreter-livy--requirements"></a>

### Requirements

Additional requirements for the Livy interpreter are:

- Spark 1.3 or above.
- Livy server.

<a id="interpreter-livy--configuration"></a>

## Configuration

We added some common configurations for spark, and you can set any configuration you want.
You can find all Spark configurations in [here](http://spark.apache.org/docs/latest/configuration.html#available-properties).
And instead of starting property with `spark.` it should be replaced with `livy.spark.`.
Example: `spark.driver.memory` to `livy.spark.driver.memory`

| Property | Default | Description |
| --- | --- | --- |
| zeppelin.livy.url | http://localhost:8998 | URL where livy server is running |
| zeppelin.livy.spark.sql.maxResult | 1000 | Max number of Spark SQL result to display. |
| zeppelin.livy.spark.sql.field.truncate | true | Whether to truncate field values longer than 20 characters or not |
| zeppelin.livy.session.create\_timeout | 120 | Timeout in seconds for session creation |
| zeppelin.livy.displayAppInfo | true | Whether to display app info |
| zeppelin.livy.pull\_status.interval.millis | 1000 | The interval for checking paragraph execution status |
| livy.spark.driver.cores |  | Driver cores. ex) 1, 2. |
| livy.spark.driver.memory |  | Driver memory. ex) 512m, 32g. |
| livy.spark.executor.instances |  | Executor instances. ex) 1, 4. |
| livy.spark.executor.cores |  | Num cores per executor. ex) 1, 4. |
| livy.spark.executor.memory |  | Executor memory per worker instance. ex) 512m, 32g. |
| livy.spark.dynamicAllocation.enabled |  | Use dynamic resource allocation. ex) True, False. |
| livy.spark.dynamicAllocation.cachedExecutorIdleTimeout |  | Remove an executor which has cached data blocks. |
| livy.spark.dynamicAllocation.minExecutors |  | Lower bound for the number of executors. |
| livy.spark.dynamicAllocation.initialExecutors |  | Initial number of executors to run. |
| livy.spark.dynamicAllocation.maxExecutors |  | Upper bound for the number of executors. |
| livy.spark.jars.packages |  | Adding extra libraries to livy interpreter |
| zeppelin.livy.ssl.trustStore |  | client trustStore file. Used when livy ssl is enabled |
| zeppelin.livy.ssl.trustStorePassword |  | password for trustStore file. Used when livy ssl is enabled |
| zeppelin.livy.ssl.trustStoreType | JKS | type of truststore. Either JKS or PKCS12. |
| zeppelin.livy.ssl.keyStore |  | client keyStore file. Needed if Livy requires two way SSL authentication. |
| zeppelin.livy.ssl.keyStorePassword |  | password for keyStore file. |
| zeppelin.livy.ssl.keyStoreType | JKS | type of keystore. Either JKS or PKCS12. |
| zeppelin.livy.ssl.keyPassword |  | password for key in the keyStore file. Defaults to zeppelin.livy.ssl.keyStorePassword. |
| zeppelin.livy.http.headers | key\_1: value\_1; key\_2: value\_2 | custom http headers when calling livy rest api. Each http header is separated by `;`, and each header is one key value pair where key value is separated by `:` |
| zeppelin.livy.tableWithUTFCharacters | false | If database contains UTF characters then set this as true. |

**We remove livy.spark.master in zeppelin-0.7. Because we sugguest user to use livy 0.3 in zeppelin-0.7. And livy 0.3 don't allow to specify livy.spark.master, it enfornce yarn-cluster mode.**

<a id="interpreter-livy--adding-external-libraries"></a>

## Adding External libraries

You can load dynamic library to livy interpreter by set `livy.spark.jars.packages` property to comma-separated list of maven coordinates of jars to include on the driver and executor classpaths. The format for the coordinates should be groupId:artifactId:version.

Example

| Property | Example | Description |
| --- | --- | --- |
| livy.spark.jars.packages | io.spray:spray-json\_2.10:1.3.1 | Adding extra libraries to livy interpreter |

<a id="interpreter-livy--how-to-use"></a>

## How to use

Basically, you can use

**spark**

```scala
%livy.spark
sc.version
```

**pyspark**

```python
%livy.pyspark
print "1"
```

**sparkR**

```r
%livy.sparkr
hello <- function( name ) {
    sprintf( "Hello, %s", name );
}

hello("livy")
```

<a id="interpreter-livy--impersonation"></a>

## Impersonation

When Zeppelin server is running with authentication enabled, then this interpreter utilizes Livy’s user impersonation feature
i.e. sends extra parameter for creating and running a session ("proxyUser": "${loggedInUser}").
This is particularly useful when multi users are sharing a Notebook server.

<a id="interpreter-livy--apply-zeppelin-dynamic-forms"></a>

## Apply Zeppelin Dynamic Forms

You can leverage [Zeppelin Dynamic Form](#usage-dynamic_form-intro). Form templates is only avalible for livy sql interpreter.

```sql
%livy.sql
select * from products where ${product_id=1}
```

And creating dynamic formst programmatically is not feasible in livy interpreter, because ZeppelinContext is not available in livy interpreter.

<a id="interpreter-livy--shared-sparkcontext"></a>

## Shared SparkContext

Starting from livy 0.5 which is supported by Zeppelin 0.8.0, SparkContext is shared between scala, python, r and sql.
That means you can query the table via `%livy.sql` when this table is registered in `%livy.spark`, `%livy.pyspark`, `$livy.sparkr`.

<a id="interpreter-livy--faq"></a>

## FAQ

Livy debugging: If you see any of these in error console

> Connect to livyhost:8998 [livyhost/127.0.0.1, livyhost/0:0:0:0:0:0:0:1] failed: Connection refused

Looks like the livy server is not up yet or the config is wrong

> Exception: Session not found, Livy server would have restarted, or lost session.

The session would have timed out, you may need to restart the interpreter.

> Blacklisted configuration values in session config: spark.master

Edit `conf/spark-blacklist.conf` file in livy server and comment out `#spark.master` line.

If you choose to work on livy in `apps/spark/java` directory in <https://github.com/cloudera/hue>, copy `spark-user-configurable-options.template` to `spark-user-configurable-options.conf` file in livy server and comment out `#spark.master`.

---

---

<a id="interpreter-mahout"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/mahout.html -->

<!-- page_index: 70 -->

<a id="interpreter-mahout--apache-mahout-interpreter-for-apache-zeppelin"></a>

# Apache Mahout Interpreter for Apache Zeppelin

<a id="interpreter-mahout--installation"></a>

## Installation

Apache Mahout is a collection of packages that enable machine learning and matrix algebra on underlying engines such as Apache Flink or Apache Spark. A convenience script for creating and configuring two Mahout enabled interpreters exists. The `%sparkMahout` and `%flinkMahout` interpreters do not exist by default but can be easily created using this script.

<a id="interpreter-mahout--easy-installation"></a>

### Easy Installation

To quickly and easily get up and running using Apache Mahout, run the following command from the top-level directory of the Zeppelin install:

```bash
python scripts/mahout/add_mahout.py
```

This will create the `%sparkMahout` and `%flinkMahout` interpreters, and restart Zeppelin.

<a id="interpreter-mahout--advanced-installation"></a>

### Advanced Installation

The `add_mahout.py` script contains several command line arguments for advanced users.

| Argument | Description | Example |
| --- | --- | --- |
| `--zeppelin_home` | This is the path to the Zeppelin installation. This flag is not needed if the script is run from the top-level installation directory or from the `zeppelin/scripts/mahout` directory. | `/path/to/zeppelin` |
| `--mahout_home` | If the user has already installed Mahout, this flag can set the path to `MAHOUT_HOME`. If this is set, downloading Mahout will be skipped. | `/path/to/mahout_home` |
| `--restart_later` | Restarting is necessary for updates to take effect. By default the script will restart Zeppelin for you. Restart will be skipped if this flag is set. | NA |
| `--force_download` | This flag will force the script to re-download the binary even if it already exists. This is useful for previously failed downloads. | NA |
| `--overwrite_existing` | This flag will force the script to overwrite existing `%sparkMahout` and `%flinkMahout` interpreters. Useful when you want to just start over. | NA |

**NOTE 1:** Apache Mahout at this time only supports Spark 1.5 and Spark 1.6 and Scala 2.10. If the user is using another version of Spark (e.g. 2.0), the `%sparkMahout` will likely not work. The `%flinkMahout` interpreter will still work and the user is encouraged to develop with that engine as the code can be ported via copy and paste, as is evidenced by the tutorial notebook.

**NOTE 2:** If using Apache Flink in cluster mode, the following libraries will also need to be coppied to `${FLINK_HOME}/lib`
- mahout-math-0.12.2.jar
- mahout-math-scala*2.10-0.12.2.jar
- mahout-flink*2.10-0.12.2.jar
- mahout-hdfs-0.12.2.jar
- [com.google.guava:guava:14.0.1](http://central.maven.org/maven2/com/google/guava/guava/14.0.1/guava-14.0.1.jar)

<a id="interpreter-mahout--overview"></a>

## Overview

The [Apache Mahout](http://mahout.apache.org/)™ project's goal is to build an environment for quickly creating scalable performant machine learning applications.

Apache Mahout software provides three major features:

- A simple and extensible programming environment and framework for building scalable algorithms
- A wide variety of premade algorithms for Scala + Apache Spark, H2O, Apache Flink
- Samsara, a vector math experimentation environment with R-like syntax which works at scale

In other words:

*Apache Mahout provides a unified API for quickly creating machine learning algorithms on a variety of engines.*

<a id="interpreter-mahout--how-to-use"></a>

## How to use

When starting a session with Apache Mahout, depending on which engine you are using (Spark or Flink), a few imports must be made and a *Distributed Context* must be declared. Copy and paste the following code and run once to get started.

<a id="interpreter-mahout--flink"></a>

### Flink

```scala
%flinkMahout

import org.apache.flink.api.scala._
import org.apache.mahout.math.drm._
import org.apache.mahout.math.drm.RLikeDrmOps._
import org.apache.mahout.flinkbindings._
import org.apache.mahout.math._
import scalabindings._
import RLikeOps._

implicit val ctx = new FlinkDistributedContext(benv)
```

<a id="interpreter-mahout--spark"></a>

### Spark

```scala
%sparkMahout

import org.apache.mahout.math._
import org.apache.mahout.math.scalabindings._
import org.apache.mahout.math.drm._
import org.apache.mahout.math.scalabindings.RLikeOps._
import org.apache.mahout.math.drm.RLikeDrmOps._
import org.apache.mahout.sparkbindings._

implicit val sdc: org.apache.mahout.sparkbindings.SparkDistributedContext = sc2sdc(sc)
```

<a id="interpreter-mahout--same-code-different-engines"></a>

### Same Code, Different Engines

After importing and setting up the distributed context, the Mahout R-Like DSL is consistent across engines. The following code will run in both `%flinkMahout` and `%sparkMahout`

```scala
val drmData = drmParallelize(dense(
  (2, 2, 10.5, 10, 29.509541),  // Apple Cinnamon Cheerios
  (1, 2, 12,   12, 18.042851),  // Cap'n'Crunch
  (1, 1, 12,   13, 22.736446),  // Cocoa Puffs
  (2, 1, 11,   13, 32.207582),  // Froot Loops
  (1, 2, 12,   11, 21.871292),  // Honey Graham Ohs
  (2, 1, 16,   8,  36.187559),  // Wheaties Honey Gold
  (6, 2, 17,   1,  50.764999),  // Cheerios
  (3, 2, 13,   7,  40.400208),  // Clusters
  (3, 3, 13,   4,  45.811716)), numPartitions = 2)

drmData.collect(::, 0 until 4)

val drmX = drmData(::, 0 until 4)
val y = drmData.collect(::, 4)
val drmXtX = drmX.t %*% drmX
val drmXty = drmX.t %*% y


val XtX = drmXtX.collect
val Xty = drmXty.collect(::, 0)
val beta = solve(XtX, Xty)
```

<a id="interpreter-mahout--leveraging-resource-pools-and-r-for-visualization"></a>

## Leveraging Resource Pools and R for Visualization

Resource Pools are a powerful Zeppelin feature that lets us share information between interpreters. A fun trick is to take the output of our work in Mahout and analyze it in other languages.

<a id="interpreter-mahout--setting-up-a-resource-pool-in-flink"></a>

### Setting up a Resource Pool in Flink

In Spark based interpreters resource pools are accessed via the ZeppelinContext API. To put and get things from the resource pool one can be done simple

```scala
val myVal = 1
z.put("foo", myVal)
val myFetchedVal = z.get("foo")
```

To add this functionality to a Flink based interpreter we declare the follwoing

```scala
%flinkMahout

import org.apache.zeppelin.interpreter.InterpreterContext

val z = InterpreterContext.get().getResourcePool()
```

Now we can access the resource pool in a consistent manner from the `%flinkMahout` interpreter.

<a id="interpreter-mahout--passing-a-variable-from-mahout-to-r-and-plotting"></a>

### Passing a variable from Mahout to R and Plotting

In this simple example, we use Mahout (on Flink or Spark, the code is the same) to create a random matrix and then take the Sin of each element. We then randomly sample the matrix and create a tab separated string. Finally we pass that string to R where it is read as a .tsv file, and a DataFrame is created and plotted using native R plotting libraries.

```scala
val mxRnd = Matrices.symmetricUniformView(5000, 2, 1234)
val drmRand = drmParallelize(mxRnd)


val drmSin = drmRand.mapBlock() {case (keys, block) =>
  val blockB = block.like()
  for (i <- 0 until block.nrow) {
    blockB(i, 0) = block(i, 0)
    blockB(i, 1) = Math.sin((block(i, 0) * 8))
  }
  keys -> blockB
}

z.put("sinDrm", org.apache.mahout.math.drm.drmSampleToTSV(drmSin, 0.85))
```

And then in an R paragraph...

```r
%spark.r {"imageWidth": "400px"}

library("ggplot2")

sinStr = z.get("flinkSinDrm")

data <- read.table(text= sinStr, sep="\t", header=FALSE)

plot(data,  col="red")
```

---

---

<a id="interpreter-markdown"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/markdown.html -->

<!-- page_index: 71 -->

<a id="interpreter-markdown--markdown-interpreter-for-apache-zeppelin"></a>

# Markdown Interpreter for Apache Zeppelin

<a id="interpreter-markdown--overview"></a>

## Overview

[Markdown](http://daringfireball.net/projects/markdown/) is a plain text formatting syntax designed so that it can be converted to HTML.
Apache Zeppelin uses [flexmark](https://github.com/vsch/flexmark-java) and [markdown4j](https://github.com/jdcasey/markdown4j) as markdown parsers.

In Zeppelin notebook, you can use `%md` in the beginning of a paragraph to invoke the Markdown interpreter and generate static html from Markdown plain text.

In Zeppelin, Markdown interpreter is enabled by default and uses the [flexmark](https://github.com/vsch/flexmark-java) parser.

![](assets/images/markdown-interpreter-setting_72aa59bca45f7572.png)

<a id="interpreter-markdown--example"></a>

## Example

The following example demonstrates the basic usage of Markdown in a Zeppelin notebook.

![](assets/images/markdown-example_d417b36c73a3d135.png)

<a id="interpreter-markdown--mathematical-expression"></a>

## Mathematical expression

Markdown interpreter leverages %html display system internally. That means you can mix mathematical expressions with markdown syntax.
For more information, please see [Mathematical Expression](#usage-display_system-basic--mathematical-expressions) section.

<a id="interpreter-markdown--configuration"></a>

## Configuration

| Name | Default Value | Description |
| --- | --- | --- |
| markdown.parser.type | flexmark | Markdown Parser Type. Available values: flexmark, markdown4j. |

<a id="interpreter-markdown--flexmark-parser-default-markdown-parser"></a>

### Flexmark parser (Default Markdown Parser)

CommonMark/Markdown Java parser with source level AST.

![](assets/images/markdown-example-flexmark-parser_19df21e83c3719d5.png)

`flexmark` parser provides [YUML](http://yuml.me/) and [Websequence](https://www.websequencediagrams.com/) extensions also.

![](assets/images/markdown-example-flexmark-parser-extensions_05c8d9e32ac346ab.png)

<a id="interpreter-markdown--markdown4j-parser"></a>

### Markdown4j Parser

Since `flexmark` parser is more accurate and provides much more markdown syntax `markdown4j` option might be removed later. But keep this parser for the backward compatibility.

---

---

<a id="interpreter-mongodb"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/mongodb.html -->

<!-- page_index: 72 -->

<a id="interpreter-mongodb--mongodb-interpreter-for-apache-zeppelin"></a>

# MongoDB interpreter for Apache Zeppelin

<a id="interpreter-mongodb--overview"></a>

## Overview

[MongoDB](https://www.mongodb.com/) is a general purpose, document-based, distributed database built for modern application developers and for the cloud era.
This interpreter use mongo shell to execute [scripts](https://docs.mongodb.com/manual/tutorial/write-scripts-for-the-mongo-shell/)
Use mongo-shell `JavaScript` to analyze data as you need.

<a id="interpreter-mongodb--installing-and-configuration"></a>

## Installing AND Configuration

First, you need to install mongo shell with Zeppelin in the same machine.
If you use mac with brew, follow this instructions.
`brew tap mongodb/brew
brew install mongodb/brew/mongodb-community-shell`
Or you can follow this [mongo shell](https://docs.mongodb.com/manual/mongo/)
Second, create mongodb interpreter in Zeppelin.
![MongoDB interpreter install](assets/images/mongo-interpreter-install_180095c0b65d8482.png)

| Name | Default Value | Description |
| --- | --- | --- |
| mongo.shell.path | mongosh | MongoDB shell local path. Use `which mongosh` to get local path in linux or mac. (For below [version 5.0](https://www.mongodb.com/docs/manual/release-notes/5.0/#shell-changes), check `mongo`) |
| mongo.shell.command.table.limit | 1000 | Limit of documents displayed in a table. Use table function when get data from mongodb |
| mongo.shell.command.timeout | 60000 | MongoDB shell command timeout in millisecond |
| mongo.server.host | localhost | MongoDB server host to connect to |
| mongo.server.port | 27017 | MongoDB server port to connect to |
| mongo.server.database | test | MongoDB database name |
| mongo.server.authentdatabase |  | MongoDB database name for authentication |
| mongo.server.username |  | Username for authentication |
| mongo.server.password |  | Password for authentication |
| mongo.interpreter.concurrency.max | 10 | Max count of scheduler concurrency |

<a id="interpreter-mongodb--examples"></a>

## Examples

The following example demonstrates the basic usage of MongoDB in a Zeppelin notebook.
![MongoDB interpreter examples](assets/images/mongo-examples_b3f3c61c62b34c32.png)
Or you can monitor stats of mongodb collections.
![MongoDB interpreter examples](assets/images/mongo-interpreter-monitor_3e2594d68cf5605c.png)

---

---

<a id="interpreter-neo4j"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/neo4j.html -->

<!-- page_index: 73 -->

<a id="interpreter-neo4j--neo4j-interpreter-for-apache-zeppelin"></a>

# Neo4j Interpreter for Apache Zeppelin

<a id="interpreter-neo4j--overview"></a>

## Overview

[Neo4j](https://neo4j.com/product/) is a native graph database, designed to store and process graphs from bottom to top.

<a id="interpreter-neo4j--supported-version"></a>

### Supported Version

The Neo4j Interpreter supports all Neo4j versions since v3 via the official [Neo4j Java Driver](https://github.com/neo4j/neo4j-java-driver)

![Neo4j - Interpreter - Video](assets/images/neo4j-interpreter-video_be590217fde9ca1a.gif)

<a id="interpreter-neo4j--configuration"></a>

## Configuration

| Property | Default | Description |
| --- | --- | --- |
| neo4j.url | bolt://localhost:7687 | The Neo4j's BOLT url. |
| neo4j.database |  | The neo4j target database, if empty use the dafault db. |
| neo4j.multi.statement | true | Enables the multi statement management, if true it computes multiple queries separated by semicolon. |
| neo4j.auth.type | BASIC | The Neo4j's authentication type (NONE, BASIC). |
| neo4j.auth.user | neo4j | The Neo4j user name. |
| neo4j.auth.password | neo4j | The Neo4j user password. |
| neo4j.max.concurrency | 50 | Max concurrency call from Zeppelin to Neo4j server. |

![Interpreter configuration](/docs/0.12.0/assets/themes/zeppelin/img/docs-img/neo4j-config.png)
<a id="interpreter-neo4j--enabling-the-neo4j-interpreter"></a>

## Enabling the Neo4j Interpreter

In a notebook, to enable the **Neo4j** interpreter, click the **Gear** icon and select **Neo4j**.

<a id="interpreter-neo4j--using-the-neo4j-interpreter"></a>

## Using the Neo4j Interpreter

In a paragraph, use `%neo4j` to select the Neo4j interpreter and then input the Cypher commands.
For list of Cypher commands please refer to the official [Cyper Refcard](http://neo4j.com/docs/cypher-refcard/current/)

```
%neo4j
//Sample the TrumpWorld dataset
WITH
'https://docs.google.com/spreadsheets/u/1/d/1Z5Vo5pbvxKJ5XpfALZXvCzW26Cl4we3OaN73K9Ae5Ss/export?format=csv&gid=1996904412' AS url
LOAD CSV WITH HEADERS FROM url AS row
RETURN row.`Entity A`, row.`Entity A Type`, row.`Entity B`, row.`Entity B Type`, row.Connection, row.`Source(s)`
LIMIT 10
```

The Neo4j interpreter leverages the [Network display system](#usage-display_system-basic--network) allowing to visualize the them directly from the paragraph.

<a id="interpreter-neo4j--write-your-cypher-queries-and-navigate-your-graph"></a>

### Write your Cypher queries and navigate your graph

This query:

```
%neo4j
MATCH (vp:Person {name:"VLADIMIR PUTIN"}), (dt:Person {name:"DONALD J. TRUMP"})
MATCH path = allShortestPaths( (vp)-[*]-(dt) )
RETURN path
```

produces the following result\_
![Neo4j - Graph - Result](assets/images/neo4j-graph_dd7b5faae764d441.png)

<a id="interpreter-neo4j--apply-zeppelin-dynamic-forms"></a>

### Apply Zeppelin Dynamic Forms

You can leverage [Zeppelin Dynamic Form](#usage-dynamic_form-intro) inside your queries. This query:

```
%neo4j
MATCH (o:Organization)-[r]-()
RETURN o.name, count(*), collect(distinct type(r)) AS types
ORDER BY count(*) DESC
LIMIT ${Show top=10}
```

produces the following result:
![Neo4j - Zeppelin - Dynamic Forms](assets/images/neo4j-dynamic-forms_05ca94d941fc7df2.png)

---

---

<a id="interpreter-postgresql"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/postgresql.html -->

<!-- page_index: 74 -->

<a id="interpreter-postgresql--postgresql-apache-hawq-incubating-interpreter-for-apache-zeppelin"></a>

# PostgreSQL, Apache HAWQ (incubating) Interpreter for Apache Zeppelin

<a id="interpreter-postgresql--important-notice"></a>

## Important Notice

Postgresql interpreter is deprecated and merged into [JDBC Interpreter](#interpreter-jdbc).
You can use it with JDBC Interpreter as same functionality.
See [Postgresql setting example](#interpreter-jdbc--postgres) for more detailed information.

---

---

<a id="interpreter-shell"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/shell.html -->

<!-- page_index: 75 -->

<a id="interpreter-shell--shell-interpreter-for-apache-zeppelin"></a>

# Shell interpreter for Apache Zeppelin

<a id="interpreter-shell--overview"></a>

## Overview

Zeppelin Shell has two interpreters the default is the %sh interpreter.

<a id="interpreter-shell--shell-interpreter"></a>

### Shell interpreter

Shell interpreter uses [Apache Commons Exec](https://commons.apache.org/proper/commons-exec) to execute external processes.
In Zeppelin notebook, you can use `%sh` in the beginning of a paragraph to invoke system shell and run commands.

<a id="interpreter-shell--terminal-interpreter"></a>

### Terminal interpreter

Terminal interpreter uses [hterm](https://chromium.googlesource.com/apps/libapps/+/HEAD/hterm), [Pty4J](https://github.com/JetBrains/pty4j) analog terminal operation.

> **Note :** Currently each command runs as the user Zeppelin server is running as.

<a id="interpreter-shell--configuration"></a>

## Configuration

At the "Interpreters" menu in Zeppelin dropdown menu, you can set the property value for Shell interpreter.

| Name | Default | Description |
| --- | --- | --- |
| shell.command.timeout.millisecs | 60000 | Shell command time out in millisecs |
| shell.working.directory.user.home | false | If this set to true, the shell's working directory will be set to user home |
| zeppelin.shell.auth.type |  | Types of authentications' methods supported are SIMPLE, and KERBEROS |
| zeppelin.shell.principal |  | The principal name to load from the keytab |
| zeppelin.shell.keytab.location |  | The path to the keytab file |
| zeppelin.shell.interpolation | false | Enable ZeppelinContext variable interpolation into paragraph text |
| zeppelin.terminal.ip.mapping |  | Internal and external IP mapping of zeppelin server |
| zeppelin.concurrency.max | 10 | Max concurrency of shell interpreter |

<a id="interpreter-shell--example"></a>

## Example

<a id="interpreter-shell--shell-interpreter-2"></a>

### Shell interpreter

The following example demonstrates the basic usage of Shell in a Zeppelin notebook.

![](assets/images/shell-example_851ce0eda225d6ce.png)

If you need further information about **Zeppelin Interpreter Setting** for using Shell interpreter, please read [What is interpreter setting?](#usage-interpreter-overview--what-is-interpreter-setting) section first.

<a id="interpreter-shell--kerberos-refresh-interval"></a>

### Kerberos refresh interval

For changing the default behavior of when to renew Kerberos ticket following changes can be made in `conf/zeppelin-env.sh`.

```bash
# Change Kerberos refresh interval (default value is 1d). Allowed postfix are ms, s, m, min, h, and d. export KERBEROS_REFRESH_INTERVAL=4h
# Change kinit number retries (default value is 5), which means if the kinit command fails for 5 retries consecutively it will close the interpreter. export KINIT_FAIL_THRESHOLD=10
```

<a id="interpreter-shell--object-interpolation"></a>

### Object Interpolation

The shell interpreter also supports interpolation of `ZeppelinContext` objects into the paragraph text.
The following example shows one use of this facility:

<a id="interpreter-shell--in-scala-cell:"></a>

#### In Scala cell:

```scala
z.put("dataFileName", "members-list-003.parquet")
    // ...
val members = spark.read.parquet(z.get("dataFileName"))
    // ...
```

<a id="interpreter-shell--in-later-shell-cell:"></a>

#### In later Shell cell:

```bash
%sh
rm -rf {dataFileName}
```

Object interpolation is disabled by default, and can be enabled (for the Shell interpreter) by
setting the value of the property `zeppelin.shell.interpolation` to `true` (see *Configuration* above).
More details of this feature can be found in [Zeppelin-Context](#usage-other_features-zeppelin_context)

<a id="interpreter-shell--terminal-interpreter-2"></a>

### Terminal interpreter

The following example demonstrates the basic usage of terminal in a Zeppelin notebook.

```bash
%sh.terminal
input any char
```

![](assets/images/shell-terminal_2dba1015b643b4e2.gif)

<a id="interpreter-shell--zeppelin.terminal.ip.mapping"></a>

### zeppelin.terminal.ip.mapping

When running the terminal interpreter in the notebook, the front end of the notebook needs to obtain the IP address of the server where the terminal interpreter is located to communicate.

In a public cloud environment, the cloud host has an internal IP and an external access IP, and the interpreter runs in the cloud host. This will cause the notebook front end to be unable to connect to the terminal interpreter properly, resulting in the terminal interpreter being unusable.

Solution: Set the mapping between internal IP and external IP in the terminal interpreter, and connect the front end of the notebook through the external IP of the terminal interpreter.

Example:
{"internal-ip1":"external-ip1", "internal-ip2":"external-ip2"}

---

---

<a id="interpreter-sparql"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/interpreter/sparql.html -->

<!-- page_index: 76 -->

<a id="interpreter-sparql--sparql-interpreter-for-apache-zeppelin"></a>

# SPARQL Interpreter for Apache Zeppelin

<a id="interpreter-sparql--overview"></a>

## Overview

[SPARQL](https://www.w3.org/TR/sparql11-query/) is an RDF query language able to retrieve and manipulate data stored in Resource Description Framework (RDF) format.
Apache Zeppelin for now only supports [Apache Jena](https://jena.apache.org/) to query SPARQL-Endpoints.

To query your endpoint configure it in the Interpreter-Settings and use the **%sparql** interpreter.
Then write your query in the paragraph.
If you want the prefixes to replace the URI's, set the replaceURIs setting.

<a id="interpreter-sparql--configuration"></a>

## Configuration

| Name | Default Value | Description |
| --- | --- | --- |
| sparql.engine | jena | The sparql engine to use for the queries |
| sparql.endpoint | http://dbpedia.org/sparql | Complete URL of the endpoint |
| sparql.replaceURIs | true | Replace the URIs in the result with the prefixes |
| sparql.removeDatatypes | true | Remove the datatypes from Literals so Zeppelin can use the values |

<a id="interpreter-sparql--example"></a>

## Example

![](assets/images/sparql-example_bb845d82e1fe398a.png)

<a id="interpreter-sparql--acknowledgement"></a>

## Acknowledgement

This work was partially supported by the Bavarian State Ministry of Economic Affairs, Regional Development and Energy within the framework of the Bavarian Research and
Development Program "Information and Communication Technology".

---

---

<a id="development-writing_zeppelin_interpreter"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/writing_zeppelin_interpreter.html -->

<!-- page_index: 77 -->

<a id="development-writing_zeppelin_interpreter--writing-a-new-interpreter"></a>

# Writing a New Interpreter

<a id="development-writing_zeppelin_interpreter--what-is-apache-zeppelin-interpreter"></a>

## What is Apache Zeppelin Interpreter

Apache Zeppelin Interpreter is a language backend. For example to use scala code in Zeppelin, you need a scala interpreter.
Every Interpreters belongs to an **InterpreterGroup**.
Interpreters in the same InterpreterGroup can reference each other. For example, SparkSqlInterpreter can reference SparkInterpreter to get SparkContext from it while they're in the same group.

![](assets/images/interpreter_a3dfafed5fc73230.png)

[InterpreterSetting](https://github.com/apache/zeppelin/blob/master/zeppelin-zengine/src/main/java/org/apache/zeppelin/interpreter/InterpreterSetting.java) is configuration of a given [InterpreterGroup](https://github.com/apache/zeppelin/blob/master/zeppelin-interpreter/src/main/java/org/apache/zeppelin/interpreter/InterpreterGroup.java) and a unit of start/stop interpreter.
All Interpreters in the same InterpreterSetting are launched in a single, separate JVM process. The Interpreter communicates with Zeppelin engine via **[Thrift](https://github.com/apache/zeppelin/blob/master/zeppelin-interpreter/src/main/thrift/RemoteInterpreterService.thrift)**.

In 'Separate Interpreter(scoped / isolated) for each note' mode which you can see at the **Interpreter Setting** menu when you create a new interpreter, new interpreter instance will be created per note. But it still runs on the same JVM while they're in the same InterpreterSettings.

<a id="development-writing_zeppelin_interpreter--make-your-own-interpreter"></a>

## Make your own Interpreter

Creating a new interpreter is quite simple. Just extend [org.apache.zeppelin.interpreter](https://github.com/apache/zeppelin/blob/master/zeppelin-interpreter/src/main/java/org/apache/zeppelin/interpreter/Interpreter.java) abstract class and implement some methods.
For your interpreter project, you need to make `interpreter-parent` as your parent project and use plugin `maven-enforcer-plugin`, `maven-dependency-plugin` and `maven-resources-plugin`. Here's one sample pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <artifactId>interpreter-parent</artifactId>
        <groupId>org.apache.zeppelin</groupId>
        <version>0.9.0-SNAPSHOT</version>
        <relativePath>../interpreter-parent</relativePath>
    </parent>

    ...

    <dependencies>
        <dependency>
            <groupId>org.apache.zeppelin</groupId>
            <artifactId>zeppelin-interpreter</artifactId>
            <version>${project.version}</version>
            <scope>provided</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <artifactId>maven-enforcer-plugin</artifactId>
            </plugin>
            <plugin>
                <artifactId>maven-dependency-plugin</artifactId>
            </plugin>
            <plugin>
                <artifactId>maven-resources-plugin</artifactId>
            </plugin>
        </plugins>
    </build>

</project>
```

You should include `org.apache.zeppelin:zeppelin-interpreter:[VERSION]` as your interpreter's dependency in `pom.xml`. Bes
And you should put your jars under your interpreter directory with a specific directory name. Zeppelin server reads interpreter directories recursively and initializes interpreters including your own interpreter.

There are three locations where you can store your interpreter group, name and other information. Zeppelin server tries to find the location below. Next, Zeppelin tries to find `interpreter-setting.json` in your interpreter jar.

```
{ZEPPELIN_INTERPRETER_DIR}/{YOUR_OWN_INTERPRETER_DIR}/interpreter-setting.json
```

Here is an example of `interpreter-setting.json` on your own interpreter.

```json
[{"group": "your-group","name": "your-name","className": "your.own.interpreter.class","properties": {"properties1": {"envName": null,"propertyName": "property.1.name","defaultValue": "propertyDefaultValue","description": "Property description","type": "textarea" },"properties2": {"envName": PROPERTIES_2,"propertyName": null,"defaultValue": "property2DefaultValue","description": "Property 2 description","type": "textarea" }, ...},"editor": {"language": "your-syntax-highlight-language","editOnDblClick": false,"completionKey": "TAB" },"config": {"runOnSelectionChange": true/false,"title": true/false,"checkEmpty": true/false} },{...}]
```

Finally, Zeppelin uses static initialization with the following:

```java
static {
  Interpreter.register("MyInterpreterName", MyClassName.class.getName());
}
```

**Static initialization is deprecated and will be supported until 0.6.0.**

The name will appear later in the interpreter name option box during the interpreter configuration process.
The name of the interpreter is what you later write to identify a paragraph which should be interpreted using this interpreter.

```
%MyInterpreterName
some interpreter specific code...
```

<a id="development-writing_zeppelin_interpreter--editor-setting-for-interpreter"></a>

## Editor setting for Interpreter

You can add `editor` object to `interpreter-setting.json` file to specify paragraph editor settings.

<a id="development-writing_zeppelin_interpreter--language"></a>

### Language

If the interpreter uses a specific programming language (like Scala, Python, SQL), it is generally recommended to add a syntax highlighting supported for that to the note paragraph editor.

To check out the list of languages supported, see the `mode-*.js` files under `zeppelin-web/bower_components/ace-builds/src-noconflict` or from [github.com/ajaxorg/ace-builds](https://github.com/ajaxorg/ace-builds/tree/master/src-noconflict).

If you want to add a new set of syntax highlighting,

1. Add the `mode-*.js` file to `zeppelin-web/bower.json` (when built, `zeppelin-web/src/index.html` will be changed automatically).
2. Add `language` field to `editor` object. Note that if you don't specify language field, your interpreter will use plain text mode for syntax highlighting. Let's say you want to set your language to `java`, then add:

```json
  "editor": {
      "language": "java"
  }
```

<a id="development-writing_zeppelin_interpreter--edit-on-double-click"></a>

### Edit on double click

If your interpreter uses mark-up language such as markdown or HTML, set `editOnDblClick` to `true` so that text editor opens on pargraph double click and closes on paragraph run. Otherwise set it to `false`.

```json
"editor": {
  "editOnDblClick": false
}
```

<a id="development-writing_zeppelin_interpreter--completion-key-optional"></a>

### Completion key (Optional)

By default, `Ctrl+dot(.)` brings autocompletion list in the editor.
Through `completionKey`, each interpreter can configure autocompletion key.
Currently `TAB` is only available option.

```json
"editor": {
  "completionKey": "TAB"
}
```

<a id="development-writing_zeppelin_interpreter--notebook-paragraph-display-title-optional"></a>

### Notebook paragraph display title (Optional)

The notebook paragraph does not display the title by default.
You can have the title of the notebook display the title by `config.title=true`.

```json
"config": {
  "title": true  # default: false
}
```

<a id="development-writing_zeppelin_interpreter--notebook-run-on-selection-change-optional"></a>

### Notebook run on selection change (Optional)

The dynamic form in the notebook triggers execution when the selection is modified.
You can make the dynamic form in the notebook not trigger execution after selecting the modification by setting `config.runOnSelectionChange=false`.

```json
"config": {
  "runOnSelectionChange": false # default: true
}
```

<a id="development-writing_zeppelin_interpreter--check-if-the-paragraph-is-empty-before-running-optional"></a>

### Check if the paragraph is empty before running (Optional)

The notebook's paragraph default will not run if it is empty.
You can set `config.checkEmpty=false`, to run even when the paragraph of the notebook is empty.

```json
"config": {
  "checkEmpty": false # default: true
}
```

<a id="development-writing_zeppelin_interpreter--install-your-interpreter-binary"></a>

## Install your interpreter binary

Once you have built your interpreter, you can place it under the interpreter directory with all its dependencies.

```
[ZEPPELIN_HOME]/interpreter/[INTERPRETER_NAME]/
```

<a id="development-writing_zeppelin_interpreter--configure-your-interpreter"></a>

## Configure your interpreter

To configure your interpreter you need to follow these steps:

1. Start Zeppelin by running `./bin/zeppelin-daemon.sh start`.
2. In the interpreter page, click the `+Create` button and configure your interpreter properties.
   Now you are done and ready to use your interpreter.

> **Note :** Interpreters released with zeppelin have a [default configuration](https://github.com/apache/zeppelin/blob/master/zeppelin-interpreter/src/main/java/org/apache/zeppelin/conf/ZeppelinConfiguration.java#L928) which is used when there is no `conf/zeppelin-site.xml`.

<a id="development-writing_zeppelin_interpreter--use-your-interpreter"></a>

## Use your interpreter

<a id="development-writing_zeppelin_interpreter--0.5.0"></a>

### 0.5.0

Inside of a note, `%[INTERPRETER_NAME]` directive will call your interpreter.
Note that the first interpreter configuration in zeppelin.interpreters will be the default one.

For example,

```scala
%myintp

val a = "My interpreter"
println(a)
```

<a id="development-writing_zeppelin_interpreter--0.6.0-and-later"></a>

### 0.6.0 and later

Inside of a note, `%[INTERPRETER_GROUP].[INTERPRETER_NAME]` directive will call your interpreter.

You can omit either `[INTERPRETER\_GROUP]` or `[INTERPRETER\_NAME]`. If you omit `[INTERPRETER\_NAME]`, then first available interpreter will be selected in the `[INTERPRETER\_GROUP]`.
Likewise, if you skip `[INTERPRETER\_GROUP]`, then `[INTERPRETER\_NAME]` will be chosen from default interpreter group.

For example, if you have two interpreter `myintp1` and `myintp2` in group `mygrp`, you can call myintp1 like

```
%mygrp.myintp1

codes for myintp1
```

and you can call `myintp2` like

```
%mygrp.myintp2

codes for myintp2
```

If you omit your interpreter name, it'll select first available interpreter in the group ( `myintp1` ).

```
%mygrp

codes for myintp1
```

You can only omit your interpreter group when your interpreter group is selected as a default group.

```
%myintp2

codes for myintp2
```

<a id="development-writing_zeppelin_interpreter--examples"></a>

## Examples

Checkout some interpreters released with Zeppelin by default.

- [spark](https://github.com/apache/zeppelin/tree/master/spark)
- [markdown](https://github.com/apache/zeppelin/tree/master/markdown)
- [shell](https://github.com/apache/zeppelin/tree/master/shell)
- [jdbc](https://github.com/apache/zeppelin/tree/master/jdbc)

<a id="development-writing_zeppelin_interpreter--contributing-a-new-interpreter-to-zeppelin-releases"></a>

## Contributing a new Interpreter to Zeppelin releases

We welcome contribution to a new interpreter. Please follow these few steps:

- First, check out the general contribution guide [here](https://zeppelin.apache.org/contribution/contributions.html).
- Follow the steps in [Make your own Interpreter](#development-writing_zeppelin_interpreter--make-your-own-interpreter) section and [Editor setting for Interpreter](#development-writing_zeppelin_interpreter--editor-setting-for-interpreter) above.
- Add your interpreter as in the [Configure your interpreter](#development-writing_zeppelin_interpreter--configure-your-interpreter) section above; also add it to the example template [zeppelin-site.xml.template](https://github.com/apache/zeppelin/blob/master/conf/zeppelin-site.xml.template).
- Add tests! They are run for all changes and it is important that they are self-contained.
- Include your interpreter as a module in [`pom.xml`](https://github.com/apache/zeppelin/blob/master/pom.xml).
- Add documentation on how to use your interpreter under `docs/interpreter/`. Follow the Markdown style as this [example](https://github.com/apache/zeppelin/blob/master/docs/interpreter/elasticsearch.md). Make sure you list config settings and provide working examples on using your interpreter in code boxes in Markdown. Link to images as appropriate (images should go to `docs/assets/themes/zeppelin/img/docs-img/`). And add a link to your documentation in the navigation menu (`docs/_includes/themes/zeppelin/_navigation.html`).
- Most importantly, ensure licenses of the transitive closure of all dependencies are list in [license file](https://github.com/apache/zeppelin/blob/master/zeppelin-distribution/src/bin_license/LICENSE).
- Commit your changes and open a [Pull Request](https://github.com/apache/zeppelin/pulls) on the project [Mirror on GitHub](https://github.com/apache/zeppelin); check to make sure Travis CI build is passing.

---

---

<a id="development-helium-overview"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/helium/overview.html -->

<!-- page_index: 78 -->

<a id="development-helium-overview--helium-overview"></a>

# Helium Overview

<a id="development-helium-overview--what-is-helium"></a>

## What is Helium?

Helium is a plugin system that can extend Zeppelin a lot.
For example, you can write [custom display system](#development-helium-writing_spell) or
install already published one in [Helium Online Registry](http://zeppelin.apache.org/helium_packages.html).

Currently, Helium supports 4 types of package.

- [Helium Visualization](#development-helium-writing_visualization_basic): Adding a new chart type
- [Helium Spell](#development-helium-writing_spell): Adding new interpreter, display system running on browser
- [Helium Application](#development-helium-writing_application)
- [Helium Interpreter](#development-writing_zeppelin_interpreter): Adding a new custom interpreter

<a id="development-helium-overview--configuration"></a>

## Configuration

Zeppelin ships with several builtin helium plugins which is located in $ZEPPELIN\_HOME/heliums. If you want to try more types of heliums plugins, you can configure `zeppelin.helium.registry` to be `helium,https://zeppelin.apache.org/helium.json` in zeppelin-site.xml. `https://zeppelin.apache.org/helium.json` will be updated regularly.

---

---

<a id="development-helium-writing_application"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/helium/writing_application.html -->

<!-- page_index: 79 -->

<a id="development-helium-writing_application--writing-a-new-application"></a>

# Writing a new Application

<a id="development-helium-writing_application--what-is-apache-zeppelin-application"></a>

## What is Apache Zeppelin Application

Apache Zeppelin Application is a package that runs on Interpreter process and displays it's output inside of the notebook. While application runs on Interpreter process, it's able to access resources provided by Interpreter through ResourcePool. Output is always rendered by AngularDisplaySystem. Therefore application provides all the possiblities of making interactive graphical application that uses data and processing power of any Interpreter.

<a id="development-helium-writing_application--make-your-own-application"></a>

## Make your own Application

Writing Application means extending `org.apache.zeppelin.helium.Application`. You can use your favorite IDE and language while Java class files are packaged into jar. `Application` class looks like

```java
/** * Constructor. Invoked when application is loaded */ public Application(ApplicationContext context);
/** * Invoked when there're (possible) updates in required resource set.* i.e. invoked after application load and after paragraph finishes.*/ public abstract void run(ResourceSet args);
/** * Invoked before application unload.* Application is automatically unloaded with paragraph/notebook removal */ public abstract void unload();
```

You can check example applications under [./zeppelin-examples](https://github.com/apache/incubator-zeppelin/tree/master/zeppelin-examples) directory.

<a id="development-helium-writing_application--development-mode"></a>

## Development mode

In the development mode, you can run your Application in your IDE as a normal java application and see the result inside of Zeppelin notebook.

`org.apache.zeppelin.helium.ZeppelinApplicationDevServer` can run Zeppelin Application in development mode.

```java

// entry point for development mode
public static void main(String[] args) throws Exception {

  // add resources for development mode
  LocalResourcePool pool = new LocalResourcePool("dev");
  pool.put("date", new Date());

  // run application in devlopment mode with given resource
  // in this case, Clock.class.getName() will be the application class name  
  org.apache.zeppelin.helium.ZeppelinApplicationDevServer devServer = new org.apache.zeppelin.helium.ZeppelinApplicationDevServer(
    Clock.class.getName(), pool.getAll());

  // start development mode
  devServer.start();
  devServer.join();
}
```

In the Zeppelin notebook, run `%dev run` will connect to application running in development mode.

<a id="development-helium-writing_application--package-file"></a>

## Package file

Package file is a json file that provides information about the application.
Json file contains the following information

```json
{"name" : "[organization].[name]","description" : "Description","artifact" : "groupId:artifactId:version","className" : "your.package.name.YourApplicationClass","resources" : [["resource.name", ":resource.class.name"],["alternative.resource.name", ":alternative.class.name"] ],"icon" : "<i class='icon'></i>"}
```

<a id="development-helium-writing_application--name"></a>

#### name

Name is a string in `[group].[name]` format.
`[group]` and `[name]` allow only `[A-Za-z0-9_]`.
Group is normally the name of an organization who creates this application.

<a id="development-helium-writing_application--description"></a>

#### description

A short description about the application

<a id="development-helium-writing_application--artifact"></a>

#### artifact

Location of the jar artifact.
`"groupId:artifactId:version"` will load artifact from maven repository.
If jar exists in the local filesystem, absolute/relative can be used.

e.g.

When artifact exists in Maven repository

```
artifact: "org.apache.zeppelin:zeppelin-examples:0.6.0"
```

When artifact exists in the local filesystem

```
artifact: "zeppelin-example/target/zeppelin-example-0.6.0.jar"
```

<a id="development-helium-writing_application--classname"></a>

#### className

Entry point. Class that extends `org.apache.zeppelin.helium.Application`

<a id="development-helium-writing_application--resources"></a>

#### resources

Two dimensional array that defines required resources by name or by className. Helium Application launcher will compare resources in the ResourcePool with the information in this field and suggest application only when all required resources are available in the ResourcePool.

Resouce name is a string which will be compared with the name of objects in the ResourcePool. className is a string with ":" prepended, which will be compared with className of the objects in the ResourcePool.

Application may require two or more resources. Required resources can be listed inside of the json array. For example, if the application requires object "name1", "name2" and "className1" type of object to run, resources field can be

```json
resources: [
  [ "name1", "name2", ":className1", ...]
]
```

If Application can handle alternative combination of required resources, alternative set can be listed as below.

```json
resources: [
  [ "name", ":className"],
  [ "altName", ":altClassName1"],
  ...
]
```

Easier way to understand this scheme is

```json
resources: [
   [ 'resource' AND 'resource' AND ... ] OR
   [ 'resource' AND 'resource' AND ... ] OR
   ...
]
```

<a id="development-helium-writing_application--icon"></a>

#### icon

Icon to be used on the application button. String in this field will be rendered as a HTML tag.

e.g.

```
icon: "<i class='fa fa-clock-o'></i>"
```

---

---

<a id="development-helium-writing_spell"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/helium/writing_spell.html -->

<!-- page_index: 80 -->

<a id="development-helium-writing_spell--writing-a-new-spell"></a>

# Writing a new Spell

<a id="development-helium-writing_spell--what-is-apache-zeppelin-spell"></a>

## What is Apache Zeppelin Spell

Spell is a kind of interpreter that runs on browser not on backend. So, technically it's the frontend interpreter.
It can provide many benefits.

- Spell is pluggable frontend interpreter. So it can be installed and removed easily using helium registry.
- Every spell is written in javascript. It means you can use existing javascript libraries whatever you want.
- Spell runs on browser like display system (`%html`, `%table`). In other words, every spell can be used as display system as well.

<a id="development-helium-writing_spell--how-it-works"></a>

## How it works

Helium Spell works like [Helium Visualization](#development-helium-writing_visualization_basic).

- Every helium packages are loaded from central (online) registry or local registry
- You can see loaded packages in `/helium` page.
- When you enable a spell, it's built from server and sent to client
- Finally it will be loaded into browser.

<a id="development-helium-writing_spell--how-to-use-spell"></a>

## How to use spell

<a id="development-helium-writing_spell--1.-enabling"></a>

### 1. Enabling

Find a spell what you want to use in `/helium` package and click `Enable` button.

![](assets/images/writing-spell-registered_a65c9952fda29832.png)

<a id="development-helium-writing_spell--2.-using"></a>

### 2. Using

Spell works like an interpreter. Use the `MAGIC` value to execute spell in a note. (you might need to refresh after enabling)
For example, Use `%echo` for the Echo Spell.

![](assets/images/writing-spell-using_f012b2c1c04f1d15.gif)

<a id="development-helium-writing_spell--write-a-new-spell"></a>

## Write a new Spell

Making a new spell is similar to [Helium Visualization#write-new-visualization](#development-helium-writing_visualization_basic--write-new-visualization).

- Add framework dependency called zeppelin-spell into `package.json`
- Write code using framework
- Publish your spell to [npm](https://zeppelin.apache.org/docs/0.12.0/development/helium/%22https:/www.npmjs.com/%22)

<a id="development-helium-writing_spell--1.-create-a-npm-package"></a>

### 1. Create a npm package

Create a [package.json](https://docs.npmjs.com/files/package.json) in new directory for spell.

- You have to add a framework called `zeppelin-spell` as a dependency to create spell ([zeppelin-spell](https://github.com/apache/zeppelin/tree/master/zeppelin-web/src/app/spell))
- Also, you can add any dependencies you want to utilise.

Here's an example

```json
{"name": "zeppelin-echo-spell","description": "Zeppelin Echo Spell (example)","version": "1.0.0","main": "index","author": "","license": "Apache-2.0","dependencies": {"zeppelin-spell": "*" },"helium": {"icon" : "<i class='fa fa-repeat'></i>","spell": {"magic": "%echo","usage": "%echo <TEXT>"}}}
```

<a id="development-helium-writing_spell--2.-write-spell-using-framework"></a>

### 2. Write spell using framework

Here are some examples you can refer

- [Echo Spell](https://github.com/apache/zeppelin/blob/master/zeppelin-examples/zeppelin-example-spell-echo/index.js)
- [Markdown Spell: Using library](https://github.com/apache/zeppelin/blob/master/zeppelin-examples/zeppelin-example-spell-markdown/index.js)
- [Flowchart Spell: Using DOM](https://github.com/apache/zeppelin/blob/master/zeppelin-examples/zeppelin-example-spell-flowchart/index.js)
- [Google Translation API Spell: Using API (returning promise)](https://github.com/apache/zeppelin/blob/master/zeppelin-examples/zeppelin-example-spell-translator/index.js)

Now, you need to write code to create spell which processing text.

```js
import {SpellBase,SpellResult,DefaultDisplayType,} from 'zeppelin-spell';
export default class EchoSpell extends SpellBase {constructor() {/** pass magic to super class's constructor parameter */ super("%echo");}
interpret(paragraphText) {const processed = paragraphText + '!';
/** * should return `SpellResult` which including `data` and `type` * default type is `TEXT` if you don't specify.*/ return new SpellResult(processed);}}
```

Here is another example. Let's say we want to create markdown spell. First of all, we should add a dependency for markdown in package.json

```json
// package.json
 "dependencies": {
    "markdown": "0.5.0",
    "zeppelin-spell": "*"
  },
```

And here is spell code.

```js
import {SpellBase,SpellResult,DefaultDisplayType,} from 'zeppelin-spell';
import md from 'markdown';
const markdown = md.markdown;
export default class MarkdownSpell extends SpellBase {constructor() {super("%markdown");}
interpret(paragraphText) {const parsed = markdown.toHTML(paragraphText);
/** * specify `DefaultDisplayType.HTML` since `parsed` will contain DOM * otherwise it will be rendered as `DefaultDisplayType.TEXT` (default) */ return new SpellResult(parsed, DefaultDisplayType.HTML);}}
```

- You might want to manipulate DOM directly (e.g google d3.js), then refer [Flowchart Spell](https://github.com/apache/zeppelin/blob/master/zeppelin-examples/zeppelin-example-spell-flowchart/index.js)
- You might want to return promise not string (e.g API call), then refer [Google Translation API Spell](https://github.com/apache/zeppelin/blob/master/zeppelin-examples/zeppelin-example-spell-translator/index.js)

<a id="development-helium-writing_spell--3.-create-helium-package-file-for-local-deployment"></a>

### 3. Create **Helium package file** for local deployment

You don't want to publish your package every time you make a change in your spell. Zeppelin provides local deploy.
The only thing you need to do is creating a **Helium Package file** (JSON) for local deploy.
It's automatically created when you publish to npm repository but in local case, you should make it by yourself.

```json
{"type" : "SPELL","name" : "zeppelin-echo-spell","version": "1.0.0","description" : "Return just what receive (example)","artifact" : "./zeppelin-examples/zeppelin-example-spell-echo","license" : "Apache-2.0","spell": {"magic": "%echo","usage": "%echo <TEXT>"}}
```

- Place this file in your local registry directory (default `$ZEPPELIN_HOME/helium`).
- `type` should be `SPELL`
- Make sure that `artifact` should be same as your spell directory.
- You can get information about other fields in [Helium Visualization#3-create-helium-package-file-and-locally-deploy](#development-helium-writing_visualization_basic--3-create-helium-package-file-and-locally-deploy).

<a id="development-helium-writing_spell--4.-run-in-dev-mode"></a>

### 4. Run in dev mode

```bash
cd zeppelin-web
yarn run dev:helium
```

You can browse localhost:9000. Every time refresh your browser, Zeppelin will rebuild your spell and reload changes.

<a id="development-helium-writing_spell--5.-publish-your-spell-to-the-npm-repository"></a>

### 5. Publish your spell to the npm repository

See [Publishing npm packages](https://docs.npmjs.com/getting-started/publishing-npm-packages)

---

---

<a id="development-helium-writing_visualization_basic"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/helium/writing_visualization_basic.html -->

<!-- page_index: 81 -->

<a id="development-helium-writing_visualization_basic--writing-a-new-visualization"></a>

# Writing a new Visualization

<a id="development-helium-writing_visualization_basic--what-is-apache-zeppelin-visualization"></a>

## What is Apache Zeppelin Visualization

Apache Zeppelin Visualization is a pluggable package that can be loaded/unloaded on runtime through Helium framework in Zeppelin. A Visualization is a javascript npm package and user can use them just like any other built-in visualization in notebook.

<a id="development-helium-writing_visualization_basic--how-it-works"></a>

## How it works

<a id="development-helium-writing_visualization_basic--1.-load-helium-package-files-from-registry"></a>

#### 1. Load Helium package files from registry

Zeppelin needs to know what Visualization packages are available. Zeppelin will read information of packages from both online and local registry.
Registries are configurable through `ZEPPELIN_HELIUM_LOCALREGISTRY_DEFAULT` env variable or `zeppelin.helium.localregistry.default` property.

<a id="development-helium-writing_visualization_basic--2.-enable-packages"></a>

#### 2. Enable packages

Once Zeppelin loads *Helium package files* from registries, available packages are displayed in Helium menu.

Click 'enable' button.

![](assets/images/writing-visualization-helium-menu_fbae72c8da22df2a.png)

<a id="development-helium-writing_visualization_basic--3.-create-and-load-visualization-bundle-on-the-fly"></a>

#### 3. Create and load visualization bundle on the fly

Once a Visualization package is enabled, [HeliumBundleFactory](https://github.com/apache/zeppelin/blob/master/zeppelin-zengine/src/main/java/org/apache/zeppelin/helium/HeliumBundleFactory.java) creates a js bundle. The js bundle is served by `helium/bundle/load` rest api endpoint.

<a id="development-helium-writing_visualization_basic--4.-run-visualization"></a>

#### 4. Run visualization

Zeppelin shows additional button for loaded Visualizations.
User can use just like any other built-in visualizations.

![](assets/images/writing-visualization-example_b0f76ff5ba1350fe.png)

<a id="development-helium-writing_visualization_basic--write-new-visualization"></a>

## Write new Visualization

<a id="development-helium-writing_visualization_basic--1.-create-a-npm-package"></a>

#### 1. Create a npm package

Create a [package.json](https://docs.npmjs.com/files/package.json) in your new Visualization directory. You can add any dependencies in package.json, but you **must include two dependencies: [zeppelin-vis](https://github.com/apache/zeppelin/tree/master/zeppelin-web/src/app/visualization) and [zeppelin-tabledata](https://github.com/apache/zeppelin/tree/master/zeppelin-web/src/app/tabledata).**

Here's an example

```json
{"name": "zeppelin_horizontalbar","description" : "Horizontal Bar chart","version": "1.0.0","main": "horizontalbar","author": "","license": "Apache-2.0","dependencies": {"zeppelin-tabledata": "*","zeppelin-vis": "*"}}
```

<a id="development-helium-writing_visualization_basic--2.-create-your-own-visualization"></a>

#### 2. Create your own visualization

To create your own visualization, you need to create a js file and import [Visualization](https://github.com/apache/zeppelin/blob/master/zeppelin-web/src/app/visualization/visualization.js) class from [zeppelin-vis](https://github.com/apache/zeppelin/tree/master/zeppelin-web/src/app/visualization) package and extend the class. [zeppelin-tabledata](https://github.com/apache/zeppelin/tree/master/zeppelin-web/src/app/tabledata) package provides some useful transformations, like pivot, you can use in your visualization. (you can create your own transformation, too).

[Visualization](https://github.com/apache/zeppelin/blob/master/zeppelin-web/src/app/visualization/visualization.js) class, there're several methods that you need to override and implement. Here's simple visualization that just prints `Hello world`.

```js
import Visualization from 'zeppelin-vis' import PassthroughTransformation from 'zeppelin-tabledata/passthrough'
export default class helloworld extends Visualization {constructor(targetEl, config) {super(targetEl, config) this.passthrough = new PassthroughTransformation(config);}
render(tableData) {this.targetEl.html('Hello world!')}
getTransformation() {return this.passthrough}}
```

To learn more about `Visualization` class, check [visualization.js](https://github.com/apache/zeppelin/blob/master/zeppelin-web/src/app/visualization/visualization.js).

You can check complete visualization package example [here](https://github.com/apache/zeppelin/tree/master/zeppelin-examples/zeppelin-example-horizontalbar).

Zeppelin's built-in visualization uses the same API, so you can check [built-in visualizations](https://github.com/apache/zeppelin/tree/master/zeppelin-web/src/app/visualization/builtins) as additional examples.

<a id="development-helium-writing_visualization_basic--3.-create-helium-package-file-and-locally-deploy"></a>

#### 3. Create **Helium package file** and locally deploy

**Helium Package file** is a json file that provides information about the application.
Json file contains the following information

```json
{"type" : "VISUALIZATION","name" : "zeppelin_horizontalbar","description" : "Horizontal Bar chart (example)","license" : "Apache-2.0","artifact" : "./zeppelin-examples/zeppelin-example-horizontalbar","icon" : "<i class='fa fa-bar-chart rotate90flipX'></i>"}
```

Place this file in your local registry directory (default `./helium`).

<a id="development-helium-writing_visualization_basic--type"></a>

##### type

When you're creating a visualization, 'type' should be 'VISUALIZATION'. Check these types as well.

- [Helium Application](#development-helium-writing_application)
- [Helium Spell](#development-helium-writing_spell)

<a id="development-helium-writing_visualization_basic--name"></a>

##### name

Name of visualization. Should be unique. Allows `[A-Za-z90-9_]`.

<a id="development-helium-writing_visualization_basic--description"></a>

##### description

A short description about visualization.

<a id="development-helium-writing_visualization_basic--artifact"></a>

##### artifact

Location of the visualization npm package. Support npm package with version or local filesystem path.

e.g.

When artifact exists in npm repository

```json
"artifact": "my-visualiztion@1.0.0"
```

When artifact exists in local file system

```json
"artifact": "/path/to/my/visualization"
```

<a id="development-helium-writing_visualization_basic--license"></a>

##### license

License information.

e.g.

```json
"license": "Apache-2.0"
```

<a id="development-helium-writing_visualization_basic--icon"></a>

##### icon

Icon to be used in visualization select button. String in this field will be rendered as a HTML tag.

e.g.

```json
"icon": "<i class='fa fa-coffee'></i>"
```

<a id="development-helium-writing_visualization_basic--4.-run-in-dev-mode"></a>

#### 4. Run in dev mode

Place your **Helium package file** in local registry (`ZEPPELIN_HOME/helium`).
Run Zeppelin. And then run zeppelin-web in visualization dev mode.

```bash
cd zeppelin-web
yarn run dev:helium
```

You can browse `localhost:9000`. Everytime refresh your browser, Zeppelin will rebuild your visualization and reload changes.

<a id="development-helium-writing_visualization_basic--5.-publish-your-visualization"></a>

#### 5. Publish your visualization

Once it's done, publish your visualization package using `npm publish`.
That's it. With in an hour, your visualization will be available in Zeppelin's helium menu.

<a id="development-helium-writing_visualization_basic--see-more"></a>

### See More

Check [Helium Visualization: Transformation](#development-helium-writing_visualization_transformation) for more complex examples.

---

---

<a id="development-helium-writing_visualization_transformation"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/helium/writing_visualization_transformation.html -->

<!-- page_index: 82 -->

<a id="development-helium-writing_visualization_transformation--transformations-for-zeppelin-visualization"></a>

# Transformations for Zeppelin Visualization

<a id="development-helium-writing_visualization_transformation--overview"></a>

## Overview

Transformations

- **renders** setting which allows users to set columns and
- **transforms** table rows according to the configured columns.

Zeppelin provides 4 types of transformations.

<a id="development-helium-writing_visualization_transformation--1.-passthroughtransformation"></a>

## 1. PassthroughTransformation

`PassthroughTransformation` is the simple transformation which does not convert original tabledata at all.

See [passthrough.js](https://github.com/apache/zeppelin/blob/master/zeppelin-web/src/app/tabledata/passthrough.js)

<a id="development-helium-writing_visualization_transformation--2.-columnselectortransformation"></a>

## 2. ColumnselectorTransformation

`ColumnselectorTransformation` is uses when you need `N` axes but do not need aggregation.

See [columnselector.js](https://github.com/apache/zeppelin/blob/master/zeppelin-web/src/app/tabledata/columnselector.js)

<a id="development-helium-writing_visualization_transformation--3.-pivottransformation"></a>

## 3. PivotTransformation

`PivotTransformation` provides group by and aggregation. Every chart using `PivotTransformation` has 3 axes. `Keys`, `Groups` and `Values`.

See [pivot.js](https://github.com/apache/zeppelin/blob/master/zeppelin-web/src/app/tabledata/pivot.js)

<a id="development-helium-writing_visualization_transformation--4.-advancedtransformation"></a>

## 4. AdvancedTransformation

`AdvancedTransformation` has more detailed options while providing existing features of `PivotTransformation` and `ColumnselectorTransformation`

- multiple sub charts
- configurable chart axes
- parameter widgets: `input`, `checkbox`, `option`, `textarea`
- parsing parameters automatically based on their types
- expand / fold axis and parameter panels
- multiple transformation methods while supporting lazy converting
- re-initialize the whole configuration based on spec hash.

<a id="development-helium-writing_visualization_transformation--spec"></a>

### Spec

`AdvancedTransformation` requires `spec` which includes axis and parameter details for charts.

Let's create 2 sub-charts called `line` and `no-group`. Each sub chart can have different axis and parameter depending on their requirements.

```js
class AwesomeVisualization extends Visualization {constructor(targetEl, config) {super(targetEl, config)
const spec = {charts: {'line': {transform: { method: 'object', },sharedAxis: false, /** set if you want to share axes between sub charts, default is `false` */ axis: {'xAxis': { dimension: 'multiple', axisType: 'key', description: 'serial', },'yAxis': { dimension: 'multiple', axisType: 'aggregator', description: 'serial', },'category': { dimension: 'multiple', axisType: 'group', description: 'categorical', },},parameter: {'xAxisUnit': { valueType: 'string', defaultValue: '', description: 'unit of xAxis', },'yAxisUnit': { valueType: 'string', defaultValue: '', description: 'unit of yAxis', },'lineWidth': { valueType: 'int', defaultValue: 0, description: 'width of line', },},},
'no-group': {transform: { method: 'object', },sharedAxis: false,axis: {'xAxis': { dimension: 'single', axisType: 'key', },'yAxis': { dimension: 'multiple', axisType: 'value', },},parameter: {'xAxisUnit': { valueType: 'string', defaultValue: '', description: 'unit of xAxis', },'yAxisUnit': { valueType: 'string', defaultValue: '', description: 'unit of yAxis', },},},}
this.transformation = new AdvancedTransformation(config, spec)}
...
// `render` will be called whenever `axis` or `parameter` is changed render(data) {const { chart, parameter, column, transformer, } = data
if (chart === 'line') {const transformed = transformer() // draw line chart } else if (chart === 'no-group') {const transformed = transformer() // draw no-group chart}}}
```

<a id="development-helium-writing_visualization_transformation--spec:-axis"></a>

### Spec: `axis`

| Field Name | Available Values (type) | Description |
| --- | --- | --- |
| `dimension` | `single` | Axis can contains only 1 column |
| `dimension` | `multiple` | Axis can contains multiple columns |
| `axisType` | `key` | Column(s) in this axis will be used as `key` like in `PivotTransformation`. These columns will be served in `column.key` |
| `axisType` | `aggregator` | Column(s) in this axis will be used as `value` like in `PivotTransformation`. These columns will be served in `column.aggregator` |
| `axisType` | `group` | Column(s) in this axis will be used as `group` like in `PivotTransformation`. These columns will be served in `column.group` |
| `axisType` | (string) | Any string value can be used here. These columns will be served in `column.custom` |
| `maxAxisCount` (optional) | (int) | The max number of columns that this axis can contain. (unlimited if `undefined`) |
| `minAxisCount` (optional) | (int) | The min number of columns that this axis should contain to draw chart. (`1` in case of single dimension) |
| `description` (optional) | (string) | Description for the axis. |

Here is an example.

```js
axis: {
  'xAxis': { dimension: 'multiple', axisType: 'key',  },
  'yAxis': { dimension: 'multiple', axisType: 'aggregator'},
  'category': { dimension: 'multiple', axisType: 'group', maxAxisCount: 2, valueType: 'string', },
},
```

<a id="development-helium-writing_visualization_transformation--spec:-sharedaxis"></a>

### Spec: `sharedAxis`

If you set `sharedAxis: false` for sub charts, then their axes are persisted in global space (shared). It's useful for when you creating multiple sub charts sharing their axes but have different parameters. For example,

- `basic-column`, `stacked-column`, `percent-column`
- `pie` and `donut`

Here is an example.

```js
    const spec = {
      charts: {
        'column': {
          transform: { method: 'array', },
          sharedAxis: true,
          axis: { ... },
          parameter: { ... },
        },

        'stacked': {
          transform: { method: 'array', },
          sharedAxis: true,
          axis: { ... }
          parameter: { ... },
        },
```

<a id="development-helium-writing_visualization_transformation--spec:-parameter"></a>

### Spec: `parameter`

| Field Name | Available Values (type) | Description |
| --- | --- | --- |
| `valueType` | `string` | Parameter which has string value |
| `valueType` | `int` | Parameter which has int value |
| `valueType` | `float` | Parameter which has float value |
| `valueType` | `boolean` | Parameter which has boolean value used with `checkbox` widget usually |
| `valueType` | `JSON` | Parameter which has JSON value used with `textarea` widget usually. `defaultValue` should be `""` (empty string). This |
| `description` | (string) | Description of this parameter. This value will be parsed as HTML for pretty output |
| `widget` | `input` | Use [input](https://developer.mozilla.org/en/docs/Web/HTML/Element/input) widget. This is the default widget (if `widget` is undefined) |
| `widget` | `checkbox` | Use [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/checkbox) widget. |
| `widget` | `textarea` | Use [textarea](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea) widget. |
| `widget` | `option` | Use [select + option](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select) widget. This parameter should have `optionValues` field as well. |
| `optionValues` | (Array) | Available option values used with the `option` widget |

Here is an example.

```js
parameter: {
  // string type, input widget
  'xAxisUnit': { valueType: 'string', defaultValue: '', description: 'unit of xAxis', },

  // boolean type, checkbox widget
  'inverted': { widget: 'checkbox', valueType: 'boolean', defaultValue: false, description: 'invert x and y axes', },

  // string type, option widget with `optionValues`
  'graphType': { widget: 'option', valueType: 'string', defaultValue: 'line', description: 'graph type', optionValues: [ 'line', 'smoothedLine', 'step', ], },

  // HTML in `description`
  'dateFormat': { valueType: 'string', defaultValue: '', description: 'format of date (<a href="https://docs.amcharts.com/3/javascriptcharts/AmGraph#dateFormat">doc</a>) (e.g YYYY-MM-DD)', },

  // JSON type, textarea widget
  'yAxisGuides': { widget: 'textarea', valueType: 'JSON', defaultValue: '', description: 'guides of yAxis ', },
```

<a id="development-helium-writing_visualization_transformation--spec:-transform"></a>

### Spec: `transform`

| Field Name | Available Values (type) | Description |
| --- | --- | --- |
| `method` | `object` | designed for rows requiring object manipulation |
| `method` | `array` | designed for rows requiring array manipulation |
| `method` | `array:2-key` | designed for xyz charts (e.g bubble chart) |
| `method` | `drill-down` | designed for drill-down charts |
| `method` | `raw` | will return the original `tableData.rows` |

Whatever you specified as `transform.method`, the `transformer` value will be always function for lazy computation.

```js
// advanced-transformation.util#getTransformer
if (transformSpec.method === 'raw') {transformer = () => { return rows; } } else if (transformSpec.method === 'array') {transformer = () => {...return { ... }}}
```

Here is actual usage.

```js
class AwesomeVisualization extends Visualization {constructor(...) { /** setup your spec */ }
...
// `render` will be called whenever `axis` or `parameter` are changed render(data) {const { chart, parameter, column, transformer, } = data
if (chart === 'line') {const transformed = transformer() // draw line chart } else if (chart === 'no-group') {const transformed = transformer() // draw no-group chart}}
...}
```

---

---

<a id="development-contribution-useful_developer_tools"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/contribution/useful_developer_tools.html -->

<!-- page_index: 83 -->

<a id="development-contribution-useful_developer_tools--useful-developer-tools"></a>

# Useful Developer Tools

<a id="development-contribution-useful_developer_tools--developing-zeppelin-web"></a>

### Developing `zeppelin-web`

Check [zeppelin-web: Local Development](https://github.com/apache/zeppelin/tree/master/zeppelin-web#local-development).

<a id="development-contribution-useful_developer_tools--tools"></a>

### Tools

<a id="development-contribution-useful_developer_tools--svm:-scala-version-manager"></a>

#### SVM: Scala Version Manager

[svm](https://github.com/yuroyoro/svm) would be useful when changing scala version frequently.

<a id="development-contribution-useful_developer_tools--jdk-change-script:-osx"></a>

#### JDK change script: OSX

this script would be helpful when changing JDK version frequently.

```bash
function setjdk() {
  if [ $# -ne 0 ]; then
  # written based on OSX.
# use diffrent base path for other OS removeFromPath '/System/Library/Frameworks/JavaVM.framework/Home/bin' if [ -n "${JAVA_HOME+x}" ]; then removeFromPath $JAVA_HOME fi export JAVA_HOME=`/usr/libexec/java_home -v $@` export PATH=$JAVA_HOME/bin:$PATH fi} function removeFromPath() {export PATH=$(echo $PATH | sed -E -e "s;:$1;;" -e "s;$1:?;;")}
```

you can use this function like `setjdk 1.8` / `setjdk 1.7`

<a id="development-contribution-useful_developer_tools--building-submodules-selectively"></a>

### Building Submodules Selectively

```bash
# build `zeppelin-web` only./mvnw clean -pl 'zeppelin-web' package -DskipTests;

# build `zeppelin-server` and its dependencies only./mvnw clean package -pl 'spark,spark-dependencies,python,markdown,zeppelin-server' --am -DskipTests

# build spark related modules with default profiles./mvnw clean package -pl 'spark,spark-dependencies,zeppelin-server' --am -DskipTests

# build spark related modules with profiles: scala 2.13, spark 3.5./mvnw clean package -Pspark-scala-2.13 -Pspark-3.5 \ -pl 'spark,spark-dependencies,zeppelin-server' --am -DskipTests

# build `zeppelin-server` and `markdown` with dependencies./mvnw clean package -pl 'markdown,zeppelin-server' --am -DskipTests
```

<a id="development-contribution-useful_developer_tools--running-individual-tests"></a>

### Running Individual Tests

```bash
# run the `HeliumBundleFactoryTest` test class./mvnw test -pl 'zeppelin-server' --am -DfailIfNoTests=false -Dtest=HeliumBundleFactoryTest
```

<a id="development-contribution-useful_developer_tools--running-selenium-tests"></a>

### Running Selenium Tests

Make sure that Zeppelin instance is started to execute integration tests (= selenium tests).

```bash
# run the `SparkParagraphIT` test class
TEST_SELENIUM="true" ./mvnw test -pl 'zeppelin-server' --am \
-DfailIfNoTests=false -Dtest=SparkParagraphIT

# run the `testSqlSpark` test function only in the `SparkParagraphIT` class
# but note that, some test might be dependent on the previous tests
TEST_SELENIUM="true" ./mvnw test -pl 'zeppelin-server' --am \
-DfailIfNoTests=false -Dtest=SparkParagraphIT#testSqlSpark
```

---

---

<a id="development-contribution-how_to_contribute_code"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/contribution/how_to_contribute_code.html -->

<!-- page_index: 84 -->

<a id="development-contribution-how_to_contribute_code--contributing-to-apache-zeppelin-code"></a>

# Contributing to Apache Zeppelin ( Code )

> **NOTE :** Apache Zeppelin is an [Apache2 License](http://www.apache.org/licenses/LICENSE-2.0.html) Software.
> Any contributions to Zeppelin (Source code, Documents, Image, Website) means you agree with license all your contributions as Apache2 License.

<a id="development-contribution-how_to_contribute_code--setting-up"></a>

## Setting up

Here are some tools you will need to build and test Zeppelin.

<a id="development-contribution-how_to_contribute_code--software-configuration-management-scm"></a>

#### Software Configuration Management ( SCM )

Since Zeppelin uses Git for it's SCM system, you need git client installed in your development machine.

<a id="development-contribution-how_to_contribute_code--integrated-development-environment-ide"></a>

#### Integrated Development Environment ( IDE )

You are free to use whatever IDE you prefer, or your favorite command line editor.

<a id="development-contribution-how_to_contribute_code--build-tools"></a>

#### Build Tools

To build the code, install

- Java 11

<a id="development-contribution-how_to_contribute_code--getting-the-source-code"></a>

## Getting the source code

First of all, you need Zeppelin source code. The official location of Zeppelin is <https://gitbox.apache.org/repos/asf/zeppelin.git>.

<a id="development-contribution-how_to_contribute_code--git-access"></a>

### git access

Get the source code on your development machine using git.

```bash
git clone git://gitbox.apache.org/repos/asf/zeppelin.git zeppelin
```

You may also want to develop against a specific branch. For example, for branch-0.12

```bash
git clone -b branch-0.12 git://gitbox.apache.org/repos/asf/zeppelin.git zeppelin
```

Apache Zeppelin follows [Fork & Pull](https://github.com/sevntu-checkstyle/sevntu.checkstyle/wiki/Development-workflow-with-Git:-Fork,-Branching,-Commits,-and-Pull-Request) as a source control workflow.
If you want to not only build Zeppelin but also make any changes, then you need to fork [Zeppelin github mirror repository](https://github.com/apache/zeppelin) and make a pull request.

Before making a pull request, please take a look [Contribution Guidelines](http://zeppelin.apache.org/contribution/contributions.html).

<a id="development-contribution-how_to_contribute_code--build"></a>

### Build

```bash
./mvnw install
```

To skip test

```bash
./mvnw install -DskipTests
```

To build with specific spark / hadoop version

```bash
./mvnw install -Dspark.version=x.x.x -Dhadoop.version=x.x.x
```

For the further

<a id="development-contribution-how_to_contribute_code--run-zeppelin-server-in-development-mode"></a>

### Run Zeppelin server in development mode

<a id="development-contribution-how_to_contribute_code--option-1-command-line"></a>

#### Option 1 - Command Line

1. Copy the `conf/zeppelin-site.xml.template` to `zeppelin-server/src/main/resources/zeppelin-site.xml` and change the configurations in this file if required
2. Run the following command

```bash
cd zeppelin-server
HADOOP_HOME=YOUR_HADOOP_HOME JAVA_HOME=YOUR_JAVA_HOME \
./mvnw exec:java -Dexec.mainClass="org.apache.zeppelin.server.ZeppelinServer" -Dexec.args=""
```

<a id="development-contribution-how_to_contribute_code--option-2-daemon-script"></a>

#### Option 2 - Daemon Script

> **Note:** Make sure you first run

```bash
./mvnw clean install -DskipTests
```

in your zeppelin root directory, otherwise your server build will fail to find the required dependencies in the local repro.

or use daemon script

```bash
bin/zeppelin-daemon start
```

Server will be run on <http://localhost:8080>.

<a id="development-contribution-how_to_contribute_code--option-3-ide"></a>

#### Option 3 - IDE

1. Copy the `conf/zeppelin-site.xml.template` to `zeppelin-server/src/main/resources/zeppelin-site.xml` and change the configurations in this file if required
2. `ZeppelinServer.java` Main class

<a id="development-contribution-how_to_contribute_code--generating-thrift-code"></a>

### Generating Thrift Code

Some portions of the Zeppelin code are generated by [Thrift](http://thrift.apache.org). For most Zeppelin changes, you don't need to worry about this. But if you modify any of the Thrift IDL files (e.g. zeppelin-interpreter/src/main/thrift/\*.thrift), then you also need to regenerate these files and submit their updated version as part of your patch.

To regenerate the code, install **thrift-0.9.2** and then run the following command to generate thrift code.

```bash
cd <zeppelin_home>/zeppelin-interpreter/src/main/thrift
./genthrift.sh
```

<a id="development-contribution-how_to_contribute_code--run-selenium-test"></a>

### Run Selenium test

Zeppelin has [set of integration tests](https://github.com/apache/zeppelin/tree/master/zeppelin-integration/src/test/java/org/apache/zeppelin/integration) using Selenium. To run these test, first build and run Zeppelin and make sure Zeppelin is running on port 8080. Then you can run test using following command

```bash
TEST_SELENIUM=true ./mvnw test -Dtest=[TEST_NAME] -DfailIfNoTests=false \
-pl 'zeppelin-interpreter,zeppelin-zengine,zeppelin-server'
```

For example, to run [ParagraphActionIT](https://github.com/apache/zeppelin/blob/master/zeppelin-integration/src/test/java/org/apache/zeppelin/integration/ParagraphActionsIT.java),

```bash
TEST_SELENIUM=true ./mvnw test -Dtest=ParagraphActionsIT -DfailIfNoTests=false \
-pl 'zeppelin-interpreter,zeppelin-zengine,zeppelin-server'
```

You'll need Firefox web browser installed in your development environment.

<a id="development-contribution-how_to_contribute_code--where-to-start"></a>

## Where to Start

You can find issues for [beginner & newbie](https://issues.apache.org/jira/browse/ZEPPELIN-981?jql=project%20%3D%20ZEPPELIN%20AND%20labels%20in%20(beginner%2C%20newbie))

<a id="development-contribution-how_to_contribute_code--stay-involved"></a>

## Stay involved

Contributors should join the Zeppelin mailing lists.

- [dev@zeppelin.apache.org](http://mail-archives.apache.org/mod_mbox/zeppelin-dev/) is for people who want to contribute code to Zeppelin. [subscribe](mailto:dev-subscribe@zeppelin.apache.org?subject=send%20this%20email%20to%20subscribe), [unsubscribe](mailto:dev-unsubscribe@zeppelin.apache.org?subject=send%20this%20email%20to%20unsubscribe), [archives](http://mail-archives.apache.org/mod_mbox/zeppelin-dev/)

If you have any issues, create a ticket in [JIRA](https://issues.apache.org/jira/browse/ZEPPELIN).

---

---

<a id="development-contribution-how_to_contribute_website"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/development/contribution/how_to_contribute_website.html -->

<!-- page_index: 85 -->

<a id="development-contribution-how_to_contribute_website--contributing-to-apache-zeppelin-website"></a>

# Contributing to Apache Zeppelin ( Website )

This page will give you an overview of how to build and contribute to the documentation of Apache Zeppelin.
The online documentation at [zeppelin.apache.org](https://zeppelin.apache.org/docs/latest/) is also generated from the files found here.

> **NOTE :** Apache Zeppelin is an [Apache2 License](http://www.apache.org/licenses/LICENSE-2.0.html) Software.
> Any contributions to Zeppelin (Source code, Documents, Image, Website) means you agree with license all your contributions as Apache2 License.

<a id="development-contribution-how_to_contribute_website--getting-the-source-code"></a>

## Getting the source code

First of all, you need Zeppelin source code. The official location of Zeppelin is <https://gitbox.apache.org/repos/asf/zeppelin.git>.
Documentation website is hosted in 'master' branch under `/docs/` dir.

<a id="development-contribution-how_to_contribute_website--git-access"></a>

### git access

First of all, you need the website source code. The official location of mirror for Zeppelin is <https://gitbox.apache.org/repos/asf/zeppelin.git>.
Get the source code on your development machine using git.

```bash
git clone git://gitbox.apache.org/repos/asf/zeppelin.git
cd docs
```

Apache Zeppelin follows [Fork & Pull](https://github.com/sevntu-checkstyle/sevntu.checkstyle/wiki/Development-workflow-with-Git:-Fork,-Branching,-Commits,-and-Pull-Request) as a source control workflow.
If you want to not only build Zeppelin but also make any changes, then you need to fork [Zeppelin github mirror repository](https://github.com/apache/zeppelin) and make a pull request.

<a id="development-contribution-how_to_contribute_website--build"></a>

### Build

You'll need to install some prerequisites to build the code. Please check [Build documentation](https://github.com/apache/zeppelin/blob/master/docs/README.md#build-documentation) section in [docs/README.md](https://github.com/apache/zeppelin/blob/master/docs/README.md).

<a id="development-contribution-how_to_contribute_website--run-website-in-development-mode"></a>

### Run website in development mode

While you're modifying website, you might want to see preview of it. Please check [Run website](https://github.com/apache/zeppelin/blob/master/docs/README.md#run-website) section in [docs/README.md](https://github.com/apache/zeppelin/blob/master/docs/README.md).
Then you'll be able to access it on <http://localhost:4000> with your web browser.

<a id="development-contribution-how_to_contribute_website--making-a-pull-request"></a>

### Making a Pull Request

When you are ready, just make a pull-request.

<a id="development-contribution-how_to_contribute_website--alternative-way"></a>

## Alternative way

You can directly edit `.md` files in `/docs/` directory at the web interface of github and make pull-request immediately.

<a id="development-contribution-how_to_contribute_website--stay-involved"></a>

## Stay involved

Contributors should join the Zeppelin mailing lists.

- [dev@zeppelin.apache.org](http://mail-archives.apache.org/mod_mbox/zeppelin-dev/) is for people who want to contribute code to Zeppelin. [subscribe](mailto:dev-subscribe@zeppelin.apache.org?subject=send%20this%20email%20to%20subscribe), [unsubscribe](mailto:dev-unsubscribe@zeppelin.apache.org?subject=send%20this%20email%20to%20unsubscribe), [archives](http://mail-archives.apache.org/mod_mbox/zeppelin-dev/)

If you have any issues, create a ticket in [JIRA](https://issues.apache.org/jira/browse/ZEPPELIN).

---

---

<a id="index"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/ -->

<!-- page_index: 86 -->

<a id="index--what-is-apache-zeppelin"></a>

# What is Apache Zeppelin?

Multi-purpose notebook which supports

20+ language backends

- Data Ingestion
- Data Discovery
- Data Transformation
- Data Analytics
- Data Visualization & Collaboration

![](assets/images/notebook_5c068925ee0a8ddf.png)

<a id="index--documentation"></a>

## Documentation

<a id="index--quick-start"></a>

#### Quick Start

- [Install](#quickstart-install) for basic instructions on installing Apache Zeppelin
- [Explore UI](#quickstart-explore_ui): basic components of Apache Zeppelin home
- [Tutorial](#quickstart-tutorial)
- [Spark with Zeppelin](#quickstart-spark_with_zeppelin)
- [SQL with Zeppelin](#quickstart-sql_with_zeppelin)
- [Python with Zeppelin](#quickstart-python_with_zeppelin)

<a id="index--usage"></a>

#### Usage

- Dynamic Form
  - [What is Dynamic Form](#usage-dynamic_form-intro): a step by step guide for creating dynamic forms
- Display System
  - [Text Display (`%text`)](#usage-display_system-basic--text)
  - [HTML Display (`%html`)](#usage-display_system-basic--html)
  - [Table Display (`%table`)](#usage-display_system-basic--table)
  - [Network Display (`%network`)](#usage-display_system-basic--network)
  - [Angular Display using Backend API (`%angular`)](#usage-display_system-angular_backend)
  - [Angular Display using Frontend API (`%angular`)](#usage-display_system-angular_frontend)
- Interpreter
  - [Overview](#usage-interpreter-overview): what is interpreter group? how can you set interpreters in Apache Zeppelin?
  - [User Impersonation](#usage-interpreter-user_impersonation) when you want to run interpreter as end user
  - [Interpreter Binding Mode](#usage-interpreter-interpreter_binding_mode) when you want to manage separate interpreter contexts
  - [Dependency Management](#usage-interpreter-dependency_management) when you include external libraries to interpreter
  - [Installing Interpreters](#usage-interpreter-installation): Install not only community managed interpreters but also 3rd party interpreters
  - [Execution Hooks](#usage-interpreter-execution_hooks) to specify additional code to be executed by an interpreter at pre and post-paragraph code execution
- Other Features:
  - [Publishing Paragraphs](#usage-other_features-publishing_paragraphs) results into your external website
  - [Personalized Mode](#usage-other_features-personalized_mode)
  - [Customizing Zeppelin Homepage](#usage-other_features-customizing_homepage) with one of your notebooks
  - [Notebook actions](#usage-other_features-notebook_actions)
  - [Zeppelin-Context](#usage-other_features-zeppelin_context)
- REST API: available REST API list in Apache Zeppelin
  - [Interpreter API](#usage-rest_api-interpreter)
  - [Zeppelin Server API](#usage-rest_api-zeppelin_server)
  - [Notebook API](#usage-rest_api-notebook)
  - [Notebook Repository API](#usage-rest_api-notebook_repository)
  - [Configuration API](#usage-rest_api-configuration)
  - [Credential API](#usage-rest_api-credential)
  - [Helium API](#usage-rest_api-helium)
- Zeppelin SDK: Java API of Zeppelin Client
  - [Client API](#usage-zeppelin_sdk-client_api)
  - [Session API](#usage-zeppelin_sdk-session_api)

<a id="index--setup"></a>

#### Setup

- Basics
  - [How to Build Zeppelin](#setup-basics-how_to_build)
  - [Manage Zeppelin with systemd](#setup-basics-systemd)
  - [Multi-user Support](#setup-basics-multi_user_support)
- Deployment
  - [Spark Cluster Mode: Standalone](#setup-deployment-spark_cluster_mode--spark-standalone-mode)
  - [Spark Cluster Mode: YARN](#setup-deployment-spark_cluster_mode--spark-on-yarn-mode)
  - [Spark Cluster Mode: Mesos](#setup-deployment-spark_cluster_mode--spark-on-mesos-mode)
  - [Zeppelin with Flink and Spark Cluster](#setup-deployment-flink_and_spark_cluster)
  - [Zeppelin on CDH](#setup-deployment-cdh)
  - [Zeppelin on VM: Vagrant](#setup-deployment-virtual_machine)
- Security: available security support in Apache Zeppelin
  - [HTTP Basic Auth using NGINX](#setup-security-authentication_nginx)
  - [Shiro Authentication](#setup-security-shiro_authentication)
  - [Notebook Authorization](#setup-security-notebook_authorization)
  - [Data Source Authorization](#setup-security-datasource_authorization)
  - [HTTP Security Headers](#setup-security-http_security_headers)
- Notebook Storage: a guide about saving notebooks to external storage
  - [Git Storage](https://zeppelin.apache.org/docs/0.12.0/setup/storage/storage.html#notebook-storage-in-local-git-repository)
  - [S3 Storage](https://zeppelin.apache.org/docs/0.12.0/setup/storage/storage.html#notebook-storage-in-s3)
  - [Azure Storage](https://zeppelin.apache.org/docs/0.12.0/setup/storage/storage.html#notebook-storage-in-azure)
  - [Google Cloud Storage](https://zeppelin.apache.org/docs/0.12.0/setup/storage/storage.html#notebook-storage-in-gcs)
  - [MongoDB Storage](https://zeppelin.apache.org/docs/0.12.0/setup/storage/storage.html#notebook-storage-in-mongodb)
- Operation
  - [Configuration](#setup-operation-configuration): lists for Apache Zeppelin
  - [Monitoring](#setup-operation-monitoring): monitoring instructions for Apache Zeppelin
  - [Proxy Setting](#setup-operation-proxy_setting)
  - [Upgrading](#setup-operation-upgrading): a manual procedure of upgrading Apache Zeppelin version
  - [Trouble Shooting](https://zeppelin.apache.org/docs/0.12.0/setup/operation/trouble_shooting.html)

<a id="index--developer-guide"></a>

#### Developer Guide

- Extending Zeppelin
  - [Writing Zeppelin Interpreter](#development-writing_zeppelin_interpreter)
  - [Helium: Overview](#development-helium-overview)
  - [Helium: Writing Application](#development-helium-writing_application)
  - [Helium: Writing Spell](#development-helium-writing_spell)
  - [Helium: Writing Visualization: Basic](#development-helium-writing_visualization_basic)
  - [Helium: Writing Visualization: Transformation](#development-helium-writing_visualization_transformation)
- Contributing to Zeppelin
  - [How to Build Zeppelin](#setup-basics-how_to_build)
  - [Useful Developer Tools](#development-contribution-useful_developer_tools)
  - [How to Contribute (code)](#development-contribution-how_to_contribute_code)
  - [How to Contribute (website)](#development-contribution-how_to_contribute_website)

<a id="index--available-interpreters"></a>

#### Available Interpreters

- [Alluxio](#interpreter-alluxio)
- [BigQuery](#interpreter-bigquery)
- [Cassandra](#interpreter-cassandra)
- [Elasticsearch](#interpreter-elasticsearch)
- [Flink](#interpreter-flink)
- [Groovy](#interpreter-groovy)
- [HBase](#interpreter-hbase)
- [HDFS](#interpreter-hdfs)
- [Hive](#interpreter-hive)
- [influxDB](#interpreter-influxdb)
- [Java](#interpreter-java)
- [JDBC](#interpreter-jdbc)
- [Jupyter](#interpreter-jupyter)
- [Livy](#interpreter-livy)
- [Mahout](#interpreter-mahout)
- [Markdown](#interpreter-markdown)
- [MongoDB](#interpreter-mongodb)
- [Neo4j](#interpreter-neo4j)
- [Postgresql, HAWQ](#interpreter-postgresql)
- [Python](#interpreter-python)
- [R](#interpreter-r)
- [Shell](#interpreter-shell)
- [Spark](#interpreter-spark)
- [Sparql](#interpreter-sparql)

<a id="index--external-resources"></a>

#### External Resources

- [Mailing List](https://zeppelin.apache.org/community.html)
- [Apache Zeppelin Wiki](https://cwiki.apache.org/confluence/display/ZEPPELIN/Zeppelin+Home)
- [Stackoverflow Questions about Zeppelin (tag: `apache-zeppelin`)](http://stackoverflow.com/questions/tagged/apache-zeppelin)

---

---

<a id="setup-basics-systemd"></a>

<!-- source_url: https://zeppelin.apache.org/docs/0.12.0/setup/basics/systemd.html -->

<!-- page_index: 87 -->

<a id="setup-basics-systemd--zeppelin-and-systemd"></a>

## Zeppelin and systemd

<a id="setup-basics-systemd--unit-file-installation-deinstallation"></a>

### Unit file installation / deinstallation

This script accepts two parameters: `enable` and `disable` which, as you might have guessed, enable or disable the Zeppelin systemd unit file. Go ahead and type:

```
# ./bin/zeppelin-systemd-service.sh enable
```

This command activates the Zeppelin systemd unit file on your system.

If you wish to roll back and remove this unit file from said system, simply type:
```

<a id="setup-basics-systemd--.-bin-zeppelin-systemd-service.sh-disable"></a>



# ./bin/zeppelin-systemd-service.sh disable


```

### Manage Zeppelin using systemd commands

To start Zeppelin using systemd;
```


<a id="setup-basics-systemd--systemctl-start-zeppelin"></a>



# systemctl start zeppelin


```

To stop Zeppelin using systemd:
```


<a id="setup-basics-systemd--systemctl-stop-zeppelin"></a>



# systemctl stop zeppelin


```

To check the service health:
```


<a id="setup-basics-systemd--systemctl-status-zeppelin"></a>



# systemctl status zeppelin"


```

```

---

---
