# Project Information

## Navigation

- Commons Imaging
  - [About](#index)
  - [Sources](#scm)
  - [Security](#security)
  - [Why Use Imaging](#whyimaging)
  - [Getting Started](#gettingstarted)
  - [Sample Usage](#sampleusage)
  - [Format Support](#formatsupport)
  - [History](#history)
  - [Incubation Status Reports (old)](#sanselan-incubation-status-reports)
  - [References](#references)
  - [Sample Images](#sampleimages)
  - [Roadmap](#roadmap)
- Project Documentation
  - [Project Information](#project-info)
    - [About](#index)
    - [Summary](#summary)
    - [Team](#team)
    - [Source Code Management](#scm)
    - [CI Management](#ci-management)
- Other pages
  - [Apache Commons Imaging Issue tracking](#issue-tracking)

## Content

<a id="index"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/index.html -->

<!-- page_index: 1 -->

<a id="index--commons-imaging:-a-pure-java-image-library"></a>

# Commons Imaging: a Pure-Java Image Library

Apache Commons Imaging, previously known as Apache Commons Sanselan, is a library that
reads and writes a variety of image formats, including fast parsing
of image info (size, color space, ICC profile, etc.) and metadata.

This library is pure Java. Compared to typical image I/O libraries in native code, it's more portable, and should be more reliable and more secure against corrupt/malicious
images, yet still performs reasonably well.
It's easier to use than ImageIO/JAI/java.awt.Toolkit (Sun/Java's image support), supports
more formats (and supports them more correctly). It also provides easy access to metadata.

Imaging was working and was used by a number of projects in production even before
reaching its initial release as an Apache Commons component.

This project is Open Source; free as in freedom and free as in beer.
It is available under the ASF (Apache) License. This is a non-viral Open Source license.

- [Why Use Commons Imaging?](#whyimaging)
- [Getting Started](#gettingstarted)

<a id="index--documentation"></a>

# Documentation

A getting started [guide](#gettingstarted) is available
together with various [project reports](https://commons.apache.org/proper/commons-imaging/project-reports.html).

The Javadoc API documents are available online:

- The [latest API docs](https://commons.apache.org/proper/commons-imaging/apidocs/index.html)
- Older releases - see the [Release History](#history) page

The [source repository](#scm) can be
[browsed](https://gitbox.apache.org/repos/asf?p=commons-imaging.git), or you can browse/contribute via [GitHub](https://github.com/apache/commons-imaging).

<a id="index--release-information"></a>

# Release Information

<a id="index--help-needed"></a>

## Help Needed!

If you want to help out you may:

- Look through the [issues waiting for a patch](https://issues.apache.org/jira/issues/?jql=project%20%3D%20IMAGING%20AND%20resolution%20%3D%20Unresolved%20AND%20fixVersion%20%3D%20%22Patch%20Needed%22%20ORDER%20BY%20priority%20DESC)
- Look through the *Needs Work* tags in the [TagList report](https://commons.apache.org/proper/commons-imaging/taglist.html)
- Contribute a patch
- Create a PR via [Github](https://github.com/apache/commons-imaging)

Make sure to read through our [guide lines for contributing patches](https://commons.apache.org/patches.html) before you start coding. This will stream line the process of getting your contributions into the code.

For information on previous releases see the [Release History](#history), and to download previous releases see the [Commons Sanselan Archive](https://archive.apache.org/dist/commons/sanselan/).

<a id="index--support"></a>

# Support

The [commons mailing lists](https://commons.apache.org/proper/commons-imaging/mail-lists.html) act as the main support forum.
The user list is suitable for most library usage queries.
The dev list is intended for the development discussion.
Please remember that the lists are shared between all commons components, so prefix your email by [imaging].

Bug reports and enhancements are also welcomed via the [JIRA](#issue-tracking) issue tracker.
Please read the instructions carefully.

---

<a id="scm"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/scm.html -->

<!-- page_index: 2 -->

<a id="scm--overview"></a>

# Overview

This project uses [Git](https://git-scm.com/) to manage its source code. Instructions on Git use can be found at <https://git-scm.com/doc>.

<a id="scm--web-browser-access"></a>

# Web Browser Access

The following is a link to a browsable version of the source repository:

```
https://gitbox.apache.org/repos/asf?p=commons-imaging.git
```

<a id="scm--anonymous-access"></a>

# Anonymous Access

The source can be checked out anonymously from Git with this command (See <https://git-scm.com/docs/git-clone>):

```
$ git clone http://gitbox.apache.org/repos/asf/commons-imaging.git
```

<a id="scm--developer-access"></a>

# Developer Access

Only project developers can access the Git tree via this method (See <https://git-scm.com/docs/git-clone>).

```
$ git clone https://gitbox.apache.org/repos/asf/commons-imaging.git
```

<a id="scm--access-from-behind-a-firewall"></a>

# Access from Behind a Firewall

Refer to the documentation of the SCM used for more information about access behind a firewall.

---

<a id="security"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/security.html -->

<!-- page_index: 3 -->

<a id="security--security-vulnerabilities"></a>

# Security Vulnerabilities

For information about reporting or asking questions about
security, please see the
[security page](https://commons.apache.org/security.html)
of the Apache Commons project.

<a id="security--security-model"></a>

# Security Model

Generally, Apache Commons libraries [do
not support possibly-malicious input](https://commons.apache.org/security.html#Security_Model) unless otherwise specified.

Processing untrusted image material is supported to some extent: this should never lead to code execution.
However, this component currently does not guarantee the absence of DoS conditions, and that any
applications processing untrusted images should be made resilient against memory, CPU and stack exhaustion
problems. If you encounter specific cases where certain inputs lead to disproportionate resource usage, we welcome those as regular (non-security)
[issues](#issue-tracking) or
[contributions](https://commons.apache.org/patches.html).
If you'd like to participate in putting together general protections against such problems, in particular
[this issue](https://issues.apache.org/jira/browse/IMAGING-379) could be a good start.

---

<a id="whyimaging"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/whyimaging.html -->

<!-- page_index: 4 -->

<a id="whyimaging--why-use-commons-imaging"></a>

# Why use Commons Imaging?

Why another image library? There are so many already.

Apache Commons Imaging is written in 100% pure Java. It will run on any JVM, and any platform, without modification.

There are no dependencies. Commons Imaging only requires Java 1.8 or later.

It is designed to be very easy to use. It has a simple, clean interface. Most operations are a single Imaging method call. See the [Sample Usage](#sampleusage) section.

Commons Imaging aims to be transparent. There are no hidden buffers to dispose, no native memory to free, no background threads.

It reads and writes a wide variety of image formats, and supports some variations and encodings missed by all or most other libraries. See the [Format Support](#formatsupport) list.

Commons Imaging does more than read and write images. Reading image info (image size, colorspace, bit depth, etc.) and metadata is easy, and does not require reading the image pixels.
It presents image info and metadata in a format-neutral manner.
It also gives easy, structured access to format-specific info.

It can read from and write to files, byte arrays, or any InputStream/OutputStream. Reading InputStreams
only reads data it needs, and caches what has been read, so it's efficient on I/O, and fast on
slow storage and networked files.

It supports reading and writing a variety of metadata in a structured way, including EXIF metadata.

Most other libraries offer little or incomplete support for ICC Profiles.
Commons Imaging can extract and (simply) parse embedded ICC Profiles.
Moreover, it applies the ICC profile by default, converting read images to sRGB.
This means images are color-corrected by default.
see: <https://en.wikipedia.org/wiki/International_Color_Consortium>,
<https://en.wikipedia.org/wiki/sRGB>

Was written with an eye to correctness and code clarity, but also good performance.
Hopefully it is easy to use, easy to extend and can be used to explore images + image formats, rather than just read images for display.

It is Free Software/Open Source. It is available under the
[Apache Software License](https://www.apache.org/licenses/LICENSE-2.0).

Commons Imaging also includes a number of useful functions such as guess an image's format by examining its "magic numbers" (header info).

The ColorConversions class offers methods to convert between the following color spaces: CIE-L\*CH°, CIE-L\*ab, CIE-L\*uv, CMY, CMYK, HSL, HSV, Hunter-Lab, RGB, XYZ and Yxy (algorithms courtesy of EasyRGB's).
see: <https://www.easyrgb.com/>

---

<a id="gettingstarted"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/gettingstarted.html -->

<!-- page_index: 5 -->

<a id="gettingstarted--requirements"></a>

# Requirements

- Commons Imaging requires Java 1.7 or higher.
- The questions of porting to J2ME and Android have been raised, but not yet pursued.
- Commons Imaging has no dependencies.
- AWT is required. ImageIO is only required to compile and used optionally
  as a fallback when reading JPEG thumbnails.

<a id="gettingstarted--getting-started"></a>

# Getting Started

- Download the latest release from the [download page](https://commons.apache.org/imaging/download_imaging.cgi).
- Add the jar to your project's classpath.
- See our [Sample Code](#sampleusage) for examples.
- Refer to the project's [javadoc](https://commons.apache.org/proper/commons-imaging/apidocs/index.html)
- Have questions? Subscribe to the commons user [mailing list](https://commons.apache.org/proper/commons-imaging/mail-lists.html).

<a id="gettingstarted--building-from-the-latest-source"></a>

# Building from the latest Source

There are two steps to building Commons Imaging from the latest source:

- Check out the latest source from [git](#scm)
- Build using [Maven 2](http://maven.apache.org)

- 1. Install the latest version of Maven
- 2. cd imaging-snapshot (if you are not already in the project directory)
- 3. mvn -Prc package
- 4. The build will be in the "target" folder.

<a id="gettingstarted--logging"></a>

# Logging

Commons Imaging uses the JDK java.util.logging (JUL) classes for logging. You can find out more about
JUL in its [documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/logging/overview.html), or reading the [logging API documentation](https://docs.oracle.com/javase/8/docs/api/java/util/logging/package-summary.html).

- A more verbose output is available by enabling the log level **FINE**
- Information that is useful for debug and troubleshooting is being logged with the **FINEST** log level
- Some exceptions that are not re-thrown are being logged with the **SEVERE** log level
- Commons Imaging loggers are created using the class name, so you should be able to filter the log output with the class or package names

---

<a id="sampleusage"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/sampleusage.html -->

<!-- page_index: 6 -->

<a id="sampleusage--example-code-and-sample-usage"></a>

# Example Code and Sample Usage

<a id="sampleusage--example-code"></a>

## Example Code

Can be found in the source distribution in org.apache.commons.imaging.examples package

- [ImageWriteExample.java](https://github.com/apache/commons-imaging/blob/master/src/test/java/org/apache/commons/imaging/examples/ImageWriteExample.java) (illustrates how to write an image)
- [ImageReadExample.java](https://github.com/apache/commons-imaging/blob/master/src/test/java/org/apache/commons/imaging/examples/ImageReadExample.java) (illustrates how to read an image)
- [SampleUsage.java](https://github.com/apache/commons-imaging/blob/master/src/test/java/org/apache/commons/imaging/examples/SampleUsage.java) (various examples)
- [MetadataExample.java](https://github.com/apache/commons-imaging/blob/master/src/test/java/org/apache/commons/imaging/examples/MetadataExample.java) (illustrates how to read JPEG EXIF metadata such as GPS, date and time photo taken, etc.)
- [WriteExifMetadataExample.java](https://github.com/apache/commons-imaging/blob/master/src/test/java/org/apache/commons/imaging/examples/WriteExifMetadataExample.java) (illustrates how to write JPEG EXIF metadata such as GPS, date and time photo taken, etc.)

---

<a id="formatsupport"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/formatsupport.html -->

<!-- page_index: 7 -->

<a id="formatsupport--image-format-support"></a>

# Image Format Support

| Format | Read | Write | Notes | References |
| --- | --- | --- | --- | --- |
| BMP | yes | yes | Mostly Complete. May not read some cursors, icons and OS/2 bitmaps. Controlling the exact format when writing is incomplete. | No spec, see: [wikipedia](http://en.wikipedia.org/wiki/Windows_bitmap) |
| GIF | yes | yes | Both versions 87a and 89a Reading of animated GIFs is supported to the extent that you can read all of the images contained in a GIF, but timing/loop info is ignored. Controlling the exact format when writing is incomplete. | [spec](http://www.w3.org/Graphics/GIF/spec-gif89a.txt) [wikipedia](http://en.wikipedia.org/wiki/GIF) |
| JPEG/JFIF | some | no | Reads only simple grayscale and YCbCr baseline sequential JPEG images without RST markers, which must use 8 bits per component and be Huffman encoded. Can read image info, metadata and extract ICC Profiles. Both JFIF and DCF/EXIF. Provides JPEG comments in ImageInfo. | [JFIF spec](http://www.jpeg.org/public/jfif.pdf) [JPEG Group](http://www.jpeg.org/jpeg/index.html) [wikipedia](http://en.wikipedia.org/wiki/JPEG) |
| ICNS | mostly | mostly | Missing support for JPEG2000 icons, but all other formats and sizes are correctly read and written. Extensively tested for correctness against MacOS X, including behavior with missing masks. | [wikipedia](http://en.wikipedia.org/wiki/Apple_Icon_Image) |
| ICO/CUR | yes | mostly | Reads 1/4/8/16/24/32 bpp .ico and .cur files. Supports the new Windows Vista ICO files with embedded PNGs. Deals correctly with alpha vs bitmask transparency issues in 32 bpp. Supports bitfield compressed bitmaps. Extensively tested. Probably the best open-source implementation under the sun. | No spec, see: [wikipedia](http://en.wikipedia.org/wiki/ICO_(icon_image_file_format)) |
| PCX/DCX | yes | yes | Reads 1 plane 1/2/4/8 bit, 1 bit 1/2/3/4 plane, 3 plane 8 bit, 1 plane 24 bit, and 1 plane 32 bit images. Monochrome is parsed correctly. Reads and can write the undocumented uncompressed PCX format. Reading short DCX tables is supported. Thoroughly tested. |  |
| PNM/PGM/PBM/PPM/PAM Portable Pixmap | yes | mostly | Reading complete. PAM writing only in RGB\_ALPHA format. | [spec](http://netpbm.sourceforge.net/doc/index.html) [wikipedia](http://en.wikipedia.org/wiki/Portable_pixmap) |
| PNG | yes | yes | Supported through version 1.2/ISO/IEC standard (15948:2003). Controlling the exact format when writing is incomplete. | [spec](http://www.libpng.org/pub/png/) [wikipedia](http://en.wikipedia.org/wiki/Portable_Network_Graphics) |
| PSD/Photoshop | yes | no | Basic support. Can only read the first Layer. No support for extra channels. Supports all modes except Multichannel. Can read some image metadata. | [Unofficial spec](http://www.fileformat.info/format/psd/egff.htm) [spec](http://www.fileformat.info/format/psd/egff.htm) [wikipedia](http://en.wikipedia.org/wiki/PSD) |
| RGBE/Radiance HDR | yes | no | Basic support. | [Wikipedia](http://en.wikipedia.org/wiki/RGBE_image_format) |
| TIFF | yes | yes | Supported through version 6.0. TIFFs is a open-ended container format, so it's not possible to support every possibly variation. Supports Bi-Level, Palette/Indexed, RGB, CMYK, YCbCr, CIELab and LOGLUV images. Supports reading and writing LZW, CCITT Modified Huffman/Group 3/Group 4, and Packbits/RLE compression. Notably missing other forms of compression though, including JPEG. Supports reading Tiled images. | [Adobe](https://www.web.archive.org/web/20060116011057/https://partners.adobe.com/public/developer/tiff/index.html) [spec](https://www.web.archive.org/web/20050828212121/https:/partners.adobe.com/public/developer/en/tiff/TIFF6.pdf) [wikipedia](http://en.wikipedia.org/wiki/TIFF) [AWare Systems TIFF Tag Reference](http://www.awaresystems.be/imaging/tiff/tifftags.html) |
| WBMP | yes | yes | Complete support for WBMP type 0 bitmaps. | [wikipedia](http://en.wikipedia.org/wiki/WBMP) [spec](https://www.web.archive.org/web/20050824034208/http:/www.wapforum.org:80/what/technical/SPEC-WAESpec-19990524.pdf) |
| XBM | yes | yes | Complete. | [wikipedia](http://en.wikipedia.org/wiki/XBM) [spec](http://www.xfree86.org/current/xlib.pdf) |
| XPM | yes | yes | Only XPM version 3 is currently supported, but the other versions are obsolete. Reads all color formats, including those using symbolic names from rgb.txt. Writing only writes color data. | [wikipedia](http://en.wikipedia.org/wiki/X_PixMap) [spec](http://www.xfree86.org/current/xpm.pdf) |

---

<a id="history"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/history.html -->

<!-- page_index: 8 -->

<a id="history--history"></a>

# History

Version 1.0-alpha released in 2019 brought many changes and is
best followed in the release notes.

Apache Commons Sanselan was renamed to Apache Commons Imaging on 16 April 2012, the package changed from `org.apache.sanselan` to `org.apache.commons.imaging`, the "main" class changed from `org.apache.sanselan.Sanselan` to
`org.apache.commons.imaging.Imaging`, the website became
<https://commons.apache.org/imaging>
and Maven co-ordinates also changed.

Version 0.97 released February 14th, 2009, was the last Sanselan release before the rename, and the last incubator release.

Version 0.94 released July 30th, 2008, was the first Apache release of Sanselan.

Version 0.90 released January 31st, 2008.

- Added some convenience functions for reading and writing GPS data.
- These are demonstrated in the metadata sample usage classes.

Version 0.89 released January 22nd, 2008. **This release was mislabeled as 0.88**

- Added EXIF insert/update/remove functionality. See WriteExifMetadataExample.java for examples.
- Rewrote JPEG and TIFF parsing.
- Greatly elaborated the unit test suite and test image suite.
- In the process found and resolved many bugs.
- Once again, I hope this is the last non-apache release. =)

Version 0.88 released November 17th, 2007.

- Restored original package structure. (org.apache.commons.sanselan.\* -> org.cmc.sanselan.\*)
- Refactored "byte sources," improving performance reading image data from InputStreams.
- More code cleanup, mostly removing debugging code and applying naming conventions.
- Fixed two bugs around pngs: alpha channels weren't be written properly, and alpha channel was not being preserved when reading grayscale pngs.
- Improved javadocs.

Version 0.87 released October 6th, 2007.

- Fixed a number of bugs.
- Began adding javadocs, starting with the facade classes: Sanselan, and every class returned by its methods.
- This is probably the last pre-apache release.

Version 0.86 released September 17th, 2007.

- Fixed bug with writing grayscale pngs.
- Fixed bug with gamma correction when reading pngs.
- Added image read param that allows control over BufferedImage creation.
- Removed an erroneous javadoc.
- Minor cleanup.

Version 0.85 released September 5th, 2007.

- Cleaned up Tiff image parser and writer.
- Added compression parameter to tiff image writer.
- Added an example that illustrates image writing, optional parameters, etc.

Version 0.84 released September 3rd, 2007.

- Fixed Tiff/Exif bug wherein rational number fields with a zero divisor prevented the metadata from being read, due to a "divide by zero" error.

Version 0.83 released August 30th, 2007.

- Fixed Tiff/Exif bug wherein Private IFD Tags were not being properly read.
- Added better metadata sample code.

Version 0.82 released August 30th, 2007.

- Complete refactor of the image metadata methods. See the new MetadataExample class for a simple example.
- Converted all of the Sanselan class's methods to static.
- Cleaned up some old code.

Version 0.81 released August 17th, 2007.

- Made a couple of methods of ImageInfo public (getColorType() and getColorTypeDescription()).

Version 0.80 released July 25th, 2007.

- I've begun a overhaul of the codebase in anticipation of becoming an Apache Incubator project.
- I've changed the package names (again) to be org.apache.commons.sanselan.\*.
- I've removed the dependency on sharedlib.
- I've removed a great deal of old cruft.
- I've begun to apply a consistent naming convention to variables (lowerCamelCase) and constant names (ALL\_CAPS).

Version 0.79 released June 21th, 2007.

- I've fixed that pernicious bug in LZW compression. I've switched the default TIFF compression scheme back to LZW.
- TIFF uses an unusual variation of LZW. For details, see this article. http://www.fileformat.info/mirror/egff/ch09\_04.htm
- In this case, the bug was: trailing EndOfInformation codes are sometimes omitted. That is, if a EndOfInformation code is the last code of a block, it may not appear.

Version 0.78 released June 20th, 2007.

- LZW compression is buggy; this only effects writing TIFF. I've switched the default TIFF compression scheme to packbits which performs worse until this can be corrected.

Version 0.77 released June 16th, 2007.

- I've open sourced the last dependency of this project, sharedlib.
- I've also renamed almost all of the package names. Sorry about this; a simple global search and replace should be easy to do.

Version 0.76 released September 16th, 2006.

Version 0.75 released September 5th, 2006.

First released September 22nd, 2004.

---

<a id="sanselan-incubation-status-reports"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/sanselan-incubation-status-reports.html -->

<!-- page_index: 9 -->

<a id="sanselan-incubation-status-reports--sanselan-incubation-status-reports"></a>

# Sanselan Incubation Status Reports

<a id="sanselan-incubation-status-reports--2009-january-sanselan-incubator-status-report"></a>

## 2009-January Sanselan Incubator status report

Sanselan has been in incubation since September 2007.

Sanselan is a pure-java image library for reading and writing
a variety of image formats.

The community hasn't grown much in the past three months. There
continues to be only one active committer. Participation level is low.

The first official Apache release occurred on July 30th, 2008. A new
release has just been prepared and is current being voted upon.

The new release includes significant bug fixes, better documentation, better
IPTC and XMP support (metadata) and improvements to the release structure.

Barriers to graduation continue to be diversity, size of the community, and overall activity.

<a id="sanselan-incubation-status-reports--2008-october-sanselan-incubator-status-report"></a>

## 2008-October Sanselan Incubator status report

Sanselan has been in incubation since September 2007.

Sanselan is a pure-java image library for reading and writing
a variety of image formats.

The community hasn't grown much in the past three months. There
continues to be only one active committer.

The first official Apache release occurred on July 30th, 2008.

A second release is being prepared. It will include significant bug
fixes, better documentation, better IPTC and XMP support and
improvements to the release structure.

Barriers to graduation continue to be diversity, size of the community, and overall activity.

<a id="sanselan-incubation-status-reports--2008-july-sanselan-incubator-status-report"></a>

## 2008-July Sanselan Incubator status report

Sanselan has been in incubation since September 2007.

Sanselan is a pure-java image library for reading and writing
a variety of image formats.

The community hasn't grown much in the past three months. There
continues to be only one active committer.

There was work on EXIF metadata read/write support and a bug
in the implementation was discussed on the dev aliaas.

Builds outside Apache have been made but no official Apache release
has been created yet.

Barriers to graduation continue to be diversity, size of the community, and overall activity.

<a id="sanselan-incubation-status-reports--2008-april-sanselan-incubator-status-report"></a>

## 2008-April Sanselan Incubator status report

Sanselan has been in incubation since September 2007.

Sanselan is a pure-java image library for reading and writing
a variety of image formats.

The community hasn't grown in the past three months. There have
been commits from only two people. No patches from contributors, yet.

There was work on EXIF metadata read/write support and some
changes were made to prepare for a first release.

<a id="sanselan-incubation-status-reports--2008-january-sanselan-incubator-status-report"></a>

## 2008-January Sanselan Incubator status report

Sanselan has been in incubation since September 2007.

Sanselan is a pure-java image library for reading and writing
a variety of image formats.

The community is still small, with a few more members now compared
to the beginning.

The code base has been imported and the package names have been
changed to org.apache.sanselan. Work continues on scrubbing the
code and organizing it into maven.

A release is being prepared.

<a id="sanselan-incubation-status-reports--2007-december-sanselan-incubator-status-report"></a>

## 2007-December Sanselan Incubator status report

Sanselan has been in incubation since September 2007.

Sanselan is a pure-java image library for reading and writing
a variety of image formats.

The community is still small, with a few more members now compared
to the beginning.

The code base has been imported and the package names have been
changed to org.apache.sanselan.

A release is being prepared.

<a id="sanselan-incubation-status-reports--2007-november-sanselan-incubator-status-report"></a>

## 2007-November Sanselan Incubator status report

The autoexport from confluence to our site has been set up (see
http://incubator.apache.org/sanselan/) so documenation
can be added soon.

We are looking for images (with no copyright restrictions) that
can be used for unit testing. Existing (private) unit tests rely
on copyrighted images that cannot be used.

<a id="sanselan-incubation-status-reports--2007-october-sanselan-incubator-status-report"></a>

## 2007-October Sanselan Incubator status report

The project has kicked off with some basic infrastructure now in place.

Mailing lists have been set up. The structure of the project has been
discussed; plans are to use maven using Jackrabbit as a model.

A site was created using Confluence.

The svn repository has had the first code drop. Most of the code from the
original base has been committed.

The JIRA project is set up and the initial code drop was posted for review.

The initial committers have been given access to the repository.

---

<a id="references"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/references.html -->

<!-- page_index: 10 -->

<a id="references--references"></a>

# References

- Marco Schmidt's list of Java image libaries (archived):
  <http://web.archive.org/web/20090204080356/http://schmidt.devlib.org/java/image-io-libraries.html>
- Another list of Java image libaries
  <http://web.archive.org/web/20170310015234/https://www.dmoz.org/Computers/Programming/Languages/Java/Class_Libraries/Graphics/Data_Formats/>
- File format cloud.
  <http://www.fileformat.info/format/cloud.htm>
- ImageInfo an excellent Java class to extract image properties (archived):
  <http://web.archive.org/web/20090216122500/http://schmidt.devlib.org/image-info>
- EasyRGB's color conversion formulas.
  <http://www.easyrgb.com/>
- AWare Systems TIFF Tag Reference (JPEG EXIF metadata is stored in TIFF directories).
  <http://www.awaresystems.be/imaging/tiff/tifftags.html>
- Phil Harvey's exiftool and metadata reference
  <http://www.sno.phy.queensu.ca/~phil/exiftool/index.html>

---

<a id="sampleimages"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/sampleimages.html -->

<!-- page_index: 11 -->

<a id="sampleimages--test-image-suite-and-sample-images"></a>

# Test Image Suite and Sample Images

- The original test image suite that Imaging was developed against cannot be released, since we don't own the rights to many of the more interesting examples.
- We are in the process of generating and collecting more.

<a id="sampleimages--sample-image-sources"></a>

## Sample Image Sources

This list is hardly comprehensive, but it is a good starting point.

- Phil Harvey's large collection
  <http://owl.phy.queensu.ca/~phil/exiftool/sample_images.html>
- Drew Noakes' collection of images with EXIF
  <http://www.drewnoakes.com/code/exif/exifImages/>
- RAWpository
  <http://www.glasslantern.com/RAWpository/>
- exif.org's Sample Images
  <http://www.exif.org/samples.html>
- dpreview.com includes sample images with every one of their full reviews.
  <http://www.dpreview.com/>
- flickr let's you search by camera type, which is invaluable, although not all images are
  "out of camera" originals (many have been edited or scaled).
  <http://www.flickr.com/>
- PNG official test suite More png sample images available here.
  <ftp://ftp.simplesystems.org/pub/libpng/png/images/suite/>

---

<a id="roadmap"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/roadmap.html -->

<!-- page_index: 12 -->

<a id="roadmap--roadmap"></a>

# Roadmap

<a id="roadmap--version-1.0"></a>

## Version 1.0

Features we hope to have for the 1.0 release.

<a id="roadmap--interoperability"></a>

#### Interoperability

- Android support. Needs AWT to be an optional dependency.
- Add the ability to use Commons Imaging as an Image I/O plugin.

<a id="roadmap--file-formats"></a>

#### File formats

- Improve JPEG read support.
- Rewrite and fully generalize TIFF parsing to support arbitrary complexity TIFF files instead of just EXIF.
  Lower level API for reading raw fields and directories, and a higher level API for image structures.
- Add pluggable TIFF tag sets.
- Parse some EXIF maker notes.
- Add a structured way to write IPTC image metadata to JPEG files.
- Reading all images from .gif files isn't working. see: getAllBufferedImages().
- Add DNG metadata/image info read. Perhaps some RAW formats as well.
- Other file formats, eg. WebP.

<a id="roadmap--api"></a>

#### API

- Support reading images incrementally, e.g. page at a time for multi-page TIFFs, to save memory.
- Provide per-image image info in multi-image formats.
- More control over writing.
- Writing multiple images into a file.
- Add support for more than 8 bits per channel.
- Add support for reading and writing detailed XMP metadata fields.
- Add request/hint params to ImageFactory, per Endre's suggestion.
- Allow user to disable autoconversion to sRGB/Grayscale.
- More formats should subclass imagemetadata class to include format-specific info i.e. GIF's transparency index.
- Improve Javadoc and write more FAQs / examples.

<a id="roadmap--test-suite"></a>

#### Test suite

- Publish image library (possibly) and links to other libraries.
- Develop suite of unit tests that only depend on images in the public domain.
- Share test image suite with comments.

---

<a id="project-info"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/project-info.html -->

<!-- page_index: 13 -->

<a id="project-info--project-information"></a>

# Project Information

This document provides an overview of the various documents and links that are part of this project's general information. All of this content is automatically generated by [Maven](https://maven.apache.org) on behalf of the project.

<a id="project-info--overview"></a>

## Overview

| Document | Description |
| --- | --- |
| [About](#index) | Apache Commons Imaging (previously Sanselan) is a pure-Java image library. |
| [Summary](#summary) | This document lists other related information of this project |
| [Team](#team) | This document provides information on the members of this project. These are the individuals who have contributed to the project in one form or another. |
| [Source Code Management](#scm) | This document lists ways to access the online source repository. |
| [Issue Management](https://commons.apache.org/proper/commons-imaging/issue-management.html) | This document provides information on the issue management system used in this project. |
| [Mailing Lists](https://commons.apache.org/proper/commons-imaging/mailing-lists.html) | This document provides subscription and archive information for this project's mailing lists. |
| [Maven Coordinates](https://commons.apache.org/proper/commons-imaging/dependency-info.html) | This document describes how to include this project as a dependency using various dependency management tools. |
| [Dependency Management](https://commons.apache.org/proper/commons-imaging/dependency-management.html) | This document lists the dependencies that are defined through dependencyManagement. |
| [Dependencies](https://commons.apache.org/proper/commons-imaging/dependencies.html) | This document lists the project's dependencies and provides information on each dependency. |
| [Dependency Convergence](https://commons.apache.org/proper/commons-imaging/dependency-convergence.html) | This document presents the convergence of dependency versions across the entire project, and its sub modules. |
| [CI Management](#ci-management) | This document lists the continuous integration management system of this project for building and testing code on a frequent, regular basis. |
| [Distribution Management](https://commons.apache.org/proper/commons-imaging/distribution-management.html) | This document provides informations on the distribution management of this project. |

---

<a id="summary"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/summary.html -->

<!-- page_index: 14 -->

<a id="summary--project-summary"></a>

# Project Summary

<a id="summary--project-information"></a>

## Project Information

| Field | Value |
| --- | --- |
| Name | Apache Commons Imaging |
| Description | Apache Commons Imaging (previously Sanselan) is a pure-Java image library. |
| Homepage | [https://commons.apache.org/proper/commons-imaging/](#index) |

<a id="summary--project-organization"></a>

## Project Organization

| Field | Value |
| --- | --- |
| Name | The Apache Software Foundation |
| URL | <https://www.apache.org/> |

<a id="summary--build-information"></a>

## Build Information

| Field | Value |
| --- | --- |
| GroupId | org.apache.commons |
| ArtifactId | commons-imaging |
| Version | 1.0.0-alpha6 |
| Type | jar |
| Java Version | 1.8 |

---

<a id="team"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/team.html -->

<!-- page_index: 15 -->

<a id="team--project-team"></a>

# Project Team

A successful project requires many people to play many roles. Some members write code or documentation, while others are valuable as testers, submitting patches and suggestions.

The project team is comprised of Members and Contributors. Members have direct access to the source of a project and actively evolve the code-base. Contributors improve the project through submission of patches and suggestions to the Members. The number of Contributors to the project is unbounded. Get involved today. All contributions to the project are greatly appreciated.

<a id="team--members"></a>

## Members

The following is a list of developers with commit privileges that have directly contributed to the project in one way or another.

| Image | Id | Name | Email | URL | Organization | Organization URL | Roles | Time Zone |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | cmchen | Charles M. Chen | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | pkoch | Philipp Koch | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | jeremias | Jeremias Maerki | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | clr | Craig Russell | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | yoavs | Yoav Shapira | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | cziegeler | Carsten Ziegeler | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | damjan | Damjan Jovanovic | - | - | - | - | - | - |
| ![](https://www.gravatar.com/avatar/00000000000000000000000000000000?d=blank&f=y&s=60) | mbenson | Matt Benson | - | - | - | - | - | - |
| ![](https://people.apache.org/~ggregory/img/garydgregory80.png) | ggregory | Gary Gregory | [ggregory at apache.org](mailto:ggregory at apache.org) | <https://www.garygregory.com> | The Apache Software Foundation | <https://www.apache.org/> | PMC Member | America/New\_York |

<a id="team--contributors"></a>

## Contributors

The following additional people have contributed to this project through the way of suggestions, patches or documentation.

Name

Adrian Moerchen

Alex Vigdor

Craig Kelly

Gary Lucas

Gavin Shiels

Peter Royal

Piyush Kapoor

Tars Joris

VVD

Wanja Gayk

Arturo Bernal

---

<a id="ci-management"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/ci-management.html -->

<!-- page_index: 16 -->

<a id="ci-management--overview"></a>

# Overview

This project uses [GitHub Actions](https://github.com/features/actions/).

<a id="ci-management--access"></a>

# Access

The following is a link to the continuous integration system used by the project:

```
https://github.com/apache/commons-parent/actions
```

<a id="ci-management--notifiers"></a>

# Notifiers

No notifiers are defined. Please check back at a later date.

---

<a id="issue-tracking"></a>

<!-- source_url: https://commons.apache.org/proper/commons-imaging/issue-tracking.html -->

<!-- page_index: 17 -->

<a id="issue-tracking--apache-commons-imaging-issue-tracking"></a>

# Apache Commons Imaging Issue tracking

Apache Commons Imaging uses [ASF JIRA](https://issues.apache.org/jira/) for tracking issues.
See the [Apache Commons Imaging JIRA project page](https://issues.apache.org/jira/browse/IMAGING).

To use JIRA you may need to [create an account](https://issues.apache.org/jira/secure/Signup!default.jspa)
(if you have previously created/updated Commons issues using Bugzilla an account will have been automatically
created and you can use the [Forgot Password](https://issues.apache.org/jira/secure/ForgotPassword!default.jspa)
page to get a new password).

If you would like to report a bug, or raise an enhancement request with
Apache Commons Imaging please do the following:

1. [Search existing open bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12313421&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4).
   If you find your issue listed then please add a comment with your details.
2. [Search the mailing list archive(s)](https://commons.apache.org/proper/commons-imaging/mail-lists.html).
   You may find your issue or idea has already been discussed.
3. Decide if your issue is a bug or an enhancement.
4. Submit either a [bug report](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12313421&issuetype=1&priority=4&assignee=-1)
   or [enhancement request](https://issues.apache.org/jira/secure/CreateIssueDetails!init.jspa?pid=12313421&issuetype=4&priority=4&assignee=-1).

Please also remember these points:

- the more information you provide, the better we can help you
- test cases are vital, particularly for any proposed enhancements
- the developers of Apache Commons Imaging are all unpaid volunteers

For more information on creating patches see the
[Apache Contributors Guide](https://www.apache.org/dev/contributors.html).

You may also find these links useful:

- [All Open Apache Commons Imaging bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12313421&sorter/field=issuekey&sorter/order=DESC&status=1&status=3&status=4)
- [All Resolved Apache Commons Imaging bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12313421&sorter/field=issuekey&sorter/order=DESC&status=5&status=6)
- [All Apache Commons Imaging bugs](https://issues.apache.org/jira/secure/IssueNavigator.jspa?reset=true&pid=12313421&sorter/field=issuekey&sorter/order=DESC)

---
