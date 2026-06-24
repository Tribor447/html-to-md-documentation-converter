# HttpClient - HttpClient User Guide

## Navigation

- Overview
  - [Features](#features)
- User Guide
  - [Overview](#userguide)
  - [Authentication Guide](#authentication)
  - [Character Encodings](#charencodings)
  - [Cookies](#cookies)
  - [Exception Handling](#exception-handling)
  - [Logging Guide](#logging)
  - [Methods](#methods)
  - [Optimization Guide](#performance)
  - [Preference Architecture](#preference-api)
  - [Redirects Handling](#redirects)
  - [SSL Guide](#sslguide)
  - [Threading](#threading)
  - [Trouble Shooting](#troubleshooting)
  - [Tutorial](#tutorial)
- Project Documentation
  - [About](#index)
  - [Project Reports](#maven-reports)
    - [JavaDoc Report](#javadoc)
    - [JavaDoc Warnings Report](#javadoc-warnings-report)
    - [Metrics](#jdepend-report)
  - [Development Process](#development-process)

## Content

<a id="features"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/features.html -->

<!-- page_index: 1 -->

<a id="features--end-of-life"></a>

## End of life

The Commons HttpClient project is now end of life, and is no longer being developed.
It has been replaced by the [Apache HttpComponents](https://hc.apache.org/) project
in its [HttpClient](https://hc.apache.org/httpcomponents-client-ga) and [HttpCore](https://hc.apache.org/httpcomponents-core-ga/) modules, which offer better performance and more flexibility.

<a id="features--features"></a>

## Features

- Standards based, pure Java, implementation of HTTP versions 1.0 and 1.1
- Full implementation of all HTTP methods (GET, POST, PUT, DELETE,
  HEAD, OPTIONS, and TRACE) in an extensible OO framework.
- Supports encryption with HTTPS (HTTP over SSL) protocol.
- Granular non-standards configuration and tracking.
- Transparent connections through HTTP proxies.
- Tunneled HTTPS connections through HTTP proxies, via the CONNECT method.
- Transparent connections through SOCKS proxies (version 4 & 5) using native Java
  socket support.
- Authentication using Basic, Digest and the encrypting NTLM (NT Lan Manager) methods.
- Plug-in mechanism for custom authentication methods.
- Multi-Part form POST for uploading large files.
- Pluggable secure sockets implementations, making it easier to use third party solutions
- Connection management support for use in multi-threaded applications. Supports setting the
  maximum total connections as well as the maximum connections per host. Detects and closes
  stale connections.
- Automatic Cookie handling for reading Set-Cookie: headers from the server and sending
  them back out in a Cookie: header when appropriate.
- Plug-in mechanism for custom cookie policies.
- Request output streams to avoid buffering any content body by streaming
  directly to the socket to the server.
- Response input streams to efficiently read the response body by streaming
  directly from the socket to the server.
- Persistent connections using KeepAlive in HTTP/1.0 and persistance in HTTP/1.1
- Direct access to the response code and headers sent by the server.
- The ability to set connection timeouts.
- HttpMethods implement the Command Pattern to allow for parallel requests
  and efficient re-use of connections.
- Source code is freely available under the Apache Software License.

<a id="features--standards-compliance"></a>

## Standards Compliance

*HttpClient* implements the following specifications
endorsed by the Internet Engineering Task Force (IETF)
and the internet at large:

- [RFC1945](http://www.ietf.org/rfc/rfc1945.txt "External Link")
  Hypertext Transfer Protocol -- HTTP/1.0
- [RFC2616](http://www.ietf.org/rfc/rfc2616.txt "External Link")
  Hypertext Transfer Protocol -- HTTP/1.1
- [RFC2617](http://www.ietf.org/rfc/rfc2617.txt "External Link")
  HTTP Authentication: Basic and Digest Access Authentication
- [RFC2109](http://www.ietf.org/rfc/rfc2109.txt "External Link")
  HTTP State Management Mechanism (Cookies)
- [RFC2396](http://www.ietf.org/rfc/rfc2396.txt "External Link")
  Uniform Resource Identifiers (URI): Generic Syntax
- [RFC1867](http://www.ietf.org/rfc/rfc1867.txt "External Link")
  Form-based File Upload in HTML

<a id="features--product-comparision"></a>

## Product Comparision

The HTTP protocol is so ubiquitous on the internet that you can find other
client side implementations written in Java. The jdk has the HttpUrlConnection
which is limited and in many ways flawed. This is one reason why Jakarta, and
others free and commercial vendors, have implemented independant HTTP clients.
To help you choose the right solution, one of those commercial vendors, Oakland Software, has a fair
[product comparison](http://www.oaklandsoftware.com/product_16.html#compare "External Link").

---

<a id="userguide"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/userguide.html -->

<!-- page_index: 2 -->

<a id="userguide--end-of-life"></a>

## End of life

The Commons HttpClient project is now end of life, and is no longer being developed.
It has been replaced by the [Apache HttpComponents](https://hc.apache.org/) project
in its [HttpClient](https://hc.apache.org/httpcomponents-client-ga) and [HttpCore](https://hc.apache.org/httpcomponents-core-ga/) modules, which offer better performance and more flexibility.

<a id="userguide--user-guide"></a>

## User Guide

The HttpClient user guide is designed to help developers use
HttpClient in their applications. While the concept of a user guide
being for developers may seem strange, the term developer is
already in use for people helping to develop HttpClient.

If you are new to HttpClient, make sure to work through the
[Tutorial](#tutorial) and have a look at the
[Sample Code](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link").
Before reporting problems, read about
[Trouble Shooting](#troubleshooting)

<a id="userguide--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [Authentication Guide](#authentication) | This document describes the authentication schemes supported by HttpClient and how to use them. |
| [Character Encodings](#charencodings) | Guidelines for correctly detecting the character encoding to use when sending and receiving data with HttpClient. |
| [Redirects Handling](#redirects) | Provide sample code for custom redirects handling. |
| [Exception Handling](#exception-handling) | This document outlines common types of errors that the users may encounter and describes the exception handling framework used by HttpClient. |
| [Logging Guide](#logging) | This document describes the logging mechanism used by HttpClient and how to control what it outputs. |
| [Methods](#methods) | This document describes the various methods that are provided by HttpClient and how to use them. |
| [Optimization Guide](#performance) | This document outlines HttpClient performance optimization techniques. |
| [Preference Architecture](#preference-api) | This document explains the preference architecture used by HttpClient and enumerates standard HttpClient parameters. |
| [Sample Code](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link") | This is a link to the sample code for using HttpClient that is stored in the Subversion repository and is available in source releases of HttpClient. |
| [Trouble Shooting](#troubleshooting) | This document provides hints and tips for debugging problems with HttpClient. |
| [Tutorial](#tutorial) | This document provides a simple introductory tutorial for new users of HttpClient. |

---

<a id="authentication"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/authentication.html -->

<!-- page_index: 3 -->

<a id="authentication--introduction"></a>

## Introduction

HttpClient supports three different types of http authentication schemes:
Basic, Digest and NTLM. These can be used to authenticate with http servers
or proxies.

<a id="authentication--contents"></a>

### Contents

- [Server Authentication](#authentication--server_authentication)
  - [Preemptive Authentication](#authentication--preemptive_authentication)
  - [Security aspects of server authentication](#authentication--security_aspects_of_server_authentication)
- [Proxy Authentication](#authentication--proxy_authentication)
- [Authentication Schemes](#authentication--authentication_schemes)
  - [Basic](#authentication--basic)
  - [Digest](#authentication--digest)
  - [NTLM](#authentication--ntlm)
  - [Alternate authentication](#authentication--alternate_authentication)
  - [Custom authentication scheme](#authentication--custom_authentication_scheme)
- [Examples](#authentication--examples)
- [Known limitations and problems](#authentication--known_limitations_and_problems)
- [Troubleshooting](#authentication--troubleshooting)

<a id="authentication--server-authentication"></a>

## Server Authentication

HttpClient handles authenticating with servers almost transparently, the only thing a developer must do is actually provide the login
credentials. These credentials are stored in the HttpState instance
and can be set or retrieved using the `setCredentials(AuthScope authscope, Credentials cred)` and `getCredentials(AuthScope authscope)`
methods.

The automatic authorization built in to HttpClient can be disabled
with the method `setDoAuthentication(boolean doAuthentication)`
in the HttpMethod class. The change only affects that method instance.

<a id="authentication--preemptive-authentication"></a>

### Preemptive Authentication

Preemptive authentication can be enabled within HttpClient. In this
mode HttpClient will send the basic authentication response even before
the server gives an unauthorized response in certain situations, thus reducing the overhead
of making the connection. To enable this use the following:

```
client.getParams().setAuthenticationPreemptive(true);
```

Preemptive authentication mode also requires default Credentials to be set
for the target or proxy host against which preemptive authentication is to be
attempted. Failure to provide default credentials will render the preemptive
authentication mode ineffective.

```
Credentials defaultcreds = new UsernamePasswordCredentials("username", "password");
client.getState().setCredentials(new AuthScope("myhost", 80, AuthScope.ANY_REALM), defaultcreds);
```

The preemptive authentication in HttpClient conforms to rfc2617:

> A client SHOULD assume that all paths at or deeper than the depth
> of the last symbolic element in the path field of the Request-URI also
> are within the protection space specified by the Basic realm value
> of the current challenge. A client MAY preemptively send the
> corresponding Authorization header with requests for resources in
> that space without receipt of another challenge from the server.
> Similarly, when a client sends a request to a proxy, it may reuse
> a userid and password in the Proxy-Authorization header field without
> receiving another challenge from the proxy server.

<a id="authentication--security-aspects-of-server-authentication"></a>

### Security aspects of server authentication

Use default credentials with caution when developing applications
that may need to communicate with untrusted web sites or web applications. When
preemptive authentication is activated or credentials are not explicitly given
for a specific authentication realm and host HttpClient will use default credentials
to try to authenticate with the target site. If you want to avoid sending sensitive
credentials to an untrusted site, narrow the credentials scope as much as possible:
always specify the host and, when known, the realm the credentials are intended for.

Setting credentials with AuthScope.ANY authentication scope (`null` value
for host and/or realm) is highly discouraged in production applications. Doing this
will result in the credentials being sent for all authentication attempts (all
requests in the case of preemptive authentication). Use of this setting should be
limited to debugging only.

```
// To be avoided unless in debug mode
Credentials defaultcreds = new UsernamePasswordCredentials("username", "password");
client.getState().setCredentials(AuthScope.ANY, defaultcreds);
```

<a id="authentication--proxy-authentication"></a>

## Proxy Authentication

Proxy authentication in HttpClient is almost identical to server
authentication with the exception that the credentials for each are
stored independantly. So for proxy authentication you must use
`setProxyCredentials(AuthScope authscope, Credentials cred)` and
`getProxyCredentials(AuthScope authscope)`.

<a id="authentication--authentication-schemes"></a>

## Authentication Schemes

The following authentication schemes are supported by HttpClient.

<a id="authentication--basic"></a>

### Basic

Basic authentication is the original and most compatible authentication
scheme for HTTP. Unfortunately, it is also the least secure as it sends
the username and password unencrypted to the server. Basic authentication
requires an instance of UsernamePasswordCredentials (which NTCredentials
extends) to be available, either for the specific realm specified by the
server or as the default credentials.

<a id="authentication--digest"></a>

### Digest

Digest authentication was added in the HTTP 1.1 protocol and while
not being as widely supported as Basic authentication there is a great
deal of support for it. Digest authentication is significantly more
secure than basic authentication as it never transfers the actual
password across the network, but instead uses it to encrypt a "nonce"
value sent from the server.

Digest authentication requires an instance of
UsernamePasswordCredentials (which NTCredentials extends) to be
available either for the specific realm specified by the server or as
the default credentials.

<a id="authentication--ntlm"></a>

### NTLM

NTLM is the most complex of the authentication protocols supported
by HttpClient. It is a proprietary protocol designed by Microsoft
with no publicly available specification. Early version of NTLM were
less secure than Digest authentication due to faults in the design, however these were fixed in a service pack for Windows NT 4 and the
protocol is now considered more secure than Digest authentication.

NTLM authentication requires an instance of NTCredentials be
available for the *domain name* of the server or the default
credentials. Note that since NTLM does not use the notion of realms
HttpClient uses the domain name of the server as the name of the realm.
Also note that the username provided to the NTCredentials should not
be prefixed with the domain - ie: "adrian" is correct whereas
"DOMAIN\adrian" is not correct.

There are some significant differences in the way that NTLM works
compared with basic and digest authentication. These differences
are generally handled by HttpClient, however having an
understanding of these differences can help avoid problems when using
NTLM authentication.

1. NTLM authentication works almost exactly the same as any other form of
   authentication in terms of the HttpClient API. The only difference is that
   you need to supply 'NTCredentials' instead of 'UsernamePasswordCredentials'
   (NTCredentials actually extends UsernamePasswordCredentials so you can use
   NTCredentials right throughout your application if need be).
2. The realm for NTLM authentication is the domain name of the computer
   being connected to, this can be troublesome as servers often have
   multiple domain names that refer to them. Only the domain name
   that HttpClient connects to (as specified by the HostConfiguration)
   is used to look up the credentials.
   It is generally advised that while initially testing NTLM
   authentication, you pass the realm in as null which is used as
   the default.
3. NTLM authenticates a connection and not a request, so you need to
   authenticate every time a new connection is made and keeping the connection
   open during authentication is vital. Due to this, NTLM cannot
   be used to authenticate with both a proxy and the server, nor can
   NTLM be used with HTTP 1.0 connections or servers that do not
   support HTTP keep-alives.

For a detailed explanation of how NTLM authentication works, please see
[http://davenport.sourceforge.net/ntlm.html](http://davenport.sourceforge.net/ntlm.html "External Link").

<a id="authentication--alternate-authentication"></a>

### Alternate authentication

Some servers support multiple schemes for authenticating users.
Given that only one scheme may be used at a time for authenticating, HttpClient
must choose which scheme to use. To accompish this, HttpClient uses an order of
preference to select the correct authentication scheme. By default
this order is: NTLM, Digest, Basic.

In certain cases it may be desirable to change this default. The
default preference of the authentication schemes may be altered using the
'http.auth.scheme-priority' parameter. The parameter value is expected to be a List
of Strings containing names of authentication schemes in descending order of
preference.

```
HttpClient client = new HttpClient();
List authPrefs = new ArrayList(2);
authPrefs.add(AuthPolicy.DIGEST);
authPrefs.add(AuthPolicy.BASIC);
// This will exclude the NTLM authentication scheme
client.getParams().setParameter(AuthPolicy.AUTH_SCHEME_PRIORITY, authPrefs);
```

<a id="authentication--custom-authentication-scheme"></a>

### Custom authentication scheme

HttpClient natively supports basic, digest, and NTLM authentication. It also contains
a mechanism to plugin additional custom authentication schemes via the
[AuthScheme](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/auth/AuthScheme.html) interface.
The following steps are required to make use of a custom authentication scheme.

1. Implement the `AuthScheme` interface.
2. Register the custom `AuthScheme` with [AuthPolicy.registerAuthScheme()](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/auth/AuthPolicy.html#registerAuthScheme(java.lang.String, java.lang.Class)).
3. Include the custom `AuthScheme` in the AuthPolicy.AUTH\_SCHEME\_PRIORITY preference
   (see the [Alternate authentication](#authentication--alternate_authentication) section).

<a id="authentication--examples"></a>

## Examples

There are a number of authentication examples in the [example directory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link"), including:

- [Basic authentication](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/BasicAuthenticationExample.java?view=markup "External Link")
- [Custom authentication](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/CustomAuthenticationExample.java?view=markup "External Link")
- [Interactive authentication](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/InteractiveAuthenticationExample.java?view=markup "External Link")

<a id="authentication--known-limitations-and-problems"></a>

## Known limitations and problems

1. **Authentication schemes that rely on persistent connection state do not work on Sun's JVMs
   below 1.4 if SSL is used**

   For details please refer to the [Known
   limitations and problems](#sslguide--known-limitations-and-problems) section of the [SSL Guide](#sslguide)

   **Workaround:** Disable stale connection check or upgrade to Java 1.4 or above.
2. **Cannot authenticate with Microsoft IIS using NTLM authentication scheme**

   NT Lan Manager (NTLM) authentication is a proprietary, closed challenge/response authentication
   protocol for Microsoft Windows. Only some details about NTLM protocol are available through
   reverse engineering. HttpClient provides limited support for what is known as NTLMv1, the early
   version of the NTLM protocol. HttpClient does not support NTLMv2 at all.

   **Workaround:** Disable NTLMv2. For details refer to this Microsoft Support
   [Article](http://support.microsoft.com/default.aspx?scid=KB;en-us;239869 "External Link")

<a id="authentication--troubleshooting"></a>

## Troubleshooting

Some authentication schemes may use cryptographic algorithms. It is recommended to include the
[Java Cryptography Extension](http://java.sun.com/products/jce/ "New Window") in
your runtime environment prior to JDK 1.4. Also note that you must register the JCE
implementation manually as HttpClient will not do so automatically. For instance to
register the Sun JCE implementation, you should execute the following code before attempting
to use HttpClient.

```

String secProviderName = "com.sun.crypto.provider.SunJCE");
java.security.Provider secProvider = 
    (java.security.Provider)Class.forName(secProviderName).newInstance();
Security.addProvider(secProvider);
	  
```

---

<a id="charencodings"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/charencodings.html -->

<!-- page_index: 4 -->

<a id="charencodings--introduction"></a>

## Introduction

This document provides an overview of how HttpClient handles character
encodings and how to use HttpClient in an encoding safe way. There are
three main sections:
[HTTP Headers](#charencodings--http_headers), [Request/Response Body](#charencodings--request_response_body) and
[URLs](#charencodings--urls).

<a id="charencodings--http-headers"></a>

## HTTP Headers

The headers of a HTTP request or response must be in US-ASCII format.
It is not possible to use non US-ASCII characters in the header of a
request or response. Generally this is not an issue however, because the
HTTP headers are designed to facilite the transfer of data rather than to
actually transfer the data itself.

One exception however are cookies. Since cookies are transfered as HTTP Headers
they are confined to the US-ASCII character set. See the Cookie Guide
for more information.

<a id="charencodings--request-response-body"></a>

## Request/Response Body

The request or response body can be any encoding, but by default is
ISO-8859-1. The encoding may be specified in the
Content-Type header, for example:
> Content-Type: text/html; charset=UTF-8

In this case the application should be careful to use UTF-8 encoding
when converting the body to a String or some characters may be corrupt.
You can set the content type header for a request with the
`addRequestHeader` method in each method and retrieve the
encoding for the response body with the `getResponseCharSet`
method.

If the response is known to be a String, you can use the
`getResponseBodyAsString` method which will automatically use
the encoding specified in the Content-Type header or
ISO-8859-1 if no charset is specified.

Note that some document types, such as HTML and XML allow the author
to specify the content type of the file. In this case, you should
consult the appropriate standards regarding how to resovle any conflicts
in the reported charsets.

<a id="charencodings--urls"></a>

## URLs

The standard for URLs ([RFC1738](http://www.ietf.org/rfc/rfc1738.txt "External Link")) explictly
states that URLs may only contain graphic printable characters of the
US-ASCII coded character set and is defined in terms of octets.
The octets `80-FF` hexadecimal are not used in US-ASCII and the octets
`OO-1F` hexadecimal represent control characters; characters in these
ranges must be encoded.

Characters which cannot be represented by an 8-bit ASCII code, can not
be used in an URL as there is no way to reliably encode them (the
encoding scheme for URLs is based off of octets). Despite this, some
servers do support varying means of encoding double byte characters in
URLs, the most common technique seems to be to use UTF-8 encoding and
encode each octet separately even if a pair of octets represents one
character. This however, is not specified by the standard and is highly
prone to error, so it is recommended that URLs be restricted to the 8-bit
ASCII range.

---

<a id="cookies"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/cookies.html -->

<!-- page_index: 5 -->

<a id="cookies--introduction"></a>

## Introduction

HttpClient supports automatic management of cookies, including
allowing the server to set cookies and automatically return them to the
server when required. It is also possible to manually set cookies to be
sent to the server.

Unfortunately, there are several at times conflicting standards for
handling Cookies: the Netscape Cookie draft, RFC2109, RFC2965 and a large
number of vendor specific implementations that are compliant with neither
specification. To deal with this, HttpClient provides policy driven cookie
management. This guide will explain how to use the different cookie
specifications and identify some of the common problems people have when
using Cookies and HttpClient.

<a id="cookies--supported-specifications"></a>

## Supported Specifications

The following cookie specifications are supported by HttpClient 3.1.

<a id="cookies--rfc2109"></a>

### RFC2109

RFC2109 is the first official cookie specification released by the W3C.
Theoretically, all servers that handle version 1 cookies should use this
specification and as such this specification is used by default within
HttpClient.

Unfortunately, many servers either incorrectly implement this
standard or are still using the Netscape draft so occasionally this
specification is too strict. If this is the case, you should switch to
the compatibility specification as described below.

RFC2109 is available at
[http://www.w3.org/Protocols/rfc2109/rfc2109.txt](http://www.w3.org/Protocols/rfc2109/rfc2109.txt "External Link")

RFC2109 is the default cookie policy used by HttpClient.

<a id="cookies--rfc2965"></a>

### RFC2965

RFC2965 defines cookie version 2 and attempts to address the
shortcomings of the RFC2109 regarding cookie version 1.
RFC2965 is intended to eventually supersede RFC2109.

Servers that send RFC2965 cookies will use the Set-Cookie2 header
in addition to the Set-Cookie header. RFC2965 cookies are port
sensitive.

RFC2965 is available at
[http://www.w3.org/Protocols/rfc2965/rfc2965.txt](http://www.w3.org/Protocols/rfc2965/rfc2965.txt "External Link")

<a id="cookies--netscape-draft"></a>

### Netscape Draft

The Netscape draft is the original cookie specification which formed
the basis for RFC2109. Despite this it has some significant
differences with RFC2109 and thus may be required for compatibility
with some servers.

The Netscape cookie draft is available at [http://wp.netscape.com/newsref/std/cookie\_spec.html](http://wp.netscape.com/newsref/std/cookie_spec.html "External Link")

<a id="cookies--browser-compatibility"></a>

### Browser Compatibility

The compatibility specification is designed to be compatible with as
many different servers as possible even if they are not completely
standards compliant. If you are encountering problems with parsing
cookies, you should probably try using this specification.

There are many web sites with badly written CGI scripts that only work
when all cookies are put into one request header. It is advisable to
set [http.protocol.single-cookie-header](#preference-api)
parameter to `true` for maximum compatibility.

<a id="cookies--ignore-cookies"></a>

### Ignore Cookies

This cookie specification ignores all cookies. It should be used to
prevent HttpClient from accepting and sending cookies.

<a id="cookies--specifying-the-specification"></a>

## Specifying the Specification

There are two ways to specify which cookie specification should be
used, either for each `HttpMethod` instance using the
`HttpMethodParams`, or by setting the default value on
`CookiePolicy`.

<a id="cookies--per-httpmethod"></a>

### Per HttpMethod

In most cases, the best way to specify the cookie spec to use is the
`setCookiePolicy(String policy)` method on
`HttpMethodParams`. The value of `policy`
must be one of the values registered with `CookiePolicy.registerCookieSpec()`.

```

        HttpMethod method = new GetMethod();
        method.getParams().setCookiePolicy(CookiePolicy.RFC_2109);
        
```

<a id="cookies--manual-handling-of-cookies"></a>

## Manual handling of cookies

The cookie management API of HttpClient can co-exist with the manual
cookie handling. One can manually set request `Cookie`
headers or process response `Set-Cookie` headers in addition
or instead of the automatic cookie management

```

        HttpMethod method = new GetMethod();
        method.getParams().setCookiePolicy(CookiePolicy.IGNORE_COOKIES);
        method.setRequestHeader("Cookie", "special-cookie=value");
        
```

<a id="cookies--common-problems"></a>

## Common Problems

The most common problems encountered with parsing cookies is due to
non-compliant servers. In these cases, switching to the compatibility
cookie specification usually solves the problem.

<a id="cookies--encoding-issues"></a>

## Encoding Issues

Since cookies are transfered as HTTP Headers they are confined to
the US-ASCII character set. Other characters will be lost or
mangeled. Cookies are typically set and read by the same server, so
a custom scheme for escaping non-ASCII characters can be used, for
instance the well-established URL encoding scheme. If cookies are
used to transfer data between server and client both parties must
agree on the escaping scheme used in a custom way. The HttpClient
cookie implementation provides no special means to handle non-ASCII
characters nor does it issue warnings.

---

<a id="exception-handling"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/exception-handling.html -->

<!-- page_index: 6 -->

<a id="exception-handling--exception-handling"></a>

## Exception handling

There are two main type of exceptions that the user of HttpClient may encounter
when executing HTTP methods:

1. **transport exceptions**
2. **protocol exceptions**

Not all of these exceptions will be propagated to the user in regular HttpClient use.
Exceptions handled internally by HttpClient are marked below as **INTERNAL**.

- [Transport exceptions](#exception-handling--transport_exceptions)
- [Protocol exceptions](#exception-handling--protocol_exceptions)
- [HTTP transport safety](#exception-handling--http_transport_safety)
- [Automatic exception recovery](#exception-handling--automatic_exception_recovery)
- [Custom exception handler](#exception-handling--custom_exception_handler)

<a id="exception-handling--transport-exceptions"></a>

## Transport exceptions

Transport exceptions are those caused by input/output failures such as an unreliable connection
or an inability to complete the execution of an HTTP method within the given time constraint
(socket timeout). Generally transport exceptions are non-fatal and may be recovered from by
retrying the failed method. However, special care must be taken when recovering from
exceptions in non-idempotent methods (refer to [HTTP transport safety](#exception-handling--http_transport_safety)
for details).

<a id="exception-handling--java.io.ioexception"></a>

### java.io.IOException

Generic transport exceptions in HttpClient are represented by the standard Java
java.io.IOException class or its sub classes such as java.net.SocketException and
java.net.InterruptedIOException.

In addition to standard input/output exception classes HttpClient defines several custom transport
exceptions that convey HttpClient specific information.

<a id="exception-handling--org.apache.commons.httpclient.nohttpresponseexception"></a>

### org.apache.commons.httpclient.NoHttpResponseException

```

java.io.IOException
  +- org.apache.commons.httpclient.NoHttpResponseException
```

In some circumstances, usually when under heavy load, the web server may be able to receive
requests but unable to process them. A lack of sufficient resources like worker threads is a good
example. This may cause the server to drop the connection to the client
without giving any response. HttpClient throws NoHttpResponseException when it encounters
such a condition. In most cases it is safe to retry a method that failed with
NoHttpResponseException.

<a id="exception-handling--org.apache.commons.httpclient.connecttimeoutexception"></a>

### org.apache.commons.httpclient.ConnectTimeoutException

```

java.io.IOException
  +- java.io.InterruptedIOException
    +- org.apache.commons.httpclient.ConnectTimeoutException
```

This exception signals that HttpClient is unable to establish a connection with the target
server or proxy server within the given period of time.

<a id="exception-handling--org.apache.commons.httpclient.connectionpooltimeoutexception"></a>

### org.apache.commons.httpclient.ConnectionPoolTimeoutException

```

java.io.IOException
  +- java.io.InterruptedIOException
    +- org.apache.commons.httpclient.ConnectTimeoutException
      +- org.apache.commons.httpclient.ConnectionPoolTimeoutException
```

This exception can only occur when using the multithreaded connection manager. The exception
signals that the connection manager fails to obtain a free connection from the connection pool
within the given period of time.

<a id="exception-handling--org.apache.commons.httpclient.httprecoverableexception"></a>

### org.apache.commons.httpclient.HttpRecoverableException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.HttpRecoverableException
```

Deprecated and no longer thrown any of the standard HttpClient classes.

<a id="exception-handling--protocol-exceptions"></a>

## Protocol exceptions

Protocol exceptions generally indicate logical errors caused by a mismatch between the client
and the server (web server or proxy server) in their interpretation of the HTTP specification.
Usually protocol exceptions cannot be recovered from without making adjustments to either
the client request or the server. Some aspects of the HTTP specification allow for different, at times conflicting, interpretations. HttpClient can be configured to support different degrees
of HTTP specification compliance varying from very lenient to very strict.

<a id="exception-handling--org.apache.commons.httpclient.httpexception"></a>

### org.apache.commons.httpclient.HttpException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
```

HttpException represents an abstract logical error in HttpClient. Generally this kind of exception
cannot be automatically recovered from.

<a id="exception-handling--org.apache.commons.httpclient.protocolexception"></a>

### org.apache.commons.httpclient.ProtocolException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
```

ProtocolException signals a violation of the HTTP specification. It is important to note that HTTP
proxies and HTTP servers can have different level of HTTP specification compliance. It may be
possible to recover from some HTTP protocol exceptions by configuring HttpClient to be more
lenient about non-fatal protocol violations.

<a id="exception-handling--org.apache.commons.httpclient.auth.malformedchallengeexception"></a>

### org.apache.commons.httpclient.auth.MalformedChallengeException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.MalformedChallengeException
```

**INTERNAL**

MalformedChallengeException signals that an authentication challenge is in some way invalid or
illegal in the given authentication context.

<a id="exception-handling--org.apache.commons.httpclient.auth.authenticationexception"></a>

### org.apache.commons.httpclient.auth.AuthenticationException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
```

**INTERNAL**

AuthenticationException signals a failure in the authentication process. Usually authentication
exceptions are handled internally when executing HTTP methods and are not propagated to the
caller.

<a id="exception-handling--org.apache.commons.httpclient.auth.authchallengeexception"></a>

### org.apache.commons.httpclient.auth.AuthChallengeException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
        +- org.apache.commons.httpclient.auth.AuthChallengeException
```

**INTERNAL**

AuthenticationException is thrown when HttpClient is unable to respond to any of the authentication
challenges sent by the server.

<a id="exception-handling--org.apache.commons.httpclient.auth.credentialsnotavailableexception"></a>

### org.apache.commons.httpclient.auth.CredentialsNotAvailableException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
        +- org.apache.commons.httpclient.auth.CredentialsNotAvailableException
```

**INTERNAL**

CredentialsNotAvailableException indicates that credentials required to respond to the authentication
challenge are not available.

<a id="exception-handling--org.apache.commons.httpclient.auth.invalidcredentialsexception"></a>

### org.apache.commons.httpclient.auth.InvalidCredentialsException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.auth.AuthenticationException
        +- org.apache.commons.httpclient.auth.InvalidCredentialsException
```

**INTERNAL**

InvalidCredentialsException indicates that the credentials used to respond to the authentication
challenge have been rejected by the server.

<a id="exception-handling--org.apache.commons.httpclient.cookie.malformedcookieexception"></a>

### org.apache.commons.httpclient.cookie.MalformedCookieException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.cookie.MalformedCookieException
```

**INTERNAL**

MalformedCookieException signals that the cookie is in some way invalid or illegal in the given
HTTP session context.

There are several cookie specifications that are often incompatible. Thus the validity of
a cookie is established within a context of a specific cookie specification used to parse
and validate the cookie header(s) sent by the server. If the application needs to process cookies
differently from the commonly used cookie specifications, it may choose to provide a
custom cookie policy or extend the existing one. Please see [cookies](#cookies)
for more details.

<a id="exception-handling--org.apache.commons.httpclient.redirectexception"></a>

### org.apache.commons.httpclient.RedirectException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.ProtocolException
      +- org.apache.commons.httpclient.RedirectException
```

RedirectException signals violation of the HTTP specification caused by an invalid
redirect response. If the application that uses HttpClient needs to be more lenient
about redirect responses, it may choose to disable automatic redirect processing and implement
a custom redirect strategy.

<a id="exception-handling--org.apache.commons.httpclient.uriexception"></a>

### org.apache.commons.httpclient.URIException

```

java.io.IOException
  +- org.apache.commons.httpclient.HttpException
    +- org.apache.commons.httpclient.URIException
```

URIException is thrown when the request URI violates the URI specification.

<a id="exception-handling--http-transport-safety"></a>

## HTTP transport safety

It is important to understand that the HTTP protocol is not well suited for all types of applications.
HTTP is a simple request/response oriented protocol which was initially designed to support static
or dynamically generated content retrieval. It has never been intended to support transactional
operations. For instance, the HTTP server will consider its part of the contract fulfilled if it
succeeds in receiving and processing the request, generating a response and sending a status code back
to the client. The server will make no attempts to roll back the transaction if the client fails to
receive the response in its entirety due to a read timeout, a request cancellation or a system crash.
If the client decides to retry the same request, the server will inevitably end up executing the same
transaction more than once. In some cases this may lead to application data corruption or inconsistent
application state.

Even though HTTP has never been designed to support transactional processing, it can still be used
as a transport protocol for mission critical applications provided certain conditions are met. To
ensure HTTP transport layer safety the system must ensure the idempotency of HTTP methods on the
application layer.

<a id="exception-handling--idempotent-methods"></a>

### Idempotent methods

HTTP/1.1 specification defines idempotent method as

> Methods can also have the property of "idempotence" in that (aside from error or expiration
> issues) the side-effects of N > 0 identical requests is the same as for a single request.

In other words the application ought to ensure that it is prepared to deal with the
implications of multiple execution of the same method. This can be achieved, for instance, by providing a unique transaction id and by other means of avoiding execution of the same
logical operation.

Please note that this problem is not specific to HttpClient. Browser based applications
are subject to exactly the same issues related to HTTP methods non-idempotency.

<a id="exception-handling--automatic-exception-recovery"></a>

## Automatic exception recovery

By default HttpClient attempts to automatically recover from exceptions. The default
auto-recovery mechanism is limited to just a few exceptions that are known to be safe.

HttpClient will make no attempt to recover from any logical or HTTP protocol error (those derived
from HttpException class).

HttpClient will automatically retry up to 5 times those methods that fail with a transport exception
while the HTTP request is still being transmitted to the target server (i.e. the request has
not been fully transmitted to the server).

HttpClient will automatically retry up to 5 times those methods that have been fully transmitted to
the server, but the server failed to respond with an HTTP status code (the server simply drops the
connection without sending anything back). In this case it is assumed that the request has not been
processed by the server and the application state has not changed. If this assumption may not hold
true for the web server your application is targeting it is highly recommended to provide a custom
exception handler.

<a id="exception-handling--custom-exception-handler"></a>

## Custom exception handler

In order to enable a custom exception recovery mechanism one should provide an implementation
of the [HttpMethodRetryHandler](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HttpMethodRetryHandler.html) interface.

```

HttpClient client = new HttpClient();

HttpMethodRetryHandler myretryhandler = new HttpMethodRetryHandler() {
    public boolean retryMethod(
        final HttpMethod method, 
        final IOException exception, 
        int executionCount) {
        if (executionCount >= 5) {
            // Do not retry if over max retry count
            return false;
        }
        if (exception instanceof NoHttpResponseException) {
            // Retry if the server dropped connection on us
            return true;
        }
        if (!method.isRequestSent()) {
            // Retry if the request has not been sent fully or
            // if it's OK to retry methods that have been sent
            return true;
        }
        // otherwise do not retry
        return false;
    }
};
        
GetMethod httpget = new GetMethod("http://www.whatever.com/");
httpget.getParams().
    setParameter(HttpMethodParams.RETRY_HANDLER, myretryhandler);
try {
    client.executeMethod(httpget);
    System.out.println(httpget.getStatusLine().toString());
} finally {
    httpget.releaseConnection();
}
```

---

<a id="logging"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/logging.html -->

<!-- page_index: 7 -->

<a id="logging--logging-practices"></a>

## Logging Practices

Being a library HttpClient is not to dictate which logging framework
the user has to use. Therefore *HttpClient* utilizes the logging
interface provided by the
[Commons Logging](http://commons.apache.org/logging/ "External Link") package. *Commons Logging* provides
a simple and generalized
[log interface](http://commons.apache.org/logging/commons-logging-1.0.4/docs/apidocs/ "External Link") to various logging packages. By using
*Commons Logging*, *HttpClient* can be configured
for a variety of different logging behaviours. That means the user will have
to make a choice which logging framework to use. By default *Commons Logging*
supports the following logging frameworks:

- [Log4J](http://logging.apache.org/log4j/docs/index.html "External Link")
- [java.util.logging](http://java.sun.com/j2se/1.4.2/docs/api/java/util/logging/package-summary.html "External Link")
- [SimpleLog](http://commons.apache.org/logging/commons-logging-1.0.4/docs/apidocs/org/apache/commons/logging/impl/SimpleLog.html "External Link") (internal to *Commons Logging*)

By implementing some simple interfaces *Commons Logging* can be extended to support
basically any other custom logging framework.
*Commons Logging* tries to automatically discover the logging framework to use. If it
fails to select the expected one, you must configure *Commons Logging* by hand. Please
refer to the *Commons Logging* documentation for more information.

*HttpClient* performs two different kinds of logging: the standard
context logging used within each class, and wire logging.

<a id="logging--context-logging"></a>

### Context Logging

Context logging contains information about the internal operation
of HttpClient as it performs HTTP requests. Each class has its own
log named according to the class's fully qualified name. For example
the class `HttpClient` has a log named
`org.apache.commons.httpclient.HttpClient`. Since all classes
follow this convention it is possible to configure context logging for
all classes using the single log named `org.apache.commons.httpclient`.

<a id="logging--wire-logging"></a>

### Wire Logging

The wire log is used to log all data transmitted to and from servers when
executing HTTP requests. This log should only be enabled to debug problems, as it will produce an extremely large amount of log data, some of it in binary
format.

Because the content of HTTP requests is usually less important for debugging
than the HTTP headers, these two types of data have been separated into
different wire logs. The content log is `httpclient.wire.content`
and the header log is `httpclient.wire.header`.

<a id="logging--configuration-examples"></a>

## Configuration Examples

*Commons Logging* can delegate to a variety of loggers for processing
the actual output. Below are configuration examples for *Commons Logging*,
*Log4j* and *java.util.logging*.

<a id="logging--commons-logging-examples"></a>

### Commons Logging Examples

*Commons Logging* comes with a basic logger called
`SimpleLog`. This logger writes all logged messages to
`System.err`. The following examples show how to configure
*Commons Logging* via system properties to use `SimpleLog`.

**Note:** The system properties must be set before a reference to any
*Commons Logging* class is made.

Enable header wire + context logging - **Best for Debugging**
> System.setProperty("org.apache.commons.logging.Log", "org.apache.commons.logging.impl.SimpleLog");
> System.setProperty("org.apache.commons.logging.simplelog.showdatetime", "true");
> System.setProperty("org.apache.commons.logging.simplelog.log.httpclient.wire.header", "debug");
> System.setProperty("org.apache.commons.logging.simplelog.log.org.apache.commons.httpclient", "debug");

Enable full wire(header and content) + context logging
> System.setProperty("org.apache.commons.logging.Log", "org.apache.commons.logging.impl.SimpleLog");
> System.setProperty("org.apache.commons.logging.simplelog.showdatetime", "true");
> System.setProperty("org.apache.commons.logging.simplelog.log.httpclient.wire", "debug");
> System.setProperty("org.apache.commons.logging.simplelog.log.org.apache.commons.httpclient", "debug");

Enable just context logging
> System.setProperty("org.apache.commons.logging.Log", "org.apache.commons.logging.impl.SimpleLog");
> System.setProperty("org.apache.commons.logging.simplelog.showdatetime", "true");
> System.setProperty("org.apache.commons.logging.simplelog.log.org.apache.commons.httpclient", "debug");

<a id="logging--log4j-examples"></a>

### Log4j Examples

The simplest way to configure [Log4j](http://logging.apache.org/log4j/ "External Link")
is via a *log4j.properties* file. *Log4j* will automatically
read and configure itself using a file named *log4j.properties* when
it's present at the root of the application classpath. Below are some
*Log4j* configuration examples.

**Note:** *Log4j* is not included in the *HttpClient* distribution.

Enable header wire + context logging - **Best for Debugging**
> log4j.rootLogger=INFO, stdout
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n
> log4j.logger.httpclient.wire.header=DEBUG
> log4j.logger.org.apache.commons.httpclient=DEBUG

Enable full wire(header and content) + context logging
> log4j.rootLogger=INFO, stdout
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n
> log4j.logger.httpclient.wire=DEBUG
> log4j.logger.org.apache.commons.httpclient=DEBUG

Log wire to file + context logging
> log4j.rootLogger=INFO
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n
> log4j.appender.F=org.apache.log4j.FileAppender
> log4j.appender.F.File=wire.log
> log4j.appender.F.layout=org.apache.log4j.PatternLayout
> log4j.appender.F.layout.ConversionPattern =%5p [%c] %m%n
> log4j.logger.httpclient.wire=DEBUG, F
> log4j.logger.org.apache.commons.httpclient=DEBUG, stdout

Enable just context logging
> log4j.rootLogger=INFO, stdout
> log4j.appender.stdout=org.apache.log4j.ConsoleAppender
> log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
> log4j.appender.stdout.layout.ConversionPattern=%5p [%c] %m%n
> log4j.logger.org.apache.commons.httpclient=DEBUG

Note that the default configuration for Log4J is very
inefficient as it causes all the logging information to be
generated but not actually sent anywhere. The Log4J manual is the
best reference for how to configure Log4J. It is available at [http://logging.apache.org/log4j/docs/manual.html](http://logging.apache.org/log4j/docs/manual.html "External Link")

<a id="logging--java.util.logging-examples"></a>

### java.util.logging Examples

Since JDK 1.4 there has been a package
[java.util.logging](http://java.sun.com/j2se/1.4.2/docs/api/java/util/logging/package-summary.html "External Link") that provides a
logging framework similar to *Log4J*. By default it reads a config file from
`$JAVA_HOME/jre/lib/logging.properties` which looks like this
(comments stripped):
> handlers=java.util.logging.ConsoleHandler
> .level=INFO
> java.util.logging.FileHandler.pattern = %h/java%u.log
> java.util.logging.FileHandler.limit = 50000
> java.util.logging.FileHandler.count = 1
> java.util.logging.FileHandler.formatter = java.util.logging.XMLFormatter
> java.util.logging.ConsoleHandler.level = INFO
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
> com.xyz.foo.level = SEVERE

To customize logging a custom `logging.properties` file should be created
in the project directory. The location of this file must be passed to the JVM as a
system property. This can be done on the command line like so:
> $JAVA\_HOME/java -Djava.util.logging.config.file=$HOME/myapp/logging.properties
> -classpath $HOME/myapp/target/classes com.myapp.Main

Alternatively
[LogManager#readConfiguration(InputStream)](http://java.sun.com/j2se/1.4.2/docs/api/java/util/logging/LogManager.html#readConfiguration(java.io.InputStream) "External Link") can be used to pass it the desired
configuration.

Enable header wire + context logging - **Best for Debugging**
> .level=INFO
> handlers=java.util.logging.ConsoleHandler
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
> httpclient.wire.header.level=FINEST
> org.apache.commons.httpclient.level=FINEST

Enable full wire(header and content) + context logging
> .level=INFO
> handlers=java.util.logging.ConsoleHandler
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
> httpclient.wire.level=FINEST
> org.apache.commons.httpclient.level=FINEST

Enable just context logging
> .level=INFO
> handlers=java.util.logging.ConsoleHandler
> java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
> org.apache.commons.httpclient.level=FINEST

More detailed information is available from the
[Java Logging documentation](http://java.sun.com/j2se/1.4.2/docs/guide/util/logging/overview.html "External Link").

---

<a id="methods"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/methods.html -->

<!-- page_index: 8 -->

<a id="methods--introduction"></a>

## Introduction

These documents provide a brief introduction to using the methods
provided by *HttpClient*. The information here does not cover all the
possible options, but covers enough of the basics to get you up and
running. For more information on the available options, refer to the [API Reference](https://hc.apache.org/httpclient-legacy/apidocs/index.html).

The examples on the following pages are not complete and are only used
to highlight the important features that are unique to each method. For
complete examples, please refer to the [sample
code](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/ "External Link").

<a id="methods--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [Options](https://hc.apache.org/httpclient-legacy/methods/options.html) | The OPTIONS method represents a request for information about the communication options available. |
| [Get](https://hc.apache.org/httpclient-legacy/methods/get.html) | The GET method means retrieve whatever information is identified by the requested URL. Also refer to the [tutorial](#tutorial). |
| [Head](https://hc.apache.org/httpclient-legacy/methods/head.html) | The HEAD method is identical to GET except that the server *must not* return a message-body in the response. This method can be used for obtaining metainformation about the document implied by the request without transferring the document itself. |
| [Post](https://hc.apache.org/httpclient-legacy/methods/post.html) | The POST method is used to request that the origin server accept the data enclosed in the request as a new child of the request URL. POST is designed to allow a uniform method to cover a variety of functions such as appending to a database, providing data to a data-handling process or posting to a message board. |
| [Multipart Post](https://hc.apache.org/httpclient-legacy/methods/multipartpost.html) | The multipart post method is identical to the POST method, except that the request body is separated into multiple parts. This method is generally used when uploading files to the server. |
| [Put](https://hc.apache.org/httpclient-legacy/methods/put.html) | The PUT method requests that the enclosed document be stored under the supplied URL. This method is generally disabled on publicly available servers because it is generally undesireable to allow clients to put new files on the server or to replace existing files. |
| [Delete](https://hc.apache.org/httpclient-legacy/methods/delete.html) | The DELETE method requests that the server delete the resource identified by the request URL. This method is generally disabled on publicly available servers because it is generally undesireable to allow clients to delete files on the server. |
| [Trace](https://hc.apache.org/httpclient-legacy/methods/trace.html) | The TRACE method is used to invoke a remote, application-layer loop-back of the request message. This allows the client to see what is being received at the other end of the request chain and use that data for testing or diagnostic information. |

---

<a id="performance"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/performance.html -->

<!-- page_index: 9 -->

<a id="performance--introduction"></a>

## Introduction

By default HttpClient is configured to provide maximum reliability and standards
compliance rather than raw performance. There are several configuration options and
optimization techniques which can significantly improve the performance of HttpClient.
This document outlines various techniques to achieve maximum HttpClient performance.

<a id="performance--contents"></a>

### Contents

- [Reuse the HttpClient instance](#performance--reuse_of_httpclient_instance)
- [Connection persistence](#performance--connection_persistence)
- [Concurrent execution of HTTP methods](#performance--concurrent_execution_of_http_methods)
- [Request/Response entity streaming](#performance--request_response_entity_streaming)
- [Expect-continue handshake](#performance--expect-continue_handshake)
- [Stale connection check](#performance--stale_connection_check)
- [Cookie processing](#performance--cookie_processing)

<a id="performance--reuse-the-httpclient-instance"></a>

## Reuse the HttpClient instance

Generally it is recommended to have a single instance of HttpClient per communication
component or even per application. However, if the application makes use of HttpClient
only very infrequently, and keeping an idle instance of HttpClient in memory is not warranted, it is highly recommended to explicitly [shut down](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html#shutdown()) the multithreaded connection manager prior to disposing
the HttpClient instance. This will ensure proper closure of all HTTP connections in the
connection pool.

<a id="performance--connection-persistence"></a>

## Connection persistence

HttpClient always does its best to reuse connections. Connection persistence is enabled
by default and requires no configuration. Under some situations this can lead to leaked
connections and therefore lost resources. The easiest way to disable connection persistence
is to provide or extend a connection manager that force-closes connections
upon release in the [releaseConnection](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HttpConnectionManager.html#releaseConnection(org.apache.commons.httpclient.HttpConnection)) method.

<a id="performance--concurrent-execution-of-http-methods"></a>

## Concurrent execution of HTTP methods

If the application logic allows for execution of multiple HTTP requests concurrently
(e.g. multiple requests against various sites, or multiple requests representing
different user identities), the use of a dedicated thread per HTTP session can result in a
significant performance gain. HttpClient is fully thread-safe when used with a thread-safe
connection manager such as [MultiThreadedHttpConnectionManager](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html). Please note that each respective thread of execution
must have a local instance of HttpMethod and can have a local instance of HttpState or/and
HostConfiguration to represent a specific host configuration and conversational state. At the
same time the HttpClient instance and connection manager should be shared among all threads
for maximum efficiency.

For details on using multiple threads with HttpClient please refer to the [HttpClient Threading Guide](#threading).

<a id="performance--request-response-entity-streaming"></a>

## Request/Response entity streaming

HttpClient is capable of efficient request/response body streaming. Large entities may be submitted
or received without being buffered in memory. This is especially critical if multiple HTTP
methods may be executed concurrently. While there are convenience methods to deal with entities such as
strings or byte arrays, their use is discouraged. Unless used carefully they can easily lead to
out of memory conditions, since they imply buffering of the complete entity in memory.

**Response streaming:** It is recommended to consume the HTTP response body as a stream of
bytes/characters using HttpMethod#getResponseBodyAsStream method. The use of HttpMethod#getResponseBody and
HttpMethod#getResponseBodyAsString are strongly discouraged.

```

  HttpClient httpclient = new HttpClient();
  GetMethod httpget = new GetMethod("http://www.myhost.com/");
  try {
    httpclient.executeMethod(httpget);
    Reader reader = new InputStreamReader(
            httpget.getResponseBodyAsStream(), httpget.getResponseCharSet()); 
    // consume the response entity
  } finally {
    httpget.releaseConnection();
  }
```

**Request streaming:** The main difficulty encountered when streaming request bodies is that
some entity enclosing methods need to be retried due to an authentication failure or an I/O failure.
Obviously non-buffered entities cannot be reread and resubmitted. The recommended approach is to create a custom
[RequestEntity](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/methods/RequestEntity.html) capable of
reconstructing the underlying input stream.

```
public class FileRequestEntity implements RequestEntity {
private File file = null;
public FileRequestEntity(File file) {super(); this.file = file;}
public boolean isRepeatable() {return true;}
public String getContentType() {return "text/plain; charset=UTF-8";}
public void writeRequest(OutputStream out) throws IOException {InputStream in = new FileInputStream(this.file); try {int l; byte[] buffer = new byte[1024]; while ((l = in.read(buffer)) != -1) {out.write(buffer, 0, l);} } finally {in.close();}}
public long getContentLength() {return file.length();}}
File myfile = new File("myfile.txt"); PostMethod httppost = new PostMethod("/stuff"); httppost.setRequestEntity(new FileRequestEntity(myfile));
```

<a id="performance--expect-continue-handshake"></a>

## Expect-continue handshake

The purpose of the HTTP 100 (Continue) status is to allow a client sending a request entity to
determine if the target server is willing to accept the request (based on the
request headers) before the client sends the request entity. It is highly inefficient for the client
to send the request entity if the server will reject the request without looking at the body.
Authentication failures are the most common reason for the request to be rejected based on the request
headers alone. Therefore, use of the 'Expect-continue' handshake is especially recommended with
those target servers that require HTTP authentication. For proxied requests caution
must be taken as older HTTP/1.0 proxies may be unable to correctly handle the 'Expect-continue'
handshake.

See the [http.protocol.expect-continue](#preference-api) parameter documentation
for more information.

<a id="performance--stale-connection-check"></a>

## Stale connection check

HTTP specification permits both the client and the server to terminate a persistent (keep-alive)
connection at any time without notice to the counterpart, thus rendering the connection invalid
or stale. By default HttpClient performs a check, just prior to executing a request, to determine if the
active connection is stale. The cost of this operation is about 15-30 ms, depending on the JRE used.
Disabling stale connection check may result in slight performance improvement, especially for small
payload responses, at the risk of getting an I/O error when executing a request over a connection
that has been closed at the server side.

See the [http.connection.stalecheck](#preference-api) parameter documentation for more
information.

<a id="performance--cookie-processing"></a>

## Cookie processing

If an application, such as web spider, does not need to maintain conversational state with the target
server, a small performance gain can made by disabling cookie processing. For details
on cookie processing please to the [HttpClient Cookies Guide](#cookies).

---

<a id="preference-api"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/preference-api.html -->

<!-- page_index: 10 -->

<a id="preference-api--table-of-contents"></a>

## Table of contents

- [HttpClient preference architecture](#preference-api--httpclient_preference_architecture)
  - [HTTP parameters](#preference-api--http_parameters)
  - [HTTP parameter hierarchy](#preference-api--http_parameter_hierarchy)
- [Supported parameters](#preference-api--supported_parameters)
  - [HTTP method parameters](#preference-api--http_method_parameters)
  - [HTTP connection parameters](#preference-api--http_connection_parameters)
  - [HTTP connection manager parameters](#preference-api--http_connection_manager_parameters)
  - [HTTP client parameters](#preference-api--http_client_parameters)

<a id="preference-api--httpclient-preference-architecture"></a>

## HttpClient preference architecture

Quality and extent of the [`HTTP/1.0`](http://www.ietf.org/rfc/rfc1945.txt "External Link") and [`HTTP/1.1`](http://www.ietf.org/rfc/rfc2616.txt "External Link") spec compliance vary significantly among commonly
used HTTP agents and HTTP servers. That requires of HttpClient to be able to

- mimic (mis-)behavior of widely used web browsers;
- support flexible and configurable level of leniency toward non-critical
  protocol violations especially in those gray areas of the specification
  subject to different, at times conflicting, interpretations;
- apply a different set of parameters to individual HTTP methods, hosts, or
  client instances using common interface;

<a id="preference-api--http-parameters"></a>

### HTTP parameters

As of version 3 HttpClient sports a new preference API based on
[HttpParams](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/params/HttpParams.html) interface. All major components of the HttpClient toolkit
(agents, host configurations, methods, connections, connection managers)
contain a collection of HTTP parameters, which determine the runtime behavior
of those components.

```

HttpClient httpclient = new HttpClient();
HttpVersion ver = (HttpVersion)httpclient.getParams().getParameter("http.protocol.version");
```

In a nutshell HTTP parameters is a collection of name/object pairs that can be linked
with other collections to form a hierarchy. If a particular parameter value has not been
explicitly defined in the collection itself, its value will be drawn from the upper level
collection of parameters.

```

HttpClient httpclient = new HttpClient();
httpclient.getParams().setParameter("http.protocol.version", HttpVersion.HTTP_1_1);
httpclient.getParams().setParameter("http.socket.timeout", new Integer(1000));
httpclient.getParams().setParameter("http.protocol.content-charset", "UTF-8");

HostConfiguration hostconfig = new HostConfiguration();
hostconfig.setHost("www.yahoo.com");
hostconfig.getParams().setParameter("http.protocol.version", HttpVersion.HTTP_1_0);
		
GetMethod httpget = new GetMethod("/");
httpget.getParams().setParameter("http.socket.timeout", new Integer(5000));
		
try {
  // Internally the parameter collections will be linked together
  // by performing the following operations: 
  // hostconfig.getParams().setDefaults(httpclient.getParams());
  // httpget.getParams().setDefaults(hostconfig.getParams());
  httpclient.executeMethod(hostconfig, httpget);
  System.out.println(httpget.getParams().getParameter("http.protocol.version"));
  System.out.println(httpget.getParams().getParameter("http.socket.timeout"));
  System.out.println(httpget.getParams().getParameter("http.protocol.content-charset"));
} finally {
  httpget.releaseConnection();
}
```

The code above will produce the following output:

```

HTTP/1.0
5000
UTF-8
```

When resolving a parameter HttpClient uses the following algorithm:

- start parameter lookup from the lowest level at which this parameter applies
- if the parameter is undefined at the current level, defer its resolution to the
  next level up in the hierarchy
- return parameter value from the lowest level in the hierarchy the parameter
  defined at
- return null if the parameter is undefined

This architecture enables the users to define generic parameters at a higher
level (for instance, at the agent level or host level) and selectively override
specific parameters at a lower level (for instance, at the method level). Whenever
a parameter is not explicitly defined at a given level, the defaults of the upper
levels will apply.

<a id="preference-api--http-parameter-hierarchy"></a>

### HTTP parameter hierarchy

Presently HttpClient provides the following parameter hierarchy:

```

global--+                            | DefaultHttpParams
        |                            |
      client                         | HttpClient
        |                            |
        +-- connection manager       | HttpConnectionManager
        |     |                      |
        |     +-- connection         | HttpConnection
        |                            |
        +-- host                     | HostConfiguration
              |                      |
              +-- method             | HttpMethod
```

<a id="preference-api--supported-parameters"></a>

## Supported parameters

<a id="preference-api--http-method-parameters"></a>

### HTTP method parameters

Applicable at the following levels: **global** -> **client** -> **host** -> **method**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.useragent | String | The content of the `User-Agent` header used by the HTTP methods. | official release name, e.g. "Jakarta Commons-HttpClient/3.0" |
| http.protocol.version | [HttpVersion](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HttpVersion.html) | The HTTP protocol version used per default by the HTTP methods. | [`HttpVersion.HTTP_1_1`](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HttpVersion.html#HTTP_1_1) |
| http.protocol.unambiguous-statusline | Boolean | Defines whether HTTP methods should reject ambiguous HTTP status line. | `<undefined>` |
| http.protocol.single-cookie-header | Boolean | Defines whether cookies should be put on a single response header. | `<undefined>` |
| http.protocol.strict-transfer-encoding | Boolean | Defines whether responses with an invalid `Transfer-Encoding` header should be rejected. | `<undefined>` |
| http.protocol.reject-head-body | Boolean | Defines whether the content body sent in response to `HEAD` request should be rejected. | `<undefined>` |
| http.protocol.head-body-timeout | Integer | Sets period of time in milliseconds to wait for a content body sent in response to `HEAD` response from a non-compliant server. If the parameter is not set or set to `-1` non-compliant response body check is disabled. | `<undefined>` |
| http.protocol.expect-continue | Boolean | Activates 'Expect: 100-Continue' handshake for the entity enclosing methods. The 'Expect: 100-Continue' handshake allows a client that is sending a request message with a request body to determine if the origin server is willing to accept the request (based on the request headers) before the client sends the request body. The use of the 'Expect: 100-continue' handshake can result in noticeable performance improvement for entity enclosing requests (such as `POST` and `PUT`) that require the target server's authentication. 'Expect: 100-continue' handshake should be used with caution, as it may cause problems with HTTP servers and proxies that do not support `HTTP/1.1` protocol. `<undefined>` |  |
| http.protocol.credential-charset | String | The charset to be used when encoding credentials. If not defined then the value of the 'http.protocol.element-charset' should be used. | `<undefined>` |
| http.protocol.element-charset | String | The charset to be used for encoding/decoding HTTP protocol elements (status line and headers). | 'US-ASCII' |
| http.protocol.content-charset | String | The charset to be used for encoding content body. | 'ISO-8859-1' |
| http.protocol.cookie-policy | String | The cookie policy to be used for cookie management. | [`CookiePolicy.RFC_2109`](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/cookie/CookiePolicy.html#RFC_2109) |
| http.protocol.warn-extra-input | Boolean | Defines HttpClient's behavior when a response provides more bytes than expected (specified with `Content-Length` header, for example). Such surplus data makes the HTTP connection unreliable for keep-alive requests, as malicious response data (faked headers etc.) can lead to undesired results on the next request using that connection. If this parameter is set to `true`, any detection of extra input data will generate a warning in the log. | `<undefined>` |
| http.protocol.status-line-garbage-limit | Integer | Defines the maximum number of ignorable lines before we expect a HTTP response's status code. With HTTP/1.1 persistent connections, the problem arises that broken scripts could return a wrong `Content-Length` (there are more bytes sent than specified). Unfortunately, in some cases, this is not possible after the bad response, but only before the next one. So, HttpClient must be able to skip those surplus lines this way. Set this to `0` to disallow any garbage/empty lines before the status line. To specify no limit, use `Integer#MAX_VALUE`. | `<undefined>` |
| http.socket.timeout | Integer | Sets the socket timeout (`SO_TIMEOUT`) in milliseconds to be used when executing the method. A timeout value of zero is interpreted as an infinite timeout. | `<undefined>` |
| http.method.retry-handler | [HttpMethodRetryHandler](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HttpMethodRetryHandler.html) | The method retry handler used for retrying failed methods. For details see the [Exception handling guide](#exception-handling--custom-exception-handler). | [default implementation](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html) |
| http.dateparser.patterns | [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link") | Date patterns used for parsing. The patterns are stored in a [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link") and must be compatible with [SimpleDateFormat](http://java.sun.com/j2se/1.4.2/docs/api/java/text/SimpleDateFormat.html "External Link"). | 'EEE, dd MMM yyyy HH:mm:ss zzz', 'EEEE, dd-MMM-yy HH:mm:ss zzz', 'EEE MMM d HH:mm:ss yyyy', 'EEE, dd-MMM-yyyy HH:mm:ss z', 'EEE, dd-MMM-yyyy HH-mm-ss z', 'EEE, dd MMM yy HH:mm:ss z', 'EEE dd-MMM-yyyy HH:mm:ss z', 'EEE dd MMM yyyy HH:mm:ss z', 'EEE dd-MMM-yyyy HH-mm-ss z', 'EEE dd-MMM-yy HH:mm:ss z', 'EEE dd MMM yy HH:mm:ss z', 'EEE,dd-MMM-yy HH:mm:ss z', 'EEE,dd-MMM-yyyy HH:mm:ss z', 'EEE, dd-MM-yyyy HH:mm:ss z' |
| http.method.response.buffer.warnlimit | Integer | The maximum buffered response size (in bytes) that triggers no warning. Buffered responses exceeding this size will trigger a warning in the log. If not set, the limit is 1 MB. | `<undefined>` |
| http.method.multipart.boundary | String | The multipart boundary string to use in conjunction with the [MultipartRequestEntity](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/params/MultipartRequestEntity.html). When not set a random value will be generated for each request. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

<a id="preference-api--http-connection-parameters"></a>

### HTTP connection parameters

Applicable at the following levels: **global** -> **client** -> **connection manager** ->
**connection**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.socket.timeout | Integer | The default socket timeout (`SO_TIMEOUT`) in milliseconds which is the timeout for waiting for data. A timeout value of zero is interpreted as an infinite timeout. This value is used when no socket timeout is set in the HTTP method parameters. | `<undefined>` |
| http.tcp.nodelay | Boolean | Determines whether Nagle's algorithm is to be used. The Nagle's algorithm tries to conserve bandwidth by minimizing the number of segments that are sent. When applications wish to decrease network latency and increase performance, they can disable Nagle's algorithm (by enabling `TCP_NODELAY`). Data will be sent earlier, at the cost of an increase in bandwidth consumption and number of packets. | `<undefined>` |
| http.socket.sendbuffer | Integer | The value to set on [Socket.setSendBufferSize(int)](http://java.sun.com/j2se/1.4.2/docs/api/java/net/Socket.html#setSendBufferSize(int) "External Link"). This value is a suggestion to the kernel from the application about the size of buffers to use for the data to be sent over the socket. | `<undefined>` |
| http.socket.receivebuffer | Integer | The value to set on [Socket.setReceiveBufferSize(int)](http://java.sun.com/j2se/1.4.2/docs/api/java/net/Socket.html#setReceiveBufferSize(int) "External Link"). This value is a suggestion to the kernel from the application about the size of buffers to use for the data to be received over the socket. | `<undefined>` |
| http.socket.linger | Integer | The linger time (`SO_LINGER`) in seconds. This option disables/enables immediate return from a close() of a TCP Socket. Enabling this option with a non-zero Integer timeout means that a close() will block pending the transmission and acknowledgement of all data written to the peer, at which point the socket is closed gracefully. Value `0` implies that the option is disabled. Value `-1` implies that the JRE default is used. | `<undefined>` |
| http.connection.timeout | Integer | The timeout until a connection is established. A value of zero means the timeout is not used. | `<undefined>` |
| http.connection.stalecheck | Boolean | Determines whether stale connection check is to be used. Disabling stale connection check may result in slight performance improvement at the risk of getting an I/O error when executing a request over a connection that has been closed at the server side. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

<a id="preference-api--http-connection-manager-parameters"></a>

### HTTP connection manager parameters

Applicable at the following levels: **global** -> **client** -> **connection manager**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.connection-manager.max-per-host | [Map](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Map.html "External Link") | Defines the maximum number of connections allowed per host configuration. These values only apply to the number of connections from a particular instance of HttpConnectionManager. This parameter expects a value of type [`Map`](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Map.html "External Link"). The value should map instances of [`HostConfiguration`](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HostConfiguration.html) to [`Integer`](http://java.sun.com/j2se/1.4.2/docs/api/java/lang/Integer.html "External Link")s. The default value can be specified using [`ANY_HOST_CONFIGURATION`](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HostConfiguration.html#ANY_HOST_CONFIGURATION). | `<undefined>` |
| http.connection-manager.max-total | Integer | Defines the maximum number of connections allowed overall. This value only applies to the number of connections from a particular instance of HttpConnectionManager. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

<a id="preference-api--host-configuration-parameters"></a>

### Host configuration parameters

Applicable at the following levels: **global** -> **client** -> **host**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.default-headers | [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link") | The request headers to be sent per default with each request. This parameter expects a value of type [Collection](http://java.sun.com/j2se/1.4.2/docs/api/java/util/Collection.html "External Link"). The collection is expected to contain [HTTP headers](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/Header.html) | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

<a id="preference-api--http-client-parameters"></a>

### HTTP client parameters

Applicable at the following levels: **global** -> **client**

| Name | Type | Description | Default |
| --- | --- | --- | --- |
| http.connection-manager.timeout | Long | The timeout in milliseconds used when retrieving an HTTP connection from the HTTP connection manager. 0 means to wait indefinitely. | `<undefined>` |
| http.connection-manager.class | Class | The default HTTP connection manager class. | [`SimpleHttpConnectionManager`](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/SimpleHttpConnectionManager.html) class |
| http.authentication.preemptive | Boolean | Defines whether authentication should be attempted preemptively. See authentication guide. | `<undefined>` |
| http.protocol.reject-relative-redirect | Boolean | Defines whether relative redirects should be rejected. Although redirects are supposed to be absolute it is common internet practice to use relative URLs. | `<undefined>` |
| http.protocol.max-redirects | Integer | Defines the maximum number of redirects to be followed. The limit on number of redirects is intended to prevent infinite loops. | `<undefined>` |
| http.protocol.allow-circular-redirects | Boolean | Defines whether circular redirects (redirects to the same location) should be allowed. The HTTP spec is not sufficiently clear whether circular redirects are permitted, therefore optionally they can be enabled. | `<undefined>` |

Whenever a parameter is left undefined (no value is explicitly set anywhere in
the parameter hierarchy) HttpClient will use its best judgment to pick up a value. This
default behavior is likely to provide the best compatibility with widely used HTTP servers.

---

<a id="redirects"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/redirects.html -->

<!-- page_index: 11 -->

<a id="redirects--introduction"></a>

## Introduction

This document provides a brief guide to custom handling of redirects
with *HttpClient*.

There are a few types of redirect that HttpClient can't handle
automatically either because they require user interaction, or they are
outside of the scope of HttpClient (these status codes are listed [below](#redirects--special-redirect-codes)), or due to internal
limitations. Currently HttpClient is unable to automatically handle
redirects of entity enclosing methods such as POST and
PUT. There can also be situations when manual processing
of redirects is desired due to specific application requirements.

<a id="redirects--handling-redirects-manually"></a>

## Handling redirects manually

All response codes between 300 and 399 inclusive are redirect responses
of some form. The most common redirect response codes are:

- 301 Moved Permanently.
  `HttpStatus.SC_MOVED_PERMANENTLY`
- 302 Moved Temporarily.
  `HttpStatus.SC_MOVED_TEMPORARILY`
- 303 See Other. `HttpStatus.SC_SEE_OTHER`
- 307 Temporary Redirect.
  `HttpStatus.SC_TEMPORARY_REDIRECT`

**Note:** there are a number of response codes in the 3xx range
which do not simply indicate a different URI to send the request to.
These response codes are listed [below](#redirects--special-redirect-codes) and the manner they are
handled will be application specific.

When your application receives one of the "simple" redirect responses, it should extract the new URL from the HttpMethod object and retry
downloading from that URL.
Additionally, it is usually a good idea to limit the number of
redirects that will be followed in case the redirects form a recursive
loop.

The URL to connect to can be extracted from the Location
header.

```

        String redirectLocation;
        Header locationHeader = method.getResponseHeader("location");
        if (locationHeader != null) {
            redirectLocation = locationHeader.getValue();
        } else {
            // The response is invalid and did not provide the new location for
            // the resource.  Report an error or possibly handle the response
            // like a 404 Not Found error.
        }
      
```

Once you have determined the new location, you can reattempt the
connection as normal. See the [Tutorial](#tutorial) for
more information on this.

<a id="redirects--special-redirect-codes"></a>

## Special Redirect Codes

The HTTP specification defines a number of somewhat unusual redirect
response codes that will likely need to be handled in a different manner
to the codes above. In particular these are:

- 300 Multiple Choices.
  `HttpStatus.SC_MULTIPLE_CHOICES`

  There are multiple choices available for the redirection. A
  preferred redirect URI may be specified in the location header, however
  generally it is expected that the user will be given the choice of
  which URI to be redirected to. It is however permissible to simply
  select one of the available choices arbitrarily.
- 304 Not Modified.
  `HttpStatus.SC_NOT_MODIFIED`

  The resource has not been modified since it was last requested. You
  should retrieve the resource from cache instead. If the resource is no
  longer available in the cache the request should be retried without the
  conditional headers.
- 305 Use Proxy.
  `HttpStatus.SC_USE_PROXY`

  The resource must be accessed through the specified proxy. The
  proxy is specified in the Location header.

---

<a id="sslguide"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/sslguide.html -->

<!-- page_index: 12 -->

<a id="sslguide--introduction"></a>

## Introduction

HttpClient provides full support for HTTP over Secure Sockets Layer (SSL) or IETF Transport Layer
Security (TLS) protocols by leveraging the [Java Secure Socket Extension (JSSE)](http://java.sun.com/products/jsse/index.html "External Link"). JSSE has been integrated into the Java 2 platform as of
version 1.4 and works with HttpClient out of the box. On older Java 2 versions JSSE
needs to be manually installed and configured. Installation instructions can be found
[here](http://java.sun.com/products/jsse/doc/guide/API_users_guide.html#Installation "External Link")

<a id="sslguide--standard-ssl-in-httpclient"></a>

## Standard SSL in HttpClient

Once you have JSSE correctly installed, secure HTTP communication over SSL should be as simple
as plain HTTP communication.

```

  HttpClient httpclient = new HttpClient();
  GetMethod httpget = new GetMethod("https://www.verisign.com/"); 
  try { 
    httpclient.executeMethod(httpget);
    System.out.println(httpget.getStatusLine());
  } finally {
    httpget.releaseConnection();
  }
```

HTTPS communication via an authenticating proxy server is also no different from plain HTTP
communication. All the low-level details of establishing a tunneled SSL connection are handled
by HttpClient:

```

  HttpClient httpclient = new HttpClient();
  httpclient.getHostConfiguration().setProxy("myproxyhost", 8080);
  httpclient.getState().setProxyCredentials("my-proxy-realm", " myproxyhost",
  new UsernamePasswordCredentials("my-proxy-username", "my-proxy-password"));
  GetMethod httpget = new GetMethod("https://www.verisign.com/");
  try { 
    httpclient.executeMethod(httpget);
    System.out.println(httpget.getStatusLine());
  } finally {
    httpget.releaseConnection();
  }
```

<a id="sslguide--customizing-ssl-in-httpclient"></a>

## Customizing SSL in HttpClient

The default behaviour of HttpClient is suitable for most uses, however
there are some aspects which you may want to configure. The most common
requirements for customizing SSL are:

- Ability to accept self-signed or untrusted SSL certificates. This
  is highlighted by an `SSLException` with the message
  *Unrecognized SSL handshake* (or similar) being thrown when a
  connection attempt is made.
- You want to use a third party SSL library instead of Sun's default
  implementation.

Implementation of a custom protocol involves the following steps:

1. Provide a custom socket factory that implements
   [org.apache.commons.httpclient.protocol.SecureProtocolSocketFactory](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/protocol/SecureProtocolSocketFactory.html) interface. The socket
   factory is responsible for opening a socket to the target server
   using either the standard or a third party SSL library and
   performing any required initialization such as performing the
   connection handshake. Generally the initialization is performed
   automatically when the socket is created.
2. Instantiate an object of type [org.apache.commons.httpclient.protocol.Protocol](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/protocol/Protocol.html). The new instance
   would be created with a valid URI protocol scheme (https in this
   case), the custom socket factory (discussed above) and a default port
   number (typically 443 for https). For example:


```

Protocol myhttps = new Protocol("https", new MySSLSocketFactory(), 443);
      
```

   The new instance of protocol can then be set as the protocol handler
   for a HostConfiguration. For example to configure the default host and
   protocol handler for a HttpClient instance use:


```

HttpClient httpclient = new HttpClient();
httpclient.getHostConfiguration().setHost("www.whatever.com", 443, myhttps);
GetMethod httpget = new GetMethod("/");
try {
  httpclient.executeMethod(httpget);
  System.out.println(httpget.getStatusLine());
} finally {
  httpget.releaseConnection();
}
```

3. Finally, you can register your custom protocol as the default handler
   for a specific protocol designator (eg: https) by calling the
   Protocol.registerProtocol method. You can specify your own protocol
   designator (such as 'myhttps') if you need to use your custom
   protocol as well as the default SSL protocol implementation.


```

Protocol.registerProtocol("myhttps", 
new Protocol("https", new MySSLSocketFactory(), 9443));
      
```

   Once registered the protocol be used as a 'virtual' scheme inside target URIs.


```

HttpClient httpclient = new HttpClient();
GetMethod httpget = new GetMethod("myhttps://www.whatever.com/");
try {
  httpclient.executeMethod(httpget);
  System.out.println(httpget.getStatusLine());
} finally {
  httpget.releaseConnection();
}
```

   If you want this protocol to represent the default SSL protocol implementation, simply register
   it under 'https' designator, which will make the protocol object take place of the existing one


```

Protocol.registerProtocol("https", 
new Protocol("https", new MySSLSocketFactory(), 443));
HttpClient httpclient = new HttpClient();
GetMethod httpget = new GetMethod("https://www.whatever.com/");
try {
  httpclient.executeMethod(httpget);
  System.out.println(httpget.getStatusLine());
} finally {
  httpget.releaseConnection();
}
```

<a id="sslguide--examples-of-ssl-customization-in-httpclient"></a>

## Examples of SSL customization in HttpClient

There are several custom socket factories available in our contribution
package. They can be a good start for those who seek to tailor the
behavior of the HTTPS protocol to the specific needs of their
application:

- [EasySSLProtocolSocketFactory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/contrib/org/apache/commons/httpclient/contrib/ssl/EasySSLProtocolSocketFactory.java?view=markup "External Link") can be used to create SSL connections that allow the target
  server to authenticate with a self-signed certificate.
- [StrictSSLProtocolSocketFactory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/contrib/org/apache/commons/httpclient/contrib/ssl/StrictSSLProtocolSocketFactory.java?view=markup "External Link") can be used to create SSL connections that can optionally perform host name verification in order to help preventing man-in-the-middle type of attacks.
- [AuthSSLProtocolSocketFactory](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/contrib/org/apache/commons/httpclient/contrib/ssl/AuthSSLProtocolSocketFactory.java?view=markup "External Link") can be used to optionally enforce mutual client/server authentication. This is the most flexible
  implementation of a protocol socket factory. It allows for customization of most, if not all, aspects of the SSL authentication.

<a id="sslguide--known-limitations-and-problems"></a>

## Known limitations and problems

1. **Persistent SSL connections do not work on Sun's JVMs below 1.4**

   Due to what appears to be a bug in Sun's older (below 1.4) implementation of
   Java Virtual Machines or JSSE there's no reliable way of telling if an SSL connection
   is 'stale' or not. For example, the HTTP 1.1 specification permits HTTP servers in
   'keep-alive' mode to drop the connection to the client after a given period inactivity
   without having to notify the client, effectively rendering such connection unusable or
   'stale'. For the HTTP agent written in Java there's no reliable way to test
   if a connection is 'stale' other than attempting to perform a read on it.
   However, a read
   operation on an idle SSL connection on Sun JVM older than 1.4 returns 'end of stream'
   instead of an expected read timeout. That effectively makes the connection appear 'stale'
   to HttpClient, which leaves it with no other way but to drop the connection and to
   open a new one, thus defeating HTTP 1.1 keep-alive mechanism and resulting in significant
   performance degradation (SSL authentication is a highly time consuming operation). The problem appears to have been fixed in Sun's
   Java 1.4 SSL implementation. Sockets which are not using HTTPS are
   unaffected on any JVM.

   **Workaround:** Disable stale connection check if upgrade to Java 1.4 or above is
   not an option. Please note that HttpClient will no longer be able to detect invalid connections
   and some requests may fail due to transport errors. For details on how transport errors can be
   recovered from please refer to the [Exception Handling Guide](#exception-handling--transport-exceptions). If persistent SSL connections support and transport reliability
   is an issue for your application we strongly advise you to upgrade to Java 1.4.
2. **Authetication schemes that rely on persistent connection state do not work on Sun's JVMs
   below 1.4 if SSL is used**

   This problem is directly related to the problem described above. Certain authentication schemes or
   certain implementations of standard authentication schemes are connection based, that is, the user
   authentication is performed once when the connection is being established, rather than every time
   a request is being processed. Microsoft NTLM scheme and Digest scheme as implemented in Microsoft
   Proxy and IIS servers are known to fall into this category. If connections cannot be kept alive
   the user authorization is lost along with the persistent connection state

   **Workaround:** Disable stale connection check or upgrade to Java 1.4 or above.
3. **JSSE prior to Java 1.4 incorrectly reports socket timeout.**

   Prior to Java 1.4, in Sun's JSSE implementation, a read operation that has timed out incorrect
   reports end of stream condition instead of throwing java.io.InterruptedIOException as expected.
   HttpClient responds to this exception by assuming that the connection was dropped and throws a
   NoHttpResponseException. It should instead report "java.io.InterruptedIOException: Read timed
   out". If you encounter NoHttpResponseException when working with an older version of JDK and
   JSSE, it can be caused by the timeout waiting for data and not by a problem with the connection.

   **Work-around:** One possible solution is to increase the timeout value as the server is
   taking too long to start sending the response. Alternatively you may choose to upgrade to Java 1.4 or
   above which does not exhibit this problem.

   The problem has been discovered and reported by Daniel C. Amadei.
4. **HttpClient does not work with IBM JSSE shipped with IBM Websphere Application Platform**

   Several releases of the IBM JSSE exhibit a bug that cause HttpClient to fail while detecting the size
   of the socket send buffer (java.net.Socket.getSendBufferSize method throws java.net.SocketException:
   "Socket closed" exception).

   **Solution:** Make sure that you have all the latest Websphere fix packs applied and IBMJSSE
   is at least version 1.0.3. HttpClient users have reported that IBM Websphere Application Server versions
   4.0.6, 5.0.2.2, 5.1.0 and above do not exhibit this problem.

<a id="sslguide--troubleshooting"></a>

## Troubleshooting

JSSE is prone to configuration problems, especially on older JVMs, which it is not an integral part of. As such, if you do encounter
problems with SSL and HttpClient it is important to check that JSSE is
correctly installed.

The application below can be used as an ultimate test that can reliably
tell if SSL configured properly, as it relies on a plain socket in
order to communicate with the target server. If an exception is thrown
when executing this code, SSL is not correctly installed and configured.
Please refer to Sun's official resources for support or additional
details on JSSE configuration.

```

  import java.io.BufferedReader;
  import java.io.InputStreamReader;
  import java.io.OutputStreamWriter;
  import java.io.Writer;
  import java.net.Socket;

  import javax.net.ssl.SSLSocketFactory;

  public class Test {
        
     public static final String TARGET_HTTPS_SERVER = "www.verisign.com"; 
     public static final int    TARGET_HTTPS_PORT   = 443; 
        
     public static void main(String[] args) throws Exception {
        
       Socket socket = SSLSocketFactory.getDefault().
         createSocket(TARGET_HTTPS_SERVER, TARGET_HTTPS_PORT);
       try {
         Writer out = new OutputStreamWriter(
            socket.getOutputStream(), "ISO-8859-1");
         out.write("GET / HTTP/1.1\r\n");  
         out.write("Host: " + TARGET_HTTPS_SERVER + ":" + 
             TARGET_HTTPS_PORT + "\r\n");  
         out.write("Agent: SSL-TEST\r\n");  
         out.write("\r\n");  
         out.flush();  
         BufferedReader in = new BufferedReader(
            new InputStreamReader(socket.getInputStream(), "ISO-8859-1"));
         String line = null;
         while ((line = in.readLine()) != null) {
            System.out.println(line);
         }
       } finally {
         socket.close(); 
       }
     }
  }
        
```

---

<a id="threading"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/threading.html -->

<!-- page_index: 13 -->

<a id="threading--introduction"></a>

## Introduction

This document provides an overview of how to use HttpClient safely from within a
multi-threaded environment. It is broken down into the following main sections:

- [MultiThreadedHttpConnectionManager](#threading--multithreadedhttpconnectionmanager)
- [Connection Release](#threading--connection_release)

Please see the [MultiThreadedExample](http://svn.apache.org/viewvc/httpcomponents/oac.hc3x/trunk/src/examples/MultiThreadedExample.java?view=markup "External Link")
for a concrete example.

<a id="threading--multithreadedhttpconnectionmanager"></a>

## MultiThreadedHttpConnectionManager

The main reason for using multiple theads in HttpClient is to allow the
execution of multiple methods at once (Simultaniously downloading the latest builds of HttpClient and
Tomcat for example). During execution each method uses an instance of an HttpConnection.
Since connections can only be safely used from a single thread and method at a time and
are a finite resource, we need to ensure that connections are properly allocated to the methods that require them.
This job goes to the [MultiThreadedHttpConnectionManager](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html).

To get started one must create an instance of the MultiThreadedHttpConnectionManager
and give it to an HttpClient. This looks something like:

```

      	MultiThreadedHttpConnectionManager connectionManager = 
      		new MultiThreadedHttpConnectionManager();
      	HttpClient client = new HttpClient(connectionManager);
      
```

This instance of HttpClient can now be used to execute multiple methods from multiple
threads. Each subsequent call to HttpClient.executeMethod() will go to the connection
manager and ask for an instance of HttpConnection. This connection will be checked out
to the method and as a result it must also be returned. More on this below in **Connection Release**.

<a id="threading--options"></a>

### Options

The MultiThreadedHttpConnectionManager supports the following options:

connectionStaleCheckingEnabled

The connectionStaleCheckingEnabled flag to set on all created connections. This value
should be left true except in special circumstances. Consult the
[HttpConnection](https://hc.apache.org/httpclient-legacy/apidocs/org/apache/commons/httpclient/HttpConnection.html#setStaleCheckingEnabled(boolean))
docs for more detail.

maxConnectionsPerHost

The maximum number of connections that will be created for any particular
HostConfiguration. Defaults to 2.

maxTotalConnections

The maximum number of active connections. Defaults to 20.

In general the connection manager makes an attempt to reuse connections
for a particular host while still allowing different connections to
be used simultaneously. Connection are reclaimed using a least recently
used approach.

<a id="threading--connection-release"></a>

## Connection Release

One main side effect of connection management is that connections must
be manually released when no longer used. This is due to the fact
that HttpClient cannot determine when a method is no longer using its connection.
This occurs because a method's response body is not read directly by
HttpClient, but by the application using HttpClient. When the response is read it must obviously make use of the method's
connection. Thus, a connection cannot be released from a method until the method's
response body is read which is after HttpClient finishes executing the
method. The application therefore must manually release the
connection by calling releaseConnection() on the method after the
response body has been read. To safely ensure
connection release HttpClient should be used in the following manner:

```


      	MultiThreadedHttpConnectionManager connectionManager = 
      		new MultiThreadedHttpConnectionManager();
      	HttpClient client = new HttpClient(connectionManager);
			...
        // and then from inside some thread executing a method
        GetMethod get = new GetMethod("http://httpcomponents.apache.org/");
        try {
            client.executeMethod(get);
            // print response to stdout
            System.out.println(get.getResponseBodyAsStream());
        } finally {
            // be sure the connection is released back to the connection 
            // manager
            get.releaseConnection();
        }
    
```

Particularly, notice that the connection is released regardless of
what the result of executing the method was or whether or not an
exception was thrown. For every call to HttpClient.executeMethod there
must be a matching call to method.releaseConnection().

---

<a id="troubleshooting"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/troubleshooting.html -->

<!-- page_index: 14 -->

<a id="troubleshooting--introduction"></a>

## Introduction

This document outlines some of the techniques that often help when
trying to track down a problem in *HttpClient*. Please try the suggestions
on this page before emailing the user or dev lists with questions. If
none of these things help, please provide the information they provide to
help the developers track down the problem.

<a id="troubleshooting--things-to-try"></a>

## Things To Try

1. Try connecting with a normal browser and make sure the server gives
   the right response.
2. If you're using a proxy server try without it if possible.
3. Try the same code on a different server (preferably running
   different server software).
4. Check that your code matches the general pattern for using
   *HttpClient* as described in the [tutorial](#tutorial).
5. Set the `User-Agent` request header to masquerade *HttpClient* as a popular browser such as IE or Firefox. Certain web sites are optimized
   to work with just one or a number of specific browser applications. These sites
   frequently reject requests originating from user agents they do not recognize.
   For example, setting the `User-Agent` request header to `Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)` would deceive the target
   server into believing that the request was issues by Microsoft Internet Explorer
   6.0 on Windows 2000.
6. Set the [logging level](#logging) to debug and check
   the output for the cause of the problem.
7. Enable the [wire trace](#logging) and follow the
   communication between the client and server to determine where the
   problem is occurring.
8. Consult the "Known limitations and problems" section of the
   [SSL Guide](#sslguide--known-limitations-and-problems)
   and the [Authentication Guide](#authentication--known-limitations-and-problems) to see if this is a known problem and follow the
   instructions given in these resources
9. Use telnet or netcat to manually send the request to the server.
   This is particularly useful once you think you know what the problem is
   and you want to easily test that changing what *HttpClient* sends will
   fix it.
10. Use netcat in listen mode to act as the server and check how
    *HttpClient* handles various responses.
11. Try updating to the latest nightly build of *HttpClient*. Bugs
    happen and they are generally fixed pretty quickly so testing against
    the latest build is often worthwhile.

<a id="troubleshooting--asking-for-help"></a>

## Asking For Help

If you've tried the things above and still can't work out how to fix
the problem, it might be time to contact the [mailing list](https://hc.apache.org/httpclient-legacy/mail-lists.html) for support. All questions, bug
reports etc should be directed to the HttpClient user list.

When you do send off the email, please include as much detail as you
can, particularly inlined wire trace logs as there is almost
nothing we can do to help without them.
If you are seeing exceptions being thrown, the full stack
trace is essential to tracking down the problem. Any of the information
you gained from the "things to try" section above are probably worth
mentioning.

<a id="troubleshooting--reporting-bugs"></a>

## Reporting Bugs

If you're fairly certain that the problem is a bug in *HttpClient*, log it in [JIRA](http://issues.apache.org/jira/browse/HTTPCLIENT "External Link").
Make sure you spend some time searching the existing bugs to make sure it
hasn't already been logged. If you're unsure about whether or not to log
something in JIRA, it's probably worth bringing it up on the
developer mailing list to clarify the situation.

---

<a id="tutorial"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/tutorial.html -->

<!-- page_index: 15 -->

<a id="tutorial--overview"></a>

## Overview

This tutorial is designed to provide a basic overview of how to use
*HttpClient*. When you have completed the tutorial you will have written
a simple application that downloads a page using *HttpClient*.

It is assumed that you have an understanding of how to program in
Java and are familiar with the development environment you are using.

<a id="tutorial--getting-ready"></a>

## Getting Ready

The first thing you need to do is get a copy of *HttpClient* and its
[dependencies](https://hc.apache.org/httpclient-legacy/dependencies.html). This tutorial was
written for *HttpClient* 3.0. You will also need JDK 1.3 or above.

Once you've downloaded *HttpClient* and dependencies you will need to
put them on your classpath. There is also an optional dependency on JSSE
which is required for HTTPS connections; this is not required for this
tutorial.

<a id="tutorial--concepts"></a>

## Concepts

The general process for using *HttpClient* consists of a number of
steps:

1. Create an instance of `HttpClient`.
2. Create an instance of one of the methods (GetMethod in this
   case). The URL to connect to is passed in to the the method
   constructor.
3. Tell `HttpClient` to execute the method.
4. Read the response.
5. Release the connection.
6. Deal with the response.

We'll cover how to perform each of these steps below. Notice that we
go through the entire process regardless of whether the server returned
an error or not. This is important because HTTP 1.1 allows multiple
requests to use the same connection by simply sending the requests one
after the other. Obviously, if we don't read the entire response to
the first request, the left over data will get in the way of the second
response. *HttpClient* tries to handle this but to avoid problems it is
important to always release the connection.

Upon the connection release
HttpClient will do its best to ensure that the connection is reusable.

It is important to always release the connection regardless of whether the server
returned an error or not.

<a id="tutorial--instantiating-httpclient"></a>

## Instantiating HttpClient

The no argument constructor for `HttpClient` provides a good set of
defaults for most situations so that is what we'll use.

```
HttpClient client = new HttpClient();
```

<a id="tutorial--creating-a-method"></a>

## Creating a Method

The various methods defined by the HTTP specification correspond to
the various classes in *HttpClient* which implement the HttpMethod
interface. These classes are all found in the package
`org.apache.commons.httpclient.methods`.

We will be using the Get method which is a simple method that simply
takes a URL and gets the document the URL points to.

```
HttpMethod method = new GetMethod("http://www.apache.org/");
```

<a id="tutorial--execute-the-method"></a>

## Execute the Method

The actual execution of the method is performed by calling
`executeMethod` on the client and passing in the method to
execute. Since networks connections are unreliable, we also need to deal
with any errors that occur.

There are two kinds of exceptions that could be thrown by
executeMethod, `HttpException` and `IOException`.

The other useful piece of information is the status code that is
returned by the server. This code is returned by executeMethod as an
int and can be used to determine if the request was successful or not
and can sometimes indicate that further action is required by the
client such as providing authentication credentials.

<a id="tutorial--httpexception"></a>

### HttpException

An HttpException represents a logical error and is thrown when the request
cannot be sent or the response cannot be processed due to a fatal violation of
the HTTP specification. Usually this kind of exceptions cannot be recovered
from. For a detailed discussion on protocol exceptions please refer to
[the HttpClient exception
handling guide](#exception-handling--protocol-exceptions). Note that HttpException actually extends IOException
so you can just ignore it and catch the IOException if your application does
not distinguish between protocol and transport errors.

<a id="tutorial--ioexception"></a>

### IOException

A plain IOException (which is not a subclass of HttpException) represents a
transport error and is thrown when an error occurs that is likely to be a
once-off I/O problem. Usually the request has a good chance of succeeding on
a second attempt, so per default HttpClient will try to recover the request
automatically. For a detailed discussion on transport exceptions please refer to
[the HttpClient exception
handling guide](#exception-handling--transport-exceptions).

<a id="tutorial--method-recovery"></a>

### Method recovery

Per default HttpClient will automatically attempt to recover from the not-fatal
errors, that is, when a plain IOException is thrown. HttpClient will retry the
method three times provided that the request has never been fully transmitted to
the target server. For a detailed discussion on HTTP method recovery please refer
to [the HttpClient
exception handling guide](#exception-handling--http-transport-safety)

```

// set per default
client.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, 
  new DefaultHttpMethodRetryHandler());
```

Default recovery procedure can be replaced with a custom one. The number
of automatic retries can be increased. HttpClient can also be instructed to
retry the method even though the request may have already been processed by
the server and the I/O exception has occurred while receiving the response.
Please exercise caution when enabling auto-retrial. Use it only if the method
is known to be idempotent, that is, it is known to be safe to retry multiple
times without causing data corruption or data inconsistency.

The rule of thumb is GET methods are usually safe unless known otherwise, entity enclosing methods such as POST and PUT are usually unsafe unless known
otherwise.

```

DefaultMethodRetryHandler retryhandler = new DefaultMethodRetryHandler(10, true);
client.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, retryhandler);
```

<a id="tutorial--read-the-response"></a>

## Read the Response

It is vital that the response body is always read regardless of the
status returned by the server. There are three ways to do this:

- Call `method.getResponseBody()`. This will return a
  byte array containing the data in the response body.
- Call `method.getResponseBodyAsString()`. This will
  return a String containing the response body. Be warned though that
  the conversion from bytes to a String is done using the default
  encoding so this method may not be portable across all platforms.
- Call `method.getResponseBodyAsStream()` and read the
  entire contents of the stream then call `stream.close()`.
  This method is best if it is possible for a lot of data to be received
  as it can be buffered to a file or processed as it is read. Be sure to
  always read the entirety of the data and call close on the stream.

For this tutorial we will use `getResponseBody()` for simplicity.

```
byte[] responseBody = method.getResponseBody();
```

<a id="tutorial--release-the-connection"></a>

## Release the Connection

This is a crucial step to keep things flowing. We must tell
*HttpClient* that we are done with the connection and that it can now be
reused. Without doing this *HttpClient* will wait indefinitely for a
connection to free up so that it can be reused.

```
method.releaseConnection();
```

<a id="tutorial--deal-with-the-repsonse"></a>

## Deal with the Repsonse

We've now completed our interaction with *HttpClient* and can just
concentrate on doing what we need to do with the data. In our case, we'll just print it out to the console.

It's worth noting that if you were retrieving the response as a stream
and processing it as it is read, this step would actually be combined
with reading the connection, and when you'd finished processing all the
data, you'd then close the input stream and release the connection.

Note: We should pay attention to character encodings here instead of
just using the system default.

```
System.out.println(new String(responseBody));
```

<a id="tutorial--final-source-code"></a>

## Final Source Code

When we put all of that together plus a little bit of glue code we get
the program below.

```

import org.apache.commons.httpclient.*;
import org.apache.commons.httpclient.methods.*;
import org.apache.commons.httpclient.params.HttpMethodParams;

import java.io.*;

public class HttpClientTutorial {
  
  private static String url = "http://www.apache.org/";

  public static void main(String[] args) {
    // Create an instance of HttpClient.
    HttpClient client = new HttpClient();

    // Create a method instance.
    GetMethod method = new GetMethod(url);
    
    // Provide custom retry handler is necessary
    method.getParams().setParameter(HttpMethodParams.RETRY_HANDLER, 
    		new DefaultHttpMethodRetryHandler(3, false));

    try {
      // Execute the method.
      int statusCode = client.executeMethod(method);

      if (statusCode != HttpStatus.SC_OK) {
        System.err.println("Method failed: " + method.getStatusLine());
      }

      // Read the response body.
      byte[] responseBody = method.getResponseBody();

      // Deal with the response.
      // Use caution: ensure correct character encoding and is not binary data
      System.out.println(new String(responseBody));

    } catch (HttpException e) {
      System.err.println("Fatal protocol violation: " + e.getMessage());
      e.printStackTrace();
    } catch (IOException e) {
      System.err.println("Fatal transport error: " + e.getMessage());
      e.printStackTrace();
    } finally {
      // Release the connection.
      method.releaseConnection();
    }  
  }
}
```

---

<a id="index"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/index.html -->

<!-- page_index: 16 -->

<a id="index--end-of-life"></a>

## End of life

The Commons HttpClient project is now end of life, and is no longer being developed.
It has been replaced by the [Apache HttpComponents](https://hc.apache.org/) project
in its [HttpClient](https://hc.apache.org/httpcomponents-client-ga) and [HttpCore](https://hc.apache.org/httpcomponents-core-ga/) modules, which offer better performance and more flexibility.

<a id="index--introduction"></a>

## Introduction

The Hyper-Text Transfer Protocol (HTTP) is perhaps the most
significant protocol used on the Internet today.
Web services, network-enabled appliances and the growth
of network computing continue to expand the role of the HTTP
protocol beyond user-driven web browsers, while increasing the
number of applications that require HTTP support.

Although the java.net
package provides basic functionality for accessing resources via HTTP, it doesn't provide the full flexibility or functionality needed
by many applications. The Jakarta Commons *HttpClient*
component seeks to fill this void
by providing an efficient, up-to-date, and feature-rich package
implementing the client side of the most recent HTTP standards
and recommendations. See the [Features](#features) page
for more details on standards compliance and capabilities.

Designed for extension while providing robust support for the
base HTTP protocol, the *HttpClient* component may be of interest
to anyone building HTTP-aware client applications such as web
browsers, web service clients, or systems that leverage or extend
the HTTP protocol for distributed communication.

There are many projects that use *HttpClient* to provide the core HTTP functionality.
Some of these are open source with project pages you can find on the web
while others are closed source that you would never see or hear about.
The Apache Source License provides maximum flexibility for source and binary
reuse. Please see the [Applications](http://wiki.apache.org/jakarta-httpclient/HttpClientPowered "External Link") page for projects using *HttpClient*.

<a id="index--history"></a>

## History

*HttpClient* was started in 2001 as a subproject of the
Jakarta Commons, based on code developed by the
[Jakarta Slide](http://jakarta.apache.org/slide/ "External Link") project.
It was promoted out of the Commons in 2004, graduating to a separate
Jakarta project. In 2005, the HttpComponents project at Jakarta was
created, with the task of developing a successor
to *HttpClient 3.x* and to maintain the existing codebase until
the new one is ready to take over.
The [Commons](http://commons.apache.org/ "External Link") project, cradle of *HttpClient*, left [Jakarta](http://jakarta.apache.org/ "External Link")
in 2007 to become an independent Top Level Project.
Later in the same year, the
[HttpComponents](http://httpcomponents.apache.org/ "External Link")
project also left Jakarta to become an independent Top Level Project, taking the responsibility for maintaining *HttpClient* with it.

---

<a id="maven-reports"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/maven-reports.html -->

<!-- page_index: 17 -->

<a id="maven-reports--maven-generated-reports"></a>

## Maven Generated Reports

This document provides an overview of the various reports that are automatically generated by
[Maven](http://maven.apache.org/ "External Link")
. Each report is briefly described below.

<a id="maven-reports--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [JavaDocs](https://hc.apache.org/httpclient-legacy/apidocs/index.html "New Window") | JavaDoc API documentation. |
| [JavaDoc Report](#javadoc) | Report on the generation of JavaDoc. |
| [JavaDoc Warnings Report](#javadoc-warnings-report) | Formatted report of JavaDoc warnings. |
| [Metrics](#jdepend-report) | Report on source code metrics. |
| [Unit Tests](https://hc.apache.org/httpclient-legacy/junit-report.html) | Report on the results of the unit tests. |
| [Source Xref](https://hc.apache.org/httpclient-legacy/xref/index.html "New Window") | A set of browsable cross-referenced sources. |
| [Test Xref](https://hc.apache.org/httpclient-legacy/xref-test/index.html "New Window") | A set of browsable cross-referenced test sources. |
| [Project License](https://hc.apache.org/httpclient-legacy/license.html) | Displays the primary license for the project. |

---

<a id="javadoc"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/javadoc.html -->

<!-- page_index: 18 -->

<a id="javadoc--javadoc-report"></a>

## Javadoc Report

```
  Generating Javadoc
  Javadoc execution
  Loading source files for package org.apache.commons.httpclient...
  Loading source files for package org.apache.commons.httpclient.auth...
  Loading source files for package org.apache.commons.httpclient.protocol...
  Loading source files for package org.apache.commons.httpclient.methods...
  Loading source files for package org.apache.commons.httpclient.methods.multipart...
  Loading source files for package org.apache.commons.httpclient.cookie...
  Loading source files for package org.apache.commons.httpclient.params...
  Loading source files for package org.apache.commons.httpclient.util...
  Constructing Javadoc information...
  Standard Doclet version 1.5.0_13
  Building tree for all the packages and classes...
  Generating target/docs/apidocs/serialized-form.html...
  Copying file /home/rweber/.maven/cache/maven-javadoc-plugin-1.7/plugin-resources/stylesheet.css to file target/docs/apidocs/stylesheet.css...
  Building index for all the packages and classes...
  Building index for all classes...
```

---

<a id="javadoc-warnings-report"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/javadoc-warnings-report.html -->

<!-- page_index: 19 -->

<a id="javadoc-warnings-report--javadoc-warnings"></a>

## JavaDoc Warnings

The following document contains JavaDoc warnings.

<a id="javadoc-warnings-report--summary"></a>

## Summary

| Files | Errors |
| --- | --- |
| 0 | 0 |

<a id="javadoc-warnings-report--files"></a>

## Files

Files

Errors

---

<a id="jdepend-report"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/jdepend-report.html -->

<!-- page_index: 20 -->

<a id="jdepend-report--metric-results"></a>

## Metric Results

[
[summary](#jdepend-report--summary)] [
[packages](#jdepend-report--packages)] [
[cycles](#jdepend-report--cycles)] [
[explanations](#jdepend-report--explanations)]

The following document contains the results of a
[JDepend](http://www.clarkware.com/software/JDepend.html "External Link")metric analysis. The various metrics are defined at the bottom of this document.

<a id="jdepend-report--summary"></a>

## Summary

[
[summary](#jdepend-report--summary)] [
[packages](#jdepend-report--packages)] [
[cycles](#jdepend-report--cycles)] [
[explanations](#jdepend-report--explanations)]

| Package | TC | AC | CC | AC | EC | A | I | D |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [org.apache.commons.httpclient](#jdepend-report--org_apache_commons_httpclient) | 68 | 7 | 61 | 6 | 15 | 0,1 | 71% | 18% |
| [org.apache.commons.httpclient.auth](#jdepend-report--org_apache_commons_httpclient_auth) | 20 | 5 | 15 | 1 | 10 | 0,25 | 91% | 16% |
| [org.apache.commons.httpclient.cookie](#jdepend-report--org_apache_commons_httpclient_cookie) | 23 | 4 | 19 | 1 | 6 | 0,17 | 86% | 3% |
| [org.apache.commons.httpclient.methods](#jdepend-report--org_apache_commons_httpclient_methods) | 15 | 3 | 12 | 1 | 8 | 0,2 | 89% | 9% |
| [org.apache.commons.httpclient.methods.multipart](#jdepend-report--org_apache_commons_httpclient_methods_multipart) | 8 | 3 | 5 | 1 | 7 | 0,38 | 88% | 25% |
| [org.apache.commons.httpclient.params](#jdepend-report--org_apache_commons_httpclient_params) | 9 | 2 | 7 | 5 | 5 | 0,22 | 50% | 28% |
| [org.apache.commons.httpclient.protocol](#jdepend-report--org_apache_commons_httpclient_protocol) | 9 | 3 | 6 | 1 | 10 | 0,33 | 91% | 24% |
| [org.apache.commons.httpclient.util](#jdepend-report--org_apache_commons_httpclient_util) | 15 | 0 | 15 | 6 | 11 | 0 | 65% | 35% |

<a id="jdepend-report--packages"></a>

## Packages

[
[summary](#jdepend-report--summary)] [
[packages](#jdepend-report--packages)] [
[cycles](#jdepend-report--cycles)] [
[explanations](#jdepend-report--explanations)]

<a id="jdepend-report--org.apache.commons.httpclient"></a>

### org.apache.commons.httpclient

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 6 | 15 | 10% | 71% | 18% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/Credentials.html">Credentials</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpConnectionManager.html">HttpConnectionManager</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpMethod.html">HttpMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpMethodBase.html">HttpMethodBase</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpMethodRetryHandler.html">HttpMethodRetryHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MethodRetryHandler.html">MethodRetryHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ResponseConsumedWatcher.html">ResponseConsumedWatcher</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/AutoCloseInputStream.html">AutoCloseInputStream</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ChunkedInputStream.html">ChunkedInputStream</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ChunkedOutputStream.html">ChunkedOutputStream</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/CircularRedirectException.html">CircularRedirectException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ConnectMethod.html">ConnectMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ConnectTimeoutException.html">ConnectTimeoutException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ConnectionPoolTimeoutException.html">ConnectionPoolTimeoutException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ContentLengthInputStream.html">ContentLengthInputStream</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/Cookie.html">Cookie</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/DefaultHttpMethodRetryHandler.html">DefaultHttpMethodRetryHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/DefaultMethodRetryHandler.html">DefaultMethodRetryHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/Header.html">Header</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HeaderElement.html">HeaderElement</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HeaderGroup.html">HeaderGroup</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HostConfiguration.html">HostConfiguration</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpClient.html">HttpClient</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpClientError.html">HttpClientError</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpConnection.html">HttpConnection</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpConstants.html">HttpConstants</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpContentTooLargeException.html">HttpContentTooLargeException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpException.html">HttpException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpHost.html">HttpHost</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpMethodBase.html">HttpMethodBase$1</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpMethodDirector.html">HttpMethodDirector</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpParser.html">HttpParser</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpRecoverableException.html">HttpRecoverableException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpState.html">HttpState</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpStatus.html">HttpStatus</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpURL.html">HttpURL</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpVersion.html">HttpVersion</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/HttpsURL.html">HttpsURL</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/InvalidRedirectLocationException.html">InvalidRedirectLocationException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$1</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$ConnectionPool</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$ConnectionSource</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$HostConnectionPool</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$HttpConnectionAdapter</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$HttpConnectionWithReference</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$ReferenceQueueThread</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/MultiThreadedHttpConnectionManager.html">MultiThreadedHttpConnectionManager$WaitingThread</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/NTCredentials.html">NTCredentials</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/NameValuePair.html">NameValuePair</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/NoHttpResponseException.html">NoHttpResponseException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ProtocolException.html">ProtocolException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ProxyClient.html">ProxyClient</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ProxyClient.html">ProxyClient$1</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ProxyClient.html">ProxyClient$ConnectResponse</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ProxyClient.html">ProxyClient$DummyConnectionManager</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/ProxyHost.html">ProxyHost</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/RedirectException.html">RedirectException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/SimpleHttpConnectionManager.html">SimpleHttpConnectionManager</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/StatusLine.html">StatusLine</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/URI.html">URI</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/URI.html">URI$DefaultCharsetChanged</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/URI.html">URI$LocaleToCharsetMap</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/URIException.html">URIException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/UsernamePasswordCredentials.html">UsernamePasswordCredentials</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/Wire.html">Wire</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/WireLogInputStream.html">WireLogInputStream</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/WireLogOutputStream.html">WireLogOutputStream</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_auth">org.apache.commons.httpclient.auth</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_cookie">org.apache.commons.httpclient.cookie</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods">org.apache.commons.httpclient.methods</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_params">org.apache.commons.httpclient.params</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_protocol">org.apache.commons.httpclient.protocol</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_util">org.apache.commons.httpclient.util</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_io">java.io</a>
</li>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_lang_ref">java.lang.ref</a>
</li>
<li>
<a href="#jdepend-report--java_lang_reflect">java.lang.reflect</a>
</li>
<li>
<a href="#jdepend-report--java_net">java.net</a>
</li>
<li>
<a href="#jdepend-report--java_security">java.security</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_codec">org.apache.commons.codec</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_codec_net">org.apache.commons.codec.net</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_auth">org.apache.commons.httpclient.auth</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_cookie">org.apache.commons.httpclient.cookie</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_params">org.apache.commons.httpclient.params</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_protocol">org.apache.commons.httpclient.protocol</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_util">org.apache.commons.httpclient.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_logging">org.apache.commons.logging</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--org.apache.commons.httpclient.auth"></a>

### org.apache.commons.httpclient.auth

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 10 | 25% | 91% | 16% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthPolicy.html">AuthPolicy</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthScheme.html">AuthScheme</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthSchemeBase.html">AuthSchemeBase</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/CredentialsProvider.html">CredentialsProvider</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/RFC2617Scheme.html">RFC2617Scheme</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthChallengeException.html">AuthChallengeException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthChallengeParser.html">AuthChallengeParser</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthChallengeProcessor.html">AuthChallengeProcessor</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthScope.html">AuthScope</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthState.html">AuthState</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/AuthenticationException.html">AuthenticationException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/BasicScheme.html">BasicScheme</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/CredentialsNotAvailableException.html">CredentialsNotAvailableException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/DigestScheme.html">DigestScheme</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/HttpAuthRealm.html">HttpAuthRealm</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/HttpAuthenticator.html">HttpAuthenticator</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/InvalidCredentialsException.html">InvalidCredentialsException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/MalformedChallengeException.html">MalformedChallengeException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/NTLM.html">NTLM</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/auth/NTLMScheme.html">NTLMScheme</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_security">java.security</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--javax_crypto">javax.crypto</a>
</li>
<li>
<a href="#jdepend-report--javax_crypto_spec">javax.crypto.spec</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_codec_binary">org.apache.commons.codec.binary</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_params">org.apache.commons.httpclient.params</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_util">org.apache.commons.httpclient.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_logging">org.apache.commons.logging</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--org.apache.commons.httpclient.cookie"></a>

### org.apache.commons.httpclient.cookie

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 6 | 17% | 86% | 3% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/CookieAttributeHandler.html">CookieAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/CookiePolicy.html">CookiePolicy</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/CookieSpec.html">CookieSpec</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/CookieVersionSupport.html">CookieVersionSupport</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/Cookie2.html">Cookie2</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/CookieOrigin.html">CookieOrigin</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/CookiePathComparator.html">CookiePathComparator</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/CookieSpecBase.html">CookieSpecBase</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/IgnoreCookiesSpec.html">IgnoreCookiesSpec</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/MalformedCookieException.html">MalformedCookieException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/NetscapeDraftSpec.html">NetscapeDraftSpec</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2109Spec.html">RFC2109Spec</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$1</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$Cookie2DomainAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$Cookie2MaxageAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$Cookie2PathAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$Cookie2PortAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$Cookie2VersionAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$CookieCommentAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$CookieCommentUrlAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$CookieDiscardAttributeHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/cookie/RFC2965Spec.html">RFC2965Spec$CookieSecureAttributeHandler</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_text">java.text</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_util">org.apache.commons.httpclient.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_logging">org.apache.commons.logging</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--org.apache.commons.httpclient.methods"></a>

### org.apache.commons.httpclient.methods

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 8 | 20% | 89% | 9% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/EntityEnclosingMethod.html">EntityEnclosingMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/ExpectContinueMethod.html">ExpectContinueMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/RequestEntity.html">RequestEntity</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/ByteArrayRequestEntity.html">ByteArrayRequestEntity</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/DeleteMethod.html">DeleteMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/FileRequestEntity.html">FileRequestEntity</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/GetMethod.html">GetMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/HeadMethod.html">HeadMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/InputStreamRequestEntity.html">InputStreamRequestEntity</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/MultipartPostMethod.html">MultipartPostMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/OptionsMethod.html">OptionsMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/PostMethod.html">PostMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/PutMethod.html">PutMethod</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/StringRequestEntity.html">StringRequestEntity</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/TraceMethod.html">TraceMethod</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods_multipart">org.apache.commons.httpclient.methods.multipart</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_io">java.io</a>
</li>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods_multipart">org.apache.commons.httpclient.methods.multipart</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_params">org.apache.commons.httpclient.params</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_util">org.apache.commons.httpclient.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_logging">org.apache.commons.logging</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--org.apache.commons.httpclient.methods.multipart"></a>

### org.apache.commons.httpclient.methods.multipart

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 7 | 38% | 88% | 25% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/Part.html">Part</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/PartBase.html">PartBase</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/PartSource.html">PartSource</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/ByteArrayPartSource.html">ByteArrayPartSource</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/FilePart.html">FilePart</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/FilePartSource.html">FilePartSource</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/MultipartRequestEntity.html">MultipartRequestEntity</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/methods/multipart/StringPart.html">StringPart</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods">org.apache.commons.httpclient.methods</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_io">java.io</a>
</li>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods">org.apache.commons.httpclient.methods</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_params">org.apache.commons.httpclient.params</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_util">org.apache.commons.httpclient.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_logging">org.apache.commons.logging</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--org.apache.commons.httpclient.params"></a>

### org.apache.commons.httpclient.params

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 5 | 5 | 22% | 50% | 28% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/HttpParams.html">HttpParams</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/HttpParamsFactory.html">HttpParamsFactory</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/DefaultHttpParams.html">DefaultHttpParams</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/DefaultHttpParamsFactory.html">DefaultHttpParamsFactory</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/HostParams.html">HostParams</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/HttpClientParams.html">HttpClientParams</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/HttpConnectionManagerParams.html">HttpConnectionManagerParams</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/HttpConnectionParams.html">HttpConnectionParams</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/params/HttpMethodParams.html">HttpMethodParams</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_auth">org.apache.commons.httpclient.auth</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods">org.apache.commons.httpclient.methods</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods_multipart">org.apache.commons.httpclient.methods.multipart</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_protocol">org.apache.commons.httpclient.protocol</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_io">java.io</a>
</li>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_logging">org.apache.commons.logging</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--org.apache.commons.httpclient.protocol"></a>

### org.apache.commons.httpclient.protocol

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 1 | 10 | 33% | 91% | 24% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.html">ControllerThreadSocketFactory$SocketTask</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/ProtocolSocketFactory.html">ProtocolSocketFactory</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/SecureProtocolSocketFactory.html">SecureProtocolSocketFactory</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.html">ControllerThreadSocketFactory</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/ControllerThreadSocketFactory.html">ControllerThreadSocketFactory$1</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/DefaultProtocolSocketFactory.html">DefaultProtocolSocketFactory</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/Protocol.html">Protocol</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/ReflectionSocketFactory.html">ReflectionSocketFactory</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/protocol/SSLProtocolSocketFactory.html">SSLProtocolSocketFactory</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_io">java.io</a>
</li>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_lang_reflect">java.lang.reflect</a>
</li>
<li>
<a href="#jdepend-report--java_net">java.net</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--javax_net">javax.net</a>
</li>
<li>
<a href="#jdepend-report--javax_net_ssl">javax.net.ssl</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_params">org.apache.commons.httpclient.params</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_util">org.apache.commons.httpclient.util</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--org.apache.commons.httpclient.util"></a>

### org.apache.commons.httpclient.util

| Afferent Couplings | Efferent Couplings | Abstractness | Instability | Distance |
| --- | --- | --- | --- | --- |
| 6 | 11 | 0% | 65% | 35% |

<table class="bodyTable">
<thead>
<tr>
<th>Abstract Classes</th>
<th>Concrete Classes</th>
<th>Used by Packages</th>
<th>Uses Packages</th>
</tr>
</thead>
<tbody>
<tr>
<td>
<em>None</em>
</td>
<td>
<ul>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/DateParseException.html">DateParseException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/DateParser.html">DateParser</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/DateUtil.html">DateUtil</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/EncodingUtil.html">EncodingUtil</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/ExceptionUtil.html">ExceptionUtil</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/HttpURLConnection.html">HttpURLConnection</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/IdleConnectionHandler.html">IdleConnectionHandler</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/IdleConnectionTimeoutThread.html">IdleConnectionTimeoutThread</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/LangUtils.html">LangUtils</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/ParameterFormatter.html">ParameterFormatter</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/ParameterParser.html">ParameterParser</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/TimeoutController.html">TimeoutController</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/TimeoutController.html">TimeoutController$TimeoutException</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/URIUtil.html">URIUtil</a>
</li>
<li>
<a href="https://hc.apache.org/httpclient-legacy/xref/org/apache/commons/httpclient/util/URIUtil.html">URIUtil$Coder</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_auth">org.apache.commons.httpclient.auth</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_cookie">org.apache.commons.httpclient.cookie</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods">org.apache.commons.httpclient.methods</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_methods_multipart">org.apache.commons.httpclient.methods.multipart</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient_protocol">org.apache.commons.httpclient.protocol</a>
</li>
</ul>
</td>
<td>
<ul>
<li>
<a href="#jdepend-report--java_io">java.io</a>
</li>
<li>
<a href="#jdepend-report--java_lang">java.lang</a>
</li>
<li>
<a href="#jdepend-report--java_lang_reflect">java.lang.reflect</a>
</li>
<li>
<a href="#jdepend-report--java_net">java.net</a>
</li>
<li>
<a href="#jdepend-report--java_security">java.security</a>
</li>
<li>
<a href="#jdepend-report--java_text">java.text</a>
</li>
<li>
<a href="#jdepend-report--java_util">java.util</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_codec">org.apache.commons.codec</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_codec_net">org.apache.commons.codec.net</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_httpclient">org.apache.commons.httpclient</a>
</li>
<li>
<a href="#jdepend-report--org_apache_commons_logging">org.apache.commons.logging</a>
</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--cycles"></a>

## Cycles

[
[summary](#jdepend-report--summary)] [
[packages](#jdepend-report--packages)] [
[cycles](#jdepend-report--cycles)] [
[explanations](#jdepend-report--explanations)]

<table class="bodyTable">
<thead>
<tr>
<th>Package</th>
<th>Cyclic Dependencies</th>
</tr>
</thead>
<tbody>
<tr>
<td>org.apache.commons.httpclient</td>
<td>
<ul>
<li>org.apache.commons.httpclient.util</li>
<li>org.apache.commons.httpclient</li>
</ul>
</td>
</tr>
<tr>
<td>org.apache.commons.httpclient.auth</td>
<td>
<ul>
<li>org.apache.commons.httpclient</li>
<li>org.apache.commons.httpclient.util</li>
<li>org.apache.commons.httpclient</li>
</ul>
</td>
</tr>
<tr>
<td>org.apache.commons.httpclient.cookie</td>
<td>
<ul>
<li>org.apache.commons.httpclient</li>
<li>org.apache.commons.httpclient.util</li>
<li>org.apache.commons.httpclient</li>
</ul>
</td>
</tr>
<tr>
<td>org.apache.commons.httpclient.methods</td>
<td>
<ul>
<li>org.apache.commons.httpclient</li>
<li>org.apache.commons.httpclient.util</li>
<li>org.apache.commons.httpclient</li>
</ul>
</td>
</tr>
<tr>
<td>org.apache.commons.httpclient.methods.multipart</td>
<td>
<ul>
<li>org.apache.commons.httpclient.util</li>
<li>org.apache.commons.httpclient</li>
<li>org.apache.commons.httpclient.util</li>
</ul>
</td>
</tr>
<tr>
<td>org.apache.commons.httpclient.params</td>
<td>
<ul>
<li>org.apache.commons.httpclient</li>
<li>org.apache.commons.httpclient.util</li>
<li>org.apache.commons.httpclient</li>
</ul>
</td>
</tr>
<tr>
<td>org.apache.commons.httpclient.protocol</td>
<td>
<ul>
<li>org.apache.commons.httpclient.util</li>
<li>org.apache.commons.httpclient</li>
<li>org.apache.commons.httpclient.util</li>
</ul>
</td>
</tr>
<tr>
<td>org.apache.commons.httpclient.util</td>
<td>
<ul>
<li>org.apache.commons.httpclient</li>
<li>org.apache.commons.httpclient.util</li>
</ul>
</td>
</tr>
</tbody>
</table>

<a id="jdepend-report--explanations"></a>

## Explanations

[
[summary](#jdepend-report--summary)] [
[packages](#jdepend-report--packages)] [
[cycles](#jdepend-report--cycles)] [
[explanations](#jdepend-report--explanations)]

The following explanations are for quick reference and are lifted directly from the original
[JDepend documentation](http://www.clarkware.com/software/JDepend.html "External Link").

| Term | Description |
| --- | --- |
| Number of Classes | The number of concrete and abstract classes (and interfaces) in the package is an indicator of the extensibility of the package. |
| Afferent Couplings | The number of other packages that depend upon classes within the package is an indicator of the package's responsibility. |
| Efferent Couplings | The number of other packages that the classes in the package depend upon is an indicator of the package's independence. |
| Abstractness | The ratio of the number of abstract classes (and interfaces) in the analyzed package to the total number of classes in the analyzed package. The range for this metric is 0 to 1, with A=0 indicating a completely concrete package and A=1 indicating a completely abstract package. |
| Instability | The ratio of efferent coupling (Ce) to total coupling (Ce / (Ce + Ca)). This metric is an indicator of the package's resilience to change. The range for this metric is 0 to 1, with I=0 indicating a completely stable package and I=1 indicating a completely instable package. |
| Distance | The perpendicular distance of a package from the idealized line A + I = 1. This metric is an indicator of the package's balance between abstractness and stability. A package squarely on the main sequence is optimally balanced with respect to its abstractness and stability. Ideal packages are either completely abstract and stable (x=0, y=1) or completely concrete and instable (x=1, y=0). The range for this metric is 0 to 1, with D=0 indicating a package that is coincident with the main sequence and D=1 indicating a package that is as far from the main sequence as possible. |
| Cycles | Packages participating in a package dependency cycle are in a deadly embrace with respect to reusability and their release cycle. Package dependency cycles can be easily identified by reviewing the textual reports of dependency cycles. Once these dependency cycles have been identified with JDepend, they can be broken by employing various object-oriented techniques. |

---

<a id="development-process"></a>

<!-- source_url: https://hc.apache.org/httpclient-legacy/development-process.html -->

<!-- page_index: 21 -->

<a id="development-process--development-process"></a>

## Development Process

[http://maven.apache.org/development-process.html](http://maven.apache.org/development-process.html "External Link")

---
