# Architecture

## Navigation

- [Overview](#index)
- [Design](#design-database-design)
  - [Admin Database Design](#design-database-design)
  - [Data Sync Design](#design-data-sync)
  - [Flow Control Design](#design-flow-control)
  - [Client Registry Design](#design-register-center-design)
  - [SPI Design](#design-spi-design)
  - [WASM plugin design](#design-wasm-plugin-design)
- [Deployment](#deployment-deployment-before)
  - [Deployment Prerequisites](#deployment-deployment-before)
  - [Local Deployment](#deployment-deployment-local)
  - [Local Quick Deployment](#deployment-deployment-quick)
  - [Binary Packages Deployment](#deployment-deployment-package)
  - [Docker-compose Deployment](#deployment-deployment-docker-compose)
  - [Docker Deployment](#deployment-deployment-docker)
  - [K8s Deployment](#deployment-deployment-k8s)
  - [Helm Deployment](#deployment-deployment-helm)
  - [aaPanel Deployment](#deployment-deployment-aapanel)
  - [Custom Deployment](#deployment-deployment-custom)
  - [Cluster Deployment](#deployment-deployment-cluster)
- [Quick Start](#quick-start-quick-start-dubbo)
  - [Quick start with Dubbo](#quick-start-quick-start-dubbo)
  - [Quick start with gRPC](#quick-start-quick-start-grpc)
  - [Quick start with Http](#quick-start-quick-start-http)
  - [Quick start with Mcp Server](#quick-start-quick-start-mcpserver)
  - [Quick start with Motan](#quick-start-quick-start-motan)
  - [Quick start with Sofa](#quick-start-quick-start-sofa)
  - [Quick start with Spring Cloud](#quick-start-quick-start-springcloud)
  - [Quick start with Tars](#quick-start-quick-start-tars)
  - [Quick start with Websocket](#quick-start-quick-start-websocket)
- [User Guide](#user-guide-admin-usage-api-document)
  - [Admin Usage](#user-guide-admin-usage-api-document)
    - [API Document Management](#user-guide-admin-usage-api-document)
    - [Data Permission Management](#user-guide-admin-usage-data-permission)
    - [Dictionary Management](#user-guide-admin-usage-dictionary-management)
    - [Namespace Management](#user-guide-admin-usage-namepsace)
    - [Plugin Config](#user-guide-admin-usage-plugin-handle-explanation)
    - [Role Management](#user-guide-admin-usage-role-management)
    - [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule)
  - [Property Config](#user-guide-property-config-admin-property-config)
    - [Admin Property Config](#user-guide-property-config-admin-property-config)
    - [Client Property Config](#user-guide-property-config-client-property-config)
    - [Gateway Property Config](#user-guide-property-config-gateway-property-config)
    - [Application Client Access Config](#user-guide-property-config-register-center-access)
    - [Register Center Instance Config](#user-guide-property-config-register-center-instance)
    - [Gateway SSL Config](#user-guide-property-config-ssl)
    - [Data Synchronization Config](#user-guide-property-config-use-data-sync)
  - [Shenyu-Sdk Usage](#user-guide-sdk-usage-shenyu-sdk-consul)
    - [Using Consul with Shenyu-SDK](#user-guide-sdk-usage-shenyu-sdk-consul)
    - [Using Etcd with Shenyu-SDK](#user-guide-sdk-usage-shenyu-sdk-etcd)
    - [Using Eureka with Shenyu-SDK](#user-guide-sdk-usage-shenyu-sdk-eureka)
    - [Using Shenyu-SDK-Feign](#user-guide-sdk-usage-shenyu-sdk-feign)
    - [Using Nacos with Shenyu-SDK](#user-guide-sdk-usage-shenyu-sdk-nacos)
    - [Using Zookeeper with Shenyu-SDK](#user-guide-sdk-usage-shenyu-sdk-zookeeper)
  - [Discovery](#user-guide-discovery-discovery-mode)
    - [Discovery](#user-guide-discovery-discovery-mode)
  - [Quick Connect to Your Service](#user-guide-proxy-dubbo-proxy)
    - [Dubbo Proxy](#user-guide-proxy-dubbo-proxy)
    - [gRPC Proxy](#user-guide-proxy-grpc-proxy)
    - [Http Proxy](#user-guide-proxy-http-proxy)
    - [McpTool Service Integration](#user-guide-proxy-mcp-tool-proxy)
    - [Motan Proxy](#user-guide-proxy-motan-proxy)
    - [Sofa Proxy](#user-guide-proxy-sofa-rpc-proxy)
    - [Spring Cloud Proxy](#user-guide-proxy-spring-cloud-proxy)
    - [Tars Proxy](#user-guide-proxy-tars-proxy)
    - [Websocket Proxy](#user-guide-proxy-websocket-proxy)
  - [Kubernetes Controller](#user-guide-kubernetes-controller-build-deploy)
    - [Build And Deploy Kubernetes Controller](#user-guide-kubernetes-controller-build-deploy)
    - [Kubernetes Controller Config](#user-guide-kubernetes-controller-config)
  - [API Document Aggregation](#user-guide-api-doc-shenyu-annotation-apidoc)
    - [The client registers the API documentation](#user-guide-api-doc-shenyu-annotation-apidoc)
    - [Pull the swagger registration API document](#user-guide-api-doc-swagger-apidoc)
- [Plugin Center](#plugin-center-http-process-contextpath-plugin)
  - [Http Process](#plugin-center-http-process-contextpath-plugin)
    - [ContextPath Plugin](#plugin-center-http-process-contextpath-plugin)
    - [ModifyResponse Plugin](#plugin-center-http-process-modifyresponse-plugin)
    - [ParamMapping Plugin](#plugin-center-http-process-parammapping-plugin)
    - [Redirect Plugin](#plugin-center-http-process-redirect-plugin)
    - [Request Plugin](#plugin-center-http-process-request-plugin)
    - [Rewrite Plugin](#plugin-center-http-process-rewrite-plugin)
  - [Proxy](#plugin-center-proxy-divide-plugin)
    - [Divide Plugin](#plugin-center-proxy-divide-plugin)
    - [Dubbo Plugin](#plugin-center-proxy-dubbo-plugin)
    - [gRPC Plugin](#plugin-center-proxy-grpc-plugin)
    - [Motan Plugin](#plugin-center-proxy-motan-plugin)
    - [Mqtt Plugin](#plugin-center-proxy-mqtt-plugin)
    - [Sofa Plugin](#plugin-center-proxy-sofa-plugin)
    - [Spring Cloud Plugin](#plugin-center-proxy-spring-cloud-plugin)
    - [Tars Plugin](#plugin-center-proxy-tars-plugin)
    - [Tcp Plugin](#plugin-center-proxy-tcp-plugin)
    - [Websocket Plugin](#plugin-center-proxy-websocket-plugin)
  - [Fault Tolerance](#plugin-center-fault-tolerance-hystrix-plugin)
    - [Hystrix Plugin](#plugin-center-fault-tolerance-hystrix-plugin)
    - [RateLimiter Plugin](#plugin-center-fault-tolerance-rate-limiter-plugin)
    - [Resilience4j Plugin](#plugin-center-fault-tolerance-resilience4j-plugin)
    - [Sentinel Plugin](#plugin-center-fault-tolerance-sentinel-plugin)
  - [Security](#plugin-center-security-casdoor)
    - [Casdoor Plugin](#plugin-center-security-casdoor)
    - [CryptorRequest plugin](#plugin-center-security-cryptor-request-plugin)
    - [CryptorResponse plugin](#plugin-center-security-cryptor-response-plugin)
    - [JWT plugin](#plugin-center-security-jwt-plugin)
    - [OAuth2 Plugin](#plugin-center-security-oauth2-plugin)
    - [Sign Plugin](#plugin-center-security-sign-plugin)
    - [Waf Plugin](#plugin-center-security-waf-plugin)
  - [Observability](#plugin-center-observability-logging-aliyun-sls)
    - [Logging-Aliyun-Sls Plugin](#plugin-center-observability-logging-aliyun-sls)
    - [Logging-ElasticSearch Plugin](#plugin-center-observability-logging-elasticsearch)
    - [Logging-Huawei-Lts Plugin](#plugin-center-observability-logging-huawei-lts)
    - [Logging-Kafka Plugin](#plugin-center-observability-logging-kafka)
    - [Logging Plugin](#plugin-center-observability-logging-plugin)
    - [Logging-Pulsar Plugin](#plugin-center-observability-logging-pulsar)
    - [Logging-RabbitMQ Plugin](#plugin-center-observability-logging-rabbitmq)
    - [Logging-RocketMQ Plugin](#plugin-center-observability-logging-rocketmq)
    - [Logging-Tencent-Cls Plugin](#plugin-center-observability-logging-tencent-cls)
    - [Metrics Plugin](#plugin-center-observability-metrics-plugin)
  - [Common](#plugin-center-common-general-context-plugin)
    - [GeneralContext Plugin](#plugin-center-common-general-context-plugin)
  - [Cache](#plugin-center-cache-cache-plugin)
    - [Cache Plugin](#plugin-center-cache-cache-plugin)
  - [Mock](#plugin-center-mock-mock-plugin)
    - [Mock Plugin](#plugin-center-mock-mock-plugin)
  - [Ai](#plugin-center-ai-ai-prompt)
    - [AiPrompt Plugin](#plugin-center-ai-ai-prompt)
    - [AiProxy Plugin](#plugin-center-ai-ai-proxy)
    - [AiTokenLimiter Plugin](#plugin-center-ai-ai-token-limiter)
  - [Mcp](#plugin-center-mcp-mcp-server-plugin)
    - [McpServer Plugin](#plugin-center-mcp-mcp-server-plugin)
- [Developer](#developer-spi-custom-load-balance)
  - [SPI](#developer-spi-custom-load-balance)
    - [Custom Load Balancer](#developer-spi-custom-load-balance)
    - [Custom Match Mode](#developer-spi-custom-match-mode)
    - [Custom Metrics Monitor](#developer-spi-custom-metrics-monitor)
    - [Custom Mock Data Generator](#developer-spi-custom-mock-generator)
    - [Custom Parameter Data](#developer-spi-custom-parameter-data)
    - [Custom Predicate Judge](#developer-spi-custom-predicate-judge)
    - [Custom Rate Limiter](#developer-spi-custom-rate-limiter)
  - [Custom Filter](#developer-custom-filter)
  - [Custom Jwt convert Algorithm](#developer-custom-jwt-covert-algorithm)
  - [Fetching Correct IP Address And Host](#developer-custom-parsing-ip-and-host)
  - [Custom Plugin](#developer-custom-plugin)
  - [Custom Response](#developer-custom-result)
  - [Custom Sign Algorithm](#developer-custom-sign-algorithm)
  - [A multilingual HTTP client](#developer-developer-shenyu-client)
  - [File Upload And Download](#developer-file-and-image)
  - [Run Integration Test Locally](#developer-integration-test)
  - [Local Model](#developer-local-model)
  - [Alarm Notice](#developer-notice-alert)
  - [ShenYu Optimize](#developer-shenyu-optimize)
  - [Thread Model](#developer-thread-model)
- [Benchmark Test](#benchmark-test)

## Content

<a id="index"></a>

<!-- source_url: https://shenyu.apache.org/docs/ -->

<!-- page_index: 1 -->

# Architecture

Version: 2.7.0.3

![](assets/images/shenyu-architecture-3d-2b673fe8dfd0ef6a14223ffd00bfe824_a242b39b3ed79509.png)

<a id="index--what-is-the-apache-shenyu"></a>

# What is the Apache ShenYu?

This is an asynchronous, high-performance, cross-language, responsive API gateway.

<a id="index--why-named-apache-shenyu"></a>

# Why named Apache ShenYu

ShenYu (神禹) is the honorific name of Chinese ancient monarch Xia Yu (also known in later times as Da Yu), who left behind the touching story of the three times he crossed the Yellow River for the benefit of the people and successfully managed the flooding of the river. He is known as one of the three greatest kings of ancient China, along with Yao and Shun.

- Firstly, the name ShenYu is to promote the traditional virtues of our Chinese civilisation.
- Secondly, the most important thing about the gateway is the governance of the traffic.
- Finally, the community will do things in a fair, just, open and meritocratic way, paying tribute to ShenYu while also conforming to the Apache Way.

---

<a id="index--features"></a>

# Features

- Proxy: Support for Apache® Dubbo™, Spring Cloud, gRPC, Motan, SOFA, TARS, WebSocket, MQTT
- Security: Sign, OAuth 2.0, JSON Web Tokens, WAF plugin
- API governance: Request, response, parameter mapping, Hystrix, RateLimiter plugin
- Observability: Tracing, metrics, logging plugin
- Dashboard: Dynamic traffic control, visual backend for user menu permissions
- Extensions: Plugin hot-swapping, dynamic loading
- Cluster: NGINX, Docker, Kubernetes
- Language: provides .NET, Python, Go, Java client for API register

---

<a id="index--mind-map"></a>

# Mind map

![](assets/images/shenyu-xmind-1e9e293ec1650cd3d74beaf7b48464c1_a5c2e65896c8f965.png)

---

<a id="index--quick-start-docker"></a>

# Quick Start (docker)

```text
docker pull apache/shenyu-admin 
docker network create shenyu 
docker run -d -p 9095:9095 --net shenyu apache/shenyu-admin 
```

Default account: **admin**

Default password: **123456**

```text
docker pull apache/shenyu-bootstrap 
docker run -d -p 9195:9195 -e "shenyu.local.enabled=true" --net shenyu apache/shenyu-bootstrap 
```

- Real requests ：<http://127.0.0.1:8080/helloworld>,

```json
{ 
  "name" : "Shenyu", 
  "data" : "hello world" 
} 
```

- Set routing rules (Standalone)

Add `localKey: 123456` to Headers. If you need to customize the localKey, you can use the sha512 tool to generate the key based on plaintext and update the `shenyu.local.sha512Key` property.

```text
curl --location --request POST 'http://localhost:9195/shenyu/plugin/selectorAndRules' \ 
--header 'Content-Type: application/json' \ 
--header 'localKey: 123456' \ 
--data-raw '{ 
    "pluginName": "divide", 
    "selectorHandler": "[{\"upstreamUrl\":\"127.0.0.1:8080\"}]", 
    "conditionDataList": [{ 
        "paramType": "uri", 
        "operator": "match", 
        "paramValue": "/**" 
    }], 
    "ruleDataList": [{ 
        "ruleHandler": "{\"loadBalance\":\"random\"}", 
        "conditionDataList": [{ 
            "paramType": "uri", 
            "operator": "match", 
            "paramValue": "/**" 
        }] 
    }] 
}' 
```

- Proxy request ：<http://localhost:9195/helloworld>

```json
{ 
  "name" : "Shenyu", 
  "data" : "hello world" 
} 
```

---

<a id="index--plugin"></a>

# Plugin

Whenever a request comes in, Apache ShenYu will execute it by all enabled plugins through the chain of responsibility.

As the heart of Apache ShenYu, plugins are extensible and hot-pluggable.

Different plugins do different things.

Of course, users can also customize plugins to meet their own needs.

If you want to customize, see [custom-plugin](#developer-custom-plugin) .

---

<a id="index--selector-rule"></a>

# Selector & Rule

According to your HTTP request headers, selectors and rules are used to route your requests.

Selector is your first route, It is coarser grained, for example, at the module level.

Rule is your second route and what do you think your request should do. For example a method level in a module.

The selector and the rule match only once, and the match is returned. So the coarsest granularity should be sorted last.

---

<a id="index--data-caching-data-sync"></a>

# Data Caching & Data Sync

Since all data have been cached using ConcurrentHashMap in the JVM, it's very fast.

Apache ShenYu dynamically updates the cache by listening to the ZooKeeper node (or WebSocket push, HTTP long polling) when the user changes configuration information in the background management.

![](assets/images/shenyu-config-processor-en-170fb1137ef0f931707f12aecd38c455_d70acc87445fe988.png)

![](assets/images/config-strategy-processor-en-444a26ebaffbb5cba994880b2487541f_e9c7a94031a55619.png)

---

<a id="index--prerequisite"></a>

# Prerequisite

- JDK 1.8+

---

<a id="index--stargazers-over-time"></a>

# Stargazers over time

[![](https://starchart.cc/apache/shenyu.svg)](https://starchart.cc/apache/shenyu.svg)

---

<a id="index--contributor-and-support"></a>

# Contributor and Support

- [How to Contribute](https://shenyu.apache.org/community/contributor-guide)
- [Mailing Lists](mailto:dev@shenyu.apache.org)

---

<a id="index--known-users"></a>

# Known Users

In order of registration, More access companies are welcome to register at <https://github.com/apache/shenyu/issues/68> (For open source users only) .

All Users : [Known Users](https://shenyu.apache.org/community/user-registration)

---

---

<a id="design-database-design"></a>

<!-- source_url: https://shenyu.apache.org/docs/design/database-design/ -->

<!-- page_index: 2 -->

# Admin Database Design

Version: 2.7.0.3

Apache Shenyu Admin is the management system of the gateway, which can manage all plugins, selectors and rules visually, set users, roles and resources.

- Plugin: ShenYu uses the plugin design idea to realize the hot plug of the plugin, which is easy to expand. Built-in rich plugins, including RPC proxy, circuit breaker and current limiting, authority and certification, monitoring, and more.
- Selector: Each plugin can set multiple selectors to carry out preliminary filtering of traffic.
- Rule: Multiple rules can be set per selector for more fine-grained control of flow.
- The Database Table UML Diagram:

![](assets/images/shenyu-db-0847449c4fb817f83e61abad7125ae4a_bff80a8acb489b4e.png)

- Detailed design:

  - One plugin corresponds to multiple selectors,one selector corresponds to multiple rules.
  - One selector corresponds to multiple match conditions,one rule corresponds to multiple match conditions.
  - Each rule handles differently in corresponding plugin according to field handler,field handler is a kind of data of JSON string type.You can view detail during the use of shenyu-admin.

- The resource are the menus and buttons in the shenyu-admin console.
- Resource Permission use database to store user name,role,resource data and relationship.
- The Resource Permission Table UML Diagram:
  ![](assets/images/shenyu-permission-db-90c870eefea0da663079cdf6638c7ce7_d6c6caca5d6fa91e.png)
- Detailed design:

  - one user corresponds to multiple role,one role corresponds to multiple resources.

- Data Permission use database to store the relationship between users, selectors and rules.
- The Data Permission Table UML Diagram:
  ![data permission uml](assets/images/data-permission-f382375f134eeb359e481ee2cd43482d_f2d4c247fea1f32b.png)
- Detailed design:

  - The most important table is `data_permission`, where a user corresponds to multiple data permissions.
  - The field `data_type` distinguishes between different types of data, which corresponds to the following: 0 -> selector, 1 -> rule.
  - The field `data_id` holds the primary key id of the corresponding type.

- Metadata is used for generic invoke by gateway.
- For each interface method, there is one piece of metadata.
- The Database Table UML Diagram:

![](assets/images/mata-data-table_625b2ab2a32bafb8.png)

- Detailed design：
  - `path`: When the gateway is requested, a piece of data will be matched according to `path`, and then the subsequent process will be carried out.
  - `rpc_ext`: Used to hold extended information for the RPC proxy.。

- Dictionary management is used to maintain and manage public data dictionaries.
- The Database Table UML Diagram:

![](assets/images/shenyu-dict_3408c8153088ba9f.png)

- The API document tables used to maintain and manage API documents.
- The API document (such as json, md, html, etc.) of common specifications (such as OpenApi3.0 and yapi) can be imported into `shenyu-admin` and finally stored in the API document tables.
- API documents of other common specifications can be generated through the API document tables.
- The Database Table UML Diagram:

![](assets/images/shenyu-api-doc-table_bc7d8b0929d4bee5.png)

- Detailed design:
  - A tag can have multiple child tags, the level of tags is unlimited, the lowest leaf node is API.
  - Interfaces with the same path but supporting multiple http methods, they are counted as multiple APIs.
  - An API has multiple request parameters and response fields.
  - A parameter/field has its own type (model), and each type have multiple fields.
  - A field has its own type, which corresponds to multiple values.
  - A value can be used as either a request example value, or a response example value (for example, 200 indicates OK, and 400 indicates illegal parameters).
  - The `query`, `header` and `body`, all of them are `json` stored in `mock_request_record`，but `body` does not support special types such as file  。
  - The `ext` of the `tag` table stores the full amount of json data of its parent tag (including the parent tag of the parent tag, and so on).
  - The `ext` of the `api` table may store the IP list and the service name of `SpringCloud`.
  - The `type` of the `parameter` table mainly includes `requestUrlParam`, `requestHeader`, `requestBody`, `requestPathVariable`, `responseHeader`, and `responseBody`; If the returned type is a special type (such as file), do not associate `model_id`.
  - The `ext` of the `field` table stores generic type in json format (convenient for subsequent expansion), such as `{"genericTypes": [model_id1, model_id2]}`; `model_id` indicates which type has this field, `self_model_id` indicates which type of this field.
  - The `is_example` of `detail` table indicates whether a value is a request sample value, true is a request sample value, and false is a response value.

---

<a id="design-data-sync"></a>

<!-- source_url: https://shenyu.apache.org/docs/design/data-sync/ -->

<!-- page_index: 3 -->

# Data Sync Design

Version: 2.7.0.3

This document explains the principle of data synchronization. Data synchronization refers to the strategy used to synchronize data to ShenYu gateway after shenyu-admin background operation data. ShenYu gateway currently supports ZooKeeper, WebSocket, HTTP Long Polling, Nacos, Etcd and Consul for data synchronization.

See [Data Synchronization Configuration](#user-guide-property-config-use-data-sync) for configuration information about data synchronization.

![](assets/images/data-sync-dir-en_d6ae0d74052f170a.png)

Gateway is the entrance of request and it is a very important part in micro service architecture, therefore the importance of gateway high availability is self-evident. When we use gateway, we have to change configuration such as flow rule, route rule for satisfying business requirement. Therefore, the dynamic configuration of the gateway is an important factor to ensure the high availability of the gateway.

In the actual use of Apache ShenYu Gateway, users also feedback some problems:

- Apache ShenYu depends on ZooKeeper, how to use Etcd, Consul, Nacos and other registry center?
- Apache ShenYu depends on Redis and InfluxDB, and do not use limiting plugins or monitoring plugins. Why need these?
- Why not use configuration center for configuration synchronization?
- Why can't updates be configured dynamically?
- Every time you want to query the database, Redis is a better way.

According to the feedback of users, we have also partially reconstructed ShenYu. The current data synchronization features are as follows:

- All configuration is cached in ShenYu gateway memory, each request uses local cache, which is very fast.
- Users can modify any data in the background of shenyu-admin, and immediately synchronize to the gateway memory.
- Support ShenYu plugin, selector, rule data, metadata, signature data and other data synchronization.
- All plugin selectors and rules are configured dynamically and take effect immediately, no service restart required.
- Data synchronization mode supports Zookeeper, HTTP long polling, Websocket, Nacos, Etcd and Consul.

The following figure shows the process of data synchronization of ShenYu. ShenYu Gateway will synchronize configuration data from configuration service at startup, and support push-pull mode to get configuration change information, and then update local cache. The administrator can change the user permissions, rules, plugins and traffic configuration in the admin system(shenyu-admin), and synchronize the change information to ShenYu Gateway through the push-pull mode. Whether the mode is push or pull depends on the synchronization mode used.

![](assets/images/shenyu-config-processor-en_ccfc766913ab675f.png)

In the original version, the configuration service relied on the Zookeeper implementation to manage the back-end push of changes to the gateway. Now, WebSocket, HTTP long polling, ZooKeeper, Nacos, Etcd, and Consul can now be supported by specifying the corresponding synchronization policy by setting `shenyu.sync.${strategy}` in the configuration file. The default WeboSocket synchronization policy can be used to achieve second level data synchronization. However, it is important to note that Apache ShenYu Gateway and shenyu-admin must use the same synchronization policy.

As showing picture below,`shenyu-admin` will issue a configuration change notification through `EventPublisher` after users change configuration,`EventDispatcher` will handle this modification and send configuration to corresponding event handler according to configured synchronization strategy.

- If it is a `websocket` synchronization strategy,it will push modified data to `shenyu-web`,and corresponding `WebsocketDataHandler` handler will handle `shenyu-admin` data push at the gateway layer
- If it is a `zookeeper` synchronization strategy,it will push modified data to `zookeeper`,and the `ZookeeperSyncCache` will monitor the data changes of `zookeeper` and process them
- If it is a `http` synchronization strategy,`shenyu-web` proactively initiates long polling requests,90 seconds timeout by default,if there is no modified data in `shenyu-admin`,http request will be blocked,if there is a data change, it will respond to the changed data information,if there is no data change after 60 seconds,then respond with empty data,gateway continue to make http request after getting response,this kind of request will repeat.

![](assets/images/config-strategy-processor-en_bbaa5f2622dd6d1b.png)

The zookeeper-based synchronization principle is very simple,it mainly depends on `zookeeper` watch mechanism,`shenyu-web` will monitor the configured node,when `shenyu-admin` starts,all the data will be written to `zookeeper`,it will incrementally update the nodes of `zookeeper` when data changes,at the same time, `shenyu-web` will monitor the node for configuration information, and update the local cache once the information changes

![Zookeeper Node Design](assets/images/shenyu-data-sync-zookeeper-46808f3374aaa2ba781e90261596adf0_98ea5939c07f2d93.png)

`Apache ShenYu` writes the configuration information to the zookeeper node,and it is meticulously designed. If you want to learn more about the code implementation, refer to the source code `ZookeeperSyncDataService`.

The mechanism of `websocket` and `zookeeper` is similar,when the gateway and the `shenyu-admin` establish a `websocket` connection,`shenyu-admin` will push all data at once,it will automatically push incremental data to `shenyu-web` through `websocket` when configured data changes

When we use websocket synchronization,pay attention to reconnect after disconnection,which also called keep heartbeat.`Apache ShenYu` uses `java-websocket` ,a third-party library,to connect to `websocket`. If you want to learn more about the code implementation, refer to the source code `WebsocketSyncDataService`.

The mechanism of zookeeper and websocket data synchronization is relatively simple,but http synchronization will be relatively complicated.ShenYu borrows the design ideas of `Apollo` and `Nacos` and realizes `http` long polling data synchronization using their advantages.Note that this is not traditional ajax long polling.

![](assets/images/http-long-polling-en_c92e5a2272201d19.png)

http long polling mechanism as above,shenyu-web gateway requests shenyu-admin configuration services,timeout is 90 seconds,it means gateway layer request configuration service will wait at most 90 seconds,this is convenient for shenyu-admin configuration service to respond modified data in time,and therefore we realize near real-time push.

After the http request reaches shenyu-admin, it does not respond immediately,but uses the asynchronous mechanism of Servlet3.0 to asynchronously respond to the data.First of all,put long polling request task `LongPollingClient` into `BlocingQueue`,and then start scheduling task,execute after 60 seconds,this aims to remove the long polling request from the queue after 60 seconds,even there is no configured data change.Because even if there is no configuration change,gateway also need to know,otherwise it will wait,and there is a 90 seconds timeout when the gateway requests configuration services.

If the administrator changes the configuration data during this period,the long polling requests in the queue will be removed one by one, and respond which group’s data has changed(we distribute plugins, rules, flow configuration , user configuration data into different groups).After gateway receives response,it only knows which Group has changed its configuration,it need to request again to get group configuration data.Someone may ask,why don't you write out the changed data directly?We also discussed this issue deeply during development, because the http long polling mechanism can only guarantee quasi real-time,if gateway layer does not handle it in time,or administrator updates configuration frequently,we probably missed some configuration change push.For security, we only inform that a certain Group information has changed.

When `shenyu-web` gateway layer receives the http response information,pull modified information(if exists),and then request `shenyu-admin` configuration service again,this will repeatedly execute. If you want to learn more about the code implementation, refer to the source code `HttpSyncDataService`.

The synchronization principle of Nacos is basically similar to that of ZooKeeper, and it mainly depends on the configuration management of Nacos. The path of each configuration node is similar to that of ZooKeeper.

ShenYu gateway will monitor the configured node. At startup, if there is no configuration node in Nacos, it will write the synchronous full amount of data into Nacos. When the sequential data send changes, it will update the configuration node in Nacos in full amount. The local cache is updated.

If you want to learn more about the code implementation, please refer to the source code `NacosSyncDataService` and the official documentation for [Nacos](https://nacos.io/zh-cn/docs/sdk.html) .

Etcd data synchronization principle is similar to Zookeeper, mainly relying on Etcd's watch mechanism, and each configuration node path is the same as that of Zookeeper.

The native API for Etcd is a bit more complicated to use, so it's somewhat encapsulated.

ShenYu gateway will listen to the configured node. When startup, if there is no configuration node in Etcd, it will write the synchronous full amount of data into Etcd. When the sequential data send changes, it will update the configuration node in Etcd incrementally.

If you want to learn more about the code implementation, refer to the source `EtcdSyncDataService`.

Consul data synchronization principle is that the gateway regularly polls Consul's configuration center to get the configuration version number for local comparison.

ShenYu gateway will poll the configured nodes regularly, and the default interval is 1s. When startup, if there is no configuration node in Consul, write the synchronous full amount of data into Consul, then incrementally update the configuration node in Consul when the subsequent data is sent to change. At the same time, Apache ShenYu Gateway will regularly polls the node of configuration information and pull the configuration version number for comparison with the local one. The local cache is updated when the version number is changed.

If you want to learn more about the code implementation, refer to the source `ConsulsyncDataService`.

---

<a id="design-flow-control"></a>

<!-- source_url: https://shenyu.apache.org/docs/design/flow-control/ -->

<!-- page_index: 4 -->

# Flow Control Design

Version: 2.7.0.3

ShenYu gateway realizes flow control through plugins, selectors and rules. For related data structure, please refer to the previous [Apache ShenYu Admin Database Design](#design-database-design) .

In Apache ShenYu Admin System, each plugin uses Handle (JSON format) fields to represent different processing, and the plugin processing is used to manage and edit the custom processing fields in the JSON.

The main purpose of this feature is to enable plugins to handle templated configurations.

Selector and rule are the most soul of Apache ShenYu Gateway. Master it and you can manage any traffic.

A plugin has multiple selectors, and one selector corresponds to multiple rules. The selector is the first level filter of traffic, and the rule is the final filter. For a plugin, we want to meet the traffic criteria based on our configuration before the plugin will be executed. Selectors and rules are designed to allow traffic to perform what we want under certain conditions. The rules need to be understood first.

The execution logic of plugin, selector and rule is as follows. When the traffic enters into ShenYu gateway, it will first judge whether there is a corresponding plugin and whether the plugin is turned on. Then determine whether the traffic matches the selector of the plugin. It then determines whether the traffic matches the rules of the selector. If the request traffic meets the matching criteria, the plugin will be executed. Otherwise, the plugin will not be executed. Process the next one. ShenYu gateway is so through layers of screening to complete the flow control.

![](assets/images/flow-control-en_a3367622666212c7.png)
![](assets/images/flow-condition_b1483a013c442eea.png)

Traffic filtering is the soul of the selector and the rule, corresponding to the matching conditions in the selector and the rule. According to different traffic filtering rules, we can deal with various complex scenes. Traffic filtering can fetch data from Http requests such as `Header`, `URI`, `Query`, `Cookie`, etc.

You can then use `Match`, `=`, `SpEL`, `Regex`, `Groovy`, `Exclude`, etc, to Match the desired data. Multi-group matching Adds matching policies that can use And/Or.

please refer to [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) for details.

---

<a id="design-register-center-design"></a>

<!-- source_url: https://shenyu.apache.org/docs/design/register-center-design/ -->

<!-- page_index: 5 -->

# Client Registry Design

Version: 2.7.0.3

> *Notice*
> After ShenYu version 2.6.1, the ShenYu register just support http type, and the middleware register type has been removed.
> So, please use the http register type to register your service.
> ShenYu Register Center isn't microservice register center, it just register metadata, selector data, rule data to shenyu-admin, and then shenyu-admin will sync data to shenyu-gateway.

Application client access means to access your microservice to ShenYu gateway, currently supports HTTP, Dubbo, Spring Cloud, gRPC, Motan, Sofa, Tars and other protocols access.

Refer to the client access configuration in the user documentation for [Application Client Access Config](#user-guide-property-config-register-center-access) .

![](assets/images/application-client-access-en_b1e7309a03cf2039.png)

![](assets/images/client-8ca2283dbd01d24dfceb32bd0057c8dd_b130122de5b6aed6.png)

Declare the registry client type, such as HTTP, in your microservice configuration. Use SPI to load and initialize the corresponding registry client when the application starts, implement the post-processor interface associated with the Spring Bean, get the service interface information to register in it, and place the obtained information into Disruptor.

The Registry client reads data from the Disruptor and registers the interface information with shenyu-admin, where the Disruptor decouples data from operations for scaling.

![](assets/images/server-11fb112ea24bec622c29ca1224dfee31_d343bdcc2dd6a94a.png)

Declare the registry server type, such as HTTP in the Shenyu-Admin configuration. When shenyu-admin is started, it will read the configuration type, load and initialize the corresponding registry server, and when the registry server receives the interface information registered by shenyu-client, it will put it into Disruptor, which will trigger the registration processing logic to update the interface information and publish a synchronous event.

Disruptor provides data and operations decoupling for expansion. If there are too many registration requests, resulting in abnormal registration, there is also a data buffer role.

The principle of HTTP service registration is relatively simple. After Shenyu-Client is started, the relevant service registration interface of Shenyu-Admin will be called to upload data for registration.

After receiving the request, shenyu-admin will update the data and publish the data synchronization event to synchronize the interface information to ShenYu Gateway.

| *SPI Name* | *Description* |
| --- | --- |
| ShenyuClientRegisterRepository | ShenYu client register SPI |

| *Implementation Class* | *Description* |
| --- | --- |
| HttpClientRegisterRepository | Http client register repository |

| *SPI Name* | *Description* |
| --- | --- |
| ShenyuServerRegisterRepository | ShenYu server register SPI |

| *Implementation Class* | *Description* |
| --- | --- |
| ShenyuHttpRegistryController | Http server repository |

---

<a id="design-spi-design"></a>

<!-- source_url: https://shenyu.apache.org/docs/design/spi-design/ -->

<!-- page_index: 6 -->

# SPI Design

Version: 2.7.0.3

SPI, called Service Provider Interface, is a built-in JDK Service that provides discovery function and a dynamic replacement discovery mechanism.

[shenyu-spi](https://github.com/apache/shenyu/tree/master/shenyu-spi) is a custom SPI extension implementation for Apache Shenyu gateway. The design and implementation principles refer to [SPI Extension Implementations](https://dubbo.apache.org/en/docs/v2.7/dev/impls/) .

`Consul`, `Etcd`, `Http`, `Nacos` and `Zookeeper` are supported. The expansion of the registry including client and server, interface respectively `ShenyuServerRegisterRepository` and `ShenyuClientRegisterRepository`.

Responsible for service monitoring, loading concrete implementation through `SPI`, currently support `Prometheus`, service interface is `MetricsService`.

Select one of the service providers to call. Currently, the supported algorithms are `Has`, `Random`, and `RoundRobin`, and the extended interface is `LoadBalance`.

In the `RateLimiter` plugin, which stream limiting algorithm to use, currently supporting `Concurren`, `LeakyBucke`, `SlidingWindow` and `TokenBucket`, the extension interface is `RateLimiterAlgorithm`.

Which matching method to use when adding selectors And rules, currently supports `And`, `Or`, And the extension interface is `MatchStrategy`.

Currently, `URI`,`RequestMethod`, `Query`, `Post`, `IP`, `Host`, `Cookie`, and `Header` are supported. The extended interface is `ParameterData`.

Which conditional policy to use when adding selectors and rules currently supports `Match`, `Contains`,`Equals`, `Groovy`, `Regex`, `SpEL`, `TimerAfter`, `TimerBefore` and `Exclude`. The extension interface is `PredicateJudge`.

---

<a id="design-wasm-plugin-design"></a>

<!-- source_url: https://shenyu.apache.org/docs/design/wasm-plugin-design/ -->

<!-- page_index: 7 -->

# WASM plugin design

Version: 2.7.0.3

`Apache ShenYu` is a Java native API Gateway for service proxy, protocol conversion and API governance. Currently, ShenYu has good scalability in the Java language. However, ShenYu's support for multiple languages is still relatively weak.

`WASM`(WebAssembly) bytecode is designed to be encoded in a size- and load-time-efficient binary format. WebAssembly aims to leverage the common hardware features available on various platforms to execute in browsers at machine code speed.

`WASI`(WebAssembly System Interface) allows WASM to run in non browser environments such as Linux.

The goal of `WASMPlugin` is to be able to run WASM bytecode. Other languages, as long as their code can be compiled into WASM bytecode (such as Rust/golang/C++), can be used to write ShenYu plugins.

![](assets/images/wasm-plugin-develop_d8ddb1c5f0682eec.png)
![](assets/images/wasm-plugin-prepare_279e6ce67ed8ee9c.png)
![](assets/images/wasm-plugin-runtime_a2316a54da6e5d29.png)

---

<a id="deployment-deployment-before"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-before/ -->

<!-- page_index: 8 -->

# Deployment Prerequisites

Version: 2.7.0.3

This article describes some of the prerequisites you need to prepare before deploying the Apache ShenYu gateway.

Before deploying the `Shenyu-admin` project, initialize the database it uses (databases currently support: Mysql, PostgreSql, Oracle), which used the script files are stored in db directory [project root directory](https://github.com/apache/shenyu/tree/master/db), The following describes the initial steps for each database.

In [the mysql initialization scripts directory](https://github.com/apache/shenyu/tree/master/db/init/mysql) found in the initialization script `schema.sql`, Use the client connection tool to connect to your Mysql service and execute, so you get a database named `shenyu`, which can later be used as the database for the `Shenyu-admin` project.

- sql script: <https://github.com/apache/shenyu/tree/master/db/init/mysql>
- driver:

  - maven repository: <https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.30/>
  - homepage: <https://www.mysql.com/products/connector/>

In [the pg initialization scripts directory](https://github.com/apache/shenyu/tree/master/db/init/pg) found in the initialization script `create-database.sql`、 `create-table.sql`, and use the client connection tool to connect to your PostgreSql service. so you get a database named `shenyu`, which can later be used as a database for the `Shenyu-admin` project.

- sql script: <https://github.com/apache/shenyu/tree/master/db/init/pg>
- driver:

  - maven repository: <https://mvnrepository.com/artifact/org.postgresql/postgresql/42.5.0>
  - homepage: <https://jdbc.postgresql.org/download/>

In [the oracle initialization scripts directory](https://github.com/apache/shenyu/blob/master/db/init/oracle) found in the initialization script `schema.sql`, Use the client connection tool to connect to your Oracle service to create a database, execute the `schema.sql` script on this database, and initialize the `Shenyu-admin` database. After can be [project configuration file](https://github.com/apache/shenyu/blob/master/shenyu-admin/src/main/resources/application-oracle.yml) to adjust your Oracle environment configuration.

- sql script: <https://github.com/apache/shenyu/blob/master/db/init/oracle>
- driver:

  - maven repository: <https://mvnrepository.com/artifact/com.oracle.database.jdbc/ojdbc8/19.3.0.0>
  - homepage: <https://www.oracle.com/database/technologies/appdev/jdbc-downloads.html>

In [the openGuass initialization scripts directory](https://github.com/apache/shenyu/blob/master/db/init/og) found in the initialization script `create-table.sql`, Use the client connection tool to connect to your openGauss service to create a database, execute the `create-table.sql` script on this database, and initialize the `Shenyu-admin` database. After can be [project configuration file](https://github.com/apache/shenyu/blob/master/shenyu-admin/src/main/resources/application-og.yml) to adjust your openGauss environment configuration.

- sql script: <https://github.com/apache/shenyu/blob/master/db/init/og>
- driver:

  - maven repository: <https://mvnrepository.com/artifact/org.opengauss/opengauss-jdbc/5.0.0-og>
  - homepage: <https://gitee.com/opengauss/openGauss-connector-jdbc>

---

<a id="deployment-deployment-local"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-local/ -->

<!-- page_index: 9 -->

# Local Deployment

Version: 2.7.0.3

This article introduces how to start the `Apache ShenYu` gateway in the local environment.

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

- Install JDK1.8+ locally
- Install Git locally
- Install Maven locally
- Choose a development tool, such as IDEA

- Download

```text
git clone https://github.com/apache/shenyu.git 
cd shenyu 
mvn clean install '-Dmaven.javadoc.skip=true' '-B' '-Drat.skip=true' '-Djacoco.skip=true' '-DskipITs' '-DskipTests' 
```

- use the development tool to start `org.apache.shenyu.admin.ShenyuAdminBootstrap`，Visit <http://localhost:9095>, the default username and password are: `admin` and `123456` respectively.

  - If you use `h2` for storage, set the variable `--spring.profiles.active = h2` and start the server.
  - If you use `MySQL` for storage, follow the [guide document](#deployment-deployment-before--mysql) to initialize the database and modify the `JDBC` configuration in `application-mysql.yml`, set the variable `--spring.profiles.active = mysql` and start the server.
  - If you use `PostgreSql` for storage, follow the [guide document](#deployment-deployment-before--postgresql) to initialize the database and modify the `JDBC` configuration in `application-pg.yml`, set the variable `--spring.profiles.active = pg` and start the server.
  - If you use `Oracle` for storage, follow the [guide document](#deployment-deployment-before--oracle) to initialize the database and modify the `JDBC` configuration in `application-oracle.yml`, set the variable `--spring.profiles.active = oracle`.
  - If you use `OpenGuass` for storage, follow the [guide document](#deployment-deployment-before--opengauss) to initialize the database and modify the `JDBC` configuration in `application-og.yml`, set the variable `--spring.profiles.active = og`.
- use the development tool to start `org.apache.shenyu.bootstrap.ShenyuBootstrapApplication`.

---

<a id="deployment-deployment-quick"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-quick/ -->

<!-- page_index: 10 -->

# Local Quick Deployment

Version: 2.7.0.3

This article introduces how to quickly start the `Apache ShenYu` gateway in the standalone environment.

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

- Install JDK1.8+ locally

- download [apache-shenyu-${current.version}-bootstrap-bin.tar.gz](https://archive.apache.org/dist/shenyu/2.6.0/apache-shenyu-2.6.0-bootstrap-bin.tar.gz)
- unzip `apache-shenyu-$\{current.version}-bootstrap-bin.tar.gz`。 go to the `bin` directory.

```text
> windwos : start.bat  
 
> linux : ./start.sh  
```

please refer to [Developer Local Model](#developer-local-model--add-selector-and-rules) add the selector and rule.

example：

- your service address is`http://127.0.0.1:8080/helloworld` and the response like follow:

```json
{ 
  "name" : "Shenyu", 
  "data" : "hello world" 
} 
```

- use the follow data to add selector and rule

> Add `localKey: 123456` to Headers. If you need to customize the localKey, you can use the sha512 tool to generate the key based on plaintext and update the `shenyu.local.sha512Key` property.
>
> `POST` method，address`http://localhost:9195/shenyu/plugin/selectorAndRules`, body use `raw json` content：

```text
Headers 
 
localKey: 123456 
```

```json
{"pluginName": "divide","selectorHandler": "[{\"upstreamUrl\":\"127.0.0.1:8080\"}]","conditionDataList": [{"paramType": "uri","operator": "match","paramValue": "/**" }],"ruleDataList": [{"ruleHandler": "{\"loadBalance\":\"random\"}","conditionDataList": [{"paramType": "uri","operator": "match","paramValue": "/**" }] }]}
```

```bash
curl --location --request POST 'http://localhost:9195/shenyu/plugin/selectorAndRules' \ 
--header 'Content-Type: application/json' \ 
--header 'localKey: 123456' \ 
--data-raw '{ 
    "pluginName": "divide", 
    "selectorHandler": "[{\"upstreamUrl\":\"127.0.0.1:8080\"}]", 
    "conditionDataList": [{ 
        "paramType": "uri", 
        "operator": "match", 
        "paramValue": "/**" 
    }], 
    "ruleDataList": [{ 
        "ruleHandler": "{\"loadBalance\":\"random\"}", 
        "conditionDataList": [{ 
            "paramType": "uri", 
            "operator": "match", 
            "paramValue": "/**" 
        }] 
    }] 
}' 
```

- open `http://localhost:9195/helloworld`:

```json
{ 
  "name" : "Shenyu", 
  "data" : "hello world" 
} 
```

---

<a id="deployment-deployment-package"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-package/ -->

<!-- page_index: 11 -->

# Binary Packages Deployment

Version: 2.7.0.3

This article introduces the deployment of the `Apache ShenYu` gateway using the binary packages.

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

- download [apache-shenyu-${current.version}-admin-bin.tar.gz](https://archive.apache.org/dist/shenyu/2.6.0/apache-shenyu-2.6.0-admin-bin.tar.gz)
- unzip `apache-shenyu-$\{current.version}-admin-bin.tar.gz`。 go to the `bin` directory.

> After version 2.5.1, `start.sh` started to support custom JVM startup parameters through the environment variable `ADMIN_JVM`.

- use `h2` to store data  ：

```text
> windows: start.bat 
 
> linux: ./start.sh 
```

- use `MySQL` to store data, follow the [guide document](#deployment-deployment-before--mysql) to initialize the database, copy [mysql-connector.jar](https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.18/mysql-connector-java-8.0.18.jar) to /$(your\_work\_dir)/ext-lib, go to the `/conf` directory, and modify the `JDBC` configuration in `application-mysql.yml`.
- Modify `spring.profiles.active` in `conf/application.yml` to `mysql`

```text
> windows: start.bat 
 
> linux: ./start.sh 
```

- use `PostgreSql` to store data, follow the [guide document](#deployment-deployment-before--postgresql) to initialize the database, go to the `/conf` directory, and modify the `JDBC` configuration in `application-pg.yml`.
- Modify `spring.profiles.active` in `conf/application.yml` to `pg`

```text
> windows: start.bat 
 
> linux: ./start.sh --spring.profiles.active = pg 
```

- use `Oracle` to store data, follow the [guide document](#deployment-deployment-before--oracle) to initialize the database, go to the `/conf` directory, and modify the `JDBC` configuration in `application-oracle.yml`.
- Modify `spring.profiles.active` in `conf/application.yml` to `oracle`

```text
> windows: start.bat 
 
> linux: ./start.sh 
```

- use `OpenGauss` to store data, follow the [guide document](#deployment-deployment-before--opengauss) to initialize the database, go to the `/conf` directory, and modify the `JDBC` configuration in `application-og.yml`.
- Modify `spring.profiles.active` in `conf/application.yml` to `og`

```text
> windows: start.bat 
 
> linux: ./start.sh 
```

- download [apache-shenyu-${current.version}-bootstrap-bin.tar.gz](https://archive.apache.org/dist/shenyu/2.6.0/apache-shenyu-2.6.0-bootstrap-bin.tar.gz)
- unzip `apache-shenyu-$\{current.version}-bootstrap-bin.tar.gz`。 go to the `bin` directory.

> After version 2.5.1, `start.sh` started to support custom JVM startup parameters through the environment variable `BOOT_JVM`.

```text
> windwos : start.bat  
 
> linux : ./start.sh  
```

---

<a id="deployment-deployment-docker-compose"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-docker-compose/ -->

<!-- page_index: 12 -->

# Docker-compose Deployment

Version: 2.7.0.3

This article introduces the use of `docker-compose` to deploy the `Apache ShenYu` gateway.

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

```shell
curl -O https://raw.githubusercontent.com/apache/shenyu/master/shenyu-dist/shenyu-docker-compose-dist/src/main/resources/install.sh 
```

This script will download the required configuration files and mysql-connector, and can be executed repeatedly if the download fails.

```shell
sh ./install.sh #The latest configuration is pulled by default. If you need to deploy the released version, you can add a parameter to indicate the version number, such as: v2.4.2 or latest 
```

Refer to the [database initialization documentation](#deployment-deployment-before--database-initialize) to initialize the database.

Modify the configuration file downloaded by the script to set up configurations such as `JDBC`.

```shell
cd shenyu-${VERSION} 
docker-compose -f ./shenyu-${VERSION}/docker-compose.yaml up -d 
```

---

<a id="deployment-deployment-docker"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-docker/ -->

<!-- page_index: 13 -->

# Docker Deployment

Version: 2.7.0.3

This article introduces the use of `docker` to deploy the `Apache ShenYu` gateway.

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

```text
docker network create shenyu 
```

```text
docker pull apache/shenyu-admin:${current.version} 
```

> After version 2.5.1, when `docker run`, we can customize JVM startup parameters by adding `-e ADMIN_JVM="xxxx"`

- use `h2` to store data:

```text
docker run -d -p 9095:9095 --name shenyu-admin --net shenyu apache/shenyu-admin:${current.version} 
```

- use `MySQL` to store data, follow the [guide document](#deployment-deployment-before--mysql) to initialize the database, copy [mysql-connector.jar](https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.29/mysql-connector-java-8.0.29.jar) to `/$(your_work_dir)/ext-lib`：

```text
docker run --name shenyu-admin -v /${your_work_dir}/ext-lib:/opt/shenyu-admin/ext-lib -e "SPRING_PROFILES_ACTIVE=mysql" -e "spring.datasource.url=jdbc:mysql://${your_ip_port}/shenyu?useUnicode=true&characterEncoding=utf-8&useSSL=false&serverTimezone=Asia/Shanghai&zeroDateTimeBehavior=convertToNull" -e "spring.datasource.username=${your_username}" -e "spring.datasource.password=${your_password}" -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

another way is to put the `application.yml`、`application-mysql.yml` configuration in ${your\_work\_dir}/conf from [Configure address](https://github.com/apache/shenyu/blob/master/shenyu-admin/src/main/resources/) , modify the configuration `spring.profiles.active = mysql` in `application.yml`, and then execute the following statement：

```text
docker run --name shenyu-admin -v ${your_work_dir}/conf:/opt/shenyu-admin/conf -v /${your_work_dir}/ext-lib:/opt/shenyu-admin/ext-lib -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

- use `PostgreSql` to store data, follow the [guide document](#deployment-deployment-before--postgresql) to initialize the database, execute the following statement：

```text
docker run --name shenyu-admin -e "SPRING_PROFILES_ACTIVE=pg" -e "spring.datasource.url=jdbc:postgresql://${your_ip_port}/shenyu?useUnicode=true&characterEncoding=utf-8&useSSL=false" -e "spring.datasource.username=${your_username}" -e "spring.datasource.password=${your_password}" -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

another way is to put the `application.yml`、`application-pg.yml` configuration in ${your\_work\_dir}/conf, modify the configuration `spring.profiles.active = pg` in `application.yml`,and then execute the following statement：

```text
docker run --name shenyu-admin -v ${your_work_dir}/conf:/opt/shenyu-admin/conf -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

- use `Oracle` to store data, follow the [guide document](#deployment-deployment-before--oracle) to initialize the database, execute the following statement：

```text
docker run --name shenyu-admin -e "SPRING_PROFILES_ACTIVE=oracle" -e "spring.datasource.url=jdbc:oracle:thin:@localhost:1521/shenyu" -e "spring.datasource.username=${your_username}" -e "spring.datasource.password=${your_password}" -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

another way is to put the `application.yml`、`application-oracle.yml` configuration in ${your\_work\_dir}/conf, modify the configuration `spring.profiles.active = oracle` in `application.yml`, and then execute the following statement：

```text
docker run --name shenyu-admin -v ${your_work_dir}/conf:/opt/shenyu-admin/conf -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

- use `OpenGauss` to store data, follow the [guide document](#deployment-deployment-before--opengauss) to initialize the database, execute the following statement：

```text
docker run --name shenyu-admin -e "SPRING_PROFILES_ACTIVE=og" -e "spring.datasource.url=jdbc:opengauss://localhost:5432/shenyu" -e "spring.datasource.username=${your_username}" -e "spring.datasource.password=${your_password}" -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

another way is to put the `application.yml`、`application-og.yml` configuration in ${your\_work\_dir}/conf, modify the configuration `spring.profiles.active = og` in `application.yml`, and then execute the following statement：

```text
docker run --name shenyu-admin -v ${your_work_dir}/conf:/opt/shenyu-admin/conf -d -p 9095:9095 --net shenyu apache/shenyu-admin:${current.version} 
```

> After version 2.5.1, when `docker run`, we can customize JVM startup parameters by adding `-e BOOT_JVM="xxxx"`

First, pull the docker image

```shell
docker pull apache/shenyu-bootstrap:${current.version} 
```

If you don't need to modify the configuration, just use the command below to run the application

```shell
docker run -d \ 
  -p 9195:9195 \ 
  --name shenyu-bootstrap \ 
  --net shenyu \ 
  --env SHENYU_SYNC_WEBSOCKET_URLS=ws://shenyu-admin:9095/websocket \ 
  apache/shenyu-bootstrap:${current.version} 
```

> `SHENYU_SYNC_WEBSOCKET_URLS` indicates the websocket address that shenyu-bootstrap used to communicate with shenyu-admin

If you need to modify the configuration, copy the configuration from the Github directory where the bootstrap [configuration file](https://github.com/apache/shenyu/tree/master/shenyu-bootstrap/src/main/resources) is located, then recorded it as `$BOOTSTRAP_CONF`. After your modification, execute the command below to run the application

```shell
docker run -d \ 
  -p 9195:9195 \ 
  -v $BOOTSTRAP_CONF:/opt/shenyu-bootstrap/conf \ 
  --name shenyu-bootstrap \ 
  --net shenyu \ 
  --env SHENYU_SYNC_WEBSOCKET_URLS=ws://shenyu-admin:9095/websocket \ 
  apache/shenyu-bootstrap:${current.version} 
```

---

<a id="deployment-deployment-k8s"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-k8s/ -->

<!-- page_index: 14 -->

# K8s Deployment

Version: 2.7.0.3

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

This article introduces the use of `K8s` to deploy the `Apache ShenYu` gateway.

> Catalog
>
> Example 1: Using h2 as a database
>
> 1. create Namespace and ConfigMap
> 2. deploying shenyu-admin
> 3. deploy shenyu-bootstrap
>
> Example 2: Use MySQL as the database
>
> Similar to the h2 process, there are two points to note
>
> 1. you need to load [mysql-connector.jar](https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.18/mysql-connector-java-8.0.18.jar), the download command is executed when the container is started
> 2. you need to specify an external MySQL database configuration
>
> The process is as follows.
>
> 1. create Namespace and ConfigMap
> 2. deploy shenyu-admin
> 3. deploy shenyu-bootstrap

- create shenyu-ns.yaml

```yaml
apiVersion: v1 
kind: Namespace 
metadata: 
  name: shenyu 
  labels: 
    name: shenyu 
--- 
apiVersion: v1 
kind: ConfigMap 
metadata: 
  name: shenyu-cm 
  namespace: shenyu 
data: 
  shenyu-admin-application.yml: | 
    server: 
      port: 9095 
      address: 0.0.0.0 
    spring: 
      profiles: 
        active: h2 
      thymeleaf: 
        cache: true 
        encoding: utf-8 
        enabled: true 
        prefix: classpath:/static/ 
        suffix: .html 
      mvc: 
        pathmatch: 
          matching-strategy: ant_path_matcher 
    mybatis: 
      config-location: classpath:/mybatis/mybatis-config.xml 
      mapper-locations: classpath:/mappers/*.xml 
    shenyu: 
      register: 
        registerType: http #http #zookeeper #etcd #nacos #consul 
        serverLists: #localhost:2181 #http://localhost:2379 #localhost:8848 
        props: 
          sessionTimeout: 5000 
          connectionTimeout: 2000 
          checked: true 
          zombieCheckTimes: 5 
          scheduledTime: 10 
          nacosNameSpace: ShenyuRegisterCenter 
      sync: 
        websocket: 
          enabled: true 
          messageMaxSize: 10240 
          allowOrigins: ws://shenyu-admin-svc.shenyu.svc.cluster.local:9095;ws://shenyu-bootstrap-svc.shenyu.svc.cluster.local:9195; 
      ldap: 
        enabled: false 
        url: ldap://xxxx:xxx 
        bind-dn: cn=xxx,dc=xxx,dc=xxx 
        password: xxxx 
        base-dn: ou=xxx,dc=xxx,dc=xxx 
        object-class: person 
        login-field: cn 
      jwt: 
        expired-seconds: 86400000 
      shiro: 
        white-list: 
          - / 
          - /favicon.* 
          - /static/** 
          - /index** 
          - /platform/login 
          - /websocket 
          - /error 
          - /actuator/health 
          - /swagger-ui.html 
          - /webjars/** 
          - /swagger-resources/** 
          - /v2/api-docs 
          - /csrf 
      swagger: 
        enable: true 
      apidoc: 
        gatewayUrl: http://127.0.0.1:9195 
        envProps: 
          - envLabel: Test environment 
            addressLabel: Request Address 
            addressUrl: http://127.0.0.1:9195 
          - envLabel: Prod environment 
            addressLabel: Request Address 
            addressUrl: http://127.0.0.1:9195 
    logging: 
      level: 
        root: info 
        org.springframework.boot: info 
        org.apache.ibatis: info 
        org.apache.shenyu.bonuspoint: info 
        org.apache.shenyu.lottery: info 
        org.apache.shenyu: info 
  shenyu-admin-application-h2.yml: | 
    shenyu: 
      database: 
        dialect: h2 
        init_script: "sql-script/h2/schema.sql" 
        init_enable: true 
    spring: 
      datasource: 
        url: jdbc:h2:mem:~/shenyu;DB_CLOSE_DELAY=-1;MODE=MySQL; 
        username: sa 
        password: sa 
        driver-class-name: org.h2.Driver 
  shenyu-bootstrap-application.yml: | 
    server: 
      port: 9195 
      address: 0.0.0.0 
    spring: 
      main: 
        allow-bean-definition-overriding: true 
        allow-circular-references: true 
      application: 
        name: shenyu-bootstrap 
      codec: 
        max-in-memory-size: 2MB 
      cloud: 
        discovery: 
          enabled: false 
        nacos: 
          discovery: 
            server-addr: 127.0.0.1:8848 # Spring Cloud Alibaba Dubbo use this. 
            enabled: false 
            namespace: ShenyuRegisterCenter 
    eureka: 
      client: 
        enabled: false 
        serviceUrl: 
          defaultZone: http://localhost:8761/eureka/ 
      instance: 
        prefer-ip-address: true 
    management: 
      health: 
        defaults: 
          enabled: false 
    shenyu: 
      matchCache: 
        selector: 
          selectorEnabled: false 
          initialCapacity: 10000 # initial capacity in cache 
          maximumSize: 10000 # max size in cache 
        rule: 
          initialCapacity: 10000 # initial capacity in cache 
          maximumSize: 10000 # max size in cache 
      trie: 
        childrenSize: 10000 
        pathVariableSize: 1000 
        pathRuleCacheSize: 1000 
        matchMode: antPathMatch 
      netty: 
        http: 
          # set to false, user can custom the netty tcp server config. 
          webServerFactoryEnabled: true 
          selectCount: 1 
          workerCount: 4 
          accessLog: false 
          serverSocketChannel: 
            soRcvBuf: 87380 
            soBackLog: 128 
            soReuseAddr: false 
            connectTimeoutMillis: 10000 
            writeBufferHighWaterMark: 65536 
            writeBufferLowWaterMark: 32768 
            writeSpinCount: 16 
            autoRead: false 
            allocType: "pooled" 
            messageSizeEstimator: 8 
            singleEventExecutorPerGroup: true 
          socketChannel: 
            soKeepAlive: false 
            soReuseAddr: false 
            soLinger: -1 
            tcpNoDelay: true 
            soRcvBuf: 87380 
            soSndBuf: 16384 
            ipTos: 0 
            allowHalfClosure: false 
            connectTimeoutMillis: 10000 
            writeBufferHighWaterMark: 65536 
            writeBufferLowWaterMark: 32768 
            writeSpinCount: 16 
            autoRead: false 
            allocType: "pooled" 
            messageSizeEstimator: 8 
            singleEventExecutorPerGroup: true 
      instance: 
        enabled: false 
        registerType: zookeeper #etcd #consul 
        serverLists: localhost:2181 #http://localhost:2379 #localhost:8848 
        props: 
      cross: 
        enabled: true 
        allowedHeaders: 
        allowedMethods: "*" 
        allowedAnyOrigin: true # the same of Access-Control-Allow-Origin: "*" 
        allowedExpose: "" 
        maxAge: "18000" 
        allowCredentials: true 
      switchConfig: 
        local: true 
      file: 
        enabled: true 
        maxSize : 10 
      sync: 
        websocket: 
          urls: ws://shenyu-admin-svc.shenyu.svc.cluster.local:9095/websocket 
          allowOrigin: ws://shenyu-bootstrap-svc.shenyu.svc.cluster.local:9195 
      exclude: 
        enabled: false 
        paths: 
          - /favicon.ico 
      fallback: 
        enabled: false 
        paths: 
          - /fallback/hystrix 
          - /fallback/resilience4j 
      health: 
        enabled: false 
        paths: 
          - /actuator/health 
          - /health_check 
      extPlugin: 
        path: 
        enabled: true 
        threads: 1 
        scheduleTime: 300 
        scheduleDelay: 30 
      scheduler: 
        enabled: false 
        type: fixed 
        threads: 16 
      upstreamCheck: 
        enabled: false 
        timeout: 3000 
        healthyThreshold: 1 
        unhealthyThreshold: 1 
        interval: 5000 
        printEnabled: true 
        printInterval: 60000 
      ribbon: 
        serverListRefreshInterval: 10000 
      metrics: 
        enabled: false 
        name : prometheus 
        host: 127.0.0.1 
        port: 8090 
        jmxConfig: 
        props: 
          jvm_enabled: true 
      local: 
        enabled: false 
        sha512Key: "BA3253876AED6BC22D4A6FF53D8406C6AD864195ED144AB5C87621B6C233B548BAEAE6956DF346EC8C17F5EA10F35EE3CBC514797ED7DDD3145464E2A0BAB413" 
    logging: 
      level: 
        root: info 
        org.springframework.boot: info 
        org.apache.ibatis: info 
        org.apache.shenyu.bonuspoint: info 
        org.apache.shenyu.lottery: info 
        org.apache.shenyu: info 
 
```

- execute `kubectl apply -f shenyu-ns.yaml`

- create shenyu-admin.yaml

```yaml
# Example of using the nodeport type to expose ports 
apiVersion: v1 
kind: Service 
metadata: 
  namespace: shenyu 
  name: shenyu-admin-svc 
spec: 
  selector: 
    app: shenyu-admin 
  type: NodePort 
  ports: 
  - protocol: TCP 
    port: 9095 
    targetPort: 9095 
    nodePort: 31095 
--- 
# shenyu-admin 
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  namespace: shenyu 
  name: shenyu-admin 
spec: 
  selector: 
    matchLabels: 
      app: shenyu-admin 
  replicas: 1 
  template: 
    metadata: 
      labels: 
        app: shenyu-admin 
    spec: 
      volumes: 
      - name: shenyu-admin-application 
        configMap: 
          name: shenyu-cm 
          items: 
          - key: shenyu-admin-application.yml 
            path: shenyu-admin-application.yml 
      - name: shenyu-admin-application-h2 
        configMap: 
          name: shenyu-cm 
          items: 
          - key: shenyu-admin-application-h2.yml 
            path: shenyu-admin-application-h2.yml 
      containers: 
      - name: shenyu-admin 
        image: apache/shenyu-admin:latest 
        imagePullPolicy: Always 
        ports: 
        - containerPort: 9095 
        env: 
        - name: 'TZ' 
          value: 'Asia/Beijing' 
        volumeMounts: 
        - name: shenyu-admin-application 
          mountPath: /opt/shenyu-admin/conf/application.yml 
          subPath: shenyu-admin-application.yml 
        - name: shenyu-admin-application-h2 
          mountPath: /opt/shenyu-admin/conf/application-h2.yml 
          subPath: shenyu-admin-application-h2.yml 
```

- execute`kubectl apply -f shenyu-admin.yaml`

- create shenyu-bootstrap.yaml

```yaml
# Example of using the nodeport type to expose ports 
apiVersion: v1 
kind: Service 
metadata: 
  namespace: shenyu 
  name: shenyu-bootstrap-svc 
spec: 
  selector: 
    app: shenyu-bootstrap 
  type: NodePort 
  ports: 
  - protocol: TCP 
    port: 9195 
    targetPort: 9195 
    nodePort: 31195 
--- 
# shenyu-bootstrap 
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  namespace: shenyu 
  name: shenyu-bootstrap 
spec: 
  selector: 
    matchLabels: 
      app: shenyu-bootstrap 
  replicas: 1 
  template: 
    metadata: 
      labels: 
        app: shenyu-bootstrap 
    spec: 
      volumes: 
      - name: shenyu-bootstrap-application 
        configMap: 
          name: shenyu-cm 
          items: 
          - key: shenyu-bootstrap-application.yml 
            path: shenyu-bootstrap-application.yml 
      containers: 
      - name: shenyu-bootstrap 
        image: apache/shenyu-bootstrap:latest 
        ports: 
        - containerPort: 9195 
        env: 
        - name: TZ 
          value: Asia/Beijing 
        volumeMounts: 
        - name: shenyu-bootstrap-application 
          mountPath: /opt/shenyu-bootstrap/conf/application.yml 
          subPath: shenyu-bootstrap-application.yml 
```

- execute `kubectl apply -f shenyu-bootstrap.yaml`

- create shenyu-ns.yaml

```yaml
apiVersion: v1 
kind: Namespace 
metadata: 
  name: shenyu 
  labels: 
    name: shenyu 
--- 
apiVersion: v1 
kind: ConfigMap 
metadata: 
  name: shenyu-cm 
  namespace: shenyu 
data: 
  shenyu-admin-application.yml: | 
    server: 
      port: 9095 
      address: 0.0.0.0 
    spring: 
      profiles: 
        active: mysql 
      thymeleaf: 
        cache: true 
        encoding: utf-8 
        enabled: true 
        prefix: classpath:/static/ 
        suffix: .html 
      mvc: 
        pathmatch: 
          matching-strategy: ant_path_matcher 
    mybatis: 
      config-location: classpath:/mybatis/mybatis-config.xml 
      mapper-locations: classpath:/mappers/*.xml 
    shenyu: 
      register: 
        registerType: http #http #zookeeper #etcd #nacos #consul 
        serverLists: #localhost:2181 #http://localhost:2379 #localhost:8848 
        props: 
          sessionTimeout: 5000 
          connectionTimeout: 2000 
          checked: true 
          zombieCheckTimes: 5 
          scheduledTime: 10 
          nacosNameSpace: ShenyuRegisterCenter 
      sync: 
        websocket: 
          enabled: true 
          messageMaxSize: 10240 
          allowOrigins: ws://shenyu-admin-svc.shenyu.svc.cluster.local:9095;ws://shenyu-bootstrap-svc.shenyu.svc.cluster.local:9195; 
      ldap: 
        enabled: false 
        url: ldap://xxxx:xxx 
        bind-dn: cn=xxx,dc=xxx,dc=xxx 
        password: xxxx 
        base-dn: ou=xxx,dc=xxx,dc=xxx 
        object-class: person 
        login-field: cn 
      jwt: 
        expired-seconds: 86400000 
      shiro: 
        white-list: 
          - / 
          - /favicon.* 
          - /static/** 
          - /index** 
          - /platform/login 
          - /websocket 
          - /error 
          - /actuator/health 
          - /swagger-ui.html 
          - /webjars/** 
          - /swagger-resources/** 
          - /v2/api-docs 
          - /csrf 
      swagger: 
        enable: true 
      apidoc: 
        gatewayUrl: http://127.0.0.1:9195 
        envProps: 
          - envLabel: Test environment 
            addressLabel: Request Address 
            addressUrl: http://127.0.0.1:9195 
          - envLabel: Prod environment 
            addressLabel: Request Address 
            addressUrl: http://127.0.0.1:9195 
    logging: 
      level: 
        root: info 
        org.springframework.boot: info 
        org.apache.ibatis: info 
        org.apache.shenyu.bonuspoint: info 
        org.apache.shenyu.lottery: info 
        org.apache.shenyu: info 
  shenyu-admin-application-mysql.yml: | 
    shenyu: 
      database: 
        dialect: mysql 
        init_script: "sql-script/mysql/schema.sql" 
        init_enable: true 
    spring: 
      datasource: 
        url: jdbc:mysql://{your_mysql_ip}:{your_mysql_port}/shenyu?useUnicode=true&characterEncoding=utf-8&useSSL=false 
        username: {your_mysql_user} 
        password: {your_mysql_password} 
        driver-class-name: com.mysql.jdbc.Driver 
  shenyu-bootstrap-application.yml: | 
    server: 
      port: 9195 
      address: 0.0.0.0 
    spring: 
      main: 
        allow-bean-definition-overriding: true 
        allow-circular-references: true 
      application: 
        name: shenyu-bootstrap 
      codec: 
        max-in-memory-size: 2MB 
      cloud: 
        discovery: 
          enabled: false 
        nacos: 
          discovery: 
            server-addr: 127.0.0.1:8848 # Spring Cloud Alibaba Dubbo use this. 
            enabled: false 
            namespace: ShenyuRegisterCenter 
    eureka: 
      client: 
        enabled: false 
        serviceUrl: 
          defaultZone: http://localhost:8761/eureka/ 
      instance: 
        prefer-ip-address: true 
    management: 
      health: 
        defaults: 
          enabled: false 
    shenyu: 
      matchCache: 
        selector: 
          selectorEnabled: false 
          initialCapacity: 10000 # initial capacity in cache 
          maximumSize: 10000 # max size in cache 
        rule: 
          initialCapacity: 10000 # initial capacity in cache 
          maximumSize: 10000 # max size in cache 
      trie: 
        childrenSize: 10000 
        pathVariableSize: 1000 
        pathRuleCacheSize: 1000 
        matchMode: antPathMatch 
      netty: 
        http: 
          # set to false, user can custom the netty tcp server config. 
          webServerFactoryEnabled: true 
          selectCount: 1 
          workerCount: 4 
          accessLog: false 
          serverSocketChannel: 
            soRcvBuf: 87380 
            soBackLog: 128 
            soReuseAddr: false 
            connectTimeoutMillis: 10000 
            writeBufferHighWaterMark: 65536 
            writeBufferLowWaterMark: 32768 
            writeSpinCount: 16 
            autoRead: false 
            allocType: "pooled" 
            messageSizeEstimator: 8 
            singleEventExecutorPerGroup: true 
          socketChannel: 
            soKeepAlive: false 
            soReuseAddr: false 
            soLinger: -1 
            tcpNoDelay: true 
            soRcvBuf: 87380 
            soSndBuf: 16384 
            ipTos: 0 
            allowHalfClosure: false 
            connectTimeoutMillis: 10000 
            writeBufferHighWaterMark: 65536 
            writeBufferLowWaterMark: 32768 
            writeSpinCount: 16 
            autoRead: false 
            allocType: "pooled" 
            messageSizeEstimator: 8 
            singleEventExecutorPerGroup: true 
      instance: 
        enabled: false 
        registerType: zookeeper #etcd #consul 
        serverLists: localhost:2181 #http://localhost:2379 #localhost:8848 
        props: 
      cross: 
        enabled: true 
        allowedHeaders: 
        allowedMethods: "*" 
        allowedAnyOrigin: true # the same of Access-Control-Allow-Origin: "*" 
        allowedExpose: "" 
        maxAge: "18000" 
        allowCredentials: true 
      switchConfig: 
        local: true 
      file: 
        enabled: true 
        maxSize : 10 
      sync: 
        websocket: 
          urls: ws://shenyu-admin-svc.shenyu.svc.cluster.local:9095/websocket 
          allowOrigin: ws://shenyu-bootstrap-svc.shenyu.svc.cluster.local:9195 
      exclude: 
        enabled: false 
        paths: 
          - /favicon.ico 
      fallback: 
        enabled: false 
        paths: 
          - /fallback/hystrix 
          - /fallback/resilience4j 
      health: 
        enabled: false 
        paths: 
          - /actuator/health 
          - /health_check 
      extPlugin: 
        path: 
        enabled: true 
        threads: 1 
        scheduleTime: 300 
        scheduleDelay: 30 
      scheduler: 
        enabled: false 
        type: fixed 
        threads: 16 
      upstreamCheck: 
        enabled: false 
        timeout: 3000 
        healthyThreshold: 1 
        unhealthyThreshold: 1 
        interval: 5000 
        printEnabled: true 
        printInterval: 60000 
      ribbon: 
        serverListRefreshInterval: 10000 
      metrics: 
        enabled: false 
        name : prometheus 
        host: 127.0.0.1 
        port: 8090 
        jmxConfig: 
        props: 
          jvm_enabled: true 
      local: 
        enabled: false 
        sha512Key: "BA3253876AED6BC22D4A6FF53D8406C6AD864195ED144AB5C87621B6C233B548BAEAE6956DF346EC8C17F5EA10F35EE3CBC514797ED7DDD3145464E2A0BAB413" 
    logging: 
      level: 
        root: info 
        org.springframework.boot: info 
        org.apache.ibatis: info 
        org.apache.shenyu.bonuspoint: info 
        org.apache.shenyu.lottery: info 
        org.apache.shenyu: info 
```

- execute `kubectl apply -f shenyu-ns.yaml`

- create shenyu-admin.yaml

```yaml
# Example of using the nodeport type to expose ports 
apiVersion: v1 
kind: Service 
metadata: 
  namespace: shenyu 
  name: shenyu-admin-svc 
spec: 
  selector: 
    app: shenyu-admin 
  type: NodePort 
  ports: 
  - protocol: TCP 
    port: 9095 
    targetPort: 9095 
    nodePort: 31095 
--- 
# shenyu-admin 
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  namespace: shenyu 
  name: shenyu-admin 
spec: 
  selector: 
    matchLabels: 
      app: shenyu-admin 
  replicas: 1 
  template: 
    metadata: 
      labels: 
        app: shenyu-admin 
    spec: 
      volumes: 
      - name: shenyu-admin-application 
        configMap: 
          name: shenyu-cm 
          items: 
          - key: shenyu-admin-application.yml 
            path: shenyu-admin-application.yml 
      - name: shenyu-admin-application-mysql 
        configMap: 
          name: shenyu-cm 
          items: 
          - key: shenyu-admin-application-mysql.yml 
            path: shenyu-admin-application-mysql.yml 
      - name: mysql-connector-volume 
        emptyDir: {} 
      initContainers: 
      - name: download-mysql-jar 
        image: busybox:1.35.0 
        command: [ "sh","-c"] 
        args: ["wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar; 
            wget https://repo1.maven.org/maven2/mysql/mysql-connector-java/8.0.23/mysql-connector-java-8.0.23.jar.md5; 
            if [ $(md5sum mysql-connector-java-8.0.23.jar | cut -d ' ' -f1) = $(cat mysql-connector-java-8.0.23.jar.md5) ]; 
            then echo success; 
            else echo failed; 
            exit 1; 
            fi; 
            mv /mysql-connector-java-8.0.23.jar /opt/shenyu-admin/ext-lib/mysql-connector-java.jar" ] 
        volumeMounts: 
        - name: mysql-connector-volume 
          mountPath: /opt/shenyu-admin/ext-lib 
      containers: 
      - name: shenyu-admin 
        image: apache/shenyu-admin:latest 
        imagePullPolicy: Always 
        ports: 
        - containerPort: 9095 
        env: 
        - name: 'TZ' 
          value: 'Asia/Beijing' 
        - name: SPRING_PROFILES_ACTIVE 
          value: mysql 
        volumeMounts: 
        - name: shenyu-admin-application 
          mountPath: /opt/shenyu-admin/conf/application.yml 
          subPath: shenyu-admin-application.yml 
        - name: shenyu-admin-application-mysql 
          mountPath: /opt/shenyu-admin/conf/application-mysql.yml 
          subPath: shenyu-admin-application-mysql.yml 
        - name: mysql-connector-volume 
          mountPath: /opt/shenyu-admin/ext-lib 
```

- execute`kubectl apply -f shenyu-admin.yaml`

- create shenyu-bootstrap.yaml

```yaml
# Example of using the nodeport type to expose ports 
apiVersion: v1 
kind: Service 
metadata: 
  namespace: shenyu 
  name: shenyu-bootstrap-svc 
spec: 
  selector: 
    app: shenyu-bootstrap 
  type: NodePort 
  ports: 
    - protocol: TCP 
      port: 9195 
      targetPort: 9195 
      nodePort: 31195 
--- 
# shenyu-bootstrap 
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  namespace: shenyu 
  name: shenyu-bootstrap 
spec: 
  selector: 
    matchLabels: 
      app: shenyu-bootstrap 
  replicas: 1 
  template: 
    metadata: 
      labels: 
        app: shenyu-bootstrap 
    spec: 
      volumes: 
        - name: shenyu-bootstrap-application 
          configMap: 
            name: shenyu-cm 
            items: 
              - key: shenyu-bootstrap-application.yml 
                path: shenyu-bootstrap-application.yml 
      containers: 
        - name: shenyu-bootstrap 
          image: apache/shenyu-bootstrap:latest 
          ports: 
            - containerPort: 9195 
          env: 
            - name: TZ 
              value: Asia/Beijing 
          volumeMounts: 
            - name: shenyu-bootstrap-application 
              mountPath: /opt/shenyu-bootstrap/conf/application.yml 
              subPath: shenyu-bootstrap-application.yml 
```

- execute `kubectl apply -f shenyu-bootstrap.yaml`

**Access Address**：http://{K8S\_CLUSTER\_IP}:31095/

**Account/password**：admin/123456

---

<a id="deployment-deployment-helm"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-helm/ -->

<!-- page_index: 15 -->

# Helm Deployment

Version: 2.7.0.3

This article introduces the use of `helm` to deploy the `Apache ShenYu` gateway.

Please refer to [Helm Deployment](https://shenyu.apache.org/helm/index/) for details.

---

<a id="deployment-deployment-aapanel"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-aapanel/ -->

<!-- page_index: 16 -->

# aaPanel Deployment

Version: 2.7.0.3

This article introduces the use of `aaPanel` to deploy the `Apache ShenYu` gateway.

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

To install aaPanel, go to the [aaPanel](https://www.aapanel.com/new/download.html#install) official website and select the corresponding script to download and install.

aaPanel(Applicable versions 7.0.11 and above) Deployment guidelines

1. Log in to aaPanel and click `Docker` in the menu bar
   ![Docker](assets/images/install-9ac763067ca7a439ced7db9af9eff97b_08f0cbba1f3851e8.png)
2. The first time you will be prompted to install the `Docker` and `Docker Compose` services, click Install Now. If it is already installed, please ignore it.
   ![install](assets/images/install2-f558fbacfaf22438b00b70402b96452e_237b2731d4223fae.png)
3. After the installation is complete, find `ShenYu` in `One-Click Install` and click `install`

   ![install_HertzBeat](assets/images/install-shenyu-79c4f9cbe0b9515492cd51ae535997dd_545e7b0ed6b149a8.png)
4. Set the basic information such as domain name and click 'OK'

   ![add](assets/images/addshenyu-72bdfc7ac05a612705de787919c91b2f_cb12946fd574e372.png)

- Name: application name, default `ShenYu-random characters`
- Version selection: default `latest`
- Domain name: If you need to access directly through the domain name, please configure the domain name here and resolve the domain name to the server
- Allow external access: If you need direct access through `IP+Port`, please check. If you have set up a domain name, please do not check here.
- Port: Web management port `9095`, can be modified by yourself

After submission, the panel will automatically initialize the application, which will take about `1-3` minutes. It can be accessed after the initialization is completed.

- If you have set a domain name, please directly enter the domain name in the browser address bar, such as `http://demo.ShenYu.apache.org`, to access the `LobeChat`ShenYu console.
- If you choose to access through `IP+Port`, please enter the domain name in the browser address bar to access `http://<aaPanelIP>:9095` to access the `ShenYu` console.
  ![console](assets/images/console-88073601555d68c43476b513379aabba_2b7a4427db298f69.png)

---

<a id="deployment-deployment-custom"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-custom/ -->

<!-- page_index: 17 -->

# Custom Deployment

Version: 2.7.0.3

This article describes how to build your own gateway based on `Apache ShenYu`.

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

- docker reference docker deployment Apache ShenYu Admin
- liunx/windows reference binary packages deployment Apache ShenYu Admin

- first create an empty `springboot` project, you can refer to `shenyu-bootstrap`, or you can create it on [spring official website](https://spring.io/quickstart).
- introduce the following `jar` package:

```xml
<dependencies> 
   <dependency> 
        <groupId>org.springframework.boot</groupId> 
        <artifactId>spring-boot-starter-webflux</artifactId> 
        <version>2.2.2.RELEASE</version> 
   </dependency> 
    <dependency> 
        <groupId>org.springframework.boot</groupId> 
        <artifactId>spring-boot-starter-actuator</artifactId> 
        <version>2.2.2.RELEASE</version> 
   </dependency> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-gateway</artifactId> 
        <version>${current.version}</version> 
   </dependency> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sync-data-websocket</artifactId> 
        <version>${current.version}</version> 
   </dependency> 
</dependencies> 
```

among them, `${project.version}` please use the current latest version.

- add the following configuration to your `application.yaml` file:

```yaml
spring: 
  main: 
    allow-bean-definition-overriding: true 
management: 
  health: 
    defaults: 
      enabled: false 
shenyu: 
  sync: 
    websocket: 
      urls: ws://localhost:9095/websocket  //set to your shenyu-admin address 
      allowOrigin: ws://localhost:9195 
```

---

<a id="deployment-deployment-cluster"></a>

<!-- source_url: https://shenyu.apache.org/docs/deployment/deployment-cluster/ -->

<!-- page_index: 18 -->

# Cluster Deployment

Version: 2.7.0.3

> Before you read this document, you need to complete some preparations before deploying Shenyu according to the [Deployment Prerequisites document](#deployment-deployment-before).

This article introduces how to deploy the `Shenyu` gateway in cluster environment.

> In this part, you can see [ShenYu Binary Packages Deployment](#deployment-deployment-package) before deploying.

- Two or more Gateway Boostrap servers, these servers must install JDK1.8+.
- A server for Gateway Admin, this server must install mysql/pgsql/h2 and JDK1.8+.
- A server for nginx.

- download and unzip [apache-shenyu-${current.version}-admin-bin.tar.gz](https://archive.apache.org/dist/incubator/shenyu/2.5.1/apache-shenyu-2.5.1-admin-bin.tar.gz) in your Gateway Admin server.
- config your database, go to the `/conf` directory, and modify `spring.profiles.active` of the configuration in `application.yaml` to `mysql`, `pg` or `h2`.
- config your way of synchronization, go to the `/conf` directory, and modify `shenyu.sync` of configuration in `application.yaml` to `websocket`, `http`, `zookeeper`, `etcd`, `consul` or `nacos`.
- start Apache ShenYu Admin in `bin` directory.

```text
> windows: start.bat  
 
> linux: ./start.sh  
```

- download and unzip [apache-shenyu-${current.version}-bootstrap-bin.tar.gz](https://archive.apache.org/dist/incubator/shenyu/2.5.1/apache-shenyu-2.5.1-bootstrap-bin.tar.gz) in your Gateway Boostrap server.
- config your synchronization, go to the `/conf` directory, and modify `shenyu.sync` of configuration in `application.yaml` to `websocket`, `http`, `zookeeper`, `etcd`, `consul` or `nacos`, this configuaration must remain the same of `ShenyYu Admin`.
- repeat above-mentioned operations in each `ShenYu Bootstrap` server.
- start Apache ShenYu Bootstrap in `bin` directory.

```text
> windwos : start.bat  
 
> linux : ./start.sh  
```

> After completing these operations, you will deploy `ShenYu Boostrap` Cluster.
>
> For example. you will deploy `ShenYu Bootstrap` in `10.1.1.1` and `10.1.1.2` and deploy nginx in `10.1.1.3`.

- download and install `nginx`.
- modify `upstream` and `server` of configuration in `nginx.conf`.

```nginx
upstream shenyu_gateway_cluster {ip_hash; server 10.1.1.1:9195 max_fails=3 fail_timeout=10s weight=50; server 10.1.1.2:9195 max_fails=3 fail_timeout=10s weight=50;}
server {listen 9195; location / {proxy_pass http://shenyu_gateway_cluster; proxy_set_header HOST $host; proxy_read_timeout 10s; proxy_connect_timeout 10s;}}
```

- start nginx.

```text
> windows: ./nginx.exe 
 
> linux: /usr/local/nginx/sbin/nginx  
```

- verify nginx, looking at your `ShenYu Bootstrap` log or `Nginx` log, Where will the verification request go.

Apache ShenYu Nginx Module

---

This module provided SDK to watch available ShenYu instance list as upstream nodes by Service Register Center for OpenResty.

1. [ETCD](#deployment-deployment-cluster--greeting-etcd) (Supported)
2. [Nacos](#deployment-deployment-cluster--greeting-nacos) (Supported)
3. [Zookeeper](#deployment-deployment-cluster--greeting-zookeeper) (Supported)
4. Consul (TODO)

In the cluster mode, Apache ShenYu supports the deployment of multiple ShenYu instances, which may have new instances joining or leaving at any time.
Hence, Apache ShenYu introduces Service Discovery modules to help client to detect the available instances.
Currently, Apache ShenYu Bootstrap already supports Apache Zookeeper, Nacos, Etcd, and consul. Client or LoadBalancer can get the available ShenYu instances by those Service register center.

- Prerequisite:

1. Luarocks
2. OpenResty

The first, clone the source from GitHub.

```text
git clone https://github.com/apache/shenyu-nginx 
```

Then, build from source and install.

```text
cd shenyu-nginx 
luarocks make rockspec/shenyu-nginx-main-0.rockspec 
```

Modify the Nginx configure, create and initialize the ShenYu Register to connect to the target register center.
The module will fetch the all of ShenYu instances which are registered to Etcd in the same cluster.
It works like Etcd client to watch(based on long polling) ShenYu instance lists.

Here is an example for Etcd.

```text
init_worker_by_lua_block { 
    local register = require("shenyu.register.etcd") 
    register.init({ 
        balancer_type = "chash", 
        etcd_base_url = "http://127.0.0.1:2379", 
    }) 
} 
```

1. `balancer_type` specify the balancer. It has supported `chash` and `round robin`.
2. `etcd_base_url` specify the Etcd server.(Currently, authentication is not supported.)

Add an `upstream block` for ShenYu and enable to update upstream servers dynamically. This case will synchronize the ShenYu instance list with register center.
And then pick one up for handling the request.

```text
upstream shenyu { 
    server 0.0.0.1; -- bad  
     
    balancer_by_lua_block { 
        require("shenyu.register.etcd").pick_and_set_peer() 
    } 
} 
```

Finally, restart OpenResty.

```text
openresty -s reload 
```

Here is a completed [example](https://github.com/apache/shenyu-nginx/blob/main/example/etcd/nginx.conf) working with ETCD.

Modify the Nginx configure, create and initialize the ShenYu Register to connect to target register center. Here is an example for Nacos.

```text
init_worker_by_lua_block { 
    local register = require("shenyu.register.nacos") 
    register.init({ 
        shenyu_storage = ngx.shared.shenyu_storage, 
        balancer_type = "chash", 
        nacos_base_url = "http://127.0.0.1:8848", 
        username = "nacos", 
        password = "naocs", 
    }) 
} 
```

1. `balancer_type` specify the balancer. It has supported `chash` and `round robin`.
2. `nacos_base_url` specify the Nacos server address.
3. `username` specify the username to log in Nacos. (it is only required when Nacos auth enable)
4. `password` specify the password to log in Nacos.

Modify the `upstream` to enable to update upstream servers dynamically. This case will synchronize the ShenYu instance list with register center.
And then pick one up for handling the request.

```text
upstream shenyu { 
    server 0.0.0.1; -- bad  
     
    balancer_by_lua_block { 
        require("shenyu.register.nacos").pick_and_set_peer() 
    } 
} 
```

Finally, restart OpenResty.

```text
openresty -s reload 
```

Here is a completed [example](https://github.com/apache/shenyu-nginx/blob/main/example/nacos/nginx.conf) working with Nacos.

Modify the Nginx configure, create and initialize the ShenYu register to connect to target register center.
Listen for changes to the node via the zookeeper watch event. Here is an example of the zookeeper configuration.

```text
init_worker_by_lua_block {local register = require("shenyu.register.zookeeper") register.init({servers = {"127.0.0.1:2181","127.0.0.1:2182"},shenyu_storage = ngx.shared.shenyu_storage,balancer_type = "roundrobin" });}
```

1. `servers` zookeeper cluster address.
2. `balancer_type` specify the balancer. It has supported `chash` and `round robin`.

Modify the upstream to enable to update upstream servers dynamically. This case will synchronize the ShenYu instance list with register center. And then pick one up for handling the request.

```text
 upstream shenyu { 
        server 0.0.0.1; 
        balancer_by_lua_block { 
            require("shenyu.register.zookeeper").pick_and_set_peer() 
        } 
    } 
```

Finally, restart OpenResty.

```text
openresty -s reload 
```

Here is a completed [example](https://github.com/apache/shenyu-nginx/blob/main/example/zookeeper/nginx.conf) working with Zookeeper.

---

<a id="quick-start-quick-start-dubbo"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-dubbo/ -->

<!-- page_index: 19 -->

# Quick start with Dubbo

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using Dubbo. You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-dubbo).

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the Dubbo plugin on in the BasicConfig `->` Plugin, and set your registry address. Please make sure the registry center is open locally.

![](assets/images/dubbo-open-en_263b800bbaa5b327.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.

If client is `apache dubbo`, registry center is `Zookeeper`, please refer to the following configuration:

```xml
        <!-- apache shenyu  apache dubbo plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-apache-dubbo</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <dependency> 
            <groupId>org.apache.dubbo</groupId> 
            <artifactId>dubbo</artifactId> 
            <version>2.7.5</version> 
        </dependency> 
        <!-- Dubbo zookeeper registry dependency start --> 
        <dependency> 
            <groupId>org.apache.curator</groupId> 
            <artifactId>curator-client</artifactId> 
            <version>4.0.1</version> 
            <exclusions> 
                <exclusion> 
                    <artifactId>log4j</artifactId> 
                    <groupId>log4j</groupId> 
                </exclusion> 
            </exclusions> 
        </dependency> 
        <dependency> 
            <groupId>org.apache.curator</groupId> 
            <artifactId>curator-framework</artifactId> 
            <version>4.0.1</version> 
        </dependency> 
        <dependency> 
            <groupId>org.apache.curator</groupId> 
            <artifactId>curator-recipes</artifactId> 
            <version>4.0.1</version> 
        </dependency> 
        <!-- Dubbo zookeeper registry dependency end --> 
        <!-- apache shenyu  apache dubbo plugin end--> 
```

If client is `alibaba dubbo`, registry center is `Zookeeper`, please refer to the following configuration:

```xml
        <!-- apache shenyu alibaba dubbo plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-alibaba-dubbo</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <dependency> 
            <groupId>com.alibaba</groupId> 
            <artifactId>dubbo</artifactId> 
            <version>${alibaba.dubbo.version}</version> 
        </dependency> 
        <dependency> 
            <groupId>org.apache.curator</groupId> 
            <artifactId>curator-client</artifactId> 
            <version>${curator.version}</version> 
            <exclusions> 
                <exclusion> 
                    <artifactId>log4j</artifactId> 
                    <groupId>log4j</groupId> 
                </exclusion> 
            </exclusions> 
        </dependency> 
        <dependency> 
            <groupId>org.apache.curator</groupId> 
            <artifactId>curator-framework</artifactId> 
            <version>${curator.version}</version> 
        </dependency> 
        <dependency> 
            <groupId>org.apache.curator</groupId> 
            <artifactId>curator-recipes</artifactId> 
            <version>${curator.version}</version> 
        </dependency> 
        <!-- apache shenyu  alibaba dubbo plugin end--> 
```

Download [shenyu-examples-dubbo](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-dubbo) .

replace the register address in `shenyu-examples-alibaba-dubbo-service/src/main/resources/spring-dubbo.xml` with your local zk address, such as:

```xml
<dubbo:registry address="zookeeper://localhost:2181"/> 
```

Execute the `org.apache.shenyu.examples.alibaba.dubbo.service.TestAlibabaDubboApplication` main method to start dubbo project.

The following log appears when the startup is successful:

```shell
2021-02-06 20:58:01.807  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/insert","pathDesc":"Insert a row of data","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboTestService","methodName":"insert","ruleName":"/dubbo/insert","parameterTypes":"org.dromara.shenyu.examples.dubbo.api.entity.DubboTest","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.821  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/findAll","pathDesc":"Get all data","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboTestService","methodName":"findAll","ruleName":"/dubbo/findAll","parameterTypes":"","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.833  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/findById","pathDesc":"Query by Id","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboTestService","methodName":"findById","ruleName":"/dubbo/findById","parameterTypes":"java.lang.String","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.844  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/findByListId","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"findByListId","ruleName":"/dubbo/findByListId","parameterTypes":"java.util.List","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.855  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/findByIdsAndName","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"findByIdsAndName","ruleName":"/dubbo/findByIdsAndName","parameterTypes":"java.util.List,java.lang.String","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.866  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/batchSave","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"batchSave","ruleName":"/dubbo/batchSave","parameterTypes":"java.util.List","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.876  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/findByArrayIdsAndName","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"findByArrayIdsAndName","ruleName":"/dubbo/findByArrayIdsAndName","parameterTypes":"[Ljava.lang.Integer;,java.lang.String","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.889  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/saveComplexBeanTestAndName","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"saveComplexBeanTestAndName","ruleName":"/dubbo/saveComplexBeanTestAndName","parameterTypes":"org.dromara.shenyu.examples.dubbo.api.entity.ComplexBeanTest,java.lang.String","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.901  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/batchSaveAndNameAndId","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"batchSaveAndNameAndId","ruleName":"/dubbo/batchSaveAndNameAndId","parameterTypes":"java.util.List,java.lang.String,java.lang.String","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.911  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/saveComplexBeanTest","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"saveComplexBeanTest","ruleName":"/dubbo/saveComplexBeanTest","parameterTypes":"org.dromara.shenyu.examples.dubbo.api.entity.ComplexBeanTest","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
2021-02-06 20:58:01.922  INFO 3724 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : dubbo client register success: {"appName":"dubbo","contextPath":"/dubbo","path":"/dubbo/findByStringArray","pathDesc":"","rpcType":"dubbo","serviceName":"org.dromara.shenyu.examples.dubbo.api.service.DubboMultiParamService","methodName":"findByStringArray","ruleName":"/dubbo/findByStringArray","parameterTypes":"[Ljava.lang.String;","rpcExt":"{\"group\":\"\",\"version\":\"\",\"loadbalance\":\"random\",\"retries\":2,\"timeout\":10000,\"url\":\"\"}","enabled":true}  
```

Note: When you need to expose `multiple protocols` at the same time, please do not configure `shenyu.client.dubbo.props.port`.

The `shenyu-examples-dubbo` project will automatically register interface methods annotated with `@ShenyuDubboClient` in the Apache ShenYu gateway after successful startup.

Open PluginList -> rpc proxy -> dubbo to see the list of plugin rule configurations:

![](assets/images/rule-list-826032a15f07a3e467617873e9ab894c_f22fe8706c5d5572.jpg)

Use `PostMan` to simulate `HTTP` to request your `Dubbo` service:

![](assets/images/postman-findbyid-2db0a41b2665dfc615923b07b0d27221_189e55356eb63b02.jpg)

Complex multi-parameter example: The related interface implementation class is `org.apache.shenyu.examples.alibaba.dubbo.service.impl.DubboMultiParamServiceImpl#batchSaveAndNameAndId`.

```java
@Override 
@ShenyuDubboClient(path = "/batchSaveAndNameAndId") 
public DubboTest batchSaveAndNameAndId(List<DubboTest> dubboTestList, String id, String name) { 
    DubboTest test = new DubboTest(); 
    test.setId(id); 
    test.setName("hello world shenyu alibaba dubbo param batchSaveAndNameAndId :" + name + ":" + dubboTestList.stream().map(DubboTest::getName).collect(Collectors.joining("-"))); 
    return test; 
} 
```

![](assets/images/postman-multiparams-b5bf03d0e31f67a605b7f2b19775ba34_2c467b40d51d66b3.jpg)

When your arguments do not match, the following exception will occur:

```java
2021-02-07 22:24:04.015 ERROR 14860 --- [:20888-thread-3] o.d.shenyu.web.handler.GlobalErrorHandler  : [e47b2a2a] Resolved [ShenyuException: org.apache.dubbo.remoting.RemotingException: java.lang.IllegalArgumentException: args.length != types.length 
java.lang.IllegalArgumentException: args.length != types.length 
	at org.apache.dubbo.common.utils.PojoUtils.realize(PojoUtils.java:91) 
	at org.apache.dubbo.rpc.filter.GenericFilter.invoke(GenericFilter.java:82) 
	at org.apache.dubbo.rpc.protocol.ProtocolFilterWrapper$1.invoke(ProtocolFilterWrapper.java:81) 
	at org.apache.dubbo.rpc.filter.ClassLoaderFilter.invoke(ClassLoaderFilter.java:38) 
	at org.apache.dubbo.rpc.protocol.ProtocolFilterWrapper$1.invoke(ProtocolFilterWrapper.java:81) 
	at org.apache.dubbo.rpc.filter.EchoFilter.invoke(EchoFilter.java:41) 
	at org.apache.dubbo.rpc.protocol.ProtocolFilterWrapper$1.invoke(ProtocolFilterWrapper.java:81) 
	at org.apache.dubbo.rpc.protocol.dubbo.DubboProtocol$1.reply(DubboProtocol.java:150) 
	at org.apache.dubbo.remoting.exchange.support.header.HeaderExchangeHandler.handleRequest(HeaderExchangeHandler.java:100) 
	at org.apache.dubbo.remoting.exchange.support.header.HeaderExchangeHandler.received(HeaderExchangeHandler.java:175) 
	at org.apache.dubbo.remoting.transport.DecodeHandler.received(DecodeHandler.java:51) 
	at org.apache.dubbo.remoting.transport.dispatcher.ChannelEventRunnable.run(ChannelEventRunnable.java:57) 
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1149) 
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:624) 
	at java.lang.Thread.run(Thread.java:748) 
] for HTTP POST /dubbo/batchSaveAndNameAndId 
```

---

<a id="quick-start-quick-start-grpc"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-grpc/ -->

<!-- page_index: 20 -->

# Quick start with gRPC

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using gRPC. You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-grpc) .

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the gRPC plugin on in the BasicConfig `->` Plugin.

![](assets/images/grpc-en-1_fa5bdbd0242453c9.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.

Add the following dependencies to the gateway's `pom.xml` file:

```xml
        <!-- apache shenyu grpc plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-grpc</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <!-- apache shenyu grpc plugin end--> 
```

Download [shenyu-examples-grpc](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-grpc)

Run the following command under `shenyu-examples-grpc` to generate Java code:

```shell
mvn protobuf:compile  
mvn protobuf:compile-custom  
```

Execute the `org.apache.shenyu.examples.grpc.ShenyuTestGrpcApplication` main method to start project.

The following log appears when the startup is successful:

```shell
2021-06-18 19:33:32.866  INFO 11004 --- [or_consumer_-19] o.a.s.r.client.http.utils.RegisterUtils  : grpc client register success: {"appName":"127.0.0.1:8080","contextPath":"/grpc","path":"/grpc/clientStreamingFun","pathDesc":"clientStreamingFun","rpcType":"grpc","serviceName":"stream.StreamService","methodName":"clientStreamingFun","ruleName":"/grpc/clientStreamingFun","parameterTypes":"io.grpc.stub.StreamObserver","rpcExt":"{\"timeout\":5000,\"methodType\":\"CLIENT_STREAMING\"}","enabled":true,"host":"172.20.10.6","port":8080,"registerMetaData":false}  
2021-06-18 19:33:32.866  INFO 11004 --- [or_consumer_-17] o.a.s.r.client.http.utils.RegisterUtils  : grpc client register success: {"appName":"127.0.0.1:8080","contextPath":"/grpc","path":"/grpc/echo","pathDesc":"echo","rpcType":"grpc","serviceName":"echo.EchoService","methodName":"echo","ruleName":"/grpc/echo","parameterTypes":"echo.EchoRequest,io.grpc.stub.StreamObserver","rpcExt":"{\"timeout\":5000,\"methodType\":\"UNARY\"}","enabled":true,"host":"172.20.10.6","port":8080,"registerMetaData":false}  
2021-06-18 19:33:32.866  INFO 11004 --- [or_consumer_-20] o.a.s.r.client.http.utils.RegisterUtils  : grpc client register success: {"appName":"127.0.0.1:8080","contextPath":"/grpc","path":"/grpc/bidiStreamingFun","pathDesc":"bidiStreamingFun","rpcType":"grpc","serviceName":"stream.StreamService","methodName":"bidiStreamingFun","ruleName":"/grpc/bidiStreamingFun","parameterTypes":"io.grpc.stub.StreamObserver","rpcExt":"{\"timeout\":5000,\"methodType\":\"BIDI_STREAMING\"}","enabled":true,"host":"172.20.10.6","port":8080,"registerMetaData":false}  
2021-06-18 19:33:32.866  INFO 11004 --- [or_consumer_-21] o.a.s.r.client.http.utils.RegisterUtils  : grpc client register success: {"appName":"127.0.0.1:8080","contextPath":"/grpc","path":"/grpc/unaryFun","pathDesc":"unaryFun","rpcType":"grpc","serviceName":"stream.StreamService","methodName":"unaryFun","ruleName":"/grpc/unaryFun","parameterTypes":"stream.RequestData,io.grpc.stub.StreamObserver","rpcExt":"{\"timeout\":5000,\"methodType\":\"UNARY\"}","enabled":true,"host":"172.20.10.6","port":8080,"registerMetaData":false}  
2021-06-18 19:33:32.866  INFO 11004 --- [or_consumer_-18] o.a.s.r.client.http.utils.RegisterUtils  : grpc client register success: {"appName":"127.0.0.1:8080","contextPath":"/grpc","path":"/grpc/serverStreamingFun","pathDesc":"serverStreamingFun","rpcType":"grpc","serviceName":"stream.StreamService","methodName":"serverStreamingFun","ruleName":"/grpc/serverStreamingFun","parameterTypes":"stream.RequestData,io.grpc.stub.StreamObserver","rpcExt":"{\"timeout\":5000,\"methodType\":\"SERVER_STREAMING\"}","enabled":true,"host":"172.20.10.6","port":8080,"registerMetaData":false}  
```

The `shenyu-examples-grpc` project will automatically register interface methods annotated with `@ShenyuGrpcClient` in the Apache ShenYu gateway after successful startup.

Open PluginList -> rpc proxy -> gRPC to see the list of plugin rule configurations:

![](assets/images/grpc-service-en-452d3e22231d1f157574d8100d0cf487_984767bcae7b2854.png)

Use `postman` to simulate `http` to request your gRPC service. The following is the request body.

```json
{ 
    "data": [ 
        { 
            "message": "hello grpc" 
        } 
    ] 
} 
```

![](assets/images/grpc-echo-622ab008544874bfe975c31ea8545f52_777e601d51637674.png)

The parameters are passed in json format. The name of the key is `data` by default, and you can reset it in `GrpcConstants.JSON_DESCRIPTOR_PROTO_FIELD_NAME`. The input of value is based on the proto file defined by you.

the Apache ShenYu can support streaming of gRPC. The following shows the calls of the four method types of gRPC. In streaming, you can pass multiple parameters in the form of an array.

- `UNARY`

The request body like this.

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

Then, call gRPC service by `UNARY` method type.

![](assets/images/grpc-unary-db53f0d92c8528d0685a008264891bad_78cfb77009caea47.png)

- `CLIENT_STREAMING`

The request body like this.

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

Then, call gRPC service by `CLIENT_STREAMING` method type.

![](assets/images/grpc-client-stream-a715f4134ee74eb658ba99c0f60c65b6_7befece77cf42572.png)

- `SERVER_STREAMING`

The request body like this.

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

Then, call gRPC service by `SERVER_STREAMING` method type.

![](assets/images/grpc-server-stream-515e14914bb628f6e1886f2c07e5a88f_7bcf5a8229cd3a14.png)

- `BIDI_STREAMING`

The request body like this.

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

Then, call gRPC service by `BIDI_STREAMING` method type.

![](assets/images/grpc-bidi-stream-56880817c53ae36e4408d957b0269cdc_7014fc5306cf96f1.png)

---

<a id="quick-start-quick-start-http"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-http/ -->

<!-- page_index: 21 -->

# Quick start with Http

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using Http. You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http).

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the Divide plugin on in the BasicConfig `->` Plugin. In the Apache ShenYu gateway, the HTTP request is handled by the Divide plugin.

![](assets/images/http-open-en_afbf799c73b0443f.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.

Add the following dependencies to the gateway's `pom.xml` file:

```xml
        <!--if you use http proxy start this--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-divide</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
```

Download [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http)

Execute the `org.apache.shenyu.examples.http.ShenyuTestHttpApplication` main method to start project.

Since `2.4.3`, `shenyu.client.http.props.port` can be non-configured if you like.

The following log appears when the startup is successful:

```shell
2021-02-10 00:57:07.561  INFO 3700 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : http client register success: {"appName":"http","context":"/http","path":"/http/test/**","pathDesc":"","rpcType":"http","host":"192.168.50.13","port":8188,"ruleName":"/http/test/**","enabled":true,"registerMetaData":false}  
2021-02-10 00:57:07.577  INFO 3700 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : http client register success: {"appName":"http","context":"/http","path":"/http/order/save","pathDesc":"Save order","rpcType":"http","host":"192.168.50.13","port":8188,"ruleName":"/http/order/save","enabled":true,"registerMetaData":false}  
2021-02-10 00:57:07.587  INFO 3700 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : http client register success: {"appName":"http","context":"/http","path":"/http/order/path/**/name","pathDesc":"","rpcType":"http","host":"192.168.50.13","port":8188,"ruleName":"/http/order/path/**/name","enabled":true,"registerMetaData":false}  
2021-02-10 00:57:07.596  INFO 3700 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : http client register success: {"appName":"http","context":"/http","path":"/http/order/findById","pathDesc":"Find by id","rpcType":"http","host":"192.168.50.13","port":8188,"ruleName":"/http/order/findById","enabled":true,"registerMetaData":false}  
2021-02-10 00:57:07.606  INFO 3700 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : http client register success: {"appName":"http","context":"/http","path":"/http/order/path/**","pathDesc":"","rpcType":"http","host":"192.168.50.13","port":8188,"ruleName":"/http/order/path/**","enabled":true,"registerMetaData":false}  
2021-02-10 00:57:08.023  INFO 3700 --- [           main] o.s.b.web.embedded.netty.NettyWebServer  : Netty started on port(s): 8188 
2021-02-10 00:57:08.026  INFO 3700 --- [           main] o.d.s.e.http.ShenyuTestHttpApplication     : Started ShenyuTestHttpApplication in 2.555 seconds (JVM running for 3.411)  
```

The `shenyu-examples-http` project will automatically register interface methods annotated with `@ShenyuSpringMvcClient` in the Apache ShenYu gateway after successful startup.

Open PluginList -> Proxy -> divide to see the list of plugin rule configurations:

![](assets/images/rule-list-44d335cb7d35496ced765ebf3751ac55_7ac7111c449a7280.png)

Use PostMan to simulate HTTP to request your http service:

![](assets/images/postman-test-ffc28736280dc05a51162a4db2a0a7df_9b4a4afe121cad9f.png)

Use IDEA HTTP Client Plugin to simulate HTTP to request your http service[local:no Shenyu proxy]:

![](assets/images/idea-http-test-local-3e6960c11dc2bd689ec5276b5e219ce3_e31caec069cca923.png)

Use IDEA HTTP Client Plugin to simulate HTTP to request your http service[Shenyu proxy]:

![](assets/images/idea-http-test-proxy-bf5aad9695bc73dc71565ea308ad1ef1_996473cc46eb68e0.png)

---

<a id="quick-start-quick-start-mcpserver"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-mcpServer/ -->

<!-- page_index: 22 -->

# Quick start with Mcp Server

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using McpServer . You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-mcp).

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the Divide and McpServer plugin on in the BasicConfig `->` Plugin.

![](assets/images/mcp-server-enable-en-4f456c17c5c33057e0c327d73579c841_f52f158ab0fb3d22.png)

![](assets/images/divide-enable-en-31dc7c1a9a5b9d6274506b5afe02804f_82f5bdfb5180a4a3.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.

To support `McpServer`, include the following dependencies in the gateway's `pom.xml` file:

```xml
        <!--if you use http proxy start this--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-divide</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
         
        <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> 
        <version>${project.version}</version> 
        </dependency> 
 
        <!--Mcp Server Plugin Start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-mcp-server</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <!--Mcp Server Plugin end--> 
```

Download [shenyu-examples-mcp](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-mcp).

Execute the `org.apache.shenyu.examples.http.ShenyuTestHttpApplication` main method to start project.

The following log appears when the startup is successful:

```shell
2025-11-07T22:39:35.596+08:00  INFO 4336 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port 8150 (http) with context path '' 
2025-11-07T22:39:35.673+08:00  INFO 4336 --- [           main] o.a.shenyu.ShenyuTestMcpApplication      : Started ShenyuTestMcpApplication in 2.125 seconds (process running for 2.571) 
2025-11-07T22:39:36.086+08:00  INFO 4336 --- [or_consumer_-65] o.a.s.r.client.http.utils.RegisterUtils  : login success: {"id":"1","userName":"admin","role":1,"enabled":true,"dateCreated":"2025-11-07 22:39:25","dateUpdated":"2025-11-07 22:39:25","token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFkbWluIiwiZXhwIjoxNzYyNjEyNzc2fQ.kSfDHEMBR99G4pUv28Bw2ZV3CcUxZTFH91Nyb7IJZxA","expiredTime":86400000}  
2025-11-07T22:39:36.153+08:00  INFO 4336 --- [or_consumer_-65] o.a.s.r.client.http.utils.RegisterUtils  : mcp client register success: {"metaDataRegisterDTO":{"appName":"/order","contextPath":"/order","path":"http://localhost:8150","pathDesc":"","rpcType":"mcp","serviceName":"","methodName":"findAll","ruleName":"findAllOrder","parameterTypes":"","enabled":true,"host":"192.168.219.1","port":-1,"pluginNames":[],"registerMetaData":false,"timeMillis":1762526375637,"addPrefixed":false,"namespaceId":"649330b6-c2d7-4edc-be8e-8a54df9eb385"},"namespaceId":"649330b6-c2d7-4edc-be8e-8a54df9eb385","mcpConfig":"{\"name\":\"findAllOrder\",\"parameters\":[],\"requestConfig\":\"{\\\"requestTemplate\\\":{\\\"url\\\":\\\"/order/findAll\\\",\\\"method\\\":\\\"Get\\\",\\\"argsPosition\\\":{},\\\"argsToJsonBody\\\":\\\"false\\\",\\\"headers\\\":[{\\\"aaa\\\":\\\"bbb\\\"}]}}\",\"description\":\"find all order\"}"}  
2025-11-07T22:39:36.153+08:00  INFO 4336 --- [or_consumer_-66] o.a.s.r.client.http.utils.RegisterUtils  : mcp client register success: {"metaDataRegisterDTO":{"appName":"/order","contextPath":"/order","path":"http://localhost:8150","pathDesc":"","rpcType":"mcp","serviceName":"","methodName":"findByName","ruleName":"findByName","parameterTypes":"java.lang.String","enabled":true,"host":"192.168.219.1","port":-1,"pluginNames":[],"registerMetaData":false,"timeMillis":1762526375655,"addPrefixed":false,"namespaceId":"649330b6-c2d7-4edc-be8e-8a54df9eb385"},"namespaceId":"649330b6-c2d7-4edc-be8e-8a54df9eb385","mcpConfig":"{\"name\":\"findByName\",\"parameters\":[{\"name\":\"name\",\"in\":\"query\",\"description\":\"name\",\"required\":false}],\"requestConfig\":\"{\\\"requestTemplate\\\":{\\\"url\\\":\\\"/order/findByName\\\",\\\"method\\\":\\\"GET\\\",\\\"argsPosition\\\":{\\\"name\\\":\\\"query\\\"},\\\"argsToJsonBody\\\":\\\"false\\\",\\\"headers\\\":[]}}\",\"description\":\"findByName\"}"}  
2025-11-07T22:39:36.153+08:00  INFO 4336 --- [or_consumer_-67] o.a.s.r.client.http.utils.RegisterUtils  : mcp client register success: {"metaDataRegisterDTO":{"appName":"/order","contextPath":"/order","path":"http://localhost:8150","pathDesc":"","rpcType":"mcp","serviceName":"","methodName":"findById","ruleName":"findOrderById","parameterTypes":"java.lang.String","enabled":true,"host":"192.168.219.1","port":-1,"pluginNames":[],"registerMetaData":false,"timeMillis":1762526375670,"addPrefixed":false,"namespaceId":"649330b6-c2d7-4edc-be8e-8a54df9eb385"},"namespaceId":"649330b6-c2d7-4edc-be8e-8a54df9eb385","mcpConfig":"{\"name\":\"findOrderById\",\"parameters\":[{\"name\":\"id\",\"in\":\"path\",\"description\":\"the id of order\",\"required\":true,\"type\":\"string\"}],\"requestConfig\":\"{\\\"requestTemplate\\\":{\\\"url\\\":\\\"/order/findById\\\",\\\"method\\\":\\\"Get\\\",\\\"argsPosition\\\":{\\\"id\\\":\\\"path\\\"},\\\"argsToJsonBody\\\":\\\"false\\\",\\\"headers\\\":[{\\\"aaa\\\":\\\"bbb\\\"}]}}\",\"description\":\"find order by id\"}"}  
```

The `shenyu-examples-http` project will automatically register interface methods annotated with `@ShenyuMcpTool` and `@ShenyuSpringMvcClient` in the Apache ShenYu gateway after successful startup.

Go to Plugin List -> mcp -> McpServer and Plugin List -> proxy -> divide to view the plugin rule configuration list:

![](assets/images/mcp-server-rule-list-3544a6beba6608805840b8c041812c35_ff76e5f1f3e27892.png)

![](assets/images/divide-rule-list-7c6a229efb9dca7b5ae102425cad81f3_9a0af89c961024b1.png)

Please ensure that the `divide` plugin's `selector -> Modify -> Discovery Config` contains the following configuration:

![](assets/images/divide-discovery-upstream-config-ed72e0b5225d875b1727cb51ac2dc2e4_cb136d1af69e4c3b.png)

Below, a custom Agent is used to simulate a client calling the `shenyu Mcp Server` service through `mcp sse`:

Create an `mcp` client and add the following URL in it. If you are using a commercial Agent, please add the URL in its relevant configuration.

![](assets/images/create-mcp-client-c5d05a73fa6f58c0cb560552bd29c35b_a4e3119b9aa65b24.png)

![](data:image/png;base64,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)

Let the Agent initiate a tool call. the result is following.

![](assets/images/user-question-en-2a4f5667d872b2f192426344876c9589_dde94fe86d95508b.png)

![](assets/images/agent-result-en-ac60133074675e434b5a40271185ebdf_715ddf60bf8118b5.png)

---

<a id="quick-start-quick-start-motan"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-motan/ -->

<!-- page_index: 23 -->

# Quick start with Motan

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using Motan RPC. You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-motan).

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the Sofa plugin on in the BasicConfig `->` Plugin.

![](assets/images/motan-open-en_bef8b6a8ae5ac0aa.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.
> Start up zookeeper in local.

Import the gateway proxy plugin for `Motan` and add the following dependencies to the gateway's `pom.xml` file:

```xml
        <!-- apache shenyu motan plugin --> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-motan</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-core</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-registry-zookeeper</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-transport-netty4</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-springsupport</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
```

Download [shenyu-examples-motan](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-motan) .

Run main method of `org.apache.shenyu.examples.motan.service.TestMotanApplication` to start this project.

log info as follows after starting:

```shell
2021-07-18 16:46:25.388  INFO 96 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8081 (http) with context path '' 
2021-07-18 16:46:25.393  INFO 96 --- [           main] o.a.s.e.m.service.TestMotanApplication   : Started TestMotanApplication in 3.89 seconds (JVM running for 4.514) 
2021-07-18 16:46:25.396  INFO 96 --- [           main] info                                     : [ZookeeperRegistry] Url (null) will set to available to Registry [zookeeper://localhost:2181/default_rpc/com.weibo.api.motan.registry.RegistryService/1.0/service] 
2021-07-18 16:46:25.399  INFO 96 --- [       Thread-6] o.a.s.c.c.s.ShenyuClientShutdownHook     : hook Thread-0 will sleep 3000ms when it start 
2021-07-18 16:46:25.399  INFO 96 --- [       Thread-6] o.a.s.c.c.s.ShenyuClientShutdownHook     : hook SpringContextShutdownHook will sleep 3000ms when it start 
2021-07-18 16:46:25.445  INFO 96 --- [ntLoopGroup-3-2] info                                     : NettyChannelHandler channelActive: remote=/192.168.1.8:49740 local=/192.168.1.8:8002 
2021-07-18 16:46:25.445  INFO 96 --- [ntLoopGroup-3-1] info                                     : NettyChannelHandler channelActive: remote=/192.168.1.8:49739 local=/192.168.1.8:8002 
2021-07-18 16:46:25.925  INFO 96 --- [or_consumer_-17] o.a.s.r.client.http.utils.RegisterUtils  : motan client register success: {"appName":"motan","contextPath":"/motan","path":"/motan/hello","pathDesc":"","rpcType":"motan","serviceName":"org.apache.shenyu.examples.motan.service.MotanDemoService","methodName":"hello","ruleName":"/motan/hello","parameterTypes":"java.lang.String","rpcExt":"{\"methodInfo\":[{\"methodName\":\"hello\",\"params\":[{\"left\":\"java.lang.String\",\"right\":\"name\"}]}],\"group\":\"motan-shenyu-rpc\"}","enabled":true,"host":"192.168.220.1","port":8081,"registerMetaData":false}  
 
```

The `shenyu-examples-motan` project will automatically register the `@ShenyuMotanClient` annotated interface methods with the gateway and add selectors and rules. If not, you can manually add them.

Open PluginList -> rpc proxy -> motan to see the list of plugin rule configurations:

![](assets/images/motan-service-en_48c78afd567dc1e3.png)

Use PostMan to simulate HTTP to request your Motan service:

![](assets/images/motan-service_50be9abcada1bb00.png)

---

<a id="quick-start-quick-start-sofa"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-sofa/ -->

<!-- page_index: 24 -->

# Quick start with Sofa

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using Sofa RPC. You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sofa).

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the Sofa plugin on in the BasicConfig `->` Plugin, and set your registry address. Please make sure the registry center is open locally.

![](assets/images/sofa-open-en_146f7b329c1210a8.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.

If client is `sofa`, registry center is `Zookeeper`, please refer to the following configuration:

```xml
        <!-- apache shenyu sofa plugin start--> 
        <dependency> 
            <groupId>com.alipay.sofa</groupId> 
            <artifactId>sofa-rpc-all</artifactId> 
            <version>5.7.6</version> 
        </dependency> 
        <dependency> 
               <groupId>org.apache.curator</groupId> 
               <artifactId>curator-client</artifactId> 
               <version>4.0.1</version> 
           </dependency> 
           <dependency> 
               <groupId>org.apache.curator</groupId> 
               <artifactId>curator-framework</artifactId> 
               <version>4.0.1</version> 
           </dependency> 
           <dependency> 
               <groupId>org.apache.curator</groupId> 
               <artifactId>curator-recipes</artifactId> 
               <version>4.0.1</version> 
           </dependency> 
 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-sofa</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <!-- apache shenyu sofa plugin end--> 
 
```

Download [shenyu-examples-sofa](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sofa), replace the register address in `spring-dubbo.xml` with your local zk address, such as:

```yaml
com: 
  alipay: 
    sofa: 
      rpc: 
        registry-address: zookeeper://127.0.0.1:2181 
```

Execute the `org.apache.shenyu.examples.sofa.service.TestSofaApplication` main method to start sofa service.

The following log appears when the startup is successful:

```shell
2021-02-10 02:31:45.599  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/insert","pathDesc":"Insert a row of data","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaSingleParamService","methodName":"insert","ruleName":"/sofa/insert","parameterTypes":"org.dromara.shenyu.examples.sofa.api.entity.SofaSimpleTypeBean","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.605  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/findById","pathDesc":"Find by Id","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaSingleParamService","methodName":"findById","ruleName":"/sofa/findById","parameterTypes":"java.lang.String","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.611  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/findAll","pathDesc":"Get all data","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaSingleParamService","methodName":"findAll","ruleName":"/sofa/findAll","parameterTypes":"","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.616  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/batchSaveNameAndId","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"batchSaveNameAndId","ruleName":"/sofa/batchSaveNameAndId","parameterTypes":"java.util.List,java.lang.String,java.lang.String#org.dromara.shenyu.examples.sofa.api.entity.SofaSimpleTypeBean","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.621  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/saveComplexBeanAndName","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"saveComplexBeanAndName","ruleName":"/sofa/saveComplexBeanAndName","parameterTypes":"org.dromara.shenyu.examples.sofa.api.entity.SofaComplexTypeBean,java.lang.String","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.627  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/findByArrayIdsAndName","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"findByArrayIdsAndName","ruleName":"/sofa/findByArrayIdsAndName","parameterTypes":"[Ljava.lang.Integer;,java.lang.String","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.632  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/findByStringArray","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"findByStringArray","ruleName":"/sofa/findByStringArray","parameterTypes":"[Ljava.lang.String;","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.637  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/saveTwoList","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"saveTwoList","ruleName":"/sofa/saveTwoList","parameterTypes":"java.util.List,java.util.Map#org.dromara.shenyu.examples.sofa.api.entity.SofaComplexTypeBean","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.642  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/batchSave","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"batchSave","ruleName":"/sofa/batchSave","parameterTypes":"java.util.List#org.dromara.shenyu.examples.sofa.api.entity.SofaSimpleTypeBean","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.647  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/findByListId","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"findByListId","ruleName":"/sofa/findByListId","parameterTypes":"java.util.List","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.653  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/saveComplexBean","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"saveComplexBean","ruleName":"/sofa/saveComplexBean","parameterTypes":"org.dromara.shenyu.examples.sofa.api.entity.SofaComplexTypeBean","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:45.660  INFO 2156 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : sofa client register success: {"appName":"sofa","contextPath":"/sofa","path":"/sofa/findByIdsAndName","pathDesc":"","rpcType":"sofa","serviceName":"org.dromara.shenyu.examples.sofa.api.service.SofaMultiParamService","methodName":"findByIdsAndName","ruleName":"/sofa/findByIdsAndName","parameterTypes":"java.util.List,java.lang.String","rpcExt":"{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}","enabled":true}  
2021-02-10 02:31:46.055  INFO 2156 --- [           main] o.a.c.f.imps.CuratorFrameworkImpl        : Starting 
2021-02-10 02:31:46.059  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:zookeeper.version=3.4.6-1569965, built on 02/20/2014 09:09 GMT 
2021-02-10 02:31:46.059  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:host.name=host.docker.internal 
2021-02-10 02:31:46.059  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:java.version=1.8.0_211 
2021-02-10 02:31:46.059  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:java.vendor=Oracle Corporation 
2021-02-10 02:31:46.059  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:java.home=C:\Program Files\Java\jdk1.8.0_211\jre 
2021-02-10 02:31:46.059  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:java.class.path=C:\Program Files\Java\jdk1.8.0_211\jre\lib\charsets.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\deploy.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\access-bridge-64.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\cldrdata.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\dnsns.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\jaccess.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\jfxrt.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\localedata.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\nashorn.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\sunec.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\sunjce_provider.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\sunmscapi.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\sunpkcs11.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\ext\zipfs.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\javaws.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\jce.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\jfr.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\jfxswt.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\jsse.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\management-agent.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\plugin.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\resources.jar;C:\Program Files\Java\jdk1.8.0_211\jre\lib\rt.jar;D:\X\dlm_github\shenyu\shenyu-examples\shenyu-examples-sofa\shenyu-examples-sofa-service\target\classes;D:\SOFT\m2\repository\com\alipay\sofa\rpc-sofa-boot-starter\6.0.4\rpc-sofa-boot-starter-6.0.4.jar;D:\SOFT\m2\repository\com\alipay\sofa\rpc-sofa-boot-core\6.0.4\rpc-sofa-boot-core-6.0.4.jar;D:\SOFT\m2\repository\com\alipay\sofa\sofa-rpc-all\5.5.7\sofa-rpc-all-5.5.7.jar;D:\SOFT\m2\repository\com\alipay\sofa\bolt\1.4.6\bolt-1.4.6.jar;D:\SOFT\m2\repository\org\javassist\javassist\3.20.0-GA\javassist-3.20.0-GA.jar;D:\SOFT\m2\repository\io\netty\netty-all\4.1.43.Final\netty-all-4.1.43.Final.jar;D:\SOFT\m2\repository\com\alipay\sofa\hessian\3.3.6\hessian-3.3.6.jar;D:\SOFT\m2\repository\com\alipay\sofa\tracer-core\2.1.2\tracer-core-2.1.2.jar;D:\SOFT\m2\repository\io\opentracing\opentracing-api\0.22.0\opentracing-api-0.22.0.jar;D:\SOFT\m2\repository\io\opentracing\opentracing-noop\0.22.0\opentracing-noop-0.22.0.jar;D:\SOFT\m2\repository\io\opentracing\opentracing-mock\0.22.0\opentracing-mock-0.22.0.jar;D:\SOFT\m2\repository\io\opentracing\opentracing-util\0.22.0\opentracing-util-0.22.0.jar;D:\SOFT\m2\repository\com\alipay\sofa\lookout\lookout-api\1.4.1\lookout-api-1.4.1.jar;D:\SOFT\m2\repository\com\alipay\sofa\runtime-sofa-boot-starter\3.1.4\runtime-sofa-boot-starter-3.1.4.jar;D:\SOFT\m2\repository\org\apache\curator\curator-client\2.9.1\curator-client-2.9.1.jar;D:\SOFT\m2\repository\org\apache\zookeeper\zookeeper\3.4.6\zookeeper-3.4.6.jar;D:\SOFT\m2\repository\log4j\log4j\1.2.16\log4j-1.2.16.jar;D:\SOFT\m2\repository\jline\jline\0.9.94\jline-0.9.94.jar;D:\SOFT\m2\repository\io\netty\netty\3.7.0.Final\netty-3.7.0.Final.jar;D:\SOFT\m2\repository\com\google\guava\guava\16.0.1\guava-16.0.1.jar;D:\SOFT\m2\repository\org\apache\curator\curator-framework\2.9.1\curator-framework-2.9.1.jar;D:\SOFT\m2\repository\org\apache\curator\curator-recipes\2.9.1\curator-recipes-2.9.1.jar;D:\SOFT\m2\repository\org\jboss\resteasy\resteasy-jaxrs\3.0.12.Final\resteasy-jaxrs-3.0.12.Final.jar;D:\SOFT\m2\repository\org\jboss\spec\javax\annotation\jboss-annotations-api_1.1_spec\1.0.1.Final\jboss-annotations-api_1.1_spec-1.0.1.Final.jar;D:\SOFT\m2\repository\javax\activation\activation\1.1.1\activation-1.1.1.jar;D:\SOFT\m2\repository\org\apache\httpcomponents\httpclient\4.5.10\httpclient-4.5.10.jar;D:\SOFT\m2\repository\org\apache\httpcomponents\httpcore\4.4.12\httpcore-4.4.12.jar;D:\SOFT\m2\repository\commons-io\commons-io\2.1\commons-io-2.1.jar;D:\SOFT\m2\repository\net\jcip\jcip-annotations\1.0\jcip-annotations-1.0.jar;D:\SOFT\m2\repository\org\jboss\resteasy\resteasy-client\3.0.12.Final\resteasy-client-3.0.12.Final.jar;D:\SOFT\m2\repository\org\jboss\resteasy\resteasy-jackson-provider\3.0.12.Final\resteasy-jackson-provider-3.0.12.Final.jar;D:\SOFT\m2\repository\org\codehaus\jackson\jackson-core-asl\1.9.12\jackson-core-asl-1.9.12.jar;D:\SOFT\m2\repository\org\codehaus\jackson\jackson-mapper-asl\1.9.12\jackson-mapper-asl-1.9.12.jar;D:\SOFT\m2\repository\org\codehaus\jackson\jackson-jaxrs\1.9.12\jackson-jaxrs-1.9.12.jar;D:\SOFT\m2\repository\org\codehaus\jackson\jackson-xc\1.9.12\jackson-xc-1.9.12.jar;D:\SOFT\m2\repository\org\jboss\resteasy\resteasy-netty4\3.0.12.Final\resteasy-netty4-3.0.12.Final.jar;D:\SOFT\m2\repository\org\jboss\resteasy\resteasy-validator-provider-11\3.0.12.Final\resteasy-validator-provider-11-3.0.12.Final.jar;D:\SOFT\m2\repository\com\fasterxml\classmate\1.5.1\classmate-1.5.1.jar;D:\SOFT\m2\repository\org\jboss\resteasy\jaxrs-api\3.0.12.Final\jaxrs-api-3.0.12.Final.jar;D:\SOFT\m2\repository\org\jboss\resteasy\resteasy-multipart-provider\3.0.12.Final\resteasy-multipart-provider-3.0.12.Final.jar;D:\SOFT\m2\repository\org\jboss\resteasy\resteasy-jaxb-provider\3.0.12.Final\resteasy-jaxb-provider-3.0.12.Final.jar;D:\SOFT\m2\repository\com\sun\xml\bind\jaxb-impl\2.2.7\jaxb-impl-2.2.7.jar;D:\SOFT\m2\repository\com\sun\xml\bind\jaxb-core\2.2.7\jaxb-core-2.2.7.jar;D:\SOFT\m2\repository\javax\xml\bind\jaxb-api\2.3.1\jaxb-api-2.3.1.jar;D:\SOFT\m2\repository\javax\activation\javax.activation-api\1.2.0\javax.activation-api-1.2.0.jar;D:\SOFT\m2\repository\com\sun\istack\istack-commons-runtime\2.16\istack-commons-runtime-2.16.jar;D:\SOFT\m2\repository\com\sun\xml\fastinfoset\FastInfoset\1.2.12\FastInfoset-1.2.12.jar;D:\SOFT\m2\repository\javax\xml\bind\jsr173_api\1.0\jsr173_api-1.0.jar;D:\SOFT\m2\repository\javax\mail\mail\1.5.0-b01\mail-1.5.0-b01.jar;D:\SOFT\m2\repository\org\apache\james\apache-mime4j\0.6\apache-mime4j-0.6.jar;D:\SOFT\m2\repository\commons-logging\commons-logging\1.1.1\commons-logging-1.1.1.jar;D:\SOFT\m2\repository\com\alibaba\dubbo\2.4.10\dubbo-2.4.10.jar;D:\SOFT\m2\repository\org\jboss\netty\netty\3.2.5.Final\netty-3.2.5.Final.jar;D:\SOFT\m2\repository\com\101tec\zkclient\0.10\zkclient-0.10.jar;D:\SOFT\m2\repository\com\alibaba\nacos\nacos-api\1.0.0\nacos-api-1.0.0.jar;D:\SOFT\m2\repository\com\alibaba\fastjson\1.2.47\fastjson-1.2.47.jar;D:\SOFT\m2\repository\org\apache\commons\commons-lang3\3.9\commons-lang3-3.9.jar;D:\SOFT\m2\repository\com\alibaba\nacos\nacos-client\1.0.0\nacos-client-1.0.0.jar;D:\SOFT\m2\repository\com\alibaba\nacos\nacos-common\1.0.0\nacos-common-1.0.0.jar;D:\SOFT\m2\repository\commons-codec\commons-codec\1.13\commons-codec-1.13.jar;D:\SOFT\m2\repository\com\fasterxml\jackson\core\jackson-core\2.10.1\jackson-core-2.10.1.jar;D:\SOFT\m2\repository\com\fasterxml\jackson\core\jackson-databind\2.10.1\jackson-databind-2.10.1.jar;D:\SOFT\m2\repository\com\fasterxml\jackson\core\jackson-annotations\2.10.1\jackson-annotations-2.10.1.jar;D:\SOFT\m2\repository\io\prometheus\simpleclient\0.5.0\simpleclient-0.5.0.jar;D:\SOFT\m2\repository\org\springframework\spring-beans\5.2.2.RELEASE\spring-beans-5.2.2.RELEASE.jar;D:\SOFT\m2\repository\org\springframework\spring-core\5.2.2.RELEASE\spring-core-5.2.2.RELEASE.jar;D:\SOFT\m2\repository\org\springframework\spring-jcl\5.2.2.RELEASE\spring-jcl-5.2.2.RELEASE.jar;D:\SOFT\m2\repository\com\alipay\sofa\infra-sofa-boot-starter\3.1.4\infra-sofa-boot-starter-3.1.4.jar;D:\SOFT\m2\repository\com\alipay\sofa\common\log-sofa-boot-starter\1.0.18\log-sofa-boot-starter-1.0.18.jar;D:\SOFT\m2\repository\org\springframework\spring-context\5.2.2.RELEASE\spring-context-5.2.2.RELEASE.jar;D:\SOFT\m2\repository\org\springframework\spring-aop\5.2.2.RELEASE\spring-aop-5.2.2.RELEASE.jar;D:\SOFT\m2\repository\org\springframework\spring-expression\5.2.2.RELEASE\spring-expression-5.2.2.RELEASE.jar;D:\SOFT\m2\repository\com\alipay\sofa\common\sofa-common-tools\1.0.18\sofa-common-tools-1.0.18.jar;D:\SOFT\m2\repository\org\springframework\boot\spring-boot-starter-validation\2.2.2.RELEASE\spring-boot-starter-validation-2.2.2.RELEASE.jar;D:\SOFT\m2\repository\jakarta\validation\jakarta.validation-api\2.0.1\jakarta.validation-api-2.0.1.jar;D:\SOFT\m2\repository\org\hibernate\validator\hibernate-validator\6.0.18.Final\hibernate-validator-6.0.18.Final.jar;D:\SOFT\m2\repository\org\jboss\logging\jboss-logging\3.4.1.Final\jboss-logging-3.4.1.Final.jar;D:\SOFT\m2\repository\org\apache\tomcat\embed\tomcat-embed-el\9.0.29\tomcat-embed-el-9.0.29.jar;D:\SOFT\m2\repository\org\springframework\boot\spring-boot-autoconfigure\2.2.2.RELEASE\spring-boot-autoconfigure-2.2.2.RELEASE.jar;D:\SOFT\m2\repository\org\springframework\boot\spring-boot\2.2.2.RELEASE\spring-boot-2.2.2.RELEASE.jar;D:\X\dlm_github\shenyu\shenyu-examples\shenyu-examples-sofa\shenyu-examples-sofa-api\target\classes;D:\SOFT\m2\repository\org\projectlombok\lombok\1.18.10\lombok-1.18.10.jar;D:\X\dlm_github\shenyu\shenyu-spring-boot-starter\shenyu-spring-boot-starter-client\shenyu-spring-boot-starter-client-sofa\target\classes;D:\SOFT\m2\repository\org\springframework\boot\spring-boot-starter\2.2.2.RELEASE\spring-boot-starter-2.2.2.RELEASE.jar;D:\SOFT\m2\repository\org\springframework\boot\spring-boot-starter-logging\2.2.2.RELEASE\spring-boot-starter-logging-2.2.2.RELEASE.jar;D:\SOFT\m2\repository\ch\qos\logback\logback-classic\1.2.3\logback-classic-1.2.3.jar;D:\SOFT\m2\repository\ch\qos\logback\logback-core\1.2.3\logback-core-1.2.3.jar;D:\SOFT\m2\repository\org\apache\logging\log4j\log4j-to-slf4j\2.12.1\log4j-to-slf4j-2.12.1.jar;D:\SOFT\m2\repository\org\apache\logging\log4j\log4j-api\2.12.1\log4j-api-2.12.1.jar;D:\SOFT\m2\repository\org\slf4j\jul-to-slf4j\1.7.29\jul-to-slf4j-1.7.29.jar;D:\SOFT\m2\repository\jakarta\annotation\jakarta.annotation-api\1.3.5\jakarta.annotation-api-1.3.5.jar;D:\SOFT\m2\repository\org\yaml\snakeyaml\1.25\snakeyaml-1.25.jar;D:\X\dlm_github\shenyu\shenyu-client\shenyu-client-sofa\target\classes;D:\X\dlm_github\shenyu\shenyu-client\shenyu-client-common\target\classes;D:\X\dlm_github\shenyu\shenyu-common\target\classes;D:\SOFT\m2\repository\org\springframework\boot\spring-boot-starter-json\2.2.2.RELEASE\spring-boot-starter-json-2.2.2.RELEASE.jar;D:\SOFT\m2\repository\org\springframework\spring-web\5.2.2.RELEASE\spring-web-5.2.2.RELEASE.jar;D:\SOFT\m2\repository\com\fasterxml\jackson\datatype\jackson-datatype-jdk8\2.10.1\jackson-datatype-jdk8-2.10.1.jar;D:\SOFT\m2\repository\com\fasterxml\jackson\datatype\jackson-datatype-jsr310\2.10.1\jackson-datatype-jsr310-2.10.1.jar;D:\SOFT\m2\repository\com\fasterxml\jackson\module\jackson-module-parameter-names\2.10.1\jackson-module-parameter-names-2.10.1.jar;D:\SOFT\m2\repository\com\squareup\okhttp3\okhttp\3.14.4\okhttp-3.14.4.jar;D:\SOFT\m2\repository\com\squareup\okio\okio\1.17.2\okio-1.17.2.jar;D:\SOFT\m2\repository\com\google\code\gson\gson\2.8.6\gson-2.8.6.jar;D:\SOFT\m2\repository\org\slf4j\slf4j-api\1.7.29\slf4j-api-1.7.29.jar;D:\SOFT\m2\repository\org\slf4j\jcl-over-slf4j\1.7.29\jcl-over-slf4j-1.7.29.jar;C:\Program Files\JetBrains\IntelliJ IDEA 2019.3.3\lib\idea_rt.jar 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:java.library.path=C:\Program Files\Java\jdk1.8.0_211\bin;C:\Windows\Sun\Java\bin;C:\Windows\system32;C:\Windows;C:\Program Files\Common Files\Oracle\Java\javapath;C:\ProgramData\Oracle\Java\javapath;C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Program Files\Java\jdk1.8.0_211\bin;C:\Program Files\Java\jdk1.8.0_211\jre\bin;D:\SOFT\apache-maven-3.5.0\bin;C:\Program Files\Go\bin;C:\Program Files\nodejs\;C:\Program Files\Python\Python38\;C:\Program Files\OpenSSL-Win64\bin;C:\Program Files\Git\bin;D:\SOFT\protobuf-2.5.0\src;D:\SOFT\zlib-1.2.8;c:\Program Files (x86)\Microsoft SQL Server\100\Tools\Binn\;c:\Program Files\Microsoft SQL Server\100\Tools\Binn\;c:\Program Files\Microsoft SQL Server\100\DTS\Binn\;C:\Program Files\Docker\Docker\resources\bin;C:\ProgramData\DockerDesktop\version-bin;D:\SOFT\gradle-6.0-all\gradle-6.0\bin;C:\Program Files\mingw-w64\x86_64-8.1.0-posix-seh-rt_v6-rev0\mingw64\bin;D:\SOFT\hugo_extended_0.55.5_Windows-64bit;C:\Users\DLM\AppData\Local\Microsoft\WindowsApps;C:\Users\DLM\go\bin;C:\Users\DLM\AppData\Roaming\npm;;C:\Program Files\Microsoft VS Code\bin;C:\Program Files\nimbella-cli\bin;. 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:java.io.tmpdir=C:\Users\DLM\AppData\Local\Temp\ 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:java.compiler=<NA> 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:os.name=Windows 10 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:os.arch=amd64 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:os.version=10.0 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:user.name=DLM 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:user.home=C:\Users\DLM 
2021-02-10 02:31:46.060  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Client environment:user.dir=D:\X\dlm_github\shenyu 
2021-02-10 02:31:46.061  INFO 2156 --- [           main] org.apache.zookeeper.ZooKeeper           : Initiating client connection, connectString=127.0.0.1:21810 sessionTimeout=60000 watcher=org.apache.curator.ConnectionState@3e850122 
2021-02-10 02:31:46.069  INFO 2156 --- [27.0.0.1:21810)] org.apache.zookeeper.ClientCnxn          : Opening socket connection to server 127.0.0.1/127.0.0.1:21810. Will not attempt to authenticate using SASL (unknown error) 
2021-02-10 02:31:46.071  INFO 2156 --- [27.0.0.1:21810)] org.apache.zookeeper.ClientCnxn          : Socket connection established to 127.0.0.1/127.0.0.1:21810, initiating session 
2021-02-10 02:31:46.078  INFO 2156 --- [27.0.0.1:21810)] org.apache.zookeeper.ClientCnxn          : Session establishment complete on server 127.0.0.1/127.0.0.1:21810, sessionid = 0x10005b0d05e0001, negotiated timeout = 40000 
2021-02-10 02:31:46.081  INFO 2156 --- [ain-EventThread] o.a.c.f.state.ConnectionStateManager     : State change: CONNECTED 
2021-02-10 02:31:46.093  WARN 2156 --- [           main] org.apache.curator.utils.ZKPaths         : The version of ZooKeeper being used doesn't support Container nodes. CreateMode.PERSISTENT will be used instead. 
2021-02-10 02:31:46.141  INFO 2156 --- [           main] o.d.s.e.s.service.TestSofaApplication    : Started TestSofaApplication in 3.41 seconds (JVM running for 4.423)  
```

The `shenyu-examples-sofa` project will automatically register interface methods annotated with `@ShenyuSofaClient` in the Apache ShenYu gateway after successful startup.

Open PluginList -> rpc proxy -> sofa to see the list of plugin rule configurations:

![](assets/images/rule-list-8024764d442e91078a69d7618ed7753f_1d15fb7ed18db920.png)

Use PostMan to simulate HTTP to request your Sofa service:

![](assets/images/postman-findbyid-37cef6ac98fe1f4cbb95e83661a214bf_0fa67ae45149e7b2.png)

Complex multi-parameter example: The related interface implementation class is `org.apache.shenyu.examples.sofa.service.impl.SofaMultiParamServiceImpl#batchSaveNameAndId`

```java
@Override 
@ShenyuSofaClient(path = "/batchSaveNameAndId") 
public SofaSimpleTypeBean batchSaveNameAndId(final List<SofaSimpleTypeBean> sofaTestList, final String id, final String name) { 
    SofaSimpleTypeBean simpleTypeBean = new SofaSimpleTypeBean(); 
    simpleTypeBean.setId(id); 
    simpleTypeBean.setName("hello world shenyu sofa param batchSaveAndNameAndId :" + name + ":" + sofaTestList.stream().map(SofaSimpleTypeBean::getName).collect(Collectors.joining("-"))); 
    return simpleTypeBean; 
} 
```

![](assets/images/postman-multiparams-d715abffdf058c90f303406306573056_97a0b16e51b8fd95.png)

---

<a id="quick-start-quick-start-springcloud"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-springcloud/ -->

<!-- page_index: 25 -->

# Quick start with Spring Cloud

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using Spring Cloud. You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-springcloud) .

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the springCloud plugin on in the BasicConfig `->` Plugin.

![](assets/images/springcloud-open-en_10c7c781d3476035.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.

Add the gateway proxy plugin for `Spring Cloud` and add your registry center dependencies:

```xml
<!-- apache shenyu springCloud plugin start--> 
               <dependency> 
                    <groupId>org.apache.shenyu</groupId> 
                    <artifactId>shenyu-spring-boot-starter-plugin-springcloud</artifactId> 
                    <version>${project.version}</version> 
                </dependency> 
 
                <dependency> 
                    <groupId>org.springframework.cloud</groupId> 
                    <artifactId>spring-cloud-commons</artifactId> 
                    <version>2.2.0.RELEASE</version> 
                </dependency> 
 
                <dependency> 
                    <groupId>org.apache.shenyu</groupId> 
                    <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> 
                    <version>${project.version}</version> 
                </dependency> 
        <!-- springCloud if you config register center is eureka please dependency end--> 
                <dependency> 
                    <groupId>org.springframework.cloud</groupId> 
                    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId> 
                    <version>2.2.0.RELEASE</version> 
                </dependency> 
        <!-- apache shenyu springCloud plugin end--> 
```

`eureka` config information:

```yml
eureka: 
  client: 
    serviceUrl: 
      defaultZone: http://localhost:8761/eureka/ 
  instance: 
    prefer-ip-address: true 
```

Note: Please ensure that the spring Cloud registry service discovery configuration is enabled

- Configuration method

```yml
spring: 
  cloud: 
    discovery: 
      enabled: true 
```

- code method

```java
@SpringBootApplication @EnableDiscoveryClient public class ShenyuBootstrapApplication {
/** * Main Entrance.* * @param args startup arguments */ public static void main(final String[] args) {SpringApplication.run(ShenyuBootstrapApplication.class, args);}}
```

Restart the `shenyu-bootstrap` project.

- Currently, the SpringCloudPlugin plugin on Shenyu implements support for service discovery of the registry center. However, it is not possible to dynamically switch the registry center. In order to allow users to use the plugin more clearly and switch the configuration of the registry center more conveniently, shenyu supports developers to configure and switch the registry center on the admin page, thereby reducing the user's usage cost and experience.

Specific operation process:

- Start shenyu-admin
- Start shenyu-bootstrap
- Start the registry center, such as the eureka project under shenyu-examples
- Start shenyu-examples-springcloud under shenyu-examples
- Configure the relevant information of the registry center on the admin system interface and click Confirm

Take the eureka registry center configuration as an example to show how to configure the relevant information of the registry center on the page:

![](assets/images/springcloud-dynamic-register-operate-en_eeac5905a5deb80d.png)

As shown in the figure above, registerType indicates the type of registration center, and the following registration centers are supported:

- eureka
- nacos
- zookeeper
- apollo
- consul
- etcd
- polaris
- kubernetes

serverLists indicates the IP address of the registration center, and props is the additional configuration items for the registration center, such as namespace, username, etc. After clicking OK, eureka is used as the registration center of springCloudPlugin.

In the example project we used `Eureka` as the registry for `Spring Cloud`. You can use the local `Eureka` or the application provided in the example.

Download [shenyu-examples-eureka](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-eureka) 、[shenyu-examples-springcloud](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-springcloud) .

Startup the Eureka service:
Execute the `org.apache.shenyu.examples.eureka.EurekaServerApplication` main method to start project.

Startup the Spring Cloud service:
Execute the `org.apache.shenyu.examples.springcloud.ShenyuTestSpringCloudApplication` main method to start project.

Since `2.4.3`, `shenyu.client.springCloud.props.port` can be non-configured if you like.

The following log appears when the startup is successful:

```shell
2021-02-10 14:03:51.301  INFO 2860 --- [           main] o.s.s.concurrent.ThreadPoolTaskExecutor  : Initializing ExecutorService 'applicationTaskExecutor' 
2021-02-10 14:03:51.669  INFO 2860 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : springCloud client register success: {"appName":"springCloud-test","context":"/springcloud","path":"/springcloud/order/save","pathDesc":"","rpcType":"springCloud","ruleName":"/springcloud/order/save","enabled":true}  
2021-02-10 14:03:51.676  INFO 2860 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : springCloud client register success: {"appName":"springCloud-test","context":"/springcloud","path":"/springcloud/order/path/**","pathDesc":"","rpcType":"springCloud","ruleName":"/springcloud/order/path/**","enabled":true}  
2021-02-10 14:03:51.682  INFO 2860 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : springCloud client register success: {"appName":"springCloud-test","context":"/springcloud","path":"/springcloud/order/findById","pathDesc":"","rpcType":"springCloud","ruleName":"/springcloud/order/findById","enabled":true}  
2021-02-10 14:03:51.688  INFO 2860 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : springCloud client register success: {"appName":"springCloud-test","context":"/springcloud","path":"/springcloud/order/path/**/name","pathDesc":"","rpcType":"springCloud","ruleName":"/springcloud/order/path/**/name","enabled":true}  
2021-02-10 14:03:51.692  INFO 2860 --- [pool-1-thread-1] o.d.s.client.common.utils.RegisterUtils  : springCloud client register success: {"appName":"springCloud-test","context":"/springcloud","path":"/springcloud/test/**","pathDesc":"","rpcType":"springCloud","ruleName":"/springcloud/test/**","enabled":true}  
2021-02-10 14:03:52.806  WARN 2860 --- [           main] ockingLoadBalancerClientRibbonWarnLogger : You already have RibbonLoadBalancerClient on your classpath. It will be used by default. As Spring Cloud Ribbon is in maintenance mode. We recommend switching to BlockingLoadBalancerClient instead. In order to use it, set the value of `spring.cloud.loadbalancer.ribbon.enabled` to `false` or remove spring-cloud-starter-netflix-ribbon from your project. 
2021-02-10 14:03:52.848  WARN 2860 --- [           main] iguration$LoadBalancerCaffeineWarnLogger : Spring Cloud LoadBalancer is currently working with default default cache. You can switch to using Caffeine cache, by adding it to the classpath. 
2021-02-10 14:03:52.921  INFO 2860 --- [           main] o.s.c.n.eureka.InstanceInfoFactory       : Setting initial instance status as: STARTING 
2021-02-10 14:03:52.949  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Initializing Eureka in region us-east-1 
2021-02-10 14:03:53.006  INFO 2860 --- [           main] c.n.d.provider.DiscoveryJerseyProvider   : Using JSON encoding codec LegacyJacksonJson 
2021-02-10 14:03:53.006  INFO 2860 --- [           main] c.n.d.provider.DiscoveryJerseyProvider   : Using JSON decoding codec LegacyJacksonJson 
2021-02-10 14:03:53.110  INFO 2860 --- [           main] c.n.d.provider.DiscoveryJerseyProvider   : Using XML encoding codec XStreamXml 
2021-02-10 14:03:53.110  INFO 2860 --- [           main] c.n.d.provider.DiscoveryJerseyProvider   : Using XML decoding codec XStreamXml 
2021-02-10 14:03:53.263  INFO 2860 --- [           main] c.n.d.s.r.aws.ConfigClusterResolver      : Resolving eureka endpoints via configuration 
2021-02-10 14:03:53.546  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Disable delta property : false 
2021-02-10 14:03:53.546  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Single vip registry refresh property : null 
2021-02-10 14:03:53.547  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Force full registry fetch : false 
2021-02-10 14:03:53.547  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Application is null : false 
2021-02-10 14:03:53.547  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Registered Applications size is zero : true 
2021-02-10 14:03:53.547  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Application version is -1: true 
2021-02-10 14:03:53.547  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Getting all instance registry info from the eureka server 
2021-02-10 14:03:53.754  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : The response status is 200 
2021-02-10 14:03:53.756  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Starting heartbeat executor: renew interval is: 30 
2021-02-10 14:03:53.758  INFO 2860 --- [           main] c.n.discovery.InstanceInfoReplicator     : InstanceInfoReplicator onDemand update allowed rate per min is 4 
2021-02-10 14:03:53.761  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Discovery Client initialized at timestamp 1612937033760 with initial instances count: 0 
2021-02-10 14:03:53.762  INFO 2860 --- [           main] o.s.c.n.e.s.EurekaServiceRegistry        : Registering application SPRINGCLOUD-TEST with eureka with status UP 
2021-02-10 14:03:53.763  INFO 2860 --- [           main] com.netflix.discovery.DiscoveryClient    : Saw local status change event StatusChangeEvent [timestamp=1612937033763, current=UP, previous=STARTING] 
2021-02-10 14:03:53.765  INFO 2860 --- [nfoReplicator-0] com.netflix.discovery.DiscoveryClient    : DiscoveryClient_SPRINGCLOUD-TEST/host.docker.internal:springCloud-test:8884: registering service... 
2021-02-10 14:03:53.805  INFO 2860 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 8884 (http) with context path '' 
2021-02-10 14:03:53.807  INFO 2860 --- [           main] .s.c.n.e.s.EurekaAutoServiceRegistration : Updating port to 8884 
2021-02-10 14:03:53.837  INFO 2860 --- [nfoReplicator-0] com.netflix.discovery.DiscoveryClient    : DiscoveryClient_SPRINGCLOUD-TEST/host.docker.internal:springCloud-test:8884 - registration status: 204 
2021-02-10 14:03:54.231  INFO 2860 --- [           main] o.d.s.e.s.ShenyuTestSpringCloudApplication : Started ShenyuTestSpringCloudApplication in 6.338 seconds (JVM running for 7.361)  
```

The `shenyu-examples-springcloud` project will automatically register interface methods annotated with `@ShenyuSpringCloudClient` in the Apache ShenYu gateway after successful startup.

Open PluginList -> rpc proxy -> springCloud to see the list of plugin rule configurations:

![](assets/images/rule-list-9a66ac71f764e2766fb7880c1811bae2_306f93f563c03c6f.png)

Use PostMan to simulate HTTP to request your SpringCloud service:

![](assets/images/postman-test-1bd985bc5b3dbe25e90f5c01d2ee1094_220e814b38335690.png)

Use IDEA HTTP Client Plugin to simulate HTTP to request your SpringCloud service[local:no Shenyu proxy]:

![](assets/images/idea-http-test-local-bd2ea4b9e8ab5d867edc120e3946e00c_937ed8759cbc350c.png)

Use IDEA HTTP Client Plugin to simulate HTTP to request your SpringCloud service[Shenyu proxy]:

![](assets/images/idea-http-test-proxy-fc83eddb6fa4a74cc790258ac670a8ec_6f525d6738a378e7.png)

---

<a id="quick-start-quick-start-tars"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-tars/ -->

<!-- page_index: 26 -->

# Quick start with Tars

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu Gateway using Tars. You can get the code example of this document by clicking [here](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-tars) .

Please refer to the deployment to select a way to start shenyu-admin. For example, start the Apache ShenYu gateway management system through [local deployment](#deployment-deployment-local) .

After successful startup, you need to open the Sofa plugin on in the BasicConfig `->` Plugin.

![](assets/images/tars-open-en_3ab7d38ce164f49f.png)

If you are a startup gateway by means of source, can be directly run the ShenyuBootstrapApplication of shenyu-bootstrap module.

> Note: Before starting, make sure the gateway has added dependencies.

`shenyu-bootstrap` need to import tars dependencies:

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-tars</artifactId> 
    <version>${project.version}</version> 
</dependency> 
 
<dependency> 
    <groupId>com.tencent.tars</groupId> 
    <artifactId>tars-client</artifactId> 
    <version>1.7.2</version> 
</dependency> 
```

Download [shenyu-examples-tars](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-tars) .

Modify `host` in `application.yml` to be your local IP

Modify config `src/main/resources/ShenyuExampleServer.ShenyuExampleApp.config.conf`:

- It is recommended to make clear the meaning of the main configuration items of config, [refer to the development guide](https://github.com/TarsCloud/TarsJava/blob/master/docs/tars_java_user_guide.md)
- bind IP in config should pay attention to providing cost machine
- local=..., Indicates the open port that the native machine connects to the tarsnode. If there is no tarsnode, this configuration can be dropped
- `locator`: Indicates the address (frame address) of the main control center, which is used to obtain the IP list according to the service name, If Registry is not required to locate the service, this configuration can be dropped
- `node=tars.tarsnode.ServerObj@xxxx`, Indicates the address of the connected tarsnode. If there is no tarsnode locally, this configuration can be removed

More config configuration instructions, Please refer to [TARS Official Documentation](https://github.com/TarsCloud/TarsJava/blob/master/docs/tars_java_user_guide.md)

Execute the `org.apache.shenyu.examples.tars.ShenyuTestTarsApplication` main method to start project.

**Note:** The `configuration file address` needs to be specified in the startup command when the service starts **-Dconfig=xxx/ShenyuExampleServer.ShenyuExampleApp.config.conf**

If the `-Dconfig` parameter is not added, the configuration may throw the following exceptions:

```text
com.qq.tars.server.config.ConfigurationException: error occurred on load server config 
	at com.qq.tars.server.config.ConfigurationManager.loadServerConfig(ConfigurationManager.java:113) 
	at com.qq.tars.server.config.ConfigurationManager.init(ConfigurationManager.java:57) 
	at com.qq.tars.server.core.Server.loadServerConfig(Server.java:90) 
	at com.qq.tars.server.core.Server.<init>(Server.java:42) 
	at com.qq.tars.server.core.Server.<clinit>(Server.java:38) 
	at com.qq.tars.spring.bean.PropertiesListener.onApplicationEvent(PropertiesListener.java:37) 
	at com.qq.tars.spring.bean.PropertiesListener.onApplicationEvent(PropertiesListener.java:31) 
	at org.springframework.context.event.SimpleApplicationEventMulticaster.doInvokeListener(SimpleApplicationEventMulticaster.java:172) 
	at org.springframework.context.event.SimpleApplicationEventMulticaster.invokeListener(SimpleApplicationEventMulticaster.java:165) 
	at org.springframework.context.event.SimpleApplicationEventMulticaster.multicastEvent(SimpleApplicationEventMulticaster.java:139) 
	at org.springframework.context.event.SimpleApplicationEventMulticaster.multicastEvent(SimpleApplicationEventMulticaster.java:127) 
	at org.springframework.boot.context.event.EventPublishingRunListener.environmentPrepared(EventPublishingRunListener.java:76) 
	at org.springframework.boot.SpringApplicationRunListeners.environmentPrepared(SpringApplicationRunListeners.java:53) 
	at org.springframework.boot.SpringApplication.prepareEnvironment(SpringApplication.java:345) 
	at org.springframework.boot.SpringApplication.run(SpringApplication.java:308) 
	at org.springframework.boot.SpringApplication.run(SpringApplication.java:1226) 
	at org.springframework.boot.SpringApplication.run(SpringApplication.java:1215) 
	at org.apache.shenyu.examples.tars.ShenyuTestTarsApplication.main(ShenyuTestTarsApplication.java:38) 
Caused by: java.lang.NullPointerException 
	at java.io.FileInputStream.<init>(FileInputStream.java:130) 
	at java.io.FileInputStream.<init>(FileInputStream.java:93) 
	at com.qq.tars.common.util.Config.parseFile(Config.java:211) 
	at com.qq.tars.server.config.ConfigurationManager.loadServerConfig(ConfigurationManager.java:63) 
	... 17 more 
The exception occurred at load server config 
```

The following log appears when the startup is successful:

```shell
[SERVER] server starting at tcp -h 127.0.0.1 -p 21715 -t 60000... 
[SERVER] server started at tcp -h 127.0.0.1 -p 21715 -t 60000... 
[SERVER] server starting at tcp -h 127.0.0.1 -p 21714 -t 3000... 
[SERVER] server started at tcp -h 127.0.0.1 -p 21714 -t 3000... 
[SERVER] The application started successfully. 
The session manager service started... 
[SERVER] server is ready... 
2021-02-09 13:28:24.643  INFO 16016 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat started on port(s): 55290 (http) with context path '' 
2021-02-09 13:28:24.645  INFO 16016 --- [           main] o.d.s.e.tars.ShenyuTestTarsApplication     : Started ShenyuTestTarsApplication in 4.232 seconds (JVM running for 5.1) 
2021-02-09 13:28:24.828  INFO 16016 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : tars client register success: {"appName":"127.0.0.1:21715","contextPath":"/tars","path":"/tars/helloInt","pathDesc":"","rpcType":"tars","serviceName":"ShenyuExampleServer.ShenyuExampleApp.HelloObj","methodName":"helloInt","ruleName":"/tars/helloInt","parameterTypes":"int,java.lang.String","rpcExt":"{\"methodInfo\":[{\"methodName\":\"helloInt\",\"params\":[{},{}],\"returnType\":\"java.lang.Integer\"},{\"methodName\":\"hello\",\"params\":[{},{}],\"returnType\":\"java.lang.String\"}]}","enabled":true}  
2021-02-09 13:28:24.837  INFO 16016 --- [pool-2-thread-1] o.d.s.client.common.utils.RegisterUtils  : tars client register success: {"appName":"127.0.0.1:21715","contextPath":"/tars","path":"/tars/hello","pathDesc":"","rpcType":"tars","serviceName":"ShenyuExampleServer.ShenyuExampleApp.HelloObj","methodName":"hello","ruleName":"/tars/hello","parameterTypes":"int,java.lang.String","rpcExt":"{\"methodInfo\":[{\"methodName\":\"helloInt\",\"params\":[{},{}],\"returnType\":\"java.lang.Integer\"},{\"methodName\":\"hello\",\"params\":[{},{}],\"returnType\":\"java.lang.String\"}]}","enabled":true}  
```

The `shenyu-examples-tars` project will automatically register interface methods annotated with `@ShenyuTarsClient` in the Apache ShenYu gateway after successful startup.

Open PluginList -> rpc proxy -> tars to see the list of plugin rule configurations:

![](assets/images/rule-list-bb247d24aa2f5e009b4749dd447e9018_f0613d52d8332be4.png)

Use PostMan to simulate HTTP to request your tars service:

![](assets/images/postman-test-71e1f81f98f8a0547421fddce8ae259a_f9362d1fc1da8cd7.png)

---

<a id="quick-start-quick-start-websocket"></a>

<!-- source_url: https://shenyu.apache.org/docs/quick-start/quick-start-websocket/ -->

<!-- page_index: 27 -->

# Quick start with Websocket

Version: 2.7.0.3

This document introduces how to quickly access the Apache ShenYu gateway using Websocket.

> Refer to [local deployment](#deployment-deployment-local) to deploy the Shenyu gateway.

1. Deploy the `shenyu-admin` service.

- After successful launch, you need to set the `Websocket` plugin to be enabled in the page's basic configuration `->`Plugin Management.

![](assets/images/enable-websocket-en_343e6fd4918ce998.png)

2. Deploy the `shenyu-bootstrap` service.

- After starting, `shenyu-bootstrap` will synchronize the data via the `websocket` protocol according to the address configured in `shenyu.sync.websocket.url`.

> Note: Before starting, make sure that the gateway has introduced the relevant dependency, which is introduced by default.

Import the gateway proxy plugin for `Websocket` and add the following dependencies to the gateway's `pom.xml` file.

```xml
        <!--shenyu websocket plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-websocket</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
```

1. Download [shenyu-examples-websocket](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-websocket/shenyu-example-spring-annotation-websocket) (`native-websocket` and `reactive-websocket` can refer to the subprojects under [shenyu-examples-websocket](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-websocket)).
2. Run main method of `org.apache.shenyu.examples.websocket.TestAnnotationWebsocketApplication` to start this project.

- The examples project will synchronize the websocket service information to `shenyu-admin` via the `http` protocol according to the address configured in `shenyu.register.serverLists`, and then to `shenyu-bootstrap` by `shenyu-admin`.

log info as follows after starting:

```shell
2022-08-09 23:37:34.994  INFO 61398 --- [or_consumer_-21] o.a.s.r.client.http.utils.RegisterUtils  : metadata client register success: {"appName":"ws-annotation","contextPath":"/ws-annotation","path":"/ws-annotation/myWs","rpcType":"websocket","ruleName":"/ws-annotation/myWs","enabled":true,"pluginNames":[],"registerMetaData":false,"timeMillis":1660059454701}  
2022-08-09 23:37:35.019  INFO 61398 --- [or_consumer_-18] o.a.s.r.client.http.utils.RegisterUtils  : uri client register success: {"protocol":"ws://","appName":"ws-annotation","contextPath":"/ws-annotation","rpcType":"websocket","host":"192.168.1.3","port":8001}  
```

1. The `shenyu-examples-websocket` project will automatically register the interface methods annotated with `@ShenyuSpringWebSocketClient` to the gateway and add selectors and rules after successful start, you can see the information of `shenyu-examples-websocket` service registration by visiting `shenyu-admin` page -> PluginList -> Proxy -> Websocket to see the `shenyu-examples-websocket` service registration information, if not, you can refer to [Websocket plugin](#plugin-center-proxy-websocket-plugin) to add the configuration manually.

![](assets/images/auto-register-en_f5e633d7c39ed562.png)

2. The following test code (see attachment) simulates the request method of the `Websocket` protocol to request your `Websocket` service.

![](assets/images/test-result-en_db65c30c73ff1c45.png)

**websocket debugging code**

- Create a file called websocket.html and copy the following code into the file.
- Open websocket.html with Chrome.

```html
<!DOCTYPE HTML> 
<html> 
<head> 
    <meta http-equiv="content-type" content="text/html" /> 
    <title>Shenyu WebSocket Test</title> 
    <script> 
        var websocket; 
        function connect() { 
            try { 
                websocket = new WebSocket(document.getElementById("url").value); 
                websocket.onopen = onOpen; 
                websocket.onerror = onError; 
                websocket.onmessage = onReceive; 
                websocket.onclose = onClose; 
            } catch (e) { 
                alert('[websocket] establish connection error.'); 
            } 
        } 
        function onOpen() { 
            alert('[websocket] connect success.'); 
        } 
        function onError(e) { 
            alert("[websocket] connect error. code: " + e.code); 
        } 
        function onReceive(msg) { 
            var show = document.getElementById("show"); 
            show.innerHTML += "[Server Response] => " + msg.data + "<br/>"; 
            show.scrollTop = show.scrollHeight; 
        } 
        function onClose(e) { 
            console.log("[websocket] connect closed. code: " + e.code) 
            alert("[websocket] connect closed."); 
            document.getElementById("show").innerHTML = ""; 
            document.getElementById("msg").value = ""; 
            websocket = null; 
        } 
        function buttonClose() { 
            if (websocket == null) { 
                console.log("Please establish a connection first.") 
            } else { 
                websocket.close(1000); 
                document.getElementById("show").innerHTML = ""; 
                document.getElementById("msg").value = ""; 
            } 
        } 
        function send() { 
            if (websocket == null) { 
                alert("Please establish a connection first.") 
            } else { 
                var msg = document.getElementById("msg").value; 
                show.innerHTML += "[Client Request] => " + msg + "<br/>"; 
                websocket.send(msg); 
            } 
        } 
    </script> 
</head> 
<body> 
    <input id="url" type="text" value="ws://localhost:9195/ws-annotation/myWs"><br /> 
    <input id="msg" type="text"><br /> 
    <button id="connect" onclick="connect();">Connect</button> 
    <button id="send" onclick="send();">Send</button> 
    <button id="close" onclick="buttonClose();">Close</button></br> 
    <div id="show" class="show"></div> 
</body> 
</html> 
<style> 
    input { 
        width: 400px; 
        margin-bottom: 10px; 
    } 
    .show { 
        width: 600px; 
        height: 400px; 
        overflow-y: auto; 
        border: 1px solid #333; 
        margin-top: 10px; 
    } 
</style> 
```

---

<a id="user-guide-admin-usage-api-document"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/admin-usage/api-document/ -->

<!-- page_index: 28 -->

# API Document Management

Version: 2.7.0.3

When the front and back end are jointly debugged, it is usually necessary for the back end to give documents to detail the input and output of the interface;

After the backend development is complete, you need to test whether the access gateway is successful.

In order to reduce the sense of fragmentation and improve the user experience of front-end and back-end development, it is necessary to see the API documentation in shenyu-admin and test the API directly.

The brief introduce is as follows.

- Back-end development produces API documents in shenyu-admin.

> Three methods of `remotely pulling swagger`, `manual filling`, and `client registration` are already supported. From the perspective of functional integrity and user experience, `remotely pulling swagger` is currently recommended, and the latter two methods will be in Continuous function enhancement in later versions.

- The frontend looks at the API documentation in shenyu-admin and starts development.

> During joint debugging, developers (including front-end and backend) may use the testing function in shenyu-admin to request APIs directly.

In actual use, you may have multiple gateway addresses (such as production environment, test environment, or public network environment, intranet environment), you can manage them in `Apache ShenYu` Gateway Management System --> BasicConfig --> Dictionary, Set multiple gateway addresses.

![apidoc-env-en](assets/images/apidoc-env-en-3c165e72cf46ab2a29de2e601380faa8_82b356c436517a9b.png)

> DictionaryType: Fill in the value must be `apidocEnv`;
>
> DictionaryCode: The identifier of the gateway address has no actual meaning. It is recommended to use `ENV_LABEL_` as a prefix, such as `ENV_LABEL_OFFLINE`;
>
> DictionaryName: Indicates the gateway type, such as filling in `test environment`, `production environment`. This value will appear on the API documentation details page;
>
> DictionaryValue: Indicates the gateway address, such as <http://127.0.0.1:9195>. This value will appear on the API documentation details page;
>
> DictionaryDescribe: Give a brief description of what scenario the gateway address is used for. This value will appear on the API documentation details page;
>
> Sort: The numerical value determines the display order of the gateway address;
>
> Status: open or close。

Clicking the menu "Document -> API Document" to create api.

If you have not created a project or you want to classify the new API into a new project, you need to create a project.

![app-create-en](assets/images/app-create-en-2aec5583662b2417491b20f2285a30e8_b9a493ca561d82cf.png)

![create-api-en](assets/images/create-api-en-39b874a6b163dfaaac45cf56d80bd7f7_2bff85b62a7036e7.png)

Automatically register API documentation by remotely pulling swager documentation. Please refer to [Remote pull swagger registration API document](#user-guide-api-doc-swagger-apidoc)

Automatically register API documents through Shenyu client annotations. Please refer to [Client Registration API Documentation](#user-guide-api-doc-shenyu-annotation-apidoc)

> This method is recommended if you do not expect to view the full interface documentation details. When you choose this automatic registration method, please turn off the registration method of remote automatic pull swagger, otherwise there will be conflicts.

If the API has never been published and the user has not used the shenyu-client, shenyu-admin will automatically expose the API described in the API document to the gateway.

![publish-api-en](assets/images/publish-api-en-d234f19ac872e8fd384cdf7229a774b8_775f3c09cb235aff.png)

After clicking Save, you'll see that the registration data for the API is inserted below the selectors and rules. As shown below:

![api-published-divide-list-en](assets/images/api-published-divide-list-en-9083836b32186bd63352c7363e88deb4_e569075c621fcfbc.png)

> Special Note: After clicking Offline, the API will still be visible in the API document list, but it will be deleted from the proxy plug-in and metadata management list. Before you republish the API, the gateway will not proxy the API. When you pass through the gateway When requesting this API, an exception will be reported.

![offline-api-en](assets/images/offline-api-en-6c6b5ac7404acc5e0d332ce8ececbd51_f53b7dfe3eb315a3.png)

![api-debug-en](assets/images/api-debug-en-9570194643e76ab71558d4030a16b398_a46bd53e4fef6cf1.png)

---

<a id="user-guide-admin-usage-data-permission"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/admin-usage/data-permission/ -->

<!-- page_index: 29 -->

# Data Permission Management

Version: 2.7.0.3

In order to achieve the different selector / rule represented by the plugin managed by different business units, the need for the plugin selector / rule data security for the user to control
When the user does not configure data permissions, it has all the data permissions, as long as the permissions are configured, the data permissions will be controlled. As shown in the following picture.

![](assets/images/data-permission-profile-en_fcf16c9fd745d4f8.png)

The Brief introduce is as follows.

- Users with administrative user resouce permissions (including the admin user) create a new user.
- Users with administrative user data resouce permissions (including admin user) click `ConfigureDataPermission` to manage the user's data permissions.

> Make sure the data exists in the plugin list before doing so. If not, you will have any data to configure.

Now, let's look how to operation step by step:

Clicking the menu "System Manage -> User" to create user, like this:

![](assets/images/create-new-user-en_f8981578798bef10.png)

Adding data in the plugin list, this article uses `divide` as an example, like:

![](assets/images/plugin-data-en_72e3592798cbf6e3.png)

Giving the `divide` plugin permission to the `default` role.

![](assets/images/role-permission-setting-en_468255a37ea7028c.png)

The `default` role has none permissions.The user can't login who we set `default` role to. So we must edit the permissions.

When we create the common users, we can edit data permissions by the `ConfigureDataPermission` button.

![](assets/images/data-permission-en_ff7624ecbb65d3ca.png)

The datas in this list are the same as the plugin list.

When the user login, he just can see the data given to him.

![](assets/images/new-user-login-en_df0b038f0a6b1000.png)

---

<a id="user-guide-admin-usage-dictionary-management"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/admin-usage/dictionary-management/ -->

<!-- page_index: 30 -->

# Dictionary Management

Version: 2.7.0.3

This document will introduce the use of dictionary management in the Apache ShenYu background management system. Dictionary management is primarily used to maintain and manage common data dictionaries.

Please refer to the `deployment` document, choose a way to start `shenyu-admin`. For example, [local deployment](#deployment-deployment-local). After startup, visit `http://localhost:9095`, the default username and password are: `admin` and `123456` .

The current usage scenario is in the [pluginHandle](#user-guide-admin-usage-plugin-handle-explanation), when the data type is selected as the `dropdown`:

![](assets/images/dictionary-pluginhandle-config-en_e087a8649024e254.jpg)

In dictionary management, you can add dictionary types for other places:

![](assets/images/dictionary-config-en_20a7e786fcf60770.jpg)

- DictionaryType: The field name used in the `pluginHandle` .
- DictionaryCode: Identify dictionary data.
- DictionaryName: The name of the `handle` field when adding plugins, selectors or rules.
- DictionaryValue: The actual value of the dictionary data.
- DictionaryDescribe: Description.
- Sort: Dictionary data order.

e.g. `degradeRuleGrade` is one of fields of Sentinel's `handle` json. When it adds rules, it automatically looks up all the general dictionaries of `type='degradeRuleGrade'` in the `shenyu_dict` table as a select-box when you edit the General rules field.

![](assets/images/dictionary-add-rule-en_8433497ae5191ce6.jpg)

---

<a id="user-guide-admin-usage-namepsace"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/admin-usage/namepsace/ -->

<!-- page_index: 31 -->

# Namespace Management

Version: 2.7.0.3

Currently, when managing gateways for different business line needs, multiple sets of ShenYu Admin and ShenYu Gateway are often deployed simultaneously. To ensure data independence, each gateway usually connects to only one ShenYu Admin. However, this architecture increases user and operational costs. To provide a more convenient user experience, ShenYu Admin introduces namespaces for data isolation, allowing management of gateway data across different business lines with just one set of ShenYu Admin and ShenYu Bootstrap services.

Note: To facilitate usage, a default namespace already exists in the system; please do not manually delete the default namespace records in the database.

Users log into the ShenYu Admin backend and select 【Basic Config - Namespace】.

![](assets/images/namespace-manager-en_0bc6c9e910ad924c.png)

In the namespace management module, click Add Data to create a new namespace. Simply fill in the 【Name】 and 【Description】 fields; the system will automatically generate a namespaceId.

![](assets/images/namespace-add-en_7a69dbb73fae73f8.png)

After successful creation, a unique namespaceId will be automatically generated.

![](assets/images/namespace-id-en_20fb268db7c94176.png)

Once you have the namespaceId, you can configure it in the downstream services (already integrated with shenyu-client) in the configuration file to use one or more namespaceIds.(Multiple namespaceIds should be separated by “;”)

![](assets/images/namespace-shenyu-client_be30479efc68b1d4.png)

Once data from Shenyu-client is registered under the specified namespace in Shenyu-admin, the backend management supports isolated gateway data. Users can switch between different namespaces for operations via the button in the upper right corner.

![](assets/images/namespace-divide-en_c026d505eae5671e.png)

Note: A gateway can only bind to a single unique namespaceId

![](assets/images/namespace-bootstrap_3d1673d7ecb6a00a.png)

The plugin group under a new namespace is empty by default. To add a plugin to a namespace, you first need to select the option to generate it under the specific namespace in the plugin template.

Choose 【PluginTemplate】-【Generate】-【Select Target Namespace】

![](assets/images/namespace-generate-plugin-en_664033d556262275.png)

Switch namespaces via the component in the top-right corner.

![](assets/images/namespace-change-en_c81bc330e927073a.png)

This allows you to manage the plugin status within the current namespace.

![](assets/images/namespace-new-plugin-en_023d2ca7b755bc45.png)

Pages that display the namespace switch component in the top-right corner support namespace isolation. By switching namespaces via the component, you can manage gateway data for a specific namespace.

![](assets/images/namespace-other-data-en_3ee6745f9e43ec04.png)

---

<a id="user-guide-admin-usage-plugin-handle-explanation"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/admin-usage/plugin-handle-explanation/ -->

<!-- page_index: 32 -->

# Plugin Config

Version: 2.7.0.3

This document will introduce the use of plugins in the `shenyu-admin` , including plugin management and plugin handle management.

Please refer to the `deployment` document, choose a way to start `shenyu-admin`. For example, [local deployment](#deployment-deployment-local). After startup, visit `http://localhost:9095`, the default username and password are: `admin` and `123456` .

In the plugin management, you can manage all plugins in a unified manner, such as turning off or turning on plugins:

![](assets/images/plugin-open-en_b544bfd89d88fab0.jpg)

You can also set configuration information for some plugins, such as setting a registry for `Dubbo` plugin:

![](assets/images/plugin-config-en_67ce97ef54d6bd9d.jpg)

In plugin handle management, you can add `handle` fields to plugin, selector, and rule.

For example, add a string type field `path` and a digital type field `timeout` to the rule list of the `SpringCloud` plugin.

1. add/edit the `handle` field in the `shenyu-admin`-> BasicConfig -> PluginHandle :

![](assets/images/plugin-handle-field-config-en_672cd118eeb7929b.jpg)

2. Fill in the field information:

![](assets/images/plugin-handle-add-en_698a8403adfe1ada.jpg)

- PluginName: Drop down to select which plugin needs to add the `handle` field.
- Field: Add the name of the field.
- Describe: Field description.
- DataType: Field data type.
  - If the `DropDown` is selected, the drop-down selection of the input box on the rule addition page is to go to the dictionary table to find all the available options through the field name to select, so you need to config the selection in [Dictionary Management](#user-guide-admin-usage-dictionary-management).
- FieldType: This field belongs to selector, rule or plugin.
- Sort: Sequence number.
- Required: Is this field required.
- DefaultValue: Specify a default value for this field.
- Placeholder: The message that appears when the user fills in the field.
- Rule (RegExp): The verification rule when the user fills in the field。

3. When adding a rule in the PluginList -> rpc proxy -> `SpringCloud` -> you can enter `path` and `timeout` :

![](assets/images/plugin-handle-setting-plugin-rule-en_f922b92ac6dfeb99.jpg)

---

<a id="user-guide-admin-usage-role-management"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/admin-usage/role-management/ -->

<!-- page_index: 33 -->

# Role Management

Version: 2.7.0.3

This article focuses on the `admin` console to manage `admin` operation permissions through user-associated roles, roles that give permissions to resources such as menus and buttons.

![](assets/images/role-profile-en_faa862f0c916b237.jpg)

Add Menus and Buttons Resource in "System Manage >> Resouce".

![](assets/images/resource-dashboard-en_3d19f2950410e6ae.png)

The admin user shows all menus and buttons of the `Shenyu` gateway. If you need to customize adding and removing, add the menu first and under the corresponding menu, add the button. Edit the menu by clicking on the small edit icon on the right side of the menu.

You can associate roles and resource permissions through the menu bar "System Administration >> Role Management". By default, two roles are created, one for super administrator and one for normal user. The super administrator is the admin user, which cannot be changed, and the normal user role can change its resource properties. By editing the corresponding role, you can give the role the appropriate menu and button permissions.

You can manage the users logged into admin through the menu bar "System Administration >> User Management". The default user is admin, which has all menu and data permissions, cannot be changed or deleted, and can only change password or username.
You can add a user by pressing the "Add Data" button. The user role is selected to manage the menu and button permissions that the user sees after logging in. When a user selects more than one role, the maximum set of all roles is taken together. After changing a user's role permissions, users who are already logged in can simply refresh the page to get the changed permissions.

The following is an example of how the new user's permissions.

- editor default user role permission

![](assets/images/default-role-en_d11cdda521332897.png)

- Add new roles and give the appropriate resource permissions

![](assets/images/default2-role-en_e80a03661ce41bb7.png)

- Create new users and give them the appropriate roles

![](assets/images/add-new-user-en_79357896bf39d495.png)

- User login to view their menu and button permissions

![](assets/images/new-login-en_851f8874366264d5.png)

---

<a id="user-guide-admin-usage-selector-and-rule"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/admin-usage/selector-and-rule/ -->

<!-- page_index: 34 -->

# Selector And Rule Config

Version: 2.7.0.3

This document will introduce the use of selectors and rules in the Apache ShenYu background management system. For the concept and design of selectors and rules, please refer to `Flow Control`.

![](assets/images/flow-control-en_a3367622666212c7.png)

Please refer to the `deployment` document, choose a way to start `shenyu-admin`. For example, [local deployment](#deployment-deployment-local). After startup, visit `http://localhost:9095`, the default username and password are: `admin` and `123456` .

All plugins are displayed in the PluginList, and selectors and rules can be added to each plugin:

![](assets/images/selector-rule-page-en_e286ee27e24c8444.jpg)

For example, add a selector to the `divide` plugin:

![](assets/images/divide-selector-config-en_e2e8d49403dd4214.jpg)

- selector detailed explanation：

  - Name: create your selector with a distinguish name.
  - Type: Choose request matching strategy.
    - `custom`: Only handle requests that meet the following matching conditions.
    - `full`: Handle all requests.
  - MatchType: Condition combination type.
    - `and`： Need to meet all conditions.
    - `or`: Meet any of the conditions.
  - Conditions：
    - uri: filter request with uri.
    - header: filter request with request header.
    - query: filter request with query string.
    - ip: filter request with your real ip.
    - host: filter request with your real host.
    - post: not recommend to use.
    - cookie: filter request with cookie.
    - req\_method: filter request with request method.
    - condition match:
      - match : fuzzy string matching，recommend to combine with uri，support path-matching.（/test/\*\*).
      - = : matches only if they are equal.
      - regEx : regex matching，match characters in regex expression.
      - contains: when it contains the specified value, it matches.
      - TimeBefore: before the specified time.
      - TimeAfter: after the specified time.
      - exclude: the inverse of the method of `match`.
      - startsWith: when its prefix is equal to the specified value, it matches. In certain scenarios, `match` can be replaced (such as `/test/` instead of `/test/**`) for better performance.
      - endsWith: when its suffix is equal to the specified value, it matches.
      - pathPattern: it's an optimized version of `match`, which has better performance than `match`, but does not support writing `**` in the middle of the path (such as `/api/**/xxx`).
  - Continued: whether the subsequent selector is still executed.
  - PrintLogs: it will print the matching log with the open option enabled.
  - Enable: whether to enable the plugin.
  - Order：the smaller will have high priority to execute among multi-selectors.
  - Handler: The `handle` field, configured in [Plugin handle management](#user-guide-admin-usage-plugin-handle-explanation). Its purpose is to determine the actions to take when the request matches this selector. Within the selector, the `handle` field is often used to represent a manually maintained list of service instances. Each service instance includes the following fields:
    - `host`: Host address
    - `ip:port`: IP+port address
    - `protocol`: Protocol
    - `weight`: Weight of the service instance
    - `warmupTime`: Service warm-up time
    - `startupTime`: Service startup time
    - `status`: true indicates the service node is available, false indicates it is not available

>
> [!NOTE]
> : For plugins that incorporate service discovery modules (such as the Divide plugin, Grpc plugin, and WebSocket plugin), the selector page does not display the handler (i.e., the `handle` field). Instead, it is manually managed through the `Service Discovery` tab under local mode. See [Discovery Module](#user-guide-discovery-discovery-mode) for details.

- the above picture means: when the prefix of the request uri is `/http`, it will redirect to this service `127.0.0.1:8080`.
- selector advice : combine `uri` condition and `startsWith` prefix（/contextPath/）as the first request filter.
- selector(the same for rule) match condition fuzzy string matching rule:
  - `?` matches one character
  - `*` matches zero or more characters
  - `**` matches zero or more directories in a path

![](assets/images/plugin-rule-config-en_0f2c50a0b7e8e09d.jpg)

- when the request was passed by the selector, then it will be processed by the rule, the final filter.
- rule is the final confirmation about how to execute request logically.
- rule detailed explanation：
  - Name：create your rule with a distinguish name.
  - MatchType: you can combine these conditions with 'and' , 'or' operators.
  - Conditions：

    - uri: filter request with uri.
    - header: filter request with request header.
    - query: filter request with query string.
    - ip: filter request with your real ip.
    - host: filter request with your real host.
    - post: not recommend to use.
    - cookie: filter request with cookie.
    - req\_method: filter request with request method.
    - condition match:

      - match : fuzzy string matching，recommend to combine with uri，support path-matching.（/test/\*\*).
      - = : matches only if they are equal.
      - regEx : regex matching，match characters in regex expression.
      - contains: when it contains the specified value, it matches.
      - TimeBefore: before the specified time.
      - TimeAfter: after the specified time.
      - exclude: Same function as `match`, flow selection is opposite.
      - startsWith: when its prefix is equal to the specified value, it matches. In certain scenarios, `match` can be replaced (such as `/test/` instead of `/test/**`) for better performance.
      - endsWith: when its suffix is equal to the specified value, it matches.
      - pathPattern: it's an optimized version of `match`, which has better performance than `match`, but does not support writing `**` in the middle of the path (such as `/api/**/xxx`).
  - PrintLogs: it will print the matching log with the open option enabled.
  - Enable: whether to enable the plugin.
  - Order：the smaller will have high priority to execute among multi-rules.
  - handle: The operation when the request matches the rule.
- above picture means: when the request `uri` equals to `/http/order/save`, it will execute based on this rule，load strategy is `random`.
- rule advice: combine `uri` condition with `match` the real `uri path` condition as the final filter.
- combine selector means ：when the request `uri` is `/http/order/save`, it will be redicted to `127.0.0.1:8080` by `random` method.

Matching mode refers to the matching mode between multiple conditions when a selector or rule is matched. Currently, `and` and `or` are supported.

- `and`

  `and` indicates that a selector or rule can be matched only if more than one condition is met.

  The example below shows that a request must meet both the condition `uri = /http/order/findById` and the condition `id = 100` to match this rule.

  For example, a real request `http://localhost:9195/http/order/findById?id=100` satisfies both conditions, this rule can be matched.

![](assets/images/match-strategy-and-en-3dc5ce5d8c0bc56e60b51e0f6abd12bd_9b727cef4f23fc6e.png)

- `or`

  `or` indicates that one of the conditions matches a selector or rule.

  The example below shows that a request matches this rule if it meets either the condition `uri = /http/order/findById` or the condition `id = 100`.

  For example, a real request `http://localhost:9195/http/order/findById?id=99` satisfies the first condition `uri = /http/order/findById`, so it can also match this rule.

![](assets/images/match-strategy-or-en-a9b2dc0ee90d0532004ef7f0defad516_3ab61e1cde624de6.png)

Conditional parameter Settings in selectors and rules are explained again. Suppose the following is a request header for an `Http` request:

```shell
GET http://localhost:9195/http/order/findById?id=100 
Accept: application/json 
Cookie: shenyu=shenyu_cookie 
MyHeader: custom-header 
```

In `ShenYu` you can set different conditional parameters to get real data from the request information.

- If the condition parameter is `uri`, then the actual data retrieved is `/http/order/findById`;
- If the condition parameter is `header`, the field name is `MyHeader`, then the actual data retrieved is `custom-header`;
- If the condition parameter is `query`, the field name is `id`, then the actual data retrieved is `100`;
- If the condition parameter is `ip`, then the actual data retrieved is `0:0:0:0:0:0:0:1`;
- If the condition parameter is `host`, then the actual data retrieved is `0:0:0:0:0:0:0:1`;
- If the condition parameter is `post`, the field name is `contextPath`, then the actual data retrieved is `/http`;
- If the condition parameter is `cookie`, the field name is `shenyu`, then the actual data retrieved is `shenyu_cookie`;
- If the condition parameter is `req_method`, then the actual data retrieved is `GET`;

- `uri`(recommended)

  - `uri` matches are based on the `uri` in the path you requested, and there is almost no change in the front end when accessing the gateway.
  - When using `match`, the principle is the same as `SpringMVC` fuzzy matching.
  - In selectors, it is recommended to use prefixes in `URI` for matching, while in rules, specific paths are used for matching.
  - When using this matching method, fill in the value of the matching field, as shown in the figure `/http/**`.

  ![](assets/images/parameter-data-uri-en-8106039033485e12adc70d751e4ba81b_8fb17bd7c4e1c221.png)
- `header`

  - The `header` is matched against the field values in your `http` request header.
  - When using this matching method, you need to fill in the field name and field value. The examples in the figure are `MyHeader` and `custom-header` respectively

  ![](assets/images/parameter-data-header-en-2d7350e606875425ba7000a63f60bae4_bbf4c5ecf8ee6906.png)
- `query`

  - This matches the query parameters in your `uri`, such as `/test?id=1`, then the matching method can be selected.
  - When using this matching method, you need to fill in the field name and field value. The examples in the figure are `id` and 1 respectively.

  ![](assets/images/parameter-data-query-en-ae199d298b7d11fb67e656e2c84c7d15_0bcc0bfbb8c76115.png)
- `ip`

  - This is matched against the `http` caller's `ip`.
  - Especially in waf plugin, if an `ip` address is found to be attacked, you can add a matching condition, fill in the `ip`, deny the `ip` access.
  - If you use nginx proxy before ShenYu, you can get the right ip with refering to [parsing-ip-and-host](#developer-custom-parsing-ip-and-host)
  - When using this matching method, fill in the value of the matching field, as shown in the example `192.168.236.75`.

  ![](assets/images/parameter-data-ip-en-24cba6d24a6946934d4cae32b8c25520_aa646960d8574b28.png)
- `host`

  - This is matched against the `http` caller's `host`.
  - Especially in waf plugin, if an `host` address is found to be attacked, you can add a matching condition, fill in the `host`, deny the `host` access.
  - If you use nginx proxy before ShenYu, you can get the right ip with refering to [parsing-ip-and-host](#developer-custom-parsing-ip-and-host)
  - When using this matching method, fill in the value of the matching field, as shown in the example `localhost`.

  ![](assets/images/parameter-data-host-en-e602968ecae139d1fd003b2088d93954_7c748922313fbf6f.png)
- `post`

  - To get condition parameters from the request context(`org.apache.shenyu.plugin.api.context.ShenyuContext`), reflection is required to get the value of the field, which is not recommended.
  - When using this matching method, the field name and value need to be specified. The examples in the figure are `contextPath` and `/http` respectively.

  ![](assets/images/parameter-data-post-en-64c4fa2226342bdbfcc7e1110e7375da_7f0ad3cc879290f9.png)
- `cookie`

  - This is matched against the `Cookie` in the `http` caller's request header as a condition parameter.
  - When using this matching method, you need to fill in the field name and field value. The examples in the figure are `shenyu` and `shenyu_cookie` respectively.

  ![](assets/images/parameter-data-cookie-en-d4f494e4ff70a1029c64946c0fc6d3be_d5c1e5c0f5c80651.png)
- `req_method`

  - This matches the request form of the `http` caller, such as `GET`, `POST`, etc.
  - When using this matching method, fill in the value of the matching field, as shown in the example `GET`.

  ![](assets/images/parameter-data-req-method-en-0dcbf034ad9d7e94df26cfbf09534f2d_213c58ac4b86f6b7.png)

For a more in-depth understanding of condition parameter fetching, read the source code, package name is `org.apache.shenyu.plugin.base.condition.data`:

| Condition Parameter | Class |
| --- | --- |
| `uri` | `URIParameterData` |
| `header` | `HeaderParameterData` |
| `query` | `QueryParameterData` |
| `ip` | `IpParameterData` |
| `host` | `HostParameterData` |
| `post` | `PostParameterData` |
| `cookie` | `CookieParameterData` |
| `req_method` | `RequestMethodParameterData` |

Condition parameters allow you to retrieve the actual data of the request. How the real data matches the conditional data preset by the selector or rule is realized through the condition match strategy.

- `match`

  `match` supports fuzzy matching (`/**`). Request `/http/order/findById` will match if your selector condition is set as follows.

  ![](assets/images/predicate-judge-match-en-bfda0697b6762102f2a40f375d1be44b_eca15f05eac6abdc.png)
- `=`

  `=` means that the requested real data is equal to the preset condition data. If your selector condition is set to request uri equal to `/http/order/findById`, then request`/http/order/findById?id=1` can match it.

  ![](assets/images/predicate-judge-equals-en-a9e1c88ebd6b0c4e109ac6e030fb1b35_240eaa32e1b1db8c.png)
- `regex`

  `regex` means that the requested real data can meet the preset condition of the regular expression to match successfully. Suppose your rule conditions are sets as follows: the request parameter contains an `id` and is a three-digit number. So request `/http/order/findById?id=900` will match.

  ![](assets/images/predicate-judge-regex-en-079903a9d60961830e37eab69821e0f7_61b4ffd791723406.png)
- `contains`

  `contains` means that the requested real data contains the default condition data. Suppose your rule condition is set as follows: request uri contains `findById`. Request `/http/order/findById?id=1` will match.

  ![](assets/images/predicate-judge-contains-en-b23ef6d367776827239d836ef55e1fd6_25918d2f4fdcc9d4.png)
- `TimeBefore`

  `TimeBefore` indicates that the request time will be matched before the preset condition time. Suppose your rule conditions are sets as follows: request parameters contain `date` and `date` is less than `2021-09-26 06:12:10`. Request `/http/order/findById?id=100&date=2021-09-22 06:12:10` will match.

  ![](assets/images/predicate-judge-timebefore-en-56c335cbe779dd1e56760a3d8c13ab94_e7f5aeca60c53f0c.png)
- `TimeAfter`

  `TimeAfter` indicates that the request time will be matched before the preset condition time. Suppose your rule conditions are sets as follows: request parameters contain `date` and `date` is greater than `2021-09-26 06:12:10`. Request `/http/order/findById?id=100&date=2021-09-22 06:12:10` will match.

  ![](assets/images/predicate-judge-timeafter-en-c3a68a43426d513363d677dd6d1f5f44_441bacbb368ebf77.png)
- `exclude`

  `exclude` is the inverse of the method of `match`, and some functions of `match` are also available, but it is a matching filter. If your selector condition is set as follows, the request `/http/order/findById` will filter this.

  ![](assets/images/predicate-judge-exclude-en-1715ee844304c48941ba38af56ea5f03_f8d5836c8b20f021.png)
- `startsWith`

  `startsWith` indicates that the prefix of the requested real data is equal to the preset condition data. Suppose your rule conditions are sets as follows: the prefix in the request `uri` is equal to `/http/`, the request `/http/order/findById?id=1` can be matched.

  ![](assets/images/predicate-judge-startswith-en-b2cca14e882a7608e314fbe0c0fdfbe0_b2f27cd5bdce09ae.png)
- `endsWith`

  `endsWith` indicates that the suffix of the requested real data is equal to the preset condition data. Suppose your rule conditions are sets as follows: request `uri` suffix equals `Id`. Then the request `/http/order/findById?id=1` can be matched.

  ![](assets/images/predicate-judge-endswith-en-6da555605e5eebba2895ab8ee3f22b9d_3fd6d6f463b74eba.png)
- `pathPattern`

  Like `match`, `pathPattern` supports fuzzy matching (`/**`). If your rule conditions are sets as follows, then the request `/http/order/findById` can be matched;

  Notice: writing `**` in the middle of the path (such as `/api/**/xxx`) is not supported!

  ![](assets/images/predicate-judge-pathpattern-en-caac10533eaa86164bfcfb75d0c9f3a5_f7b3ad2f91dc9b63.png)

If you want to further understand conditions matching strategy, please read the source code, the package name is `org.apache.shenyu.plugin.base.condition.judge`:

| Match Strategy | Class |
| --- | --- |
| `match` | `MatchPredicateJudge` |
| `=` | `EqualsPredicateJudge` |
| `regex` | `RegexPredicateJudge` |
| `contains` | `ContainsPredicateJudge` |
| `TimeBefore` | `TimerBeforePredicateJudge` |
| `TimeAfter` | `TimerAfterPredicateJudge` |
| `exclude` | `ExcludePredicateJudge` |
| `startsWith` | `StartsWithPredicateJudge` |
| `endsWith` | `EndsWithPredicateJudge` |
| `pathPattern` | `PathPatternPredicateJudge` |

The examples in this article illustrate the use of selectors and rules. The Settings of specific conditions need to be selected according to actual conditions.

---

<a id="user-guide-property-config-admin-property-config"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/property-config/admin-property-config/ -->

<!-- page_index: 35 -->

# Admin Property Config

Version: 2.7.0.3

This paper mainly explains how to configure Apache ShenYu properties on the admin side.

![](assets/images/shenyu-admin-application-config_008371d98c8ad214.png)

```yaml
shenyu: 
  register: 
    registerType: http #http #zookeeper #etcd #nacos #consul 
    serverLists: #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      sessionTimeout: 5000 
      connectionTimeout: 2000 
      checked: true 
      zombieCheckTimes: 5 
      scheduledTime: 10 
      nacosNameSpace: ShenyuRegisterCenter 
  sync: 
    websocket: 
      enabled: true 
      messageMaxSize: 10240 
      allowOrigins: ws://localhost:9095;ws://localhost:9195; 
#      zookeeper: 
#        url: localhost:2181 
#        sessionTimeout: 5000 
#        connectionTimeout: 2000 
#      http: 
#        enabled: true 
#      nacos: 
#        url: localhost:8848 
#        namespace: 1c10d748-af86-43b9-8265-75f487d20c6c 
#        username: 
#        password: 
#        acm: 
#          enabled: false 
#          endpoint: acm.aliyun.com 
#          namespace: 
#          accessKey: 
#          secretKey: 
#    etcd: 
#      url: http://localhost:2379 
#    consul: 
#      url: http://localhost:8500 
  aes: 
    secret: 
      key: 2095132720951327 
      iv: 6075877187097700 
  ldap: 
    enabled: false 
    url: ldap://xxxx:xxx 
    bind-dn: cn=xxx,dc=xxx,dc=xxx 
    password: xxxx 
    base-dn: ou=xxx,dc=xxx,dc=xxx 
    object-class: person 
    login-field: cn 
  jwt: 
    expired-seconds: 86400000 
  shiro: 
    white-list: 
      - / 
      - /favicon.* 
      - /static/** 
      - /index** 
      - /plugin 
      - /platform/** 
      - /websocket 
      - /configs/** 
      - /shenyu-client/** 
      - /error 
      - /actuator/health 
      - /swagger-ui.html 
      - /webjars/** 
      - /swagger-resources/** 
      - /v2/api-docs 
      - /csrf 
  swagger: 
    enable: true 
```

This section describes configurations related to client access. For details about client access principles, see: [Application Client Access](#design-register-center-design) , for client access configuration, see: [Application Client Access Config](https://shenyu.apache.org/docs/next/user-guide/property-config/register-center-access) .

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| registerType | String | http | Yes | Which mode to use for registry. Currently, http, zookeeper, etcd, consul and nacos are supported. |
| serverLists | String | null | No | Configure the address of the registry. If `http` is used, you do not need to enter this parameter. In clustering, multiple addresses are separated by commas (,). |
| props |  |  |  | The value of the property varies according to the registerType. |

- `props` config

The value of the attribute varies according to the registerType.

When the registerType is `http`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| checked | boolean | false | No | is checked |
| zombieCheckTimes | int | 5 | No | how many times does it fail to detect the service. |
| scheduledTime | int | 10 | No | timed detection interval time |

When the registerType is `zookeeper`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| sessionTimeout | int | 30000 | No | session timeout(millisecond) |
| connectionTimeout | int | 3000 | No | connection timeout(millisecond) |

When the registerType is `etcd`, no properties are provided for the time being.

When the registerType is `nacos`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| nacosNameSpace | String | null | Yes | namespace |
| username | String | "" | No | username |
| password | String | "" | No | password |
| accessKey | String | "" | No | accessKey |
| secretKey | String | "" | No | secretKey |

When the registerType is `consul`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| delay | int | 1 | No | The interval of each polling of monitoring metadata, in seconds, the default value is 1 second. |
| wait-time | int | 55 | No | # wait-time: The waiting time for each polling of metadata monitoring, in seconds, the default value is 55 second . |
| metadata-path | String | `shenyu/register` | No | Metadata path name, default is `shenyu/register`. |

When the registerType is `apollo`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| appId | String | null | Yes | Apollo appId |
| namespace | String | null | Yes | Apollo namespace |
| portalUrl | String | null | Yes | Apollo portalUrl |
| env | String | null | Yes | Apollo env |
| clusterName | String | null | Yes | Apollo clusterName |
| token | String | null | Yes | Apollo token |

The Admin System and the Apache ShenYu gateway use data synchronization configurations.

The following properties are configured for data synchronization using `websocket` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | boolean | true | No | whether to enable websocket for data synchronization. |
| messageMaxSize | int | 0 | No | Set the `websocket` max buffer size in bytes. |
| allowOrigins | String | "" | No | Set allowed `origins`, multiple parameters separated by `;`. |

The following properties are configured for data synchronization using `zookeeper` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | Yes | zookeeper server url |
| sessionTimeout | int | null | Yes | session timeout(millisecond) |
| connectionTimeout | int | null | Yes | connection timeout(millisecond) |

The following properties are configured for data synchronization using `http long polling` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | boolean | true | No | whether to enable. |
| refreshInterval | int | 5(minute) | No | Periodically fetch data from the database and load it into memory. |
| notifyBatchSize | int | 100 | No | notify clients in batches |

The following properties are configured for data synchronization using `nacos` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | 是 | nacos url |
| namespace | String | null | Yes | namespace |
| username | String | null | No | username |
| password | String | null | No | password |
| acm |  |  | No | aliyun ACM service configuration |

- `acm` config

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | boolean | false | No | whether to enable |
| endpoint | String | null | No | ACM service address |
| namespace | String | null | No | namespace |
| accessKey | String | null | No | accessKey |
| secretKey | String | null | No | secretKey |

The following properties are configured for data synchronization using `etcd` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | Yes | etcd url |

The following properties are configured for data synchronization using `consul` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | Yes | consul url |

aes secret properties:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| key | String | `2095132720951327` | No | key |
| iv | String | null | No | iv |

Spring ldap properties:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | boolean | true | No | whether to enable |
| url | String | null | No | ldap url |
| bind-dn | String | null | No | UserDn |
| password | String | null | No | password |
| base-dn | String | null | No | searchBase |
| object-class | String | `person` | No | filter |
| login-field | String | `cn` | No | searchBase |
| connectTimeout | int | 3000 | No | connect timeout(millisecond) |
| readTimeout | int | 3000 | No | read timeout(millisecond) |

`jwt` properties:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| expired-seconds | long | 24 *60* 60 \* 1000L | No | expiration time(millisecond) |

`shiro` properties:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| white-list | List | null | No | white list |

---

<a id="user-guide-property-config-client-property-config"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/property-config/client-property-config/ -->

<!-- page_index: 36 -->

# Client Property Config

Version: 2.7.0.3

This paper mainly explains how to configure the properties of Apache ShenYu when the client accesses the gateway.

Set the `shenyu` property in your microservice, for example, in [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http) :

![](assets/images/shenyu-client-application-config_abd01ed14a365513.png)

```yaml
shenyu: 
  client: 
    registerType: http #zookeeper #etcd #nacos #consul #apollo 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 #localhost:8080 
    props: 
      contextPath: /http 
      appName: http 
      port: 8189 
      nacosNameSpace: ShenyuRegisterCenter 
```

This section describes configurations related to client access. For details about client access principles, see: [Application Client Access](#design-register-center-design) , for client access configuration, see: [Application Client Access Config](#user-guide-property-config-register-center-access) .

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| registerType | String | http | Yes | Which mode to use for registry. Currently, http, zookeeper, etcd, consul ,apollo and nacos are supported. |
| serverLists | String | null | No | Configure the address of the registry. In clustering, multiple addresses are separated by commas (,). |
| props |  |  |  | The value of the property varies according to the registerType. |

- `props` config

When microservices are built by different protocols, the property configuration is slightly different. The general attributes are as follows:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| contextPath | String | null | Yes | The route prefix of the microservice in the gateway. |
| appName | String | null | Yes | microservice name. `springcloud` service don't set, please set `spring.application.name`. |
| host | String | null | Yes | microservice address |
| port | int | null | Yes | microservice port |
| isFull | boolean | false | No | Whether to proxy the all service, currently just applies to `springmvc`/ `springcloud` |
| ipAndPort | String | null | No | Service IP and port address, currently just applies to `gRPC` Proxy. |
| shutdownWaitTime | int | 3000 | No | shutdown wait time(millisecond) |
| delayOtherHooksExecTime | int | 2000 | No | `hook` execute time(millisecond) |
| applicationShutdownHooksClassName | String | `java.lang.ApplicationShutdownHooks` | No | `hook` execute class name |
| applicationShutdownHooksFieldName | String | `hooks` | No | `hook` execute field name |

The value of the property varies according to the `registerType`.

When the registerType is `nacos`, there has no other properties.

When the registerType is `zookeeper`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| sessionTimeout | int | 30000 | No | session time out(millisecond) |
| connectionTimeout | int | 3000 | No | connection time out(millisecond) |

When the registerType is `etcd`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| etcdTimeout | int | 30000 | No | etcd time out(millisecond) |
| etcdTTL | int | 5 | No | client lease time to live(second) |

When the registerType is `nacos`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| nacosNameSpace | String | null | Yes | namespace |
| username | String | "" | No | username |
| password | String | "" | No | password |
| accessKey | String | "" | No | accessKey |
| secretKey | String | "" | No | secretKey |

When the registerType is `apollo`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| appId | String | "shenyu" | Yes | appId |
| env | String | "" | Yes | env |
| clusterName | String | "" | Yes | clusterName |
| namespace | String | "" | Yes | namespace |
| token | String | "" | Yes | token |
| portalUrl | String | "" | Yes | portalUrl |

When the registerType is `consul`, no other property configuration is provided. please set `spring.cloud.consul` for the configuration.

---

<a id="user-guide-property-config-gateway-property-config"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/property-config/gateway-property-config/ -->

<!-- page_index: 37 -->

# Gateway Property Config

Version: 2.7.0.3

This paper mainly explains how to configure `Apache ShenYu` properties on the gateway side.

![](assets/images/shenyu-gateway-application-config_76152d567d02e0cb.jpg)

```yaml
shenyu: 
  selectorMatchCache: 
    ## selector L1 cache 
    cache: 
      enabled: false 
      initialCapacity: 10000 # initial capacity in cache 
      maximumSize: 10000 # max size in cache 
    ## selector L2 cache, use trie as L2 cache 
    trie: 
      enabled: false 
      cacheSize: 128 # the number of plug-ins 
      matchMode: antPathMatch 
  ruleMatchCache: 
    ## rule L1 cache 
    cache: 
      enabled: true 
      initialCapacity: 10000 # initial capacity in cache 
      maximumSize: 65536 # max size in cache 
    ## rule L2 cache, use trie as L2 cache 
    trie: 
      enabled: false 
      cacheSize: 1024 # the number of selectors 
      matchMode: antPathMatch 
  netty: 
    http: 
      webServerFactoryEnabled: true 
      selectCount: 1 
      workerCount: 4 
      accessLog: false 
      serverSocketChannel: 
        soRcvBuf: 87380 
        soBackLog: 128 
        soReuseAddr: true 
        connectTimeoutMillis: 30000 
        writeBufferHighWaterMark: 65536 
        writeBufferLowWaterMark: 32768 
        writeSpinCount: 16 
        autoRead: false 
        allocType: "pooled" 
        messageSizeEstimator: 8 
        singleEventExecutorPerGroup: true 
      socketChannel: 
        soKeepAlive: false 
        soReuseAddr: true 
        soLinger: -1 
        tcpNoDelay: true 
        soRcvBuf: 87380 
        soSndBuf: 16384 
        ipTos: 0 
        allowHalfClosure: false 
        connectTimeoutMillis: 30000 
        writeBufferHighWaterMark: 65536 
        writeBufferLowWaterMark: 32768 
        writeSpinCount: 16 
        autoRead: false 
        allocType: "pooled" 
        messageSizeEstimator: 8 
        singleEventExecutorPerGroup: true 
  instance: 
    enabled: false 
    registerType: zookeeper #etcd #consul 
    serverLists: localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
#  httpclient: 
#    strategy: webClient 
#    connectTimeout: 45000 
#    responseTimeout: 3000 
#    readerIdleTime: 3000 
#    writerIdleTime: 3000 
#    allIdleTime: 3000 
#    readTimeout: 3000 
#    writeTimeout: 3000 
#    wiretap: false 
#    keepAlive: false 
#    pool: 
#      type: ELASTIC 
#      name: proxy 
#      maxConnections: 16 
#      acquireTimeout: 45000 
#      maxIdleTime: 3000 
#    proxy: 
#      host: 
#      port: 
#      username: 
#      password: 
#      nonProxyHostsPattern: 
#    ssl: 
#      useInsecureTrustManager: true 
#      keyStoreType: PKCS12 
#      keyStorePath: classpath:keystore.p12 
#      keyStorePassword: 123456 
#      keyStoreProvider:  
#      keyPassword: 123456 
#      trustedX509Certificates: 
#      handshakeTimeout: 
#      closeNotifyFlushTimeout: 
#      closeNotifyReadTimeout: 
#      defaultConfigurationType: 
  sync: 
    websocket: 
      urls: ws://localhost:9095/websocket 
      allowOrigin: ws://localhost:9195 
#    zookeeper: 
#      url: localhost:2181 
#      sessionTimeout: 5000 
#      connectionTimeout: 2000 
#    http: 
#      url: http://localhost:9095 
#    nacos: 
#      url: localhost:8848 
#      namespace: 1c10d748-af86-43b9-8265-75f487d20c6c 
#      username: 
#      password: 
#      acm: 
#        enabled: false 
#        endpoint: acm.aliyun.com 
#        namespace: 
#        accessKey: 
#        secretKey: 
#    etcd: 
#      url: http://localhost:2379 
#    consul: 
#      url: http://localhost:8500 
#      waitTime: 1000 
#      watchDelay: 1000 
  cross: 
    enabled: true 
    allowedHeaders: 
    allowedMethods: "*" 
    allowedAnyOrigin: false 
    allowedOrigin: 
      # format : schema://prefix spacer domain 
      # Access-Control-Allow-Origin: "http://a.apache.org,http://b.apache.org" 
      spacer: "." 
      domain: apache.org 
      prefixes: 
        - a # a.apache.org 
        - b # b.apache.org 
      origins: 
        - c.apache.org 
        - d.apache.org 
        - http://e.apache.org 
      originRegex: ^http(|s)://(.*\.|)abc.com$ 
    allowedExpose: "" 
    maxAge: "18000" 
    allowCredentials: true 
  switchConfig: 
    local: true 
  file: 
    enabled: true 
    maxSize : 10 
  exclude: 
    enabled: false 
    paths: 
      - /favicon.ico 
  fallback: 
    enabled: false 
    paths: 
      - /fallback/hystrix 
      - /fallback/resilience4j 
  health: 
    enabled: false 
    paths: 
      - /actuator/health 
      - /health_check 
  alert: 
    enabled: true 
    admins: localhost:9095 
  extPlugin: 
    path: 
    enabled: true 
    threads: 1 
    scheduleTime: 300 
    scheduleDelay: 30 
  scheduler: 
    enabled: false 
    type: fixed 
    threads: 16 
  upstreamCheck: 
    enabled: false 
    timeout: 3000 
    healthyThreshold: 1 
    unhealthyThreshold: 1 
    interval: 5000 
    printEnabled: true 
    printInterval: 60000 
  ribbon: 
    serverListRefreshInterval: 10000 
  metrics: 
    enabled: false 
    name : prometheus 
    host: 127.0.0.1 
    port: 8090 
    jmxConfig: 
    props: 
      jvm_enabled: true 
  sharedPool: 
    enable: true 
    prefix: "shenyu-shared" 
    corePoolSize: 200 
    maximumPoolSize: 2000 
    keepAliveTime: 60000 
    maxWorkQueueMemory: 1073741824 # 1GB 
    maxFreeMemory: 268435456 # 256MB 
```

- selector match cache

| Field | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to enable selector cache. |
| initialCapacity | Integer | 10000 | No | selector initial capacity |
| maximumSize | Integer | 10000 | No | selector max size |

- selector trie cache

| Field | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to enable selector trie cache |
| cacheSize | Integer | 512 | No | trie cache size |
| matchMode | String | antPathMatch | Yes | path match mode, shenyu support two match modes, `antPathMatch` and `pathPattern` |

- rule match cache

| Field | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to enable rule cache. |
| initialCapacity | Integer | 10000 | No | selector initial capacity |
| maximumSize | Integer | 10000 | No | selector max size |

- rule trie cache

| Field | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to enable rule trie cache |
| cacheSize | Integer | 512 | No | trie cache size |
| matchMode | String | antPathMatch | Yes | path match mode, shenyu support two match modes, `antPathMatch` and `pathPattern` |

shenyu trie match support two match mode, we suggest use `pathPattern` as default match mode

> pathPattern: org.springframework.web.util.pattern.PathPatternParser
> antPathMatch: org.springframework.util.AntPathMatcher

when you mark `matchRestful` as true, we suggest mark all cache to `false` to avoid cache conflict.

The apache shenyu reactor-netty config.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| webServerFactoryEnabled | Boolean | true | No | Whether to enable custom parameters. True-enable. False-NettyReactiveWebServerFactory Can be configured by yourself. |
| selectCount | Integer | 1 | No | Number of netty selectors. |
| workerCount | Integer | 4 | No | Number of netty workers. |
| accessLog | Boolean | false | No | netty request parameters. |
| **ServerSocketChannelConfig** |  |  |  |  |
| soRcvBuf | Integer | -- | No | Socket config, the size of the socket receive buffer. The default value is system dependent. |
| soBackLog | Integer | 128 | No | Socket config, maximum length of the accept queue. |
| soReuseAddr | Boolean | true | No | Socket config, allow reuse of local addresses. The default value in reactor-netty is true. |
| connectTimeoutMillis | Integer | 30000 | No | Netty config, the connect timeout of the channel in milliseconds. |
| writeBufferHighWaterMark | Integer | 65536 | No | Netty config, the high water mark of the write buffer. |
| writeBufferLowWaterMark | Integer | 32768 | No | Netty config, the low water mark of the write buffer. |
| writeSpinCount | Integer | 16 | No | Netty config, the maximum loop count for a write operation. |
| autoRead | Boolean | false | No | Netty config, channel read method will be invoked automatically so that a user application doesn't need to call it at all. The default value in reactor-netty is false, and can only be false. |
| allocType | String | pooled | No | Netty config, set the ByteBufAllocator which is used for the channel to allocate buffers. |
| messageSizeEstimator | Integer | 8 | No | Netty config, message size estimator, estimate ByteBuf,ByteBufHolder and FileRegion size. |
| singleEventExecutorPerGroup | Boolean | true | No | Netty config, single thread execute the event of ChannelPipeline. |
| **SocketChannelConfig** |  |  |  |  |
| soKeepAlive | Boolean | false | No | Socket config, enable tcp keepalive. |
| soReuseAddr | Boolean | true | No | Socket config, allow reuse of local addresses. The default value in reactor-netty is true. |
| soLinger | Integer | -1 | No | Socket config, the delay time for closing the socket. |
| tcpNoDelay | Boolean | true | No | Socket config, enable Nagle algorithm. |
| soRcvBuf | Integer | -- | No | Socket config, the size of the socket receive buffer. The default value is system dependent. |
| soSndBuf | Integer | -- | No | Socket config, the size of the socket send buffer. The default value is system dependent. |
| ipTos | Integer | 0 | No | IP config, the Type of Service (ToS) octet in the Internet Protocol (IP) header. |
| allowHalfClosure | Boolean | false | No | Netty config, Sets whether the channel should not close itself when its remote peer shuts down output to make the connection half-closed. |
| connectTimeoutMillis | Integer | 30000 | No | Netty config, the connect timeout of the channel in milliseconds. |
| writeBufferHighWaterMark | Integer | 65536 | No | Netty config, the high water mark of the write buffer. |
| writeBufferLowWaterMark | Integer | 32768 | No | Netty config, the low water mark of the write buffer. |
| writeSpinCount | Integer | 16 | No | Netty config, the maximum loop count for a write operation. |
| autoRead | Boolean | false | No | Netty config, channel read method will be invoked automatically so that a user application doesn't need to call it at all. The default value in reactor-netty is false, and can only be false. |
| allocType | String | pooled | No | Netty config, set the ByteBufAllocator which is used for the channel to allocate buffers. |
| messageSizeEstimator | Integer | 8 | No | Netty config, message size estimator, estimate ByteBuf,ByteBufHolder and FileRegion size. |
| singleEventExecutorPerGroup | Boolean | true | No | Netty config, single thread execute the event of ChannelPipeline. |

This is the relevant configuration for the `ShenYu` gateway to register to the registration center. For the configuration of the registration center, please refer to [Register Center Instance Config](#user-guide-property-config-register-center-instance).

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | boolean | false | Yes | Whether to start. |
| registerType | String | zookeeper | Yes | Which registry to use, currently supports zookeeper, etcd. |
| serverLists | String | localhost:2181 | Yes | The address of the register center. If using clusters, separate with `,`. |
| props |  |  |  | When using different register types, the attribute values are different. |

- `props` config

When using different register center, the attribute values are different.

When the registerType is `zookeeper`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| sessionTimeout | int | 30000 | No | session time out(millisecond). |
| connectionTimeout | int | 3000 | No | connection time out(millisecond). |

When the registerType is `etcd`, the supported properties are as follows.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| etcdTimeout | int | 30000 | No | etcd time out(millisecond). |
| etcdTTL | int | 5 | No | client lease time to live(second). |

This is the HttpClient configuration used to send proxy requests after proxying the Http and SpringCloud protocols in the `ShenYu` gateway.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| strategy | String | webClient | No | Type of http client, defaults to webClient. - webClient: use by WebClientPlugin - netty: use by NettyHttpClientPlugin. |
| connectTimeout | int | 45000 | No | Connection timeout (millisecond), the default value is 45000. |
| responseTimeout | int | 3000 | No | The response timeout (millisecond), the default value is 3000. |
| readerIdleTime | int | 3000 | No | The reader idle timeout (millisecond), the default value is 3000. |
| writerIdleTime | int | 3000 | No | The writer idle timeout (millisecond), the default value is 3000. |
| allIdleTime | int | 3000 | No | The all idle timeout (millisecond), the default value is 3000. |
| readTimeout | int | 3000 | No | Read timeout (millisecond), the default value is 3000. |
| writeTimeout | int | 3000 | No | Write timeout (millisecond), the default value is 3000. |
| wiretap | Boolean | false | No | Enables wiretap debugging for Netty HttpClient, the default value is 'false'. |
| keepAlive | Boolean | false | No | Enable or Disable Keep-Alive support for the outgoing request, the default value is 'false'. |
| pool |  |  |  | HttpClient connection pool config. |
| proxy |  |  |  | HttpClient proxy config. |
| ssl |  |  |  | HttpClient ssl config. |

- `pool` config

HttpClient connection pool configuration:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| type | String | ELASTIC | No | Type of pool for HttpClient to use, defaults to ELASTIC. - ELASTIC: The connection pool can be cached and grown on demand - FIXED: The connection pool cache and reuse a fixed maximum The number of connections. - DISABLED: The connection pool will always create a new connection. |
| name | String | proxy | No | The channel pool map name, defaults to proxy. |
| maxConnections | int | the maximum value of 2\*CPU and 16 | No | Only for type FIXED, the maximum number of connections before starting pending acquisition on existing ones. the default value is available number of processors\*2. (but with a minimum value of 16). |
| acquireTimeout | int | 45000 | No | Only for type FIXED, the maximum time in millis to wait for acquiring. the default value is 45000. |
| maxIdleTime | int | NULL | No | After which the channel will be closed, if NULL there is no max idle time. |

- `proxy` config

Netty HttpClient proxy configuration:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| host | String | null | No | Hostname for proxy configuration of Netty HttpClient. |
| port | String | null | No | Port for proxy configuration of Netty HttpClient. |
| username | String | null | No | Username for proxy configuration of Netty HttpClient. |
| password | String | null | No | Password for proxy configuration of Netty HttpClient. |
| nonProxyHostsPattern | String | null | No | Regular expression (Java) for a configured list of hosts. that should be reached directly, bypassing the proxy. |

- `SSL` config

Gateway routing can support routing to http and https back-end services at the same time. The following is the SSL-related configuration:

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| useInsecureTrustManager | Boolean | false | No | Installs the netty InsecureTrustManagerFactory. This is insecure and not suitable for production. |
| keyStoreType | String | PKCS12 | No | SSL key store type. |
| keyStorePath | String |  | No | SSL key store path. |
| keyStorePassword | String |  | No | SSL key store pass word. |
| keyStoreProvider | String |  | No | SSL Keystore provider for netty httpClient and webclient. |
| keyPassword | String |  | No | SSL key pass word. |
| trustedX509Certificates | String | Null | No | Trusted certificates for verifying the remote endpoint's certificate.(Use `,` to separate multiple values) |
| handshakeTimeout | int | 10000 | No | SSL handshake timeout. Default to 10000 ms |
| closeNotifyFlushTimeout | int | 3000 | No | SSL close\_notify flush timeout. Default to 3000 ms. |
| closeNotifyReadTimeout | int | 0 | No | SSL close\_notify read timeout. Default to 0 ms. |
| defaultConfigurationType | String | TCP | No | The default ssl configuration type. Defaults to TCP. - H2: SslProvider will be set depending on OpenSsl.isAlpnSupported(), SslProvider.HTTP2\_CIPHERS, ALPN support, HTTP/1.1 and HTTP/2 support. - TCP: [`SslProvider`](https://netty.io/4.1/api/io/netty/handler/ssl/SslProvider.html?is-external=true) will be set depending on `OpenSsl.isAvailable()`. - NONE: There will be no default configuration. |

- `shenyu.file` config

File filter properties.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | enable file size filtering |
| maxSize | Integer | 10 | No | upload file maxSize （MB） |

- `shenyu.cross` config

Cross filter properties:

| Name |  | Type | Default | Required | Description |
| --- | --- | --- | --- | --- | --- |
| enabled |  | Boolean | false | No | allow cross-domain requests |
| allowedHeaders |  | String | x-requested-with, authorization, Content-Type, Authorization, credential, X-XSRF-TOKEN, token, username, client | No | allowedHeaders, Use "," split in multiple cases. the new "allowedHeaders" will append to "Access-Control-Allow-Headers" based on the default value and remove the reduplicative header. |
| allowedMethods |  | String | "\*" | No | allowedMethods |
| allowedAnyOrigin |  | Boolean | false | No | Whether to allow any Origin, if it is true, directly set the `Access-Control-Allow-Origin` to the same value as the Origin, that is, `request.getHeaders().getOrigin()`, and discard the `allowedOrigin` configuration. |
| allowedOrigin |  | AllowedOriginConfig | - | No | Set the allowed request sources. |
|  | spacer | String | "" | No | Set the allowed subdomains, need to use with `domain`, `prefixes`. |
|  | domain | String | "" | No | Set the allowed subdomains, need to use with `spacer`, `prefixes`. |
|  | prefixes | Set | [] | No | Set the allowed subdomains, need to use with `spacer`, `domain`. |
|  | origins | Set | null | No | Set the domain names that are allowed to be accessed, which can be used separately. |
|  | originRegex | String | "" | No | Set up access to domains that allow regular matching, available separately. |
| allowedExpose |  | String | "" | No | allowedExpose |
| maxAge |  | String | "18000" | No | maxAge (ms) |
| allowCredentials |  | Boolean | true | No | allowCredentials |

- `shenyu.exclude` config

Exculde filter properties.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | whether to enable `exclude filter` and reject the specified request to pass through the gateway. |
| paths | Array | null | Yes | Requests matching this list can not pass through the gateway (support Path-Matching). |

- `shenyu.fallback` config

Related configuration of fallback response.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to turn on the fallback response. |
| paths | Array | [] | Yes | Address of the service fallback request. |

- `shenyu.health` config

Configuration related to service health status.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to turn on health detection. |
| paths | Array | `"/actuator/health"` 、`"/health_check"` | No | Set up service health monitoring paths. |

- `shenyu.local` config

Local forwarding-related configuration.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to enable local forwarding. |
| sha512Key | String | "" | Yes | Secret key, according to the secret key to determine whether the need for local forwarding. |

The apache shenyu switch configuration.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| local | Boolean | true | No | Whether to open local mode, if so, local operation data, default open. |

The apache shenyu gateway and the Admin System use data synchronization configurations.

The following properties are configured for data synchronization using `websocket` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| urls | String | null | Yes | The websocket server address of `Admin`, separate multiple addresses with `,`. |
| allowOrigin | String | "" | No | Set the allowed `origins`, with multiple parameters separated by `;`. |

The following properties are configured for data synchronization using `zookeeper` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | Yes | zookeeper server url. |
| sessionTimeout | int | null | Yes | session timeout (millisecond). |
| connectionTimeout | int | null | Yes | connection timeout (millisecond). |

The following properties are configured for data synchronization using `http long polling` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | Yes | `Admin` server address. |

The following properties are configured for data synchronization using `nacos` :

| Name |  | Type | Default | Required | Description |
| --- | --- | --- | --- | --- | --- |
| url |  | String | null | Yes | nacos url |
| namespace |  | String | null | Yes | namespace |
| username |  | String | null | No | username |
| password |  | String | null | No | password |
| acm |  | Object | - | No | aliyun ACM service configuration. |
|  | enabled | boolean | false | No | whether to enable. |
|  | endpoint | String | null | No | ACM service address. |
|  | namespace | String | null | No | namespace. |
|  | accessKey | String | null | No | accessKey. |
|  | secretKey | String | null | No | secretKey. |

The following properties are configured for data synchronization using `apollo` :

| Name |  | Type | Default | Required | Description |
| --- | --- | --- | --- | --- | --- |
| namespace |  | String | null | Yes | namespace |
| appId |  | String | null | Yes | appId |
| token |  | String | null | Yes | token |
| clusterName |  | String | default | Yes | cluster |
| portalUrl |  | String | null | Yes | portalUrl |
| meta |  | String | null | Yes | meta |
| env |  | String | null | Yes | env |

The following properties are configured for data synchronization using `etcd` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | Yes | `etcd` server url. |

The following properties are configured for data synchronization using `consul` :

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| url | String | null | Yes | `consul` server url. |
| waitTime | int | null | Yes | the timeout period for requesting consul service to pull configuration information (milliseconds). |
| watchDelay | int | null | Yes | Synchronization interval (milliseconds). |

The apache shenyu supports dynamic loading of custom plug-ins with the following configuration

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | true | No | open dynamic loading of custom plug-ins. |
| path | String |  | False | custom plugins path, if not config, the path is /ext/lib. |
| threads | Integer | 1 | False | threads for dynamic loading custom plug-ins. |
| scheduleTime | Integer | 300 | False | schedule time (s) for dynamic loading custom plug-ins. |
| scheduleDelay | Integer | 30 | False | schedule delay when app startup. |

Scheduler config for apache shenyu scheduler thread model.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to turn on Scheduler Thread Model. |
| type | String | fixed | False | fixed Thread Pool or elastic Scheduler Thread Model. |
| threads | Integer | Math.max((Runtime.getRuntime().availableProcessors() << 1) + 1, 16) | False | threads for fixed Thread Pool. |

UpstreamCheck config is the configuration used by apache shenyu to detect upstream.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to turn on upstreamCheck. |
| timeout | Integer | 3000 | No | timeout (ms). |
| healthyThreshold | Integer | 1 | No | healthyThreshold. |
| unhealthyThreshold | Integer | 1 | No | unhealthyThreshold. |
| interval | Integer | 5000 | No | schedule time (ms) for checked. |
| printEnabled | Boolean | true | No | Whether to turn on print logs. |
| printInterval | Integer | 60000 | No | schedule time (ms) for print logs. |

The apache shenyu polling interval configuration.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| serverListRefreshInterval | Integer | 10000 | No | Adjust the refresh interval parameter, refer to`com.netflix.client.config.CommonClientConfigKey#ServerListRefreshInterval`. |

The apache shenyu metrics config，the gateway is used to monitor its own operational status.

| Name |  | Type | Default | Required | Description |
| --- | --- | --- | --- | --- | --- |
| enabled |  | Boolean | false | No | Whether to enable metrics, true means enable. |
| name |  | String | "" | No | name. |
| host |  | String | "" | No | IP exposed by the gateway service to the collection service. |
| port |  | Integer | Null | No | Port exposed by the gateway service to the collection service. |
| jmxConfig |  | String | "" | No | jmx config. |
| props |  | - |  | No | properties. |
|  | jvm\_enabled | Boolean | Null | No | Turn on jvm's monitoring metrics. |

The apache shenyu shared thread pool configuration.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to enable shared thread pooling. |
| prefix | String | "shenyu-shared" | No | Thread pool name prefix. |
| corePoolSize | Integer | 200 | No | Number of core threads in the thread pool. |
| maximumPoolSize | Integer | Integer.MAX\_VALUE | No | Maximum number of threads in the thread pool. |
| keepAliveTime | Long | 60000L | No | Excess idle thread keepAlive time, in milliseconds. |
| maxWorkQueueMemory | Long | 80% of the current JVM maximum available memory | No | Maximum memory used (byte). |
| maxFreeMemory | Integer | 无 | No | Maximum remaining memory (byte). |

The apache shenyu alert notice configuration.

| Name | Type | Default | Required | Description |
| --- | --- | --- | --- | --- |
| enabled | Boolean | false | No | Whether to enable alarm message. |
| admins | String | "localhost:9095" | No | Report alarm message to shenyu admin server list. |

---

<a id="user-guide-property-config-register-center-access"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/property-config/register-center-access/ -->

<!-- page_index: 38 -->

# Application Client Access Config

Version: 2.7.0.3

> *Notice*
> After ShenYu version 2.6.1, the ShenYu register just support http type, and the middleware register type has been removed.
> So, please use the http register type to register your service.
> ShenYu Register Center isn't microservice register center, it just register metadata, selector data, rule data to shenyu-admin, and then shenyu-admin will sync data to shenyu-gateway.

Application client access means to access your microservice to ShenYu gateway, currently supports HTTP, Dubbo, Spring Cloud, gRPC, Motan, Sofa, Tars and other protocols access. Currently, ShenYu just support HTTP register type.

This article describes how to configure the application client to access the Apache ShenYu gateway. For related principles, see [Application Client Access](#design-register-center-design) in the design document .

![](assets/images/app-client-access-config-en_84306e266916699d.png)

Set the register type to '`Http` in the `yml` file. The configuration information is as follows:

```yaml
shenyu: 
  register: 
    registerType: http 
    props: 
      	checked: true  # is checked 
      	zombieCheckTimes: 5 # how many times does it fail to detect the service 
      	scheduledTime: 10 # timed detection interval time 
```

![](assets/images/register-http-admin-yml_d736e70fc8d022b7.png)

The following shows the configuration information registered through `Http` when the `Http` service accesses the `Apache ShenYu` gateway as a client. Other clients (such as `Dubbo` and `Spring Cloud`) can be configured in the same way.

```yaml
shenyu: 
  register: 
    registerType: http 
    serverLists: http://localhost:9095 
    props: 
      username: admin 
      password: 123456 
  client: 
    http: 
    	props: 
      		contextPath: /http 
      		appName: http 
      		port: 8188   
      		isFull: false 
# registerType : register type, set http 
# serverList: when register type is http，set shenyu-admin address list，pls note 'http://' is necessary. 
# port: your project port number; apply to springmvc/tars/grpc 
# contextPath: your project's route prefix through shenyu gateway, such as /order ，/product etc，gateway will route based on it. 
# appName：your project name,the default value is`spring.application.name`. 
# isFull: set true means providing proxy for your entire service, or only a few controller. apply to springmvc/springcloud 
```

![](assets/images/register-http-client-yml_71f9c50197d31b16.jpg)
> follow example use the http and dubbo.

the `yml` configuration like follow:

```yaml
shenyu: 
  register: 
    registerType: http 
    serverLists: localhost:9195 
    props: 
      username: admin 
      password: 123456 
  client: 
    http: 
    	props: 
      		contextPath: /http 
      		appName: http 
      		port: 8188   
      		isFull: false 
    dubbo: 
    	props: 
      		contextPath: /dubbo 
      		appName: dubbo 
      		port: 28080 
    props: 
      nacosNameSpace: ShenyuRegisterCenter 
# registerType : register type, set nacos  
# serverList: when register type is nacos, add nacos address list 
# http.port: your project port number; apply to springmvc 
# http.contextPath: your project's route prefix through shenyu gateway, such as /order ，/product etc，gateway will route based on it. 
# http.appName：your project name,the default value is`spring.application.name`. 
# http.isFull: set true means providing proxy for your entire service, or only a few controller. apply to springmvc/springcloud 
# dubbo.contextPath: your project dubbo service's context path 
# dubbo.port: your project dubbo rpc port 
# dubbo.appName: your project dubbo application name 
# nacosNameSpace: nacos namespace 
```

In conclusion, this paper mainly describes how to connect your microservices (currently supporting `Http`, `Dubbo`, `Spring Cloud`, `gRPC`, `Motan`, `Sofa`, `Tars` and other protocols) to the `Apache ShenYu` gateway. the Apache ShenYu gateway support registry has `Http` This paper introduces the different ways to register configuration information when `Http` service is used as the client to access `Apache ShenYu` gateway.

---

<a id="user-guide-property-config-register-center-instance"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/property-config/register-center-instance/ -->

<!-- page_index: 39 -->

# Register Center Instance Config

Version: 2.7.0.3

This document will introduce how to register the gateway instance to the registry. The `Apache ShenYu` gateway currently supports registration to `zookeeper` , `etcd` and `consul`.

First, introduce the following dependencies in the gateway's `pom.xml` file.

```xml
<!--shenyu registry start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-registry</artifactId> 
    <version>${project.version}</version> 
</dependency> 
<!--shenyu registry end--> 
```

> Please pay attention! From ShenYu 2.5.0, ShenYu will no longer support Zookeeper 3.4.x or below version. If you're already using Zookeeper, You need to use Zookeeper with a higher version and initialize the data.

Add the following configuration to the gateway's `yml` file:

```yaml
registry: 
    enabled: true 
    registerType: zookeeper 
    serverLists: localhost:2181 #config with your zk address, used by the cluster environment, separated with (,). 
    props: 
      sessionTimeout: 3000 #Optional, default 3000 
      connectionTimeout: 3000 #Optional, default 3000 
```

Add the following configuration to the gateway's `yml` file:

```yaml
registry: 
    enabled: true 
    registerType: etcd 
    serverLists: http://localhost:2379 #config with your etcd address, used by the cluster environment, separated with (,). 
    props: 
      etcdTimeout: 3000 #Optional, default 3000 
      etcdTTL: 5 #Optional, default 5 
```

Add the following configuration to the gateway's `yml` file:

```yaml
registry: 
    enabled: true 
    registerType: apollo 
    serverLists: http://localhost:8080 
    props: 
      env: dev 
      appId: shenyu 
      namespace: application 
      clusterName: default 
      token: 0fff5645fc74ee5e0d63a6389433c8c8afc0beea31eed0279ecc1c8961d12da9 
      portalUrl: http://localhost:8070 
```

> After the configuration is complete, start the gateway and it will successfully register to the corresponding registration center.

---

<a id="user-guide-property-config-ssl"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/property-config/ssl/ -->

<!-- page_index: 40 -->

# Gateway SSL Config

Version: 2.7.0.3

This article explains how to configure SSL and the questions users often have about SSL configuration.

`ShenYu` receives messages through tomcat, but the actual forwarding is achieved through its own plug-in.

Therefore, configuring tomcat's SSL cannot achieve full-link SSL forwarding. You only need to configure `webClientPlugin` to achieve full-link SSL forwarding.

Take the p12 certificate as an example.

```yaml
shenyu: 
  httpclient: 
    ssl: 
      useInsecureTrustManager: false 
      keyStoreType: PKCS12 
      keyStorePath: classpath:keystore.p12 
      keyStorePassword: 123456 
      keyPassword: 123456 
```

---

<a id="user-guide-property-config-use-data-sync"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/property-config/use-data-sync/ -->

<!-- page_index: 41 -->

# Data Synchronization Config

Version: 2.7.0.3

This document focuses on how to use different data synchronization strategies. Data synchronization refers to the strategy used to synchronize data to ShenYu gateway after shenyu-admin background operation data. ShenYu gateway currently supports ZooKeeper, WebSocket, HTTP Long Polling, Nacos, Etcd and Consul for data synchronization.

![](assets/images/data-sync-config-dir-en_1d4a805d9dd6d65e.png)

For details about the data synchronization principles, see [Data Synchronization Design](#design-data-sync) in the design document.

- `Apache ShenYu` gateway config

  Add these dependencies in `pom.xml`：

```xml
    <!-- apache shenyu data sync start use websocket--> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sync-data-websocket</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
```

![](assets/images/shenyu-data-sync-websocket-pom_b81cba729e5340ee.png)

Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    websocket : 
      # urls: address of shenyu-admin，multi-address will be separated with (,). 
      urls: ws://localhost:9095/websocket 
      allowOrigin: ws://localhost:9195 
```

![](assets/images/shenyu-data-sync-websocket-yml_ce915dd6db399777.png)

- `shenyu-admin` config

  Add these config values in yaml file:

```yml
shenyu: 
  sync: 
    websocket: 
      enabled: true 
```

![](assets/images/shenyu-data-sync-websocket-admin-yml_5ae463563b8e9e5f.png)

After the connection is established, the data will be fully obtained once, and the subsequent data will be updated and added increments, with good performance. It also supports disconnection (default: `30` seconds). This mode is recommended for data synchronization and is the default data synchronization strategy of ShenYu.

> Please pay attention! From ShenYu 2.5.0, ShenYu will no longer support Zookeeper 3.4.x or below version. If you're already using Zookeeper, You need to use Zookeeper with a higher version and initialize the data.

- `Apache ShenYu` gateway config

  Add these dependencies in `pom.xml`：

```xml
       <!-- apache shenyu data sync start use zookeeper--> 
       <dependency> 
           <groupId>org.apache.shenyu</groupId> 
           <artifactId>shenyu-spring-boot-starter-sync-data-zookeeper</artifactId> 
           <version>${project.version}</version> 
       </dependency> 
```

![](assets/images/shenyu-data-sync-zk-pom_d50dabb479387126.png)

Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    zookeeper: 
      url: localhost:2181 
       #url: config with your zk address, used by the cluster environment, separated with (,). 
      sessionTimeout: 5000 
      connectionTimeout: 2000 
```

![](assets/images/shenyu-data-sync-zk-yml_4462b040276f8447.png)

- `shenyu-admin` config

Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    zookeeper: 
      url: localhost:2181 
       #url: config with your zk address, used by the cluster environment, separated with (,). 
      sessionTimeout: 5000 
      connectionTimeout: 2000 
```

![](assets/images/shenyu-data-sync-admin-zk-yml_029a74406a1cfc66.png)

It is a good idea to use ZooKeeper synchronization mechanism with high timeliness, but we also have to deal with the unstable environment of ZK, cluster brain splitting and other problems.

- `Apache ShenYu` gateway config

Add these dependencies in `pom.xml`：

```xml
        <!-- apache shenyu data sync start use http--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-sync-data-http</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
```

![](assets/images/shenyu-data-sync-http-pom_553e609d6463b977.png)

Add these config values in yaml file:

```yaml
shenyu: 
    sync: 
        http: 
             url: http://localhost:9095 
        #url: config your shenyu-admin  ip and port，cluster IP by split by (,) 
```

![](assets/images/shenyu-data-sync-http-yml_9f2eb79968cf4587.png)

- `shenyu-admin` config

  Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    http: 
      enabled: true 
```

![](assets/images/shenyu-data-sync-admin-http-yml_3438b34abe91f0f7.png)

HTTP long-polling makes the gateway lightweight, but less time-sensitive. It pulls according to the group key, if the data is too large, it will have some influences, a small change under a group will pull the entire group.

- `Apache ShenYu` gateway config

Add these dependencies in `pom.xml`：

```xml
        <!-- apache shenyu data sync start use nacos--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-sync-data-nacos</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
```

![](assets/images/shenyu-data-sync-nacos-pom_f6c4e0e5092e8b11.png)

Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    nacos: 
      url: localhost:8848 
         # url: config with your nacos address, please use (,) to split your cluster environment. 
      namespace: 1c10d748-af86-43b9-8265-75f487d20c6c 
      username: 
      password: 
      acm: 
        enabled: false 
        endpoint: acm.aliyun.com 
        namespace: 
        accessKey: 
        secretKey: 
     # other configure，please refer to the naocs website. 
```

![](assets/images/shenyu-data-sync-nacos-yml_75fb13ba74a37ea9.png)

- `shenyu-admin` config

  Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
      nacos: 
        url: localhost:8848 
        namespace: 1c10d748-af86-43b9-8265-75f487d20c6c 
        username: 
        password: 
        acm: 
          enabled: false 
          endpoint: acm.aliyun.com 
          namespace: 
          accessKey: 
          secretKey: 
        # url: config with your nacos address, pls use (,) to split your cluster environment. 
        # other configure，pls refer to the naocs website. 
```

![](assets/images/shenyu-data-sync-admin-nacos-yml_25d3b2a8254b8d03.png)

- `Apache ShenYu` gateway config

  Add these dependencies in `pom.xml`：

```xml
        <!-- apache shenyu data sync start use etcd--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-sync-data-etcd</artifactId> 
            <version>${project.version}</version> 
            <exclusions> 
                <exclusion> 
                    <groupId>io.grpc</groupId> 
                    <artifactId>grpc-grpclb</artifactId> 
                </exclusion> 
                <exclusion> 
                    <groupId>io.grpc</groupId> 
                    <artifactId>grpc-netty</artifactId> 
                </exclusion> 
            </exclusions> 
        </dependency> 
```

![](assets/images/shenyu-data-sync-etcd-pom_8cca9b1ad19cd239.png)

Add these config values in yaml file:

```yaml
shenyu: 
    sync: 
       etcd: 
         url: http://localhost:2379 
       #url: config with your etcd address, used by the cluster environment, separated with (,). 
```

![](assets/images/shenyu-data-sync-etcd-yml_ac9daa872b054bd5.png)

- `shenyu-admin` config

  Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    etcd: 
      url: http://localhost:2379 
       #url: config with your etcd address, used by the cluster environment, separated with (,). 
```

![](assets/images/shenyu-data-sync-admin-etcd-yml_4080b5e6f14899e8.png)

- `Apache ShenYu` gateway config

Add these dependencies in `pom.xml`：

```xml
<!-- apache shenyu data sync start use consul--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-sync-data-consul</artifactId> 
  <version>${project.version}</version> 
</dependency> 
```

![](assets/images/shenyu-consul-sync-gateway_0dece94013161443.jpg)

Add these config values in yaml file:

```yaml
shenyu: 
    sync: 
      consul: 
        url: http://localhost:8500 
        waitTime: 1000	# query wait time 
        watchDelay: 1000	# Data synchronization interval                              
```

![](assets/images/shenyu-consul-gateway-sync-config_4d6a0a73ba59ba79.jpg)

- `shenyu-admin` config

  Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    consul: 
      url: http://localhost:8500 
```

![](assets/images/shenyu-consul-admin-sync-config_c6cd8bb63023a896.jpg)

Apollo just support Java [8,17), if you want to use apollo as data sync center, please make sure your JDK version is between [8,17).

- `Apache ShenYu` gateway config

Download the corresponding version of the jar package from `https://repo1.maven.org/maven2/org/apache/shenyu/shenyu-spring-boot-starter-sync-data-apollo/`, and then put the jar package into the `/lib` directory.

Add these config values in yaml file:

```yaml
shenyu: 
  sync: 
    apollo: 
    appId: shenyu 
    meta: http://localhost:8080 
    env: dev 
    clusterName: test 
    namespace: application 
```

- `Apache ShenYu Admin` config

Download the corresponding version of the jar package from `https://repo1.maven.org/maven2/org/apache/shenyu/shenyu-admin-listener-apollo/`, and then put the jar package into the `/lib` directory.

```yaml
shenyu: 
  sync: 
    apollo: 
      meta: http://localhost:8080 
      appId: shenyu 
      portalUrl: http://localhost:8070 
      env: dev 
      clusterName: test 
      namespace: application 
      token: 0fff5645fc74ee5e0d63a6389433c8c8afc0beea31eed0279ecc1c8961d12da9 
```

![](assets/images/shenyu-data-sync-admin-apollo-yml_6e7abd68ffdc1f72.png)
> After the data synchronization strategy of Apache ShenYu gateway and shenyu-admin is reconfigured, the microservice needs to be restarted.
> the Apache ShenYu gateway and shenyu-admin must use the same synchronization strategy.

---

<a id="user-guide-sdk-usage-shenyu-sdk-consul"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/sdk-usage/shenyu-sdk-consul/ -->

<!-- page_index: 42 -->

# Using Consul with Shenyu-SDK

Version: 2.7.0.3

Shenyu offers Shenyu-Sdk to make it easy for services to quickly integrate with the Shenyu gateway. By simply depending on the SDK and doing some simple configuration, client services can call the gateway's exposed APIs as if they were calling local interfaces.

![](assets/images/shenyu-sdk-process_7bd4c21ad3577744.png)

The registration center supported by the gateway for client access includes (nacos, eureka, etcd, zookeeper, consul), and the following is the relevant guide for using **Zookeeper** registration center when `shenyu-bootstrap` and `application client` are used.

Refer to `Deployment` guide, and choose a way to start `shenyu-admin` and `shenyu-bootstrap`.

In the gateway's `pom.xml` file, introduce the following dependencies.

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-registry</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

Add the following configuration to the gateway's `yml` configuration file.

```yaml
shenyu: 
  register: 
    enabled: true 
    registerType: consul 
    serverLists: localhost 
    props: 
      delay: 1 
      wait-time: 55 
      instanceId: shenyu-gateway 
      hostName: localhost 
      tags: test1,test2 
      preferAgentAddress: false 
      enableTagOverride: false 
 
# registerType: service registration type, fill in consul 
# serverLists: consul client agent address (sidecar deployment mode (single machine or cluster), can also be the address of consul server agent (can only connect to one consul server agent node, if it is a cluster, then there will be a single point of failure problem)) 
# delay: the polling interval of each metadata monitoring, unit: second, default 1 second 
# wait-time: the waiting time of a single request for metadata monitoring (long polling mechanism), unit: second, default 55 seconds 
# instanceId: required for consul service, consul needs to find specific services through instance-id 
# name: the group name where the service is registered to consul 
# hostName: for consul registration type, fill in the address of the registered service instance, the address of the registered service instance in this registration center will not be used for client calls, so this configuration can be omitted, port, preferAgentAddress similarly 
# port: for consul registration type, fill in the port of the registered service instance 
# tags: corresponding to the tags configuration in consul configuration 
# preferAgentAddress: use the address of the agent on the consul client side as the address of the registered service instance, which will override the manual configuration of hostName 
# enableTagOverride: corresponding to the enableTagOverride configuration in consul configuration for detailed reference, please see the user guide> attribute configuration> client access configuration document 
 
# for detailed reference, please see the `user-guide> Property Config> Register Center Instance Config` configuration document. 
```

In the `pom.xml` file of the application client, introduce the following dependencies.

- Shenyu-Sdk Core

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-sdk-core</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sdk</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
</dependencies> 
```

- Shenyu-Sdk http implementation

> HTTP client implementation, offering okhttp and httpclient as implementation options. Other implementations can be created by extending the `AbstractShenyuSdkClient` class.

```xml
<!-- httpclient --> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-httpclient</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
 
<!-- okhttp --> 
<!--  
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-okhttp</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
--> 
```

Add the following configuration in the application client's `yml` configuration file.

```yaml
shenyu: 
  sdk: 
    enabled: true 
    register-type: consul 
    server-lists: localhost 
    props: 
      checkTtl: 5 
      token: "" 
      waitTime: 30 
      watchDelay: 5 
      tags: "" 
      port: 8500 
      retry: 
        enable: true 
        period: 100 
        maxPeriod: 1000 
        maxAttempts: 5 
      algorithm: roundRobin 
      scheme: http 
       
# registerType: service registration type, fill in consul. 
# serverLists: consul client agent address (sidecar deployment mode (single machine or cluster), can also be the address of consul server agent (can only connect to one consul server agent node, if it is a cluster, then there will be a single point of failure problem)). 
# checkTtl: TTL, Default 5 seconds. 
# token: "" 
# waitTime: The waiting time for a single request for monitoring metadata (long polling mechanism), in seconds, with a default value of 55 seconds. 
# watchDelay: The interval duration for each polling of metadata monitoring, in seconds, with a default value of 1 second. 
# tags: tags for consul configure. 
# port: consul server port. 
# scheme: Request protocol. 
 
# retry Configuration related to failure retries 
# retry.period: Retry waiting time. 
# retry.maxPeriod: Maximum retry waiting time . 
# retry.maxAttempts: Maximum retry count. 
```

1. In the project startup class, annotate `@EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api")`, where `basePackages` maintains the package location of Shenyu-Sdk's corresponding maintained gateway API interface.
2. Create an interface and use the `@ShenyuClient(name = "xxx", contextId = "ShenyuSdkApiName")` annotation to mark it, where `name` represents the gateway service name. If you need to define multiple beans to maintain the gateway's API, you can use `contextId` as the corresponding bean alias.
3. In the defined interface, add the methods of the interface to be mapped to the shenyu gateway, where the `value` of `@xxMapping` corresponds to the path of the corresponding request in the gateway.

**Example**

Project startup class

```java
import org.apache.shenyu.sdk.spring.EnableShenyuClients;
@SpringBootApplication @EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api") public class ShenyuSdkHttpExampleApplication {
/** * main.* * @param args args */ public static void main(final String[] args) {SpringApplication.run(ShenyuSdkHttpExampleApplication.class, args);}}
```

Shenyu-SDK interface

```java
import org.apache.shenyu.sdk.spring.ShenyuClient;
@ShenyuClient(name = "shenyu-gateway", contextId = "ShenyuSdkApiName") public interface ShenyuHttpClientApi {
/** * findById.* test Get.* * @param id id * @return SdkTestDto */ @GetMapping("/http/shenyu/client/findById") SdkTestDto findById(@RequestParam("id") String id);}
```

For more information, refer to the sample project [shenyu-examples-sdk](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sdk)

---

<a id="user-guide-sdk-usage-shenyu-sdk-etcd"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/sdk-usage/shenyu-sdk-etcd/ -->

<!-- page_index: 43 -->

# Using Etcd with Shenyu-SDK

Version: 2.7.0.3

Shenyu offers Shenyu-Sdk to make it easy for services to quickly integrate with the Shenyu gateway. By simply depending on the SDK and doing some simple configuration, client services can call the gateway's exposed APIs as if they were calling local interfaces.

![](assets/images/shenyu-sdk-process_7bd4c21ad3577744.png)

The registration center supported by the gateway for client access includes (nacos, eureka, etcd, zookeeper, consul), and the following is the relevant guide for using **etcd** registration center when `shenyu-bootstrap` and `application client` are used.

Refer to `Deployment` guide, and choose a way to start `shenyu-admin` and `shenyu-bootstrap`.

In the gateway's `pom.xml` file, introduce the following dependencies.

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-registry</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

Add the following configuration to the gateway's `yml` configuration file.

```yaml
shenyu: 
  register: 
    enabled: true 
    registerType: etcd 
    serverLists: http://localhost:2379 
    props: 
      appName: http 
      port: xx 
       
# registerType: service registration type, fill in etcd. 
# serverList: Enter the etcd address(es), separated by commas in English. 
# appName：Your application name. If not configured, the default value will be taken from spring.application.name. 
# port: Your project's startup port, currently springmvc/tars/grpc needs to be filled in. 
 
# for detailed reference, please see the `user-guide> Property Config> Register Center Instance Config` configuration document. 
```

In the `pom.xml` file of the application client, introduce the following dependencies.

- Shenyu-Sdk Core

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-sdk-core</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sdk</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
</dependencies> 
```

- Shenyu-Sdk http implementation

> HTTP client implementation, offering okhttp and httpclient as implementation options. Other implementations can be created by extending the `AbstractShenyuSdkClient` class.

```xml
<!-- httpclient --> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-httpclient</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
 
<!-- okhttp --> 
<!--  
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-okhttp</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
--> 
```

Add the following configuration in the application client's `yml` configuration file.

```yaml
shenyu: 
  sdk: 
    enabled: true 
    register-type: etcd 
    server-lists: http://localhost:2379 
    props: 
      etcdTimeout: 3000 
      etcdTTL: 5 
      retry: 
        enable: true 
        period: 100 
        maxPeriod: 1000 
        maxAttempts: 5 
      algorithm: roundRobin 
      scheme: http 
 
# register-type: service registration type, fill in etcd. 
# server-lists: Enter the etcd address(es), separated by commas in English. 
# etcdTimeout: Request timeout time, in milliseconds, default 3000 
# etcdTTL: Lease TTL, default 5 seconds. 
# scheme: Request protocol. 
 
# retry: Configuration related to failure retries. 
# retry.period: Retry waiting time. 
# retry.maxPeriod: Maximum retry waiting time . 
# retry.maxAttempts: Maximum retry count. 
```

1. In the project startup class, annotate `@EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api")`, where `basePackages` maintains the package location of Shenyu-Sdk's corresponding maintained gateway API interface.
2. Create an interface and use the `@ShenyuClient(name = "xxx", contextId = "ShenyuSdkApiName")` annotation to mark it, where `name` represents the gateway service name. If you need to define multiple beans to maintain the gateway's API, you can use `contextId` as the corresponding bean alias.
3. In the defined interface, add the methods of the interface to be mapped to the shenyu gateway, where the `value` of `@xxMapping` corresponds to the path of the corresponding request in the gateway.

**Example**

Project startup class

```java
import org.apache.shenyu.sdk.spring.EnableShenyuClients;
@SpringBootApplication @EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api") public class ShenyuSdkHttpExampleApplication {
/** * main.* * @param args args */ public static void main(final String[] args) {SpringApplication.run(ShenyuSdkHttpExampleApplication.class, args);}}
```

Shenyu-SDK interface

```java
import org.apache.shenyu.sdk.spring.ShenyuClient;
@ShenyuClient(name = "shenyu-gateway", contextId = "ShenyuSdkApiName") public interface ShenyuHttpClientApi {
/** * findById.* test Get.* * @param id id * @return SdkTestDto */ @GetMapping("/http/shenyu/client/findById") SdkTestDto findById(@RequestParam("id") String id);}
```

For more information, refer to the sample project [shenyu-examples-sdk](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sdk)

---

<a id="user-guide-sdk-usage-shenyu-sdk-eureka"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/sdk-usage/shenyu-sdk-eureka/ -->

<!-- page_index: 44 -->

# Using Eureka with Shenyu-SDK

Version: 2.7.0.3

Shenyu offers Shenyu-Sdk to make it easy for services to quickly integrate with the Shenyu gateway. By simply depending on the SDK and doing some simple configuration, client services can call the gateway's exposed APIs as if they were calling local interfaces.

![](assets/images/shenyu-sdk-process_7bd4c21ad3577744.png)

The registration center supported by the gateway for client access includes (nacos, eureka, etcd, zookeeper, consul), and the following is the relevant guide for using **eureka** registration center when `shenyu-bootstrap` and `application client` are used.

Refer to `Deployment` guide, and choose a way to start `shenyu-admin` and `shenyu-bootstrap`.

In the gateway's `pom.xml` file, introduce the following dependencies.

```xml
<dependency> 
    <groupId>org.springframework.cloud</groupId> 
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId> 
    <version>${eureka-client.version}</version> 
    <exclusions> 
        <exclusion> 
            <groupId>org.springframework.cloud</groupId> 
            <artifactId>spring-cloud-starter-loadbalancer</artifactId> 
        </exclusion> 
    </exclusions> 
</dependency> 
```

Add the following configuration to the gateway's `yml` configuration file.

```yaml
spring: 
  cloud: 
    discovery: 
      enabled: true # Enable service discovery 
   
eureka: 
  client: 
    enabled: true 
    serviceUrl: 
      defaultZone: http://localhost:8761/eureka/ # Enter your eureka registry center address here 
  instance: 
    prefer-ip-address: true 
```

In the `pom.xml` file of the application client, introduce the following dependencies.

- Shenyu-Sdk Core

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-sdk-core</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sdk</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
</dependencies> 
```

- Shenyu-Sdk http implementation

> HTTP client implementation, offering okhttp and httpclient as implementation options. Other implementations can be created by extending the `AbstractShenyuSdkClient` class.

```xml
<!-- httpclient --> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-httpclient</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
 
<!-- okhttp --> 
<!--  
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-okhttp</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
--> 
```

Add the following configuration in the application client's `yml` configuration file.

```yaml
shenyu: 
  sdk: 
    enabled: true 
    register-type: eureka  
    server-lists: http://localhost:8761/eureka/ 
    props: 
      retry: 
        enable: true 
        period: 100 
        maxPeriod: 1000 
        maxAttempts: 5 
      algorithm: roundRobin 
      scheme: http 
       
# registerType: service registration type, fill in eureka 
# serverList: Enter the eureka server address(es), separated by commas in English. 
# scheme: Request protocol. 
 
# retry: Configuration related to failure retries. 
# retry.period: Retry waiting time. 
# retry.maxPeriod: Maximum retry waiting time . 
# retry.maxAttempts: Maximum retry count. 
```

1. In the project startup class, annotate `@EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api")`, where `basePackages` maintains the package location of Shenyu-Sdk's corresponding maintained gateway API interface.
2. Create an interface and use the `@ShenyuClient(name = "xxx", contextId = "ShenyuSdkApiName")` annotation to mark it, where `name` represents the gateway service name. If you need to define multiple beans to maintain the gateway's API, you can use `contextId` as the corresponding bean alias.
3. In the defined interface, add the methods of the interface to be mapped to the shenyu gateway, where the `value` of `@xxMapping` corresponds to the path of the corresponding request in the gateway.

**Example**

Project startup class

```java
import org.apache.shenyu.sdk.spring.EnableShenyuClients;
@SpringBootApplication @EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api") public class ShenyuSdkHttpExampleApplication {
/** * main.* * @param args args */ public static void main(final String[] args) {SpringApplication.run(ShenyuSdkHttpExampleApplication.class, args);}}
```

Shenyu-SDK interface

```java
import org.apache.shenyu.sdk.spring.ShenyuClient;
@ShenyuClient(name = "shenyu-bootstrap", contextId = "ShenyuSdkApiName") public interface ShenyuHttpClientApi {
/** * findById.* test Get.* * @param id id * @return SdkTestDto */ @GetMapping("/http/shenyu/client/findById") SdkTestDto findById(@RequestParam("id") String id);}
```

For more information, refer to the sample project [shenyu-examples-sdk](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sdk)

---

<a id="user-guide-sdk-usage-shenyu-sdk-feign"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/sdk-usage/shenyu-sdk-feign/ -->

<!-- page_index: 45 -->

# Using Shenyu-SDK-Feign

Version: 2.7.0.3

> Integrate `open Feign` to implement declarative SDK call gateway API.
> Like 'shenyu sdk', 'shenyu sdk feign' is another option;
> for more information see :
>
> - please refer to: [shenyu-sdk-consul](#user-guide-sdk-usage-shenyu-sdk-consul)
> - please refer to: [shenyu-sdk-etcd](#user-guide-sdk-usage-shenyu-sdk-etcd)
> - please refer to: [shenyu-sdk-eureka](#user-guide-sdk-usage-shenyu-sdk-eureka)
> - please refer to: [shenyu-sdk-nacos](#user-guide-sdk-usage-shenyu-sdk-nacos)
> - please refer to: [shenyu-sdk-zookeeper](#user-guide-sdk-usage-shenyu-sdk-zookeeper)

In the `pom.xml` file of the application client, introduce the following dependencies(Compatible with `FeignClient`).

```xml
<dependencies> 
    <dependency> 
        <groupId>org.springframework.cloud</groupId> 
        <artifactId>spring-cloud-starter-openfeign</artifactId> 
        <version>${spring-cloud.version}</version> 
    </dependency> 
     
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sdk-feign</artifactId> 
        <version>2.6.1-SNAPSHOT</version> 
    </dependency> 
</dependencies> 
```

Add the following configuration in the application client's `yml` configuration file.

```yaml
shenyu: 
  sdk: 
    enabled: true 
    register-type: consul 
    server-lists: localhost 
    props: 
      algorithm: roundRobin 
      scheme: http 
 
# if not use openFeign and springCloud-loadBalance, feign client options must be enabled. 
feign: 
  client: 
    httpclient: 
      enabled: true 
 
# registerType: service registration type, fill in consul. 
# serverLists: consul client agent address (sidecar deployment mode (single machine or cluster), can also be the address of consul server agent (can only connect to one consul server agent node, if it is a cluster, then there will be a single point of failure problem)). 
 
# algorithm: load balance algorithm. 
# scheme: Request protocol. 
 
```

1. In the project startup class, annotate `@EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api")`, where `basePackages` maintains the package location of Shenyu-Sdk's corresponding maintained gateway API interface.
2. Create an interface and use the `@ShenyuClient(name = "xxx", contextId = "ShenyuSdkApiName")` annotation to mark it, where `name` represents the gateway service name. If you need to define multiple beans to maintain the gateway's API, you can use `contextId` as the corresponding bean alias.
3. In the defined interface, add the methods of the interface to be mapped to the shenyu gateway, where the `value` of `@xxMapping` corresponds to the path of the corresponding request in the gateway.

**Example**

Project startup class

```java
import org.apache.shenyu.sdk.feign.EnableShenyuClients;
@SpringBootApplication @EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.feign.api") public class ShenyuSdkHttpExampleApplication {
/** * main.* * @param args args */ public static void main(final String[] args) {SpringApplication.run(ShenyuSdkHttpExampleApplication.class, args);}}
```

Shenyu-SDK interface

```java
import org.apache.shenyu.sdk.feign.ShenyuClient;
@ShenyuClient(name = "shenyu-gateway", contextId = "ShenyuSdkApiName", path = "/feign/shenyu/client") public interface ShenyuFeignClientApi {
/** * findById.* test Get.* * @param id id * @return SdkTestDto */ @GetMapping("/findById") SdkTestDto findById(@RequestParam("id") String id);
/** * annoTest.* * @param cookie     cookie * @param header     header * @param id         id * @param requestDto requestDto * @return sdkTestDto */ @PostMapping("/{id}/anno") SdkTestDto annoTest(@CookieValue("cookie") String cookie, @RequestHeader("header") String header, @PathVariable("id") String id, @RequestBody SdkTestDto requestDto);
}
```

For more information, refer to the sample project [shenyu-examples-sdk-feign](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sdk/shenyu-examples-sdk-feign)

---

<a id="user-guide-sdk-usage-shenyu-sdk-nacos"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/sdk-usage/shenyu-sdk-nacos/ -->

<!-- page_index: 46 -->

# Using Nacos with Shenyu-SDK

Version: 2.7.0.3

Shenyu offers Shenyu-Sdk to make it easy for services to quickly integrate with the Shenyu gateway. By simply depending on the SDK and doing some simple configuration, client services can call the gateway's exposed APIs as if they were calling local interfaces.

![](assets/images/shenyu-sdk-process_7bd4c21ad3577744.png)

The registration center supported by the gateway for client access includes (nacos, eureka, etcd, zookeeper, consul), and the following is the relevant guide for using **nacos** registration center when `shenyu-bootstrap` and `application client` are used.

Refer to `Deployment` guide, and choose a way to start `shenyu-admin` and `shenyu-bootstrap`.

In the gateway's `pom.xml` file, introduce the following dependencies.

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-registry</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

Add the following configuration to the gateway's `yml` configuration file.

```yaml
spring: 
  application: 
    name: shenyu-bootstrap 
  cloud: 
    discovery: 
      enabled: true 
    nacos: 
      discovery: 
        server-addr: 127.0.0.1:8848 # Enter the nacos address(es), separated by commas in English. 
        enabled: true 
        namespace: ShenyuRegisterCenter # nacos namespace ID 
        # if nacos authentication is enabled, the following parameters must be configured 
        username: nacos # Authentication username 
        password: nacos # Authentication password 
```

In the `pom.xml` file of the application client, introduce the following dependencies.

- Shenyu-Sdk Core

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-sdk-core</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sdk</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
</dependencies> 
```

- Shenyu-Sdk http implementation

> HTTP client implementation, offering okhttp and httpclient as implementation options. Other implementations can be created by extending the `AbstractShenyuSdkClient` class.

```xml
<!-- httpclient --> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-httpclient</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
 
<!-- okhttp --> 
<!--  
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-okhttp</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
--> 
```

Add the following configuration in the application client's `yml` configuration file.

```yaml
shenyu: 
  sdk: 
    enabled: true 
    register-type: nacos  
    server-lists: localhost:2181 
    props: 
      nacosNameSpace: ShenyuRegisterCenter 
      username: nacos 
      password: nacos 
      retry: 
        enable: true 
        period: 100 
        maxPeriod: 1000 
        maxAttempts: 5 
      algorithm: roundRobin 
      scheme: http 
       
# registerType: service registration type, fill in nacos. 
# serverList: Enter the nacos address(es), separated by commas in English. 
# nacosNameSpace: nacos namespace ID 
# username: Authentication username 
# password: Authentication password 
# scheme: Request protocol. 
 
# retry: Configuration related to failure retries. 
# retry.period: Retry waiting time. 
# retry.maxPeriod: Maximum retry waiting time . 
# retry.maxAttempts: Maximum retry count. 
```

1. In the project startup class, annotate `@EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api")`, where `basePackages` maintains the package location of Shenyu-Sdk's corresponding maintained gateway API interface.
2. Create an interface and use the `@ShenyuClient(name = "xxx", contextId = "ShenyuSdkApiName")` annotation to mark it, where `name` represents the gateway service name. If you need to define multiple beans to maintain the gateway's API, you can use `contextId` as the corresponding bean alias.
3. In the defined interface, add the methods of the interface to be mapped to the shenyu gateway, where the `value` of `@xxMapping` corresponds to the path of the corresponding request in the gateway.

**Example**

Project startup class

```java
import org.apache.shenyu.sdk.spring.EnableShenyuClients;
@SpringBootApplication @EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api") public class ShenyuSdkHttpExampleApplication {
/** * main.* * @param args args */ public static void main(final String[] args) {SpringApplication.run(ShenyuSdkHttpExampleApplication.class, args);}}
```

Shenyu-SDK interface

```java
import org.apache.shenyu.sdk.spring.ShenyuClient;
@ShenyuClient(name = "shenyu-bootstrap", contextId = "ShenyuSdkApiName") public interface ShenyuHttpClientApi {
/** * findById.* test Get.* * @param id id * @return SdkTestDto */ @GetMapping("/http/shenyu/client/findById") SdkTestDto findById(@RequestParam("id") String id);}
```

For more information, refer to the sample project [shenyu-examples-sdk](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sdk)

---

<a id="user-guide-sdk-usage-shenyu-sdk-zookeeper"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/sdk-usage/shenyu-sdk-zookeeper/ -->

<!-- page_index: 47 -->

# Using Zookeeper with Shenyu-SDK

Version: 2.7.0.3

Shenyu offers Shenyu-Sdk to make it easy for services to quickly integrate with the Shenyu gateway. By simply depending on the SDK and doing some simple configuration, client services can call the gateway's exposed APIs as if they were calling local interfaces.

![](assets/images/shenyu-sdk-process_7bd4c21ad3577744.png)

The registration center supported by the gateway for client access includes (nacos, eureka, etcd, zookeeper, consul), and the following is the relevant guide for using **Zookeeper** registration center when `shenyu-bootstrap` and `application client` are used.

Refer to `Deployment` guide, and choose a way to start `shenyu-admin` and `shenyu-bootstrap`.

In the gateway's `pom.xml` file, introduce the following dependencies.

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-registry</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

Add the following configuration to the gateway's `yml` configuration file.

```yaml
shenyu: 
  register: 
    enabled: true 
    registerType: zookeeper 
    serverLists: localhost:2181 
    props: 
      appName: http 
      port: xx 
# registerType: service registration type, fill in zookeeper. 
# serverList: Enter the zookeeper address(es), separated by commas in English. 
# appName：Your application name. If not configured, the default value will be taken from spring.application.name. 
# port: Your project's startup port, currently springmvc/tars/grpc needs to be filled in. 
 
# for detailed reference, please see the `user-guide> Property Config> Register Center Instance Config` configuration document. 
```

In the `pom.xml` file of the application client, introduce the following dependencies.

- Shenyu-Sdk Core

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-sdk-core</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-sdk</artifactId> 
        <version>2.5.1-SNAPSHOT</version> 
    </dependency> 
</dependencies> 
```

- Shenyu-Sdk http implementation

> HTTP client implementation, offering okhttp and httpclient as implementation options. Other implementations can be created by extending the `AbstractShenyuSdkClient` class.

```xml
<!-- httpclient --> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-httpclient</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
 
<!-- okhttp --> 
<!--  
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-sdk-okhttp</artifactId> 
    <version>2.5.1-SNAPSHOT</version> 
</dependency> 
--> 
```

Add the following configuration in the application client's `yml` configuration file.

```yaml
shenyu: 
  sdk: 
    enabled: true 
    register-type: zookeeper  
    server-lists: localhost:2181 
    props: 
      retry: 
        enable: true 
        period: 100 
        maxPeriod: 1000 
        maxAttempts: 5 
      algorithm: roundRobin 
      scheme: http 
 
# register-type: service registration type, fill in zookeeper. 
# server-lists: Enter the zookeeper address(es), separated by commas in English. 
# scheme: Request protocol. 
 
# retry: Configuration related to failure retries. 
# retry.period: Retry waiting time. 
# retry.maxPeriod: Maximum retry waiting time . 
# retry.maxAttempts: Maximum retry count. 
```

1. In the project startup class, annotate `@EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api")`, where `basePackages` maintains the package location of Shenyu-Sdk's corresponding maintained gateway API interface.
2. Create an interface and use the `@ShenyuClient(name = "xxx", contextId = "ShenyuSdkApiName")` annotation to mark it, where `name` represents the gateway service name. If you need to define multiple beans to maintain the gateway's API, you can use `contextId` as the corresponding bean alias.
3. In the defined interface, add the methods of the interface to be mapped to the shenyu gateway, where the `value` of `@xxMapping` corresponds to the path of the corresponding request in the gateway.

**Example**

Project startup class

```java
import org.apache.shenyu.sdk.spring.EnableShenyuClients;
@SpringBootApplication @EnableShenyuClients(basePackages = "org.apache.shenyu.examples.sdk.http.api") public class ShenyuSdkHttpExampleApplication {
/** * main.* * @param args args */ public static void main(final String[] args) {SpringApplication.run(ShenyuSdkHttpExampleApplication.class, args);}}
```

Shenyu-SDK interface

```java
import org.apache.shenyu.sdk.spring.ShenyuClient;
@ShenyuClient(name = "shenyu-gateway", contextId = "ShenyuSdkApiName") public interface ShenyuHttpClientApi {
/** * findById.* test Get.* * @param id id * @return SdkTestDto */ @GetMapping("/http/shenyu/client/findById") SdkTestDto findById(@RequestParam("id") String id);}
```

For more information, refer to the sample project [shenyu-examples-sdk](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sdk)

---

<a id="user-guide-discovery-discovery-mode"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/discovery/discovery-mode/ -->

<!-- page_index: 48 -->

# Discovery

Version: 2.7.0.3

Discovery

- Module Design Diagram

![discovery-design.png](assets/images/discovery-design-3081f14fec1ef9322d39bd1b998f42a3_ca104e8e9422010d.png)

- Database Design

![db-design.png](assets/images/db-design-ace76c69c809afe5bf47464fc1b0209c_d24181ea4b9bd637.png)

The Discovery module endows the ShenYu Gateway with the ability to actively perceive and respond to changes in the list of services being proxied.
By actively listening to the admin service of the Discovery Gateway, the ShenYu Gateway can promptly track changes in the services being proxied.
This functionality is designed to be flexible and can be configured at either **the selector level or the plugin level**, as needed.
Currently, plugins that have incorporated the Discovery feature include TCP, Divide, Websocket and gRPC plugins.

LOCAL, ZOOKEEPER, NACOS, EUREKA, ETCD

- LOCAL Mode: Primarily relies on manual maintenance of the upstream list and pushing it to the gateway.
- ZOOKEEPER Mode: Monitors changes in ephemeral nodes under a specified node in ZooKeeper to obtain data.
- NACOS Mode: Listens for changes in instances under a specified service name in Nacos to obtain data.
- EUREKA Mode: Listens for changes in instances under a specified service name in Eureka to obtain data.
- ETCD Mode: Obtains data by monitoring changes in key-value pairs under specified nodes in etcd.

- Plugin Level: Impacts the entire plugin,
  and all selectors under that plugin will default to the current listening mode.
- Selector Level: Applies to the current selector,
  allowing different selectors under the same plugin to use different listening modes.

- In plugins that support the Discovery module (currently, only the TCP plugin supports plugin-level discovery
  configuration on the admin console page; other plugins can configure plugin-level discovery through shenyu-client,
  as described in the "Using Shenyu-client" section below), click on `Discovery Configuration`. In the popup form,
  select the desired listening mode and fill in the service discovery name, registration server URL, registry configuration parameters, etc.:

![config-discovery-plugin-en.png](assets/images/config-discovery-plugin-en-03817c824ab97b6f6144141cfbb5750f_20954dcee23d6065.png)

![config-discovery-plugin-modal-en.png](assets/images/config-discovery-plugin-modal-en-5922e43048c244e8dcd8b3eab8ad8d9b_a81dc4653b690023.png)

- To add a new selector, click on `Add Selector`. In the new selector page, you will notice that the `Type` field enforces the previously configured plugin-level listening mode,
  indicating that the added selector will also adopt the same configuration.
  At this point, simply input the desired `ListeningNode`:

  ![add-selector-under-plugin-discovery-en.png](assets/images/add-selector-under-plugin-discovery-en-bdd4aaafdff4e9cce7a2df86d5472e85_7d05cb6ae533371d.png)
- The `Handler` here refers to ShenYu's specified JSON format for transmitting upstream registration data,
  as shown below:

  - url: URL of the upstream
  - protocol: communication protocol of the upstream
  - status: status of the upstream node (0 for healthy, 1 for unhealthy)
  - weight: Used for load balancing calculations


```json
{ 
    "url": "127.0.0.1::6379",  
    "protocol": "tcp", 
    "status": 0,  
    "weight": 10 
} 
```

- If your service alias does not match ShenYu's defined JSON format,
  you can perform alias mapping in `Handler`.
  For example, as shown in the above image,
  if you need to change `status` to "healthy" while keeping other keys unchanged,
  follow these steps: create a new alias, map `status` to `healthy`,
  and retain the original JSON keys' format.
- Configure the remaining properties for the selector according to the specific plugin's documentation.

- In plugins that support the Discovery module, click on `Add Selector`.
  In the `Discovery Config` tab, configure the fields such as type,
  listening node, server URL list, and registry properties.
  This configuration only applies to the current selector and must be reconfigured each time a new selector is added.

![add-selector-en.png](assets/images/add-selector-en-f69527e00c21591f8f22a3c8c46c1dbb_ca4ae32e85e6c497.png)

- For the Divide, gRPC, and Websocket plugins,
  the `Import Background Discovery Config` function on the selector creation page
  allows you to import and use the backend configuration if the service connecting to the ShenYu Gateway
  was configured with shenyu-discovery-related properties (see usage with shenyu-client).
  As shown in the following image, click `Import Background Discovery Config` to view the backend configuration:

![config-import-en.png](assets/images/config-import-en-520151b4311fdd295879ae00da086657_f064711c08c78635.png)

- If you confirm the import, clicking the `Import` button in the backend configuration popup will automatically populate the form with the backend service discovery properties.
  At this point, you only need to configure the listening node:

![after-import-en.png](assets/images/after-import-en-1080a3e988b4efde089dddc3366ec4d0_51d81706766cc07f.png)

>
> [!NOTE]
> : If you confirm importing the backend configuration, the backend service discovery properties will be automatically filled in the form and will continue to use the previous discovery object.
> In this case, modifying service discovery properties in the form will be ineffective, and the backend configuration will be retained.

- If you choose the LOCAL mode, there is no need to connect to a registry, and users must manually maintain the upstream list.

- Local mode only supports configuration at the **selector level**.
  There is no need to connect to a registry, and users must manually maintain the upstream list.
  This list is an editable table. Click the `Edit` button for each row in the table to modify each parameter of the upstream:

![local-selector-en.png](assets/images/local-selector-en-94c6799b40684d6d04f8fc1cd8943fd2_bbfaefce7aaea919.png)

- In the ZooKeeper/Nacos/Eureka/Etcd modes, service discovery configuration is supported at both the plugin level and the selector level.

> [!NOTE]
> - For each registry property under these modes, taking ZooKeeper as an example, users can go to `shenyu-admin` --> `BasicConfig` --> `Dictionary`,
>   search for the dictionary name "zookeeper", and edit the dictionary values corresponding to the default properties
>   (: You cannot modify the dictionary type and dictionary name).
- In these modes, the gateway dynamically retrieves service instance information from the registry. Additions, removals, modifications,
  and other changes to service instances will be displayed in real-time in the upstream list.

![zk_dict_en.png](assets/images/zk-dict-en-fd86f5888a94e38c84a97588ff295e79_6bd00765d770a2cd.png)

- To use Shenyu-client, you need to depend on the corresponding mode's registry middleware: ZooKeeper, Nacos, Etcd, Eureka.
  These modes can automatically detect service up and down events through ShenYu Admin.
- Additionally, if you are using the local mode, you will need to manually maintain the upstream list.
- For detailed instructions on using Shenyu-client, refer to the Shenyu-client module documentation.

- Shenyu-client defaults to the Local mode, so there is no need for any special discovery configuration.
  It will automatically register the current service.
- For services that are automatically registered, you can manually add, modify,
  or delete them in the upstream list on the page:

![local-selector-en.png](assets/images/local-selector-en-94c6799b40684d6d04f8fc1cd8943fd2_bbfaefce7aaea919.png)

- If you are not using Shenyu-client, you can manually add, modify,
  or delete service information on the `Discovery Config` tab under `Add Selector`:

![add-selector-local-en.png](assets/images/add-selector-local-en-a27bc0cf61e1caca2e35bf405bf14079_618be2e97daa9c6c.png)

- Configure other selector information:

![add-selector-basic-en.png](assets/images/add-selector-basic-en-13721a2c3d5b2ff3eb923d6022249766_376db68cc511206a.png)

- Configure rules:

![rule-en.png](assets/images/rule-en-95ac5e751ee513a5e2f1f6df880bf892_a9ff8669526ba9b5.png)

- Test Connection

```text
curl http://localhost:9195/http/hello 
 
hello! I'm Shenyu-Gateway System. Welcome!%  
```

(Taking the Divide plugin as an example)

- Add Dependencies

```xml
<dependencies> 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-discovery-zookeeper</artifactId> 
    <version>${project.version}</version> 
  </dependency> 
 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-client-http</artifactId> 
  </dependency> 
</dependencies> 
```

- Add the Following Configuration in application.yml

```yaml
shenyu: 
   discovery: 
      enable: true 
      type: zookeeper 
      serverList: ${your.zookeeper.ip}:{your.zookeeper.port} 
      registerPath: /shenyu/discovery/demo_http_common 
      props: 
         baseSleepTimeMilliseconds: 1000 
         maxRetries: 4 
         maxSleepTimeMilliseconds: 5000 
         connectionTimeoutMilliseconds: 60000 
         sessionTimeoutMilliseconds: 8 
```

- Start the shenyu-examples-http service.
- Once the service registration is successful,
  you can view the list of automatically registered service instances on the selector page:

![zk-selector-en.png](assets/images/zk-selector-en-7d96c81ae13fa7c6e837c5adf35d28d7_0d844c33fd691822.png)

- Users can click on `Edit` in the service instance list to edit the service instance information
  (Note that in non-Local mode, the URL is maintained by the registry and cannot be manually edited):

![edit-zk-upstream-en.png](assets/images/edit-zk-upstream-en-003302d02022263db95f1e68110f441f_87eae022f7f4161e.png)

- Test Connection

```text
curl http://localhost:9195/http/hello 
 
hello! I'm Shenyu-Gateway System. Welcome!%  
```

- Add Dependencies

```xml
<dependencies> 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-discovery-etcd</artifactId> 
    <version>${project.version}</version> 
  </dependency> 
 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-client-http</artifactId> 
  </dependency> 
</dependencies> 
```

- Add the Following Configuration in application.yml

```yaml
shenyu: 
   discovery: 
      enable: true 
      protocol: http:// 
      type: etcd 
      serverList: http://${your.etcd.host}:${your.etcd.port} 
      registerPath: /shenyu/test/http_common 
      props: 
         etcdTimeout: 3000 
         etcdTTL: 5 
```

- Start the shenyu-examples-http service. Similarly, on the selector page,
  you can see the list of automatically registered service instances and edit them as needed:
  ![etcd-selector-en.png](assets/images/etcd-selector-en-32149574a23a9f958f3c51f5a4e17800_8a40da8765eb1fb3.png)
- Test Connection

```text
curl http://localhost:9195/http/hello 
 
hello! I'm Shenyu-Gateway System. Welcome!%  
```

- Add Dependencies

```xml
<dependencies> 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-discovery-eureka</artifactId> 
    <version>${project.version}</version> 
  </dependency> 
 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-client-http</artifactId> 
  </dependency> 
</dependencies> 
```

- Add the Following Configuration in application.yml
  (in this context, `registerPath` can be understood as the name of the service to be monitored):

```yaml
shenyu: 
   discovery: 
      enable: true 
      protocol: http:// 
      type: eureka 
      serverList: http://${your.eureka.host}:${your.eureka.port}/eureka 
      registerPath: shenyu_discovery_demo_http_common 
      props: 
         eurekaClientRefreshInterval: 10 
         eurekaClientRegistryFetchIntervalSeconds: 10 
```

- Start the shenyu-examples-http service. Similarly, on the selector page,
  you can see the list of automatically registered service instances and edit them as needed:

![eureka-selector-en.png](assets/images/eureka-selector-en-438b997614fcd24234dc72ee81d35be6_95dd78b70dc45a51.png)

- Test Connection

```text
curl http://localhost:9195/http/hello 
 
hello! I'm Shenyu-Gateway System. Welcome!%  
```

- Add Dependencies

```xml
<dependencies> 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-discovery-eureka</artifactId> 
    <version>${project.version}</version> 
  </dependency> 
 
  <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-client-http</artifactId> 
  </dependency> 
</dependencies> 
```

- Add the Following Configuration in application.yml
  (Here, `registerPath` can also be understood as the name of the service to be monitored.)

```yaml
shenyu: 
   discovery: 
      enable: true 
      protocol: http:// 
      type: nacos 
      serverList: ${your.nacos.host}:${your.nacos.port} 
      registerPath: shenyu_discovery_demo_http_common 
      props: 
         groupName: SHENYU_GROUP 
```

- Start the shenyu-examples-http service. Similarly, on the selector page,
  you can view the list of automatically registered service instances and edit them as needed.

![nacos-selector-en.png](assets/images/nacos-selector-en-848290702d46c73d029d688e3c3c1a03_82ba8671f8cd2573.png)

- Test Connection

```text
curl http://localhost:9195/http/hello 
 
hello! I'm Shenyu-Gateway System. Welcome!%  
```

>
> [!NOTE]
> ：Configuring service discovery using Shenyu-client essentially configures service discovery at the plugin level.
> Under the same service discovery mode, there is, in fact, only one discovery object
> (meaning you can only configure the same set of type, server URL, and service discovery parameters), while multiple listening nodes can be configured.

![ws-selector-en.png](assets/images/ws-selector-en-0646fe75699ac938f415edfc2f5fcc09_30fd085907445e5a.png)

>
> [!NOTE]
> ：In the Divide and gRPC plugins, you can modify the protocol by configuring the protocol in the application.yml file.
> The default protocol for the Websocket plugin is 'ws'.

- In local mode, you can manually modify all parameters of the upstream on the service list page.
- In non-local modes, you can manually modify parameters other than URL and start time.
- Manually changing the status (open/close) and weight of service instances only affects the current plugin.
- For the same plugin, when configuring discovery-related parameters through Shenyu-client in the backend, it essentially configures service discovery at the plugin level. Although you can manually add selectors on the console page to configure selector-level service discovery, in reality, there is only one discovery object (meaning you can only configure the same set of type, server URL, and service discovery parameters), while multiple listening nodes can be configured.

[Test Report](https://www.yuque.com/eureca/pgotw1/hkqkk5laubspgwl3#UojLR)

---

<a id="user-guide-proxy-dubbo-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/dubbo-proxy/ -->

<!-- page_index: 49 -->

# Dubbo Proxy

Version: 2.7.0.3

This document is intended to help the `Dubbo` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `Dubbo` plugin to handle `dubbo` service.

Support Alibaba Dubbo(< 2.7.x) and Apache Dubbo (>=2.7.x).

Before the connection, start `shenyu-admin` correctly, start `Dubbo` plugin, and add related dependencies on the gateway and `Dubbo` application client. Refer to the previous [Quick start with Dubbo](#quick-start-quick-start-dubbo) .

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync) .

Add these dependencies in gateway's `pom.xml`.

Alibaba dubbo user, configure the dubbo version and registry center with yours.

```xml
<!-- apache shenyu alibaba dubbo plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-client-alibaba-dubbo</artifactId> 
   <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu  alibaba dubbo plugin end--> 
<dependency> 
  <groupId>com.alibaba</groupId> 
  <artifactId>dubbo</artifactId> 
  <version>2.6.5</version> 
</dependency> 
<dependency> 
  <groupId>org.apache.curator</groupId> 
  <artifactId>curator-client</artifactId> 
  <version>4.0.1</version> 
</dependency> 
<dependency> 
  <groupId>org.apache.curator</groupId> 
  <artifactId>curator-framework</artifactId> 
  <version>4.0.1</version> 
</dependency> 
<dependency> 
  <groupId>org.apache.curator</groupId> 
  <artifactId>curator-recipes</artifactId> 
  <version>4.0.1</version> 
</dependency> 
```

Apache dubbo user, configure the dubbo version and registry center with yours.

```xml
<!-- apache shenyu apache dubbo plugin start--> 
<dependency> 
   <groupId>org.apache.shenyu</groupId> 
   <artifactId>shenyu-spring-boot-starter-client-apache-dubbo</artifactId> 
   <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu apache dubbo plugin end--> 
 
<dependency> 
   <groupId>org.apache.dubbo</groupId> 
   <artifactId>dubbo</artifactId> 
   <version>2.7.5</version> 
</dependency> 
<!-- Dubbo Nacos registry dependency start --> 
<dependency> 
   <groupId>org.apache.dubbo</groupId> 
   <artifactId>dubbo-registry-nacos</artifactId> 
   <version>2.7.5</version> 
</dependency> 
<dependency> 
   <groupId>com.alibaba.nacos</groupId> 
   <artifactId>nacos-client</artifactId> 
   <version>1.1.4</version> 
</dependency> 
<!-- Dubbo Nacos registry dependency  end--> 
 
<!-- Dubbo zookeeper registry dependency start--> 
<dependency> 
   <groupId>org.apache.curator</groupId> 
   <artifactId>curator-client</artifactId> 
   <version>4.0.1</version> 
</dependency> 
<dependency> 
   <groupId>org.apache.curator</groupId> 
   <artifactId>curator-framework</artifactId> 
   <version>4.0.1</version> 
</dependency> 
<dependency> 
   <groupId>org.apache.curator</groupId> 
   <artifactId>curator-recipes</artifactId> 
   <version>4.0.1</version> 
</dependency> 
<!-- Dubbo zookeeper registry dependency end --> 
```

- restart gateway service.

Dubbo integration with gateway, please refer to : [shenyu-examples-dubbo](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-dubbo) .

- Alibaba Dubbo User

  - SpringBoot

    Add these dependencies:


```xml
<dependency> 
     <groupId>org.apache.shenyu</groupId> 
     <artifactId>shenyu-spring-boot-starter-client-alibaba-dubbo</artifactId> 
     <version>${shenyu.version}</version> 
</dependency> 
```

  - Spring

    Add these dependencies：


```xml
   <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-client-alibaba-dubbo</artifactId> 
      <version>${shenyu.version}</version> 
   </dependency> 
```

    Inject these properties into your Spring beans XML file：


```xml
<bean id="clientConfig" class="org.apache.shenyu.register.common.config.PropertiesConfig"> 
     <property name="props"> 
       <map> 
         <entry key="contextPath" value="/你的contextPath"/> 
         <entry key="appName" value="你的名字"/> 
       </map> 
     </property> 
 </bean> 
 
 <bean id="shenyuRegisterCenterConfig" class="org.apache.shenyu.register.common.config.ShenyuRegisterCenterConfig"> 
   <property name="registerType" value="http"/> 
   <property name="serverList" value="http://localhost:9095"/> 
 </bean> 
 
 <bean id="shenyuClientRegisterRepository" class="org.apache.shenyu.client.core.register.ShenyuClientRegisterRepositoryFactory" factory-method="newInstance"> 
       <property name="shenyuRegisterCenterConfig" ref="shenyuRegisterCenterConfig"/> 
 </bean> 
 
 <bean id ="alibabaDubboServiceBeanListener" class ="org.apache.shenyu.client.alibaba.dubbo.AlibabaDubboServiceBeanListener"> 
   <constructor-arg name="clientConfig" ref="clientConfig"/> 
   <constructor-arg name="shenyuClientRegisterRepository" ref="shenyuClientRegisterRepository"/>  
 </bean> 
```

- Apache Dubbo User

  - SpringBoot

    Add these dependencies:


```xml
 <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-client-apache-dubbo</artifactId> 
      <version>${shenyu.version}</version> 
 </dependency> 
```

    Add these in your client project's application.yml:


```yml
dubbo: 
  registry: 
    address: dubbo register address 
    port: dubbo service port 
 
shenyu: 
  register: 
    registerType: shenyu service register type #http #zookeeper #etcd #nacos #consul 
    serverLists: shenyu service register address #http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
  client: 
    dubbo: 
      props: 
        contextPath: /your contextPath 
        appName: your app name 
```

  - Spring

    Add these dependencies:


```xml
   <dependency> 
       <groupId>org.apache.shenyu</groupId> 
       <artifactId>shenyu-client-apache-dubbo</artifactId> 
       <version>${shenyu.version}</version> 
    </dependency> 
```

    Injecct these properties into your Spring beans XML file:


```xml
<bean id = "apacheDubboServiceBeanListener" class="org.apache.shenyu.client.apache.dubbo.ApacheDubboServiceBeanListener"> 
    <constructor-arg ref="clientPropertiesConfig"/> 
    <constructor-arg ref="clientRegisterRepository"/> 
</bean> 
 
 <!-- Config register repository according to your register type --> 
 <bean id="shenyuRegisterCenterConfig" class="org.apache.shenyu.register.common.config.ShenyuRegisterCenterConfig"> 
     <property name="registerType" value="your service registerType"/> 
     <property name="serverLists" value="your service register serverLists"/> 
 </bean> 
 
 <!-- Client properties config --> 
 <bean id="clientPropertiesConfig" 
    class="org.apache.shenyu.register.common.config.ShenyuClientConfig.ClientPropertiesConfig"> 
    <property name="props"> 
        <map> 
            <entry key="contextPath" value="/your contextPath"/> 
            <entry key="appName" value="your appName"/> 
        </map> 
    </property> 
 </bean> 
 
<!-- Config register repository according to your register type --> 
<bean id="clientRegisterRepository" class="org.apache.shenyu.register.client.http.HttpClientRegisterRepository"> 
    <constructor-arg ref="shenyuRegisterCenterConfig"/> 
</bean> 
 
<bean id="shenyuClientShutdownHook" class="org.apache.shenyu.client.core.shutdown.ShenyuClientShutdownHook"> 
    <constructor-arg ref="shenyuRegisterCenterConfig"/> 
    <constructor-arg ref="clientRegisterRepository"/> 
</bean> 
```

    Add these in your client project's application.yml:


```yml
dubbo: 
  registry: 
    address: dubbo register address 
    port: dubbo service port 
```

- Enable `dubbo` option in `shenyu-admin`.
- Configure your registry address in `dubbo`.

```yaml
{"register":"zookeeper://localhost:2181"}   or {"register":"nacos://localhost:8848"} 
```

- you can add the annotation `@ShenyuDubboClient` to your dubbo service implementation class, so that the interface method will be configured with gateway.
- Start your provider. After successful startup, go to PluginList -> rpc Proxy -> dubbo in the backend management system. You will see auto-registered selectors and rules information.

- Communicate with dubbo service through Http transport protocol.
- Apache ShenYu gateway need a route prefix which configured when accessing the project.

```yaml
# for example: you have an order service and it has a interface, registry address: /order/test/save 
 
# now we can communicate with gateway through POST request http://localhost:9195/order/test/save 
 
# localhost:9195 is gateway's ip port，default port is 9195 ，/order is the contextPath you set through gateway. 
```

- parameter deliver:
  - communicate with gateway through body or json of http post request.
  - more parameter types, please refer to the interface definition in [shenyu-examples-dubbo](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-dubbo) and parameter passing
    method.
- Single java bean parameter type (`default`).
- Multi-parameter type support, add this config value in gateway's yaml file:

```yaml
shenyu: 
  dubbo: 
    parameter: multi 
```

- Support for customized multi-parameter type
- Create a new implementation class `MyDubboParamResolveService` in your gateway project of `org.apache.shenyu.web.dubbo.DubboParamResolveService`.

```java
public interface DubboParamResolveService {
/** * Build parameter pair.* this is Resolve http body to get dubbo param.* * @param body           the body * @param parameterTypes the parameter types * @return the pair */ Pair<String[], Object[]> buildParameter(String body, String parameterTypes);}
```

- `body` is the json string in http request.
- `parameterTypes`: the list of method parameter types that are matched，split with `,`.
- in Pair，left is parmeter type，right is parameter value, it's the standard of dubbo generalization calls.
- Inject your class into Spring bean, cover the default implementation.

```java
@Bean 
public DubboParamResolveService myDubboParamResolveService() { 
      return new MyDubboParamResolveService(); 
} 
```

- Tag route
  - Add `Dubbo_Tag_Route` when send request, the current request will be routed to the provider of the specified tag, which is only valid for the current request.
- Explicit Target
  - Set the `url` property in the annotation `@ShenyuDubboClient`.
  - Update the configuration in Admin.
  - It's valid for all request.
- Param valid and ShenyuException
  - Set `validation="shenyuValidation"`.
  - When `ShenyuException` is thrown in the interface, exception information will be returned. It should be noted that `ShenyuException` is thrown explicitly.


```java
@Service(validation = "shenyuValidation") public class TestServiceImpl implements TestService {
@Override @ShenyuDubboClient(path = "/test", desc = "test method") public String test(@Valid HelloServiceRequest name) throws ShenyuException {if (true){throw new ShenyuException("Param binding error.");} return "Hello " + name.getName();}}
```

  - Request param


```java
public class HelloServiceRequest implements Serializable {
private static final long serialVersionUID = -5968745817846710197L;
@NotEmpty(message = "name cannot be empty") private String name;
@NotNull(message = "age cannot be null") private Integer age;
public String getName() {return name;}
public void setName(String name) {this.name = name;}
public Integer getAge() {return age;}
public void setAge(Integer age) {this.age = age;}}
```

  - Send request


```json
{ 
    "name": "" 
} 
```

  - Response


```json
{ 
    "code": 500, 
    "message": "Internal Server Error", 
    "data": "name cannot be empty,age cannot be null" 
} 
```

  - Error message


```json
{ 
    "code": 500, 
    "message": "Internal Server Error", 
    "data": "Param binding error." 
} 
```

It basically switches from HTTP request to Dubbo protocol, then invoke Dubbo service and return to the result.
Two things need to notice after intgeration with gateway, one is the added annoation `@ShenyuDubboClient`, another is a path used to speicify the request path.
And you added a config value of `contextPath`.

If you have a function like this, the config value in contextPath is `/dubbo`

```java
    @Override 
    @ShenyuDubboClient(path = "/insert", desc = "insert data") 
    public DubboTest insert(final DubboTest dubboTest) { 
        return dubboTest; 
    } 
```

So our request path is: <http://localhost:9195/dubbo/insert>, localhost:9195 is the gateway's domain name,if you changed before,so does with yours here..

`DubboTest` is a java bean object，has 2 parameters, id and name, so we can transfer the value's json type through request body.

```text
{"id":"1234","name":"XIAO5y"} 
```

If your interface has no parameter, then the value is:

```text
{} 
```

If the interface has multiple parameters, refer to the multi-parameter type support described above.

---

<a id="user-guide-proxy-grpc-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/grpc-proxy/ -->

<!-- page_index: 50 -->

# gRPC Proxy

Version: 2.7.0.3

This document is intended to help the `gRPC` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `gRPC` plugin to handle `gRPC` service.

Before the connection, start `shenyu-admin` correctly, start `gRPC` plugin, and add related dependencies on the gateway and `gRPC` application client. Refer to the previous [Quick start with gRPC](#quick-start-quick-start-grpc) .

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync) .

Add the following dependencies in the gateway's `pom.xml` file:

```xml
        <!-- apache shenyu grpc plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-grpc</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <!-- apache shenyu grpc plugin end--> 
```

- Restart the gateway service.

You can refer to：[shenyu-examples-grpc](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-grpc) .

1. In the microservice built by `gRPC`, add the following dependencies:

```xml
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-grpc</artifactId> 
            <version>${shenyu.version}</version> 
            <exclusions> 
                <exclusion> 
                    <artifactId>guava</artifactId> 
                    <groupId>com.google.guava</groupId> 
                </exclusion> 
            </exclusions> 
        </dependency> 
```

Execute command to generate java code in `shenyu-examples-grpc` project.

```shell
mvn protobuf:compile  
mvn protobuf:compile-custom  
```

2. Add the following configuration to application.yaml:

```yaml
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    grpc: 
      props: 
        contextPath: /grpc 
        appName: grpc 
        ipAndPort: 127.0.0.1:38080 
        port: 38080 
```

3. Add `@ShenyuGrpcClient` Annotation on the `gRPC` service interface implementation class. Start your service provider, after successful registration, in the background management system go to PluginList -> rpc proxy -> gRPC, you will see automatic registration of selectors and rules information.

Example:

```java
    @Override 
    @ShenyuGrpcClient(path = "/echo", desc = "echo") 
    public void echo(EchoRequest request, StreamObserver<EchoResponse> responseObserver) { 
        System.out.println("Received: " + request.getMessage()); 
        EchoResponse.Builder response = EchoResponse.newBuilder() 
                .setMessage("ReceivedHELLO") 
                .addTraces(Trace.newBuilder().setHost(getHostname()).build()); 
        responseObserver.onNext(response.build()); 
        responseObserver.onCompleted(); 
    } 
 
```

You can request your gRPC service by Http. The `Apache ShenYu` gateway needs to have a route prefix that you access to configure `contextPath`.

If your `proto` file is defined as follows:

```protobuf
message EchoRequest { 
  string message = 1; 
} 
```

So the request parameters look like this:

```json
{ 
    "data": [ 
        { 
            "message": "hello grpc" 
        } 
    ] 
} 
```

The parameters are currently passed in `json` format, and the name of `key` defaults to `data`, which you can reset in `GrpcConstants.JSON_DESCRIPTOR_PROTO_FIELD_NAME`; The `value` is passed in according to the `proto` file you define.

the Apache ShenYu can support streaming calls to `gRPC` service, passing multiple arguments in the form of an array.

If your `proto` file is defined as follows:

```protobuf
message RequestData { 
  string text = 1; 
} 
```

The corresponding method call request parameters are as follows:

- `UNARY`

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

- `CLIENT_STREAMING`

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

- `SERVER_STREAMING`

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

- `BIDI_STREAMING`

```json
{ 
    "data": [ 
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        },  
        { 
            "text": "hello grpc" 
        } 
    ] 
} 
```

---

<a id="user-guide-proxy-http-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/http-proxy/ -->

<!-- page_index: 51 -->

# Http Proxy

Version: 2.7.0.3

This document is intended to help the `Http` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `Divide` plugin to handle `Http` requests.

Before the connection, start `shenyu-admin` correctly, start `Divide` plugin, and add related dependencies on the gateway and `Http` application client. Refer to the previous [Quick start with Http](#quick-start-quick-start-http) .

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync) .

- Add the following dependencies to the gateway's `pom.xml` file:


```xml
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-plugin-divide</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
```

- SpringBoot

  Please refer this：[shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http)

  1. Add the following dependencies to the `pom.xml` file in your `Http` service:


```xml
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-client-springmvc</artifactId> 
        <version>${shenyu.version}</version> 
    </dependency> 
```

  2. Add the following configuration to application.yaml:


```yaml
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    http: 
      props: 
        contextPath: /http 
        appName: http 
  #      port: 8189 
```

- SpringMvc

  Please refer this：[shenyu-examples-springmvc](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-springmvc)

  Add the following dependencies to the `pom.xml` file in your `Http` service:


```xml
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-client-springmvc</artifactId> 
        <version>${shenyu.version}</version> 
    </dependency> 
```

  Add the following to the `XML` file defined by your `bean` :


```xml
   <bean id="springMvcClientBeanPostProcessor" class="org.apache.shenyu.client.springmvc.init.SpringMvcClientBeanPostProcessor"> 
       <constructor-arg ref="clientPropertiesConfig"/> 
       <constructor-arg ref="clientRegisterRepository"/> 
   </bean> 
        
   <!-- Config register center according to your register type--> 
   <bean id="shenyuRegisterCenterConfig" class="org.apache.shenyu.register.common.config.ShenyuRegisterCenterConfig"> 
       <property name="registerType" value="http"/> 
       <property name="serverLists" value="http://localhost:9095"/> 
   </bean> 
 
   <!-- Client properties config --> 
   <bean id="clientPropertiesConfig" 
         class="org.apache.shenyu.register.common.config.ShenyuClientConfig.ClientPropertiesConfig"> 
     <property name="props"> 
         <map> 
             <entry key="contextPath" value="/your contextPath"/> 
             <entry key="appName" value="your appName"/> 
             <entry key="port" value="your port"/> 
             <entry key="isFull" value="false"/> 
         </map> 
     </property> 
   </bean> 
 
   <!-- Config register repository according to your register type --> 
   <bean id="clientRegisterRepository" class="org.apache.shenyu.register.client.http.HttpClientRegisterRepository"> 
       <constructor-arg ref="shenyuRegisterCenterConfig"/> 
   </bean> 
    
   <bean id="shenyuClientShutdownHook" class="org.apache.shenyu.client.core.shutdown.ShenyuClientShutdownHook"> 
       <constructor-arg ref="shenyuRegisterCenterConfig"/> 
       <constructor-arg ref="clientRegisterRepository"/> 
   </bean> 
    
   <bean id="contextRegisterListener" class="org.apache.shenyu.client.springmvc.init.ContextRegisterListener"> 
       <constructor-arg ref="clientPropertiesConfig"/> 
   </bean> 
```

  Add this annotation `@ShenyuSpringMvcClient` in your `controller` interface.

  You can apply the annotation to class-level in a controller. The name of the `path` variable is prefix and `/**` will apply proxy for entire interfaces.

Example(1)

The following indicates that `/test/payment`, `/test/findByUserId` will be proxy by the gateway.

```java
  @RestController 
  @RequestMapping("/test") 
  @ShenyuSpringMvcClient(path = "/test/**") 
  public class HttpTestController { 
 
      @PostMapping("/payment") 
      public UserDTO post(@RequestBody final UserDTO userDTO) { 
          return userDTO; 
      } 
 
      @GetMapping("/findByUserId") 
      public UserDTO findByUserId(@RequestParam("userId") final String userId) { 
          UserDTO userDTO = new UserDTO(); 
          userDTO.setUserId(userId); 
          userDTO.setUserName("hello world"); 
          return userDTO; 
      } 
   } 
```

Example(2)

The following indicates that `/order/save` is proxied by the gateway, while `/order/findById` is not.

```java
  @RestController 
  @RequestMapping("/order") 
  @ShenyuSpringMvcClient(path = "/order") 
  public class OrderController { 
 
      @PostMapping("/save") 
      @ShenyuSpringMvcClient(path = "/save") 
      public OrderDTO save(@RequestBody final OrderDTO orderDTO) { 
          orderDTO.setName("hello world save order"); 
          return orderDTO; 
      } 
 
      @GetMapping("/findById") 
      public OrderDTO findById(@RequestParam("id") final String id) { 
          OrderDTO orderDTO = new OrderDTO(); 
          orderDTO.setId(id); 
          orderDTO.setName("hello world findById"); 
          return orderDTO; 
      } 
  } 
```

example (3)：This is a simplified way to use it, just need a simple annotation to register to the gateway using metadata.
Special note: currently only supports `@RequestMapping, @GetMapping, @PostMapping, @DeleteMapping, @PutMapping` annotations, and only valid for the first path in `@XXXMapping`

```java
@RestController @RequestMapping("new/feature") public class NewFeatureController {
/** * no support gateway access api.* * @return result */ @RequestMapping("/gateway/not") public EntityResult noSupportGateway() {return new EntityResult(200, "no support gateway access");}
/** * Do not use shenyu annotation path. used request mapping path.* * @return result */ @RequestMapping("/requst/mapping/path") @ShenyuSpringCloudClient public EntityResult requestMappingUrl() {return new EntityResult(200, "Do not use shenyu annotation path. used request mapping path");}
/** * Do not use shenyu annotation path. used post mapping path.* * @return result */ @PostMapping("/post/mapping/path") @ShenyuSpringCloudClient public EntityResult postMappingUrl() {return new EntityResult(200, "Do not use shenyu annotation path. used post mapping path");}
/** * Do not use shenyu annotation path. used post mapping path.* * @return result */ @GetMapping("/get/mapping/path") @ShenyuSpringCloudClient public EntityResult getMappingUrl() {return new EntityResult(200, "Do not use shenyu annotation path. used get mapping path");}}
```

- Start your project, your service interface is connected to the gateway, go to the `shenyu-admin` management system plugin list `->` HTTP process `->` Divide, see automatically created selectors and rules.

- First, find `divide` plugin in `shenyu-admin`, add selector, and rules, and filter traffic matching.
- If you don't know how to configure, please refer to [Selector Detailed Explanation](#user-guide-admin-usage-selector-and-rule).
- You can also develop your customized http-client，refer to [multi-language Http client development](#developer-developer-shenyu-client)。

- Send the request as before, only two points need to notice.
- Firstly, the domain name that requested before in your service, now need to replace with gateway's domain name.
- Secondly, `Apache ShenYu` Gateway needs a route prefix which comes from `contextPath`, it configured during the integration with gateway, you can change it freely in `divide` plugin of `shenyu-admin`, if you are familiar with it.

  - for example, if you have an `order` service, and it has an interface, the request url: `http://localhost:8080/test/save`
  - Now need to change to: `http://localhost:9195/order/test/save`
  - We can see `localhost:9195` is your gateway's `ip` port，default port number is `9195` ，`/order` is your `contextPath` which you configured with gateway.
  - Other parameters doesn't change in request method.
- Then you can visit, very easy and simple.

---

<a id="user-guide-proxy-mcp-tool-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/mcp-tool-proxy/ -->

<!-- page_index: 52 -->

# McpTool Service Integration

Version: 2.7.0.3

This document is intended to help the `mcpTool` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `mcpServer` plugin to connect with `mcpTool` services.

Before the connection, start `shenyu-admin` correctly, start `mcpServer` plugin and add related dependencies on the gateway and `mcpTool` application client service side. You can refer to the previous [Quick Start with McpServer](https://shenyu.apache.org/docs/quick-start/quick-start-McpServer).

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync) .

- Add the following dependencies to the gateway’s `pom.xml` file:

```xml
    <!--Mcp Server Plugin Start--> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-spring-boot-starter-plugin-mcp-server</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
    <!--Mcp Server Plugin End--> 
```

Refer to the example project: [shenyu-examples-mcp](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-mcp)

- `SpringBoot` Users

  1. Add the following dependencies to your `mcpTool` service’s `pom.xml` file:


```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-client-mcp</artifactId> 
    <version>${shenyu.version}</version> 
</dependency> 
```

  2. Add the following configuration in `application.yaml`:


```yaml
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    mcp: 
      props: 
        contextPath: /mcp 
        appName: mcp 
```

- `Spring` Users

  Add the following dependencies to your HTTP service’s `pom.xml` file:


```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-client-mcp</artifactId> 
    <version>${shenyu.version}</version> 
</dependency> 
```

  Then add the following bean definitions to your XML configuration file:


```xml
<bean id="clientConfig" class="org.apache.shenyu.register.common.config.PropertiesConfig"> 
    <property name="props"> 
      <map> 
        <entry key="contextPath" value="/yourContextPath"/> 
        <entry key="appName" value="yourAppName"/> 
      </map> 
    </property> 
</bean> 
 
<bean id="shenyuRegisterCenterConfig" class="org.apache.shenyu.register.common.config.ShenyuRegisterCenterConfig"> 
   <property name="registerType" value="http"/> 
   <property name="serverList" value="http://localhost:9095"/> 
</bean> 
 
<bean id="shenyuClientRegisterRepository" class="org.apache.shenyu.client.core.register.ShenyuClientRegisterRepositoryFactory" factory-method="newInstance"> 
       <property name="shenyuRegisterCenterConfig" ref="shenyuRegisterCenterConfig"/> 
 </bean> 
 
<bean id="McpServiceEventListener" class="org.apache.shenyu.client.mcp.McpServiceEventListener"> 
   <constructor-arg name="clientConfig" ref="clientConfig"/> 
   <constructor-arg name="shenyuClientRegisterRepository" ref="shenyuClientRegisterRepository"/> 
   <constructor-arg name="env" ref="environment"/>   
</bean> 
```

  Add the `@ShenyuMcpTool` annotations to your controller interfaces.

  You need to add the `@ShenyuMcpTool` annotation on the `Controller` class. Only controllers annotated with `@ShenyuMcpTool` will be recognized as `mcpTool`.

This example demonstrates full McpTool configuration. You can fully customize your configuration by annotations, including parameter information defined in the operation.

```java
@GetMapping("/findById") @ShenyuMcpTool(operation = @Operation(method = "GET", description = "find order by id" ),requestConfig = @ShenyuMcpRequestConfig(bodyToJson = "false",headers = {@ShenyuMcpHeader(key = "aaa", value = "bbb")} ),enabled = true, toolName = "findOrderById") @ApiDoc(desc = "findById") public OrderDTO findById(@ShenyuMcpToolParam(parameter = @Parameter(name = "id",in = ParameterIn.PATH,description = "the id of order",required = true,schema = @Schema(type = "string",defaultValue = "1")) ) @RequestParam("id") final String id) {OrderDTO dto = new OrderDTO(); dto.setId(id); return dto;}
```

This example shows the configuration for a McpTool function without parameters.

```java
@GetMapping("/findAll") @ShenyuMcpTool(operation = @Operation(method = "GET", description = "find all order" ),requestConfig = @ShenyuMcpRequestConfig(bodyToJson = "false",headers = {@ShenyuMcpHeader(key = "aaa", value = "bbb")} ),enabled = true, toolName = "findAllOrder") @ApiDoc(desc = "findAll") public String findAll() {return "hello apache shenyu , mcp findAll success";}
```

This is a simplified usage that requires only a simple annotation to register the `McpTool` to the gateway.

> Special note: Currently only supports `@RequestMapping`, `@GetMapping`, `@PostMapping`, `@DeleteMapping`, and `@PutMapping` annotations. Only the first path of the `@XXXMapping` annotation is effective.

```java
@GetMapping("/findByName") 
@ShenyuMcpTool 
@ApiDoc(desc = "findName") 
public OrderDTO findByName(@ShenyuMcpToolParam final String name) { 
        OrderDTO dto = new OrderDTO(); 
        dto.setName(name); 
        return dto; 
} 
```

- Start your project. Your service interfaces will be connected to the gateway. In the `shenyu-admin` backend management system, go to `Plugin List -> HTTP process -> mcpServer`, and you will see the automatically created endpoints and Tools.

- First, find the `mcpServer` plugin in `shenyu-admin`, then add selectors and rules to filter traffic accordingly.
- If you are unsure how to configure, please refer to [Selector and Rule Management](#user-guide-admin-usage-selector-and-rule).

After your `mcpTool` service is connected to the `Apache ShenYu` gateway, you can use the `endPoint` configured in the `Selector` as the request interface for your `McpClient`.

- Firstly, the domain name of your previous `endPoint` was your own service; now it should be replaced with the gateway’s domain name.
- Secondly, the `Apache ShenYu` gateway requires a route prefix configured as the `contextPath` in your integration project.

  - In the `mcpServer` plugin, this `contextPath` corresponds to your `endPoint`.
  - For example, if you configured `contextPath` as `mcp`, then your `endPoint` should be configured as: `http://localhost:9195/mcp/sse`.
  - Here, `localhost:9195` is the IP and port of your gateway (default port is `9195`), and `/mcp` is the `contextPath` configured during integration.
- Third, the mcpServer plugin does not include request forwarding functionality. To perform remote tool invocation, please enable the corresponding proxy plugin for proxying. You can refer to [Quick Start with McpServer](https://shenyu.apache.org/docs/quick-start/quick-start-McpServer).

Then you can invoke tools via the `mcpClient` through the gateway easily.

---

<a id="user-guide-proxy-motan-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/motan-proxy/ -->

<!-- page_index: 53 -->

# Motan Proxy

Version: 2.7.0.3

This document is intended to help the `Motan` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `Motan` plugin to handle `motan` service.

Before the connection, start `shenyu-admin` correctly, start `Motan` plugin, and add related dependencies on the gateway and `Motan` application client. Refer to the previous [Quick start with Motan](#quick-start-quick-start-motan) .

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync) .

Add the following dependencies to the gateway's `pom.xml` file:

```xml
        <!-- apache shenyu motan plugin --> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-motan</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-core</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-registry-zookeeper</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-transport-netty4</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
        <dependency> 
            <groupId>com.weibo</groupId> 
            <artifactId>motan-springsupport</artifactId> 
            <version>1.1.9</version> 
        </dependency> 
```

- Restart your gateway service.

Please refer to: [shenyu-examples-motan](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-motan)

1. In the microservice built by `Motan`, add the following dependencies:

```xml
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-motan</artifactId> 
            <version>${shenyu.version}</version> 
        </dependency> 
```

2. Add the following configuration to the `application.yaml` configuration file:

```yaml
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    motan: 
      props: 
        contextPath: /motan 
        ipAndPort: motan 
        appName: motan 
        port: 8081 
      package-path: org.apache.shenyu.examples.motan.service 
      basicServiceConfig: 
        exportPort: 8002 
motan: 
  registry: 
    protocol: zookeeper 
    address: 127.0.0.1:2181 
```

3. Add `@ShenyuMotanClient` annotation to the method of `Motan` service interface implementation class, start your service provider, after successful registration, go to PluginList -> rpc proxy -> motan in the background management system, you will see automatic registration of selectors and rules information.

Example:

```java
@MotanService(export = "demoMotan:8002") public class MotanDemoServiceImpl implements MotanDemoService {@Override @ShenyuMotanClient(path = "/hello") public String hello(String name) {return "hello " + name;}}
```

You can request your `motan` service by Http. The `Apache ShenYu` gateway needs to have a route prefix which is the `contextPath` configured by the access gateway. For example: `http://localhost:9195/motan/hello` .

---

<a id="user-guide-proxy-sofa-rpc-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/sofa-rpc-proxy/ -->

<!-- page_index: 54 -->

# Sofa Proxy

Version: 2.7.0.3

This document is intended to help the `Sofa` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `Sofa` plugin to handle `sofa` service.

Before the connection, start `shenyu-admin` correctly, start `Sofa` plugin, and add related dependencies on the gateway and `Sofa` application client. Refer to the previous [Quick start with Sofa](#quick-start-quick-start-sofa) .

For the use of the plugin, see：[Sofa Plugin](#plugin-center-proxy-sofa-plugin)

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync) .

> In the current version, this dependency has been introduced by default.

1. Add the following dependencies in the gateway's `pom.xml` file：

```xml
       <dependency> 
           <groupId>com.alipay.sofa</groupId> 
           <artifactId>sofa-rpc-all</artifactId> 
           <version>5.7.6</version> 
           <exclusions> 
               <exclusion> 
                   <groupId>net.jcip</groupId> 
                   <artifactId>jcip-annotations</artifactId> 
               </exclusion> 
           </exclusions> 
       </dependency> 
       <dependency> 
           <groupId>org.apache.curator</groupId> 
           <artifactId>curator-client</artifactId> 
           <version>4.0.1</version> 
       </dependency> 
       <dependency> 
           <groupId>org.apache.curator</groupId> 
           <artifactId>curator-framework</artifactId> 
           <version>4.0.1</version> 
       </dependency> 
       <dependency> 
           <groupId>org.apache.curator</groupId> 
           <artifactId>curator-recipes</artifactId> 
           <version>4.0.1</version> 
       </dependency> 
       <dependency> 
           <groupId>org.apache.shenyu</groupId> 
           <artifactId>shenyu-spring-boot-starter-plugin-sofa</artifactId> 
           <version>${project.version}</version> 
       </dependency> 
```

2. Restart the gateway service.

Please refer to：[shenyu-examples-sofa](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sofa)

1. Based on the `springboot` project，Introduce the following dependencies：

```xml
        <dependency> 
            <groupId>com.alipay.sofa</groupId> 
            <artifactId>rpc-sofa-boot-starter</artifactId> 
            <version>${rpc-sofa-boot-starter.version}</version> 
        </dependency> 
				<dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-sofa</artifactId> 
            <version>${shenyu.version}</version> 
        </dependency> 
```

2. Configure in application.yml

```yaml
com: 
  alipay: 
    sofa: 
      rpc: 
        registry-address: zookeeper://127.0.0.1:2181 # consul # nacos 
        bolt-port: 8888 
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    sofa: 
      props: 
        contextPath: /sofa 
        ipAndPort: sofa 
        appName: sofa 
        port: 8888 
```

3. Configure the service interface exposed by the sofa service in the xml file in the resources.

```xml
<beans xmlns="http://www.springframework.org/schema/beans" 
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
       xmlns:sofa="http://sofastack.io/schema/sofaboot" 
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd 
            http://sofastack.io/schema/sofaboot https://sofastack.io/schema/sofaboot.xsd" 
       default-autowire="byName"> 
    <sofa:service ref="sofaSingleParamService" interface="org.apache.shenyu.examples.sofa.api.service.SofaSingleParamService"> 
        <sofa:binding.bolt/> 
    </sofa:service> 
    <sofa:service ref="sofaMultiParamService" interface="org.apache.shenyu.examples.sofa.api.service.SofaMultiParamService"> 
        <sofa:binding.bolt/> 
    </sofa:service> 
</beans> 
```

4. Add the `@ShenyuSofaClient` annotation to the interface

```java
@ShenyuSofaClient("/demo") @Service public class SofaClientMultiParamServiceImpl implements SofaClientMultiParamService {
@Override @ShenyuSofaClient("/findByIdsAndName") public SofaSimpleTypeBean findByIdsAndName(final List<Integer> ids, final String name) {return new SofaSimpleTypeBean(ids.toString(), "hello world shenyu sofa param findByIdsAndName ：" + name);}}
```

5. Start the `sofa` service, and after successful registration:

- Go to `PluginList -> Proxy -> Sofa` in the backend management system, you will see the information of auto-registered selectors and rules.
- Go to `BasicConfig -> Metadata` and search by app name . You will see the metadata of sofa, each `sofa` interface method, will correspond to a metadata.

- The gateway can be requested by means of `http` to request your `sofa` service.
  - ShenYu gateway needs to have a routing prefix, this routing prefix is for you to access the project for configuration `contextPath` .

> For example, if you have an `order` service, it has an interface and its registration path `/order/test/save`
>
> Now it's to request the gateway via post：`http://localhost:9195/order/test/save`
>
> Where `localhost:9195` is the IP port of the gateway, default port is `9195`, `/order` is the `contextPath` of your sofa access gateway configuration.

- Parameter passing：

  - Access the gateway through http post，and pass through body and json.
  - For more parameter type transfer, please refer to the interface definition in [shenyu-examples-sofa](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sofa) and the parameter transfer method.
- Single java bean parameter type (default)
- Customize multi-parameter support:
- In the gateway project you built, add a new class `MySofaParamResolveService`, implements `org.apache.shenyu.plugin.api.sofa.SofaParamResolveService` .

```java
public interface SofaParamResolveService {
/** * Build parameter pair.* this is Resolve http body to get sofa param.* * @param body           the body * @param parameterTypes the parameter types * @return the pair */ Pair<String[], Object[]> buildParameter(String body, String parameterTypes);}
```

- `body` is the json string passed by body in http.
- `parameterTypes`: list of matched method parameter types, If there are multiple, use `,` to separate.
- In Pair，left is the parameter type，and right is the parameter value. This is the standard for sofa generalization calls.
- Register your class as a String bean and override the default implementation.

```java
@Bean 
public SofaParamResolveService mySofaParamResolveService() { 
  return new MySofaParamResolveService(); 
} 
```

---

<a id="user-guide-proxy-spring-cloud-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/spring-cloud-proxy/ -->

<!-- page_index: 55 -->

# Spring Cloud Proxy

Version: 2.7.0.3

This document is intended to help the `Spring Cloud` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `springCloud` plugin to handle `Spring Cloud` service.

Before the connection, start `shenyu-admin` correctly, start `springCloud` plugin, and add related dependencies on the gateway and `springCloud` application client. Refer to the previous [Quick start with Spring Cloud](#quick-start-quick-start-springcloud) .

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync) .

- add these dependencies in gateway's pom.xml:

```xml
  <!-- apache shenyu springCloud plugin start--> 
  <dependency> 
       <groupId>org.apache.shenyu</groupId> 
       <artifactId>shenyu-spring-boot-starter-plugin-springcloud</artifactId> 
        <version>${project.version}</version> 
  </dependency> 
 
  <dependency> 
       <groupId>org.apache.shenyu</groupId> 
       <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> 
       <version>${project.version}</version> 
   </dependency> 
   <!-- apache shenyu springCloud plugin end--> 
 
   <dependency> 
        <groupId>org.springframework.cloud</groupId> 
        <artifactId>spring-cloud-commons</artifactId> 
        <version>2.2.0.RELEASE</version> 
   </dependency> 
```

- If you use `eureka` as SpringCloud registry center.

  add these dependencies:

```xml
  <dependency> 
       <groupId>org.springframework.cloud</groupId> 
       <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId> 
       <version>2.2.0.RELEASE</version> 
  </dependency> 
```

add these config values in gateway's yaml file:

```yaml
   eureka: 
     client: 
       serviceUrl: 
         defaultZone: http://localhost:8761/eureka/ #your eureka address 
     instance: 
       prefer-ip-address: true 
```

- if you use `nacos` as Spring Cloud registry center.

  add these dependencies:

```xml
 <dependency> 
       <groupId>com.alibaba.cloud</groupId> 
       <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId> 
       <version>2.1.0.RELEASE</version> 
 </dependency> 
```

add these config values in gateway's yaml file:

```yaml
  spring: 
     cloud: 
       nacos: 
         discovery: 
            server-addr: 127.0.0.1:8848 # your nacos address 
```

Special note: Please ensure that the spring Cloud registry service discovery configuration is enabled

- Configuration method

```yml
spring: 
  cloud: 
    discovery: 
      enabled: true 
```

- code method

```java
@SpringBootApplication @EnableDiscoveryClient public class ShenyuBootstrapApplication {
/** * Main Entrance.* * @param args startup arguments */ public static void main(final String[] args) {SpringApplication.run(ShenyuBootstrapApplication.class, args);}}
```

- restart your gateway service.

Please refer to [shenyu-examples-springcloud](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-springcloud)

- Add the following dependencies to your `Spring Cloud` microservice :

```xml
 <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-client-springcloud</artifactId> 
      <version>${shenyu.version}</version> 
 </dependency> 
```

- Add the annotation `@ShenyuSpringCloudClient` in your `controller` interface. you can apply the annotation to class-level in a controller.the name of the path variable is prefix and '/\*\*' will apply proxy for entire interfaces.
- example (1)：both `/test/payment` and `/test/findByUserId` will be handled by gateway.

```java
 @RestController 
 @RequestMapping("/test") 
 @ShenyuSpringCloudClient(path = "/test/**") 
 public class HttpTestController { 
 
     @PostMapping("/payment") 
     public UserDTO post(@RequestBody final UserDTO userDTO) { 
         return userDTO; 
     } 
 
     @GetMapping("/findByUserId") 
     public UserDTO findByUserId(@RequestParam("userId") final String userId) { 
         UserDTO userDTO = new UserDTO(); 
         userDTO.setUserId(userId); 
         userDTO.setUserName("hello world"); 
         return userDTO; 
     } 
  } 
```

example (2)：`/order/save` will be handled by gateway, and `/order/findById` won't.

```java
 @RestController 
 @RequestMapping("/order") 
 @ShenyuSpringCloudClient(path = "/order") 
 public class OrderController { 
 
     @PostMapping("/save") 
     @ShenyuSpringMvcClient(path = "/save") 
     public OrderDTO save(@RequestBody final OrderDTO orderDTO) { 
         orderDTO.setName("hello world save order"); 
         return orderDTO; 
     } 
 
     @GetMapping("/findById") 
     public OrderDTO findById(@RequestParam("id") final String id) { 
         OrderDTO orderDTO = new OrderDTO(); 
         orderDTO.setId(id); 
         orderDTO.setName("hello world findById"); 
         return orderDTO; 
     } 
 } 
```

example (3)： `isFull`：`true` represents that all service will be represented by the gateway.

```yaml
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    springCloud: 
      props: 
        contextPath: /springcloud 
        isFull: true 
#        port: 8884 
# registerType : service registre type, see the application client access document 
# serverList: server list, see the application client access document 
# contextPath: route prefix for your project in ShenYu gateway. 
# isFull: set true to proxy your all service and false to proxy some of your controllers 
```

```java
 @RestController 
 @RequestMapping("/order") 
 public class OrderController { 
 
     @PostMapping("/save") 
     @ShenyuSpringMvcClient(path = "/save") 
     public OrderDTO save(@RequestBody final OrderDTO orderDTO) { 
         orderDTO.setName("hello world save order"); 
         return orderDTO; 
     } 
 
     @GetMapping("/findById") 
     public OrderDTO findById(@RequestParam("id") final String id) { 
         OrderDTO orderDTO = new OrderDTO(); 
         orderDTO.setId(id); 
         orderDTO.setName("hello world findById"); 
         return orderDTO; 
     } 
 } 
```

example (4)：This is a simplified way to use it, just need a simple annotation to register to the gateway using metadata.
Special note: currently only supports `@RequestMapping, @GetMapping, @PostMapping, @DeleteMapping, @PutMapping` annotations, and only valid for the first path in `@XXXMapping`.

```java
@RestController @RequestMapping("new/feature") public class NewFeatureController {
/** * no support gateway access api.* * @return result */ @RequestMapping("/gateway/not") public EntityResult noSupportGateway() {return new EntityResult(200, "no support gateway access");}
/** * Do not use shenyu annotation path. used request mapping path.* * @return result */ @RequestMapping("/requst/mapping/path") @ShenyuSpringCloudClient public EntityResult requestMappingUrl() {return new EntityResult(200, "Do not use shenyu annotation path. used request mapping path");}
/** * Do not use shenyu annotation path. used post mapping path.* * @return result */ @PostMapping("/post/mapping/path") @ShenyuSpringCloudClient public EntityResult postMappingUrl() {return new EntityResult(200, "Do not use shenyu annotation path. used post mapping path");}
/** * Do not use shenyu annotation path. used post mapping path.* * @return result */ @GetMapping("/get/mapping/path") @ShenyuSpringCloudClient public EntityResult getMappingUrl() {return new EntityResult(200, "Do not use shenyu annotation path. used get mapping path");}}
```

- After successfully registering your service, go to the backend management system PluginList -> rpc proxy -> springCloud ', you will see the automatic registration of selectors and rules information.

- Send the request as before, only two points need to notice.
- firstly,the domain name that requested before in your service, now need to replace with gateway's domain name.
- secondly, Apache ShenYu gateway needs a route prefix which comes from `contextPath`, it configured during the integration with gateway, you can change it freely in divide plugin of `shenyu-admin`, if your familiar with it.

> For example, your have an `order` service and it has a interface, the request url: `http://localhost:8080/test/save` .
>
> Now need to change to：`http://localhost:9195/order/test/save` .
>
> We can see `localhost:9195` is the gateway's ip port, default port number is `9195` , `/order` is the `contextPath` in your config yaml file.
>
> The request of other parameters doesn't change. Then you can visit, very easy and simple.

---

<a id="user-guide-proxy-tars-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/tars-proxy/ -->

<!-- page_index: 56 -->

# Tars Proxy

Version: 2.7.0.3

This document is intended to help the `Tars` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `tars` plugin to handle `tars` service.

Before the connection, start `shenyu-admin` correctly, start `tars` plugin, and add related dependencies on the gateway and `tars` application client. Refer to the previous [Quick start with Tars](#quick-start-quick-start-tars) .

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync)).

Add the following dependencies to the gateway's `pom.xml` file:

```xml
        <!-- apache shenyu tars plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-tars</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
 
        <dependency> 
            <groupId>com.tencent.tars</groupId> 
            <artifactId>tars-client</artifactId> 
            <version>1.7.2</version> 
        </dependency> 
        <!-- apache shenyu tars plugin end--> 
```

- Restart your gateway service.

Please refer to： [shenyu-examples-tars](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-tars)

1. In the microservice built by `Tars`, add the following dependencies:

```xml
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-tars</artifactId> 
            <version>${shenyu.version}</version> 
        </dependency> 
```

2. Add the following configuration to the `application.yaml` configuration file:

```yaml
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    tars: 
      props: 
        contextPath: /tars 
        appName: tars 
        port: 21715 
        host: 192.168.41.103 
```

3. Add `@ShenyuTarsService` Annotation on the tars service interface implementation class and `@ShenyuTarsClient` on the method, start your service provider, and register successfully. In the background management system, enter PluginList -> rpc proxy -> tars, you will see the automatic registration of selectors and rules information.

Example:

```java
@TarsServant("HelloObj") @ShenyuTarsService(serviceName = "ShenyuExampleServer.ShenyuExampleApp.HelloObj") public class HelloServantImpl implements HelloServant {@Override @ShenyuTarsClient(path = "/hello", desc = "hello") public String hello(int no, String name) {return String.format("hello no=%s, name=%s, time=%s", no, name, System.currentTimeMillis());}
@Override @ShenyuTarsClient(path = "/helloInt", desc = "helloInt") public int helloInt(int no, String name) {return 1;}}
```

You can request your tars service by Http. The `Apache ShenYu` gateway needs to have a route prefix which is the `contextPath` configured by the access gateway. For example: `http://localhost:9195/tars/hello` .

---

<a id="user-guide-proxy-websocket-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/proxy/websocket-proxy/ -->

<!-- page_index: 57 -->

# Websocket Proxy

Version: 2.7.0.3

This document is intended to help the `Websocket` service access the `Apache ShenYu` gateway. The `Apache ShenYu` gateway uses the `Websocket` plugin to handle `Websocket` service.

Before the connection, start `shenyu-admin` correctly, start `Websocket` plugin, and add related dependencies on the gateway and `Websocket` application client. Refer to the previous [Quick start with Websocket](#quick-start-quick-start-websocket) .

For details about client access configuration, see [Application Client Access Config](#user-guide-property-config-register-center-access) .

For details about data synchronization configurations, see [Data Synchronization Config](#user-guide-property-config-use-data-sync)).

Add the following dependencies to the gateway's `pom.xml` file , which is introduced by default：

```xml
        <!--shenyu websocket plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-websocket</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
```

- Restart your gateway service.

> Please refer to： [shenyu-examples-websocket](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-websocket), Contains examples of the three implementations of `annotation websocket`、`spring native websocket`、`spring reactive websocket`

1. In the `Websocket` service, add the following dependencies:

```xml
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-websocket</artifactId> 
            <version>${shenyu.version}</version> 
        </dependency> 
```

2. Add the following configuration to the `application.yaml` configuration file:

```yaml
shenyu: 
  register: 
    registerType: http 
    serverLists: http://localhost:9095 # shenyu-admin ip and port 
    props: 
      username: admin 
      password: 123456 
  client: 
    websocket: 
      props: 
        contextPath: /ws-annotation 
        appName: ws-annotation 
        port: 8001 # need to be consistent with the service port 
```

3. Add `@ShenyuSpringWebSocketClient` annotation to the `Websocket` service interface implementation class, start your service and after successful registration, go to `Client List -> Proxy -> Websocket` in the `shenyu-admin` management system and you will see the auto-registered selector and rule information.

示例：

```java
@ShenyuSpringWebSocketClient("/myWs") @ServerEndpoint("/myWs") public class WsServerEndpoint {@OnOpen public void onOpen(final Session session) {LOG.info("connect successful");}
@OnClose public void onClose(final Session session) {LOG.info("connect closed");}
@OnMessage public String onMsg(final String text) {return "server send message：" + text;}}
```

You need to request your `Websocket` service via the `ws` protocol. The `Apache ShenYu` gateway will configure a routing prefix which is the `contextPath` in the access gateway configuration file. For example: `ws://localhost:9195/ws-annotation/myWs`, after which you can establish a connection to send and receive messages normally.

---

<a id="user-guide-kubernetes-controller-build-deploy"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/kubernetes-controller/build-deploy/ -->

<!-- page_index: 58 -->

# Build And Deploy Kubernetes Controller

Version: 2.7.0.3

This article introduces how to use ShenYu Ingress Controller.

It is recommended to refer to [Custom Deployment](#deployment-deployment-custom) to build a custom gateway, add the shenyu-kubernetes-controller dependency to the Maven dependency of the gateway, and the gateway can integrate the kubernetes controller.

```xml
         <dependency> 
             <groupId>org.apache.shenyu</groupId> 
             <artifactId>shenyu-spring-boot-starter-k8s</artifactId> 
             <version>${project.version}</version> 
         </dependency> 
```

You can also directly use the officially built docker image (TODO, unfinished)

K8s deployment files can refer to:

```yaml
apiVersion: v1 
kind: Namespace 
metadata: 
  name: shenyu-ingress 
--- 
apiVersion: v1 
automountServiceAccountToken: true 
kind: ServiceAccount 
metadata: 
  name: shenyu-ingress-controller 
  namespace: shenyu-ingress 
--- 
apiVersion: apps/v1 
kind: Deployment 
metadata: 
  name: shenyu-ingress-controller 
  namespace: shenyu-ingress 
  labels: 
    app: shenyu-ingress-controller 
    all: shenyu-ingress-controller 
spec: 
  replicas: 1 
  selector: 
    matchLabels: 
      app: shenyu-ingress-controller 
  template: 
    metadata: 
      labels: 
        app: shenyu-ingress-controller 
    spec: 
      containers: 
      - name: shenyu-ingress-controller 
        image: apache/shenyu-integrated-test-k8s-ingress:latest 
        ports: 
        - containerPort: 9195 
        imagePullPolicy: IfNotPresent 
      serviceAccountName: shenyu-ingress-controller 
--- 
apiVersion: v1 
kind: Service 
metadata: 
  name: shenyu-ingress-controller 
  namespace: shenyu-ingress 
spec: 
  selector: 
    app: shenyu-ingress-controller 
  type: NodePort 
  ports: 
    - port: 9195 
      targetPort: 9195 
      nodePort: 30095 
--- 
apiVersion: rbac.authorization.k8s.io/v1 
kind: ClusterRole 
metadata: 
  name: shenyu-ingress-controller 
rules: 
- apiGroups: 
  - "" 
  resources: 
  - namespaces 
  - services 
  - endpoints 
  - secrets 
  - pods 
  verbs: 
  - get 
  - list 
  - watch 
- apiGroups: 
  - networking.k8s.io 
  resources: 
  - ingresses 
  verbs: 
  - get 
  - list 
  - watch 
--- 
apiVersion: rbac.authorization.k8s.io/v1 
kind: ClusterRoleBinding 
metadata: 
  name: shenyu-ingress-controller 
  namespace: shenyu-ingress 
roleRef: 
  apiGroup: rbac.authorization.k8s.io 
  kind: ClusterRole 
  name: shenyu-ingress-controller 
subjects: 
- kind: ServiceAccount 
  name: shenyu-ingress-controller 
  namespace: shenyu-ingress 
```

Among them, Service can be changed to `LoadBalancer` type according to the actual situation.

---

<a id="user-guide-kubernetes-controller-config"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/kubernetes-controller/config/ -->

<!-- page_index: 59 -->

# Kubernetes Controller Config

Version: 2.7.0.3

This article introduces Kubernetes Controller configuration.

To enable HTTPS, you need to configure the `sni protocol` in the `application.yml` file of the gateway:

```yaml
shenyu: 
   netty: 
     http: 
       sni: 
         enabled: true 
         mod: k8s #k8s mode applies 
         defaultK8sSecretNamespace: shenyu-ingress #The namespace of the default secret resource 
         defaultK8sSecretName: default-cert #default secret resource name 
```

Among them, the default secret resource must be available, but it will not be actually used at present.

ShenYu Kubernetes Controller implements the K8s native Ingress standard, see [K8s official documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/) for the use of the native standard

In addition, Apache ShenYu has expanded based on the Annotation field of Ingress, and the configuration is shown in the following tables:

| Name | Default | Required | Description |
| --------------------------- | ------ | -------- | ----- --- |
| kubernetes.io/ingress.class | | Yes | Fill in shenyu |

| Name | Default | Required | Description |
| ------------------------------------- | ------ | ------- - | ------------------------------------------------ ------------ |
| shenyu.apache.org/loadbalancer | random | No | Load balancing algorithm, optional hash, random, roundRobin, leastActive, p2c, shortestResponse |
| shenyu.apache.org/retry | 3 | No | Number of failed retries |
| shenyu.apache.org/timeout | 3000 | No | Backend request timeout, in milliseconds |
| shenyu.apache.org/header-max-size | 10240 | No | The maximum size of the request header, unit byte |
| shenyu.apache.org/request-max-size | 102400 | No | Maximum request body size, unit byte |

| Name | Default | Required or not | Description |
| --- | --- | --- | --- |
| shenyu.apache.org/loadbalancer | random | No | Load balancing algorithm, optional hash, random, roundRobin, lastActive, p2c, shortestResponse |
| shenyu.apache.org/retry | 3 | No | Number of failed retries |
| shenyu.apache.org/timeout | 3000 | no | Backend request timeout in milliseconds |
| shenyu.apache.org/header-max-size | 10240 | No | Maximum request header size in bytes |
| shenyu.apache.org/request-max-size | 102400 | No | Maximum request body size in bytes |
| shenyu.apache.org/upstreams-protocol | dubbo:// | No | Specify the protocol protocol used by upstream |
| shenyu.apache.org/plugin-dubbo-enabled |  | No | Determines if the dubbo plugin is enabled |
| shenyu.apache.org/zookeeper-register-address |  | Yes | Specify zookeeper address |
| shenyu.apache.org/plugin-dubbo-app-name |  | Yes | Specify the metadata application name |
| shenyu.apache.org/plugin-dubbo-path |  | Yes | Specify the request path for metadata |
| shenyu.apache.org/plugin-dubbo-rpc-type |  | Yes | Specify the rpc type for metadata (dubbo, sofa, tars, springCloud, motan, grpc) |
| shenyu.apache.org/plugin-dubbo-service-name |  | Yes | Specify the interface name for the metadata |
| shenyu.apache.org/plugin-dubbo-method-name |  | Yes | Specifies the method name for metadata |
| shenyu.apache.org/plugin-dubbo-rpc-expand |  | No | Specifies the rpc expansion parameter (json object) for the metadata |
| shenyu.apache.org/plugin-dubbo-parameter-types |  | Yes | Specify parameter types for metadata |

| Name | Default | Required or not | Description |
| --- | --- | --- | --- |
| shenyu.apache.org/loadbalancer | random | No | Load balancing algorithm, optional hash, random, roundRobin, lastActive, p2c, shortestResponse |
| shenyu.apache.org/retry | 3 | No | Number of failed retries |
| shenyu.apache.org/timeout | 3000 | No | Back-end request timeout in milliseconds |
| shenyu.apache.org/header-max-size | 10240 | No | Maximum request header size in bytes |
| shenyu.apache.org/request-max-size | 102400 | No | Maximum request body size in bytes |
| shenyu.apache.org/plugin-motan-enabled | No | Yes | Determines if the motan plugin is enabled |
| shenyu.apache.org/zookeeper-register-address |  | Yes | Specify zookeeper address |
| shenyu.apache.org/plugin-motan-app-name |  | Yes | Specify the metadata application name |
| shenyu.apache.org/plugin-motan-path |  | Yes | Specify the request path for metadata |
| shenyu.apache.org/plugin-motan-rpc-type |  | Yes | Specify the rpc type for metadata (dubbo, sofa, tars, springCloud, motan, grpc) |
| shenyu.apache.org/plugin-motan-service-name |  | Yes | Specify the interface name for the metadata |
| shenyu.apache.org/plugin-motan-method-name |  | Yes | Specifies the method name for metadata |
| shenyu.apache.org/plugin-motan-rpc-expand |  | No | Specifies the rpc extension parameter (json object) for the metadata |
| shenyu.apache.org/plugin-motan-parameter-types |  | Yes | Specify parameter types for metadata |

| Name | Default | Required or not | Description |
| --- | --- | --- | --- |
| shenyu.apache.org/loadbalancer | random | No | Load balancing algorithm, optional hash, random, roundRobin, lastActive, p2c, shortestResponse |
| shenyu.apache.org/retry | 3 | No | Number of failed retries |
| shenyu.apache.org/timeout | 3000 | No | Backend request timeout in milliseconds |
| shenyu.apache.org/header-max-size | 10240 | No | Maximum request header size in bytes |
| shenyu.apache.org/request-max-size | 102400 | No | Maximum request body size in bytes |
| shenyu.apache.org/plugin-spring-cloud-enabled |  | Yes | Determines whether to start the springCloud plugin |
| shenyu.apache.org/zookeeper-register-address |  | Yes | Specify the zookeeper address |
| shenyu.apache.org/plugin-spring-cloud-app-name |  | Yes | Specify the metadata application name |
| shenyu.apache.org/plugin-spring-cloud-path |  | Yes | Specify the request path for metadata |
| shenyu.apache.org/plugin-spring-cloud-rpc-type |  | Yes | Specify the rpc type (dubbo, sofa, tars, springCloud, motan, grpc) of the metadata |
| shenyu.apache.org/plugin-spring-cloud-service-name |  | Yes | Specify the interface name for metadata |
| shenyu.apache.org/plugin-spring-cloud-method-name |  | Yes | Specifies the method name for metadata |
| shenyu.apache.org/plugin-spring-cloud-rpc-expand |  | No | Specifies the rpc extension parameter (json object) for the metadata |
| shenyu.apache.org/plugin-spring-cloud-parameter-types |  | Yes | Specify parameter types for metadata |

| Name | Default | Required or not | Description |
| --- | --- | --- | --- |
| shenyu.apache.org/loadbalancer | random | No | Load balancing algorithm, optional hash, random, roundRobin, lastActive, p2c, shortestResponse |
| shenyu.apache.org/retry | 3 | No | Number of failed retries |
| shenyu.apache.org/timeout | 3000 | No | Back-end request timeout in milliseconds |
| shenyu.apache.org/header-max-size | 10240 | No | Maximum request header size in bytes |
| shenyu.apache.org/request-max-size | 102400 | No | Maximum size of request body in byte |

---

<a id="user-guide-api-doc-shenyu-annotation-apidoc"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/api-doc/shenyu-annotation-apidoc/ -->

<!-- page_index: 60 -->

# The client registers the API documentation

Version: 2.7.0.3

This article describes how to expose the `API documentation` to the `Apache ShenYu` gateway.

Before accessing, please start `shenyu-admin` correctly.

You can refer to any of the example codes below [shenyu-examples](https://github.com/apache/shenyu/tree/master/shenyu-examples).

The only thing you need to do is to add `@ApiModule` and `@ApiDoc` annotations to your service, here is an example from `shenyu-examples-http`:

```java
@RestController 
@RequestMapping("/order") 
@ShenyuSpringMvcClient("/order") 
@ApiModule(value = "order") 
public class OrderController { 
 
    @GetMapping("/findById") 
    @ShenyuSpringMvcClient("/findById") 
    @ApiDoc(desc = "findById") 
    public OrderDTO findById(@RequestParam("id") final String id) { 
        return build(id, "hello world findById"); 
    } 
 
    private OrderDTO build(final String id, final String name) { 
        OrderDTO orderDTO = new OrderDTO(); 
        orderDTO.setId(id); 
        orderDTO.setName(name); 
        return orderDTO; 
    } 
} 
```

---

<a id="user-guide-api-doc-swagger-apidoc"></a>

<!-- source_url: https://shenyu.apache.org/docs/user-guide/api-doc/swagger-apidoc/ -->

<!-- page_index: 61 -->

# Pull the swagger registration API document

Version: 2.7.0.3

This article introduces how to aggregate the `Swagger API documentation` of each backend microservice to the `Apache ShenYu` gateway management system.

Remotely pull swagger documents, currently only supports swagger2.0, and only supports Divide and SpringCloud proxy plug-ins.

Please refer to the `deployment` document, choose a way to run `shenyu-admin`.

It is enabled by default. In the `Apache ShenYu` gateway management system --> BasicConfig --> Dictionary, find the data whose DictionaryType is `apidoc`, and modify the dictionary value: `true`.

> 【Notice】DictionaryValue: `true` means the switch is on, `false` means it is off. If it is closed, `shenyu-admin` will not automatically pull the swagger documents of each microservice.

![apidoc-dictionary-en](assets/images/apidoc-dictionary-en-c62f7e2be1763f8bee65a1245556327b_91c0244b1cc61d99.png)

3.1. Download [shenyu-examples-http-swagger2](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http-swagger2)

3.2. Run `org.apache.shenyu.examples.http.ShenyuTestSwaggerApplication` main method to start the project.

The examples project will synchronize the service startup information to `shenyu-admin` through the Shenyu client annotation (such as `@ShenyuSpringMvcClient`) according to the address configured by `shenyu.register.serverLists`, and then trigger `shenyu-admin` to remotely pull the swagger document And complete the analysis, and finally aggregate to produce a new API document.

In `Apache ShenYu` Gateway Management System --> Document --> API Document, you can see the aggregated API documents.

![apidoc-swagger-list-en](assets/images/apidoc-swagger-list-en-1eb2c525a7c0e2ab6a955d91b42982c3_07cd3b966144c1ba.png)

![apidoc-detail-en](assets/images/apidoc-detail-en-828985abbfa6d2b36b87f819ed3f39ae_e617ad8e7c8e9b1f.png)

As in the example above, an automatic update of the API docs is triggered by starting the project.

In the PlugiList --> Proxy --> selector, find the target service, and then modify the startup time.

> Note: The startup time of the new setting must not be earlier than the original startup time, otherwise the API document will not be automatically pulled and refreshed.

![app-proxy-startuptime-en](assets/images/app-proxy-startuptime-en-1696ab1f3f4b39a079d04e9cafb45bf2_85ed4c5145a0e5cb.png)

---

<a id="plugin-center-http-process-contextpath-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/http-process/contextpath-plugin/ -->

<!-- page_index: 62 -->

# 1. Overview

Version: 2.7.0.3

- ContextPath Plugin

- Different services can do traffic governance of services by setting different context paths.

- Set the context path for service.
- When the interface is called, the plug-in uniformly prefixes the interface address of the service.

- Core module `shenyu-plugin-context-path`
- Core class `org.apache.shenyu.plugin.context.path.ContextPathPlugin`

- 2.3.0

<a id="plugin-center-http-process-contextpath-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/procedure-en-1e938b19eab6ff11bd956e3e9641bc52_586b9319e212be2b.png)

- import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-gateway</artifactId> 
     <version>${project.version}</version> 
  </dependency> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `contextPath` set Status enable.

![](assets/images/enable-en-93474e3fbe53b33a7870f7cc5a2990e6_75d3f43be1f4e111.png)

- Set client project's contextPath.

![](assets/images/client-project-config-1b8ee987a5aaf08a17499f11a013f548_3c820d01ee8205ae.png)

- Selector and rule config, please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).
- shenyu-admin contextPath plugin config, config contextPath and addPrefix, contextPath defines the value of contextPath,
- and addPrefix defines the prefix that needs to be automatically added when the interface is called.

![](assets/images/plugin-config-en-eb907beb602715d69ffe2df9e66b66ce_f4261b53e9322beb.png)

Client project can directly use [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http), and config contextPath in application.yml.

![](assets/images/client-project-config-1b8ee987a5aaf08a17499f11a013f548_3c820d01ee8205ae.png)

- After the configuration is completed, and start client project, you can see that there is an additional context selector and rule configuration in shenyu-admin.

![](assets/images/context-path-selector-and-rule-en-73179545dae6c534b9dd2639949e1a57_5aebcbd172ae040e.png)

![](assets/images/invoke-interface-cde95ab27ebf6f7608fcfe075e5245f7_8b23afd71da1cbd5.png)

For client project we can directly use [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http), and config contextPath in application.yml.

![](assets/images/client-project-config-1b8ee987a5aaf08a17499f11a013f548_3c820d01ee8205ae.png)

- After the configuration is completed, start client project, you can see that there is an additional context selector and rule configuration in shenyu-admin.

![](assets/images/context-path-selector-and-rule-en-73179545dae6c534b9dd2639949e1a57_5aebcbd172ae040e.png)

![](assets/images/add-prefix-en-a804086aec06625788372c6a3933ff32_78309f43beb3209f.png)

Since this example uses the service of the http protocol, we need to modify the divide plugin.

![](assets/images/remove-add-prefix-en-9c8f7b7d266761d4ceb0f3ca720a5928_24a917c253b236d4.png)

![](assets/images/invoke-interface-add-prefix-51c6dfad10bf466ae61d0bfc507a7443_186ff494f9458907.png)

For client project we can directly use [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http) and [shenyu-examples-https](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-https).

- After the client projects started, you can see that there are two additional context selectors and rules configuration in shenyu-admin.

![](assets/images/context-path-selectors-9f0e881bd1af70c10089bbcbbc5665cb_1d2d8c392fd24c29.jpg)

![](assets/images/rewrite-context-path-303dcab09c0e37b2a1cb8007dc4bcda7_d72611c65ca0829b.jpg)

Note: the percentage can adjust the rewriting ratio from 0 to 100, with a default of 100, indicating complete rewriting.

![](assets/images/invoke-interface-rewrite-context-path-2e805aabd6653039e16345f93e1d54a6_dcdc89e27c84b56d.jpg)

<a id="plugin-center-http-process-contextpath-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `contextPath` set Status disable.

![](assets/images/disable-en-e92e23f9495300ceabd7f3937970e5db_e9cdc757dca8e3af.png)

---

<a id="plugin-center-http-process-modifyresponse-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/http-process/modifyresponse-plugin/ -->

<!-- page_index: 63 -->

# 1. Overview

Version: 2.7.0.3

- ModifyResponse Plugin

- This plugin is used for modifying HTTP response status code, response headers or response body parameters.

- Reset HTTP response status code
- Add, set, replace or remove HTTP response headers.
- Add, replace or remove HTTP response body(JSON) parameters.

- Core module `shenyu-plugin-modify-response`
- Core class `org.apache.shenyu.plugin.modify.response.ModifyResponsePlugin`

- 2.4.0

<a id="plugin-center-http-process-modifyresponse-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/procedure-en-7fc93c4eb1c76a7cf253a0a6d2c072c7_9afab81216c74997.png)

- import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-gateway</artifactId> 
     <version>${project.version}</version> 
  </dependency> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `modifyResponse` set Status enable.

![](assets/images/enable-en-ac2aa2d0b684f329ba5eefaadf61b30c_2a688411ba2b6ecc.png)

- Selector and rule config, please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).
- In `shenyu-admin` --> `PluginList` --> `HttpProcess` --> `modifyResponse`, add selector config first，then add rule config：
  - Add selector config
    ![](assets/images/plugin-selector-config-en-c9eba64e9bd6d1d7daca6c974280c079_d4a4282f254272a9.png)
  - Add rule config
    ![](assets/images/plugin-rule-config-en-92ed9341ca270670294f41ffdfe520c3_0ac7365aecfb778c.png)

Here is an example of client project [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http).

Add plugin config:

![](assets/images/status-code-rule-config-en-3cb49cba49823843b9076ecfafcdb358_b62df1732fff241c.png)

![](assets/images/status-code-invoke-interface-688a23664d58e142832432e3e8abc449_facc359bc5bae3e9.png)

Add plugin config:

![](assets/images/header-rule-config-en-6531c7d9c41f5e744c0cf88ce38cb071_a2494d3dbf85be6b.png)

![](assets/images/header-invoke-interface-1ec5514412331e6438e4b1f5b2796d6e_a9d0db4456cddada.png)

Add plugin config:

![](assets/images/body-rule-config-en-fa57f66c274d0ab89fce27bd95317b6e_a6f55c7bd87e2024.png)

![](assets/images/body-invoke-interface-d5fd9ba3d67c539595c1e69f8ddd6716_9f88e6150ae0ccb9.png)

- In `shenyu-admin` --> BasicConfig --> Plugin --> `modifyResponse` set Status disable.

![](assets/images/disable-en-eac55ef5d1fa2120726b27881db51082_bae30da5c8164e2a.png)

for modifying status code:

- `statusCode`: reset response status code

for modifying response headers:

- `addHeaders`: add response headers, `k-v` format
- `setHeaders`: set response headers, `k-v` format
- `replaceHeaderKeys`: replace response headers，`key` is matching to the header key that should be replacing, value is target value after replacing
- `removeHeaderKeys`: remove response headers，`key` is matching to the header key that should be removing

for modifying response body:

- `addBodyKeys`: add response body parameters
- `replaceBodyKeys`: replace response body parameters，`key` is matching to the body(JSON) key that should be replacing, value is target value after replacing
- `removeBodyKeys`: remove response body parameters，`key` is matching to the body(JSON) key that should be removing

---

<a id="plugin-center-http-process-parammapping-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/http-process/parammapping-plugin/ -->

<!-- page_index: 64 -->

# 1. Overview

Version: 2.7.0.3

- ParamMapping Plugin

- Add/remove/replace certain fixed parameters to the request

- `paramMapping` is used to edit your request parameters.

- Core Module `shenyu-plugin-param-mapping`
- Core Class `org.apache.shenyu.plugin.param.mapping.ParamMappingPlugin`

- Since ShenYu 2.4.0

<a id="plugin-center-http-process-parammapping-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Introduce `paramMapping` dependency in the pom.xml file of the gateway.

```xml
<!-- apache shenyu param_mapping plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-param-mapping</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu param_mapping plugin end--> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `paramMapping` set Status enabled.

- you should open this plugin when using.

- Selectors and rules, please refer to:[Selector And Rule Config](#user-guide-admin-usage-selector-and-rule)。
- Only those matched requests can be modified your request body.

![](assets/images/param-mapping-48f0bc50c54e2044a1904fe4870ba9b5_9e98c77e21892ef6.png)

- param details:

  - `addParameterKeys`: add a new `key-value` on body
  - `replaceParameterKeys`: replace request body's `key` ，`key` is the value to be replaced，`value` is the value after replacement
  - `removeParameterKeys`: remove a body `key`
- param\_mapping modify the request body is achieved through `JSONPath` , `$.` represents the root directory.

- you should open the plugin when using.

![](assets/images/param-mapping-48f0bc50c54e2044a1904fe4870ba9b5_9e98c77e21892ef6.png)

use the configuration，unopened the plugin，request body is:

```json
{"id":3,"data":{"value":"18","age":"36"}} 
```

open the plugin，the final request body is

```json
{"name":"shenyu","userId":3,"data":{"age":"36"}} 
```

add a new key-value `name:shenyu`,replace the key `id` to `userId`, remove the key `data.value` .

<a id="plugin-center-http-process-parammapping-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `paramMapping` set Status disable.

---

<a id="plugin-center-http-process-redirect-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/http-process/redirect-plugin/ -->

<!-- page_index: 65 -->

# 1. Overview

Version: 2.7.0.3

- Redirect Plugin

- As the name suggests, the `redirect` plugin is to re-forward and redirect `uri`.

- When the Apache ShenYu gateway makes proxy calls to the target service, it also allows users to use the `redirect` plugin to redirect requests.

Core module `shenyu-plugin-context-redirect`
Core class `org.apache.shenyu.plugin.redirect.RedirectPlugin`

before 2.2.0 .

<a id="plugin-center-http-process-redirect-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/redirect-procedure-en_2ccae93543335049.png)

- import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
<!-- apache shenyu redirect plugin start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-redirect</artifactId> 
   <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu redirect plugin end--> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `Redirect` set Status enable.

  ![](assets/images/redirect-plugin-enable-en_23fc9cdbf3d4c794.png)

- Selector and rule config, please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).
- In `shenyu-admin` --> `PluginList` --> `HttpProcess` --> `Redirect`, add selector config first，then add rule config：
  - Add selector config

    ![](assets/images/redirect-plugin-forward-rule-en_ad4aee392f55ac65.png)
  - Add rule config

    ![](assets/images/redirect-plugin-rule-en_0057ed578a3a6a6e.png)

- When we configure a custom path in `Rule`, it should be a reachable service path.
- When the request is matched, the `ShenYu Gateway` will perform the `308` service jump according to the customized path.

1. Refer [Local Deployment](#deployment-deployment-local) to start admin and bootstrap.
2. Refer 2.2 to import pom and restart bootstrap.
3. Refer 2.3 to enable plugin.
4. Refer 2.4 and [Selector and rule config](#user-guide-admin-usage-selector-and-rule).
5. Invoke interface: [demo](http://localhost:9195/http)

- Invoke the interface declared by selectors and rules will redirect to the specified path.
- In this demo, it will jump to [ShenYu official website](https://shenyu.apache.org/)

  ![](assets/images/redirect_f8485dda6abd5635.png)

- When the matching rules are met, the service will use the `DispatcherHandler` internal interface for forwarding.
- To implement the gateway's own interface forwarding, we need to use `/` as the prefix in the configuration path. The specific configuration is as shown in the figure below.

  ![](assets/images/demo2-en_342f4c48b2218897.png)

<a id="plugin-center-http-process-redirect-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `Redirect` set Status disable.

  ![](assets/images/disable-redirect-plugin-zh_f7a3f8fe678c3e21.png)

---

<a id="plugin-center-http-process-request-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/http-process/request-plugin/ -->

<!-- page_index: 66 -->

# 1. Overview

Version: 2.7.0.3

- Request Plugin

- The request plugin is able to make customized changes to the request parameters of `uri`.

- The `Apache ShenYu` gateway allows users to use the `request` plugin to add, modify, and remove request headers to request parameters, request headers, and `Cookie` when proxying a target service.

- Core Module `shenyu-plugin-request`
- Core Class `org.apache.shenyu.plugin.request.RequestPlugin`

- Since ShenYu 2.4.0

<a id="plugin-center-http-process-request-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/request-plugin-procedure-en_61d661e4c1ac568f.png)

- Import maven config in shenyu-bootstrap project's `pom.xml` file, which is already added by default.

```xml
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-plugin-request</artifactId> 
      <version>${project.version}</version> 
  </dependency> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `request` set Status enabled.

  > If there is an option to configure a `ruleHandlePageType` on the page here, you can configure any string, e.g. `custom`, which has no effect on the request, and will be removed in later versions.

  ![](assets/images/request-plugin-enable-en_27c6e76b54745811.png)

- selectors and rules, only requests that match are forwarded and redirected, see the [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule)
- `shenyu-admin` Plugin --> `HttpProcess` --> `Request`. Add the selector first, then add the rule：
- Add the selector:

  ![](assets/images/request-plugin-selector-en_76bf9e954a4e4357.png)
- Add the rule

  ![](assets/images/request-plugin-rule-en_75f6052f7f0537d4.png)

- When we configure a custom path in `Rules`, it should be a reachable service path.
- When a request is matched, based on the customized path, the `Apache ShenYu` gateway performs a service hop.

1. Refer to [Local Deployment](#deployment-deployment-local)启动 admin 和网关
2. Refer to 2.2 importing pom and restarting the gateway.
3. Refer to 2.3 enabling Plugin
4. Start the project [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http)
5. Refer to 2.4 and [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule), configuring plugin rules.
6. Call interface：[http-test-api.http](https://github.com/apache/shenyu/blob/master/shenyu-examples/shenyu-examples-http/src/main/http/http-test-api.http)

- Calling the interface declared by the selector and rule will see the request parameters configured in the request plugin.

  ![](assets/images/request-plugin-example-zh_2eeb389d6755f898.png)

<a id="plugin-center-http-process-request-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `request` set Status disable.
- ![](assets/images/request-plugin-disable-en_58c1fcc9c47a9522.png)

---

<a id="plugin-center-http-process-rewrite-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/http-process/rewrite-plugin/ -->

<!-- page_index: 67 -->

# 1. Overview

Version: 2.7.0.3

- Rewrite Plugin

- The request uri can be different from the target service by rewriting the path.

- This plugin is used to rewrite the request uri.

- Core Module `shenyu-plugin-rewrite`
- Core Class `org.apache.shenyu.plugin.rewrite.RewritePlugin`

- Since ShenYu 2.4.0

<a id="plugin-center-http-process-rewrite-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/rewrite-use-en-805b67cd07b5e0c64168d13424be9f8c_43460ffd28f92fc7.png)

- Import maven config in shenyu-bootstrap project's `pom.xml` file..

```xml
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-plugin-rewrite</artifactId> 
      <version>${project.version}</version> 
  </dependency> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `rewrite` set Status enabled.
  ![](assets/images/rewrite-open-en-6f19bcb0b1115b24a6bf49b382938253_15f640ecce68360a.png)

- Enable the plugin before using.
- Disable the plugin if don't use.

- Please refer to: [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule).

![](assets/images/rewrite-rule-config-d5e17a2648c2d6a0e0def60767164ae5_1c73bea659546004.png)

- Param details:
  - `regex`: The regular expression that matches the part of uri to be rewrited.
  - `replace`: The content of replacement.
  - `percentage` : The percentage of rewriting, 100 represents 100%.
  - `rewriteMetaData`: Whether to rewrite metadata, true indicates that it is enabled, and once enabled, the uri can be rewritten across plugins.

- Use [shenyu-examples-http](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-http), please refer to [Run the shenyu-examples-http project](#quick-start-quick-start-http--run-the-shenyu-examples-http-project)

- Refer to [2.4.1](#plugin-center-http-process-rewrite-plugin--241-plugin-config) to configure plugin.

- Refer to [2.4.2](#plugin-center-http-process-rewrite-plugin--242-selector-config) to configure selector

![](assets/images/rewrite-example-rule-5ad55fb5d2a785738487d663b9c49977_e16c00aead1a83f0.png)

The request `/http/hello` would be rewritten to `/hi`

Use some tool (such as Postman) to make a request:

![](assets/images/rewrite-example-result-1f6860e296fc5418aa97ad425dca82b3_1f1febe20c05fdf6.png)

<a id="plugin-center-http-process-rewrite-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `rewrite` set Status disable.

---

<a id="plugin-center-proxy-divide-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/divide-plugin/ -->

<!-- page_index: 68 -->

# 1. Overview

Version: 2.7.0.3

- `divide` Plugin

- Handling `http protocol` requests.
- Support traffic management, such as a/b test, grayscale test.
- Service Load Balancing.
- Set request timeout.

- Supports traffic management based on request information such as uri, header, and query.
- Supports setting the load balancing strategy for requests, and supports service warm-up. Currently, three strategies are supported: ip hash (consistent hash with virtual nodes), round-robbin (weighted polling), random (weighted random).
- Supports setting the maximum value of the request header, the maximum value of the request body, and the request level timeout.
- Supports setting the timeout retry policy and the number of retries. Currently, the retry policy supports: current (retrying the server that failed before) and failover (retrying other servers).

- Core module is `shenyu-plugin-divide`.
- Core class is `org.apache.shenyu.plugin.divide.DividePlugin`.

<a id="plugin-center-proxy-divide-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/procedure-en-5b17e369f9d6c12d70118a29f5b7bd30_b9738abfbc29bfda.png)

- Import maven in shenyu-bootstrap project's `pom.xml` file.

```xml
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-gateway</artifactId> 
     <version>${project.version}</version> 
  </dependency> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `divide` set Status enable.

![](assets/images/enable-en-d6ddedc0d79f6f071df86d262a7cda03_937dfeced327adda.png)

- Client access method and server address. The following example uses the http access method. Currently, the client supports the following access methods: http, zookeeper, etcd, nacos, consul. For detailed access configuration parameters, please refer to [Client Access Configuration](https://shenyu.apache.org/docs/next/user-guide/property-config/register-center-access).
- Client configuration, including the protocol name and the routing address of the service, please use the http protocol here, and the value of contextPath must be configured as the routing address of each service.

```yaml
  shenyu: 
    register: 
      registerType: http 
      serverLists: http://localhost:9095 
      props: 
        username: admin 
        password: 123456 
    client: 
      http: # http protocol 
        props: 
          contextPath: /http # routing address for each service 
```

The following example uses the http access method. Currently, the client supports the following access methods: http, zookeeper, etcd, nacos, consul. For detailed access configuration parameters, please refer to [Client Access Configuration](https://shenyu.apache.org/docs/next/user-guide/property-config/register-center-access).

> Only http-type registries support upstream detection.

```yaml
  shenyu: 
    register: 
      registerType: http # Only http-type register center support upstream detection. 
      serverLists:  
      props: 
        checked: true # The default is true, set to false, do not detect. 
        zombieCheckTimes: 5 # The maximum number of zombie upstream detections. If it exceeds 5 times, its validity will no longer be detected. The default value is 5. 
        scheduledTime: 10 # Timing detection interval, the default is 10 seconds. 
        zombieRemovalTimes: 60 # How many seconds the upstream is offline to be considered as a zombie upstream, the default is 60 seconds. 
```

After the client is started, the [selector and rule](#user-guide-admin-usage-selector-and-rule) information will be automatically registered in shenyu-admin -> Plugin List -> Proxy -> Divide.

![](assets/images/select-and-rule-en-3a62f8cb06cf350e1f7e48daaa601978_d5c88bf95139f36f.png)

Example of divide selector. For general selector configuration, please refer to [Selectors and Rules](#user-guide-admin-usage-selector-and-rule).

![](assets/images/selector-en-0b99d7a7e1ce0334e5dadc04ba8611c8_51971bac53101f53.png)

- `host`: fill in `localhost`, this field is not used currently.
- `ip:port`: `ip` and port, fill in the `ip` + port of your real service here.
- `protocol`: `http` protocol, fill in `http:` or `https:`, if not fill in, the default is: `http:`.
- `startupTime`: Startup time in milliseconds.
- `weight`: load balancing weight, the default value of service startup automatic registration is 50.
- `warmupTime`: Warmup time, in milliseconds. The server during warmup will calculate the instantaneous weight, and the calculated value will be smaller than the actual configured weight to protect the server just started. The default value of service startup registration is 10. For example, the warm-up time is 100 milliseconds, the current startup is 50 milliseconds, the configured weight is 50, and the actual weight is 25.
- `status`: On or off, this selector is valid only in the on state.

Example of divide rule. For general rule configuration, please refer to [selectors and rules](#user-guide-admin-usage-selector-and-rule).

![](assets/images/rule-en-0b219597a708404400981a3a9d6a89c0_f7cb36e9d1a0da30.png)

- `loadStrategy`: If the `http` client is a cluster, which load balancing strategy is used when the `Apache ShenYu` gateway is called, currently supports `roundRobin`, `random` and `hash`.
- `timeout`: The timeout for calling the `http` client.
- `retry Count`: The number of retries that failed to call the `http` client timeout.
- `headerMaxSize`: The maximum value of the requested `header`.
- `requestMaxSize`: The maximum value of the request body.
- `retryStrategy`: Supported since `2.4.3`, retry strategy after failure, default `current` to maintain compatibility with lower versions. For example, there are 3 downstream services `http:localhost:1111`, `http:localhost:1112` and `http:localhost:1113`, assuming the first load balancing to `http:localhost:1111` and `call failed`. Using the `current` strategy will continue to retry calling `http:localhost:1111`; using the `failover` strategy will retry calling other services such as `http:localhost:1112` through the `load balancing`, if it fails again at this time , call to `http:localhost:1113` until no service is available.

To be added, welcome contribute.

To be added, welcome contribute.

<a id="plugin-center-proxy-divide-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `divide` set Status disable.

![](assets/images/disable-en-8ae0fcbf271bbccd293931cc20f3dfa1_3c3a35edf21d46f9.png)

---

<a id="plugin-center-proxy-dubbo-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/dubbo-plugin/ -->

<!-- page_index: 69 -->

# Dubbo Plugin

Version: 2.7.0.3

- Dubbo is a plugin that converts `http protocol` into `Dubbo protocol` and it is also the key for gateway to realize dubbo generic service.
- Dubbo plugin needs to cooperate with metadata to realize dubbo calls.
- Apache Dubbo and Alibaba Dubbo users both use the same plugin.

- Add related dependencies and enable plugin, please refer to: [Quick start with Dubbo](#quick-start-quick-start-dubbo) .
- `Dubbo` client access, please refer to: [Dubbo Proxy](#user-guide-proxy-dubbo-proxy) .
- Set selector and rule, please refer to: [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) .
- Since `version 2.4.3`, the new fields and meanings of the dubbo plugin:

![](assets/images/dubbo-plugin_477d0df7a32d5f59.png)

- `corethreads`：The number of core threads in the business thread pool。
- `queues`：The length of the blocking queue of the business thread pool, 0 means `unbounded blocking queue`。
- `threadpool`：There are five types of business thread pools: `fixed`, `eager`, `cached`, `limited` and `shared`. The first 4 types correspond to the thread pools officially provided by dubbo. Let's talk about `shared`, as its name implies, `all proxy plugins` share a `shared` thread pool, the advantage of this is that it can reduce the number of thread pools, thereby reducing memory and improving resource utilization。
- `threads`：The maximum number of threads in the business thread pool。

After the client accesses the `ShenYu` gateway, it will automatically register the selector and rule information. For details about the selector and rule configuration, see [Selector and Rule Config](#user-guide-admin-usage-selector-and-rule) .

![](assets/images/selector-en-new_a96e67e2322aeb2e.png)

Selector Handler, the `handle` field, is an operation that can be processed by the gateway after matching the traffic. For more information, please refer to [Plugin handle management](#user-guide-admin-usage-plugin-handle-explanation) in Plugin Config.

- details：

  - `host`：host string.
  - `ip:port`：ip+port string.
  - `protocol`：protocol default is 'http'.
  - `group`：the group of dubbo service.
  - `version`：the version of dubbo service.
  - `weight`：the server instance and participate in load balancing calculation.
  - `warmupTime`：the server's warm up time and and participate in load balancing calculation.
  - `startupTime`：the server's start time.
  - `status`：true: the server is available，false: the server is unavailable.
  - `gray`：enable gray routing.

Gray routing

if you want to user gray route in dubbo-plugin, you can click the `gray` button.

- Gray level publishing can customize and control the traffic proportion of new version applications when publishing new version applications, gradually complete the full launch of new version applications, maximize the business risk caused by new version publishing, reduce the impact surface caused by faults, and support rapid roll back.

when the gray is open,Gateway load balancing will select one node from the current node list for routing and you can modify node weights to change the weight of nodes in the load balancing algorithm.
It should be noted that,if your business instance not use the client jar of 'shenyu-client-apache-dubbo' or 'shenyu-client-alibaba-dubbo', You should add gray node information manually on this selector page.

![](assets/images/rule-en_653fab09253fb7f3.png)

Rule Handler, the `handle` field, can be performed by the gateway after the final matching of traffic. For more information, please refer to [Plugin handle management](#user-guide-admin-usage-plugin-handle-explanation) in Plugin Config.

- details：

  - `loadbalance`：the loadbalance of dubbo service, if the gray node selection fails, the default load balancing method will be used.
- Apache ShenYu will obtain the real IP of the corresponding service and initiate rpc proxy calls from registration center of dubbo.

- Every dubbo interface method corresponds to a piece of metadata, which can be found in `shenyu-admin` --> BasicConfig -> Metadata .

![](assets/images/dubbo-metadata-en_36306ab603189989.jpg)

- AppName: The name of the application to which this piece of metadata belongs.
- MethodName: The name of the method that needs to be called.
- Path: your http request path.
- PathDescribe: Description of the path, for easy viewing.
- ParamsType: List of parameter types of dubbo interface, there are two declaration methods here:
  e.g. we have an interface `update(Integer id, String name, Integer age)`

  - Type list


```yaml
java.lang.Integer,java.lang.String,java.lang.Integer 
```

    - According to the order of the parameter types of the interface, separated by `,`
    - When requesting to pass parameters, **the parameters must be passed in strictly in accordance with the order of the parameter types**, if a parameter without value use `null` as a placeholder.

      Request body example: `{"id":1,"name": null,"age":18}`
  - Name mapping


```yaml
{"id":"java.lang.Integer","name":"java.lang.String","age":"java.lang.Integer"}       
```

    - Use `"parameter name":"parameter type"` to represent a parameter, set in order of interface parameter type, separated by `,`
    - No need to pay attention to the order when requesting, and no need to use null placeholders.

      Request body example: `{"name":"Mike","id":1}`
- RpcExpand: corresponding to some configurations of dubbo interface; If you want to adjust, please modify here, which support json format like the following fields:

```yaml
{"timeout":10000,"group":"",version":"","loadbalance":"","retries":1} 
```

- Interface: The fully-qualified name for dubbo interface .
- RpcType: Choose `dubbo` .

---

<a id="plugin-center-proxy-grpc-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/grpc-plugin/ -->

<!-- page_index: 70 -->

# gRPC Plugin

Version: 2.7.0.3

- The grpc plugin is a plugin that converts the Http protocol into the grpc protocol.

- Add related dependencies and enable plugin, please refer to: [Quick start with gRPC](#quick-start-quick-start-grpc) .
- `gRPC` client access, please refer to: [gRPC Proxy](#user-guide-proxy-grpc-proxy) .
- New fields and meanings of grpc plugin since `2.4.3`:

  - `threadpool`：There are two types of business thread pools, `cached` and `shared`.

    `cached` is equivalent to the default thread pool officially provided by grpc;

    `shared` thread pool, just as its name, `all proxy plugins` share a `shared` `Thread pool, the advantage of doing this is that it can reduce the number of thread pools, thereby reducing memory and improving resource utilization.

After the client accesses the `Apache ShenYu` gateway, it will automatically register the selector and rule information. You can see it in PluginList -> rpc proxy -> grpc. For details about the selector and rule configuration, see [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) .

![](assets/images/selector-en_09d170e75d3d4c50.png)

Selector Handler, the `handle` field, is the processing operation that the gateway can perform after matching the traffic.

- config details：

  - `ip:port`：enter the ip:port of your real service .
  - `protocol`：indicates the Http protocol. Generally, the value is `http://` or `https://`. If the value is not specified, the default value is `http://` .
  - `weight`：service weight.
  - `status`：open or close.

Each `grpc` interface method, will correspond to a metadata, when the `grpc` application client access to the `Apache ShenYu` gateway, will be automatically registered, can be viewed in the `shenyu-admin` background management system of the BasicConfig --> Metadata management.

![](assets/images/metadata-en_0ce632d0f7845dd6.png)

- AppName: specifies the name of the application to which the metadata belongs.
- MethodName: the name of the method to call.
- Path: http request path.
- PathDescribe: the description of the path is easy to view.
- ParamsType: the parameters are separated by commas (,) in the order of interface parameter types.
- RpcExpand: other configurations of the `grpc` interface, which support the `JSON` format, are as follows:

```json
{ 
  "timeout": 5000, 
  "methodType": "SERVER_STREAMING" 
} 
```

- Interface: The fully qualified class name of the `grpc` interface.
- RpcType：choose `grpc`.

---

<a id="plugin-center-proxy-motan-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/motan-plugin/ -->

<!-- page_index: 71 -->

# Motan Plugin

Version: 2.7.0.3

- The motan plugin is a plugin that converts the Http protocol into the motan protocol.

- Add related dependencies and enable plugin, please refer to: [Quick start with Motan](#quick-start-quick-start-motan) .
- `Motan` client access, please refer to: [Motan Proxy](#user-guide-proxy-motan-proxy) .

After the client accesses the `Apache ShenYu` gateway, it will automatically register the selector and rule information.

You can see it in PluginList -> rpc proxy -> motan. For details about the selector and rule configuration, see [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) .

Each `motan` interface method, will correspond to a metadata, when the `motan` application client access to the `Apache ShenYu` gateway, will be automatically registered, can be viewed in the `shenyu-admin` background management system of the BasicConfig --> Metadata management.

![](assets/images/metadata-en_bf4e8ed2e443933a.png)

- AppName: specifies the name of the application to which the metadata belongs.
- MethodName: the name of the method to call.
- Path: http request path.
- PathDescribe: the description of the path is easy to view.
- ParamsType: the parameters are separated by commas (,) in the order of interface parameter types.
- RpcExpand: description of each interface in a `motan` service. For example, here is the interface information for the `motan` service:

```json
{"methodInfo": [{"methodName": "hello","params": [{"left": "java.lang.String","right": "name"}]} ],"group": "motan-shenyu-rpc"}
```

- Interface: The fully qualified class name of the `motan` interface.
- RpcType：choose `motan`.

---

<a id="plugin-center-proxy-mqtt-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/mqtt-plugin/ -->

<!-- page_index: 72 -->

# Mqtt Plugin

Version: 2.7.0.3

- After the plugin is used, it will give the ability of mqtt.

- Introducing those dependencies in the pom.xml file of the gateway.

```xml
<!-- apache shenyu mqtt plugin start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-mqtt</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- port: MQTT BS port designation.
- bossGroupThreadCount: default 1.
- maxPayloadSize: Maximum packet size.
- workerGroupThreadCount: default 12.
- username: default shenyu.
- password: default shenyu.
- isEncryptPassword: The default is false , whether to encrypt the password.
- encryptMode: encryption mode, currently only MD5 is implemented, the encryption mode can be customized, `org.apache.shenyu.protocol.mqtt.utils.EncryptUtil` view the implementation of this encryption class.
- leakDetectorLevel: default DISABLED, resource target detection or detection level.

- Mqtt does not have selector and ruler configurations.

---

<a id="plugin-center-proxy-sofa-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/sofa-plugin/ -->

<!-- page_index: 73 -->

# 1. Overview

Version: 2.7.0.3

- Sofa plugin

- Protocol conversion, a plugin that converts http protocol requests into the sofa framework protocol
- Service Load Balancing.

- Converting http protocol requests to sofa framework protocol.

- Core Module `shenyu-plugin-sofa`
- Core Class `org.apache.shenyu.plugin.sofa.SofaPlugin`

- 2.3.0

<a id="plugin-center-proxy-sofa-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![image-20220828222022336](assets/images/procedure-chart-en-5d71f183478498a526b766c4a72db530_78b2ee2fde6b3d40.png)

```xml
        <dependency> 
            <groupId>com.alipay.sofa</groupId> 
            <artifactId>rpc-sofa-boot-starter</artifactId> 
            <version>${rpc-sofa-boot-starter.version}</version> 
        </dependency> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-sofa</artifactId> 
            <version>${project.version}</version> 
            <exclusions> 
                <exclusion> 
                    <artifactId>guava</artifactId> 
                    <groupId>com.google.guava</groupId> 
                </exclusion> 
            </exclusions> 
        </dependency> 
```

1. Configure the sofa configuration in application.yml.

```yaml
com: 
  alipay: 
    sofa: 
      rpc: 
        registry-address: zookeeper://127.0.0.1:2181 # consul # nacos 
        bolt-port: 8888 
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    sofa: 
      props: 
        contextPath: /sofa 
        ipAndPort: sofa 
        appName: sofa 
        port: 8888 
```

2. Configure the service interface exposed by the sofa service in the xml file in the resources directory.

```xml
<beans xmlns="http://www.springframework.org/schema/beans" 
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
       xmlns:sofa="http://sofastack.io/schema/sofaboot" 
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd 
            http://sofastack.io/schema/sofaboot https://sofastack.io/schema/sofaboot.xsd" 
       default-autowire="byName"> 
		<!-- 示例 sofa 接口 --> 
    <sofa:service ref="sofaSingleParamService" interface="org.apache.shenyu.examples.sofa.api.service.SofaSingleParamService"> 
        <sofa:binding.bolt/> 
    </sofa:service> 
		<!-- 示例 sofa 接口 --> 
    <sofa:service ref="sofaMultiParamService" interface="org.apache.shenyu.examples.sofa.api.service.SofaMultiParamService"> 
        <sofa:binding.bolt/> 
    </sofa:service> 
</beans> 
```

3. Add the `@ShenyuSofaClient` annotation to the interface.

```java
@ShenyuSofaClient("/demo") @Service public class SofaClientMultiParamServiceImpl implements SofaClientMultiParamService {
@Override @ShenyuSofaClient("/findByIdsAndName") public SofaSimpleTypeBean findByIdsAndName(final List<Integer> ids, final String name) {return new SofaSimpleTypeBean(ids.toString(), "hello world shenyu sofa param findByIdsAndName ：" + name);}}
```

- In shenyu-admin --> BasicConfig --> Plugin --> `sofa` set Status enabled.

  ![image-20220829193836286](assets/images/enable-sofa-en-0fdb2ba4cad714e87d04fb8fa4bd4591_521b92baf6321370.png)

![image-20220829193913149](assets/images/sofa-registry-en-a6f245993c5792729effce29214f0b87_c8d7434e46496e41.png)

- `protocol`: Register center protocol, currently supports zookeeper、consul、nacos.
- `register`: The service IP and PORT of the registry.
- `threadpool`：There are five types of business thread pools: `fixed`, `eager`, `cached`, `limited` and `shared`. The first 4 types correspond to the thread pools officially provided by dubbo. Let's talk about `shared`, as its name implies, `all proxy plugins` share a `shared` thread pool, the advantage of this is that it can reduce the number of thread pools, thereby reducing memory and improving resource utilization.
- `corethreads`：The number of core threads in the business thread pool.
- `threads`：The maximum number of threads in the business thread pool.
- `queues`：The length of the blocking queue of the business thread pool, 0 means `unbounded blocking queue`.

> Flow needs to be matched by selector.

![image-20220829193948830](assets/images/selector-config-en-0c4c2b8f91583b3e13bf41f09b0e2ab2_aab220e31b9f730d.png)

- Automatically configure the selector with the `@ShenyuSofaClient` annotation.

> After the traffic has been successfully matched by the selector, it will enter the rules for the final traffic matching.

![image-20220829194018202](assets/images/rule-config-en-64d4b22ac30218bf808693c6f2f94e2d_15616d0bca05c338.png)

- Automatically configure the selector with the `@ShenyuSofaClient` annotation.

> When the `sofa` application client accesses the `Apache ShenYu` gateway, it will be automatically registered, and can be viewed in the `-shenyu-admin` backend management system's basic configuration `-->` metadata management, each `sofa` interface method, will correspond to a metadata.

![image-20220829194058044](assets/images/metadata-config-en-fa04cf537ccb6e5e3e14b9cc6ad907a0_c1681d0313970a70.png)

- AppName: specifies the name of the application to which the metadata belongs.
- MethodName: the name of the method to call.
- Path: http request path.
- PathDescribe: the description of the path is easy to view.
- ParamsType: the parameters are separated by commas (,) in the order of interface parameter types.
- RpcExpand: other configurations of the `sofa` interface, which support the `JSON` format.

  examples：`{"loadbalance":"hash","retries":3,"timeout":-1}`

  - `loadbalance`：Load balancing policy, currently supports roundRobin, random and hash.
  - `retries`：Number of retries to call client timeout failures.
  - `timeout`：Calling the client's timeout time.
- Interface: The fully qualified class name of the `sofa` interface.
- RpcType：choose `sofa`.

- Start `Zookeeper` service.
- Start `ShenYu Admin`.
- Start `Shenyu Bootstrap`.

- In shenyu-admin --> BasicConfig --> Plugin --> `sofa` set Status enabled, And adjust the registry configuration as needed.
- Adjust to the actual situation [shenyu-examples-sofa](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-sofa) application.yml configuration in the project and start it.

![image-20220828012420068](assets/images/check-request-zh-c4535143f335e2e88be54d7d10a65d61_b9e3061a92ab1098.png)

<a id="plugin-center-proxy-sofa-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `sofa` set Status disable.

![image-20220829194151368](assets/images/close-sofa-en-5e49d5ba450a5fb8dc793c11a7422f9a_0030564a40c3a463.png)

---

<a id="plugin-center-proxy-spring-cloud-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/spring-cloud-plugin/ -->

<!-- page_index: 74 -->

# 1. Overview

Version: 2.7.0.3

- SpringCloud Plugin

- transform http to springcloud
- springcloud gray flow control

- transform http protocol into springCloud protocol.

- Core Module `shenyu-plugin-springcloud`
- Core Class `org.apache.shenyu.plugin.springcloud.SpringCloudPlugin`

Since ShenYu 2.4.0

<a id="plugin-center-proxy-spring-cloud-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

- Add related dependencies and enable plugin, please refer to: [Quick start with Spring Cloud](#quick-start-quick-start-springcloud) .
- `Spring Cloud` client access, please refer to: [Spring Cloud Proxy](#user-guide-proxy-spring-cloud-proxy) .

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Eureka Registry

```xml
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-springcloud</artifactId> 
  <version>${project.version}</version> 
</dependency> 
 
<dependency> 
  <groupId>org.springframework.cloud</groupId> 
  <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId> 
  <version>${eureka-client.version}</version> 
</dependency> 
 
<dependency> 
  <groupId>org.springframework.cloud</groupId> 
  <artifactId>spring-cloud-commons</artifactId> 
  <version>${spring-cloud-commons.version}</version> 
</dependency> 
 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> 
  <version>${project.version}</version> 
</dependency> 
```

- Nacos Registry

```xml
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-springcloud</artifactId> 
  <version>${project.version}</version> 
</dependency> 
 
<dependency> 
  <groupId>com.alibaba.cloud</groupId> 
  <artifactId>spring-cloud-starter-alibaba-nacos-discovery</artifactId> 
  <version>${nacos-discovery.version}</version> 
</dependency> 
 
<dependency> 
  <groupId>org.springframework.cloud</groupId> 
  <artifactId>spring-cloud-commons</artifactId> 
  <version>${spring-cloud-commons.version}</version> 
</dependency> 
 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-httpclient</artifactId> 
  <version>${project.version}</version> 
</dependency> 
```

```yaml
spring: 
  cloud: 
    discovery: 
      enabled: true 
 
eureka: 
  client: 
    enabled: true 
    serviceUrl: 
      defaultZone: http://localhost:8761/eureka/ 
  instance: 
    prefer-ip-address: true 
```

```yaml
spring: 
  cloud: 
    discovery: 
      enabled: true 
    nacos: 
      discovery: 
        server-addr: 127.0.0.1:8848 # Spring Cloud Alibaba Dubbo use this. 
        enabled: true 
        namespace: ShenyuRegisterCenter 
```

> *Notice*
>
> After ShenYu 2.5.0(include), ShenYu use `shenyu-loadbalancer` as loadbalancer client, you just config loadbalance in springcloud plugin rule.
> if you don't config loadbalance, springcloud plugin will use `roundRobin` algorithm.
>
> Before ShenYu 2.4.3(include), ShenYu use `Ribbon` as loadbalancer client, you must config loadbalancer as follows.

```yaml
spring: 
  cloud: 
    loadbalancer: 
      ribbon: 
        enabled: true 
```

- In shenyu-admin --> BasicConfig --> Plugin --> `springCloud` set Status enabled.

![](assets/images/springcloud-open-en_10c7c781d3476035.png)

- you must config springcloud registry and set springcloud plugin enabled.

![](assets/images/selector-en-2-ee54c943437d9b25d6014ebf6fd2ef4e_32678634aa8b2f7f.png)

- Gray routing

if you want to user gray route in springCloud-plugin, you can click the `gray` button.

![](assets/images/gray-en-2-a6f62d441d0d0b41452abdc8962eb544_2b3122b06fc2b30e.png)

- Gray level publishing can customize and control the traffic proportion of new version applications when publishing new version applications, gradually complete the full launch of new version applications, maximize the business risk caused by new version publishing, reduce the impact surface caused by faults, and support rapid roll back.

when the gray is open,Gateway load balancing will select one node from the current node list for routing and you can modify node weights to change the weight of nodes in the load balancing algorithm.

![](assets/images/gray_40764ac2deafdf71.png)

It should be noted that,if your business instance not use the client jar of `shenyu-client-springcloud`, You should add gray node information manually on this selector page.

- `serviceId`: your springcloud service id
- `gray`：enable gray routing.

  - `protocol`: protocol default is 'http://'.
  - `upstreamUrl`: the server instance host, ip:port.
  - `weight`: the server instance and participate in load balancing calculation.
  - `status`: true: the server is available，false: the server is unavailable.
  - `timestamp`: the server's start time.
  - `warmup`: the server's warm up time and and participate in load balancing calculation.

Rule Handler, the `handle` field, can be performed by the gateway after the final matching of traffic. For more information, please refer to [Plugin handle management](#user-guide-admin-usage-plugin-handle-explanation) in Plugin Config.

- use `shenyu-client-springcloud` rule config

![](assets/images/rule-en-2-accf682c14590865cbcdcb39b6d58b54_7b9ee765385ddec7.png)

- details：

  - `timeout`：set time out.
  - `loadbalance`：loadbalance algorithm,there are three options: `roundRobin`,`random`,`hash`
- not use `shenyu-client-springcloud` rule config

![](assets/images/rule-en-ac80ec4eabec57e3005aca1b5c9fa3c1_ec1f4a7e0d16c0a8.png)

- details：

  - `path`：request path.
  - `timeout`：set time out.

you can config springcloud serviceInstance cache in `shenyu-bootstrap.yml` as follows.

```yaml
shenyu: 
  springCloudCache: 
    enabled: false 
```

this config will help you get serviceInstance from springcloud registry every heartbeat time(listen to spring cloud heartbeat event)

- when you use nacos or eureka as registry, you can config springcloud serviceInstance cache to `false`.
- when you use zookeeper or consul as registry, you can config springcloud serviceInstance cache to `true`.

- Start `Eureka` or `Nacos` Registry, if you use eureka, start `shenyu-examples-eureka` in `shenyu-example`
- Start `ShenYu Admin` application
- Start `shenyu-examples-springcloud`

- In shenyu-admin --> BasicConfig --> Plugin --> `springCloud` set Status enabled.
- Config SpringCloud Registry in `ShenYu Bootstrap`, please read [2.3 Config SpringCloud in ShenYu-Boostrap](#2.3 Config SpringCloud in ShenYu-Boostrap)

![](assets/images/selector-en-2-ee54c943437d9b25d6014ebf6fd2ef4e_32678634aa8b2f7f.png)

if your want to use gray flow and the gray flow have registered to `ShenyYu`, you must config gray upstream as follows.

![](assets/images/gray-en-2-a6f62d441d0d0b41452abdc8962eb544_2b3122b06fc2b30e.png)

if you use `shenyu-client-springcloud` register service to `ShenYu`, you don't config rule, if you want to change rule config, please read [2.5.3 Rule Config](#2.5.3 Rule Config)

![](assets/images/springcloud-request-a2b6b014e19f9de790a62f353723071b_d8f37a98b038fab4.png)

- Start `Eureka` or `Nacos` Registry, if you use eureka, start `shenyu-examples-eureka` in `shenyu-example`
- Start `ShenYu Admin` application
- Start `shenyu-examples-springcloud`

- In shenyu-admin --> BasicConfig --> Plugin --> `springCloud` set Status enabled.
- Config SpringCloud Registry in `ShenYu Bootstrap`, please read [2.3 Config SpringCloud in ShenYu-Boostrap](#2.3 Config SpringCloud in ShenYu-Boostrap)

![](assets/images/selector-en-2-ee54c943437d9b25d6014ebf6fd2ef4e_32678634aa8b2f7f.png)

if your want to use gray flow and the gray flow unregister to `ShenyYu`, you must config gray upstream as follows.

![](assets/images/gray-en-2-a6f62d441d0d0b41452abdc8962eb544_2b3122b06fc2b30e.png)

![](assets/images/rule-en-ac80ec4eabec57e3005aca1b5c9fa3c1_ec1f4a7e0d16c0a8.png)

you must config `path` in rule config, `path` is your service uri, for example: `/springcloud/new/feature/gateway/not`, `timeout` is your service allow timeout.

```text
### shengyu getway proxy not support 
POST http://localhost:9195/springcloud/new/feature/gateway/not 
Accept: application/json 
Content-Type: application/json 
rpc_type: springCloud 
```

![](assets/images/springcloud-metadata-en-3dba84d698af7567e3ad9db0c68e0484_a11d69a2489990b4.png)

![](assets/images/springcloud-request-unregistered-9a6e941b32cd45ac1789f4c5ef115529_091db6c977d24e00.png)

<a id="plugin-center-proxy-spring-cloud-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `springCloud` set Status disable.

---

<a id="plugin-center-proxy-tars-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/tars-plugin/ -->

<!-- page_index: 75 -->

# 1. Overview

Version: 2.7.0.3

- Tars plugin

- Protocol conversion, a plugin that converts http protocol requests into the Tars framework protocol
- Service Load Balancing.

- Converting http protocol requests to Tars framework protocol.

- Core Module `shenyu-plugin-tars`
- Core Class `org.apache.shenyu.plugin.tars.TarsPlugin`

- 2.3.0

<a id="plugin-center-proxy-tars-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![image-20221206221707914](assets/images/produce-chart-en-2efaa216b9aca95860902c4e62dac10e_d83dcfe830188280.png)

```xml
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-client-tars</artifactId> 
            <version>${shenyu.version}</version> 
        </dependency> 
```

1. Configure the Tars configuration in application.yml.

```yaml
shenyu: 
  register: 
    registerType: http #zookeeper #etcd #nacos #consul 
    serverLists: http://localhost:9095 #localhost:2181 #http://localhost:2379 #localhost:8848 
    props: 
      username: admin 
      password: 123456 
  client: 
    tars: 
      props: 
        contextPath: /tars 
        appName: tars 
        port: 21715 
        host: 192.168.41.103 # client IP 
```

2. Add the `@ShenyuTarsService` and `@ShenyuTarsClient` and annotation to the interface.

```java
@TarsServant("HelloObj") @ShenyuTarsService(serviceName = "ShenyuExampleServer.ShenyuExampleApp.HelloObj") public class HelloServantImpl implements HelloServant {
@Override @ShenyuTarsClient("/hello") public String hello(final int no, final String name) {return String.format("hello no=%s, name=%s, time=%s", no, name, System.currentTimeMillis());}}
```

- In shenyu-admin --> BasicConfig --> Plugin --> `tars` set Status enabled.

![enable_tars_en](assets/images/enable-tars-en-adbf5589ad2bbb3d15136b87ddc0398c_627f459217d47a0f.png)

![plugin_config_en](assets/images/plugin-config-en-bdb93d3db24b39ce654594ab25e41d0e_9f2a2da77d5020fb.png)

- `multiSelectorHandle`：Set to enable multiple selector processing, multiple selector processing services can be configured in the selector list.
- `multiRuleHandle`：Set to multiple rules processing, configure multiple processing rules in the rule list, it is recommended to configure as single rule.
- `threadpool`：There are five types of business thread pools: `fixed`, `eager`, `cached`, `limited` and `shared`. The first 4 types correspond to the thread pools officially provided by dubbo. Let's talk about `shared`, as its name implies, `all proxy plugins` share a `shared` thread pool, the advantage of this is that it can reduce the number of thread pools, thereby reducing memory and improving resource utilization.
- `corethreads`：The number of core threads in the business thread pool.
- `threads`：The maximum number of threads in the business thread pool.
- `queues`：The length of the blocking queue of the business thread pool, 0 means `unbounded blocking queue`.

> Flow needs to be matched by selector.

![selector_config_en](assets/images/selector-config-en-480ebdaf7d31b5e65c74225ba58424a3_8f20ed62ebfe8946.png)

Automatically configure the selectors with the `@ShenyuTarsClient` annotation.

> After the traffic has been successfully matched by the selector, it will enter the rules for the final traffic matching.

![rule_config_en](assets/images/rule-config-en-f235fadf861a283cb385c641139ab56a_2c0a2623fcdec301.png)

Automatically configure the rules with the `@ShenyuTarsClient` annotation.

> When the `Tars` application client accesses the `Apache ShenYu` gateway, it will be automatically registered, and can be viewed in the `shenyu-admin` backend management system's basic configuration `-->` metadata management, each `Tars` interface method, will correspond to a metadata.

![metadata_config_en](assets/images/metadata-config-en-55b4de23e1b38626a9b401003ae6c018_0670b0202b0adb9e.png)

- AppName: specifies the name of the application to which the metadata belongs.
- MethodName: the name of the method to call.
- Path: http request path.
- PathDescribe: the description of the path is easy to view.
- ParamsType: the parameters are separated by commas (,) in the order of interface parameter types.
- RpcExpand: other configurations of the `Tars` interface, which support the `JSON` format.

  examples：`{"loadbalance":"hash","retries":3,"timeout":-1}`

  - `loadbalance`：Load balancing policy, currently supports roundRobin, random and hash.
  - `retries`：Number of retries to call client timeout failures.
  - `timeout`：Calling the client's timeout time.
- Interface: The fully qualified class name of the `Tars` interface.
- RpcType：Auto-registration defaults to `Tars`.

- Start `ShenYu Admin`.
- Start `Shenyu Bootstrap`.

- In shenyu-admin --> BasicConfig --> Plugin --> `tars` set Status enabled, And adjust the registry configuration as needed.
- Adjust to the actual situation [shenyu-examples-tars](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-tars) application.yml configuration in the project and start it.

![check_request_zh](assets/images/check-request-zh-bbfa76e720e865629981ab1e65739eeb_8709c10c8131c187.png)

<a id="plugin-center-proxy-tars-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `tars` set Status disable.

![close_tars_en](assets/images/close-tars-en-17311011e6bc29d7156f65ec9073e859_c0ed96164d4b9eff.png)

---

<a id="plugin-center-proxy-tcp-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/tcp-plugin/ -->

<!-- page_index: 76 -->

# 1. Overview

Version: 2.7.0.3

- TCP Plugin

- Process TCP protocol requests and forward them to backend services of other TCP protocols
- Service load balancing

- Supports TCP proxy based on configured upstream list
- The upstream list can be hot-synchronized to the gateway by the admin module
- Support setting load balancing policy for requests, currently support shenyu load balancing module policy
- Configurable open port for listening, configurable reactor-netty parameter
- Enable multiple proxy selectors

>
> [!NOTE]
> : When a connection is established with the gateway, after the connection is established, the traffic continues to stay in the upstream that has been selected by the load balancing module

- Core Module: `shenyu-plugin-tcp` `shenyu-protocol-tcp`

- 2.6.0

<a id="plugin-center-proxy-tcp-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

- When using it for the first time, start the admin server,
  in `shenyu-admin` --> BasicConfig --> Plugin, search for the tcp plugin and click "Resource" to activate the TCP plugin module.

![init-tcp-en](assets/images/init-tcp-en-4584b71f42ac085b7891906821981f5d_f59354578d732370.png)

- In `shenyu-admin` --> BasicConfig--> Plugin --> `tcp`, set status enabled.

![start-tcp-en](assets/images/start-tcp-en-4d297b59fea93f6262eda73363106fbf_27eb66c2a7c62cd3.png)

- The TCP plugin is created in units of proxy-selectors, so configuring the plugin is to configure the properties of the proxy-selector.
  When creating a proxy-selector, click the "Add" button on the page, and in the pop-up selector form, you can configure the selector properties:

![selector_props_en](assets/images/selector-props-en-142de223b88aee9c183b63679771c465_314828b4b0df454d.png)

The default configuration is as follows:

```json
{ 
  "loadBalanceAlgorithm": "random", 
  "bossGroupThreadCount": "1", 
  "workerGroupThreadCount": "12", 
  "clientMaxConnections": "20", 
  "clientMaxIdleTimeMs": "30000", 
  "clientMaxLifeTimeMs": "60000", 
  "clientPendingAcquireTimeout": "5", 
  "clientPendingAcquireMaxCount": "5" 
} 
```

- `loadBalanceAlgorithm` : shenyu load balancing algorithm, random by default
- `bossGroupThreadCount` , `workerGroupThreadCount`:
  ReactorNetty TcpServer For configuration details, see `shenyu-protocol-tcp#TcpBootstrapServer#start` for details
- `clientMaxConnections` , `clientMaxIdleTimeMs` , `clientMaxLifeTimeMs` , `clientPendingAcquireTimeout` ,
  `clientPendingAcquireMaxCount`
  ReactorNetty `ConnectionProvider` , see `shenyu-protocol-tcp#ConnectionContext` for details

You can search for the tcp plugin in `shenyu-admin` --> BasicConfig --> PluginHandle, and modify the default configuration:

![plugin_handle_en](assets/images/plugin-handle-en-4b5f6172dc424e386d079e2f98d46544_52466758dd07767b.png)

`discovery` see [discovery-mode](https://shenyu.apache.org/docs/plugin-center/discovery/discovery-mode.md)

The TCP plugin supports two levels of discovery configuration: plugin-level and selector-level:

① You can click the "Discovery Configuration" button on the page to configure plugin-level discovery in the pop-up form.
After the configuration is complete, you can open the form again to modify or delete the previous configuration.
After the plug-in level discovery is configured, the discovery settings of the selectors are consistent with the plugin-level config by default:

![discovery_config_en](assets/images/discovery-config-en-95d68cd3d3dc00d2d1542ff79aab650e_d2d5617e4f0fffd3.png)

② If you have not configured plugin-level discovery, you can configure the selector-level discovery every time you create a proxy-selector:

![selector_discovery_en](assets/images/selector-discovery-en-c29eb5ec2a7c017e6c74ecf324cea5f0_ec372a545aea3e8c.png)

Discovery `Zookeeper` and `Local` modes are currently supported.

- When the type of service Discovery is Zookeeper, you need to fill out the Discovery-ZooKeeper configuration training for details [discovery-mode](https://shenyu.apache.org/docs/plugin-center/discovery/discovery-mode.md)
- In zookeeper mode, the discovery module will automatically monitor the user's zookeeper registration center
  and automatically maintain discovery upstreams:

![zookeeper.png](assets/images/zookeeper-02405e396bbe1de2d53c3ac3943fdbed_ba7f2116936915ec.png)

- When "local" is selected as the discovery type,
  you need to manually fill in the discovery upstream list.
  As shown in the figure below, the discovery upstream list is an editable table.
  Double-click each cell to modify the table content:

![local_selector_en.png](assets/images/local-selector-en-fbcfaa38524bf9b33cd887ae2607b849_b2ecf195283a8052.png)

- In addition to the discovery configuration above, when creating a selector,
  you also need to fill in the "basic config" part of the selector,
  including name and forward port, etc. In order to improve the convenience of filling in,
  you can click "Copy Selector" to copy part of the information of the created selector.

>
> [!NOTE]
> : The name of the selector uniquely identifies the selector and cannot be repeated

![selector_basic_en.png](assets/images/selector-basic-en-3e19e72619bff948afc38506ae75ba4a_7e70a6ca09340d89.png)

- After the selectors are created,
  the selectors are displayed in the form of cards.
  When the mouse hovers over the cards, the creation time, update time and properties of the selectors will be displayed.
  At the bottom of the card there are three clickable icons, from left to right the Sync, Edit, and Delete selector icons:

![card_list_en.png](assets/images/card-list-en-b1d754f9380710d7570b0bb00054e74f_6059bbf9d7b73e17.png)

- If there is difference between the discovery upstream list of the current admin and the gateway,
  you can click the "Sync" icon to force synchronization to the gateway.

- shenyu-gateway port start log
  ![gateway_start_port_log.png](assets/images/gateway-start-port-log-66e5b55d4865a6cf6e2219d9678e724e_e3646443e594bceb.png)
- shenyu-gateway proxy upstreamList‘s success log
  ![gateway_upstream_list.png](assets/images/gateway-upstream-list-45dd034fab2ed19e67687c9d135dcba9_0b8c105cda89b565.png)

Take proxying redis as an example, use `redis-cli -p {forwardPort}` to access.

![connection.png](data:image/png;base64,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)

---

<a id="plugin-center-proxy-websocket-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/proxy/websocket-plugin/ -->

<!-- page_index: 77 -->

# 1. Overview

Version: 2.7.0.3

- Websocket Plugin.

- Forwarding scenarios, processing websocket protocol requests and forwarding them to other websocket protocol services on the backend.
- Service Load Balancing.

- Support traffic management based on host, uri, query and other request information.
- Supports setting load balancing policies for requests and also supports service warm-up, currently supports three policies: ip hash (consistent hashing with virtual nodes), round-robbin (weighted polling), random (weighted random).
- Support setting interface level request timeout time.
- Support setting the number of timeout retries.

- Core Module `shenyu-plugin-websocket`.
- Core Class `org.apache.shenyu.plugin.websocket.WebSocketPlugin`.

- 2.4.3

<a id="plugin-center-proxy-websocket-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![image-20220726223545558](assets/images/procedure-chart-en-d7602e00db6527ccd37f649b15fa3d9b_a9654d3923c19bec.png)

**Explanation of terms**

- Shenyu gateway service：Include shenyu-admin and shenyu-bootstrap services.
- Client services：Real backend websocket service.

**Explanation of the process**

1. Start shenyu gateway service: Refer to the deployment, start shenyu-admin and shenyu-bootstrap to make sure shenyu gateway service is normal.
2. Enable the websocket plugin in shenyu-admin: Turn on the websocket plugin in the shenyu-admin plugin management page.
3. Configure and start the client service: start the client project (real websocket service on the back end) and configure the service information into the shenyu gateway, in two ways: manual configuration and automatic configuration.
4. Check if forwarding is normal: Check if forwarding is successful.

- In shenyu-admin --> BasicConfig --> Plugin --> websocket is set to on.

![image-20220726224444058](assets/images/enable-websocket-en-7bf13e1c7396e1c12ebe0f39230390e1_07392c79d13d6c1f.png)

> Manually configure the client service on the shenyu-admin page, and the backend service will implement the websocket protocol forwarding without any changes.

1. Adding selectors to the websocket plugin.

![image-20220726225217950](assets/images/add-selector-en-40d5626d61c16a9a9b5ac00cd8b0a6a1_1e769df6648c0946.png)

2. Add rules to the websocket plugin.

![image-20220726225315550](assets/images/add-rule-en-dccc9a34db1ca2d73a775262bdf36041_36eb7c5da86d19e0.png)

3. Start the client service (backend websocket service).
4. Test the success of service forwarding.

- See Annex 5.1 for the test code.

![image-20220726222003131](assets/images/test-result-en-e23f4e8528881c929712ae84b01d53e8_dbe6c0e63b872ff3.png)

> If there are scenarios where you need to automate configuration to reduce workload, you can add annotations to the backend service to automate the configuration of the service to the shenyu gateway.

1. Add the plugin maven configuration to the pom.xml file in the backend service project.

```xml
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
  		<artifactId>shenyu-spring-boot-starter-plugin-websocket</artifactId> 
      <version>${project.version}</version> 
  </dependency> 
```

2. Use the `@ShenyuSpringWebSocketClient` annotation, which will automatically register the websocket service to the shenyu gateway.
3. Adjust the plugin configuration, see 2.4.1 for details of the configuration parameters.
4. Start the client project (the backend `websocket service), see 2.5 for sample code.
5. Check whether the PluginList service registration information in the shenyu-admin page is registered successfully.
6. Test the success of service forwarding.

- See Annex 5.1 for the test code.

![image-20220726221945414](assets/images/test-result-en-e23f4e8528881c929712ae84b01d53e8_dbe6c0e63b872ff3.png)

- Client access method and server address, the parameters are: `shenyu.register.*`, the following example uses the http access method, currently the client supports the following access methods: http, zookeeper, etcd, nacos, consul, please refer to [client access configuration](#user-guide-property-config-register-center-access) for detailed access configuration parameters.
- Client configuration with the parameter: `shenyu.client.websocket.*`, containing the service name, routing address and port, and the contextPath value must be configured as the routing address for each service.

```yaml
shenyu: 
  register: 
    registerType: http 
    serverLists: http://localhost:9095  
    props: 
      username: admin 
      password: 123456 
  client: 
    websocket: 
      props: 
        contextPath: /ws-annotation  
        appName: ws-annotation 
        port: 8001 # Need to be consistent with the service port 
```

Using auto-configuration, after the client starts it will automatically register [selectors and rules](#user-guide-admin-usage-selector-and-rule) in shenyu-admin -> Plugin List -> Proxy -> Websocket information.
![image-20220725222628106](assets/images/auto-register-en-3b95f15cf9c9e77ab84f83d0bff3c497_8ac87e59ac996e4f.png)

The example of websocket selector configuration, please refer to [selectors and rules](#user-guide-admin-usage-selector-and-rule) for general selector configuration.

![image-20220725222913298](assets/images/config-selectors-en-6fb067685bdeef81b55411f443b4a738_22b9d3e88cc4426a.png)

- `host`：Fill in `localhost`, this field is not used for now.
- `ip:port`：`ip` and port, here fill in the `ip` + port of your real service.
- `protocol`：`ws` protocol, do not fill in the default: `ws://`.
- `startupTime`：Start-up time in milliseconds.
- `weight`：The default value for load balancing weight, which is automatically registered for service startup, is 50.
- `warmupTime`：Warm-up time, in milliseconds, the server in warm-up will calculate the instantaneous weight, the calculated value will be less than the actual weight configured to protect the server just started, the default value of service start registration is 10. For example, the warm-up time is 100 milliseconds, currently started 50 milliseconds, the configured weight is 50, the actual weight is 25.
- `status`：open or close, the start state of this processor is only valid.

The example of websocket rule configuration, please refer to [selectors and rules](#user-guide-admin-usage-selector-and-rule) for general rule configuration .

![image-20220725223225388](assets/images/config-rules-en-2dc38e12c2c04f95d351ba1567839b24_d69a9bd6f8613164.png)

- `loadStrategy`: if the websocket client is a cluster, which load balancing strategy to take when the Apache ShenYu gateway is invoked, currently supports roundRobin, random and hash.
- `timeout`: The timeout period for calling the client.
- `retryCount`: The number of retries to call client timeout failures.

[shenyu-example-spring-annotation-websocket](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-websocket/shenyu-example-spring-annotation-websocket)

[shenyu-example-spring-native-websocket](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-websocket/shenyu-example-spring-native-websocket)

[shenyu-example-spring-reactive-websocket](https://github.com/apache/shenyu/tree/master/shenyu-examples/shenyu-examples-websocket/shenyu-example-spring-reactive-websocket)

<a id="plugin-center-proxy-websocket-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- shenyu-admin --> BasicConfig --> Plugin --> Close websocket plugin status.

![image-20220726231206572](assets/images/close-websocket-en-57cc860359037abaf7e7ff539a519003_1abad0847313b95b.png)

<a id="plugin-center-proxy-websocket-plugin--4.-frequently-asked-questions"></a>

# 4. Frequently Asked Questions

**4.1 Websocket connection establishment error 1002**

Possible causes: client service is not normal, shenyu gateway and client project can not establish a normal connection, please check the gateway to the client network, client service is normal.

**4.2 Multiple client services are displayed as empty in the websocket selector**

Possible cause: BasicConfig -> Plugin -> websocket -> multiSelectorHandle option select multiple handle.

![image-20220726222250136](assets/images/questions-multiselectorhandle-en-9761e919964a55a683768475e3021049_61dbc0d2b46746c3.png)

<a id="plugin-center-proxy-websocket-plugin--5.-annexes"></a>

# 5. Annexes

- Create a file called websocket.html and copy the following code into the file.
- Open websocket.html with Chrome.

```html
<!DOCTYPE HTML> 
<html> 
<head> 
    <meta http-equiv="content-type" content="text/html" /> 
    <title>Shenyu WebSocket Test</title> 
    <script> 
        var websocket; 
        function connect() { 
            try { 
                websocket = new WebSocket(document.getElementById("url").value); 
                websocket.onopen = onOpen; 
                websocket.onerror = onError; 
                websocket.onmessage = onReceive; 
                websocket.onclose = onClose; 
            } catch (e) { 
                alert('[websocket] establish connection error.'); 
            } 
        } 
        function onOpen() { 
            alert('[websocket] connect success.'); 
        } 
        function onError(e) { 
            alert("[websocket] connect error. code: " + e.code); 
        } 
        function onReceive(msg) { 
            var show = document.getElementById("show"); 
            show.innerHTML += "[Server Response] => " + msg.data + "<br/>"; 
            show.scrollTop = show.scrollHeight; 
        } 
        function onClose(e) { 
            console.log("[websocket] connect closed. code: " + e.code) 
            alert("[websocket] connect closed."); 
            document.getElementById("show").innerHTML = ""; 
            document.getElementById("msg").value = ""; 
            websocket = null; 
        } 
        function buttonClose() { 
            if (websocket == null) { 
                console.log("Please establish a connection first.") 
            } else { 
                websocket.close(1000); 
                document.getElementById("show").innerHTML = ""; 
                document.getElementById("msg").value = ""; 
            } 
        } 
        function send() { 
            if (websocket == null) { 
                alert("Please establish a connection first.") 
            } else { 
                var msg = document.getElementById("msg").value; 
                show.innerHTML += "[Client Request] => " + msg + "<br/>"; 
                websocket.send(msg); 
            } 
        } 
    </script> 
</head> 
<body> 
    <input id="url" type="text" value="ws://localhost:9195/ws-annotation/myWs"><br /> 
    <input id="msg" type="text"><br /> 
    <button id="connect" onclick="connect();">Connect</button> 
    <button id="send" onclick="send();">Send</button> 
    <button id="close" onclick="buttonClose();">Close</button></br> 
    <div id="show" class="show"></div> 
</body> 
</html> 
<style> 
    input { 
        width: 400px; 
        margin-bottom: 10px; 
    } 
    .show { 
        width: 600px; 
        height: 400px; 
        overflow-y: auto; 
        border: 1px solid #333; 
        margin-top: 10px; 
    } 
</style> 
```

---

<a id="plugin-center-fault-tolerance-hystrix-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/fault-tolerance/hystrix-plugin/ -->

<!-- page_index: 78 -->

# 1. Overview

Version: 2.7.0.3

- Hystrix Plugin

- The backend service is unstable, use hystrix for protection

- Fusing the flow
- Protect the application behind ShenYu Gateway
- Isolation mode supports `thread` and `semaphore`.

- Core Module: `shenyu-plugin-hystrix`
- Core Class: `org.apache.shenyu.plugin.hystrix.HystrixPlugin`

- Since ShenYu 2.4.0

<a id="plugin-center-fault-tolerance-hystrix-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Add `hystrix` dependency in the `pom.xml` file of the gateway.

```xml
<!-- apache shenyu hystrix plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-hystrix</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu hystrix plugin end--> 
```

- In `shenyu-admin`--> BasicConfig --> Plugin --> `hystrix` set to enable.

- No Config, but you should open hystrix plugin.

It is used to filter traffic for the first time and does not require handle fields.

For more information on selectors and rules configuration, see [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) , only some of the fields are covered here.

![](assets/images/selector-en-b44d5128003f1f2cc5f9cc6d0aee9a5f_73fa8d4629da1982.png)

- For the final filtering of traffic, there is a rule handler logic, isolation mode supports `thread` and `semaphore`.

![](assets/images/rule-en-e4b2b2b83e12da05d99784fd35e0d590_b28cdfab82b74c7e.png)

- Hystrix handler details:

  - `MinimumRequests`: the minimum number of requests required to trigger a circuit breaker.
  - `ErrorThresholdPercentage`: percentage of exception occurring during that time.
  - `Timeout`(ms): execution timeout.
  - `MaxConcurrentRequests`: max concurrent requests.
  - `Sleep`(ms): The recovery time after the circuit breaker.
  - `GroupKey`: It is generally set to: `contextPath`.
  - `CallBackUrl`: default url `/fallback/hystrix`.
  - `CommandKey`: generally, it is set to a specific path interface.

- Start ShenYu Admin
- Start ShenYu Bootstrap
- Start a backend service

![](assets/images/selector-en-b44d5128003f1f2cc5f9cc6d0aee9a5f_73fa8d4629da1982.png)

- The rules in the pictures below are test examples, actual environment depends on the specific situation.

![](assets/images/hystrix-example-rule-en-061686d393c8d34e9cc3f61973513eda_16d0fa5fa089f81d.png)

- test example

```java
@RestController @RequestMapping("/test") @ShenyuSpringMvcClient("/test/**") public class HttpTestController {@PostMapping("/testHystrix") public ResultBean ok() {Random random = new Random(); int num = random.nextInt(100); if (num > 20) {throw new RuntimeException();} return new ResultBean(200, "ok", null);}}
```

![](assets/images/hystrix-send-request-bdd87396a153240c2408c12f3e39d5f1_e70e60b74267a79a.png)

![](assets/images/hystrix-result-008924e1e83b1489d3f0aaac4e4761df_8fca2a649877c5c4.png)

<a id="plugin-center-fault-tolerance-hystrix-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `hystrix` set Status disable.

---

<a id="plugin-center-fault-tolerance-rate-limiter-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/fault-tolerance/rate-limiter-plugin/ -->

<!-- page_index: 79 -->

# 1. Overview

Version: 2.7.0.3

- RateLimiter Plugin

- traffic control in gateway cluster environment
- rate limiting according to specific rules
- You can set to the interface level, or the parameter level. How to use it depends on your traffic configuration.

- use redis to control gateway traffic

- Core Module `shenyu-plugin-ratelimiter`.
- Core Class `org.apache.shenyu.plugin.ratelimiter.RateLimiterPlugin`
- Core Class `org.apache.shenyu.plugin.ratelimiter.executor.RedisRateLimiter`

- Since ShenYu 2.4.0

- The system generates the token at a constant rate, and then puts the token into the token bucket.
- The token bucket's capacity. When the bucket is full, the token put into it will be discarded.
- Each time requests come, you need to obtain a token from the token bucket. If there are tokens, the service will be provided; if there are no tokens, the service will be rejected.

- Flow Diagram：
  ![](assets/images/tokenbucket-a11a51776844dc57cb9ba82904dc4ca6_26af79034a849bc2.png)

- water (request) go to the leaky bucket first. The leaky bucket goes out at a fixed speed. When the flow speed is too fast, it will overflow directly (reject service)

- Flow Diagram：
  ![](assets/images/leakybucket-cc829d5529e0847152a90793867e9f96_0152b84441ed0ffe.png)

- The sliding time window maintains the count value of unit time. Whenever a requests pass, the count value will be increased by 1. When the count value exceeds the preset threshold, other requests in unit time will be rejected. If the unit time has ended, clear the counter to zero and start the next round counting.

- Flow Diagram：
  ![](assets/images/sldingwindow-c529b50727afb275845585edb72b0215_0ef27388b8cdf5a2.png)

<a id="plugin-center-fault-tolerance-rate-limiter-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Add `rateLimiter` dependency in `pom.xml` file of the gateway.

```xml
<!-- apache shenyu ratelimiter plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-ratelimiter</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu ratelimiter plugin end--> 
```

- In `shenyu-admin`--> BasicConfig --> Plugin --> `rateLimiter` set to enable.

![](assets/images/ratelimiter-plugin-en-db82d697a0e4dedda72274a7f72a80f3_1876edf8ccb3f1fc.png)

- `mode`: the working mode of redis, the default is single-point mode: `standalone`, in addition to cluster
  mode: `cluster`, sentinel mode: `sentinel`.
- `master`: default is master.
- `url`: configure the IP and port of the redis database, configured by colon connection, example: `192.168.1.1:6379`.
- `password`: the password of the redis database, if not, you can not configure.

- Selectors and rules, please refer to: [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule)

![](assets/images/ratelimiter-plugin-rule-en-c977fc7840a3952eb0da74183290dedd_6ed65a287f5aeedd.png)

- TokenBucket/Concurrent

  - `algorithmName`: `tokenBucket`/`concurrent`.
  - `replenishRate`: It is how many requests you allow users to execute per second, while not discarding any requests. This is the filling rate of token bucket.
  - `burstCapacity`: it is the maximum number of requests that users are allowed to execute in one second. This is token bucket can save the number of token.
  - `keyResolverName`: `whole` indicates that the traffic is limited by gateway per second, and `remoteAddress` indicates that the traffic is limited by IP per second.
- LeakyBucket

  - `algorithmName`: `leakyBucket`.
  - `replenishRate`: The rate at which requests are executed per unit time, and the rate at which water droplets leak out of the leaky bucket.
  - `burstCapacity`: The maximum number of requests that users are allowed to execute in one second. This is the amount of water in the bucket.
  - `keyResolverName`: `whole` indicates that the traffic is limited by gateway per second, and `remoteAddress` indicates that the traffic is limited by IP per second.
- SlidingWindow

  - `algorithmName`: `slidingWindow`.
  - `replenishRate`: The rate of requests per unit time, used to calculate the size of the time window.
  - `burstCapacity`: The maximum number of requests in the time window (per unit time).
  - `keyResolverName`: `whole` indicates that the traffic is limited by gateway per second, and `remoteAddress` indicates that the traffic is limited by IP per second.

- Start ShenYu Admin on `10.10.10.10:9095`
- Start two ShenYu Bootstrap on `10.10.10.20:9195` and `10.10.10.30:9195`, and config data sync center on `10.10.10.10:9095`
- config nginx, for example:

```nginx
upstream shenyu_gateway_cluster {ip_hash; server 10.1.1.1:9195 max_fails=3 fail_timeout=10s weight=50; server 10.1.1.2:9195 max_fails=3 fail_timeout=10s weight=50;}
server {location / {proxy_pass http://shenyu_gateway_cluster; proxy_set_header HOST $host; proxy_read_timeout 10s; proxy_connect_timeout 10s;}}
```

- config redis configuration with ratelimiter plugin
- config selector
- config rule

![](assets/images/rule-example-en-77a21daeb9fb7e26a8cf802f41b2587d_4ba1700813bfa596.png)

replenishRate is 3, burstCapacity is 10

- jmeter thread group configuration

![](assets/images/jmeter-thread-group-d9b10e917818cec79120a61e3c3451b6_b56d76f6a7ad9729.png)

- jmeter http request configuration

![](assets/images/jmeter-http-request-0023ff8824d62685af80b3c2de6d40e4_9444323518b56db6.png)

![](assets/images/jmeter-result-cc7f6f7a1d678078ae3d3058b6d0afff_9618550cbfc2a5c2.png)

<a id="plugin-center-fault-tolerance-rate-limiter-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `rateLimiter` set Status disable.

---

<a id="plugin-center-fault-tolerance-resilience4j-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/fault-tolerance/resilience4j-plugin/ -->

<!-- page_index: 80 -->

# Resilience4j Plugin

Version: 2.7.0.3

- `Resilience4j` is one of the options that supports flow control and circuit breaking.
- `Resilience4j` supports flow control and circuit breaking functions for gateway.

Select a mode to start shenyu-admin. For details, see deployment. For example, with [Local Deployment](#deployment-deployment-local) starts the `Apache ShenYu` background management system.

- In BasicConfig --> Plugin --> resilience4j, set to enable.
- If the user don't use, please disable the plugin in the background.

![](assets/images/resilience4j-plugin-en-1_1704f670c4e8a505.png)

- Add `resilience4j` dependency in the `pom.xml` file of the gateway.

```xml
        <!-- apache shenyu resilience4j plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-resilience4j</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <!-- apache shenyu resilience4j plugin end--> 
```

For more information on selectors and rules configuration, see [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) , only some of the fields are covered here.

It is used to filter traffic for the first time and does not require handle fields.

![](assets/images/resilience4j-plugin-en-2_bc97d7d9addbf631.png)

For the final filtering of traffic, there is a rule handler logic.

![](assets/images/resilience4j-plugin-en-3_99a019aaecd64977.png)

- Resilience4j Processing Details

  - `limitForPeriod` ：Configures the number of permissions available during one limit refresh period,default value:`50`.
  - `limitRefreshPeriod` ：Configures the period of a limit refresh. After each period the rate limiter sets its permissions count back to the limitForPeriod value,default value:`500`.
  - `timeoutDurationRate` ：Configures wait time(ms) a thread waits for a permission,default value:`5000`.
  - `circuitEnable` ：Configures circuitBreaker enable, `0`:OFF ,`1`:ON ,default value:`0`.
  - `failureRateThreshold` ：Configures the failure rate threshold in percentage,When the failure rate is equal or greater than the threshold the CircuitBreaker transitions to open and starts short-circuiting calls,default value:`50`.
  - `fallbackUri` ：Configures the fallback uri.
  - `minimumNumberOfCalls` ：Configures the minimum number of calls which are required (per sliding window period) before the CircuitBreaker can calculate the error rate or slow call rate,default value:`100`.
  - `bufferSizeInHalfOpen`：Configures the number of permitted calls when the CircuitBreaker is half open,default value:`10`.
  - `slidingWindowSize` ：Configures the size of the sliding window which is used to record the outcome of calls when the CircuitBreaker is closed,default value:`100`.
  - `slidingWindowType` ：Configures the type of the sliding window which is used to record the outcome of calls when the CircuitBreaker is closed,
    Sliding window can either be `0`:count-based or `1`:time-based.,default value:`0`.
  - `timeoutDuration` ：Configures request CircuitBreaker timeout(ms),default value:`30000`.
  - `waitIntervalInOpen` ：Configures the circuitBreaker time(ms) of duration,default value:`10`.
  - `automaticTransitionFromOpenToHalfOpenEnabled` ：Configures automatically transition from open state to half open state,`true`:ON, `false`:OFF, default value:`false`.

---

<a id="plugin-center-fault-tolerance-sentinel-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/fault-tolerance/sentinel-plugin/ -->

<!-- page_index: 81 -->

# 1. Overview

Version: 2.7.0.3

- Sentinel Plugin

- `Sentinel` is one of the options that supports flow control and circuit breaking.
- `Sentinel` supports flow control and circuit breaking functions for gateway.

- flow control
- request circuit breaker and service degrade

- Core Module `shenyu-plugin-sentinel`.
- Core Class `org.apache.shenyu.plugin.sentinel.SentinelPlugin`

- Since 2.4.0

<a id="plugin-center-fault-tolerance-sentinel-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Add `sentinel` dependency in the `pom.xml` file of the gateway(shenyu-bootstrap).

```xml
<!-- apache shenyu sentinel plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-sentinel</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu sentinel plugin end--> 
```

- In `shenyu-admin`--> BasicConfig --> Plugin --> `sentinel` set to enable.

It is used to filter traffic for the first time and does not require `handle` fields.

![](assets/images/selector-en_5979a4b49290f63f.png)

For the final filtering of traffic, there is a rule handler logic.

![](assets/images/rule-en_19b89c76ea9b61b2.png)

| field | default value | field type | desc |
| --- | --- | --- | --- |
| degradeRuleCount |  | Doule | degrade threshold |
| degradeRuleEnable | 1(enabled) | Integer | whether enable circuit breaking function of `sentinel` |
| degradeRuleGrade | 0(slow call ratio) | Integer | circuit breaker strategy, support RT of seconds level/ Error Ratio of seconds level/ Error Count of minutes level strategy |
| degradeRuleMinRequestAmount | 5 | Integer | circuit breaker min request amount |
| degradeRuleSlowRatioThreshold | 1.0d | Double | slow ratio threshold of degrading |
| degradeRuleStatIntervals | 1 | Integer | status intervals of degrade |
| degradeRuleTimeWindow |  | Integer | time of degrading(unit: second) |
| flowRuleControlBehavior | 0(direact reject) | Integer | effect(reject directly/ queue/ slow start up), it do not support flow control by invocation relation. |
| flowRuleControlBehavior-direct rejection by default |  |  |  |
| flowRuleControlBehavior-warm up |  |  |  |
| flowRuleControlBehavior-constant speed queuing |  |  |  |
| flowRuleControlBehavior-preheating uniformly queued |  |  |  |
| flowRuleMaxQueueingTimeMs | 500ms | Integer | Maximum queuing time (valid in "preheating uniformly queued", "constant speed queuing" mode) |
| flowRuleWarmUpPeriodSec | 10 | Integer | Cold start warm-up time (seconds) (valid in "preheating uniformly queued" "warm up" mode) |
| flowRuleCount |  | Integer | sentinel flow control count |
| flowRuleEnable | 1(enabled) | Integer | whether enable sentinel flow control function. |
| flowRuleGrade | 1(QPS) | Integer | type of current limit threshold(QPS or Thread Count)。 |
| fallbackUri |  | String | degraded uri after circuit breaking. |

For more information on selectors and rules configuration, see [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) , only some of the fields are covered here.

- In `shenyu-admin`--> BasicConfig --> Plugin --> `sentinel` set to enable.

![](assets/images/example-selector-en-e663414645580533c9955129d6f307b6_5a81562972c94ce1.png)

![](assets/images/example-rule-en-1e1c6c944c9fd26e59bf67b72134bc96_6869ca41e762c9db.png)

just use qps flow control strategy, and qps is 10, reject strategy is directly reject.

the code is as follows:

```java
@RestController @RequestMapping("/order") @ShenyuSpringMvcClient("/order") public class OrderController {
/** * Save order dto.* * @param orderDTO the order dto * @return the order dto */ @PostMapping("/save") @ShenyuSpringMvcClient("/save") public OrderDTO save(@RequestBody final OrderDTO orderDTO) {orderDTO.setName("hello world save order"); return orderDTO;}}
```

- Jmeter thead group config

![](assets/images/sentinel-flow-control-config-a199d4df41efcc9c6a8b70dc7f0e3548_582cc09c7b66c7b0.png)

- Jmeter http request config

![](assets/images/sentinel-flow-control-http-c656d6e601942c7c6f9ee04aa61d95e2_350372ede97e1c8c.png)

![](assets/images/sentinel-flow-control-91b365f39a45d8bd4d3998b9e9278ea0_1616c96ca773e1b2.png)

- In `shenyu-admin`--> BasicConfig --> Plugin --> `sentinel` set to enable.

![](assets/images/example-selector-en-e663414645580533c9955129d6f307b6_5a81562972c94ce1.png)

![](assets/images/example-circuitbreaker-rule-23ad5dcc03364812c69954f80c5c3500_b7b158ca1e611724.png)

when degrade strategy is `exception number`, `degradeRuleSlowRatioThreshold` is not effective. When the minimum number of requests per unit of time is 5, and the request happens exception great than 3, it will trigger the circuit breaker.

when degrade strategy is `slow call ratio`, `degradeRuleSlowRatioThreshold` is effective, `degradeRuleCount` means RT(e.g. 200).

the code is as follows:

```java
@RestController @RequestMapping("/order") @ShenyuSpringMvcClient("/order") public class OrderController {
/** * Save order dto.* * @param orderDTO the order dto * @return the order dto */ @PostMapping("/save") @ShenyuSpringMvcClient("/save") public OrderDTO save(@RequestBody final OrderDTO orderDTO) {
Random random = new Random(); int num = random.nextInt(100); if (num > 40) {throw new RuntimeException("num great than 20");} orderDTO.setName("hello world save order"); return orderDTO;}
}
```

- Jmeter thead group config

![](assets/images/sentinel-flow-control-config-a199d4df41efcc9c6a8b70dc7f0e3548_582cc09c7b66c7b0.png)

- Jmeter http request config

![](assets/images/sentinel-flow-control-http-c656d6e601942c7c6f9ee04aa61d95e2_350372ede97e1c8c.png)

![](assets/images/example-circuitbreaker-02859aa4ac59f7c652b3c99ba9baf4b8_f6fb876763d1a002.png)

<a id="plugin-center-fault-tolerance-sentinel-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `sentinel` set Status disable.

---

<a id="plugin-center-security-casdoor"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/security/casdoor/ -->

<!-- page_index: 82 -->

# Casdoor Plugin

Version: 2.7.0.3

ShenYu has Casdoor plugin to use Casdoor

Firstly, the Casdoor should be deployed.

You can refer to the Casdoor official documentation

After a successful deployment, you need to ensure:

- The Casdoor server is successfully running on **<http://localhost:8000>**.
- Open your favorite browser and visit **<http://localhost:7001>**, you will see the login page of Casdoor.
- Input `admin` and `123` to test login functionality is working fine.

Then you can quickly implement a Casdoor based login page in your own app with the following steps.

![casdoor_config](assets/images/casdoor-config-20e7c6a1dc3df10781df800415ee651c_8a8995ca6da4b01c.png)

![casdoor_cert](assets/images/casdoor-cert-ea19a42199bd15b7446d569b67509100_468a194d73649270.png)

![casdoor_configPlugin](assets/images/casdoor-configplugin-e92c5ad845808a848120645fb00413ba_b1ccb169adec0eb0.png)

note: because the shenyu only have Single line input box so we need add \n in every line of cert.

![casdoor_cert2](assets/images/casdoor-cert2-b483af40e83475bafaddc1e41727137c_36a7b8ab87d9ff50.png)

You can copy it and paste it on the certificate of shenyu casdoor config.

**You don't need save it in Casdoor certificate editing page**,because it just for copying.

![casdoor_casdoor](assets/images/casdoor-casdoor-9382e2b98d7facaf3b335574d2696df0_7692f6321670e0c5.png)

You can config what you need to use Casdoor config

![casdoor_faillogin](data:image/png;base64,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)

![casdoor_login](assets/images/casdoor-login-a3f60223d82325df9f22d48084074985_aa89210b36d4fb7d.png)
![casdoor_successlogin](data:image/png;base64,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)

![casdoor_token](assets/images/casdoor-token-e317f35a2028635bc978ad9261e3e384_128fef60c9cf4af8.png)

---

<a id="plugin-center-security-cryptor-request-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/security/cryptor-request-plugin/ -->

<!-- page_index: 83 -->

# CryptorRequest plugin

Version: 2.7.0.3

- The `cryptorRequest` plugin uses `fieldNames` to match the parameters in `requestBody` for `decryption` processing, replacing the current `requestBody` content.

1. In `shenyu-admin` BasicConfig --> plugin -> `cryptor_request` set to enable.

![](assets/images/enable-cryptor-request-plugin_0161270b23a062f6.png)

2. Open `selector` to configure the traffic that needs to be matched.
3. Open the `Rules` configuration corresponding to the `selector`.

![](assets/images/cryptor-request-rules-config_7c5464edd11b6691.png)

- strategyName: Algorithm name. Currently, based on shenyu's SPI mechanism, the encryption and decryption algorithms can be customized,
  Need to implement the `org.apache.shenyu.plugin.cryptor.strategy.CryptorStrategy` interface.

  At the same time find the `org.apache.shenyu.plugin.cryptor.strategy.CryptorStrategy` file under `resources/META-INF/shenyu/`,
  Write the name of the algorithm, and the package name of the class that implements the `CryptorStrategy` interface.
- fieldNames: Matching parameter name. Support parsing multi-level json format matching, using `.` segmentation, such as data.id.

```json5
        { 
          data: { 
            "id": "" 
          }   
        } 
```

- decryptKey: Secret key. Used to decrypt data.
- encryptKey: Secret key. Used to encrypt data.
- way: Select encrypt or decrypt.

- Add support for `cryptorRequest` in the `pom.xml` file of shenyu-bootstrap.

```xml
<!-- apache shenyu Cryptor Request plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-cryptor</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu Cryptor Request plugin end--> 
```

Prevent Internet hacking and obtain data maliciously. Improve data security.

---

<a id="plugin-center-security-cryptor-response-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/security/cryptor-response-plugin/ -->

<!-- page_index: 84 -->

# CryptorResponse plugin

Version: 2.7.0.3

- The `CryptorResponse` plug-in uses `fieldNames` to match the parameters in `responseBody` for `encryption` processing, replacing the corresponding content of the current `fieldNames`.

1. In `shenyu-admin` BasicConfig --> plugin -> `cryptor_response` set to enable.

![](assets/images/enable-cryptor-response-plugin_fb5cde32809fd7d3.png)

2. Open `selector` to configure the traffic that needs to be matched.
3. Open the `Rules` configuration corresponding to the `selector`.

![](assets/images/cryptor-response-rules-config_1f052a674c3df6ea.png)

- strategyName: Algorithm name. Currently, based on shenyu's SPI mechanism, the encryption and decryption algorithms can be customized,
  Need to implement the `org.apache.shenyu.plugin.cryptor.strategy.CryptorStrategy` interface.

  At the same time find the `org.apache.shenyu.plugin.cryptor.strategy.CryptorStrategy` file under `resources/META-INF/shenyu/`,
  Write the name of the algorithm, and the package name of the class that implements the `CryptorStrategy` interface.
- fieldNames: Matching parameter name. Support parsing multi-level json format matching, using `.` segmentation, such as data.id.

```json5
    { 
      data: { 
        "id": "" 
      } 
    } 
```

- decryptKey: Secret key. Used to decrypt data.
- encryptKey: Secret key. Used to encrypt data.
- way: Select encrypt or decrypt.

- Add support for `cryptorResponse` in the `pom.xml` file of shenyu-bootstrap.

```xml
<!-- apache shenyu Cryptor Response plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-cryptor</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu Cryptor Response plugin end--> 
```

Prevent Internet hacking and obtain data maliciously. Improve data security.

---

<a id="plugin-center-security-jwt-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/security/jwt-plugin/ -->

<!-- page_index: 85 -->

# 1. Overview

Version: 2.7.0.3

- `jwt` plugin

- Requires unified authentication by jwt at the gateway.

- The `jwt` plug-in is for the `token` attribute or `authorization` of the http request header to carry the attribute value for authentication judgment and judge `OAuth2.0` .

- Core module is `shenyu-plugin-jwt`.
- Core class is `org.apache.shenyu.plugin.jwt.JwtPlugin`.

- Since ShenYu 2.4.0

<a id="plugin-center-security-jwt-plugin--2.how-to-use-plugin"></a>

# 2.How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-jwt</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- In shenyu-admin --> BasicConfig --> Plugin --> jwt set Status enable.

- Config secretKey of jwt-plugin in shenyu-admin, the secretKey must more than 256 bit.
- `secretKey`: The private key when using `jwt` to generate `token`, it is required.

![](assets/images/jwt-plugin-config-en-41fdb635e52370b6882c09741a0c29aa_0b9d415f9fab8649.jpg)

- Selector and rule Config. Please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).

![](assets/images/jwt-plugin-rule-handle-en-3efcc377c242e0047edd129a535d50d5_dedf9e2723b2475c.jpg)

- convert means jwt converter
- jwtVal: jwt of body name
- headerVal: jwt header name

custom covert algorithm：[custom-jwt-covert-algorithm](#developer-custom-jwt-covert-algorithm)

![](assets/images/jwt-plugin-config-en-41fdb635e52370b6882c09741a0c29aa_0b9d415f9fab8649.jpg)

![](assets/images/jwt-plugin-selector-config-en-73506b6e96a35eac7fe268145cebbc3b_42e0ef3891348e5b.jpg)

![](assets/images/jwt-plugin-rule-handle-en-3efcc377c242e0047edd129a535d50d5_dedf9e2723b2475c.jpg)

- You can open `https://jwt.io/` in your browser and fill in the corresponding parameters.
- Config jwt header `HEADER` in `https://jwt.io/`
- Config jwt body `PAYLOAD` in `https://jwt.io/`
- Config jwt signature `VERIFY SIGNATURE` in `https://jwt.io/`

![](assets/images/jwt-web-428e7d369c17035e0daa838740150227_58dfd7c86ffce79e.jpg)

```java
public final class JwtPluginTest { 
     
  public void generateJwtCode() { 
    final String secreteKey = "shenyu-test-shenyu-test-shenyu-test"; 
    Map<String, String> map = new HashMap<>(); 
    map.put("id", "1"); 
    map.put("name", "xiaoming"); 
    Date date = new Date(); 
    date.setTime(1655524800000L); 
    String token = Jwts.builder() 
            .setIssuedAt(date) 
            .setExpiration(new Date()) 
            .setClaims(map) 
            .signWith(Keys.hmacShaKeyFor(secreteKey.getBytes(StandardCharsets.UTF_8)), SignatureAlgorithm.HS256) 
            .compact(); 
    System.out.println(token); 
  } 
} 
```

- request your service with jwt token `token: eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoieGlhb21pbmciLCJpZCI6IjEifQ.LdRzGlB49alhq204chwF7pf3C0z8ZpuowPvoQdJmSRw` in your request header.

- request your service with Authorization `Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJuYW1lIjoieGlhb21pbmciLCJpZCI6IjEifQ.LdRzGlB49alhq204chwF7pf3C0z8ZpuowPvoQdJmSRw` in your request header.

- error token request result

```text
{ 
  "code": 401, 
  "message": "Illegal authorization" 
} 
```

- normal token request result

```text
{ 
  "id": "123", 
  "name": "hello world save order" 
} 
```

<a id="plugin-center-security-jwt-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `jwt` set Status disable.

![](assets/images/jwt-plugin-close-en-47c04e90a85f27746b2a9b3e771de5a9_c24a6f6c72053d30.jpg)

---

<a id="plugin-center-security-oauth2-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/security/oauth2-plugin/ -->

<!-- page_index: 86 -->

# OAuth2 Plugin

Version: 2.7.0.3

The `OAuth2` plugin in Apache Shenyu is implemented using the OAuth2 standard. It allows for secure and authorized access to protected resources on a web server by using a token-based authentication method.

In Apache Shenyu, the OAuth2 plugin acts as the client application, while the authorization server and resource server are typically provided by external services like GitHub, Google, or Facebook. When a user attempts to access a protected resource on the Apache Shenyu server, the OAuth2 plugin redirects the user to the authorization server to request permission to access the resource. The user then logs in to the authorization server and grants permission for the client application (OAuth2 plugin) to access the requested resource on their behalf. The authorization server then sends a token to the client application, which it can use to access the resource server and retrieve the protected resource.

Setting up the OAuth2 Plugin in Apache Shenyu

To configure the OAuth2 plugin in Apache Shenyu, you will need to follow these steps:

- Step 1: Install the OAuth2 Plugin

  First, you need to ensure that the OAuth2 plugin is installed and enabled in Apache Shenyu. If it is not already installed, you can download it from the Shenyu GitHub repository and follow the installation instructions.
- Step 2: Register an OAuth2 Application with the Authorization Server

  Before you can use the OAuth2 plugin in Apache Shenyu, you need to register an OAuth2 application with the authorization server you plan to use (e.g., GitHub, Google, etc.). The registration process typically involves providing basic information about your application, such as the application name, website URL, and redirect URI.

  Once you have registered your OAuth2 application with the authorization server, you will receive a client ID and client secret, which you will need to use in the next step.
- Step 3: Configure the OAuth2 Plugin

  To configure the OAuth2 plugin in Apache Shenyu, you will need to modify the shenyu-server.yaml configuration file. Here's an example of what the configuration might look like:


```text
plugins: 
oauth2: 
  enabled: true 
  client_id: <your_client_id> 
  client_secret: <your_client_secret> 
  authorization_url: <authorization_server_url> 
  token_url: <token_endpoint_url> 
  user_info_url: <user_info_endpoint_url> 
```

  - `enabled`: Set this to `true` to enable the OAuth2 plugin in Shenyu.
  - `client_id` and `client_secret`: These are the client credentials you received when you registered your OAuth2 application with the authorization server.
  - `authorization_url`: This is the URL of the authorization server's authorization endpoint.
  - `token_url`: This is the URL of the authorization server's token endpoint.
  - `user_info_url`: This is the URL of the authorization server's user info endpoint, which is used to retrieve information about the authenticated user.
- Step 4: Test the OAuth2 Plugin

  To test the OAuth2 plugin in Apache Shenyu, you can try to access a protected resource on the Shenyu server that requires authentication. When you attempt to access the resource, the OAuth2 plugin should redirect you to the authorization server's login page. After you log in and grant permission to the client application (OAuth2 plugin), the plugin should be able to retrieve an access token and use it to access the protected resource on your behalf.

---

<a id="plugin-center-security-sign-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/security/sign-plugin/ -->

<!-- page_index: 87 -->

# 1. Overview

Version: 2.7.0.3

- Sign Plugin

- Support http header to authorize
- Support http header and request body to authorize

- Process signature authentication of requests.

- Core Module: `shenyu-plugin-sign`
- Core Class: `org.apache.shenyu.plugin.sign.SignPlugin`

- Since ShenYu 2.4.0

<a id="plugin-center-security-sign-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Introducing `sign` dependency in the `pom.xml` file of the gateway

```xml
<!-- apache shenyu sign plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-sign</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- apache shenyu sign plugin end--> 
```

- In `shenyu-admin`--> BasicConfig --> Plugin --> `sign` set to enable.

- Manage and control the permissions of requests passing through the Apache ShenYu gateway.
- Generate `AK/SK` and use it with the `Sign` plugin to achieve precise authority control based on URI level.

First, we can add a piece of authentication information in `BasicConfig` - `Authentication`

![](assets/images/auth-manages-add-en_8e7a50a81398e08f.jpg)

Then configure this authentication information

![](assets/images/auth-param-en_f3c435b71300b600.jpg)

- AppName：The application name associated with this account, it can can fill in or choose (data comes from the application name configured in the Metadata).
- TelPhone：Telphone information.
- AppParams：When the requested context path is the same as the AppName，add this value to the header, the key is `appParam`.
- UserId：Give the user a name, just as an information record.
- ExpandInfo：Description of the account.
- PathAuth：After opening, the account only allows access to the resource path configured below.
- ResourcePath：Allow access to the resource path, support path matching，e.g. `/order/**` .

After submit, a piece of authentication information is generated, which contains `AppKey` and `AppSecret`, which is the `AK/SK` in the `Sign` plugin.

Please refer to the detailed instructions of the `Sign` plugin： [Sign Plugin](#plugin-center-security-sign-plugin).

For the created authentication information, you can click `PathOperation` at the end of a piece of authentication information.

![](assets/images/auth-manage-modifypath-en_780cfc90b1931cc7.jpg)

- On the left is a list of configurable paths, and on the right is a list of paths that allow the account to access.
- Check the resource path, click the `>` or `<` in the middle to move the checked data to the corresponding list.
- In the list of configurable paths on the left, click "Editor" at the end of the account information line, and add them in the "Resource Path" in the pop-up box.

- Adopt `AK/SK` authentication technical scheme.
- Adopt authentication plug-in and Chain of Responsibility Pattern to realize.
- Take effect when the authentication plugin is enabled and all interfaces are configured for authentication.

- Step 1: `AK/SK` is assigned by the gateway. For example, the `AK` assigned to you is: `1TEST123456781` SK is: ` 506eeb535cf740d7a755cb49f4a1536'
- Step 2: Decide the gateway path you want to access, such as `/api/service/abc`
- Step 3: Construct parameters (the following are general parameters)

| Field | Value | Description |
| --- | --- | --- |
| timestamp | current timestamp(String) | The number of milliseconds of the current time（gateway will filter requests the before 5 minutes） |
| path | /api/service/abc | The path that you want to request(Modify by yourself according to your configuration of gateway) |
| version | 1.0.0 | `1.0.0` is a fixed string value |

Sort the above three field natually according to the key, then splice fields and fields, finally splice SK. The following is a code example.

Step 1: First, construct a Map.

```java
 
   Map<String, String> map = Maps.newHashMapWithExpectedSize(3); 
   //timestamp is string format of millisecond. String.valueOf(LocalDateTime.now().toInstant(ZoneOffset.of("+8")).toEpochMilli()) 
   map.put("timestamp","1571711067186");  // Value should be string format of milliseconds 
   map.put("path", "/api/service/abc"); 
   map.put("version", "1.0.0"); 
```

Step 2: Sort the `Keys` naturally, then splice the key and values, and finally splice the `SK` assigned to you.

```java
List<String> storedKeys = Arrays.stream(map.keySet() 
                .toArray(new String[]{})) 
                .sorted(Comparator.naturalOrder()) 
                .collect(Collectors.toList()); 
final String sign = storedKeys.stream() 
                .map(key -> String.join("", key, map.get(key))) 
                .collect(Collectors.joining()).trim() 
                .concat("506EEB535CF740D7A755CB4B9F4A1536"); 
```

- The returned sign value should be:`path/api/service/abctimestamp1571711067186version1.0.0506EEB535CF740D7A755CB4B9F4A1536`

Step 3: Md5 encryption and then capitalization.

```java
DigestUtils.md5DigestAsHex(sign.getBytes()).toUpperCase() 
```

- The final returned value is: `A021BF82BE342668B78CD9ADE593D683`.

Step 1: First, construct a Map, and the map must save every request body parameters

```java
 
   Map<String, String> map = Maps.newHashMapWithExpectedSize(3); 
   //timestamp is string format of millisecond. String.valueOf(LocalDateTime.now().toInstant(ZoneOffset.of("+8")).toEpochMilli()) 
   map.put("timestamp","1660659201000");  // Value should be string format of milliseconds 
   map.put("path", "/http/order/save"); 
   map.put("version", "1.0.0"); 
   // if your request body is:{"id":123,"name":"order"} 
   map.put("id", "1"); 
   map.put("name", "order") 
```

Step 2: Sort the `Keys` naturally, then splice the key and values, and finally splice the `SK` assigned to you.

```java
List<String> storedKeys = Arrays.stream(map.keySet() 
                .toArray(new String[]{})) 
                .sorted(Comparator.naturalOrder()) 
                .collect(Collectors.toList()); 
final String sign = storedKeys.stream() 
                .map(key -> String.join("", key, map.get(key))) 
                .collect(Collectors.joining()).trim() 
                .concat("2D47C325AE5B4A4C926C23FD4395C719"); 
```

- The returned sign value should be:`id123nameorderpath/http/order/savetimestamp1660659201000version1.0.02D47C325AE5B4A4C926C23FD4395C719`

Step 3: Md5 encryption and then capitalization.

```java
DigestUtils.md5DigestAsHex(sign.getBytes()).toUpperCase() 
```

- The final returned value is: `35FE61C21F73E9AAFC46954C14F299D7`.

- If your visited path is:`/api/service/abc`.
- Address: http: domain name of gateway `/api/service/abc`.
- Set `header`，`header` Parameter：

| Field | Value | Description |
| --- | --- | --- |
| timestamp | `1571711067186` | Timestamp when signing |
| appKey | `1TEST123456781` | The AK value assigned to you |
| sign | `A90E66763793BDBC817CF3B52AAAC041` | The signature obtained above |
| version | `1.0.0` | `1.0.0` is a fixed value. |

- The signature plugin will filter requests before `5` minutes by default
- If the authentication fails, will return code `401`, message may change.

```json
{ 
  "code": 401, 
  "message": "sign is not pass,Please check you sign algorithm!", 
  "data": null 
} 
```

![](assets/images/sign-open-en-7a1bcfbe89eec35490eec64c037a7103_1267c9969c6d4eea.jpg)

![](assets/images/selector-en-993bda66883505a34953d527663d7475_229afccbc3f8cb64.png)

- Only those matched requests can be authenticated by signature.
- Selectors and rules, please refer to: [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule)

![](assets/images/rule-en-66585f6eca8f875a4a6e1fd5c65646d1_b975b884a3b996bf.png)

- close(signRequestBody): generate signature with request header.
- open(signRequestBody): generate signature with request header and request body.

This authentication algorithm is the version 2.0.0 algorithm, which is same as version1's except **Authentication Guide** and **Request GateWay.**

Authentication algorithm of Version 2.0.0 generates a Token based on the signature algorithm, and puts the Token value into the request header `ShenYu-Authorization` parameter when sending a request. To distinguish it from version 1.0.0, the `version` parameter of the request header is left, which is 2.0.0.

- Step 1: `AK/SK` is assigned by the gateway. For example, the `AK` assigned to you is: `1TEST123456781` SK is: ` 506eeb535cf740d7a755cb49f4a1536'
- Step 2: Decide the gateway path you want to access, such as `/api/service/abc`

- build parameter

  build the `parameters` that is json string


```json
{ 
    "alg":"MD5", 
    "appKey":"506EEB535CF740D7A755CB4B9F4A1536", 
    "timestamp":"1571711067186" 
} 
```

  **alg**: signature algorithm（result is uppercase HEX string）

  - MD5: MD5-HASH(data+key)
  - HMD5:HMAC-MD5
  - HS256:HMAC-SHA-256
  - HS512:HMAC-SHA-512

  **appKey**：appKey

  **timestamp**: timestamp of the length is 13
- Calculate signature value


```tex
signature = sign( 
  base64Encoding(parameters) + Relative URL + Body*, 
  secret 
); 
* indicate Optional , it depends on handler config 
Relative URL = path [ "?" query ] eg: /apache/shenyu/pulls?name=jack 
```

  > note :`Relative URL` is not include fragment
- Calculate Token

  > token = base64Encoding(parameters) + '.' + base64Encoding(signature)

  Put the Token into the request header `ShenYu-Authorization` parameter.

| Field | 值 | 描述 |
| --- | --- | --- |
| ShenYu-Authorization | Token | Token |
| version | `2.0.0` | Fixed value |

> please change the Authorization field to ShenYu-Authorization as soon as possible to avoid conflicts with application Authorization.

![](assets/images/sign-open-en-7a1bcfbe89eec35490eec64c037a7103_1267c9969c6d4eea.jpg)

![](assets/images/example-selector-en-5f344f0f789b9b37e2ddefe245149eaf_d720c578674cff47.png)

![](assets/images/example-rule-en-503e8b5697e5aada40d67b999ce281c7_cfe92296bffba557.png)

![](assets/images/example-sign-auth-en-7531558c55916cf987b149f58a336d16_c26f6e969db549e6.png)

- build request params with `Authentication Guide`,

```java
public class Test1 { 
  public static void main(String[] args) { 
    Map<String, String> map = Maps.newHashMapWithExpectedSize(3); 
    //timestamp为毫秒数的字符串形式 String.valueOf(LocalDateTime.now().toInstant(ZoneOffset.of("+8")).toEpochMilli()) 
    map.put("timestamp","1660658725000");  //值应该为毫秒数的字符串形式 
    map.put("path", "/http/order/save"); 
    map.put("version", "1.0.0"); 
    map.put("id", "123"); 
    map.put("name", "order"); 
    // map.put("body", "{\"id\":123,\"name\":\"order\"}"); 
 
    List<String> storedKeys = Arrays.stream(map.keySet() 
                    .toArray(new String[]{})) 
            .sorted(Comparator.naturalOrder()) 
            .collect(Collectors.toList()); 
    final String sign = storedKeys.stream() 
            .map(key -> String.join("", key, map.get(key))) 
            .collect(Collectors.joining()).trim() 
            .concat("2D47C325AE5B4A4C926C23FD4395C719"); 
    System.out.println(sign); 
 
    System.out.println(DigestUtils.md5DigestAsHex(sign.getBytes()).toUpperCase()); 
  } 
} 
```

- signature without body: `path/http/order/savetimestamp1571711067186version1.0.02D47C325AE5B4A4C926C23FD4395C719`
- sign without body result is: `9696D3E549A6AEBE763CCC2C7952DDC1`

![](assets/images/result-1c40210c3da55750298242b3b037f289_a71d77ed5cb921b8.png)

```java
public class Test2 { 
  public static void main(String[] args) { 
    Map<String, String> map = Maps.newHashMapWithExpectedSize(3); 
    //timestamp为毫秒数的字符串形式 String.valueOf(LocalDateTime.now().toInstant(ZoneOffset.of("+8")).toEpochMilli()) 
    map.put("timestamp","1660659201000");  //值应该为毫秒数的字符串形式 
    map.put("path", "/http/order/save"); 
    map.put("version", "1.0.0"); 
 
    List<String> storedKeys = Arrays.stream(map.keySet() 
                    .toArray(new String[]{})) 
            .sorted(Comparator.naturalOrder()) 
            .collect(Collectors.toList()); 
    final String sign = storedKeys.stream() 
            .map(key -> String.join("", key, map.get(key))) 
            .collect(Collectors.joining()).trim() 
            .concat("2D47C325AE5B4A4C926C23FD4395C719"); 
    System.out.println(sign); 
 
    System.out.println(DigestUtils.md5DigestAsHex(sign.getBytes()).toUpperCase()); 
  } 
} 
```

\*signature with body:`id123nameorderpath/http/order/savetimestamp1660659201000version1.0.02D47C325AE5B4A4C926C23FD4395C719`
\*sign with body result is:`35FE61C21F73E9AAFC46954C14F299D7`

![](assets/images/result-with-body-d430bbcc77fef2c8bdd89cace7d6e418_aca985b53523ae27.png)

All the configuration parts are the same, so let's look directly at the the calculation part of parameter of request header and the part of sending request.

- implements the algorithm

  Suppose we use a signature algorithm named MD5. According to the previous description, the signature value is to concatenate the data and key, and then hash.


```java
private static String sign(final String signKey, final String base64Parameters, final URI uri, final String body) {
String data = base64Parameters + getRelativeURL(uri) + Optional.ofNullable(body).orElse("");
return DigestUtils.md5Hex(data+signKey).toUpperCase();}
private static String getRelativeURL(final URI uri) {if (Objects.isNull(uri.getQuery())) {return uri.getPath();} return uri.getPath() + "?" + uri.getQuery();}
```

- verify without the request body


```java
public static void main(String[] args) { 
     
    String appSecret = "2D47C325AE5B4A4C926C23FD4395C719"; 
 
    URI uri = URI.create("/http/order/save"); 
 
    String parameters = JsonUtils.toJson(ImmutableMap.of( 
        "alg","MD5", 
        "appKey","BD7980F5688A4DE6BCF1B5327FE07F5C", 
        "timestamp","1673708353996")); 
 
    String base64Parameters = Base64.getEncoder() 
        .encodeToString(parameters.getBytes(StandardCharsets.UTF_8)); 
 
    String signature = sign(appSecret,base64Parameters,uri,null); 
 
    String Token = base64Parameters+"."+signature; 
 
    System.out.println(Token); 
 
} 
```

  Token:


```tex
eyJhbGciOiJNRDUiLCJhcHBLZXkiOiJCRDc5ODBGNTY4OEE0REU2QkNGMUI1MzI3RkUwN0Y1QyIsInRpbWVzdGFtcCI6IjE2NzM3MDgzNTM5OTYifQ==.33ED53DF79CA5B53C0BF2448B670AF35 
```

  发送请求：

  ![image-20230114230500887](assets/images/version2-sign-request-07e41df7117f83bea75f60631e3c7ec1_1cba6f79d75ae752.png)
- verify with the request body

```java
    public static void main(String[] args) { 
        String appSecret = "2D47C325AE5B4A4C926C23FD4395C719"; 
 
        URI uri = URI.create("/http/order/save"); 
 
        String parameters = JsonUtils.toJson(ImmutableMap.of( 
                "alg","MD5", 
                "appKey","BD7980F5688A4DE6BCF1B5327FE07F5C", 
                "timestamp","1673708905488")); 
 
        String base64Parameters = Base64.getEncoder() 
                .encodeToString(parameters.getBytes(StandardCharsets.UTF_8)); 
 
        String requestBody = "{\"id\":123,\"name\":\"order\"}"; 
 
        String signature = sign(appSecret,base64Parameters,uri,requestBody); 
 
        String Token = base64Parameters+"."+signature; 
 
        System.out.println(Token); 
 
    } 
```

Token:

```tex
eyJhbGciOiJNRDUiLCJhcHBLZXkiOiJCRDc5ODBGNTY4OEE0REU2QkNGMUI1MzI3RkUwN0Y1QyIsInRpbWVzdGFtcCI6IjE2NzM3MDg5MDU0ODgifQ==.FBCEB6D816644A98378635050AB85EF1 
```

![image-20230114231032837](assets/images/request-body-1fa3cc7c11fa0dff45216ec5e90c34cd_29647d4af6c9151b.png)

![image-20230114230922598](assets/images/version2-sign-request-with-body-1823973903b2b06403e1bda8fda9de15_6f12c86d38569ce1.png)

<a id="plugin-center-security-sign-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin`--> BasicConfig --> Plugin --> `sign` set to disabled.

<a id="plugin-center-security-sign-plugin--4.-extension"></a>

# 4. Extension

- Please refer to: [dev-sign](#developer-custom-sign-algorithm).

---

<a id="plugin-center-security-waf-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/security/waf-plugin/ -->

<!-- page_index: 88 -->

# Waf Plugin

Version: 2.7.0.3

- `Waf` is the core implementation of gateway to realize firewall function for network traffic.

Please refer to the `deployment` document, choose a way to start `shenyu-admin`. For example, through [Local Deployment](#deployment-deployment-local) to start the `Apache ShenYu` management system.

- In `shenyu-admin` BasicConfig --> plugin -> `waf` set to enable.If you don't want to use this function, please disable this plugin in the `shenyu-admin`.

  ![](assets/images/waf-open-en_970c1d8161b6f61f.jpg)
- Add configuration mode in plugin editing.

```yaml
{"model":"black"} 
# model can be 'black' or 'mixed' 
# The default mode is blacklist mode; If setting is mixed, it will be mixed mode. We will explain it specifically below. 
```

- Introducing `waf` dependency in the pom.xml of the gateway.

```xml
  <!-- apache shenyu waf plugin start--> 
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-plugin-waf</artifactId> 
      <version>${project.version}</version> 
  </dependency> 
  <!-- apache shenyu waf plugin end--> 
```

For more instructions on selector and rule configuration, please refer to: [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule), here only some fields are introduced.

`Waf` plugin rule configuration page:

![](assets/images/waf-rule-en_9927f64ff40d07e4.jpg)

For requests that are denied access by `Waf` , the response header status code is: `403`.

- When `model` is set to `black` mode, only the matched traffic will execute the rejection policy, and the unmatched traffic will be skipped directly.
- The `Handler` feild in the rule configuration is invalid and can be configured to be empty.

- When `model` is set to `mixed` mode, all traffic will pass through waf plugin. For different matching traffic, users can set whether to reject or pass.
- The `Handler` feild in the rule configuration must be configured:

  - `permission`: The handle logic that matches the rule. `reject`: deny access, `allow`: allow access.
  - `statusCode`: When access is denied, the value of the code field in the response body. `Will not modify the status code of the response header`.

    e.g.：`statusCode=10001`，The rejected response body is :


```json
{"code":10001,"message":"You are forbidden to visit"} 
```

- `Waf` is also the pre-plugin of `ShenYu`, which is mainly used to intercept illegal requests or exception requests and give relevant rejection policies.
- When faced with replay attacks, you can intercept illegal `ip` and `host`, and set reject strategy according to matched `ip` or `host`.
- How to determine `ip` and `host`, please refer to: [parsing-ip-and-host](#developer-custom-parsing-ip-and-host)

---

<a id="plugin-center-observability-logging-aliyun-sls"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-aliyun-sls/ -->

<!-- page_index: 89 -->

# 1. Overview

Version: 2.7.0.3

- Logging-AliyunSls Plugin

- collect http request information to aliyun sls, analysis request information by aliyun sls platform.

- The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，
- the plugin records access logs and sends to aliyun sls platform.

- Core Module `shenyu-plugin-logging-aliyun-sls`
- Core Class `org.apache.shenyu.plugin.aliyun.sls.LoggingAliYunSlsPlugin`
- Core Class `org.apache.shenyu.plugin.aliyun.sls.client.AliyunSlsLogCollectClient`

ShenYu 2.5.0

<a id="plugin-center-observability-logging-aliyun-sls--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
<!-- shenyu logging-aliyunsls plugin start --> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-logging-aliyun-sls</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- shenyu logging-aliyunsls plugin end --> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingAliyunSls` set Status enable.

![](assets/images/plugin-config-en-9d0d7b720199c059009e104e95e30ad7_f94095b1b997662e.jpg)

| config-item | type | description | remarks |
| --- | --- | --- | --- |
| accessId | String | accessId | must |
| accesskey | String | accesskey | must |
| host | String | host name, example:cn-guangzhou.log.aliyuncs.com | must |
| projectName | String | log project name | optional, default shenyu |
| logStoreName | String | log store name | optional, default shenyu-logstore |
| topic | String | aliyun sls log topic | optional, default shenyu-topic |
| ttlInDay | Integer | ttl times in one day | optional, default 3 |
| shardCount | Integer | aliyun sls log shard count | optional, default 10 |
| sendThreadCount | Integer | send log to aliyun sls thread number | optional, default 1 |
| ioThreadCount | Integer | io thread count | optional, default 1 |
| sampleRate | String | sample consume rate | optional, default 1 |
| maxRequestBody | Integer | max request body | optional, default 524288 |
| maxResponseBody | Integer | max response body | optional, default 524288 |
| bufferQueueSize | Integer | consume log queue size | optional, default 50000 |

- Selector and rule Config. Please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).

collect request info as follows

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

- Open the plugin and configure aliyun-sls, configure it as follows.

![](assets/images/plugin-config-en-9d0d7b720199c059009e104e95e30ad7_f94095b1b997662e.jpg)

![](assets/images/aliyun-sls-log-selector-en-7f6d52e5e558b7df430acca33e9a7c05_f99a0f5ddbc80b82.png)

![](assets/images/aliyun-sls-log-rule-en-1ab20149d1a9e4289b54145fb1ea194a_9501d535690436d9.png)

![](assets/images/call-service-ceeafb89bf58792af70883bdaedbcb93_c3e030552a6c5dce.png)

![](assets/images/aliyun-sls-log-ec218ef357112103ac1189111b661eb0_b88ce0a4e5bb1c84.jpg)

<a id="plugin-center-observability-logging-aliyun-sls--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingAliyunSls` set Status disable.

---

<a id="plugin-center-observability-logging-elasticsearch"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-elasticsearch/ -->

<!-- page_index: 90 -->

# 1. Overview

Version: 2.7.0.3

- Logging-ElasticSearch Plugin

- collect http request info to elasticsearch, query or display request info by another application(kibana).

> `Apache ShenYu` The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，
> The list includes: request time, request parameters, request path, response result, response status code, time consumption, upstream IP, exception information waiting.
> Shenyu gateway can record access logs through logging-elasticsearch-plugin and send access logs to elasticsearch database.

- Core Module `shenyu-plugin-logging-elasticsearch`
- Core Class `org.apache.shenyu.plugin.logging.elasticsearch.LoggingElasticSearchPlugin`
- Core Class `org.apache.shenyu.plugin.logging.elasticsearch.client.ElasticSearchLogCollectClient`

- Since 2.5.0

- Architecture Diagram

![](assets/images/logging-elasticsearch-arch-dcee306a7551430f19c4da0be6a8b8b8_62a590d9ac453e5b.png)

<a id="plugin-center-observability-logging-elasticsearch--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Add the dependency of logging-elasticsearch to the Shenyu-bootstrap-module 's `pom.xml` file.

```xml
 <!--shenyu logging-elasticsearch plugin start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-logging-elasticsearch</artifactId> 
    <version>${project.version}</version> 
</dependency> 
<!--shenyu logging-elasticsearch plugin end--> 
```

- In `shenyu-admin` --> Basic Configuration --> Plugin Management --> `loggingElasticSearch`, configure the ElasticSearch parameter and set it to on.

![](assets/images/logging-elasticsearch-config-en-c91dd7924f5890897c59e2671cd9b3a9_dafa8e9b28e05684.png)

- The individual configuration items are described as follows:

| config-item | type | description | remarks |
| --- | --- | --- | --- |
| host | String | host name | must |
| port | String | port num | must |
| sampleRate | String | Sampling rate, range 0~1, 0: off, 0.01: acquisition 1%, 1: acquisition 100% | Optional, default 1, all collection |
| compressAlg | String | Compression algorithm, no compression by default, currently supports LZ4 compression | Optional, no compression by default |
| maxResponseBody | Ingeter | Maximum response size, above the threshold no response will be collected | Optional, default 512KB |
| maxRequestBody | Ingeter | Maximum request body size, above the threshold no request body will be collected | Optional, default 512KB |
| Except for host, port, all others are optional, in most cases only these 3 items need to be configured. |  |  |  |

For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。
In addition sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:

![](assets/images/logging-elasticsearch-option-24daaa3dc1d8e0efdb8d31b6ebdb5749_d5db7a08fc8e4a01.png)

The fields of the captured access log are as follows.

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

Users need to deploy the `ElasticSearch` service to collect

- To [download address](https://www.elastic.co/downloads/elasticsearch) Select Windows version to download
- After downloading the installation package, unzip it, enter the `bin` directory, and double-click to execute `elasticsearch.bat` to start
- The default startup port is `9200`. Access`http://localhost:9200`, verify success

![](data:image/png;base64,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)

- To [download address](https://www.elastic.co/downloads/elasticsearch) Select Windows version to download
- After downloading the installation package, unzip it, enter the `bin` directory and execute the startup command on the terminal: `./elasticsearch`
- The default startup port is `9200`. Access `http://localhost:9200`, verify success

![](data:image/png;base64,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)

- To [download address](https://www.elastic.co/cn/downloads/kibana) Select Windows version to download
- After downloading the installation package, unzip it, enter the `bin` directory, and double-click to execute `kibana.bat` to start
- The default startup port is `5601`. Access `http://localhost:5601`, verify success

![](data:image/png;base64,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)

- To [download address](https://www.elastic.co/cn/downloads/kibana) Select Windows version to download
- After downloading the installation package, unzip it, enter the `bin` directory and execute the startup command on the terminal: `./kibana`
- The default startup port is `5601`. Access `http://localhost:5601`, verify success

![](data:image/png;base64,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)

![](assets/images/logging-elasticsearch-config-en-c91dd7924f5890897c59e2671cd9b3a9_dafa8e9b28e05684.png)

- For detailed configuration of selectors and rules, please refer to:[Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

![](assets/images/postman-request-1adbf718cb54cbffd218415fa99b684b_ccce5e2b53cfc646.png)

![](assets/images/index-6dc305bb6f2cad48a6bf3881e430304a_a513f700a679b9af.png)

- The first time you use the plug-in, you will automatically create a `shenyu-access-logging` index

![](assets/images/data-20751809e7350746e6d9942ac4bdd9c4_a5b28fe5ffe46a2c.png)

- Using ES query statement, the requested log information can be queried

<a id="plugin-center-observability-logging-elasticsearch--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `LoggingElasticSearch` set Status disable.

---

<a id="plugin-center-observability-logging-huawei-lts"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-huawei-lts/ -->

<!-- page_index: 91 -->

# 1. Overview

Version: 2.7.0.3

- Logging-HuaweiLts Plugin

- collect http request information to huawei lts, analysis request information by huawei lts platform.

- The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，

- the plugin records access logs and sends to huawei lts platform.

- Core Module `shenyu-plugin-logging-huawei-lts`
- Core Class `org.apache.shenyu.plugin.huawei.lts.LoggingHuaweiLtsPlugin`
- Core Class `org.apache.shenyu.plugin.huawei.lts.client.HuaweiLtsLogCollectClient`

ShenYu 2.6.0

<a id="plugin-center-observability-logging-huawei-lts--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- - import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
<!-- shenyu logging-huaweilts plugin start --> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-logging-huawei-lts</artifactId> 
    <version>${project.version}</version> 
</dependency> 
<!-- shenyu logging-huaweilts plugin end --> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingHuaweiLts` set Status enable.

###

| config-item | description | type | remarks |
| --- | --- | --- | --- |
| projectId | The project ID of the HUAWEI CLOUD account（project id） | String | must |
| accessKeyId | AK of the HUAWEI CLOUD account | String | must |
| accessKeySecret | SK of HUAWEI CLOUD account | String | must |
| regionName | Regions of Cloud Log Service | String | must |
| logGroupId | The log group ID of the LTS | String | must |
| logStreamId | The log stream ID of the LTS | String | must |
| totalSizeInBytes | The upper limit of the log size that can be cached by a single producer instance | int | optional |
| maxBlockMs | If the producer has insufficient free space, the caller's maximum block time on the send method, in milliseconds. The default is 60 seconds (60000 milliseconds), and 0 seconds is recommended. When the maxBlockMs value >= 0, it will block until the set time. If the blocking time is reached, the memory cannot be obtained, that is, an error will be reported and the log will be discarded. When the value of maxBlockMs=-1, it will be blocked until the sending is successful, and the log will not be discarded | long | optional |
| ioThreadCount | The thread pool size for executing log sending tasks | int | optional |
| batchSizeThresholdInBytes | When the cached log size in a ProducerBatch is greater than or equal to batchSizeThresholdInBytes, the batch will be sent | int | optional |
| batchCountThreshold | When the number of cached logs in a ProducerBatch is greater than or equal to batchCountThreshold, the batch will be sent | int | optional |
| lingerMs | The lingering time of a ProducerBatch from creation until it is sendable | int | optional |
| retries | If a ProducerBatch fails to send for the first time, the number of times it can be retried is recommended to be 3 times. If retries is less than or equal to 0, the ProducerBatch will directly enter the failure queue after the first sending failure | int | optional |
| baseRetryBackoffMs | The backoff time for the first retry | long | optional |
| maxRetryBackoffMs | Maximum backoff time for retries | long | optional |
| giveUpExtraLongSingleLog | For logs exceeding 1M, the data larger than 1M will be discarded after splitting | boolean | optional |
| enableLocalTest | 是否开启跨云上报日志 | boolean | optional |

- get `regionName`

![](assets/images/huawei-lts-regionname-be9173dc5e3388f228d702a27685393f_1836fdaf4facc24a.png)

| **区域名称** | **RegionName** |
| --- | --- |
| 华北-北京二 | cn-north-2 |
| 华北-北京四 | cn-north-4 |
| 华北-北京一 | cn-north-1 |
| 华东-上海二 | cn-east-2 |
| 华东-上海一 | cn-east-3 |
| 华南-广州 | cn-south-1 |
| 华南-深圳 | cn-south-2 |
| 西南-贵阳一 | cn-southwest-2 |

- get `projectId`

![](assets/images/huawei-lts-projectid-e1782f387d5a90f1bd59d7d8985e8fed_f932b4508537ce42.png)

- get `accessKeyId` and `accessKeySecret`

![](assets/images/huawei-lts-access-21854a21f1fa9ec0f1c6e1276e604f3b_12940d8b51128048.png)

- get `logGroupId` and `logStreamId`

![](assets/images/huawei-lts-loggroupid-71c2d0667cf39674ddc189f77ec78db9_fb38664f1013c34e.png)

![](assets/images/huawei-lts-logstreamid-5f509d5b340b6fb8ff101fb12448c32f_645a5cef8dd816e1.png)

- Selector and rule Config. Please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).

collect request info as follows

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

- Open the plugin and configure huawei lts, configure it as follows.

![](assets/images/plugin-config-en-5912fd3fb201b9e76bbdea8d8516d985_e5ed9f79ff53f543.png)

![](assets/images/huawei-lts-log-selector-en-c3e5234a112022d68472ca48abefb667_585f1d1292e2f8d6.png)

![](assets/images/huawei-lts-log-rule-en-15c3693a08401d9f4b8e3a6c0f8ea71c_eb1fa9807f4cb78f.png)

![](assets/images/call-service-f861b37db3fcb62580c41f9e613c26c6_b652ff9ff6e9d765.png)

![](assets/images/huawei-lts-log-741297040fca951dab0ca0379ed7b2d7_0d7c1f77af8dec4a.png)

<a id="plugin-center-observability-logging-huawei-lts--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin -->`loggingHuaweiLts`set Status disable.

---

<a id="plugin-center-observability-logging-kafka"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-kafka/ -->

<!-- page_index: 92 -->

# 1. Overview

Version: 2.7.0.3

- Logging-Kafka Plugin

- collect http request log to Kafka, consume Kafka message to another application and analysis.

> `Apache ShenYu` The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，
> The list includes: request time, request parameters, request path, response result, response status code, time consumption, upstream IP, exception information waiting.
> The Logging-Kafka plugin is a plugin that records access logs and sends them to the Kafka cluster.

- Core Module `shenyu-plugin-logging-kafka`.
- Core Class `org.apache.shenyu.plugin.logging.kafka.LoggingKafkaPlugin`
- Core Claas `org.apache.shenyu.plugin.logging.kafka.client.KafkaLogCollectClient`

- Since ShenYu 2.5.0

- Architecture Diagram

![](assets/images/logging-kafka-arch-86d15893445535929a2c02c5c9f2d181_38ccde1059539343.jpg)

- Full asynchronous collection and delivery of `Logging` inside the `Apache ShenYu` gateway
- Logging platform by consuming the logs in the `Kafka` cluster for repository, and then using `Grafana`, `Kibana` or other visualization platform to display

<a id="plugin-center-observability-logging-kafka--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/loggingconsole-use-en-64a3c389309209c07d4ae4602e0e3895_8ed42c6f5a315126.png)

- Add the `Logging-Kafka` dependency to the gateway's `pom.xml` file.

```xml
<!--shenyu logging-kafka plugin start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-logging-kafka</artifactId> 
    <version>${project.version}</version> 
</dependency> 
<!--shenyu logging-kafka plugin end--> 
```

- In `shenyu-admin` --> Basic Configuration --> Plugin Management --> `loggingKafka`, configure the kafka parameter and set it to on.

![](assets/images/logging-config-en-2d08ddb2fde45effd73f6de8dcf9677c_76b13204f006e046.png)

- The individual configuration items are described as follows:

| config-item | type | description | remarks |
| --- | --- | --- | --- |
| topic | String | Message Queue Topics | must |
| namesrvAddr | String | Message queue nameserver address | must |
| sampleRate | String | Sampling rate, range 0~1, 0: off, 0.01: acquisition 1%, 1: acquisition 100% | Optional, default 1, all collection |
| compressAlg | String | Compression algorithm, no compression by default, currently supports LZ4 compression | Optional, no compression by default |
| maxResponseBody | Ingeter | Maximum response size, above the threshold no response will be collected | Optional, default 512KB |
| maxRequestBody | Ingeter | Maximum request body size, above the threshold no request body will be collected | Optional, default 512KB |
| Except for topic, namesrvAddr, all others are optional, in most cases only these 3 items need to be configured. The default group id is "shenyu-access-logging" |  |  |  |

- For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-config-7d106f4fbe790030983a05d502a4279d_16c424caa6627130.png)

collect request info as follows

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

Open the plugin and configure kafka, configure it as follows.

![](assets/images/logging-config-cn-38036184d6385744163b25162b0fe581_7f2aeca5ca6e163b.png)

For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-option-topic-bea02b4cebee0533b5aa8ddd438d1eb9_83bd658513b1326e.png)

![](assets/images/log-rule-en-ba4ee123192df9f3790a4383c0805c80_bfbbcc174b65f5a0.png)

![](assets/images/call-service-ceeafb89bf58792af70883bdaedbcb93_c3e030552a6c5dce.png)

As each logging platform has differences, such as storage available clickhouse, ElasticSearch, etc., visualization has self-developed or open source Grafana, Kibana, etc..
Logging-Kafka plugin uses Kafka to decouple production and consumption, while outputting logs in json format, consumption and visualization require users to choose different technology stacks to achieve their own situation.=

<a id="plugin-center-observability-logging-kafka--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingKafka` set Status disable.

---

<a id="plugin-center-observability-logging-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-plugin/ -->

<!-- page_index: 93 -->

# 1. Overview

Version: 2.7.0.3

- Logging-Console Plugin

- Users may want to view the information about request(including request headers, request parameters, response headers, response body...etc) where in the side of gateway when debugging during development or troubleshooting problems online.

- Collect http request url, header, request body, response and response body by logback or log4j, the log file will be saved locally.

- Core Module `shenyu-pluign-logging-console`.
- Core Class `org.apache.shenyu.plugin.logging.console.LoggingConsolePlugin`

- Since ShenYu 2.4.0

<a id="plugin-center-observability-logging-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/loggingconsole-use-en-64a3c389309209c07d4ae4602e0e3895_8ed42c6f5a315126.png)

- import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-logging-console</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- In shenyu-admin --> BasicConfig --> Plugin --> loggingConsole set Status enable.

- Selector and rule Config. Please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).

> you must open loggingConsole plugin before you use loggingConsole plugin.

![](assets/images/log-selector-en-cfb6bca5a768524b0300d65eee1947d2_6e5e68c693955a0b.jpg)

![](assets/images/log-rule-en-d09e07905e13a68c6f28941fe2d5a8e1_65b967a927bcc3a1.jpg)

![](assets/images/call-service-ceeafb89bf58792af70883bdaedbcb93_c3e030552a6c5dce.png)

if the request arrived successfully, you will see request information as follow.

```text
Request Uri: http://localhost:9195/test/payment 
Request Method: POST 
 
[Request Headers Start] 
Content-Type: application/json 
Content-Length: 46 
Host: localhost:9195 
Connection: Keep-Alive 
User-Agent: Apache-HttpClient/4.5.13 (Java/11.0.11) 
Cookie: JSESSIONID=CD325CE813F61BB37783A1D0835959DD 
Accept-Encoding: gzip,deflate 
[Request Headers End] 
 
[Request Body Start] 
{ 
  "userId": "11", 
  "userName": "xiaoming" 
} 
[Request Body End] 
 
Response Code: 200 OK 
 
[Response Headers Start] 
transfer-encoding: chunked 
Content-Length: 37 
Content-Type: application/json 
[Response Headers End] 
 
[Response Body Start] 
{"userId":"11","userName":"xiaoming"} 
[Response Body End] 
```

<a id="plugin-center-observability-logging-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingConsole` set Status disable.

![](assets/images/unenable-log-plugin-en-dba4c92e874037084d051575fa90e2e0_7b0121429e995101.jpg)

---

<a id="plugin-center-observability-logging-pulsar"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-pulsar/ -->

<!-- page_index: 94 -->

# 1. Overview

Version: 2.7.0.3

- Logging-Pulsar Plugin

- collect http request log to Pulsar, consume Pulsar message to another application and analysis.

> `Apache ShenYu` The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，
> The list includes: request time, request parameters, request path, response result, response status code, time consumption, upstream IP, exception information waiting.
> The Logging-Pulsar plugin is a plugin that records access logs and sends them to the Pulsar cluster.

- Core Module `shenyu-plugin-logging-pulsar`.
- Core Class `org.apache.shenyu.plugin.logging.pulsar.LoggingPulsarPlugin`
- Core Claas `org.apache.shenyu.plugin.logging.pulsar.client.PulsarLogCollectClient`

- Since ShenYu 2.5.1

- Architecture Diagram

![](assets/images/logging-pulsar-arch-2d4e314b30134d63840444462d10840b_3c5c353a69245389.jpg)

- Full asynchronous collection and delivery of `Logging` inside the `Apache ShenYu` gateway
- Logging platform by consuming the logs in the `Pulsar` cluster for repository, and then using `Grafana`, `Kibana` or other visualization platform to display

<a id="plugin-center-observability-logging-pulsar--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/loggingconsole-use-en-64a3c389309209c07d4ae4602e0e3895_8ed42c6f5a315126.png)

- Add the `Logging-Pulsar` dependency to the gateway's `pom.xml` file.

```xml
 <!--shenyu logging-pulsar plugin start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-logging-pulsar</artifactId> 
    <version>${project.version}</version> 
</dependency> 
<!--shenyu logging-pulsar plugin end--> 
```

- In `shenyu-admin` --> Basic Configuration --> Plugin Management --> `loggingPulsar`, configure the pulsar parameter and set it to on.

![](assets/images/logging-pulsar-config-76f49201912f1a8b106efaa6244997dc_b254c90cf8b7fa7f.jpg)

- The individual configuration items are described as follows:

| config-item | type | description | remarks |
| --- | --- | --- | --- |
| topic | String | Message Queue Topics | must |
| serviceUrl | String | Message queue service address | must |
| sampleRate | String | Sampling rate, range 0~1, 0: off, 0.01: acquisition 1%, 1: acquisition 100% | Optional, default 1, all collection |
| compressAlg | String | Compression algorithm, no compression by default, currently supports LZ4 compression | Optional, no compression by default |
| maxResponseBody | Ingeter | Maximum response size, above the threshold no response will be collected | Optional, default 512KB |
| maxRequestBody | Ingeter | Maximum request body size, above the threshold no request body will be collected | Optional, default 512KB |
| Except for topic, serviceUrl, all others are optional, in most cases only these 3 items need to be configured. The default group id is "shenyu-access-logging" |  |  |  |

- For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-config-7d106f4fbe790030983a05d502a4279d_16c424caa6627130.png)

collect request info as follows

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

Open the plugin and configure pulsar, configure it as follows.

![](assets/images/logging-pulsar-config-76f49201912f1a8b106efaa6244997dc_b254c90cf8b7fa7f.jpg)

For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and samplingf rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-option-topic-8f4ee3bca20050803cde1168d93f7743_74900cd9a806ddc4.jpg)

![](assets/images/log-rule-485f460982c9a3179d2aec6baed5cad3_dc5d85107143d880.jpg)

![](assets/images/call-service-ceeafb89bf58792af70883bdaedbcb93_c3e030552a6c5dce.png)

As each logging platform has differences, such as storage available clickhouse, ElasticSearch, etc., visualization has self-developed or open source Grafana, Kibana, etc..
Logging-Pulsar plugin uses Pulsar to decouple production and consumption, while outputting logs in json format, consumption and visualization require users to choose different technology stacks to achieve their own situation.=

<a id="plugin-center-observability-logging-pulsar--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingPulsar` set Status disable.

---

<a id="plugin-center-observability-logging-rabbitmq"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-rabbitmq/ -->

<!-- page_index: 95 -->

# 1. Overview

Version: 2.7.0.3

- Logging-RabbitMQ Plugin

- collect http request log to rabbitmq, consume rabbitmq message to another application and analysis.

> `Apache ShenYu` The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，
> The list includes: request time, request parameters, request path, response result, response status code, time consumption, upstream IP, exception information waiting.
> The Logging-RabbitMQ plugin is a plugin that records access logs and sends them to the RabbitMQ cluster.

- Core Module `shenyu-plugin-logging-rabbitmq`.
- Core Class `org.apache.shenyu.plugin.logging.rabbitmq.LoggingRabbitmqPlugin`
- Core Claas `org.apache.shenyu.plugin.logging.rabbitmq.client.RabbitmqLogCollectClient`

- Since ShenYu 2.5.0

- Architecture Diagram

![](assets/images/shenyu-agent-logging-arch-9071c054a78f807fac785e44ff908ca4_dd39eb96b0d67200.png)

- Full asynchronous collection and delivery of `Logging` inside the `Apache ShenYu` gateway
- Logging platform by consuming the logs in the `RabbitMQ` cluster for repository, and then using `Grafana`, `Kibana` or other visualization platform to display

<a id="plugin-center-observability-logging-rabbitmq--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Add the `Logging-RabbitMQ` dependency to the gateway's `pom.xml` file.

```xml
<!--shenyu logging-rabbitmq plugin start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-logging-rabbitmq</artifactId> 
    <version>${project.version}</version> 
</dependency> 
<!--shenyu logging-rabbitmq plugin end--> 
```

- In `shenyu-admin` --> Basic Configuration --> Plugin Management --> `loggingRabbitMQ`, configure the rabbitMQ parameter and set it to on.

![](assets/images/logging-config-rabbitmq-en-580b260c6f9540f18c00da2e66ccfd63_50f663937b12e16c.png)

- The individual configuration items are described as follows:

| config-item | type | description | remarks |
| --- | --- | --- | --- |
| host | type | IP | 必须 |
| port | type | PORT | 必须 |
| username | String | rabbitmq username | 可选 |
| password | String | rabbitmq password | 可选 |
| virtualHost | String | rabbitmq virtualHost | 必须，默认/ |
| exchangeType | String | rabbitmq exchange type | 必须，默认direct |
| exchangeName | String | rabbitmq exchange name | 必须 |
| queueName | String | rabbitmq queue name | 必须 |
| routingKey | String | rabbitmq routing key | 必须 |
| durable | Boolean | message durable | 必须，默认true |
| exclusive | Boolean | message exclusive | 必须，默认false |
| autoDelete | String | message auto delete | 必须，默认false |
| args | String | rabbitmq args，exaple：{"x-delay":"1000"}，delay queue | 可选 |
| sampleRate | String | Sampling rate, range 0~1, 0: off, 0.01: acquisition 1%, 1: acquisition 100% | Optional, default 1, all collection |
| maxResponseBody | Ingeter | Maximum response size, above the threshold no response will be collected | Optional, default 512KB |
| maxRequestBody | Ingeter | Maximum request body size, above the threshold no request body will be collected | Optional, default 512KB |
| Except for host,port,virtualHost,exchangeType,exchangeName,queueName,routingKey,durable,exclusive,autoDelete, all others are optional. |  |  |  |

- For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-option-topic-en-976e6ac4788cb63f6064c776f11e487f_17f39ede705fe3d5.png)

collect request info as follows

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

Open the plugin and configure rabbitmq, configure it as follows.

![](assets/images/logging-config-rabbitmq-en-580b260c6f9540f18c00da2e66ccfd63_50f663937b12e16c.png)

For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-option-topic-en-98fcb4293da1c41228784a4ef4b4e22d_0e761e8ef35b0ad2.png)

![](assets/images/log-rule-en-f6395cf773f0db8c42aa6939e2e5ff40_d08815f8cb645ede.jpg)

![](assets/images/call-service-ceeafb89bf58792af70883bdaedbcb93_c3e030552a6c5dce.png)

As each logging platform has differences, such as storage available clickhouse, ElasticSearch, etc., visualization has self-developed or open source Grafana, Kibana, etc..
Logging-RabbitMQ plugin uses RabbitMQ to decouple production and consumption, while outputting logs in json format, consumption and visualization require users to choose different technology stacks to achieve their own situation.

Users can choose to visualize the implementation according to their own situation.
The following shows the effect of `Grafana`:
[Grafana Sandbox Experience](https://play.grafana.org)

![](assets/images/grafana-loki-gateway-381810a5db3b2c0640dbe3fc4b99f5f5_12f05b5849cd51fc.png)

<a id="plugin-center-observability-logging-rabbitmq--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingRabbitMQ` set Status disable.

![](assets/images/logging-rabbitmq-disabled-en-de85a0a331ff79e85afdf3c264abba04_108f66251b770a04.jpg)

---

<a id="plugin-center-observability-logging-rocketmq"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-rocketmq/ -->

<!-- page_index: 96 -->

# 1. Overview

Version: 2.7.0.3

- Logging-RocketMQ Plugin

- collect http request log to rocketmq, consume rocketmq message to another application and analysis.

> `Apache ShenYu` The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，
> The list includes: request time, request parameters, request path, response result, response status code, time consumption, upstream IP, exception information waiting.
> The Logging-RocketMQ plugin is a plugin that records access logs and sends them to the RocketMQ cluster.

- Core Module `shenyu-plugin-logging-rocketmq`.
- Core Class `org.apache.shenyu.plugin.logging.rocketmq.LoggingRocketMQPlugin`
- Core Claas `org.apache.shenyu.plugin.logging.rocketmq.client.RocketMQLogCollectClient`

- Since ShenYu 2.5.0

- Architecture Diagram

![](assets/images/shenyu-agent-logging-arch-9071c054a78f807fac785e44ff908ca4_dd39eb96b0d67200.png)

- Full asynchronous collection and delivery of `Logging` inside the `Apache ShenYu` gateway
- Logging platform by consuming the logs in the `RocketMQ` cluster for repository, and then using `Grafana`, `Kibana` or other visualization platform to display

<a id="plugin-center-observability-logging-rocketmq--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Add the `Logging-RocketMQ` dependency to the gateway's `pom.xml` file.

```xml
<!--shenyu logging-rocketmq plugin start--> 
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-logging-rocketmq</artifactId> 
    <version>${project.version}</version> 
</dependency> 
<!--shenyu logging-rocketmq plugin end--> 
```

- In `shenyu-admin` --> Basic Configuration --> Plugin Management --> `loggingRocketMQ`, configure the rocketMQ parameter and set it to on.

![](assets/images/logging-config-en-2d08ddb2fde45effd73f6de8dcf9677c_76b13204f006e046.png)

- The individual configuration items are described as follows:

| config-item | type | description | remarks |
| --- | --- | --- | --- |
| topic | String | Message Queue Topics | must |
| namesrvAddr | String | Message queue nameserver address | must |
| producerGroup | String | Log Message Producer Group | must |
| sampleRate | String | Sampling rate, range 0~1, 0: off, 0.01: acquisition 1%, 1: acquisition 100% | Optional, default 1, all collection |
| compressAlg | String | Compression algorithm, no compression by default, currently supports LZ4 compression | Optional, no compression by default |
| maxResponseBody | Ingeter | Maximum response size, above the threshold no response will be collected | Optional, default 512KB |
| maxRequestBody | Ingeter | Maximum request body size, above the threshold no request body will be collected | Optional, default 512KB |
| Except for topic, namesrvAddr, producerGroup, all others are optional, in most cases only these 3 items need to be configured. |  |  |  |

- For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-option-topic-en-98fcb4293da1c41228784a4ef4b4e22d_0e761e8ef35b0ad2.png)

collect request info as follows

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

Open the plugin and configure rocketmq, configure it as follows.

![](assets/images/logging-config-en-2d08ddb2fde45effd73f6de8dcf9677c_76b13204f006e046.png)

For detailed configuration of selectors and rules, please refer to: [Selector and rule management](#user-guide-admin-usage-selector-and-rule)。

In addition, sometimes a large gateway cluster corresponds to multiple applications (business), different applications (business) corresponds to different topics, related to isolation, then you can configure different topics (optional) and sampling rate (optional) by selector, the meaning of the configuration items as shown in the table above.
The operation is shown below:
![](assets/images/logging-option-topic-en-98fcb4293da1c41228784a4ef4b4e22d_0e761e8ef35b0ad2.png)

![](assets/images/log-rule-en-d09e07905e13a68c6f28941fe2d5a8e1_65b967a927bcc3a1.jpg)

![](assets/images/call-service-ceeafb89bf58792af70883bdaedbcb93_c3e030552a6c5dce.png)

As each logging platform has differences, such as storage available clickhouse, ElasticSearch, etc., visualization has self-developed or open source Grafana, Kibana, etc..
Logging-RocketMQ plugin uses RocketMQ to decouple production and consumption, while outputting logs in json format, consumption and visualization require users to choose different technology stacks to achieve their own situation.

Users can choose to visualize the implementation according to their own situation.
The following shows the effect of `Grafana`:
[Grafana Sandbox Experience](https://play.grafana.org)

![](assets/images/grafana-loki-gateway-381810a5db3b2c0640dbe3fc4b99f5f5_12f05b5849cd51fc.png)

<a id="plugin-center-observability-logging-rocketmq--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingRocketMQ` set Status disable.

![](assets/images/logging-rocket-disabled-en-abcbfccb1ef5821004a0c7eeeff2138d_815c685d288a4d89.jpg)

---

<a id="plugin-center-observability-logging-tencent-cls"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/logging-tencent-cls/ -->

<!-- page_index: 97 -->

# 1. Overview

Version: 2.7.0.3

- Logging-TencentCls Plugin

- collect http request information to tencent cls, analysis request information by tencent cls platform.

- The gateway receives requests from the client, forwards them to the server, and returns the server results to the client. The gateway can record the details of each request，
- the plugin records access logs and sends to tencent cls platform.

- Core Module `shenyu-plugin-logging-tencent-cls`
- Core Class `org.apache.shenyu.plugin.tencent.cls.LoggingTencentClsPlugin`
- Core Class `org.apache.shenyu.plugin.tencent.cls.client.TencentClsLogCollectClient`

ShenYu 2.5.1

<a id="plugin-center-observability-logging-tencent-cls--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
<!-- shenyu logging-tencent-cls plugin start --> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-logging-tencent-cls</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!-- shenyu logging-tencent-cls plugin end --> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingTencentCls` set Status enable.

![](assets/images/plugin-config-en-50ccf87d6faa6f3c48d1de0c4d44c2ac_5b699d76dc8d3ade.jpg)

| config-item | type | remarks | description |
| --- | --- | --- | --- |
| secretId | String | must | secretId |
| secretKey | String | must | secretKey |
| endpoint | String | must | host name, example:ap-guangzhou.cls.tencentcs.com |
| topic | String | optional, default shenyu-topic | topic |
| sendThreadCount | String | optional, default 1 | Number of core threads for log consumption callback |
| TotalSizeInBytes | Integer | optional, default 104857600 | The maximum log size that the instance can cache |
| MaxSendThreadCount | Integer | optional, default 50 | The maximum number of "goroutines" that the client can concurrently |
| MaxBlockSec | Integer | optional, default 60000 ms | The maximum amount of time the caller can block on the send method if the client is running out of free space. If the required space cannot be satisfied after this time, the send method will throw a TimeoutException. Set this value to a negative number if you want the send method to block until the required space is met |
| MaxBatchSize | Integer | optional, default 512 \* 1024 (512KB) | When the cached log size in a Batch is greater than or equal to batchSizeThresholdInBytes, the batch will be sent, and the maximum size can be set to 5MB |
| MaxBatchCount | Integer | optional, default 4096 | When the number of logs cached in a batch is greater than or equal to batchCountThreshold, the batch will be sent and the maximum can be set to 40960 |
| LingerMs | Integer | optional, default 2000 ms | The duration of the batch from the creation to the time it can be sent, the minimum can be set to 100 milliseconds |
| Retries | Integer | optional, default 10 | If a Batch fails to be sent for the first time, the number of times it can be retried, if the retries is less than or equal to 0, the ProducerBatch will directly enter the failure queue after the first failure of sending |
| MaxReservedAttempts | Integer | optional, default 11 | Each batch that is attempted to be sent corresponds to an Attemp. This parameter is used to control the number of attempts returned to the user. By default, only the latest 11 attempts are retained. A larger parameter allows you to trace more information, but also consumes more memory |
| BaseRetryBackoffMs | Integer | optional, default 100 ms | Backoff time for the first retry The client samples the exponential backoff algorithm, and the planned waiting time for the Nth retry is baseRetryBackoffMs \* 2^(N-1 |
| MaxRetryBackoffMs | Integer | optional, default 50 s | Maximum backoff time for retries |

- get `topic`

![](assets/images/tencent-topic-2d1def01f076253ff3d13b62a1858cde_5cb5318a2100ff5a.png)

- Selector and rule Config. Please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).

collect request info as follows

| Field Name | Meaning | Description | Remarks |
| --- | --- | --- | --- |
| clientIp | Client IP |  |  |
| timeLocal | Request time string, format: yyyy-MM-dd HH:mm:ss.SSS |  |  |
| method | request method (different rpc type is not the same, http class for: get, post wait, rpc class for the interface name) |  |  |
| requestHeader | Request header (json format) |  |  |
| responseHeader | Response header (json format) |  |  |
| queryParams | Request query parameters |  |  |
| requestBody | Request Body (body of binary type will not be captured) |  |  |
| requestUri | Request uri |  |  |
| responseBody | Response body |  |  |
| responseContentLength | Response body size |  |  |
| rpcType | rpc type |  |  |
| status | response status |  |  |
| upstreamIp | Upstream (program providing the service) IP |  |  |
| upstreamResponseTime | Time taken by the upstream (program providing the service) to respond to the request (ms ms) |  |  |
| userAgent | Requested user agent |  |  |
| host | The requested host |  |  |
| module | Requested modules |  |  |
| path | The requested path |  |  |
| traceId | Requested Link Tracking ID | Need to access link tracking plugins, such as skywalking,zipkin |  |

- Open the plugin and configure tencent-cls, configure it as follows.

![](assets/images/plugin-config-en-50ccf87d6faa6f3c48d1de0c4d44c2ac_5b699d76dc8d3ade.jpg)

![](assets/images/tencent-cls-log-selector-en-baf341acf4576d2c99465243260b22fa_fb68b67a146f1e0d.png)

![](assets/images/tencent-cls-log-rule-en-58a0d8e2101b2317e7bf900d4ec38d75_7a144c6a3b82bee3.png)

![](assets/images/call-service-82c34bd837e86ae6d808a8f86dbd2a50_ecfa3a4c571276fc.png)

![](assets/images/tencent-cls-log-e9fa8f8a850ad5ea6bde2cb42d8fa125_4d58bd6f5b69cd7f.jpg)

<a id="plugin-center-observability-logging-tencent-cls--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `loggingTencentCls` set Status disable.

---

<a id="plugin-center-observability-metrics-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/observability/metrics-plugin/ -->

<!-- page_index: 98 -->

# Metrics Plugin

Version: 2.7.0.3

- Metrics plugin is used to monitor its own running status(JVM-related) by gateway, include request response delay, QPS, TPS, and other related metrics.

- Flow Diagram
  ![](assets/images/shenyu-metrics-805b9a2539e9808d934caae9b3a1404f_f60cd206dc98dde8.png)
- Make even tracking in ShenYu Gateway by asynchronous or synchronous mode.
- The `prometheus` server pulls metrics' through http request, and then displays it by `Grafana`.

- Introduce `metrics` dependency in the pom.xml file of the gateway.

```xml
  <!-- apache shenyu metrics plugin start--> 
  <dependency> 
      <groupId>org.apache.shenyu</groupId> 
      <artifactId>shenyu-spring-boot-starter-plugin-metrics</artifactId> 
      <version>${project.version}</version> 
  </dependency> 
  <!-- apache shenyu metrics plugin end--> 
```

- modify this config in shenyu gateway yaml

```yml
shenyu: 
  metrics: 
    enabled: false #false is close, true is open 
    name : prometheus  
    host: 127.0.0.1 
    port: 8090 
    jmxConfig: 
    props: 
      jvm_enabled: true #enable jvm monitoring 
```

- All JVM，thread，memory，and other related information will be made event tracking，you can add a JVM module in the Grafana' panel, and it will be fully displayed, please refer to： <https://github.com/prometheus/jmx_exporter>
- There are also the following custom `metrics`

| Name | type | labels | description |
| --- | --- | --- | --- |
| shenyu\_request\_total | Counter | none | collecting all requests of Apache ShenYu Gateway |
| shenyu\_request\_throw\_total | Counter | none | collecting all exception requests of Apache ShenYu Gateway |
| shenyu\_request\_type\_total | Counter | path,type | collecting all matched requests of monitor |
| shenyu\_execute\_latency\_millis | histogram | none | ShenYu gateway execute time interval |

| name | type | labals | help |
| --- | --- | --- | --- |
| jmx\_config\_reload\_success\_total | counter |  | Number of times configuration have successfully been reloaded. |
| jmx\_config\_reload\_failure\_total | counter |  | Number of times configuration have failed to be reloaded. |
| jmx\_scrape\_duration\_seconds | gauge |  | Time this JMX scrape took, in seconds. |
| jmx\_scrape\_error | gauge |  | Non-zero if this scrape failed. |
| jmx\_scrape\_cached\_beans | gauge |  | Number of beans with their matching rule cached |
| jmx\_scrape\_duration\_seconds | gauge |  | Time this JMX scrape took, in seconds. |
| jmx\_scrape\_error | gauge |  | Non-zero if this scrape failed. |
| jmx\_scrape\_cached\_beans | gauge |  | Number of beans with their matching rule cached |

| name | type | labels | help |
| --- | --- | --- | --- |
| process\_cpu\_seconds\_total | counter |  | Total user and system CPU time spent in seconds. |
| process\_start\_time\_seconds | gauge |  | Start time of the process since unix epoch in seconds. |
| process\_open\_fds | gauge |  | Number of open file descriptors. |
| process\_max\_fds | gauge |  | Maximum number of open file descriptors. |
| process\_virtual\_memory\_bytes | gauge |  | Virtual memory size in bytes. |
| process\_resident\_memory\_bytes | gauge |  | Resident memory size in bytes. |

| name | type | labels | help |
| --- | --- | --- | --- |
| jvm\_memory\_objects\_pending\_finalization | gauge | {area="heap\|nonheap"} | The number of objects waiting in the finalizer queue. |
| jvm\_memory\_bytes\_used | gauge | {area="heap\|nonheap"} | Used bytes of a given JVM memory area. |
| jvm\_memory\_bytes\_committed | gauge | {area="heap\|nonheap"} | Committed (bytes) of a given JVM memory area. |
| jvm\_memory\_bytes\_max | gauge | {area="heap\|nonheap"} | Max (bytes) of a given JVM memory area. |
| jvm\_memory\_bytes\_init | gauge | {area="heap\|nonheap"} | Initial bytes of a given JVM memory area. |
| jvm\_memory\_pool\_bytes\_used | gauge | {pool} | Used bytes of a given JVM memory pool. |
| jvm\_memory\_pool\_bytes\_committed | gauge | {pool} | Committed bytes of a given JVM memory pool. |
| jvm\_memory\_pool\_bytes\_max | gauge | {pool} | Max bytes of a given JVM memory pool. |
| jvm\_memory\_pool\_bytes\_init | gauge | {pool} | Initial bytes of a given JVM memory pool. |
| jvm\_memory\_pool\_collection\_used\_bytes | gauge | {pool} | Used bytes after last collection of a given JVM memory pool. |
| jvm\_memory\_pool\_collection\_committed\_bytes | gauge | {pool} | Committed after last collection bytes of a given JVM memory pool. |
| jvm\_memory\_pool\_collection\_max\_bytes | gauge | {pool} | Max bytes after last collection of a given JVM memory pool. |
| jvm\_memory\_pool\_collection\_init\_bytes | gauge | {pool} | Initial after last collection bytes of a given JVM memory pool. |

| name | type | labels | help |
| --- | --- | --- | --- |
| jvm\_memory\_pool\_allocated\_bytes\_total | counter | {pool} | Total bytes allocated in a given JVM memory pool. Only updated after GC, not continuously. |

| name | type | labels | help |
| --- | --- | --- | --- |
| jvm\_buffer\_pool\_used\_bytes | gauge | {pool} | Used bytes of a given JVM buffer pool. |
| jvm\_buffer\_pool\_capacity\_bytes | gauge | {pool} | Bytes capacity of a given JVM buffer pool. |
| jvm\_buffer\_pool\_used\_buffers | gauge | {pool} | Used buffers of a given JVM buffer pool. |

| name | type | labels | help |
| --- | --- | --- | --- |
| jvm\_gc\_collection\_seconds | summary | {gc} | Time spent in a given JVM garbage collector in seconds. |

| name | type | labels | help |
| --- | --- | --- | --- |
| jvm\_threads\_current | gauge |  | Current thread count of a JVM |
| jvm\_threads\_daemon | gauge |  | Daemon thread count of a JVM |
| jvm\_threads\_peak | gauge |  | Peak thread count of a JVM |
| jvm\_threads\_started\_total | counter |  | Started thread count of a JVM |
| jvm\_threads\_deadlocked | gauge |  | Cycles of JVM-threads that are in deadlock waiting to acquire object monitors or ownable synchronizers |
| jvm\_threads\_deadlocked\_monitor | gauge |  | Cycles of JVM-threads that are in deadlock waiting to acquire object monitors |
| jvm\_threads\_state | gauge | {state} | Current count of threads by state |

| name | type | labels | help |
| --- | --- | --- | --- |
| jvm\_classes\_loaded | gauge |  | The number of classes that are currently loaded in the JVM |
| jvm\_classes\_loaded\_total | counter |  | The total number of classes that have been loaded since the JVM has started execution |
| jvm\_classes\_unloaded\_total | counter |  | The total number of classes that have been unloaded since the JVM has started execution |

| name | type | labels | help |
| --- | --- | --- | --- |
| jvm | info | {version(java.runtime.version),vendor(java.vm.vendor),runtime(java.runtime.name)} | VM version info |

Users need to install `Prometheus` service to collect

- Choose the corresponding environment [download address](https://prometheus.io/download/) to install
- Modify configuration file: `prometheus.yml`

```yaml
scrape_configs: 
  - job_name: 'Apache ShenYu' 
    # metrics_path defaults to '/metrics' 
    # scheme defaults to 'http'. 
    static_configs: 
    - targets: ['localhost:8090'] # metrics of apache shenyu are exposed on port 8090 by default 
```

- After the configuration is completed, you can directly double-click `prometheus.exe` in the window to start. The default boot port is `9090`,check `status`->`Targets` . Success can be verified at <http://localhost:9090/>

![](assets/images/request-metric-6-e6e3fea6e33e3799c8f4d2dfa98bc5ec_d0505997d791911e.png)

- Install prometheus with brew，After installation `prometheus` is in the `Cellar` folder under `homebrew`。

```text
brew install prometheus 
```

- Execute the following command in the location of the prometheus.yml file to start prometheus。

```text
prometheus --config.file=prometheus.yml & 
```

Visit `http://localhost:9090/` to verify that it starts normally。

It is recommended to use `Grafana`, Users can customize the query to personalize the display panel.

Here's how to install and deploy `Grafana`

- Install Grafana

[download](https://dl.grafana.com/oss/release/grafana-7.4.2.windows-amd64.zip) Unzip it and enter the `bin` directory and `double-click` `grafana-server.exe` to run it. Go to <http://localhost:3000/?orgId=1> `admin/admin` to verify the success

- Install grafana using brew.

```text
brew install grafana 
```

- Start grafana as a service

```text
brew services start grafana 
```

Visit `http://localhost:3000/` to verify that it starts normally.

- Configure the data source, select prometheus, note that the data source name is prometheus.

![](assets/images/request-metric-7-355daf90afad71497091d1b1fdb477fb_209631adc02fd199.png)

![](assets/images/request-metric-8-8425d041585a6db6b27412ac052c5e57_166af2fe335d4555.png)

- Config Custom Metric Dashboard `request_total`、`http_request_total`

Click `Create` - `Import` and enter the [panel config json](assets/files/request-metric-dashboard_d8b545a2b2beb738.json)

The final custom HTTP request monitoring panel looks like this:

![](assets/images/request-metric-1-92f09dff492b284cf5462a1b2149f804_595cc18ea65ca5f7.png)

![](assets/images/request-metric-2-4ef0ea780f6d612bb1076decaa4c4549_1cab72f1d60eb935.png)

![](assets/images/request-metric-3-25e310a4c0c636d2ccd872bada66bfe9_43bb371f1d55f57b.png)

![](assets/images/request-metric-4-d95d82437f8344ab537170fc78ee980c_246ac5677126cd44.png)

![](assets/images/request-metric-5-5be0cded02230111957e9cbf0b74f653_e08b05cfc62a38d5.png)

---

<a id="plugin-center-common-general-context-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/common/general-context-plugin/ -->

<!-- page_index: 99 -->

# GeneralContext Plugin

Version: 2.7.0.3

- When making invokes to the target service, Apache ShenYu gateway also allows users to use the `generalContext` plugin to pass the service context parameters by reading the header in this request.

- In `shenyu-admin` --> BasicConfig --> Plugin --> `generalContext`, set to enable.
- If the user don't use, please disable the plugin in the background.

![](assets/images/general-context-open-en_74f748c9f877e63f.png)

- Introduce `generalContext` support in the pox.xml file of the gateway.

```xml
        <!-- apache shenyu general context plugin start--> 
        <dependency> 
            <groupId>org.apache.shenyu</groupId> 
            <artifactId>shenyu-spring-boot-starter-plugin-general-context</artifactId> 
            <version>${project.version}</version> 
        </dependency> 
        <!-- apache shenyu general context plugin end--> 
```

- Selectors and rules, please refer to: [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule).
- Only those matched requests can print the information about this request.

- The parameters in the request header need to be passed to the proxy server.
- Need to replace a key in the request header and pass it to the proxy server.

---

<a id="plugin-center-cache-cache-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/cache/cache-plugin/ -->

<!-- page_index: 100 -->

# 1. Overview

Version: 2.7.0.3

- Cache Plugin

- Situation where data is not updated frequently and a large number of calls are required.
- For Situation where data consistency is not required.

- The `Cache` plugin is able to cache the results of the target service, allowing the user to configure the expiration
  time of the cached results.

- Core Module `shenyu-plugin-cache-handler`.
- Core Module `shenyu-plugin-cache-redis`.
- Core Module `shenyu-plugin-cache-memory`.
- Core Class `org.apache.shenyu.plugin.cache.CachePlugin`
- Core Class `org.apache.shenyu.plugin.cache.redis.RedisCache`
- Core Class `org.apache.shenyu.plugin.cache.memory.MemoryCache`

- Since 2.4.3

<a id="plugin-center-cache-cache-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

![](assets/images/plugin-use-en-8b5661551cdf92fdabc9cb2e7947cffc_92f943a9f1a2d6a8.jpg)

- Import cache plugin dependency in `ShenYu Bootstrap`.

```xml
<!--shenyu cache plugin start--> 
<dependency> 
  <groupId>org.apache.shenyu</groupId> 
  <artifactId>shenyu-spring-boot-starter-plugin-cache</artifactId> 
  <version>${project.version}</version> 
</dependency> 
<!--shenyu cache plugin end--> 
```

- In shenyu-admin --> BasicConfig --> Plugin --> `cache` set Status enabled.

![](assets/images/cache-plugin-config-en-a94429e8eb8d41ab800b4cf63f83ebd6_eabb053e1eeb4e6f.png)

- `cacheType`: Cache currently supports two modes of caching data.
- memory：local memory mode
- redis：redis mode

The current default is `local memory mode`, the results of the target service are stored in the local memory, if the
gateway is deployed by way of cluster, it is not recommended to use `local memory mode`, it is recommended to
use `redis mode`, the data of the target service are cached in redis.

If you are using `local memory mode`, you only need to select memory in cacheType, no other configuration is needed.

If you are using `redis mode`, select redis in cacheType, and the parameters are as follows

- `database`: which database the cache results are stored in, the default is index database 0.
- `master`: default is master.
- `mode`: the working mode of redis, the default is single-point mode: `standalone`, in addition to cluster
  mode: `cluster`, sentinel mode: `sentinel`.
- `url`: configure the IP and port of the redis database, configured by colon connection, example: `192.168.1.1:6379`.
- `password`: the password of the redis database, if not, you can not configure.
- `maxldle`: the maximum free connections in the connection pool
- `minldle`: minimum idle connections in the connection pool
- `maxActive`: the maximum number of connections in the connection pool
- `maxWait`: the maximum blocking wait time for the connection pool (use negative values to indicate no limit) default -1

- Selectors and rules, please refer to: [Selector And Rule Config](#user-guide-admin-usage-selector-and-rule) .

![](assets/images/cache-plugin-rule-en-f87256d214b81b378f155e1cf02b6fdf_3c2eb8dd6c2e6c1f.png)

- Only matching requests will be cached by the Cache plugin for the results of the target service.

`timeoutSecods`: the value is the target service result data cache time, the default is 60, in `seconds`.

Notice: The current version of the Cache plugin uses the url as a unique key to identify the same request.

![](assets/images/cache-plugin-config-example-en-51e820d0cd6ca19fb8ebea5ee045352d_520c1c95da013deb.png)

select redis cache type, config redis database, url, mode, password

![](assets/images/cache-plugin-selector-en-a4d58981c816f3776646f74865ae102c_1a6a8e9ef7f4dc1d.png)

![](assets/images/cache-plugin-rule-en-f87256d214b81b378f155e1cf02b6fdf_3c2eb8dd6c2e6c1f.png)

- send http request to cache result.

request

```http
### shengyu getway proxy orderSave 
GET http://localhost:9195/http/order/findById?id=123 
Accept: application/json 
Content-Type: application/json 
```

![](assets/images/cache-result-6cf64e74954ad4fb3bbd1f0bae2cfc9b_a66b08e1355f9a01.jpg)

![](assets/images/cache-result-check-0070758c84d5ab1ba0d88d4bab73fe92_f47895012ff4cf7f.png)

<a id="plugin-center-cache-cache-plugin--3.-how-to-disable-plugin"></a>

# 3. How to disable plugin

- In `shenyu-admin` --> BasicConfig --> Plugin --> `cache` set Status disable.

---

<a id="plugin-center-mock-mock-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/mock/mock-plugin/ -->

<!-- page_index: 101 -->

# 1. Overview

Version: 2.7.0.3

- Mock Plugin

- Specify the status code and response body for the request to facilitate testing.

- Set the status code and body of the request.
- Support configuration `${}` placeholder to automatically generate data.
- **Note:** In order to support a more flexible data generation method, the mock plug-in supports users to use SpEL expressions to generate mock data. Using SpEL expressions may lead to the risk of executing malicious scripts or applying destructive programs. We recommend that you be extra careful when using them, use them in a safe environment as much as possible, such as an intranet environment, and follow security best practices.

- Core module `shenyu-plugin-mock`
- Core class `org.apache.shenyu.plugin.mock.MockPlugin`

- 2.5.0

<a id="plugin-center-mock-mock-plugin--2.-how-to-use-plugin"></a>

# 2. How to use plugin

- import maven config in shenyu-bootstrap project's `pom.xml` file.

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-spring-boot-starter-plugin-mock</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- In `shenyu-admin` --> BasicConfig --> Plugin --> `mock` set Status enable.

![](assets/images/enable-mock-plugin-en-4c1452eb346e287d11b94f8cdf4cbec7_9837bcaa1bad3600.png)

- Selector and rule config, please refer: [Selector and rule config](#user-guide-admin-usage-selector-and-rule).
- shenyu-admin mock plugin configuration, supports configuring httpStatusCode and responseContent
  - httpStatusCode:the status code of the request.
  - responseContent:the response body of the request,support configuring `${}` placeholders to generate random data.

![](assets/images/mock-rule-configuration-en-f71ebf28e7338971afc9136819d32277_576096057d2a11ab.png)

**~~`${int|min-max}`~~**

- **Description:** Generate random integers from `min` to `max`, inclusive of `min` and `max`.
- **Example:** `${int|10-20}`

**~~`${double|min-max|format}`~~**

- **Description:** Generate random floating point numbers from `min` to `max`, formatted according to `format`.
- **Example:** `${double|10-20}` , `${double|10-20.5|%.2f}`

**~~`${email}`~~**

- **Description:** Generate random email addresses.

**~~`${phone}`~~**

- **Description:** Generate random 13-digit mobile number.

**~~`${zh|min-max}`~~**

- **Description:** Generate random Chinese strings of length `min` to `max`.
- **Example:** `${zh|10-20}`

**~~`${en|min-max}`~~**

- **Description:** Generate random English strings of length `min` to `max`.
- **Example:** `${en|10-20}`

**~~`${bool}`~~**

- **Description:** Generate a random `boolean` value i.e. `true` or `false`.

**~~`${list|[arg1,arg2...]}`~~**

- **Description:** Randomly returns any value in a list as a string.
- **Example:** `${list|[gril,boy]}` will return `boy` or `girl`

**~~`${current|format}`~~**

- **Description:** Returns the current time and uses `format` to format, `format` can be default, the default is `YYYY-MM-dd HH:mm:ss`.
- **Example:** `${current}`，`${current|YYYY-MM-dd}`

**~~`${array|item|length}`~~**

- **Description:** According to the `item` format definition, an array of length `length` can be generated. All the above data generation rules can be nested in `item`, and the result will be automatically added with `[]`.
- **Example:** `${array|{"name":"test"}|3}` result is `[{"name":"test"},{"name":"test"},{"name":"test"}]`，`${array|{"age":${int|18-65}}|3}`.

**${expression|expression}**

`Spel` expressions are currently supported with built-in functions and arguments, which fully replace the old $ syntax

- **`${expression|#int(min,max)}`**

  - **Description:** Generate random integers from `min` to `max`, inclusive of `min` and `max`.
  - **Example：** `${expression|#int(1,2)}`
- **`${expression|#double(min,max)}`**

  - **Description:** Generate random floating point numbers from `min` to `max`, formatted according to `format`.
  - **Example:**`${expression|#double(10.5,12.0)}`,`${expression|#double(10.5,12.0,'￥%.2f')}`
- **`${expression|#email()}`**

  - **Description:** Generate random email addresses.
- **`${expression|#phone()}`**

  - **Description:** Generate random 13-digit mobile number.
- **`${expression|zh(min,max)}`**

  - **Description:** Generate random Chinese strings of length `min` to `max`.
  - **Example：** `${expression|#zh(1,10)}`
- **`${expression|#bool()}`**

  - **Description:** Generate a random `boolean` value i.e. `true` or `false`.
- **`${expression|#oneOf(arg1,arg2...)}`**

  - **Description:** Randomly returns any value in a list.
  - **Example：** `${expression|#oneOf('shenyu','number',1)}` will return `'shenyu'` or `'number'`or`1`
- **`${expression|current()}`**

  - **Description:** Returns the current time and uses `format` to format, `format` can be default, the default is `YYYY-MM-dd HH:mm:ss`.
  - **Example：** `${expression|#current()}`，`${expression|#current('YYYY-MM-dd')}`
- **`${expression|#array(item,length)}`**

  - **Description:** According to the `item` format definition, an array of length `length` can be generated.
  - **Example:** `expression|#array('shenyu',3)` would generate `["shenyu","shenyu","shenyu"]`.

    You can use it nested like`${expression|#array(#bool(),2)}`or`${expression|#array(#array('shenyu',2),2)}`
- **`${expression|#req}`**

  - **Description:** Req is built-in request parameters ,which can generate response data based on request content
  - **Example:**`${expression|#req.method}`、`${expression|#req.queries['query_name']}`、`${req.queries.query_name}`、`${expression|#req.uri}`。`jsonPath` is used when the request body is json . For example ,when the request body is `{"name":"shenyu"}`，`${expression|#req.json.name}`would return "shenyu"

- **`${expression|spel}`**

  - **Description**：Use Spel expressions directly to generate data
  - **Example**：`${expression|T(java.time.LocalDate).now()}`、`${expression|1==1}`

It is recommended to use the new '$' syntax. The old syntax may be removed at an later date.

Function replaceable table:

| old | new |
| --- | --- |
| ${int\|min-max} | ${expression\|#int(min,max)} |
| ${double\|min-max\|format} | ${expression\|#double(min,max)} |
| ${email} | ${expression\|#email()} |
| ${phone} | ${expression\|#phone()} |
| ${zh\|min-max} | ${expression\|#zh(min,max)} |
| ${en\|min-max} | ${expression\|#en(min,max)} |
| ${list\|[arg1,arg2...]} | ${expression\|#oneOf(arg1,agr2...)} |
| ${current\|format} | ${expression\|#current(format)} |
| ${bool} | ${expression\|#bool()} |
| ${array\|item\|length} | ${expression#array(item,length)} |

**You do not need to use add `""` on both sides of `${}`, the generated content will be prefixed and suffixed according to the definition of generator**

---

<a id="plugin-center-ai-ai-prompt"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/ai/ai-prompt/ -->

<!-- page_index: 102 -->

# AiPrompt Plugin

Version: 2.7.0.3

The **aiPrompt** plugin is used to dynamically inject preset prompt content (such as system-role messages or contextual information) into requests before forwarding them. When a request configured with aiPrompt reaches the gateway, the plugin first adds the specified prompt text to the request body (for example, inserting a **system** message at the beginning of the message list). This is useful for unified context control or preset roles—for instance, automatically adding a “You are a translation assistant” system prompt to every request. Used together with aiProxy, it’s primarily for enhancing prompts.

In the ShenYu admin interface, you first create a **Selector** and then a **Rule**. A Selector matches incoming requests (by path, headers, etc.), while a Rule configures plugin parameters or forwarding targets. For more on Selector and Rule setup, see [Selector and Rule Management](#user-guide-admin-usage-selector-and-rule).

When configuring aiPrompt, pay attention to:

- **Selector**: Defines which requests to match. For example, set `Pattern` to `/**` to match all requests, or specify a particular route.
- **Rule**: Specify plugin parameters at the rule level:
  - `prepend`: **Prepend prompt content.** This text is inserted before the user’s original messages as the first message sent to the LLM. Typically used to inject global system instructions or context, e.g., “You are a translation assistant; translate user input into English.”
  - `preRole`: **Role for the prepend prompt.** Sets the `role` field for the `prepend` message (same options as the OpenAI Chat API).
  - `append`: **Append prompt content.** Text added after the user’s messages.
  - `postRole`: **Role for the append prompt.** Sets the `role` field for the `append` message.

Below are example screenshots of aiPrompt plugin configuration in the admin UI:

![](assets/images/ai-prompt-selector-en-91a8a8b25fa4798839b1d88150bb85b7_bf710dc0079653a6.png)

![](assets/images/ai-prompt-rule-en-ad41c83349adf623db8ded5f479296c1_19d259370b6742fb.png)

> **Note:** The aiPrompt plugin depends on aiProxy. In a typical request flow, apply **AiPrompt** first (if injecting prompts), then **AiTokenLimiter** for token counting/rate limiting (if needed), and finally **AiProxy** to forward the request to the LLM service. Ensure **AiTokenLimiter**’s **sort** value is **less than** **AiProxy** and **greater than** **AiPrompt** in the “Plugin Management” order.

After enabling the aiProxy plugin, you can send requests to the ShenYu gateway (e.g., via Postman) to obtain LLM responses through the proxy:

```bash
curl --location --request POST 'http://localhost:9195/ai/proxy/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{"model": "gpt-4o-mini","messages": [{"role": "user","content": "I bloom amidst slaughter, like a flower at dawn."}] }'
```

![](assets/images/ai-prompt-api-867ce005e059588819b7a7899a1f53b4_0e3c607126b730c3.png)

---

<a id="plugin-center-ai-ai-proxy"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/ai/ai-proxy/ -->

<!-- page_index: 103 -->

# AiProxy Plugin

Version: 2.7.0.3

The **aiProxy** plugin acts as a forwarding proxy for LLM requests, supporting major large-model services. Users send requests through ShenYu to a route configured with aiProxy; aiProxy then uses the plugin settings—such as provider (e.g., OpenAI, Alibaba Cloud), model name, API key, etc.—to call the corresponding LLM API and return the result. Typical use cases include forwarding chat requests to OpenAI’s ChatGPT endpoint or using domestic AI services for intelligent Q&A. Similar to previous plugin usage patterns, you can think of the LLM as taking on the role of your original application service. If you have a local model compatible with the OpenAI protocol or other mainstream protocols, you can also proxy it via the shenyu-aiProxy plugin.

When configuring the plugin in the ShenYu admin interface, you first create a **Selector**, then create a **Rule**. A Selector is typically used to match request conditions (e.g., path, headers), while a Rule is used to configure plugin parameters or forwarding targets. For details on Selector and Rule configuration, see [Selector and Rule Management](#user-guide-admin-usage-selector-and-rule).

When using the aiProxy plugin, pay attention to the following fields:

- **Selector**: Defines the paths or request characteristics to match. For example, set `Pattern` to `/**` to match all requests, or specify a particular route path.
- **Rule**: Specify plugin parameters at the rule level. Common fields include:
  - `provider`: The name of the provider, e.g., `OpenAI`.
  - `baseUrl`: The API endpoint for the LLM provider.
  - `model`: The model name.
  - `apiKey`: The authorization key.

Below are example screenshots of the aiProxy plugin configuration in the admin UI:

Selector matching the incoming path, followed by Rule settings for provider, model, API key, upstream address, etc.

![](assets/images/ai-proxy-selector-en-230480625466a1dfa9c425afc223aaa1_950d1fdf1329b3db.png)

![](assets/images/ai-proxy-rule-en-2960454f8b38246d7730e40784ee795d_eab091752c97984c.png)

> **Note:** With this setup, you also need to configure the `contextPath` plugin to remove the matched prefix and assemble the correct call URL. See [contextPath Plugin Configuration](https://shenyu.apache.org/docs/plugin-center/http-process/contextPath-plugin.md) for details.

After enabling the aiProxy plugin, you can send requests to the ShenYu gateway (e.g., via Postman) and obtain LLM responses through the proxy:

```bash
curl --location --request POST 'http://localhost:9195/ai/proxy/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{"model": "gpt-4o-mini","messages": [{"role": "system","content": "You are a translation assistant. Please translate the input content into English." },{"role": "user","content": "I bloom amidst slaughter, like a flower at dawn."}] }'
```

![](assets/images/ai-proxy-api-ef5e61fe03ccef55196fedd4b5e80797_ab72117ef3701876.png)

---

<a id="plugin-center-ai-ai-token-limiter"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/ai/ai-token-limiter/ -->

<!-- page_index: 104 -->

# AiTokenLimiter Plugin

Version: 2.7.0.3

The **aiTokenLimiter** plugin is used to track token consumption from LLM responses and enforce rate limiting via Redis. After each response, aiTokenLimiter calculates the number of tokens used and accumulates counts by user or business dimension. If the preset threshold is exceeded, subsequent requests can be rejected or throttled. Note that ShenYu’s rate limiting is typically implemented using Redis to store token buckets or sliding-window states; aiTokenLimiter likewise relies on Redis to record and check token usage. It is most commonly paired with **aiProxy** for token-based rate limiting.

When configuring the plugin in the ShenYu admin console, you first create a **Selector**, then a **Rule**. A **Selector** matches request conditions (e.g., path, headers), while a **Rule** defines plugin parameters or forwarding targets. For more details, see [Selector and Rule Management](#user-guide-admin-usage-selector-and-rule).

Key fields for **aiTokenLimiter**:

- **Selector**: Defines which requests to match. For example, set `Pattern` to `/**` to match all requests, or specify a particular route.
- **Rule**: Configure plugin parameters:
  - `timeWindowSeconds`: Length of the rate-limiting window (in seconds). Within this window, the plugin tallies total token usage and compares it against `tokenLimit`.
  - `keyName`: Field name in the request used as the rate-limiting “dimension key,” in conjunction with `aiTokenLimitType` (e.g., HEADER, PARAMETER, COOKIE).
  - `tokenLimit`: Maximum number of tokens allowed within the time window. The plugin counts downstream LLM **completion tokens** (the tokens consumed by generated content). Once this limit is exceeded, further requests receive an HTTP 429 response.

Example screenshots of **aiTokenLimiter** setup in the admin interface:

![ai-token-limiter-selector](assets/images/ai-token-limiter-selector-zh-050f076c8987cb9c9c834684cc01aa17_d172fc1e6e096a30.png)

![ai-token-limiter-rule](assets/images/ai-token-limiter-rule-zh-672a88bbeb70045a60ecfcc39d406ea6_5606e4ab8142ad74.png)

> **Note:** The **aiTokenLimiter** plugin depends on **aiProxy**. In a typical flow, apply **AiPrompt** (if injecting a prompt), then **AiTokenLimiter** (for token counting/rate limiting), and finally **AiProxy** (to forward the request to the LLM). Ensure that **AiTokenLimiter**’s **sort** value is **less than** **AiProxy** and **greater than** **AiPrompt** in the “Plugin Management” list.

With **AiProxy** and **AiTokenLimiter** enabled, send requests through the ShenYu gateway (e.g., via Postman) to proxy LLM calls:

```bash
curl --location --request POST 'http://localhost:9195/ai/proxy/v1/chat/completions' \ --header 'Content-Type: application/json' \ --data-raw '{"model": "gpt-4o-mini","messages": [{"role": "user","content": "我于杀戮之中盛放，亦如黎明中的花朵"}] }'
```

Example request (before rate limiting):
![ai-proxy-api](assets/images/ai-token-limiter-api-before-cc7312a27b9b44ef36834bc9c28127d3_053c115ad8aa609c.png)

If you set tokenLimit=10 and make another request within 60 seconds, AiTokenLimiter will intercept it, return HTTP 429, and indicate that the token usage limit has been reached. Please try again later.

Example response (after rate limiting):
![ai-proxy-api](assets/images/ai-token-limiter-api-after-7fc54594554eb138101ed65ab48c8ce5_8db0e33238eb7223.png)

---

<a id="plugin-center-mcp-mcp-server-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/plugin-center/mcp/mcp-server-plugin/ -->

<!-- page_index: 105 -->

# McpServer Plugin

Version: 2.7.0.3

- The `mcpServer` plugin is used to enable the `mcpServer` functionality in the ShenYu gateway. After enabling this plugin, users can register `Tools` for unified management by the gateway.
- The `mcpServer` plugin must be used together with a `proxy` plugin to enable Tool invocation.

- To add the necessary dependencies and enable the plugin, please refer to: [Quick Start with McpServer](#quick-start-quick-start-mcpserver).
- For McpTool client integration, please refer to: [McpTool Service Integration](#user-guide-proxy-mcp-tool-proxy).
- For selector and rule configuration, please refer to: [Selector and Rule Management](#user-guide-admin-usage-selector-and-rule).

After the client is connected to the `Apache ShenYu` gateway, selector and rule information will be automatically registered. For details about selector and rule configuration, please refer to: [Selector and Rule Management](#user-guide-admin-usage-selector-and-rule).

![](assets/images/selector-new_de922246b2dd4b6e.png)

For selector handling, the current version only supports the `startWith` condition in `Condition`. The `endpoint` is equal to the gateway route plus the URL configured in `Condition` and the request protocol (sse/streamablehttp).

Click "SSE Configuration" or "Streamable Configuration" to enter the JSON editing page, which helps users conveniently edit the JSON configuration required by the Mcp client.

![](assets/images/mcp-client-config-en_0e20d498febdf02b.png)
![](assets/images/tool-config_278cb84a8b467b1a.png)
![](assets/images/request-config_8780678811625630.png)

Tool handling refers to the `handle` field, which allows you to perform operations after the gateway has completed traffic matching. For more information, please refer to [Plugin Handle Explanation](#user-guide-admin-usage-plugin-handle-explanation) in plugin management.

- Details of tool configuration:

  - `Description`: Defines the purpose of the tool.
  - `Parameter`: Defines the type of parameters required by the tool.
- Details of requestConfig configuration:

  - `url`: Defines context-path + the actual URL of the tool.
  - `method`: Defines the request type of the tool method.
  - `argsPosition`: Defines the correspondence between all parameters and their positions.
  - `argsToJsonBody`: If true, all parameters will be added to the body.
  - `headers`: You can add headers required by the Tool here.

- In `shenyu-admin` --> Basic Configuration --> Plugin Management --> set `mcpServer` to disabled.

![](assets/images/disable-ed149a0d49785cec3ddf99dd39618440_f2448c18864f2760.png)

---

<a id="developer-spi-custom-load-balance"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/spi/custom-load-balance/ -->

<!-- page_index: 106 -->

# Custom Load Balancer

Version: 2.7.0.3

- This paper describes how to customize the extension of `org.apache.shenyu.loadbalancer.spi.LoadBalancer`.
- Create a new project and introduce the following dependencies:

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-plugin-base</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
</dependencies> 
```

- Create a new class `CustomLoadBalancer`, extends `org.apache.shenyu.loadbalancer.spi.AbstractLoadBalancer`.

```java
public class CustomLoadBalancer extends AbstractLoadBalancer { 
 
    @Override 
    public Upstream doSelect(final List<Upstream> upstreamList, final String ip) { 
        // custom load balancer 
    } 
} 
```

- In the project's META-INF/services directory, create key-value as following in `org.apache.shenyu.loadbalancer.spi.LoadBalancer` file.

script

```shell
${spi name}=${custom class path} 
```

`${spi name}` represents the name of `spi` and `${custom class path}` represents the fully qualified name of the class. Such as:

script

```shell
custom=xxx.xxx.xxx.CustomLoadBalancer 
```

- Package the project and copy it to the `lib` or `ext-lib` directory of the gateway (bootstrap-bin).
- In the `Apache ShenYu` gateway management system --> BasicConfig --> Dictionary, find the dictionary code as `LOAD_BALANCE`, add a new piece of data, pay attention to the dictionary name: `${spi name}`.

![](assets/images/custom-load-balancer-en_cd72196089a3c800.png)
> DictionaryType: `loadBalance`;
>
> DictionaryCode: `LOAD_BALANCE`;
>
> DictionaryName: `${spi name}`, input your custom spi name;
>
> DictionaryValue: When used, the value of the drop-down box, do not repeat with the existing;
>
> DictionaryDescribe: desc your custom match strategy;
>
> Sort: to sort;

- When adding selectors or rules, you can use custom MatchType:

![](assets/images/use-custom-load-balancer-en_92068eecb58df49e.png)

---

<a id="developer-spi-custom-match-mode"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/spi/custom-match-mode/ -->

<!-- page_index: 107 -->

# Custom Match Mode

Version: 2.7.0.3

- This paper describes how to customize the extension of `org.apache.shenyu.plugin.base.condition.strategy.MatchStrategy`.
- Create a new project and introduce the following dependencies:

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-plugin-base</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
</dependencies> 
```

- Create a new class `CustomMatchStrategy`, extends `org.apache.shenyu.plugin.base.condition.strategy.AbstractMatchStrategy`, implements `org.apache.shenyu.plugin.base.condition.strategy.MatchStrategy`, add annotation `org.apache.shenyu.spi.Join`.

```java
/** * This is custom match strategy.*/ @Join public class CustomMatchStrategy extends AbstractMatchStrategy implements MatchStrategy {
@Override public Boolean match(final List<ConditionData> conditionDataList, final ServerWebExchange exchange) {// custom match strategy}}
```

- In the project's META-INF/services directory, create `org.apache.shenyu.plugin.base.condition.strategy.MatchStrategy` file.

script

```shell
${spi name} = ${custom class path} 
```

`${spi name}` represents the name of `spi` and `${custom class path}` represents the fully qualified name of the class. Such as:

script

```shell
custom = xxx.xxx.xxx.CustomMatchStrategy 
```

- Package the project and copy it to the `lib` or `ext-lib` directory of the gateway (bootstrap-bin).
- In the `Apache ShenYu` gateway management system --> BasicConfig --> Dictionary, find the dictionary code as `MATCH_MODE`, add a new piece of data, pay attention to the dictionary name: `${spi name}`.

![](assets/images/custom-match-strategy-en_5afae2f47a0010e9.png)
> DictionaryType: `matchMode`;
>
> DictionaryCode: `MATCH_MODE`;
>
> DictionaryName: `${spi name}`, input your custom spi name;
>
> DictionaryValue: When used, the value of the drop-down box, do not repeat with the existing;
>
> DictionaryDescribe: desc your custom match strategy;
>
> Sort: to sort;
>
> Status: open or close.

- When adding selectors or rules, you can use custom MatchType:

![](assets/images/use-custom-match-strategy-en_88b4593dce179619.png)

---

<a id="developer-spi-custom-metrics-monitor"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/spi/custom-metrics-monitor/ -->

<!-- page_index: 108 -->

# Custom Metrics Monitor

Version: 2.7.0.3

- Before custom development, please customize and build the gateway environment first, please refer to: [custom deployment](#deployment-deployment-custom)
- This article describes how to customize the extension of `org.apache.shenyu.plugin.metrics.spi.MetricsService`.

- Create a new project and introduce the following dependencies:

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-plugin-base</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
</dependencies> 
```

- Create a new class `${you class}`，implements `org.apache.shenyu.plugin.metrics.spi.MetricsService`

```text
public class ${you class} implements MetricsService {
/** * Start metrics tracker.* * @param metricsConfig metrics config * @param metricsRegister the metrics register */ public void start(MetricsConfig metricsConfig, MetricsRegister metricsRegister){//your code}
/** * Stop metrics tracker.*/ public void stop() {//your code}}
```

- In the project `resources` directory，Create a new `META-INF/shenyu` directory， and the new file name is : `org.apache.shenyu.plugin.metrics.spi.MetricsService`.
  add `${you spi name}` = `${you class path}`:

```text
${you spi name} = ${you class path} 
```

- Package the project and copy it to the `lib` or `ext-lib` directory of the gateway (bootstrap-bin).
- In the `Admin` service ---> BasicConfig ---> Plugin , Find the `Monitor` plugin, edit config, pay attention to the `metricsName` name: `${you spi name}`.

![](/img/shenyu/custom/custom-metrics-monitor-en.jpg)

---

<a id="developer-spi-custom-mock-generator"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/spi/custom-mock-generator/ -->

<!-- page_index: 109 -->

# Custom Mock Data Generator

Version: 2.7.0.3

1. This article describes how to make custom extensions to `org.apache.shenyu.plugin.mock.generator.Generator`.
2. The mock data generation expression needs to satisfy the format of `${name|param1|param2|...}`

- Create a new project and introduce the following dependencies:

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-plugin-mock</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
</dependencies> 
```

- Create a new class `CustomerGenerator`，implements `org.apache.shenyu.plugin.mock.generator.Generator`。

```java
@Join public class CustomGenerator implements Generator<String> {@Override public String getName() {// The name of the generator, i.e. the content before the first | of the expression}
@Override public String generate() {// Implement the logic of data generation}
@Override public int getParamSize() {// The number of required parameters of the expression}
@Override public void initParam(List params, String rule) {// params is the contents except the name after the expression is split according to | // rule is the content of the original expression , if there is a custom parameter processing logic, you can use this parameter}
@Override public boolean match(String rule) {// Check if the current expression is valid}
@Override public String[] getPrefixAndSuffix() {// Return the prefix and suffix added after the generated content, please return a string array with two elements // 0th element is the prefix, 1st element is the suffix}}
```

- In the project `resources` directory，Create a new `META-INF/shenyu` directory， and the new file name is : `org.apache.shenyu.plugin.mock.generator.Generator`.
  add `${you spi name}` = `${you class path}`:

script

```shell
${spi name}=${custom class path} 
```

`${spi name}` represents the name of `spi`, `${spi name }` needs to be consistent with the definition of the getName() method in the Generator implementation class, `${custom class path}` represents the fully qualified name of the class. for example:

script

```shell
custom=xxx.xxx.xxx.CustomGenerator 
```

- Package the project and copy it to the `lib` or `ext-lib` directory of the gateway (bootstrap-bin).

---

<a id="developer-spi-custom-parameter-data"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/spi/custom-parameter-data/ -->

<!-- page_index: 110 -->

# Custom Parameter Data

Version: 2.7.0.3

This paper describes how to customize the extension of `org.apache.shenyu.plugin.base.condition.data.ParameterData`.

- Create a new project and introduce the following dependencies:

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-plugin-base</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
</dependencies> 
```

- Create a new class `CustomParameterData`, implements `org.apache.shenyu.plugin.base.condition.data.ParameterData`, add annotation `org.apache.shenyu.spi.Join`.

```java
/** * This is custom parameter data.*/ @Join public class CustomParameterData implements ParameterData {
@Override public String builder(final String paramName, final ServerWebExchange exchange) {// custom parameter data}}
```

- In the project's META-INF/services directory, create `org.apache.shenyu.plugin.base.condition.data.ParameterData` file, add key-value as following:

script

```shell
${spi name} = ${custom class path} 
```

`${spi name}` represents the name of `spi` and `${custom class path}` represents the fully qualified name of the class. Such as:

script

```shell
custom=xxx.xxx.xxx.CustomParameterData 
```

- Package the project and copy it to the `lib` or `ext-lib` directory of the gateway (bootstrap-bin).
- In the `Apache ShenYu` gateway management system --> BasicConfig --> Dictionary, find the dictionary code as `PARAM_TYPE`, add a new piece of data, pay attention to the dictionary name: `${spi name}`.

![](assets/images/custom-parameter-data-en_dd26431a67c03a12.png)
> DictionaryType: `paramType`;
>
> DictionaryCode: `PARAM_TYPE`;
>
> DictionaryName: `${spi name}`, input your custom spi name;
>
> DictionaryValue: When used, the value of the drop-down box, do not repeat with the existing;
>
> DictionaryDescribe: desc your custom match strategy;
>
> Sort: to sort;
>
> Status: open or close.

- When adding selectors or rules, you can use custom parameter data:

![](assets/images/use-custom-parameter-data-en_d90fe8de43b03701.png)

---

<a id="developer-spi-custom-predicate-judge"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/spi/custom-predicate-judge/ -->

<!-- page_index: 111 -->

# Custom Predicate Judge

Version: 2.7.0.3

- This paper describes how to customize the extension of `org.apache.shenyu.plugin.base.condition.judge.PredicateJudge`.
- The conditional predicate is the bridge between data and rules in the selector and serves to filter out requests that match the conditions.
- There are already seven conditional predicates including match, =, regex, contains, TimeBefore, TimeAfter, exclude.
- Please refer to [judge](https://github.com/apache/shenyu/tree/master/shenyu-plugin/shenyu-plugin-base/src/main/java/org/apache/shenyu/plugin/base/condition/judge) module, add your own conditional predicates, or submit `pr` to the official website if you have a good common plugin.

- Create a new project and introduce the following dependencies:

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-plugin-base</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
</dependencies> 
```

- Create a new class `CustomPredicateJudge`, implements `org.apache.shenyu.plugin.base.condition.judge.PredicateJudge`, add annotation `org.apache.shenyu.spi.Join`.

```java
/** * custom predicate judge.*/ @Join public class CustomPredicateJudge implements PredicateJudge {
@Override public Boolean judge(final ConditionData conditionData, final String realData) {// Custom Predicate Judge}}
```

- In the project's META-INF/services directory, create `org.apache.shenyu.plugin.base.condition.judge.PredicateJudge` file, add key-value as following:

script

```shell
${spi name} = ${custom class path} 
```

`${spi name}` represents the name of `spi` and `${custom class path}` represents the fully qualified name of the class. Such as:

script

```shell
custom=xxx.xxx.xxx.CustomPredicateJudge 
```

- Package the project and copy it to the `lib` or `ext-lib` directory of the gateway (bootstrap-bin).
- In the `Apache ShenYu` gateway management system --> BasicConfig --> Dictionary, find the dictionary code as `OPERATOR`, add a new piece of data, pay attention to the dictionary name: `${spi name}`.

![](assets/images/custom-predicate-judge-en_aca933ab06c811b8.png)
> DictionaryType: `operator`;
>
> DictionaryCode: `OPERATOR`;
>
> DictionaryName: `${spi name}`, input your custom spi name;
>
> DictionaryValue: When used, the value of the drop-down box, do not repeat with the existing;
>
> DictionaryDescribe: desc your custom match strategy;
>
> Sort: to sort;
>
> Status: open or close.

- When adding selectors or rules, you can use custom predicate judge:

![](assets/images/use-custom-predicate-judge-en_a79074d8a1f959a0.png)

- Add `GroovyPredicateJudge` and `SpELPredicateJudge` extension.

```java
/** * Groovy predicate judge.*/ @Join public class GroovyPredicateJudge implements PredicateJudge {
@Override public Boolean judge(final ConditionData conditionData, final String realData) {return (Boolean) Eval.me(conditionData.getParamName(), realData, conditionData.getParamValue());}}
```

```java
/** * SpEL predicate judge.*/ @Join public class SpELPredicateJudge implements PredicateJudge {
private static final ExpressionParser EXPRESSION_PARSER = new SpelExpressionParser();
@Override public Boolean judge(final ConditionData conditionData, final String realData) {Expression expression = EXPRESSION_PARSER.parseExpression(conditionData.getParamValue().replace('#' + conditionData.getParamName(), realData)); return expression.getValue(Boolean.class);}}
```

- Update `org.apache.shenyu.plugin.base.condition.judge.PredicateJudge`:

script

```shell
Groovy=xxx.xxx.xxx.GroovyPredicateJudge 
SpEL=xxx.xxx.xxx.SpELPredicateJudge 
```

---

<a id="developer-spi-custom-rate-limiter"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/spi/custom-rate-limiter/ -->

<!-- page_index: 112 -->

# Custom Rate Limiter

Version: 2.7.0.3

- Before custom development, please customize and build the gateway environment first, please refer to: [custom deployment](#deployment-deployment-custom).
- This article describes how to customize the extension of `org.apache.shenyu.plugin.ratelimiter.algorithm.RateLimiterAlgorithm` .

- Create a new project and introduce the following dependencies:

```xml
<dependencies> 
    <dependency> 
        <groupId>org.apache.shenyu</groupId> 
        <artifactId>shenyu-plugin-base</artifactId> 
        <version>${project.version}</version> 
    </dependency> 
</dependencies> 
```

- Create a new class `${you class}`, implements `org.apache.shenyu.plugin.ratelimiter.algorithm.RateLimiterAlgorithm`

```java
public class ${you class} implements RateLimiterAlgorithm<T> {
/** * Gets script.* * @return the script */ public RedisScript<T> getScript() {//coding and return}
/** * Gets keys.* * @param id the id * @return the keys */ public List<String> getKeys(String id) {//coding and return}
/** * Callback string.* * @param script the script * @param keys the keys * @param scriptArgs the script args */ public void callback(final RedisScript<?> script, final List<String> keys, final List<String> scriptArgs) {//coding and return}}
```

- In the project `resources` directory，Create a new `META-INF/shenyu` directory， and the new file name is : `org.apache.shenyu.plugin.ratelimiter.algorithm.RateLimiterAlgorithm`.
  add `${you spi name}` = `${you class path}`:

```text
${you spi name} = ${you class path} 
```

- Package the project and copy it to the `lib` or `ext-lib` directory of the gateway (bootstrap-bin).
- In the `Admin` service ---> BasicConfig ---> Dictionary , Find the dictionary code as `ALGORITHM_*`, add a new piece of data, pay attention to the dictionary name: `${you spi name}`.

![](assets/images/custom-rate-limiter-en_1001ed163a3321c1.jpg)

- Or execute the following custom `SQL` statement：

```sql
INSERT IGNORE INTO `shenyu_dict` ( 
        `id`, 
        `type`, 
        `dict_code`, 
        `dict_name`, 
        `dict_value`, 
        `desc`, 
        `sort`, 
        `enabled`, 
        `date_created`, 
        `date_updated` 
    ) 
VALUES ( 
        'you id', 
        'matchMode', 
        'MATCH_MODE', 
        'you spi name', 
        'you value', 
        'you spi name', 
        0, 
        1, 
        '2021-08-30 19:29:10', 
        '2021-08-30 20:15:23' 
    ); 
```

---

<a id="developer-custom-filter"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/custom-filter/ -->

<!-- page_index: 113 -->

# Custom Filter

Version: 2.7.0.3

- This doc shows a demo for how to extend `org.springframework.web.server.WebFliter`.

- `org.apache.shenyu.web.filter.CrossFilter` is designed for `WebFilter` implementation.

```java
public class CrossFilter implements WebFilter { 
 
    private static final String ALLOWED_HEADERS = "x-requested-with, authorization, Content-Type, Authorization, credential, X-XSRF-TOKEN,token,username,client"; 
 
    private static final String ALLOWED_METHODS = "*"; 
 
    private static final String ALLOWED_ORIGIN = "*"; 
 
    private static final String ALLOWED_EXPOSE = "*"; 
 
    private static final String MAX_AGE = "18000"; 
 
    @Override 
    @SuppressWarnings("all") 
    public Mono<Void> filter(final ServerWebExchange exchange, final WebFilterChain chain) { 
        ServerHttpRequest request = exchange.getRequest(); 
        if (CorsUtils.isCorsRequest(request)) { 
            ServerHttpResponse response = exchange.getResponse(); 
            HttpHeaders headers = response.getHeaders(); 
            headers.add("Access-Control-Allow-Origin", ALLOWED_ORIGIN); 
            headers.add("Access-Control-Allow-Methods", ALLOWED_METHODS); 
            headers.add("Access-Control-Max-Age", MAX_AGE); 
            headers.add("Access-Control-Allow-Headers", ALLOWED_HEADERS); 
            headers.add("Access-Control-Expose-Headers", ALLOWED_EXPOSE); 
            headers.add("Access-Control-Allow-Credentials", "true"); 
            if (request.getMethod() == HttpMethod.OPTIONS) { 
                response.setStatusCode(HttpStatus.OK); 
                return Mono.empty(); 
            } 
        } 
        return chain.filter(exchange); 
    } 
} 
```

- Registering `CrossFilter` as a `Spring Bean`.

- You can control the order by applying `@Order` to the implementation class .

```java
@Component @Order(-99) public final class HealthFilter implements WebFilter {
private static final String[] FILTER_TAG = {"/actuator/health", "/health_check"};
@Override public Mono<Void> filter(@Nullable final ServerWebExchange exchange, @Nullable final WebFilterChain chain) {ServerHttpRequest request = Objects.requireNonNull(exchange).getRequest(); String urlPath = request.getURI().getPath(); for (String check : FILTER_TAG) {if (check.equals(urlPath)) {String result = JsonUtils.toJson(new Health.Builder().up().build()); DataBuffer dataBuffer = exchange.getResponse().bufferFactory().wrap(result.getBytes()); return exchange.getResponse().writeWith(Mono.just(dataBuffer));}} return Objects.requireNonNull(chain).filter(exchange);}}
```

- Add a new class and inherit from `org.apache.shenyu.web.filter.AbstractWebFilter`.
- Implement abstract methods of parent class.

```java
/** * this is Template Method ,children Implement your own filtering logic.* * @param exchange the current server exchange * @param chain    provides a way to delegate to the next filter * @return {@code Mono<Boolean>} result：TRUE (is pass)，and flow next filter；FALSE (is not pass) execute doDenyResponse(ServerWebExchange exchange) */ protected abstract Mono<Boolean> doFilter(ServerWebExchange exchange, WebFilterChain chain);
/** * this is Template Method ,children Implement your own And response client.* * @param exchange the current server exchange.* @return {@code Mono<Void>} response msg.*/ protected abstract Mono<Void> doDenyResponse(ServerWebExchange exchange);
```

- if method `doFilter` returns `Mono<true>`, this filter is passing, While rejecting, it will call method `doDenyResponse` and sending infos in response body to frontend.

---

<a id="developer-custom-jwt-covert-algorithm"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/custom-jwt-covert-algorithm/ -->

<!-- page_index: 114 -->

# Custom Jwt convert Algorithm

Version: 2.7.0.3

- Users can customize the convert algorithm of `Jwt-plugin` to achieve convert.

The default implementation is `org.apache.shenyu.plugin.jwt.strategy.DefaultJwtConvertStrategy`. The SPI mechanism is adopted for extension, and the steps are as follows:

1. Implements interface `org.apache.shenyu.plugin.jwt.strategy.JwtConvertStrategy`


```java
/** * Represents a conversion strategy that convert jwt to some attributes of * serverWebExchange, especially attributes of the request header.*/ @SPI public interface JwtConvertStrategy {
/** * HandleJson needs to be parsed into jwtRuleHandle in order to * specify how to convert jwt.* * @param handleJson handleJson from rule * @return jwtRuleHandle */ JwtRuleHandle parseHandleJson(String handleJson);
/** * Converts jwt to some attributes of serverWebExchange based on jwtRuleHandle.* * @param jwtRuleHandle jwtRuleHandle * @param exchange      exchange * @param jwtBody       jwtBody * @return serverWebExchange */ ServerWebExchange convert(JwtRuleHandle jwtRuleHandle, ServerWebExchange exchange, Map<String, Object> jwtBody);
}
```


```java
 
    @Join 
    public class CustomJwtConvertStrategy implements JwtConvertStrategy { 
     
        @Override 
        public CustomJwtRuleHandle parseHandleJson(final String handleJson) { 
     
            return GsonUtils.getInstance().fromJson(handleJson, CustomJwtRuleHandle.class); 
        } 
     
        @Override 
        public ServerWebExchange convert(final JwtRuleHandle jwtRuleHandle, final ServerWebExchange exchange, final Map<String, Object> jwtBody) { 
            final CustomJwtRuleHandle customJwtRuleHandle = (CustomJwtRuleHandle) jwtRuleHandle; 
            String customConvert = customJwtRuleHandle.getCustomConvert(); 
            ServerHttpRequest modifiedRequest = 
                    exchange.getRequest().mutate().header("custom", customConvert).build(); 
     
            return exchange.mutate().request(modifiedRequest).build(); 
        } 
    } 
```

2. Configures SPI


```tex
custom=org.apache.shenyu.plugin.jwt.strategy.CustomJwtConvertStrategy 
```

The project would use different conversion strategies based on the`handleType` parameter of `JwtRuleHandle` . For example, for the following `JwtRuleHandle`,the project would use our above `CustomJwtConvertStrategy` . (Note: `handleType` is `default` or nonexistent, the project would use default `DefaultJwtConvertStrategy`)

```json
{ 
    "handleType":"custom", 
 	"customConvert":"customConvert" 
} 
```

The case code is available for viewing in `org.apache.shenyu.plugin.jwt.strategy.CustomJwtConvertStrategy`

---

<a id="developer-custom-parsing-ip-and-host"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/custom-parsing-ip-and-host/ -->

<!-- page_index: 115 -->

# Fetching Correct IP Address And Host

Version: 2.7.0.3

- This doc demonstrates how to get correct IP address and host when `Apache ShenYu` serves behind `nginx` reverse proxy.
- After fetched real `IP` and `host`, you can match them with plugins and selectors.

- The embedded implementation in `Apache ShenYu` is :`org.apache.shenyu.web.forward.ForwardedRemoteAddressResolver`.
- You need to config `X-Forwarded-For` in `nginx` first to get correct `IP address` and `host`.

- Declare a new class named `CustomRemoteAddressResolver` and implements `org.apache.shenyu.plugin.api.RemoteAddressResolver`.

```java
public interface RemoteAddressResolver {
/** * Resolve inet socket address.* * @param exchange the exchange * @return the inet socket address */ default InetSocketAddress resolve(ServerWebExchange exchange) {return exchange.getRequest().getRemoteAddress();}
}
```

- Register defined class as a `Spring Bean`.

```java
   @Bean 
   public SignService customRemoteAddressResolver() { 
         return new CustomRemoteAddressResolver(); 
   } 
```

---

<a id="developer-custom-plugin"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/custom-plugin/ -->

<!-- page_index: 116 -->

# Custom Plugin

Version: 2.7.0.3

- Plugins are core executors of `Apache ShenYu` gateway. Every plugin handles matched requests when enabled.
- There are two kinds of plugins in the `Apache ShenYu` gateway.
  - The first type is a chain with single responsibility, and can not custom filtering of traffic.
  - The other one can do its own chain of responsibility for matched traffic.
- You could reference from [shenyu-plugin](https://github.com/apache/shenyu/tree/master/shenyu-plugin) module and develop plugins by yourself. Please fire pull requests of your wonderful plugins without hesitate.

- Add following dependency:

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-plugin-api</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- Declare a new class named `MyShenyuPlugin` and implements `org.apache.shenyu.plugin.api.ShenyuPlugin`

```java
public interface ShenyuPlugin {
/** * Process the Web request and (optionally) delegate to the next * {@code WebFilter} through the given {@link ShenyuPluginChain}.* * @param exchange the current server exchange * @param chain    provides a way to delegate to the next filter * @return {@code Mono<Void>} to indicate when request processing is complete */ Mono<Void> execute(ServerWebExchange exchange, ShenyuPluginChain chain);
/** * return plugin order .* This attribute To determine the plugin execution order in the same type plugin.* * @return int order */ int getOrder();
/** * acquire plugin name.* this is plugin name define you must offer the right name.* if you impl AbstractShenyuPlugin this attribute not use.* * @return plugin name.*/ default String named() {return "";}
/** * plugin is execute.* if return true this plugin can not execute.* * @param exchange the current server exchange * @return default false.*/ default Boolean skip(ServerWebExchange exchange) {return false;}}
```

Detailed instruction of interface methods:

- `execute()` core method, you can do any task here freely.
- `getOrder()` get the order of current plugin.
- `named()` acquire the name of specific plugin that uses the `Camel Case`, eg: `dubbo`, `springCloud` .
- `skip()` determines whether this plugin should be skipped under certain conditions.
- Register plugin in `Spring` as a `Bean`, or simply apply `@Component` in implementation class.

```java
    @Bean 
    public ShenyuPlugin myShenyuPlugin() { 
        return new MyShenyuPlugin(); 
    } 
```

- The above is about writing a single responsibility plugin in Java. If you want to write plugins in another language, at least the language you are good at supporting `WASM`, you can find resources [here](https://shenyu.apache.org/docs/next/design/wasm-plugin-design/) . After you have learned about `WASM`, let's introduce the following dependency to build the Java part of the plugin:

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-plugin-wasm-api</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- Add a new class `MyShenyuWasmPlugin`, inherit from `org.apache.shenyu.plugin.wasm.api.AbstractWasmPlugin`

```java
package x.y.z; 
 
public class MyShenyuWasmPlugin extends AbstractWasmPlugin { 
     
    private static final Map<Long, String> RESULTS = new ConcurrentHashMap<>(); 
     
    @Override 
    public int getOrder() { 
        // your plugin order 
        return 0; 
    } 
     
    @Override 
    public String named() { 
        return "yourPluginName"; 
    } 
     
    @Override 
    protected Mono<Void> doExecute(final ServerWebExchange exchange, final ShenyuPluginChain chain, final Long argumentId) { 
        final String result = RESULTS.remove(argumentId); 
        // Results returned by calling other languages 
        return chain.execute(exchange); 
    } 
     
    @Override 
    protected Long getArgumentId(final ServerWebExchange exchange, final ShenyuPluginChain chain) { 
        // Need to generate unique IDs for parameters based on exchange and chain 
        return 0L; 
    } 
     
    @Override 
    protected Map<String, Func> initWasmCallJavaFunc(final Store<Void> store) { 
        Map<String, Func> funcMap = new HashMap<>(); 
        funcMap.put("get_args", WasmFunctions.wrap(store, WasmValType.I64, WasmValType.I64, WasmValType.I32, WasmValType.I32, 
            (argId, addr, len) -> { 
                // Callbacks for obtaining parameters from Java in other languages 
                String config = "hello from java " + argId; 
                LOG.info("java side->" + config); 
                ByteBuffer buf = super.getBuffer(); 
                for (int i = 0; i < len && i < config.length(); i++) { 
                    buf.put(addr.intValue() + i, (byte) config.charAt(i)); 
                } 
                return Math.min(config.length(), len); 
            })); 
        funcMap.put("put_result", WasmFunctions.wrap(store, WasmValType.I64, WasmValType.I64, WasmValType.I32, WasmValType.I32, 
            (argId, addr, len) -> { 
                // Callbacks that pass call results to Java in other languages 
                ByteBuffer buf = super.getBuffer(); 
                byte[] bytes = new byte[len]; 
                for (int i = 0; i < len; i++) { 
                    bytes[i] = buf.get(addr.intValue() + i); 
                } 
                String result = new String(bytes, StandardCharsets.UTF_8); 
                RESULTS.put(argId, result); 
                LOG.info("java side->" + result); 
                return 0; 
            })); 
        return funcMap; 
        } 
    } 
```

- Create projects in other languages, using the Rust language as an example:

```shell
cd {shenyu}/shenyu-plugin/{your_plugin_moodule}/src/main 
cargo new --lib your_plugin_name 
```

- Add `execute` method in `lib.rs`:

```rust
#[link(wasm_import_module = "shenyu")] 
extern "C" { 
    fn get_args(arg_id: i64, addr: i64, len: i32) -> i32; 
 
    fn put_result(arg_id: i64, addr: i64, len: i32) -> i32; 
} 
 
// Adding `#[no_mangle]` to prevent the Rust compiler from modifying method names is mandatory 
#[no_mangle] 
pub unsafe extern "C" fn execute(arg_id: i64) { 
    let mut buf = [0u8; 32]; 
    let buf_ptr = buf.as_mut_ptr() as i64; 
    eprintln!("rust side-> buffer base address: {}", buf_ptr); 
    // Get parameters from Java 
    let len = get_args(arg_id, buf_ptr, buf.len() as i32); 
    let java_arg = std::str::from_utf8(&buf[..len as usize]).unwrap(); 
    eprintln!("rust side-> recv:{}", java_arg); 
    // Add plugin logic for the Rust section here, such as rpc calls, etc 
    // Pass the call result of rust to Java 
    let rust_result = "rust result".as_bytes(); 
    let result_ptr = rust_result.as_ptr() as i64; 
    _ = put_result(arg_id, result_ptr, rust_result.len() as i32); 
} 
```

- Add `[lib]` to `Cargo.toml` and change `crate-type` to `["cdylib"]`. Ultimately, your `Cargo.toml` should look like:

```toml
[package] 
name = "your_plugin_name" 
version = "0.1.0" 
edition = "2021" 
 
[dependencies] 
# ...... 
 
[lib] 
crate-type = ["cdylib"] 
```

- Generate the wasm file：

```shell
cargo build --target wasm32-wasi --release 
```

- You will see `{shenyu}/shenyu-plugin/{your_plugin_moodule}/src/main/{your_plugin_name}/target/wasm32-wasi/release/{your_plugin_name}.wasm`, then rename it, due to the `x.y.z.MyShenyuWasmPlugin`，the final wasm file name should be `x.y.z.MyShenyuWasmPlugin.wasm`, finally, put the wasm file in the `resources` folder of your plugin module.

- Introduce the following dependency:

```xml
 <dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-plugin-base</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- Add a new class `CustomPlugin`, inherit from `org.apache.shenyu.plugin.base.AbstractShenyuPlugin`
- examples down below:

```java
/** * This is your custom plugin.* He is running in after before plugin, implement your own functionality.* extends AbstractShenyuPlugin so you must user shenyu-admin And add related plug-in development.* * @author xiaoyu(Myth) */ public class CustomPlugin extends AbstractShenyuPlugin {
/** * return plugin order .* The same plugin he executes in the same order.* * @return int */ @Override public int getOrder() {return 0;}
/** * acquire plugin name.* return you custom plugin name.* It must be the same name as the plug-in you added in the admin background.* * @return plugin name.*/ @Override public String named() {return "shenYu";}
/** * plugin is execute.* Do I need to skip.* if you need skip return true.* * @param exchange the current server exchange * @return default false.*/ @Override public Boolean skip(final ServerWebExchange exchange) {return false;}
/** * this is Template Method child has Implement your own logic.* * @param exchange exchange the current server exchange * @param chain    chain the current chain * @param selector selector * @param rule     rule * @return {@code Mono<Void>} to indicate when request handling is complete */ @Override protected abstract Mono<Void> doExecute(ServerWebExchange exchange, ShenyuPluginChain chain, SelectorData selector, RuleData rule) {LOGGER.debug(".......... function plugin start.............."); /* * Processing after your selector matches the rule.* rule.getHandle() is you Customize the json string to be processed.* for this example.* Convert your custom json string pass to an entity class.*/ final String ruleHandle = rule.getHandle();
final Test test = GsonUtils.getInstance().fromJson(ruleHandle, Test.class);
/* * Then do your own business processing.* The last execution  chain.execute(exchange).* Let it continue on the chain until the end.*/ System.out.println(test.toString()); return chain.execute(exchange);}}
```

- Detailed explanation:

  - Plugins will match the selector rule for customized plugins inherit from this abstract class.
  - Firstly define a new plugin in `shenyu-admin` –> BasicConfig –> Plugin, please mind that your plugin name should match the `named()` method overridden in your class.
  - Re-login `shenyu-admin`, the plugin you added now showing on plugin-list page, you can choose selectors for matching.
  - There is a field named `handler` in rules, it is customized json string to be processed. You can process data after acquiring a ruleHandle (`final String ruleHandle = rule.getHandle();`) in `doExecute()` method.
- Register plugin in `Spring` as a `Bean`, or simply apply `@Component` in implementation class.

```java
    @Bean 
    public ShenyuPlugin customPlugin() { 
        return new CustomPlugin(); 
    } 
```

- The general logic is similar to [Single Responsibility Plugin in Multiple Languages](#Single Responsibility Plugin in Multiple Languages) , but the dependency in Java and the methods that need to be added in other languages are different from `Single Responsibility Plugin in Multiple Languages`. The following are the dependency required for the Java part of the `Multi Language Matching Traffic Processing Plugin`:

```xml
<dependency> 
    <groupId>org.apache.shenyu</groupId> 
    <artifactId>shenyu-plugin-wasm-base</artifactId> 
    <version>${project.version}</version> 
</dependency> 
```

- The following are the methods that must be added (using the Rust language as an example):

```rust
#[no_mangle] 
pub unsafe extern "C" fn doExecute(arg_id: i64) { 
    //...... 
} 
```

- The following are optional methods (using the Rust language as an example):

```rust
#[no_mangle] pub unsafe extern "C" fn before(arg_id: i64) {//......}
#[no_mangle] pub unsafe extern "C" fn after(arg_id: i64) {//......}
```

- Declare a new class named `PluginDataHandler` and implements `org.apache.shenyu.plugin.base.handler.PluginDataHandler`

```java
public interface PluginDataHandler {
/** * Handler plugin.* * @param pluginData the plugin data */ default void handlerPlugin(PluginData pluginData) {}
/** * Remove plugin.* * @param pluginData the plugin data */ default void removePlugin(PluginData pluginData) {}
/** * Handler selector.* * @param selectorData the selector data */ default void handlerSelector(SelectorData selectorData) {}
/** * Remove selector.* * @param selectorData the selector data */ default void removeSelector(SelectorData selectorData) {}
/** * Handler rule.* * @param ruleData the rule data */ default void handlerRule(RuleData ruleData) {}
/** * Remove rule.* * @param ruleData the rule data */ default void removeRule(RuleData ruleData) {}
/** * Plugin named string.* * @return the string */ String pluginNamed();
}
```

- Ensure `pluginNamed()` is same as the plugin name you defined.
- Register defined class as a `Spring Bean`, or simply apply `@Component` in implementation class.

```java
@Bean 
public PluginDataHandler pluginDataHandler() { 
  return new PluginDataHandler(); 
} 
```

- When using this feature, the above extensions `ShenyuPlugin`, `PluginDataHandler`, do not need to be `spring bean`. You just need to build the jar package of the extension project.
- Config in Yaml：

```yaml
shenyu: 
  extPlugin: 
    path:  //Load the extension plugin jar package path 
    enabled: true //Whether to turn on  
    threads: 1  //Number of loading plug-in threads 
    scheduleTime: 300  //Cycle time (in seconds) 
    scheduleDelay: 30 //How long the shenyu gateway is delayed to load after it starts (in seconds) 
```

- This path is for the directory where the extended plugin jar package is stored。
- Used `-Dplugin-ext=xxxx`, Also used `shenyu.extPlugin.path` in yaml，If neither is configured, the `ext-lib` directory in the apache shenyu gateway boot path will be loaded by default.
- Priority ：`-Dplugin-ext=xxxx` > `shenyu.extPlugin.path` > `ext-lib(default)`

- To use this feature, you will need to package the `ShenyuPlugin` extension as a custom ShenyuPlugin Jar
- Configure it in ShenyuAdmin
  - use `ShenyuAdmin - BasicConfig - Plugin` add plugin in `pluginJar` click upload button
- Custom ShenyuPlugin can be started by loading third-party jars into the `-cp` directory if it depends on other third-party packages in shenyu-bootstrap

Tips:

The Upload jar package plugin supports hot loading
If you need to modify the jar online. You can make a new jar. And raise the version number, for example '1.0.1' to '1.0.2'

---

<a id="developer-custom-result"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/custom-result/ -->

<!-- page_index: 117 -->

# Custom Response

Version: 2.7.0.3

- This doc offers examples for customising response structure in `Apache ShenYu` gateway.
- The response body structure in gateways should be unified, it is recommended for specify yours.

- The default implementation class is `org.apache.shenyu.plugin.api.result.DefaultShenyuResult`.
- Following is the response structure:

```java
public class ShenyuDefaultEntity implements Serializable { 
 
    private static final long serialVersionUID = -2792556188993845048L; 
 
    private Integer code; 
 
    private String message; 
 
    private Object data; 
 
} 
```

- The returned `json` as follows:

```json
{ 
    "code": -100, //response code, 
    "message": "Your parameter error, please check the relevant documentation!", //hint messages 
    "data": null  // business data 
} 
```

- Declare a new class named `CustomShenyuResult` and implements `org.apache.shenyu.plugin.api.result.ShenyuResult`

```java
/** * The interface shenyu result.*/ public interface ShenyuResult<T> {
/** * The response result.* * @param exchange the exchange * @param formatted the formatted object * @return the result object */ default Object result(ServerWebExchange exchange, Object formatted) {return formatted;}
/** * format the origin, default is json format.* * @param exchange the exchange * @param origin the origin * @return format origin */ default Object format(ServerWebExchange exchange, Object origin) {// basic data if (ObjectTypeUtils.isBasicType(origin)) {return origin;} // error result or rpc origin result.return JsonUtils.toJson(origin);}
/** * the response context type, default is application/json.* * @param exchange the exchange * @param formatted the formatted data that is origin data or byte[] convert string * @return the context type */ default MediaType contentType(ServerWebExchange exchange, Object formatted) {return MediaType.APPLICATION_JSON;}
/** * Error t.* * @param code    the code * @param message the message * @param object  the object * @return the t */ T error(int code, String message, Object object);}
```

> Processing sequence: `format`->`contextType`->`result`. The `format` method performs data formatting. If the data is a basic type and returns itself, other types are converted to `JSON`, and the parameter `origin` is the original data. Formatting can be performed according to the situation. `contextType`, if it is a basic type, use `text/plain`, the default is `application/json`, the parameter `formatted` is the data processed by the `format` method, and can be combined with the return result of `format` for data type Define processing. The parameter `formatted` of `result` is the data processed by the `format` method, which returns to itself by default, and can be combined with the return result of `format` for custom processing of the data type.

- `T` is a generic parameter for your response data.
- Register defined class as a `Spring Bean`.

```java
@Bean 
public ShenyuResult<?> customShenyuResult() { 
    return new CustomShenyuResult(); 
} 
```

---

<a id="developer-custom-sign-algorithm"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/custom-sign-algorithm/ -->

<!-- page_index: 118 -->

# Custom Sign Algorithm

Version: 2.7.0.3

- Users can customize the signature authentication algorithm to achieve verification.

- The default implementation is `org.apache.shenyu.plugin.sign.service.ComposableSignService`.


```java
@Bean 
@ConditionalOnMissingBean(value = SignService.class, search = SearchStrategy.ALL) 
public SignService signService() { 
    return new ComposableSignService(new DefaultExtractor(), new DefaultSignProvider()); 
} 
```

- Declare a new class named `CustomSignService` and implements `org.apache.shenyu.plugin.plugin.sign.service`.

```java
public interface SignService {
/** * Gets verifyResult.* @param exchange exchange * @param requestBody requestBody * @return result */ VerifyResult signatureVerify(ServerWebExchange exchange, String requestBody);
/** * Gets verifyResult.* @param exchange exchange * @return result */ VerifyResult signatureVerify(ServerWebExchange exchange);}
```

- When returning is `isSuccess()` of VerifyResult, the sign verification passes. If there's false, the `getReason()` of VerifyResult will be return to the frontend to show.
- Register defined class as a Spring Bean.

```java
   @Bean 
   public SignService customSignService() { 
         return new CustomSignService(); 
   } 
```

---

<a id="developer-developer-shenyu-client"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/developer-shenyu-client/ -->

<!-- page_index: 119 -->

# A multilingual HTTP client

Version: 2.7.0.3

- This document focuses on how to access gateways for `HTTP` services in other languages.
- To access the gateway, you need to get the token first, and then you can call the registration service or metadata interface according to your needs.

- **Request Method**

  `GET`
- **Request Path**

  - `http://{shenyu-admin}/platform/login`
  - Where `shenyu-admin` is the `ip + port` of the `admin` backend management system.
- **Request Params**

  - `query` parameter, the account password is the username and password of the admin service.
| Field | Type | Required | Desc |
| --- | --- | --- | --- |
| userName | String | Yes | shenyu admin account |
| password | String | Yes | shenyu admin password |

- **Return Data**


| Field |  | Type | Desc |
| --- | --- | --- | --- |
| code |  | Integer | Return code |
| message |  | String | Return message |
| data |  | Object | Return data |
|  | id | Integer | user id |
|  | userName | String | account |
|  | role | Integer | role id |
|  | enabled | Boolean | status |
|  | dateCreated | String | create time |
|  | dateUpdated | String | update time |
|  | token | String | token |
|  | expiredTime | Long | timeout time, in milliseconds |

  **Example**


```json
{"code": 200,"message": "login dashboard user success","data": {"id": "1","userName": "admin","role": 1,"enabled": true,"dateCreated": "2022-09-07 22:08:23","dateUpdated": "2022-09-07 22:08:23","token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyTmFtZSI6ImFkbWluIiwiZXhwIjoxNjYyNjQ2MzU5fQ.WBXBgCcGsnnC00pRbDOtqCVoAaZr8MKH6WE6kY-NGaI","expiredTime": 86400000}}
```

- **Request Method**

  `POST`
- **Request Path**

  - `http://{shenyu-admin}/shenyu-client/register-uri`
  - Where `shenyu-admin` is the `ip + port` of the `admin` backend management system.

- **Request Params**

  - `Header`

    - `contentType: application/json`
    - `X-Access-Token: {token}`，token is the token obtained by `Get token`.
  - `Body`，`json` format


| Field | Type | Required | Desc |
| --- | --- | --- | --- |
| protocol | String | Yes | protocol type |
| appName | String | Yes | app name |
| contextPath | String | Yes | service path |
| rpcType | String | Yes | rpc type, supported type reference [RpcTypeEnum](https://github.com/apache/shenyu/blob/master/shenyu-common/src/main/java/org/apache/shenyu/common/enums/RpcTypeEnum.java) |
| host | String | Yes | service IP |
| port | Integer | Yes | service port |
| eventType | String | Yes | event type, supported types reference [EventType](https://github.com/apache/shenyu/blob/master/shenyu-register-center/shenyu-register-common/src/main/java/org/apache/shenyu/register/common/enums/EventType.java) |

  **Example**


```json
{"protocol": "http","appName": "app","contextPath": "/test","rpcType": "http","host": "127.0.0.1","port": "8080","eventType": "REGISTER"}
```

- **Return Data**

  A successful registration returns `success`.

- **Request Method**

  `POST`
- **Request Path**

  - `http://{shenyu-admin}/shenyu-client/register-metadata`
  - Where `shenyu-admin` is the `ip + port` of the `admin` backend management system.
- **Request Params**

  - `Header`

    - `contentType: application/json`
    - `X-Access-Token: {token}`，token is the token obtained by `Get token`.
  - `Body`，`json` format.


| Field | Type | Required | Desc |
| --- | --- | --- | --- |
| appName | String | Yes | app name |
| contextPath | String | Yes | service path |
| path | String | Yes | path |
| pathDesc | String | Yes | path description |
| rpcType | String | Yes | rpc type, supported type reference [RpcTypeEnum](https://github.com/apache/shenyu/blob/master/shenyu-common/src/main/java/org/apache/shenyu/common/enums/RpcTypeEnum.java) |
| serviceName | String | Yes | service name |
| methodName | String | Yes | method name |
| ruleName | String | Yes | rule name |
| parameterTypes | String | Yes | parameter Type |
| rpcExt | String | Yes | rpc expansion parameters |
| enabled | Boolean | No | status |
| host | String | Yes | service IP |
| port | Integer | Yes | service port |
| pluginNames | List | No | plugin name list |
| registerMetaData | Boolean | No | whether to register metadata |

    **examples**


```json
{ 
    "appName": "app", 
    "contextPath": "/", 
    "path": "/test", 
    "rpcType": "http", 
    "serviceName": "test service", 
    "parameterTypes": "java.lang.String", 
    "pathDesc": "test path", 
    "methodName": "test method", 
    "ruleName": "test rule", 
    "rpcExt": "{\"loadbalance\":\"hash\",\"retries\":3,\"timeout\":-1}", 
    "enabled": true, 
    "host": "127.0.0.1", 
    "port": 8080, 
    "pluginNames": [], 
    "registerMetaData": true 
} 
```

- **Return Data**

  A successful registration returns `success`.

---

<a id="developer-file-and-image"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/file-and-image/ -->

<!-- page_index: 120 -->

# File Upload And Download

Version: 2.7.0.3

- This doc gives a brief description for upload and download files using `Apache ShenYu`.

- The default file size limit is `10M`.
- For custom limitation, use`--file.size` with an integer variable. e.g.`--file.size = 30`
- Upload your files just as way you did before

- `Apache ShenYu` supports download files in stream. There is no need to change anything.

---

<a id="developer-integration-test"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/integration-test/ -->

<!-- page_index: 121 -->

# Run Integration Test Locally

Version: 2.7.0.3

1. Clone the code of [Apache ShenYu](https://github.com/apache/shenyu).
2. Install and start docker.

1. Build with Maven

```shell
./mvnw -B clean install -Prelease,docker -Dmaven.javadoc.skip=true -Dmaven.test.skip=true 
```

2. Build integrated tests

```shell
./mvnw -B clean install -Pit -DskipTests -f ./shenyu-integrated-test/pom.xml 
```

3. Start docker compose

```shell
docker-compose -f ./shenyu-integrated-test/${{ matrix.case }}/docker-compose.yml up -d 
```

> You need to replace `${{ matrix.case }}` with the exact directory, such as `shenyu-integrated-test-http`.

4. Run test

```shell
./mvnw test -Pit -f ./shenyu-integrated-test/${{ matrix.case }}/pom.xml 
```

---

<a id="developer-local-model"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/local-model/ -->

<!-- page_index: 122 -->

# Local Model

Version: 2.7.0.3

- Standalone environment, then use the local `API` to update the apache shenyu gateway data.the yaml config:

```yaml
shenyu: 
  local: 
    enabled: true 
    sha512Key: 123456 
```

- Common result:

> [!TIP]
> **success**
>

- Common preFix: `localhost:9095/shenyu`
- Common Header: `localKey: 123456`

save or update plugin data

POST

/plugin/saveOrUpdate

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **PluginData** | [PluginData](#developer-local-model--plugindata) | True |  | Plugin data object (pass Json object inside Body) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **id** | String | False |  | plugin id |
| **name** | String | True |  | plugin name |
| **config** | String | False |  | plugin configuration (Json format) |
| **role** | String | False |  | plugin role |
| **enabled** | Boolean | False |  | whether to turn on |

POST body

```text
{"id":3,"name":"divide","enabled":"true"} 
 
```

Clear all data (plugins, selectors, rules)

GET

/cleanAll

Clear plugin data（selector, rule）

GET

/cleanPlugin?name = xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **name** | String | true |  | plugin name |

Remove plugin data (not included, the selectors and rules data)

GET

/plugin/delete?name = xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **name** | String | true |  | plugin name |

Remove all plugin data (not included, the selectors and rules data)

GET

/plugin/deleteAll

Find plugin by name

GET

/plugin/findByName?name=xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **name** | String | true |  | plugin name |

Save or Update Selector

POST

/plugin/selector/saveOrUpdate

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **SelectorData** | [SelectorData](#developer-local-model--selectordata) | True |  | Selector object (pass Json object inside Body) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **id** | String | False |  | selector id |
| **pluginName** | String | True |  | plugin name |
| **name** | String | False |  | Selector name (default is plugin:selector+random number if not filled) |
| **matchMode** | Integer | False |  | Matching mode (0:and;1:or), not filled with the default generation And mode |
| **type** | Integer | False |  | Traffic type（0: full traffic; 1: custom traffic) do not fill in the default generation of full traffic |
| **sort** | Integer | False |  | Sort by, not filled by default generate 10 |
| **enabled** | Boolean | False |  | Whether to turn on, not fill in the default generation true |
| **logged** | Boolean | False |  | Whether or not to print the log, do not fill in the default generated into false |
| **handle** | String | False |  | Selector handler (Json objects, depending on each plug-in, different objects are passed) |
| **conditionList** | [Condition](#developer-local-model--condition) | False |  | Conditional collection, custom traffic needs to be passed, full traffic does not need to be passed (Json List object) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **paramType** | String | True |  | param type（post，uri，query，host，header，cookie，req\_method，domain） |
| **operator** | String | True |  | operator （match，=，regex，>，<，contains，SpEL，Groovy，TimeBefore，TimeAfter） |
| **paramName** | String | False |  | param mame（The uri parameter type can be passed without） |
| **paramValue** | Integer | False |  | param value |

POST body

```text
{"pluginName": "divide","type": 1,"handle": "[{\"upstreamUrl\":\"127.0.0.1:8089\"}]","conditionDataList": [{"paramType": "uri","operator": "match","paramName": null,"paramValue": "/**" }]}
```

Is selector id

```text
xxxxx 
```

Add a selector with multiple rules

POST

/plugin/selectorAndRules

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **SelectorRulesData** | [SelectorRulesData](#developer-local-model--selectorrulesdata) | True |  | Selector rule object (Body inside pass Json object) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **pluginName** | String | True |  | plugin name |
| **selectorName** | String | False |  | Selector name (if not filled in, it is generated by default plugin:selector+random number) |
| **matchMode** | Integer | False |  | Matching mode (0:and;1:or), not filled with the default generation And mode |
| **selectorHandler** | String | False |  | Selector handler (Json objects, depending on each plug-in, different objects are passed) |
| **conditionList** | [ConditionData](#developer-local-model--conditiondata) | True |  | Selector condition collection (Json List object) |
| **ruleDataList** | [RuleLocalData](#developer-local-model--rulelocaldata) | True |  | Rule condition collection (Json List object) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **ruleName** | String | False |  | rule name |
| **ruleHandler** | String | True |  | Rule handler (different plugins pass different values)） |
| **matchMode** | Integer | False |  | Matching pattern (0:and;1:or) |
| **conditionList** | [ConditionData](#developer-local-model--conditiondata) | True |  | Rule condition collection (Json List object) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **paramType** | String | True |  | param type（post，uri，query，host，header，cookie，req\_method，domain） |
| **operator** | String | True |  | operator （match，=，regex，>，<，contains，SpEL，Groovy，TimeBefore，TimeAfter） |
| **paramName** | String | False |  | param mame（The uri parameter type can be passed without） |
| **paramValue** | Integer | False |  | param value |

POST body

```text
{"pluginName": "divide","selectorHandler": "[{\"upstreamUrl\":\"127.0.0.1:8089\"}]","conditionDataList": [{"paramType": "uri","operator": "match","paramValue": "/http/**" }],"ruleDataList": [{"ruleHandler": "{\"loadBalance\":\"random\"}","conditionDataList": [{"paramType": "uri","operator": "=","paramValue": "/http/test/payment" }] }, {"ruleHandler": "{\"loadBalance\":\"random\"}","conditionDataList": [{"paramType": "uri","operator": "=","paramValue": "/http/order/save" }] }]}
```

Delete selectors based on selector id and plugin name

GET

/plugin/selector/delete?pluginName=xxxx&&id=xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **pluginName** | String | true |  | plugin name |
| **id** | String | true |  | selector id |

Get all selectors by plugin name

GET

/plugin/selector/findList?pluginName=xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **pluginName** | String | true |  | plugin name |

Save or Update Rule Data

POST

/plugin/rule/saveOrUpdate

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **RuleData** | [RuleData](#developer-local-model--ruledata) | True |  | Rule object (pass Json object inside Body) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **id** | String | False |  | rule id |
| **pluginName** | String | True |  | plugin name |
| **name** | String | False |  | Rule name (default generation if not filled plugin:rule+random number) |
| **selectorId** | String | True |  | Selector id |
| **matchMode** | Integer | False |  | Matching mode (0:and;1:or), not filled with the default generation And mode |
| **sort** | Integer | False |  | Sort by , not filled by default generate 10 |
| **enabled** | Boolean | False |  | Whether to turn on, not fill in the default generation true |
| **logged** | Boolean | False |  | Whether or not to print the log, do not fill in the default generated into false |
| **handle** | String | False |  | Rule handler (Json objects, depending on each plug-in, different objects are passed) |
| **conditionList** | [ConditionData](#developer-local-model--conditiondata) | False |  | Conditional collections (Json List objects) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **paramType** | String | True |  | param type（post，uri，query，host，header，cookie，req\_method，domain） |
| **operator** | String | True |  | operator （match，=，regex，>，<，contains，SpEL，Groovy，TimeBefore，TimeAfter） |
| **paramName** | String | False |  | param mame（The uri parameter type can be passed without） |
| **paramValue** | Integer | False |  | param value |

POST body

```text
{"pluginName": "divide","selectorId": 123456,"handle": "{\"loadBalance\":\"random\"}","conditionDataList": [{"paramType": "uri","operator": "=","paramValue": "/test" }]}
```

Is rule id

```text
xxxxx 
```

Delete rules based on selector id and rule id

GET

/plugin/rule/delete?selectorId=xxxx&&id=xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **selectorId** | String | true |  | selector ID |
| **id** | String | true |  | rule ID |

Get all rules by selector ID

GET

/plugin/rule/findList?selectorId=xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **selectorId** | String | true |  | selector id |

Save Or Update Meta data

POST

/meta/saveOrUpdate

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **MetaData** | [MetaData](#developer-local-model--metadata) | True |  | Metadata object (pass Json object inside Body) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **id** | String | False |  | ID |
| **appName** | String | True |  | app name |
| **contextPath** | String | True |  | contextPath |
| **path** | String | True |  | path |
| **rpcType** | String | True |  | rpc type（dubbo，sofa，tars，springCloud，motan，grpc） |
| **serviceName** | String | True |  | service name |
| **methodName** | String | True |  | method name |
| **parameterTypes** | String | True |  | parameter types |
| **rpcExt** | String | False |  | rpc extension parameters (json objects) |
| **enabled** | Boolean | False |  | Whether to turn on |

Delete Meta data

GET

/meta/delete?rpcType=xxxx&&path=xxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **rpcType** | String | true |  | rpc type（dubbo，sofa，tars，springCloud，motan，grpc） |
| **path** | String | true |  | path |

Save Or Update App Sign Data

POST

/auth/saveOrUpdate

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **AppAuthData** | [AppAuthData](#developer-local-model--appauthdata) | True |  | Signature object (Json object passed inside the Body) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **appKey** | String | True |  | app key |
| **appSecret** | String | True |  | app secret |
| **enabled** | Boolean | False |  | Whether to turn on |
| **open** | Boolean | False |  | is open |
| **paramDataList** | [AuthParamData](#developer-local-model--authparamdata) | false |  | Parameter set, open is true when you need to pass (Json list object) |
| **AuthPathData** | [AuthPathData](#developer-local-model--authpathdata) | false |  | Path collection, open is true when you need to pass (Json list object) |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **appName** | String | True |  | app name |
| **appParam** | String | True |  | app param |

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **appName** | String | True |  | app name |
| **path** | String | True |  | path |
| **enabled** | Boolean | False |  | Whether to turn on |

Delete App Sign Data

GET

/auth/delete?appKey=xxxx

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| **appKey** | String | true |  | app key |

---

<a id="developer-notice-alert"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/notice-alert/ -->

<!-- page_index: 123 -->

# Alarm Notice

Version: 2.7.0.3

- This doc gives a brief description for send alarm notice message using `Apache ShenYu API`.

- Config the gateway `application.yml`

```yaml
shenyu: 
  alert: 
    enabled: true 
    # the shenyu admin servers, if admin cluster, config like 127.0.0.1:9095,192.3.4.2:9095 
    admins: localhost:9095 
```

- We can send custom alarm message in plugin using `AlarmSender.alarm()`

Refer below:

```java
public class ParamMappingPlugin extends AbstractShenyuPlugin { 
 
    @Override 
    public Mono<Void> doExecute(final ServerWebExchange exchange, final ShenyuPluginChain chain, final SelectorData selector, final RuleData rule) { 
        ParamMappingRuleHandle paramMappingRuleHandle = ParamMappingPluginDataHandler.CACHED_HANDLE.get().obtainHandle(CacheKeyUtils.INST.getKey(rule)); 
      
        if(some condition) { 
             Map<String, String> labels = new HashMap<>(8); 
             labels.put("plugin", "http-redirect"); 
             labels.put("component", "http"); 
             AlarmSender.alarmHighEmergency("alarm-title", "alarm-content", labels); 
             AlarmSender.alarmMediumCritical("alarm-title", "alarm-content", labels); 
             AlarmSender.alarmLowWarning("alarm-title", "alarm-content", labels); 
             AlarmSender.alarm((byte) 0, "alarm-title", "alarm-content"); 
        } 
       
        HttpHeaders headers = exchange.getRequest().getHeaders(); 
        MediaType contentType = headers.getContentType(); 
        return match(contentType).apply(exchange, chain, paramMappingRuleHandle); 
    } 
} 
```

- In the previous step, we send custom alarm message in plugin.
- Now we configure how these messages are sent to whom(tom,lili...) by which type(email,DingDing...)
- Config this in ShenYu Admin Dashboard.

![alarm-config](assets/images/alarm-config-b93b5e5f2e8b71d5c79a49a07398e674_6e562dbe06a24654.png)

Have fun!

1. If you use the email notice, you should config your email send server in ShenYu Admin `application.yml`

```yaml
spring: 
  mail: 
    # Attention: this is mail server address. 
    host: smtp.qq.com 
    username: shenyu@apache.com 
    # Attention: this is not email account password, this requires an email authorization code 
    password: your-password 
    port: 465 
    default-encoding: UTF-8 
    properties: 
      mail: 
        smtp: 
          socketFactoryClass: javax.net.ssl.SSLSocketFactory 
          ssl: 
            enable: true 
```

---

<a id="developer-shenyu-optimize"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/shenyu-optimize/ -->

<!-- page_index: 124 -->

# ShenYu Optimize

Version: 2.7.0.3

- This doc shows how to do performance optimization for Apache ShenYu.

- Apache ShenYu is JVM driven and processing time for a single request is nearly between `1-3` ms.

- `spring-webflux` is one of dependencies of ShenYu, and it uses Netty in lower layer.
- The demo down below demonstrates tuning ShenYu by customizing params in Netty.

```java
@Bean 
 public NettyReactiveWebServerFactory nettyReactiveWebServerFactory() { 
     NettyReactiveWebServerFactory webServerFactory = new NettyReactiveWebServerFactory(); 
     webServerFactory.addServerCustomizers(new EventLoopNettyCustomizer()); 
     return webServerFactory; 
 } 
 
private static class EventLoopNettyCustomizer implements NettyServerCustomizer { 
 
    @Override 
    public HttpServer apply(final HttpServer httpServer) { 
        return httpServer 
                .tcpConfiguration(tcpServer -> tcpServer 
                        .runOn(LoopResources.create("shenyu-netty", 1, DEFAULT_IO_WORKER_COUNT, true), false) 
                        .selectorOption(ChannelOption.SO_REUSEADDR, true) 
                        .selectorOption(ChannelOption.ALLOCATOR, PooledByteBufAllocator.DEFAULT) 
                        .option(ChannelOption.TCP_NODELAY, true) 
                        .option(ChannelOption.ALLOCATOR, PooledByteBufAllocator.DEFAULT)); 
    } 
} 
```

- The `shenyu-bootstrap` module offers this class, you may modify it when benchmarking your app if necessary.
- You can get references of business thread model from [thread model](#developer-thread-model)

---

<a id="developer-thread-model"></a>

<!-- source_url: https://shenyu.apache.org/docs/developer/thread-model/ -->

<!-- page_index: 125 -->

# Thread Model

Version: 2.7.0.3

- This article gives an introduction to thread models in ShenYu and usage in various scenarios.

- `spring-webflux` is one of dependencies of ShenYu, and it uses Netty thread model in lower layer.

- Use scheduling thread to execute by default.
- A fixed thread pool manages business threads, the number of threads is count in this formula: cpu \* 2 + 1.

- `reactor.core.scheduler.Schedulers`.
- `-Dshenyu.scheduler.type=fixed` is a default config. If set to other value, a flexible thread pool will take place it.`Schedulers.elastic()`.
- `-Dshenyu.work.threads = xx` is for configuring number of threads, the default value calculates in following formula `cpu * 2 + 1` with a minimum of 16 threads.

---

<a id="benchmark-test"></a>

<!-- source_url: https://shenyu.apache.org/docs/benchmark-test/ -->

<!-- page_index: 126 -->

# Benchmark Test Report

Version: 2.7.0.3

- CPU: 4 cores and 8 threads Intel Cascade Lake @ 3.0GHz
- RAM: 16G

- CPU: 4 cores and 8 threads Intel Cascade Lake @ 3.0GHz
- RAM: 16G

The test tool takes up few resources and is installed on the gateway node server.

- ShenYu Admin: 2.6.0
- ShenYu Bootstrap: 2.6.0

wrk-4.2.0

- Use the Mock service to simulate an interface with an average response time of 20ms and about 2k response messages
- Each test lasts 3 minutes
- JDK version: OpenJdk-1.8.0
- The HTTP request side is tested with `NettyClient` and `WebClient` respectively
- Log level is set to `WARN`
- Apache ShenYu Bootstrap deploy mode: standalone
- Apache ShenYu Admin deploy in `Back-end Mock Service Server`

```text
-Xmx 4g  
-Xms 4g  
-Xmn 1g  
-Xss 512k  
-XX: +DisableExplicitGC  
-XX: LargePageSizeInBytes=128m 
```

- application.yml

```yml
matchCache: 
  selector: 
    selectorEnabled: true 
    initialCapacity: 10000 # initial capacity in cache 
    maximumSize: 10000 # max size in cache 
  rule: 
    initialCapacity: 10000 # initial capacity in cache 
    maximumSize: 65536 # max size in cache 
trie: 
  enabled: true 
  childrenSize: 10000 
  pathVariableSize: 1000 
  pathRuleCacheSize: 1000 
  matchMode: antPathMatch 
```

```yml
netty: 
  http: 
  # set to false, user can custom the netty tcp server config. 
  webServerFactoryEnabled: true 
  selectCount: 1 
  workerCount: 8 
  accessLog: false 
  serverSocketChannel: 
    soRcvBuf: 87380 
    soBackLog: 128 
    soReuseAddr: false 
    connectTimeoutMillis: 10000 
    writeBufferHighWaterMark: 65536 
    writeBufferLowWaterMark: 32768 
    writeSpinCount: 16 
    autoRead: false 
    allocType: "pooled" 
    messageSizeEstimator: 8 
    singleEventExecutorPerGroup: true 
  socketChannel: 
    soKeepAlive: false 
    soReuseAddr: false 
    soLinger: -1 
    tcpNoDelay: true 
    soRcvBuf: 87380 
    soSndBuf: 16384 
    ipTos: 0 
    allowHalfClosure: false 
    connectTimeoutMillis: 10000 
    writeBufferHighWaterMark: 65536 
    writeBufferLowWaterMark: 32768 
    writeSpinCount: 16 
    autoRead: false 
    allocType: "pooled" 
    messageSizeEstimator: 8 
    singleEventExecutorPerGroup: true 
```

```yaml
  file: 
    enabled: false 
    maxSize : 10 
```

```yaml
  cross: 
    enabled: false 
```

```yaml
logging: 
  level: 
    root: warn 
    org.springframework.boot: warn 
    org.apache.ibatis: warn 
    org.apache.shenyu.bonuspoint: warn 
    org.apache.shenyu.lottery: warn 
    org.apache.shenyu: warn 
```

- logback.xml

```xml
    <root level="WARN"> 
        <appender-ref ref="ASYNC_STDOUT"/> 
        <appender-ref ref="ASYNC_FILE"/> 
        <appender-ref ref="ASYNC_ERROR_FILE"/> 
    </root> 
```

```yml
httpclient: 
  strategy: webClient # netty 
  connectTimeout: 45000 # 45000 
  responseTimeout: 3000 # 3000 
  readerIdleTime: 3000 # 3000 
  writerIdleTime: 3000 # 3000 
  allIdleTime: 3000 # 3000 
  readTimeout: 3000 # 3000 
  writeTimeout: 3000 # 3000 
  wiretap: false # false 
  keepAlive: false # false 
  maxInMemorySize: 1 # 1 
  pool: 
    type: ELASTIC # ELASTIC 
    name: proxy # proxy 
    maxConnections: 16 # 16 
    acquireTimeout: 45000 # 45000 
    maxIdleTime: 3000 # 3000 
```

```yml
httpclient: 
  strategy: netty # netty 
  connectTimeout: 45000 # 45000 
  responseTimeout: 3000 # 3000 
  readerIdleTime: 3000 # 3000 
  writerIdleTime: 3000 # 3000 
  allIdleTime: 3000 # 3000 
  readTimeout: 3000 # 3000 
  writeTimeout: 3000 # 3000 
  wiretap: false # false 
  keepAlive: false # false 
  maxInMemorySize: 1 # 1 
  pool: 
    type: ELASTIC # ELASTIC 
    name: proxy # proxy 
    maxConnections: 16 # 16 
    acquireTimeout: 45000 # 45000 
    maxIdleTime: 3000 # 3000 
```

- Direct Access to Back-end Test Result

| **QPS** | **50% latency (ms)** | **75% latency (ms)** | **90% latency (ms)** | **99% latency (ms)** | **平均响应时间(ms)** | **最大响应时间(ms)** |
| --- | --- | --- | --- | --- | --- | --- |
| 28998.20 | 19.81 | 23.78 | 28.26 | 41.24 | 20.92 | 402.90 |

- netty

| currency | QPS | 50% latency (ms) | 75% latency (ms) | 90% latency (ms) | 99% latency (ms) | 平均响应时间(ms) | 最大响应时间(ms) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 600 currency | 20472.95 | 19.37 | 25.36 | 32.89 | 69.92 | 22.09 | 1043.33 |
| 800 currency | 20703.55 | 23.57 | 31.32 | 40.11 | 77.28 | 26.11 | 576.47 |
| 1000 currency | 20979.91 | 29.21 | 37.86 | 47.23 | 80.91 | 31.20 | 860.55 |
| 1200 currency | 21129.88 | 32.45 | 42.40 | 52.68 | 96.10 | 35.06 | 1070 |

- webClient

| currency | QPS | 50% latency (ms) | 75% latency (ms) | 90% latency (ms) | 99% latency (ms) | 平均响应时间(ms) | 最大响应时间(ms) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 600 currency | 18640.47 | 15.77 | 24.77 | 38.26 | 80.31 | 20.32 | 852.06 |
| 800 currency | 18723.44 | 18.12 | 28.69 | 44.96 | 95.3 | 23.52 | 765.26 |
| 1000 currency | 18928.99 | 19.99 | 31.42 | 49.09 | 108.84 | 25.93 | 1040 |
| 1200 currency | 18965.37 | 22.10 | 34.62 | 54.48 | 122.31 | 28.66 | 1075 |

| **QPS** | **50% latency (ms)** | **75% latency (ms)** | **90% latency (ms)** | **99% latency (ms)** | **Avg response time (ms)** | **Max response time (ms)** |
| --- | --- | --- | --- | --- | --- | --- |
| 28998.20 | 19.81 | 23.78 | 28.26 | 41.24 | 20.92 | 402.90 |

![](assets/images/1_337f8e97c371de5d.png)

| currency | **QPS** | **50% latency (ms)** | **75% latency (ms)** | **90% latency (ms)** | **99% latency (ms)** | **Avg response time (ms)** | **Max response time (ms)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 600 concurrency | 20472.95 | 19.37 | 25.36 | 32.89 | 69.92 | 22.09 | 1043.33 |
| 800 concurrency | 20703.55 | 23.57 | 31.32 | 40.11 | 77.28 | 26.11 | 576.47 |
| 1000 concurrency | 20979.91 | 29.21 | 37.86 | 47.23 | 80.91 | 31.20 | 860.55 |
| 1200 concurrency | 21129.88 | 32.45 | 42.40 | 52.68 | 96.10 | 35.06 | 1070 |

![](assets/images/1-netty-cache-selector_ffff464427e1426f.png)
![](assets/images/2-netty-cache-selector_3d6d2cf4c97eb315.jpg)
![](assets/images/3-netty-cache-selector_32bbc4c27ddb3915.jpg)
![](assets/images/1-netty-cache-selector_d0d32665b85feee9.jpg)
![](assets/images/2-netty-cache-selector_ac156614a2584748.jpg)
![](assets/images/3-netty-cache-selector_2d7486071f46d958.jpg)
![](assets/images/1-netty-cache-selector_5613470a937b7eaa.jpg)
![](assets/images/2-netty-cache-selector_5e0ad154cb6a53ce.jpg)
![](assets/images/3-netty-cache-selector_7d9f58fe75aeb7a6.jpg)
![](assets/images/1-netty-cache-selector_73eea75856c292f1.jpg)
![](assets/images/2-netty-cache-selector_7bbfc5882fe79b7a.jpg)
![](assets/images/3-netty-cache-selector_589ede457ac32948.jpg)

| currency | **QPS** | **50% latency (ms)** | **75% latency (ms)** | **90% latency (ms)** | **99% latency (ms)** | **Avg response time (ms)** | **Max response time (ms)** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 600 concurrency | 18640.47 | 15.77 | 24.77 | 38.26 | 80.31 | 20.32 | 852.06 |
| 800 concurrency | 18723.44 | 18.12 | 28.69 | 44.96 | 95.3 | 23.52 | 765.26 |
| 1000 concurrency | 18928.99 | 19.99 | 31.42 | 49.09 | 108.84 | 25.93 | 1040 |
| 1200 concurrency | 18965.37 | 22.10 | 34.62 | 54.48 | 122.31 | 28.66 | 1075 |

![](assets/images/1-netty-cache-selector_1ede714202ac2cad.jpg)
![](assets/images/2-netty-cache-selector_d1648770757873d0.jpg)
![](assets/images/3-netty-cache-selector_6f27127e0fbbd995.jpg)
![](assets/images/1-netty-cache-selector_8c499f0f802b0126.jpg)
![](assets/images/2-netty-cache-selector_313e894eb7b074bd.jpg)
![](assets/images/1-netty-cache-selector_49d60f62fdb14deb.jpg)
![](assets/images/2-netty-cache-selector_c7d30e422aeba4e4.jpg)
![](assets/images/1-netty-cache-selector_fbbda2d87ebe468d.jpg)
![](assets/images/2-netty-cache-selector_c6aafb97b45e2fd8.jpg)

---
