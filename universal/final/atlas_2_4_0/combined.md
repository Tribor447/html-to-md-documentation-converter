# Overview

## Navigation

- Docs
  - Api
    - V2
      - [Data Types](#api-v2-data)
      - [Resources](#api-v2)
      - [Resources](#api-v2-resources)
  - [Overview](#index)

## Content

<a id="api-v2-data"></a>

<!-- source_url: https://atlas.apache.org/2.4.0/api/v2/data.html -->

<!-- page_index: 1 -->

<a id="api-v2-data--data"></a>
<a id="api-v2-data--data-types"></a>

# Data Types

<a id="api-v2-data--syntax_json"></a>
<a id="api-v2-data--json"></a>

### JSON

| type | description |
| --- | --- |
| AtlasAggregationEntry |  |
| AtlasAttributeDef |  |
| AtlasBaseModelObject |  |
| AtlasBaseTypeDef |  |
| AtlasBusinessMetadataDef |  |
| AtlasClassification |  |
| AtlasClassificationDef |  |
| AtlasClassifications |  |
| AtlasConstraintDef |  |
| AtlasEntitiesWithExtInfo |  |
| AtlasEntity |  |
| AtlasEntityDef |  |
| AtlasEntityExtInfo |  |
| AtlasEntityHeader |  |
| AtlasEntityHeaders |  |
| AtlasEntityWithExtInfo |  |
| AtlasEnumDef |  |
| AtlasEnumElementDef |  |
| AtlasFullTextResult |  |
| AtlasGlossary |  |
| AtlasGlossaryBaseObject |  |
| AtlasGlossaryCategory |  |
| AtlasGlossaryExtInfo |  |
| AtlasGlossaryHeader |  |
| AtlasGlossaryTerm |  |
| AtlasGlossaryTermHeader |  |
| AtlasLineageInfo |  |
| AtlasObjectId |  |
| AtlasQueryType |  |
| AtlasQuickSearchResult |  |
| AtlasRelatedCategoryHeader |  |
| AtlasRelatedObjectId |  |
| AtlasRelatedTermHeader |  |
| AtlasRelationship |  |
| AtlasRelationshipAttributeDef |  |
| AtlasRelationshipDef |  |
| AtlasRelationshipEndDef |  |
| AtlasRelationshipHeader |  |
| AtlasRelationshipWithExtInfo |  |
| AtlasSearchDownloadRecord |  |
| AtlasSearchResult |  |
| AtlasSearchResultDownloadStatus |  |
| AtlasStruct |  |
| AtlasStructDef |  |
| AtlasSuggestionsResult |  |
| AtlasTermAssignmentHeader |  |
| AtlasTermAssignmentStatus |  |
| AtlasTermCategorizationHeader |  |
| AtlasTermRelationshipStatus |  |
| AtlasTypeDefHeader |  |
| AtlasTypesDef |  |
| AtlasUserSavedSearch |  |
| AttributeSearchResult |  |
| BulkImportResponse |  |
| Cardinality |  |
| ClassificationAssociateRequest |  |
| Condition |  |
| DateFormat |  |
| EntityAuditActionV2 |  |
| EntityAuditEventV2 |  |
| EntityAuditType |  |
| EntityMutationResponse |  |
| EntityOperation |  |
| FilterCriteria |  |
| Format |  |
| ImportInfo |  |
| ImportStatus |  |
| IndexType |  |
| LineageDirection |  |
| LineageInfoOnDemand |  |
| LineageOnDemandConstraints |  |
| LineageRelation |  |
| NumberFormat |  |
| Operator |  |
| PList |  |
| PropagateTags |  |
| QuickSearchParameters |  |
| Relation |  |
| RelationshipCategory |  |
| RelationshipSearchParameters |  |
| RoundingMode |  |
| SavedSearchType |  |
| SearchFilter |  |
| SearchParameters |  |
| SortOrder |  |
| SortType |  |
| Status |  |
| Status |  |
| Status |  |
| TimeBoundary |  |
| TimeZone |  |
| TypeCategory |  |

<a id="api-v2-data--syntax_xml"></a>
<a id="api-v2-data--xml"></a>

### XML

| type | description |
| --- | --- |
| PList |  |
| searchFilter |  |
| sortType |  |
| timeBoundary |  |

---

<a id="api-v2"></a>

<!-- source_url: https://atlas.apache.org/2.4.0/api/v2/index.html -->

<!-- page_index: 2 -->

# Resources

Atlas exposes a variety of REST endpoints to work with types, entities, lineage and data discovery.

<a id="api-v2--resources"></a>

# Resources

There is a [WADL document](https://atlas.apache.org/2.4.0/api/v2/application.wadl) available that describes the resources API.

You may also enjoy the [interactive interface](https://atlas.apache.org/2.4.0/api/v2/ui/index.html) provided for this API by [Swagger](http://swagger.io).

[Try it out!](https://atlas.apache.org/2.4.0/api/v2/ui/index.html)

<table class="table table-hover resources">
<thead>
<tr>
<th align="center">name</th>
<th align="center">path</th>
<th align="center">methods</th>
<th align="center">description</th>
</tr>
</thead>
<tbody>
<tr>
<td> <span>DiscoveryREST</span>
</td>
<td><ul><li> <span>/v2/search/attribute</span>
</li><li> <span>/v2/search/basic</span>
</li><li> <span>/v2/search/dsl</span>
</li><li> <span>/v2/search/fulltext</span>
</li><li> <span>/v2/search/quick</span>
</li><li> <span>/v2/search/relations</span>
</li><li> <span>/v2/search/relationship</span>
</li><li> <span>/v2/search/saved</span>
</li><li> <span>/v2/search/suggestions</span>
</li><li> <span>/v2/search/download/status</span>
</li><li> <span>/v2/search/download/{filename}</span>
</li><li> <span>/v2/search/saved/{guid}</span>
</li><li> <span>/v2/search/saved/{name}</span>
</li><li> <span>/v2/search/basic/download/create_file</span>
</li><li> <span>/v2/search/dsl/download/create_file</span>
</li><li> <span>/v2/search/saved/execute/{name}</span>
</li><li> <span>/v2/search/saved/execute/guid/{guid}</span>
</li></ul></td>
<td><ul><li> <span>GET</span>
</li><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span>
</li><li> <span>GET</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li></ul></td>
<td> <span>REST interface for data discovery using dsl or full text search</span>
</td>
</tr>
<tr>
<td> <span>EntityREST</span>
</td>
<td><ul><li> <span>/v2/entity</span>
</li><li> <span>/v2/entity/bulk</span>
</li><li> <span>/v2/entity/bulk/classification</span>
</li><li> <span>/v2/entity/bulk/headers</span>
</li><li> <span>/v2/entity/bulk/setClassifications</span>
</li><li> <span>/v2/entity/businessmetadata/import</span>
</li><li> <span>/v2/entity/guid/{guid}</span>
</li><li> <span>/v2/entity/{guid}/audit</span>
</li><li> <span>/v2/entity/businessmetadata/import/template</span>
</li><li> <span>/v2/entity/guid/{guid}/businessmetadata</span>
</li><li> <span>/v2/entity/guid/{guid}/classifications</span>
</li><li> <span>/v2/entity/guid/{guid}/header</span>
</li><li> <span>/v2/entity/guid/{guid}/labels</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}</span>
</li><li> <span>/v2/entity/bulk/uniqueAttribute/type/{typeName}</span>
</li><li> <span>/v2/entity/guid/{guid}/businessmetadata/{bmName}</span>
</li><li> <span>/v2/entity/guid/{guid}/classification/{classificationName}</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/classifications</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/header</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/labels</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/classification/{classificationName}</span>
</li></ul></td>
<td><ul><li> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span>
</li><li> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span>
</li><li> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span> <span>PUT</span>
</li><li> <span>DELETE</span>
</li></ul></td>
<td> <span>REST for a single entity</span>
</td>
</tr>
<tr>
<td> <span>GlossaryREST</span>
</td>
<td><ul><li> <span>/v2/glossary</span>
</li><li> <span>/v2/glossary/categories</span>
</li><li> <span>/v2/glossary/category</span>
</li><li> <span>/v2/glossary/import</span>
</li><li> <span>/v2/glossary/term</span>
</li><li> <span>/v2/glossary/terms</span>
</li><li> <span>/v2/glossary/{glossaryGuid}</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}</span>
</li><li> <span>/v2/glossary/import/template</span>
</li><li> <span>/v2/glossary/term/{termGuid}</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/categories</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/detailed</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/partial</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/terms</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}/partial</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}/related</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}/terms</span>
</li><li> <span>/v2/glossary/term/{termGuid}/partial</span>
</li><li> <span>/v2/glossary/terms/{termGuid}/assignedEntities</span>
</li><li> <span>/v2/glossary/terms/{termGuid}/related</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/categories/headers</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/terms/headers</span>
</li></ul></td>
<td><ul><li> <span>GET</span> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li></ul></td>
<td> <span></span>
</td>
</tr>
<tr>
<td> <span>IndexRecoveryREST</span>
</td>
<td><ul><li> <span>/v2/indexrecovery</span>
</li><li> <span>/v2/indexrecovery/start</span>
</li></ul></td>
<td><ul><li> <span>GET</span>
</li><li> <span>POST</span>
</li></ul></td>
<td> <span></span>
</td>
</tr>
<tr>
<td> <span>LineageREST</span>
</td>
<td><ul><li> <span>/v2/lineage/{guid}</span>
</li><li> <span>/v2/lineage/uniqueAttribute/type/{typeName}</span>
</li></ul></td>
<td><ul><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span>
</li></ul></td>
<td> <span>REST interface for an entity's lineage information</span>
</td>
</tr>
<tr>
<td> <span>NotificationREST</span>
</td>
<td><ul><li> <span>/v2/notification/topic/{topicName}</span>
</li></ul></td>
<td><ul><li> <span>POST</span>
</li></ul></td>
<td> <span></span>
</td>
</tr>
<tr>
<td> <span>RelationshipREST</span>
</td>
<td><ul><li> <span>/v2/relationship</span>
</li><li> <span>/v2/relationship/guid/{guid}</span>
</li></ul></td>
<td><ul><li> <span>POST</span> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span>
</li></ul></td>
<td> <span>REST interface for entity relationships.</span>
</td>
</tr>
<tr>
<td> <span>TypesREST</span>
</td>
<td><ul><li> <span>/v2/types/typedefs</span>
</li><li> <span>/v2/types/typedefs/headers</span>
</li><li> <span>/v2/types/businessmetadatadef/guid/{guid}</span>
</li><li> <span>/v2/types/businessmetadatadef/name/{name}</span>
</li><li> <span>/v2/types/classificationdef/guid/{guid}</span>
</li><li> <span>/v2/types/classificationdef/name/{name}</span>
</li><li> <span>/v2/types/entitydef/guid/{guid}</span>
</li><li> <span>/v2/types/entitydef/name/{name}</span>
</li><li> <span>/v2/types/enumdef/guid/{guid}</span>
</li><li> <span>/v2/types/enumdef/name/{name}</span>
</li><li> <span>/v2/types/relationshipdef/guid/{guid}</span>
</li><li> <span>/v2/types/relationshipdef/name/{name}</span>
</li><li> <span>/v2/types/structdef/guid/{guid}</span>
</li><li> <span>/v2/types/structdef/name/{name}</span>
</li><li> <span>/v2/types/typedef/guid/{guid}</span>
</li><li> <span>/v2/types/typedef/name/{name}</span>
</li><li> <span>/v2/types/typedef/name/{typeName}</span>
</li></ul></td>
<td><ul><li> <span>DELETE</span> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span>
</li></ul></td>
<td> <span>REST interface for CRUD operations on type definitions</span>
</td>
</tr>
</tbody>
</table>

<a id="api-v2--data"></a>
<a id="api-v2--data-types"></a>

# Data Types

<a id="api-v2--syntax_json"></a>
<a id="api-v2--json"></a>

### JSON

| type | description |
| --- | --- |
| AtlasAggregationEntry |  |
| AtlasAttributeDef |  |
| AtlasBaseModelObject |  |
| AtlasBaseTypeDef |  |
| AtlasBusinessMetadataDef |  |
| AtlasClassification |  |
| AtlasClassificationDef |  |
| AtlasClassifications |  |
| AtlasConstraintDef |  |
| AtlasEntitiesWithExtInfo |  |
| AtlasEntity |  |
| AtlasEntityDef |  |
| AtlasEntityExtInfo |  |
| AtlasEntityHeader |  |
| AtlasEntityHeaders |  |
| AtlasEntityWithExtInfo |  |
| AtlasEnumDef |  |
| AtlasEnumElementDef |  |
| AtlasFullTextResult |  |
| AtlasGlossary |  |
| AtlasGlossaryBaseObject |  |
| AtlasGlossaryCategory |  |
| AtlasGlossaryExtInfo |  |
| AtlasGlossaryHeader |  |
| AtlasGlossaryTerm |  |
| AtlasGlossaryTermHeader |  |
| AtlasLineageInfo |  |
| AtlasObjectId |  |
| AtlasQueryType |  |
| AtlasQuickSearchResult |  |
| AtlasRelatedCategoryHeader |  |
| AtlasRelatedObjectId |  |
| AtlasRelatedTermHeader |  |
| AtlasRelationship |  |
| AtlasRelationshipAttributeDef |  |
| AtlasRelationshipDef |  |
| AtlasRelationshipEndDef |  |
| AtlasRelationshipHeader |  |
| AtlasRelationshipWithExtInfo |  |
| AtlasSearchDownloadRecord |  |
| AtlasSearchResult |  |
| AtlasSearchResultDownloadStatus |  |
| AtlasStruct |  |
| AtlasStructDef |  |
| AtlasSuggestionsResult |  |
| AtlasTermAssignmentHeader |  |
| AtlasTermAssignmentStatus |  |
| AtlasTermCategorizationHeader |  |
| AtlasTermRelationshipStatus |  |
| AtlasTypeDefHeader |  |
| AtlasTypesDef |  |
| AtlasUserSavedSearch |  |
| AttributeSearchResult |  |
| BulkImportResponse |  |
| Cardinality |  |
| ClassificationAssociateRequest |  |
| Condition |  |
| DateFormat |  |
| EntityAuditActionV2 |  |
| EntityAuditEventV2 |  |
| EntityAuditType |  |
| EntityMutationResponse |  |
| EntityOperation |  |
| FilterCriteria |  |
| Format |  |
| ImportInfo |  |
| ImportStatus |  |
| IndexType |  |
| LineageDirection |  |
| LineageInfoOnDemand |  |
| LineageOnDemandConstraints |  |
| LineageRelation |  |
| NumberFormat |  |
| Operator |  |
| PList |  |
| PropagateTags |  |
| QuickSearchParameters |  |
| Relation |  |
| RelationshipCategory |  |
| RelationshipSearchParameters |  |
| RoundingMode |  |
| SavedSearchType |  |
| SearchFilter |  |
| SearchParameters |  |
| SortOrder |  |
| SortType |  |
| Status |  |
| Status |  |
| Status |  |
| TimeBoundary |  |
| TimeZone |  |
| TypeCategory |  |

<a id="api-v2--syntax_xml"></a>
<a id="api-v2--xml"></a>

### XML

| type | description |
| --- | --- |
| PList |  |
| searchFilter |  |
| sortType |  |
| timeBoundary |  |

---

<a id="api-v2-resources"></a>

<!-- source_url: https://atlas.apache.org/2.4.0/api/v2/resources.html -->

<!-- page_index: 3 -->

<a id="api-v2-resources--resources"></a>

# Resources

There is a [WADL document](https://atlas.apache.org/2.4.0/api/v2/application.wadl) available that describes the resources API.

You may also enjoy the [interactive interface](https://atlas.apache.org/2.4.0/api/v2/ui/index.html) provided for this API by [Swagger](http://swagger.io).

[Try it out!](https://atlas.apache.org/2.4.0/api/v2/ui/index.html)

<table class="table table-hover resources">
<thead>
<tr>
<th align="center">name</th>
<th align="center">path</th>
<th align="center">methods</th>
<th align="center">description</th>
</tr>
</thead>
<tbody>
<tr>
<td> <span>DiscoveryREST</span>
</td>
<td><ul><li> <span>/v2/search/attribute</span>
</li><li> <span>/v2/search/basic</span>
</li><li> <span>/v2/search/dsl</span>
</li><li> <span>/v2/search/fulltext</span>
</li><li> <span>/v2/search/quick</span>
</li><li> <span>/v2/search/relations</span>
</li><li> <span>/v2/search/relationship</span>
</li><li> <span>/v2/search/saved</span>
</li><li> <span>/v2/search/suggestions</span>
</li><li> <span>/v2/search/download/status</span>
</li><li> <span>/v2/search/download/{filename}</span>
</li><li> <span>/v2/search/saved/{guid}</span>
</li><li> <span>/v2/search/saved/{name}</span>
</li><li> <span>/v2/search/basic/download/create_file</span>
</li><li> <span>/v2/search/dsl/download/create_file</span>
</li><li> <span>/v2/search/saved/execute/{name}</span>
</li><li> <span>/v2/search/saved/execute/guid/{guid}</span>
</li></ul></td>
<td><ul><li> <span>GET</span>
</li><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span>
</li><li> <span>GET</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li></ul></td>
<td> <span>REST interface for data discovery using dsl or full text search</span>
</td>
</tr>
<tr>
<td> <span>EntityREST</span>
</td>
<td><ul><li> <span>/v2/entity</span>
</li><li> <span>/v2/entity/bulk</span>
</li><li> <span>/v2/entity/bulk/classification</span>
</li><li> <span>/v2/entity/bulk/headers</span>
</li><li> <span>/v2/entity/bulk/setClassifications</span>
</li><li> <span>/v2/entity/businessmetadata/import</span>
</li><li> <span>/v2/entity/guid/{guid}</span>
</li><li> <span>/v2/entity/{guid}/audit</span>
</li><li> <span>/v2/entity/businessmetadata/import/template</span>
</li><li> <span>/v2/entity/guid/{guid}/businessmetadata</span>
</li><li> <span>/v2/entity/guid/{guid}/classifications</span>
</li><li> <span>/v2/entity/guid/{guid}/header</span>
</li><li> <span>/v2/entity/guid/{guid}/labels</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}</span>
</li><li> <span>/v2/entity/bulk/uniqueAttribute/type/{typeName}</span>
</li><li> <span>/v2/entity/guid/{guid}/businessmetadata/{bmName}</span>
</li><li> <span>/v2/entity/guid/{guid}/classification/{classificationName}</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/classifications</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/header</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/labels</span>
</li><li> <span>/v2/entity/uniqueAttribute/type/{typeName}/classification/{classificationName}</span>
</li></ul></td>
<td><ul><li> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>GET</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span>
</li><li> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span>
</li><li> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>POST</span> <span>PUT</span>
</li><li> <span>DELETE</span>
</li></ul></td>
<td> <span>REST for a single entity</span>
</td>
</tr>
<tr>
<td> <span>GlossaryREST</span>
</td>
<td><ul><li> <span>/v2/glossary</span>
</li><li> <span>/v2/glossary/categories</span>
</li><li> <span>/v2/glossary/category</span>
</li><li> <span>/v2/glossary/import</span>
</li><li> <span>/v2/glossary/term</span>
</li><li> <span>/v2/glossary/terms</span>
</li><li> <span>/v2/glossary/{glossaryGuid}</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}</span>
</li><li> <span>/v2/glossary/import/template</span>
</li><li> <span>/v2/glossary/term/{termGuid}</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/categories</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/detailed</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/partial</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/terms</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}/partial</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}/related</span>
</li><li> <span>/v2/glossary/category/{categoryGuid}/terms</span>
</li><li> <span>/v2/glossary/term/{termGuid}/partial</span>
</li><li> <span>/v2/glossary/terms/{termGuid}/assignedEntities</span>
</li><li> <span>/v2/glossary/terms/{termGuid}/related</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/categories/headers</span>
</li><li> <span>/v2/glossary/{glossaryGuid}/terms/headers</span>
</li></ul></td>
<td><ul><li> <span>GET</span> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>POST</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li></ul></td>
<td> <span></span>
</td>
</tr>
<tr>
<td> <span>IndexRecoveryREST</span>
</td>
<td><ul><li> <span>/v2/indexrecovery</span>
</li><li> <span>/v2/indexrecovery/start</span>
</li></ul></td>
<td><ul><li> <span>GET</span>
</li><li> <span>POST</span>
</li></ul></td>
<td> <span></span>
</td>
</tr>
<tr>
<td> <span>LineageREST</span>
</td>
<td><ul><li> <span>/v2/lineage/{guid}</span>
</li><li> <span>/v2/lineage/uniqueAttribute/type/{typeName}</span>
</li></ul></td>
<td><ul><li> <span>GET</span> <span>POST</span>
</li><li> <span>GET</span>
</li></ul></td>
<td> <span>REST interface for an entity's lineage information</span>
</td>
</tr>
<tr>
<td> <span>NotificationREST</span>
</td>
<td><ul><li> <span>/v2/notification/topic/{topicName}</span>
</li></ul></td>
<td><ul><li> <span>POST</span>
</li></ul></td>
<td> <span></span>
</td>
</tr>
<tr>
<td> <span>RelationshipREST</span>
</td>
<td><ul><li> <span>/v2/relationship</span>
</li><li> <span>/v2/relationship/guid/{guid}</span>
</li></ul></td>
<td><ul><li> <span>POST</span> <span>PUT</span>
</li><li> <span>DELETE</span> <span>GET</span>
</li></ul></td>
<td> <span>REST interface for entity relationships.</span>
</td>
</tr>
<tr>
<td> <span>TypesREST</span>
</td>
<td><ul><li> <span>/v2/types/typedefs</span>
</li><li> <span>/v2/types/typedefs/headers</span>
</li><li> <span>/v2/types/businessmetadatadef/guid/{guid}</span>
</li><li> <span>/v2/types/businessmetadatadef/name/{name}</span>
</li><li> <span>/v2/types/classificationdef/guid/{guid}</span>
</li><li> <span>/v2/types/classificationdef/name/{name}</span>
</li><li> <span>/v2/types/entitydef/guid/{guid}</span>
</li><li> <span>/v2/types/entitydef/name/{name}</span>
</li><li> <span>/v2/types/enumdef/guid/{guid}</span>
</li><li> <span>/v2/types/enumdef/name/{name}</span>
</li><li> <span>/v2/types/relationshipdef/guid/{guid}</span>
</li><li> <span>/v2/types/relationshipdef/name/{name}</span>
</li><li> <span>/v2/types/structdef/guid/{guid}</span>
</li><li> <span>/v2/types/structdef/name/{name}</span>
</li><li> <span>/v2/types/typedef/guid/{guid}</span>
</li><li> <span>/v2/types/typedef/name/{name}</span>
</li><li> <span>/v2/types/typedef/name/{typeName}</span>
</li></ul></td>
<td><ul><li> <span>DELETE</span> <span>GET</span> <span>POST</span> <span>PUT</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>GET</span>
</li><li> <span>DELETE</span>
</li></ul></td>
<td> <span>REST interface for CRUD operations on type definitions</span>
</td>
</tr>
</tbody>
</table>

---

<a id="index"></a>

<!-- source_url: https://atlas.apache.org/2.4.0/index.html -->

<!-- page_index: 4 -->

# Overview

Versions

2.4.0

2.3.0

2.2.0

2.1.0

2.0.0

1.2.0

1.1.0

1.0.0

0.8.4

0.8.3

0.8.2

0.8.1

0.8-incubating

0.7.1-incubating

0.7-incubating

0.6-incubating

0.5-incubating

<a id="index--overview"></a>

# Overview

Atlas is a scalable and extensible set of core foundational governance services – enabling
enterprises to effectively and efficiently meet their compliance requirements within Hadoop and
allows integration with the whole enterprise data ecosystem.

Apache Atlas provides open metadata management and governance capabilities for organizations
to build a catalog of their data assets, classify and govern these assets and provide collaboration
capabilities around these data assets for data scientists, analysts and the data governance team.

<a id="index--features"></a>

## Features

<a id="index--metadata-types-instances"></a>

### Metadata types & instances

- Pre-defined types for various Hadoop and non-Hadoop metadata
- Ability to define new types for the metadata to be managed
- Types can have primitive attributes, complex attributes, object references; can inherit from other types
- Instances of types, called entities, capture metadata object details and their relationships
- REST APIs to work with types and instances allow easier integration

<a id="index--classification"></a>

### Classification

- Ability to dynamically create classifications - like PII, EXPIRES\_ON, DATA\_QUALITY, SENSITIVE
- Classifications can include attributes - like expiry\_date attribute in EXPIRES\_ON classification
- Entities can be associated with multiple classifications, enabling easier discovery and security enforcement
- Propagation of classifications via lineage - automatically ensures that classifications follow the data as it goes through various processing

<a id="index--lineage"></a>

### Lineage

- Intuitive UI to view lineage of data as it moves through various processes
- REST APIs to access and update lineage

<a id="index--searchdiscovery"></a>
<a id="index--search-discovery"></a>

### Search/Discovery

- Intuitive UI to search entities by type, classification, attribute value or free-text
- Rich REST APIs to search by complex criteria
- SQL like query language to search entities - Domain Specific Language (DSL)

<a id="index--security-data-masking"></a>

### Security & Data Masking

- Fine-grained security for metadata access, enabling controls on access to entity instances and operations like add/update/remove classifications
- Integration with Apache Ranger enables authorization/data-masking on data access based on classifications associated with entities in Apache Atlas. For example:
  - who can access data classified as PII, SENSITIVE
  - customer-service users can only see last 4 digits of columns classified as NATIONAL\_ID

<a id="index--getting-started"></a>

## Getting Started

- [What's new in Apache Atlas 2.4?](#index--whatsnew-2.4)
- [Build & Install](#index--installation)
- [Quick Start](#index--quickstart)

<a id="index--api-documentation"></a>

## API Documentation

- [REST API Documentation](#api-v2)
- [Export & Import REST API Documentation](#index--importexportapi)
- [Legacy API Documentation](https://atlas.apache.org/api/rest.html)

<a id="index--developer-setup-documentation"></a>

## Developer Setup Documentation

- [Developer Setup: Eclipse](#index--eclipsesetup)

---
