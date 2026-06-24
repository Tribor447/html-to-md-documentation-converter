# Spring Cloud Config

## Navigation

- Introduction
  
- [Introduction](#index)
  
- [Spring Cloud Config Server](#server)
    
- [Environment Repository](#server-environment-repository)
      
- [Git Backend](#server-environment-repository-git-backend)
      
- [Version Control Backend Filesystem Use](#server-environment-repository-version-control-backend-filesystem-use)
      
- [File System Backend](#server-environment-repository-file-system-backend)
      
- [Vault Backend](#server-environment-repository-vault-backend)
      
- [Accessing Backends Through a Proxy](#server-environment-repository-accessing-backends-through-a-proxy)
      
- [Sharing Configuration With All Applications](#server-environment-repository-sharing-configuration-with-all-applications)
      
- [AWS Secrets Manager](#server-environment-repository-aws-secrets-manager)
      
- [AWS Parameter Store](#server-environment-repository-aws-parameter-store)
      
- [JDBC Backend](#server-environment-repository-jdbc-backend)
      
- [Redis Backend](#server-environment-repository-redis-backend)
      
- [AWS S3 Backend](#server-environment-repository-aws-s3-backend)
      
- [AWS Parameter Store Backend](#server-environment-repository-aws-parameter-store-backend)
      
- [AWS Secrets Manager Backend](#server-environment-repository-aws-secrets-manager-backend)
      
- [Google Secret Manager Backend](#server-environment-repository-gcp-secret-manager-backend)
      
- [CredHub Backend](#server-environment-repository-credhub-backend)
      
- [MongoDB Backend](#server-environment-repository-mongo-backend)
      
- [Composite Environment Repositories](#server-environment-repository-composite-repositories)
      
- [Custom Environment Repositories](#server-environment-repository-custom-enviroment-repository)
      
- [Property Overrides](#server-environment-repository-property-overrides)
      
- [Using Bootstrap To Override Properties](#server-environment-repository-using-bootstrap-to-override-properties)
      
- [Overriding Properties Using Placeholders](#server-environment-repository-overriding-properties-using-placeholders)
      
- [Overriding Properties Using Profiles](#server-environment-repository-overriding-properties-using-profiles)
    
- [Health Indicator](#server-health-indicator)
    
- [Security](#server-security)
    
- [Actuator and Security](#server-actuator-and-security)
    
- [Encryption and Decryption](#server-encryption-and-decryption)
    
- [Key Management](#server-key-management)
    
- [Creating a Key Store for Testing](#server-creating-a-key-store-for-testing)
    
- [Using Multiple Keys and Key Rotation](#server-using-multiple-keys-and-key-rotation)
    
- [Serving Encrypted Properties](#server-serving-encrypted-properties)
    
- [Serving Alternative Formats](#server-serving-alternative-formats)
    
- [Serving Plain Text](#server-serving-plain-text)
    
- [Serving Binary Files](#server-serving-binary-files)
    
- [Embedding the Config Server](#server-embedding)
    
- [Push Notifications and Spring Cloud Bus](#server-push-notifications-and-bus)
    
- [AOT and Native Image Support](#server-aot-and-native-image-support)
  
- [Spring Cloud Config Client](#client)

## Content

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/index.html -->

<!-- page_index: 1 -->

# Spring Cloud Config

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="index--page-title"></a>
<a id="index--spring-cloud-config"></a>

# Spring Cloud Config

Spring Cloud Config provides server-side and client-side support for externalized configuration in a distributed system. With the Config Server, you have a central place to manage external properties for applications across all environments.
The concepts on both client and server map identically to the Spring `Environment` and `PropertySource` abstractions, so they fit very well with Spring applications but can be used with any application running in any language.
As an application moves through the deployment pipeline from dev to test and into production, you can manage the configuration between those environments and be certain that applications have everything they need to run when they migrate.
The default implementation of the server storage backend uses git, so it easily supports labelled versions of configuration environments as well as being accessible to a wide range of tooling for managing the content.
It is easy to add alternative implementations and plug them in with Spring configuration.

**5.0.3**

[Spring Cloud Config Server](#server)

---

<a id="server"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server.html -->

<!-- page_index: 2 -->

# Spring Cloud Config Server

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server--page-title"></a>
<a id="server--spring-cloud-config-server"></a>

# Spring Cloud Config Server

Spring Cloud Config Server provides an HTTP resource-based API for external configuration (name-value pairs or equivalent YAML content).
The server is embeddable in a Spring Boot application, by using the `@EnableConfigServer` annotation.
Consequently, the following application is a config server:

ConfigServer.java

```java
@SpringBootApplication
@EnableConfigServer
public class ConfigServer {
  public static void main(String[] args) {
    SpringApplication.run(ConfigServer.class, args);
  }
}
```

Like all Spring Boot applications, it runs on port 8080 by default, but you can switch it to the more conventional port 8888 in various ways.
The easiest, which also sets a default configuration repository, is by launching it with `spring.config.name=configserver` (there is a `configserver.yml` in the Config Server jar).
Another is to use your own `application.properties`, as shown in the following example:

application.properties

```properties
server.port: 8888
spring.cloud.config.server.git.uri: file://${user.home}/config-repo
```

where `${user.home}/config-repo` is a git repository containing YAML and properties files.

> [!NOTE]
> On Windows, you need an extra "/" in the file URL if it is absolute with a drive prefix (for example,`/${user.home}/config-repo`).

> [!TIP]
> The following listing shows a recipe for creating the git repository in the preceding example:
>
> ```
> $ cd $HOME
> $ mkdir config-repo
> $ cd config-repo
> $ git init .
> $ echo info.foo: bar > application.properties
> $ git add -A .
> $ git commit -m "Add application.properties"
> ```

> [!WARNING]
> Using the local filesystem for your git repository is intended for testing only.
> You should use a server to host your configuration repositories in production.

> [!WARNING]
> The initial clone of your configuration repository can be quick and efficient if you keep only text files in it.
> If you store binary files, especially large ones, you may experience delays on the first request for configuration or encounter out of memory errors in the server.

[Introduction](#index)
[Environment Repository](#server-environment-repository)

---

<a id="server-environment-repository"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository.html -->

<!-- page_index: 3 -->

# Environment Repository

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository--page-title"></a>
<a id="server-environment-repository--environment-repository"></a>

# Environment Repository

Where should you store the configuration data for the Config Server?
The strategy that governs this behaviour is the `EnvironmentRepository`, serving `Environment` objects.
This `Environment` is a shallow copy of the domain from the Spring `Environment` (including `propertySources` as the main feature).
The `Environment` resources are parametrized by three variables:

- `{application}`, which maps to `spring.application.name` on the client side.
- `{profile}`, which maps to `spring.profiles.active` on the client (comma-separated list).
- `{label}`, which is a server side feature labelling a "versioned" set of config files.

Repository implementations generally behave like a Spring Boot application, loading configuration files from a `spring.config.name` equal to the `{application}` parameter, and `spring.profiles.active` equal to the `{profiles}` parameter.
Precedence rules for profiles are also the same as in a regular Spring Boot application: Active profiles take precedence over defaults, and, if there are multiple profiles, the last one wins (similar to adding entries to a `Map`).

The following sample client application has this bootstrap configuration:

```yaml
spring:
  application:
    name: foo
  profiles:
    active: dev,mysql
```

(As usual with a Spring Boot application, these properties could also be set by environment variables or command line arguments).

If the repository is file-based, the server creates an
`Environment` from `application.yml` (shared between all clients) and
`foo.yml` (with `foo.yml` taking precedence).
If the YAML files have documents inside them that point to Spring profiles, those are applied with higher precedence (in order of the profiles listed).
If there are profile-specific YAML (or properties) files, these are also applied with higher precedence than the defaults.
Higher precedence translates to a `PropertySource` listed earlier in the `Environment`.
(These same rules apply in a standalone Spring Boot application.)

You can set `spring.cloud.config.server.accept-empty` to `false` so that Server would return a HTTP 404 status, if the application is not found. By default, this flag is set to `true`.

> [!NOTE]
> You cannot place `spring.main.*` properties in a remote `EnvironmentRepository`. These properties are used as part of the application initialization.

[Spring Cloud Config Server](#server)
[Git Backend](#server-environment-repository-git-backend)

---

<a id="server-environment-repository-git-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/git-backend.html -->

<!-- page_index: 4 -->

# Git Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-git-backend--page-title"></a>
<a id="server-environment-repository-git-backend--git-backend"></a>

# Git Backend

The default implementation of `EnvironmentRepository` uses a Git backend, which is very convenient for managing upgrades and physical environments and for auditing changes.
To change the location of the repository, you can set the `spring.cloud.config.server.git.uri` configuration property in the Config Server (for example in `application.yml`).
If you set it with a `file:` prefix, it should work from a local repository so that you can get started quickly and easily without a server. However, in that case, the server operates directly on the local repository without cloning it (it does not matter if it is not bare because the Config Server never makes changes to the "remote" repository).
To scale the Config Server up and make it highly available, you need to have all instances of the server pointing to the same repository, so only a shared file system would work.
Even in that case, it is better to use the `ssh:` protocol for a shared filesystem repository, so that the server can clone it and use a local working copy as a cache.

This repository implementation maps the `{label}` parameter of the HTTP resource to a git label (commit id, branch name, or tag).
If the git branch or tag name contains a slash (`/`), then the label in the HTTP URL should instead be specified with the special string `({special-string})` (to avoid ambiguity with other URL paths).
For example, if the label is `foo/bar`, replacing the slash would result in the following label: `foo({special-string})bar`.
The inclusion of the special string `({special-string})` can also be applied to the `{application}` parameter.
If you use a command-line client such as curl, be careful with the brackets in the URL — you should escape them from the shell with single quotes ('').

<a id="server-environment-repository-git-backend--git-backend-local-path-hardening"></a>
<a id="server-environment-repository-git-backend--local-path-hardening"></a>

## Local Path Hardening

When the Git backend touches the local file system, it applies extra checks to
reduce time-of-check/time-of-use (TOCTOU) issues and unwanted symbolic-link
behavior. These mitigations complement normal host hardening (permissions, separate service accounts, and non-world-writable parent directories); they do
not replace it.

**`file:` repositories (`spring.cloud.config.server.git.uri`)**
:   Before JGit opens a `file:` repository, the server resolves the configured path and
    rejects a symbolic link used as the repository root or as the `.git` entry.
    Paths are canonicalized with `Path#toRealPath` using `LinkOption.NOFOLLOW_LINKS`
    so intermediate symlink segments are not followed silently. After the
    repository is opened, the work tree and git directory that JGit reports are
    checked to stay under the same resolved root. Configure a concrete directory
    path for `file:` URIs (not a path whose final name is a symlink to a repository
    elsewhere).

**Remote clones and `spring.cloud.config.server.git.basedir`**
:   When the server clones into `basedir`, it prepares an empty leaf directory
    (including removing a prior symlink at that path when present), creates the leaf
    with an exclusive directory create when the OS allows it, clears old content
    without following directory symlinks during recursive delete, and re-resolves
    `basedir` immediately before invoking JGit’s clone so a concurrent replacement of
    the path is more likely to be detected.

<a id="server-environment-repository-git-backend--skipping-ssl-certificate-validation"></a>

## Skipping SSL Certificate Validation

The configuration server’s validation of the Git server’s SSL certificate can be disabled by setting the `git.skipSslValidation` property to `true` (default is `false`).

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://example.com/my/repo
          skipSslValidation: true
```

<a id="server-environment-repository-git-backend--setting-connection-timeout"></a>

## Setting Connection Timeout

You can configure the time, in seconds, that the configuration server will wait to acquire an HTTP or SSH connection. Use the `git.timeout` property (default is `5`).

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://example.com/my/repo
          timeout: 4
```

<a id="server-environment-repository-git-backend--placeholders-in-git-uri"></a>

## Placeholders in Git URI

Spring Cloud Config Server supports a git repository URL with placeholders for the `{application}` and `{profile}` (and `{label}` if you need it, but remember that the label is applied as a git label anyway).
So you can support a “one repository per application” policy by using a structure similar to the following:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/myorg/\{application}
```

You can also support a “one repository per profile” policy by using a similar pattern but with
`{profile}`.

Additionally, using the special string `({special-string})` within your `{application}` parameters can enable support for multiple
organizations, as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/\{application}
```

where `{application}` is provided at request time in the following format: `organization({special-string})application`.

<a id="server-environment-repository-git-backend--pattern-matching-and-multiple-repositories"></a>

## Pattern Matching and Multiple Repositories

Spring Cloud Config also includes support for more complex requirements with pattern
matching on the application and profile name.
The pattern format is a comma-separated list of `{application}/{profile}` names with wildcards (note that a pattern beginning with a wildcard may need to be quoted), as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          repos:
            simple: https://github.com/simple/config-repo
            special:
              pattern: special*/dev*,*special*/dev*
              uri: https://github.com/special/config-repo
            local:
              pattern: local*
              uri: file:/home/configsvc/config-repo
```

If `{application}/{profile}` does not match any of the patterns, it uses the default URI defined under `spring.cloud.config.server.git.uri`.
In the above example, for the “simple” repository, the pattern is `simple/*` (it only matches one application named `simple` in all profiles). The “local” repository matches all application names beginning with `local` in all profiles (the `/*` suffix is added automatically to any pattern that does not have a profile matcher).

> [!NOTE]
> The “one-liner” short cut used in the “simple” example can be used only if the only property to be set is the URI.
> If you need to set anything else (credentials, pattern, and so on) you need to use the full form.

The `pattern` property in the repo is actually an array, so you can use a YAML array (or `[0]`, `[1]`, etc. suffixes in properties files) to bind to multiple patterns.
You may need to do so if you are going to run apps with multiple profiles, as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          repos:
            development:
              pattern:
                - '*/development'
                - '*/staging'
              uri: https://github.com/development/config-repo
            staging:
              pattern:
                - '*/qa'
                - '*/production'
              uri: https://github.com/staging/config-repo
```

> [!NOTE]
> Spring Cloud guesses that a pattern containing a profile that does not end in `*` implies that you actually want to match a list of profiles starting with this pattern (so `*/staging` is a shortcut for `["*/staging", "*/staging,*"]`, and so on).
> This is common where, for instance, you need to run applications in the “development” profile locally but also the “cloud” profile remotely.

Every repository can also optionally store config files in sub-directories, and patterns to search for those directories can be specified as `search-paths`.
The following example shows a config file at the top level:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          search-paths:
            - foo
            - bar*
```

In the preceding example, the server searches for config files in the top level and in the `foo/` sub-directory and also any sub-directory whose name begins with `bar`.

By default, the server clones remote repositories when configuration
is first requested.
The server can be configured to clone the repositories at startup, as shown in the following top-level example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://git/common/config-repo.git
          repos:
            team-a:
                pattern: team-a-*
                cloneOnStart: true
                uri: https://git/team-a/config-repo.git
            team-b:
                pattern: team-b-*
                cloneOnStart: false
                uri: https://git/team-b/config-repo.git
            team-c:
                pattern: team-c-*
                uri: https://git/team-a/config-repo.git
```

In the preceding example, the server clones team-a’s config-repo on startup, before it
accepts any requests.
All other repositories are not cloned until configuration from the repository is requested.

> [!NOTE]
> Setting a repository to be cloned when the Config Server starts up can help to identify a misconfigured configuration source (such as an invalid repository URI) quickly, while the Config Server is starting up.
> With `cloneOnStart` not enabled for a configuration source, the Config Server may start successfully with a misconfigured or invalid configuration source and not detect an error until an application requests configuration from that configuration source.

<a id="server-environment-repository-git-backend--authentication"></a>

## Authentication

To use HTTP basic authentication on the remote repository, add the `username` and `password` properties separately (not in the URL), as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          username: trolley
          password: strongpassword
```

If you do not use HTTPS and user credentials, SSH should also work out of the box when you store keys in the default directories (`~/.ssh`) and the URI points to an SSH location, such as `[email protected]:configuration/cloud-configuration`.
It is important that an entry for the Git server be present in the `~/.ssh/known_hosts` file and that it is in `ssh-rsa` format.
Other formats (such as `ecdsa-sha2-nistp256`) are not supported.
To avoid surprises, you should ensure that only one entry is present in the `known_hosts` file for the Git server and that it matches the URL you provided to the config server.
If you use a hostname in the URL, you want to have exactly that (not the IP) in the `known_hosts` file.
The repository is accessed by using JGit, so any documentation you find on that should be applicable.
HTTPS proxy settings can be set in `~/.git/config` or (in the same way as for any other JVM process) with
system properties (`-Dhttps.proxyHost` and `-Dhttps.proxyPort`).

> [!TIP]
> If you do not know where your `~/.git` directory is, use `git config --global` to manipulate the settings (for example, `git config --global http.sslVerify false`).

JGit requires RSA keys in PEM format. Below is an example ssh-keygen (from openssh) command that will generate a key in the corect format:

```bash
ssh-keygen -m PEM -t rsa -b 4096 -f ~/config_server_deploy_key.rsa
```

> [!WARNING]
> When working with SSH keys, the expected ssh private-key must begin with `-----BEGIN RSA PRIVATE KEY-----`. If the key starts with `-----BEGIN OPENSSH PRIVATE KEY-----` then the RSA key will not load when spring-cloud-config server is started. The error looks like:
>
> ```none
> - Error in object 'spring.cloud.config.server.git': codes [PrivateKeyIsValid.spring.cloud.config.server.git,PrivateKeyIsValid]; arguments [org.springframework.context.support.DefaultMessageSourceResolvable: codes [spring.cloud.config.server.git.,]; arguments []; default message []]; default message [Property 'spring.cloud.config.server.git.privateKey' is not a valid private key]
> ```

To correct the above error the RSA key must be converted to PEM format. An example using openssh is provided above for generating a new key in the appropriate format.

<a id="server-environment-repository-git-backend--authentication-with-aws-codecommit"></a>

## Authentication with AWS CodeCommit

Spring Cloud Config Server also supports [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) authentication.
AWS CodeCommit uses an authentication helper when using Git from the command line.
This helper is not used with the JGit library, so a JGit CredentialProvider for AWS CodeCommit is created if the Git URI matches the AWS CodeCommit pattern.
AWS CodeCommit URIs follow this pattern:

```bash
https://git-codecommit.${AWS_REGION}.amazonaws.com/v1/repos/${repo}
```

If you provide a username and password with an AWS CodeCommit URI, they must be the [AWS accessKeyId and secretAccessKey](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSGettingStartedGuide/AWSCredentials.html) that provide access to the repository.
If you do not specify a username and password, the accessKeyId and secretAccessKey are retrieved by using the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/credentials.html).

If your Git URI matches the CodeCommit URI pattern (shown earlier), you must provide valid AWS credentials in the username and password or in one of the locations supported by the default credential provider chain.
AWS EC2 instances may use [IAM Roles for EC2 Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html).

> [!NOTE]
> The `software.amazon.awssdk:auth` jar is an optional dependency.
> If the `software.amazon.awssdk:auth` jar is not on your classpath, the AWS Code Commit credential provider is not created, regardless of the git server URI.

<a id="server-environment-repository-git-backend--authentication-with-google-cloud-source"></a>

## Authentication with Google Cloud Source

Spring Cloud Config Server also supports authenticating against [Google Cloud Source](https://cloud.google.com/source-repositories/) repositories.

If your Git URI uses the `http` or `https` protocol and the domain name is `source.developers.google.com`, the Google Cloud Source credentials provider will be used. A Google Cloud Source repository URI has the format `source.developers.google.com/p/${GCP_PROJECT}/r/${REPO}`. To obtain the URI for your repository, click on "Clone" in the Google Cloud Source UI, and select "Manually generated credentials". Do not generate any credentials, simply copy the displayed URI.

The Google Cloud Source credentials provider will use Google Cloud Platform application default credentials. See [Google Cloud SDK documentation](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login) on how to create application default credentials for a system. This approach will work for user accounts in dev environments and for service accounts in production environments.

> [!NOTE]
> `com.google.auth:google-auth-library-oauth2-http` is an optional dependency.
> If the `google-auth-library-oauth2-http` jar is not on your classpath, the Google Cloud Source credential provider is not created, regardless of the git server URI.

<a id="server-environment-repository-git-backend--git-ssh-configuration-using-properties"></a>

## Git SSH configuration using properties

By default, the JGit library used by Spring Cloud Config Server uses SSH configuration files such as `~/.ssh/known_hosts` and `/etc/ssh/ssh_config` when connecting to Git repositories by using an SSH URI.
In cloud environments such as Cloud Foundry, the local filesystem may be ephemeral or not easily accessible.
For those cases, SSH configuration can be set by using Java properties.
In order to activate property-based SSH configuration, the `spring.cloud.config.server.git.ignoreLocalSshSettings` property must be set to `true`, as shown in the following example:

```yaml
  spring:
    cloud:
      config:
        server:
          git:
            uri: [email protected]:team/repo1.git
            ignoreLocalSshSettings: true
            hostKey: someHostKey
            hostKeyAlgorithm: ssh-rsa
            privateKey: |
                         -----BEGIN RSA PRIVATE KEY-----
                         MIIEpgIBAAKCAQEAx4UbaDzY5xjW6hc9jwN0mX33XpTDVW9WqHp5AKaRbtAC3DqX
                         IXFMPgw3K45jxRb93f8tv9vL3rD9CUG1Gv4FM+o7ds7FRES5RTjv2RT/JVNJCoqF
                         ol8+ngLqRZCyBtQN7zYByWMRirPGoDUqdPYrj2yq+ObBBNhg5N+hOwKjjpzdj2Ud
                         1l7R+wxIqmJo1IYyy16xS8WsjyQuyC0lL456qkd5BDZ0Ag8j2X9H9D5220Ln7s9i
                         oezTipXipS7p7Jekf3Ywx6abJwOmB0rX79dV4qiNcGgzATnG1PkXxqt76VhcGa0W
                         DDVHEEYGbSQ6hIGSh0I7BQun0aLRZojfE3gqHQIDAQABAoIBAQCZmGrk8BK6tXCd
                         fY6yTiKxFzwb38IQP0ojIUWNrq0+9Xt+NsypviLHkXfXXCKKU4zUHeIGVRq5MN9b
                         BO56/RrcQHHOoJdUWuOV2qMqJvPUtC0CpGkD+valhfD75MxoXU7s3FK7yjxy3rsG
                         EmfA6tHV8/4a5umo5TqSd2YTm5B19AhRqiuUVI1wTB41DjULUGiMYrnYrhzQlVvj
                         5MjnKTlYu3V8PoYDfv1GmxPPh6vlpafXEeEYN8VB97e5x3DGHjZ5UrurAmTLTdO8
                         +AahyoKsIY612TkkQthJlt7FJAwnCGMgY6podzzvzICLFmmTXYiZ/28I4BX/mOSe
                         pZVnfRixAoGBAO6Uiwt40/PKs53mCEWngslSCsh9oGAaLTf/XdvMns5VmuyyAyKG
                         ti8Ol5wqBMi4GIUzjbgUvSUt+IowIrG3f5tN85wpjQ1UGVcpTnl5Qo9xaS1PFScQ
                         xrtWZ9eNj2TsIAMp/svJsyGG3OibxfnuAIpSXNQiJPwRlW3irzpGgVx/AoGBANYW
                         dnhshUcEHMJi3aXwR12OTDnaLoanVGLwLnkqLSYUZA7ZegpKq90UAuBdcEfgdpyi
                         PhKpeaeIiAaNnFo8m9aoTKr+7I6/uMTlwrVnfrsVTZv3orxjwQV20YIBCVRKD1uX
                         VhE0ozPZxwwKSPAFocpyWpGHGreGF1AIYBE9UBtjAoGBAI8bfPgJpyFyMiGBjO6z
                         FwlJc/xlFqDusrcHL7abW5qq0L4v3R+FrJw3ZYufzLTVcKfdj6GelwJJO+8wBm+R
                         gTKYJItEhT48duLIfTDyIpHGVm9+I1MGhh5zKuCqIhxIYr9jHloBB7kRm0rPvYY4
                         VAykcNgyDvtAVODP+4m6JvhjAoGBALbtTqErKN47V0+JJpapLnF0KxGrqeGIjIRV
                         cYA6V4WYGr7NeIfesecfOC356PyhgPfpcVyEztwlvwTKb3RzIT1TZN8fH4YBr6Ee
                         KTbTjefRFhVUjQqnucAvfGi29f+9oE3Ei9f7wA+H35ocF6JvTYUsHNMIO/3gZ38N
                         CPjyCMa9AoGBAMhsITNe3QcbsXAbdUR00dDsIFVROzyFJ2m40i4KCRM35bC/BIBs
                         q0TY3we+ERB40U8Z2BvU61QuwaunJ2+uGadHo58VSVdggqAo0BSkH58innKKt96J
                         69pcVH/4rmLbXdcmNYGm6iu+MlPQk4BUZknHSmVHIFdJ0EPupVaQ8RHT
                         -----END RSA PRIVATE KEY-----
```

The following table describes the SSH configuration properties.

| Property Name | Remarks |
| --- | --- |
| **ignoreLocalSshSettings** | If `true`, use property-based instead of file-based SSH config. Must be set at as `spring.cloud.config.server.git.ignoreLocalSshSettings`, **not** inside a repository definition. |
| **privateKey** | Valid SSH private key. Must be set if `ignoreLocalSshSettings` is true and Git URI is SSH format. |
| **hostKey** | Valid SSH host key. Must be set if `hostKeyAlgorithm` is also set. |
| **hostKeyAlgorithm** | One of `ssh-dss, ssh-rsa, ssh-ed25519, ecdsa-sha2-nistp256, ecdsa-sha2-nistp384, or ecdsa-sha2-nistp521`. Must be set if `hostKey` is also set. |
| **strictHostKeyChecking** | `true` or `false`. If false, ignore errors with host key. |
| **knownHostsFile** | Location of custom `.known_hosts` file. |
| **preferredAuthentications** | Override server authentication method order. This should allow for evading login prompts if server has keyboard-interactive authentication before the `publickey` method. |

<a id="server-environment-repository-git-backend--placeholders-in-git-search-paths"></a>

## Placeholders in Git Search Paths

Spring Cloud Config Server also supports a search path with placeholders for the `{application}` and `{profile}` (and `{label}` if
you need it), as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          search-paths: '\{application}'
```

The preceding listing causes a search of the repository for files in the same name as the directory (as well as the top level).
Wildcards are also valid in a search path with placeholders (any matching directory is included in the search).

<a id="server-environment-repository-git-backend--force-pull-in-git-repositories"></a>

## Force pull in Git Repositories

As mentioned earlier, Spring Cloud Config Server makes a clone of the remote git repository in case the local copy gets dirty (for example, folder content changes by an OS process) such that Spring Cloud Config Server cannot update the local copy from remote repository.

To solve this issue, there is a `force-pull` property that makes Spring Cloud Config Server force pull from the remote repository if the local copy is dirty, as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          force-pull: true
```

If you have a multiple-repositories configuration, you can configure the `force-pull` property per repository, as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://git/common/config-repo.git
          force-pull: true
          repos:
            team-a:
                pattern: team-a-*
                uri: https://git/team-a/config-repo.git
                force-pull: true
            team-b:
                pattern: team-b-*
                uri: https://git/team-b/config-repo.git
                force-pull: true
            team-c:
                pattern: team-c-*
                uri: https://git/team-a/config-repo.git
```

> [!NOTE]
> The default value for `force-pull` property is `false`.

<a id="server-environment-repository-git-backend--deleting-untracked-branches-in-git-repositories"></a>

## Deleting untracked branches in Git Repositories

As Spring Cloud Config Server has a clone of the remote git repository
after check-outing branch to local repo (e.g fetching properties by label) it will keep this branch
forever or till the next server restart (which creates new local repo).
So there could be a case when remote branch is deleted but local copy of it is still available for fetching.
And if Spring Cloud Config Server client service starts with `--spring.cloud.config.label=deletedRemoteBranch,master`
it will fetch properties from `deletedRemoteBranch` local branch, but not from `master`.

In order to keep local repository branches clean and up to remote - `deleteUntrackedBranches` property could be set.
It will make Spring Cloud Config Server **force** delete untracked branches from local repository.
Example:

```yaml
spring:
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          deleteUntrackedBranches: true
```

> [!NOTE]
> The default value for `deleteUntrackedBranches` property is `false`.

<a id="server-environment-repository-git-backend--git-refresh-rate"></a>

## Git Refresh Rate

You can control how often the config server will fetch updated configuration data
from your Git backend by using `spring.cloud.config.server.git.refreshRate`. The
value of this property is specified in seconds. By default the value is 0, meaning
the config server will fetch updated configuration from the Git repo every time it
is requested. If the value is a negative number the refresh will not occur.

<a id="server-environment-repository-git-backend--default-label"></a>

## Default Label

The default label used for Git is `main`. If you do not set `spring.cloud.config.server.git.defaultLabel` and a branch named `main`
does not exist, the config server will by default also try to checkout a branch named `master`. If
you would like to disable to the fallback branch behavior you can set
`spring.cloud.config.server.git.tryMasterBranch` to `false`.

<a id="server-environment-repository-git-backend--container"></a>
<a id="server-environment-repository-git-backend--running-the-config-server-using-git-in-a-container"></a>

## Running The Config Server Using Git In A Container

If you are getting a `java.io.IOException` when running the Config Server in a container that is similar to:

```none
2022-01-03 20:04:02,892 [tributeWriter-2] ERROR org.eclipse.jgit.util.FS$FileStoreAttributes.saveToConfig - Cannot save config file 'FileBasedConfig[/.config/jgit/config]'
java.io.IOException: Creating directories for /.config/jgit failed
```

You must either:

1. Provide a user with a writeable home directory inside the container.
2. Set the environment variable `XDG_CONFIG_HOME` inside the container to point to a directory where the Java process has write permissions.

[Environment Repository](#server-environment-repository)
[Version Control Backend Filesystem Use](#server-environment-repository-version-control-backend-filesystem-use)

---

<a id="server-environment-repository-version-control-backend-filesystem-use"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/version-control-backend-filesystem-use.html -->

<!-- page_index: 5 -->

# Version Control Backend Filesystem Use

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-version-control-backend-filesystem-use--page-title"></a>
<a id="server-environment-repository-version-control-backend-filesystem-use--version-control-backend-filesystem-use"></a>

# Version Control Backend Filesystem Use

> [!WARNING]
> With VCS-based backends (git, svn), files are checked out or cloned to the local filesystem.
> By default, they are put in the system temporary directory with a prefix of `config-repo-`.
> On linux, for example, it could be `/tmp/config-repo-<randomid>`.
> Some operating systems [routinely clean out](https://serverfault.com/questions/377348/when-does-tmp-get-cleared/377349#377349) temporary directories.
> This can lead to unexpected behavior, such as missing properties.
> To avoid this problem, change the directory that Config Server uses by setting `spring.cloud.config.server.git.basedir` or `spring.cloud.config.server.svn.basedir` to a directory that does not reside in the system temp structure.

<a id="server-environment-repository-version-control-backend-filesystem-use--errors-with-multiple-labels"></a>
<a id="server-environment-repository-version-control-backend-filesystem-use--error-handling-with-multiple-labels"></a>

## Error Handling With Multiple Labels

If a request is made to the config server and the request contains multiple labels the config server
will return property sources for each label. However if trying to fetch one of those labels results in
an error, the config server will return an error without trying any remaining labels.

If you prefer to have the config server ignore any errors when a label is invalid and try all
labels before returning an error you can set `spring.cloud.config.server.[git | svn].continue-on-multiple-label-failure=true`.

[Git Backend](#server-environment-repository-git-backend)
[File System Backend](#server-environment-repository-file-system-backend)

---

<a id="server-environment-repository-file-system-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/file-system-backend.html -->

<!-- page_index: 6 -->

# File System Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-file-system-backend--page-title"></a>
<a id="server-environment-repository-file-system-backend--file-system-backend"></a>

# File System Backend

There is also a “native” profile in the Config Server that does not use Git but loads the config files from the local classpath or file system (any static URL you want to point to with `spring.cloud.config.server.native.searchLocations`).
To use the native profile, launch the Config Server with `spring.profiles.active=native`.

> [!NOTE]
> Remember to use the `file:` prefix for file resources (the default without a prefix is usually the classpath).
> As with any Spring Boot configuration, you can embed `${}`-style environment placeholders, but remember that absolute paths in Windows require an extra `/` (for example, `/${user.home}/config-repo`).

> [!WARNING]
> The default value of the `searchLocations` is identical to a local Spring Boot application (that is, `[classpath:/, classpath:/config, file:./, file:./config]`).
> This does not expose the `application.properties` from the server to all clients, because any property sources present in the server are removed before being sent to the client.

> [!TIP]
> A filesystem backend is great for getting started quickly and for testing.
> To use it in production, you need to be sure that the file system is reliable and shared across all instances of the Config Server.

The search locations can contain placeholders for `{application}`, `{profile}`, and `{label}`.
In this way, you can segregate the directories in the path and choose a strategy that makes sense for you (such as subdirectory per application or subdirectory per profile).

If you do not use placeholders in the search locations, this repository also appends the `{label}` parameter of the HTTP resource to a suffix on the search path, so properties files are loaded from each search location **and** a subdirectory with the same name as the label (the labelled properties take precedence in the Spring Environment).
Thus, the default behaviour with no placeholders is the same as adding a search location ending with `/{label}/`.
For example, `file:/tmp/config` is the same as `file:/tmp/config,file:/tmp/config/{label}`.
This behavior can be disabled by setting `spring.cloud.config.server.native.addLabelLocations=false`.

[Version Control Backend Filesystem Use](#server-environment-repository-version-control-backend-filesystem-use)
[Vault Backend](#server-environment-repository-vault-backend)

---

<a id="server-environment-repository-vault-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/vault-backend.html -->

<!-- page_index: 7 -->

# Vault Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-vault-backend--page-title"></a>
<a id="server-environment-repository-vault-backend--vault-backend"></a>

# Vault Backend

Spring Cloud Config Server also supports [Vault](https://www.vaultproject.io) as a backend.

For more information on Vault, see the [Vault quick start guide](https://learn.hashicorp.com/vault/?track=getting-started#getting-started).

To enable the config server to use a Vault backend, you can run your config server with the `vault` profile.
For example, in your config server’s `application.properties`, you can add `spring.profiles.active=vault`.

By default, the config server assumes that your Vault server runs at `127.0.0.1:8200`.
It also assumes that the name of backend is `secret` and the key is `application`.
All of these defaults can be configured in your config server’s `application.properties`.
The following table describes configurable Vault properties:

| Name | Default Value |
| --- | --- |
| host | 127.0.0.1 |
| port | 8200 |
| scheme | http |
| backend | secret |
| fullKeyPath | false |
| defaultKey | application |
| defaultLabel | main (Only used when `enableLabel` is set to `true`) |
| enableLabel | false |
| profileSeparator | , |
| kvVersion | 1 |
| skipSslValidation | false |
| timeout | 5 |
| namespace | null |

> [!IMPORTANT]
> All of the properties in the preceding table must be prefixed with `spring.cloud.config.server.vault` or placed in the correct Vault section of a composite configuration.

All configurable properties can be found in `org.springframework.cloud.config.server.environment.VaultEnvironmentProperties`.

> [!IMPORTANT]
> Vault 0.10.0 introduced a versioned key-value backend (k/v backend version 2) that exposes a different API than earlier versions, it now requires a `data/` between the mount path and the actual context path and wraps secrets in a `data` object. Setting `spring.cloud.config.server.vault.kv-version=2` will take this into account.

Optionally, there is support for the Vault Enterprise `X-Vault-Namespace` header. To have it sent to Vault set the `namespace` property.

With your config server running, you can make HTTP requests to the server to retrieve
values from the Vault backend.
To do so, you need a token for your Vault server.

First, place some data in you Vault, as shown in the following example:

```sh
$ vault kv put secret/application foo=bar baz=bam
$ vault kv put secret/myapp foo=myappsbar
```

Second, make an HTTP request to your config server to retrieve the values, as shown in the following example:

`$ curl -X "GET" "http://localhost:8888/myapp/default" -H "X-Config-Token: yourtoken"`

You should see a response similar to the following:

```json
{"name":"myapp","profiles":["default" ],"label":null,"version":null,"state":null,"propertySources":[{"name":"vault:myapp","source":{"foo":"myappsbar"} },{"name":"vault:application","source":{"baz":"bam","foo":"bar"}}]}
```

The default way for a client to provide the necessary authentication to let Config Server talk to Vault is to set the X-Config-Token header.
However, you can instead omit the header and configure the authentication in the server, by setting the same configuration properties as Spring Cloud Vault.
The property to set is `spring.cloud.config.server.vault.authentication`.
It should be set to one of the supported authentication methods.
You may also need to set other properties specific to the authentication method you use, by using the same property names as documented for `spring.cloud.vault` but instead using the `spring.cloud.config.server.vault` prefix.
See the [Spring Cloud Vault Reference Guide](https://cloud.spring.io/spring-cloud-vault/reference/html/#vault.config.authentication) for more detail.

> [!IMPORTANT]
> If you omit the X-Config-Token header and use a server property to set the authentication, the Config Server application needs an additional dependency on Spring Vault to enable the additional authentication options.
> See the [Spring Vault Reference Guide](https://docs.spring.io/spring-vault/docs/current/reference/html/#dependencies) for how to add that dependency.

<a id="server-environment-repository-vault-backend--multiple-properties-sources"></a>

## Multiple Properties Sources

When using Vault, you can provide your applications with multiple properties sources.
For example, assume you have written data to the following paths in Vault:

```sh
secret/myApp,dev
secret/myApp
secret/application,dev
secret/application
```

Properties written to `secret/application` are available to [all applications using the Config Server](#server-environment-repository-vault-backend--_vault_server).
An application with the name, `myApp`, would have any properties written to `secret/myApp` and `secret/application` available to it.
When `myApp` has the `dev` profile enabled, properties written to all of the above paths would be available to it, with properties in the first path in the list taking priority over the others.

<a id="server-environment-repository-vault-backend--full-key-path"></a>
<a id="server-environment-repository-vault-backend--disambiguating-composite-property-sources"></a>

## Disambiguating Composite Property Sources

By default, the config server generates property source names based on the vault key, e.g. `vault:myApp` in the example above.
When composite vault backends have the same vault key, the config server client will overwrite preceding property sources.

With `fullKeyPath` set to `true`, the property sources will contain the full backend path, e.g. `vault:secret/backendA/myApp` and `vault:secret/backendB/myApp`, preventing overwriting the preceding property source.

```yaml
spring.cloud.config.server.composite:
  - type: vault
    fullKeyPath: true
    # ...
    backend: secret/backendA
  - type: vault
    fullKeyPath: true
    # ...
    backend: secret/backendB
```

<a id="server-environment-repository-vault-backend--enabling-serach-by-label"></a>
<a id="server-environment-repository-vault-backend--enabling-search-by-label"></a>

## Enabling Search by Label

By default, Vault backend does not use the label when searching for secrets. You can change this by
setting the `enableLabel` feature flag to `true` and, optionally, setting the `defaultLabel`.
When `defaultLabel` is not provided `main` will be used.

When `enableLabel` feature flag is on, the secrets in Vault should always have all three segments(application name, profile and label) in their paths.
So the example in previous section, with enabled feature flag, would be like :

```sh
secret/myApp,dev,myLabel
secret/myApp,default,myLabel       # default profile
secret/application,dev,myLabel     # default application name
secret/application,default,myLabel # default application name and default profile.
```

<a id="server-environment-repository-vault-backend--decrypting-vault-secrets"></a>
<a id="server-environment-repository-vault-backend--decrypting-vault-secrets-in-property-sources"></a>

## Decrypting Vault Secrets in Property Sources

Spring Cloud Config Server supports decrypting properties from Vault by utilizing a special placeholder prefix `{vault}`. This feature allows for dynamic resolution of sensitive configuration properties directly from Vault at runtime.

<a id="server-environment-repository-vault-backend--_configuration_steps"></a>
<a id="server-environment-repository-vault-backend--configuration-steps"></a>

### Configuration Steps

All configuration settings for integrating with Vault should be placed in your `application.yml` or `application.properties`. Below are the specific configurations required to activate the Vault profile, connect to your Vault server, and format properties using the `{vault}` prefix.

<a id="server-environment-repository-vault-backend--_enable_vault_profile"></a>
<a id="server-environment-repository-vault-backend--enable-vault-profile"></a>

#### Enable Vault Profile

Activate the Vault profile for your Spring Cloud Config Server:

```yaml
spring:
  profiles:
    active: vault
```

<a id="server-environment-repository-vault-backend--_vault_configuration"></a>
<a id="server-environment-repository-vault-backend--vault-configuration"></a>

#### Vault Configuration

Set up the connection to your Vault server with the necessary authentication details:

```yaml
spring:
  cloud:
    config:
      server:
        vault:
          host: vault.example.com
          port: 8200
          scheme: https
          backend: secret
          defaultKey: application
          kvVersion: 2
          authentication: TOKEN
          token: ${VAULT_TOKEN}
          skipSslValidation: true
```

These settings specify the Vault server address, authentication method, and the token required to access Vault.

<a id="server-environment-repository-vault-backend--_property_formatting"></a>
<a id="server-environment-repository-vault-backend--property-formatting"></a>

#### Property Formatting

Define properties with the `{vault}` prefix to specify the Vault path and key for retrieving secrets:

```yaml
some:
  sensitive:
    value: '{vault}:path/to/secret#key'
```

This format directly maps to the location in Vault where the secret is stored (`path/to/secret`) and the specific secret key (`key`) to be retrieved.

<a id="server-environment-repository-vault-backend--_error_handling"></a>
<a id="server-environment-repository-vault-backend--error-handling"></a>

### Error Handling

If the Config Server encounters any issues during the decryption process, such as incorrect paths, access issues, or missing keys, the affected property will be prefixed with `invalid.` and its value will be set to `<n/a>`. This approach is similar to the handling of properties prefixed with `{cipher}`, but it is specifically tailored for integration with Vault, providing clear feedback when decryption fails.

[File System Backend](#server-environment-repository-file-system-backend)
[Accessing Backends Through a Proxy](#server-environment-repository-accessing-backends-through-a-proxy)

---

<a id="server-environment-repository-accessing-backends-through-a-proxy"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/accessing-backends-through-a-proxy.html -->

<!-- page_index: 8 -->

# Accessing Backends Through a Proxy

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-accessing-backends-through-a-proxy--page-title"></a>
<a id="server-environment-repository-accessing-backends-through-a-proxy--accessing-backends-through-a-proxy"></a>

# Accessing Backends Through a Proxy

The configuration server can access a Git or Vault backend through an HTTP or HTTPS proxy.
This behavior is controlled for either Git or Vault by settings under `proxy.http` and `proxy.https`.
These settings are per repository, so if you are using a [composite environment repository](#server-environment-repository-composite-repositories) you must configure proxy settings for each backend in the composite individually.
If using a network which requires separate proxy servers for HTTP and HTTPS URLs, you can configure both the HTTP and the HTTPS proxy settings for a single backend: in this case `http` access will use `http` proxy and `https` access the `https` one.
Also, you may specify one sole proxy that will be used for both protocols using the proxy definition protocol between application and proxy.

The following table describes the proxy configuration properties for both HTTP and HTTPS proxies. All of these properties must be prefixed by `proxy.http` or `proxy.https`.

| Property Name | Remarks |
| --- | --- |
| **host** | The host of the proxy. |
| **port** | The port with which to access the proxy. |
| **nonProxyHosts** | Any hosts which the configuration server should access outside the proxy. If values are provided for both `proxy.http.nonProxyHosts` and `proxy.https.nonProxyHosts`, the `proxy.http` value will be used. |
| **username** | The username with which to authenticate to the proxy. If values are provided for both `proxy.http.username` and `proxy.https.username`, the `proxy.http` value will be used. |
| **password** | The password with which to authenticate to the proxy. If values are provided for both `proxy.http.password` and `proxy.https.password`, the `proxy.http` value will be used. |

The following configuration uses an HTTPS proxy to access a Git repository.

```yaml
spring:
  profiles:
    active: git
  cloud:
    config:
      server:
        git:
          uri: https://github.com/spring-cloud-samples/config-repo
          proxy:
            https:
              host: my-proxy.host.io
              password: myproxypassword
              port: '3128'
              username: myproxyusername
              nonProxyHosts: example.com
```

[Vault Backend](#server-environment-repository-vault-backend)
[Sharing Configuration With All Applications](#server-environment-repository-sharing-configuration-with-all-applications)

---

<a id="server-environment-repository-sharing-configuration-with-all-applications"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/sharing-configuration-with-all-applications.html -->

<!-- page_index: 9 -->

# Sharing Configuration With All Applications

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-sharing-configuration-with-all-applications--page-title"></a>
<a id="server-environment-repository-sharing-configuration-with-all-applications--sharing-configuration-with-all-applications"></a>

# Sharing Configuration With All Applications

Sharing configuration between all applications varies according to which approach you take, as described in the following topics:

- [File Based Repositories](#server-environment-repository-sharing-configuration-with-all-applications--spring-cloud-config-server-file-based-repositories)
- [Vault Server](#server-environment-repository-sharing-configuration-with-all-applications--spring-cloud-config-server-vault-server)
- [CredHub Server](#server-environment-repository-sharing-configuration-with-all-applications--credhub-server)
- [JDBC Repository](#server-environment-repository-sharing-configuration-with-all-applications--spring-cloud-config-server-jdbc)

<a id="server-environment-repository-sharing-configuration-with-all-applications--spring-cloud-config-server-file-based-repositories"></a>
<a id="server-environment-repository-sharing-configuration-with-all-applications--file-based-repositories"></a>

## File Based Repositories

With file-based (git, svn, and native) repositories, resources with file names in `application*` (`application.properties`, `application.yml`, `application-*.properties`, and so on) are shared between all client applications.
You can use resources with these file names to configure global defaults and have them be overridden by application-specific files as necessary.

The [property overrides](#server-environment-repository-property-overrides) feature can also be used for setting global defaults, with placeholders applications
allowed to override them locally.

> [!TIP]
> With the “native” profile (a local file system backend) , you should use an explicit search location that is not part of the server’s own configuration.
> Otherwise, the `application*` resources in the default search locations get removed because they are part of the server.

<a id="server-environment-repository-sharing-configuration-with-all-applications--spring-cloud-config-server-vault-server"></a>
<a id="server-environment-repository-sharing-configuration-with-all-applications--vault-server"></a>

## Vault Server

When using Vault as a backend, you can share configuration with all applications by placing configuration in `secret/application`.
For example, if you run the following Vault command, all applications using the config server will have the properties `foo` and `baz` available to them:

```sh
$ vault write secret/application foo=bar baz=bam
```

<a id="server-environment-repository-sharing-configuration-with-all-applications--credhub-server"></a>

## CredHub Server

When using CredHub as a backend, you can share configuration with all applications by placing configuration in `/application/` or by placing it in the `default` profile for the application.
For example, if you run the following CredHub command, all applications using the config server will have the properties `shared.color1` and `shared.color2` available to them:

```sh
credhub set --name "/application/profile/master/shared" --type=json
value: {"shared.color1": "blue", "shared.color": "red"}
```

```sh
credhub set --name "/my-app/default/master/more-shared" --type=json
value: {"shared.word1": "hello", "shared.word2": "world"}
```

<a id="server-environment-repository-sharing-configuration-with-all-applications--spring-cloud-config-server-jdbc"></a>
<a id="server-environment-repository-sharing-configuration-with-all-applications--jdbc-environment-repository"></a>

## JDBC Environment Repository

To share configurations using the JDBC backend, insert records into your database with `'application'` as the value in the application column for entries intended to be shared across all clients. Application-specific properties can then override these shared configurations, providing flexibility and control over your application environments.

```sql
INSERT INTO PROPERTIES (APPLICATION, PROFILE, LABEL, KEY, VALUE)
VALUES ('application', 'default', 'master', 'a.b.c', 'shared-value');
INSERT INTO PROPERTIES (APPLICATION, PROFILE, LABEL, KEY, VALUE)
VALUES ('myapp', 'prod', 'master', 'd.e.f', 'specific-value');
```

Refer to the `JdbcEnvironmentRepository` implementation and associated tests for detailed examples on setup and configuration management using the JDBC repository.

[Accessing Backends Through a Proxy](#server-environment-repository-accessing-backends-through-a-proxy)
[AWS Secrets Manager](#server-environment-repository-aws-secrets-manager)

---

<a id="server-environment-repository-aws-secrets-manager"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/aws-secrets-manager.html -->

<!-- page_index: 10 -->

# AWS Secrets Manager

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-aws-secrets-manager--page-title"></a>
<a id="server-environment-repository-aws-secrets-manager--aws-secrets-manager"></a>

# AWS Secrets Manager

When using AWS Secrets Manager as a backend, you can share configuration with all applications by placing configuration in `/application/` or by placing it in the `default` profile for the application.
For example, if you add secrets with the following keys, all application using the config server will have the properties `shared.foo` and `shared.bar` available to them:

```none
secret name = /secret/application-default/
```

```json
secret value =
{
 shared.foo: foo,
 shared.bar: bar
}
```

or

```none
secret name = /secret/application/
```

```json
secret value =
{
 shared.foo: foo,
 shared.bar: bar
}
```

<a id="server-environment-repository-aws-secrets-manager--labelled-versions"></a>

## Labelled Versions

AWS Secrets Manager repository allows to keep labelled versions of the configuration environments the same way Git backend does.

The repository implementation maps the `{label}` parameter of the HTTP resource to [AWS Secrets Manager secret’s staging label](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version). To create a labelled secret, create a secret or update its content and define a staging label for it (sometimes it’s called version stage in the AWS documentation). For example:

```sh
$ aws secretsmanager create-secret \ --name /secret/test/ \ --secret-string '{"version":"1"}' {"ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:/secret/test/-a1b2c3","Name": "/secret/test/","VersionId": "cd291674-de2f-41de-8f3b-37dbf4880d69"}
$ aws secretsmanager update-secret-version-stage \ --secret-id /secret/test/ \ --version-stage 1.0.0 \ --move-to-version-id cd291674-de2f-41de-8f3b-37dbf4880d69 {"ARN": "arn:aws:secretsmanager:us-east-1:123456789012:secret:/secret/test/-a1b2c3","Name": "/secret/test/",}
```

Use `spring.cloud.config.server.aws-secretsmanager.default-label` property to set the default label. If the property is not defined, the backend uses AWSCURRENT as a staging label.

```yaml
spring:
  profiles:
    active: aws-secretsmanager
  cloud:
    config:
      server:
        aws-secretsmanager:
          region: us-east-1
          default-label: 1.0.0
```

Note that if the default label is not set and a request does not define a label, the repository will use secrets as if labelled version support is disabled. Also, the default label will be used only if the labelled support is enabled. Otherwise, defining this property is pointless.

Note that if the staging label contains a slash (`/`), then the label in the HTTP URL should instead be specified with the special string `({special-string})` (to avoid ambiguity with other URL paths) the same way [Git backend’s section](#server-environment-repository-aws-secrets-manager--_git_backend) describes it.

Use `spring.cloud.config.server.aws-secretsmanager.ignore-label` property to ignore the `{label}` parameter of the HTTP resource as well as `spring.cloud.config.server.aws-secretsmanager.default-label` property. The repository will use secrets as if labelled version support is disabled.

```yaml
spring:
  profiles:
    active: aws-secretsmanager
  cloud:
    config:
      server:
        aws-secretsmanager:
          region: us-east-1
          ignore-label: true
```

[Sharing Configuration With All Applications](#server-environment-repository-sharing-configuration-with-all-applications)
[AWS Parameter Store](#server-environment-repository-aws-parameter-store)

---

<a id="server-environment-repository-aws-parameter-store"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/aws-parameter-store.html -->

<!-- page_index: 11 -->

# AWS Parameter Store

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-aws-parameter-store--page-title"></a>
<a id="server-environment-repository-aws-parameter-store--aws-parameter-store"></a>

# AWS Parameter Store

When using AWS Parameter Store as a backend, you can share configuration with all applications by placing properties within the `/application` hierarchy.

For example, if you add parameters with the following names, all applications using the config server will have the properties `foo.bar` and `fred.baz` available to them:

```none
/config/application/foo.bar
/config/application-default/fred.baz
```

[AWS Secrets Manager](#server-environment-repository-aws-secrets-manager)
[JDBC Backend](#server-environment-repository-jdbc-backend)

---

<a id="server-environment-repository-jdbc-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/jdbc-backend.html -->

<!-- page_index: 12 -->

# JDBC Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-jdbc-backend--page-title"></a>
<a id="server-environment-repository-jdbc-backend--jdbc-backend"></a>

# JDBC Backend

Spring Cloud Config Server supports JDBC (relational database) as a backend for configuration properties.
You can enable this feature by adding `spring-boot-starter-data-jdbc` to the classpath and using the `jdbc` profile or by adding a bean of type `JdbcEnvironmentRepository`.
If you include the right dependencies on the classpath (see the user guide for more details on that), Spring Boot configures a data source.

You can disable autoconfiguration for `JdbcEnvironmentRepository` by setting the `spring.cloud.config.server.jdbc.enabled` property to `false`.

The database needs to have a table called `PROPERTIES` with columns called `APPLICATION`, `PROFILE`, and `LABEL` (with the usual `Environment` meaning), plus `KEY` and `VALUE` for the key and value pairs in `Properties` style.
All fields are of type String in Java, so you can make them `VARCHAR` of whatever length you need.
Property values behave in the same way as they would if they came from Spring Boot properties files named `{application}-{profile}.properties`, including all the encryption and decryption, which will be applied as post-processing steps (that is, not in the repository implementation directly).

> [!NOTE]
> The default label used for JDBC is `master`. You can change that by setting `spring.cloud.config.server.jdbc.defaultLabel`.

[AWS Parameter Store](#server-environment-repository-aws-parameter-store)
[Redis Backend](#server-environment-repository-redis-backend)

---

<a id="server-environment-repository-redis-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/redis-backend.html -->

<!-- page_index: 13 -->

# Redis Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-redis-backend--page-title"></a>
<a id="server-environment-repository-redis-backend--redis-backend"></a>

# Redis Backend

Spring Cloud Config Server supports Redis as a backend for configuration properties.
You can enable this feature by adding a dependency to [Spring Data Redis](https://spring.io/projects/spring-data-redis).

pom.xml

```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-data-redis</artifactId>
	</dependency>
</dependencies>
```

The following configuration uses Spring Data `RedisTemplate` to access a Redis. We can use `spring.redis.*` properties to override default connection settings.

```yaml
spring:
  profiles:
    active: redis
  redis:
    host: redis
    port: 16379
```

The properties should be stored as fields in a hash. The name of hash should be the same as `spring.application.name` property or conjunction of `spring.application.name` and `spring.profiles.active[n]`.

```sh
HMSET sample-app server.port "8100" sample.topic.name "test" test.property1 "property1"
```

After running the command visible above a hash should contain the following keys with values:

```
HGETALL sample-app
{
  "server.port": "8100",
  "sample.topic.name": "test",
  "test.property1": "property1"
}
```

> [!NOTE]
> When no profile is specified `default` will be used.

[JDBC Backend](#server-environment-repository-jdbc-backend)
[AWS S3 Backend](#server-environment-repository-aws-s3-backend)

---

<a id="server-environment-repository-aws-s3-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/aws-s3-backend.html -->

<!-- page_index: 14 -->

# AWS S3 Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-aws-s3-backend--page-title"></a>
<a id="server-environment-repository-aws-s3-backend--aws-s3-backend"></a>

# AWS S3 Backend

Spring Cloud Config Server supports AWS S3 as a backend for configuration properties.
You can enable this feature by adding a dependency to the [AWS Java SDK For Amazon S3](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/examples-s3.html).

pom.xml

```xml
<dependencies>
	<dependency>
		<groupId>software.amazon.awssdk</groupId>
		<artifactId>s3</artifactId>
	</dependency>
</dependencies>
```

The following configuration uses the AWS S3 client to access configuration files. We can use `spring.cloud.config.server.awss3.*` properties to select the bucket where your configuration is stored.

```yaml
spring:
  profiles:
    active: awss3
  cloud:
    config:
      server:
        awss3:
          region: us-east-1
          bucket: bucket1
```

It is also possible to specify an AWS URL to [override the standard endpoint](https://aws.amazon.com/blogs/developer/using-new-regions-and-endpoints/) of your S3 service with `spring.cloud.config.server.awss3.endpoint`. This allows support for beta regions of S3, and other S3 compatible storage APIs.

Credentials are found using the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/credentials.html). Versioned and encrypted buckets are supported without further configuration.

By default, configuration files are stored in your bucket as `{application}-{profile}.properties`, `{application}-{profile}.yml` or `{application}-{profile}.json`. An optional label can be provided to specify a directory path to the file.

> [!NOTE]
> When no profile is specified `default` will be used.

<a id="server-environment-repository-aws-s3-backend--directory-layout"></a>

## Directory layout

Spring Cloud Config Server also supports per-app directory layout analogous to [`search-paths: '{application}'`](#server-environment-repository-git-backend--placeholders-in-git-search-paths) in Git backend.

In order to enable it set `useDirectoryLayout` property to `true` as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        awss3:
          region: us-east-1
          bucket: bucket1
          useDirectoryLayout: true
```

The preceding listing matches objects stored in your bucket in `/{application}` directory like: `/{application}/application\{-profile}.yml`. Then structure of the bucket should look like this:

```none
├── foo
│   ├── application-test.yml
│   └── application.yml
├── bar
│   ├── application-test.yml
│   └── application.yml
```

[Redis Backend](#server-environment-repository-redis-backend)
[AWS Parameter Store Backend](#server-environment-repository-aws-parameter-store-backend)

---

<a id="server-environment-repository-aws-parameter-store-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/aws-parameter-store-backend.html -->

<!-- page_index: 15 -->

# AWS Parameter Store Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-aws-parameter-store-backend--page-title"></a>
<a id="server-environment-repository-aws-parameter-store-backend--aws-parameter-store-backend"></a>

# AWS Parameter Store Backend

Spring Cloud Config Server supports AWS Parameter Store as a backend for configuration properties. You can enable this feature by adding a dependency to the [AWS Java SDK for SSM](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/examples-ssm.html).

pom.xml

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>ssm</artifactId>
</dependency>
```

The following configuration uses the AWS SSM client to access parameters.

```yaml
spring:
  profiles:
    active: awsparamstore
  cloud:
    config:
      server:
        awsparamstore:
          region: eu-west-2
          endpoint: https://ssm.eu-west-2.amazonaws.com
          origin: aws:parameter:
          prefix: /config/service
          profile-separator: _
          recursive: true
          decrypt-values: true
          max-results: 5
```

The following table describes the AWS Parameter Store configuration properties.

| Property Name | Required | Default Value | Remarks |
| --- | --- | --- | --- |
| **region** | no |  | The region to be used by the AWS Parameter Store client. If it’s not explicitly set, the SDK tries to determine the region to use by using the [Default Region Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/region-selection.html#default-region-provider-chain). |
| **endpoint** | no |  | The URL of the entry point for the AWS SSM client. This can be used to specify an alternate endpoint for the API requests. |
| **origin** | no | `aws:ssm:parameter:` | The prefix that is added to the property source’s name to show their provenance. |
| **prefix** | no | `/config` | Prefix indicating L1 level in the parameter hierarchy for every property loaded from the AWS Parameter Store. |
| **profile-separator** | no | `-` | String that separates an appended profile from the context name. |
| **recursive** | no | `true` | Flag to indicate the retrieval of all AWS parameters within a hierarchy. |
| **decrypt-values** | no | `true` | Flag to indicate the retrieval of all AWS parameters with their value decrypted. |
| **max-results** | no | `10` | The maximum number of items to return for an AWS Parameter Store API call. |

AWS Parameter Store API credentials are determined using the [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/credentials.html#credentials-default).
Versioned parameters are already supported with the default behaviour of returning the latest version.

> [!NOTE]
> - When no application is specified `application` is the default, and when no profile is specified `default` is used.
> - Valid values for `awsparamstore.prefix` must start with a forward slash followed by one or more valid path segments or be empty.
> - Valid values for `awsparamstore.profile-separator` can only contain dots, dashes and underscores.
> - Valid values for `awsparamstore.max-results` must be within the **[1, 10]** range.

[AWS S3 Backend](#server-environment-repository-aws-s3-backend)
[AWS Secrets Manager Backend](#server-environment-repository-aws-secrets-manager-backend)

---

<a id="server-environment-repository-aws-secrets-manager-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/aws-secrets-manager-backend.html -->

<!-- page_index: 16 -->

# AWS Secrets Manager Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-aws-secrets-manager-backend--page-title"></a>
<a id="server-environment-repository-aws-secrets-manager-backend--aws-secrets-manager-backend"></a>

# AWS Secrets Manager Backend

Spring Cloud Config Server supports [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) as a backend for configuration properties.
You can enable this feature by adding a dependency to [AWS Java SDK for Secrets Manager](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/examples-secretsmanager.html).

pom.xml

```xml
<dependency>
    <groupId>software.amazon.awssdk</groupId>
    <artifactId>secretsmanager</artifactId>
</dependency>
```

The following configuration uses the AWS Secrets Manager client to access secrets.

```yaml
spring:
  profiles:
  	active: awssecretsmanager
  cloud:
    config:
      server:
        aws-secretsmanager:
          region: us-east-1
          endpoint: https://us-east-1.console.aws.amazon.com/
          origin: aws:secrets:
          prefix: /secret/foo
          profileSeparator: _
```

AWS Secrets Manager API credentials are determined using [Default Credential Provider Chain](https://docs.aws.amazon.com/sdk-for-java/v2/developer-guide/credentials.html#credentials-default).

> [!NOTE]
> - When no application is specified `application` is the default, and when no profile is specified `default` is used.
> - Both `label` and `defaultLabel` properties are ignored, when `ignoreLabel` is set to `true`.

[AWS Parameter Store Backend](#server-environment-repository-aws-parameter-store-backend)
[Google Secret Manager Backend](#server-environment-repository-gcp-secret-manager-backend)

---

<a id="server-environment-repository-gcp-secret-manager-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/gcp-secret-manager-backend.html -->

<!-- page_index: 17 -->

# Google Secret Manager Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-gcp-secret-manager-backend--page-title"></a>
<a id="server-environment-repository-gcp-secret-manager-backend--google-secret-manager-backend"></a>

# Google Secret Manager Backend

Spring Cloud Config Server can use [Google Cloud Secret Manager](https://cloud.google.com/secret-manager) as an `EnvironmentRepository`.
Secrets are exposed as a `PropertySource` whose entries are built from secret payloads.

<a id="server-environment-repository-gcp-secret-manager-backend--_enabling_the_backend"></a>
<a id="server-environment-repository-gcp-secret-manager-backend--enabling-the-backend"></a>

## Enabling the backend

The repository is registered when all of the following hold:

- The Spring profile `secret-manager` is active.
- `com.google.cloud.secretmanager.v1.SecretManagerServiceClient` is on the classpath (typically by adding `google-cloud-secretmanager`).

pom.xml

```xml
<dependency>
    <groupId>com.google.cloud</groupId>
    <artifactId>google-cloud-secretmanager</artifactId>
</dependency>
```

If you use `spring-cloud-config-server` without its optional Google libraries, add the artifacts your build needs explicitly.
The permission check described below uses the Cloud Resource Manager API; include `google-api-services-cloudresourcemanager` and `google-auth-library-oauth2-http` when you rely on that behavior.

```yaml
spring:
  profiles:
    active: secret-manager
  cloud:
    config:
      server:
        gcp-secret-manager:
          order: 0
          application-label: application
          profile-label: profile
          service-account: /path/to/service-account.json
          token-mandatory: true
          version: 1
```

Configuration properties are bound under `spring.cloud.config.server.gcp-secret-manager`:

| Property | Default | Description |
| --- | --- | --- |
| `order` | Same as other environment repositories | Order in a composite repository (`org.springframework.core.Ordered`). |
| `application-label` | `application` | Secret Manager label key used to match the Config Server `{application}` name (see [Mapping applications and profiles](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-mapping)). |
| `profile-label` | `profile` | Secret Manager label key used to match each active profile (see [Mapping applications and profiles](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-mapping)). |
| `service-account` | *empty* | Path to a Google Cloud service account JSON key file. If set, the Secret Manager client uses these credentials. If unset, the client uses [Application Default Credentials](https://cloud.google.com/docs/authentication/application-default-credentials) (for example the metadata server on Google Compute Engine). |
| `token-mandatory` | `true` | When `true`, secrets are only loaded if [Optional permission check (`token-mandatory`)](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-permission-check) succeeds. When `false`, that check is skipped and secrets are loaded using only the server-side Secret Manager credentials. Also controls whether [`allowed-project-ids`](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project) applies to client-supplied `X-Project-ID` (see below). |
| `allowed-project-ids` | *empty* | When `token-mandatory` is `false`: allow-list for non-empty [`X-Project-ID`](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project). When empty, client-supplied project IDs are rejected. When `token-mandatory` is `true`, this property is ignored for the header ([Optional permission check (`token-mandatory`)](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-permission-check) applies instead). Not applied to metadata or [`project-id`](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project). |
| `project-id` | *empty* | Fallback Google Cloud project when `X-Project-ID` is absent and [metadata](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project) is unavailable (for example local development). Not validated against `allowed-project-ids`. |
| `version` | `1` | API access strategy version (only `1` is supported). |

<a id="server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-mapping"></a>
<a id="server-environment-repository-gcp-secret-manager-backend--mapping-applications-and-profiles"></a>

## Mapping applications and profiles

The server lists secrets in the Google Cloud project (see [Resolving the Google Cloud project](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project)) and filters them for each Config Client request.

- **Label-based matching (default):** A secret is included for a given `{application}` and profile when its Secret Manager labels match, case-insensitively, on the configured keys (`application-label` and `profile-label`). If a label is missing on the secret, the code treats it as the default string `application` or `profile` respectively (same keys as the property names), so unlabeled secrets align with those defaults.
- **Prefix-based matching:** If the HTTP request includes a non-empty `X-Secret-Prefix` header, secrets whose **short** name (the segment after `projects/…/secrets/`) starts with that prefix are also included. The prefix is stripped from the property key. This path can be combined with label filtering logic in the same loop (see `GoogleSecretManagerEnvironmentRepository`).

The repository always ensures the `default` profile is considered before additional profiles (similar to other backends): if the client does not send `default` first, the server prepends it.

For each matching secret, the property **value** is the payload of the **latest enabled** secret version, where “latest” is determined by comparing numeric version IDs (not the Secret Manager “latest” alias).

Property sources are named `gsm:{application}-{profile}`.

The Config Server `{label}` path segment is accepted on the API but **this backend does not use it** to select secrets; version selection is based on secret versions as described above.

<a id="server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project"></a>
<a id="server-environment-repository-gcp-secret-manager-backend--resolving-the-google-cloud-project"></a>

## Resolving the Google Cloud project

Secret Manager API calls are scoped to a project ID. Resolution is performed by `GcpProjectResolutionSupport` inside `GoogleSecretManagerV1AccessStrategy` using the current HTTP request headers, optional metadata, and configuration.

The project is chosen in this order:

1. **Non-empty `X-Project-ID` header** (after trim). If `token-mandatory` is `true`, the header value is accepted without an allow-list check; access for that project is then enforced by [Optional permission check (`token-mandatory`)](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-permission-check). If `token-mandatory` is `false`, the project must appear in `allowed-project-ids`. When that list is **empty**, client-supplied project IDs are **not** allowed.
2. **GCE metadata:** GET `metadata.google.internal/computeMetadata/v1/project/project-id` with header `Metadata-Flavor: Google`. Uses the instance’s project (the client cannot steer via this path). The allow-list is **not** applied.
3. **`project-id` property:** `spring.cloud.config.server.gcp-secret-manager.project-id`, when set and metadata did not yield a project. Server-admin configuration only; the allow-list is **not** applied.

If no project can be resolved, `getSecrets()` behaves as if there were no secrets (no GSM-backed entries), and `checkRemotePermissions()` returns `false` when `token-mandatory` is `true`—so the repository contributes **no** GSM `PropertySource` for that request, consistent with a failed permission check.

> [!WARNING]
> Setting `token-mandatory` to `false` allows clients to load secrets from any project in the `allowed-project-ids` list. It is recommended you never set `token-mandatory` to `false` so the [Optional permission check (`token-mandatory`)](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-permission-check) is performed before loading any secrets.

> [!NOTE]
> With `token-mandatory` `false`, clients that rely on `X-Project-ID` must list allowed project ID(s) in `allowed-project-ids`.

<a id="server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-credentials"></a>
<a id="server-environment-repository-gcp-secret-manager-backend--credentials-for-listing-and-reading-secrets"></a>

## Credentials for listing and reading secrets

Listing secrets and accessing secret values uses `SecretManagerServiceClient` only:

- With `service-account` set: credentials from that JSON file.
- Without it: Application Default Credentials.

The OAuth access token in `X-Config-Token` is **not** passed to the Secret Manager client. Those credentials are always the server’s (or the key file’s), independent of the client token.

<a id="server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-permission-check"></a>
<a id="server-environment-repository-gcp-secret-manager-backend--optional-permission-check-token-mandatory"></a>

## Optional permission check (`token-mandatory`)

When `token-mandatory` is `true` (default), before loading any secrets the server calls `checkRemotePermissions()` on the access strategy. That method resolves the target project the same way as Secret Manager calls (see [Resolving the Google Cloud project](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project)), then:

1. Reads the access token from the `X-Config-Token` HTTP header (required for this check; a missing or invalid header causes the check to fail).
2. If the project could not be resolved, the check fails.
3. Uses the Cloud Resource Manager REST API `projects.testIamPermissions` for that project with the permission `secretmanager.versions.access`.
4. If that permission is reported for the token, the check passes and secrets are loaded. If not, or if the API call fails, the check fails and **no** GSM-backed property sources are added for that request.

So the token in `X-Config-Token` acts as a **gate** for whether GSM data is returned when `token-mandatory` is `true`, while **reading** secrets still uses [the server’s Secret Manager credentials](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-credentials). The principal that passes IAM testing and the principal used for Secret Manager API calls can differ.

When `token-mandatory` is `false`, this remote check is not performed and secrets are loaded solely subject to server credentials and Secret Manager data access (subject to [project resolution](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-project) and `allowed-project-ids` when using `X-Project-ID`).

<a id="server-environment-repository-gcp-secret-manager-backend--_http_headers_config_client_to_config_server"></a>
<a id="server-environment-repository-gcp-secret-manager-backend--http-headers-config-client-to-config-server"></a>

## HTTP headers (Config Client to Config Server)

| Header | Required when | Purpose |
| --- | --- | --- |
| `X-Config-Token` | `token-mandatory` is `true` for the permission check | Bearer-style access token used only for Cloud Resource Manager `testIamPermissions`. |
| `X-Project-ID` | Recommended when not running on GCP with metadata | Google Cloud project ID for Secret Manager and IAM checks. |
| `X-Secret-Prefix` | Optional | Restricts which secrets contribute properties when matching by name prefix (see [Mapping applications and profiles](#server-environment-repository-gcp-secret-manager-backend--gcp-secret-manager-mapping)). |

Header names are case-insensitive per HTTP; the implementation uses `X-Config-Token`, `X-Project-ID`, and `X-Secret-Prefix`.

[AWS Secrets Manager Backend](#server-environment-repository-aws-secrets-manager-backend)
[CredHub Backend](#server-environment-repository-credhub-backend)

---

<a id="server-environment-repository-credhub-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/credhub-backend.html -->

<!-- page_index: 18 -->

# CredHub Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-credhub-backend--page-title"></a>
<a id="server-environment-repository-credhub-backend--credhub-backend"></a>

# CredHub Backend

Spring Cloud Config Server supports [CredHub](https://docs.cloudfoundry.org/credhub) as a backend for configuration properties.
You can enable this feature by adding a dependency to [Spring CredHub](https://spring.io/projects/spring-credhub).

pom.xml

```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.credhub</groupId>
		<artifactId>spring-credhub-starter</artifactId>
	</dependency>
</dependencies>
```

The following configuration uses mutual TLS to access a CredHub:

```yaml
spring:
  profiles:
    active: credhub
  cloud:
    config:
      server:
        credhub:
          url: https://credhub:8844
```

The properties should be stored as JSON, such as:

```sh
credhub set --name "/demo-app/default/master/toggles" --type=json
value: {"toggle.button": "blue", "toggle.link": "red"}
```

```sh
credhub set --name "/demo-app/default/master/abs" --type=json
value: {"marketing.enabled": true, "external.enabled": false}
```

All client applications with the name `spring.cloud.config.name=demo-app` will have the following properties available to them:

```
{
    toggle.button: "blue",
    toggle.link: "red",
    marketing.enabled: true,
    external.enabled: false
}
```

> [!NOTE]
> When no label is specified `master` will be used as a default value. You can change that by setting `spring.cloud.config.server.credhub.defaultLabel`.

> [!NOTE]
> When no profile is specified `default` will be used.

> [!NOTE]
> Values added to `application` will be shared by all the applications.

<a id="server-environment-repository-credhub-backend--oauth-2-0"></a>
<a id="server-environment-repository-credhub-backend--oauth-2.0"></a>

## OAuth 2.0

You can authenticate with [OAuth 2.0](https://oauth.net/2/) using [UAA](https://docs.cloudfoundry.org/concepts/architecture/uaa.html) as a provider.

pom.xml

```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.security</groupId>
		<artifactId>spring-security-config</artifactId>
	</dependency>
	<dependency>
		<groupId>org.springframework.security</groupId>
		<artifactId>spring-security-oauth2-client</artifactId>
	</dependency>
</dependencies>
```

The following configuration uses OAuth 2.0 and UAA to access a CredHub:

```yaml
spring:
  profiles:
    active: credhub
  cloud:
    config:
      server:
        credhub:
          url: https://credhub:8844
          oauth2:
            registration-id: credhub-client
  security:
    oauth2:
      client:
        registration:
          credhub-client:
            provider: uaa
            client-id: credhub_config_server
            client-secret: asecret
            authorization-grant-type: client_credentials
        provider:
          uaa:
            token-uri: https://uaa:8443/oauth/token
```

> [!NOTE]
> The used UAA client-id should have `credhub.read` as scope.

The following table describes the CredHub configuration properties.

| Property Name | Remarks |
| --- | --- |
| **url** | CredHub server URL. |
| **path** | Base path for all credentials. Optional, defaults to empty. |
| **defaultLabel** | Default label to use when is not provided by client application. Optional, defaults to `master`. |
| **oauth2** | OAuth2 configuration to access CredHub. Optional. |

[Google Secret Manager Backend](#server-environment-repository-gcp-secret-manager-backend)
[MongoDB Backend](#server-environment-repository-mongo-backend)

---

<a id="server-environment-repository-mongo-backend"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/mongo-backend.html -->

<!-- page_index: 19 -->

# MongoDB Backend

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-mongo-backend--page-title"></a>
<a id="server-environment-repository-mongo-backend--mongodb-backend"></a>

# MongoDB Backend

Spring Cloud Config Server supports MongoDB as a backend for configuration properties.
You can enable this feature by adding `spring-boot-starter-data-mongodb` to the classpath and using the `mongodb` profile.

pom.xml

```xml
<dependencies>
	<dependency>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-data-mongodb</artifactId>
	</dependency>
</dependencies>
```

Configure your application’s `application.properties` or `application.yml` to point to your MongoDB instance:

```yaml
spring:
  profiles:
    active: mongodb
  data:
    mongodb:
      database: your-database-name
      port: '27017'
      host: localhost
```

The configuration properties should be stored in documents within the `properties` collection. Each document represents a set of properties for a given application, profile, and label.

Example MongoDB document:

```json
{"application": "myapp","profile": "development","label": "master","properties": {"property1": "value1","property2": "value2"}}
```

You can disable autoconfiguration for `MongoDbEnvironmentRepository` by setting the `spring.cloud.config.server.mongodb.enabled` property to `false`.

The default values for MongoDB backend configuration are as follows:

- **Collection Name:** `"properties"` (Name of the MongoDB collection to query for configuration properties.)
- **Default Label:** `"master"` (Default label to use if none is specified.)

> [!NOTE]
> You can change these defaults by setting `spring.cloud.config.server.mongodb.collection` and `spring.cloud.config.server.mongodb.defaultLabel` in your application’s configuration.

[CredHub Backend](#server-environment-repository-credhub-backend)
[Composite Environment Repositories](#server-environment-repository-composite-repositories)

---

<a id="server-environment-repository-composite-repositories"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/composite-repositories.html -->

<!-- page_index: 20 -->

# Composite Environment Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-composite-repositories--page-title"></a>
<a id="server-environment-repository-composite-repositories--composite-environment-repositories"></a>

# Composite Environment Repositories

In some scenarios, you may wish to pull configuration data from multiple environment repositories.
To do so, you can enable the `composite` profile in your configuration server’s application properties or YAML file.
If, for example, you want to pull configuration data from a Subversion repository as well as two Git repositories, you can set the following properties for your configuration server:

```yaml
spring:
  profiles:
    active: composite
  cloud:
    config:
      server:
        composite:
        -
          type: svn
          uri: file:///path/to/svn/repo
        -
          type: git
          uri: file:///path/to/rex/git/repo
        -
          type: git
          uri: file:///path/to/walter/git/repo
```

Using this configuration, precedence is determined by the order in which repositories are listed under the `composite` key.
In the above example, the Subversion repository is listed first, so a value found in the Subversion repository will override values found for the same property in one of the Git repositories.
A value found in the `rex` Git repository will be used before a value found for the same property in the `walter` Git repository.

If you want to pull configuration data only from repositories that are each of distinct types, you can enable the corresponding profiles, rather than the `composite` profile, in your configuration server’s application properties or YAML file.
If, for example, you want to pull configuration data from a single Git repository and a single HashiCorp Vault server, you can set the following properties for your configuration server:

```yaml
spring:
  profiles:
    active: git, vault
  cloud:
    config:
      server:
        git:
          uri: file:///path/to/git/repo
          order: 2
        vault:
          host: 127.0.0.1
          port: 8200
          order: 1
```

Using this configuration, precedence can be determined by an `order` property.
You can use the `order` property to specify the priority order for all your repositories.
The lower the numerical value of the `order` property, the higher priority it has.
The priority order of a repository helps resolve any potential conflicts between repositories that contain values for the same properties.

> [!NOTE]
> If your composite environment includes a Vault server as in the previous example, you must include a Vault token in every request made to the configuration server. See [Vault Backend](#server-environment-repository-vault-backend).

> [!NOTE]
> Any type of failure when retrieving values from an environment repository results in a failure for the entire composite environment.
> If you would like the composite to continue even when a repository fails you can set `spring.cloud.config.server.failOnCompositeError` to `false`.

> [!NOTE]
> When using a composite environment, it is important that all repositories contain the same labels.
> If you have an environment similar to those in the preceding examples and you request configuration data with the `master` label but the Subversion repository does not contain a branch called `master`, the entire request fails.

<a id="server-environment-repository-composite-repositories--custom-composite-environment-repositories"></a>

## Custom Composite Environment Repositories

In addition to using one of the environment repositories from Spring Cloud, you can also provide your own `EnvironmentRepository` bean to be included as part of a composite environment.
To do so, your bean must implement the `EnvironmentRepository` interface.
If you want to control the priority of your custom `EnvironmentRepository` within the composite environment, you should also implement the `Ordered` interface and override the `getOrdered` method.
If you do not implement the `Ordered` interface, your `EnvironmentRepository` is given the lowest priority.

[MongoDB Backend](#server-environment-repository-mongo-backend)
[Custom Environment Repositories](#server-environment-repository-custom-enviroment-repository)

---

<a id="server-environment-repository-custom-enviroment-repository"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/custom-enviroment-repository.html -->

<!-- page_index: 21 -->

# Custom Environment Repositories

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-custom-enviroment-repository--page-title"></a>
<a id="server-environment-repository-custom-enviroment-repository--custom-environment-repositories"></a>

# Custom Environment Repositories

Spring Cloud Config supports enhancing its configuration management by allowing you to create and integrate custom EnvironmentRepository implementations. This enables the addition of unique configuration sources to your application. Implementing the Ordered interface and specifying the getOrder method also lets you set the priority of your custom repository within a composite configuration setup. Without this, custom repositories are considered with the lowest priority by default.

Below is an example of how to create and configure a custom `EnvironmentRepository`:

```java
public class CustomConfigurationRepository implements EnvironmentRepository, Ordered {
@Override public Environment findOne(String application, String profile, String label) {// Simulate fetching configuration from a custom source final Map<String, String> properties = Map.of("key1", "value1","key2", "value2","key3", "value3" ); Environment environment = new Environment(application, profile); environment.add(new PropertySource("customPropertySource", properties)); return environment;}
@Override public int getOrder() {return 0;}}
@Configuration @Profile("custom") public class AppConfig {@Bean public CustomConfigurationRepository customConfigurationRepository() {return new CustomConfigurationRepository();}}
```

With this setup, if you activate the `custom` profile within your Spring application’s configuration, your custom environment repository will be integrated into the configuration server. For instance, specifying the `custom` profile in your `application.properties` or `application.yml` as follows:

```yaml
spring:
  application:
    name: configserver
  profiles:
    active: custom
```

Now, accessing the configuration server at:

```
http://localhost:8080/any-client/dev/latest
```

will return default values from the custom repository, as shown below:

```json
{"name": "any-client","profiles": ["dev"],"label": "latest","propertySources": [{"name": "customPropertySource","source": {"key1": "value1","key2": "value2","key3": "value3"}}]}
```

[Composite Environment Repositories](#server-environment-repository-composite-repositories)
[Property Overrides](#server-environment-repository-property-overrides)

---

<a id="server-environment-repository-property-overrides"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/property-overrides.html -->

<!-- page_index: 22 -->

# Property Overrides

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-property-overrides--page-title"></a>
<a id="server-environment-repository-property-overrides--property-overrides"></a>

# Property Overrides

The Config Server has an “overrides” feature that lets the operator provide configuration properties to all applications.
The overridden properties cannot be accidentally changed by the application with the normal Spring Boot hooks.
To declare overrides, add a map of name-value pairs to `spring.cloud.config.server.overrides`, as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        overrides:
          foo: bar
```

The preceding examples causes all applications that are config clients to read `foo=bar`, independent of their own configuration.

> [!NOTE]
> A configuration system cannot force an application to use configuration data in any particular way.
> Consequently, overrides are not enforceable.
> However, they do provide useful default behavior for Spring Cloud Config clients.

> [!TIP]
> Normally, Spring environment placeholders with `${}` can be escaped (and resolved on the client) by using backslash (`\`) to escape the `$` or the `{`.
> For example, `\${app.foo:bar}` resolves to `bar`, unless the app provides its own `app.foo`.

> [!NOTE]
> In YAML, you do not need to escape the backslash itself.
> However, in properties files, you do need to escape the backslash, when you configure the overrides on the server.

You can change the priority of all overrides in the client to be more like default values, letting applications supply their own values in environment variables or System properties, by setting the `spring.cloud.config.overrideNone=true` flag (the default is false) in the remote repository.

[Custom Environment Repositories](#server-environment-repository-custom-enviroment-repository)
[Using Bootstrap To Override Properties](#server-environment-repository-using-bootstrap-to-override-properties)

---

<a id="server-environment-repository-using-bootstrap-to-override-properties"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/using-bootstrap-to-override-properties.html -->

<!-- page_index: 23 -->

# Using Bootstrap To Override Properties

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-using-bootstrap-to-override-properties--page-title"></a>
<a id="server-environment-repository-using-bootstrap-to-override-properties--using-bootstrap-to-override-properties"></a>

# Using Bootstrap To Override Properties

If you enable [config first bootstrap](#client--config-first-bootstrap), you can let client settings override configuration from the config server by placing two properties within
the application’s configuration that reside in the external environment repository (for example, Git, Vault, SVN, and others) used by the config server.

```properties
spring.cloud.config.allowOverride=true
spring.cloud.config.overrideNone=true
```

With Bootstrap enabled and these two properties set to true you will be able to override configuration from the config server
within the clients application configuration.

[Property Overrides](#server-environment-repository-property-overrides)
[Overriding Properties Using Placeholders](#server-environment-repository-overriding-properties-using-placeholders)

---

<a id="server-environment-repository-overriding-properties-using-placeholders"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/overriding-properties-using-placeholders.html -->

<!-- page_index: 24 -->

# Overriding Properties Using Placeholders

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-overriding-properties-using-placeholders--page-title"></a>
<a id="server-environment-repository-overriding-properties-using-placeholders--overriding-properties-using-placeholders"></a>

# Overriding Properties Using Placeholders

A cleaner way to override properties without enabling config first bootstrap is to use property placeholders in the configuration coming from the config server.

For example if the configuration coming from the config server contains the following property

```properties
hello=${app.hello:Hello From Config Server!}
```

You can override the value of `hello` coming from the config server by setting `app.hello` in your local application configuration

```properties
app.hello=Hello From Application!
```

[Using Bootstrap To Override Properties](#server-environment-repository-using-bootstrap-to-override-properties)
[Overriding Properties Using Profiles](#server-environment-repository-overriding-properties-using-profiles)

---

<a id="server-environment-repository-overriding-properties-using-profiles"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/environment-repository/overriding-properties-using-profiles.html -->

<!-- page_index: 25 -->

# Overriding Properties Using Profiles

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-environment-repository-overriding-properties-using-profiles--page-title"></a>
<a id="server-environment-repository-overriding-properties-using-profiles--overriding-properties-using-profiles"></a>

# Overriding Properties Using Profiles

The final way to override properties coming from the config server is to specify them in profile specific configuration file within the client
application.

For example, if you have the following configuration from the config server

```properties
hello="Hello From Config Server!"
```

You can override the value of `hello` in the client application by setting `hello` in a profile specific configuration file and
then enabling that profile.

application-overrides.properties

```properties
hello="Hello From Application!"
```

In the above example you would have to enable the `overrides` profile.

[Overriding Properties Using Placeholders](#server-environment-repository-overriding-properties-using-placeholders)
[Health Indicator](#server-health-indicator)

---

<a id="server-health-indicator"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/health-indicator.html -->

<!-- page_index: 26 -->

# Health Indicator

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-health-indicator--page-title"></a>
<a id="server-health-indicator--health-indicator"></a>

# Health Indicator

Config Server comes with a Health Indicator that checks whether the configured `EnvironmentRepository` is working.
By default, it asks the `EnvironmentRepository` for an application named `app`, the `default` profile, and the default label provided by the `EnvironmentRepository` implementation.

You can configure the Health Indicator to check more applications along with custom profiles and custom labels, as shown in the following example:

```yaml
spring:
  cloud:
    config:
      server:
        health:
          repositories:
            myservice:
              label: mylabel
            myservice-dev:
              name: myservice
              profiles: development
```

You can disable the Health Indicator by setting `spring.cloud.config.server.health.enabled=false`.

Also, you can provide a custom `down` status of your own by setting property `spring.cloud.config.server.health.down-health-status` (valued to `"DOWN'` by default).

> [!NOTE]
> If `spring.cloud.config.server.accept-empty` is `false` and the health indicator check
> does not return any repository data the health indicator will return `down` status.
> You can override this by setting `spring.cloud.config.server.health.accept-empty=true`.

[Overriding Properties Using Profiles](#server-environment-repository-overriding-properties-using-profiles)
[Security](#server-security)

---

<a id="server-security"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/security.html -->

<!-- page_index: 27 -->

# Security

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-security--page-title"></a>
<a id="server-security--security"></a>

# Security

You can secure your Config Server in any way that makes sense to you (from physical network security to OAuth2 bearer tokens), because Spring Security and Spring Boot offer support for many security arrangements.

To use the default Spring Boot-configured HTTP Basic security, include Spring Security on the classpath (for example, through `spring-boot-starter-security`).
The default is a username of `user` and a randomly generated password. A random password is not useful in practice, so we recommend you configure the password (by setting `spring.security.user.password`) and encrypt it (see below for instructions on how to do that).

[Health Indicator](#server-health-indicator)
[Actuator and Security](#server-actuator-and-security)

---

<a id="server-actuator-and-security"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/actuator-and-security.html -->

<!-- page_index: 28 -->

# Actuator and Security

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-actuator-and-security--page-title"></a>
<a id="server-actuator-and-security--actuator-and-security"></a>

# Actuator and Security

> [!IMPORTANT]
> Some platforms configure health checks or something similar and point to `/actuator/health` or other actuator endpoints. If actuator is not a dependency of config server, requests to `/actuator/` would match the config server API `/{application}/{label}` possibly leaking secure information. Remember to add the `spring-boot-starter-actuator` dependency in this case and configure the users such that the user that makes calls to `/actuator/` does not have access to the config server API at `/{application}/{label}`.

[Security](#server-security)
[Encryption and Decryption](#server-encryption-and-decryption)

---

<a id="server-encryption-and-decryption"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/encryption-and-decryption.html -->

<!-- page_index: 29 -->

# Encryption and Decryption

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-encryption-and-decryption--page-title"></a>
<a id="server-encryption-and-decryption--encryption-and-decryption"></a>

# Encryption and Decryption

> [!IMPORTANT]
> To use the encryption and decryption features you need the full-strength JCE installed in your JVM (it is not included by default).
> You can download the “Java Cryptography Extension (JCE) Unlimited Strength Jurisdiction Policy Files” from Oracle and follow the installation instructions (essentially, you need to replace the two policy files in the JRE lib/security directory with the ones that you downloaded). This is only applicable for old versions of Java. Starting from Java 9, and definitively from Java 8u161 onwards, unlimited strength cryptography is enabled by default

If the remote property sources contain encrypted content (values starting with `{cipher}`), they are decrypted before sending to clients over HTTP.
The main advantage of this setup is that the property values need not be in plain text when they are “at rest” (for example, in a git repository).
If a value cannot be decrypted, it is removed from the property source and an additional property is added with the same key but prefixed with `invalid` and a value that means “not applicable” (usually `<n/a>`).
This is largely to prevent cipher text being used as a password and accidentally leaking.

If you set up a remote config repository for config client applications, it might contain an `application.yml` similar to the following:

application.yml

```yaml
spring:
  datasource:
    username: dbuser
    password: '{cipher}FKSAJDFGYOS8F7GLHAKERGFHLSAJ'
```

Encrypted values in `application.properties` file must not be wrapped in quotes. Otherwise, the value is not decrypted. The following example shows values that would work:

application.properties

```
spring.datasource.username: dbuser
spring.datasource.password: {cipher}FKSAJDFGYOS8F7GLHAKERGFHLSAJ
```

You can safely push this plain text to a shared git repository, and the secret password remains protected.

The server also exposes `/encrypt` and `/decrypt` endpoints (on the assumption that these are secured and only accessed by authorized agents).
If you edit a remote config file, you can use the Config Server to encrypt values by POSTing to the `/encrypt` endpoint, as shown in the following example:

```
$ curl localhost:8888/encrypt -s -d mysecret 682bc583f4641835fa2db009355293665d2647dade3375c0ee201de2a49f7bda
```

> [!TIP]
> If you are testing with curl, then use `--data-urlencode` (instead of `-d`) and prefix the value to encrypt with `=` (curl requires this) or set an explicit `Content-Type: text/plain` to make sure curl encodes the data correctly when there are special characters ('+' is particularly tricky).

> [!TIP]
> Be sure not to include any of the curl command statistics in the encrypted value, this is why the examples use the `-s` option to silence them. Outputting the value to a file can help avoid this problem.

The inverse operation is also available through `/decrypt` (provided the server is
configured with a symmetric key or a full key pair), as shown in the following example:

```
$ curl localhost:8888/decrypt -s -d 682bc583f4641835fa2db009355293665d2647dade3375c0ee201de2a49f7bda mysecret
```

Take the encrypted value and add the `{cipher}` prefix before you put it in the YAML or properties file and before you commit and push it to a remote (potentially insecure) store.

The `/encrypt` and `/decrypt` endpoints also both accept paths in the form of `/*/{application}/{profiles}`, which can be used to control cryptography on a per-application (name) and per-profile basis when clients call into the main environment resource.

> [!NOTE]
> To control the cryptography in this granular way, you must also provide a `@Bean` of type `TextEncryptorLocator` that creates a different encryptor per name and profiles.
> The one that is provided by default does not do so (all encryptions use the same key).

The `spring` command line client (with Spring Cloud CLI extensions
installed) can also be used to encrypt and decrypt, as shown in the following example:

```
$ spring encrypt mysecret --key foo 682bc583f4641835fa2db009355293665d2647dade3375c0ee201de2a49f7bda
$ spring decrypt --key foo 682bc583f4641835fa2db009355293665d2647dade3375c0ee201de2a49f7bda mysecret
```

To use a key in a file (such as an RSA public key for encryption), prepend
the key value with "@" and provide the file path, as shown in the following example:

```
$ spring encrypt mysecret --key @${HOME}/.ssh/id_rsa.pub AQAjPgt3eFZQXwt8tsHAVv/QHiY5sI2dRcR+...
```

> [!NOTE]
> The `--key` argument is mandatory (despite having a `--` prefix).

<a id="server-encryption-and-decryption--_decryption_errors"></a>
<a id="server-encryption-and-decryption--decryption-errors"></a>

## Decryption Errors

When the config server fails to decrypt a value it will create an `invalid` property in the HTTP response.

For example

```json
{"label": null,"name": "application","profiles": ["prd" ],"propertySources": [{"name": "file:/demo/configserver/application-prd.yaml","source": {"invalid.SharedPassword": "<n/a>"} },{"name": "file:/demo/configserver/application.yaml","source": {"SharedPassword": "Fill_me_in"}} ],"state": null,"version": null}
```

In the example above the config server could not decrypt the value of `SharedPassword` in `application-prd.yaml`
so the config server prefixed the property name with `invalid`.

If this response was received by the Config Client and then added to the app’s `Environment` and the client
requested the value of `SharedPassword` it would get `Fill_me_in`.

If you do not want the config server to prefix properties it can’t decrypt wit `invalid` then you can set
`spring.cloud.config.server.encrypt.prefix-invalid-properties` to `false`. If you do this then the same response from
the config server would look like this:

```json
"label": null,"name": "application","profiles": ["prd" ],"propertySources": [{"name": "file:/demo/configserver/application-prd.yaml","source": {"SharedPassword": "AYBKlpcZpaR36OcRDQjNIQl6fmnddAQhetMw/uyTpnn5fDj+unJ9QOEbqiPc9fX0N+CC8i+EJiN6nlH9Xqu6sH1tX/P6zg1CIy+ct/1RWGNbmQ256jc6vQaXhiN8sA8Mr6QiqYnMoBd+Jni/Miir5G3a7G9MmjbEUASKJOhUlIFKqL1IqB81RBT/cv0bg9kAiy5VBF1WppxP/PwtjECzbeUi2Y1jbpYb98rnc/qmRO3ZJam9fDNcPpW09qGFhGgJIujca257F7G4guS2w/7haVzNoyRiwHzZ14oL8AIxHLMBSJJF19ULlsMAkROj9o9TnwhL9r4rX9sAWk28c5eq77+iVpmlT3yoRdZqvMqffzKiibDlzz95Gmms7V7mctxrhNVOOWTwMSJvk94Y9ZPenljKgPJIV3Z1cqqx+W8JxFFeelOuYvMEe4bOVBh1TepGzzdWVdYbylgXJy35uRTZ2drybUe5+jc0hiAuujHz0zdY1FwOHfwzSsSidlYn4syPeuytnxTzn7fbWXeXetTTtDlmLRf8MBSzXzDFWNH0cNGOCQ=="} },{"name": "file:/demo/configserver/application.yaml","source": {"SharedPassword": "Fill_me_in"}} ],"state": null,"version": null}
```

In this case if the config client were to receive the above response and requested that value
of `SharedPassword` from the `Environment` it would get the encrypted value back instead of
`Fill_me_in`.

[Actuator and Security](#server-actuator-and-security)
[Key Management](#server-key-management)

---

<a id="server-key-management"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/key-management.html -->

<!-- page_index: 30 -->

# Key Management

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-key-management--page-title"></a>
<a id="server-key-management--key-management"></a>

# Key Management

The Config Server can use a symmetric (shared) key or an asymmetric one (RSA key pair).
The asymmetric choice is superior in terms of security, but it is often more convenient to use a symmetric key since it is a single property value to configure in the `application.properties`.

To configure a symmetric key, you need to set `encrypt.key` to a secret String (or use the `ENCRYPT_KEY` environment variable to keep it out of plain-text configuration files).

> [!NOTE]
> If you include `spring-cloud-starter-bootstrap` on the classpath or set `spring.cloud.bootstrap.enabled=true` as a system property, you will need to set `encrypt.key` in `bootstrap.properties`.

> [!NOTE]
> You cannot configure an asymmetric key using `encrypt.key`.

To configure an asymmetric key use a keystore (e.g. as
created by the `keytool` utility that comes with the JDK). The
keystore properties are `encrypt.keyStore.*` with `*` equal to

| Property | Description |
| --- | --- |
| `encrypt.keyStore.location` | Contains a `Resource` location |
| `encrypt.keyStore.password` | Holds the password that unlocks the keystore |
| `encrypt.keyStore.alias` | Identifies which key in the store to use |
| `encrypt.keyStore.type` | The type of KeyStore to create. Defaults to `jks`. |

The encryption is done with the public key, and a private key is
needed for decryption.
Thus, in principle, you can configure only the public key in the server if you want to only encrypt (and are prepared to decrypt the values yourself locally with the private key).
In practice, you might not want to do decrypt locally, because it spreads the key management process around all the clients, instead of
concentrating it in the server.
On the other hand, it can be a useful option if your config server is relatively insecure and only a handful of clients need the encrypted properties.

[Encryption and Decryption](#server-encryption-and-decryption)
[Creating a Key Store for Testing](#server-creating-a-key-store-for-testing)

---

<a id="server-creating-a-key-store-for-testing"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/creating-a-key-store-for-testing.html -->

<!-- page_index: 31 -->

# Creating a Key Store for Testing

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-creating-a-key-store-for-testing--page-title"></a>
<a id="server-creating-a-key-store-for-testing--creating-a-key-store-for-testing"></a>

# Creating a Key Store for Testing

To create a keystore for testing, you can use a command resembling the following:

```
$ keytool -genkeypair -alias mytestkey -keyalg RSA \ -dname "CN=Web Server,OU=Unit,O=Organization,L=City,S=State,C=US" \ -keypass changeme -keystore server.jks -storepass letmein
```

> [!NOTE]
> When using JDK 11 or above you may get the following warning when using the command above. In this case
> you probably want to make sure the `keypass` and `storepass` values match.

> [!WARNING]
> Different store and key passwords not supported for PKCS12 KeyStores. Ignoring user-specified -keypass value.

Put the `server.jks` file in the classpath (for instance) and then, in
your `bootstrap.yml`, for the Config Server, create the following settings:

```yaml
encrypt:
  keyStore:
    location: classpath:/server.jks
    password: letmein
    alias: mytestkey
    secret: changeme
```

[Key Management](#server-key-management)
[Using Multiple Keys and Key Rotation](#server-using-multiple-keys-and-key-rotation)

---

<a id="server-using-multiple-keys-and-key-rotation"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/using-multiple-keys-and-key-rotation.html -->

<!-- page_index: 32 -->

# Using Multiple Keys and Key Rotation

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-using-multiple-keys-and-key-rotation--page-title"></a>
<a id="server-using-multiple-keys-and-key-rotation--using-multiple-keys-and-key-rotation"></a>

# Using Multiple Keys and Key Rotation

In addition to the `{cipher}` prefix in encrypted property values, the Config Server looks for zero or more `{name:value}` prefixes before the start of the (Base64 encoded) cipher text.
The keys are passed to a `TextEncryptorLocator`, which can do whatever logic it needs to locate a `TextEncryptor` for the cipher.
If you have configured a keystore (`encrypt.keystore.location`), the default locator looks for keys with aliases supplied by the `key` prefix, with a cipher text like resembling the following:

```yaml
foo:
  bar: `\{cipher}{key:testkey}...`
```

The locator looks for a key named "testkey".
A secret can also be supplied by using a `{secret:…}` value in the prefix.
However, if it is not supplied, the default is to use the keystore password (which is what you get when you build a keystore and do not specify a secret).
If you do supply a secret, you should also encrypt the secret using a custom `SecretLocator`.

When the keys are being used only to encrypt a few bytes of configuration data (that is, they are not being used elsewhere), key rotation is hardly ever necessary on cryptographic grounds.
However, you might occasionally need to change the keys (for example, in the event of a security breach).
In that case, all the clients would need to change their source config files (for example, in git) and use a new `{key:…}` prefix in all the ciphers.
Note that the clients need to first check that the key alias is available in the Config Server keystore.

> [!TIP]
> If you want to let the Config Server handle all encryption as well as decryption, the `{name:value}` prefixes can also be added as plain text posted to the `/encrypt` endpoint.

[Creating a Key Store for Testing](#server-creating-a-key-store-for-testing)
[Serving Encrypted Properties](#server-serving-encrypted-properties)

---

<a id="server-serving-encrypted-properties"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/serving-encrypted-properties.html -->

<!-- page_index: 33 -->

# Serving Encrypted Properties

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-serving-encrypted-properties--page-title"></a>
<a id="server-serving-encrypted-properties--serving-encrypted-properties"></a>

# Serving Encrypted Properties

Sometimes you want the clients to decrypt the configuration locally, instead of doing it in the server.
In that case, if you provide the `encrypt.*` configuration to locate a key, you can still have `/encrypt` and `/decrypt` endpoints, but you need to explicitly switch off the decryption of outgoing properties by placing `spring.cloud.config.server.encrypt.enabled=false` in `bootstrap.[yml|properties]`.
If you do not care about the endpoints, it should work if you do not configure either the key or the enabled flag.

[Using Multiple Keys and Key Rotation](#server-using-multiple-keys-and-key-rotation)
[Serving Alternative Formats](#server-serving-alternative-formats)

---

<a id="server-serving-alternative-formats"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/serving-alternative-formats.html -->

<!-- page_index: 34 -->

# Serving Alternative Formats

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-serving-alternative-formats--page-title"></a>
<a id="server-serving-alternative-formats--serving-alternative-formats"></a>

# Serving Alternative Formats

The default JSON format from the environment endpoints is perfect for consumption by Spring applications, because it maps directly onto the `Environment` abstraction.
If you prefer, you can consume the same data as YAML or Java properties by adding a suffix (".yml", ".yaml" or ".properties") to the resource path.
This can be useful for consumption by applications that do not care about the structure of the JSON endpoints or the extra metadata they provide (for example, an application that is not using Spring might benefit from the simplicity of this approach).

The YAML and properties representations have an additional flag (provided as a boolean query parameter called `resolvePlaceholders`) to signal that placeholders in the source documents (in the standard Spring `${…}` form) should be resolved in the output before rendering, where possible.
This is a useful feature for consumers that do not know about the Spring placeholder conventions.

> [!NOTE]
> There are limitations in using the YAML or properties formats, mainly in relation to the loss of metadata.
> For example, the JSON is structured as an ordered list of property sources, with names that correlate with the source.
> The YAML and properties forms are coalesced into a single map, even if the origin of the values has multiple sources, and the names of the original source files are lost.
> Also, the YAML representation is not necessarily a faithful representation of the YAML source in a backing repository either. It is constructed from a list of flat property sources, and assumptions have to be made about the form of the keys.

[Serving Encrypted Properties](#server-serving-encrypted-properties)
[Serving Plain Text](#server-serving-plain-text)

---

<a id="server-serving-plain-text"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/serving-plain-text.html -->

<!-- page_index: 35 -->

# Serving Plain Text

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-serving-plain-text--page-title"></a>
<a id="server-serving-plain-text--serving-plain-text"></a>

# Serving Plain Text

Instead of using the `Environment` abstraction (or one of the alternative representations of it in YAML or properties format), your applications might need generic plain-text configuration files that are tailored to their environment.
The Config Server provides these through an additional endpoint at `/{application}/{profile}/{label}/{path}`, where `application`, `profile`, and `label` have the same meaning as the regular environment endpoint, but `path` is a path to a file name (such as `log.xml`).
The source files for this endpoint are located in the same way as for the environment endpoints.
The same search path is used for properties and YAML files.
However, instead of aggregating all matching resources, only the first one to match is returned.

After a resource is located, placeholders in the normal format (`${…}`) are resolved by using the effective `Environment` for the supplied application name, profile, and label.
In this way, the resource endpoint is tightly integrated with the environment endpoints.

> [!NOTE]
> As with the source files for environment configuration, the `profile` is used to resolve the file name.
> So, if you want a profile-specific file, `/*/development/*/logback.xml` can be resolved by a file called `logback-development.xml` (in preference to `logback.xml`).

> [!NOTE]
> If you do not want to supply the `label` and let the server use the default label, you can supply a `useDefaultLabel` request parameter.
> Consequently, the preceding example for the `default` profile could be `/sample/default/nginx.conf?useDefaultLabel`.

At present, Spring Cloud Config can serve plaintext for git, SVN, native backends, and AWS S3.
The support for git, SVN, and native backends is identical. AWS S3 works a bit differently.
The following sections show how each one works:

- [Git, SVN, and Native Backends](#server-serving-binary-files--spring-cloud-config-serving-plain-text-git-svn-native-backends)
- [AWS S3](#server-serving-binary-files--spring-cloud-config-serving-plain-text-aws-s3)

[Serving Alternative Formats](#server-serving-alternative-formats)
[Serving Binary Files](#server-serving-binary-files)

---

<a id="server-serving-binary-files"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/serving-binary-files.html -->

<!-- page_index: 36 -->

# Serving Binary Files

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-serving-binary-files--page-title"></a>
<a id="server-serving-binary-files--serving-binary-files"></a>

# Serving Binary Files

In order to serve binary files from the config server you will need to send an `Accept` header of `application/octet-stream`.

<a id="server-serving-binary-files--spring-cloud-config-serving-plain-text-git-svn-native-backends"></a>
<a id="server-serving-binary-files--git-svn-and-native-backends"></a>

## Git, SVN, and Native Backends

Consider the following example for a GIT or SVN repository or a native backend:

```none
application.yml
nginx.conf
```

The `nginx.conf` might resemble the following listing:

```none
server {
    listen              80;
    server_name         ${nginx.server.name};
}
```

`application.yml` might resemble the following listing:

```yaml
nginx:
  server:
    name: example.com
---
spring:
  profiles: development
nginx:
  server:
    name: develop.com
```

The `/sample/default/master/nginx.conf` resource might be as follows:

```none
server {
    listen              80;
    server_name         example.com;
}
```

`/sample/development/master/nginx.conf` might be as follows:

```none
server {
    listen              80;
    server_name         develop.com;
}
```

<a id="server-serving-binary-files--spring-cloud-config-serving-plain-text-aws-s3"></a>
<a id="server-serving-binary-files--aws-s3"></a>

## AWS S3

To enable serving plain text for AWS s3, the Config Server application needs to include a dependency on `io.awspring.cloud:spring-cloud-aws-context`.
For details on how to set up that dependency, see the
[Spring Cloud AWS Reference Guide](https://docs.awspring.io/spring-cloud-aws/docs/2.4.3/reference/html/index.html#spring-cloud-aws-maven-dependency-management).
In addition, when using Spring Cloud AWS with Spring Boot it is useful to include the [auto-configuration dependency](https://docs.awspring.io/spring-cloud-aws/docs/2.4.3/reference/html/index.html#spring-boot-auto-configuration).
Then you need to configure Spring Cloud AWS, as described in the
[Spring Cloud AWS Reference Guide](https://docs.awspring.io/spring-cloud-aws/docs/2.4.3/reference/html/index.html#configuring-credentials).

<a id="server-serving-binary-files--decrypting-plain-text"></a>

## Decrypting Plain Text

By default, encrypted values in plain text files are not decrypted. In order to enable decryption for plain text files, set `spring.cloud.config.server.encrypt.enabled=true` and `spring.cloud.config.server.encrypt.plainTextEncrypt=true` in `bootstrap.[yml|properties]`

> [!NOTE]
> Decrypting plain text files is only supported for YAML, JSON, and properties file extensions.

If this feature is enabled, and an unsupported file extention is requested, any encrypted values in the file will not be decrypted.

[Serving Plain Text](#server-serving-plain-text)
[Embedding the Config Server](#server-embedding)

---

<a id="server-embedding"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/embedding.html -->

<!-- page_index: 37 -->

# Embedding the Config Server

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-embedding--page-title"></a>
<a id="server-embedding--embedding-the-config-server"></a>

# Embedding the Config Server

The Config Server runs best as a standalone application.
However, if need be, you can embed it in another application.
To do so, use the `@EnableConfigServer` annotation.
An optional property named `spring.cloud.config.server.bootstrap` can be useful in this case.
It is a flag to indicate whether the server should configure itself from its own remote repository.
By default, the flag is off, because it can delay startup.
However, when embedded in another application, it makes sense to initialize the same way as any other application.
When setting `spring.cloud.config.server.bootstrap` to `true` you must also use a [composite environment repository configuration](#server-environment-repository-composite-repositories).
For example

```yaml
spring:
  application:
    name: configserver
  profiles:
    active: composite
  cloud:
    config:
      server:
        composite:
          - type: native
            search-locations: ${HOME}/Desktop/config
        bootstrap: true
```

> [!NOTE]
> If you use the bootstrap flag, the config server needs to have its name and repository URI configured in `bootstrap.yml`.

To change the location of the server endpoints, you can (optionally) set `spring.cloud.config.server.prefix` (for example, `/config`), to serve the resources under a prefix.
The prefix should start but not end with a `/`.
It is applied to the `@RequestMappings` in the Config Server (that is, underneath the Spring Boot `server.servletPath` and `server.contextPath` prefixes).

If you want to read the configuration for an application directly from the backend repository (instead of from the config server), you
basically want an embedded config server with no endpoints.
You can switch off the endpoints entirely by not using the `@EnableConfigServer` annotation (set `spring.cloud.config.server.bootstrap=true`).

[Serving Binary Files](#server-serving-binary-files)
[Push Notifications and Spring Cloud Bus](#server-push-notifications-and-bus)

---

<a id="server-push-notifications-and-bus"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/push-notifications-and-bus.html -->

<!-- page_index: 38 -->

# Push Notifications and Spring Cloud Bus

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-push-notifications-and-bus--page-title"></a>
<a id="server-push-notifications-and-bus--push-notifications-and-spring-cloud-bus"></a>

# Push Notifications and Spring Cloud Bus

Many source code repository providers (such as Github, Gitlab, Gitea, Gitee, Gogs, or Bitbucket) notify you of changes in a repository through a webhook.
You can configure the webhook through the provider’s user interface as a URL and a set of events in which you are interested.
For instance, [Github](https://developer.github.com/v3/activity/events/types/#pushevent) uses a POST to the webhook with a JSON body containing a list of commits and a header (`X-Github-Event`) set to `push`.
If you add a dependency on the `spring-cloud-config-monitor` library and activate the Spring Cloud Bus in your Config Server, then a `/monitor` endpoint is enabled.

When the webhook is activated, the Config Server sends a `RefreshRemoteApplicationEvent` targeted at the applications it thinks might have changed.
The change detection can be strategized.
However, by default, it looks for changes in files that match the application name (for example, `foo.properties` is targeted at the `foo` application, while `application.properties` is targeted at all applications).
The strategy to use when you want to override the behavior is `PropertyPathNotificationExtractor`, which accepts the request headers and body as parameters and returns a list of file paths that changed.

The default configuration works out of the box with Github, Gitlab, Gitea, Gitee, Gogs or Bitbucket.
In addition to the JSON notifications from Github, Gitlab, Gitee, or Bitbucket, you can trigger a change notification by POSTing to `/monitor` with form-encoded body parameters in the pattern of `path={application}`.
Doing so broadcasts to applications matching the `{application}` pattern (which can contain wildcards).

> [!NOTE]
> The `RefreshRemoteApplicationEvent` is transmitted only if the `spring-cloud-bus` is activated in both the Config Server and in the client application.

> [!NOTE]
> The default configuration also detects filesystem changes in local git repositories. In that case, the webhook is not used. However, as soon as you edit a config file, a refresh is broadcast.

[Embedding the Config Server](#server-embedding)
[AOT and Native Image Support](#server-aot-and-native-image-support)

---

<a id="server-aot-and-native-image-support"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/server/aot-and-native-image-support.html -->

<!-- page_index: 39 -->

# AOT and Native Image Support

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="server-aot-and-native-image-support--page-title"></a>
<a id="server-aot-and-native-image-support--aot-and-native-image-support"></a>

# AOT and Native Image Support

Since `4.0.0`, Spring Cloud Config Server supports Spring AOT transformations. As of `4.1.0` it also supports GraalVM native images, as long as GraalVM 21 or higher is used, however it requires the user to add some workarounds for known GraalVM issues, as described below.

> [!IMPORTANT]
> Due to [a bug](https://github.com/oracle/graal/issues/5134) in Graal’s `FileSystemProvider` a configuration workaround needs to be added to allow the Config Server to run as a native image. You will need to add the following options to your GraalVM build plugin setup (please refer to [Maven plugin for GraalVM](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html) or [Gradle plugin for GraalVM](https://graalvm.github.io/native-build-tools/latest/gradle-plugin.html) for more details):
>
> ```none
> -H:-AddAllFileSystemProviders
> --strict-image-heap
> --initialize-at-build-time=org.bouncycastle
> --initialize-at-build-time=net.i2p.crypto.eddsa.EdDSASecurityProvider
> --initialize-at-run-time=org.bouncycastle.jcajce.provider.drbg.DRBG$Default
> --initialize-at-run-time=org.bouncycastle.jcajce.provider.drbg.DRBG$NonceAndIV
> ```

> [!NOTE]
> Adding the additional build time initializations can affect performance, but it still may offer gains as compared to a regular JVM run. Make sure to measure and compare for your application.

> [!TIP]
> If you are connecting with your config data backend over SSH, keep in mind that GraalVM requires [security provider registration using `java.security`](https://www.graalvm.org/latest/reference-manual/native-image/dynamic-features/JCASecurityServices/#provider-registration)

> [!WARNING]
> Refresh scope is not supported with native images. If you are going to run your config client application as a native image, make sure to set `spring.cloud.refresh.enabled` property to `false`.

[Push Notifications and Spring Cloud Bus](#server-push-notifications-and-bus)
[Spring Cloud Config Client](#client)

---

<a id="client"></a>

<!-- source_url: https://docs.spring.io/spring-cloud-config/reference/client.html -->

<!-- page_index: 40 -->

# Spring Cloud Config Client

<svg enable-background="new 0 0 32 32" id="Glyph" version="1.1" viewbox="0 0 32 32" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
<path id="XMLID_223_"></path>
</svg>

Search

<a id="client--page-title"></a>
<a id="client--spring-cloud-config-client"></a>

# Spring Cloud Config Client

A Spring Boot application can take immediate advantage of the Spring Config Server (or other external property sources provided by the application developer).
It also picks up some additional useful features related to `Environment` change events.

<a id="client--config-data-import"></a>
<a id="client--spring-boot-config-data-import"></a>

## Spring Boot Config Data Import

Spring Boot 2.4 introduced a new way to import configuration data via the `spring.config.import` property. This is now the default way to bind to Config Server.

To optionally connect to config server set the following in application.properties:

application.properties

```properties
spring.config.import=optional:configserver:
```

This will connect to the Config Server at the default location of "http://localhost:8888". Removing the `optional:` prefix will cause the Config Client to fail if it is unable to connect to Config Server. To change the location of Config Server either set `spring.cloud.config.uri` or add the url to the `spring.config.import` statement such as, `spring.config.import=optional:configserver:http://myhost:8888`. The location in the import property has precedence over the uri property.

Spring Boot Config Data resolves configuration in a two step process. First it loads all configuration using the `default`
profile. This allows Spring Boot to gather all configuration which may activate any additional profiles.
After it has gathered all activated profiles it will load any additional configuration for the active profiles.
Due to this you may see multiple requests being made to the Spring Cloud Config Server to fetch configuration. This
is normal and is a side effect of how Spring Boot loads configuration when using `spring.config.import`. In previous
versions of Spring Cloud Config there was only a single request made but this meant you could not activate profiles
from configuration coming from the Config Server. The additional request with just the `default` profile now makes
this possible.

> [!NOTE]
> A `bootstrap` file (properties or yaml) is **not** needed for the Spring Boot Config Data method of import via `spring.config.import`.

<a id="client--config-first-bootstrap"></a>

## Config First Bootstrap

To use the legacy bootstrap way of connecting to Config Server, bootstrap must be enabled via a property or the `spring-cloud-starter-bootstrap` starter. The property is `spring.cloud.bootstrap.enabled=true`. It must be set as a System Property or environment variable.
Once bootstrap has been enabled any application with Spring Cloud Config Client on the classpath will connect to Config Server as follows:
When a config client starts, it binds to the Config Server (through the `spring.cloud.config.uri` bootstrap configuration property) and initializes Spring `Environment` with remote property sources.

The net result of this behavior is that all client applications that want to consume the Config Server need a `bootstrap.yml` (or an environment variable) with the server address set in `spring.cloud.config.uri` (it defaults to "http://localhost:8888").

<a id="client--discovery-first-bootstrap"></a>
<a id="client--discovery-first-lookup"></a>

### Discovery First Lookup

> [!WARNING]
> Unless you are using [config first bootstrap](#client--config-first-bootstrap), you will need to have a `spring.config.import` property in your configuration properties with an `optional:` prefix.
> For example, `spring.config.import=optional:configserver:`.

If you use a `DiscoveryClient` implementation, such as Spring Cloud Netflix and Eureka Service Discovery or Spring Cloud Consul, you can have the Config Server register with the Discovery Service.

If you prefer to use `DiscoveryClient` to locate the Config Server, you can do so by setting `spring.cloud.config.discovery.enabled=true` (the default is `false`).
For example, with Spring Cloud Netflix, you need to define the Eureka server address (for example, in `eureka.client.serviceUrl.defaultZone`).
The price for using this option is an extra network round trip on startup, to locate the service registration.
The benefit is that, as long as the Discovery Service is a fixed point, the Config Server can change its coordinates.
The default service ID is `configserver`, but you can change that on the client by setting `spring.cloud.config.discovery.serviceId` (and on the server, in the usual way for a service, such as by setting `spring.application.name`).

The discovery client implementations all support some kind of metadata map (for example, we have `eureka.instance.metadataMap` for Eureka).
Some additional properties of the Config Server may need to be configured in its service registration metadata so that clients can connect correctly.
If the Config Server is secured with HTTP Basic, you can configure the credentials as `user` and `password`.
Also, if the Config Server has a context path, you can set `configPath`.
For example, the following YAML file is for a Config Server that is a Eureka client:

```yaml
eureka:
  instance:
    ...
    metadataMap:
      user: osufhalskjrtl
      password: lviuhlszvaorhvlo5847
      configPath: /config
```

<a id="client--discovery-first-bootstrap-using-eureka-and-webclient"></a>

### Discovery First Bootstrap Using Eureka And WebClient

If you use the Eureka `DiscoveryClient` from Spring Cloud Netflix and also want to use `WebClient` instead of Jersey or `RestTemplate`, you need to include `WebClient` on your classpath as well as set `eureka.client.webclient.enabled=true`.

<a id="client--config-client-fail-fast"></a>

## Config Client Fail Fast

In some cases, you may want to fail startup of a service if it cannot connect to the Config Server.
If this is the desired behavior, set the bootstrap configuration property `spring.cloud.config.fail-fast=true` to make the client halt with an Exception.

> [!NOTE]
> To get similar functionality using `spring.config.import`, simply omit the `optional:` prefix.

<a id="client--config-client-retry"></a>

## Config Client Retry

If you expect that the config server may occasionally be unavailable when your application starts, you can make it keep trying after a failure.
First, you need to set `spring.cloud.config.fail-fast=true`.
Then you need to add `spring-retry` and `spring-boot-starter-aop` to your classpath.
The default behavior is to retry six times with an initial backoff interval of 1000ms and an exponential multiplier of 1.1 for subsequent backoffs.
You can configure these properties (and others) by setting the `spring.cloud.config.retry.*` configuration properties.
To use a random exponential backoff policy set `spring.cloud.config.retry.useRandomPolicy` to `true`.

> [!NOTE]
> When `spring.cloud.config.retry.useRandomPolicy` is `true` the `max-attempts`, `initial-interval`, `max-interval`, and `multiplier` properties will
> still have an effect even when using a random exponential backoff policy. The details on how they are used can be found in the
> `ExponentialRandomBackOffPolicy` and `ExponentialBackOffPolicy` in [Spring Retry](https://github.com/spring-projects/spring-retry).

> [!TIP]
> To take full control of the retry behavior and are using legacy bootstrap, add a `@Bean` of type `RetryOperationsInterceptor` with an ID of `configServerRetryInterceptor`.
> Spring Retry has a `RetryInterceptorBuilder` that supports creating one.

<a id="client--config-client-retry-with-spring-config-import"></a>
<a id="client--config-client-retry-with-spring.config.import"></a>

## Config Client Retry with spring.config.import

Retry works with the Spring Boot `spring.config.import` statement and the normal properties work. However, if the import statement is in a profile, such as `application-prod.properties`, then you need a different way to configure retry. Configuration needs to be placed as url parameters on the import statement.

application-prod.properties

```properties
spring.config.import=configserver:http://configserver.example.com?fail-fast=true&max-attempts=10&max-interval=1500&multiplier=1.2&initial-interval=1100"
```

This sets `spring.cloud.config.fail-fast=true` (notice the missing prefix above) and all the available `spring.cloud.config.retry.*` configuration properties.

<a id="client--locating-remote-configuration-resources"></a>

## Locating Remote Configuration Resources

The Config Service serves property sources from `/{application}/{profile}/{label}`, where the default bindings in the client app are as follows:

- "application" = `${spring.application.name}`
- "profile" = `${spring.profiles.active}` (actually `Environment.getActiveProfiles()`)
- "label" = "master"

> [!NOTE]
> When setting the property `${spring.application.name}` do not prefix your app name with the reserved word `application-` to prevent issues resolving the correct property source.

You can override all of them by setting `spring.cloud.config.*` (where `*` is `name`, `profile` or `label`).
The `label` is useful for rolling back to previous versions of configuration.
With the default Config Server implementation, it can be a git label, branch name, or commit ID.
Label can also be provided as a comma-separated list.
This behavior can be useful when working on a feature branch.
For instance, you might want to align the config label with your branch but make it optional (in that case, use `spring.cloud.config.label=myfeature,develop`).

<a id="client--requesting-multiple-labels"></a>

## Requesting Multiple Labels

Prior to Spring Cloud Config 4.2.0, if you set `spring.cloud.config.label` to a comma-separated list of labels, the Config Client would
try each label by making a request to the Config Server until it found one that worked. This meant that if the first label was found, subsequent labels would not be tried.

As of Spring Cloud Config 4.2.0 if you set `spring.cloud.config.label` to a comma-separated list of labels **AND** set
`spring.cloud.config.send-all-labels` the Config Client will make a single request to the Config Server with the comma-separated list of labels
and if **THE CONFIG SERVER IS USING VERSION 4.2.0 OR LATER** it will return a single response with property sources for all the labels.

> [!NOTE]
> Setting `spring.cloud-config.send-all-labels` to `true`, setting `spring.cloud.config.label` to a comma-separated list of labels, and using a Config Server version prior to 4.2.0 will result in unexpected behavior because the Config Server will try and find a label
> that matches the comma-separated list value and will not try and split apart the labels.

By sending all labels in a single request you can reduce the number of requests made to the Config Server.

`spring.cloud.config.send-all-labels` is set to `false` by default so the old behavior is still the default, and it also maintains
compatibility with older versions of the Config Server.

<a id="client--specifying-multiple-urls-for-the-config-server"></a>

## Specifying Multiple URLs for the Config Server

To ensure high availability when you have multiple instances of Config Server deployed and expect one or more instances to be unavailable or unable to honor requests from time to time (such as if the Git server is down), you can either specify multiple URLs (as a comma-separated list under the `spring.cloud.config.uri` property) or have all your instances register in a Service Registry like Eureka (if using Discovery-First Bootstrap mode).

The URLs listed under `spring.cloud.config.uri` are tried in the order listed. By default, the Config Client will try to fetch properties from each URL until an attempt is successful to ensure high availability.

However, if you want to ensure high availability only when the Config Server is not running (that is, when the application has exited) or when a connection timeout has occurred, set `spring.cloud.config.multiple-uri-strategy` to `connection-timeout-only`. (The default value of `spring.cloud.config.multiple-uri-strategy` is `always`.) For example, if the Config Server returns a 500 (Internal Server Error) response or the Config Client receives a 401 from the Config Server (due to bad credentials or other causes), the Config Client does not try to fetch properties from other URLs. A 400 error (except possibly 404) indicates a user issue rather than an availability problem. Note that if the Config Server is set to use a Git server and the call to Git server fails, a 404 error may occur.

Several locations can be specified under a single `spring.config.import` key instead of `spring.cloud.config.uri`. Locations will be processed in the order that they are defined, with later imports taking precedence. However, if `spring.cloud.config.fail-fast` is `true`, the Config Client will fail if the first Config Server call is unsuccessful for any reason. If `fail-fast` is `false`, it will try all URLs until one call is successful, regardless of the reason for failure. (The `spring.cloud.config.multiple-uri-strategy` does not apply when specifying URLs under `spring.config.import`.)

If you use HTTP basic security on your Config Server, it is currently possible to support per-Config Server auth credentials only if you embed the credentials in each URL you specify under the `spring.cloud.config.uri` property. If you use any other kind of security mechanism, you cannot (currently) support per-Config Server authentication and authorization.

<a id="client--configuring-timeouts"></a>

## Configuring Timeouts

If you want to configure timeout thresholds:

- Read timeouts can be configured by using the property `spring.cloud.config.request-read-timeout`.
- Connection timeouts can be configured by using the property `spring.cloud.config.request-connect-timeout`.

<a id="client--configuring-charsets"></a>
<a id="client--configuring-charset"></a>

## Configuring Charset

If you want to configure a specific charset the resources should be delivered by the server, you need to apply it via charset.

```
spring:
  cloud:
    config:
      charset: UTF-8
```

The charset configuration property is defined as `java.nio.charset.Charset`

<a id="client--security"></a>

## Security

If you use HTTP Basic security on the server, clients need to know the password (and username if it is not the default).
You can specify the username and password through the config server URI or via separate username and password properties, as shown in the following example:

```yaml
spring:
  cloud:
    config:
     uri: https://user:[email protected]
```

The following example shows an alternate way to pass the same information:

```yaml
spring:
  cloud:
    config:
     uri: https://myconfig.mycompany.com
     username: user
     password: secret
```

The `spring.cloud.config.password` and `spring.cloud.config.username` values override anything that is provided in the URI.

If you deploy your apps on Cloud Foundry, the best way to provide the password is through service credentials (such as in the URI, since it does not need to be in a config file).
The following example works locally and for a user-provided service on Cloud Foundry named `configserver`:

```yaml
spring:
  cloud:
    config:
     uri: ${vcap.services.configserver.credentials.uri:http://user:password@localhost:8888}
```

If config server requires client side TLS certificate, you can configure client side TLS certificate and trust store via properties, as shown in following example:

```yaml
spring:
  cloud:
    config:
      uri: https://myconfig.myconfig.com
      tls:
        enabled: true
        key-store: <path-of-key-store>
        key-store-type: PKCS12
        key-store-password: <key-store-password>
        key-password: <key-password>
        trust-store: <path-of-trust-store>
        trust-store-type: PKCS12
        trust-store-password: <trust-store-password>
```

The `spring.cloud.config.tls.enabled` needs to be true to enable config client side TLS. When `spring.cloud.config.tls.trust-store` is omitted, a JVM default trust store is used. The default value for `spring.cloud.config.tls.key-store-type` and `spring.cloud.config.tls.trust-store-type` is PKCS12. When password properties are omitted, empty password is assumed.

If you use another form of security, you might need to [provide a `RestTemplate`](#client--custom-rest-template) to the `ConfigServicePropertySourceLocator` (for example, by grabbing it in the bootstrap context and injecting it).

<a id="client--health-indicator"></a>

### Health Indicator

The Config Client supplies a Spring Boot Health Indicator that attempts to load configuration from the Config Server.
The health indicator can be disabled by setting `management.health.config.enabled=false`.
The response is also cached for performance reasons.
The default cache time to live is 5 minutes.
To change that value, set the `health.config.time-to-live` property (in milliseconds).

<a id="client--custom-rest-template"></a>
<a id="client--providing-a-custom-resttemplate"></a>

### Providing A Custom RestTemplate

In some cases, you might need to customize the requests made to the config server from the client.
Typically, doing so involves passing special `Authorization` headers to authenticate requests to the server.

<a id="client--providing-a-custom-resttemplate-using-config-data"></a>

#### Providing A Custom RestTemplate Using Config Data

To provide a custom `RestTemplate` when using Config Data:

1. Create a class which implements `BootstrapRegistryInitializer`

   CustomBootstrapRegistryInitializer.java


```java
public class CustomBootstrapRegistryInitializer implements BootstrapRegistryInitializer {
@Override public void initialize(BootstrapRegistry registry) {registry.register(RestTemplate.class, context -> {RestTemplate restTemplate = new RestTemplate(); // Customize RestTemplate here return restTemplate; });}
}
```

2. In `resources/META-INF`, create a file called
   `spring.factories` and specify your custom configuration, as shown in the following example:

   spring.factories


```properties
org.springframework.boot.BootstrapRegistryInitializer=com.my.config.client.CustomBootstrapRegistryInitializer
```

<a id="client--providing-a-custom-resttemplate-using-bootstrap"></a>

#### Providing A Custom RestTemplate Using Bootstrap

To provide a custom `RestTemplate` when using Bootstrap:

1. Create a new configuration bean with an implementation of `PropertySourceLocator`, as shown in the following example:

   CustomConfigServiceBootstrapConfiguration.java


```java
@Configuration
public class CustomConfigServiceBootstrapConfiguration {
    @Bean
    public ConfigServicePropertySourceLocator configServicePropertySourceLocator() {
        ConfigClientProperties clientProperties = configClientProperties();
       ConfigServicePropertySourceLocator configServicePropertySourceLocator =  new ConfigServicePropertySourceLocator(clientProperties);
        configServicePropertySourceLocator.setRestTemplate(customRestTemplate(clientProperties));
        return configServicePropertySourceLocator;
    }
}
```


> [!NOTE]
> For a simplified approach to adding `Authorization` headers, the `spring.cloud.config.headers.*` property can be used instead.

2. In `resources/META-INF`, create a file called
   `spring.factories` and specify your custom configuration, as shown in the following example:

   spring.factories


```properties
org.springframework.cloud.bootstrap.BootstrapConfiguration = com.my.config.client.CustomConfigServiceBootstrapConfiguration
```

<a id="client--vault"></a>

### Vault

When using Vault as a backend to your config server, the client needs to supply a token for the server to retrieve values from Vault.
This token can be provided within the client by setting `spring.cloud.config.token`
in `bootstrap.yml`, as shown in the following example:

```yaml
spring:
  cloud:
    config:
      token: YourVaultToken
```

<a id="client--nested-keys-in-vault"></a>

## Nested Keys In Vault

Vault supports the ability to nest keys in a value stored in Vault, as shown in the following example:

`echo -n '{"appA": {"secret": "appAsecret"}, "bar": "baz"}' | vault write secret/myapp -`

This command writes a JSON object to your Vault.
To access these values in Spring, you would use the traditional dot(`.`) annotation, as shown in the following example

```java
@Value("${appA.secret}")
String name = "World";
```

The preceding code would sets the value of the `name` variable to `appAsecret`.

<a id="client--aot-and-native-image-support"></a>

## AOT and Native Image Support

Since `4.0.0`, Spring Cloud Config Client supports Spring AOT transformations and GraalVM native images.

> [!WARNING]
> AOT and native image support is not available for [config first bootstrap](#client--config-first-bootstrap) (with `spring.config.use-legacy-processing=true`).

> [!WARNING]
> Refresh scope is not supported with native images. If you are going to run your config client application as a native image, make sure to set `spring.cloud.refresh.enabled` property to `false`.

> [!WARNING]
> While building a project that contains Spring Cloud Config Client, you must make sure that the configuration data source that it connects to (such as, Spring Cloud Config Server, Consul, Zookeeper, Vault, and others) is available. For example, if you retrieve configuration data from Spring Cloud Config Server, make sure you have its instance running and available at the port indicated in the Config Client setup. This is necessary because the application context is being optimized at build time and requires the target environment to be resolved.

> [!WARNING]
> Since in AOT and native mode, configuration is being processed and the context is being optimised at build time, any properties that would influence bean creation (such as the ones used within bootstrap context) should be set to the same values at build time and runtime to avoid unexpected behaviour.

> [!WARNING]
> Since Config Client connects to a running data source (such as Config Server) while starting up from native image, the quick startup time will be slowed down by the time required for this network communication to take place.

<a id="client--appendix"></a>
<a id="client--appendices"></a>

## Appendices

<a id="client--observability"></a>
<a id="client--observability-metadata"></a>

## Observability metadata

<a id="client--observability-metrics"></a>

### Observability - Metrics

Below you can find a list of all metrics declared by this project.

<a id="client--observability-metrics-environment-repository"></a>
<a id="client--environment-repository"></a>

#### Environment Repository

> Observation created around an EnvironmentRepository.

**Metric name** `spring.cloud.config.environment.find` (defined by convention class `org.springframework.cloud.config.server.environment.ObservationEnvironmentRepositoryObservationConvention`). **Type** `timer`.

**Metric name** `spring.cloud.config.environment.find.active` (defined by convention class `org.springframework.cloud.config.server.environment.ObservationEnvironmentRepositoryObservationConvention`). **Type** `long task timer`.

> [!IMPORTANT]
> KeyValues that are added after starting the Observation might be missing from the \*.active metrics.

> [!IMPORTANT]
> Micrometer internally uses `nanoseconds` for the baseunit. However, each backend determines the actual baseunit. (i.e. Prometheus uses seconds)

Fully qualified name of the enclosing class `org.springframework.cloud.config.server.environment.DocumentedConfigObservation`.

> [!IMPORTANT]
> All tags must be prefixed with `spring.cloud.config.environment` prefix!

| Name | Description |
| --- | --- |
| `spring.cloud.config.environment.application` *(required)* | Application name for which properties are being queried for. |
| `spring.cloud.config.environment.class` *(required)* | Implementation of the EnvironmentRepository. |
| `spring.cloud.config.environment.label` *(required)* | Label for which properties are being queried for. |
| `spring.cloud.config.environment.profile` *(required)* | Application name for which properties are being queried for. |

<a id="client--observability-spans"></a>

### Observability - Spans

Below you can find a list of all spans declared by this project.

<a id="client--observability-spans-environment-repository"></a>
<a id="client--environment-repository-span"></a>

#### Environment Repository Span

> Observation created around an EnvironmentRepository.

**Span name** `spring.cloud.config.environment.find` (defined by convention class `org.springframework.cloud.config.server.environment.ObservationEnvironmentRepositoryObservationConvention`).

Fully qualified name of the enclosing class `org.springframework.cloud.config.server.environment.DocumentedConfigObservation`.

> [!IMPORTANT]
> All tags must be prefixed with `spring.cloud.config.environment` prefix!

| Name | Description |
| --- | --- |
| `spring.cloud.config.environment.application` *(required)* | Application name for which properties are being queried for. |
| `spring.cloud.config.environment.class` *(required)* | Implementation of the EnvironmentRepository. |
| `spring.cloud.config.environment.label` *(required)* | Label for which properties are being queried for. |
| `spring.cloud.config.environment.profile` *(required)* | Application name for which properties are being queried for. |

[AOT and Native Image Support](#server-aot-and-native-image-support)

---
