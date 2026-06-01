# Commons Email – Project Information

## Navigation

- Email
  - [Overview](#index)
  - [User guide](#userguide)
  - [Security Reports](#security-reports)
- Development
  - [Building](#building)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Project Modules](#modules)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Other pages
  - [Apache Commons Email Bill of Materials – CI Management](#commons-email2-bom-ci-management)
  - [Apache Commons Email Bill of Materials – About](#commons-email2-bom)
  - [Apache Commons Email Bill of Materials – Source Code Management](#commons-email2-bom-scm)
  - [Apache Commons Email Bill of Materials – Project Summary](#commons-email2-bom-summary)
  - [Apache Commons Email Bill of Materials – Project Team](#commons-email2-bom-team)
  - [Apache Commons Email Core – CI Management](#commons-email2-core-ci-management)
  - [Apache Commons Email Core – About](#commons-email2-core)
  - [Apache Commons Email Core – Source Code Management](#commons-email2-core-scm)
  - [Apache Commons Email Core – Project Summary](#commons-email2-core-summary)
  - [Apache Commons Email Core – Project Team](#commons-email2-core-team)
  - [Apache Commons Email Distribution – CI Management](#commons-email2-distribution-ci-management)
  - [Apache Commons Email Distribution – About](#commons-email2-distribution)
  - [Apache Commons Email Distribution – Source Code Management](#commons-email2-distribution-scm)
  - [Apache Commons Email Distribution – Project Summary](#commons-email2-distribution-summary)
  - [Apache Commons Email Distribution – Project Team](#commons-email2-distribution-team)
  - [Apache Commons Email for Jakarta – CI Management](#commons-email2-jakarta-ci-management)
  - [Apache Commons Email for Jakarta – About](#commons-email2-jakarta)
  - [Apache Commons Email for Jakarta – Source Code Management](#commons-email2-jakarta-scm)
  - [Apache Commons Email for Jakarta – Project Summary](#commons-email2-jakarta-summary)
  - [Apache Commons Email for Jakarta – Project Team](#commons-email2-jakarta-team)
  - [Apache Commons Email for Javax – CI Management](#commons-email2-javax-ci-management)
  - [Apache Commons Email for Javax – About](#commons-email2-javax)
  - [Apache Commons Email for Javax – Source Code Management](#commons-email2-javax-scm)
  - [Apache Commons Email for Javax – Project Summary](#commons-email2-javax-summary)
  - [Apache Commons Email for Javax – Project Team](#commons-email2-javax-team)
  - [Commons Email – Apache Commons Email Parent POM Issue tracking](#issue-tracking)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-email"></a>

## Commons Email

Commons Email aims to provide a API for sending email.
It is built on top of the Java Mail API, which it aims to simplify.

You must choose between the Javax `org.apache.commons:commons-email2-javax` or
Jakarta `org.apache.commons:commons-email2-jakarta` implementation. Either one
will bring in the Core `org.apache.commons:commons-email2-core` module when using Maven.

See the [modules](#modules) page.

Some of the mail classes that are provided are as follows:

- **SimpleEmail**
  -
  This class is used to send basic text based emails.
- **MultiPartEmail**
  -
  This class is used to send multipart messages.
  This allows a text message with attachments either inline or attached.
- **HtmlEmail**
  -
  This class is used to send HTML formatted emails.
  It has all of the capabilities as MultiPartEmail allowing attachments to be easily added.
  It also supports embedded images.
- **ImageHtmlEmail**
  -
  This class is used to send HTML formatted emails with inline images.
  It has all of the capabilities as HtmlEmail but transform all image
  references to inline images.
- **EmailAttachment**
  -
  This is a simple container class to allow for easy handling of attachments.
  It is for use with instances of MultiPartEmail and HtmlEmail.

<a id="index--documentation"></a>

## Documentation

The
[Commons Email User Guide](#userguide)
covers many
typical cases and provides several useful examples.

The Javadoc API documents are available online:

- [Javadoc for Core](https://commons.apache.org/proper/commons-email/commons-email2-core/apidocs/index.html)
- [Javadoc for Jakarta](https://commons.apache.org/proper/commons-email/commons-email2-jakarta/apidocs/index.html)
- [Javadoc for Javax](https://commons.apache.org/proper/commons-email/commons-email2-javax/apidocs/index.html)
- [Javadoc 2.x Core Archive](https://javadoc.io/doc/org.apache.commons/commons-email2-core/latest/index.html)
- [Javadoc 2.x Jakarta Archive](https://javadoc.io/doc/org.apache.commons/commons-email-jakarta/latest/index.html)
- [Javadoc 2.x Javax Archive](https://javadoc.io/doc/org.apache.commons/commons-email-javax/latest/index.html)
- [Javadoc 1.x Archive](https://javadoc.io/doc/org.apache.commons/commons-email/latest/index.html)

The
[git repository](#scm)
can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-email.git).

<a id="index--releases"></a>

## Releases

The latest version requires Java 8 -
[Download now!](https://commons.apache.org/email/download_email.cgi)
The full
[change log](https://commons.apache.org/proper/commons-email/changes-report.html)
is available

For previous releases, see the [Apache Archive](https://archive.apache.org/dist/commons/email/).

<a id="index--support"></a>

## Support

The
[commons mailing lists](https://commons.apache.org/proper/commons-email/mail-lists.html)
act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [email].

Issues may be reported via [ASF JIRA](#issue-tracking).

---

<a id="userguide"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/userguide.html -->

<!-- page_index: 2 -->

<a id="userguide--choose-an-implementation"></a>

## Choose an implementation

You must choose between the Javax `org.apache.commons:commons-email2-javax` or
Jakarta `org.apache.commons:commons-email2-jakarta` implementation. Either one
will bring in the Core `org.apache.commons:commons-email2-core` module when using
Maven.

<a id="userguide--a-simple-text-email"></a>

## A simple text email

Our first example will create a basic email message to "John Doe" and
send it through your Google Mail (GMail) account.

```


Email email = new SimpleEmail();
email.setHostName("smtp.googlemail.com");
email.setSmtpPort(465);
email.setAuthenticator(new DefaultAuthenticator("username", "password"));
email.setSSLOnConnect(true);
email.setFrom("user@gmail.com");
email.setSubject("TestMail");
email.setMsg("This is a test mail ... :-)");
email.addTo("foo@bar.com");
email.send();
```

The call to setHostName("mail.myserver.com") sets the address of the
outgoing SMTP server that will be used to send the message. If this is
not set, the system property "mail.host" will be used.

<a id="userguide--sending-emails-with-attachments"></a>

## Sending emails with attachments

To add attachments to an email, you will need to use the MultiPartEmail
class. This class works just like SimpleEmail except that it adds
several overloaded attach() methods to add attachments to the email.
You can add an unlimited number of attachments either inline or
attached. The attachments will be MIME encoded.

The simplest way to add the attachments is by using the EmailAttachment
class to reference your attachments.

In the following example, we will create an attachment for a picture.
We will then attach the picture to the email and send it.

```


import org.apache.commons.mail2.core.*;
...
import org.apache.commons.mail2.jakarta.*;
// or
import org.apache.commons.mail2.javax.*;
...

  // Create the attachment
  EmailAttachment attachment = new EmailAttachment();
  attachment.setPath("mypictures/john.jpg");
  attachment.setDisposition(EmailAttachment.ATTACHMENT);
  attachment.setDescription("Picture of John");
  attachment.setName("John");

  // Create the email message
  MultiPartEmail email = new MultiPartEmail();
  email.setHostName("mail.myserver.com");
  email.addTo("jdoe@somewhere.org", "John Doe");
  email.setFrom("me@apache.org", "Me");
  email.setSubject("The picture");
  email.setMsg("Here is the picture you wanted");

  // add the attachment
  email.attach(attachment);

  // send the email
  email.send();
```

You can also use EmailAttachment to reference any valid URL for files
that you do not have locally. When the message is sent, the file will
be downloaded and attached to the message automatically.

The next example shows how we could have sent the apache logo
to John instead.

```


import org.apache.commons.mail2.core.*;
...
import org.apache.commons.mail2.jakarta.*;
// or
import org.apache.commons.mail2.javax.*;
...

  // Create the attachment
  EmailAttachment attachment = new EmailAttachment();
  attachment.setURL(new URL("http://www.apache.org/images/asf_logo_wide.gif"));
  attachment.setDisposition(EmailAttachment.ATTACHMENT);
  attachment.setDescription("Apache logo");
  attachment.setName("Apache logo");

  // Create the email message
  MultiPartEmail email = new MultiPartEmail();
  email.setHostName("mail.myserver.com");
  email.addTo("jdoe@somewhere.org", "John Doe");
  email.setFrom("me@apache.org", "Me");
  email.setSubject("The logo");
  email.setMsg("Here is Apache's logo");
  
  // add the attachment
  email.attach(attachment);

  // send the email
  email.send();
```

<a id="userguide--sending-html-formatted-email"></a>

## Sending HTML formatted email

Sending HTML formatted email is accomplished by using the HtmlEmail
class. This class works exactly like the MultiPartEmail class with
additional methods to set the html content, alternative text content
if the recipient does not support HTML email, and add inline images.

In this example, we will send an email message with formatted HTML
content with an inline image.

```


import org.apache.commons.mail.HtmlEmail;
...

  // Create the email message
  HtmlEmail email = new HtmlEmail();
  email.setHostName("mail.myserver.com");
  email.addTo("jdoe@somewhere.org", "John Doe");
  email.setFrom("me@apache.org", "Me");
  email.setSubject("Test email with inline image");
  
  // embed the image and get the content id
  URL url = new URL("http://www.apache.org/images/asf_logo_wide.gif");
  String cid = email.embed(url, "Apache logo");
  
  // set the html message
  email.setHtmlMsg("<html>The apache logo - <img src=\"cid:"+cid+"\"></html>");

  // set the alternative message
  email.setTextMsg("Your email client does not support HTML messages");

  // send the email
  email.send();
```

First, notice that the call to embed() returns a String. This String
is a randomly generated identifier that must be used to reference
the image in the image tag.

Next, there was no call to setMsg() in this example. The method is
still available in HtmlEmail but it should not be used if you will be
using inline images. Instead, the setHtmlMsg() and setTextMsg()
methods were used.

<a id="userguide--sending-html-formatted-email-with-embedded-images"></a>

## Sending HTML formatted email with embedded images

The previous example showed how to create a HTML email with embedded
images but you need to know all images upfront which is inconvenient
when using a HTML email template. The ImageHtmlEmail helps you
solving this problem by converting all external images to inline
images.

```

        
import org.apache.commons.mail2.core.*;
...
import org.apache.commons.mail2.jakarta.*;
// or
import org.apache.commons.mail2.javax.*;
...

  // load your HTML email template
  String htmlEmailTemplate = ".... <img src=\"http://www.apache.org/images/feather.gif\"> ....";

  // define you base URL to resolve relative resource locations
  URL url = new URL("http://www.apache.org");

  // create the email message
  ImageHtmlEmail email = new ImageHtmlEmail();
  email.setDataSourceResolver(new DataSourceUrlResolver(url));
  email.setHostName("mail.myserver.com");
  email.addTo("jdoe@somewhere.org", "John Doe");
  email.setFrom("me@apache.org", "Me");
  email.setSubject("Test email with inline image");
  
  // set the html message
  email.setHtmlMsg(htmlEmailTemplate);

  // set the alternative message
  email.setTextMsg("Your email client does not support HTML messages");

  // send the email
  email.send();
  
```

First we create a HTML email template referencing some images. All
referenced images are automatically transformed to inline images by
the specified DataSourceResolver.

<a id="userguide--debugging"></a>

## Debugging

The JavaMail API supports a debugging option that will can be very
useful if you run into problems. You can activate debugging on any
of the mail classes by calling setDebug(true). The debugging output
will be written to `System.out`.

Sometimes you want to experiment with various security setting or
features of commons-email. A good starting point is the test class
`EmailLiveTest` and `EmailConfiguration` which
are used for testing commons-email with real SMTP servers.

<a id="userguide--authentication"></a>

## Authentication

If you need to authenticate to your SMTP server, you can call the
`setAuthentication(userName,password)` method before sending
your email. This will create an instance of
`DefaultAuthenticator` which will be used by the JavaMail
API when the email is sent. Your server must support RFC2554 in
order for this to work.

You can perform a more complex authentication method such as displaying
a dialog box to the user by creating a subclass of the
`javax.mail.Authenticator` object. You will need to
override the `getPasswordAuthentication()` method where
you will handle collecting the user's information. To make use of
your new `Authenticator` class, use the
`Email.setAuthenticator` method.

<a id="userguide--security"></a>

## Security

Nowadays you should not use plain SMTP protocol when using public SMTP servers
but there is a some confusion regarding the available options.

Two commons options are using

- STARTTLS on port 25
- SSL on port 465

The following definitions were taken from Wikipedia

- STARTTLS is an extension to plain text communication protocols, which offers a
  way to upgrade a plain text connection to an encrypted (TLS or SSL) connection
  instead of using a separate port for encrypted communication.
- Transport Layer Security (TLS) and its predecessor, Secure Sockets Layer (SSL),
  are cryptographic protocols that provide communication security over the
  Internet.TLS and SSL encrypt the segments of network connections above the
  Transport Layer, using asymmetric cryptography for key exchange, symmetric
  encryption for privacy, and message authentication codes for message integrity.

In addition you can force the following security checks (which are disabled by default)

- When using a secured transport (STARTTLS or SSL) you can force validating the server's
  certificate by calling `Email.setSSLCheckServerIdentity(true)`.
- Enforce using STARTTLS by calling `Email.setStartTLSRequired(true)`

<a id="userguide--handling-bounced-messages"></a>

## Handling Bounced Messages

Normally, messages which cannot be delivered to a recipient are returned to the
sender (specified with the `from` property). However, in some cases, you'll want these to be sent to a different address. To do this, simply call the
`setBounceAddress(emailAddressString)` method before sending
your email.

Technical notes: When SMTP servers cannot deliver mail, they do not pay any attention
to the contents of the message to determine where the error notification should be
sent. Rather, they refer to the SMTP "envelope sender" value. JavaMail sets this
value according to the value of the `mail.smtp.from` property on the
JavaMail `Session`. (Commons Email initializes the JavaMail
`Session` using `System.getProperties()`)
If this property has not been set, then JavaMail
uses the "from" address. If your email bean has the `bounceAddress`
property set, then Commons Email uses it to set the value of `mail.smtp.from`
when the `Session` is initialized, overriding any other value
which might have been set.

*Note:*  This is the only way to control the handling of bounced email.
Specifically, the "Errors-to:" SMTP header is deprecated and cannot be trusted
to control how a bounced message will be handled. Also note that it is considered bad
practice to send email with an untrusted "from" address unless you also set the
bounce address. If your application allows users to enter an address which is used
as the "from" address on an email, you should be sure to set the bounce address
to a known good address.

---

<a id="security-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/security-reports.html -->

<!-- page_index: 3 -->

<a id="security-reports--general-information"></a>

## General Information

For information about reporting or asking questions about
security problems, please see the [security page
of the Commons project](https://commons.apache.org/security.html).

<a id="security-reports--apache-commons-email-security-vulnerabilities"></a>

## Apache Commons Email Security Vulnerabilities

This page lists all security vulnerabilities fixed in
released versions of Apache Commons Email. Each
vulnerability is given a security impact rating by the
development team - please note that this rating may vary from
platform to platform. We also list the versions of Commons
Email the flaw is known to affect, and where a flaw has not
been verified list the version with a question mark.

Please note that binary patches are never provided. If you
need to apply a source code patch, use the building
instructions for the Commons Email version that you are
using.

If you need help on building Commons Email or other help
on following the instructions to mitigate the known
vulnerabilities listed here, please send your questions to the
public [Commons Users mailing
list](https://commons.apache.org/proper/commons-email/mail-lists.html).

If you have encountered an unlisted security vulnerability
or other unexpected behavior that has security impact, or if
the descriptions here are incomplete, please report them
privately to the Apache Security Team. Thank you.

<a id="security-reports--fixed-in-apache-commons-email-1.5"></a>

### Fixed in Apache Commons Email 1.5

**Low: SMTP header injection vulnerabilty** [CVE-2017-9801](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-9801)

When passing text that contains line-breaks as the
subject of an email arbitrary SMTP headers can be added.

This was fixed in revisions
[1801385](https://svn.apache.org/viewvc?view=revision&revision=1801385)
[1801388](https://svn.apache.org/viewvc?view=revision&revision=1801388) and
[1801389](https://svn.apache.org/viewvc?view=revision&revision=1801389).

This was first reported to the Security Team on 27 June
2017 and made public on 1 August 2017.

Affects: 1.0 - 1.4

**Moderate: Insufficient input validation for bounce address**
[CVE-2018-1294](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-1294)

When passing text that contains line-breaks as the bounce address of an Email, then
the email details (SMTP headers, recipient list, contents) can be manipulated.

This was fixed in revisions
[1777030](https://svn.apache.org/viewvc?view=revision&revision=1777030)

This was first reported to the Security Team on 02-Sep-2016 and made public on 26-Jan-2018.

Affects: 1.0-1.4

<a id="security-reports--errors-and-ommissions"></a>

## Errors and Ommissions

Please report any errors or omissions to [the dev mailing list](https://commons.apache.org/proper/commons-email/mail-lists.html).

---

<a id="building"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/building.html -->

<!-- page_index: 4 -->

<a id="building--overview"></a>

## Overview

Commons Email uses
[Maven](http://maven.apache.org).

<a id="building--maven-goals"></a>

## Maven Goals

To build a jar and verify all files, change into Email's root directory and run `mvn`.
The result will be in the "target" subdirectory.

To only build the jar file, change into Email's root directory and run `mvn clean package`.
The result will be in the "target" subdirectory.

To only build the Javadocs, run "mvn clean javadoc:javadoc".
The result will be in "target/docs/apidocs".

To build the full website, run "mvn clean verify site".
The result will be in "target/site".
You must be using JDK 5 or higher to successfully complete this target.

<a id="building--development"></a>

## Development

Commons Email requires Java 8.

Commons Email requires
[SubEtha SMTP](http://code.google.com/p/subethasmtp/)
for its unit tests.

This jar will be automatically installed to your local Maven repository
if you build using `mvn clean install`.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/project-info.html -->

<!-- page_index: 5 -->

<a id="project-info--project-information"></a>

## Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](http://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

### Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Email provides an API for sending email, simplifying the JavaMail API. |
| [Summary](#summary) | This document lists other related information of this project |
| [Project Modules](#modules) | This document lists the modules (sub-projects) of this project. |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-email/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-email/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Dependency Information](https://commons.apache.org/proper/commons-email/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-email/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-email/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-email/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/summary.html -->

<!-- page_index: 6 -->

<a id="summary--project-summary"></a>

## Project Summary

<a id="summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Email Parent POM |
| Description | Apache Commons Email provides an API for sending email, simplifying the JavaMail API. |
| Homepage | [https://commons.apache.org/proper/commons-email/](#index) |

<a id="summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-email2-parent |
| Version | 2.0.0-M1 |
| Type | pom |

---

<a id="modules"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/modules.html -->

<!-- page_index: 7 -->

<a id="modules--project-modules"></a>

## Project Modules

This project has declared the following modules:

| Name | Description |
| --- | --- |
| [Apache Commons Email Core](#commons-email2-core) | Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API. |
| [Apache Commons Email for Jakarta](#commons-email2-jakarta) | Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API. |
| [Apache Commons Email for Javax](#commons-email2-javax) | Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API. |
| [Apache Commons Email Bill of Materials](#commons-email2-bom) | This Bill of Materials POM can be used to ease dependency management when referencing multiple artifacts using Maven. |
| [Apache Commons Email Distribution](#commons-email2-distribution) | Apache Commons Email Distribution archives. |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/team.html -->

<!-- page_index: 8 -->

<a id="team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/cdb8b39b4d3afa6be1e2cda37f75f880?d=mm&s=60) | dion | dIon Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/28206b147858407d3246a39215067866?d=mm&s=60) | jmcnally | John McNally | [jmcnally@collab.net](mailto:jmcnally@collab.net) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/ab858863fac6e5a02e2e5df7f9949e22?d=mm&s=60) | quintonm | Quinton McCombs | [quintonm@bellsouth.net](mailto:quintonm@bellsouth.net) | - | NequalsOne, LLC. | - | - | - |
| ![](https://www.gravatar.com/avatar/9cd154bd87385c597d95250177e5bca6?d=mm&s=60) | epugh | Eric Pugh | [epugh@opensourceconnections.com](mailto:epugh@opensourceconnections.com) | - | OpenSource Connections | - | - | - |
| ![](https://www.gravatar.com/avatar/cd55fa3f775b72fc74b6ba6fc9507edc?d=mm&s=60) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/134d9d61c91768c5addfd9e9d9a0bbac?d=mm&s=60) | jon | Jon Scott Stevens | [jon@latchkey.com](mailto:jon@latchkey.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/1380eb1a41b8e20bad1128bac1031402?d=mm&s=60) | jvanzyl | Jason van Zyl | [jason@zenplex.com](mailto:jason@zenplex.com) | - | Zenplex | - | - | - |
| ![](https://www.gravatar.com/avatar/e7daec2f9052c7c1690422d0d74c3b7d?d=mm&s=60) | germuska | Joe Germuska | [Joe@Germuska.com](mailto:Joe@Germuska.com) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/30f9094d5dbe2ce93f1a41afc9615b83?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/126d93a0374e9fa5faa40527b2faa177?d=mm&s=60) | henning | Henning P. Schmiedehausen | [hps@intermeta.de](mailto:hps@intermeta.de) | - | INTERMETA - Gesellschaft fuer Mehrwertdienste mbH | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | scolebourne | Stephen Colebourne | - | - | - | - | - | 0 |
| ![](https://www.gravatar.com/avatar/abebbde126a07a66094d738d1a3af445?d=mm&s=60) | bspeakmon | Ben Speakmon | [bspeakmon@apache.org](mailto:bspeakmon@apache.org) | - | The Apache Software Foundation | - | Java Developer | -8 |
| ![](https://www.gravatar.com/avatar/a393af16a299976c4336f7432d89ab79?d=mm&s=60) | sgoeschl | Siegfried Goeschl | [sgoeschl@apache.org](mailto:sgoeschl@apache.org) | - | - | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/bacbd457de9bc401c902be783f92d417?d=mm&s=60) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Bindul Bhowmik | - |
| ![](https://www.gravatar.com/avatar/2b54253c7b59be6bba7024152b96e5ac?d=mm&s=60) | Colin Chalmers | [colin.chalmers@maxware.nl](mailto:colin.chalmers@maxware.nl) |
| ![](https://www.gravatar.com/avatar/785d62a87031b0e0ba12a620ddd33e39?d=mm&s=60) | Frank Y. Kim | [frank.kim@clearink.com](mailto:frank.kim@clearink.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Regis Koenig | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Stephen Kruger | - |
| ![](https://www.gravatar.com/avatar/89747060222d94162c69b432cea5189d?d=mm&s=60) | Sean Legassick | [sean@informage.net](mailto:sean@informage.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Andrew Liles | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Cedrik Lime | - |
| ![](https://www.gravatar.com/avatar/43f0936289be0f4857d0b38a8705e34a?d=mm&s=60) | Mark Lowe | [mark.lowe@boxstuff.com](mailto:mark.lowe@boxstuff.com) |
| ![](https://www.gravatar.com/avatar/99a2de4b67388abdaf13ca4627398a7d?d=mm&s=60) | Brett McLaughlin | [bmclaugh@algx.net](mailto:bmclaugh@algx.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Piero Ottuzzi | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Niall Pemberton | - |
| ![](https://www.gravatar.com/avatar/0b28160da341f2aca1ab94d78c438f57?d=mm&s=60) | Greg Ritter | [greg@shwoop.com](mailto:greg@shwoop.com) |
| ![](https://www.gravatar.com/avatar/b30da618a502d63ba0ae4736799ad0ef?d=mm&s=60) | Corey Scott | [corey.scott@gmail.com](mailto:corey.scott@gmail.com) |
| ![](https://www.gravatar.com/avatar/cf1a8f7cce5d2e829561e6d3081e0777?d=mm&s=60) | Eric Spiegelberg | [eric@spiegs.com](mailto:eric@spiegs.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Dominik Stadler | - |
| ![](https://www.gravatar.com/avatar/cc058d8d4bde1b49e2654d79981be257?d=mm&s=60) | Matthias Wessendorf | [matthias@wessendorf.net](mailto:matthias@wessendorf.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Brandon Wolfe | - |
| ![](https://www.gravatar.com/avatar/3beea937ea4cc3017325d006a52bfa9f?d=mm&s=60) | Alexander Lehmann | [alexlehm@gmail.com](mailto:alexlehm@gmail.com) |
| ![](https://www.gravatar.com/avatar/15f2e307ebe1eccbd816d4ce5bfd573b?d=mm&s=60) | Vegard Stuen | [vegard.stuen@gmail.com](mailto:vegard.stuen@gmail.com) |

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/scm.html -->

<!-- page_index: 9 -->

<a id="scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-email
```

<a id="scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email
```

<a id="scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email
```

<a id="scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/ci-management.html -->

<!-- page_index: 10 -->

<a id="ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-email2-bom-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-bom/ci-management.html -->

<!-- page_index: 11 -->

<a id="commons-email2-bom-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-email2-bom-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-email2-bom-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-email2-bom"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-bom/index.html -->

<!-- page_index: 12 -->

<a id="commons-email2-bom--about-apache-commons-email-bill-of-materials"></a>

## About Apache Commons Email Bill of Materials

This Bill of Materials POM can be used to ease dependency management when referencing multiple artifacts using Maven.

---

<a id="commons-email2-bom-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-bom/scm.html -->

<!-- page_index: 13 -->

<a id="commons-email2-bom-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-email2-bom-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-email/commons-email2-bom
```

<a id="commons-email2-bom-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-bom
```

<a id="commons-email2-bom-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-bom
```

<a id="commons-email2-bom-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-email2-bom-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-bom/summary.html -->

<!-- page_index: 14 -->

<a id="commons-email2-bom-summary--project-summary"></a>

## Project Summary

<a id="commons-email2-bom-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Email Bill of Materials |
| Description | This Bill of Materials POM can be used to ease dependency management when referencing multiple artifacts using Maven. |
| Homepage | [https://commons.apache.org/proper/commons-email/commons-email2-bom/](#commons-email2-bom) |

<a id="commons-email2-bom-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-email2-bom-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-email2-bom |
| Version | 2.0.0-M1 |
| Type | pom |

---

<a id="commons-email2-bom-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-bom/team.html -->

<!-- page_index: 15 -->

<a id="commons-email2-bom-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-email2-bom-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/cdb8b39b4d3afa6be1e2cda37f75f880?d=mm&s=60) | dion | dIon Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/28206b147858407d3246a39215067866?d=mm&s=60) | jmcnally | John McNally | [jmcnally@collab.net](mailto:jmcnally@collab.net) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/ab858863fac6e5a02e2e5df7f9949e22?d=mm&s=60) | quintonm | Quinton McCombs | [quintonm@bellsouth.net](mailto:quintonm@bellsouth.net) | - | NequalsOne, LLC. | - | - | - |
| ![](https://www.gravatar.com/avatar/9cd154bd87385c597d95250177e5bca6?d=mm&s=60) | epugh | Eric Pugh | [epugh@opensourceconnections.com](mailto:epugh@opensourceconnections.com) | - | OpenSource Connections | - | - | - |
| ![](https://www.gravatar.com/avatar/cd55fa3f775b72fc74b6ba6fc9507edc?d=mm&s=60) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/134d9d61c91768c5addfd9e9d9a0bbac?d=mm&s=60) | jon | Jon Scott Stevens | [jon@latchkey.com](mailto:jon@latchkey.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/1380eb1a41b8e20bad1128bac1031402?d=mm&s=60) | jvanzyl | Jason van Zyl | [jason@zenplex.com](mailto:jason@zenplex.com) | - | Zenplex | - | - | - |
| ![](https://www.gravatar.com/avatar/e7daec2f9052c7c1690422d0d74c3b7d?d=mm&s=60) | germuska | Joe Germuska | [Joe@Germuska.com](mailto:Joe@Germuska.com) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/30f9094d5dbe2ce93f1a41afc9615b83?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/126d93a0374e9fa5faa40527b2faa177?d=mm&s=60) | henning | Henning P. Schmiedehausen | [hps@intermeta.de](mailto:hps@intermeta.de) | - | INTERMETA - Gesellschaft fuer Mehrwertdienste mbH | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | scolebourne | Stephen Colebourne | - | - | - | - | - | 0 |
| ![](https://www.gravatar.com/avatar/abebbde126a07a66094d738d1a3af445?d=mm&s=60) | bspeakmon | Ben Speakmon | [bspeakmon@apache.org](mailto:bspeakmon@apache.org) | - | The Apache Software Foundation | - | Java Developer | -8 |
| ![](https://www.gravatar.com/avatar/a393af16a299976c4336f7432d89ab79?d=mm&s=60) | sgoeschl | Siegfried Goeschl | [sgoeschl@apache.org](mailto:sgoeschl@apache.org) | - | - | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/bacbd457de9bc401c902be783f92d417?d=mm&s=60) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="commons-email2-bom-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Bindul Bhowmik | - |
| ![](https://www.gravatar.com/avatar/2b54253c7b59be6bba7024152b96e5ac?d=mm&s=60) | Colin Chalmers | [colin.chalmers@maxware.nl](mailto:colin.chalmers@maxware.nl) |
| ![](https://www.gravatar.com/avatar/785d62a87031b0e0ba12a620ddd33e39?d=mm&s=60) | Frank Y. Kim | [frank.kim@clearink.com](mailto:frank.kim@clearink.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Regis Koenig | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Stephen Kruger | - |
| ![](https://www.gravatar.com/avatar/89747060222d94162c69b432cea5189d?d=mm&s=60) | Sean Legassick | [sean@informage.net](mailto:sean@informage.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Andrew Liles | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Cedrik Lime | - |
| ![](https://www.gravatar.com/avatar/43f0936289be0f4857d0b38a8705e34a?d=mm&s=60) | Mark Lowe | [mark.lowe@boxstuff.com](mailto:mark.lowe@boxstuff.com) |
| ![](https://www.gravatar.com/avatar/99a2de4b67388abdaf13ca4627398a7d?d=mm&s=60) | Brett McLaughlin | [bmclaugh@algx.net](mailto:bmclaugh@algx.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Piero Ottuzzi | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Niall Pemberton | - |
| ![](https://www.gravatar.com/avatar/0b28160da341f2aca1ab94d78c438f57?d=mm&s=60) | Greg Ritter | [greg@shwoop.com](mailto:greg@shwoop.com) |
| ![](https://www.gravatar.com/avatar/b30da618a502d63ba0ae4736799ad0ef?d=mm&s=60) | Corey Scott | [corey.scott@gmail.com](mailto:corey.scott@gmail.com) |
| ![](https://www.gravatar.com/avatar/cf1a8f7cce5d2e829561e6d3081e0777?d=mm&s=60) | Eric Spiegelberg | [eric@spiegs.com](mailto:eric@spiegs.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Dominik Stadler | - |
| ![](https://www.gravatar.com/avatar/cc058d8d4bde1b49e2654d79981be257?d=mm&s=60) | Matthias Wessendorf | [matthias@wessendorf.net](mailto:matthias@wessendorf.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Brandon Wolfe | - |
| ![](https://www.gravatar.com/avatar/3beea937ea4cc3017325d006a52bfa9f?d=mm&s=60) | Alexander Lehmann | [alexlehm@gmail.com](mailto:alexlehm@gmail.com) |
| ![](https://www.gravatar.com/avatar/15f2e307ebe1eccbd816d4ce5bfd573b?d=mm&s=60) | Vegard Stuen | [vegard.stuen@gmail.com](mailto:vegard.stuen@gmail.com) |

---

<a id="commons-email2-core-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-core/ci-management.html -->

<!-- page_index: 16 -->

<a id="commons-email2-core-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-email2-core-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-email2-core-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-email2-core"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-core/index.html -->

<!-- page_index: 17 -->

<a id="commons-email2-core--about-apache-commons-email-core"></a>

## About Apache Commons Email Core

Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API.

---

<a id="commons-email2-core-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-core/scm.html -->

<!-- page_index: 18 -->

<a id="commons-email2-core-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-email2-core-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-email/commons-email2-core
```

<a id="commons-email2-core-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-core
```

<a id="commons-email2-core-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-core
```

<a id="commons-email2-core-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-email2-core-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-core/summary.html -->

<!-- page_index: 19 -->

<a id="commons-email2-core-summary--project-summary"></a>

## Project Summary

<a id="commons-email2-core-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Email Core |
| Description | Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API. |
| Homepage | [https://commons.apache.org/proper/commons-email/commons-email2-core/](#commons-email2-core) |

<a id="commons-email2-core-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-email2-core-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-email2-core |
| Version | 2.0.0-M1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-email2-core-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-core/team.html -->

<!-- page_index: 20 -->

<a id="commons-email2-core-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-email2-core-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/cdb8b39b4d3afa6be1e2cda37f75f880?d=mm&s=60) | dion | dIon Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/28206b147858407d3246a39215067866?d=mm&s=60) | jmcnally | John McNally | [jmcnally@collab.net](mailto:jmcnally@collab.net) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/ab858863fac6e5a02e2e5df7f9949e22?d=mm&s=60) | quintonm | Quinton McCombs | [quintonm@bellsouth.net](mailto:quintonm@bellsouth.net) | - | NequalsOne, LLC. | - | - | - |
| ![](https://www.gravatar.com/avatar/9cd154bd87385c597d95250177e5bca6?d=mm&s=60) | epugh | Eric Pugh | [epugh@opensourceconnections.com](mailto:epugh@opensourceconnections.com) | - | OpenSource Connections | - | - | - |
| ![](https://www.gravatar.com/avatar/cd55fa3f775b72fc74b6ba6fc9507edc?d=mm&s=60) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/134d9d61c91768c5addfd9e9d9a0bbac?d=mm&s=60) | jon | Jon Scott Stevens | [jon@latchkey.com](mailto:jon@latchkey.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/1380eb1a41b8e20bad1128bac1031402?d=mm&s=60) | jvanzyl | Jason van Zyl | [jason@zenplex.com](mailto:jason@zenplex.com) | - | Zenplex | - | - | - |
| ![](https://www.gravatar.com/avatar/e7daec2f9052c7c1690422d0d74c3b7d?d=mm&s=60) | germuska | Joe Germuska | [Joe@Germuska.com](mailto:Joe@Germuska.com) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/30f9094d5dbe2ce93f1a41afc9615b83?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/126d93a0374e9fa5faa40527b2faa177?d=mm&s=60) | henning | Henning P. Schmiedehausen | [hps@intermeta.de](mailto:hps@intermeta.de) | - | INTERMETA - Gesellschaft fuer Mehrwertdienste mbH | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | scolebourne | Stephen Colebourne | - | - | - | - | - | 0 |
| ![](https://www.gravatar.com/avatar/abebbde126a07a66094d738d1a3af445?d=mm&s=60) | bspeakmon | Ben Speakmon | [bspeakmon@apache.org](mailto:bspeakmon@apache.org) | - | The Apache Software Foundation | - | Java Developer | -8 |
| ![](https://www.gravatar.com/avatar/a393af16a299976c4336f7432d89ab79?d=mm&s=60) | sgoeschl | Siegfried Goeschl | [sgoeschl@apache.org](mailto:sgoeschl@apache.org) | - | - | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/bacbd457de9bc401c902be783f92d417?d=mm&s=60) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="commons-email2-core-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Bindul Bhowmik | - |
| ![](https://www.gravatar.com/avatar/2b54253c7b59be6bba7024152b96e5ac?d=mm&s=60) | Colin Chalmers | [colin.chalmers@maxware.nl](mailto:colin.chalmers@maxware.nl) |
| ![](https://www.gravatar.com/avatar/785d62a87031b0e0ba12a620ddd33e39?d=mm&s=60) | Frank Y. Kim | [frank.kim@clearink.com](mailto:frank.kim@clearink.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Regis Koenig | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Stephen Kruger | - |
| ![](https://www.gravatar.com/avatar/89747060222d94162c69b432cea5189d?d=mm&s=60) | Sean Legassick | [sean@informage.net](mailto:sean@informage.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Andrew Liles | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Cedrik Lime | - |
| ![](https://www.gravatar.com/avatar/43f0936289be0f4857d0b38a8705e34a?d=mm&s=60) | Mark Lowe | [mark.lowe@boxstuff.com](mailto:mark.lowe@boxstuff.com) |
| ![](https://www.gravatar.com/avatar/99a2de4b67388abdaf13ca4627398a7d?d=mm&s=60) | Brett McLaughlin | [bmclaugh@algx.net](mailto:bmclaugh@algx.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Piero Ottuzzi | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Niall Pemberton | - |
| ![](https://www.gravatar.com/avatar/0b28160da341f2aca1ab94d78c438f57?d=mm&s=60) | Greg Ritter | [greg@shwoop.com](mailto:greg@shwoop.com) |
| ![](https://www.gravatar.com/avatar/b30da618a502d63ba0ae4736799ad0ef?d=mm&s=60) | Corey Scott | [corey.scott@gmail.com](mailto:corey.scott@gmail.com) |
| ![](https://www.gravatar.com/avatar/cf1a8f7cce5d2e829561e6d3081e0777?d=mm&s=60) | Eric Spiegelberg | [eric@spiegs.com](mailto:eric@spiegs.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Dominik Stadler | - |
| ![](https://www.gravatar.com/avatar/cc058d8d4bde1b49e2654d79981be257?d=mm&s=60) | Matthias Wessendorf | [matthias@wessendorf.net](mailto:matthias@wessendorf.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Brandon Wolfe | - |
| ![](https://www.gravatar.com/avatar/3beea937ea4cc3017325d006a52bfa9f?d=mm&s=60) | Alexander Lehmann | [alexlehm@gmail.com](mailto:alexlehm@gmail.com) |
| ![](https://www.gravatar.com/avatar/15f2e307ebe1eccbd816d4ce5bfd573b?d=mm&s=60) | Vegard Stuen | [vegard.stuen@gmail.com](mailto:vegard.stuen@gmail.com) |

---

<a id="commons-email2-distribution-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-distribution/ci-management.html -->

<!-- page_index: 21 -->

<a id="commons-email2-distribution-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-email2-distribution-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-email2-distribution-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-email2-distribution"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-distribution/index.html -->

<!-- page_index: 22 -->

<a id="commons-email2-distribution--about-apache-commons-email-distribution"></a>

## About Apache Commons Email Distribution

Apache Commons Email Distribution archives.

---

<a id="commons-email2-distribution-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-distribution/scm.html -->

<!-- page_index: 23 -->

<a id="commons-email2-distribution-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-email2-distribution-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-email/commons-email2-distribution
```

<a id="commons-email2-distribution-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-distribution
```

<a id="commons-email2-distribution-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-distribution
```

<a id="commons-email2-distribution-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-email2-distribution-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-distribution/summary.html -->

<!-- page_index: 24 -->

<a id="commons-email2-distribution-summary--project-summary"></a>

## Project Summary

<a id="commons-email2-distribution-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Email Distribution |
| Description | Apache Commons Email Distribution archives. |
| Homepage | [https://commons.apache.org/proper/commons-email/commons-email2-distribution/](#commons-email2-distribution) |

<a id="commons-email2-distribution-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-email2-distribution-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-email2-distribution |
| Version | 2.0.0-M1 |
| Type | pom |

---

<a id="commons-email2-distribution-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-distribution/team.html -->

<!-- page_index: 25 -->

<a id="commons-email2-distribution-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-email2-distribution-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/cdb8b39b4d3afa6be1e2cda37f75f880?d=mm&s=60) | dion | dIon Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/28206b147858407d3246a39215067866?d=mm&s=60) | jmcnally | John McNally | [jmcnally@collab.net](mailto:jmcnally@collab.net) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/ab858863fac6e5a02e2e5df7f9949e22?d=mm&s=60) | quintonm | Quinton McCombs | [quintonm@bellsouth.net](mailto:quintonm@bellsouth.net) | - | NequalsOne, LLC. | - | - | - |
| ![](https://www.gravatar.com/avatar/9cd154bd87385c597d95250177e5bca6?d=mm&s=60) | epugh | Eric Pugh | [epugh@opensourceconnections.com](mailto:epugh@opensourceconnections.com) | - | OpenSource Connections | - | - | - |
| ![](https://www.gravatar.com/avatar/cd55fa3f775b72fc74b6ba6fc9507edc?d=mm&s=60) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/134d9d61c91768c5addfd9e9d9a0bbac?d=mm&s=60) | jon | Jon Scott Stevens | [jon@latchkey.com](mailto:jon@latchkey.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/1380eb1a41b8e20bad1128bac1031402?d=mm&s=60) | jvanzyl | Jason van Zyl | [jason@zenplex.com](mailto:jason@zenplex.com) | - | Zenplex | - | - | - |
| ![](https://www.gravatar.com/avatar/e7daec2f9052c7c1690422d0d74c3b7d?d=mm&s=60) | germuska | Joe Germuska | [Joe@Germuska.com](mailto:Joe@Germuska.com) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/30f9094d5dbe2ce93f1a41afc9615b83?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/126d93a0374e9fa5faa40527b2faa177?d=mm&s=60) | henning | Henning P. Schmiedehausen | [hps@intermeta.de](mailto:hps@intermeta.de) | - | INTERMETA - Gesellschaft fuer Mehrwertdienste mbH | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | scolebourne | Stephen Colebourne | - | - | - | - | - | 0 |
| ![](https://www.gravatar.com/avatar/abebbde126a07a66094d738d1a3af445?d=mm&s=60) | bspeakmon | Ben Speakmon | [bspeakmon@apache.org](mailto:bspeakmon@apache.org) | - | The Apache Software Foundation | - | Java Developer | -8 |
| ![](https://www.gravatar.com/avatar/a393af16a299976c4336f7432d89ab79?d=mm&s=60) | sgoeschl | Siegfried Goeschl | [sgoeschl@apache.org](mailto:sgoeschl@apache.org) | - | - | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/bacbd457de9bc401c902be783f92d417?d=mm&s=60) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="commons-email2-distribution-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Bindul Bhowmik | - |
| ![](https://www.gravatar.com/avatar/2b54253c7b59be6bba7024152b96e5ac?d=mm&s=60) | Colin Chalmers | [colin.chalmers@maxware.nl](mailto:colin.chalmers@maxware.nl) |
| ![](https://www.gravatar.com/avatar/785d62a87031b0e0ba12a620ddd33e39?d=mm&s=60) | Frank Y. Kim | [frank.kim@clearink.com](mailto:frank.kim@clearink.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Regis Koenig | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Stephen Kruger | - |
| ![](https://www.gravatar.com/avatar/89747060222d94162c69b432cea5189d?d=mm&s=60) | Sean Legassick | [sean@informage.net](mailto:sean@informage.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Andrew Liles | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Cedrik Lime | - |
| ![](https://www.gravatar.com/avatar/43f0936289be0f4857d0b38a8705e34a?d=mm&s=60) | Mark Lowe | [mark.lowe@boxstuff.com](mailto:mark.lowe@boxstuff.com) |
| ![](https://www.gravatar.com/avatar/99a2de4b67388abdaf13ca4627398a7d?d=mm&s=60) | Brett McLaughlin | [bmclaugh@algx.net](mailto:bmclaugh@algx.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Piero Ottuzzi | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Niall Pemberton | - |
| ![](https://www.gravatar.com/avatar/0b28160da341f2aca1ab94d78c438f57?d=mm&s=60) | Greg Ritter | [greg@shwoop.com](mailto:greg@shwoop.com) |
| ![](https://www.gravatar.com/avatar/b30da618a502d63ba0ae4736799ad0ef?d=mm&s=60) | Corey Scott | [corey.scott@gmail.com](mailto:corey.scott@gmail.com) |
| ![](https://www.gravatar.com/avatar/cf1a8f7cce5d2e829561e6d3081e0777?d=mm&s=60) | Eric Spiegelberg | [eric@spiegs.com](mailto:eric@spiegs.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Dominik Stadler | - |
| ![](https://www.gravatar.com/avatar/cc058d8d4bde1b49e2654d79981be257?d=mm&s=60) | Matthias Wessendorf | [matthias@wessendorf.net](mailto:matthias@wessendorf.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Brandon Wolfe | - |
| ![](https://www.gravatar.com/avatar/3beea937ea4cc3017325d006a52bfa9f?d=mm&s=60) | Alexander Lehmann | [alexlehm@gmail.com](mailto:alexlehm@gmail.com) |
| ![](https://www.gravatar.com/avatar/15f2e307ebe1eccbd816d4ce5bfd573b?d=mm&s=60) | Vegard Stuen | [vegard.stuen@gmail.com](mailto:vegard.stuen@gmail.com) |

---

<a id="commons-email2-jakarta-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-jakarta/ci-management.html -->

<!-- page_index: 26 -->

<a id="commons-email2-jakarta-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-email2-jakarta-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-email2-jakarta-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-email2-jakarta"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-jakarta/index.html -->

<!-- page_index: 27 -->

<a id="commons-email2-jakarta--about-apache-commons-email-for-jakarta"></a>

## About Apache Commons Email for Jakarta

Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API.

---

<a id="commons-email2-jakarta-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-jakarta/scm.html -->

<!-- page_index: 28 -->

<a id="commons-email2-jakarta-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-email2-jakarta-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-email/commons-email2-jakarta
```

<a id="commons-email2-jakarta-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-jakarta
```

<a id="commons-email2-jakarta-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-jakarta
```

<a id="commons-email2-jakarta-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-email2-jakarta-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-jakarta/summary.html -->

<!-- page_index: 29 -->

<a id="commons-email2-jakarta-summary--project-summary"></a>

## Project Summary

<a id="commons-email2-jakarta-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Email for Jakarta |
| Description | Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API. |
| Homepage | [https://commons.apache.org/proper/commons-email/commons-email2-jakarta/](#commons-email2-jakarta) |

<a id="commons-email2-jakarta-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-email2-jakarta-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-email2-jakarta |
| Version | 2.0.0-M1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-email2-jakarta-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-jakarta/team.html -->

<!-- page_index: 30 -->

<a id="commons-email2-jakarta-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-email2-jakarta-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/cdb8b39b4d3afa6be1e2cda37f75f880?d=mm&s=60) | dion | dIon Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/28206b147858407d3246a39215067866?d=mm&s=60) | jmcnally | John McNally | [jmcnally@collab.net](mailto:jmcnally@collab.net) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/ab858863fac6e5a02e2e5df7f9949e22?d=mm&s=60) | quintonm | Quinton McCombs | [quintonm@bellsouth.net](mailto:quintonm@bellsouth.net) | - | NequalsOne, LLC. | - | - | - |
| ![](https://www.gravatar.com/avatar/9cd154bd87385c597d95250177e5bca6?d=mm&s=60) | epugh | Eric Pugh | [epugh@opensourceconnections.com](mailto:epugh@opensourceconnections.com) | - | OpenSource Connections | - | - | - |
| ![](https://www.gravatar.com/avatar/cd55fa3f775b72fc74b6ba6fc9507edc?d=mm&s=60) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/134d9d61c91768c5addfd9e9d9a0bbac?d=mm&s=60) | jon | Jon Scott Stevens | [jon@latchkey.com](mailto:jon@latchkey.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/1380eb1a41b8e20bad1128bac1031402?d=mm&s=60) | jvanzyl | Jason van Zyl | [jason@zenplex.com](mailto:jason@zenplex.com) | - | Zenplex | - | - | - |
| ![](https://www.gravatar.com/avatar/e7daec2f9052c7c1690422d0d74c3b7d?d=mm&s=60) | germuska | Joe Germuska | [Joe@Germuska.com](mailto:Joe@Germuska.com) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/30f9094d5dbe2ce93f1a41afc9615b83?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/126d93a0374e9fa5faa40527b2faa177?d=mm&s=60) | henning | Henning P. Schmiedehausen | [hps@intermeta.de](mailto:hps@intermeta.de) | - | INTERMETA - Gesellschaft fuer Mehrwertdienste mbH | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | scolebourne | Stephen Colebourne | - | - | - | - | - | 0 |
| ![](https://www.gravatar.com/avatar/abebbde126a07a66094d738d1a3af445?d=mm&s=60) | bspeakmon | Ben Speakmon | [bspeakmon@apache.org](mailto:bspeakmon@apache.org) | - | The Apache Software Foundation | - | Java Developer | -8 |
| ![](https://www.gravatar.com/avatar/a393af16a299976c4336f7432d89ab79?d=mm&s=60) | sgoeschl | Siegfried Goeschl | [sgoeschl@apache.org](mailto:sgoeschl@apache.org) | - | - | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/bacbd457de9bc401c902be783f92d417?d=mm&s=60) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="commons-email2-jakarta-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Bindul Bhowmik | - |
| ![](https://www.gravatar.com/avatar/2b54253c7b59be6bba7024152b96e5ac?d=mm&s=60) | Colin Chalmers | [colin.chalmers@maxware.nl](mailto:colin.chalmers@maxware.nl) |
| ![](https://www.gravatar.com/avatar/785d62a87031b0e0ba12a620ddd33e39?d=mm&s=60) | Frank Y. Kim | [frank.kim@clearink.com](mailto:frank.kim@clearink.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Regis Koenig | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Stephen Kruger | - |
| ![](https://www.gravatar.com/avatar/89747060222d94162c69b432cea5189d?d=mm&s=60) | Sean Legassick | [sean@informage.net](mailto:sean@informage.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Andrew Liles | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Cedrik Lime | - |
| ![](https://www.gravatar.com/avatar/43f0936289be0f4857d0b38a8705e34a?d=mm&s=60) | Mark Lowe | [mark.lowe@boxstuff.com](mailto:mark.lowe@boxstuff.com) |
| ![](https://www.gravatar.com/avatar/99a2de4b67388abdaf13ca4627398a7d?d=mm&s=60) | Brett McLaughlin | [bmclaugh@algx.net](mailto:bmclaugh@algx.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Piero Ottuzzi | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Niall Pemberton | - |
| ![](https://www.gravatar.com/avatar/0b28160da341f2aca1ab94d78c438f57?d=mm&s=60) | Greg Ritter | [greg@shwoop.com](mailto:greg@shwoop.com) |
| ![](https://www.gravatar.com/avatar/b30da618a502d63ba0ae4736799ad0ef?d=mm&s=60) | Corey Scott | [corey.scott@gmail.com](mailto:corey.scott@gmail.com) |
| ![](https://www.gravatar.com/avatar/cf1a8f7cce5d2e829561e6d3081e0777?d=mm&s=60) | Eric Spiegelberg | [eric@spiegs.com](mailto:eric@spiegs.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Dominik Stadler | - |
| ![](https://www.gravatar.com/avatar/cc058d8d4bde1b49e2654d79981be257?d=mm&s=60) | Matthias Wessendorf | [matthias@wessendorf.net](mailto:matthias@wessendorf.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Brandon Wolfe | - |
| ![](https://www.gravatar.com/avatar/3beea937ea4cc3017325d006a52bfa9f?d=mm&s=60) | Alexander Lehmann | [alexlehm@gmail.com](mailto:alexlehm@gmail.com) |
| ![](https://www.gravatar.com/avatar/15f2e307ebe1eccbd816d4ce5bfd573b?d=mm&s=60) | Vegard Stuen | [vegard.stuen@gmail.com](mailto:vegard.stuen@gmail.com) |

---

<a id="commons-email2-javax-ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-javax/ci-management.html -->

<!-- page_index: 31 -->

<a id="commons-email2-javax-ci-management--overview"></a>

## Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="commons-email2-javax-ci-management--access"></a>

## Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="commons-email2-javax-ci-management--notifiers"></a>

## Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="commons-email2-javax"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-javax/index.html -->

<!-- page_index: 32 -->

<a id="commons-email2-javax--about-apache-commons-email-for-javax"></a>

## About Apache Commons Email for Javax

Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API.

---

<a id="commons-email2-javax-scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-javax/scm.html -->

<!-- page_index: 33 -->

<a id="commons-email2-javax-scm--overview"></a>

## Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/documentation>.

<a id="commons-email2-javax-scm--web-browser-access"></a>

## Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf/commons-email/commons-email2-javax
```

<a id="commons-email2-javax-scm--anonymous-access"></a>

## Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-javax
```

<a id="commons-email2-javax-scm--developer-access"></a>

## Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-email/commons-email2-javax
```

<a id="commons-email2-javax-scm--access-from-behind-a-firewall"></a>

## Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="commons-email2-javax-summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-javax/summary.html -->

<!-- page_index: 34 -->

<a id="commons-email2-javax-summary--project-summary"></a>

## Project Summary

<a id="commons-email2-javax-summary--project-information"></a>

### Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Email for Javax |
| Description | Apache Commons Email provides an API for sending email, simplifying the JavaMail Javax API. |
| Homepage | [https://commons.apache.org/proper/commons-email/commons-email2-javax/](#commons-email2-javax) |

<a id="commons-email2-javax-summary--project-organization"></a>

### Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="commons-email2-javax-summary--build-information"></a>

### Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-email2-javax |
| Version | 2.0.0-M1 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="commons-email2-javax-team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/commons-email2-javax/team.html -->

<!-- page_index: 35 -->

<a id="commons-email2-javax-team--project-team"></a>

## Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="commons-email2-javax-team--members"></a>

### Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/cdb8b39b4d3afa6be1e2cda37f75f880?d=mm&s=60) | dion | dIon Gillard | [dion@apache.org](mailto:dion@apache.org) | - | The Apache Software Foundation | - | Java Developer | - |
| ![](https://www.gravatar.com/avatar/28206b147858407d3246a39215067866?d=mm&s=60) | jmcnally | John McNally | [jmcnally@collab.net](mailto:jmcnally@collab.net) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/ab858863fac6e5a02e2e5df7f9949e22?d=mm&s=60) | quintonm | Quinton McCombs | [quintonm@bellsouth.net](mailto:quintonm@bellsouth.net) | - | NequalsOne, LLC. | - | - | - |
| ![](https://www.gravatar.com/avatar/9cd154bd87385c597d95250177e5bca6?d=mm&s=60) | epugh | Eric Pugh | [epugh@opensourceconnections.com](mailto:epugh@opensourceconnections.com) | - | OpenSource Connections | - | - | - |
| ![](https://www.gravatar.com/avatar/cd55fa3f775b72fc74b6ba6fc9507edc?d=mm&s=60) | dlr | Daniel Rall | [dlr@finemaltcoding.com](mailto:dlr@finemaltcoding.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/134d9d61c91768c5addfd9e9d9a0bbac?d=mm&s=60) | jon | Jon Scott Stevens | [jon@latchkey.com](mailto:jon@latchkey.com) | - | CollabNet, Inc. | - | - | - |
| ![](https://www.gravatar.com/avatar/1380eb1a41b8e20bad1128bac1031402?d=mm&s=60) | jvanzyl | Jason van Zyl | [jason@zenplex.com](mailto:jason@zenplex.com) | - | Zenplex | - | - | - |
| ![](https://www.gravatar.com/avatar/e7daec2f9052c7c1690422d0d74c3b7d?d=mm&s=60) | germuska | Joe Germuska | [Joe@Germuska.com](mailto:Joe@Germuska.com) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/30f9094d5dbe2ce93f1a41afc9615b83?d=mm&s=60) | rdonkin | Robert Burrell Donkin | [rdonkin@apache.org](mailto:rdonkin@apache.org) | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/126d93a0374e9fa5faa40527b2faa177?d=mm&s=60) | henning | Henning P. Schmiedehausen | [hps@intermeta.de](mailto:hps@intermeta.de) | - | INTERMETA - Gesellschaft fuer Mehrwertdienste mbH | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | scolebourne | Stephen Colebourne | - | - | - | - | - | 0 |
| ![](https://www.gravatar.com/avatar/abebbde126a07a66094d738d1a3af445?d=mm&s=60) | bspeakmon | Ben Speakmon | [bspeakmon@apache.org](mailto:bspeakmon@apache.org) | - | The Apache Software Foundation | - | Java Developer | -8 |
| ![](https://www.gravatar.com/avatar/a393af16a299976c4336f7432d89ab79?d=mm&s=60) | sgoeschl | Siegfried Goeschl | [sgoeschl@apache.org](mailto:sgoeschl@apache.org) | - | - | - | Java Developer | 2 |
| ![](https://www.gravatar.com/avatar/bacbd457de9bc401c902be783f92d417?d=mm&s=60) | tn | Thomas Neidhart | [tn@apache.org](mailto:tn@apache.org) | - | The Apache Software Foundation | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="commons-email2-javax-team--contributors"></a>

### Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

| Image | Name | Email |
| --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Bindul Bhowmik | - |
| ![](https://www.gravatar.com/avatar/2b54253c7b59be6bba7024152b96e5ac?d=mm&s=60) | Colin Chalmers | [colin.chalmers@maxware.nl](mailto:colin.chalmers@maxware.nl) |
| ![](https://www.gravatar.com/avatar/785d62a87031b0e0ba12a620ddd33e39?d=mm&s=60) | Frank Y. Kim | [frank.kim@clearink.com](mailto:frank.kim@clearink.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Regis Koenig | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Stephen Kruger | - |
| ![](https://www.gravatar.com/avatar/89747060222d94162c69b432cea5189d?d=mm&s=60) | Sean Legassick | [sean@informage.net](mailto:sean@informage.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Andrew Liles | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Cedrik Lime | - |
| ![](https://www.gravatar.com/avatar/43f0936289be0f4857d0b38a8705e34a?d=mm&s=60) | Mark Lowe | [mark.lowe@boxstuff.com](mailto:mark.lowe@boxstuff.com) |
| ![](https://www.gravatar.com/avatar/99a2de4b67388abdaf13ca4627398a7d?d=mm&s=60) | Brett McLaughlin | [bmclaugh@algx.net](mailto:bmclaugh@algx.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Piero Ottuzzi | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Niall Pemberton | - |
| ![](https://www.gravatar.com/avatar/0b28160da341f2aca1ab94d78c438f57?d=mm&s=60) | Greg Ritter | [greg@shwoop.com](mailto:greg@shwoop.com) |
| ![](https://www.gravatar.com/avatar/b30da618a502d63ba0ae4736799ad0ef?d=mm&s=60) | Corey Scott | [corey.scott@gmail.com](mailto:corey.scott@gmail.com) |
| ![](https://www.gravatar.com/avatar/cf1a8f7cce5d2e829561e6d3081e0777?d=mm&s=60) | Eric Spiegelberg | [eric@spiegs.com](mailto:eric@spiegs.com) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Dominik Stadler | - |
| ![](https://www.gravatar.com/avatar/cc058d8d4bde1b49e2654d79981be257?d=mm&s=60) | Matthias Wessendorf | [matthias@wessendorf.net](mailto:matthias@wessendorf.net) |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | Brandon Wolfe | - |
| ![](https://www.gravatar.com/avatar/3beea937ea4cc3017325d006a52bfa9f?d=mm&s=60) | Alexander Lehmann | [alexlehm@gmail.com](mailto:alexlehm@gmail.com) |
| ![](https://www.gravatar.com/avatar/15f2e307ebe1eccbd816d4ce5bfd573b?d=mm&s=60) | Vegard Stuen | [vegard.stuen@gmail.com](mailto:vegard.stuen@gmail.com) |

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-email/issue-tracking.html -->

<!-- page_index: 36 -->

<a id="issue-tracking--apache-commons-email-parent-pom-issue-tracking"></a>

## Apache Commons Email Parent POM Issue tracking

Apache Commons Email Parent POM uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons Email Parent POM JIRA project page](https://issues.apache.org/jira/browse/EMAIL).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons Email Parent POM please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310474&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-email/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310474&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12310474&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons Email Parent POM are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons Email Parent POM bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310474&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons Email Parent POM bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310474&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons Email Parent POM bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12310474&sorter/field=issuekey&sorter/order=DESC)

---
