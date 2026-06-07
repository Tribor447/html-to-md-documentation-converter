# Spring LDAP Reference

## Navigation

- [Spring LDAP Reference](#index)
  
- [Spring LDAP Reference](#index)
  
- [Preface](#preface)
  
- [Introduction](#introduction)
  
- [What’s New in Spring LDAP 4.1](#whats-new)
  
- [Basic Usage](#spring-ldap-basic-usage)
  
- [Simplifying Attribute Access and Manipulation with DirContextAdapter](#dirobjectfactory)
  
- [Object-Directory Mapping (ODM)](#odm)
  
- [Advanced LDAP Queries](#query-builder-advanced)
  
- [Configuration](#configuration)
  
- [Spring LDAP Repositories](#repositories)
  
- [Pooling Support](#pooling)
  
- [Adding Missing Overloaded API Methods](#adding-missing-overloaded-api-methods)
  
- [Processing the DirContext](#processing-the-dircontext)
  
- [Transaction Support](#transaction-support)
  
- [User Authentication using Spring LDAP](#user-authentication)
  
- [LDIF Parsing](#ldif-parsing)
  
- [Utilities](#utilities)
  
- [Testing](#testing)
  
- [Spring LDAP FAQ](#faq)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/index.html -->

<!-- page_index: 1 -->

<a id="index--page-title"></a>
<a id="index--spring-ldap-reference"></a>

# Spring LDAP Reference

Spring LDAP makes it easier to build Spring-based applications that use the Lightweight Directory Access Protocol.

*Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each copy contains this Copyright Notice, whether distributed in print or electronically.*

[Preface](#preface)

---

<a id="preface"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/preface.html -->

<!-- page_index: 2 -->

# Preface

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="preface--page-title"></a>
<a id="preface--preface"></a>

# Preface

The Java Naming and Directory Interface (JNDI) is to LDAP programming what Java Database Connectivity (JDBC) is to SQL programming. There are several similarities between JDBC and JNDI/LDAP (Java LDAP). Despite being two completely different APIs with different pros and cons, they share a number of less flattering characteristics:

- They require extensive plumbing code, even to perform the simplest of tasks.
- All resources need to be correctly closed, no matter what happens.
- Exception handling is difficult.

These points often lead to massive code duplication in common use cases of the APIs. As we all know, code duplication is one of the worst “code smells”. All in all, it boils down to this: JDBC and LDAP programming in Java are both incredibly dull and repetitive.

Spring JDBC, a core component of Spring Framework, provides excellent utilities for simplifying SQL programming. We need a similar framework for Java LDAP programming.

[Spring LDAP Reference](#index)
[Introduction](#introduction)

---

<a id="introduction"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/introduction.html -->

<!-- page_index: 3 -->

# Introduction

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="introduction--page-title"></a>
<a id="introduction--introduction"></a>

# Introduction

This section offers a relatively quick introduction to Spring LDAP. It includes the following content:

- [Overview](#introduction--spring-ldap-introduction-overview)
- [Traditional Java LDAP versus `LdapClient`](#introduction--spring-ldap-traditional-ldap-vs-ldaptemplate)
- [Packaging Overview](#introduction--spring-ldap-packaging-overview)
- [Getting Started](#introduction--spring-ldap-getting-started)
- [Support](#introduction--spring-ldap-support)
- [Acknowledgements](#introduction--spring-ldap-acknowledgements)

<a id="introduction--spring-ldap-introduction-overview"></a>
<a id="introduction--overview"></a>

## Overview

Spring LDAP is designed to simplify LDAP programming in Java. Some of the features provided by the library are:

- [`JdbcTemplate`](https://docs.spring.io/spring/docs/current/javadoc-api/org/springframework/jdbc/core/JdbcTemplate.html)-style template simplifications to LDAP programming.
- JPA- or Hibernate-style annotation-based object and directory mapping.
- Spring Data repository support, including support for QueryDSL.
- Utilities to simplify building LDAP queries and distinguished names.
- Proper LDAP connection pooling.
- Client-side LDAP compensating transaction support.

<a id="introduction--spring-ldap-traditional-ldap-vs-ldaptemplate"></a>
<a id="introduction--traditional-java-ldap-versus-ldapclient"></a>

## Traditional Java LDAP versus `LdapClient`

Consider a method that should search some storage for all persons and return their names in a list.
By using JDBC, we would create a *connection* and run a *query* by using a *statement*. We would then loop over the *result set* and retrieve the *column* we want, adding it to a list.

Working against an LDAP database with JNDI, we would create a *context* and perform a *search* by using a *search filter*. We would then loop over the resulting *naming enumeration*, retrieve the *attribute* we want, and add it to a list.

The traditional way of implementing this person-name search method in Java LDAP looks like the next example. Note the code marked **bold** - this is the code that
actually performs tasks related to the business purpose of the method. The rest is plumbing.

```java
public class TraditionalPersonRepoImpl implements PersonRepo {
   public List<String> getAllPersonNames() {
      Hashtable env = new Hashtable();
      env.put(Context.INITIAL_CONTEXT_FACTORY, "com.sun.jndi.ldap.LdapCtxFactory");
      env.put(Context.PROVIDER_URL, "ldap://localhost:389/dc=example,dc=com");

      DirContext ctx;
      try {
         ctx = new InitialDirContext(env);
      } catch (NamingException e) {
         throw new RuntimeException(e);
      }

      List<String> list = new LinkedList<String>();
      NamingEnumeration results = null;
      try {
         SearchControls controls = new SearchControls();
         controls.setSearchScope(SearchControls.SUBTREE_SCOPE);
         results = ctx.search("", "(objectclass=person)", controls);

         while (results.hasMore()) {
            SearchResult searchResult = (SearchResult) results.next();
            Attributes attributes = searchResult.getAttributes();
            Attribute attr = attributes.get("cn");
            String cn = attr.get().toString();
            list.add(cn);
         }
      } catch (NameNotFoundException e) {
         // The base context was not found.
         // Just clean up and exit.
      } catch (NamingException e) {
         throw new RuntimeException(e);
      } finally {
         if (results != null) {
            try {
               results.close();
            } catch (Exception e) {
               // Never mind this.
            }
         }
         if (ctx != null) {
            try {
               ctx.close();
            } catch (Exception e) {
               // Never mind this.
            }
         }
      }
      return list;
   }
}
```

By using the Spring LDAP `AttributesMapper` and `LdapClient` classes, we get the exact same functionality with the following code:

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient;
public void setLdapClient(LdapClient ldapClient) {this.ldapClient = ldapClient;}
public List<String> getAllPersonNames() {return ldapClient.search().query(query().where("objectclass").is("person") ).map((Attributes attrs) -> attrs.get("cn").get().toString() ).list();}}
```

The amount of boilerplate code is significantly less than in the traditional example.
The `LdapClient` search method makes sure a `DirContext` instance is created, performs the search, maps the attributes to a string by using the given `AttributesMapper`, collects the strings in an internal list, and, finally, returns the list. It also makes sure that the `NamingEnumeration` and `DirContext` are properly closed and
takes care of any exceptions that might happen.

Naturally, this being a Spring Framework sub-project, we use Spring to configure our application, as follows:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:ldap="http://www.springframework.org/schema/ldap"
       xsi:schemaLocation="http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/ldap https://www.springframework.org/schema/ldap/spring-ldap.xsd">

   <ldap:context-source
          url="ldap://localhost:389"
          base="dc=example,dc=com"
          username="cn=Manager"
          password="secret" />

   <bean id="ldapClient" class="org.springframework.ldap.core.LdapClient" factory-method="create">
        <constructor-arg ref="contextSource" />
    </bean>

   <bean id="personRepo" class="com.example.repo.PersonRepoImpl">
      <property name="ldapClient" ref="ldapClient" />
   </bean>
</beans>
```

> [!NOTE]
> To use the custom XML namespace to configure the Spring LDAP components, you need to include references to this namespace in your XML declaration, as in the preceding example.

<a id="introduction--spring-ldap-packaging-overview"></a>
<a id="introduction--packaging-overview"></a>

## Packaging Overview

At a minimum, to use Spring LDAP you need the following:

- `spring-ldap-core`: The Spring LDAP library
- `spring-core`: Miscellaneous utility classes used internally by the framework
- `spring-beans`: Interfaces and classes for manipulating Java beans
- `slf4j`: A simple logging facade, used internally

In addition to the required dependencies, the following optional dependencies are required for certain functionality:

- `spring-data-ldap`: Base infrastructure for repository support and so on
- `spring-context`: Needed if your application is wired up by using the Spring Application Context. `spring-context` adds the ability for application objects to obtain resources by using a consistent API. It is definitely needed if you plan to use the `BaseLdapPathBeanPostProcessor`.
- `spring-tx`: Needed if you plan to use the client-side compensating transaction support.
- `spring-jdbc`: Needed if you plan to use the client-side compensating transaction support.
- `commons-pool`: Needed if you plan to use the pooling functionality.
- `spring-batch`: Needed if you plan to use the LDIF parsing functionality together with Spring Batch.

> [!NOTE]
> `spring-data-ldap` transitively adds `spring-repository.xsd`, which `spring-ldap.xsd` uses.
> Because of this, Spring LDAP’s XML config support requires the dependency even when Spring Data’s feature set is not in use.

<a id="introduction--spring-ldap-getting-started"></a>
<a id="introduction--getting-started"></a>

## Getting Started

The [samples](https://github.com/spring-projects/spring-ldap/tree/main/samples) provide some useful examples of how to use Spring LDAP for common use cases.

<a id="introduction--spring-ldap-support"></a>
<a id="introduction--support"></a>

## Support

If you have questions, ask them on [Stack Overflow with the `spring-ldap` tag](https://stackoverflow.com/questions/tagged/spring-ldap).
The project web page is [spring.io/spring-ldap/](https://spring.io/spring-ldap/).

<a id="introduction--spring-ldap-acknowledgements"></a>
<a id="introduction--acknowledgements"></a>

## Acknowledgements

The initial effort when starting the Spring LDAP project was sponsored by [Jayway](https://www.jayway.com).
Current maintenance of the project is funded by [Pivotal](https://pivotal.io), which has since been acquired by [VMware](https://vmware.com).

Thanks to [Structure101](https://structure101.com/) for providing an open source license that has come in handy for keeping the project structure in check.

[Preface](#preface)
[What’s New in Spring LDAP 4.1](#whats-new)

---

<a id="whats-new"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/whats-new.html -->

<!-- page_index: 4 -->

<a id="whats-new--page-title"></a>
<a id="whats-new--what-s-new-in-spring-ldap-4.1"></a>

# What’s New in Spring LDAP 4.1

<a id="whats-new--whats-new-breaking-changes"></a>
<a id="whats-new--breaking-changes"></a>

## Breaking Changes

- [gh-1285](https://github.com/spring-projects/spring-ldap/issues/1285) - `spring-data-commons` is no longer an optional dependency of `spring-ldap-core`; applications that relied on `spring-ldap-core` to transmit it transitively must now declare it explicitly.

<a id="whats-new--_core"></a>
<a id="whats-new--core"></a>

## Core

- [gh-1404](https://github.com/spring-projects/spring-ldap/issues/1404) - Added `map()`, `single()`, `optional()`, `list()`, and `stream()` methods to `LdapClient` search support

[Introduction](#introduction)
[Javadoc](https://docs.spring.io/spring-ldap/reference/api/java/index.html)

---

<a id="spring-ldap-basic-usage"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/spring-ldap-basic-usage.html -->

<!-- page_index: 5 -->

# Basic Usage

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="spring-ldap-basic-usage--page-title"></a>
<a id="spring-ldap-basic-usage--basic-usage"></a>

# Basic Usage

This section describes the basics of using Spring LDAP. It contains the following content:

- [Search and Lookup Using `AttributesMapper`](#spring-ldap-basic-usage--spring-ldap-basic-usage-search-lookup-attributesmapper)
- [Building LDAP Queries](#spring-ldap-basic-usage--basic-queries)
- [Dynamically Building Distinguished Names](#spring-ldap-basic-usage--ldap-names)
- [Examples](#spring-ldap-basic-usage--spring-ldap-basic-usage-examples)
- [Binding and Unbinding](#spring-ldap-basic-usage--spring-ldap-basic-usage-binding-unbinding)
- [Updating](#spring-ldap-basic-usage--spring-ldap-basic-usage-updating)

<a id="spring-ldap-basic-usage--spring-ldap-basic-usage-search-lookup-attributesmapper"></a>
<a id="spring-ldap-basic-usage--search-and-lookup-using-attributesmapper"></a>

## Search and Lookup Using `AttributesMapper`

The following example uses an [`AttributesMapper`](https://docs.spring.io/spring-ldap/docs/current/api/org/springframework/ldap/core/AttributesMapper.html) to build a List of all the common names of all the person objects.

Example 1. `AttributesMapper` that returns a single attribute

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient;
public void setLdapClient(LdapClient ldapClient) {this.ldapClient = ldapClient;}
public List<String> getAllPersonNames() {return ldapClient.search() .query(query().where("objectclass").is("person")) .map((Attributes attrs) -> (String) attrs.get("cn").get()).list();}}
```

The inline implementation of `AttributesMapper` gets the desired attribute value from the `Attributes` object and returns it. Internally, `LdapClient` iterates over all entries found, calls the given `AttributesMapper` for each entry, and collects the results in a list. The list is then returned by the `search` method.

Note that the `AttributesMapper` implementation could easily be modified to return a full `Person` object, as follows:

Example 2. AttributesMapper that returns a Person object

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient; ...private class PersonAttributesMapper implements AttributesMapper<Person> {public Person mapFromAttributes(Attributes attrs) throws NamingException {Person person = new Person(); person.setFullName((String)attrs.get("cn").get()); person.setLastName((String)attrs.get("sn").get()); person.setDescription((String)attrs.get("description").get()); return person;}}
public List<Person> getAllPersons() {return ldapClient.search() .query(query().where("objectclass").is("person")) .map(new PersonAttributesMapper()).list();}}
```

Entries in LDAP are uniquely identified by their distinguished name (DN).
If you have the DN of an entry, you can retrieve the entry directly without querying for it.
This is called a “lookup” in Java LDAP. The following example shows a lookup for a `Person` object:

Example 3. A lookup resulting in a Person object

```java
public class PersonRepoImpl implements PersonRepo {
   private LdapClient ldapClient;
   ...
   public Person findPerson(String dn) {
      return ldapClient.search().name(dn).map(new PersonAttributesMapper()).single();
   }
}
```

The preceding example looks up the specified DN and passes the found attributes to the supplied `AttributesMapper` — in this case, resulting in a `Person` object.

<a id="spring-ldap-basic-usage--basic-queries"></a>
<a id="spring-ldap-basic-usage--building-ldap-queries"></a>

## Building LDAP Queries

LDAP searches involve a number of parameters, including the following:

- Base LDAP path: Where in the LDAP tree should the search start.
- Search scope: How deep in the LDAP tree should the search go.
- Attributes to return.
- Search filter: The criteria to use when selecting elements within scope.

Spring LDAP provides an [`LdapQueryBuilder`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/query/LdapQueryBuilder.html) with a fluent API for building LDAP Queries.

Suppose you want to perform a search starting at the base DN `dc=261consulting,dc=com`, limiting the returned attributes to `cn` and `sn`, with a filter of `(&(objectclass=person)(sn=?))`, where we want the `?` to be replaced with the value of the `lastName` parameter.
The following example shows how to do it by using the `LdapQueryBuilder`:

Example 4. Building a search filter dynamically

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient; ...public List<String> getPersonNamesByLastName(String lastName) {
LdapQuery query = query() .base("dc=261consulting,dc=com") .attributes("cn", "sn") .where("objectclass").is("person") .and("sn").is(lastName);
return ldapClient.search().query(query) .map((Attributes attrs) -> (String) attrs.get("cn").get()).single();}}
```

> [!NOTE]
> In addition to simplifying building of complex search parameters, the `LdapQueryBuilder` and its associated classes also provide proper escaping of any unsafe characters in search filters. This prevents “LDAP injection”, where a user might use such characters to inject unwanted operations into your LDAP operations.

> [!NOTE]
> `LdapClient` includes many overloaded methods for performing LDAP searches. This is in order to accommodate as many different use cases and programming style preferences as possible. For the vast majority of use cases, the methods that take an `LdapQuery` as input are the recommended methods to use.

> [!NOTE]
> The `AttributesMapper` is only one of the available callback interfaces you can use when handling search and lookup data. See [Simplifying Attribute Access and Manipulation with `DirContextAdapter`](#dirobjectfactory) for alternatives.

For more information on the `LdapQueryBuilder`, see [Advanced LDAP Queries](#query-builder-advanced).

<a id="spring-ldap-basic-usage--ldap-names"></a>
<a id="spring-ldap-basic-usage--dynamically-building-distinguished-names"></a>

## Dynamically Building Distinguished Names

The standard Java implementation of Distinguished Name ([`LdapName`](https://docs.oracle.com/javase/6/docs/api/javax/naming/ldap/LdapName.html))
performs well when it comes to parsing Distinguished Names. However, in practical use, this implementation has a number of shortcomings:

- The `LdapName` implementation is mutable, which is badly suited for an object that represents identity.
- Despite its mutable nature, the API for dynamically building or modifying Distinguished Names by using `LdapName` is cumbersome.
  Extracting values of indexed or (particularly) named components is also a little bit awkward.
- Many of the operations on `LdapName` throw checked exceptions, requiring `try-catch` statements for situations where the error is typically fatal and cannot be repaired in a meaningful manner.

To simplify working with Distinguished Names, Spring LDAP provides an [`LdapNameBuilder`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/support/LdapNameBuilder.html), as well as a number of utility methods in [`LdapUtils`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/support/LdapUtils.html) that help when working with `LdapName`.

<a id="spring-ldap-basic-usage--spring-ldap-basic-usage-examples"></a>
<a id="spring-ldap-basic-usage--examples"></a>

### Examples

This section presents a few examples of the subjects covered in the preceding sections.
The first example dynamically builds an `LdapName` by using `LdapNameBuilder`:

Example 5. Dynamically building an `LdapName` by using `LdapNameBuilder`

```java
import org.springframework.ldap.support.LdapNameBuilder; import javax.naming.Name;
public class PersonRepoImpl implements PersonRepo {public static final String BASE_DN = "dc=example,dc=com";
protected Name buildDn(Person p) {return LdapNameBuilder.newInstance(BASE_DN) .add("c", p.getCountry()) .add("ou", p.getCompany()) .add("cn", p.getFullname()) .build();} ...}
```

Assume that a `Person` has the following attributes:

| Attribute Name | Attribute Value |
| --- | --- |
| `country` | Sweden |
| `company` | Some Company |
| `fullname` | Some Person |

The preceding code would then result in the following distinguished name:

```none
cn=Some Person, ou=Some Company, c=Sweden, dc=example, dc=com
```

The following example extracts values from a distinguished name by using `LdapUtils`

Example 6. Extracting values from a distinguished name by using `LdapUtils`

```java
import org.springframework.ldap.support.LdapNameBuilder; import javax.naming.Name; public class PersonRepoImpl implements PersonRepo {...protected Person buildPerson(Name dn, Attributes attrs) {Person person = new Person(); person.setCountry(LdapUtils.getStringValue(dn, "c")); person.setCompany(LdapUtils.getStringValue(dn, "ou")); person.setFullname(LdapUtils.getStringValue(dn, "cn")); // Populate rest of person object using attributes.
return person;}}
```

Since Java versions prior to and including 1.4 did not provide any public Distinguished Name implementation at all, Spring LDAP 1.x provided its own implementation, `DistinguishedName`.
This implementation suffered from a couple of shortcomings of its own and has been deprecated in version 2.0. You should now use `LdapName` along with the utilities described earlier.

<a id="spring-ldap-basic-usage--spring-ldap-basic-usage-binding-unbinding"></a>
<a id="spring-ldap-basic-usage--binding-and-unbinding"></a>

## Binding and Unbinding

This section describes how to add and remove data. Updating is covered in the [next section](#spring-ldap-basic-usage--spring-ldap-basic-usage-updating).

<a id="spring-ldap-basic-usage--basic-binding-data"></a>
<a id="spring-ldap-basic-usage--adding-data"></a>

### Adding Data

Inserting data in Java LDAP is called binding. This is somewhat confusing, because in LDAP terminology, “bind” means something completely different.
A JNDI bind performs an LDAP Add operation, associating a new entry that has a specified distinguished name with a set of attributes.
The following example adds data by using `LdapClient`:

Example 7. Adding data using Attributes

```java
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient; ...public void create(Person p) {Name dn = buildDn(p); ldapClient.bind(dn).attributes(buildAttributes(p)).execute();}
private Attributes buildAttributes(Person p) {Attributes attrs = new BasicAttributes(); BasicAttribute ocattr = new BasicAttribute("objectclass"); ocattr.add("top"); ocattr.add("person"); attrs.put(ocattr); attrs.put("cn", "Some Person"); attrs.put("sn", "Person"); return attrs;}}
```

Manual attributes building is — while dull and verbose — sufficient for many purposes. You can, however, simplify the binding operation further, as described in [Simplifying Attribute Access and Manipulation with `DirContextAdapter`](#dirobjectfactory).

<a id="spring-ldap-basic-usage--removing-data"></a>

### Removing Data

Removing data in Java LDAP is called unbinding.
A JNDI unbind performs an LDAP Delete operation, removing the entry associated with the specified distinguished name from the LDAP tree.
The following example removes data by using `LdapClient`:

Example 8. Removing data

```java
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient; ...public void delete(Person p) {Name dn = buildDn(p); ldapClient.unbind(dn).execute();}}
```

<a id="spring-ldap-basic-usage--spring-ldap-basic-usage-updating"></a>
<a id="spring-ldap-basic-usage--updating"></a>

## Updating

In Java LDAP, data can be modified in two ways: either by using `rebind` or by using `modifyAttributes`.

<a id="spring-ldap-basic-usage--updating-by-using-rebind"></a>

### Updating by Using Rebind

A `rebind` is a crude way to modify data. It is basically an `unbind` followed by a `bind`.
The following example invokes LDAP’s `rebind`:

Example 9. Modifying using rebind

```java
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient; ...public void update(Person p) {Name dn = buildDn(p); ldapTemplate.bind(dn).attributes(buildAttributes(p)).replaceExisting(true).execute();}}
```

<a id="spring-ldap-basic-usage--modify-modifyattributes"></a>
<a id="spring-ldap-basic-usage--updating-by-using-modifyattributes"></a>

### Updating by Using `modifyAttributes`

A more sophisticated way of modifying data is to use `modifyAttributes`. This operation takes an array of explicit attribute modifications
and performs them on a specific entry, as follows:

Example 10. Modifying using modifyAttributes

```java
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient; ...public void updateDescription(Person p) {Name dn = buildDn(p); Attribute attr = new BasicAttribute("description", p.getDescription()) ModificationItem item = new ModificationItem(DirContext.REPLACE_ATTRIBUTE, attr); ldapTemplate.modify().name(dn).attributes(item).execute();}}
```

Building `Attributes` and `ModificationItem` arrays is a lot of work. However, as we describe in [Simplifying Attribute Access and Manipulation with `DirContextAdapter`](#dirobjectfactory), Spring LDAP provides more help for simplifying these operations.

[Javadoc](https://docs.spring.io/spring-ldap/reference/api/java/index.html)
[Simplifying Attribute Access and Manipulation with `DirContextAdapter`](#dirobjectfactory)

---

<a id="dirobjectfactory"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/dirobjectfactory.html -->

<!-- page_index: 6 -->

# Simplifying Attribute Access and Manipulation with DirContextAdapter

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="dirobjectfactory--page-title"></a>
<a id="dirobjectfactory--simplifying-attribute-access-and-manipulation-with-dircontextadapter"></a>

# Simplifying Attribute Access and Manipulation with `DirContextAdapter`

A little-known — and probably underestimated — feature of the Java LDAP API is the ability to register a `DirObjectFactory` to automatically create objects from found LDAP entries.
Spring LDAP makes use of this feature to return [`DirContextAdapter`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/core/DirContextAdapter.html) instances in certain search and lookup operations.

`DirContextAdapter` is a useful tool for working with LDAP attributes, particularly when adding or modifying data.

<a id="dirobjectfactory--search-and-lookup-using-contextmapper"></a>

## Search and Lookup Using `ContextMapper`

Whenever an entry is found in the LDAP tree, its attributes and Distinguished Name (DN) are used by Spring LDAP to construct a `DirContextAdapter`.
This lets us use a [`ContextMapper`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/core/ContextMapper.html) instead of an `AttributesMapper`
to transform found values, as follows:

Example 1. Searching using a ContextMapper

```java
public class PersonRepoImpl implements PersonRepo {...private static class PersonContextMapper implements ContextMapper {public Object mapFromContext(Object ctx) {DirContextAdapter context = (DirContextAdapter)ctx; Person p = new Person(); p.setFullName(context.getStringAttribute("cn")); p.setLastName(context.getStringAttribute("sn")); p.setDescription(context.getStringAttribute("description")); return p;}}
public Person findByPrimaryKey(String name, String company, String country) {Name dn = buildDn(name, company, country); return ldapClient.search().name(dn).map(new PersonContextMapper()).single();}}
```

As shown in the preceding example, we can retrieve the attribute values directly by name without having to go through the `Attributes` and `Attribute` classes.
This is particularly useful when working with multi-value attributes.
Extracting values from multi-value attributes normally requires looping through a `NamingEnumeration` of attribute values returned from the `Attributes` implementation.
`DirContextAdapter` does this for you
in the [`getStringAttributes()`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/core/DirContextAdapter.html#getStringAttributes(java.lang.String))
or [`getObjectAttributes()`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/core/DirContextAdapter.html#getObjectAttributes(java.lang.String)) methods.
The following example uses the `getStringAttributes` method:

Example 2. Getting multi-value attribute values using `getStringAttributes()`

```java
private static class PersonContextMapper implements ContextMapper {
   public Object mapFromContext(Object ctx) {
      DirContextAdapter context = (DirContextAdapter)ctx;
      Person p = new Person();
      p.setFullName(context.getStringAttribute("cn"));
      p.setLastName(context.getStringAttribute("sn"));
      p.setDescription(context.getStringAttribute("description"));
      // The roleNames property of Person is an String array
      p.setRoleNames(context.getStringAttributes("roleNames"));
      return p;
   }
}
```

<a id="dirobjectfactory--using-abstractcontextmapper"></a>

### Using `AbstractContextMapper`

Spring LDAP provides an abstract base implementation of `ContextMapper`, called [`AbstractContextMapper`](https://docs.spring.io/spring-ldap/docs/current/apidocs/org/springframework/ldap/core/support/AbstractContextMapper.html).
This implementation automatically takes care of the casting of the supplied `Object` parameter to `DirContexOperations`.
Using `AbstractContextMapper`, the `PersonContextMapper` shown earlier can thus be re-written as follows:

Example 3. Using an `AbstractContextMapper`

```java
private static class PersonContextMapper extends AbstractContextMapper {public Object doMapFromContext(DirContextOperations ctx) {Person p = new Person(); p.setFullName(ctx.getStringAttribute("cn")); p.setLastName(ctx.getStringAttribute("sn")); p.setDescription(ctx.getStringAttribute("description")); return p;}}
```

<a id="dirobjectfactory--adding-and-updating-data-by-using-dircontextadapter"></a>

## Adding and Updating Data by Using `DirContextAdapter`

`
While useful when extracting attribute values, `DirContextAdapter` is even more powerful for managing the details
involved in adding and updating data.

<a id="dirobjectfactory--adding-data-by-using-dircontextadapter"></a>

### Adding Data by Using `DirContextAdapter`

The following example uses `DirContextAdapter` to implement an improved implementation of the `create` repository method presented in [Adding Data](#spring-ldap-basic-usage--basic-binding-data):

Example 4. Binding using `DirContextAdapter`

```java
public class PersonRepoImpl implements PersonRepo {...public void create(Person p) {Name dn = buildDn(p); DirContextAdapter context = new DirContextAdapter(dn);
context.setAttributeValues("objectclass", new String[] {"top", "person"}); context.setAttributeValue("cn", p.getFullname()); context.setAttributeValue("sn", p.getLastname()); context.setAttributeValue("description", p.getDescription());
ldapClient.bind(dn).object(context).execute();}}
```

Note that we use the `DirContextAdapter` instance as the second parameter to bind, which should be a `Context`.
The third parameter is `null`, since we do not specify the attributes explicitly.

Also note the use of the `setAttributeValues()` method when setting the `objectclass` attribute values.
The `objectclass` attribute is multi-value. Similar to the troubles of extracting muti-value attribute data, building multi-value attributes is tedious and verbose work. By using the `setAttributeValues()` method, you can have `DirContextAdapter` handle that work for you.

<a id="dirobjectfactory--updating-data-by-using-dircontextadapter"></a>

### Updating Data by Using `DirContextAdapter`

We previously saw that updating by using `modifyAttributes` is the recommended approach, but that doing so requires us to perform
the task of calculating attribute modifications and constructing `ModificationItem` arrays accordingly.
`DirContextAdapter` can do all of this for us, as follows:

Example 5. Updating using `DirContextAdapter`

```java
public class PersonRepoImpl implements PersonRepo {...public void update(Person p) {Name dn = buildDn(p); DirContextOperations context = ldapClient.search().name(dn).single();
context.setAttributeValue("cn", p.getFullname()); context.setAttributeValue("sn", p.getLastname()); context.setAttributeValue("description", p.getDescription());
ldapClient.modify(dn).attributes(context.getModificationItems()).execute();}}
```

When calling `SearchSpec#single`, the result is a `DirContextAdapter` instance by default.
While the `lookup` method returns an `Object`, `single` automatically casts the return value to a `DirContextOperations`
(the interface that `DirContextAdapter` implements).

Notice that we have duplicate code in the `LdapTemplate#create` and `LdapTemplate#update` methods. This code maps from a domain object to a context. It can be extracted to a separate method, as follows:

Example 6. Adding and modifying using DirContextAdapter

```java
public class PersonRepoImpl implements PersonRepo {private LdapClient ldapClient;
...public void create(Person p) {Name dn = buildDn(p); DirContextAdapter context = new DirContextAdapter(dn);
context.setAttributeValues("objectclass", new String[] {"top", "person"}); mapToContext(p, context); ldapClient.bind(dn).object(context).execute();}
public void update(Person p) {Name dn = buildDn(p); DirContextOperations context = ldapClient.search().name(dn).single(); mapToContext(person, context); ldapClient.modify(dn).attributes(context.getModificationItems()).execute();}
protected void mapToContext (Person p, DirContextOperations context) {context.setAttributeValue("cn", p.getFullName()); context.setAttributeValue("sn", p.getLastName()); context.setAttributeValue("description", p.getDescription());}}
```

<a id="dirobjectfactory--dns-as-attribute-values"></a>
<a id="dirobjectfactory--dircontextadapter-and-distinguished-names-as-attribute-values"></a>

## `DirContextAdapter` and Distinguished Names as Attribute Values

When managing security groups in LDAP, it is common to have attribute values that represent
distinguished names. Since distinguished name equality differs from String equality (for example, whitespace and case differences
are ignored in distinguished name equality), calculating attribute modifications using string equality does not work as expected.

For instance, if a `member` attribute has a value of `cn=John Doe,ou=People` and we call `ctx.addAttributeValue("member", "CN=John Doe, OU=People")`, the attribute is now considered to have two values, even though the strings actually represent the same
distinguished name.

As of Spring LDAP 2.0, supplying `javax.naming.Name` instances to the attribute modification methods makes `DirContextAdapter`
use distinguished name equality when calculating attribute modifications. If we modify the earlier example to be
`ctx.addAttributeValue("member", LdapUtils.newLdapName("CN=John Doe, OU=People"))`, it does **not** render a modification, as the following example shows:

Example 7. Group Membership Modification using DirContextAdapter

```java
public class GroupRepo implements BaseLdapNameAware {
    private LdapClient ldapClient;
    private LdapName baseLdapPath;

    public void setLdapClient(LdapClient ldapClient) {
        this.ldapClient = ldapClient;
    }

    public void setBaseLdapPath(LdapName baseLdapPath) {
        this.setBaseLdapPath(baseLdapPath);
    }

    public void addMemberToGroup(String groupName, Person p) {
        Name groupDn = buildGroupDn(groupName);
        Name userDn = buildPersonDn(
            person.getFullname(),
            person.getCompany(),
            person.getCountry());

        DirContextOperation ctx = ldapClient.search().name(groupDn).single();
        ctx.addAttributeValue("member", userDn);

        ldapClient.modify(groupDn).attributes(ctx.getModificationItems()).execute();
    }

    public void removeMemberFromGroup(String groupName, Person p) {
        Name groupDn = buildGroupDn(String groupName);
        Name userDn = buildPersonDn(
            person.getFullname(),
            person.getCompany(),
            person.getCountry());

        DirContextOperation ctx = ldapClient.search().name(groupDn).single();
        ctx.removeAttributeValue("member", userDn);

        ldapClient.modify(groupDn).attributes(ctx.getModificationItems()).execute();
    }

    private Name buildGroupDn(String groupName) {
        return LdapNameBuilder.newInstance("ou=Groups")
            .add("cn", groupName).build();
    }

    private Name buildPersonDn(String fullname, String company, String country) {
        return LdapNameBuilder.newInstance(baseLdapPath)
            .add("c", country)
            .add("ou", company)
            .add("cn", fullname)
            .build();
   }
}
```

In the preceding example, we implement `BaseLdapNameAware` to get the base LDAP path as described in [Obtaining a Reference to the Base LDAP Path](#configuration--base-context-configuration).
This is necessary because distinguished names as member attribute values must always be absolute from the directory root.

<a id="dirobjectfactory--a-complete-personrepository-class"></a>

## A Complete `PersonRepository` Class

To illustrate the usefulness of Spring LDAP and `DirContextAdapter`, the following example shows a complete `Person` Repository implementation for LDAP:

```java
import java.util.List;

import javax.naming.Name;
import javax.naming.NamingException;
import javax.naming.directory.Attributes;
import javax.naming.ldap.LdapName;

import org.springframework.ldap.core.AttributesMapper;
import org.springframework.ldap.core.ContextMapper;
import org.springframework.ldap.core.LdapTemplate;
import org.springframework.ldap.core.DirContextAdapter;
import org.springframework.ldap.filter.AndFilter;
import org.springframework.ldap.filter.EqualsFilter;
import org.springframework.ldap.filter.WhitespaceWildcardsFilter;

import static org.springframework.ldap.query.LdapQueryBuilder.query;

public class PersonRepoImpl implements PersonRepo {
   private LdapClient ldapClient;

   public void setLdapClient(LdapClient ldapClient) {
      this.ldapClient = ldapClient;
   }

   public void create(Person person) {
      DirContextAdapter context = new DirContextAdapter(buildDn(person));
      mapToContext(person, context);
      ldapClient.bind(context.getDn()).object(context).execute();
   }

   public void update(Person person) {
      Name dn = buildDn(person);
      DirContextOperations context = ldapClient.lookupContext(dn);
      mapToContext(person, context);
      ldapClient.modify(dn).attributes(context.getModificationItems()).execute();
   }

   public void delete(Person person) {
      ldapClient.unbind(buildDn(person)).execute();
   }

   public Person findByPrimaryKey(String name, String company, String country) {
      Name dn = buildDn(name, company, country);
      return ldapClient.search().name(dn).map(getContextMapper()).single();
   }

   public List<Person> findByName(String name) {
      LdapQuery query = query()
         .where("objectclass").is("person")
         .and("cn").whitespaceWildcardsLike("name");

      return ldapClient.search().query(query).map(getContextMapper()).list();
   }

   public List<Person> findAll() {
      EqualsFilter filter = new EqualsFilter("objectclass", "person");
      return ldapClient.search().query((query) -> query.filter(filter)).map(getContextMapper()).list();
   }

   protected ContextMapper getContextMapper() {
      return new PersonContextMapper();
   }

   protected Name buildDn(Person person) {
      return buildDn(person.getFullname(), person.getCompany(), person.getCountry());
   }

   protected Name buildDn(String fullname, String company, String country) {
      return LdapNameBuilder.newInstance()
        .add("c", country)
        .add("ou", company)
        .add("cn", fullname)
        .build();
   }

   protected void mapToContext(Person person, DirContextOperations context) {
      context.setAttributeValues("objectclass", new String[] {"top", "person"});
      context.setAttributeValue("cn", person.getFullName());
      context.setAttributeValue("sn", person.getLastName());
      context.setAttributeValue("description", person.getDescription());
   }

   private static class PersonContextMapper extends AbstractContextMapper<Person> {
      public Person doMapFromContext(DirContextOperations context) {
         Person person = new Person();
         person.setFullName(context.getStringAttribute("cn"));
         person.setLastName(context.getStringAttribute("sn"));
         person.setDescription(context.getStringAttribute("description"));
         return person;
      }
   }
}
```

> [!NOTE]
> In several cases, the Distinguished Name (DN) of an object is constructed by using properties of the object.
> In the preceding example, the country, company and full name of the `Person` are used in the DN, which means that updating any of these properties actually requires moving the entry in the LDAP tree by using the `rename()` operation in addition to updating the `Attribute` values.
> Since this is highly implementation-specific, this is something you need to keep track of yourself, either by disallowing the user to change these properties or performing the `rename()` operation in your `update()` method if needed.
> Note that, by using [Object-Directory Mapping (ODM)](#odm), the library can automatically handle this for you if you annotate your domain classes appropriately.

[Basic Usage](#spring-ldap-basic-usage)
[Object-Directory Mapping (ODM)](#odm)

---

<a id="odm"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/odm.html -->

<!-- page_index: 7 -->

# Object-Directory Mapping (ODM)

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="odm--page-title"></a>
<a id="odm--object-directory-mapping-odm"></a>

# Object-Directory Mapping (ODM)

Object-relational mapping frameworks (such as Hibernate and JPA) offer developers the ability to use annotations to map relational database tables to Java objects.
The Spring LDAP project offers a similar ability with respect to LDAP directories through a number of methods in `LdapOperations`:

- `<T> T findByDn(Name dn, Class<T> clazz)`
- `<T> T findOne(LdapQuery query, Class<T> clazz)`
- `<T> List<T> find(LdapQuery query, Class<T> clazz)`
- `<T> List<T> findAll(Class<T> clazz)`
- `<T> List<T> findAll(Name base, SearchControls searchControls, Class<T> clazz)`
- `<T> List<T> findAll(Name base, Filter filter, SearchControls searchControls, Class<T> clazz)`
- `void create(Object entry)`
- `void update(Object entry)`
- `void delete(Object entry)`

<a id="odm--configuration"></a>

## Configuration

`LdapTemplate` constructs a default `ObjectDirectoryMapper` which typically renders additional configuration unnecessary.

<a id="odm--_converters_with_boot"></a>
<a id="odm--converters-with-boot"></a>

### Converters with Boot

`ObjectDirectoryMapper` supports `ConversionService` which allows you to specify customer `Converter`s for mapping between Java and LDAP.

When you are using Spring Boot, you can simply publish a `Converter` as you would normally and the `ObjectDirectoryMapper` bean that Boot provides will pick them up.

<a id="odm--_converters_without_boot"></a>
<a id="odm--converters-without-boot"></a>

### Converters without Boot

You can also make `ObjectDirectoryMapper` available as a `@Bean` by importing `ObjectDirectoryMapperConfiguration` like so:

```java
@Import(ObjectDirectoryMapperConfiguration.class)
@Configuration
public class LdapConfig {
	// ...
}
```

You can then supply it to your `LdapTemplate` instance as follows:

```java
@Bean
LdapTemplate ldapTemplate(ContextSource contextSource, ObjectDirectoryMapper odm) {
	LdapTemplate ldap = new LdapTemplate(contextSource);
	ldap.setObjectDirectoryMapper(odm);
	return ldap;
}
```

Doing so will make so that Spring LDAP will use your configured `Converter` instances.

<a id="odm--annotations"></a>

## Annotations

Entity classes managed with the object mapping methods are required to be annotated with annotations from the `org.springframework.ldap.odm.annotations` package. The available annotations are:

- `@Entry`: Class level annotation indicating the `objectClass` definitions to which the entity maps. *(required)*
- `@Id`: Indicates the entity DN. The field declaring this attribute must be a derivative of the `javax.naming.Name` class. (required)
- `@Attribute`: Indicates the mapping of a directory attribute to the object class field.
- `@DnAttribute`: Indicates the mapping of a DN attribute to the object class field.
- `@Transient`: Indicates the field is not persistent and should be ignored by the `OdmManager`.

The `@Entry` and `@Id` annotations are required to be declared on managed classes.
`@Entry` is used to specify which object classes the entity maps to and (optionally) the directory root of the LDAP entries represented by the class.
All object classes for which fields are mapped are required to be declared. Note that, when creating new entries of the managed class, only the declared object classes are used.

In order for a directory entry to be considered a match to the managed entity, all object classes declared by the directory entry must be declared by the `@Entry` annotation.
For example, assume that you have entries in your LDAP tree that have the following object classes: `inetOrgPerson,organizationalPerson,person,top`.
If you are interested only in changing the attributes defined in the `person` object class, you can annotate your `@Entry` with `@Entry(objectClasses = { "person", "top" })`.
However, if you want to manage attributes defined in the `inetOrgPerson` objectclass, you need to use the following: `@Entry(objectClasses = { "inetOrgPerson", "organizationalPerson", "person", "top" })`.

All entity fields are mapped by their field name to LDAP attributes. The remaining annotations — `@Id`, `@Attribute`, `@Transient`, and `@DnAttribute` — affect how that mapping occurs.

First, the `@Id` annotation maps the distinguished name of the entry to a field. The field must be an instance of `javax.naming.Name`.

Second, the `@Attribute` annotation maps entity fields to LDAP attributes.
This is handy when the attribute name is different from the field name.
To use `@Attribute`, you must declare the name of the attribute to which the field maps.
Optionally, you can also guarantee and exact match by including the syntax OID of the LDAP attribute.
Finally, `@Attribute` also provides the type declaration, which lets you indicate whether the attribute is regarded as binary- or string-based by the LDAP JNDI provider.

Third, the `@Transient` annotation indicates that the given entity field does not map to an LDAP attribute.

Finally, the `@DnAttribute` annotation additionally maps entity fields to components of an entry’s distinguished name.

Consider a class with the following annotation:

```java
@DnAttribute(name="uid")
String uid;
```

and a DN like the following:

```bash
uid=carla,dc=springframework,dc=org
```

Then Spring LDAP will populate `uid` using `uid=carla` instead of looking for a `uid` attribute.

```
Only fields of type `String` can be annotated with `@DnAttribute`. Other types are not supported.
```

You can alternatively supply an index like so:

```java
@DnAttribute(index=1)
String uid;

@DnAttribute(index=0)
String department;
```

which is handy for DNs that have multiple components:

```bash
uid=carla,department=engineering,dc=springframework,dc=org
```

Using an `index` also allows Spring LDAP to compute the DN for you when creating or locating an entity for update or deletion.
For update scenarios, this also automatically takes care of moving entries in the tree if attributes that are part of the distinguished name have changed.

```
Note that while both attributes are present on `@DnAttribute`, if `index` is specified, then `name` is ignored.
```

> [!NOTE]
> Remember that all fields are mapped to LDAP attributes by default.
> `@DnAttribute` does not change this; in other words, fields annotated with `@DnAttribute` will also map to an LDAP attribute, unless you also annotate the field with `@Transient`.

<a id="odm--execution"></a>

## Execution

When all components have been properly configured and annotated, the object mapping methods of `LdapTemplate` can be used as follows:

Example 1. Execution

```java
@Entry(objectClasses = { "person", "top" }, base="ou=someOu") public class Person {@Id private Name dn;
@Attribute(name="cn") @DnAttribute(value="cn", index=1) private String fullName;
// No @Attribute annotation means this will be bound to the LDAP attribute // with the same value private String description;
@DnAttribute(value="ou", index=0) @Transient private String company;
@Transient private String someUnmappedField; // ...more attributes below}
public class OdmPersonRepo {@Autowired private LdapTemplate ldapTemplate;
public Person create(Person person) {ldapTemplate.create(person); return person;}
public Person findByUid(String uid) {return ldapTemplate.findOne(query().where("uid").is(uid), Person.class);}
public void update(Person person) {ldapTemplate.update(person);}
public void delete(Person person) {ldapTemplate.delete(person);}
public List<Person> findAll() {return ldapTemplate.findAll(Person.class);}
public List<Person> findByLastName(String lastName) {return ldapTemplate.find(query().where("sn").is(lastName), Person.class);}
public Stream<Person> streamFindByLastName(String lastName) {return ldapTemplate.findStream(query().where("sn").is(lastName), Person.class);}}
```

<a id="odm--odm-dn-attributes"></a>
<a id="odm--odm-and-distinguished-names-as-attribute-values"></a>

## ODM and Distinguished Names as Attribute Values

Security groups in LDAP commonly contain a multi-value attribute, where each of the values is the distinguished name
of a user in the system. The difficulties involved when handling these kinds of attributes are discussed in [`DirContextAdapter` and Distinguished Names as Attribute Values](#dirobjectfactory--dns-as-attribute-values).

ODM also has support for `javax.naming.Name` attribute values, making group modifications easy, as the following example shows:

Example 2. Example Group representation

```java
@Entry(objectClasses = {"top", "groupOfUniqueNames"}, base = "cn=groups") public class Group {
@Id private Name dn;
@Attribute(name="cn") @DnAttribute("cn") private String name;
@Attribute(name="uniqueMember") private Set<Name> members;
public Name getDn() {return dn;}
public void setDn(Name dn) {this.dn = dn;}
public Set<Name> getMembers() {return members;}
public void setMembers(Set<Name> members) {this.members = members;}
public String getName() {return name;}
public void setName(String name) {this.name = name;}
public void addMember(Name member) {members.add(member);}
public void removeMember(Name member) {members.remove(member);}}
```

When you modify group members by using `setMembers`, `addMember`, and `removeMember` and then calling `ldapTemplate.update()`, attribute modifications are calculated by using distinguished name equality, meaning that the text formatting of
distinguished names is disregarded when figuring out whether they are equal.

[Simplifying Attribute Access and Manipulation with `DirContextAdapter`](#dirobjectfactory)
[Advanced LDAP Queries](#query-builder-advanced)

---

<a id="query-builder-advanced"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/query-builder-advanced.html -->

<!-- page_index: 8 -->

# Advanced LDAP Queries

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="query-builder-advanced--page-title"></a>
<a id="query-builder-advanced--advanced-ldap-queries"></a>

# Advanced LDAP Queries

This section covers various how to use LDAP queries with Spring LDAP.

<a id="query-builder-advanced--ldap-query-builder-parameters"></a>

## LDAP Query Builder Parameters

The `LdapQueryBuilder` and its associated classes are intended to support all of the parameters that can be supplied to an LDAP search.
The following parameters are supported:

- `base`: Specifies the root DN in the LDAP tree where the search should start.
- `searchScope`: Specifies how deep into the LDAP tree the search should traverse.
- `attributes`: Specifies the attributes to return from the search. The default is all.
- `countLimit`: Specifies the maximum number of entries to return from the search.
- `timeLimit`: Specifies the maximum time that the search may take.
- Search filter: The conditions that the entries we are looking for must meet.

An `LdapQueryBuilder` is created with a call to the `query` method of `LdapQueryBuilder`. It is intended as a fluent builder API, where the base parameters are defined first, followed by the filter specification calls. Once filter conditions have been started to be defined with a call to the `where` method of `LdapQueryBuilder`, later attempts to call (for example) `base` are rejected. The base search parameters are optional, but at least one filter specification call is required.
The following query searches for all entries with an object class of `Person`:

Example 1. Search for all entries with object class `Person`

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
...

List<Person> persons = ldapClient.search()
      .query(query().where("objectclass").is("person"))
      .map(new PersonAttributesMapper()).list();
```

The following query searches for all entries with an object class of `person` and a `cn` (common name) of `John Doe`:

Example 2. Search for all entries with object class `person` and `cn=John Doe`

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
...

List<Person> persons = ldapClient.search()
      .query(query().where("objectclass").is("person").and("cn").is("John Doe"))
      .map(new PersonAttributesMapper()).list();
```

The following query searches for all entries with an object class of `person` and starting at a `dc` (domain component) of `dc=261consulting,dc=com`:

Example 3. Search for all entries with object class `person` starting at `dc=261consulting,dc=com`

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
...

List<Person> persons = ldapClient.search()
      .query(query().base("dc=261consulting,dc=com").where("objectclass").is("person"))
      .map(new PersonAttributesMapper()).list();
```

The following query returns the `cn` (common name) attribute for all entries with an object class of `person` and starting at a `dc` (domain component) of `dc=261consulting,dc=com`:

Example 4. Search for all entries with class `Person` starting at `dc=261consulting,dc=com`, returning only the `cn` attribute

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
...

Stream<Person> persons = ldapClient.search()
      .query(query().base("dc=261consulting,dc=com")
             .attributes("cn")
             .where("objectclass").is("person")),
      .map(new PersonAttributesMapper()).stream();
```

The following query uses `or` to search for multiple spellings of a common name (`cn`):

Example 5. Search with `or` criteria

```java
import static org.springframework.ldap.query.LdapQueryBuilder.query;
...
Stream<Person> persons = ldapClient.search()
      .query(query().where("objectclass").is("person"),
             .and(query().where("cn").is("Doe").or("cn").is("Doo"))
      .map(new PersonAttributesMapper()).stream();
```

<a id="query-builder-advanced--filter-criteria"></a>

## Filter Criteria

The earlier examples demonstrate simple equals conditions in LDAP filters. The LDAP query builder has support for the following criteria types:

- `is`: Specifies an equals (=) condition.
- `gte`: Specifies a greater-than-or-equals (>=) condition.
- `lte`: Specifies a less-than-or-equals (⇐) condition.
- `like`: Specifies a “like” condition where wildcards can be included in the query — for example, `where("cn").like("J*hn Doe")` results in the following filter: `(cn=J*hn Doe)`.
- `whitespaceWildcardsLike`: Specifies a condition where all whitespace is replaced with wildcards — for example, `where("cn").whitespaceWildcardsLike("John Doe")` results in the following filter: `(cn=John*Doe)`.
- `isPresent`: Specifies a condition that checks for the presence of an attribute — for example, `where("cn").isPresent()` results in the following filter: `(cn=*)`.
- `not`: Specifies that the current condition should be negated — for example, `where("sn").not().is("Doe)` results in the following filter: `(!(sn=Doe))`

<a id="query-builder-advanced--hardcoded-filters"></a>

## Hardcoded Filters

There may be occasions when you want to specify a hardcoded filter as input to an `LdapQuery`. `LdapQueryBuilder` has two methods for this purpose:

- `filter(String hardcodedFilter)`: Uses the specified string as a filter. Note that the specified input string is not touched in any way, meaning that this method is not particularly well suited if you are building filters from user input.
- `filter(String filterFormat, String… params)`: Uses the specified string as input to `MessageFormat`, properly encoding the parameters and inserting them at the specified places in the filter string.
- `filter(Filter filter)`: Uses the specified filter.

You cannot mix the hardcoded filter methods with the `where` approach described earlier. It is either one or the other. If you specify a filter by using `filter()`, you get an exception if you try to call `where` afterwards.

[Object-Directory Mapping (ODM)](#odm)
[Configuration](#configuration)

---

<a id="configuration"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/configuration.html -->

<!-- page_index: 9 -->

# Configuration

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="configuration--page-title"></a>
<a id="configuration--configuration"></a>

# Configuration

The recommended way of configuring Spring LDAP is to use the custom XML configuration namespace. To make this available, you need to include the Spring LDAP namespace declaration in your bean file, as follows:

```java
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:ldap="http://www.springframework.org/schema/ldap"
       xsi:schemaLocation="http://www.springframework.org/schema/beans https://www.springframework.org/schema/beans/spring-beans.xsd
       http://www.springframework.org/schema/ldap https://www.springframework.org/schema/ldap/spring-ldap.xsd">
```

<a id="configuration--contextsource-configuration"></a>

## `ContextSource` Configuration

`ContextSource` is defined by using an `<ldap:context-source>` tag.
The simplest possible `context-source` declaration requires you to specify a server URL, a username, and a password, as follows:

Example 1. Simplest possible context-source declaration

```java
<ldap:context-source
    username="cn=Administrator"
    password="secret"
    url="ldap://localhost:389" />
```

The preceding example creates an `LdapContextSource` with default values (see the table after this paragraph) and the URL and authentication credentials as specified.
The configurable attributes on context-source are as follows (required attributes marked with \*):

<table class="tableblock frame-all grid-all stretch">
<caption>Table 1. ContextSource Configuration Attributes</caption>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>id</code></p></td>
<td><p><code>contextSource</code></p></td>
<td><p>The ID of the created bean.</p></td>
</tr>
<tr>
<td><p><code>username</code></p></td>
<td></td>
<td><p>The username (principal) to use when authenticating with the LDAP server.
   This is usually the distinguished name of an admin user (for example, <code>cn=Administrator</code>) but may differ depending on server and authentication method.
   Required if <code>authentication-source-ref</code> is not explicitly configured.</p></td>
</tr>
<tr>
<td><p><code>password</code></p></td>
<td></td>
<td><p>The password (credentials) to use when authenticating with the LDAP server. Required if <code>authentication-source-ref</code> is not explicitly configured.</p></td>
</tr>
<tr>
<td><p><code>url</code> *</p></td>
<td></td>
<td><p>The URL of the LDAP server to use. The URL should be in the following format: <code>ldap://myserver.example.com:389</code>.
   For SSL access, use the <code>ldaps</code> protocol and the appropriate port — for example, <code>ldaps://myserver.example.com:636</code>.
   If you want fail-over functionality, you can specify more than one URL, separated by commas (<code>,</code>).</p></td>
</tr>
<tr>
<td><p><code>base</code></p></td>
<td><p><code>LdapUtils.emptyLdapName()</code></p></td>
<td><p>The base DN. When this attribute has been configured, all Distinguished Names supplied to and received from LDAP operations are relative to the specified LDAP path.
   This can significantly simplify working against the LDAP tree. However, there are several occasions when you need to have access to the base path.
   For more information on this, see <a href="#configuration--base-context-configuration">Obtaining a Reference to the Base LDAP Path</a></p></td>
</tr>
<tr>
<td><p><code>anonymous-read-only</code></p></td>
<td><p><code>false</code></p></td>
<td><p>Defines whether read-only operations are performed by using an anonymous (unauthenticated) context.
   Note that setting this parameter to <code>true</code> together with the compensating transaction support is not supported and is rejected.</p></td>
</tr>
<tr>
<td><p><code>referral</code></p></td>
<td><p><code>null</code></p></td>
<td><div><div>
<p>Defines the strategy with which to handle referrals, as described <a href="https://docs.oracle.com/javase/jndi/tutorial/ldap/referral/jndi.html">here</a>. The valid values are:</p>
</div>
<div>
<ul>
<li>
<p><code>ignore</code></p>
</li>
<li>
<p><code>follow</code></p>
</li>
<li>
<p><code>throw</code></p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td><p><code>native-pooling</code></p></td>
<td><p><code>false</code></p></td>
<td><p>Specify whether native Java LDAP connection pooling should be used. Consider using Spring LDAP connection pooling instead. See <a href="#pooling">Pooling Support</a> for more information.</p></td>
</tr>
<tr>
<td><p><code>authentication-source-ref</code></p></td>
<td><p>A <code>SimpleAuthenticationSource</code> instance.</p></td>
<td><p>ID of the <code>AuthenticationSource</code> instance to use (see <a href="#configuration--spring-ldap-custom-principal-credentials-management">Custom Principal and Credentials Management</a>).</p></td>
</tr>
<tr>
<td><p><code>authentication-strategy-ref</code></p></td>
<td><p>A <code>SimpleDirContextAuthenticationStrategy</code> instance.</p></td>
<td><p>ID of the <code>DirContextAuthenticationStrategy</code> instance to use (see <a href="#configuration--spring-ldap-custom-dircontext-authentication-processing">Custom <code>DirContext</code> Authentication Processing</a>).</p></td>
</tr>
<tr>
<td><p><code>base-env-props-ref</code></p></td>
<td></td>
<td><p>A reference to a <code>Map</code> of custom environment properties that should supplied with the environment sent to the <code>DirContext</code> on construction.</p></td>
</tr>
</tbody>
</table>

<a id="configuration--dircontext-authentication"></a>

### `DirContext` Authentication

When `DirContext` instances are created to be used for performing operations on an LDAP server, these contexts often need to be authenticated.
Spring LDAP offers various options for configuring this.

> [!NOTE]
> This section refers to authenticating contexts in the core functionality of the `ContextSource`, to construct `DirContext` instances for use by `LdapClient` and `LdapTemplate`. LDAP is commonly used for the sole purpose of user authentication, and the `ContextSource` may be used for that as well. That process is discussed in [User Authentication using Spring LDAP](#user-authentication).

By default, authenticated contexts are created for both read-only and read-write operations. You should specify the `username` and `password` of the LDAP user to be used for authentication on the `context-source` element.

> [!NOTE]
> If `username` is the Distinguished Name (DN) of an LDAP user, it needs to be the full DN of the user from the root of the LDAP tree, regardless of whether a `base` LDAP path has been specified on the `context-source` element.

Some LDAP server setups allow anonymous read-only access. If you want to use anonymous contexts for read-only operations, set the `anonymous-read-only` attribute to `true`.

<a id="configuration--spring-ldap-custom-dircontext-authentication-processing"></a>
<a id="configuration--custom-dircontext-authentication-processing"></a>

#### Custom `DirContext` Authentication Processing

The default authentication mechanism used in Spring LDAP is `SIMPLE` authentication. This means that the principal (as specified by the `username` attribute) and the credentials (as specified by the `password`) are set in the `Hashtable` that is sent to the `DirContext` implementation constructor.

There are many occasions when this processing is not sufficient. For instance, LDAP Servers are commonly set up to accept communication only on a secure TLS channel. There might be a need to use the particular LDAP Proxy Auth mechanism or other concerns.

You can specify an alternative authentication mechanism by supplying a `DirContextAuthenticationStrategy` implementation reference to the `context-source` element. To do so, set the `authentication-strategy-ref` attribute.

<a id="configuration--tls"></a>

##### TLS

Spring LDAP provides two different configuration options for LDAP servers that require TLS secure channel communication: `DefaultTlsDirContextAuthenticationStrategy` and `ExternalTlsDirContextAuthenticationStrategy`.
Both implementations negotiate a TLS channel on the target connection, but they differ in the actual authentication mechanism.
Where `DefaultTlsDirContextAuthenticationStrategy` applies SIMPLE authentication on the secure channel (by using the specified `username` and `password`), the `ExternalTlsDirContextAuthenticationStrategy` uses EXTERNAL SASL authentication, applying a client certificate that is configured by using system properties for authentication.

Since different LDAP server implementations respond differently to explicit shutdown of the TLS channel (some servers require the connection be shut down gracefully, while others do not support it), the TLS `DirContextAuthenticationStrategy` implementations support specifying the shutdown behavior by using the `shutdownTlsGracefully` parameter. If this property is set to `false` (the default), no explicit TLS shutdown happens. If it is `true`, Spring LDAP tries to shut down the TLS channel gracefully before closing the target context.

> [!NOTE]
> When working with TLS connections, you need to make sure that the native LDAP Pooling functionality (as specified by using the `native-pooling` attribute) is turned off. This is particularly important if `shutdownTlsGracefully` is set to `false`. However, since the TLS channel negotiation process is quite expensive, you can gain great performance benefits by using the Spring LDAP Pooling Support, described in [Pooling Support](#pooling).

<a id="configuration--spring-ldap-custom-principal-credentials-management"></a>
<a id="configuration--custom-principal-and-credentials-management"></a>

#### Custom Principal and Credentials Management

While the user name (that is, the user DN) and password used for creating an authenticated `Context` are statically defined by default (the ones defined in the `context-source` element configuration are used throughout the lifetime of the `ContextSource`), there are several cases where this is not the desired behavior. A common scenario is that the principal and credentials of the current user should be used when performing LDAP operations for that user. You can modify the default behavior by supplying a reference to an `AuthenticationSource` implementation to the `context-source` element by using the `authentication-source-ref` element, instead of explicitly specifying the `username` and `password`. The `AuthenticationSource` is queried by the `ContextSource` for principal and credentials each time an authenticated `Context` is to be created.

If you use [Spring Security](https://spring.io/spring-security), you can make sure the principal and credentials of the currently logged-in user are used at all times by configuring your `ContextSource` with an instance of the `SpringSecurityAuthenticationSource` shipped with Spring Security. The following example shows how to do so:

Example 2. Using the SpringSecurityAuthenticationSource

```java
<beans> ...<ldap:context-source url="ldap://localhost:389" authentication-source-ref="springSecurityAuthenticationSource"/>
<bean id="springSecurityAuthenticationSource" class="org.springframework.security.ldap.authentication.SpringSecurityAuthenticationSource" /> ...</beans>
```

> [!NOTE]
> We do not specify any `username` or `password` for. our `context-source` when using an `AuthenticationSource`. These properties are needed only when the default behavior is used.

> [!NOTE]
> When using the `SpringSecurityAuthenticationSource`, you need to use Spring Security’s `LdapAuthenticationProvider` to authenticate the users against LDAP.

<a id="configuration--native-java-ldap-pooling"></a>

### Native Java LDAP Pooling

The internal Java LDAP provider provides some very basic pooling capabilities. You can turn this LDAP connection pooling on or off by using the `pooled` flag on `AbstractContextSource`. The default value is `false` (since release 1.3) — that is, the native Java LDAP pooling is turned off. The configuration of LDAP connection pooling is managed by using `System` properties, so you need to handle this manually, outside of the Spring Context configuration. You can find details of the native pooling configuration [here](https://java.sun.com/products/jndi/tutorial/ldap/connect/config.html).

> [!NOTE]
> There are several serious deficiencies in the built-in LDAP connection pooling, which is why Spring LDAP provides a more sophisticated approach to LDAP connection pooling, described in [Pooling Support](#pooling). If you need pooling functionality, this is the recommended approach.

> [!NOTE]
> Regardless of the pooling configuration, the `ContextSource#getContext(String principal, String credentials)` method always explicitly does not use native Java LDAP Pooling, in order for reset passwords to take effect as soon as possible.

<a id="configuration--advanced-contextsource-configuration"></a>

### Advanced `ContextSource` Configuration

This section covers more advanced ways to configure a `ContextSource`.

<a id="configuration--custom-dircontext-environment-properties"></a>

#### Custom `DirContext` Environment Properties

In some cases, you might want to specify additional environment setup properties, in addition to the ones directly configurable on `context-source`. You should set such properties in a `Map` and reference them in the `base-env-props-ref` attribute.

<a id="configuration--ldapclient-configuration"></a>

## `LdapClient` Configuration

`LdapClient` is the new interface for calling an LDAP backend. It improves upon `LdapTemplate` in the following ways:

- Provides built-in `Stream` support
- Provides a simplified API centered around bind ©, search ®, modify (U), unbind (D), and authenticate.

> [!NOTE]
> `LdapClient` does not yet support ODM.
> If this is something you need, `LdapTemplate` has this capacity.
> Both `LdapClient` and `LdapTemplate` can coexist quite nicely in the same application, if needed.

An `LdapClient` is defined by using the `LdapClient#create` factory method like so:

Example 3. Simplest possible LdapClient declaration

```xml
<bean id="ldapClient" class="org.springframework.ldap.core.LdapClient" factory-method="create">
   <constructor-arg ref="contextSource" />
</bean>
```

This element references the default `ContextSource`, which is expected to have an ID of `contextSource` (the default for the `context-source` element).

Your `LdapClient` instance can be configured for how to handle certain checked exceptions and what any default `SearchControls` should be used for queries.

<a id="configuration--ldaptemplate-configuration"></a>

## `LdapTemplate` Configuration

The `LdapTemplate` is defined by using a `<ldap:ldap-template>` element. The simplest possible `ldap-template` declaration is the element by itself:

Example 4. Simplest possible ldap-template declaration

```java
<ldap:ldap-template />
```

The element by itself creates an `LdapTemplate` instance with the default ID, referencing the default `ContextSource`, which is expected to have an ID of `contextSource` (the default for the `context-source` element).

The following table describes the configurable attributes on `ldap-template`:

<table class="tableblock frame-all grid-all stretch">
<caption>Table 2. LdapTemplate Configuration Attributes</caption>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>id</code></p></td>
<td><p><code>ldapTemplate</code></p></td>
<td><div><div>
<p>The ID of the created bean.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>context-source-ref</code></p></td>
<td><p><code>contextSource</code></p></td>
<td><div><div>
<p>The ID of the <code>ContextSource</code> instance to use.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>count-limit</code></p></td>
<td><p><code>0</code></p></td>
<td><div><div>
<p>The default count limit for searches. 0 means no limit.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>time-limit</code></p></td>
<td><p><code>0</code></p></td>
<td><div><div>
<p>The default time limit for searches, in milliseconds. 0 means no limit.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>search-scope</code></p></td>
<td><p><code>SUBTREE</code></p></td>
<td><div><div>
<p>The default search scope for searches. The valid values are:</p>
</div>
<div>
<ul>
<li>
<p><code>OBJECT</code></p>
</li>
<li>
<p><code>ONELEVEL</code></p>
</li>
<li>
<p><code>SUBTREE</code></p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td><p><code>ignore-name-not-found</code></p></td>
<td><p><code>false</code></p></td>
<td><div><div>
<p>Specifies whether a <code>NameNotFoundException</code> should be ignored in searches. Setting this attribute to <code>true</code> make errors that are caused by an invalid search base be silently swallowed.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>ignore-partial-result</code></p></td>
<td><p><code>false</code></p></td>
<td><div><div>
<p>Specifies whether <code>PartialResultException</code> should be ignored in searches. Some LDAP servers have problems with referrals. These should normally be followed automatically. However, if this does not work, it manifests itself with a <code>PartialResultException</code>. Setting this attribute to <code>true</code> presents a work-around to this problem.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>odm-ref</code></p></td>
<td></td>
<td><div><div>
<p>The ID of the <code>ObjectDirectoryMapper</code> instance to use. The default is a default-configured <code>DefaultObjectDirectoryMapper</code>.</p>
</div></div></td>
</tr>
</tbody>
</table>

<a id="configuration--base-context-configuration"></a>
<a id="configuration--obtaining-a-reference-to-the-base-ldap-path"></a>

## Obtaining a Reference to the Base LDAP Path

As described earlier, you can supply a base LDAP path to the `ContextSource`, specifying the root in the LDAP tree to which all operations are relative. This means that you are working only with relative distinguished names throughout your system, which is typically rather handy. There are, however, some cases in which you may need to have access to the base path in order to be able to construct full DNs, relative to the actual root of the LDAP tree. One example would be when working with LDAP groups (for example, the `groupOfNames` object class). In that case, each group member attribute value needs to be the full DN of the referenced member.

For that reason, Spring LDAP has a mechanism by which any Spring-controlled bean may be supplied with the base path on startup.
For beans to be notified of the base path, two things need to be in place. First, the bean that wants the base path reference needs to implement the `BaseLdapNameAware` interface.
Second, you need to define a `BaseLdapPathBeanPostProcessor` in the application context.
The following example shows how to implement `BaseLdapNameAware`:

Example 5. Implementing `BaseLdapNameAware`

```java
public class PersonService implements PersonService, BaseLdapNameAware {...private LdapName basePath;
public void setBaseLdapPath(LdapName basePath) {this.basePath = basePath;} ...private LdapName getFullPersonDn(Person person) {return LdapNameBuilder.newInstance(basePath) .add(person.getDn()) .build();} ...}
```

The following example shows how to define a `BaseLdapPathBeanPostProcessor`:

Example 6. Specifying a BaseLdapPathBeanPostProcessor in your ApplicationContext

```java
<beans>
   ...
   <ldap:context-source
          username="cn=Administrator"
          password="secret"
          url="ldap://localhost:389"
          base="dc=261consulting,dc=com" />
   ...
   <bean class="org.springframework.ldap.core.support.BaseLdapPathBeanPostProcessor" />
</beans>
```

The default behavior of the `BaseLdapPathBeanPostProcessor` is to use the base path of the single defined `BaseLdapPathSource` (`AbstractContextSource`) in the `ApplicationContext`. If more than one `BaseLdapPathSource` is defined, you need to specify which one to use by setting the `baseLdapPathSourceName` property.

[Advanced LDAP Queries](#query-builder-advanced)
[Spring LDAP Repositories](#repositories)

---

<a id="repositories"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/repositories.html -->

<!-- page_index: 10 -->

# Spring LDAP Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="repositories--page-title"></a>
<a id="repositories--spring-ldap-repositories"></a>

# Spring LDAP Repositories

Spring LDAP has built-in support for Spring Data repositories. The basic functionality and configuration is described [here](https://docs.spring.io/spring-data/data-commons/docs/current/reference/html/#repositories). When working with Spring LDAP repositories, you should remember the following:

- You can enable Spring LDAP repositories by using an `<ldap:repositories>` element in your XML configuration or by using an `@EnableLdapRepositories` annotation on a configuration class.
- To include support for `LdapQuery` parameters in automatically generated repositories, have your interface extend `LdapRepository` rather than `CrudRepository`.
- All Spring LDAP repositories must work with entities that are annotated with the ODM annotations, as described in [Object-Directory Mapping (ODM)](#odm).
- Since all ODM managed classes must have a Distinguished Name as the ID, all Spring LDAP repositories must have the ID type parameter set to `javax.naming.Name`.
  The built-in `LdapRepository` takes only one type parameter: the managed entity class, defaulting the ID to `javax.naming.Name`.
- Due to specifics of the LDAP protocol, paging and sorting are not supported for Spring LDAP repositories.

<a id="repositories--querydsl-support"></a>

## QueryDSL support

Basic QueryDSL support is included in Spring LDAP. This support includes the following:

- An annotation processor, called `LdapAnnotationProcessor`, for generating QueryDSL classes based on Spring LDAP ODM annotations. See [Object-Directory Mapping (ODM)](#odm) for more information on the ODM annotations.
- A Query implementation, called `QueryDslLdapQuery`, for building and running QueryDSL queries in code.
- Spring Data repository support for QueryDSL predicates. `QueryDslPredicateExecutor` includes a number of additional methods with appropriate parameters. You can extend this interface along with `LdapRepository` to include this support in your repository.

[Configuration](#configuration)
[Pooling Support](#pooling)

---

<a id="pooling"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/pooling.html -->

<!-- page_index: 11 -->

# Pooling Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="pooling--page-title"></a>
<a id="pooling--pooling-support"></a>

# Pooling Support

Pooling LDAP connections helps mitigate the overhead of creating a new LDAP connection for each LDAP interaction. While [Java LDAP pooling support](https://java.sun.com/products/jndi/tutorial/ldap/connect/pool.html) exists, it is limited in its configuration options and features, such as connection validation and pool maintenance. Spring LDAP provides support for detailed pool configuration on a per-`ContextSource` basis.

Pooling support is provided by supplying a `<ldap:pooling />` child element to the `<ldap:context-source />` element in the application context configuration. Read-only and read-write `DirContext` objects are pooled separately (if `anonymous-read-only` is specified). [Jakarta Commons-Pool](https://commons.apache.org/pool/index.html) is used to provide the underlying pool implementation.

<a id="pooling--dircontext-validation"></a>

## `DirContext` Validation

Validation of pooled connections is the primary motivation for using a custom pooling library versus the JDK-provided LDAP pooling functionality. Validation allows pooled `DirContext` connections to be checked to ensure that they are still properly connected and configured when checking them out of the pool, checking them into the pool, or while they are idle in the pool.

If connection validation is configured, pooled connections are validated by using `DefaultDirContextValidator`.
`DefaultDirContextValidator` does a `DirContext.search(String, String, SearchControls)`, with an empty name, a filter of `"objectclass=*"`, and `SearchControls` set to limit a single result with the only the `objectclass` attribute and a 500ms timeout. If the returned `NamingEnumeration` has results, the `DirContext` passes validation. If no results are returned or an exception is thrown, the `DirContext` fails validation.
The default settings should work with no configuration changes on most LDAP servers and provide the fastest way to validate the `DirContext`.
If you need customization, you can do so by using the validation configuration attributes, described in [Pool Configuration](#pooling--pool-configuration).

> [!NOTE]
> Connections are automatically invalidated if they throw an exception that is considered non-transient. For example, if a `DirContext` instance throws a `javax.naming.CommunicationException`, it is interpreted as a non-transient error and the instance is automatically invalidated, without the overhead of an additional `testOnReturn` operation. The exceptions that are interpreted as non-transient are configured by using the `nonTransientExceptions` property of the `PoolingContextSource`.

<a id="pooling--pool-configuration"></a>

## Pool Configuration

The following attributes are available on the `<ldap:pooling />` element for configuration of the DirContext pool:

<table class="tableblock frame-all grid-all stretch">
<caption>Table 1. Pooling Configuration Attributes</caption>
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Default</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td><p><code>max-active</code></p></td>
<td><p><code>8</code></p></td>
<td><div><div>
<p>The maximum number of active connections of each type (read-only or read-write) that can be allocated from this pool at the same time. You can use a non-positive number for no limit.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>max-total</code></p></td>
<td><p><code>-1</code></p></td>
<td><div><div>
<p>The overall maximum number of active connections (for all types) that can be allocated from this pool at the same time. You can use a non-positive number for no limit.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>max-idle</code></p></td>
<td><p><code>8</code></p></td>
<td><div><div>
<p>The maximum number of active connections of each type (read-only or read-write) that can remain idle in the pool without extra connections being released. You can use a non-positive number for no limit.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>min-idle</code></p></td>
<td><p><code>0</code></p></td>
<td><div><div>
<p>The minimum number of active connections of each type (read-only or read-write) that can remain idle in the pool without extra connections being created. You can use zero (the default) to create none.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>max-wait</code></p></td>
<td><p><code>-1</code></p></td>
<td><div><div>
<p>The maximum number of milliseconds that the pool waits (when no connections are available) for a connection to be returned before throwing an exception. You can use a non-positive number to wait indefinitely.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>when-exhausted</code></p></td>
<td><p><code>BLOCK</code></p></td>
<td><div><div>
<p>Specifies the behavior when the pool is exhausted.</p>
</div>
<div>
<ul>
<li>
<p>The <code>FAIL</code> option throws <code>NoSuchElementException</code> when the pool is exhausted.</p>
</li>
<li>
<p>The <code>BLOCK</code> option waits until a new object is available. If <code>max-wait</code> is positive and no new object is available after the <code>max-wait</code> time expires, <code>NoSuchElementException</code> is thrown.</p>
</li>
<li>
<p>The <code>GROW</code> option creates and returns a new object (essentially making <code>max-active</code> meaningless).</p>
</li>
</ul>
</div></div></td>
</tr>
<tr>
<td><p><code>test-on-borrow</code></p></td>
<td><p><code>false</code></p></td>
<td><div><div>
<p>Whether objects are validated before being borrowed from the pool. If the object fails to validate, it is dropped from the pool, and an attempt to borrow another is made.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>test-on-return</code></p></td>
<td><p><code>false</code></p></td>
<td><div><div>
<p>Whether objects are validated before being returned to the pool.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>test-while-idle</code></p></td>
<td><p><code>false</code></p></td>
<td><div><div>
<p>Whether objects are validated by the idle object evictor (if any). If an object fails to validate, it is dropped from the pool.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>eviction-run-interval-millis</code></p></td>
<td><p><code>-1</code></p></td>
<td><div><div>
<p>The number of milliseconds to sleep between runs of the idle object evictor thread. When non-positive, no idle object evictor thread is run.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>tests-per-eviction-run</code></p></td>
<td><p><code>3</code></p></td>
<td><div><div>
<p>The number of objects to examine during each run of the idle object evictor thread (if any).</p>
</div></div></td>
</tr>
<tr>
<td><p><code>min-evictable-time-millis</code></p></td>
<td><p><code>1000 * 60 * 30</code> (30 minutes)</p></td>
<td><div><div>
<p>The minimum amount of time an object may sit idle in the pool before it is eligible for eviction by the idle object evictor (if any).</p>
</div></div></td>
</tr>
<tr>
<td><p><code>validation-query-base</code></p></td>
<td><p><code>LdapUtils.emptyName()</code></p></td>
<td><div><div>
<p>The search base to be used when validating connections. Used only if <code>test-on-borrow</code>, <code>test-on-return</code>, or <code>test-while-idle</code> is specified.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>validation-query-filter</code></p></td>
<td><p><code>objectclass=*</code></p></td>
<td><div><div>
<p>The search filter to be used when validating connections. Used only if <code>test-on-borrow</code>, <code>test-on-return</code>, or <code>test-while-idle</code> is specified.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>validation-query-search-controls-ref</code></p></td>
<td><p><code>null</code>; default search control settings are described above.</p></td>
<td><div><div>
<p>The ID of a <code>SearchControls</code> instance to be used when validating connections. Only used if <code>test-on-borrow</code>, <code>test-on-return</code>, or <code>test-while-idle</code> is specified.</p>
</div></div></td>
</tr>
<tr>
<td><p><code>non-transient-exceptions</code></p></td>
<td><p><code>javax.naming.CommunicationException</code></p></td>
<td><div><div>
<p>Comma-separated list of <code>Exception</code> classes. The listed exceptions are considered non-transient with regards to eager invalidation. Should any of the listed exceptions (or subclasses of them) be thrown by a call to a pooled <code>DirContext</code> instance, that object is automatically invalidated without any additional testOnReturn operation.</p>
</div></div></td>
</tr>
</tbody>
</table>

<a id="pooling--pool2-configuration"></a>

## Pool2 Configuration

The following attributes are available on the `<ldap:pooling2 />` element for configuring the `DirContext` pool:

| Attribute | Default | Description |
| --- | --- | --- |
| `max-total` | `-1` | The overall maximum number of active connections (for all types) that can be allocated from this pool at the same time. You can use a non-positive number for no limit. |
| `max-total-per-key` | `8` | The limit on the number of object instances allocated by the pool (checked out or idle), per key. When the limit is reached, the sub-pool is exhausted. A negative value indicates no limit. |
| `max-idle-per-key` | `8` | The maximum number of active connections of each type (read-only or read-write) that can remain idle in the pool, without extra connections being released. A negative value indicates no limit. |
| `min-idle-per-key` | `0` | The minimum number of active connections of each type (read-only or read-write) that can remain idle in the pool, without extra connections being created. You can use zero (the default) to create none. |
| `max-wait` | `-1` | The maximum number of milliseconds that the pool waits (when there are no available connections) for a connection to be returned before throwing an exception. You can use a non-positive number to wait indefinitely. |
| `block-when-exhausted` | `true` | Whether to wait until a new object is available. If max-wait is positive, a `NoSuchElementException` is thrown if no new object is available after the `maxWait` time expires. |
| `test-on-create` | `false` | Whether objects are validated before borrowing. If the object fails to validate, then borrowing fails. |
| `test-on-borrow` | `false` | The indicator for whether objects are validated before being borrowed from the pool. If the object fails to validate, it is dropped from the pool, and an attempt to borrow another is made. |
| `test-on-return` | `false` | The indicator for whether objects are validated before being returned to the pool. |
| `test-while-idle` | `false` | The indicator for whether objects are validated by the idle object evictor (if any). If an object fails to validate, it is dropped from the pool. |
| `eviction-run-interval-millis` | `-1` | The number of milliseconds to sleep between runs of the idle object evictor thread. When non-positive, no idle object evictor thread is run. |
| `tests-per-eviction-run` | `3` | The number of objects to examine during each run of the idle object evictor thread (if any). |
| `min-evictable-time-millis` | `1000 * 60 * 30` (30 minutes) | The minimum amount of time an object may sit idle in the pool before it is eligible for eviction by the idle object evictor (if any). |
| `soft-min-evictable-time-millis` | `-1` | The minimum amount of time an object may sit idle in the pool before it is eligible for eviction by the idle object evictor, with the extra condition that at least the minimum number of object instances per key remain in the pool. This setting is overridden by `min-evictable-time-millis` if it is set to a positive value. |
| `eviction-policy-class` | `org.apache.commons.pool2.impl.DefaultEvictionPolicy` | The eviction policy implementation that is used by this pool. The pool tries to load the class by using the thread context class loader. If that fails, the pool tries to load the class by using the class loader that loaded this class. |
| `fairness` | `false` | The pool serves threads that are waiting to borrow connections fairly. `true` means that waiting threads are served as if waiting in a FIFO queue. |
| `jmx-enable` | `true` | JMX is enabled with the platform MBean server for the pool. |
| `jmx-name-base` | `null` | The JMX name base that is used as part of the name assigned to JMX enabled pools. |
| `jmx-name-prefix` | `pool` | The JMX name prefix that is used as part of the name assigned to JMX enabled pools. |
| `lifo` | `true` | The indicator for whether the pool has LIFO (last in, first out) behavior with respect to idle objects or as a FIFO (first in, first out) queue. LIFO always returns the most recently used object from the pool, while FIFO always returns the oldest object in the idle object pool |
| `validation-query-base` | `LdapUtils.emptyPath()` | The base DN to use for validation searches. |
| `validation-query-filter` | `objectclass=*` | The filter to use for validation queries. |
| `validation-query-search-controls-ref` | `null`; default search control settings are described above. | The ID of a `SearchControls` instance to be used when validating connections. Used only if `test-on-borrow`, `test-on-return`, or `test-while-idle` is specified |
| `non-transient-exceptions` | `javax.naming.CommunicationException` | Comma-separated list of `Exception` classes. The listed exceptions are considered non-transient with regards to eager invalidation. Should any of the listed exceptions (or subclasses of them) be thrown by a call to a pooled `DirContext` instance, that object is automatically invalidated without any additional testOnReturn operation. |

<a id="pooling--configuration"></a>

## Configuration

Configuring pooling requires adding an `<ldap:pooling>` element nested in the `<ldap:context-source>` element, as follows:

```xml
<beans> ...<ldap:context-source password="secret" url="ldap://localhost:389" username="cn=Manager"> <ldap:pooling /> </ldap:context-source> ...</beans>
```

In a real-world situation, you would probably configure the pool options and enable connection validation. The preceding example demonstrates the general idea.

<a id="pooling--validation-configuration"></a>

### Validation Configuration

The following example tests each `DirContext` before it is passed to the client application and tests `DirContext` objects that have been sitting idle in the pool:

```xml
<beans>
   ...
    <ldap:context-source
        username="cn=Manager" password="secret" url="ldap://localhost:389" >
        <ldap:pooling
            test-on-borrow="true"
            test-while-idle="true" />
    </ldap:context-source>
   ...
</beans>
```

<a id="pooling--known-issues"></a>

## Known Issues

This section describes issues that sometimes arise when people use Spring LDAP. At present, it covers the following issues:

- [Custom Authentication](#pooling--spring-ldap-known-issues-custom-authentication)

<a id="pooling--spring-ldap-known-issues-custom-authentication"></a>
<a id="pooling--custom-authentication"></a>

### Custom Authentication

The `PoolingContextSource` assumes that all `DirContext` objects retrieved from `ContextSource.getReadOnlyContext()` have the same environment and, likewise, that all `DirContext` objects retrieved from `ContextSource.getReadWriteContext()` have the same environment. This means that wrapping an `LdapContextSource` configured with an `AuthenticationSource` in a `PoolingContextSource` does not function as expected. The pool would be populated by using the credentials of the first user, and, unless new connections were needed, subsequent context requests would not be filled for the user specified by the `AuthenticationSource` for the requesting thread.

[Spring LDAP Repositories](#repositories)
[Adding Missing Overloaded API Methods](#adding-missing-overloaded-api-methods)

---

<a id="adding-missing-overloaded-api-methods"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/adding-missing-overloaded-api-methods.html -->

<!-- page_index: 12 -->

# Adding Missing Overloaded API Methods

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="adding-missing-overloaded-api-methods--page-title"></a>
<a id="adding-missing-overloaded-api-methods--adding-missing-overloaded-api-methods"></a>

# Adding Missing Overloaded API Methods

This section covers how to add your own overloaded API methods to implement new functionality.

<a id="adding-missing-overloaded-api-methods--implementing-custom-search-methods"></a>

## Implementing Custom Search Methods

`LdapTemplate` contains several overloaded versions of the most common operations in `DirContext`. However, we have not provided an alternative for each and every method signature, mostly because there are so many of them. We have, however, provided a means to call whichever `DirContext` method you want and still get the benefits that `LdapTemplate` provides.

Suppose you want to call the following `DirContext` method:

```java
NamingEnumeration search(Name name, String filterExpr, Object[] filterArgs, SearchControls ctls)
```

There is no corresponding overloaded method in `LdapTemplate`. The way to solve this is to use a custom `SearchExecutor` implementation, as follows:

```java
public interface SearchExecutor {
   public NamingEnumeration executeSearch(DirContext ctx) throws NamingException;
}
```

In your custom executor, you have access to a `DirContext` object, which you can use to call the method you want. You can then provide a handler that is responsible for mapping attributes and collecting the results. You can, for example, use one of the available implementations of `CollectingNameClassPairCallbackHandler`, which collects the mapped results in an internal list. In order to actually perform the search, you need to call the `search` method in `LdapTemplate` that takes an executor and a handler as arguments. Finally, you need to return whatever your handler has collected. The following example shows how to do all of that:

Example 1. A custom search method using `SearchExecutor` and `AttributesMapper`

```java
public class PersonRepoImpl implements PersonRepo {...public List search(final Name base, final String filter, final String[] params,final SearchControls ctls) {SearchExecutor executor = new SearchExecutor() {public NamingEnumeration executeSearch(DirContext ctx) {return ctx.search(base, filter, params, ctls);} };
CollectingNameClassPairCallbackHandler handler =new AttributesMapperCallbackHandler(new PersonAttributesMapper());
ldapTemplate.search(executor, handler); return handler.getList();}}
```

If you prefer the `ContextMapper` to the `AttributesMapper`, the following example shows what it would look like:

Example 2. A custom search method using `SearchExecutor` and `ContextMapper`

```java
public class PersonRepoImpl implements PersonRepo {...public List search(final Name base, final String filter, final String[] params,final SearchControls ctls) {SearchExecutor executor = new SearchExecutor() {public NamingEnumeration executeSearch(DirContext ctx) {return ctx.search(base, filter, params, ctls);} };
CollectingNameClassPairCallbackHandler handler =new ContextMapperCallbackHandler(new PersonContextMapper());
ldapTemplate.search(executor, handler); return handler.getList();}}
```

> [!NOTE]
> When you use the `ContextMapperCallbackHandler`, you must make sure that you have called `setReturningObjFlag(true)` on your `SearchControls` instance.

<a id="adding-missing-overloaded-api-methods--implementing-other-custom-context-methods"></a>

## Implementing Other Custom Context Methods

In the same manner as for custom `search` methods, you can actually call any method in `DirContext` by using a `ContextExecutor`, as follows:

```java
public interface ContextExecutor {
   public Object executeWithContext(DirContext ctx) throws NamingException;
}
```

When implementing a custom `ContextExecutor`, you can choose between using the `executeReadOnly()` or the `executeReadWrite()` method. Suppose you want to call the following method:

```java
Object lookupLink(Name name)
```

The method is available in `DirContext`, but there is no matching method in `LdapTemplate`. It is a lookup method, so it should be read-only. We can implement it as follows:

Example 3. A custom `DirContext` method using `ContextExecutor`

```java
public class PersonRepoImpl implements PersonRepo {...public Object lookupLink(final Name name) {ContextExecutor executor = new ContextExecutor() {public Object executeWithContext(DirContext ctx) {return ctx.lookupLink(name);} };
return ldapTemplate.executeReadOnly(executor);}}
```

In the same manner, you can perform a read-write operation by using the `executeReadWrite()` method.

[Pooling Support](#pooling)
[Processing the `DirContext`](#processing-the-dircontext)

---

<a id="processing-the-dircontext"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/processing-the-dircontext.html -->

<!-- page_index: 13 -->

# Processing the DirContext

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="processing-the-dircontext--page-title"></a>
<a id="processing-the-dircontext--processing-the-dircontext"></a>

# Processing the `DirContext`

This section covers how to process the `DirContext`, including pre- and post-processing.

<a id="processing-the-dircontext--custom-dircontext-pre-and-post-processing"></a>

## Custom `DirContext` Pre- and Post-processing

In some situations, you might like to perform operations on the `DirContext` before and after the search operation. The interface that is used for this is called `DirContextProcessor`. The following listing shows the `DirContextProcessor` interface:

```java
public interface DirContextProcessor {
   public void preProcess(DirContext ctx) throws NamingException;
   public void postProcess(DirContext ctx) throws NamingException;
}
```

The `LdapTemplate` class has a search method that takes a `DirContextProcessor`, as follows:

```java
public void search(SearchExecutor se, NameClassPairCallbackHandler handler,
   DirContextProcessor processor) throws DataAccessException;
```

Before the search operation, the `preProcess` method is called on the given `DirContextProcessor` instance. After the search has run and the resulting `NamingEnumeration` has been processed, the `postProcess` method is called. This lets you perform operations on the `DirContext` to be used in the search and to check the `DirContext` when the search has been performed. This can be very useful (for example, when handling request and response controls).

You can also use the following convenience methods when you do not need a custom `SearchExecutor`:

```java
public void search(Name base, String filter,
   SearchControls controls, NameClassPairCallbackHandler handler, DirContextProcessor processor)

public void search(String base, String filter,
   SearchControls controls, NameClassPairCallbackHandler handler, DirContextProcessor processor)

public void search(Name base, String filter,
   SearchControls controls, AttributesMapper mapper, DirContextProcessor processor)

public void search(String base, String filter,
   SearchControls controls, AttributesMapper mapper, DirContextProcessor processor)

public void search(Name base, String filter,
   SearchControls controls, ContextMapper mapper, DirContextProcessor processor)

public void search(String base, String filter,
   SearchControls controls, ContextMapper mapper, DirContextProcessor processor)
```

<a id="processing-the-dircontext--implementing-a-request-control-dircontextprocessor"></a>

## Implementing a Request Control `DirContextProcessor`

The LDAPv3 protocol uses “Controls” to send and receive additional data to affect the behavior of predefined operations. To simplify the implementation of a request control `DirContextProcessor`, Spring LDAP provides the `AbstractRequestControlDirContextProcessor` base class. This class handles the retrieval of the current request controls from the `LdapContext`, calls a template method for creating a request control, and adds it to the `LdapContext`. All you have to do in the subclass is to implement the template method called `createRequestControl` and the `postProcess` method for performing whatever you need to do after the search. The following listing shows the relevant signatures:

```java
public abstract class AbstractRequestControlDirContextProcessor implements DirContextProcessor {
public void preProcess(DirContext ctx) throws NamingException {...}
public abstract Control createRequestControl();}
```

A typical `DirContextProcessor` is similar to the following example:

Example 1. A request control `DirContextProcessor` implementation

```java
public class MyCoolRequestControl extends AbstractRequestControlDirContextProcessor {private static final boolean CRITICAL_CONTROL = true; private MyCoolCookie cookie; ...public MyCoolCookie getCookie() {return cookie;}
public Control createRequestControl() {return new SomeCoolControl(cookie.getCookie(), CRITICAL_CONTROL);}
public void postProcess(DirContext ctx) throws NamingException {LdapContext ldapContext = (LdapContext) ctx; Control[] responseControls = ldapContext.getResponseControls();
for (int i = 0; i < responseControls.length; i++) {if (responseControls[i] instanceof SomeCoolResponseControl) {SomeCoolResponseControl control = (SomeCoolResponseControl) responseControls[i]; this.cookie = new MyCoolCookie(control.getCookie());}}}}
```

> [!NOTE]
> Make sure you use `LdapContextSource` when you use controls. The [`Control`](https://download.oracle.com/javase/1.5.0/docs/api/javax/naming/ldap/Control.html) interface is specific for LDAPv3 and requires that `LdapContext` is used instead of `DirContext`. If an `AbstractRequestControlDirContextProcessor` subclass is called with an argument that is not an `LdapContext`, it throws an `IllegalArgumentException`.

<a id="processing-the-dircontext--paged-search-results"></a>

## Paged Search Results

Some searches may return large numbers of results. When there is no easy way to filter out a smaller amount, it is convenient to have the server return only a certain number of results each time it is called. This is known as “paged search results”. Each “page” of the result could then be displayed, with links to the next and previous page. Without this functionality, the client must either manually limit the search result into pages or retrieve the whole result and then chop it into pages of suitable size. The former would be rather complicated, and the latter would consume unnecessary amounts of memory.

Some LDAP servers support `PagedResultsControl`, which requests that the results of a search operation are returned by the LDAP server in pages of a specified size. The user controls the rate at which the pages are returned, by controlling the rate at which the searches are called. However, you must keep track of a cookie between the calls. The server uses this cookie to keep track of where it left off the previous time it was called with a paged results request.

Spring LDAP provides support for paged results by using the concept for pre- and post-processing of an `LdapContext`, as discussed in the previous sections. It does so by using the `PagedResultsControlExchangeDirContextProcessor` class. The `PagedResultsControlExchangeDirContextProcessor` class creates a `PagedResultsControl` with the requested page size and adds it to the `LdapContext`. After the search, it gets the `PagedResultsResponseControl` and retrieves the paged results cookie, which is needed to keep the context between consecutive paged results requests.

The following example shows how the to use the paged search results functionality:

Example 2. Paged results using `PagedResultsControlDirContextProcessor`

```java
public List<String> getAllPersonNames() {
  final SearchControls searchControls = new SearchControls();
  searchControls.setSearchScope(SearchControls.SUBTREE_SCOPE);

  PagedResultsControlExchangeDirContextProcessor processor = new PagedResultsControlExchangeDirContextProcessor(PAGE_SIZE);

  return SingleContextSource.doWithSingleContext(
        contextSource, new LdapOperationsCallback<List<String>>() {

      @Override
      public List<String> doWithLdapOperations(LdapOperations operations) {
        List<String> result = new LinkedList<String>();

        do {
          List<String> oneResult = operations.search(
            "ou=People",
            "(&(objectclass=person))",
            searchControls,
            CN_ATTRIBUTES_MAPPER,
            processor);
          result.addAll(oneResult);
        } while(processor.hasMore());

        return result;
      }
  });
}
```

> [!NOTE]
> For a paged results cookie to continue being valid, you must use the same underlying connection for each paged results call. You can do so by using the `SingleContextSource`, as demonstrated in the preceding example or by using a `ContextSourceTransactionManager` and `TransactionAwareContextSourceProxy`.

[Adding Missing Overloaded API Methods](#adding-missing-overloaded-api-methods)
[Transaction Support](#transaction-support)

---

<a id="transaction-support"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/transaction-support.html -->

<!-- page_index: 14 -->

# Transaction Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="transaction-support--page-title"></a>
<a id="transaction-support--transaction-support"></a>

# Transaction Support

Programmers used to working with relational databases coming to the LDAP world often express surprise at the fact that there is no notion of transactions.
It is not specified in the protocol, and no LDAP servers support it.
Recognizing that this may be a major problem, Spring LDAP provides support for client-side, compensating transactions on LDAP resources.

LDAP transaction support is provided by `ContextSourceTransactionManager`, a `PlatformTransactionManager` implementation that manages Spring transaction support for LDAP operations. Along with its collaborators, it keeps track of the LDAP operations performed in a transaction, making a record of the state before each operation and taking steps to restore the initial state should the transaction need to be rolled back.

In addition to the actual transaction management, Spring LDAP transaction support also makes sure that the same `DirContext` instance is used throughout the same transaction. That is, the `DirContext` is not actually closed until the transaction is finished, allowing for more efficient resources usage.

> [!IMPORTANT]
> While the approach used by Spring LDAP to provide transaction support is sufficient for many cases, it is by no means “real” transactions in the traditional sense.
> The server is completely unaware of the transactions, so (for example), if the connection is broken, there is no way to roll back the transaction.
> While this should be carefully considered, it should also be noted that the alternative is to operate without any transaction support whatsoever. Spring LDAP’s transaction support is pretty much as good as it gets.

> [!NOTE]
> The client-side transaction support adds some overhead in addition to the work required by the original operations.
> While this overhead should not be something to worry about in most cases, if your application does not perform several LDAP operations within the same transaction (for example, `modifyAttributes` followed by `rebind`), or if transaction synchronization with a JDBC data source is not required (see [JDBC Transaction Integration](#transaction-support--spring-ldap-jdbc-transaction-integration)), you gain little by using the LDAP transaction support.

<a id="transaction-support--configuration"></a>

## Configuration

Configuring Spring LDAP transactions should look very familiar if you are used to configuring Spring transactions. You can annotate your transacted classes with `@Transactional`, create a `TransactionManager` instance, and include a `<tx:annotation-driven>` element in your bean configuration. The following example shows how to do so:

```xml
<ldap:context-source url="ldap://localhost:389" base="dc=example,dc=com" username="cn=Manager" password="secret" />
<ldap:ldap-template id="ldapTemplate" /> <ldap:transaction-manager> <!-- Note this default configuration will not work for more complex scenarios; see below for more information on RenamingStrategies.--> <ldap:default-renaming-strategy /> </ldap:transaction-manager>
<!-- The MyDataAccessObject class is annotated with @Transactional.--> <bean id="myDataAccessObject" class="com.example.MyRepository"> <property name="ldapTemplate" ref="ldapTemplate" /> </bean>
<tx:annotation-driven /> ...
```

> [!NOTE]
> While this setup works fine for most simple use cases, some more complex scenarios require additional configuration.
> Specifically, if you need to create or delete subtrees within transactions, you need to use an alternative `TempEntryRenamingStrategy`, as described in [Renaming Strategies](#transaction-support--renaming-strategies).

In a real-world situation, you would probably apply the transactions on the service-object level rather than the repository level. The preceding example demonstrates the general idea.

<a id="transaction-support--spring-ldap-jdbc-transaction-integration"></a>
<a id="transaction-support--jdbc-transaction-integration"></a>

## JDBC Transaction Integration

This support was removed in Spring LDAP 4.0.

<a id="transaction-support--ldap-compensating-transactions-explained"></a>

## LDAP Compensating Transactions Explained

Spring LDAP manages compensating transactions by making a record of the state in the LDAP tree before each modifying operation (`bind`, `unbind`, `rebind`, `modifyAttributes`, and `rename`).
This lets the system perform compensating operations should the transaction need to be rolled back.

In many cases, the compensating operation is pretty straightforward. For example, the compensating rollback operation for a `bind` operation is to unbind the entry.
Other operations, however, require a different, more complicated approach because of some particular characteristics of LDAP databases.
Specifically, it is not always possible to get the values of all `Attributes` of an entry, making the aforementioned strategy insufficient for (for example) an `unbind` operation.

This is why each modifying operation performed within a Spring LDAP managed transaction is internally split up into four distinct operations: a recording operation, a preparation operation, a commit operation, and a rollback operation. The following table describes each LDAP operation:

| LDAP Operation | Recording | Preparation | Commit | Rollback |
| --- | --- | --- | --- | --- |
| `bind` | Make a record of the DN of the entry to bind. | Bind the entry. | No operation. | Unbind the entry by using the recorded DN. |
| `rename` | Make a record of the original and target DN. | Rename the entry. | No operation. | Rename the entry back to its original DN. |
| `unbind` | Make a record of the original DN and calculate a temporary DN. | Rename the entry to the temporary location. | Unbind the temporary entry. | Rename the entry from the temporary location back to its original DN. |
| `rebind` | Make a record of the original DN and the new `Attributes` and calculate a temporary DN. | Rename the entry to a temporary location. | Bind the new `Attributes` at the original DN and unbind the original entry from its temporary location. | Rename the entry from the temporary location back to its original DN. |
| `modifyAttributes` | Make a record of the DN of the entry to modify and calculate compensating `ModificationItem` instances for the modifications to be done. | Perform the `modifyAttributes` operation. | No operation. | Perform a `modifyAttributes` operation by using the calculated compensating `ModificationItem` instances. |

A more detailed description of the internal workings of the Spring LDAP transaction support is available in the [Javadoc](https://docs.spring.io/spring-ldap/docs/current/apidocs/).

<a id="transaction-support--renaming-strategies"></a>

### Renaming Strategies

As described in the table in the preceding section, the transaction management of some operations requires the original entry affected by the operation to be temporarily renamed before the actual modification can be made in the commit. The manner in which the temporary DN of the entry is calculated is managed by a `TempEntryRenamingStrategy` that is specified in a child element of the `<ldap:transaction-manager >` declaration in the configuration. Spring LDAP includes two implementations:

- `DefaultTempEntryRenamingStrategy` (the default): Specified by using an `<ldap:default-renaming-strategy />` element. Adds a suffix to the least significant part of the entry DN. For example, for a DN of `cn=john doe, ou=users`, this strategy returns a temporary DN of `cn=john doe_temp, ou=users`. You can configure the suffix by setting the `temp-suffix` attribute.
- `DifferentSubtreeTempEntryRenamingStrategy`: Specified by using an `<ldap:different-subtree-renaming-strategy />` element. It appends a subtree DN to the least significant part of the DN. Doing so makes all temporary entries be placed at a specific location in the LDAP tree. The temporary subtree DN is configured by setting the `subtree-node` attribute. For example, if `subtree-node` is `ou=tempEntries` and the original DN of the entry is `cn=john doe, ou=users`, the temporary DN is `cn=john doe, ou=tempEntries`. Note that the configured subtree node needs to be present in the LDAP tree.

> [!NOTE]
> The `DefaultTempEntryRenamingStrategy` does not work in some situations. For example, if you plan to do recursive deletes, you need to use `DifferentSubtreeTempEntryRenamingStrategy`. This is because the recursive delete operation actually consists of a depth-first delete of each node in the sub tree individually. Since you cannot rename an entry that has any children and `DefaultTempEntryRenamingStrategy` would leave each node in the same subtree (with a different name) instead of actually removing it, this operation would fail. When in doubt, use `DifferentSubtreeTempEntryRenamingStrategy`.

[Processing the `DirContext`](#processing-the-dircontext)
[User Authentication using Spring LDAP](#user-authentication)

---

<a id="user-authentication"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/user-authentication.html -->

<!-- page_index: 15 -->

# User Authentication using Spring LDAP

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="user-authentication--page-title"></a>
<a id="user-authentication--user-authentication-using-spring-ldap"></a>

# User Authentication using Spring LDAP

This section covers user authentication with Spring LDAP. It contains the following topics:

- [Basic Authentication](#user-authentication--spring-ldap-user-authentication-basic)
- [Performing Operations on the Authenticated Context](#user-authentication--operationsonauthenticatedcontext)
- [Obsolete Authentication Methods](#user-authentication--spring-ldap-authentication-obsolete)
- [Using Spring Security](#user-authentication--spring-ldap-using-spring-security)

<a id="user-authentication--spring-ldap-user-authentication-basic"></a>
<a id="user-authentication--basic-authentication"></a>

## Basic Authentication

While the core functionality of the `ContextSource` is to provide `DirContext` instances for use by `LdapClient` and `LdapTemplate`, you can also use it for authenticating users against an LDAP server. The `getContext(principal, credentials)` method of `ContextSource` does exactly that. It constructs a `DirContext` instance according to the `ContextSource` configuration and authenticates the context by using the supplied principal and credentials. A custom authenticate method could look like the following example:

```java
public boolean authenticate(String userDn, String credentials) {
  DirContext ctx = null;
  try {
    ctx = contextSource.getContext(userDn, credentials);
    return true;
  } catch (Exception e) {
    // Context creation failed - authentication did not succeed
    logger.error("Login failed", e);
    return false;
  } finally {
    // It is imperative that the created DirContext instance is always closed
    LdapUtils.closeContext(ctx);
  }
}
```

The `userDn` supplied to the `authenticate` method needs to be the full DN of the user to authenticate (regardless of the `base` setting on the `ContextSource`). You typically need to perform an LDAP search based on (for example) the user name to get this DN. The following example shows how to do so:

```java
private String getDnForUser(String uid) {List<String> result = ldapClient.search() .query(query().where("uid").is(uid)) .map((Object ctx) -> ((DirContextOperations) ctx).getNameInNamespace()).list();
if(result.size() != 1) {throw new RuntimeException("User not found or not unique");}
return result.get(0);}
```

There are some drawbacks to this approach. You are forced to concern yourself with the DN of the user, you can search only for the user’s uid, and the search always starts at the root of the tree (the empty path). A more flexible method would let you specify the search base, the search filter, and the credentials. Spring LDAP includes an authenticate method in `LdapClient` that provides this functionality.

When you use this method, authentication becomes as simple as follows:

Example 1. Authenticating a user using Spring LDAP

```java
ldapClient.authenticate().query(query().where("uid").is("john.doe")).password("secret").execute();
```

> [!NOTE]
> As described in the [Performing Operations on the Authenticated Context](#user-authentication--operationsonauthenticatedcontext), some setups may require you to perform additional operations to get actual authentication to occur. See [Performing Operations on the Authenticated Context](#user-authentication--operationsonauthenticatedcontext) for details.

> [!TIP]
> Do not write your own custom authenticate methods. Use the ones provided in Spring LDAP.

<a id="user-authentication--operationsonauthenticatedcontext"></a>
<a id="user-authentication--performing-operations-on-the-authenticated-context"></a>

## Performing Operations on the Authenticated Context

Some authentication schemes and LDAP servers require some operation to be performed on the created `DirContext` instance for the actual authentication to occur. You should test and make sure how your server setup and authentication schemes behave. Failure to do so might result in users being admitted into your system regardless of the supplied DN and credentials. The following example shows a naïve implementation of an authenticate method where a hard-coded `lookup` operation is performed on the authenticated context:

```java
public boolean myAuthenticate(String userDn, String credentials) {
  DirContext ctx = null;
  try {
    ctx = contextSource.getContext(userDn, credentials);
    // Take care here - if a base was specified on the ContextSource
    // that needs to be removed from the user DN for the lookup to succeed.
    ctx.lookup(userDn);
    return true;
  } catch (Exception e) {
    // Context creation failed - authentication did not succeed
    logger.error("Login failed", e);
    return false;
  } finally {
    // It is imperative that the created DirContext instance is always closed
    LdapUtils.closeContext(ctx);
  }
}
```

It would be better if the operation could be provided as an implementation of a callback interface, rather than limiting the operation to always be a `lookup`. Spring LDAP includes the `AuthenticatedLdapEntryContextMapper` callback interface and a corresponding `authenticate` method.

This method lets any operation be performed on the authenticated context, as follows:

Example 2. Performing an LDAP operation on the authenticated context using Spring LDAP

```java
AuthenticatedLdapEntryContextMapper<DirContextOperations> mapper = new AuthenticatedLdapEntryContextMapper<DirContextOperations>() {public DirContextOperations mapWithContext(DirContext ctx, LdapEntryIdentification ldapEntryIdentification) {try {return (DirContextOperations) ctx.lookup(ldapEntryIdentification.getRelativeName());} catch (NamingException e) {throw new RuntimeException("Failed to lookup " + ldapEntryIdentification.getRelativeName(), e);}} };
ldapClient.authenticate().query(query().where("uid").is("john.doe")).password("secret").execute(mapper);
```

<a id="user-authentication--spring-ldap-authentication-obsolete"></a>
<a id="user-authentication--obsolete-authentication-methods"></a>

## Obsolete Authentication Methods

In addition to the `authenticate` methods described in the preceding sections, you can use a number of deprecated methods for authentication. While these work fine, we recommend using the `LdapQuery` methods instead.

<a id="user-authentication--spring-ldap-using-spring-security"></a>
<a id="user-authentication--using-spring-security"></a>

## Using Spring Security

While the approach described in the preceding sections may be sufficient for simple authentication scenarios, requirements in this area commonly expand rapidly. A multitude of aspects apply, including authentication, authorization, web integration, user context management, and others. If you suspect that the requirements might expand beyond just simple authentication, you should definitely consider using [Spring Security](https://spring.io/spring-security) for your security purposes instead. It is a full-featured, mature security framework that addresses the aforementioned aspects as well as several others.

[Transaction Support](#transaction-support)
[LDIF Parsing](#ldif-parsing)

---

<a id="ldif-parsing"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/ldif-parsing.html -->

<!-- page_index: 16 -->

# LDIF Parsing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="ldif-parsing--page-title"></a>
<a id="ldif-parsing--ldif-parsing"></a>

# LDIF Parsing

LDAP Directory Interchange Format (LDIF) files are the standard medium for describing directory data in a flat-file format. The most common uses of this format include information transfer and archival. However, the standard also defines a way to describe modifications to stored data in a flat-file format. LDIFs of this later type are typically referred to as *changetype* or *modify* LDIFs.

The `org.springframework.ldap.ldif` package provides the classes needed to parse LDIF files and deserialize them into tangible objects. The `LdifParser` is the main class of the `org.springframework.ldap.ldif` package and is capable of parsing files that comply with RFC 2849. This class reads lines from a resource and assembles them into an `LdapAttributes` object.

> [!NOTE]
> The `LdifParser` currently ignores *changetype* LDIF entries, as their usefulness in the context of an application has yet to be determined.

<a id="ldif-parsing--object-representation"></a>

## Object Representation

Two classes in the `org.springframework.ldap.core` package provide the means to represent an LDIF in code:

- `LdapAttribute`: Extends `javax.naming.directory.BasicAttribute` adding support for LDIF options as defined in RFC2849.
- `LdapAttributes`: Extends `javax.naming.directory.BasicAttributes` adding specialized support for DNs.

`LdapAttribute` objects represent options as a `Set<String>`. The DN support added to the `LdapAttributes` object employs the `javax.naming.ldap.LdapName` class.

<a id="ldif-parsing--the-parser"></a>

## The Parser

The `Parser` interface provides the foundation for operation and employs three supporting policy definitions:

- `SeparatorPolicy`: Establishes the mechanism by which lines are assembled into attributes.
- `AttributeValidationPolicy`: Ensures that attributes are correctly structured prior to parsing.
- `Specification`: Provides a mechanism by which object structure can be validated after assembly.

The default implementations of these interfaces are as follows:

- `org.springframework.ldap.ldif.parser.LdifParser`
- `org.springframework.ldap.ldif.support.SeparatorPolicy`
- `org.springframework.ldap.ldif.support.DefaultAttributeValidationPolicy`
- `org.springframework.ldap.schema.DefaultSchemaSpecification`

Together, these four classes parse a resource line by line and translate the data into `LdapAttributes` objects.

The `SeparatorPolicy` determines how individual lines read from the source file should be interpreted, as the LDIF specification lets attributes span multiple lines. The default policy assesses lines in the context of the order in which they were read to determine the nature of the line in consideration. *control* attributes and *changetype* records are ignored.

The `DefaultAttributeValidationPolicy` uses REGEX expressions to ensure that each attribute conforms to a valid attribute format (according to RFC 2849) once parsed. If an attribute fails validation, an `InvalidAttributeFormatException` is logged, and the record is skipped (the parser returns `null`).

<a id="ldif-parsing--schema-validation"></a>

## Schema Validation

A mechanism for validating parsed objects against a schema is available through the `Specification` interface in the `org.springframework.ldap.schema` package. The `DefaultSchemaSpecification` does not do any validation and is available for instances where records are known to be valid and need not be checked. This option saves the performance penalty that validation imposes. The `BasicSchemaSpecification` applies basic checks, such as ensuring DN and object class declarations have been provided. Currently, validation against an actual schema requires implementation of the `Specification` interface.

<a id="ldif-parsing--spring-batch-integration"></a>

## Spring Batch Integration

While the `LdifParser` can be employed by any application that requires parsing of LDIF files, Spring offers a batch processing framework that offers many file-processing utilities for parsing delimited files such as CSV. The `org.springframework.ldap.ldif.batch` package offers the classes needed to use the `LdifParser` as a valid configuration option in the Spring Batch framework.
There are five classes in this package. Together, they offer three basic use cases:

- Reading LDIF records from a file and returning an `LdapAttributes` object.
- Reading LDIF records from a file and mapping records to Java objects (POJOs).
- Writing LDIF records to a file.

The first use case is accomplished with `LdifReader`. This class extends Spring Batch’s `AbstractItemCountingItemStreamItemReader` and implements its `ResourceAwareItemReaderItemStream`. It fits naturally into the framework, and you can use it to read `LdapAttributes` objects from a file.

You can use `MappingLdifReader` to map LDIF objects directly to any POJO. This class requires you to provide an implementation of the `RecordMapper` interface. This implementation should implement the logic for mapping objects to POJOs.

You can implement `RecordCallbackHandler` and provide the implementation to either reader. You can use this handler to operate on skipped records. See the [Spring Batch API documentation](https://docs.spring.io/spring-batch/docs/current/api/org/springframework/batch/item/ldif/RecordCallbackHandler.html) for more information.

The last member of this package, the `LdifAggregator`, can be used to write LDIF records to a file. This class invokes the `toString()` method of the `LdapAttributes` object.

[User Authentication using Spring LDAP](#user-authentication)
[Utilities](#utilities)

---

<a id="utilities"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/utilities.html -->

<!-- page_index: 17 -->

# Utilities

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="utilities--page-title"></a>
<a id="utilities--utilities"></a>

# Utilities

This section describes additional utilities that you can use with Spring LDAP.

<a id="utilities--incremental-retrieval-of-multi-valued-attributes"></a>

## Incremental Retrieval of Multi-Valued Attributes

When there are a very large number of attribute values (>1500) for a specific attribute, Active Directory typically refuses to return all these values at once. Instead, the attribute values are returned according to the [Incremental Retrieval of Multi-valued Properties](https://tools.ietf.org/html/draft-kashi-incremental-00) method. Doing so requires the calling part to inspect the returned attribute for specific markers and, if necessary, make additional lookup requests until all values are found.

Spring LDAP’s `org.springframework.ldap.core.support.DefaultIncrementalAttributesMapper` helps when working with this kind of attributes, as follows:

```java
Object[] attrNames =  new Object[]{"oneAttribute", "anotherAttribute"};
Attributes attrs = DefaultIncrementalAttributeMapper.lookupAttributes(ldapTemplate, theDn, attrNames);
```

The preceding example parses any returned attribute range markers and makes repeated requests as necessary until all values for all requested attributes have been retrieved.

[LDIF Parsing](#ldif-parsing)
[Testing](#testing)

---

<a id="testing"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/testing.html -->

<!-- page_index: 18 -->

# Testing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="testing--page-title"></a>
<a id="testing--testing"></a>

# Testing

This section covers testing with Spring LDAP. It contains the following topics:

- [Using an Embedded Server](#testing--spring-ldap-testing-embedded-server)
- [ApacheDS](#testing--spring-ldap-testing-apacheds)
- [UnboundID](#testing--spring-ldap-testing-unboundid)

<a id="testing--spring-ldap-testing-embedded-server"></a>
<a id="testing--using-an-embedded-server"></a>

## Using an Embedded Server

`spring-ldap-test` supplies an embedded LDAP server that is based on [ApacheDS](https://directory.apache.org/apacheds/) or [UnboundID](https://www.ldap.com/unboundid-ldap-sdk-for-java).

> [!NOTE]
> `spring-ldap-test` is compatible with ApacheDS 1.5.5. Newer versions of ApacheDS are not supported.

To get started, you need to include the `spring-ldap-test` dependency.

The following listing shows how to include the `spring-ldap-test` for Maven:

```xml
<dependency>
    <groupId>org.springframework.ldap</groupId>
    <artifactId>spring-ldap-test</artifactId>
    <version>4.1.0</version>
    <scope>test</scope>
</dependency>
```

The following listing shows how to include the `spring-ldap-test` for Gradle:

```groovy
testCompile "org.springframework.ldap:spring-ldap-test:4.1.0"
```

<a id="testing--spring-ldap-testing-apacheds"></a>
<a id="testing--apacheds"></a>

## ApacheDS

To use ApacheDS, you need to include a number of ApacheDS dependencies.

The following example shows how to include the ApacheDS dependencies for Maven:

```xml
<dependency>
    <groupId>org.apache.directory.server</groupId>
    <artifactId>apacheds-core</artifactId>
    <version>1.5.5</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.apache.directory.server</groupId>
    <artifactId>apacheds-core-entry</artifactId>
    <version>1.5.5</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.apache.directory.server</groupId>
    <artifactId>apacheds-protocol-shared</artifactId>
    <version>1.5.5</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.apache.directory.server</groupId>
    <artifactId>apacheds-protocol-ldap</artifactId>
    <version>1.5.5</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.apache.directory.server</groupId>
    <artifactId>apacheds-server-jndi</artifactId>
    <version>1.5.5</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.apache.directory.shared</groupId>
    <artifactId>shared-ldap</artifactId>
    <version>0.9.15</version>
    <scope>test</scope>
</dependency>
```

The following example shows how to include the ApacheDS dependencies for Gradle:

```groovy
testCompile "org.apache.directory.server:apacheds-core:1.5.5",
            "org.apache.directory.server:apacheds-core-entry:1.5.5",
            "org.apache.directory.server:apacheds-protocol-shared:1.5.5",
            "org.apache.directory.server:apacheds-protocol-ldap:1.5.5",
            "org.apache.directory.server:apacheds-server-jndi:1.5.5",
            "org.apache.directory.shared:shared-ldap:0.9.15"
```

The following bean definition creates an embedded LDAP server:

```xml
<bean id="embeddedLdapServer" class="org.springframework.ldap.test.EmbeddedLdapServerFactoryBean">
    <property name="partitionName" value="example"/>
    <property name="partitionSuffix" value="dc=261consulting,dc=com" />
    <property name="port" value="9321" />
</bean>
```

`spring-ldap-test` provides a mechanism to populate the LDAP server by using `org.springframework.ldap.test.LdifPopulator`. To use it, create a bean similar to the following:

```xml
<bean class="org.springframework.ldap.test.LdifPopulator" depends-on="embeddedLdapServer">
    <property name="contextSource" ref="contextSource" />
    <property name="resource" value="classpath:/setup_data.ldif" />
    <property name="base" value="dc=jayway,dc=se" />
    <property name="clean" value="true" />
    <property name="defaultBase" value="dc=jayway,dc=se" />
</bean>
```

Another way to work against an embedded LDAP server is by using `org.springframework.ldap.test.TestContextSourceFactoryBean`, as follows:

```xml
<bean id="contextSource" class="org.springframework.ldap.test.TestContextSourceFactoryBean">
    <property name="defaultPartitionSuffix" value="dc=jayway,dc=se" />
    <property name="defaultPartitionName" value="jayway" />
    <property name="principal" value="uid=admin,ou=system" />
    <property name="password" value="secret" />
    <property name="ldifFile" value="classpath:/setup_data.ldif" />
    <property name="port" value="1888" />
</bean>
```

Also, `org.springframework.ldap.test.LdapTestUtils` provides methods to programmatically work with an embedded LDAP server.

<a id="testing--spring-ldap-testing-unboundid"></a>
<a id="testing--unboundid"></a>

## UnboundID

To use UnboundID, you need to include an UnboundID dependency.

The following example shows how to include the UnboundID dependency for Maven:

```xml
<dependency>
    <groupId>com.unboundid</groupId>
    <artifactId>unboundid-ldapsdk</artifactId>
    <version>3.1.1</version>
    <scope>test</scope>
</dependency>
```

The following example shows how to include the UnboundID dependency for Gradle:

```groovy
testCompile "com.unboundid:unboundid-ldapsdk:3.1.1"
```

The following bean definition creates an embedded LDAP server:

```java
@Bean
EmbeddedLdapServer embeddedLdapServer() {
    return EmbeddedLdapServer.withPartitionSuffix("dc=jayway,dc=se")
        .partitionName("jayway")
        .port(18881)
        .configurationCustomizer((config) -> config.setCodeLogDetails(tempLogFile, true))
        .build();
}
```

Alternatively, you can use the `org.springframework.ldap.test.unboundid.LdifPopulator` to create and populate the LDAP server. To use it, create a bean similar to the following:

```xml
<bean class="org.springframework.ldap.test.unboundid.LdifPopulator" depends-on="embeddedLdapServer">
    <property name="contextSource" ref="contextSource" />
    <property name="resource" value="classpath:/setup_data.ldif" />
    <property name="base" value="dc=jayway,dc=se" />
    <property name="clean" value="true" />
    <property name="defaultBase" value="dc=jayway,dc=se" />
</bean>
```

Another way to work against an embedded LDAP server is by using `org.springframework.ldap.test.unboundid.TestContextSourceFactoryBean`.
To use it, create a bean similar to the following:

```xml
<bean id="contextSource" class="org.springframework.ldap.test.unboundid.TestContextSourceFactoryBean">
    <property name="defaultPartitionSuffix" value="dc=jayway,dc=se" />
    <property name="defaultPartitionName" value="jayway" />
    <property name="principal" value="uid=admin,ou=system" />
    <property name="password" value="secret" />
    <property name="ldifFile" value="classpath:/setup_data.ldif" />
    <property name="port" value="1888" />
</bean>
```

Also, `org.springframework.ldap.test.unboundid.LdapTestUtils` provide methods to programmatically work with an embedded LDAP server.

[Utilities](#utilities)
[Spring LDAP FAQ](#faq)

---

<a id="faq"></a>

<!-- source_url: https://docs.spring.io/spring-ldap/reference/faq.html -->

<!-- page_index: 19 -->

# Spring LDAP FAQ

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="faq--page-title"></a>
<a id="faq--spring-ldap-faq"></a>

# Spring LDAP FAQ

<a id="faq--operational-attributes"></a>

## Operational Attributes

<a id="faq--how-do-i-remove-an-operational-attribute-by-using-context-removeattributevalue"></a>
<a id="faq--how-do-i-remove-an-operational-attribute-by-using-context.removeattributevalue"></a>

### How do I remove an operational attribute by using `context.removeAttributeValue()`?

By default, the `DirContextAdapter` reads only the visible attributes. This is because the operational attributes are returned by the server only if explicitly asked for, and there is no way for Spring LDAP to know the attributes for which to ask. This means that the `DirContextAdapter` is not populated with the operational attributes. Consequently, the `removeAttributeValue` does not have any effect (since, from the point of view of the `DirContextAdapter`, it was not there in the first place).

There are basically two ways to do this:

- Use a search or lookup method that takes the attribute names as an argument, such as `LdapTemplate#lookup(Name, String[], ContextMapper)`. Then use a `ContextMapper` implementation that returns the supplied `DirContextAdapter` in `mapFromContext()`.
- Use `LdapTemplate#modifyAttributes(Name, ModificationItem[])` directly, manually building the `ModificationItem` array.

[Testing](#testing)

---
