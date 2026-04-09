---
entry_url: https://devlake.apache.org/docs/v1.0/Overview/Introduction
page_count: 120
asset_count: 201
---
# Introduction
## Navigation
- [Overview](#overview)
  - Introduction (https://devlake.apache.org/docs/v1.0/Overview/Introduction)
  - [Architecture](#overview-architecture)
  - [Key Concepts](#overview-keyconcepts)
  - [Supported Data Sources](#overview-supporteddatasources)
  - [API References](#overview-references)
  - [Roadmap](#overview-roadmap)
- [Getting Started](#gettingstarted)
  - [Quick Start](#gettingstarted-quickstart)
  - [Install via Docker Compose](#gettingstarted-dockercomposesetup)
  - [Install via Helm](#gettingstarted-helmsetup)
  - [Upgrade](#gettingstarted-upgrade)
  - [Security and Authentication](#gettingstarted-authentication)
- [Config UI](#config-ui)
  - [Tutorial](#configuration-tutorial)
  - [How to Organize DevLake Projects](#configuration-howtoorganizedevlakeprojects)
  - [Azure DevOps](#configuration-azuredevops)
  - [Bitbucket Cloud](#configuration-bitbucket)
  - [Bitbucket Server/Data Center](#configuration-bitbucketserver)
  - [CircleCI](#configuration-circleci)
  - [GitHub](#configuration-github)
  - [GitLab](#configuration-gitlab)
  - [Opsgenie](#configuration-opsgenie)
  - [Jenkins](#configuration-jenkins)
  - [Jira](#configuration-jira)
  - [PagerDuty](#configuration-pagerduty)
  - [SonarQube Server](#configuration-sonarqube)
  - [TAPD](#configuration-tapd)
  - [Teambition(WIP)](#configuration-teambition)
  - [Webhooks](#configuration-webhook)
  - [Zentao](#configuration-zentao)
  - [Blueprint Advanced Mode](#configuration-advancedmode)
  - [API Keys](#configuration-apikeys)
  - [Team Configuration](#configuration-teamconfiguration)
  - [Dashboard Configuration](#configuration-dashboards-accesscontrol)
    - [Dashboard Access Control](#configuration-dashboards-accesscontrol)
    - [Grafana User Guide](#configuration-dashboards-grafanauserguide)
- [DORA](#dora)
- [Metrics](#metrics)
  - [Requirement Count](#metrics-requirementcount)
  - [Requirement Lead Time](#metrics-requirementleadtime)
  - [Requirement Delivery Rate](#metrics-requirementdeliveryrate)
  - [Requirement Granularity](#metrics-requirementgranularity)
  - [Bug Age](#metrics-bugage)
  - [Bug Count per 1k Lines of Code](#metrics-bugcountper1klinesofcode)
  - [Incident Age](#metrics-incidentage)
  - [Incident Count per 1k Lines of Code](#metrics-incidentcountper1klinesofcode)
  - [Commit Count](#metrics-commitcount)
  - [Commit Author Count](#metrics-commitauthorcount)
  - [Added Lines of Code](#metrics-addedlinesofcode)
  - [Deleted Lines of Code](#metrics-deletedlinesofcode)
  - [PR Count](#metrics-prcount)
  - [PR Cycle Time](#metrics-prcycletime)
  - [PR Coding Time](#metrics-prcodingtime)
  - [PR Pickup Time](#metrics-prpickuptime)
  - [PR Review Time](#metrics-prreviewtime)
  - [PR Deploy Time](#metrics-prdeploytime)
  - [PR Time To Merge](#metrics-prtimetomerge)
  - [PR Merge Rate](#metrics-prmergerate)
  - [PR Review Depth](#metrics-prreviewdepth)
  - [PR Size](#metrics-prsize)
  - [Build Count](#metrics-buildcount)
  - [Build Duration](#metrics-buildduration)
  - [Build Success Rate](#metrics-buildsuccessrate)
  - [DORA - Deployment Frequency](#metrics-deploymentfrequency)
  - [DORA - Median Lead Time for Changes](#metrics-leadtimeforchanges)
  - [DORA - Failed Deployment Recovery Time](#metrics-faileddeploymentrecoverytime)
  - [DORA - Median Time to Restore Service](#metrics-mttr)
  - [DORA - Change Failure Rate](#metrics-cfr)
  - [Code Quality Issue Count](#metrics-cqissuecount)
  - [Code Quality Test](#metrics-cqtest)
  - [Code Quality Maintainability-Debt](#metrics-cqmaintainability-debt)
  - [Code Quality Duplicated Blocks](#metrics-cqduplicatedblocks)
  - [Code Quality Duplicated Lines](#metrics-cqduplicatedlines)
- [Data Models](#datamodels)
  - [Domain Layer Schema](#datamodels-devlakedomainlayerschema)
  - [Tool Layer Schema](#datamodels-toollayerschema)
  - [Raw Layer Schema](#datamodels-rawlayerschema)
  - [System Tables](#datamodels-systemtables)
- [Developer Manuals](#developermanuals)
  - [Developer Setup](#developermanuals-developersetup)
  - [Source Code References](#developermanuals-sourcecodereference)
  - [Plugin Implementation](#developermanuals-pluginimplementation)
  - [DB Migration](#developermanuals-dbmigration)
  - [Notifications](#developermanuals-notifications)
  - [Dal](#developermanuals-dal)
  - [Project](#developermanuals-project)
  - [Tag Naming Conventions](#developermanuals-tagnamingconventions)
  - [E2E Test Guide](#developermanuals-e2e-test-guide)
  - [DevLake Release Guide](#developermanuals-release-sop)
  - [UnitTest Test Guide](#developermanuals-unittest)
- [Plugins](#plugins)
  - [Azure DevOps](#plugins-azuredevops)
  - [Bamboo](#plugins-bamboo)
  - [BitBucket Cloud](#plugins-bitbucket)
  - [BitBucket Data Center](#plugins-bitbucket_server)
  - [CircleCI](#plugins-circleci)
  - [Customize](#plugins-customize)
  - [DBT](#plugins-dbt)
  - [Feishu](#plugins-feishu)
  - [Gitee(WIP)](#plugins-gitee)
  - [GitExtractor](#plugins-gitextractor)
  - [GitHub](#plugins-github)
  - [GitLab](#plugins-gitlab)
  - [Jenkins](#plugins-jenkins)
  - [Jira](#plugins-jira)
  - [Linker](#plugins-linker)
  - [Opsgenie](#plugins-opsgenie)
  - [PagerDuty](#plugins-pagerduty)
  - [RefDiff](#plugins-refdiff)
  - [SonarQube](#plugins-sonarqube)
  - [TAPD](#plugins-tapd)
  - [Teambition(WIP)](#plugins-teambition)
  - [Trello(WIP)](#plugins-trello)
  - Webhook (https://devlake.apache.org/docs/v1.0/Plugins/webhook)
  - [Zentao](#plugins-zentao)
- [Troubleshooting](#troubleshooting)
  - [Installation Troubleshooting](#troubleshooting-installation)
  - [Configuration and Blueprint Troubleshooting](#troubleshooting-configuration)
  - [Dashboard Troubleshooting](#troubleshooting-dashboard)
  - [Mysql Troubleshooting](#troubleshooting-mysqlissue)

## Content

<a id="overview"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Overview/ -->

<!-- page_index: 1 -->

# Overview

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Overview

[## 📄️ Introduction

General introduction of Apache DevLake](https://devlake.apache.org/docs/v1.0/Overview/Introduction)

[## 📄️ Architecture

Understand the architecture of Apache DevLake](#overview-architecture)

[## 📄️ Key Concepts

DevLake Key Concepts](#overview-keyconcepts)

[## 📄️ Supported Data Sources

Data sources that DevLake supports](#overview-supporteddatasources)

[## 📄️ API References

API References](#overview-references)

[## 📄️ Roadmap

The goals and roadmap for DevLake](#overview-roadmap)

---

<a id="overview-introduction"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Overview/Introduction/ -->

<!-- page_index: 2 -->

# Introduction

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Introduction

<a id="overview-introduction--what-is-apache-devlake"></a>

## What is Apache DevLake?

Apache DevLake (Incubating) is an open-source dev data platform that ingests, analyzes, and visualizes the fragmented data from DevOps tools to extract insights for engineering excellence, developer experience, and community growth.

Apache DevLake is designed for developer teams looking to make better sense of their development process and to bring a more data-driven approach to their own practices. You can ask Apache DevLake many questions regarding your development process. Just connect and query.

<a id="overview-introduction--what-can-be-accomplished-with-devlake"></a>

## What can be accomplished with DevLake?

- Unified data integration: Bring together DevOps data from across the Software Development Life Cycle (SDLC) with our [standard data model](https://devlake.apache.org/docs/DataModels/DevLakeDomainLayerSchema).
- Out-of-the-box insights: Access key engineering metrics through intuitive, use-case driven dashboards.
- Customizable: Extend DevLake to align with your unique needs, adding [data sources](#overview-supporteddatasources), [metrics](https://devlake.apache.org/docs/Metrics/), and [dashboards](https://devlake.apache.org/livedemo/EngineeringLeads/DORA) as required.
- Industry standards implementation: Use DevLake to apply recognized [DORA metrics](https://devlake.apache.org/docs/DORA) to optimize DevOps performance.
- Create a thriving culture: DevLake is centered on healthy practices that may help teams adopt and build a practical data-driven culture.

<a id="overview-introduction--how-do-i-use-devlake"></a>

## How do I use DevLake?

<a id="overview-introduction--1-setting-up-devlake"></a>

### 1. Setting-up DevLake

- To implement a proof of concept for Apache DevLake tailored to your specific use cases, you can install it on your local machines using Docker Compose. The detailed instructions for this setup can be found in the [Docker Compose setup documentation](https://devlake.apache.org/docs/GettingStarted/DockerComposeSetup).
- Alternatively, if your infrastructure is powered by Kubernetes, you can explore the [Helm setup](#gettingstarted-helmsetup) option. The Helm setup documentation provides guidance on deploying and configuring Apache DevLake using Helm.

<a id="overview-introduction--2-configuring-data-source"></a>

### 2. Configuring Data Source

- Once Installed, you can start configuring DevLake with [supported data sources](#overview-supporteddatasources) like GitHub, GitLab, Jira, Jenkins, BitBucket, Azure DevOps, SonarQube, PagerDuty, TAPD, ZenTao, Teambition, and we are extending our support to many other tools, feel free to check out the [roadmap](#overview-roadmap).
- However, if your CI/CD tool is not currently supported by DevLake, you can utilize the [webhooks](https://devlake.apache.org/docs/Plugins/webhook/) feature. The Webhooks feature allows you to actively push data to DevLake when there is not a specific plugin available for your DevOps tool.

  ![img](assets/images/introduction-userflow1-969ad4dd4a43f7aaab63c855a5614aed_efed75cdffd8dfad.png)

  ![img](assets/images/introduction-userflow2-5f902237f30cbf20c584732dd5a452a2_efc16e500c0f8467.png)

<a id="overview-introduction--3-creating-your-project"></a>

### 3. Creating your Project

- Once you have connected a data source to Apache DevLake, you can create a "Project" to ensure that you are all set for execution. The process of setting up a project in DevLake typically involves four steps:

  ![img](assets/images/introduction-userflow3-c72d051a7f0aa26d3556937b477f52b7_5711031c4192d71c.png)

<a id="overview-introduction--4-checking-the-dashboards-and-metrics"></a>

### 4. Checking the Dashboards and Metrics

- After configuring your project in DevLake, you can access pre-built dashboards in Grafana. These dashboards provide visualizations and insights for various metrics related to software development.

  ![img](assets/images/userflow3-0d673e4c7005bff5f852f182f765f9ca_6cd6551f7733f950.png)
- To customize the dashboards according to your specific goals and requirements, you can tweak them using Grafana's features. Additionally, if you prefer to create your own dashboards, you have the option to use SQL queries to fetch the necessary data from DevLake referring to the [domain layer data schema](https://devlake.apache.org/docs/DataModels/DevLakeDomainLayerSchema) and SQL examples in the [metrics documentation](https://devlake.apache.org/docs/Metrics/).

  ![img](assets/images/introduction-userflow5-553752c91d53d8fe8c6f69987b385957_af5d4abbf03ab542.png)

- [What is Apache DevLake?](#overview-introduction--what-is-apache-devlake)
- [What can be accomplished with DevLake?](#overview-introduction--what-can-be-accomplished-with-devlake)
- [How do I use DevLake?](#overview-introduction--how-do-i-use-devlake)
  - [1. Setting-up DevLake](#overview-introduction--1-setting-up-devlake)
  - [2. Configuring Data Source](#overview-introduction--2-configuring-data-source)
  - [3. Creating your Project](#overview-introduction--3-creating-your-project)
  - [4. Checking the Dashboards and Metrics](#overview-introduction--4-checking-the-dashboards-and-metrics)

---

<a id="overview-architecture"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Overview/Architecture/ -->

<!-- page_index: 3 -->

# Architecture

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Architecture

<a id="overview-architecture--overview"></a>

## Overview

![](assets/images/arch-component_15573fc40ad7ac08.svg)

DevLake Components

A DevLake installation typically consists of the following components:

- Config UI: A handy user interface to create, trigger, and debug Blueprints. A Blueprint specifies the where (data connection), what (data scope), how (transformation rule), and when (sync frequency) of a data pipeline.
- API Server: The main programmatic interface of DevLake.
- Runner: The runner does all the heavy-lifting for executing tasks. In the default DevLake installation, it runs within the API Server, but DevLake provides a temporal-based runner (beta) for production environments.
- Database: The database stores both DevLake's metadata and user data collected by data pipelines. DevLake supports MySQL and PostgreSQL as of v0.11.
- Plugins: Plugins enable DevLake to collect and analyze dev data from any DevOps tools with an accessible API. DevLake community is actively adding plugins for popular DevOps tools, but if your preferred tool is not covered yet, feel free to open a GitHub issue to let us know or check out our doc on how to build a new plugin by yourself.
- Dashboards: Dashboards deliver data and insights to DevLake users. A dashboard is simply a collection of SQL queries along with corresponding visualization configurations. DevLake's official dashboard tool is Grafana and pre-built dashboards are shipped in Grafana's JSON format. Users are welcome to swap for their own choice of dashboard/BI tool if desired.

<a id="overview-architecture--dataflow"></a>

## Dataflow

![](assets/images/arch-dataflow-7829e34501bbb6941bee89d7ad8e2790_814f360f4de3eb8f.svg)

A typical plugin's dataflow is illustrated below:

1. The Raw layer stores the API responses from data sources (DevOps tools) in JSON. This saves developers' time if the raw data is to be transformed differently later on. Please note that communicating with data sources' APIs is usually the most time-consuming step.
2. The Tool layer extracts raw data from JSONs into a relational schema that's easier to consume by analytical tasks. Each DevOps tool would have a schema that's tailored to its data structure, hence the name, the Tool layer.
3. The Domain layer attempts to build a layer of abstraction on top of the Tool layer so that analytics logics can be re-used across different tools. For example, GitHub's Pull Request (PR) and GitLab's Merge Request (MR) are similar entities. They each have their own table name and schema in the Tool layer, but they're consolidated into a single entity in the Domain layer, so that developers only need to implement metrics like Cycle Time and Code Review Rounds once against the domain layer schema.

<a id="overview-architecture--principles"></a>

## Principles

1. Extensible: DevLake's plugin system allows users to integrate with any DevOps tool. DevLake also provides a dbt plugin that enables users to define their own data transformation and analysis workflows.
2. Portable: DevLake has a modular design and provides multiple options for each module. Users of different setups can freely choose the right configuration for themselves.
3. Robust: DevLake provides an SDK to help plugins efficiently and reliably collect data from data sources while respecting their API rate limits and constraints.

- [Overview](#overview-architecture--overview)
- [Dataflow](#overview-architecture--dataflow)
- [Principles](#overview-architecture--principles)

---

<a id="overview-keyconcepts"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Overview/KeyConcepts/ -->

<!-- page_index: 4 -->

# Key Concepts

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Key Concepts

*Last updated: Nov 9, 2023*

<a id="overview-keyconcepts--in-config-ui"></a>

## In Config UI

The following terms are arranged in the order of their appearance in the actual user workflow in the config UI.

<a id="overview-keyconcepts--data-source"></a>

### Data Source

**A data source is a specific DevOps tool from which you wish to sync your data, such as GitHub, GitLab, Jira and Jenkins.**

Typically, DevLake uses one [data plugin](#overview-keyconcepts--data-plugins) to pull data for a single data source. For example, the [jira](https://devlake.apache.org/docs/Plugins/jira) plugin is used to fetch data from Jira.

However, there are cases where DevLake may use multiple data plugins for a single data source. This approach is employed to enhance the synchronization speed and provide other advantages. For instance, when retrieving data from GitHub or GitLab, aside from the [github](https://devlake.apache.org/docs/Plugins/github) and [gitlab](https://devlake.apache.org/docs/Plugins/gitlab) plugins, the [gitextractor](https://devlake.apache.org/docs/Plugins/gitextractor) is also used to fetch data. In these cases, DevLake still recognizes GitHub or GitLab as a single data source.

<a id="overview-keyconcepts--data-connection"></a>

### Data Connection

**A data connection is a specific instance of a [data source](#overview-keyconcepts--data-source).** It stores the necessary access information, such as the endpoint URL and authentication token, to establish a connection to that data source.

A single data source can have one or more data connections associated with it. This allows you to connect to and retrieve data from different instances or installations of the same data source.

To set up a new data connection, it is recommended to use the 'Data Connections' page in DevLake. This page provides a convenient interface for adding and configuring data connections. Once a data connection is set up, you can later associate it with a DevLake project.

<a id="overview-keyconcepts--data-scope"></a>

### Data Scope

**A data scope is the top-level 'container' in a data source**. For example, a data scope for Jira is a Jira board, for TAPD is a TAPD workspace, for GitHub/GitLab/BitBucket is a repo, for Jenkins is a Jenkins job, etc.

You can add multiple data scopes to a data connection to determine which data to collect. Data scopes vary for different data sources.

<a id="overview-keyconcepts--scope-config"></a>

### Scope Config

**A scope config refers to the configuration of a data scope.** It defines the specific data entities to be collected and the transformations to be applied to that data.

Each data scope can have at most one scope config associated with it; while a scope config can be shared among multiple data scopes under the same data connection.

A scope config consists of two parts: [Data Entities](#overview-keyconcepts--data-entities) and [Transformations](#overview-keyconcepts--transformations).

<a id="overview-keyconcepts--data-entities"></a>

#### Data Entities

Data entities refer to the specific data fields that are collected from different data domains. Check the [supported data entities](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-collection-scope-by-each-plugin) of each data source.

Data entities are categorized into [six data domains](https://devlake.apache.org/docs/DataModels/DevLakeDomainLayerSchema#data-models) in DevLake: Issue Tracking, Source Code Management, Code Review, CI/CD, Code Quality, and Cross-Domain.

When setting up the scope config of a GitHub data connection, you have the flexibility to choose which specific data entities you want to collect. if you only want to collect 'repos', 'commits', and 'pull requests' while excluding 'issues' and 'workflow runs', you need to check the 'Source Code Management' and 'Code Review' domains, and uncheck 'Issue Tracking' or 'CI/CD' domains.

<a id="overview-keyconcepts--transformations"></a>

#### Transformations

Transformations are configurations for users to customize how DevLake transforms raw API responses to the domain layer data.

Although configuring transformation rules is not mandatory, certain pre-built dashboards, such as [DORA](https://devlake.apache.org/livedemo/EngineeringLeads/DORA) and [Weekly Bug Retro](https://devlake.apache.org/livedemo/EngineeringLeads/WeeklyBugRetro) require them to display the metrics accurately. If you leave the rules blank or have not configured them correctly, only a few [data source dashboards](https://devlake.apache.org/livedemo/DataSources/GitHub) will be displayed as expected.

You can find the required transformations in the 'Dashboard Introduction' panel in each pre-built dashboard.

<a id="overview-keyconcepts--project"></a>

### Project

**On a high level, a DevLake project can be viewed as a real-world project or product line.** It represents a specific initiative or endeavor within the software development domain.

**On a lower level, a DevLake project is a way of organizing and grouping data from different domains.** DevLake uses various [data scopes](#overview-keyconcepts--data-scope), such as repos, boards, cicd\_scopes, and cq\_projects as the 'container' to associate different types of data to a specific project.

- A project has a [blueprint](#overview-keyconcepts--bluepirnts) for data collection and metric computation.
- DevLake measures DORA metrics at the project level. Each project has a set of DORA metrics. For example, if a user associates 'Jenkins Job A' and 'Jira board B' with project M, only the 'deployments' from 'Jenkins Job A' and the 'incidents' from 'Jira board B' will be considered when calculating the Change Failure Rate metric for project M.
  ![](assets/images/project-pipeline-06b394bb2f3453ffd888f20affbe2d5d_311dbba751935852.png)

<a id="overview-keyconcepts--blueprint"></a>

### Blueprint

**A blueprint serves as the plan to synchronize data from data sources into the DevLake platform.** Creating a blueprint consists of four steps:

1. Adding [data connections](#overview-keyconcepts--data-connections): You can add one or more data connections to a blueprint, depending on the data sources you want to sync with DevLake. Each data connection represents a specific data source, such as GitHub or Jira.
2. Setting up the [data scope](#overview-keyconcepts--data-scope): When adding a data connection, you can choose to collect all or part of the configured data scopes of the data connection.
3. Setting up the sync policy: You can specify the sync frequency and the time range for data collection.

The relationship between 'Blueprint', 'Project' and 'Data Connection' is explained as follows:

![Blueprint ERD](assets/images/blueprint-erd-762692dfe07100fd9c045dd22ec90954_9fd1ff1365d183a2.svg)

- A blueprint will be automatically created by along the creation with a DevLake project.
- Each blueprint can have multiple data connections.
- Each data connection can have multiple data scopes.
- Each set of data scope only consists of one GitHub/GitLab project or Jira board, along with their corresponding data entities.
- Each set of data scope can only have one set of scope config.

<a id="overview-keyconcepts--apis-and-config-ui-advanced-mode"></a>

## APIs and Config UI Advanced Mode

Typically, the following terms do not appear in the regular mode of the Config UI, but can be very useful if you use [DevLake's APIs](#overview-references) or the advanced mode of Config UI.

<a id="overview-keyconcepts--data-plugins"></a>

### Data Plugins

**A data plugin is a specific module that syncs or transforms data.** There are two types of data plugins: Data Collection Plugins and Data Transformation Plugins.

Data Collection Plugins pull data from one or more data sources. DevLake supports 8 data plugins in this category: `ae`, `feishu`, `gitextractor`, `github`, `gitlab`, `jenkins`, `jira` and `tapd`.

Data Transformation Plugins transform the data pulled by other Data Collection Plugins. `refdiff` is currently the only plugin in this category.

Although the names of the data plugins are not displayed in the regular mode of DevLake Configuration UI, they can be used directly in JSON in the Advanced Mode.

For detailed information about the relationship between data sources and data plugins, please refer to [Supported Data Sources](#overview-supporteddatasources).

<a id="overview-keyconcepts--pipelines"></a>

### Pipelines

**A pipeline is an orchestration of [tasks](#overview-keyconcepts--tasks) of data `collection`, `extraction`, `conversion` and `enrichment`, defined in the DevLake API.** A pipeline is composed of one or multiple [stages](#overview-keyconcepts--stages) that are executed in a sequential order. Any error occurring during the execution of any stage, task or subtask will cause the immediate fail of the pipeline.

The composition of a pipeline is explained as follows:
![Blueprint ERD](assets/images/pipeline-erd-63705e2232b63c7fe75197ee3e96f170_57359be3045fcb2a.svg)
Notice: **You can manually orchestrate the pipeline in Configuration UI Advanced Mode and the DevLake API; whereas in Configuration UI regular mode, an optimized pipeline orchestration will be automatically generated for you.**

<a id="overview-keyconcepts--stages"></a>

### Stages

**A stages is a collection of tasks performed by data plugins.** Stages are executed in a sequential order in a pipeline.

<a id="overview-keyconcepts--tasks"></a>

### Tasks

**A task is a collection of [subtasks](#overview-keyconcepts--subtasks) that perform any of the `collection`, `extraction`, `conversion` and `enrichment` jobs of a particular data plugin.** Tasks are executed in a parallel order in any stages.

<a id="overview-keyconcepts--subtasks"></a>

### Subtasks

**A subtask is the minimal work unit in a pipeline that performs in any of the four roles: `Collectors`, `Extractors`, `Converters` and `Enrichers`.** Subtasks are executed in sequential orders.

- `Collectors`: Collect raw data from data sources, normally via DevLake API and stored into `raw data table`
- `Extractors`: Extract data from `raw data tables` to `tool layer tables`
- `Converters`: Convert data from `tool layer tables` into `domain layer tables`
- `Enrichers`: Enrich data from one domain to other domains. For instance, the Fourier Transformation can examine `issue_changelog` to show time distribution of an issue on every assignee.

- [In Config UI](#overview-keyconcepts--in-config-ui)
  - [Data Source](#overview-keyconcepts--data-source)
  - [Data Connection](#overview-keyconcepts--data-connection)
  - [Data Scope](#overview-keyconcepts--data-scope)
  - [Scope Config](#overview-keyconcepts--scope-config)
  - [Project](#overview-keyconcepts--project)
  - [Blueprint](#overview-keyconcepts--blueprint)
- [APIs and Config UI Advanced Mode](#overview-keyconcepts--apis-and-config-ui-advanced-mode)
  - [Data Plugins](#overview-keyconcepts--data-plugins)
  - [Pipelines](#overview-keyconcepts--pipelines)
  - [Stages](#overview-keyconcepts--stages)
  - [Tasks](#overview-keyconcepts--tasks)
  - [Subtasks](#overview-keyconcepts--subtasks)

---

<a id="overview-supporteddatasources"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Overview/SupportedDataSources/ -->

<!-- page_index: 5 -->

# Supported Data Sources

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Supported Data Sources

<a id="overview-supporteddatasources--data-sources-and-data-plugins"></a>

## Data Sources and Data Plugins

Apache DevLake(incubating) supports the following data sources. The data from each data source is collected with one or
more plugins. Detailed plugin docs can be found [here](https://devlake.apache.org/docs/Plugins).

<table><thead><tr><th>Data Source</th><th>Domain(s)</th><th>Supported Versions</th><th>Config UI Availability</th><th>Triggered Plugins</th><th>Collection Mode</th></tr></thead><tbody><tr><td>GitHub</td><td>Source Code Management, Code Review, Issue Tracking, CI/CD (GitHub Actions)</td><td>Cloud</td><td>Available</td><td><code>github</code>, <code>gitextractor</code></td><td>Incremental Sync</td></tr><tr><td>GitLab</td><td>Source Code Management, Code Review, Issue Tracking, CI/CD (GitLab CI)</td><td>Cloud, Community Edition 11+</td><td>Available</td><td><code>gitlab</code>, <code>gitextractor</code></td><td>Full Refresh, Incremental Sync(for <code>issues</code>,<code>MRs</code>)</td></tr><tr><td>Jira</td><td>Issue Tracking</td><td>Cloud, Server/Data Center 7.x, 8.x</td><td>Available</td><td><code>jira</code></td><td>Full Refresh, Incremental Sync(for <code>issues</code> and related)</td></tr><tr><td>Jenkins</td><td>CI/CD</td><td>2.263.x+</td><td>Available</td><td><code>jenkins</code></td><td>Incremental Sync</td></tr><tr><td>BitBucket (Beta)</td><td>Source Code Management, Code Review</td><td>Cloud</td><td>Advanced Mode Available</td><td><code>bitbucket</code>, <code>gitextractor</code></td><td>Full Refresh</td></tr><tr><td>TAPD (Beta)</td><td>Issue Tracking</td><td>Cloud</td><td>Advanced Mode Available</td><td><code>tapd</code></td><td>Full Refresh, Incremental Sync(for <code>stories</code>, <code>bugs</code>, <code>tasks</code>)</td></tr><tr><td>Teambition (Beta)</td><td>Issue Tracking</td><td>Cloud</td><td>Advanced Mode Available</td><td><code>teambition</code></td><td>Full Refresh</td></tr><tr><td>Zentao (Beta)</td><td>Issue Tracking</td><td>v17.x, v18.x</td><td>Advanced Mode Available</td><td><code>zentao</code></td><td>Full Refresh</td></tr><tr><td>Gitee (WIP)</td><td>Source Code Management, Code Review, Issue Tracking</td><td>Cloud</td><td>Not Available</td><td><code>gitee</code>, <code>gitextractor</code></td><td>Full Refresh, Incremental Sync(for <code>issues</code>,<code>MRs</code>)</td></tr><tr><td>PagerDuty</td><td>Issue Tracking</td><td>Cloud</td><td>Available</td><td><code>pagerduty</code></td><td>Incremental Sync</td></tr><tr><td>Opsgenie</td><td>Issue Tracking</td><td>Cloud</td><td>Available</td><td><code>opsgenie</code></td><td>Full Refresh (for <code>users</code>,<code>teams</code>), Incremental Sync (for <code>issues</code>)</td></tr><tr><td>Feishu (WIP)</td><td>Calendar</td><td>Cloud</td><td>Not Available</td><td><code>feishu</code></td><td>Full Refresh</td></tr><tr><td>AE</td><td>Source Code Management</td><td>On-prem</td><td>Not Available</td><td><code>ae</code></td><td>Full Refresh</td></tr><tr><td>Sonarqube</td><td>CODE QUALITY</td><td>SonarQube v8.x, v9.x</td><td>Available</td><td><code>sonarqube</code></td><td>Full Refresh</td></tr><tr><td>Bamboo CI(WIP)</td><td>CI/CD</td><td>v6.8.1, Server</td><td>Not Available</td><td><code>bamboo</code></td><td>Full Refresh</td></tr><tr><td>Azure Devops (Beta)</td><td>CI/CD, Source Code Management, Code Review</td><td>Cloud</td><td>Available</td><td><code>azuredevops</code>, <code>gitextractor</code></td><td>Full Refresh</td></tr><tr><td>CircleCI</td><td>CI/CD</td><td>Cloud</td><td>Available</td><td><code>circleci</code></td><td>Full Refresh</td></tr></tbody></table>
<a id="overview-supporteddatasources--data-collection-scope-by-each-plugin"></a>

## Data Collection Scope By Each Plugin

This table shows the entities collected by each plugin. Domain layer entities in this table are consistent with the
entities [here](#datamodels-devlakedomainlayerschema).
✅ : Collect by default.
💪 : Collect not by default. You need to add the corresponding subtasks to collect these entities in
the [advanced mode](#configuration-advancedmode).

<table><thead><tr><th>Domain Layer Entities</th><th>ae</th><th>dora</th><th>gitextractor</th><th>incoming webhook</th><th>github</th><th>gitlab</th><th>jenkins</th><th>jira</th><th>refdiff</th><th>tapd</th><th>sonarqube</th><th>bamboo</th><th>azuredevops</th><th>opsgenie</th><th>circleci</th></tr></thead><tbody><tr><td><a href="#datamodels-devlakedomainlayerschema--accounts">accounts</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td>✅</td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--board_issues">board_issues</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td>✅</td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--board_repos">board_repos</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--board_sprints">board_sprints</a></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--boards">boards</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td>✅</td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cicd_pipeline_commits">cicd_pipeline_commits</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cicd_pipelines">cicd_pipelines</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cicd_scopes">cicd_scopes</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cicd_tasks">cicd_tasks</a></td><td></td><td>✅</td><td></td><td>💪</td><td>✅</td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--commit_file_components">commit_file_components</a></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--commit_files">commit_files</a></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--commit_line_change">commit_line_change</a></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--commit_parents">commit_parents</a></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--commits">commits</a></td><td>✅</td><td></td><td>✅</td><td></td><td>💪</td><td>💪</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--commits_diffs">commits_diffs</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--components">components</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--finished_commits_diffs">finished_commits_diffs</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--issue_changelogs">issue_changelogs</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--issue_comments">issue_comments</a></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--issue_commits">issue_commits</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--issue_labels">issue_labels</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--issue_repo_commits">issue_repo_commits</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--issue_worklogs">issue_worklogs</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--issues">issues</a></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td>✅</td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--project_issue_metrics">project_issue_metrics</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--project_mapping">project_mapping</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--project_metrics">project_metrics</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--project_pr_metrics">project_pr_metrics</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--project">project</a></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td>✅</td><td>✅</td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td>✅</td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--pull_request_comments">pull_request_comments</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--pull_request_commits">pull_request_commits</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--pull_request_issues">pull_request_issues</a></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--pull_request_labels">pull_request_labels</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--pull_requests">pull_requests</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--ref_commits">ref_commits</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--refs">refs</a></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--refs_issues_diffs">refs_issues_diffs</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--ref_pr_cherry_picks">ref_pr_cherry_picks</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--repo_commits">repo_commits</a></td><td></td><td></td><td>✅</td><td></td><td>💪</td><td>💪</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--repo_snapshot">repo_snapshot</a></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--repos">repos</a></td><td></td><td></td><td></td><td></td><td>✅</td><td>✅</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--sprint_issues">sprint_issues</a></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--sprints">sprints</a></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--team_users">team_users</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--teams">teams</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--user_accounts">user_account</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--users">users</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td>✅</td><td></td><td></td><td></td><td>✅</td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cq_projects">cq_projects</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cq_issues">cq_issues</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cq_issue_code_blocks">cq_issue_code_blocks</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td></tr><tr><td><a href="#datamodels-devlakedomainlayerschema--cq_file_metrics">cq_file_metrics</a></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>✅</td><td></td><td></td><td></td><td></td></tr></tbody></table>
<a id="overview-supporteddatasources--data-sync-policy"></a>

## Data Sync Policy

**bold:** means it may collect slowly.

**\*bold\*:** means it may collect very slowly.

<a id="overview-supporteddatasources--jira"></a>

### Jira

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectStatusMeta</td><td>1</td><td>-</td><td>-</td></tr><tr><td>CollectProjectsMeta</td><td>&lt;10</td><td>❌</td><td>-</td></tr><tr><td>CollectIssueTypesMeta</td><td>&lt;10</td><td>❌</td><td>-</td></tr><tr><td>CollectIssuesMeta</td><td>&lt;10^4</td><td>✅</td><td>✅</td></tr><tr><td>CollectIssueChangelogsMeta</td><td>1000~10^5</td><td>✅</td><td>✅</td></tr><tr><td>CollectAccountsMeta</td><td>&lt;10^3</td><td>❌</td><td>❌</td></tr><tr><td>CollectWorklogsMeta</td><td>1000~10^5</td><td>✅</td><td>✅</td></tr><tr><td>CollectRemotelinksMeta</td><td>1000~10^5</td><td>✅</td><td>✅</td></tr><tr><td>CollectSprintsMeta</td><td>&lt;100</td><td>❌</td><td>❌</td></tr><tr><td>CollectEpicsMeta</td><td>&lt;100</td><td>❌</td><td>✅</td></tr></tbody></table>
<a id="overview-supporteddatasources--jenkins"></a>

### Jenkins

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectApiBuildsMeta</td><td>≈100</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiStagesMeta</td><td>≈10^4</td><td>❌</td><td>✅</td></tr></tbody></table>
<a id="overview-supporteddatasources--gitlab"></a>

### GitLab

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectApiIssuesMeta</td><td>&lt;10^4</td><td>✅</td><td>✅</td></tr><tr><td>CollectApiMergeRequestsMeta</td><td>&lt;10^3</td><td>✅</td><td>✅</td></tr><tr><td>CollectApiMrNotesMeta</td><td>&lt;10^5</td><td>❌</td><td>✅</td></tr><tr><td>CollectApiMrCommitsMeta</td><td>&lt;10^5</td><td>❌</td><td>✅</td></tr><tr><td><strong>CollectApiPipelinesMeta</strong></td><td>&lt;10^4</td><td>✅</td><td>❌</td></tr><tr><td>CollectApiJobsMeta</td><td>&lt;10^5</td><td>❌</td><td>✅</td></tr></tbody></table>
<a id="overview-supporteddatasources--github"></a>

### Github

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>---------------------------------</td><td>Common</td><td>-----------------------</td><td></td></tr><tr><td>CollectMilestonesMeta</td><td>≈10</td><td>✅</td><td>❌</td></tr><tr><td>CollectRunsMeta</td><td>&lt;10^4</td><td>✅</td><td>✅</td></tr><tr><td>CollectApiCommentsMeta</td><td>400 (max page that GitHub supports)</td><td>✅</td><td>✅</td></tr><tr><td><strong>CollectApiEventsMeta</strong></td><td>400 (max page that GitHub supports)</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiPullRequestReviewsMeta</td><td>&lt;10^5</td><td>✅</td><td>✅</td></tr><tr><td>---------------------------------</td><td>Graphql Only (Default)</td><td>-----------------------</td><td></td></tr><tr><td>CollectIssueMeta</td><td>≈10^4</td><td>❌</td><td>✅</td></tr><tr><td>CollectPrMeta</td><td>≈10^3</td><td>❌</td><td>✅</td></tr><tr><td>CollectCheckRunMeta</td><td>&lt;10^4</td><td>❌</td><td>✅</td></tr><tr><td>CollectAccountMeta</td><td>≈10^2</td><td>❌</td><td>-</td></tr><tr><td>---------------------------------</td><td>Restful Only (Not by Default)</td><td>-----------------------</td><td></td></tr><tr><td>CollectApiIssuesMeta</td><td>≈10^4</td><td>✅</td><td>❌</td></tr><tr><td>CollectApiPullRequestsMeta</td><td>≈10^2</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiPullRequestCommitsMeta</td><td>≈10^4</td><td>✅</td><td>✅</td></tr><tr><td><strong>CollectApiPrReviewCommentsMeta</strong></td><td>≈10^4</td><td>✅</td><td>✅</td></tr><tr><td><strong>CollectAccountsMeta</strong></td><td>≈10^4</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectAccountOrgMeta</strong></td><td>≈10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectJobsMeta</td><td>&lt;10^6</td><td>❌</td><td>✅</td></tr><tr><td>CollectApiCommitsMeta</td><td>Not enabled</td><td>-</td><td>-</td></tr><tr><td>CollectApiCommitStatsMeta</td><td>Not enabled</td><td>-</td><td>-</td></tr></tbody></table>
<a id="overview-supporteddatasources--feishu"></a>

### Feishu

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectMeetingTopUserItemMeta</td><td>≈10^3</td><td>❌</td><td>✅</td></tr></tbody></table>
<a id="overview-supporteddatasources--bitbucket"></a>

### Bitbucket

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td><del>CollectApiRepoMeta</del></td><td>1</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiPullRequestsMeta</td><td>≈10^3</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectApiIssuesMeta</strong></td><td>≈10^4</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectApiPrCommentsMeta</strong></td><td>≈10^5</td><td>❌</td><td>❌</td></tr><tr><td><strong>*<!-- -->CollectApiIssueCommentsMeta<!-- -->*</strong></td><td>≈10^6</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectApiPipelinesMeta</strong></td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiDeploymentsMeta</td><td>&lt;10^2</td><td>❌</td><td>❌</td></tr></tbody></table>
<a id="overview-supporteddatasources--bitbucket-serverdata-center"></a>

### Bitbucket Server/Data Center

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td><del>CollectApiBranchesMeta</del></td><td>1</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiPullRequestsMeta</td><td>≈10^3</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectApiPrActivitiesMeta</strong></td><td>≈10^4</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectApiPrCommentsMeta</strong></td><td>≈10^5</td><td>❌</td><td>❌</td></tr><tr><td><strong>*<!-- -->CollectApiIssueCommentsMeta<!-- -->*</strong></td><td>≈10^6</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectApiCommitsMeta</strong></td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiPrCommitsMeta</td><td>&lt;10^2</td><td>❌</td><td>❌</td></tr></tbody></table>
<a id="overview-supporteddatasources--gitee"></a>

### Gitee

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td><del>CollectApiRepoMeta</del></td><td>1</td><td>❌</td><td>❌</td></tr><tr><td>CollectApiPullRequestsMeta</td><td>≈10^3</td><td>✅</td><td>❌</td></tr><tr><td><strong>CollectApiIssuesMeta</strong></td><td>≈10^4</td><td>✅</td><td>❌</td></tr><tr><td><strong>CollectCommitsMeta?</strong></td><td>≈10^4</td><td>✅</td><td>❌</td></tr><tr><td><strong>CollectApiPrCommentsMeta</strong></td><td>≈10^5</td><td>❌</td><td>❌</td></tr><tr><td><strong>*<!-- -->CollectApiIssueCommentsMeta<!-- -->*</strong></td><td>≈10^6</td><td>✅</td><td>❌</td></tr><tr><td><strong>CollectApiPullRequestCommitsMeta</strong></td><td>≈10^5</td><td>❌</td><td>❌</td></tr><tr><td><strong>CollectApiPullRequestReviewsMeta</strong></td><td>≈10^5</td><td>❌</td><td>❌</td></tr><tr><td><strong>*<!-- -->CollectApiCommitStatsMeta<!-- -->*</strong></td><td>≈10^6 (Not enable)</td><td>❌</td><td>❌</td></tr></tbody></table>
<a id="overview-supporteddatasources--sonarqube"></a>

### SonarQube

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectAccounts</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectIssues</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectHotspots</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectFilemetrics</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectAdditionalFilemetrics</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr></tbody></table>
<a id="overview-supporteddatasources--bamboo"></a>

### Bamboo

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectPlanMeta</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectJobMeta</td><td>&lt;10^5</td><td>❌</td><td>❌</td></tr><tr><td>CollectPlanBuildMeta</td><td>&lt;10^6</td><td>❌</td><td>❌</td></tr><tr><td>CollectJobBuildMeta</td><td>&lt;10^6</td><td>❌</td><td>❌</td></tr><tr><td>CollectDeployMeta</td><td>1</td><td>❌</td><td>❌</td></tr></tbody></table>
<a id="overview-supporteddatasources--zentao"></a>

### Zentao

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectExecutionMeta</td><td>&lt;10^3</td><td>❌</td><td>❌</td></tr><tr><td>CollectStoryMeta</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectBugMeta</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectTaskMeta</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectAccountMeta</td><td>≈10^2</td><td>❌</td><td>❌</td></tr><tr><td>CollectDepartmentMeta</td><td>≈10^2</td><td>❌</td><td>❌</td></tr></tbody></table>
<a id="overview-supporteddatasources--tapd"></a>

### Tapd

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectWorkitemTypesMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectStoryCustomFieldsMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectTaskCustomFieldsMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectBugCustomFieldsMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectStoryCategoriesMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectStoryStatusMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectStoryStatusLastStepMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectBugStatusMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectBugStatusLastStepMeta</td><td>≈10</td><td>-</td><td>-</td></tr><tr><td>CollectAccountsMeta</td><td>≈10^3</td><td>❌</td><td>❌</td></tr><tr><td>CollectIterationMeta</td><td>≈10^4</td><td>✅</td><td>✅</td></tr><tr><td>CollectStoryMeta</td><td>≈10^4</td><td>✅</td><td>✅</td></tr><tr><td>CollectBugMeta</td><td>≈10^4</td><td>✅</td><td>✅</td></tr><tr><td>CollectTaskMeta</td><td>≈10^4</td><td>✅</td><td>✅</td></tr><tr><td>CollectBugChangelogMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr><tr><td>CollectStoryChangelogMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr><tr><td>CollectTaskChangelogMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr><tr><td>CollectWorklogMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr><tr><td>CollectBugCommitMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr><tr><td>CollectStoryCommitMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr><tr><td>CollectTaskCommitMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr><tr><td>CollectStoryBugMeta</td><td>≈10^6</td><td>✅</td><td>✅</td></tr></tbody></table>
<a id="overview-supporteddatasources--azure-devops"></a>

### Azure Devops

<table><thead><tr><th>Subtask Name</th><th>Estimated Max Number of Request</th><th>Does It support Incremental Collection?</th><th>Does It Support Time Filter?</th></tr></thead><tbody><tr><td>CollectBuilds</td><td>&lt;10^3</td><td>❌</td><td>❌</td></tr><tr><td>CollectJobs</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr><tr><td>CollectPullRequests</td><td>&lt;10^3</td><td>❌</td><td>❌</td></tr><tr><td>CollectPullRequestCommits</td><td>&lt;10^4</td><td>❌</td><td>❌</td></tr></tbody></table>

- [Data Sources and Data Plugins](#overview-supporteddatasources--data-sources-and-data-plugins)
- [Data Collection Scope By Each Plugin](#overview-supporteddatasources--data-collection-scope-by-each-plugin)
- [Data Sync Policy](#overview-supporteddatasources--data-sync-policy)
  - [Jira](#overview-supporteddatasources--jira)
  - [Jenkins](#overview-supporteddatasources--jenkins)
  - [GitLab](#overview-supporteddatasources--gitlab)
  - [Github](#overview-supporteddatasources--github)
  - [Feishu](#overview-supporteddatasources--feishu)
  - [Bitbucket](#overview-supporteddatasources--bitbucket)
  - [Bitbucket Server/Data Center](#overview-supporteddatasources--bitbucket-serverdata-center)
  - [Gitee](#overview-supporteddatasources--gitee)
  - [SonarQube](#overview-supporteddatasources--sonarqube)
  - [Bamboo](#overview-supporteddatasources--bamboo)
  - [Zentao](#overview-supporteddatasources--zentao)
  - [Tapd](#overview-supporteddatasources--tapd)
  - [Azure Devops](#overview-supporteddatasources--azure-devops)

---

<a id="overview-references"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Overview/References/ -->

<!-- page_index: 6 -->

# API References

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# API References

For users/developers who wish to interact with the Apache DevLake by using the RESTful APIs, the Swagger Document would very useful for you. The `devlake` docker image has it packaged, you may access it from:
If you are using the `devlake` container alone without `config-ui`:

```text
http://<DEVLAKE_CONTIANER_HOST>:<PORT>/swagger/index.html
```

or

```text
http://<CONFIG_UI_CONTIANER_HOST>:<PORT>/api/swagger/index.html
```

---

<a id="overview-roadmap"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Overview/Roadmap/ -->

<!-- page_index: 7 -->

# Roadmap

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Roadmap

<a id="overview-roadmap--goals"></a>

## Goals

DevLake has joined the Apache Incubator and is aiming to become a top-level project. To achieve this goal, the Apache DevLake (Incubating) community will continue to make efforts in helping development teams to analyze and improve their engineering productivity. In this roadmap, we have summarized three major goals followed by the feature breakdown to invite the broader community to join us and grow together.

1. As a dev data analysis application, discover and implement 3 (or even more!) usage scenarios:
   - A collection of metrics to track the contribution, quality and growth of open-source projects
   - DORA metrics for DevOps engineers
   - To be decided ([let us know](https://join.slack.com/t/devlake-io/shared_invite/zt-1lkgbdmys-AU2azidzO1u~mtjlg9my7A) if you have any suggestions!)
2. As dev data infrastructure, provide robust data collection modules, customizable data models, and data extensibility.
3. Design better user experience for end-users and contributors.

<a id="overview-roadmap--feature-breakdown"></a>

## Feature Breakdown

Apache DevLake is currently under rapid development. You are more than welcome to use the following table to explore your intereted features and make contributions. We deeply appreciate the collective effort of our community to make this project possible!

<table><thead><tr><th>Category</th><th>Features</th></tr></thead><tbody><tr><td>More data sources across different DevOps domains (Goal No.1 &amp; 2). See <a href="https://devlake.apache.org/docs/Overview/SupportedDataSources">existing data sources</a></td><td>Issue Tracking: <ul><li>Jira (cloud) <a href="https://github.com/apache/incubator-devlake/issues/886" rel="noopener noreferrer" target="_blank">#886 (Done)</a></li><li>Jira (server/data center) <a href="https://github.com/apache/incubator-devlake/issues/1687" rel="noopener noreferrer" target="_blank">#1687 (Done)</a></li><li>GitHub Issues <a href="https://github.com/apache/incubator-devlake/issues/407" rel="noopener noreferrer" target="_blank">#407 (Done)</a></li><li>GitLab Issues <a href="https://github.com/apache/incubator-devlake/issues/715" rel="noopener noreferrer" target="_blank">#715 (Done)</a></li><li>TAPD <a href="https://github.com/apache/incubator-devlake/issues/560" rel="noopener noreferrer" target="_blank">#560 (Beta)</a></li><li>Zentao <a href="https://github.com/apache/incubator-devlake/issues/2961" rel="noopener noreferrer" target="_blank">#2961 (Beta)</a></li><li>Teambition <a href="https://github.com/apache/incubator-devlake/issues/1882" rel="noopener noreferrer" target="_blank">#1882 (Beta)</a></li><li>Trello <a href="https://github.com/apache/incubator-devlake/issues/1881" rel="noopener noreferrer" target="_blank">#1881 (Pending)</a></li><li>Ones <a href="https://github.com/apache/incubator-devlake/issues/1884" rel="noopener noreferrer" target="_blank">#1884 (Pending)</a></li></ul> Source Code Management: <ul><li>GitHub (Done)</li><li>GitLab (Done)</li><li>BitBucket <a href="https://github.com/apache/incubator-devlake/issues/2100" rel="noopener noreferrer" target="_blank">#2100 (Supported from v0.16)</a></li><li>Azure DevOps <a href="https://github.com/apache/incubator-devlake/issues/2604" rel="noopener noreferrer" target="_blank">#2604 (Supported from v0.16)</a></li><li>Gitee <a href="https://github.com/apache/incubator-devlake/issues/1883" rel="noopener noreferrer" target="_blank">#1883 (WIP)</a></li><li>Coder <a href="https://github.com/apache/incubator-devlake/issues/3447" rel="noopener noreferrer" target="_blank">#3447 (Pending)</a></li></ul> Code Review: <ul><li>GitHub PRs (Done)</li><li>GitLab MRs (Done)</li><li>BitBucket PRs <a href="https://github.com/apache/incubator-devlake/issues/2100" rel="noopener noreferrer" target="_blank">#2100 (Supported from v0.16)</a></li><li>Azure DevOps PRs <a href="https://github.com/apache/incubator-devlake/issues/2604" rel="noopener noreferrer" target="_blank">#2604 (Supported from v0.16)</a></li><li>Phabricator (Pending)</li><li>Gerrit (Pending)</li></ul> CI/CD: <ul><li>GitHub Action <a href="https://github.com/apache/incubator-devlake/issues/2584" rel="noopener noreferrer" target="_blank">#2584 (Done)</a></li><li>GitLab CI <a href="https://github.com/apache/incubator-devlake/issues/2583" rel="noopener noreferrer" target="_blank">#2583 (Done)</a></li><li>Jenkins <a href="https://github.com/apache/incubator-devlake/issues/2637" rel="noopener noreferrer" target="_blank">#2637 (Done)</a></li><li>Bamboo CI <a href="https://github.com/apache/incubator-devlake/issues/3322" rel="noopener noreferrer" target="_blank">#3322 (WIP)</a></li><li>Argo CI <a href="https://github.com/apache/incubator-devlake/issues/2584" rel="noopener noreferrer" target="_blank">#2585 (Pending)</a></li><li>Argo CD <a href="https://github.com/apache/incubator-devlake/issues/5207" rel="noopener noreferrer" target="_blank">#5207 (Pending)</a></li><li>TeamCity (Pending)</li></ul>Code Quality: <ul><li>SonarQube <a href="https://github.com/apache/incubator-devlake/issues/2305" rel="noopener noreferrer" target="_blank">#2305 (Supported from v0.16)</a></li><li>Coverity (Pending)</li></ul> Incident Management: <ul><li>PagerDuty <a href="https://github.com/apache/incubator-devlake/issues/3498" rel="noopener noreferrer" target="_blank">#3498 (WIP)</a></li><li>ServiceNow <a href="https://github.com/apache/incubator-devlake/issues/4234" rel="noopener noreferrer" target="_blank">#4234 (Planned)</a></li></ul> QA: <ul><li>Selenium (Pending)</li><li>Junit (Pending)</li><li>JMeter (Pending)</li><li>Cucumber Test (Pending)</li></ul> Documentation: <ul><li>Google Docs (Pending)</li><li>Lark Docs (Pending)</li><li>Tencent Docs (Pending)</li></ul> Calendar: <ul><li>Lark Calendar <a href="https://github.com/apache/incubator-devlake/issues/261" rel="noopener noreferrer" target="_blank">#261 (Done)</a></li><li>Google Calendar (Pending)</li><li>Zoom Calendar (Pending)</li><li>Tencent Calendar (Pending)</li></ul> OSS Community Metrics: <ul><li>GitHub stars, clones, watches <a href="https://github.com/apache/incubator-devlake/issues/3721" rel="noopener noreferrer" target="_blank">#3721 (WIP)</a></li></ul> Instant Messaging: <ul><li>Slack (Pending)</li><li>Discord (Pending)</li><li>Lark messages (Pending)</li></ul></td></tr><tr><td>Improved data collection, <a href="#datamodels-devlakedomainlayerschema">data models</a> and data extensibility (Goal No.2)</td><td>Data Collection:
 <ul><li>Complete the logging system</li><li>Implement a good error handling mechanism during data collection</li></ul> Data Models:<ul><li>Introduce DBT to allow users to create and modify the domain layer schema. <a href="https://github.com/apache/incubator-devlake/issues/1479" rel="noopener noreferrer" target="_blank">#1479 (Done)</a></li><li>Design the data models for 6 new domains, please refers to the data models of the tools under each domain (see the cell above):<ul><li>Code Quality (WIP)</li><li>Testing</li><li>Calendar</li><li>Documentation</li><li>OSS Community Metrics (WIP)</li><li>Instant messaging</li></ul></li><li>Polish the data models for <a href="#datamodels-devlakedomainlayerschema">existing domains</a>: Issue/Task Management, Source Code Management, Code Review and CI/CD.</li></ul> Data Extensibility: <ul><li>Enhance the performance of data application under large-scaled usage scenarios</li><li>Support OLAP databases for more flexible data storage options</li></ul></td></tr><tr><td>Better user experience (Goal No.3)</td><td>For new users: <ul><li> Iterate on a clearer step-by-step guide to improve the pre-configuration experience.</li><li>Provide a new Config UI to reduce frictions for data configuration <a href="https://github.com/apache/incubator-devlake/issues/1700" rel="noopener noreferrer" target="_blank">#1700 (Done)</a></li><li> Showcase dashboard live demos to let users explore and learn about the dashboards. <a href="https://github.com/apache/incubator-devlake/issues/1784" rel="noopener noreferrer" target="_blank">#1784 (Done)</a></li></ul>For returning users: <ul><li>Provide detailed guides to help users customize Grafana dashboards.</li><li>Work on the documentation for advanced features in the Config UI, such as the usage of Advanced Mode and replacements of old auth tokens for data connections.</li></ul>For contributors:<ul><li>Add more guide to set up DevLake in different operating system.</li><li>Provide clearer docs for contributors to get on board easier.</li><li>Add Swagger to document API <a href="https://github.com/apache/incubator-devlake/issues/292" rel="noopener noreferrer" target="_blank">#292 (Done)</a></li><li>More docs about raw/tool/domain data models</li></ul></td></tr></tbody></table>
<a id="overview-roadmap--how-to-influence-the-roadmap"></a>

## How to Influence the Roadmap

A roadmap is only useful when it captures real user needs. We are glad to hear from you if you have specific use cases, feedback, or ideas. You can submit an issue to let us know!
Also, if you plan to work (or are already working) on a new or existing feature, tell us, so that we can update the roadmap accordingly. We are happy to share knowledge and context to help your feature land successfully.

- [Goals](#overview-roadmap--goals)
- [Feature Breakdown](#overview-roadmap--feature-breakdown)
- [How to Influence the Roadmap](#overview-roadmap--how-to-influence-the-roadmap)

---

<a id="gettingstarted"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/GettingStarted/ -->

<!-- page_index: 8 -->

# Getting Started

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Getting Started

[## 📄️ Quick Start

The steps to utilize Apache DevLake](#gettingstarted-quickstart)

[## 📄️ Install via Docker Compose

The steps to install DevLake via Docker Compose](#gettingstarted-dockercomposesetup)

[## 📄️ Install via Helm

The steps to install Apache DevLake via Helm for Kubernetes](#gettingstarted-helmsetup)

[## 📄️ Upgrade

How to upgrade your Apache DevLake to a newer version](#gettingstarted-upgrade)

[## 📄️ Security and Authentication

How to secure your deployment and enable the Authentication](#gettingstarted-authentication)

---

<a id="gettingstarted-quickstart"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/GettingStarted/QuickStart/ -->

<!-- page_index: 9 -->

# Quick Start

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Quick Start

The key steps to deploy and utilize Apache DevLake.

<a id="gettingstarted-quickstart--step-1-install-devlake"></a>

## Step 1. Install DevLake

Install DevLake using either [Docker Compose](#gettingstarted-dockercomposesetup) or [Helm](#gettingstarted-helmsetup). If you want to upgrade DevLake to a newer version, please refer to the [upgrade manuals](#gettingstarted-upgrade).

<a id="gettingstarted-quickstart--step-2-configure-devlake"></a>

## Step 2. Configure DevLake

Configure DevLake via the Config UI. Follow the [turorial](https://devlake.apache.org/docs/Configuration/Tutorial) for configuration instructions. If you specifically want to configure DORA metrics, please refer to the [DORA manuals](https://devlake.apache.org/docs/DORA) for detailed instructions.

<a id="gettingstarted-quickstart--step-3-view-data-in-grafana-dashboards"></a>

## Step 3. View Data in Grafana Dashboards

After configuring DevLake and collecting data, access the Config UI and click the "Dashboards" button in the top-right corner to view the data in Grafana dashboards. For comprehensive instructions, please refer to the [Grafana manuals](https://devlake.apache.org/docs/Configuration/Dashboards/GrafanaUserGuide).

- [Step 1. Install DevLake](#gettingstarted-quickstart--step-1-install-devlake)
- [Step 2. Configure DevLake](#gettingstarted-quickstart--step-2-configure-devlake)
- [Step 3. View Data in Grafana Dashboards](#gettingstarted-quickstart--step-3-view-data-in-grafana-dashboards)

---

<a id="gettingstarted-dockercomposesetup"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/GettingStarted/DockerComposeSetup/ -->

<!-- page_index: 10 -->

# Install via Docker Compose

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Install via Docker Compose

<a id="gettingstarted-dockercomposesetup--prerequisites"></a>

## Prerequisites

- [Docker v19.03.10+](https://docs.docker.com/get-docker)
- [docker-compose v2.2.3+](https://docs.docker.com/compose/install/) (If you have Docker Desktop installed then you already have the Compose plugin installed)

<a id="gettingstarted-dockercomposesetup--launch-devlake"></a>

## Launch DevLake

1. Download `docker-compose.yml` and `env.example` from the [latest release](https://github.com/apache/incubator-devlake/releases) into a folder.
2. Rename `env.example` to `.env`. For Mac/Linux users, please run `mv env.example .env` in the terminal. This file contains the environment variables that the Devlake server will use. Additional ones can be found in the compose file(s).
3. Generate a secure encryption key using a method such as OpenSSL. For example, run the following command to generate a 128-character string consisting of uppercase letters:


```text
openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1
```

   Copy the generated string. Set the value of the ENCRYPTION\_SECRET environment variable:

   - Method 1: In the docker-compose.yml, set an environment variable ENCRYPTION\_SECRET: "copied string"
   - Method 2: Alternatively, you can set the ENCRYPTION\_SECRET environment variable in the .env file: ENCRYPTION\_SECRET="copied string"

     If you set the ENCRYPTION\_SECRET environment variable in both docker-compose.yml and the .env file, the value set in docker-compose.yml takes precedence.

   **Please make sure to keep the ENCRYPTION\_SECRET safe as it is used to encrypt sensitive information in the database, such as personal access tokens and passwords. If ENCRYPTION\_SECRET is lost, it may not be possible to decrypt this sensitive information.**
4. By default, the timezone is UTC. You can change it by adjusting the env variable TZ in docker-compose.yml
5. Run `docker-compose up -d` if the version of Docker Desktop is too low to use `docker compose up -d`.

<a id="gettingstarted-dockercomposesetup--collect-data-and-view-dashboards"></a>

## Collect data and view dashboards

1. Visit "config-ui" at `http://localhost:4000` in your browser to configure DevLake and collect data.
   - Please follow the [tutorial](#configuration-tutorial)
   - "devlake" container takes a while to fully boot up. If "config-ui" complains about API being unreachable, please wait a few seconds and refresh the page.
2. To view dashboards, click *View Dashboards* button in the top left corner, or visit `localhost:3002` (username: "admin", password: "admin").
   - We use [Grafana](https://grafana.com/) to visualize the DevOps [data](#overview-supporteddatasources) and build dashboards.
   - For how to customize and provision dashboards, please see our [Grafana doc](#configuration-dashboards-grafanauserguide).

<a id="gettingstarted-dockercomposesetup--upgrade"></a>

## Upgrade

> [!WARNING]
> **caution**
> - **Back up your Grafana dashboards** before upgrading if you have modified/customized any dashboards. You can re-import these dashboards to Grafana after the upgrade.
> - **If you are upgrading from DevLake v0.17.x or earlier versions to v0.18.x or later versions**, you need to find the ENCODE\_KEY value in the .env file of devlake container, and assign the value to ENCRYPTION\_SECRET via .env file or environment variable in docker-compose.yml

1. Run `docker-compose down` to stop services;
2. Download `docker-compose.yml` and `env.example` from the [latest release](https://github.com/apache/incubator-devlake/releases).
3. Use the new `docker-compose.yml` and `env.example` to replace the old `docker-compose.yml` and `.env`; Or if you have modified/customized values in the old files, compare the new files with the old ones, adjust the old files according to the new ones.
4. [Optional] If you are upgrading from earlier versions to v0.18.0+, set the ENCRYPTION\_SECRET environment variable in docker-compose.yml or .env file, refer to the second caution.
5. Run `docker-compose up -d` to start DevLake services.

<a id="gettingstarted-dockercomposesetup--faq"></a>

## FAQ

<a id="gettingstarted-dockercomposesetup--can-i-use-a-managed-cloud-database-service-instead-of-running-database-in-docker"></a>

### Can I use a managed cloud database service instead of running database in Docker?

Yes, please follow the steps below:

1. Comment out the 'mysql' part in `docker-compose.yml`:

```yaml
mysql:
  image: mysql:8
  volumes:
    - mysql-storage:/var/lib/mysql
  restart: always
  ports:
    - "127.0.0.1:3306:3306"
  environment:
    MYSQL_ROOT_PASSWORD: admin
    MYSQL_DATABASE: lake
    MYSQL_USER: merico
    MYSQL_PASSWORD: merico
  command: --character-set-server=utf8mb4
    --collation-server=utf8mb4_bin
```

2. Comment out the 'mysql' volume in `docker-compose.yml`:

```yaml
volumes:
  mysql-storage:
```

3. Comment out the 'depends\_on mysql' part in `docker-compose.yml`:

```yaml
depends_on:
  - mysql
```

4. Provide your managed cloud database connection info in the 'grafana' section in `docker-compose.yml`:

- MYSQL\_URL: This parameter specifies the URL of your database instance. For example, if your database is hosted on a server with IP address 123.45.67.89 and port number 3306, the URL would be "123.45.67.89:3306".
- MYSQL\_DATABASE: This parameter specifies the name of your database. For example, if your database is named "mydatabase", you would set this parameter to "mydatabase".
- MYSQL\_USER: This parameter specifies the username that you will use to connect to your database. For example, if your username is "myuser", you would set this parameter to "myuser".
- MYSQL\_PASSWORD: This parameter specifies the password that you will use to connect to your database. For example, if your password is "mypassword", you would set this parameter to "mypassword".

```yaml
MYSQL_URL: 123.45.67.89:3306
MYSQL_DATABASE: mydatabase
MYSQL_USER: myuser
MYSQL_PASSWORD: mypassword
```

5. Set DB\_URL to your own DB\_URL in `.env`:

```bash
DB_URL="mysql://YOUR_USER:YOUR_PASSWORD@YOUR_IP:YOUR_PORT/lake?charset=utf8mb4&parseTime=True"
# Don't forget to create db named `lake` in your own db, and set character-set-server=utf8mb4, collation-server=utf8mb4_bin as below
#      character-set-server=utf8mb4
#      collation-server=utf8mb4_bin
```

6. Final step: `docker compose up -d`

<a id="gettingstarted-dockercomposesetup--can-i-use-an-external-grafana-instead-of-running-grafana-in-docker"></a>

### Can I use an external Grafana instead of running Grafana in Docker?

Yes, please follow the steps below:

1. Comment out the 'grafana' part:

```yaml
grafana:
  image: mericodev/devlake-dashboard:latest
  build:
    context: grafana/
  ports:
    - "3002:3000"
  volumes:
    - grafana-storage:/var/lib/grafana
  environment:
    GF_SERVER_ROOT_URL: "http://localhost:4000/grafana"
    GF_USERS_DEFAULT_THEME: "light"
    MYSQL_URL: mysql:3306
    MYSQL_DATABASE: lake
    MYSQL_USER: merico
    MYSQL_PASSWORD: merico
  restart: always
  depends_on:
    - mysql
```

2. Comment out grafana volume:

```yaml
volumes:
  grafana-storage:
```

3. Set up the `config-ui` container to adopt the external Grafana in the `docker-compose.yml`

```yaml
config-ui:
  ...
  environment:
    USE_EXTERNAL_GRAFANA: "true"
    GRAFANA_ENDPOINT: "http://grafana.example.com"
  ...
```

4. Please connect your Grafana to DevLake's database by following <https://grafana.com/docs/grafana/latest/administration/data-source-management/>
5. If you want to import dashboards, please check <https://grafana.com/docs/grafana/latest/dashboards/export-import/>.

- You can find DevLake's self-built Grafana dashboards here (<https://github.com/apache/incubator-devlake/tree/main/grafana/dashboards>).

6. Final step: `docker compose up -d`

<a id="gettingstarted-dockercomposesetup--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-installation) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Prerequisites](#gettingstarted-dockercomposesetup--prerequisites)
- [Launch DevLake](#gettingstarted-dockercomposesetup--launch-devlake)
- [Collect data and view dashboards](#gettingstarted-dockercomposesetup--collect-data-and-view-dashboards)
- [Upgrade](#gettingstarted-dockercomposesetup--upgrade)
- [FAQ](#gettingstarted-dockercomposesetup--faq)
  - [Can I use a managed cloud database service instead of running database in Docker?](#gettingstarted-dockercomposesetup--can-i-use-a-managed-cloud-database-service-instead-of-running-database-in-docker)
  - [Can I use an external Grafana instead of running Grafana in Docker?](#gettingstarted-dockercomposesetup--can-i-use-an-external-grafana-instead-of-running-grafana-in-docker)
- [Troubleshooting](#gettingstarted-dockercomposesetup--troubleshooting)

---

<a id="gettingstarted-helmsetup"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/GettingStarted/HelmSetup/ -->

<!-- page_index: 11 -->

# Install via Helm

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Install via Helm

<a id="gettingstarted-helmsetup--prerequisites"></a>

## Prerequisites

- Helm >= 3.6.0
- Kubernetes >= 1.19.0

<a id="gettingstarted-helmsetup--quick-start"></a>

## Quick Start

<a id="gettingstarted-helmsetup--you-can-also-check-httpsgithubcomapacheincubator-devlake-helm-chart-to-make-contribution"></a>

#### You can also check <https://github.com/apache/incubator-devlake-helm-chart> to make contribution

<a id="gettingstarted-helmsetup--to-install-or-upgrade-to-the-latest-version-please-check-here"></a>

#### To install or upgrade to the latest version, please check [here](https://github.com/apache/incubator-devlake-helm-chart/releases)

<a id="gettingstarted-helmsetup--install"></a>

### Install

To install the chart with release name `devlake`,follow these steps:

1. Generate a secure encryption key using a method such as OpenSSL. For example, run the following command to generate a 128-character string consisting of uppercase letters:


```text
openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1
```

2. Copy the generated string, set the value of the ENCRYPTION\_SECRET environment variable by running the following command:


```text
export ENCRYPTION_SECRET="copied string"
```

   This command will set the `ENCRYPTION_SECRET` environment variable to the value of the copied string.

   **Please make sure to keep the ENCRYPTION\_SECRET safe as it is used to encrypt sensitive information in the database, such as personal access tokens and passwords. If ENCRYPTION\_SECRET is lost, it may not be possible to decrypt this sensitive information.**
3. By default, the timezone is UTC. To customize the timezone settings, apply the `--set commonEnvs.TZ="your timezone",grafana.env.TZ="your timezone"` command. For further guidance, please refer to [FAQ](#gettingstarted-helmsetup--faq).
4. By default, a random password is generated and stored in a Kubernetes Secret for the Grafana admin user. Alternatively, you can explicitly set the password via `--set grafana.adminPassword=<your password>`. For further guidance, please refer to [FAQ](#gettingstarted-helmsetup--faq).
5. Install the chart by running the following commands:


```shell
helm repo add devlake https://apache.github.io/incubator-devlake-helm-chart
helm repo update
helm install devlake devlake/devlake --version=1.0-beta1 --set lake.encryptionSecret.secret=$ENCRYPTION_SECRET
```

And visit your devlake from the node port (32001 by default).

http://YOUR-NODE-IP:32001

<a id="gettingstarted-helmsetup--tips"></a>

#### Tips:

If you are using minikube inside your mac, please use the following command to forward the port:

```shell
kubectl port-forward service/devlake-ui  30090:4000
```

and open another terminal:

```shell
kubectl port-forward service/devlake-grafana  30091:3000
```

Then you can visit:
config-ui by url `http://YOUR-NODE-IP:30090`
grafana by url `http://YOUR-NODE-IP:30091`

<a id="gettingstarted-helmsetup--upgrade"></a>

### Upgrade

> [!WARNING]
> **caution**
> **Back up your Grafana dashboards** before upgrading if you have modified/customized any dashboards. You can re-import these dashboards to Grafana after the upgrade.

**If you are upgrading from DevLake v0.18.x or later versions:**

```shell
helm repo update
helm upgrade devlake devlake/devlake --version=1.0-beta1
```

**If you are upgrading from DevLake v0.17.x or earlier versions to v0.18.x or later versions:**

1. Copy the ENCODE\_KEY value from /app/config/.env of the lake pod (e.g. devlake-lake-0), and replace the <ENCRYPTION\_SECRET> in the upgrade command below.
2. You may encounter the below error when upgrading because the built-in grafana has been replaced by the official grafana dependency. So you may need to delete the grafana deployment first.

   > Error: UPGRADE FAILED: cannot patch "devlake-grafana" with kind Deployment: Deployment.apps "devlake-grafana" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/instance":"devlake", "app.kubernetes.io/name":"grafana"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable


```shell
helm repo update
helm upgrade devlake devlake/devlake --version=1.0-beta1 --set lake.encryptionSecret.secret=<ENCRYPTION_SECRET>
```

<a id="gettingstarted-helmsetup--uninstall"></a>

### Uninstall

To uninstall/delete the `devlake` release:

```shell
helm uninstall devlake
```

<a id="gettingstarted-helmsetup--some-example-deployments"></a>

## Some example deployments

<a id="gettingstarted-helmsetup--deploy-with-nodeport"></a>

### Deploy with NodePort

Conditions:

- IP Address of Kubernetes node: 192.168.0.6
- Want to visit devlake with port 30000.

```text
ENCRYPTION_SECRET=$(openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1)
helm install devlake devlake/devlake --set service.uiPort=30000 --set lake.encryptionSecret.secret=$ENCRYPTION_SECRET
```

After deployed, visit devlake: <http://192.168.0.6:30000>

<a id="gettingstarted-helmsetup--deploy-with-ingress"></a>

### Deploy with Ingress

Conditions:

- I have already configured default ingress for the Kubernetes cluster
- I want to use <http://devlake.example.com> for visiting devlake

```text
ENCRYPTION_SECRET=$(openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1)
helm install devlake devlake/devlake --set "ingress.enabled=true,ingress.hostname=devlake.example.com" --set lake.encryptionSecret.secret=$ENCRYPTION_SECRET
```

After deployed, visit devlake: <http://devlake.example.com>, and grafana at <http://devlake.example.com/grafana>

<a id="gettingstarted-helmsetup--deploy-with-ingress-https"></a>

### Deploy with Ingress (Https)

Conditions:

- I have already configured ingress(class: nginx) for the Kubernetes cluster, and the https using 8443 port.
- I want to use <https://devlake-0.example.com:8443> for visiting devlake.
- The https certificates are generated by letsencrypt.org, and the certificate and key files: `cert.pem` and `key.pem`

First, create the secret:

```text
kubectl create secret tls ssl-certificate --cert cert.pem --key secret.pem
```

Then, deploy the devlake:

```text
ENCRYPTION_SECRET=$(openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1)
helm install devlake devlake/devlake \
    --set "ingress.enabled=true,ingress.enableHttps=true,ingress.hostname=devlake-0.example.com" \
    --set "ingress.className=nginx,ingress.httpsPort=8443" \
    --set "ingress.tlsSecretName=ssl-certificate"
    --set lake.encryptionSecret.secret=$ENCRYPTION_SECRET
```

After deployed, visit devlake: <https://devlake-0.example.com:8443>, and grafana at <https://devlake-0.example.com:8443/grafana>

<a id="gettingstarted-helmsetup--parameters"></a>

## Parameters

Some useful parameters for the chart, you could also check them in values.yaml

<table><thead><tr><th>Parameter</th><th>Description</th><th>Default</th></tr></thead><tbody><tr><td>replicaCount</td><td>Replica Count for devlake, currently not used</td><td>1</td></tr><tr><td>imageTag</td><td>The version tag for all images</td><td>see Values.yaml</td></tr><tr><td>commonEnvs</td><td>The common envs for all pods except grafana</td><td>{TZ: "UTC"}</td></tr><tr><td>mysql.useExternal</td><td>If use external mysql server, set true</td><td>false</td></tr><tr><td>mysql.externalServer</td><td>External mysql server address</td><td>127.0.0.1</td></tr><tr><td>mysql.externalPort</td><td>External mysql server port</td><td>3306</td></tr><tr><td>mysql.username</td><td>username for mysql</td><td>merico</td></tr><tr><td>mysql.password</td><td>password for mysql</td><td>merico</td></tr><tr><td>mysql.database</td><td>database for mysql</td><td>lake</td></tr><tr><td>mysql.rootPassword</td><td>root password for mysql</td><td>admin</td></tr><tr><td>mysql.storage.type</td><td>storage type, pvc or hostpath</td><td>pvc</td></tr><tr><td>mysql.storage.class</td><td>storage class for mysql's volume</td><td>""</td></tr><tr><td>mysql.storage.size</td><td>volume size for mysql's data</td><td>5Gi</td></tr><tr><td>mysql.storage.hostPath</td><td>the host path if mysql.storage.type is hostpath</td><td>/devlake/mysql/data</td></tr><tr><td>mysql.image.repository</td><td>repository for mysql's image</td><td>mysql</td></tr><tr><td>mysql.image.tag</td><td>image tag for mysql's image</td><td>8</td></tr><tr><td>mysql.image.pullPolicy</td><td>pullPolicy for mysql's image</td><td>IfNotPresent</td></tr><tr><td>mysql.initContainers</td><td>init containers to run to complete before mysql</td><td>[]</td></tr><tr><td>mysql.extraLabels</td><td>extra labels for mysql's statefulset</td><td>{}</td></tr><tr><td>mysql.securityContext</td><td>pod security context values</td><td>{}</td></tr><tr><td>mysql.containerSecurityContext</td><td>container security context values</td><td>{}</td></tr><tr><td>mysql.service.type</td><td>mysql service type</td><td>ClusterIP</td></tr><tr><td>mysql.service.nodePort</td><td>specify mysql nodeport</td><td>""</td></tr><tr><td>grafana</td><td>dashboard, datasource, etc. settings for grafana, installed by grafana official chart</td><td></td></tr><tr><td>lake.image.repository</td><td>repository for lake's image</td><td>apache/devlake</td></tr><tr><td>lake.image.pullPolicy</td><td>pullPolicy for lake's image</td><td>Always</td></tr><tr><td>lake.port</td><td>the port of devlake backend</td><td>8080</td></tr><tr><td>lake.envs</td><td>initial envs for lake</td><td>see Values.yaml</td></tr><tr><td>lake.extraEnvsFromSecret</td><td>existing secret name of extra envs</td><td>""</td></tr><tr><td>lake.encryptionSecret.secretName</td><td>the k8s secret name for ENCRYPTION_SECRET</td><td>""</td></tr><tr><td>lake.encryptionSecret.secret</td><td>the secret for ENCRYPTION_SECRET</td><td>""</td></tr><tr><td>lake.encryptionSecret.autoCreateSecret</td><td>whether let the helm chart create the secret</td><td>true</td></tr><tr><td>lake.extraLabels</td><td>extra labels for lake's statefulset</td><td>{}</td></tr><tr><td>lake.securityContext</td><td>pod security context values</td><td>{}</td></tr><tr><td>lake.containerSecurityContext</td><td>container security context values</td><td>{}</td></tr><tr><td>ui.image.repository</td><td>repository for ui's image</td><td>apache/devlake-config-ui</td></tr><tr><td>ui.image.pullPolicy</td><td>pullPolicy for ui's image</td><td>Always</td></tr><tr><td>ui.basicAuth.enabled</td><td>If the basic auth in ui is enabled</td><td>false</td></tr><tr><td>ui.basicAuth.user</td><td>The user name for the basic auth</td><td>"admin"</td></tr><tr><td>ui.basicAuth.password</td><td>The password for the basic auth</td><td>"admin"</td></tr><tr><td>ui.basicAuth.autoCreateSecret</td><td>If let the helm chart create the secret</td><td>true</td></tr><tr><td>ui.basicAuth.secretName</td><td>The basic auth secret name</td><td>""</td></tr><tr><td>ui.extraLabels</td><td>extra labels for ui's statefulset</td><td>{}</td></tr><tr><td>ui.securityContext</td><td>pod security context values</td><td>{}</td></tr><tr><td>ui.containerSecurityContext</td><td>container security context values</td><td>{}</td></tr><tr><td>service.type</td><td>Service type for exposed service</td><td>NodePort</td></tr><tr><td>service.uiPort</td><td>Node port for config ui</td><td>32001</td></tr><tr><td>service.ingress.enabled</td><td>If enable ingress</td><td>false</td></tr><tr><td>service.ingress.enableHttps</td><td>If enable https</td><td>false</td></tr><tr><td>service.ingress.className</td><td>Name for ingressClass. leave empty for using default</td><td>""</td></tr><tr><td>service.ingress.hostname</td><td>The hostname/domainname for ingress</td><td>localhost</td></tr><tr><td>service.ingress.prefix</td><td>The prefix for endpoints, currently not used</td><td>/</td></tr><tr><td>service.ingress.tlsSecretName</td><td>The secret name for tls's certificate for https</td><td>""</td></tr><tr><td>service.ingress.httpPort</td><td>The http port for ingress</td><td>80</td></tr><tr><td>service.ingress.httpsPort</td><td>The https port for ingress</td><td>443</td></tr><tr><td>option.database</td><td>The database type, valids: mysql</td><td>mysql</td></tr><tr><td>option.connectionSecretName</td><td>The database connection details secret name</td><td>devlake-mysql-auth</td></tr><tr><td>option.autoCreateSecret</td><td>If let the helm chart create the secret</td><td>true</td></tr></tbody></table>
<a id="gettingstarted-helmsetup--faq"></a>

## FAQ

1. Can I use a managed Cloud database service instead of running database in docker?

Yes, it just set useExternal value to true while you deploy devlake with helm chart. Below we'll use MySQL on AWS RDS as an example.

a. (Optional) Create a MySQL instance on AWS RDS following this [doc](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html), skip this step if you'd like to use an existing instance
b. Proviede below values while install from helm:

```text
- `mysql.useExternal`: this should be `true`
- `mysql.externalServer`: use your RDS instance's IP address or domain name.
- `mysql.externalPort`: use your RDS instance's database port.
- `mysql.username`: use your `username` for access RDS instance's DB
- `mysql.password`: use your `password` for access RDS instance's DB
- `mysql.database`: use your RDS instance's DB name, you may need to create a database first with `CREATE DATABASE <DB name>;`
```

Here is the example:

```text
helm repo add devlake https://apache.github.io/incubator-devlake-helm-chart
helm repo update
ENCRYPTION_SECRET=$(openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1)
helm install devlake devlake/devlake \
  --set mysql.useExternal=true \
  --set mysql.externalServer=db.example.com \
  --set mysql.externalPort=3306 \
  --set mysql.username=admin \
  --set mysql.password=password_4_admin \
  --set mysql.database=devlake
  --set lake.encryptionSecret.secret=$ENCRYPTION_SECRET
```

2. Can I use a secret to store the database connection details?

Yes, to do so, you need to have a secret in your Kubernetes Cluster that contains the following values:

- `MYSQL_USER`: The user to connect to your DB.
- `MYSQL_PASSWORD`: The password to connect to your DB.
- `MYSQL_DATABASE`: The database to connect to your DB.
- `MYSQL_ROOT_PASSWORD`: The root password to connect to your DB.
- `DB_URL`: mysql://`username`:`password`@`dbserver`:`port`/`database`?charset=utf8mb4&parseTime=True

The secret name needs to be the same as the value `option.connectionSecretName`

3. Can I use an external Grafana instead of running built-in Grafana?

Yes, the devlake helm chart supports using an external Grafana. You can set the following values while installing from helm:

- `grafana.enabled`: this should be `false`
- `grafana.external.url`: use your Grafana's URL, e.g. `https://grafana.example.com`

Here is the example:

```text
helm repo add devlake https://apache.github.io/incubator-devlake-helm-chart
helm repo update
ENCRYPTION_SECRET=$(openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1)
helm install devlake devlake/devlake \
  --set grafana.enabled=false \
  --set grafana.external.url=https://grafana.example.com
  --set lake.encryptionSecret.secret=$ENCRYPTION_SECRET
```

4. How to set the timezone? If not explicitly set, the default is UTC

- `commonEnvs.TZ`: your timezone
- `grafana.env.TZ`: your timezone

Here is the example:

```text
helm repo add devlake https://apache.github.io/incubator-devlake-helm-chart
helm repo update
ENCRYPTION_SECRET=$(openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1)
helm install devlake devlake/devlake \
  --set commonEnvs.TZ=<your timezone> \
  --set grafana.env.TZ=<your timezone>
```

5. How to set the Grafana admin password? If not explicitly set, a random password will be generated and saved in a Kubernetes Secret

- `grafana.adminPassword`: your password

Here is the example:

```text
helm repo add devlake https://apache.github.io/incubator-devlake-helm-chart
helm repo update
ENCRYPTION_SECRET=$(openssl rand -base64 2000 | tr -dc 'A-Z' | fold -w 128 | head -n 1)
helm install devlake devlake/devlake \
  --set grafana.adminPassword=<your password> \
  --set lake.encryptionSecret.secret=$ENCRYPTION_SECRET
```

<a id="gettingstarted-helmsetup--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-installation) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Prerequisites](#gettingstarted-helmsetup--prerequisites)
- [Quick Start](#gettingstarted-helmsetup--quick-start)
  - [Install](#gettingstarted-helmsetup--install)
  - [Upgrade](#gettingstarted-helmsetup--upgrade)
  - [Uninstall](#gettingstarted-helmsetup--uninstall)
- [Some example deployments](#gettingstarted-helmsetup--some-example-deployments)
  - [Deploy with NodePort](#gettingstarted-helmsetup--deploy-with-nodeport)
  - [Deploy with Ingress](#gettingstarted-helmsetup--deploy-with-ingress)
  - [Deploy with Ingress (Https)](#gettingstarted-helmsetup--deploy-with-ingress-https)
- [Parameters](#gettingstarted-helmsetup--parameters)
- [FAQ](#gettingstarted-helmsetup--faq)
- [Troubleshooting](#gettingstarted-helmsetup--troubleshooting)

---

<a id="gettingstarted-upgrade"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/GettingStarted/Upgrade/ -->

<!-- page_index: 12 -->

# Upgrade

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Upgrade

<a id="gettingstarted-upgrade--how-to-upgrade-to-a-new-version"></a>

## How to Upgrade to a new version

Please follow the guide for detailed information:

- Upgrade via [Docker Compose](#gettingstarted-dockercomposesetup--upgrade)
- Upgrade via [Helm](#gettingstarted-helmsetup--upgrade)

<a id="gettingstarted-upgrade--key-points"></a>

## Key points

1. ENCRYPTION\_SECRET: It is important to keep the ENCRYPTION\_SECRET safe as it is used to encrypt sensitive information in the database, such as personal access tokens and passwords. Losing the ENCRYPTION\_SECRET may result in the inability to decrypt this sensitive information.
2. .env file: The .env file is now optional. You can choose to store your variables in the environment instead. Remember to consider important variables such as ENCRYPTION\_SECRET and DB\_URL. If both the environment variables and the .env file exist, the values in the environment variables will take precedence. However, make sure that these variables are defined in either one of them to avoid any issues with DevLake.
3. Back up your Grafana dashboards before upgrade if you have modified/customized any dashboards. You can re-import these dashboards to Grafana after the upgrade.
4. Upgrade to v0.18.0+: When upgrading from a previous version of DevLake, you need to find the ENCODE\_KEY value in the .env file of devlake container, and assign the value to ENCRYPTION\_SECRET according to the upgrade steps, see [helm setup](https://devlake.apache.org/docs/GettingStarted/HelmSetup) or [docker compose setup](https://devlake.apache.org/docs/GettingStarted/DockerComposeSetup). This will ensure that the encryption process continues to work as expected.
5. Upgrade to v0.18.0+: When upgrading from a previous version of DevLake, You may encounter the below error when upgrading because the built-in grafana has been replaced by the official grafana dependency. So you may need to delete the grafana deployment first, please also take care of Note 3 before deleting.

> Error: UPGRADE FAILED: cannot patch "devlake-grafana" with kind Deployment: Deployment.apps "devlake-grafana" is invalid: spec.selector: Invalid value: v1.LabelSelector{MatchLabels:map[string]string{"app.kubernetes.io/instance":"devlake", "app.kubernetes.io/name":"grafana"}, MatchExpressions:[]v1.LabelSelectorRequirement(nil)}: field is immutable

6. When upgrading via docker-compose.yml, please download the new docker-compose.yml and env.example from [release assets](https://github.com/apache/incubator-devlake/releases) to do the upgrade, please refer to [docker compose upgrade notes](#gettingstarted-dockercomposesetup)

These notes provide guidance on upgrading your Apache DevLake to a newer version. Ensure you follow them carefully to avoid any issues during the upgrade process.

- [How to Upgrade to a new version](#gettingstarted-upgrade--how-to-upgrade-to-a-new-version)
- [Key points](#gettingstarted-upgrade--key-points)

---

<a id="gettingstarted-authentication"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/GettingStarted/Authentication/ -->

<!-- page_index: 13 -->

# Security and Authentication

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Security and Authentication

The document explains how you can set up Apache DevLake securely.

First of all, there are 4 services included in the deployment:

- database: `mysql` is supported, you may use it or any other compatible DBS like cloud-based systems. You should follow the document from the database to make it secure.
- grafana: You are likely to use it most of the time, browsing built-in dashboards, and creating your own customized metric. grafana supports [User Management](https://grafana.com/docs/grafana/latest/administration/user-management/), please follow the official document to set it up based on your need.
- devlake: This is the core service for Data Collection and Metric Calculation, all collected/calculated data would be stored to the database, and accessed by the `grafana` service. `devlake` itself doesn't support User Management of any kind, so we don't recommend that you expose its port to the outside world.
- config-ui: A web interface to set up `devlake` to do the work. You may set up an automated `blueprint` to collect data. `config-ui` supports `Basic Authentication`, by simply set up the Environment Variable `ADMIN_USER` and `ADMIN_PASS` for the container. There are commented lines in `config-ui.environment` section in our `docker-compose.yml` file for your convenience.
  In General, we suggest that you reduce the Attack Surface as small as possible.

<a id="gettingstarted-authentication--internal-deployment-recommended"></a>

### Internal Deployment (Recommended)

- database: Remove the `ports` if you don't need to access the database directly
- devlake: Remove the `ports` section. If you want to call the API directly, do it via `config-ui/api` endpoint.
- grafana: We have no choice but to expose the `ports` for people to browse the dashboards. However, you may want to set up the User Management, and a read-only database account for `grafana`
- config-ui: Normally, exposing the `ports` with `Basic Authentication` is sufficient for Internal Deployment, you may choose to remove the `ports` and use techniques like `k8s port-forwarding` or `expose-port-when-needed` to enhance the security. Keep in mind config-ui is NOT designed to be used by many people, and it shouldn't be. Do NOT grant access if NOT necessary.

<a id="gettingstarted-authentication--internet-deployment-not-recommended"></a>

### Internet Deployment (NOT Recommended)

THIS IS DANGEROUS, DON'T DO IT. If you insist, here are some suggestions you may follow, please consult Security Advisor before everything:

- database: Same as above.
- grafana: Same as above. In addition, set up the `HTTPS` for the transportation.
- devlake: Same as above.
- config-ui: Same as above. In addition, use port-forward if you are using `k8s`, otherwise, set up `HTTPS` for the transportation.

<a id="gettingstarted-authentication--disclaimer"></a>

## Disclaimer

Security is complicated, all suggestions listed above are based on what we learned so far. Apache Devlake makes no guarantee of any kind, please consult your Security Advisor before applying.

<a id="gettingstarted-authentication--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-installation) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Internal Deployment (Recommended)](#gettingstarted-authentication--internal-deployment-recommended)
- [Internet Deployment (NOT Recommended)](#gettingstarted-authentication--internet-deployment-not-recommended)
- [Disclaimer](#gettingstarted-authentication--disclaimer)
- [Troubleshooting](#gettingstarted-authentication--troubleshooting)

---

<a id="config-ui"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Config%20UI/ -->

<!-- page_index: 14 -->

# Config UI

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Config UI

[## 📄️ Tutorial

Config UI instruction](#configuration-tutorial)

[## 📄️ How to Organize DevLake Projects

How to Organize DevLake Projects](#configuration-howtoorganizedevlakeprojects)

[## 📄️ Azure DevOps

Config UI instruction for Azure DevOps](#configuration-azuredevops)

[## 📄️ Bitbucket Cloud

Config UI instruction for Bitbucket(Cloud)](#configuration-bitbucket)

[## 📄️ Bitbucket Server/Data Center

Config UI instruction for Bitbucket Server/Data Center](#configuration-bitbucketserver)

[## 📄️ CircleCI

Config UI instruction for CircleCI](#configuration-circleci)

[## 📄️ GitHub

Config UI instruction for GitHub](#configuration-github)

[## 📄️ GitLab

Config UI instruction for GitLab](#configuration-gitlab)

[## 📄️ Opsgenie

Config UI instruction for Opsgenie](#configuration-opsgenie)

[## 📄️ Jenkins

Config UI instruction for Jenkins](#configuration-jenkins)

[## 📄️ Jira

Config UI instruction for Jira](#configuration-jira)

[## 📄️ PagerDuty

Config UI instruction for PagerDuty](#configuration-pagerduty)

[## 📄️ SonarQube Server

Config UI instruction for SonarQube](#configuration-sonarqube)

[## 📄️ TAPD

Config UI instruction for TAPD](#configuration-tapd)

[## 📄️ Teambition(WIP)

Config UI instruction for Teambition](#configuration-teambition)

[## 📄️ Webhooks

Config UI instructions for Webhook](#configuration-webhook)

[## 📄️ Zentao

Config UI instruction for Zentao(禅道)](#configuration-zentao)

[## 📄️ Blueprint Advanced Mode

Using the advanced mode of Config-UI](#configuration-advancedmode)

[## 📄️ API Keys

API Keys](#configuration-apikeys)

[## 📄️ Team Configuration

Team Configuration](#configuration-teamconfiguration)

[## 🗃️ Dashboard Configuration

2 items](#configuration-dashboards-accesscontrol)

---

<a id="configuration-tutorial"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Tutorial/ -->

<!-- page_index: 15 -->

# Tutorial

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Tutorial

The Apache DevLake Config UI provides a user-friendly interface for configuring the data collection process. To access the Config UI, please visit http://localhost:4000.

<a id="configuration-tutorial--basic-configuration"></a>

## Basic Configuration

To ensure the proper functioning of DevLake, follow these two key steps:

<a id="configuration-tutorial--step-1-add-data-connections"></a>

### Step 1 - Add Data Connections

![img](assets/images/data-connections-33cb6723203fd68be912aee3360a62f5_cb140dfa068cae3e.png)

- Step 1.1 - Add a connection. Configure the endpoint and authentication details to connect to the source data.
- Step 1.2 - Add data scope, such as Git repositories, issue boards, or CI/CD pipelines, to determine what data should be collected.
- Step 1.3 - Add scope config (optional). Define the specific data entities within the data scope for collection or apply transformation rules to the raw API responses.

<a id="configuration-tutorial--step-2-collect-data-in-a-project"></a>

### Step 2 - Collect Data in a Project

- Step 2.1 - Create a project. DevLake assesses DORA metrics at the project level. For more information on organizing DevLake projects, please refer to [how to organize DevLake projects](https://devlake.apache.org/docs/Configuration/HowToOrganizeDevlakeProjects) for more details.
- Step 2.2 - Associate connection(s) with the project. When associating a connection with a project, you can select specific data scopes. All connections linked to the same project will be considered part of the same project for calculating DORA metrics.
- Step 2.3 - Set the synchronization policy. Specify the sync frequency, time range and the skip-on-fail option for your data.
- Step 2.4 - Start data collection. Choose the desired [mode](#configuration-tutorial--step-2-collect-data-in-a-project) for collecting data.

<a id="configuration-tutorial--step-3-check-the-data-in-grafana-dashboards"></a>

### Step 3 - Check the Data in Grafana Dashboards

To view the collected data, click on the "Dashboards" button located in the top-right corner of Config UI. For detailed instructions, please refer to the [Grafana manuals](#configuration-dashboards-grafanauserguide).

<a id="configuration-tutorial--examples"></a>

## Examples

For detailed examples, please refer to the respective documentation files available in this folder, such as [GitHub configuration](#configuration-github), [GitLab configuration](#configuration-gitlab), [Jira configuration](#configuration-jira) and more. They provide step-by-step instructions and guidance for configuring DevLake with different platforms.

<a id="configuration-tutorial--qa"></a>

## Q&A

<a id="configuration-tutorial--q1-what-are-the-specific-sync-policies-to-configure"></a>

#### Q1. What are the specific sync policies to configure?

- Time Filter: This allows you to select the desired time range for syncing data, optimizing the collection process.
- Frequency: You can determine the frequency of data synchronization by choosing a sync frequency option or specifying a cron code for a custom schedule.
- Running Policy: By default, the "Skip failed tasks" option is enabled. This helps prevent data loss in scenarios where you are collecting a large volume of data (e.g., 10+ GitHub repositories, Jira boards, etc.). When a task fails, this policy allows the pipeline to continue running, preserving the data collected by successful tasks. You can rerun the failed tasks later from the blueprint's detail page.

<a id="configuration-tutorial--q2-what-data-collection-modes-do-devlake-support"></a>

#### Q2. What data collection modes do DevLake support?

Three modes.

- *Collect Data (Default)*: This mode retrieves data within the specified time range. Tools and entities that support incremental refresh will utilize this method, while those that only support full refresh will perform a full refresh. This mode is the default choice for recurring pipelines.
- *Collect Data in Full Refresh Mode*: In this mode, all existing data within the designated time range will be deleted and re-collected. It is useful for removing outdated or irrelevant data from DevLake that no longer exists in the original tools.
- *Re-transform Data*: This mode does not collect new data. Instead, it applies the latest transformation rules from the Scope Config to the existing data.

<a id="configuration-tutorial--troubleshooting"></a>

## Troubleshooting

<a id="configuration-tutorial--1-what-can-be-done-when-a-data-collection-failed-or-partially-succeeded"></a>

#### 1. What can be done when a data collection failed or partially succeeded?

- First, re-run the failed task once all other tasks have completed. If the task still fails, proceed to the next steps.
- Capture a screenshot of the error message associated with the failed task.
- Download the logs from the pipeline for further analysis.
- Visit the [GitHub repository](https://github.com/apache/incubator-devlake/issues) and create a bug report. Include the captured screenshot and the downloaded logs in the bug report.

  ![img](assets/images/blueprint-edit3-beff0ecb765048a9a008d2b06c0c268a_8f867072fc919e84.png)

For other problems, please check the [troubleshooting](#troubleshooting-configuration) doc, [create an issue](https://github.com/apache/incubator-devlake/issues), or contact us on [Slack](https://join.slack.com/t/devlake-io/shared_invite/zt-1lkgbdmys-AU2azidzO1u~mtjlg9my7A).

- [Basic Configuration](#configuration-tutorial--basic-configuration)
  - [Step 1 - Add Data Connections](#configuration-tutorial--step-1-add-data-connections)
  - [Step 2 - Collect Data in a Project](#configuration-tutorial--step-2-collect-data-in-a-project)
  - [Step 3 - Check the Data in Grafana Dashboards](#configuration-tutorial--step-3-check-the-data-in-grafana-dashboards)
- [Examples](#configuration-tutorial--examples)
- [Q&A](#configuration-tutorial--qa)
- [Troubleshooting](#configuration-tutorial--troubleshooting)

---

<a id="configuration-howtoorganizedevlakeprojects"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/HowToOrganizeDevlakeProjects/ -->

<!-- page_index: 16 -->

# How to Organize DevLake Projects

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# How to Organize DevLake Projects

This guide provides a step-by-step approach to organizing projects in DevLake, enabling you to measure DORA metrics according to your specific use cases.

<a id="configuration-howtoorganizedevlakeprojects--1-what-is-a-devlake-project"></a>

## 1. What is a DevLake project?

On a high level, a DevLake project can be viewed as a real-world project or product line. It represents a specific initiative or endeavor within the software development domain.

On a lower level, a DevLake project is a way of organizing and grouping data from different domains. DevLake uses various [data scopes](https://devlake.apache.org/docs/Overview/KeyConcepts#data-scope), such as repos, boards, cicd\_scopes, and cq\_projects as the 'container' to associate different types of data to a specific project. See more on this [doc](https://devlake.apache.org/docs/Overview/KeyConcepts#project).

<a id="configuration-howtoorganizedevlakeprojects--2-why-is-it-important-to-organize-projects"></a>

## 2. Why is it important to organize projects?

This is crucial due to the fact that DevLake measures DORA metrics at the project level. Each project is associated with specific key entities, such as 'pull requests', 'deployments', and 'incidents', which are used to calculate the corresponding DORA metrics. Therefore, proper project organization ensures accurate and meaningful DORA metric calculations for effective analysis and evaluation.

![](assets/images/project-pipeline-06b394bb2f3453ffd888f20affbe2d5d_311dbba751935852.png)

> How are four [DORA](#dora) metrics calculated from 'pull requests', 'deployments', and 'incidents'?
>
> - [Deployment Frequency](#metrics-deploymentfrequency): How often does a project `deploys`?
> - [Lead Time for Changes](#metrics-leadtimeforchanges): How fast are the `pull requests` delivered?
> - [Change Failure Rate](#metrics-cfr): How many `deployments` lead to `incidents`?
> - [Median Time to Restore](#metrics-mttr): How fast are `incidents` solved?

<a id="configuration-howtoorganizedevlakeprojects--3-challenges-in-project-organization"></a>

## 3. Challenges in project organization

There are several challenges associated with organizing projects in DevLake due to different development practices within teams. Some of these challenges include:

- Managing multiple Git repos, issue boards, and CI/CD pipelines within a project.
- Having a Git repo, issue board, or CI/CD pipeline associated with multiple projects, such as in the case of mono-repos or boards used to track incidents from user feedback.
- Managing multiple projects within a team and the need to measure DORA metrics at the team level.
- Projects contributed by multiple teams, with each team requiring the ability to measure their own DORA metrics.

This document serves as a guide to address these challenges and provide assistance in effectively dealing with these diverse development practices.

<a id="configuration-howtoorganizedevlakeprojects--4-general-advice"></a>

## 4. General advice

<a id="configuration-howtoorganizedevlakeprojects--41-determining-the-number-of-devlake-projects"></a>

### 4.1. Determining the number of DevLake projects

It is advisable to create DevLake projects that align with the number of real-life projects you have.

For example, if you have a team (Team A) responsible for managing multiple projects, it is recommended to create separate DevLake projects for each individual project instead of creating a single project named 'Team A'. This approach allows for better organization and tracking of metrics specific to each project.

<a id="configuration-howtoorganizedevlakeprojects--42-principles-of-organizing-projects"></a>

### 4.2 Principles of organizing projects

When organizing projects in DevLake, it is important to associate all relevant [data scopes](https://devlake.apache.org/docs/Overview/KeyConcepts#data-scope), such as repos, issue boards, and CI/CD scopes, with the corresponding DevLake project based on real-life practices.

In situations where a repo or board is shared by multiple projects in real life, it is recommended to include them in all of these projects within DevLake. This is because DevLake cannot differentiate which commits or issues belong to specific projects. Rather than excluding shared resources from DORA measurements, it is advisable to consider them in all relevant projects.

<a id="configuration-howtoorganizedevlakeprojects--43-measuring-dora-at-the-team-level"></a>

### 4.3 Measuring DORA at the team level

To clarify the concepts, let's define three terms:

- [`Project`](https://devlake.apache.org/docs/Overview/KeyConcepts#project): Refers to a real-world project or product line, such as Apache DevLake or Apache Spark. It focuses on the work to be done.
- `Team`: Represents a department, such as the 'product team' or 'engineering team'. It focuses on the people and their roles. Note that people within the same team may not always work on the same projects.
- `Project Team`: Comprises individuals working on a specific project.

DevLake does support measuring DORA metrics at the project-team level, which is essentially the same as measuring at the project level. However, it is important to note that DevLake does not recommend measuring DORA metrics at the team level. Despite the existence of the 'DORA by team' dashboard contributed by the community. Doing so may introduce inaccuracies and dilute the significance of measuring DORA metrics from the outset.

<a id="configuration-howtoorganizedevlakeprojects--5-use-cases"></a>

## 5. Use Cases

This section demonstrates real-life practices and how they get reflected in DevLake.

Disclaimer: *To keep this guide shorter, some technical details are only mentioned in
[Use Case 1](#configuration-howtoorganizedevlakeprojects--41-use-case-1-apache-projects), so if you read this page for the first time, make sure to go through them in order.*

Note: *If you use webhooks, check the [quick note](#configuration-howtoorganizedevlakeprojects--5-about-webhooks) about them below.*

<a id="configuration-howtoorganizedevlakeprojects--51-use-case-1-apache-projects"></a>

### 5.1. Use Case 1: Apache Projects

Apache Software Foundation (ASF) has and is developing many
[projects](https://en.wikipedia.org/wiki/List_of_Apache_Software_Foundation_projects).

To take an example we will analyze 2 `projects`: DevLake and [Spark](https://spark.apache.org/).
Both are independent of each other. Assume that ASF wants to check the health of the development
and maintenance of these projects with DORA.

DevLake manages 3 `repos`: [incubator-devlake](https://github.com/apache/incubator-devlake), [incubator-devlake-website](https://github.com/apache/incubator-devlake-website), and [incubator-devlake-helm-chart](https://github.com/apache/incubator-devlake-helm-chart).
There are many repos related to *Spark* in one way or another. To keep it simple, we will also pick 3 `repos`: [spark](https://github.com/apache/spark), [spark-website](https://github.com/apache/spark-website), and [incubator-livy](https://github.com/apache/incubator-livy).

![](assets/images/project-use-case-1-9473d6310f48a48761835cb210b50117_8d512aea78b158ed.png)

Both projects use GitHub for storing code (including `pull requests`), `deployments` on GitHub Actions, and `incidents`.

Note: *To avoid confusion between DevLake as a `project` in this use case and DevLake as a platform, we will use complete names i.e. `project DevLake` and `platform DevLake` respectively.*

<a id="configuration-howtoorganizedevlakeprojects--511-organizing-projects"></a>

#### 5.1.1. Organizing Projects

First, create two projects on the DevLake platform, one for DevLake and one for Spark.
These will represent real-world projects.

![](assets/images/create-project-1-6acc9250dc0a4aad6225ebc8c5b2d477_1b29a56e8716eca3.png)
![](assets/images/create-project-2-a1bab3ab059002352d53f2609ca9410d_ea0bf56e44ef1148.png)

Once these are created, the connections created in the following steps will be bound to them.

<a id="configuration-howtoorganizedevlakeprojects--512-creating-connections"></a>

#### 5.1.2. Creating Connections

Since all is on GitHub in this case, we can use just 1 connection with the following properties:

- it includes all the project's `repos`
- its scope includes everything we work with (i.e. `pull requests`, `deployments`, and `incidents`)

If you store `incidents` on Jira, for example, you will need to create a separate connection just for them.
The same applies to `deployments`, a separate connection is needed in case they are stored in Jenkins (or any other host for `deployments`).

<a id="configuration-howtoorganizedevlakeprojects--513-configuring-connections"></a>

#### 5.1.3. Configuring Connections

This part is described in [GitHub](#configuration-github) connection configuration. Please check the [configuration guide](#configuration-tutorial) for configuring other data sources.

<a id="configuration-howtoorganizedevlakeprojects--514-using-connections"></a>

#### 5.1.4. Using Connections

At this point, we have projects and connections created on the platform DevLake.
It is time to bind those connections to the projects. To do so, follow the steps described in the [Tutorial](#configuration-tutorial).

<a id="configuration-howtoorganizedevlakeprojects--515-resulting-metrics"></a>

#### 5.1.5. Resulting Metrics

To know if the data of a project is successfully collected to your DORA Dashboard:

![](assets/images/navigate-to-dora-1-cc59f31f0dcb5e45750e6ae972675a8b_240afa5a3204a098.png)
![](assets/images/navigate-to-dora-2-047353792d77d9c6e828e6f13b84fbf3_1a6d4b25494d4267.png)

If everything goes well, you should see all the 4 charts.
If something is wrong, and you are puzzled as to why, check out the
[Debugging Dora Issue Metrics](#troubleshooting-dashboard--debugging-dora-issue-metrics) page.

<a id="configuration-howtoorganizedevlakeprojects--516-how-can-i-observe-metrics-by-project"></a>

#### 5.1.6. How can I observe metrics by project?

In the same DORA dashboard check out this menu point:
![](assets/images/observe-metrics-by-project-panel-74cecdf33da26d2f38c6d0ea8a8de910_420d691fb5066bdc.png)

The metrics should change when you select or deselect projects, representing the projects you selected.

<a id="configuration-howtoorganizedevlakeprojects--52-use-case-2-multiple-teams-with-distinct-projects"></a>

### 5.2. Use Case 2: Multiple Teams with Distinct Projects

Consider a scenario where a company operates with several teams, each managing one or more projects.
For illustration, we will explore two such teams: the Payments team and the Internal Tools team.
Here's a simplified representation of this scenario:

<a id="configuration-howtoorganizedevlakeprojects--quick-overview"></a>

#### Quick Overview:

- The Payments team works on a single project: “payments”.
- The Internal Tools team manages two projects: “it-legacy” and “it-new”.
- Both teams use different sets of tools and boards.

![](assets/images/project-use-case-2-6ea9c31326d89a9095ff32cad07cdc13_b6142b5dfbecb3e9.png)

<a id="configuration-howtoorganizedevlakeprojects--step-by-step-simplification"></a>

#### Step-by-Step Simplification:

1. **Define the Teams and Projects:**
   - **Payments Team**:
     - One project: "payments".
   - **Internal Tools Team**:
     - Two projects: "it-legacy" and "it-new".
2. **Understand the Tools**:
   - Assume both teams utilize GitHub for `repos` and Jenkins for CI/CD.
   - The *Payments* team uses Jira boards.
   - The *Internal Tools* team uses webhooks for reporting incidents.

<a id="configuration-howtoorganizedevlakeprojects--521-organizing-projects"></a>

#### 5.2.1. Organizing Projects

DORA is effective for observing the impacts of methodology changes within a team.
From DORA’s standpoint, the concept of distinct `teams` is not recognized; only `projects` exist.
Adding a `team` concept introduces unnecessary complexity without providing any substantial benefit.

In DevLake, we create three `projects`: *payments*, *it-legacy*, and *it-new*.

It is crucial to maintain **atomic** `projects`, representing the smallest, independent units, to prevent complexity and ensure precise data representation. **Atomic** `projects` allow for a more flexible
and accurate data comparison and combination between `projects`.

<a id="configuration-howtoorganizedevlakeprojects--522-adding-connections"></a>

#### 5.2.2. Adding Connections

Create just one connection and reuse it across projects by adding data scopes.
This method optimizes data collection, minimizing redundancy and ensuring more efficient use of resources.

It is NOT recommended to create multiple connections, for instance, GitHub repos, as it
will increase the time to collect the data due to the storage of multiple copies of shared repos in the database.

The only exception is the webhooks: **we must have 1 connection per project**, as this is the only way DevLake can accurately assign `incidents` to the corresponding `project`.

So, in total we will have only these connections:

- 1 connection for all GitHub `repos` to collect `pull requests`
- 1 connection to Jenkins to collect all `deployments`
- 1 connection to Jira to collect `incidents`
- 2 webhook connections to collect `incidents`: 1 per each `project` that uses webhooks (*it-legacy* and *it-new*)

The step-by-step [Configuration Guide](#configuration-tutorial) shows how to both add connections and set scopes as described in the next chapter.

<a id="configuration-howtoorganizedevlakeprojects--523-setting-scopes"></a>

#### 5.2.3. Setting Scopes

Now, add the connections to our projects and set the scope to them:

For payments `project`:

- add 1 scope to GitHub connection for *p1...p10* `repos` to collect their `pull requests`
- add 1 scope to Jenkins for `deployments` of *p1...p10* `repos`
- add 1 scope to Jira to collect `incidents`

For it-legacy `project`:

- add 1 scope to GitHub for `repos` *it-legacy-1*, *it-legacy-2*, *it-core-1* and *it-core-2* to collect their `pull requests`
- add 1 scope to Jenkins for `deployments` of *it-legacy-1*, *it-legacy-2*, *it-core-1* and *it-core-2* `repos`
- include the *it-legacy* webhook for collecting `incidents`

For it-new `project`:

- add 1 scope to GitHub for `repos` *it-new-1*, *it-new-2*, *it-core-1* and *it-core-2* to collect their `pull requests`
- add 1 scope to Jenkins for `deployments` of *it-new-1*, *it-new-2*, *it-core-1* and *it-core-2* `repos`
- include the *it-new* webhook for collecting `incidents`

<a id="configuration-howtoorganizedevlakeprojects--524-resulting-metrics"></a>

#### 5.2.4. Resulting Metrics

See [5.1.5 Resulting Metrics](#configuration-howtoorganizedevlakeprojects--515-resulting-metrics)

<a id="configuration-howtoorganizedevlakeprojects--6-about-webhooks"></a>

## 6. About Webhooks

**Assigning a UNIQUE webhook to each project is critical.** This ensures that the DevLake platform
correctly associates the incoming data with the corresponding project through the webhook.

If you use the same webhook across multiple projects, the data sent by it **will be replicated per each
project that uses that webhook**. More information available on the [Webhook](https://devlake.apache.org/docs/Plugins/webhook) page

<a id="configuration-howtoorganizedevlakeprojects--7-troubleshooting"></a>

## 7. Troubleshooting

Please check out the [Debugging DORA Issue Metrics](#troubleshooting-dashboard--debugging-dora-issue-metrics) to debug DORA dashboard.

If you still run into any problems, please check the [Troubleshooting](https://devlake.apache.org/docs/Troubleshooting/Configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [1. What is a DevLake project?](#configuration-howtoorganizedevlakeprojects--1-what-is-a-devlake-project)
- [2. Why is it important to organize projects?](#configuration-howtoorganizedevlakeprojects--2-why-is-it-important-to-organize-projects)
- [3. Challenges in project organization](#configuration-howtoorganizedevlakeprojects--3-challenges-in-project-organization)
- [4. General advice](#configuration-howtoorganizedevlakeprojects--4-general-advice)
  - [4.1. Determining the number of DevLake projects](#configuration-howtoorganizedevlakeprojects--41-determining-the-number-of-devlake-projects)
  - [4.2 Principles of organizing projects](#configuration-howtoorganizedevlakeprojects--42-principles-of-organizing-projects)
  - [4.3 Measuring DORA at the team level](#configuration-howtoorganizedevlakeprojects--43-measuring-dora-at-the-team-level)
- [5. Use Cases](#configuration-howtoorganizedevlakeprojects--5-use-cases)
  - [5.1. Use Case 1: Apache Projects](#configuration-howtoorganizedevlakeprojects--51-use-case-1-apache-projects)
  - [5.2. Use Case 2: Multiple Teams with Distinct Projects](#configuration-howtoorganizedevlakeprojects--52-use-case-2-multiple-teams-with-distinct-projects)
- [6. About Webhooks](#configuration-howtoorganizedevlakeprojects--6-about-webhooks)
- [7. Troubleshooting](#configuration-howtoorganizedevlakeprojects--7-troubleshooting)

---

<a id="configuration-azuredevops"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/AzureDevOps/ -->

<!-- page_index: 17 -->

# Azure DevOps

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Azure DevOps

Visit Config UI at: `http://localhost:4000`.

<a id="configuration-azuredevops--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

On the Connections page, you can select GitHub and create a new connection or it.

<a id="configuration-azuredevops--step-11-authentication"></a>

### Step 1.1 - Authentication

![azuredevops-create-a-connection](assets/images/azuredevops-create-a-connection-3a4ecfc90ce12c5dacdb74f3f95df19f_0cead2a69de8b756.png)

<a id="configuration-azuredevops--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-azuredevops--token"></a>

#### Token

Paste your Azure DevOps personal access token (PAT) here. Check [Azure's official doc](https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate?view=azure-devops&tabs=Windows#create-a-pat) on how to create a PAT.
Make sure that the Organization field is set to "All accessible organizations" when creating the PAT.

<a id="configuration-azuredevops--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-azuredevops--step-12-add-data-scopes"></a>

### Step 1.2 - Add Data Scopes

![azuredevops-set-data-scope](assets/images/azuredevops-set-data-scope-30fe830036ca8fdccf9f3b7aa7aa89c0_db5d6bc929f9032f.png)

<a id="configuration-azuredevops--select-repositories"></a>

#### Select repositories

Select the repositories you want to collect data from.

<a id="configuration-azuredevops--data-entities"></a>

#### Data Entities

Azure DevOps supports the following data entities.

- CI/CD: builds and jobs.
- Source Code Management: repositories and their commits.
- Code Review: pull requests and their commits.

<a id="configuration-azuredevops--step-13-add-scope-config-optional"></a>

### Step 1.3 - Add Scope Config (Optional)

![azuredevops-add-scope config](assets/images/azuredevops-add-scope-config-01facab03b3978cb074757de07543d46_36f52aab64c0435d.png)

Scope config contains two parts:

- The entities of which domain you wish to collect: Usually, you don't have to modify this part. However, if you don't want to collect certain Azure DevOps entities, you can unselect some entities to accelerate the collection speed.
  - Source Code Management: Azure repos, refs, commits, etc.
  - Code Review: Azure PRs, PR comments and reviews, etc.
  - CI/CD: Azure pipelines, jobs, etc.
  - Cross Domain: Azure accounts, etc.
- The transformations on the Azure DevOps data you are going to collect.

![azuredevops-set-transformation](assets/images/azuredevops-set-transformation-25ff252773e9b8b0f189be3d2ed6e87a_89d29795ef2df458.png)

<a id="configuration-azuredevops--cicd"></a>

#### CI/CD

To effectively measure [DORA metrics](#dora) through Azure DevOps, it is necessary to define the concept of a 'deployment'. DevLake considers an Azure Pipeline Run (see the blue rectangle) as a DevLake deployment using specific conditions expressed through regular expressions (regex):

- Deployment: The provided regex should match either the name of the Azure pipeline (see the red rectangle) that the pipeline run belongs to or any of the job display names (see the yellow rectangle) associated with the pipeline run. This will designate it as a deployment. For example, if the deployment pipeline is named 'build-and-push-image', you can input (push-image) as the regex. To ensure case insensitivity, include (?i) before the regex.
- Production: The given regex should match either the pipeline run's name or any of its job display names to classify it as a deployment within the production environment. For instance, if the deployment pipeline is named 'build-to-prod', you can input (prod) as the regex. To ensure case insensitivity, include (?i) before the regex.

![azure-pipeline](assets/images/azuredevops-ui-pipeline-072c4460d8f26170bdadc117debe7e2e_1383e0fa01eb3848.png)
![azure-job](assets/images/azuredevops-ui-job-1b8b05dd25e00fabac9f1c1464f216f3_ebd6e93aac1186cf.png)

<a id="configuration-azuredevops--additional-settings"></a>

#### Additional Settings

The additional settings for transformations are RefDiff options:

- Tags Limit: the number of tags to compare.
- Tags Pattern: Only tags that match the given regex are taken into account.

<a id="configuration-azuredevops--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-azuredevops--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecting Azure DevOps data requires creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-azuredevops--step-22-add-a-azure-devops-connection"></a>

### Step 2.2 - Add a Azure DevOps Connection

You can add a previously configured GitLab connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the repositories you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-azuredevops--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or entering a cron code to specify your prefered schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-azuredevops--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.
![collect-data](assets/images/collect-data-5919e2e6ddad525bca4fbcb46e672aff_083db1164108a1f4.png)

<a id="configuration-azuredevops--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-azuredevops--step-1-add-data-connections)
  - [Step 1.1 - Authentication](#configuration-azuredevops--step-11-authentication)
  - [Step 1.2 - Add Data Scopes](#configuration-azuredevops--step-12-add-data-scopes)
  - [Step 1.3 - Add Scope Config (Optional)](#configuration-azuredevops--step-13-add-scope-config-optional)
- [Step 2 - Collect Data in a Project](#configuration-azuredevops--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-azuredevops--step-21-create-a-project)
  - [Step 2.2 - Add a Azure DevOps Connection](#configuration-azuredevops--step-22-add-a-azure-devops-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-azuredevops--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-azuredevops--step-24-start-data-collection)
- [Troubleshooting](#configuration-azuredevops--troubleshooting)

---

<a id="configuration-bitbucket"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/BitBucket/ -->

<!-- page_index: 18 -->

# Bitbucket Cloud

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Bitbucket Cloud

Visit Config UI at `http://localhost:4000` and go to the `Connections` page.

<a id="configuration-bitbucket--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![image](assets/images/220118398-2d08070f-0edb-4de6-8696-9ee58b80719b_9c6080ebd2ed0111.png)

<a id="configuration-bitbucket--step-11-authentication"></a>

### Step 1.1 - Authentication

<a id="configuration-bitbucket--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-bitbucket--endpoint-url"></a>

#### Endpoint URL

For Bitbucket Cloud, you do not need to enter the REST API endpoint URL, which is always `https://api.bitbucket.org/2.0/`.

<a id="configuration-bitbucket--username-and-app-password"></a>

#### Username and App Password

Learn about [how to create a Bitbucket app password](https://support.atlassian.com/bitbucket-cloud/docs/create-an-app-password/).

The following permissions are required to collect data from Bitbucket repositories:

- Account:Read
- Workspace membership:Read
- Projects:Read
- Repositories:Read
- Pull requests:Read
- Issues:Read
- Pipelines:Read
- Runners:Read

![bitbucket-app-password-permissions](assets/images/bitbucket-app-password-permissions-2b87fad376a9ab4a5e4f52b4352d38f1_1a746cf93cf3fc77.jpeg)

<a id="configuration-bitbucket--proxy-url-optional"></a>

#### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-bitbucket--fixed-rate-limit-optional"></a>

#### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit to collect Bitbucket data. You can adjust the rate limit if you want to increase or lower the speed.

The maximum rate limit for different entities in Bitbucket(Cloud) [varies from 1,000 - 60,000 requests/hour](https://support.atlassian.com/bitbucket-cloud/docs/api-request-limits/). The rate limit to access repository data is 1,000 requests/hour, but we find it can still run when we input a value that exceeds 1,000. You can try using a larger rate limit if you have large repositories.

<a id="configuration-bitbucket--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-bitbucket--step-12-add-data-scopes"></a>

### Step 1.2 - Add Data Scopes

Choose the Bitbucket repositories you wish to collect either by finding them in the miller column, or searching. You can only add public repositories through the search box.

![image](assets/images/224308925-449a4d3e-ed52-45e9-bb72-0d2892df374f_7fd23cbeb254b93e.png)

<a id="configuration-bitbucket--step-13-add-scope-config-optional"></a>

### Step 1.3 - Add Scope Config (Optional)

<a id="configuration-bitbucket--entities"></a>

#### Entities

The entities of which domain you wish to collect: Usually, you don't have to modify this part. However, if you don't want to collect certain Bitbucket entities, you can unselect some entities to accelerate the collection speed.

```text
- Issue Tracking: Bitbucket issues, issue comments, etc.
- Source Code Management: Bitbucket repos, refs, commits, etc.
- Code Review: Bitbucket PRs, PR comments, etc.
- CI/CD: Bitbucket Pipelines, Bitbucket Deployments, etc.
- Cross Domain: Bitbucket users, etc.
```

<a id="configuration-bitbucket--transformations"></a>

#### Transformations

The transformations on the Bitbucket data you are going to collect.

- The details of the transformations will be explained below.
- Without adding transformation rules, you can still view the 'Bitbucket' dashboard. However, if you want to view more pre-built dashboards, finish the transformations required.
- Each Bitbucket repo has at most ONE set of transformations.

<a id="configuration-bitbucket--issue-tracking-issue-status-mapping"></a>

###### Issue Tracking > Issue Status Mapping

![image](assets/images/224309704-b096c256-b2cf-4107-b78c-044d06b5f23c_8270288a8bb20e96.png)

The given settings transformed the Bitbucket issue statuses to the issue statuses used by DevLake, enabling you to measure metrics like the Issue Delivery Rate on the pre-built dashboards, as DevLake understands your definition of when an issue is considered as completed (status = 'DONE').

- TODO: The issues that are planned but have not been worked on yet
- IN-PROGRESS: The issues that are work-in-progress
- DONE: The issues that are completed
- OTHER: Other issues statuses that do not belong to the three statuses above

The original status will be saved in the column `original_status` of the table 'issues', and the new status will be saved in the column `status` of the same table.

<a id="configuration-bitbucket--issue-tracking-issue-type-mapping"></a>

###### Issue Tracking > Issue Type Mapping

DevLake will convert the issue types of 'enhancement', 'proposal', and 'task' from Bitbucket into the new issue type 'REQUIREMENT' for DevLake. In contrast, any issues classified as 'bug' in Bitbucket will be converted into the new issue type 'BUG' for DevLake. The original type will be saved in the column `original_type` of the table 'issues', and the new type will be saved in the column `type` of the same table.

<a id="configuration-bitbucket--cicd"></a>

###### CI/CD

The CI/CD configuration for Bitbucket is used for calculating [DORA metrics](#dora).

By default, DevLake will identify the deployment and environment settings that are defined in the Bitbucket CI .yml file.

![image](assets/images/224311429-31304867-8cdd-476b-8675-e4acbc17f552_f063387c7a25826a.png)

However, to ensure this works properly, you must specify the deployment settings in the .yml file.
![img_v2_89602d14-a733-4679-9d4b-d9635c03bc5g](assets/images/221528908-4943b1e6-1398-49e9-8ce9-aa264995f9bc_740c8ebd92797b03.jpg)

The pipeline steps with the `deployment` key will be recognized as DevLake deployments. The value of the `deployment` key will be recognized as the environment of DevLake deployments.

All Bitbucket pipeline steps will be saved in table 'cicd\_tasks', but DevLake deployments will be set as `type` = 'deployment' and `environment` = '{Bitbucket-pipeline-step.deployment.value}'.

If you have not defined these settings in the .yml file, please select 'Detect Deployments from Pipeline steps in Bitbucket', and input the RegEx in the following fields:

![image](assets/images/224310350-cc9a4901-476d-4583-ad73-4d3b394bc343_e6a7d3d030a49de4.png)

- Deployment: A pipeline step with a name that matches the given RegEx will be recognized as a DevLake deployment.
- Production: A pipeline step with a name that matches the given RegEx will be recognized as a DevLake cicd\_task in the production environment.

<a id="configuration-bitbucket--introduction-to-bitbucket-ci-entities"></a>

###### Introduction to Bitbucket CI entities

Bitbucket has several key CI entities: `pipelines`, `pipeline steps`, and `deployments`. A Bitbucket pipeline contains several pipeline steps. Each pipeline step defined with a deployment key can be mapped to a Bitbucket deployment.

Each Bitbucket pipeline is converted to a cicd\_pipeline in DevLake's domain layer schema and each Bitbucket pipeline step is converted to a cicd\_task in DevLake's domain layer.
![image](assets/images/220288225-71bee07d-c319-45bd-98e5-f4d01359840e_35ebe5687cc52642.png)

If a pipeline step defines `deployment` with a value (usually indicating the environment), this pipeline step is also a Bitbucket deployment.

![image](assets/images/221887426-4cae1c46-31ce-4fcd-b773-a54c28af0264_aeeb0d68c7af088f.png)

<a id="configuration-bitbucket--additional-settings-optional"></a>

###### Additional Settings (Optional)

- Tags Limit: DevLake compares the last N pairs of tags to get the "commit diff', "issue diff" between tags. N defaults to 10.

  - commit diff: new commits for a tag relative to the previous one
  - issue diff: issues solved by the new commits for a tag relative to the previous one
- Tags Pattern: Only tags that meet the given Regular Expression will be counted.
- Tags Order: Only "reverse semver" order is supported for now.

Please click `Save` to save the transformation rules for the repo. In the data scope list, click `Next Step` to continue configuring.

<a id="configuration-bitbucket--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-bitbucket--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecting Bitbucket data requires creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-bitbucket--step-22-add-a-bitbucket-connection"></a>

### Step 2.2 - Add a Bitbucket Connection

You can add a previously configured Bitbucket connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the repositories you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-bitbucket--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your preferred schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-bitbucket--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.

<a id="configuration-bitbucket--troubleshooting"></a>

## Troubleshooting

If you run into any problems, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues).

- [Step 1 - Add Data Connections](#configuration-bitbucket--step-1-add-data-connections)
  - [Step 1.1 - Authentication](#configuration-bitbucket--step-11-authentication)
  - [Step 1.2 - Add Data Scopes](#configuration-bitbucket--step-12-add-data-scopes)
  - [Step 1.3 - Add Scope Config (Optional)](#configuration-bitbucket--step-13-add-scope-config-optional)
- [Step 2 - Collect Data in a Project](#configuration-bitbucket--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-bitbucket--step-21-create-a-project)
  - [Step 2.2 - Add a Bitbucket Connection](#configuration-bitbucket--step-22-add-a-bitbucket-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-bitbucket--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-bitbucket--step-24-start-data-collection)
- [Troubleshooting](#configuration-bitbucket--troubleshooting)

---

<a id="configuration-bitbucketserver"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/BitBucketServer/ -->

<!-- page_index: 19 -->

# Bitbucket Server/Data Center

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Bitbucket Server/Data Center

Visit Config UI at `http://localhost:4000` and go to the `Connections` page.

<a id="configuration-bitbucketserver--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![image](assets/images/bitbucket-server-config-ui-026c15a5ab5bcdbe5d073c1599c75c07_573acf9503d7eefc.png)

<a id="configuration-bitbucketserver--step-11-authentication"></a>

### Step 1.1 - Authentication

<a id="configuration-bitbucketserver--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-bitbucketserver--endpoint-url"></a>

#### Endpoint URL

For Bitbucket Server/Data Center, you do need to enter the REST API endpoint URL, which generally is `https://<bitbucket-server>/`.

<a id="configuration-bitbucketserver--username-and-app-password"></a>

#### Username and App Password

The following permissions are required to collect data from Bitbucket repositories:

- Repository read

![bitbucket-server-permissions](assets/images/bitbucket-server-permissions-07c6fa3dd0a98ec55f8a5ca5e95a7704_b30c27efa2c200e5.png)

<a id="configuration-bitbucketserver--proxy-url-optional"></a>

#### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-bitbucketserver--fixed-rate-limit-optional"></a>

#### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit to collect Bitbucket Server/Data Center data. You can adjust the rate limit if you want to increase or lower the speed.

Bitbucket admins could set up the rate limit in the Bitbucket instance referring to [this doc](https://confluence.atlassian.com/bitbucketserver/improving-instance-stability-with-rate-limiting-976171954.html).

<a id="configuration-bitbucketserver--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-bitbucketserver--step-12-add-data-scopes"></a>

### Step 1.2 - Add Data Scopes

Choose the Bitbucket repositories you wish to collect either by finding them in the miller column, or searching. You can only add public repositories through the search box.

![image](assets/images/224308925-449a4d3e-ed52-45e9-bb72-0d2892df374f_7fd23cbeb254b93e.png)

<a id="configuration-bitbucketserver--step-13-add-scope-config-optional"></a>

### Step 1.3 - Add Scope Config (Optional)

<a id="configuration-bitbucketserver--entities"></a>

#### Entities

The entities of which domain you wish to collect: Usually, you don't have to modify this part. However, if you don't want to collect certain Bitbucket Server/Data Center entities, you can unselect some entities to accelerate the collection speed.

```text
- Source Code Management: Bitbucket repos, refs, commits, etc.
- Code Review: Bitbucket PRs, PR comments, etc.
- Cross Domain: Bitbucket users, etc.
```

Please noted that compared to Bitbucket Cloud, Bitbucket Server/Data Center DOES NOT collect issues or CI/CD data.

<a id="configuration-bitbucketserver--transformations"></a>

#### Transformations

The transformations on the Bitbucket Server data you are going to collect.

- The details of the transformations will be explained below.
- Without adding transformation rules, you can still view the 'Bitbucket' dashboard. However, if you want to view more pre-built dashboards, finish the transformations required.
- Each Bitbucket repo has at most ONE set of transformations.

<a id="configuration-bitbucketserver--code-review"></a>

###### Code Review

- Type: The `type` of pull requests will be parsed from PR labels by given regular expression. For example:

  - when your labels for PR types are like 'type/feature-development', 'type/bug-fixing' and 'type/docs', please input 'type/(.\*)$'
  - when your labels for PR types are like 'feature-development', 'bug-fixing' and 'docs', please input '(feature-development|bug-fixing|docs)$'
- Component: The `component` of pull requests will be parsed from PR labels by given regular expression.

<a id="configuration-bitbucketserver--additional-settings-optional"></a>

###### Additional Settings (Optional)

- Tags Limit: DevLake compares the last N pairs of tags to get the "commit diff', "issue diff" between tags. N defaults to 10.

  - commit diff: new commits for a tag relative to the previous one
  - issue diff: issues solved by the new commits for a tag relative to the previous one
- Tags Pattern: Only tags that meet the given Regular Expression will be counted.
- Tags Order: Only "reverse semver" order is supported for now.

Please click `Save` to save the transformation rules for the repo. In the data scope list, click `Next Step` to continue configuring.

<a id="configuration-bitbucketserver--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-bitbucketserver--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecting Bitbucket data requires creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-bitbucketserver--step-22-add-a-bitbucket-server-connection"></a>

### Step 2.2 - Add a Bitbucket Server Connection

You can add a previously configured Bitbucket Server connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the repositories you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-bitbucketserver--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your preferred schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-bitbucketserver--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.

<a id="configuration-bitbucketserver--troubleshooting"></a>

## Troubleshooting

If you run into any problems, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues).

- [Step 1 - Add Data Connections](#configuration-bitbucketserver--step-1-add-data-connections)
  - [Step 1.1 - Authentication](#configuration-bitbucketserver--step-11-authentication)
  - [Step 1.2 - Add Data Scopes](#configuration-bitbucketserver--step-12-add-data-scopes)
  - [Step 1.3 - Add Scope Config (Optional)](#configuration-bitbucketserver--step-13-add-scope-config-optional)
- [Step 2 - Collect Data in a Project](#configuration-bitbucketserver--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-bitbucketserver--step-21-create-a-project)
  - [Step 2.2 - Add a Bitbucket Server Connection](#configuration-bitbucketserver--step-22-add-a-bitbucket-server-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-bitbucketserver--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-bitbucketserver--step-24-start-data-collection)
- [Troubleshooting](#configuration-bitbucketserver--troubleshooting)

---

<a id="configuration-circleci"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/CircleCI/ -->

<!-- page_index: 20 -->

# CircleCI

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# CircleCI

Visit Config UI at : `http://localhost:4000` and go to `Connections` page.

<a id="configuration-circleci--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

<a id="configuration-circleci--step-11-authentication"></a>

### Step 1.1 - Authentication

![image](assets/images/circleci-add-data-connections-bd6cb2687069ef9942cf09723a413534_7bc9e514debd1bec.png)

<a id="configuration-circleci--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-circleci--endpoint-url"></a>

#### Endpoint URL

For CircleCI, you do not need to enter the REST API endpoint URL, which is always `https://circleci.com/api/`.

<a id="configuration-circleci--token"></a>

#### Token

Learn about [Managing API Tokens](https://circleci.com/docs/managing-api-tokens/).

Tokens you have generated that can be used to access the CircleCI API. Apps using these tokens can act as you and have full read- and write-permissions!
There are two types of API token(Personal and Project) you can create within CircleCI.

<a id="configuration-circleci--proxy-url-optional"></a>

#### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-circleci--fixed-rate-limit-optional"></a>

#### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit to collect CircleCI data. You can adjust the rate limit if you want to increase or lower the speed.
Learn more about [CircleCI API rate limit](https://circleci.com/docs/api-developers-guide/#rate-limits).

<a id="configuration-circleci--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-circleci--step-12-configure-data-scope"></a>

### Step 1.2 - Configure Data Scope

![image](assets/images/circleci-choose-data-scope-1fd82c60a84e042c5e9781717fb72bc2_acc6e8cb08018ca8.png)

<a id="configuration-circleci--projects"></a>

#### Projects

Select the CircleCI projects to collect.

<a id="configuration-circleci--step-13-adding-scope-config-optional"></a>

### Step 1.3 - Adding Scope Config (Optional)

Scope config includes two sets of configurations:

- Data Entities
- Transformations

<a id="configuration-circleci--data-entities"></a>

##### Data Entities

![image](assets/images/circleci-scope-config-1-c2f1900e354459833f0d10d32b561a07_938ba5690219bff9.png)

CircleCI only supports `CI/CD` domain entities, which include CircleCI `projects`, `workflows`, `jobs`, and etc.

<a id="configuration-circleci--transformations"></a>

##### Transformations

![image](assets/images/circleci-scope-config-2-265d394287123cb84ad26d36064e4c18_3e4b267b5f4a8528.png)

This set of configurations is used for calculating [DORA metrics](#dora).

You can transform a CircleCI workflow run into a DevLake deployment with the following regex:

- Deployment: The given regex should match the name of the Circle workflow run or one of its jobs to be considered as a deployment. For example, if the workflow run used for deployment is named 'build-and-push-image', you can input `(push-image)`. To make the regex case insensitive, you can include `(?i)` before the regex.
- Environment: The given regex should match the workflow run's name to be considered a deployment within the production environment. For instance, if the workflow run used for deployment is named 'deploy-to-prod', you can input `(prod)`. To make the regex case insensitive, you can include (?i) before the regex.

<a id="configuration-circleci--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-circleci--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecting CircleCI data requires creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-circleci--step-22-add-a-circleci-connection"></a>

### Step 2.2 - Add a CircleCI Connection

You can add a previously configured CircleCI connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the repositories you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-circleci--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your preferred schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-circleci--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.
![collect-data](assets/images/collect-data-5919e2e6ddad525bca4fbcb46e672aff_083db1164108a1f4.png)

<a id="configuration-circleci--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-circleci--step-1-add-data-connections)
  - [Step 1.1 - Authentication](#configuration-circleci--step-11-authentication)
  - [Step 1.2 - Configure Data Scope](#configuration-circleci--step-12-configure-data-scope)
  - [Step 1.3 - Adding Scope Config (Optional)](#configuration-circleci--step-13-adding-scope-config-optional)
- [Step 2 - Collect Data in a Project](#configuration-circleci--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-circleci--step-21-create-a-project)
  - [Step 2.2 - Add a CircleCI Connection](#configuration-circleci--step-22-add-a-circleci-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-circleci--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-circleci--step-24-start-data-collection)
- [Troubleshooting](#configuration-circleci--troubleshooting)

---

<a id="configuration-github"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/GitHub/ -->

<!-- page_index: 21 -->

# GitHub

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# GitHub

Visit Config UI at: `http://localhost:4000`.

<a id="configuration-github--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

On the Connections page, you can select GitHub and create a new connection or it.

<a id="configuration-github--step-11-authentication"></a>

### Step 1.1 - Authentication

![github-add-data-connections](assets/images/github-create-a-connection-29962b92b1f53daa4bc9eb388743f63c_c08136228bac8f14.png)

<a id="configuration-github--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-github--endpoint-url"></a>

#### Endpoint URL

This should be a valid REST API endpoint, e.g. `https://api.github.com/`. The URL should end with `/`.

<a id="configuration-github--personal-access-tokens"></a>

#### Personal Access Token(s)

You can use one of the following GitHub tokens: personal access tokens(PATs) or fine-grained personal access tokens.

<a id="configuration-github--github-personal-access-tokensrecommended"></a>

##### GitHub Personal Access Tokens(Recommended)

> Prerequisites: please make sure your organization has enabled Personal Access Token before configuration. See the [detailed doc](https://docs.github.com/en/organizations/managing-programmatic-access-to-your-organization/setting-a-personal-access-token-policy-for-your-organization).

Learn about [how to create a GitHub personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token). The following permissions are required to collect data from repositories:

- `repo:status`
- `repo_deployment`
- `read:user`
- `read:org`

However, if you want to collect data from private repositories, the following permissions are required:

- `repo`
- `read:user`
- `read:org`

The difference is that you have to give full permission for `repos`, not just `repo:status` and `repo_deployment`. Starting from v0.18.0, DevLake provides the auto-check for the permissions of your token(s).

The data collection speed is restricted by the **rate limit of [5,000 requests](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting) per hour per token** (15,000 requests/hour if you pay for GitHub enterprise). You can accelerate data collection by configuring *multiple* personal access tokens. Please note that multiple tokens should be created by different GitHub accounts. Tokens belonging to the same GitHub account share the rate limit.

<a id="configuration-github--fine-grained-personal-access-tokens"></a>

##### Fine-grained Personal Access Tokens

Note: this token doesn't support GraphQL APIs. You have to disable `Use GraphQL APIs` on the connection page if you want to use it. However, this will significantly increase the data collection time.

If you're concerned with giving classic PATs full unrestricted access to your repositories, you can use fine-grained PATs announced by GitHub recently. With fine-grained PATs, GitHub users can create read-only PATs that only have access to repositories under certain GitHub orgs. But in order to do that, org admin needs to enroll that org with fine-grained PATs beta feature first. Please check [this doc](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token#creating-a-fine-grained-personal-access-token) for more details.
The token should be granted read-only permission for the following entities.

- `Actions`
- `Contents`
- `Discussions`
- `Issues`
- `Metadata`
- `Pull requests`

<a id="configuration-github--github-apps"></a>

##### GitHub Apps

Learn about [how to create a GitHub Apps](https://docs.github.com/en/apps/maintaining-github-apps/modifying-a-github-app-registration#navigating-to-your-github-app-settings). The following permissions are required to collect data from repositories:

- Repository
  - Actions
  - Administration
  - Checks
  - Commit statuses
  - Contents
  - Deployments
  - Issues
  - Metadata
  - Pull requests
- Organization
  - Members

<a id="configuration-github--use-graphql-apis"></a>

#### Use Graphql APIs

If you are using `github.com` or your on-premise GitHub version supports GraphQL APIs, toggle on this setting to collect data quicker.

- GraphQL APIs are 10+ times faster than REST APIs, but they may not be supported in GitHub on-premise versions.
- Instead of using multiple tokens to collect data, you can use ONLY ONE token because GraphQL APIs are quick enough.

<a id="configuration-github--proxy-url-optional"></a>

#### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-github--fixed-rate-limit-optional"></a>

#### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit to collect GitHub data. You can adjust the rate limit if you want to increase or lower the speed.

The maximum rate limit for GitHub is  **[5,000 requests/hour](https://docs.github.com/en/rest/overview/resources-in-the-rest-api#rate-limiting)** (15,000 requests/hour if you pay for GitHub enterprise). Please do not use a rate that exceeds this number.

<a id="configuration-github--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-github--step-12-add-data-scopes"></a>

### Step 1.2 - Add Data Scopes

<a id="configuration-github--repositories"></a>

#### Repositories

Choose the GitHub repositories you wish to collect either by finding them in the miller column, or searching. You can only add public repositories through the search box.

![github-set-data-scope](assets/images/github-add-data-scopes-de766e05a42c88954b66757efae19acc_eb0e03ab628160c7.png)

<a id="configuration-github--step-13-add-scope-config-optional"></a>

### Step 1.3 - Add Scope Config (Optional)

Scope config contains two parts:

- The entities of which domain you wish to collect: Usually, you don't have to modify this part. However, if you don't want to collect certain GitHub entities, you can unselect some entities to accelerate the collection speed.
  - Issue Tracking: GitHub issues, issue comments, issue labels, etc.
  - Source Code Management: GitHub repos, refs, commits, etc.
  - Code Review: GitHub PRs, PR comments and reviews, etc.
  - CI/CD: GitHub Workflow runs, GitHub Workflow jobs, etc.
  - Cross Domain: GitHub accounts, etc.
- The transformations on the GitHub data you are going to collect.
  - The details of the transformations will be explained below.
  - Without adding transformation rules, you can still view the "[GitHub Metrics](https://devlake.apache.org/livedemo/DataSources/GitHub)" dashboard. However, if you want to view "[Weekly Bug Retro](https://devlake.apache.org/livedemo/EngineeringLeads/WeeklyBugRetro)", "[Weekly Community Retro](https://devlake.apache.org/livedemo/OSSMaintainers/WeeklyCommunityRetro)" or other pre-built dashboards, the following transformation rules, especially "Type/Bug", should be added.
  - Each GitHub repo has at most ONE set of transformations.

![github-add-transformation-rules-list](assets/images/github-scope-config-3fc69efcca404c7e07a30c456d3b7cf8_3df9d5f982bd4e88.png)
![github-add-transformation-rules](assets/images/github-set-transformation2-8a84153828bfed36f4089019c8059db9_f94b15e4e05f4485.png)

<a id="configuration-github--issue-tracking"></a>

#### Issue Tracking

- Severity: Parse the value of `severity` from issue labels.

  - when your issue labels for severity level are like 'severity/p0', 'severity/p1', 'severity/p2', then input 'severity/(.\*)$'
  - when your issue labels for severity level are like 'p0', 'p1', 'p2', then input '(p0|p1|p2)$'
- Component: Same as "Severity".
- Priority: Same as "Severity".
- Type/Requirement: The `type` of issues with labels that match given regular expression will be set to "REQUIREMENT". Unlike "PR.type", submatch does nothing, because for issue management analysis, users tend to focus on 3 kinds of types (Requirement/Bug/Incident), however, the concrete naming varies from repo to repo, time to time, so we decided to standardize them to help analysts metrics.
- Type/Bug: Same as "Type/Requirement", with `type` setting to "BUG".
- Type/Incident: Same as "Type/Requirement", with `type` setting to "INCIDENT".

<a id="configuration-github--cicd"></a>

#### CI/CD

This set of configurations is used to define 'deployments'. Deployments are related to measure [DORA metrics](#dora).

For GitHub deployments, DevLake recognizes them as deployments by specifying a regular expression (regex) to identify the production environments among all 'GitHub environments'.

If your deployments are not performed through GitHub deployments but rather specific workflow runs in GitHub, you have the option to convert a workflow run into a DevLake deployment. In this case, you need to configure two regular expressions (regex):

- Deployment: The given regex should match the name of the GitHub workflow run or one of its jobs to be considered as a deployment. For example, if the workflow run used for deployment is named 'build-and-push-image', you can input (push-image). To make the regex case insensitive, you can include (?i) before the regex.
- Production: The given regex should match either the workflow run's name or its branch's name to be considered a deployment within the production environment. For instance:
  - If the workflow run used for deployment is named 'build-to-prod', you can input (prod). To make the regex case insensitive, you can include (?i) before the regex.
  - Also, many users in GitHub utilize the same workflow for both staging and prod deployments, executing it on the release branch would indicate a production deployment.

![github-action-run](assets/images/github-action-run-321793e23959ffae0597e53aab1bd8f5_f80dfd8cded15907.png)
![github-action-job](assets/images/github-action-job-9c30243e63c1731fcac7f35f1e6e9aa5_c0e4e80f16269a89.png)

<a id="configuration-github--code-review"></a>

#### Code Review

- Type: The `type` of pull requests will be parsed from PR labels by given regular expression. For example:

  - when your labels for PR types are like 'type/feature-development', 'type/bug-fixing' and 'type/docs', please input 'type/(.\*)$'
  - when your labels for PR types are like 'feature-development', 'bug-fixing' and 'docs', please input '(feature-development|bug-fixing|docs)$'
- Component: The `component` of pull requests will be parsed from PR labels by given regular expression.

<a id="configuration-github--additional-settings-optional"></a>

#### Additional Settings (Optional)

- Tags Limit: It'll compare the last N pairs of tags to get the "commit diff", "issue diff" between tags. N defaults to 10.

  - commit diff: new commits for a tag relative to the previous one
  - issue diff: issues solved by the new commits for a tag relative to the previous one
- Tags Pattern: Only tags that meet given regular expression will be counted.
- Tags Order: Only "reverse semver" order is supported for now.

Please click `Save` to save the transformation rules for the repo. In the data scope list, click `Next Step` to continue configuring.

<a id="configuration-github--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-github--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecting GitHub data requires creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-github--step-22-add-a-github-connection"></a>

### Step 2.2 - Add a GitHub Connection

You can add a previously configured GitHub connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the repositories you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-github--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your preferred schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-github--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.
![collect-data](assets/images/collect-data-5919e2e6ddad525bca4fbcb46e672aff_083db1164108a1f4.png)

<a id="configuration-github--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-github--step-1-add-data-connections)
  - [Step 1.1 - Authentication](#configuration-github--step-11-authentication)
  - [Step 1.2 - Add Data Scopes](#configuration-github--step-12-add-data-scopes)
  - [Step 1.3 - Add Scope Config (Optional)](#configuration-github--step-13-add-scope-config-optional)
- [Step 2 - Collect Data in a Project](#configuration-github--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-github--step-21-create-a-project)
  - [Step 2.2 - Add a GitHub Connection](#configuration-github--step-22-add-a-github-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-github--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-github--step-24-start-data-collection)
- [Troubleshooting](#configuration-github--troubleshooting)

---

<a id="configuration-gitlab"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/GitLab/ -->

<!-- page_index: 22 -->

# GitLab

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# GitLab

Visit Config UI: `http://localhost:4000`.

<a id="configuration-gitlab--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

On the Connections page, you can select GitHub and create a new connection or it.

<a id="configuration-gitlab--step-11-authentication"></a>

### Step 1.1 - Authentication

![gitlab-add-data-connections](assets/images/gitlab-create-a-connection-2bca753578a1ea2f32ebea8f2b392161_1ce6170339f1cdbf.png)

<a id="configuration-gitlab--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-gitlab--gitlab-version"></a>

#### GitLab Version

Select if you use GitLab Cloud or GitLab Server (v11+).

<a id="configuration-gitlab--endpoint-url"></a>

#### Endpoint URL

This should be a valid REST API endpoint.

- If you use GitLab cloud, you do not need to enter the endpoint, which is always `https://gitlab.com/api/v4/`.
- If you GitLab Server (v11+), the endpoint will look like `https://gitlab.example.com/api/v4/`.
  Please note: the endpoint URL should end with `/`.

<a id="configuration-gitlab--personal-access-token"></a>

#### Personal Access Token

Your GitLab personal access token (PAT) is required to add a connection. Learn about [how to create a GitLab personal access token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html).

<a id="configuration-gitlab--personal-access-token-permissions"></a>

##### Personal Access Token Permissions

At least one of the following permissions is required to collect data from repositories:

- `api`
- `read_api`

You also have to double-check your GitLab user permission settings.

1. Go to the Project information -> Members page of the GitLab projects you wish to collect.
2. Check your role in this project from the Max role column. Make sure you are not the Guest role, otherwise, you will not be able to collect data from this project.

<a id="configuration-gitlab--proxy-url-optional"></a>

#### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-gitlab--fixed-rate-limit-optional"></a>

#### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit at around 12,000 requests/hour to collect GitLab data. You can adjust the rate limit if you want to increase or lower the speed.

The maximum rate limit for GitLab Cloud is  **[120,000 requests/hour](https://docs.gitlab.com/ee/user/gitlab_com/index.html#gitlabcom-specific-rate-limits)**. Tokens under the same IP address share the rate limit, so the actual rate limit for your token will be lower than this number.

For self-managed GitLab rate limiting, please contact your GitLab admin to [get or set the maximum rate limit](https://repository.prace-ri.eu/git/help/security/rate_limits.md) of your GitLab instance. Please do not use a rate that exceeds this number.

<a id="configuration-gitlab--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-gitlab--step-12-add-data-scopes"></a>

### Step 1.2 - Add Data Scopes

<a id="configuration-gitlab--repositories"></a>

#### Repositories

![gitlab-set-data-scope](assets/images/gitlab-set-data-scope-71302fedcb351724279d43c0041e94a6_3f68b747fe5c3c25.png)

Select the GitLab repositories you want to collect from the miller column. **Please note that repositories with guest permissions or those that are archived have already been excluded.** You can also use the search function to find them. Limited by the GitLab API, You need to type more than 2 characters to search. The repositories only with guest permissions are not shown in the list.

<a id="configuration-gitlab--step-13-add-scope-config-optional"></a>

### Step 1.3 - Add Scope Config (Optional)

Scope config contains two parts:

- The entities of which domain you wish to collect: Usually, you don't have to modify this part. However, if you don't want to collect certain GitLab entities, you can unselect some entities to accelerate the collection speed.
  - Issue Tracking: GitLab issues, issue comments, issue labels, etc.
  - Source Code Management: GitLab repos, refs, commits, etc.
  - Code Review: GitLab MRs, MR comments and reviews, etc.
  - CI/CD: GitLab pipelines, jobs, etc.
  - Cross Domain: GitLab accounts, etc.
- The transformations on the GitLab data you are going to collect.
  - The details of the transformations will be explained below.
  - Without adding transformation rules, you can still view some of the dashboards.
  - Each GitLab repo has at most ONE set of transformations.

![gitlab-set-transformation1](assets/images/gitlab-scope-config-a5ad3581c89ab4d47b6b6ce5a80a244e_a791ebd31a945e0c.png)
![gitlab-set-transformation2](assets/images/gitlab-set-transformation2-b0e013f8fb05d5f5725bf3d1be8cc10c_5e13188aba1b73ac.png)

<a id="configuration-gitlab--cicd"></a>

#### CI/CD

This set of configurations is used to define 'deployments'. Deployments are related to measure [DORA metrics](#dora).

For GitLab deployments, DevLake recognizes them as deployments by specifying a regular expression (regex) to identify the production environments among all 'GitLab environments'.

If your deployments are not performed through GitLab deployments but rather specific pipelines in GitLab, you have the option to convert a GitLab pipeline run into a DevLake deployment. In this case, you need to configure two regular expressions (regex):

- Deployment: The given regex should match the name of the GitLab pipeline's branch name or one of its job names to be considered as a deployment. For example, if the pipeline is executet on the 'build-and-push-image', you can input (push-image). To make the regex case insensitive, you can include (?i) before the regex.
- Production: The given regex should match either the pipeline's branch name or one of its job names to be considered a deployment within the production environment. For instance:
  - If the pipeline used for deployment is named 'build-to-prod', you can input (prod). To make the regex case insensitive, you can include (?i) before the regex.
  - Also, many users in GitLab utilize the same pipeline for both staging and prod deployments, executing it on the release branch would indicate a production deployment.

<a id="configuration-gitlab--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-gitlab--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecting GitLab data requires creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-gitlab--step-22-add-a-gitlab-connection"></a>

### Step 2.2 - Add a GitLab Connection

You can add a previously configured GitLab connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the repositories you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-gitlab--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or entering a cron code to specify your prefered schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-gitlab--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.
![collect-data](assets/images/collect-data-5919e2e6ddad525bca4fbcb46e672aff_083db1164108a1f4.png)

<a id="configuration-gitlab--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-gitlab--step-1-add-data-connections)
  - [Step 1.1 - Authentication](#configuration-gitlab--step-11-authentication)
  - [Step 1.2 - Add Data Scopes](#configuration-gitlab--step-12-add-data-scopes)
  - [Step 1.3 - Add Scope Config (Optional)](#configuration-gitlab--step-13-add-scope-config-optional)
- [Step 2 - Collect Data in a Project](#configuration-gitlab--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-gitlab--step-21-create-a-project)
  - [Step 2.2 - Add a GitLab Connection](#configuration-gitlab--step-22-add-a-gitlab-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-gitlab--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-gitlab--step-24-start-data-collection)
- [Troubleshooting](#configuration-gitlab--troubleshooting)

---

<a id="configuration-opsgenie"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Opsgenie/ -->

<!-- page_index: 23 -->

# Opsgenie

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Opsgenie

Visit Config UI at: `http://localhost:4000`.

<a id="configuration-opsgenie--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

On the Connections page, you can select Opsgenie and create a new connection on it.

<a id="configuration-opsgenie--step-11-authentication"></a>

### Step 1.1 - Authentication

![opsgenie-add-data-connections](assets/images/opsgenie-create-a-connection-d5d467f71e6321c9d5543bd8f2209294_b49681ed16d68dcc.png)

<a id="configuration-opsgenie--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-opsgenie--endpoint-url"></a>

#### Endpoint URL

Opsgenie makes available two types of REST API endpoints, US and EU, eg. `https://api.opsgenie.com/` or `https://api.eu.opsgenie.com/`. You can choose wich instance by selecting the due radio input.

<a id="configuration-opsgenie--api-access-key"></a>

#### API Access Key

In the `API key management` section of your Atlassian Opsgenie account settings, you can create a API key to manage your requests.

Learn about [how to create a Opsgenie API key](https://support.atlassian.com/opsgenie/docs/api-key-management/). The following permissions are required to collect data from repositories:

- `Read`
- `Create and Update`
- `Configuration Access`

<a id="configuration-opsgenie--proxy-url-optional"></a>

#### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-opsgenie--fixed-rate-limit-optional"></a>

#### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit to collect Opsgenie data. You can adjust the rate limit if you want to increase or lower the speed.

Opsgenie doesn't establishes a maximum rate limit for its API request, thus you should check this **[detailed doc](https://docs.opsgenie.com/docs/api-rate-limiting)** on how to calculate your rate limit, based on number of user and account plan that you hired. For now, the default rate limit is in 6,000 request/hour (100 request/minute).

<a id="configuration-opsgenie--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-opsgenie--step-12-add-data-scopes"></a>

### Step 1.2 - Add Data Scopes

<a id="configuration-opsgenie--services"></a>

#### Services

Choose the Opsgenie services you wish to collect either by finding them in the miller column, or searching.

![opsgenie-set-data-scope](assets/images/opsgenie-add-data-scopes-3190f3235564d4cc411492bc97a83009_343034a4716914f4.png)

<a id="configuration-opsgenie--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-opsgenie--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecing Opsgenie data requires creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-opsgenie--step-22-add-a-opsgenie-connection"></a>

### Step 2.2 - Add a Opsgenie Connection

You can add a previously configured Opsgenie connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the services you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-opsgenie--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your prefered schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-opsgenie--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.
![collect-data](assets/images/collect-data-5919e2e6ddad525bca4fbcb46e672aff_083db1164108a1f4.png)

<a id="configuration-opsgenie--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-opsgenie--step-1-add-data-connections)
  - [Step 1.1 - Authentication](#configuration-opsgenie--step-11-authentication)
  - [Step 1.2 - Add Data Scopes](#configuration-opsgenie--step-12-add-data-scopes)
- [Step 2 - Collect Data in a Project](#configuration-opsgenie--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-opsgenie--step-21-create-a-project)
  - [Step 2.2 - Add a Opsgenie Connection](#configuration-opsgenie--step-22-add-a-opsgenie-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-opsgenie--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-opsgenie--step-24-start-data-collection)
- [Troubleshooting](#configuration-opsgenie--troubleshooting)

---

<a id="configuration-jenkins"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Jenkins/ -->

<!-- page_index: 24 -->

# Jenkins

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Jenkins

Visit Config UI at: `http://localhost:4000`.

<a id="configuration-jenkins--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![jenkins-create-a-connection](assets/images/jenkins-create-a-connection-20c7484322eb364ef2d95c7630d349d9_130faad93f84e59d.png)

<a id="configuration-jenkins--connection-name"></a>

### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-jenkins--endpoint-url"></a>

### Endpoint URL

This should be a valid REST API endpoint. Eg. `https://ci.jenkins.io/`. The endpoint url should end with `/`.

<a id="configuration-jenkins--username-e-mail"></a>

### Username (E-mail)

Your User ID for the Jenkins Instance.

<a id="configuration-jenkins--password"></a>

### Password

For help on Username and Password, please see Jenkins docs on [using credentials](https://www.jenkins.io/doc/book/using/using-credentials/). You can also use "API Access Token" for this field, which can be generated at `User` -> `Configure` -> `API Token` section on Jenkins.

<a id="configuration-jenkins--fixed-rate-limit-optional"></a>

### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit to collect Jenkins data. You can adjust the rate limit if you want to increase or lower the speed.

There is no doc about Jenkins rate limiting. Please create an issue if you find related information.

<a id="configuration-jenkins--test-and-save-connection"></a>

### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-jenkins--step-2-setting-data-scope"></a>

## Step 2 - Setting Data Scope

![jenkins-set-data-scope](assets/images/jenkins-set-data-scope-b4da7996db498317c309fc5eacc9527e_1cb9f10c380e74d5.png)

<a id="configuration-jenkins--jobs"></a>

### Jobs

Choose the Jenkins jobs. All `Jenkins builds` under these jobs will be collected.

<a id="configuration-jenkins--data-entities"></a>

### Data Entities

Jenkins only supports `CI/CD` domain entities, transformed from Jenkins builds and stages.

- CI/CD: Jenkins builds, stages, etc.

<a id="configuration-jenkins--step-3-adding-transformation-rules-optional"></a>

## Step 3 - Adding Transformation Rules (Optional)

![jenkins-set-transformation1](assets/images/jenkins-set-transformation1-bb4979188f3d7fa38819ef40401f073e_2b6e927b95ae788b.png)
![jenkins-set-transformation2](assets/images/jenkins-set-transformation2-1360ed3fad4994cc208d5b79dea778e7_98ce4ac6da2c2170.png)

This set of configurations is used for calculating [DORA metrics](#dora).

If you'd like to define `deployments` with Jenkins, please select "Detect Deployment from Jenkins Builds", and provide the following regexes

- Deployment: Jenkins stages whose names match the regex will be registered as deployments (if a Jenkins build has no stage, its job name will be used to match the regex)
- Production: Jenkins stages whose names match the regex will be assigned environment 'PRODUCTION' (if a Jenkins build has no stage, its job name will be used to match the regex)

This is how it works behind the scene:

- If a Jenkins build has stages, it's converted to a cicd\_pipeline and its stages are converted to cicd\_tasks in DevLake's domain layer schema.
- If a Jenkins build has no stage, it's converted to both a cicd\_pipeline and a cicd\_task whose names are the build's jobName.

After the conversion, the two regexes are applied to the records in the cicd\_tasks table.
![jenkins-job-build-stage](assets/images/jenkins-job-build-stage-1aa7f958b4fe1a1c4e27dd8ec04b4327_fb0ada655e42bfbe.png)

You can also select "Not using Jenkins builds as Deployments" if you're not using Jenkins to conduct deployments.

<a id="configuration-jenkins--step-4-setting-sync-policy"></a>

## Step 4 - Setting Sync Policy

You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your prefered schedule.

<a id="configuration-jenkins--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-jenkins--step-1-add-data-connections)
  - [Connection Name](#configuration-jenkins--connection-name)
  - [Endpoint URL](#configuration-jenkins--endpoint-url)
  - [Username (E-mail)](#configuration-jenkins--username-e-mail)
  - [Password](#configuration-jenkins--password)
  - [Fixed Rate Limit (Optional)](#configuration-jenkins--fixed-rate-limit-optional)
  - [Test and Save Connection](#configuration-jenkins--test-and-save-connection)
- [Step 2 - Setting Data Scope](#configuration-jenkins--step-2-setting-data-scope)
  - [Jobs](#configuration-jenkins--jobs)
  - [Data Entities](#configuration-jenkins--data-entities)
- [Step 3 - Adding Transformation Rules (Optional)](#configuration-jenkins--step-3-adding-transformation-rules-optional)
- [Step 4 - Setting Sync Policy](#configuration-jenkins--step-4-setting-sync-policy)
- [Troubleshooting](#configuration-jenkins--troubleshooting)

---

<a id="configuration-jira"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Jira/ -->

<!-- page_index: 25 -->

# Jira

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Jira

Visit Config UI at: `http://localhost:4000`.

<a id="configuration-jira--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

On the Connections page, you can select Jira and create a new connection or it.

<a id="configuration-jira--stept-11-authentication"></a>

### Stept 1.1 - Authentication

![jira-add-data-connections](assets/images/jira-create-a-connection-3f933bb21ec56a7d065f9d855d7aa43b_9993edb7790e3775.png)

<a id="configuration-jira--connection-name"></a>

#### Connection Name

Give your connection a unique name to help you identify it in the future.

Please note: the following configuration for the endpoint and authentication for your Jira connection depends on your Jira version, Jira Cloud or Server/Data Center.

<a id="configuration-jira--jira-cloud"></a>

#### Jira Cloud

<a id="configuration-jira--endpoint-url"></a>

##### Endpoint URL

This should be a valid REST API endpoint: `https://<mydomain>.atlassian.net/rest/`

Please note: the endpoint url should end with `/`.

<a id="configuration-jira--e-mail"></a>

##### E-mail

Please enter the e-mail of your Jira account.

<a id="configuration-jira--api-token"></a>

##### API Token

Learn about [how to create an API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/).

Please note: Jira API token and Personal Access Token are two different tokens.

<a id="configuration-jira--jira-serverdata-center"></a>

#### Jira Server/Data Center

<a id="configuration-jira--endpoint-url-1"></a>

##### Endpoint URL

This should be a valid REST API endpoint: `https://jira.<mydomain>.com/rest/`

Please note: the endpoint url should end with `/`.

<a id="configuration-jira--authentication-method"></a>

##### Authentication Method

Jira Server supports two ways of authentication: using basic authentication or Personal Access Token.

<a id="configuration-jira--username"></a>

##### Username

Please enter the username of your Jira account.

<a id="configuration-jira--password"></a>

##### Password

Please enter the password of your Jira account.

<a id="configuration-jira--personal-access-token"></a>

##### Personal Access Token

Learn about [how to create a Personal Access Token](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html).

<a id="configuration-jira--token-permissions"></a>

#### Token Permissions

For both Jira Cloud and Jira Server, when accessing Jira API, users may encounter access restrictions if their token does not have sufficient permissions. This is typically caused by insufficient scope or role settings for the Jira token.

To solve this issue, users can take the following steps:

- Checking User Permissions

Users can confirm whether they have sufficient permissions by checking their permissions in Jira. For Cloud users, they can view their global and project permissions through the "Permissions" tab on the "Profile" page. For Server users, they can log in to Jira as an administrator and view user permissions on the "User Management" page.

- Ensuring Sufficient Permissions

Before using the Jira API, users need to ensure that their account has at least the necessary project or global permissions. Global permissions include various Jira system settings and management operations, while project permissions control specific operations and configurations for each Jira project. Users can assign roles such as `Project Administrator`, `Project Lead`, `Developer`, etc. for the corresponding projects, or assign global permissions such as `Jira Administrators`, `Jira Software Administrators`, etc. It is recommended to minimize the permissions granted to the API to ensure system security.

- Solving Access Restrictions

To solve access restrictions caused by insufficient Jira token permissions, users should check the token's permission settings to ensure the correct scope and role are set. If the permission settings are correct but the required API is still inaccessible, consider using other authentication methods, such as authenticating with a username and password. If the issue persists, contact the Jira administrator for further assistance.

<a id="configuration-jira--proxy-url-optional"></a>

#### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-jira--fixed-rate-limit-optional"></a>

##### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit to collect Jira data. You can adjust the rate limit if you want to increase or lower the speed. If you encounter a 403 error during data collection, please lower the rate limit.

Jira(Cloud) uses a dynamic rate limit and has no clear rate limit. For Jira Server's rate limiting, please contact your Jira Server admin to [get or set the maximum rate limit](https://repository.prace-ri.eu/git/help/security/rate_limits.md) of your Jira instance. Please do not use a rate that exceeds this number.

<a id="configuration-jira--test-and-save-connection"></a>

#### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-jira--step-12-add-data-scopes"></a>

### Step 1.2 - Add Data Scopes

<a id="configuration-jira--boards"></a>

#### Boards

Choose the Jira boards to collect.

![jira-set-data-scope](assets/images/jira-add-data-scopes-25706691feac40ea43438d4d7deda4da_8f92655e0282358c.png)

<a id="configuration-jira--step-13-add-scope-config-optional"></a>

### Step 1.3 - Add Scope Config (Optional)

Scope config contains two parts:

- The entities of which domain you wish to collect: Usually, you don't have to modify this part. However, if you don't want to collect certain Jira entities, you can unselect some entities to accelerate the collection speed.
  - Issue Tracking: Jira issues, issue comments, issue labels, etc.
  - Cross Domain: Jira accounts, etc.
- The transformations on the Jira data you are going to collect
  - Issue Type: Standardize the issue types to DevLake's pre-defined three issue types: REQUIREMENT, BUG, and INCIDENT.
  - Story Points: Map the custom field that represents story\_point in your Jira to DevLake's issue story point.
  - Cross-domain: Get the commit(s) associated with Jira issues from Jira issues' remote links or development panels.

Although this configuration is optional, some of the above transformations are required to measure metrics such as [Requirement Lead Time](https://devlake.apache.org/docs/Metrics/RequirementLeadTime), [Bug Age](https://devlake.apache.org/docs/Metrics/BugAge) or [DORA - Median Time to Restore Service](https://devlake.apache.org/docs/Metrics/MTTR) in the built-in Grafana dashboards.

Without adding transformation rules, you can not view all charts in "Jira" or "Engineering Throughput and Cycle Time" dashboards.

Each Jira board has at most ONE set of transformations.

![jira-add-transformation-1](assets/images/jira-set-transformation1-c7ff3516ebdca4b869d620902f24943d_3dc1ddea65bdf8d5.png)
![jira-add-transformation-2](assets/images/jira-set-transformation2-61ac18bf07c7b6a1fafa45a64bd07d47_a6b35572bc5d3940.png)
![jira-add-transformation-3](assets/images/jira-set-transformation3-6ca1ddad5d756a3fc415171c690f316d_13b302a8a64765a7.png)

<a id="configuration-jira--issue-tracking"></a>

#### Issue Tracking

- Requirement: choose the issue types to be transformed to "REQUIREMENT".
- Bug: choose the issue types to be transformed to "BUG".
- Incident: choose the issue types to be transformed to "INCIDENT".
- Epic Key: choose the custom field that represents Epic key. In most cases, it is "Epic Link".
- Story Point: choose the custom field that represents story points. In most cases, it is "Story Points".

<a id="configuration-jira--additional-settings"></a>

#### Additional Settings

- Remotelink Commit SHA: parse the commits from an issue's remote links by the given regular expression so that the relationship between `issues` and `commits` can be created. You can directly use the regular expression `/commit/([0-9a-f]{40})$`.

<a id="configuration-jira--step-2-collect-data-in-a-project"></a>

## Step 2 - Collect Data in a Project

<a id="configuration-jira--step-21-create-a-project"></a>

### Step 2.1 - Create a Project

Collecing Jira data reuiqres creating a project first. You can visit the Project page from the side menu and create a new project by following the instructions on the user interface.

![create-a-project](assets/images/create-a-project-20e220196044bbf9be564773c45c5990_2492c60a646d31e1.png)

<a id="configuration-jira--step-22-add-a-jira-connection"></a>

### Step 2.2 - Add a Jira Connection

You can add a previously configured Jira connection to the project and select the boards for which you wish to collect the data for.
Please note: if you don't see the boards you are looking for, please check if you have added them to the connection first.

![add-a-connection](assets/images/add-a-connection-project-4032e8e9a72cb4a6df81b6ced714205e_df23b32ff0d3fca6.png)

<a id="configuration-jira--step-23-set-the-sync-policy"></a>

### Step 2.3 - Set the Sync Policy

There are three settings for Sync Policy:

- Data Time Range: You can select the time range of the data you wish to collect. The default is set to the past six months.
- Sync Frequency: You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your prefered schedule.
- Skip Failed Tasks: sometime a few tasks may fail in a long pipeline; you can choose to skip them to avoid spending more time in running the pipeline all over again.

![sync-policy](assets/images/sync-policy-2ac941b2918fc873626375dfe4cbf5f5_a0e6ccde9b3c999b.png)

<a id="configuration-jira--step-24-start-data-collection"></a>

### Step 2.4 - Start Data Collection

Click on "Collect Data" to start collecting data for the whole project. You can check the status in the Status tab on the same page.
![collect-data](assets/images/collect-data-5919e2e6ddad525bca4fbcb46e672aff_083db1164108a1f4.png)

<a id="configuration-jira--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-jira--step-1-add-data-connections)
  - [Stept 1.1 - Authentication](#configuration-jira--stept-11-authentication)
  - [Step 1.2 - Add Data Scopes](#configuration-jira--step-12-add-data-scopes)
  - [Step 1.3 - Add Scope Config (Optional)](#configuration-jira--step-13-add-scope-config-optional)
- [Step 2 - Collect Data in a Project](#configuration-jira--step-2-collect-data-in-a-project)
  - [Step 2.1 - Create a Project](#configuration-jira--step-21-create-a-project)
  - [Step 2.2 - Add a Jira Connection](#configuration-jira--step-22-add-a-jira-connection)
  - [Step 2.3 - Set the Sync Policy](#configuration-jira--step-23-set-the-sync-policy)
  - [Step 2.4 - Start Data Collection](#configuration-jira--step-24-start-data-collection)
- [Troubleshooting](#configuration-jira--troubleshooting)

---

<a id="configuration-pagerduty"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/PagerDuty/ -->

<!-- page_index: 26 -->

# PagerDuty

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PagerDuty

Visit Config UI at: `http://localhost:4000`.

<a id="configuration-pagerduty--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![pagerduty-create-a-connection](assets/images/pagerduty-create-a-connection-06b87c06651b753bffaf348c9738620b_edda72ef3d97a380.png)

<a id="configuration-pagerduty--connection-name"></a>

### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-pagerduty--token"></a>

### Token

Paste your PagerDuty personal access token (PAT) here. You may make it a Read-Only token for the plugin's purposes.

<a id="configuration-pagerduty--test-and-save-connection"></a>

### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-pagerduty--step-1-add-data-connection"></a>

## Step 1 - Add Data Connection

Create a project for PagerDuty by adding the connection created above to it.

![pagerduty-add-data-connection](assets/images/pagerduty-add-data-connection-a17283917188cb9257bf19df1ea7707d_264a93979c77e3b6.png)

<a id="configuration-pagerduty--step-2-setting-data-scope"></a>

## Step 2 - Setting Data Scope

<a id="configuration-pagerduty--select-services"></a>

### Select services

Select the services you want to collect data from.

![pagerduty-set-data-scope](assets/images/pagerduty-set-data-scope-16ac55b48a4c94f599ce7e2c13217d16_4e9d9581dd981796.png)

<a id="configuration-pagerduty--data-entities"></a>

### Data Entities

PagerDuty supports the following data entities.

- Issue Tracking: These map to PagerDuty incidents.

<a id="configuration-pagerduty--step-3-adding-transformation-rules-optional"></a>

## Step 3 - Adding Transformation Rules (Optional)

Currently, this plugin does not support transformation rules, so skip this page by clicking `Next Step`.

<a id="configuration-pagerduty--step-4-set-sync-policy"></a>

## Step 4 - Set Sync Policy

Set the sync policy as you see fit. Note that PagerDuty can only collect data from up to 6 months prior to the present time.

![pagerduty-sync-policy](assets/images/pagerduty-sync-policy-abbde8fa2ebf80b65a9b7f1b0c6dbe4e_86299c882a17c441.png)

<a id="configuration-pagerduty--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-pagerduty--step-1-add-data-connections)
  - [Connection Name](#configuration-pagerduty--connection-name)
  - [Token](#configuration-pagerduty--token)
  - [Test and Save Connection](#configuration-pagerduty--test-and-save-connection)
- [Step 1 - Add Data Connection](#configuration-pagerduty--step-1-add-data-connection)
- [Step 2 - Setting Data Scope](#configuration-pagerduty--step-2-setting-data-scope)
  - [Select services](#configuration-pagerduty--select-services)
  - [Data Entities](#configuration-pagerduty--data-entities)
- [Step 3 - Adding Transformation Rules (Optional)](#configuration-pagerduty--step-3-adding-transformation-rules-optional)
- [Step 4 - Set Sync Policy](#configuration-pagerduty--step-4-set-sync-policy)
- [Troubleshooting](#configuration-pagerduty--troubleshooting)

---

<a id="configuration-sonarqube"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/SonarQube/ -->

<!-- page_index: 27 -->

# SonarQube Server

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# SonarQube Server

Visit Config UI at: `http://localhost:4000`.

<a id="configuration-sonarqube--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![sonarqube-add-data-connections](assets/images/sonarqube-add-data-connections-9536a4d073ce2e86c6f274d294149935_e1cee80b2bb044d7.png)

<a id="configuration-sonarqube--connection-name"></a>

### Connection Name

Name your connection.

<a id="configuration-sonarqube--endpoint-url"></a>

### Endpoint URL

This should be a valid REST API endpoint

- `http://<host>:<port>/api/`

The endpoint url should end with `/`.

<a id="configuration-sonarqube--token"></a>

### Token

Please use a system admin account to create the SonarQube token, because some SonarQube APIs require this permission to list all projects. Learn about [how to create a SonarQube token](https://docs.sonarsource.com/sonarqube/8.9/user-guide/user-account/generating-and-using-tokens/#generating-a-token).

<a id="configuration-sonarqube--proxy-url-optional"></a>

### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-sonarqube--fixed-rate-limit-optional"></a>

### Fixed Rate Limit (Optional)

DevLake uses a dynamic rate limit at around 18,000 requests/hour to collect SonarQube data. You can adjust the rate limit if you want to increase or lower the speed.

<a id="configuration-sonarqube--test-and-save-connection"></a>

### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-sonarqube--step-2-setting-data-scope"></a>

## Step 2 - Setting Data Scope

![sonarqube-set-data-scope](assets/images/sonarqube-set-data-scope-d93d56def8465b3403dc1ea4882ac5c2_f6e43a84b04c1738.png)

<a id="configuration-sonarqube--projects"></a>

### Projects

Choose the SonarQube projects to collect.

<a id="configuration-sonarqube--data-entities"></a>

### Data Entities

Usually, you don't have to modify this part. However, if you don't want to collect certain SonarQube entities, you can unselect some entities to accerlerate the collection speed.

- Code Quality Domain: SonarQube issues, issue code blocks, file metrics, hotspots, etc.
- Cross Domain: SonarQube accounts, etc.

<a id="configuration-sonarqube--step-3-adding-transformation-rules-optional"></a>

## Step 3 - Adding Transformation Rules (Optional)

SonarQube does not have transformation and this step will be skipped.

<a id="configuration-sonarqube--step-4-setting-sync-policy"></a>

## Step 4 - Setting Sync Policy

You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your prefered schedule.

<a id="configuration-sonarqube--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-sonarqube--step-1-add-data-connections)
  - [Connection Name](#configuration-sonarqube--connection-name)
  - [Endpoint URL](#configuration-sonarqube--endpoint-url)
  - [Token](#configuration-sonarqube--token)
  - [Proxy URL (Optional)](#configuration-sonarqube--proxy-url-optional)
  - [Fixed Rate Limit (Optional)](#configuration-sonarqube--fixed-rate-limit-optional)
  - [Test and Save Connection](#configuration-sonarqube--test-and-save-connection)
- [Step 2 - Setting Data Scope](#configuration-sonarqube--step-2-setting-data-scope)
  - [Projects](#configuration-sonarqube--projects)
  - [Data Entities](#configuration-sonarqube--data-entities)
- [Step 3 - Adding Transformation Rules (Optional)](#configuration-sonarqube--step-3-adding-transformation-rules-optional)
- [Step 4 - Setting Sync Policy](#configuration-sonarqube--step-4-setting-sync-policy)
- [Troubleshooting](#configuration-sonarqube--troubleshooting)

---

<a id="configuration-tapd"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Tapd/ -->

<!-- page_index: 28 -->

# TAPD

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# TAPD

Visit Config UI at: `http://localhost:4000` and go to `Connections` page.

<a id="configuration-tapd--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![tapd-add-data-connections](assets/images/tapd-add-data-connections-f3698cc74f0e533bcca3206964290e65_71f1fc0695f64fb2.png)

<a id="configuration-tapd--connection-name"></a>

### Connection Name

Name your connection.

<a id="configuration-tapd--endpoint-url"></a>

### Endpoint URL

This should be a valid REST API endpoint

- `https://api.tapd.cn/`
  The endpoint url should end with `/`.

<a id="configuration-tapd--usernamepassword"></a>

### Username/Password

Input the username and password of your Tapd account, you can follow the steps as below.
![tapd-account](assets/images/tapd-account-4058c8f303edf4c53f94b04368c9251c_dd6d49fc638aa776.png)

<a id="configuration-tapd--proxy-url-optional"></a>

### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-tapd--ralte-limit-optional"></a>

### Ralte Limit (Optional)

For TAPD, we suggest you setting the rate limit to 3500

<a id="configuration-tapd--test-and-save-connection"></a>

### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-tapd--step-2-setting-data-scope"></a>

## Step 2 - Setting Data Scope

![image-20230410224100853](assets/images/230924072-433451e5-97a3-4d99-9ca7-0a43d0bacd01_265bc61ac634ebab.png)

You can find the campany id in your Tapd company dashboard.

![image-20230410223926964](assets/images/230923942-4dd5bbd7-a391-4abc-ab99-ff7543d919ac_b725e594e856d700.png)

<a id="configuration-tapd--workspaces"></a>

### Workspaces

Choose the Tapd workspaces to collect.

<a id="configuration-tapd--data-entities"></a>

### Data Entities

Usually, you don't have to modify this part. However, if you don't want to collect certain Tapd entities, you can unselect some entities to accerlerate the collection speed.

- Issue Tracking: Tapd issues, issue comments, issue labels, etc.
- Cross Domain: Tapd accounts, etc.

<a id="configuration-tapd--step-3-adding-transformation-rules-optional"></a>

## Step 3 - Adding Transformation Rules (Optional)

![image](assets/images/230924606-bf6ef00c-73fa-4a60-be8f-1f27fe4ef6ae_1fbfd09caaa51f7e.png)

Without adding transformation rules, you can not view all charts in "Engineering Throughput and Cycle Time" dashboards.

Each Tapd workspace can be configured with different transformation rules.

<a id="configuration-tapd--issue-tracking"></a>

### Issue Tracking

- Requirement: choose the issue types to be transformed to "REQUIREMENT".
- Bug: choose the issue types to be transformed to "BUG".
- Incident: choose the issue types to be transformed to "INCIDENT".
- TODO: The issues that are planned but have not been worked on yet
- IN-PROGRESS: The issues that are work-in-progress
- DONE: The issues that are completed

<a id="configuration-tapd--step-4-setting-sync-policy"></a>

## Step 4 - Setting Sync Policy

You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your prefered schedule.

<a id="configuration-tapd--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-tapd--step-1-add-data-connections)
  - [Connection Name](#configuration-tapd--connection-name)
  - [Endpoint URL](#configuration-tapd--endpoint-url)
  - [Username/Password](#configuration-tapd--usernamepassword)
  - [Proxy URL (Optional)](#configuration-tapd--proxy-url-optional)
  - [Ralte Limit (Optional)](#configuration-tapd--ralte-limit-optional)
  - [Test and Save Connection](#configuration-tapd--test-and-save-connection)
- [Step 2 - Setting Data Scope](#configuration-tapd--step-2-setting-data-scope)
  - [Workspaces](#configuration-tapd--workspaces)
  - [Data Entities](#configuration-tapd--data-entities)
- [Step 3 - Adding Transformation Rules (Optional)](#configuration-tapd--step-3-adding-transformation-rules-optional)
  - [Issue Tracking](#configuration-tapd--issue-tracking)
- [Step 4 - Setting Sync Policy](#configuration-tapd--step-4-setting-sync-policy)
- [Troubleshooting](#configuration-tapd--troubleshooting)

---

<a id="configuration-teambition"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Teambition/ -->

<!-- page_index: 29 -->

# Teambition(WIP)

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Teambition(WIP)

Visit Config UI: `http://localhost:4000` and go to `Connections` page.

<a id="configuration-teambition--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![teambition-add-data-connections](assets/images/229744282-1959dc82-9038-49a8-924d-11821fafa73a_96aaf541c6ebd776.png)

<a id="configuration-teambition--connection-name"></a>

### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-teambition--endpoint-url"></a>

#### Endpoint URL

This should be a valid REST API endpoint

- `https://open.teambition.com/api/`
  The endpoint url should end with `/`.

<a id="configuration-teambition--app-idsecret-key"></a>

### App Id/Secret Key

Input the app id and secret key of your Teambition account, you can follow the steps as below.
![image-20230404213648139](assets/images/229810617-fe75cf7d-5a84-4741-9016-47140b276e18_bffb5f2bbea04cca.png)![image](assets/images/229810458-cf47806b-6307-419c-8147-a176ebafca74_b054c69fdef1a800.png)

You should ensure that you have added all the necessary "get" and "list" authentication methods.

![image](assets/images/229813323-0c490e65-1ecb-4e1c-8df2-ef68cb55a4a4_e47fdfea6832285a.png)

<a id="configuration-teambition--tenant-typetenant-id"></a>

#### Tenant Type/Tenant Id

It is important to add your app before finding the Tenant Id.

![image](assets/images/229812333-188e497f-db5c-426c-ad1e-6fdb5e1e3b17_f872934e18b5aac6.png)

![image](assets/images/229812594-e3c619cb-363d-491f-aeae-3e8e6912c70a_f9e1b60958e3b18f.png)

![image](assets/images/229814145-9bdf006e-450e-4c14-98c6-a5b3fba690ea_6e7ebf42c79fde15.png)

<a id="configuration-teambition--proxy-url-optional"></a>

### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-teambition--ralte-limit-optional"></a>

### Ralte Limit (Optional)

For Teambition, we suggest you setting the rate limit to 5000

<a id="configuration-teambition--test-and-save-connection"></a>

### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-teambition--step-2-configure-blueprint"></a>

## Step 2 - Configure Blueprint

Similar to other beta plugins, Teambition does not support `project`, which means, you can only collect Teambition data via blueprint's advanced mode.

Please go to the `Blueprints` page and switch to advanced mode. See how to use advanced mode and JSON [examples](#configuration-advancedmode--11-teambition).

<a id="configuration-teambition--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-teambition--step-1-add-data-connections)
  - [Connection Name](#configuration-teambition--connection-name)
  - [App Id/Secret Key](#configuration-teambition--app-idsecret-key)
  - [Proxy URL (Optional)](#configuration-teambition--proxy-url-optional)
  - [Ralte Limit (Optional)](#configuration-teambition--ralte-limit-optional)
  - [Test and Save Connection](#configuration-teambition--test-and-save-connection)
- [Step 2 - Configure Blueprint](#configuration-teambition--step-2-configure-blueprint)
- [Troubleshooting](#configuration-teambition--troubleshooting)

---

<a id="configuration-webhook"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/webhook/ -->

<!-- page_index: 30 -->

# Webhooks

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Webhooks

Visit config-ui: `http://{localhost}:4000`.

<a id="configuration-webhook--step-1-add-a-new-incoming-webhook"></a>

### Step 1 - Add a new incoming webhook

Go to the 'Connections' page. Create a webhook with a unique name.

![webhook-add-data-connections](assets/images/webhook-add-eb48af539781d1eab9e7da0802d68c8f_9566e624cb6869e6.png)

<a id="configuration-webhook--step-2-create-webhooks-connection"></a>

### Step 2 - Create webhooks connection

Click on Generate POST URL, and you will find three webhook URLs.

![webhook-connection1](assets/images/webhook-connection1-e887ee855adf99611df237e7a8a137f5_6390452e75236ac5.png)

Copy the ones that suit your usage into your CI/CD or issue-tracking systems. You can always come back to the webhook page to copy the URLs later on.

A non-expired API key is auto-generated for the authentication of the webhook. This API key only shows in the payload when you create the webhook. However, you can always revoke and generate a new token when you view the webhook details.

See the [full payload schema](https://devlake.apache.org/docs/v1.0/Plugins/webhook) of webhooks.

<a id="configuration-webhook--step-3-use-webhook-in-a-project"></a>

### Step 3 - Use webhook in a project

If you want to use webhook data to measure [DORA metrics](#dora), you have to associate it with a DevLake project.

- Go to the 'Incoming Webhooks' tab on a project's page.
- Add webhook by selecting the existing webhook.
- Go to the project's blueprint page and click 'Collect Data'. This will trigger the DORA plugin to measure DORA metrics with the data collected by the [data connections and webhooks associated with this project](#configuration-howtoorganizedevlakeprojects--2-why-is-it-important-to-organize-projects).

![project-webhook-use](assets/images/project-webhook-use-6163946d4d066eb59480da8d01eade50_a49599a548b76338.png)

<a id="configuration-webhook--put-webhook-on-the-internet"></a>

#### Put webhook on the internet

For the new webhook to work, it needs to be accessible from the DevOps tools from which you would like to push data to DevLake. If DevLake is deployed in your private network and your DevOps tool (e.g. CircleCI) is a cloud service that lives outside of your private network, then you need to make DevLake's webhook accessible to the outside cloud service.

There are many tools for this:

- For testing and quick setup, [ngrok](https://ngrok.com/) is a useful utility that provides a publicly accessible web URL to any locally hosted application. You can put DevLake's webhook on the internet within 5 mins by following ngrok's [Getting Started](https://ngrok.com/docs/getting-started) guide. Note that, when posting to webhook, you may need to replace the `localhost` part in the webhook URL with the forwarding URL that ngrok provides.
- If you prefer DIY, please check out open-source reverse proxies like [fatedier/frp](https://github.com/fatedier/frp) or go for the classic [nginx](https://www.nginx.com/).

<a id="configuration-webhook--troubleshooting"></a>

## Troubleshooting

If you run into any problems, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues).

- [Step 1 - Add a new incoming webhook](#configuration-webhook--step-1-add-a-new-incoming-webhook)
- [Step 2 - Create webhooks connection](#configuration-webhook--step-2-create-webhooks-connection)
- [Step 3 - Use webhook in a project](#configuration-webhook--step-3-use-webhook-in-a-project)
- [Troubleshooting](#configuration-webhook--troubleshooting)

---

<a id="configuration-zentao"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Zentao/ -->

<!-- page_index: 31 -->

# Zentao

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Zentao

Visit Config UI at: `http://localhost:4000` and go to `Connections` page.

<a id="configuration-zentao--step-1-add-data-connections"></a>

## Step 1 - Add Data Connections

![zentao-add-data-connections](assets/images/zentao-create-a-connection-04a6a47435a4d49337073828460f5251_eb4ada6fe8e4ff0f.png)

<a id="configuration-zentao--connection-name"></a>

### Connection Name

Give your connection a unique name to help you identify it in the future.

<a id="configuration-zentao--endpoint-url"></a>

### Endpoint URL

Please ensure that the REST API endpoint URL is valid. It should be in the format of either `http://<host>:<port>/api.php/v1/` or `http://<host>:<port>/zentao/api.php/v1/`.

If the initial test fails, please try another endpoint URL as the URL depends on where Zentao is deployed. Additionally, please ensure that the endpoint URL ends with a forward slash `/`.

<a id="configuration-zentao--usernamepassword"></a>

### Username/Password

Input the username and password of your Zentao account.

<a id="configuration-zentao--proxy-url-optional"></a>

### Proxy URL (Optional)

If you are behind a corporate firewall or VPN you may need to utilize a proxy server. Enter a valid proxy server address on your network, e.g. `http://your-proxy-server.com:1080`

<a id="configuration-zentao--test-and-save-connection"></a>

### Test and Save Connection

Click `Test Connection`, if the connection is successful, click `Save Connection` to add the connection.

<a id="configuration-zentao--step-2-setting-data-scope"></a>

## Step 2 - Setting Data Scope

![image](assets/images/230921313-d43821c2-0c41-4bb4-b1ef-d87e4afb1fa4_bc790dda4b32a658.png)

<a id="configuration-zentao--projects-and-products"></a>

### Projects and Products

Please select the Zentao products for collecting stories/bugs and the Zentao projects for collecting executions. Both will also collect information on accounts/departments.

<a id="configuration-zentao--data-entities"></a>

### Data Entities

Usually, you don't have to modify this part. However, if you don't want to collect certain Lento entities, you can unselect some entities to accerlerate the collection speed.

- Issue Tracking: Lento issues, issue comments, issue labels, etc.

<a id="configuration-zentao--step-3-adding-transformation-rules-optional"></a>

## Step 3 - Adding Transformation Rules (Optional)

Zentao does not have transformation and this step will be skipped.

<a id="configuration-zentao--step-4-setting-sync-policy"></a>

## Step 4 - Setting Sync Policy

You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your prefered schedule.

<a id="configuration-zentao--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Step 1 - Add Data Connections](#configuration-zentao--step-1-add-data-connections)
  - [Connection Name](#configuration-zentao--connection-name)
  - [Endpoint URL](#configuration-zentao--endpoint-url)
  - [Username/Password](#configuration-zentao--usernamepassword)
  - [Proxy URL (Optional)](#configuration-zentao--proxy-url-optional)
  - [Test and Save Connection](#configuration-zentao--test-and-save-connection)
- [Step 2 - Setting Data Scope](#configuration-zentao--step-2-setting-data-scope)
  - [Projects and Products](#configuration-zentao--projects-and-products)
  - [Data Entities](#configuration-zentao--data-entities)
- [Step 3 - Adding Transformation Rules (Optional)](#configuration-zentao--step-3-adding-transformation-rules-optional)
- [Step 4 - Setting Sync Policy](#configuration-zentao--step-4-setting-sync-policy)
- [Troubleshooting](#configuration-zentao--troubleshooting)

---

<a id="configuration-advancedmode"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/AdvancedMode/ -->

<!-- page_index: 32 -->

# Blueprint Advanced Mode

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Blueprint Advanced Mode

<a id="configuration-advancedmode--why-advanced-mode"></a>

## Why advanced mode?

Advanced mode allows users to create any pipeline by writing JSON. This is useful for users who want to:

1. Collect multiple GitHub/GitLab repos or Jira projects within a single pipeline
2. Have fine-grained control over what entities to collect or what subtasks to run for each plugin
3. Orchestrate a complex pipeline that consists of multiple stages of plugins.

Advanced mode gives utmost flexibility to users by exposing the JSON API.

<a id="configuration-advancedmode--how-to-use-advanced-mode-to-create-pipelines"></a>

## How to use advanced mode to create pipelines?

1. Click on "+ New Blueprint" on the Blueprint page.

![image](assets/images/advancedmode1-b57f41fff7e23f19c2af911e2adaddcf_c0342efbebd8a312.png)

2. In step 1, click on the "Advanced Mode" link.

![image](assets/images/advancedmode2-3dd7ce37847a5d866cad6d9a45779830_eabac4bc0627376a.png)

3. The pipeline editor expects a 2D array of plugins. The first dimension represents different stages of the pipeline and the second dimension describes the plugins in each stage. Stages run in sequential order and plugins within the same stage runs in parallel. We provide some templates for users to get started. Please also see the next section for some examples.

![image](assets/images/advancedmode3-9194e51e02f239171d9f920cb9d3dd6c_1ed77ad6b37c9fab.png)

4. You can choose how often you would like to sync your data in this step by selecting a sync frequency option or enter a cron code to specify your preferred schedule. After setting up the Blueprint, you will be prompted to the Blueprint's activity detail page, where you can track the progress of the current run and wait for it to finish before the dashboards become available. You can also view all historical runs of previously created Blueprints from the list on the Blueprint page.

<a id="configuration-advancedmode--examples"></a>

## Examples

<a id="configuration-advancedmode--1-github"></a>

### 1. GitHub

Collect multiple GitHub repos sequentially. Below is an example for collecting 2 GitHub repos sequentially. It has 2 stages, each contains a GitHub task.

```text
[
  [
    {
      "Plugin": "github",
      "Options": {
        "connectionId": 1,
        "repo": "incubator-devlake",
        "owner": "apache"
      }
    },
    {
      "Plugin": "github",
      "Options": {
        "connectionId": 1,
        "repo": "lake",
        "owner": "merico-dev"
      }
    }
  ]
]
```

GitHub:

- `connectionId`: The ID of your GitHub connection at page http://localhost:4000/connections/github.
- `owner`: Just take a look at the URL: <https://github.com/apache/incubator-devlake>, owner is `apache`.
- `repo`: Just take a look at the URL: <https://github.com/apache/incubator-devlake>, repo is `incubator-devlake`.

<a id="configuration-advancedmode--2-gitlab"></a>

### 2. GitLab

Collect multiple GitLab repos sequentially.

> When there're multiple collection tasks against a single data source, we recommend running these tasks sequentially since the collection speed is mostly limited by the API rate limit of the data source.
> Running multiple tasks against the same data source is unlikely to speed up the process and may overwhelm the data source.

Below is an example for collecting 2 GitLab repos sequentially. It has 2 stages, each contains a GitLab task.

```text
[
  [
    {
      "Plugin": "gitlab",
      "Options": {
        "connectionId": 1,
        "projectId": 152***74
      }
    }
  ],
  [
    {
      "Plugin": "gitlab",
      "Options": {
        "connectionId": 2,
        "projectId": 116***98
      }
    }
  ]
]
```

- `connectionId`: The ID of your GitLab connection at page http://localhost:4000/connections/gitlab.
- `projectId`: GitLab repo's Project ID.

<a id="configuration-advancedmode--3-jenkins"></a>

### 3. Jenkins

Collect multiple Jenkins jobs sequentially. Below is an example for collecting 2 Jenkins jobs sequentially. It has 2 stages, each contains a Jenkins task.

```text
[
    [
        {
            "plugin": "jenkins",
            "options": {
                "connectionId": 1,
                "scopeId": "auto_deploy"
            }
        }
    ],
    [
        {
            "plugin": "jenkins",
            "options": {
                "connectionId": 2,
                "scopeId": "Deploy test"
            }
        }
    ]
]
```

- `connectionId`: The ID of your Jenkins connection at page http://localhost:4000/connections/jenkins.
- `scopeId`: Jenkins job name.

<a id="configuration-advancedmode--4-jira"></a>

### 4. Jira

Collect multiple Jira boards sequentially. Below is an example for collecting 2 Jira boards sequentially. It has 2 stages, each contains a Jira task.

```text
[
    [
        {
            "plugin": "jira",
            "options": {
                "boardId": 8,
                "connectionId": 1
            }
        }
    ],
    [
        {
            "plugin": "jira",
            "options": {
                "boardId": 26,
                "connectionId": 1
            }
        }
    ]
]
```

- `connectionId`: The ID of your Jira connection at page http://localhost:4000/connections/jira.
- `boardId`: Just take a look at the URL - it will be the last number in the address. Should look something like this at the end: `RapidBoard.jspa?rapidView=8` or `/projects/xxx/boards/8`. So `8` would be the board ID in that case.

<a id="configuration-advancedmode--5-jira-gitlab"></a>

### 5. Jira + GitLab

Below is an example for collecting a GitLab repo and a Jira board in parallel. It has a single stage with a GitLab task and a Jira task. As GitLab and Jira are using their own tokens, they can be executed in parallel.

```text
[
    [
        {
            "plugin":"jira",
            "options":{
                "boardId":8,
                "connectionId":1
            }
        }
    ],
    [
        {
            "Plugin":"gitlab",
            "Options":{
                "connectionId":1,
                "projectId":116***98
            }
        }
    ]
]
```

<a id="configuration-advancedmode--6-tapd"></a>

### 6. TAPD

Below is an example for collecting a TAPD workspace. Since users can configure multiple TAPD connection, it's required to pass in a `connectionId` for TAPD task to specify which connection to use.

```text
[
    [
        {
            "plugin": "tapd",
            "options": {
                "createdDateAfter": "2006-01-02T15:04:05Z",
                "workspaceId": 34***66,
                "connectionId": 1
            }
        }
    ]
]
```

- `createdDateAfter`: The data range you wish to collect after the given date.
- `connectionId`: The ID of your TAPD connection at page http://localhost:4000/connections/tapd.
- `workspaceId`: TAPD workspace id, you can get it from two ways:
  - url: ![tapd-workspace-id](assets/images/tapd-find-workspace-id-9ff3c284a5966c50cb962518da677028_0b6dd820379e5380.png)
  - db: you can check workspace info from db.\_tool\_tapd\_workspaces and get all workspaceId you want to collect after execution of the following json in `advanced mode`


```json
[
  [
    {
      "plugin": "tapd",
      "options": {
        "companyId": 558***09,
        "workspaceId": 1,
        "connectionId": 1
      },
      "subtasks": ["collectCompanies", "extractCompanies"]
    }
  ]
]
```

<a id="configuration-advancedmode--7-tapd-gitlab"></a>

### 7. TAPD + GitLab

Below is an example for collecting a TAPD workspace and a GitLab repo in parallel. It has a single stage with a TAPD task and a GitLab task.

```text
[
    [
        {
            "plugin": "tapd",
            "options": {
                "createdDateAfter": "2006-01-02T15:04:05Z",
                "workspaceId": 6***14,
                "connectionId": 1
            }
        }
    ],
    [
        {
            "Plugin":"gitlab",
            "Options":{
                "connectionId":1,
                "projectId":116***98
            }
        }
    ]
]
```

<a id="configuration-advancedmode--8-zentao"></a>

### 8. Zentao

Below is an example for collecting a Zentao workspace. Since users can configure multiple Zentao connection, it's required to pass in a `connectionId` for Zentao task to specify which connection to use.

```text
[
  [
    {
      plugin: 'zentao',
      options: {
        connectionId: 1,
        productId: 1,
        projectId: 1,
        executionId: 1
      }
    }
  ]
]
```

- `connectionId`: The ID of your Zentao connection at page http://localhost:4000/connections/zentao.
- `productId`: optional, ZENTAO product id, see "Find Product Id" for details.
- `projectId`: optional, ZENTAO product id, see "Find Project Id" for details.
- `executionId`: optional, ZENTAO product id, see "Find Execution Id" for details.

You must choose at least one of `productId`, `projectId` and `executionId`.

<a id="configuration-advancedmode--find-product-id"></a>

#### Find Product Id

1. Navigate to the Zentao Product in the browser
   ![](assets/images/zentao-product-7ce1f181a027be0785868c2129d778c5_02b5a28cd7093355.png)
2. Click the red square annotated in the pic above
   ![](assets/images/zentao-product-id-e446124e43c79f4a6a17855d1d64ad13_e0debdc7532fdebf.png)
3. Then the number in the red circle above is `ProductId`

<a id="configuration-advancedmode--find-project-id"></a>

#### Find Project Id

1. Navigate to the Zentao Project in the browser
   ![](assets/images/zentao-project-id-5b01a92ea6a9275b6bdf4b33b7485ebd_6b74cbf875c9a719.png)
2. Then the number in the red square above is `ProjectId`

<a id="configuration-advancedmode--find-execution-id"></a>

#### Find Execution Id

1. Navigate to the Zentao Execution in the browser
   ![](assets/images/zentao-execution-id-498b8dc784a8e78ebadc01f07f613589_1d381c8e74e389a2.png)
2. Then the number in the red square above is `ExecutionId`

<a id="configuration-advancedmode--9-bitbucket"></a>

### 9. BitBucket

Below is an example for collecting a bitbucket repo.

```json
[
  [
    {
      "plugin": "bitbucket",
      "options": {
        "connectionId": 1,
        "owner": "apache",
        "repo": "devlake"
      }
    }
  ]
]
```

- `connectionId`: The ID of your bitbucket connection at page http://localhost:4000/connections/bitbucket.
- `owner`: the owner of the repository.
- `repo`: the bitbucket repository name.

<a id="configuration-advancedmode--10-sonarqube"></a>

### 10. SonarQube

Below is an example for collecting a SonarQube project.

```json
[
  [
    {
      "plugin": "sonarqube",
      "options": {
        "connectionId": 1,
        "projectKey": "testDevLake"
      }
    }
  ]
]
```

- `connectionId`: The ID of your SonarQube connection at page http://localhost:4000/connections/sonarqube.
- `projectKey`: The project key of the SonarQube. To find the project key in SonarQube, please follow the steps:
  - 1. Log in to the SonarQube management page.
  - 2. Find the project for which you want to find the project key.
  - 3. Click on the project name to enter the project homepage.
  - 4. In the top menu bar of the project homepage, select "Project Information".
  - 5. On the "Project Information" page, you will see the project key.

<a id="configuration-advancedmode--11-teambition"></a>

### 11. Teambition

Below is an example for collecting a Teambition project. Since users can configure multiple Teambition connection, it's required to pass in a `connectionId` for Teambition task to specify which connection to use.

```json
[
    [
        {
            "plugin": "teambition",
            "options": {
                "createdDateAfter": "2006-01-02T15:04:05Z",
                "projectId": "5e5****376",
                "connectionId": 1
            }
        }
    ]
]
```

- `connectionId`: The ID of your Teambition connection at page http://localhost:4000/connections/teambition.
- `projectId`: Teambition project id, you can get it from url: ![image](assets/images/229808849-66dac8c0-5ff6-459b-850c-62bc60a3a519_5c1a66cf7de1d391.png)

<a id="configuration-advancedmode--editing-a-blueprint-advanced-mode"></a>

## Editing a Blueprint (Advanced Mode)

This section is for editing a Blueprint in the Advanced Mode. To edit in the Normal mode, please refer to [this guide](#configuration-tutorial--editing-a-blueprint-normal-mode).

To edit a Blueprint created in the Advanced mode, you can simply go the Configuration page of that Blueprint and edit its configuration.

![img](assets/images/blueprint-edit2-ca4a8895cfae74109b65dcdbda816ce3_d2959ce77ad1a931.png)

<a id="configuration-advancedmode--how-to-skip-collectors-in-a-blueprint-advanced-mode"></a>

## How to skip collectors in a Blueprint (Advanced Mode)?

- 1. Create a Blueprint in the Advanced Mode.
- 2. You can skip collectors in a Blueprint by setting `skipCollectors` to `true` in the request body of the trigger API. For example:

```text
  curl --request POST \
    --url http://localhost:8080/blueprints/:blueprintId/trigger \
    --header 'content-type: application/json' \
    --data '{
      "skipCollectors": true
  }'
```

<a id="configuration-advancedmode--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-configuration) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Why advanced mode?](#configuration-advancedmode--why-advanced-mode)
- [How to use advanced mode to create pipelines?](#configuration-advancedmode--how-to-use-advanced-mode-to-create-pipelines)
- [Examples](#configuration-advancedmode--examples)
  - [1. GitHub](#configuration-advancedmode--1-github)
  - [2. GitLab](#configuration-advancedmode--2-gitlab)
  - [3. Jenkins](#configuration-advancedmode--3-jenkins)
  - [4. Jira](#configuration-advancedmode--4-jira)
  - [5. Jira + GitLab](#configuration-advancedmode--5-jira-gitlab)
  - [6. TAPD](#configuration-advancedmode--6-tapd)
  - [7. TAPD + GitLab](#configuration-advancedmode--7-tapd-gitlab)
  - [8. Zentao](#configuration-advancedmode--8-zentao)
  - [9. BitBucket](#configuration-advancedmode--9-bitbucket)
  - [10. SonarQube](#configuration-advancedmode--10-sonarqube)
  - [11. Teambition](#configuration-advancedmode--11-teambition)
- [Editing a Blueprint (Advanced Mode)](#configuration-advancedmode--editing-a-blueprint-advanced-mode)
- [How to skip collectors in a Blueprint (Advanced Mode)?](#configuration-advancedmode--how-to-skip-collectors-in-a-blueprint-advanced-mode)
- [Troubleshooting](#configuration-advancedmode--troubleshooting)

---

<a id="configuration-apikeys"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/APIKeys/ -->

<!-- page_index: 33 -->

# API Keys

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# API Keys

<a id="configuration-apikeys--what-is-an-api-key"></a>

## What is an 'API Key'

![api-key-list](assets/images/api-key-list-35169cf33ad13b64d7e3fa395d6d285c_2913cd2b7d40476d.png)

An API key, also known as an API token, is a string used for authentication when making requests to DevLake's open API or webhook. It serves as a form of identification to ensure authorized access.

An API key contains three components:

1. Name: This is the descriptive name assigned to the key for easy identification.
2. Expiration: You have the option to set an expiration period for the API key, such as 7 days, 30 days, 90 days, or choose for it to never expire.
3. Allowed Path: The API URL or endpoint that the API key is permitted to access. It defines the specific resources that the key can interact with.

<a id="configuration-apikeys--how-does-an-api-key-work"></a>

## How does an API key work?

<a id="configuration-apikeys--accessing-devlake-open-apis"></a>

### Accessing DevLake Open APIs

Check out the [API docs](https://devlake.apache.org/docs/Overview/References).

<a id="configuration-apikeys--utilizing-api-key-in-incoming-webhooks"></a>

### Utilizing API Key in [Incoming Webhooks](#configuration-webhook)

It is typically not necessary to manually create an API key from the 'API keys' page. Instead, you can follow these steps:

1. Navigate to the 'Data Connection' page.
2. Create a new webhook, and an API key will be automatically generated for you.
3. You can copy the provided curl commands, which include the API key, and save them in your local environment for future use.
4. If you happen to forget to save the API key, do not worry. You can view the webhook details and regenerate a new API key if needed. It is important to note that the API keys automatically generated for webhooks will not be displayed on the 'API keys' page.

![api-key-list](assets/images/auto-generated-api-key-bf75b32badf805e667fc510c15ad2d53_87ce2c9cea8a11f5.png)

<a id="configuration-apikeys--troubleshooting"></a>

## Troubleshooting

If you run into any problems, please check the [Troubleshooting](#troubleshooting-installation) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [What is an 'API Key'](#configuration-apikeys--what-is-an-api-key)
- [How does an API key work?](#configuration-apikeys--how-does-an-api-key-work)
  - [Accessing DevLake Open APIs](#configuration-apikeys--accessing-devlake-open-apis)
  - [Utilizing API Key in Incoming Webhooks](#configuration-apikeys--utilizing-api-key-in-incoming-webhooks)
- [Troubleshooting](#configuration-apikeys--troubleshooting)

---

<a id="configuration-teamconfiguration"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/TeamConfiguration/ -->

<!-- page_index: 34 -->

# Team Configuration

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Team Configuration

<a id="configuration-teamconfiguration--what-is-team-configuration-and-how-it-works"></a>

## What is 'Team Configuration' and how it works?

To organize and display metrics by `team`, Apache DevLake needs to know about the team configuration in an organization, specifically:

1. What are the teams?
2. Who are the users(unified identities)?
3. Which users belong to a team?
4. Which accounts(identities in specific tools) belong to the same user?

Each of the questions above corresponds to a table in DevLake's schema, illustrated below:

![image](assets/images/teamflow0-e3332efd877ee18bb43b83f6ba789bac_8c04dacc9f4dfc01.png)

1. `teams` table stores all the teams in the organization.
2. `users` table stores the organization's roster. An entry in the `users` table corresponds to a person in the org.
3. `team_users` table stores which users belong to a team.
4. `user_accounts` table stores which accounts belong to a user. An `account` refers to an identiy in a DevOps tool and is automatically created when importing data from that tool. For example, a `user` may have a GitHub `account` as well as a Jira `account`.

Apache DevLake uses a simple heuristic algorithm based on emails and names to automatically map accounts to users and populate the `user_accounts` table.
When Apache DevLake cannot confidently map an `account` to a `user` due to insufficient information, it allows DevLake users to manually configure the mapping to ensure accuracy and integrity.

<a id="configuration-teamconfiguration--a-step-by-step-guide"></a>

## A step-by-step guide

In the following sections, we'll walk through how to configure teams and create the five aforementioned tables (`teams`, `users`, `team_users`, `accounts`, and `user_accounts`).
The overall workflow is:

1. Create the `teams` table
2. Create the `users` and `team_users` table
3. Populate the `accounts` table via data collection
4. Run a heuristic algorithm to populate `user_accounts` table
5. Manually update `user_accounts` when the algorithm can't catch everything

> [!INFO]
> 1. Please replace `/path/to/*.csv` with the absolute path of the CSV file you'd like to upload.
> 2. Please replace `http://127.0.0.1:4000` with your actual Config UI service IP and port number. If you have enabled HTTPS, please replace it accordingly.
> 3. Please create your API key on the `API Keys` page instead of using the automatically generated key from the webhook creation.

<a id="configuration-teamconfiguration--step-1-create-the-teams-table"></a>

## Step 1 - Create the `teams` table

You can create the `teams` table by sending a PUT request to `/plugins/org/teams.csv` with a `teams.csv` file. To jumpstart the process, you can download a template `teams.csv` from `/plugins/org/teams.csv?fake_data=true`. Below are the detailed instructions:

1. Download the template `teams.csv` file. You can do it by

   a. Pasting the URL into your browser to download the template.


```text
http://127.0.0.1:4000/api/plugins/org/teams.csv?fake_data=true
```

   b. Or using CURL:


```text
curl 'http://127.0.0.1:4000/api/rest/plugins/org/teams.csv?fake_data=true'  -X 'GET' -H 'Authorization: Bearer {API_key}'
```

2. Fill out `teams.csv` file and upload it to DevLake (If you are using Excel to modify the CSV file, please save it with UTF-8 encoding. See [how](https://answers.microsoft.com/en-us/msoffice/forum/all/how-can-i-save-a-csv-with-utf-8-encoding-using/12801501-c1e4-4a64-80d9-96b680b64cfe))

   a. Fill out `teams.csv` with your org data. Please don't modify the column headers or the file suffix.

   b. Upload `teams.csv` to DevLake with the following curl command


```text
curl 'http://127.0.0.1:4000/api/rest/plugins/org/teams.csv' -X 'PUT' -H 'Authorization: Bearer {API_key}' --form 'file=@"/path/to/teams.csv"'
```

   c. The PUT request would populate the `teams` table with data from `teams.csv` file.
   You can connect to the database and verify the data in the `teams` table. See 'Appendix A' for how to connect to the database.

   ![image](assets/images/teamflow3-b45b67eed4d0241da98eb650d276c596_120bf594b8c0b790.png)

<a id="configuration-teamconfiguration--step-2-create-the-users-and-team_users-table"></a>

## Step 2 - Create the `users` and `team_users` table

You can create the `users` and `team_users` table by sending a single PUT request to `/plugins/org/users.csv` with a `users.csv` file. To jumpstart the process, you can download a template `users.csv` from `/plugins/org/users.csv?fake_data=true`. Below are the detailed instructions:

1. Download the template `users.csv` file. You can do it by

   a. Pasting the URL into your browser to download the template.


```text
http://127.0.0.1:4000/api/plugins/org/users.csv?fake_data=true
```

   b. Or using CURL:


```text
curl 'http://127.0.0.1:4000/api/rest/plugins/org/users.csv?fake_data=true'  -X 'GET' -H 'Authorization: Bearer {API_key}'
```

2. Fill out `users.csv` and upload it to DevLake (If you are using Excel to modify the CSV file, please save it with UTF-8 encoding. See [how](https://answers.microsoft.com/en-us/msoffice/forum/all/how-can-i-save-a-csv-with-utf-8-encoding-using/12801501-c1e4-4a64-80d9-96b680b64cfe))

   a. Fill out `users.csv` with your org data. Please do not modify the column headers or the file suffix.

   b. Upload `users.csv` to DevLake with the following curl command:


```text
curl 'http://127.0.0.1:4000/api/rest/plugins/org/users.csv' -X 'PUT' -H 'Authorization: Bearer {API_key}' --form 'file=@"/path/to/users.csv"'
```

   c. The PUT request would populate the `users` table along with the `team_users` table with data from `users.csv` file. You can connect to the database and verify these two tables.

   ![image](assets/images/teamflow1-73bddf3280eff9dd9b82a98ea2150ac3_bd7109db80d40c54.png)

   ![image](assets/images/teamflow2-cb7557cb19dee75f241a741049333e04_d0463c0a24ea0c33.png)
3. If you want to update `team_users` or `users` table, simply upload the updated `users.csv` to DevLake again following the previous step.

<a id="configuration-teamconfiguration--step-3-populate-the-accounts-table-via-data-collection"></a>

## Step 3 - Populate the `accounts` table via data collection

The `accounts` table is automatically populated when you collect data from data sources like GitHub and Jira through DevLake.

For example, the GitHub plugin would create one entry in the `accounts` table for each GitHub user involved in your repository. For demo purposes, we will insert some mock data into the `accounts` table using SQL:

```text
INSERT INTO `accounts` (`id`, `created_at`, `updated_at`, `_raw_data_params`, `_raw_data_table`, `_raw_data_id`, `_raw_data_remark`, `email`, `full_name`, `user_name`, `avatar_url`, `organization`, `created_date`, `status`)
VALUES
        ('github:GithubAccount:1:1234', '2022-07-12 10:54:09.632', '2022-07-12 10:54:09.632', '{\"ConnectionId\":1,\"Owner\":\"apache\",\"Repo\":\"incubator-devlake\"}', '_raw_github_api_pull_request_reviews', 28, '', 'TyroneKCummings@teleworm.us', '', 'Tyrone K. Cummings', 'https://avatars.githubusercontent.com/u/101256042?u=a6e460fbaffce7514cbd65ac739a985f5158dabc&v=4', '', NULL, 0),
        ('jira:JiraAccount:1:629cdf', '2022-07-12 10:54:09.632', '2022-07-12 10:54:09.632', '{\"ConnectionId\":1,\"BoardId\":\"76\"}', '_raw_jira_api_users', 5, '', 'DorothyRUpdegraff@dayrep.com', '', 'Dorothy R. Updegraff', 'https://avatars.jiraxxxx158dabc&v=4', '', NULL, 0);
```

![image](assets/images/teamflow4-53a9ee2bc9385f4b580775213de1fb42_562b7894a9f07526.png)

<a id="configuration-teamconfiguration--step-4-run-a-heuristic-algorithm-to-populate-user_accounts-table"></a>

## Step 4 - Run a heuristic algorithm to populate `user_accounts` table

Now that we have data in both the `users` and `accounts` table, we can tell DevLake to infer the mappings between `users` and `accounts` with a simple heuristic algorithm based on names and emails.

1. Send an API request to DevLake to run the mapping algorithm


```text
curl --location --request POST '127.0.0.1:4000/api/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '{
    "name": "test",
    "plan":[
        [
            {
                "plugin": "org",
                "subtasks":["connectUserAccountsExact"]
            }
        ]
    ]
}'
```

2. After successful execution, you can verify the data in `user_accounts` in the database.

   ![image](assets/images/teamflow5-79508a7cbd6b791786f77db90373c788_891b98386ec9cf5c.png)

<a id="configuration-teamconfiguration--step-5-manually-update-user_accounts-when-the-algorithm-cant-catch-everything"></a>

## Step 5 - Manually update `user_accounts` when the algorithm can't catch everything

It is recommended to examine the generated `user_accounts` table after running the algorithm. We will demonstrate how to manually update `user_accounts` when the mapping is inaccurate or incomplete in this section.

To make manual verification easier, DevLake provides an API for users to download `user_accounts` as a CSV file. Alternatively, you can verify and modify `user_accounts` all by SQL, see Appendix for more info.

1. Download the template by pasting the following URL to your browser:


```text
http://127.0.0.1:4000/api/plugins/org/user_account_mapping.csv
```

   b. Or using CURL:


```text
curl 'http://127.0.0.1:4000/api/rest/plugins/org/user_account_mapping.csv'  -X 'GET' -H 'Authorization: Bearer {API_key}'
```

   ![image](assets/images/teamflow6-681d45c768beb8f3f9001268b0990c2e_27a5074124e901fb.png)
2. If you find the mapping inaccurate or incomplete, you can modify the `user_account_mapping.csv` file and then upload it to DevLake. For example, here we change the `UserId` of row 'Id=github:GithubAccount:1:1234' in the `user_account_mapping.csv` file to 2.
3. Save and upload the updated `user_account_mapping.csv` file with the following curl command (If you are using Excel to modify the CSV file, please save it with UTF-8 encoding. See [how](https://answers.microsoft.com/en-us/msoffice/forum/all/how-can-i-save-a-csv-with-utf-8-encoding-using/12801501-c1e4-4a64-80d9-96b680b64cfe)):


```text
curl 'http://127.0.0.1:4000/api/rest/plugins/org/user_account_mapping.csv' -X 'PUT' -H 'Authorization: Bearer {API_key}' --form 'file=@"/path/to/user_account_mapping.csv"'
```

4. You can verify the data in the `user_accounts` table has been updated.

![image](assets/images/teamflow7-68cb374cc7bb9047659c3896f6e6acba_ce172cd42856a388.png)

<a id="configuration-teamconfiguration--appendix-a-how-to-connect-to-the-database"></a>

## Appendix A: how to connect to the database

There are many ways to connect to the database:

1. Through Grafana. Go to Grafana's Explore page. Switch the SQL editor to the code mode. Then, you can write SQL to describe database and query data.
2. Through database management tools such as Navicat, phyMyAdmin, DataGrip, MySQLWorkbench, etc. Type in your host, port, username and password to connect to the DB. The username and password can be fount in the image or .env file.
3. Through the command line. Take MySQL as an example:


```text
mysql -h <ip> -u <username> -p -P <port>
```

<a id="configuration-teamconfiguration--appendix-b-how-to-examine-user_accounts-via-sql"></a>

## Appendix B: how to examine `user_accounts` via SQL

```text
SELECT a.id as account_id, a.email, a.user_name as account_user_name, u.id as user_id, u.name as real_name
FROM accounts a
        join user_accounts ua on a.id = ua.account_id
        join users u on ua.user_id = u.id
```

<a id="configuration-teamconfiguration--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-installation) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [What is 'Team Configuration' and how it works?](#configuration-teamconfiguration--what-is-team-configuration-and-how-it-works)
- [A step-by-step guide](#configuration-teamconfiguration--a-step-by-step-guide)
- [Step 1 - Create the `teams` table](#configuration-teamconfiguration--step-1-create-the-teams-table)
- [Step 2 - Create the `users` and `team_users` table](#configuration-teamconfiguration--step-2-create-the-users-and-team_users-table)
- [Step 3 - Populate the `accounts` table via data collection](#configuration-teamconfiguration--step-3-populate-the-accounts-table-via-data-collection)
- [Step 4 - Run a heuristic algorithm to populate `user_accounts` table](#configuration-teamconfiguration--step-4-run-a-heuristic-algorithm-to-populate-user_accounts-table)
- [Step 5 - Manually update `user_accounts` when the algorithm can't catch everything](#configuration-teamconfiguration--step-5-manually-update-user_accounts-when-the-algorithm-cant-catch-everything)
- [Appendix A: how to connect to the database](#configuration-teamconfiguration--appendix-a-how-to-connect-to-the-database)
- [Appendix B: how to examine `user_accounts` via SQL](#configuration-teamconfiguration--appendix-b-how-to-examine-user_accounts-via-sql)
- [Troubleshooting](#configuration-teamconfiguration--troubleshooting)

---

<a id="configuration-dashboards-accesscontrol"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Dashboards/AccessControl/ -->

<!-- page_index: 35 -->

# Dashboard Access Control

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Dashboard Access Control

This tutorial shows how to leverage Grafana's role-based access control (RBAC) to manage what dashboards a user has access to. If you're setting up a single DevLake instance to be shared by multiple teams in your organization, this tutorial can help you achieve data segregation between teams.

<a id="configuration-dashboards-accesscontrol--example-solution-one-folder-for-each-team"></a>

## Example solution: one folder for each team

One of the simplest solutions is to create one Grafana folder for each team and assign permissions to teams at the folder level. Below is a step-by-step walk through.

1. Sign in as Grafana admin and create a new folder

![create-new-folder](assets/images/create-new-folder-64fceb44c8f7a9eea17d473e9bf1bc7a_0b70f264654f8bb8.png)

2. Click "Permissions" tab and remove the default access of "Editor (Role)" and "Viewer (Role)"

![folder-permission](assets/images/folder-permission-0010f0b853838c60c911b9f249b69f96_058aeffc024d97b3.png)

After removing default permissions:

![after-remove-default-permissions](assets/images/after-remove-default-permissions-1b8fff455ed303bd220c94aecd72daaa_d951799e08641f24.png)

3. Add "View" permission to the target team (you'll need to create this team in Grafana first)

![add-team-permission](assets/images/add-team-permission-ec18f6f057c5b95cd318e42510abba32_d82ea9a72ff2e2ca.png)

4. Copy/move dashboards into this folder (you may need to edit the dashboard so that it only shows data belongs to this team)

<a id="configuration-dashboards-accesscontrol--reference"></a>

## Reference

1. [Manage dashboard permissions by Grafana](https://grafana.com/docs/grafana/latest/administration/user-management/manage-dashboard-permissions/#grant-dashboard-folder-permissions)

- [Example solution: one folder for each team](#configuration-dashboards-accesscontrol--example-solution-one-folder-for-each-team)
- [Reference](#configuration-dashboards-accesscontrol--reference)

---

<a id="configuration-dashboards-grafanauserguide"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Configuration/Dashboards/GrafanaUserGuide/ -->

<!-- page_index: 36 -->

# Grafana

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Grafana

![](assets/images/128533901-3107e9bf-c3e3-4320-ba47-879fe2b0ea4d_5fb37d4c010333a5.png)

When first visiting Grafana, you will be provided with a sample dashboard with some basic charts setup from the database.

<a id="configuration-dashboards-grafanauserguide--contents"></a>

## Contents

<table><thead><tr><th align="left">Section</th><th align="left">Link</th></tr></thead><tbody><tr><td align="left">Logging In</td><td align="left"><a href="#configuration-dashboards-grafanauserguide--logging-in">View Section</a></td></tr><tr><td align="left">Viewing All Dashboards</td><td align="left"><a href="#configuration-dashboards-grafanauserguide--viewing-all-dashboards">View Section</a></td></tr><tr><td align="left">Customizing a Dashboard</td><td align="left"><a href="#configuration-dashboards-grafanauserguide--customizing-a-dashboard">View Section</a></td></tr><tr><td align="left">Dashboard Settings</td><td align="left"><a href="#configuration-dashboards-grafanauserguide--dashboard-settings">View Section</a></td></tr><tr><td align="left">Provisioning a Dashboard</td><td align="left"><a href="#configuration-dashboards-grafanauserguide--provisioning-a-dashboard">View Section</a></td></tr><tr><td align="left">Troubleshooting DB Connection</td><td align="left"><a href="#configuration-dashboards-grafanauserguide--troubleshooting-db-connection">View Section</a></td></tr></tbody></table>
<a id="configuration-dashboards-grafanauserguide--logging-in"></a>

## Logging In

Once the app is up and running, visit `http://localhost:3002` to view the Grafana dashboard.

Default login credentials are:

- Username: `admin`
- Password: `admin`

<a id="configuration-dashboards-grafanauserguide--viewing-all-dashboards"></a>

## Viewing All Dashboards

To see all dashboards created in Grafana visit `/dashboards`

Or, use the sidebar and click on **Manage**:

![Screen Shot 2021-08-06 at 11 27 08 AM](assets/images/128534617-1992c080-9385-49d5-b30f-be5c96d5142a_6be36a5fa1d8f011.png)

<a id="configuration-dashboards-grafanauserguide--importing-a-dashboard"></a>

## Importing a Dashboard

If you want to import a dashboard to Grafana which you have backed up earlier, please follow the steps below:

1. Click the `Import` icon
2. Click the `Upload JSON file` button
3. If the dashboard conflicts with an existing one, please change the `Name` and `uid`
4. Click `Import`

![grafana-sections](assets/images/upload-dashboard-707b8b22983822618144079fb2095366_3a2bf584c3547511.png)

<a id="configuration-dashboards-grafanauserguide--customizing-a-dashboard"></a>

## Customizing a Dashboard

When viewing a dashboard, click the top bar of a panel, and go to **edit**

![Screen Shot 2021-08-06 at 11 35 36 AM](assets/images/128535505-a56162e0-72ad-46ac-8a94-70f1c7a910ed_dd2944197aaad0c8.png)

**Edit Dashboard Panel Page:**

![grafana-sections](assets/images/128540136-ba36ee2f-a544-4558-8282-84a7cb9df27a_93c6e89bbf037b54.png)

<a id="configuration-dashboards-grafanauserguide--1-preview-area"></a>

### 1. Preview Area

- **Top Left** is the variable select area (custom dashboard variables, used for switching projects, or grouping data)
- **Top Right** we have a toolbar with some buttons related to the display of the data:
  - View data results in a table
  - Time range selector
  - Refresh data button
- **The Main Area** will display the chart and should update in real time

> Note: Data should refresh automatically, but may require a refresh using the button in some cases

<a id="configuration-dashboards-grafanauserguide--2-query-builder"></a>

### 2. Query Builder

Here we form the SQL query to pull data into our chart, from our database

- Ensure the **Data Source** is the correct database

  ![Screen Shot 2021-08-06 at 10 14 22 AM](assets/images/128545278-be4846e0-852d-4bc8-8994-e99b79831d8c_248b6c143011af52.png)
- Select **Format as Table**, and **Edit SQL** buttons to write/edit queries as SQL

  ![Screen Shot 2021-08-06 at 10 17 52 AM](assets/images/128545197-a9ff9cb3-f12d-4331-bf6a-39035043667a_1131cfb78874574f.png)
- The **Main Area** is where the queries are written, and in the top right is the **Query Inspector** button (to inspect returned data)

  ![Screen Shot 2021-08-06 at 10 18 23 AM](assets/images/128545557-ead5312a-e835-4c59-b9ca-dd5c08f2a38b_0d345467daf2b99b.png)

<a id="configuration-dashboards-grafanauserguide--3-main-panel-toolbar"></a>

### 3. Main Panel Toolbar

In the top right of the window are buttons for:

- Dashboard settings (regarding entire dashboard)
- Save/apply changes (to specific panel)

<a id="configuration-dashboards-grafanauserguide--4-grafana-parameter-sidebar"></a>

### 4. Grafana Parameter Sidebar

- Change chart style (bar/line/pie chart etc)
- Edit legends, chart parameters
- Modify chart styling
- Other Grafana specific settings

<a id="configuration-dashboards-grafanauserguide--dashboard-settings"></a>

## Dashboard Settings

When viewing a dashboard click on the settings icon to view dashboard settings. Here are 2 important sections to use:

![Screen Shot 2021-08-06 at 1 51 14 PM](assets/images/128555763-4d0370c2-bd4d-4462-ae7e-4b140c4e8c34_c76a6e001ca12c36.png)

- Variables

  - Create variables to use throughout the dashboard panels, that are also built on SQL queries

  ![Screen Shot 2021-08-06 at 2 02 40 PM](assets/images/128553157-a8e33042-faba-4db4-97db-02a29036e27c_f1a4202865ce648b.png)
- JSON Model

  - Copy `json` code here and save it to a new file in `/grafana/dashboards/` with a unique name in the `lake` repo. This will allow us to persist dashboards when we load the app

  ![Screen Shot 2021-08-06 at 2 02 52 PM](assets/images/128553176-65a5ae43-742f-4abf-9c60-04722033339e_3b5935dd6e339c06.png)

<a id="configuration-dashboards-grafanauserguide--provisioning-a-dashboard"></a>

## Provisioning a Dashboard

To save a dashboard in the `lake` repo and load it:

1. Create a dashboard in browser (visit `/dashboard/new`, or use sidebar)
2. Save dashboard (in top right of screen)
3. Go to dashboard settings (in top right of screen)
4. Click on *JSON Model* in sidebar
5. Copy code into a new `.json` file in `/grafana/dashboards`

<a id="configuration-dashboards-grafanauserguide--troubleshooting-db-connection"></a>

## Troubleshooting DB Connection

To ensure we have properly connected our database to the data source in Grafana, check database settings in `./grafana/datasources/datasource.yml`, specifically:

- `database`
- `user`
- `secureJsonData/password`

<a id="configuration-dashboards-grafanauserguide--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the [Troubleshooting](#troubleshooting-dashboard) or [create an issue](https://github.com/apache/incubator-devlake/issues)

- [Contents](#configuration-dashboards-grafanauserguide--contents)
- [Logging In](#configuration-dashboards-grafanauserguide--logging-in)
- [Viewing All Dashboards](#configuration-dashboards-grafanauserguide--viewing-all-dashboards)
- [Importing a Dashboard](#configuration-dashboards-grafanauserguide--importing-a-dashboard)
- [Customizing a Dashboard](#configuration-dashboards-grafanauserguide--customizing-a-dashboard)
  - [1. Preview Area](#configuration-dashboards-grafanauserguide--1-preview-area)
  - [2. Query Builder](#configuration-dashboards-grafanauserguide--2-query-builder)
  - [3. Main Panel Toolbar](#configuration-dashboards-grafanauserguide--3-main-panel-toolbar)
  - [4. Grafana Parameter Sidebar](#configuration-dashboards-grafanauserguide--4-grafana-parameter-sidebar)
- [Dashboard Settings](#configuration-dashboards-grafanauserguide--dashboard-settings)
- [Provisioning a Dashboard](#configuration-dashboards-grafanauserguide--provisioning-a-dashboard)
- [Troubleshooting DB Connection](#configuration-dashboards-grafanauserguide--troubleshooting-db-connection)
- [Troubleshooting](#configuration-dashboards-grafanauserguide--troubleshooting)

---

<a id="dora"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DORA/ -->

<!-- page_index: 37 -->

# DORA

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DORA

This document describes everything you need to know about DORA, and implementing this powerful and practical framework in DevLake.

<a id="dora--what-are-dora-metrics"></a>

## What are DORA metrics?

Created six years ago by a team of researchers, DORA stands for "DevOps Research & Assessment" and is the answer to years of research, having examined thousands of teams, seeking a reliable and actionable approach to understanding the performance of software development teams.

DORA has since become a standardized framework focused on the stability and velocity of development processes, one that avoids the more controversial aspects of productivity and individual performance measures.

There are two key clusters of data inside DORA: Velocity and Stability. The DORA framework is focused on keeping them in context with each other, as a whole, rather than as independent variables, making the data more challenging to misinterpret or abuse.

Within velocity are two core metrics:

- [Deployment Frequency](#metrics-deploymentfrequency): Number of successful deployments to production, how rapidly is your team releasing to users?
- [Lead Time for Changes](#metrics-leadtimeforchanges): How long does it take from commit to the code running in production? This is important, as it reflects how quickly your team can respond to user requirements.

Stability is composed of two core metrics:

- [Change Failure Rate](#metrics-cfr): How often are your deployments causing a failure?
- [Median Time to Restore Service (MTTR)](#metrics-mttr): How long does it take the team to properly recover from a failure once it is identified?

However, MTTR is replaced by [Failed Deployment Recovery Time](#metrics-faileddeploymentrecoverytime) from the 2023 DORA report. This metric measures the finish time of a deployment to the resolution of the incident caused by the deployment.

![](assets/images/dora-intro-e3847646d8dbe47220e6c8347ab14f7b_1478a45adfb502b9.png)

To make DORA even more actionable, there are well-established benchmarks to determine if you are performing at "Elite", "High", "Medium", or "Low" levels. Inside DevLake, you will find the benchmarking table available to assess and compare your own projects.

<a id="dora--why-is-dora-important"></a>

## Why is DORA important?

DORA metrics help teams and projects measure and improve software development practices to consistently deliver reliable products, and thus happy users!

<a id="dora--how-to-implement-dora-metrics-with-apache-devlake"></a>

## How to implement DORA metrics with Apache DevLake?

DevLake measures DORA metrics at the [project level](#configuration-howtoorganizedevlakeprojects--2-why-is-it-important-to-organize-projects). You can set up DORA metrics in a few steps:

- **Install**: via [Docker Compose](#gettingstarted-dockercomposesetup) or [Helm](#gettingstarted-helmsetup).
- **Configure and collect data**:

  - Create [data connections](#overview-keyconcepts--data-connection) to retrieve the data from various tools such as Jira, GitHub, Jenkins, etc.
  - Configure the DORA-related [scope config](#overview-keyconcepts--scope-config) to define `deployments` and `incidents`.
  - Create a DevLake project, and associate the data connections with the project. Collect data to see DORA metrics
- **Report**: DevLake provides a built-in DORA dashboard and another dashboard to help you debug DORA. See an example screenshot below or check out our [live demo](https://grafana-lake.demo.devlake.io/grafana/d/qNo8_0M4z/dora?orgId=1).

  ![DORA Dashboard](assets/images/dora-dashboard-d0c06a27821366eb4fe8f0575b1501e1_11471e29e667ffce.png)

DevLake now supports Jenkins, GitHub Action, GitLab CI, BitBucket and Azure Pipelines as the data sources for `deployments`; Jira boards, GitHub issues, TAPD workspaces and Zentao issues as the sources for `incidents` data; Github/BitBucket/Azure/GitLab repos as the sources for `Pull Requests` and `Commits`.

If your CI/CD or incident management tools are not listed on the [Supported Data Sources](#overview-supporteddatasources) page, have no fear! DevLake provides incoming webhooks to push your `deployments` or `incidents` to DevLake. The webhook configuration doc can be found [here](#configuration-webhook).

<a id="dora--a-real-world-example"></a>

## A real-world example

Let us walk through the DORA implementation process for a [project team](#configuration-howtoorganizedevlakeprojects--43-measuring-dora-at-the-team-level) with the following toolchain

- Source Code Management and Code Review: GitHub
- Continous Deployments: GitHub Actions & CircleCI
- Incident management: Jira

Calculating DORA metrics requires three key entities: **Pull requests**, **deployments**, and **incidents**. Their exact definitions of course depend on a project's DevOps practice and vary project by project. For the project in this example, let us assume the following definition:

- Code Changes: All commits and pull requests in GitHub.
- Deployments: GitHub workflow run whose jobs contain "deploy" and "push-image" in their names and CircleCI deployments.
- Incidents: Jira issues whose type is "DORA Incident"

In the next section, we will demonstrate how to configure DevLake to implement DORA metrics for the aforementioned example project team.

<a id="dora--step-1-configure-github-jira-connections"></a>

### Step 1 - Configure GitHub & Jira connections

1.1 Visit the config-ui at `http://localhost:4000`.

1.2 Go to the **Connections** page. Create a Jira connection.

1.3 Add your project's Jira boards. Click the `Associate Scope Config` icon to configure for DORA metrics.

![](assets/images/dora-jira-connection-1-7b05f4818671ef5d65c895722fd1da26_c26b745dd76afad6.png)

To make it simple, fields with the ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAAAcCAYAAADC8vmmAAAMbWlDQ1BJQ0MgUHJvZmlsZQAASImVVwdYU8kWnluSkJCEEkBASuhNEKkBpITQAkgvgo2QBBJKjAlBxV4WFVy7iIANXRVRbCsgduzKotj7YkFFWRd1saHyJiSg677yvfN9c++fM2f+U+5M7j0AaH3gSaV5qDYA+ZICWUJ4MHN0WjqT9BQggAjoAAU4jy+XsuPiogGUgfvf5d0NaA3lqrOS65/z/1V0BUI5HwBkLMSZAjk/H+LjAOBVfKmsAACiUm81uUCqxLMh1pPBACFepcTZKrxdiTNV+HC/TVICB+LLAGhQeTxZNgD0e1DPLORnQx76Z4hdJQKxBACtYRAH8EU8AcTK2Ifl509U4nKI7aG9FGIYD2BlfseZ/Tf+zEF+Hi97EKvy6heNELFcmseb+n+W5n9Lfp5iwIctHFSRLCJBmT+s4a3ciVFKTIW4S5IZE6usNcQfxAJV3QFAKSJFRLLKHjXhyzmwfsAAYlcBLyQKYhOIwyR5MdFqfWaWOIwLMdwt6BRxATcJYkOIFwrloYlqm42yiQlqX2h9lozDVuvP8WT9fpW+Hihyk9lq/jciIVfNj9GLREmpEFMgti4Up8RATIfYRZ6bGKW2GVkk4sQM2MgUCcr4rSFOEErCg1X8WGGWLCxBbV+SLx/IF9soEnNj1HhfgSgpQlUf7BSf1x8/zAW7LJSwkwd4hPLR0QO5CIQhoarcsedCSXKimueDtCA4QbUWp0jz4tT2uKUwL1ypt4TYQ16YqF6LpxTAzanix7OkBXFJqjjxohxeZJwqHnwZiAYcEAKYQAFHJpgIcoC4tauhC/5SzYQBHpCBbCAEzmrNwIrU/hkJvCaCIvAHREIgH1wX3D8rBIVQ/2VQq7o6g6z+2cL+FbngKcT5IArkwd+K/lWSQW8p4AnUiP/hnQcHH8abB4dy/t/rB7TfNGyoiVZrFAMemVoDlsRQYggxghhGdMCN8QDcD4+G1yA43HAW7jOQxzd7wlNCG+ER4TqhnXB7gniu7IcoR4F2yB+mrkXm97XAbSGnJx6M+0N2yIwb4MbAGfeAfth4IPTsCbUcddzKqjB/4P5bBt89DbUd2ZWMkoeQg8j2P66kO9I9B1mUtf6+PqpYMwfrzRmc+dE/57vqC+A96kdLbCG2HzuLncDOY4exBsDEjmGNWAt2RIkHd9eT/t014C2hP55cyCP+hz+e2qeyknLXWtdO18+quQLhlALlweNMlE6VibNFBUw2fDsImVwJ32UY083VzQ0A5btG9ff1Nr7/HYIYtHzTzfsdAP9jfX19h77pIo8BsNcbHv+D33T2LAB0NAE4d5CvkBWqdLjyQoD/ElrwpBkBM2AF7GE+bsAL+IEgEAoiQSxIAmlgPKyyCO5zGZgMpoM5oBiUgmVgNagAG8BmsB3sAvtAAzgMToAz4CK4DK6Du3D3dICXoBu8A70IgpAQGsJAjBBzxAZxQtwQFhKAhCLRSAKShmQg2YgEUSDTkXlIKbICqUA2ITXIXuQgcgI5j7Qht5GHSCfyBvmEYigV1UNNUVt0OMpC2WgUmoSOQ7PRSWgROh9dgpaj1ehOtB49gV5Er6Pt6Eu0BwOYJmaAWWDOGAvjYLFYOpaFybCZWAlWhlVjdVgTfM5XsXasC/uIE3EGzsSd4Q6OwJNxPj4Jn4kvxivw7Xg9fgq/ij/Eu/GvBBrBhOBE8CVwCaMJ2YTJhGJCGWEr4QDhNDxLHYR3RCLRgGhH9IZnMY2YQ5xGXExcR9xNPE5sIz4m9pBIJCOSE8mfFEvikQpIxaS1pJ2kY6QrpA7SBw1NDXMNN40wjXQNicZcjTKNHRpHNa5oPNPoJWuTbci+5FiygDyVvJS8hdxEvkTuIPdSdCh2FH9KEiWHModSTqmjnKbco7zV1NS01PTRjNcUa87WLNfco3lO86HmR6ou1ZHKoY6lKqhLqNuox6m3qW9pNJotLYiWTiugLaHV0E7SHtA+0Bl0FzqXLqDPolfS6+lX6K+0yFo2Wmyt8VpFWmVa+7UuaXVpk7VttTnaPO2Z2pXaB7VvavfoMHRG6MTq5Oss1tmhc17nuS5J11Y3VFegO193s+5J3ccMjGHF4DD4jHmMLYzTjA49op6dHlcvR69Ub5deq163vq6+h36K/hT9Sv0j+u0GmIGtAdcgz2CpwT6DGwafhpgOYQ8RDlk0pG7IlSHvDYcaBhkKDUsMdxteN/xkxDQKNco1Wm7UYHTfGDd2NI43nmy83vi0cddQvaF+Q/lDS4buG3rHBDVxNEkwmWay2aTFpMfUzDTcVGq61vSkaZeZgVmQWY7ZKrOjZp3mDPMAc7H5KvNj5i+Y+kw2M49ZzjzF7LYwsYiwUFhssmi16LW0s0y2nGu52/K+FcWKZZVltcqq2arb2tx6lPV061rrOzZkG5aNyGaNzVmb97Z2tqm2C2wbbJ/bGdpx7Yrsau3u2dPsA+0n2VfbX3MgOrAcch3WOVx2RB09HUWOlY6XnFAnLyex0zqntmGEYT7DJMOqh910pjqznQuda50fuhi4RLvMdWlweTXcenj68OXDzw7/6urpmue6xfXuCN0RkSPmjmga8cbN0Y3vVul2zZ3mHuY+y73R/bWHk4fQY73HLU+G5yjPBZ7Nnl+8vL1kXnVend7W3hneVd43WXqsONZi1jkfgk+wzyyfwz4ffb18C3z3+f7p5+yX67fD7/lIu5HCkVtGPva39Of5b/JvD2AGZARsDGgPtAjkBVYHPgqyChIEbQ16xnZg57B3sl8FuwbLgg8Ev+f4cmZwjodgIeEhJSGtobqhyaEVoQ/CLMOyw2rDusM9w6eFH48gRERFLI+4yTXl8rk13O5I78gZkaeiqFGJURVRj6Ido2XRTaPQUZGjVo66F2MTI4lpiAWx3NiVsffj7OImxR2KJ8bHxVfGP00YkTA94WwiI3FC4o7Ed0nBSUuT7ibbJyuSm1O0Usam1KS8Tw1JXZHaPnr46BmjL6YZp4nTGtNJ6SnpW9N7xoSOWT2mY6zn2OKxN8bZjZsy7vx44/F5449M0JrAm7A/g5CRmrEj4zMvllfN68nkZlZldvM5/DX8l4IgwSpBp9BfuEL4LMs/a0XW82z/7JXZnaJAUZmoS8wRV4hf50TkbMh5nxubuy23Ly81b3e+Rn5G/kGJriRXcmqi2cQpE9ukTtJiafsk30mrJ3XLomRb5Yh8nLyxQA9+1Lco7BU/KR4WBhRWFn6YnDJ5/xSdKZIpLVMdpy6a+qworOiXafg0/rTm6RbT50x/OIM9Y9NMZGbmzOZZVrPmz+qYHT57+xzKnNw5v811nbti7l/zUuc1zTedP3v+45/Cf6otphfLim8u8FuwYSG+ULywdZH7orWLvpYISi6UupaWlX5ezF984ecRP5f/3Lcka0nrUq+l65cRl0mW3VgeuHz7Cp0VRSserxy1sn4Vc1XJqr9WT1h9vsyjbMMayhrFmvby6PLGtdZrl639XCGquF4ZXLm7yqRqUdX7dYJ1V9YHra/bYLqhdMOnjeKNtzaFb6qvtq0u20zcXLj56ZaULWd/Yf1Ss9V4a+nWL9sk29q3J2w/VeNdU7PDZMfSWrRWUdu5c+zOy7tCdjXWOddt2m2wu3QP2KPY82Jvxt4b+6L2Ne9n7a/71ebXqgOMAyX1SP3U+u4GUUN7Y1pj28HIg81Nfk0HDrkc2nbY4nDlEf0jS49Sjs4/2nes6FjPcenxrhPZJx43T2i+e3L0yWun4k+1no46fe5M2JmTZ9lnj53zP3f4vO/5gxdYFxouel2sb/FsOfCb528HWr1a6y95X2q87HO5qW1k29ErgVdOXA25euYa99rF6zHX224k37h1c+zN9luCW89v591+fafwTu/d2fcI90rua98ve2DyoPp3h993t3u1H3kY8rDlUeKju4/5j18+kT/53DH/Ke1p2TPzZzXP3Z4f7gzrvPxizIuOl9KXvV3Ff+j8UfXK/tWvfwb92dI9urvjtex135vFb43ebvvL46/mnrieB+/y3/W+L/lg9GH7R9bHs59SPz3rnfyZ9Ln8i8OXpq9RX+/15ff1SXkyXv+nAAYHmpUFwJttANDSAGDAvo0yRtUL9gui6l/7EfhPWNUv9osXAHXw+z2+C37d3ARgzxbYfkF+LdirxtEASPIBqLv74FCLPMvdTcVFhX0K4UFf31vYs5FWAvBlWV9fb3Vf35fNMFjYOx6XqHpQpRBhz7Ax9Etmfib4N6LqT7/L8cc7UEbgAX68/wuAmJCA1D8RWAAAADhlWElmTU0AKgAAAAgAAYdpAAQAAAABAAAAGgAAAAAAAqACAAQAAAABAAAASKADAAQAAAABAAAAHAAAAAB+ag3eAAAGE0lEQVRYCe1YeUyTZxj/tQXKVZBDBy2KB4dCOTwGC8wbkS1kziObukwz5sySadRt2T/zj8UlO7ItMcvmtjivoM6pi5k3c6go6A4QaAOCcsjNuJFLKi173q/tt36Wtp+kiWbpQ75+7/s8z3t8v/e5XiRDD0ZH+4ZG4aKxEZAO6cYWuLhGBKQjepf12DMGqT2hSwa4AHJgBU8MoJ4BHTr7HmD0KfdwNwcACsQFlc3YfixPwPN0d4NK4Y254ZOwMjkSEc9MEMgtO/cHdTiQp8WJW9XoMGUHPw83rIyfjjcXqzHJ39tSHQPDI1j02QkBTyaRIHrSBMSqgrA8fioSwicK5JadXlov/atTkEmAnPdXQeHpbikW1X4sgPSGUfQ91GN5pAqRIUYg2u8PobCuDfv+qsThorvY+/piJEWEWi2uGzFgR/ZVFDS0ITpQgZfip0HuJkV+VQsOFd7B3/dacWBzBvy9PfixzLrYenEE+sIoFcfXGwyoa+/DOe09/FRUhW/WLURqtJIfY9m4RDq9ww851mVtHVY8G2EpFtV+LIDMMy6LC0fmnOnmLvdu6urHluwr2HI0D/uz0qAOC+blBvrSncfzOXA+X/GcYKPbSKvgTjM2H76CdwnAPTRW7i70/LjQIGxZPpufjzWYe27af4ks+hpu7nwFbjLhGKZzprgGMcF+GKGDZe3xAGQ9K5t5HKQK9MW3G5ZA4eGOHUeEbnhJU4fT5fXYtkA95iZTo5TYlZnEAfjzjduiVg9SeGJtUhRZ2AgqW7qsxtR13MefjR3ITJjGPfn1bWjs7rfSc8RwGkBsIWWAD7Kej0FD35BgM9r6DsikEmRRnLFFq5MiofL1QinpiqUQfx9OtbVn0GrIBbIYRumJ05BBD6OLJh7XEfnjVIDYmtHKAG7p242d/Ba0TR2ImehPrmPfo9WhgdA0iwdI29DOrTGLArYlsdh1urQWKWETERbgiylBCswjndMltY+dNZ0OUGRIILfXcjJvRiN6AzSt3YilOOKIYlSBnPW19VpbhHks+3jmKsduVOC7gnLMVQZxlmuWs3fxvX9Q0zOAF0yWw3jM1e509UFTbwSV8cSQ/SMVM8MjOuwDGEnoj9EoMViQpuzskCQmJb15EtOIoyXVOKkxuoyOAq6ZmFXs2bjU3OXf527VwoNcOk0dzvOWxU3FrgtFOF9ca7c04AeYGk4H6C5ZC6NYUxZzd5MhISQAt5utA6lpD/yroqkLSl9PhE4wxhZeQI23UmZx3UGdHgeopGD0Q9Yy+MiFnzBMQftIcRUnP19iBJXr0A87KFZSvJc5Dx5UYogh4exiRjjQqWw2xp6Z5C5milMF4yBtbPihwSqFm3XYW9vSiUTlf+WBWbY+cQa2ZswxdxEerMBH5wtx/GYF3lik5vmscbW8ke9/fLGIb1s2rlc0Yql6iiXLZtupALHYsJ/iwmSFF1jaN1PslGDo6dSzr5dh05I4M1vwPnurhos/65OtARIoUmdNchSyCZzvab6X50UiwFfOq5ylTMUy5vUPVsObSg5L6n+gw4IvfsE5WkssQOLszHIVG+3m7gG8czAXg7oR7H5toUArg64EL0aF4cvLpbhAmeRRKqxpxYe//oEkiinrTK70qI5lnxWFW9MSuSp53xUtL+qgqj63ugWr1FMRSK7q6SETPMF+XlgRE47fq5rQ3T/Mj7PXGJcF5ZU3oLXHWHTVd/ajiIqwarIeL4o3P25YzMcf88JSOtFP1s5Hx77fsONkAQ5eK0NqpJLcTYaCu80opPg0g+LObrqmsI8SQ+nx4ZidX4Zsct1XU6Mxma4vOZTaWZzJoIxli1hmO1VWhxxNLdamzLSlxvPHBdCZigawh5G/3B2T/byRlRyNVVTs2bqssg//mirtvbkanKCsVEquyEhO1rCG7mVvpyVwp84xRfxIKeNtT5+DjYdysSenBJ+um48zZJ0hPnIkR4TYnCGFqvZgLw/SrREFkKSt2yJv2pzWuQJ2yu29Q3RHMiCELIfFjKeVnghATysYY+3LaUF6rMn/DzwXQA5O0QWQCyAHCDgQS93YP2xdZBMBKZUELrKDwL+tOQrZ+WcgbgAAAABJRU5ErkJggg==) label are DORA-related configurations for every data source. Via these fields, you can define what "incidents" and "deployments" are for each data source.

This project uses Jira issue type `DORA Incident` as "incident". Please select the `DORA Incident` for the `Incident` field. Jira issues belonging to this type will be converted to 'INCIDENT' in DevLake.

![](assets/images/dora-jira-connection-2-40732530bdc277cbdcf6fce462757bb7_f68cb619cebe7294.png)

1.4 Create a GitHub connection. Add the GitHub repositories. Once added, associate the scope configuration with the repositories.

In this project, the GitHub CI jobs 'deploy' and 'push-image' are recognized as deployments. To identify these deployments, please use the pattern '(?i)(deploy|push-image)'. GitHub Workflow runs that match this pattern will be transformed into 'deployments' and recorded in the table 'cicd\_deployments' in DevLake.

![](assets/images/dora-github-connection-1-6151fbcb441d0acd7bab8b9364e5564a_796a17406e2f5223.png)

Please note that starting from v0.20, DevLake automatically collects GitHub deployments and converts them into DevLake deployments by default.

<a id="dora--step-2-collect-circleci-deployments-via-webhook"></a>

### Step 2 - Collect CircleCI deployments via webhook

Using CircleCI as an example, we demonstrate how to actively push data to DevLake using the Webhook approach, in cases where DevLake does not have a plugin specific to that tool to pull data from your data source. Please note that CircleCI will be supported from v0.21.

2.1 Go to the **Connections** page. Add a webhook called 'CircleCI'.

2.2 Copy the curl command to register deployments to Devlake. This curl command includes a non-expired [API key](#configuration-apikeys) generated automatically.

![](assets/images/dora-webhook-1-cc0e2acaafc3ce36fcb4963c5f04a971_a0dfbf9af4331843.png)

2.3 Head to your CircleCI's pipelines page in a new tab. Find your deployment pipeline and click `Configuration File`.

![](assets/images/dora-circleci-screenshot-1-8e12b69a93c1106fa9cdfd4cf25102b7_3b81540e63b29574.png)

2.4 Paste the curl command to the `config.yml`. Change the key-values in the payload. See the full payload schema [here](#plugins-webhook--deployment).

```text
version: 2.1

jobs:
  build:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: "build"
          command: |
            echo Hello, World!

  deploy:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: "deploy"
          command: |
            # The time a deploy started
            start_time=`date '+%Y-%m-%dT%H:%M:%S%z'`

            # Some deployment tasks here ...
            echo Hello, World!

            # Send the request to DevLake after deploy
            # The values start with a '$CIRCLE_' are CircleCI's built-in variables
            curl http://127.0.0.1:4000/api/plugins/webhook/2/deployments -X 'POST' -d "{
              \"commit_sha\":\"$CIRCLE_SHA1\",
              \"repo_url\":\"$CIRCLE_REPOSITORY_URL\",
              \"start_time\":\"$start_time\"
            }"

workflows:
  build_and_deploy_workflow:
    jobs:
      - build
      - deploy
```

2.5 Run the CircleCI pipeline. Visit DevLake's DB to check if the deployments have been successfully pushed to DevLake. The deployments will appear in table [cicd\_deployments](#datamodels-devlakedomainlayerschema--cicd_deployments) and [cicd\_deployment\_commits](#datamodels-devlakedomainlayerschema--cicd_deployment_commits) in DevLake's database.

![](assets/images/dora-circleci-screenshot-2-43c262068235ddb25e8ff35a2e2638b9_99020baf3349108a.png)

![webhook-query](assets/images/webhook-query-deployments-c48f75ecf8c47f5175f0594fbefc9f7f_5a841f394a82f6f6.png)

<a id="dora--step-3-create-a-project-and-collect-data"></a>

### Step 3 - Create a project and collect data

Once all the data connections and webhooks have been configured, it is essential to associate them with a DevLake project. This association is necessary to accurately measure DORA metrics.

3.1 Go to the **Projects** page. Create 'project1' and enable DORA metrics.

![project1](assets/images/project1-58602175bfe30a91e7ce91d60049d4f1_e12bacce66d24bc2.png)

3.2 Add Jira and a GitHub connections to this project.

![](assets/images/dora-project-2-32ac2c0d302d31eb323b2de03358615e_e5713bfcd2056d43.png)

Choose the Jira boards and GitHub repos that belong to 'project1'.

![](assets/images/dora-project-3-82bfc86350e8484cfb6d5f8c95d0f62f_69b9cced7c257d6f.png)

3.3 Go to the **webhooks** tab. Add the existing webhook 'CircleCI' to this project.

![](assets/images/dora-webhook-2-fa7a0be3e246e5a8cc6dfae3294f1e82_3a26260451f608c7.png)

![](assets/images/dora-webhook-3-c868e69c28deca4d46fb44399ed239e9_cc7915754803ac5b.png)

3.4 Go to the **blueprint status** tab, click `Collect All` to start data collection.

<a id="dora--step-4-view-and-customize-devlakes-dora-dashboard"></a>

### Step 4 - View and customize DevLake's DORA dashboard

With all the data collected, DevLake's DORA dashboard is ready to deliver your DORA metrics and benchmarks.

Click the `Dashboards` on the top right corner. You can find the DORA dashboard within the Grafana instance shipped with DevLake, ready for you to put into action.

You can customize the DORA dashboard by editing the underlying SQL query of each panel.

For a breakdown of each metric's SQL query, please refer to the corresponding metric docs:

- [Deployment Frequency](#metrics-deploymentfrequency)
- [Lead Time for Changes](#metrics-leadtimeforchanges)
- [Median Time to Restore Service](#metrics-mttr)
- [Change Failure Rate](#metrics-cfr)

If you are not familiar with Grafana, please refer to our [Grafana doc](#configuration-dashboards-grafanauserguide), or jump into Slack for help.

🎉🎉🎉 Congratulations! You are now a DevOps Hero, with your own DORA dashboard!

<a id="dora--try-it-out"></a>

## Try it Out

To create the DORA dashboard with your own toolchain, please look at the [configuration tutorial](#configuration-tutorial) and [project organization documentation](#configuration-howtoorganizedevlakeprojects) for more details.

<a id="dora--troubleshooting"></a>

## Troubleshooting

If you run into any problem, please check the DORA debug dashboard, [DORA troubleshooting documentation](#troubleshooting-dashboard--debugging-dora-issue-metrics) or [create an issue](https://github.com/apache/incubator-devlake/issues) on GitHub.

- [What are DORA metrics?](#dora--what-are-dora-metrics)
- [Why is DORA important?](#dora--why-is-dora-important)
- [How to implement DORA metrics with Apache DevLake?](#dora--how-to-implement-dora-metrics-with-apache-devlake)
- [A real-world example](#dora--a-real-world-example)
  - [Step 1 - Configure GitHub & Jira connections](#dora--step-1-configure-github-jira-connections)
  - [Step 2 - Collect CircleCI deployments via webhook](#dora--step-2-collect-circleci-deployments-via-webhook)
  - [Step 3 - Create a project and collect data](#dora--step-3-create-a-project-and-collect-data)
  - [Step 4 - View and customize DevLake's DORA dashboard](#dora--step-4-view-and-customize-devlakes-dora-dashboard)
- [Try it Out](#dora--try-it-out)
- [Troubleshooting](#dora--troubleshooting)

---

<a id="metrics"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/ -->

<!-- page_index: 38 -->

# Metrics

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Metrics

[## 📄️ Requirement Count

Requirement Count](#metrics-requirementcount)

[## 📄️ Requirement Lead Time

Requirement Lead Time](#metrics-requirementleadtime)

[## 📄️ Requirement Delivery Rate

Requirement Delivery Rate](#metrics-requirementdeliveryrate)

[## 📄️ Requirement Granularity

Requirement Granularity](#metrics-requirementgranularity)

[## 📄️ Bug Age

Bug Age](#metrics-bugage)

[## 📄️ Bug Count per 1k Lines of Code

Bug Count per 1k Lines of Code](#metrics-bugcountper1klinesofcode)

[## 📄️ Incident Age

Incident Age](#metrics-incidentage)

[## 📄️ Incident Count per 1k Lines of Code

Incident Count per 1k Lines of Code](#metrics-incidentcountper1klinesofcode)

[## 📄️ Commit Count

Commit Count](#metrics-commitcount)

[## 📄️ Commit Author Count

Commit Author Count](#metrics-commitauthorcount)

[## 📄️ Added Lines of Code

Added Lines of Code](#metrics-addedlinesofcode)

[## 📄️ Deleted Lines of Code

Deleted Lines of Code](#metrics-deletedlinesofcode)

[## 📄️ PR Count

Pull Request Count](#metrics-prcount)

[## 📄️ PR Cycle Time

PR Cycle Time](#metrics-prcycletime)

[## 📄️ PR Coding Time

PR Coding Time](#metrics-prcodingtime)

[## 📄️ PR Pickup Time

PR Pickup Time](#metrics-prpickuptime)

[## 📄️ PR Review Time

PR Review Time](#metrics-prreviewtime)

[## 📄️ PR Deploy Time

PR Deploy Time](#metrics-prdeploytime)

[## 📄️ PR Time To Merge

PR Time To Merge](#metrics-prtimetomerge)

[## 📄️ PR Merge Rate

Pull Request Merge Rate](#metrics-prmergerate)

[## 📄️ PR Review Depth

PR Review Depth](#metrics-prreviewdepth)

[## 📄️ PR Size

PR Size](#metrics-prsize)

[## 📄️ Build Count

Build Count](#metrics-buildcount)

[## 📄️ Build Duration

Build Duration](#metrics-buildduration)

[## 📄️ Build Success Rate

Build Success Rate](#metrics-buildsuccessrate)

[## 📄️ DORA - Deployment Frequency

DORA - Deployment Frequency](#metrics-deploymentfrequency)

[## 📄️ DORA - Median Lead Time for Changes

DORA - Median Lead Time for Changes](#metrics-leadtimeforchanges)

[## 📄️ DORA - Failed Deployment Recovery Time

DORA - Failed Deployment Recovery Time](#metrics-faileddeploymentrecoverytime)

[## 📄️ DORA - Median Time to Restore Service

DORA - Median Time to Restore Service](#metrics-mttr)

[## 📄️ DORA - Change Failure Rate

DORA - Change Failure Rate](#metrics-cfr)

[## 📄️ Code Quality Issue Count

Code Quality Issue Count](#metrics-cqissuecount)

[## 📄️ Code Quality Test

Code Quality Test](#metrics-cqtest)

[## 📄️ Code Quality Maintainability-Debt

Code Quality Maintainability-Debt](#metrics-cqmaintainability-debt)

[## 📄️ Code Quality Duplicated Blocks

Code Quality Duplicated Blocks](#metrics-cqduplicatedblocks)

[## 📄️ Code Quality Duplicated Lines

Code Quality Duplicated Lines](#metrics-cqduplicatedlines)

---

<a id="metrics-requirementcount"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/RequirementCount/ -->

<!-- page_index: 39 -->

# Requirement Count

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Requirement Count

<a id="metrics-requirementcount--what-is-this-metric"></a>

## What is this metric?

The number of delivered requirements or features.

<a id="metrics-requirementcount--why-is-it-important"></a>

## Why is it important?

1. Based on historical data, establish a baseline of the delivery capacity of a single iteration to improve the organization and planning of R&D resources.
2. Evaluate whether the delivery capacity matches the business phase and demand scale. Identify key bottlenecks and reasonably allocate resources.

<a id="metrics-requirementcount--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jira](https://devlake.apache.org/livedemo/DataSources/Jira)
- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)

<a id="metrics-requirementcount--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the number of delivered issues in type "REQUIREMENT" in the given data range.

**Data Sources Required**

This metric relies on the `issues` collected from Jira, GitHub, or TAPD.

**Data Transformation Required**

This metric relies on the 'type-requirement' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `requirements`.

**SQL Queries**

The following SQL shows how to find the total count of requirements in specific boards, eg. 'board-1' and 'board-2'.

```text
select
  count(*) as "Requirement Count"
from issues i
  join board_issues bi on i.id = bi.issue_id
where
  i.type = 'REQUIREMENT'
  and i.status = 'DONE'
  -- please replace the board ids with your own, or create a '$board_id' variable in Grafana
  and bi.board_id in ('board-1','board-2')
  and $__timeFilter(i.created_date)
```

If you want to see the monthly trend of `requirement count` in the screenshot below, please run the following SQL

![](assets/images/requirement-count-monthly-7238fd8f30cdc7d56ee9a2a332d520d6_bd69b29ab15bb1d9.png)

```text
SELECT
  DATE_ADD(date(i.created_date), INTERVAL -DAYOFMONTH(date(i.created_date))+1 DAY) as time,
  count(distinct case when status != 'DONE' then i.id else null end) as "Number of Open Requirements",
  count(distinct case when status = 'DONE' then i.id else null end) as "Number of Delivered Requirements"
FROM issues i
    join board_issues bi on i.id = bi.issue_id
    join boards b on bi.board_id = b.id
where
  i.type = 'REQUIREMENT'
  and $__timeFilter(i.created_date)
  -- please replace the board ids with your own, or create a '$board_id' variable in Grafana
  and bi.board_id in ($board_id)
group by 1
```

<a id="metrics-requirementcount--how-to-improve"></a>

## How to improve?

1. Analyze the number of requirements and delivery rate of different time cycles to find the stability and trend of the development process.
2. Analyze and compare the number of requirements delivered and delivery rate of each project/team, and compare the scale of requirements of different projects.
3. Based on historical data, establish a baseline of the delivery capacity of a single iteration (optimistic, probable and pessimistic values) to provide a reference for iteration estimation.
4. Drill down to analyze the number and percentage of requirements in different phases of SDLC. Analyze rationality and identify the requirements stuck in the backlog.

- [What is this metric?](#metrics-requirementcount--what-is-this-metric)
- [Why is it important?](#metrics-requirementcount--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-requirementcount--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-requirementcount--how-is-it-calculated)
- [How to improve?](#metrics-requirementcount--how-to-improve)

---

<a id="metrics-requirementleadtime"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/RequirementLeadTime/ -->

<!-- page_index: 40 -->

# Requirement Lead Time

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Requirement Lead Time

<a id="metrics-requirementleadtime--what-is-this-metric"></a>

## What is this metric?

The amount of time it takes a requirement to deliver.

<a id="metrics-requirementleadtime--why-is-it-important"></a>

## Why is it important?

1. Analyze key projects and critical points, identify good/to-be-improved practices that affect requirement lead time, and reduce the risk of delays
2. Focus on the end-to-end velocity of value delivery process; coordinate different parts of R&D to avoid efficiency shafts; make targeted improvements to bottlenecks.

<a id="metrics-requirementleadtime--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jira](https://devlake.apache.org/livedemo/DataSources/Jira)
- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)
- [Community Experience](https://devlake.apache.org/livedemo/OSSMaintainers/CommunityExperience)

<a id="metrics-requirementleadtime--how-is-it-calculated"></a>

## How is it calculated?

This metric equals `resolution_date - created_date` of issues in type "REQUIREMENT".

**Data Sources Required**

This metric relies on issues collected from Jira, GitHub, or TAPD.

**Data Transformation Required**

This metric relies on the 'type-requirement' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `requirements`.

**SQL Queries**

The following SQL shows how to find the lead time of a specific `requirement`.

```text
-- lead_time_minutes is a pre-calculated field whose value equals 'resolution_date - created_date'
SELECT
  lead_time_minutes/1440 as requirement_lead_time_in_days
FROM
  issues
WHERE
  type = 'REQUIREMENT'
```

If you want to measure the `mean requirement lead time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/requirement-lead-time-monthly-297def3418d5bf1a6caf63114552aba4_b55ef3c43af05f19.png)

```text
with _issues as(
  SELECT
    DATE_ADD(date(i.resolution_date), INTERVAL -DAY(date(i.resolution_date))+1 DAY) as time,
    AVG(i.lead_time_minutes/1440) as issue_lead_time
  FROM issues i
    join board_issues bi on i.id = bi.issue_id
    join boards b on bi.board_id = b.id
  WHERE
    -- $board_id is a variable defined in Grafana's dashboard settings to filter out issues by boards
    b.id in ($board_id)
    and i.type = 'REQUIREMENT'
    and i.status = "DONE"
    and $__timeFilter(i.resolution_date)
    -- the following condition will remove the month with incomplete data
    and i.resolution_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  group by 1
)

SELECT
  date_format(time,'%M %Y') as month,
  issue_lead_time as "Mean Requirement Lead Time in Days"
FROM _issues
ORDER BY time
```

<a id="metrics-requirementleadtime--how-to-improve"></a>

## How to improve?

1. Analyze the trend of requirement lead time to observe if it has improved over time.
2. Compare the requirement lead time of each project/team to identify key projects with abnormal lead time.
3. Drill down to analyze a requirement's staying time in different phases of SDLC. Analyze the bottleneck of delivery velocity and improve the workflow.

- [What is this metric?](#metrics-requirementleadtime--what-is-this-metric)
- [Why is it important?](#metrics-requirementleadtime--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-requirementleadtime--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-requirementleadtime--how-is-it-calculated)
- [How to improve?](#metrics-requirementleadtime--how-to-improve)

---

<a id="metrics-requirementdeliveryrate"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/RequirementDeliveryRate/ -->

<!-- page_index: 41 -->

# Requirement Delivery Rate

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Requirement Delivery Rate

<a id="metrics-requirementdeliveryrate--what-is-this-metric"></a>

## What is this metric?

The ratio of delivered requirements to all requirements.

<a id="metrics-requirementdeliveryrate--why-is-it-important"></a>

## Why is it important?

1. Based on historical data, establish a baseline of the delivery capacity of a single iteration to improve the organization and planning of R&D resources.
2. Evaluate whether the delivery capacity matches the business phase and demand scale. Identify key bottlenecks and reasonably allocate resources.

<a id="metrics-requirementdeliveryrate--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jira](https://devlake.apache.org/livedemo/DataSources/Jira)
- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)

<a id="metrics-requirementdeliveryrate--how-is-it-calculated"></a>

## How is it calculated?

The number of delivered requirements divided by the total number of requirements in the given data range.

**Data Sources Required**

This metric relies on the `issues` collected from Jira, GitHub, or TAPD.

**Data Transformation Required**

This metric relies on the 'type-requirement' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `requirements`.

**SQL Queries**

The following SQL shows how to find the `requirement delivery rate` in specific boards, eg. 'board-1' and 'board-2'.

![](assets/images/requirement-delivery-rate-text-7e0e63ca119372141eb7183731314b61_06ad46111c4baf56.png)

```text
WITH _requirements as(
  SELECT
    count(distinct i.id) as total_count,
    count(distinct case when i.status = 'DONE' then i.id else null end) as delivered_count
  FROM issues i
    join board_issues bi on i.id = bi.issue_id
  WHERE
    i.type = 'REQUIREMENT'
    and $__timeFilter(i.created_date)
    -- please replace the board ids with your own, or create a '$board_id' variable in Grafana
    and bi.board_id in ('board_1', 'board_2')
)

SELECT
  now() as time,
  1.0 * delivered_count/total_count as requirement_delivery_rate
FROM _requirements
```

If you want to measure the monthly trend of `requirement delivery rate` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/requirement-delivery-rate-monthly-73541cc01c85985615cf5acfb15ae2ac_1100d64585b25682.png)

```text
WITH _requirements as(
  SELECT
    DATE_ADD(date(i.created_date), INTERVAL -DAYOFMONTH(date(i.created_date))+1 DAY) as time,
    1.0 * count(distinct case when i.status = 'DONE' then i.id else null end)/count(distinct i.id) as delivered_rate
  FROM issues i
    join board_issues bi on i.id = bi.issue_id
  WHERE
     i.type = 'REQUIREMENT'
    and $__timeFilter(i.created_date)
    -- please replace the board ids with your own, or create a '$board_id' variable in Grafana
    and bi.board_id in ($board_id)
  GROUP BY 1
)

SELECT
  time,
  delivered_rate
FROM _requirements
ORDER BY time
```

<a id="metrics-requirementdeliveryrate--how-to-improve"></a>

## How to improve?

1. Analyze the number of requirements and delivery rate of different time cycles to find the stability and trend of the development process.
2. Analyze and compare the number of requirements delivered and delivery rate of each project/team, and compare the scale of requirements of different projects.
3. Based on historical data, establish a baseline of the delivery capacity of a single iteration (optimistic, probable and pessimistic values) to provide a reference for iteration estimation.
4. Drill down to analyze the number and percentage of requirements in different phases of SDLC. Analyze rationality and identify the requirements stuck in the backlog.

- [What is this metric?](#metrics-requirementdeliveryrate--what-is-this-metric)
- [Why is it important?](#metrics-requirementdeliveryrate--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-requirementdeliveryrate--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-requirementdeliveryrate--how-is-it-calculated)
- [How to improve?](#metrics-requirementdeliveryrate--how-to-improve)

---

<a id="metrics-requirementgranularity"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/RequirementGranularity/ -->

<!-- page_index: 42 -->

# Requirement Granularity

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Requirement Granularity

<a id="metrics-requirementgranularity--what-is-this-metric"></a>

## What is this metric?

The average number of story points per requirement.

<a id="metrics-requirementgranularity--why-is-it-important"></a>

## Why is it important?

1. Promote product teams to split requirements carefully, improve requirements quality, help developers understand requirements clearly, deliver efficiently and with high quality, and improve the project management capability of the team.
2. Establish a data-supported workload estimation model to help R&D teams calibrate their estimation methods and more accurately assess the granularity of requirements, which is useful to achieve better issue planning in project management.

<a id="metrics-requirementgranularity--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jira](https://devlake.apache.org/livedemo/DataSources/Jira)
- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)

<a id="metrics-requirementgranularity--how-is-it-calculated"></a>

## How is it calculated?

The average story points of issues in type "REQUIREMENT" in the given data range.

**Data Sources Required**

This metric relies on `issues` collected from Jira, GitHub, or TAPD.

**Data Transformation Required**

This metric relies on the 'type-requirement' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `requirements`.

Besides, if you are importing Jira issues, you also need to configure the field of 'story\_points' in the transformation.

<a id="metrics-requirementgranularity--how-to-improve"></a>

## How to improve?

1. Analyze the story points/requirement lead time of requirements to evaluate whether the ticket size, ie. requirement complexity is optimal.
2. Compare the estimated requirement granularity with the actual situation and evaluate whether the difference is reasonable by combining more microscopic workload metrics (e.g. lines of code/code equivalents)

- [What is this metric?](#metrics-requirementgranularity--what-is-this-metric)
- [Why is it important?](#metrics-requirementgranularity--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-requirementgranularity--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-requirementgranularity--how-is-it-calculated)
- [How to improve?](#metrics-requirementgranularity--how-to-improve)

---

<a id="metrics-bugage"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/BugAge/ -->

<!-- page_index: 43 -->

# Bug Age

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Bug Age

<a id="metrics-bugage--what-is-this-metric"></a>

## What is this metric?

The amount of time it takes a bug to fix.

<a id="metrics-bugage--why-is-it-important"></a>

## Why is it important?

1. Help the team to establish an effective hierarchical response mechanism for bugs. Focus on the resolution of important problems in the backlog.
2. Improve team's and individual's bug fixing efficiency. Identify good/to-be-improved practices that affect bug age age

<a id="metrics-bugage--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jira](https://devlake.apache.org/livedemo/DataSources/Jira)
- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)
- [Weekly Bug Retro](https://devlake.apache.org/livedemo/EngineeringLeads/WeeklyBugRetro)

<a id="metrics-bugage--how-is-it-calculated"></a>

## How is it calculated?

Similar to [requirement lead time](#metrics-requirementleadtime), this metric equals `resolution_date - created_date` of issues in type "BUG".

**Data Sources Required**

This metric relies on `issues` collected from Jira, GitHub, or TAPD.

**Data Transformation Required**

This metric relies on the 'type-bug' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `bugs`.

**SQL Queries**

The following SQL shows how to find the bug age of a specific `bug`.

```text
-- lead_time_minutes is a pre-calculated field whose value equals 'resolution_date - created_date'
SELECT
  lead_time_minutes/1440 as bug_age_in_days
FROM
  issues
WHERE
  type = 'BUG'
```

If you want to measure the `mean bug age` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/bug-age-monthly-4463714643145a716df6de60a6b7005c_c1444ffd4aa0fc65.png)

```text
with _bugs as(
  SELECT
    DATE_ADD(date(i.resolution_date), INTERVAL -DAY(date(i.resolution_date))+1 DAY) as time,
    AVG(i.lead_time_minutes/1440) as issue_lead_time
  FROM issues i
    join board_issues bi on i.id = bi.issue_id
    join boards b on bi.board_id = b.id
  WHERE
    -- $board_id is a variable defined in Grafana's dashboard settings to filter out issues by boards
    b.id in ($board_id)
    and i.status = "DONE"
    and i.type = 'BUG'
    and $__timeFilter(i.resolution_date)
    -- the following condition will remove the month with incomplete data
    and i.resolution_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  group by 1
)

SELECT
  date_format(time,'%M %Y') as month,
  issue_lead_time as "Mean Bug Age in Days"
FROM _bugs
ORDER BY time
```

<a id="metrics-bugage--how-to-improve"></a>

## How to improve?

1. Observe the trend of bug age and locate the key reasons.
2. Compare the age of bugs by severity levels, types (business, functional classification), affected components, etc.

- [What is this metric?](#metrics-bugage--what-is-this-metric)
- [Why is it important?](#metrics-bugage--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-bugage--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-bugage--how-is-it-calculated)
- [How to improve?](#metrics-bugage--how-to-improve)

---

<a id="metrics-bugcountper1klinesofcode"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/BugCountPer1kLinesOfCode/ -->

<!-- page_index: 44 -->

# Bug Count per 1k Lines of Code

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Bug Count per 1k Lines of Code

<a id="metrics-bugcountper1klinesofcode--what-is-this-metric"></a>

## What is this metric?

Amount of bugs per 1,000 lines of code.

<a id="metrics-bugcountper1klinesofcode--why-is-it-important"></a>

## Why is it important?

1. Defect drill-down analysis to inform the development of design and code review strategies and to improve the internal QA process
2. Assist teams to locate projects/modules with higher defect severity and density, and clean up technical debts
3. Identify good/to-be-improved practices that affect defect count or defect rate, to reduce the number of future defects

<a id="metrics-bugcountper1klinesofcode--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

N/A

<a id="metrics-bugcountper1klinesofcode--how-is-it-calculated"></a>

## How is it calculated?

The number of bugs divided by the total accumulated lines of code (additions + deletions) in the given data range.

**Data sources required**

- `issues` collected from Jira, GitHub or TAPD.
- `commits` collected from GitHub, GitLab or BitBucket.

**Data Transformation Required**

This metric relies on the 'type-bug' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `bugs`.

**SQL Queries**

If you want to measure the monthly trend of `Bugs per 1k lines of code` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/bug-per-1k-loc-monthly-fe582edc7ad50e884d69cb3a0dc63d7a_47566135b6e7b1a6.png)

```text
with _line_of_code as (
    select
      DATE_ADD(date(authored_date), INTERVAL -DAY(date(authored_date))+1 DAY) as time,
      sum(additions + deletions) as line_count
    from
      commits
    where
      message not like 'Merge%'
      and $__timeFilter(authored_date)
    group by 1
),


_bug_count as(
  select
    DATE_ADD(date(created_date), INTERVAL -DAY(date(created_date))+1 DAY) as time,
    count(*) as bug_count
  from issues i
  where
    type = 'Bug'
    and $__timeFilter(created_date)
  group by 1
),


_bug_count_per_1k_loc as(
  select
    loc.time,
    1.0 * bc.bug_count / loc.line_count * 1000 as bug_count_per_1k_loc
  from
    _line_of_code loc
    left join _bug_count bc on bc.time = loc.time
  where
    bc.bug_count is not null
    and loc.line_count is not null
    and loc.line_count != 0
)

select
  date_format(time,'%M %Y') as month,
  bug_count_per_1k_loc as 'Bug Count per 1000 Lines of Code'
from _bug_count_per_1k_loc
order by time;
```

<a id="metrics-bugcountper1klinesofcode--how-to-improve"></a>

## How to improve?

1. From the project or team dimension, observe the statistics on the total number of defects, the distribution of the number of defects in each severity level/type/owner, the cumulative trend of defects, and the change trend of the defect rate in thousands of lines, etc.
2. From version cycle dimension, observe the statistics on the cumulative trend of the number of defects/defect rate, which can be used to determine whether the growth rate of defects is slowing down, showing a flat convergence trend, and is an important reference for judging the stability of software version quality
3. From the time dimension, analyze the trend of the number of test defects, defect rate to locate the key items/key points
4. Evaluate whether the software quality and test plan are reasonable by referring to CMMI standard values

- [What is this metric?](#metrics-bugcountper1klinesofcode--what-is-this-metric)
- [Why is it important?](#metrics-bugcountper1klinesofcode--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-bugcountper1klinesofcode--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-bugcountper1klinesofcode--how-is-it-calculated)
- [How to improve?](#metrics-bugcountper1klinesofcode--how-to-improve)

---

<a id="metrics-incidentage"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/IncidentAge/ -->

<!-- page_index: 45 -->

# Incident Age

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Incident Age

<a id="metrics-incidentage--what-is-this-metric"></a>

## What is this metric?

The amount of time it takes an incident to fix.

<a id="metrics-incidentage--why-is-it-important"></a>

## Why is it important?

1. Help the team to establish an effective hierarchical response mechanism for incidents. Focus on the resolution of important problems in the backlog.
2. Improve team's and individual's incident fixing efficiency. Identify good/to-be-improved practices that affect incident age

<a id="metrics-incidentage--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jira](https://devlake.apache.org/livedemo/DataSources/Jira)
- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)

<a id="metrics-incidentage--how-is-it-calculated"></a>

## How is it calculated?

Similar to [requirement lead time](#metrics-requirementleadtime), this metric equals `resolution_date - created_date` of issues in type "INCIDENT".

**Data Sources Required**

This metric relies on `issues` collected from Jira, GitHub, TAPD, or PagerDuty.

**Transformation Rules Required**

This metric relies on the 'type-incident' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `incidents`.

**SQL Queries**

The following SQL shows how to find the incident age of a specific `incident`.

```text
-- lead_time_minutes is a pre-calculated field whose value equals 'resolution_date - created_date'
SELECT
  lead_time_minutes/1440 as incident_age_in_days
FROM
  issues
WHERE
  type = 'INCIDENT'
```

If you want to measure the `mean incident age` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/incident-age-monthly-98ad510805ed2538c125c7eba2f1aed7_73563121fde1ec68.png)

```text
with _incidents as(
  SELECT
    DATE_ADD(date(i.resolution_date), INTERVAL -DAY(date(i.resolution_date))+1 DAY) as time,
    AVG(i.lead_time_minutes/1440) as issue_lead_time
  FROM issues i
    join board_issues bi on i.id = bi.issue_id
    join boards b on bi.board_id = b.id
  WHERE
    -- $board_id is a variable defined in Grafana's dashboard settings to filter out issues by boards
    b.id in ($board_id)
    and i.status = "DONE"
    and i.type = 'INCIDENT'
    and $__timeFilter(i.resolution_date)
    -- the following condition will remove the month with incomplete data
    and i.resolution_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  group by 1
)

SELECT
  date_format(time,'%M %Y') as month,
  issue_lead_time as "Mean Incident Age in Days"
FROM _incidents
ORDER BY time
```

<a id="metrics-incidentage--how-to-improve"></a>

## How to improve?

1. Observe the trend of incident age and locate the key reasons.
2. Compare the age of incidents by severity levels, types (business, functional classification), affected components, etc.

- [What is this metric?](#metrics-incidentage--what-is-this-metric)
- [Why is it important?](#metrics-incidentage--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-incidentage--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-incidentage--how-is-it-calculated)
- [How to improve?](#metrics-incidentage--how-to-improve)

---

<a id="metrics-incidentcountper1klinesofcode"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/IncidentCountPer1kLinesOfCode/ -->

<!-- page_index: 46 -->

# Incident Count per 1k Lines of Code

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Incident Count per 1k Lines of Code

<a id="metrics-incidentcountper1klinesofcode--what-is-this-metric"></a>

## What is this metric?

Amount of incidents per 1,000 lines of code.

<a id="metrics-incidentcountper1klinesofcode--why-is-it-important"></a>

## Why is it important?

1. Defect drill-down analysis to inform the development of design and code review strategies and to improve the internal QA process
2. Assist teams to locate projects/modules with higher defect severity and density, and clean up technical debts
3. Identify good/to-be-improved practices that affect defect count or defect rate, to reduce the number of future defects

<a id="metrics-incidentcountper1klinesofcode--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

N/A

<a id="metrics-incidentcountper1klinesofcode--how-is-it-calculated"></a>

## How is it calculated?

The number of incidents divided by total accumulated lines of code (additions + deletions) in the given data range.

**Data Sources Required**

- `issues` collected from Jira, GitHub, TAPD or PagerDuty.
- `commits` collected from GitHub, GitLab or BitBucket.

**Data Transformation Required**

This metric relies on the 'type-incident' configuration in Jira, GitHub or TAPD's transformation rules while adding/editing a blueprint. This configuration tells DevLake what issues are `incidents`.

**SQL Queries**

If you want to measure the monthly trend of `Incidents per 1k lines of code` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/incident-per-1k-loc-monthly-3f15dae97c9f58e7affd9c37ac84bc7c_528c900acc80cf4d.png)

```text
with _line_of_code as (
    select
      DATE_ADD(date(authored_date), INTERVAL -DAY(date(authored_date))+1 DAY) as time,
      sum(additions + deletions) as line_count
    from
      commits
    where
      message not like 'Merge%'
      and $__timeFilter(authored_date)
    group by 1
),


_incident_count as(
  select
    DATE_ADD(date(created_date), INTERVAL -DAY(date(created_date))+1 DAY) as time,
    count(*) as incident_count
  from issues i
  where
    type = 'INCIDENT'
    and $__timeFilter(created_date)
  group by 1
),


_incident_count_per_1k_loc as(
  select
    loc.time,
    1.0 * ic.incident_count / loc.line_count * 1000 as incident_count_per_1k_loc
  from
    _line_of_code loc
    left join _incident_count ic on ic.time = loc.time
  where
    ic.incident_count is not null
    and loc.line_count is not null
    and loc.line_count != 0
)

select
  date_format(time,'%M %Y') as month,
  incident_count_per_1k_loc as 'Incident Count per 1000 Lines of Code'
from _incident_count_per_1k_loc
order by time;
```

<a id="metrics-incidentcountper1klinesofcode--how-to-improve"></a>

## How to improve?

1. From the project or team dimension, observe the statistics on the total number of defects, the distribution of the number of defects in each severity level/type/owner, the cumulative trend of defects, and the change trend of the defect rate in thousands of lines, etc.
2. From version cycle dimension, observe the statistics on the cumulative trend of the number of defects/defect rate, which can be used to determine whether the growth rate of defects is slowing down, showing a flat convergence trend, and is an important reference for judging the stability of software version quality
3. From the time dimension, analyze the trend of the number of test defects, defect rate to locate the key items/key points
4. Evaluate whether the software quality and test plan are reasonable by referring to CMMI standard values

- [What is this metric?](#metrics-incidentcountper1klinesofcode--what-is-this-metric)
- [Why is it important?](#metrics-incidentcountper1klinesofcode--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-incidentcountper1klinesofcode--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-incidentcountper1klinesofcode--how-is-it-calculated)
- [How to improve?](#metrics-incidentcountper1klinesofcode--how-to-improve)

---

<a id="metrics-commitcount"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CommitCount/ -->

<!-- page_index: 47 -->

# Commit Count

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Commit Count

<a id="metrics-commitcount--what-is-this-metric"></a>

## What is this metric?

The number of commits created.

<a id="metrics-commitcount--why-is-it-important"></a>

## Why is it important?

1. Identify potential bottlenecks that may affect output
2. Encourage R&D practices of small step submissions and develop excellent coding habits

<a id="metrics-commitcount--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- GitHub Release Quality and Contribution Analysis
- Demo-Is this month more productive than last?
- Demo-Commit Count by Author

<a id="metrics-commitcount--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the number of commits in the given data range.

**Data Sources Required**

This metric relies on commits collected from GitHub, GitLab or BitBucket.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find commits in specific repositories, eg. 'repo-1' and 'repo-2'.

```text
SELECT
  r.id,
  c.*
FROM
  commits c
  LEFT JOIN repo_commits rc ON c.sha = rc.commit_sha
  LEFT JOIN repos r ON r.id = rc.repo_id
WHERE
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
  r.id in ('repo-1','repo-2')
  and message not like '%Merge%'
  and $__timeFilter(c.authored_date)
  -- the following condition will remove the month with incomplete data
  and c.authored_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
```

If you want to measure the monthly trend of `commit count` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/commit-count-monthly-e307246386b3d297c10ce0f16a9fc3f3_f6762f35b5b3adec.png)

```text
with _commits as(
  SELECT
    DATE_ADD(date(c.authored_date), INTERVAL -DAY(date(c.authored_date))+1 DAY) as time,
    count(c.sha) as commit_count
  FROM
    commits c
    LEFT JOIN repo_commits rc ON c.sha = rc.commit_sha
    LEFT JOIN repos r ON r.id = rc.repo_id
  WHERE
    -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
    r.id in ($repo_id)
    and message not like '%Merge%'
    and $__timeFilter(c.authored_date)
    -- the following condition will remove the month with incomplete data
    and c.authored_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  group by 1
)

SELECT
  date_format(time,'%M %Y') as month,
  commit_count as "Commit Count"
FROM _commits
ORDER BY time
```

<a id="metrics-commitcount--how-to-improve"></a>

## How to improve?

1. Identify the main reasons for the unusual number of commits and the possible impact on the number of commits through comparison
2. Evaluate whether the number of commits is reasonable in conjunction with more microscopic workload metrics (e.g. lines of code/code equivalents)

- [What is this metric?](#metrics-commitcount--what-is-this-metric)
- [Why is it important?](#metrics-commitcount--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-commitcount--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-commitcount--how-is-it-calculated)
- [How to improve?](#metrics-commitcount--how-to-improve)

---

<a id="metrics-commitauthorcount"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CommitAuthorCount/ -->

<!-- page_index: 48 -->

# Commit Author Count

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Commit Author Count

<a id="metrics-commitauthorcount--what-is-this-metric"></a>

## What is this metric?

The number of commit authors who have committed code.

<a id="metrics-commitauthorcount--why-is-it-important"></a>

## Why is it important?

Take inventory of project/team R&D resource inputs, assess input-output ratio, and rationalize resource deployment.

<a id="metrics-commitauthorcount--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

N/A

<a id="metrics-commitauthorcount--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the number of commit authors in the given data range.

**Data Sources Required**

This metric relies on commits collected from GitHub, GitLab or BitBucket.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the `commit author count` in specific repositories, eg. 'repo-1' and 'repo-2'.

```text
SELECT
  count(distinct c.author_id)
FROM
  commits c
  LEFT JOIN repo_commits rc ON c.sha = rc.commit_sha
  LEFT JOIN repos r ON r.id = rc.repo_id
WHERE
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
  r.id in ('repo-1', 'repo-2')
  and message not like '%Merge%'
  and $__timeFilter(c.authored_date)
  -- the following condition will remove the month with incomplete data
  and c.authored_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
```

<a id="metrics-commitauthorcount--how-to-improve"></a>

## How to improve?

As a secondary indicator, this helps assess the labor cost of participating in coding.

- [What is this metric?](#metrics-commitauthorcount--what-is-this-metric)
- [Why is it important?](#metrics-commitauthorcount--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-commitauthorcount--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-commitauthorcount--how-is-it-calculated)
- [How to improve?](#metrics-commitauthorcount--how-to-improve)

---

<a id="metrics-addedlinesofcode"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/AddedLinesOfCode/ -->

<!-- page_index: 49 -->

# Added Lines of Code

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Added Lines of Code

<a id="metrics-addedlinesofcode--what-is-this-metric"></a>

## What is this metric?

The accumulated number of added lines of code.

<a id="metrics-addedlinesofcode--why-is-it-important"></a>

## Why is it important?

1. identify potential bottlenecks that may affect the output
2. Encourage the team to implement a development model that matches the business requirements; develop excellent coding habits

<a id="metrics-addedlinesofcode--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

N/A

<a id="metrics-addedlinesofcode--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by summing the additions of commits in the given data range.

**Data Sources Required**

This metric relies on `commits` collected from GitHub, GitLab or BitBucket.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the added lines of code in specific repositories, eg. 'repo-1' and 'repo-2'.

```text
SELECT
  sum(c.additions) as added_lines_of_code
FROM
  commits c
  LEFT JOIN repo_commits rc ON c.sha = rc.commit_sha
  LEFT JOIN repos r ON r.id = rc.repo_id
WHERE
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
  r.id in ('repo-1','repo-2')
  and message not like '%Merge%'
  and $__timeFilter(c.authored_date)
  -- the following condition will remove the month with incomplete data
  and c.authored_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
```

If you want to measure the monthly trend of `added lines of code` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/added-loc-monthly-4a65e11c8e2ee438edc4e7ece3b08366_009cd82402567016.png)

```text
WITH _commits as(
  SELECT
    DATE_ADD(date(authored_date), INTERVAL -DAY(date(authored_date))+1 DAY) as time,
    sum(additions) as added_lines_of_code
  FROM commits
  WHERE
    message not like '%Merge%'
    and $__timeFilter(authored_date)
    -- the following condition will remove the month with incomplete data
    and authored_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  group by 1
)

SELECT
  date_format(time,'%M %Y') as month,
  added_lines_of_code
FROM _commits
ORDER BY time
```

<a id="metrics-addedlinesofcode--how-to-improve"></a>

## How to improve?

1. From the project/team dimension, observe the accumulated change in added lines to assess the team activity and code growth rate
2. From version cycle dimension, observe the active time distribution of code changes, and evaluate the effectiveness of project development model.
3. From the member dimension, observe the trend and stability of code output of each member, and identify the key points that affect code output by comparison.

- [What is this metric?](#metrics-addedlinesofcode--what-is-this-metric)
- [Why is it important?](#metrics-addedlinesofcode--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-addedlinesofcode--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-addedlinesofcode--how-is-it-calculated)
- [How to improve?](#metrics-addedlinesofcode--how-to-improve)

---

<a id="metrics-deletedlinesofcode"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/DeletedLinesOfCode/ -->

<!-- page_index: 50 -->

# Deleted Lines of Code

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Deleted Lines of Code

<a id="metrics-deletedlinesofcode--what-is-this-metric"></a>

## What is this metric?

The accumulated number of deleted lines of code.

<a id="metrics-deletedlinesofcode--why-is-it-important"></a>

## Why is it important?

1. identify potential bottlenecks that may affect the output
2. Encourage the team to implement a development model that matches the business requirements; develop excellent coding habits

<a id="metrics-deletedlinesofcode--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

N/A

<a id="metrics-deletedlinesofcode--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by summing the deletions of commits in the given data range.

**Data Sources Required**

This metric relies on `commits` collected from GitHub, GitLab or BitBucket.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the `deleted lines of code` in specific repositories, eg. 'repo-1' and 'repo-2'.

```text
SELECT
  sum(c.deletions) as deleted_lines_of_code
FROM
  commits c
  LEFT JOIN repo_commits rc ON c.sha = rc.commit_sha
  LEFT JOIN repos r ON r.id = rc.repo_id
WHERE
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
  r.id in ('repo-1','repo-2')
  and message not like '%Merge%'
  and $__timeFilter(c.authored_date)
  -- the following condition will remove the month with incomplete data
  and c.authored_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
```

If you want to measure the monthly trend of `deleted lines of code` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/deleted-loc-monthly-cbdb2dc7c1a10a62930dedf4667b0517_27d2bef4297c2e55.png)

```text
with _commits as(
  SELECT
    DATE_ADD(date(authored_date), INTERVAL -DAY(date(authored_date))+1 DAY) as time,
    sum(deletions) as deleted_lines_of_code
  FROM commits
  WHERE
    message not like '%Merge%'
    and $__timeFilter(authored_date)
    -- the following condition will remove the month with incomplete data
    and authored_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  group by 1
)

SELECT
  date_format(time,'%M %Y') as month,
  deleted_lines_of_code
FROM _commits
ORDER BY time
```

<a id="metrics-deletedlinesofcode--how-to-improve"></a>

## How to improve?

1. From the project/team dimension, observe the accumulated change in Added lines to assess the team activity and code growth rate
2. From version cycle dimension, observe the active time distribution of code changes, and evaluate the effectiveness of project development model.
3. From the member dimension, observe the trend and stability of code output of each member, and identify the key points that affect code output by comparison.

- [What is this metric?](#metrics-deletedlinesofcode--what-is-this-metric)
- [Why is it important?](#metrics-deletedlinesofcode--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-deletedlinesofcode--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-deletedlinesofcode--how-is-it-calculated)
- [How to improve?](#metrics-deletedlinesofcode--how-to-improve)

---

<a id="metrics-prcount"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRCount/ -->

<!-- page_index: 51 -->

# PR Count

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Count

<a id="metrics-prcount--what-is-this-metric"></a>

## What is this metric?

The number of pull requests (eg. GitHub PRs, Bitbucket PRs, GitLab MRs) created.

<a id="metrics-prcount--why-is-it-important"></a>

## Why is it important?

1. Code review metrics are process indicators to provide quick feedback on developers' code quality
2. Promote the team to establish a unified coding specification and standardize the code review criteria
3. Identify modules with low-quality risks in advance, optimize practices, and precipitate into reusable knowledge and tools to avoid technical debt accumulation

<a id="metrics-prcount--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)
- [GitLab](https://devlake.apache.org/livedemo/DataSources/GitLab)
- [Weekly Community Retro](https://devlake.apache.org/livedemo/OSSMaintainers/WeeklyCommunityRetro)
- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prcount--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the number of PRs in the given data range.

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find PRs **created** in specific repositories and given time range.

```text
select
    count(*) as pull_request_count
from
    pull_requests pr
where
  -- $__timeFilter will take Grafana's time range
  $__timeFilter(created_date)
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
    and base_repo_id in ('repo_1', 'repo_2')
  -- remove PRs submitted by bots, comment it out if you don't need it
  and author_name not rlike  '^robot-|-robot$|\\[bot\\]|-bot$|-ci$|-testing$'
```

If you want to measure the monthly trend of `PR count` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-count-monthly-944940a90ca55f3029792a0af01f19d9_030fce6b22bd647b.png)

```text
WITH _prs as(
  SELECT
    DATE_ADD(date(created_date), INTERVAL -DAY(date(created_date))+1 DAY) as time,
    count(*) as pr_count
  FROM pull_requests
  WHERE
    -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
    base_repo_id in ('repo_1', 'repo_2')
    and $__timeFilter(created_date)
    -- the following condition will remove the month with incomplete data
    and created_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
    -- remove PRs submitted by bots, comment it out if you don't need it
    and author_name not rlike  '^robot-|-robot$|\\[bot\\]|-bot$|-ci$|-testing$'
  GROUP BY 1
)

SELECT
  date_format(time,'%M %Y') as month,
  pr_count as "Pull Request Count"
FROM _prs
ORDER BY time
```

<a id="metrics-prcount--how-to-improve"></a>

## How to improve?

1. From the developer dimension, we evaluate the code quality of developers by combining the task complexity with the metrics related to the number of review passes and review rounds.
2. From the reviewer dimension, we observe the reviewer's review style by taking into account the task complexity, the number of passes and the number of review rounds.
3. From the project/team dimension, we combine the project phase and team task complexity to aggregate the metrics related to the number of review passes and review rounds, and identify the modules with abnormal code review process and possible quality risks.

- [What is this metric?](#metrics-prcount--what-is-this-metric)
- [Why is it important?](#metrics-prcount--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-prcount--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prcount--how-is-it-calculated)
- [How to improve?](#metrics-prcount--how-to-improve)

---

<a id="metrics-prcycletime"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRCycleTime/ -->

<!-- page_index: 52 -->

# PR Cycle Time

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Cycle Time

<a id="metrics-prcycletime--what-is-this-metric"></a>

## What is this metric?

PR Cycle Time is the sum of PR Coding Time, PR Time-to-Merge and PR Deploy Time. It is the total time from the first commit to when the PR is deployed.

The reason why we use PR Time-to-Merge rather than PR Pickup Time + PR Review Time is that a merged PR may not have any review. In this case, PR Pickup Time and PR Review Time will be NULL, while PR Time-to-Merge is not.

<a id="metrics-prcycletime--why-is-it-important"></a>

## Why is it important?

PR Cycle Time indicates the overall velocity of the delivery progress in terms of PR.

<a id="metrics-prcycletime--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prcycletime--how-is-it-calculated"></a>

## How is it calculated?

You can define `deployment` based on your actual practice. For a full list of `deployment`'s definitions that DevLake support, please refer to [Deployment Frequency](https://devlake.apache.org/docs/Metrics/DeploymentFrequency).

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the `cycle time` of a specific PR. DevLake pre-calculates the metric and stores it in table.project\_pr\_metrics.

```text
SELECT
  pr_cycle_time/60 as 'PR Cycle Time(h)'
FROM
  project_pr_metrics
```

If you want to measure the monthly trend of `PR cycle time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-cycle-time-monthly-2297a31214bf298cf6da56e5f5eabfdc_286cb5a8a52193df.png)

```text
SELECT
  DATE_ADD(date(pr.created_date), INTERVAL -DAY(date(pr.created_date))+1 DAY) as time,
  avg(ppm.pr_cycle_time)/60 as 'PR Cycle Time(h)'
FROM
  pull_requests pr
  JOIN project_pr_metrics ppm ON pr.id = ppm.id
GROUP BY 1
ORDER BY 1
```

<a id="metrics-prcycletime--how-to-improve"></a>

## How to improve?

1. Divide coding tasks into workable and manageable pieces;
2. Use DevLake's dashboards to monitor your delivery progress;
3. Have a habit to check for hanging PRs regularly;
4. Set up alerts for your communication tools (e.g. Slack, Lark) when new PRs are issued;
5. Use automated tests for the initial work;
6. Reduce PR size;
7. Analyze the causes for long reviews.

- [What is this metric?](#metrics-prcycletime--what-is-this-metric)
- [Why is it important?](#metrics-prcycletime--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prcycletime--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prcycletime--how-is-it-calculated)
- [How to improve?](#metrics-prcycletime--how-to-improve)

---

<a id="metrics-prcodingtime"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRCodingTime/ -->

<!-- page_index: 53 -->

# PR Coding Time

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Coding Time

<a id="metrics-prcodingtime--what-is-this-metric"></a>

## What is this metric?

The time it takes from the first commit until a PR is issued.

<a id="metrics-prcodingtime--why-is-it-important"></a>

## Why is it important?

It is recommended that you keep every task on a workable and manageable scale for a reasonably short amount of coding time. The average coding time of most engineering teams is around 3-4 days.

<a id="metrics-prcodingtime--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prcodingtime--how-is-it-calculated"></a>

## How is it calculated?

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the `coding time` of a specific PR. DevLake pre-calculates the metric and stores it in table.project\_pr\_metrics.

```text
SELECT
  pr_coding_time/60 as 'PR Coding Time(h)'
FROM
  project_pr_metrics
```

If you want to measure the monthly trend of `PR coding time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-coding-time-monthly-ef784a357be7784149db0546124bbda3_a0317c00522bed36.png)

```text
SELECT
  DATE_ADD(date(pr.created_date), INTERVAL -DAY(date(pr.created_date))+1 DAY) as time,
  avg(ppm.pr_coding_time)/60 as 'PR Coding Time(h)'
FROM
  pull_requests pr
  JOIN project_pr_metrics ppm ON pr.id = ppm.id
GROUP BY 1
ORDER BY 1
```

<a id="metrics-prcodingtime--how-to-improve"></a>

## How to improve?

Divide coding tasks into workable and manageable pieces.

- [What is this metric?](#metrics-prcodingtime--what-is-this-metric)
- [Why is it important?](#metrics-prcodingtime--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prcodingtime--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prcodingtime--how-is-it-calculated)
- [How to improve?](#metrics-prcodingtime--how-to-improve)

---

<a id="metrics-prpickuptime"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRPickupTime/ -->

<!-- page_index: 54 -->

# PR Pickup Time

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Pickup Time

<a id="metrics-prpickuptime--what-is-this-metric"></a>

## What is this metric?

The time it takes from when a PR is issued until the first comment is added to that PR.

<a id="metrics-prpickuptime--why-is-it-important"></a>

## Why is it important?

PR Pickup Time shows how engaged your team is in collaborative work by identifying the delay in picking up PRs.

<a id="metrics-prpickuptime--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prpickuptime--how-is-it-calculated"></a>

## How is it calculated?

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the `pickup time` of a specific PR. DevLake pre-calculates the metric and stores it in table.project\_pr\_metrics.

```text
SELECT
  pr_pickup_time/60 as 'PR Pickup Time(h)'
FROM
  project_pr_metrics
```

If you want to measure the monthly trend of `PR pickup time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-pickup-time-monthly-c1b29ac4df1b6212190c74117de512f6_625994fc5f27882d.png)

```text
SELECT
  DATE_ADD(date(pr.created_date), INTERVAL -DAY(date(pr.created_date))+1 DAY) as time,
  avg(ppm.pr_pickup_time)/60 as 'PR Pickup Time(h)'
FROM
  pull_requests pr
  JOIN project_pr_metrics ppm ON pr.id = ppm.id
GROUP BY 1
ORDER BY 1
```

<a id="metrics-prpickuptime--how-to-improve"></a>

## How to improve?

1. Use DevLake's dashboard to monitor your delivery progress;
2. Have a habit to check for hanging PRs regularly;
3. Set up alerts for your communication tools (e.g. Slack, Lark) when new PRs are issued.

- [What is this metric?](#metrics-prpickuptime--what-is-this-metric)
- [Why is it important?](#metrics-prpickuptime--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prpickuptime--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prpickuptime--how-is-it-calculated)
- [How to improve?](#metrics-prpickuptime--how-to-improve)

---

<a id="metrics-prreviewtime"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRReviewTime/ -->

<!-- page_index: 55 -->

# PR Review Time

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Review Time

<a id="metrics-prreviewtime--what-is-this-metric"></a>

## What is this metric?

The time it takes to complete a code review of a PR before it gets merged.

<a id="metrics-prreviewtime--why-is-it-important"></a>

## Why is it important?

Code review should be conducted almost in real-time and usually take less than two days. Abnormally long PR Review Time may indicate one or more of the following problems:

1. The PR size is too large that makes it difficult to review.
2. The team is too busy to review code.

<a id="metrics-prreviewtime--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prreviewtime--how-is-it-calculated"></a>

## How is it calculated?

This metric is the time frame between when the first comment is added to a PR, to when the PR is merged.

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the `review time` of a specific PR. DevLake pre-calculates the metric and stores it in table.project\_pr\_metrics.

```text
SELECT
  pr_review_time/60 as 'PR Review Time(h)'
FROM
  project_pr_metrics
```

If you want to measure the monthly trend of `PR review time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-review-time-monthly-93c08cf08a68a91a810a143e188e7a17_1f1da88ac1102d17.png)

```text
SELECT
  DATE_ADD(date(pr.created_date), INTERVAL -DAY(date(pr.created_date))+1 DAY) as time,
  avg(ppm.pr_review_time)/60 as 'PR Review Time(h)'
FROM
  pull_requests pr
  JOIN project_pr_metrics ppm ON pr.id = ppm.id
GROUP BY 1
ORDER BY 1
```

<a id="metrics-prreviewtime--how-to-improve"></a>

## How to improve?

1. Use DevLake's dashboards to monitor your delivery progress;
2. Use automated tests for the initial work;
3. Reduce PR size;
4. Analyze the causes for long reviews.

- [What is this metric?](#metrics-prreviewtime--what-is-this-metric)
- [Why is it important?](#metrics-prreviewtime--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prreviewtime--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prreviewtime--how-is-it-calculated)
- [How to improve?](#metrics-prreviewtime--how-to-improve)

---

<a id="metrics-prdeploytime"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRDeployTime/ -->

<!-- page_index: 56 -->

# PR Deploy Time

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Deploy Time

<a id="metrics-prdeploytime--what-is-this-metric"></a>

## What is this metric?

The time it takes from when a PR is merged to when it is deployed.

<a id="metrics-prdeploytime--why-is-it-important"></a>

## Why is it important?

1. Based on historical data, establish a baseline of the delivery capacity of a single iteration to improve the organization and planning of R&D resources.
2. Evaluate whether the delivery capacity matches the business phase and demand scale. Identify key bottlenecks and reasonably allocate resources.

<a id="metrics-prdeploytime--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prdeploytime--how-is-it-calculated"></a>

## How is it calculated?

`PR deploy time` is calculated by subtracting a PR's deployed\_date and merged\_date. Hence, we should associate PR/MRs with deployments.

Here are the detailed steps:

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAhgAAABdCAYAAADnjh/mAAASwElEQVR4Xu3diY/U5B/Hcf8mNB6boAhGESSrgiiIQS5BQTSCF7usUUA8USMaMIog3ooYBEVBVkTFI6iI54KKgAcgiOvKDc8v7+eXZ9KtszN9Zp6ZdrqfV9K4dGba+rRP++1znmJEREREAjslvkJERESkWgowREREJDgFGCIiIhKcAgwREREJTgGGiIiIBKcAQ0RERIJTgCEiIiLBKcAQkYb0xx9/mNWrV5tdu3bFPxKRDFCAISINp62tzUyYMMEsXLjQTJo0yVxzzTXm0KFD8a+JSIoUYIhIQ9m8ebMNLqJGjRpl1q5d222diKRLAYaI1NTEiRPNpk2bzPjx401zc7OZMWOGOXDggP1sx44dpqWlxSxfvtwMHjzY3HvvvbFf/9f27dv/Uy0ybtw4s3Hjxm7rRCRdCjBEpKb69etnpk2bZv79919z8uRJs3TpUtPa2mo/27p1q+nbt6+58cYbTUdHh9m7d2/s1z3r7Ow0a9asMbNnz7ZBy5EjR+JfEZEUKcAQkZoiwGhvby/8m7YS/fv3N0ePHrUBRp8+fWyDTV+7d+828+fPt9Uj/FcBhki2KMAQkZoiwNizZ0+3daNHjzZbtmyxAcawYcO6fbZo0SK7Lr6MHDmy2/eipkyZYlatWhVfLSIpUoAhIjVFgBFtH3H8+HG7jioOAowRI0ZEvm3MsWPHzOHDh4suoAfJypUru/2G3iTz5s3rtk5E0qUAQ0RqimBi5syZ5uDBg+bEiRNmxYoVZvLkyfazYgFGOcuWLTPDhw83XV1d9t9UrwwZMsSsX78+9k0RSZMCDBGpKQKMd955xwwdOtRWddCThAadqCTAIEhZsGCB3R7tL5qamszixYvjXxORlCnAEJGaIsDYv3+/rRqhYWYo9Eih9IIqFRHJHgUYIlJTLsAQkd5FAYaI1BTVGYyBISK9iwIMERERCU4BhoiIiASnAENERESCU4AhIiIiwSnAEBERkeAUYIiIiEhwCjBEREQkOAUYIiIiEpwCDBEREQlOAYaIiIgEpwBDREREgkstwPjuu+/MF198EV/trb293fz+++/x1bmybds289dff8VXp2rixImmT58+WgIspGU96dyFW2p57v7880/z9ttvx1d76w33SJ4lK1eutLPrSnakFmA8++yzZv78+fHV3qZOnWo++eST+OpM2rJli3nxxRfjq3t06NAhm06nnXaa2bBhQ/zjVMVvtFqqW+opvm8t1S218s0335jRo0fHV3vL8z3y5MmTZubMmWbYsGFm4cKFZtKkSWbatGnm2LFj8a9KChRg1NFrr71m7r///vjqHo0dO9asWLHCXHvttZkNMKQ6aaRjGvvMo1qnY28MMHzvke+9955pbm62gYZz+eWXm3Xr1kW+JWmpW4CxceNGM3LkSHPRRReZefPmmWeeeaYQYJw4ccI8/fTT5uKLL7af33XXXYXpndesWWNefvlle9Fddtll9uJhnRPNPEePHrXbvOSSS+y27r777sJ25syZYz799NPC77gg+e1PP/1kHn30UXthT5gwwQwcONAe399//22mT59uBg8ebB588EFz4MAB+7tyx7po0SJ7rPzulltuMZs3b7afzZ49264bMGCAueqqq2wVUTlHjhyx/73++usVYORUGumYxj7zKHQ67tq1y1x33XX2HnTTTTeZDz/8sBBglLvvJL1HgqqEK664wm6Hz3bu3GnXN+I98rnnnrPbi5oyZYp9MZP01SXA4MI7//zzzdq1a20QwEXGheQCDEozeIj+9ttvpquryyxYsMBeeHj11VdN3759bWYDdWwEENu3b7f/jmaeBx54wNxxxx32wXz8+HHz+OOP2+IycMHdeuut9m9wUQ8dOtRmottuu80MHz7cZjTqPUeMGGGj4q1bt9rjaWtrMy+99JL9XbljPeOMM2wwQBEd+xw1apT9jAz2wgsv2KDnn3/+sceXlAKM/EojHdPYZx6FTkfuFUuWLLH3CqoKxo8fXwgwyt13kt4jebPn/sZ9DtxXBg0aZPfZyPdI5+effzZNTU1235K+ugQYNFSaNWtWt3WTJ08uBBgXXHCB+fLLLwufHTx40Jxzzjlm37599oIkIo968sknzdKlS+3fLvMcPnzYtlVwmQpcsKeffrp9M+Dvfv36mf3799vP7rnnHhv9gszz/PPPF373xBNPmJaWlsK/P/roI1tNgXLHyhuIQyTfv39/s2fPHvtv3+I/RwFGfqWRjmnsM49CpiNBAW/7UZQCuACj3H0nyT0SlEAsX748+lVbFUupRiPfI/H111/bF1f+XyQb6hJgEJFy4URRrEWAQUNGMumVV15pI1m3EB1///339oLkQo8iUifTwGUeAotzzz232/dw9dVXF4r97rvvPtuAiGCEYjgueJB5onV2ROIPPfRQ4d9cuGT0JMdKKUoU1UJ8hnjmIQ1onBRf+E2UAoz8SiMd09hnHoVMR17Cog9s0DMi6X0nyT0SlCT/+OOP0a/a+zANJNGo90i2O2TIEPP55593Wy/pqkuAwUVDHV1Ua2troQTj7LPPNh0dHd0+J2CgiIwLZ8yYMd0+I6p2v3WZhyI1Luzdu3cXvkd1DEWHLkNxEVP3+O6779oM4yTNPCh3rD6ZhyJCMnKxJUoBRn6lkY5p7DOPQqYj7RzipRCUNCS97yS5R4KHfbR9hvt82bJl9u9GvEfSPmTcuHGFah/JjroEGPTBpsEP9XGg3o7o2GUASjjmzp1rAwIQfVOUR90fF+SZZ55p6yRBURqlEq4ILpp5br75ZvPUU0/Zv/Hmm2/aDEUxnMNvORYanTo+mafcsZbKPKtXrzZ33nlnt8+TUICRX2mkYxr7zKPQ6ejaNICSA8bYSHrfSXqP5N7Gv103Th78VIu4Kgo00j3ys88+K7QhkeypS4ABGv5Qx0g/ZVo6UyTnAgxaI9MYk+I7IlEuZteWgguSi5V1ROlnnXWWefjhhwtBQzTzUHfIw5gWyDSQIqPQ/iKKtwLq6aJBh0/mKXespTIPETbHxY3EtbhOQgFGfqWRjmnsM49CpyMPS4r5aZ9GO4ZXXnkl8X0n6T2SUgQ+oxEo+yGQ+Pjjj+1nTiPdIyntoJ0dpSbRJdpepLej4eyvv/4aX10XdQswQEQbrcKI6+zstFUdUdELktEsaTBUDhe4a6gUR8+SaClHpYoda28S+ubaW6WRjmnsM49qkY481GnwGX24RxW771Ryj6SnHfuJjh/h6B6ZL+46JQBkeIhoR4haq2uAUYliEW+lqLc777zzcj9sbj3U4uaaBkq4KukOF0WGpeW6ewvzkUY6prHPWghx7ihap/s8g1r19FDvSVbSUfdIKcVdp9GFbsY0oHVVcrWS+QCDltSMpR8CDwIVnYWRlZtrNXiLo08+DdrA2x+t6H3QOI6i4EceecTcfvvtNuP63JzTSMc09hlaiHPHg5kGjVTVcu6oLvB5u8tKOuoeKaXEg4v44oZZTzKwma+KA4z4QWrpnUujo27SvQUzSA/tg5Lau3evbVwXHdSH3lI+b5Px9Kzn0uiqOXeUXNDOgOpUhyDRJ0iJp6cWLY2+0PaFgJsGw8Wqz3wpwNBS1eKDOl+GQL7wwgvtoDxvvPFG4TMad9EYjEZuPChoFOwucLrVMbAPkxrR+O2GG26wDcDICDQc5neuqM/nu2DkQora6R7HfmkgRyPh+GBExfDmyPajFi9ebEeTTSqenvVcfJQ6d6WG6Pc5Hzt27LD/ZoApHv5uuGjGiODc0GDw/fffL+y3mnNHG634GxsjTtL+IKl4emrR0uiLCzC++uqrdAOMJNxBS3WymI6+x8SbJkVx1Pvx8KGxLw8F3jyp+6YlOQ8K/qZhGC3caf0MirIpDt+0aZNtwMbcBtQT0+6B7na0aKeLsu93wTExTgpF7kTtDI3M/t08MD74DQ9G6vST8k3HEHz3WercodQQ/T7ng0Dj1FNPtSNQsi2uB0Z5pKcAbQPoqcBvXalFqHNH0MIx08PNp7W9bzr2JNR2ejulY3EuXXpaMllFkoROeBhZTEffY2I0VdoqRKPib7/91s53QPe8+Gd0neNhDR5SvD077vuuUR4PPd5eebD4fBfuIQXfYvYoSmDo68+ETT580zEE332WOnc8+EsN0e9zPggwGJPBjdHAqJBsxwUyoOs5JUcIde7oMUFXcIKi6HgQ5fimY09Cbae3UzoW59IlurhGntu2bYt/PSgFGA0gi+noe0yvv/66bUhXTLHPePCwfRc0RNs1/PDDDzaDRPEg4jc+30WphxQDDcWHKHZLdLhlHnhU7bBv32JF33QMwXefxc6PU26Ifp/zQYDBhFpRjMQbHQ+BKhY3qVeIcxdF9RYlLEn5pmNPQm2nt1M6FufSJXfdVHXCw8hiOvoe0/r16//zhsnDhofzBx98YC699NJun1Hk7R5cPg8pn++i1EOKt+z48MRucW/g/H9R0uJGUfTlm44h+O6z1LkrN0S/z/kIGWCUO3f0/qGtSBQBEb1KkvJNx56E2k5vp3QsLrcDbemEh5HFdPQ9JlrrU/xNETmoR2fEPur9qJun8aCbqIhSgDlz5tgRB+HzkPL5LqIPKbqXumqZJOgaSRuBauoufdMxBN99ljp3KDVEv8/5qCbA8D137IuqGfc2x/6ZUtxdc0n4pmNPQm2nt1M6Zo8CjAaQxXSs5JhcXT4PHyZ2ij6UeFjxcKGHAv9ta2srBAE+Dymf7yJeZM5+6d3A9NPlMAYDjRLjwxRPnz49/tUeVZKO1apkn6XOXakh+n3ORzUBBnzOHeidQrExM382NTXZni7uukiiknQsJtR2ejulY/YowGgAWUzHSo+J0olSQyHTyM7nJt/oKk3HalS6z3LnrtQQ/VlGA91KrrlK0zEu1HZ6O6Vj9ijAaABZTMcsHlMjSiMd09hnHoVKx1Db6e2UjtmjACOhSt9yomhrQF9+X1lMxyweUyNKIx3T2GcehUrHUNtJW4i5YRzut75z++QlHfNEAUZCtA1gwB+HIYVp5JcU9cvUX1Pf6yuL6ZjFY2pEaaRjGvvMo1DpGGo7aQoxN4zDtrhX0q7HRx7SMW8UYCS0b9++biUYAwYMsOuSeOutt+w4AqtWrVKAId2kkY5p7DOPQqVjqO2krZq5YaLmzp1rZs2apQAjBzIZYBDBUlpAi3AeyMwR4Eb3A8MM01+dz6dOnWp27txp1/vOZTBx4kTbpY7PmEOB7XZ0dNiW8MyrwKAkzpIlS2x0zrTObJfRC2kNH+9LX4wbNZLx3RVgSFQa6ZjGPvMoVDpWsp1Sc8M04rw+Di9jlHwwtLwCjMaXyQCDh/aMGTNsJurq6rLdz9xFum7dOvtgJxNhw4YNZtCgQYVubj5zGdC3v6WlxXR2dtruc8yMScDCttk3mYT14KJncB5+y+BCbPeXX37xapehAEPi0kjHNPaZR6HS0Xc7peaGaeR5ffgtw+3zfQUY+ZC5AIMLOT63AdNiE02DCzAeEY8dO9Ze9L5zGfDd6CBJbJuM6Tz22GM2E8MFGI5PFYmjAEPi0kjHNPaZR6HS0Xc7peaGadR5fdjWmDFjCuOnKMDIh8wFGAQWlA70hAs8PpcARXbMBuc7UA8BRrTfPtE4wyI7lISwbZQKMGjQFJ/vwC0EPk4eAwwtYZZ6iu9bS3VLtXy3U2pumGKf8fBm+1me14dqmPb2dhu8sBDMEGD0NOZKMb7pKLWXuQCDYIDfuCoQ8ABfvXq1/ZvWxa40w6Fag4d/WgEGbwvx+Q7cEu22lacAg/Yr8RutlsoW0rKedO7CLSHOndtWUqXmhmnUeX24r9MOzi0DBw60o6vyd9Kh+H3TUWovcwEGJk2aZKsm3MOZh7yrQ6Tej4DCVYNQ4kGgwAiQ9QwwmpubC8V5SeUpwBCRMHzzd6m5YRp1Xp84VZHkQyYDDLo7MUcAD3EaLLW2ttr2FCAzkVno5UHjJSJc6hhRzwCDQIfji87JUI4CDBGJqyR/l5obphHn9YlTgJEPmQwwHKogKEIrhvpEenpEGzPlVbXpKCLZVWn+Ljc3jOb1kbRlOsCQ/1M6iuSX8ncYSsfsUYDRAJSOIvml/B2G0jF7FGA0AKWjSH4pf4ehdMweBRgNQOkokl/K32EoHbNHAUYDUDqK5JfydxhKx+xRgNEAlI4i+aX8HYbSMXsUYDQApaNIfil/h6F0zB4FGA1A6SiSX8rfYSgds6cuAYaWMIuI5E88n2upbpHsqGmAoUmVwi0hJlUSkezRfTLcovtkttQ0wBAREZHeSQGGiIiIBKcAQ0RERIJTgCEiIiLBKcAQERGR4BRgiIiISHAKMERERCQ4BRgiIiISnAIMERERCU4BhoiIiASnAENERESCU4AhIiIiwSnAEBERkeAUYIiIiEhwCjBEREQkOAUYIiIiEpwCDBEREQnuf1EJw6EHEDlLAAAAAElFTkSuQmCC)

1. Find the [commits diff](https://devlake.apache.org/docs/Plugins/refdiff/) between two consecutive deployments by deployments' commit\_sha
   under the same scope and environment (in terms of TESTING/STAGING/PRODUCTION),
   for example, we will get commit-2 and commit-3 by calculating commits\_diff between deployment-1 and deployment-2, which means commit-2 and commit-3 are deployed by deployment-2
2. Connect PR/MR and commits\_diff through merge\_commit or pr\_commit, for example,
   we get pr-3 connected to commit-3
3. Now we can get pr-3's deploy time by finish\_time of deployment-2 minus merge\_time of pr-3.

**Data Transformation Required**

This metric relies on two sources:

1. PR/MRs collected from GitHub or GitLab by enabling "Code Review" under the Data Entities section.
2. Deployments collected in one of the following ways::
   - Open APIs of Jenkins, GitLab, GitHub, etc by enabling "CICD" under the Data Entities section.
   - Webhook for general CI tools.
   - Releases and PR/MRs from GitHub, GitLab APIs, etc.

**SQL Queries**

The following SQL shows how to find the `deploy time` of a specific PR. DevLake pre-calculates the metric and stores it in table.project\_pr\_metrics.

```text
SELECT
  pr_deploy_time/60 as 'PR Deploy Time(h)'
FROM
  project_pr_metrics
```

If you want to measure the monthly trend of `PR deploy time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-deploy-time-monthly-cc8f4e0f2bb961f51b6766625fcaf364_96473c104c5e5fa5.png)

```text
SELECT
  DATE_ADD(date(pr.created_date), INTERVAL -DAY(date(pr.created_date))+1 DAY) as time,
  avg(ppm.pr_deploy_time)/60 as 'PR Deploy Time(h)'
FROM
  pull_requests pr
  JOIN project_pr_metrics ppm ON pr.id = ppm.id
GROUP BY 1
ORDER BY 1
```

<a id="metrics-prdeploytime--how-to-improve"></a>

## How to improve?

N/A

- [What is this metric?](#metrics-prdeploytime--what-is-this-metric)
- [Why is it important?](#metrics-prdeploytime--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prdeploytime--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prdeploytime--how-is-it-calculated)
- [How to improve?](#metrics-prdeploytime--how-to-improve)

---

<a id="metrics-prtimetomerge"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRTimeToMerge/ -->

<!-- page_index: 57 -->

# PR Time To Merge

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Time To Merge

<a id="metrics-prtimetomerge--what-is-this-metric"></a>

## What is this metric?

The time it takes from when a PR is issued to when it is merged. Essentially, PR Time to Merge = PR Pickup Time + PR Review Time.

<a id="metrics-prtimetomerge--why-is-it-important"></a>

## Why is it important?

The delay of reviewing and waiting to review PRs has large impact on delivery speed, while reasonably short PR Time to Merge can indicate frictionless teamwork. Improving on this metric is the key to reduce PR cycle time.

<a id="metrics-prtimetomerge--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)
- [Weekly Community Retro](https://devlake.apache.org/livedemo/OSSMaintainers/WeeklyCommunityRetro)

<a id="metrics-prtimetomerge--how-is-it-calculated"></a>

## How is it calculated?

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the `mean time to merge of PRs` in specific repositories and given time range.

![](assets/images/pr-time-to-merge-text-3c5e1aa05c3ec3ff350ee3b2d54dce6c_261e58d9007f8f4a.png)

```text
SELECT
    avg(TIMESTAMPDIFF(Minute,created_date,merged_date)/1440)
FROM
    pull_requests
WHERE
  -- $__timeFilter will take Grafana's time range
  $__timeFilter(created_date)
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
    and base_repo_id in ('repo_1', 'repo_2')
    and merged_date is not null
```

If you want to measure the monthly trend of `PR time to merge` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-time-to-merge-monthly-996cf97309f11f98aaece50be09604c8_139541bb4faa90b5.png)

```text
with _prs as(
  SELECT
    DATE_ADD(date(created_date), INTERVAL -DAY(date(created_date))+1 DAY) as time,
    avg(TIMESTAMPDIFF(Minute,created_date,merged_date)/1440) as time_to_merge
  FROM pull_requests
  WHERE
    $__timeFilter(created_date)
    -- the following condition will remove the month with incomplete data
    and created_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
    -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
      and base_repo_id in ('repo_1', 'repo_2')
  GROUP BY 1
)

SELECT
  date_format(time,'%M %Y') as month,
  time_to_merge as "Time to Merge"
FROM _prs
ORDER BY time
```

<a id="metrics-prtimetomerge--how-to-improve"></a>

## How to improve?

1. Use DevLake's dashboards to monitor your delivery progress;
2. Have a habit to check for hanging PRs regularly;
3. Set up alerts for your communication tools (e.g. Slack, Lark) when new PRs are issued;
4. Reduce PR size;
5. Analyze the causes for long reviews.

- [What is this metric?](#metrics-prtimetomerge--what-is-this-metric)
- [Why is it important?](#metrics-prtimetomerge--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prtimetomerge--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prtimetomerge--how-is-it-calculated)
- [How to improve?](#metrics-prtimetomerge--how-to-improve)

---

<a id="metrics-prmergerate"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRMergeRate/ -->

<!-- page_index: 58 -->

# PR Merge Rate

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Merge Rate

<a id="metrics-prmergerate--what-is-this-metric"></a>

## What is this metric?

The ratio of PRs/MRs that get merged.

<a id="metrics-prmergerate--why-is-it-important"></a>

## Why is it important?

1. Code review metrics are process indicators to provide quick feedback on developers' code quality
2. Promote the team to establish a unified coding specification and standardize the code review criteria
3. Identify modules with low-quality risks in advance, optimize practices, and precipitate into reusable knowledge and tools to avoid technical debt accumulation

<a id="metrics-prmergerate--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [GitHub](https://devlake.apache.org/livedemo/DataSources/GitHub)
- [GitLab](https://devlake.apache.org/livedemo/DataSources/GitLab)
- [Weekly Community Retro](https://devlake.apache.org/livedemo/OSSMaintainers/WeeklyCommunityRetro)
- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prmergerate--how-is-it-calculated"></a>

## How is it calculated?

The number of merged PRs divided by the number of all PRs in the given data range.

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the PR merged rate in specific repositories and given time range, eg. 'repo-1' and 'repo-2'.

```text
select
    count(distinct case when merged_date is not null then id else null end)/count(*) as pr_merged_rate
from
    pull_requests pr
where
  -- $__timeFilter will take Grafana's time range
  $__timeFilter(created_date)
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
    and base_repo_id in ('repo_1', 'repo_2')
  -- remove PRs submitted by bots, comment it out if you don't need it
  and author_name not rlike  '^robot-|-robot$|\\[bot\\]|-bot$|-ci$|-testing$'
```

If you want to measure the monthly trend of `PR merge rate` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-merge-rate-monthly-aa8035b065e18b38e20a0997228443b4_6e597e0d7e1f027b.png)

```text
SELECT
  DATE_ADD(date(created_date), INTERVAL -DAYOFMONTH(date(created_date))+1 DAY) as time,
  count(distinct case when merged_date is not null then id else null end)/count(*) as pr_merged_rate
FROM pull_requests
WHERE
  $__timeFilter(created_date)
  -- please replace the repo ids with your own, or create a '$repo_id' variable in Grafana
  and base_repo_id in ('repo_1', 'repo_2')
  -- remove PRs submitted by bots, comment it out if you don't need it
  and author_name not rlike  '^robot-|-robot$|\\[bot\\]|-bot$|-ci$|-testing$'
GROUP BY 1
```

If you want to measure the monthly trend of `PR status distribution`, please run the following SQL in Grafana.

![](assets/images/pr-status-distribution-monthly-535e1b8c62d61a515c9b47ccaf076c16_f993d0b4e71ccb10.png)

```text
SELECT
  DATE_ADD(date(created_date), INTERVAL -DAYOFMONTH(date(created_date))+1 DAY) as time,
  count(distinct case when status != 'closed' then id else null end) as "PR: Open",
  count(distinct case when status = 'closed' and merged_date is null then id else null end) as "PR: Closed without merging",
  count(distinct case when status = 'closed' and merged_date is not null then id else null end) as "PR: Closed and merged"
FROM pull_requests
WHERE
  $__timeFilter(created_date)
  and created_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  and base_repo_id in ('repo_1', 'repo_2')
  -- remove PRs submitted by bots, comment it out if you don't need it
  and author_name not rlike  '^robot-|-robot$|\\[bot\\]|-bot$|-ci$|-testing$'
GROUP BY 1
```

<a id="metrics-prmergerate--how-to-improve"></a>

## How to improve?

1. From the developer dimension, we evaluate the code quality of developers by combining the task complexity with the metrics related to the number of review passes and review rounds.
2. From the reviewer dimension, we observe the reviewer's review style by taking into account the task complexity, the number of passes and the number of review rounds.
3. From the project/team dimension, we combine the project phase and team task complexity to aggregate the metrics related to the number of review passes and review rounds, and identify the modules with abnormal code review process and possible quality risks.

- [What is this metric?](#metrics-prmergerate--what-is-this-metric)
- [Why is it important?](#metrics-prmergerate--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-prmergerate--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prmergerate--how-is-it-calculated)
- [How to improve?](#metrics-prmergerate--how-to-improve)

---

<a id="metrics-prreviewdepth"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRReviewDepth/ -->

<!-- page_index: 59 -->

# PR Review Depth

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Review Depth

<a id="metrics-prreviewdepth--what-is-this-metric"></a>

## What is this metric?

The average number of comments of PRs in the selected time range.

<a id="metrics-prreviewdepth--why-is-it-important"></a>

## Why is it important?

PR Review Depth (in Comments per RR) is related to the quality of code review, indicating how thorough your team reviews PRs.

<a id="metrics-prreviewdepth--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prreviewdepth--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the total number of PR comments divided by the total number of PRs in the selected time range.

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

If you want to measure the monthly trend of `PR review time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-review-depth-monthly-a459a8bf854dbaeb50bc9f84e23fec01_22507c3edbc802af.png)

```text
SELECT
  DATE_ADD(date(pr.created_date), INTERVAL -$interval(date(pr.created_date))+1 DAY) as time,
  count(distinct prc.id)/count(pr.id) as "PR Review Depth"
FROM
  pull_requests pr
  left join pull_request_comments prc on pr.id = prc.pull_request_id
WHERE
  $__timeFilter(pr.created_date)
  and pr.base_repo_id in ($repo_id)
  and pr.merged_date is not null
GROUP BY 1
```

<a id="metrics-prreviewdepth--how-to-improve"></a>

## How to improve?

1. Encourage multiple reviewers to review a PR;
2. Review Depth is an indicator for generally how thorough your PRs are reviewed, but it does not mean the deeper the better. In some cases, spending an excessive amount of resources on reviewing PRs is also not recommended.

- [What is this metric?](#metrics-prreviewdepth--what-is-this-metric)
- [Why is it important?](#metrics-prreviewdepth--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prreviewdepth--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prreviewdepth--how-is-it-calculated)
- [How to improve?](#metrics-prreviewdepth--how-to-improve)

---

<a id="metrics-prsize"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/PRSize/ -->

<!-- page_index: 60 -->

# PR Size

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PR Size

<a id="metrics-prsize--what-is-this-metric"></a>

## What is this metric?

The average code changes (in Lines of Code) of PRs in the selected time range.

<a id="metrics-prsize--why-is-it-important"></a>

## Why is it important?

Small PRs can reduce risks of introducing new bugs and increase code review quality, as problems may often be hidden in big chuncks of code and difficult to identify.

<a id="metrics-prsize--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [Engineering Throughput and Cycle Time](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTime)
- [Engineering Throughput and Cycle Time - Team View](https://devlake.apache.org/livedemo/EngineeringLeads/EngineeringThroughputAndCycleTimeTeamView)

<a id="metrics-prsize--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the total number of code changes (in LOC) divided by the total number of PRs in the selected time range.

**Data Sources Required**

This metric relies on PRs/MRs collected from GitHub, GitLab, BitBucket, Gitee or other code review tools.

**Data Transformation Required**

N/A

**SQL Queries**

If you want to measure the monthly trend of `PR review time` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/pr-size-monthly-a18c16dc0ff755d709ad27b4d5d9b744_e705aa07a1b0de45.png)

```text
with _pr_commits_data as(
  SELECT
    DATE_ADD(date(pr.created_date), INTERVAL -$interval(date(pr.created_date))+1 DAY) as time,
    pr.id as pr_id,
    prc.commit_sha,
    sum(c.additions)+sum(c.deletions) as loc
  FROM
    pull_requests pr
    left join pull_request_commits prc on pr.id = prc.pull_request_id
    left join commits c on prc.commit_sha = c.sha
  WHERE
    $__timeFilter(pr.created_date)
    and pr.base_repo_id in ($repo_id)
  group by 1,2,3
)

SELECT
  time,
  sum(loc)/count(distinct pr_id) as 'PR Size'
FROM _pr_commits_data
GROUP BY 1
```

<a id="metrics-prsize--how-to-improve"></a>

## How to improve?

1. Divide coding tasks into workable and manageable pieces;
2. Encourage developers to submit small PRs and only keep related changes in the same PR.

- [What is this metric?](#metrics-prsize--what-is-this-metric)
- [Why is it important?](#metrics-prsize--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-prsize--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-prsize--how-is-it-calculated)
- [How to improve?](#metrics-prsize--how-to-improve)

---

<a id="metrics-buildcount"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/BuildCount/ -->

<!-- page_index: 61 -->

# Build Count

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Build Count

<a id="metrics-buildcount--what-is-this-metric"></a>

## What is this metric?

The number of successful builds.

<a id="metrics-buildcount--why-is-it-important"></a>

## Why is it important?

1. As a process indicator, it reflects the value flow efficiency of upstream production and research links
2. Identify excellent/to-be-improved practices that impact the build, and drive the team to precipitate reusable tools and mechanisms to build infrastructure for fast and high-frequency delivery

<a id="metrics-buildcount--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jenkins](https://grafana-lake.demo.devlake.io/grafana/d/W8AiDFQnk/jenkins?orgId=1)

<a id="metrics-buildcount--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the number of successful cicd\_pipelines, such as Jenkins builds, GitLab pipelines and GitHub workflow runs in the given data range.

**Data Sources Required**

This metric relies on Jenkins builds, GitLab pipelines or GitHub workflow runs.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the total number of successful CI builds **finished** in the given time range.

```text
SELECT
  count(*)
FROM
  cicd_pipelines
WHERE
  result = 'SUCCESS'
  and $__timeFilter(finished_date)
ORDER BY 1
```

If you want to measure the monthly trend of the `successful build count` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/build-count-monthly-90f7a5a678e6931debdacd6c48eec72f_3ee76c2e9bd44e5b.png)

```text
WITH _builds as(
  SELECT
    DATE_ADD(date(finished_date), INTERVAL -DAYOFMONTH(date(finished_date))+1 DAY) as time,
    count(*) as build_count
  FROM
    cicd_pipelines
  WHERE
    result = "SUCCESS"
    and $__timeFilter(finished_date)
    -- the following condition will remove the month with incomplete data
    and finished_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  GROUP BY 1
)

SELECT
  date_format(time,'%M %Y') as month,
  build_count as "Build Count"
FROM _builds
ORDER BY time
```

<a id="metrics-buildcount--how-to-improve"></a>

## How to improve?

1. From the project dimension, compare the number of builds and success rate by combining the project phase and the complexity of tasks.
2. From the time dimension, analyze the trend of the number of builds and success rate to see if it has improved over time.

- [What is this metric?](#metrics-buildcount--what-is-this-metric)
- [Why is it important?](#metrics-buildcount--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-buildcount--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-buildcount--how-is-it-calculated)
- [How to improve?](#metrics-buildcount--how-to-improve)

---

<a id="metrics-buildduration"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/BuildDuration/ -->

<!-- page_index: 62 -->

# Build Duration

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Build Duration

<a id="metrics-buildduration--what-is-this-metric"></a>

## What is this metric?

The duration of successful builds.

<a id="metrics-buildduration--why-is-it-important"></a>

## Why is it important?

1. As a process indicator, it reflects the value flow efficiency of upstream production and research links
2. Identify excellent/to-be-improved practices that impact the build, and drive the team to precipitate reusable tools and mechanisms to build infrastructure for fast and high-frequency delivery

<a id="metrics-buildduration--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jenkins](https://grafana-lake.demo.devlake.io/grafana/d/W8AiDFQnk/jenkins?orgId=1)

<a id="metrics-buildduration--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by getting the duration of successful cicd\_pipelines, such as Jenkins builds, GitLab pipelines and GitHub workflow runs in the given data range.

**Data Sources Required**

This metric relies on Jenkins builds, GitLab pipelines or GitHub workflow runs.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the mean duration of successful CI builds **finished** in the given time range.

```text
SELECT
  avg(duration_sec/60) as duration_in_minutes
FROM cicd_pipelines
WHERE
  result = 'SUCCESS'
  and $__timeFilter(finished_date)
ORDER BY 1
```

If you want to measure the `mean duration of builds` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/build-duration-monthly-cd1d38f33475808d166c3ffc2f2733c6_61310df361423e8c.png)

```text
WITH _builds as(
  SELECT
    DATE_ADD(date(finished_date), INTERVAL -DAYOFMONTH(date(finished_date))+1 DAY) as time,
    avg(duration_sec) as mean_duration_sec
  FROM
    cicd_pipelines
  WHERE
    $__timeFilter(finished_date)
    and id like "%jenkins%"
    and name in ($job_id)
    -- the following condition will remove the month with incomplete data
    and finished_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
  GROUP BY 1
)

SELECT
  date_format(time,'%M %Y') as month,
  mean_duration_sec/60 as mean_duration_minutes
FROM _builds
ORDER BY time
```

<a id="metrics-buildduration--how-to-improve"></a>

## How to improve?

1. From the project dimension, compare the number of builds and success rate by combining the project phase and the complexity of tasks.
2. From the time dimension, analyze the trend of the number of builds and success rate to see if it has improved over time.

- [What is this metric?](#metrics-buildduration--what-is-this-metric)
- [Why is it important?](#metrics-buildduration--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-buildduration--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-buildduration--how-is-it-calculated)
- [How to improve?](#metrics-buildduration--how-to-improve)

---

<a id="metrics-buildsuccessrate"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/BuildSuccessRate/ -->

<!-- page_index: 63 -->

# Build Success Rate

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Build Success Rate

<a id="metrics-buildsuccessrate--what-is-this-metric"></a>

## What is this metric?

The ratio of successful builds to all builds.

<a id="metrics-buildsuccessrate--why-is-it-important"></a>

## Why is it important?

1. As a process indicator, it reflects the value flow efficiency of upstream production and research links
2. Identify excellent/to-be-improved practices that impact the build, and drive the team to precipitate reusable tools and mechanisms to build infrastructure for fast and high-frequency delivery

<a id="metrics-buildsuccessrate--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

- [Jenkins](https://grafana-lake.demo.devlake.io/grafana/d/W8AiDFQnk/jenkins?orgId=1)

<a id="metrics-buildsuccessrate--how-is-it-calculated"></a>

## How is it calculated?

The number of successful builds divided by the total number of builds in the given data range.

**Data Sources Required**

This metric relies on Jenkins builds, GitLab pipelines or GitHub workflow runs.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the success rate of CI builds **finished** in the given time range.

```text
SELECT
  1.0 * sum(case when result = 'SUCCESS' then 1 else 0 end)/ count(*) as "Build Success Rate"
FROM
  cicd_pipelines
WHERE
  $__timeFilter(finished_date)
ORDER BY 1
```

If you want to measure the distribution of CI build result like the donut chart below, please run the following SQL in Grafana.

![](assets/images/build-result-distribution-940f7704a76fe24331ff5ed0d08582dc_99e21a844bc9817e.png)

```text
SELECT
  result,
  count(*) as build_count
FROM
  cicd_pipelines
WHERE
  $__timeFilter(finished_date)
  and id like "%jenkins%"
  and name in ($job_id)
  -- the following condition will remove the month with incomplete data
  and finished_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
GROUP BY 1
ORDER BY 2 DESC
```

If you want to measure the `mean build success rate per month` in the screenshot below, please run the following SQL in Grafana.

![](assets/images/build-success-rate-monthly-83f229c1d5118c159253a66dea930f95_b06a34a0a30292dc.png)

```text
WITH _build_success_rate as(
  SELECT
    DATE_ADD(date(finished_date), INTERVAL -DAYOFMONTH(date(finished_date))+1 DAY) as time,
    result
  FROM
    cicd_pipelines
  WHERE
    $__timeFilter(finished_date)
    -- the following condition will remove the month with incomplete data
    and finished_date >= DATE_ADD(DATE_ADD($__timeFrom(), INTERVAL -DAY($__timeFrom())+1 DAY), INTERVAL +1 MONTH)
)

SELECT
  date_format(time,'%M %Y') as month,
  1.0 * sum(case when result = 'SUCCESS' then 1 else 0 end)/ count(*) as "Build Success Rate"
FROM _build_success_rate
GROUP BY 1
ORDER BY 1
```

<a id="metrics-buildsuccessrate--how-to-improve"></a>

## How to improve?

1. From the project dimension, compare the number of builds and success rate by combining the project phase and the complexity of tasks.
2. From the time dimension, analyze the trend of the number of builds and success rate to see if it has improved over time.

- [What is this metric?](#metrics-buildsuccessrate--what-is-this-metric)
- [Why is it important?](#metrics-buildsuccessrate--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-buildsuccessrate--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-buildsuccessrate--how-is-it-calculated)
- [How to improve?](#metrics-buildsuccessrate--how-to-improve)

---

<a id="metrics-deploymentfrequency"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/DeploymentFrequency/ -->

<!-- page_index: 64 -->

# DORA - Deployment Frequency

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DORA - Deployment Frequency

<a id="metrics-deploymentfrequency--what-is-this-metric"></a>

## What is this metric?

How often an organization deploys code to production or release it to end users. Below is a picture showing the definition of DevLake `deployments`.

![](assets/images/deployment-definition-2e776551aa90ae4009b0335adfab2411_b39f90c37c0f7e59.png)

<a id="metrics-deploymentfrequency--why-is-it-important"></a>

## Why is it important?

Deployment frequency reflects the efficiency of a team's deployment. A team that deploys more frequently can deliver the product faster and users' feature requirements can be met faster.

<a id="metrics-deploymentfrequency--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

DORA dashboard. See [live demo](https://grafana-lake.demo.devlake.io/grafana/d/qNo8_0M4z/dora?orgId=1).

<a id="metrics-deploymentfrequency--how-is-it-calculated"></a>

## How is it calculated?

Deployment frequency is calculated based on the number of `deployment days`, not the number of deployments, e.g., daily, weekly, monthly, yearly.

When there are multiple deployments triggered by one pipeline, tools like GitLab and BitBucket will generate more than one deployment. In these cases, DevLake will consider these deployments as ONE deployment and use the last deployment's finished date as the deployment finished date.

Below are the 2023 DORA benchmarks for different development teams from Google's report. However, it's difficult to tell which group a team falls into when the team's deployment frequency is `between once per week and once per month`. Therefore, DevLake provides its own benchmarks to address this problem:

<table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th><th>The Criteria of DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>On-demand (multiple deploys per day)</td><td>On-demand</td><td>Median Number of <code>Deployment Days</code> per Week &gt;= 5</td></tr><tr><td>High performers</td><td>Between once per day and once per week</td><td>Between once per day and once per week</td><td>Median Number of <code>Deployment Days</code> per Week &gt;= 1</td></tr><tr><td>Medium performers</td><td>Between once per week and once per month</td><td>Between once per week and once per month</td><td>Median Number of <code>Deployment Days</code> per Month &gt;= 1</td></tr><tr><td>Low performers</td><td>Between once per week and once per month</td><td>Fewer than once per month</td><td>Median Number of <code>Deployment Days</code> per Month &lt; 1</td></tr></tbody></table>

*Source: 2023 Accelerate State of DevOps, Google*

> [!INFO]
> **Click to expand or collapse 2021 DORA benchmarks**
> <table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th><th>The Criteria of DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>On-demand (multiple deploys per day)</td><td>On-demand</td><td>Median Number of <code>Deployment Days</code> per Week &gt;= 5</td></tr><tr><td>High performers</td><td>Between once per week and once per month</td><td>Between once per day and once per month</td><td>Median Number of <code>Deployment Days</code> per Month &gt;= 1</td></tr><tr><td>Medium performers</td><td>Between once per month and once every 6 months</td><td>Between once per month and once every 6 months</td><td>Median Number of <code>Deployment Days</code> per six Months &gt;= 1</td></tr><tr><td>Low performers</td><td>Fewer than once per six months</td><td>Fewer than once per six months</td><td>Median Number of <code>Deployment Days</code> per six Months &lt; 1</td></tr></tbody></table>
>
> *Source: 2021 Accelerate State of DevOps, Google*

**Data Sources Required**

- `Deployments` from Jenkins, GitLab CI, GitHub Action, BitBucket Pipelines, Webhook, etc.

**Transformation Rules Required**

Define `deployment` in [data transformations](https://devlake.apache.org/docs/Configuration/Tutorial#step-3---add-transformations-optional) while configuring the blueprint of a project to let DevLake know what CI records can be regarded as deployments.

**SQL Queries**

DevLake deployments can be found in table [cicd\_deployment\_commits](https://devlake.apache.org/docs/DataModels/DevLakeDomainLayerSchema#cicd_deployment_commits). If you want to measure the monthly trend of deployment count as the picture shown below, run the following SQL in Grafana.

![](assets/images/deployment-frequency-monthly-e3d6db34bbe66ff899f5dc15ae0716be_e09206fbdd23e420.jpeg)

```text
-- Metric 1: Number of deployments per month
with _deployments as(
-- When deploying multiple commits in one pipeline, GitLab and BitBucket may generate more than one deployment. However, DevLake consider these deployments as ONE production deployment and use the last one's finished_date as the finished date.
    SELECT
        date_format(deployment_finished_date,'%y/%m') as month,
        count(cicd_deployment_id) as deployment_count
    FROM (
        SELECT
            cdc.cicd_deployment_id,
            max(cdc.finished_date) as deployment_finished_date
        FROM cicd_deployment_commits cdc
        JOIN project_mapping pm on cdc.cicd_scope_id = pm.row_id and pm.`table` = 'cicd_scopes'
        WHERE
            pm.project_name in (${project:sqlstring}+'')
            and cdc.result = 'SUCCESS'
            and cdc.environment = 'PRODUCTION'
        GROUP BY 1
        HAVING $__timeFilter(max(cdc.finished_date))
    ) _production_deployments
    GROUP BY 1
)

SELECT
    cm.month,
    case when d.deployment_count is null then 0 else d.deployment_count end as deployment_count
FROM
    calendar_months cm
    LEFT JOIN _deployments d on cm.month = d.month
    WHERE $__timeFilter(cm.month_timestamp)
```

If you want to measure in which category your team falls as in the picture shown below, run the following SQL in Grafana. Unlike monthly deployments which are based on the number of deployments, the metric below is based on `deployment days`.

![](assets/images/deployment-frequency-text-5efb6391b4283c21b1e7f4dd1904a4ca_80a92295effa6284.png)

```text
-- Metric 1: Deployment Frequency
with last_few_calendar_months as(
-- construct the last few calendar months within the selected time period in the top-right corner
    SELECT CAST((SYSDATE()-INTERVAL (H+T+U) DAY) AS date) day
    FROM ( SELECT 0 H
            UNION ALL SELECT 100 UNION ALL SELECT 200 UNION ALL SELECT 300
        ) H CROSS JOIN ( SELECT 0 T
            UNION ALL SELECT  10 UNION ALL SELECT  20 UNION ALL SELECT  30
            UNION ALL SELECT  40 UNION ALL SELECT  50 UNION ALL SELECT  60
            UNION ALL SELECT  70 UNION ALL SELECT  80 UNION ALL SELECT  90
        ) T CROSS JOIN ( SELECT 0 U
            UNION ALL SELECT   1 UNION ALL SELECT   2 UNION ALL SELECT   3
            UNION ALL SELECT   4 UNION ALL SELECT   5 UNION ALL SELECT   6
            UNION ALL SELECT   7 UNION ALL SELECT   8 UNION ALL SELECT   9
        ) U
    WHERE
        (SYSDATE()-INTERVAL (H+T+U) DAY) > $__timeFrom()
),

_production_deployment_days as(
-- When deploying multiple commits in one pipeline, GitLab and BitBucket may generate more than one deployment. However, DevLake consider these deployments as ONE production deployment and use the last one's finished_date as the finished date.
    SELECT
        cdc.cicd_deployment_id as deployment_id,
        max(DATE(cdc.finished_date)) as day
    FROM cicd_deployment_commits cdc
    JOIN project_mapping pm on cdc.cicd_scope_id = pm.row_id and pm.`table` = 'cicd_scopes'
    WHERE
        pm.project_name in (${project})
        and cdc.result = 'SUCCESS'
        and cdc.environment = 'PRODUCTION'
    GROUP BY 1
),

_days_weekly_deploy as(
-- calculate the number of deployment days every week
    SELECT
            date(DATE_ADD(last_few_calendar_months.day, INTERVAL -WEEKDAY(last_few_calendar_months.day) DAY)) as week,
            MAX(if(_production_deployment_days.day is not null, 1, null)) as weeks_deployed,
            COUNT(distinct _production_deployment_days.day) as days_deployed
    FROM
        last_few_calendar_months
        LEFT JOIN _production_deployment_days ON _production_deployment_days.day = last_few_calendar_months.day
    GROUP BY week
    ),

_days_monthly_deploy as(
-- calculate the number of deployment days every month
    SELECT
            date(DATE_ADD(last_few_calendar_months.day, INTERVAL -DAY(last_few_calendar_months.day)+1 DAY)) as month,
            MAX(if(_production_deployment_days.day is not null, 1, null)) as months_deployed,
          COUNT(distinct _production_deployment_days.day) as days_deployed
    FROM
        last_few_calendar_months
        LEFT JOIN _production_deployment_days ON _production_deployment_days.day = last_few_calendar_months.day
    GROUP BY month
    ),

_days_six_months_deploy AS (
  SELECT
    month,
    SUM(days_deployed) OVER (
      ORDER BY month
      ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
    ) AS days_deployed_per_six_months,
    COUNT(months_deployed) OVER (
      ORDER BY month
      ROWS BETWEEN 5 PRECEDING AND CURRENT ROW
    ) AS months_deployed_count,
    ROW_NUMBER() OVER (
      PARTITION BY DATE_FORMAT(month, '%Y-%m') DIV 6
      ORDER BY month DESC
    ) AS rn
  FROM _days_monthly_deploy
),

_median_number_of_deployment_days_per_week_ranks as(
    SELECT *, percent_rank() over(order by days_deployed) as ranks
    FROM _days_weekly_deploy
),

_median_number_of_deployment_days_per_week as(
    SELECT max(days_deployed) as median_number_of_deployment_days_per_week
    FROM _median_number_of_deployment_days_per_week_ranks
    WHERE ranks <= 0.5
),

_median_number_of_deployment_days_per_month_ranks as(
    SELECT *, percent_rank() over(order by days_deployed) as ranks
    FROM _days_monthly_deploy
),

_median_number_of_deployment_days_per_month as(
    SELECT max(days_deployed) as median_number_of_deployment_days_per_month
    FROM _median_number_of_deployment_days_per_month_ranks
    WHERE ranks <= 0.5
),

_days_per_six_months_deploy_by_filter AS (
SELECT
  month,
  days_deployed_per_six_months,
  months_deployed_count
FROM _days_six_months_deploy
WHERE rn%6 = 1
),


_median_number_of_deployment_days_per_six_months_ranks as(
    SELECT *, percent_rank() over(order by days_deployed_per_six_months) as ranks
    FROM _days_per_six_months_deploy_by_filter
),

_median_number_of_deployment_days_per_six_months as(
    SELECT min(days_deployed_per_six_months) as median_number_of_deployment_days_per_six_months, min(months_deployed_count) as is_collected
    FROM _median_number_of_deployment_days_per_six_months_ranks
    WHERE ranks >= 0.5
)

SELECT
  CASE
    WHEN ('$dora_report') = '2023' THEN
            CASE
                WHEN median_number_of_deployment_days_per_week >= 5 THEN CONCAT(median_number_of_deployment_days_per_week, ' deployment days per week(elite)')
                WHEN median_number_of_deployment_days_per_week >= 1 THEN CONCAT(median_number_of_deployment_days_per_week, ' deployment days per week(high)')
                WHEN median_number_of_deployment_days_per_month >= 1 THEN CONCAT(median_number_of_deployment_days_per_month, ' deployment days per month(medium)')
                WHEN median_number_of_deployment_days_per_month < 1 and is_collected is not null THEN CONCAT(median_number_of_deployment_days_per_month, ' deployment days per month(low)')
                ELSE "N/A. Please check if you have collected deployments." END
        WHEN ('$dora_report') = '2021' THEN
            CASE
                WHEN median_number_of_deployment_days_per_week >= 5 THEN CONCAT(median_number_of_deployment_days_per_week, ' deployment days per week(elite)')
                WHEN median_number_of_deployment_days_per_month >= 1 THEN CONCAT(median_number_of_deployment_days_per_month, ' deployment days per month(high)')
                WHEN median_number_of_deployment_days_persix_months >= 1 THEN CONCAT(median_number_of_deployment_days_per_six_months, ' deployment days per six months(medium)')
                WHEN median_number_of_deployment_days_per_six_months < 1 and is_collected is not null THEN CONCAT(median_number_of_deployment_days_per_six_months, ' deployment days per six months(low)')
                ELSE "N/A. Please check if you have collected deployments." END
        ELSE 'Invalid dora report'
    END AS 'Deployment Frequency'
FROM _median_number_of_deployment_days_per_week, _median_number_of_deployment_days_per_month, _median_number_of_deployment_days_per_six_months
```

<a id="metrics-deploymentfrequency--how-to-improve"></a>

## How to improve?

- Trunk development. Work in small batches and often merge their work into shared trunks.
- Integrate CI/CD tools for automated deployment
- Improve automated test coverage

- [What is this metric?](#metrics-deploymentfrequency--what-is-this-metric)
- [Why is it important?](#metrics-deploymentfrequency--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-deploymentfrequency--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-deploymentfrequency--how-is-it-calculated)
- [How to improve?](#metrics-deploymentfrequency--how-to-improve)

---

<a id="metrics-leadtimeforchanges"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/LeadTimeForChanges/ -->

<!-- page_index: 65 -->

# DORA - Median Lead Time for Changes

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DORA - Median Lead Time for Changes

<a id="metrics-leadtimeforchanges--what-is-this-metric"></a>

## What is this metric?

The median amount of time for a code change to be deployed into production.

<a id="metrics-leadtimeforchanges--why-is-it-important"></a>

## Why is it important?

This metric measures the time it takes to a code change to the production environment and reflects the speed of software delivery. A lower average change preparation time means that your team is efficient at coding and deploying your project.

<a id="metrics-leadtimeforchanges--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

DORA dashboard. See [live demo](https://grafana-lake.demo.devlake.io/grafana/d/qNo8_0M4z/dora?orgId=1).

<a id="metrics-leadtimeforchanges--how-is-it-calculated"></a>

## How is it calculated?

This metric is quite similar to [PR Cycle Time](#metrics-prcycletime). The difference is that 'Lead Time for Changes' uses a different method to filter PRs.

1. Find the PRs' associated deployment commits whose finished\_date falls into the time range that users select.
2. Find the associated pull requests of the commits diff between two consecutive successful `deployment commits` in the production environment.
3. Calculate the PRs' median cycle time. This will be the Median Lead Time for Changes.

![](assets/images/lead-time-for-changes-definition-5afbf8a11fd6b47dcacd316d42f50a12_4bdde7b04878a419.png)

[PR cycle time](#metrics-prcycletime) is pre-calculated by the `dora` plugin during every data collection. You can find it in `pr_cycle_time` in [table.project\_pr\_metrics](https://devlake.apache.org/docs/DataModels/DevLakeDomainLayerSchema/#project_pr_metrics) of DevLake's database.

Below are the 2023 DORA benchmarks for different development teams from Google's report. However, it's difficult to tell which group a team falls into when the team's median lead time for changes is `between one week and one month`. Therefore, DevLake provides its own benchmarks to address this problem:

<table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>Less than one day</td><td>Less than one day</td></tr><tr><td>High performers</td><td>Between one day and one week</td><td>Between one day and one week</td></tr><tr><td>Medium performers</td><td>Between one week and one month</td><td>Between one week and one month</td></tr><tr><td>Low performers</td><td>Between one week and one month</td><td>More than one month</td></tr></tbody></table>

*Source: 2023 Accelerate State of DevOps, Google*

> [!INFO]
> **Click to expand or collapse 2021 DORA benchmarks**
> <table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>Less than one hour</td><td>Less than one hour</td></tr><tr><td>High performers</td><td>Between one day and one week</td><td>Less than one week</td></tr><tr><td>Medium performers</td><td>Between one month and six months</td><td>Between one week and six months</td></tr><tr><td>Low performers</td><td>More than six months</td><td>More than six months</td></tr></tbody></table>
>
> *Source: 2021 Accelerate State of DevOps, Google*

**Data Sources Required**

- `Deployments` from Jenkins, GitLab CI, GitHub Action, BitBucket Pipelines, Webhook, etc.
- `Pull Requests` from GitHub PRs, GitLab MRs, BitBucket PRs, Azure DevOps PRs, etc.

**Transformation Rules Required**

Define `deployment` in [data transformations](https://devlake.apache.org/docs/Configuration/Tutorial#step-3---add-transformations-optional) while configuring the blueprint of a project to let DevLake know what CI records can be regarded as deployments.

**SQL Queries**

If you want to measure the monthly trend of median lead time for changes as the picture shown below, run the following SQL in Grafana.

![](assets/images/lead-time-for-changes-monthly-7086f1b85f30342aa7385a1baaa026d1_f85d7591c3d6b0a2.jpeg)

```text
-- Metric 2: median change lead time per month
with _pr_stats as (
-- get the cycle time of PRs deployed by the deployments finished each month
    SELECT
        distinct pr.id,
        date_format(cdc.finished_date,'%y/%m') as month,
        ppm.pr_cycle_time
    FROM
        pull_requests pr
        join project_pr_metrics ppm on ppm.id = pr.id
        join project_mapping pm on pr.base_repo_id = pm.row_id and pm.`table` = 'repos'
        join cicd_deployment_commits cdc on ppm.deployment_commit_id = cdc.id
    WHERE
        pm.project_name in (${project:sqlstring}+'')
        and pr.merged_date is not null
        and ppm.pr_cycle_time is not null
        and $__timeFilter(cdc.finished_date)
),

_find_median_clt_each_month_ranks as(
    SELECT *, percent_rank() over(PARTITION BY month order by pr_cycle_time) as ranks
    FROM _pr_stats
),

_clt as(
    SELECT month, max(pr_cycle_time) as median_change_lead_time
    FROM _find_median_clt_each_month_ranks
    WHERE ranks <= 0.5
    group by month
)

SELECT
    cm.month,
    case
        when _clt.median_change_lead_time is null then 0
        else _clt.median_change_lead_time/60 end as median_change_lead_time_in_hour
FROM
    calendar_months cm
    LEFT JOIN _clt on cm.month = _clt.month
  WHERE $__timeFilter(cm.month_timestamp)
```

If you want to measure in which category your team falls as in the picture shown below, run the following SQL in Grafana.

![](assets/images/lead-time-for-changes-text-b81d2d8be9003977a5784df68450821a_960f2120f43ff462.png)

```text
-- Metric 2: median lead time for changes
with _pr_stats as (
-- get the cycle time of PRs deployed by the deployments finished in the selected period
    SELECT
        distinct pr.id,
        ppm.pr_cycle_time
    FROM
        pull_requests pr
        join project_pr_metrics ppm on ppm.id = pr.id
        join project_mapping pm on pr.base_repo_id = pm.row_id and pm.`table` = 'repos'
        join cicd_deployment_commits cdc on ppm.deployment_commit_id = cdc.id
    WHERE
      pm.project_name in (${project})
        and pr.merged_date is not null
        and ppm.pr_cycle_time is not null
        and $__timeFilter(cdc.finished_date)
),

_median_change_lead_time_ranks as(
    SELECT *, percent_rank() over(order by pr_cycle_time) as ranks
    FROM _pr_stats
),

_median_change_lead_time as(
-- use median PR cycle time as the median change lead time
    SELECT max(pr_cycle_time) as median_change_lead_time
    FROM _median_change_lead_time_ranks
    WHERE ranks <= 0.5
)

SELECT
  CASE
    WHEN ('$dora_report') = '2023' THEN
            CASE
                WHEN median_change_lead_time < 24 * 60 THEN CONCAT(round(median_change_lead_time/60,1), "(elite)")
                WHEN median_change_lead_time < 7 * 24 * 60 THEN CONCAT(round(median_change_lead_time/60,1), "(high)")
                WHEN median_change_lead_time < 30 * 24 * 60 THEN CONCAT(round(median_change_lead_time/60,1), "(medium)")
                WHEN median_change_lead_time >= 30 * 24 * 60 THEN CONCAT(round(median_change_lead_time/60,1), "(low)")
                ELSE "N/A. Please check if you have collected deployments/pull_requests."
                END
    WHEN ('$dora_report') = '2021' THEN
          CASE
                WHEN median_change_lead_time < 60 THEN CONCAT(round(median_change_lead_time/60,1), "(elite)")
                WHEN median_change_lead_time < 7 * 24 * 60 THEN CONCAT(round(median_change_lead_time/60,1), "(high)")
                WHEN median_change_lead_time < 180 * 24 * 60 THEN CONCAT(round(median_change_lead_time/60,1), "(medium)")
                WHEN median_change_lead_time >= 180 * 24 * 60 THEN CONCAT(round(median_change_lead_time/60,1), "(low)")
                ELSE "N/A. Please check if you have collected deployments/pull_requests."
                END
        ELSE 'Invalid dora report'
    END AS median_change_lead_time
FROM _median_change_lead_time
```

<a id="metrics-leadtimeforchanges--how-to-improve"></a>

## How to improve?

- Break requirements into smaller, more manageable deliverables
- Optimize the code review process
- "Shift left", start QA early and introduce more automated tests
- Integrate CI/CD tools to automate the deployment process

- [What is this metric?](#metrics-leadtimeforchanges--what-is-this-metric)
- [Why is it important?](#metrics-leadtimeforchanges--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-leadtimeforchanges--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-leadtimeforchanges--how-is-it-calculated)
- [How to improve?](#metrics-leadtimeforchanges--how-to-improve)

---

<a id="metrics-faileddeploymentrecoverytime"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/FailedDeploymentRecoveryTime/ -->

<!-- page_index: 66 -->

# DORA - Failed Deployment Recovery Time

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DORA - Failed Deployment Recovery Time

<a id="metrics-faileddeploymentrecoverytime--what-is-this-metric"></a>

## What is this metric?

The time of changes that were made to a code that then resulted in incidents, rollbacks, or any type of production failure.

<a id="metrics-faileddeploymentrecoverytime--why-is-it-important"></a>

## Why is it important?

This metric is crucial in evaluating the resilience and efficiency of a team's deployment process. A shorter recovery time indicates a team's ability to swiftly detect issues, troubleshoot them, and restore the system to a functional state, minimizing downtime and impact on end-users.

<a id="metrics-faileddeploymentrecoverytime--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

DORA dashboard. See [live demo](https://grafana-lake.demo.devlake.io/grafana/d/qNo8_0M4z/dora?orgId=1).

<a id="metrics-faileddeploymentrecoverytime--how-is-it-calculated"></a>

## How is it calculated?

The time from deployment to the incident corresponding to deployment is resolved. For example, if a deployment finishes at 10:00 AM and causes an incident at 10:20. Then, the incident gets resolved at 11:00 AM. The failed deployment recovery time is one hour.

![](assets/images/fdrt-995d8559fd24da1d59a4db749fdbfddd_071bbf704492b9d4.png)

Below are the 2023 DORA benchmarks for different development teams from Google's report. However, it's difficult to tell which group a team falls into when the team's failed deployment recovery time is `between one week and six months`. Therefore, DevLake provides its own benchmarks to address this problem:

<table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>Less than one hour</td><td>Less than one hour</td></tr><tr><td>High performers</td><td>Less than one day</td><td>Less than one day</td></tr><tr><td>Medium performers</td><td>Between one day and one week</td><td>Between one day and one week</td></tr><tr><td>Low performers</td><td>More than six months</td><td>More than one week</td></tr></tbody></table>

*Source: 2023 Accelerate State of DevOps, Google*

**Data Sources Required**

- `Deployments` from Jenkins, GitLab CI, GitHub Action, BitBucket Pipelines, Webhook, etc.
- `Incidents` from Jira issues, GitHub issues, TAPD issues, PagerDuty Incidents, Webhook, etc.

**Transformation Rules Required**

Define `deployment` and `incident` in [data transformations](#configuration-tutorial--step-3-add-transformations-optional) while configuring the blueprint of a project to let DevLake know what CI/issue records can be regarded as deployments or incidents.

**SQL Queries**

If you want to measure the monthly trend of the Failed Deployment Recovery Time as the picture shown below, run the following SQL in Grafana.

![](assets/images/failed-deployment-recovery-time-9cb2dbd76f01d76677cbce7815d8414b_39a8ff7f62db1bca.png)

```text
--  ***** 2023 report ***** --
--  Metric 4: Failed deployment recovery time
with _deployments as (
    SELECT
        cdc.cicd_deployment_id as deployment_id,
        max(cdc.finished_date) as deployment_finished_date
    FROM
        cicd_deployment_commits cdc
        JOIN project_mapping pm on cdc.cicd_scope_id = pm.row_id and pm.`table` = 'cicd_scopes'
    WHERE
        pm.project_name in ($project)
        and cdc.result = 'SUCCESS'
        and cdc.environment = 'PRODUCTION'
    GROUP BY 1
    HAVING $__timeFilter(max(cdc.finished_date))
),

_incidents_for_deployments as (
    SELECT
        i.id as incident_id,
        i.created_date as incident_create_date,
        i.resolution_date as incident_resolution_date,
        fd.deployment_id as caused_by_deployment,
        fd.deployment_finished_date,
        date_format(fd.deployment_finished_date,'%y/%m') as deployment_finished_month
    FROM
        issues i
        left join project_issue_metrics pim on i.id = pim.id
        join _deployments fd on pim.deployment_id = fd.deployment_id
    WHERE
        i.type = 'INCIDENT'
    and $__timeFilter(i.resolution_date)
),

_recovery_time_ranks as (
    SELECT *, percent_rank() over(PARTITION BY deployment_finished_month order by TIMESTAMPDIFF(MINUTE, deployment_finished_date, incident_resolution_date)) as ranks
    FROM _incidents_for_deployments
),

_median_recovery_time as (
    SELECT deployment_finished_month, max(TIMESTAMPDIFF(MINUTE, deployment_finished_date, incident_resolution_date)) as median_recovery_time
    FROM _recovery_time_ranks
    WHERE ranks <= 0.5
    GROUP BY deployment_finished_month
),

_metric_recovery_time_2023_report as (
    SELECT
    cm.month,
    case
        when m.median_recovery_time is null then 0
        else m.median_recovery_time/60
        end as median_recovery_time_in_hour
    FROM
    calendar_months cm
    LEFT JOIN _median_recovery_time m on cm.month = m.deployment_finished_month
    WHERE $__timeFilter(cm.month_timestamp)
)

SELECT
  cm.month,
  CASE
    WHEN '${dora_report}' = '2023' THEN mrt.median_recovery_time_in_hour
  END AS '${title_value} In Hours'
FROM
  calendar_months cm
  LEFT JOIN _metric_recovery_time_2023_report mrt ON cm.month = mrt.month
WHERE
  $__timeFilter(cm.month_timestamp)
```

If you want to measure in which category your team falls into as in the picture shown below, run the following SQL in Grafana.

![](assets/images/failed-deployment-recovery-time-text-53d49a25dc677446f388bd1ec32585a2_3b94d43ab797f224.png)

```text
--  ***** 2023 report ***** --
--  Metric 4: Failed deployment recovery time
with _deployments as (
    SELECT
        cdc.cicd_deployment_id as deployment_id,
        max(cdc.finished_date) as deployment_finished_date
    FROM
        cicd_deployment_commits cdc
        JOIN project_mapping pm on cdc.cicd_scope_id = pm.row_id and pm.`table` = 'cicd_scopes'
    WHERE
        pm.project_name in ($project)
        and cdc.result = 'SUCCESS'
        and cdc.environment = 'PRODUCTION'
    GROUP BY 1
    HAVING $__timeFilter(max(cdc.finished_date))
),

_incidents_for_deployments as (
    SELECT
        i.id as incident_id,
        i.created_date as incident_create_date,
        i.resolution_date as incident_resolution_date,
        fd.deployment_id as caused_by_deployment,
        fd.deployment_finished_date,
        date_format(fd.deployment_finished_date,'%y/%m') as deployment_finished_month
    FROM
        issues i
        left join project_issue_metrics pim on i.id = pim.id
        join _deployments fd on pim.deployment_id = fd.deployment_id
    WHERE
        i.type = 'INCIDENT'
    and $__timeFilter(i.resolution_date)
),

_recovery_time_ranks as (
    SELECT *, percent_rank() over(order by TIMESTAMPDIFF(MINUTE, deployment_finished_date, incident_resolution_date)) as ranks
    FROM _incidents_for_deployments
),

_median_recovery_time as (
    SELECT max(TIMESTAMPDIFF(MINUTE, deployment_finished_date, incident_resolution_date)) as median_recovery_time
    FROM _recovery_time_ranks
    WHERE ranks <= 0.5
),

_metric_recovery_time_2023_report as(
    SELECT
    CASE
        WHEN ('$dora_report') = '2023' THEN
        CASE
            WHEN median_recovery_time < 60 THEN  CONCAT(round(median_recovery_time/60,1), "(elite)")
            WHEN median_recovery_time < 24 * 60 THEN CONCAT(round(median_recovery_time/60,1), "(high)")
            WHEN median_recovery_time < 7 * 24 * 60 THEN CONCAT(round(median_recovery_time/60,1), "(medium)")
            WHEN median_recovery_time >= 7 * 24 * 60 THEN CONCAT(round(median_recovery_time/60,1), "(low)")
            ELSE "N/A. Please check if you have collected incidents."
        END
    END AS median_recovery_time
    FROM
    _median_recovery_time
)

SELECT
  median_recovery_time AS median_time_in_hour
FROM
  _metric_recovery_time_2023_report
WHERE
  ('$dora_report') = '2023'
```

<a id="metrics-faileddeploymentrecoverytime--how-to-improve"></a>

## How to improve?

- Add unit tests for all new feature
- "Shift left", start QA early and introduce more automated tests
- Enforce code review if it is not strictly executed
- Improve your user support workflow to cope with incidents more efficiently

- [What is this metric?](#metrics-faileddeploymentrecoverytime--what-is-this-metric)
- [Why is it important?](#metrics-faileddeploymentrecoverytime--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-faileddeploymentrecoverytime--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-faileddeploymentrecoverytime--how-is-it-calculated)
- [How to improve?](#metrics-faileddeploymentrecoverytime--how-to-improve)

---

<a id="metrics-mttr"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/MTTR/ -->

<!-- page_index: 67 -->

# DORA - Median Time to Restore Service

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DORA - Median Time to Restore Service

<a id="metrics-mttr--what-is-this-metric"></a>

## What is this metric?

The time to restore service after service incidents, rollbacks, or any type of production failure happened.

<a id="metrics-mttr--why-is-it-important"></a>

## Why is it important?

This metric is essential to measure the disaster control capability of your team and the robustness of the software.

<a id="metrics-mttr--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

DORA dashboard. See [live demo](https://grafana-lake.demo.devlake.io/grafana/d/qNo8_0M4z/dora?orgId=1).

<a id="metrics-mttr--how-is-it-calculated"></a>

## How is it calculated?

MTTR = The median [incident age](#metrics-incidentage) of all incidents.

If you have three incidents that happened in the given data range, one lasting 1 hour, one lasting 3 hours and one lasting 4 hours. Your MTTR will be: median(1, 3, 4) = 3 hours.

Below are the 2023 DORA benchmarks for different development teams from Google's report. However, it's difficult to tell which group a team falls into when the team's median time to restore service is `between one week and six months`. Therefore, DevLake provides its own benchmarks to address this problem:

<table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>Less than one hour</td><td>Less than one hour</td></tr><tr><td>High performers</td><td>Less than one day</td><td>Less than one day</td></tr><tr><td>Medium performers</td><td>Between one day and one week</td><td>Between one day and one week</td></tr><tr><td>Low performers</td><td>More than six months</td><td>More than one week</td></tr></tbody></table>

> [!INFO]
> **Click to expand or collapse 2021 DORA benchmarks**
> <table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>Less than one hour</td><td>Less than one hour</td></tr><tr><td>High performers</td><td>Less than one day</td><td>Less than one day</td></tr><tr><td>Medium performers</td><td>Between one day and one week</td><td>Between one day and one week</td></tr><tr><td>Low performers</td><td>More than six months</td><td>More than one week</td></tr></tbody></table>
>
> *Source: 2021 Accelerate State of DevOps, Google*

**Data Sources Required**

- `Incidents` from Jira issues, GitHub issues, TAPD issues, PagerDuty Incidents, etc.

**Transformation Rules Required**

Define `incident` in [data transformations](https://devlake.apache.org/docs/Configuration/Tutorial#step-3---add-transformations-optional) while configuring the blueprint of a project to let DevLake know what CI/issue records can be regarded as deployments or incidents.

**SQL Queries**

If you want to measure the monthly trend of the Median Time to Restore Service as the picture shown below, run the following SQL in Grafana.

![](assets/images/mttr-monthly-71f037b867c1f94523aa18ca7cd2e497_58c9a0e81490d7dc.jpeg)

```text
-- Metric 3: median time to restore service - MTTR
-- Metric 3: median time to restore service - MTTR
with _incidents as (
-- get the number of incidents created each month
    SELECT
      distinct i.id,
        date_format(i.created_date,'%y/%m') as month,
        cast(lead_time_minutes as signed) as lead_time_minutes
    FROM
        issues i
      join board_issues bi on i.id = bi.issue_id
      join boards b on bi.board_id = b.id
      join project_mapping pm on b.id = pm.row_id and pm.`table` = 'boards'
    WHERE
      pm.project_name in (${project:sqlstring}+'')
        and i.type = 'INCIDENT'
        and i.lead_time_minutes is not null
),

_find_median_mttr_each_month_ranks as(
    SELECT *, percent_rank() over(PARTITION BY month order by lead_time_minutes) as ranks
    FROM _incidents
),

_mttr as(
    SELECT month, max(lead_time_minutes) as median_time_to_resolve
    FROM _find_median_mttr_each_month_ranks
    WHERE ranks <= 0.5
    GROUP BY month
)

SELECT
    cm.month,
    case
        when m.median_time_to_resolve is null then 0
        else m.median_time_to_resolve/60 end as median_time_to_resolve_in_hour
FROM
    calendar_months cm
    LEFT JOIN _mttr m on cm.month = m.month
  WHERE $__timeFilter(cm.month_timestamp)
```

If you want to measure in which category your team falls into as in the picture shown below, run the following SQL in Grafana.

![](assets/images/mttr-text-bd3e5e9835de07a63e2ec1533a16be7f_c9127ebb4515e5e2.png)

```text
--  ***** 2023 report ***** --
--  Metric 4: Failed deployment recovery time
with _incidents as (
-- get the incidents created within the selected time period in the top-right corner
    SELECT
      distinct i.id,
        cast(lead_time_minutes as signed) as lead_time_minutes
    FROM
        issues i
      join board_issues bi on i.id = bi.issue_id
      join boards b on bi.board_id = b.id
      join project_mapping pm on b.id = pm.row_id and pm.`table` = 'boards'
    WHERE
      pm.project_name in (${project})
        and i.type = 'INCIDENT'
        and $__timeFilter(i.created_date)
),

_median_mttr_ranks as(
    SELECT *, percent_rank() over(order by lead_time_minutes) as ranks
    FROM _incidents
),

_median_mttr as(
    SELECT max(lead_time_minutes) as median_time_to_resolve
    FROM _median_mttr_ranks
    WHERE ranks <= 0.5
),

_metric_mttr_2021_report as(
    SELECT
    CASE
        WHEN ('$dora_report') = '2021' THEN
            CASE
                WHEN median_time_to_resolve < 60 THEN CONCAT(round(median_time_to_resolve/60,1), "(elite)")
                WHEN median_time_to_resolve < 24 * 60 THEN CONCAT(round(median_time_to_resolve/60,1), "(high)")
                WHEN median_time_to_resolve < 7 * 24 * 60 THEN CONCAT(round(median_time_to_resolve/60,1), "(medium)")
                WHEN median_time_to_resolve >= 7 * 24 * 60 THEN CONCAT(round(median_time_to_resolve/60,1), "(low)")
                ELSE "N/A. Please check if you have collected incidents."
            END
    END AS median_time_to_resolve
    FROM
        _median_mttr
)

SELECT
  median_time_to_resolve AS median_time_to_resolve
FROM
  _metric_mttr_2021_report
WHERE
  ('$dora_report') = '2021'
```

<a id="metrics-mttr--how-to-improve"></a>

## How to improve?

- Use automated tools to quickly report failure
- Prioritize recovery when a failure happens
- Establish a go-to action plan to respond to failures immediately
- Reduce the deployment time for failure-fixing

- [What is this metric?](#metrics-mttr--what-is-this-metric)
- [Why is it important?](#metrics-mttr--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-mttr--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-mttr--how-is-it-calculated)
- [How to improve?](#metrics-mttr--how-to-improve)

---

<a id="metrics-cfr"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CFR/ -->

<!-- page_index: 68 -->

# DORA - Change Failure Rate

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DORA - Change Failure Rate

<a id="metrics-cfr--what-is-this-metric"></a>

## What is this metric?

The percentage of changes that were made to a code that then resulted in incidents, rollbacks, or any type of production failure.

<a id="metrics-cfr--why-is-it-important"></a>

## Why is it important?

Unlike Deployment Frequency and Lead Time for Changes that measure the throughput, Change Failure Rate measures the stability and quality of software delivery. A low CFR reflects a bad end-user experience as the production failure is relatively high.

<a id="metrics-cfr--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in

DORA dashboard. See [live demo](https://grafana-lake.demo.devlake.io/grafana/d/qNo8_0M4z/dora?orgId=1).

<a id="metrics-cfr--how-is-it-calculated"></a>

## How is it calculated?

The number of deployments affected by incidents/total number of deployments. For example, if there are five deployments and two deployments cause one or more incidents, that is a 40% change failure rate.

![](assets/images/cfr-definition-94d92cc75f857f183443ad5390d31d65_905723ec0f096f50.png)

When there are multiple deployments triggered by one pipeline, tools like GitLab and BitBucket will generate more than one deployment. In these cases, DevLake will consider these deployments as ONE deployment and use the last deployment's finished date as the deployment finished date.

Below are the 2023 DORA benchmarks for different development teams from Google's report. However, it's difficult to tell which group a team falls into when the team's change failure rate is between 15% and 64%. Therefore, DevLake provides its own benchmarks to address this problem:

<table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>5%</td><td>(0, 5%]</td></tr><tr><td>High performers</td><td>10%</td><td>(5%, 10%]</td></tr><tr><td>Medium performers</td><td>15%</td><td>(10%, 15%]</td></tr><tr><td>Low performers</td><td>64%</td><td>(15%, 100%]</td></tr></tbody></table>

> [!INFO]
> **Click to expand or collapse 2021 DORA benchmarks**
> <table><thead><tr><th>Groups</th><th>Benchmarks</th><th>DevLake Benchmarks</th></tr></thead><tbody><tr><td>Elite performers</td><td>0%-15%</td><td>(0, 15%]</td></tr><tr><td>High performers</td><td>16%-30%</td><td>(16%, 20%]</td></tr><tr><td>Medium performers</td><td>16%-30%</td><td>(21%, 30%]</td></tr><tr><td>Low performers</td><td>16%-30%</td><td>(30%, 100%]</td></tr></tbody></table>
>
> *Source: 2021 Accelerate State of DevOps, Google*

**Data Sources Required**

- `Deployments` from Jenkins, GitLab CI, GitHub Action, BitBucket Pipelines, or Webhook, etc.
- `Incidents` from Jira issues, GitHub issues, TAPD issues, PagerDuty Incidents, etc.

**Transformation Rules Required**

Define `deployment` and `incident` in [data transformations](https://devlake.apache.org/docs/Configuration/Tutorial#step-3---add-transformations-optional) while configuring the blueprint of a project to let DevLake know what CI/issue records can be regarded as deployments or incidents.

**SQL Queries**

If you want to measure the monthly trend of Change Failure Rate, run the following SQL in Grafana.

![](assets/images/cfr-monthly-78a4c5dd7640417bb22742a2b3453912_550b5a5bdb8eca12.jpeg)

```text
-- Metric 4: change failure rate per month
with _deployments as (
-- When deploying multiple commits in one pipeline, GitLab and BitBucket may generate more than one deployment. However, DevLake consider these deployments as ONE production deployment and use the last one's finished_date as the finished date.
    SELECT
        cdc.cicd_deployment_id as deployment_id,
        max(cdc.finished_date) as deployment_finished_date
    FROM
        cicd_deployment_commits cdc
        JOIN project_mapping pm on cdc.cicd_scope_id = pm.row_id and pm.`table` = 'cicd_scopes'
    WHERE
        pm.project_name in (${project:sqlstring}+'')
        and cdc.result = 'SUCCESS'
        and cdc.environment = 'PRODUCTION'
    GROUP BY 1
    HAVING $__timeFilter(max(cdc.finished_date))
),

_failure_caused_by_deployments as (
-- calculate the number of incidents caused by each deployment
    SELECT
        d.deployment_id,
        d.deployment_finished_date,
        count(distinct case when i.type = 'INCIDENT' then d.deployment_id else null end) as has_incident
    FROM
        _deployments d
        left join project_issue_metrics pim on d.deployment_id = pim.deployment_id
        left join issues i on pim.id = i.id
    GROUP BY 1,2
),

_change_failure_rate_for_each_month as (
    SELECT
        date_format(deployment_finished_date,'%y/%m') as month,
        case
            when count(deployment_id) is null then null
            else sum(has_incident)/count(deployment_id) end as change_failure_rate
    FROM
        _failure_caused_by_deployments
    GROUP BY 1
)

SELECT
    cm.month,
    cfr.change_failure_rate
FROM
    calendar_months cm
    LEFT JOIN _change_failure_rate_for_each_month cfr on cm.month = cfr.month
    WHERE $__timeFilter(cm.month_timestamp)
```

If you want to measure in which category your team falls, run the following SQL in Grafana.

![](assets/images/cfr-text-b4ada4fdcf2f1f21302ffef16869514e_2375cf56aeb3a3b7.png)

```text
-- Metric 3: change failure rate
with _deployments as (
-- When deploying multiple commits in one pipeline, GitLab and BitBucket may generate more than one deployment. However, DevLake consider these deployments as ONE production deployment and use the last one's finished_date as the finished date.
    SELECT
        cdc.cicd_deployment_id as deployment_id,
        max(cdc.finished_date) as deployment_finished_date
    FROM
        cicd_deployment_commits cdc
        JOIN project_mapping pm on cdc.cicd_scope_id = pm.row_id and pm.`table` = 'cicd_scopes'
    WHERE
        pm.project_name in (${project})
        and cdc.result = 'SUCCESS'
        and cdc.environment = 'PRODUCTION'
    GROUP BY 1
    HAVING $__timeFilter(max(cdc.finished_date))
),

_failure_caused_by_deployments as (
-- calculate the number of incidents caused by each deployment
    SELECT
        d.deployment_id,
        d.deployment_finished_date,
        count(distinct case when i.type = 'INCIDENT' then d.deployment_id else null end) as has_incident
    FROM
        _deployments d
        left join project_issue_metrics pim on d.deployment_id = pim.deployment_id
        left join issues i on pim.id = i.id
    GROUP BY 1,2
),

_change_failure_rate as (
    SELECT
        case
            when count(deployment_id) is null then null
            else sum(has_incident)/count(deployment_id) end as change_failure_rate
    FROM
        _failure_caused_by_deployments
),

_is_collected_data as(
    SELECT
        CASE
        WHEN COUNT(i.id) = 0 AND COUNT(cdc.id) = 0 THEN 'No All'
        WHEN COUNT(i.id) = 0 THEN 'No Incidents'
        WHEN COUNT(cdc.id) = 0 THEN 'No Deployments'
        END AS is_collected
FROM
    (SELECT 1) AS dummy
LEFT JOIN
    issues i ON i.type = 'INCIDENT'
LEFT JOIN
    cicd_deployment_commits cdc ON 1=1
)


SELECT
  CASE
    WHEN ('$dora_report') = '2023' THEN
            CASE
                WHEN is_collected = "No All"  THEN "N/A. Please check if you have collected deployments/incidents."
                WHEN is_collected = "No Incidents"  THEN "N/A. Please check if you have collected incidents."
                WHEN is_collected = "No Deployments"  THEN "N/A. Please check if you have collected deployments."
                WHEN change_failure_rate <= .05 THEN CONCAT(round(change_failure_rate*100,1), "%(elite)")
                WHEN change_failure_rate <= .10 THEN CONCAT(round(change_failure_rate*100,1), "%(high)")
                WHEN change_failure_rate <= .15 THEN CONCAT(round(change_failure_rate*100,1), "%(medium)")
                WHEN change_failure_rate > .15 THEN CONCAT(round(change_failure_rate*100,1), "%(low)")
                ELSE "N/A. Please check if you have collected deployments/incidents."
                END
        WHEN ('$dora_report') = '2021' THEN
            CASE
              WHEN is_collected = "No All"  THEN "N/A. Please check if you have collected deployments/incidents."
                WHEN is_collected = "No Incidents"  THEN "N/A. Please check if you have collected incidents."
                WHEN is_collected = "No Deployments"  THEN "N/A. Please check if you have collected deployments."
                WHEN change_failure_rate <= .15 THEN CONCAT(round(change_failure_rate*100,1), "%(elite)")
                WHEN change_failure_rate <= .20 THEN CONCAT(round(change_failure_rate*100,1), "%(high)")
                WHEN change_failure_rate <= .30 THEN CONCAT(round(change_failure_rate*100,1), "%(medium)")
                WHEN change_failure_rate > .30 THEN CONCAT(round(change_failure_rate*100,1), "%(low)")
                ELSE "N/A. Please check if you have collected deployments/incidents."
                END
        ELSE 'Invalid dora report'
    END AS change_failure_rate
FROM
    _change_failure_rate, _is_collected_data
```

<a id="metrics-cfr--how-to-improve"></a>

## How to improve?

- Add unit tests for all new feature
- "Shift left", start QA early and introduce more automated tests
- Enforce code review if it's not strictly executed

- [What is this metric?](#metrics-cfr--what-is-this-metric)
- [Why is it important?](#metrics-cfr--why-is-it-important)
- [Which dashboard(s) does it exist in](#metrics-cfr--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-cfr--how-is-it-calculated)
- [How to improve?](#metrics-cfr--how-to-improve)

---

<a id="metrics-cqissuecount"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CQIssueCount/ -->

<!-- page_index: 69 -->

# Code Quality Issue Count

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Code Quality Issue Count

<a id="metrics-cqissuecount--what-is-this-metric"></a>

## What is this metric?

This metric is a the total number of issues found in a project by SonarQube. It includes various types of issues such as bugs, vulnerabilities, code smells, and security hotspots. This metric is collected from SonarQube, check [this doc](https://docs.sonarqube.org/latest/user-guide/metric-definitions/#issues) for detailed definition.

<a id="metrics-cqissuecount--why-is-it-important"></a>

## Why is it important?

Issue provides information about potential problems or issues in the code. Issues can include bugs, vulnerabilities, and code smells, which can all affect the maintainability, reliability, and security of the codebase. By identifying and addressing issues, developers can improve the quality of their code and reduce technical debt. Additionally, tracking issues over time can help to identify trends and measure progress in improving code quality.

<a id="metrics-cqissuecount--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [SonarQube](https://devlake.apache.org/livedemo/DataSources/SonarQube)

<a id="metrics-cqissuecount--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the total number of cq\_issues.

**Data Sources Required**

This metric relies on issues collected from SonarQube.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find issues in specific projects, eg. 'project1' and 'project2'.

1. To get the issue count of 'BUG', please add the condition `type = BUG`

```text
SELECT
  count(*) as 'Bugs'
FROM cq_issues
WHERE
  $__timeFilter(created_date)
  and  project_key in ('project1', 'project2')
  and `type` = 'BUG'
ORDER BY created_date
```

2. To get the issue count of 'VULNERABILITY', please add the condition `type = VULNERABILITY`

```text
SELECT
  count(*) as 'Vulnerabilities'
FROM cq_issues
WHERE
  $__timeFilter(created_date)
  and project_key in ('project1', 'project2')
  and `type` = 'VULNERABILITY'
ORDER BY created_date
```

3. To get the issue count of 'HOTSPOTS', please add the condition `type = HOTSPOTS`

```text
SELECT
  COUNT(IF(status = 'TO_REVIEW', 1, NULL)) AS 'Security Hotspots'
FROM cq_issues
WHERE
  $__timeFilter(created_date)
  and project_key in ('project1', 'project2')
  and `type` = 'HOTSPOTS'
ORDER BY created_date
```

```text
SELECT
  CONCAT(ROUND(COUNT(IF(status != 'TO_REVIEW', 1, NULL)) / COUNT(*) * 100, 2), '%') AS 'Reviewed'
FROM cq_issues
WHERE
  $__timeFilter(created_date)
  and project_key in ('project1', 'project2')
  and `type` = 'HOTSPOTS'
ORDER BY created_date
```

4. To get the issue count of 'CODE\_SMELL', please add the condition `type = CODE_SMELL`

```text
SELECT
    COUNT(if(type = 'CODE_SMELL', 1, null)) as 'Code Smells'
FROM cq_issues
WHERE
  $__timeFilter(created_date)
  and project_key in ('project1', 'project2')
```

![](assets/images/issue-type-count-1142fdb52475a7a8ff09a75f359aef74_1bba15bbc7bbdccc.png)

- [What is this metric?](#metrics-cqissuecount--what-is-this-metric)
- [Why is it important?](#metrics-cqissuecount--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-cqissuecount--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-cqissuecount--how-is-it-calculated)

---

<a id="metrics-cqtest"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CQTest/ -->

<!-- page_index: 70 -->

# Code Quality Test

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Code Quality Test

<a id="metrics-cqtest--what-is-this-metric"></a>

## What is this metric?

This metric is the number of unit tests that have been executed against the code. This metric is collected from SonarQube, check [this doc](https://docs.sonarqube.org/latest/user-guide/metric-definitions/#tests) for detailed definition.

<a id="metrics-cqtest--why-is-it-important"></a>

## Why is it important?

Test is an indicator used to indicate the test coverage of the code. This means that SonarQube checks that your code contains enough test cases to cover the various paths and branches in your code. This metric can help you understand the extent of your code test coverage, thereby determining your code quality and stability.

<a id="metrics-cqtest--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [SonarQube](https://devlake.apache.org/livedemo/DataSources/SonarQube)

<a id="metrics-cqtest--how-is-it-calculated"></a>

## How is it calculated?

This SQL query retrieves the test coverage percentage for the lines to cover in a project from the cq\_file\_metrics table in SonarQube. The query calculates the percentage by subtracting the number of uncovered lines from the total number of lines to cover, then dividing the result by the total number of lines to cover, and multiplying by 100. The result is rounded to one decimal point and displayed as a percentage. Additionally, the query also includes a message that shows the total number of lines to cover in thousands.

**Data Sources Required**

This metric relies on file\_metrics collected from SonarQube.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find unit tests that have been executed against the code in specific projects, eg. 'project1' and 'project2'.

```text
SELECT
  CONCAT(ROUND((sum(lines_to_cover) - sum(uncovered_lines)) / sum(lines_to_cover) * 100, 1), '% ', 'Coverage on ', ROUND(sum(lines_to_cover) / 1000, 0),'k Lines to cover')
FROM cq_file_metrics
WHERE
  project_key in ('project1', 'project2')
```

- [What is this metric?](#metrics-cqtest--what-is-this-metric)
- [Why is it important?](#metrics-cqtest--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-cqtest--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-cqtest--how-is-it-calculated)

---

<a id="metrics-cqmaintainability-debt"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CQMaintainability-Debt/ -->

<!-- page_index: 71 -->

# Code Quality Maintainability-Debt

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Code Quality Maintainability-Debt

<a id="metrics-cqmaintainability-debt--what-is-this-metric"></a>

## What is this metric?

This metric is a measure of effort to fix all code smells. This metric is collected from SonarQube, check [this doc](https://docs.sonarqube.org/latest/user-guide/metric-definitions/#maintainability) for detailed definition.

<a id="metrics-cqmaintainability-debt--why-is-it-important"></a>

## Why is it important?

It helps developers and project managers understand the costs and risks associated with maintaining the codebase. High levels of technical debt can lead to more bugs, slower development cycles, and higher maintenance costs over time. By monitoring technical debt and working to reduce it, developers can ensure that their code is easier to maintain, more reliable, and more scalable.

<a id="metrics-cqmaintainability-debt--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [SonarQube](https://devlake.apache.org/livedemo/DataSources/SonarQube)

<a id="metrics-cqmaintainability-debt--how-is-it-calculated"></a>

## How is it calculated?

This SQL query calculates the total technical debt in days for all issues in the SonarQube instance. check [this doc](https://docs.sonarqube.org/latest/user-guide/metric-definitions/#maintainability) for detailed info.

**Data Sources Required**

This metric relies on issues collected from SonarQube.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find effort to fix all code smells in specific projects, eg. 'project1' and 'project2'.

```text
SELECT
  CONCAT(ROUND(SUM(debt) / (8 * 60), 0), ' days') AS 'Debt'
FROM cq_issues
WHERE
  $__timeFilter(created_date)
  project_key in ('project1', 'project2')
```

- [What is this metric?](#metrics-cqmaintainability-debt--what-is-this-metric)
- [Why is it important?](#metrics-cqmaintainability-debt--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-cqmaintainability-debt--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-cqmaintainability-debt--how-is-it-calculated)

---

<a id="metrics-cqduplicatedblocks"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CQDuplicatedBlocks/ -->

<!-- page_index: 72 -->

# Code Quality Duplicated Blocks

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Code Quality Duplicated Blocks

<a id="metrics-cqduplicatedblocks--what-is-this-metric"></a>

## What is this metric?

This metric is the number of duplicated blocks of lines. This metric is collected from SonarQube, check [this doc](https://docs.sonarqube.org/latest/user-guide/metric-definitions/#duplications) for detailed definition.

<a id="metrics-cqduplicatedblocks--why-is-it-important"></a>

## Why is it important?

Duplicated Blocks is a code metric that measures the amount of duplicated code in a project. Duplicated blocks are sequences of code that are identical or nearly identical to each other, and can occur within a single file or across multiple files. Duplicated code can make the codebase harder to maintain, increase the risk of bugs and errors, and make it more difficult to understand and modify the code. Identifying and removing duplicated code can improve the maintainability, reliability, and readability of the codebase, and reduce the risk of introducing bugs or errors in the future.

<a id="metrics-cqduplicatedblocks--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [SonarQube](https://devlake.apache.org/livedemo/DataSources/SonarQube)

<a id="metrics-cqduplicatedblocks--how-is-it-calculated"></a>

## How is it calculated?

This metric is calculated by counting the total number of duplicated\_blocks.

**Data Sources Required**

This metric relies on file metrics collected from SonarQube.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find duplicated blocks of lines in specific projects, eg. 'project1' and 'project2'.

```text
SELECT
  sum(duplicated_blocks)
FROM cq_file_metrics
WHERE
  project_key in ('project1', 'project2')
```

- [What is this metric?](#metrics-cqduplicatedblocks--what-is-this-metric)
- [Why is it important?](#metrics-cqduplicatedblocks--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-cqduplicatedblocks--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-cqduplicatedblocks--how-is-it-calculated)

---

<a id="metrics-cqduplicatedlines"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Metrics/CQDuplicatedLines/ -->

<!-- page_index: 73 -->

# Code Quality Duplicated Lines

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Code Quality Duplicated Lines

<a id="metrics-cqduplicatedlines--what-is-this-metric"></a>

## What is this metric?

This metric is the number of files involved in duplications. This metric is collected from SonarQube, check [this doc](https://docs.sonarqube.org/latest/user-guide/metric-definitions/#duplications) for detailed definition.

<a id="metrics-cqduplicatedlines--why-is-it-important"></a>

## Why is it important?

Duplicated lines are individual lines of code that are identical or nearly identical to each other, and can occur within a single file or across multiple files. Duplicated code can make the codebase harder to maintain, increase the risk of bugs and errors, and make it more difficult to understand and modify the code. Identifying and removing duplicated code can improve the maintainability, reliability, and readability of the codebase, and reduce the risk of introducing bugs or errors in the future.

<a id="metrics-cqduplicatedlines--which-dashboards-does-it-exist-in"></a>

## Which dashboard(s) does it exist in?

- [SonarQube](https://devlake.apache.org/livedemo/DataSources/SonarQube)

<a id="metrics-cqduplicatedlines--how-is-it-calculated"></a>

## How is it calculated?

This SQL query calculates the percentage of duplicated lines in a project, as well as the total number of lines in the project.
The sum(duplicated\_lines) represents the total number of duplicated lines in the project, while sum(num\_of\_lines) represents the total number of lines of code. These two values are divided and multiplied by 100 to get the percentage of duplicated lines in the project.

**Data Sources Required**

This metric relies on file metrics collected from SonarQube.

**Data Transformation Required**

N/A

**SQL Queries**

The following SQL shows how to find the number of files involved in duplications in specific projects, eg. 'project1' and 'project2'.

```text
SELECT
  CONCAT(ROUND(sum(duplicated_lines) / sum(num_of_lines) * 100, 1), '% ', 'Duplications on ', ROUND(sum(ncloc) / 1000, 0),'k Lines')
FROM cq_file_metrics
WHERE
  project_key in ('project1', 'project2')
```

- [What is this metric?](#metrics-cqduplicatedlines--what-is-this-metric)
- [Why is it important?](#metrics-cqduplicatedlines--why-is-it-important)
- [Which dashboard(s) does it exist in?](#metrics-cqduplicatedlines--which-dashboards-does-it-exist-in)
- [How is it calculated?](#metrics-cqduplicatedlines--how-is-it-calculated)

---

<a id="datamodels"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DataModels/ -->

<!-- page_index: 74 -->

# Data Models

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Data Models

[## 📄️ Domain Layer Schema

The data tables to query engineering metrics](#datamodels-devlakedomainlayerschema)

[## 📄️ Tool Layer Schema

Extract raw data into a relational schema for each specific tool](#datamodels-toollayerschema)

[## 📄️ Raw Layer Schema

Caches raw API responses from data source plugins](#datamodels-rawlayerschema)

[## 📄️ System Tables

Stores DevLake's own entities](#datamodels-systemtables)

---

<a id="datamodels-devlakedomainlayerschema"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DataModels/DevLakeDomainLayerSchema/ -->

<!-- page_index: 75 -->

# Domain Layer Schema

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Domain Layer Schema

<a id="datamodels-devlakedomainlayerschema--summary"></a>

## Summary

This document describes Apache DevLake's domain layer schema.

Referring to DevLake's [architecture](#overview-architecture), the data in the domain layer is transformed from the data in the tool layer. The tool layer schema is based on the data from specific tools such as Jira, GitHub, GitLab, Jenkins, etc. The domain layer schema can be regarded as an abstraction of tool-layer schemas.

![](assets/images/arch-dataflow-domain-93047a532b60cd864bdddf8f279b785d_8e0aaea2f49032e7.svg)

DevLake Dataflow

<a id="datamodels-devlakedomainlayerschema--use-cases"></a>

## Use Cases

1. [All metrics](#metrics) from pre-built dashboards are based on this data schema.
2. As a user, you can create your own customized dashboards based on this data schema.
3. As a contributor, you can refer to this data schema while working on the ETL logic when adding/updating data source plugins.

<a id="datamodels-devlakedomainlayerschema--data-models"></a>

## Data Models

This is the up-to-date domain layer schema for DevLake. Tables (entities) are categorized into 5 domains.

1. Issue tracking: Jira issues, GitHub issues, GitLab issues, etc.
2. Source code management: Git/GitHub/GitLab commits and refs(tags and branches), etc.
3. Code review: GitHub PRs, GitLab MRs, etc.
4. CI/CD: Jenkins jobs & builds, etc.
5. Code Quality: SonarQube issues, hotspots, file metrics, etc.
6. Cross-domain: entities that map entities from different domains to break data isolation.

<a id="datamodels-devlakedomainlayerschema--schema-diagram"></a>

### Schema Diagram

![Domain Layer Schema](assets/images/domain-layer-schema-diagram-96dac99687ade10d70a9d4865022f50e_364de201ce389fa1.svg)

When reading the schema, you'll notice that many tables' primary key is called `id`. Unlike auto-increment id or UUID, `id` is a string composed of several parts to uniquely identify similar entities (e.g. repo) from different platforms (e.g. GitHub/GitLab) and allow them to co-exist in a single table.

Tables that end with WIP are still under development.

<a id="datamodels-devlakedomainlayerschema--naming-conventions"></a>

### Naming Conventions

1. The name of a table is in plural form. E.g. boards, issues, etc.
2. The name of a table which describe the relation between 2 entities is in the form of [BigEntity in singular form]\_[SmallEntity in plural form]. E.g. board\_issues, sprint\_issues, pull\_request\_comments, etc.
3. Value of the field in enum type are in capital letters. E.g. [table.issues.type](#datamodels-devlakedomainlayerschema--issues) has 3 values, REQUIREMENT, BUG, INCIDENT. Values that are phrases, such as 'IN\_PROGRESS' of [table.issues.status](#datamodels-devlakedomainlayerschema--issues), are separated with underscore '\_'.

<a id="datamodels-devlakedomainlayerschema--how-to-customize-data-models"></a>

## How to Customize Data Models

Apache DevLake provides 2 plugins:

- [customize](https://devlake.apache.org/docs/Plugins/customize): to create/delete columns in the domain layer schema with the data extracted from [raw layer tables](https://devlake.apache.org/docs/Overview/Architecture/#dataflow)
- [dbt](https://devlake.apache.org/docs/Plugins/customize): to transform data based on the domain layer schema and generate new tables

<a id="datamodels-devlakedomainlayerschema--dwd-entities-data-warehouse-detail"></a>

## DWD Entities - (Data Warehouse Detail)

<a id="datamodels-devlakedomainlayerschema--domain-1-issue-tracking"></a>

### Domain 1 - Issue Tracking

<a id="datamodels-devlakedomainlayerschema--issues"></a>

#### issues

An `issue` is the abstraction of GitHub/GitLab/BitBucket/Jira/TAPD/Zentao... issues.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">An issue's <code>id</code> is composed of &lt; plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..." <ul><li>For Github issues, a Github issue's id is like "github:GithubIssues:&lt; GithubIssueId &gt;". E.g. 'github:GithubIssues:1049355647'</li> <li>For Jira issues, a Github repo's id is like "jira:JiraIssues:&lt; JiraSourceId &gt;:&lt; JiraIssueId &gt;". E.g. 'jira:JiraIssues:1:10063'. &lt; JiraSourceId &gt; is used to identify which jira source the issue came from, since DevLake users can import data from several different Jira instances at the same time.</li></ul></td><td align="left">PK</td></tr><tr><td align="left"><code>issue_key</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The key of this issue. For example, the key of this Github <a href="https://github.com/apache/incubator-devlake/issues/1145" rel="noopener noreferrer" target="_blank">issue</a> is 1145.</td><td align="left"></td></tr><tr><td align="left"><code>url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The url of the issue. It's a web address in most cases.</td><td align="left"></td></tr><tr><td align="left"><code>title</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The title of an issue</td><td align="left"></td></tr><tr><td align="left"><code>description</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The detailed description/summary of an issue</td><td align="left"></td></tr><tr><td align="left"><code>type</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The standard type of this issue. There are 3 standard types: <ul><li>REQUIREMENT: this issue is a feature</li><li>BUG: this issue is a bug found during test</li><li>INCIDENT: this issue is a bug found after release</li></ul>The 3 standard types are transformed from the original types of an issue. The transformation rule is set in the '.env' file or 'config-ui' before data collection. For issues with an original type that has not mapped to a standard type, the value of <code>type</code> will be the issue's original type.</td><td align="left"></td></tr><tr><td align="left"><code>original_type</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original type of an issue.</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The standard statuses of this issue. There are 3 standard statuses: <ul><li> TODO: this issue is in backlog or to-do list</li><li>IN_PROGRESS: this issue is in progress</li><li>DONE: this issue is resolved or closed</li></ul>The 3 standard statuses are transformed from the original statuses of an issue. The transformation rule: <ul><li>For Jira issue status: transformed from the Jira issue's <code>statusCategory</code>. Jira issue has 3 default status categories: 'To Do', 'In Progress', 'Done'.</li><li>For Github issue status: <ul><li>open -&gt; TODO</li><li>closed -&gt; DONE</li></ul></li></ul></td><td align="left"></td></tr><tr><td align="left"><code>original_status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original status of an issue.</td><td align="left"></td></tr><tr><td align="left"><code>story_point</code></td><td align="left">double</td><td align="left"></td><td align="left">The story point of this issue. Only certain types(e.g. story) of Jira or TAPD issues has story points</td><td align="left"></td></tr><tr><td align="left"><code>priority</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The priority of the issue</td><td align="left"></td></tr><tr><td align="left"><code>urgency</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The urgency of the issue</td><td align="left"></td></tr><tr><td align="left"><code>component</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The component a bug-issue affects. This field only supports Github plugin for now. The value is transformed from Github issue labels by the rules set according to the user's configuration of .env by end users during DevLake installation.</td><td align="left"></td></tr><tr><td align="left"><code>severity</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The severity level of a bug-issue. This field only supports Github plugin for now. The value is transformed from Github issue labels by the rules set according to the user's configuration of .env by end users during DevLake installation.</td><td align="left"></td></tr><tr><td align="left"><code>parent_issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of its parent issue</td><td align="left"></td></tr><tr><td align="left"><code>epic_key</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The key of the epic this issue belongs to. For tools with no epic-type issues such as Github and GitLab, this field is default to an empty string</td><td align="left"></td></tr><tr><td align="left"><code>original_estimate_minutes</code></td><td align="left">int</td><td align="left"></td><td align="left">The original estimation of the time allocated for this issue</td><td align="left"></td></tr><tr><td align="left"><code>time_spent_minutes</code></td><td align="left">int</td><td align="left"></td><td align="left">The original estimation of the time allocated for this issue</td><td align="left"></td></tr><tr><td align="left"><code>time_remaining_minutes</code></td><td align="left">int</td><td align="left"></td><td align="left">The remaining time to resolve the issue</td><td align="left"></td></tr><tr><td align="left"><code>creator_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of issue creator</td><td align="left"></td></tr><tr><td align="left"><code>creator_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the creator</td><td align="left"></td></tr><tr><td align="left"><code>assignee_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of issue assignee.<ul><li>For Github issues: this is the last assignee of an issue if the issue has multiple assignees</li><li>For Jira issues: this is the assignee of the issue at the time of collection</li></ul></td><td align="left"></td></tr><tr><td align="left"><code>assignee_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the assignee</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time issue created</td><td align="left"></td></tr><tr><td align="left"><code>updated_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The last time issue gets updated</td><td align="left"></td></tr><tr><td align="left"><code>resolution_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time the issue changes to 'DONE'.</td><td align="left"></td></tr><tr><td align="left"><code>lead_time_minutes</code></td><td align="left">int</td><td align="left"></td><td align="left">Describes the cycle time from issue creation to issue resolution.<ul><li>For issues whose type = 'REQUIREMENT' and status = 'DONE', lead_time_minutes = resolution_date - created_date. The unit is minute.</li><li>For issues whose type != 'REQUIREMENT' or status != 'DONE', lead_time_minutes is null</li></ul></td><td align="left"></td></tr><tr><td align="left"><code>original_project</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the original project this issue belongs to. Transformed from a Jira project's name, a TAPD workspace's name, etc.</td><td align="left"></td></tr><tr><td align="left"><code>icon_url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The url of the issue icon.</td><td align="left"></td></tr><tr><td align="left"><code>x_custom_field_1</code></td><td align="left">It depends on the type of the converted field</td><td align="left">-</td><td align="left">The value of the custom field. This field is available when utilizing the <a href="https://devlake.apache.org/docs/Plugins/customize">customize</a> plugin to convert Jira's raw layer fields to the domain layer fields.</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_assignees"></a>

#### issue\_assignees

This table shows the assignee(s) of issues. Multiple entries can exist per issue, as a GitHub/TAPD issue may have multiple assignees at the same time. This table can be used to get the detailed information of all issue assignees.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">FK_issues.id</td></tr><tr><td align="left"><code>assignee_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Assignee ID</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>assignee_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Assignee Name</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_labels"></a>

#### issue\_labels

This table shows the labels of issues. Multiple entries can exist per issue. This table can be used to filter issues by label name.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>label_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Label name. Collect from GitHub issue labels or Jira issue labels</td><td align="left"></td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">FK_issues.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_comments"></a>

#### issue\_comments

This table shows the comments of issues. Only GitHub and TAPD issue comments are collected. Issues with multiple comments are shown as multiple records. This table can be used to calculate *metric - issue response time*.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The unique id of a comment</td><td align="left">PK</td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">FK_issues.id</td></tr><tr><td align="left"><code>account_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the account who made the comment</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>body</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The body/detail of the comment</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The creation date of the comment</td><td align="left"></td></tr><tr><td align="left"><code>updated_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The update date of the comment</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_changelogs"></a>

#### issue\_changelogs

This table shows the changelogs of issues. Only Jira issue changelogs are collected for now. Issues with multiple changelogs are shown as multiple records. This is transformed from Jira or TAPD changelogs.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The unique id of an issue changelog</td><td align="left">PK</td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">FK_issues.id</td></tr><tr><td align="left"><code>author_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the user who made the change</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>author_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the user who made the change</td><td align="left"></td></tr><tr><td align="left"><code>field_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of changed field</td><td align="left"></td></tr><tr><td align="left"><code>field_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of changed field</td><td align="left"></td></tr><tr><td align="left"><code>original_from_value</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The original value of the changed field</td><td align="left"></td></tr><tr><td align="left"><code>original_to_value</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The new value of the changed field</td><td align="left"></td></tr><tr><td align="left"><code>from_value</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The transformed/standardized original value of the changed field</td><td align="left"></td></tr><tr><td align="left"><code>to_value</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The transformed/standardized new value of the changed field</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The creation date of the changelog</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_worklogs"></a>

#### issue\_worklogs

This table shows the work logged under issues. Only Jira issue worklogs are collected for now. Usually, an issue has multiple worklogs logged by different developers.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the worklog.</td><td align="left">PK</td></tr><tr><td align="left"><code>author_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the author who logged the work</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>comment</code></td><td align="left">longtext</td><td align="left">255</td><td align="left">The comment made while logging the work.</td><td align="left"></td></tr><tr><td align="left"><code>time_spent_minutes</code></td><td align="left">int</td><td align="left"></td><td align="left">The time logged. The unit of value is normalized to minute. E.g. 1d =) 480, 4h30m =) 270</td><td align="left"></td></tr><tr><td align="left"><code>logged_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time of this logging action</td><td align="left"></td></tr><tr><td align="left"><code>started_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">Start time of the worklog</td><td align="left"></td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">FK_issues.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_relationships"></a>

#### issue\_relationships

This table shows the metadata of information about relationships between issues.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">PK</td></tr><tr><td align="left"><code>source_issue_id</code></td><td align="left">int</td><td align="left"></td><td align="left">ID of the source issue in the relationship</td><td align="left"></td></tr><tr><td align="left"><code>target_issue_id</code></td><td align="left">int</td><td align="left"></td><td align="left">ID of the target issue in the relationship</td><td align="left"></td></tr><tr><td align="left"><code>original_type</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Type of relationship between the source and target issues</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_repo_commits"></a>

#### issue\_repo\_commits

This table shows the metadata of commits made to a code repository associated with specific issues.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">PK</td></tr><tr><td align="left"><code>repo_url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The URL of the code repository</td><td align="left">PK</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The SHA of the commit.</td><td align="left">PK</td></tr><tr><td align="left"><code>host</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The hostname</td><td align="left"></td></tr><tr><td align="left"><code>namespace</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The namespace of the code repository</td><td align="left"></td></tr><tr><td align="left"><code>repo_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the code repository.</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--issue_custom_array_fields"></a>

#### issue\_custom\_array\_fields

The table below presents the custom fields of issues in an 'array' type. This table is available when utilizing the [customize](https://devlake.apache.org/docs/Plugins/customize) plugin to convert Jira's raw layer fields to the domain layer fields. It is important to note that custom fields of other types will be displayed as 'x\_custom\_field\_1' in the [issues](#datamodels-devlakedomainlayerschema--issues) table.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue ID</td><td align="left">PK</td></tr><tr><td align="left"><code>field_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The ID of the array field of the issue. It starts with 'x_', e.g. x_product_lines.</td><td align="left"></td></tr><tr><td align="left"><code>field_value</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The value of the array field. E.g. DevLake, DevSea, DevPond.</td><td align="left"></td></tr></tbody></table>

You can refer to the following SQL to use this table.

```text
-- query issue count by product lines
select
  count(*) as issue_count, field_value
from issues
  join issue_custom_array_fields on issues.id = issue_custom_array_fields.issue_id
where field_id = 'x_product_lines'
group by field_value;
```

<a id="datamodels-devlakedomainlayerschema--boards"></a>

#### boards

A `board` is an issue list or a collection of issues. It's the abstraction of a Jira board, a Jira or TAPD project, a [GitHub repo's issue list](https://github.com/apache/incubator-devlake/issues) or a GitLab repo's issue list. This table can be used to filter issues by the boards they belong to.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A board's <code>id</code> is composed of "&lt; plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..." <ul><li>For a Github repo's issue list, the board id is like "&lt; github &gt;:&lt; GithubRepos &gt;:&lt; ConnectionId &gt;:&lt; GithubRepoId &gt;". E.g. "github:GithubRepo:384111310"</li> <li>For a Jira Board, the id is like "&lt; jira &gt;:&lt; JiraSourceId &gt;&lt; JiraBoards &gt;:&lt; ConnectionId &gt;:&lt; JiraBoardsId &gt;". E.g. "jira:1:JiraBoards:1:12"</li></ul></td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the board. Note: the board name of a Github repo 'apache/incubator-devlake' is 'apache/incubator-devlake', representing the <a href="https://github.com/apache/incubator-devlake/issues" rel="noopener noreferrer" target="_blank">default issue list</a>.</td><td align="left"></td></tr><tr><td align="left"><code>description</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The description of the board.</td><td align="left"></td></tr><tr><td align="left"><code>url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The url of the board. E.g. <a href="https://github.com/apache/incubator-devlake/issues" rel="noopener noreferrer" target="_blank">https://github.com/apache/incubator-devlake/issues</a></td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">Board creation time</td><td align="left"></td></tr><tr><td align="left"><code>type</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Identify scrum and non-scrum board</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--board_issues"></a>

#### board\_issues

This table shows the relation between boards and issues. This table can be used to filter issues by board.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>board_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Board id</td><td align="left">FK_boards.id</td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue id</td><td align="left">FK_issues.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--sprints"></a>

#### sprints

A `sprint` is the abstraction of Jira sprints, TAPD iterations and GitHub milestones. A sprint contains a list of
issues.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A sprint's <code>id</code> is composed of "&lt; plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..."<ul><li>A sprint in a Github repo is a milestone, the sprint id is like "&lt; github &gt;:&lt; GithubRepos &gt;:&lt; GithubRepoId &gt;:&lt; milestoneNumber &gt;". Eg. The id for this <a href="https://github.com/apache/incubator-devlake/milestone/5" rel="noopener noreferrer" target="_blank">sprint</a> is "github:GithubRepo:384111310:5"</li><li>For a Jira Board, the id is like "&lt; jira &gt;:&lt; JiraSourceId &gt;&lt; JiraBoards &gt;:&lt; JiraBoardsId &gt;". Eg. "jira:1:JiraBoards:12"</li></ul></td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of sprint. For Github projects, the sprint name is the milestone name. For instance, 'v0.10.0 - Introduce Temporal to DevLake' is the name of this <a href="https://github.com/apache/incubator-devlake/milestone/5" rel="noopener noreferrer" target="_blank">sprint</a>.</td><td align="left"></td></tr><tr><td align="left"><code>url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The url of sprint.</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">There are 3 statuses of a sprint:<ul><li>CLOSED: a completed sprint</li><li>ACTIVE: a sprint started but not completed</li><li>FUTURE: a sprint that has not started</li><li>SUSPENDED: a sprint that has been suspended</li></ul></td><td align="left"></td></tr><tr><td align="left"><code>started_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The start time of a sprint</td><td align="left"></td></tr><tr><td align="left"><code>ended_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The planned/estimated end time of a sprint. It's usually set when planning a sprint.</td><td align="left"></td></tr><tr><td align="left"><code>completed_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The actual time to complete a sprint.</td><td align="left"></td></tr><tr><td align="left"><code>original_board_id</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The id of board where the sprint first created. This field is not null only when this entity is transformed from Jira sprints.
In Jira, sprint and board entities have 2 types of relation:<ul><li>A sprint is created based on a specific board. In this case, board(1):(n)sprint. This field <code>original_board_id</code> is used to show the relation.</li><li>A sprint can be mapped to multiple boards, a board can also show multiple sprints. In this case, board(n):(n)sprint. This relation is shown in <a href="#datamodels-devlakedomainlayerschema--board_sprints">table.board_sprints</a></li></ul></td><td align="left">FK_boards.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--sprint_issues"></a>

#### sprint\_issues

This table shows the relation between sprints and issues that have been added to sprints. This table can be used to show
metrics such as *'ratio of unplanned issues'*, *'completion rate of sprint issues'*, etc

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>sprint_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Sprint id</td><td align="left">FK_sprints.id</td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue id</td><td align="left">FK_issues.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--board_sprints"></a>

#### board\_sprints

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>board_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Board id</td><td align="left">FK_boards.id</td></tr><tr><td align="left"><code>sprint_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Sprint id</td><td align="left">FK_sprints.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--domain-2-source-code-management"></a>

### Domain 2 - Source Code Management

<a id="datamodels-devlakedomainlayerschema--repos"></a>

#### repos

GitHub, GitLab or BitBucket repositories.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A repo's <code>id</code> is composed of "&lt; plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..."
For example, a Github repo's id is like "&lt; github &gt;:&lt; GithubRepos &gt;:&lt; ConnectionId &gt;:&lt; GithubRepoId &gt;". E.g. 'github:GithubRepos:1:384111310'</td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The name of repo. For DevLake, it's 'apache/incubator-devlake'</td><td align="left"></td></tr><tr><td align="left"><code>description</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The description of repo.</td><td align="left"></td></tr><tr><td align="left"><code>url</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The url of repo. E.g. <a href="https://github.com/apache/incubator-devlake" rel="noopener noreferrer" target="_blank">https://github.com/apache/incubator-devlake</a></td><td align="left"></td></tr><tr><td align="left"><code>owner_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the owner of repo</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>language</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The major language of repo. E.g. The language for apache/incubator-devlake is 'Go'</td><td align="left"></td></tr><tr><td align="left"><code>forked_from</code></td><td align="left">longtext</td><td align="left"></td><td align="left">Empty unless the repo is a fork in which case it contains the <code>id</code> of the repo the repo is forked from.</td><td align="left"></td></tr><tr><td align="left"><code>deleted</code></td><td align="left">tinyint</td><td align="left">1</td><td align="left">0: repo is active 1: repo has been deleted</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">Repo creation date</td><td align="left"></td></tr><tr><td align="left"><code>updated_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">Last full update was done for this repo</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--repo_commits"></a>

#### repo\_commits

The commits belong to the history of a repository. More than one repo can share the same commits if one is a fork of the
other.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Repo id</td><td align="left">FK_repos.id</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">Commit sha</td><td align="left">FK_commits.sha</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--refs"></a>

#### refs

A ref is the abstraction of a branch or tag.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A ref's <code>id</code> is composed of "&lt; plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..."
For example, a Github ref is composed of "github:GithubRepos:&lt; GithubRepoId &gt;:&lt; RefUrl &gt;". E.g. The id of release v5.3.0 of PingCAP/TiDB project is 'github:GithubRepos:384111310:refs/tags/v5.3.0' A repo's <code>id</code> is composed of "&lt; plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..."</td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the ref. E.g. '<a href="https://github.com/apache/incubator-devlake/tree/v0.9.3" rel="noopener noreferrer" target="_blank">refs/tags/v0.9.3</a>' or 'origin/main'</td><td align="left"></td></tr><tr><td align="left"><code>repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of repo this ref belongs to</td><td align="left">FK_repos.id</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit this ref points to at the time of collection</td><td align="left"></td></tr><tr><td align="left"><code>is_default</code></td><td align="left">tinyint</td><td align="left">1</td><td align="left"><ul><li>0: not the default branch</li><li>1: the ref is the default branch. By the definition of <a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch" rel="noopener noreferrer" target="_blank">Github</a>, the default branch is the base branch for pull requests and code commits.</li></ul></td><td align="left"></td></tr><tr><td align="left"><code>ref_type</code></td><td align="left">varchar</td><td align="left">64</td><td align="left">There are 2 typical types:<ul><li>BRANCH</li><li>TAG</li></ul></td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--commits_diffs"></a>

#### commits\_diffs

This table shows the commits added in a new commit compared to an old commit. This table can be used to support tag-based and deploy-based metrics.

The records of this table are computed by [RefDiff](https://github.com/apache/incubator-devlake/tree/main/backend/plugins/refdiff) plugin. The computation should be manually triggered after using [GitRepoExtractor](https://github.com/apache/incubator-devlake/tree/main/backend/plugins/gitextractor) to collect commits and refs. The algorithm behind is similar to [this](https://github.com/apache/incubator-devlake/compare/v0.8.0%E2%80%A6v0.9.0).

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>new_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit new ref/deployment points to at the time of collection</td><td align="left">PK</td></tr><tr><td align="left"><code>old_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit old ref/deployment points to at the time of collection</td><td align="left">PK</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">One of the added commits in the new ref compared to the old ref/deployment</td><td align="left">PK</td></tr><tr><td align="left"><code>sorting_index</code></td><td align="left">bigint</td><td align="left"></td><td align="left">An index for debugging, please skip it</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--ref_commits"></a>

#### ref\_commits

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>new_ref_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The new ref's id for comparison</td><td align="left">PK</td></tr><tr><td align="left"><code>old_ref_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The old ref's id for comparison</td><td align="left">PK</td></tr><tr><td align="left"><code>new_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit new ref points to at the time of collection</td><td align="left"></td></tr><tr><td align="left"><code>old_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit old ref points to at the time of collection</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--commits"></a>

#### commits

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">One of the added commits in the new ref compared to the old ref</td><td align="left">FK_commits.sha</td></tr><tr><td align="left"><code>message</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Commit message</td><td align="left"></td></tr><tr><td align="left"><code>author_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The value is set with command <code>git config user.name xxxxx</code> commit</td><td align="left"></td></tr><tr><td align="left"><code>author_email</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The value is set with command <code>git config user.email xxxxx</code> author</td><td align="left"></td></tr><tr><td align="left"><code>authored_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The date when this commit was originally made</td><td align="left"></td></tr><tr><td align="left"><code>author_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of commit author</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>committer_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of committer</td><td align="left"></td></tr><tr><td align="left"><code>committer_email</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The email of committer</td><td align="left"></td></tr><tr><td align="left"><code>committed_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The last time the commit gets modified. For example, when rebasing the branch where the commit is in on another branch, the committed_date changes.</td><td align="left"></td></tr><tr><td align="left"><code>committer_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of committer</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>additions</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Added lines of code</td><td align="left"></td></tr><tr><td align="left"><code>deletions</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Deleted lines of code</td><td align="left"></td></tr><tr><td align="left"><code>dev_eq</code></td><td align="left">int</td><td align="left"></td><td align="left">A metric that quantifies the amount of code contribution. The data can be retrieved from <a href="https://github.com/apache/incubator-devlake/tree/main/backend/plugins/ae" rel="noopener noreferrer" target="_blank">AE plugin</a>.</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--commit_files"></a>

#### commit\_files

The files that have been changed by commits.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The <code>id</code> is composed of "&lt; Commit_sha &gt;:&lt; file_path &gt;"</td><td align="left">FK_commits.sha</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">Commit sha</td><td align="left">FK_commits.sha</td></tr><tr><td align="left"><code>file_path</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Path of a changed file in a commit</td><td align="left"></td></tr><tr><td align="left"><code>additions</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The added lines of code in this file by the commit</td><td align="left"></td></tr><tr><td align="left"><code>deletions</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The deleted lines of code in this file by the commit</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--components"></a>

#### components

The components of files extracted from the file paths. This can be used to analyze Git metrics by component.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The repo id</td><td align="left">FK_repos.id</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of component</td><td align="left"></td></tr><tr><td align="left"><code>path_regex</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The regex to extract components from this repo's paths</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--commit_file_components"></a>

#### commit\_file\_components

The relationship between commit\_file and component\_name.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>commit_file_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of commit file</td><td align="left">FK_commit_files.id</td></tr><tr><td align="left"><code>component_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The component name of a file</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--commit_parents"></a>

#### commit\_parents

The parent commit(s) for each commit, as specified by Git.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">commit sha</td><td align="left">FK_commits.sha</td></tr><tr><td align="left"><code>parent_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">Parent commit sha</td><td align="left">FK_commits.sha</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--domain-3-code-review"></a>

### Domain 3 - Code Review

<a id="datamodels-devlakedomainlayerschema--pull_requests"></a>

#### pull\_requests

Pull requests are the abstraction of GitHub pull requests, GitLab merge requests, BitBucket pull requests, etc.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A pull request's <code>id</code> is composed of "&lt; plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..." E.g. For 'github:GithubPullRequests:1347'</td><td align="left"></td></tr><tr><td align="left"><code>title</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The title of pull request</td><td align="left"></td></tr><tr><td align="left"><code>description</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The body/description of pull request</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The PR/MR statuses are standardized to 'OPEN', 'MERGED' and 'CLOSED'. <a href="https://github.com/apache/incubator-devlake/issues/4745" rel="noopener noreferrer" target="_blank">Learn how each plugin's PR statuses are standardized</a>.</td><td align="left"></td></tr><tr><td align="left"><code>original_status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original status of pull requests.</td><td align="left"></td></tr><tr><td align="left"><code>parent_pr_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the parent PR</td><td align="left"></td></tr><tr><td align="left"><code>pull_request_key</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The key of PR. E.g. 1536 is the key of this <a href="https://github.com/apache/incubator-devlake/pull/1563" rel="noopener noreferrer" target="_blank">PR</a></td><td align="left"></td></tr><tr><td align="left"><code>base_repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The repo that will be updated.</td><td align="left"></td></tr><tr><td align="left"><code>head_repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The repo containing the changes that will be added to the base. If the head repository is NULL, this means that the corresponding project had been deleted when DevLake processed the pull request.</td><td align="left"></td></tr><tr><td align="left"><code>author_name</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The author's name of the pull request</td><td align="left"></td></tr><tr><td align="left"><code>author_id</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The author's id of the pull request</td><td align="left"></td></tr><tr><td align="left"><code>url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">the web link of the pull request</td><td align="left"></td></tr><tr><td align="left"><code>type</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The work-type of a pull request.For example: feature-development, bug-fix, docs,etc.</td><td align="left"></td></tr><tr><td align="left"><code>component</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The component this PR affects.
The value is transformed from Github/GitLab pull request labels by configuring <code>GITHUB_PR_COMPONENT</code> in <code>.env</code> file during installation.</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time PR created.</td><td align="left"></td></tr><tr><td align="left"><code>merged_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time PR gets merged. Null when the PR is not merged.</td><td align="left"></td></tr><tr><td align="left"><code>closed_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time PR closed. Null when the PR is not closed.</td><td align="left"></td></tr><tr><td align="left"><code>merge_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">the merge commit of this PR. By the definition of <a href="https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/changing-the-default-branch" rel="noopener noreferrer" target="_blank">Github</a>, when you click the default Merge pull request option on a pull request on Github, all commits from the feature branch are added to the base branch in a merge commit.</td><td align="left">FK_commits.sha</td></tr><tr><td align="left"><code>base_ref</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The branch name in the base repo that will be updated</td><td align="left"></td></tr><tr><td align="left"><code>head_ref</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The branch name in the head repo that contains the changes that will be added to the base</td><td align="left"></td></tr><tr><td align="left"><code>base_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The base commit of this PR.</td><td align="left"></td></tr><tr><td align="left"><code>head_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The head commit of this PR.</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--pull_request_labels"></a>

#### pull\_request\_labels

This table shows the labels of pull request. Multiple entries can exist per pull request. This table can be used to
filter pull requests by label name.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>label_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Label name</td><td align="left"></td></tr><tr><td align="left"><code>pull_request_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Pull request ID</td><td align="left">FK_pull_requests.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--pull_request_commits"></a>

#### pull\_request\_commits

A commit associated with a pull request.

The list is additive. This means if a rebase with commit squashing takes place after the commits of a pull request have been processed, the old commits will not be deleted.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>pull_request_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Pull request id</td><td align="left">FK_pull_requests.id</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">Commit sha</td><td align="left">FK_commits.sha</td></tr><tr><td align="left"><code>commit_author_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the person who authored the commit</td><td align="left"></td></tr><tr><td align="left"><code>commit_author_email</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The email address of the person who authored the commit.</td><td align="left"></td></tr><tr><td align="left"><code>commit_authored_date</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The date and time when the commit was authored.</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--pull_request_comments"></a>

#### pull\_request\_comments

Normal comments, review bodies, reviews' inline comments of GitHub's pull requests or GitLab's merge requests.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Comment id</td><td align="left">PK</td></tr><tr><td align="left"><code>pull_request_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Pull request id</td><td align="left">FK_pull_requests.id</td></tr><tr><td align="left"><code>body</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The body of the comments</td><td align="left"></td></tr><tr><td align="left"><code>account_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The account who made the comment</td><td align="left">FK_accounts.id</td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">Comment creation time</td><td align="left"></td></tr><tr><td align="left"><code>position</code></td><td align="left">int</td><td align="left"></td><td align="left">Deprecated</td><td align="left"></td></tr><tr><td align="left"><code>type</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">- For normal comments: NORMAL  - For review comments, ie. diff/inline comments: DIFF  - For reviews' body (exist in GitHub but not GitLab): REVIEW</td><td align="left"></td></tr><tr><td align="left"><code>review_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Review_id of the comment if the type is <code>REVIEW</code> or <code>DIFF</code></td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Status of the comment</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--domain-4-cicd"></a>

### Domain 4 - CI/CD

<a id="datamodels-devlakedomainlayerschema--cicd_scopes"></a>

#### cicd\_scopes

The entity to filter or group 'cicd\_pipelines'.

- For GitHub: a GitHub repo is converted to a cicd\_scope
- For GitLab: a GitLab project is converted to a cicd\_scope
- For Jenkins: a Jenkins job is converted to a cicd\_scope
- For Bamboo CI: a Bamboo plan is converted to a cicd\_scope

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A cicd_scope's <code>id</code> is composed of "&lt; plugin &gt;:&lt; Entity &gt;:&lt; PluginConnectionId &gt;<!-- -->[:PK1]<!-- -->..."
For example, a GitHub cicd_scope's id is "github:GithubRepos:&lt; GithubConnectionId &gt;:&lt; GithubRepoId &gt;", a Bamboo cicd_scope's id is 'bamboo:BambooPlan:&lt; BambooConnectionId &gt;:&lt; BambooPlanKey &gt;'</td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of cicd_scope.</td><td align="left"></td></tr><tr><td align="left"><code>description</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The description of cicd_scope.</td><td align="left"></td></tr><tr><td align="left"><code>url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The url of cicd_scope. E.g. <a href="https://github.com/apache/incubator-devlake" rel="noopener noreferrer" target="_blank">https://github.com/apache/incubator-devlake</a> or <a href="https://jenkins.xxx.cn/view/PROD/job/OPS_releasev2/" rel="noopener noreferrer" target="_blank">https://jenkins.xxx.cn/view/PROD/job/OPS_releasev2/</a></td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">Creation date of the cicd_scope, nullable</td><td align="left"></td></tr><tr><td align="left"><code>updated_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">Updation date of the cicd_scope, nullable</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cicd_pipelines"></a>

#### cicd\_pipelines

A cicd\_pipeline is the abstraction of a top-level CI/CD execution, e.g. a GitHub workflow run, a GitLab pipeline, a BitBucket pipeline, a Jenkins build, a Bamboo plan build, etc. A cicd\_pipeline contains one or more of cicd\_tasks.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is generated based on details from the original plugin</td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">For gitlab, as there is no name for pipeline, so we use projectId, others have their own name</td><td align="left"></td></tr><tr><td align="left"><code>result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The result of the pipeline. It will be standardized to 'SUCCESS', 'FAILURE', '' in DevLake based on each plugin's possible results.</td><td align="left"></td></tr><tr><td align="left"><code>original_result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_result of the pipeline. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The status of the pipeline. It will be standardized to 'DONE', 'IN_PROGRESS', 'OTHER' in DevLake based on each plugin's possible statues.</td><td align="left"></td></tr><tr><td align="left"><code>original_status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_status of the pipeline. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>type</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The value will be set to 'DEPLOYMENT' if it matched the regex configured in the Scope Config, otherwise it is an empty string.</td><td align="left"></td></tr><tr><td align="left"><code>environment</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The value will be set to 'PRODUCTION' if it matched the regex configured in the Scope Config, otherwise it is an empty string.</td><td align="left"></td></tr><tr><td align="left"><code>duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">how long does this pipeline take</td><td align="left"></td></tr><tr><td align="left"><code>queued_duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">how long does this pipeline take queuing</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">When this pipeline created.</td><td align="left"></td></tr><tr><td align="left"><code>queued_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The queued time of the pipeline.</td><td align="left"></td></tr><tr><td align="left"><code>started_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The started time of the pipeline.</td><td align="left"></td></tr><tr><td align="left"><code>finished_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">When this pipeline finished.</td><td align="left"></td></tr><tr><td align="left"><code>cicd_scope_id</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The id of cicd_scope this pipeline belongs to</td><td align="left">FK_cicd_scopes.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cicd_pipeline_commits"></a>

#### cicd\_pipeline\_commits

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>pipeline_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is generated based on details from the original plugin</td><td align="left">PK</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The commit that triggers this pipeline</td><td align="left">PK</td></tr><tr><td align="left"><code>branch</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The branch that triggers this pipeline</td><td align="left"></td></tr><tr><td align="left"><code>repo_url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left"></td><td align="left"></td></tr><tr><td align="left"><code>repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The repo that this pipeline belongs to</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cicd_tasks"></a>

#### cicd\_tasks

A cicd\_task is the abstraction of the bottom-level CI/CD execution.

- For GitHub: a cicd\_task is a GitHub job run in a GitHub workflow run.
- For GitLab: a cicd\_task is a GitLab job run of a GitLab pipeline run.
- For Jenkins: a cicd\_task is a subtask of a Jenkins build. If a build does not have subtask(s), then the build will also be saved as a cicd\_task in this table.
- For Bamboo CI: a cicd\_task is a Bamboo job build in a Bamboo plan build.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is generated based on details from the original plugin</td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left"></td><td align="left"></td></tr><tr><td align="left"><code>pipeline_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of the cicd_pipeline it belongs to</td><td align="left"></td></tr><tr><td align="left"><code>result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The result of the task. It will be standardized to 'SUCCESS', 'FAILURE', '' in DevLake based on each plugin's possible.</td><td align="left"></td></tr><tr><td align="left"><code>original_result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_result of the task. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The status of the task. It will be standardized to 'DONE', 'IN_PROGRESS', 'OTHER' in DevLake based on each plugin's possible states.</td><td align="left"></td></tr><tr><td align="left"><code>original_status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_status of the task. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>type</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The value will be set to 'DEPLOYMENT' if it matched the regex configured in the Scope Config, otherwise it is an empty string.</td><td align="left"></td></tr><tr><td align="left"><code>environment</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The value will be set to 'PRODUCTION' if it matched the regex configured in the Scope Config, otherwise it is an empty string.</td><td align="left"></td></tr><tr><td align="left"><code>duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">How long does this task take</td><td align="left"></td></tr><tr><td align="left"><code>ququed_duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">How long does this task take queuing</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The created time of the task.</td><td align="left"></td></tr><tr><td align="left"><code>queued_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The queued time of the task.</td><td align="left"></td></tr><tr><td align="left"><code>started_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">When this task started</td><td align="left"></td></tr><tr><td align="left"><code>finished_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">When this task finished</td><td align="left"></td></tr><tr><td align="left"><code>cicd_scope_id</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The id of cicd_scope this task belongs to</td><td align="left">FK_cicd_scopes.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cicd_deployments"></a>

#### cicd\_deployments

A cicd\_deployment refers to a deployment at the project level. In the case where a pipeline run or build deploys across three distinct repositories, it will be categorized as ONE cicd\_deployment while being recorded as THREE separate cicd\_deployment\_commits.
It may come from several sources:

- Domain layer [cicd\_pipelines](#datamodels-devlakedomainlayerschema--cicd_pipelines), such as GitHub workflow runs, GitLab pipelines, Jenkins builds and BitBucket pipelines, etc. Deployments from cicd\_pipelines will be transformed according to the regex configuration set in the Blueprint transformation before adding to this table.
- Tool layer deployments: in v0.20, only the BitBucket\Bamboo\GitLab and GitHub(Use GraphQL APIs) plugins collect the independent deployment entity which you can find in table.\_tool\_bitbucket\_deployments and \_tool\_bamboo\_deploy\_builds, there will be more in the future.
- Deployments pushed directly from webhooks

Additional Notes

- CICD deployments are recorded at the project level, not the repository level.
- CICD deployment commits are individual commits that represent a single deployment across multiple repositories.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The deployment_id of this deployment. The value will be set with <code>id</code> when it comes from webhooks.</td><td align="left">PK</td></tr><tr><td align="left"><code>cicd_scope_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of cicd_scope this deployment belongs to</td><td align="left">FK_cicd_scopes.id</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the deployment</td><td align="left"></td></tr><tr><td align="left"><code>result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The result of the deployment, enum. 'SUCCESS', 'FAILUR'E, ''</td><td align="left"></td></tr><tr><td align="left"><code>original_result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_result of the deployment. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The status of this deployment, enum: 'IN_PROGRESS', 'DONE', 'OTHER'</td><td align="left"></td></tr><tr><td align="left"><code>original_status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_status of the deployment. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>environment</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The environment to deploy, only 'PRODUCTION' deployment will appear in v0.17</td><td align="left"></td></tr><tr><td align="left"><code>original_environment</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The original environment field of the deployment. It appeared since v1.0.</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The created time of the deployment.</td><td align="left"></td></tr><tr><td align="left"><code>queued_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The queued time of the deployment.</td><td align="left"></td></tr><tr><td align="left"><code>started_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The started time of the deployment.</td><td align="left"></td></tr><tr><td align="left"><code>finished_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The finished time of the deployment</td><td align="left"></td></tr><tr><td align="left"><code>duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">The time this deployment takes</td><td align="left"></td></tr><tr><td align="left"><code>ququed_duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">The time this deployment takes queuing</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cicd_deployment_commits"></a>

#### cicd\_deployment\_commits

A cicd\_deployment\_commit is a deployment in a specific repo. A deployment may come from several sources:

- Domain layer [cicd\_pipelines](#datamodels-devlakedomainlayerschema--cicd_pipelines), such as GitHub workflow runs, GitLab pipelines, Jenkins builds and BitBucket pipelines, etc. Deployments from cicd\_pipelines will be transformed according to the regex configuration set in the Blueprint transformation before adding to this table.
- Tool layer deployments: in v0.18, only the BitBucket and Bamboo plugins collect the independent deployment entity which you can find in table.\_tool\_bitbucket\_deployments and \_tool\_bamboo\_deploy\_builds, but there will be more in the future.
- Deployments pushed directly from webhooks

You can query deployments from this table by `SELECT DISTINCT cicd_deployment_id FROM cicd_deployments_commits`.

Normally, one deployment only deploy to one repo. But in some cases, one deployment may deploy in multiple repos with different commits. In these cases, there will be multiple pairs of deployment-commit-repo, appeared in multiple entries in this table.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is the combination of the deployment's id and repo_url, e.g.  - from a GitHub workflow run: github:GithubRun:1:384111310:3521097091:<a href="https://github.com/apache/incubator-devlake" rel="noopener noreferrer" target="_blank">https://github.com/apache/incubator-devlake</a>  - from a Jenkins build, jenkins:JenkinsBuild:1:deploy#7:<a href="https://github.com/apache/incubator-devlake" rel="noopener noreferrer" target="_blank">https://github.com/apache/incubator-devlake</a>  - from a webhook, webhook:1:90489d3951711d72:e6bde456807818c5c78d7b265964d6d48b653af6</td><td align="left">PK</td></tr><tr><td align="left"><code>cicd_scope_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The id of cicd_scope this deployment_commit belongs to</td><td align="left">FK_cicd_scopes.id</td></tr><tr><td align="left"><code>cicd_deployment_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The deployment_id of this deployment_commit. The value will be set with <code>id</code> when it comes from webhooks.</td><td align="left"></td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the deployment</td><td align="left"></td></tr><tr><td align="left"><code>result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The result of the deployment, enum: 'SUCCESS', 'FAILURE', ''</td><td align="left"></td></tr><tr><td align="left"><code>original_result</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_result of the deployment. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The status of this deployment, enum: 'IN_PROGRESS', 'DONE', 'OTHER'</td><td align="left"></td></tr><tr><td align="left"><code>original_status</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The original_status of the deployment. Its value depends on the state of the corresponding entity in the different plugins.</td><td align="left"></td></tr><tr><td align="left"><code>environment</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The environment to deploy</td><td align="left"></td></tr><tr><td align="left"><code>original_environment</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The original environment of the deployment. It appeared since v1.0.</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The created time of the deployment.</td><td align="left"></td></tr><tr><td align="left"><code>queued_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The queued time of the deployment.</td><td align="left"></td></tr><tr><td align="left"><code>started_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The started time of the deployment.</td><td align="left"></td></tr><tr><td align="left"><code>finished_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The finished time of the deployment</td><td align="left"></td></tr><tr><td align="left"><code>duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">The time this deployment takes</td><td align="left"></td></tr><tr><td align="left"><code>queued_duration_sec</code></td><td align="left">double</td><td align="left"></td><td align="left">The time this deployment takes queueing</td><td align="left"></td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit sha that triggers the deployment</td><td align="left"></td></tr><tr><td align="left"><code>ref_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The ref (branch/tag) name of the commit</td><td align="left"></td></tr><tr><td align="left"><code>repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">-</td><td align="left"></td></tr><tr><td align="left"><code>repo_url</code></td><td align="left">varchar</td><td align="left">191</td><td align="left">The url of the repo</td><td align="left"></td></tr><tr><td align="left"><code>prev_success_deployment_commit_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The last successful deployment_commit_id before this one in the same <code>cicd_scope</code>, <code>repo</code> and <code>environment</code>, which is used to calculate the new commits deployed by this deployment, thereby measuring <a href="#metrics-leadtimeforchanges">DORA - change lead time</a>.</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--domain-5-code-quality"></a>

### Domain 5 - Code Quality

The names of tables in the 'Code Quality' domain will start with a prefix cq\_

<a id="datamodels-devlakedomainlayerschema--cq_projects"></a>

#### cq\_projects

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is generated based on details from the original plugin</td><td align="left">PK</td></tr><tr><td align="left"><code>name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the project in SonarQube</td><td align="left"></td></tr><tr><td align="left"><code>qualifier</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The type of project. Examples include "TRK" for regular projects and "VW" for views</td><td align="left"></td></tr><tr><td align="left"><code>visibility</code></td><td align="left">varchar</td><td align="left">64</td><td align="left">The visibility of the project. Examples include "public" and "private"</td><td align="left"></td></tr><tr><td align="left"><code>last_analysis_date</code></td><td align="left">datatime</td><td align="left">3</td><td align="left">The date and time of the most recent analysis of the project</td><td align="left"></td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">varchar</td><td align="left">128</td><td align="left">It represents the version number or code version identifier of a project</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cq_issues"></a>

#### cq\_issues

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is generated based on details from the original plugin</td><td align="left">PK</td></tr><tr><td align="left"><code>rule</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The key of the rule that the issue is violating</td><td align="left"></td></tr><tr><td align="left"><code>severity</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The severity level of the issue</td><td align="left"></td></tr><tr><td align="left"><code>component</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The name of the component where the issue was found</td><td align="left"></td></tr><tr><td align="left"><code>project_key</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The key of the project that the issue belongs to</td><td align="left"></td></tr><tr><td align="left"><code>line</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The line number where the issue was found</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The status of the issue</td><td align="left"></td></tr><tr><td align="left"><code>message</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The message associated with the issue</td><td align="left"></td></tr><tr><td align="left"><code>debt</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The estimated time required to fix the issue</td><td align="left"></td></tr><tr><td align="left"><code>effort</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The effort required to fix the issue</td><td align="left"></td></tr><tr><td align="left"><code>commit_author_email</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The email address of the author of the commit that introduced the issue</td><td align="left"></td></tr><tr><td align="left"><code>assignee</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The person assigned to fix the issue</td><td align="left"></td></tr><tr><td align="left"><code>hash</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A hash code for the issue</td><td align="left"></td></tr><tr><td align="left"><code>tags</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Any tags associated with the issue</td><td align="left"></td></tr><tr><td align="left"><code>type</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The type of the issue</td><td align="left"></td></tr><tr><td align="left"><code>scope</code></td><td align="left">varchar</td><td align="left">128</td><td align="left">The scope of the issue</td><td align="left"></td></tr><tr><td align="left"><code>start_line</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">The starting line of the issue</td><td align="left"></td></tr><tr><td align="left"><code>end_line</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">The ending line of the issue</td><td align="left"></td></tr><tr><td align="left"><code>start_offset</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">The starting offset of the issue</td><td align="left"></td></tr><tr><td align="left"><code>end_offset</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">The ending offset of the issue</td><td align="left"></td></tr><tr><td align="left"><code>vulnerability_probability</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The probability of the issue being a vulnerability</td><td align="left"></td></tr><tr><td align="left"><code>security_category</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The security category of the issue</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time when the issue was created</td><td align="left"></td></tr><tr><td align="left"><code>updated_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">The time when the issue was last updated</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cq_issue_code_blocks"></a>

#### cq\_issue\_code\_blocks

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is generated based on details from the original plugin</td><td align="left">PK</td></tr><tr><td align="left"><code>issue_key</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A string that stores the key of the issue that the code block is associated with</td><td align="left"></td></tr><tr><td align="left"><code>component</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">A string that stores the name of the component that the code block is associated with</td><td align="left"></td></tr><tr><td align="left"><code>start_line</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">An integer that stores the line number where the code block starts</td><td align="left"></td></tr><tr><td align="left"><code>end_line</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">An integer that stores the line number where the code block ends</td><td align="left"></td></tr><tr><td align="left"><code>start_offset</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">An integer that stores the offset where the code block starts</td><td align="left"></td></tr><tr><td align="left"><code>end_offset</code></td><td align="left">bigint</td><td align="left">255</td><td align="left">An integer that stores the offset where the code block ends</td><td align="left"></td></tr><tr><td align="left"><code>msg</code></td><td align="left">longtext</td><td align="left"></td><td align="left">A long text field that stores the message associated with the code block</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--cq_file_metrics"></a>

#### cq\_file\_metrics

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">This key is generated based on details from the original plugin</td><td align="left">PK</td></tr><tr><td align="left"><code>project_key</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The key of the project that the issue belongs to</td><td align="left">PK</td></tr><tr><td align="left"><code>file_name</code></td><td align="left">longtext</td><td align="left"></td><td align="left">longtext fields that store the name of the file</td><td align="left"></td></tr><tr><td align="left"><code>file_path</code></td><td align="left">longtext</td><td align="left"></td><td align="left">longtext fields that store the path of the file</td><td align="left"></td></tr><tr><td align="left"><code>file_language</code></td><td align="left">longtext</td><td align="left"></td><td align="left">longtext fields that store the language of the file</td><td align="left"></td></tr><tr><td align="left"><code>code_smells</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Code smells of this file</td><td align="left"></td></tr><tr><td align="left"><code>sqale_index</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Sqale index of the file</td><td align="left"></td></tr><tr><td align="left"><code>sqale_rating</code></td><td align="left">double</td><td align="left"></td><td align="left">Sqale rating of the file</td><td align="left"></td></tr><tr><td align="left"><code>bugs</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Bugs rating of the file</td><td align="left"></td></tr><tr><td align="left"><code>reliability_rating</code></td><td align="left">longtext</td><td align="left"></td><td align="left">Reliability rating of the file</td><td align="left"></td></tr><tr><td align="left"><code>vulnerabilities</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Vulnerabilities of the file</td><td align="left"></td></tr><tr><td align="left"><code>security_rating</code></td><td align="left">longtext</td><td align="left"></td><td align="left">Security rating of the file</td><td align="left"></td></tr><tr><td align="left"><code>security_hotspots</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Security hotspots of the file</td><td align="left"></td></tr><tr><td align="left"><code>security_hotspots_reviewed</code></td><td align="left">double</td><td align="left"></td><td align="left">Security hotspots reviewed of the file</td><td align="left"></td></tr><tr><td align="left"><code>security_review_rating</code></td><td align="left">longtext</td><td align="left"></td><td align="left">Security review rating of the file</td><td align="left"></td></tr><tr><td align="left"><code>ncloc</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Ncloc of the file</td><td align="left"></td></tr><tr><td align="left"><code>coverage</code></td><td align="left">double</td><td align="left"></td><td align="left">Ncoverage of the file</td><td align="left"></td></tr><tr><td align="left"><code>lines_to_cover</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Lines to cover of the file</td><td align="left"></td></tr><tr><td align="left"><code>duplicated_lines_density</code></td><td align="left">double</td><td align="left"></td><td align="left">Duplicated lines density of the file</td><td align="left"></td></tr><tr><td align="left"><code>duplicated_blocks</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Duplicated blocks of the file</td><td align="left"></td></tr><tr><td align="left"><code>duplicated_files</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Duplicated files of the file</td><td align="left"></td></tr><tr><td align="left"><code>duplicated_lines</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Duplicated lines of the file</td><td align="left"></td></tr><tr><td align="left"><code>effort_to_reach_maintainability_rating_a</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Effort to reach maintainability rating a of the file</td><td align="left"></td></tr><tr><td align="left"><code>complexity</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Complexity of the file</td><td align="left"></td></tr><tr><td align="left"><code>cognitive_complexity</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Cognitive complexity of the file</td><td align="left"></td></tr><tr><td align="left"><code>num_of_lines</code></td><td align="left">bigint</td><td align="left"></td><td align="left">Num of lines of the file</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--domain-6-cross-domain-entities"></a>

### Domain 6 - Cross-Domain Entities

These entities are used to map entities between different domains. They are the key players to break data isolation.

There are low-level entities such as issue\_commits, users, and higher-level cross domain entities such as board\_repos

<a id="datamodels-devlakedomainlayerschema--issue_commits"></a>

#### issue\_commits

A low-level mapping between "issue tracking" and "source code management" domain by mapping `issues` and `commits`. Issue(n): Commit(n).

The original connection between these two entities lies in either issue tracking tools like Jira or source code management tools like GitLab. You have to use tools to accomplish this.

For example, a common method to connect Jira issue and GitLab commit is a GitLab plugin [Jira Integration](https://docs.gitlab.com/ee/integration/jira/). With this plugin, the Jira issue key in the commit message written by the committers will be parsed. Then, the plugin will add the commit urls under this jira issue. Hence, DevLake's [Jira plugin](https://github.com/apache/incubator-devlake/tree/main/backend/plugins/jira) can get the related commits (including repo, commit\_id, url) of an issue.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue id</td><td align="left">FK_issues.id</td></tr><tr><td align="left"><code>commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">Commit sha</td><td align="left">FK_commits.sha</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--pull_request_issues"></a>

#### pull\_request\_issues

This table shows the issues closed by pull requests. It's a medium-level mapping between "issue tracking" and "source code management" domain by mapping issues and commits. Issue(n): Commit(n).

The data is extracted from the body of pull requests conforming to certain regular expression. The regular expression can be defined in GITHUB\_PR\_BODY\_CLOSE\_PATTERN in the .env file

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>pull_request_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Pull request id</td><td align="left">FK_pull_requests.id</td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue id</td><td align="left">FK_issues.id</td></tr><tr><td align="left"><code>pull_request_number</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Pull request key</td><td align="left"></td></tr><tr><td align="left"><code>issue_number</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue key</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--board_repos-deprecated"></a>

#### board\_repos (Deprecated)

A way to link "issue tracking" and "source code management" domain by mapping `boards` and `repos`. Board(n): Repo(n).

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>board_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Board id</td><td align="left">FK_boards.id</td></tr><tr><td align="left"><code>repo_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Repo id</td><td align="left">FK_repos.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--accounts"></a>

#### accounts

This table stores of user accounts across different tools such as GitHub, Jira, GitLab, etc. This table can be joined to get the metadata of all accounts.
metrics, such as *'No. of Issue closed by contributor', 'No. of commits by contributor',*

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">An account's <code>id</code> is the identifier of the account of a specific tool. It is composed of "&lt; Plugin &gt;:&lt; Entity &gt;:&lt; PK0 &gt;<!-- -->[:PK1]<!-- -->..."
For example, a Github account's id is composed of "&lt; github &gt;:&lt; GithubAccounts &gt;:&lt; GithubUserId &gt;)". E.g. 'github:GithubUsers:14050754'</td><td align="left">PK</td></tr><tr><td align="left"><code>email</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Email of the account</td><td align="left"></td></tr><tr><td align="left"><code>full_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Full name</td><td align="left"></td></tr><tr><td align="left"><code>user_name</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Username, nickname or Github login of an account</td><td align="left"></td></tr><tr><td align="left"><code>avatar_url</code></td><td align="left">varchar</td><td align="left">255</td><td align="left"></td><td align="left"></td></tr><tr><td align="left"><code>organization</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">User's organization(s)</td><td align="left"></td></tr><tr><td align="left"><code>created_date</code></td><td align="left">datetime</td><td align="left">3</td><td align="left">User creation time</td><td align="left"></td></tr><tr><td align="left"><code>status</code></td><td align="left">int</td><td align="left"></td><td align="left">0: default, the user is active. 1: the user is not active</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--users"></a>

#### users

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>id</code></td><td>varchar</td><td>255</td><td>id of a person</td><td>PK</td></tr><tr><td><code>email</code></td><td>varchar</td><td>255</td><td>the primary email of a person</td><td></td></tr><tr><td><code>name</code></td><td>varchar</td><td>255</td><td>name of a person</td><td></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--user_accounts"></a>

#### user\_accounts

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>user_id</code></td><td>varchar</td><td>255</td><td>users.id</td><td>Composite PK, FK</td></tr><tr><td><code>account_id</code></td><td>varchar</td><td>255</td><td>accounts.id</td><td>Composite PK, FK</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--teams"></a>

#### teams

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>id</code></td><td>varchar</td><td>255</td><td>id from the data sources, decided by DevLake users</td><td>PK</td></tr><tr><td><code>name</code></td><td>varchar</td><td>255</td><td>name of the team. E.g. team A, team B, etc.</td><td></td></tr><tr><td><code>alias</code></td><td>varchar</td><td>255</td><td>alias or abbreviation of a team</td><td></td></tr><tr><td><code>parent_id</code></td><td>varchar</td><td>255</td><td>teams.id, default to null</td><td>FK</td></tr><tr><td><code>sorting_index</code></td><td>int</td><td>255</td><td>the field to sort team</td><td></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--team_users"></a>

#### team\_users

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>team_id</code></td><td>varchar</td><td>255</td><td>Full name of the team. E.g. team A, team B, etc.</td><td>Composite PK, FK</td></tr><tr><td><code>user_id</code></td><td>varchar</td><td>255</td><td>users.id</td><td>Composite PK, FK</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--project"></a>

#### project

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>name</code></td><td>varchar</td><td>255</td><td>name for project</td><td>PK</td></tr><tr><td><code>description</code></td><td>longtext</td><td></td><td>description of the project</td><td></td></tr><tr><td><code>created_at</code></td><td>datetime</td><td>3</td><td>created time of project</td><td></td></tr><tr><td><code>updated_at</code></td><td>datetime</td><td>3</td><td>last updated time of project</td><td></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--project_metric_settings"></a>

#### project\_metric\_settings

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>project_name</code></td><td>varchar</td><td>255</td><td>name for project</td><td>PK</td></tr><tr><td><code>plugin_name</code></td><td>varchar</td><td>255</td><td>name for plugin</td><td>PK</td></tr><tr><td><code>plugin_option</code></td><td>longtext</td><td></td><td>check if metric plugins have been enabled by the project</td><td></td></tr><tr><td><code>enable</code></td><td>tinyint</td><td>1</td><td>if the metric plugins is enabled</td><td></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--project_mapping"></a>

#### project\_mapping

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>project_name</code></td><td>varchar</td><td>255</td><td>name for project</td><td>PK</td></tr><tr><td><code>table</code></td><td>varchar</td><td>255</td><td>the table name of <a href="#overview-keyconcepts--data-scope">Scope</a></td><td>PK</td></tr><tr><td><code>row_id</code></td><td>varchar</td><td>255</td><td>the row_id in the <a href="#overview-keyconcepts--data-scope">Scope</a> table</td><td>PK</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--project_pr_metrics"></a>

#### project\_pr\_metrics

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Id of PR</td><td align="left">PK</td></tr><tr><td align="left"><code>project_name</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The project that this PR belongs to</td><td align="left">PK</td></tr><tr><td align="left"><code>first_review_id</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The id of the first review on this pr</td><td align="left"></td></tr><tr><td align="left"><code>first_commit_sha</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The sha of the first commit</td><td align="left"></td></tr><tr><td align="left"><code>pr_coding_time</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The time it takes from the first commit until a PR is issued</td><td align="left"></td></tr><tr><td align="left"><code>pr_pickup_time</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The time it takes from when a PR is issued until the first comment is added to that PR</td><td align="left"></td></tr><tr><td align="left"><code>pr_review_time</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The time it takes to complete a code review of a PR before it gets merged</td><td align="left"></td></tr><tr><td align="left"><code>deployment_id</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The id of cicd_task which deploy the commits of this PR</td><td align="left"></td></tr><tr><td align="left"><code>pr_deploy_time</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The time it takes from when a PR is merged to when it is deployed</td><td align="left"></td></tr><tr><td align="left"><code>pr_cycle_time</code></td><td align="left">bigint</td><td align="left"></td><td align="left">The total time from the first commit to when the PR is deployed</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--project_issue_metrics"></a>

#### project\_issue\_metrics

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Id of Issue</td><td align="left">PK</td></tr><tr><td align="left"><code>project_name</code></td><td align="left">varchar</td><td align="left">100</td><td align="left">The project that this Issue belongs to</td><td align="left">PK</td></tr><tr><td align="left"><code>deployment_id</code></td><td align="left">longtext</td><td align="left"></td><td align="left">The id of cicd_task which cause an incident</td><td align="left"></td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--refs_issues_diffs"></a>

#### refs\_issues\_diffs

This table shows the issues fixed by commits added in a new ref compared to an old one. The data is computed from [table.commits\_diffs](#datamodels-devlakedomainlayerschema--commits_diffs), [table.pull\_requests](#datamodels-devlakedomainlayerschema--pull_requests), [table.pull\_request\_commits](#datamodels-devlakedomainlayerschema--pull_request_commits), and [table.pull\_request\_issues](#datamodels-devlakedomainlayerschema--pull_request_issues).

This table can support tag-based analysis, for instance, '*No. of bugs closed in a tag*'.

<table><thead><tr><th align="left"><strong>field</strong></th><th align="left"><strong>type</strong></th><th align="left"><strong>length</strong></th><th align="left"><strong>description</strong></th><th align="left"><strong>key</strong></th></tr></thead><tbody><tr><td align="left"><code>new_ref_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The new ref's id for comparison</td><td align="left">FK_refs.id</td></tr><tr><td align="left"><code>old_ref_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">The old ref's id for comparison</td><td align="left">FK_refs.id</td></tr><tr><td align="left"><code>new_ref_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit new ref points to at the time of collection</td><td align="left"></td></tr><tr><td align="left"><code>old_ref_commit_sha</code></td><td align="left">char</td><td align="left">40</td><td align="left">The commit old ref points to at the time of collection</td><td align="left"></td></tr><tr><td align="left"><code>issue_number</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue number</td><td align="left"></td></tr><tr><td align="left"><code>issue_id</code></td><td align="left">varchar</td><td align="left">255</td><td align="left">Issue id</td><td align="left">FK_issues.id</td></tr></tbody></table>
<a id="datamodels-devlakedomainlayerschema--get-domain-layer-models-in-developer-mode"></a>

## Get Domain Layer Models in Developer Mode

When developing a new plugin, you need to refer to domain layer models, as all raw data should be transformed to domain layer data to provide standardized metrics across tools. Please use the following method to access the domain data models.

```golang
import "github.com/apache/incubator-devlake/models/domainlayer/domaininfo"

domaininfo := domaininfo.GetDomainTablesInfo()
for _, table := range domaininfo {
// do something
}
```

If you want to learn more about plugin models, please visit [PluginImplementation](https://devlake.apache.org/docs/DeveloperManuals/PluginImplementation)

- [Summary](#datamodels-devlakedomainlayerschema--summary)
- [Use Cases](#datamodels-devlakedomainlayerschema--use-cases)
- [Data Models](#datamodels-devlakedomainlayerschema--data-models)
  - [Schema Diagram](#datamodels-devlakedomainlayerschema--schema-diagram)
  - [Naming Conventions](#datamodels-devlakedomainlayerschema--naming-conventions)
- [How to Customize Data Models](#datamodels-devlakedomainlayerschema--how-to-customize-data-models)
- [DWD Entities - (Data Warehouse Detail)](#datamodels-devlakedomainlayerschema--dwd-entities-data-warehouse-detail)
  - [Domain 1 - Issue Tracking](#datamodels-devlakedomainlayerschema--domain-1-issue-tracking)
  - [Domain 2 - Source Code Management](#datamodels-devlakedomainlayerschema--domain-2-source-code-management)
  - [Domain 3 - Code Review](#datamodels-devlakedomainlayerschema--domain-3-code-review)
  - [Domain 4 - CI/CD](#datamodels-devlakedomainlayerschema--domain-4-cicd)
  - [Domain 5 - Code Quality](#datamodels-devlakedomainlayerschema--domain-5-code-quality)
  - [Domain 6 - Cross-Domain Entities](#datamodels-devlakedomainlayerschema--domain-6-cross-domain-entities)
- [Get Domain Layer Models in Developer Mode](#datamodels-devlakedomainlayerschema--get-domain-layer-models-in-developer-mode)

---

<a id="datamodels-toollayerschema"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DataModels/ToolLayerSchema/ -->

<!-- page_index: 76 -->

# Tool Layer Schema

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Tool Layer Schema

<a id="datamodels-toollayerschema--summary"></a>

## Summary

This document describes Apache DevLake's tool layer schema.

Referring to DevLake's [architecture](#overview-architecture), the Tool layer extracts raw data from JSONs into a relational schema that's easier to consume by analytical tasks. Each DevOps tool would have a schema that's tailored to its data structure, hence the name, the Tool layer.

<a id="datamodels-toollayerschema--use-cases"></a>

## Use Cases

As a user, you can check tool data tables to verify data quality if you have concerns about the [domain layer data](#datamodels-devlakedomainlayerschema).

<a id="datamodels-toollayerschema--data-models"></a>

## Data Models

Tool layer tables start with a prefix `_tool_`. Each plugin contains multiple tool data tables, the naming convension of these tables is `_tool_{plugin}_{entity}`. For instance,

- \_tool\_jira\_issues
- \_tool\_jira\_boards
- \_tool\_jira\_board\_issues`
- ...

Normally, you do not need to use tool layer tables, unless you have one of the above use cases.

- [Summary](#datamodels-toollayerschema--summary)
- [Use Cases](#datamodels-toollayerschema--use-cases)
- [Data Models](#datamodels-toollayerschema--data-models)

---

<a id="datamodels-rawlayerschema"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DataModels/RawLayerSchema/ -->

<!-- page_index: 77 -->

# Raw Layer Schema

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Raw Layer Schema

<a id="datamodels-rawlayerschema--summary"></a>

## Summary

This document describes Apache DevLake's raw layer schema.

Referring to DevLake's [architecture](#overview-architecture), the raw layer stores the API responses from data sources (DevOps tools) in JSON. This saves developers' time if the raw data is to be transformed differently later on. Please note that communicating with data sources' APIs is usually the most time-consuming step.

<a id="datamodels-rawlayerschema--use-cases"></a>

## Use Cases

1. As a user, you can check raw data tables to verify data quality if you have concerns about the [domain layer data](#datamodels-devlakedomainlayerschema).
2. As a developer, you can customize domain layer schema based on raw data tables via [customize](#plugins-customize).

<a id="datamodels-rawlayerschema--data-models"></a>

## Data Models

Raw layer tables start with a prefix `_raw_`. Each plugin contains multiple raw data tables, the naming convension of these tables is `_raw_{plugin}_{entity}`. For instance,

- \_raw\_jira\_issues
- \_raw\_jira\_boards
- \_raw\_jira\_board\_issues
- ...

Normally, you do not need to use these tables, unless you have one of the above use cases.

- [Summary](#datamodels-rawlayerschema--summary)
- [Use Cases](#datamodels-rawlayerschema--use-cases)
- [Data Models](#datamodels-rawlayerschema--data-models)

---

<a id="datamodels-systemtables"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DataModels/SystemTables/ -->

<!-- page_index: 78 -->

# System Tables

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# System Tables

<a id="datamodels-systemtables--summary"></a>

## Summary

This document describes Apache DevLake's data models of its own entities. These tables are used and managed by the Devlake framework.

<a id="datamodels-systemtables--use-cases"></a>

## Use Cases

1. As a user, you can check `_devlake_blueprints` and `_devlake_pipelines` when failing to collect data via DevLake's blueprint.
2. As a contributor, you can check these tables to debug task concurrency or data migration features.

<a id="datamodels-systemtables--data-models"></a>

## Data Models

These tables start with a prefix `_devlake`. Unlike raw or tool data tables, DevLake only contains one set of system tables. The naming convension of these tables is `_raw_{plugin}_{entity}`, such as

- \_devlake\_blueprints
- \_devlake\_pipelines
- \_devlake\_tasks
- \_devlake\_subtasks
- ...

Normally, you do not need to use these tables, unless you have one of the above use cases.

- [Summary](#datamodels-systemtables--summary)
- [Use Cases](#datamodels-systemtables--use-cases)
- [Data Models](#datamodels-systemtables--data-models)

---

<a id="developermanuals"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/ -->

<!-- page_index: 79 -->

# Developer Manuals

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Developer Manuals

[## 📄️ Developer Setup

The steps to install DevLake in developer mode.](#developermanuals-developersetup)

[## 📄️ Source Code References

Source Code References](#developermanuals-sourcecodereference)

[## 📄️ Plugin Implementation

Plugin Implementation](#developermanuals-pluginimplementation)

[## 📄️ DB Migration

DB Migration](#developermanuals-dbmigration)

[## 📄️ Notifications

Notifications](#developermanuals-notifications)

[## 📄️ Dal

The Dal (Data Access Layer) is designed to decouple the hard dependency on `gorm` in v0.12](#developermanuals-dal)

[## 📄️ Project

`Project` is \*\*a set of [Scope](../Overview/KeyConcepts.md#data-scope) from different domains\*\*, a way to group different resources, and it is crucial for some metric calculations like `Dora`.](#developermanuals-project)

[## 📄️ Tag Naming Conventions

Tag Naming Conventions](#developermanuals-tagnamingconventions)

[## 📄️ E2E Test Guide

The steps to write E2E tests for plugins.](#developermanuals-e2e-test-guide)

[## 📄️ DevLake Release Guide

Please make sure your public key was included in the https://downloads.apache.org/incubator/devlake/KEYS , if not, please update this file first.](#developermanuals-release-sop)

[## 📄️ UnitTest Test Guide

The steps to write UnitTest tests for plugins.](#developermanuals-unittest)

---

<a id="developermanuals-developersetup"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/DeveloperSetup/ -->

<!-- page_index: 80 -->

# Developer Setup

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Developer Setup

<a id="developermanuals-developersetup--requirements"></a>

## Requirements

- [Docker v19.03.10+](https://docs.docker.com/get-docker)
- [Golang v1.19+](https://golang.org/doc/install)
- [GNU Make](https://www.gnu.org/software/make/)- Mac (Preinstalled) - Windows: [Download](http://gnuwin32.sourceforge.net/packages/make.htm) - Ubuntu: `sudo apt-get install build-essential libssl-dev`

<a id="developermanuals-developersetup--how-to-setup-dev-environment"></a>

## How to setup dev environment

The following guide will walk through how to run DevLake's frontend (`config-ui`) and backend in dev mode.

1. Navigate to where you would like to install this project and clone the repository:


```sh
git clone https://github.com/apache/incubator-devlake.git
cd incubator-devlake
```

2. Install dependencies for plugins:

   - [RefDiff](#plugins-refdiff--development)
3. Install Go packages


```sh
cd backend
go get
cd ..
```

4. Copy the sample config file to new local file:


```sh
cp env.example .env
```

5. Update the following variables in the file `.env`:

   - `DB_URL`: Replace `mysql:3306` with `127.0.0.1:3306`
6. Start the MySQL and Grafana containers:

   > Make sure the Docker daemon is running before this step.


```sh
docker-compose -f docker-compose-dev.yml up -d mysql grafana
```

7. Run `devlake` and `config-ui` in dev mode in two separate terminals:


```sh
# specify the plugins that you need for both backend and frontend export DEVLAKE_PLUGINS=bamboo,bitbucket,circleci,customize,dora,gitextractor,github,github_graphql,gitlab,jenkins,jira,org,pagerduty,refdiff,slack,sonarqube,trello,webhook
# install poetry, just follow the guide in: https://python-poetry.org/docs/#installation
# run devlake make dev
# run config-ui make configure-dev
```

   For common errors, please see [Troubleshooting](#developermanuals-developersetup--troubleshotting).
8. Config UI is running at `localhost:4000`

   - For how to use Config UI, please refer to our [tutorial](#configuration-tutorial)

<a id="developermanuals-developersetup--running-tests"></a>

## Running Tests

```sh
# install mockery go install github.com/vektra/mockery/v2@latest
# generate mocking stubs make mock
# run tests make test
```

<a id="developermanuals-developersetup--db-migrations"></a>

## DB migrations

Please refer to the [Migration Doc](#developermanuals-dbmigration).

<a id="developermanuals-developersetup--using-devlake-api"></a>

## Using DevLake API

All DevLake APIs (core service + plugin API) are documented with swagger. To see API doc live with swagger:

```text
- Install [swag](https://github.com/swaggo/swag).
- Run `make swag` to generate the swagger documentation.
- Visit `http://localhost:8080/swagger/index.html` while `devlake` is running.
```

<a id="developermanuals-developersetup--developing-dashboards"></a>

## Developing dashboards

To access Grafana, click *View Dashboards* button in the top left corner of Config UI, or visit `localhost:3002` (username: `admin`, password: `admin`).

For provisioning, customizing, and creating dashboards, please refer to our [Grafana Doc](#configuration-dashboards-grafanauserguide).

<a id="developermanuals-developersetup--troubleshooting"></a>

## Troubleshooting

````text
Q: Running `make dev` yields error: `libgit2.so.1.3: cannot open share object file: No such file or directory`

A: `libgit2.so.1.3` is required by the gitextractor plugin and should be . Make sure your program can find `libgit2.so.1.3`. `LD_LIBRARY_PATH` can be assigned like this if your `libgit2.so.1.3` is located at `/usr/local/lib`:

```sh
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```

Note that the version has to be pinned to 1.3.0. If you don't have it, you may need to build it manually with CMake from [source](https://github.com/libgit2/libgit2/releases/tag/v1.3.0).
````

<a id="developermanuals-developersetup--compiling"></a>

## Compiling

```text
- Compile all plugins: `make build-plugin`
- Compile specific plugins: `PLUGIN=<PLUGIN_NAME> make build-plugin`
- Compile server: `make build`
- Compile worker: `make build-worker`
```

<a id="developermanuals-developersetup--references"></a>

## References

To dig deeper into developing and utilizing our built-in functions and have a better developer experience, feel free to dive into our [godoc](https://pkg.go.dev/github.com/apache/incubator-devlake) reference.

- [Requirements](#developermanuals-developersetup--requirements)
- [How to setup dev environment](#developermanuals-developersetup--how-to-setup-dev-environment)
- [Running Tests](#developermanuals-developersetup--running-tests)
- [DB migrations](#developermanuals-developersetup--db-migrations)
- [Using DevLake API](#developermanuals-developersetup--using-devlake-api)
- [Developing dashboards](#developermanuals-developersetup--developing-dashboards)
- [Troubleshooting](#developermanuals-developersetup--troubleshooting)
- [Compiling](#developermanuals-developersetup--compiling)
- [References](#developermanuals-developersetup--references)

---

<a id="developermanuals-sourcecodereference"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/SourceCodeReference/ -->

<!-- page_index: 81 -->

# Source Code References

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Source Code References

For developers who wish to contribute to or develop based on the Apache DevLake, the
[pkg.go.dev](https://pkg.go.dev/github.com/apache/incubator-devlake#section-documentation)
is a good resource for reference, you can learn the overall structure of the code base or
the definition of a specific function.

---

<a id="developermanuals-pluginimplementation"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/PluginImplementation/ -->

<!-- page_index: 82 -->

# Plugin Implementation

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Plugin Implementation

Plugins are code extensions that enable you to pull data from data-sources and present them in DevLake.
They can be implemented in both Go and Python. The framework itself is written in Go, and Python (called PyDevLake) is a supplemental extension to
support developers who prefer it using it. PyDevLake is relatively brand new, and we would like to see it gain more traction; we encourage you to give it
a try if you are familiar with Python.

The Go development manual can be found [here](https://github.com/apache/incubator-devlake/blob/main/backend/DevelopmentManual.md). This manual also covers the framework in detail.

The Python development manual can be found [here](https://github.com/apache/incubator-devlake/blob/main/backend/python/README.md).

---

<a id="developermanuals-dbmigration"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/DBMigration/ -->

<!-- page_index: 83 -->

# DB Migration

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DB Migration

<a id="developermanuals-dbmigration--summary"></a>

## Summary

Starting in v0.10.0, DevLake provides a lightweight migration tool for executing migration scripts.
Both the framework and the plugins can define their migration scripts in their own migration folder.
The migration scripts are written with gorm in Golang to support different SQL dialects.

<a id="developermanuals-dbmigration--migration-scripts"></a>

## Migration Scripts

The migration scripts describe how to do database migration and implement the `MigrationScript` interface.
When DevLake starts, the scripts register themselves to the framework by invoking the `Register` function.
The method `Up` contains the steps of migration.

```go
type MigrationScript interface {
    // this function will contain the business logic of the migration (e.g. DDL logic)
    Up(basicRes BasicRes) errors.Error
    // the version number of the migration. typically in date format (YYYYMMDDHHMMSS), e.g. 20220728000001. Migrations are executed sequentially based on this number.
    Version() uint64
    // The name of this migration
    Name() string
}
```

<a id="developermanuals-dbmigration--the-migration-model"></a>

## The Migration Model

For each migration, we define a "snapshot" datamodel of the model that we wish to perform the migration on.
The fields on this model shall be identical to the actual model; but unlike the actual one, this one will
never change in the future. The naming convention of these models is `<ModelName>YYYYMMDD` and they must implement
the `func TableName() string` method, and consumed by the `Script::Up` method.

<a id="developermanuals-dbmigration--table-migration_history"></a>

## Table `migration_history`

The table tracks migration scripts execution and schemas changes, and from which, DevLake can figure out the current state of database schemas.

<a id="developermanuals-dbmigration--execution"></a>

## Execution

Each plugin has a `migrationscripts` subpackage that lists all the migrations to be executed for that plugin. You
will need to add your migration to that list for the framework to pick it up. Similarly, there is a package
for the framework-only migrations defined under the `models` package.

<a id="developermanuals-dbmigration--how-it-works"></a>

## How It Works

1. Check `migration_history` table, calculate all the migration scripts need to be executed.
2. Sort scripts by `Version` and `Name` in ascending order. Please do NOT change these two values for the script after release for any reasons; otherwise, users may fail to upgrade due to the duplicated execution.
3. Execute the scripts.
4. Save the results in the `migration_history` table.

<a id="developermanuals-dbmigration--best-practices"></a>

## Best Practices

When you write a new migration script, please pay attention to the fault tolerance and the side effect. It would be better if the failed script could be safely retried, in case if something goes wrong during the migration. For this purpose, the migration scripts should be well-designed. For example, if you have created a temporary table in the Up method, it should be dropped before exiting, regardless of success or failure.

Suppose we want to change the type of the Primary Key `name` of table `users` from `int` to `varchar(255)`

1. Rename `users` to `users_20221018` (stop if error, otherwise define a `defer` to rename back on error)
2. Create new `users` (stop if error, otherwise define a `defer` to drop the table on error)
3. Convert data from `users_20221018` to `users` (stop if error)
4. Drop table `users_20221018`

With these steps, the `defer` functions would be executed in reverse order if any error occurred during the migration process so the database would roll back to the original state in most cases.

However, you don't neccessary deal with all the mess. We had summarized some of the most useful code examples for you to follow:

- [Create new tables]<https://github.com/apache/incubator-devlake/blob/main/backend/core/models/migrationscripts/20220406_add_frame_tables.go>)
  [Rename column](https://github.com/apache/incubator-devlake/blob/main/backend/core/models/migrationscripts/20220505_rename_pipeline_step_to_stage.go)
- [Add columns with default value](https://github.com/apache/incubator-devlake/blob/main/backend/core/models/migrationscripts/20220616_add_blueprint_mode.go)
- [Change the values(or type) of Primary Key](https://github.com/apache/incubator-devlake/blob/main/backend/core/models/migrationscripts/20220913_fix_commitfile_id_toolong.go)
- [Change the values(or type) of Column](https://github.com/apache/incubator-devlake/blob/main/backend/core/models/migrationscripts/20220903_encrypt_blueprint.go)

The above examples should cover most of the scenarios you may encounter. If you come across other scenarios, feel free to create issues in our GitHub Issue Tracker for discussions.

In order to help others understand the script you have written, there are a couple of rules we suggest to follow:

- Name your script in a meaningful way. For instance, `renamePipelineStepToStage` is more descriptive than `modifyPipelines`.
- The script should keep only the targeted `fields` you are attempting to operate except when using `migrationhelper.Transform`, which is a full table tranformation that requires full table definition. If this is the case, add comment to the end of the fields to indicate which ones are the targets.
- Add comments to the script when the operation is too complicated to be expressed in plain code.

Other rules to follow when writing a migration script:

- The migration script should only use the interfaces and packages offered by the framework like `core`, `errors` and `migrationhelper`. Do NOT import `gorm` or package from `plugin` directly.
- The name of `model struct` defined in your script should be suffixed with the `Version` of the script to distinguish from other scripts in the same package to keep it self-contained, i.e. `tasks20221018`. Do NOT refer `struct` defined in other scripts.
- All scripts and models names should be `camelCase` to avoid accidental reference from other packages.

- [Summary](#developermanuals-dbmigration--summary)
- [Migration Scripts](#developermanuals-dbmigration--migration-scripts)
- [The Migration Model](#developermanuals-dbmigration--the-migration-model)
- [Table `migration_history`](#developermanuals-dbmigration--table-migration_history)
- [Execution](#developermanuals-dbmigration--execution)
- [How It Works](#developermanuals-dbmigration--how-it-works)
- [Best Practices](#developermanuals-dbmigration--best-practices)

---

<a id="developermanuals-notifications"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/Notifications/ -->

<!-- page_index: 84 -->

# Notifications

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Notifications

<a id="developermanuals-notifications--request"></a>

## Request

Example request

```text
POST /lake/notify?nouce=3-FDXxIootApWxEVtz&sign=424c2f6159bd9e9828924a53f9911059433dc14328a031e91f9802f062b495d5

{"TaskID":39,"PluginName":"jenkins","CreatedAt":"2021-09-30T15:28:00.389+08:00","UpdatedAt":"2021-09-30T15:28:00.785+08:00"}
```

<a id="developermanuals-notifications--configuration"></a>

## Configuration

If you want to use the notification feature, you should add two configuration key to `.env` file.

```shell
# .env
# notification request url, e.g.: http://example.com/lake/notify NOTIFICATION_ENDPOINT=
# secret is used to calculate signature NOTIFICATION_SECRET=
```

<a id="developermanuals-notifications--signature"></a>

## Signature

You should check the signature before accepting the notification request. We use sha256 algorithm to calculate the checksum.

```go
// calculate checksum
sum := sha256.Sum256([]byte(requestBody + NOTIFICATION_SECRET + nouce))
return hex.EncodeToString(sum[:])
```

- [Request](#developermanuals-notifications--request)
- [Configuration](#developermanuals-notifications--configuration)
- [Signature](#developermanuals-notifications--signature)

---

<a id="developermanuals-dal"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/Dal/ -->

<!-- page_index: 85 -->

# Dal

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Dal

<a id="developermanuals-dal--summary"></a>

## Summary

The Dal (Data Access Layer) is designed to decouple the hard dependency on `gorm` in v0.12. The advantages of introducing this isolation are:

- Unit Test: Mocking an Interface is easier and more reliable than Patching a Pointer.
- Clean Code: DBS operations are more consistence than using `gorm`  directly.
- Replaceable: It would be easier to replace `gorm` in the future if needed.

<a id="developermanuals-dal--the-dal-interface"></a>

## The Dal Interface

```go
type Dal interface {
    AutoMigrate(entity interface{}, clauses ...Clause) error
    Exec(query string, params ...interface{}) error
    RawCursor(query string, params ...interface{}) (*sql.Rows, error)
    Cursor(clauses ...Clause) (*sql.Rows, error)
    Fetch(cursor *sql.Rows, dst interface{}) error
    All(dst interface{}, clauses ...Clause) error
    First(dst interface{}, clauses ...Clause) error
    Count(clauses ...Clause) (int64, error)
    Pluck(column string, dest interface{}, clauses ...Clause) error
    Create(entity interface{}, clauses ...Clause) error
    Update(entity interface{}, clauses ...Clause) error
    CreateOrUpdate(entity interface{}, clauses ...Clause) error
    CreateIfNotExist(entity interface{}, clauses ...Clause) error
    Delete(entity interface{}, clauses ...Clause) error
    AllTables() ([]string, error)
}
```

<a id="developermanuals-dal--how-to-use"></a>

## How to use

<a id="developermanuals-dal--query"></a>

### Query

```go
// Get a database cursor
user := &models.User{}
cursor, err := db.Cursor(
  dal.From(user),
  dal.Where("department = ?", "R&D"),
  dal.Orderby("id DESC"),
)
if err != nil {
  return err
}
for cursor.Next() {
  err = dal.Fetch(cursor, user)  // fetch one record at a time
  ...
}

// Get a database cursor by raw sql query
cursor, err := db.Raw("SELECT * FROM users")

// USE WITH CAUTIOUS: loading a big table at once is slow and dangerous
// Load all records from database at once.
users := make([]models.Users, 0)
err := db.All(&users, dal.Where("department = ?", "R&D"))

// Load a column as Scalar or Slice
var email string
err := db.Pluck("email", &username, dal.Where("id = ?", 1))
var emails []string
err := db.Pluck("email", &emails)

// Execute query
err := db.Exec("UPDATE users SET department = ? WHERE department = ?", "Research & Development", "R&D")
```

<a id="developermanuals-dal--insert"></a>

### Insert

```go
err := db.Create(&models.User{
  Email: "hello@example.com", // assuming this the Primarykey
  Name: "hello",
  Department: "R&D",
})
```

<a id="developermanuals-dal--update"></a>

### Update

```go
err := db.Create(&models.User{
  Email: "hello@example.com", // assuming this the Primarykey
  Name: "hello",
  Department: "R&D",
})
```

<a id="developermanuals-dal--insert-or-update"></a>

### Insert or Update

```go
err := db.CreateOrUpdate(&models.User{
  Email: "hello@example.com",  // assuming this is the Primarykey
  Name: "hello",
  Department: "R&D",
})
```

<a id="developermanuals-dal--insert-if-recordby-primarykey-didnt-exist"></a>

### Insert if record(by PrimaryKey) didn't exist

```go
err := db.CreateIfNotExist(&models.User{
  Email: "hello@example.com",  // assuming this is the Primarykey
  Name: "hello",
  Department: "R&D",
})
```

<a id="developermanuals-dal--delete"></a>

### Delete

```go
err := db.CreateIfNotExist(&models.User{
  Email: "hello@example.com",  // assuming this is the Primary key
})
```

<a id="developermanuals-dal--ddl-and-others"></a>

### DDL and others

```go
// Returns all table names
allTables, err := db.AllTables()

// Automigrate: create/add missing table/columns
// Note: it won't delete any existing columns, nor does it update the column definition
err := db.AutoMigrate(&models.User{})
```

<a id="developermanuals-dal--how-to-do-unit-test"></a>

## How to do Unit Test

First, run the command `make mock` to generate the Mocking Stubs, the generated source files should appear in `mocks` folder.

```text
mocks
├── ApiResourceHandler.go
├── AsyncResponseHandler.go
├── BasicRes.go
├── CloseablePluginTask.go
├── ConfigGetter.go
├── Dal.go
├── DataConvertHandler.go
├── ExecContext.go
├── InjectConfigGetter.go
├── InjectLogger.go
├── Iterator.go
├── Logger.go
├── Migratable.go
├── PluginApi.go
├── PluginBlueprintV100.go
├── PluginInit.go
├── PluginMeta.go
├── PluginTask.go
├── RateLimitedApiClient.go
├── SubTaskContext.go
├── SubTaskEntryPoint.go
├── SubTask.go
└── TaskContext.go
```

With these Mocking stubs, you may start writing your TestCases using the `mocks.Dal`.

```go
import "github.com/apache/incubator-devlake/mocks"

func TestCreateUser(t *testing.T) {
    mockDal := new(mocks.Dal)
    mockDal.On("Create", mock.Anything, mock.Anything).Return(nil).Once()
    userService := &services.UserService{
        Dal: mockDal,
    }
    userService.Post(map[string]interface{}{
        "email": "helle@example.com",
        "name": "hello",
        "department": "R&D",
    })
    mockDal.AssertExpectations(t)
```

- [Summary](#developermanuals-dal--summary)
- [The Dal Interface](#developermanuals-dal--the-dal-interface)
- [How to use](#developermanuals-dal--how-to-use)
  - [Query](#developermanuals-dal--query)
  - [Insert](#developermanuals-dal--insert)
  - [Update](#developermanuals-dal--update)
  - [Insert or Update](#developermanuals-dal--insert-or-update)
  - [Insert if record(by PrimaryKey) didn't exist](#developermanuals-dal--insert-if-recordby-primarykey-didnt-exist)
  - [Delete](#developermanuals-dal--delete)
  - [DDL and others](#developermanuals-dal--ddl-and-others)
- [How to do Unit Test](#developermanuals-dal--how-to-do-unit-test)

---

<a id="developermanuals-project"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/Project/ -->

<!-- page_index: 86 -->

# Summary

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Summary

For some metric calculations such as the `DORA` metric, we often encounter situations requiring comprehensive calculations based on data from multiple data sources.

For example, we may use `GitLab` for code hosting, `Jenkins` for CI/CD, to calculate PR deployment cycle time, we need to know which `GitLab Projects` and `Jenkins Jobs` are related for correctness and performance reasons.

However, in most cases, we have multiple `GitLab Projects` / `Jenkins Jobs` that belong to different teams in our Apache DevLake database.

To distinguish them into different groups. The `Project` is introduced in v0.15. Essentially, a `project` consists of a set of [Scopes](#overview-keyconcepts--data-scope), i.e., a couple of `GitLab Projects`, `Jira Boards` or `Jenkins Jobs`, etc.

`Project` is **a set of [Scope](#overview-keyconcepts--data-scope) from different domains**, a way to group different resources, and it is crucial for some metric calculation like `Dora`.

Next, let us introduce `Project` in the following order:

- `Project` related models
- Related APIs that can be used to manipulate `Project` models
- The interface that needs to be implemented when developing various plugins to support the `Project`.
  - The interface that needs to be implemented to develop the `Data Source Plugin`
  - The interface that needs to be implemented to develop the `Metric Plugins`

# Models

To support project we contains the following three models:

- `projects` describes a project object, including its name, creation and update time and other basic information
- `project_metric_settings` describes what metric plugins a project had enabled.
- `project_mapping` describes the mapping relationship of project and scope, including the name of the project、the table name of [Scope](#overview-keyconcepts--data-scope) and the row\_id in the [Scope](#overview-keyconcepts--data-scope) table.

<a id="developermanuals-project--projects"></a>

## projects

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>name</code></td><td>varchar</td><td>255</td><td>name for project</td><td>PK</td></tr><tr><td><code>description</code></td><td>longtext</td><td></td><td>description of the project</td><td></td></tr><tr><td><code>created_at</code></td><td>datetime</td><td>3</td><td>created time of project</td><td></td></tr><tr><td><code>updated_at</code></td><td>datetime</td><td>3</td><td>last updated time of project</td><td></td></tr></tbody></table>
<a id="developermanuals-project--example"></a>

### example

<table><thead><tr><th><strong>name</strong></th><th><strong>describe</strong></th><th><strong>created_at</strong></th><th><strong>updated_at</strong></th></tr></thead><tbody><tr><td>project_1</td><td>this is one of the test projects</td><td>2022-11-01 01:22:13.000</td><td>2022-11-01 02:24:15.000</td></tr><tr><td>project_2</td><td>this is another project test project</td><td>2022-11-01 01:23:29.000</td><td>2022-11-01 02:27:24.000</td></tr></tbody></table>
<a id="developermanuals-project--project_metric_settings"></a>

## project\_metric\_settings

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>project_name</code></td><td>varchar</td><td>255</td><td>name for project</td><td>PK</td></tr><tr><td><code>plugin_name</code></td><td>varchar</td><td>255</td><td>name for plugin</td><td>PK</td></tr><tr><td><code>plugin_option</code></td><td>longtext</td><td></td><td>check if metric plugins have been enabled by the project</td><td></td></tr><tr><td><code>enable</code></td><td>tinyint</td><td>1</td><td>if the metric plugins is enabled</td><td></td></tr></tbody></table>
<a id="developermanuals-project--example-1"></a>

### example

<table><thead><tr><th><strong>project_name</strong></th><th><strong>plugin_name</strong></th><th><strong>plugin_option</strong></th><th><strong>enable</strong></th></tr></thead><tbody><tr><td>project_1</td><td>dora</td><td>{}</td><td>true</td></tr><tr><td>project_2</td><td>dora</td><td>{}</td><td>false</td></tr></tbody></table>
<a id="developermanuals-project--project_mapping"></a>

## project\_mapping

<table><thead><tr><th><strong>field</strong></th><th><strong>type</strong></th><th><strong>length</strong></th><th><strong>description</strong></th><th><strong>key</strong></th></tr></thead><tbody><tr><td><code>project_name</code></td><td>varchar</td><td>255</td><td>name for project</td><td>PK</td></tr><tr><td><code>table</code></td><td>varchar</td><td>255</td><td>the table name of <a href="#overview-keyconcepts--data-scope">Scope</a></td><td>PK</td></tr><tr><td><code>row_id</code></td><td>varchar</td><td>255</td><td>the row_id in the <a href="#overview-keyconcepts--data-scope">Scope</a> table</td><td>PK</td></tr></tbody></table>
<a id="developermanuals-project--example-2"></a>

### example

<table><thead><tr><th><strong>project_name</strong></th><th><strong>table</strong></th><th><strong>row_id</strong></th></tr></thead><tbody><tr><td>project_1</td><td>Repo</td><td>gitlab:GithubRepo:1:lake</td></tr><tr><td>project_1</td><td>Board</td><td>jira:JiraBoard:1:lake</td></tr><tr><td>project_2</td><td>Repo</td><td>github:GithubRepo:1:lake</td></tr></tbody></table>

# How to manage project via API

For API specification, please check the swagger doc(by visiting `[Your Config-UI Host]/api/swagger/index.html`).
Related endpoints:

1. /projects
2. /projects/:projectName/metrics
3. /plugins

# The interface that needs to be implemented

We divide plugins into two categories

- The first category is `Data Source Plugin`, such as `GitLab` `GitHub` `Jira` `Jenkins`, etc. These plugins collect data from various data sources
- The second category is `Metric Plugin`, such as `Dora`, etc. These plugins do not directly contact the data source but do secondary calculations based on the collected data after the `Data Source Plugin` works

<a id="developermanuals-project--data-source-plugin"></a>

## Data Source Plugin

For example `GitLab` `GitHub` `Jira` `Jenkins` etc.

These plugins, from various data sources, extract data into the database and store them, they deal directly with the data source, so we classify them as `Data Source Plugin`.

<a id="developermanuals-project--the-datasourcepluginblueprintv200-interface"></a>

## the DataSourcePluginBlueprintV200 interface

`Data Source Plugin` needs to implement `DataSourcePluginBlueprintV200` interface to support `project`

The interface definition for this interface is as follows

```go
// DataSourcePluginBlueprintV200 extends the V100 to provide support for
// Project, so that complex metrics like DORA can be implemented based on a set
// of Data Scopes
type DataSourcePluginBlueprintV200 interface {
    MakeDataSourcePipelinePlanV200(
        connectionId uint64,
        scopes []*BlueprintScopeV200,
        syncPolicy BlueprintSyncPolicy,
    ) (PipelinePlan, []Scope, errors.Error)
}
```

`scopes` in input parameters is a set of arrays containing IDs, Names, and Entities.

The input data format is as follows:

```go
[]*core.BlueprintScopeV200{
    {
        Entities: []string{"CODE", "TICKET",  "CICD"},
        Id:       "37",
        Name:     "test",
    },
}
```

`syncPolicy` in input parameters contains some option settings, whose structure is defined as follows:

```go
type BlueprintSyncPolicy struct {
    Version          string     `json:"version" validate:"required,semver,oneof=1.0.0"`
    SkipOnFail       bool       `json:"skipOnFail"`
    CreatedDateAfter *time.Time `json:"createdDateAfter"`
}
```

`PipelinePlan` in output is a part of blueprint JSON:

The input data format is as follows:(Take GitLab plugin as an example)

```go
core.PipelinePlan{
    {
        {
            Plugin: "gitlab",
            Subtasks: []string{
                tasks.ConvertProjectMeta.Name,
                tasks.CollectApiIssuesMeta.Name,
                tasks.ExtractApiIssuesMeta.Name,
                tasks.ConvertIssuesMeta.Name,
                tasks.ConvertIssueLabelsMeta.Name,
                tasks.CollectApiJobsMeta.Name,
                tasks.ExtractApiJobsMeta.Name,
                tasks.CollectApiPipelinesMeta.Name,
                tasks.ExtractApiPipelinesMeta.Name,
            },
            Options: map[string]interface{}{
                "connectionId": uint64(1),
                "projectId":    testID,
            },
        },
        {
            Plugin: "gitextractor",
            Options: map[string]interface{}{
                "proxy":  "",
                "repoId": repoId,
                "url":    "https://git:nddtf@this_is_cloneUrl",
            },
        },
    },
    {
        {
            Plugin: "refdiff",
            Options: map[string]interface{}{
                "tagsLimit":   10,
                "tagsOrder":   "reverse semver",
                "tagsPattern": "pattern",
            },
        },
    },
}
```

`project` needs to provide a specific set of [Scopes](#overview-keyconcepts--data-scope) for a specific `connection` to the plugin through this interface, and then obtain the plugin involved in the `PipelineTask` All `plugins` and corresponding parameter information. At the same time, the plugin needs to convert entities like `repo` and `board` in the data source into a `scope interface` that `project` can understand

The corresponding `scope interface` has been implemented at following files of in the framework layer:

- `models/domainlayer/devops/cicd_scope.go`
- `models/domainlayer/ticket/board.go`
- `models/domainlayer/code/repo.go`

In the `plugins/gitlab/impl/impl.go` file, there is a `GitLab` plugin implementation of the above interface, which can be used as a reference.

And the `plugins/gitlab/api/blueprint_v200.go` contains implementation details.

The following files contain the models that the relevant implementations depend on for reference:

- `plugins/gitlab/models/project.go`
- `plugins/gitlab/models/scope_config.go`

<a id="developermanuals-project--metric-plugins"></a>

## Metric Plugins

For example `Dora`, and `Refdff` plugins belong to the `Metric Plugins`

These plugins are mainly for calculating various metrics, they do not directly contact the data source, so we classify them as `Metric Plugins`.

<a id="developermanuals-project--the-pluginmetric-interface"></a>

## The PluginMetric Interface

`Metric Plugins` needs to implement the `PluginMetric` interface to support `project`

The interface definition for this interface looks like this:

```go
type PluginMetric interface {
    // returns a list of required data entities and expected features.
    // [{ "model": "cicd_tasks", "requiredFields": {"column": "type", "execptedValue": "Deployment"}}, ...]
    RequiredDataEntities() (data []map[string]interface{}, err errors.Error)

    // returns if the metric depends on Project for calculation.
    // Currently, only dora would return true.
    IsProjectMetric() bool

    // indicates which plugins must be executed before executing this one.
    // declare a set of dependencies with this
    RunAfter() ([]string, errors.Error)

    // returns an empty pointer of the plugin setting struct.
    // (no concrete usage at this point)
    Settings() (p interface{})
}
```

`Project` needs `PluginMetric` to know whether a `Metric Plugin` is dependent on `project`, and the tables and fields required in its calculation process.

In the `plugins/dora/impl/impl.go` file, there is a `Dora` plugin implementation of the above interface, which can be used as a sample reference.You can find it by searching the following fields:

- `func (plugin Dora) RequiredDataEntities() (data []map[string]interface{}, err errors.Error)`
- `func (plugin Dora) IsProjectMetric() bool`
- `func (plugin Dora) RunAfter() ([]string, errors.Error)`
- `func (plugin Dora) Settings() interface{}`

<a id="developermanuals-project--references"></a>

## References

To dig deeper into developing and utilizing our built-in functions and have a better developer experience, feel free to dive into our [godoc](https://pkg.go.dev/github.com/apache/incubator-devlake) reference.

- [projects](#developermanuals-project--projects)
  - [example](#developermanuals-project--example)
- [project\_metric\_settings](#developermanuals-project--project_metric_settings)
  - [example](#developermanuals-project--example-1)
- [project\_mapping](#developermanuals-project--project_mapping)
  - [example](#developermanuals-project--example-2)
- [Data Source Plugin](#developermanuals-project--data-source-plugin)
- [the DataSourcePluginBlueprintV200 interface](#developermanuals-project--the-datasourcepluginblueprintv200-interface)
- [Metric Plugins](#developermanuals-project--metric-plugins)
- [The PluginMetric Interface](#developermanuals-project--the-pluginmetric-interface)
- [References](#developermanuals-project--references)

---

<a id="developermanuals-tagnamingconventions"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/TagNamingConventions/ -->

<!-- page_index: 87 -->

# Tag Naming Conventions

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Tag Naming Conventions

Please refer to the rules when creating a new tag for Apache DevLake

- alpha: internal testing/preview, i.e. v0.12.0-alpha1
- beta: community/customer testing/preview, i.e. v0.12.0-beta1
- rc: asf release candidate, i.e. v0.12.0-rc1

---

<a id="developermanuals-e2e-test-guide"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/E2E-Test-Guide/ -->

<!-- page_index: 88 -->

# How to write E2E tests for plugins

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# How to write E2E tests for plugins

<a id="developermanuals-e2e-test-guide--why-write-e2e-tests"></a>

## Why write E2E tests

E2E testing, as a part of automated testing, generally refers to black-box testing at the file and module level or unit testing that allows the use of some external services such as databases. The purpose of writing E2E tests is to shield some internal implementation logic and see whether the same external input can output the same result in terms of data aspects. In addition, compared to the black-box integration tests, it can avoid some chance problems caused by network and other factors. More information about the plugin can be found here: Why write E2E tests (incomplete).
In DevLake, E2E testing consists of interface testing and input/output result validation for the plugin Extract/Convert subtask. This article only describes the process of writing the latter. As the Collectors invoke external
services we typically do not write E2E tests for them.

<a id="developermanuals-e2e-test-guide--preparing-data"></a>

## Preparing data

Let's take a simple plugin - Feishu Meeting Hours Collection as an example here. Its directory structure looks like this.
![image](assets/images/175061114-53404aac-16ca-45d1-a0ab-3f61d84922ca_15d2a5a4e6ce5690.png)
Next, we will write the E2E tests of the sub-tasks.

The first step in writing the E2E test is to run the Collect task of the corresponding plugin to complete the data collection; that is, to have the corresponding data saved in the table starting with `_raw_feishu_` in the database.
This data will be presumed to be the "source of truth" for our tests. Here are the logs and database tables using the DirectRun (cmd) run method.

```text
$ go run plugins/feishu/main.go --numOfDaysToCollect 2 --connectionId 1 (Note: command may change with version upgrade)
[2022-06-22 23:03:29] INFO failed to create dir logs: mkdir logs: file exists
press `c` to send cancel signal
[2022-06-22 23:03:29]  INFO  [feishu] start plugin
[2022-06-22 23:03:33]  INFO  [feishu] scheduler for api https://open.feishu.cn/open-apis/vc/v1 worker: 13, request: 10000, duration: 1h0m0s
[2022-06-22 23:03:33]  INFO  [feishu] total step: 2
[2022-06-22 23:03:33]  INFO  [feishu] executing subtask collectMeetingTopUserItem
[2022-06-22 23:03:33]  INFO  [feishu] [collectMeetingTopUserItem] start api collection
[2022-06-22 23:03:34]  INFO  [feishu] [collectMeetingTopUserItem] finished records: 1
[2022-06-22 23:03:34]  INFO  [feishu] [collectMeetingTopUserItem] end api collection error: %!w(<nil>)
[2022-06-22 23:03:34]  INFO  [feishu] finished step: 1 / 2
[2022-06-22 23:03:34]  INFO  [feishu] executing subtask extractMeetingTopUserItem
[2022-06-22 23:03:34]  INFO  [feishu] [extractMeetingTopUserItem] get data from _raw_feishu_meeting_top_user_item where params={"connectionId":1} and got 148
[2022-06-22 23:03:34]  INFO  [feishu] [extractMeetingTopUserItem] finished records: 1
[2022-06-22 23:03:34]  INFO  [feishu] finished step: 2 / 2
```

![image](assets/images/175064505-bc2f98d6-3f2e-4ccf-be68-a1cab1e46401_23ea80251932f914.png)Ok, the data has now been saved to the `\_raw\_feishu\_\*` table, and the `data` column is the return information from the plugin. Here we only collected data for the last 2 days. The data information is not much, but it also covers a variety of situations. That is, the same person has data on different days.

It is also worth mentioning that the plugin runs two tasks, `collectMeetingTopUserItem` and `extractMeetingTopUserItem`. The former is the task of collecting, which is needed to run this time, and the latter is the task of extracting data. It doesn't matter whether the extractor runs in the prepared data session.

Next, we need to export the data to .csv format. This step can be done in a variety of different ways - you can show your skills. I will only introduce a few common methods here.

<a id="developermanuals-e2e-test-guide--devlake-code-generator-export"></a>

### DevLake Code Generator Export

Run `go run generator/main.go create-e2e-raw` directly and follow the guidelines to complete the export. This solution is the simplest, but has some limitations, such as the exported fields being fixed. You can refer to the next solutions if you need more customisation options.

![usage](assets/images/175849225-12af5251-6181-4cd9-ba72-26087b05ee73_db26fc1d55c75571.gif)

<a id="developermanuals-e2e-test-guide--goland-database-export"></a>

### GoLand Database export

![image](assets/images/175067303-7e5e1c4d-2430-4eb5-ad00-e38d86bbd108_8f4aaf985060cd78.png)

This solution is very easy to use and will not cause problems using Postgres or MySQL.
![image](assets/images/175068178-f1c1c290-e043-4672-b43e-54c4b954c685_4bc60c268fc9c2f5.png)
The success criteria for csv export is that the go program can read it without errors, so several points are worth noticing.

1. the values in the csv file should be wrapped in double quotes to avoid special symbols such as commas in the values that break the csv format
2. double quotes in csv files are escaped. generally `""` represents a double quote
3. pay attention to whether the column `data` is the actual value, not the value after base64 or hex

After exporting, move the .csv file to `plugins/feishu/e2e/raw_tables/_raw_feishu_meeting_top_user_item.csv`.

<a id="developermanuals-e2e-test-guide--mysql-select-into-outfile"></a>

### MySQL Select Into Outfile

This is MySQL's solution for exporting query results to a file. The MySQL currently started in docker-compose-dev.yml comes with the --security parameter, so it does not allow `select ... into outfile`. The first step is to turn off the security parameter, which is done roughly as follows.
![origin_img_v2_c809c901-01bc-4ec9-b52a-ab4df24c376g](assets/images/175070770-9b7d5b75-574b-49ed-9bca-e9f611f60795_045f2384b52150bf.jpg)
After closing it, use `select ... into outfile` to export the csv file. The export result is rough as follows.
![origin_img_v2_ccfdb260-668f-42b4-b249-6c2dd45816ag](assets/images/175070866-2204ae13-c058-4a16-bc20-93ab7c95f832_1eff29347e55840a.jpg)
Notice that the data field has extra hexsha fields, which need to be manually converted to literal quantities.

<a id="developermanuals-e2e-test-guide--vscode-database"></a>

### Vscode Database

This is Vscode's solution for exporting query results to a file, but it is not easy to use. Here is the export result without any configuration changes
![origin_img_v2_c9eaadaa-afbc-4c06-85bc-e78235f7eb3g](assets/images/175071987-760c2537-240c-4314-bbd6-1a0cd85ddc0f_19f12ed1ff04c7d1.jpg)
However, it is obvious that the escape symbol does not conform to the csv specification, and the data is not successfully exported. After adjusting the configuration and manually replacing `\"` with `""`, we get the following result.
![image](assets/images/175072314-954c6794-3ebd-45bb-98e7-60ddbb5a7da9_fbbebb55be448dc8.png)
The data field of this file is encoded in base64, so it needs to be decoded manually to a literal amount before using it.

<a id="developermanuals-e2e-test-guide--mysql-workbench"></a>

### MySQL workbench

This tool must write the SQL yourself to complete the data export, which can be rewritten by imitating the following SQL.

```sql
SELECT id, params, CAST(`data` as char) as data, url, input,created_at FROM _raw_feishu_meeting_top_user_item;
```

![image](assets/images/175080866-1631a601-cbe6-40c0-9d3a-d23ca3322a50_a6bc6377c162563e.png)
Select csv as the save format and export it for use.

<a id="developermanuals-e2e-test-guide--postgres-copy-with-csv-header"></a>

### Postgres Copy with csv header

`Copy(SQL statement) to '/var/lib/postgresql/data/raw.csv' with csv header;` is a common export method for PG to export csv, which can also be used here.

```sql
COPY (
SELECT id, params, convert_from(data, 'utf-8') as data, url, input,created_at FROM _raw_feishu_meeting_top_user_item
) to '/var/lib/postgresql/data/raw.csv' with csv header;
```

Use the above statement to complete the export of the file. If pg runs in docker, just use the command `docker cp` to export the file to the host.

<a id="developermanuals-e2e-test-guide--writing-e2e-tests"></a>

## Writing E2E tests

First, create a test environment. For example, let's create `meeting_test.go`.
![image](assets/images/175091380-424974b9-15f3-457b-af5c-03d3b5d17e73_c824409b9c70434d.png)
Then enter the test preparation code in it as follows. The code is to create an instance of the `feishu` plugin and then call `ImportCsvIntoRawTable` to import the data from the csv file into the `_raw_feishu_meeting_top_user_item` table.

```go
func TestMeetingDataFlow(t *testing.T) {
    var plugin impl.Feishu
    dataflowTester := e2ehelper.NewDataFlowTester(t, "feishu", plugin)

    // import raw data table
    dataflowTester.ImportCsvIntoRawTable("./raw_tables/_raw_feishu_meeting_top_user_item.csv", "_raw_feishu_meeting_top_user_item")
}
```

The signature of the import function is as follows.
`func (t *DataFlowTester) ImportCsvIntoRawTable(csvRelPath string, rawTableName string)`
It has a twin, with only slight differences in parameters.
`func (t *DataFlowTester) ImportCsvIntoTabler(csvRelPath string, dst schema.Tabler)`
The former is used to import tables in the raw layer. The latter is used to import arbitrary tables.
**Note:** These two functions will delete the db table and use `gorm.AutoMigrate` to re-create a new table to clear data in it.
After importing the data is complete, run this tester and it must be PASS without any test logic at this moment. Then write the logic for calling the call to the extractor task in `TestMeetingDataFlow`.

```go
func TestMeetingDataFlow(t *testing.T) {
    var plugin impl.Feishu
    dataflowTester := e2ehelper.NewDataFlowTester(t, "feishu", plugin)

    taskData := &tasks.FeishuTaskData{
        Options: &tasks.FeishuOptions{
            ConnectionId: 1,
        },
    }

    // import raw data table
    dataflowTester.ImportCsvIntoRawTable("./raw_tables/_raw_feishu_meeting_top_user_item.csv", "_raw_feishu_meeting_top_user_item")

    // verify extraction
    dataflowTester.FlushTabler(&models.FeishuMeetingTopUserItem{})
    dataflowTester.Subtask(tasks.ExtractMeetingTopUserItemMeta, taskData)

}
```

The added code includes a call to `dataflowTester.FlushTabler` to clear the table `_tool_feishu_meeting_top_user_items` and a call to `dataflowTester.Subtask` to simulate the running of the subtask `ExtractMeetingTopUserItemMeta`.

Now run it and see if the subtask `ExtractMeetingTopUserItemMeta` completes without errors. The data results of the `extract` run generally come from the raw table, so the plugin subtask will run correctly if written without errors. We can observe if the data is successfully parsed in the db table in the tool layer. In this case the `_tool_feishu_meeting_top_user_items` table has the correct data.

If the run is incorrect, maybe you can troubleshoot the problem with the plugin itself before moving on to the next step.

<a id="developermanuals-e2e-test-guide--verify-that-the-results-of-the-task-are-correct"></a>

## Verify that the results of the task are correct

Let's continue writing the test and add the following code at the end of the test function

```go
func TestMeetingDataFlow(t *testing.T) {
    ......

    dataflowTester.VerifyTable(
      models.FeishuMeetingTopUserItem{},
      "./snapshot_tables/_tool_feishu_meeting_top_user_items.csv",
      []string{
        "meeting_count",
        "meeting_duration",
        "user_type",
        "_raw_data_params",
        "_raw_data_table",
        "_raw_data_id",
        "_raw_data_remark",
      },
    )
}
```

Its purpose is to call `dataflowTester.VerifyTable` to complete the validation of the data results. The third parameter is all the fields of the table that need to be verified.
The data used for validation exists in `. /snapshot_tables/_tool_feishu_meeting_top_user_items.csv`, but of course, this file does not exist yet.

There is a twin, more generalized function, that could be used instead:

```go
dataflowTester.VerifyTableWithOptions(models.FeishuMeetingTopUserItem{},
        dataflowTester.TableOptions{
            CSVRelPath: "./snapshot_tables/_tool_feishu_meeting_top_user_items.csv"
        },
    )
```

The above usage will be default to validating against all fields of the `models.FeishuMeetingTopUserItem` model. There are additional fields on `TableOptions` that can be specified to limit which fields on that model to perform validation on.

To facilitate the generation of the file mentioned above, DevLake has adopted a testing technique called `Snapshot`, which will automatically generate the file based on the run results when the `VerifyTable` or `VerifyTableWithOptions` functions are called without the csv existing.

But note! Please do two things after the snapshot is created: 1. check if the file is generated correctly 2. re-run it to make sure there are no errors between the generated results and the re-run results.
These two operations are critical and directly related to the quality of test writing. We should treat the snapshot file in `.csv` format like a code file.

If there is a problem with this step, there are usually 2 ways to solve it.

1. The validated fields contain fields like create\_at runtime or self-incrementing ids, which cannot be repeatedly validated and should be excluded.
2. there is `\n` or `\r\n` or other escape mismatch fields in the run results. Generally, when parsing the `httpResponse` error, you can follow these solutions:
   1. modify the field type of the content in the api model to `json.
   2. convert it to string when parsing
   3. so that the `\n` symbol can be kept intact, avoiding the parsing of line breaks by the database or the operating system

For example, in the `github` plugin, this is how it is handled.
![image](assets/images/175098219-c04b810a-deaf-4958-9295-d5ad4ec152e6_500c594bdfa4dd18.png)
![image](assets/images/175098273-e4a18f9a-51c8-4637-a80c-3901a3c2934e_bc4b0f1cee5aadbd.png)

Well, at this point, the E2E writing is done. We have added a total of 3 new files to complete the testing of the meeting length collection task. It's pretty easy.
![image](assets/images/175098574-ae6c7fb7-7123-4d80-aa85-790b492290ca_aef2a51324b7ca61.png)

<a id="developermanuals-e2e-test-guide--run-e2e-tests-for-all-plugins-like-ci"></a>

## Run E2E tests for all plugins like CI

It's straightforward. Just run `make e2e-plugins` because DevLake has already solidified it into a script~

- [Why write E2E tests](#developermanuals-e2e-test-guide--why-write-e2e-tests)
- [Preparing data](#developermanuals-e2e-test-guide--preparing-data)
  - [DevLake Code Generator Export](#developermanuals-e2e-test-guide--devlake-code-generator-export)
  - [GoLand Database export](#developermanuals-e2e-test-guide--goland-database-export)
  - [MySQL Select Into Outfile](#developermanuals-e2e-test-guide--mysql-select-into-outfile)
  - [Vscode Database](#developermanuals-e2e-test-guide--vscode-database)
  - [MySQL workbench](#developermanuals-e2e-test-guide--mysql-workbench)
  - [Postgres Copy with csv header](#developermanuals-e2e-test-guide--postgres-copy-with-csv-header)
- [Writing E2E tests](#developermanuals-e2e-test-guide--writing-e2e-tests)
- [Verify that the results of the task are correct](#developermanuals-e2e-test-guide--verify-that-the-results-of-the-task-are-correct)
- [Run E2E tests for all plugins like CI](#developermanuals-e2e-test-guide--run-e2e-tests-for-all-plugins-like-ci)

---

<a id="developermanuals-release-sop"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/Release-SOP/ -->

<!-- page_index: 89 -->

# DevLake Release Guide

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DevLake Release Guide

**Please make sure your public key was included in the <https://downloads.apache.org/incubator/devlake/KEYS> , if not, please update this file first.**

<a id="developermanuals-release-sop--how-to-update-keys"></a>

## How to update KEYS

1. Clone the svn repository


```shell
svn co https://dist.apache.org/repos/dist/dev/incubator/devlake
```

2. Append your public key to the KEYS file
   cd devlake

   - Check if your public key is in the KEYS file
   - If it does not, create a new [GPG key](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key), and then run the following command to see if it was successful.


```shell
gpg --list-sigs <your name>
```

   - Append your publick key


```shell
    gpg --armor --export <your name> >> KEYS
```

3. Upload


```shell
svn add KEYS
svn commit -m "update KEYS"
svn cp https://dist.apache.org/repos/dist/dev/incubator/devlake/KEYS https://dist.apache.org/repos/dist/release/incubator/devlake/ -m "update KEYS"
```

   We will use `v0.16.0` as an example to demonstrate the release process.

<a id="developermanuals-release-sop--asf-release-policy"></a>

## ASF Release Policy

- <https://www.apache.org/legal/release-policy.html>
- <https://incubator.apache.org/guides/releasemanagement.html>

<a id="developermanuals-release-sop--tools"></a>

## Tools:

- `gpg` creating and verifying the signature
- `shasum` creating and verifying the checksum
- `git` checkout and pack the codebase
- `svn` uploading the code to the Apache code hosting server

<a id="developermanuals-release-sop--prepare"></a>

## Prepare

- Check against the Incubator Release Checklist
- Create folder `releases/lake-v0.16.0` and put the two files `docker-compose.yml` and `env.example` in there.
- Update the file `.github/ISSUE_TEMPLATE/bug-report.yml` to include the version `v0.16.0`

<a id="developermanuals-release-sop--pack"></a>

## Pack

- Checkout to the branch/commit

```shell
git clone https://github.com/apache/incubator-devlake.git
cd incubator-devlake
git checkout b268d53a48edb26d3c9b73b782798703f068f655
```

- Tag the commit and push to origin


```shell
git tag v0.16.0-rc2
git push origin v0.16.0-rc2
```

- Pack the code


```shell
git archive --format=tar.gz --output="<the-output-dir>/apache-devlake-0.16.0-incubating-src.tar.gz" --prefix="apache-devlake-0.16.0-incubating-src/" v0.16.0-rc2
```

- Before proceeding to the next step, please make sure your public key was included in the <https://downloads.apache.org/incubator/devlake/KEYS>
- Create signature and checksum


```shell
cd <the-output-dir>
gpg -s --armor --output apache-devlake-0.16.0-incubating-src.tar.gz.asc --detach-sig apache-devlake-0.16.0-incubating-src.tar.gz
shasum -a 512  apache-devlake-0.16.0-incubating-src.tar.gz > apache-devlake-0.16.0-incubating-src.tar.gz.sha512
```

- Verify signature and checksum


```shell
gpg --verify apache-devlake-0.16.0-incubating-src.tar.gz.asc apache-devlake-0.16.0-incubating-src.tar.gz
shasum -a 512 --check apache-devlake-0.16.0-incubating-src.tar.gz.sha512
```

<a id="developermanuals-release-sop--upload"></a>

## Upload

- Clone the svn repository


```shell
svn co https://dist.apache.org/repos/dist/dev/incubator/devlake
```

- Copy the files into the svn local directory


```shell
cd devlake
mkdir -p 0.16.0-incubating-rc2
cp <the-output-dir>/apache-devlake-0.16.0-incubating-src.tar.gz* 0.16.0-incubating-rc2/
```

- Upload local files


```shell
svn add 0.16.0-incubating-rc2
svn commit -m "add 0.16.0-incubating-rc2"
```

<a id="developermanuals-release-sop--vote"></a>

## Vote

You can check [Incubator Release Checklist](https://cwiki.apache.org/confluence/display/INCUBATOR/Incubator+Release+Checklist) before voting.

1. Devlake community vote:

   - Start the [vote](https://lists.apache.org/thread/2v2so22fj9mg5h7jck1opsqhjyc86k06) by sending an email to [dev@devlake.apache.org](mailto:dev@devlake.apache.org)

     Title: [VOTE] Release Apache DevLake (Incubating) v{{.Version}}-rc{{.RC}}

     Content:


```text
 Hello everyone,

 This is a call for vote to release Apache DevLake (Incubating) v{{.Version}}-rc{{.RC}}

 The release candidates:
 https://dist.apache.org/repos/dist/dev/incubator/devlake/{{.Version}}-incubating-rc{{.RC}}/

 Git tag for the release:
 https://github.com/apache/incubator-devlake/releases/tag/v{{.Version}}-rc{{.RC}}

 Keys to verify the Release Candidate:
 https://downloads.apache.org/incubator/devlake/KEYS

 How to build:
 https://devlake.apache.org/docs/DeveloperManuals/DeveloperSetup

 The vote will be open for at least 72 hours or until the necessary number of votes are reached.
 If approved we will seek final release approval from the IPMC.

 Please vote accordingly:

 [ ] +1 approve
 [ ] +0 no opinion
 [ ] -1 disapprove with the reason

 Thanks
 {{.YourName}}
```

   - Announce the [vote](https://lists.apache.org/thread/wfzzjv53vfxml54098o6dt4913j47d4j) result:
     Title: [RESULT][VOTE] Release Apache DevLake (Incubating) v{{.Version}}-rc{{.RC}}

     Content:


```text
Hello everyone,

The vote closes now with the following results:

{{.TotalVotes}} (+1 binding) votes
{{range .Votes}}- {{.Name}}{{end}}

I will bring the vote results to general@incubator.apache.org

Thanks
{{.YourName}}
```

2. Apache incubator community vote:

   - Start the [vote](https://lists.apache.org/thread/5dbqc3t2bq7kfqccobrh7j9vqopj030k) by sending an email to [general@incubator.apache.org](mailto:general@incubator.apache.org)
     Title: [VOTE] Release Apache DevLake (Incubating) v{{.Version}}-rc{{.RC}}

     Content:


```text
Hello everyone,

This is a call for vote to release Apache DevLake (Incubating) v{{.Version}}-rc{{.RC}}.
The Apache DevLake community has voted on and approved a proposal to release Apache DevLake (Incubating) version v{{.Version}}-rc{{.RC}}.

Community vote thread:
[Community Vote Thread]({{.VoteThreadURL}})

Community vote result thread:
[Community Vote Result Thread]({{.VoteResultThreadURL}})

The release candidates:
[Release Candidates]({{.RCURL}})

Git tag for the release:
[Git Tag]({{.GitTagURL}})

Keys to verify the Release Candidate:
https://downloads.apache.org/incubator/devlake/KEYS

How to build:
https://devlake.apache.org/docs/DeveloperManuals/DeveloperSetup/

The vote will be open for at least 72 hours or until the necessary number of votes are reached.

Please vote accordingly:
[ ] +1 approve
[ ] +0 no opinion
[ ] -1 disapprove with the reason

Thanks

{{.YourName}}
```

   - Announce the [vote](https://lists.apache.org/thread/40ktrw42c7hpok7vj33ql6wgdq2mpg92) result:
     Title:
     [RESULT][VOTE] Release Apache DevLake (Incubating) v{{.Version}}-rc{{.RC}}

     Content:


```text
Hello everyone,

I am pleased to announce that the vote for Apache DevLake (Incubating) v{{.Version}}-rc{{.RC}} has now concluded. Thank you all for your review and participation in the voting process.

The release voting has passed with {{bindingVotes}} binding votes, {{nonBindingVotes}} non-binding vote and no +0 or -1 votes.

The individuals who provided binding votes are:
{{bindingVotesList}}

The non-binding vote{{pluralNonBindingVotes}} is from:
{{nonBindingVotesList}}

You can find the voting thread at the following link: [Voting Thread](https://lists.apache.org/thread/{{votingThreadURL}})

In closing, I want to express my gratitude to everyone who has offered us help, advice, and guidance throughout this process. We will proceed with completing the remaining tasks.

Thank you all once again!

Best Regards,
{{.YourName}}
```

<a id="developermanuals-release-sop--release"></a>

## Release

<a id="developermanuals-release-sop--apache"></a>

### Apache

- Move the release to the ASF content distribution system


```shell
svn mv https://dist.apache.org/repos/dist/dev/incubator/devlake/0.16.0-incubating-rc2 https://dist.apache.org/repos/dist/release/incubator/devlake/0.16.0-incubating -m "transfer packages for 0.16.0-incubating-rc2"
```

- Wait until the directory `https://downloads.apache.org/incubator/devlake/0.16.0-incubating/` was created
- Remove the last release from `https://downloads.apache.org/` (according the Apache release policy, this link should be pointing to the current release)


```shell
svn rm https://dist.apache.org/repos/dist/release/incubator/devlake/0.15.0-incubating -m "remove 0.15.0-incubating"
```

- Announce [release](https://lists.apache.org/thread/czf6p3xtlkq6t8g4q35blkbf2xclsl3p) by sending an email to [general@incubator.apache.org](mailto:general@incubator.apache.org)
  Title:
  [[ANNOUNCE] Release Apache Devlake(incubating) {{.Version}}-incubating

  Content:


```text
Hello everyone,

The Apache DevLake (Incubating) {{.Version}}-incubating has been released!

**Apache DevLake** is an open-source dev data platform that ingests, analyzes, and visualizes the fragmented data from DevOps tools to distill insights for engineering productivity.

Download Links: https://downloads.apache.org/incubator/devlake/

Changelogs:
- xxx.
- xxx.
- xxx.

Website: https://devlake.apache.org/

Resources:
- Issue:https://github.com/apache/incubator-devlake/issues
- Mailing list: dev@devlake.apache.org

Best Regards,
{{.YourName}}

----
Disclaimer: Apache DevLake(incubating) is an effort undergoing incubation at the Apache
Software Foundation (ASF), sponsored by the Apache Incubator PMC.

Incubation is required of all newly accepted projects until a further review
indicates that the infrastructure, communications, and decision making process
have stabilized in a manner consistent with other successful ASF projects.

While incubation status is not necessarily a reflection of the completeness
or stability of the code, it does indicate that the project has yet to be
fully endorsed by the ASF.
```

<a id="developermanuals-release-sop--github"></a>

### GitHub

- Create tag v0.16.0 and push


```shell
git checkout v0.16.0-rc2
git tag v0.16.0
git push origin v0.16.0
```

- Open the URL `https://github.com/apache/incubator-devlake/releases/`, draft a new release, fill in the form and upload two files `docker-compose.yml` and `env.example`

- [How to update KEYS](#developermanuals-release-sop--how-to-update-keys)
- [ASF Release Policy](#developermanuals-release-sop--asf-release-policy)
- [Tools:](#developermanuals-release-sop--tools)
- [Prepare](#developermanuals-release-sop--prepare)
- [Pack](#developermanuals-release-sop--pack)
- [Upload](#developermanuals-release-sop--upload)
- [Vote](#developermanuals-release-sop--vote)
- [Release](#developermanuals-release-sop--release)
  - [Apache](#developermanuals-release-sop--apache)
  - [GitHub](#developermanuals-release-sop--github)

---

<a id="developermanuals-unittest"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/DeveloperManuals/UnitTest/ -->

<!-- page_index: 90 -->

# Introduction of UnitTest

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Introduction of UnitTest

A unit test is a type of software testing that tests individual units or components of a software application. The goal of unit testing is to validate that each unit of the software performs as expected. Unit tests are typically written by developers as they work on the code, to ensure that the code they are writing is correct and behaves as intended.

Unit tests are automated and are typically written in the same programming language as the code being tested. They are usually run as part of a continuous integration process, ensuring that changes to the codebase don't break existing functionality.

Unit tests are typically small and focus on a specific function or method of the code. They are usually designed to run quickly and in isolation, so that any issues that are discovered can be easily traced back to the specific code that is causing the problem.

# How to write UnitTest for golang

Here are some resources for writing UnitTest for golang:

- [Add a test - The Go Programming Language](https://go.dev/doc/tutorial/add-a-test)
- [How To Write Unit Tests in Go | DigitalOcean](https://www.digitalocean.com/community/tutorials/how-to-write-unit-tests-in-go-using-go-test-and-the-testing-package)

# Test case examples

- [Source code](https://github.com/apache/incubator-devlake/blob/243cc8a80aa5b37828e2a142ac9f7e3269b7e1dc/backend/core/migration/migrator_test.go)

# Recommended Libraries for writing UnitTest cases

- [Library-1](https://github.com/stretchr/testify/tree/master/assert)
- [Library-2](https://github.com/stretchr/testify/tree/master/mock)

---

<a id="plugins"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/ -->

<!-- page_index: 91 -->

# Plugins

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Plugins

[## 📄️ Azure DevOps

Azure DevOps Plugin](#plugins-azuredevops)

[## 📄️ Bamboo

Bamboo Plugin](#plugins-bamboo)

[## 📄️ BitBucket Cloud

BitBucket Plugin](#plugins-bitbucket)

[## 📄️ BitBucket Data Center

BitBucket Data Center Plugin](#plugins-bitbucket_server)

[## 📄️ CircleCI

CircleCI Plugin](#plugins-circleci)

[## 📄️ Customize

Customize Plugin](#plugins-customize)

[## 📄️ DBT

DBT Plugin](#plugins-dbt)

[## 📄️ Feishu

Feishu Plugin](#plugins-feishu)

[## 📄️ Gitee(WIP)

Gitee Plugin](#plugins-gitee)

[## 📄️ GitExtractor

GitExtractor Plugin](#plugins-gitextractor)

[## 📄️ GitHub

GitHub Plugin](#plugins-github)

[## 📄️ GitLab

GitLab Plugin](#plugins-gitlab)

[## 📄️ Jenkins

Jenkins Plugin](#plugins-jenkins)

[## 📄️ Jira

Jira Plugin](#plugins-jira)

[## 📄️ Linker

Linker Plugin](#plugins-linker)

[## 📄️ Opsgenie

Opsgenie Plugin](#plugins-opsgenie)

[## 📄️ PagerDuty

PagerDuty Plugin](#plugins-pagerduty)

[## 📄️ RefDiff

RefDiff Plugin](#plugins-refdiff)

[## 📄️ SonarQube

SonarQube Plugin](#plugins-sonarqube)

[## 📄️ TAPD

Tapd Plugin](#plugins-tapd)

[## 📄️ Teambition(WIP)

Teambition Plugin](#plugins-teambition)

[## 📄️ Trello(WIP)

Trello Plugin](#plugins-trello)

[## 📄️ Webhook

Webhook Plugin](https://devlake.apache.org/docs/v1.0/Plugins/webhook)

[## 📄️ Zentao

Zentao Plugin](#plugins-zentao)

---

<a id="plugins-azuredevops"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/azuredevops/ -->

<!-- page_index: 92 -->

# Azure DevOps

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Azure DevOps

<a id="plugins-azuredevops--summary"></a>

## Summary

This plugin collects Azure DevOps data through Azure DevOps REST API.

<a id="plugins-azuredevops--supported-versions"></a>

## Supported Versions

Available for Azure DevOps Cloud. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-azuredevops--entities"></a>

## Entities

Check out the [Azure DevOps entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-azuredevops--data-refresh-policy"></a>

## Data Refresh Policy

Right now, this plugin supports only full refresh.
Check out the [data refresh policy](/docs/v1.0/Overview/SupportedDataSources#Azure DevOps) of this plugin.

<a id="plugins-azuredevops--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Azure DevOps:

- [Commit Count](#metrics-commitcount)
- [Commit Author Count](#metrics-commitauthorcount)
- [Added Lines of Code](#metrics-addedlinesofcode)
- [Deleted Lines of Code](#metrics-deletedlinesofcode)
- [Build Count](#metrics-buildcount)
- [Build Duration](#metrics-buildduration)
- [Build Success Rate](#metrics-buildsuccessrate)
- [DORA - Deployment Frequency](#metrics-deploymentfrequency)
- [DORA - Lead Time for Changes](#metrics-leadtimeforchanges)
- [DORA - Median Time to Restore Service](#metrics-mttr)
- [DORA - Change Failure Rate](#metrics-cfr)

<a id="plugins-azuredevops--configuration"></a>

## Configuration

Configuring Azure DevOps via [config-ui](#configuration-azuredevops).

<a id="plugins-azuredevops--api-sample-request"></a>

## API Sample Request

You can trigger data collection by making a POST request to `/pipelines`.

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "MY PIPELINE",
  "plan": [
    [
      {
        "plugin": "azuredevops",
        "options": {
          "connectionId": 1,
          "scopeId": "orgname/reponame",
          "transformationRules": {
            "deploymentPattern": "",
            "productionPattern": ""
          }
        }
      }
    ]
  ]
}
'
```

- [Summary](#plugins-azuredevops--summary)
- [Supported Versions](#plugins-azuredevops--supported-versions)
- [Entities](#plugins-azuredevops--entities)
- [Data Refresh Policy](#plugins-azuredevops--data-refresh-policy)
- [Metrics](#plugins-azuredevops--metrics)
- [Configuration](#plugins-azuredevops--configuration)
- [API Sample Request](#plugins-azuredevops--api-sample-request)

---

<a id="plugins-bamboo"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/bamboo/ -->

<!-- page_index: 93 -->

# Bamboo

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Bamboo

<a id="plugins-bamboo--summary"></a>

## Summary

This plugin collects Bamboo's CI data through [API](https://developer.atlassian.com/server/bamboo/rest/). It then computes and visualizes various DevOps metrics from the Bamboo data, which helps tech leads, QA and DevOps engineers, and project managers to answer questions such as:

- What is the deployment frequency of your team?
- How long does it take for your codes to get deployed?

<a id="plugins-bamboo--supported-versions"></a>

## Supported Versions

Only Bamboo v6.8.1+ is supported as of v0.20. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-bamboo--entities"></a>

## Entities

Check out the [Bamboo entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-bamboo--data-refresh-policy"></a>

## Data Refresh Policy

Check out the [data refresh policy](#overview-supporteddatasources--bamboo) of this plugin.

<a id="plugins-bamboo--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Bamboo:

- [DORA - Deployment Frequency](#metrics-deploymentfrequency)
- [DORA - Lead Time for Changes](#metrics-leadtimeforchanges)
- [DORA - Median Time to Restore Service](#metrics-mttr)
- [DORA - Change Failure Rate](#metrics-cfr)

<a id="plugins-bamboo--api-sample-request"></a>

## API Sample Request

You can trigger data collection by making a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1-BLUEPRINT",
  "blueprintId": 1,
  "plan": [
    [
      {
        "plugin": "bamboo",
        "options": {
          "connectionId": 1,
          "key": "TEST",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":"",
          }
        }
      }
    ]
  ]
}
'
```

<a id="plugins-bamboo--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-bamboo--summary)
- [Supported Versions](#plugins-bamboo--supported-versions)
- [Entities](#plugins-bamboo--entities)
- [Data Refresh Policy](#plugins-bamboo--data-refresh-policy)
- [Metrics](#plugins-bamboo--metrics)
- [API Sample Request](#plugins-bamboo--api-sample-request)
- [References](#plugins-bamboo--references)

---

<a id="plugins-bitbucket"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/bitbucket/ -->

<!-- page_index: 94 -->

# BitBucket Cloud

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# BitBucket Cloud

<a id="plugins-bitbucket--summary"></a>

## Summary

This plugin collects various entities from Bitbucket, including pull requests, issues, comments, pipelines, git commits, and etc.

As of v0.14.2, `bitbucket` plugin can only be invoked through DevLake API. Its support in Config-UI is WIP.

<a id="plugins-bitbucket--supported-versions"></a>

## Supported Versions

Available for BitBucket Cloud. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-bitbucket--entities"></a>

## Entities

Check out the [BitBucket entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-bitbucket--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from bitbucket:

- [Commit Count](#metrics-commitcount)
- [Commit Author Count](#metrics-commitauthorcount)
- [Added Lines of Code](#metrics-addedlinesofcode)
- [Deleted Lines of Code](#metrics-deletedlinesofcode)
- [PR Count](#metrics-prcount)
- [PR Time To Merge](#metrics-prtimetomerge)
- [PR Merge Rate](#metrics-prmergerate)
- [PR Review Depth](#metrics-prreviewdepth)
- [PR Size](#metrics-prsize)
- [Build Count](#metrics-buildcount)
- [Build Duration](#metrics-buildduration)
- [Build Success Rate](#metrics-buildsuccessrate)

<a id="plugins-bitbucket--configuration"></a>

## Configuration

- Configuring Bitbucket via [Config UI](#configuration-bitbucket)

<a id="plugins-bitbucket--api-sample-request"></a>

## API Sample Request

> Note: Please replace the `http://localhost:8080` in the sample requests with your actual DevLake API endpoint. For how to view DevLake API's swagger documentation, please refer to the "Using DevLake API" section of [Developer Setup](#developermanuals-developersetup).

You can trigger data collection by making a POST request to `/pipelines`.

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1",
  "plan": [
    [
      {
        "plugin": "bitbucket",
        "options": {
          "connectionId": 1,
          "fullName": "likyh/likyhphp",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":"",
            "issueStatusTodo":"new,open",
            "issueStatusInProgress":"",
            "issueStatusDone":"resolved,closed",
            "issueStatusOther":"on hold,wontfix,duplicate,invalid"
          }
        }
      }
    ]
  ]
}
'
```

<a id="plugins-bitbucket--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-bitbucket--summary)
- [Supported Versions](#plugins-bitbucket--supported-versions)
- [Entities](#plugins-bitbucket--entities)
- [Metrics](#plugins-bitbucket--metrics)
- [Configuration](#plugins-bitbucket--configuration)
- [API Sample Request](#plugins-bitbucket--api-sample-request)
- [References](#plugins-bitbucket--references)

---

<a id="plugins-bitbucket_server"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/bitbucket_server/ -->

<!-- page_index: 95 -->

# BitBucket Data Center

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# BitBucket Data Center

<a id="plugins-bitbucket_server--summary"></a>

## Summary

This plugin collects various entities from Bitbucket Data Center, including pull requests, issues, comments, pipelines, git commits, and etc.

As of v0.20.0, `bitbucket_server` plugin can only be invoked through DevLake API. Its support in Config-UI is WIP.

<a id="plugins-bitbucket_server--supported-versions"></a>

## Supported Versions

Available for BitBucket Data Center 8.16 and BitBucket Data Center and Server 7.21. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-bitbucket_server--entities"></a>

## Entities

Check out the [BitBucket entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-bitbucket_server--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from bitbucket:

- [Commit Count](#metrics-commitcount)
- [Commit Author Count](#metrics-commitauthorcount)
- [Added Lines of Code](#metrics-addedlinesofcode)
- [Deleted Lines of Code](#metrics-deletedlinesofcode)
- [PR Count](#metrics-prcount)
- [PR Time To Merge](#metrics-prtimetomerge)
- [PR Merge Rate](#metrics-prmergerate)
- [PR Review Depth](#metrics-prreviewdepth)
- [PR Size](#metrics-prsize)

<a id="plugins-bitbucket_server--configuration"></a>

## Configuration

- Configuring Bitbucket via [Config UI](#configuration-bitbucketserver)

<a id="plugins-bitbucket_server--api-sample-request"></a>

## API Sample Request

> Note: Please replace the `http://localhost:8080` in the sample requests with your actual DevLake API endpoint. For how to view DevLake API's swagger documentation, please refer to the "Using DevLake API" section of [Developer Setup](#developermanuals-developersetup).

You can trigger data collection by making a POST request to `/pipelines`.

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1",
  "plan": [
    [
      {
        "plugin": "bitbucket",
        "options": {
          "connectionId": 1,
          "fullName": "likyh/likyhphp",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":"",
            "issueStatusTodo":"new,open",
            "issueStatusInProgress":"",
            "issueStatusDone":"resolved,closed",
            "issueStatusOther":"on hold,wontfix,duplicate,invalid"
          }
        }
      }
    ]
  ]
}
'
```

<a id="plugins-bitbucket_server--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-bitbucket_server--summary)
- [Supported Versions](#plugins-bitbucket_server--supported-versions)
- [Entities](#plugins-bitbucket_server--entities)
- [Metrics](#plugins-bitbucket_server--metrics)
- [Configuration](#plugins-bitbucket_server--configuration)
- [API Sample Request](#plugins-bitbucket_server--api-sample-request)
- [References](#plugins-bitbucket_server--references)

---

<a id="plugins-circleci"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/circleci/ -->

<!-- page_index: 96 -->

# CircleCI

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# CircleCI

<a id="plugins-circleci--summary"></a>

## Summary

This plugin collects various entities from CircleCI, including accounts, jobs, workflows, pipelines and projects.

<a id="plugins-circleci--supported-versions"></a>

## Supported Versions

Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-circleci--entities"></a>

## Entities

Check out the [CircleCI entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-circleci--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from CircleCI:

- [Build Count](#metrics-buildcount)
- [Build Duration](#metrics-buildduration)
- [Build Success Rate](#metrics-buildsuccessrate)
- [DORA - Deployment Frequency](#metrics-deploymentfrequency)
- [DORA - Lead Time for Changes](#metrics-leadtimeforchanges)
- [DORA - Median Time to Restore Service](#metrics-mttr)
- [DORA - Change Failure Rate](#metrics-cfr)

<a id="plugins-circleci--configuration"></a>

## Configuration

- Configuring CircleCI via [Config UI](#configuration-circleci)

<a id="plugins-circleci--api-sample-request"></a>

## API Sample Request

> Note: Please replace the `http://localhost:8080` in the sample requests with your actual DevLake API endpoint. For how to view DevLake API's swagger documentation, please refer to the "Using DevLake API" section of [Developer Setup](#developermanuals-developersetup).

You can trigger data collection by making a POST request to `/pipelines`.

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1",
  "plan": [
    [
      {
        "plugin": "circleci",
        "options": {
          "connectionId": 1,
          "fullName": "likyh/likyhphp",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":"",
            "issueStatusTodo":"new,open",
            "issueStatusInProgress":"",
            "issueStatusDone":"resolved,closed",
            "issueStatusOther":"on hold,wontfix,duplicate,invalid"
          }
        }
      }
    ]
  ]
}
'
```

<a id="plugins-circleci--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-circleci--summary)
- [Supported Versions](#plugins-circleci--supported-versions)
- [Entities](#plugins-circleci--entities)
- [Metrics](#plugins-circleci--metrics)
- [Configuration](#plugins-circleci--configuration)
- [API Sample Request](#plugins-circleci--api-sample-request)
- [References](#plugins-circleci--references)

---

<a id="plugins-customize"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/customize/ -->

<!-- page_index: 97 -->

# Customize

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Customize

<a id="plugins-customize--summary"></a>

## Summary

This plugin provides users the ability to:

- Add/delete columns in domain layer tables
- Insert values to certain columns with data extracted from some raw layer tables
- Import data from CSV files(only `issues` and `issue_commits` two tables are supported)

**NOTE:** The names of columns added via this plugin must start with the prefix `x_`

For now, only the following five types were supported:

- varchar(255)
- text
- bigint
- float
- timestamp
- array

<a id="plugins-customize--sample-request"></a>

## Sample Request

<a id="plugins-customize--trigger-data-extraction"></a>

### Trigger Data Extraction

To extract data, switch to `Advanced Mode` on the first step of creating a Blueprint and paste a JSON config as the following:

The example below demonstrates how to extract status name from the table `_raw_jira_api_issues`:

1. For non-array types: Extract the status name from the `_raw_jira_api_issues` table and assign it to the `x_test` column in the [issues](#datamodels-devlakedomainlayerschema--issues) table.
2. For array types: Extract the status name from the `_raw_jira_api_issues` table, and create a new [issue\_custom\_array\_fields](#datamodels-devlakedomainlayerschema--issue_custom_array_fields) table containing `issue_id`, `field_id`, and `value` columns. This table has a one-to-many relationship with the `issues` table. `issue_id` is the id corresponding to the issue, `x_test` corresponds to the `field_id` column, and the value of `x_test` corresponds to the `value` column.

We leverage the package `https://github.com/tidwall/gjson` to extract value from the JSON. For the extraction syntax, please refer to this [docs](https://github.com/tidwall/gjson/blob/master/SYNTAX.md)

- `table`: domain layer table name
- `rawDataTable`: raw layer table, from which we extract values by json path
- `rawDataParams`: the filter to select records from the raw layer table (**The value should be a string not an object**)
- `mapping`: the extraction rule; the key is the extension field name; the value is json path

```json
[
  [
    {
      "plugin":"customize",
      "options":{
        "transformationRules":[
          {
            "table":"issues",
            "rawDataTable":"_raw_jira_api_issues",
            "rawDataParams":"{\"ConnectionId\":1,\"BoardId\":8}",
            "mapping":{
              "x_test":"fields.status.name"
            }
          }
        ]
      }
    }
  ]
]
```

You can also trigger data extraction by making a POST request to `/pipelines`.

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "extract fields",
    "plan": [
        [
            {
                "plugin": "customize",
                "options": {
                    "transformationRules": [
                        {
                            "table": "issues",
                            "rawDataTable": "_raw_jira_api_issues",
                            "rawDataParams": "{\"ConnectionId\":1,\"BoardId\":8}",
                            "mapping": {
                                "x_test": "fields.status.name"
                            }
                        }
                    ]
                }
            }
        ]
    ]
}
'
```

<a id="plugins-customize--list-columns"></a>

### List Columns

Get all columns of the table `issues`

> GET /plugins/customize/issues/fields

**NOTE** some fields are omitted in the following example
response

```json
[
  {
    "columnName": "id",
    "displayName": "",
    "dataType": "varchar(255)",
    "description": ""
  },
  {
    "columnName": "created_at",
    "displayName": "",
    "dataType": "datetime(3)",
    "description": ""
  },
  {
    "columnName": "x_time",
    "displayName": "time",
    "dataType": "timestamp",
    "description": "test for time"
  },
  {
    "columnName": "x_int",
    "displayName": "bigint",
    "dataType": "bigint",
    "description": "test for int"
  },
  {
    "columnName": "x_float",
    "displayName": "float",
    "dataType": "float",
    "description": "test for float"
  },
  {
    "columnName": "x_text",
    "displayName": "text",
    "dataType": "text",
    "description": "test for text"
  },
  {
    "columnName": "x_varchar",
    "displayName": "varchar",
    "dataType": "varchar(255)",
    "description": "test for varchar"
  }
]
```

<a id="plugins-customize--create-a-customized-column"></a>

### Create a Customized Column

Create a new column `x_abc` with datatype `varchar(255)` for the table `issues`.

The value of `columnName` must start with `x_` and consist of no more than 50 alphanumerics and underscores.
The value of field `dataType` must be one of the following 5 types:

- varchar(255)
- text
- bigint
- float
- timestamp

> POST /plugins/customize/issues/fields
>
>
```json
{
  "columnName": "x_abc",
  "displayName": "ABC",
  "dataType": "varchar(255)",
  "description": "test field"
}
```

<a id="plugins-customize--drop-a-column"></a>

### Drop A Column

Drop the column `x_text` of the table `issues`

> DELETE /plugins/customize/issues/fields/x\_test

<a id="plugins-customize--upload-issuescsv-file"></a>

### Upload `issues.csv` file

> POST /plugins/customize/csvfiles/issues.csv

The HTTP `Content-Type` must be `multipart/form-data`, and the form should have three fields:

- `file`: The CSV file
- `boardId`: It will be written to the `id` field of the `boards` table, the `board_id` field of `board_issues`, and the `_raw_data_params` field of `issues`
- `boardName`: It will be written to the `name` field of the `boards` table

Upload a CSV file and import it to the `issues` table via this API. There should be no extra fields in the file except the `labels` field, and if the field value is `NULL`, it should be `NULL` in the CSV instead of the empty string.
DevLake will parse the CSV file and store it in the `issues` table, where the `labels` are stored in the `issue_labels` table.
If the `boardId` does not appear, a new record will be created in the boards table. The `board_issues` table will be updated at the same time as the import.
The following is an issues.CSV file sample:

<table><thead><tr><th>id</th><th>_raw_data_params</th><th>url</th><th>icon_url</th><th>issue_key</th><th>title</th><th>description</th><th>epic_key</th><th>type</th><th>status</th><th>original_status</th><th>story_point</th><th>resolution_date</th><th>created_date</th><th>updated_date</th><th>parent_issue_id</th><th>priority</th><th>original_estimate_minutes</th><th>time_spent_minutes</th><th>time_remaining_minutes</th><th>creator_id</th><th>creator_name</th><th>assignee_id</th><th>assignee_name</th><th>severity</th><th>component</th><th>lead_time_minutes</th><th>original_project</th><th>original_type</th><th>x_int</th><th>x_time</th><th>x_varchar</th><th>x_float</th><th>labels</th></tr></thead><tbody><tr><td>bitbucket:BitbucketIssue:1:1</td><td>board789</td><td><a href="https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/1" rel="noopener noreferrer" target="_blank">https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/1</a></td><td></td><td>1</td><td>issue test</td><td>bitbucket issues test for devlake</td><td></td><td>issue</td><td>TODO</td><td>new</td><td>0</td><td>NULL</td><td>2022-07-17 07:15:55.959+00:00</td><td>2022-07-17 09:11:42.656+00:00</td><td></td><td>major</td><td>0</td><td>0</td><td>0</td><td>bitbucket:BitbucketAccount:1:62abf394192edb006fa0e8cf</td><td>tgp</td><td>bitbucket:BitbucketAccount:1:62abf394192edb006fa0e8cf</td><td>tgp</td><td></td><td></td><td>NULL</td><td>NULL</td><td>NULL</td><td>10</td><td>2022-09-15 15:27:56</td><td>world</td><td>8</td><td>NULL</td></tr><tr><td>bitbucket:BitbucketIssue:1:10</td><td>board789</td><td><a href="https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/10" rel="noopener noreferrer" target="_blank">https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/10</a></td><td></td><td>10</td><td>issue test007</td><td>issue test007</td><td></td><td>issue</td><td>TODO</td><td>new</td><td>0</td><td>NULL</td><td>2022-08-12 13:43:00.783+00:00</td><td>2022-08-12 13:43:00.783+00:00</td><td></td><td>trivial</td><td>0</td><td>0</td><td>0</td><td>bitbucket:BitbucketAccount:1:62abf394192edb006fa0e8cf</td><td>tgp</td><td>bitbucket:BitbucketAccount:1:62abf394192edb006fa0e8cf</td><td>tgp</td><td></td><td></td><td>NULL</td><td>NULL</td><td>NULL</td><td>30</td><td>2022-09-15 15:27:56</td><td>abc</td><td>2456790</td><td>hello worlds</td></tr><tr><td>bitbucket:BitbucketIssue:1:13</td><td>board789</td><td><a href="https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/13" rel="noopener noreferrer" target="_blank">https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/13</a></td><td></td><td>13</td><td>issue test010</td><td>issue test010</td><td></td><td>issue</td><td>TODO</td><td>new</td><td>0</td><td>NULL</td><td>2022-08-12 13:44:46.508+00:00</td><td>2022-08-12 13:44:46.508+00:00</td><td></td><td>critical</td><td>0</td><td>0</td><td>0</td><td>bitbucket:BitbucketAccount:1:62abf394192edb006fa0e8cf</td><td>tgp</td><td></td><td></td><td></td><td></td><td>NULL</td><td>NULL</td><td>NULL</td><td>1</td><td>2022-09-15 15:27:56</td><td>NULL</td><td>0.00014</td><td>NULL</td></tr><tr><td>bitbucket:BitbucketIssue:1:14</td><td>board789</td><td><a href="https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/14" rel="noopener noreferrer" target="_blank">https://api.bitbucket.org/2.0/repositories/thenicetgp/lake/issues/14</a></td><td></td><td>14</td><td>issue test011</td><td>issue test011</td><td></td><td>issue</td><td>TODO</td><td>new</td><td>0</td><td>NULL</td><td>2022-08-12 13:45:12.810+00:00</td><td>2022-08-12 13:45:12.810+00:00</td><td></td><td>blocker</td><td>0</td><td>0</td><td>0</td><td>bitbucket:BitbucketAccount:1:62abf394192edb006fa0e8cf</td><td>tgp</td><td>bitbucket:BitbucketAccount:1:62abf394192edb006fa0e8cf</td><td>tgp</td><td></td><td></td><td>NULL</td><td>NULL</td><td>NULL</td><td>41534568464351</td><td>2022-09-15 15:27:56</td><td>NULL</td><td>NULL</td><td>label1,label2,label3</td></tr></tbody></table>
<a id="plugins-customize--upload-issue_commitscsv-file"></a>

### Upload `issue_commits.csv` file

> POST /plugins/customize/csvfiles/issue\_commits.csv

The `Content-Type` should be `multipart/form-data`, and the form should have two fields:

- `file`: The CSV file
- `boardId`: It will be written to the `_raw_data_params` field of `issue_commits`

The following is an issue\_commits.CSV file sample:

<table><thead><tr><th>issue_id</th><th>commit_sha</th></tr></thead><tbody><tr><td>jira:JiraIssue:1:10063</td><td>8748a066cbaf67b15e86f2c636f9931347e987cf</td></tr><tr><td>jira:JiraIssue:1:10064</td><td>e6bde456807818c5c78d7b265964d6d48b653af6</td></tr><tr><td>jira:JiraIssue:1:10065</td><td>8f91020bcf684c6ad07adfafa3d8a2f826686c42</td></tr><tr><td>jira:JiraIssue:1:10066</td><td>0dfe2e9ed88ad4e27f825d9b67d4d56ac983c5ef</td></tr><tr><td>jira:JiraIssue:1:10145</td><td>07aa2ebed68e286dc51a7e0082031196a6135f74</td></tr><tr><td>jira:JiraIssue:1:10145</td><td>d70d6687e06304d9b6e0cb32b3f8c0f0928400f7</td></tr><tr><td>jira:JiraIssue:1:10159</td><td>d28785ff09229ac9e3c6734f0c97466ab00eb4da</td></tr><tr><td>jira:JiraIssue:1:10202</td><td>0ab12c4d4064003602edceed900d1456b6209894</td></tr><tr><td>jira:JiraIssue:1:10203</td><td>980e9fe7bc3e22a0409f7241a024eaf9c53680dd</td></tr></tbody></table>

- [Summary](#plugins-customize--summary)
- [Sample Request](#plugins-customize--sample-request)
  - [Trigger Data Extraction](#plugins-customize--trigger-data-extraction)
  - [List Columns](#plugins-customize--list-columns)
  - [Create a Customized Column](#plugins-customize--create-a-customized-column)
  - [Drop A Column](#plugins-customize--drop-a-column)
  - [Upload `issues.csv` file](#plugins-customize--upload-issuescsv-file)
  - [Upload `issue_commits.csv` file](#plugins-customize--upload-issue_commitscsv-file)

---

<a id="plugins-dbt"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/dbt/ -->

<!-- page_index: 98 -->

# DBT

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# DBT

<a id="plugins-dbt--summary"></a>

## Summary

dbt (data build tool) enables analytics engineers to transform data in their warehouses by simply writing select statements. dbt handles turning these select statements into tables and views.
dbt does the T in ELT (Extract, Load, Transform) processes – it doesn’t extract or load data, but it’s extremely good at transforming data that’s already loaded into your warehouse.

<a id="plugins-dbt--user-setup"></a>

## User setup

- If you plan to use this product, you need to install some environments first.

<a id="plugins-dbt--required-packages-to-install"></a>

#### Required Packages to Install

- [python3.7+](https://www.python.org/downloads/)
- [dbt-mysql](https://pypi.org/project/dbt-mysql/#configuring-your-profile)

<a id="plugins-dbt--commands-to-run-or-create-in-your-terminal-and-the-dbt-project"></a>

#### Commands to run or create in your terminal and the dbt project

1. pip install dbt-mysql
2. dbt init demoapp (demoapp is project name)
3. create your SQL transformations and data models

<a id="plugins-dbt--convert-data-by-dbt"></a>

## Convert Data By DBT

Use the Raw JSON API to manually initiate a run using **cURL** or graphical API tool such as **Postman**. `POST` the following request to the DevLake API Endpoint.

```json
[
  [
    {
      "plugin": "dbt",
      "options": {
          "projectPath": "/Users/abeizn/demoapp",
          "projectName": "demoapp",
          "projectTarget": "dev",
          "selectedModels": ["my_first_dbt_model","my_second_dbt_model"],
          "projectVars": {
            "demokey1": "demovalue1",
            "demokey2": "demovalue2"
        }
      }
    }
  ]
]
```

- `projectPath`: the absolute path of the dbt project. (required)
- `projectName`: the name of the dbt project. (required)
- `projectTarget`: this is the default target your dbt project will use. (optional)
- `selectedModels`: a model is a select statement. Models are defined in .sql files, and typically in your models directory. (required)
  And selectedModels accepts one or more arguments. Each argument can be one of:

1. a package name, runs all models in your project, example: example
2. a model name, runs a specific model, example: my\_fisrt\_dbt\_model
3. a fully-qualified path to a directory of models.

- `projectVars`: variables to parametrize dbt models. (optional)
  example:
  `select * from events where event_type = '{{ var("event_type") }}'`
  To execute this SQL query in your model, you need set a value for `event_type`.

<a id="plugins-dbt--resources"></a>

### Resources:

- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers

- [Summary](#plugins-dbt--summary)
- [User setup](#plugins-dbt--user-setup)
- [Convert Data By DBT](#plugins-dbt--convert-data-by-dbt)
  - [Resources:](#plugins-dbt--resources)

---

<a id="plugins-feishu"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/feishu/ -->

<!-- page_index: 99 -->

# Feishu

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Feishu

<a id="plugins-feishu--summary"></a>

## Summary

This plugin collects Feishu meeting data through [Feishu Openapi](https://open.feishu.cn/document/home/user-identity-introduction/introduction).

<a id="plugins-feishu--supported-versions"></a>

## Supported Versions

Will be available for all versions. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-feishu--configuration"></a>

## Configuration

In order to fully use this plugin, you need to get `app_id` and `app_secret` from a Feishu administrator (for help on App info, please see [official Feishu Docs](https://open.feishu.cn/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal)).

A connection should be created before you can collect any data. Currently, this plugin supports creating connection by requesting the `connections` API:

```text
curl 'http://localhost:8080/plugins/feishu/connections' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "feishu",
    "endpoint": "https://open.feishu.cn/open-apis/vc/v1/",
    "proxy": "http://localhost:1080",
    "rateLimitPerHour": 20000,
    "appId": "<YOUR_APP_ID>",
    "appSecret": "<YOUR_APP_SECRET>"
}
'
```

<a id="plugins-feishu--collect-data-from-feishu"></a>

## Collect data from Feishu

To collect data, select `Advanced Mode` on the `Create Pipeline Run` page and paste a JSON config like the following:

```json
[
  [
    {
      "plugin": "feishu",
      "options": {
        "connectionId": 1,
        "numOfDaysToCollect" : 80
      }
    }
  ]
]
```

> `numOfDaysToCollect`: The number of days you want to collect

> `rateLimitPerSecond`: The number of requests to send(Maximum is 8)

You can also trigger data collection by making a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "feishu 20211126",
    "plan": [[{
      "plugin": "feishu",
      "options": {
        "connectionId": 1,
        "numOfDaysToCollect" : 80
      }
    }]]
}
'
```

- [Summary](#plugins-feishu--summary)
- [Supported Versions](#plugins-feishu--supported-versions)
- [Configuration](#plugins-feishu--configuration)
- [Collect data from Feishu](#plugins-feishu--collect-data-from-feishu)

---

<a id="plugins-gitee"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/gitee/ -->

<!-- page_index: 100 -->

# Gitee(WIP)

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Gitee(WIP)

<a id="plugins-gitee--summary"></a>

## Summary

This plugin collects `Gitee` data through [Gitee Openapi](https://gitee.com/api/v5/swagger).

<a id="plugins-gitee--supported-versions"></a>

## Supported Versions

Will be available for Gitee Cloud. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-gitee--configuration"></a>

## Configuration

In order to fully use this plugin, you need to get the `token` on the Gitee website.

A connection should be created before you can collect any data. Currently, this plugin supports creating connection by requesting the `connections` API:

```text
curl 'http://localhost:8080/plugins/gitee/connections' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "gitee",
    "endpoint": "https://gitee.com/api/v5/",
    "proxy": "http://localhost:1080",
    "rateLimitPerHour": 20000,
    "token": "<YOUR_TOKEN>"
}
'
```

<a id="plugins-gitee--collect-data-from-gitee"></a>

## Collect data from Gitee

In order to collect data, you have to compose a JSON looks like following one, and send it by selecting `Advanced Mode` on `Create Pipeline Run` page:

1. Configure-UI Mode

```json
[
  [
    {
      "plugin": "gitee",
      "options": {
        "connectionId": 1,
        "repo": "lake",
        "owner": "merico-dev"
      }
    }
  ]
]
```

and if you want to perform certain subtasks.

```json
[
  [
    {
      "plugin": "gitee",
      "subtasks": ["collectXXX", "extractXXX", "convertXXX"],
      "options": {
        "connectionId": 1,
        "repo": "lake",
        "owner": "merico-dev"
      }
    }
  ]
]
```

2. Curl Mode:
   You can also trigger data collection by making a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "gitee 20211126",
    "plan": [[{
        "plugin": "gitee",
        "options": {
            "connectionId": 1,
            "repo": "lake",
            "owner": "merico-dev"
        }
    }]]
}
'
```

and if you want to perform certain subtasks.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "gitee 20211126",
    "plan": [[{
        "plugin": "gitee",
        "subtasks": ["collectXXX", "extractXXX", "convertXXX"],
        "options": {
            "connectionId": 1,
            "repo": "lake",
            "owner": "merico-dev"
        }
    }]]
}
'
```

- [Summary](#plugins-gitee--summary)
- [Supported Versions](#plugins-gitee--supported-versions)
- [Configuration](#plugins-gitee--configuration)
- [Collect data from Gitee](#plugins-gitee--collect-data-from-gitee)

---

<a id="plugins-gitextractor"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/gitextractor/ -->

<!-- page_index: 101 -->

# GitExtractor

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# GitExtractor

<a id="plugins-gitextractor--summary"></a>

## Summary

This plugin extracts commits and references from a remote or local git repository. It then saves the data into the database or csv files.

<a id="plugins-gitextractor--steps-to-make-this-plugin-work"></a>

## Steps to make this plugin work

1. Use the Git repo extractor to retrieve data about commits and branches from your repository.
2. Use the GitHub plugin to retrieve data about Github issues and PRs from your repository.
   NOTE: you can run only one issue collection stage as described in the Github Plugin README.
3. Use the [RefDiff](#plugins-refdiff) plugin to calculate version diff, which will be stored in `refs_commits` table.

Note: If you do not want to collect commit files, you can bypass this step by setting the SKIP\_COMMIT\_FILES=true in the .env file. This will prevent the plugin from collecting commit file data.

<a id="plugins-gitextractor--sample-request"></a>

## Sample Request

```text
curl --location --request POST 'localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "git repo extractor",
    "plan": [
        [
            {
                "Plugin": "gitextractor",
                "Options": {
                    "url": "https://github.com/merico-dev/lake.git",
                    "repoId": "github:GithubRepo:384111310"
                }
            }
        ]
    ]
}
'
```

- `url`: the location of the git repository. It should start with `http`/`https` for a remote git repository and with `/` for a local one.
- `repoId`: column `id` of `repos`.
  Note : For GitHub, to find the repo id run `$("meta[name=octolytics-dimension-repository_id]").getAttribute('content')` in browser console.
- `proxy`: optional, http proxy, e.g. `http://your-proxy-server.com:1080`.
- `user`: optional, for cloning private repository using HTTP/HTTPS
- `password`: optional, for cloning private repository using HTTP/HTTPS
- `privateKey`: optional, for SSH cloning, base64 encoded `PEM` file
- `passphrase`: optional, passphrase for the private key

<a id="plugins-gitextractor--standalone-mode"></a>

## Standalone Mode

You call also run this plugin in a standalone mode without any DevLake service running using the following command:

```text
go run plugins/gitextractor/main.go -url https://github.com/merico-dev/lake.git -id github:GithubRepo:384111310 -db "merico:merico@tcp(127.0.0.1:3306)/lake?charset=utf8mb4&parseTime=True"
```

For more options (e.g., saving to a csv file instead of a db), please read `plugins/gitextractor/main.go`.

<a id="plugins-gitextractor--development"></a>

## Development

This plugin depends on `libgit2`, you need to install version 1.3.0 to run and debug this plugin on your local
machine.

<a id="plugins-gitextractor--linux"></a>

### Linux

```text
1. require cmake
[ubuntu]
apt install cmake -y
[centos]
yum install cmake -y

2. compiling
git clone -b v1.3.0 https://github.com/libgit2/libgit2.git && cd libgit2
mkdir build && cd build && cmake ..
make && make install

3.PKG_CONFIG and LD_LIBRARY_PATH
[centos]
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib64:/usr/local/lib64/pkgconfig
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib64
[ubuntu]
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib:/usr/local/lib/pkgconfig
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
```

<a id="plugins-gitextractor--troubleshooting-linux"></a>

#### Troubleshooting (Linux)

> Q: # pkg-config --cflags -- libgit2 Package libgit2 was not found in the pkg-config search path.
> Perhaps you should add the directory containing `libgit2.pc` to the PKG\_CONFIG\_PATH environment variable
> No package 'libgit2' found pkg-config: exit status 1

> A:
> Make sure your pkg config path covers the installation:
> if your libgit2.pc in `/usr/local/lib64/pkgconfig`(like centos)
>
> `export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib64:/usr/local/lib64/pkgconfig`
>
> else if your libgit2.pc in `/usr/local/lib/pkgconfig`(like ubuntu)
>
> `export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib:/usr/local/lib/pkgconfig`
>
> else consider install pkgconfig or rebuild the libgit2

<a id="plugins-gitextractor--macos"></a>

### MacOS

NOTE: **Do NOT** install libgit2 via `MacPorts` or `homebrew`, install from source instead.

```text
brew install cmake
git clone https://github.com/libgit2/libgit2.git
cd libgit2
git checkout v1.3.0
mkdir build
cd build
cmake ..
make
make install
```

<a id="plugins-gitextractor--troubleshooting-macos"></a>

#### Troubleshooting (MacOS)

> Q: I got an error saying: `pkg-config: exec: "pkg-config": executable file not found in $PATH`

> A:
>
> 1. Make sure you have pkg-config installed:
>
> `brew install pkg-config`
>
> 2. Make sure your pkg config path covers the installation:
>    `export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib:/usr/local/lib/pkgconfig`

- [Summary](#plugins-gitextractor--summary)
- [Steps to make this plugin work](#plugins-gitextractor--steps-to-make-this-plugin-work)
- [Sample Request](#plugins-gitextractor--sample-request)
- [Standalone Mode](#plugins-gitextractor--standalone-mode)
- [Development](#plugins-gitextractor--development)
  - [Linux](#plugins-gitextractor--linux)
  - [MacOS](#plugins-gitextractor--macos)

---

<a id="plugins-github"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/github/ -->

<!-- page_index: 102 -->

# GitHub

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# GitHub

<a id="plugins-github--summary"></a>

## Summary

This plugin collects GitHub data through [REST API](https://docs.github.com/en/rest/) and [GraphQL API](https://docs.github.com/en/graphql). It then computes and visualizes various DevOps metrics from the GitHub data, which helps tech leads, QA and DevOps engineers, and project managers to answer questions such as:

- Is this month more productive than last?
- How fast do we respond to customer requirements?
- Was our quality improved or not?

<a id="plugins-github--supported-versions"></a>

## Supported Versions

Available for GitHub Cloud. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-github--entities"></a>

## Entities

Check out the [GitHub entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-github--data-refresh-policy"></a>

## Data Refresh Policy

Check out the [data refresh policy](#overview-supporteddatasources--github) of this plugin.

<a id="plugins-github--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from GitHub:

- [Requirement Count](#metrics-requirementcount)
- [Requirement Lead Time](#metrics-requirementleadtime)
- [Requirement Delivery Rate](#metrics-requirementdeliveryrate)
- [Requirement Granularity](#metrics-requirementgranularity)
- [Bug Age](#metrics-bugage)
- [Bug Count per 1k Lines of Code](#metrics-bugcountper1klinesofcode)
- [Incident Age](#metrics-incidentage)
- [Incident Count per 1k Lines of Code](#metrics-incidentcountper1klinesofcode)
- [Commit Count](#metrics-commitcount)
- [Commit Author Count](#metrics-commitauthorcount)
- [Added Lines of Code](#metrics-addedlinesofcode)
- [Deleted Lines of Code](#metrics-deletedlinesofcode)
- [PR Count](#metrics-prcount)
- [PR Cycle Time](#metrics-prcycletime)
- [PR Coding Time](#metrics-prcodingtime)
- [PR Pickup Time](#metrics-prpickuptime)
- [PR Review Time](#metrics-prreviewtime)
- [PR Deploy Time](#metrics-prdeploytime)
- [PR Time To Merge](#metrics-prtimetomerge)
- [PR Merge Rate](#metrics-prmergerate)
- [PR Review Depth](#metrics-prreviewdepth)
- [PR Size](#metrics-prsize)
- [Build Count](#metrics-buildcount)
- [Build Duration](#metrics-buildduration)
- [Build Success Rate](#metrics-buildsuccessrate)
- [DORA - Deployment Frequency](#metrics-deploymentfrequency)
- [DORA - Lead Time for Changes](#metrics-leadtimeforchanges)
- [DORA - Median Time to Restore Service](#metrics-mttr)
- [DORA - Change Failure Rate](#metrics-cfr)

<a id="plugins-github--configuration"></a>

## Configuration

- Configuring GitHub via [Config UI](#configuration-github)
- Configuring GitHub via Config UI's [advanced mode](#configuration-advancedmode--1-github).

<a id="plugins-github--api-sample-request"></a>

## API Sample Request

You can trigger data collection by making a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1-BLUEPRINT",
  "blueprintId": 1,
  "plan": [
    [
      {
        "plugin": "github",
        "options": {
          "connectionId": 1,
          "scopeId": "384111310",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":"",
            "issueComponent":"",
            "issuePriority":"(high|medium|low)$",
            "issueSeverity":"",
            "issueTypeBug":"(bug)$",
            "issueTypeIncident":"",
            "issueTypeRequirement":"(feature|feature-request)$",
            "prBodyClosePattern":"",
            "prComponent":"",
            "prType":""
          }
        }
      }
    ]
  ]
}
'
```

or

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1-BLUEPRINT",
  "blueprintId": 1,
  "plan": [
    [
      {
        "plugin": "github",
        "options": {
          "connectionId": 1,
          "owner": "apache",
          "repo": "incubator-devlake",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":"",
            "issueComponent":"",
            "issuePriority":"(high|medium|low)$",
            "issueSeverity":"",
            "issueTypeBug":"(bug)$",
            "issueTypeIncident":"",
            "issueTypeRequirement":"(feature|feature-request)$",
            "prBodyClosePattern":"",
            "prComponent":"",
            "prType":""
          }
        }
      }
    ]
  ]
}
'
```

<a id="plugins-github--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-github--summary)
- [Supported Versions](#plugins-github--supported-versions)
- [Entities](#plugins-github--entities)
- [Data Refresh Policy](#plugins-github--data-refresh-policy)
- [Metrics](#plugins-github--metrics)
- [Configuration](#plugins-github--configuration)
- [API Sample Request](#plugins-github--api-sample-request)
- [References](#plugins-github--references)

---

<a id="plugins-gitlab"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/gitlab/ -->

<!-- page_index: 103 -->

# GitLab

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# GitLab

<a id="plugins-gitlab--summary"></a>

## Summary

This plugin collects GitLab data through [API](https://docs.gitlab.com/ee/api/). It then computes and visualizes various DevOps metrics from the GitLab data, which helps tech leads, QA and DevOps engineers, and project managers to answer questions such as:

- How long does it take for your codes to get merged?
- How much time is spent on code review?
- How long does it take for your codes to get merged?
- How much time is spent on code review?

<a id="plugins-gitlab--supported-versions"></a>

## Supported Versions

Available for GitLab Cloud, Community Edition 11+. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-gitlab--entities"></a>

## Entities

Check out the [GitLab entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-gitlab--data-refresh-policy"></a>

## Data Refresh Policy

Check out the [data refresh policy](#overview-supporteddatasources--gitlab) of this plugin.

<a id="plugins-gitlab--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from GitLab:

- [Commit Count](#metrics-commitcount)
- [Commit Author Count](#metrics-commitauthorcount)
- [Added Lines of Code](#metrics-addedlinesofcode)
- [Deleted Lines of Code](#metrics-deletedlinesofcode)
- [PR Count](#metrics-prcount)
- [PR Cycle Time](#metrics-prcycletime)
- [PR Coding Time](#metrics-prcodingtime)
- [PR Pickup Time](#metrics-prpickuptime)
- [PR Review Time](#metrics-prreviewtime)
- [PR Deploy Time](#metrics-prdeploytime)
- [PR Time To Merge](#metrics-prtimetomerge)
- [PR Merge Rate](#metrics-prmergerate)
- [PR Review Depth](#metrics-prreviewdepth)
- [PR Size](#metrics-prsize)
- [Build Count](#metrics-buildcount)
- [Build Duration](#metrics-buildduration)
- [Build Success Rate](#metrics-buildsuccessrate)
- [DORA - Deployment Frequency](#metrics-deploymentfrequency)
- [DORA - Lead Time for Changes](#metrics-leadtimeforchanges)
- [DORA - Median Time to Restore Service](#metrics-mttr)
- [DORA - Change Failure Rate](#metrics-cfr)

<a id="plugins-gitlab--configuration"></a>

## Configuration

- Configuring GitLab via [config-ui](#configuration-gitlab).
- Configuring GitLab via Config UI's [advanced mode](#configuration-advancedmode--2-gitlab).

<a id="plugins-gitlab--api-sample-request"></a>

## API Sample Request

You can trigger data collection by making a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1-BLUEPRINT",
  "blueprintId": 1,
  "plan": [
    [
      {
        "plugin": "gitlab",
        "options": {
          "connectionId": 1,
          "projectId": 33728042,
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":"",
            "issueComponent":"",
            "issuePriority":"(high|medium|low)$",
            "issueSeverity":"",
            "issueTypeBug":"(bug)$",
            "issueTypeIncident":"",
            "issueTypeRequirement":"(feature|feature-request)$",
            "prBodyClosePattern":"",
            "prComponent":"",
            "prType":""
          }
        }
      }
    ]
  ]
}
'
```

<a id="plugins-gitlab--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-gitlab--summary)
- [Supported Versions](#plugins-gitlab--supported-versions)
- [Entities](#plugins-gitlab--entities)
- [Data Refresh Policy](#plugins-gitlab--data-refresh-policy)
- [Metrics](#plugins-gitlab--metrics)
- [Configuration](#plugins-gitlab--configuration)
- [API Sample Request](#plugins-gitlab--api-sample-request)
- [References](#plugins-gitlab--references)

---

<a id="plugins-jenkins"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/jenkins/ -->

<!-- page_index: 104 -->

# Jenkins

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Jenkins

<a id="plugins-jenkins--summary"></a>

## Summary

This plugin collects Jenkins data through [Remote Access API](https://www.jenkins.io/doc/book/using/remote-access-api/). It then computes and visualizes various DevOps metrics from the Jenkins data, which helps tech leads and DevOps engineers to answer questions such as:

- What is the deployment frequency of your team?
- What is the build success rate?
- How long does it take for a code change to be deployed into production?

<a id="plugins-jenkins--supported-versions"></a>

## Supported Versions

Available for Jenkins v2.263.x+. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-jenkins--note"></a>

### Note

Please note that it is important to avoid [rerunning Jenkins builds in place](https://www.jenkins.io/doc/pipeline/tour/running-multiple-steps/#timeouts-retries-and-more), and instead ensure that each rerun has a unique build number. This is because rerunning builds with the same build number can lead to inconsistencies in the data collected by the Jenkins plugin.

<a id="plugins-jenkins--entities"></a>

## Entities

Check out the [Jenkins entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-jenkins--data-refresh-policy"></a>

## Data Refresh Policy

Check out the [data refresh policy](#overview-supporteddatasources--jenkins) of this plugin.

<a id="plugins-jenkins--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Jenkins:

- [Build Count](#metrics-buildcount)
- [Build Duration](#metrics-buildduration)
- [Build Success Rate](#metrics-buildsuccessrate)
- [DORA - Deployment Frequency](#metrics-deploymentfrequency)
- [DORA - Lead Time for Changes](#metrics-leadtimeforchanges)
- [DORA - Median Time to Restore Service](#metrics-mttr)
- [DORA - Change Failure Rate](#metrics-cfr)

<a id="plugins-jenkins--configuration"></a>

## Configuration

- Configuring Jenkins via [Config UI](#configuration-jenkins)
- Configuring Jenkins via Config UI's [advanced mode](#configuration-advancedmode--3-jenkins).

<a id="plugins-jenkins--api-sample-request"></a>

## API Sample Request

You can trigger data collection by making a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1-BLUEPRINT",
  "blueprintId": 1,
  "plan": [
    [
      {
        "plugin": "jenkins",
        "options": {
          "connectionId": 1,
          "scopeId": "auto_deploy",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":""
          }
        }
      }
    ]
  ]
}
'
```

or

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1-BLUEPRINT",
  "blueprintId": 2,
  "plan": [
    [
      {
        "plugin": "jenkins",
        "options": {
          "connectionId": 1,
          "jobFullName": "auto_deploy",
          "transformationRules":{
            "deploymentPattern":"",
            "productionPattern":""
          }
        }
      }
    ]
  ]
}
'
```

<a id="plugins-jenkins--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-jenkins--summary)
- [Supported Versions](#plugins-jenkins--supported-versions)
  - [Note](#plugins-jenkins--note)
- [Entities](#plugins-jenkins--entities)
- [Data Refresh Policy](#plugins-jenkins--data-refresh-policy)
- [Metrics](#plugins-jenkins--metrics)
- [Configuration](#plugins-jenkins--configuration)
- [API Sample Request](#plugins-jenkins--api-sample-request)
- [References](#plugins-jenkins--references)

---

<a id="plugins-jira"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/jira/ -->

<!-- page_index: 105 -->

# Jira

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Jira

<a id="plugins-jira--summary"></a>

## Summary

This plugin collects Jira data through Jira REST API. It then computes and visualizes various engineering metrics from the Jira data.

<a id="plugins-jira--supported-versions"></a>

## Supported Versions

Available for Jira Cloud, Sever/Data Center 7.x, 8.x. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-jira--entities"></a>

## Entities

Check out the [Jira entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-jira--data-refresh-policy"></a>

## Data Refresh Policy

Check out the [data refresh policy](#overview-supporteddatasources--jira) of this plugin.

<a id="plugins-jira--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Jira:

- [Requirement Count](#metrics-requirementcount)
- [Requirement Lead Time](#metrics-requirementleadtime)
- [Requirement Delivery Rate](#metrics-requirementdeliveryrate)
- [Requirement Granularity](#metrics-requirementgranularity)
- [Bug Age](#metrics-bugage)
- [Bug Count per 1k Lines of Code](#metrics-bugcountper1klinesofcode)
- [Incident Age](#metrics-incidentage)
- [Incident Count per 1k Lines of Code](#metrics-incidentcountper1klinesofcode)

<a id="plugins-jira--configuration"></a>

## Configuration

- Configuring Jira via [config-ui](#configuration-jira).
- Configuring Jira via Config UI's [advanced mode](#configuration-advancedmode--4-jira).

<a id="plugins-jira--api-sample-request"></a>

## API Sample Request

You can trigger data collection by making a POST request to `/pipelines`.

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "MY PIPELINE",
  "plan": [
    [
      {
        "plugin": "jira",
        "options": {
          "connectionId": 1,
          "boardId": 8,
          "transformationRules": {
            "epicKeyField": "",
            "storyPointField": "",
            "remotelinkCommitShaPattern": "",
            "typeMappings": {
              "10040": {
                "standardType": "Incident",
                "statusMappings": null
              }
            }
          }
        }
      }
    ]
  ]
}
'
```

- [Summary](#plugins-jira--summary)
- [Supported Versions](#plugins-jira--supported-versions)
- [Entities](#plugins-jira--entities)
- [Data Refresh Policy](#plugins-jira--data-refresh-policy)
- [Metrics](#plugins-jira--metrics)
- [Configuration](#plugins-jira--configuration)
- [API Sample Request](#plugins-jira--api-sample-request)

---

<a id="plugins-linker"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/linker/ -->

<!-- page_index: 106 -->

# Linker

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Linker

This document comprehensively explains Linker and provides guidance on implementing this powerful and practical framework in DevLake.

<a id="plugins-linker--summary"></a>

## Summary

Just like the DORA plugin, the linker works on the domain layer and attempts to link the domain layer data.

For example, in the current version, the linker uses regular expressions to extract issue\_keys from pull requests' title and description fields, and it tries to relate existing issues with PRs, storing the relations in the `pull_request_issues` table.

<a id="plugins-linker--supported-versions"></a>

## Supported Versions

The linker was added in release v1.0.0-beta10 and has been available ever since.

<a id="plugins-linker--configuration"></a>

## Configuration

You can find it on the project settings page.
![](assets/images/linker-configuration-b9cb41b8d5f12acb77c067bd2ebfc049_d9f883c20af1047a.png)

- [Summary](#plugins-linker--summary)
- [Supported Versions](#plugins-linker--supported-versions)
- [Configuration](#plugins-linker--configuration)

---

<a id="plugins-opsgenie"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/opsgenie/ -->

<!-- page_index: 107 -->

# Opsgenie

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Opsgenie

<a id="plugins-opsgenie--summary"></a>

## Summary

This plugin collects Opsgenie incident data, users and teams, and uses them to compute incident-type DORA metrics. Namely,

- [Median time to restore service](#metrics-mttr)
- [Change failure rate](#metrics-cfr).
- [Incident Age](#metrics-incidentage)
- [Incident Count Per 1k Lines of Code](#metrics-incidentcountper1klinesofcode)

<a id="plugins-opsgenie--supported-versions"></a>

## Supported Versions

Available for Atlassian Opsgenie Cloud, for both US or EU instances. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-opsgenie--configuration"></a>

## Configuration

- Configure Opsgenie via Config UI. See instructions [here](#configuration-opsgenie).
- Configure Opsgenie via Config UI's [advanced mode](#configuration-advancedmode).

- [Summary](#plugins-opsgenie--summary)
- [Supported Versions](#plugins-opsgenie--supported-versions)
- [Configuration](#plugins-opsgenie--configuration)

---

<a id="plugins-pagerduty"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/pagerduty/ -->

<!-- page_index: 108 -->

# PagerDuty

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# PagerDuty

<a id="plugins-pagerduty--summary"></a>

## Summary

This plugin collects all incidents from PagerDuty, and uses them to compute incident-type DORA metrics. Namely,

- [Median time to restore service](#metrics-mttr)
- [Change failure rate](#metrics-cfr).
- [Incident Age](#metrics-incidentage)
- [Incident Count Per 1k Lines of Code](#metrics-incidentcountper1klinesofcode)

<a id="plugins-pagerduty--supported-versions"></a>

## Supported Versions

Available for PagerDuty Cloud. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-pagerduty--configuration"></a>

## Configuration

- Configure PagerDuty via Config UI. See instructions [here](#configuration-pagerduty).
- Configure PagerDuty via Config UI's [advanced mode](#configuration-advancedmode).

- [Summary](#plugins-pagerduty--summary)
- [Supported Versions](#plugins-pagerduty--supported-versions)
- [Configuration](#plugins-pagerduty--configuration)

---

<a id="plugins-refdiff"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/refdiff/ -->

<!-- page_index: 109 -->

# RefDiff

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# RefDiff

<a id="plugins-refdiff--summary"></a>

## Summary

RefDiff is a plugin that performs calculation tasks and has 2 main purposes.

- Calculate the difference in commits between releases/tags to [analyze the amount of code in each release](https://github.com/apache/incubator-devlake/blob/main/backend/plugins/refdiff/tasks/commit_diff_calculator.go)
- Calculate the difference in commits between deployments to [calculate DORA metrics](https://github.com/apache/incubator-devlake/blob/main/backend/plugins/refdiff/tasks/deployment_commit_diff_calculator.go)

And the output of RefDiff is stored in the table commits\_diffs, finished\_commits\_diffs, ref\_commits.

<a id="plugins-refdiff--important-note"></a>

## Important Note

You need to run `gitextractor` before the `refdiff` plugin. The `gitextractor` plugin should create records in the `refs` table in your database before this plugin can be run.

<a id="plugins-refdiff--configuration"></a>

## Configuration

This is an enrichment plugin based on the domain layer data, no configuration is needed.

<a id="plugins-refdiff--how-to-use-refdiff"></a>

## How to use refdiff

To trigger the enrichment, you need to insert a new task into your pipeline.

1. Make sure `commits` and `refs` are collected into your database, `refs` table should contain records like following:


```text
id                                            ref_type
github:GithubRepo:1:384111310:refs/tags/0.3.5   TAG
github:GithubRepo:1:384111310:refs/tags/0.3.6   TAG
github:GithubRepo:1:384111310:refs/tags/0.5.0   TAG
github:GithubRepo:1:384111310:refs/tags/v0.0.1  TAG
github:GithubRepo:1:384111310:refs/tags/v0.2.0  TAG
github:GithubRepo:1:384111310:refs/tags/v0.3.0  TAG
github:GithubRepo:1:384111310:refs/tags/v0.4.0  TAG
github:GithubRepo:1:384111310:refs/tags/v0.6.0  TAG
github:GithubRepo:1:384111310:refs/tags/v0.6.1  TAG
```

2. If you want to run calculatePrCherryPick, please configure GITHUB\_PR\_TITLE\_PATTERN in .env, you can check the example in .env.example(we have a default value, please make sure your pattern is disclosed by single quotes '')
3. And then, trigger a pipeline like the following format:

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "test-refdiff",
    "plan": [
        [
            {
                "plugin": "refdiff",
                "options": {
                    "repoId": "github:GithubRepo:1:384111310",
                    "pairs": [
                       { "newRef": "refs/tags/v0.6.0", "oldRef": "refs/tags/0.5.0" },
                       { "newRef": "refs/tags/0.5.0", "oldRef": "refs/tags/0.4.0" }
                    ],
                    "tasks": [
                        "calculateCommitsDiff",
                        "calculateIssuesDiff",
                        "calculatePrCherryPick",
                    ]
                }
            }
        ]
    ]
}'
```

Or if you preferred calculating latest releases

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "test-refdiff",
    "plan": [
        [
            {
                "plugin": "refdiff",
                "options": {
                    "repoId": "github:GithubRepo:1:384111310",
                    "tagsPattern": "v\d+\.\d+.\d+",
                    "tagsLimit": 10,
                    "tagsOrder": "reverse semver",
                    "tasks": [
                        "calculateCommitsDiff",
                        "calculateIssuesDiff",
                        "calculatePrCherryPick",
                    ]
                }
            }
        ]
    ]
}'
```

<a id="plugins-refdiff--how-to-use-refdiff-in-dora"></a>

## How to use refdiff in DORA

RefDiff can be called by the [DORA plugin](https://github.com/apache/incubator-devlake/tree/main/backend/plugins/dora) to support the calculation of [DORA metrics](https://devlake.apache.org/docs/DORA). RefDiff has a subtask called 'calculateProjectDeploymentCommitsDiff'. This subtask takes the `project_name` from task options to calculate the commits diff between two consecutive deployments in this project. That is to say, refdiff will generate the relationship between `deployed commit(s)` and the `deployment` in which these commits get deployed.

```shell
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "test-refdiff-dora",
    "plan": [
        [
            {
                "plugin": "refdiff",
                "options": {
                    "projectName": "project_name_1",
                    "tasks": [
                        "calculateProjectDeploymentCommitsDiff"
                    ]
                }
            }
        ]
    ]
}'
```

<a id="plugins-refdiff--development"></a>

## Development

This plugin depends on `libgit2`, you need to install version 1.3.0 in order to run and debug this plugin on your local
machine. [Click here](#plugins-gitextractor--development) for a brief guide.

- [Summary](#plugins-refdiff--summary)
- [Important Note](#plugins-refdiff--important-note)
- [Configuration](#plugins-refdiff--configuration)
- [How to use refdiff](#plugins-refdiff--how-to-use-refdiff)
- [How to use refdiff in DORA](#plugins-refdiff--how-to-use-refdiff-in-dora)
- [Development](#plugins-refdiff--development)

---

<a id="plugins-sonarqube"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/sonarqube/ -->

<!-- page_index: 110 -->

# SonarQube

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# SonarQube

<a id="plugins-sonarqube--summary"></a>

## Summary

This plugin collects SonarQube data through its REST APIs. SonarQube is a tool for static code analysis and code quality management. It can help you discover potential problems and defects in your code, and provide suggestions and solutions.

When collecting issues under a certain SonarQube project, divide the issues into smaller groups to collect, so as not to obtain 10,000 issues at once and exceed the result limit of SonarQube APIs themselves. Specific rules include:

1. First, classify the issues according to "severity", "status", and "type" and collect them separately.
2. Secondly, issues are classified according to the time fields "createdBefore" and "createdAfter" and collected separately.
3. Finally, the issues are classified according to "the file to which the issue belongs" and collected separately.

<a id="plugins-sonarqube--supported-versions"></a>

## Supported Versions

Available for SonarQube Server v8.x, v9.x. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-sonarqube--entities"></a>

## Entities

Check out the [SonarQube entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-sonarqube--data-refresh-policy"></a>

## Data Refresh Policy

Check out the [data refresh policy](#overview-supporteddatasources--sonarqube) of this plugin.

<a id="plugins-sonarqube--metrics"></a>

## Metrics

Most of SonarQube metrics are collected and can be found in DevLake's SonarQube dashboard.

- [Code Quality Issue Count](#metrics-cqissuecount)
- [Code Quality Test](#metrics-cqtest)
- [Code Quality Maintainability-Debt](#metrics-cqmaintainability-debt)
- [Code Quality Duplicated Blocks](#metrics-cqduplicatedblocks)
- [Code Quality Duplicated Lines](#metrics-cqduplicatedlines)

<a id="plugins-sonarqube--configuration"></a>

## Configuration

- Configuring SonarQube via [config-ui](#configuration-sonarqube).
- Configuring SonarQube via Config UI's [advanced mode](#configuration-advancedmode--10-sonarqube).

<a id="plugins-sonarqube--api-sample-request"></a>

## API Sample Request

You can trigger data collection by making a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "name": "project1-BLUEPRINT",
  "blueprintId": 1,
  "plan": [
    [
      {
        "plugin": "sonarqube",
        "options": {
          "connectionId": 1,
           "projectKey": "testDevLake"
        }
      }
    ]
  ]
}
'
```

<a id="plugins-sonarqube--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-sonarqube--summary)
- [Supported Versions](#plugins-sonarqube--supported-versions)
- [Entities](#plugins-sonarqube--entities)
- [Data Refresh Policy](#plugins-sonarqube--data-refresh-policy)
- [Metrics](#plugins-sonarqube--metrics)
- [Configuration](#plugins-sonarqube--configuration)
- [API Sample Request](#plugins-sonarqube--api-sample-request)
- [References](#plugins-sonarqube--references)

---

<a id="plugins-tapd"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/tapd/ -->

<!-- page_index: 111 -->

# TAPD

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# TAPD

<a id="plugins-tapd--summary"></a>

## Summary

This plugin collects TAPD data through its REST APIs. TAPD is an issue-tracking tool similar to Jira.

<a id="plugins-tapd--supported-versions"></a>

## Supported Versions

Advanced mode available for Tapd Cloud. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-tapd--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Tapd:

- [Requirement Count](#metrics-requirementcount)
- [Requirement Lead Time](#metrics-requirementleadtime)
- [Requirement Delivery Rate](#metrics-requirementdeliveryrate)
- [Bug Age](#metrics-bugage)
- [Incident Age](#metrics-incidentage)

<a id="plugins-tapd--configuration"></a>

## Configuration

- Configuring Tapd via [config-ui](#configuration-tapd).
- Configuring Tapd via Config UI's [advanced mode](#configuration-advancedmode--6-tapd).

- [Summary](#plugins-tapd--summary)
- [Supported Versions](#plugins-tapd--supported-versions)
- [Metrics](#plugins-tapd--metrics)
- [Configuration](#plugins-tapd--configuration)

---

<a id="plugins-teambition"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/teambition/ -->

<!-- page_index: 112 -->

# Teambition(WIP)

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Teambition(WIP)

<a id="plugins-teambition--summary"></a>

## Summary

This plugin collects Teambition data through its REST APIs. Teambition is an issue-tracking tool similar to Trello.

<a id="plugins-teambition--supported-versions"></a>

## Supported Versions

Available for Teambition Cloud. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-teambition--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Teambition:

- [Requirement Count](#metrics-requirementcount)
- [Requirement Lead Time](#metrics-requirementleadtime)
- [Requirement Delivery Rate](#metrics-requirementdeliveryrate)
- [Bug Age](#metrics-bugage)
- [Incident Age](#metrics-incidentage)

<a id="plugins-teambition--configuration"></a>

## Configuration

- Configuring Teambition via [config-ui](#configuration-teambition).
- Configuring Teambition via Config UI's [advanced mode](#configuration-advancedmode--11-teambition).

- [Summary](#plugins-teambition--summary)
- [Supported Versions](#plugins-teambition--supported-versions)
- [Metrics](#plugins-teambition--metrics)
- [Configuration](#plugins-teambition--configuration)

---

<a id="plugins-trello"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/trello/ -->

<!-- page_index: 113 -->

# Trello(WIP)

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Trello(WIP)

<a id="plugins-trello--summary"></a>

## Summary

This plugin collects `Trello` data through [Trello's rest api](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

<a id="plugins-trello--configuration"></a>

## Configuration

In order to fully use this plugin, you will need to get `apikey` and `token` on the [Trello website](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/).

A connection should be created before you can collect any data. Currently, this plugin supports creating connection by requesting `connections` API:

```text
curl 'http://localhost:8080/plugins/trello/connections' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name": "trello",
    "endpoint": "https://api.trello.com/",
    "rateLimitPerHour": 20000,
    "appId": "<YOUR_APIKEY>",
    "secretKey": "<YOUR_TOKEN>"
}
'
```

<a id="plugins-trello--collect-data-from-trello"></a>

## Collect data from Trello

You can make the following request to get all the boards.

```text
curl 'http://localhost:8080/plugins/trello/connections/<CONNECTION_ID>/proxy/rest/1/members/me/boards?fields=name,id'
```

In order to collect data, you have to compose a JSON looks like following one, and send it by selecting `Advanced Mode` on `Create Pipeline Run` page:

1. Configure-UI Mode

```json
[
  [
    {
      "plugin": "trello",
      "options": {
        "connectionId": <CONNECTION_ID>,
        "boardId": "<BOARD_ID>"
      }
    }
  ]
]
```

and if you want to perform certain subtasks.

```json
[
  [
    {
      "plugin": "trello",
      "subtasks": ["collectXXX", "extractXXX", "convertXXX"],
      "options": {
        "connectionId": <CONNECTION_ID>,
        "boardId": "<BOARD_ID>"
      }
    }
  ]
]
```

2. Curl Mode:

In order to collect data, you have to make a POST request to `/pipelines`.

```text
curl 'http://localhost:8080/pipelines' \
--header 'Content-Type: application/json' \
--data-raw '
{
    "name":"MY PIPELINE",
    "plan":[
        [
            {
                "plugin":"trello",
                "options":{
                    "connectionId":<CONNECTION_ID>,
                    "boardId":"<BOARD_ID>"
                }
            }
        ]
    ]
}
'
```

You can make the following request to get all the boards.

```text
curl 'http://localhost:8080/plugins/trello/connections/<CONNECTION_ID>/proxy/rest/1/members/me/boards?fields=name,id'
```

- [Summary](#plugins-trello--summary)
- [Configuration](#plugins-trello--configuration)
- [Collect data from Trello](#plugins-trello--collect-data-from-trello)

---

<a id="plugins-webhook"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/webhook/ -->

<!-- page_index: 114 -->

# Webhook

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Webhook

<a id="plugins-webhook--summary"></a>

## Summary

Incoming Webhooks are your solution to bring data to Apache DevLake when there isn't a specific plugin ready for your DevOps tool. An Incoming Webhook allows users to actively push data to DevLake.

When you create an Incoming Webhook within DevLake, DevLake generates a unique URL. You can then post JSON payloads to this URL to push data directly to your DevLake instance.

In v0.14+, users can push "incidents" and "deployments" required by DORA metrics to DevLake via Incoming Webhooks.

Webhooks are meant to be used at the lowest level that you want to relate incidents with deployments. For example, if you want to relate incidents at the individual service level, you will need a webhook per service. If you wish to relate incidents at the product level, you will need a webhook for the product. This is because incidents on a project will be related to the last deployment on the project with a timestamp that is before the incident's timestamp. This is true regardless of the source of incidents or deployments.

Note: If you post incidents using webhook due to your tool not being supported but your deployments are collected via plugins automatically, you need to re-collect data for deployments for the posted incidents to get mapped to deployments based on timestamps. This is required for Change Failure Rate (DORA) metric to show up correctly for the project.

Diagram of the relationship between incidents and deployments:

![Change Failure Reporting](assets/images/cfr-definition-94d92cc75f857f183443ad5390d31d65_905723ec0f096f50.png)

<a id="plugins-webhook--entities"></a>

## Entities

Check out the [Incoming Webhooks entities](#overview-supporteddatasources--data-collection-scope-by-each-plugin) collected by this plugin.

<a id="plugins-webhook--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Incoming Webhooks:

- [Requirement Delivery Rate](#metrics-requirementdeliveryrate)
- [Requirement Granularity](#metrics-requirementgranularity)
- [Bug Age](#metrics-bugage)
- [Bug Count per 1k Lines of Code](#metrics-bugcountper1klinesofcode)
- [Incident Age](#metrics-incidentage)
- [Incident Count per 1k Lines of Code](#metrics-incidentcountper1klinesofcode)
- [DORA - Deployment Frequency](#metrics-deploymentfrequency)
- [DORA - Lead Time for Changes](#metrics-leadtimeforchanges)
- [DORA - Median Time to Restore Service](#metrics-mttr)
- [DORA - Change Failure Rate](#metrics-cfr)

<a id="plugins-webhook--configuration"></a>

## Configuration

- Configuring Incoming Webhooks via [Config UI](#configuration-webhook)

<a id="plugins-webhook--api-sample-request"></a>

## API Sample Request

<a id="plugins-webhook--deployment"></a>

### Deployment

If you want to collect deployment data from your system, you can use the incoming webhooks for deployment.

<a id="plugins-webhook--payload-schema"></a>

#### Payload Schema

You can copy the generated deployment curl commands to your CI/CD script to post deployments to Apache DevLake. Below is the detailed payload schema:

<table><thead><tr><th align="center">Key</th><th align="center">Required</th><th>Notes</th></tr></thead><tbody><tr><td align="center">id</td><td align="center">✔️ Yes</td><td>This will be the unique ID of table cicd_deployments. This key replaced pipeline_id for clarity.</td></tr><tr><td align="center">createdDate</td><td align="center">✖️ No</td><td>The time this deploy pipeline starts. E.g. 2020-01-01T12:00:00+00:00  No default value.</td></tr><tr><td align="center">startedDate</td><td align="center">✔️ Yes</td><td>The time when the first deploy to a certain repo starts. E.g. 2020-01-01T12:00:00+00:00  No default value.</td></tr><tr><td align="center">finishedDate</td><td align="center">✔️ Yes</td><td>The time when the last deploy to a certain repo ends. E.g. 2020-01-01T12:00:00+00:00  No default value.</td></tr><tr><td align="center">environment</td><td align="center">✖️ No</td><td>The environment this deployment happens. For example, <code>PRODUCTION</code> <code>STAGING</code> <code>TESTING</code> <code>DEVELOPMENT</code>.
The default value is <code>PRODUCTION</code></td></tr><tr><td align="center">result</td><td align="center">✖️ No</td><td>deployment result, one of the values : <code>SUCCESS</code>, <code>FAILURE</code>, <code>ABORT</code>, <code>MANUAL</code>,
 The default value is <code>SUCCESS</code>.</td></tr><tr><td align="center">displayTitle</td><td align="center">✖️ No</td><td>A readable title for the deployment.</td></tr><tr><td align="center">name</td><td align="center">✖️ No</td><td>Deprecated.</td></tr><tr><td align="center">deploymentCommits.repoUrl</td><td align="center">✔️ Yes</td><td>The repo URL of the deployment commit
If there is a row in the domain layer table <code>repos</code> where <code>repos.url</code> equals <code>repo_url</code>, the <code>repoId</code> will be filled with <code>repos.id</code>.</td></tr><tr><td align="center">deploymentCommits.repoId</td><td align="center">✖️ No</td><td>Deprecated.</td></tr><tr><td align="center">deploymentCommits.refName</td><td align="center">✖️ No</td><td>The branch/tag to deploy   No default value.</td></tr><tr><td align="center">deploymentCommits.startedDate</td><td align="center">✔️ Yes</td><td>The start time of the deploy to this repo. E.g. 2020-01-01T12:00:00+00:00  No default value.</td></tr><tr><td align="center">deploymentCommits.finishedDate</td><td align="center">✔️ Yes</td><td>The end time of the deploy to this repo. E.g. 2020-01-01T12:00:00+00:00  No default value.</td></tr><tr><td align="center">deploymentCommits.commitSha</td><td align="center">✔️ Yes</td><td>Commit sha that triggers the deploy in this repo</td></tr><tr><td align="center">deploymentCommits.commitMsg</td><td align="center">✖️ No</td><td>Commit sha of the deployment commit message</td></tr><tr><td align="center">deploymentCommits.result</td><td align="center">✖️ No</td><td>The result of the deploy to this repo. The default value is 'SUCCESS'</td></tr><tr><td align="center">deploymentCommits.displayTitle</td><td align="center">✖️ No</td><td>A readable title for the deployment to this repo.</td></tr><tr><td align="center">deploymentCommits.name</td><td align="center">✖️ No</td><td>Deprecated.</td></tr></tbody></table>

More information about these columns at the domain layer tables: [cicd\_deployments](#datamodels-devlakedomainlayerschema--cicd_deployments) and [cicd\_deployment\_commits](#datamodels-devlakedomainlayerschema--cicd_deployment_commits).

<a id="plugins-webhook--register-a-deployment-sample-api-calls"></a>

#### Register a Deployment - Sample API Calls

The payload supports the deployment to one or multiple repositories (referring to the [discussion](https://github.com/apache/incubator-devlake/discussions/6162)).

Please replace the `API_KEY` with the real token generated after creating a webhook.

```text
curl <devlake-host>/api/rest/plugins/webhook/1/deployments -X 'POST' -H 'Authorization: Bearer {API_KEY}' -d '{
    "id": "required-id",
    "createdDate":"2020-01-01T11:00:00+00:00",
    "startedDate":"2020-01-01T12:00:00+00:00",
    "finishedDate":"2020-01-02T13:00:00+00:00",
    "environment":"PRODUCTION",
    "result": "SUCCESS",
    "displayTitle":"optional-custom-deploy-display-title",
    "name": "optional-deployment-name. If you do not post a name, DevLake will generate one for you.",
    "deploymentCommits":[
       {
           "repoUrl":"required-repo-url",
           "refName": "optional-release-v0.17",
           "startedDate":"2020-01-01T11:00:00+00:00",
           "finishedDate":"2020-01-02T11:00:00+00:00",
           "commitSha":"c1",
           "commitMsg":"optional-msg-1",
           "result":"SUCCESS",
           "name":"optional, if null, it will be deployment for {commit_sha}",
           "displayTitle":"optional-custom-deployment-commit-display-title-1"
       },
       {
           "repoUrl":"repo-2",
           "refName": "optional-release-v0.17",
           "startedDate":"2020-01-01T11:00:00+00:00",
           "finishedDate":"2020-01-02T11:00:00+00:00",
           "commitSha":"c2",
           "commitMsg":"optional-msg-2",
           "result":"FAILURE",
           "name":"optional, if null, it will be deployment for {commit_sha}",
           "displayTitle":"optional-custom-deployment-commit-display-title-2"
       }
    ]
  }'
```

<a id="plugins-webhook--a-real-world-example-push-circleci-deployments-to-devlake"></a>

#### A real-world example - Push CircleCI deployments to DevLake

The following demo shows how to post "deployments" to DevLake from CircleCI. In this example, the CircleCI job 'deploy' is used to manage deployments.

```text
version: 2.1

jobs:
  build:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: "build"
          command: |
            echo Hello, World!

  deploy:
    docker:
      - image: cimg/base:stable
    steps:
      - checkout
      - run:
          name: "deploy"
          command: |
            # The time a deploy started
            started_date=`date '+%Y-%m-%dT%H:%M:%S%z'`

            # Some deployment tasks here ...
            echo Hello, World!

            # Send the request to DevLake after deploy
            # The values start with a '$CIRCLE_' are CircleCI's built-in variables
            curl <devlake-host>/api/rest/plugins/webhook/1/deployments -X 'POST' -d "{
              \"id\": \"$PIPELINE_ID\",
              \"startedDate\":\"$started_date\",
              \"finishedDate\":\"$finished_date\",
              \"deploymentCommits\":\[
                \{
                  \"commitSha\":\"$CIRCLE_SHA1\",
                  \"repoUrl\":\"$CIRCLE_REPOSITORY_URL\",
                \}
              \]
            }"

workflows:
  build_and_deploy_workflow:
    jobs:
      - build
      - deploy
```

<a id="plugins-webhook--incident-issue"></a>

### Incident / Issue

If you want to collect issue or incident data from your system, you can use the two webhooks for issues.

<a id="plugins-webhook--register-issues-update-or-create-issues"></a>

#### Register Issues - Update or Create Issues

`POST <devlake-host>/api/rest/plugins/webhook/1/issues`

needs to be called when an issue or incident is created. The body should be a JSON and include columns as follows:

<table><thead><tr><th align="center">Keyname</th><th align="center">Required</th><th>Notes</th></tr></thead><tbody><tr><td align="center">url</td><td align="center">✖️ No</td><td>Issue's URL</td></tr><tr><td align="center">issueKey</td><td align="center">✔️ Yes</td><td>Issue's key, needs to be unique in a connection</td></tr><tr><td align="center">title</td><td align="center">✔️ Yes</td><td></td></tr><tr><td align="center">description</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">epicKey</td><td align="center">✖️ No</td><td>Issue's epic</td></tr><tr><td align="center">type</td><td align="center">✖️ No</td><td>Type, such as <code>INCIDENT</code>, <code>BUG</code>, <code>REQUIREMENT</code></td></tr><tr><td align="center">status</td><td align="center">✔️ Yes</td><td>Issue's status. Must be one of <code>TODO</code> <code>DONE</code> <code>IN_PROGRESS</code></td></tr><tr><td align="center">originalStatus</td><td align="center">✔️ Yes</td><td>Status in your tool, such as created/open/closed/...</td></tr><tr><td align="center">storyPoint</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">resolutionDate</td><td align="center">✖️ No</td><td>Resolved date, Format should be 2020-01-01T12:00:00+00:00</td></tr><tr><td align="center">createdDate</td><td align="center">✔️ Yes</td><td>Created date, Format should be 2020-01-01T12:00:00+00:00</td></tr><tr><td align="center">updatedDate</td><td align="center">✖️ No</td><td>Last updated date, Format should be 2020-01-01T12:00:00+00:00</td></tr><tr><td align="center">leadTimeMinutes</td><td align="center">✖️ No</td><td>How long from this issue accepted to develop.</td></tr><tr><td align="center">parentIssueKey</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">priority</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">originalEstimateMinutes</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">timeSpentMinutes</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">timeRemainingMinutes</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">creatorId</td><td align="center">✖️ No</td><td>The user id of the creator</td></tr><tr><td align="center">creatorName</td><td align="center">✖️ No</td><td>The username of the creator, it will just be used to display</td></tr><tr><td align="center">assigneeId</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">assigneeName</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">severity</td><td align="center">✖️ No</td><td></td></tr><tr><td align="center">component</td><td align="center">✖️ No</td><td></td></tr></tbody></table>

More information about these columns at the [domain layer issues table](#datamodels-devlakedomainlayerschema--issues).

<a id="plugins-webhook--register-issues-close-issues-optional"></a>

#### Register Issues - Close Issues (Optional)

`POST <devlake-host>/api/rest/plugins/webhook/1/issue/:issueId/close`

needs to be called when an issue or incident is closed. Replace `:issueId` with specific strings and keep the body empty.

<a id="plugins-webhook--register-issues-sample-api-calls"></a>

#### Register Issues - Sample API Calls

Sample CURL for creating an incident:

```text
curl <devlake-host>/api/rest/plugins/webhook/1/issues -X 'POST' -d '{
  "issueKey":"DLK-1234",
  "title":"a feature from DLK",
  "description":"",
  "url":"",
  "type":"INCIDENT",
  "status":"TODO",
  "createdDate":"2020-01-01T12:00:00+00:00",
  "updatedDate":"2020-01-01T12:00:00+00:00",
  "priority":"",
  "severity":"",
  "creatorId":"user1131",
  "creatorName":"Nick name 1",
  "assigneeId":"user1132",
  "assigneeName":"Nick name 2"
}'
```

Sample CURL for Issue Closing:

```text
curl <devlake-host>/api/rest/plugins/webhook/1/issue/DLK-1234/close -X 'POST'
```

<a id="plugins-webhook--references"></a>

## References

- [references](#developermanuals-developersetup--references)

- [Summary](#plugins-webhook--summary)
- [Entities](#plugins-webhook--entities)
- [Metrics](#plugins-webhook--metrics)
- [Configuration](#plugins-webhook--configuration)
- [API Sample Request](#plugins-webhook--api-sample-request)
  - [Deployment](#plugins-webhook--deployment)
  - [Incident / Issue](#plugins-webhook--incident-issue)
- [References](#plugins-webhook--references)

---

<a id="plugins-zentao"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Plugins/zentao/ -->

<!-- page_index: 115 -->

# Zentao

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Zentao

<a id="plugins-zentao--summary"></a>

## Summary

This plugin collects Zentao data through its REST APIs. [Zentao](https://github.com/easysoft/zentaopms) is an issue-tracking tool similar to Jira.

<a id="plugins-zentao--supported-versions"></a>

## Supported Versions

Advanced mode vailable for Zentao OSS v18.3, Enterprise v8.2, Flagship v4.3. Check [this doc](https://devlake.apache.org/docs/Overview/SupportedDataSources#data-sources-and-data-plugins) for more details.

<a id="plugins-zentao--metrics"></a>

## Metrics

Metrics that can be calculated based on the data collected from Zentao:

- [Requirement Count](#metrics-requirementcount)
- [Requirement Lead Time](#metrics-requirementleadtime)
- [Requirement Delivery Rate](#metrics-requirementdeliveryrate)
- [Bug Age](#metrics-bugage)
- [Incident Age](#metrics-incidentage)

<a id="plugins-zentao--configuration"></a>

## Configuration

- Configuring Zentao via [config-ui](#configuration-zentao).
- Configuring Zentao via Config UI's [advanced mode](#configuration-advancedmode--8-zentao).

- [Summary](#plugins-zentao--summary)
- [Supported Versions](#plugins-zentao--supported-versions)
- [Metrics](#plugins-zentao--metrics)
- [Configuration](#plugins-zentao--configuration)

---

<a id="troubleshooting"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Troubleshooting/ -->

<!-- page_index: 116 -->

# Troubleshooting

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Troubleshooting

[## 📄️ Installation Troubleshooting

Installation Troubleshooting](#troubleshooting-installation)

[## 📄️ Configuration and Blueprint Troubleshooting

Debug errors found in Config UI or during data collection.](#troubleshooting-configuration)

[## 📄️ Dashboard Troubleshooting

Dashboard Troubleshooting](#troubleshooting-dashboard)

[## 📄️ Mysql Troubleshooting

Mysql Troubleshooting](#troubleshooting-mysqlissue)

---

<a id="troubleshooting-installation"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Troubleshooting/Installation/ -->

<!-- page_index: 117 -->

# Installation Troubleshooting

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Installation Troubleshooting

<a id="troubleshooting-installation--panic-invalid-enckey-error"></a>

### `panic: invalid encKey` error

The cause is the `devlake` container trying to decrypt data in the database with the wrong key.
Please check the [GettingStarted/Upgrade](#gettingstarted-upgrade) doc for more detail.

<a id="troubleshooting-installation--go-panic-in-openshift-kubernetes"></a>

### Go Panic in OpenShift Kubernetes

One of the known root causes of the phonomenon is the Dynatrace agent being injected into the container.
Excluding the namespace from the Dynatrace deployments should fix the problem.
Check [#5612](https://github.com/apache/incubator-devlake/issues/5612) if you needed more detail.

<a id="troubleshooting-installation--none-of-them-solve-your-problem"></a>

## None of them solve your problem?

Sorry for the inconvenience, please help us improve by [creating an issue](https://github.com/apache/incubator-devlake/issues)

- [`panic: invalid encKey` error](#troubleshooting-installation--panic-invalid-enckey-error)
- [Go Panic in OpenShift Kubernetes](#troubleshooting-installation--go-panic-in-openshift-kubernetes)
- [None of them solve your problem?](#troubleshooting-installation--none-of-them-solve-your-problem)

---

<a id="troubleshooting-configuration"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Troubleshooting/Configuration/ -->

<!-- page_index: 118 -->

# Configuration and Blueprint Troubleshooting

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Configuration and Blueprint Troubleshooting

<a id="troubleshooting-configuration--common-error-code-while-collectingprocessing-data"></a>

### Common Error Code while collecting/processing data

<table><thead><tr><th>Error code</th><th>An example</th><th>Causes</th><th>Solutions</th></tr></thead><tbody><tr><td>429</td><td>subtask collectAPiPipelines ended unexpectedly caused: Error waiting for async Collector execution caused by: retry exceeded 3 times calling projects/{projectId}/pipelines {429}</td><td>This error exmaple is caused by GitLab's Pipeline APIs. These APIs are implemented via Cloudflare, which is different from other GitLab entities.</td><td>Two ways:
 - Enable <code>fixed rate limit</code> in the GitLab connection, lower the API rates to 2,000. If it works, you can try increase the rates to accerlerate. This solution also applies to other plugins that return the 429 while collecting data, such as GitHub, TAPD, etc.
 - Upgrade to v0.15.x</td></tr><tr><td>403</td><td>error: preparing task data for gitextractor caused by: unexpected http status code: 403</td><td>This is usually caused by the permission of your tokens. For example, if you're using an un-supported auth method, or using a token without ticking permissions to certain entities you want to collect.</td><td>Find the supported authentication methods and token permissions that should be selected in the corresponding plugin's Config UI manuals, for example, <a href="https://devlake.apache.org/docs/Configuration/GitHub#auth-tokens">configuring GitHub</a></td></tr><tr><td>1406</td><td>subtask extractApiBuilds ended unexpectedly caused by: error adding the result to batch caused by: Error 1406: Data too long for column 'full_display_name' at row 138. See bug <a href="https://github.com/apache/incubator-devlake/issues/4053" rel="noopener noreferrer" target="_blank">#4053</a></td><td>This is usually thrown by MySQL because a certain value is too long</td><td>A work-around is to manually change the field length to varchar(255) or longer in MySQL. Also, please put up a <a href="https://github.com/apache/incubator-devlake/issues/new?assignees=&amp;labels=type%2Fbug&amp;template=bug-report.yml&amp;title=%5BBug%5D%5BModule+Name%5D+Bug+title+" rel="noopener noreferrer" target="_blank">bug</a> to let us know.</td></tr></tbody></table>
<a id="troubleshooting-configuration--failed-to-collect-data-from-the-server-with-a-self-signed-certificate"></a>

### Failed to collect data from the server with a self-signed certificate

There might be two problems when trying to collect data from a private GitLab server with a self-signed certificate:

1. "Test Connection" error. This can be solved by setting the environment variable `IN_SECURE_SKIP_VERIFY=true` for the `devlake` container
2. "GitExtractor" fails to clone the repository due to certificate verification, sadly, neither gogit nor git2go we are using supports insecure HTTPS.

A better approach would be adding your root CA to the `devlake` container:

1. Mount your `rootCA.crt` into the `devlake` container
2. Add a `command` node to install the mounted certificate

Here is an example of the `docker-compose`` installation, the idea applies to other installation methods.

```text
  devlake:
    image: apache/devlake:v...
    ...
    volumes:
      ...
      - /path/to/your/rootCA.crt:/usr/local/share/ca-certificates/rootCA.crt
    command: [ "sh", "-c", "update-ca-certificates; lake" ]
    ...
```

<a id="troubleshooting-configuration--gitextractor-task-failed-in-a-githubgitlabbitbucket-blueprint"></a>

### GitExtractor task failed in a GitHub/GitLab/BitBucket blueprint

See bug [#3719](https://github.com/apache/incubator-devlake/issues/3719)

This bug happens occasionally in v0.14.x and previous versions. It is fixed by changing the docker base image. Please upgrade to v0.15.x to get it fixed if you encounter it.

<a id="troubleshooting-configuration--pipeline-failed-with-the-total-number-of-locks-exceeds-the-lock-table-size"></a>

### Pipeline failed with "The total number of locks exceeds the lock table size"

We have had a couple of reports suggesting MySQL InnoDB would fail with the message.

- [Error 1206: The total number of locks exceeds the lock table size · Issue #3849 · apache/incubator-devlake](https://github.com/apache/incubator-devlake/issues/3849)
- [[Bug][GitLab] gitlab collectApiJobs task failed for mysql locks error · Issue #3653 · apache/incubator-devlake](https://github.com/apache/incubator-devlake/issues/3653)

The cause of the problem is:

- Before Apache DevLake data collection starts, it must purge expired data in the database.
- MySQL InnoDB Engine would create locks in memory for the records being deleted.
- When deleting huge amounts of records, the memory bursts, hence the error.

You are likely to see the error when dealing with a huge repository or board. For MySQL, you can solve it by increasing the `innodb_buffer_pool_size` to a higher value.

Here is an example of the `docker-compose` installation, the idea applies to other installation methods.

```text
  mysql:
    image: mysql:8.....
    ...
    # add the follow line to the mysql container
    command: --innodb-buffer-pool-size=200M
```

<a id="troubleshooting-configuration--github-repositories-keep-loading-when-adding-data-scopes"></a>

### GitHub repositories keep loading when adding data scopes

See issue [#6038](https://github.com/apache/incubator-devlake/issues/6038)

If you're having trouble adding data scopes to a GitHub connection because the repositories keep loading, there are a few things you can check:

1. Make sure your access token has the necessary permissions.
2. If your account is protected by organization SAML enforcement, make sure you've authorized the token using SSO.

For more details about authenticating with SAML single sign-on, see here: <https://docs.github.com/en/enterprise-cloud@latest/authentication/authenticating-with-saml-single-sign-on>.

<a id="troubleshooting-configuration--none-of-them-solve-your-problem"></a>

## None of them solve your problem?

Sorry for the inconvenience, please help us improve by [creating an issue](https://github.com/apache/incubator-devlake/issues)

- [Common Error Code while collecting/processing data](#troubleshooting-configuration--common-error-code-while-collectingprocessing-data)
- [Failed to collect data from the server with a self-signed certificate](#troubleshooting-configuration--failed-to-collect-data-from-the-server-with-a-self-signed-certificate)
- [GitExtractor task failed in a GitHub/GitLab/BitBucket blueprint](#troubleshooting-configuration--gitextractor-task-failed-in-a-githubgitlabbitbucket-blueprint)
- [Pipeline failed with "The total number of locks exceeds the lock table size"](#troubleshooting-configuration--pipeline-failed-with-the-total-number-of-locks-exceeds-the-lock-table-size)
- [GitHub repositories keep loading when adding data scopes](#troubleshooting-configuration--github-repositories-keep-loading-when-adding-data-scopes)
- [None of them solve your problem?](#troubleshooting-configuration--none-of-them-solve-your-problem)

---

<a id="troubleshooting-dashboard"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Troubleshooting/Dashboard/ -->

<!-- page_index: 119 -->

# Dashboard Troubleshooting

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Dashboard Troubleshooting

<a id="troubleshooting-dashboard--debugging-dora-issue-metrics"></a>

## Debugging DORA Issue Metrics

This section may help if `Median Time to Restore Service (MTTR)` or `Change Failure Rate (CFR)` do not appear on the dashboards or you want to learn more about how these issue-based metrics are built.

<a id="troubleshooting-dashboard--dora-validation-dashboard"></a>

### DORA Validation Dashboard

Starting from DevLake v0.18 this dashboard can be found near the `DORA` dashboard. Also, it can be accessed by a direct link in the `Dashboard Instruction` panel in the `DORA` dashboard.

This dashboard is a step-by-step guide to check which step went wrong **for all 4 of the DORA metrics**. The sections are:

- Check "Deployment Frequency"
- Check "Median Lead Time for Changes"
- Check "Change Failure Rate" & "Median Time to Restore Service

<a id="troubleshooting-dashboard--sql-scripts-behind-grafana-charts"></a>

### SQL scripts behind Grafana charts

Each chart has a hidden button in the top-right corner to access the context menu. In that menu, click `Edit` to open a more detailed view with the script that tells how exactly the data is queried.

<a id="troubleshooting-dashboard--how-issues-and-deployments-are-associated-to-projects"></a>

### How issues and deployments are associated to projects

Following Entity-Relationship diagrams below represent how the data is mapped and used for each of the 4 DORA metrics.
They are based on the SQL queries for each of the charts.

Legend:

- Blue box: user data source, be it **deployments**, **pull requests** from the source code, or **issues**
- White box: a table or entity used by DevLake
- Connections: lines that tell how the tables are mapped, also specify which fields are used.

The `project_mapping` is responsible for mapping **deployments**, **pull requests** from the source code, or **issues**.
To do so, it must be filtered using either `table = 'cicd_scopes'`, `table = 'repos'`, or `table = 'boards'` when connecting to another table.

![](assets/images/cfr-a828bb154b8b9139a758126b670a783a_0ec52bb5e2ac88a7.png)

![](assets/images/deployments-2dbcee174e7ba1eab645923b9c632809_391abb5f4ad3a3ec.png)

![](assets/images/lead-time-f7fb898d559f96e0d2d0eedd9db3a910_840977073a3f7da8.png)

![](assets/images/mttr-9aa08ffbf6f14ca2264ecde8ed2284d4_649beffe8dc8d7f6.png)

<a id="troubleshooting-dashboard--if-you-use-webhooks"></a>

### If you use webhooks

DevLake knows to which project an issue or a deployment belongs only by segregation between the webhooks.
I.e. **each project should have its own webhook**. A webhook used by multiple projects means that all the
issues or deployments published by that webhook **will be replicated among those projects**, as they belong to both of them.

WIP

<a id="troubleshooting-dashboard--none-of-them-solve-your-problem"></a>

## None of them solve your problem?

Sorry for the inconvenience, please help us improve by [creating an issue](https://github.com/apache/incubator-devlake/issues)

- [Debugging DORA Issue Metrics](#troubleshooting-dashboard--debugging-dora-issue-metrics)
  - [DORA Validation Dashboard](#troubleshooting-dashboard--dora-validation-dashboard)
  - [SQL scripts behind Grafana charts](#troubleshooting-dashboard--sql-scripts-behind-grafana-charts)
  - [How issues and deployments are associated to projects](#troubleshooting-dashboard--how-issues-and-deployments-are-associated-to-projects)
  - [If you use webhooks](#troubleshooting-dashboard--if-you-use-webhooks)
- [None of them solve your problem?](#troubleshooting-dashboard--none-of-them-solve-your-problem)

---

<a id="troubleshooting-mysqlissue"></a>

<!-- source_url: https://devlake.apache.org/docs/v1.0/Troubleshooting/MySqlIssue/ -->

<!-- page_index: 120 -->

# Mysql Troubleshooting

> [!WARNING]
> **For up\-to\-date documentation, see the latest version \( Next \)\.**
> This is documentation for Apache DevLake - Open-Source Dev Data Platform for Productivity **v1.0**, which is no longer actively maintained.

Version: v1.0

# Mysql Troubleshooting

<a id="troubleshooting-mysqlissue--how-to-manage-the-quickly-increasing-mysql-disk-consumption"></a>

## How to manage the quickly increasing MySQL disk consumption?

DevLake is designed to collect data by first deleting the existing data and
then inserting new data. While this approach ensures that the latest data is
always available, it leads to a rapid increase in MySQL disk consumption.
This growth is primarily caused by the large size of the binary logs generated
after each data collection cycle.

<a id="troubleshooting-mysqlissue--why-does-devlake-choose-to-delete-the-existing-data-and-then-insert-new-data"></a>

### Why does DevLake choose to delete the existing data and then insert new data?

Because we want to ensure that the latest data is
always available. If we don't delete the existing data, some old data which has been deleted
from the previous step will still be available in the DevLake database.

<a id="troubleshooting-mysqlissue--how-to-purge-old-binary-logs"></a>

### How to purge old binary logs?

1. Connect to your MySQL server using the MySQL client or any other database management tool such as PhpMyAdmin, MySQL Workbench, etc.
2. Run the following command to check the current status of your binary log files:

```sql
SHOW BINARY LOGS;
```

This will display a list of all the binary log files that are currently available on your MySQL server.

3. Determine the last binary log file that you want to keep. This is the file that you want to retain for any future point-in-time recovery or replication purposes.
4. Run the following command to purge all binary logs that are older than the binary log file that you want to retain:

```sql
PURGE BINARY LOGS BEFORE 'DATE' ;
```

You need to provide the specific date and time up to which you want to purge the binary logs. The date and time should be formatted as a string in the 'YYYY-MM-DD hh:mm:ss' format.
For example, if you want to purge all binary logs before March 22, 2023, 15:30:00, you would replace DATE with '2023-03-22 15:30:00', like this:

```sql
PURGE BINARY LOGS BEFORE '2023-03-22 15:30:00' ;
```

5. After running the command, MySQL will delete all binary log files that are older than the specified file. You can verify that the purge was successful by running the SHOW BINARY LOGS; command again.

Note: Keep in mind that deleting old binary log files can affect point-in-time recovery and replication capabilities, so it's important to only delete files that are no longer needed.

Additionally, it's recommended to take a backup before deleting any binary log files in case you need to restore to a point before the binary logs were purged.

<a id="troubleshooting-mysqlissue--how-to-automate-the-purge-of-old-binary-logs"></a>

### How to "automate" the purge of old binary logs?

1. Connect to your MySQL server using the MySQL client or any other database management tool such as PhpMyAdmin, MySQL Workbench, etc.
2. Run the following command to set the expire\_logs\_days global variable to the number of days that you want to keep binary logs for:

```sql
SET GLOBAL expire_logs_days = 1;
```

<a id="troubleshooting-mysqlissue--how-to-skip-bin-logs"></a>

### How to skip bin logs?

1. To skip bin logs, you can set the skip-log-bin configuration option directly in the docker-compose.yaml file using the command option. Here's an example of how to do this:

```yaml
services:
  mysql:
    image: mysql:8
    volumes:
      - mysql-storage:/var/lib/mysql
    restart: always
    ports:
      - "127.0.0.1:3306:3306"
    environment:
      MYSQL_ROOT_PASSWORD: admin
      MYSQL_DATABASE: lake
      MYSQL_USER: merico
      MYSQL_PASSWORD: merico
    command:
      --character-set-server=utf8mb4
      --collation-server=utf8mb4_bin
      --skip-log-bin
```

2. After making the changes, you can restart the MySQL container using the following command:

```bash
  docker-compose restart mysql
```

<a id="troubleshooting-mysqlissue--how-to-connect-mysql-server-which-requires-ssl"></a>

### How to connect mysql server which requires SSL?

1. Skip-verifying the SSL certificate: you can add &tls=skip-verify to DB\_URL variable, for example:


```text
DB_URL=mysql://merico:merico@localhost:3306/lake?charset=utf8mb4&parseTime=True&loc=UTC&tls=skip-verify
```

2. Verify the SSL certificate: you can add &tls=custom&ca-cert=/path/to/your/ca-certificate.crt to DB\_URL variable, for example:


```text
DB_URL=mysql://merico:merico@lake.mysql.database.azure.com:3306/lake?charset=utf8mb4&parseTime=True&tls=custom&ca-cert=/path/to/your/DigiCertGlobalRootCA.crt.pem
```

   Note: in Python plugins, it will fallback to the `skip-verify` policy.

<a id="troubleshooting-mysqlissue--how-to-skip-subtask-collectgitcommits-ended-unexpectedly-deadlock-found-when-trying-to-get-lock"></a>

### How to skip "subtask collectGitCommits ended unexpectedly, deadlock found when trying to get lock"?

When users have large repositories with a substantial number of commit files to collect, it can lead to the following issues:

```text
1. The time to collect Git data is too long
2. Errors occurred while writing data to the DevLake database
```

To address this, you can bypass this step by setting the SKIP\_COMMIT\_FILES=true in the .env file.

- [How to manage the quickly increasing MySQL disk consumption?](#troubleshooting-mysqlissue--how-to-manage-the-quickly-increasing-mysql-disk-consumption)
  - [Why does DevLake choose to delete the existing data and then insert new data?](#troubleshooting-mysqlissue--why-does-devlake-choose-to-delete-the-existing-data-and-then-insert-new-data)
  - [How to purge old binary logs?](#troubleshooting-mysqlissue--how-to-purge-old-binary-logs)
  - [How to "automate" the purge of old binary logs?](#troubleshooting-mysqlissue--how-to-automate-the-purge-of-old-binary-logs)
  - [How to skip bin logs?](#troubleshooting-mysqlissue--how-to-skip-bin-logs)
  - [How to connect mysql server which requires SSL?](#troubleshooting-mysqlissue--how-to-connect-mysql-server-which-requires-ssl)
  - [How to skip "subtask collectGitCommits ended unexpectedly, deadlock found when trying to get lock"?](#troubleshooting-mysqlissue--how-to-skip-subtask-collectgitcommits-ended-unexpectedly-deadlock-found-when-trying-to-get-lock)

---
