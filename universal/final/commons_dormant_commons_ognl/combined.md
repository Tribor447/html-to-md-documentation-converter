# OGNL - Project Information

## Navigation

- OGNL
  - [Overview](#index)
  - [Language Guide](#language-guide)
  - [Developer Guide](#developer-guide)
  - [Benchmarks](#benchmark)
- Development
  - [Issue Tracking](#issue-tracking)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Project Summary](#project-summary)
    - [Issue Tracking](#issue-tracking)
    - [Continuous Integration](#integration)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-commons-ognl-object-graph-navigation-library"></a>

## Apache Commons OGNL - Object Graph Navigation Library

OGNL stands for Object-Graph Navigation Language; it is an expression language for getting and setting
properties of Java objects, plus other extras such as list projection and selection and lambda expressions.
You use the same expression for both getting and setting the value of a property.

The Ognl class contains convenience methods for evaluating OGNL expressions. You can do this in two
stages, parsing an expression into an internal form and then using that internal form to either set or get the
value of a property; or you can do it in a single stage, and get or set a property using the String form of the
expression directly.

OGNL started out as a way to set up associations between UI components and controllers using property names. As the
desire for more complicated associations grew, Drew Davidson created what he called KVCL, for Key-Value Coding
Language, egged on by Luke Blanshard. Luke then reimplemented the language using ANTLR, came up with the new name, and, egged on by Drew, filled it out to its current state. Later on Luke again reimplemented the language using
JavaCC. Further maintenance on all the code is done by Drew (with spiritual guidance from Luke).

We pronounce OGNL as a word, like the last syllables of a drunken pronunciation of "*orthogonal*".

<a id="index--introduction"></a>

## Introduction

Many people have asked exactly what OGNL is good for. Several of the uses to which OGNL
has been applied are:

- A binding language between GUI elements (textfield, combobox, etc.) to model objects. Transformations are made
  easier by OGNL's TypeConverter mechanism to convert values from one type to another (String to
  numeric types, for example);
- A data source language to map between table columns and a Swing TableModel;
- A binding language between web components and the underlying model objects;
- A more expressive replacement for the property-getting language used by the Apache Commons BeanUtils package or
  JSTL's EL (which only allow simple property navigation and rudimentary indexed properties).

Most of what you can do in Java is possible in OGNL, plus other extras such as list *projection*,
*selection* and *lambda expressions*.

---

<a id="language-guide"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/language-guide.html -->

<!-- page_index: 2 -->

<a id="language-guide--syntax"></a>

## Syntax

Basic OGNL expressions are very simple. The language has become quite rich with features, but
you don't generally need to worry about the more complicated parts of the language: the simple cases have
remained that way. For example, to get at the name property of an object, the OGNL expression
is simply name. To get at the text property of the object returned by the headline
property, the OGNL expression is headline.text.

What is a property? Roughly, an OGNL property is the same as a bean property, which means that
a pair of get/set methods, or alternatively a field, defines a property (the full story is a bit more complicated, since properties differ for different kinds of objects; see below for a full explanation).

The fundamental unit of an OGNL expression is the navigation chain, usually just called
"chain." The simplest chains consist of the following parts:

| Expression Element Part | Example |
| --- | --- |
| Property names | like the name and headline.text examples above |
| Method Calls | hashCode() to return the current object's hash code |
| Array Indices | listeners[0] to return the first of the current object's list of listeners |

All OGNL expressions are evaluated in the context of a current object, and a chain simply uses
the result of the previous link in the chain as the current object for the next one. You can extend a chain as
long as you like. For example, this chain:

```
name.toCharArray()[0].numericValue.toString()
```

This expression follows these steps to evaluate:

- extracts the name property of the initial, or root, object (which the user provides to
  OGNL through the OGNL context);
- calls the toCharArray() method on the resulting String;
- extracts the first character (the one at index 0) from the resulting array;
- gets the numericValue property from that character (the character is represented as a
  Character object, and the Character class has a method called
  getNumericValue());
- calls toString() on the resulting Integer object. The final result of this expression
  is the String returned by the last toString() call.

Note that this example can only be used to get a value from an object, not to set a value. Passing the above
expression to the Ognl.setValue() method would cause an InappropriateExpressionException
to be thrown, because the last link in the chain is neither a property name nor an array index.

This is enough syntax to do the vast majority of what you ever need to do.

<a id="language-guide--expressions"></a>

## Expressions

This section outlines the details the elements of OGNL's expressions.

<a id="language-guide--constants"></a>

### Constants

OGNL has the following kinds of constants:

- String literals, as in Java (with the addition of single quotes): delimited by single- or double-quotes,
  with the full set of character escapes;
- Character literals, also as in Java: delimited by single-quotes, also with the full set of escapes;
- Numeric literals, with a few more kinds than Java. In addition to Java's ints, longs, floats and doubles,
  OGNL lets you specify BigDecimals with a "b" or "B" suffix, and BigIntegers
  with an "h" or "H" suffix (think "huge"---we chose "h" for BigIntegers because
  it does not interfere with hexadecimal digits);
- Boolean (true and false) literals;
- The null literal.

<a id="language-guide--referring-to-properties"></a>

### Referring to Properties

OGNL treats different kinds of objects differently in its handling of property references.
Maps treat all property references as element lookups or storage, with the property name as the key.
Lists and arrays treat numeric properties similarly, with the property name as the index, but string properties
the same way ordinary objects do. Ordinary objects (that is, all other kinds) only can handle string properties
and do so by using "get" and "set" methods (or "is" and "set"), if the object
has them, or a field with the given name otherwise.

Note the new terminology here. Property "names" can be of any type, not just Strings. But to refer to
non-String properties, you must use what we have been calling the "index" notation. For example, to get
the length of an array, you can use this expression:

```
array.length
```

But to get at element 0 of the array, you must use an expression like this:

```
array[0]
```

Note that Java collections have some special properties associated with them.

<a id="language-guide--indexing"></a>

### Indexing

As discussed above, the "indexing" notation is actually just property reference, though a computed form
of property reference rather than a constant one.

For example, OGNL internally treats the "array.length" expression exactly the same as
this expression:

```
array["length"]
```

And this expression would have the same result (though not the same internal form):

```
array["len" + "gth"]
```

**Array and List Indexing**

For Java arrays and Lists indexing is fairly simple, just like in Java.
An integer index is given and that element is the referrent. If the index is out of bounds of the array or List
and IndexOutOfBoundsException is thrown, just as in Java.

**JavaBeans Indexed Properties**

JavaBeans supports the concept of Indexed properties. Specifically this means that an object has a set of
methods that follow the following pattern:

- public *PropertyType*[] get*PropertyName*();
- public void set*PropertyName*(*PropertyType*[] anArray);
- public *PropertyType* get*PropertyName*(int index);
- public void set*PropertyName*(int index, *PropertyType* value);

OGNL can interpret this and provide seamless access to the property through the indexing notation.
References such as

```
someProperty[2]
```

are automatically routed through the correct indexed property accessor (in the above case through
getSomeProperty(2) or setSomeProperty(2, value)). If there is no indexed property
accessor a property is found with the name someProperty and the index is applied to that.

**OGNL Object Indexed Properties**

OGNL extends the concept of indexed properties to include indexing with arbitrary objects, not just integers as
with JavaBeans Indexed Properties. When finding properties as candidates for object indexing, OGNL looks for
patterns of methods with the following signature:

- public *PropertyType* get*PropertyName*(*IndexType* index);
- public void set*PropertyName*(*IndexType* index, *PropertyType* value);

The PropertyType and IndexType must match each other in the corresponding set and get
methods. An actual example of using Object Indexed Properties is with the Servlet API: the Session object has
two methods for getting and setting arbitrary attributes:

```
public Object getAttribute(String name) public void setAttribute(String name, Object value)
```

An OGNL expression that can both get and set one of these attributes is:

```
session.attribute["foo"]
```

<a id="language-guide--calling-methods"></a>

## Calling Methods

OGNL calls methods a little differently from the way Java does, because
OGNL is interpreted and must choose the right method at run time, with no extra type
information aside from the actual arguments supplied. OGNL always chooses the most specific
method it can find whose types match the supplied arguments; if there are two or more methods that are equally
specific and match the given arguments, one of them will be chosen arbitrarily.

In particular, a null argument matches all non-primitive types, and so is most likely to result in an unexpected
method being called.

Note that the arguments to a method are separated by commas, and so the comma operator cannot be used unless it is
enclosed in parentheses. For example,

```
method( ensureLoaded(), name )
```

is a call to a 2-argument method, while

```
method( (ensureLoaded(), name) )
```

is a call to a 1-argument method.

<a id="language-guide--variable-references"></a>

## Variable References

OGNL has a simple variable scheme, which lets you store intermediate results and use them
again, or just name things to make an expression easier to understand. All variables in OGNL
are global to the entire expression. You refer to a variable using a number sign in front of its name, like this:

```
#var
```

OGNL also stores the current object at every point in the evaluation of an expression in the
this variable, where it can be referred to like any other variable. For example, the following expression operates
on the number of listeners, returning twice the number if it is more than 100, or 20 more than the number otherwise:

```
listeners.size().(#this > 100? 2*#this : 20+#this)
```

OGNL can be invoked with a map that defines initial values for variables. The standard way of
invoking OGNL defines the variables root (which holds the initial, or root, object), and context (which holds the Map of variables itself).

To assign a value to a variable explicitly, simply write an assignment statement with a variable reference on the
left-hand side:

```
#var = 99
```

<a id="language-guide--parenthetical-expressions"></a>

## Parenthetical Expressions

As you would expect, an expression enclosed in parentheses is evaluated as a unit, separately from any surrounding
operators. This can be used to force an evaluation order different from the one that would be implied by
OGNL operator precedences. It is also the only way to use the comma operator in a method
argument.

<a id="language-guide--chained-subexpressions"></a>

## Chained Subexpressions

If you use a parenthetical expression after a dot, the object that is current at the dot is used as the current object throughout the parenthetical expression. For example,

```
headline.parent.(ensureLoaded(), name)
```

traverses through the headline and parent properties, ensures that the parent is loaded and then returns (or sets) the parent's name.

Top-level expressions can also be chained in this way. The result of the expression is the right-most expression element.

```
ensureLoaded(), name
```

This will call ensureLoaded() on the root object, then get the name property of the root object as the result of the expression.

<a id="language-guide--collection-construction"></a>

## Collection Construction

<a id="language-guide--lists"></a>

### Lists

To create a list of objects, enclose a list of expressions in curly braces. As with method arguments, these expressions cannot use the comma operator unless it is enclosed in parentheses. Here is an example:

```
name in { null,"Untitled" }
```

This tests whether the name property is null or equal to "Untitled".

The syntax described above will create a instanceof the List interface. The exact subclass is not defined.

<a id="language-guide--native-arrays"></a>

### Native Arrays

Sometimes you want to create Java native arrays, such as int[] or Integer[]. OGNL supports the creation of these similarly to the way that constructors are normally called, but allows
initialization of the native array from either an existing list or a given size of the array.

```
new int[] { 1, 2, 3 }
```

This creates a new int array consisting of three integers 1, 2 and 3.

To create an array with all null or 0 elements, use the alternative size constructor

```
new int[5]
```

This creates an int array with 5 slots, all initialized to zero.

<a id="language-guide--maps"></a>

### Maps

Maps can also be created using a special syntax.

```
#{ "foo" : "foo value", "bar" : "bar value" }
```

This creates a Map initialized with mappings for "foo" and "bar".

Advanced users who wish to select the specific Map class can specify that class before the opening curly brace

```
#@java.util.LinkedHashMap@{ "foo" : "foo value", "bar" : "bar value" }
```

The above example will create an instance of the JDK 1.4 class LinkedHashMap, ensuring the the insertion order of the elements is preserved.

<a id="language-guide--projecting-across-collections"></a>

## Projecting Across Collections

OGNL provides a simple way to call the same method or extract the same property from each element in a collection and store the results in a new collection. We call this "projection," from the database
term for choosing a subset of columns from a table. For example, this expression:

```
listeners.{delegate}
```

returns a list of all the listeners' delegates. See the coercion section for how OGNL treats various kinds of objects as collections.

During a projection the #this variable refers to the current element of the iteration.

```
objects.{ #this instanceof String ? #this : #this.toString()}
```

The above would produce a new list of elements from the objects list as string values.

<a id="language-guide--selecting-from-collections"></a>

## Selecting From Collections

OGNL provides a simple way to use an expression to choose some elements from a collection and save the results in a new collection. We call this "selection," from the database term for choosing a subset of
rows from a table. For example, this expression:

```
listeners.{? #this instanceof ActionListener}
```

returns a list of all those listeners that are instances of the ActionListener class.

<a id="language-guide--selecting-first-match"></a>

### Selecting First Match

In order to get the first match from a list of matches, you could use indexing such as listeners.{? true }[0]. However, this is cumbersome because if the match does not return any results (or if the result
list is empty) you will get an ArrayIndexOutOfBoundsException.

The selection syntax is also available to select only the first match and return it as a list. If the match does not succeed for any elements an empty list is the result.

```
objects.{^ #this instanceof String }
```

Will return the first element contained in objects that is an instance of the String class.

<a id="language-guide--selecting-last-match"></a>

### Selecting Last Match

Similar to getting the first match, sometimes you want to get the last element that matched.

```
objects.{$ #this instanceof String }
```

This will return the last element contained in objects that is an instanceof the String class

<a id="language-guide--calling-constructors"></a>

## Calling Constructors

You can create new objects as in Java, with the new operator. One difference is that you must specify the fully qualified class name for classes other than those in the java.lang package.

This is only true with the default ClassResolver in place. With a custom class resolver packages can be mapped in such a way that more Java-like references to classes can be made. Refer to the
OGNL Developer's Guide for details on using ClassResolver class (for example, new java.util.ArrayList(), rather than simply new ArrayList()).

OGNL chooses the right constructor to call using the same procedure it uses for overloaded method calls.

<a id="language-guide--calling-static-methods"></a>

## Calling Static Methods

You can call a static method using the syntax @class@method(args). If you leave out class, it defaults to java.lang.Math, to
make it easier to call min and max methods. If you specify the class, you must give the fully qualified name.

If you have an instance of a class whose static method you wish to call, you can call the method through the object as if it was an instance method.

If the method name is overloaded, OGNL chooses the right static method to call using the same procedure it uses for overloaded instance methods.

<a id="language-guide--getting-static-fields"></a>

## Getting Static Fields

You can refer to a static field using the syntax @class@field. The class must be fully qualified.

<a id="language-guide--expression-evaluation"></a>

## Expression Evaluation

If you follow an OGNL expression with a parenthesized expression, without a dot in front of the parentheses, OGNL will try to treat the result of the first expression as another expression to
evaluate, and will use the result of the parenthesized expression as the root object for that evaluation. The result of the first expression may be any object; if it is an AST, OGNL assumes it is the parsed form of an
expression and simply interprets it; otherwise, OGNL takes the string value of the object and parses that string to get the AST to interpret.

For example, this expression

```
#fact(30H)
```

looks up the fact variable, and interprets the value of that variable as an OGNL expression using the BigInteger representation of 30 as the
root object. See below for an example of setting the fact variable with an expression that returns the factorial of its argument. Note that there is an ambiguity in OGNL's
syntax between this double evaluation operator and a method call. OGNL resolves this ambiguity by calling anything that looks like a method call, a method call. For example, if the current object had a fact property
that held an OGNL factorial expression, you could not use this approach to call it

```
fact(30H)
```

because OGNL would interpret this as a call to the fact method. You could force the interpretation you want by surrounding the property reference by parentheses:

```
(fact)(30H)
```

<a id="language-guide--pseudo-lambda-expressions"></a>

## Pseudo-Lambda Expressions

OGNL has a simplified lambda-expression syntax, which lets you write simple functions. It is not a full-blown lambda calculus, because there are no closures---all variables in OGNL have global
scope and extent.

For example, here is an OGNL expression that declares a recursive factorial function, and then calls it:

```
#fact = :[#this<=1? 1 : #this*#fact(#this-1)], #fact(30H)
```

The lambda expression is everything inside the brackets. The #this variable holds the argument to the expression, which is initially 30H, and is then one less for each successive call to the
expression.

OGNL treats lambda expressions as constants. The value of a lambda expression is the AST that OGNL uses as the parsed form of the contained expression.

<a id="language-guide--pseudo-properties-for-collections"></a>

## Pseudo-Properties for Collections

There are some special properties of collections that OGNL makes available. The reason for this is that the collections do not follow JavaBeans patterns for method naming; therefore the size(), length(), etc. methods must be called instead of more intuitively referring to these as properties. OGNL corrects this by exposing certain pseudo-properties as if they were built-in.

<table border="0" class="bodyTable"><caption>Special Collections Pseudo-Properties</caption>
<thead>
<tr>
<th>Collection</th>
<th>Special Properties</th>
</tr>
</thead>
<tbody>
<tr>
<td>Collection (inherited by Map, List &amp; Set)</td>
<td>
<ul>
<li>size: The size of the collection</li>
<li>isEmpty: Evaluates
                            to true if the collection is empty</li>
</ul>
</td>
</tr>
<tr>
<td>List</td>
<td>
<ul>
<li>iterator: Evalutes to an Iterator over the List.</li>
</ul>
</td>
</tr>
<tr>
<td>Map</td>
<td>
<ul>
<li>keys: Evalutes to a Set of all keys in the Map</li>
<li>values: Evaluates to a Collection of all values in the Map</li>
</ul>
Note These properties, plus size and isEmpty,
                            are different than the indexed form of access for Maps (i.e. someMap["size"] gets the "size" key from the map, whereas someMap.size
                            gets the size of the Map
</td>
</tr>
<tr>
<td>Set</td>
<td>
<ul>
<li>iterator: Evalutes to an Iterator over the Set</li>
</ul>
</td>
</tr>
<tr>
<td>Iterator</td>
<td>
<ul>
<li>next: Evalutes to the next object from the Iterator</li>
<li>hasNext: Evaluates to true if there is a next object available from the Iterator</li>
</ul>
</td>
</tr>
<tr>
<td>Enumeration</td>
<td>
<ul>
<li>next: Evalutes to the next object from the Enumeration</li>
<li>hasNext: Evaluates to true if there is a next object available from the Enumeration</li>
<li>nextElement: Synonym for next</li>
<li>hasMoreElements: Synonym for hasNext</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="language-guide--operators-that-differ-from-java-s-operators"></a>

## Operators that differ from Java's operators

For the most part, OGNL's operators are borrowed from Java and work similarly to Java's operators. See the OGNL Reference for a complete discussion. Here we describe OGNL
operators that are not in Java, or that are different from Java.

- The comma (,) or sequence operator. This operator is borrowed from C. The comma is used to separate two independent expressions. The value of the second of these expressions is the value of the comma expression. Here is an
  example:


```
ensureLoaded(), name
```

  When this expression is evaluated, the ensureLoaded method is called (presumably to make sure that all parts of the object are in memory), then the name property is retrieved (if getting the value) or replaced (if setting).
- List construction with curly braces ({}). You can create a list in-line by enclosing the values in curly braces, as in this example:


```
{ null, true, false }
```

- The in operator (and not in, its negation). This is a containment test, to see if a value is in a collection. For example,


```
name in {null,"Untitled"} || name
```

<a id="language-guide--setting-values-versus-getting-values"></a>

## Setting values versus getting values

As stated before, some values that are gettable are not also settable because of the nature of the expression. For example,

```
names[0].location
```

is a settable expression - the final component of the expression resolves to a settable property.

However, some expressions, such as

```
names[0].length + 1
```

are not settable because they do not resolve to a settable property in an object. It is simply a computed value. If you try to evaluate this expression using any of the Ognl.setValue() methods it will fail with
an InappropriateExpressionException.

It is also possible to set variables using get expressions that include the '=' operator. This is useful when a get expression needs to set a variable as a side effect of execution.

<a id="language-guide--coercing-objects-to-types"></a>

## Coercing Objects to Types

Here we describe how OGNL interprets objects as various types. See below for how OGNL coerces objects to booleans, numbers, integers, and collections.

<a id="language-guide--interpreting-objects-as-booleans"></a>

### Interpreting Objects as Booleans

Any object can be used where a boolean is required. OGNL interprets objects as booleans like this:

- If the object is a Boolean, its value is extracted and returned;
- If the object is a Number, its double-precision floating-point value is compared with zero; non-zero is treated as true, zero as false;
- If the object is a Character, its boolean value is true if and only if its char value is non-zero;
- Otherwise, its boolean value is true if and only if it is non-null.

<a id="language-guide--interpreting-objects-as-numbers"></a>

### Interpreting Objects as Numbers

Numerical operators try to treat their arguments as numbers. The basic primitive-type wrapper classes (Integer, Double, and so on, including Character and Boolean, which are treated as integers), and the "big" numeric
classes from the java.math package (BigInteger and BigDecimal), are recognized as special numeric types. Given an object of some other class, OGNL tries to parse the object's string value as a number.

Numerical operators that take two arguments use the following algorithm to decide what type the result should be. The type of the actual result may be wider, if the result does not fit in the given type.

- If both arguments are of the same type, the result will be of the same type if possible;
- If either argument is not of a recognized numeric class, it will be treated as if it was a Double for the rest of this algorithm;
- If both arguments are approximations to real numbers (Float, Double, or BigDecimal), the result will be the wider type;
- If both arguments are integers (Boolean, Byte, Character, Short, Integer, Long, or
  BigInteger), the result will be the wider type;
- If one argument is a real type and the other an integer type, the result will be the real type if the integer is narrower than "int"; BigDecimal if the integer is BigInteger;
  or the wider of the real type and Double otherwise.

<a id="language-guide--interpreting-objects-as-integers"></a>

### Interpreting Objects as Integers

Operators that work only on integers, like the bit-shifting operators, treat their arguments as numbers, except that BigDecimals and BigIntegers are operated on as
BigIntegers and all other kinds of numbers are operated on as Longs. For the BigInteger case, the result of these operators remains a BigInteger; for the
Long case, the result is expressed as the same type of the arguments, if it fits, or as a Long otherwise.

<a id="language-guide--interpreting-objects-as-collections"></a>

### Interpreting Objects as Collections

The projection and selection operators (e1.{e2} and e1.{?e2}), and the in operator, all treat one of their arguments as a collection and walk it. This is done
differently depending on the class of the argument:

- Java arrays are walked from front to back;
- Members of java.util.Collection are walked by walking their iterators;
- Members of java.util.Map are walked by walking iterators over their values;
- Members of java.util.Iterator and java.util.Enumeration are walked by iterating them;
- Members of java.lang.Number are "walked" by returning integers less than the given number starting with zero;
- All other objects are treated as singleton collections containing only themselves.

<a id="language-guide--appendix:-ognl-language-reference"></a>

## Appendix: OGNL Language Reference

This section has a fairly detailed treatment of OGNL's syntax and implementation. See below for a complete table of OGNL's operators, a section on how OGNL coerces objects
to various types, and a detailed description of OGNL's basic expressions.

<a id="language-guide--operators"></a>

### Operators

OGNL borrows most of Java's operators, and adds a few new ones. For the most part, OGNL's treatment of a given operator is the same as Java's, with the important caveat that
OGNL is essentially a typeless language. What that means is that every value in OGNL is a Java object, and OGNL attempts to coerce from each object a meaning appropriate to the
situation it is used in (see the section on coercion).

The following table lists OGNL operators in reverse precedence order. When more than one operator is listed in the same box, these operators have the same precedence and are evaluated in left-to-right order.

<table border="0" class="bodyTable"><caption>OGNL Operators - operators are listed in reverse precedence order</caption>
<thead>
<tr>
<th>Operator</th>
<th>getValue() Notes</th>
<th>setValue() Notes</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<div>

<span>e1, e2</span>

<p>Sequence operator</p>

</div>
</td>
<td>Both e1 and e2 are evaluated with the same
              source object, and the result of e2 is returned.</td>
<td>getValue is called on e1, and then
              setValue is called on e2.</td>
</tr>
<tr>
<td>
<div>

<span>e1 = e2</span>

<p>Assignment operator</p>

</div>
</td>
<td>getValue is called on e2, and then
              setValue is called on e1 with the result of e2 as the target object.</td>
<td>Cannot be the top-level expression for setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1 ? e2 : e3</span>

<p>Conditional operator</p>

</div>
</td>
<td>getValue is called on e1 and the result is interpreted as a boolean.
              getValue is then called on either e2 or e3, depending on whether the result of
              e1 was true or false respectively, and the result is returned.</td>
<td>getValue is called on e1, and then
              setValue is called on either e2 or e3.</td>
</tr>
<tr>
<td>
<div>

<span>e1 || e2,</span> <span>e1 or e2</span>

<p>Logical or operator</p>

</div>
</td>
<td>getValue is called on e1 and the result is
              interpreted as a boolean. If
              true, that result is returned; if false, getValue is called on e2 and its value is returned.</td>
<td>getValue is called on e1; if false, setValue is called on e2. Note that
              e1 being true prevents any further setting from taking
              place.</td>
</tr>
<tr>
<td>
<div>

<span>e1 &amp;&amp;
e2,</span> <span>e1
and e2</span>

<p>Logical and operator</p>

</div>
</td>
<td>getValue is called on e1 and the result is
              interpreted as a boolean. If
              false, that result is returned; if true, getValue is called
              on e2 and its value is returned.</td>
<td>getValue is called on e1; if true, setValue is called on e2. Note that
              e1 being false prevents any further setting from taking
              place.</td>
</tr>
<tr>
<td>
<div>

<span>e1 | e2,</span> <span>e1
bor e2</span>

<p>Bitwise or operator</p>

</div>
</td>
<td>e1 and e2 are interpreted as integers and the result is an integer.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1 ^ e2,</span> <span>e1
xor e2</span>

<p>Bitwise exclusive-or operator</p>

</div>
</td>
<td>e1 and e2 are interpreted as integers and the result is an integer.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1 &amp; e2,</span> <span>e1
band e2</span>

<p>Bitwise and operator</p>

</div>
</td>
<td>e1 and e2 are interpreted as integers and the result is an integer.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1 == e2,</span> <span>e1
eq e2</span>

<p>Equality test</p>

<span>e1 != e2,</span> <span>e1
neq e2</span>

<p>Inequality test</p>

</div>
</td>
<td>Equality is tested for as follows. If either value is null, they are
              equal if and only if both are null. If they are the same object or the equals()
              method says they are equal, they are equal. If they are both Numbers, they are equal if their values as
              double-precision floating point numbers are equal.
              Otherwise, they are not equal. These rules make numbers compare equal more readily than they would normally, if
              just using the equals method.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1 &lt; e2,</span> <span>e1
lt e2</span>

<p>Less than comparison</p>

<span>e1 &lt;= e2,</span> <span>e1
lte e2</span>

<p>Less than or equals comparison</p>

<span>e1 &gt; e2,</span> <span>e1
gt e2</span>

<p>Greater than comparison</p>

<span>e1 &gt;= e2,</span> <span>e1
gte e2</span>

<p>Greater than or equals comparison</p>

<span>e1 in e2</span>

<p>List membership comparison</p>

<span>e1 not in e2</span>

<p>List non-membership comparison</p>

</div>
</td>
<td>The ordering operators compare with compareTo() if their arguments
              are non-numeric and implement Comparable; otherwise, the arguments are interpreted
              as numbers and compared numerically. The in operator is not from Java; it tests for inclusion of e1 in e2,
              where e2 is interpreted as a collection. This test is not efficient: it iterates the collection. However, it
              uses the standard OGNL equality test.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1 &lt;&lt; e2,</span> <span>e1
shl e2</span>

<p>Bit shift left</p>

<span>e1 &gt;&gt; e2,</span> <span>e1
shr e2</span>

<p>Bit shift right</p>

<span>e1 &gt;&gt;&gt;
e2,</span> <span>e1
ushr e2</span>

<p>Logical shift right</p>

</div>
</td>
<td>e1 and e2 are interpreted as integers and the result is an integer.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1 + e2</span>

<p>Addition</p>

<span>e1 - e2</span>

<p>Subtraction</p>

</div>
</td>
<td>The plus operator concatenates strings if its arguments are non-numeric; otherwise it interprets its arguments as numbers and adds
              them. The minus operator always works on numbers.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>e1* e2</span>

<p>Multiplication</p>

<span>e1 / e2</span>

<p>Division</p>

<span>e1 % e2</span>

<p>Remainder</p>

</div>
</td>
<td>Multiplication, division, which interpret their arguments as numbers, and remainder, which interprets its arguments as integers.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

<span>+ e</span>

<p>Unary plus</p>

<span>- e</span>

<p>Unary minus</p>

<span>! e,</span>
<span>not e</span>

<p>Logical not</p>

<span>~ e</span>

<p>Bitwise not</p>

<span>e instanceof
class</span>

<p>Class membership</p>

</div>
</td>
<td>Unary plus is a no-op, it simply returns the value of its argument. Unary minus interprets its argument as a
              number. Logical not interprets its argument as a
              boolean. Bitwise not interprets its
              argument as an integer. The class argument to instanceof is the fully
              qualified name of a Java class.</td>
<td>Cannot be the top-level expression passed to setValue.</td>
</tr>
<tr>
<td>
<div>

e.method(args)

<p>Method call</p>

e.property

<p>Property</p>

e1[ e2 ]

<p>Index</p>

e1.{ e2
}

<p>Projection</p>

e1.{? e2
}

<p>Selection</p>

e1.(e2)

<p>Subexpression evaluation</p>

e1(e2)

<p>Expression evaluation</p>

</div>
</td>
<td>Generally speaking, navigation chains are evaluated by evaluating the first expression, then
              evaluating the second one with the result of the first as the source object.</td>
<td>Some of these forms can be passed as top-level expressions to setValue and others cannot.
              Only those chains that end in property references (e.property),
              indexes (e1[e2]), and subexpressions (e1.(e2)) can be; and
              expression evaluations can be as well. For the chains, getValue is called on the
              left-hand expression (e or e1), and then setValue is called on the rest with the result as the target object.</td>
</tr>
<tr>
<td>
<div>

constant

<p>Constant</p>

(
e )

<p>Parenthesized expression</p>

method(args)

<p>Method call</p>

property

<p>Property reference</p>

[ e ]

<p>Index reference</p>

{ e, ... }

<p>List creation</p>

#variable

<p>Context variable reference</p>

@class@method(args)

<p>Static method reference</p>

@class@field

<p>Static field reference</p>

new class(args)

<p>Constructor call</p>

new array-component-class[] { e, ... }

<p>Array creation</p>

#{ e1 : e2, ... }

<p>Map creation</p>

#@classname@{ e1 : e2, ... }

<p>Map creation with specific subclass</p>

:[ e ]

<p>Lambda expression definition</p>

</div>
</td>
<td>Basic expressions</td>
<td>Only property references (property), indexes ([e]), and variable references
              (#variable) can be passed as top-level
              expressions to setValue. For indexes, getValue is called on
              e, and then the result is used as the property "name" (which might be a String or any other
              kind of object) to set in the current target object. Variable and property
              references are set more directly.</td>
</tr>
</tbody>
</table>

---

<a id="developer-guide"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/developer-guide.html -->

<!-- page_index: 3 -->

<a id="developer-guide--introduction"></a>

## Introduction

OGNL as a language allows for the navigation of Java objects through a concise syntax that allows for specifying, where possible, symmetrically settable and gettable values. The language specifies a syntax that
attempts to provide as high a level of abstraction as possible for navigating object graphs; this usually means specifying paths through and to JavaBeans properties, collection indices, etc. rather than directly accessing property getters and
setters (collectively know as *accessors*).

The normal usage of OGNL is to embed the language inside of other constructs to provide a place for flexible binding of values from one place to another. An example of this is a web application where values need to be bound from a model
of some sort to data transfer objects that are operated on by a view. Another example is an XML configuration file wherein values are generated via expressions which are then bound to configured objects.

<a id="developer-guide--embedding-ognl"></a>

## Embedding OGNL

The org.apache.commons.ognl.Ognl class contains convenience methods for evaluating OGNL expressions. You can do this in two stages, parsing an expression into an internal form and then using that internal form
to either set or get the value of a property; or you can do it in a single stage, and get or set a property using the String form of the expression directly. It is more efficient to pre-compile the expression to it's parsed form, however, and this is the recommended usage.

OGNL expressions can be evaluated without any external context, or they can be provided with an execution environment that sets up custom extensions to modify the way that expressions are evaluated.

The following example illustrates how to encapsulate the parsing of an OGNL expression within an object so that execution will be more efficient. The class then takes an OgnlContext and a root object to
evaluate against.

```
import org.apache.commons.ognl.Ognl; import org.apache.commons.ognl.OgnlContext;
public class OgnlExpression {
private Object expression;
public OgnlExpression( String expressionString ) throws OgnlException {super(); expression = Ognl.parseExpression( expressionString );}
public Object getExpression() {return expression;}
public Object getValue( OgnlContext context, Object rootObject ) throws OgnlException {return Ognl.getValue( getExpression(), context, rootObject );}
public void setValue( OgnlContext context, Object rootObject, Object value ) throws OgnlException {Ognl.setValue(getExpression(), context, rootObject, value);}
}
```

<a id="developer-guide--extending-ognl"></a>

## Extending OGNL

OGNL expressions are not evaluated in a static environment, as Java programs are. Expressions are not compiled to bytecode at the expression level based on static class reachability. The same expression can have multiple paths
through an object graph depending upon the root object specified and the dynamic results of the navigation. Objects that are delegated to handle all of the access to properties of objects, elements of collections, methods of objects, resolution of class names to classes and converting between types are collectively known as *OGNL extensions*. The following chapters delve more deeply into these extensions and provide a roadmap as to how they are used
within OGNL to customize the dynamic runtime environment to suit the needs of the embedding program.

<a id="developer-guide--property-accessors"></a>

## Property Accessors

When navigating an OGNL expression many of the elements that are found are properties. Properties can be many things depending on the object being accessed. Most of the time these property names resolve to JavaBeans
properties that conform to the set/get pattern. Other objects (such as Map) access properties as keyed values. Regardless of access methodology the OGNL syntax remains the same. Under the hood, however, there are
PropertyAccessor objects that handle the conversion of property name to an actual access to an objects' properties.

```
public interface PropertyAccessor {
Object getProperty( Map context, Object target, Object name ) throws OgnlException;
void setProperty( Map context, Object target, Object name, Object value ) throws OgnlException;
}
```

You can set a property accessor on a class-by-class basis using OgnlRuntime.setPropertyAccessor(). There are default property accessors for Object (which uses JavaBeans patterns to extract
properties) and Map (which uses the property name as a key).

<a id="developer-guide--method-accessors"></a>

## Method Accessors

Method calls are another area where OGNL needs to do lookups for methods based on dynamic information. The MethodAccessor interface provides a hook into how OGNL calls a method. When a static or instance method is requested the
implementor of this interface is called to actually execute the method.

```
public interface MethodAccessor {
Object callStaticMethod( Map context, Class targetClass, String methodName, List args ) throws MethodFailedException;
Object callMethod( Map context, Object target, String methodName, List args ) throws MethodFailedException;
}
```

You can set a method accessor on a class-by-class basis using OgnlRuntime.setMethodAccessor(). The is a default method accessor for Object (which simply finds an appropriate method based
on method name and argument types and uses reflection to call the method).

<a id="developer-guide--elements-accessors"></a>

## Elements Accessors

Since iteration is a built-in function of OGNL and many objects support the idea of iterating over the contents of an object (i.e. the object.{ ... } syntax) OGNL provides a hook into how iteration is done. The
ElementsAccessor interface defines how iteration is done based on a source object. Simple examples could be a Collection elements accessor, which would simply

```
public interface ElementsAccessor
{

    Enumeration getElements( Object target )
        throws OgnlException;

}
```

You can set a method accessor on a class-by-class basis using OgnlRuntime.setElementsAccessor(). There are default elements accessors for Object (which returns an Enumeration
of itself as the only object), Map (which iterates over the values in the Map), and Collection (which uses the collection's iterator()). One clever use of
ElementsAccessors is the NumberElementsAccessor class which allows for generating numeric sequences from 0 to the target value. For example the expression (100).{ #this } will
generate a list of 100 integers ranged 0..99.

<a id="developer-guide--class-references"></a>

## Class References

In the sections on accessing static field and static methods it stated that classes must be full-specified in between the class reference specifier (@<classname>@<field|method>@).
This is not entirely true; the default ClassResolver simply looks up the name of the class and assumes that it is fully specified. The ClassResolver interface is included in the
OGNL context to perform lookup of classes when an expression is evaluated. This makes it possible to specify, for example, a list of imports that are specific to a particular setValue() or
getValue() context in order to look up classes. It also makes class references agreeably short because you don't have to full specify a class name.

```
public interface ClassResolver
{

    Class classForName( Map context, String className )
        throws ClassNotFoundException;

}
```

You can set a class resolver on a context basis using the Ognl methods addDefaultContext() and createDefaultContext().

<a id="developer-guide--type-conversion"></a>

## Type Conversion

When performing set operations on properties or calling methods it is often the case that the values you want to set have a different type from the expected type of the class. OGNL supports a context variable (set by
OgnlRuntime.setTypeConverter(Map context, TypeConverter typeConverter)) that will allow types to be converted from one to another. The default type converter that is uses is the ognl.DefaultTypeConverter, which will convert among numeric types (Integer, Long, Short, Double, Float, BigInteger, BigDecimal, and their primitive equivalents), string types (String, Character) and Boolean. Should you need specialized type conversion (one popular
example is in Servlets where you have a String[] from an HttpServletRequest.getParameters() and you want to set values with it in other objects; a custom type converter can be written (most likely
subclassing ognl.DefaultTypeConverter) to convert String[] to whatever is necessary.

```
public interface TypeConverter
{

    <T> T convertValue( Map context,
                                Object target,
                                Member member,
                                String propertyName,
                                Object value,
                                Class<T> toType );

}
```

Note that ognl.DefaultTypeConverter is much easier to subclass; it implements TypeConverter and calls it's own convertValue(Map context, Object value, Class toType)
method and already provides the numeric conversions. For example, the above converter (i.e. converting String[] to int[] for a list of identifier parameters in a request) implemented as a subclass
of org.apache.commons.ognl.DefaultTypeConverter:

```
HttpServletRequest request; Map context = Ognl.createDefaultContext( this );
/* Create an anonymous inner class to handle special conversion */ Ognl.setTypeConverter( context, new org.apache.commons.ognl.DefaultTypeConverter() {
public <T> convertValue( Map context, Object value, Class<T> toType ) {
T result = null;
if ( ( toType == int[].class ) && ( value instanceof String[].class ) ) {String  sa = (String[]) value; int[]   ia = new int[sa.length];
for ( int i = 0; i < sa.length; i++) {Integer cv;
cv = super.convertValue( context, sa[i], Integer.class ); ia[i] = cv.intValue();} result = (T) ia;} else {result = super.convertValue( context, value, toType );}
return result;} }); /* Setting values within this OGNL context will use the above-defined TypeConverter */ Ognl.setValue( "identifiers",context,this,request.getParameterValues( "identifier" ) );
```

<a id="developer-guide--member-access"></a>

## Member Access

Normally in Java the only members of a class (fields, methods) that can be accessed are the ones defined with public access. OGNL includes an interface that you can set globally (using OgnlContext.setMemberAccessManager())
that allows you to modify the runtime in Java 2 to allow access to private, protected and package protected fields and methods. Included in the OGNL package is the DefaultMemberAccess class. It
contains a constructor that allows you to selectively lower the protection on any private, protected or package protected members using the AccessibleObject interface in Java2. The default class can be subclasses to
select different objects for which accessibility is allowed.

```
public interface MemberAccess {
Object setup( Member member );
void restore( Member member, Object state );
boolean isAccessible( Member member );
}
```

<a id="developer-guide--null-handler"></a>

## Null Handler

When navigating a chain sometimes properties or methods will evaluate to null, causing subsequent properties or method calls to fail with NullPointerExceptions. Most of the time this behaviour is correct (as it is
with Java), but sometimes you want to be able to dynamically substitute another object in place of null. The NullHandler interface allows you to specify on a class-by-class basis how nulls are
handled within OGNL expressions. Implementing this interface allows you to intercept when methods return null and properties evaluate to null and allow you to substitute a new value. Since you are
given the source of the method or property a really clever implementor might write the property back to the object so that subsequent invocations do not return or evaluate to null.

```
public interface NullHandler {
Object nullMethodResult( Map context, Object target, String methodName, List args );
Object nullPropertyValue( Map context, Object target, Object property );
}
```

NullHandler implementors are registered with OGNL using the OgnlRuntime.setNullHandler() method.

<a id="developer-guide--other-api-features"></a>

## Other API features

<a id="developer-guide--tracing-evaluations"></a>

### Tracing Evaluations

As of OGNL 2.5.0 the OgnlContext object can automatically tracks evaluations of expressions. This tracking is kept in the OgnlContext as currentEvaluation during the
evaluation. After execution you can access the last evaluation through the lastEvaluation property of OgnlContext.

**Note**: The tracing feature is turned off by default. If you wish to turn it on there is a setTraceEvaluations() method on OgnlContext that you can call.

Any *method accessor*, *elements accessor*, *type converter*, *property accessor*
or *null handler* may find this useful to give context to the operation being performed. The Evaluation object is itself a tree and can be traversed up, down and left and right
through siblings to determine the exact circumstances of an evaluation. In addition the Evaluation object tracks the node that was performing the operation, the source object on which that operation was being
performed and the result of the operation. If an exception is thrown during execution the user can get the last evaluation's last descendent to find out exactly which subexpression caused the error. The execption is also tracked in
the Evaluation.

---

<a id="benchmark"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/benchmark.html -->

<!-- page_index: 4 -->

<a id="benchmark--benchmark-results-for-methods-in-class-org.apache.commons.ognl.performance.performancecommonsognltest"></a>

# Benchmark results for methods in class org.apache.commons.ognl.performance.PerformanceCommonsOgnlTest

- [Orientation](#benchmark)

Click on table headers to change the sorting order and redraw the chart.

- [Properties](#benchmark)

```
Run ID: 2
Run timestamp: 2013-03-01 19:25:05.747
JVM: 1.6.0_41-b02-445-11M4107
OS: x86_64
```

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/issue-tracking.html -->

<!-- page_index: 5 -->

<a id="issue-tracking--overview"></a>

## Overview

This project uses [JIRA](http://www.atlassian.com/software/jira) a J2EE-based, issue tracking and project management application.

<a id="issue-tracking--issue-tracking"></a>

## Issue Tracking

Issues, bugs, and feature requests should be submitted to the following issue tracking system for this project.

```
https://issues.apache.org/jira/browse/OGNL
```

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/project-info.html -->

<!-- page_index: 6 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | The Apache Commons OGNL library is a Java development framework for Object-Graph Navigation Language, plus other extras such as list projection and selection and lambda expressions. |
| [Project Summary](#project-summary) | This document lists other related information of this project |
| [Project Team](https://commons.apache.org/dormant/commons-ognl/team-list.html) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Repository](https://commons.apache.org/dormant/commons-ognl/source-repository.html) | This is a link to the online source repository that can be viewed via a web browser. |
| [Issue Tracking](#issue-tracking) | This is a link to the issue management system for this project. Issues (bugs, features, change requests) can be created and queried using this link. |
| [Mailing Lists](https://commons.apache.org/dormant/commons-ognl/mail-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependencies](https://commons.apache.org/dormant/commons-ognl/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Continuous Integration](#integration) | This is a link to the definitions of all continuous integration processes that builds and tests code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/dormant/commons-ognl/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="project-summary"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/project-summary.html -->

<!-- page_index: 7 -->

<a id="project-summary--project-summary"></a>

## Project Summary

<a id="project-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons OGNL - Object Graph Navigation Library |
| Description | The Apache Commons OGNL library is a Java development framework for Object-Graph Navigation Language, plus other extras such as list projection and selection and lambda expressions. |
| Homepage | <http://commons.apache.org/ognl/> |

<a id="project-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <http://www.apache.org/> |

<a id="project-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-ognl |
| Version | 4.0-SNAPSHOT |
| Type | jar |
| JDK Rev | 1.5 |

---

<a id="integration"></a>

<!-- source_url: https://commons.apache.org/dormant/commons-ognl/integration.html -->

<!-- page_index: 8 -->

<a id="integration--overview"></a>

## Overview

This project uses [Jenkins](http://jenkins-ci.org/).

<a id="integration--access"></a>

## Access

The following is a link to the continuous integration system used by the project.

```
https://builds.apache.org/job/ognl/
```

<a id="integration--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---
