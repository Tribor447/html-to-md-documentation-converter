---
entry_url: https://bifromq.incubator.apache.org/docs/get_started/intro/
page_count: 57
asset_count: 5
---
# Introduction
## Navigation
- [Get Started](#get_started-intro)
  - [Quick Install & Verify](#get_started-quick_install)
  - [Frequently Asked Questions](#get_started-faq)
  - [Road Map](#get_started-roadmap)
- [Installation](#installation-intro)
  - [Docker](#installation-docker)
  - [Linux](#installation-linux)
  - [Windows](#installation-windows)
  - [Install from Source](#installation-install_from_source)
  - [Configuration Convention & Migration](#installation-config_migration_between_versions)
  - [Notes on Kubernetes Deployment](#installation-nodes_on_k8s)
- [Cluster](#cluster-intro)
  - [Clustering](#cluster-clustering)
  - [Load Balancing](#cluster-loadbalance-intro)
    - [MQTT Server](#cluster-loadbalance-mqttserver)
    - [API Server](#cluster-loadbalance-apiserver)
    - [Internal RPC Server](#cluster-loadbalance-rpcserver)
    - [Stateful Server](#cluster-loadbalance-stateful-intro)
      - [Dist Worker](#cluster-loadbalance-stateful-distworker)
      - [Inbox Store](#cluster-loadbalance-stateful-inboxstore)
      - [Retain Store](#cluster-loadbalance-stateful-retainstore)
  - [Upgrade](#cluster-upgrade)
- [User Guide](#user_guide-intro)
  - [Basic MQTT Features](#user_guide-basic-intro)
    - [Connect to BifroMQ](#user_guide-basic-connect)
    - [Pub/Sub](#user_guide-basic-pubsub)
    - [Shared Subscriptions](#user_guide-basic-shared_sub)
  - [Data Integration](#user_guide-integration-intro)
  - [API Usage](#user_guide-api-intro)
    - [OpenAPI Reference](#user_guide-api-openapi)
- [Plugin](#plugin-intro)
  - [Auth Provider](#plugin-auth_provider)
  - [Client Balancer](#plugin-client_balancer)
  - [Event Collector](#plugin-event_collector)
  - [Resource Throttler](#plugin-resource_throttler)
  - [Setting Provider](#plugin-setting_provider-intro)
    - [Tenant-level Settings](#plugin-setting_provider-tenantsetting)
  - [Plugin Practice and Notice](#plugin-plugin_practice)
- [SPI](#spi-intro)
- [Administration](#admin_guide-overview)
  - [Configuration](#admin_guide-configuration-intro)
    - [Config File Manual](#admin_guide-configuration-config_file_manual)
    - [System Properties](#admin_guide-configuration-bifromq_sys_props)
    - [Configuration Printing](#admin_guide-configuration-configs_print)
  - [Tuning](#admin_guide-tuning-intro)
    - [Linux Kernel Tuning](#admin_guide-tuning-os_tuning_linux)
  - [Observability](#admin_guide-observability-intro)
    - [Logging](#admin_guide-observability-logging)
    - [Metrics](#admin_guide-observability-metrics-intro)
      - [Tenant-level Metrics](#admin_guide-observability-metrics-tenantmetrics)
    - [Events](#admin_guide-observability-events)
  - [Security](#admin_guide-security-intro)
- [Benchmark](#benchmark-overview)
- [Contribution Guide](#contribution_guide-intro)
  - [Code Contribution](#contribution_guide-code_contribution)
  - [Code Review](#contribution_guide-code_review)
  - [Documentation Contribution](#contribution_guide-documentation_contribution)

## Content

<a id="get_started-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/get_started/intro/ -->

<!-- page_index: 1 -->

# Introduction

Version: 4.0.0-incubating

# Introduction

BifroMQ (Incubating) is a Java-based, high-performance, distributed MQTT broker implementation that seamlessly integrates native multi-tenancy support. It is designed to facilitate the building of large-scale IoT device connections and messaging
systems.

<a id="get_started-intro--origin-of-the-name"></a>

## Origin of the Name

`BifroMQ` derives its name from the Norse mythological Bifröst, a rainbow bridge that connects Midgard (the realm of humans) and Asgard (the domain of gods). Like Bifröst, BifroMQ serves as a flexible and sturdy bridge, linking different
systems or applications to enable communication through message exchange. This aligns with the core function of MQTT middleware, which is to manage and accelerate message delivery in distributed systems.

The robustness of Bifröst symbolizes BifroMQ's stability and reliability, while its flexibility signifies BifroMQ's scalability and adaptability. In a nutshell, "BifroMQ" epitomizes resilient, adaptable MQTT middleware that interconnects
various systems or applications.

<a id="get_started-intro--features-list"></a>

## Features List

- Full support for MQTT 3.1, 3.1.1 and 5.0 features over TCP, TLS, WS, WSS.
- Native support for multi-tenancy, resource sharing, and workload isolation.
- Built-in distributed storage engine optimized for MQTT workloads, with no third-party middleware dependencies.
- Extension mechanism for supporting:
  - Authentication/Authorization.
  - Tenant-level Client Balancing.
  - Tenant-level Resource Throttling.
  - Tenant-level Runtime Setting.
  - Event & Monitoring.

<a id="get_started-intro--community"></a>

## Community

<a id="get_started-intro--issue-tracker"></a>

#### **Issue Tracker**

We use GitHub [Issues](https://github.com/apache/bifromq/issues) for tracking requests and bugs. Feel free to open an issue if you have any questions or problems.

<a id="get_started-intro--mailing-list"></a>

#### **Mailing List**

We use Apache mailing lists for asynchronous discussion and announcements. Please choose the appropriate list for your needs:

- **`commits@bifromq.apache.org`** – Receives automated commit logs and code changes.
- **`dev@bifromq.apache.org`** – Used for general development discussions, proposals, questions, and community communication.

Follow these [steps](https://bifromq.incubator.apache.org/community/#how-to-subscribe) to subscribe or unsubscribe.

<a id="get_started-intro--discord"></a>

#### **Discord**

We also use [Discord](https://discord.gg/Pfs3QRadRB) for real-time chat and community discussion. Join our server to ask questions, share ideas, and stay up-to-date with the latest project progress. Please adhere to the Apache Code of Conduct while participating.

- [Origin of the Name](#get_started-intro--origin-of-the-name)
- [Features List](#get_started-intro--features-list)
- [Community](#get_started-intro--community)

---

<a id="get_started-quick_install"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/get_started/quick_install/ -->

<!-- page_index: 2 -->

# Quick Install

Version: 4.0.0-incubating

# Quick Install

For a rapid setup, Docker is recommended:

```bash
docker run -d --name bifromq -p 1883:1883 apache/bifromq:4.0.0-incubating
```

For further installation alternatives and comprehensive details, refer to [Installation](#installation-intro).

# Quick Verify

Below are the steps to quickly verify the basic MQTT functionality of BifroMQ using MQTTX.

1. Visit <https://mqttx.app/> to download MQTTX and install it.
2. Open MQTTX and click on **New Connection** (the “+” sign on the left sidebar) to create a new connection configuration.

   ![new connection screenshot](assets/images/newconn-5744d494a22ab7fd3231d5ae1435d296_daf3e2b196bde152.jpg)
3. Fill in the required fields:

   - **Name**: Any descriptive name of your choice.
   - **ClientID**: Can be set manually or generated randomly. Must consist of "a–z", "0–9", "\_", "-", ≤128 bytes, UTF8 encoded, and unique.
   - **Host**: The connection address, including protocol prefix:
     - `mqtt://<HOST>` for TCP
     - `mqtts://<HOST>` for TLS/SSL
     - `wss://<HOST>` for WebSocket Secure
   - **Port**: Select based on protocol:
     - TCP: `1883`
     - TLS/SSL: `1884`
     - WSS: `443`
   - **Username & Password**: Provide credentials if configured; otherwise leave blank for test environments.
   - **MQTT Version**: Choose from 3.1, 3.1.1, or 5.0.
4. After configuring, click **Connect** in the top right corner.
5. **Subscribe** to a topic: click **New Subscription**, enter the topic in the dialog, and confirm.

   ![subscribe screenshot](assets/images/subscribe-a7e73104ace819a62661347eab598b1f_d55a942b0450ede8.jpg)
6. **Publish** a message: in the send/receive interface, enter the same topic, select QoS 0, type your message, and click **Send**.

   ![publish screenshot](assets/images/publish-15956d94297e1bfbac726fba2d5db831_87150b9d5502c22a.jpg)
7. You should see your published message appear in the interface.

---

<a id="get_started-faq"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/get_started/faq/ -->

<!-- page_index: 3 -->

# Frequently Asked Questions

Version: 4.0.0-incubating

# Frequently Asked Questions

<a id="get_started-faq--what-versions-of-the-mqtt-protocol-are-supported-by-bifromq"></a>

## What versions of the MQTT protocol are supported by BifroMQ?

BifroMQ provides comprehensive support for the following MQTT protocol versions: v3.1, v3.1.1, and v5.0. This versatility ensures that BifroMQ can accommodate a wide range of IoT devices and applications, adhering to different protocol standards. Additionally, BifroMQ allows for dynamic control of protocol capabilities at the tenant level during runtime, offering tailored connectivity options to meet specific tenant requirements.

<a id="get_started-faq--what-are-the-java-version-requirements-for-bifromq"></a>

## What are the Java version requirements for BifroMQ?

The Java version requirements for BifroMQ can be divided into two aspects:

- **BifroMQ runtime environment**: BifroMQ itself requires JDK 17 or higher for operation.
- **BifroMQ plugin development**: For developing BifroMQ plugins, there's no enforced requirement for a specific Java language version or JDK version. However, plugin developers need to ensure their plugins function properly in higher Java environments. To prevent compatibility issues, we suggest keeping the plugin's runtime environment consistent with BifroMQ's.

<a id="get_started-faq--does-bifromq-include-a-built-in-rule-engine"></a>

## Does BifroMQ include a built-in rule engine?

Unlike other products or projects providing MQTT protocol capabilities, BifroMQ's primary aim is to serve as a high-performance, multi-tenant, distributed middleware implementing the standard MQTT protocol. "Rule engines" are not part of the MQTT protocol specification and hence are not included in BifroMQ.
BifroMQ focuses on standard integrations with upstream and downstream systems, while “rule engines” represent additional functionality that can be implemented externally. We welcome contributions to a community-driven side project for rule engine implementations,allowing developers to build and share rule engine integrations with BifroMQ.

<a id="get_started-faq--how-to-use-bifromq-for-data-integration"></a>

## How to use BifroMQ for data integration?

Integration with downstream systems should follow a **decoupled** and **dependency-inverted** approach. We recommend leveraging MQTT 5.0’s built-in shared subscription feature, which allows downstream consumers to control routing rules directly.

To bring this capability to earlier clients, BifroMQ has **backported shared subscriptions** into the MQTT 3.1.1 protocol, ensuring a consistent, standardized integration model across versions.

Additionally, we provide an **ordered shared subscription** mode for use cases that require strict message ordering. See the documentation for details: [Ordered Shared Subscriptions](#user_guide-basic-shared_sub).

<a id="get_started-faq--what-data-persistence-is-bifromqs-built-in-storage-engine-primarily-used-for"></a>

## What data persistence is BifroMQ's built-in storage engine primarily used for?

BifroMQ's built-in storage engine is mainly used for the persistence of SessionState required by the MQTT protocol to be persistent and Retain Topic messages. This helps prevent loss of session state during a broker restart or crash. It's noteworthy that the persistence engine is not directly related to the message's QoS in most cases. For instance, when an MQTT connection starts a persistent session, offline QoS0 subscription messages will still be persisted until the session is restored and pushing is completed.

<a id="get_started-faq--why-doesnt-bifromq-have-a-management-web-interfacecli"></a>

## Why doesn't BifroMQ have a management Web interface/CLI?

BifroMQ is designed as a core middleware component to be embedded within broader business systems. Management logic is therefore exposed for integration rather than provided as a standalone Web UI or CLI. The project itself does not include built-in management consoles; instead, it offers the following APIs and plugins to enable external systems to implement management capabilities:

- **[API](#user_guide-api-intro)**: Broker-side control logic, such as forcing disconnection.
- **[Metrics](#admin_guide-observability-metrics-intro)**: Runtime metrics that can be consumed by existing monitoring systems.
- **[AuthProvider Plugin](#plugin-auth_provider)**: Enable customized authentication and authorizaiton
- **[ClientBalancer Plugin](#plugin-client_balancer)**: Implements an active client‐balancing strategy, dynamically distributing incoming client connections across broker instances to ensure even load distribution.
- **[EventCollector Plugin](#plugin-event_collector)**: Emits operational events for custom Event Sourcing logic (e.g., connection counts, online/offline).
- **[ResourceThrottler Plugin](#plugin-resource_throttler)**: Controls tenant-level resource usage.
- **[SettingProvider Plugin](#plugin-setting_provider-intro)**: Adjusts tenant-level runtime settings.

As with rule-engine support, we welcome community-driven side projects to build Web UIs, CLI tools, or other management interfaces leveraging these integration points.

- [What versions of the MQTT protocol are supported by BifroMQ?](#get_started-faq--what-versions-of-the-mqtt-protocol-are-supported-by-bifromq)
- [What are the Java version requirements for BifroMQ?](#get_started-faq--what-are-the-java-version-requirements-for-bifromq)
- [Does BifroMQ include a built-in rule engine?](#get_started-faq--does-bifromq-include-a-built-in-rule-engine)
- [How to use BifroMQ for data integration?](#get_started-faq--how-to-use-bifromq-for-data-integration)
- [What data persistence is BifroMQ's built-in storage engine primarily used for?](#get_started-faq--what-data-persistence-is-bifromqs-built-in-storage-engine-primarily-used-for)
- [Why doesn't BifroMQ have a management Web interface/CLI?](#get_started-faq--why-doesnt-bifromq-have-a-management-web-interfacecli)

---

<a id="get_started-roadmap"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/get_started/roadmap/ -->

<!-- page_index: 4 -->

# Road Map

Version: 4.0.0-incubating

# Road Map

This roadmap is organized into two categories:

- **Core BifroMQ Project**: Enhancements and new features within the main broker codebase, focusing on performance, resource efficiency, and protocol extensibility.
- **Satellite Projects**: Community-driven side projects that extend and complement the core broker with additional tooling, UIs, testing suites, and various plugin implementations.

The following lists are highlights of some directions (but not limited to):

<a id="get_started-roadmap--core-bifromq-project"></a>

## Core BifroMQ Project

1. **Runtime Efficiency**
   Continuously improve runtime performance and optimize memory usage.
2. **Native Image Support**
   Enable native image builds (e.g., GraalVM) to run BifroMQ in resource-constrained environments.
3. **Integration Extensibility**
   Incorporate user feedback to expand additional integration and customization extension points.
4. **Storage Engine Optimization**
   Continuously tune the built-in storage engine for different MQTT workload patterns.
5. **Efficient RPC Mechanism**
   Explore more efficient internal RPC implementations to better handle varying message payload sizes across use cases.

<a id="get_started-roadmap--satellite-projects"></a>

## Satellite Projects

1. **Website Building**
   Contributions of translations, corrections, and additional content are welcome.
2. **General Rule Engine**
   A community-driven, generic MQTT broker rule engine for flexible message routing and processing.
3. **BifroMQ UI (Web & CLI)**
   A side project to build web-based dashboards and command-line tools for managing and monitoring BifroMQ.
4. **MQTT Load Testing Suite**
   A toolkit to simulate real-world MQTT workloads and stress-test BifroMQ deployments.
5. **Common Scenario Plugins**
   Prebuilt plugins for typical use cases, such as database-backed authentication/authorization and event diagnostics tools.
6. **Deployment Utilities**
   Various scripts/tools for deploying and operating in various environment, e.g. VM, Kubernetes

- [Core BifroMQ Project](#get_started-roadmap--core-bifromq-project)
- [Satellite Projects](#get_started-roadmap--satellite-projects)

---

<a id="installation-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/installation/intro/ -->

<!-- page_index: 5 -->

# Installation Overview

Version: 4.0.0-incubating

# Installation Overview

<a id="installation-intro--prerequisites"></a>

## Prerequisites

BifroMQ requires **Java 17** or higher for its operation. Ensure your Java runtime environment is updated to meet these requirements before proceeding with the BifroMQ installation.

<a id="installation-intro--installation-directory-structure"></a>

## Installation Directory Structure

Upon installation, BifroMQ organizes its files within the following directory structure:

<table><thead><tr><th>Directory</th><th>Description</th></tr></thead><tbody><tr><td><code>bin</code></td><td>Executable scripts for starting and managing BifroMQ.</td></tr><tr><td><code>conf</code></td><td>Configuration files necessary for customizing BifroMQ operations.</td></tr><tr><td><code>lib</code></td><td>Program libs for running BifroMQ.</td></tr><tr><td><code>plugins</code></td><td>BifroMQ plugins in <a class="" href="https://pf4j.org" rel="noopener noreferrer" target="_blank">pf4j</a> compatible format.</td></tr><tr><td><code>data</code></td><td>User's persistent data.</td></tr><tr><td><code>logs</code></td><td>Log files.</td></tr></tbody></table>
<a id="installation-intro--running-bifromq"></a>

## Running BifroMQ

The startup script for BifroMQ recognizes several environment variables that allow for customization and optimization of its runtime environment:

<table><thead><tr><th>Environment Variable</th><th>Description</th></tr></thead><tbody><tr><td><code>LOG_DIR</code></td><td>Specifies the directory where BifroMQ should store its log files. Defaults to <code>./logs</code> if unset.</td></tr><tr><td><code>DATA_DIR</code></td><td>Determines the directory for storing BifroMQ data. Defaults to <code>./data</code> if unset.</td></tr><tr><td><code>JAVA_HOME</code></td><td>Specifies the path to the Java Runtime Environment (JRE) that BifroMQ should use.</td></tr><tr><td><code>MEM_LIMIT</code></td><td>Limits the maximum amount of memory that BifroMQ can use.</td></tr><tr><td><code>JVM_PERF_OPTS</code></td><td>Custom JVM performance options for tuning the JVM instance running BifroMQ.</td></tr><tr><td><code>JVM_GC_OPTS</code></td><td>Garbage Collection (GC) options to optimize memory management for BifroMQ.</td></tr><tr><td><code>JVM_HEAP_OPTS</code></td><td>Specifies JVM heap size and other memory settings directly impacting BifroMQ's performance.</td></tr><tr><td><code>EXTRA_JVM_OPTS</code></td><td>Additional JVM options that users may want to pass to customize the BifroMQ runtime environment.</td></tr><tr><td><code>JVM_DEBUG</code></td><td>Enables debugging options for the JVM, useful for development and troubleshooting.</td></tr><tr><td><code>JAVA_DEBUG_PORT</code></td><td>When <code>JVM_DEBUG</code> is enabled, sets the port for the JVM debugger to attach to.</td></tr></tbody></table>

- [Prerequisites](#installation-intro--prerequisites)
- [Installation Directory Structure](#installation-intro--installation-directory-structure)
- [Running BifroMQ](#installation-intro--running-bifromq)

---

<a id="installation-docker"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/installation/docker/ -->

<!-- page_index: 6 -->

# Docker

Version: 4.0.0-incubating

# Docker

<a id="installation-docker--prerequisites"></a>

## Prerequisites

- [Docker](https://www.docker.com/) is installed.
- You have permission to use port 1883, and the port is available. If you do not have permission, please change to the corresponding port.

<a id="installation-docker--docker-command"></a>

## Docker Command

Run the following command, which will run Apache BifroMQ within a container as the Linux user `bifromq`.

```bash
docker run -d --name bifromq -p 1883:1883 apache/bifromq:4.0.0-incubating
```

<a id="installation-docker--memory-constraints"></a>

## Memory Constraints

By default, upon Apache BifroMQ process initiation, it dynamically computes the relevant JVM parameters based on the physical memory of the hosting server. However, when launched within a containerized environment, it introspects the host
machine's physical memory, potentially causing conflicts with Docker or container-imposed memory constraints, consequently leading to the premature termination of the container.

To circumvent such challenges, it is advisable to proactively delimit the container's memory consumption and convey these limitations to the container runtime via environmental variables. During the startup of BifroMQ, priority is given to
the calculation of JVM parameters based on the `MEM_LIMIT` environmental variable. A specific illustration is provided below:

```bash
docker run -d -m 10G -e MEM_LIMIT='10737418240'--name bifromq -p 1883:1883 apache/bifromq:4.0.0-incubating
```

***Note: The unit of MEM\_LIMIT is in bytes.***

Going a step further, it is possible to proactively configure the JVM heap memory and directly transmit it to the container runtime for utilization by BifroMQ. A specific illustration is provided below:

```bash
docker run -d -m 10G -e JVM_HEAP_OPTS='-Xms2G -Xmx4G -XX:MetaspaceSize=128m -XX:MaxMetaspaceSize=500m -XX:MaxDirectMemorySize=1G' --name bifromq -p 1883:1883 apache/bifromq:4.0.0-incubating
```

You can build an Apache BifroMQ cluster using Docker Compose on a single host for development and testing. Suppose you want to create a cluster with three nodes: node1, node2, and node3. The directory structure should be as follows:

```text
|- docker-compose.yml
|- node1
|- node2
|- node3
```

Each node should have a configuration file, it is defined as follows:

```yml
clusterConfig:
  env: "Test"
  host: bifromq-node1 # Change this to bifromq-node2 for node2 and bifromq-node3 for node3
  port: 8899
  seedEndpoints: "bifromq-node1:8899,bifromq-node2:8899,bifromq-node3:8899"
```

The `docker-compose.yml` file defines the services for the three nodes:

```yaml
services:
bifromq-node1:
  image: apache/bifromq:4.0.0-incubating
  container_name: bifromq-node1
  volumes:
    - ./node1/standalone.yml:/home/bifromq/conf/standalone.yml
  ports:
    - "1883:1883"
  environment:
    - MEM_LIMIT=10737418240 # Adjust the value according to the actual host configuration.
  networks:
    - bifromq-net

bifromq-node2:
  image: apache/bifromq:4.0.0-incubating
  container_name: bifromq-node2
  volumes:
    - ./node2/standalone.yml:/home/bifromq/conf/standalone.yml
  ports:
    - "1884:1883"
  environment:
    - MEM_LIMIT=2147483648
  networks:
    - bifromq-net

bifromq-node3:
  image: apache/bifromq:4.0.0-incubating
  container_name: bifromq-node3
  volumes:
    - ./node3/standalone.yml:/home/bifromq/conf/standalone.yml
  ports:
    - "1885:1883"
  environment:
    - MEM_LIMIT=2147483648
  networks:
    - bifromq-net

networks:
bifromq-net:
  driver: bridge
```

To launch the cluster, run the following command:

```shell
docker compose up -d
```

- [Prerequisites](#installation-docker--prerequisites)
- [Docker Command](#installation-docker--docker-command)
- [Memory Constraints](#installation-docker--memory-constraints)

---

<a id="installation-linux"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/installation/linux/ -->

<!-- page_index: 7 -->

# Linux

Version: 4.0.0-incubating

# Linux

<a id="installation-linux--prerequisites"></a>

## Prerequisites

- JDK 17+
- Latest version BifroMQ [releases](https://bifromq.incubator.apache.org/download/)

<a id="installation-linux--shell-commands"></a>

## Shell Commands

```bash
tar -zxvf apache-bifromq-4.0.0-incubating.tar.gz --strip-components 1  -C /usr/share/bifromq/
cd /usr/share/bifromq && ./bin/standalone.sh start
```

- [Prerequisites](#installation-linux--prerequisites)
- [Shell Commands](#installation-linux--shell-commands)

---

<a id="installation-windows"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/installation/windows/ -->

<!-- page_index: 8 -->

# Windows

Version: 4.0.0-incubating

# Windows

<a id="installation-windows--prerequisites"></a>

## Prerequisites

- JDK 17+
- Latest version from BifroMQ [releases](https://bifromq.incubator.apache.org/download/)

<a id="installation-windows--shell-commands"></a>

## Shell Commands

```bash
unzip -zxvf apache-bifromq-4.0.0-incubating-windows.zip
cd bifromq\bin
standalone.bat start
```

- [Prerequisites](#installation-windows--prerequisites)
- [Shell Commands](#installation-windows--shell-commands)

---

<a id="installation-install_from_source"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/installation/install_from_source/ -->

<!-- page_index: 9 -->

# Install from Source

Version: 4.0.0-incubating

# Install from Source

<a id="installation-install_from_source--prerequisites"></a>

## Prerequisites

- JDK 17+
- Maven 3.5.0+

<a id="installation-install_from_source--build"></a>

## Build

Clone the repository to local workspace

```bash
cd <YOUR_WORKSPACE>
git clone --branch 4.0.0-incubating https://github.com/apache/bifromq bifromq
```

```bash
cd bifromq
./mvnw -v
./mvnw -U clean verify -DskipTests -Pbuild-release
```

The build output consists of several archive files with sha512 checksum located under /target/output

- apache-bifromq-4.0.0-incubating-src.tar.gz
- apache-bifromq-4.0.0-incubating.tar.gz
- apache-bifromq-4.0.0-incubating-windows.zip

- [Prerequisites](#installation-install_from_source--prerequisites)
- [Build](#installation-install_from_source--build)

---

<a id="installation-config_migration_between_versions"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/installation/config_migration_between_versions/ -->

<!-- page_index: 10 -->

# Configuration Convention & Migration

Version: 4.0.0-incubating

# Configuration Convention & Migration

Configurations may vary between different versions. When deploying BifroMQ, you can use previous configuration files, and it won't prevent BifroMQ from starting. However, please be aware that these older configurations might not take effect.

To simplify the configuration process of BifroMQ, the configuration file standalone.yml includes only common configuration items. For unspecified configurations, default values will be used, and BifroMQ will output the complete content of the configuration file at the beginning of `info.log` after starting. Users can utilize the full configuration output in the log to compare and update their standalone.yml configuration.

---

<a id="installation-nodes_on_k8s"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/installation/nodes_on_k8s/ -->

<!-- page_index: 11 -->

# Notes on Kubernetes Deployment

Version: 4.0.0-incubating

# Notes on Kubernetes Deployment

Deploying BifroMQ on Kubernetes requires careful consideration of its stateful service characteristics and understanding of Kubernetes-specific cluster operations and maintenance practices. Here are some key considerations and guidelines.

<a id="installation-nodes_on_k8s--stateful-service-considerations"></a>

## Stateful Service Considerations

BifroMQ includes a built-in distributed storage engine, and users choosing to run BifroMQ in Kubernetes should carefully plan for:

- **Persistent Volume**
- **StatefulSets**
- **Headless Services**

<a id="installation-nodes_on_k8s--deployment-complexity"></a>

## Deployment Complexity

Running BifroMQ on Kubernetes involves complexities including:

- **Networking**: Choosing the appropriate network policies and Ingress Controller to manage communication between internal and external clients to the cluster.
- **Configuration Management**: Using ConfigMaps or Secrets to manage BifroMQ configurations in a dynamic and scalable manner.
- **Resource Limits and Requests**: Defining appropriate CPU and memory limits and requests to ensure BifroMQ has sufficient resources for optimal performance without starving other applications.

<a id="installation-nodes_on_k8s--cluster-operations-and-maintenance"></a>

## Cluster Operations and Maintenance

Successful deployment of BifroMQ on Kubernetes requires a deep understanding of:

- **Cluster Monitoring and Logging**: Implementing comprehensive monitoring and logging to quickly identify and resolve issues.
- **Scalability**: Understanding how to scale BifroMQ appropriately in Kubernetes to handle varying loads without impacting performance.

- [Stateful Service Considerations](#installation-nodes_on_k8s--stateful-service-considerations)
- [Deployment Complexity](#installation-nodes_on_k8s--deployment-complexity)
- [Cluster Operations and Maintenance](#installation-nodes_on_k8s--cluster-operations-and-maintenance)

---

<a id="cluster-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/intro/ -->

<!-- page_index: 12 -->

# BifroMQ Cluster Overview

Version: 4.0.0-incubating

# BifroMQ Cluster Overview

BifroMQ employs a decentralized clustering approach, where MQTT protocol workloads are distributed across independent sub-clusters, each dedicated to specific functions. This design is built upon two foundational layers: the Underlay
Cluster and the Overlay Cluster, offering clarity and decoupled architecture for enhanced scalability and fault tolerance.

<a id="cluster-intro--underlay-cluster"></a>

## Underlay Cluster

The Underlay Cluster forms the backbone of BifroMQ's cluster system. This layer
ensures high availability by eliminating single points of failure and maintaining accurate and timely cluster topology consistency.

<a id="cluster-intro--key-features"></a>

#### Key Features:

- **Decentralized Construction**: Facilitates cluster formation without reliance on traditional registration centers, minimizing operational risks.
- **Failure Detection and Auto-Eviction**: Enhances cluster reliability through proactive failure detection and swift membership information synchronization.
- **Split-Brain Recovery**: Incorporates mechanisms to recover from network partitions, maintaining cluster integrity and consistency.

<a id="cluster-intro--overlay-cluster"></a>

## Overlay Cluster

Built atop the Underlay Cluster, the Overlay Cluster, or Agent Cluster, focuses on specific functional services, leveraging the foundational cluster for membership management and inter-node communication. It simplifies deployment and
operational processes, automatically forming clusters to support stateless RPC services and stateful services built on distributed KV storage engines.

<a id="cluster-intro--deployment-models"></a>

## Deployment Models

BifroMQ supports flexible deployment models, ranging from all-in-one processes(a.k.a `Standalone` cluster) to so-called `Independent Workload` clusters. See the [clustering guide](#cluster-clustering) for practical steps to configure, start, scale, and monitor a cluster.

- [Underlay Cluster](#cluster-intro--underlay-cluster)
- [Overlay Cluster](#cluster-intro--overlay-cluster)
- [Deployment Models](#cluster-intro--deployment-models)

---

<a id="cluster-clustering"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/clustering/ -->

<!-- page_index: 13 -->

# Clustering

Version: 4.0.0-incubating

# Clustering

<a id="cluster-clustering--overview"></a>

## Overview

BifroMQ clusters are built on two logical layers: the Underlay Cluster, which provides decentralized membership and failure detection, and the Overlay Cluster, which hosts functional services such as MQTT brokering and data persistence. This guide focuses on practical steps to deploy and operate a BifroMQ cluster.

<a id="cluster-clustering--prerequisites"></a>

## Prerequisites

- Java 17 or later installed on all nodes.
- Sufficient CPU and memory for the expected workload.
- Required ports opened in firewalls (see configuration below).

<a id="cluster-clustering--step-0-understand-the-two-tier-cluster-topology"></a>

## Step 0 – Understand the Two-Tier Cluster Topology

![](assets/images/two-tier-clustering-73c330259ba1c8b0dfb99c974dcd3095_9962768ce25b7af0.png)

BifroMQ uses a **two-tier clustering architecture**, consisting of:

- an **Underlay Cluster**, which provides decentralized membership, failure detection, and topology information, and
- multiple **Overlay Service Clusters**, enabled selectively inside each node to provide MQTT-related functionalities.

In practice:

- Every BifroMQ node must first join the **Underlay Cluster**.
- Overlay services (e.g., MQTT broker, distworker, inboxstore, retainstore) are **optional** and communicate directly with their peers once enabled.

<a id="cluster-clustering--step-1-prepare-clusterconfig"></a>

## Step 1 - Prepare `clusterConfig`

The `clusterConfig` section in [config file](#admin_guide-configuration-config_file_manual) controls the Underlay Cluster. Key fields include:

```yaml
clusterConfig:
  env: "Test"
  host:
  port:
  clusterDomainName:
  seedEndpoints:
```

Field details:

- `env`: Logical cluster identifier. Nodes must share the same value to join.
- `host`: IP to bind for inter-node communication; leave blank to auto-select a local address.
- `port`: Port for membership messages. For seed nodes, set an explicit port to simplify discovery.
- `clusterDomainName`: Optional DNS domain for resolving seed nodes in container/Kubernetes environments.
- `seedEndpoints`: Comma-separated `IP:port` list of seed nodes to join at startup.

If you prefer DNS-based discovery, set `clusterDomainName` and ensure the cluster communication port is fixed and identical among all cluster nodes.

**Firewall note:** Besides `clusterConfig.port`, BifroMQ uses dedicated ports for inter-cluster RPC (e.g., `RPCServerConfig.port`). If not set explicitly, these ports are randomly chosen and may be blocked by firewalls. Refer to the [full configuration manual](#admin_guide-configuration-config_file_manual) to pin ports and adjust firewall rules.

<a id="cluster-clustering--step-2-select-overlay-services"></a>

## Step 2 - Select overlay services

Overlay services are enabled via configuration flags:

<table><thead><tr><th>Service</th><th>Config key</th><th>Description (see <a class="" href="#admin_guide-configuration-config_file_manual">config manual</a>)</th></tr></thead><tbody><tr><td><code>mqttserver</code></td><td><code>mqttServiceConfig.server.enable</code></td><td>Enable MQTT server</td></tr><tr><td><code>distserver</code></td><td><code>distServiceConfig.server.enable</code></td><td>Enable Dist server</td></tr><tr><td><code>distworker</code></td><td><code>distServiceConfig.worker.enable</code></td><td>Enable Dist worker</td></tr><tr><td><code>inboxserver</code></td><td><code>inboxServiceConfig.server.enable</code></td><td>Enable Inbox server</td></tr><tr><td><code>inboxstore</code></td><td><code>inboxServiceConfig.store.enable</code></td><td>Enable Inbox store</td></tr><tr><td><code>retainserver</code></td><td><code>retainServiceConfig.server.enable</code></td><td>Enable Retain server</td></tr><tr><td><code>retainstore</code></td><td><code>retainServiceConfig.store.enable</code></td><td>Enable Retain store</td></tr><tr><td><code>sessiondictserver</code></td><td><code>sessionDictServiceConfig.server.enable</code></td><td>Enable SessionDict server</td></tr><tr><td><code>apiserver</code></td><td><code>apiServerConfig.enable</code></td><td>Enable HTTP API server</td></tr></tbody></table>

By default, all services are enabled in a BifroMQ process (standalone cluster). To run an independent workload cluster, disable services you do not need using their config keys. For example, a seed-only node can act purely as an Underlay Cluster member:

```yaml
clusterConfig:
  env: <CLUSTER_ENV>
  host: <SEED_HOST>
  port: <SEED_PORT>
  seedEndpoints: <SEED_LIST>
# Disable all overlay services on a seed-only node
mqttServiceConfig:
  server:
    enable: false
distServiceConfig:
  server:
    enable: false
  worker:
    enable: false
inboxServiceConfig:
  server:
    enable: false
  store:
    enable: false
retainServiceConfig:
  server:
    enable: false
  store:
    enable: false
sessionDictServiceConfig:
  server:
    enable: false
apiServerConfig:
  enable: false
```

<a id="cluster-clustering--step-3-launch-and-form-the-cluster"></a>

## Step 3 - Launch and form the cluster

<a id="cluster-clustering--start-seed-nodes"></a>

### Start seed nodes

- Set `env` to the same value on all seed nodes.
- Specify each seed node's own IP in `host` and use a fixed `port`.
- Leave `seedEndpoints` blank on the first node; include it on subsequent seed nodes.
- Start the process:

```bash
./bin/standalone.sh start
```

<a id="cluster-clustering--start-additional-nodes"></a>

### Start additional nodes

For each additional node, set the same `env` and point `seedEndpoints` to the seed nodes (by IPs or via `clusterDomainName`). Start the node via same command:

```text
./bin/standalone.sh start
```

<a id="cluster-clustering--verify-cluster-membership"></a>

### Verify cluster membership

- Check `info.log` to confirm nodes recognize each other, e.g.:

```text
AgentHost joined seedEndpoint: 10.0.0.2:9000
```

- If `apiserver` is enabled (see `apiServerConfig.*` in the config manual), query any BifroMQ node exposing the API to list Underlay Cluster members:

```bash
curl http://<API_HOST>:<API_PORT>/cluster
```

Sample response:

```json
{
  "env": "Test",
  "nodes": [
    {
      "id": "...", // unique node id in the underlay cluster
      "address": "10.0.0.1", // bind address
      "port": 8890, // cluster bind port
      "pid": 3098996 // process id of this node
    },
    { "id": "...", "address": "10.0.0.2", "port": 42855, "pid": 45037 }
  ],
  "local": "..." // id of the local node
}
```

<a id="cluster-clustering--step-4-high-availability-and-scaling"></a>

## Step 4 - High availability and scaling

BifroMQ achieves high availability by running redundant instances of both **stateless** and **stateful** overlay service clusters.
Each category uses different mechanisms for reliability and scaling.

<a id="cluster-clustering--stateless-service-clusters"></a>

### Stateless Service Clusters

Stateless services do not maintain persistent state. They include:

- `mqttserver`
- `distserver`
- `inboxserver`
- `retainserver`
- `sessiondictserver`
- `apiserver`

High availability relies on **traffic distribution**:

<a id="cluster-clustering--client-facing-services"></a>

#### Client-facing services

- `mqttbroker` and `apiserver` should be placed **behind an L4 or L7 load balancer**.
- The load balancer ensures seamless failover and horizontal scaling.

<a id="cluster-clustering--internal-stateless-services"></a>

#### Internal stateless services

- `distserver`, `inboxserver`, and `retainserver` use **RPC** for communication.
- Traffic distribution and routing behaviors are handled by **BifroMQ’s traffic governance mechanisms** (documented separately).

Because stateless services maintain no data, they can be **scaled in or out** at any time without special procedures.

<a id="cluster-clustering--stateful-service-clusters"></a>

### Stateful Service Clusters

Stateful services rely on the **base-kv** storage engine:

- `distworker`
- `inboxstore`
- `retainstore`

These services provide **strong consistency**, **replicated shards**, and **automatic sharding** across multiple nodes.

<a id="cluster-clustering--reliability-model"></a>

#### Reliability model

- **Shard replication with quorum semantics** enables continued operation even if nodes fail.
- The **Balancer framework** manages:
  - shard placement
  - leader distribution
  - range splitting and merging
  - replica redistribution

<a id="cluster-clustering--customizable-balancer-strategies"></a>

#### Customizable balancer strategies

The Balancer framework is **highly extensible** and allows operators to implement **custom strategies** tuned to workload patterns, performance goals, or SLA requirements.

<a id="cluster-clustering--scaling-stateful-services"></a>

#### Scaling stateful services

- When new nodes with stateful services enabled join the cluster, the Balancer **gradually redistributes shards**.
- When scaling in, ensure remaining nodes can maintain quorum before removing capacity.
- Shard movement and balancing occur **online**, without interrupting services.

<a id="cluster-clustering--step-5-monitoring-and-troubleshooting"></a>

## Step 5 - Monitoring and troubleshooting

- BifroMQ exposes extensive metrics via Micrometer covering underlay/overlay status and load; integrate them with your monitoring system (e.g., Prometheus) per the [observability guide](#admin_guide-observability-metrics-intro).
- The API Server provides cluster landscape and traffic/load governance APIs; use the relevant docs to query and manage these rules.

- [Overview](#cluster-clustering--overview)
- [Prerequisites](#cluster-clustering--prerequisites)
- [Step 0 – Understand the Two-Tier Cluster Topology](#cluster-clustering--step-0-understand-the-two-tier-cluster-topology)
- [Step 1 - Prepare `clusterConfig`](#cluster-clustering--step-1-prepare-clusterconfig)
- [Step 2 - Select overlay services](#cluster-clustering--step-2-select-overlay-services)
- [Step 3 - Launch and form the cluster](#cluster-clustering--step-3-launch-and-form-the-cluster)
  - [Start seed nodes](#cluster-clustering--start-seed-nodes)
  - [Start additional nodes](#cluster-clustering--start-additional-nodes)
  - [Verify cluster membership](#cluster-clustering--verify-cluster-membership)
- [Step 4 - High availability and scaling](#cluster-clustering--step-4-high-availability-and-scaling)
  - [Stateless Service Clusters](#cluster-clustering--stateless-service-clusters)
  - [Stateful Service Clusters](#cluster-clustering--stateful-service-clusters)
- [Step 5 - Monitoring and troubleshooting](#cluster-clustering--step-5-monitoring-and-troubleshooting)

---

<a id="cluster-loadbalance-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/intro/ -->

<!-- page_index: 14 -->

# Load Balancing

Version: 4.0.0-incubating

# Load Balancing

BifroMQ applies different load-balancing mechanisms for client-facing services, internal RPC services, and stateful storage services.

<a id="cluster-loadbalance-intro--client-facing-services"></a>

## Client-Facing Services

**Purpose:**
Distribute external MQTT and API traffic across multiple nodes to improve availability and absorb load variations.

**Approach:**

- Use standard **Layer 4 or Layer 7 load balancers** in front of MQTT Server or API Server.
- In controlled network environments, MQTT clients may use **custom client-side balancing strategies**.

<a id="cluster-loadbalance-intro--internal-rpc-services"></a>

## Internal RPC Services

**Purpose:**
Balance internal request routing for subscription processing, inbox dispatching, and retained-message operations.

**Approach:**

- Use BifroMQ’s **traffic governance interfaces** to inspect service topology, define routing rules, and direct RPC traffic.

<a id="cluster-loadbalance-intro--stateful-service-clusters"></a>

## Stateful Service Clusters

**Purpose:**
Distribute sharded storage and compute workloads for dynamic subscriptions, offline messages, and retained messages.

**Approach:**

- The storage layer manages **shard placement, leader roles, and adaptive load distribution** automatically.
- Landscape-level APIs provide visibility into shard layout and replica distribution.

- [Client-Facing Services](#cluster-loadbalance-intro--client-facing-services)
- [Internal RPC Services](#cluster-loadbalance-intro--internal-rpc-services)
- [Stateful Service Clusters](#cluster-loadbalance-intro--stateful-service-clusters)

---

<a id="cluster-loadbalance-mqttserver"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/mqttserver/ -->

<!-- page_index: 15 -->

# MQTT Server Load Balancing

Version: 4.0.0-incubating

# MQTT Server Load Balancing

MQTT Broker nodes expose **TCP / TLS / WS / WSS** endpoints for MQTT 3.1.1 and MQTT 5.0 clients.
Two load-balancing approaches are available depending on deployment conditions.

<a id="cluster-loadbalance-mqttserver--l4-load-balancing"></a>

## L4 Load Balancing

**Use cases:**

- Horizontal distribution of client connections
- TLS offloading at the load balancer layer

**Supported balancers:**
Any standard **Layer-4 TCP load balancer** (e.g., NGINX stream, HAProxy, AWS NLB).

**Proxy Protocol Support:**
BifroMQ supports **Proxy Protocol v1 and v2**. It allows the load balancer to forward the real client IP and port.

<a id="cluster-loadbalance-mqttserver--non-lb-deployment"></a>

## Non-LB Deployment

Applicable when all clients use **MQTT 5** and the environment allows brokers to instruct clients to reconnect elsewhere.

**Mechanism:**
BifroMQ can actively redirect clients using MQTT 5 disconnect semantics:

- `Server moved (0x9D)` — permanent relocation
- `Use another server (0x9C)` — temporary relocation

Redirection logic is defined by the **[Client Balancer Plugin](#plugin-client_balancer)**, which can select target brokers based on metrics such as load, latency, or session distribution.

- [L4 Load Balancing](#cluster-loadbalance-mqttserver--l4-load-balancing)
- [Non-LB Deployment](#cluster-loadbalance-mqttserver--non-lb-deployment)

---

<a id="cluster-loadbalance-apiserver"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/apiserver/ -->

<!-- page_index: 16 -->

# API Server Load Balancing

Version: 4.0.0-incubating

# API Server Load Balancing

The API Server exposes **HTTP/HTTPS** endpoints for administrative operations such as proxy subscription, message publishing, session management, etc.

<a id="cluster-loadbalance-apiserver--layer-7-load-balancing"></a>

## Layer-7 Load Balancing

**Use cases:**

- SSL termination
- request routing
- authentication and authorization
- centralized rate limiting

**Approach:**
Place a **Layer-7 load balancer or API Gateway** (e.g., NGINX, Envoy, Kong, AWS ALB, GCP API Gateway) in front of API Server nodes.

The L7 load balancer:

- distributes API requests across all nodes with API service enabled
- shields clients from node failures
- provides policy control not included in BifroMQ (auth, quota, throttling)

<a id="cluster-loadbalance-apiserver--api-server-cluster-behavior"></a>

## API Server Cluster Behavior

The API Server forms a **logical service cluster** automatically on top of the Underlay cluster. Any BifroMQ node with the API server enabled (via `apiServerConfig.enable`) can process HTTP/HTTPS requests. No additional coordination is required beyond load balancer configuration.

- [Layer-7 Load Balancing](#cluster-loadbalance-apiserver--layer-7-load-balancing)
- [API Server Cluster Behavior](#cluster-loadbalance-apiserver--api-server-cluster-behavior)

---

<a id="cluster-loadbalance-rpcserver"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/rpcserver/ -->

<!-- page_index: 17 -->

# Internal RPC Load Balancing

Version: 4.0.0-incubating

# Internal RPC Load Balancing

BifroMQ’s internal RPC framework supports **runtime traffic governing**, allowing operators to control how internal service requests are distributed across nodes at runtime.

The following internal RPC services support runtime traffic governance (the value shown is the required `service_name` header):

<table><thead><tr><th>Service</th><th>Internal role</th><th><code>&lt;SERVICE_NAME_HEADER&gt;</code></th></tr></thead><tbody><tr><td>Dist Server</td><td>subscription distribution</td><td><code>DistService</code></td></tr><tr><td>Inbox Server</td><td>offline message delivery</td><td><code>InboxService</code></td></tr><tr><td>Retain Server</td><td>retain message lookup</td><td><code>RetainService</code></td></tr><tr><td>Session Dict Server</td><td>shared session dictionary</td><td><code>SessionDictService</code></td></tr></tbody></table>

These services form logically independent subclusters on top of the underlay cluster, each responsible for a specific class of internal workloads.

<a id="cluster-loadbalance-rpcserver--traffic-governance-api"></a>

## Traffic governance API

The traffic governance API provides introspection and control over routing weights and node groups within a service subcluster.

<a id="cluster-loadbalance-rpcserver--service-landscape"></a>

### Service landscape

The Service Landscape API returns all active RPC service instances for a given service\_name.
It reflects the runtime topology of the service subcluster on the overlay layer, including node identity, bind address, port, static attributes, and dynamically assigned groups.

<a id="cluster-loadbalance-rpcserver--request"></a>

##### Request

```text
GET /service/landscape
Headers:
  service_name: <SERVICE_NAME_HEADER>
```

<a id="cluster-loadbalance-rpcserver--response-structure"></a>

##### Response Structure

```json
[
  {
    "hostId": "OTQ0OWE5NzAtNjliOC00ZDI3LTg5MjQtOWU3NDEyMWNhNDFj", // Identity of the node in the Underlay Cluster
    "id": "342586ce-a8d4-4d85-9ae0-3bf596e982d5/1456250665", // Identity of the RPC server instance in the Overlay Cluster
    "address": "10.0.0.2", // RPC server bind address
    "port": 40469, // RPC server bind port
    "attributes": {}, // Static metadata configured at startup (e.g., availability zone, rack ID).
    "groups": [] // Runtime-assigned groups (via `/service/group`)
  }
]
```

<a id="cluster-loadbalance-rpcserver--traffic-rules"></a>

### Traffic rules

Traffic rules control how tenant-tagged requests are distributed across RPC service instances at runtime.
Rules are evaluated based on the `service_name` header and define a per-tenant routing policy.
Incoming requests from a tenant are distributed across one or more server groups according to their configured weights.
Each server group forwards requests to its RPC servers. If a selected server group has no available servers, the request is rejected.
Tenants without an explicit traffic rule use the default server group.

The traffic rule JSON:

```json
{
    "<TENANT_ID>": {          // tenant for which the rule applies
        "<SERVER_GROUP>": <WEIGHT>   // server group name and its routing weight
    }
}
```

<a id="cluster-loadbalance-rpcserver--get-traffic-rules"></a>

#### Get Traffic Rules

Returns the current routing rules for the specified service.

<a id="cluster-loadbalance-rpcserver--request-1"></a>

##### Request

```text
GET /service/traffic
Headers:
service_name: <SERVICE_NAME_HEADER>
```

<a id="cluster-loadbalance-rpcserver--response-structure-1"></a>

##### Response Structure

Same as the traffic rule JSON above.

<a id="cluster-loadbalance-rpcserver--set-traffic-rules"></a>

#### Set Traffic Rules

Updates traffic rules by merging the provided JSON with the existing rules.

<a id="cluster-loadbalance-rpcserver--request-2"></a>

##### Request

```text
PUT /service/traffic
Headers:
service_name: <SERVICE_NAME_HEADER>
Body: traffic rule JSON shown above.
```

<a id="cluster-loadbalance-rpcserver--unset-traffic-rule"></a>

#### Unset Traffic Rule

Removes traffic rules for the specified tenants.
The request body must contain an array of `<TENANT_ID>` values.

```text
DELETE /service/traffic
Headers:
service_name: <SERVICE_NAME_HEADER>
```

<a id="cluster-loadbalance-rpcserver--server-groups"></a>

### Server Groups

Service groups classify RPC server instances into logical buckets (e.g., AZ, rack, region).
Traffic rules reference these groups to determine how tenant traffic is routed.
A server may belong to multiple groups. Servers with no explicit groups are implicitly part of the 'default' group.
Server groups can be set in two ways:

- at startup via configuration file (static initial groups)
- at runtime via the /service/group API (dynamic override)

<a id="cluster-loadbalance-rpcserver--set-server-groups-runtime"></a>

#### Set Server Groups (runtime)

Assigns one or more group names to a specific RPC server instance.

<a id="cluster-loadbalance-rpcserver--request-3"></a>

##### Request

```text
PUT /service/group
Headers:
  service_name: <SERVICE_NAME_HEADER>
  server_id: <SERVER_ID>   # Returned from /service/landscape
Body: JSON array of strings, each represents a group name
```

Runtime group assignment:

- replaces any previously assigned groups
- may assign multiple groups
- if the array is empty → server belongs only to the 'default' group

<a id="cluster-loadbalance-rpcserver--startup-configuration-static-group-assignment"></a>

#### Startup Configuration (static group assignment)

Server groups may also be defined in the configuration file.
These groups become the server’s initial group list before any /service/group updates occur.

```yaml
distServiceConfig:
  server:
    attributes:
      - "prod"
      - "az1"
```

- [Traffic governance API](#cluster-loadbalance-rpcserver--traffic-governance-api)
  - [Service landscape](#cluster-loadbalance-rpcserver--service-landscape)
  - [Traffic rules](#cluster-loadbalance-rpcserver--traffic-rules)
  - [Server Groups](#cluster-loadbalance-rpcserver--server-groups)

---

<a id="cluster-loadbalance-stateful-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/stateful/intro/ -->

<!-- page_index: 18 -->

# Stateful Server Load Balancing

Version: 4.0.0-incubating

# Stateful Server Load Balancing

All stateful services in BifroMQ are built on top of the **base-kv** distributed storage engine.
base-kv provides **strong consistency**, **automatic sharding**, and **fault tolerance**, forming the foundation for high availability and elastic scaling of stateful workloads.
Load distribution and availability are jointly managed by **replicated shards** and the **Balancer framework**, which continuously adapts the cluster topology to runtime conditions.

<a id="cluster-loadbalance-stateful-intro--core-principles"></a>

## Core Principles

<a id="cluster-loadbalance-stateful-intro--replicated-shards-and-quorum"></a>

### Replicated Shards and Quorum

Each stateful service cluster continuously replicates its data across multiple nodes using the Raft protocol.

- As long as a quorum of replicas for a shard (Range) remains alive, the service continues to serve reads and writes.
- Node failures are tolerated transparently without manual intervention.

<a id="cluster-loadbalance-stateful-intro--leader-based-access-model"></a>

### Leader-Based Access Model

- Each shard has a designated **leader** responsible for handling writes.
- Leaders are deliberately distributed across the cluster to avoid hotspots and ensure balanced utilization.

High availability therefore emerges from:

- Replica redundancy
- Deterministic leader placement
- Continuous topology adjustment

<a id="cluster-loadbalance-stateful-intro--stateful-services-built-on-base-kv"></a>

## Stateful Services Built on base-kv

All BifroMQ stateful servers share the same architectural foundation but optimize their storage schema and access paths based on workload characteristics:

<table><thead><tr><th>Service</th><th>store_name (for API headers)</th><th>Role/Workload</th></tr></thead><tbody><tr><td><a class="" href="#cluster-loadbalance-stateful-distworker"><strong>DistWorker</strong></a></td><td><code>dist.worker</code></td><td>subscription routing</td></tr><tr><td><a class="" href="#cluster-loadbalance-stateful-inboxstore"><strong>InboxStore</strong></a></td><td><code>inbox.store</code></td><td>persistent offline message queues</td></tr><tr><td><a class="" href="#cluster-loadbalance-stateful-retainstore"><strong>RetainStore</strong></a></td><td><code>retain.store</code></td><td>retained message storage</td></tr></tbody></table>

This design allows each service to:

- Use the same base-kv primitives
- Apply **deep, workload-specific optimizations**
- Reuse the same balancing and recovery mechanisms

<a id="cluster-loadbalance-stateful-intro--store-landscape"></a>

## Store Landscape

Stateful services run on an overlay cluster just like RPC services. You can inspect the server topology via API and also inspect how Range replicas are placed across storage nodes.

<a id="cluster-loadbalance-stateful-intro--get-store-landscape"></a>

### Get store landscape

List the nodes of the stateful service overlay cluster.

**Request**

```text
GET /store/landscape
Headers:
  store_name: <STORE_NAME_HEADER>
```

**Response**

```json
[
  {
    "hostId": "c3RvcmUtaWQ=", // Identity of the node in the Underlay Cluster
    "id": "710dc192-4641-4b31-bde1-a36329b33273", // Identity of the stateful server instance in the Overlay Cluster
    "address": "10.0.0.2", // server bind address
    "port": 36801, // server bind port
    "attributes": {
        ...
    }
  }
]
```

<a id="cluster-loadbalance-stateful-intro--get-range-placement-in-a-store"></a>

### Get range placement in a store

List Range replicas hosted on a specific store server.

**Request**

```text
GET /store/ranges
Headers:
  store_name: <STORE_NAME_HEADER>
  store_id: <STORE_ID_HEADER>
```

**Response**

```json
[
  {
    "id": "115240914861228032_0", // the range id
    "ver": 14, // the version of range
    "boundary": {
      // the range boundary
      "startKey": null,
      "endKey": null
    },
    "state": "Normal", // the range state
    "role": "Leader", // the replica role
    "clusterConfig": {
      "voters": [
        "710dc192-4641-4b31-bde1-a36329b33273",
        "c2784a36-4509-41be-96bc-5809026bce99",
        "cd360c5f-7693-40c6-af9c-541cc2467a00"
      ],
      "learners": [],
      "nextVoters": [],
      "nextLearners": []
    }
  }
]
```

<a id="cluster-loadbalance-stateful-intro--balancer-framework-overview"></a>

## Balancer Framework Overview

The **Balancer framework** continuously shapes the base-kv cluster topology. Although a centralized coordinator is straightforward to implement, the framework is designed to enable **distributed convergence**, meaning there is:

- No central coordinator
- No single point of control
- No out-of-band orchestration

Achieving distributed convergence requires each balancer implementation to be deterministic:

- Every node observes the strong eventually consistent global cluster state
- Each balancer deterministically derives the same *expected* Range topology (the built-in balancers follow this pattern)
- Each node independently executes balance commands for the Ranges it currently leads

<a id="cluster-loadbalance-stateful-intro--built-in-storebalancers"></a>

### Built-in StoreBalancers

BifroMQ ships with several built-in Balancers that cover common scenarios and can serve as references for custom implementations.
The framework lets Balancer implementations expose runtime-tunable rules and be started/paused via API; which balancers to enable and their initial rules are set in configuration (for example, `BalancerOptions.balancers` keyed by balancerFactory FQN).

<table><thead><tr><th>Balancer</th><th>Focus</th><th>Rules</th></tr></thead><tbody><tr><td><code>RangeLeaderBalancer</code></td><td>Evenly spread Range leaders to avoid hotspots</td><td></td></tr><tr><td><code>ReplicaCntBalancer</code></td><td>Keep replica counts aligned with goals (voters/learners)</td><td>- <code>votersPerRange</code>: target voters per range (must be odd)
- <code>learnersPerRange</code>: target learners per range (-1 means no limit)</td></tr><tr><td><code>RangeSplitBalancer</code></td><td>Split "hot" Ranges to sustain throughput</td><td>- <code>maxCpuUsagePerRange</code>: CPU threshold
- <code>maxIODensityPerRange</code>: IO density cap
- <code>ioNanosLimitPerRange</code>: IO latency cap (ns)
- <code>maxRangesPerStore</code>: per-store range cap</td></tr></tbody></table>
<a id="cluster-loadbalance-stateful-intro--balanceroptions"></a>

### BalancerOptions

[`BalancerOptions`](#admin_guide-configuration-config_file_manual--balanceroptions) tells a BifroMQ process with DistWorker enabled which balancers to instantiate at startup and the initial values of their rules. `BalancerOptions.balancers` is a map keyed by the balancerFactory FQN, with a `Struct` payload for initial rules. For example, to start a `ReplicaCntBalancer` on DistWorker with default replica targets:

```yaml
distWorkerConfig:
  balanceConfig:
    balancers:
      org.apache.bifromq.dist.worker.balance.ReplicaCntBalancerFactory:
        votersPerRange: 3
        learnersPerRange: -1
```

<a id="cluster-loadbalance-stateful-intro--enabledisable-balancer-at-runtime"></a>

### Enable/Disable Balancer at Runtime

Balancers can be started or paused via the runtime API without restarting the service. This lets operators temporarily disable a balancer for observation or mitigation, then re-enable it as needed; deterministic behavior preserves convergence when reactivated. Note: ensure the `balancer_factory_class` is correct when enabling the balancer instances initialized via `BalancerOptions`.

<a id="cluster-loadbalance-stateful-intro--enable-the-balancer-instances"></a>

#### Enable the balancer instances

```text
PUT /store/balancer/enable
Headers:
  store_name: <STORE_NAME_HEADER>
  balancer_factory_class: <BALANCER_FACTORY_CLASS_FQN>
```

<a id="cluster-loadbalance-stateful-intro--disable-the-balancer-instances"></a>

#### Disable the balancer instances

```text
PUT /store/balancer/disable
Headers:
  store_name: <STORE_NAME_HEADER>
  balancer_factory_class: <BALANCER_FACTORY_CLASS_FQN>
```

<a id="cluster-loadbalance-stateful-intro--update-balancers-rules-at-runtime"></a>

### Update Balancer's rules at runtime

Balancer rules (the same `Struct` schema used in `BalancerOptions.balancers`) can be updated at runtime through the API. New rules take effect immediately, and subsequent balance cycles converge using the updated values.

<a id="cluster-loadbalance-stateful-intro--get-rules-override"></a>

#### Get rules override

Retrieve the rules override; a 404 is returned if no override is set.

**Request**

```text
GET /store/balancer/rules
Headers:
  store_name: <STORE_NAME_HEADER>
  balancer_factory_class: <BALANCER_FACTORY_CLASS_FQN>
```

**Response**

```json
{
  "votersPerRange": 1.0
}
```

<a id="cluster-loadbalance-stateful-intro--merge-rules-override-with-existing-rules"></a>

#### Merge rules override with existing rules

Merge a rules override with existing rules; the caller must ensure the payload is structurally valid.

```text
PUT /store/balancer/rules
Headers:
  store_name: <STORE_NAME_HEADER>
  balancer_factory_class: <BALANCER_FACTORY_CLASS_FQN>
Body: balance rules override json
```

<a id="cluster-loadbalance-stateful-intro--get-balancer-states"></a>

#### Get balancer states

Get the latest state of the balancer instances running on each stateful server.

**Request**

```text
GET /store/balancer
Headers:
  store_name: <STORE_NAME_HEADER>
  balancer_factory_class: <BALANCER_FACTORY_CLASS_FQN>
```

**Response**

```json
{
  "org.apache.bifromq.dist.worker.balance.ReplicaCntBalancerFactory": {
    "710dc192-4641-4b31-bde1-a36329b33273": { // store id running the balancer instance
      "disable": false, // whether the balancer is disabled
      "loadRules": { // effective load rules
        "votersPerRange": 1.0,
        "learnersPerRange": -1.0
      },
      "hlc": "115526170745044992" // hlc timestamp of last update
    },
    ...
  }
}
```

- [Core Principles](#cluster-loadbalance-stateful-intro--core-principles)
  - [Replicated Shards and Quorum](#cluster-loadbalance-stateful-intro--replicated-shards-and-quorum)
  - [Leader-Based Access Model](#cluster-loadbalance-stateful-intro--leader-based-access-model)
- [Stateful Services Built on base-kv](#cluster-loadbalance-stateful-intro--stateful-services-built-on-base-kv)
- [Store Landscape](#cluster-loadbalance-stateful-intro--store-landscape)
  - [Get store landscape](#cluster-loadbalance-stateful-intro--get-store-landscape)
  - [Get range placement in a store](#cluster-loadbalance-stateful-intro--get-range-placement-in-a-store)
- [Balancer Framework Overview](#cluster-loadbalance-stateful-intro--balancer-framework-overview)
  - [Built-in StoreBalancers](#cluster-loadbalance-stateful-intro--built-in-storebalancers)
  - [BalancerOptions](#cluster-loadbalance-stateful-intro--balanceroptions)
  - [Enable/Disable Balancer at Runtime](#cluster-loadbalance-stateful-intro--enabledisable-balancer-at-runtime)
  - [Update Balancer's rules at runtime](#cluster-loadbalance-stateful-intro--update-balancers-rules-at-runtime)

---

<a id="cluster-loadbalance-stateful-distworker"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/stateful/distworker/ -->

<!-- page_index: 19 -->

# Dist Worker

Version: 4.0.0-incubating

# Dist Worker

DistWorker handles subscription routing and fan-out (read-heavy). It runs as a stateful service on the base-kv overlay cluster; `store_name` for API headers: `dist.worker`.

<a id="cluster-loadbalance-stateful-distworker--default-balancers"></a>

## Default balancers

<table><thead><tr><th>balancerFactory FQN</th><th>Role</th><th>Default parameters (load rules)</th></tr></thead><tbody><tr><td><code>org.apache.bifromq.dist.worker.balance.RangeLeaderBalancerFactory</code></td><td>Spread range leaders evenly</td><td></td></tr><tr><td><code>org.apache.bifromq.dist.worker.balance.ReplicaCntBalancerFactory</code></td><td>Keep replica count per range to targets</td><td>- <code>votersPerRange: 3</code>
- <code>learnersPerRange: -1</code></td></tr></tbody></table>

These defaults come from `distWorkerConfig.balanceConfig.balancers` in starter config.

- [Default balancers](#cluster-loadbalance-stateful-distworker--default-balancers)

---

<a id="cluster-loadbalance-stateful-inboxstore"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/stateful/inboxstore/ -->

<!-- page_index: 20 -->

# Inbox Store

Version: 4.0.0-incubating

# Inbox Store

InboxStore provides persistent offline message queues (write-intensive). It runs as a stateful service on the base-kv overlay cluster; `store_name` for API headers: `inbox.store`.

<a id="cluster-loadbalance-stateful-inboxstore--default-balancers"></a>

## Default balancers

<table><thead><tr><th>balancerFactory FQN</th><th>Role</th><th>Default parameters (load rules)</th></tr></thead><tbody><tr><td><code>org.apache.bifromq.inbox.store.balance.RangeLeaderBalancerFactory</code></td><td>Spread range leaders evenly</td><td></td></tr><tr><td><code>org.apache.bifromq.inbox.store.balance.ReplicaCntBalancerFactory</code></td><td>Keep replica count per range to targets</td><td><code>votersPerRange: 3</code></td></tr><tr><td><code>org.apache.bifromq.inbox.store.balance.RangeSplitBalancerFactory</code></td><td>Split hot/large ranges to sustain throughput</td><td>- <code>maxRangesPerStore: (availableProcessors / 4)</code>
- <code>maxCPUUsage: 0.8</code>
- <code>maxIODensity: 100</code>
- <code>ioNanosLimit: 30000</code></td></tr></tbody></table>

Defaults are set in `inboxStoreConfig.balanceConfig.balancers` in starter config.

- [Default balancers](#cluster-loadbalance-stateful-inboxstore--default-balancers)

---

<a id="cluster-loadbalance-stateful-retainstore"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/loadbalance/stateful/retainstore/ -->

<!-- page_index: 21 -->

# Retain Store

Version: 4.0.0-incubating

# Retain Store

RetainStore serves retained messages (read-dominant). It runs as a stateful service on the base-kv overlay cluster; `store_name` for API headers: `retain.store`.

<a id="cluster-loadbalance-stateful-retainstore--default-balancers"></a>

## Default balancers

<table><thead><tr><th>balancerFactory FQN</th><th>Role</th><th>Default parameters (load rules)</th></tr></thead><tbody><tr><td><code>org.apache.bifromq.retain.store.balance.ReplicaCntBalancerFactory</code></td><td>Keep replica count per range to targets</td><td>- <code>votersPerRange: 3</code>
- <code>learnersPerRange: -1</code></td></tr><tr><td><code>org.apache.bifromq.retain.store.balance.RangeSplitBalancerFactory</code></td><td>Split hot/large ranges to sustain throughput</td><td>- <code>maxRangesPerStore: (availableProcessors / 4)</code>
-<code>maxCPUUsage: 0.8</code>
-<code>maxIODensity: 100</code>
- <code>ioNanosLimit: 30000</code></td></tr></tbody></table>

Defaults are set in `retainStoreConfig.balanceConfig.balancers` in starter config.

- [Default balancers](#cluster-loadbalance-stateful-retainstore--default-balancers)

---

<a id="cluster-upgrade"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/cluster/upgrade/ -->

<!-- page_index: 22 -->

# Upgrade Guide

Version: 4.0.0-incubating

> [!WARNING]
> **Important:** Since BifroMQ joined the Apache Incubator, the Java package names have changed. Users of pre-incubation versions must migrate to the Apache-released BifroMQ versions to avoid package conflicts.

# Upgrade Guide

BifroMQ supports multiple upgrade strategies to ensure smooth transitions between versions. This document provides a detailed guide on upgrading BifroMQ, including version compatibility, upgrade methods, and specific steps for each method.

<a id="cluster-upgrade--version-compatibility"></a>

## Version Compatibility

BifroMQ version compatibility is categorized into two main aspects: **data compatibility** and **inter-cluster RPC protocol compatibility**. The versioning scheme follows semantic versioning conventions:

- **x.y.z**:
  - **x**: Major version number.
  - **y**: Minor version number.
  - **z**: Patch version number.

<a id="cluster-upgrade--compatibility-rules"></a>

### Compatibility Rules

1. **Patch Version Upgrades (x.y.z)**:

   - When only the patch version (z) changes, **both data compatibility and inter-cluster RPC protocol compatibility** are guaranteed.
2. **Minor Version Upgrades (x.y)**:

   - When the minor version (y) changes, **inter-cluster RPC protocol compatibility** is guaranteed.
   - **Data compatibility** may change, but any such changes will be explicitly documented.
3. **Major Version Upgrades (x)**:

   - Major version upgrades may introduce **breaking changes** that affect both data compatibility and inter-cluster RPC protocol compatibility.
   - **Rolling upgrades within the cluster are not supported** for major version changes unless explicitly stated in the release notes that both data compatibility and inter-cluster RPC protocol compatibility are maintained. Users will need to manage the migration of their applications and data from the old version cluster to the new version cluster independently.

<a id="cluster-upgrade--upgrade-methods"></a>

## Upgrade Methods

BifroMQ supports two rolling upgrade methods:

1. **In-Place Upgrade**
2. **Replace Upgrade**

<a id="cluster-upgrade--prerequisite"></a>

### Prerequisite

Apache BifroMQ **4.0.0-incubating introduces breaking changes** and is **not backward compatible** with earlier versions. In particular, several **plugin interfaces have been updated**.
If you are using any **custom plugins**, you must:

1. **Update your plugin code** to use the latest interfaces, and
2. **Rebuild** your plugins against the new version of BifroMQ before upgrading.

<a id="cluster-upgrade--in-place-upgrade"></a>

### In-Place Upgrade

This method is suitable when the new version maintains both data compatibility and inter-cluster RPC protocol compatibility with the existing version.

<a id="cluster-upgrade--steps-for-in-place-upgrade"></a>

#### Steps for In-Place Upgrade

1. **Stop the Current Version**:

   - Gracefully shut down the BifroMQ service.
2. **Preserve the Data Directory**:

   - Ensure the `data` directory is retained.
3. **Update Files and Configurations**:

   - Replace the necessary binaries and update the configuration files as required by the new version.
4. **Start the New Version**:

   - Launch the new version of BifroMQ using the existing data.

<a id="cluster-upgrade--replace-upgrade"></a>

### Replace Upgrade

Use this method when the new version does not maintain data compatibility or when inter-cluster RPC protocol compatibility is ensured.

<a id="cluster-upgrade--steps-for-replace-upgrade"></a>

#### Steps for Replace Upgrade

1. **Add New Version Nodes**:

   - Gradually introduce nodes running the new version into the cluster.
2. **Remove Old Version Nodes**:

   - Sequentially remove nodes running the old version from the cluster until all nodes are upgraded to the new version.
3. **Automatic Data Migration**:

   - During the upgrade, BifroMQ automatically handles data migration and synchronization between nodes.

<a id="cluster-upgrade--important-considerations-for-replace-upgrade"></a>

#### Important Considerations for Replace Upgrade

- **Voter Configuration**:

  - Ensure that the following BifroSysProp properties for `dist-worker`, `inbox-store`, and `retain-store` have more than one Voter configured, otherwise data migration will not happen:
    - `dist_worker_range_voter_count`
    - `inbox_store_range_voter_count`
    - `retain_store_range_voter_count`
- **Node Upgrade Limitation**:

  - Do not upgrade more than half of the nodes simultaneously to avoid making the cluster unavailable.

<a id="cluster-upgrade--summary"></a>

## Summary

- **In-Place Upgrade**: Suitable for upgrades within the same major and minor versions (x.y), where data and RPC protocol compatibility are maintained.
- **Replace Upgrade**: Necessary for upgrades across minor versions or where data compatibility may not be maintained. Follow the step-by-step process to ensure a smooth transition.

- [Version Compatibility](#cluster-upgrade--version-compatibility)
  - [Compatibility Rules](#cluster-upgrade--compatibility-rules)
- [Upgrade Methods](#cluster-upgrade--upgrade-methods)
  - [Prerequisite](#cluster-upgrade--prerequisite)
  - [In-Place Upgrade](#cluster-upgrade--in-place-upgrade)
  - [Replace Upgrade](#cluster-upgrade--replace-upgrade)
- [Summary](#cluster-upgrade--summary)

---

<a id="user_guide-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/intro/ -->

<!-- page_index: 23 -->

# User Guide Overview

Version: 4.0.0-incubating

# User Guide Overview

BifroMQ is a sophisticated, Java-based MQTT broker that excels in providing high-performance, distributed messaging capabilities. With its native support for multi-tenancy, BifroMQ stands out as a versatile tool for integrating MQTT
functionalities into a wide range of business systems, particularly those geared towards large-scale IoT device communications and messaging infrastructures.

<a id="user_guide-intro--key-features-and-considerations"></a>

#### Key Features and Considerations:

- **Integration Flexibility with Multi-Tenancy Support**: BifroMQ is designed to seamlessly integrate with various business systems that require MQTT capabilities. A fundamental aspect of BifroMQ is its native support for multi-tenancy,
  which allows different tenants (clients or customer organizations) to operate in isolated environments within the same broker instance. Understanding the concept of **tenants** and BifroMQ's approach to multi-tenancy is crucial when
  planning your integration strategy.
- **Tenant Identification and Namespace Isolation**: In BifroMQ, tenants are uniquely identified by a ***tenantId*** and are defined as "namespaces". This design ensures that all MQTT connections and sessions are associated with a specific
  tenant namespace. MQTT connections within the same tenant namespace can publish and subscribe to messages amongst each other, while connections across different tenant namespaces remain isolated, enhancing security and data privacy.
- **Tenant Lifecycle Management by Integrators**: Unlike some systems that manage tenant lifecycles internally, BifroMQ delegates the definition and management of tenants to the integrating business. This is achieved by implementing
  an [Auth Provider Plugin](#plugin-auth_provider), where the business specifies the ***tenantId*** for each connection during the authentication process. This model supports a wide range of business scenarios,
  including the use of a single, "global" tenant namespace for businesses not requiring multi-tenancy features.
- **Resource and Load Isolation per Tenant**: Beyond logical isolation of MQTT sessions and message publication/subscription, BifroMQ uses tenant spaces as boundaries for resource and load isolation. This capability is facilitated
  by [Tenant Metrics](#admin_guide-observability-metrics-tenantmetrics) and the [Resource Throttler Plugin](#plugin-resource_throttler), ensuring efficient resource utilization and system stability.
- **Optimized Tenant Capability with Minimal Resource Overhead**: BifroMQ is specifically designed for multi-tenancy, yet the multi-tenant capability incurs a certain level of resource overhead. However, this overhead does not need to be a concern in the vast majority of multi-tenant business scenarios. It is important to note, though, that scaling the BifroMQ cluster horizontally cannot achieve an infinite increase in the number of tenants served simultaneously within the cluster. Therefore, when designing multi-tenant business, one should avoid mapping BifroMQ tenants to overly granular entities, such as "one tenant per connection".

---

<a id="user_guide-basic-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/basic/intro/ -->

<!-- page_index: 24 -->

# MQTT Basic Features Highlights

Version: 4.0.0-incubating

# MQTT Basic Features Highlights

BifroMQ provides extensive MQTT protocol support for IoT applications and services, demonstrated through compatibility with different protocol versions, customized configurations for tenants, dynamic adjustment capabilities, message interchangeability across protocol versions, and support for shared subscriptions in specific protocol versions.

- **Comprehensive Protocol Support**: BifroMQ supports MQTT versions 3.1, 3.1.1, and 5.0, compatible with all third-party clients that utilize these protocol versions. This ensures users can seamlessly integrate BifroMQ into their existing systems, offering a smooth experience for developers and administrators.
- **Tenant-Specific Configurations**: BifroMQ allows for protocol-related [settings](#plugin-setting_provider-tenantsetting) to be customized for each tenant, catering to the specific needs and application scenarios of each tenant.
- **Dynamic Adjustment via Plugins**: BifroMQ supports dynamic adjustments of protocol settings through the use of [setting provider plugins](#plugin-setting_provider-intro), offering flexibility and adaptability in rapidly changing business operations.
- **Interoperability Between Protocol Versions**: BifroMQ supports message exchange between sessions established with different MQTT protocol versions within the same tenant, ensuring seamless communication between devices and clients on different protocol versions.
- **Shared Subscriptions Support**: BifroMQ provides [shared subscriptions](#user_guide-basic-shared_sub) for MQTT versions 3.1 and 3.1.1, allowing multiple clients to subscribe to the same topic and balance the message load among them, improving the efficiency and reliability of message processing.

---

<a id="user_guide-basic-connect"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/basic/connect/ -->

<!-- page_index: 25 -->

# Connect to BifroMQ

Version: 4.0.0-incubating

# Connect to BifroMQ

BifroMQ is a standard MQTT messaging middleware, which allows you to connect using any client that supports MQTT version 3.1, 3.1.1 or 5.0.

<a id="user_guide-basic-connect--connection-address"></a>

## Connection Address

Use the IP address or domain name corresponding to the launched service. Below are the default ports and their purposes:

<table><thead><tr><th>Port</th><th>Note</th></tr></thead><tbody><tr><td>IP or Domain:1883</td><td>TCP Connection</td></tr><tr><td>IP or Domain:1884</td><td>TLS Connection</td></tr><tr><td>IP or Domain:80/mqtt</td><td>WS Connection</td></tr><tr><td>IP or Domain:443/mqtt</td><td>WSS Connection</td></tr></tbody></table>
<a id="user_guide-basic-connect--authentication-and-authorization"></a>

## Authentication and Authorization

By default, without an AuthProvider plugin, BifroMQ does not enforce authentication or authorization. However, you can assign a connection to a specific tenant by specifying the username in the format `<TenantId>/<UserName>`. If you omit the tenant prefix, the connection will be assigned to the default `"DevOnly"` tenant.

For full authentication and authorization support, please refer to the [AuthProvider Plugin](#plugin-auth_provider).

- [Connection Address](#user_guide-basic-connect--connection-address)
- [Authentication and Authorization](#user_guide-basic-connect--authentication-and-authorization)

---

<a id="user_guide-basic-pubsub"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/basic/pubsub/ -->

<!-- page_index: 26 -->

# Pub/Sub

Version: 4.0.0-incubating

# Pub/Sub

According to the MQTT protocol, entities involved in sending and receiving messages can be categorized as Publishers and Subscribers. The basic model is depicted below:

- **Publishing Messages**: Clients can publish messages to the server through a connection. Messages are published based on `topics`, which describe the content of the communication and are hierarchical in nature (
  e.g., `home/bedroom/temperature`).

  When publishing a message, clients need to specify a topic, and the message payload contains the actual content of the communication. Additionally, the publisher must specify the Quality of Service (QoS) for the message. BifroMQ supports
  all MQTT QoS levels: QoS0, QoS1, and QoS2. Their meanings are as follows:

  <table><thead><tr><th>QoS</th><th>Description</th></tr></thead><tbody><tr><td>QoS0</td><td>At most once delivery</td></tr><tr><td>QoS1</td><td>At least once delivery</td></tr><tr><td>QoS2</td><td>Exactly once delivery</td></tr></tbody></table>
- **Subscribing to Topics**: In subscription, the subscribed topics are called `topicFilter`. The server receives subscription requests from clients and records these subscriptions. Generally, subscriptions can be either non-wildcard
  subscriptions or wildcard subscriptions.

  - For **non-wildcard subscriptions**: Clients subscribe to a specific topic without using wildcards. For example, if a client subscribes to `home/bedroom/temperature`, it will only match messages with the
    topic `home/bedroom/temperature`.
  - For **wildcard subscriptions**: The subscription topic includes wildcard characters (`+` or `#`). The `+` wildcard matches a single level in the topic hierarchy, while the `#` wildcard matches multiple levels. Below are examples of
    how to use wildcards for subscriptions:

    Using the `+` wildcard:

    - Subscribing to `sensor/+/temperature` matches topics like `sensor/bedroom/temperature`, `sensor/kitchen/temperature`, etc.
    - Subscribing to `home/+/light/+` matches topics like `home/livingroom/light/on`, `home/bedroom/light/off`, etc.

    Using the `#` wildcard:

    - Subscribing to `home/bedroom/#` matches topics like `home/bedroom/light/on`, `home/bedroom/temperature`, and their subtopics.
    - Subscribing to `home/+/#` matches topics like `home/bedroom/light/on`, `home/kitchen/temperature`, and their subtopics.
    - Subscribing to `#` matches all topics.

    Note that wildcard subscriptions can result in a large number of topics being subscribed to, so performance and resource consumption should be carefully considered when using wildcard subscriptions.

    Similar to publishing messages, when subscribing to topics, the client needs to specify the QoS for that topic. BifroMQ, according to the MQTT protocol, will take the minimum of the QoS of the published message and the subscribed
    topic when forwarding messages, i.e., `Min(PublishQoS, SubscribeQoS)`. This means that even if the subscriber has subscribed to a topic with QoS2, it might still receive messages with QoS0.

---

<a id="user_guide-basic-shared_sub"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/basic/shared_sub/ -->

<!-- page_index: 27 -->

# Shared Subscriptions

Version: 4.0.0-incubating

# Shared Subscriptions

MQTT Shared Subscriptions are a feature of the MQTT protocol that enables multiple subscribers to receive messages from the same topic in a fair manner.

To initiate a shared subscription, you should subscribe to a topic using the `$share/{groupName}/{topicFilter}` format. `{groupName}` refers to the name of the group sharing the subscription, as demonstrated with `group1` in the diagram.
When subscribers choose to subscribe using the same topicFilter and groupName, they become part of the same shared group. Whenever a publisher sends a message, BifroMQ determines which subscriber in the group receives the message based on the defined sharing strategy.

<a id="user_guide-basic-shared_sub--sharing-strategies"></a>

### Sharing Strategies

Sharing strategies define the method used to decide which subscriber within the shared group receives the message when it is sent. The MQTT protocol does not explicitly detail these strategies, but based on the use cases for shared subscriptions, BifroMQ implements two strategies:

- **Random Selection (`$share/{groupName}/topicFilter`)**: Utilizing the `$share` prefix for shared subscriptions, this strategy is ideal for applications where the order of message processing is not crucial.
- **Ordered Binding (`$oshare/{groupName}/topicFilter`)**: By employing the `$oshare` prefix for shared subscriptions, this strategy ensures messages from the same client connection and topic are forwarded in the order they were published to the same subscriber. This is suitable for scenarios where the sequence of messages is important.

**Note**: The combination of a sharing strategy and group name creates a unique identifier, meaning that shared subscriptions with the same group name but different prefixes (`$share` and `$oshare`) will establish separate shared groups, each with its own sharing strategy.

- [Sharing Strategies](#user_guide-basic-shared_sub--sharing-strategies)

---

<a id="user_guide-integration-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/integration/intro/ -->

<!-- page_index: 28 -->

# Data Integration Overview

Version: 4.0.0-incubating

# Data Integration Overview

BifroMQ focuses on being deeply integrated, providing foundational MQTT capabilities for various messaging systems. This guide primarily introduces the recommended methods for data integration with BifroMQ.

<a id="user_guide-integration-intro--understanding-data-integration-with-bifromq"></a>

## Understanding Data Integration with BifroMQ

Data integration with BifroMQ involves a bidirectional flow of messages between BifroMQ and external systems, including databases, rule-based message forwarding systems, other messaging middleware, or another MQTT Broker. This integration encompasses several key aspects:

- **Protocol Conversion**
- **Service Quality Matching**
- **Message Routing**
- **Flow Control**
- **Monitoring**
- **Scalability Considerations**

<a id="user_guide-integration-intro--common-pattern"></a>

### Common Pattern

A common architectural pattern involves embedding downstream system clients directly within the MQTT Broker. This method utilizes specific communication mechanisms and mapping logic to achieve protocol conversion, treating the MQTT protocol implementation and integration with heterogeneous systems as a unified whole, providing out-of-the-box integration capabilities.

<a id="user_guide-integration-intro--non-coupled-pattern"></a>

### Non-Coupled Pattern

Contrary to the common practice, BifroMQ recommends a non-coupled approach for data integration: Integration logic directly utilizes the MQTT protocol as a client to subscribe to messages from BifroMQ. This architectural pattern allows the integration module to be reused across different MQTT Brokers, hence the BifroMQ project itself does not include out-of-the-box data integration functionalities.

<a id="user_guide-integration-intro--directions-of-message-flow-integration"></a>

## Directions of Message Flow Integration

There are two primary directions for message flow integration with BifroMQ:

<a id="user_guide-integration-intro--from-bifromq-to-external-systems"></a>

### From BifroMQ to External Systems

BifroMQ recommends using the [shared subscription](#user_guide-basic-shared_sub) feature to balance the message load sent to downstream systems, utilizing MQTT's QoS capabilities for semantic message forwarding. This approach requires maintaining a set of MQTT client connections that subscribe to BifroMQ. Notably, BifroMQ supports shared subscriptions across MQTT versions 3.1, 3.1.1, and 5.0.

<a id="user_guide-integration-intro--from-external-systems-to-bifromq"></a>

### From External Systems to BifroMQ

External systems can publish messages to BifroMQ using direct MQTT client connections or the [HTTP Restful API](#user_guide-api-intro), providing a straightforward method for message injection into the BifroMQ deployment.

<a id="user_guide-integration-intro--considerations-for-implementing-data-integration"></a>

## Considerations for Implementing Data Integration

When integrating data with BifroMQ, consider the following:

- **Bandwidth Limitations**: BifroMQ defaults to a bandwidth limit of 512kb/s per MQTT connection, adjustable via Tenant Settings. Calculating the number of connections needed based on actual business demands when receiving messages forwarded through shared subscriptions is crucial.
- **Flow Control**: Using MQTT as the forwarding protocol inherently provides flow control. Downstream systems must have sufficient resources to receive forwarded messages to avoid backpressure-induced message loss.
- **Monitoring**: Thanks to the use of the MQTT protocol, the monitoring metrics provided by BifroMQ can be directly reused during the message forwarding phase, simplifying the integration monitoring process.

<a id="user_guide-integration-intro--reference-for-starters"></a>

## Reference for Starters

This [project](https://github.com/bifromqio/bifromq-data-integration) showcases the concepts discussed in this guide and can serve as a reference for similar projects.

- [Understanding Data Integration with BifroMQ](#user_guide-integration-intro--understanding-data-integration-with-bifromq)
  - [Common Pattern](#user_guide-integration-intro--common-pattern)
  - [Non-Coupled Pattern](#user_guide-integration-intro--non-coupled-pattern)
- [Directions of Message Flow Integration](#user_guide-integration-intro--directions-of-message-flow-integration)
  - [From BifroMQ to External Systems](#user_guide-integration-intro--from-bifromq-to-external-systems)
  - [From External Systems to BifroMQ](#user_guide-integration-intro--from-external-systems-to-bifromq)
- [Considerations for Implementing Data Integration](#user_guide-integration-intro--considerations-for-implementing-data-integration)
- [Reference for Starters](#user_guide-integration-intro--reference-for-starters)

---

<a id="user_guide-api-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/api/intro/ -->

<!-- page_index: 29 -->

# API Overview

Version: 4.0.0-incubating

# API Overview

BifroMQ incorporates built-in API capabilities, allowing for operations such as disconnecting client connections, querying session status, publishing messages, managing subscriptions and cluster state inspection. These features enable the integration of BifroMQ's management operations into custom management workflows.

<a id="user_guide-api-intro--deployment"></a>

## Deployment

By default, the API service functionality is automatically enabled on every BifroMQ service node using port 8091. For more setting options, refer to the [configuration file](#admin_guide-configuration-config_file_manual). API requests can be sent to any node; high availability comes from running the API Server as an overlay cluster with front-end L7 load balancing (see [API Server load balancing](#cluster-loadbalance-apiserver)).

<a id="user_guide-api-intro--swagger-generation"></a>

## Swagger generation

The Swagger definition is generated automatically during build:

- `mvn -pl bifromq-apiserver -am package` produces `bifromq-apiserver/target/swagger/BifroMQ-API.yaml`.
- The build copies it to the aggregated output at `target/output/site/swagger/BifroMQ-API.yaml`.

See the [OpenAPI reference](#user_guide-api-openapi) to view the generated spec inline.

- [Deployment](#user_guide-api-intro--deployment)
- [Swagger generation](#user_guide-api-intro--swagger-generation)

---

<a id="user_guide-api-openapi"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/user_guide/api/openapi/ -->

<!-- page_index: 30 -->

# OpenAPI Reference

Version: 4.0.0-incubating

# OpenAPI Reference

The full OpenAPI definition is generated from the codebase (see [Swagger generation](#user_guide-api-intro--swagger-generation)).

The live reference below renders `BifroMQ-API.yaml` directly.

<svg class="sc-iJrDZr kVRcFp search-icon" version="1.1" viewbox="0 0 1000 1000" x="0px" xmlns="http://www.w3.org/2000/svg" y="0px"><path d="M968.2,849.4L667.3,549c83.9-136.5,66.7-317.4-51.7-435.6C477.1-25,252.5-25,113.9,113.4c-138.5,138.3-138.5,362.6,0,501C219.2,730.1,413.2,743,547.6,666.5l301.9,301.4c43.6,43.6,76.9,14.9,104.2-12.4C981,928.3,1011.8,893,968.2,849.4z M524.5,522c-88.9,88.7-233,88.7-321.8,0c-88.9-88.7-88.9-232.6,0-321.3c88.9-88.7,233-88.7,321.8,0C613.4,289.4,613.4,433.3,524.5,522z"></path></svg>

- putDisable store balancer
- putEnable store balancer
- postRetain a message to given topic
- delExpire all retain messages using given expiry time
- getGet the session information of the given user and client id
- delExpire inactive persistent session using given expiry time
- getGet the store balancer state
- getGet cluster membership known from current node
- getGet the expected load rules of a store balancer
- putSet the expected load rules of a store balancer
- getGet the service landscape information
- getGet the inbox state of a mqtt session
- getGet the store landscape information
- getGet the ranges information in a store node
- getGet the traffic rules of a service
- putSet the traffic rules of a service
- delDisconnect a MQTT client connection
- getList the name of services in BifroMQ cluster
- getList the name of stores in BifroMQ cluster
- postPublish a message to given topic
- putSet group tag to a server in a service
- putAdd a topic subscription to a mqtt session
- delRemove a topic subscription from a mqtt session

[API docs by Redocly](https://redocly.com/redoc/)

<svg class="" height="15" style="transform:translate(2px, -4px) rotate(180deg);transition:transform 0.2s ease" version="1.1" viewbox="0 0 926.23699 573.74994" width="15" x="0px" y="0px"><g transform="translate(904.92214,-879.1482)"><path d="
          m -673.67664,1221.6502 -231.2455,-231.24803 55.6165,
          -55.627 c 30.5891,-30.59485 56.1806,-55.627 56.8701,-55.627 0.6894,
          0 79.8637,78.60862 175.9427,174.68583 l 174.6892,174.6858 174.6892,
          -174.6858 c 96.079,-96.07721 175.253196,-174.68583 175.942696,
          -174.68583 0.6895,0 26.281,25.03215 56.8701,
          55.627 l 55.6165,55.627 -231.245496,231.24803 c -127.185,127.1864
          -231.5279,231.248 -231.873,231.248 -0.3451,0 -104.688,
          -104.0616 -231.873,-231.248 z
        " fill="currentColor"></path></g></svg>
<svg class="" height="15" style="transform:translate(2px, 4px);transition:transform 0.2s ease" version="1.1" viewbox="0 0 926.23699 573.74994" width="15" x="0px" y="0px"><g transform="translate(904.92214,-879.1482)"><path d="
          m -673.67664,1221.6502 -231.2455,-231.24803 55.6165,
          -55.627 c 30.5891,-30.59485 56.1806,-55.627 56.8701,-55.627 0.6894,
          0 79.8637,78.60862 175.9427,174.68583 l 174.6892,174.6858 174.6892,
          -174.6858 c 96.079,-96.07721 175.253196,-174.68583 175.942696,
          -174.68583 0.6895,0 26.281,25.03215 56.8701,
          55.627 l 55.6165,55.627 -231.245496,231.24803 c -127.185,127.1864
          -231.5279,231.248 -231.873,231.248 -0.3451,0 -104.688,
          -104.0616 -231.873,-231.248 z
        " fill="currentColor"></path></g></svg>

# BifroMQ RESTful API (4.0.0-incubating)

Download OpenAPI specification:[Download](assets/files/bifromq_310005b885c28bdf.yaml)

## Disable store balancer

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the store name&lt;/p&gt;
"><p>the store name</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="balancer_factory_class"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">balancer_factory_class</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the full qualified name of balancer factory class configured for the store&lt;/p&gt;
"><p>the full qualified name of balancer factory class configured for the store</p>
</div></div></div></td></tr></tbody></table>

##### Request Body schema: application/json

 *Schema not provided*

### Responses

**200**

Success

put/store/balancer/disable
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/store/balancer/disable

## Enable store balancer

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the store name&lt;/p&gt;
"><p>the store name</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="balancer_factory_class"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">balancer_factory_class</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the full qualified name of balancer factory class configured for the store&lt;/p&gt;
"><p>the full qualified name of balancer factory class configured for the store</p>
</div></div></div></td></tr></tbody></table>

##### Request Body schema: application/json

 *Schema not provided*

### Responses

**200**

Success

put/store/balancer/enable
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/store/balancer/enable

## Retain a message to given topic

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional, caller provided request id&lt;/p&gt;
"><p>optional, caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the tenant id&lt;/p&gt;
"><p>the tenant id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="topic"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">topic</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the message topic&lt;/p&gt;
"><p>the message topic</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="qos"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">qos</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int32<!-- -->&gt;<!-- --> </span></div><div><span class="sc-gUjXxo frcCjv"> <!-- -->Enum<!-- -->:</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">0</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">1</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">2</span> </div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;QoS of the message to be retained&lt;/p&gt;
"><p>QoS of the message to be retained</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="expiry_seconds"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">expiry_seconds</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int32<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the message expiry seconds&lt;/p&gt;
"><p>the message expiry seconds</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_type"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_type</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the caller client type&lt;/p&gt;
"><p>the caller client type</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_meta_*"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_meta_*</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the metadata header about caller client, must be started with client_meta_&lt;/p&gt;
"><p>the metadata header about caller client, must be started with client_meta_</p>
</div></div></div></td></tr></tbody></table>

##### Request Body schema: application/octet-stream required

Message payload will be treated as binary

 *Schema not provided*

### Responses

<svg aria-hidden="true" class="sc-eTNem gSSIGk" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**400**

Invalid QoS or expiry seconds

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**403**

Unaccepted Topic

post/retain
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/retain

## Expire all retain messages using given expiry time

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the tenant id&lt;/p&gt;
"><p>the tenant id</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="expiry_seconds"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">expiry_seconds</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int32<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the overridden retain message expiry time in seconds&lt;/p&gt;
"><p>the overridden retain message expiry time in seconds</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

delete/retain
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/retain

## Get the session information of the given user and client id

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of tenant&lt;/p&gt;
"><p>the id of tenant</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="user_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">user_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of user who established the session&lt;/p&gt;
"><p>the id of user who established the session</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the client id of the mqtt session&lt;/p&gt;
"><p>the client id of the mqtt session</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

No session found for the given user and client id

get/session
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/session

## Expire inactive persistent session using given expiry time

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the tenant id&lt;/p&gt;
"><p>the tenant id</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="expiry_seconds"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">expiry_seconds</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int32<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the overridden session expiry time in seconds&lt;/p&gt;
"><p>the overridden session expiry time in seconds</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

delete/session
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/session

## Get the store balancer state

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the store name&lt;/p&gt;
"><p>the store name</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="balancer_factory_class"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">balancer_factory_class</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the full qualified name of balancer factory class configured for the store&lt;/p&gt;
"><p>the full qualified name of balancer factory class configured for the store</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

Balancer not found for the store

get/store/balancer
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/store/balancer

## Get cluster membership known from current node

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

get/cluster
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/cluster

## Get the expected load rules of a store balancer

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the service name&lt;/p&gt;
"><p>the service name</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="balancer_factory_class"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">balancer_factory_class</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the full qualified name of balancer factory class configured for the store&lt;/p&gt;
"><p>the full qualified name of balancer factory class configured for the store</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

Not load rules ever set for the store balancer

get/store/balancer/rules
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/store/balancer/rules

## Set the expected load rules of a store balancer

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the store name&lt;/p&gt;
"><p>the store name</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="balancer_factory_class"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">balancer_factory_class</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the full qualified name of balancer factory class configured for the store&lt;/p&gt;
"><p>the full qualified name of balancer factory class configured for the store</p>
</div></div></div></td></tr></tbody></table>

##### Request Body schema: application/json

 *Schema not provided*

### Responses

**200**

Success

put/store/balancer/rules
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/store/balancer/rules

## Get the service landscape information

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="service_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">service_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the service name&lt;/p&gt;
"><p>the service name</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

Service not found

get/service/landscape
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/service/landscape

## Get the inbox state of a mqtt session

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of tenant&lt;/p&gt;
"><p>the id of tenant</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="user_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">user_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of user who established the session&lt;/p&gt;
"><p>the id of user who established the session</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the client id of the mqtt session&lt;/p&gt;
"><p>the client id of the mqtt session</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

No session found for the given user and client id

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**409**

Try later

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**429**

Too many requests

get/session/inbox
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/session/inbox

## Get the store landscape information

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the store name&lt;/p&gt;
"><p>the store name</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

Store not found

get/store/landscape
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/store/landscape

## Get the ranges information in a store node

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the store name&lt;/p&gt;
"><p>the store name</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="store_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">store_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the store id&lt;/p&gt;
"><p>the store id</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

Store or store server not found

get/store/ranges
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/store/ranges

## Get the traffic rules of a service

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="service_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">service_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the service name&lt;/p&gt;
"><p>the service name</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

Service not found

get/service/traffic
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/service/traffic

## Set the traffic rules of a service

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="service_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">service_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the service name&lt;/p&gt;
"><p>the service name</p>
</div></div></div></td></tr></tbody></table>

##### Request Body schema: application/json

 *Schema not provided*

### Responses

**200**

Success

**400**

Bad Request

put/service/traffic
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/service/traffic

## Disconnect a MQTT client connection

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the tenant id&lt;/p&gt;
"><p>the tenant id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="user_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">user_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the user id of the MQTT client connection to be disconnected&lt;/p&gt;
"><p>the user id of the MQTT client connection to be disconnected</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the client id of the mqtt session&lt;/p&gt;
"><p>the client id of the mqtt session</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="server_redirect"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">server_redirect</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div><div><span class="sc-gUjXxo frcCjv"> <!-- -->Enum<!-- -->:</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">"no"</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">"move"</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">"temp_use"</span> </div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;indicate if the client should redirect to another server&lt;/p&gt;
"><p>indicate if the client should redirect to another server</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="server_reference"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">server_reference</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span><span> <span class="sc-gUjXxo sc-cmfmEr frcCjv eNcZim"> <!-- -->&lt;= 65535 characters<!-- --> </span></span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;indicate the server reference to redirect to&lt;/p&gt;
"><p>indicate the server reference to redirect to</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_type"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_type</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the caller client type&lt;/p&gt;
"><p>the caller client type</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_meta_*"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_meta_*</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the metadata header about the caller client, must be started with client_meta_&lt;/p&gt;
"><p>the metadata header about the caller client, must be started with client_meta_</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**404**

Not Found

delete/kill
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/kill

## List the name of services in BifroMQ cluster

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

get/services
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/services

## List the name of stores in BifroMQ cluster

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

get/stores
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/stores

## Publish a message to given topic

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the tenant id&lt;/p&gt;
"><p>the tenant id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="topic"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">topic</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the message topic&lt;/p&gt;
"><p>the message topic</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="qos"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">qos</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int32<!-- -->&gt;<!-- --> </span></div><div><span class="sc-gUjXxo frcCjv"> <!-- -->Enum<!-- -->:</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">0</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">1</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">2</span> </div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;QoS of the message to be published&lt;/p&gt;
"><p>QoS of the message to be published</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="expiry_seconds"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">expiry_seconds</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int32<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the message expiry seconds, must be positive&lt;/p&gt;
"><p>the message expiry seconds, must be positive</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_type"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_type</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the caller client type&lt;/p&gt;
"><p>the caller client type</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_meta_*"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_meta_*</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the metadata header about caller client, must be started with client_meta_&lt;/p&gt;
"><p>the metadata header about caller client, must be started with client_meta_</p>
</div></div></div></td></tr></tbody></table>

##### Request Body schema: application/octet-stream required

Message payload will be treated as binary

 *Schema not provided*

### Responses

<svg aria-hidden="true" class="sc-eTNem gSSIGk" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**200**

Success

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**400**

Invalid QoS or expiry seconds

<svg aria-hidden="true" class="sc-eTNem imkAqM" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>
**403**

Unaccepted Topic

post/pub
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/pub

## Set group tag to a server in a service

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="service_name"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">service_name</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the service name&lt;/p&gt;
"><p>the service name</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="server_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">server_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the service server id&lt;/p&gt;
"><p>the service server id</p>
</div></div></div></td></tr></tbody></table>

##### Request Body schema: application/json required

Array

string

### Responses

**200**

Success

**400**

Bad Request

**404**

Service or server not found

put/service/group
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/service/group

### Request samples

<ul class="react-tabs__tab-list" role="tablist"><li aria-controls="panel_R_2addaq7dalbah_0" aria-disabled="false" aria-selected="true" class="react-tabs__tab react-tabs__tab--selected" data-rttab="true" id="tab_R_2addaq7dalbah_0" role="tab" tabindex="0">Payload</li></ul>

Content type

application/json

Copy

`[

- "string"

]`

## Add a topic subscription to a mqtt session

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of tenant&lt;/p&gt;
"><p>the id of tenant</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="user_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">user_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of user who established the session&lt;/p&gt;
"><p>the id of user who established the session</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the client id of the mqtt session&lt;/p&gt;
"><p>the client id of the mqtt session</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="topic_filter"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">topic_filter</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the topic filter to add&lt;/p&gt;
"><p>the topic filter to add</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="sub_qos"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">sub_qos</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int32<!-- -->&gt;<!-- --> </span></div><div><span class="sc-gUjXxo frcCjv"> <!-- -->Enum<!-- -->:</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">0</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">1</span> <span class="sc-gUjXxo sc-ldgPul frcCjv dXemGY">2</span> </div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the qos of the subscription&lt;/p&gt;
"><p>the qos of the subscription</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

**400**

Request is invalid

**401**

Unauthorized to make subscription using the given topic filter

**404**

No session found for the given user and client id

put/sub
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/sub

## Remove a topic subscription from a mqtt session

##### header Parameters

<table class="sc-hIPCAM jIDPJw"><tbody><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="req_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">req_id</span></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">integer</span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf"> <!-- -->&lt;<!-- -->int64<!-- -->&gt;<!-- --> </span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;optional caller provided request id&lt;/p&gt;
"><p>optional caller provided request id</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="tenant_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">tenant_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of tenant&lt;/p&gt;
"><p>the id of tenant</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="user_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">user_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the id of user who established the session&lt;/p&gt;
"><p>the id of user who established the session</p>
</div></div></div></td></tr><tr class=""><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="client_id"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">client_id</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the client id of the mqtt session&lt;/p&gt;
"><p>the client id of the mqtt session</p>
</div></div></div></td></tr><tr class="last"><td class="sc-hABAzn sc-fHekdU hYqafI fLtkWi" kind="field" title="topic_filter"><span class="sc-ifyqMW jEjUYa"></span><span class="property-name">topic_filter</span><div class="sc-gUjXxo sc-eKzwpd frcCjv bindgb">required</div></td><td class="sc-blmETN goCQmO"><div><div><span class="sc-gUjXxo sc-kZOrUD frcCjv eZjMvI"></span><span class="sc-gUjXxo sc-iLXwom frcCjv bTRxzf">string</span></div> <div><div class="sc-iKOlBD sc-cCzKKD kTLocR fQpLDr" html="&lt;p&gt;the topic filter to remove&lt;/p&gt;
"><p>the topic filter to remove</p>
</div></div></div></td></tr></tbody></table>

### Responses

**200**

Success

**401**

Unauthorized to remove subscription of the given topic filter

**404**

No session found for the given user and client id

delete/unsub
<svg aria-hidden="true" class="sc-eTNem jDFKUE" style="margin-right:-25px" version="1.1" viewbox="0 0 24 24" x="0" xmlns="http://www.w3.org/2000/svg" y="0"><polygon points="17.3 8.3 12 13.6 6.7 8.3 5.3 9.7 12 16.4 18.7 9.7 "></polygon></svg>

https://bifromq.apache.org/unsub

---

<a id="plugin-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/intro/ -->

<!-- page_index: 31 -->

# Plugin Overview

Version: 4.0.0-incubating

# Plugin Overview

The plugin mechanism is a primary way for BifroMQ to deeply integrate with business systems. Currently, BifroMQ exposes five types of plugin extension interfaces to cater to different usage scenarios:

- **[Auth Provider](#plugin-auth_provider)**: Integrates authentication and topic Pub/Sub authorization logic.
- **[Client Balancer](#plugin-client_balancer)**: Inject your customized client balancing strategy in cooporative way.
- **[Event Collector](#plugin-event_collector)**: Collects runtime events to implement various event-driven business logic.
- **[Resource Throttler](#plugin-resource_throttler)**: Dynamically controls resource usage at the tenant level.
- **[Setting Provider](#plugin-setting_provider-intro)**: Dynamically adjusts tenant-specific MQTT protocol settings.

<a id="plugin-intro--plugin-development"></a>

## Plugin Development

- Project Organization: A pf4j project can contain multiple plugin implementations.
- Singleton Plugins: Extensions of AuthProvider, ClientBalancer, Resource Throttler, and Setting Provider types are singletons at runtime. The specific type to be loaded needs to be specified through a configuration file.
- Multiple Instance Plugins: EventCollector allows for multiple different types of instances to exist, with interface methods of these EventCollector instances being called back simultaneously.
- Quick Start：We provide a plugin project scaffolding tool, allowing you to start plugin development quickly. See [Start a BifroMQ Plugin Project Quickly](#plugin-plugin_practice--start-a-bifromq-plugin-project-quickly)

<a id="plugin-intro--plugin-deployment"></a>

## Plugin Deployment

- Plugin Directory: BifroMQ loads plugin implementations (JAR files or directories) from the plugins subdirectory within its installation directory.
- Classloader Isolation: Each plugin uses an independent ClassLoader to isolate its code from BifroMQ and other plugins.
- BifroMQ provides class loading for the following commonly used packages:
  - `org.apache.bifromq.type.*`
  - `org.apache.bifromq.plugin.*`
  - `io.micrometer.core.*`
  - `com.google.protobuf.*`

**Note**: Some 3rd party dependencies used in a plugin may use the `Thread.currentThread().getContextClassLoader()` to load classes, which can result in a `ClassNotFoundException`. To prevent this, you can include the logic for loading dependency classes within the following try-finally structure:

```java
public pluginMethod() {
    ClassLoader contextLoader = Thread.currentThread().getContextClassLoader();
    // using PluginClassLoader for context class loader
    Thread.currentThread().setContextClassLoader(this.getClass().getClassLoader());
    try {
        // loading 3rd party dependencies
    } finally {
        Thread.currentThread().setContextClassLoader(contextLoader);
    }
}
```

<a id="plugin-intro--version-compatibility"></a>

## Version Compatibility

To ensure optimal compatibility and avoid potential issues, it is advised to deploy your custom plugin with the main version of the BifroMQ main program aligned.

Example:

- If BifroMQ's version is 4.x.y, then the version of the plugin interface definition modules used should also be 4.x.y.

<a id="plugin-intro--performance-considerations"></a>

## Performance Considerations

BifroMQ calls plugin interface methods on worker threads. Ensure plugin interface implementations are lightweight and non-blocking to avoid negatively impacting performance.

<a id="plugin-intro--configuring-parameters-in-demo-plugin"></a>

## Configuring Parameters in Demo Plugin

BifroMQ supports configuring the demo plugin's Prometheus exporter via environment variables or JVM system properties:

- **Metrics path**: `PLUGIN_PROMETHEUS_CONTEXT` (env) or `-DPLUGIN_PROMETHEUS_CONTEXT=<path>` (JVM). Default `/metrics`. A leading `/` is added automatically if omitted.
- **Exporter port**: `PLUGIN_PROMETHEUS_PORT` (env) or `-DPLUGIN_PROMETHEUS_PORT=<port>` (JVM). Default `9090`. Non-numeric values fall back to `9090`.

Example:

```bash
export PLUGIN_PROMETHEUS_PORT=9200
export PLUGIN_PROMETHEUS_CONTEXT=/demo-metrics
# or pass as JVM args: -DPLUGIN_PROMETHEUS_PORT=9200 -DPLUGIN_PROMETHEUS_CONTEXT=/demo-metrics
```

- [Plugin Development](#plugin-intro--plugin-development)
- [Plugin Deployment](#plugin-intro--plugin-deployment)
- [Version Compatibility](#plugin-intro--version-compatibility)
- [Performance Considerations](#plugin-intro--performance-considerations)
- [Configuring Parameters in Demo Plugin](#plugin-intro--configuring-parameters-in-demo-plugin)

---

<a id="plugin-auth_provider"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/auth_provider/ -->

<!-- page_index: 32 -->

# Auth Provider

Version: 4.0.0-incubating

# Auth Provider

The Auth Provider plugin enhances BifroMQ by integrating authentication and authorization functionalities for MQTT clients and Pub/Sub operations. The plugin's interface is detailed in the following Maven module:

```xml
<dependency>
  <groupId>org.apache.bifromq</groupId>
  <artifactId>bifromq-plugin-auth-provider</artifactId>
  <version>4.0.0-incubating</version>
</dependency>
```

BifroMQ operates with only one instance of the Auth Provider at any given time. The specific class to be loaded can be configured in [configuration file](#admin_guide-configuration-config_file_manual) by specifying its Fully
Qualified Name (FQN):

```yaml
authProviderFQN: "YOUR_AUTH_PROVIDER_CLASS"
```

<a id="plugin-auth_provider--authentication"></a>

## Authentication

During the connection phase, BifroMQ invokes the Auth Provider Plugin's interface methods to authenticate MQTT client connections across versions 3.1, 3.1.1, and 5.0:

```java
// Authenticate MQTT 3.1 and 3.1.1 clients
CompletableFuture<MQTT3AuthResult> auth(MQTT3AuthData authData);

// Authenticate MQTT 5.0 clients
CompletableFuture<MQTT5AuthResult> auth(MQTT5AuthData authData);

// Enhanced authentication for MQTT 5.0 clients
CompletableFuture<MQTT5ExtendedAuthResult> extendedAuth(MQTT5ExtendedAuthData authData);
```

It's crucial to ensure that the implementations of these interface methods are efficient and non-blocking to avoid negatively impacting connection performance. For MQTT 5.0, BifroMQ supports two methods of authentication: Basic and
Extended. The Basic authentication provides compatibility with MQTT 3 behavior by default.

Protobuf objects are utilized for the parameters and return types of these interface methods.

<a id="plugin-auth_provider--mqtt3authdata"></a>

#### [MQTT3AuthData](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt3_auth_types.proto)

```protobuf
message MQTT3AuthData{
  bool isMQIsdp = 1; // true indicates the client is using MQTT 3.1
  optional string username = 2; // username specified by the client in Connect
  optional bytes password = 3; // password specified by the client in Connect
  optional bytes cert = 4; // TLS certificate used by the client in Base64 encoding
  optional string clientId = 5; // client identifier specified by the client in Connect
  string remoteAddr = 6; // source address of the client
  uint32 remotePort = 7; // port of the client
  string channelId = 8; // globally unique identifier for this connection
}
```

<a id="plugin-auth_provider--mqtt3authresult"></a>

#### [MQTT3AuthResult](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt3_auth_types.proto)

```protobuf
message Ok{
  string tenantId = 1;
  string userId = 2;
  map<string, string> attrs = 3; // additional attributes filled by auth provider plugin which will be copied to ClientInfo
}

message Reject{
  enum Code {
    BadPass = 0;
    NotAuthorized = 1;
    Error = 2;
  }
  Code code = 1;
  optional string tenantId = 2; // optional if tenant can be determined
  optional string userId = 3; // optional if user can be determined
  optional string reason = 4; // optional description}

  message MQTT3AuthResult {
    oneof Type{
      Ok ok = 1;
      Reject reject = 2;
    }
  }
```

<a id="plugin-auth_provider--mqtt5authdata-and-mqtt5extendedauthdata"></a>

#### [MQTT5AuthData](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt5_auth_types.proto) and [MQTT5ExtendedAuthData](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt5_auth_types.proto)

```protobuf
message MQTT5AuthData{
  optional string username = 1;
  optional bytes password = 2;
  optional bytes cert = 3;
  optional string clientId = 4;
  string remoteAddr = 5;
  uint32 remotePort = 6;
  string channelId = 7;
  bool responseInfo = 8; // for MQTT5 request/response use case
  commontype.UserProperties userProps = 9;
}

message MQTT5ExtendedAuthData{
  message Initial{
    MQTT5AuthData basic = 1;
    string authMethod = 2;
    bytes authData = 3;
  }
  message Auth{
    string authMethod = 1;
    bytes authData = 2;
    commontype.UserProperties userProps = 3;
    bool isReAuth = 4;
  }
  oneof Type{
    Initial initial = 1;
    Auth auth = 2;
  }
}
```

<a id="plugin-auth_provider--mqtt5authresult-and-mqtt5extendedauthresult"></a>

#### [MQTT5AuthResult](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt5_auth_types.proto) and [MQTT5ExtendedAuthResult](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt5_auth_types.proto)

```protobuf
message Success{
  string tenantId = 1;
  string userId = 2;
  map<string, string> attrs = 3; // additional attributes filled by auth provider plugin which will be copied to ClientInfo
  optional string ResponseInfo = 4; // for mqtt5 request/response use case
  commontype.UserProperties userProps = 5; // user properties return back via mqtt5 connack
}

message Failed{
  enum Code {
    BadPass = 0;
    NotAuthorized = 1;
    Banned = 2;
    BadAuthMethod = 3;
    Error = 4;
  }
  Code code = 1;
  optional string tenantId = 2; // optional if tenant can be determined
  optional string userId = 3; // optional if user can be determined
  optional string reason = 4; // optional description
  commontype.UserProperties userProps = 5; // user properties return back via mqtt5 connack
}

message Continue{
  bytes authData = 1;
  optional string tenantId = 2; // optional if tenant can be determined
  optional string userId = 3; // optional if user can be determined
  optional string reason = 4;
  commontype.UserProperties userProps = 5;
}

message MQTT5AuthResult {
  oneof Type{
    Success success = 1;
    Failed failed = 2;
  }
}

message MQTT5ExtendedAuthResult {
  oneof Type{
    Success success = 1;
    Continue continue = 2;
    Failed failed = 3;
  }
}
```

Successful authentication returns an Ok structure with tenantId, userId, and optionally additional metadata in attrs, which is copied to ClientInfo. A Reject return indicates failure due to incorrect authentication info (BadPass), unauthorized access (NotAuthorized), or internal errors (Error), with detailed explanations in optional fields.

<a id="plugin-auth_provider--authorization"></a>

## Authorization

BifroMQ checks permissions for Publish, Subscribe, and Unsubscribe actions via:

```java
CompletableFuture<CheckResult> checkPermission(ClientInfo client, MQTTAction action);
```

Ensuring the `checkPermission` method's implementation is efficient and non-blocking is critical to prevent any negative impact on messaging performance. The method leverages ClientInfo with metadata returned from authentication, enabling
JWT-like authentication and authorization mechanisms. Additionally, the permission check method is not differentiated by the client's MQTT protocol version. However, for clients using MQTT 5.0, the MQTTAction object will contain
UserProperties from the Control Packets.

In cases of authorization failure for MQTT 5.0 clients, UserProperties included in the result are relayed back to the client within the corresponding MQTT Control Packets' UserProperties, aiding in problem diagnosis.

The checkPermission method's parameters and return type are also defined by Protobuf.

<a id="plugin-auth_provider--clientinfo"></a>

#### [ClientInfo](https://github.com/apache/bifromq/blob/main/bifromq-common-type/src/main/proto/commontype/ClientInfo.proto)

```protobuf
message ClientInfo{
  string tenantId = 1;
  string type = 2; // the type of the calling client, e.g. "mqtt"
  map<string, string> metadata = 3; // the metadata of the client
}
```

BifroMQ will include the following predefined metadata in the `metadata` property of the `ClientInfo` object:

<table><thead><tr><th>Key</th><th>Description</th><th>Possible Values</th></tr></thead><tbody><tr><td><code>ver</code></td><td>MQTT protocol version</td><td><code>"3"</code> (MQTT 3.1), <code>"4"</code> (MQTT 3.1.1), <code>"5"</code> (MQTT 5)</td></tr><tr><td><code>userId</code></td><td>User ID</td><td>User-defined string</td></tr><tr><td><code>clientId</code></td><td>Client ID</td><td>User-defined string</td></tr><tr><td><code>channelId</code></td><td>Channel ID</td><td>System-generated unique identifier</td></tr><tr><td><code>address</code></td><td>Client address</td><td>IP address or hostname of the client</td></tr><tr><td><code>broker</code></td><td>Broker the client is connected to</td><td>Broker identifier</td></tr><tr><td><code>sessionType</code></td><td>Type of session</td><td><code>"t"</code> (Transient), <code>"p"</code> (Persistent)</td></tr><tr><td><code>respInfo</code></td><td>Response information for MQTT 5.0 request/response</td><td>User-defined string</td></tr></tbody></table>

These metadata fields will not be overwritten by attributes (attrs) passed in the authentication result.

<a id="plugin-auth_provider--mqttaction"></a>

#### [MQTTAction](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt_actions.proto)

```protobuf
message PubAction {
  string topic = 1;
  commontype.QoS qos = 2;
  bool isRetained = 3;
  commontype.UserProperties userProps = 4;
}

message SubAction {
  string topicFilter = 1;
  commontype.QoS qos = 2;
  commontype.UserProperties userProps = 5;
}

message UnsubAction {
  string topicFilter = 1;
  commontype.UserProperties userProps = 2;
}

message MQTTAction {
  oneof Type{
    PubAction pub = 1;
    SubAction sub = 2;
    UnsubAction unsub = 3;
  }
}
```

<a id="plugin-auth_provider--checkresult"></a>

#### [CheckResult](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider/src/main/proto/mqtt_actions.proto)

```protobuf
message Granted{
  commontype.UserProperties userProps = 1; // user properties return back via mqtt5 pubAck/pubRel
}

message Denied{
  optional string reason = 1;
  commontype.UserProperties userProps = 2; // user properties return back via mqtt5 pubAck/pubRel or disconnect in case QoS0
}

message Error{
  optional string reason = 1;
  commontype.UserProperties userProps = 2; // user properties return back via mqtt5 pubAck/pubRel or disconnect in case QoS0
}

message CheckResult {
  oneof Type{
    Granted granted = 1;
    Denied denied = 2;
    Error error = 3;
  }
}
```

<a id="plugin-auth_provider--metrics"></a>

## Metrics

Because the two methods of the AuthProvider Plugin are frequently called during connection authentication and the process of handling message publication and subscription forwarding, BifroMQ records and outputs the following metrics to help
plugin implementers observe the performance indicators of the plugin interface methods:

<table><thead><tr><th>Metric Name</th><th>Meter Type</th><th>Tag(<code>method</code>)</th><th>Description</th></tr></thead><tbody><tr><td><code>call.exec.timer</code></td><td>TIMER</td><td>AuthProvider/auth</td><td>Latency for <code>auth</code> call</td></tr><tr><td><code>call.exec.fail.count</code></td><td>COUNTER</td><td>AuthProvider/auth</td><td>Fail counter for <code>auth</code> call</td></tr><tr><td><code>call.exec.timer</code></td><td>TIMER</td><td>AuthProvider/extAuth</td><td>Latency for <code>extendedAuth</code> call</td></tr><tr><td><code>call.exec.fail.count</code></td><td>COUNTER</td><td>AuthProvider/extAuth</td><td>Fail counter for <code>extendedAuth</code> call</td></tr><tr><td><code>call.exec.timer</code></td><td>TIMER</td><td>AuthProvider/check</td><td>Latency for <code>checkPermission</code> call</td></tr><tr><td><code>call.exec.fail.count</code></td><td>COUNTER</td><td>AuthProvider/check</td><td>Fail counter for <code>checkPermission</code> call</td></tr></tbody></table>
<a id="plugin-auth_provider--devonly-mode"></a>

## DevOnly Mode

By default, when no AuthPlugin type is specified, BifroMQ loads the [DevOnlyAuthProvider](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-auth-provider-helper/src/main/java/org/apache/bifromq/plugin/authprovider/DevOnlyAuthProvider.java), bypassing client authentication and permission checks. This mode is strictly for development and testing purposes due to its lack of security.

<a id="plugin-auth_provider--implementation-example"></a>

## Implementation Example

BifroMQ includes a demonstration implementation of a WebHook-based AuthProvider that can be enabled by specifying `authProviderFQN` as `org.apache.bifromq.demo.plugin.DemoAuthProvider` in
the [configuration file](#admin_guide-configuration-config_file_manual). The example implementation uses the JVM startup parameter (`-Dplugin.authprovider.url`) to specify a webhook callback URL.

When BifroMQ triggers the auth method, the plugin initializes an HTTP POST request. Within this request, we transform the protobuf message `MQTT3AuthData` into JSON format to serve as its body. The content of the response body is then interpreted and converted into the appropriate `MQTT3AuthResult` value type.

Below is a simple Node implementation of a WebhookServer for testing the example plugin, with webhook URLs: `http://<ADDR>:<PORT>/auth`, `http://<ADDR>:<PORT>/check` and `http://<ADDR>:<PORT>/register` for authentication, checking pub/sub permission and registering users' information, respectively.

```js
const http = require("http");
const url = require("url");

const authMap = {};
const server = http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  const pathname = parsedUrl.pathname;

  res.setHeader("Content-Type", "text/plain");

  if (pathname === "/auth") {
    let body = "";
    req.on("data", (chunk) => {
      body += chunk.toString();
    });

    req.on("end", () => {
      let data = {};
      try {
        data = JSON.parse(body);
      } catch (error) {
        res.writeHead(400, { "Content-Type": "text/plain" });
        res.end("Invalid JSON");
      }
      if (data.username && data.password) {
        const user = authMap[data.username];
        if (user && user.password === data.password) {
          res.writeHead(200, { "Content-Type": "application/json" });
          res.end(
            JSON.stringify({
              ok: { tenantId: user.tenantId, userId: data.username },
            })
          );
        } else {
          res.writeHead(403, { "Content-Type": "application/json" });
          res.end(JSON.stringify({ reject: "NotAuthorized" }));
        }
      } else {
        res.writeHead(400, { "Content-Type": "text/plain" });
        res.end("Missing username or password");
      }
    });
  } else if (pathname === "/check") {
    if (!req.method === "POST") {
      res.writeHead(404);
    }
    const tenantId = req.headers["tenant_id"];
    const userId = req.headers["user_id"];
    if (tenantId && userId) {
      res.writeHead(200, { "Content-Type": "text/plain" });
      if (userId in authMap) {
        res.end("true");
      } else {
        res.end("false");
      }
    } else {
      res.writeHead(400, { "Content-Type": "text/plain" });
      res.end("Missing user_id or tenant_id");
    }
  } else if (pathname === "/register") {
    const tenantId = req.headers["tenant_id"];
    const userId = req.headers["user_id"];
    const password = req.headers["password"];

    if (tenantId && userId && password) {
      if (!authMap[userId]) {
        authMap[userId] = {
          password: btoa(password),
          tenantId: tenantId,
        };
        res.writeHead(200, { "Content-Type": "text/plain" });
        res.end("User registered successfully");
      } else {
        res.writeHead(400, { "Content-Type": "application/json" });
        res.end("User already exists");
      }
    } else {
      res.writeHead(400, { "Content-Type": "text/plain" });
      res.end("Missing user_id, password or tenant_id");
    }
  } else {
    res.writeHead(404);
    res.end("Not Found");
  }
});

const args = process.argv.slice(2);
const hostname = args[0] || "localhost";
const port = args[1] || 3000;

server.listen(port, hostname, () => {
  console.log(`Server listening on port ${server.address().port}`);
});
```

In this example, we simply convert the registered password to Base64 format for storage. Please choose a more secure and reliable method for handling it in actual usage.

- [Authentication](#plugin-auth_provider--authentication)
- [Authorization](#plugin-auth_provider--authorization)
- [Metrics](#plugin-auth_provider--metrics)
- [DevOnly Mode](#plugin-auth_provider--devonly-mode)
- [Implementation Example](#plugin-auth_provider--implementation-example)

---

<a id="plugin-client_balancer"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/client_balancer/ -->

<!-- page_index: 33 -->

# Client Balancer

Version: 4.0.0-incubating

# Client Balancer

The Client Balancer plugin enables BifroMQ to inject redirection strategies at runtime, providing active control over client connections to manage load distribution.

To integrate the Client Balancer plugin into your BifroMQ deployment, include the following Maven dependency:

```xml
<dependency>
  <groupId>org.apache.bifromq</groupId>
  <artifactId>bifromq-plugin-client-balancer</artifactId>
  <version>4.0.0-incubating</version>
</dependency>
```

<a id="plugin-client_balancer--configuration"></a>

## Configuration

BifroMQ operates with a single `ClientBalancer` instance. You must specify the fully qualified class name (FQN) of your implementation in the [configuration file](#admin_guide-configuration-config_file_manual):

```yaml
clientBalancerFQN: "YOUR_CLIENT_BALANCER_CLASS"
```

<a id="plugin-client_balancer--client-redirection"></a>

## Client Redirection

The `ClientBalancer` interface defines a single method that is invoked by BifroMQ to decide whether a client connection should be redirected:

```java
Optional<Redirection> needRedirect(ClientInfo clientInfo);
```

When BifroMQ determines it's time to evaluate redirection, it calls this method. If a non-empty `Optional` is returned, the client connection will be actively disconnected based on the returned redirection hint.

The `Redirection` record carries the disconnection hint:

```java
public record Redirection(boolean permanentMove, Optional<String> serverReference) { }
```

When the client uses the MQTT 5.0 protocol, BifroMQ maps the redirection information to MQTT disconnect semantics:

- If `permanentMove` is `true`, the client receives `Server moved (0x9D)` reason code.
- If `permanentMove` is `false`, the client receives `Use another server (0x9C)` reason code.
- If `serverReference` is present, its value is included in the `Server Reference` field of the disconnect packet.

<a id="plugin-client_balancer--redirection-evaluation-timing"></a>

## Redirection Evaluation Timing

- **Post-authentication check**: Immediately after a client's authentication, BifroMQ invokes `needRedirect` to determine if the connection should be redirected.
- **Periodic check**: For already established connections, BifroMQ periodically invokes `needRedirect` to evaluate if a redirection is needed.

The default periodic check interval is **600 seconds**. This interval can be adjusted using the [system property](#admin_guide-configuration-bifromq_sys_props): `client_redirect_check_interval_seconds`

<a id="plugin-client_balancer--performance-considerations"></a>

## Performance Considerations

The `ClientBalancer` executes within BifroMQ's core worker threads. Its implementation should remain lightweight and efficient to avoid degrading system performance.

BifroMQ collects metrics to monitor the plugin's performance:

- **`call.exec.timer`**: Tracks the execution duration and frequency of `needRedirect` invocations.
- **`call.exec.fail.count`**: Counts the number of exceptions thrown during `needRedirect` calls.

- [Configuration](#plugin-client_balancer--configuration)
- [Client Redirection](#plugin-client_balancer--client-redirection)
- [Redirection Evaluation Timing](#plugin-client_balancer--redirection-evaluation-timing)
- [Performance Considerations](#plugin-client_balancer--performance-considerations)

---

<a id="plugin-event_collector"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/event_collector/ -->

<!-- page_index: 34 -->

# Event Collector

Version: 4.0.0-incubating

# Event Collector

The Event Collector plugin is designed to capture a variety of events that occur during the running of BifroMQ. The interface for this plugin is defined in the following Maven module:

```xml
<dependency>
  <groupId>org.apache.bifromq</groupId>
  <artifactId>bifromq-plugin-event-collector</artifactId>
  <version>4.0.0-incubating</version>
</dependency>
```

Upon startup, BifroMQ scans the plugins directory and loads all available EventCollector implementations. It is recommended that each EventCollector focuses only on a simple specific task by utilizing the EventType feature to filter out
events that are not relevant to their intended purpose.

<a id="plugin-event_collector--event-types"></a>

## Event Types

The types of event objects generated during BifroMQ's runtime all inherit from
the [Event](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-event-collector/src/main/java/org/apache/bifromq/plugin/eventcollector/Event.java) class. Each specific event class corresponds to
an [EventType](https://github.com/apache/bifromq/blob/main/bifromq-plugin/bifromq-plugin-event-collector/src/main/java/org/apache/bifromq/plugin/eventcollector/EventType.java) enumeration, which can be accessed through the type() method
on the object. This facilitates the implementation of event filtering logic. The hlc() method allows for retrieving an event object's timestamp. BifroMQ's timestamps are partially ordered, reflecting the sequence in which related events
occur. This feature is particularly useful for handling events in BifroMQ's distributed deployments.

<a id="plugin-event_collector--interface-method"></a>

## Interface Method

When an event is generated, BifroMQ invokes the `report()` method on all loaded EventCollectors. The method signature is as follows:

```java
public void report(Event<?> event);
```

This method is called on BifroMQ's worker thread. As the load increases, a large number of events will be generated. To avoid the creation of a multitude of event objects and excessive memory overhead, the event object passed into this
method will be reused after the method returns. Therefore, when implementing the Event Collector plugin, it's important to consider the following:

- Avoid including complex business logic within the report method to ensure it returns quickly; otherwise, it may negatively impact BifroMQ's performance.
- The ownership of the passed-in event object does not transfer. If the business logic is asynchronous and there's a need to access the content of the event after the report method returns, you should create a shallow copy of the object
  using the `clone()` method before returning.

<a id="plugin-event_collector--metrics"></a>

## Metrics

Because the `report` method is frequently called, BifroMQ records and outputs the following metrics to help
plugin implementers observe the performance indicators of the plugin interface methods:

<table><thead><tr><th>Metric Name</th><th>Meter Type</th><th>Tag(<code>method</code>)</th><th>Description</th></tr></thead><tbody><tr><td><code>call.exec.timer</code></td><td>TIMER</td><td>EventCollector/report</td><td>Latency for <code>report</code> call</td></tr></tbody></table>

- [Event Types](#plugin-event_collector--event-types)
- [Interface Method](#plugin-event_collector--interface-method)
- [Metrics](#plugin-event_collector--metrics)

---

<a id="plugin-resource_throttler"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/resource_throttler/ -->

<!-- page_index: 35 -->

# Resource Throttler

Version: 4.0.0-incubating

# Resource Throttler

In BifroMQ's multi-tenant architecture, tenants share resources provided by a single cluster instance. To prevent any single tenant from overusing resources and impacting others, it is crucial to control each tenant's resource usage
globally at runtime. It is important to note that the ability to achieve load isolation among tenants through resource limitations presupposes the availability of surplus resources in the cluster during peak business periods.

Tenant-level global resource limitations require real-time monitoring of each tenant's cluster resource usage. BifroMQ provides [Tenant-level Metrics](#admin_guide-observability-metrics-tenantmetrics) for measuring resources in
terms of quantity and rate, including Gauge, Counter, and Summary metrics.

The interface for the plugin is defined in the following Maven module:

```xml
<dependency>
  <groupId>org.apache.bifromq</groupId>
  <artifactId>bifromq-plugin-resource-throttler</artifactId>
  <version>4.0.0-incubating</version>
</dependency>
```

BifroMQ allows only one instance of the Resource Throttler to run at a time. The specific implementation class to be loaded must be specified in the [configuration file](#admin_guide-configuration-config_file_manual) by its
Fully Qualified Name (FQN):

```yaml
resourceThrottlerFQN: "YOUR_SETTING_PROVIDER_CLASS"
```

<a id="plugin-resource_throttler--interface-method"></a>

## Interface Method

```java
public boolean hasResource(String tenantId, TenantResourceType type);
```

This method is called synchronously on BifroMQ's worker thread and must be implemented efficiently to avoid impacting BifroMQ performance. A return value of false triggers a limiting action, and a ResourceThrottling event is generated and
reported to the [Event Collector](#plugin-event_collector).

Here are the resource types defined in `TenantResourceType`:

<table><thead><tr><th>Enum Value</th><th>Description</th><th>Action on Limiting(MQTT3)</th><th>Action on Limiting(MQTT5)</th></tr></thead><tbody><tr><td><code>TotalConnections</code></td><td>Total number of connections</td><td>ConnAck with code(0x03)</td><td>ConnAck with code(0x97)</td></tr><tr><td><code>TotalSessionMemoryBytes</code></td><td>Total session memory usage in bytes</td><td>ConnAck with code(0x03)</td><td>ConnAck with code(0x97)</td></tr><tr><td><code>TotalPersistentSessions</code></td><td>Total number of persistent sessions</td><td>Close connection by server</td><td>Disconnect with code(0x97) and close connection by server</td></tr><tr><td><code>TotalPersistentSessionSpaceBytes</code></td><td>Total persistent session storage space in bytes</td><td>Close connection by server</td><td>Disconnect with code(0x97) and close connection by server</td></tr><tr><td><code>TotalSharedSubscriptions</code></td><td>Total number of shared subscriptions</td><td>SubAck with code(0x80)</td><td>SubAck with code(0x97)</td></tr><tr><td><code>TotalTransientSubscriptions</code></td><td>Total number of transient subscriptions</td><td>SubAck with code(0x80)</td><td>SubAck with code(0x97)</td></tr><tr><td><code>TotalPersistentSubscriptions</code></td><td>Total number of persistent subscriptions</td><td>SubAck with code(0x80)</td><td>SubAck with code(0x97)</td></tr><tr><td><code>TotalRetainMessageSpaceBytes</code></td><td>Total storage space for Retain messages in bytes</td><td>Ignore</td><td>Ignore</td></tr><tr><td><code>TotalRetainTopics</code></td><td>Total number of Retain topics</td><td>Ignore</td><td>Ignore</td></tr><tr><td><code>TotalConnectPerSecond</code></td><td>Total connections per second</td><td>ConnAck with code(0x03)</td><td>ConnAck with code(0x97)</td></tr><tr><td><code>TotalInboundBytesPerSecond</code></td><td>Total inbound bytes per second</td><td>Slowdown throughput</td><td>Slowdown throughput</td></tr><tr><td><code>TotalTransientSubscribePerSecond</code></td><td>Total transient subscribes per second</td><td>SubAck with code(0x80)</td><td>SubAck with code(0x97)</td></tr><tr><td><code>TotalPersistentSubscribePerSecond</code></td><td>Total persistent subscribes per second</td><td>SubAck with code(0x80)</td><td>SubAck with code(0x97)</td></tr><tr><td><code>TotalTransientUnsubscribePerSecond</code></td><td>Total transient unsubscribes per second</td><td>UnsubAck only</td><td>UnsubAck with code(0x80)</td></tr><tr><td><code>TotalPersistentUnsubscribePerSecond</code></td><td>Total persistent unsubscribes per second</td><td>UnsubAck only</td><td>UnsubAck with code(0x80)</td></tr><tr><td><code>TotalTransientFanOutBytesPerSeconds</code></td><td>Total transient fan-out bytes per second</td><td>Throttled to one subscriber</td><td>Throttled</td></tr><tr><td><code>TotalPersistentFanOutBytesPerSeconds</code></td><td>Total persistent fan-out bytes per second</td><td>Throttled to one subscriber</td><td>Throttled</td></tr><tr><td><code>TotalRetainedMessagesPerSeconds</code></td><td>Total Retain messages per second</td><td>Ignore</td><td>Ignore</td></tr><tr><td><code>TotalRetainedBytesPerSecond</code></td><td>Total bytes for Retain messages per second</td><td>Ignore</td><td>Ignore</td></tr><tr><td><code>TotalRetainMatchPerSeconds</code></td><td>Total Retain message match requests per second</td><td>SubAck with code(0x80)</td><td>SubAck with code(0x97)</td></tr><tr><td><code>TotalRetainMatchBytesPerSecond</code></td><td>Total bytes for Retain match requests per second</td><td>SubAck with code(0x80)</td><td>SubAck with code(0x97)</td></tr></tbody></table>

These enum values represent the types of resources that can be throttled in a multi-tenant BifroMQ setup, with different resource types triggering different limiting actions.

<a id="plugin-resource_throttler--metrics"></a>

## Metrics

Because the `hasResource` method is frequently called, BifroMQ records and outputs the following metrics to help
plugin implementers observe the performance indicators of the plugin interface methods:

<table><thead><tr><th>Metric Name</th><th>Meter Type</th><th>Tag(<code>method</code>)</th><th>Description</th></tr></thead><tbody><tr><td><code>call.exec.timer</code></td><td>TIMER</td><td>ResourceThrottler/hasResource</td><td>Latency for <code>hasResource</code> call</td></tr><tr><td><code>call.exec.fail.count</code></td><td>COUNTER</td><td>ResourceThrottler/hasResource</td><td>Fail counter for <code>hasResource</code> call</td></tr></tbody></table>
<a id="plugin-resource_throttler--implementation-considerations"></a>

## Implementation Considerations

Implementing multi-tenant services with BifroMQ involves several key considerations for effectively managing resource usage and ensuring fair access across tenants:

1. **Collection and Aggregation of Tenant Metrics**: Collect resource metrics from BifroMQ for each tenant to build and maintain a real-time view of resource usage. The real-time nature of this view determines the precision of throttling
   strategies.
2. **Resource Limitation Strategy**: Based on the real-time resource view, implement decision-making for tenant resource allocation and translate these into specific resource limitation instructions.
3. **Implementing Resource Limitations**: Resource limitation instructions need to be fed back to BifroMQ through the `hasResource` method in a non-blocking manner.

<a id="plugin-resource_throttler--example-implementation"></a>

## Example Implementation

BifroMQ includes an example implementation of the Resource Throttler, which can be enabled by specifying `resourceThrottlerFQN` as `org.apache.bifromq.demo.plugin.DemoResourceThrottler` in
the [configuration file](#admin_guide-configuration-intro). The example uses a JVM startup argument (`-Dplugin.resourcethrottler.url`) to specify a callback URL for a webhook.

When BifroMQ calls the hasResource method, the plugin initiates a GET request that includes tenant\_id and resource\_type headers, corresponding to the two parameters of the hasResource method call. The request is asynchronous, and
hasResource always returns true before a response is received, ensuring processing is not blocked by the request.

The result of the request is cached for 60 seconds and refreshed every second. The response body's string is parsed into a boolean value, which becomes the return value of the hasResource method.

Below is a demonstration webhook server implementation (based on Node.js) that can be used to test the example plugin. The webhook URL address is `http://<ADDR>:<PORT>/query`. Two additional urls `http://<ADDR>:<PORT>/throttle`, and `http://<ADDR>:<PORT>/release` are for setting and cancelling the throttling state for a given tenant, respectively.

```js
const hasResourceMap = {};

const args = process.argv.slice(2);
const hostname = args[0] || 'localhost';
const port = args[1] || 3000;

const server = http.createServer((req, res) => {

const parsedUrl = url.parse(req.url, true);
const pathname = parsedUrl.pathname;

res.setHeader('Content-Type', 'text/plain');

if (pathname === '/query') {
    const tenantId = req.headers['tenant_id'];
    const resourceType = req.headers['resource_type'];
    const key = `${tenantId}${resourceType}`;

    const exists = key in hasResourceMap ? hasResourceMap[key] : true;
    res.end(`${exists}`);

}
else if (pathname === '/throttle') {
    const tenantId = req.headers['tenant_id'];
    the resourceType = req.headers['resource_type'];
    const key = `${tenantId}${resourceType}`;

    hasResourceMap[key] = false;
    res.end('Throttled');

}
else if (pathname === '/release') {
    the tenantId = req.headers['tenant_id'];
    the resourceType = req.headers['resource_type'];
    const key = `${tenantId}${resourceType}`;

    delete hasResourceMap[key];
    res.end('Released');
}
else {
    res.statusCode = 404;
    res.end('Not Found');
}
});

server.listen(port, hostname, () => {
    console.log(`Server listening on port ${server.address().port} from address ${server.address().address}`);
});
```

- [Interface Method](#plugin-resource_throttler--interface-method)
- [Metrics](#plugin-resource_throttler--metrics)
- [Implementation Considerations](#plugin-resource_throttler--implementation-considerations)
- [Example Implementation](#plugin-resource_throttler--example-implementation)

---

<a id="plugin-setting_provider-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/setting_provider/intro/ -->

<!-- page_index: 36 -->

# Setting Provider

Version: 4.0.0-incubating

# Setting Provider

BifroMQ defines a category of [Tenant-level Settings](#plugin-setting_provider-tenantsetting) that can be modified at runtime, allowing for dynamic adjustment of BifroMQ's service behavior per tenant. The purpose of the Setting Provider Plugin is to supply
custom values for these settings at runtime.

The Plugin's interface is defined in the following Maven module:

```xml
<dependency>
  <groupId>org.apache.bifromq</groupId>
  <artifactId>bifromq-plugin-setting-provider</artifactId>
  <version>4.0.0-incubating</version>
</dependency>
```

BifroMQ allows only a single instance of the Setting Provider to run at a time. You can configure the specific implementation class to be loaded through a configuration file by specifying its fully qualified name (FQN) using the following
key:

```yaml
settingProviderFQN: "YOUR_SETTING_PROVIDER_CLASS"
```

<a id="plugin-setting_provider-intro--initial-values-and-validation-of-settings"></a>

## Initial Values and Validation of Settings

Each Setting has an initial value, for example, MaxTopicLength has an initial value of 255 and is validated to be an integer between 0 and 65535. A Setting’s initial value can be overridden by a System Property of the same name, for
example, adding `-DMaxTopicLength=128` to the JVM launch parameters of BifroMQ. Note that the initial value passed through the System Property must be correctly parsed to the corresponding data type, otherwise, the override will not be
successful.

<a id="plugin-setting_provider-intro--updating-current-value-of-setting"></a>

## Updating Current Value of Setting

BifroMQ updates the current value of a Setting by invoking the SettingProvider Plugin's `provide` method. The signature of the provide method is as follows:

```java
public <R> R provide(Setting setting, String tenantId);
```

This method is called by BifroMQ's thread pool, hence when implementing the Setting Provider Plugin, keep the following in mind:

1. Avoid including heavy business logic within the provide method to ensure it returns quickly, as this can otherwise negatively impact BifroMQ's performance.
2. When it is not possible to quickly determine the value of a Setting, it can return `null`, in which case the Setting will continue to use its current value. This allows for the decision logic for the Setting to be made asynchronous.

<a id="plugin-setting_provider-intro--cache-behavior"></a>

## Cache Behavior

The values of Settings for different tenants are cached to reduce the number of calls to the Setting Provider. The following JVM system properties control the caching behavior to balance the immediacy of runtime settings with the load of
requests:

<table><thead><tr><th>System Property Name</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>setting_provide_init_value</code></td><td>false</td><td>Determines whether to call <code>provide</code> to populate the cache on a cache miss. By default, the initial value is used.</td></tr><tr><td><code>setting_refresh_seconds</code></td><td>5</td><td>The interval, in seconds, between refreshes of a cached setting.</td></tr><tr><td><code>setting_expire_seconds</code></td><td>300</td><td>The expiration time, in seconds, of a setting in the cache.</td></tr><tr><td><code>setting_tenant_cache_limit</code></td><td>100</td><td>The maximum number of tenants' values that can be cached.</td></tr></tbody></table>

**Note:** Enabling `setting_provide_init_value` could potentially block BifroMQ's working threads and cause performance issues if the `provide` method is slow.

<a id="plugin-setting_provider-intro--metrics"></a>

## Metrics

Because the `provide` method is frequently called, BifroMQ records and outputs the following metrics to help
plugin implementers observe the performance indicators of the plugin interface methods:

<table><thead><tr><th>Metric Name</th><th>Meter Type</th><th>Tag(<code>method</code>)</th><th>Description</th></tr></thead><tbody><tr><td><code>call.exec.timer</code></td><td>TIMER</td><td>SettingProvider/provide</td><td>Latency for <code>provide</code> call</td></tr><tr><td><code>call.exec.fail.count</code></td><td>COUNTER</td><td>SettingProvider/provide</td><td>Fail counter for <code>provide</code> call</td></tr></tbody></table>
<a id="plugin-setting_provider-intro--implementation-example"></a>

## Implementation Example

BifroMQ includes a demonstration implementation of a WebHook-based SettingProvider that can be enabled by specifying `settingProviderFQN` as `org.apache.bifromq.demo.plugin.DemoSettingProvider` in
the [configuration file](#admin_guide-configuration-intro). The example implementation uses the JVM startup parameter (`-Dplugin.settingprovider.url`) to specify a webhook callback URL.

When BifroMQ calls the `provide` method, the plugin initiates an HTTP GET request containing the `tenant_id` and `setting_name` headers, corresponding to the two parameters of the `provide` method. The string contained in the response body
is parsed into the corresponding Setting value type as the return value.

Below is a simple Node implementation of a WebhookServer for testing the example plugin, with webhook URLs: `http://<ADDR>:<PORT>/query` and `http://<ADDR>:<PORT>/provide` for querying and setting runtime Settings for a given tenant, respectively.

```js
const http = require('http');
const url = require('url');

const settingMap = {};
const server =

 http.createServer((req, res) => {
  const parsedUrl = url.parse(req.url, true);
  the pathname = parsedUrl.pathname;

  res.setHeader('Content-Type', 'text/plain');

  if (pathname === '/query') {
    const tenantId = req.headers['tenant_id'];
    the settingName = req.headers['setting_name'];
    const key = `${tenantId}${settingName}`;
    if (key in settingMap) {
      res.end(`${settingMap[key]}`);
    } else {
      res.statusCode = 404;
      res.end("");
    }
  }
  else if (pathname === '/provide') {
    const tenantId = req.headers['tenant_id'];
    the settingName = req.headers['setting_name'];
    const key = `${tenantId}${settingName}`;

    let body = [];
    req.on('data', (chunk) => {
      body.push(chunk);
    }).on('end', () => {
      body = Buffer.concat(body).toString();
      settingMap[key] = body;
      res.end('OK');
    });
  }
  else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

const args = process.argv.slice(2);
const hostname = args[0] || 'localhost';
const port = args[1] || 3000;

server.listen(port, hostname, () => {
  console.log(`Server listening on port ${server.address().port} at ${server.address().address}`);
});
```

- [Initial Values and Validation of Settings](#plugin-setting_provider-intro--initial-values-and-validation-of-settings)
- [Updating Current Value of Setting](#plugin-setting_provider-intro--updating-current-value-of-setting)
- [Cache Behavior](#plugin-setting_provider-intro--cache-behavior)
- [Metrics](#plugin-setting_provider-intro--metrics)
- [Implementation Example](#plugin-setting_provider-intro--implementation-example)

---

<a id="plugin-setting_provider-tenantsetting"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/setting_provider/tenantsetting/ -->

<!-- page_index: 37 -->

# Tenant-level Settings

Version: 4.0.0-incubating

# Tenant-level Settings

Tenant-level settings allow for detailed control of BifroMQ's functionality and performance characteristics. Each setting can be adjusted per tenant, enabling customized behavior according to the specific requirements and preferences of
each
tenant. This granularity ensures that BifroMQ can cater to a wide variety of use cases and operational environments.

<a id="plugin-setting_provider-tenantsetting--initial-value-adjustment"></a>

## Initial Value Adjustment

Initial values for these settings can be adjusted through JVM startup parameters. This allows for system-wide default adjustments before runtime customization per tenant. For example, to disable MQTT version 3.1 client connections by
default, you can start the JVM with the parameter `-DMQTT3Enabled=false`. This level of control provides the flexibility to optimize the broker's behavior based on the deployment context and operational requirements.

<a id="plugin-setting_provider-tenantsetting--customization-through-setting-provider-plugins"></a>

## Customization through Setting Provider Plugins

The management responsibility of tenant settings is inverted, meaning it is implemented by the business side. Customization and runtime adjustment of these settings are achieved through the development and integration of custom Setting
Provider plugins. This approach allows businesses to dynamically adjust settings in response to changing operational conditions, regulatory requirements, or specific business logic, enhancing the adaptability and scalability of BifroMQ
deployments.

<a id="plugin-setting_provider-tenantsetting--supported-settings"></a>

## Supported Settings

<table><thead><tr><th>Name</th><th>Type</th><th>Initial Value</th><th>Description</th></tr></thead><tbody><tr><td><code>MQTT3Enabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables MQTT v3.1 support.</td></tr><tr><td><code>MQTT4Enabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables MQTT v3.1.1 support.</td></tr><tr><td><code>MQTT5Enabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables MQTT v5.0 support.</td></tr><tr><td><code>NoLWTWhenServerShuttingDown</code></td><td>Boolean</td><td>true</td><td>Suppresses Last Will delivery when the server is shutting down.</td></tr><tr><td><code>DebugModeEnabled</code></td><td>Boolean</td><td>false</td><td>Enables or disables debug mode.</td></tr><tr><td><code>ForceTransient</code></td><td>Boolean</td><td>false</td><td>Forces transient mode for connections.</td></tr><tr><td><code>ByPassPermCheckError</code></td><td>Boolean</td><td>true</td><td>Bypasses permission check errors.</td></tr><tr><td><code>PayloadFormatValidationEnabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables payload format validation.</td></tr><tr><td><code>RetainEnabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables message retain feature.</td></tr><tr><td><code>WildcardSubscriptionEnabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables wildcard subscriptions.</td></tr><tr><td><code>SubscriptionIdentifierEnabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables subscription identifiers.</td></tr><tr><td><code>SharedSubscriptionEnabled</code></td><td>Boolean</td><td>true</td><td>Enables or disables shared subscriptions.</td></tr><tr><td><code>MaximumQoS</code></td><td>Integer</td><td>2</td><td>Maximum QoS level. Valid values: 0, 1, 2.</td></tr><tr><td><code>MaxTopicLevelLength</code></td><td>Integer</td><td>40</td><td>Maximum length of each topic level (&gt; 0).</td></tr><tr><td><code>MaxTopicLevels</code></td><td>Integer</td><td>16</td><td>Maximum number of topic levels (&gt; 0).</td></tr><tr><td><code>MaxTopicLength</code></td><td>Integer</td><td>255</td><td>Maximum total topic length (&lt; 65536).</td></tr><tr><td><code>MaxTopicAlias</code></td><td>Integer</td><td>10</td><td>Maximum number of topic aliases (&lt; 65536).</td></tr><tr><td><code>MaxSharedGroupMembers</code></td><td>Integer</td><td>200</td><td>Maximum members in a shared subscription group (&gt; 0).</td></tr><tr><td><code>MaxTopicFiltersPerInbox</code></td><td>Integer</td><td>100</td><td>Maximum topic filters per inbox (&gt; 0).</td></tr><tr><td><code>MsgPubPerSec</code></td><td>Integer</td><td>200</td><td>Maximum publishes per second per connection (&gt; 0, ≤ 1000).</td></tr><tr><td><code>ReceivingMaximum</code></td><td>Integer</td><td>200</td><td>Maximum in-flight QoS 1/2 messages per connection (&gt; 0, ≤ 65535).</td></tr><tr><td><code>InBoundBandWidth</code></td><td>Long</td><td>512 * 1024L</td><td>Maximum inbound bandwidth per connection in bytes (≥ 0).</td></tr><tr><td><code>OutBoundBandWidth</code></td><td>Long</td><td>512 * 1024L</td><td>Maximum outbound bandwidth per connection in bytes (≥ 0).</td></tr><tr><td><code>MaxLastWillBytes</code></td><td>Integer</td><td>128</td><td>Maximum Last Will payload size in bytes (&gt; 0, ≤ 250 * 1024 * 1024).</td></tr><tr><td><code>MaxUserPayloadBytes</code></td><td>Integer</td><td>256 * 1024</td><td>Maximum user payload size in bytes (&gt; 0, ≤ 256 * 1024 * 1024).</td></tr><tr><td><code>MinSendPerSec</code></td><td>Integer</td><td>8</td><td>Minimum allowed publishes per second per connection (&gt; 0).</td></tr><tr><td><code>MaxResendTimes</code></td><td>Integer</td><td>3</td><td>Maximum resend attempts for QoS 1/2 messages (≥ 0).</td></tr><tr><td><code>ResendTimeoutSeconds</code></td><td>Integer</td><td>10</td><td>Timeout in seconds before a message is considered for resend (&gt; 0).</td></tr><tr><td><code>MaxTopicFiltersPerSub</code></td><td>Integer</td><td>10</td><td>Maximum topic filters per subscription (&gt; 0, ≤ 100).</td></tr><tr><td><code>MaxGroupFanout</code></td><td>Integer</td><td>100</td><td>Maximum fanout for group deliveries (&gt; 0).</td></tr><tr><td><code>MaxPersistentFanout</code></td><td>Integer</td><td>Integer.MAX_VALUE</td><td>Maximum persistent fanout concurrency (&gt; 0).</td></tr><tr><td><code>MaxPersistentFanoutBytes</code></td><td>Long</td><td>Long.MAX_VALUE</td><td>Maximum bytes allowed for persistent fanout (&gt; 0).</td></tr><tr><td><code>MaxSessionExpirySeconds</code></td><td>Integer</td><td>24 * 60 * 60</td><td>Maximum session expiry time in seconds (&gt; 0, ≤ 0xFFFFFFFF).</td></tr><tr><td><code>MinSessionExpirySeconds</code></td><td>Integer</td><td>60</td><td>Minimum session expiry time in seconds (&gt; 0, ≤ MaxSessionExpirySeconds).</td></tr><tr><td><code>MinKeepAliveSeconds</code></td><td>Integer</td><td>60</td><td>Minimum keep alive in seconds (&gt; 0, &lt; 65535).</td></tr><tr><td><code>SessionInboxSize</code></td><td>Integer</td><td>1000</td><td>Maximum size of session inbox (&gt; 0, ≤ 65535).</td></tr><tr><td><code>QoS0DropOldest</code></td><td>Boolean</td><td>false</td><td>Whether to drop the oldest QoS 0 messages first.</td></tr><tr><td><code>RetainMessageMatchLimit</code></td><td>Integer</td><td>10</td><td>Limit for retained message matches (≥ 0).</td></tr></tbody></table>

- [Initial Value Adjustment](#plugin-setting_provider-tenantsetting--initial-value-adjustment)
- [Customization through Setting Provider Plugins](#plugin-setting_provider-tenantsetting--customization-through-setting-provider-plugins)
- [Supported Settings](#plugin-setting_provider-tenantsetting--supported-settings)

---

<a id="plugin-plugin_practice"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/plugin/plugin_practice/ -->

<!-- page_index: 38 -->

# Plugin Practice and Notice

Version: 4.0.0-incubating

# Plugin Practice and Notice

This article outlines some practices and considerations when developing BifroMQ plugins.

<a id="plugin-plugin_practice--start-a-bifromq-plugin-project-quickly"></a>

## Start a BifroMQ Plugin Project Quickly

To jump start your BifroMQ plugin development, execute the following Maven command (the version placeholders automatically use the current docs version):

```bash
mvn archetype:generate \
  -DarchetypeGroupId=org.apache.bifromq \
  -DarchetypeArtifactId=bifromq-plugin-archetype \
  -DarchetypeVersion=4.0.0-incubating \
  -DgroupId=<YOUR_GROUP_ID> \
  -DartifactId=<YOUR_ARTIFACT_ID> \
  -Dversion=<YOUR_PROJECT_VERSION> \
  -DpluginName=<YOUR_PLUGIN_CLASS_NAME> \
  -DpluginContextName=<YOUR_PLUGIN_CONTEXT_CLASS_NAME> \
  -DbifromqVersion=4.0.0-incubating \
  -DinteractiveMode=false
```

Replace `<YOUR_GROUP_ID>`, `<YOUR_ARTIFACT_ID>`, `<YOUR_PROJECT_VERSION>`, `<YOUR_PLUGIN_CLASS_NAME>`, and `< YOUR_PLUGIN_CONTEXT_CLASS_NAME>` with your specific details. This command generates a ready-to-build multi-module
project structured for BifroMQ plugin development.

In addition to the foundational code framework for plugin development, the generated BifroMQ plugin project also includes the following features:

- PluginContext: Defines the plugin context to facilitate the transfer of necessary runtime information.
- Configuration File: Uses a standalone config.yaml file for plugin configuration.
- Logging Configuration: Uses a standalone logback.xml file for plugin logging configuration.

<a id="plugin-plugin_practice--remote-debugging-with-bifromq"></a>

## Remote Debugging with BifroMQ

BifroMQ supports remote debugging, which can be activated through the `JVM_DEBUG` environment variable. Additionally, the remote debugging port can be specified through the `JAVA_DEBUG_PORT` environment variable. If not specified, the
default port is 8008. Before starting the BifroMQ process, specify these environment variables using shell:

```shell
export JVM_DEBUG=true
export JAVA_DEBUG_PORT=8008
export DEBUG_SUSPEND_FLAG=n
```

Ensure the debugging port is correctly configured to avoid port conflicts. Remote debugging can be performed using an IDE (for example, IntelliJ or Eclipse). Setting DEBUG\_SUSPEND\_FLAG=y can assist in debugging the plugin's initialization
process.

<a id="plugin-plugin_practice--pay-attention-to-java-classloading"></a>

## Pay Attention to Java ClassLoading

BifroMQ uses separate ClassLoaders for each plugin to load classes from the plugin's classpath. Therefore, ensure your plugin's packaging includes all dependencies used (except those [provided](#plugin-intro--plugin-deployment) by BifroMQ). Some
third-party libraries might load classes in other ways, leading to class loading failures. Most situations can be resolved by swapping the Thread ContextLoader:

```java
class MyPlugin {
    public void pluginMethod() {
        ClassLoader originalLoader = Thread.currentThread().getContextClassLoader();
        try {
            Thread.currentThread().setContextClassLoader(this.getClass().getClassLoader());
            // Initialize dependencies here
            dependenciesInit();
        } finally {
            Thread.currentThread().setContextClassLoader(originalLoader);
        }
    }
}
```

<a id="plugin-plugin_practice--properly-organize-the-plugin-directory"></a>

## Properly Organize the Plugin Directory

When developing plugins, ensure there are no unrelated jar files in the plugin directory. [pf4j](https://pf4j.org) recursively checks jar files in the plugin directory, and unrelated jars may lead to PF4J validation errors. Keeping the
plugin directory clean and containing only necessary jar files ensures smooth plugin loading and prevents conflicts or validation issues.

<a id="plugin-plugin_practice--metrics-and-logging"></a>

## Metrics and Logging

- For the Plugin project generated from BifroMQ Plugin Archetype. The plubin log output can be controlled using dedicated `log4j2.xml` file under plugin's own `conf` folder.
- BifroMQ captures and records metrics during invocations of plugin methods, offering useful insights for debugging and performance optimization.

- [Start a BifroMQ Plugin Project Quickly](#plugin-plugin_practice--start-a-bifromq-plugin-project-quickly)
- [Remote Debugging with BifroMQ](#plugin-plugin_practice--remote-debugging-with-bifromq)
- [Pay Attention to Java ClassLoading](#plugin-plugin_practice--pay-attention-to-java-classloading)
- [Properly Organize the Plugin Directory](#plugin-plugin_practice--properly-organize-the-plugin-directory)
- [Metrics and Logging](#plugin-plugin_practice--metrics-and-logging)

---

<a id="spi-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/spi/intro/ -->

<!-- page_index: 39 -->

# SPI Overview

Version: 4.0.0-incubating

# SPI Overview

Service Provider Interfaces (SPIs) are extension points that let you customize BifroMQ’s own runtime behavior. They share the same process and execution context as BifroMQ, and are intended for shaping core behaviors rather than integrating external systems.

> [!NOTE]
> **Important**
> - SPIs run inside BifroMQ’s process and share its execution context; a deep understanding of internal workflows is required to avoid stability and performance regressions.
> - ABI compatibility is **not guaranteed across releases**, and these interfaces are **not published to Maven**. Keep your SPI implementation version-aligned with the BifroMQ runtime you deploy.
> - SPIs may change or new ones may appear as the project evolves; verify compatibility before upgrading.

<a id="spi-intro--when-to-use-spi-vs-plugin"></a>

## When to use SPI vs. Plugin

- **SPI**: Extend/Customize BifroMQ itself (e.g., define custom MQTT message UserProperties or add workload-specific balancing strategies) via Java’s SPI mechanism. Runs in-process and shares BifroMQ’s context.
- **Plugin**: Integrate BifroMQ with external systems (e.g., call an external authentication/authorization service). Plugins run in their own ClassLoader context and are relatively isolated.

<a id="spi-intro--spi-development-tips"></a>

## SPI Development Tips

Consult the official Java SPI documentation to understand how discovery and registration work; the following tips highlight BifroMQ-specific considerations:

- Fetch the BifroMQ source for the exact runtime version you will deploy; SPI interfaces are not published to Maven Central.
- Keep your SPI project and the BifroMQ source in a single IDE workspace so you can reference the SPI modules directly without relying on published artifacts.
- Some SPIs only use the first discovered implementation—deploy a single implementation for those to avoid unexpected behavior. Others can be selected explicitly via configuration, which avoids conflicts.
- Run and debug with the broker in that workspace (same version), adding logs/metrics to validate behavior.
- Rebuild and retest whenever you upgrade BifroMQ, since interfaces may change across releases.

<a id="spi-intro--available-spis"></a>

## Available SPIs

- `base-env-provider-spi`: Provide customized thread environment/context.
- `base-kv-local-engine-spi`: Customize the local KV engine used by base-kv.
- `base-kv-split-hinter-spi`: Influence KV partitioning/splitting strategies.
- `base-kv-store-balancer-spi`: Introduce custom balancing strategies.
- `bifromq-dist-worker-spi`: Introduce custom balancers to dist worker cluster.
- `bifromq-inbox-store-spi`: Introduce custom balancers to inbox store cluster.
- `bifromq-retain-store-spi`: Introduce custom balancers to retain store cluster.
- `bifromq-mqtt-server-spi`: Extend MQTT server behaviors (e.g., customized user properties hooks).

- [When to use SPI vs. Plugin](#spi-intro--when-to-use-spi-vs-plugin)
- [SPI Development Tips](#spi-intro--spi-development-tips)
- [Available SPIs](#spi-intro--available-spis)

---

<a id="admin_guide-overview"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/overview/ -->

<!-- page_index: 40 -->

# Admin Guide Overview

Version: 4.0.0-incubating

# Admin Guide Overview

The administration of BifroMQ encompasses two levels: system-level management and tenant-level management. The former is mainly targeted at system administrators and operations personnel, while the requirements for tenant-level management
are often intertwined with specific business needs, thereby manifesting more prominently in integrated capabilities.

---

<a id="admin_guide-configuration-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/configuration/intro/ -->

<!-- page_index: 41 -->

# Configuration Overview

Version: 4.0.0-incubating

# Configuration Overview

Based on different usage scenarios, BifroMQ divides configurations into system-level and tenant-level. System-level configurations are set at the system's startup and cannot be changed afterward. In contrast, tenant-level configurations can be dynamically adjusted during runtime as needed, and their initial values can also be customized at the system's startup. The capability for tenant-level settings requires the implementation of a custom [setting provider](#plugin-setting_provider-intro) plugin, which is not covered in this chapter.

System-level configurations are categorized based on criteria such as their common use, whether they are in an experimental phase, or whether they have not been finalized. They can be provided either through a [configuration file](#admin_guide-configuration-config_file_manual) (located in the conf directory's standalone.yml) or via JVM system [properties](#admin_guide-configuration-bifromq_sys_props) (in the format of -D`conf`=`value`).

The configuration file usually includes common and relatively stable configuration items, while other settings are provided through JVM system properties. Therefore, as versions are updated, the content and method of system-level configurations may change. To simplify the migration process of system-level configurations, BifroMQ provides auxiliary means, with detailed information available in [Configuration Convention & Migration](#installation-config_migration_between_versions).

---

<a id="admin_guide-configuration-config_file_manual"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/configuration/config_file_manual/ -->

<!-- page_index: 42 -->

# Config File Manual

Version: 4.0.0-incubating

# Config File Manual

The configuration file for BifroMQ is a YAML file located in the `conf` directory under `standalone.yml`. This file contains all the configuration parameters for BifroMQ. When starting BifroMQ, you can specify the path to the configuration
file with the command-line parameter `-c` or `--config`. If the configuration file path is not specified, BifroMQ will attempt to load the `standalone.yml` file from the `conf` directory.

The complete configuration file is defined by a set of configuration objects, with the top-level object being `StandaloneConfig`.

<a id="admin_guide-configuration-config_file_manual--standaloneconfig"></a>

## StandaloneConfig

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>authProviderFQN</code></td><td>String</td><td>null</td><td>Fully qualified class name of the custom Auth Provider implementation. If not configured, authentication and authorization will not be performed.</td></tr><tr><td><code>clientBalancerFQN</code></td><td>String</td><td>null</td><td>Fully qualified class name of the custom Client Balancer implementation. If not configured, no active redirection happens.</td></tr><tr><td><code>resourceThrottlerFQN</code></td><td>String</td><td>null</td><td>Fully qualified class name of the custom Resource Throttler implementation. If not configured, resource limiting will not be performed.</td></tr><tr><td><code>settingProviderFQN</code></td><td>String</td><td>null</td><td>Fully qualified class name of the custom Setting Provider implementation. If not configured, default initial values defined in Settings will be used.</td></tr><tr><td><code>bgTaskThreads</code></td><td>Integer</td><td>max(available processor cores/4, 1)</td><td>Threads reserved for the starter's background task executor.</td></tr><tr><td><code>clusterConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--clusterconfig-clusterconfig">ClusterConfig</a></td><td>Cluster join and addressing options.</td></tr><tr><td><code>rpcConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--rpcconfig-rpcconfig">RPCConfig</a></td><td>RPC client/server options.</td></tr><tr><td><code>mqttServiceConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--mqttserviceconfig-mqttserviceconfig">MQTTServiceConfig</a></td><td>MQTT service settings.</td></tr><tr><td><code>distServiceConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--distserviceconfig-distserviceconfig">DistServiceConfig</a></td><td>Dist service settings.</td></tr><tr><td><code>inboxServiceConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--inboxserviceconfig-inboxserviceconfig">InboxServiceConfig</a></td><td>Inbox service settings.</td></tr><tr><td><code>retainServiceConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--retainserviceconfig-retainserviceconfig">RetainServiceConfig</a></td><td>Retain service settings.</td></tr><tr><td><code>sessionDictServiceConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--sessiondictserviceconfig-sessiondictserviceconfig">SessionDictServiceConfig</a></td><td>Session dictionary service settings.</td></tr><tr><td><code>apiServerConfig.*</code></td><td>Object</td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--apiserverconfig-apiserverconfig">APIServerConfig</a></td><td>API server settings.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--clusterconfig-clusterconfig"></a>

### ClusterConfig (`clusterConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>clusterConfig.env</code></td><td>String</td><td>""</td><td>Cluster environment name. Cluster nodes with different environment names are isolated from each other. Cannot be null or empty.</td></tr><tr><td><code>clusterConfig.host</code></td><td>String</td><td>null</td><td>Communication address of the node as a cluster node. Resolution order: if <code>mqttServiceConfig.server.tcpListener.host</code> is not "0.0.0.0", use it; else if <code>rpcConfig.host</code> is set, use it; else use the SiteLocal address of the host.</td></tr><tr><td><code>clusterConfig.port</code></td><td>Integer</td><td>0</td><td>Communication port number of the node as a cluster node. <code>0</code> selects a free port. For bootstrap nodes, configure a fixed port.</td></tr><tr><td><code>clusterConfig.seedEndpoints</code></td><td>String</td><td>null</td><td>Seed node addresses to join the cluster, formatted as <code>ip:port</code> and separated by commas. Non-bootstrap nodes should point to a bootstrap node.</td></tr><tr><td><code>clusterConfig.clusterDomainName</code></td><td>String</td><td>null</td><td>Cluster domain name. If set, BifroMQ resolves the domain to find cluster contact nodes, simplifying fixed-domain deployments.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--rpcconfig-rpcconfig"></a>

### RPCConfig (`rpcConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>rpcConfig.host</code></td><td>String</td><td>null</td><td>Host used for intra-cluster RPC. If null, follows the same host resolution rule as <code>clusterConfig</code>.</td></tr><tr><td><code>rpcConfig.port</code></td><td>Integer</td><td>0</td><td>RPC server port. <code>0</code> lets the system pick a free port.</td></tr><tr><td><code>rpcConfig.enableSSL</code></td><td>Boolean</td><td>false</td><td>Whether to enable TLS for RPC.</td></tr><tr><td><code>rpcConfig.clientEventLoopThreads</code></td><td>Integer</td><td>max(4, available processor cores/8)</td><td>Netty client event-loop threads for RPC clients.</td></tr><tr><td><code>rpcConfig.serverEventLoopThreads</code></td><td>Integer</td><td>max(4, available processor cores/8)</td><td>Netty server event-loop threads for RPC servers.</td></tr><tr><td><code>rpcConfig.clientSSLConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--sslcontextconfig-serversslcontextconfig">SSLContextConfig</a></td><td>null</td><td>TLS settings for RPC clients (used when <code>enableSSL</code> is true).</td></tr><tr><td><code>rpcConfig.serverSSLConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--sslcontextconfig-serversslcontextconfig">ServerSSLContextConfig</a></td><td>null</td><td>TLS settings for RPC servers (used when <code>enableSSL</code> is true).</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--mqttserviceconfig-mqttserviceconfig"></a>

### MQTTServiceConfig (`mqttServiceConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>mqttServiceConfig.client.workerThreads</code></td><td>Integer</td><td>0</td><td>Worker threads for MQTT internal clients (0 = use caller thread).</td></tr><tr><td><code>mqttServiceConfig.server.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable the MQTT server.</td></tr><tr><td><code>mqttServiceConfig.server.connTimeoutSec</code></td><td>Integer</td><td>20</td><td>Timeout from TCP connect to MQTT CONNECT completion; exceeded connections are closed.</td></tr><tr><td><code>mqttServiceConfig.server.maxConnPerSec</code></td><td>Integer</td><td>2000</td><td>Max MQTT connect operations per second; excess connections are throttled/disconnected.</td></tr><tr><td><code>mqttServiceConfig.server.maxDisconnPerSec</code></td><td>Integer</td><td>1000</td><td>Max disconnect operations per second during graceful shutdown.</td></tr><tr><td><code>mqttServiceConfig.server.maxMsgByteSize</code></td><td>Integer</td><td>262144</td><td>Max MQTT CONNECT packet size (including Will); larger packets are rejected.</td></tr><tr><td><code>mqttServiceConfig.server.maxConnBandwidth</code></td><td>Integer</td><td>524288</td><td>Max per-connection bandwidth (inbound/outbound), in bytes per second.</td></tr><tr><td><code>mqttServiceConfig.server.bossELGThreads</code></td><td>Integer</td><td>1</td><td>Netty boss threads for accepting MQTT TCP connections.</td></tr><tr><td><code>mqttServiceConfig.server.workerELGThreads</code></td><td>Integer</td><td>max(available processor cores/2, 2)</td><td>Netty worker threads for MQTT protocol processing.</td></tr><tr><td><code>mqttServiceConfig.server.userPropsCustomizerFactoryConfig</code></td><td><code>Map&lt;String, Struct&gt;</code></td><td></td><td>Customizer factory settings for MQTT 5 user properties.</td></tr><tr><td><code>mqttServiceConfig.server.tcpListener.enable</code></td><td>Boolean</td><td>true</td><td>Enable MQTT over TCP.</td></tr><tr><td><code>mqttServiceConfig.server.tcpListener.host</code></td><td>String</td><td>"0.0.0.0"</td><td>Listen address for MQTT over TCP.</td></tr><tr><td><code>mqttServiceConfig.server.tcpListener.port</code></td><td>Integer</td><td>1883</td><td>Listen port for MQTT over TCP.</td></tr><tr><td><code>mqttServiceConfig.server.tlsListener.enable</code></td><td>Boolean</td><td>false</td><td>Enable MQTT over TLS.</td></tr><tr><td><code>mqttServiceConfig.server.tlsListener.host</code></td><td>String</td><td>null</td><td>Listen address for MQTT over TLS (defaults to resolved host when null).</td></tr><tr><td><code>mqttServiceConfig.server.tlsListener.port</code></td><td>Integer</td><td>1884</td><td>Listen port for MQTT over TLS.</td></tr><tr><td><code>mqttServiceConfig.server.tlsListener.sslConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--sslcontextconfig-serversslcontextconfig">ServerSSLContextConfig</a></td><td>null</td><td>TLS settings for MQTT over TLS.</td></tr><tr><td><code>mqttServiceConfig.server.wsListener.enable</code></td><td>Boolean</td><td>true</td><td>Enable MQTT over WebSocket.</td></tr><tr><td><code>mqttServiceConfig.server.wsListener.host</code></td><td>String</td><td>null</td><td>Listen address for MQTT over WebSocket (defaults to resolved host when null).</td></tr><tr><td><code>mqttServiceConfig.server.wsListener.port</code></td><td>Integer</td><td>8080</td><td>Listen port for MQTT over WebSocket.</td></tr><tr><td><code>mqttServiceConfig.server.wsListener.wsPath</code></td><td>String</td><td>"/mqtt"</td><td>WebSocket path for MQTT over WebSocket.</td></tr><tr><td><code>mqttServiceConfig.server.wssListener.enable</code></td><td>Boolean</td><td>false</td><td>Enable MQTT over WebSocket Secure.</td></tr><tr><td><code>mqttServiceConfig.server.wssListener.host</code></td><td>String</td><td>null</td><td>Listen address for MQTT over WebSocket Secure (defaults to resolved host when null).</td></tr><tr><td><code>mqttServiceConfig.server.wssListener.port</code></td><td>Integer</td><td>8443</td><td>Listen port for MQTT over WebSocket Secure.</td></tr><tr><td><code>mqttServiceConfig.server.wssListener.wsPath</code></td><td>String</td><td>"/mqtt"</td><td>WebSocket path for MQTT over WebSocket Secure.</td></tr><tr><td><code>mqttServiceConfig.server.wssListener.sslConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--sslcontextconfig-serversslcontextconfig">ServerSSLContextConfig</a></td><td>null</td><td>TLS settings for MQTT over WebSocket Secure.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--distserviceconfig-distserviceconfig"></a>

### DistServiceConfig (`distServiceConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>distServiceConfig.client.workerThreads</code></td><td>Integer</td><td>0</td><td>Worker threads for Dist client.</td></tr><tr><td><code>distServiceConfig.server.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable Dist server.</td></tr><tr><td><code>distServiceConfig.server.workerThreads</code></td><td>Integer</td><td>max(2, available processor cores/4)</td><td>Dist server worker threads (0 = run on caller thread).</td></tr><tr><td><code>distServiceConfig.server.attributes</code></td><td><code>Map&lt;String,String&gt;</code></td><td></td><td>Custom attributes attached to Dist server nodes.</td></tr><tr><td><code>distServiceConfig.server.defaultGroups</code></td><td><code>Set&lt;String&gt;</code></td><td>[]</td><td>Default groups served by this Dist server.</td></tr><tr><td><code>distServiceConfig.workerClient.workerThreads</code></td><td>Integer</td><td>max(2, available processor cores/4)</td><td>Worker client threads for Dist worker communication.</td></tr><tr><td><code>distServiceConfig.workerClient.queryPipelinePerStore</code></td><td>Integer</td><td>1000</td><td>Query pipelines per Dist store.</td></tr><tr><td><code>distServiceConfig.worker.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable Dist worker.</td></tr><tr><td><code>distServiceConfig.worker.workerThreads</code></td><td>Integer</td><td>0</td><td>Dist worker threads (0 = use caller thread).</td></tr><tr><td><code>distServiceConfig.worker.tickerThreads</code></td><td>Integer</td><td>max(1, available processor cores/20)</td><td>Background ticker threads.</td></tr><tr><td><code>distServiceConfig.worker.maxWALFetchSize</code></td><td>Integer</td><td>10MB</td><td>Max WAL fetch size in bytes.</td></tr><tr><td><code>distServiceConfig.worker.compactWALThreshold</code></td><td>Integer</td><td>256MB</td><td>WAL compaction threshold in bytes.</td></tr><tr><td><code>distServiceConfig.worker.minGCIntervalSeconds</code></td><td>Integer</td><td>30</td><td>Minimum GC interval in seconds.</td></tr><tr><td><code>distServiceConfig.worker.maxGCIntervalSeconds</code></td><td>Integer</td><td>86400</td><td>Maximum GC interval in seconds.</td></tr><tr><td><code>distServiceConfig.worker.dataEngineConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--storageengineconfig">StorageEngineConfig</a></td><td>rocksdb with default settings for data engine</td><td>Data store engine settings for Dist worker.</td></tr><tr><td><code>distServiceConfig.worker.walEngineConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--storageengineconfig">StorageEngineConfig</a></td><td>rocksdb with default settings for wal engine</td><td>WAL store engine settings for Dist worker.</td></tr><tr><td><code>distServiceConfig.worker.balanceConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--balanceroptions">BalancerOptions</a></td><td>Default balancers for dist worker</td><td>Balancer settings for Dist worker.</td></tr><tr><td><code>distServiceConfig.worker.splitHinterConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--splithinteroptions">SplitHinterOptions</a></td><td>Default split hinters for dist worker</td><td>Split hinter settings for Dist worker. See <a class="" href="#admin_guide-configuration-config_file_manual--splithinteroptions">SplitHinterOptions</a>.</td></tr><tr><td><code>distServiceConfig.worker.attributes</code></td><td><code>Map&lt;String,String&gt;</code></td><td>{}</td><td>Custom attributes attached to Dist worker.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--inboxserviceconfig-inboxserviceconfig"></a>

### InboxServiceConfig (`inboxServiceConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>inboxServiceConfig.client.workerThreads</code></td><td>Integer</td><td>0</td><td>Worker threads for Inbox client.</td></tr><tr><td><code>inboxServiceConfig.server.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable Inbox server.</td></tr><tr><td><code>inboxServiceConfig.server.workerThreads</code></td><td>Integer</td><td>max(2, available processor cores/4)</td><td>Inbox server worker threads.</td></tr><tr><td><code>inboxServiceConfig.server.attributes</code></td><td><code>Map&lt;String,String&gt;</code></td><td></td><td>Custom attributes attached to Inbox server.</td></tr><tr><td><code>inboxServiceConfig.server.defaultGroups</code></td><td><code>Set&lt;String&gt;</code></td><td>[]</td><td>Default groups served by this Inbox server.</td></tr><tr><td><code>inboxServiceConfig.storeClient.workerThreads</code></td><td>Integer</td><td>max(2, available processor cores/4)</td><td>Inbox store client worker threads.</td></tr><tr><td><code>inboxServiceConfig.storeClient.queryPipelinePerStore</code></td><td>Integer</td><td>1000</td><td>Query pipelines per Inbox store.</td></tr><tr><td><code>inboxServiceConfig.store.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable Inbox store.</td></tr><tr><td><code>inboxServiceConfig.store.workerThreads</code></td><td>Integer</td><td>0</td><td>Inbox store worker threads.</td></tr><tr><td><code>inboxServiceConfig.store.tickerThreads</code></td><td>Integer</td><td>max(1, available processor cores/20)</td><td>Inbox store ticker threads.</td></tr><tr><td><code>inboxServiceConfig.store.maxWALFetchSize</code></td><td>Integer</td><td>-1</td><td>Max WAL fetch size in bytes (-1 means no limit).</td></tr><tr><td><code>inboxServiceConfig.store.compactWALThreshold</code></td><td>Integer</td><td>256MB</td><td>WAL compaction threshold in bytes.</td></tr><tr><td><code>inboxServiceConfig.store.expireRateLimit</code></td><td>Integer</td><td>1000</td><td>Max expired Session cleanup rate per second.</td></tr><tr><td><code>inboxServiceConfig.store.minGCIntervalSeconds</code></td><td>Integer</td><td>30</td><td>Minimum GC interval in seconds.</td></tr><tr><td><code>inboxServiceConfig.store.maxGCIntervalSeconds</code></td><td>Integer</td><td>86400</td><td>Maximum GC interval in seconds.</td></tr><tr><td><code>inboxServiceConfig.store.dataEngineConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--storageengineconfig">StorageEngineConfig</a></td><td>rocksdb with default settings for data engine</td><td>Data store engine settings for Inbox store.</td></tr><tr><td><code>inboxServiceConfig.store.walEngineConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--storageengineconfig">StorageEngineConfig</a></td><td>rocksdb with default settings for wal engine</td><td>WAL store engine settings for Inbox store.</td></tr><tr><td><code>inboxServiceConfig.store.balanceConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--balanceroptions">BalancerOptions</a></td><td>Default balancers for inbox store</td><td>Balancer settings for Inbox store.</td></tr><tr><td><code>inboxServiceConfig.store.splitHinterConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--splithinteroptions">SplitHinterOptions</a></td><td>Default split hinter for inbox store</td><td>Split hinter settings for Inbox store. See <a class="" href="#admin_guide-configuration-config_file_manual--splithinteroptions">SplitHinterOptions</a>.</td></tr><tr><td><code>inboxServiceConfig.store.attributes</code></td><td><code>Map&lt;String,String&gt;</code></td><td>{}</td><td>Custom attributes attached to Inbox store.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--retainserviceconfig-retainserviceconfig"></a>

### RetainServiceConfig (`retainServiceConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>retainServiceConfig.client.workerThreads</code></td><td>Integer</td><td>0</td><td>Worker threads for Retain client.</td></tr><tr><td><code>retainServiceConfig.server.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable Retain server.</td></tr><tr><td><code>retainServiceConfig.server.workerThreads</code></td><td>Integer</td><td>max(2, available processor cores/4)</td><td>Retain server worker threads.</td></tr><tr><td><code>retainServiceConfig.server.attributes</code></td><td><code>Map&lt;String,String&gt;</code></td><td></td><td>Custom attributes attached to Retain server.</td></tr><tr><td><code>retainServiceConfig.server.defaultGroups</code></td><td><code>Set&lt;String&gt;</code></td><td>[]</td><td>Default groups served by this Retain server.</td></tr><tr><td><code>retainServiceConfig.storeClient.workerThreads</code></td><td>Integer</td><td>max(2, available processor cores/4)</td><td>Retain store client worker threads.</td></tr><tr><td><code>retainServiceConfig.storeClient.queryPipelinePerStore</code></td><td>Integer</td><td>1000</td><td>Query pipelines per Retain store.</td></tr><tr><td><code>retainServiceConfig.store.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable Retain store.</td></tr><tr><td><code>retainServiceConfig.store.workerThreads</code></td><td>Integer</td><td>0</td><td>Retain store worker threads.</td></tr><tr><td><code>retainServiceConfig.store.tickerThreads</code></td><td>Integer</td><td>max(1, available processor cores/20)</td><td>Retain store ticker threads.</td></tr><tr><td><code>retainServiceConfig.store.maxWALFetchSize</code></td><td>Integer</td><td>50MB</td><td>Max WAL fetch size in bytes.</td></tr><tr><td><code>retainServiceConfig.store.compactWALThreshold</code></td><td>Integer</td><td>256MB</td><td>WAL compaction threshold in bytes.</td></tr><tr><td><code>retainServiceConfig.store.gcIntervalSeconds</code></td><td>Integer</td><td>600</td><td>GC interval in seconds.</td></tr><tr><td><code>retainServiceConfig.store.dataEngineConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--storageengineconfig">StorageEngineConfig</a></td><td>rocksdb with default settings for data engine</td><td>Data store engine settings for Retain store.</td></tr><tr><td><code>retainServiceConfig.store.walEngineConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--storageengineconfig">StorageEngineConfig</a></td><td>rocksdb with default settings for wal engine</td><td>WAL store engine settings for Retain store.</td></tr><tr><td><code>retainServiceConfig.store.balanceConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--balanceroptions">BalancerOptions</a></td><td>Default balancers for retain store</td><td>Balancer settings for Retain store.</td></tr><tr><td><code>retainServiceConfig.store.splitHinterConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--splithinteroptions">SplitHinterOptions</a></td><td>Default split hinter for retain store</td><td>Split hinter settings for Retain store. See <a class="" href="#admin_guide-configuration-config_file_manual--splithinteroptions">SplitHinterOptions</a>.</td></tr><tr><td><code>retainServiceConfig.store.attributes</code></td><td><code>Map&lt;String,String&gt;</code></td><td>{}</td><td>Custom attributes attached to Retain store.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--sessiondictserviceconfig-sessiondictserviceconfig"></a>

### SessionDictServiceConfig (`sessionDictServiceConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>sessionDictServiceConfig.client.workerThreads</code></td><td>Integer</td><td>0</td><td>Worker threads for SessionDict client.</td></tr><tr><td><code>sessionDictServiceConfig.server.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable SessionDict server.</td></tr><tr><td><code>sessionDictServiceConfig.server.workerThreads</code></td><td>Integer</td><td>0</td><td>SessionDict server worker threads (0 = use caller thread).</td></tr><tr><td><code>sessionDictServiceConfig.server.attributes</code></td><td><code>Map&lt;String,String&gt;</code></td><td>{}</td><td>Custom attributes attached to SessionDict server.</td></tr><tr><td><code>sessionDictServiceConfig.server.defaultGroups</code></td><td><code>Set&lt;String&gt;</code></td><td>[]</td><td>Default groups served by this SessionDict server.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--apiserverconfig-apiserverconfig"></a>

### APIServerConfig (`apiServerConfig.*`)

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>apiServerConfig.enable</code></td><td>Boolean</td><td>true</td><td>Whether to enable HTTP API access.</td></tr><tr><td><code>apiServerConfig.host</code></td><td>String</td><td>null</td><td>API listen address; if null, follows the same host resolution rule.</td></tr><tr><td><code>apiServerConfig.httpPort</code></td><td>Integer</td><td>8091</td><td>HTTP API port.</td></tr><tr><td><code>apiServerConfig.maxContentLength</code></td><td>Integer</td><td>262144</td><td>Max request body size in bytes.</td></tr><tr><td><code>apiServerConfig.workerThreads</code></td><td>Integer</td><td>2</td><td>Worker threads handling HTTP API requests.</td></tr><tr><td><code>apiServerConfig.enableSSL</code></td><td>Boolean</td><td>false</td><td>Whether to enable HTTPS for the API.</td></tr><tr><td><code>apiServerConfig.sslConfig</code></td><td>See <a class="" href="#admin_guide-configuration-config_file_manual--sslcontextconfig-serversslcontextconfig">ServerSSLContextConfig</a></td><td>null</td><td>TLS settings for the API server when HTTPS is enabled.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--sslcontextconfig-serversslcontextconfig"></a>

## SSLContextConfig & ServerSSLContextConfig

SSLContextConfig is used to configure the SSL connection parameters for the client, while ServerSSLContextConfig is used to configure the SSL connection parameters for the server.

If you leave SSLContextConfig or ServerSSLContextConfig set to null while the corresponding `enable` flags are set to true, a self-signed certificate will be generated, which is not recommended for production environments.

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>certFile</code></td><td>String</td><td>null</td><td>The filename of the public certificate for the client or server.</td></tr><tr><td><code>keyFile</code></td><td>String</td><td>null</td><td>The filename of the private key for the client or server.</td></tr><tr><td><code>trustCertsFile</code></td><td>String</td><td>null</td><td>The filename of the root certificate for the client or server. If null, peer certification will not be verified, when clientAuth is OPTIONAL or REQUIRE.</td></tr><tr><td><code>clientAuth</code></td><td>String</td><td>"OPTIONAL"</td><td>Only valid for ServerSSLContextConfig. Whether the server requires client verification. Possible values include:  NONE: No verification required;  OPTIONAL: Server requests client verification, but if the client does not provide a certificate, it will not fail;  REQUIRE: Server requires client verification, and if the client does not provide a certificate, it will fail.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--storageengineconfig"></a>

## StorageEngineConfig

StorageEngineConfig is used to set the configuration parameters for the data engine and WAL engine of the built-in stateful service. The shape of `props` depends on the engine type; defaults are applied per service in code.

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>type</code></td><td>String</td><td><code>rocksdb</code></td><td>Storage engine type. <code>rocksdb</code> enables persistence; <code>memory</code> keeps state in memory only (lost on restart).</td></tr><tr><td><code>props</code> (rocksdb)</td><td><code>Map&lt;String, Object&gt;</code></td><td>Service-specific defaults</td><td>Additional selectively exposed RocksDB options. Tune only if you understand RocksDB well.</td></tr><tr><td><code>props</code> (memory)</td><td><code>Map&lt;String, Object&gt;</code></td><td>{}</td><td>No options for <code>memory</code> currently, normally for testing purpose</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--balanceroptions"></a>

## BalancerOptions

BalancerOptions is used to set the configuration parameters for the Balancer of the built-in stateful service.

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>bootstrapDelayInMS</code></td><td>Long</td><td>15000</td><td>Delay before the balancer starts; helps avoid rebalancing during initial bootstrap.</td></tr><tr><td><code>zombieProbeDelayInMS</code></td><td>Long</td><td>15000</td><td>Interval for probing zombie (stale) replicas.</td></tr><tr><td><code>retryDelayInMS</code></td><td>Long</td><td>5000</td><td>Delay between rebalance retries.</td></tr><tr><td><code>balancers</code></td><td><code>Map&lt;String, Struct&gt;</code></td><td>Service-specific defaults (see code)</td><td>Map of balancer implementation FQNs to their config. Multiple balancers can be enabled; defaults are set in each service (Dist/Inbox/Retain) per code.</td></tr></tbody></table>
<a id="admin_guide-configuration-config_file_manual--splithinteroptions"></a>

## SplitHinterOptions

SplitHinterOptions configures how ranges are split for built-in stateful services.

<table><thead><tr><th>Configuration Name</th><th>Value Type</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>hinters</code></td><td><code>Map&lt;String, Struct&gt;</code></td><td>Service-specific defaults (see code)</td><td>A map of split hinter implementation FQNs to their config. Multiple hinters can be enabled.</td></tr></tbody></table>

Note: Adjusting the parameters related to StorageEngineConfig, BalancerOptions, and SplitHinterOptions requires an in-depth understanding of the storage engine implementation of BifroMQ. Improper configuration may lead to abnormal behavior of the state storage
service.

- [StandaloneConfig](#admin_guide-configuration-config_file_manual--standaloneconfig)
  - [ClusterConfig (`clusterConfig.*`)](#admin_guide-configuration-config_file_manual--clusterconfig-clusterconfig)
  - [RPCConfig (`rpcConfig.*`)](#admin_guide-configuration-config_file_manual--rpcconfig-rpcconfig)
  - [MQTTServiceConfig (`mqttServiceConfig.*`)](#admin_guide-configuration-config_file_manual--mqttserviceconfig-mqttserviceconfig)
  - [DistServiceConfig (`distServiceConfig.*`)](#admin_guide-configuration-config_file_manual--distserviceconfig-distserviceconfig)
  - [InboxServiceConfig (`inboxServiceConfig.*`)](#admin_guide-configuration-config_file_manual--inboxserviceconfig-inboxserviceconfig)
  - [RetainServiceConfig (`retainServiceConfig.*`)](#admin_guide-configuration-config_file_manual--retainserviceconfig-retainserviceconfig)
  - [SessionDictServiceConfig (`sessionDictServiceConfig.*`)](#admin_guide-configuration-config_file_manual--sessiondictserviceconfig-sessiondictserviceconfig)
  - [APIServerConfig (`apiServerConfig.*`)](#admin_guide-configuration-config_file_manual--apiserverconfig-apiserverconfig)
- [SSLContextConfig & ServerSSLContextConfig](#admin_guide-configuration-config_file_manual--sslcontextconfig-serversslcontextconfig)
- [StorageEngineConfig](#admin_guide-configuration-config_file_manual--storageengineconfig)
- [BalancerOptions](#admin_guide-configuration-config_file_manual--balanceroptions)
- [SplitHinterOptions](#admin_guide-configuration-config_file_manual--splithinteroptions)

---

<a id="admin_guide-configuration-bifromq_sys_props"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/configuration/bifromq_sys_props/ -->

<!-- page_index: 43 -->

# System Properties

Version: 4.0.0-incubating

# System Properties

Before adjusting system properties in BifroMQ, it's necessary to have a thorough understanding of its internal mechanisms, as inappropriate modifications can lead to unexpected behavior. Additionally, these system properties are closely
linked with BifroMQ's internal implementation and may not be compatible across different versions. System properties can be set via JVM startup parameters, allowing for flexible customization of BifroMQ's behavior.
For example, setting `-Dmqtt_utf8_sanity_check=false` disables the check for MQTT protocol-defined UTF8 string formats.

Below is a table listing the system properties supported by the current version:

<table><thead><tr><th>Property Key</th><th>Default Value</th><th>Description</th></tr></thead><tbody><tr><td><code>client_redirect_check_interval_seconds</code></td><td>600</td><td>The client redirection check interval in seconds.</td></tr><tr><td><code>cluster_domain_resolve_timeout_seconds</code></td><td>120L</td><td>Timeout for resolving the cluster domain to discover seed nodes.</td></tr><tr><td><code>control_plane_burst_latency_ms</code></td><td>5000L</td><td>The max latency in milliseconds tolerated for the control plane burst.</td></tr><tr><td><code>data_plane_burst_latency_ms</code></td><td>5000L</td><td>The max latency in milliseconds tolerated for the data plane burst.</td></tr><tr><td><code>dist_server_dist_worker_call_queues</code></td><td>CPU cores</td><td>Number of dist worker call queues.</td></tr><tr><td><code>dist_worker_inline_fanout_threshold</code></td><td>1000</td><td>The threshold of the fanout to be executed in the calling thread.</td></tr><tr><td><code>dist_worker_fanout_parallelism</code></td><td>Max(2, CPU cores / 8)</td><td>Parallelism level for fanout operations.</td></tr><tr><td><code>dist_worker_cache_fanout_check_seconds</code></td><td>5</td><td>Interval seconds for checking cached routes against fanout related settings.</td></tr><tr><td><code>dist_worker_match_parallelism</code></td><td>Max(2, CPU cores / 2)</td><td>Parallelism level for match operations.</td></tr><tr><td><code>dist_worker_max_cached_subs_per_tenant</code></td><td>200_000L</td><td>Maximum cached subscriptions per tenant.</td></tr><tr><td><code>dist_worker_topic_match_expiry_seconds</code></td><td>60</td><td>Expiry time in seconds for topic matches.</td></tr><tr><td><code>inbox_check_queues_per_range</code></td><td>1</td><td>Number of check queues per range.</td></tr><tr><td><code>inbox_deliverers</code></td><td>100</td><td>Number of inbox deliverers.</td></tr><tr><td><code>inbox_fetch_queues_per_range</code></td><td>Max(1, CPU cores / 4)</td><td>Number of fetch queues per range.</td></tr><tr><td><code>inbox_meta_cache_expiry_second</code></td><td>300</td><td>Timeout in seconds before cached inbox metadata expires.</td></tr><tr><td><code>ingress_slowdown_direct_memory_usage</code></td><td>0.8</td><td>Threshold for slowing down ingress traffic based on direct memory usage.</td></tr><tr><td><code>ingress_slowdown_heap_memory_usage</code></td><td>0.9</td><td>Threshold for slowing down ingress traffic based on heap memory usage.</td></tr><tr><td><code>mqtt_utf8_sanity_check</code></td><td>false</td><td>Enables/disables UTF8 sanity checks according to MQTT-1.5.3.</td></tr><tr><td><code>max_mqtt3_client_id_length</code></td><td>65535</td><td>Maximum client ID length for MQTT 3 clients.</td></tr><tr><td><code>max_mqtt5_client_id_length</code></td><td>65535</td><td>Maximum client ID length for MQTT 5 clients.</td></tr><tr><td><code>max_slowdown_timeout_seconds</code></td><td>5</td><td>Maximum duration (in seconds) that the slowdown mechanism is allowed to operate before further backpressure protection measures are taken.</td></tr><tr><td><code>mqtt_deliverers_per_server</code></td><td>CPU cores</td><td>Number of MQTT deliverers per server.</td></tr><tr><td><code>persistent_session_detach_timeout_second</code></td><td>7200</td><td>The timeout seconds to consider persistent session is probably detached from mqtt client.</td></tr><tr><td><code>session_register_num</code></td><td>10</td><td>Number of concurrent session registers.</td></tr><tr><td><code>maxActiveDedupChannels</code></td><td>1024</td><td>Maximum active deduplication channels per session.</td></tr><tr><td><code>maxActiveDedupTopicsPerChannel</code></td><td>10</td><td>Maximum active deduplication topics per channel.</td></tr></tbody></table>

---

<a id="admin_guide-configuration-configs_print"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/configuration/configs_print/ -->

<!-- page_index: 44 -->

# Configuration Printing

Version: 4.0.0-incubating

# Configuration Printing

When BifroMQ starts, it prints the values of various configurations in the info logs. Printing configuration information helps you understand the specific settings of the BifroMQ service, facilitating troubleshooting. It is also recommended
to include the printed configuration information when seeking help in the community.

For information on how to view logs, refer to: [Logging](#admin_guide-observability-logging)

<a id="admin_guide-configuration-configs_print--printed-content"></a>

## Printed Content

The printed configuration information in the logs consists of four main parts:

<a id="admin_guide-configuration-configs_print--jvm-parameters"></a>

### JVM Parameters

JVM parameters refer to the parameters passed to the JVM when starting BifroMQ using the `-D` parameter. An example of the printed output is as follows:

```text
15:21:46.890 [main] INFO o.a.b.starter.StandaloneStarter - JVM arguments:
-Xms1045m
-Xmx4096m
-Xlog:gc:file=/usr/share/bifromq-standalone/bin/../logs/gc-%t.log:time,tid,tags:filecount=5,filesize=50m
-DLOG_DIR=/usr/share/bifromq-standalone/bin/../logs
-DCONF_DIR=/usr/share/bifromq-standalone/bin/../conf
-DDATA_DIR=/usr/share/bifromq-standalone/bin/../data
-Dpf4j.pluginsDir=/usr/share/bifromq-standalone/bin/../plugins
-Dfile.encoding=UTF-8
```

<a id="admin_guide-configuration-configs_print--setting-initial-values"></a>

### Setting Initial Values

For information about Settings and their initial values, refer to: [Setting Provider Plugin](#plugin-setting_provider-intro).

It is important to note that the printed values here represent the initial values of Setting when BifroMQ starts. These values can be modified at runtime using your custom Setting Provider Plugin, so the values printed here may not
necessarily be the actual runtime values. An example of the printed output is as follows:

```text
15:21:46.890 [main] INFO o.a.b.starter.StandaloneStarter - Settings, which can be modified at runtime, allowing for dynamic adjustment of BifroMQ's service behavior per tenant. See https://bifromq.io/docs/plugin/setting_provider/
15:21:46.890 [main] INFO o.a.b.starter.StandaloneStarter - Following is the initial value of each setting:
15:21:46.913 [main] INFO o.a.b.starter.StandaloneStarter - Setting: DebugModeEnabled=false
15:21:46.913 [main] INFO o.a.b.starter.StandaloneStarter - Setting: MaxTopicLevelLength=40
15:21:46.913 [main] INFO o.a.b.starter.StandaloneStarter - Setting: MaxTopicLevels=16
15:21:46.913 [main] INFO o.a.b.starter.StandaloneStarter - Setting: MaxTopicLength=255
15:21:46.913 [main] INFO o.a.b.starter.StandaloneStarter - Setting: MaxSharedGroupMembers=200
15:21:46.913 [main] INFO o.a.b.starter.StandaloneStarter - Setting: MaxTopicFiltersPerInbox=100
15:21:46.913 [main] INFO o.a.b.starter.StandaloneStarter - Setting: MsgPubPerSec=200
...
```

<a id="admin_guide-configuration-configs_print--bifromqsystem-properties"></a>

### BifroMQ[System Properties](#admin_guide-configuration-bifromq_sys_props)

An example of the printed output is as follows:

```text
17:21:34.067 [main] INFO  o.a.b.starter.StandaloneStarter - BifroMQ system properties:
17:21:34.070 [main] INFO  o.a.b.starter.StandaloneStarter - BifroMQSysProp: mqtt_utf8_sanity_check=false
17:21:34.070 [main] INFO  o.a.b.starter.StandaloneStarter - BifroMQSysProp: max_client_id_length=65535
17:21:34.070 [main] INFO  o.a.b.starter.StandaloneStarter - BifroMQSysProp: session_register_num=1000
17:21:34.070 [main] INFO  o.a.b.starter.StandaloneStarter - BifroMQSysProp: data_plane_burst_latency_ms=1000
17:21:34.070 [main] INFO  o.a.b.starter.StandaloneStarter - BifroMQSysProp: control_plane_burst_latency_ms=5000
...
```

<a id="admin_guide-configuration-configs_print--bifromq-configuration-file"></a>

### BifroMQ Configuration File

The configuration file section will include the consolidated complete content of the configuration file, with an example of the output as follows:

```text
17:21:34.098 [main] INFO  o.a.b.starter.StandaloneStarter - Consolidated Config:
---
clusterConfig:
  env: "Test"
  host: "127.0.0.1"
  port: 0
mqttServerConfig:
  connTimeoutSec: 20
  maxConnPerSec: 2000
  maxDisconnPerSec: 1000
  maxMsgByteSize: 262144
  maxResendTimes: 5
  maxConnBandwidth: 524288
  defaultKeepAliveSec: 300
  qos2ConfirmWindowSec: 5
  bossELGThreads: 1
  workerELGThreads: 4
...
```

- [Printed Content](#admin_guide-configuration-configs_print--printed-content)
  - [JVM Parameters](#admin_guide-configuration-configs_print--jvm-parameters)
  - [Setting Initial Values](#admin_guide-configuration-configs_print--setting-initial-values)
  - [BifroMQSystem Properties](#admin_guide-configuration-configs_print--bifromqsystem-properties)
  - [BifroMQ Configuration File](#admin_guide-configuration-configs_print--bifromq-configuration-file)

---

<a id="admin_guide-tuning-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/tuning/intro/ -->

<!-- page_index: 45 -->

# Tuning Overview

Version: 4.0.0-incubating

# Tuning Overview

Performance tuning in BifroMQ requires starting with adjustments in the running environment and specific optimizations for the workload.

<a id="admin_guide-tuning-intro--running-environment-tuning"></a>

## Running Environment Tuning

The starting point for performance optimization in BifroMQ is the adjustment of its running environment. Adjustments in this area typically depend on the technical capabilities and recommendations of the hosting environment provider. For instance, when BifroMQ is deployed on the Linux operating system, there are several system-level tuning [options](#admin_guide-tuning-os_tuning_linux) that can significantly impact performance:

- **Network Stack Tuning**: Adjusting TCP settings, such as buffer sizes, backlog settings, and enabling TCP Fast Open, can reduce latency and increase throughput.
- **File Descriptor Limits**: Raising the limit on file descriptors can prevent bottlenecks associated with a high number of concurrent connections.
- **Disk I/O Optimization**: For deployments with heavy persistence requirements, optimizing disk I/O settings and choosing the appropriate filesystem can accelerate message storage and retrieval speeds.

A deep understanding and application of these tuning measures can significantly enhance BifroMQ's performance in specific environments. For detailed content, please refer to the optimization guide for the running environment.

<a id="admin_guide-tuning-intro--workload-specific-tuning"></a>

## Workload-Specific Tuning

BifroMQ is designed to handle various workload types inherent to the MQTT protocol, each with unique characteristics and optimization needs. Efficiently tuning these workloads begins with a detailed analysis of the MQTT traffic patterns generated by your applications. This analysis can help identify key areas for optimization, such as message throughput, client connection handling, session persistence, and topic subscription management. BifroMQ was designed with these needs in mind, offering a suite of specialized mechanisms and configuration options to optimize different aspects of MQTT workloads.

Key areas for workload-specific tuning include:

- **Connection and Session Management**: Optimizing parameters related to client connections and session states can enhance the broker's ability to handle a large number of concurrent clients efficiently.
- **Message Throughput and QoS Handling**: Adjusting settings for message queue sizes, delivery retry mechanisms, and QoS level handling can improve overall message throughput and delivery reliability.
- **Subscription and Topic Matching**: Fine-tuning the mechanisms for subscription management and topic matching can lead to faster and more efficient routing of messages to the appropriate clients.

- [Running Environment Tuning](#admin_guide-tuning-intro--running-environment-tuning)
- [Workload-Specific Tuning](#admin_guide-tuning-intro--workload-specific-tuning)

---

<a id="admin_guide-tuning-os_tuning_linux"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/tuning/os_tuning_linux/ -->

<!-- page_index: 46 -->

# Linux Kernel Tuning

Version: 4.0.0-incubating

# Linux Kernel Tuning

The following Kernel parameters can affect the maximum number of connections that the machine hosting BifroMQ can accept.

<a id="admin_guide-tuning-os_tuning_linux--memory"></a>

## Memory

- vm.max\_map\_count: Limits the number of VMAs (Virtual Memory Areas) that a process can have. It can be increased to 221184.

<a id="admin_guide-tuning-os_tuning_linux--maximum-open-files"></a>

## Maximum Open Files

- nofile: Specifies the maximum number of files that a single process can open.
- nr\_open: Specifies the maximum number of files that can be allocated per process, usually defaulting to 1024 \* 1024 = 1048576.
- file-max: Specifies the maximum number of files that the system kernel can open, with a default value of 185745.

<a id="admin_guide-tuning-os_tuning_linux--max-user-processes"></a>

## Max user processes

- nproc: Indicates the maximum number of processes that a single user can launch. For Java processes, each thread will also occupy a Linux proc resource. In certain versions, for non-root users, this parameter defaults to 4096 and may need to be appropriately increased.

<a id="admin_guide-tuning-os_tuning_linux--netfilter-tuning"></a>

## NetFilter Tuning

Use `sysctl -a | grep conntrack` to view the current parameters. The following parameters determine the maximum number of connections:

- net.netfilter.nf\_conntrack\_buckets: The size of the hashtable buckets that record connection entries.
  - Modification command: `echo 262144 > /sys/module/nf_conntrack/parameters/hashsize`
- net.netfilter.nf\_conntrack\_max: The maximum number of entries in the hashtable, generally equal to nf\_conntrack\_buckets \* 4.
- net.nf\_conntrack\_max: Same as net.netfilter.nf\_conntrack\_max.
- net.netfilter.nf\_conntrack\_tcp\_timeout\_fin\_wait: Default 120s -> Recommended 30s.
- net.netfilter.nf\_conntrack\_tcp\_timeout\_time\_wait: Default 120s -> Recommended 30s.
- net.netfilter.nf\_conntrack\_tcp\_timeout\_close\_wait: Default 60s -> Recommended 15s.
- net.netfilter.nf\_conntrack\_tcp\_timeout\_established: Default 432000 seconds (5 days) -> Recommended 300s.

The following sysctl parameters can affect the performance of TCP channels under high load:

<a id="admin_guide-tuning-os_tuning_linux--server-side-and-load-testing-tcp-related-tuning"></a>

## Server-Side and Load Testing TCP-related Tuning

It is recommended to use the CentOS 7 and above environment for deployment and stress testing.

For CentOS 6, system parameter tuning is required:

- net.core.wmem\_max: Maximum TCP data send window size (bytes).
  - Modification command: `echo 'net.core.wmem_max=16777216' >> /etc/sysctl.conf`
- net.core.wmem\_default: Default TCP data send window size (bytes).
  - Modification command: `echo 'net.core.wmem_default=262144' >> /etc/sysctl.conf`
- net.core.rmem\_max: Maximum TCP data receive window size (bytes).
  - Modification command: `echo 'net.core.rmem_max=16777216' >> /etc/sysctl.conf`
- net.core.rmem\_default: Default TCP data receive window size (bytes).
  - Modification command: `echo 'net.core.rmem_default=262144' >> /etc/sysctl.conf`
- net.ipv4.tcp\_rmem: Memory usage of the socket receive buffer - minimum, warning, maximum.
  - Modification command: `echo 'net.ipv4.tcp_rmem= 1024 4096 16777216' >> /etc/sysctl.conf`
- net.ipv4.tcp\_wmem: Memory usage of the socket send buffer - minimum, warning, maximum.
  - Modification command: `echo 'net.ipv4.tcp_wmem= 1024 4096 16777216' >> /etc/sysctl.conf`
- net.core.optmem\_max: The maximum buffer size (in bytes) allowed for each socket.
  - Modification command: `echo 'net.core.optmem_max = 16777216' >> /etc/sysctl.conf`
- net.core.netdev\_max\_backlog: The length of the queue into which network device places requests.
  - Modification command:`echo 'net.core.netdev_max_backlog = 16384' >> /etc/sysctl.conf`

After making the modifications, use `sysctl -p` and restart the server for them to take effect.

- [Memory](#admin_guide-tuning-os_tuning_linux--memory)
- [Maximum Open Files](#admin_guide-tuning-os_tuning_linux--maximum-open-files)
- [Max user processes](#admin_guide-tuning-os_tuning_linux--max-user-processes)
- [NetFilter Tuning](#admin_guide-tuning-os_tuning_linux--netfilter-tuning)
- [Server-Side and Load Testing TCP-related Tuning](#admin_guide-tuning-os_tuning_linux--server-side-and-load-testing-tcp-related-tuning)

---

<a id="admin_guide-observability-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/observability/intro/ -->

<!-- page_index: 47 -->

# Observability Overview

Version: 4.0.0-incubating

# Observability Overview

In the administration of BifroMQ, ensuring comprehensive system observability stands as a foundational element for conducting effective system operations and maintenance activities. Given BifroMQ's unique positioning as a multi-tenant capable MQTT broker, its observability features not only facilitate general operational excellence but are also crucial for the efficient management of multi-tenant business scenarios. This section explores the key components of BifroMQ's observability capabilities: logging, metrics, and events, with a particular focus on features designed to support multi-tenant environments.

---

<a id="admin_guide-observability-logging"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/observability/logging/ -->

<!-- page_index: 48 -->

# Logging

Version: 4.0.0-incubating

# Logging

BifroMQ utilizes the standard SLF4J interface for logging purposes and selects Apache Log4j as its logging backend. The logs are organized into five distinct levels: TRACE, DEBUG, INFO, WARN, and ERROR, with INFO set as the default log level.

<a id="admin_guide-observability-logging--log4j-configuration-file"></a>

### Log4j Configuration File

The log4j configuration file, named `log4j2.xml`, is located in the `conf` directory within the BifroMQ installation folder. This file allows for detailed customization of logging behavior, including log level settings, output formats, and file rotation policies.

<a id="admin_guide-observability-logging--log-directories"></a>

### Log Directories

By default, BifroMQ stores log files in the `log` directory found in the installation folder. If necessary, an alternative logging directory can be designated by setting the `LOG_DIR` environment variable.

<a id="admin_guide-observability-logging--plugin-logging"></a>

### Plugin Logging

Plugin implementors can also leverage the standard SLF4J interface for logging.

- [Log4j Configuration File](#admin_guide-observability-logging--log4j-configuration-file)
- [Log Directories](#admin_guide-observability-logging--log-directories)
- [Plugin Logging](#admin_guide-observability-logging--plugin-logging)

---

<a id="admin_guide-observability-metrics-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/observability/metrics/intro/ -->

<!-- page_index: 49 -->

# Metrics

Version: 4.0.0-incubating

# Metrics

BifroMQ adopts [Micrometer](https://micrometer.io/) as its framework for metrics collection, analogous to its use of SLF4J and Logback for logging purposes. Micrometer acts as the "SLF4J for metrics" within BifroMQ, providing an easy way to collect metrics without binding users to a specific metrics backend. Instead, users are free to choose their preferred monitoring system and can direct metrics to it using BifroMQ's plugin mechanism.

<a id="admin_guide-observability-metrics-intro--prometheus-integration-via-demoplugin"></a>

## Prometheus Integration via DemoPlugin

BifroMQ offers out-of-the-box support for Prometheus through its bundled [DemoPlugin](https://github.com/apache/bifromq/blob/main/build/build-plugin-demo/src/main/java/org/apache/bifromq/demo/plugin/DemoPlugin.java) for **Demo and Testing Purpose Only**. By default the plubin exposes a Prometheus scraping endpoint (`http://<BIFROMQ_NODE_HOST>:9090/metrics`), enabling direct metrics collection by Prometheus.

<a id="admin_guide-observability-metrics-intro--tenant-level-metrics-for-multi-tenancy"></a>

## Tenant-Level Metrics for Multi-Tenancy

BifroMQ introduces a set of tenant-level [metrics](#admin_guide-observability-metrics-tenantmetrics). These metrics enable the real-time collection and aggregation of data reflecting the resource usage and activity of individual tenants. When used in combination with the [Resource Throttler](#plugin-resource_throttler) plugin, tenant-level metrics facilitate effective load isolation strategies.

<a id="admin_guide-observability-metrics-intro--advanced-diagnostics-and-tuning"></a>

## Advanced Diagnostics and Tuning

Beyond tenant-level insights, BifroMQ collects a broad array of internal metrics from its various functional modules. These metrics are indispensable for deep system tuning and runtime diagnostics. However, due to their close ties to BifroMQ's internal mechanisms and architecture, these deep metrics may vary between BifroMQ versions and are not guaranteed to remain consistent across updates. To avoid compatibility issues, these metrics have not been documented for general use.

- [Prometheus Integration via DemoPlugin](#admin_guide-observability-metrics-intro--prometheus-integration-via-demoplugin)
- [Tenant-Level Metrics for Multi-Tenancy](#admin_guide-observability-metrics-intro--tenant-level-metrics-for-multi-tenancy)
- [Advanced Diagnostics and Tuning](#admin_guide-observability-metrics-intro--advanced-diagnostics-and-tuning)

---

<a id="admin_guide-observability-metrics-tenantmetrics"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/observability/metrics/tenantmetrics/ -->

<!-- page_index: 50 -->

# Tenant-level Metrics

Version: 4.0.0-incubating

# Tenant-level Metrics

Below is a comprehensive table of BifroMQ's tenant metrics, including their MetricName (as recognized within Micrometer), the type of meter used, and a brief description of each metric's purpose.
It's important to note that the final naming convention of metrics as stored in the collection backend may vary depending on the specific collector used. For detailed mapping relationships, refer to the official Micrometer documentation.

<table><thead><tr><th>Metric Name</th><th>Meter Type</th><th>Description</th></tr></thead><tbody><tr><td><code>mqtt.connection.num.gauge</code></td><td>GAUGE</td><td>Current number of MQTT connections.</td></tr><tr><td><code>mqtt.auth.failure.count</code></td><td>COUNTER</td><td>the counter of authentication failures.</td></tr><tr><td><code>mqtt.connect.count</code></td><td>COUNTER</td><td>The counter of MQTT connect.</td></tr><tr><td><code>mqtt.disconnect.count</code></td><td>COUNTER</td><td>the counter of MQTT disconnect.</td></tr><tr><td><code>mqtt.session.mem.gauge</code></td><td>GAUGE</td><td>Memory usage by MQTT sessions.</td></tr><tr><td><code>mqtt.psession.space.gauge</code></td><td>GAUGE</td><td>Storage space used by persistent MQTT sessions.</td></tr><tr><td><code>mqtt.psession.live.num.gauge</code></td><td>GAUGE</td><td>Number of live persistent MQTT sessions.</td></tr><tr><td><code>mqtt.psession.num.gauge</code></td><td>GAUGE</td><td>Total number of persistent MQTT sessions.</td></tr><tr><td><code>mqtt.ingress.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes received by the broker.</td></tr><tr><td><code>mqtt.egress.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes sent from the broker.</td></tr><tr><td><code>mqtt.channel.latency</code></td><td>TIMER</td><td>Latency of network channels.</td></tr><tr><td><code>mqtt.ingress.qos0.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes received for QoS 0 messages.</td></tr><tr><td><code>mqtt.qos0.dist.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Distribution of QoS 0 message bytes.</td></tr><tr><td><code>mqtt.ingress.qos1.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes received for QoS 1 messages.</td></tr><tr><td><code>mqtt.qos1.dist.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Distribution of QoS 1 message bytes.</td></tr><tr><td><code>mqtt.ingress.qos2.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes received for QoS 2 messages.</td></tr><tr><td><code>mqtt.qos2.dist.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Distribution of QoS 2 message bytes.</td></tr><tr><td><code>mqtt.egress.qos0.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes sent from broker for QoS 0 messages.</td></tr><tr><td><code>mqtt.egress.qos1.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes sent from broker for QoS 1 messages.</td></tr><tr><td><code>mqtt.deliver.qos1.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes delivered for QoS 1 messages.</td></tr><tr><td><code>mqtt.egress.qos2.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes sent from broker for QoS 2 messages.</td></tr><tr><td><code>mqtt.deliver.qos2.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes delivered for QoS 2 messages.</td></tr><tr><td><code>mqtt.in.qos0.latency</code></td><td>TIMER</td><td>Internal latency for QoS 0 message processing.</td></tr><tr><td><code>mqtt.in.qos1.latency</code></td><td>TIMER</td><td>Internal latency for QoS 1 message processing.</td></tr><tr><td><code>mqtt.ex.qos1.latency</code></td><td>TIMER</td><td>External latency for QoS 1 message delivery.</td></tr><tr><td><code>mqtt.in.qos2.latency</code></td><td>TIMER</td><td>Internal latency for QoS 2 message processing.</td></tr><tr><td><code>mqtt.ex.qos2.latency</code></td><td>TIMER</td><td>External latency for QoS 2 message delivery.</td></tr><tr><td><code>mqtt.tfanout.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes fanned out for transient messages.</td></tr><tr><td><code>mqtt.pfanout.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes fanned out for persistent messages.</td></tr><tr><td><code>mqtt.route.space.gauge</code></td><td>GAUGE</td><td>Space used for message routing.</td></tr><tr><td><code>mqtt.shared.sub.num.gauge</code></td><td>GAUGE</td><td>Number of shared subscriptions.</td></tr><tr><td><code>mqtt.tsub.count</code></td><td>COUNTER</td><td>Count of transient subscriptions.</td></tr><tr><td><code>mqtt.tsub.latency</code></td><td>TIMER</td><td>Latency in handling transient subscriptions.</td></tr><tr><td><code>mqtt.psub.count</code></td><td>COUNTER</td><td>Count of persistent subscriptions.</td></tr><tr><td><code>mqtt.psub.latency</code></td><td>TIMER</td><td>Latency in handling persistent subscriptions.</td></tr><tr><td><code>mqtt.tunsub.count</code></td><td>COUNTER</td><td>Count of transient unsubscriptions.</td></tr><tr><td><code>mqtt.tunsub.latency</code></td><td>TIMER</td><td>Latency in handling transient unsubscriptions.</td></tr><tr><td><code>mqtt.punsub.count</code></td><td>COUNTER</td><td>Count of persistent unsubscriptions.</td></tr><tr><td><code>mqtt.punsub.latency</code></td><td>TIMER</td><td>Latency in handling persistent unsubscriptions.</td></tr><tr><td><code>mqtt.tsub.num.gauge</code></td><td>GAUGE</td><td>Number of transient subscriptions currently active.</td></tr><tr><td><code>mqtt.psub.num.gauge</code></td><td>GAUGE</td><td>Number of persistent subscriptions currently active.</td></tr><tr><td><code>mqtt.ingress.retain.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes received for retained messages.</td></tr><tr><td><code>mqtt.retained.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Total bytes of retained messages stored.</td></tr><tr><td><code>mqtt.retained.num.gauge</code></td><td>GAUGE</td><td>Number of retained messages stored.</td></tr><tr><td><code>mqtt.retain.match.count</code></td><td>COUNTER</td><td>Count of retained message matches.</td></tr><tr><td><code>mqtt.retain.matched.bytes</code></td><td>DISTRIBUTION_SUMMARY</td><td>Bytes of retained messages delivered after matching.</td></tr><tr><td><code>mqtt.retain.space.gauge</code></td><td>GAUGE</td><td>Space used for storing retained messages.</td></tr></tbody></table>

- **Internal** latency measures the time between the broker receiving a message and the broker sending the message to subscribing clients.
- **External** latency measures the time between the broker sending the message to subscribing clients and the broker got the acknowledgement from clients, so it's only applied to QoS1 messages(when PubAck received) and QoS2 messages(when
  PubComp received).

---

<a id="admin_guide-observability-events"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/observability/events/ -->

<!-- page_index: 51 -->

# Events

Version: 4.0.0-incubating

# Events

BifroMQ generates events at crucial junctures in its workflow, providing users with the ability to implement custom event collector plugins to capture and process these events.

<a id="admin_guide-observability-events--event-collection-and-usage"></a>

## Event Collection and Usage

The implementation of an event collector plugin in BifroMQ enables the gathering of system-generated events, which can then be utilized across various business scenarios. While BifroMQ does not dictate specific uses for these events, common applications include billing, risk management, real-time diagnostics and more.

<a id="admin_guide-observability-events--demonstration-and-reference-implementation"></a>

## Demonstration and Reference Implementation

To assist users in developing their own event collection solutions, BifroMQ offers the DemoPlugin, which includes the [EventLogger](https://github.com/apache/bifromq/blob/main/build/build-plugin-demo/src/main/java/org/apache/bifromq/demo/plugin/EventLogger.java) as an example of an EventCollector implementation.

<a id="admin_guide-observability-events--interface-stability-and-implementation-guidance"></a>

## Interface Stability and Implementation Guidance

Although event objects form a crucial part of the Event Collector Plugin interface, their stability is considered to be relatively low due to their close association with BifroMQ's internal mechanisms. Given this, it is advisable for plugin developers to ensure their implementations remain in sync with the version of the interface definition they are based on. To prevent compatibility issues, deploying plugins across different interface versions within BifroMQ should be avoided.

<a id="admin_guide-observability-events--plugin-development-best-practices"></a>

## Plugin Development Best Practices

For those interested in extending BifroMQ's capabilities through plugin development, including event collection, further guidance and best practices can be found in the relevant [sections](#plugin-plugin_practice).

- [Event Collection and Usage](#admin_guide-observability-events--event-collection-and-usage)
- [Demonstration and Reference Implementation](#admin_guide-observability-events--demonstration-and-reference-implementation)
- [Interface Stability and Implementation Guidance](#admin_guide-observability-events--interface-stability-and-implementation-guidance)
- [Plugin Development Best Practices](#admin_guide-observability-events--plugin-development-best-practices)

---

<a id="admin_guide-security-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/admin_guide/security/intro/ -->

<!-- page_index: 52 -->

# Security Overview

Version: 4.0.0-incubating

# Security Overview

Security, a broad and critical aspect of any system, is a key focus for BifroMQ. Recognizing the importance of securing MQTT broker deployments, BifroMQ offers a suite of features designed to address various security concerns, from cluster isolation to client authentication and risk management of malicious client behavior.

<a id="admin_guide-security-intro--cluster-isolation-and-secure-inter-node-communication"></a>

## Cluster Isolation and Secure Inter-Node Communication

<a id="admin_guide-security-intro--decentralized-cluster-formation"></a>

### Decentralized Cluster Formation

BifroMQ utilizes a decentralized approach for cluster building, allowing nodes to join a cluster by simply sending a `join` request to any existing cluster member. To prevent unintended cluster mergers due to operational errors, BifroMQ supports specifying a "cluster environment" in the [configuration file](#admin_guide-configuration-config_file_manual). This logical separation ensures that clusters intended for different purposes remain distinct, safeguarding against incorrect merges.

<a id="admin_guide-security-intro--secure-inter-node-communication"></a>

### Secure Inter-Node Communication

Node communication in BifroMQ occurs through two primary methods: P2P communication via `base-cluster` technology and RPC communication via `base-rpc` technology. Both methods offer configurable binding addresses and ports for finer control over firewall rules. Importantly, base-rpc supports TLS configuration, enabling end-to-end secure RPC communication between nodes.

<a id="admin_guide-security-intro--client-authentication-and-authorization"></a>

## Client Authentication and Authorization

<a id="admin_guide-security-intro--auth-provider-plugin"></a>

### Auth Provider Plugin

Client security in BifroMQ encompasses both authentication (verifying client identity) and authorization (granting privileges to various actions). BifroMQ employs the [auth provider plugin](#plugin-auth_provider) as a unified approach to client security management.

<a id="admin_guide-security-intro--secure-communication-channels"></a>

### Secure Communication Channels

BifroMQ supports MQTT over TLS and MQTT over WSS, enabling secure communication between clients and the broker. Businesses can choose between one-way and two-way authentication depending on their security requirements. For two-way authentication scenarios, the plugin implementation can access the complete certificate content, aiding in custom large-scale client certificate lifecycle management.

<a id="admin_guide-security-intro--risk-management-of-bad-behavior-clients"></a>

## Risk Management of Bad-behavior Clients

Identifying and managing bad-behavior clients—those that violate protocol standards or consume excessive system resources—is crucial for maintaining system integrity, especially in large-scale, multi-tenant MQTT deployments. BifroMQ addresses this challenge through real-time event collection and analysis via the EventCollector plugin. By identifying malicious client behaviors and integrating response strategies into the auth provider plugin, BifroMQ enables administrators to deny access to offending clients effectively. While the implementation of such strategies extends beyond BifroMQ's core functionality, the [BifroMQ team](mailto:hello@bifromq.io) offers extensive expertise and professional consulting services for users facing similar challenges.

- [Cluster Isolation and Secure Inter-Node Communication](#admin_guide-security-intro--cluster-isolation-and-secure-inter-node-communication)
  - [Decentralized Cluster Formation](#admin_guide-security-intro--decentralized-cluster-formation)
  - [Secure Inter-Node Communication](#admin_guide-security-intro--secure-inter-node-communication)
- [Client Authentication and Authorization](#admin_guide-security-intro--client-authentication-and-authorization)
  - [Auth Provider Plugin](#admin_guide-security-intro--auth-provider-plugin)
  - [Secure Communication Channels](#admin_guide-security-intro--secure-communication-channels)
- [Risk Management of Bad-behavior Clients](#admin_guide-security-intro--risk-management-of-bad-behavior-clients)

---

<a id="benchmark-overview"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/benchmark/overview/ -->

<!-- page_index: 53 -->

# Benchmark Overview

Version: 4.0.0-incubating

# Benchmark Overview

Coming Soon...

---

<a id="contribution_guide-intro"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/contribution_guide/intro/ -->

<!-- page_index: 54 -->

# Contribution Guide

Version: 4.0.0-incubating

# Contribution Guide

<a id="contribution_guide-intro--contributing-to-apache-bifromq-incubating"></a>

## Contributing to Apache BifroMQ (Incubating)

As an Apache Incubator project, BifroMQ adheres to the principles and processes of the Apache Way: open, transparent, community-driven development. Whether you're helping improve the broker engine, fixing a documentation typo, or proposing new ideas, your contribution makes a meaningful impact.

In this guide, you'll find everything you need to get started contributing to BifroMQ, including:

- [Contribute Code](#contribution_guide-code_contribution)
- [Help with Code Reviews](#contribution_guide-code_review)
- [Improve Documentation and Website](#contribution_guide-documentation_contribution)

- [Contributing to Apache BifroMQ (Incubating)](#contribution_guide-intro--contributing-to-apache-bifromq-incubating)

---

<a id="contribution_guide-code_contribution"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/contribution_guide/code_contribution/ -->

<!-- page_index: 55 -->

# Code Contribution

Version: 4.0.0-incubating

# Code Contribution

<a id="contribution_guide-code_contribution--contribute-code-to-apache-bifromq-incubating"></a>

## Contribute Code to Apache BifroMQ (Incubating)

This guide will walk you through the process of proposing, developing, and submitting code changes to the project.

<a id="contribution_guide-code_contribution--1-find-or-propose-an-issue"></a>

### 1. Find or Propose an Issue

Before writing any code, we recommend the following:

- **Check for Existing Issues:** Browse open issues in [GitHub Issues](https://github.com/apache/bifromq/issues) to see if someone is already working on the task.
- **Propose a New Issue:** If your idea is new, open an issue describing the problem or feature clearly. Include motivation, background, and potential approaches.

> For larger changes, it's a good idea to discuss your proposal on the [dev@bifromq.apache.org](mailto:dev@bifromq.apache.org) mailing list before starting implementation.

<a id="contribution_guide-code_contribution--2-work-on-the-code"></a>

### 2. Work on the Code

Once an issue is assigned to you or you’ve received a green light from the community:

<a id="contribution_guide-code_contribution--clone-the-repository"></a>

#### Clone the Repository

```bash
git clone https://github.com/apache/bifromq.git
cd bifromq
```

<a id="contribution_guide-code_contribution--follow-coding-guidelines"></a>

#### Follow Coding Guidelines

Please follow BifroMQ’s:

- Code style conventions (Java)
- Commit message format (`[Component] Description`)

> Tip: Include meaningful tests for your changes and ensure existing tests pass.

<a id="contribution_guide-code_contribution--3-submit-a-pull-request-pr"></a>

### 3. Submit a Pull Request (PR)

Once your changes are ready:

- Push your branch to your fork
- Open a Pull Request against the target branch
- Reference the corresponding issue in the PR description (e.g., “Fixes #123”)
- Include a clear summary of the changes and motivation

<a id="contribution_guide-code_contribution--4-address-review-feedback"></a>

### 4. Address Review Feedback

During the review phase:

- Engage constructively with feedback
- Revise your code as needed
- Rebase your branch to keep the commit history clean

Once your PR is approved, a committer will merge it. Congratulations!

<a id="contribution_guide-code_contribution--5-merge-change"></a>

### 5. Merge change

The code will be merged by a committer once the review is finished.

After your contribution is merged:

- Consider picking up another issue
- Help review others’ PRs
- Share your experiences and ideas on the mailing list

- [Contribute Code to Apache BifroMQ (Incubating)](#contribution_guide-code_contribution--contribute-code-to-apache-bifromq-incubating)
  - [1. Find or Propose an Issue](#contribution_guide-code_contribution--1-find-or-propose-an-issue)
  - [2. Work on the Code](#contribution_guide-code_contribution--2-work-on-the-code)
  - [3. Submit a Pull Request (PR)](#contribution_guide-code_contribution--3-submit-a-pull-request-pr)
  - [4. Address Review Feedback](#contribution_guide-code_contribution--4-address-review-feedback)
  - [5. Merge change](#contribution_guide-code_contribution--5-merge-change)

---

<a id="contribution_guide-code_review"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/contribution_guide/code_review/ -->

<!-- page_index: 56 -->

# Code Review

Version: 4.0.0-incubating

# Code Review

<a id="contribution_guide-code_review--review-a-pull-request"></a>

## Review a Pull Request

Here’s how you can effectively review a Pull Request (PR) in BifroMQ:

<a id="contribution_guide-code_review--1-understand-the-context"></a>

### 1. Understand the Context

Before diving into the code:

- **Read the PR description carefully.** Understand what problem the change solves and how.
- **Check the linked issue**, if any. This gives insight into the motivation, discussion history, and design considerations.
- **Scan the commit message(s)** to ensure they follow the project’s format and are descriptive.

<a id="contribution_guide-code_review--2-review-checklist"></a>

### 2. Review Checklist

While reviewing, consider the following:

<a id="contribution_guide-code_review--correctness"></a>

#### Correctness

- Does the code behave as described?
- Are edge cases handled properly?
- Is it backwards-compatible?

<a id="contribution_guide-code_review--test-coverage"></a>

#### Test Coverage

- Are there new or updated tests that cover the change?
- Do tests pass locally or in CI?

<a id="contribution_guide-code_review--code-quality"></a>

#### Code Quality

- Is the code clear and easy to understand?
- Are any parts overly complex or in need of refactoring?
- Does the code follow BifroMQ’s style and conventions?

<a id="contribution_guide-code_review--design-architecture"></a>

#### Design & Architecture

- Does the change align with the existing architecture?
- Could it introduce unnecessary coupling, duplication, or inefficiency?

<a id="contribution_guide-code_review--documentation"></a>

#### Documentation

- Are code comments helpful and accurate?
- For user-facing changes, is documentation updated where applicable?

<a id="contribution_guide-code_review--3-give-constructive-feedback"></a>

### 3. Give Constructive Feedback

Use GitHub’s review tools to:

- Ask clarifying questions
- Suggest improvements
- Point out potential bugs
- Praise good practices and elegant solutions

Be respectful and collaborative — we strive to foster a supportive and inclusive community. Assume positive intent and focus on shared learning and improvement.

<a id="contribution_guide-code_review--4-approve-or-request-changes"></a>

### 4. Approve or Request Changes

Once you’re done reviewing:

- If the PR meets the quality bar, approve it.
- If changes are needed, submit a review with comments and select **“Request changes”**.
- If you're not sure, leave comments and mark the review as **“Comment only”** — others can follow up.

<a id="contribution_guide-code_review--5-follow-up"></a>

### 5. Follow Up

After leaving your review:

- Stay engaged if the author responds with updates or questions.
- Re-review the PR after updates and adjust your review status if needed.

- [Review a Pull Request](#contribution_guide-code_review--review-a-pull-request)
  - [1. Understand the Context](#contribution_guide-code_review--1-understand-the-context)
  - [2. Review Checklist](#contribution_guide-code_review--2-review-checklist)
  - [3. Give Constructive Feedback](#contribution_guide-code_review--3-give-constructive-feedback)
  - [4. Approve or Request Changes](#contribution_guide-code_review--4-approve-or-request-changes)
  - [5. Follow Up](#contribution_guide-code_review--5-follow-up)

---

<a id="contribution_guide-documentation_contribution"></a>

<!-- source_url: https://bifromq.incubator.apache.org/docs/contribution_guide/documentation_contribution/ -->

<!-- page_index: 57 -->

# Documentation Contribution

Version: 4.0.0-incubating

# Documentation Contribution

<a id="contribution_guide-documentation_contribution--contribute-to-documentation"></a>

## Contribute to Documentation

We welcome and encourage all kinds of documentation improvements.

<a id="contribution_guide-documentation_contribution--what-you-can-contribute"></a>

### What You Can Contribute

Here are some ways you can help improve the documentation:

- Fix typos, grammar, or formatting issues
- Clarify instructions or explanations
- Update outdated content
- Add new sections (e.g., feature usage, configuration examples, deployment tips)
- Improve the structure or navigation
- Translate content (when relevant)
- Update or improve the project website

No contribution is too small — even fixing a broken link makes a difference!

<a id="contribution_guide-documentation_contribution--how-the-documentation-is-organized"></a>

### How the Documentation is Organized

BifroMQ’s documentation is hosted in the main [GitHub repository](https://github.com/apache/bifromq-sites) under: `docs/`

- `docs/` contains technical guides, usage examples, and system architecture.

<a id="contribution_guide-documentation_contribution--how-to-contribute-documentation"></a>

### How to Contribute Documentation

1. **Fork the Repository**

   Fork [bifromq-sites](https://github.com/apache/bifromq-sites) to your own GitHub account.
2. **Create a Branch**


```bash
git checkout -b feat-xyz
```

3. **Edit or Add Content**

   - Use Markdown for most files.
   - Follow the existing writing style and structure.
   - Preview locally if making website changes (e.g., using `npm install` then running `npm start`).
4. **Open a Pull Request**

   - Push your branch and open a PR targeting the `master` branch.
   - Use a clear title like: `[Docs] Clarify broker configuration options`.
   - Explain what you changed and why.

<a id="contribution_guide-documentation_contribution--writing-guidelines"></a>

### Writing Guidelines

- Use clear, concise language.
- Favor practical examples and command-line snippets.
- Be consistent in tone (neutral and helpful).
- Link to relevant code or external references when useful.

<a id="contribution_guide-documentation_contribution--need-help"></a>

### Need Help?

If you're unsure about what or how to contribute:

- **Check open issues** labeled `documentation` or `good first issue`
- **Ask on the mailing list:** [dev@bifromq.apache.org](mailto:dev@bifromq.apache.org)

- [Contribute to Documentation](#contribution_guide-documentation_contribution--contribute-to-documentation)
  - [What You Can Contribute](#contribution_guide-documentation_contribution--what-you-can-contribute)
  - [How the Documentation is Organized](#contribution_guide-documentation_contribution--how-the-documentation-is-organized)
  - [How to Contribute Documentation](#contribution_guide-documentation_contribution--how-to-contribute-documentation)
  - [Writing Guidelines](#contribution_guide-documentation_contribution--writing-guidelines)
  - [Need Help?](#contribution_guide-documentation_contribution--need-help)

---
