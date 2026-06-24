# What is airflowctl? ¶

## Navigation

- Content
  - [Installation of airflowctl](#installation)
    - [Prerequisites](#installation-prerequisites)
      - Keyring Backend [Recommended]
        - Third-Party Backends
    - [Python Version Compatibility](#installation-prerequisites)
    - [Installing from sources](#installation-installing-from-sources)
      - Released packages
      - Release integrity
      - Verifying PyPI releases
    - [Installing from PyPI](#installation-installing-from-pypi)
      - Installation tools
    - [Using released sources](#installation)
    - [Using PyPI](#installation)
  - [How-to Guides](#howto)
    - How to use airflowctl
      - Important Note
      - Datetime Usage
      - Login
        - What is authentication for airflowctl ?
        - Parameter Details for airflowctl auth login
      - More Usage and Help Pictures
    - All Available Group Command References
      - Assets
      - Auth
      - Backfill
      - Config
      - Connections
      - Dags
      - Dag Runs
      - Jobs
      - Pools
      - Providers
      - Variables
      - Version
  - [Security](#security)
  - [Release Notes](https://airflow.apache.org/docs/apache-airflow-ctl/stable/release_notes.html)
- Usage
  - [Quick Start](#start)
  - [References](#cli-and-env-variables-ref)
    - CLI
      - Positional Arguments
      - Sub-commands
        - assets
          - Positional Arguments
          - Sub-commands
            - create-event
              - Named Arguments
            - delete-dag-queued-events
              - Named Arguments
            - delete-queued-event
              - Named Arguments
            - delete-queued-events
              - Named Arguments
            - get
              - Named Arguments
            - get-by-alias
              - Named Arguments
            - get-dag-queued-event
              - Named Arguments
            - get-dag-queued-events
              - Named Arguments
            - get-queued-events
              - Named Arguments
            - list
              - Named Arguments
            - list-by-alias
              - Named Arguments
            - materialize
              - Named Arguments
        - auth
          - Positional Arguments
          - Sub-commands
            - list-envs
              - Named Arguments
            - login
              - Named Arguments
            - token
              - Named Arguments
        - backfill
          - Positional Arguments
          - Sub-commands
            - cancel
              - Named Arguments
            - create
              - Named Arguments
            - create-dry-run
              - Named Arguments
            - get
              - Named Arguments
            - list
              - Named Arguments
            - pause
              - Named Arguments
            - unpause
              - Named Arguments
        - config
          - Positional Arguments
          - Sub-commands
            - get
              - Named Arguments
            - lint
              - Named Arguments
            - list
              - Named Arguments
        - connections
          - Positional Arguments
          - Sub-commands
            - create
              - Named Arguments
            - create-defaults
              - Named Arguments
            - delete
              - Named Arguments
            - get
              - Named Arguments
            - import
              - Positional Arguments
              - Named Arguments
            - list
              - Named Arguments
            - test
              - Named Arguments
            - update
              - Named Arguments
        - dagrun
          - Positional Arguments
          - Sub-commands
            - get
              - Named Arguments
            - list
              - Named Arguments
        - dags
          - Positional Arguments
          - Sub-commands
            - delete
              - Named Arguments
            - get
              - Named Arguments
            - get-details
              - Named Arguments
            - get-import-error
              - Named Arguments
            - get-stats
              - Named Arguments
            - get-tags
              - Named Arguments
            - get-version
              - Named Arguments
            - list
              - Named Arguments
            - list-import-errors
              - Named Arguments
            - list-version
              - Named Arguments
            - list-warning
              - Named Arguments
            - pause
              - Positional Arguments
              - Named Arguments
            - trigger
              - Named Arguments
            - unpause
              - Positional Arguments
              - Named Arguments
            - update
              - Named Arguments
        - jobs
          - Positional Arguments
          - Sub-commands
            - list
              - Named Arguments
        - pools
          - Positional Arguments
          - Sub-commands
            - create
              - Named Arguments
            - delete
              - Named Arguments
            - export
              - Positional Arguments
              - Named Arguments
            - get
              - Named Arguments
            - import
              - Positional Arguments
              - Named Arguments
            - list
              - Named Arguments
            - update
              - Named Arguments
        - providers
          - Positional Arguments
          - Sub-commands
            - list
              - Named Arguments
        - variables
          - Positional Arguments
          - Sub-commands
            - create
              - Named Arguments
            - delete
              - Named Arguments
            - get
              - Named Arguments
            - import
              - Positional Arguments
              - Named Arguments
            - list
              - Named Arguments
            - update
              - Named Arguments
        - version
          - Named Arguments
        - xcom
          - Positional Arguments
          - Sub-commands
            - add
              - Named Arguments
            - delete
              - Named Arguments
            - edit
              - Named Arguments
            - get
              - Named Arguments
            - list
              - Named Arguments
    - Environment Variables
- [Home](#index)

## Content

<a id="installation"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/installation/index.html -->

<!-- page_index: 1 -->

# Installation of airflowctl ¶

<svg fill="currentColor" height="16" viewbox="0 0 16 16" width="16">
<path></path>
</svg>

`↑↓` Navigate
`⏎` Select
`Esc` Close

# Installation of airflowctl

- [Using released sources](#installation--using-released-sources)
- [Using PyPI](#installation--using-pypi)

This page describes installations options that you might use when considering how to install Airflow®.
Airflow consists of many components, often distributed among many physical or virtual machines, therefore
installation of Airflow might be quite complex, depending on the options you choose.

## [Using released sources](#installation--id1)

More details: [Installing from Sources](#installation-installing-from-sources)

**When this option works best**

- This option is best if you expect to build all your software from sources.
- Apache Airflow is one of the projects that belong to the [Apache Software Foundation](https://www.apache.org/).
  It is a requirement for all ASF projects that they can be installed using official sources released via [Official Apache Downloads](https://dlcdn.apache.org/).
- This is the best choice if you have a strong need to [verify the integrity and provenance of the software](https://www.apache.org/dyn/closer.cgi#verify)

**Intended users**

- Users who are familiar with installing and building software from sources and are conscious about integrity and provenance
  of the software they use down to the lowest level possible.

**What are you expected to handle**

- You are expected to build and install airflow and its components on your own.
- You should develop and handle the deployment for all components of Airflow.
- You are responsible for setting up database, creating and managing database schema with `airflow db` commands,
  automated startup and recovery, maintenance, cleanup and upgrades of Airflow and the Airflow Providers.
- You need to setup monitoring of your system allowing you to observe resources and react to problems.
- You are expected to configure and manage appropriate resources for the installation (memory, CPU, etc) based
  on the monitoring of your installation and feedback loop. See the notes about requirements.

**What Apache Airflow Community provides for that method**

- You have [instructions](https://github.com/apache/airflow/blob/main/INSTALL) on how to build the software but due to various environments
  and tools you might want to use, you might expect that there will be problems which are specific to your deployment and environment
  you will have to diagnose and solve.

**Where to ask for help**

- The `#user-troubleshooting` channel on slack can be used for quick general troubleshooting questions. The
  [GitHub discussions](https://github.com/apache/airflow/discussions) if you look for longer discussion and have more information to share.
- The `#user-best-practices` channel on slack can be used to ask for and share best practices on using and deploying airflow.
- If you can provide description of a reproducible problem with Airflow software, you can open issue at [GitHub issues](https://github.com/apache/airflow/issues)
- If you want to contribute back to Airflow, the `#contributors` slack channel for building the Airflow itself

## [Using PyPI](#installation--id2)

More details: [Installation from PyPI](#installation-installing-from-pypi)

**When this option works best**

- This installation method is useful when you are not familiar with Containers and Docker and want to install
  Apache Airflow on physical or virtual machines and you are used to installing and running software using custom
  deployment mechanism.
- The only officially supported mechanism of installation is via `pip` using constraint mechanisms. The constraint
  files are managed by Apache Airflow release managers to make sure that you can repeatably install Airflow from PyPI with all Providers and
  required dependencies.
- In case of PyPI installation you could also verify integrity and provenance of the packages
  downloaded from PyPI as described at the installation page, but software you download from PyPI is pre-built
  for you so that you can install it without building, and you do not build the software from sources.

**Intended users**

- Users who are familiar with installing and configuring Python applications, managing Python environments,
  dependencies and running software with their custom deployment mechanisms.

**What are you expected to handle**

- You are expected to install airflowctl.
- You should run the Airflow API server.
- You need to setup monitoring of your system allowing you to observe resources and react to problems.

**What Apache Airflow Community provides for that method**

- You have [Installation from PyPI](#installation-installing-from-pypi)
  on how to install the software but due to various environments and tools you might want to use, you might
  expect that there will be problems which are specific to your deployment and environment you will have to
  diagnose and solve.
- You have [Quick Start](#start) where you can see an example of Quick Start with running Airflow
  locally which you can use to start Airflow quickly for local testing and development.
  However, this is just for inspiration. Do not expect [Quick Start](#start) is ready for production installation,
  you need to build your own production-ready deployment if you follow this approach.

**Where to ask for help**

- The `#user-troubleshooting` channel on Airflow Slack for quick general
  troubleshooting questions. The [GitHub discussions](https://github.com/apache/airflow/discussions)
  if you look for longer discussion and have more information to share.
- The `#user-best-practices` channel on slack can be used to ask for and share best
  practices on using and deploying airflow.
- If you can provide description of a reproducible problem with Airflow software, you can open
  issue at [GitHub issues](https://github.com/apache/airflow/issues)

[Previous](#index "What is airflowctl?")
[Next](#installation-prerequisites "Prerequisites")

---

<a id="installation-prerequisites"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/installation/prerequisites.html -->

<!-- page_index: 2 -->

# Prerequisites ¶

<svg fill="currentColor" height="16" viewbox="0 0 16 16" width="16">
<path></path>
</svg>

`↑↓` Navigate
`⏎` Select
`Esc` Close

# Prerequisites

airflowctl is tested with:

The minimum memory required we recommend airflowctl to run with is 200MB, but the actual requirements depend
wildly on the deployment options you have.
The Keyring backend needs to be installed separately into your operating system. This will enhance security. See [Security](#security) for more information.

## Keyring Backend [Recommended]

airflowctl uses keyring to store the API token securely. This ensures that the token is not stored in plain text and is only accessible to authorized users.

Recommended keyring backends are:

- [macOS Keychain](https://en.wikipedia.org/wiki/Keychain_%28software%29)
- [Freedesktop Secret Service](http://standards.freedesktop.org/secret-service/) supports many DE including GNOME (requires [secretstorage](https://pypi.python.org/pypi/secretstorage))
- [KDE4 & KDE5 KWallet](https://en.wikipedia.org/wiki/KWallet) (requires [dbus](https://pypi.python.org/pypi/dbus-python))
- [Windows Credential Locker](https://docs.microsoft.com/en-us/windows/uwp/security/credential-locker)

In case there’s no keyring available (common in headless environments) you can provide the token to each command. See [Security](#security) for more information.

### Third-Party Backends

In addition to the backends provided by the core keyring package for
the most common and secure use cases, there
are additional keyring backend implementations available for other
use cases. Simply install them to make them available:

- [keyrings.cryptfile](https://pypi.org/project/keyrings.cryptfile)
  :   - Encrypted text file storage.
- [keyrings.alt](https://pypi.org/project/keyrings.alt)
  :   - “alternate”, possibly-insecure backends, originally part of the core package, but available for opt-in.
- [gsheet-keyring](https://pypi.org/project/gsheet-keyring)
  :   - a backend that stores secrets in a Google Sheet. For use with [ipython-secrets](https://pypi.org/project/ipython-secrets).
- [bitwarden-keyring](https://pypi.org/project/bitwarden-keyring/)
  :   - a backend that stores secrets in the [BitWarden](https://bitwarden.com/) password manager.
- [onepassword-keyring](https://pypi.org/project/onepassword-keyring/)
  :   - a backend that stores secrets in the [1Password](https://1password.com/) password manager.
- [sagecipher](https://pypi.org/project/sagecipher)
  :   - an encryption backend which uses the ssh agent protocol’s signature operation to derive the cipher key.
- [keyrings.osx\_keychain\_keys](https://pypi.org/project/keyrings.osx-keychain-keys)
  :   - `OSX keychain key-management`, for private, public, and symmetric keys.
- [keyring\_pass.PasswordStoreBackend](https://github.com/nazarewk/keyring_pass)
  :   - Password Store (pass) backend for python’s keyring
- [keyring\_jeepney](https://pypi.org/project/keyring_jeepney)
  :   - a pure Python backend using the secret service `DBus` API for desktop Linux (requires `keyring<24`).

# Python Version Compatibility

`airflowctl` is compatible with versions of Python 3.10 through Python 3.14.
Currently, Python 3.14 is not supported. Thanks for your understanding!
We will work on adding support for Python 3.14.

| Python Version | Supported |
| --- | --- |
| 3.10 | Yes |
| 3.11 | Yes |
| 3.12 | Yes |
| 3.13 | Yes |
| 3.14 | No |

[Previous](#installation "Installation of airflowctl")
[Next](#installation-installing-from-sources "Installing from Sources")

---

<a id="installation-installing-from-sources"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/installation/installing-from-sources.html -->

<!-- page_index: 3 -->

# Installing from Sources ¶

<svg fill="currentColor" height="16" viewbox="0 0 16 16" width="16">
<path></path>
</svg>

`↑↓` Navigate
`⏎` Select
`Esc` Close

# Installing from Sources

## Released packages

This page describes downloading and verifying Airflow Ctl version `0.1.3` using officially released packages.
You can also install `airflowctl` - as most Python packages - via [PyPI](#installation-installing-from-pypi).
You can choose different version of Airflow by selecting a different version from the drop-down at
the top-left of the page.

The Source packages are official packages of the Apache Software Foundation - and the ones that you can
use is you want to build the packages yourself from the source code and be sure that the provenance of
the packages is verified and matches the source code from the repository and you can verify the
checksums and signatures of the packages.

The `sdist` and `whl` packages released are the convenience packages - of installation also installed from
the same sources and you can still verify the origin of the packages and want to verify checksums and
signatures of the packages. The packages are available via the Official Apache Software Foundations Downloads
[Official Apache Software Foundations Downloads](https://dlcdn.apache.org/)

The `0.1.3` downloads of Airflow Ctl are available at:

- [Sources package for airflow-ctl:](https://www.apache.org/dyn/closer.lua/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3-source.tar.gz) ([asc](https://downloads.apache.org/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3-source.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3-source.tar.gz.sha512))
- [Sdist package for airflow-ctl distributions](https://www.apache.org/dyn/closer.lua/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3.tar.gz) ([asc](https://downloads.apache.org/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3.tar.gz.sha512))
- [Whl package for airflow-ctl distribution](https://www.apache.org/dyn/closer.lua/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/airflow-ctl/0.1.3/apache_airflow_ctl-0.1.3-py3-none-any.whl.sha512))

If you want to install from the source code, you can download from the sources link above, it will contain
a `INSTALL` file containing details on how you can build and install airflowctl.

## Release integrity

[PGP signatures KEYS](https://downloads.apache.org/airflowctl/KEYS)

It is essential that you verify the integrity of the downloaded files using the PGP or SHA signatures.
The PGP signatures can be verified using GPG or PGP. Please download the KEYS as well as the asc
signature files for relevant distribution. It is recommended to get these files from the
main distribution directory and not from the mirrors.

```
gpg -i KEYS
```

or

```
pgpk -a KEYS
```

or

```
pgp -ka KEYS
```

To verify the binaries/sources you can download the relevant asc files for it from main
distribution directory and follow the below guide.

```
gpg --verify apache-airflow-ctl-********.asc apache-airflow-ctl-*********
```

or

```
pgpv apache-airflow-ctl-********.asc
```

or

```
pgp apache-airflow-********.asc
```

Example:

```
$ gpg --verify apache-airflow-ctl-0.1.3-source.tar.gz.asc apache-airflow-ctl-0.1.3-source.tar.gz gpg: Signature made Sat 11 Sep 12:49:54 2021 BST gpg: using RSA key CDE15C6E4D3A8EC4ECF4BA4B6674E08AD7DE406F gpg: issuer "kaxilnaik@apache.org" gpg: Good signature from "Kaxil Naik <kaxilnaik@apache.org>" [unknown] gpg: aka "Kaxil Naik <kaxilnaik@gmail.com>" [unknown] gpg: WARNING: The key's User ID is not certified with a trusted signature! gpg: There is no indication that the signature belongs to the owner. Primary key fingerprint: CDE1 5C6E 4D3A 8EC4 ECF4 BA4B 6674 E08A D7DE 406F
```

The “Good signature from …” is indication that the signatures are correct.
Do not worry about the “not certified with a trusted signature” warning. Most of the certificates used
by release managers are self signed, that’s why you get this warning. By importing the server in the
previous step and importing it via ID from `KEYS` page, you know that this is a valid Key already.

For SHA512 sum check, download the relevant `sha512` and run the following:

```
shasum -a 512 apache-airflow-ctl--********  | diff - apache-airflow-ctl--********.sha512
```

The `SHASUM` of the file should match the one provided in `.sha512` file.

Example:

```
shasum -a 512 apache-airflow-ctl-0.1.3-source.tar.gz  | diff - apache-airflow-ctl-0.1.3-source.tar.gz.sha512
```

## Verifying PyPI releases

You can verify the airflowctl `.whl` packages from PyPI by locally downloading the package and signature
and SHA sum files with the script below:

```
#!/bin/bash
airflowctl_version="0.1.3"
ctl_download_dir="$(mktemp -d)"
pip download --no-deps "apache-airflow-ctl==${airflowctl_version}" --dest "${airflow_download_dir}"
curl "https://downloads.apache.org/airflowctl/${airflowctl_version}/apache_airflow_ctl-${airflowctl_version}-py3-none-any.whl.asc" \
    -L -o "${airflowctl_download_dir}/apache_airflow_ctl-${airflowctl_version}-py3-none-any.whl.asc"
curl "https://downloads.apache.org/airflow/${airflowctl_version}/apache_airflow_ctl-${airflowctl_version}-py3-none-any.whl.sha512" \
    -L -o "${airflowctl_download_dir}/apache_airflow_ctl-${airflowctl_version}-py3-none-any.whl.sha512"
echo
echo "Please verify files downloaded to ${airflowctl_download_dir}"
ls -la "${airflowctl_download_dir}"
echo
```

Once you verify the files following the instructions from previous chapter you can remove the temporary
folder created.

[Previous](#installation-prerequisites "Prerequisites")
[Next](#installation-installing-from-pypi "Installation from PyPI")

---

<a id="installation-installing-from-pypi"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/installation/installing-from-pypi.html -->

<!-- page_index: 4 -->

# Installation from PyPI ¶

> [!NOTE]
> > [!NOTE]
> > `↑↓` Navigate
> > `⏎` Select
> > `Esc` Close
> >
> > # Installation from PyPI
> >
> > This page describes installations using the `apache-airflow-ctl` package [published in
> > PyPI](https://pypi.org/project/apache-airflow-ctl/).
> >
> > ## Installation tools
> >
> > Only `pip` and `uv` installation is currently officially supported.
> >
> > > [!NOTE]
> > > While there are some successes with using other tools like [poetry](https://python-poetry.org/) or
> > > [pip-tools](https://pypi.org/project/pip-tools/), they do not share the same workflow as
> > > `pip` - especially when it comes to constraint vs. requirements management.
> > > Installing via `Poetry` or `pip-tools` is not currently supported. If you wish to install airflow
> > > using those tools you should use the constraints and convert them to appropriate
> > > format and workflow that your tool requires. Uv follows `pip` approach
> > > with `uv pip` so it should work similarly.
> > >
> > > There are known issues with `bazel` that might lead to circular dependencies when using it to install
> > > Airflow. Please switch to `pip` if you encounter such problems. `Bazel` community works on fixing
> > > the problem in [this PR](https://github.com/bazelbuild/rules_python/pull/1166) so it might be that
> > > newer versions of `bazel` will handle it.
> >
> > Typical command to install airflowctl from scratch in a reproducible way from PyPI looks like below:
> >
> > ```
> > pip install "apache-airflow-ctl==0.1.3"
> > ```
> >
> > Those are just examples, see further for more explanation why those are the best practices.
> >
> > > [!NOTE]
> > > Generally speaking, Python community established practice is to perform application installation in a
> > > virtualenv created with `virtualenv` or `venv` tools. You can also use `uv` or `pipx` to install
> > > Airflow in application dedicated virtual environment created for you. There are also other tools that can be used
> > > to manage your virtualenv installation and you are free to choose how you are managing the environments.
> > > Airflow has no limitation regarding to the tool of your choice when it comes to virtual environment.
> > >
> > > The only exception where you might consider not using virtualenv is when you are building a container
> > > image with only Airflow installed - this is for example how Airflow is installed in the official Container
> > > image.
> >
> > [Previous](#installation-installing-from-sources "Installing from Sources")
> > [Next](#howto "How-to Guides")

---

<a id="howto"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/howto/index.html -->

<!-- page_index: 5 -->

# How-to Guides ¶

<svg fill="currentColor" height="16" viewbox="0 0 16 16" width="16">
<path></path>
</svg>

`↑↓` Navigate
`⏎` Select
`Esc` Close

# How-to Guides

Setting up the sandbox in the [Quick Start](#start) section was easy;
building a production-grade environment requires a bit more work!

These how-to guides will step you through common tasks in using and
configuring an airflowctl environment.

## How to use airflowctl

### **Important Note**

airflowctl needs the Airflow API running to be able to work. Please, see the login section below before use.
Otherwise, you may get errors.

### Datetime Usage

For datetime parameters, date should be timezone aware and in ISO format.
For example: `2025-10-10T10:00:00+00:00`
Let’s take example of triggering a DAG run with a logical date, run after and a note.

```
airflowctl dagrun trigger --dag-id="example_bash_operator" --logical-date="2025-09-06T00:00:00+00:00" --run-after="2025-09-06T00:00:00+00:00" --note="Triggered from airflowctl"
```

### Login

airflowctl needs to be able to connect to the Airflow API. You should pass API URL as a parameter to the command
`--api-url`. The URL should be in the form of `http(s)://<host>:<port>`.
You can also set the environment variable `AIRFLOW_CLI_TOKEN` to the token to use for authentication.

There are two ways to authenticate with the Airflow API:

1. Using a token acquired from the Airflow API

```
airflowctl auth login --api-url <api_url> --api-token <token> --env <env_name:production>
```

2. Using a username and password

```
airflowctl auth login --api-url <api_url> --username <username> --password <password> --env <env_name:production>
```

If there’s no keyring available, common in headless systems like docker images, you can still use the tool by setting
the environment variable `AIRFLOW_CLI_TOKEN`.

```
export AIRFLOW_CLI_TOKEN=<token>
airflowctl auth login --api-url <api_url> --env <env_name:production> --skip-keyring
```

In both cases token is securely stored in the keyring backend. Only configuration persisted in `~/.config/airflow` file
is the API URL and the environment name. The token is stored in the keyring backend and is not persisted in the
configuration file. The keyring backend is used to securely store the token and is not accessible to the user.

#### What is authentication for `airflowctl`?

For `airflowctl` to be able to communicate with the Airflow API, it needs to authenticate itself and acquire token.
This is done using either a token or a username and password.
The token can be acquired from the Airflow API or generated using a username and password.

[![airflowctl Auth Login Help](assets/images/airflowctl-api-network-architecture-diagram_b54a1e92b784734f.png)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/diagrams/airflowctl_api_network_architecture_diagram.png)

#### Parameter Details for airflowctl auth login

**–api-url**: This parameter is required. (e.g. `http://localhost:8080`)
The default value is `http://localhost:8080`. Full URL of the Airflow API. Without any `/api/*` suffixes.
If you are running the `airflowctl` in `breeze` container, it is optional.

**–api-token**: This parameter is optional.
If you are setting the token via the environment variable `AIRFLOW_CLI_TOKEN`, you can skip using this parameter.

**–username**: This parameter is optional.
If you are not using `--api-token` or the environment variable `AIRFLOW_CLI_TOKEN`, you must provide a username to authentication along with `--password`.

**–password**: This parameter is optional.
If you provide a username via `--username` this is the required password to authenticate.

**–env**: This parameter is optional.
The name of the environment to create or update. The default value is `production`.
This parameter is useful when you want to manage multiple Airflow environments.

**–skip-keyring**: This parameter is optional.
Useful when there’s no keyring available in the system where airflowctl is running.
Set `AIRFLOW_CLI_TOKEN` or use the `--api-token` flag for next commands.

### More Usage and Help Pictures

For more information use

```
airflowctl auth login --help
```

[![airflowctl Auth Login Help](assets/images/output-auth-login_588189fe090a7152.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_auth_login.svg)

You are ready to use airflowctl now.
Please, also see [Command Line Interface and Environment Variables Reference](#cli-and-env-variables-ref) for the list of available commands and options.

You can use the command `airflowctl --help` to see the list of available commands.

[![airflowctl Help](assets/images/output-main_0f568cfe3d8b4d65.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_main.svg)

## All Available Group Command References

Below are the command reference diagrams for all available commands in airflowctl.
These visual references show the full command syntax, options, and parameters for each command.

### **Assets**

[![airflowctl Assets Command](assets/images/output-assets_dfc1796afa994440.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_assets.svg)

### **Auth**

[![airflowctl Auth Command](assets/images/output-auth_7515eb3e7f7d14c5.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_auth.svg)

### **Backfill**

[![airflowctl Backfills Command](assets/images/output-backfill_5d21fc319b3328c2.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_backfill.svg)

### **Config**

[![airflowctl Config Command](assets/images/output-config_8b868caf47dd7ef0.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_config.svg)

### **Connections**

[![airflowctl Connections Command](assets/images/output-connections_7e0a567509ebb8ba.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_connections.svg)

### **Dags**

[![airflowctl Dag Command](assets/images/output-dags_610a2541e8ae8504.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_dags.svg)

### **Dag Runs**

[![airflowctl Dag Run Command](assets/images/output-dagrun_533b9e919151e0a5.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_dagrun.svg)

### **Jobs**

[![airflowctl Jobs Command](assets/images/output-jobs_1d157e065edd1a8a.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_jobs.svg)

### **Pools**

[![airflowctl Pools Command](assets/images/output-pools_4083ff293a5e456b.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_pools.svg)

### **Providers**

[![airflowctl Providers Command](assets/images/output-providers_14943716f976c636.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_providers.svg)

### **Variables**

[![airflowctl Variables Command](assets/images/output-variables_78dfd67ca6c5fe9b.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_variables.svg)

### **Version**

[![airflowctl Version Command](assets/images/output-version_119d414978a99031.svg)](https://raw.githubusercontent.com/apache/airflow/main/airflow-ctl/docs/images/output_version.svg)

[Previous](#installation-installing-from-pypi "Installation from PyPI")
[Next](#security "Security")

---

<a id="security"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/security.html -->

<!-- page_index: 6 -->

# Security ¶

<svg fill="currentColor" height="16" viewbox="0 0 16 16" width="16">
<path></path>
</svg>

`↑↓` Navigate
`⏎` Select
`Esc` Close

# Security

airflowctl is leveraging Apache Airflow Public API security features and additional layers of security to ensure that your data is safe and secure.
airflowctl facilitates the seamless deployment of CLI and API features together, reducing redundancy and simplifying maintenance. Transitioning from direct database access to an API-driven model will enhance the CLI’s capabilities and improve security.

- **Authentication**: airflowctl uses authentication to ensure that only authorized users can access the system. This is done using an API Token. See more on <https://airflow.apache.org/docs/apache-airflow/stable/security/api.html>
- **Keyring**: airflowctl uses keyring to store the API Token securely. This ensures that the Token is not stored in plain text and is only accessible to authorized users.
  :   - In case no keyring is available, you can set the `AIRFLOW_CLI_TOKEN` environment variable or the `--api-token` flag for each command. Be cautious of not exposing this token to others.

airflowctl API Token has its own expiration time. The default is 1 hour. You can change it in the Airflow configuration file (airflow.cfg) by setting the `jwt_cli_expiration_time` parameter under the `[api_auth]` section. The value is in seconds. This will impact all users using `airflowctl`.

For more information see [Setting Configuration
Options](https://airflow.apache.org/docs/apache-airflow/stable/howto/set-config.html).

[Previous](#howto "How-to Guides")
[Next](https://airflow.apache.org/docs/apache-airflow-ctl/stable/release_notes.html "Release Notes")

---

<a id="start"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/start.html -->

<!-- page_index: 7 -->

# Quick Start ¶

<svg fill="currentColor" height="16" viewbox="0 0 16 16" width="16">
<path></path>
</svg>

`↑↓` Navigate
`⏎` Select
`Esc` Close

# Quick Start

Let’s first install `airflowctl` if you haven’t already:

From PyPI: [Installation from PyPI](#installation-installing-from-pypi)

From source: [Installing from Sources](#installation-installing-from-sources)

airflowctl is a command line tool that helps you manage your Airflow deployments.
It is designed to be easy to use and provides a simple interface for managing your Airflow environment.

To get started, you can use the following command to create a new airflowctl environment:

```
airflowctl auth login --username <username> --password <password> --api-url <api_url> --env <env_name>
```

To persist the environment, you can set `AIRFLOW_CLI_ENVIRONMENT`.
The environment variable should be the name of the environment you want to use.
This will allow users to switch environments easily.

OR

```
export AIRFLOW_CLI_TOKEN=<token>
airflowctl auth login --api-url <api_url> --env <env_name>
```

This command will create a new airflowctl environment with the specified username and password.
You can then use the following command to start the airflowctl environment:

```
airflowctl --help
```

[Previous](https://airflow.apache.org/docs/apache-airflow-ctl/stable/release_notes.html "Release Notes")
[Next](#cli-and-env-variables-ref "Command Line Interface and Environment Variables Reference")

---

<a id="cli-and-env-variables-ref"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/cli-and-env-variables-ref.html -->

<!-- page_index: 8 -->

# Command Line Interface and Environment Variables Reference ¶

> [!NOTE]
> `↑↓` Navigate
> `⏎` Select
> `Esc` Close
>
> # Command Line Interface and Environment Variables Reference
>
> ## CLI
>
> airflowctl has a very rich command line interface that allows for
> many types of operation on a Dag, starting services, and supporting
> development and testing.
>
> > [!NOTE]
> > **For more information on usage CLI, see Command Line Interface and Environment Variables Reference**
> >
>
> Content
>
> - [Positional Arguments](#cli-and-env-variables-ref--airflowctl.ctl.cli_parser-get_parser-positional-arguments)
> - [Sub-commands](#cli-and-env-variables-ref--sub-commands)
>
>   - [assets](#cli-and-env-variables-ref--assets)
>   - [auth](#cli-and-env-variables-ref--auth)
>   - [backfill](#cli-and-env-variables-ref--backfill)
>   - [config](#cli-and-env-variables-ref--config)
>   - [connections](#cli-and-env-variables-ref--connections)
>   - [dagrun](#cli-and-env-variables-ref--dagrun)
>   - [dags](#cli-and-env-variables-ref--dags)
>   - [jobs](#cli-and-env-variables-ref--jobs)
>   - [pools](#cli-and-env-variables-ref--pools)
>   - [providers](#cli-and-env-variables-ref--providers)
>   - [variables](#cli-and-env-variables-ref--variables)
>   - [version](#cli-and-env-variables-ref--version)
>   - [xcom](#cli-and-env-variables-ref--xcom)
>
> ```
>
> Usage
> :
> airflowctl
> [
> -
> h
> ]
> GROUP_OR_COMMAND
> ...
> ```
>
> ### [Positional Arguments](#cli-and-env-variables-ref--id1)
>
> `GROUP_OR_COMMAND`
> :   Possible choices: assets, auth, backfill, config, connections, dagrun, dags, jobs, pools, providers, variables, version, xcom
>
> ### [Sub-commands](#cli-and-env-variables-ref--id2)
>
> #### [assets](#cli-and-env-variables-ref--id3)
>
> Perform Assets operations
>
> ```
>
> airflowctl
> assets
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: create-event, delete-dag-queued-events, delete-queued-event, delete-queued-events, get, get-by-alias, get-dag-queued-event, get-dag-queued-events, get-queued-events, list, list-by-alias, materialize
>
> ##### Sub-commands
>
> ###### create-event
>
> Perform create\_event operation
>
> ```
>
> airflowctl
> assets
> create
> -
> event
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> asset
> -
> id
> ASSET_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> extra
> EXTRA
> ]
> [
> --
> partition
> -
> key
> PARTITION_KEY
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--asset-id`
> :   asset\_id for asset\_event\_body operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--extra`
> :   extra for asset\_event\_body operation
>
> `--partition-key`
> :   partition\_key for asset\_event\_body operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### delete-dag-queued-events
>
> Perform delete\_dag\_queued\_events operation
>
> ```
>
> airflowctl
> assets
> delete
> -
> dag
> -
> queued
> -
> events
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> before
> BEFORE
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--before`
> :   before for delete\_dag\_queued\_events operation in AssetsOperations
>
> `--dag-id`
> :   dag\_id for delete\_dag\_queued\_events operation in AssetsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### delete-queued-event
>
> Perform delete\_queued\_event operation
>
> ```
>
> airflowctl
> assets
> delete
> -
> queued
> -
> event
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> asset
> -
> id
> ASSET_ID
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--asset-id`
> :   asset\_id for delete\_queued\_event operation in AssetsOperations
>
> `--dag-id`
> :   dag\_id for delete\_queued\_event operation in AssetsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### delete-queued-events
>
> Perform delete\_queued\_events operation
>
> ```
>
> airflowctl
> assets
> delete
> -
> queued
> -
> events
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> asset
> -
> id
> ASSET_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--asset-id`
> :   asset\_id for delete\_queued\_events operation in AssetsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> assets
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> asset
> -
> id
> ASSET_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--asset-id`
> :   asset\_id for get operation in AssetsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-by-alias
>
> Perform get\_by\_alias operation
>
> ```
>
> airflowctl
> assets
> get
> -
> by
> -
> alias
> [
> -
> h
> ]
> [
> --
> alias
> ALIAS
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--alias`
> :   alias for get\_by\_alias operation in AssetsOperations
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-dag-queued-event
>
> Perform get\_dag\_queued\_event operation
>
> ```
>
> airflowctl
> assets
> get
> -
> dag
> -
> queued
> -
> event
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> asset
> -
> id
> ASSET_ID
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--asset-id`
> :   asset\_id for get\_dag\_queued\_event operation in AssetsOperations
>
> `--dag-id`
> :   dag\_id for get\_dag\_queued\_event operation in AssetsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-dag-queued-events
>
> Perform get\_dag\_queued\_events operation
>
> ```
>
> airflowctl
> assets
> get
> -
> dag
> -
> queued
> -
> events
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> before
> BEFORE
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--before`
> :   before for get\_dag\_queued\_events operation in AssetsOperations
>
> `--dag-id`
> :   dag\_id for get\_dag\_queued\_events operation in AssetsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-queued-events
>
> Perform get\_queued\_events operation
>
> ```
>
> airflowctl
> assets
> get
> -
> queued
> -
> events
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> asset
> -
> id
> ASSET_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--asset-id`
> :   asset\_id for get\_queued\_events operation in AssetsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> assets
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list-by-alias
>
> Perform list\_by\_alias operation
>
> ```
>
> airflowctl
> assets
> list
> -
> by
> -
> alias
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### materialize
>
> Perform materialize operation
>
> ```
>
> airflowctl
> assets
> materialize
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> asset
> -
> id
> ASSET_ID
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--asset-id`
> :   asset\_id for materialize operation in AssetsOperations
>
> #### [auth](#cli-and-env-variables-ref--id4)
>
> Manage authentication for CLI. Either pass token from environment variable/parameter or pass username and password.
>
> ```
>
> airflowctl
> auth
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: list-envs, login, token
>
> ##### Sub-commands
>
> ###### list-envs
>
> List all CLI environments with their authentication status
>
> ```
>
> airflowctl
> auth
> list
> -
> envs
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### login
>
> Login to the metadata database
>
> ```
>
> airflowctl
> auth
> login
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> api
> -
> url
> API_URL
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> password
> PASSWORD
> ]
> [
> --
> skip
> -
> keyring
> ]
> [
> --
> username
> USERNAME
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--api-url`
> :   The URL of the metadata database API
>
>     Default: `'http://localhost:8080'`
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--password`
> :   The password to use for authentication
>
> `--skip-keyring`
> :   Skip storing credentials in keyring
>
>     Default: `False`
>
> `--username`
> :   The username to use for authentication
>
> ###### token
>
> Authenticate with username and password and print the access token to stdout. Username and password are prompted interactively if not provided.
>
> ```
>
> airflowctl
> auth
> token
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> api
> -
> url
> API_URL
> ]
> [
> --
> password
> PASSWORD
> ]
> [
> --
> username
> USERNAME
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--api-url`
> :   The URL of the metadata database API
>
>     Default: `'http://localhost:8080'`
>
> `--password`
> :   The password to use for authentication
>
> `--username`
> :   The username to use for authentication
>
> #### [backfill](#cli-and-env-variables-ref--id5)
>
> Perform Backfill operations
>
> ```
>
> airflowctl
> backfill
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: cancel, create, create-dry-run, get, list, pause, unpause
>
> ##### Sub-commands
>
> ###### cancel
>
> Perform cancel operation
>
> ```
>
> airflowctl
> backfill
> cancel
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> backfill
> -
> id
> BACKFILL_ID
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--backfill-id`
> :   backfill\_id for cancel operation in BackfillOperations
>
> ###### create
>
> Perform create operation
>
> ```
>
> airflowctl
> backfill
> create
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> conf
> DAG_RUN_CONF
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> from
> -
> date
> FROM_DATE
> ]
> [
> --
> max
> -
> active
> -
> runs
> MAX_ACTIVE_RUNS
> ]
> [
> --
> reprocess
> -
> behavior
> REPROCESS_BEHAVIOR
> ]
> [
> --
> run
> -
> backwards
> |
> --
> no
> -
> run
> -
> backwards
> ]
> [
> --
> run
> -
> on
> -
> latest
> -
> version
> |
> --
> no
> -
> run
> -
> on
> -
> latest
> -
> version
> ]
> [
> --
> to
> -
> date
> TO_DATE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for backfill operation
>
> `--dag-run-conf`
> :   dag\_run\_conf for backfill operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--from-date`
> :   from\_date for backfill operation
>
> `--max-active-runs`
> :   max\_active\_runs for backfill operation
>
> `--reprocess-behavior`
> :   reprocess\_behavior for backfill operation
>
> `--run-backwards, --no-run-backwards`
> :   run\_backwards for backfill operation (default: False)
>
>     Default: `False`
>
> `--run-on-latest-version, --no-run-on-latest-version`
> :   run\_on\_latest\_version for backfill operation (default: False)
>
>     Default: `False`
>
> `--to-date`
> :   to\_date for backfill operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### create-dry-run
>
> Perform create\_dry\_run operation
>
> ```
>
> airflowctl
> backfill
> create
> -
> dry
> -
> run
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> conf
> DAG_RUN_CONF
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> from
> -
> date
> FROM_DATE
> ]
> [
> --
> max
> -
> active
> -
> runs
> MAX_ACTIVE_RUNS
> ]
> [
> --
> reprocess
> -
> behavior
> REPROCESS_BEHAVIOR
> ]
> [
> --
> run
> -
> backwards
> |
> --
> no
> -
> run
> -
> backwards
> ]
> [
> --
> run
> -
> on
> -
> latest
> -
> version
> |
> --
> no
> -
> run
> -
> on
> -
> latest
> -
> version
> ]
> [
> --
> to
> -
> date
> TO_DATE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for backfill operation
>
> `--dag-run-conf`
> :   dag\_run\_conf for backfill operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--from-date`
> :   from\_date for backfill operation
>
> `--max-active-runs`
> :   max\_active\_runs for backfill operation
>
> `--reprocess-behavior`
> :   reprocess\_behavior for backfill operation
>
> `--run-backwards, --no-run-backwards`
> :   run\_backwards for backfill operation (default: False)
>
>     Default: `False`
>
> `--run-on-latest-version, --no-run-on-latest-version`
> :   run\_on\_latest\_version for backfill operation (default: False)
>
>     Default: `False`
>
> `--to-date`
> :   to\_date for backfill operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> backfill
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> backfill
> -
> id
> BACKFILL_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--backfill-id`
> :   backfill\_id for get operation in BackfillOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> backfill
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for list operation in BackfillOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### pause
>
> Perform pause operation
>
> ```
>
> airflowctl
> backfill
> pause
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> backfill
> -
> id
> BACKFILL_ID
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--backfill-id`
> :   backfill\_id for pause operation in BackfillOperations
>
> ###### unpause
>
> Perform unpause operation
>
> ```
>
> airflowctl
> backfill
> unpause
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> backfill
> -
> id
> BACKFILL_ID
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--backfill-id`
> :   backfill\_id for unpause operation in BackfillOperations
>
> #### [config](#cli-and-env-variables-ref--id6)
>
> Perform Config operations
>
> ```
>
> airflowctl
> config
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: get, lint, list
>
> ##### Sub-commands
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> config
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> option
> OPTION
> ]
> [
> --
> section
> SECTION
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--option`
> :   option for get operation in ConfigOperations
>
> `--section`
> :   section for get operation in ConfigOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### lint
>
> Lint options for the configuration changes while migrating from Airflow 2 to Airflow 3
>
> ```
>
> airflowctl
> config
> lint
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> ignore
> -
> option
> IGNORE_OPTION
> ]
> [
> --
> ignore
> -
> section
> IGNORE_SECTION
> ]
> [
> --
> option
> OPTION
> ]
> [
> --
> section
> SECTION
> ]
> [
> -
> v
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--ignore-option`
> :   The configuration option being ignored
>
> `--ignore-section`
> :   The configuration section being ignored
>
> `--option`
> :   The option of the configuration
>
> `--section`
> :   The section of the configuration
>
> `-v, --verbose`
> :   Enables detailed output, including the list of ignored sections and options
>
>     Default: `False`
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> config
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [connections](#cli-and-env-variables-ref--id7)
>
> Perform Connections operations
>
> ```
>
> airflowctl
> connections
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: create, create-defaults, delete, get, import, list, test, update
>
> ##### Sub-commands
>
> ###### create
>
> Perform create operation
>
> ```
>
> airflowctl
> connections
> create
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> conn
> -
> type
> CONN_TYPE
> ]
> [
> --
> connection
> -
> id
> CONNECTION_ID
> ]
> [
> --
> description
> DESCRIPTION
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> extra
> EXTRA
> ]
> [
> --
> host
> HOST
> ]
> [
> --
> login
> LOGIN
> ]
> [
> --
> password
> PASSWORD
> ]
> [
> --
> port
> PORT
> ]
> [
> --
> team
> -
> name
> TEAM_NAME
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--conn-type`
> :   conn\_type for connection operation
>
> `--connection-id`
> :   connection\_id for connection operation
>
> `--description`
> :   description for connection operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--extra`
> :   extra for connection operation
>
> `--host`
> :   host for connection operation
>
> `--login`
> :   login for connection operation
>
> `--password`
> :   password for connection operation
>
> `--port`
> :   port for connection operation
>
> `--team-name`
> :   team\_name for connection operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### create-defaults
>
> Perform create\_defaults operation
>
> ```
>
> airflowctl
> connections
> create
> -
> defaults
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### delete
>
> Perform delete operation
>
> ```
>
> airflowctl
> connections
> delete
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> conn
> -
> id
> CONN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--conn-id`
> :   conn\_id for delete operation in ConnectionsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> connections
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> conn
> -
> id
> CONN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--conn-id`
> :   conn\_id for get operation in ConnectionsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### import
>
> Import connections from a file exported with local CLI.
>
> ```
>
> airflowctl
> connections
> import
>
> [
> -
> h
> ]
> [
> -
> a
> {
> overwrite
> ,
> fail
> ,
> skip
> }]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> FILEPATH
> ```
>
> ###### Positional Arguments
>
> `FILEPATH`
> :   Connections JSON file
>
> ###### Named Arguments
>
> `-a, --action-on-existing-key`
> :   Possible choices: overwrite, fail, skip
>
>     Action to take if the entity already exists.
>
>     Default: `'overwrite'`
>
> `--api-token`
> :   The token to use for authentication
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> connections
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### test
>
> Perform test operation
>
> ```
>
> airflowctl
> connections
> test
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> conn
> -
> type
> CONN_TYPE
> ]
> [
> --
> connection
> -
> id
> CONNECTION_ID
> ]
> [
> --
> description
> DESCRIPTION
> ]
> [
> --
> extra
> EXTRA
> ]
> [
> --
> host
> HOST
> ]
> [
> --
> login
> LOGIN
> ]
> [
> --
> password
> PASSWORD
> ]
> [
> --
> port
> PORT
> ]
> [
> --
> team
> -
> name
> TEAM_NAME
> ]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--conn-type`
> :   conn\_type for connection operation
>
> `--connection-id`
> :   connection\_id for connection operation
>
> `--description`
> :   description for connection operation
>
> `--extra`
> :   extra for connection operation
>
> `--host`
> :   host for connection operation
>
> `--login`
> :   login for connection operation
>
> `--password`
> :   password for connection operation
>
> `--port`
> :   port for connection operation
>
> `--team-name`
> :   team\_name for connection operation
>
> ###### update
>
> Perform update operation
>
> ```
>
> airflowctl
> connections
> update
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> conn
> -
> type
> CONN_TYPE
> ]
> [
> --
> connection
> -
> id
> CONNECTION_ID
> ]
> [
> --
> description
> DESCRIPTION
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> extra
> EXTRA
> ]
> [
> --
> host
> HOST
> ]
> [
> --
> login
> LOGIN
> ]
> [
> --
> password
> PASSWORD
> ]
> [
> --
> port
> PORT
> ]
> [
> --
> team
> -
> name
> TEAM_NAME
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--conn-type`
> :   conn\_type for connection operation
>
> `--connection-id`
> :   connection\_id for connection operation
>
> `--description`
> :   description for connection operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--extra`
> :   extra for connection operation
>
> `--host`
> :   host for connection operation
>
> `--login`
> :   login for connection operation
>
> `--password`
> :   password for connection operation
>
> `--port`
> :   port for connection operation
>
> `--team-name`
> :   team\_name for connection operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [dagrun](#cli-and-env-variables-ref--id8)
>
> Perform DagRun operations
>
> ```
>
> airflowctl
> dagrun
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: get, list
>
> ##### Sub-commands
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> dagrun
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> id
> DAG_RUN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for get operation in DagRunOperations
>
> `--dag-run-id`
> :   dag\_run\_id for get operation in DagRunOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> dagrun
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> end
> -
> date
> END_DATE
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> limit
> LIMIT
> ]
> [
> --
> start
> -
> date
> START_DATE
> ]
> [
> --
> state
> STATE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for list operation in DagRunOperations
>
> `--end-date`
> :   end\_date for list operation in DagRunOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--limit`
> :   limit for list operation in DagRunOperations
>
> `--start-date`
> :   start\_date for list operation in DagRunOperations
>
> `--state`
> :   state for list operation in DagRunOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [dags](#cli-and-env-variables-ref--id9)
>
> Perform Dags operations
>
> ```
>
> airflowctl
> dags
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: delete, get, get-details, get-import-error, get-stats, get-tags, get-version, list, list-import-errors, list-version, list-warning, pause, trigger, unpause, update
>
> ##### Sub-commands
>
> ###### delete
>
> Perform delete operation
>
> ```
>
> airflowctl
> dags
> delete
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for delete operation in DagsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> dags
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for get operation in DagsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-details
>
> Perform get\_details operation
>
> ```
>
> airflowctl
> dags
> get
> -
> details
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for get\_details operation in DagsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-import-error
>
> Perform get\_import\_error operation
>
> ```
>
> airflowctl
> dags
> get
> -
> import
> -
> error
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> import
> -
> error
> -
> id
> IMPORT_ERROR_ID
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--import-error-id`
> :   import\_error\_id for get\_import\_error operation in DagsOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-stats
>
> Perform get\_stats operation
>
> ```
>
> airflowctl
> dags
> get
> -
> stats
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> ids
> DAG_IDS
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-ids`
> :   dag\_ids for get\_stats operation in DagsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-tags
>
> Perform get\_tags operation
>
> ```
>
> airflowctl
> dags
> get
> -
> tags
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get-version
>
> Perform get\_version operation
>
> ```
>
> airflowctl
> dags
> get
> -
> version
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> version
> -
> number
> VERSION_NUMBER
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for get\_version operation in DagsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--version-number`
> :   version\_number for get\_version operation in DagsOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> dags
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list-import-errors
>
> Perform list\_import\_errors operation
>
> ```
>
> airflowctl
> dags
> list
> -
> import
> -
> errors
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list-version
>
> Perform list\_version operation
>
> ```
>
> airflowctl
> dags
> list
> -
> version
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for list\_version operation in DagsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list-warning
>
> Perform list\_warning operation
>
> ```
>
> airflowctl
> dags
> list
> -
> warning
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### pause
>
> Pause a Dag
>
> ```
>
> airflowctl
> dags
> pause
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> dag_id
> ```
>
> ###### Positional Arguments
>
> `dag_id`
> :   The DAG ID of the DAG to pause or unpause
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### trigger
>
> Perform trigger operation
>
> ```
>
> airflowctl
> dags
> trigger
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> conf
> CONF
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> id
> DAG_RUN_ID
> ]
> [
> --
> data
> -
> interval
> -
> end
> DATA_INTERVAL_END
> ]
> [
> --
> data
> -
> interval
> -
> start
> DATA_INTERVAL_START
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> logical
> -
> date
> LOGICAL_DATE
> ]
> [
> --
> note
> NOTE
> ]
> [
> --
> partition
> -
> key
> PARTITION_KEY
> ]
> [
> --
> run
> -
> after
> RUN_AFTER
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--conf`
> :   conf for trigger\_dag\_run operation
>
> `--dag-id`
> :   dag\_id for trigger operation in DagsOperations
>
> `--dag-run-id`
> :   dag\_run\_id for trigger\_dag\_run operation
>
> `--data-interval-end`
> :   data\_interval\_end for trigger\_dag\_run operation
>
> `--data-interval-start`
> :   data\_interval\_start for trigger\_dag\_run operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--logical-date`
> :   logical\_date for trigger\_dag\_run operation
>
> `--note`
> :   note for trigger\_dag\_run operation
>
> `--partition-key`
> :   partition\_key for trigger\_dag\_run operation
>
> `--run-after`
> :   run\_after for trigger\_dag\_run operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### unpause
>
> Unpause a Dag
>
> ```
>
> airflowctl
> dags
> unpause
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> dag_id
> ```
>
> ###### Positional Arguments
>
> `dag_id`
> :   The DAG ID of the DAG to pause or unpause
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### update
>
> Perform update operation
>
> ```
>
> airflowctl
> dags
> update
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> is
> -
> paused
> |
> --
> no
> -
> is
> -
> paused
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for update operation in DagsOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--is-paused, --no-is-paused`
> :   is\_paused for dag\_body operation (default: False)
>
>     Default: `False`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [jobs](#cli-and-env-variables-ref--id10)
>
> Perform Jobs operations
>
> ```
>
> airflowctl
> jobs
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: list
>
> ##### Sub-commands
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> jobs
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> hostname
> HOSTNAME
> ]
> [
> --
> is
> -
> alive
> |
> --
> no
> -
> is
> -
> alive
> ]
> [
> --
> job
> -
> type
> JOB_TYPE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--hostname`
> :   hostname for list operation in JobsOperations
>
> `--is-alive, --no-is-alive`
> :   is\_alive for list operation in JobsOperations (default: False)
>
>     Default: `False`
>
> `--job-type`
> :   job\_type for list operation in JobsOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [pools](#cli-and-env-variables-ref--id11)
>
> Perform Pools operations
>
> ```
>
> airflowctl
> pools
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: create, delete, export, get, import, list, update
>
> ##### Sub-commands
>
> ###### create
>
> Perform create operation
>
> ```
>
> airflowctl
> pools
> create
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> description
> DESCRIPTION
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> include
> -
> deferred
> |
> --
> no
> -
> include
> -
> deferred
> ]
> [
> --
> name
> NAME
> ]
> [
> --
> slots
> SLOTS
> ]
> [
> --
> team
> -
> name
> TEAM_NAME
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--description`
> :   description for pool operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--include-deferred, --no-include-deferred`
> :   include\_deferred for pool operation (default: False)
>
>     Default: `False`
>
> `--name`
> :   name for pool operation
>
> `--slots`
> :   slots for pool operation
>
> `--team-name`
> :   team\_name for pool operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### delete
>
> Perform delete operation
>
> ```
>
> airflowctl
> pools
> delete
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> pool
> POOL
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--pool`
> :   pool for delete operation in PoolsOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### export
>
> Export all pools
>
> ```
>
> airflowctl
> pools
> export
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> FILEPATH
> ```
>
> ###### Positional Arguments
>
> `FILEPATH`
> :   File path to read from for import commands.
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> pools
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> pool
> -
> name
> POOL_NAME
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--pool-name`
> :   pool\_name for get operation in PoolsOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### import
>
> Import pools
>
> ```
>
> airflowctl
> pools
> import
>
> [
> -
> h
> ]
> [
> -
> a
> {
> overwrite
> ,
> fail
> ,
> skip
> }]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> FILEPATH
> ```
>
> ###### Positional Arguments
>
> `FILEPATH`
> :   File path to read from for import commands.
>
> ###### Named Arguments
>
> `-a, --action-on-existing-key`
> :   Possible choices: overwrite, fail, skip
>
>     Action to take if the entity already exists.
>
>     Default: `'overwrite'`
>
> `--api-token`
> :   The token to use for authentication
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> pools
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### update
>
> Perform update operation
>
> ```
>
> airflowctl
> pools
> update
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> description
> DESCRIPTION
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> include
> -
> deferred
> |
> --
> no
> -
> include
> -
> deferred
> ]
> [
> --
> pool
> POOL
> ]
> [
> --
> slots
> SLOTS
> ]
> [
> --
> team
> -
> name
> TEAM_NAME
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--description`
> :   description for pool\_body operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--include-deferred, --no-include-deferred`
> :   include\_deferred for pool\_body operation (default: False)
>
>     Default: `False`
>
> `--pool`
> :   pool for pool\_body operation
>
> `--slots`
> :   slots for pool\_body operation
>
> `--team-name`
> :   team\_name for pool\_body operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [providers](#cli-and-env-variables-ref--id12)
>
> Perform Providers operations
>
> ```
>
> airflowctl
> providers
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: list
>
> ##### Sub-commands
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> providers
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [variables](#cli-and-env-variables-ref--id13)
>
> Perform Variables operations
>
> ```
>
> airflowctl
> variables
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: create, delete, get, import, list, update
>
> ##### Sub-commands
>
> ###### create
>
> Perform create operation
>
> ```
>
> airflowctl
> variables
> create
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> description
> DESCRIPTION
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> key
> KEY
> ]
> [
> --
> team
> -
> name
> TEAM_NAME
> ]
> [
> --
> value
> VALUE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--description`
> :   description for variable operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--key`
> :   key for variable operation
>
> `--team-name`
> :   team\_name for variable operation
>
> `--value`
> :   value for variable operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### delete
>
> Perform delete operation
>
> ```
>
> airflowctl
> variables
> delete
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> variable
> -
> key
> VARIABLE_KEY
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--variable-key`
> :   variable\_key for delete operation in VariablesOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> variables
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> variable
> -
> key
> VARIABLE_KEY
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--variable-key`
> :   variable\_key for get operation in VariablesOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### import
>
> Import variables from a file exported with local CLI.
>
> ```
>
> airflowctl
> variables
> import
>
> [
> -
> h
> ]
> [
> -
> a
> {
> overwrite
> ,
> fail
> ,
> skip
> }]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> FILEPATH
> ```
>
> ###### Positional Arguments
>
> `FILEPATH`
> :   File path to read from for import commands.
>
> ###### Named Arguments
>
> `-a, --action-on-existing-key`
> :   Possible choices: overwrite, fail, skip
>
>     Action to take if the entity already exists.
>
>     Default: `'overwrite'`
>
> `--api-token`
> :   The token to use for authentication
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> variables
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### update
>
> Perform update operation
>
> ```
>
> airflowctl
> variables
> update
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> description
> DESCRIPTION
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> key
> KEY
> ]
> [
> --
> team
> -
> name
> TEAM_NAME
> ]
> [
> --
> value
> VALUE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--description`
> :   description for variable operation
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--key`
> :   key for variable operation
>
> `--team-name`
> :   team\_name for variable operation
>
> `--value`
> :   value for variable operation
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> #### [version](#cli-and-env-variables-ref--id14)
>
> Show version information
>
> ```
>
> airflowctl
> version
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> remote
> ]
> ```
>
> ##### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--remote`
> :   Fetch the Airflow version in remote server, otherwise only shows the local airflowctl version
>
>     Default: `False`
>
> #### [xcom](#cli-and-env-variables-ref--id15)
>
> Perform XCom operations
>
> ```
>
> airflowctl
> xcom
> [
> -
> h
> ]
> COMMAND
> ...
> ```
>
> ##### Positional Arguments
>
> `COMMAND`
> :   Possible choices: add, delete, edit, get, list
>
> ##### Sub-commands
>
> ###### add
>
> Perform add operation
>
> ```
>
> airflowctl
> xcom
> add
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> id
> DAG_RUN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> key
> KEY
> ]
> [
> --
> map
> -
> index
> MAP_INDEX
> ]
> [
> --
> task
> -
> id
> TASK_ID
> ]
> [
> --
> value
> VALUE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for add operation in XComOperations
>
> `--dag-run-id`
> :   dag\_run\_id for add operation in XComOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--key`
> :   key for add operation in XComOperations
>
> `--map-index`
> :   map\_index for add operation in XComOperations
>
> `--task-id`
> :   task\_id for add operation in XComOperations
>
> `--value`
> :   value for add operation in XComOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### delete
>
> Perform delete operation
>
> ```
>
> airflowctl
> xcom
> delete
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> id
> DAG_RUN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> key
> KEY
> ]
> [
> --
> map
> -
> index
> MAP_INDEX
> ]
> [
> --
> task
> -
> id
> TASK_ID
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for delete operation in XComOperations
>
> `--dag-run-id`
> :   dag\_run\_id for delete operation in XComOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--key`
> :   key for delete operation in XComOperations
>
> `--map-index`
> :   map\_index for delete operation in XComOperations
>
> `--task-id`
> :   task\_id for delete operation in XComOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### edit
>
> Perform edit operation
>
> ```
>
> airflowctl
> xcom
> edit
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> id
> DAG_RUN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> key
> KEY
> ]
> [
> --
> map
> -
> index
> MAP_INDEX
> ]
> [
> --
> task
> -
> id
> TASK_ID
> ]
> [
> --
> value
> VALUE
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for edit operation in XComOperations
>
> `--dag-run-id`
> :   dag\_run\_id for edit operation in XComOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--key`
> :   key for edit operation in XComOperations
>
> `--map-index`
> :   map\_index for edit operation in XComOperations
>
> `--task-id`
> :   task\_id for edit operation in XComOperations
>
> `--value`
> :   value for edit operation in XComOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### get
>
> Perform get operation
>
> ```
>
> airflowctl
> xcom
> get
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> id
> DAG_RUN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> key
> KEY
> ]
> [
> --
> map
> -
> index
> MAP_INDEX
> ]
> [
> --
> task
> -
> id
> TASK_ID
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for get operation in XComOperations
>
> `--dag-run-id`
> :   dag\_run\_id for get operation in XComOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--key`
> :   key for get operation in XComOperations
>
> `--map-index`
> :   map\_index for get operation in XComOperations
>
> `--task-id`
> :   task\_id for get operation in XComOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ###### list
>
> Perform list operation
>
> ```
>
> airflowctl
> xcom
> list
> [
> -
> h
> ]
> [
> --
> api
> -
> token
> API_TOKEN
> ]
> [
> --
> dag
> -
> id
> DAG_ID
> ]
> [
> --
> dag
> -
> run
> -
> id
> DAG_RUN_ID
> ]
> [
> -
> e
> ENV
> ]
> [
> --
> key
> KEY
> ]
> [
> --
> map
> -
> index
> MAP_INDEX
> ]
> [
> --
> task
> -
> id
> TASK_ID
> ]
> [
> --
> output
> (
> table
> ,
> json
> ,
> yaml
> ,
> plain
> )]
> ```
>
> ###### Named Arguments
>
> `--api-token`
> :   The token to use for authentication
>
> `--dag-id`
> :   dag\_id for list operation in XComOperations
>
> `--dag-run-id`
> :   dag\_run\_id for list operation in XComOperations
>
> `-e, --env`
> :   The environment to run the command in
>
>     Default: `'production'`
>
> `--key`
> :   key for list operation in XComOperations
>
> `--map-index`
> :   map\_index for list operation in XComOperations
>
> `--task-id`
> :   task\_id for list operation in XComOperations
>
> `--output, -o`
> :   Possible choices: table, json, yaml, plain
>
>     Output format. Allowed values: json, yaml, plain, table (default: json)
>
>     Default: `'json'`
>
> ## Environment Variables
>
> AIRFLOW\_CLI\_TOKEN
> :   The token used to authenticate with the Airflow API. This is only
>     required if you are using the Airflow API and have not set up
>     authentication using a different method. If username and password hasn’t been used.
>
> AIRFLOW\_CLI\_ENVIRONMENT
> :   Environment name to use for the CLI. This is used to determine
>     which environment to use when running the CLI. This is only
>     required if you have multiple environments set up and want to
>     specify which one to use. If not set, the default environment
>     will be used which is production.
>
> AIRFLOW\_CLI\_DEBUG\_MODE
> :   This variable can be used to enable debug mode for the CLI.
>     It disables some features such as keyring integration and save credentials to file.
>     It is only meant to use if either you are developing airflowctl or running API integration tests.
>     Please do not use this variable unless you know what you are doing.
>
> AIRFLOW\_CLI\_API\_RETRIES
> :   The number of times to retry an API call if it fails. This is
>     only used if you are using the Airflow API and have not set up
>     authentication using a different method. The default value is 3.
>
> AIRFLOW\_CLI\_API\_RETRY\_WAIT\_MIN
> :   The minimum amount of time to wait between API retries in seconds.
>     This is only used if you are using the Airflow API and have not set up
>     authentication using a different method. The default value is 1 second.
>
> AIRFLOW\_CLI\_API\_RETRY\_WAIT\_MAX
> :   The maximum amount of time to wait between API retries in seconds.
>     This is only used if you are using the Airflow API and have not set up
>     authentication using a different method. The default value is 10 seconds.
>
> [Previous](#start "Quick Start")Next

---

<a id="index"></a>

<!-- source_url: https://airflow.apache.org/docs/apache-airflow-ctl/stable/index.html -->

<!-- page_index: 9 -->

# What is airflowctl? ¶

<svg fill="currentColor" height="16" viewbox="0 0 16 16" width="16">
<path></path>
</svg>

`↑↓` Navigate
`⏎` Select
`Esc` Close

# What is airflowctl?

airflowctl is a command line tool that helps you communicate with API and provide similar functionality with Apache Airflow CLI.
It is designed to be easy to use and provides a simple interface for managing your Airflow API calls and daily operations.

Please head over to [Quick Start](#start) to get started.

Previous
[Next](#installation "Installation of airflowctl")

---
