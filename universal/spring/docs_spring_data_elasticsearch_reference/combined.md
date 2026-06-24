# Spring Data Elasticsearch

## Navigation

- Overview
  
- [Overview](#index)
    
- [Upgrading Spring Data](#commons-upgrade)
    
- [Migration Guides](#migration-guides)
      
- [Upgrading from 3.2.x to 4.0.x](#migration-guides-migration-guide-3.2-4.0)
      
- [Upgrading from 4.0.x to 4.1.x](#migration-guides-migration-guide-4.0-4.1)
      
- [Upgrading from 4.1.x to 4.2.x](#migration-guides-migration-guide-4.1-4.2)
      
- [Upgrading from 4.2.x to 4.3.x](#migration-guides-migration-guide-4.2-4.3)
      
- [Upgrading from 4.3.x to 4.4.x](#migration-guides-migration-guide-4.3-4.4)
      
- [Upgrading from 4.4.x to 5.0.x](#migration-guides-migration-guide-4.4-5.0)
      
- [Upgrading from 5.0.x to 5.1.x](#migration-guides-migration-guide-5.0-5.1)
      
- [Upgrading from 5.1.x to 5.2.x](#migration-guides-migration-guide-5.1-5.2)
      
- [Upgrading from 5.2.x to 5.3.x](#migration-guides-migration-guide-5.2-5.3)
      
- [Upgrading from 5.3.x to 5.4.x](#migration-guides-migration-guide-5.3-5.4)
      
- [Upgrading from 5.4.x to 5.5.x](#migration-guides-migration-guide-5.4-5.5)
      
- [Upgrading from 5.5.x to 6.0.x](#migration-guides-migration-guide-5.5-6.0)
  
- [Elasticsearch Support](#elasticsearch)
    
- [Elasticsearch Clients](#elasticsearch-clients)
    
- [Elasticsearch Object Mapping](#elasticsearch-object-mapping)
    
- [Elasticsearch Operations](#elasticsearch-template)
    
- [Reactive Elasticsearch Operations](#elasticsearch-reactive-template)
    
- [Entity Callbacks](#elasticsearch-entity-callbacks)
    
- [Elasticsearch Auditing](#elasticsearch-auditing)
    
- [Join-Type implementation](#elasticsearch-join-types)
    
- [Routing values](#elasticsearch-routing)
    
- [Miscellaneous Elasticsearch Operation Support](#elasticsearch-misc)
    
- [Scripted and runtime fields](#elasticsearch-scripted-and-runtime-fields)
  
- [Repositories](#repositories)
    
- [Core concepts](#repositories-core-concepts)
    
- [Defining Repository Interfaces](#repositories-definition)
    
- [Elasticsearch Repositories](#elasticsearch-repositories-elasticsearch-repositories)
    
- [Reactive Elasticsearch Repositories](#elasticsearch-repositories-reactive-elasticsearch-repositories)
    
- [Creating Repository Instances](#repositories-create-instances)
    
- [Defining Query Methods](#repositories-query-methods-details)
    
- [Query methods](#elasticsearch-repositories-elasticsearch-repository-queries)
    
- [Projections](#repositories-projections)
    
- [Custom Repository Implementations](#repositories-custom-implementations)
    
- [Publishing Events from Aggregate Roots](#repositories-core-domain-events)
    
- [Null Handling of Repository Methods](#repositories-null-handling)
    
- [CDI Integration](#elasticsearch-repositories-cdi-integration)
    
- [Repository query keywords](#repositories-query-keywords-reference)
    
- [Repository query return types](#repositories-query-return-types-reference)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/index.html -->

<!-- page_index: 1 -->

# Spring Data Elasticsearch

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="index--page-title"></a>
<a id="index--spring-data-elasticsearch"></a>

# Spring Data Elasticsearch

*Spring Data Elasticsearch provides repository support for the Elasticsearch database.
It eases development of applications with a consistent programming model that need to access Elasticsearch data sources.*

<table>
<tr>
<td>
<a href="https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/versions.html">Versions</a>
</td>
<td>
<p>Version Compatibility Matrix</p>
</td>
</tr>
<tr>
<td>
<a href="#elasticsearch-clients">Clients</a>
</td>
<td>
<p>Elasticsearch Client Configuration</p>
</td>
</tr>
<tr>
<td>
<a href="#elasticsearch">Elasticsearch</a>
</td>
<td>
<p>Elasticsearch support</p>
</td>
</tr>
<tr>
<td>
<a href="#repositories">Repositories</a>
</td>
<td>
<p>Elasticsearch Repositories</p>
</td>
</tr>
<tr>
<td>
<a href="#migration-guides">Migration</a>
</td>
<td>
<p>Migration Guides</p>
</td>
</tr>
<tr>
<td>
<a href="https://github.com/spring-projects/spring-data-commons/wiki">Wiki</a>
</td>
<td>
<p>What’s New, Upgrade Notes, Supported Versions, additional cross-version information.</p>
</td>
</tr>
</table>

BioMed Central Development Team; Oliver Drotbohm; Greg Turnquist; Christoph Strobl; Peter-Josef Meisch

© 2008-2026 VMware, Inc.

Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.

---

<a id="commons-upgrade"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/commons/upgrade.html -->

<!-- page_index: 2 -->

<a id="commons-upgrade--page-title"></a>
<a id="commons-upgrade--upgrading-spring-data"></a>

# Upgrading Spring Data

Instructions for how to upgrade from earlier versions of Spring Data are provided on the project [wiki](https://github.com/spring-projects/spring-data-commons/wiki).
Follow the links in the [release notes section](https://github.com/spring-projects/spring-data-commons/wiki#release-notes) to find the version that you want to upgrade to.

Upgrading instructions are always the first item in the release notes. If you are more than one release behind, please make sure that you also review the release notes of the versions that you jumped.

---

<a id="migration-guides"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides.html -->

<!-- page_index: 3 -->

# Migration Guides

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides--page-title"></a>
<a id="migration-guides--migration-guides"></a>

# Migration Guides

This section contains version-specific migration guides explaining how to upgrade across versions.

<a id="migration-guides--section-summary"></a>

## Section Summary

- [Upgrading from 3.2.x to 4.0.x](#migration-guides-migration-guide-3.2-4.0)
- [Upgrading from 4.0.x to 4.1.x](#migration-guides-migration-guide-4.0-4.1)
- [Upgrading from 4.1.x to 4.2.x](#migration-guides-migration-guide-4.1-4.2)
- [Upgrading from 4.2.x to 4.3.x](#migration-guides-migration-guide-4.2-4.3)
- [Upgrading from 4.3.x to 4.4.x](#migration-guides-migration-guide-4.3-4.4)
- [Upgrading from 4.4.x to 5.0.x](#migration-guides-migration-guide-4.4-5.0)
- [Upgrading from 5.0.x to 5.1.x](#migration-guides-migration-guide-5.0-5.1)
- [Upgrading from 5.1.x to 5.2.x](#migration-guides-migration-guide-5.1-5.2)
- [Upgrading from 5.2.x to 5.3.x](#migration-guides-migration-guide-5.2-5.3)
- [Upgrading from 5.3.x to 5.4.x](#migration-guides-migration-guide-5.3-5.4)
- [Upgrading from 5.4.x to 5.5.x](#migration-guides-migration-guide-5.4-5.5)
- [Upgrading from 5.5.x to 6.0.x](#migration-guides-migration-guide-5.5-6.0)

---

<a id="migration-guides-migration-guide-3.2-4.0"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-3.2-4.0.html -->

<!-- page_index: 4 -->

# Upgrading from 3.2.x to 4.0.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-3.2-4.0--page-title"></a>
<a id="migration-guides-migration-guide-3.2-4.0--upgrading-from-3.2.x-to-4.0.x"></a>

# Upgrading from 3.2.x to 4.0.x

This section describes breaking changes from version 3.2.x to 4.0.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-migration-guide-3.2-4.0.jackson-removal"></a>
<a id="migration-guides-migration-guide-3.2-4.0--removal-of-the-used-jackson-mapper"></a>

## Removal of the used Jackson Mapper

One of the changes in version 4.0.x is that Spring Data Elasticsearch does not use the Jackson Mapper anymore to map an entity to the JSON representation needed for Elasticsearch (see [Elasticsearch Object Mapping](#elasticsearch-object-mapping)).
In version 3.2.x the Jackson Mapper was the default that was used.
It was possible to switch to the meta-model based converter (named `ElasticsearchEntityMapper`) by explicitly configuring it ([Meta Model Object Mapping](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model)).

In version 4.0.x the meta-model based converter is the only one that is available and does not need to be configured explicitly.
If you had a custom configuration to enable the meta-model converter by providing a bean like this:

```java
@Bean @Override public EntityMapper entityMapper() {
ElasticsearchEntityMapper entityMapper = new ElasticsearchEntityMapper(elasticsearchMappingContext(), new DefaultConversionService() ); entityMapper.setConversions(elasticsearchCustomConversions());
return entityMapper;}
```

You now have to remove this bean, the `ElasticsearchEntityMapper` interface has been removed.

Entity configuration

Some users had custom Jackson annotations on the entity class, for example in order to define a custom name for the mapped document in Elasticsearch or to configure date conversions.
These are not taken into account anymore.
The needed functionality is now provided with Spring Data Elasticsearch’s `@Field` annotation.
Please see [Mapping Annotation Overview](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations) for detailed information.

<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-migration-guide-3.2-4.0.implicit-index-name"></a>
<a id="migration-guides-migration-guide-3.2-4.0--removal-of-implicit-index-name-from-query-objects"></a>

## Removal of implicit index name from query objects

In 3.2.x the different query classes like `IndexQuery` or `SearchQuery` had properties that were taking the index name or index names that they were operating upon.If these were not set, the passed in entity was inspected to retrieve the index name that was set in the `@Document` annotation.
In 4.0.x the index name(s) must now be provided in an additional parameter of type `IndexCoordinates`.By separating this, it now is possible to use one query object against different indices.

So for example the following code:

```java
IndexQuery indexQuery = new IndexQueryBuilder()
  .withId(person.getId().toString())
  .withObject(person)
  .build();

String documentId = elasticsearchOperations.index(indexQuery);
```

must be changed to:

```java
IndexCoordinates indexCoordinates = elasticsearchOperations.getIndexCoordinatesFor(person.getClass());

IndexQuery indexQuery = new IndexQueryBuilder()
  .withId(person.getId().toString())
  .withObject(person)
  .build();

String documentId = elasticsearchOperations.index(indexQuery, indexCoordinates);
```

To make it easier to work with entities and use the index name that is contained in the entitie’s `@Document` annotation, new methods have been added like `DocumentOperations.save(T entity)`;

<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-migration-guide-3.2-4.0.new-operations"></a>
<a id="migration-guides-migration-guide-3.2-4.0--the-new-operations-interfaces"></a>

## The new Operations interfaces

In version 3.2 there was the `ElasticsearchOperations` interface that defined all the methods for the `ElasticsearchTemplate` class. In version 4 the functions have been split into different interfaces, aligning these interfaces with the Elasticsearch API:

- `DocumentOperations` are the functions related documents like saving, or deleting
- `SearchOperations` contains the functions to search in Elasticsearch
- `IndexOperations` define the functions to operate on indexes, like index creation or mappings creation.

`ElasticsearchOperations` now extends `DocumentOperations` and `SearchOperations` and has methods get access to an `IndexOperations` instance.

> [!NOTE]
> All the functions from the `ElasticsearchOperations` interface in version 3.2 that are now moved to the `IndexOperations` interface are still available, they are marked as deprecated and have default implementations that delegate to the new implementation:

```java
/** * Create an index for given indexName.* * @param indexName the name of the index * @return {@literal true} if the index was created * @deprecated since 4.0, use {@link IndexOperations#create()} */ @Deprecated default boolean createIndex(String indexName) {return indexOps(IndexCoordinates.of(indexName)).create();}
```

<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-migration-guide-3.2-4.0.deprecations"></a>
<a id="migration-guides-migration-guide-3.2-4.0--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-migration-guide-3.2-4.0.deprecations.methods-classes"></a>
<a id="migration-guides-migration-guide-3.2-4.0--methods-and-classes"></a>

### Methods and classes

Many functions and classes have been deprecated. These functions still work, but the Javadocs show with what they should be replaced.

Example from ElasticsearchOperations

```java
/* * Retrieves an object from an index.* * @param query the query defining the id of the object to get * @param clazz the type of the object to be returned * @return the found object * @deprecated since 4.0, use {@link #get(String, Class, IndexCoordinates)} */ @Deprecated @Nullable <T> T queryForObject(GetQuery query, Class<T> clazz);
```

<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-migration-guide-3.2-4.0.deprecations.elasticsearch"></a>
<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-deprecations"></a>

### Elasticsearch deprecations

Since version 7 the Elasticsearch `TransportClient` is deprecated, it will be removed with Elasticsearch version 8. Spring Data Elasticsearch deprecates the `ElasticsearchTemplate` class which uses the `TransportClient` in version 4.0.

Mapping types were removed from Elasticsearch 7, they still exist as deprecated values in the Spring Data `@Document` annotation and the `IndexCoordinates` class but they are not used anymore internally.

<a id="migration-guides-migration-guide-3.2-4.0--elasticsearch-migration-guide-3.2-4.0.removal"></a>
<a id="migration-guides-migration-guide-3.2-4.0--removals"></a>

## Removals

- As already described, the `ElasticsearchEntityMapper` interface has been removed.
- The `SearchQuery` interface has been merged into it’s base interface `Query`, so it’s occurrences can just be replaced with `Query`.
- The method `org.springframework.data.elasticsearch.core.ElasticsearchOperations.query(SearchQuery query, ResultsExtractor<T> resultsExtractor);` and the `org.springframework.data.elasticsearch.core.ResultsExtractor` interface have been removed.
  These could be used to parse the result from Elasticsearch for cases in which the response mapping done with the Jackson based mapper was not enough.
  Since version 4.0, there are the new [Search Result Types](#elasticsearch-template--elasticsearch.operations.searchresulttypes) to return the information from an Elasticsearch response, so there is no need to expose this low level functionality.
- The low level methods `startScroll`, `continueScroll` and `clearScroll` have been removed from the `ElasticsearchOperations` interface.
  For low level scroll API access, there now are `searchScrollStart`, `searchScrollContinue` and `searchScrollClear` methods on the `ElasticsearchRestTemplate` class.

---

<a id="migration-guides-migration-guide-4.0-4.1"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-4.0-4.1.html -->

<!-- page_index: 5 -->

# Upgrading from 4.0.x to 4.1.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-4.0-4.1--page-title"></a>
<a id="migration-guides-migration-guide-4.0-4.1--upgrading-from-4.0.x-to-4.1.x"></a>

# Upgrading from 4.0.x to 4.1.x

This section describes breaking changes from version 4.0.x to 4.1.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-4.0-4.1--elasticsearch-migration-guide-4.0-4.1.deprecations"></a>
<a id="migration-guides-migration-guide-4.0-4.1--deprecations"></a>

## Deprecations

Definition of the id property

It is possible to define a property of en entity as the id property by naming it either `id` or `document`.
This behaviour is now deprecated and will produce a warning.
Please use the `@Id` annotation to mark a property as being the id property.

Index mappings

In the `ReactiveElasticsearchClient.Indices` interface the `updateMapping` methods are deprecated in favour of the `putMapping` methods.
They do the same, but `putMapping` is consistent with the naming in the Elasticsearch API:

Alias handling

In the `IndexOperations` interface the methods `addAlias(AliasQuery)`, `removeAlias(AliasQuery)` and `queryForAlias()` have been deprecated.
The new methods `alias(AliasAction)`, `getAliases(String…)` and `getAliasesForIndex(String…)` offer more functionality and a cleaner API.

Parent-ID

Usage of a parent-id has been removed from Elasticsearch since version 6. We now deprecate the corresponding fields and methods.

<a id="migration-guides-migration-guide-4.0-4.1--elasticsearch-migration-guide-4.0-4.1.removal"></a>
<a id="migration-guides-migration-guide-4.0-4.1--removals"></a>

## Removals

Type mappings

The *type mappings* parameters of the `@Document` annotation and the `IndexCoordinates` object were removed.
They had been deprecated in Spring Data Elasticsearch 4.0 and their values weren’t used anymore.

<a id="migration-guides-migration-guide-4.0-4.1--elasticsearch-migration-guide-4.0-4.1.breaking-changes"></a>
<a id="migration-guides-migration-guide-4.0-4.1--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-4.0-4.1--elasticsearch-migration-guide-4.0-4.1.breaking-changes.returntypes-1"></a>
<a id="migration-guides-migration-guide-4.0-4.1--return-types-of-reactiveelasticsearchclient.indices-methods"></a>

### Return types of ReactiveElasticsearchClient.Indices methods

The methods in the `ReactiveElasticsearchClient.Indices` were not used up to now.
With the introduction of the `ReactiveIndexOperations` it became necessary to change some of the return types:

- the `createIndex` variants now return a `Mono<Boolean>` instead of a `Mono<Void>` to signal successful index creation.
- the `updateMapping` variants now return a `Mono<Boolean>` instead of a `Mono<Void>` to signal successful mappings storage.

<a id="migration-guides-migration-guide-4.0-4.1--elasticsearch-migration-guide-4.0-4.1.breaking-changes.returntypes-2"></a>
<a id="migration-guides-migration-guide-4.0-4.1--return-types-of-documentoperations.bulkindex-methods"></a>

### Return types of DocumentOperations.bulkIndex methods

These methods were returning a `List<String>` containing the ids of the new indexed records.
Now they return a `List<IndexedObjectInformation>`; these objects contain the id and information about optimistic locking (seq\_no and primary\_term)

---

<a id="migration-guides-migration-guide-4.1-4.2"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-4.1-4.2.html -->

<!-- page_index: 6 -->

# Upgrading from 4.1.x to 4.2.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-4.1-4.2--page-title"></a>
<a id="migration-guides-migration-guide-4.1-4.2--upgrading-from-4.1.x-to-4.2.x"></a>

# Upgrading from 4.1.x to 4.2.x

This section describes breaking changes from version 4.1.x to 4.2.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.deprecations"></a>
<a id="migration-guides-migration-guide-4.1-4.2--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.deprecations.document"></a>
<a id="migration-guides-migration-guide-4.1-4.2--document-parameters"></a>

### @Document parameters

The parameters of the `@Document` annotation that are relevant for the index settings (`useServerConfiguration`, `shards`. `replicas`, `refreshIntervall` and `indexStoretype`) have been moved to the `@Setting` annotation. Use in `@Document` is still possible but deprecated.

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.removal"></a>
<a id="migration-guides-migration-guide-4.1-4.2--removals"></a>

## Removals

The `@Score` annotation that was used to set the score return value in an entity was deprecated in version 4.0 and has been removed.
Score values are returned in the `SearchHit` instances that encapsulate the returned entities.

The `org.springframework.data.elasticsearch.ElasticsearchException` class has been removed.
The remaining usages have been replaced with `org.springframework.data.mapping.MappingException` and `org.springframework.dao.InvalidDataAccessApiUsageException`.

The deprecated `ScoredPage`, `ScrolledPage` `@AggregatedPage` and implementations has been removed.

The deprecated `GetQuery` and `DeleteQuery` have been removed.

The deprecated `find` methods from `ReactiveSearchOperations` and `ReactiveDocumentOperations` have been removed.

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes"></a>
<a id="migration-guides-migration-guide-4.1-4.2--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes.refresh-policy"></a>
<a id="migration-guides-migration-guide-4.1-4.2--refreshpolicy"></a>

### RefreshPolicy

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes.refresh-policy.enum"></a>
<a id="migration-guides-migration-guide-4.1-4.2--enum-package-changed"></a>

#### Enum package changed

It was possible in 4.1 to configure the refresh policy for the `ReactiveElasticsearchTemplate` by overriding the method `AbstractReactiveElasticsearchConfiguration.refreshPolicy()` in a custom configuration class.
The return value of this method was an instance of the class `org.elasticsearch.action.support.WriteRequest.RefreshPolicy`.

Now the configuration must return `org.springframework.data.elasticsearch.core.RefreshPolicy`.
This enum has the same values and triggers the same behaviour as before, so only the `import` statement has to be adjusted.

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes.refresh-policy.behaviour"></a>
<a id="migration-guides-migration-guide-4.1-4.2--refresh-behaviour"></a>

#### Refresh behaviour

`ElasticsearchOperations` and `ReactiveElasticsearchOperations` now explicitly use the `RefreshPolicy` set on the template for write requests if not null.
If the refresh policy is null, then nothing special is done, so the cluster defaults are used. `ElasticsearchOperations` was always using the cluster default before this version.

The provided implementations for `ElasticsearchRepository` and `ReactiveElasticsearchRepository` will do an explicit refresh when the refresh policy is null.
This is the same behaviour as in previous versions.
If a refresh policy is set, then it will be used by the repositories as well.

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes.refresh-policy.configuration"></a>
<a id="migration-guides-migration-guide-4.1-4.2--refresh-configuration"></a>

#### Refresh configuration

When configuring Spring Data Elasticsearch like described in [Elasticsearch Clients](#elasticsearch-clients) by using `ElasticsearchConfigurationSupport`, `AbstractElasticsearchConfiguration` or `AbstractReactiveElasticsearchConfiguration` the refresh policy will be initialized to `null`.
Previously the reactive code initialized this to `IMMEDIATE`, now reactive and non-reactive code show the same behaviour.

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes.method-return-types"></a>
<a id="migration-guides-migration-guide-4.1-4.2--method-return-types"></a>

### Method return types

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes.method-return-types.delete"></a>
<a id="migration-guides-migration-guide-4.1-4.2--delete-methods-that-take-a-query"></a>

#### delete methods that take a Query

The reactive methods previously returned a `Mono<Long>` with the number of deleted documents, the non reactive versions were void. They now return a `Mono<ByQueryResponse>` which contains much more detailed information about the deleted documents and errors that might have occurred.

<a id="migration-guides-migration-guide-4.1-4.2--elasticsearch-migration-guide-4.1-4.2.breaking-changes.method-return-types.multiget"></a>
<a id="migration-guides-migration-guide-4.1-4.2--multiget-methods"></a>

#### multiget methods

The implementations of *multiget* previousl only returned the found entities in a `List<T>` for non-reactive implementations and in a `Flux<T>` for reactive implementations. If the request contained ids that were not found, the information that these are missing was not available. The user needed to compare the returned ids to the requested ones to find
which ones were missing.

Now the `multiget` methods return a `MultiGetItem` for every requested id. This contains information about failures (like non existing indices) and the information if the item existed (then it is contained in the `MultiGetItem) or not.

---

<a id="migration-guides-migration-guide-4.2-4.3"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-4.2-4.3.html -->

<!-- page_index: 7 -->

# Upgrading from 4.2.x to 4.3.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-4.2-4.3--page-title"></a>
<a id="migration-guides-migration-guide-4.2-4.3--upgrading-from-4.2.x-to-4.3.x"></a>

# Upgrading from 4.2.x to 4.3.x

This section describes breaking changes from version 4.2.x to 4.3.x and how removed features can be replaced by new introduced features.

> [!NOTE]
> Elasticsearch is working on a new Client that will replace the `RestHighLevelClient` because the `RestHighLevelClient` uses code from Elasticsearch core libraries which are not Apache 2 licensed anymore.
> Spring Data Elasticsearch is preparing for this change as well.
> This means that internally the implementations for the `*Operations` interfaces need to change - which should be no problem if users program against the interfaces like `ElasticsearchOperations` or `ReactiveElasticsearchOperations`.
> If you are using the implementation classes like `ElasticsearchRestTemplate` directly, you will need to adapt to these changes.
>
> Spring Data Elasticsearch also removes or replaces the use of classes from the `org.elasticsearch` packages in it’s API classes and methods, only using them in the implementation where the access to Elasticsearch is implemented.
> For the user that means, that some enum classes that were used are replaced by enums that live in `org.springframework.data.elasticsearch` with the same values, these are internally mapped onto the Elasticsearch ones.
>
> Places where classes are used that cannot easily be replaced, this usage is marked as deprecated, we are working on replacements.
>
> Check the sections on [Deprecations](#migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.deprecations) and [Breaking Changes](#migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes) for further details.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.deprecations"></a>
<a id="migration-guides-migration-guide-4.2-4.3--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.deprecations.suggest"></a>
<a id="migration-guides-migration-guide-4.2-4.3--suggest-methods"></a>

### suggest methods

In `SearchOperations`, and so in `ElasticsearchOperations` as well, the `suggest` methods taking a `org.elasticsearch.search.suggest.SuggestBuilder` as argument and returning a `org.elasticsearch.action.search.SearchResponse` have been deprecated.
Use `SearchHits<T> search(Query query, Class<T> clazz)` instead, passing in a `NativeSearchQuery` which can contain a `SuggestBuilder` and read the suggest results from the returned `SearchHit<T>`.

In `ReactiveSearchOperations` the new `suggest` methods return a `Mono<org.springframework.data.elasticsearch.core.suggest.response.Suggest>` now.
Here as well the old methods are deprecated.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes"></a>
<a id="migration-guides-migration-guide-4.2-4.3--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes.1"></a>
<a id="migration-guides-migration-guide-4.2-4.3--removal-of-org.elasticsearch-classes-from-the-api."></a>

### Removal of `org.elasticsearch` classes from the API.

- In the `org.springframework.data.elasticsearch.annotations.CompletionContext` annotation the property `type()` has changed from `org.elasticsearch.search.suggest.completion.context.ContextMapping.Type` to `org.springframework.data.elasticsearch.annotations.CompletionContext.ContextMappingType`, the available enum values are the same.
- In the `org.springframework.data.elasticsearch.annotations.Document` annotation the `versionType()` property has changed to `org.springframework.data.elasticsearch.annotations.Document.VersionType`, the available enum values are the same.
- In the `org.springframework.data.elasticsearch.core.query.Query` interface the `searchType()` property has changed to `org.springframework.data.elasticsearch.core.query.Query.SearchType`, the available enum values are the same.
- In the `org.springframework.data.elasticsearch.core.query.Query` interface the return value of `timeout()` was changed to `java.time.Duration`.
- The `` SearchHits<T>`class does not contain the `org.elasticsearch.search.aggregations.Aggregations `` anymore.
  Instead it now contains an instance of the `org.springframework.data.elasticsearch.core.AggregationsContainer<T>` class where `T` is the concrete aggregations type from the underlying client that is used.
  Currently this will be a `org
  .springframework.data.elasticsearch.core.clients.elasticsearch7.ElasticsearchAggregations` object; later different implementations will be available.
  The same change has been done to the `ReactiveSearchOperations.aggregate()` functions, the now return a `Flux<AggregationContainer<?>>`.
  Programs using the aggregations need to be changed to cast the returned value to the appropriate class to further proces it.
- methods that might have thrown a `org.elasticsearch.ElasticsearchStatusException` now will throw `org.springframework.data.elasticsearch.RestStatusException` instead.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes.2"></a>
<a id="migration-guides-migration-guide-4.2-4.3--handling-of-field-and-sourcefilter-properties-of-query"></a>

### Handling of field and sourceFilter properties of Query

Up to version 4.2 the `fields` property of a `Query` was interpreted and added to the include list of the `sourceFilter`.
This was not correct, as these are different things for Elasticsearch.
This has been corrected.
As a consequence code might not work anymore that relies on using `fields` to specify which fields should be returned from the document’s `` _source' and should be changed to use the `sourceFilter ``.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes.3"></a>
<a id="migration-guides-migration-guide-4.2-4.3--search_type-default-value"></a>

### search\_type default value

The default value for the `search_type` in Elasticsearch is `query_then_fetch`.
This now is also set as default value in the `Query` implementations, it was previously set to `dfs_query_then_fetch`.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes.4"></a>
<a id="migration-guides-migration-guide-4.2-4.3--bulkoptions-changes"></a>

### BulkOptions changes

Some properties of the `org.springframework.data.elasticsearch.core.query.BulkOptions` class have changed their type:

- the type of the `timeout` property has been changed to `java.time.Duration`.
- the type of the`refreshPolicy` property has been changed to `org.springframework.data.elasticsearch.core.RefreshPolicy`.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes.5"></a>
<a id="migration-guides-migration-guide-4.2-4.3--indicesoptions-change"></a>

### IndicesOptions change

Spring Data Elasticsearch now uses `org.springframework.data.elasticsearch.core.query.IndicesOptions` instead of `org.elasticsearch.action.support.IndicesOptions`.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes.6"></a>
<a id="migration-guides-migration-guide-4.2-4.3--completion-classes"></a>

### Completion classes

The classes from the package `org.springframework.data.elasticsearch.core.completion` have been moved to `org.springframework.data.elasticsearch.core.suggest`.

<a id="migration-guides-migration-guide-4.2-4.3--elasticsearch-migration-guide-4.2-4.3.breaking-changes.7"></a>
<a id="migration-guides-migration-guide-4.2-4.3--other-renamings"></a>

### Other renamings

The `org.springframework.data.elasticsearch.core.mapping.ElasticsearchPersistentPropertyConverter` interface has been renamed to `org.springframework.data.elasticsearch.core.mapping.PropertyValueConverter`.
Likewise the implementations classes named *XXPersistentPropertyConverter* have been renamed to *XXPropertyValueConverter*.

---

<a id="migration-guides-migration-guide-4.3-4.4"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-4.3-4.4.html -->

<!-- page_index: 8 -->

# Upgrading from 4.3.x to 4.4.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-4.3-4.4--page-title"></a>
<a id="migration-guides-migration-guide-4.3-4.4--upgrading-from-4.3.x-to-4.4.x"></a>

# Upgrading from 4.3.x to 4.4.x

This section describes breaking changes from version 4.3.x to 4.4.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.deprecations"></a>
<a id="migration-guides-migration-guide-4.3-4.4--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.deprecations.reactive-operations"></a>
<a id="migration-guides-migration-guide-4.3-4.4--org.springframework.data.elasticsearch.core.reactiveelasticsearchoperations"></a>

### org.springframework.data.elasticsearch.core.ReactiveElasticsearchOperations

The method `<T> Publisher<T> execute(ClientCallback<Publisher<T>> callback)` has been deprecated.
As there now are multiple implementations using different client libraries the `execute` method is still available in the different implementations, but there is no more method in the interface, because there is no common callback interface for the different clients.

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.breaking-changes"></a>
<a id="migration-guides-migration-guide-4.3-4.4--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.breaking-changes.1"></a>
<a id="migration-guides-migration-guide-4.3-4.4--removal-of-deprecated-classes"></a>

### Removal of deprecated classes

<a id="migration-guides-migration-guide-4.3-4.4--org-springframework-data-elasticsearch-core-elasticsearchtemplate-has-been-removed"></a>
<a id="migration-guides-migration-guide-4.3-4.4--org.springframework.data.elasticsearch.core.elasticsearchtemplate-has-been-removed"></a>

#### `org.springframework.data.elasticsearch.core.ElasticsearchTemplate` has been removed

As of version 4.4 Spring Data Elasticsearch does not use the `TransportClient` from Elasticsearch anymore (which itself is deprecated since Elasticsearch 7.0).
This means that the `org.springframework.data.elasticsearch.core.ElasticsearchTemplate` class which was deprecated since Spring Data Elasticsearch 4.0 has been removed.
This was the implementation of the `ElasticsearchOperations` interface that was using the `TransportClient`.
Connections to Elasticsearch must be made using either the imperative `ElasticsearchRestTemplate` or the reactive `ReactiveElasticsearchTemplate`.

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.breaking-changes.2"></a>
<a id="migration-guides-migration-guide-4.3-4.4--package-changes"></a>

### Package changes

In 4.3 two classes (`ElasticsearchAggregations` and `ElasticsearchAggregation`) had been moved to the `org.springframework.data.elasticsearch.core.clients.elasticsearch7` package in preparation for the integration of the new Elasticsearch client.
The were moved back to the `org.springframework.data.elasticsearch.core` package as we keep the classes use the old Elasticsearch client where they were.

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.breaking-changes.3"></a>
<a id="migration-guides-migration-guide-4.3-4.4--behaviour-change"></a>

### Behaviour change

The `ReactiveElasticsearchTemplate`, when created directly or by Spring Boot configuration had a default refresh policy of IMMEDIATE.
This could cause performance issues on heavy indexing and was different than the default behaviour of Elasticsearch.
This has been changed to that now the default refresh policy is NONE.
When the
`ReactiveElasticsearchTemplate` was provided by using the configuration like described in [Reactive REST Client](#elasticsearch-clients--elasticsearch.clients.reactiverestclient) the default refresh policy already was set to NONE.

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.new-clients"></a>
<a id="migration-guides-migration-guide-4.3-4.4--new-elasticsearch-client"></a>

## New Elasticsearch client

Elasticsearch has introduced it’s new `ElasticsearchClient` and has deprecated the previous `RestHighLevelClient`.
Spring Data Elasticsearch 4.4 still uses the old client as the default client for the following reasons:

- The new client forces applications to use the `jakarta.json.spi.JsonProvider` package whereas Spring Boot will stick to `javax.json.spi.JsonProvider` until version 3. So switching the default implementaiton in Spring Data Elasticsearch can only come with Spring Data Elasticsearch 5 (Spring Data 3, Spring 6).
- There are still some bugs in the Elasticsearch client which need to be resolved
- The implementation using the new client in Spring Data Elasticsearch is not yet complete, due to limited resources working on that - remember Spring Data Elasticsearch is a community driven project that lives from public contributions.

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.new-clients.how-to"></a>
<a id="migration-guides-migration-guide-4.3-4.4--how-to-use-the-new-client"></a>

### How to use the new client

> [!WARNING]
> The implementation using the new client is not complete, some operations will throw a `java.lang.UnsupportedOperationException` or might throw NPE (for example when the Elasticsearch cannot parse a response from the server, this still happens sometimes)
> Use the new client to test the implementations but do not use it in productive code yet!

In order to try and use the new client the following steps are necessary:

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.new-clients.how-to.not"></a>
<a id="migration-guides-migration-guide-4.3-4.4--make-sure-not-to-configure-the-existing-default-client"></a>

#### Make sure not to configure the existing default client

If using Spring Boot, exclude Spring Data Elasticsearch from the autoconfiguration

```java
@SpringBootApplication(exclude = ElasticsearchDataAutoConfiguration.class)
public class SpringdataElasticTestApplication {
	// ...
}
```

Remove Spring Data Elasticsearch related properties from your application configuration.
If Spring Data Elasticsearch was configured using a programmatic configuration (see [Elasticsearch Clients](#elasticsearch-clients)), remove these beans from the Spring application context.

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.new-clients.how-to.dependencies"></a>
<a id="migration-guides-migration-guide-4.3-4.4--add-dependencies"></a>

#### Add dependencies

The dependencies for the new Elasticsearch client are still optional in Spring Data Elasticsearch so they need to be added explicitly:

```xml
<dependencies>
    <dependency>
        <groupId>co.elastic.clients</groupId>
        <artifactId>elasticsearch-java</artifactId>
        <version>7.17.3</version>
        <exclusions>
            <exclusion>
                <groupId>commons-logging</groupId>
                <artifactId>commons-logging</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
    <dependency>
        <groupId>org.elasticsearch.client</groupId>
        <artifactId>elasticsearch-rest-client</artifactId> <!-- is Apache 2-->
        <version>7.17.3</version>
        <exclusions>
            <exclusion>
                <groupId>commons-logging</groupId>
                <artifactId>commons-logging</artifactId>
            </exclusion>
        </exclusions>
    </dependency>
</dependencies>
```

When using Spring Boot, it is necessary to set the following property in the *pom.xml*.

```xml
<properties>
    <jakarta-json.version>2.0.1</jakarta-json.version>
</properties>
```

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.new-clients.how-to.configuration"></a>
<a id="migration-guides-migration-guide-4.3-4.4--new-configuration-classes"></a>

#### New configuration classes

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.new-clients.how-to.configuration.imperative"></a>
<a id="migration-guides-migration-guide-4.3-4.4--imperative-style"></a>

##### Imperative style

In order configure Spring Data Elasticsearch to use the new client, it is necessary to create a configuration bean that derives from `org.springframework.data.elasticsearch.client.elc.ElasticsearchConfiguration`:

```java
@Configuration public class NewRestClientConfig extends ElasticsearchConfiguration {
@Override public ClientConfiguration clientConfiguration() {return ClientConfiguration.builder() // .connectedTo("localhost:9200") // .build();}}
```

The configuration is done in the same way as with the old client, but it is not necessary anymore to create more than the configuration bean.
With this configuration, the following beans will be available in the Spring application context:

- a `RestClient` bean, that is the configured low level `RestClient` that is used by the Elasticsearch client
- an `ElasticsearchClient` bean, this is the new client that uses the `RestClient`
- an `ElasticsearchOperations` bean, available with the bean names *elasticsearchOperations* and *elasticsearchTemplate*, this uses the `ElasticsearchClient`

<a id="migration-guides-migration-guide-4.3-4.4--elasticsearch-migration-guide-4.3-4.4.new-clients.how-to.configuration.reactive"></a>
<a id="migration-guides-migration-guide-4.3-4.4--reactive-style"></a>

##### Reactive style

To use the new client in a reactive environment the only difference is the class from which to derive the configuration:

```java
@Configuration public class NewRestClientConfig extends ReactiveElasticsearchConfiguration {
@Override public ClientConfiguration clientConfiguration() {return ClientConfiguration.builder() // .connectedTo("localhost:9200") // .build();}}
```

With this configuration, the following beans will be available in the Spring application context:

- a `RestClient` bean, that is the configured low level `RestClient` that is used by the Elasticsearch client
- an `ReactiveElasticsearchClient` bean, this is the new reactive client that uses the `RestClient`
- an `ReactiveElasticsearchOperations` bean, available with the bean names *reactiveElasticsearchOperations* and *reactiveElasticsearchTemplate*, this uses the `ReactiveElasticsearchClient`

---

<a id="migration-guides-migration-guide-4.4-5.0"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-4.4-5.0.html -->

<!-- page_index: 9 -->

# Upgrading from 4.4.x to 5.0.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-4.4-5.0--page-title"></a>
<a id="migration-guides-migration-guide-4.4-5.0--upgrading-from-4.4.x-to-5.0.x"></a>

# Upgrading from 4.4.x to 5.0.x

This section describes breaking changes from version 4.4.x to 5.0.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-4.5.deprecations"></a>
<a id="migration-guides-migration-guide-4.4-5.0--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-4.4-5.0--custom-trace-level-logging"></a>

### Custom trace level logging

Logging by setting the property `logging.level.org.springframework.data.elasticsearch.client.WIRE=trace` is deprecated now, the Elasticsearch `RestClient` provides a better solution that can be activated by setting the logging level of the `tracer` package to "trace".

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-4.5.deprecations.package"></a>
<a id="migration-guides-migration-guide-4.4-5.0--org.springframework.data.elasticsearch.client.erhlc-package"></a>

### `org.springframework.data.elasticsearch.client.erhlc` package

See [Package changes](#migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.breaking-changes-packages), all classes in this package have been deprecated, as the default client implementations to use are the ones based on the new Java Client from Elasticsearch, see [New Elasticsearch client](#migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.new-clients)

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-4.5.deprecations.code"></a>
<a id="migration-guides-migration-guide-4.4-5.0--removal-of-deprecated-code"></a>

### Removal of deprecated code

`DateFormat.none` and `DateFormat.custom` had been deprecated since version 4.2 and have been removed.

The properties of `@Document` that were deprecated since 4.2 have been removed.
Use the `@Settings` annotation for these.

`@DynamicMapping` and `@DynamicMappingValue` have been removed.
Use `@Document.dynamic` or `@Field.dynamic` instead.

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.breaking-changes"></a>
<a id="migration-guides-migration-guide-4.4-5.0--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.breaking-changes.deprecated-calls"></a>
<a id="migration-guides-migration-guide-4.4-5.0--removal-of-deprecated-calls"></a>

### Removal of deprecated calls

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.breaking-changes.deprecated-calls.1"></a>
<a id="migration-guides-migration-guide-4.4-5.0--suggest-calls-in-operations-interfaces-have-been-removed"></a>

#### suggest calls in operations interfaces have been removed

Both `SearchOperations` and `ReactiveSearchOperations` had deprecated calls that were using Elasticsearch classes as parameters.
These now have been removed and so the dependency on Elasticsearch classes in these APIs has been cleaned.

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.breaking-changes-packages"></a>
<a id="migration-guides-migration-guide-4.4-5.0--package-changes"></a>

### Package changes

All the classes that are using or depend on the deprecated Elasticsearch `RestHighLevelClient` have been moved to the package `org.springframework.data.elasticsearch.client.erhlc`.
By this change we now have a clear separation of code using the old deprecated Elasticsearch libraries, code using the new Elasticsearch client and code that is independent of the client implementation.
Also the reactive implementation that was provided up to now has been moved here, as this implementation contains code that was copied and adapted from Elasticsearch libraries.

If you are using `ElasticsearchRestTemplate` directly and not the `ElasticsearchOperations` interface you’ll need to adjust your imports as well.

When working with the `NativeSearchQuery` class, you’ll need to switch to the `NativeQuery` class, which can take a
`Query` instance coming from the new Elasticsearch client libraries.
You’ll find plenty of examples in the test code.

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.breaking-changes-records"></a>
<a id="migration-guides-migration-guide-4.4-5.0--conversion-to-java-17-records"></a>

### Conversion to Java 17 records

The following classes have been converted to `Record`, you might need to adjust the use of getter methods from
`getProp()` to `prop()`:

- `org.springframework.data.elasticsearch.core.AbstractReactiveElasticsearchTemplate.IndexResponseMetaData`
- `org.springframework.data.elasticsearch.core.ActiveShardCount`
- `org.springframework.data.elasticsearch.support.Version`
- `org.springframework.data.elasticsearch.support.ScoreDoc`
- `org.springframework.data.elasticsearch.core.query.ScriptData`
- `org.springframework.data.elasticsearch.core.query.SeqNoPrimaryTerm`

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.breaking-changes-http-headers"></a>
<a id="migration-guides-migration-guide-4.4-5.0--new-httpheaders-class"></a>

### New HttpHeaders class

Until version 4.4 the client configuration used the `HttpHeaders` class from the `org.springframework:spring-web`
project.
This introduces a dependency on that artifact.
Users that do not use spring-web then face an error as this class cannot be found.

In version 5.0 we introduce our own `HttpHeaders` to configure the clients.

So if you are using headers in the client configuration, you need to replace `org.springframework.http.HttpHeaders`
with `org.springframework.data.elasticsearch.support.HttpHeaders`.

Hint: You can pass a `org.springframework.http
.HttpHeaders` to the `addAll()` method of `org.springframework.data.elasticsearch.support.HttpHeaders`.

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.new-clients"></a>
<a id="migration-guides-migration-guide-4.4-5.0--new-elasticsearch-client"></a>

## New Elasticsearch client

Spring Data Elasticsearch now uses the new `ElasticsearchClient` and has deprecated the use of the previous `RestHighLevelClient`.

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.new-clients.imperative"></a>
<a id="migration-guides-migration-guide-4.4-5.0--imperative-style-configuration"></a>

### Imperative style configuration

To configure Spring Data Elasticsearch to use the new client, it is necessary to create a configuration bean that derives from `org.springframework.data.elasticsearch.client.elc.ElasticsearchConfiguration`:

```java
@Configuration public class NewRestClientConfig extends ElasticsearchConfiguration {
@Override public ClientConfiguration clientConfiguration() {return ClientConfiguration.builder() // .connectedTo("localhost:9200") // .build();}}
```

The configuration is done in the same way as with the old client, but it is not necessary anymore to create more than the configuration bean.
With this configuration, the following beans will be available in the Spring application context:

- a `RestClient` bean, that is the configured low level `RestClient` that is used by the Elasticsearch client
- an `ElasticsearchClient` bean, this is the new client that uses the `RestClient`
- an `ElasticsearchOperations` bean, available with the bean names *elasticsearchOperations* and *elasticsearchTemplate*, this uses the `ElasticsearchClient`

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.new-clients.reactive"></a>
<a id="migration-guides-migration-guide-4.4-5.0--reactive-style-configuration"></a>

### Reactive style configuration

To use the new client in a reactive environment the only difference is the class from which to derive the configuration:

```java
@Configuration public class NewRestClientConfig extends ReactiveElasticsearchConfiguration {
@Override public ClientConfiguration clientConfiguration() {return ClientConfiguration.builder() // .connectedTo("localhost:9200") // .build();}}
```

With this configuration, the following beans will be available in the Spring application context:

- a `RestClient` bean, that is the configured low level `RestClient` that is used by the Elasticsearch client
- an `ReactiveElasticsearchClient` bean, this is the new reactive client that uses the `RestClient`
- an `ReactiveElasticsearchOperations` bean, available with the bean names *reactiveElasticsearchOperations* and *reactiveElasticsearchTemplate*, this uses the `ReactiveElasticsearchClient`

<a id="migration-guides-migration-guide-4.4-5.0--elasticsearch-migration-guide-4.4-5.0.old-client"></a>
<a id="migration-guides-migration-guide-4.4-5.0--still-want-to-use-the-old-client"></a>

### Still want to use the old client?

The old deprecated `RestHighLevelClient` can still be used, but you will need to add the dependency explicitly to your application as Spring Data Elasticsearch does not pull it in automatically anymore:

```xml
<!-- include the RHLC, specify version explicitly	-->
<dependency>
	<groupId>org.elasticsearch.client</groupId>
	<artifactId>elasticsearch-rest-high-level-client</artifactId>
	<version>7.17.5</version>
	<exclusions>
		<exclusion>
			<groupId>commons-logging</groupId>
			<artifactId>commons-logging</artifactId>
		</exclusion>
	</exclusions>
</dependency>
```

Make sure to specify the version 7.17.6 explicitly, otherwise maven will resolve to 8.5.0, and this does not exist.

---

<a id="migration-guides-migration-guide-5.0-5.1"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-5.0-5.1.html -->

<!-- page_index: 10 -->

# Upgrading from 5.0.x to 5.1.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-5.0-5.1--page-title"></a>
<a id="migration-guides-migration-guide-5.0-5.1--upgrading-from-5.0.x-to-5.1.x"></a>

# Upgrading from 5.0.x to 5.1.x

This section describes breaking changes from version 5.0.x to 5.1.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-5.0-5.1--elasticsearch-migration-guide-5.0-5.1.breaking-changes"></a>
<a id="migration-guides-migration-guide-5.0-5.1--breaking-changes"></a>

## Breaking Changes

In the `org.springframework.data.elasticsearch.core.index.AliasData` class, which is used for alias information returned from Elasticsearch, the property `filter` (of type `Document`) is replaced by `filterQuery` which is of type
`org.springframework.data.elasticsearch.core.query.Query`.

`org.springframework.data.elasticsearch.annotations.Similarity` was an enum class until 5.1. This enum was used in the `@Field` annotation to specify a similarity value.
But besides the values defined by the enum, it is possible to have similarities with custom names in Elasticsearch.
Therefore, the annotation property was changed from the type of the enum to a simple `String`.
The previous enum values like `Similarity.Default` do still exist as String constants, so existing code will compile unmodified.
Adaptions are necessary when this enum was used at other places than as a property of the `@Field` annotation.

<a id="migration-guides-migration-guide-5.0-5.1--elasticsearch-migration-guide-5.0-5.1.deprecations"></a>
<a id="migration-guides-migration-guide-5.0-5.1--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-5.0-5.1--template-functions"></a>

### template functions

The functions in the `IndexOperations` and `ReactiverIndexOperations` to manage index templates that were introduced in Spring Data Elasticsearch 4.1
have been deprecated. They were using the old Elasticsearch API that was deprecated in Elasticsearch version 7.8.

Please use the new functions that are based on the composable index template API instead.

---

<a id="migration-guides-migration-guide-5.1-5.2"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-5.1-5.2.html -->

<!-- page_index: 11 -->

# Upgrading from 5.1.x to 5.2.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-5.1-5.2--page-title"></a>
<a id="migration-guides-migration-guide-5.1-5.2--upgrading-from-5.1.x-to-5.2.x"></a>

# Upgrading from 5.1.x to 5.2.x

This section describes breaking changes from version 5.1.x to 5.2.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-5.1-5.2--elasticsearch-migration-guide-5.1-5.2.breaking-changes"></a>
<a id="migration-guides-migration-guide-5.1-5.2--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-5.1-5.2--bulk-failures"></a>

### Bulk failures

In the `org.springframework.data.elasticsearch.BulkFailureException` class, the return type of the `getFailedDocuments` is changed from `Map<String, String>`
to `Map<String, FailureDetails>`, which allows to get additional details about failure reasons.

The definition of the `FailureDetails` class (inner to `BulkFailureException`):

```java
public record FailureDetails(Integer status, String errorMessage) {
}
```

<a id="migration-guides-migration-guide-5.1-5.2--scripted-and-runtime-fields"></a>

### scripted and runtime fields

The classes `org.springframework.data.elasticsearch.core.RuntimeField` and `org.springframework.data.elasticsearch.core.query.ScriptType` have been moved to the subpackage `org.springframework.data.elasticsearch.core.query`.

The `type` parameter of the `ScriptData` constructor is not nullable any longer.

<a id="migration-guides-migration-guide-5.1-5.2--elasticsearch-migration-guide-5.1-5.2.deprecations"></a>
<a id="migration-guides-migration-guide-5.1-5.2--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-5.1-5.2--removal-of-deprecated-code"></a>

### Removal of deprecated code

- All the code using the old deprecated `RestHighLevelClient` has been removed.
  The default Elasticsearch client used since version 5.0 is the (not so) new Elasticsearch Java client.
- The `org.springframework.data.elasticsearch.client.ClientLogger` class has been removed.
  This logger was configured with the `org.springframework.data.elasticsearch.client.WIRE` setting, but was not working with all clients.
  From version 5 on, use the trace logger available in the Elasticsearch Java client, see [Client Logging](#elasticsearch-clients--elasticsearch.clients.logging).
- The method `org.springframework.data.elasticsearch.core.ElasticsearchOperations.stringIdRepresentation(Object)` has been removed, use the `convertId(Object)` method defined in the same interface instead.
- The class `org.springframework.data.elasticsearch.core.Range` has been removed, use `org.springframework.data.domain.Range` instead.
- The methods `` org.springframework.data.elasticsearch.core.query.IndexQuery.getParentId() and `setParentId(String) `` have been removed, they weren’t used anymore and were no-ops.
  It has been removed from the `org.springframework.data.elasticsearch.core.query.IndexQuery` class as well.

---

<a id="migration-guides-migration-guide-5.2-5.3"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-5.2-5.3.html -->

<!-- page_index: 12 -->

# Upgrading from 5.2.x to 5.3.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-5.2-5.3--page-title"></a>
<a id="migration-guides-migration-guide-5.2-5.3--upgrading-from-5.2.x-to-5.3.x"></a>

# Upgrading from 5.2.x to 5.3.x

This section describes breaking changes from version 5.2.x to 5.3.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-5.2-5.3--elasticsearch-migration-guide-5.2-5.3.breaking-changes"></a>
<a id="migration-guides-migration-guide-5.2-5.3--breaking-changes"></a>

## Breaking Changes

During the parameter replacement in `@Query` annotated repository methods previous versions wrote the String `"null"` into the query that was sent to Elasticsearch when the actual parameter value was `null`.
As Elasticsearch does not store `null` values, this behaviour could lead to problems, for example whent the fields to be searched contains the string `"null"`.
In Version 5.3 a `null` value in a parameter will cause a `ConversionException` to be thrown.
If you are using `"null"` as the
`null_value` defined in a field mapping, then pass that string into the query instead of a Java `null`.

<a id="migration-guides-migration-guide-5.2-5.3--elasticsearch-migration-guide-5.2-5.3.deprecations"></a>
<a id="migration-guides-migration-guide-5.2-5.3--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-5.2-5.3--_removals"></a>
<a id="migration-guides-migration-guide-5.2-5.3--removals"></a>

### Removals

The deprecated classes `org.springframework.data.elasticsearch.ELCQueries`
and `org.springframework.data.elasticsearch.client.elc.QueryBuilders` have been removed, use `org.springframework.data.elasticsearch.client.elc.Queries` instead.

---

<a id="migration-guides-migration-guide-5.3-5.4"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-5.3-5.4.html -->

<!-- page_index: 13 -->

# Upgrading from 5.3.x to 5.4.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-5.3-5.4--page-title"></a>
<a id="migration-guides-migration-guide-5.3-5.4--upgrading-from-5.3.x-to-5.4.x"></a>

# Upgrading from 5.3.x to 5.4.x

This section describes breaking changes from version 5.3.x to 5.4.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-5.3-5.4--elasticsearch-migration-guide-5.3-5.4.breaking-changes"></a>
<a id="migration-guides-migration-guide-5.3-5.4--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-5.3-5.4--elasticsearch-migration-guide-5.3-5.4.breaking-changes.knn-search"></a>
<a id="migration-guides-migration-guide-5.3-5.4--knn-search"></a>

### knn search

The `withKnnQuery` method in `NativeQueryBuilder` has been replaced with `withKnnSearches` to build a `NativeQuery` with knn search.

`KnnQuery` and `KnnSearch` are two different classes in elasticsearch java client and are used for different queries, with different parameters supported:

- `KnnSearch`: is [the top level `knn` query](https://www.elastic.co/guide/en/elasticsearch/reference/8.13/search-search.html#search-api-knn) in the elasticsearch request;
- `KnnQuery`: is [the `knn` query inside `query` clause](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-knn-query.html);

If `KnnQuery` is still preferable, please be sure to construct it inside `query` clause manually, by means of `withQuery(co.elastic.clients.elasticsearch._types.query_dsl.Query query)` clause in `NativeQueryBuilder`.

<a id="migration-guides-migration-guide-5.3-5.4--elasticsearch-migration-guide-5.3-5.4.deprecations"></a>
<a id="migration-guides-migration-guide-5.3-5.4--deprecations"></a>

## Deprecations

<a id="migration-guides-migration-guide-5.3-5.4--_removals"></a>
<a id="migration-guides-migration-guide-5.3-5.4--removals"></a>

### Removals

---

<a id="migration-guides-migration-guide-5.4-5.5"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-5.4-5.5.html -->

<!-- page_index: 14 -->

# Upgrading from 5.4.x to 5.5.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-5.4-5.5--page-title"></a>
<a id="migration-guides-migration-guide-5.4-5.5--upgrading-from-5.4.x-to-5.5.x"></a>

# Upgrading from 5.4.x to 5.5.x

This section describes breaking changes from version 5.4.x to 5.5.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-5.4-5.5--elasticsearch-migration-guide-5.4-5.5.breaking-changes"></a>
<a id="migration-guides-migration-guide-5.4-5.5--breaking-changes"></a>

## Breaking Changes

<a id="migration-guides-migration-guide-5.4-5.5--elasticsearch-migration-guide-5.4-5.5.deprecations"></a>
<a id="migration-guides-migration-guide-5.4-5.5--deprecations"></a>

## Deprecations

Some classes that probably are not used by a library user have been renamed, the classes with the old names are still there, but are deprecated:

| old name | new name |
| --- | --- |
| ElasticsearchPartQuery | RepositoryPartQuery |
| ElasticsearchStringQuery | RepositoryStringQuery |
| ReactiveElasticsearchStringQuery | ReactiveRepositoryStringQuery |

<a id="migration-guides-migration-guide-5.4-5.5--_removals"></a>
<a id="migration-guides-migration-guide-5.4-5.5--removals"></a>

### Removals

The following methods that had been deprecated since release 5.3 have been removed:

```none
DocumentOperations.delete(Query, Class<?>)
DocumentOperations.delete(Query, Class<?>, IndexCoordinates)
ReactiveDocumentOperations.delete(Query, Class<?>)
ReactiveDocumentOperations.delete(Query, Class<?>, IndexCoordinates)
```

---

<a id="migration-guides-migration-guide-5.5-6.0"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/migration-guides/migration-guide-5.5-6.0.html -->

<!-- page_index: 15 -->

# Upgrading from 5.5.x to 6.0.x

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="migration-guides-migration-guide-5.5-6.0--page-title"></a>
<a id="migration-guides-migration-guide-5.5-6.0--upgrading-from-5.5.x-to-6.0.x"></a>

# Upgrading from 5.5.x to 6.0.x

This section describes breaking changes from version 5.5.x to 6.0.x and how removed features can be replaced by new introduced features.

<a id="migration-guides-migration-guide-5.5-6.0--elasticsearch-migration-guide-5.5-6.0.breaking-changes"></a>
<a id="migration-guides-migration-guide-5.5-6.0--breaking-changes"></a>

## Breaking Changes

From version 6.0 on, Spring Data Elasticsearch uses the Elasticsearch 9 libraries and as default the new `Rest5Client` provided by these libraries. It is still possible to use the old `RestClient`, check [Elasticsearch clients](#elasticsearch-clients) for information. The configuration callbacks for this `RestClient` have been moved from `org.springframework.data.elasticsearch.client.elc.ElasticsearchClients` to the `org.springframework.data.elasticsearch.client.elc.rest_client.RestClients` class.

In the `org.springframework.data.elasticsearch.core.query.UpdateQuery` class the type of the two fields `ifSeqNo` and `ifPrimaryTerm` has changed from `Integer` to `Long` to align with the normal query and the underlying Elasticsearch client.

<a id="migration-guides-migration-guide-5.5-6.0--elasticsearch-migration-guide-5.5-6.0.deprecations"></a>
<a id="migration-guides-migration-guide-5.5-6.0--deprecations"></a>

## Deprecations

All the code using the old `RestClient` has been moved to the `org.springframework.data.elasticsearch.client.elc.rest_client` package and has been deprecated. Users should switch to the classes from the `org.springframework.data.elasticsearch.client.elc.rest5_client` package.

<a id="migration-guides-migration-guide-5.5-6.0--_removals"></a>
<a id="migration-guides-migration-guide-5.5-6.0--removals"></a>

### Removals

The `org.springframework.data.elasticsearch.core.query.ScriptType` enum has been removed. To distinguish between an inline and a stored script set the appropriate values in the `org.springframework.data.elasticsearch.core.query.ScriptData` record.

These methods have been removed because the Elasticsearch Client 9 does not support them anymore:

```none
org.springframework.data.elasticsearch.client.elc.ReactiveElasticsearchIndicesClient.unfreeze(UnfreezeRequest)
org.springframework.data.elasticsearch.client.elc.ReactiveElasticsearchIndicesClient.unfreeze(Function<UnfreezeRequest.Builder, ObjectBuilder<UnfreezeRequest>>)
```

---

<a id="elasticsearch"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch.html -->

<!-- page_index: 16 -->

# Elasticsearch Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch--page-title"></a>
<a id="elasticsearch--elasticsearch-support"></a>

# Elasticsearch Support

Spring Data support for Elasticsearch contains a wide range of features:

- Spring configuration support for various [Elasticsearch clients](#elasticsearch-clients).
- The [`ElasticsearchTemplate` and `ReactiveElasticsearchTemplate`](#elasticsearch-template) helper classes that provide object mapping between Elasticsearch index operations and POJOs.
- [Exception translation](#elasticsearch-template--exception-translation) into Spring’s portable [Data Access Exception Hierarchy](https://docs.spring.io/spring-framework/reference/7.0data-access.html#dao-exceptions).
- Feature rich [object mapping](#elasticsearch-object-mapping) integrated with *Spring’s* [Conversion Service](https://docs.spring.io/spring-framework/reference/7.0core.html#core-convert).
- [Annotation-based mapping](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations) metadata that is extensible to support other metadata formats.
- Java-based [query, criteria, and update DSLs](#elasticsearch-template--cassandra.template.query).
- Automatic implementation of [imperative and reactive `Repository` interfaces](#repositories) including support for [custom query methods](#repositories-custom-implementations).

For most data-oriented tasks, you can use the `[Reactive]ElasticsearchTemplate` or the `Repository` support, both of which use the rich object-mapping functionality.
Spring Data Elasticsearch uses consistent naming conventions on objects in various APIs to those found in the DataStax Java Driver so that they are familiar and so that you can map your existing knowledge onto the Spring APIs.

<a id="elasticsearch--section-summary"></a>

## Section Summary

- [Elasticsearch Clients](#elasticsearch-clients)
- [Elasticsearch Object Mapping](#elasticsearch-object-mapping)
- [Elasticsearch Operations](#elasticsearch-template)
- [Reactive Elasticsearch Operations](#elasticsearch-reactive-template)
- [Entity Callbacks](#elasticsearch-entity-callbacks)
- [Elasticsearch Auditing](#elasticsearch-auditing)
- [Join-Type implementation](#elasticsearch-join-types)
- [Routing values](#elasticsearch-routing)
- [Miscellaneous Elasticsearch Operation Support](#elasticsearch-misc)
- [Scripted and runtime fields](#elasticsearch-scripted-and-runtime-fields)

---

<a id="elasticsearch-clients"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/clients.html -->

<!-- page_index: 17 -->

# Elasticsearch Clients

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-clients--page-title"></a>
<a id="elasticsearch-clients--elasticsearch-clients"></a>

# Elasticsearch Clients

This chapter illustrates configuration and usage of supported Elasticsearch client implementations.

Spring Data Elasticsearch operates upon an Elasticsearch client (provided by Elasticsearch client libraries) that is connected to a single Elasticsearch node or a cluster.
Although the Elasticsearch Client can be used directly to work with the cluster, applications using Spring Data Elasticsearch normally use the higher level abstractions of [Elasticsearch Operations](#elasticsearch-template) and [Elasticsearch Repositories](#elasticsearch-repositories-elasticsearch-repositories).

<a id="elasticsearch-clients--elasticsearch.clients.rest5client"></a>
<a id="elasticsearch-clients--imperative-rest5client"></a>

## Imperative Rest5Client

To use the imperative (non-reactive) Rest5Client - the default client provided by the Elasticsearch Java client library from version 9 on -, a configuration bean must be configured like this:

```java
import org.springframework.data.elasticsearch.client.elc.ElasticsearchConfiguration;

@Configuration
public class MyClientConfig extends ElasticsearchConfiguration {

	@Override
	public ClientConfiguration clientConfiguration() {
		return ClientConfiguration.builder()           (1)
			.connectedTo("localhost:9200")
			.build();
	}
}
```

**1**

for a detailed description of the builder methods see [Client Configuration](#elasticsearch-clients--elasticsearch.clients.configuration)

The [`ElasticsearchConfiguration`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/client/elc/ElasticsearchConfiguration.html) class allows further configuration by overriding for example the `jsonpMapper()` or `transportOptions()` methods.

The following beans can then be injected in other Spring components:

```java
import org.springframework.beans.factory.annotation.Autowired;

@Autowired
ElasticsearchOperations operations;      (1)

@Autowired
ElasticsearchClient elasticsearchClient; (2)

@Autowired
Rest5Client rest5Client;                 (3)

@Autowired
JsonpMapper jsonpMapper;                 (4)
```

<table>
<tr>
<td>1</td>
<td>an implementation of <a href="https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ElasticsearchOperations.html"><code>ElasticsearchOperations</code></a></td>
</tr>
<tr>
<td>2</td>
<td>the <code>co.elastic.clients.elasticsearch.ElasticsearchClient</code> that is used.</td>
</tr>
<tr>
<td>3</td>
<td>the low level <code>Rest5Client</code> from the Elasticsearch libraries</td>
</tr>
<tr>
<td>4</td>
<td>the <code>JsonpMapper</code> user by the Elasticsearch <code>Transport</code></td>
</tr>
</table>

Basically one should just use the [`ElasticsearchOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ElasticsearchOperations.html) to interact with the Elasticsearch cluster.
When using repositories, this instance is used under the hood as well.

<a id="elasticsearch-clients--elasticsearch.clients.restclient"></a>
<a id="elasticsearch-clients--deprecated-imperative-restclient"></a>

## Deprecated Imperative RestClient

To use the imperative (non-reactive) RestClient - deprecated since version 6 - , the following dependency needs to be added, adapt the correct version. The exclusion is needed in a Spring Boot application:

```xml
        <dependency>
            <groupId>org.elasticsearch.client</groupId>
            <artifactId>elasticsearch-rest-client</artifactId>
            <version>${elasticsearch-client.version}</version>
            <exclusions>
                <exclusion>
                    <groupId>commons-logging</groupId>
                    <artifactId>commons-logging</artifactId>
                </exclusion>
            </exclusions>
        </dependency>
```

The configuration bean must then be configured like this:

```java
import org.springframework.data.elasticsearch.client.elc.ElasticsearchLegacyRestClientConfiguration;

@Configuration
public class MyClientConfig extends ElasticsearchLegacyRestClientConfiguration {

	@Override
	public ClientConfiguration clientConfiguration() {
		return ClientConfiguration.builder()           (1)
			.connectedTo("localhost:9200")
			.build();
	}
}
```

**1**

for a detailed description of the builder methods see [Client Configuration](#elasticsearch-clients--elasticsearch.clients.configuration)

The [`ElasticsearchConfiguration`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/client/elc/ElasticsearchConfiguration.html) class allows further configuration by overriding for example the `jsonpMapper()` or `transportOptions()` methods.

The following beans can then be injected in other Spring components:

```java
import org.springframework.beans.factory.annotation.Autowired;

@Autowired
ElasticsearchOperations operations;      (1)

@Autowired
ElasticsearchClient elasticsearchClient; (2)

@Autowired
RestClient restClient;                   (3)

@Autowired
JsonpMapper jsonpMapper;                 (4)
```

<table>
<tr>
<td>1</td>
<td>an implementation of <a href="https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ElasticsearchOperations.html"><code>ElasticsearchOperations</code></a></td>
</tr>
<tr>
<td>2</td>
<td>the <code>co.elastic.clients.elasticsearch.ElasticsearchClient</code> that is used.</td>
</tr>
<tr>
<td>3</td>
<td>the low level <code>RestClient</code> from the Elasticsearch libraries</td>
</tr>
<tr>
<td>4</td>
<td>the <code>JsonpMapper</code> user by the Elasticsearch <code>Transport</code></td>
</tr>
</table>

Basically one should just use the [`ElasticsearchOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ElasticsearchOperations.html) to interact with the Elasticsearch cluster.
When using repositories, this instance is used under the hood as well.

<a id="elasticsearch-clients--elasticsearch.clients.reactiverest5client"></a>
<a id="elasticsearch-clients--reactive-rest5client"></a>

## Reactive Rest5Client

When working with the reactive stack, the configuration must be derived from a different class:

```java
import org.springframework.data.elasticsearch.client.elc.ReactiveElasticsearchConfiguration;

@Configuration
public class MyClientConfig extends ReactiveElasticsearchConfiguration {

	@Override
	public ClientConfiguration clientConfiguration() {
		return ClientConfiguration.builder()           (1)
			.connectedTo("localhost:9200")
			.build();
	}
}
```

**1**

for a detailed description of the builder methods see [Client Configuration](#elasticsearch-clients--elasticsearch.clients.configuration)

The [`ReactiveElasticsearchConfiguration`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/client/elc/ReactiveElasticsearchConfiguration.html) class allows further configuration by overriding for example the `jsonpMapper()` or `transportOptions()` methods.

The following beans can then be injected in other Spring components:

```java
import org.springframework.beans.factory.annotation.Autowired;

@Autowired
ReactiveElasticsearchOperations operations;      (1)

@Autowired
ReactiveElasticsearchClient elasticsearchClient; (2)

@Autowired
Rest5Client rest5Client;                           (3)

@Autowired
JsonpMapper jsonpMapper;                         (4)
```

the following can be injected:

<table>
<tr>
<td>1</td>
<td>an implementation of <a href="https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ReactiveElasticsearchOperations.html"><code>ReactiveElasticsearchOperations</code></a></td>
</tr>
<tr>
<td>2</td>
<td>the <code>org.springframework.data.elasticsearch.client.elc.ReactiveElasticsearchClient</code> that is used.
This is a reactive implementation based on the Elasticsearch client implementation.</td>
</tr>
<tr>
<td>3</td>
<td>the low level <code>RestClient</code> from the Elasticsearch libraries</td>
</tr>
<tr>
<td>4</td>
<td>the <code>JsonpMapper</code> user by the Elasticsearch <code>Transport</code></td>
</tr>
</table>

Basically one should just use the [`ReactiveElasticsearchOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ReactiveElasticsearchOperations.html) to interact with the Elasticsearch cluster.
When using repositories, this instance is used under the hood as well.

<a id="elasticsearch-clients--elasticsearch.clients.reactiverestclient"></a>
<a id="elasticsearch-clients--deprecated-reactive-restclient"></a>

## Deprecated Reactive RestClient

See the section above for the imperative code to use the deprecated RestClient for the necessary dependencies to include.

When working with the reactive stack, the configuration must be derived from a different class:

```java
import org.springframework.data.elasticsearch.client.elc.ReactiveElasticsearchLegacyRestClientConfiguration;

@Configuration
public class MyClientConfig extends ReactiveElasticsearchLegacyRestClientConfiguration {

	@Override
	public ClientConfiguration clientConfiguration() {
		return ClientConfiguration.builder()           (1)
			.connectedTo("localhost:9200")
			.build();
	}
}
```

**1**

for a detailed description of the builder methods see [Client Configuration](#elasticsearch-clients--elasticsearch.clients.configuration)

The [`ReactiveElasticsearchConfiguration`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/client/elc/ReactiveElasticsearchConfiguration.html) class allows further configuration by overriding for example the `jsonpMapper()` or `transportOptions()` methods.

The following beans can then be injected in other Spring components:

```java
import org.springframework.beans.factory.annotation.Autowired;

@Autowired
ReactiveElasticsearchOperations operations;      (1)

@Autowired
ReactiveElasticsearchClient elasticsearchClient; (2)

@Autowired
RestClient restClient;                           (3)

@Autowired
JsonpMapper jsonpMapper;                         (4)
```

the following can be injected:

<table>
<tr>
<td>1</td>
<td>an implementation of <a href="https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ReactiveElasticsearchOperations.html"><code>ReactiveElasticsearchOperations</code></a></td>
</tr>
<tr>
<td>2</td>
<td>the <code>org.springframework.data.elasticsearch.client.elc.ReactiveElasticsearchClient</code> that is used.
This is a reactive implementation based on the Elasticsearch client implementation.</td>
</tr>
<tr>
<td>3</td>
<td>the low level <code>RestClient</code> from the Elasticsearch libraries</td>
</tr>
<tr>
<td>4</td>
<td>the <code>JsonpMapper</code> user by the Elasticsearch <code>Transport</code></td>
</tr>
</table>

Basically one should just use the [`ReactiveElasticsearchOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ReactiveElasticsearchOperations.html) to interact with the Elasticsearch cluster.
When using repositories, this instance is used under the hood as well.

<a id="elasticsearch-clients--elasticsearch.clients.configuration"></a>
<a id="elasticsearch-clients--client-configuration"></a>

## Client Configuration

Client behaviour can be changed via the [`ClientConfiguration`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/client/ClientConfiguration.html) that allows to set options for SSL, connect and socket timeouts, headers and other parameters.

Example 1. Client Configuration

```java
import org.springframework.data.elasticsearch.client.ClientConfiguration;
import org.springframework.data.elasticsearch.support.HttpHeaders;

import static org.springframework.data.elasticsearch.client.elc.ElasticsearchClients.*;

HttpHeaders httpHeaders = new HttpHeaders();
httpHeaders.add("some-header", "on every request")                      (1)

ClientConfiguration clientConfiguration = ClientConfiguration.builder()
  .connectedTo("localhost:9200", "localhost:9291")                      (2)
  .usingSsl()                                                           (3)
  .withProxy("localhost:8888")                                          (4)
  .withPathPrefix("ela")                                                (5)
  .withConnectTimeout(Duration.ofSeconds(5))                            (6)
  .withSocketTimeout(Duration.ofSeconds(3))                             (7)
  .withDefaultHeaders(defaultHeaders)                                   (8)
  .withBasicAuth(username, password)                                    (9)
  .withHeaders(() -> {                                                  (10)
    HttpHeaders headers = new HttpHeaders();
    headers.add("currentTime", LocalDateTime.now().format(DateTimeFormatter.ISO_LOCAL_DATE_TIME));
    return headers;
  })
  .withClientConfigurer(                                                (11)
    ElasticsearchHttpClientConfigurationCallback.from(clientBuilder -> {
  	  // ...
      return clientBuilder;
  	}))
  . // ... other options
  .build();
```

| **1** | Define default headers, if they need to be customized |
| --- | --- |
| **2** | Use the builder to provide cluster addresses, set default `HttpHeaders` or enable SSL. |
| **3** | Optionally enable SSL.There exist overloads of this function that can take a `SSLContext` or as an alternative the fingerprint of the certificate as it is output by Elasticsearch on startup (since version 8). |
| **4** | Optionally set a proxy. |
| **5** | Optionally set a path prefix, mostly used when different clusters a behind some reverse proxy. |
| **6** | Set the connection timeout. |
| **7** | Set the socket timeout. |
| **8** | Optionally set headers. |
| **9** | Add basic authentication. |
| **10** | A `Supplier<HttpHeaders>` function can be specified which is called every time before a request is sent to Elasticsearch - here, as an example, the current time is written in a header. |
| **11** | a function to configure the created client (see [Client configuration callbacks](#elasticsearch-clients--elasticsearch.clients.configuration.callbacks)), can be added multiple times. |

> [!IMPORTANT]
> Adding a Header supplier as shown in above example allows to inject headers that may change over the time, like authentication JWT tokens.
> If this is used in the reactive setup, the supplier function **must not** block!

<a id="elasticsearch-clients--elasticsearch.clients.configuration.callbacks"></a>
<a id="elasticsearch-clients--client-configuration-callbacks"></a>

### Client configuration callbacks

The [`ClientConfiguration`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/client/ClientConfiguration.html) class offers the most common parameters to configure the client.
In the case this is not enough, the user can add callback functions by using the `withClientConfigurer(ClientConfigurationCallback<?>)` method.

The following callbacks are provided:

<a id="elasticsearch-clients--elasticsearch.clients.configuration.callbacks.rest5"></a>
<a id="elasticsearch-clients--configuration-of-the-low-level-elasticsearch-rest5client-:"></a>

#### Configuration of the low level Elasticsearch `Rest5Client`:

This callback provides a `org.elasticsearch.client.RestClientBuilder` that can be used to configure the Elasticsearch
`Rest5Client`:

```java
ClientConfiguration.builder()
    .connectedTo("localhost:9200", "localhost:9291")
    .withClientConfigurer(Rest5Clients.ElasticsearchRest5ClientConfigurationCallback.from(restClientBuilder -> {
        // configure the Elasticsearch Rest5Client
        return restClientBuilder;
    }))
    .build();
```

<a id="elasticsearch-clients--elasticsearch.clients.configuration.callbacks.rest"></a>
<a id="elasticsearch-clients--configuration-of-the-deprecated-low-level-elasticsearch-restclient-:"></a>

#### Configuration of the deprecated low level Elasticsearch `RestClient`:

This callback provides a `org.elasticsearch.client.RestClientBuilder` that can be used to configure the Elasticsearch
`RestClient`:

```java
ClientConfiguration.builder()
    .connectedTo("localhost:9200", "localhost:9291")
    .withClientConfigurer(RestClients.ElasticsearchRestClientConfigurationCallback.from(restClientBuilder -> {
        // configure the Elasticsearch RestClient
        return restClientBuilder;
    }))
    .build();
```

<a id="elasticsearch-clients--elasticsearch.clients.configurationcallbacks.httpasync5"></a>
<a id="elasticsearch-clients--configuration-of-the-httpasyncclient-used-by-the-low-level-elasticsearch-rest5client-:"></a>

#### Configuration of the HttpAsyncClient used by the low level Elasticsearch `Rest5Client`:

This callback provides a `org.apache.hc.client5.http.impl.async.HttpAsyncClientBuilder` to configure the HttpClient that is
used by the `Rest5Client`.

```java
ClientConfiguration.builder()
    .connectedTo("localhost:9200", "localhost:9291")
    .withClientConfigurer(Rest5Clients.ElasticsearchHttpClientConfigurationCallback.from(httpAsyncClientBuilder -> {
        // configure the HttpAsyncClient
        return httpAsyncClientBuilder;
    }))
    .build();
```

<a id="elasticsearch-clients--elasticsearch.clients.configurationcallbacks.httpasync"></a>
<a id="elasticsearch-clients--configuration-of-the-httpasyncclient-used-by-the-deprecated-low-level-elasticsearch-restclient-:"></a>

#### Configuration of the HttpAsyncClient used by the deprecated low level Elasticsearch `RestClient`:

This callback provides a `org.apache.http.impl.nio.client.HttpAsyncClientBuilder` to configure the HttpClient that is
used by the `RestClient`.

```java
ClientConfiguration.builder()
    .connectedTo("localhost:9200", "localhost:9291")
    .withClientConfigurer(RestClients.ElasticsearchHttpClientConfigurationCallback.from(httpAsyncClientBuilder -> {
        // configure the HttpAsyncClient
        return httpAsyncClientBuilder;
    }))
    .build();
```

<a id="elasticsearch-clients--elasticsearch.clients.configurationcallbacks.connectionconfig"></a>
<a id="elasticsearch-clients--configuration-of-the-connectionconfig-used-by-the-low-level-elasticsearch-rest5client-:"></a>

#### Configuration of the ConnectionConfig used by the low level Elasticsearch `Rest5Client`:

This callback provides a `org.apache.hc.client5.http.config.ConnectionConfig` to configure the connection that is
used by the `Rest5Client`.

```java
ClientConfiguration.builder()
    .connectedTo("localhost:9200", "localhost:9291")
    .withClientConfigurer(Rest5Clients.ElasticsearchConnectionConfigurationCallback.from(connectionConfigBuilder -> {
        // configure the connection
        return connectionConfigBuilder;
    }))
    .build();
```

<a id="elasticsearch-clients--elasticsearch.clients.configurationcallbacks.connectioncmanager"></a>
<a id="elasticsearch-clients--configuration-of-the-connectionmanager-used-by-the-low-level-elasticsearch-rest5client-:"></a>

#### Configuration of the ConnectionManager used by the low level Elasticsearch `Rest5Client`:

This callback provides a `org.apache.hc.client5.http.impl.nio.PoolingAsyncClientConnectionManagerBuilder` to configure the connection manager that is
used by the `Rest5Client`.

```java
ClientConfiguration.builder()
    .connectedTo("localhost:9200", "localhost:9291")
    .withClientConfigurer(Rest5Clients.ElasticsearchConnectionManagerCallback.from(connectionManagerBuilder -> {
        // configure the connection manager
        return connectionManagerBuilder;
    }))
    .build();
```

<a id="elasticsearch-clients--elasticsearch.clients.configurationcallbacks.requestconfig"></a>
<a id="elasticsearch-clients--configuration-of-the-requestconfig-used-by-the-low-level-elasticsearch-rest5client-:"></a>

#### Configuration of the RequestConfig used by the low level Elasticsearch `Rest5Client`:

This callback provides a `org.apache.hc.client5.http.config.RequestConfig` to configure the RequestConfig that is
used by the `Rest5Client`.

```java
ClientConfiguration.builder()
    .connectedTo("localhost:9200", "localhost:9291")
    .withClientConfigurer(Rest5Clients.ElasticsearchRequestConfigCallback.from(requestConfigBuilder -> {
        // configure the request config
        return requestConfigBuilder;
    }))
    .build();
```

<a id="elasticsearch-clients--elasticsearch.clients.logging"></a>
<a id="elasticsearch-clients--client-logging"></a>

## Client Logging

To see what is actually sent to and received from the server `Request` / `Response` logging on the transport level needs to be turned on as outlined in the snippet below.
This can be enabled in the Elasticsearch client by setting the level of the `co.elastic.clients.transport.rest5_client.low_level.Request` package to "trace" (see
[www.elastic.co/docs/reference/elasticsearch/clients/java/transport/rest5-client/usage/logging](https://www.elastic.co/docs/reference/elasticsearch/clients/java/transport/rest5-client/usage/logging))

Enable transport layer logging

- XML
- yml
- ini

```xml
<logger name="co.elastic.clients.transport.rest5_client.low_level.Request" level="trace"/>
```

```yml
logging.level:
  co.elastic.clients.transport.rest5_client.low_level.Request: trace
```

```ini
logging.level.co.elastic.clients.transport.rest5_client.low_level.Request=trace
```

---

<a id="elasticsearch-object-mapping"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/object-mapping.html -->

<!-- page_index: 18 -->

# Elasticsearch Object Mapping

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-object-mapping--page-title"></a>
<a id="elasticsearch-object-mapping--elasticsearch-object-mapping"></a>

# Elasticsearch Object Mapping

Spring Data Elasticsearch Object Mapping is the process that maps a Java object - the domain entity - into the JSON representation that is stored in Elasticsearch and back.
The class that is internally used for this mapping is the
`MappingElasticsearchConverter`.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model"></a>
<a id="elasticsearch-object-mapping--meta-model-object-mapping"></a>

## Meta Model Object Mapping

The Metamodel based approach uses domain type information for reading/writing from/to Elasticsearch.
This allows to register `Converter` instances for specific domain type mapping.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations"></a>
<a id="elasticsearch-object-mapping--mapping-annotation-overview"></a>

### Mapping Annotation Overview

The `MappingElasticsearchConverter` uses metadata to drive the mapping of objects to documents.
The metadata is taken from the entity’s properties which can be annotated.

The following annotations are available:

- `@Document`: Applied at the class level to indicate this class is a candidate for mapping to the database.
  The most important attributes are (check the API documentation for the complete list of attributes):

  - `indexName`: the name of the index to store this entity in.
    This can contain a SpEL template expression like `"log-#{T(java.time.LocalDate).now().toString()}"`
  - `createIndex`: flag whether to create an index on repository bootstrapping.
    Default value is *true*.
    See [Automatic creation of indices with the corresponding mapping](#elasticsearch-repositories-elasticsearch-repositories--elasticsearch.repositories.autocreation)
- `@Id`: Applied at the field level to mark the field used for identity purpose.
- `@Transient`, `@ReadOnlyProperty`, `@WriteOnlyProperty`: see the following section [Controlling which properties are written to and read from Elasticsearch](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.read-write) for detailed information.
- `@PersistenceConstructor`: Marks a given constructor - even a package protected one - to use when instantiating the object from the database.
  Constructor arguments are mapped by name to the key values in the retrieved Document.
- `@Field`: Applied at the field level and defines properties of the field, most of the attributes map to the respective [Elasticsearch Mapping](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping.html) definitions (the following list is not complete, check the annotation Javadoc for a complete reference):

  - `name`: The name of the field as it will be represented in the Elasticsearch document, if not set, the Java field name is used.
  - `type`: The field type, can be one of *Text, Keyword, Long, Integer, Short, Byte, Double, Float, Half\_Float, Scaled\_Float, Date, Date\_Nanos, Boolean, Binary, Integer\_Range, Float\_Range, Long\_Range, Double\_Range, Date\_Range, Ip\_Range, Object, Nested, Ip, TokenCount, Percolator, Flattened, Search\_As\_You\_Type*.
    See [Elasticsearch Mapping Types](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-types.html).
    If the field type is not specified, it defaults to `FieldType.Auto`.
    This means, that no mapping entry is written for the property and that Elasticsearch will add a mapping entry dynamically when the first data for this property is stored (check the Elasticsearch documentation for dynamic mapping rules).
  - `format`: One or more built-in date formats, see the next section [Date format mapping](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.date-formats).
  - `pattern`: One or more custom date formats, see the next section [Date format mapping](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.date-formats).
  - `store`: Flag whether the original field value should be store in Elasticsearch, default value is *false*.
  - `analyzer`, `searchAnalyzer`, `normalizer` for specifying custom analyzers and normalizer.
- `@GeoPoint`: Marks a field as *geo\_point* datatype.
  Can be omitted if the field is an instance of the `GeoPoint` class.
- `@ValueConverter` defines a class to be used to convert the given property.
  In difference to a registered Spring `Converter` this only converts the annotated property and not every property of the given type.

The mapping metadata infrastructure is defined in a separate spring-data-commons project that is technology agnostic.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.read-write"></a>
<a id="elasticsearch-object-mapping--controlling-which-properties-are-written-to-and-read-from-elasticsearch"></a>

#### Controlling which properties are written to and read from Elasticsearch

This section details the annotations that define if the value of a property is written to or read from Elasticsearch.

`@Transient`: A property annotated with this annotation will not be written to the mapping, it’s value will not be sent to Elasticsearch and when documents are returned from Elasticsearch, this property will not be set in the resulting entity.

`@ReadOnlyProperty`: A property with this annotation will not have its value written to Elasticsearch, but when returning data, the property will be filled with the value returned in the document from Elasticsearch.
One use case for this are runtime fields defined in the index mapping.

`@WriteOnlyProperty`: A property with this annotation will have its value stored in Elasticsearch but will not be set with any value when reading document.
This can be used for example for synthesized fields which should go into the Elasticsearch index but are not used elsewhere.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.date-formats"></a>
<a id="elasticsearch-object-mapping--date-format-mapping"></a>

#### Date format mapping

Properties that derive from `TemporalAccessor` or are of type `java.util.Date` must either have a `@Field` annotation of type `FieldType.Date` or a custom converter must be registered for this type.
This paragraph describes the use of
`FieldType.Date`.

There are two attributes of the `@Field` annotation that define which date format information is written to the mapping (also see [Elasticsearch Built In Formats](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-date-format.html#built-in-date-formats) and [Elasticsearch Custom Date Formats](https://www.elastic.co/guide/en/elasticsearch/reference/current/mapping-date-format.html#custom-date-formats))

The `format` attribute is used to define at least one of the predefined formats.
If it is not defined, then a default value of *\_date\_optional\_time* and *epoch\_millis* is used.

The `pattern` attribute can be used to add additional custom format strings.
If you want to use only custom date formats, you must set the `format` property to empty `{}`.

The following table shows the different attributes and the mapping created from their values:

| annotation | format string in Elasticsearch mapping |
| --- | --- |
| @Field(type=FieldType.Date) | "date\_optional\_time\|\|epoch\_millis", |
| @Field(type=FieldType.Date, format=DateFormat.basic\_date) | "basic\_date" |
| @Field(type=FieldType.Date, format={DateFormat.basic\_date, DateFormat.basic\_time}) | "basic\_date\|\|basic\_time" |
| @Field(type=FieldType.Date, pattern="dd.MM.uuuu") | "date\_optional\_time\|\|epoch\_millis\|\|dd.MM.uuuu", |
| @Field(type=FieldType.Date, format={}, pattern="dd.MM.uuuu") | "dd.MM.uuuu" |

> [!NOTE]
> If you are using a custom date format, you need to use *uuuu* for the year instead of *yyyy*.
> This is due to a [change in Elasticsearch 7](https://www.elastic.co/guide/en/elasticsearch/reference/current/migrate-to-java-time.html#java-time-migration-incompatible-date-formats).

Check the code of the `org.springframework.data.elasticsearch.annotations.DateFormat` enum for a complete list of predefined values and their patterns.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.range"></a>
<a id="elasticsearch-object-mapping--range-types"></a>

#### Range types

When a field is annotated with a type of one of *Integer\_Range, Float\_Range, Long\_Range, Double\_Range, Date\_Range,* or *Ip\_Range* the field must be an instance of a class that will be mapped to an Elasticsearch range, for example:

```java
class SomePersonData {

    @Field(type = FieldType.Integer_Range)
    private ValidAge validAge;

    // getter and setter
}

class ValidAge {
    @Field(name="gte")
    private Integer from;

    @Field(name="lte")
    private Integer to;

    // getter and setter
}
```

As an alternative Spring Data Elasticsearch provides a `Range<T>` class so that the previous example can be written as:

```java
class SomePersonData {

    @Field(type = FieldType.Integer_Range)
    private Range<Integer> validAge;

    // getter and setter
}
```

Supported classes for the type `<T>` are `Integer`, `Long`, `Float`, `Double`, `Date` and classes that implement the
`TemporalAccessor` interface.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.mapped-names"></a>
<a id="elasticsearch-object-mapping--mapped-field-names"></a>

#### Mapped field names

Without further configuration, Spring Data Elasticsearch will use the property name of an object as field name in Elasticsearch.
This can be changed for individual field by using the `@Field` annotation on that property.

It is also possible to define a `FieldNamingStrategy` in the configuration of the client ([Elasticsearch Clients](#elasticsearch-clients)).
If for example a `SnakeCaseFieldNamingStrategy` is configured, the property *sampleProperty* of the object would be mapped to *sample\_property* in Elasticsearch.
A `FieldNamingStrategy` applies to all entities; it can be overwritten by setting a specific name with `@Field` on a property.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.non-field-backed-properties"></a>
<a id="elasticsearch-object-mapping--non-field-backed-properties"></a>

#### Non-field-backed properties

Normally the properties used in an entity are fields of the entity class.
There might be cases, when a property value is calculated in the entity and should be stored in Elasticsearch.
In this case, the getter method (`getProperty()`) can be annotated with the `@Field` annotation, in addition to that the method must be annotated with `@AccessType(AccessType.Type
.PROPERTY)`.
The third annotation that is needed in such a case is `@WriteOnlyProperty`, as such a value is only written to Elasticsearch.
A full example:

```java
@Field(type = Keyword)
@WriteOnlyProperty
@AccessType(AccessType.Type.PROPERTY)
public String getProperty() {
	return "some value that is calculated here";
}
```

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations.misc"></a>
<a id="elasticsearch-object-mapping--other-property-annotations"></a>

#### Other property annotations

<a id="elasticsearch-object-mapping--indexedindexname"></a>

##### @IndexedIndexName

This annotation can be set on a String property of an entity.
This property will not be written to the mapping, it will not be stored in Elasticsearch and its value will not be read from an Elasticsearch document.
After an entity is persisted, for example with a call to `ElasticsearchOperations.save(T entity)`, the entity returned from that call will contain the name of the index that an entity was saved to in that property.
This is useful when the index name is dynamically set by a bean, or when writing to a write alias.

Putting some value into such a property does not set the index into which an entity is stored!

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.rules"></a>
<a id="elasticsearch-object-mapping--mapping-rules"></a>

### Mapping Rules

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.rules.typehints"></a>
<a id="elasticsearch-object-mapping--type-hints"></a>

> [!NOTE]
> #### Type Hints

Mapping uses *type hints* embedded in the document sent to the server to allow generic type mapping.
Those type hints are represented as `_class` attributes within the document and are written for each aggregate root.

Example 1. Type Hints

```java
public class Person {              (1)
  @Id String id;
  String firstname;
  String lastname;
}
```

```json
{
  "_class" : "com.example.Person", (1)
  "id" : "cb7bef",
  "firstname" : "Sarah",
  "lastname" : "Connor"
}
```

**1**

By default the domain types class name is used for the type hint.

Type hints can be configured to hold custom information.
Use the `@TypeAlias` annotation to do so.

> [!NOTE]
> Make sure to add types with `@TypeAlias` to the initial entity set (`AbstractElasticsearchConfiguration#getInitialEntitySet`) to already have entity information available when first reading data from the store.

Example 2. Type Hints with Alias

```java
@TypeAlias("human")                (1)
public class Person {

  @Id String id;
  // ...
}
```

```json
{
  "_class" : "human",              (1)
  "id" : ...
}
```

**1**

The configured alias is used when writing the entity.

> [!NOTE]
> Type hints will not be written for nested Objects unless the properties type is `Object`, an interface or the actual value type does not match the properties declaration.

<a id="elasticsearch-object-mapping--disabling-type-hints"></a>

> [!NOTE]
> ##### Disabling Type Hints

It may be necessary to disable writing of type hints when the index that should be used already exists without having the type hints defined in its mapping and with the mapping mode set to strict.
In this case, writing the type hint will produce an error, as the field cannot be added automatically.

Type hints can be disabled for the whole application by overriding the method `writeTypeHints()` in a configuration class derived from `AbstractElasticsearchConfiguration` (see [Elasticsearch Clients](#elasticsearch-clients)).

As an alternative they can be disabled for a single index with the `@Document` annotation:

```java
@Document(indexName = "index", writeTypeHint = WriteTypeHint.FALSE)
```

> [!WARNING]
> We strongly advise against disabling Type Hints.
> Only do this if you are forced to.
> Disabling type hints can lead to documents not being retrieved correctly from Elasticsearch in case of polymorphic data or document retrieval may fail completely.

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.rules.geospatial"></a>
<a id="elasticsearch-object-mapping--geospatial-types"></a>

#### Geospatial Types

Geospatial types like `Point` & `GeoPoint` are converted into *lat/lon* pairs.

Example 3. Geospatial types

```java
public class Address {
  String city, street;
  Point location;
}
```

```json
{
  "city" : "Los Angeles",
  "street" : "2800 East Observatory Road",
  "location" : { "lat" : 34.118347, "lon" : -118.3026284 }
}
```

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.rules.geojson"></a>
<a id="elasticsearch-object-mapping--geojson-types"></a>

#### GeoJson Types

Spring Data Elasticsearch supports the GeoJson types by providing an interface `GeoJson` and implementations for the different geometries.
They are mapped to Elasticsearch documents according to the GeoJson specification.
The corresponding properties of the entity are specified in the index mappings as `geo_shape` when the index mappings is written. (check the [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/geo-shape.html) as well)

Example 4. GeoJson types

```java
public class Address {

  String city, street;
  GeoJsonPoint location;
}
```

```json
{"city": "Los Angeles","street": "2800 East Observatory Road","location": {"type": "Point","coordinates": [-118.3026284, 34.118347]}}
```

The following GeoJson types are implemented:

- `GeoJsonPoint`
- `GeoJsonMultiPoint`
- `GeoJsonLineString`
- `GeoJsonMultiLineString`
- `GeoJsonPolygon`
- `GeoJsonMultiPolygon`
- `GeoJsonGeometryCollection`

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.rules.collections"></a>
<a id="elasticsearch-object-mapping--collections"></a>

#### Collections

For values inside Collections apply the same mapping rules as for aggregate roots when it comes to *type hints* and [Custom Conversions](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.conversions).

Example 5. Collections

```java
public class Person {

  // ...

  List<Person> friends;

}
```

```json
{
  // ...

  "friends" : [ { "firstname" : "Kyle", "lastname" : "Reese" } ]
}
```

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.rules.maps"></a>
<a id="elasticsearch-object-mapping--maps"></a>

#### Maps

For values inside Maps apply the same mapping rules as for aggregate roots when it comes to *type hints* and [Custom Conversions](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.conversions).
However the Map key needs to a String to be processed by Elasticsearch.

Example 6. Collections

```java
public class Person {

  // ...

  Map<String, Address> knownLocations;

}
```

```json
{// ...
"knownLocations" : {"arrivedAt" : {"city" : "Los Angeles","street" : "2800 East Observatory Road","location" : { "lat" : 34.118347, "lon" : -118.3026284 }}}}
```

<a id="elasticsearch-object-mapping--elasticsearch.mapping.meta-model.conversions"></a>
<a id="elasticsearch-object-mapping--custom-conversions"></a>

### Custom Conversions

Looking at the `Configuration` from the [previous section](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model) `ElasticsearchCustomConversions` allows registering specific rules for mapping domain and simple types.

Example 7. Meta Model Object Mapping Configuration

```java
@Configuration public class Config extends ElasticsearchConfiguration  {
@Override public ClientConfiguration clientConfiguration() {return ClientConfiguration.builder() // .connectedTo("localhost:9200") // .build();}
@Bean @Override public ElasticsearchCustomConversions elasticsearchCustomConversions() {return new ElasticsearchCustomConversions(Arrays.asList(new AddressToMap(), new MapToAddress()));       (1)}
@WritingConverter                                                 (2) static class AddressToMap implements Converter<Address, Map<String, Object>> {
@Override public Map<String, Object> convert(Address source) {
LinkedHashMap<String, Object> target = new LinkedHashMap<>(); target.put("ciudad", source.getCity()); // ...
return target;}}
@ReadingConverter                                                 (3) static class MapToAddress implements Converter<Map<String, Object>, Address> {
@Override public Address convert(Map<String, Object> source) {
// ...return address;}}}
```

```json
{
  "ciudad" : "Los Angeles",
  "calle" : "2800 East Observatory Road",
  "localidad" : { "lat" : 34.118347, "lon" : -118.3026284 }
}
```

| **1** | Add `Converter` implementations. |
| --- | --- |
| **2** | Set up the `Converter` used for writing `DomainType` to Elasticsearch. |
| **3** | Set up the `Converter` used for reading `DomainType` from search result. |

---

<a id="elasticsearch-template"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/template.html -->

<!-- page_index: 19 -->

# Elasticsearch Operations

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-template--page-title"></a>
<a id="elasticsearch-template--elasticsearch-operations"></a>

# Elasticsearch Operations

Spring Data Elasticsearch uses several interfaces to define the operations that can be called against an Elasticsearch index (for a description of the reactive interfaces see [Reactive Elasticsearch Operations](#elasticsearch-reactive-template)).

- [`IndexOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/IndexOperations.html) defines actions on index level like creating or deleting an index.
- [`DocumentOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/DocumentOperations.html) defines actions to store, update and retrieve entities based on their id.
- [`SearchOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/SearchOperations.html) define the actions to search for multiple entities using queries
- [`ElasticsearchOperations`](https://docs.spring.io/spring-data/elasticsearch/reference/api/java/org/springframework/data/elasticsearch/core/ElasticsearchOperations.html) combines the `DocumentOperations` and `SearchOperations` interfaces.

These interfaces correspond to the structuring of the [Elasticsearch API](https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html).

The default implementations of the interfaces offer:

- index management functionality.
- Read/Write mapping support for domain types.
- A rich query and criteria api.
- Resource management and Exception translation.

> [!NOTE]
> Index management and automatic creation of indices and mappings.
>
> The `IndexOperations` interface and the provided implementation which can be obtained from an `ElasticsearchOperations` instance - for example with a call to `operations.indexOps(clazz)`- give the user the ability to create indices, put mappings or store template and alias information in the Elasticsearch cluster.
> Details of the index that will be created can be set by using the `@Setting` annotation, refer to [Index settings](#elasticsearch-misc--elasticsearc.misc.index.settings) for further information.
>
> **None of these operations are done automatically** by the implementations of `IndexOperations` or `ElasticsearchOperations`.
> It is the user’s responsibility to call the methods.
>
> There is support for automatic creation of indices and writing the mappings when using Spring Data Elasticsearch repositories, see [Automatic creation of indices with the corresponding mapping](#elasticsearch-repositories-elasticsearch-repositories--elasticsearch.repositories.autocreation)

<a id="elasticsearch-template--elasticsearch.operations.usage"></a>
<a id="elasticsearch-template--usage-examples"></a>

## Usage examples

The example shows how to use an injected `ElasticsearchOperations` instance in a Spring REST controller.
The example assumes that `Person` is a class that is annotated with `@Document`, `@Id` etc (see [Mapping Annotation Overview](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations)).

Example 1. ElasticsearchOperations usage

```java
@RestController @RequestMapping("/") public class TestController {
private  ElasticsearchOperations elasticsearchOperations;
public TestController(ElasticsearchOperations elasticsearchOperations) { (1) this.elasticsearchOperations = elasticsearchOperations;}
@PostMapping("/person") public String save(@RequestBody Person person) {                         (2) Person savedEntity = elasticsearchOperations.save(person); return savedEntity.getId();}
@GetMapping("/person/{id}") public Person findById(@PathVariable("id")  Long id) {                   (3) Person person = elasticsearchOperations.get(id.toString(), Person.class); return person;}}
```

<table>
<tr>
<td>1</td>
<td>Let Spring inject the provided <code>ElasticsearchOperations</code> bean in the constructor.</td>
</tr>
<tr>
<td>2</td>
<td>Store some entity in the Elasticsearch cluster.
The id is read from the returned entity, as it might have been null in the <code>person</code> object and been created by Elasticsearch.</td>
</tr>
<tr>
<td>3</td>
<td>Retrieve the entity with a get by id.</td>
</tr>
</table>

To see the full possibilities of `ElasticsearchOperations` please refer to the API documentation.

<a id="elasticsearch-template--elasticsearch.operations.searchresulttypes"></a>
<a id="elasticsearch-template--search-result-types"></a>

## Search Result Types

When a document is retrieved with the methods of the `DocumentOperations` interface, just the found entity will be returned.
When searching with the methods of the `SearchOperations` interface, additional information is available for each entity, for example the *score* or the *sortValues* of the found entity.

In order to return this information, each entity is wrapped in a `SearchHit` object that contains this entity-specific additional information.
These `SearchHit` objects themselves are returned within a `SearchHits` object which additionally contains informations about the whole search like the *maxScore* or requested aggregations or the execution duration it took to complete the request.
The following classes and interfaces are now available:

SearchHit<T>

Contains the following information:

- Id
- Score
- Sort Values
- Highlight fields
- Inner hits (this is an embedded `SearchHits` object containing eventually returned inner hits)
- The retrieved entity of type <T>

SearchHits<T>

Contains the following information:

- Number of total hits
- Total hits relation
- Maximum score
- A list of `SearchHit<T>` objects
- Returned aggregations
- Returned suggest results

SearchPage<T>

Defines a Spring Data `Page` that contains a `SearchHits<T>` element and can be used for paging access using repository methods.

SearchScrollHits<T>

Returned by the low level scroll API functions in `ElasticsearchRestTemplate`, it enriches a `SearchHits<T>` with the Elasticsearch scroll id.

SearchHitsIterator<T>

An Iterator returned by the streaming functions of the `SearchOperations` interface.

ReactiveSearchHits

`ReactiveSearchOperations` has methods returning a `Mono<ReactiveSearchHits<T>>`, this contains the same information as a `SearchHits<T>` object, but will provide the contained `SearchHit<T>` objects as a `Flux<SearchHit<T>>` and not as a list.

<a id="elasticsearch-template--elasticsearch.operations.queries"></a>
<a id="elasticsearch-template--queries"></a>

## Queries

Almost all of the methods defined in the `SearchOperations` and `ReactiveSearchOperations` interface take a `Query` parameter that defines the query to execute for searching. `Query` is an interface and Spring Data Elasticsearch provides three implementations: `CriteriaQuery`, `StringQuery` and `NativeQuery`.

<a id="elasticsearch-template--elasticsearch.operations.criteriaquery"></a>
<a id="elasticsearch-template--criteriaquery"></a>

### CriteriaQuery

`CriteriaQuery` based queries allow the creation of queries to search for data without knowing the syntax or basics of Elasticsearch queries.
They allow the user to build queries by simply chaining and combining `Criteria` objects that specify the criteria the searched documents must fulfill.

> [!NOTE]
> when talking about AND or OR when combining criteria keep in mind, that in Elasticsearch AND are converted to a **must** condition and OR to a **should**

`Criteria` and their usage are best explained by example (let’s assume we have a `Book` entity with a `price` property):

Example 2. Get books with a given price

```java
Criteria criteria = new Criteria("price").is(42.0);
Query query = new CriteriaQuery(criteria);
```

Conditions for the same field can be chained, they will be combined with a logical AND:

Example 3. Get books with a given price

```java
Criteria criteria = new Criteria("price").greaterThan(42.0).lessThan(34.0);
Query query = new CriteriaQuery(criteria);
```

When chaining `Criteria`, by default a AND logic is used:

Example 4. Get all persons with first name *James* and last name *Miller*:

```java
Criteria criteria = new Criteria("lastname").is("Miller") (1)
  .and("firstname").is("James")                           (2)
Query query = new CriteriaQuery(criteria);
```

**1**

the first `Criteria`

**2**

the and() creates a new `Criteria` and chaines it to the first one.

If you want to create nested queries, you need to use subqueries for this.
Let’s assume we want to find all persons with a last name of *Miller* and a first name of either *Jack* or *John*:

Example 5. Nested subqueries

```java
Criteria miller = new Criteria("lastName").is("Miller")  (1)
  .subCriteria(                                          (2)
    new Criteria().or("firstName").is("John")            (3)
      .or("firstName").is("Jack")                        (4)
  );
Query query = new CriteriaQuery(criteria);
```

| **1** | create a first `Criteria` for the last name |
| --- | --- |
| **2** | this is combined with AND to a subCriteria |
| **3** | This sub Criteria is an OR combination for the first name *John* |
| **4** | and the first name Jack |

Please refer to the API documentation of the `Criteria` class for a complete overview of the different available operations.

<a id="elasticsearch-template--elasticsearch.operations.stringquery"></a>
<a id="elasticsearch-template--stringquery"></a>

### StringQuery

This class takes an Elasticsearch query as JSON String.
The following code shows a query that searches for persons having the first name "Jack":

```java
Query query = new StringQuery("{ \"match\": { \"firstname\": { \"query\": \"Jack\" } } } ");
SearchHits<Person> searchHits = operations.search(query, Person.class);
```

Using `StringQuery` may be appropriate if you already have an Elasticsearch query to use.

<a id="elasticsearch-template--elasticsearch.operations.nativequery"></a>
<a id="elasticsearch-template--nativequery"></a>

### NativeQuery

`NativeQuery` is the class to use when you have a complex query, or a query that cannot be expressed by using the `Criteria` API, for example when building queries and using aggregates.
It allows to use all the different `co.elastic.clients.elasticsearch._types.query_dsl.Query` implementations from the Elasticsearch library therefore named "native".

The following code shows how to search for persons with a given `firstName` and for the found documents have a terms aggregation that counts the number of occurrences of the `lastName` for these persons:

```java
Query query = NativeQuery.builder()
	.withAggregation("lastNames", Aggregation.of(a -> a
		.terms(ta -> ta.field("lastName").size(10))))
	.withQuery(q -> q
		.match(m -> m
			.field("firstName")
			.query(firstName)
		)
	)
	.withPageable(pageable)
	.build();

SearchHits<Person> searchHits = operations.search(query, Person.class);
```

<a id="elasticsearch-template--elasticsearch.operations.searchtemplatequery"></a>
<a id="elasticsearch-template--searchtemplatequery"></a>

### SearchTemplateQuery

This is a special implementation of the `Query` interface to be used in combination with a stored search template.
See [Search Template support](#elasticsearch-misc--elasticsearch.misc.searchtemplates) for further information.

---

<a id="elasticsearch-reactive-template"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/reactive-template.html -->

<!-- page_index: 20 -->

# Reactive Elasticsearch Operations

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-reactive-template--page-title"></a>
<a id="elasticsearch-reactive-template--reactive-elasticsearch-operations"></a>

# Reactive Elasticsearch Operations

`ReactiveElasticsearchOperations` is the gateway to executing high level commands against an Elasticsearch cluster using the `ReactiveElasticsearchClient`.

The `ReactiveElasticsearchTemplate` is the default implementation of `ReactiveElasticsearchOperations`.

To get started the `ReactiveElasticsearchOperations` needs to know about the actual client to work with.
Please see [Reactive Rest Client](#elasticsearch-clients--elasticsearch.clients.reactiverestclient) for details on the client and how to configure it.

<a id="elasticsearch-reactive-template--elasticsearch.reactive.operations.usage"></a>
<a id="elasticsearch-reactive-template--reactive-operations-usage"></a>

## Reactive Operations Usage

`ReactiveElasticsearchOperations` lets you save, find and delete your domain objects and map those objects to documents stored in Elasticsearch.

Consider the following:

Example 1. Use the ReactiveElasticsearchOperations

```java
@Document(indexName = "marvel")
public class Person {

  private @Id String id;
  private String name;
  private int age;
  // Getter/Setter omitted...
}
```

```java
ReactiveElasticsearchOperations operations;

// ...

operations.save(new Person("Bruce Banner", 42))                    (1)
  .doOnNext(System.out::println)
  .flatMap(person -> operations.get(person.id, Person.class))      (2)
  .doOnNext(System.out::println)
  .flatMap(person -> operations.delete(person))                    (3)
  .doOnNext(System.out::println)
  .flatMap(id -> operations.count(Person.class))                   (4)
  .doOnNext(System.out::println)
  .subscribe();                                                    (5)
```

The above outputs the following sequence on the console.

```text
> Person(id=QjWCWWcBXiLAnp77ksfR, name=Bruce Banner, age=42)
> Person(id=QjWCWWcBXiLAnp77ksfR, name=Bruce Banner, age=42)
> QjWCWWcBXiLAnp77ksfR
> 0
```

**1**

Insert a new `Person` document into the *marvel* index . The `id` is generated on server side and set into the instance returned.

**2**

Lookup the `Person` with matching `id` in the *marvel* index.

**3**

Delete the `Person` with matching `id`, extracted from the given instance, in the *marvel* index.

**4**

Count the total number of documents in the *marvel* index.

**5**

Don’t forget to *subscribe()*.

---

<a id="elasticsearch-entity-callbacks"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/entity-callbacks.html -->

<!-- page_index: 21 -->

# Entity Callbacks

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-entity-callbacks--page-title"></a>
<a id="elasticsearch-entity-callbacks--entity-callbacks"></a>

# Entity Callbacks

The Spring Data infrastructure provides hooks for modifying an entity before and after certain methods are invoked.
Those so called `EntityCallback` instances provide a convenient way to check and potentially modify an entity in a callback fashioned style.
An `EntityCallback` looks pretty much like a specialized `ApplicationListener`.
Some Spring Data modules publish store specific events (such as `BeforeSaveEvent`) that allow modifying the given entity. In some cases, such as when working with immutable types, these events can cause trouble.
Also, event publishing relies on `ApplicationEventMulticaster`. If configuring that with an asynchronous `TaskExecutor` it can lead to unpredictable outcomes, as event processing can be forked onto a Thread.

Entity callbacks provide integration points with both synchronous and reactive APIs to guarantee in-order execution at well-defined checkpoints within the processing chain, returning a potentially modified entity or a reactive wrapper type.

Entity callbacks are typically separated by API type. This separation means that a synchronous API considers only synchronous entity callbacks and a reactive implementation considers only reactive entity callbacks.

> [!NOTE]
> The Entity Callback API has been introduced with Spring Data Commons 2.2. It is the recommended way of applying entity modifications.
> Existing store specific `ApplicationEvents` are still published **before** the invoking potentially registered `EntityCallback` instances.

<a id="elasticsearch-entity-callbacks--entity-callbacks.implement"></a>
<a id="elasticsearch-entity-callbacks--implementing-entity-callbacks"></a>

## Implementing Entity Callbacks

An `EntityCallback` is directly associated with its domain type through its generic type argument.
Each Spring Data module typically ships with a set of predefined `EntityCallback` interfaces covering the entity lifecycle.

Anatomy of an `EntityCallback`

```java
@FunctionalInterface public interface BeforeSaveCallback<T> extends EntityCallback<T> {
/** * Entity callback method invoked before a domain object is saved.* Can return either the same or a modified instance.* * @return the domain object to be persisted.*/ (1) T onBeforeSave(T entity, (2) String collection); (3)}
```

**1**

`BeforeSaveCallback` specific method to be called before an entity is saved. Returns a potentially modified instance.

**2**

The entity right before persisting.

**3**

A number of store specific arguments like the *collection* the entity is persisted to.

Anatomy of a reactive `EntityCallback`

```java
@FunctionalInterface public interface ReactiveBeforeSaveCallback<T> extends EntityCallback<T> {
/** * Entity callback method invoked on subscription, before a domain object is saved.* The returned Publisher can emit either the same or a modified instance.* * @return Publisher emitting the domain object to be persisted.*/ (1) Publisher<T> onBeforeSave(T entity, (2) String collection); (3)}
```

**1**

`BeforeSaveCallback` specific method to be called on subscription, before an entity is saved. Emits a potentially modified instance.

**2**

The entity right before persisting.

**3**

A number of store specific arguments like the *collection* the entity is persisted to.

> [!NOTE]
> Optional entity callback parameters are defined by the implementing Spring Data module and inferred from call site of `EntityCallback.callback()`.

Implement the interface suiting your application needs like shown in the example below:

Example `BeforeSaveCallback`

```java
class DefaultingEntityCallback implements BeforeSaveCallback<Person>, Ordered {      (2)
@Override public Object onBeforeSave(Person entity, String collection) {                   (1)
if("user".equals(collection)) {return …;}
return …;}
@Override public int getOrder() {return 100;                                                                  (2)}}
```

**1**

Callback implementation according to your requirements.

**2**

Potentially order the entity callback if multiple ones for the same domain type exist. Ordering follows lowest precedence.

<a id="elasticsearch-entity-callbacks--entity-callbacks.register"></a>
<a id="elasticsearch-entity-callbacks--registering-entity-callbacks"></a>

## Registering Entity Callbacks

`EntityCallback` beans are picked up by the store specific implementations in case they are registered in the `ApplicationContext`.
Most template APIs already implement `ApplicationContextAware` and therefore have access to the `ApplicationContext`

The following example explains a collection of valid entity callback registrations:

Example `EntityCallback` Bean registration

```java
@Order(1)                                                           (1) @Component class First implements BeforeSaveCallback<Person> {
@Override public Person onBeforeSave(Person person) {return // ...}}
@Component class DefaultingEntityCallback implements BeforeSaveCallback<Person>,Ordered { (2)
@Override public Object onBeforeSave(Person entity, String collection) {// ...}
@Override public int getOrder() {return 100;                                                  (2)}}
@Configuration public class EntityCallbackConfiguration {
@Bean BeforeSaveCallback<Person> unorderedLambdaReceiverCallback() {   (3) return (BeforeSaveCallback<Person>) it -> // ...}}
@Component class UserCallbacks implements BeforeConvertCallback<User>,BeforeSaveCallback<User> {   (4)
@Override public Person onBeforeConvert(User user) {return // ...}
@Override public Person onBeforeSave(User user) {return // ...}}
```

| **1** | `BeforeSaveCallback` receiving its order from the `@Order` annotation. |
| --- | --- |
| **2** | `BeforeSaveCallback` receiving its order via the `Ordered` interface implementation. |
| **3** | `BeforeSaveCallback` using a lambda expression. Unordered by default and invoked last. Note that callbacks implemented by a lambda expression do not expose typing information hence invoking these with a non-assignable entity affects the callback throughput. Use a `class` or `enum` to enable type filtering for the callback bean. |
| **4** | Combine multiple entity callback interfaces in a single implementation class. |

<a id="elasticsearch-entity-callbacks--elasticsearch.entity-callbacks"></a>
<a id="elasticsearch-entity-callbacks--store-specific-entitycallbacks"></a>

## Store specific EntityCallbacks

Spring Data Elasticsearch uses the `EntityCallback` API internally for its auditing support and reacts on the following callbacks:

| Callback | Method | Description | Order |
| --- | --- | --- | --- |
| Reactive/BeforeConvertCallback | `onBeforeConvert(T entity, IndexCoordinates index)` | Invoked before a domain object is converted to `org.springframework.data.elasticsearch.core.document.Document`. Can return the `entity` or a modified entity which then will be converted. | `Ordered.LOWEST_PRECEDENCE` |
| Reactive/AfterLoadCallback | `onAfterLoad(Document document, Class<T> type, IndexCoordinates indexCoordinates)` | Invoked after the result from Elasticsearch has been read into a `org.springframework.data.elasticsearch.core.document.Document`. | `Ordered.LOWEST_PRECEDENCE` |
| Reactive/AfterConvertCallback | `onAfterConvert(T entity, Document document, IndexCoordinates indexCoordinates)` | Invoked after a domain object is converted from `org.springframework.data.elasticsearch.core.document.Document` on reading result data from Elasticsearch. | `Ordered.LOWEST_PRECEDENCE` |
| Reactive/AuditingEntityCallback | `onBeforeConvert(Object entity, IndexCoordinates index)` | Marks an auditable entity *created* or *modified* | 100 |
| Reactive/AfterSaveCallback | `T onAfterSave(T entity, IndexCoordinates index)` | Invoked after a domain object is saved. | `Ordered.LOWEST_PRECEDENCE` |

---

<a id="elasticsearch-auditing"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/auditing.html -->

<!-- page_index: 22 -->

# Elasticsearch Auditing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-auditing--page-title"></a>
<a id="elasticsearch-auditing--elasticsearch-auditing"></a>

# Elasticsearch Auditing

<a id="elasticsearch-auditing--elasticsearch.auditing.preparing"></a>
<a id="elasticsearch-auditing--preparing-entities"></a>

## Preparing entities

In order for the auditing code to be able to decide whether an entity instance is new, the entity must implement the `Persistable<ID>` interface which is defined as follows:

```java
import org.jspecify.annotations.Nullable;

public interface Persistable<ID> {
    @Nullable
    ID getId();

    boolean isNew();
}
```

As the existence of an Id is not a sufficient criterion to determine if an enitity is new in Elasticsearch, additional information is necessary. One way is to use the creation-relevant auditing fields for this decision:

A `Person` entity might look as follows - omitting getter and setter methods for brevity:

```java
@Document(indexName = "person")
public class Person implements Persistable<Long> {
    @Id private Long id;
    private String lastName;
    private String firstName;
    @CreatedDate
    @Field(type = FieldType.Date, format = DateFormat.basic_date_time)
    private Instant createdDate;
    @CreatedBy
    private String createdBy
    @Field(type = FieldType.Date, format = DateFormat.basic_date_time)
    @LastModifiedDate
    private Instant lastModifiedDate;
    @LastModifiedBy
    private String lastModifiedBy;

    public Long getId() {                                                 (1)
        return id;
    }

    @Override
    public boolean isNew() {
        return id == null || (createdDate == null && createdBy == null);  (2)
    }
}
```

**1**

the getter is the required implementation from the interface

**2**

an object is new if it either has no `id` or none of fields containing creation attributes are set.

<a id="elasticsearch-auditing--elasticsearch.auditing.activating"></a>
<a id="elasticsearch-auditing--activating-auditing"></a>

## Activating auditing

After the entities have been set up and providing the `AuditorAware` - or `ReactiveAuditorAware` - the Auditing must be activated by setting the `@EnableElasticsearchAuditing` on a configuration class:

```java
@Configuration
@EnableElasticsearchRepositories
@EnableElasticsearchAuditing
class MyConfiguration {
   // configuration code
}
```

When using the reactive stack this must be:

```java
@Configuration
@EnableReactiveElasticsearchRepositories
@EnableReactiveElasticsearchAuditing
class MyConfiguration {
   // configuration code
}
```

If your code contains more than one `AuditorAware` bean for different types, you must provide the name of the bean to use as an argument to the `auditorAwareRef` parameter of the
`@EnableElasticsearchAuditing` annotation.

---

<a id="elasticsearch-join-types"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/join-types.html -->

<!-- page_index: 23 -->

# Join-Type implementation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-join-types--page-title"></a>
<a id="elasticsearch-join-types--join-type-implementation"></a>

# Join-Type implementation

Spring Data Elasticsearch supports the [Join data type](https://www.elastic.co/guide/en/elasticsearch/reference/current/parent-join.html) for creating the corresponding index mappings and for storing the relevant information.

<a id="elasticsearch-join-types--elasticsearch.jointype.setting-up"></a>
<a id="elasticsearch-join-types--setting-up-the-data"></a>

## Setting up the data

For an entity to be used in a parent child join relationship, it must have a property of type `JoinField` which must be annotated.
Let’s assume a `Statement` entity where a statement may be a *question*, an *answer*, a *comment* or a *vote* (a *Builder* is also shown in this example, it’s not necessary, but later used in the sample code):

```java
@Document(indexName = "statements") @Routing("routing")                                                                       (1) public class Statement {@Id private String id;
@Field(type = FieldType.Text) private String text;
@Field(type = FieldType.Keyword) private String routing;
@JoinTypeRelations(relations ={@JoinTypeRelation(parent = "question", children = {"answer", "comment"}), (2) @JoinTypeRelation(parent = "answer", children = "vote")                   (3)}) private JoinField<String> relation;                                                   (4)
private Statement() {}
public static StatementBuilder builder() {return new StatementBuilder();}
public String getId() {return id;}
public void setId(String id) {this.id = id;}
public String getRouting() {return routing;}
public void setRouting(String routing) {this.routing = routing;}
public String getText() {return text;}
public void setText(String text) {this.text = text;}
public JoinField<String> getRelation() {return relation;}
public void setRelation(JoinField<String> relation) {this.relation = relation;}
public static final class StatementBuilder {private String id; private String text; private String routing; private JoinField<String> relation;
private StatementBuilder() {}
public StatementBuilder withId(String id) {this.id = id; return this;}
public StatementBuilder withRouting(String routing) {this.routing = routing; return this;}
public StatementBuilder withText(String text) {this.text = text; return this;}
public StatementBuilder withRelation(JoinField<String> relation) {this.relation = relation; return this;}
public Statement build() {Statement statement = new Statement(); statement.setId(id); statement.setRouting(routing); statement.setText(text); statement.setRelation(relation); return statement;}}}
```

| **1** | for routing related info see [Routing values](#elasticsearch-routing) |
| --- | --- |
| **2** | a question can have answers and comments |
| **3** | an answer can have votes |
| **4** | the `JoinField` property is used to combine the name (*question*, *answer*, *comment* or *vote*) of the relation with the parent id. The generic type must be the same as the `@Id` annotated property. |

Spring Data Elasticsearch will build the following mapping for this class:

```json
{"statements": {"mappings": {"properties": {"_class": {"type": "text","fields": {"keyword": {"type": "keyword","ignore_above": 256}} },"routing": {"type": "keyword" },"relation": {"type": "join","eager_global_ordinals": true,"relations": {"question": ["answer","comment" ],"answer": "vote"} },"text": {"type": "text"}}}}}
```

<a id="elasticsearch-join-types--elasticsearch.jointype.storing"></a>
<a id="elasticsearch-join-types--storing-data"></a>

## Storing data

Given a repository for this class the following code inserts a question, two answers, a comment and a vote:

```java
void init() {
    repository.deleteAll();

    Statement savedWeather = repository.save(
        Statement.builder()
            .withText("How is the weather?")
            .withRelation(new JoinField<>("question"))                          (1)
            .build());

    Statement sunnyAnswer = repository.save(
        Statement.builder()
            .withText("sunny")
            .withRelation(new JoinField<>("answer", savedWeather.getId()))      (2)
            .build());

    repository.save(
        Statement.builder()
            .withText("rainy")
            .withRelation(new JoinField<>("answer", savedWeather.getId()))      (3)
            .build());

    repository.save(
        Statement.builder()
            .withText("I don't like the rain")
            .withRelation(new JoinField<>("comment", savedWeather.getId()))     (4)
            .build());

    repository.save(
        Statement.builder()
            .withText("+1 for the sun")
            .withRouting(savedWeather.getId())
            .withRelation(new JoinField<>("vote", sunnyAnswer.getId()))         (5)
            .build());
}
```

| **1** | create a question statement |
| --- | --- |
| **2** | the first answer to the question |
| **3** | the second answer |
| **4** | a comment to the question |
| **5** | a vote for the first answer, this needs to have the routing set to the weather document, see [Routing values](#elasticsearch-routing). |

<a id="elasticsearch-join-types--elasticsearch.jointype.retrieving"></a>
<a id="elasticsearch-join-types--retrieving-data"></a>

## Retrieving data

Currently native queries must be used to query the data, so there is no support from standard repository methods. [Custom Repository Implementations](#repositories-custom-implementations) can be used instead.

The following code shows as an example how to retrieve all entries that have a *vote* (which must be *answers*, because only answers can have a vote) using an `ElasticsearchOperations` instance:

```java
SearchHits<Statement> hasVotes() {

	Query query = NativeQuery.builder()
		.withQuery(co.elastic.clients.elasticsearch._types.query_dsl.Query.of(qb -> qb
			.hasChild(hc -> hc
				.type("answer")
				.queryName("vote")
				.query(matchAllQueryAsQuery())
				.scoreMode(ChildScoreMode.None)
			)))
		.build();

	return operations.search(query, Statement.class);
}
```

---

<a id="elasticsearch-routing"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/routing.html -->

<!-- page_index: 24 -->

# Routing values

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-routing--page-title"></a>
<a id="elasticsearch-routing--routing-values"></a>

# Routing values

When Elasticsearch stores a document in an index that has multiple shards, it determines the shard to you use based on the *id* of the document.
Sometimes it is necessary to predefine that multiple documents should be indexed on the same shard (join-types, faster search for related data).
For this Elasticsearch offers the possibility to define a routing, which is the value that should be used to calculate the shard from instead of the *id*.

Spring Data Elasticsearch supports routing definitions on storing and retrieving data in the following ways:

<a id="elasticsearch-routing--elasticsearch.routing.join-types"></a>
<a id="elasticsearch-routing--routing-on-join-types"></a>

## Routing on join-types

When using join-types (see [Join-Type implementation](#elasticsearch-join-types)), Spring Data Elasticsearch will automatically use the `parent` property of the entity’s `JoinField` property as the value for the routing.

This is correct for all the use-cases where the parent-child relationship has just one level.
If it is deeper, like a child-parent-grandparent relationship - like in the above example from *vote* → *answer* → *question* - then the routing needs to explicitly specified by using the techniques described in the next section (the *vote* needs the *question.id* as routing value).

<a id="elasticsearch-routing--elasticsearch.routing.custom"></a>
<a id="elasticsearch-routing--custom-routing-values"></a>

## Custom routing values

To define a custom routing for an entity, Spring Data Elasticsearch provides a `@Routing` annotation (reusing the `Statement` class from above):

```java
@Document(indexName = "statements")
@Routing("routing")                  (1)
public class Statement {
    @Id
    private String id;

    @Field(type = FieldType.Text)
    private String text;

    @JoinTypeRelations(
        relations =
            {
                @JoinTypeRelation(parent = "question", children = {"answer", "comment"}),
                @JoinTypeRelation(parent = "answer", children = "vote")
            }
    )
    private JoinField<String> relation;

    @Nullable
    @Field(type = FieldType.Keyword)
    private String routing;          (2)

    // getter/setter...
}
```

**1**

This defines *"routing"* as routing specification

**2**

a property with the name *routing*

If the `routing` specification of the annotation is a plain string and not a SpEL expression, it is interpreted as the name of a property of the entity, in the example it’s the *routing* property.
The value of this property will then be used as the routing value for all requests that use the entity.

It is also possible to us a SpEL expression in the `@Document` annotation like this:

```java
@Document(indexName = "statements")
@Routing("@myBean.getRouting(#entity)")
public class Statement{
    // all the needed stuff
}
```

In this case the user needs to provide a bean with the name *myBean* that has a method `String getRouting(Object)`. To reference the entity *"#entity"* must be used in the SpEL expression, and the return value must be `null` or the routing value as a String.

If plain property’s names and SpEL expressions are not enough to customize the routing definitions, it is possible to define provide an implementation of the `RoutingResolver` interface. This can then be set on the `ElasticOperations` instance:

```java
RoutingResolver resolver = ...;

ElasticsearchOperations customOperations= operations.withRouting(resolver);
```

The `withRouting()` functions return a copy of the original `ElasticsearchOperations` instance with the customized routing set.

When a routing has been defined on an entity when it is stored in Elasticsearch, the same value must be provided when doing a *get* or *delete* operation. For methods that do not use an entity - like `get(ID)` or `delete(ID)` - the `ElasticsearchOperations.withRouting(RoutingResolver)` method can be used like this:

```java
String id = "someId";
String routing = "theRoutingValue";

// get an entity
Statement s = operations
                .withRouting(RoutingResolver.just(routing))       (1)
                .get(id, Statement.class);

// delete an entity
operations.withRouting(RoutingResolver.just(routing)).delete(id);
```

**1**

`RoutingResolver.just(s)` returns a resolver that will just return the given String.

---

<a id="elasticsearch-misc"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/misc.html -->

<!-- page_index: 25 -->

# Miscellaneous Elasticsearch Operation Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-misc--page-title"></a>
<a id="elasticsearch-misc--miscellaneous-elasticsearch-operation-support"></a>

# Miscellaneous Elasticsearch Operation Support

This chapter covers additional support for Elasticsearch operations that cannot be directly accessed via the repository interface.
It is recommended to add those operations as custom implementation as described in [Custom Repository Implementations](#repositories-custom-implementations) .

<a id="elasticsearch-misc--elasticsearc.misc.index.settings"></a>
<a id="elasticsearch-misc--index-settings"></a>

## Index settings

When creating Elasticsearch indices with Spring Data Elasticsearch different index settings can be defined by using the `@Setting` annotation.
The following arguments are available:

- `useServerConfiguration` does not send any settings parameters, so the Elasticsearch server configuration determines them.
- `settingPath` refers to a JSON file defining the settings that must be resolvable in the classpath, it is possible to use a SpEL expression here
- `shards` the number of shards to use, defaults to *1*
- `replicas` the number of replicas, defaults to *1*
- `refreshIntervall`, defaults to *"1s"*
- `indexStoreType`, defaults to *"fs"*

It is as well possible to define [index sorting](https://www.elastic.co/guide/en/elasticsearch/reference/7.11/index-modules-index-sorting.html) (check the linked Elasticsearch documentation for the possible field types and values):

```java
@Document(indexName = "entities")
@Setting(
  sortFields = { "secondField", "firstField" },                                  (1)
  sortModes = { Setting.SortMode.max, Setting.SortMode.min },                    (2)
  sortOrders = { Setting.SortOrder.desc, Setting.SortOrder.asc },
  sortMissingValues = { Setting.SortMissing._last, Setting.SortMissing._first })
class Entity {
    @Nullable
    @Id private String id;

    @Nullable
    @Field(name = "first_field", type = FieldType.Keyword)
    private String firstField;

    @Nullable @Field(name = "second_field", type = FieldType.Keyword)
    private String secondField;

    // getter and setter...
}
```

**1**

when defining sort fields, use the name of the Java property (*firstField*), not the name that might be defined for Elasticsearch (*first\_field*)

**2**

`sortModes`, `sortOrders` and `sortMissingValues` are optional, but if they are set, the number of entries must match the number of `sortFields` elements

<a id="elasticsearch-misc--elasticsearch.misc.mappings"></a>
<a id="elasticsearch-misc--index-mapping"></a>

## Index Mapping

When Spring Data Elasticsearch creates the index mapping with the `IndexOperations.createMapping()` methods, it uses the annotations described in [Mapping Annotation Overview](#elasticsearch-object-mapping--elasticsearch.mapping.meta-model.annotations), especially the `@Field` annotation.
In addition to that it is possible to add the `@Mapping` annotation to a class.
This annotation has the following properties:

- `mappingPath` a classpath resource in JSON format; if this is not empty it is used as the mapping, no other mapping processing is done.
- `enabled` when set to false, this flag is written to the mapping and no further processing is done.
- `dateDetection` and `numericDetection` set the corresponding properties in the mapping when not set to `DEFAULT`.
- `dynamicDateFormats` when this String array is not empty, it defines the date formats used for automatic date detection.
- `runtimeFieldsPath` a classpath resource in JSON format containing the definition of runtime fields which is written to the index mappings, for example:

```json
{"day_of_week": {"type": "keyword","script": {"source": "emit(doc['@timestamp'].value.dayOfWeekEnum.getDisplayName(TextStyle.FULL, Locale.ROOT))"}}}
```

<a id="elasticsearch-misc--elasticsearch.misc.filter"></a>
<a id="elasticsearch-misc--filter-builder"></a>

## Filter Builder

Filter Builder improves query speed.

```java
private ElasticsearchOperations operations;

IndexCoordinates index = IndexCoordinates.of("sample-index");

Query query = NativeQuery.builder()
	.withQuery(q -> q
		.matchAll(ma -> ma))
	.withFilter( q -> q
		.bool(b -> b
			.must(m -> m
				.term(t -> t
					.field("id")
					.value(documentId))
			)))
	.build();

SearchHits<SampleEntity> sampleEntities = operations.search(query, SampleEntity.class, index);
```

<a id="elasticsearch-misc--elasticsearch.scroll"></a>
<a id="elasticsearch-misc--using-scroll-for-big-result-set"></a>

## Using Scroll For Big Result Set

Elasticsearch has a scroll API for getting big result set in chunks.
This is internally used by Spring Data Elasticsearch to provide the implementations of the `<T> SearchHitsIterator<T> SearchOperations.searchForStream(Query query, Class<T> clazz, IndexCoordinates index)` method.

```java
IndexCoordinates index = IndexCoordinates.of("sample-index");

Query searchQuery = NativeQuery.builder()
    .withQuery(q -> q
        .matchAll(ma -> ma))
    .withFields("message")
    .withPageable(PageRequest.of(0, 10))
    .build();

SearchHitsIterator<SampleEntity> stream = elasticsearchOperations.searchForStream(searchQuery, SampleEntity.class,
index);

List<SampleEntity> sampleEntities = new ArrayList<>();
while (stream.hasNext()) {
  sampleEntities.add(stream.next());
}

stream.close();
```

There are no methods in the `SearchOperations` API to access the scroll id, if it should be necessary to access this, the following methods of the `AbstractElasticsearchTemplate` can be used (this is the base implementation for the different `ElasticsearchOperations` implementations):

```java
@Autowired ElasticsearchOperations operations;

AbstractElasticsearchTemplate template = (AbstractElasticsearchTemplate)operations;

IndexCoordinates index = IndexCoordinates.of("sample-index");

Query query = NativeQuery.builder()
    .withQuery(q -> q
        .matchAll(ma -> ma))
    .withFields("message")
    .withPageable(PageRequest.of(0, 10))
    .build();

SearchScrollHits<SampleEntity> scroll = template.searchScrollStart(1000, query, SampleEntity.class, index);

String scrollId = scroll.getScrollId();
List<SampleEntity> sampleEntities = new ArrayList<>();
while (scroll.hasSearchHits()) {
  sampleEntities.addAll(scroll.getSearchHits());
  scrollId = scroll.getScrollId();
  scroll = template.searchScrollContinue(scrollId, 1000, SampleEntity.class);
}
template.searchScrollClear(scrollId);
```

To use the Scroll API with repository methods, the return type must defined as `Stream` in the Elasticsearch Repository.
The implementation of the method will then use the scroll methods from the ElasticsearchTemplate.

```java
interface SampleEntityRepository extends Repository<SampleEntity, String> {

    Stream<SampleEntity> findBy();

}
```

<a id="elasticsearch-misc--elasticsearch.misc.sorts"></a>
<a id="elasticsearch-misc--sort-options"></a>

## Sort options

In addition to the default sort options described in [Paging and Sorting](#repositories-query-methods-details--repositories.paging-and-sorting), Spring Data Elasticsearch provides the class `org.springframework.data.elasticsearch.core.query.Order` which derives from `org.springframework.data.domain.Sort.Order`.
It offers additional parameters that can be sent to Elasticsearch when specifying the sorting of the result (see [www.elastic.co/guide/en/elasticsearch/reference/7.15/sort-search-results.html](https://www.elastic.co/guide/en/elasticsearch/reference/7.15/sort-search-results.html)).

There also is the `org.springframework.data.elasticsearch.core.query.GeoDistanceOrder` class which can be used to have the result of a search operation ordered by geographical distance.

If the class to be retrieved has a `GeoPoint` property named *location*, the following `Sort` would sort the results by distance to the given point:

```java
Sort.by(new GeoDistanceOrder("location", new GeoPoint(48.137154, 11.5761247)))
```

<a id="elasticsearch-misc--elasticsearch.misc.runtime-fields"></a>
<a id="elasticsearch-misc--runtime-fields"></a>

## Runtime Fields

From version 7.12 on Elasticsearch has added the feature of runtime fields ([www.elastic.co/guide/en/elasticsearch/reference/7.12/runtime.html](https://www.elastic.co/guide/en/elasticsearch/reference/7.12/runtime.html)).
Spring Data Elasticsearch supports this in two ways:

<a id="elasticsearch-misc--elasticsearch.misc.runtime-fields.index-mappings"></a>
<a id="elasticsearch-misc--runtime-field-definitions-in-the-index-mappings"></a>

### Runtime field definitions in the index mappings

The first way to define runtime fields is by adding the definitions to the index mappings (see [www.elastic.co/guide/en/elasticsearch/reference/7.12/runtime-mapping-fields.html](https://www.elastic.co/guide/en/elasticsearch/reference/7.12/runtime-mapping-fields.html)).
To use this approach in Spring Data Elasticsearch the user must provide a JSON file that contains the corresponding definition, for example:

Example 1. runtime-fields.json

```json
{"day_of_week": {"type": "keyword","script": {"source": "emit(doc['@timestamp'].value.dayOfWeekEnum.getDisplayName(TextStyle.FULL, Locale.ROOT))"}}}
```

The path to this JSON file, which must be present on the classpath, must then be set in the `@Mapping` annotation of the entity:

```java
@Document(indexName = "runtime-fields")
@Mapping(runtimeFieldsPath = "/runtime-fields.json")
public class RuntimeFieldEntity {
	// properties, getter, setter,...
}
```

<a id="elasticsearch-misc--elasticsearch.misc.runtime-fields.query"></a>
<a id="elasticsearch-misc--runtime-fields-definitions-set-on-a-query"></a>

### Runtime fields definitions set on a Query

The second way to define runtime fields is by adding the definitions to a search query (see [www.elastic.co/guide/en/elasticsearch/reference/7.12/runtime-search-request.html](https://www.elastic.co/guide/en/elasticsearch/reference/7.12/runtime-search-request.html)).
The following code example shows how to do this with Spring Data Elasticsearch :

The entity used is a simple object that has a `price` property:

```java
@Document(indexName = "some_index_name")
public class SomethingToBuy {

	private @Id @Nullable String id;
	@Nullable @Field(type = FieldType.Text) private String description;
	@Nullable @Field(type = FieldType.Double) private Double price;

	// getter and setter
}
```

The following query uses a runtime field that calculates a `priceWithTax` value by adding 19% to the price and uses this value in the search query to find all entities where `priceWithTax` is higher or equal than a given value:

```java
RuntimeField runtimeField = new RuntimeField("priceWithTax", "double", "emit(doc['price'].value * 1.19)");
Query query = new CriteriaQuery(new Criteria("priceWithTax").greaterThanEqual(16.5));
query.addRuntimeField(runtimeField);

SearchHits<SomethingToBuy> searchHits = operations.search(query, SomethingToBuy.class);
```

This works with every implementation of the `Query` interface.

<a id="elasticsearch-misc--elasticsearch.misc.point-in-time"></a>
<a id="elasticsearch-misc--point-in-time-pit-api"></a>

## Point In Time (PIT) API

`ElasticsearchOperations` supports the point in time API of Elasticsearch (see [www.elastic.co/guide/en/elasticsearch/reference/8.3/point-in-time-api.html](https://www.elastic.co/guide/en/elasticsearch/reference/8.3/point-in-time-api.html)).
The following code snippet shows how to use this feature with a fictional `Person` class:

```java
ElasticsearchOperations operations; // autowired
Duration tenSeconds = Duration.ofSeconds(10);

String pit = operations.openPointInTime(IndexCoordinates.of("person"), tenSeconds); (1)

// create query for the pit
Query query1 = new CriteriaQueryBuilder(Criteria.where("lastName").is("Smith"))
    .withPointInTime(new Query.PointInTime(pit, tenSeconds))                        (2)
    .build();
SearchHits<Person> searchHits1 = operations.search(query1, Person.class);
// do something with the data

// create 2nd query for the pit, use the id returned in the previous result
Query query2 = new CriteriaQueryBuilder(Criteria.where("lastName").is("Miller"))
    .withPointInTime(
        new Query.PointInTime(searchHits1.getPointInTimeId(), tenSeconds))          (3)
    .build();
SearchHits<Person> searchHits2 = operations.search(query2, Person.class);
// do something with the data

operations.closePointInTime(searchHits2.getPointInTimeId());                        (4)
```

**1**

create a point in time for an index (can be multiple names) and a keep-alive duration and retrieve its id

**2**

pass that id into the query to search together with the next keep-alive value

**3**

for the next query, use the id returned from the previous search

**4**

when done, close the point in time using the last returned id

<a id="elasticsearch-misc--elasticsearch.misc.searchtemplates"></a>
<a id="elasticsearch-misc--search-template-support"></a>

## Search Template support

Use of the search template API is supported.
To use this, it first is necessary to create a stored script.
The `ElasticsearchOperations` interface extends `ScriptOperations` which provides the necessary functions.
The example used here assumes that we have `Person` entity with a property named `firstName`.
A search template script can be saved like this:

```java
import org.springframework.data.elasticsearch.core.ElasticsearchOperations; import org.springframework.data.elasticsearch.core.script.Script;
operations.putScript(                            (1) Script.builder() .withId("person-firstname")                  (2) .withLanguage("mustache")                    (3) .withSource("""                              (4) {"query": {"bool": {"must": [{"match": {"firstName": "{{firstName}}"   (5)}}]} },"from": "{{from}}",                      (6) "size": "{{size}}"                       (7)} """) .build() );
```

| **1** | Use the `putScript()` method to store a search template script |
| --- | --- |
| **2** | The name / id of the script |
| **3** | Scripts that are used in search templates must be in the *mustache* language. |
| **4** | The script source |
| **5** | The search parameter in the script |
| **6** | Paging request offset |
| **7** | Paging request size |

To use a search template in a search query, Spring Data Elasticsearch provides the `SearchTemplateQuery`, an implementation of the `org.springframework.data.elasticsearch.core.query.Query` interface.

> [!NOTE]
> Although `SearchTemplateQuery` is an implementation of the `Query` interface, not all of the functionality provided by the base class is available for a `SearchTemplateQuery` like setting a `Pageable` or a `Sort`. Values for this functionality must be added to the stored script like shown in the following example for paging parameters. If these values are set on the `Query` object, they will be ignored.

In the following code, we will add a call using a search template query to a custom repository implementation (see
[Custom Repository Implementations](#repositories-custom-implementations)) as an example how this can be integrated into a repository call.

We first define the custom repository fragment interface:

```java
interface PersonCustomRepository {
	SearchPage<Person> findByFirstNameWithSearchTemplate(String firstName, Pageable pageable);
}
```

The implementation of this repository fragment looks like this:

```java
public class PersonCustomRepositoryImpl implements PersonCustomRepository {
private final ElasticsearchOperations operations;
public PersonCustomRepositoryImpl(ElasticsearchOperations operations) {this.operations = operations;}
@Override public SearchPage<Person> findByFirstNameWithSearchTemplate(String firstName, Pageable pageable) {
var query = SearchTemplateQuery.builder()                               (1) .withId("person-firstname")                                           (2) .withParams(Map.of(                                                             (3) "firstName", firstName,"from", pageable.getOffset(),"size", pageable.getPageSize())) .build();
SearchHits<Person> searchHits = operations.search(query, Person.class); (4)
return SearchHitSupport.searchPageFor(searchHits, pageable);}}
```

| **1** | Create a `SearchTemplateQuery` |
| --- | --- |
| **2** | Provide the id of the search template |
| **3** | The parameters are passed in a `Map<String,Object>` |
| **4** | Do the search in the same way as with the other query types. |

<a id="elasticsearch-misc--elasticsearch.misc.nested-sort"></a>
<a id="elasticsearch-misc--nested-sort"></a>

## Nested sort

Spring Data Elasticsearch supports sorting within nested objects ([www.elastic.co/guide/en/elasticsearch/reference/8.9/sort-search-results.html#nested-sorting](https://www.elastic.co/guide/en/elasticsearch/reference/8.9/sort-search-results.html#nested-sorting))

The following example, taken from the `org.springframework.data.elasticsearch.core.query.sort.NestedSortIntegrationTests` class, shows how to define the nested sort.

```java
var filter = StringQuery.builder("""
	{ "term": {"movies.actors.sex": "m"} }
	""").build();
var order = new org.springframework.data.elasticsearch.core.query.Order(Sort.Direction.DESC,
	"movies.actors.yearOfBirth")
	.withNested(
		Nested.builder("movies")
			.withNested(
				Nested.builder("movies.actors")
					.withFilter(filter)
					.build())
			.build());

var query = Query.findAll().addSort(Sort.by(order));
```

About the filter query: It is not possible to use a `CriteriaQuery` here, as this query would be converted into a Elasticsearch nested query which does not work in the filter context. So only `StringQuery` or `NativeQuery` can be used here. When using one of these, like the term query above, the Elasticsearch field names must be used, so take care, when these are redefined with the `@Field(name="…")` definition.

For the definition of the order path and the nested paths, the Java entity property names should be used.

---

<a id="elasticsearch-scripted-and-runtime-fields"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/scripted-and-runtime-fields.html -->

<!-- page_index: 26 -->

# Scripted and runtime fields

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-scripted-and-runtime-fields--page-title"></a>
<a id="elasticsearch-scripted-and-runtime-fields--scripted-and-runtime-fields"></a>

# Scripted and runtime fields

Spring Data Elasticsearch supports scripted fields and runtime fields.
Please refer to the Elasticsearch documentation about scripting ([www.elastic.co/guide/en/elasticsearch/reference/current/modules-scripting.html](https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-scripting.html)) and runtime fields ([www.elastic.co/guide/en/elasticsearch/reference/8.9/runtime.html](https://www.elastic.co/guide/en/elasticsearch/reference/8.9/runtime.html)) for detailed information about this.
In the context of Spring Data Elasticsearch you can use

- scripted fields that are used to return fields that are calculated on the result documents and added to the returned document.
- runtime fields that are calculated on the stored documents and can be used in a query and/or be returned in the search result.

The following code snippets will show what you can do (these show imperative code, but the reactive implementation works similar).

<a id="elasticsearch-scripted-and-runtime-fields--the-person-entity"></a>

## The person entity

The enity that is used in these examples is a `Person` entity.
This entity has a `birthDate` and an `age` property.
Whereas the birthdate is fix, the age depends on the time when a query is issued and needs to be calculated dynamically.

```java
import org.jspecify.annotations.Nullable;
import org.springframework.data.annotation.Id;
import org.springframework.data.elasticsearch.annotations.DateFormat;
import org.springframework.data.elasticsearch.annotations.Document;
import org.springframework.data.elasticsearch.annotations.Field;
import org.springframework.data.elasticsearch.annotations.ScriptedField;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;

import static org.springframework.data.elasticsearch.annotations.FieldType.*;

import java.lang.Integer;

@Document(indexName = "persons")
public record Person(
        @Id
        @Nullable
        String id,
        @Field(type = Text)
        String lastName,
        @Field(type = Text)
        String firstName,
        @Field(type = Keyword)
        String gender,
        @Field(type = Date, format = DateFormat.basic_date)
        LocalDate birthDate,
        @Nullable
        @ScriptedField Integer age                   (1)
) {
    public Person(String id,String lastName, String firstName, String gender, String birthDate) {
        this(id,                                     (2)
            lastName,
            firstName,
            LocalDate.parse(birthDate, DateTimeFormatter.ISO_LOCAL_DATE),
            gender,
            null);
    }
}
```

**1**

the `age` property will be calculated and filled in search results.

**2**

a convenience constructor to set up the test data.

Note that the `age` property is annotated with `@ScriptedField`.
This inhibits the writing of a corresponding entry in the index mapping and marks the property as a target to put a calculated field from a search response.

<a id="elasticsearch-scripted-and-runtime-fields--the-repository-interface"></a>

## The repository interface

The repository used in this example:

```java
public interface PersonRepository extends ElasticsearchRepository<Person, String> {

    SearchHits<Person> findAllBy(ScriptedField scriptedField);

    SearchHits<Person> findByGenderAndAgeLessThanEqual(String gender, Integer age, RuntimeField runtimeField);
}
```

<a id="elasticsearch-scripted-and-runtime-fields--the-service-class"></a>

## The service class

The service class has a repository injected and an `ElasticsearchOperations` instance to show several ways of populating and using the `age` property.
We show the code split up in different pieces to put the explanations in

```java
import org.springframework.data.elasticsearch.core.ElasticsearchOperations;
import org.springframework.data.elasticsearch.core.SearchHits;
import org.springframework.data.elasticsearch.core.query.Criteria;
import org.springframework.data.elasticsearch.core.query.CriteriaQuery;
import org.springframework.data.elasticsearch.core.query.FetchSourceFilter;
import org.springframework.data.elasticsearch.core.query.RuntimeField;
import org.springframework.data.elasticsearch.core.query.ScriptData;
import org.springframework.data.elasticsearch.core.query.ScriptType;
import org.springframework.data.elasticsearch.core.query.ScriptedField;
import org.springframework.data.elasticsearch.core.query.StringQuery;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PersonService {
    private final ElasticsearchOperations operations;
    private final PersonRepository repository;

    public PersonService(ElasticsearchOperations operations, SaRPersonRepository repository) {
        this.operations = operations;
        this.repository = repository;
    }

    public void save() { (1)
        List<Person> persons = List.of(
                new Person("1", "Smith", "Mary", "f", "1987-05-03"),
                new Person("2", "Smith", "Joshua", "m", "1982-11-17"),
                new Person("3", "Smith", "Joanna", "f", "2018-03-27"),
                new Person("4", "Smith", "Alex", "m", "2020-08-01"),
                new Person("5", "McNeill", "Fiona", "f", "1989-04-07"),
                new Person("6", "McNeill", "Michael", "m", "1984-10-20"),
                new Person("7", "McNeill", "Geraldine", "f", "2020-03-02"),
                new Person("8", "McNeill", "Patrick", "m", "2022-07-04"));

        repository.saveAll(persons);
    }
```

**1**

a utility method to store some data in Elasticsearch.

<a id="elasticsearch-scripted-and-runtime-fields--scripted-fields"></a>

### Scripted fields

The next piece shows how to use a scripted field to calculate and return the age of the persons.
Scripted fields can only add something to the returned data, the age cannot be used in the query (see runtime fields for that).

```java
    public SearchHits<Person> findAllWithAge() {

        var scriptedField = ScriptedField.of("age",                               (1)
                ScriptData.of(b -> b
                        .withType(ScriptType.INLINE)
                        .withScript("""
                                Instant currentDate = Instant.ofEpochMilli(new Date().getTime());
                                Instant startDate = doc['birth-date'].value.toInstant();
                                return (ChronoUnit.DAYS.between(startDate, currentDate) / 365);
                                """)));

        // version 1: use a direct query
        var query = new StringQuery("""
                { "match_all": {} }
                """);
        query.addScriptedField(scriptedField);                                    (2)
        query.addSourceFilter(FetchSourceFilter.of(b -> b.withIncludes("*")));    (3)

        var result1 = operations.search(query, Person.class);                     (4)

        // version 2: use the repository
        var result2 = repository.findAllBy(scriptedField);                        (5)

        return result1;
    }
```

| **1** | define the `ScriptedField` that calculates the age of a person. |
| --- | --- |
| **2** | when using a `Query`, add the scripted field to the query. |
| **3** | when adding a scripted field to a `Query`, an additional source filter is needed to also retrieve the *normal* fields from the document source. |
| **4** | get the data where the `Person` entities now have the values set in their `age` property. |
| **5** | when using the repository, all that needs to be done is adding the scripted field as method parameter. |

<a id="elasticsearch-scripted-and-runtime-fields--runtime-fields"></a>

### Runtime fields

When using runtime fields, the calculated value can be used in the query itself.
In the following code this is used to run a query for a given gender and maximum age of persons:

```java
    public SearchHits<Person> findWithGenderAndMaxAge(String gender, Integer maxAge) {

        var runtimeField = new RuntimeField("age", "long", """                    (1)
                                Instant currentDate = Instant.ofEpochMilli(new Date().getTime());
                                Instant startDate = doc['birthDate'].value.toInstant();
                                emit (ChronoUnit.DAYS.between(startDate, currentDate) / 365);
                """);

        // variant 1 : use a direct query
        var query = CriteriaQuery.builder(Criteria
                        .where("gender").is(gender)
                        .and("age").lessThanEqual(maxAge))
                .withRuntimeFields(List.of(runtimeField))                         (2)
                .withFields("age")                                                (3)
                .withSourceFilter(FetchSourceFilter.of(b -> b.withIncludes("*"))) (4)
                .build();

        var result1 = operations.search(query, Person.class);                     (5)

        // variant 2: use the repository                                          (6)
        var result2 = repository.findByGenderAndAgeLessThanEqual(gender, maxAge, runtimeField);

        return result1;
    }
}
```

**1**

define the runtime field that calculates the age of a person. // see [asciidoctor.org/docs/user-manual/#builtin-attributes](https://asciidoctor.org/docs/user-manual/#builtin-attributes) for builtin attributes.

**2**

when using `Query`, add the runtime field.

**3**

when adding a scripted field to a `Query`, an additional field parameter is needed to have the calculated value returned.

**4**

when adding a scripted field to a `Query`, an additional source filter is needed to also retrieve the *normal* fields from the document source.

**5**

get the data filtered with the query and where the returned entites have the age property set.

**6**

when using the repository, all that needs to be done is adding the runtime field as method parameter.

In addition to define a runtime fields on a query, they can also be defined in the index by setting the `runtimeFieldsPath` property of the `@Mapping` annotation to point to a JSON file that contains the runtime field definitions.

---

<a id="repositories"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories.html -->

<!-- page_index: 27 -->

# Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories--page-title"></a>
<a id="repositories--repositories"></a>

# Repositories

This chapter explains the basic foundations of Spring Data repositories and Elasticsearch specifics.
Before continuing to the Elasticsearch specifics, make sure you have a sound understanding of the basic concepts.

The goal of the Spring Data repository abstraction is to significantly reduce the amount of boilerplate code required to implement data access layers for various persistence stores.

<a id="repositories--section-summary"></a>

## Section Summary

- [Core concepts](#repositories-core-concepts)
- [Defining Repository Interfaces](#repositories-definition)
- [Elasticsearch Repositories](#elasticsearch-repositories-elasticsearch-repositories)
- [Reactive Elasticsearch Repositories](#elasticsearch-repositories-reactive-elasticsearch-repositories)
- [Creating Repository Instances](#repositories-create-instances)
- [Defining Query Methods](#repositories-query-methods-details)
- [Query methods](#elasticsearch-repositories-elasticsearch-repository-queries)
- [Projections](#repositories-projections)
- [Custom Repository Implementations](#repositories-custom-implementations)
- [Publishing Events from Aggregate Roots](#repositories-core-domain-events)
- [Null Handling of Repository Methods](#repositories-null-handling)
- [CDI Integration](#elasticsearch-repositories-cdi-integration)
- [Repository query keywords](#repositories-query-keywords-reference)
- [Repository query return types](#repositories-query-return-types-reference)

---

<a id="repositories-core-concepts"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/core-concepts.html -->

<!-- page_index: 28 -->

# Core concepts

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-core-concepts--page-title"></a>
<a id="repositories-core-concepts--core-concepts"></a>

# Core concepts

The central interface in the Spring Data repository abstraction is `Repository`.
It takes the domain class to manage as well as the identifier type of the domain class as type arguments.
This interface acts primarily as a marker interface to capture the types to work with and to help you to discover interfaces that extend this one.

> [!TIP]
> Spring Data considers domain types to be entities, more specifically aggregates.
> So you will see the term "entity" used throughout the documentation that can be interchanged with the term "domain type" or "aggregate".
>
> As you might have noticed in the introduction it already hinted towards domain-driven concepts.
> We consider domain objects in the sense of DDD.
> Domain objects have identifiers (otherwise these would be identity-less value objects), and we somehow need to refer to identifiers when working with certain patterns to access data.
> Referring to identifiers will become more meaningful as we talk about repositories and query methods.

The [`CrudRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/CrudRepository.html) and [`ListCrudRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/ListCrudRepository.html) interfaces provide sophisticated CRUD functionality for the entity class that is being managed.

`CrudRepository` Interface

```java
public interface CrudRepository<T, ID> extends Repository<T, ID> {

  <S extends T> S save(S entity);      (1)

  Optional<T> findById(ID primaryKey); (2)

  Iterable<T> findAll();               (3)

  long count();                        (4)

  void delete(T entity);               (5)

  boolean existsById(ID primaryKey);   (6)

  // … more functionality omitted.
}
```

| **1** | Saves the given entity. |
| --- | --- |
| **2** | Returns the entity identified by the given ID. |
| **3** | Returns all entities. |
| **4** | Returns the number of entities. |
| **5** | Deletes the given entity. |
| **6** | Indicates whether an entity with the given ID exists. |

The methods declared in this interface are commonly referred to as CRUD methods.
`ListCrudRepository` offers equivalent methods, but they return `List` where the `CrudRepository` methods return an `Iterable`.

> [!IMPORTANT]
> The repository interface implies a few reserved methods like `findById(ID identifier)` that target the domain type identifier property regardless of its property name.
> Read more about this in “[Defining Query Methods](#repositories-query-methods-details--repositories.query-methods.reserved-methods)”.
>
> You can annotate your query method with `@Query` to provide a custom query if a property named `Id` doesn’t refer to the identifier.
> Following that path can easily lead to confusion and is discouraged as you will quickly hit type limits if the `ID` type and the type of your `Id` property deviate.

> [!NOTE]
> We also provide persistence technology-specific abstractions, such as `JpaRepository` or `MongoRepository`.
> Those interfaces extend `CrudRepository` and expose the capabilities of the underlying persistence technology in addition to the rather generic persistence technology-agnostic interfaces such as `CrudRepository`.

In addition to `CrudRepository`, there are [`PagingAndSortingRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/PagingAndSortingRepository.html) and [`ListPagingAndSortingRepository`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/ListPagingAndSortingRepository.html) which add additional methods to ease paginated access to entities:

`PagingAndSortingRepository` interface

```java
interface PagingAndSortingRepository<T, ID> extends Repository<T, ID> {

  Iterable<T> findAll(Sort sort);

  Page<T> findAll(Pageable pageable);
}
```

> [!NOTE]
> Extension interfaces are subject to be supported by the actual store module.
> While this documentation explains the general scheme, make sure that your store module supports the interfaces that you want to use.

To access the second page of `User` by a page size of 20, you could do something like the following:

```java
PagingAndSortingRepository<User, Long> repository = // … get access to a bean
Page<User> users = repository.findAll(PageRequest.of(1, 20));
```

`ListPagingAndSortingRepository` offers equivalent methods, but returns a `List` where the `PagingAndSortingRepository` methods return an `Iterable`.

In addition to pagination, scrolling provides a more fine-grained access to iterate through chunks of larger result sets.

In addition to query methods, query derivation for both count and delete queries is available.
The following list shows the interface definition for a derived count query:

Derived Count Query

```java
interface UserRepository extends CrudRepository<User, Long> {

  long countByLastname(String lastname);
}
```

The following listing shows the interface definition for a derived delete query:

Derived Delete Query

```java
interface UserRepository extends CrudRepository<User, Long> {

  long deleteByLastname(String lastname);

  List<User> removeByLastname(String lastname);
}
```

<a id="repositories-core-concepts--is-new-state-detection"></a>
<a id="repositories-core-concepts--entity-state-detection-strategies"></a>

## Entity State Detection Strategies

The following table describes the strategies that Spring Data offers for detecting whether an entity is new:

`@Id`-Property inspection (the default)

By default, Spring Data inspects the identifier property of the given entity.
If the identifier property is `null` or `0` in case of primitive types, then the entity is assumed to be new.
Otherwise, it is assumed to not be new.

`@Version`-Property inspection

If a property annotated with `@Version` is present and `null`, or in case of a version property of primitive type `0` the entity is considered new.
If the version property is present but has a different value, the entity is considered to not be new.
If no version property is present Spring Data falls back to inspection of the identifier property.

Implementing `Persistable`

If an entity implements `Persistable`, Spring Data delegates the new detection to the `isNew(…)` method of the entity.
See the [Javadoc](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/domain/Persistable.html) for details.

*Note: Properties of `Persistable` will get detected and persisted if you use `AccessType.PROPERTY`.
To avoid that, use `@Transient`.*

---

<a id="repositories-definition"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/definition.html -->

<!-- page_index: 29 -->

# Defining Repository Interfaces

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-definition--page-title"></a>
<a id="repositories-definition--defining-repository-interfaces"></a>

# Defining Repository Interfaces

To define a repository interface, you first need to define a domain class-specific repository interface.
The interface must extend `Repository` and be typed to the domain class and an ID type.
If you want to expose CRUD methods for that domain type, you may extend `CrudRepository`, or one of its variants instead of `Repository`.

<a id="repositories-definition--repositories.definition-tuning"></a>
<a id="repositories-definition--fine-tuning-repository-definition"></a>

## Fine-tuning Repository Definition

There are a few ways to get started with your repository interface.

The typical approach is to extend `CrudRepository`, which gives you methods for CRUD functionality.
CRUD stands for Create, Read, Update, Delete.
With version 3.0 we also introduced `ListCrudRepository` which is very similar to the `CrudRepository` but for those methods that return multiple entities it returns a `List` instead of an `Iterable` which you might find easier to use.

If you are using a reactive store you might choose `ReactiveCrudRepository`, or `RxJava3CrudRepository` depending on which reactive framework you are using.

If you are using Kotlin you might pick `CoroutineCrudRepository` which utilizes Kotlin’s coroutines.

Additionally you can extend `PagingAndSortingRepository`, `ReactiveSortingRepository`, `RxJava3SortingRepository`, or `CoroutineSortingRepository` if you need methods that allow to specify a `Sort` abstraction or in the first case a `Pageable` abstraction.
Note that the various sorting repositories no longer extend their respective CRUD repository as they did in Spring Data versions prior to 3.0.
Therefore, you need to extend both interfaces if you want functionality of both.

If you do not want to extend Spring Data interfaces, you can also annotate your repository interface with `@RepositoryDefinition`.
Extending one of the CRUD repository interfaces exposes a complete set of methods to manipulate your entities.
If you prefer to be selective about the methods being exposed, copy the methods you want to expose from the CRUD repository into your domain repository.
When doing so, you may change the return type of methods.
Spring Data will honor the return type if possible.
For example, for methods returning multiple entities you may choose `Iterable<T>`, `List<T>`, `Collection<T>` or a VAVR list.

If many repositories in your application should have the same set of methods you can define your own base interface to inherit from.
Such an interface must be annotated with `@NoRepositoryBean`.
This prevents Spring Data to try to create an instance of it directly and failing because it can’t determine the entity for that repository, since it still contains a generic type variable.

The following example shows how to selectively expose CRUD methods (`findById` and `save`, in this case):

Selectively exposing CRUD methods

```java
@NoRepositoryBean interface MyBaseRepository<T, ID> extends Repository<T, ID> {
Optional<T> findById(ID id);
<S extends T> S save(S entity);}
interface UserRepository extends MyBaseRepository<User, Long> {User findByEmailAddress(EmailAddress emailAddress);}
```

In the prior example, you defined a common base interface for all your domain repositories and exposed `findById(…)` as well as `save(…)`.These methods are routed into the base repository implementation of the store of your choice provided by Spring Data (for example, if you use JPA, the implementation is `SimpleJpaRepository`), because they match the method signatures in `CrudRepository`.
So the `UserRepository` can now save users, find individual users by ID, and trigger a query to find `Users` by email address.

> [!NOTE]
> The intermediate repository interface is annotated with `@NoRepositoryBean`.
> Make sure you add that annotation to all repository interfaces for which Spring Data should not create instances at runtime.

<a id="repositories-definition--repositories.multiple-modules"></a>
<a id="repositories-definition--using-repositories-with-multiple-spring-data-modules"></a>

## Using Repositories with Multiple Spring Data Modules

Using a unique Spring Data module in your application makes things simple, because all repository interfaces in the defined scope are bound to the Spring Data module.
Sometimes, applications require using more than one Spring Data module.
In such cases, a repository definition must distinguish between persistence technologies.
When it detects multiple repository factories on the class path, Spring Data enters strict repository configuration mode.
Strict configuration uses details on the repository or the domain class to decide about Spring Data module binding for a repository definition:

1. If the repository definition [extends the module-specific repository](#repositories-definition--repositories.multiple-modules.types), it is a valid candidate for the particular Spring Data module.
2. If the domain class is [annotated with the module-specific type annotation](#repositories-definition--repositories.multiple-modules.annotations), it is a valid candidate for the particular Spring Data module.
   Spring Data modules accept either third-party annotations (such as JPA’s `@Entity`) or provide their own annotations (such as `@Document` for Spring Data MongoDB and Spring Data Elasticsearch).

The following example shows a repository that uses module-specific interfaces (JPA in this case):

Example 1. Repository definitions using module-specific interfaces

```java
interface MyRepository extends JpaRepository<User, Long> { }

@NoRepositoryBean
interface MyBaseRepository<T, ID> extends JpaRepository<T, ID> { … }

interface UserRepository extends MyBaseRepository<User, Long> { … }
```

`MyRepository` and `UserRepository` extend `JpaRepository` in their type hierarchy.
They are valid candidates for the Spring Data JPA module.

The following example shows a repository that uses generic interfaces:

Example 2. Repository definitions using generic interfaces

```java
interface AmbiguousRepository extends Repository<User, Long> { … }

@NoRepositoryBean
interface MyBaseRepository<T, ID> extends CrudRepository<T, ID> { … }

interface AmbiguousUserRepository extends MyBaseRepository<User, Long> { … }
```

`AmbiguousRepository` and `AmbiguousUserRepository` extend only `Repository` and `CrudRepository` in their type hierarchy.
While this is fine when using a unique Spring Data module, multiple modules cannot distinguish to which particular Spring Data these repositories should be bound.

The following example shows a repository that uses domain classes with annotations:

Example 3. Repository definitions using domain classes with annotations

```java
interface PersonRepository extends Repository<Person, Long> { … }

@Entity
class Person { … }

interface UserRepository extends Repository<User, Long> { … }

@Document
class User { … }
```

`PersonRepository` references `Person`, which is annotated with the JPA `@Entity` annotation, so this repository clearly belongs to Spring Data JPA. `UserRepository` references `User`, which is annotated with Spring Data MongoDB’s `@Document` annotation.

The following bad example shows a repository that uses domain classes with mixed annotations:

Example 4. Repository definitions using domain classes with mixed annotations

```java
interface JpaPersonRepository extends Repository<Person, Long> { … }

interface MongoDBPersonRepository extends Repository<Person, Long> { … }

@Entity
@Document
class Person { … }
```

This example shows a domain class using both JPA and Spring Data MongoDB annotations.
It defines two repositories, `JpaPersonRepository` and `MongoDBPersonRepository`.
One is intended for JPA and the other for MongoDB usage.
Spring Data is no longer able to tell the repositories apart, which leads to undefined behavior.

[Repository type details](#repositories-definition--repositories.multiple-modules.types) and [distinguishing domain class annotations](#repositories-definition--repositories.multiple-modules.annotations) are used for strict repository configuration to identify repository candidates for a particular Spring Data module.
Using multiple persistence technology-specific annotations on the same domain type is possible and enables reuse of domain types across multiple persistence technologies.
However, Spring Data can then no longer determine a unique module with which to bind the repository.

The last way to distinguish repositories is by scoping repository base packages.
Base packages define the starting points for scanning for repository interface definitions, which implies having repository definitions located in the appropriate packages.
By default, annotation-driven configuration uses the package of the configuration class.
The [base package in XML-based configuration](#repositories-create-instances--repositories.create-instances.xml) is mandatory.

The following example shows annotation-driven configuration of base packages:

Annotation-driven configuration of base packages

```java
@EnableJpaRepositories(basePackages = "com.acme.repositories.jpa")
@EnableMongoRepositories(basePackages = "com.acme.repositories.mongo")
class Configuration { … }
```

---

<a id="elasticsearch-repositories-elasticsearch-repositories"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/repositories/elasticsearch-repositories.html -->

<!-- page_index: 30 -->

# Elasticsearch Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-repositories-elasticsearch-repositories--page-title"></a>
<a id="elasticsearch-repositories-elasticsearch-repositories--elasticsearch-repositories"></a>

# Elasticsearch Repositories

This chapter includes details of the Elasticsearch repository implementation.

Example 1. The sample `Book` entity

```java
@Document(indexName="books")
class Book {
    @Id
    private String id;

    @Field(type = FieldType.Text)
    private String name;

    @Field(type = FieldType.Text)
    private String summary;

    @Field(type = FieldType.Integer)
    private Integer price;

	// getter/setter ...
}
```

<a id="elasticsearch-repositories-elasticsearch-repositories--elasticsearch.repositories.autocreation"></a>
<a id="elasticsearch-repositories-elasticsearch-repositories--automatic-creation-of-indices-with-the-corresponding-mapping"></a>

## Automatic creation of indices with the corresponding mapping

The `@Document` annotation has an argument `createIndex`.
If this argument is set to true - which is the default value - Spring Data Elasticsearch will during bootstrapping the repository support on application startup check if the index defined by the `@Document` annotation exists.

If it does not exist, the index will be created and the mappings derived from the entity’s annotations (see [Elasticsearch Object Mapping](#elasticsearch-object-mapping)) will be written to the newly created index.
Details of the index that will be created can be set by using the `@Setting` annotation, refer to [Index settings](#elasticsearch-misc--elasticsearc.misc.index.settings) for further information.

<a id="elasticsearch-repositories-elasticsearch-repositories--elasticsearch.repositories.annotations"></a>
<a id="elasticsearch-repositories-elasticsearch-repositories--annotations-for-repository-methods"></a>

## Annotations for repository methods

<a id="elasticsearch-repositories-elasticsearch-repositories--elasticsearch.repositories.annotations.highlight"></a>
<a id="elasticsearch-repositories-elasticsearch-repositories--highlight"></a>

### @Highlight

The `@Highlight` annotation on a repository method defines for which fields of the returned entity highlighting should be included.To search for some text in a `Book` 's name or summary and have the found data highlighted, the following repository method can be used:

```java
interface BookRepository extends Repository<Book, String> {
@Highlight(fields = {@HighlightField(name = "name"),@HighlightField(name = "summary") }) SearchHits<Book> findByNameOrSummary(String text, String summary);}
```

It is possible to define multiple fields to be highlighted like above, and both the `@Highlight` and the `@HighlightField` annotation can further be customized with a `@HighlightParameters` annotation. Check the Javadocs for the possible configuration options.

In the search results the highlight data can be retrieved from the `SearchHit` class.

<a id="elasticsearch-repositories-elasticsearch-repositories--elasticsearch.repositories.annotations.sourcefilters"></a>
<a id="elasticsearch-repositories-elasticsearch-repositories--sourcefilters"></a>

### @SourceFilters

Sometimes the user does not need to have all the properties of an entity returned from a search but only a subset.
Elasticsearch provides source filtering to reduce the amount of data that is transferred across the network to the
application.

When working with `Query` implementations and the `ElasticsearchOperations` this is easily possible by setting a
source filter on the query.

When using repository methods there is the `@SourceFilters` annotation:

```java
interface BookRepository extends Repository<Book, String> {

    @SourceFilters(includes = "name")
    SearchHits<Book> findByName(String text);
}
```

In this example, all the properties of the returned `Book` objects would be `null` except the name.

<a id="elasticsearch-repositories-elasticsearch-repositories--elasticsearch.annotation"></a>
<a id="elasticsearch-repositories-elasticsearch-repositories--annotation-based-configuration"></a>

## Annotation based configuration

The Spring Data Elasticsearch repositories support can be activated using an annotation through JavaConfig.

Example 2. Spring Data Elasticsearch repositories using JavaConfig

```java
@Configuration @EnableElasticsearchRepositories(                             (1) basePackages = "org.springframework.data.elasticsearch.repositories") static class Config {
@Bean public ElasticsearchOperations elasticsearchTemplate() {    (2) // ...}}
class ProductService {
private ProductRepository repository;                       (3)
public ProductService(ProductRepository repository) {this.repository = repository;}
public Page<Product> findAvailableBookByName(String name, Pageable pageable) {return repository.findByAvailableTrueAndNameStartingWith(name, pageable);}}
```

**1**

The `EnableElasticsearchRepositories` annotation activates the Repository support.
If no base package is configured, it will use the one of the configuration class it is put on.

**2**

Provide a Bean named `elasticsearchTemplate` of type `ElasticsearchOperations` by using one of the configurations shown in the [Elasticsearch Operations](#elasticsearch-template) chapter.

**3**

Let Spring inject the Repository bean into your class.

<a id="elasticsearch-repositories-elasticsearch-repositories--elasticsearch.namespace"></a>
<a id="elasticsearch-repositories-elasticsearch-repositories--spring-namespace"></a>

## Spring Namespace

The Spring Data Elasticsearch module contains a custom namespace allowing definition of repository beans as well as elements for instantiating a `ElasticsearchServer` .

Using the `repositories` element looks up Spring Data repositories as described in [Creating Repository Instances](#repositories-create-instances).

Example 3. Setting up Elasticsearch repositories using Namespace

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:elasticsearch="http://www.springframework.org/schema/data/elasticsearch"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       https://www.springframework.org/schema/beans/spring-beans-3.1.xsd
       http://www.springframework.org/schema/data/elasticsearch
       https://www.springframework.org/schema/data/elasticsearch/spring-elasticsearch-1.0.xsd">

  <elasticsearch:repositories base-package="com.acme.repositories" />

</beans>
```

Using the `Transport Client` or `Rest Client` element registers an instance of `Elasticsearch Server` in the context.

Example 4. Transport Client using Namespace

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:elasticsearch="http://www.springframework.org/schema/data/elasticsearch"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
       https://www.springframework.org/schema/beans/spring-beans-3.1.xsd
       http://www.springframework.org/schema/data/elasticsearch
       https://www.springframework.org/schema/data/elasticsearch/spring-elasticsearch-1.0.xsd">

  <elasticsearch:transport-client id="client" cluster-nodes="localhost:9300,someip:9300" />

</beans>
```

Example 5. Rest Client using Namespace

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:elasticsearch="http://www.springframework.org/schema/data/elasticsearch"
       xsi:schemaLocation="http://www.springframework.org/schema/data/elasticsearch
       https://www.springframework.org/schema/data/elasticsearch/spring-elasticsearch.xsd
       http://www.springframework.org/schema/beans
       https://www.springframework.org/schema/beans/spring-beans.xsd">

  <elasticsearch:rest-client id="restClient" hosts="http://localhost:9200">

</beans>
```

---

<a id="elasticsearch-repositories-reactive-elasticsearch-repositories"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/repositories/reactive-elasticsearch-repositories.html -->

<!-- page_index: 31 -->

# Reactive Elasticsearch Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-repositories-reactive-elasticsearch-repositories--page-title"></a>
<a id="elasticsearch-repositories-reactive-elasticsearch-repositories--reactive-elasticsearch-repositories"></a>

# Reactive Elasticsearch Repositories

Reactive Elasticsearch repository support builds on the core repository support explained in [Repositories](#repositories) utilizing operations provided via [Reactive Elasticsearch Operations](#elasticsearch-reactive-template) executed by a [Reactive REST Client](#elasticsearch-clients--elasticsearch.clients.reactiverestclient).

Spring Data Elasticsearch reactive repository support uses [Project Reactor](https://projectreactor.io/) as its reactive composition library of choice.

There are 3 main interfaces to be used:

- `ReactiveRepository`
- `ReactiveCrudRepository`
- `ReactiveSortingRepository`

<a id="elasticsearch-repositories-reactive-elasticsearch-repositories--elasticsearch.reactive.repositories.usage"></a>
<a id="elasticsearch-repositories-reactive-elasticsearch-repositories--usage"></a>

## Usage

To access domain objects stored in a Elasticsearch using a `Repository`, just create an interface for it.
Before you can actually go on and do that you will need an entity.

Example 1. Sample `Person` entity

```java
public class Person {

  @Id
  private String id;
  private String firstname;
  private String lastname;
  private Address address;

  // … getters and setters omitted
}
```

> [!NOTE]
> Please note that the `id` property needs to be of type `String`.

Example 2. Basic repository interface to persist Person entities

```none
interface ReactivePersonRepository extends ReactiveSortingRepository<Person, String> {

  Flux<Person> findByFirstname(String firstname);                                   (1)

  Flux<Person> findByFirstname(Publisher<String> firstname);                        (2)

  Flux<Person> findByFirstnameOrderByLastname(String firstname);                    (3)

  Flux<Person> findByFirstname(String firstname, Sort sort);                        (4)

  Flux<Person> findByFirstname(String firstname, Pageable page);                    (5)

  Mono<Person> findByFirstnameAndLastname(String firstname, String lastname);       (6)

  Mono<Person> findFirstByLastname(String lastname);                                (7)

  @Query("{ \"bool\" : { \"must\" : { \"term\" : { \"lastname\" : \"?0\" } } } }")
  Flux<Person> findByLastname(String lastname);                                     (8)

  Mono<Long> countByFirstname(String firstname)                                     (9)

  Mono<Boolean> existsByFirstname(String firstname)                                 (10)

  Mono<Long> deleteByFirstname(String firstname)                                    (11)
}
```

| **1** | The method shows a query for all people with the given `lastname`. |
| --- | --- |
| **2** | Finder method awaiting input from `Publisher` to bind parameter value for `firstname`. |
| **3** | Finder method ordering matching documents by `lastname`. |
| **4** | Finder method ordering matching documents by the expression defined via the `Sort` parameter. |
| **5** | Use `Pageable` to pass offset and sorting parameters to the database. |
| **6** | Finder method concating criteria using `And` / `Or` keywords. |
| **7** | Find the first matching entity. |
| **8** | The method shows a query for all people with the given `lastname` looked up by running the annotated `@Query` with given parameters. |
| **9** | Count all entities with matching `firstname`. |
| **10** | Check if at least one entity with matching `firstname` exists. |
| **11** | Delete all entities with matching `firstname`. |

<a id="elasticsearch-repositories-reactive-elasticsearch-repositories--elasticsearch.reactive.repositories.configuration"></a>
<a id="elasticsearch-repositories-reactive-elasticsearch-repositories--configuration"></a>

## Configuration

For Java configuration, use the `@EnableReactiveElasticsearchRepositories` annotation. If no base package is configured, the infrastructure scans the package of the annotated configuration class.

The following listing shows how to use Java configuration for a repository:

Example 3. Java configuration for repositories

```java
@Configuration @EnableReactiveElasticsearchRepositories public class Config extends AbstractReactiveElasticsearchConfiguration {
@Override public ReactiveElasticsearchClient reactiveElasticsearchClient() {return ReactiveRestClients.create(ClientConfiguration.localhost());}}
```

Because the repository from the previous example extends `ReactiveSortingRepository`, all CRUD operations are available
as well as methods for sorted access to the entities. Working with the repository instance is a matter of dependency
injecting it into a client, as the following example shows:

Example 4. Sorted access to Person entities

```java
public class PersonRepositoryTests {
@Autowired ReactivePersonRepository repository;
@Test public void sortsElementsCorrectly() {
Flux<Person> persons = repository.findAll(Sort.by(new Order(ASC, "lastname")));
// ...}}
```

---

<a id="repositories-create-instances"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/create-instances.html -->

<!-- page_index: 32 -->

# Creating Repository Instances

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-create-instances--page-title"></a>
<a id="repositories-create-instances--creating-repository-instances"></a>

# Creating Repository Instances

This section covers how to create instances and bean definitions for the defined repository interfaces.

<a id="repositories-create-instances--repositories.create-instances.java-config"></a>
<a id="repositories-create-instances--java-configuration"></a>

## Java Configuration

Use the store-specific `@EnableElasticsearchRepositories` annotation on a Java configuration class to define a configuration for repository activation.
For an introduction to Java-based configuration of the Spring container, see [JavaConfig in the Spring reference documentation](https://docs.spring.io/spring-framework/reference/7.0/core/beans/java.html).

A sample configuration to enable Spring Data repositories resembles the following:

Sample annotation-based repository configuration

```java
@Configuration @EnableJpaRepositories("com.acme.repositories") class ApplicationConfiguration {
@Bean EntityManagerFactory entityManagerFactory() {// …}}
```

> [!NOTE]
> The preceding example uses the JPA-specific annotation, which you would change according to the store module you actually use. The same applies to the definition of the `EntityManagerFactory` bean. See the sections covering the store-specific configuration.

<a id="repositories-create-instances--repositories.create-instances.java-config.placeholders-and-patterns"></a>
<a id="repositories-create-instances--property-placeholders-and-ant-style-patterns"></a>

### Property Placeholders and Ant-style Patterns

The `basePackages` and `value` attributes in `@EnableElasticsearchRepositories` support `${…}` property placeholders which are resolved against the `Environment` as well as Ant-style package patterns such as `"org.example.**"`.

The following example specifies the `app.scan.packages` property placeholder for the implicit `value` attribute in `@EnableElasticsearchRepositories`.

- Java
- Kotlin

```java
@Configuration
@EnableElasticsearchRepositories("${app.scan.packages}")    (1)
public class ApplicationConfiguration {
  // …
}
```

**1**

`app.scan.packages` property placeholder to be resolved against the `Environment`

```kotlin
@EnableElasticsearchRepositories(["\${app.scan.packages}"]) (1)
class ApplicationConfiguration {
  // …
}
```

**1**

`app.scan.packages` property placeholder to be resolved against the `Environment`

<a id="repositories-create-instances--repositories.create-instances.xml"></a>
<a id="repositories-create-instances--xml-configuration"></a>

## XML Configuration

Each Spring Data module includes a `repositories` element that lets you define a base package that Spring scans for you, as shown in the following example:

Enabling Spring Data repositories via XML

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans:beans xmlns:beans="http://www.springframework.org/schema/beans"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xmlns="http://www.springframework.org/schema/data/jpa"
  xsi:schemaLocation="http://www.springframework.org/schema/beans
    https://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/data/jpa
    https://www.springframework.org/schema/data/jpa/spring-jpa.xsd">

  <jpa:repositories base-package="com.acme.repositories" />

</beans:beans>
```

In the preceding example, Spring is instructed to scan `com.acme.repositories` and all its sub-packages for interfaces extending `Repository` or one of its sub-interfaces.
For each interface found, the infrastructure registers the persistence technology-specific `FactoryBean` to create the appropriate proxies that handle invocations of the query methods.
Each bean is registered under a bean name that is derived from the interface name, so an interface of `UserRepository` would be registered under `userRepository`.
Bean names for nested repository interfaces are prefixed with their enclosing type name.
The base package attribute allows wildcards so that you can define a pattern of scanned packages.

<a id="repositories-create-instances--repositories.using-filters"></a>
<a id="repositories-create-instances--using-filters"></a>

## Using Filters

By default, the infrastructure picks up every interface that extends the persistence technology-specific `Repository` sub-interface located under the configured base package and creates a bean instance for it.
However, you might want more fine-grained control over which interfaces have bean instances created for them.
To do so, use filter elements inside the repository declaration.
The semantics are exactly equivalent to the elements in Spring’s component filters.
For details, see the [Spring reference documentation](https://docs.spring.io/spring-framework/reference/7.0/core/beans/classpath-scanning.html) for these elements.

For example, to exclude certain interfaces from instantiation as repository beans, you could use the following configuration:

Using filters

- Java
- XML

```java
@Configuration
@EnableElasticsearchRepositories(basePackages = "com.acme.repositories",
    includeFilters = { @Filter(type = FilterType.REGEX, pattern = ".*SomeRepository") },
    excludeFilters = { @Filter(type = FilterType.REGEX, pattern = ".*SomeOtherRepository") })
class ApplicationConfiguration {

  @Bean
  EntityManagerFactory entityManagerFactory() {
    // …
  }
}
```

```xml
<repositories base-package="com.acme.repositories">
  <context:include-filter type="regex" expression=".*SomeRepository" />
  <context:exclude-filter type="regex" expression=".*SomeOtherRepository" />
</repositories>
```

The preceding example includes all interfaces ending with `SomeRepository` and excludes those ending with `SomeOtherRepository` from being instantiated.

<a id="repositories-create-instances--repositories.create-instances.standalone"></a>
<a id="repositories-create-instances--standalone-usage"></a>

## Standalone Usage

You can also use the repository infrastructure outside of a Spring container — for example, in CDI environments.You still need some Spring libraries in your classpath, but, generally, you can set up repositories programmatically as well.The Spring Data modules that provide repository support ship with a persistence technology-specific `RepositoryFactory` that you can use, as follows:

Standalone usage of the repository factory

```java
RepositoryFactorySupport factory = … // Instantiate factory here
UserRepository repository = factory.getRepository(UserRepository.class);
```

---

<a id="repositories-query-methods-details"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/query-methods-details.html -->

<!-- page_index: 33 -->

# Defining Query Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-query-methods-details--page-title"></a>
<a id="repositories-query-methods-details--defining-query-methods"></a>

# Defining Query Methods

The repository proxy has two ways to derive a store-specific query from the method name:

- By deriving the query from the method name directly.
- By using a manually defined query.

Available options depend on the actual store.
However, there must be a strategy that decides what actual query is created.
The next section describes the available options.

<a id="repositories-query-methods-details--repositories.query-methods.query-lookup-strategies"></a>
<a id="repositories-query-methods-details--query-lookup-strategies"></a>

## Query Lookup Strategies

The following strategies are available for the repository infrastructure to resolve the query.
With XML configuration, you can configure the strategy at the namespace through the `query-lookup-strategy` attribute.
For Java configuration, you can use the `queryLookupStrategy` attribute of the `EnableElasticsearchRepositories` annotation.
Some strategies may not be supported for particular datastores.

- `CREATE` attempts to construct a store-specific query from the query method name.
  The general approach is to remove a given set of well known prefixes from the method name and parse the rest of the method.
  You can read more about query construction in “[Query Creation](#repositories-query-methods-details--repositories.query-methods.query-creation)”.
- `USE_DECLARED_QUERY` tries to find a declared query and throws an exception if it cannot find one.
  The query can be defined by an annotation somewhere or declared by other means.
  See the documentation of the specific store to find available options for that store.
  If the repository infrastructure does not find a declared query for the method at bootstrap time, it fails.
- `CREATE_IF_NOT_FOUND` (the default) combines `CREATE` and `USE_DECLARED_QUERY`.
  It looks up a declared query first, and, if no declared query is found, it creates a custom method name-based query.
  This is the default lookup strategy and, thus, is used if you do not configure anything explicitly.
  It allows quick query definition by method names but also custom-tuning of these queries by introducing declared queries as needed.

<a id="repositories-query-methods-details--repositories.query-methods.query-creation"></a>
<a id="repositories-query-methods-details--query-creation"></a>

## Query Creation

The query builder mechanism built into the Spring Data repository infrastructure is useful for building constraining queries over entities of the repository.

The following example shows how to create a number of queries:

Query creation from method names

```java
interface PersonRepository extends Repository<Person, Long> {

  List<Person> findByEmailAddressAndLastname(EmailAddress emailAddress, String lastname);

  // Enables the distinct flag for the query
  List<Person> findDistinctPeopleByLastnameOrFirstname(String lastname, String firstname);
  List<Person> findPeopleDistinctByLastnameOrFirstname(String lastname, String firstname);

  // Enabling ignoring case for an individual property
  List<Person> findByLastnameIgnoreCase(String lastname);
  // Enabling ignoring case for all suitable properties
  List<Person> findByLastnameAndFirstnameAllIgnoreCase(String lastname, String firstname);

  // Enabling static ORDER BY for a query
  List<Person> findByLastnameOrderByFirstnameAsc(String lastname);
  List<Person> findByLastnameOrderByFirstnameDesc(String lastname);
}
```

Parsing query method names is divided into subject and predicate.
The first part (`find…By`, `exists…By`) defines the subject of the query, the second part forms the predicate.
The introducing clause (subject) can contain further expressions.
Any text between `find` (or other introducing keywords) and `By` is considered to be descriptive unless using one of the result-limiting keywords such as a `Distinct` to set a distinct flag on the query to be created or [`Top`/`First` to limit query results](#repositories-query-methods-details--repositories.limit-query-result).

The appendix contains the [full list of query method subject keywords](#repositories-query-keywords-reference--appendix.query.method.subject) and [query method predicate keywords including sorting and letter-casing modifiers](#repositories-query-keywords-reference--appendix.query.method.predicate).
However, the first `By` acts as a delimiter to indicate the start of the actual criteria predicate.
At a very basic level, you can define conditions on entity properties and concatenate them with `And` and `Or`.

The actual result of parsing the method depends on the persistence store for which you create the query.
However, there are some general things to notice:

- The expressions are usually property traversals combined with operators that can be concatenated.
  You can combine property expressions with `AND` and `OR`.
  You also get support for operators such as `Between`, `LessThan`, `GreaterThan`, and `Like` for the property expressions.
  The supported operators can vary by datastore, so consult the appropriate part of your reference documentation.
- The method parser supports setting an `IgnoreCase` flag for individual properties (for example, `findByLastnameIgnoreCase(…)`) or for all properties of a type that supports ignoring case (usually `String` instances — for example, `findByLastnameAndFirstnameAllIgnoreCase(…)`).
  Whether ignoring cases is supported may vary by store, so consult the relevant sections in the reference documentation for the store-specific query method.
- You can apply static ordering by appending an `OrderBy` clause to the query method that references a property and by providing a sorting direction (`Asc` or `Desc`).
  To create a query method that supports dynamic sorting, see “[Paging, Iterating Large Results, Sorting & Limiting](#repositories-query-methods-details--repositories.special-parameters)”.

<a id="repositories-query-methods-details--repositories.query-methods.reserved-methods"></a>
<a id="repositories-query-methods-details--reserved-method-names"></a>

## Reserved Method Names

While derived repository methods bind to properties by name, there are a few exceptions to this rule when it comes to certain method names inherited from the base repository targeting the *identifier* property.
Those *reserved methods* like `CrudRepository#findById` (or just `findById`) are targeting the *identifier* property regardless of the actual property name used in the declared method.

Consider the following domain type holding a property `pk` marked as the identifier via `@Id` and a property called `id`.
In this case you need to pay close attention to the naming of your lookup methods as they may collide with predefined signatures:

```java
class User {
  @Id Long pk;                          (1)

  Long id;                              (2)

  // …
}

interface UserRepository extends Repository<User, Long> {

  Optional<User> findById(Long id);     (3)

  Optional<User> findByPk(Long pk);     (4)

  Optional<User> findUserById(Long id); (5)
}
```

| **1** | The identifier property (primary key). |
| --- | --- |
| **2** | A property named `id`, but not the identifier. |
| **3** | Targets the `pk` property (the one marked with `@Id` which is considered to be the identifier) as it refers to a `CrudRepository` base repository method. Therefore, it is not a derived query using of `id` as the property name would suggest because it is one of the *reserved methods*. |
| **4** | Targets the `pk` property by name as it is a derived query. |
| **5** | Targets the `id` property by using the descriptive token between `find` and `by` to avoid collisions with *reserved methods*. |

This special behaviour not only targets lookup methods but also applies to the `exists` and `delete` ones.
Please refer to the “[Repository query keywords](#repositories-query-keywords-reference--appendix.query.method.reserved)” for the list of methods.

<a id="repositories-query-methods-details--repositories.query-methods.query-property-expressions"></a>
<a id="repositories-query-methods-details--property-expressions"></a>

## Property Expressions

Property expressions can refer only to a direct property of the managed entity, as shown in the preceding example.
At query creation time, you already make sure that the parsed property is a property of the managed domain class.
However, you can also define constraints by traversing nested properties.
Consider the following method signature:

```java
List<Person> findByAddressZipCode(ZipCode zipCode);
```

Assume a `Person` has an `Address` with a `ZipCode`.
In that case, the method creates the `x.address.zipCode` property traversal.
The resolution algorithm starts by interpreting the entire part (`AddressZipCode`) as the property and checks the domain class for a property with that name (uncapitalized).
If the algorithm succeeds, it uses that property.
If not, the algorithm splits up the source at the camel-case parts from the right side into a head and a tail and tries to find the corresponding property — in our example, `AddressZip` and `Code`.
If the algorithm finds a property with that head, it takes the tail and continues building the tree down from there, splitting the tail up in the way just described.
If the first split does not match, the algorithm moves the split point to the left (`Address`, `ZipCode`) and continues.

Although this should work for most cases, it is possible for the algorithm to select the wrong property.
Suppose the `Person` class has an `addressZip` property as well.
The algorithm would match in the first split round already, choose the wrong property, and fail (as the type of `addressZip` probably has no `code` property).

To resolve this ambiguity you can use `_` inside your method name to manually define traversal points.
So our method name would be as follows:

```java
List<Person> findByAddress_ZipCode(ZipCode zipCode);
```

> [!NOTE]
> Because we treat underscores (`_`) as a reserved character, we strongly advise to follow standard Java naming conventions (that is, not using underscores in property names but applying camel case instead).

> [!WARNING]
> Field Names starting with underscore:
>
> Field names may start with underscores like `String _name`.
> Make sure to preserve the `_` as in `_name` and use double `_` to split nested paths like `user__name`.
>
> Upper Case Field Names:
>
> Field names that are all uppercase can be used as such.
> Nested paths if applicable require splitting via `_` as in `USER_name`.
>
> Field Names with 2nd uppercase letter:
>
> Field names that consist of a starting lower case letter followed by an uppercase one like `String qCode` can be resolved by starting with two upper case letters as in `QCode`.
> Please be aware of potential path ambiguities.
>
> Path Ambiguities:
>
> In the following sample the arrangement of properties `qCode` and `q`, with `q` containing a property called `code`, creates an ambiguity for the path `QCode`.
>
> ```java
> record Container(String qCode, Code q) {}
> record Code(String code) {}
> ```
>
> Since a direct match on a property is considered first, any potential nested paths will not be considered and the algorithm picks the `qCode` field.
> In order to select the `code` field in `q` the underscore notation `Q_Code` is required.

<a id="repositories-query-methods-details--repositories.collections-and-iterables"></a>
<a id="repositories-query-methods-details--repository-methods-returning-collections-or-iterables"></a>

## Repository Methods Returning Collections or Iterables

Query methods that return multiple results can use standard Java `Iterable`, `List`, and `Set`.
Beyond that, we support returning Spring Data’s `Streamable`, a custom extension of `Iterable`, as well as collection types provided by [Vavr](https://www.vavr.io/).
Refer to the appendix explaining all possible [query method return types](#repositories-query-return-types-reference--appendix.query.return.types).

<a id="repositories-query-methods-details--repositories.collections-and-iterables.streamable"></a>
<a id="repositories-query-methods-details--using-streamable-as-query-method-return-type"></a>

### Using Streamable as Query Method Return Type

You can use `Streamable` as alternative to `Iterable` or any collection type.
It provides convenience methods to access a non-parallel `Stream` (missing from `Iterable`) and the ability to directly `….filter(…)` and `….map(…)` over the elements and concatenate the `Streamable` to others:

Using Streamable to combine query method results

```java
interface PersonRepository extends Repository<Person, Long> {
  Streamable<Person> findByFirstnameContaining(String firstname);
  Streamable<Person> findByLastnameContaining(String lastname);
}

Streamable<Person> result = repository.findByFirstnameContaining("av")
  .and(repository.findByLastnameContaining("ea"));
```

<a id="repositories-query-methods-details--repositories.collections-and-iterables.streamable-wrapper"></a>
<a id="repositories-query-methods-details--returning-custom-streamable-wrapper-types"></a>

### Returning Custom Streamable Wrapper Types

Providing dedicated wrapper types for collections is a commonly used pattern to provide an API for a query result that returns multiple elements.
Usually, these types are used by invoking a repository method returning a collection-like type and creating an instance of the wrapper type manually.
You can avoid that additional step as Spring Data lets you use these wrapper types as query method return types if they meet the following criteria:

1. The type implements `Streamable`.
2. The type exposes either a constructor or a static factory method named `of(…)` or `valueOf(…)` that takes `Streamable` as an argument.

The following listing shows an example:

```java
class Product {                                         (1) MonetaryAmount getPrice() { … }}
@RequiredArgsConstructor(staticName = "of") class Products implements Streamable<Product> {         (2)
private final Streamable<Product> streamable;
public MonetaryAmount getTotal() {                    (3) return streamable.stream() .map(Product::getPrice) .reduce(Money.of(0), MonetaryAmount::add);}
@Override public Iterator<Product> iterator() {                 (4) return streamable.iterator();}}
interface ProductRepository extends Repository<Product, Long> {Products findAllByDescriptionContaining(String text); (5)}
```

| **1** | A `Product` entity that exposes API to access the product’s price. |
| --- | --- |
| **2** | A wrapper type for a `Streamable<Product>` that can be constructed by using `Products.of(…)` (factory method created with the Lombok annotation). A standard constructor taking the `Streamable<Product>` will do as well. |
| **3** | The wrapper type exposes an additional API, calculating new values on the `Streamable<Product>`. |
| **4** | Implement the `Streamable` interface and delegate to the actual result. |
| **5** | That wrapper type `Products` can be used directly as a query method return type. You do not need to return `Streamable<Product>` and manually wrap it after the query in the repository client. |

<a id="repositories-query-methods-details--repositories.collections-and-iterables.vavr"></a>
<a id="repositories-query-methods-details--support-for-vavr-collections"></a>

### Support for Vavr Collections

[Vavr](https://www.vavr.io/) is a library that embraces functional programming concepts in Java.
It ships with a custom set of collection types that you can use as query method return types, as the following table shows:

| Vavr collection type | Used Vavr implementation type | Valid Java source types |
| --- | --- | --- |
| `io.vavr.collection.Seq` | `io.vavr.collection.List` | `java.util.Iterable` |
| `io.vavr.collection.Set` | `io.vavr.collection.LinkedHashSet` | `java.util.Iterable` |
| `io.vavr.collection.Map` | `io.vavr.collection.LinkedHashMap` | `java.util.Map` |

You can use the types in the first column (or subtypes thereof) as query method return types and get the types in the second column used as implementation type, depending on the Java type of the actual query result (third column).
Alternatively, you can declare `Traversable` (the Vavr `Iterable` equivalent), and we then derive the implementation class from the actual return value.
That is, a `java.util.List` is turned into a Vavr `List` or `Seq`, a `java.util.Set` becomes a Vavr `LinkedHashSet` `Set`, and so on.

<a id="repositories-query-methods-details--repositories.query-streaming"></a>
<a id="repositories-query-methods-details--streaming-query-results"></a>

## Streaming Query Results

You can process the results of query methods incrementally by using a `Stream<T>` as the return type.
Instead of wrapping the query results in a `Stream`, data store-specific methods are used to perform the streaming, as shown in the following example:

Stream the result of a query with Java 8 `Stream<T>`

```java
@Query("select u from User u")
Stream<User> findAllByCustomQueryAndStream();

Stream<User> readAllByFirstnameNotNull();

@Query("select u from User u")
Stream<User> streamAllPaged(Pageable pageable);
```

> [!NOTE]
> A `Stream` potentially wraps underlying data store-specific resources and must, therefore, be closed after usage.
> You can either manually close the `Stream` by using the `close()` method or by using a `try`-with-resources block, as shown in the following example:

Working with a `Stream<T>` result in a `try-with-resources` block

```java
try (Stream<User> stream = repository.findAllByCustomQueryAndStream()) {
  stream.forEach(…);
}
```

> [!NOTE]
> Not all Spring Data modules currently support `Stream<T>` as a return type.

<a id="repositories-query-methods-details--repositories.query-async"></a>
<a id="repositories-query-methods-details--asynchronous-query-results"></a>

## Asynchronous Query Results

You can run repository queries asynchronously by using [Spring’s asynchronous method running capability](https://docs.spring.io/spring-framework/reference/7.0/integration/scheduling.html).
This means the method returns immediately upon invocation while the actual query occurs in a task that has been submitted to a Spring `TaskExecutor`.
Asynchronous queries differ from reactive queries and should not be mixed.
See the store-specific documentation for more details on reactive support.
The following example shows a number of asynchronous queries:

```java
@Async
Future<User> findByFirstname(String firstname);               (1)

@Async
CompletableFuture<User> findOneByFirstname(String firstname); (2)
```

**1**

Use `java.util.concurrent.Future` as the return type.

**2**

Use `java.util.concurrent.CompletableFuture` as the return type.

<a id="repositories-query-methods-details--repositories.special-parameters"></a>
<a id="repositories-query-methods-details--paging-iterating-large-results-sorting-limiting"></a>

## Paging, Iterating Large Results, Sorting & Limiting

To handle parameters in your query, define method parameters as already seen in the preceding examples.
Besides that, the infrastructure recognizes certain specific types like `Pageable`, `Sort` and `Limit`, to apply pagination, sorting and limiting to your queries dynamically.
The following example demonstrates these features:

Using `Pageable`, `Slice`, `Sort` and `Limit` in query methods

```java
Page<User> findByLastname(String lastname, Pageable pageable);

Slice<User> findByLastname(String lastname, Pageable pageable);

List<User> findByLastname(String lastname, Sort sort);

List<User> findByLastname(String lastname, Sort sort, Limit limit);

List<User> findByLastname(String lastname, Pageable pageable);
```

> [!IMPORTANT]
> APIs taking `Sort`, `Pageable` and `Limit` expect non-`null` values to be handed into methods.
> If you do not want to apply any sorting or pagination, use `Sort.unsorted()`, `Pageable.unpaged()` and `Limit.unlimited()`.

The first method lets you pass an `org.springframework.data.domain.Pageable` instance to the query method to dynamically add paging to your statically defined query.
A `Page` knows about the total number of elements and pages available.
It does so by the infrastructure triggering a count query to calculate the overall number.
As this might be expensive (depending on the store used), you can instead return a `Slice`.
A `Slice` knows only about whether a next `Slice` is available, which might be sufficient when walking through a larger result set.

Sorting options are handled through the `Pageable` instance, too.
If you need only sorting, add an `org.springframework.data.domain.Sort` parameter to your method.
As you can see, returning a `List` is also possible.
In this case, the additional metadata required to build the actual `Page` instance is not created (which, in turn, means that the additional count query that would have been necessary is not issued).
Rather, it restricts the query to look up only the given range of entities.

> [!NOTE]
> To find out how many pages you get for an entire query, you have to trigger an additional count query.
> By default, this query is derived from the query you actually trigger.

> [!IMPORTANT]
> Special parameters may only be used once within a query method.
> Some special parameters described above are mutually exclusive.
> Please consider the following list of invalid parameter combinations.
>
> | Parameters | Example | Reason |
> | --- | --- | --- |
> | `Pageable` and `Sort` | `findBy…(Pageable page, Sort sort)` | `Pageable` already defines `Sort` |
> | `Pageable` and `Limit` | `findBy…(Pageable page, Limit limit)` | `Pageable` already defines a limit. |
>
> The `Top` keyword can be used together with `Pageable`: `Top` defines the total maximum number of results, while the `Pageable` parameter may reduce this number further.

<a id="repositories-query-methods-details--repositories.scrolling.guidance"></a>
<a id="repositories-query-methods-details--which-method-is-appropriate"></a>

### Which Method is Appropriate?

The value provided by the Spring Data abstractions is perhaps best shown by the possible query method return types outlined in the following table below.
The table shows which types you can return from a query method

<table class="tableblock frame-all grid-all stretch">
<caption>Table 1. Consuming Large Query Results</caption>
<colgroup>
<col/>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Method</th>
<th>Amount of Data Fetched</th>
<th>Query Structure</th>
<th>Constraints</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><a href="#repositories-query-methods-details--repositories.collections-and-iterables"><code>List&lt;T&gt;</code></a></p></td>
<td><p>All results.</p></td>
<td><p>Single query.</p></td>
<td><p>Query results can exhaust all memory. Fetching all data can be time-intensive.</p></td>
</tr>
<tr>
<td><p><a href="#repositories-query-methods-details--repositories.collections-and-iterables.streamable"><code>Streamable&lt;T&gt;</code></a></p></td>
<td><p>All results.</p></td>
<td><p>Single query.</p></td>
<td><p>Query results can exhaust all memory. Fetching all data can be time-intensive.</p></td>
</tr>
<tr>
<td><p><a href="#repositories-query-methods-details--repositories.query-streaming"><code>Stream&lt;T&gt;</code></a></p></td>
<td><p>Chunked (one-by-one or in batches) depending on <code>Stream</code> consumption.</p></td>
<td><p>Single query using typically cursors.</p></td>
<td><p>Streams must be closed after usage to avoid resource leaks.</p></td>
</tr>
<tr>
<td><p><code>Flux&lt;T&gt;</code></p></td>
<td><p>Chunked (one-by-one or in batches) depending on <code>Flux</code> consumption.</p></td>
<td><p>Single query using typically cursors.</p></td>
<td><p>Store module must provide reactive infrastructure.</p></td>
</tr>
<tr>
<td><p><code>Slice&lt;T&gt;</code></p></td>
<td><p><code>Pageable.getPageSize() + 1</code> at <code>Pageable.getOffset()</code></p></td>
<td><p>One to many queries fetching data starting at <code>Pageable.getOffset()</code> applying limiting.</p></td>
<td><div><div>
<p>A <code>Slice</code> can only navigate to the next <code>Slice</code>.</p>
</div>
<div>
<ul>
<li>
<p><code>Slice</code> provides details whether there is more data to fetch.</p>
</li>
<li>
<p>Offset-based queries becomes inefficient when the offset is too large because the database still has to materialize the full result.</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td><p><code>Page&lt;T&gt;</code></p></td>
<td><p><code>Pageable.getPageSize()</code>  at <code>Pageable.getOffset()</code></p></td>
<td><p>One to many queries starting at <code>Pageable.getOffset()</code> applying limiting. Additionally, <code>COUNT(…)</code> query to determine the total number of elements can be required.</p></td>
<td><div><div>
<p>Often times, <code>COUNT(…)</code> queries are required that are costly.</p>
</div>
<div>
<ul>
<li>
<p>Offset-based queries becomes inefficient when the offset is too large because the database still has to materialize the full result.</p>
</li>
</ul>
</div></div></td>
</tr>
</tbody>
</table>

<a id="repositories-query-methods-details--repositories.paging-and-sorting"></a>
<a id="repositories-query-methods-details--paging-and-sorting"></a>

### Paging and Sorting

You can define simple sorting expressions by using property names.
You can concatenate expressions to collect multiple criteria into one expression.

Defining sort expressions

```java
Sort sort = Sort.by("firstname").ascending()
  .and(Sort.by("lastname").descending());
```

For a more type-safe way to define sort expressions, start with the type for which to define the sort expression and use method references to define the properties on which to sort.

Defining sort expressions by using the type-safe API

```java
TypedSort<Person> person = Sort.sort(Person.class);

Sort sort = person.by(Person::getFirstname).ascending()
  .and(person.by(Person::getLastname).descending());
```

> [!NOTE]
> `TypedSort.by(…)` makes use of runtime proxies by (typically) using CGlib, which may interfere with native image compilation when using tools such as GraalVM Native Image.

If your store implementation supports Querydsl, you can also use the generated metamodel types to define sort expressions:

Defining sort expressions by using the Querydsl API

```java
QSort sort = QSort.by(QPerson.firstname.asc())
  .and(QSort.by(QPerson.lastname.desc()));
```

<a id="repositories-query-methods-details--repositories.limit-query-result"></a>
<a id="repositories-query-methods-details--limiting-query-results"></a>

### Limiting Query Results

In addition to paging it is possible to limit the result size using a dedicated `Limit` parameter.
You can also limit the results of query methods by using the `First` or `Top` keywords, which you can use interchangeably but may not be mixed with a `Limit` parameter.
You can append an optional numeric value to `Top` or `First` to specify the maximum result size to be returned.
If the number is left out, a result size of 1 is assumed.
The following example shows how to limit the query size:

Limiting the result size of a query with `Top` and `First`

```java
List<User> findByLastname(String lastname, Limit limit);

User findFirstByOrderByLastnameAsc();

User findTopByLastnameOrderByAgeDesc(String lastname);

Page<User> queryFirst10ByLastname(String lastname, Pageable pageable);

Slice<User> findTop3By(Pageable pageable);

List<User> findFirst10ByLastname(String lastname, Sort sort);

List<User> findTop10ByLastname(String lastname, Pageable pageable);
```

The limiting expressions also support the `Distinct` keyword for datastores that support distinct queries.
Also, for the queries that limit the result set to one instance, wrapping the result into with the `Optional` keyword is supported.

If pagination or slicing is applied to a limiting query pagination (and the calculation of the number of available pages), it is applied within the limited result.

> [!NOTE]
> Limiting the results in combination with dynamic sorting by using a `Sort` parameter lets you express query methods for the 'K' smallest as well as for the 'K' biggest elements.

---

<a id="elasticsearch-repositories-elasticsearch-repository-queries"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/repositories/elasticsearch-repository-queries.html -->

<!-- page_index: 34 -->

# Query methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-repositories-elasticsearch-repository-queries--page-title"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--query-methods"></a>

# Query methods

<a id="elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.finders"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--query-lookup-strategies"></a>

## Query lookup strategies

The Elasticsearch module supports all basic query building feature as string queries, native search queries, criteria based queries or have it being derived from the method name.

<a id="elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.finders.declared"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--declared-queries"></a>

### Declared queries

Deriving the query from the method name is not always sufficient and/or may result in unreadable method names.
In this case one might make use of the `@Query` annotation (see [Using the @Query Annotation](#elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.at-query) ).

Another possibility is the use of a search-template, (see [Using the @SearchTemplateQuery Annotation](#elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.at-searchtemplate-query) ).

<a id="elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.criterions"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--query-creation"></a>

## Query creation

Generally the query creation mechanism for Elasticsearch works as described in [Defining Query Methods](#repositories-query-methods-details).
Here’s a short example of what a Elasticsearch query method translates into:

Example 1. Query creation from method names

```java
interface BookRepository extends Repository<Book, String> {
  List<Book> findByNameAndPrice(String name, Integer price);
}
```

The method name above will be translated into the following Elasticsearch json query

```none
{"query": {"bool" : {"must" : [{ "query_string" : { "query" : "?", "fields" : [ "name" ] } },{ "query_string" : { "query" : "?", "fields" : [ "price" ] } }]}}}
```

A list of supported keywords for Elasticsearch is shown below.

| Keyword | Sample | Elasticsearch Query String |
| --- | --- | --- |
| `And` | `findByNameAndPrice` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "?", "fields" : [ "name" ] } }, { "query_string" : { "query" : "?", "fields" : [ "price" ] } } ] } }}` |
| `Or` | `findByNameOrPrice` | `{ "query" : { "bool" : { "should" : [ { "query_string" : { "query" : "?", "fields" : [ "name" ] } }, { "query_string" : { "query" : "?", "fields" : [ "price" ] } } ] } }}` |
| `Is` | `findByName` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "?", "fields" : [ "name" ] } } ] } }}` |
| `Not` | `findByNameNot` | `{ "query" : { "bool" : { "must_not" : [ { "query_string" : { "query" : "?", "fields" : [ "name" ] } } ] } }}` |
| `Between` | `findByPriceBetween` | `{ "query" : { "bool" : { "must" : [ {"range" : {"price" : {"from" : ?, "to" : ?, "include_lower" : true, "include_upper" : true } } } ] } }}` |
| `LessThan` | `findByPriceLessThan` | `{ "query" : { "bool" : { "must" : [ {"range" : {"price" : {"from" : null, "to" : ?, "include_lower" : true, "include_upper" : false } } } ] } }}` |
| `LessThanEqual` | `findByPriceLessThanEqual` | `{ "query" : { "bool" : { "must" : [ {"range" : {"price" : {"from" : null, "to" : ?, "include_lower" : true, "include_upper" : true } } } ] } }}` |
| `GreaterThan` | `findByPriceGreaterThan` | `{ "query" : { "bool" : { "must" : [ {"range" : {"price" : {"from" : ?, "to" : null, "include_lower" : false, "include_upper" : true } } } ] } }}` |
| `GreaterThanEqual` | `findByPriceGreaterThanEqual` | `{ "query" : { "bool" : { "must" : [ {"range" : {"price" : {"from" : ?, "to" : null, "include_lower" : true, "include_upper" : true } } } ] } }}` |
| `Before` | `findByPriceBefore` | `{ "query" : { "bool" : { "must" : [ {"range" : {"price" : {"from" : null, "to" : ?, "include_lower" : true, "include_upper" : true } } } ] } }}` |
| `After` | `findByPriceAfter` | `{ "query" : { "bool" : { "must" : [ {"range" : {"price" : {"from" : ?, "to" : null, "include_lower" : true, "include_upper" : true } } } ] } }}` |
| `Like` | `findByNameLike` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "?*", "fields" : [ "name" ] }, "analyze_wildcard": true } ] } }}` |
| `StartingWith` | `findByNameStartingWith` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "?*", "fields" : [ "name" ] }, "analyze_wildcard": true } ] } }}` |
| `EndingWith` | `findByNameEndingWith` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "*?", "fields" : [ "name" ] }, "analyze_wildcard": true } ] } }}` |
| `Contains/Containing` | `findByNameContaining` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "*?*", "fields" : [ "name" ] }, "analyze_wildcard": true } ] } }}` |
| `In` (when annotated as FieldType.Keyword) | `findByNameIn(Collection<String>names)` | `{ "query" : { "bool" : { "must" : [ {"bool" : {"must" : [ {"terms" : {"name" : ["?","?"]}} ] } } ] } }}` |
| `In` | `findByNameIn(Collection<String>names)` | `{ "query": {"bool": {"must": [{"query_string":{"query": "\"?\" \"?\"", "fields": ["name"]}}]}}}` |
| `NotIn` (when annotated as FieldType.Keyword) | `findByNameNotIn(Collection<String>names)` | `{ "query" : { "bool" : { "must" : [ {"bool" : {"must_not" : [ {"terms" : {"name" : ["?","?"]}} ] } } ] } }}` |
| `NotIn` | `findByNameNotIn(Collection<String>names)` | `{"query": {"bool": {"must": [{"query_string": {"query": "NOT(\"?\" \"?\")", "fields": ["name"]}}]}}}` |
| `True` | `findByAvailableTrue` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "true", "fields" : [ "available" ] } } ] } }}` |
| `False` | `findByAvailableFalse` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "false", "fields" : [ "available" ] } } ] } }}` |
| `OrderBy` | `findByAvailableTrueOrderByNameDesc` | `{ "query" : { "bool" : { "must" : [ { "query_string" : { "query" : "true", "fields" : [ "available" ] } } ] } }, "sort":[{"name":{"order":"desc"}}] }` |
| `Exists` | `findByNameExists` | `{"query":{"bool":{"must":[{"exists":{"field":"name"}}]}}}` |
| `IsNull` | `findByNameIsNull` | `{"query":{"bool":{"must_not":[{"exists":{"field":"name"}}]}}}` |
| `IsNotNull` | `findByNameIsNotNull` | `{"query":{"bool":{"must":[{"exists":{"field":"name"}}]}}}` |
| `IsEmpty` | `findByNameIsEmpty` | `{"query":{"bool":{"must":[{"bool":{"must":[{"exists":{"field":"name"}}],"must_not":[{"wildcard":{"name":{"wildcard":"*"}}}]}}]}}}` |
| `IsNotEmpty` | `findByNameIsNotEmpty` | `{"query":{"bool":{"must":[{"wildcard":{"name":{"wildcard":"*"}}}]}}}` |

> [!NOTE]
> Methods names to build Geo-shape queries taking `GeoJson` parameters are not supported.
> Use `ElasticsearchOperations` with `CriteriaQuery` in a custom repository implementation if you need to have such a function in a repository.

<a id="elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.return-types"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--method-return-types"></a>

## Method return types

Repository methods can be defined to have the following return types for returning multiple Elements:

- `List<T>`
- `Stream<T>`
- `SearchHits<T>`
- `List<SearchHit<T>>`
- `Stream<SearchHit<T>>`
- `SearchPage<T>`

<a id="elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.at-query"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--using-the-query-annotation"></a>

## Using the @Query Annotation

Example 2. Declare query on the method using the `@Query` annotation.

The arguments passed to the method can be inserted into placeholders in the query string.
The placeholders are of the form `?0`, `?1`, `?2` etc. for the first, second, third parameter and so on.

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {
    @Query("{\"match\": {\"name\": {\"query\": \"?0\"}}}")
    Page<Book> findByName(String name,Pageable pageable);
}
```

The String that is set as the annotation argument must be a valid Elasticsearch JSON query.
It will be sent to Easticsearch as value of the query element; if for example the function is called with the parameter *John*, it would produce the following query body:

```json
{"query": {"match": {"name": {"query": "John"}}}}
```

Example 3. `@Query` annotation on a method taking a Collection argument

A repository method such as

```java
@Query("{\"ids\": {\"values\": ?0 }}")
List<SampleEntity> getByIds(Collection<String> ids);
```

would make an [IDs query](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-ids-query.html) to return all the matching documents.
So calling the method with a `List` of `["id1", "id2", "id3"]` would produce the query body

```json
{
  "query": {
    "ids": {
      "values": ["id1", "id2", "id3"]
    }
  }
}
```

<a id="elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.at-query.spel"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--using-spel-expressions"></a>

### Using SpEL Expressions

Example 4. Declare query on the method using the `@Query` annotation with SpEL expression.

[SpEL expression](https://docs.spring.io/spring-framework/reference/7.0/core/expressions.html) is also supported when defining query in `@Query`.

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {@Query(""" {"bool":{"must":[{"term":{"name": "#{#name}"}}]}} """) Page<Book> findByName(String name, Pageable pageable);}
```

If for example the function is called with the parameter *John*, it would produce the following query body:

```json
{
  "bool":{
    "must":[
      {
        "term":{
          "name": "John"
        }
      }
    ]
  }
}
```

Example 5. accessing parameter property.

Supposing that we have the following class as query parameter type:

```java
public record QueryParameter(String value) {
}
```

It’s easy to access the parameter by `#` symbol, then reference the property `value` with a simple `.`:

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {@Query(""" {"bool":{"must":[{"term":{"name": "#{#parameter.value}"}}]}} """) Page<Book> findByName(QueryParameter parameter, Pageable pageable);}
```

We can pass `new QueryParameter("John")` as the parameter now, and it will produce the same query string as above.

Example 6. accessing bean property.

[Bean property](https://docs.spring.io/spring-framework/reference/7.0/core/expressions/language-ref/bean-references.html) is also supported to access.
Given that there is a bean named `queryParameter` of type `QueryParameter`, we can access the bean with symbol `@` rather than `#`, and there is no need to declare a parameter of type `QueryParameter` in the query method:

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {
    @Query("""
            {
              "bool":{
                "must":[
                  {
                    "term":{
                      "name": "#{@queryParameter.value}"
                    }
                  }
                ]
              }
            }
            """)
    Page<Book> findByName(Pageable pageable);
}
```

Example 7. SpEL and `Collection` param.

`Collection` parameter is also supported and is as easy to use as normal `String`, such as the following `terms` query:

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {@Query(""" {"bool":{"must":[{"terms":{"name": #{#names}}}]}} """) Page<Book> findByName(Collection<String> names, Pageable pageable);}
```

> [!NOTE]
> collection values should not be quoted when declaring the elasticsearch json query.

A collection of `names` like `List.of("name1", "name2")` will produce the following terms query:

```json
{"bool":{"must":[{"terms":{"name": ["name1", "name2"]}}]}}
```

Example 8. access property in the `Collection` param.

[SpEL Collection Projection](https://docs.spring.io/spring-framework/reference/7.0/core/expressions/language-ref/collection-projection.html) is convenient to use when values in the `Collection` parameter is not plain `String`:

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {@Query(""" {"bool":{"must":[{"terms":{"name": #{#parameters.![value]}}}]}} """) Page<Book> findByName(Collection<QueryParameter> parameters, Pageable pageable);}
```

This will extract all the `value` property values as a new `Collection` from `QueryParameter` collection, thus takes the same effect as above.

Example 9. alter parameter name by using `@Param`

When accessing the parameter by SpEL, it’s also useful to alter the parameter name to another one by `@Param` annotation in Sping Data:

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {@Query(""" {"bool":{"must":[{"terms":{"name": #{#another.![value]}}}]}} """) Page<Book> findByName(@Param("another") Collection<QueryParameter> parameters, Pageable pageable);}
```

<a id="elasticsearch-repositories-elasticsearch-repository-queries--elasticsearch.query-methods.at-searchtemplate-query"></a>
<a id="elasticsearch-repositories-elasticsearch-repository-queries--using-the-searchtemplatequery-annotation"></a>

## Using the @SearchTemplateQuery Annotation

When using Elasticsearch search templates - (see [Search Template support](#elasticsearch-misc--elasticsearch.misc.searchtemplates)) it is possible to specify that a repository method should use a template by adding the `@SearchTemplateQuery` annotation to that method.

Let’s assume that there is a search template stored with the name "book-by-title" and this template need a parameter named "title", then a repository method using that search template can be defined like this:

```java
interface BookRepository extends ElasticsearchRepository<Book, String> {
    @SearchTemplateQuery(id = "book-by-title")
    SearchHits<Book> findByTitle(String title);
}
```

The parameters of the repository method are sent to the seacrh template as key/value pairs where the key is the parameter name and the value is taken from the actual value when the method is invoked.

---

<a id="repositories-projections"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/projections.html -->

<!-- page_index: 35 -->

# Projections

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-projections--page-title"></a>
<a id="repositories-projections--projections"></a>

# Projections

<a id="repositories-projections--elasticsearch.projections.limitations"></a>
<a id="repositories-projections--spring-data-elasticsearch-projection-limitations"></a>

## Spring Data Elasticsearch Projection Limitations

This chapter is pulled in from the Spring Data Commons documentation, but does not apply to Spring Data Elasticsearch.

> [!IMPORTANT]
> Interface-based projections are not supported in Spring Data Elasticsearch repository query methods.

To limit the fields returned from Elasticsearch, use the [`@SourceFilters`](#elasticsearch-repositories-elasticsearch-repositories--elasticsearch.repositories.annotations.sourcefilters) annotation on your repository methods instead.

<a id="repositories-projections--projections-2"></a>

## Projections

Spring Data query methods usually return one or multiple instances of the aggregate root managed by the repository.
However, it might sometimes be desirable to create projections based on certain attributes of those types.
Spring Data allows modeling dedicated return types, to more selectively retrieve partial views of the managed aggregates.

Imagine a repository and aggregate root type such as the following example:

A sample aggregate and repository

```java
class Person {
@Id UUID id; String firstname, lastname; Address address;
static class Address {String zipCode, city, street;}}
interface PersonRepository extends Repository<Person, UUID> {
Collection<Person> findByLastname(String lastname);}
```

Now imagine that we want to retrieve the person’s name attributes only.
What means does Spring Data offer to achieve this?
The rest of this chapter answers that question.

> [!NOTE]
> Projection types are types residing outside the entity’s type hierarchy.
> Superclasses and interfaces implemented by the entity are inside the type hierarchy hence returning a supertype (or implemented interface) returns an instance of the fully materialized entity.

<a id="repositories-projections--projections.interfaces"></a>
<a id="repositories-projections--interface-based-projections"></a>

## Interface-based Projections

The easiest way to limit the result of the queries to only the name attributes is by declaring an interface that exposes accessor methods for the properties to be read, as shown in the following example:

A projection interface to retrieve a subset of attributes

```java
interface NamesOnly {

  String getFirstname();
  String getLastname();
}
```

The important bit here is that the properties defined here exactly match properties in the aggregate root.
Doing so lets a query method be added as follows:

A repository using an interface based projection with a query method

```java
interface PersonRepository extends Repository<Person, UUID> {

  Collection<NamesOnly> findByLastname(String lastname);
}
```

The query execution engine creates proxy instances of that interface at runtime for each element returned and forwards calls to the exposed methods to the target object.

> [!NOTE]
> Declaring a method in your `Repository` that overrides a base method (e.g. declared in `CrudRepository`, a store-specific repository interface, or the `Simple…Repository`) results in a call to the base method regardless of the declared return type.
> Make sure to use a compatible return type as base methods cannot be used for projections.
> Some store modules support `@Query` annotations to turn an overridden base method into a query method that then can be used to return projections.

Projections can be used recursively.
If you want to include some of the `Address` information as well, create a projection interface for that and return that interface from the declaration of `getAddress()`, as shown in the following example:

A projection interface to retrieve a subset of attributes

```java
interface PersonSummary {
String getFirstname(); String getLastname(); AddressSummary getAddress();
interface AddressSummary {String getCity();}}
```

On method invocation, the `address` property of the target instance is obtained and wrapped into a projecting proxy in turn.

<a id="repositories-projections--projections.interfaces.closed"></a>
<a id="repositories-projections--closed-projections"></a>

### Closed Projections

A projection interface whose accessor methods all match properties of the target aggregate is considered to be a closed projection.
The following example (which we used earlier in this chapter, too) is a closed projection:

A closed projection

```java
interface NamesOnly {

  String getFirstname();
  String getLastname();
}
```

If you use a closed projection, Spring Data can optimize the query execution, because we know about all the attributes that are needed to back the projection proxy.
For more details on that, see the module-specific part of the reference documentation.

<a id="repositories-projections--projections.interfaces.open"></a>
<a id="repositories-projections--open-projections"></a>

### Open Projections

Accessor methods in projection interfaces can also be used to compute new values by using the `@Value` annotation, as shown in the following example:

An Open Projection

```java
interface NamesOnly {

  @Value("#{target.firstname + ' ' + target.lastname}")
  String getFullName();
  …
}
```

The aggregate root backing the projection is available in the `target` variable.
A projection interface using `@Value` is an open projection.
Spring Data cannot apply query execution optimizations in this case, because the SpEL expression could use any attribute of the aggregate root.

The expressions used in `@Value` should not be too complex — you want to avoid programming in `String` variables.
For very simple expressions, one option might be to resort to default methods (introduced in Java 8), as shown in the following example:

A projection interface using a default method for custom logic

```java
interface NamesOnly {
String getFirstname(); String getLastname();
default String getFullName() {return getFirstname().concat(" ").concat(getLastname());}}
```

This approach requires you to be able to implement logic purely based on the other accessor methods exposed on the projection interface.
A second, more flexible, option is to implement the custom logic in a Spring bean and then invoke that from the SpEL expression, as shown in the following example:

Sample Person object

```java
@Component class MyBean {
String getFullName(Person person) {…}}
interface NamesOnly {
@Value("#{@myBean.getFullName(target)}") String getFullName(); …}
```

Notice how the SpEL expression refers to `myBean` and invokes the `getFullName(…)` method and forwards the projection target as a method parameter.
Methods backed by SpEL expression evaluation can also use method parameters, which can then be referred to from the expression.
The method parameters are available through an `Object` array named `args`.
The following example shows how to get a method parameter from the `args` array:

Sample Person object

```java
interface NamesOnly {

  @Value("#{args[0] + ' ' + target.firstname + '!'}")
  String getSalutation(String prefix);
}
```

Again, for more complex expressions, you should use a Spring bean and let the expression invoke a method, as described [earlier](#repositories-projections--projections.interfaces.open.bean-reference).

<a id="repositories-projections--projections.interfaces.nullable-wrappers"></a>
<a id="repositories-projections--nullable-wrappers"></a>

### Nullable Wrappers

Getters in projection interfaces can make use of nullable wrappers for improved null-safety.
Currently supported wrapper types are:

- `java.util.Optional`
- `com.google.common.base.Optional`
- `scala.Option`
- `io.vavr.control.Option`

A projection interface using nullable wrappers

```java
interface NamesOnly {

  Optional<String> getFirstname();
}
```

If the underlying projection value is not `null`, then values are returned using the present-representation of the wrapper type.
In case the backing value is `null`, then the getter method returns the empty representation of the used wrapper type.

<a id="repositories-projections--projections.dtos"></a>
<a id="repositories-projections--class-based-projections-dtos"></a>

## Class-based Projections (DTOs)

Another way of defining projections is by using value type DTOs (Data Transfer Objects) that hold properties for the fields that are supposed to be retrieved.
These DTO types can be used in exactly the same way projection interfaces are used, except that no proxying happens and no nested projections can be applied.

If the store optimizes the query execution by limiting the fields to be loaded, the fields to be loaded are determined from the parameter names of the constructor that is exposed.

The following example shows a projecting DTO:

A projecting DTO

```java
record NamesOnly(String firstname, String lastname) {
}
```

Java Records are ideal to define DTO types since they adhere to value semantics:
All fields are `private final` and `equals(…)`/`hashCode()`/`toString()` methods are created automatically.
Alternatively, you can use any class that defines the properties you want to project.

<a id="repositories-projections--projection.dynamic"></a>
<a id="repositories-projections--dynamic-projections"></a>

### Dynamic Projections

So far, we have used the projection type as the return type or element type of a collection.
However, you might want to select the type to be used at invocation time (which makes it dynamic).
To apply dynamic projections, use a query method such as the one shown in the following example:

A repository using a dynamic projection parameter

```java
interface PersonRepository extends Repository<Person, UUID> {

  <T> Collection<T> findByLastname(String lastname, Class<T> type);
}
```

This way, the method can be used to obtain the aggregates as is or with a projection applied, as shown in the following example:

Using a repository with dynamic projections

```java
void someMethod(PersonRepository people) {

  Collection<Person> aggregates =
    people.findByLastname("Matthews", Person.class);

  Collection<NamesOnly> aggregates =
    people.findByLastname("Matthews", NamesOnly.class);
}
```

> [!NOTE]
> Query parameters of type `Class` are inspected whether they qualify as dynamic projection parameter.
> If the actual return type of the query equals the generic parameter type of the `Class` parameter, then the matching `Class` parameter is not available for usage within the query or SpEL expressions.
> If you want to use a `Class` parameter as query argument then make sure to use a different generic parameter, for example `Class<?>`.

> [!NOTE]
> When using [Class-based projection](#repositories-projections--projections.dtos), types must declare a single constructor so that Spring Data can determine their input properties.
> If your class defines more than one constructor, then you cannot use the type without further hints for DTO projections.
> In such a case annotate the desired constructor with `@PersistenceCreator` as outlined below so that Spring Data can determine which properties to select:
>
> ```java
> public class NamesOnly {
>
>   private final String firstname;
>   private final String lastname;
>
>   protected NamesOnly() { }
>
>   @PersistenceCreator
>   public NamesOnly(String firstname, String lastname) {
>       this.firstname = firstname;
>       this.lastname = lastname;
>   }
>
>   // ...
> }
> ```

---

<a id="repositories-custom-implementations"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/custom-implementations.html -->

<!-- page_index: 36 -->

# Custom Repository Implementations

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-custom-implementations--page-title"></a>
<a id="repositories-custom-implementations--custom-repository-implementations"></a>

# Custom Repository Implementations

Spring Data provides various options to create query methods with little coding.
But when those options don’t fit your needs you can also provide your own custom implementation for repository methods.
This section describes how to do that.

<a id="repositories-custom-implementations--repositories.single-repository-behavior"></a>
<a id="repositories-custom-implementations--customizing-individual-repositories"></a>

## Customizing Individual Repositories

To enrich a repository with custom functionality, you must first define a fragment interface and an implementation for the custom functionality, as follows:

Interface for custom repository functionality

```java
interface CustomizedUserRepository {
  void someCustomMethod(User user);
}
```

Implementation of custom repository functionality

```java
class CustomizedUserRepositoryImpl implements CustomizedUserRepository {

  @Override
  public void someCustomMethod(User user) {
    // Your custom implementation
  }
}
```

> [!NOTE]
> The most important part of the class name that corresponds to the fragment interface is the `Impl` postfix.
> You can customize the store-specific postfix by setting `@Enable<StoreModule>Repositories(repositoryImplementationPostfix = …)`.

> [!WARNING]
> Historically, Spring Data custom repository implementation discovery followed a
> [naming pattern](https://docs.spring.io/spring-data/commons/docs/1.9.0.RELEASE/reference/html/#repositories.single-repository-behaviour)
> that derived the custom implementation class name from the repository allowing effectively a single custom implementation.
>
> A type located in the same package as the repository interface, matching *repository interface name* followed by *implementation postfix*, is considered a custom implementation and will be treated as a custom implementation.
> A class following that name can lead to undesired behavior.
>
> We consider the single-custom implementation naming deprecated and recommend not using this pattern.
> Instead, migrate to a fragment-based programming model.

The implementation itself does not depend on Spring Data and can be a regular Spring bean.
Consequently, you can use standard dependency injection behavior to inject references to other beans (such as a `JdbcTemplate`), take part in aspects, and so on.

Then you can let your repository interface extend the fragment interface, as follows:

Changes to your repository interface

```java
interface UserRepository extends CrudRepository<User, Long>, CustomizedUserRepository {

  // Declare query methods here
}
```

Extending the fragment interface with your repository interface combines the CRUD and custom functionality and makes it available to clients.

Spring Data repositories are implemented by using fragments that form a repository composition.
Fragments are the base repository, functional aspects (such as [Querydsl](https://docs.spring.io/spring-data/elasticsearch/reference/repositories/core-extensions.html#core.extensions.querydsl)), and custom interfaces along with their implementations.
Each time you add an interface to your repository interface, you enhance the composition by adding a fragment.
The base repository and repository aspect implementations are provided by each Spring Data module.

The following example shows custom interfaces and their implementations:

Fragments with their implementations

```java
interface HumanRepository {void someHumanMethod(User user);}
class HumanRepositoryImpl implements HumanRepository {
@Override public void someHumanMethod(User user) {// Your custom implementation}}
interface ContactRepository {
void someContactMethod(User user);
User anotherContactMethod(User user);}
class ContactRepositoryImpl implements ContactRepository {
@Override public void someContactMethod(User user) {// Your custom implementation}
@Override public User anotherContactMethod(User user) {// Your custom implementation}}
```

The following example shows the interface for a custom repository that extends `CrudRepository`:

Changes to your repository interface

```java
interface UserRepository extends CrudRepository<User, Long>, HumanRepository, ContactRepository {

  // Declare query methods here
}
```

Repositories may be composed of multiple custom implementations that are imported in the order of their declaration.
Custom implementations have a higher priority than the base implementation and repository aspects.
This ordering lets you override base repository and aspect methods and resolves ambiguity if two fragments contribute the same method signature.
Repository fragments are not limited to use in a single repository interface.
Multiple repositories may use a fragment interface, letting you reuse customizations across different repositories.

The following example shows a repository fragment and its implementation:

Fragments overriding `save(…)`

```java
interface CustomizedSave<T> {<S extends T> S save(S entity);}
class CustomizedSaveImpl<T> implements CustomizedSave<T> {
@Override public <S extends T> S save(S entity) {// Your custom implementation}}
```

The following example shows a repository that uses the preceding repository fragment:

Customized repository interfaces

```java
interface UserRepository extends CrudRepository<User, Long>, CustomizedSave<User> {
}

interface PersonRepository extends CrudRepository<Person, Long>, CustomizedSave<Person> {
}
```

<a id="repositories-custom-implementations--repositories.configuration"></a>
<a id="repositories-custom-implementations--configuration"></a>

### Configuration

The repository infrastructure tries to autodetect custom implementation fragments by scanning for classes below the package in which it found a repository.
These classes need to follow the naming convention of appending a postfix defaulting to `Impl`.

The following example shows a repository that uses the default postfix and a repository that sets a custom value for the postfix:

Example 1. Configuration example

- Java
- XML

```java
@EnableElasticsearchRepositories(repositoryImplementationPostfix = "MyPostfix")
class Configuration { … }
```

```xml
<repositories base-package="com.acme.repository" />

<repositories base-package="com.acme.repository" repository-impl-postfix="MyPostfix" />
```

The first configuration in the preceding example tries to look up a class called `com.acme.repository.CustomizedUserRepositoryImpl` to act as a custom repository implementation.
The second example tries to look up `com.acme.repository.CustomizedUserRepositoryMyPostfix`.

<a id="repositories-custom-implementations--repositories.single-repository-behaviour.ambiguity"></a>
<a id="repositories-custom-implementations--resolution-of-ambiguity"></a>

#### Resolution of Ambiguity

If multiple implementations with matching class names are found in different packages, Spring Data uses the bean names to identify which one to use.

Given the following two custom implementations for the `CustomizedUserRepository` shown earlier, the first implementation is used.
Its bean name is `customizedUserRepositoryImpl`, which matches that of the fragment interface (`CustomizedUserRepository`) plus the postfix `Impl`.

Example 2. Resolution of ambiguous implementations

```java
class CustomizedUserRepositoryImpl implements CustomizedUserRepository {

  // Your custom implementation
}
```

```java
@Component("specialCustomImpl")
class CustomizedUserRepositoryImpl implements CustomizedUserRepository {

  // Your custom implementation
}
```

If you annotate the `UserRepository` interface with `@Component("specialCustom")`, the bean name plus `Impl` then matches the one defined for the repository implementation in `com.acme.impl.two`, and it is used instead of the first one.

<a id="repositories-custom-implementations--repositories.manual-wiring"></a>
<a id="repositories-custom-implementations--manual-wiring"></a>

#### Manual Wiring

If your custom implementation uses annotation-based configuration and autowiring only, the preceding approach shown works well, because it is treated as any other Spring bean.
If your implementation fragment bean needs special wiring, you can declare the bean and name it according to the conventions described in the [preceding section](#repositories-custom-implementations--repositories.single-repository-behaviour.ambiguity).
The infrastructure then refers to the manually defined bean definition by name instead of creating one itself.
The following example shows how to manually wire a custom implementation:

Example 3. Manual wiring of custom implementations

- Java
- XML

```java
class MyClass {
  MyClass(@Qualifier("userRepositoryImpl") UserRepository userRepository) {
    …
  }
}
```

```xml
<repositories base-package="com.acme.repository" />

<beans:bean id="userRepositoryImpl" class="…">
  <!-- further configuration -->
</beans:bean>
```

<a id="repositories-custom-implementations--repositories.spring-factories"></a>
<a id="repositories-custom-implementations--registering-fragments-with-spring.factories"></a>

#### Registering Fragments with spring.factories

As already mentioned in the [Configuration](#repositories-custom-implementations--repositories.configuration) section, the infrastructure only auto-detects fragments within the repository base-package.
Therefore, fragments residing in another location or want to be contributed by an external archive will not be found if they do not share a common namespace.
Registering fragments within `spring.factories` allows you to circumvent this restriction as explained in the following section.

Imagine you’d like to provide some custom search functionality usable across multiple repositories for your organization leveraging a text search index.

First all you need is the fragment interface.
Note the generic `<T>` parameter to align the fragment with the repository domain type.

Fragment Interface

```java
public interface SearchExtension<T> {

    List<T> search(String text, Limit limit);
}
```

Let’s assume the actual full-text search is available via a `SearchService` that is registered as a `Bean` within the context so you can consume it in our `SearchExtension` implementation.
All you need to run the search is the collection (or index) name and an object mapper that converts the search results into actual domain objects as sketched out below.

Fragment implementation

```java
import org.springframework.beans.factory.annotation.Autowired; import org.springframework.data.domain.Limit; import org.springframework.data.repository.core.RepositoryMethodContext;
class DefaultSearchExtension<T> implements SearchExtension<T> {
private final SearchService service;
DefaultSearchExtension(SearchService service) {this.service = service;}
@Override public List<T> search(String text, Limit limit) {return search(RepositoryMethodContext.getContext(), text, limit);}
List<T> search(RepositoryMethodContext metadata, String text, Limit limit) {
Class<T> domainType = metadata.getRepository().getDomainType();
String indexName = domainType.getSimpleName().toLowerCase(); List<String> jsonResult = service.search(indexName, text, 0, limit.max());
return jsonResult.stream().map(…).collect(toList());}}
```

In the example above `RepositoryMethodContext.getContext()` is used to retrieve metadata for the actual method invocation.
`RepositoryMethodContext` exposes information attached to the repository such as the domain type.
In this case we use the repository domain type to identify the name of the index to be searched.

Exposing invocation metadata is costly, hence it is disabled by default.
To access `RepositoryMethodContext.getContext()` you need to advise the repository factory responsible for creating the actual repository to expose method metadata.

Expose Repository Metadata

- Marker Interface
- Bean Post Processor

Adding the `RepositoryMetadataAccess` marker interface to the fragments implementation will trigger the infrastructure and enable metadata exposure for those repositories using the fragment.

```java
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.Limit;
import org.springframework.data.repository.core.support.RepositoryMetadataAccess;
import org.springframework.data.repository.core.RepositoryMethodContext;

class DefaultSearchExtension<T> implements SearchExtension<T>, RepositoryMetadataAccess {

    // ...
}
```

The `exposeMetadata` flag can be set directly on the repository factory bean via a `BeanPostProcessor`.

```java
import org.springframework.beans.factory.config.BeanPostProcessor; import org.springframework.context.annotation.Configuration; import org.springframework.data.repository.core.support.RepositoryFactoryBeanSupport;
@Configuration class MyConfiguration {
@Bean static BeanPostProcessor exposeMethodMetadata() {
return new BeanPostProcessor() {
@Override public Object postProcessBeforeInitialization(Object bean, String beanName) {
if(bean instanceof RepositoryFactoryBeanSupport<?,?,?> factoryBean) {factoryBean.setExposeMetadata(true);} return bean;} };}}
```

Please do not just copy/paste the above but consider your actual use case which may require a more fine-grained approach as the above will simply enable the flag on every repository.

Having both, the fragment declaration and implementation in place you can register the extension in the `META-INF/spring.factories` file and package things up if needed.

Register the fragment in `META-INF/spring.factories`

```properties
com.acme.search.SearchExtension=com.acme.search.DefaultSearchExtension
```

Now you are ready to make use of your extension; Simply add the interface to your repository.

Using it

```java
import com.acme.search.SearchExtension;
import org.springframework.data.repository.CrudRepository;

interface MovieRepository extends CrudRepository<Movie, String>, SearchExtension<Movie> {

}
```

<a id="repositories-custom-implementations--repositories.customize-base-repository"></a>
<a id="repositories-custom-implementations--customize-the-base-repository"></a>

## Customize the Base Repository

The approach described in the [preceding section](#repositories-custom-implementations--repositories.manual-wiring) requires customization of each repository interfaces when you want to customize the base repository behavior so that all repositories are affected.
To instead change behavior for all repositories, you can create an implementation that extends the persistence technology-specific repository base class.
This class then acts as a custom base class for the repository proxies, as shown in the following example:

Custom repository base class

```java
class MyRepositoryImpl<T, ID>
  extends SimpleJpaRepository<T, ID> {

  private final EntityManager entityManager;

  MyRepositoryImpl(JpaEntityInformation entityInformation,
                          EntityManager entityManager) {
    super(entityInformation, entityManager);

    // Keep the EntityManager around to used from the newly introduced methods.
    this.entityManager = entityManager;
  }

  @Override
  @Transactional
  public <S extends T> S save(S entity) {
    // implementation goes here
  }
}
```

> [!WARNING]
> The class needs to have a constructor of the super class which the store-specific repository factory implementation uses.
> If the repository base class has multiple constructors, override the one taking an `EntityInformation` plus a store specific infrastructure object (such as an `EntityManager` or a template class).

The final step is to make the Spring Data infrastructure aware of the customized repository base class.
In configuration, you can do so by using the `repositoryBaseClass`, as shown in the following example:

Example 4. Configuring a custom repository base class

- Java
- XML

```java
@Configuration
@EnableElasticsearchRepositories(repositoryBaseClass = MyRepositoryImpl.class)
class ApplicationConfiguration { … }
```

```xml
<repositories base-package="com.acme.repository"
     base-class="….MyRepositoryImpl" />
```

<a id="repositories-custom-implementations--repositories.customize-repository-factory"></a>
<a id="repositories-custom-implementations--customizing-the-repository-factory"></a>

## Customizing the Repository Factory

Customizing the [repository factory](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFactorySupport.html) through [`RepositoryFactoryCustomizer`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFactoryCustomizer.html) provides direct access to components involved with repository instance creation.
This mechanism is useful when you want to adjust selected aspects of proxy creation without introducing a fully custom repository factory bean.
The following example, demonstrates registering additional listeners and proxy advisors:

```java
factoryBean.addRepositoryFactoryCustomizer(repositoryFactory -> {
	repositoryFactory.addInvocationListener(…);
	repositoryFactory.addQueryCreationListener(…);

	repositoryFactory.addRepositoryProxyPostProcessor((factory, repositoryInformation) -> factory.addAdvice(…));
});
```

A `RepositoryFactoryCustomizer` is associated with a particular repository factory bean, ideally through `BeanPostProcessor` so that only specific repositories are affected.
Note that customizer beans are not applied automatically to prevent unwanted wiring that become especially relevant in multi-repository arrangements or when using multiple Spring Data modules.

<a id="repositories-custom-implementations--repositories.customize-repository-factory-bean"></a>
<a id="repositories-custom-implementations--customize-the-repository-factory-bean"></a>

## Customize the Repository Factory Bean

The most powerful approach to customize repository creation is to provide a custom repository factory bean, typically a subclass of [`RepositoryFactorySupport`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFactorySupport.html), [`TransactionalRepositoryFactoryBeanSupport`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/TransactionalRepositoryFactoryBeanSupport.html) or the store-specific repository factory bean.

Customizing the repository factory bean allows you to change repository creation entirely with full access to the underlying repository factory.

Note that this approach requires the most effort and is typically only needed when you want to change core aspects of repository creation.
Also, you need to take into consideration repository metadata derivation that is used to identify query methods, base implementation methods and custom implementations.
The following summary outlines the key aspects:

- `repositoryBaseClass`: The repository base class defines which methods are implemented by the base class and which methods require additional handling through aspects or custom implementations.
- `repositoryFragmentsContributor`: A [`RepositoryFragmentsContributor`](https://docs.spring.io/spring-data/commons/reference/4.1/api/java/org/springframework/data/repository/core/support/RepositoryFragmentsContributor.html) allows contributions to repository composition after all standard fragments have been collected.
  Store modules use this mechanism to add features such as Querydsl or Query-by-Example support.
  It also serves as an SPI for third-party extensions.
- `exposeMetadata`: Controls whether [invocation metadata](#repositories-custom-implementations--expose-repository-metadata) is available through `RepositoryMethodContext.getContext()`.

---

<a id="repositories-core-domain-events"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/core-domain-events.html -->

<!-- page_index: 37 -->

# Publishing Events from Aggregate Roots

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-core-domain-events--page-title"></a>
<a id="repositories-core-domain-events--publishing-events-from-aggregate-roots"></a>

# Publishing Events from Aggregate Roots

Entities managed by repositories are aggregate roots.
In a Domain-Driven Design application, these aggregate roots usually publish domain events.
Spring Data provides an annotation called `@DomainEvents` that you can use on a method of your aggregate root to make that publication as easy as possible, as shown in the following example:

Exposing domain events from an aggregate root

```java
class AnAggregateRoot {
@DomainEvents (1) Collection<Object> domainEvents() {// … return events you want to get published here}
@AfterDomainEventPublication (2) void callbackMethod() {// … potentially clean up domain events list}}
```

**1**

The method that uses `@DomainEvents` can return either a single event instance or a collection of events.
It must not take any arguments.

**2**

After all events have been published, we have a method annotated with `@AfterDomainEventPublication`.
You can use it to potentially clean the list of events to be published (among other uses).

The methods are called every time one of the following a Spring Data repository methods are called:

- `save(…)`, `saveAll(…)`
- `delete(…)`, `deleteAll(…)`, `deleteAllInBatch(…)`, `deleteInBatch(…)`

Note, that these methods take the aggregate root instances as arguments.
This is why `deleteById(…)` is notably absent, as the implementations might choose to issue a query deleting the instance and thus we would never have access to the aggregate instance in the first place.

---

<a id="repositories-null-handling"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/null-handling.html -->

<!-- page_index: 38 -->

# Null Handling of Repository Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-null-handling--page-title"></a>
<a id="repositories-null-handling--null-handling-of-repository-methods"></a>

# Null Handling of Repository Methods

Repository CRUD methods that return an individual aggregate instances can use `Optional` to indicate the potential absence of a value.
Besides that, Spring Data supports returning the following wrapper types on query methods:

- `com.google.common.base.Optional`
- `scala.Option`
- `io.vavr.control.Option`

Alternatively, query methods can choose not to use a wrapper type at all.
The absence of a query result is then indicated by returning `null`.
Repository methods returning collections, collection alternatives, wrappers, and streams are guaranteed never to return `null` but rather the corresponding empty representation.
See “[Repository query return types](#repositories-query-return-types-reference)” for details.

<a id="repositories-null-handling--repositories.nullability.annotations"></a>
<a id="repositories-null-handling--nullability-annotations"></a>

## Nullability Annotations

<a id="repositories-null-handling--_jspecify"></a>
<a id="repositories-null-handling--jspecify"></a>

### JSpecify

As of Spring Framework 7 and Spring Data 4, you can express nullability constraints for repository methods by using [JSpecify](https://jspecify.dev/docs/start-here/).
JSpecify is well integrated into IntelliJ and Eclipse to provide a tooling-friendly approach and opt-in `null` checks during runtime, as follows:

- [`@NullMarked`](https://jspecify.dev/docs/api/org/jspecify/annotations/NullMarked.html): Used on the module-, package- and class-level to declare that the default behavior for parameters and return values is, respectively, neither to accept nor to produce `null` values.
- [`@NonNull`](https://jspecify.dev/docs/api/org/jspecify/annotations/NonNull.html): Used on a type level for parameter or return values that must not be `null` (not needed on parameters and return values already covered by `@NullMarked`).
- [`@Nullable`](https://jspecify.dev/docs/api/org/jspecify/annotations/Nullable.html): Used on the type level for parameter or return values that can be `null`.
- [`@NullUnmarked`](https://jspecify.dev/docs/api/org/jspecify/annotations/NullUnmarked.html): Used on the package-, class-, and method-level to roll back nullness declaration and opt-out from a previous `@NullMarked`.
  Nullness changes to unspecified in such a case.

`@NullMarked` at the package level via a `package-info.java` file

```java
@NullMarked
package org.springframework.core;

import org.jspecify.annotations.NullMarked;
```

In the various Java files belonging to the package, nullable type usages are defined explicitly with
[`@Nullable`](https://jspecify.dev/docs/api/org/jspecify/annotations/Nullable.html).
It is recommended that this annotation is specified just before the related type.

For example, for a field:

```java
private @Nullable String fileEncoding;
```

Or for method parameters and return value:

```java
public static @Nullable String buildMessage(@Nullable String message,
                                            @Nullable Throwable cause) {
    // ...
}
```

When overriding a method, nullness annotations are not inherited from the superclass method.
That means those nullness annotations should be repeated if you just want to override the implementation and keep the same API nullness.

With arrays and varargs, you need to be able to differentiate the nullness of the elements from the nullness of the array itself.
Pay attention to the syntax
[defined by the Java specification](https://docs.oracle.com/javase/specs/jls/se17/html/jls-9.html#jls-9.7.4) which may be initially surprising:

- `@Nullable Object[] array` means individual elements can be null but the array itself can’t.
- `Object @Nullable [] array` means individual elements can’t be null but the array itself can.
- `@Nullable Object @Nullable [] array` means both individual elements and the array can be null.

The Java specifications also enforces that annotations defined with `@Target(ElementType.TYPE_USE)` like JSpecify
`@Nullable` should be specified after the last `.` with inner or fully qualified types:

- `Cache.@Nullable ValueWrapper`
- `jakarta.validation.@Nullable Validator`

[`@NonNull`](https://jspecify.dev/docs/api/org/jspecify/annotations/NonNull.html) and
[`@NullUnmarked`](https://jspecify.dev/docs/api/org/jspecify/annotations/NullUnmarked.html) should rarely be needed for typical use cases.

<a id="repositories-null-handling--_spring_framework_nullability_and_jsr_305_annotations"></a>
<a id="repositories-null-handling--spring-framework-nullability-and-jsr-305-annotations"></a>

### Spring Framework Nullability and JSR-305 Annotations

You can express nullability constraints for repository methods by using [Spring Framework’s nullability annotations](https://docs.spring.io/spring-framework/reference/7.0/core/null-safety.html).

> [!NOTE]
> As of Spring Framework 7, Spring’s nullability annotations are deprecated in favor of JSpecify.
> Consult the framework documentation on [Migrating from Spring null-safety annotations to JSpecify](https://docs.spring.io/spring-framework/reference/7.0/core/null-safety.html) for more information.

They provide a tooling-friendly approach and opt-in `null` checks during runtime, as follows:

- [`@NonNullApi`](https://docs.spring.io/spring-framework/docs/7.0.8/javadoc-api/org/springframework/lang/NonNullApi.html): Used on the package level to declare that the default behavior for parameters and return values is, respectively, neither to accept nor to produce `null` values.
- [`@NonNull`](https://docs.spring.io/spring-framework/docs/7.0.8/javadoc-api/org/springframework/lang/NonNull.html): Used on a parameter or return value that must not be `null` (not needed on a parameter and return value where `@NonNullApi` applies).
- [`@Nullable`](https://docs.spring.io/spring-framework/docs/7.0.8/javadoc-api/org/springframework/lang/Nullable.html): Used on a parameter or return value that can be `null`.

Spring annotations are meta-annotated with [JSR 305](https://jcp.org/en/jsr/detail?id=305) annotations (a dormant but widely used JSR).
JSR 305 meta-annotations let tooling vendors (such as [IDEA](https://www.jetbrains.com/help/idea/nullable-and-notnull-annotations.html), [Eclipse](https://help.eclipse.org/latest/index.jsp?topic=/org.eclipse.jdt.doc.user/tasks/task-using_external_null_annotations.htm), and [Kotlin](https://kotlinlang.org/docs/reference/java-interop.html#null-safety-and-platform-types)) provide null-safety support in a generic way, without having to hard-code support for Spring annotations.
To enable runtime checking of nullability constraints for query methods, you need to activate non-nullability on the package level by using Spring’s `@NonNullApi` in `package-info.java`, as shown in the following example:

Declaring Non-nullability in `package-info.java`

```java

```

Once non-null defaulting is in place, repository query method invocations get validated at runtime for nullability constraints.
If a query result violates the defined constraint, an exception is thrown.
This happens when the method would return `null` but is declared as non-nullable (the default with the annotation defined on the package in which the repository resides).
If you want to opt-in to nullable results again, selectively use `@Nullable` on individual methods.
Using the result wrapper types mentioned at the start of this section continues to work as expected: an empty result is translated into the value that represents absence.

The following example shows a number of the techniques just described:

Using different nullability constraints

```java
package com.acme;                                                       (1)

import org.springframework.lang.Nullable;

interface UserRepository extends Repository<User, Long> {

  User getByEmailAddress(EmailAddress emailAddress);                    (2)

  @Nullable
  User findByEmailAddress(@Nullable EmailAddress emailAddress);          (3)

  Optional<User> findOptionalByEmailAddress(EmailAddress emailAddress); (4)
}
```

**1**

The repository resides in a package (or sub-package) for which we have defined non-null behavior.

**2**

Throws an `EmptyResultDataAccessException` when the query does not produce a result.
Throws an `IllegalArgumentException` when the `emailAddress` handed to the method is `null`.

**3**

Returns `null` when the query does not produce a result.
Also accepts `null` as the value for `emailAddress`.

**4**

Returns `Optional.empty()` when the query does not produce a result.
Throws an `IllegalArgumentException` when the `emailAddress` handed to the method is `null`.

<a id="repositories-null-handling--repositories.nullability.kotlin"></a>
<a id="repositories-null-handling--nullability-in-kotlin-based-repositories"></a>

## Nullability in Kotlin-based Repositories

Kotlin has the definition of [nullability constraints](https://kotlinlang.org/docs/reference/null-safety.html) baked into the language.
Kotlin code compiles to bytecode, which does not express nullability constraints through method signatures but rather through compiled-in metadata.
Make sure to include the `kotlin-reflect` JAR in your project to enable introspection of Kotlin’s nullability constraints.
Spring Data repositories use the language mechanism to define those constraints to apply the same runtime checks, as follows:

Using nullability constraints on Kotlin repositories

```kotlin
interface UserRepository : Repository<User, String> {

  fun findByUsername(username: String): User     (1)

  fun findByFirstname(firstname: String?): User? (2)
}
```

**1**

The method defines both the parameter and the result as non-nullable (the Kotlin default).
The Kotlin compiler rejects method invocations that pass `null` to the method.
If the query yields an empty result, an `EmptyResultDataAccessException` is thrown.

**2**

This method accepts `null` for the `firstname` parameter and returns `null` if the query does not produce a result.

---

<a id="elasticsearch-repositories-cdi-integration"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/elasticsearch/repositories/cdi-integration.html -->

<!-- page_index: 39 -->

# CDI Integration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="elasticsearch-repositories-cdi-integration--page-title"></a>
<a id="elasticsearch-repositories-cdi-integration--cdi-integration"></a>

# CDI Integration

The Spring Data Elasticsearch repositories can also be set up using CDI functionality.

Example 1. Spring Data Elasticsearch repositories using CDI

```java
class ElasticsearchTemplateProducer {
@Produces @ApplicationScoped public ElasticsearchOperations createElasticsearchTemplate() {// ...                               (1)}}
class ProductService {
private ProductRepository repository;  (2) public Page<Product> findAvailableBookByName(String name, Pageable pageable) {return repository.findByAvailableTrueAndNameStartingWith(name, pageable);} @Inject public void setRepository(ProductRepository repository) {this.repository = repository;}}
```

**1**

Create a component by using the same calls as are used in the [Elasticsearch Operations](#elasticsearch-template) chapter.

**2**

Let the CDI framework inject the Repository into your class.

---

<a id="repositories-query-keywords-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/query-keywords-reference.html -->

<!-- page_index: 40 -->

# Repository query keywords

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-query-keywords-reference--page-title"></a>
<a id="repositories-query-keywords-reference--repository-query-keywords"></a>

# Repository query keywords

<a id="repositories-query-keywords-reference--appendix.query.method.subject"></a>
<a id="repositories-query-keywords-reference--supported-query-method-subject-keywords"></a>

## Supported query method subject keywords

The following table lists the subject keywords generally supported by the Spring Data repository query derivation mechanism to express the predicate.
Consult the store-specific documentation for the exact list of supported keywords, because some keywords listed here might not be supported in a particular store.

| Keyword | Description |
| --- | --- |
| `find…By`, `read…By`, `get…By`, `query…By`, `search…By`, `stream…By` | General query method returning typically the repository type, a `Collection` or `Streamable` subtype or a result wrapper such as `Page`, `GeoResults` or any other store-specific result wrapper. Can be used as `findBy…`, `findMyDomainTypeBy…` or in combination with additional keywords. |
| `exists…By` | Exists projection, returning typically a `boolean` result. |
| `count…By` | Count projection returning a numeric result. |
| `delete…By`, `remove…By` | Delete query method returning either no result (`void`) or the delete count. |
| `…First<number>…`, `…Top<number>…` | Limit the query results to the first `<number>` of results. This keyword can occur in any place of the subject between `find` (and the other keywords) and `by`. |
| `…Distinct…` | Use a distinct query to return only unique results. Consult the store-specific documentation whether that feature is supported. This keyword can occur in any place of the subject between `find` (and the other keywords) and `by`. |

<a id="repositories-query-keywords-reference--appendix.query.method.reserved"></a>
<a id="repositories-query-keywords-reference--reserved-methods"></a>

## Reserved methods

The following table lists reserved methods that use predefined functionality (as defined in `CrudRepository`).
These methods are directly invoked on the backing (store-specific) implementation of the repository proxy.
See also “[Defining Query Methods](#repositories-query-methods-details--repositories.query-methods.reserved-methods)”.

`deleteAllById(Iterable<ID> identifiers)`

`deleteById(ID identifier)`

`existsById(ID identifier)`

`findAllById(Iterable<ID> identifiers)`

`findById(ID identifier)`

<a id="repositories-query-keywords-reference--appendix.query.method.predicate"></a>
<a id="repositories-query-keywords-reference--supported-query-method-predicate-keywords-and-modifiers"></a>

## Supported query method predicate keywords and modifiers

The following table lists the predicate keywords generally supported by the Spring Data repository query derivation mechanism.
However, consult the store-specific documentation for the exact list of supported keywords, because some keywords listed here might not be supported in a particular store.

| Logical keyword | Keyword expressions |
| --- | --- |
| `AND` | `And` |
| `OR` | `Or` |
| `AFTER` | `After`, `IsAfter` |
| `BEFORE` | `Before`, `IsBefore` |
| `CONTAINING` | `Containing`, `IsContaining`, `Contains` |
| `BETWEEN` | `Between`, `IsBetween` |
| `ENDING_WITH` | `EndingWith`, `IsEndingWith`, `EndsWith` |
| `EXISTS` | `Exists` |
| `FALSE` | `False`, `IsFalse` |
| `GREATER_THAN` | `GreaterThan`, `IsGreaterThan` |
| `GREATER_THAN_EQUALS` | `GreaterThanEqual`, `IsGreaterThanEqual` |
| `IN` | `In`, `IsIn` |
| `IS` | `Is`, `Equals`, (or no keyword) |
| `IS_EMPTY` | `IsEmpty`, `Empty` |
| `IS_NOT_EMPTY` | `IsNotEmpty`, `NotEmpty` |
| `IS_NOT_NULL` | `NotNull`, `IsNotNull` |
| `IS_NULL` | `Null`, `IsNull` |
| `LESS_THAN` | `LessThan`, `IsLessThan` |
| `LESS_THAN_EQUAL` | `LessThanEqual`, `IsLessThanEqual` |
| `LIKE` | `Like`, `IsLike` |
| `NEAR` | `Near`, `IsNear` |
| `NOT` | `Not`, `IsNot` |
| `NOT_IN` | `NotIn`, `IsNotIn` |
| `NOT_LIKE` | `NotLike`, `IsNotLike` |
| `REGEX` | `Regex`, `MatchesRegex`, `Matches` |
| `STARTING_WITH` | `StartingWith`, `IsStartingWith`, `StartsWith` |
| `TRUE` | `True`, `IsTrue` |
| `WITHIN` | `Within`, `IsWithin` |

In addition to filter predicates, the following list of modifiers is supported:

| Keyword | Description |
| --- | --- |
| `IgnoreCase`, `IgnoringCase` | Used with a predicate keyword for case-insensitive comparison. |
| `AllIgnoreCase`, `AllIgnoringCase` | Ignore case for all suitable properties. Used somewhere in the query method predicate. |
| `OrderBy…` | Specify a static sorting order followed by the property path and direction (e.g. `OrderByFirstnameAscLastnameDesc`). |

---

<a id="repositories-query-return-types-reference"></a>

<!-- source_url: https://docs.spring.io/spring-data/elasticsearch/reference/repositories/query-return-types-reference.html -->

<!-- page_index: 41 -->

# Repository query return types

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories-query-return-types-reference--page-title"></a>
<a id="repositories-query-return-types-reference--repository-query-return-types"></a>

# Repository query return types

<a id="repositories-query-return-types-reference--appendix.query.return.types"></a>
<a id="repositories-query-return-types-reference--supported-query-return-types"></a>

## Supported Query Return Types

The following table lists the return types generally supported by Spring Data repositories.
However, consult the store-specific documentation for the exact list of supported return types, because some types listed here might not be supported in a particular store.

> [!NOTE]
> Geospatial types (such as `GeoResult`, `GeoResults`, and `GeoPage`) are available only for data stores that support geospatial queries.
> Some store modules may define their own result wrapper types.

| Return type | Description |
| --- | --- |
| `void` | Denotes no return value. |
| Primitives | Java primitives. |
| Wrapper types | Java wrapper types. |
| `T` | A unique entity. Expects the query method to return one result at most. If no result is found, `null` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Iterator<T>` | An `Iterator`. |
| `Collection<T>` | A `Collection`. |
| `List<T>` | A `List`. |
| `Optional<T>` | A Java `Optional` or Guava `Optional`. Expects the query method to return one result at most. If no result is found, `Optional.empty()` or `Optional.absent()` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Option<T>` | Either a Scala or Vavr `Option` type. Semantically the same behavior as Java’s `Optional`, described earlier. |
| `Stream<T>` | A Java `Stream`. |
| `Streamable<T>` | A convenience extension of `Iterable` that directly exposes methods to stream, map and filter results, concatenate them etc. |
| Types that implement `Streamable` and take a `Streamable` constructor or factory method argument | Types that expose a constructor or `….of(…)`/`….valueOf(…)` factory method taking a `Streamable` as argument. See [Returning Custom Streamable Wrapper Types](#repositories-query-methods-details--repositories.collections-and-iterables.streamable-wrapper) for details. |
| Vavr `Seq`, `List`, `Map`, `Set` | Vavr collection types. See [Support for Vavr Collections](#repositories-query-methods-details--repositories.collections-and-iterables.vavr) for details. |
| `Future<T>` | A `Future`. Expects a method to be annotated with `@Async` and requires Spring’s asynchronous method execution capability to be enabled. |
| `CompletableFuture<T>` | A `CompletableFuture`. Expects a method to be annotated with `@Async` and requires Spring’s asynchronous method execution capability to be enabled. |
| `Slice<T>` | A sized chunk of data with an indication of whether there is more data available. Requires a `Pageable` method parameter. |
| `Page<T>` | A `Slice` with additional information, such as the total number of results. Requires a `Pageable` method parameter. |
| `Window<T>` | A `Window` of results obtained from a scroll query. Provides `ScrollPosition` to issue the next scroll query. Requires a `ScrollPosition` method parameter. |
| `GeoResult<T>` | A result entry with additional information, such as the distance to a reference location. |
| `GeoResults<T>` | A list of `GeoResult<T>` with additional information, such as the average distance to a reference location. |
| `GeoPage<T>` | A `Page` with `GeoResult<T>`, such as the average distance to a reference location. |
| `SearchResult<T>` | A result entry with additional information, such as the score in relation to the reference search term. |
| `SearchResults<T>` | A list of `SearchResult<T>`. |
| `Mono<T>` | A Project Reactor `Mono` emitting zero or one element using reactive repositories. Expects the query method to return one result at most. If no result is found, `Mono.empty()` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Flux<T>` | A Project Reactor `Flux` emitting zero, one, or many elements using reactive repositories. Queries returning `Flux` can emit also an infinite number of elements. |
| `Single<T>` | A RxJava `Single` emitting a single element using reactive repositories. Expects the query method to return one result at most. If no result is found, an error signal (e.g. `EmptyResultDataAccessException`) is emitted. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Maybe<T>` | A RxJava `Maybe` emitting zero or one element using reactive repositories. Expects the query method to return one result at most. If no result is found, `Maybe.empty()` is returned. More than one result triggers an `IncorrectResultSizeDataAccessException`. |
| `Flowable<T>` | A RxJava `Flowable` emitting zero, one, or many elements using reactive repositories. Queries returning `Flowable` can emit also an infinite number of elements. |

---
