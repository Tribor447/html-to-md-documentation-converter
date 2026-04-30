# Getting Started (Java)

## Navigation

- Parent Project
  - [Apache Avro Java](#index)
- [Getting Started (Java)](#getting-started-java)
- [Getting Started (Python)](#getting-started-python)
- [Specification](#specification)
- [Java API](#api-java)
- [C API](#api-c)
- [C++ API](#api-cpp-html)
- [MapReduce guide](#mapreduce-guide)
- [IDL Language](#idl-language)
- [SASL profile](#sasl-profile)
- Other pages
  - [Apache Avro](#trevni)

## Content

<a id="index"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-avro-1.12.0-documentation"></a>

# Apache Avro™ 1.12.0 Documentation

<a id="index--introduction"></a>

## Introduction

Apache Avro™ is a data serialization system.

Avro provides:

- Rich data structures.
- A compact, fast, binary data format.
- A container file, to store persistent data.
- Remote procedure call (RPC).
- Simple integration with dynamic languages. Code generation is not required to read or write data files nor to use or implement RPC protocols. Code generation as an optional optimization, only worth implementing for statically typed languages.

<a id="index--schemas"></a>

## Schemas

Avro relies on schemas. When Avro data is read, the schema used when writing it is always present. This permits each datum to be written with no per-value overheads, making serialization both fast and small. This also facilitates use with dynamic, scripting languages, since data, together with its schema, is fully self-describing.

When Avro data is stored in a file, its schema is stored with it, so that files may be processed later by any program. If the program reading the data expects a different schema this can be easily resolved, since both schemas are present.

When Avro is used in RPC, the client and server exchange schemas in the connection handshake. (This can be optimized so that, for most calls, no schemas are actually transmitted.) Since both client and server both have the other’s full schema, correspondence between same named fields, missing fields, extra fields, etc. can all be easily resolved.

Avro schemas are defined with JSON . This facilitates implementation in languages that already have JSON libraries.

<a id="index--comparison-with-other-systems"></a>

## Comparison with other systems

Avro provides functionality similar to systems such as [Thrift](https://thrift.apache.org/), [Protocol Buffers](https://code.google.com/p/protobuf/), etc. Avro differs from these systems in the following fundamental aspects.

- Dynamic typing: Avro does not require that code be generated. Data is always accompanied by a schema that permits full processing of that data without code generation, static datatypes, etc. This facilitates construction of generic data-processing systems and languages.
- Untagged data: Since the schema is present when data is read, considerably less type information need be encoded with data, resulting in smaller serialization size.
- No manually-assigned field IDs: When a schema changes, both the old and new schema are always present when processing data, so differences may be resolved symbolically, using field names.

---

<a id="index--getting-started-java"></a>

##### [Getting Started (Java)](#getting-started-java)

<a id="index--getting-started-python"></a>

##### [Getting Started (Python)](#getting-started-python)

<a id="index--specification"></a>

##### [Specification](#specification)

<a id="index--java-api"></a>

##### [Java API](#api-java)

<a id="index--c-api"></a>

##### [C API](#api-c)

<a id="index--c-api-2"></a>

##### [C++ API](#api-cpp-html)

<a id="index--c-api-3"></a>

##### [C# API](https://avro.apache.org/docs/1.12.0/api/csharp/html/)

<a id="index--python-api"></a>

##### [Python API](https://avro.apache.org/docs/1.12.0/api/py/html/)

<a id="index--mapreduce-guide"></a>

##### [MapReduce guide](#mapreduce-guide)

<a id="index--idl-language"></a>

##### [IDL Language](#idl-language)

<a id="index--sasl-profile"></a>

##### [SASL profile](#sasl-profile)

#####

Last modified April 27, 2026: [Bump postcss from 8.5.10 to 8.5.12 in /doc (#3741) (fed0011)](https://github.com/apache/avro/commit/fed00117056cdc3dad424cf8442c2d38775e4658)

---

<a id="getting-started-java"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/getting-started-java/ -->

<!-- page_index: 2 -->

<a id="getting-started-java--getting-started-java"></a>

# Getting Started (Java)

This is a short guide for getting started with Apache Avro™ using Java. This guide only covers using Avro for data serialization; see Patrick Hunt’s [Avro RPC Quick Start](https://github.com/phunt/avro-rpc-quickstart) for a good introduction to using Avro for RPC.

<a id="getting-started-java--download"></a>

## Download

Avro implementations for C, C++, C#, Java, PHP, Python, and Ruby can be downloaded from the [Apache Avro™ Download](https://avro.apache.org/project/download/) page. This guide uses Avro 1.12.0, the latest version at the time of writing. For the examples in this guide, download avro-1.12.0.jar and avro-tools-1.12.0.jar.

Alternatively, if you are using Maven, add the following dependency to your POM:

```xml
<dependency>
  <groupId>org.apache.avro</groupId>
  <artifactId>avro</artifactId>
  <version>1.12.0</version>
</dependency>
```

As well as the Avro Maven plugin (for performing code generation):

```xml
<plugin>
  <groupId>org.apache.avro</groupId>
  <artifactId>avro-maven-plugin</artifactId>
  <version>1.12.0</version>
  <configuration>
    <sourceDirectory>${project.basedir}/src/main/avro/</sourceDirectory>
    <outputDirectory>${project.basedir}/src/main/java/</outputDirectory>
  </configuration>
  <executions>
    <execution>
      <phase>generate-sources</phase>
      <goals>
        <goal>schema</goal>
      </goals>
    </execution>
  </executions>
</plugin>
<plugin>
  <groupId>org.apache.maven.plugins</groupId>
  <artifactId>maven-compiler-plugin</artifactId>
  <configuration>
    <source>1.8</source>
    <target>1.8</target>
  </configuration>
</plugin>
```

You may also build the required Avro jars from source. Building Avro is beyond the scope of this guide; see the Build Documentation page in the wiki for more information.

<a id="getting-started-java--defining-a-schema"></a>

## Defining a schema

Avro schemas are defined using JSON or IDL (the latter requires an extra dependency). Schemas are composed of primitive types (null, boolean, int, long, float, double, bytes, and string) and complex types (record, enum, array, map, union, and fixed). You can learn more about Avro schemas and types from the specification, but for now let’s start with a simple schema example, user.avsc:

```json
{"namespace": "example.avro",
 "type": "record",
 "name": "User",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": ["int", "null"]},
     {"name": "favorite_color", "type": ["string", "null"]}
 ]
}
```

This schema defines a record representing a hypothetical user. (Note that a schema file can only contain a single schema definition.) At minimum, a record definition must include its type (“type”: “record”), a name (“name”: “User”), and fields, in this case name, favorite\_number, and favorite\_color. We also define a namespace (“namespace”: “example.avro”), which together with the name attribute defines the “full name” of the schema (example.avro.User in this case).

Fields are defined via an array of objects, each of which defines a name and type (other attributes are optional, see the record specification for more details). The type attribute of a field is another schema object, which can be either a primitive or complex type. For example, the name field of our User schema is the primitive type string, whereas the favorite\_number and favorite\_color fields are both unions, represented by JSON arrays. unions are a complex type that can be any of the types listed in the array; e.g., favorite\_number can either be an int or null, essentially making it an optional field.

<a id="getting-started-java--serializing-and-deserializing-with-code-generation"></a>

## Serializing and deserializing with code generation

<a id="getting-started-java--compiling-the-schema"></a>

### Compiling the schema

Code generation allows us to automatically create classes based on our previously-defined schema. Once we have defined the relevant classes, there is no need to use the schema directly in our programs. We use the avro-tools jar to generate code as follows:

```shell
java -jar /path/to/avro-tools-1.12.0.jar compile schema <schema file> <destination>
```

This will generate the appropriate source files in a package based on the schema’s namespace in the provided destination folder. For instance, to generate a User class in package example.avro from the schema defined above, run

```shell
java -jar /path/to/avro-tools-1.12.0.jar compile schema user.avsc .
```

Note that if you using the Avro Maven plugin, there is no need to manually invoke the schema compiler; the plugin automatically performs code generation on any .avsc files present in the configured source directory.

<a id="getting-started-java--creating-users"></a>

### Creating Users

Now that we’ve completed the code generation, let’s create some Users, serialize them to a data file on disk, and then read back the file and deserialize the User objects.

First let’s create some Users and set their fields.

```java
User user1 = new User();
user1.setName("Alyssa");
user1.setFavoriteNumber(256);
// Leave favorite color null

// Alternate constructor
User user2 = new User("Ben", 7, "red");

// Construct via builder
User user3 = User.newBuilder()
             .setName("Charlie")
             .setFavoriteColor("blue")
             .setFavoriteNumber(null)
             .build();
```

As shown in this example, Avro objects can be created either by invoking a constructor directly or by using a builder. Unlike constructors, builders will automatically set any default values specified in the schema. Additionally, builders validate the data as it set, whereas objects constructed directly will not cause an error until the object is serialized. However, using constructors directly generally offers better performance, as builders create a copy of the datastructure before it is written.

Note that we do not set user1’s favorite color. Since that record is of type [“string”, “null”], we can either set it to a string or leave it null; it is essentially optional. Similarly, we set user3’s favorite number to null (using a builder requires setting all fields, even if they are null).

<a id="getting-started-java--serializing"></a>

### Serializing

Now let’s serialize our Users to disk.

```java
// Serialize user1, user2 and user3 to disk
DatumWriter<User> userDatumWriter = new SpecificDatumWriter<User>(User.class);
DataFileWriter<User> dataFileWriter = new DataFileWriter<User>(userDatumWriter);
dataFileWriter.create(user1.getSchema(), new File("users.avro"));
dataFileWriter.append(user1);
dataFileWriter.append(user2);
dataFileWriter.append(user3);
dataFileWriter.close();
```

We create a DatumWriter, which converts Java objects into an in-memory serialized format. The SpecificDatumWriter class is used with generated classes and extracts the schema from the specified generated type.

Next we create a DataFileWriter, which writes the serialized records, as well as the schema, to the file specified in the dataFileWriter.create call. We write our users to the file via calls to the dataFileWriter.append method. When we are done writing, we close the data file.

<a id="getting-started-java--deserializing"></a>

### Deserializing

Finally, let’s deserialize the data file we just created.

```java
// Deserialize Users from disk
DatumReader<User> userDatumReader = new SpecificDatumReader<User>(User.class);
DataFileReader<User> dataFileReader = new DataFileReader<User>(file, userDatumReader);
User user = null;
while (dataFileReader.hasNext()) {
// Reuse user object by passing it to next(). This saves us from
// allocating and garbage collecting many objects for files with
// many items.
user = dataFileReader.next(user);
System.out.println(user);
}
```

This snippet will output:

```json
{"name": "Alyssa", "favorite_number": 256, "favorite_color": null}
{"name": "Ben", "favorite_number": 7, "favorite_color": "red"}
{"name": "Charlie", "favorite_number": null, "favorite_color": "blue"}
```

Deserializing is very similar to serializing. We create a SpecificDatumReader, analogous to the SpecificDatumWriter we used in serialization, which converts in-memory serialized items into instances of our generated class, in this case User. We pass the DatumReader and the previously created File to a DataFileReader, analogous to the DataFileWriter, which reads both the schema used by the writer as well as the data from the file on disk. The data will be read using the writer’s schema included in the file and the schema provided by the reader, in this case the User class. The writer’s schema is needed to know the order in which fields were written, while the reader’s schema is needed to know what fields are expected and how to fill in default values for fields added since the file was written. If there are differences between the two schemas, they are resolved according to the Schema Resolution specification.

Next we use the DataFileReader to iterate through the serialized Users and print the deserialized object to stdout. Note how we perform the iteration: we create a single User object which we store the current deserialized user in, and pass this record object to every call of dataFileReader.next. This is a performance optimization that allows the DataFileReader to reuse the same User object rather than allocating a new User for every iteration, which can be very expensive in terms of object allocation and garbage collection if we deserialize a large data file. While this technique is the standard way to iterate through a data file, it’s also possible to use for (User user : dataFileReader) if performance is not a concern.

<a id="getting-started-java--compiling-and-running-the-example-code"></a>

### Compiling and running the example code

This example code is included as a Maven project in the examples/java-example directory in the Avro docs. From this directory, execute the following commands to build and run the example:

```shell
$ mvn compile # includes code generation via Avro Maven plugin
$ mvn -q exec:java -Dexec.mainClass=example.SpecificMain
```

<a id="getting-started-java--beta-feature-generating-faster-code"></a>
<a id="getting-started-java--beta-feature:-generating-faster-code"></a>

### Beta feature: Generating faster code

In release 1.9.0, we introduced a new approach to generating code that speeds up decoding of objects by more than 10% and encoding by more than 30% (future performance enhancements are underway). To ensure a smooth introduction of this change into production systems, this feature is controlled by a feature flag, the system property org.apache.avro.specific.use\_custom\_coders. In this first release, this feature is off by default. To turn it on, set the system flag to true at runtime. In the sample above, for example, you could enable the fater coders as follows:

$ mvn -q exec:java -Dexec.mainClass=example.SpecificMain -Dorg.apache.avro.specific.use\_custom\_coders=true

Note that you do not have to recompile your Avro schema to have access to this feature. The feature is compiled and built into your code, and you turn it on and off at runtime using the feature flag. As a result, you can turn it on during testing, for example, and then off in production. Or you can turn it on in production, and quickly turn it off if something breaks.

We encourage the Avro community to exercise this new feature early to help build confidence. (For those paying on demand for compute resources in the cloud, it can lead to meaningful cost savings.) As confidence builds, we will turn this feature on by default, and eventually eliminate the feature flag (and the old code).

<a id="getting-started-java--serializing-and-deserializing-without-code-generation"></a>

## Serializing and deserializing without code generation

Data in Avro is always stored with its corresponding schema, meaning we can always read a serialized item regardless of whether we know the schema ahead of time. This allows us to perform serialization and deserialization without code generation.

Let’s go over the same example as in the previous section, but without using code generation: we’ll create some users, serialize them to a data file on disk, and then read back the file and deserialize the users objects.

<a id="getting-started-java--creating-users-1"></a>
<a id="getting-started-java--creating-users-2"></a>

### Creating users

First, we use a SchemaParser to read our schema definition and create a Schema object.

```java
Schema schema = new SchemaParser().parse(new File("user.avsc")).mainSchema();
```

Using this schema, let’s create some users.

```java
GenericRecord user1 = new GenericData.Record(schema);
user1.put("name", "Alyssa");
user1.put("favorite_number", 256);
// Leave favorite color null

GenericRecord user2 = new GenericData.Record(schema);
user2.put("name", "Ben");
user2.put("favorite_number", 7);
user2.put("favorite_color", "red");
```

Since we’re not using code generation, we use GenericRecords to represent users. GenericRecord uses the schema to verify that we only specify valid fields. If we try to set a non-existent field (e.g., user1.put(“favorite\_animal”, “cat”)), we’ll get an AvroRuntimeException when we run the program.

Note that we do not set user1’s favorite color. Since that record is of type [“string”, “null”], we can either set it to a string or leave it null; it is essentially optional.

<a id="getting-started-java--serializing-1"></a>
<a id="getting-started-java--serializing-2"></a>

### Serializing

Now that we’ve created our user objects, serializing and deserializing them is almost identical to the example above which uses code generation. The main difference is that we use generic instead of specific readers and writers.

First we’ll serialize our users to a data file on disk.

```java
// Serialize user1 and user2 to disk
File file = new File("users.avro");
DatumWriter<GenericRecord> datumWriter = new GenericDatumWriter<GenericRecord>(schema);
DataFileWriter<GenericRecord> dataFileWriter = new DataFileWriter<GenericRecord>(datumWriter);
dataFileWriter.create(schema, file);
dataFileWriter.append(user1);
dataFileWriter.append(user2);
dataFileWriter.close();
```

We create a DatumWriter, which converts Java objects into an in-memory serialized format. Since we are not using code generation, we create a GenericDatumWriter. It requires the schema both to determine how to write the GenericRecords and to verify that all non-nullable fields are present.

As in the code generation example, we also create a DataFileWriter, which writes the serialized records, as well as the schema, to the file specified in the dataFileWriter.create call. We write our users to the file via calls to the dataFileWriter.append method. When we are done writing, we close the data file.

<a id="getting-started-java--deserializing-1"></a>
<a id="getting-started-java--deserializing-2"></a>

### Deserializing

Finally, we’ll deserialize the data file we just created.

```java
// Deserialize users from disk
DatumReader<GenericRecord> datumReader = new GenericDatumReader<GenericRecord>(schema);
DataFileReader<GenericRecord> dataFileReader = new DataFileReader<GenericRecord>(file, datumReader);
GenericRecord user = null;
while (dataFileReader.hasNext()) {
// Reuse user object by passing it to next(). This saves us from
// allocating and garbage collecting many objects for files with
// many items.
user = dataFileReader.next(user);
System.out.println(user);
```

This outputs:

```json
{"name": "Alyssa", "favorite_number": 256, "favorite_color": null}
{"name": "Ben", "favorite_number": 7, "favorite_color": "red"}
```

Deserializing is very similar to serializing. We create a GenericDatumReader, analogous to the GenericDatumWriter we used in serialization, which converts in-memory serialized items into GenericRecords. We pass the DatumReader and the previously created File to a DataFileReader, analogous to the DataFileWriter, which reads both the schema used by the writer as well as the data from the file on disk. The data will be read using the writer’s schema included in the file, and the reader’s schema provided to the GenericDatumReader. The writer’s schema is needed to know the order in which fields were written, while the reader’s schema is needed to know what fields are expected and how to fill in default values for fields added since the file was written. If there are differences between the two schemas, they are resolved according to the Schema Resolution specification.

Next, we use the DataFileReader to iterate through the serialized users and print the deserialized object to stdout. Note how we perform the iteration: we create a single GenericRecord object which we store the current deserialized user in, and pass this record object to every call of dataFileReader.next. This is a performance optimization that allows the DataFileReader to reuse the same record object rather than allocating a new GenericRecord for every iteration, which can be very expensive in terms of object allocation and garbage collection if we deserialize a large data file. While this technique is the standard way to iterate through a data file, it’s also possible to use for (GenericRecord user : dataFileReader) if performance is not a concern.

<a id="getting-started-java--compiling-and-running-the-example-code-1"></a>
<a id="getting-started-java--compiling-and-running-the-example-code-2"></a>

### Compiling and running the example code

This example code is included as a Maven project in the examples/java-example directory in the Avro docs. From this directory, execute the following commands to build and run the example:

```shell
$ mvn compile
$ mvn -q exec:java -Dexec.mainClass=example.GenericMain
```

Last modified April 27, 2026: [Bump postcss from 8.5.10 to 8.5.12 in /doc (#3741) (fed0011)](https://github.com/apache/avro/commit/fed00117056cdc3dad424cf8442c2d38775e4658)

---

<a id="getting-started-python"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/getting-started-python/ -->

<!-- page_index: 3 -->

<a id="getting-started-python--getting-started-python"></a>

# Getting Started (Python)

This is a short guide for getting started with Apache Avro™ using Python. This guide only covers using Avro for data serialization; see Patrick Hunt’s Avro RPC Quick Start for a good introduction to using Avro for RPC.

<a id="getting-started-python--notice-for-python-3-users"></a>

> [!NOTE]
> ## Notice for Python 3 users

A package called “avro-python3” had been provided to support Python 3 previously, but the codebase was consolidated into the “avro” package and that supports both Python 2 and 3 now. The avro-python3 package will be removed in the near future, so users should use the “avro” package instead. They are mostly API compatible, but there’s a few minor difference (e.g., function name capitalization, such as avro.schema.Parse vs avro.schema.parse).

<a id="getting-started-python--download"></a>

## Download

For Python, the easiest way to get started is to install it from PyPI. Python’s Avro API is available over PyPi.

```shell
$ python3 -m pip install avro
```

The official releases of the Avro implementations for C, C++, C#, Java, PHP, Python, and Ruby can be downloaded from the Apache Avro™ Releases page. This guide uses Avro 1.12.0, the latest version at the time of writing. Download and unzip avro-1.12.0.tar.gz, and install via python setup.py (this will probably require root privileges). Ensure that you can import avro from a Python prompt.

```shell
$ tar xvf avro-1.12.0.tar.gz
$ cd avro-1.12.0
$ python setup.py install
$ python >>> import avro # should not raise ImportError
```

Alternatively, you may build the Avro Python library from source. From your the root Avro directory, run the commands

```shell
$ cd lang/py/
$ python3 -m pip install -e .
$ python
```

<a id="getting-started-python--defining-a-schema"></a>

## Defining a schema

Avro schemas are defined using JSON. Schemas are composed of primitive types (null, boolean, int, long, float, double, bytes, and string) and complex types (record, enum, array, map, union, and fixed). You can learn more about Avro schemas and types from the specification, but for now let’s start with a simple schema example, user.avsc:

```json
{"namespace": "example.avro",
 "type": "record",
 "name": "User",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": ["int", "null"]},
     {"name": "favorite_color", "type": ["string", "null"]}
 ]
}
```

This schema defines a record representing a hypothetical user. (Note that a schema file can only contain a single schema definition.) At minimum, a record definition must include its type (“type”: “record”), a name (“name”: “User”), and fields, in this case name, favorite\_number, and favorite\_color. We also define a namespace (“namespace”: “example.avro”), which together with the name attribute defines the “full name” of the schema (example.avro.User in this case).

Fields are defined via an array of objects, each of which defines a name and type (other attributes are optional, see the record specification for more details). The type attribute of a field is another schema object, which can be either a primitive or complex type. For example, the name field of our User schema is the primitive type string, whereas the favorite\_number and favorite\_color fields are both unions, represented by JSON arrays. unions are a complex type that can be any of the types listed in the array; e.g., favorite\_number can either be an int or null, essentially making it an optional field.

<a id="getting-started-python--serializing-and-deserializing-without-code-generation"></a>

## Serializing and deserializing without code generation

Data in Avro is always stored with its corresponding schema, meaning we can always read a serialized item, regardless of whether we know the schema ahead of time. This allows us to perform serialization and deserialization without code generation. Note that the Avro Python library does not support code generation.

Try running the following code snippet, which serializes two users to a data file on disk, and then reads back and deserializes the data file:

```python
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

schema = avro.schema.parse(open("user.avsc", "rb").read())

writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open("users.avro", "rb"), DatumReader())
for user in reader:
    print(user)
reader.close()
```

This outputs:

```json
{'favorite_color': None, 'favorite_number': 256, 'name': 'Alyssa'}
{'favorite_color': 'red', 'favorite_number': 7, 'name': 'Ben'}
```

Do make sure that you open your files in binary mode (i.e. using the modes wb or rb respectively). Otherwise you might generate corrupt files due to automatic replacement of newline characters with the platform-specific representations.

Let’s take a closer look at what’s going on here.

```python
schema = avro.schema.parse(open("user.avsc", "rb").read())
```

avro.schema.parse takes a string containing a JSON schema definition as input and outputs a avro.schema.Schema object (specifically a subclass of Schema, in this case RecordSchema). We’re passing in the contents of our user.avsc schema file here.

```python
writer = DataFileWriter(open("users.avro", "wb"), DatumWriter(), schema)
```

We create a DataFileWriter, which we’ll use to write serialized items to a data file on disk. The DataFileWriter constructor takes three arguments:

- The file we’ll serialize to
- A DatumWriter, which is responsible for actually serializing the items to Avro’s binary format (DatumWriters can be used separately from DataFileWriters, e.g., to perform IPC with Avro).
- The schema we’re using. The DataFileWriter needs the schema both to write the schema to the data file, and to verify that the items we write are valid items and write the appropriate fields.

```python
writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
```

We use DataFileWriter.append to add items to our data file. Avro records are represented as Python dicts. Since the field favorite\_color has type [“string”, “null”], we are not required to specify this field, as shown in the first append. Were we to omit the required name field, an exception would be raised. Any extra entries not corresponding to a field are present in the dict are ignored.

```python
reader = DataFileReader(open("users.avro", "rb"), DatumReader())
```

We open the file again, this time for reading back from disk. We use a DataFileReader and DatumReader analagous to the DataFileWriter and DatumWriter above.

```python
for user in reader:
    print(user)
```

The DataFileReader is an iterator that returns dicts corresponding to the serialized items.

Last modified April 27, 2026: [Bump postcss from 8.5.10 to 8.5.12 in /doc (#3741) (fed0011)](https://github.com/apache/avro/commit/fed00117056cdc3dad424cf8442c2d38775e4658)

---

<a id="specification"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/specification/ -->

<!-- page_index: 4 -->

<a id="specification--specification"></a>

# Specification

<a id="specification--introduction"></a>

## Introduction

This document defines Apache Avro. It is intended to be the authoritative specification. Implementations of Avro must adhere to this document.

<a id="specification--schema-declaration"></a>

## Schema Declaration

A Schema is represented in [JSON](https://www.json.org/) by one of:

- A JSON string, naming a defined type.
- A JSON object, of the form:

```js
{"type": "typeName", ...attributes...}
```

where *typeName* is either a primitive or derived type name, as defined below. Attributes not defined in this document are permitted as metadata, but must not affect the format of serialized data.

- A JSON array, representing a union of embedded types.

<a id="specification--primitive-types"></a>

## Primitive Types

The set of primitive type names is:

- *null*: no value
- *boolean*: a binary value
- *int*: 32-bit signed integer
- *long*: 64-bit signed integer
- *float*: single precision (32-bit) IEEE 754 floating-point number
- *double*: double precision (64-bit) IEEE 754 floating-point number
- *bytes*: sequence of 8-bit unsigned bytes
- *string*: unicode character sequence

Primitive types have no specified attributes.

Primitive type names are also defined type names. Thus, for example, the schema “string” is equivalent to:

```json
{"type": "string"}
```

<a id="specification--complex-types"></a>

## Complex Types

Avro supports six kinds of complex types: *records*, *enums*, *arrays*, *maps*, *unions* and *fixed*.

<a id="specification--schema-record"></a>
<a id="specification--records"></a>

### Records

Records use the type name “record” and support the following attributes:

- *name*: a JSON string providing the name of the record (required).
- *namespace*, a JSON string that qualifies the name (optional);
- *doc*: a JSON string providing documentation to the user of this schema (optional).
- *aliases*: a JSON array of strings, providing alternate names for this record (optional).
- *fields*: a JSON array, listing fields (required). Each field is a JSON object with the following attributes:
  - *name*: a JSON string providing the name of the field (required), and
  - *doc*: a JSON string describing this field for users (optional).
  - *type*: a [schema](#specification--schema-declaration "Schema declaration"), as defined above
  - *order*: specifies how this field impacts sort ordering of this record (optional). Valid values are “ascending” (the default), “descending”, or “ignore”. For more details on how this is used, see the sort order section below.
  - *aliases*: a JSON array of strings, providing alternate names for this field (optional).
  - *default*: A default value for this field, only used when reading instances that lack the field for schema evolution purposes. The presence of a default value does not make the field optional at encoding time. Permitted values depend on the field’s schema type, according to the table below. Default values for union fields correspond to the first schema that matches in the union. Default values for bytes and fixed fields are JSON strings, where Unicode code points 0-255 are mapped to unsigned 8-bit byte values 0-255. Avro encodes a field even if its value is equal to its default.

*field default values*

| **avro type** | **json type** | **example** |
| --- | --- | --- |
| null | null | `null` |
| boolean | boolean | `true` |
| int,long | integer | `1` |
| float,double | number | `1.1` |
| bytes | string | `"\u00FF"` |
| string | string | `"foo"` |
| record | object | `{"a": 1}` |
| enum | string | `"FOO"` |
| array | array | `[1]` |
| map | object | `{"a": 1}` |
| fixed | string | `"\u00ff"` |

For example, a linked-list of 64-bit values may be defined with:

```jsonc
{
  "type": "record",
  "name": "LongList",
  "aliases": ["LinkedLongs"],                      // old name for this
  "fields" : [
    {"name": "value", "type": "long"},             // each element has a long
    {"name": "next", "type": ["null", "LongList"]} // optional next element
  ]
}
```

<a id="specification--enums"></a>

### Enums

Enums use the type name “enum” and support the following attributes:

- *name*: a JSON string providing the name of the enum (required).
- *namespace*, a JSON string that qualifies the name (optional);
- *aliases*: a JSON array of strings, providing alternate names for this enum (optional).
- *doc*: a JSON string providing documentation to the user of this schema (optional).
- *symbols*: a JSON array, listing symbols, as JSON strings (required). All symbols in an enum must be unique; duplicates are prohibited. Every symbol must match the regular expression [A-Za-z\_][A-Za-z0-9\_]\* (the same requirement as for [names](#specification--names "Names")).
- *default*: A default value for this enumeration, used during resolution when the reader encounters a symbol from the writer that isn’t defined in the reader’s schema (optional). The value provided here must be a JSON string that’s a member of the symbols array. See documentation on schema resolution for how this gets used.

For example, playing card suits might be defined with:

```json
{
  "type": "enum",
  "name": "Suit",
  "symbols" : ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
}
```

<a id="specification--arrays"></a>

### Arrays

Arrays use the type name “array” and support a single attribute:

- *items*: the schema of the array’s items.

For example, an array of strings is declared with:

```json
{
  "type": "array",
  "items" : "string",
  "default": []
}
```

<a id="specification--maps"></a>

### Maps

Maps use the type name “map” and support one attribute:

- *values*: the schema of the map’s values.

Map keys are assumed to be strings.

For example, a map from string to long is declared with:

```json
{
  "type": "map",
  "values" : "long",
  "default": {}
}
```

<a id="specification--unions"></a>

### Unions

Unions, as mentioned above, are represented using JSON arrays. For example, `["null", "string"]` declares a schema which may be either a null or string.

(Note that when a [default value](#specification--schema-record "Schema record") is specified for a record field whose type is a union, the type of the default value must match with one element of the union.

Unions may not contain more than one schema with the same type, except for the named types record, fixed and enum. For example, unions containing two array types or two map types are not permitted, but two types with different names are permitted. (Names permit efficient resolution when reading and writing unions.)

Unions may not immediately contain other unions.

<a id="specification--fixed"></a>

### Fixed

Fixed uses the type name “fixed” and supports the following attributes:

- *name*: a string naming this fixed (required).
- *namespace*, a string that qualifies the name (optional);
- *aliases*: a JSON array of strings, providing alternate names for this enum (optional).
- *size*: an integer, specifying the number of bytes per value (required).

For example, 16-byte quantity may be declared with:

```json
{"type": "fixed", "size": 16, "name": "md5"}
```

<a id="specification--names"></a>

### Names

Record, enums and fixed are named types. Each has a fullname that is composed of two parts: a name and a namespace, separated by a dot. Equality of names is defined on the fullname – it is an error to specify two different types with the same name.

Record fields and enum symbols have names as well (but no namespace). Equality of field names and enum symbols is defined within their scope (the record/enum that defines them). It is an error to define multiple fields or enum symbols with the same name in a single type. Fields and enum symbols across scopes are never equal, so field names and enum symbols can be reused in a different type.

The name portion of the fullname of named types, record field names, and enum symbols must:

- start with [A-Za-z\_]
- subsequently contain only [A-Za-z0-9\_]

A namespace is a dot-separated sequence of such names. The empty string may also be used as a namespace to indicate the null namespace. Equality of names (including field names and enum symbols) as well as fullnames is case-sensitive.

The null namespace may not be used in a dot-separated sequence of names. So the grammar for a namespace is:

```
  <empty> | <name>[(<dot><name>)*]
```

In record, enum and fixed definitions, the fullname is determined according to the algorithm below the example:

```
{
  "type": "record",
  "name": "Example",
  "doc": "A simple name (attribute) and no namespace attribute: use the null namespace (\"\"); the fullname is 'Example'.",
  "fields": [
    {
      "name": "inheritNull",
      "type": {
        "type": "enum",
        "name": "Simple",
        "doc": "A simple name (attribute) and no namespace attribute: inherit the null namespace of the enclosing type 'Example'. The fullname is 'Simple'.",
        "symbols": ["a", "b"]
      }
    }, {
      "name": "explicitNamespace",
      "type": {
        "type": "fixed",
        "name": "Simple",
        "namespace": "explicit",
        "doc": "A simple name (attribute) and a namespace (attribute); the fullname is 'explicit.Simple' (this is a different type than of the 'inheritNull' field).",
        "size": 12
      }
    }, {
      "name": "fullName",
      "type": {
        "type": "record",
        "name": "a.full.Name",
        "namespace": "ignored",
        "doc": "A name attribute with a fullname, so the namespace attribute is ignored. The fullname is 'a.full.Name', and the namespace is 'a.full'.",
        "fields": [
          {
            "name": "inheritNamespace",
            "type": {
              "type": "enum",
              "name": "Understanding",
              "doc": "A simple name (attribute) and no namespace attribute: inherit the namespace of the enclosing type 'a.full.Name'. The fullname is 'a.full.Understanding'.",
              "symbols": ["d", "e"]
            }
          }
        ]
      }
    }
  ]
}
```

The fullname of a record, enum or fixed definition is determined by the required `name` and optional `namespace` attributes like this:

- A fullname is specified. If the name specified contains a dot, then it is assumed to be a fullname, and any namespace also specified is ignored. For example, use “name”: “org.foo.X” to indicate the fullname org.foo.X.
- A simple name (a name that contains no dots) and namespace are both specified. For example, one might use “name”: “X”, “namespace”: “org.foo” to indicate the fullname org.foo.X.
- A simple name only is specified (a name that contains no dots). In this case the namespace is taken from the most tightly enclosing named schema or protocol, and the fullname is constructed from that namespace and the name. For example, if “name”: “X” is specified, and this occurs within a field of the record definition of org.foo.Y, then the fullname is org.foo.X. This also happens if there is no enclosing namespace (i.e., the enclosing schema definition has the null namespace).

References to previously defined names are as in the latter two cases above: if they contain a dot they are a fullname, if they do not contain a dot, the namespace is the namespace of the enclosing definition.

Primitive type names (`null`, `boolean`, `int`, `long`, `float`, `double`, `bytes`, `string`) have no namespace and their names may not be defined in any namespace.

Complex types (`record`, `enum`, `array`, `map`, `fixed`) have no namespace, but their names (as well as `union`) are permitted to be reused as type names. This can be confusing to the human reader, but is always unambiguous for binary serialization. Due to the limitations of JSON encoding, it is a best practice to use a namespace when using these names.

A schema or protocol may not contain multiple definitions of a fullname. Further, a name must be defined before it is used (“before” in the depth-first, left-to-right traversal of the JSON parse tree, where the types attribute of a protocol is always deemed to come “before” the messages attribute.)

<a id="specification--aliases"></a>

### Aliases

Named types and fields may have aliases. An implementation may optionally use aliases to map a writer’s schema to the reader’s. This facilitates both schema evolution as well as processing disparate datasets.

Aliases function by re-writing the writer’s schema using aliases from the reader’s schema. For example, if the writer’s schema was named “Foo” and the reader’s schema is named “Bar” and has an alias of “Foo”, then the implementation would act as though “Foo” were named “Bar” when reading. Similarly, if data was written as a record with a field named “x” and is read as a record with a field named “y” with alias “x”, then the implementation would act as though “x” were named “y” when reading.

A type alias may be specified either as a fully namespace-qualified, or relative to the namespace of the name it is an alias for. For example, if a type named “a.b” has aliases of “c” and “x.y”, then the fully qualified names of its aliases are “a.c” and “x.y”.

Aliases are alternative names, and thus subject to the same uniqueness constraints as names. Aliases should be valid names, but this is not required: any string is accepted as an alias. When aliases are used “to map a writer’s schema to the reader’s” (see above), this allows schema evolution to correct illegal names in old schemata.

<a id="specification--fixing-an-invalid-but-previously-accepted-schema"></a>

## Fixing an invalid, but previously accepted, schema

Over time, rules and validations on schemas have changed. It is therefore possible that a schema used to work with an older version of Avro, but now fails to parse.

This can have several reasons, as listed below. Each reason also describes a fix, which can be applied using [schema resolution](#specification--schema-resolution): you fix the problems in the schema in a way that is compatible, and then you can use the new schema to read the old data.

<a id="specification--invalid-names"></a>

### Invalid names

Invalid names of types and fields can be corrected by renaming (using an [alias](#specification--aliases)). This works for simple names, namespaces and fullnames.

This fix is twofold: first, you add the invalid name as an alias to the type/field. Then, you change the name to any valid name.

<a id="specification--invalid-defaults"></a>

### Invalid defaults

Default values are only used to fill in missing data when reading. Invalid defaults create invalid values in these cases. The fix is to correct the default values.

<a id="specification--data-serialization-and-deserialization"></a>

## Data Serialization and Deserialization

Binary encoded Avro data does not include type information or field names. The benefit is that the serialized data is small, but as a result a schema must always be used in order to read Avro data correctly. The best way to ensure that the schema is structurally identical to the one used to write the data is to use the exact same schema.

Therefore, files or systems that store Avro data should always include the writer’s schema for that data. Avro-based remote procedure call (RPC) systems must also guarantee that remote recipients of data have a copy of the schema used to write that data. In general, it is advisable that any reader of Avro data should use a schema that is the same (as defined more fully in [Parsing Canonical Form for Schemas](#specification--parsing-canonical-form-for-schemas "Parsing Canonical Form for Schemas")) as the schema that was used to write the data in order to deserialize it correctly. Deserializing data into a newer schema is accomplished by specifying an additional schema, the results of which are described in [Schema Resolution](#specification--schema-resolution).

In general, both serialization and deserialization proceed as a depth-first, left-to-right traversal of the schema, serializing or deserializing primitive types as they are encountered. Therefore, it is possible, though not advisable, to read Avro data with a schema that does not have the same Parsing Canonical Form as the schema with which the data was written. In order for this to work, the serialized primitive values must be compatible, in order value by value, with the items in the deserialization schema. For example, int and long are always serialized the same way, so an int could be deserialized as a long. Since the compatibility of two schemas depends on both the data and the serialization format (eg. binary is more permissive than JSON because JSON includes field names, eg. a long that is too large will overflow an int), it is simpler and more reliable to use schemas with identical Parsing Canonical Form.

<a id="specification--encodings"></a>

### Encodings

Avro specifies two serialization encodings: binary and JSON. Most applications will use the binary encoding, as it is smaller and faster. But, for debugging and web-based applications, the JSON encoding may sometimes be appropriate.

<a id="specification--binary-encoding"></a>

### Binary Encoding

Binary encoding does not include field names, self-contained information about the types of individual bytes, nor field or record separators. Therefore readers are wholly reliant on the schema used when the data was encoded.

<a id="specification--primitive-types-1"></a>
<a id="specification--primitive-types-2"></a>

#### Primitive Types

Primitive types are encoded in binary as follows:

- *null* is written as zero bytes.
- a *boolean* is written as a single byte whose value is either 0 (false) or 1 (true).
- *int* and *long* values are written using [variable-length](https://lucene.apache.org/java/3_5_0/fileformats.html#VInt) [zig-zag](https://code.google.com/apis/protocolbuffers/docs/encoding.html#types) coding. Some examples:

| *value* | *hex* |
| --- | --- |
| 0 | 00 |
| -1 | 01 |
| 1 | 02 |
| -2 | 03 |
| 2 | 04 |
| … | … |
| -64 | 7f |
| 64 | 80 01 |
| … | … |

- a *float* is written as 4 bytes. The float is converted into a 32-bit integer using a method equivalent to Java’s [floatToRawIntBits](https://docs.oracle.com/javase/8/docs/api/java/lang/Float.html#floatToRawIntBits-float-) and then encoded in little-endian format.
- a *double* is written as 8 bytes. The double is converted into a 64-bit integer using a method equivalent to Java’s [doubleToRawLongBits](https://docs.oracle.com/javase/8/docs/api/java/lang/Double.html#doubleToRawLongBits-double-) and then encoded in little-endian format.
- *bytes* are encoded as a long followed by that many bytes of data.
- a *string* is encoded as a long followed by that many bytes of UTF-8 encoded character data.
  For example, the three-character string “foo” would be encoded as the long value 3 (encoded as hex 06) followed by the UTF-8 encoding of ‘f’, ‘o’, and ‘o’ (the hex bytes 66 6f 6f):

```
06 66 6f 6f
```

<a id="specification--complex-types-1"></a>
<a id="specification--complex-types-2"></a>

### Complex Types

Complex types are encoded in binary as follows:

<a id="specification--records-2"></a>

#### Records

A record is encoded by encoding the values of its fields in the order that they are declared. In other words, a record is encoded as just the concatenation of the encodings of its fields. Field values are encoded per their schema.

For example, the record schema

```json
{
  "type": "record",
  "name": "test",
  "fields" : [
    {"name": "a", "type": "long"},
    {"name": "b", "type": "string"}
  ]
}
```

An instance of this record whose a field has value 27 (encoded as hex 36) and whose b field has value “foo” (encoded as hex bytes 06 66 6f 6f), would be encoded simply as the concatenation of these, namely the hex byte sequence:

```
36 06 66 6f 6f
```

<a id="specification--enums-1"></a>
<a id="specification--enums-2"></a>

#### Enums

An enum is encoded by a int, representing the zero-based position of the symbol in the schema.

For example, consider the enum:

```json
{"type": "enum", "name": "Foo", "symbols": ["A", "B", "C", "D"] }
```

This would be encoded by an int between zero and three, with zero indicating “A”, and 3 indicating “D”.

<a id="specification--arrays-1"></a>
<a id="specification--arrays-2"></a>

#### Arrays

Arrays are encoded as a series of blocks. Each block consists of a long count value, followed by that many array items. A block with count zero indicates the end of the array. Each item is encoded per the array’s item schema.

If a block’s count is negative, its absolute value is used, and the count is followed immediately by a long block size indicating the number of bytes in the block. This block size permits fast skipping through data, e.g., when projecting a record to a subset of its fields.

For example, the array schema

```json
{"type": "array", "items": "long"}
```

an array containing the items 3 and 27 could be encoded as the long value 2 (encoded as hex 04) followed by long values 3 and 27 (encoded as hex 06 36) terminated by zero:

```
04 06 36 00
```

The blocked representation permits one to read and write arrays larger than can be buffered in memory, since one can start writing items without knowing the full length of the array.

<a id="specification--schema-maps"></a>
<a id="specification--maps-2"></a>

#### Maps

Maps are encoded as a series of *blocks*. Each block consists of a `long` *count* value, followed by that many key/value pairs. A block with count zero indicates the end of the map. Each item is encoded per the map’s value schema.

If a block’s count is negative, its absolute value is used, and the count is followed immediately by a `long` block size indicating the number of bytes in the block. This block size permits fast skipping through data, e.g., when projecting a record to a subset of its fields.

The blocked representation permits one to read and write maps larger than can be buffered in memory, since one can start writing items without knowing the full length of the map.

<a id="specification--unions-1"></a>
<a id="specification--unions-2"></a>

#### Unions

A union is encoded by first writing an `int` value indicating the zero-based position within the union of the schema of its value. The value is then encoded per the indicated schema within the union.

For example, the union schema `["null","string"]` would encode:

- *null* as zero (the index of “null” in the union):
  `00`
- the string “a” as one (the index of “string” in the union, 1, encoded as hex 02), followed by the serialized string:
  `02 02 61`
  NOTE: Currently for C/C++ implementations, the positions are practically an int, but theoretically a long. In reality, we don’t expect unions with 215M members

<a id="specification--fixed-1"></a>
<a id="specification--fixed-2"></a>

#### Fixed

Fixed instances are encoded using the number of bytes declared in the schema.

<a id="specification--json-encoding"></a>

### JSON Encoding

Except for unions, the JSON encoding is the same as is used to encode [field default values](#specification--schema-record).

The value of a union is encoded in JSON as follows:

- if its type is *null*, then it is encoded as a JSON *null*;
- otherwise it is encoded as a JSON object with one name/value pair whose name is the type’s name and whose value is the recursively encoded value. For Avro’s named types (record, fixed or enum) the user-specified name is used, for other types the type name is used.

For example, the union schema `["null","string","Foo"]`, where Foo is a record name, would encode:

- *null* as *null*;
- the string “a” as `{"string": "a"}` and
- a Foo instance as `{"Foo": {...}}`, where `{...}` indicates the JSON encoding of a Foo instance.

Note that the original schema is still required to correctly process JSON-encoded data. For example, the JSON encoding does not distinguish between *int* and *long*, *float* and *double*, records and maps, enums and strings, etc.

<a id="specification--single-object-encoding"></a>

### Single-object encoding

In some situations a single Avro serialized object is to be stored for a longer period of time. One very common example is storing Avro records for several weeks in an [Apache Kafka](https://kafka.apache.org/) topic.

In the period after a schema change this persistence system will contain records that have been written with different schemas. So the need arises to know which schema was used to write a record to support schema evolution correctly. In most cases the schema itself is too large to include in the message, so this binary wrapper format supports the use case more effectively.

<a id="specification--single-object-encoding-specification"></a>

#### Single object encoding specification

Single Avro objects are encoded as follows:

1. A two-byte marker, `C3 01`, to show that the message is Avro and uses this single-record format (version 1).
2. The 8-byte little-endian CRC-64-AVRO [fingerprint](#specification--schema-fingerprints "Schema fingerprints") of the object’s schema.
3. The Avro object encoded using [Avro’s binary encoding](#specification--binary-encoding).

Implementations use the 2-byte marker to determine whether a payload is Avro. This check helps avoid expensive lookups that resolve the schema from a fingerprint, when the message is not an encoded Avro payload.

<a id="specification--sort-order"></a>

## Sort Order

Avro defines a standard sort order for data. This permits data written by one system to be efficiently sorted by another system. This can be an important optimization, as sort order comparisons are sometimes the most frequent per-object operation. Note also that Avro binary-encoded data can be efficiently ordered without deserializing it to objects.

Data items may only be compared if they have identical schemas. Pairwise comparisons are implemented recursively with a depth-first, left-to-right traversal of the schema. The first mismatch encountered determines the order of the items.

Two items with the same schema are compared according to the following rules.

- *null* data is always equal.
- *boolean* data is ordered with false before true.
- *int*, *long*, *float* and *double* data is ordered by ascending numeric value.
- *bytes* and fixed data are compared lexicographically by unsigned 8-bit values.
- *string* data is compared lexicographically by Unicode code point. Note that since UTF-8 is used as the binary encoding for strings, sorting of bytes and string binary data is identical.
- *array* data is compared lexicographically by element.
- *enum* data is ordered by the symbol’s position in the enum schema. For example, an enum whose symbols are `["z", "a"]` would sort “z” values before “a” values.
- *union* data is first ordered by the branch within the union, and, within that, by the type of the branch. For example, an `["int", "string"]` union would order all int values before all string values, with the ints and strings themselves ordered as defined above.
- *record* data is ordered lexicographically by field. If a field specifies that its order is:
  - “ascending”, then the order of its values is unaltered.
  - “descending”, then the order of its values is reversed.
  - “ignore”, then its values are ignored when sorting.
- *map* data may not be compared. It is an error to attempt to compare data containing maps unless those maps are in an `"order":"ignore"` record field.

<a id="specification--object-container-files"></a>

## Object Container Files

Avro includes a simple object container file format. A file has a schema, and all objects stored in the file must be written according to that schema, using binary encoding. Objects are stored in blocks that may be compressed. Syncronization markers are used between blocks to permit efficient splitting of files for MapReduce processing.

Files may include arbitrary user-specified metadata.

A file consists of:

- A file header, followed by
- one or more file data blocks.

A file header consists of:

- Four bytes, ASCII ‘O’, ‘b’, ‘j’, followed by 1.
- file metadata, including the schema.
- The 16-byte, randomly-generated sync marker for this file.

File metadata is written as if defined by the following [map](#specification--schema-maps) schema:

```json
{"type": "map", "values": "bytes"}
```

All metadata properties that start with “avro.” are reserved. The following file metadata properties are currently used:

- **avro.schema** contains the schema of objects stored in the file, as JSON data (required).
- **avro.codec** the name of the compression codec used to compress blocks, as a string. Implementations are required to support the following codecs: “null” and “deflate”. If codec is absent, it is assumed to be “null”. The codecs are described with more detail below.

A file header is thus described by the following schema:

```json
{"type": "record", "name": "org.apache.avro.file.Header",
 "fields" : [
   {"name": "magic", "type": {"type": "fixed", "name": "Magic", "size": 4}},
   {"name": "meta", "type": {"type": "map", "values": "bytes"}},
   {"name": "sync", "type": {"type": "fixed", "name": "Sync", "size": 16}}
  ]
}
```

A file data block consists of:

- A long indicating the count of objects in this block.
- A long indicating the size in bytes of the serialized objects in the current block, after any codec is applied
- The serialized objects. If a codec is specified, this is compressed by that codec.
- The file’s 16-byte sync marker.

A file data block is thus described by the following schema:

```json
{"type": "record", "name": "org.apache.avro.file.DataBlock",
 "fields" : [
   {"name": "count", "type": "long"},
   {"name": "data", "type": "bytes"},
   {"name": "sync", "type": {"type": "fixed", "name": "Sync", "size": 16}}
  ]
}
```

Each block’s binary data can be efficiently extracted or skipped without deserializing the contents. The combination of block size, object counts, and sync markers enable detection of corrupt blocks and help ensure data integrity.

<a id="specification--required-codecs"></a>

### Required Codecs

*null*

The “null” codec simply passes through data uncompressed.

*deflate*

The “deflate” codec writes the data block using the deflate algorithm as specified in [RFC 1951](https://www.isi.edu/in-notes/rfc1951.txt), and typically implemented using the zlib library. Note that this format (unlike the “zlib format” in RFC 1950) does not have a checksum.

<a id="specification--optional-codecs"></a>

### Optional Codecs

*bzip2*

The “bzip2” codec uses the [bzip2](https://sourceware.org/bzip2/) compression library.

*snappy*

The “snappy” codec uses Google’s [Snappy](https://code.google.com/p/snappy/) compression library. Each compressed block is followed by the 4-byte, big-endian CRC32 checksum of the uncompressed data in the block.

*xz*

The “xz” codec uses the [XZ](https://tukaani.org/xz/) compression library.

*zstandard*

The “zstandard” codec uses Facebook’s [Zstandard](https://facebook.github.io/zstd/) compression library.

<a id="specification--protocol-declaration"></a>

### Protocol Declaration

Avro protocols describe RPC interfaces. Like schemas, they are defined with JSON text.

A protocol is a JSON object with the following attributes:

- *protocol*, a string, the name of the protocol (required);
- *namespace*, an optional string that qualifies the name (optional);
- *doc*, an optional string describing this protocol;
- *types*, an optional list of definitions of named types (records, enums, fixed and errors). An error definition is just like a record definition except it uses “error” instead of “record”. Note that forward references to named types are not permitted.
- *messages*, an optional JSON object whose keys are message names and whose values are objects whose attributes are described below. No two messages may have the same name.

The name and namespace qualification rules defined for schema objects apply to protocols as well.

<a id="specification--messages"></a>

### Messages

A message has attributes:

- a *doc*, an optional description of the message,
- a *request*, a list of named, typed parameter schemas (this has the same form as the fields of a record declaration);
- a *response* schema;
- an optional union of declared error schemas. The effective union has “string” prepended to the declared union, to permit transmission of undeclared “system” errors. For example, if the declared error union is `["AccessError"]`, then the effective union is `["string", "AccessError"]`. When no errors are declared, the effective error union is `["string"]`. Errors are serialized using the effective union; however, a protocol’s JSON declaration contains only the declared union.
- an optional one-way boolean parameter.

A request parameter list is processed equivalently to an anonymous record. Since record field lists may vary between reader and writer, request parameters may also differ between the caller and responder, and such differences are resolved in the same manner as record field differences.

The one-way parameter may only be true when the response type is `"null"` and no errors are listed.

<a id="specification--sample-protocol"></a>

### Sample Protocol

For example, one may define a simple HelloWorld protocol with:

```json
{
  "namespace": "com.acme",
  "protocol": "HelloWorld",
  "doc": "Protocol Greetings",

  "types": [
    {"name": "Greeting", "type": "record", "fields": [
      {"name": "message", "type": "string"}]},
    {"name": "Curse", "type": "error", "fields": [
      {"name": "message", "type": "string"}]}
  ],

  "messages": {
    "hello": {
      "doc": "Say hello.",
      "request": [{"name": "greeting", "type": "Greeting" }],
      "response": "Greeting",
      "errors": ["Curse"]
    }
  }
}
```

<a id="specification--protocol-wire-format"></a>

## Protocol Wire Format

<a id="specification--message-transport"></a>

### Message Transport

Messages may be transmitted via different transport mechanisms.

To the transport, a *message* is an opaque byte sequence.

A transport is a system that supports:

- **transmission of request messages**
- **receipt of corresponding response messages**
  Servers may send a response message back to the client corresponding to a request message. The mechanism of correspondence is transport-specific. For example, in HTTP it is implicit, since HTTP directly supports requests and responses. But a transport that multiplexes many client threads over a single socket would need to tag messages with unique identifiers.

Transports may be either stateless or stateful. In a stateless transport, messaging assumes no established connection state, while stateful transports establish connections that may be used for multiple messages. This distinction is discussed further in the [handshake](#specification--handshake) section below.

<a id="specification--http-as-transport"></a>

#### HTTP as Transport

When [HTTP](https://www.w3.org/Protocols/rfc2616/rfc2616.html) is used as a transport, each Avro message exchange is an HTTP request/response pair. All messages of an Avro protocol should share a single URL at an HTTP server. Other protocols may also use that URL. Both normal and error Avro response messages should use the 200 (OK) response code. The chunked encoding may be used for requests and responses, but, regardless the Avro request and response are the entire content of an HTTP request and response. The HTTP Content-Type of requests and responses should be specified as “avro/binary”. Requests should be made using the POST method.

HTTP is used by Avro as a stateless transport.

<a id="specification--message-framing"></a>

### Message Framing

Avro messages are *framed* as a list of buffers.

Framing is a layer between messages and the transport. It exists to optimize certain operations.

The format of framed message data is:

- a series of buffers, where each buffer consists of:
  - a four-byte, big-endian *buffer length*, followed by
  - that many bytes of *buffer* data.
- a message is always terminated by a zero-length buffer.

Framing is transparent to request and response message formats (described below). Any message may be presented as a single or multiple buffers.

Framing can permit readers to more efficiently get different buffers from different sources and for writers to more efficiently store different buffers to different destinations. In particular, it can reduce the number of times large binary objects are copied. For example, if an RPC parameter consists of a megabyte of file data, that data can be copied directly to a socket from a file descriptor, and, on the other end, it could be written directly to a file descriptor, never entering user space.

A simple, recommended, framing policy is for writers to create a new segment whenever a single binary object is written that is larger than a normal output buffer. Small objects are then appended in buffers, while larger objects are written as their own buffers. When a reader then tries to read a large object the runtime can hand it an entire buffer directly, without having to copy it.

<a id="specification--handshake"></a>

### Handshake

The purpose of the handshake is to ensure that the client and the server have each other’s protocol definition, so that the client can correctly deserialize responses, and the server can correctly deserialize requests. Both clients and servers should maintain a cache of recently seen protocols, so that, in most cases, a handshake will be completed without extra round-trip network exchanges or the transmission of full protocol text.

RPC requests and responses may not be processed until a handshake has been completed. With a stateless transport, all requests and responses are prefixed by handshakes. With a stateful transport, handshakes are only attached to requests and responses until a successful handshake response has been returned over a connection. After this, request and response payloads are sent without handshakes for the lifetime of that connection.

The handshake process uses the following record schemas:

```json
{
  "type": "record",
  "name": "HandshakeRequest", "namespace":"org.apache.avro.ipc",
  "fields": [
    {"name": "clientHash",
     "type": {"type": "fixed", "name": "MD5", "size": 16}},
    {"name": "clientProtocol", "type": ["null", "string"]},
    {"name": "serverHash", "type": "MD5"},
    {"name": "meta", "type": ["null", {"type": "map", "values": "bytes"}]}
  ]
}
{
  "type": "record",
  "name": "HandshakeResponse", "namespace": "org.apache.avro.ipc",
  "fields": [
    {"name": "match",
     "type": {"type": "enum", "name": "HandshakeMatch",
              "symbols": ["BOTH", "CLIENT", "NONE"]}},
    {"name": "serverProtocol",
     "type": ["null", "string"]},
    {"name": "serverHash",
     "type": ["null", {"type": "fixed", "name": "MD5", "size": 16}]},
    {"name": "meta",
     "type": ["null", {"type": "map", "values": "bytes"}]}
  ]
}
```

- A client first prefixes each request with a `HandshakeRequest` containing just the hash of its protocol and of the server’s protocol (`clientHash!=null, clientProtocol=null, serverHash!=null`), where the hashes are 128-bit MD5 hashes of the JSON protocol text. If a client has never connected to a given server, it sends its hash as a guess of the server’s hash, otherwise it sends the hash that it previously obtained from this server.
  The server responds with a HandshakeResponse containing one of:
  - `match=BOTH, serverProtocol=null, serverHash=null` if the client sent the valid hash of the server’s protocol and the server knows what protocol corresponds to the client’s hash. In this case, the request is complete and the response data immediately follows the HandshakeResponse.
  - `match=CLIENT, serverProtocol!=null, serverHash!=null` if the server has previously seen the client’s protocol, but the client sent an incorrect hash of the server’s protocol. The request is complete and the response data immediately follows the HandshakeResponse. The client must use the returned protocol to process the response and should also cache that protocol and its hash for future interactions with this server.
  - `match=NONE` if the server has not previously seen the client’s protocol. The serverHash and serverProtocol may also be non-null if the server’s protocol hash was incorrect.
    In this case the client must then re-submit its request with its protocol text (`clientHash!=null, clientProtocol!=null, serverHash!=null`) and the server should respond with a successful match (match=BOTH, serverProtocol=null, serverHash=null) as above.

The meta field is reserved for future handshake enhancements.

<a id="specification--call-format"></a>

### Call Format

A *call* consists of a request message paired with its resulting response or error message. Requests and responses contain extensible metadata, and both kinds of messages are framed as described above.

The format of a call request is:

- *request metadata*, a map with values of type bytes
- the *message name*, an Avro string, followed by
- the *message parameters*. Parameters are serialized according to the message’s request declaration.
  When the empty string is used as a message name a server should ignore the parameters and return an empty response. A client may use this to ping a server or to perform a handshake without sending a protocol message.

When a message is declared one-way and a stateful connection has been established by a successful handshake response, no response data is sent. Otherwise the format of the call response is:

- *response metadata*, a map with values of type bytes
- a one-byte error *flag* boolean, followed by either:
  - if the error flag is false, the message *response*, serialized per the message’s response schema.
  - if the error flag is true, the *error*, serialized per the message’s effective error union schema.

<a id="specification--schema-resolution"></a>

### Schema Resolution

A reader of Avro data, whether from an RPC or a file, can always parse that data because the original schema must be provided along with the data. However, the reader may be programmed to read data into a different schema. For example, if the data was written with a different version of the software than it is read, then fields may have been added or removed from records. This section specifies how such schema differences should be resolved.

We refer to the schema used to write the data as the writer’s schema, and the schema that the application expects the reader’s schema. Differences between these should be resolved as follows:

- It is an error if the two schemas do not *match*.
  To match, one of the following must hold:

  - both schemas are arrays whose item types match
  - both schemas are maps whose value types match
  - both schemas are enums whose (unqualified) names match
  - both schemas are fixed whose sizes and (unqualified) names match
  - both schemas are records with the same (unqualified) name
  - either schema is a union
  - both schemas have same primitive type
  - the writer’s schema may be promoted to the reader’s as follows:
    - int is promotable to long, float, or double
    - long is promotable to float or double
    - float is promotable to double
    - string is promotable to bytes
    - bytes is promotable to string
- **if both are records**:

  - the ordering of fields may be different: fields are matched by name.
  - schemas for fields with the same name in both records are resolved recursively.
  - if the writer’s record contains a field with a name not present in the reader’s record, the writer’s value for that field is ignored.
  - if the reader’s record schema has a field that contains a default value, and writer’s schema does not have a field with the same name, then the reader should use the default value from its field.
  - if the reader’s record schema has a field with no default value, and writer’s schema does not have a field with the same name, an error is signalled.
- **if both are enums**:
  if the writer’s symbol is not present in the reader’s enum and the reader has a default value, then that value is used, otherwise an error is signalled.
- **if both are arrays**:
  This resolution algorithm is applied recursively to the reader’s and writer’s array item schemas.
- **if both are maps**:
  This resolution algorithm is applied recursively to the reader’s and writer’s value schemas.
- **if both are unions**:
  The first schema in the reader’s union that matches the selected writer’s union schema is recursively resolved against it. if none match, an error is signalled.
- **if reader’s is a union, but writer’s is not**
  The first schema in the reader’s union that matches the writer’s schema is recursively resolved against it. If none match, an error is signalled.
- **if writer’s is a union, but reader’s is not**
  If the reader’s schema matches the selected writer’s schema, it is recursively resolved against it. If they do not match, an error is signalled.

A schema’s *doc* fields are ignored for the purposes of schema resolution. Hence, the *doc* portion of a schema may be dropped at serialization.

<a id="specification--parsing-canonical-form-for-schemas"></a>

### Parsing Canonical Form for Schemas

One of the defining characteristics of Avro is that a reader must use the schema used by the writer of the data in order to know how to read the data. This assumption results in a data format that’s compact and also amenable to many forms of schema evolution. However, the specification so far has not defined what it means for the reader to have the “same” schema as the writer. Does the schema need to be textually identical? Well, clearly adding or removing some whitespace to a JSON expression does not change its meaning. At the same time, reordering the fields of records clearly does change the meaning. So what does it mean for a reader to have “the same” schema as a writer?

Parsing Canonical Form is a transformation of a writer’s schema that let’s us define what it means for two schemas to be “the same” for the purpose of reading data written against the schema. It is called Parsing Canonical Form because the transformations strip away parts of the schema, like “doc” attributes, that are irrelevant to readers trying to parse incoming data. It is called Canonical Form because the transformations normalize the JSON text (such as the order of attributes) in a way that eliminates unimportant differences between schemas. If the Parsing Canonical Forms of two different schemas are textually equal, then those schemas are “the same” as far as any reader is concerned, i.e., there is no serialized data that would allow a reader to distinguish data generated by a writer using one of the original schemas from data generated by a writing using the other original schema. (We sketch a proof of this property in a companion document.)

The next subsection specifies the transformations that define Parsing Canonical Form. But with a well-defined canonical form, it can be convenient to go one step further, transforming these canonical forms into simple integers (“fingerprints”) that can be used to uniquely identify schemas. The subsection after next recommends some standard practices for generating such fingerprints.

<a id="specification--transforming-into-parsing-canonical-form"></a>

#### Transforming into Parsing Canonical Form

Assuming an input schema (in JSON form) that’s already UTF-8 text for a *valid* Avro schema (including all quotes as required by JSON), the following transformations will produce its Parsing Canonical Form:

- [PRIMITIVES] Convert primitive schemas to their simple form (e.g., int instead of `{"type":"int"}`).
- [FULLNAMES] Replace short names with fullnames, using applicable namespaces to do so. Then eliminate namespace attributes, which are now redundant.
- [STRIP] Keep only attributes that are relevant to parsing data, which are: *type*, *name*, *fields*, *symbols*, *items*, *values*, *size*. Strip all others (e.g., *doc* and *aliases*).
- [ORDER] Order the appearance of fields of JSON objects as follows: *name*, *type*, *fields*, *symbols*, *items*, *values*, *size*. For example, if an object has *type*, *name*, and *size* fields, then the *name* field should appear first, followed by the *type* and then the *size* fields.
- [STRINGS] For all JSON string literals in the schema text, replace any escaped characters (e.g., \uXXXX escapes) with their UTF-8 equivalents.
- [INTEGERS] Eliminate quotes around and any leading zeros in front of JSON integer literals (which appear in the *size* attributes of *fixed* schemas).
- [WHITESPACE] Eliminate all whitespace in JSON outside of string literals.

<a id="specification--schema-fingerprints"></a>

#### Schema Fingerprints

“[A] fingerprinting algorithm is a procedure that maps an arbitrarily large data item (such as a computer file) to a much shorter bit string, its fingerprint, that uniquely identifies the original data for all practical purposes” (quoted from [Wikipedia](https://en.wikipedia.org/wiki/Fingerprint_(computing))). In the Avro context, fingerprints of Parsing Canonical Form can be useful in a number of applications; for example, to cache encoder and decoder objects, to tag data items with a short substitute for the writer’s full schema, and to quickly negotiate common-case schemas between readers and writers.

In designing fingerprinting algorithms, there is a fundamental trade-off between the length of the fingerprint and the probability of collisions. To help application designers find appropriate points within this trade-off space, while encouraging interoperability and ease of implementation, we recommend using one of the following three algorithms when fingerprinting Avro schemas:

- When applications can tolerate longer fingerprints, we recommend using the [SHA-256 digest algorithm](https://en.wikipedia.org/wiki/SHA-2) to generate 256-bit fingerprints of Parsing Canonical Forms. Most languages today have SHA-256 implementations in their libraries.
- At the opposite extreme, the smallest fingerprint we recommend is a 64-bit [Rabin fingerprint](https://en.wikipedia.org/wiki/Rabin_fingerprint). Below, we provide pseudo-code for this algorithm that can be easily translated into any programming language. 64-bit fingerprints should guarantee uniqueness for schema caches of up to a million entries (for such a cache, the chance of a collision is 3E-8). We don’t recommend shorter fingerprints, as the chances of collisions is too great (for example, with 32-bit fingerprints, a cache with as few as 100,000 schemas has a 50% chance of having a collision).
- Between these two extremes, we recommend using the [MD5 message digest](https://en.wikipedia.org/wiki/MD5) to generate 128-bit fingerprints. These make sense only where very large numbers of schemas are being manipulated (tens of millions); otherwise, 64-bit fingerprints should be sufficient. As with SHA-256, MD5 implementations are found in most libraries today.

These fingerprints are not meant to provide any security guarantees, even the longer SHA-256-based ones. Most Avro applications should be surrounded by security measures that prevent attackers from writing random data and otherwise interfering with the consumers of schemas. We recommend that these surrounding mechanisms be used to prevent collision and pre-image attacks (i.e., “forgery”) on schema fingerprints, rather than relying on the security properties of the fingerprints themselves.

Rabin fingerprints are [cyclic redundancy checks](https://en.wikipedia.org/wiki/Cyclic_redundancy_check) computed using irreducible polynomials. In the style of the Appendix of [RFC 1952](https://www.ietf.org/rfc/rfc1952.txt) (pg 10), which defines the CRC-32 algorithm, here’s our definition of the 64-bit AVRO fingerprinting algorithm:

```java
long fingerprint64(byte[] buf) {
  if (FP_TABLE == null) initFPTable();
  long fp = EMPTY;
  for (int i = 0; i < buf.length; i++)
    fp = (fp >>> 8) ^ FP_TABLE[(int)(fp ^ buf[i]) & 0xff];
  return fp;
}

static long EMPTY = 0xc15d213aa4d7a795L;
static long[] FP_TABLE = null;

void initFPTable() {
  FP_TABLE = new long[256];
  for (int i = 0; i < 256; i++) {
    long fp = i;
    for (int j = 0; j < 8; j++)
      fp = (fp >>> 1) ^ (EMPTY & -(fp & 1L));
    FP_TABLE[i] = fp;
  }
}
```

Readers interested in the mathematics behind this algorithm may want to read [Chapter 14 of the Second Edition of Hacker’s Delight](https://books.google.com/books?id=XD9iAwAAQBAJ&pg=PA319). (Unlike RFC-1952 and the book chapter, we prepend a single one bit to messages. We do this because CRCs ignore leading zero bits, which can be problematic. Our code prepends a one-bit by initializing fingerprints using EMPTY, rather than initializing using zero as in RFC-1952 and the book chapter.)

<a id="specification--logical-types"></a>

## Logical Types

A logical type is an Avro primitive or complex type with extra attributes to represent a derived type. The attribute `logicalType` must always be present for a logical type, and is a string with the name of one of the logical types listed later in this section. Other attributes may be defined for particular logical types.

A logical type is always serialized using its underlying Avro type so that values are encoded in exactly the same way as the equivalent Avro type that does not have a `logicalType` attribute. Language implementations may choose to represent logical types with an appropriate native type, although this is not required.

Language implementations must ignore unknown logical types when reading, and should use the underlying Avro type. If a logical type is invalid, for example a decimal with scale greater than its precision, then implementations should ignore the logical type and use the underlying Avro type.

<a id="specification--decimal"></a>

### Decimal

The `decimal` logical type represents an arbitrary-precision signed decimal number of the form *unscaled × 10-scale*.

A `decimal` logical type annotates Avro *bytes* or *fixed* types. The byte array must contain the two’s-complement representation of the unscaled integer value in big-endian byte order. The scale is fixed, and is specified using an attribute.

The following attributes are supported:

- *scale*, a JSON integer representing the scale (optional). If not specified the scale is 0.
- *precision*, a JSON integer representing the (maximum) precision of decimals stored in this type (required).
  For example, the following schema represents decimal numbers with a maximum precision of 4 and a scale of 2:

```json
{
  "type": "bytes",
  "logicalType": "decimal",
  "precision": 4,
  "scale": 2
}
```

Precision must be a positive integer greater than zero. If the underlying type is a *fixed*, then the precision is limited by its size. An array of length n can store at most *floor(log10(28 × n - 1 - 1))* base-10 digits of precision.

Scale must be zero or a positive integer less than or equal to the precision.

For the purposes of schema resolution, two schemas that are `decimal` logical types *match* if their scales and precisions match.

**alternative**

As it’s not always possible to fix scale and precision in advance for a decimal field, `big-decimal` is another `decimal` logical type restrict to Avro *bytes*.

*Currently only available in Java and Rust*.

```json
{
  "type": "bytes",
  "logicalType": "big-decimal"
}
```

Here, as scale property is stored in value itself it needs more bytes than preceding `decimal` type, but it allows more flexibility.

<a id="specification--uuid"></a>

### UUID

The `uuid` logical type represents a random generated universally unique identifier (UUID).

A `uuid` logical type annotates an Avro `string` or `fixed` of length 16. Both the string and `fixed` byte layout have to conform with [RFC-4122](https://www.ietf.org/rfc/rfc4122.txt).

The following schemas represent a uuid:

```json
{
  "type": "string",
  "logicalType": "uuid"
}
```

```json
{
  "type": "fixed",
  "size": 16,
  "logicalType": "uuid"
}
```

<a id="specification--date"></a>

### Date

The `date` logical type represents a date within the calendar, with no reference to a particular time zone or time of day.

A `date` logical type annotates an Avro `int`, where the int stores the number of days from the unix epoch, 1 January 1970 (ISO calendar).

The following schema represents a date:

```json
{
  "type": "int",
  "logicalType": "date"
}
```

<a id="specification--time_ms"></a>
<a id="specification--time-millisecond-precision"></a>

### Time (millisecond precision)

The `time-millis` logical type represents a time of day, with no reference to a particular calendar, time zone or date, with a precision of one millisecond.

A `time-millis` logical type annotates an Avro `int`, where the int stores the number of milliseconds after midnight, 00:00:00.000.

<a id="specification--time-microsecond-precision"></a>

### Time (microsecond precision)

The `time-micros` logical type represents a time of day, with no reference to a particular calendar, time zone or date, with a precision of one microsecond.

A `time-micros` logical type annotates an Avro `long`, where the long stores the number of microseconds after midnight, 00:00:00.000000.

<a id="specification--timestamps"></a>

### Timestamps

The `timestamp-{millis,micros,nanos}` logical type represents an instant on the global timeline, independent of a particular time zone or calendar. Upon reading a value back, we can only reconstruct the instant, but not the original representation. In practice, such timestamps are typically displayed to users in their local time zones, therefore they may be displayed differently depending on the execution environment.

- `timestamp-millis`: logical type annotates an Avro `long`, where the long stores the number of milliseconds from the unix epoch, 1 January 1970 00:00:00.000.
- `timestamp-micros`: logical type annotates an Avro `long`, where the long stores the number of microseconds from the unix epoch, 1 January 1970 00:00:00.000000.
- `timestamp-nanos`: logical type annotates an Avro `long`, where the long stores the number of nanoseconds from the unix epoch, 1 January 1970 00:00:00.000000000.

Example: Given an event at noon local time (12:00) on January 1, 2000, in Helsinki where the local time was two hours east of UTC (UTC+2). The timestamp is first shifted to UTC 2000-01-01T10:00:00 and that is then converted to Avro long 946720800000 (milliseconds) and written.

<a id="specification--local_timestamp"></a>
<a id="specification--local-timestamps"></a>

### Local Timestamps

The `local-timestamp-{millis,micros,nanos}` logical type represents a timestamp in a local timezone, regardless of what specific time zone is considered local.

- `local-timestamp-millis`: logical type annotates an Avro `long`, where the long stores the number of milliseconds, from 1 January 1970 00:00:00.000.
- `local-timestamp-micros`: logical type annotates an Avro `long`, where the long stores the number of microseconds, from 1 January 1970 00:00:00.000000.
- `local-timestamp-nanos`: logical type annotates an Avro `long`, where the long stores the number of nanoseconds, from 1 January 1970 00:00:00.000000000.

Example: Given an event at noon local time (12:00) on January 1, 2000, in Helsinki where the local time was two hours east of UTC (UTC+2). The timestamp is converted to Avro long 946728000000 (milliseconds) and then written.

<a id="specification--duration"></a>

### Duration

The `duration` logical type represents an amount of time defined by a number of months, days and milliseconds. This is not equivalent to a number of milliseconds, because, depending on the moment in time from which the duration is measured, the number of days in the month and number of milliseconds in a day may differ. Other standard periods such as years, quarters, hours and minutes can be expressed through these basic periods.

A `duration` logical type annotates Avro `fixed` type of size 12, which stores three little-endian unsigned integers that represent durations at different granularities of time. The first stores a number in months, the second stores a number in days, and the third stores a number in milliseconds.

Last modified April 27, 2026: [Bump postcss from 8.5.10 to 8.5.12 in /doc (#3741) (fed0011)](https://github.com/apache/avro/commit/fed00117056cdc3dad424cf8442c2d38775e4658)

---

<a id="api-java"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/api/java/ -->

<!-- page_index: 5 -->

<a id="api-java--apache-avro-java-1.12.0-api"></a>

# Apache Avro Java 1.12.0 API

Packages

Package

Description

[org.apache.avro](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/package-summary.html)

Avro kernel classes.

[org.apache.avro.avro\_maven\_plugin](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/avro_maven_plugin/package-summary.html)

[org.apache.avro.compiler.schema](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/compiler/schema/package-summary.html)

[org.apache.avro.compiler.specific](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/compiler/specific/package-summary.html)

[org.apache.avro.data](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/data/package-summary.html)

Interfaces and base classes shared by generic, specific and reflect.

[org.apache.avro.file](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/file/package-summary.html)

A container file for Avro data.

[org.apache.avro.generic](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/generic/package-summary.html)

A generic representation for Avro data.

[org.apache.avro.grpc](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/grpc/package-summary.html)

[org.apache.avro.hadoop.file](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/hadoop/file/package-summary.html)

[org.apache.avro.hadoop.io](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/hadoop/io/package-summary.html)

[org.apache.avro.hadoop.util](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/hadoop/util/package-summary.html)

[org.apache.avro.idl](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/idl/package-summary.html)

[org.apache.avro.io](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/io/package-summary.html)

Utilities for Encoding and Decoding Avro data.

[org.apache.avro.io.parsing](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/io/parsing/package-summary.html)

Implementation of Avro schemas as LL(1) grammars.

[org.apache.avro.ipc](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/ipc/package-summary.html)

Support for inter-process calls.

[org.apache.avro.ipc.generic](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/ipc/generic/package-summary.html)

[org.apache.avro.ipc.jetty](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/ipc/jetty/package-summary.html)

[org.apache.avro.ipc.netty](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/ipc/netty/package-summary.html)

[org.apache.avro.ipc.reflect](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/ipc/reflect/package-summary.html)

[org.apache.avro.ipc.specific](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/ipc/specific/package-summary.html)

[org.apache.avro.ipc.stats](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/ipc/stats/package-summary.html)

Utilities to collect and display IPC statistics.

[org.apache.avro.mapred](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/mapred/package-summary.html)

Run [Hadoop](https://hadoop.apache.org/) MapReduce jobs over
Avro data, with map and reduce functions written in Java.

[org.apache.avro.mapred.tether](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/mapred/tether/package-summary.html)

Run [Hadoop](https://hadoop.apache.org/) MapReduce jobs over
Avro data, with map and reduce functions run in a sub-process.

[org.apache.avro.mapreduce](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/mapreduce/package-summary.html)

[org.apache.avro.message](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/message/package-summary.html)

[org.apache.avro.mojo](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/mojo/package-summary.html)

[org.apache.avro.path](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/path/package-summary.html)

Interfaces and base classes for AvroPath.

[org.apache.avro.perf](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/package-summary.html)

[org.apache.avro.perf.test](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/package-summary.html)

[org.apache.avro.perf.test.basic](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/basic/package-summary.html)

[org.apache.avro.perf.test.basic.jmh\_generated](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/basic/jmh_generated/package-summary.html)

[org.apache.avro.perf.test.generic](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/generic/package-summary.html)

[org.apache.avro.perf.test.generic.jmh\_generated](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/generic/jmh_generated/package-summary.html)

[org.apache.avro.perf.test.record](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/record/package-summary.html)

[org.apache.avro.perf.test.record.jmh\_generated](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/record/jmh_generated/package-summary.html)

[org.apache.avro.perf.test.reflect](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/reflect/package-summary.html)

[org.apache.avro.perf.test.reflect.jmh\_generated](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/perf/test/reflect/jmh_generated/package-summary.html)

[org.apache.avro.protobuf](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/protobuf/package-summary.html)

[Protocol Buffer](https://code.google.com/p/protobuf/)
compatibility.

[org.apache.avro.reflect](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/reflect/package-summary.html)

Use Java reflection to generate schemas and protocols for existing
classes.

[org.apache.avro.specific](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/specific/package-summary.html)

Generate specific Java classes for schemas and protocols.

[org.apache.avro.thrift](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/thrift/package-summary.html)

[Thrift](https://thrift.apache.org/) compatibility.

[org.apache.avro.tool](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/tool/package-summary.html)

Avro command-line tool.

[org.apache.avro.util](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/util/package-summary.html)

Common utility classes.

[org.apache.avro.util.springframework](https://avro.apache.org/docs/1.12.0/api/java/org/apache/avro/util/springframework/package-summary.html)

[org.apache.trevni](https://avro.apache.org/docs/1.12.0/api/java/org/apache/trevni/package-summary.html)

A column file format.

[org.apache.trevni.avro](https://avro.apache.org/docs/1.12.0/api/java/org/apache/trevni/avro/package-summary.html)

Read and write [Avro](https://avro.apache.org/) data
in Trevni column files.

[org.apache.trevni.avro.mapreduce](https://avro.apache.org/docs/1.12.0/api/java/org/apache/trevni/avro/mapreduce/package-summary.html)

---

<a id="api-c"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/api/c/ -->

<!-- page_index: 6 -->

# Avro C

The current version of Avro is `1.12.0`. The current version of `libavro` is `24:0:1`.
This document was created `2024-07-25`.

<a id="api-c--_introduction_to_avro"></a>
<a id="api-c--1.-introduction-to-avro"></a>

## 1. Introduction to Avro

Avro is a data serialization system.

Avro provides:

- Rich data structures.
- A compact, fast, binary data format.
- A container file, to store persistent data.
- Remote procedure call (RPC).

This document will focus on the C implementation of Avro. To learn more about
Avro in general, [visit the Avro website](https://avro.apache.org/).

<a id="api-c--_introduction_to_avro_c"></a>
<a id="api-c--2.-introduction-to-avro-c"></a>

## 2. Introduction to Avro C

```
    ___                      ______
   /   |_   ___________     / ____/
  / /| | | / / ___/ __ \   / /
 / ___ | |/ / /  / /_/ /  / /___
/_/  |_|___/_/   \____/   \____/
```

A C program is like a fast dance on a newly waxed dance floor by people carrying razors.

*(walra%moacs11 @ nl.net) 94/03/18*
— Waldi Ravens

The C implementation has been tested on `MacOSX` and `Linux` but, over
time, the number of support OSes should grow. Please let us know if
you’re using `Avro C` on other systems.

Avro depends on the [Jansson JSON parser](http://www.digip.org/jansson/), version 2.3 or higher. On many operating systems this library is
available through your package manager (for example, `apt-get install libjansson-dev` on Ubuntu/Debian, and
`brew install jansson` on Mac OS). If not, please download and install
it from source.

The C implementation supports:

- binary encoding/decoding of all primitive and complex data types
- storage to an Avro Object Container File
- schema resolution, promotion and projection
- validating and non-validating mode for writing Avro data

The C implementation is lacking:

- RPC

To learn about the API, take a look at the examples and reference files
later in this document.

We’re always looking for contributions so, if you’re a C hacker, please
feel free to [submit patches to the project](https://avro.apache.org/).

<a id="api-c--_error_reporting"></a>
<a id="api-c--3.-error-reporting"></a>

## 3. Error reporting

Most functions in the Avro C library return a single `int` status code.
Following the POSIX *errno.h* convention, a status code of 0 indicates
success. Non-zero codes indicate an error condition. Some functions
return a pointer value instead of an `int` status code; for these
functions, a `NULL` pointer indicates an error.

You can retrieve
a string description of the most recent error using the `avro_strerror`
function:

```
avro_schema_t  schema = avro_schema_string();
if (schema == NULL) {
    fprintf(stderr, "Error was %s\n", avro_strerror());
}
```

<a id="api-c--_avro_values"></a>
<a id="api-c--4.-avro-values"></a>

## 4. Avro values

Starting with version 1.6.0, the Avro C library has a new API for
handling Avro data. To help distinguish between the two APIs, we refer
to the old one as the *legacy* or *datum* API, and the new one as the
*value* API. (These names come from the names of the C types used to
represent Avro data in the corresponding API — `avro_datum_t` and
`avro_value_t`.) The legacy API is still present, but it’s deprecated —
you shouldn’t use the `avro_datum_t` type or the `avro_datum_*`
functions in new code.

One main benefit of the new value API is that you can treat any existing
C type as an Avro value; you just have to provide a custom
implementation of the value interface. In addition, we provide a
*generic* value implementation; “generic”, in this sense, meaning that
this single implementation works for instances of any Avro schema type.
Finally, we also provide a wrapper implementation for the deprecated
`avro_datum_t` type, which lets you gradually transition to the new
value API.

<a id="api-c--_avro_value_interface"></a>
<a id="api-c--4.1.-avro-value-interface"></a>

### 4.1. Avro value interface

You interact with Avro values using the *value interface*, which defines
methods for setting and retrieving the contents of an Avro value. An
individual value is represented by an instance of the `avro_value_t`
type.

This section provides an overview of the methods that you can call on an
`avro_value_t` instance. There are quite a few methods in the value
interface, but not all of them make sense for all Avro schema types.
For instance, you won’t be able to call `avro_value_set_boolean` on an
Avro array value. If you try to call an inappropriate method, we’ll
return an `EINVAL`/`AVRO_INVALID` error code.

Note that the functions in this section apply to *all* Avro values, regardless of which value implementation is used under the covers. This
section doesn’t describe how to *create* value instances, since those
constructors will be specific to a particular value implementation.

<a id="api-c--_common_methods"></a>
<a id="api-c--4.1.1.-common-methods"></a>

#### 4.1.1. Common methods

There are a handful of methods that can be used with any value, regardless of which Avro schema it’s an instance of:

```
#include <stdint.h>
#include <avro.h>

avro_type_t avro_value_get_type(const avro_value_t *value);
avro_schema_t avro_value_get_schema(const avro_value_t *value);

int avro_value_equal(const avro_value_t *v1, const avro_value_t *v2);
int avro_value_equal_fast(const avro_value_t *v1, const avro_value_t *v2);

int avro_value_copy(avro_value_t *dest, const avro_value_t *src);
int avro_value_copy_fast(avro_value_t *dest, const avro_value_t *src);

uint32_t avro_value_hash(avro_value_t *value);

int avro_value_reset(avro_value_t *value);
```

The `get_type` and `get_schema` methods can be used to get information
about what kind of Avro value a given `avro_value_t` instance
represents. (For `get_schema`, you borrow the value’s reference to the
schema; if you need to save it and ensure that it outlives the value, you need to call `avro_schema_incref` on it.)

The `equal` and `equal_fast` methods compare two values for equality.
The two values do *not* have to have the same value implementations, but
they *do* have to be instances of the same schema. (Not *equivalent*
schemas; the *same* schema.) The `equal` method checks that the schemas
match; the `equal_fast` method assumes that they do.

The `copy` and `copy_fast` methods copy the contents of one Avro value
into another. (Where possible, this is done without copying the actual
content of a `bytes`, `string`, or `fixed` value, using the
`avro_wrapped_buffer_t` functions described in the next section.) Like
`equal`, the two values must have the same schema; `copy` checks this, while `copy_fast` assumes it.

The `hash` method returns a hash value for the given Avro value. This
can be used to construct hash tables that use Avro values as keys. The
function works correctly even with maps; it produces a hash that doesn’t
depend on the ordering of the elements of the map. Hash values are only
meaningful for comparing values of exactly the same schema. Hash values
are *not* guaranteed to be consistent across different platforms, or
different versions of the Avro library. That means that it’s really
only safe to use these hash values internally within the context of a
single execution of a single application.

The `reset` method “clears out” an `avro_value_t` instance, making sure
that it’s ready to accept the contents of a new value. For scalars, this is usually a no-op, since the new value will just overwrite the old
one. For arrays and maps, this removes any existing elements from the
container, so that we can append the elements of the new value. For
records and unions, this just recursively resets the fields or current
branch.

<a id="api-c--_scalar_values"></a>
<a id="api-c--4.1.2.-scalar-values"></a>

#### 4.1.2. Scalar values

The simplest case is handling instances of the scalar Avro schema types.
In Avro, the scalars are all of the primitive schema types, as well as
`enum` and `fixed` — i.e., anything that can’t contain another Avro
value. Note that we use standard C99 types to represent the primitive
contents of an Avro scalar.

To retrieve the contents of an Avro scalar, you can use one of the
*getter* methods:

```
#include <stdint.h>
#include <stdlib.h>
#include <avro.h>

int avro_value_get_boolean(const avro_value_t *value, int *dest);
int avro_value_get_bytes(const avro_value_t *value,
                         const void **dest, size_t *size);
int avro_value_get_double(const avro_value_t *value, double *dest);
int avro_value_get_float(const avro_value_t *value, float *dest);
int avro_value_get_int(const avro_value_t *value, int32_t *dest);
int avro_value_get_long(const avro_value_t *value, int64_t *dest);
int avro_value_get_null(const avro_value_t *value);
int avro_value_get_string(const avro_value_t *value,
                          const char **dest, size_t *size);
int avro_value_get_enum(const avro_value_t *value, int *dest);
int avro_value_get_fixed(const avro_value_t *value,
                         const void **dest, size_t *size);
```

For the most part, these should be self-explanatory. For `bytes`, `string`, and `fixed` values, the pointer to the underlying content is
`const` — you aren’t allowed to modify the contents directly. We
guarantee that the content of a `string` will be NUL-terminated, so you
can use it as a C string as you’d expect. The `size` returned for a
`string` object will include the NUL terminator; it will be one more
than you’d get from calling `strlen` on the content.

Also, for `bytes`, `string`, and `fixed`, the `dest` and `size`
parameters are optional; if you only want to determine the length of a
`bytes` value, you can use:

```
avro_value_t  *value = /* from somewhere */;
size_t  size;
avro_value_get_bytes(value, NULL, &size);
```

To set the contents of an Avro scalar, you can use one of the *setter*
methods:

```
#include <stdint.h>
#include <stdlib.h>
#include <avro.h>

int avro_value_set_boolean(avro_value_t *value, int src);
int avro_value_set_bytes(avro_value_t *value,
                         void *buf, size_t size);
int avro_value_set_double(avro_value_t *value, double src);
int avro_value_set_float(avro_value_t *value, float src);
int avro_value_set_int(avro_value_t *value, int32_t src);
int avro_value_set_long(avro_value_t *value, int64_t src);
int avro_value_set_null(avro_value_t *value);
int avro_value_set_string(avro_value_t *value, const char *src);
int avro_value_set_string_len(avro_value_t *value,
                              const char *src, size_t size);
int avro_value_set_enum(avro_value_t *value, int src);
int avro_value_set_fixed(avro_value_t *value,
                         void *buf, size_t size);
```

These are also straightforward. For `bytes`, `string`, and `fixed`
values, the `set` methods will make a copy of the underlying data. For
`string` values, the content must be NUL-terminated. You can use
`set_string_len` if you already know the length of the string content;
the length you pass in should include the NUL terminator. If you call
`set_string`, then we’ll use `strlen` to calculate the length.

For `fixed` values, the `size` must match what’s expected by the value’s
underlying `fixed` schema; if the sizes don’t match, you’ll get an error
code.

If you don’t want to copy the contents of a `bytes`, `string`, or
`fixed` value, you can use the *giver* and *grabber* functions:

```
#include <stdint.h>
#include <stdlib.h>
#include <avro.h>

typedef void
(*avro_buf_free_t)(void *ptr, size_t sz, void *user_data);

int avro_value_give_bytes(avro_value_t *value, avro_wrapped_buffer_t *src);
int avro_value_give_string_len(avro_value_t *value, avro_wrapped_buffer_t *src);
int avro_value_give_fixed(avro_value_t *value, avro_wrapped_buffer_t *src);

int avro_value_grab_bytes(const avro_value_t *value, avro_wrapped_buffer_t *dest);
int avro_value_grab_string(const avro_value_t *value, avro_wrapped_buffer_t *dest);
int avro_value_grab_fixed(const avro_value_t *value, avro_wrapped_buffer_t *dest);

typedef struct avro_wrapped_buffer {
    const void  *buf;
    size_t  size;
    void (*free)(avro_wrapped_buffer_t *self);
    int (*copy)(avro_wrapped_buffer_t *dest,
                const avro_wrapped_buffer_t *src,
                size_t offset, size_t length);
    int (*slice)(avro_wrapped_buffer_t *self,
                 size_t offset, size_t length);
} avro_wrapped_buffer_t;

void
avro_wrapped_buffer_free(avro_wrapped_buffer_t *buf);

int
avro_wrapped_buffer_copy(avro_wrapped_buffer_t *dest,
                         const avro_wrapped_buffer_t *src,
                         size_t offset, size_t length);

int
avro_wrapped_buffer_slice(avro_wrapped_buffer_t *self,
                          size_t offset, size_t length);
```

The `give` functions give control of an existing buffer to the value.
(You should **not** try to free the `src` wrapped buffer after calling
this method.) The `grab` function fills in a wrapped buffer with a
pointer to the contents of an Avro value. (You **should** free the `dest`
wrapped buffer when you’re done with it.)

The `avro_wrapped_buffer_t` struct encapsulates the location and size of
the existing buffer. It also includes several methods. The `free`
method will be called when the content of the buffer is no longer
needed. The `slice` method will be called when the wrapped buffer needs
to be updated to point at a subset of what it pointed at before. (This
doesn’t create a new wrapped buffer; it updates an existing one.) The
`copy` method will be called if the content needs to be copied. Note
that if you’re wrapping a buffer with nice reference counting features, you don’t need to perform an actual copy; you just need to ensure that
the `free` function can be called on both the original and the copy, and
not have things blow up.

The “generic” value implementation takes advantage of this feature; if
you pass in a wrapped buffer with a `give` method, and then retrieve it
later with a `grab` method, then we’ll use the wrapped buffer’s `copy`
method to fill in the `dest` parameter. If your wrapped buffer
implements a `slice` method that updates reference counts instead of
actually copying, then you’ve got nice zero-copy access to the contents
of an Avro value.

<a id="api-c--_compound_values"></a>
<a id="api-c--4.1.3.-compound-values"></a>

#### 4.1.3. Compound values

The following sections describe the getter and setter methods for
handling compound Avro values. All of the compound values are
responsible for the storage of their children; this means that there
isn’t a method, for instance, that lets you add an existing
`avro_value_t` to an array. Instead, there’s a method that creates a
new, empty `avro_value_t` of the appropriate type, adds it to the array, and returns it for you to fill in as needed.

You also shouldn’t try to free the child elements that are created this
way; the container value is responsible for their life cycle. The child
element is guaranteed to be valid for as long as the container value
is. You’ll usually define an `avro_value_t` in the stack, and let it
fall out of scope when you’re done with it:

```
avro_value_t  *array = /* from somewhere else */;

{
    avro_value_t  child;
    avro_value_get_by_index(array, 0, &child, NULL);
    /* do something interesting with the array element */
}
```

<a id="api-c--_arrays"></a>
<a id="api-c--4.1.4.-arrays"></a>

#### 4.1.4. Arrays

There are three methods that can be used with array values:

```
#include <stdlib.h>
#include <avro.h>

int avro_value_get_size(const avro_value_t *array, size_t *size);
int avro_value_get_by_index(const avro_value_t *array, size_t index,
                            avro_value_t *element, const char **unused);
int avro_value_append(avro_value_t *array, avro_value_t *element,
                      size_t *new_index);
```

The `get_size` method returns the number of elements currently in the
array. The `get_by_index` method fills in `element` to point at the
array element with the given index. (You should use `NULL` for the
`unused` parameter; it’s ignored for array values.)

The `append` method creates a new value, appends it to the array, and
returns it in `element`. If `new_index` is given, then it will be
filled in with the index of the new element.

<a id="api-c--_maps"></a>
<a id="api-c--4.1.5.-maps"></a>

#### 4.1.5. Maps

There are four methods that can be used with map values:

```
#include <stdlib.h>
#include <avro.h>

int avro_value_get_size(const avro_value_t *map, size_t *size);
int avro_value_get_by_name(const avro_value_t *map, const char *key,
                           avro_value_t *element, size_t *index);
int avro_value_get_by_index(const avro_value_t *map, size_t index,
                            avro_value_t *element, const char **key);
int avro_value_add(avro_value_t *map,
                   const char *key, avro_value_t *element,
                   size_t *index, int *is_new);
```

The `get_size` method returns the number of elements currently in the
map. Map elements can be retrieved either by their key (`get_by_name`)
or by their numeric index (`get_by_index`). (Numeric indices in a map
are based on the order that the elements were added to the map.) In
either case, the method takes in an optional output parameter that let
you retrieve the index associated with a key, and vice versa.

The `add` method will add a new value to the map, if the given key isn’t
already present. If the key is present, then the existing value with be
returned. The `index` parameter, if given, will be filled in the
element’s index. The `is_new` parameter, if given, can be used to
determine whether the mapped value is new or not.

<a id="api-c--_records"></a>
<a id="api-c--4.1.6.-records"></a>

#### 4.1.6. Records

There are three methods that can be used with record values:

```
#include <stdlib.h>
#include <avro.h>

int avro_value_get_size(const avro_value_t *record, size_t *size);
int avro_value_get_by_index(const avro_value_t *record, size_t index,
                            avro_value_t *element, const char **field_name);
int avro_value_get_by_name(const avro_value_t *record, const char *field_name,
                           avro_value_t *element, size_t *index);
```

The `get_size` method returns the number of fields in the record. (You
can also get this by querying the value’s schema, but for some
implementations, this method can be faster.)

The `get_by_index` and `get_by_name` functions can be used to retrieve
one of the fields in the record, either by its ordinal position within
the record, or by the name of the underlying field. Like with maps, the
methods take in an additional parameter that let you retrieve the index
associated with a field name, and vice versa.

When possible, it’s recommended that you access record fields by their
numeric index, rather than by their field name. For most
implementations, this will be more efficient.

<a id="api-c--_unions"></a>
<a id="api-c--4.1.7.-unions"></a>

#### 4.1.7. Unions

There are three methods that can be used with union values:

```
#include <avro.h>

int avro_value_get_discriminant(const avro_value_t *union_val, int *disc);
int avro_value_get_current_branch(const avro_value_t *union_val, avro_value_t *branch);
int avro_value_set_branch(avro_value_t *union_val,
                          int discriminant, avro_value_t *branch);
```

The `get_discriminant` and `get_current_branch` methods return the
current state of the union value, without modifying which branch is
currently selected. The `set_branch` method can be used to choose the
active branch, filling in the `branch` value to point at the branch’s
value instance. (Most implementations will be smart enough to detect
when the desired branch is already selected, so you should always call
this method unless you can *guarantee* that the right branch is already
current.)

<a id="api-c--_creating_value_instances"></a>
<a id="api-c--4.2.-creating-value-instances"></a>

### 4.2. Creating value instances

Okay, so we’ve described how to interact with a value that you already
have a pointer to, but how do you create one in the first place? Each
implementation of the value interface must provide its own functions for
creating `avro_value_t` instances for that class. The 10,000-foot view
is to:

1. Get an *implementation struct* for the value implementation that you
   want to use. (This is represented by an `avro_value_iface_t`
   pointer.)
2. Use the implementation’s constructor function to allocate instances
   of that value implementation.
3. Do whatever you need to the value (using the `avro_value_t` methods
   described in the previous section).
4. Free the value instance, if necessary, using the implementation’s
   destructor function.
5. Free the implementation struct when you’re done creating value
   instances.

These steps use the following functions:

```
#include <avro.h>

avro_value_iface_t *avro_value_iface_incref(avro_value_iface_t *iface);
void avro_value_iface_decref(avro_value_iface_t *iface);
```

Note that for most value implementations, it’s fine to reuse a single
`avro_value_t` instance for multiple values, using the
`avro_value_reset` function before filling in the instance for each
value. (This helps reduce the number of `malloc` and `free` calls that
your application will make.)

We provide a “generic” value implementation that will work (efficiently)
for any Avro schema.

For most applications, you won’t need to write your own value
implementation; the Avro C library provides an efficient “generic”
implementation, which supports the full range of Avro schema types.
There’s a good chance that you just want to use this implementation, rather than rolling your own. (The primary reason for rolling your own
would be if you want to access the elements of a compound value using C
syntax — for instance, translating an Avro record into a C struct.) You
can use the following functions to create and work with a generic value
implementation for a particular schema:

```
#include <avro.h>

avro_value_iface_t *avro_generic_class_from_schema(avro_schema_t schema);
int avro_generic_value_new(const avro_value_iface_t *iface, avro_value_t *dest);
void avro_generic_value_free(avro_value_t *self);
```

Combining all of this together, you might have the following snippet of
code:

```
avro_schema_t  schema = avro_schema_long();
avro_value_iface_t  *iface = avro_generic_class_from_schema(schema);

avro_value_t  val;
avro_generic_value_new(iface, &val);

/* Generate Avro longs from 0-499 */
int  i;
for (i = 0; i < 500; i++) {
    avro_value_reset(&val);
    avro_value_set_long(&val, i);
    /* do something with the value */
}

avro_generic_value_free(&val);
avro_value_iface_decref(iface);
avro_schema_decref(schema);
```

<a id="api-c--_reference_counting"></a>
<a id="api-c--5.-reference-counting"></a>

## 5. Reference Counting

`Avro C` does reference counting for all schema and data objects.
When the number of references drops to zero, the memory is freed.

For example, to create and free a string, you would use:

```
avro_datum_t string = avro_string("This is my string");

...
avro_datum_decref(string);
```

Things get a little more complicated when you consider more elaborate
schema and data structures.

For example, let’s say that you create a record with a single
string field:

```
avro_datum_t example = avro_record("Example");
avro_datum_t solo_field = avro_string("Example field value");

avro_record_set(example, "solo", solo_field);

...
avro_datum_decref(example);
```

In this example, the `solo_field` datum would **not** be freed since it
has two references: the original reference and a reference inside
the `Example` record. The `avro_datum_decref(example)` call drops
the number of reference to one. If you are finished with the `solo_field`
schema, then you need to `avro_schema_decref(solo_field)` to
completely dereference the `solo_field` datum and free it.

<a id="api-c--_wrap_it_and_give_it"></a>
<a id="api-c--6.-wrap-it-and-give-it"></a>

## 6. Wrap It and Give It

You’ll notice that some datatypes can be "wrapped" and "given". This
allows C programmers the freedom to decide who is responsible for
the memory. Let’s take strings for example.

To create a string datum, you have three different methods:

```
avro_datum_t avro_string(const char *str);
avro_datum_t avro_wrapstring(const char *str);
avro_datum_t avro_givestring(const char *str);
```

If you use, `avro_string` then `Avro C` will make a copy of your
string and free it when the datum is dereferenced. In some cases, especially when dealing with large amounts of data, you want
to avoid this memory copy. That’s where `avro_wrapstring` and
`avro_givestring` can help.

If you use, `avro_wrapstring` then `Avro C` will do no memory
management at all. It will just save a pointer to your data and
it’s your responsibility to free the string.

> [!NOTE]
> |  |
> | --- |
> |
> > [!WARNING]
> > |
>  When using `avro_wrapstring`, do not free the string before you dereference the string datum with `avro_datum_decref()`. |

Lastly, if you use `avro_givestring` then `Avro C` will free the
string later when the datum is dereferenced. In a sense, you
are "giving" responsibility for freeing the string to `Avro C`.

> [!NOTE]
> |  |
> | --- |
> |
> > [!WARNING]
> > |
>  Don’t "give" `Avro C` a string that you haven’t allocated from the heap with e.g. `malloc` or `strdup`.  For example, **don’t** do this: ```
> avro_datum_t bad_idea = avro_givestring("This isn't allocated on the heap");
> ```
>  |

<a id="api-c--_schema_validation"></a>
<a id="api-c--7.-schema-validation"></a>

## 7. Schema Validation

If you want to write a datum, you would use the following function

```
int avro_write_data(avro_writer_t writer,
                    avro_schema_t writers_schema, avro_datum_t datum);
```

If you pass in a `writers_schema`, then you `datum` will be validated **before**
it is sent to the `writer`. This check ensures that your data has the
correct format. If you are certain your datum is correct, you can pass
a `NULL` value for `writers_schema` and `Avro C` will not validate before
writing.

> [!NOTE]
> |  |
> | --- |
> |
> > [!NOTE]
> > |
>  Data written to an Avro File Object Container is always validated. |

<a id="api-c--_examples"></a>
<a id="api-c--8.-examples"></a>

## 8. Examples

I’m not even supposed to be here today!

— Dante Hicks

Imagine you’re a free-lance hacker in Leonardo, New Jersey and you’ve
been approached by the owner of the local **Quick Stop Convenience** store.
He wants you to create a contact database case he needs to call employees
to work on their day off.

You might build a simple contact system using Avro C like the following…

```
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to you under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 * https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.  See the License for the specific language governing
 * permissions and limitations under the License.
 */

#include <avro.h>
#include <stdio.h>
#include <stdlib.h>

#ifdef DEFLATE_CODEC
#define QUICKSTOP_CODEC  "deflate"
#else
#define QUICKSTOP_CODEC  "null"
#endif

avro_schema_t person_schema;
int64_t id = 0;

/* A simple schema for our tutorial */
const char  PERSON_SCHEMA[] =
"{\"type\":\"record\",\
  \"name\":\"Person\",\
  \"fields\":[\
     {\"name\": \"ID\", \"type\": \"long\"},\
     {\"name\": \"First\", \"type\": \"string\"},\
     {\"name\": \"Last\", \"type\": \"string\"},\
     {\"name\": \"Phone\", \"type\": \"string\"},\
     {\"name\": \"Age\", \"type\": \"int\"}]}";

/* Parse schema into a schema data structure */
void init_schema(void)
{
        if (avro_schema_from_json_literal(PERSON_SCHEMA, &person_schema)) {
                fprintf(stderr, "Unable to parse person schema\n");
                exit(EXIT_FAILURE);
        }
}

/* Create a value to match the person schema and save it */
void
add_person(avro_file_writer_t db, const char *first, const char *last,
           const char *phone, int32_t age)
{
        avro_value_iface_t  *person_class =
            avro_generic_class_from_schema(person_schema);

        avro_value_t  person;
        avro_generic_value_new(person_class, &person);

        avro_value_t id_value;
        avro_value_t first_value;
        avro_value_t last_value;
        avro_value_t age_value;
        avro_value_t phone_value;

        if (avro_value_get_by_name(&person, "ID", &id_value, NULL) == 0) {
                avro_value_set_long(&id_value, ++id);
        }
        if (avro_value_get_by_name(&person, "First", &first_value, NULL) == 0) {
                avro_value_set_string(&first_value, first);
        }
        if (avro_value_get_by_name(&person, "Last", &last_value, NULL) == 0) {
                avro_value_set_string(&last_value, last);
        }
        if (avro_value_get_by_name(&person, "Age", &age_value, NULL) == 0) {
                avro_value_set_int(&age_value, age);
        }
        if (avro_value_get_by_name(&person, "Phone", &phone_value, NULL) == 0) {
                avro_value_set_string(&phone_value, phone);
        }

        if (avro_file_writer_append_value(db, &person)) {
                fprintf(stderr,
                        "Unable to write Person value to memory buffer\nMessage: %s\n", avro_strerror());
                exit(EXIT_FAILURE);
        }

        /* Decrement all our references to prevent memory from leaking */
        avro_value_decref(&person);
        avro_value_iface_decref(person_class);
}

int print_person(avro_file_reader_t db, avro_schema_t reader_schema)
{

        avro_value_iface_t  *person_class =
            avro_generic_class_from_schema(person_schema);

        avro_value_t person;
        avro_generic_value_new(person_class, &person);

        int rval;

        rval = avro_file_reader_read_value(db, &person);
        if (rval == 0) {
                int64_t id;
                int32_t age;
                const char *p;
                size_t size;
                avro_value_t id_value;
                avro_value_t first_value;
                avro_value_t last_value;
                avro_value_t age_value;
                avro_value_t phone_value;

                if (avro_value_get_by_name(&person, "ID", &id_value, NULL) == 0) {
                        avro_value_get_long(&id_value, &id);
                        fprintf(stdout, "%"PRId64" | ", id);
                }
                if (avro_value_get_by_name(&person, "First", &first_value, NULL) == 0) {
                        avro_value_get_string(&first_value, &p, &size);
                        fprintf(stdout, "%15s | ", p);
                }
                if (avro_value_get_by_name(&person, "Last", &last_value, NULL) == 0) {
                        avro_value_get_string(&last_value, &p, &size);
                        fprintf(stdout, "%15s | ", p);
                }
                if (avro_value_get_by_name(&person, "Phone", &phone_value, NULL) == 0) {
                        avro_value_get_string(&phone_value, &p, &size);
                        fprintf(stdout, "%15s | ", p);
                }
                if (avro_value_get_by_name(&person, "Age", &age_value, NULL) == 0) {
                        avro_value_get_int(&age_value, &age);
                        fprintf(stdout, "%"PRId32" | ", age);
                }
                fprintf(stdout, "\n");

                /* We no longer need this memory */
                avro_value_decref(&person);
                avro_value_iface_decref(person_class);
        }
        return rval;
}

int main(void)
{
        int rval;
        avro_file_reader_t dbreader;
        avro_file_writer_t db;
        avro_schema_t projection_schema, first_name_schema, phone_schema;
        int64_t i;
        const char *dbname = "quickstop.db";
        char number[15] = {0};

        /* Initialize the schema structure from JSON */
        init_schema();

        /* Delete the database if it exists */
        remove(dbname);
        /* Create a new database */
        rval = avro_file_writer_create_with_codec
            (dbname, person_schema, &db, QUICKSTOP_CODEC, 0);
        if (rval) {
                fprintf(stderr, "There was an error creating %s\n", dbname);
                fprintf(stderr, " error message: %s\n", avro_strerror());
                exit(EXIT_FAILURE);
        }

        /* Add lots of people to the database */
        for (i = 0; i < 1000; i++)
        {
                sprintf(number, "(%d)", (int)i);
                add_person(db, "Dante", "Hicks", number, 32);
                add_person(db, "Randal", "Graves", "(555) 123-5678", 30);
                add_person(db, "Veronica", "Loughran", "(555) 123-0987", 28);
                add_person(db, "Caitlin", "Bree", "(555) 123-2323", 27);
                add_person(db, "Bob", "Silent", "(555) 123-6422", 29);
                add_person(db, "Jay", "???", number, 26);
        }

        /* Close the block and open a new one */
        avro_file_writer_flush(db);
        add_person(db, "Super", "Man", "123456", 31);

        avro_file_writer_close(db);

        fprintf(stdout, "\nNow let's read all the records back out\n");

        /* Read all the records and print them */
        if (avro_file_reader(dbname, &dbreader)) {
                fprintf(stderr, "Error opening file: %s\n", avro_strerror());
                exit(EXIT_FAILURE);
        }
        for (i = 0; i < id; i++) {
                if (print_person(dbreader, NULL)) {
                        fprintf(stderr, "Error printing person\nMessage: %s\n", avro_strerror());
                        exit(EXIT_FAILURE);
                }
        }
        avro_file_reader_close(dbreader);

        /* You can also use projection, to only decode only the data you are
           interested in.  This is particularly useful when you have
           huge data sets and you'll only interest in particular fields
           e.g. your contacts First name and phone number */
        projection_schema = avro_schema_record("Person", NULL);
        first_name_schema = avro_schema_string();
        phone_schema = avro_schema_string();
        avro_schema_record_field_append(projection_schema, "First",
                                        first_name_schema);
        avro_schema_record_field_append(projection_schema, "Phone",
                                        phone_schema);

        /* Read only the record you're interested in */
        fprintf(stdout,
                "\n\nUse projection to print only the First name and phone numbers\n");
        if (avro_file_reader(dbname, &dbreader)) {
                fprintf(stderr, "Error opening file: %s\n", avro_strerror());
                exit(EXIT_FAILURE);
        }
        for (i = 0; i < id; i++) {
                if (print_person(dbreader, projection_schema)) {
                        fprintf(stderr, "Error printing person: %s\n",
                                avro_strerror());
                        exit(EXIT_FAILURE);
                }
        }
        avro_file_reader_close(dbreader);
        avro_schema_decref(first_name_schema);
        avro_schema_decref(phone_schema);
        avro_schema_decref(projection_schema);

        /* We don't need this schema anymore */
        avro_schema_decref(person_schema);
        return 0;
}
```

When you compile and run this program, you should get the following output

```
Successfully added Hicks, Dante id=1
Successfully added Graves, Randal id=2
Successfully added Loughran, Veronica id=3
Successfully added Bree, Caitlin id=4
Successfully added Silent, Bob id=5
Successfully added ???, Jay id=6

Avro is compact. Here is the data for all 6 people.
| 02 0A 44 61 6E 74 65 0A | 48 69 63 6B 73 1C 28 35 |   ..Dante.Hicks.(5
| 35 35 29 20 31 32 33 2D | 34 35 36 37 40 04 0C 52 |   55) 123-4567@..R
| 61 6E 64 61 6C 0C 47 72 | 61 76 65 73 1C 28 35 35 |   andal.Graves.(55
| 35 29 20 31 32 33 2D 35 | 36 37 38 3C 06 10 56 65 |   5) 123-5678<..Ve
| 72 6F 6E 69 63 61 10 4C | 6F 75 67 68 72 61 6E 1C |   ronica.Loughran.
| 28 35 35 35 29 20 31 32 | 33 2D 30 39 38 37 38 08 |   (555) 123-09878.
| 0E 43 61 69 74 6C 69 6E | 08 42 72 65 65 1C 28 35 |   .Caitlin.Bree.(5
| 35 35 29 20 31 32 33 2D | 32 33 32 33 36 0A 06 42 |   55) 123-23236..B
| 6F 62 0C 53 69 6C 65 6E | 74 1C 28 35 35 35 29 20 |   ob.Silent.(555)
| 31 32 33 2D 36 34 32 32 | 3A 0C 06 4A 61 79 06 3F |   123-6422:..Jay.?
| 3F 3F 1C 28 35 35 35 29 | 20 31 32 33 2D 39 31 38 |   ??.(555) 123-918
| 32 34 .. .. .. .. .. .. | .. .. .. .. .. .. .. .. |   24..............

Now let's read all the records back out
1 |           Dante |           Hicks |  (555) 123-4567 | 32
2 |          Randal |          Graves |  (555) 123-5678 | 30
3 |        Veronica |        Loughran |  (555) 123-0987 | 28
4 |         Caitlin |            Bree |  (555) 123-2323 | 27
5 |             Bob |          Silent |  (555) 123-6422 | 29
6 |             Jay |             ??? |  (555) 123-9182 | 26


Use projection to print only the First name and phone numbers
          Dante |  (555) 123-4567 |
         Randal |  (555) 123-5678 |
       Veronica |  (555) 123-0987 |
        Caitlin |  (555) 123-2323 |
            Bob |  (555) 123-6422 |
            Jay |  (555) 123-9182 |
```

The **Quick Stop** owner was so pleased, he asked you to create a
movie database for his **RST Video** store.

<a id="api-c--_reference_files"></a>
<a id="api-c--9.-reference-files"></a>

## 9. Reference files

<a id="api-c--_avro_h"></a>
<a id="api-c--9.1.-avro.h"></a>

### 9.1. avro.h

The `avro.h` header file contains the complete public API
for `Avro C`. The documentation is rather sparse right now
but we’ll be adding more information soon.

```
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to you under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 * https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.  See the License for the specific language governing
 * permissions and limitations under the License.
 */
#ifndef AVRO_H
#define AVRO_H
#ifdef __cplusplus
extern "C" {
#define CLOSE_EXTERN }
#else
#define CLOSE_EXTERN
#endif

#include <avro/allocation.h>
#include <avro/basics.h>
#include <avro/consumer.h>
#include <avro/data.h>
#include <avro/errors.h>
#include <avro/generic.h>
#include <avro/io.h>
#include <avro/legacy.h>
#include <avro/platform.h>
#include <avro/resolver.h>
#include <avro/schema.h>
#include <avro/value.h>

CLOSE_EXTERN
#endif
```

<a id="api-c--_test_avro_data_c"></a>
<a id="api-c--9.2.-test_avro_data.c"></a>

### 9.2. test\_avro\_data.c

Another good way to learn how to encode/decode data in `Avro C` is
to look at the `test_avro_data.c` unit test. This simple unit test
checks that all the avro types can be encoded/decoded correctly.

```
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to you under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 * https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
 * implied.  See the License for the specific language governing
 * permissions and limitations under the License.
 */

#include "avro.h"
#include "avro_private.h"
#include <limits.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

char buf[4096];
avro_reader_t reader;
avro_writer_t writer;

typedef int (*avro_test) (void);

/*
 * Use a custom allocator that verifies that the size that we use to
 * free an object matches the size that we use to allocate it.
 */

static void *
test_allocator(void *ud, void *ptr, size_t osize, size_t nsize)
{
        AVRO_UNUSED(ud);
        AVRO_UNUSED(osize);

        if (nsize == 0) {
                size_t  *size = ((size_t *) ptr) - 1;
                if (osize != *size) {
                        fprintf(stderr,
                                "Error freeing %p:\n"
                                "Size passed to avro_free (%" PRIsz ") "
                                "doesn't match size passed to "
                                "avro_malloc (%" PRIsz ")\n",
                                ptr, osize, *size);
                        abort();
                        //exit(EXIT_FAILURE);
                }
                free(size);
                return NULL;
        } else {
                size_t  real_size = nsize + sizeof(size_t);
                size_t  *old_size = ptr? ((size_t *) ptr)-1: NULL;
                size_t  *size = (size_t *) realloc(old_size, real_size);
                *size = nsize;
                return (size + 1);
        }
}

void init_rand(void)
{
        srand(time(NULL));
}

double rand_number(double from, double to)
{
        double range = to - from;
        return from + ((double)rand() / (RAND_MAX + 1.0)) * range;
}

int64_t rand_int64(void)
{
        return (int64_t) rand_number(LONG_MIN, LONG_MAX);
}

int32_t rand_int32(void)
{
        return (int32_t) rand_number(INT_MIN, INT_MAX);
}

void
write_read_check(avro_schema_t writers_schema, avro_datum_t datum,
                 avro_schema_t readers_schema, avro_datum_t expected, char *type)
{
        avro_datum_t datum_out;
        int validate;

        for (validate = 0; validate <= 1; validate++) {

                reader = avro_reader_memory(buf, sizeof(buf));
                writer = avro_writer_memory(buf, sizeof(buf));

                if (!expected) {
                        expected = datum;
                }

                /* Validating read/write */
                if (avro_write_data
                    (writer, validate ? writers_schema : NULL, datum)) {
                        fprintf(stderr, "Unable to write %s validate=%d\n  %s\n",
                                type, validate, avro_strerror());
                        exit(EXIT_FAILURE);
                }
                int64_t size =
                    avro_size_data(writer, validate ? writers_schema : NULL,
                                   datum);
                if (size != avro_writer_tell(writer)) {
                        fprintf(stderr,
                                "Unable to calculate size %s validate=%d "
                                "(%"PRId64" != %"PRId64")\n  %s\n",
                                type, validate, size, avro_writer_tell(writer),
                                avro_strerror());
                        exit(EXIT_FAILURE);
                }
                if (avro_read_data
                    (reader, writers_schema, readers_schema, &datum_out)) {
                        fprintf(stderr, "Unable to read %s validate=%d\n  %s\n",
                                type, validate, avro_strerror());
                        fprintf(stderr, "  %s\n", avro_strerror());
                        exit(EXIT_FAILURE);
                }
                if (!avro_datum_equal(expected, datum_out)) {
                        fprintf(stderr,
                                "Unable to encode/decode %s validate=%d\n  %s\n",
                                type, validate, avro_strerror());
                        exit(EXIT_FAILURE);
                }

                avro_reader_dump(reader, stderr);
                avro_datum_decref(datum_out);
                avro_reader_free(reader);
                avro_writer_free(writer);
        }
}

static void test_json(avro_datum_t datum, const char *expected)
{
        char  *json = NULL;
        avro_datum_to_json(datum, 1, &json);
        if (strcasecmp(json, expected) != 0) {
                fprintf(stderr, "Unexpected JSON encoding: %s\n", json);
                exit(EXIT_FAILURE);
        }
        free(json);
}

static int test_string(void)
{
        unsigned int i;
        const char *strings[] = { "Four score and seven years ago",
                "our father brought forth on this continent",
                "a new nation", "conceived in Liberty",
                "and dedicated to the proposition that all men are created equal."
        };
        avro_schema_t writer_schema = avro_schema_string();
        for (i = 0; i < sizeof(strings) / sizeof(strings[0]); i++) {
                avro_datum_t datum = avro_givestring(strings[i], NULL);
                write_read_check(writer_schema, datum, NULL, NULL, "string");
                avro_datum_decref(datum);
        }

        avro_datum_t  datum = avro_givestring(strings[0], NULL);
        test_json(datum, "\"Four score and seven years ago\"");
        avro_datum_decref(datum);

        // The following should bork if we don't copy the string value
        // correctly (since we'll try to free a static string).

        datum = avro_string("this should be copied");
        avro_string_set(datum, "also this");
        avro_datum_decref(datum);

        avro_schema_decref(writer_schema);
        return 0;
}

static int test_bytes(void)
{
        char bytes[] = { 0xDE, 0xAD, 0xBE, 0xEF };
        avro_schema_t writer_schema = avro_schema_bytes();
        avro_datum_t datum;
        avro_datum_t expected_datum;

        datum = avro_givebytes(bytes, sizeof(bytes), NULL);
        write_read_check(writer_schema, datum, NULL, NULL, "bytes");
        test_json(datum, "\"\\u00de\\u00ad\\u00be\\u00ef\"");
        avro_datum_decref(datum);
        avro_schema_decref(writer_schema);

        datum = avro_givebytes(NULL, 0, NULL);
        avro_givebytes_set(datum, bytes, sizeof(bytes), NULL);
        expected_datum = avro_givebytes(bytes, sizeof(bytes), NULL);
        if (!avro_datum_equal(datum, expected_datum)) {
                fprintf(stderr,
                        "Expected equal bytes instances.\n");
                exit(EXIT_FAILURE);
        }
        avro_datum_decref(datum);
        avro_datum_decref(expected_datum);

        // The following should bork if we don't copy the bytes value
        // correctly (since we'll try to free a static string).

        datum = avro_bytes("original", 8);
        avro_bytes_set(datum, "alsothis", 8);
        avro_datum_decref(datum);

        avro_schema_decref(writer_schema);
        return 0;
}

static int test_int32(void)
{
        int i;
        avro_schema_t writer_schema = avro_schema_int();
        avro_schema_t long_schema = avro_schema_long();
        avro_schema_t float_schema = avro_schema_float();
        avro_schema_t double_schema = avro_schema_double();
        for (i = 0; i < 100; i++) {
                int32_t  value = rand_int32();
                avro_datum_t datum = avro_int32(value);
                avro_datum_t long_datum = avro_int64(value);
                avro_datum_t float_datum = avro_float(value);
                avro_datum_t double_datum = avro_double(value);
                write_read_check(writer_schema, datum, NULL, NULL, "int");
                write_read_check(writer_schema, datum,
                                 long_schema, long_datum, "int->long");
                write_read_check(writer_schema, datum,
                                 float_schema, float_datum, "int->float");
                write_read_check(writer_schema, datum,
                                 double_schema, double_datum, "int->double");
                avro_datum_decref(datum);
                avro_datum_decref(long_datum);
                avro_datum_decref(float_datum);
                avro_datum_decref(double_datum);
        }

        avro_datum_t  datum = avro_int32(10000);
        test_json(datum, "10000");
        avro_datum_decref(datum);

        avro_schema_decref(writer_schema);
        avro_schema_decref(long_schema);
        avro_schema_decref(float_schema);
        avro_schema_decref(double_schema);
        return 0;
}

static int test_int64(void)
{
        int i;
        avro_schema_t writer_schema = avro_schema_long();
        avro_schema_t float_schema = avro_schema_float();
        avro_schema_t double_schema = avro_schema_double();
        for (i = 0; i < 100; i++) {
                int64_t  value = rand_int64();
                avro_datum_t datum = avro_int64(value);
                avro_datum_t float_datum = avro_float(value);
                avro_datum_t double_datum = avro_double(value);
                write_read_check(writer_schema, datum, NULL, NULL, "long");
                write_read_check(writer_schema, datum,
                                 float_schema, float_datum, "long->float");
                write_read_check(writer_schema, datum,
                                 double_schema, double_datum, "long->double");
                avro_datum_decref(datum);
                avro_datum_decref(float_datum);
                avro_datum_decref(double_datum);
        }

        avro_datum_t  datum = avro_int64(10000);
        test_json(datum, "10000");
        avro_datum_decref(datum);

        avro_schema_decref(writer_schema);
        avro_schema_decref(float_schema);
        avro_schema_decref(double_schema);
        return 0;
}

static int test_double(void)
{
        int i;
        avro_schema_t schema = avro_schema_double();
        for (i = 0; i < 100; i++) {
                avro_datum_t datum = avro_double(rand_number(-1.0E10, 1.0E10));
                write_read_check(schema, datum, NULL, NULL, "double");
                avro_datum_decref(datum);
        }

        avro_datum_t  datum = avro_double(2000.0);
        test_json(datum, "2000.0");
        avro_datum_decref(datum);

        avro_schema_decref(schema);
        return 0;
}

static int test_float(void)
{
        int i;
        avro_schema_t schema = avro_schema_float();
        avro_schema_t double_schema = avro_schema_double();
        for (i = 0; i < 100; i++) {
                float  value = rand_number(-1.0E10, 1.0E10);
                avro_datum_t datum = avro_float(value);
                avro_datum_t double_datum = avro_double(value);
                write_read_check(schema, datum, NULL, NULL, "float");
                write_read_check(schema, datum,
                                 double_schema, double_datum, "float->double");
                avro_datum_decref(datum);
                avro_datum_decref(double_datum);
        }

        avro_datum_t  datum = avro_float(2000.0);
        test_json(datum, "2000.0");
        avro_datum_decref(datum);

        avro_schema_decref(schema);
        avro_schema_decref(double_schema);
        return 0;
}

static int test_boolean(void)
{
        int i;
        const char  *expected_json[] = { "false", "true" };
        avro_schema_t schema = avro_schema_boolean();
        for (i = 0; i <= 1; i++) {
                avro_datum_t datum = avro_boolean(i);
                write_read_check(schema, datum, NULL, NULL, "boolean");
                test_json(datum, expected_json[i]);
                avro_datum_decref(datum);
        }
        avro_schema_decref(schema);
        return 0;
}

static int test_null(void)
{
        avro_schema_t schema = avro_schema_null();
        avro_datum_t datum = avro_null();
        write_read_check(schema, datum, NULL, NULL, "null");
        test_json(datum, "null");
        avro_datum_decref(datum);
        return 0;
}

static int test_record(void)
{
        avro_schema_t schema = avro_schema_record("person", NULL);
        avro_schema_record_field_append(schema, "name", avro_schema_string());
        avro_schema_record_field_append(schema, "age", avro_schema_int());

        avro_datum_t datum = avro_record(schema);
        avro_datum_t name_datum, age_datum;

        name_datum = avro_givestring("Joseph Campbell", NULL);
        age_datum = avro_int32(83);

        avro_record_set(datum, "name", name_datum);
        avro_record_set(datum, "age", age_datum);

        write_read_check(schema, datum, NULL, NULL, "record");
        test_json(datum, "{\"name\": \"Joseph Campbell\", \"age\": 83}");

        int  rc;
        avro_record_set_field_value(rc, datum, int32, "age", 104);

        int32_t  age = 0;
        avro_record_get_field_value(rc, datum, int32, "age", &age);
        if (age != 104) {
                fprintf(stderr, "Incorrect age value\n");
                exit(EXIT_FAILURE);
        }

        avro_datum_decref(name_datum);
        avro_datum_decref(age_datum);
        avro_datum_decref(datum);
        avro_schema_decref(schema);
        return 0;
}

static int test_nested_record(void)
{
        const char  *json =
                "{"
                "  \"type\": \"record\","
                "  \"name\": \"list\","
                "  \"fields\": ["
                "    { \"name\": \"x\", \"type\": \"int\" },"
                "    { \"name\": \"y\", \"type\": \"int\" },"
                "    { \"name\": \"next\", \"type\": [\"null\",\"list\"]}"
                "  ]"
                "}";

        int  rval;

        avro_schema_t schema = NULL;
        avro_schema_error_t error;
        avro_schema_from_json(json, strlen(json), &schema, &error);

        avro_datum_t  head = avro_datum_from_schema(schema);
        avro_record_set_field_value(rval, head, int32, "x", 10);
        avro_record_set_field_value(rval, head, int32, "y", 10);

        avro_datum_t  next = NULL;
        avro_datum_t  tail = NULL;

        avro_record_get(head, "next", &next);
        avro_union_set_discriminant(next, 1, &tail);
        avro_record_set_field_value(rval, tail, int32, "x", 20);
        avro_record_set_field_value(rval, tail, int32, "y", 20);

        avro_record_get(tail, "next", &next);
        avro_union_set_discriminant(next, 0, NULL);

        write_read_check(schema, head, NULL, NULL, "nested record");

        avro_schema_decref(schema);
        avro_datum_decref(head);

        return 0;
}

static int test_enum(void)
{
        enum avro_languages {
                AVRO_C,
                AVRO_CPP,
                AVRO_PYTHON,
                AVRO_RUBY,
                AVRO_JAVA
        };
        avro_schema_t schema = avro_schema_enum("language");
        avro_datum_t datum = avro_enum(schema, AVRO_C);

        avro_schema_enum_symbol_append(schema, "C");
        avro_schema_enum_symbol_append(schema, "C++");
        avro_schema_enum_symbol_append(schema, "Python");
        avro_schema_enum_symbol_append(schema, "Ruby");
        avro_schema_enum_symbol_append(schema, "Java");

        if (avro_enum_get(datum) != AVRO_C) {
                fprintf(stderr, "Unexpected enum value AVRO_C\n");
                exit(EXIT_FAILURE);
        }

        if (strcmp(avro_enum_get_name(datum), "C") != 0) {
                fprintf(stderr, "Unexpected enum value name C\n");
                exit(EXIT_FAILURE);
        }

        write_read_check(schema, datum, NULL, NULL, "enum");
        test_json(datum, "\"C\"");

        avro_enum_set(datum, AVRO_CPP);
        if (strcmp(avro_enum_get_name(datum), "C++") != 0) {
                fprintf(stderr, "Unexpected enum value name C++\n");
                exit(EXIT_FAILURE);
        }

        write_read_check(schema, datum, NULL, NULL, "enum");
        test_json(datum, "\"C++\"");

        avro_enum_set_name(datum, "Python");
        if (avro_enum_get(datum) != AVRO_PYTHON) {
                fprintf(stderr, "Unexpected enum value AVRO_PYTHON\n");
                exit(EXIT_FAILURE);
        }

        write_read_check(schema, datum, NULL, NULL, "enum");
        test_json(datum, "\"Python\"");

        avro_datum_decref(datum);
        avro_schema_decref(schema);
        return 0;
}

static int test_array(void)
{
        int i, rval;
        avro_schema_t schema = avro_schema_array(avro_schema_int());
        avro_datum_t datum = avro_array(schema);

        for (i = 0; i < 10; i++) {
                avro_datum_t i32_datum = avro_int32(i);
                rval = avro_array_append_datum(datum, i32_datum);
                avro_datum_decref(i32_datum);
                if (rval) {
                        exit(EXIT_FAILURE);
                }
        }

        if (avro_array_size(datum) != 10) {
                fprintf(stderr, "Unexpected array size");
                exit(EXIT_FAILURE);
        }

        write_read_check(schema, datum, NULL, NULL, "array");
        test_json(datum, "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]");
        avro_datum_decref(datum);
        avro_schema_decref(schema);
        return 0;
}

static int test_map(void)
{
        avro_schema_t schema = avro_schema_map(avro_schema_long());
        avro_datum_t datum = avro_map(schema);
        int64_t i = 0;
        char *nums[] =
            { "zero", "one", "two", "three", "four", "five", "six", NULL };
        while (nums[i]) {
                avro_datum_t i_datum = avro_int64(i);
                avro_map_set(datum, nums[i], i_datum);
                avro_datum_decref(i_datum);
                i++;
        }

        if (avro_array_size(datum) != 7) {
                fprintf(stderr, "Unexpected map size\n");
                exit(EXIT_FAILURE);
        }

        avro_datum_t value;
        const char  *key;
        avro_map_get_key(datum, 2, &key);
        avro_map_get(datum, key, &value);
        int64_t  val;
        avro_int64_get(value, &val);

        if (val != 2) {
                fprintf(stderr, "Unexpected map value 2\n");
                exit(EXIT_FAILURE);
        }

        int  index;
        if (avro_map_get_index(datum, "two", &index)) {
                fprintf(stderr, "Can't get index for key \"two\": %s\n",
                        avro_strerror());
                exit(EXIT_FAILURE);
        }
        if (index != 2) {
                fprintf(stderr, "Unexpected index for key \"two\"\n");
                exit(EXIT_FAILURE);
        }
        if (!avro_map_get_index(datum, "foobar", &index)) {
                fprintf(stderr, "Unexpected index for key \"foobar\"\n");
                exit(EXIT_FAILURE);
        }

        write_read_check(schema, datum, NULL, NULL, "map");
        test_json(datum,
                  "{\"zero\": 0, \"one\": 1, \"two\": 2, \"three\": 3, "
                  "\"four\": 4, \"five\": 5, \"six\": 6}");
        avro_datum_decref(datum);
        avro_schema_decref(schema);
        return 0;
}

static int test_union(void)
{
        avro_schema_t schema = avro_schema_union();
        avro_datum_t union_datum;
        avro_datum_t datum;
        avro_datum_t union_datum1;
        avro_datum_t datum1;

        avro_schema_union_append(schema, avro_schema_string());
        avro_schema_union_append(schema, avro_schema_int());
        avro_schema_union_append(schema, avro_schema_null());

        datum = avro_givestring("Follow your bliss.", NULL);
        union_datum = avro_union(schema, 0, datum);

        if (avro_union_discriminant(union_datum) != 0) {
                fprintf(stderr, "Unexpected union discriminant\n");
                exit(EXIT_FAILURE);
        }

        if (avro_union_current_branch(union_datum) != datum) {
                fprintf(stderr, "Unexpected union branch datum\n");
                exit(EXIT_FAILURE);
        }

        union_datum1 = avro_datum_from_schema(schema);
        avro_union_set_discriminant(union_datum1, 0, &datum1);
        avro_givestring_set(datum1, "Follow your bliss.", NULL);

        if (!avro_datum_equal(datum, datum1)) {
                fprintf(stderr, "Union values should be equal\n");
                exit(EXIT_FAILURE);
        }

        write_read_check(schema, union_datum, NULL, NULL, "union");
        test_json(union_datum, "{\"string\": \"Follow your bliss.\"}");

        avro_datum_decref(datum);
        avro_union_set_discriminant(union_datum, 2, &datum);
        test_json(union_datum, "null");

        avro_datum_decref(union_datum);
        avro_datum_decref(datum);
        avro_datum_decref(union_datum1);
        avro_schema_decref(schema);
        return 0;
}

static int test_fixed(void)
{
        char bytes[] = { 0xD, 0xA, 0xD, 0xA, 0xB, 0xA, 0xB, 0xA };
        avro_schema_t schema = avro_schema_fixed("msg", sizeof(bytes));
        avro_datum_t datum;
        avro_datum_t expected_datum;

        datum = avro_givefixed(schema, bytes, sizeof(bytes), NULL);
        write_read_check(schema, datum, NULL, NULL, "fixed");
        test_json(datum, "\"\\r\\n\\r\\n\\u000b\\n\\u000b\\n\"");
        avro_datum_decref(datum);

        datum = avro_givefixed(schema, NULL, sizeof(bytes), NULL);
        avro_givefixed_set(datum, bytes, sizeof(bytes), NULL);
        expected_datum = avro_givefixed(schema, bytes, sizeof(bytes), NULL);
        if (!avro_datum_equal(datum, expected_datum)) {
                fprintf(stderr,
                        "Expected equal fixed instances.\n");
                exit(EXIT_FAILURE);
        }
        avro_datum_decref(datum);
        avro_datum_decref(expected_datum);

        // The following should bork if we don't copy the fixed value
        // correctly (since we'll try to free a static string).

        datum = avro_fixed(schema, "original", 8);
        avro_fixed_set(datum, "alsothis", 8);
        avro_datum_decref(datum);

        avro_schema_decref(schema);
        return 0;
}

int main(void)
{
        avro_set_allocator(test_allocator, NULL);

        unsigned int i;
        struct avro_tests {
                char *name;
                avro_test func;
        } tests[] = {
                {
                "string", test_string}, {
                "bytes", test_bytes}, {
                "int", test_int32}, {
                "long", test_int64}, {
                "float", test_float}, {
                "double", test_double}, {
                "boolean", test_boolean}, {
                "null", test_null}, {
                "record", test_record}, {
                "nested_record", test_nested_record}, {
                "enum", test_enum}, {
                "array", test_array}, {
                "map", test_map}, {
                "fixed", test_fixed}, {
                "union", test_union}
        };

        init_rand();
        for (i = 0; i < sizeof(tests) / sizeof(tests[0]); i++) {
                struct avro_tests *test = tests + i;
                fprintf(stderr, "**** Running %s tests ****\n", test->name);
                if (test->func() != 0) {
                        return EXIT_FAILURE;
                }
        }
        return EXIT_SUCCESS;
}
```

---

<a id="api-cpp-html"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/api/cpp/html/ -->

<!-- page_index: 7 -->

# Avro C++: Main Page

Avro C++ Documentation

<a id="api-cpp-html--introduction"></a>
<a id="api-cpp-html--introduction-to-avro-c"></a>

## Introduction to Avro C++ [§](#api-cpp-html--introduction)

Avro is a data serialization system. See <https://avro.apache.org/docs/current/> for background information.

Avro C++ is a C++ library which implements parts of the [Avro Specification](https://avro.apache.org/docs/current/spec.html). The library includes the following functionality:

- Assembling schemas programmatically.
- A schema parser, which can parse Avro schema (written in JSON) into a Schema object.
- Encoders and decoders to encode data into Avro format and decode it back using primitive functions. There are multiple implementations of encoders and decoders.
  - A binary encoder, which encodes into binary Avro data.
  - A JSON encoder, which encodes into JSON Avro data.
  - A validating encoder, an encoder proxy, which validates the call sequence to the encoder before sending the calls to another encoder.
  - A binary decoder, which decodes binary Avro data.
  - A JSON decoder, which decodes JSON Avro data.
  - A validating decoder, a decoder proxy, which validates the call sequence to the decoder before sending the calls to another decoder.
  - A resolving decoder, which accepts calls for according to a reader's schema but decodes data corresponding to a different (writer's) schema doing schema resolution according to resolution rules in the Avro specification.
- Streams for storing and reading data, which Encoders and Decoders use.
- Support for Avro DataFile.
- A code generator, which generates C++ classes and functions to encode and decode them. The code generator produces a C++ header file from a given schema file.

Presently there is no support for the following specified in Avro specification.

- Avro RPC

**Note:** Prior to Avro release 1.5, some of the functionality mentioned above was available through a somewhat different API and set tools. They are partially incompatible to the present ones. They continue to be available but will be deprecated and discontinued sometime in the future. The documentation on that API can be found at <https://avro.apache.org/docs/1.4.0/api/cpp/html/index.html>

<a id="api-cpp-html--installing"></a>
<a id="api-cpp-html--installing-avro-c"></a>

## Installing Avro C++ [§](#api-cpp-html--installing)

<a id="api-cpp-html--supported-platforms-and-pre-requisites"></a>

### Supported platforms and pre-requisites

One should be able to build Avro C++ on (1) any UNIX flavor including cygwin for Windows and (2) natively on Windows using Visual Studio. We have tested it on (1) Linux systems (Ubuntu and RHEL) and Cygwin and Visual Studio 2010 Express edition.

In order to build Avro C++, one needs the following:

- A C++17 or later compiler and runtime libraries.
- Boost library version 1.38 or later. Apart from the header-only libraries of Boost, Avro C++ requires filesystem, iostreams, system and program\_options libraries. Please see [https://www.boost.org](https://www.boost.org/) or your platform's documentation for details on how to set up Boost for your platform.
- CMake build tool version 3.5 or later. Please see <https://www.cmake.org> or your platform's documentation for details on how to set up CMake for your system.
- Python. If not already present, please consult your platform-specific documentation on how to install Python on your system.

For Ubuntu Linux, for example, you can have these by doing `apt-get install` for the following packages:

- cmake
- g++
- libboost-dev
- libboost-filesystem-dev
- libboost-iostreams-dev
- libboost-program-options-dev
- libboost-system-dev

For Windows native builds, you need to install the following:

- cmake
- boost distribution from Boost consulting
- Visual studio

<a id="api-cpp-html--installing-avro-c-2"></a>

### Installing Avro C++

1. Download the latest Avro distribution. Avro distribution is a compressed tarball. Please see the main documentation if you want to build anything more than Avro C++.

<a id="api-cpp-html--on-unix-systems-and-on-cygwin"></a>

#### On Unix systems and on Cygwin

1. Expand the tarball into a directory.
2. Change to `lang/c++` subdirectory.
3. Type `./build.sh test`. This builds Avro C++ and runs tests on it.
4. Type `./build.sh install`. This installs Avro C++ under /usr/local on your system.

<a id="api-cpp-html--on-native-windows"></a>

#### On native Windows

1. Ensure that CMake's bin directory and Boost's lib directory are in the path.
2. Expand the tarball into a directory.
3. Change to `lang/c++` subdirectory.
4. Create a subdirectory, say, build.win, and change to that directory.
5. Type `cmake -G "Visual Studio 10"`. It creates, among other things, Avro-cpp.sln file.
6. Open the solution file using Visual Studio and build the projects from within the Visual Studio.
7. To run all unit tests, build the special project named "RUN\_TESTS".
8. After building all the projects, you can also execute the unit tests from command line. `ctest -C release` or `ctest -C debug`.

<a id="api-cpp-html--gettingstarted"></a>
<a id="api-cpp-html--getting-started-with-avro-c"></a>

## Getting started with Avro C++ [§](#api-cpp-html--gettingstarted)

Although Avro does not require use of code generation, that is the easiest way to get started with the Avro C++ library. The code generator reads a schema, and generates a C++ header file that defines one or more C++ `struct`s to represent the data for the schema and functions to encode and decode those `struct`s. Even if you wish to write custom code to encode and decode your objects using the core functionality of Avro C++, the generated code can serve as an example of how to use the code functionality.

Let's walk through an example, using a simple schema. Use the schema that represents an complex number:

**File: cpx.json**

1 {

2 "type": "record",

3 "name": "cpx",

4 "fields" : [

5 {"name": "re", "type": "double"},

6 {"name": "im", "type" : "double"}

7 ]

8 }

**Note:** All the example code given here can be found under `examples` directory of the distribution.

Assume this JSON representation of the schema is stored in a file called `cpx.json`. To generate the code issue the command:.

```

avrogencpp -i cpx.json -o cpx.hh -n c
```

The `-i` flag specifies the input schema file and `-o` flag specifies the output header file to generate. The generated C++ code will be in the namespace specified with `-n` flag.

The generated file, among other things will have the following:

```


...
namespace c {
...

struct cpx {
    double re;
    double im;
};


...

}
```

`cpx` is a C++ representation of the Avro schema `cpx`.

Now let's see how we can use the code generated to encode data into avro and decode it back.

**File: generated.cc**

1

19 #include "avro/Decoder.hh"

20 #include "avro/Encoder.hh"

21 #include "cpx.hh"

22

23 int main() {

24 std::unique\_ptr<avro::OutputStream> out = avro::memoryOutputStream();

25 avro::EncoderPtr e = avro::binaryEncoder();

26 e->init(\*out);

27 c::cpx c1;

28 c1.re = 1.0;

29 c1.im = 2.13;

30 avro::encode(\*e, c1);

31

32 std::unique\_ptr<avro::InputStream> in = avro::memoryInputStream(\*out);

33 avro::DecoderPtr d = avro::binaryDecoder();

34 d->init(\*in);

35

36 c::cpx c2;

37 avro::decode(\*d, c2);

38 std::cout << '(' << c2.re << ", " << c2.im << ')' << std::endl;

39 return 0;

40 }

In line 27, we construct a memory output stream. By this we indicate that we want to send the encoded Avro data into memory. In line 28, we construct a binary encoder, whereby we mean the output should be encoded using the Avro binary standard. In line 29, we attach the output stream to the encoder. At any given time an encoder can write to only one output stream.

In line 32, we write the contents of c1 into the output stream using the encoder. Now the output stream contains the binary representation of the object. The rest of the code verifies that the data is indeed in the stream.

In line 35, we construct a memory input stream from the contents of the output stream. Thus the input stream has the binary representation of the object. In line 36 and 37, we construct a binary decoder and attach the input stream to it. Line 40 decodes the contents of the stream into another object c2. Now c1 and c2 should have identical contents, which one can readily verify from the output of the program, which should be:

```

(1, 2.13)
```

Now, if you want to encode the data using Avro JSON encoding, you should use avro::jsonEncoder() instead of avro::binaryEncoder() in line 28 and avro::jsonDecoder() instead of avro::binaryDecoder() in line 36.

On the other hand, if you want to write the contents to a file instead of memory, you should use avro::fileOutputStream() instead of avro::memoryOutputStream() in line 27 and avro::fileInputStream() instead of avro::memoryInputStream() in line 35.

<a id="api-cpp-html--readingjsonschema"></a>
<a id="api-cpp-html--reading-a-json-schema"></a>

## Reading a JSON schema [§](#api-cpp-html--readingjsonschema)

The section above demonstrated pretty much all that's needed to know to get started reading and writing objects using the Avro C++ code generator. The following sections will cover some more information.

The library provides some utilities to read a schema that is stored in a JSON file:

**File: schemaload.cc**

1

19 #include <fstream>

20

21 #include "avro/Compiler.hh"

22 #include "avro/ValidSchema.hh"

23

24 int main() {

25 std::ifstream in("cpx.json");

26

27 avro::ValidSchema cpxSchema;

28 avro::compileJsonSchema(in, cpxSchema);

29 }

This reads the file, and parses the JSON schema into an in-memory schema object of type avro::ValidSchema. If, for some reason, the schema is not valid, the `cpxSchema` object will not be set, and an exception will be thrown.

If you always use code Avro generator you don't really need the in-memory schema objects. But if you use custom objects and routines to encode or decode avro data, you will need the schema objects. Other uses of schema objects are generic data objects and schema resolution described in the following sections.

<a id="api-cpp-html--customencodingdecoding"></a>
<a id="api-cpp-html--custom-encoding-and-decoding"></a>

## Custom encoding and decoding [§](#api-cpp-html--customencodingdecoding)

Suppose you want to encode objects of type std::complex<double> from C++ standard library using the schema defined in cpx.json. Since std::complex<double> was not generated by Avro, it doesn't know how to encode or decode objects of that type. You have to tell Avro how to do that.

The recommended way to tell Avro how to encode or decode is to specialize Avro's codec\_traits template. For std::complex<double>, here is what you'd do:

**File: custom.cc**

1

19 #include <complex>

20

21 #include "avro/Decoder.hh"

22 #include "avro/Encoder.hh"

23 #include "avro/Specific.hh"

24

25 namespace avro {

26 template<typename T>

27 struct codec\_traits<std::complex<T>> {

28 static void encode(Encoder &e, const std::complex<T> &c) {

29 avro::encode(e, std::real(c));

30 avro::encode(e, std::imag(c));

31 }

32

33 static void decode(Decoder &d, std::complex<T> &c) {

34 T re, im;

35 avro::decode(d, re);

36 avro::decode(d, im);

37 c = std::complex<T>(re, im);

38 }

39 };

40

41 } // namespace avro

42 int main() {

43 std::unique\_ptr<avro::OutputStream> out = avro::memoryOutputStream();

44 avro::EncoderPtr e = avro::binaryEncoder();

45 e->init(\*out);

46 std::complex<double> c1(1.0, 2.0);

47 avro::encode(\*e, c1);

48

49 std::unique\_ptr<avro::InputStream> in = avro::memoryInputStream(\*out);

50 avro::DecoderPtr d = avro::binaryDecoder();

51 d->init(\*in);

52

53 std::complex<double> c2;

54 avro::decode(\*d, c2);

55 std::cout << '(' << std::real(c2) << ", " << std::imag(c2) << ')' << std::endl;

56 return 0;

57 }

Please notice that the main function is pretty much similar to that we used for the generated class. Once `codec_traits` for a specific type is supplied, you do not really need to do anything special for your custom types.

But wait, how does Avro know that complex<double> represents the data for the schema in `cpx.json`? It doesn't. In fact, if you have used `std::complex<float>` instead of `std::complex<double>` program would have worked. But the data in the memory would not have been corresponding to the schema in `cpx.json`.

In order to ensure that you indeed use the correct type, you can use the validating encoders and decoder. Here is how:

**File: validating.cc**

1

19 #include <complex>

20 #include <fstream>

21

22 #include "avro/Compiler.hh"

23 #include "avro/Decoder.hh"

24 #include "avro/Encoder.hh"

25 #include "avro/Specific.hh"

26

27 namespace avro {

28 template<typename T>

29 struct codec\_traits<std::complex<T>> {

30 static void encode(Encoder &e, const std::complex<T> &c) {

31 avro::encode(e, std::real(c));

32 avro::encode(e, std::imag(c));

33 }

34

35 static void decode(Decoder &d, std::complex<T> &c) {

36 T re, im;

37 avro::decode(d, re);

38 avro::decode(d, im);

39 c = std::complex<T>(re, im);

40 }

41 };

42

43 } // namespace avro

44 int main() {

45 std::ifstream ifs("cpx.json");

46

47 avro::ValidSchema cpxSchema;

48 avro::compileJsonSchema(ifs, cpxSchema);

49

50 std::unique\_ptr<avro::OutputStream> out = avro::memoryOutputStream();

51 avro::EncoderPtr e = avro::validatingEncoder(cpxSchema,

52 avro::binaryEncoder());

53 e->init(\*out);

54 std::complex<double> c1(1.0, 2.0);

55 avro::encode(\*e, c1);

56

57 std::unique\_ptr<avro::InputStream> in = avro::memoryInputStream(\*out);

58 avro::DecoderPtr d = avro::validatingDecoder(cpxSchema,

59 avro::binaryDecoder());

60 d->init(\*in);

61

62 std::complex<double> c2;

63 avro::decode(\*d, c2);

64 std::cout << '(' << std::real(c2) << ", " << std::imag(c2) << ')' << std::endl;

65 return 0;

66 }

Here, instead of using the plain binary encoder, you use a validating encoder backed by a binary encoder. Similarly, instead of using the plain binary decoder, you use a validating decoder backed by a binary decoder. Now, if you use `std::complex<float>` instead of `std::complex<double>` the validating encoder and decoder will throw exception stating that you are trying to encode or decode `float` instead of `double`.

You can use any encoder behind the validating encoder and any decoder behind the validating decoder. But in practice, only the binary encoder and the binary decoder have no knowledge of the underlying schema. All other encoders (JSON encoder) and decoders (JSON decoder, resolving decoder) do know about the schema and they validate internally. So, fronting them with a validating encoder or validating decoder is wasteful.

<a id="api-cpp-html--genericdataobjects"></a>
<a id="api-cpp-html--generic-data-objects"></a>

## Generic data objects [§](#api-cpp-html--genericdataobjects)

A third way to encode and decode data is to use Avro's generic datum. Avro's generic datum allows you to read any arbitrary data corresponding to an arbitrary schema into a generic object. One need not know anything about the schema or data at compile time.

Here is an example how one can use the generic datum.

**File: generic.cc**

1

19 #include <complex>

20 #include <fstream>

21

22 #include "cpx.hh"

23

24 #include "avro/Compiler.hh"

25 #include "avro/Decoder.hh"

26 #include "avro/Encoder.hh"

27 #include "avro/Generic.hh"

28 #include "avro/Specific.hh"

29

30 int main() {

31 std::ifstream ifs("cpx.json");

32

33 avro::ValidSchema cpxSchema;

34 avro::compileJsonSchema(ifs, cpxSchema);

35

36 std::unique\_ptr<avro::OutputStream> out = avro::memoryOutputStream();

37 avro::EncoderPtr e = avro::binaryEncoder();

38 e->init(\*out);

39 c::cpx c1;

40 c1.re = 100.23;

41 c1.im = 105.77;

42 avro::encode(\*e, c1);

43

44 std::unique\_ptr<avro::InputStream> in = avro::memoryInputStream(\*out);

45 avro::DecoderPtr d = avro::binaryDecoder();

46 d->init(\*in);

47

48 avro::GenericDatum datum(cpxSchema);

49 avro::decode(\*d, datum);

50 std::cout << "Type: " << datum.type() << std::endl;

51 if (datum.type() == avro::AVRO\_RECORD) {

52 const avro::GenericRecord &r = datum.value<avro::GenericRecord>();

53 std::cout << "Field-count: " << r.fieldCount() << std::endl;

54 if (r.fieldCount() == 2) {

55 const avro::GenericDatum &f0 = r.fieldAt(0);

56 if (f0.type() == avro::AVRO\_DOUBLE) {

57 std::cout << "Real: " << f0.value<double>() << std::endl;

58 }

59 const avro::GenericDatum &f1 = r.fieldAt(1);

60 if (f1.type() == avro::AVRO\_DOUBLE) {

61 std::cout << "Imaginary: " << f1.value<double>() << std::endl;

62 }

63 }

64 }

65 return 0;

66 }

In this example, we encode the data using generated code and decode it with generic datum. Then we examine the contents of the generic datum and extract them. Please see avro::GenericDatum for more details on how to use it.

<a id="api-cpp-html--readingdifferentschema"></a>
<a id="api-cpp-html--reading-data-with-a-schema-different-from-that-of-the-writer"></a>

## Reading data with a schema different from that of the writer [§](#api-cpp-html--readingdifferentschema)

It is possible to read the data written according to one schema using a different schema, provided the reader's schema and the writer's schema are compatible according to the Avro's Schema resolution rules.

For example, you have a reader which is interested only in the imaginary part of a complex number while the writer writes both the real and imaginary parts. It is possible to do automatic schema resolution between the writer's schema and schema as shown below.

**File: imaginary.json**

1 {

2 "type": "record",

3 "name": "cpx",

4 "fields" : [

5 {"name": "im", "type" : "double"}

6 ]

7 }

```

avrogencpp -i imaginary.json -o imaginary.hh -n i
```

**File: resolving.cc**

1

19 #include <fstream>

20

21 #include "cpx.hh"

22 #include "imaginary.hh"

23

24 #include "avro/Compiler.hh"

25 #include "avro/Decoder.hh"

26 #include "avro/Encoder.hh"

27 #include "avro/Generic.hh"

28 #include "avro/Specific.hh"

29

30 avro::ValidSchema load(const char \*filename) {

31 std::ifstream ifs(filename);

32 avro::ValidSchema result;

33 avro::compileJsonSchema(ifs, result);

34 return result;

35 }

36

37 int main() {

38 avro::ValidSchema cpxSchema = load("cpx.json");

39 avro::ValidSchema imaginarySchema = load("imaginary.json");

40

41 std::unique\_ptr<avro::OutputStream> out = avro::memoryOutputStream();

42 avro::EncoderPtr e = avro::binaryEncoder();

43 e->init(\*out);

44 c::cpx c1;

45 c1.re = 100.23;

46 c1.im = 105.77;

47 avro::encode(\*e, c1);

48

49 std::unique\_ptr<avro::InputStream> in = avro::memoryInputStream(\*out);

50 avro::DecoderPtr d = avro::resolvingDecoder(cpxSchema, imaginarySchema,

51 avro::binaryDecoder());

52 d->init(\*in);

53

54 i::cpx c2;

55 avro::decode(\*d, c2);

56 std::cout << "Imaginary: " << c2.im << std::endl;

57 }

In this example, writer and reader deal with different schemas, both have a record with the name 'cpx'. The writer schema has two fields and the reader's has just one. We generated code for writer's schema in a namespace `c` and the reader's in `i`.

Please notice how the reading part of the example at line 60 reads as if the stream contains the data corresponding to its schema. The schema resolution is automatically done by the resolving decoder.

In this example, we have used a simple (somewhat artificial) projection (where the set of fields in the reader's schema is a subset of set of fields in the writer's). But more complex resolutions are allowed by Avro specification.

<a id="api-cpp-html--usingavrodatafiles"></a>
<a id="api-cpp-html--using-avro-data-files"></a>

## Using Avro data files [§](#api-cpp-html--usingavrodatafiles)

Avro specification specifies a format for data files. Avro C++ implements the specification. The code below demonstrates how one can use the Avro data file to store and retrieve a collection of objects corresponding to a given schema.

**File: datafile.cc**

1

19 #include <fstream>

20

21 #include "avro/Compiler.hh"

22 #include "avro/DataFile.hh"

23 #include "avro/Decoder.hh"

24 #include "avro/Encoder.hh"

25 #include "avro/ValidSchema.hh"

26 #include "cpx.hh"

27

28 avro::ValidSchema loadSchema(const char \*filename) {

29 std::ifstream ifs(filename);

30 avro::ValidSchema result;

31 avro::compileJsonSchema(ifs, result);

32 return result;

33 }

34

35 int main() {

36 avro::ValidSchema cpxSchema = loadSchema("cpx.json");

37

38 {

39 avro::DataFileWriter<c::cpx> dfw("test.bin", cpxSchema);

40 c::cpx c1;

41 for (int i = 0; i < 100; i++) {

42 c1.re = i \* 100;

43 c1.im = i + 100;

44 dfw.write(c1);

45 }

46 dfw.close();

47 }

48

49 {

50 avro::DataFileReader<c::cpx> dfr("test.bin", cpxSchema);

51 c::cpx c2;

52 while (dfr.read(c2)) {

53 std::cout << '(' << c2.re << ", " << c2.im << ')' << std::endl;

54 }

55 }

56 return 0;

57 }

Please see DataFile.hh for more details.

---

<a id="mapreduce-guide"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/mapreduce-guide/ -->

<!-- page_index: 8 -->

<a id="mapreduce-guide--mapreduce-guide"></a>

# MapReduce guide

Avro provides a convenient way to represent complex data structures within a Hadoop MapReduce job. Avro data can be used as both input to and output from a MapReduce job, as well as the intermediate format. The example in this guide uses Avro data for all three, but it’s possible to mix and match; for instance, MapReduce can be used to aggregate a particular field in an Avro record.

This guide assumes basic familiarity with both Hadoop MapReduce and Avro. See the [Hadoop documentation](https://hadoop.apache.org/docs/current/) and the [Avro getting started guide](https://avro.apache.org/docs/1.12.0/mapreduce-guide/getting-started-java/) for introductions to these projects. This guide uses the old MapReduce API (`org.apache.hadoop.mapred`) and the new MapReduce API (`org.apache.hadoop.mapreduce`).

<a id="mapreduce-guide--setup"></a>

## Setup

The code from this guide is included in the Avro docs under examples/mr-example. The example is set up as a Maven project that includes the necessary Avro and MapReduce dependencies and the Avro Maven plugin for code generation, so no external jars are needed to run the example. In particular, the POM includes the following dependencies:

```xml
<dependency>
  <groupId>org.apache.avro</groupId>
  <artifactId>avro</artifactId>
  <version>1.12.0</version>
</dependency>
<dependency>
  <groupId>org.apache.avro</groupId>
  <artifactId>avro-mapred</artifactId>
  <version>1.12.0</version>
</dependency>
<dependency>
  <groupId>org.apache.hadoop</groupId>
  <artifactId>hadoop-client</artifactId>
  <version>3.1.2</version>
</dependency>
```

And the following plugin:

```xml
<plugin>
  <groupId>org.apache.avro</groupId>
  <artifactId>avro-maven-plugin</artifactId>
  <version>1.12.0</version>
  <executions>
    <execution>
      <phase>generate-sources</phase>
      <goals>
        <goal>schema</goal>
      </goals>
      <configuration>
        <sourceDirectory>${project.basedir}/../</sourceDirectory>
        <outputDirectory>${project.basedir}/target/generated-sources/</outputDirectory>
      </configuration>
    </execution>
  </executions>
</plugin>
```

If you do not configure the *sourceDirectory* and *outputDirectory* properties, the defaults will be used. The *sourceDirectory* property defaults to *src/main/avro*. The *outputDirectory* property defaults to *target/generated-sources*. You can change the paths to match your project layout.

Alternatively, Avro jars can be downloaded directly from the Apache Avro™ Releases [page](https://avro.apache.org/releases.html). The relevant Avro jars for this guide are *avro-1.12.0.jar* and *avro-mapred-1.12.0.jar*, as well as *avro-tools-1.12.0.jar* for code generation and viewing Avro data files as JSON. In addition, you will need to install Hadoop in order to use MapReduce.

<a id="mapreduce-guide--example-colorcount"></a>
<a id="mapreduce-guide--example:-colorcount"></a>

## Example: ColorCount

Below is a simple example of a MapReduce that uses Avro. There is an example for both the old (org.apache.hadoop.mapred) and new (org.apache.hadoop.mapreduce) APIs under *examples/mr-example/src/main/java/example/*. *MapredColorCount* is the example for the older mapred API while *MapReduceColorCount* is the example for the newer mapreduce API. Both examples are below, but we will detail the mapred API in our subsequent examples.

MapredColorCount.java:

```java
package example;

import java.io.IOException;

import org.apache.avro.*;
import org.apache.avro.Schema.Type;
import org.apache.avro.mapred.*;
import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapred.*;
import org.apache.hadoop.util.*;

import example.avro.User;

public class MapredColorCount extends Configured implements Tool {

  public static class ColorCountMapper extends AvroMapper<User, Pair<CharSequence, Integer>> {
    @Override
    public void map(User user, AvroCollector<Pair<CharSequence, Integer>> collector, Reporter reporter)
        throws IOException {
      CharSequence color = user.getFavoriteColor();
      // We need this check because the User.favorite_color field has type ["string", "null"]
      if (color == null) {
        color = "none";
      }
      collector.collect(new Pair<CharSequence, Integer>(color, 1));
    }
  }

  public static class ColorCountReducer extends AvroReducer<CharSequence, Integer,
                                                            Pair<CharSequence, Integer>> {
    @Override
    public void reduce(CharSequence key, Iterable<Integer> values,
                       AvroCollector<Pair<CharSequence, Integer>> collector,
                       Reporter reporter)
        throws IOException {
      int sum = 0;
      for (Integer value : values) {
        sum += value;
      }
      collector.collect(new Pair<CharSequence, Integer>(key, sum));
    }
  }

  public int run(String[] args) throws Exception {
    if (args.length != 2) {
      System.err.println("Usage: MapredColorCount <input path> <output path>");
      return -1;
    }

    JobConf conf = new JobConf(getConf(), MapredColorCount.class);
    conf.setJobName("colorcount");

    FileInputFormat.setInputPaths(conf, new Path(args[0]));
    FileOutputFormat.setOutputPath(conf, new Path(args[1]));

    AvroJob.setMapperClass(conf, ColorCountMapper.class);
    AvroJob.setReducerClass(conf, ColorCountReducer.class);

    // Note that AvroJob.setInputSchema and AvroJob.setOutputSchema set
    // relevant config options such as input/output format, map output
    // classes, and output key class.
    AvroJob.setInputSchema(conf, User.getClassSchema());
    AvroJob.setOutputSchema(conf, Pair.getPairSchema(Schema.create(Type.STRING),
        Schema.create(Type.INT)));

    JobClient.runJob(conf);
    return 0;
  }

  public static void main(String[] args) throws Exception {
    int res = ToolRunner.run(new Configuration(), new MapredColorCount(), args);
    System.exit(res);
  }
}
```

MapReduceColorCount.java:

```java
package example;

import java.io.IOException;

import org.apache.avro.Schema;
import org.apache.avro.mapred.AvroKey;
import org.apache.avro.mapred.AvroValue;
import org.apache.avro.mapreduce.AvroJob;
import org.apache.avro.mapreduce.AvroKeyInputFormat;
import org.apache.avro.mapreduce.AvroKeyValueOutputFormat;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

import example.avro.User;

public class MapReduceColorCount extends Configured implements Tool {

  public static class ColorCountMapper extends
      Mapper<AvroKey<User>, NullWritable, Text, IntWritable> {

    @Override
    public void map(AvroKey<User> key, NullWritable value, Context context)
        throws IOException, InterruptedException {

      CharSequence color = key.datum().getFavoriteColor();
      if (color == null) {
        color = "none";
      }
      context.write(new Text(color.toString()), new IntWritable(1));
    }
  }

  public static class ColorCountReducer extends
      Reducer<Text, IntWritable, AvroKey<CharSequence>, AvroValue<Integer>> {

    @Override
    public void reduce(Text key, Iterable<IntWritable> values,
        Context context) throws IOException, InterruptedException {

      int sum = 0;
      for (IntWritable value : values) {
        sum += value.get();
      }
      context.write(new AvroKey<CharSequence>(key.toString()), new AvroValue<Integer>(sum));
    }
  }

  public int run(String[] args) throws Exception {
    if (args.length != 2) {
      System.err.println("Usage: MapReduceColorCount <input path> <output path>");
      return -1;
    }

    Job job = new Job(getConf());
    job.setJarByClass(MapReduceColorCount.class);
    job.setJobName("Color Count");

    FileInputFormat.setInputPaths(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(args[1]));

    job.setInputFormatClass(AvroKeyInputFormat.class);
    job.setMapperClass(ColorCountMapper.class);
    AvroJob.setInputKeySchema(job, User.getClassSchema());
    job.setMapOutputKeyClass(Text.class);
    job.setMapOutputValueClass(IntWritable.class);

    job.setOutputFormatClass(AvroKeyValueOutputFormat.class);
    job.setReducerClass(ColorCountReducer.class);
    AvroJob.setOutputKeySchema(job, Schema.create(Schema.Type.STRING));
    AvroJob.setOutputValueSchema(job, Schema.create(Schema.Type.INT));

    return (job.waitForCompletion(true) ? 0 : 1);
  }

  public static void main(String[] args) throws Exception {
    int res = ToolRunner.run(new MapReduceColorCount(), args);
    System.exit(res);
  }
}
```

ColorCount reads in data files containing *User* records, defined in *examples/user.avsc*, and counts the number of instances of each favorite color. (This example draws inspiration from the canonical *WordCount* MapReduce application.) This example uses the old MapReduce API. See MapReduceAvroWordCount, found under *doc/examples/mr-example/src/main/java/example/* to see the new MapReduce API example. The User schema is defined as follows:

```json
{"namespace": "example.avro",
 "type": "record",
 "name": "User",
 "fields": [
     {"name": "name", "type": "string"},
     {"name": "favorite_number",  "type": ["int", "null"]},
     {"name": "favorite_color", "type": ["string", "null"]}
 ]
}
```

This schema is compiled into the *User* class used by *ColorCount* via the Avro Maven plugin (see *examples/mr-example/pom.xml* for how this is set up).

*ColorCountMapper* essentially takes a *User* as input and extracts the User’s favorite color, emitting the key-value pair `<favoriteColor, 1>`. *ColorCountReducer* then adds up how many occurrences of a particular favorite color were emitted, and outputs the result as a Pair record. These Pairs are serialized to an Avro data file.

<a id="mapreduce-guide--running-colorcount"></a>

## Running ColorCount

The *ColorCount* application is provided as a Maven project in the Avro docs under *examples/mr-example*. To build the project, including the code generation of the User schema, run:

```shell
mvn compile
```

Next, run *GenerateData* from `examples/mr-examples` to create an Avro data file, `input/users.avro`, containing 20 Users with favorite colors chosen randomly from a list:

```shell
mvn exec:java -q -Dexec.mainClass=example.GenerateData
```

Besides creating the data file, GenerateData prints the JSON representations of the Users generated to stdout, for example:

```json
{"name": "user", "favorite_number": null, "favorite_color": "red"}
{"name": "user", "favorite_number": null, "favorite_color": "green"}
{"name": "user", "favorite_number": null, "favorite_color": "purple"}
{"name": "user", "favorite_number": null, "favorite_color": null}
...
```

Now we’re ready to run ColorCount. We specify our freshly-generated input folder as the input path and output as our output folder (note that MapReduce will not start a job if the output folder already exists):

```shell
mvn exec:java -q -Dexec.mainClass=example.MapredColorCount -Dexec.args="input output"
```

Once ColorCount completes, checking the contents of the new output directory should yield the following:

```shell
$ ls output/part-00000.avro _SUCCESS
```

You can check the contents of the generated Avro file using the avro-tools jar:

```shell
$ java -jar /path/to/avro-tools-1.12.0.jar tojson output/part-00000.avro {"value": 3, "key": "blue"} {"value": 7, "key": "green"} {"value": 1, "key": "none"} {"value": 2, "key": "orange"} {"value": 3, "key": "purple"} {"value": 2, "key": "red"} {"value": 2, "key": "yellow"}
```

Now let’s go over the ColorCount example in detail.

<a id="mapreduce-guide--avromapper-orgapachehadoopmapred-api"></a>
<a id="mapreduce-guide--avromapper-org.apache.hadoop.mapred-api"></a>

## AvroMapper - org.apache.hadoop.mapred API

The easiest way to use Avro data files as input to a MapReduce job is to subclass `AvroMapper`. An `AvroMapper` defines a `map` function that takes an Avro datum as input and outputs a key/value pair represented as a Pair record. In the ColorCount example, ColorCountMapper is an AvroMapper that takes a User as input and outputs a `Pair<CharSequence, Integer>>`, where the CharSequence key is the user’s favorite color and the Integer value is 1.

```java
public static class ColorCountMapper extends AvroMapper<User, Pair<CharSequence, Integer>> {
  @Override
  public void map(User user, AvroCollector<Pair<CharSequence, Integer>> collector, Reporter reporter)
      throws IOException {
    CharSequence color = user.getFavoriteColor();
    // We need this check because the User.favorite_color field has type ["string", "null"]
    if (color == null) {
      color = "none";
    }
    collector.collect(new Pair<CharSequence, Integer>(color, 1));
  }
}
```

In order to use our AvroMapper, we must call AvroJob.setMapperClass and AvroJob.setInputSchema.

```java
AvroJob.setMapperClass(conf, ColorCountMapper.class);
AvroJob.setInputSchema(conf, User.getClassSchema());
```

Note that `AvroMapper` does not implement the `Mapper` interface. Under the hood, the specified Avro data files are deserialized into AvroWrappers containing the actual data, which are processed by a Mapper that calls the configured AvroMapper’s map function. AvroJob.setInputSchema sets up the relevant configuration parameters needed to make this happen, thus you should not need to call `JobConf.setMapperClass`, `JobConf.setInputFormat`, `JobConf.setMapOutputKeyClass`, `JobConf.setMapOutputValueClass`, or `JobConf.setOutputKeyComparatorClass`.

<a id="mapreduce-guide--mapper-orgapachehadoopmapreduce-api"></a>
<a id="mapreduce-guide--mapper-org.apache.hadoop.mapreduce-api"></a>

## Mapper - org.apache.hadoop.mapreduce API

This document will not go into all the differences between the mapred and mapreduce APIs, however will describe the main differences. As you can see, ColorCountMapper is now a subclass of the Hadoop Mapper class and is passed an AvroKey as it’s key. Additionally, the AvroJob method calls were slightly changed.

```java
  public static class ColorCountMapper extends
      Mapper<AvroKey<User>, NullWritable, Text, IntWritable> {

    @Override
    public void map(AvroKey<User> key, NullWritable value, Context context)
        throws IOException, InterruptedException {

      CharSequence color = key.datum().getFavoriteColor();
      if (color == null) {
        color = "none";
      }
      context.write(new Text(color.toString()), new IntWritable(1));
    }
  }
```

<a id="mapreduce-guide--avroreducer-orgapachehadoopmapred-api"></a>
<a id="mapreduce-guide--avroreducer-org.apache.hadoop.mapred-api"></a>

## AvroReducer - org.apache.hadoop.mapred API

Analogously to AvroMapper, an AvroReducer defines a reducer function that takes the key/value types output by an AvroMapper (or any mapper that outputs Pairs) and outputs a key/value pair represented a Pair record. In the ColorCount example, ColorCountReducer is an AvroReducer that takes the CharSequence key representing a favorite color and the `Iterable<Integer>` representing the counts for that color (they should all be 1 in this example) and adds up the counts.

```java
public static class ColorCountReducer extends AvroReducer<CharSequence, Integer,
                                                          Pair<CharSequence, Integer>> {
  @Override
  public void reduce(CharSequence key, Iterable<Integer> values,
                     AvroCollector<Pair<CharSequence, Integer>> collector,
                     Reporter reporter)
      throws IOException {
    int sum = 0;
    for (Integer value : values) {
      sum += value;
    }
    collector.collect(new Pair<CharSequence, Integer>(key, sum));
  }
}
```

In order to use our AvroReducer, we must call AvroJob.setReducerClass and AvroJob.setOutputSchema.

```java
AvroJob.setReducerClass(conf, ColorCountReducer.class);
AvroJob.setOutputSchema(conf, Pair.getPairSchema(Schema.create(Type.STRING),
                                                 Schema.create(Type.INT)));
```

Note that *AvroReducer* does not implement the *Reducer* interface. The intermediate Pairs output by the mapper are split into *AvroKeys* and *AvroValues*, which are processed by a Reducer that calls the configured AvroReducer’s `reduce` function. `AvroJob.setOutputSchema` sets up the relevant configuration parameters needed to make this happen, thus you should not need to call `JobConf.setReducerClass`, `JobConf.setOutputFormat`, `JobConf.setOutputKeyClass`, `JobConf.setMapOutputKeyClass`, `JobConf.setMapOutputValueClass`, or `JobConf.setOutputKeyComparatorClass`.

<a id="mapreduce-guide--reduce-orgapachehadoopmapreduce-api"></a>
<a id="mapreduce-guide--reduce-org.apache.hadoop.mapreduce-api"></a>

## Reduce - org.apache.hadoop.mapreduce API

As before we not detail every difference between the APIs. As with the *Mapper* change *ColorCountReducer* is now a subclass of *Reducer* and *AvroKey* and *AvroValue* are emitted. Additionally, the *AvroJob* method calls were slightly changed.

```java
  public static class ColorCountReducer extends
      Reducer<Text, IntWritable, AvroKey<CharSequence>, AvroValue<Integer>> {

    @Override
    public void reduce(Text key, Iterable<IntWritable> values,
        Context context) throws IOException, InterruptedException {

      int sum = 0;
      for (IntWritable value : values) {
        sum += value.get();
      }
      context.write(new AvroKey<CharSequence>(key.toString()), new AvroValue<Integer>(sum));
    }
  }
```

<a id="mapreduce-guide--learning-more"></a>

## Learning more

The mapred API allows users to mix Avro AvroMappers and AvroReducers with non-Avro Mappers and Reducers and the mapreduce API allows users input Avro and output non-Avro or vice versa.

The mapred package has API org.apache.avro.mapred documentation as does the `org.apache.avro.mapreduce` package. MapReduce API (`org.apache.hadoop.mapreduce`). Similarily to the mapreduce package, it’s possible with the mapred API to implement your own Mappers and Reducers directly using the public classes provided in these libraries. See the `AvroWordCount` application, found under *examples/mr-example/src/main/java/example/AvroWordCount.java* in the Avro documentation, for an example of implementing a Reducer that outputs Avro data using the old MapReduce API. See the `MapReduceAvroWordCount` application, found under *examples/mr-example/src/main/java/example/MapReduceAvroWordCount.java* in the Avro documentation, for an example of implementing a Reducer that outputs Avro data using the new MapReduce API.

Last modified April 27, 2026: [Bump postcss from 8.5.10 to 8.5.12 in /doc (#3741) (fed0011)](https://github.com/apache/avro/commit/fed00117056cdc3dad424cf8442c2d38775e4658)

---

<a id="idl-language"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/idl-language/ -->

<!-- page_index: 9 -->

<a id="idl-language--idl-language"></a>

# IDL Language

<a id="idl-language--introduction"></a>

## Introduction

This document defines Avro IDL, a higher-level language for authoring Avro schemata. Before reading this document, you should have familiarity with the concepts of schemata and protocols, as well as the various primitive and complex types available in Avro.

<a id="idl-language--overview"></a>

## Overview

<a id="idl-language--purpose"></a>

### Purpose

The aim of the Avro IDL language is to enable developers to author schemata in a way that feels more similar to common programming languages like Java, C++, or Python. Additionally, the Avro IDL language may feel more familiar for those users who have previously used the interface description languages (IDLs) in other frameworks like Thrift, Protocol Buffers, or CORBA.

<a id="idl-language--usage"></a>

### Usage

Each Avro IDL file defines either a single Avro Protocol, or an Avro Schema with supporting named schemata in a namespace. When parsed, it thus yields either a Protocol or a Schema. These can be respectively written to JSON-format Avro Protocol files with extension .avpr or JSON-format Avro Schema files with extension .avsc.

To convert a *.avdl* file into a *.avpr* file, it may be processed by the `idl` tool. For example:

```shell
$ java -jar avro-tools.jar idl src/test/idl/input/namespaces.avdl /tmp/namespaces.avpr
$ head /tmp/namespaces.avpr {"protocol" : "TestNamespace","namespace" : "avro.test.protocol",
```

To convert a *.avdl* file into a *.avsc* file, it may be processed by the `idl` tool too. For example:

```shell
$ java -jar avro-tools.jar idl src/test/idl/input/schema_syntax_schema.avdl /tmp/schema_syntax.avsc
$ head /tmp/schema_syntax.avsc {"type": "array","items": {"type": "record","name": "StatusUpdate",
```

The `idl` tool can also process input to and from *stdin* and *stdout*. See `idl --help` for full usage information.

A Maven plugin is also provided to compile .avdl files. To use it, add something like the following to your pom.xml:

```xml
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.avro</groupId>
      <artifactId>avro-maven-plugin</artifactId>
      <executions>
        <execution>
          <goals>
            <goal>idl</goal>
          </goals>
        </execution>
      </executions>
    </plugin>
  </plugins>
</build>
```

<a id="idl-language--defining-a-schema-in-avro-idl"></a>

## Defining a Schema in Avro IDL

An Avro IDL file consists of exactly one (main) schema definition. The minimal schema is defined by the following code:

```java
schema int;
```

This is equivalent to (and generates) the following JSON schema definition:

```json
{
  "type": "int"
}
```

More complex schemata can also be defined, for example by adding named schemata like this:

```java
namespace default.namespace.for.named.schemata;
schema Message;

record Message {
    string? title = null;
    string message;
}
```

This is equivalent to (and generates) the following JSON schema definition:

```json
{
  "type" : "record",
  "name" : "Message",
  "namespace" : "default.namespace.for.named.schemata",
  "fields" : [ {
    "name" : "title",
    "type" : [ "null", "string" ],
    "default": null
  }, {
    "name" : "message",
    "type" : "string"
  } ]
}
```

Schemata in Avro IDL can contain the following items:

- Imports of external protocol and schema files (only named schemata are imported).
- Definitions of named schemata, including records, errors, enums, and fixeds.

<a id="idl-language--defining-a-protocol-in-avro-idl"></a>

## Defining a Protocol in Avro IDL

An Avro IDL file consists of exactly one protocol definition. The minimal protocol is defined by the following code:

```java
protocol MyProtocol {
}
```

This is equivalent to (and generates) the following JSON protocol definition:

```json
{
"protocol" : "MyProtocol",
  "types" : [ ],
  "messages" : {
  }
}
```

The namespace of the protocol may be changed using the @namespace annotation:

```java
@namespace("mynamespace")
protocol MyProtocol {
}
```

This notation is used throughout Avro IDL as a way of specifying properties for the annotated element, as will be described later in this document.

Protocols in Avro IDL can contain the following items:

- Imports of external protocol and schema files.
- Definitions of named schemata, including records, errors, enums, and fixeds.
- Definitions of RPC messages

<a id="idl-language--imports"></a>

## Imports

Files may be imported in one of three formats:

- An IDL file may be imported with a statement like:

  `import idl "foo.avdl";`
- A JSON protocol file may be imported with a statement like:

  `import protocol "foo.avpr";`
- A JSON schema file may be imported with a statement like:

  `import schema "foo.avsc";`

When importing into an IDL schema file, only (named) types are imported into this file. When importing into an IDL protocol, messages are imported into the protocol as well.

Imported file names are resolved relative to the current IDL file.

<a id="idl-language--defining-an-enumeration"></a>

## Defining an Enumeration

Enums are defined in Avro IDL using a syntax similar to C or Java. An Avro Enum supports optional default values. In the case that a reader schema is unable to recognize a symbol written by the writer, the reader will fall back to using the defined default value. This default is only used when an incompatible symbol is read. It is not used if the enum field is missing.

Example Writer Enum Definition

```java
enum Shapes {
  SQUARE, TRIANGLE, CIRCLE, OVAL
}
```

Example Reader Enum Definition

```java
enum Shapes {
  SQUARE, TRIANGLE, CIRCLE
} = CIRCLE;
```

In the above example, the reader will use the default value of `CIRCLE` whenever reading data written with the `OVAL` symbol of the writer. Also note that, unlike the JSON format, anonymous enums cannot be defined.

<a id="idl-language--defining-a-fixed-length-field"></a>

## Defining a Fixed Length Field

Fixed fields are defined using the following syntax:

```
fixed MD5(16);
```

This example defines a fixed-length type called MD5, which contains 16 bytes.

<a id="idl-language--defining-records-and-errors"></a>

## Defining Records and Errors

Records are defined in Avro IDL using a syntax similar to a struct definition in C:

```java
record Employee {
  string name;
  boolean active = true;
  long salary;
}
```

The above example defines a record with the name “Employee” with three fields.

To define an error, simply use the keyword *error* instead of *record*. For example:

```java
error Kaboom {
  string explanation;
  int result_code = -1;
}
```

Each field in a record or error consists of a type and a name, optional property annotations and an optional default value.

A type reference in Avro IDL must be one of:

- A primitive type
- A logical type
- A named schema (either defined or imported)
- A complex type (array, map, or union)

<a id="idl-language--primitive-types"></a>

### Primitive Types

The primitive types supported by Avro IDL are the same as those supported by Avro’s JSON format. This list includes *int*, *long*, *string*, *boolean*, *float*, *double*, *null*, and *bytes*.

<a id="idl-language--logical-types"></a>

### Logical Types

Some of the logical types supported by Avro’s JSON format are directly supported by Avro IDL. The currently supported types are:

- *decimal* (logical type [decimal](#specification--decimal))
- *date* (logical type [date](#specification--date))
- *time\_ms* (logical type [time-millis](#specification--time-millisecond-precision))
- *timestamp\_ms* (logical type [timestamp-millis](#specification--timestamp-millisecond-precision))
- *local\_timestamp\_ms* (logical type [local-timestamp-millis](#specification--local_timestamp_ms))
- *uuid* (logical type [uuid](#specification--uuid))

For example:

```java
record Job {
  string jobid;
  date submitDate;
  time_ms submitTime;
  timestamp_ms finishTime;
  decimal(9,2) finishRatio;
  uuid pk = "a1a2a3a4-b1b2-c1c2-d1d2-d3d4d5d6d7d8";
}
```

Logical types can also be specified via an annotation, which is useful for logical types for which a keyword does not exist:

```java
record Job {
  string jobid;
  @logicalType("timestamp-micros")
  long finishTime;
}
```

<a id="idl-language--references-to-named-schemata"></a>

### References to Named Schemata

If a named schema has already been defined in the same Avro IDL file, it may be referenced by name as if it were a primitive type:

```java
record Card {
  Suit suit; // refers to the enum Card defined above
  int number;
}
```

<a id="idl-language--default-values"></a>

### Default Values

Default values for fields may be optionally specified by using an equals sign after the field name followed by a JSON expression indicating the default value. This JSON is interpreted as described in the [spec](#specification--schema-record).

<a id="idl-language--complex-types"></a>

### Complex Types

<a id="idl-language--arrays"></a>

#### Arrays

Array types are written in a manner that will seem familiar to C++ or Java programmers. An array of any type t is denoted `array<t>`. For example, an array of strings is denoted `array<string>`, and a multidimensional array of Foo records would be `array<array<Foo>>`.

<a id="idl-language--maps"></a>

#### Maps

Map types are written similarly to array types. An array that contains values of type t is written `map<t>`. As in the JSON schema format, all maps contain `string`-type keys.

<a id="idl-language--unions"></a>

#### Unions

Union types are denoted as `union { typeA, typeB, typeC, ... }`. For example, this record contains a string field that is optional (unioned with null), and a field containing either a precise or a imprecise number:

```java
record RecordWithUnion {
  union { null, string } optionalString;
  union { decimal(12, 6), float } number;
}
```

Note that the same restrictions apply to Avro IDL unions as apply to unions defined in the JSON format; namely, a union may not contain multiple elements of the same type. Also, fields/parameters that use the union type and have a default parameter must specify a default value of the same type as the **first** union type.

Because it occurs so often, there is a special shorthand to denote a union of `null` with one other schema. The first three fields in the following snippet have identical schemata, as do the last two fields:

```java
record RecordWithUnion {
  union { null, string } optionalString1 = null;
  string? optionalString2 = null;
  string? optionalString3; // No default value

  union { string, null } optionalString4 = "something";
  string? optionalString5 = "something else";
}
```

Note that unlike explicit unions, the position of the `null` type is fluid; it will be the first or last type depending on the default value (if any). So all fields are valid in the example above.

<a id="idl-language--defining-rpc-messages"></a>

## Defining RPC Messages

The syntax to define an RPC message within a Avro IDL protocol is similar to the syntax for a method declaration within a C header file or a Java interface. To define an RPC message *add* which takes two arguments named *foo* and *bar*, returning an *int*, simply include the following definition within the protocol:

```java
int add(int foo, int bar = 0);
```

Message arguments, like record fields, may specify default values.

To define a message with no response, you may use the alias *void*, equivalent to the Avro *null* type:

```java
void logMessage(string message);
```

If you have defined or imported an error type within the same protocol, you may declare that a message can throw this error using the syntax:

```java
void goKaboom() throws Kaboom;
```

To define a one-way message, use the keyword `oneway` after the parameter list, for example:

```java
void fireAndForget(string message) oneway;
```

<a id="idl-language--other-language-features"></a>

## Other Language Features

<a id="idl-language--comments-and-documentation"></a>

### Comments and documentation

All Java-style comments are supported within a Avro IDL file. Any text following *//* on a line is ignored, as is any text between */\** and *\*/*, possibly spanning multiple lines.

Comments that begin with */\*\** are used as the documentation string for the type or field definition that follows the comment.

<a id="idl-language--escaping-identifiers"></a>

### Escaping Identifiers

Occasionally, one may want to distinguish between identifiers and languages keywords. In order to do so, backticks (`) may be used to escape
the identifier. For example, to define a message with the literal name error, you may write:

```java
void `error`();
```

This syntax is allowed anywhere an identifier is expected.

<a id="idl-language--annotations-for-ordering-and-namespaces"></a>

### Annotations for Ordering and Namespaces

Java-style annotations may be used to add additional properties to types and fields throughout Avro IDL. These can be custom properties, or
special properties as used in the JSON-format Avro Schema and Protocol files.

For example, to specify the sort order of a field within a record, one may use the `@order` annotation before the field name as follows:

```java
record MyRecord {
  string @order("ascending") myAscendingSortField;
  string @order("descending")  myDescendingField;
  string @order("ignore") myIgnoredField;
}
```

A field’s type (with the exception of type references) may also be preceded by annotations, e.g.:

```java
record MyRecord {
  @java-class("java.util.ArrayList") array<string> myStrings;
}
```

This can be used to support java classes that can be serialized/deserialized via their `toString`/`String constructor`, e.g.:

```java
record MyRecord {
  @java-class("java.math.BigDecimal") string value;
  @java-key-class("java.io.File") map<string> fileStates;
  array<@java-class("java.math.BigDecimal") string> weights;
}
```

Similarly, a `@namespace` annotation may be used to modify the namespace when defining a named schema. For example:

```java
@namespace("org.apache.avro.firstNamespace")
protocol MyProto {
  @namespace("org.apache.avro.someOtherNamespace")
  record Foo {}

  record Bar {}
}
```

will define a protocol in the *firstNamespace* namespace. The record *Foo* will be defined in *someOtherNamespace* and *Bar* will be defined in *firstNamespace* as it inherits its default from its container.

Type and field aliases are specified with the `@aliases` annotation as follows:

```java
@aliases(["org.old.OldRecord", "org.ancient.AncientRecord"])
record MyRecord {
  string @aliases(["oldField", "ancientField"]) myNewField;
}
```

Some annotations like those listed above are handled specially. All other annotations are added as properties to the protocol, message, schema or field. You can use any identifier or series of identifiers separated by dots and/or dashes as property name.

<a id="idl-language--complete-example"></a>

## Complete Example

The following is an example of two Avro IDL files that together show most of the above features:

<a id="idl-language--schemaavdl"></a>
<a id="idl-language--schema.avdl"></a>

### schema.avdl

```java
/*
 * Header with license information.
 */
// Optional default namespace (if absent, the default namespace is the null namespace).
namespace org.apache.avro.test;
// Optional main schema definition; if used, the IDL file is equivalent to a .avsc file.
schema TestRecord;

/** Documentation for the enum type Kind */
@aliases(["org.foo.KindOf"])
enum Kind {
  FOO,
  BAR, // the bar enum value
  BAZ
} = FOO; // For schema evolution purposes, unmatched values do not throw an error, but are resolved to FOO.

/** MD5 hash; good enough to avoid most collisions, and smaller than (for example) SHA256. */
fixed MD5(16);

record TestRecord {
  /** Record name; has no intrinsic order */
  string @order("ignore") name;

  Kind @order("descending") kind;

  MD5 hash;

  /*
  Note that 'null' is the first union type. Just like .avsc / .avpr files, the default value must be of the first union type.
  */
  union { null, MD5 } /** Optional field */ @aliases(["hash"]) nullableHash = null;
  // Shorthand syntax; the null in this union is placed based on the default value (or first is there's no default).
  MD5? anotherNullableHash = null;

  array<long> arrayOfLongs;
}
```

<a id="idl-language--protocolavdl"></a>
<a id="idl-language--protocol.avdl"></a>

### protocol.avdl

```java
/*
 * Header with license information.
 */

/**
 * An example protocol in Avro IDL
 */
@namespace("org.apache.avro.test")
protocol Simple {
  // Import the example file above
  import idl "schema.avdl";

  /** Errors are records that can be thrown from a method */
  error TestError {
    string message;
  }

  string hello(string greeting);
  /** Return what was given. Demonstrates the use of backticks to name types/fields/messages/parameters after keywords */
  TestRecord echo(TestRecord `record`);
  int add(int arg1, int arg2);
  bytes echoBytes(bytes data);
  void `error`() throws TestError;
  // The oneway keyword forces the method to return null.
  void ping() oneway;
}
```

Additional examples may be found in the Avro source tree under the `src/test/idl/input` directory.

<a id="idl-language--ide-support"></a>

## IDE support

There are several editors and IDEs that support Avro IDL files, usually via plugins.

<a id="idl-language--jetbrains"></a>

### JetBrains

Apache Avro IDL Schema Support 203.1.2 was released in 9 December 2021.

Features:

- Syntax Highlighting
- Code Completion
- Code Formatting
- Error Highlighting
- Inspections & quick fixes
- JSON schemas for .avpr and .avsc files

It’s available via the [JetBrains Marketplace](https://plugins.jetbrains.com/plugin/15728-apache-avro-idl-schema-support)
and on [GitHub](https://github.com/opwvhk/avro-schema-support).

The plugin supports almost the all JetBrains products: IntelliJ IDEA, PyCharm, WebStorm, Android Studio, AppCode, GoLand, Rider, CLion, RubyMine, PhpStorm, DataGrip, DataSpell, MPS, Code With Me Guest and JetBrains Client.

Only JetBrains Gateway does not support this plugin directly. But the backend (JetBrains) IDE that it connects to does.

<a id="idl-language--eclipse"></a>

### Eclipse

Avroclipse 0.0.11 was released on 4 December 2019.

Features:

- Syntax Highlighting
- Error Highlighting
- Code Completion

It is available on the [Eclipse Marketplace](https://marketplace.eclipse.org/content/avroclipse)
and [GitHub](https://github.com/dvdkruk/avroclipse).

<a id="idl-language--visual-studio-code"></a>

### Visual Studio Code

avro-idl 0.5.0 was released on 16 June 2021. It provides syntax highlighting.

It is available on the [VisualStudio Marketplace](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.avro)
and [GitHub](https://github.com/Jason3S/vscode-avro-ext)

<a id="idl-language--atomio"></a>
<a id="idl-language--atom.io"></a>

### Atom.io

atom-language-avro 0.0.13 was released on 14 August 2015. It provides syntax highlighting.

It is available as [Atom.io package](https://atom.io/packages/atom-language-avro)
and [GitHub](https://github.com/jonesetc/atom-language-avro)

<a id="idl-language--vim"></a>

### Vim

A `.avdl` detecting plugin by Gurpreet Atwal on [GitHub](https://github.com/gurpreetatwal/vim-avro) (Last change in December 2016)

[avro-idl.vim](https://github.com/apache/avro/blob/main/share/editors/avro-idl.vim) in the Avro repository `share/editors` directory (last change in September 2010)

Both provide syntax highlighting.

Last modified April 27, 2026: [Bump postcss from 8.5.10 to 8.5.12 in /doc (#3741) (fed0011)](https://github.com/apache/avro/commit/fed00117056cdc3dad424cf8442c2d38775e4658)

---

<a id="sasl-profile"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/sasl-profile/ -->

<!-- page_index: 10 -->

<a id="sasl-profile--sasl-profile"></a>

# SASL profile

<a id="sasl-profile--introduction"></a>

## Introduction

SASL ([RFC 2222](https://www.ietf.org/rfc/rfc2222.txt)) provides a framework for authentication and security of network protocols. Each protocol that uses SASL is meant to define a SASL profile. This document provides a SASL profile for connection-based Avro RPC.

<a id="sasl-profile--overview"></a>

## Overview

SASL negotiation proceeds as a series of message interactions over a connection between a client and server using a selected SASL mechanism. The client starts this negotiation by sending its chosen mechanism name with an initial (possibly empty) message. Negotiation proceeds with the exchange of messages until either side indicates success or failure. The content of the messages is mechanism-specific. If the negotiation succeeds, then the session can proceed over the connection, otherwise it must be abandoned.

Some mechanisms continue to process session data after negotiation (e.g., encrypting it), while some specify that further session data is transmitted unmodified.

<a id="sasl-profile--negotiation"></a>

## Negotiation

<a id="sasl-profile--commands"></a>

### Commands

Avro SASL negotiation uses four one-byte commands.

- 0: START Used in a client’s initial message.
- 1: CONTINUE Used while negotiation is ongoing.
- 2: FAIL Terminates negotiation unsuccessfully.
- 3: COMPLETE Terminates negotiation successfully.

The format of a START message is:

`| 0 | 4-byte mechanism name length | mechanism name | 4-byte payload length | payload data |`

The format of a CONTINUE message is:

`| 1 | 4-byte payload length | payload data |`

The format of a FAIL message is:

`| 2 | 4-byte message length | UTF-8 message |`

The format of a COMPLETE message is:

`| 3 | 4-byte payload length | payload data |`

<a id="sasl-profile--process"></a>

### Process

Negotiation is initiated by a client sending a START command containing the client’s chosen mechanism name and any mechanism-specific payload data.

The server and client then interchange some number (possibly zero) of CONTINUE messages. Each message contains payload data that is processed by the security mechanism to generate the next message.

Once either the client or server send a FAIL message then negotiation has failed. UTF-8-encoded text is included in the failure message. Once either a FAIL message has been sent or received, or any other error occurs in the negotiation, further communication on this connection must cease.

Once either the client or server send a COMPLETE message then negotiation has completed successfully. Session data may now be transmitted over the connection until it is closed by either side.

<a id="sasl-profile--session-data"></a>

## Session Data

If no SASL QOP (quality of protection) is negotiated, then all subsequent writes to/reads over this connection are written/read unmodified. In particular, messages use Avro [framing](#sasl-profile--message-framing), and are of the form:

`| 4-byte frame length | frame data | ... | 4 zero bytes |`

If a SASL QOP is negotiated, then it must be used by the connection for all subsequent messages. This is done by wrapping each non-empty frame written using the security mechanism and unwrapping each non-empty frame read. The length written in each non-empty frame is the length of the wrapped data. Complete frames must be passed to the security mechanism for unwrapping. Unwrapped data is then passed to the application as the content of the frame.

If at any point processing fails due to wrapping, unwrapping or framing errors, then all further communication on this connection must cease.

<a id="sasl-profile--anonymous-mechanism"></a>

## Anonymous Mechanism

The SASL anonymous mechanism ([RFC 2245](https://www.ietf.org/rfc/rfc2222.txt)) is quite simple to implement. In particular, an initial anonymous request may be prefixed by the following static sequence:

`| 0 | 0009 | ANONYMOUS | 0000 |`

If a server uses the anonymous mechanism, it should check that the mechanism name in the start message prefixing the first request received is ‘ANONYMOUS’, then simply prefix its initial response with a COMPLETE message of:

`| 3 | 0000 |`

If an anonymous server recieves some other mechanism name, then it may respond with a FAIL message as simple as:

`| 2 | 0000 |`

Note that the anonymous mechanism need add no additional round-trip messages between client and server. The START message can be piggybacked on the initial request and the COMPLETE or FAIL message can be piggybacked on the initial response.

Last modified April 27, 2026: [Bump postcss from 8.5.10 to 8.5.12 in /doc (#3741) (fed0011)](https://github.com/apache/avro/commit/fed00117056cdc3dad424cf8442c2d38775e4658)

---

<a id="trevni"></a>

<!-- source_url: https://avro.apache.org/docs/1.12.0/trevni/ -->

<!-- page_index: 11 -->

<a id="trevni--about-trevni-java"></a>

## About Trevni Java

Trevni Java

<a id="trevni--project-modules"></a>

### Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Trevni Java Core](https://avro.apache.org/docs/1.12.0/trevni/trevni-core/index.html) | Trevni Java Core |
| [Trevni Java Avro](https://avro.apache.org/docs/1.12.0/trevni/trevni-avro/index.html) | Trevni Java Avro |
| [Trevni Specification](https://avro.apache.org/docs/1.12.0/trevni/trevni-doc/index.html) | Trevni Java |

---
