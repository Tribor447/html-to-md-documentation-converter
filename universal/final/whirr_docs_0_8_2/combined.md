# Untitled

## Navigation

- Documentation
  - [Home](#index)
  - [Whirr in 5 Minutes](#whirr-in-5-minutes)
  - [Quick Start Guide](#quick-start-guide)
  - [Configuration Guide](#configuration-guide)
  - [API Guide](#api-guide)
  - [Release Notes](#release-notes)
  - [Known Limitations](#known-limitations)
  - [Supported Services and Clouds](#supported-services-and-clouds)

## Content

<a id="index"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/index.html -->

<!-- page_index: 1 -->

<a id="index--apache-whirr-0.8.2"></a>

## Apache Whirr™ 0.8.2

Apache Whirr is a set of libraries for running cloud services.

Whirr provides:

- A cloud-neutral way to run services. You don't have to worry about the idiosyncrasies of
  each provider.
- A common service API. The details of provisioning are particular to the service.
- Smart defaults for services. You can get a properly configured system running quickly,
  while still being able to override settings as needed.

You can also use Whirr as a command line tool for deploying clusters.

<a id="index--getting-started"></a>

### Getting Started

Start with [Whirr in 5 Minutes](#whirr-in-5-minutes)
or the
[Quick Start Guide](#quick-start-guide).

There is also an
[FAQ](http://whirr.apache.org/faq.html) which covers how to achieve common tasks with Whirr, and a
[configuration guide](#configuration-guide) for reference.

---

<a id="whirr-in-5-minutes"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/whirr-in-5-minutes.html -->

<!-- page_index: 2 -->

<a id="whirr-in-5-minutes--whirr-in-5-minutes"></a>

## Whirr™ in 5 minutes

The following commands install Whirr and start a 3 node ZooKeeper cluster on Amazon EC2 in 5
minutes or less. You need to have Java 6 and an SSH client already installed. Help on finding
your AWS credentials can be found in the
[FAQ](http://whirr.apache.org/faq.html#how-do-i-find-my-cloud-credentials).

```

export WHIRR_PROVIDER=aws-ec2
export WHIRR_IDENTITY=$AWS_ACCESS_KEY_ID
export WHIRR_CREDENTIAL=$AWS_SECRET_ACCESS_KEY
# or create ~/.whirr/credentials similar to conf/credentials.sample

curl -O http://www.apache.org/dist/whirr/whirr-0.8.2/whirr-0.8.2.tar.gz
tar zxf whirr-0.8.2.tar.gz; cd whirr-0.8.2 

ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa_whirr 
bin/whirr launch-cluster --config recipes/zookeeper.properties --private-key-file ~/.ssh/id_rsa_whirr 

echo "ruok" | nc $(awk '{print $3}' ~/.whirr/zookeeper/instances | head -1) 2181; echo
```

Upon success you should see
imokechoed to the console, indicating that ZooKeeper is running.

You can shut down the cluster with

```
bin/whirr destroy-cluster --config recipes/zookeeper.properties --private-key-file ~/.ssh/id_rsa_whirr
```

The various options are explained in more detail in the
[Quick Start Guide](#quick-start-guide).

---

<a id="quick-start-guide"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/quick-start-guide.html -->

<!-- page_index: 3 -->

<a id="quick-start-guide--getting-started-with-whirr"></a>

## Getting Started with Whirr™

The Whirr CLI provides the most convenient way to launch clusters. For the programmatic
interface, see the
[javadoc](https://whirr.apache.org/docs/0.8.2/apidocs/index.html).

Also see
[Whirr in 5 Minutes](#whirr-in-5-minutes) for the condensed instructions for
getting started (with ZooKeeper as the example).

<a id="quick-start-guide--pre-requisites"></a>

#### Pre-requisites

- Java 6
- An account with a cloud provider, such as Amazon EC2, or Rackspace Cloud Servers
- An SSH client

<a id="quick-start-guide--install-whirr"></a>

#### Install Whirr

[Download](http://www.apache.org/dyn/closer.cgi/whirr/) or
[build](https://cwiki.apache.org/confluence/display/WHIRR/How+To+Contribute) Whirr.

You can test that Whirr is working by running:

```
% bin/whirr version
```

Which will display the version of Whirr that is installed.

To get usage instructions type:

```
% bin/whirr
```

<a id="quick-start-guide--setup-your-credentials"></a>

#### Setup your Credentials

```

% mkdir -p ~/.whirr
% cp conf/credentials.sample ~/.whirr/credentials
    
```

Edit ~/.whirr/credentials using your editor of choice and add the API
connection credentials as required.

<a id="quick-start-guide--configure-a-hadoop-cluster"></a>

#### Configure a Hadoop cluster

First, create a properties file to define the cluster. The name doesn't matter, but here we
will assume it is called
*hadoop.properties* and located in your home directory. This file defines a cluster with a
single machine for the namenode and jobtracker, and a further machine for a datanode and
tasktracker. You can see how to launch other services by consulting the sample configurations
in the
*recipes* directory of the distribution.

```

whirr.cluster-name=myhadoopcluster 
whirr.instance-templates=1 hadoop-jobtracker+hadoop-namenode,1 hadoop-datanode+hadoop-tasktracker 
whirr.provider=aws-ec2
whirr.private-key-file=${sys:user.home}/.ssh/id_rsa
whirr.public-key-file=${sys:user.home}/.ssh/id_rsa.pub
```

Note that we haven't specified a particular cloud image, since Whirr provides a default for
each provider which should work well enough. However, for larger clusters you will likely use
larger hardware sizes or particular images. See the
*recipes* files and the
[Configuration Guide](#configuration-guide) for details.

In this configuration file the cloud identity and credential are read from environment
variables - you can equally well put them in the configuration file if you wish.

The
private-key-file and
public-key-file properties specify an SSH keypair. You can generate a keypair with:

```
% ssh-keygen -t rsa -P ''
```

You should use only RSA SSH keys, since DSA keys are not accepted yet.

**Note**: the keypair specified by these properties is not the same as the AWS keypair
generated with the
ec2-add-keypair command or the AWS Management Console (since these don't place
*both* of the keys on your local machine). The PEM-encoded X.509 Certificate and Private
Key (e.g. pk-XXXXXX.pem) cannot be used as a keypair either.

<a id="quick-start-guide--launch-a-hadoop-cluster"></a>

#### Launch a Hadoop cluster

Run the following command to launch a cluster:

```
% bin/whirr launch-cluster --config hadoop.properties
```

Messages will be logged to the console as the cluster starts. You can see debug-level
logging in a file named
*whirr.log* in the directory you ran the
*whirr* command from.

A message will be printed out when the cluster has started, with a URL that you can use to
access the web UI.

<a id="quick-start-guide--run-a-proxy"></a>

#### Run a proxy

For security reasons, traffic from the network your client is running on is proxied through
the master node of the cluster using an SSH tunnel (a SOCKS proxy on port 6666).

A script to launch the proxy is created when you launch the cluster, and may be found in
*~/.whirr/<cluster-name>*. Run it as a follows (in a new terminal window):

```
% . ~/.whirr/myhadoopcluster/hadoop-proxy.sh
```

To stop the proxy, just kill the process with Ctrl-C.

Web browsers need to be configured to use this proxy too, so you can view pages served by
worker nodes in the cluster. The most convenient way to do this is to use a
[proxy auto-config
(PAC) file](http://en.wikipedia.org/wiki/Proxy_auto-config) file, such as
[this
one](https://svn.apache.org/repos/asf/whirr/trunk/resources/hadoop-ec2-proxy.pac) for Hadoop EC2 clusters.

If you are using Firefox, then you may find
[FoxyProxy](http://foxyproxy.mozdev.org/) useful for managing
PAC files.

<a id="quick-start-guide--run-a-mapreduce-job"></a>

#### Run a MapReduce job

After you launch a cluster, a
*hadoop-site.xml* file is created in the directory
*~/.whirr/<cluster-name>*. You can use this to connect to the cluster by setting the
HADOOP\_CONF\_DIR environment variable. (It is also possible to set the configuration
file to use by passing it as a
-conf option to Hadoop Tools):

```
% export HADOOP_CONF_DIR=~/.whirr/myhadoopcluster
```

You should now be able to browse HDFS:

```
% hadoop fs -ls /
```

Note that the version of Hadoop installed locally should match the version installed on the
cluster. You should also make sure that the
HADOOP\_HOME environment variable is set.

Here's how you can run a MapReduce job:

```

hadoop fs -mkdir input 
hadoop fs -put $HADOOP_HOME/LICENSE.txt input 
hadoop jar $HADOOP_HOME/hadoop-*examples*.jar wordcount input output 
hadoop fs -cat output/part-* | head
```

<a id="quick-start-guide--configuration"></a>

#### Configuration

Whirr is configured using a properties file, and optionally using command line arguments
when using the CLI. Command line arguments take precedence over properties specified in a
properties file.

For example, instead of using the properties file above, you could launch a Hadoop cluster
with the following command line (note that the
whirr. prefix for properties is not reflected in the command line argument):

```

% bin/whirr launch-cluster \
    --cluster-name=myhadoopcluster \ 
    --instance-templates='1 hadoop-jobtracker+hadoop-namenode,1 hadoop-datanode+hadoop-tasktracker' \ 
    --provider=aws-ec2 \
    --identity=$AWS_ACCESS_KEY_ID \ 
    --credential=$AWS_SECRET_ACCESS_KEY \
    --private-key-file=~/.ssh/id_rsa \ 
    --public-key-file=~/.ssh/id_rsa.pub
```

Notice that here we took advantage of the fact that the AWS credentials have been defined in
environment variables.

See the
[configuration guide](#configuration-guide) for a list of all the configuration
properties you can set.

<a id="quick-start-guide--destroy-a-cluster"></a>

#### Destroy a cluster

When you've finished using a cluster you can terminate the instances and clean up resources
with the following.

**WARNING: All data will be deleted when you destroy the cluster.**

```
% bin/whirr destroy-cluster --config hadoop.properties
```

At this point you shut down the SSH proxy to the cluster if you started one earlier.

---

<a id="configuration-guide"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/configuration-guide.html -->

<!-- page_index: 4 -->

<a id="configuration-guide--whirr-configuration-guide"></a>

## Whirr™ Configuration Guide

Whirr is configured using a properties file, and optionally using command line arguments
when using the CLI. Command line arguments take precedence over properties specified in a
properties file.

For example working configurations, please see the recipes in the
*recipes* directory of the distribution.

<a id="configuration-guide--general-options"></a>

### General Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.config | --config | none | A filename of a properties file containing properties in this table. Note that Whirr properties specified in this file all have a whirr.prefix. |
| whirr.service-name | --service-name | The default service for launching clusters | The name of the service to use. You only need to set this if you want to use a non-standard service launcher. |
| whirr.cluster-name | --cluster-name | none | The name of the cluster to operate on. E.g. hadoopcluster. The cluster name is used to tag the instances in some cloud-specific way. For example, in Amazon it is used to form the security group name. |
| whirr.terminate-all-on-launch-failure | --terminate-all-on-launch-failure | true | Whether or not to automatically terminate all nodes when cluster launch fails for some reason. |

<a id="configuration-guide--instance-templates-options"></a>

### Instance Templates Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.instance-templates | --instance-templates | none | The number of instances to launch for each set of roles in a service. E.g. 1 nn+jt,10 dn+ttmeans one instance with the roles nn(namenode) and jt(jobtracker), and ten instances each with the roles dn(datanode) and tt(tasktracker). Note that currently a role may only be specified in a single group. |
| whirr.instance-templates-max-percent-failures | --instance-templates-max-percent-failures | none | The percentage of successfully started instances for each set of roles. E.g. 100 nn+jt,60 dn+ttmeans all instances with the roles nn(namenode) and jt(jobtracker) has to be successfully started, and 60% of instances has to be successfully started each with the roles dn(datanode) and tt(tasktracker), otherwise a retry step is initiated with the number of nodes equal with the missing nodes per role compared to instance-templatesvalue. If after the retry the percentage of successfully started instances is still behind the limit, then the cluster startup is considered invalid. In a valid cluster startup, with or without retry mechanism, all the failed nodes will be cleaned up immediately. Only the completely failed cluster may leave unterminated failed nodes. Default value is 100 for each roles, in that case we don't need to use this parameter at all. In case we would like to lower the limit from 100% to 60% for only the dd(datanode) and tt(tasktracker), then we can specify 60 dn+ttfor the parameter and we may left the 100 nn+jt,from the beginning of the value. |
| whirr.instance-templates-minimum-number-of-instances | --instance-templates-minimum-number-of-instances | none | The minimum number of successfully started instances for each set of roles. E.g. 1 nn+jt,6 dn+ttmeans 1 instance with the roles nn(namenode) and jt(jobtracker) has to be successfully started, and 6 instances has to be successfully started each with the roles dn(datanode) and tt(tasktracker), otherwise a retry step is initiated with the number of nodes equal with the missing nodes per role compared to instance-templatesvalue. If after the retry the number of successfully started instances i still behind the limit, then the cluster startup is considered invalid. In a valid cluster startup, with or without retry mechanism, all the failed nodes will be cleaned up immediately. Only the completely failed cluster may leave unterminated failed nodes. Note that we may specify only 6 dd+tt, in that case the limit will be applied only to the specified role. Default value is 100 for each roles, in that case we don't need to use this parameter at all. In case we would like to lower the limit for only the dd(datanode) and tt(tasktracker), then we can specify 60 dn+ttfor the parameter, skipping the 100 nn+jt. |
| whirr.max-startup-retries | --max-startup-retries | 1 | The number of retries in case of insufficient successfully started instances. |
| whirr.aws-ec2-spot-price | --aws-ec2-spot-price | none | Spot instance price. If the price isn't fulfilled it times out after 20 minutes (jclouds.compute.timeout.node-running). We recommended that you set the spot price to current real price so that you will always save money while keeping the instances running because you will still pay the spot price and not the max value you put in. Keep in mind that price spikes can still take out some instances, or prevent requests being filled, but it works well most of the time. Note: this is an EC2 specific option. |

<a id="configuration-guide--cloud-provider-options"></a>

### Cloud Provider Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.provider | --provider | aws-ec2 | The name of the cloud provider. See the [table below](#configuration-guide--cloud-provider-config) for possible provider names. |
| whirr.location-id | --location-id | none | The location to launch instances in. If not specified then an arbitrary location will be chosen. |
| whirr.endpoint | --endpoint | none | Specifies the url of the compute provider. For example, for openstack-nova, it is the keystone url, like: http://localhost:5000/v2.0/. If not specified, it is the default for the provider |
| whirr.identity | --identity | none | The cloud identity. See the [table below](#configuration-guide--cloud-provider-config) for how this maps to the credentials for your provider. |
| whirr.credential | --credential | none | The cloud credential. See the [table below](#configuration-guide--cloud-provider-config) for how this maps to the credentials for your provider. |
| whirr.bootstrap-user | --bootstrap-user | none | Override the default login user used to bootstrap whirr. E.g. ubuntu or myuser:mypass |

You can see a list of all the available compute providers by running:

```
$ whirr list-providers compute
```

Note: we are testing only on aws-ec2 and cloudserver-us.

<a id="configuration-guide--blobstore-provider-options"></a>

### BlobStore Provider Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.blobstore-provider | --blobstore-provider | Computed from whirr.provider | The name of the blobstore provider. All jclouds blobstore providers are supported |
| whirr.blobstore-endpoint | --blobstore-endpoint | none | Specifies the url of the blobstore provider. For example, for swift-keystone, it is the keystone url, like: http://localhost:5000/v2.0/. If not specified, it is the default for the provider |
| whirr.blobstore-identity | --blobstore-identity | whirr.identity | The blobstore identity. See the [table below](#configuration-guide--cloud-provider-config) for how this maps to the credentials for your provider. |
| whirr.blobstore-credential | --blobstore-credential | whirr.credential | The blobstore credential. See the [table below](#configuration-guide--cloud-provider-config) for how this maps to the credentials for your provider. |
| whirr.blobstore-location-id | --blobstore-location-id | As close as possible to the compute nodes | The blobstore location ID |
| whirr.blobstore-cache-container | --blobstore-cache-container | Random container automatically removed at the end of the session | The name of the container that Whirr should use to cache local files |

You can see a list of all the available blobstore providers by running

```
$ whirr list-providers blobstore
```

Note: we are testing only on aws-s3 and cloudfiles-us.

<a id="configuration-guide--cluster-state-store-options"></a>

### Cluster State Store Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.state-store | --state-store | local | What kind of store to use for cluster state (local, blob or none). |
| whirr.state-store-container | --state-store-container | none | Container where to store state. Valid only for the blob state store. |
| whirr.state-store-blob | --state-store-blob | whirr-< whirr.cluster-name> | Blob name for state storage. Valid only for the blob state store. |

<a id="configuration-guide--instance-login-options"></a>

### Instance Login Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.cluster-user | --cluster-user | Current local user | The name of the user that Whirr will create on all instances. This is the user you should use to access the cluster. |
| whirr.private-key-file | --private-key-file | *~/.ssh/id\_rsa* | The filename of the private RSA SSH key used to connect to instances. Note: the public/private key must be set together, and must be passwordless. |
| whirr.public-key-file | --public-key-file | *~/.ssh/id\_rsa*.pub | The filename of the public RSA SSH key used to connect to instances. Note: the public/private key must be set together, and must be passwordless. |

<a id="configuration-guide--image-and-hardware-selection-options"></a>

### Image and Hardware Selection Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.template | --template | osFamily=UBUNTU,osVersionMatches=10.04,minRam=1024 | The specification of requirements for instances in jclouds [TemplateBuilderSpec](https://github.com/jclouds/jclouds/blob/1.5.x/compute/src/main/java/org/jclouds/compute/domain/TemplateBuilderSpec.java) format. For example, this can control the ram, cores, os, and login user details. |
| whirr.image-id | --image-id | none | The ID of the image to use for instances. If not specified then a vanilla Linux image is chosen. |
| whirr.hardware-id | --hardware-id | none | The type of hardware to use for the instance. This must be compatible with the image ID. |
| whirr.hardware-min-ram | --hardware-min-ram | 1024 | The minimum amount of RAM each instance should have |

<a id="configuration-guide--firewall-and-dns-related-options"></a>

### Firewall and DNS-Related Options

| **Name** | **Command line option** | **Default** | **Description** |
| --- | --- | --- | --- |
| whirr.client-cidrs | --client-cidrs | none | A comma-separated list of [CIDR](http://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing)blocks. E.g. 208.128.0.0/11,108.128.0.0/11 |
| whirr.firewall-rules | --firewall-rules | none | A comma-separated list of port numbers to open. E.g. 8080,8181. |
| whirr.firewall-rules.{role} | --firewall-rules.{role} | none | A comma-separated list of port numbers to open on instances with a specific role. Replace {role} the actual role name. E.g. whirr.firewall-rules.hbase-master=10101. |
| whirr.store-cluster-in-etc-hosts | --store-cluster-in-etc-hosts | false | Whether to store all cluster IPs and hostnames in /etc/hosts on each node. |

<a id="configuration-guide--cloud-provider-specific-configuration"></a>

### Cloud provider specific configuration

| **Compute Service Provider** | **whirr.provider** | **whirr.identity** | **whirr.credential** | **Notes** |
| --- | --- | --- | --- | --- |
| Amazon EC2 | aws-ec2 | Access Key ID | Secret Access Key | Used to form security Group (via jclouds tag) |
| Rackspace Cloud Servers | cloudservers-us | Username | API Key | Warning: clusters do not run behind a firewall. |

<a id="configuration-guide--relevant-jclouds-configuration-options"></a>

### Relevant jclouds configuration options

| **Name** | **Default** | **Unit** | **Description** |
| --- | --- | --- | --- |
| jclouds.compute.timeout.node-terminated | 30000 (30 sec.) | msec | The max. time to wait for nodes to be terminated |
| jclouds.compute.timeout.node-running | 120000 (2 min.) | msec | The max. time to wait for nodes to be in running state |
| jclouds.compute.timeout.script-complete | 600000 (10 min.) | msec | The max. time to wait for a script to complete execution |
| jclouds.compute.timeout.port-open | 30000 (30 sec.) | msec | The max. time to wait for nodes to wait for the ssh port to open on newly lauched nodes |
| jclouds.ssh.retryable-messages | failed to send channel request, channel is not opened, invalid data, End of IO Stream Read, Connection reset, connection is closed by foreign host, socket is not established | -- | Comma-separated list of error messages upon receiving which jclouds retries the ssh action. |
| jclouds.ssh.max-retries | 7 | times | The max. number of retries jclouds will attempt a failed ssh action. The period between tries increases from 200ms -> 2 seconds per math.pow(attempt, 2) |
| jclouds.ssh.retry-auth | true | boolean | Whether jclouds should retry ssh actions on authentication failed errors. |
| jclouds.compute.blacklist-nodes |  | -- | Comma-separated list of nodes that we shouldn't attempt to list as they are dead in the provider for some reason. |

---

<a id="api-guide"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/api-guide.html -->

<!-- page_index: 5 -->

<a id="api-guide--whirr-api-guide"></a>

## Whirr™ API Guide

Whirr provides a Java API for stopping and starting clusters. Please see the
[javadoc](https://whirr.apache.org/docs/0.8.2/apidocs/index.html) and the unit test source code for how to achieve
this.

The downloaded artifact contains a example project that shows how Whirr can be used
for various tasks .Check the *examples* subfolder.

You can execute an example by running:

```
$ ./bin/example [example-name]
```

---

<a id="release-notes"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/release-notes.html -->

<!-- page_index: 6 -->

# Release Notes - Whirr - Version 0.8.1

Release Notes - Whirr - Version 0.8.2

<a id="release-notes--bug"></a>

## Bug

- [[WHIRR-677](https://issues.apache.org/jira/browse/WHIRR-677)] - Whirr fails to install CDH4 nodemanager properly
- [[WHIRR-678](https://issues.apache.org/jira/browse/WHIRR-678)] - Apache Whirr is not using my whirr.location-id parameter on EC2
- [[WHIRR-679](https://issues.apache.org/jira/browse/WHIRR-679)] - Switch to HBase 0.94.2
- [[WHIRR-693](https://issues.apache.org/jira/browse/WHIRR-693)] - Control order of actions with waves of whirr.instance-templates
- [[WHIRR-705](https://issues.apache.org/jira/browse/WHIRR-705)] - provide better integration between parameterized classes and Hiera
- [[WHIRR-707](https://issues.apache.org/jira/browse/WHIRR-707)] - RunUrlStatementTest fails due to missing URL
- [[WHIRR-709](https://issues.apache.org/jira/browse/WHIRR-709)] - Hadoop defaults fail to install due to version bump @ osuosl.org
- [[WHIRR-712](https://issues.apache.org/jira/browse/WHIRR-712)] - prepare\_all\_disks.sh should cover xvdX as well as sdX.
- [[WHIRR-715](https://issues.apache.org/jira/browse/WHIRR-715)] - Unit test failure in whirr-puppet
- [[WHIRR-716](https://issues.apache.org/jira/browse/WHIRR-716)] - Karaf itests fail

<a id="release-notes--improvement"></a>

## Improvement

- [[WHIRR-546](https://issues.apache.org/jira/browse/WHIRR-546)] - Add destroy instructions to stdout for all create actions
- [[WHIRR-634](https://issues.apache.org/jira/browse/WHIRR-634)] - Update private IP host file entry when required by AUTO\_HOSTNAME\_SUFFIX
- [[WHIRR-660](https://issues.apache.org/jira/browse/WHIRR-660)] - provide a useful error message if whirr.instance-templates is not in a cluster spec
- [[WHIRR-661](https://issues.apache.org/jira/browse/WHIRR-661)] - Upgrade to Hadoop 1.0.3
- [[WHIRR-669](https://issues.apache.org/jira/browse/WHIRR-669)] - The whirr karaf feature should use feature version range on jclouds.
- [[WHIRR-670](https://issues.apache.org/jira/browse/WHIRR-670)] - Upgrade to jclouds 1.5.3
- [[WHIRR-672](https://issues.apache.org/jira/browse/WHIRR-672)] - Allow eager caching of instance hostname based on pre-provision instance metadata
- [[WHIRR-673](https://issues.apache.org/jira/browse/WHIRR-673)] - Upgrade CDH Repos for RHEL/CentOS 6
- [[WHIRR-675](https://issues.apache.org/jira/browse/WHIRR-675)] - Convert all whirr.env.\* environment variable labels to upper case
- [[WHIRR-681](https://issues.apache.org/jira/browse/WHIRR-681)] - enhance puppet service with an ability to export cluster topology to the puppet code
- [[WHIRR-691](https://issues.apache.org/jira/browse/WHIRR-691)] - Java install to support Debian
- [[WHIRR-694](https://issues.apache.org/jira/browse/WHIRR-694)] - install puppet from puppetlabs repos instead of the ruby gem
- [[WHIRR-699](https://issues.apache.org/jira/browse/WHIRR-699)] - Fix indentation and formatting on "Getting Started" page
- [[WHIRR-711](https://issues.apache.org/jira/browse/WHIRR-711)] - Add security group support for OpenStack
- [[WHIRR-713](https://issues.apache.org/jira/browse/WHIRR-713)] - Enable programmatic use of BYON via CacheNodeStoreModule
- [[WHIRR-717](https://issues.apache.org/jira/browse/WHIRR-717)] - Make use of the context name in the dynamic compute cache.

<a id="release-notes--new-feature"></a>

## New Feature

- [[WHIRR-118](https://issues.apache.org/jira/browse/WHIRR-118)] - Adaptor for OpenStack Clouds
- [[WHIRR-671](https://issues.apache.org/jira/browse/WHIRR-671)] - Create Kerberos Service
- [[WHIRR-680](https://issues.apache.org/jira/browse/WHIRR-680)] - add python scripts to aid ssh/scp in to VMs
- [[WHIRR-696](https://issues.apache.org/jira/browse/WHIRR-696)] - Whirr script for Hadoop MRv2 YARN installs that supports Hadoop-2.0.x and Hadoop 3.x (trunk) branches

<a id="release-notes--release-notes-whirr-version-0.8.1"></a>

# Release Notes - Whirr - Version 0.8.1

<a id="release-notes--bug-2"></a>

## Bug

- [[WHIRR-641](https://issues.apache.org/jira/browse/WHIRR-641)] - No longer possible to hardcode password for bootstrap user
- [[WHIRR-642](https://issues.apache.org/jira/browse/WHIRR-642)] - Whirr writes the AWS Secret key to the stdout. is it an unforeseen byproduct or intended behavior?
- [[WHIRR-645](https://issues.apache.org/jira/browse/WHIRR-645)] - Race condition between collocated namenode and jobtracker start/init services
- [[WHIRR-646](https://issues.apache.org/jira/browse/WHIRR-646)] - Integration tests should have failsafe timeouts
- [[WHIRR-648](https://issues.apache.org/jira/browse/WHIRR-648)] - CDH repo install removes other repos with same prefix
- [[WHIRR-666](https://issues.apache.org/jira/browse/WHIRR-666)] - Upgrade to jclouds 1.5.1

<a id="release-notes--improvement-2"></a>

## Improvement

- [[WHIRR-593](https://issues.apache.org/jira/browse/WHIRR-593)] - Upgrade to jclouds 1.5.0
- [[WHIRR-638](https://issues.apache.org/jira/browse/WHIRR-638)] - Paramaterize OAB Java install
- [[WHIRR-649](https://issues.apache.org/jira/browse/WHIRR-649)] - Make install\_cdh\_hadoop.sh idempotent, fast failing if already run
- [[WHIRR-654](https://issues.apache.org/jira/browse/WHIRR-654)] - Tell RAT to avoid checking atlassian-idex.xml
- [[WHIRR-659](https://issues.apache.org/jira/browse/WHIRR-659)] - Upgrade to jclouds 1.5.0

<a id="release-notes--release-notes-whirr-version-0.8.0"></a>

# Release Notes - Whirr - Version 0.8.0

<a id="release-notes--sub-task"></a>

## Sub-task

- [[WHIRR-421](https://issues.apache.org/jira/browse/WHIRR-421)] - Handle more role / service lifecycle events as part of the core functionality
- [[WHIRR-422](https://issues.apache.org/jira/browse/WHIRR-422)] - Integration tests should fail or succeed in a limited amount of time

<a id="release-notes--bug-3"></a>

## Bug

- [[WHIRR-378](https://issues.apache.org/jira/browse/WHIRR-378)] - Auth fail when creating a cluster from an EC2 instance
- [[WHIRR-435](https://issues.apache.org/jira/browse/WHIRR-435)] - sun-java6-jdk installation fails in install\_java\_deb() function on Ubuntu 11.10 AMI
- [[WHIRR-438](https://issues.apache.org/jira/browse/WHIRR-438)] - Add new amazon west region
- [[WHIRR-445](https://issues.apache.org/jira/browse/WHIRR-445)] - JAVA\_HOME is not set / exported by the install script
- [[WHIRR-473](https://issues.apache.org/jira/browse/WHIRR-473)] - HadoopServiceController.getInstance(String config) does not update instances correctly
- [[WHIRR-494](https://issues.apache.org/jira/browse/WHIRR-494)] - Update the BYON cluster controller to support all the operations the regular controller supports
- [[WHIRR-496](https://issues.apache.org/jira/browse/WHIRR-496)] - Documentation in 5-Minute guide is missing key option for destroy step
- [[WHIRR-511](https://issues.apache.org/jira/browse/WHIRR-511)] - Instance.getPrivateHostName returns an IP address
- [[WHIRR-524](https://issues.apache.org/jira/browse/WHIRR-524)] - Change confusing 'Starting cluster' message
- [[WHIRR-536](https://issues.apache.org/jira/browse/WHIRR-536)] - Using SNAPSHOT versions of jclouds breaks OSGi support
- [[WHIRR-541](https://issues.apache.org/jira/browse/WHIRR-541)] - install\_oracle\_jdk[67].sh fails to create /usr/bin/java
- [[WHIRR-549](https://issues.apache.org/jira/browse/WHIRR-549)] - Remove dependency on system SSH keys in tests
- [[WHIRR-568](https://issues.apache.org/jira/browse/WHIRR-568)] - Use the correct CDH version/repository
- [[WHIRR-579](https://issues.apache.org/jira/browse/WHIRR-579)] - sun jdk install fails
- [[WHIRR-580](https://issues.apache.org/jira/browse/WHIRR-580)] - install\_openjdk\_rpm is broken
- [[WHIRR-582](https://issues.apache.org/jira/browse/WHIRR-582)] - Yarn service does not build in IntelliJ because of missing Hadoop test dependencies
- [[WHIRR-583](https://issues.apache.org/jira/browse/WHIRR-583)] - Install OpenJDK fails on centos
- [[WHIRR-584](https://issues.apache.org/jira/browse/WHIRR-584)] - Change confusing ssh login help message at the end of deployment
- [[WHIRR-588](https://issues.apache.org/jira/browse/WHIRR-588)] - Timeouts on whirr run-script command
- [[WHIRR-599](https://issues.apache.org/jira/browse/WHIRR-599)] - Whirr CDH4 CDHHadoopServiceTest.testVersion() is broken
- [[WHIRR-600](https://issues.apache.org/jira/browse/WHIRR-600)] - Bump up CDH4 Maven dependencies
- [[WHIRR-601](https://issues.apache.org/jira/browse/WHIRR-601)] - Cassandra 1.0.8 download URL no longer valid
- [[WHIRR-602](https://issues.apache.org/jira/browse/WHIRR-602)] - Cloud providers may only return "private" IPs
- [[WHIRR-603](https://issues.apache.org/jira/browse/WHIRR-603)] - HBase 0.89 tests won't work with Hadoop 0.20.205
- [[WHIRR-604](https://issues.apache.org/jira/browse/WHIRR-604)] - Non-resolvable hostnames should be reset to something resolvable
- [[WHIRR-608](https://issues.apache.org/jira/browse/WHIRR-608)] - CDH HBase configuration uses CDH3 package and service names only
- [[WHIRR-609](https://issues.apache.org/jira/browse/WHIRR-609)] - Yum install of openjdk needs -y
- [[WHIRR-610](https://issues.apache.org/jira/browse/WHIRR-610)] - whirr.env.repo should be whirr.env.REPO (?)
- [[WHIRR-611](https://issues.apache.org/jira/browse/WHIRR-611)] - Cloud providers may only return "public" IPs
- [[WHIRR-612](https://issues.apache.org/jira/browse/WHIRR-612)] - CDH4 can be installed on Ubuntu now as well as CentOS
- [[WHIRR-613](https://issues.apache.org/jira/browse/WHIRR-613)] - OpenJDK JAVA\_HOME detection needs to be improved
- [[WHIRR-614](https://issues.apache.org/jira/browse/WHIRR-614)] - Add HADOOP\_HOME/lib to HBase classpath
- [[WHIRR-615](https://issues.apache.org/jira/browse/WHIRR-615)] - Use Hadoop 1.0.3 in HBase 0.90 tests
- [[WHIRR-616](https://issues.apache.org/jira/browse/WHIRR-616)] - Starting multiple yarn nodemanagers on EC2
- [[WHIRR-618](https://issues.apache.org/jira/browse/WHIRR-618)] - Site generation is unnecessarily recursive
- [[WHIRR-629](https://issues.apache.org/jira/browse/WHIRR-629)] - YARN tests fail on Rackspace
- [[WHIRR-633](https://issues.apache.org/jira/browse/WHIRR-633)] - Align jclouds 1.5.0 modularity changes with Whirr
- [[WHIRR-635](https://issues.apache.org/jira/browse/WHIRR-635)] - Ensure hostname update as required by AUTO\_HOSTNAME\_SUFFIX is consistent for RHEL derivatives
- [[WHIRR-639](https://issues.apache.org/jira/browse/WHIRR-639)] - /data\*/hadoop should be owned and writable by the hadoop group for CDH.
- [[WHIRR-640](https://issues.apache.org/jira/browse/WHIRR-640)] - Recipes and tests using whirr.template should specify minRam there

<a id="release-notes--improvement-3"></a>

## Improvement

- [[WHIRR-189](https://issues.apache.org/jira/browse/WHIRR-189)] - Hadoop on EC2 should use all available local storage
- [[WHIRR-332](https://issues.apache.org/jira/browse/WHIRR-332)] - Need to specify different instance size/type depending on role
- [[WHIRR-347](https://issues.apache.org/jira/browse/WHIRR-347)] - Support provider-independent environment variables for cloud credentials
- [[WHIRR-351](https://issues.apache.org/jira/browse/WHIRR-351)] - configure\_hadoop should create+chown all data dirs listed in hadoop-hdfs.dfs.data.dir
- [[WHIRR-370](https://issues.apache.org/jira/browse/WHIRR-370)] - Templating for configuration files
- [[WHIRR-428](https://issues.apache.org/jira/browse/WHIRR-428)] - Always match a stable Canonical AMI on AWS EC2
- [[WHIRR-436](https://issues.apache.org/jira/browse/WHIRR-436)] - Allow Whirr to run from inside OSGi
- [[WHIRR-456](https://issues.apache.org/jira/browse/WHIRR-456)] - Upgrade to jclouds 1.3.0
- [[WHIRR-458](https://issues.apache.org/jira/browse/WHIRR-458)] - Remove deprecated code and aliasing mechanism
- [[WHIRR-461](https://issues.apache.org/jira/browse/WHIRR-461)] - Allow user to specify spot instance price per instance template group
- [[WHIRR-469](https://issues.apache.org/jira/browse/WHIRR-469)] - Optimal Cassandra Node Balancing
- [[WHIRR-471](https://issues.apache.org/jira/browse/WHIRR-471)] - Display jclouds version
- [[WHIRR-474](https://issues.apache.org/jira/browse/WHIRR-474)] - Add functions that can be used as basic distributed synchronisation primitives in bash scripts
- [[WHIRR-475](https://issues.apache.org/jira/browse/WHIRR-475)] - Rename login-user to bootstrap-user to avoid confusions
- [[WHIRR-479](https://issues.apache.org/jira/browse/WHIRR-479)] - ScriptBasedClusterAction should allow filtering by role and instance-id
- [[WHIRR-483](https://issues.apache.org/jira/browse/WHIRR-483)] - Upgrade to jclouds 1.3.1
- [[WHIRR-484](https://issues.apache.org/jira/browse/WHIRR-484)] - Add restart-services command
- [[WHIRR-497](https://issues.apache.org/jira/browse/WHIRR-497)] - Update maven plugins & project deps
- [[WHIRR-504](https://issues.apache.org/jira/browse/WHIRR-504)] - Upgrade to jclouds 1.4.0
- [[WHIRR-509](https://issues.apache.org/jira/browse/WHIRR-509)] - Provide live OSGi integration tests
- [[WHIRR-510](https://issues.apache.org/jira/browse/WHIRR-510)] - Get ZooKeeper ensemble with internal addresses
- [[WHIRR-525](https://issues.apache.org/jira/browse/WHIRR-525)] - Upgrade to HBase 0.92.0
- [[WHIRR-528](https://issues.apache.org/jira/browse/WHIRR-528)] - Add a retry loop around apt-get and yum commands to overcome transient errors
- [[WHIRR-542](https://issues.apache.org/jira/browse/WHIRR-542)] - Only expose start / stop / restart as new CLI commands
- [[WHIRR-548](https://issues.apache.org/jira/browse/WHIRR-548)] - Allow whirr to reuse existing compute services
- [[WHIRR-551](https://issues.apache.org/jira/browse/WHIRR-551)] - Upgrade to jclouds 1.3.2
- [[WHIRR-556](https://issues.apache.org/jira/browse/WHIRR-556)] - The message 'running on $PROVIDER using identity $IDENTITY' is confusing
- [[WHIRR-561](https://issues.apache.org/jira/browse/WHIRR-561)] - Make HBase metrics appear in Ganglia
- [[WHIRR-573](https://issues.apache.org/jira/browse/WHIRR-573)] - Allow specification of REPO\_HOST for RPMs/debs
- [[WHIRR-587](https://issues.apache.org/jira/browse/WHIRR-587)] - Update version of jopt-simple (from 3.2 to 4.3)
- [[WHIRR-591](https://issues.apache.org/jira/browse/WHIRR-591)] - Maven profile for Karaf itests (inactive by default)
- [[WHIRR-605](https://issues.apache.org/jira/browse/WHIRR-605)] - Upgrade Cassandra to 1.1.2
- [[WHIRR-630](https://issues.apache.org/jira/browse/WHIRR-630)] - add property endpoint
- [[WHIRR-665](https://issues.apache.org/jira/browse/WHIRR-665)] - list of SSH commands should also identify host roles

<a id="release-notes--new-feature-2"></a>

## New Feature

- [[WHIRR-63](https://issues.apache.org/jira/browse/WHIRR-63)] - Support EC2 Cluster Compute Groups for Hadoop
- [[WHIRR-388](https://issues.apache.org/jira/browse/WHIRR-388)] - Support for CloudStack
- [[WHIRR-465](https://issues.apache.org/jira/browse/WHIRR-465)] - Add Solr as a service
- [[WHIRR-500](https://issues.apache.org/jira/browse/WHIRR-500)] - Let users control which hardware is used for each instance template.

<a id="release-notes--task"></a>

## Task

- [[WHIRR-477](https://issues.apache.org/jira/browse/WHIRR-477)] - Upgrade Cassandra service to 1.0.7
- [[WHIRR-514](https://issues.apache.org/jira/browse/WHIRR-514)] - Update release instructions or fix update-version script?

<a id="release-notes--test"></a>

## Test

- [[WHIRR-493](https://issues.apache.org/jira/browse/WHIRR-493)] - Test override number of mappers for Hadoop

<a id="release-notes--release-notes-whirr-version-0.7.1"></a>

# Release Notes - Whirr - Version 0.7.1

<a id="release-notes--bug-4"></a>

## Bug

- [[WHIRR-367](https://issues.apache.org/jira/browse/WHIRR-367)] - Wrong groupId for zookeeper
- [[WHIRR-460](https://issues.apache.org/jira/browse/WHIRR-460)] - Error while running whirr on Cygwin
- [[WHIRR-490](https://issues.apache.org/jira/browse/WHIRR-490)] - hadoop-mapreduce.mapred.child.ulimit should be unlimited by default
- [[WHIRR-495](https://issues.apache.org/jira/browse/WHIRR-495)] - bin/whirr is does not have executable permissions in the 0.7.0 pre-built download
- [[WHIRR-502](https://issues.apache.org/jira/browse/WHIRR-502)] - configure\_cdh\_hadoop.sh: syntax error trying to modify permissions on $HADOOP\_LOG\_DIR
- [[WHIRR-518](https://issues.apache.org/jira/browse/WHIRR-518)] - Change to OpenJDK
- [[WHIRR-520](https://issues.apache.org/jira/browse/WHIRR-520)] - Using OAB script to install sun jdk
- [[WHIRR-521](https://issues.apache.org/jira/browse/WHIRR-521)] - Backport InstallJDK functionality from jclouds 1.4.0

<a id="release-notes--improvement-4"></a>

## Improvement

- [[WHIRR-439](https://issues.apache.org/jira/browse/WHIRR-439)] - Make proxy files executable
- [[WHIRR-454](https://issues.apache.org/jira/browse/WHIRR-454)] - Allow openjdk to be installed as an alternative to sun-java-6
- [[WHIRR-463](https://issues.apache.org/jira/browse/WHIRR-463)] - Fail fast when running as root
- [[WHIRR-498](https://issues.apache.org/jira/browse/WHIRR-498)] - Update the list of known limitations
- [[WHIRR-507](https://issues.apache.org/jira/browse/WHIRR-507)] - Make whirr script executable from any path
- [[WHIRR-517](https://issues.apache.org/jira/browse/WHIRR-517)] - Add a retry loop around apt-get and yum commands to overcome transient errors
- [[WHIRR-526](https://issues.apache.org/jira/browse/WHIRR-526)] - Don't log harmless sshj errors to console

<a id="release-notes--release-notes-whirr-version-0.7.0"></a>

# Release Notes - Whirr - Version 0.7.0

<a id="release-notes--sub-task-2"></a>

## Sub-task

- [[WHIRR-386](https://issues.apache.org/jira/browse/WHIRR-386)] - Remove references to the Apache Incubator
- [[WHIRR-387](https://issues.apache.org/jira/browse/WHIRR-387)] - Add Website Navigation Links
- [[WHIRR-403](https://issues.apache.org/jira/browse/WHIRR-403)] - Add Trademark Attributions
- [[WHIRR-404](https://issues.apache.org/jira/browse/WHIRR-404)] - Add Project Metadata

<a id="release-notes--bug-5"></a>

## Bug

- [[WHIRR-352](https://issues.apache.org/jira/browse/WHIRR-352)] - mvn package assembly:assembly fails
- [[WHIRR-376](https://issues.apache.org/jira/browse/WHIRR-376)] - Launching a BYON cluster doesn't produce an instances file.
- [[WHIRR-377](https://issues.apache.org/jira/browse/WHIRR-377)] - Fix broken CLI logging config
- [[WHIRR-394](https://issues.apache.org/jira/browse/WHIRR-394)] - NPE used for flow control
- [[WHIRR-396](https://issues.apache.org/jira/browse/WHIRR-396)] - service/ganglia needs non-zero send\_metadata\_interval= in gmond.conf
- [[WHIRR-397](https://issues.apache.org/jira/browse/WHIRR-397)] - Automatic template selection is too restrictive
- [[WHIRR-410](https://issues.apache.org/jira/browse/WHIRR-410)] - Review automatic image selection
- [[WHIRR-412](https://issues.apache.org/jira/browse/WHIRR-412)] - cannot set up eclipse at "How To Contribute"
- [[WHIRR-414](https://issues.apache.org/jira/browse/WHIRR-414)] - whirr can have a non-zero return code and unterminated (orphaned) host instances
- [[WHIRR-427](https://issues.apache.org/jira/browse/WHIRR-427)] - CDH Hadoop integration test fails with malformed reply from SOCKS, may be version issue
- [[WHIRR-432](https://issues.apache.org/jira/browse/WHIRR-432)] - Puppet integration tests failing
- [[WHIRR-433](https://issues.apache.org/jira/browse/WHIRR-433)] - Chef integration tests failing
- [[WHIRR-437](https://issues.apache.org/jira/browse/WHIRR-437)] - Cassandra integration test is failing
- [[WHIRR-442](https://issues.apache.org/jira/browse/WHIRR-442)] - release 0.6.0 is in breach of the AL2.0 and general Apache rules in regards to the inclusion of Voldemort
- [[WHIRR-447](https://issues.apache.org/jira/browse/WHIRR-447)] - FastDnsResolver fails with SocketTimeoutException
- [[WHIRR-449](https://issues.apache.org/jira/browse/WHIRR-449)] - slf4j impl is not being copied to the lib dir when executing the binary assembly

<a id="release-notes--improvement-5"></a>

## Improvement

- [[WHIRR-116](https://issues.apache.org/jira/browse/WHIRR-116)] - Site should have docs for each released version
- [[WHIRR-243](https://issues.apache.org/jira/browse/WHIRR-243)] - Allow to run component tests in memory
- [[WHIRR-325](https://issues.apache.org/jira/browse/WHIRR-325)] - Reduce cloud provider-specific code in scripts
- [[WHIRR-340](https://issues.apache.org/jira/browse/WHIRR-340)] - Use spot instances for testing
- [[WHIRR-342](https://issues.apache.org/jira/browse/WHIRR-342)] - hadoop/hbase configuration & active roles on a node
- [[WHIRR-356](https://issues.apache.org/jira/browse/WHIRR-356)] - Upgrade elasticsearch to 0.17.4
- [[WHIRR-357](https://issues.apache.org/jira/browse/WHIRR-357)] - Run elasticsearch as a non-root-user
- [[WHIRR-358](https://issues.apache.org/jira/browse/WHIRR-358)] - Enable remote JMX access for HBase
- [[WHIRR-366](https://issues.apache.org/jira/browse/WHIRR-366)] - Make website comply with Apache branding guidelines
- [[WHIRR-368](https://issues.apache.org/jira/browse/WHIRR-368)] - Add the ability to adjust contents of hadoop-env.sh from a cluster properties file
- [[WHIRR-371](https://issues.apache.org/jira/browse/WHIRR-371)] - Allow defining additional firewall rules
- [[WHIRR-382](https://issues.apache.org/jira/browse/WHIRR-382)] - Upgrade to Commons Configuration 1.7
- [[WHIRR-395](https://issues.apache.org/jira/browse/WHIRR-395)] - Less verbose logging when setting firewall rules
- [[WHIRR-399](https://issues.apache.org/jira/browse/WHIRR-399)] - Move common script setup and script execution fork/join outside of ConfigureClusterAction and DestroyClusterAction
- [[WHIRR-400](https://issues.apache.org/jira/browse/WHIRR-400)] - Upgrade to jclouds 1.2.1
- [[WHIRR-401](https://issues.apache.org/jira/browse/WHIRR-401)] - Use regular instances for testing on aws-ec2
- [[WHIRR-402](https://issues.apache.org/jira/browse/WHIRR-402)] - Remove SaveHttpResponseTo and use the class provided by jclouds
- [[WHIRR-408](https://issues.apache.org/jira/browse/WHIRR-408)] - Upgrade elasticsearch to 0.18.2.
- [[WHIRR-411](https://issues.apache.org/jira/browse/WHIRR-411)] - put install\_git, install\_ruby scripts in core
- [[WHIRR-415](https://issues.apache.org/jira/browse/WHIRR-415)] - Let users specify the CDH release (cdh3u1, cdh3u2)
- [[WHIRR-416](https://issues.apache.org/jira/browse/WHIRR-416)] - Enable lazy image fetching when the image-id is known
- [[WHIRR-417](https://issues.apache.org/jira/browse/WHIRR-417)] - Allow users to choose their own jclouds modules with properties
- [[WHIRR-418](https://issues.apache.org/jira/browse/WHIRR-418)] - add ssh debug logs to tests
- [[WHIRR-419](https://issues.apache.org/jira/browse/WHIRR-419)] - Display how to connect to remote machines
- [[WHIRR-420](https://issues.apache.org/jira/browse/WHIRR-420)] - Document jclouds specific configuration options
- [[WHIRR-423](https://issues.apache.org/jira/browse/WHIRR-423)] - Refactor StartupProcess.cleanupFailedNodes
- [[WHIRR-426](https://issues.apache.org/jira/browse/WHIRR-426)] - Create a convention for naming clusters used for integration tests
- [[WHIRR-440](https://issues.apache.org/jira/browse/WHIRR-440)] - Unit tests improvements (less bound to external services)
- [[WHIRR-446](https://issues.apache.org/jira/browse/WHIRR-446)] - Upgrade all maven plugins to latest stable release

<a id="release-notes--new-feature-3"></a>

## New Feature

- [[WHIRR-49](https://issues.apache.org/jira/browse/WHIRR-49)] - Allow Whirr to use Chef for configuration management
- [[WHIRR-258](https://issues.apache.org/jira/browse/WHIRR-258)] - Add Ganglia as a service
- [[WHIRR-384](https://issues.apache.org/jira/browse/WHIRR-384)] - Add Mahout as a service
- [[WHIRR-385](https://issues.apache.org/jira/browse/WHIRR-385)] - Implement support for using nodeless, masterless Puppet to provision and run scripts
- [[WHIRR-398](https://issues.apache.org/jira/browse/WHIRR-398)] - Implement the execution of scripts on DestroyClusterAction

<a id="release-notes--test-2"></a>

## Test

- [[WHIRR-409](https://issues.apache.org/jira/browse/WHIRR-409)] - Add an integration test that shows that there is no overlap between install & configure scripts on the remote machine

<a id="release-notes--wish"></a>

## Wish

- [[WHIRR-405](https://issues.apache.org/jira/browse/WHIRR-405)] - Read PMC Branding Responsibilities

<a id="release-notes--release-notes-whirr-version-0.6.0"></a>

# Release Notes - Whirr™ - Version 0.6.0

<a id="release-notes--sub-task-3"></a>

## Sub-task

- [[WHIRR-341](https://issues.apache.org/jira/browse/WHIRR-341)] - Improve automatic OS image selection

<a id="release-notes--bug-6"></a>

## Bug

- [[WHIRR-249](https://issues.apache.org/jira/browse/WHIRR-249)] - Firewall authorization should be idempotent
- [[WHIRR-315](https://issues.apache.org/jira/browse/WHIRR-315)] - Temporary override Providers#withIds until jclouds beta-10 is out
- [[WHIRR-330](https://issues.apache.org/jira/browse/WHIRR-330)] - BYON doesn't work with HadoopConfigurationBuilder
- [[WHIRR-334](https://issues.apache.org/jira/browse/WHIRR-334)] - Support for CDH3u0 HBase
- [[WHIRR-363](https://issues.apache.org/jira/browse/WHIRR-363)] - ComputeCache redundantly creates ComputeServiceContexts
- [[WHIRR-364](https://issues.apache.org/jira/browse/WHIRR-364)] - [voldemort] 0.90.RC3 build artifact no longer available
- [[WHIRR-365](https://issues.apache.org/jira/browse/WHIRR-365)] - Too verbose command line interface logging

<a id="release-notes--improvement-6"></a>

## Improvement

- [[WHIRR-28](https://issues.apache.org/jira/browse/WHIRR-28)] - Add examples module
- [[WHIRR-311](https://issues.apache.org/jira/browse/WHIRR-311)] - Allow services to register new CLI commands
- [[WHIRR-319](https://issues.apache.org/jira/browse/WHIRR-319)] - Run rat & checkstyle before packaging
- [[WHIRR-320](https://issues.apache.org/jira/browse/WHIRR-320)] - Convert site documentation to xdoc format
- [[WHIRR-323](https://issues.apache.org/jira/browse/WHIRR-323)] - Allow user to specify a blobstore container to be used for caching local files
- [[WHIRR-327](https://issues.apache.org/jira/browse/WHIRR-327)] - Upgrade to jclouds 1.0.0
- [[WHIRR-331](https://issues.apache.org/jira/browse/WHIRR-331)] - Add the ability to specify tarball URLs that are local to the remote machine
- [[WHIRR-338](https://issues.apache.org/jira/browse/WHIRR-338)] - byon cluster with hostnames defined in /etc/hosts
- [[WHIRR-339](https://issues.apache.org/jira/browse/WHIRR-339)] - Allow to specify hbase-site.xml properties through cluster configuration file
- [[WHIRR-345](https://issues.apache.org/jira/browse/WHIRR-345)] - Add Hama service information to the website
- [[WHIRR-349](https://issues.apache.org/jira/browse/WHIRR-349)] - Retry if blobstore put fails
- [[WHIRR-350](https://issues.apache.org/jira/browse/WHIRR-350)] - Update Hama service to 0.3 version
- [[WHIRR-354](https://issues.apache.org/jira/browse/WHIRR-354)] - Upgrade to jclouds 1.1.0
- [[WHIRR-359](https://issues.apache.org/jira/browse/WHIRR-359)] - Document known limitations for Whirr 0.6.0
- [[WHIRR-361](https://issues.apache.org/jira/browse/WHIRR-361)] - refactor jclouds dependencies
- [[WHIRR-362](https://issues.apache.org/jira/browse/WHIRR-362)] - BlobStore contexts are redundantly created

<a id="release-notes--new-feature-4"></a>

## New Feature

- [[WHIRR-76](https://issues.apache.org/jira/browse/WHIRR-76)] - Support spot instances in python scripts
- [[WHIRR-240](https://issues.apache.org/jira/browse/WHIRR-240)] - [HBase] Enable support for HBase 0.90.x
- [[WHIRR-260](https://issues.apache.org/jira/browse/WHIRR-260)] - Support Spot Instances
- [[WHIRR-313](https://issues.apache.org/jira/browse/WHIRR-313)] - Add Hama as a Service
- [[WHIRR-326](https://issues.apache.org/jira/browse/WHIRR-326)] - Use jclouds provider metadata to help with cloud provider configuration

<a id="release-notes--wish-2"></a>

## Wish

- [[WHIRR-257](https://issues.apache.org/jira/browse/WHIRR-257)] - Remove outdated Python contrib

<a id="release-notes--release-notes-whirr-version-0.5.0"></a>

# Release Notes - Whirr - Version 0.5.0

<a id="release-notes--sub-task-4"></a>

## Sub-task

- [[WHIRR-277](https://issues.apache.org/jira/browse/WHIRR-277)] - Support multiple versions of ZooKeeper
- [[WHIRR-279](https://issues.apache.org/jira/browse/WHIRR-279)] - Create ClusterSpec aware BlobStoreContext factory class
- [[WHIRR-280](https://issues.apache.org/jira/browse/WHIRR-280)] - Create a blob cache that could be used for storing local files
- [[WHIRR-292](https://issues.apache.org/jira/browse/WHIRR-292)] - Separate Cassandra install and configuration scripts into more generic functions
- [[WHIRR-296](https://issues.apache.org/jira/browse/WHIRR-296)] - Separate Voldemort install and configuration scripts into more generic functions
- [[WHIRR-297](https://issues.apache.org/jira/browse/WHIRR-297)] - Separate ZooKeeper and ElasticSearch install and configuration scripts into more generic functions

<a id="release-notes--bug-7"></a>

## Bug

- [[WHIRR-172](https://issues.apache.org/jira/browse/WHIRR-172)] - Log warning for unrecognized service names
- [[WHIRR-253](https://issues.apache.org/jira/browse/WHIRR-253)] - ZooKeeper service should only authorize ingress to ZooKeeper instances
- [[WHIRR-268](https://issues.apache.org/jira/browse/WHIRR-268)] - whirr hangs when the file '$HOME/.ssh/known\_hosts' includes an obsolete identifier for a certain ip address host.
- [[WHIRR-271](https://issues.apache.org/jira/browse/WHIRR-271)] - Classpath needs to be quoted in whirr script
- [[WHIRR-274](https://issues.apache.org/jira/browse/WHIRR-274)] - Add wagon-ssh-external as a maven build extension
- [[WHIRR-298](https://issues.apache.org/jira/browse/WHIRR-298)] - Use all cluster spec properties for hash and equality
- [[WHIRR-312](https://issues.apache.org/jira/browse/WHIRR-312)] - Destroy instance removes all entries from the instances file except the one that is being terminated
- [[WHIRR-314](https://issues.apache.org/jira/browse/WHIRR-314)] - HBase integration test can fail due to Thrift server race

<a id="release-notes--improvement-7"></a>

## Improvement

- [[WHIRR-61](https://issues.apache.org/jira/browse/WHIRR-61)] - make more efficient use of ComputeServiceContext
- [[WHIRR-173](https://issues.apache.org/jira/browse/WHIRR-173)] - Add ClusterAction for generic script execution
- [[WHIRR-216](https://issues.apache.org/jira/browse/WHIRR-216)] - Improve error message if whirr.instance-templates left out of config
- [[WHIRR-222](https://issues.apache.org/jira/browse/WHIRR-222)] - Support multiple versions of Hadoop
- [[WHIRR-236](https://issues.apache.org/jira/browse/WHIRR-236)] - Update Configuration Guides with Recipe Info
- [[WHIRR-245](https://issues.apache.org/jira/browse/WHIRR-245)] - Clearly demarcate the user and service provider APIs
- [[WHIRR-246](https://issues.apache.org/jira/browse/WHIRR-246)] - Single place to store/load cluster state
- [[WHIRR-262](https://issues.apache.org/jira/browse/WHIRR-262)] - Services should not have to do reverse DNS lookups
- [[WHIRR-269](https://issues.apache.org/jira/browse/WHIRR-269)] - improve error msg "Key pair is encrypted"
- [[WHIRR-275](https://issues.apache.org/jira/browse/WHIRR-275)] - Improve firewall API for services
- [[WHIRR-278](https://issues.apache.org/jira/browse/WHIRR-278)] - Refactor ClusterSpec and extract InstanceTemplate class
- [[WHIRR-282](https://issues.apache.org/jira/browse/WHIRR-282)] - Set number of Hadoop slots based on hardware
- [[WHIRR-283](https://issues.apache.org/jira/browse/WHIRR-283)] - Whirr in 5 minutes
- [[WHIRR-284](https://issues.apache.org/jira/browse/WHIRR-284)] - Runurl should only be installed when needed
- [[WHIRR-288](https://issues.apache.org/jira/browse/WHIRR-288)] - Add blob store persistence for cluster state
- [[WHIRR-289](https://issues.apache.org/jira/browse/WHIRR-289)] - Display role names in list-cluster command
- [[WHIRR-291](https://issues.apache.org/jira/browse/WHIRR-291)] - Add "noop" role useful just for provisioning
- [[WHIRR-299](https://issues.apache.org/jira/browse/WHIRR-299)] - Recipe for BYON provider
- [[WHIRR-300](https://issues.apache.org/jira/browse/WHIRR-300)] - FAQ entry for noop role
- [[WHIRR-304](https://issues.apache.org/jira/browse/WHIRR-304)] - Upgrade to jclouds 1.0-beta-9c
- [[WHIRR-310](https://issues.apache.org/jira/browse/WHIRR-310)] - Improve Configuration Guide

<a id="release-notes--new-feature-5"></a>

## New Feature

- [[WHIRR-191](https://issues.apache.org/jira/browse/WHIRR-191)] - [CDH] Start other services based on CDH, not just HDFS and MR
- [[WHIRR-220](https://issues.apache.org/jira/browse/WHIRR-220)] - Support local tarball upload
- [[WHIRR-237](https://issues.apache.org/jira/browse/WHIRR-237)] - Add Voldemort as a service
- [[WHIRR-261](https://issues.apache.org/jira/browse/WHIRR-261)] - Add ElasticSearch as a service
- [[WHIRR-285](https://issues.apache.org/jira/browse/WHIRR-285)] - Add support for BYON

<a id="release-notes--task-2"></a>

## Task

- [[WHIRR-141](https://issues.apache.org/jira/browse/WHIRR-141)] - Create a logo

<a id="release-notes--test-3"></a>

## Test

- [[WHIRR-287](https://issues.apache.org/jira/browse/WHIRR-287)] - Script for running YCSB on HBase

<a id="release-notes--release-notes-whirr-version-0.4.0"></a>

# Release Notes - Whirr - Version 0.4.0

<a id="release-notes--sub-task-5"></a>

## Sub-task

- [[WHIRR-139](https://issues.apache.org/jira/browse/WHIRR-139)] - upgrade to version 1 of the "enforcer" plugin

<a id="release-notes--bug-8"></a>

## Bug

- [[WHIRR-170](https://issues.apache.org/jira/browse/WHIRR-170)] - Instances should be started in the order specified in the template
- [[WHIRR-201](https://issues.apache.org/jira/browse/WHIRR-201)] - [HBase] Integration test fails
- [[WHIRR-207](https://issues.apache.org/jira/browse/WHIRR-207)] - Handle curl timeouts better
- [[WHIRR-217](https://issues.apache.org/jira/browse/WHIRR-217)] - Log files should not be included in tarball or checked by RAT
- [[WHIRR-227](https://issues.apache.org/jira/browse/WHIRR-227)] - CDH and Hadoop integration tests are failing
- [[WHIRR-232](https://issues.apache.org/jira/browse/WHIRR-232)] - NPE for stopped instances on EC2
- [[WHIRR-234](https://issues.apache.org/jira/browse/WHIRR-234)] - Resource functions/install\_cdh\_hadoop.sh not found when running from the CLI
- [[WHIRR-235](https://issues.apache.org/jira/browse/WHIRR-235)] - fix whirr.provider in recipes/\*
- [[WHIRR-241](https://issues.apache.org/jira/browse/WHIRR-241)] - Update to use CDH3B4
- [[WHIRR-247](https://issues.apache.org/jira/browse/WHIRR-247)] - Add license headers to service install and configure scripts
- [[WHIRR-250](https://issues.apache.org/jira/browse/WHIRR-250)] - Ensure all libraries in binary distribution have associated licenses where stipulated
- [[WHIRR-251](https://issues.apache.org/jira/browse/WHIRR-251)] - Handle Apache cryptography requirements for release
- [[WHIRR-263](https://issues.apache.org/jira/browse/WHIRR-263)] - Default tarball not found for Cassandra (broken link in install\_cassandra.sh)
- [[WHIRR-264](https://issues.apache.org/jira/browse/WHIRR-264)] - JClouds is unable to do SSH on automatically selected images
- [[WHIRR-267](https://issues.apache.org/jira/browse/WHIRR-267)] - Update NOTICE and LICENSE files to mention 3rd party products

<a id="release-notes--improvement-8"></a>

## Improvement

- [[WHIRR-55](https://issues.apache.org/jira/browse/WHIRR-55)] - Users should be able to override an arbitrary Hadoop property before launch
- [[WHIRR-124](https://issues.apache.org/jira/browse/WHIRR-124)] - Upgrade to jclouds 1.0-beta-9
- [[WHIRR-167](https://issues.apache.org/jira/browse/WHIRR-167)] - Improve bootstrapping and configuration to be able to isolate and repair or evict failing nodes on EC2
- [[WHIRR-183](https://issues.apache.org/jira/browse/WHIRR-183)] - ZooKeeper Data Directory Cleanup
- [[WHIRR-186](https://issues.apache.org/jira/browse/WHIRR-186)] - [HBase] Add version support configurable in properties file
- [[WHIRR-193](https://issues.apache.org/jira/browse/WHIRR-193)] - Recipe for a HBase Cluster
- [[WHIRR-195](https://issues.apache.org/jira/browse/WHIRR-195)] - Display available roles instead of service names when running ./bin/whirr
- [[WHIRR-199](https://issues.apache.org/jira/browse/WHIRR-199)] - Add aliases for short role names like nn, jt, tt, dn, zk
- [[WHIRR-215](https://issues.apache.org/jira/browse/WHIRR-215)] - Add builder pattern to addRunUrl() call
- [[WHIRR-219](https://issues.apache.org/jira/browse/WHIRR-219)] - Support dynamic addition of services to CLI
- [[WHIRR-231](https://issues.apache.org/jira/browse/WHIRR-231)] - Update documentation after upgrade to jclouds 1.0-beta-9
- [[WHIRR-233](https://issues.apache.org/jira/browse/WHIRR-233)] - Change test properties to be less provider bound and improve TemplateBuilder defaults
- [[WHIRR-242](https://issues.apache.org/jira/browse/WHIRR-242)] - Update documentation for overriding locally supplied scripts
- [[WHIRR-244](https://issues.apache.org/jira/browse/WHIRR-244)] - Add package-level javadoc
- [[WHIRR-254](https://issues.apache.org/jira/browse/WHIRR-254)] - Document limitation that a role may only appear in one instance template group
- [[WHIRR-259](https://issues.apache.org/jira/browse/WHIRR-259)] - Disable configuration list handling for Hadoop properties
- [[WHIRR-265](https://issues.apache.org/jira/browse/WHIRR-265)] - Missing SVN EOL properties

<a id="release-notes--new-feature-6"></a>

## New Feature

- [[WHIRR-158](https://issues.apache.org/jira/browse/WHIRR-158)] - Allow users to log into clusters as themselves
- [[WHIRR-198](https://issues.apache.org/jira/browse/WHIRR-198)] - support user-defined images
- [[WHIRR-225](https://issues.apache.org/jira/browse/WHIRR-225)] - Support locally-supplied scripts
- [[WHIRR-226](https://issues.apache.org/jira/browse/WHIRR-226)] - Add the ability to destroy a cluster instance

<a id="release-notes--task-3"></a>

## Task

- [[WHIRR-129](https://issues.apache.org/jira/browse/WHIRR-129)] - Add Adrian Cole as a committer in the whirr pom.xml and site.
- [[WHIRR-248](https://issues.apache.org/jira/browse/WHIRR-248)] - Update to jclouds-1.0-beta9b

<a id="release-notes--release-notes-whirr-version-0.3.0"></a>

# Release Notes - Whirr - Version 0.3.0

<a id="release-notes--bug-9"></a>

## Bug

- [[WHIRR-123](https://issues.apache.org/jira/browse/WHIRR-123)] - Cassandra integration tests hang if whirr's scripts bucket is missing
- [[WHIRR-127](https://issues.apache.org/jira/browse/WHIRR-127)] - binary assembly from WHIRR-100 is not generated as part of release process
- [[WHIRR-128](https://issues.apache.org/jira/browse/WHIRR-128)] - In ec2 instances instead of public dns names a public ip address is resolved for the started master node which causes workers to not be able to connect back to the master
- [[WHIRR-137](https://issues.apache.org/jira/browse/WHIRR-137)] - Allow use of an arbitrary AMI on EC2
- [[WHIRR-146](https://issues.apache.org/jira/browse/WHIRR-146)] - Changing the mapred.child.java.opts value does not change the heap size from a default one.
- [[WHIRR-147](https://issues.apache.org/jira/browse/WHIRR-147)] - Regression on launching clusters from EC2
- [[WHIRR-151](https://issues.apache.org/jira/browse/WHIRR-151)] - Credentials not set correctly for Hadoop service configure step
- [[WHIRR-156](https://issues.apache.org/jira/browse/WHIRR-156)] - Cli script doesn't launch post-modularization
- [[WHIRR-159](https://issues.apache.org/jira/browse/WHIRR-159)] - Cassandra and ZooKeeper fail on Ubuntu on Rackspace
- [[WHIRR-162](https://issues.apache.org/jira/browse/WHIRR-162)] - DnsUtilTest fails when offline or for slow connections
- [[WHIRR-164](https://issues.apache.org/jira/browse/WHIRR-164)] - Tests fail if there is no ~/.ssh/id\_rsa keypair
- [[WHIRR-165](https://issues.apache.org/jira/browse/WHIRR-165)] - Hadoop integration tests fail due to WHIRR-160 changes
- [[WHIRR-175](https://issues.apache.org/jira/browse/WHIRR-175)] - ZooKeeper service does not honor instance roles
- [[WHIRR-179](https://issues.apache.org/jira/browse/WHIRR-179)] - [Hadoop] Guard $MOUNT/tmp mkdir call against existing directory
- [[WHIRR-180](https://issues.apache.org/jira/browse/WHIRR-180)] - ListClusterCommand.run throws a NullPointerException for unrecognized service names
- [[WHIRR-185](https://issues.apache.org/jira/browse/WHIRR-185)] - [ZooKeeper] Fix selection of instances for getHosts() call
- [[WHIRR-200](https://issues.apache.org/jira/browse/WHIRR-200)] - Cassandra integration test hangs
- [[WHIRR-201](https://issues.apache.org/jira/browse/WHIRR-201)] - HBase integration test fails
- [[WHIRR-204](https://issues.apache.org/jira/browse/WHIRR-204)] - CDH Hadoop integration test fails on Rackspace
- [[WHIRR-205](https://issues.apache.org/jira/browse/WHIRR-205)] - Override service.provider for integration tests
- [[WHIRR-209](https://issues.apache.org/jira/browse/WHIRR-209)] - bin/whirr fails on a new release
- [[WHIRR-210](https://issues.apache.org/jira/browse/WHIRR-210)] - Remove unneeded dependent libraries
- [[WHIRR-211](https://issues.apache.org/jira/browse/WHIRR-211)] - Fix checkstyle errors for 0.3.0

<a id="release-notes--improvement-9"></a>

## Improvement

- [[WHIRR-87](https://issues.apache.org/jira/browse/WHIRR-87)] - Parallelize Hadoop cluster creation
- [[WHIRR-115](https://issues.apache.org/jira/browse/WHIRR-115)] - Distribution should include documentation
- [[WHIRR-140](https://issues.apache.org/jira/browse/WHIRR-140)] - include KEYS file in release artifact.
- [[WHIRR-145](https://issues.apache.org/jira/browse/WHIRR-145)] - Add Whirr recipes for common configurations
- [[WHIRR-150](https://issues.apache.org/jira/browse/WHIRR-150)] - Allow retrieval of instance roles
- [[WHIRR-153](https://issues.apache.org/jira/browse/WHIRR-153)] - Add documentation for WHIRR-87 (Parallelize Hadoop cluster creation)
- [[WHIRR-154](https://issues.apache.org/jira/browse/WHIRR-154)] - cassandra: expose RPC port, as well
- [[WHIRR-155](https://issues.apache.org/jira/browse/WHIRR-155)] - Support multiple versions of Cassandra
- [[WHIRR-157](https://issues.apache.org/jira/browse/WHIRR-157)] - Remove service name property
- [[WHIRR-160](https://issues.apache.org/jira/browse/WHIRR-160)] - Improve SSH key diagnostics
- [[WHIRR-161](https://issues.apache.org/jira/browse/WHIRR-161)] - Check that both SSH keys belong to the same pair
- [[WHIRR-163](https://issues.apache.org/jira/browse/WHIRR-163)] - Support environment variable interpolation in configuration properties
- [[WHIRR-166](https://issues.apache.org/jira/browse/WHIRR-166)] - Improve docs regarding private keys
- [[WHIRR-174](https://issues.apache.org/jira/browse/WHIRR-174)] - Fix ZooKeeper to allow stand-alone mode setups
- [[WHIRR-178](https://issues.apache.org/jira/browse/WHIRR-178)] - [Hadoop] Guard useradd against existing user account
- [[WHIRR-181](https://issues.apache.org/jira/browse/WHIRR-181)] - Add descriptions for CLI command options
- [[WHIRR-187](https://issues.apache.org/jira/browse/WHIRR-187)] - [HBase] Change hbase.tmp.dir to be in line with Hadoop service
- [[WHIRR-190](https://issues.apache.org/jira/browse/WHIRR-190)] - Create /tmp in HDFS for Pig
- [[WHIRR-194](https://issues.apache.org/jira/browse/WHIRR-194)] - Update the list of supported services on the home page
- [[WHIRR-202](https://issues.apache.org/jira/browse/WHIRR-202)] - Improve instance template syntax checking
- [[WHIRR-203](https://issues.apache.org/jira/browse/WHIRR-203)] - General documentation improvements for 0.3.0
- [[WHIRR-206](https://issues.apache.org/jira/browse/WHIRR-206)] - [HBase] Extract strings to a HBaseServiceConstants interface

<a id="release-notes--new-feature-7"></a>

## New Feature

- [[WHIRR-25](https://issues.apache.org/jira/browse/WHIRR-25)] - Add HBase service
- [[WHIRR-117](https://issues.apache.org/jira/browse/WHIRR-117)] - Composable services
- [[WHIRR-176](https://issues.apache.org/jira/browse/WHIRR-176)] - Set AWS credentials in the local site file for Hadoop S3 access

<a id="release-notes--task-4"></a>

## Task

- [[WHIRR-196](https://issues.apache.org/jira/browse/WHIRR-196)] - Ensure integration tests pass on all supported providers

<a id="release-notes--test-4"></a>

## Test

- [[WHIRR-92](https://issues.apache.org/jira/browse/WHIRR-92)] - Add a benchmark for Hadoop clusters

<a id="release-notes--release-notes-whirr-version-0.2.0"></a>

# Release Notes - Whirr - Version 0.2.0

<a id="release-notes--bug-10"></a>

## Bug

- [[WHIRR-91](https://issues.apache.org/jira/browse/WHIRR-91)] - Add DISCLAIMER file to CLI JAR
- [[WHIRR-93](https://issues.apache.org/jira/browse/WHIRR-93)] - Fail on checkstyle violation
- [[WHIRR-97](https://issues.apache.org/jira/browse/WHIRR-97)] - Lucid is not stable on EC2
- [[WHIRR-101](https://issues.apache.org/jira/browse/WHIRR-101)] - Hadoop on EC2 does not use the /mnt partition
- [[WHIRR-102](https://issues.apache.org/jira/browse/WHIRR-102)] - unknown service NPEs cli, should print the bad service to console
- [[WHIRR-106](https://issues.apache.org/jira/browse/WHIRR-106)] - improve logging in whirr cli
- [[WHIRR-107](https://issues.apache.org/jira/browse/WHIRR-107)] - Test failing due to not matching Amazon Linux AMI on EC2
- [[WHIRR-108](https://issues.apache.org/jira/browse/WHIRR-108)] - Fix checkstyle and rat violations
- [[WHIRR-113](https://issues.apache.org/jira/browse/WHIRR-113)] - Hadoop cluster instances should all start in the same location
- [[WHIRR-114](https://issues.apache.org/jira/browse/WHIRR-114)] - Support + character in version number
- [[WHIRR-122](https://issues.apache.org/jira/browse/WHIRR-122)] - whirr site has two FAQ links
- [[WHIRR-126](https://issues.apache.org/jira/browse/WHIRR-126)] - Deployment process does not deploy required test JARs

<a id="release-notes--improvement-10"></a>

## Improvement

- [[WHIRR-52](https://issues.apache.org/jira/browse/WHIRR-52)] - Allow a Hadoop MapReduce job to be run against a Hadoop Service running on Rackspace Cloud Servers
- [[WHIRR-66](https://issues.apache.org/jira/browse/WHIRR-66)] - Upgrade to jclouds 1.0-beta-7
- [[WHIRR-89](https://issues.apache.org/jira/browse/WHIRR-89)] - Support maven 3 builds
- [[WHIRR-90](https://issues.apache.org/jira/browse/WHIRR-90)] - Scripts should be versioned
- [[WHIRR-103](https://issues.apache.org/jira/browse/WHIRR-103)] - add more to .gitignore
- [[WHIRR-104](https://issues.apache.org/jira/browse/WHIRR-104)] - print available services in cli help string
- [[WHIRR-105](https://issues.apache.org/jira/browse/WHIRR-105)] - Add version command to the CLI
- [[WHIRR-109](https://issues.apache.org/jira/browse/WHIRR-109)] - Unit tests fail if there is no private key found at ~/.ssh/id\_rsa
- [[WHIRR-110](https://issues.apache.org/jira/browse/WHIRR-110)] - Create client-side Hadoop configuration file during cluster launch
- [[WHIRR-112](https://issues.apache.org/jira/browse/WHIRR-112)] - Expand documentation

<a id="release-notes--new-feature-8"></a>

## New Feature

- [[WHIRR-73](https://issues.apache.org/jira/browse/WHIRR-73)] - Add a list command to the CLI
- [[WHIRR-100](https://issues.apache.org/jira/browse/WHIRR-100)] - Create a binary distribution of Whirr

<a id="release-notes--release-notes-whirr-version-0.1.0"></a>

# Release Notes - Whirr - Version 0.1.0

<a id="release-notes--sub-task-6"></a>

## Sub-task

- [[WHIRR-40](https://issues.apache.org/jira/browse/WHIRR-40)] - fill in getting started documentation - getting-started.confluence
- [[WHIRR-77](https://issues.apache.org/jira/browse/WHIRR-77)] - Document and implement release process
- [[WHIRR-78](https://issues.apache.org/jira/browse/WHIRR-78)] - Add KEYS file to distribution directory
- [[WHIRR-85](https://issues.apache.org/jira/browse/WHIRR-85)] - Publish Maven artifacts to http://repository.apache.org
- [[WHIRR-86](https://issues.apache.org/jira/browse/WHIRR-86)] - Update quick start documentation to work with release 0.1.0

<a id="release-notes--bug-11"></a>

## Bug

- [[WHIRR-4](https://issues.apache.org/jira/browse/WHIRR-4)] - hadoop-cloud push command invokes proxy creation
- [[WHIRR-37](https://issues.apache.org/jira/browse/WHIRR-37)] - Don't require manual installation of Apache RAT to compile
- [[WHIRR-48](https://issues.apache.org/jira/browse/WHIRR-48)] - Fix RAT warnings due to site files
- [[WHIRR-50](https://issues.apache.org/jira/browse/WHIRR-50)] - Cassandra POM should depend on top-level
- [[WHIRR-65](https://issues.apache.org/jira/browse/WHIRR-65)] - Workaround bug 331 in jclouds (Some EC2ComputeService operations fail for stopped instances)
- [[WHIRR-71](https://issues.apache.org/jira/browse/WHIRR-71)] - Only allow access to clusters from defined networks
- [[WHIRR-79](https://issues.apache.org/jira/browse/WHIRR-79)] - Hadoop service is broken
- [[WHIRR-82](https://issues.apache.org/jira/browse/WHIRR-82)] - Integration tests should not run on "mvn install"
- [[WHIRR-84](https://issues.apache.org/jira/browse/WHIRR-84)] - Log4j is missing from the CLI JAR

<a id="release-notes--improvement-11"></a>

## Improvement

- [[WHIRR-8](https://issues.apache.org/jira/browse/WHIRR-8)] - Create ant build for running EC2 unit tests
- [[WHIRR-9](https://issues.apache.org/jira/browse/WHIRR-9)] - Support additional security group option in hadoop-ec2 script
- [[WHIRR-10](https://issues.apache.org/jira/browse/WHIRR-10)] - Create setup.py for EC2 cloud scripts
- [[WHIRR-20](https://issues.apache.org/jira/browse/WHIRR-20)] - Generate RAT report
- [[WHIRR-21](https://issues.apache.org/jira/browse/WHIRR-21)] - Enforce source code style
- [[WHIRR-22](https://issues.apache.org/jira/browse/WHIRR-22)] - Separate unit and integration (system) tests
- [[WHIRR-23](https://issues.apache.org/jira/browse/WHIRR-23)] - Upgrade to jclouds 1.0-beta-6
- [[WHIRR-26](https://issues.apache.org/jira/browse/WHIRR-26)] - Allow script locations to be overridden
- [[WHIRR-31](https://issues.apache.org/jira/browse/WHIRR-31)] - Add Whirr quick start to README.txt and website (once it's live)
- [[WHIRR-32](https://issues.apache.org/jira/browse/WHIRR-32)] - Update POM to point to Apache RAT 0.8-SNAPSHOT
- [[WHIRR-34](https://issues.apache.org/jira/browse/WHIRR-34)] - Open up ports 50010 (JobTracker) and 50070 (NameNode) for the Hadoop Service
- [[WHIRR-38](https://issues.apache.org/jira/browse/WHIRR-38)] - Add core javadoc
- [[WHIRR-47](https://issues.apache.org/jira/browse/WHIRR-47)] - Create a Service factory
- [[WHIRR-51](https://issues.apache.org/jira/browse/WHIRR-51)] - Allow the Hadoop service to be run on Rackspace Cloud servers
- [[WHIRR-53](https://issues.apache.org/jira/browse/WHIRR-53)] - Adopt the standard Java SPI interface
- [[WHIRR-54](https://issues.apache.org/jira/browse/WHIRR-54)] - Implement service/cdh
- [[WHIRR-58](https://issues.apache.org/jira/browse/WHIRR-58)] - introduce naming consistency for cloud service providers
- [[WHIRR-64](https://issues.apache.org/jira/browse/WHIRR-64)] - Unify ClusterSpec and ServiceSpec
- [[WHIRR-70](https://issues.apache.org/jira/browse/WHIRR-70)] - decouple keypairs from the files that hold them
- [[WHIRR-75](https://issues.apache.org/jira/browse/WHIRR-75)] - Use Commons Configuration to manage cluster specs
- [[WHIRR-80](https://issues.apache.org/jira/browse/WHIRR-80)] - Clean up POM dependencies

<a id="release-notes--new-feature-9"></a>

## New Feature

- [[WHIRR-3](https://issues.apache.org/jira/browse/WHIRR-3)] - Add support for EBS storage on EC2
- [[WHIRR-5](https://issues.apache.org/jira/browse/WHIRR-5)] - Run namenode and jobtracker on separate EC2 instances
- [[WHIRR-6](https://issues.apache.org/jira/browse/WHIRR-6)] - Write a Rackspace cloud provider
- [[WHIRR-7](https://issues.apache.org/jira/browse/WHIRR-7)] - Add a ZooKeeper service to the cloud scripts
- [[WHIRR-27](https://issues.apache.org/jira/browse/WHIRR-27)] - Add Cassandra service
- [[WHIRR-33](https://issues.apache.org/jira/browse/WHIRR-33)] - Add a CLI

<a id="release-notes--task-5"></a>

## Task

- [[WHIRR-1](https://issues.apache.org/jira/browse/WHIRR-1)] - Import initial source code from Hadoop contrib
- [[WHIRR-2](https://issues.apache.org/jira/browse/WHIRR-2)] - Import initial Java source code
- [[WHIRR-19](https://issues.apache.org/jira/browse/WHIRR-19)] - Create project website
- [[WHIRR-29](https://issues.apache.org/jira/browse/WHIRR-29)] - Add target directories to svn ignore
- [[WHIRR-46](https://issues.apache.org/jira/browse/WHIRR-46)] - Release version 0.1.0

© 2010-2013
The Apache Software Foundation
- [Privacy Policy](http://maven.apache.org/privacy-policy.html)

Apache Whirr, Whirr, Apache, the Apache feather logo, and the Apache Whirr project logo are trademarks of The Apache Software Foundation.

---

<a id="known-limitations"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/known-limitations.html -->

<!-- page_index: 7 -->

<a id="known-limitations--whirr-know-limitations"></a>

## Whirr™ Know Limitations

We are striving to make each release as good as possible but there are still a set of
limitations that you should be aware of. The following issues are known to exist in the 0.8.0 release of Whirr.

- When launching an HBase 0.92.0 or 0.92.1 cluster, the regionserver may not launch properly if the master is not already up. Start the regionserver service again after the master is up. This is a bug in HBase, fixed in the upcoming 0.92.2.
- The order of the roles is significant. (e.g. hadoop-jobtracker+hadoop-namenode will try to start the jobtracker before starting the namenode)
- The "jclouds.aws-s3.endpoint" property is needed in order to use BlobCache with Amazon AWS in a region besides us-east-1. See [WHIRR-349](https://issues.apache.org/jira/browse/WHIRR-349#comment-13084590) for more details

---

<a id="supported-services-and-clouds"></a>

<!-- source_url: https://whirr.apache.org/docs/0.8.2/supported-services-and-clouds.html -->

<!-- page_index: 8 -->

<a id="supported-services-and-clouds--which-services-and-cloud-providers-are-supported-by-whirr"></a>

## Which Services and Cloud Providers Are Supported by Whirr™?

Whirr uses
[jclouds](http://code.google.com/p/jclouds/) for provisioning, so in principle it should support all the cloud providers that jclouds supports. The following
table shows the cloud provider and service combinations that have been tested.

| **Cloud provider** | **Cassandra** | **Hadoop** | **ZooKeeper** | **HBase** | **elasticsearch** | **Voldemort** | **Hama** |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Amazon EC2 | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Rackspace Cloud Servers | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

For development and local testing we are also supporting the BYON (bring your own nodes)
jclouds provider. Check the
*recipes* folder for a configuration sample.

<a id="supported-services-and-clouds--what-server-operating-systems-are-supported"></a>

### What server operating systems are supported?

Each release is tested by running the integration tests on Ubuntu Server 10.04. All setup
scripts should also work on Centos 5.x but we don't have a formal testing procedure in place
right now.

---
