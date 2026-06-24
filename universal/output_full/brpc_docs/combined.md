# Docs

## Navigation

- [Docs](#index)
- Other pages
  - [ASF](#asf)
  - [Performance benchmark](#benchmark)
  - [Blog](#blogs)
  - [bthread or not](#bthread-bthread-or-not)
  - [bthread](#bthread-bthread)
  - [Execution Queue](#bthread-execution-queue)
  - [bthread](#bthread)
  - [thread-local](#bthread-thread-local)
  - [builtin services](#builtin-services-buildin_services)
  - [connections](#builtin-services-connections)
  - [contention profiler](#builtin-services-contention_profiler)
  - [cpu profiler](#builtin-services-cpu_profiler)
  - [flags](#builtin-services-flags)
  - [heap profiler](#builtin-services-heap_profiler)
  - [Builtin Services](#builtin-services)
  - [rpcz](#builtin-services-rpcz)
  - [status](#builtin-services-status)
  - [vars](#builtin-services-vars)
  - [bvar c++](#bvar-bvar-c)
  - [bvar](#bvar-bvar)
  - [bvar](#bvar)
  - [bRPC Training Materials](#c-base-brpc-training-materials)
  - [FlatMap](#c-base-flatmap)
  - [C++ Base](#c-base)
  - [IOBuf](#c-base-iobuf)
  - [Streaming Log](#c-base-streaming-log)
  - [Access gRPC](#client-access-grpc)
  - [Access http:h2](#client-access-httph2)
  - [Access memcached](#client-access-memcached)
  - [Access redis](#client-access-redis)
  - [Access thrift](#client-access-thrift)
  - [Access UB](#client-access-ub)
  - [Backup request](#client-backup-request)
  - [Basics](#client-basics)
  - [Combo channels](#client-combo-channels)
  - [Dummy server](#client-dummy-server)
  - [Error code](#client-error-code)
  - [Client](#client)
  - [Streaming RPC](#client-streaming-rpc)
  - [Committer Guide](#community-committer)
  - [Committers](#community-committers)
  - [Community](#community-community)
  - [Contribute Guide](#community-contributing)
  - [Community](#community)
  - [Mailing List](#community-mailing_list)
  - [Monthly Meeting](#community-monthly-meeting)
  - [On Call](#community-on-call)
  - [CVE-2023-31039](#community-security-cve-2023-31039-bugfix)
  - [Security](#community-security)
  - [Download](#downloadbrpc)
  - [FAQ](#faq)
  - [Getting started](#getting_started)
  - [bRPC overview](#overview)
  - [Atomic instructions](#rpc-in-depth-atomic-instructions)
  - [bthread_id](#rpc-in-depth-bthread_id)
  - [Consistent Hashing](#rpc-in-depth-consistent-hashing)
  - [RPC in depth](#rpc-in-depth)
  - [IO](#rpc-in-depth-io)
  - [Load Balancing](#rpc-in-depth-load-balancing)
  - [Locality-aware](#rpc-in-depth-locality-aware)
  - [Memory Management](#rpc-in-depth-memory-management)
  - [New Protocol](#rpc-in-depth-new-protocol)
  - [Threading Overview](#rpc-in-depth-threading-overview)
  - [Timer keeping](#rpc-in-depth-timer-keeping)
  - [Auto ConcurrencyLimiter](#server-auto-concurrencylimiter)
  - [Avalanche](#server-avalanche)
  - [Basics](#server-basics)
  - [Debug server issues](#server-debug-server-issues)
  - [Server](#server)
  - [json2pb](#server-json2pb)
  - [Media Server](#server-media-server)
  - [Serve gRPC](#server-serve-grpc)
  - [Serve http:h2](#server-serve-httph2)
  - [Serve Nshead](#server-serve-nshead)
  - [Serve thrift](#server-serve-thrift)
  - [Server push](#server-server-push)
  - [benchmark_http](#tools-benchmark_http)
  - [Tools](#tools)
  - [parallel_http](#tools-parallel_http)
  - [rpc_press](#tools-rpc_press)
  - [rpc_replay](#tools-rpc_replay)
  - [rpc_view](#tools-rpc_view)
  - [Use cases inside Baidu](#use-cases-inside-baidu)
  - [百度地图api入口](#use-cases-inside-baidu-use-case1)
  - [联盟DSP](#use-cases-inside-baidu-use-case2)
  - [ELF学习框架](#use-cases-inside-baidu-use-case3)
  - [云平台代理服务](#use-cases-inside-baidu-use-case4)
  - [Users](#users)

## Content

<a id="index"></a>

<!-- source_url: https://brpc.apache.org/docs/ -->

<!-- page_index: 1 -->

# Docs

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Docs)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Docs

The official bRPC documentation.

---

##### [bRPC overview](#overview)

The basic description of bRPC.

##### [Download](#downloadbrpc)

Download bRPC Release Version.

##### [Getting started](#getting_started)

Read getting started for building steps and play with [examples](https://github.com/apache/brpc/tree/master/example).

##### [Performance benchmark](#benchmark)

A comparison between brpc and other implementations.

##### [bvar](#bvar)

Bvar, a high performance counters in multi-threaded applications.

##### [bthread](#bthread)

Bthread, a high performance M:N thread library.

##### [C++ Base](#c-base)

Learn about C++ Base.

##### [Client](#client)

Learn how to use bRPC client.

##### [Server](#server)

Learn how to use bRPC server.

##### [Builtin Services](#builtin-services)

Learn about bRPC builtin services.

##### [Tools](#tools)

Learn about bRPC tools.

##### [RPC in depth](#rpc-in-depth)

Learn about bRPC in depth.

##### [Community](#community)

About bRPC community

##### [ASF](#asf)

About Apache Software Foundation.

##### [Users](#users)

Providing your info on [Wanted: who’s using bRPC](https://github.com/apache/brpc/issues/1640) to help improving bRPC better

##### [Use cases inside Baidu](#use-cases-inside-baidu)

Learn about bRPC use cases inside Baidu.

##### [FAQ](#faq)

bRPC Issues.

##### [Blog](#blogs)

About bRPC blogs.

Last modified November 4, 2022: [Changing the directory order (ca4c7980a)](https://github.com/apache/brpc-website/commit/ca4c7980a98ea4dba158bc17b91d1466cba46fac)

---

<a id="asf"></a>

<!-- source_url: https://brpc.apache.org/docs/asf/ -->

<!-- page_index: 2 -->

# ASF

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/ASF/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=ASF)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# ASF

About Apache Software Foundation.

<a id="asf--apache-software-foundation"></a>

## Apache Software Foundation

- [Foundation](https://www.apache.org/)
- [License](https://www.apache.org/licenses/)
- [Security](https://www.apache.org/security/)
- [Events](https://www.apache.org/events/current-event)
- [Sponsorship](https://www.apache.org/foundation/sponsorship.html)
- [Privacy](https://privacy.apache.org/policies/privacy-policy-public.html)
- [Thanks](https://www.apache.org/foundation/thanks.html)

Last modified November 15, 2022: [Update index.md (5373e25cf)](https://github.com/apache/brpc-website/commit/5373e25cf7272a5534df6e82f40ea9dacb3e54c6)

---

<a id="benchmark"></a>

<!-- source_url: https://brpc.apache.org/docs/benchmark/ -->

<!-- page_index: 3 -->

# Performance benchmark

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/benchmark/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Performance%20benchmark)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [UB](#benchmark--ub)
- [hulu-pbrpc](#benchmark--hulu-pbrpc)
- [brpc](#benchmark--brpc)
- [sofa-pbrpc](#benchmark--sofa-pbrpc)
- [apache thrift](#benchmark--apache-thrift)
- [gRPC](#benchmark--grpc)

- [环境](#benchmark--section)
- [配置](#benchmark--section)
- [同机单client→单server在不同请求下的QPS（越高越好）](#benchmark--client-server-qps)
- [同机单client→单server在不同线程数下的QPS（越高越好）](#benchmark--client-server-qps)
- [同机单client→单server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）](#benchmark--client-server-qps-cdfbuiltin-servicesvars)
- [跨机多client→单server的QPS（越高越好）](#benchmark--client-server-qps)
- [跨机多client→单server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）](#benchmark--client-server-qps-cdfbuiltin-servicesvars)
- [跨机多client→多server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）](#benchmark--client-server-qps-cdfbuiltin-servicesvars)
- [跨机多client→多server→多server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）](#benchmark--client-server-server-qps-cdfbuiltin-servicesvars)

# Performance benchmark

A comparison between brpc and other implementations.

<a id="benchmark--section"></a>

# 序言

在多核的前提下，性能和线程是紧密联系在一起的。线程间的跳转对高频IO操作的性能有决定性作用: 一次跳转意味着至少3-20微秒的延时，由于每个核心的L1 cache独立（我们的cpu L2 cache也是独立的），随之而来是大量的cache miss，一些变量的读取、写入延时会从纳秒级上升几百倍至微秒级: 等待cpu把对应的cacheline同步过来。有时这带来了一个出乎意料的结果，当每次的处理都很简短时，一个多线程程序未必比一个单线程程序更快。因为前者可能在每次付出了大的切换代价后只做了一点点“正事”，而后者在不停地做“正事”。不过单线程也是有代价的，它工作良好的前提是“正事”都很快，否则一旦某次变慢就使后续的所有“正事”都被延迟了。在一些处理时间普遍较短的程序中，使用（多个不相交的）单线程能最大程度地”做正事“，由于每个请求的处理时间确定，延时表现也很稳定，各种http server正是这样。但我们的检索服务要做的事情可就复杂多了，有大量的后端服务需要访问，广泛存在的长尾请求使每次处理的时间无法确定，排序策略也越来越复杂。如果还是使用（多个不相交的）单线程的话，一次难以预计的性能抖动，或是一个大请求可能导致后续一堆请求被延迟。

为了避免请求之间相互影响，请求级的线程跳转是brpc必须付出的代价，我们能做的是使[线程跳转最优化](https://brpc.apache.org/docs/rpc-in-depth/io#the-full-picture)。不过，对服务的性能测试还不能很好地体现这点。测试中的处理往往极为简单，使得线程切换的影响空前巨大，通过控制多线程和单线程处理的比例，我们可以把一个测试服务的qps从100万到500万操纵自如（同机），这损伤了性能测试结果的可信度。要知道，真实的服务并不是在累加一个数字，或者echo一个字符串，一个qps几百万的echo程序没有指导意义。鉴于此，在发起性能测试一年后（15年底），在brpc又经历了1200多次改动后，我们需要review所有的测试，加强其中的线程因素，以获得对真实场景有明确意义的结果。具体来说:

- 请求不应等长，要有长尾。这能考察RPC能否让请求并发，否则一个慢请求会影响大量后续请求。
- 要有多级server的场景。server内用client访问下游server，这能考察server和client的综合表现。
- 要有一个client访问多个server的场景。这能考察负载均衡是否足够并发，真实场景中很少一个client只访问一个server。

我们希望这套测试场景对其他服务的性能测试有借鉴意义。

<a id="benchmark--section"></a>

# 测试目标

<a id="benchmark--ub"></a>

## UB

百度在08年开发的RPC框架，在百度产品线广泛使用，已被brpc代替。UB的每个请求独占一个连接(连接池)，在大规模服务中每台机器都需要保持大量的连接，限制了其使用场景，像百度的分布式系统没有用UB。UB只支持nshead+mcpack协议，也没怎么考虑扩展性，所以增加新协议和新功能往往要调整大段代码，在实践中大部分人“知难而退”了。UB缺乏调试和运维接口，服务的运行状态对用户基本是黑盒，只能靠低效地打日志来追踪问题，服务出现问题时常要拉上维护者一起排查，效率很低。UB有多个变种:

- ubrpc: 百度在10年基于UB开发的RPC框架，用.idl文件(类似.proto)描述数据的schema，而不是手动打包。这个RPC有被使用，但不广泛。

- nova\_pbrpc: 百度网盟团队在12年基于UB开发的RPC框架，用protobuf代替mcpack作为序列化方法，协议是nshead + user’s protobuf。
- public\_pbrpc: 百度在13年初基于UB开发的RPC框架，用protobuf代替mcpack作为序列化方法，但协议与nova\_pbrpc不同，大致是nshead + meta protobuf。meta protobuf中有个string字段包含user’s protobuf。由于用户数据要序列化两次，这个RPC的性能很差，没有被推广开来。

我们以在百度网盟团队广泛使用的nova\_pbrpc为UB的代表。测试时其代码为r10500。早期的UB支持CPOOL和XPOOL，分别使用[select](http://linux.die.net/man/2/select)和[leader-follower模型](http://kircher-schwanninger.de/michael/publications/lf.pdf)，后来提供了EPOLL，使用[epoll](http://man7.org/linux/man-pages/man7/epoll.7.html)处理多路连接。鉴于产品线大都是用EPOLL模型，我们的UB配置也使用EPOLL。UB只支持[连接池](#client-basics--connection-type)，结果用“**ubrpc\_mc**“指代（mc代表"multiple
connection”）。虽然这个名称不太准确（见上文对ubrpc的介绍），但在本文的语境下，请默认ubrpc = UB。

<a id="benchmark--hulu-pbrpc"></a>

## hulu-pbrpc

百度在13年基于saber(kylin变种)和protobuf实现的RPC框架，hulu在多线程实现上有较多问题，已被brpc代替，测试时其代码为`pbrpc_2-0-15-27959_PD_BL`。hulu-pbrpc只支持单连接，结果用“**hulu-pbrpc**“指代。

<a id="benchmark--brpc"></a>

## brpc

INF在2014年底开发至今的rpc产品，支持百度内所有协议（不限于protobuf），并第一次统一了百度主要分布式系统和业务线的RPC框架。测试时代码为r31906。brpc既支持单连接也支持连接池，前者的结果用”**baidu-rpc**“指代，后者用“**baidu-rpc\_mc**“指代。

<a id="benchmark--sofa-pbrpc"></a>

## sofa-pbrpc

百度大搜团队在13年基于boost::asio和protobuf实现的RPC框架，有多个版本，咨询相关同学后，确认ps/opensource下的和github上的较新，且会定期同步。故测试使用使用ps/opensource下的版本。测试时其代码为`sofa-pbrpc_1-0-2_BRANCH`。sofa-pbrpc只支持单连接，结果用“**sofa-pbrpc**”指代。

<a id="benchmark--apache-thrift"></a>

## apache thrift

thrift是由facebook最早在07年开发的序列化方法和rpc框架，包含独特的序列化格式和IDL，支持很多编程语言。开源后改名[apache thrift](https://thrift.apache.org/)，fb自己有一个[fbthrift分支](https://github.com/facebook/fbthrift)，我们使用的是apache thrift。测试时其代码为`thrift_0-9-1-400_PD_BL`。thrift的缺点是: 代码看似分层清晰，client和server选择很多，但没有一个足够通用，每个server实现都只能解决很小一块场景，每个client都线程不安全，实际使用很麻烦。由于thrift没有线程安全的client，所以每个线程中都得建立一个client，使用独立的连接。在测试中thrift其实是占了其他实现的便宜: 它的client不需要处理多线程问题。thrift的结果用”**thrift\_mc**“指代。

<a id="benchmark--grpc"></a>

## gRPC

由google开发的rpc框架，使用http/2和protobuf 3.0，测试时其代码为<https://github.com/grpc/grpc/tree/release-0_11>。gRPC并不是stubby，定位更像是为了推广http/2和protobuf 3.0，但鉴于很多人对它的表现很感兴趣，我们也（很麻烦地）把它加了进来。gRPC的结果用”**grpc**“指代。

<a id="benchmark--section"></a>

# 测试方法

如序言中解释的那样，性能数字有巨大的调整空间。这里的关键在于，我们对RPC的底线要求是什么，脱离了这个底线，测试中的表现就严重偏离真实环境中的了。

这个底线我们认为是**RPC必须能处理长尾**。

在百度的环境中，这是句大白话，哪个产品线，哪个系统没有长尾呢？作为承载大部分服务的RPC框架自然得处理好长尾，减少长尾对正常请求的影响。但在实现层面，这个问题对设计的影响太大了。如果测试中没有长尾，那么RPC实现就可以假设每个请求都差不多快，这时候最优的方法是用多个线程独立地处理请求。由于没有上下文切换和cache一致性同步，程序的性能会显著高于多个线程协作时的表现。

比如简单的echo程序，处理一个请求只需要200-300纳秒，单个线程可以达到300-500万的吞吐。但如果多个线程协作，即使在极其流畅的系统中，也要付出3-5微秒的上下文切换代价和1微秒的cache同步代价，这还没有考虑多个线程间的其他互斥逻辑，一般来说单个线程的吞吐很难超过10万，即使24核全部用满，吞吐也只有240万，不及一个线程。这正是以http server为典型的服务选用[单线程模型](#rpc-in-depth-threading-overview--single-threaded-reactorhttpenwikipediaorgwikireactor_pattern)的原因（多个线程独立运行eventloop）: 大部分http请求的处理时间是可预测的，对下游的访问也不会有任何阻塞代码。这个模型可以最大化cpu利用率，同时提供可接受的延时。

多线程付出这么大的代价是为了**隔离请求间的影响**。一个计算复杂或索性阻塞的过程不会影响到其他请求，1%的长尾最终只会影响到1%的性能。而多个独立的线程是保证不了这点的，一个请求进入了一个线程就等于“定了终生”，如果前面的请求慢了一下，那也只能跟着慢了。1%的长尾会影响远超1%的请求，最终表现不佳。换句话说，乍看上去多线程模型“慢”了，但在真实应用中反而会获得更好的综合性能。

延时能精确地体现出长尾的干扰作用，如果普通请求的延时没有被长尾请求干扰，就说明RPC成功地隔离了请求。而QPS无法体现这点，只要CPU都在忙，即使一个正常请求进入了挤满长尾的队列而被严重延迟，最终的QPS也变化不大。为了测量长尾的干扰作用，我们在涉及到延时的测试中都增加了1%的长尾请求。

<a id="benchmark--section"></a>

# 开始测试

<a id="benchmark--section"></a>

## 环境

性能测试使用的机器配置为:

- 单机1: CPU开超线程24核，E5-2620 @ 2.00GHz；64GB内存；OS linux 2.6.32\_1-15-0-0
- 多机1（15台+8台）: CPU均未开超线程12核，其中15台的CPU为E5-2420 @ 1.90GHz.，64GB内存，千兆网卡，无法开启多队列。其余8台为E5-2620 2.0GHz，千兆网卡，绑定多队列到前8个核。这些长期测试机器比较杂，跨了多个机房，测试中延时在1ms以上的就是这批机器。
- 多机2（30台）: CPU未开超线程12核，E5-2620 v3 @ 2.40GHz.；96GB内存；OS linux 2.6.32\_1-17-0-0；万兆网卡，绑定多队列到前8个核。这是临时借用的新机器，配置非常好，都在广州机房，延时非常短，测试中延时在几百微秒的就是这批机器。

下面所有的曲线图是使用brpc开发的dashboard程序绘制的，去掉路径后可以看到和所有brpc
server一样的[内置服务](#builtin-services-buildin_services)。

<a id="benchmark--section"></a>

## 配置

如无特殊说明，所有测试中的配置只是数量差异（线程数，请求大小，client个数etc），而不是模型差异。我们确保用户看到的qps和延时是同一个场景的不同维度，而不是无法统一的两个场景。

所有RPC server都配置了24个工作线程，这些线程一般运行用户的处理逻辑。关于每种RPC的特殊说明:

- UB: 配置了12个reactor线程，使用EPOOL模型。连接池限制数配置为线程个数（24）
- hulu-pbrpc: 额外配置了12个IO线程。这些线程会处理fd读取，请求解析等任务。hulu有个“共享队列“的配置项，默认不打开，作用是把fd静态散列到多个线程中，由于线程间不再争抢，hulu的qps会显著提高，但会明显地被长尾影响（原因见[测试方法](#benchmark--section)）。考虑到大部分使用者并不会去改配置，我们也选择不打开。
- thrift: 额外配置了12个IO线程。这些线程会处理fd读取，请求解析等任务。thrift的client不支持多线程，每个线程得使用独立的client，连接也都是分开的。
- sofa-pbrpc: 按照sofa同学的要求，把io\_service\_pool\_size配置为24，work\_thread\_num配置为1。大概含义是使用独立的24组线程池，每组1个worker thread。和hulu不打开“共享队列”时类似，这个配置会显著提高sofa-pbrpc的QPS，但同时使它失去了处理长尾的能力。如果你在真实产品中使用，我们不建议这个配置。（而应该用io\_service\_pool\_size=1, work\_thread\_num=24)
- brpc: 尽管brpc的client运行在bthread中时会获得10%~20%的QPS提升和更低的延时，但测试中的client都运行统一的pthread中。

所有的RPC client都以多个线程同步方式发送，这种方法最接近于真实系统中的情况，在考察QPS时也兼顾了延时因素。

一种流行的方案是client不停地往连接中写入数据看server表现，这个方法的弊端在于: server一下子能读出大量请求，不同RPC的比拼变成了“for循环执行用户代码”的比拼，而不是分发请求的效率。在真实系统中server很少能同时读到超过4个请求。这个方法也完全放弃了延时，client其实是让server陷入了雪崩时才会进入的状态，所有请求都因大量排队而超时了。

<a id="benchmark--client-server-qps"></a>

## 同机单client→单server在不同请求下的QPS（越高越好）

本测试运行在[单机1](#benchmark--section)上。图中的数值均为用户数据的字节数，实际的请求尺寸还要包括协议头，一般会增加40字节左右。

（X轴是用户数据的字节数，Y轴是对应的QPS）

![img](assets/images/qps-vs-reqsize_622c1c2cf72b127f.png)

以\_mc结尾的曲线代表client和server保持多个连接（线程数个），在本测试中会有更好的表现。

**分析**

<a id="benchmark--client-server-qps"></a>

## 同机单client→单server在不同线程数下的QPS（越高越好）

本测试运行在[单机1](#benchmark--section)上。

（X轴是线程数，Y轴是对应的QPS）

![img](assets/images/qps-vs-threadnum_282b01e3c680ec24.png)

**分析**

brpc: 随着发送线程增加，QPS在快速增加，有很好的多线程扩展性。

UB和thrift: 8个线程下高于brpc，但超过8个线程后被brpc迅速超过，thrift继续“平移”，UB出现了明显下降。

gRPC，hulu-pbrpc，sofa-pbrpc: 几乎重合，256个线程时相比1个线程时只有1倍的提升，多线程扩展性不佳。

<a id="benchmark--client-server-qps-cdfbuiltin-servicesvars"></a>

## 同机单client→单server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）

本测试运行在[单机1](#benchmark--section)上。考虑到不同RPC的处理能力，我们选择了一个较低、在不少系统中会达到的的QPS: 1万。

本测试中有1%的长尾请求耗时5毫秒，长尾请求的延时不计入结果，因为我们考察的是普通请求是否被及时处理了。

（X轴是延时（微秒），Y轴是小于X轴延时的请求比例）

![img](assets/images/latency-cdf_a4ab3410749594b2.png)

**分析**

- brpc: 平均延时短，几乎没有被长尾影响。
- UB和thrift: 平均延时比brpc高1毫秒，受长尾影响不大。
- hulu-pbrpc: 走向和UB和thrift类似，但平均延时进一步增加了1毫秒。
- gRPC : 初期不错，到长尾区域后表现糟糕，直接有一部分请求超时了。（反复测试都是这样，像是有bug）
- sofa-pbrpc: 30%的普通请求（上图未显示）被长尾严重干扰。

<a id="benchmark--client-server-qps"></a>

## 跨机多client→单server的QPS（越高越好）

本测试运行在[多机1](#benchmark--section)上。

（X轴是client数，Y轴是对应的QPS）

![img](assets/images/qps-vs-multi-client_fe6beb082be42fce.png)

**分析**

- brpc: 随着cilent增加，server的QPS在快速增加，有不错的client扩展性。
- sofa-pbrpc: 随着client增加，server的QPS也在快速增加，但幅度不如brpc，client扩展性也不错。从16个client到32个client时的提升较小。
- hulu-pbrpc: 随着client增加，server的QPS在增加，但幅度进一步小于sofa-pbrpc。
- UB: 增加client几乎不能增加server的QPS。
- thrift: 平均QPS低于UB，增加client几乎不能增加server的QPS。
- gRPC: 垫底、增加client几乎不能增加server的QPS。

<a id="benchmark--client-server-qps-cdfbuiltin-servicesvars"></a>

## 跨机多client→单server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）

本测试运行在[多机1](#benchmark--section)上。负载均衡算法为round-robin或RPC默认提供的。由于有32个client且一些RPC的单client能力不佳，我们为每个client仅设定了2500QPS，这是一个真实业务系统能达到的数字。

本测试中有1%的长尾请求耗时15毫秒，长尾请求的延时不计入结果，因为我们考察的是普通请求是否被及时处理了。

（X轴是延时（微秒），Y轴是小于X轴延时的请求比例）

![img](assets/images/multi-client-latency-cdf_62f1dafece9b8147.png)

**分析**

- brpc: 平均延时短，几乎没有被长尾影响。
- UB和thrift: 平均延时短，受长尾影响小，平均延时高于brpc
- sofa-pbrpc: 14%的普通请求被长尾严重干扰。
- hulu-pbrpc: 15%的普通请求被长尾严重干扰。
- gRPC: 已经完全失控，非常糟糕。

<a id="benchmark--client-server-qps-cdfbuiltin-servicesvars"></a>

## 跨机多client→多server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）

本测试运行在[多机2](#benchmark--section)上。20台每台运行4个client，多线程同步访问10台server。负载均衡算法为round-robin或RPC默认提供的。由于gRPC访问多server较麻烦且有很大概率仍表现不佳，这个测试不包含gRPC。

本测试中有1%的长尾请求耗时10毫秒，长尾请求的延时不计入结果，因为我们考察的是普通请求是否被及时处理了。

（X轴是延时（微秒），Y轴是小于X轴延时的请求比例）

![img](assets/images/multi-server-latency-cdf_95db561a43fa27be.png)

**分析**

- brpc和UB: 平均延时短，几乎没有被长尾影响。
- thrift: 平均延时显著高于brpc和UB。
- sofa-pbrpc: 2.5%的普通请求被长尾严重干扰。
- hulu-pbrpc: 22%的普通请求被长尾严重干扰。

<a id="benchmark--client-server-server-qps-cdfbuiltin-servicesvars"></a>

## 跨机多client→多server→多server在固定QPS下的延时[CDF](#builtin-services-vars--section)（越左越好，越直越好）

本测试运行在[多机2](#benchmark--section)上。14台每台运行4个client，多线程同步访问8台server，这些server还会同步访问另外8台server。负载均衡算法为round-robin或RPC默认提供的。由于gRPC访问多server较麻烦且有很大概率仍表现不佳，这个测试不包含gRPC。

本测试中有1%的长尾请求耗时10毫秒，长尾请求的延时不计入结果，因为我们考察的是普通请求是否被及时处理了。

（X轴是延时（微秒），Y轴是小于X轴延时的请求比例）

![img](assets/images/twolevel-server-latency-cdf_d2ca14544c611009.png)

**分析**

- brpc: 平均延时短，几乎没有被长尾影响。
- UB: 平均延时短，长尾区域略差于brpc。
- thrift: 平均延时显著高于brpc和UB。
- sofa-pbrpc: 17%的普通请求被长尾严重干扰，其中2%的请求延时极长。
- hulu-pbrpc: 基本消失在视野中，已无法正常工作。

<a id="benchmark--section"></a>

# 结论

brpc: 在吞吐，平均延时，长尾处理上都表现优秀。

UB: 平均延时和长尾处理的表现都不错，吞吐的扩展性较差，提高线程数和client数几乎不能提升吞吐。

thrift: 单机的平均延时和吞吐尚可，多机的平均延时明显高于brpc和UB。吞吐的扩展性较差，提高线程数和client数几乎不能提升吞吐。

sofa-pbrpc: 处理小包的吞吐尚可，大包的吞吐显著低于其他RPC，延时受长尾影响很大。

hulu-pbrpc: 单机表现和sofa-pbrpc类似，但多机的延时表现极差。

gRPC: 几乎在所有参与的测试中垫底，可能它的定位是给google cloud platform的用户提供一个多语言，对网络友好的实现，性能还不是要务。

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="blogs"></a>

<!-- source_url: https://brpc.apache.org/docs/blogs/ -->

<!-- page_index: 4 -->

# Blog

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/blogs/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Blog)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Blog

About bRPC blogs.

---

##### [Release](https://brpc.apache.org/docs/blogs/releases/)

Last modified November 7, 2022: [add ASF page (f7462e073)](https://github.com/apache/brpc-website/commit/f7462e07303f64f538630de63f8b75373fa3f500)

---

<a id="bthread-bthread-or-not"></a>

<!-- source_url: https://brpc.apache.org/docs/bthread/bthread-or-not/ -->

<!-- page_index: 5 -->

# bthread or not

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bthread/bthread%20or%20not/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bthread%20or%20not)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# bthread or not

Where should I choose to use bthread?

brpc提供了[异步接口](#client-basics--asynchronous-call)，所以一个常见的问题是：我应该用异步接口还是bthread？

短回答：延时不高时你应该先用简单易懂的同步接口，不行的话用异步接口，只有在需要多核并行计算时才用bthread。

<a id="bthread-bthread-or-not--section"></a>

# 同步或异步

异步即用回调代替阻塞，有阻塞的地方就有回调。虽然在javascript这种语言中回调工作的很好，接受度也非常高，但只要用过，就会发现这和我们需要的回调是两码事，这个区别不是[lambda](https://en.wikipedia.org/wiki/Anonymous_function)，也不是[future](https://en.wikipedia.org/wiki/Futures_and_promises)，而是javascript是单线程的。javascript的回调放到多线程下可能没有一个能跑过，竞争太多，单线程的同步方法和多线程的同步方法是完全不同的。那是不是服务能搞成类似的形式呢？多个线程，每个都是独立的eventloop。可以，ub**a**server就是（注意带a)，但实际效果糟糕，因为阻塞改回调可不简单，当阻塞发生在循环，条件分支，深层子函数中时，改造特别困难，况且很多老代码、第三方代码根本不可能去改造。结果是代码中会出现不可避免的阻塞，导致那个线程中其他回调都被延迟，流量超时，server性能不符合预期。如果你说，”我想把现在的同步代码改造为大量的回调，除了我其他人都看不太懂，并且性能可能更差了”，我猜大部分人不会同意。别被那些鼓吹异步的人迷惑了，他们写的是从头到尾从下到上全异步且不考虑多线程的代码，和你要写的完全是两码事。

brpc中的异步和单线程的异步是完全不同的，异步回调会运行在与调用处不同的线程中，你会获得多核扩展性，但代价是你得意识到多线程问题。你可以在回调中阻塞，只要线程够用，对server整体的性能并不会有什么影响。不过异步代码还是很难写的，所以我们提供了[组合访问](https://brpc.apache.org/docs/client/combo-channels)来简化问题，通过组合不同的channel，你可以声明式地执行复杂的访问，而不用太关心其中的细节。

当然，延时不长，qps不高时，我们更建议使用同步接口，这也是创建bthread的动机：维持同步代码也能提升交互性能。

**判断使用同步或异步**：计算qps \* latency(in seconds)，如果和cpu核数是同一数量级，就用同步，否则用异步。

比如：

- qps = 2000，latency = 10ms，计算结果 = 2000 \* 0.01s = 20。和常见的32核在同一个数量级，用同步。
- qps = 100, latency = 5s, 计算结果 = 100 \* 5s = 500。和核数不在同一个数量级，用异步。
- qps = 500, latency = 100ms，计算结果 = 500 \* 0.1s = 50。基本在同一个数量级，可用同步。如果未来延时继续增长，考虑异步。

这个公式计算的是同时进行的平均请求数（你可以尝试证明一下），和线程数，cpu核数是可比的。当这个值远大于cpu核数时，说明大部分操作并不耗费cpu，而是让大量线程阻塞着，使用异步可以明显节省线程资源（栈占用的内存）。当这个值小于或和cpu核数差不多时，异步能节省的线程资源就很有限了，这时候简单易懂的同步代码更重要。

<a id="bthread-bthread-or-not--bthread"></a>

# 异步或bthread

有了bthread这个工具，用户甚至可以自己实现异步。以“半同步”为例，在brpc中用户有多种选择：

哪种效率更高呢？显然是前者。后者不仅要付出创建bthread的代价，在RPC过程中bthread还被阻塞着，不能用于其他用途。

**如果仅仅是为了并发RPC，别用bthread。**

不过当你需要并行计算时，问题就不同了。使用bthread可以简单地构建树形的并行计算，充分利用多核资源。比如检索过程中有三个环节可以并行处理，你可以建立两个bthread运行两个环节，在原地运行剩下的环节，最后join那两个bthread。过程大致如下：

```c++
bool search() {
  ...
  bthread th1, th2;
  if (bthread_start_background(&th1, NULL, part1, part1_args) != 0) {
    LOG(ERROR) << "Fail to create bthread for part1";
    return false;
  }
  if (bthread_start_background(&th2, NULL, part2, part2_args) != 0) {
    LOG(ERROR) << "Fail to create bthread for part2";
    return false;
  }
  part3(part3_args);
  bthread_join(th1);
  bthread_join(th2);
  return true;
}
```

这么实现的point：

- 你当然可以建立三个bthread分别执行三个部分，最后join它们，但相比这个方法要多耗费一个线程资源。
- bthread从建立到执行是有延时的（调度延时），在不是很忙的机器上，这个延时的中位数在3微秒左右，90%在10微秒内，99.99%在30微秒内。这说明两点：
  - 计算时间超过1ms时收益比较明显。如果计算非常简单，几微秒就结束了，用bthread是没有意义的。
  - 尽量让原地运行的部分最慢，那样bthread中的部分即使被延迟了几微秒，最后可能还是会先结束，而消除掉延迟的影响。并且join一个已结束的bthread时会立刻返回，不会有上下文切换开销。

另外当你有类似线程池的需求时，像执行一类job的线程池时，也可以用bthread代替。如果对job的执行顺序有要求，你可以使用基于bthread的[ExecutionQueue](https://brpc.apache.org/docs/bthread/execution-queue)。

---

Last modified April 11, 2022: [site search bugfix and update community info (#57) (a895fb1b8)](https://github.com/apache/brpc-website/commit/a895fb1b806a5b2667efc5e32866c9e96b42c781)

---

<a id="bthread-bthread"></a>

<!-- source_url: https://brpc.apache.org/docs/bthread/bthread/ -->

<!-- page_index: 6 -->

# bthread

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bthread/bthread/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bthread)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# bthread

Bthread, a high performance M:N thread library.

[bthread](https://github.com/brpc/brpc/tree/master/src/bthread)是brpc使用的M:N线程库，目的是在提高程序的并发度的同时，降低编码难度，并在核数日益增多的CPU上提供更好的scalability和cache locality。”M:N“是指M个bthread会映射至N个pthread，一般M远大于N。由于linux当下的pthread实现([NPTL](http://en.wikipedia.org/wiki/Native_POSIX_Thread_Library))是1:1的，M个bthread也相当于映射至N个[LWP](http://en.wikipedia.org/wiki/Light-weight_process)。bthread的前身是Distributed Process(DP)中的fiber，一个N:1的合作式线程库，等价于event-loop库，但写的是同步代码。

<a id="bthread-bthread--goals"></a>

# Goals

- 用户可以延续同步的编程模式，能在数百纳秒内建立bthread，可以用多种原语同步。
- bthread所有接口可在pthread中被调用并有合理的行为，使用bthread的代码可以在pthread中正常执行。
- 能充分利用多核。
- better cache locality, supporting NUMA is a plus.

<a id="bthread-bthread--nongoals"></a>

# NonGoals

- 提供pthread的兼容接口，只需链接即可使用。**拒绝理由**: bthread没有优先级，不适用于所有的场景，链接的方式容易使用户在不知情的情况下误用bthread，造成bug。
- 覆盖各类可能阻塞的glibc函数和系统调用，让原本阻塞系统线程的函数改为阻塞bthread。**拒绝理由**:
  - bthread阻塞可能切换系统线程，依赖系统TLS的函数的行为未定义。
  - 和阻塞pthread的函数混用时可能死锁。
  - 这类hook函数本身的效率一般更差，因为往往还需要额外的系统调用，如epoll。但这类覆盖对N:1合作式线程库(fiber)有一定意义：虽然函数本身慢了，但若不覆盖会更慢（系统线程阻塞会导致所有fiber阻塞）。
- 修改内核让pthread支持同核快速切换。**拒绝理由**: 拥有大量pthread后，每个线程对资源的需求被稀释了，基于thread-local cache的代码效果会很差，比如tcmalloc。而独立的bthread不会有这个问题，因为它最终还是被映射到了少量的pthread。bthread相比pthread的性能提升很大一部分来自更集中的线程资源。另一个考量是可移植性，bthread更倾向于纯用户态代码。

<a id="bthread-bthread--faq"></a>

# FAQ

<a id="bthread-bthread--qbthread-coroutine"></a>

##### Q：bthread是协程(coroutine)吗？

不是。我们常说的协程特指N:1线程库，即所有的协程运行于一个系统线程中，计算能力和各类eventloop库等价。由于不跨线程，协程之间的切换不需要系统调用，可以非常快(100ns-200ns)，受cache一致性的影响也小。但代价是协程无法高效地利用多核，代码必须非阻塞，否则所有的协程都被卡住，对开发者要求苛刻。协程的这个特点使其适合写运行时间确定的IO服务器，典型如http server，在一些精心调试的场景中，可以达到非常高的吞吐。但百度内大部分在线服务的运行时间并不确定，且很多检索由几十人合作完成，一个缓慢的函数会卡住所有的协程。在这点上eventloop是类似的，一个回调卡住整个loop就卡住了，比如ub**a**server（注意那个a，不是ubserver）是百度对异步框架的尝试，由多个并行的eventloop组成，真实表现糟糕：回调里打日志慢一些，访问redis卡顿，计算重一点，等待中的其他请求就会大量超时。所以这个框架从未流行起来。

bthread是一个M:N线程库，一个bthread被卡住不会影响其他bthread。关键技术两点：work stealing调度和butex，前者让bthread更快地被调度到更多的核心上，后者让bthread和pthread可以相互等待和唤醒。这两点协程都不需要。更多线程的知识查看[这里](https://brpc.apache.org/docs/rpc-in-depth/threading-overview)。

<a id="bthread-bthread--q-bthread"></a>

##### Q: 我应该在程序中多使用bthread吗？

不应该。除非你需要在一次RPC过程中[让一些代码并发运行](https://brpc.apache.org/docs/bthread/bthread-or-not)，你不应该直接调用bthread函数，把这些留给brpc做更好。

<a id="bthread-bthread--qbthread-pthread-worker"></a>

##### Q：bthread和pthread worker如何对应？

pthread worker在任何时间只会运行一个bthread，当前bthread挂起时，pthread worker先尝试从本地runqueue弹出一个待运行的bthread，若没有，则随机偷另一个worker的待运行bthread，仍然没有才睡眠并会在有新的待运行bthread时被唤醒。

<a id="bthread-bthread--qbthread-pthread"></a>

##### Q：bthread中能调用阻塞的pthread或系统函数吗？

可以，只阻塞当前pthread worker。其他pthread worker不受影响。

<a id="bthread-bthread--q-bthread-bthread"></a>

##### Q：一个bthread阻塞会影响其他bthread吗？

不影响。若bthread因bthread API而阻塞，它会把当前pthread worker让给其他bthread。若bthread因pthread API或系统函数而阻塞，当前pthread worker上待运行的bthread会被其他空闲的pthread worker偷过去运行。

<a id="bthread-bthread--qpthread-bthread-api"></a>

##### Q：pthread中可以调用bthread API吗？

可以。bthread API在bthread中被调用时影响的是当前bthread，在pthread中被调用时影响的是当前pthread。使用bthread API的代码可以直接运行在pthread中。

<a id="bthread-bthread--q-bthread-pthread-rpc"></a>

##### Q：若有大量的bthread调用了阻塞的pthread或系统函数，会影响RPC运行么？

会。比如有8个pthread worker，当有8个bthread都调用了系统usleep()后，处理网络收发的RPC代码就暂时无法运行了。只要阻塞时间不太长, 这一般**没什么影响**, 毕竟worker都用完了, 除了排队也没有什么好方法.
在brpc中用户可以选择调大worker数来缓解问题, 在server端可设置[ServerOptions.num\_threads](#server-basics--number-of-worker-pthreads)或[-bthread\_concurrency](http://brpc.baidu.com:8765/flags/bthread_concurrency), 在client端可设置[-bthread\_concurrency](http://brpc.baidu.com:8765/flags/bthread_concurrency).

那有没有完全规避的方法呢?

<a id="bthread-bthread--qbthread-channelhttpsgobyexamplecomchannels"></a>

##### Q：bthread会有[Channel](https://gobyexample.com/channels)吗？

不会。channel代表的是两点间的关系，而很多现实问题是多点的，这个时候使用channel最自然的解决方案就是：有一个角色负责操作某件事情或某个资源，其他线程都通过channel向这个角色发号施令。如果我们在程序中设置N个角色，让它们各司其职，那么程序就能分类有序地运转下去。所以使用channel的潜台词就是把程序划分为不同的角色。channel固然直观，但是有代价：额外的上下文切换。做成任何事情都得等到被调用处被调度，处理，回复，调用处才能继续。这个再怎么优化，再怎么尊重cache locality，也是有明显开销的。另外一个现实是：用channel的代码也不好写。由于业务一致性的限制，一些资源往往被绑定在一起，所以一个角色很可能身兼数职，但它做一件事情时便无法做另一件事情，而事情又有优先级。各种打断、跳出、继续形成的最终代码异常复杂。

我们需要的往往是buffered channel，扮演的是队列和有序执行的作用，bthread提供了[ExecutionQueue](https://brpc.apache.org/docs/bthread/execution-queue)，可以完成这个目的。

---

Last modified April 11, 2022: [site search bugfix and update community info (#57) (a895fb1b8)](https://github.com/apache/brpc-website/commit/a895fb1b806a5b2667efc5e32866c9e96b42c781)

---

<a id="bthread-execution-queue"></a>

<!-- source_url: https://brpc.apache.org/docs/bthread/execution-queue/ -->

<!-- page_index: 7 -->

# Execution Queue

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bthread/Execution%20Queue/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Execution%20Queue)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- - [实现执行函数](#bthread-execution-queue--section)
  - [启动一个ExecutionQueue:](#bthread-execution-queue--executionqueue)
  - [停止一个ExecutionQueue:](#bthread-execution-queue--executionqueue)
  - [提交任务](#bthread-execution-queue--section)
  - [取消一个已提交任务](#bthread-execution-queue--section)

# Execution Queue

A high performance execution queue.

<a id="bthread-execution-queue--section"></a>

# 概述

类似于kylin的ExecMan, [ExecutionQueue](https://github.com/brpc/brpc/blob/master/src/bthread/execution_queue.h)提供了异步串行执行的功能。ExecutionQueue的相关技术最早使用在RPC中实现[多线程向同一个fd写数据](https://brpc.apache.org/docs/rpc-in-depth/io#sending-messages). 在r31345之后加入到bthread。 ExecutionQueue 提供了如下基本功能:

- 异步有序执行: 任务在另外一个单独的线程中执行, 并且执行顺序严格和提交顺序一致.
- Multi Producer: 多个线程可以同时向一个ExecutionQueue提交任务
- 支持cancel一个已经提交的任务
- 支持stop
- 支持高优任务插队

和ExecMan的主要区别:

- ExecutionQueue的任务提交接口是[wait-free](https://en.wikipedia.org/wiki/Non-blocking_algorithm#Wait-freedom)的, ExecMan依赖了lock, 这意味着当机器整体比较繁忙的时候，使用ExecutionQueue不会因为某个进程被系统强制切换导致所有线程都被阻塞。
- ExecutionQueue支持批量处理: 执行线程可以批量处理提交的任务, 获得更好的locality. ExecMan的某个线程处理完某个AsyncClient的AsyncContext之后下一个任务很可能是属于另外一个AsyncClient的AsyncContex, 这时候cpu cache会在不同AsyncClient依赖的资源间进行不停的切换。
- ExecutionQueue的处理函数不会被绑定到固定的线程中执行, ExecMan中是根据AsyncClient hash到固定的执行线程，不同的ExecutionQueue之间的任务处理完全独立，当线程数足够多的情况下，所有非空闲的ExecutionQueue都能同时得到调度。同时也意味着当线程数不足的时候，ExecutionQueue无法保证公平性, 当发生这种情况的时候需要动态增加bthread的worker线程来增加整体的处理能力.
- ExecutionQueue运行线程为bthread, 可以随意的使用一些bthread同步原语而不用担心阻塞pthread的执行. 而在ExecMan里面得尽量避免使用较高概率会导致阻塞的同步原语.

<a id="bthread-execution-queue--section"></a>

# 背景

在多核并发编程领域， [Message passing](https://en.wikipedia.org/wiki/Message_passing)作为一种解决竞争的手段得到了比较广泛的应用，它按照业务依赖的资源将逻辑拆分成若干个独立actor，每个actor负责对应资源的维护工作，当一个流程需要修改某个资源的时候，
就转化为一个消息发送给对应actor，这个actor(通常在另外的上下文中)根据命令内容对这个资源进行相应的修改，之后可以选择唤醒调用者(同步)或者提交到下一个actor(异步)的方式进行后续处理。

![img](http://web.mit.edu/6.005/www/fa14/classes/20-queues-locks/figures/producer-consumer.png)

<a id="bthread-execution-queue--executionqueue-vs-mutex"></a>

# ExecutionQueue Vs Mutex

ExecutionQueue和mutex都可以用来在多线程场景中消除竞争. 相比较使用mutex,
使用ExecutionQueue有着如下几个优点:

- 角色划分比较清晰, 概念理解上比较简单, 实现中无需考虑锁带来的问题(比如死锁)
- 能保证任务的执行顺序，mutex的唤醒顺序不能得到严格保证.
- 所有线程各司其职，都能在做有用的事情，不存在等待.
- 在繁忙、卡顿的情况下能更好的批量执行，整体上获得较高的吞吐.

但是缺点也同样明显:

- 一个流程的代码往往散落在多个地方，代码理解和维护成本高。
- 为了提高并发度， 一件事情往往会被拆分到多个ExecutionQueue进行流水线处理，这样会导致在多核之间不停的进行切换，会付出额外的调度以及同步cache的开销, 尤其是竞争的临界区非常小的情况下， 这些开销不能忽略.
- 同时原子的操作多个资源实现会变得复杂, 使用mutex可以同时锁住多个mutex, 用了ExeuctionQueue就需要依赖额外的dispatch queue了。
- 由于所有操作都是单线程的，某个任务运行慢了就会阻塞同一个ExecutionQueue的其他操作。
- 并发控制变得复杂，ExecutionQueue可能会由于缓存的任务过多占用过多的内存。

不考虑性能和复杂度，理论上任何系统都可以只使用mutex或者ExecutionQueue来消除竞争.
但是复杂系统的设计上，建议根据不同的场景灵活决定如何使用这两个工具:

总之，多线程编程没有万能的模型，需要根据具体的场景，结合丰富的profliling工具，最终在复杂度和性能之间找到合适的平衡。

**特别指出一点**，Linux中mutex无竞争的lock/unlock只有需要几条原子指令，在绝大多数场景下的开销都可以忽略不计.

<a id="bthread-execution-queue--section"></a>

# 使用方式

<a id="bthread-execution-queue--section"></a>

### 实现执行函数

```
// Iterate over the given tasks
//
// Example:
//
// #include <bthread/execution_queue.h>
//
// int demo_execute(void* meta, TaskIterator<T>& iter) {
//     if (iter.is_stopped()) {
//         // destroy meta and related resources
//         return 0;
//     }
//     for (; iter; ++iter) {
//         // do_something(meta, *iter)
//         // or do_something(meta, iter->a_member_of_T)
//     }
//     return 0;
// }
template <typename T>
class TaskIterator;
```

<a id="bthread-execution-queue--executionqueue"></a>

### 启动一个ExecutionQueue:

```
// Start a ExecutionQueue. If |options| is NULL, the queue will be created with
// default options.
// Returns 0 on success, errno otherwise
// NOTE: type |T| can be non-POD but must be copy-constructible
template <typename T>
int execution_queue_start(
        ExecutionQueueId<T>* id,
        const ExecutionQueueOptions* options,
        int (*execute)(void* meta, TaskIterator<T>& iter),
        void* meta);
```

创建的返回值是一个64位的id, 相当于ExecutionQueue实例的一个[弱引用](https://en.wikipedia.org/wiki/Weak_reference), 可以wait-free的在O(1)时间内定位一个ExecutionQueue, 你可以到处拷贝这个id， 甚至可以放在RPC中，作为远端资源的定位工具。
你必须保证meta的生命周期，在对应的ExecutionQueue真正停止前不会释放.

<a id="bthread-execution-queue--executionqueue"></a>

### 停止一个ExecutionQueue:

```
// Stop the ExecutionQueue.
// After this function is called:
//  - All the following calls to execution_queue_execute would fail immediately.
//  - The executor will call |execute| with TaskIterator::is_queue_stopped() being
//    true exactly once when all the pending tasks have been executed, and after
//    this point it's ok to release the resource referenced by |meta|.
// Returns 0 on success, errno othrwise
template <typename T>
int execution_queue_stop(ExecutionQueueId<T> id);
 
// Wait until the the stop task (Iterator::is_queue_stopped() returns true) has
// been executed
template <typename T>
int execution_queue_join(ExecutionQueueId<T> id);
```

stop和join都可以多次调用， 都会有合理的行为。stop可以随时调用而不用当心线程安全性问题。

和fd的close类似，如果stop不被调用, 相应的资源会永久泄露。

安全释放meta的时机: 可以在execute函数中收到iter.is\_queue\_stopped()==true的任务的时候释放，也可以等到join返回之后释放. 注意不要double-free

<a id="bthread-execution-queue--section"></a>

### 提交任务

```
struct TaskOptions {
    TaskOptions();
    TaskOptions(bool high_priority, bool in_place_if_possible);
 
    // Executor would execute high-priority tasks in the FIFO order but before
    // all pending normal-priority tasks.
    // NOTE: We don't guarantee any kind of real-time as there might be tasks still
    // in process which are uninterruptible.
    //
    // Default: false
    bool high_priority;
 
    // If |in_place_if_possible| is true, execution_queue_execute would call
    // execute immediately instead of starting a bthread if possible
    //
    // Note: Running callbacks in place might cause the dead lock issue, you
    // should be very careful turning this flag on.
    //
    // Default: false
    bool in_place_if_possible;
};
 
const static TaskOptions TASK_OPTIONS_NORMAL = TaskOptions(/*high_priority=*/ false, /*in_place_if_possible=*/ false);
const static TaskOptions TASK_OPTIONS_URGENT = TaskOptions(/*high_priority=*/ true, /*in_place_if_possible=*/ false);
const static TaskOptions TASK_OPTIONS_INPLACE = TaskOptions(/*high_priority=*/ false, /*in_place_if_possible=*/ true);
 
// Thread-safe and Wait-free.
// Execute a task with defaut TaskOptions (normal task);
template <typename T>
int execution_queue_execute(ExecutionQueueId<T> id,
                            typename butil::add_const_reference<T>::type task);
 
// Thread-safe and Wait-free.
// Execute a task with options. e.g
// bthread::execution_queue_execute(queue, task, &bthread::TASK_OPTIONS_URGENT)
// If |options| is NULL, we will use default options (normal task)
// If |handle| is not NULL, we will assign it with the hanlder of this task.
template <typename T>
int execution_queue_execute(ExecutionQueueId<T> id,
                            typename butil::add_const_reference<T>::type task,
                            const TaskOptions* options);
template <typename T>
int execution_queue_execute(ExecutionQueueId<T> id,
                            typename butil::add_const_reference<T>::type task,
                            const TaskOptions* options,
                            TaskHandle* handle); 
```

high\_priority的task之间的执行顺序也会**严格按照提交顺序**, 这点和ExecMan不同, ExecMan的QueueExecEmergent的AsyncContex执行顺序是undefined. 但是这也意味着你没有办法将任何任务插队到一个high priority的任务之前执行.

开启inplace\_if\_possible, 在无竞争的场景中可以省去一次线程调度和cache同步的开销. 但是可能会造成死锁或者递归层数过多(比如不停的ping-pong)的问题，开启前请确定你的代码中不存在这些问题。

<a id="bthread-execution-queue--section"></a>

### 取消一个已提交任务

```
/// [Thread safe and ABA free] Cancel the corresponding task.
// Returns:
//  -1: The task was executed or h is an invalid handle
//  0: Success
//  1: The task is executing
int execution_queue_cancel(const TaskHandle& h);
```

返回非0仅仅意味着ExecutionQueue已经将对应的task递给过execute, 真实的逻辑中可能将这个task缓存在另外的容器中，所以这并不意味着逻辑上的task已经结束，你需要在自己的业务上保证这一点.

---

Last modified June 28, 2023: [typo (#151) (49251654f)](https://github.com/apache/brpc-website/commit/49251654fa10d3dffbdec4e521b5fe37eda1648f)

---

<a id="bthread"></a>

<!-- source_url: https://brpc.apache.org/docs/bthread/ -->

<!-- page_index: 8 -->

# bthread

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bthread/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bthread)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# bthread

Bthread, a high performance M:N thread library.

---

##### [bthread](#bthread-bthread)

Bthread, a high performance M:N thread library.

##### [bthread or not](#bthread-bthread-or-not)

Where should I choose to use bthread?

##### [Execution Queue](#bthread-execution-queue)

A high performance execution queue.

##### [thread-local](#bthread-thread-local)

The thread-local problem.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="bthread-thread-local"></a>

<!-- source_url: https://brpc.apache.org/docs/bthread/thread-local/ -->

<!-- page_index: 9 -->

# thread-local

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bthread/thread-local/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=thread-local)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# thread-local

The thread-local problem.

本页说明bthread下使用pthread-local可能会导致的问题。bthread-local的使用方法见[这里](#server-basics--bthread-local)。

<a id="bthread-thread-local--thread-local"></a>

# thread-local问题

调用阻塞的bthread函数后，所在的pthread很可能改变，这使[pthread\_getspecific](http://linux.die.net/man/3/pthread_getspecific)，[gcc \_\_thread](https://gcc.gnu.org/onlinedocs/gcc-4.2.4/gcc/Thread_002dLocal.html)和c++11
thread\_local变量，pthread\_self()等的值变化了，如下代码的行为是不可预计的：

```
thread_local SomeObject obj;
...
SomeObject* p = &obj;
p->bar();
bthread_usleep(1000);
p->bar();
```

bthread\_usleep之后，该bthread很可能身处不同的pthread，这时p指向了之前pthread的thread\_local变量，继续访问p的结果无法预计。这种使用模式往往发生在用户使用线程级变量传递业务变量的情况。为了防止这种情况，应该谨记：

- 不使用线程级变量传递业务数据。这是一种槽糕的设计模式，依赖线程级数据的函数也难以单测。判断是否滥用：如果不使用线程级变量，业务逻辑是否还能正常运行？线程级变量应只用作优化手段，使用过程中不应直接或间接调用任何可能阻塞的bthread函数。比如使用线程级变量的tcmalloc就不会和bthread有任何冲突。
- 如果一定要（在业务中）使用线程级变量，使用bthread\_key\_create和bthread\_getspecific。

<a id="bthread-thread-local--gcc4-errno"></a>

# gcc4下的errno问题

gcc4会优化[标记为\_\_attribute\_\_((**const**))](https://gcc.gnu.org/onlinedocs/gcc/Function-Attributes.html#index-g_t_0040code_007bconst_007d-function-attribute-2958)的函数，这个标记大致指只要参数不变，输出就不会变。所以当一个函数中以相同参数出现多次时，gcc4会合并为一次。比如在我们的系统中errno是内容为\*\_\_errno\_location()的宏，这个函数的签名是：

```
/* Function to get address of global `errno' variable.  */
extern int *__errno_location (void) __THROW __attribute__ ((__const__));
```

由于此函数被标记为`__const__`，且没有参数，当你在一个函数中调用多次errno时，可能只有第一次才调用\_\_errno\_location()，而之后只是访问其返回的`int*`。在pthread中这没有问题，因为返回的`int*`是thread-local的，一个给定的pthread中是不会变化的。但是在bthread中，这是不成立的，因为一个bthread很可能在调用一些函数后跑到另一个pthread去，如果gcc4做了类似的优化，即一个函数内所有的errno都替换为第一次调用返回的int\*，这中间bthread又切换了pthread，那么可能会访问之前pthread的errno，从而造成未定义行为。

比如下文是一种errno的使用场景：

```
Use errno ...   (original pthread)
bthread functions that may switch to another pthread.
Use errno ...   (another pthread) 
```

我们期望看到的行为：

```
Use *__errno_location() ...  -  the thread-local errno of original pthread
bthread may switch another pthread ...
Use *__errno_location() ...  -  the thread-local errno of another pthread
```

使用gcc4时的实际行为：

```
int* p= __errno_location();
Use *p ...                   -  the thread-local errno of original pthread
bthread context switches ...
Use *p ...                   -  still the errno of original pthread, undefined behavior!!
```

严格地说这个问题不是gcc4导致的，而是glibc给\_\_errno\_location的签名不够准确，一个返回thread-local指针的函数依赖于段寄存器（TLS的一般实现方式），这怎么能算const呢？由于我们还未找到覆盖\_\_errno\_location的方法，所以这个问题目前实际的解决方法是：

**务必在直接或间接使用bthread的项目的gcc编译选项中添加`-D__const__=`，即把`__const__`定义为空，避免gcc4做相关优化。**

把`__const__`定义为空对程序其他部分的影响几乎为0。另外如果你没有**直接**使用errno（即你的项目中没有出现errno），或使用的是gcc
3.4，即使没有定义`-D__const__=`，程序的正确性也不会受影响，但为了防止未来可能的问题，我们强烈建议加上。

需要说明的是，和errno类似，pthread\_self也有类似的问题，不过一般pthread\_self除了打日志没有其他用途，影响面较小，在`-D__const__=`后pthread\_self也会正常。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="builtin-services-buildin_services"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/buildin_services/ -->

<!-- page_index: 10 -->

# builtin services

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/buildin_services/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=builtin%20services)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# builtin services

Learn about bRPC builtin services.

<a id="builtin-services-buildin_services--builtin-services"></a>

# Builtin Services

Builtin services expose internal status of servers in different pespectives, making development and debugging over brpc more efficient. brpc serves builting services via HTTP, which can be easily accessed through curl and web browsers. Servers respond plain text or html according to `User-Agent` in the request header, or you may append `?console=1` to the uri to force the server to respond in plain text. Check the [example](http://brpc.baidu.com:8765/) running on our dev machine(only accessible from Baidu internal) for more details. If the port is forbidden from where you run curl or web browser (e.g. not all ports are accessible from a web browser inside Baidu), you can use [rpc\_view](#tools-rpc_view) for proxying.

Following 2 screenshots show accesses to builtin services from a web browser and a terminal respectively. Note that the logo is the codename inside Baidu, and being modified to brpc in opensourced version.

**From a web browser**

![img](assets/images/builtin-service-more_7c84f2b9904a7916.png)

**From a terminal**

![img](assets/images/builtin-service-from-console_e75d557064bd2e81.png)

<a id="builtin-services-buildin_services--security-mode"></a>

# Security Mode

To avoid potential attacks and information leaks, builtin services **must** be hidden on servers that may be accessed from public, including the ones proxied by nginx or other http servers. Click [here](#server-basics--security-mode) for more details.

<a id="builtin-services-buildin_services--main-services"></a>

# Main services:

[/status](#builtin-services-status): displays brief status of all services.

[/vars](#builtin-services-vars): lists user-customizable counters on miscellaneous metrics.

[/connections](#builtin-services-connections): lists all connections and their stats.

[/flags](#builtin-services-flags): lists all gflags, some of them are modifiable at run-time.

[/rpcz](#builtin-services-rpcz): traces all RPCs.

[cpu profiler](#builtin-services-cpu_profiler): analyzes CPU hotspots.

[heap profiler](#builtin-services-heap_profiler): shows how memory are allocated.

[contention profiler](#builtin-services-contention_profiler): analyzes lock contentions.

<a id="builtin-services-buildin_services--other-services"></a>

# Other services

[/version](http://brpc.baidu.com:8765/version) shows version of the server. Call Server::set\_version() to specify version of the server, or brpc would generate a default version like `brpc_server_<service-name1>_<service-name2> ...`

![img](assets/images/version-service_1b274822e84a88b8.png)

[/health](http://brpc.baidu.com:8765/health) shows whether this server is alive or not.

![img](assets/images/health-service_da9c417edb4ff5a9.png)

[/protobufs](http://brpc.baidu.com:8765/protobufs) shows scheme of all protobuf messages inside the server.

![img](assets/images/protobufs-service_6c3ab89247473b94.png)

[/vlog](http://brpc.baidu.com:8765/vlog) shows all the [VLOG](#c-base-streaming-log--vlog) that can be enabled(not working with glog).

![img](assets/images/vlog-service_d9dc37d000bf8a68.png)

/dir: browses all files on the server, convenient but too dangerous, disabled by default.

/threads: displays information of all threads of the process, hurting performance significantly when being turned on, disabled by default.

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="builtin-services-connections"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/connections/ -->

<!-- page_index: 11 -->

# connections

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/connections/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=connections)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# connections

Learn about connections service.

[connections服务](http://brpc.baidu.com:8765/connections)可以查看所有的连接。一个典型的页面如下：

server\_socket\_count: 5

| CreatedTime | RemoteSide | SSL | Protocol | fd | BytesIn/s | In/s | BytesOut/s | Out/s | BytesIn/m | In/m | BytesOut/m | Out/m | SocketId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2015/09/21-21:32:09.630840 | 172.22.38.217:51379 | No | http | 19 | 1300 | 1 | 269 | 1 | 68844 | 53 | 115860 | 53 | 257 |
| 2015/09/21-21:32:09.630857 | 172.22.38.217:51380 | No | http | 20 | 1308 | 1 | 5766 | 1 | 68884 | 53 | 129978 | 53 | 258 |
| 2015/09/21-21:32:09.630880 | 172.22.38.217:51381 | No | http | 21 | 1292 | 1 | 1447 | 1 | 67672 | 52 | 143414 | 52 | 259 |
| 2015/09/21-21:32:01.324587 | 127.0.0.1:55385 | No | baidu\_std | 15 | 1480 | 20 | 880 | 20 | 88020 | 1192 | 52260 | 1192 | 512 |
| 2015/09/21-21:32:01.325969 | 127.0.0.1:55387 | No | baidu\_std | 17 | 4016 | 40 | 1554 | 40 | 238879 | 2384 | 92660 | 2384 | 1024 |

channel\_socket\_count: 1

| CreatedTime | RemoteSide | SSL | Protocol | fd | BytesIn/s | In/s | BytesOut/s | Out/s | BytesIn/m | In/m | BytesOut/m | Out/m | SocketId |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2015/09/21-21:32:01.325870 | 127.0.0.1:8765 | No | baidu\_std | 16 | 1554 | 40 | 4016 | 40 | 92660 | 2384 | 238879 | 2384 | 0 |

channel\_short\_socket\_count: 0

上述信息分为三段：

- 第一段是server接受(accept)的连接。
- 第二段是server与下游的单连接（使用brpc::Channel建立），fd为-1的是虚拟连接，对应第三段中所有相同RemoteSide的连接。
- 第三段是server与下游的短连接或连接池(pooled connections)，这些连接从属于第二段中的相同RemoteSide的虚拟连接。

表格标题的含义：

- RemoteSide : 远端的ip和端口。
- SSL：是否使用SSL加密，若为Yes的话，一般是HTTPS连接。
- Protocol : 使用的协议，可能为baidu\_std hulu\_pbrpc sofa\_pbrpc memcache http public\_pbrpc nova\_pbrpc nshead\_server等。
- fd : file descriptor（文件描述符），可能为-1。
- BytesIn/s : 上一秒读入的字节数
- In/s : 上一秒读入的消息数（消息是对request和response的统称）
- BytesOut/s : 上一秒写出的字节数
- Out/s : 上一秒写出的消息数
- BytesIn/m: 上一分钟读入的字节数
- In/m: 上一分钟读入的消息数
- BytesOut/m: 上一分钟写出的字节数
- Out/m: 上一分钟写出的消息数
- SocketId ：内部id，用于debug，用户不用关心。

典型截图分别如下所示：

单连接：![img](assets/images/single-conn_8722803d2618c611.png)

连接池：![img](assets/images/pooled-conn_2b60c18edc9badf1.png)

短连接：![img](assets/images/short-conn_674ea72177f684d9.png)

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="builtin-services-contention_profiler"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/contention_profiler/ -->

<!-- page_index: 12 -->

# contention profiler

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/contention_profiler/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=contention%20profiler)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# contention profiler

Learn about contention profiler service.

brpc可以分析花在等待锁上的时间及发生等待的函数。

<a id="builtin-services-contention_profiler--section"></a>

# 开启方法

按需开启。无需配置，不依赖tcmalloc，不需要链接frame pointer或libunwind。如果只是brpc client或没有使用brpc，看[这里](#client-dummy-server)。

<a id="builtin-services-contention_profiler--section"></a>

# 图示

当很多线程争抢同一把锁时，一些线程无法立刻获得锁，而必须睡眠直到某个线程退出临界区。这个争抢过程我们称之为**contention**。在多核机器上，当多个线程需要操作同一个资源却被一把锁挡住时，便无法充分发挥多个核心的并发能力。现代OS通过提供比锁更底层的同步原语，使得无竞争锁完全不需要系统调用，只是一两条wait-free，耗时10-20ns的原子操作，非常快。而锁一旦发生竞争，一些线程就要陷入睡眠，再次醒来触发了OS的调度代码，代价至少为3-5us。所以让锁尽量无竞争，让所有线程“一起飞”是需要高性能的server的永恒话题。

r31906后brpc支持contention profiler，可以分析在等待锁上花费了多少时间。等待过程中线程是睡着的不会占用CPU，所以contention profiler中的时间并不是cpu时间，也不会出现在[cpu profiler](#builtin-services-cpu_profiler)中。cpu profiler可以抓到特别频繁的锁（以至于花费了很多cpu），但耗时真正巨大的临界区往往不是那么频繁，而无法被cpu profiler发现。\*\*contention profiler和cpu profiler好似互补关系，前者分析等待时间（被动），后者分析忙碌时间。\*\*还有一类由用户基于condition或sleep发起的主动等待时间，无需分析。

目前contention profiler支持pthread\_mutex\_t（非递归）和bthread\_mutex\_t，开启后每秒最多采集1000个竞争锁，这个数字由参数-bvar\_collector\_expected\_per\_second控制（同时影响rpc\_dump）。

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| bvar\_collector\_expected\_per\_second | 1000 | Expected number of samples to be collected per second | bvar/collector.cpp |

如果一秒内竞争锁的次数Ｎ超过了1000，那么每把锁会有1000/N的概率被采集。在我们的各类测试场景中（qps在10万-60万不等）没有观察到被采集程序的性能有明显变化。

我们通过实际例子来看下如何使用contention profiler，点击“contention”按钮（more左侧）后就会开启默认10秒的分析过程。下图是libraft中的一个示例程序的锁状况，这个程序是3个节点复制组的leader，qps在10-12万左右。左上角的**Total seconds: 2.449**是采集时间内（10秒）在锁上花费的所有等待时间。注意是“等待”，无竞争的锁不会被采集也不会出现在下图中。顺着箭头往下走能看到每份时间来自哪些函数。

![img](assets/images/raft-contention-1_a4840481501de192.png)

上图有点大，让我们放大一个局部看看。下图红框中的0.768是这个局部中最大的数字，它代表raft::LogManager::get\_entry在等待涉及到bvar::detail::UniqueLockBase的函数上共等待了0.768秒（10秒内）。我们如果觉得这个时间不符合预期，就可以去排查代码。

![img](assets/images/raft-contention-2_47c7f45d5af2db89.png)

点击上方的count选择框，可以查看锁的竞争次数。选择后左上角变为了**Total samples: 439026**，代表采集时间内总共的锁竞争次数（估算）。图中箭头上的数字也相应地变为了次数，而不是时间。对比同一份结果的时间和次数，可以更深入地理解竞争状况。

![img](assets/images/raft-contention-3_3c34943f50d8f648.png)

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="builtin-services-cpu_profiler"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/cpu_profiler/ -->

<!-- page_index: 13 -->

# cpu profiler

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/cpu_profiler/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=cpu%20profiler)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# cpu profiler

Learn about cpu profiler service.

brpc可以分析程序中的热点函数。

<a id="builtin-services-cpu_profiler--section"></a>

# 开启方法

注意要关闭Server端的认证，否则可能会看到这个：

```
$ tools/pprof --text localhost:9002/pprof/profile Use of uninitialized value in substitution (s///) at tools/pprof line 2703. http://localhost:9002/profile/symbol doesn't exist
```

server端可能会有这样的日志：

```
FATAL: 12-26 10:01:25:   * 0 [src/brpc/policy/giano_authenticator.cpp:65][4294969345] Giano fails to verify credentical, 70003
WARNING: 12-26 10:01:25:   * 0 [src/brpc/input_messenger.cpp:132][4294969345] Authentication failed, remote side(127.0.0.1:22989) of sockfd=5, close it
```

<a id="builtin-services-cpu_profiler--section"></a>

# 查看方法

1. 通过builtin service的 /hotspots/cpu 页面查看
2. 通过pprof 工具查看，如 tools/pprof –text localhost:9002/pprof/profile

<a id="builtin-services-cpu_profiler--section"></a>

# 控制采样频率

启动前设置环境变量：export CPUPROFILE\_FREQUENCY=xxx

默认值为: 100

<a id="builtin-services-cpu_profiler--section"></a>

# 控制采样时间

url加上?seconds=秒数，如/hotspots/cpu?seconds=5

<a id="builtin-services-cpu_profiler--section"></a>

# 图示

下图是一次运行cpu profiler后的结果：

- 左上角是总体信息，包括时间，程序名，总采样数等等。
- View框中可以选择查看之前运行过的profile结果，Diff框中可选择查看和之前的结果的变化量，重启后清空。
- 代表函数调用的方框中的字段从上到下依次为：函数名，这个函数本身（除去所有子函数）占的采样数和比例，这个函数及调用的所有子函数累计的采样数和比例。采样数越大框越大。
- 方框之间连线上的数字表示被采样到的上层函数对下层函数的调用数，数字越大线越粗。

热点分析一般开始于找到最大的框最粗的线考察其来源及去向。

cpu profiler的原理是在定期被调用的SIGPROF handler中采样所在线程的栈，由于handler（在linux 2.6后）会被随机地摆放于活跃线程的栈上运行，cpu profiler在运行一段时间后能以很大的概率采集到所有活跃线程中的活跃函数，最后根据栈代表的函数调用关系汇总为调用图，并把地址转换成符号，这就是我们看到的结果图了。采集频率由环境变量CPUPROFILE\_FREQUENCY控制，默认100，即每秒钟100次或每10ms一次。在实践中cpu profiler对原程序的影响不明显。

![img](assets/images/echo-cpu-profiling_9925227ef7fe4de5.png)

在Linux下，你也可以使用[pprof](https://github.com/brpc/brpc/blob/master/tools/pprof)或gperftools中的pprof进行profiling。

比如`pprof --text localhost:9002 --seconds=5`的意思是统计运行在本机9002端口的server的cpu情况，时长5秒。一次运行的例子如下：

```
$ tools/pprof --text 0.0.0.0:9002 --seconds=5 Gathering CPU profile from http://0.0.0.0:9002/pprof/profile?seconds=5 for 5 seconds to
  /home/gejun/pprof/echo_server.1419501210.0.0.0.0
Be patient...
Wrote profile to /home/gejun/pprof/echo_server.1419501210.0.0.0.0
Removing funlockfile from all stack traces.
Total: 2946 samples
    1161  39.4%  39.4%     1161  39.4% syscall
     248   8.4%  47.8%      248   8.4% bthread::TaskControl::steal_task
     227   7.7%  55.5%      227   7.7% writev
      87   3.0%  58.5%       88   3.0% ::cpp_alloc
      74   2.5%  61.0%       74   2.5% __read_nocancel
      46   1.6%  62.6%       48   1.6% tc_delete
      42   1.4%  64.0%       42   1.4% brpc::Socket::Address
      41   1.4%  65.4%       41   1.4% epoll_wait
      35   1.2%  66.6%       35   1.2% memcpy
      33   1.1%  67.7%       33   1.1% __pthread_getspecific
      33   1.1%  68.8%       33   1.1% brpc::Socket::Write
      33   1.1%  69.9%       33   1.1% epoll_ctl
      28   1.0%  70.9%       42   1.4% brpc::policy::ProcessRpcRequest
      27   0.9%  71.8%       27   0.9% butil::IOBuf::_push_back_ref
      27   0.9%  72.7%       27   0.9% bthread::TaskGroup::ending_sched
```

省略–text进入交互模式，如下图所示：

```
$ tools/pprof localhost:9002 --seconds=5 Gathering CPU profile from http://0.0.0.0:9002/pprof/profile?seconds=5 for 5 seconds to
  /home/gejun/pprof/echo_server.1419501236.0.0.0.0
Be patient...
Wrote profile to /home/gejun/pprof/echo_server.1419501236.0.0.0.0
Removing funlockfile from all stack traces.
Welcome to pprof!  For help, type 'help'.
(pprof) top
Total: 2954 samples
    1099  37.2%  37.2%     1099  37.2% syscall
     253   8.6%  45.8%      253   8.6% bthread::TaskControl::steal_task
     240   8.1%  53.9%      240   8.1% writev
      90   3.0%  56.9%       90   3.0% ::cpp_alloc
      67   2.3%  59.2%       67   2.3% __read_nocancel
      47   1.6%  60.8%       47   1.6% butil::IOBuf::_push_back_ref
      42   1.4%  62.2%       56   1.9% brpc::policy::ProcessRpcRequest
      41   1.4%  63.6%       41   1.4% epoll_wait
      38   1.3%  64.9%       38   1.3% epoll_ctl
      37   1.3%  66.1%       37   1.3% memcpy
      35   1.2%  67.3%       35   1.2% brpc::Socket::Address
```

<a id="builtin-services-cpu_profiler--macos"></a>

# MacOS的额外配置

在MacOS下，gperftools中的perl pprof脚本无法将函数地址转变成函数名，解决办法是：

1. 安装[standalone pprof](https://github.com/google/pprof)，并把下载的pprof二进制文件路径写入环境变量GOOGLE\_PPROF\_BINARY\_PATH中
2. 安装llvm-symbolizer（将函数符号转化为函数名），直接用brew安装即可：`brew install llvm`

<a id="builtin-services-cpu_profiler--section"></a>

# 火焰图

若需要结果以火焰图的方式展示，请下载并安装[FlameGraph](https://github.com/brendangregg/FlameGraph)工具，将环境变量FLAMEGRAPH\_PL\_PATH正确设置到本地的/path/to/flamegraph.pl后启动server即可。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="builtin-services-flags"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/flags/ -->

<!-- page_index: 14 -->

# flags

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/flags/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=flags)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# flags

Learn about flags service.

brpc使用gflags管理配置。如果你的程序也使用gflags，那么你应该已经可以修改和brpc相关的flags，你可以浏览[flags服务](http://brpc.baidu.com:8765/flags)了解每个flag的具体功能。如果你的程序还没有使用gflags，我们建议你使用，原因如下：

- 命令行和文件均可传入，前者方便做测试，后者适合线上运维。放在文件中的gflags可以reload。而configure只支持从文件读取配置。
- 你可以在浏览器中查看brpc服务器中所有gflags，并对其动态修改（如果允许的话）。configure不可能做到这点。
- gflags分散在和其作用紧密关联的文件中，更好管理。而使用configure需要聚集到一个庞大的读取函数中。

<a id="builtin-services-flags--usage-of-gflags"></a>

# Usage of gflags

gflags一般定义在需要它的源文件中。#include <gflags/gflags.h>后在全局scope加入DEFINE\_*<type>*(*<name>*, *<default-value>*, *<description>*); 比如：

```c++
#include <gflags/gflags.h>
...
DEFINE_bool(hex_log_id, false, "Show log_id in hexadecimal");
DEFINE_int32(health_check_interval, 3, "seconds between consecutive health-checkings");
```

一般在main函数开头用ParseCommandLineFlags处理程序参数：

```c++
#include <gflags/gflags.h>
...
int main(int argc, char* argv[]) {
    google::ParseCommandLineFlags(&argc, &argv, true/*表示把识别的参数从argc/argv中删除*/);
    ...
}
```

如果要从conf/gflags.conf中加载gflags，则可以加上参数-flagfile=conf/gflags.conf。如果希望默认（什么参数都不加）就从文件中读取，则可以在程序中直接给flagfile赋值，一般这么写

```c++
google::SetCommandLineOption("flagfile", "conf/gflags.conf");
```

程序启动时会检查conf/gflags.conf是否存在，如果不存在则会报错：

```
$ ./my_program conf/gflags.conf: No such file or directory
```

更具体的使用指南请阅读[官方文档](http://gflags.github.io/gflags/)。

<a id="builtin-services-flags--flagfile"></a>

# flagfile

在命令行中参数和值之间可不加等号，而在flagfile中一定要加。比如`./myapp -param 7`是ok的，但在`./myapp -flagfile=./gflags.conf`对应的gflags.conf中一定要写成 **-param=7** 或 **–param=7**，否则就不正确且不会报错。

在命令行中字符串可用单引号或双引号包围，而在flagfile中不能加。比如`./myapp -name="tom"`或`./myapp -name='tom'`都是ok的，但在`./myapp -flagfile=./gflags.conf`对应的gflags.conf中一定要写成 **-name=tom** 或 **–name=tom**，如果写成-name=“tom"的话，引号也会作为值的一部分。配置文件中的值可以有空格，比如gflags.conf中写成-name=value with spaces是ok的，参数name的值就是value with spaces，而在命令行中要用引号括起来。

flagfile中参数可由单横线(如-foo)或双横线(如–foo)打头，但不能以三横线或更多横线打头，否则的话是无效参数且不会报错!

flagfile中以`#开头的行被认为是注释。开头的空格和空白行都会被忽略。`

flagfile中可以使用`--flagfile包含另一个flagfile。`

<a id="builtin-services-flags--change-gflag-on-the-fly"></a>

# Change gflag on-the-fly

[flags服务](http://brpc.baidu.com:8765/flags)可以查看服务器进程中所有的gflags。修改过的flags会以红色高亮。“修改过”指的是修改这一行为，即使再改回默认值，仍然会显示为红色。

/flags：列出所有的gflags

/flags/NAME：查询名字为NAME的gflag

/flags/NAME1,NAME2,NAME3：查询名字为NAME1或NAME2或NAME3的gflag

/flags/foo\*,b$r：查询名字与某一统配符匹配的gflag，注意用$代替?匹配单个字符，因为?在url中有特殊含义。

访问/flags/NAME?setvalue=VALUE即可动态修改一个gflag的值，validator会被调用。

为了防止误修改，需要动态修改的gflag必须有validator，显示此类gflag名字时有(R)后缀。

![img](assets/images/reloadable-flags_2199ca3106a421c1.png)

*修改成功后会显示如下信息*：

![img](assets/images/flag-setvalue_85e9579b64e5b981.png)

*尝试修改不允许修改的gflag会显示如下错误信息*：

![img](assets/images/set-flag-reject_6baf4ee0fcc94e35.png)

*设置一个不允许的值会显示如下错误（flag值不会变化）*：

![img](assets/images/set-flag-invalid-value_517b1131983b3e34.png)

r31658之后支持可视化地修改，在浏览器上访问时将看到(R)下多了下划线：

![img](assets/images/the-r-after-flag_0fd9fb8c98dfc0b6.png)

点击后在一个独立页面可视化地修改对应的flag：

![img](assets/images/set-flag-with-form_9d75c399fca3c81d.png)

填入true后确定：

![img](assets/images/set-flag-with-form-2_7b381448ea4eefbc.png)

返回/flags可以看到对应的flag已经被修改了：

![img](assets/images/set-flag-with-form-3_f9b49e2fb01576e4.png)

关于重载gflags，重点关注：

- 避免在一段代码中多次调用同一个gflag，应把该gflag的值保存下来并调用该值。因为gflag的值随时可能变化，而产生意想不到的结果。
- 使用google::GetCommandLineOption()访问string类型的gflag，直接访问是线程不安全的。
- 处理逻辑和副作用应放到validator里去。比如修改FLAGS\_foo后得更新另一处的值，如果只是写在程序初始化的地方，而不是validator里，那么重载时这段逻辑就运行不到了。

如果你确认某个gflag不需要额外的线程同步和处理逻辑就可以重载，那么可以用如下方式为其注册一个总是返回true的validator：

```c++
DEFINE_bool(hex_log_id, false, "Show log_id in hexadecimal");
BRPC_VALIDATE_GFLAG(hex_log_id, brpc::PassValidate/*always true*/);
```

这个flag是单纯的开关，修改后不需要更新其他数据（没有处理逻辑），代码中前面看到true后面看到false也不会产生什么后果（不需要线程同步），所以我们让其默认可重载。

对于int32和int64类型，有一个判断是否为正数的常用validator：

```c++
DEFINE_int32(health_check_interval, 3, "seconds between consecutive health-checkings");
BRPC_VALIDATE_GFLAG(health_check_interval, brpc::PositiveInteger);
```

以上操作都可以在命令行中进行：

```shell
$ curl brpc.baidu.com:8765/flags/health_check_interval Name | Value | Description | Defined At ---------------------------------------health_check_interval (R) | 3 | seconds between consecutive health-checkings | src/brpc/socket_map.cpp
```

1.0.251.32399后增加了-immutable\_flags，打开后所有的gflags将不能被动态修改。当一个服务对某个gflag值比较敏感且不希望在线上被误改，可打开这个开关。打开这个开关的同时也意味着你无法动态修改线上的配置，每次修改都要重启程序，对于还在调试阶段或待收敛阶段的程序不建议打开。

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="builtin-services-heap_profiler"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/heap_profiler/ -->

<!-- page_index: 15 -->

# heap profiler

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/heap_profiler/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=heap%20profiler)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# heap profiler

Learn about heap profiler service.

brpc可以分析内存是被哪些函数占据的。heap profiler的原理是每分配满一些内存就采样调用处的栈，“一些”由环境变量TCMALLOC\_SAMPLE\_PARAMETER控制，默认524288，即512K字节。根据栈表现出的函数调用关系汇总为我们看到的结果图。在实践中heap profiler对原程序的影响不明显。

<a id="builtin-services-heap_profiler--section"></a>

# 开启方法

注意要关闭Server端的认证，否则可能会看到这个：

```
$ tools/pprof --text localhost:9002/pprof/heap Use of uninitialized value in substitution (s///) at tools/pprof line 2703. http://localhost:9002/pprof/symbol doesn't exist
```

server端可能会有这样的日志：

```
FATAL: 12-26 10:01:25:   * 0 [src/brpc/policy/giano_authenticator.cpp:65][4294969345] Giano fails to verify credentical, 70003
WARNING: 12-26 10:01:25:   * 0 [src/brpc/input_messenger.cpp:132][4294969345] Authentication failed, remote side(127.0.0.1:22989) of sockfd=5, close it
```

<a id="builtin-services-heap_profiler--section"></a>

# 图示

![img](assets/images/heap-profiler-1_c68069ae22911e2f.png)

左上角是当前程序通过malloc分配的内存总量，顺着箭头上的数字可以看到内存来自哪些函数。

点击左上角的text选择框可以查看文本格式的结果，有时候这种按分配量排序的形式更方便。

![img](assets/images/heap-profiler-2_e6f8ad4f0c8fa609.png)

左上角的两个选择框作用分别是：

- View：当前正在看的profile。选择<new profile>表示新建一个。新建完毕后，View选择框中会出现新profile，URL也会被修改为对应的地址。这意味着你可以通过粘贴URL分享结果，点击链接的人将看到和你一模一样的结果，而不是重做profiling的结果。你可以在框中选择之前的profile查看。历史profiie保留最近的32个，可通过[–max\_profiles\_kept](http://brpc.baidu.com:8765/flags/max_profiles_kept)调整。
- Diff：和选择的profile做对比。表示什么都不选。如果你选择了之前的某个profile，那么将看到View框中的profile相比Diff框中profile的变化量。

下图演示了勾选Diff和Text的效果。

![img](assets/images/heap-profiler-3_39a1cd674c750407.gif)

在Linux下，你也可以使用pprof脚本（tools/pprof）在命令行中查看文本格式结果：

```
$ tools/pprof --text db-rpc-dev00.db01:8765/pprof/heap Fetching /pprof/heap profile from http://db-rpc-dev00.db01:8765/pprof/heap to
  /home/gejun/pprof/play_server.1453216025.db-rpc-dev00.db01.pprof.heap
Wrote profile to /home/gejun/pprof/play_server.1453216025.db-rpc-dev00.db01.pprof.heap
Adjusting heap profiles for 1-in-524288 sampling rate
Heap version 2
Total: 38.9 MB
    35.8  92.0%  92.0%     35.8  92.0% ::cpp_alloc
     2.1   5.4%  97.4%      2.1   5.4% butil::FlatMap
     0.5   1.3%  98.7%      0.5   1.3% butil::IOBuf::append
     0.5   1.3% 100.0%      0.5   1.3% butil::IOBufAsZeroCopyOutputStream::Next
     0.0   0.0% 100.0%      0.6   1.5% MallocExtension::GetHeapSample
     0.0   0.0% 100.0%      0.5   1.3% ProfileHandler::Init
     0.0   0.0% 100.0%      0.5   1.3% ProfileHandlerRegisterCallback
     0.0   0.0% 100.0%      0.5   1.3% __do_global_ctors_aux
     0.0   0.0% 100.0%      1.6   4.2% _end
     0.0   0.0% 100.0%      0.5   1.3% _init
     0.0   0.0% 100.0%      0.6   1.5% brpc::CloseIdleConnections
     0.0   0.0% 100.0%      1.1   2.9% brpc::GlobalUpdate
     0.0   0.0% 100.0%      0.6   1.5% brpc::PProfService::heap
     0.0   0.0% 100.0%      1.9   4.9% brpc::Socket::Create
     0.0   0.0% 100.0%      2.9   7.4% brpc::Socket::Write
     0.0   0.0% 100.0%      3.8   9.7% brpc::Span::CreateServerSpan
     0.0   0.0% 100.0%      1.4   3.5% brpc::SpanQueue::Push
     0.0   0.0% 100.0%      1.9   4.8% butil::ObjectPool
     0.0   0.0% 100.0%      0.8   2.0% butil::ResourcePool
     0.0   0.0% 100.0%      1.0   2.6% butil::iobuf::tls_block
     0.0   0.0% 100.0%      1.0   2.6% bthread::TimerThread::Bucket::schedule
     0.0   0.0% 100.0%      1.6   4.1% bthread::get_stack
     0.0   0.0% 100.0%      4.2  10.8% bthread_id_create
     0.0   0.0% 100.0%      1.1   2.9% bvar::Variable::describe_series_exposed
     0.0   0.0% 100.0%      1.0   2.6% bvar::detail::AgentGroup
     0.0   0.0% 100.0%      0.5   1.3% bvar::detail::Percentile::operator
     0.0   0.0% 100.0%      0.5   1.3% bvar::detail::PercentileSamples
     0.0   0.0% 100.0%      0.5   1.3% bvar::detail::Sampler::schedule
     0.0   0.0% 100.0%      6.5  16.8% leveldb::Arena::AllocateNewBlock
     0.0   0.0% 100.0%      0.5   1.3% leveldb::VersionSet::LogAndApply
     0.0   0.0% 100.0%      4.2  10.8% pthread_mutex_unlock
     0.0   0.0% 100.0%      0.5   1.3% pthread_once
     0.0   0.0% 100.0%      0.5   1.3% std::_Rb_tree
     0.0   0.0% 100.0%      1.5   3.9% std::basic_string
     0.0   0.0% 100.0%      3.5   9.0% std::string::_Rep::_S_create
```

brpc还提供一个类似的growth profiler分析内存的分配去向（不考虑释放）。

![img](assets/images/growth-profiler_4fe92bdcdda69595.png)

<a id="builtin-services-heap_profiler--macos"></a>

# MacOS的额外配置

1. 安装[standalone pprof](https://github.com/google/pprof)，并把下载的pprof二进制文件路径写入环境变量GOOGLE\_PPROF\_BINARY\_PATH中
2. 安装llvm-symbolizer（将函数符号转化为函数名），直接用brew安装即可：`brew install llvm`

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="builtin-services"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/ -->

<!-- page_index: 16 -->

# Builtin Services

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Builtin%20Services)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Builtin Services

Learn about bRPC builtin services.

---

##### [builtin services](#builtin-services-buildin_services)

Learn about bRPC builtin services.

##### [status](#builtin-services-status)

Learn about status service.

##### [vars](#builtin-services-vars)

Learn about vars service.

##### [connections](#builtin-services-connections)

Learn about connections service.

##### [flags](#builtin-services-flags)

Learn about flags service.

##### [rpcz](#builtin-services-rpcz)

Learn about rpcz service.

##### [cpu profiler](#builtin-services-cpu_profiler)

Learn about cpu profiler service.

##### [heap profiler](#builtin-services-heap_profiler)

Learn about heap profiler service.

##### [contention profiler](#builtin-services-contention_profiler)

Learn about contention profiler service.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="builtin-services-rpcz"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/rpcz/ -->

<!-- page_index: 17 -->

# rpcz

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/rpcz/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=rpcz)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [开关方法](#builtin-services-rpcz--section)
- [数据展现](#builtin-services-rpcz--section)
- [Annotation](#builtin-services-rpcz--annotation)

# rpcz

Learn about rpcz service.

用户能通过/rpcz看到最近请求的详细信息，并可以插入注释（annotation），不同于tracing system（如[dapper](http://static.googleusercontent.com/media/research.google.com/en/pubs/archive/36356.pdf)）以全局视角看到整体系统的延时分布，rpcz更多是一个调试工具，虽然角色有所不同，但在brpc中rpcz和tracing的数据来源是一样的。当每秒请求数小于1万时，rpcz会记录所有的请求，超过1万时，rpcz会随机忽略一些请求把采样数控制在1万左右。rpcz可以淘汰时间窗口之前的数据，通过-span\_keeping\_seconds选项设置，默认1小时。[一个长期运行的例子](http://brpc.baidu.com:8765/rpcz)。

关于开销：我们的实现完全规避了线程竞争，开销极小，在qps 30万的测试场景中，观察不到明显的性能变化，对大部分应用而言应该是“free”的。即使采集了几千万条请求，rpcz也不会增加很多内存，一般在50兆以内。rpcz会占用一些磁盘空间（就像日志一样），如果设定为存一个小时的数据，一般在几百兆左右。

<a id="builtin-services-rpcz--section"></a>

## 开关方法

默认不开启，加入[-enable\_rpcz](http://brpc.baidu.com:8765/flags/*rpcz*)选项会在启动后开启。

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| enable\_rpcz (R) | true (default:false) | Turn on rpcz | src/baidu/rpc/builtin/rpcz\_service.cpp |
| rpcz\_hex\_log\_id (R) | false | Show log\_id in hexadecimal | src/baidu/rpc/builtin/rpcz\_service.cpp |
| rpcz\_database\_dir | ./rpc\_data/rpcz | For storing requests/contexts collected by rpcz. | src/baidu/rpc/span.cpp |
| rpcz\_keep\_span\_db | false | Don’t remove DB of rpcz at program’s exit | src/baidu/rpc/span.cpp |
| rpcz\_keep\_span\_seconds (R) | 3600 | Keep spans for at most so many seconds | src/baidu/rpc/span.cpp |

若启动时未加-enable\_rpcz，则可在启动后访问SERVER\_URL/rpcz/enable动态开启rpcz，访问SERVER\_URL/rpcz/disable则关闭，这两个链接等价于访问SERVER\_URL/flags/enable\_rpcz?setvalue=true和SERVER\_URL/flags/enable\_rpcz?setvalue=false。在r31010之后，rpc在html版本中增加了一个按钮可视化地开启和关闭。

![img](assets/images/rpcz-4_1c57d55d2516b69a.png)

![img](assets/images/rpcz-5_e46e79ac36edcd98.png)

如果只是brpc client或没有使用brpc，看[这里](#client-dummy-server)。

<a id="builtin-services-rpcz--section"></a>

## 数据展现

/rpcz展现的数据分为两层。

<a id="builtin-services-rpcz--section"></a>

### 第一层

看到最新请求的概况，点击链接进入第二层。

![img](assets/images/rpcz-6_eac76cc00c75015e.png)

<a id="builtin-services-rpcz--section"></a>

### 第二层

看到某系列(trace)或某个请求(span)的详细信息。一般通过点击链接进入，也可以把trace=和span=作为query-string拼出链接

![img](assets/images/rpcz-7_57e39276cc994a0e.png)

内容说明：

- 时间分为了绝对时间（如2015/01/21-20:20:30.817392，小数点后精确到微秒）和前一个时间的差值（如. 19，代表19微秒)。
- trace=ID有点像“session id”，对应一个系统中完成一次对外服务牵涉到的所有服务，即上下游server都共用一个trace-id。span=ID对应一个server或client中一个请求的处理过程。trace-id和span-id在概率上唯一。
- 第一层页面中的request=和response=后的是数据包的字节数，包括附件但不包括协议meta。第二层中request和response的字节数一般在括号里，比如"Responded(13)“中的13。
- 点击链接可能会访问其他server上的rpcz，点浏览器后退一般会返回到之前的页面位置。
- I’m the last call, I’m about to …都是用户的annotation。

<a id="builtin-services-rpcz--annotation"></a>

## Annotation

只要你使用了brpc，就可以使用[TRACEPRINTF](https://github.com/brpc/brpc/blob/master/src/brpc/traceprintf.h)打印内容到事件流中，比如：

```c++
TRACEPRINTF("Hello rpcz %d", 123);
```

这条annotation会按其发生时间插入到对应请求的rpcz中。从这个角度看，rpcz是请求级的日志。如果你用TRACEPRINTF打印了沿路的上下文，便可看到请求在每个阶段停留的时间，牵涉到的数据集和参数。这是个很有用的功能。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="builtin-services-status"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/status/ -->

<!-- page_index: 18 -->

# status

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/status/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=status)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# status

Learn about status service.

[/status](http://brpc.baidu.com:8765/status) shows primary statistics of services inside the server. The data sources are same with [/vars](#builtin-services-vars), but stats are grouped differently.

![img](assets/images/status_6f83d31d4e719c2a.png)

Meanings of the fields above:

- **non\_service\_error**: number of errors raised outside processing code of the service. When a valid service is obtained, the subsequent error is regarded as *service\_error*, otherwise it is regarded as *non\_service\_error* (such as request parsing failed, service name does not exist, request concurrency exceeding limit, etc.). As a contrast, failing to access back-end servers during the processing is an error of the service, not a *non\_service\_error*. Even if the response written out successfully stands for failure, the error is counted into the service rather than *non\_service\_error*.
- **connection\_count**: number of connections to the server from clients, not including number of outward connections which are displayed at /vars/rpc\_channel\_connection\_count.
- **example.EchoService**: Full name of the service, including the package name defined in proto.
- **Echo (EchoRequest) returns (EchoResponse)**: Signature of the method. A service can have multiple methods. Click links on request/response to see schemes of the protobuf messages.
- **count**: Number of requests that are succesfully processed.

> [!CAUTION]
> **error**
> - : Number of requests that are failed to process.
- **latency**: average latency in recent *60s/60m/24h/30d* from *right to left* on html, average latency in recent 10s(by default, specified by [-bvar\_dump\_interval](http://brpc.baidu.com:8765/flags/bvar_dump_interval)) on plain texts.
- **latency\_percentiles**: 80%, 90%, 99%, 99.9% percentiles of latency in 10 seconds(specified by[-bvar\_dump\_interval](http://brpc.baidu.com:8765/flags/bvar_dump_interval)). Curves with historical values are shown on html.
- **latency\_cdf**: shows percentiles as [CDF](https://en.wikipedia.org/wiki/Cumulative_distribution_function), only available on html.
- **max\_latency**: max latency in recent *60s/60m/24h/30d* from *right to left* on html, max latency in recent 10s(by default, specified by [-bvar\_dump\_interval](http://brpc.baidu.com:8765/flags/bvar_dump_interval)) on plain texts.
- **qps**: QPS(Queries Per Second) in recent *60s/60m/24h/30d* from *right to left* on html. QPS in recent 10s(by default, specified by [-bvar\_dump\_interval](http://brpc.baidu.com:8765/flags/bvar_dump_interval)) on plain texts.
- **processing**: (renamed to concurrency in master) Number of requests being processed by the method. If this counter can’t hit zero when the traffic to the service becomes zero, the server probably has bugs, such as forgetting to call done->Run() or stuck on some processing steps.

Users may customize descriptions on /status by letting the service implement [brpc::Describable](https://github.com/brpc/brpc/blob/master/src/brpc/describable.h).

```c++
class MyService : public XXXService, public brpc::Describable {
public:
    ...
    void Describe(std::ostream& os, const brpc::DescribeOptions& options) const {
        os << "my_status: blahblah";
    }
};
```

For example:

![img](assets/images/status-2_123e38c229d313bb.png)

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="builtin-services-vars"></a>

<!-- source_url: https://brpc.apache.org/docs/builtin-services/vars/ -->

<!-- page_index: 19 -->

# vars

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Builtin%20Services/vars/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=vars)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Query methods](#builtin-services-vars--query-methods)
- [View historical trends](#builtin-services-vars--view-historical-trends)
- [Calculate and view percentiles](#builtin-services-vars--calculate-and-view-percentiles)
- [Non brpc server](#builtin-services-vars--non-brpc-server)

# vars

Learn about vars service.

[bvar](https://github.com/brpc/brpc/tree/master/src/bvar/) is a set of counters to record and view miscellaneous statistics conveniently in multi-threaded applications. The implementation reduces cache bouncing by storing data in thread local storage(TLS), being much faster than UbMonitor(a legacy counting library inside Baidu) and even atomic operations in highly contended scenarios. brpc integrates bvar by default, namely all exposed bvars in a server are accessible through [/vars](http://brpc.baidu.com:8765/vars), and a single bvar is addressable by [/vars/VARNAME](http://brpc.baidu.com:8765/vars/rpc_socket_count). Read [bvar](#bvar-bvar) to know how to add bvars for your program. brpc extensively use bvar to expose internal status. If you are looking for an utility to collect and display metrics of your application, consider bvar in the first place. bvar definitely can’t replace all counters, essentially it moves contentions occurred during write to read: which needs to combine all data written by all threads and becomes much slower than an ordinary read. If read and write on the counter are both frequent or decisions need to be made based on latest values, you should not use bvar.

<a id="builtin-services-vars--query-methods"></a>

## Query methods

[/vars](http://brpc.baidu.com:8765/vars) : List all exposed bvars

[/vars/NAME](http://brpc.baidu.com:8765/vars/rpc_socket_count)：List the bvar whose name is `NAME`

[/vars/NAME1,NAME2,NAME3](http://brpc.baidu.com:8765/vars/pid;process_cpu_usage;rpc_controller_count)：List bvars whose names are either `NAME1`, `NAME2` or `NAME3`.

[/vars/foo\*,b$r](http://brpc.baidu.com:8765/vars/rpc_server*_count;iobuf_blo$k_*): List bvars whose names match given wildcard patterns. Note that `$` matches a single character instead of `?` which is a reserved character in URL.

Following animation shows how to find bvars with wildcard patterns. You can copy and paste the URL to others who will see same bvars that you see. (values may change)

![img](assets/images/vars-1_62953961358ed095.gif)

There’s a search box in the upper-left corner on /vars page, in which you can type part of the names to locate bvars. Different patterns are separated by `,` `:` or space.

![img](assets/images/vars-2_92cdef864886273a.gif)

/vars is accessible from terminal as well:

```shell
$ curl brpc.baidu.com:8765/vars/bthread* bthread_creation_count : 125134 bthread_creation_latency : 3 bthread_creation_latency_50 : 3 bthread_creation_latency_90 : 5 bthread_creation_latency_99 : 7 bthread_creation_latency_999 : 12 bthread_creation_latency_9999 : 12 bthread_creation_latency_cdf : "click to view" bthread_creation_latency_percentiles : "[3,5,7,12]" bthread_creation_max_latency : 7 bthread_creation_qps : 100 bthread_group_status : "0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 " bthread_num_workers : 24 bthread_worker_usage : 1.01056
```

<a id="builtin-services-vars--view-historical-trends"></a>

## View historical trends

Clicking on most of the numerical bvars shows historical trends. Each clickable bvar records values in recent *60 seconds, 60 minutes, 24 hours and 30 days*, which are *174* numbers in total. 1000 clickable bvars take roughly 1M memory.

![img](assets/images/vars-3_7f2a32257fa8f4c0.gif)

<a id="builtin-services-vars--calculate-and-view-percentiles"></a>

## Calculate and view percentiles

x-ile (short for x-th percentile) is the value ranked at N \* x%-th position amongst a group of ordered values. E.g. If there’re 1000 values inside a time window, sort them in ascending order first. The 500-th value(1000 \* 50%) in the ordered list is 50-ile(a.k.a median), the 990-th(1000 \* 99%) value is 99-ile, the 999-th value is 99.9-ile. Percentiles give more information on how latencies distribute than mean values, and being helpful for analyzing behavior of the system more accurately. Industrial-grade services often require SLA to be not less than 99.97% (the requirement for 2nd-level services inside Baidu, >=99.99% for 1st-level services), even if a system has good average latencies, a bad long-tail area may still break SLA. Percentiles do help analyzing the long-tail area.

Percentiles can be plotted as a CDF or percentiles-over-time curve.

**Following diagram plots percentiles as CDF**, where the X-axis is the ratio(ranked-position/total-number) and the Y-axis is the corresponding percentile. E.g. The Y value corresponding to X=50% is 50-ile. If a system requires that “99.9% requests need to be processed within Y milliseconds”, you should check the Y at 99.9%.

![img](assets/images/vars-4_70c6e71489a67066.png)

Why do we call it [CDF](https://en.wikipedia.org/wiki/Cumulative_distribution_function) ? When a Y=y is chosen, the corresponding X means “percentage of values <= y”. Since values are sampled randomly (and uniformly), the X can be viewed as “probability of values <= y”, or P(values <= y), which is just the definition of CDF.

Derivative of the CDF is [PDF](https://en.wikipedia.org/wiki/Probability_density_function). If we divide the Y-axis of the CDF into many small-range segments, calculate the difference between X values of both ends of each segment, and use the difference as new value for X-axis, a PDF curve would be plotted, just like a normal distribution rotated 90 degrees clockwise. However density of the median is often much higher than others in a PDF and probably make long-tail area very flat and hard to read. As a result, systems prefer showing distributions in CDF rather than PDF.

Here’re 2 simple rules to check if a CDF curve is good or not:

- The flatter the better. A horizontal line is an ideal CDF curve which means that there’re no waitings, congestions or pauses, very unlikely in practice.
- The area between 99% and 100% should be as small as possible: right-side of 99% is the long-tail area, which has a significant impact on SLA.

A CDF with slowly ascending curve and small long-tail area is great in practice.

**Following diagram plots percentiles over time** and has four curves. The X-axis is time and Y-axis from top to bottom are 99.9% 99% 90% 50% percentiles respectively, plotted in lighter and lighter colors (from orange to yellow).

![img](assets/images/vars-5_8cb222fa6a2f8c0d.png)

Hovering mouse over the curves shows corresponding values at the time. The tooltip in above diagram means “The 99% percentile of latency before 39 seconds is 330 **microseconds**”. The diagram does not include the 99.99-ile curve which is usually significantly higher than others, making others hard to read. You may click bvars ended with “\_latency\_9999” to read the 99.99-ile curve separately. This diagram shows how percentiles change over time, which is helpful to analyze performance regressions of systems.

brpc calculates latency distributions of services automatically, which do not need users to add manually. The metrics are as follows:

![img](assets/images/vars-6_b529f8aa966cc77a.png)

`bvar::LatencyRecorder` is able to calculate latency distributions of any code, as depicted below. (checkout [bvar-c++](#bvar-bvar-c) for details):

```c++
#include <bvar/bvar.h>

...
bvar::LatencyRecorder g_latency_recorder("client");  // expose this recorder
... 
void foo() {
    ...
    g_latency_recorder << my_latency;
    ...
}
```

If the application already starts a brpc server, values like `client_latency`, `client_latency_cdf` can be viewed from `/vars` as follows. Clicking them to see (dynamically-updated) curves:

![img](assets/images/vars-7_3989485ea960fe44.png)

<a id="builtin-services-vars--non-brpc-server"></a>

## Non brpc server

If your program only uses brpc client or even not use brpc, and you also want to view the curves, check [here](#client-dummy-server).

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="bvar-bvar-c"></a>

<!-- source_url: https://brpc.apache.org/docs/bvar/bvar-c++/ -->

<!-- page_index: 20 -->

# bvar c++

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bvar/bvar-c++/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bvar%20c++)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [bvar::Adder](#bvar-bvar-c--bvaradder)
- [bvar::Maxer](#bvar-bvar-c--bvarmaxer)
- [bvar::Miner](#bvar-bvar-c--bvarminer)

- [Difference between Window and PerSecond](#bvar-bvar-c--difference-between-window-and-persecond)

# bvar c++

A quick introduction of bvar c++.

<a id="bvar-bvar-c--quick-introduction"></a>

# Quick introduction

The basic usage of bvar is simple:

```c++
#include <bvar/bvar.h>
namespace foo {
namespace bar {
// bvar::Adder<T> used for running sum, we define a Adder for read_error as below
bvar::Adder<int> g_read_error;
// put another bvar inside window so that we can get the value over this period of time
bvar::Window<bvar::Adder<int> > g_read_error_minute("foo_bar", "read_error", &g_read_error, 60);
//                                                     ^          ^                         ^
//                                                    prefix1     monitor name             time window, 10 by default
// bvar::LatencyRecorder is a compound varibale, can be used for troughput、qps、avg latency, latency percentile, max latency。
bvar::LatencyRecorder g_write_latency("foo_bar", "write");
//                                      ^          ^
//                                     prefix1      monitor entry, LatencyRecorder includes different bvar, and expose() will add the suffix for them by default, such as write_qps, write_latency etc
// define a varible for the # of 'been-pushed task'
bvar::Adder<int> g_task_pushed("foo_bar", "task_pushed");
// put nested bvar into PerSecond so that we can get the value per second within this time window. Over here what we get is the # of tasks pushed per second
bvar::PerSecond<bvar::Adder<int> > g_task_pushed_second("foo_bar", "task_pushed_second", &g_task_pushed);
//       ^                                                                                             ^
//    different from Window, PerSecond will be divided by the time winodw.                            time window is the last param, we omit here, its 10 by default
}  // bar
}  // foo
```

how we use the bvar

```c++
// run into read errors
foo::bar::g_read_error << 1;
// record down the latenct, which is 23ms
foo::bar::g_write_latency << 23;
// one task has been pushed
foo::bar::g_task_pushed << 1;
```

Remember Window<> and PerSecond<> are derived variables, we don’t have to push value to them and they will auto-update.
Obviously, we can take bvar as local or member variables.

There are essentially 7 commonly used bvar classes, they all extend from the base class bvar:Variable.

- `bvar::Adder<T>` : counter, 0 by default, varname « N equals to varname += N。
- `bvar::Maxer<T>` : get the maximum value, std::numeric\_limits::min() by default, varname « N equals to varname = max(varname, N)。
- `bvar::Miner<T>` : get the minimum value, std::numeric\_limits::max() by default, varname « N equals to varname = min(varname, N)。
- `bvar::IntRecorder` : get the mean value since it was in use, notice here we don’t use “over a period of time”, since this bvar always comes with Window<> to calculate the mean value within the predefined time window.
- `bvar::Window<VAR>` : get the running sum over a time window. Window derives from other existing bvar and will auto-update
- `bvar::PerSecond<VAR>` : get the value per second during a predefined amount of time. PerSecond will also auto-update and derives from other bvar
- `bvar::LatencyRecorder` : intended for recording latency and qps, when we push latency to it, for mean latency/max lantency/qps, we will get all in once.

**caveat: make sure the name of bvar is globally unique, otherwise, the expose() will fail. When the option -bvar\_abort\_on\_same\_name is true(false by default), program will abort.**

<a id="bvar-bvar-c--best-practice-for-naming"></a>

### Best Practice for Naming:

There are different bvar from different module, to avoid duplicating name, we’d better follow the rule as `module\_class\_indicator

- a module usually refers to the program name, can be the acronym of product line, like inf\_ds, ecom\_retrbs etc.
- a class usually refers to the class name/ function name, like storage\_manager, file\_transfer, rank\_stage1.
- an indicator usually refers to qps, count, latency etc.
  some legit naming examples

```
iobuf_block_count : 29                          # module=iobuf   class=block  indicator=count
iobuf_block_memory : 237568                     # module=iobuf   class=block  indicator=memory
process_memory_resident : 34709504              # module=process class=memory indicator=resident
process_memory_shared : 6844416                 # module=process class=memory indicator=shared
rpc_channel_connection_count : 0                # module=rpc     class=channel_connection  indicator=count
rpc_controller_count : 1                        # module=rpc     class=controller indicator=count
rpc_socket_count : 6                            # module=rpc     class=socket     indicator=count
```

bvar will normalize the variable name, no matter whether we type foo::BarNum, foo.bar.num, foo bar num , foo-bar-num, they all go to foo\_bar\_num in the end.
**Things about indicators:**

- use `_count` as suffix for number, like request\_count, error\_count
- use `_second` as suffix for number per second is clear enough, no need to use ‘\_count\_second’ or ‘\_per\_second’, like request\_second, process\_inblocks\_second
- `_minute` as suffix for number per minute like request\_minute, process\_inblocks\_minute
  if we need to use a counter defined in another file, we have to declare that variable in header file

```
namespace foo {
namespace bar {
// notice g_read_error_minute and g_task_pushed_second are derived bvar, will auto update, no need to declare
extern bvar::Adder<int> g_read_error;
extern bvar::LatencyRecorder g_write_latency;
extern bvar::Adder<int> g_task_pushed;
}  // bar
}  // foo
```

**Don’t define golabel Window<> and PerSecond<> across files. The order for the initialization of global variables in different compile units is undefined.** foo.cpp defines `Adder<int> foo_count`, then defining `PerSecond<Adder<int> > foo_qps(&foo_count);` in foo\_qps.cpp is illegal
**Things about thread-safety**:

- bvar is thread-compatible. We can manipulate a bvar in different threads, such as we can expose or hide different bvar in multiple threads simultaneously, they will safely do some job on global shared variables.
- **Excpet read and write API,** any other functions of bvar are not thread-safe：u can not expose or hide a same bvar in different threads, this may cause the program crash. Generally speaking, we don’t have to call any other API concurrently except read and write.
  we can use butil::Timer for timer, API is as below:

```C++
#include <butil/time.h>
namespace butil {
class Timer {
public:
    enum TimerType { STARTED };
    Timer();
    // butil::Timer tm(butil::Timer::STARTED);  // tm is already started after creation.
    explicit Timer(TimerType);
    // Start this timer
    void start();
    // Stop this timer
    void stop();
    // Get the elapse from start() to stop().
    int64_t n_elapsed() const;  // in nanoseconds
    int64_t u_elapsed() const;  // in microseconds
    int64_t m_elapsed() const;  // in milliseconds
    int64_t s_elapsed() const;  // in seconds
};
}  // namespace butil
```

<a id="bvar-bvar-c--bvarvariable"></a>

# bvar::Variable:

Varibale is the base class for all bvar, it provides registering, listing and searching functions.

When user created a bvar with default params, it hasn’t been registered into any global structure, it’s merely a faster counter, which means we cannot use it elsewhere. The action of putting this bvar into the global registry is called `expose`, can be achieved by calling `expose()`

The name for globally exposed bvar consists of ’name’ or ’name+prefix’, can be searched by function with suffix `_exposed` , e.g. Variable::describe\_exposed(“foo”) will return the description of bvar with the name ‘foo’.

When there already exists the name, expose() will print FATAL log and return -1. When the option **-bvar\_abort\_on\_same\_name** is true(false by default), program will abort.

Some examples for expose() as below

```
bvar::Adder<int> count1; // create a bvar with defalut params
count1 << 10 << 20 << 30;   // values add up to 60.
count1.expose("count1");  // expose the variable globally
CHECK_EQ("60", bvar::Variable::describe_exposed("count1"));
count1.expose("another_name_for_count1");  // expose the variable with another name
CHECK_EQ("", bvar::Variable::describe_exposed("count1"));
CHECK_EQ("60", bvar::Variable::describe_exposed("another_name_for_count1"));
bvar::Adder<int> count2("count2");  // exposed in constructor directly
CHECK_EQ("0", bvar::Variable::describe_exposed("count2"));  // default value of Adder<int> is 0
bvar::Status<std::string> status1("count2", "hello");  // the name conflicts. if -bvar_abort_on_same_name is true,
                                                      // program aborts, otherwise a fatal log is printed.
```

To avoid duplicate name, we should have prefix for bvar, we recommend the name as `<namespace>_<module>_<name>`

For convenience, we provide expose\_as() as it will accept a prefix.

```C++
// Expose this variable with a prefix.
// Example:
//   namespace foo {
//   namespace bar {
//   class ApplePie {
//       ApplePie() {
//           // foo_bar_apple_pie_error
//           _error.expose_as("foo_bar_apple_pie", "error");
//       }
//   private:
//       bvar::Adder<int> _error;
//   };
//   }  // foo
//   }  // bar
int expose_as(const butil::StringPiece& prefix, const butil::StringPiece& name);
```

<a id="bvar-bvar-c--export-all-variables"></a>

# Export All Variables

Common needs for exporting are querying by HTTP API and writing into local file, the former is provided by brpc [/vars](https://github.com/apache/brpc/blob/master/docs/cn/vars.md) service, the latter has been implemented in bvar, and it’s turned off by default. A couple of methods can activate this function：

- Using [gflags](https://github.com/apache/brpc/blob/master/docs/cn/flags.md) to parse the input params. We can add `-bvar_dump` during the starup of program or we can dynamically change the params thru brpc [/flags](https://github.com/apache/brpc/blob/master/docs/cn/flags.md) service after starup. gflags parsing is as below


```C++
#include <gflags/gflags.h>
...
int main(int argc, char* argv[]) {
    if (google::SetCommandLineOption("bvar_dump", "true").empty()) {
        LOG(FATAL) << "Fail to enable bvar dump";
    }
    ...
}
```

- If u dont want to use gflags and expect them opened by default in program


```C++
#include <gflags/gflags.h>
...
int main(int argc, char* argv[]) {
    if (google::SetCommandLineOption("bvar_dump", "true").empty()) {
        LOG(FATAL) << "Fail to enable bvar dump";
    }
    ...
}
```

- dump function is controlled by following gflags


| Name | Default Value | Effect |
| --- | --- | --- |
| bvar\_dump | false | Create a background thread dumping all bvar periodically, all bvar\_dump\_\* flags are not effective when this flag is off |
| bvar\_dump\_exclude | "" | Dump bvar excluded from these wildcards(separated by comma), empty means no exclusion |
| bvar\_dump\_file | monitor/bvar.<app>.data | Dump bvar into this file |
| bvar\_dump\_include | "" | Dump bvar matching these wildcards(separated by comma), empty means including all |
| bvar\_dump\_interval | 10 | Seconds between consecutive dump |
| bvar\_dump\_prefix | <app> | Every dumped name starts with this prefix |
| bvar\_dump\_tabs | <check the code> | Dump bvar into different tabs according to the filters (seperated by semicolon), format: \*(tab\_name=wildcards) |

  when the bvar\_dump\_file is not empty, a background thread will be started to update `bvar_dump_file` for the specified time interval called `bvar_dump_interval` , including all the bvar which is matched by `bvar_dump_include` while not matched by `bvar_dump_exclude`

  such like we modify the gflags as below：

  [![img](https://github.com/apache/brpc/raw/master/docs/images/bvar_dump_flags_2.png)](https://github.com/apache/brpc/blob/master/docs/images/bvar_dump_flags_2.png)

  exporting file will be like：


```
$ cat bvar.echo_server.data rpc_server_8002_builtin_service_count : 20 rpc_server_8002_connection_count : 1 rpc_server_8002_nshead_service_adaptor : brpc::policy::NovaServiceAdaptor rpc_server_8002_service_count : 1 rpc_server_8002_start_time : 2015/07/24-21:08:03 rpc_server_8002_uptime_ms : 14740954
```

  `iobuf_block_count : 8` is filtered out by bvar\_dump\_include, `rpc_server_8002_error : 0` is ruled out by bvar\_dump\_exclude.

  if you didn’t use brpc in your program, u also need to dynamically change gflags（normally no need), we can call google::SetCommandLineOption(), as below


```c++
#include <gflags/gflags.h>
...
if (google::SetCommandLineOption("bvar_dump_include", "*service*").empty()) {
    LOG(ERROR) << "Fail to set bvar_dump_include";
    return -1;
}
LOG(INFO) << "Successfully set bvar_dump_include to *service*";
```

  Do not directly set FLAGS\_bvar\_dump\_file / FLAGS\_bvar\_dump\_include / FLAGS\_bvar\_dump\_exclude. On the one hand, these gflags are std::string, which are not thread-safe to be overridden；On the other hand, the validator will not be triggered(call back to check the correctness), so the exporting thread will not be invoked

  users can also customize dump\_exposed() to export all the exposed bvar：


```c++
// Implement this class to write variables into different places.
// If dump() returns false, Variable::dump_exposed() stops and returns -1.
class Dumper {
public:
    virtual bool dump(const std::string& name, const butil::StringPiece& description) = 0;
};

// Options for Variable::dump_exposed().
struct DumpOptions {
    // Contructed with default options.
    DumpOptions();
    // If this is true, string-type values will be quoted.
    bool quote_string;
    // The ? in wildcards. Wildcards in URL need to use another character
    // because ? is reserved.
    char question_mark;
    // Separator for white_wildcards and black_wildcards.
    char wildcard_separator;
    // Name matched by these wildcards (or exact names) are kept.
    std::string white_wildcards;
    // Name matched by these wildcards (or exact names) are skipped.
    std::string black_wildcards;
};

class Variable {
    ...
    ...
    // Find all exposed variables matching `white_wildcards' but
    // `black_wildcards' and send them to `dumper'.
    // Use default options when `options' is NULL.
    // Return number of dumped variables, -1 on error.
    static int dump_exposed(Dumper* dumper, const DumpOptions* options);
};
```

<a id="bvar-bvar-c--bvarreducer"></a>

# bvar::Reducer

Reducer uses binary operators over several values to combine them into one final result, which are commutative, associative and without side effect. Only satisfying all of these thress, we can make sure the combined result is not affected by the distribution of the private variables of thread. Like substraciton does not satisfy associative nor commutative, so it cannot be taken as the operator here.

```C++
// Reduce multiple values into one with `Op': e1 Op e2 Op e3 ...
// `Op' shall satisfy:
//   - associative:     a Op (b Op c) == (a Op b) Op c
//   - commutative:     a Op b == b Op a;
//   - no side effects: a Op b never changes if a and b are fixed.
// otherwise the result is undefined.
template <typename T, typename Op>
class Reducer : public Variable;
```

reducer « e1 « e2 « e3 equals to reducer = e1 op e2 op e3。
Common Redcuer subclass: bvar::Adder, bvar::Maxer, bvar::Miner

<a id="bvar-bvar-c--bvaradder"></a>

## bvar::Adder

we can tell from its name, it’s intended for running sum. Opeator is `+`

```c++
bvar::Adder<int> value;
value << 1 << 2 << 3 << -4;
CHECK_EQ(2, value.get_value());
bvar::Adder<double> fp_value;  // may have warning
fp_value << 1.0 << 2.0 << 3.0 << -4.0;
CHECK_DOUBLE_EQ(2.0, fp_value.get_value());
```

Adder<> can be applied to the non-primitive type, which at least overrides `T operator+(T, T)`, an existing example is `std::string`, the code below will concatenate strings：

```c++
// This is just proof-of-concept, don't use it for production code because it makes a
// bunch of temporary strings which is not efficient, use std::ostringstream instead.
bvar::Adder<std::string> concater;
std::string str1 = "world";
concater << "hello " << str1;
CHECK_EQ("hello world", concater.get_value());
```

<a id="bvar-bvar-c--bvarmaxer"></a>

## bvar::Maxer

is producing the maximum value, operator is `std::max` 。

```c++
bvar::Maxer<int> value;
value << 1 << 2 << 3 << -4;
CHECK_EQ(3, value.get_value());
```

Since Maxer<> use std::numeric\_limits::min() as the identity, it cannot be applied to generic types unless you specialized std::numeric\_limits<> (and overloaded operator<, yes, not operator>).

<a id="bvar-bvar-c--bvarminer"></a>

## bvar::Miner

producing minimum value, operator is std::min

```c++
bvar::Maxer<int> value;
value << 1 << 2 << 3 << -4;
CHECK_EQ(-4, value.get_value());
```

Since Miner<> use std::numeric\_limits::max() as the identity, it cannot be applied to generic types unless you specialized std::numeric\_limits<> (and overloaded operator<).

<a id="bvar-bvar-c--bvarintrecorder"></a>

# bvar::IntRecorder

used for mean value

```c++
// For calculating average of numbers.
// Example:
//   IntRecorder latency;
//   latency << 1 << 3 << 5;
//   CHECK_EQ(3, latency.average());
class IntRecorder : public Variable;
```

<a id="bvar-bvar-c--bvarlatencyrecoder"></a>

# bvar::LatencyRecoder

A counter used for latency and qps. We can get latency / max\_latency / qps / count as long as the latency data filled in. Time window is the last param, omit by `bvar_dump_interval`

LatencyRecoder is a compound variable, consisting of several bvar.

```c++
LatencyRecorder write_latency("table2_my_table_write");  // produces 4 variables:
                                                         //   table2_my_table_write_latency
                                                         //   table2_my_table_write_max_latency
                                                         //   table2_my_table_write_qps
                                                         //   table2_my_table_write_count
// In your write function
write_latency << the_latency_of_write;
```

<a id="bvar-bvar-c--bvarwindow"></a>

# bvar::Window

Get data within a time window. Window cannot exist alone, it relies on a counter. Window will auto-update, we don’t have to send data to it. For the sake of performance, the data comes from every-second sampling over the original counter, in the worst case, Window has one-second latency

```c++
// Get data within a time window.
// The time unit is 1 second fixed.
// Window relies on other bvar which should be constructed before this window and destructs after this window.
// R must:
// - have get_sampler() (not require thread-safe)
// - defined value_type and sampler_type
template <typename R>
class Window : public Variable;
```

<a id="bvar-bvar-c--bvarpersecond"></a>

# bvar::PerSecond

Get the mean value over the last amount of time. Its almost the same as Window, except for the value will be divided by the time window

```c++
bvar::Adder<int> sum;
// sum_per_second.get_value()is summing every-second value over the last 60 seconds, if we omit the time window, it's set to 'bvar_dump_interval' by default
bvar::PerSecond<bvar::Adder<int> > sum_per_second(&sum, 60);
```

**PerSecond does not always make sense**

There is no Maxer in the above code, since the max value over a period of time divided by the time window is meaningless.

```c++
bvar::Maxer<int> max_value;
// WRONG！max value divided by time window is pointless
bvar::PerSecond<bvar::Maxer<int> > max_value_per_second_wrong(&max_value);
// CORRECT. It's the right way to set the time window to 1s so that we can get the max value for every second
bvar::Window<bvar::Maxer<int> > max_value_per_second(&max_value, 1);
```

<a id="bvar-bvar-c--difference-between-window-and-persecond"></a>

## Difference between Window and PerSecond

Suppose we want the memory change since last minute, if we use Window<>, the meaning for the returning value is “the memory increase over the last minute is 18M” if we use PerSecond<>, the meaning for return value will be “the average memory increase per second over the last minute is 0.3M”.

Pros of Window is preciseness, it fits in some small-number cases, like “the number of error produced over last minute“, if we use PerSecond, we might get something like “the average error rate per second over the last minute is 0.0167”, which is very unclear as opposed to “one error produced over last minute”. Some other non-time-related variables also fit in Window<>, such like calculating the CPU ratio over the last minute is using a Adder by summing CPU time and real time, then we use Window<> on top of the Adder to get the last-mintue CPU time and real time, dividing these two value then we get the CPU ratio for the last minute, which is not time-related. It will get wrong when use PerSeond

<a id="bvar-bvar-c--bvarstatus"></a>

# bvar::Status

Record and display one value, has additional set\_value() function

```c++
// Display a rarely or periodically updated value.
// Usage:
//   bvar::Status<int> foo_count1(17);
//   foo_count1.expose("my_value");
//
//   bvar::Status<int> foo_count2;
//   foo_count2.set_value(17);
//
//   bvar::Status<int> foo_count3("my_value", 17);
//
// Notice that Tp needs to be std::string or acceptable by boost::atomic<Tp>.
template <typename Tp>
class Status : public Variable;
```

<a id="bvar-bvar-c--bvarpassivestatus"></a>

# bvar::PassiveStatus

Display the value when needed. In some cases, we are not able to actively set\_value nor set\_value in a certain time interval. We’d better print it out when needed, user can pass in the print-out callback function to achieve this.

```c++
// Display a updated-by-need value. This is done by passing in an user callback
// which is called to produce the value.
// Example:
//   int print_number(void* arg) {
//      ...
//      return 5;
//   }
//
//   // number1 : 5
//   bvar::PassiveStatus status1("number1", print_number, arg);
//
//   // foo_number2 : 5
//   bvar::PassiveStatus status2(typeid(Foo), "number2", print_number, arg);
template <typename Tp>
class PassiveStatus : public Variable;
even though it looks simple, PassiveStatus is one of the most useful bvar, since most of the statistic values have already existed, we don't have to store it again, just fetch the data according to our need. Declare a bvar which can display user process name as below：
static void get_username(std::ostream& os, void*) {
    char buf[32];
    if (getlogin_r(buf, sizeof(buf)) == 0) {
        buf[sizeof(buf)-1] = '\0';
        os << buf;
    } else {
        os << "unknown";
    }
}
PassiveStatus<std::string> g_username("process_username", get_username, NULL);
```

<a id="bvar-bvar-c--bvargflag"></a>

# bvar::GFlag

Expose important gflags as bvar so that they’re monitored (in noah).

```c++
DEFINE_int32(my_flag_that_matters, 8, "...");
// Expose the gflag as *same-named* bvar so that it's monitored (in noah).
static bvar::GFlag s_gflag_my_flag_that_matters("my_flag_that_matters");
//                                                ^
//                                            the gflag name
// Expose the gflag as a bvar named "foo_bar_my_flag_that_matters".
static bvar::GFlag s_gflag_my_flag_that_matters_with_prefix("foo_bar", "my_flag_that_matters");
```

---

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="bvar-bvar"></a>

<!-- source_url: https://brpc.apache.org/docs/bvar/bvar/ -->

<!-- page_index: 21 -->

# bvar

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bvar/bvar/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bvar)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# bvar

Bvar, a high performance counters in multi-threaded applications.

<a id="bvar-bvar--what-is-bvar"></a>

# What is bvar?

[bvar](https://github.com/brpc/brpc/tree/master/src/bvar/) is a set of counters to record and view miscellaneous statistics conveniently in multi-threaded applications. The implementation reduces cache bouncing by storing data in thread local storage(TLS), being much faster than UbMonitor(a legacy counting library inside Baidu) and even atomic operations in highly contended scenarios. brpc integrates bvar by default, namely all exposed bvars in a server are accessible through [/vars](http://brpc.baidu.com:8765/vars), and a single bvar is addressable by [/vars/VARNAME](http://brpc.baidu.com:8765/vars/rpc_socket_count). Read [vars](#builtin-services-vars) to know how to query them in brpc servers. brpc extensively use bvar to expose internal status. If you are looking for an utility to collect and display metrics of your application, consider bvar in the first place. bvar definitely can’t replace all counters, essentially it moves contentions occurred during write to read: which needs to combine all data written by all threads and becomes much slower than an ordinary read. If read and write on the counter are both frequent or decisions need to be made based on latest values, you should not use bvar.

To understand how bvar works, read [explaining cacheline](#rpc-in-depth-atomic-instructions--cacheline) first, in which the mentioned counter example is just bvar. When many threads are modifying a counter, each thread writes into its own area without joining the global contention and all private data are combined at read, which is much slower than an ordinary one, but OK for low-frequency logging or display. The much faster and very-little-overhead write enables users to monitor systems from all aspects without worrying about hurting performance. This is the purpose that we designed bvar.

Following graph compares overhead of bvar, atomics, static UbMonitor, dynamic UbMonitor when they’re accessed by multiple threads simultaneously. We can see that overhead of bvar is not related to number of threads basically, and being constantly low (~20 nanoseconds). As a contrast, dynamic UbMonitor costs 7 microseconds on each operation when there’re 24 threads, which is the overhead of using the bvar for 300 times.

![img](assets/images/bvar-perf_9b7269ff8c50a570.png)

<a id="bvar-bvar--adding-new-bvar"></a>

# Adding new bvar

Read [Quick introduction](#bvar-bvar-c--quick-introduction) to know how to add bvar in C++. bvar already provides stats of many process-level and system-level variables by default, which are prefixed with `process_` and `system_`, such as:

```
process_context_switches_involuntary_second : 14
process_context_switches_voluntary_second : 15760
process_cpu_usage : 0.428
process_cpu_usage_system : 0.142
process_cpu_usage_user : 0.286
process_disk_read_bytes_second : 0
process_disk_write_bytes_second : 260902
process_faults_major : 256
process_faults_minor_second : 14
process_memory_resident : 392744960
system_core_count : 12
system_loadavg_15m : 0.040
system_loadavg_1m : 0.000
system_loadavg_5m : 0.020
```

and miscellaneous bvars used by brpc itself:

```
bthread_switch_second : 20422
bthread_timer_scheduled_second : 4
bthread_timer_triggered_second : 4
bthread_timer_usage : 2.64987e-05
bthread_worker_count : 13
bthread_worker_usage : 1.33733
bvar_collector_dump_second : 0
bvar_collector_dump_thread_usage : 0.000307385
bvar_collector_grab_second : 0
bvar_collector_grab_thread_usage : 1.9699e-05
bvar_collector_pending_samples : 0
bvar_dump_interval : 10
bvar_revision : "34975"
bvar_sampler_collector_usage : 0.00106495
iobuf_block_count : 89
iobuf_block_count_hit_tls_threshold : 0
iobuf_block_memory : 729088
iobuf_newbigview_second : 10
```

New exported files overwrite previous files, which is different from regular logs which append new data.

<a id="bvar-bvar--monitoring-bvar"></a>

# Monitoring bvar

Turn on [dump feature](#bvar-bvar-c--export-all-variables) of bvar to export all exposed bvars to files, which are formatted just like above texts: each line is a pair of “name” and “value”. Check if there’re data under $PWD/monitor/ after enabling dump, for example:

```
$ ls monitor/bvar.echo_client.data bvar.echo_server.data
 
$ tail -5 monitor/bvar.echo_client.data process_swaps : 0 process_time_real : 2580.157680 process_time_system : 0.380942 process_time_user : 0.741887 process_username : "gejun"
```

The monitoring system should combine data on every single machine periodically and merge them together to provide on-demand queries. Take the “noah” system inside Baidu as an example, variables defined by bvar appear as metrics in noah, which can be checked by users to view historical curves.

![img](assets/images/bvar-noah2_e30c7679518f8d1e.png)

![img](assets/images/bvar-noah3_e79f84a477b9b611.png)

<a id="bvar-bvar--export-to-prometheus"></a>

# Export to Prometheus

To export to [Prometheus](https://prometheus.io), set the path in scraping target url to `/brpc_metrics`. For example, if brpc server is running on localhost:8080, the scraping target should be `127.0.0.1:8080/brpc_metrics`.

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="bvar"></a>

<!-- source_url: https://brpc.apache.org/docs/bvar/ -->

<!-- page_index: 22 -->

# bvar

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/bvar/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bvar)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# bvar

Bvar, a high performance counters in multi-threaded applications.

---

##### [bvar](#bvar-bvar)

Bvar, a high performance counters in multi-threaded applications.

##### [bvar c++](#bvar-bvar-c)

A quick introduction of bvar c++.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="c-base-brpc-training-materials"></a>

<!-- source_url: https://brpc.apache.org/docs/c++-base/brpc-training-materials/ -->

<!-- page_index: 23 -->

# bRPC Training Materials

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/C++%20Base/bRPC%20Training%20Materials/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bRPC%20Training%20Materials)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# bRPC Training Materials

bRPC Training Materials.

- [bRPC外功修炼宝典](https://github.com/apache/brpc/blob/master/docs/cn/brpc_intro.pptx)
- [A tutorial on building large-scale services](https://github.com/apache/brpc/blob/master/docs/en/tutorial_on_building_services.pptx)
- [bRPC Internal](https://github.com/apache/brpc/blob/master/docs/en/brpc_internal.pptx)

---

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="c-base-flatmap"></a>

<!-- source_url: https://brpc.apache.org/docs/c++-base/flatmap/ -->

<!-- page_index: 24 -->

# FlatMap

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/C++%20Base/FlatMap/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=FlatMap)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# FlatMap

Learn about bRPC FlatMap.

<a id="c-base-flatmap--name"></a>

# NAME

FlatMap - Maybe the fastest hashmap, with tradeoff of space.

<a id="c-base-flatmap--example"></a>

# EXAMPLE

```c++
#include <string>
#include <butil/logging.h>
#include <butil/containers/flat_map.h>

void flatmap_example() {
    butil::FlatMap<int, std::string> map;
    // bucket_count: initial count of buckets, big enough to avoid resize.
    // load_factor: element_count * 100 / bucket_count, 80 as default.
    int bucket_count = 1000;
    int load_factor = 80;
    map.init(bucket_count, load_factor);
    map.insert(10, "hello");
    map[20] = "world";
    std::string* value = map.seek(20);
    CHECK(value != NULL);

    CHECK_EQ(2UL, map.size());
    CHECK_EQ(0UL, map.erase(30));
    CHECK_EQ(1UL, map.erase(10));

    LOG(INFO) << "All elements of the map:";
    for (butil::FlatMap<int, std::string>::const_iterator it = map.begin(); it != map.end(); ++it) {
        LOG(INFO) << it->first << " : " << it->second;
    }
    map.clear();
    CHECK_EQ(0UL, map.size());
}
```

<a id="c-base-flatmap--description"></a>

# DESCRIPTION

[FlatMap](https://github.com/brpc/brpc/blob/master/src/butil/containers/flat_map.h)可能是最快的哈希表，但当value较大时它需要更多的内存，它最适合作为检索过程中需要极快查找的小字典。

原理：把开链桶中第一个节点的内容直接放桶内。由于在实践中，大部分桶没有冲突或冲突较少，所以大部分操作只需要一次内存跳转：通过哈希值访问对应的桶。桶内两个及以上元素仍存放在链表中，由于桶之间彼此独立，一个桶的冲突不会影响其他桶，性能很稳定。在很多时候，FlatMap的查找性能和原生数组接近。

<a id="c-base-flatmap--benchmark"></a>

# BENCHMARK

下面是FlatMap和其他key/value容器的比较：

- [AlignHashMap](https://svn.baidu.com/app/ecom/nova/trunk/public/util/container/alignhash.h)：闭链中较快的实现。
- [CowHashMap](https://svn.baidu.com/app/ecom/nova/trunk/afs/smalltable/cow_hash_map.hpp)：smalltable中的开链哈希表，和普通开链不同的是带Copy-on-write逻辑。
- [std::map](http://www.cplusplus.com/reference/map/map/)：非哈希表，一般是红黑树。

```
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:474] [ value = 8 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 15/19/30/102ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing     100 from FlatMap/AlighHashMap/CowHashMap/std::map takes 7/11/33/146ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting  1000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 10/28/26/93ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing    1000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 6/9/29/100ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting 10000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 10/21/26/130ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing   10000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 5/10/30/104ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:474] [ value = 32 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 23/31/31/130ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing     100 from FlatMap/AlighHashMap/CowHashMap/std::map takes 9/11/72/104ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting  1000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 20/53/28/112ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing    1000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 7/10/29/101ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting 10000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 20/46/28/137ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing   10000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 7/10/29/112ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:474] [ value = 128 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 34/109/91/179ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing     100 from FlatMap/AlighHashMap/CowHashMap/std::map takes 8/11/33/112ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting  1000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 28/76/86/169ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing    1000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 8/9/30/110ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Sequentially inserting 10000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 28/68/87/201ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Sequentially erasing   10000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 9/9/30/125ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:474] [ value = 8 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 14/56/29/157ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing     100 from FlatMap/AlighHashMap/CowHashMap/std::map takes 9/11/31/181ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting  1000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 11/17/27/156ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing    1000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 6/10/30/204ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting 10000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 13/26/27/212ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing   10000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 7/11/38/309ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:474] [ value = 32 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 24/32/32/181ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing     100 from FlatMap/AlighHashMap/CowHashMap/std::map takes 10/12/32/182ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting  1000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 21/46/35/168ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing    1000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 7/10/36/209ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting 10000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 24/46/31/240ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing   10000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 8/11/40/314ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:474] [ value = 128 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting   100 into FlatMap/AlignHashMap/CowHashMap/std::map takes 36/114/93/231ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing     100 from FlatMap/AlighHashMap/CowHashMap/std::map takes 9/12/35/190ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting  1000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 44/94/88/224ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing    1000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 8/10/34/236ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:521] Randomly inserting 10000 into FlatMap/AlignHashMap/CowHashMap/std::map takes 46/92/93/314ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:558] Randomly erasing   10000 from FlatMap/AlighHashMap/CowHashMap/std::map takes 12/11/42/362ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:576] [ value = 8 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking   100 from FlatMap/AlignHashMap/CowHashMap/std::map takes 4/7/12/54ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking  1000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 3/7/11/78ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking 10000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 4/8/13/172ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:576] [ value = 32 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking   100 from FlatMap/AlignHashMap/CowHashMap/std::map takes 5/8/12/55ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking  1000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 4/8/11/82ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking 10000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 6/10/14/164ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:576] [ value = 128 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking   100 from FlatMap/AlignHashMap/CowHashMap/std::map takes 7/9/13/56ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking  1000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 6/10/12/93ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking 10000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 9/12/21/166ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:576] [ value = 8 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking   100 from FlatMap/AlignHashMap/CowHashMap/std::map takes 4/7/11/56ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking  1000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 3/7/11/79ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking 10000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 4/9/13/173ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:576] [ value = 32 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking   100 from FlatMap/AlignHashMap/CowHashMap/std::map takes 5/8/12/54ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking  1000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 4/8/11/100ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking 10000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 6/10/14/165ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:576] [ value = 128 bytes ]
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking   100 from FlatMap/AlignHashMap/CowHashMap/std::map takes 7/9/12/56ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking  1000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 6/10/12/88ns
TRACE: 12-30 13:19:53:   * 0 [test_flat_map.cpp:637] Seeking 10000 from FlatMap/AlignHashMap/CowHashMap/std::map takes 9/14/20/169ns
```

<a id="c-base-flatmap--overview-of-hashmaps"></a>

# Overview of hashmaps

哈希表是最常用的数据结构，它的基本原理是通过[计算哈希值](http://en.wikipedia.org/wiki/Hash_function)把不同的key分散到不同的区间，在查找时通过key的哈希值能快速地缩小查找区间。在使用恰当参数的前提下，哈希表在大部分时候能在O(1)时间内把一个key映射为value。像其他算法一样，这个“O(1)”在不同的实现中差异很大。哈希表的实现一般有两部分：

<a id="c-base-flatmap--section"></a>

## 计算哈希值(非加密型)

即把key散列开的方法，最常见的莫过于线性同余，但一个好的哈希算法(非加密型)要考虑很多因素：

- 结果是确定的。
- [雪崩效应](http://en.wikipedia.org/wiki/Avalanche_effect)：输入中一个bit的变化应该尽量影响输出所有bit的变化。
- 输出应尽量在值域中均匀分布。
- 充分利用现代cpu特性：成块计算，减少分支，循环展开等等。

大部分哈希算法针对的只是一个key，不会耗用太多的cpu。影响主要来自哈希表的整体数据分布，对于工程师来说，选用何种算法得看实践效果，一些最简单的方法也许就有很好的效果。通用算法可选择Murmurhash。

<a id="c-base-flatmap--section"></a>

## 解决冲突

哈希值可能重合，解决冲突是哈希表性能的另一关键因素。常见的冲突解决方法有：

- 开链哈希(open hashing, closed addressing): 开链哈希表是链表的数组，其中链表一般称为桶。当若干个key落到同一个桶时，做链表插入。这是最通用的结构，有很多优点：占用内存为O(NumElement \* (KeySize + ValueSize + SomePointers))，resize时候不会使之前的存放key/value的内存失效。桶之间是独立的，一个桶的冲突不会影响到其他桶，平均查找时间较为稳定，独立的桶也易于高并发。缺点是至少要两次内存跳转：先跳到桶入口，再跳到桶中的第一个节点。对于一些很小的表这个问题不明显，因为当表很小时，节点内存是接近的，但当表变大时，访存就愈发随机。如果一次访存在50ns左右（2G左右主频），开链哈希的查找时间往往就在100ns以上。在检索端的层层ranking过程中，对一些热点字典的查找1秒内可能有几百万次以上，开链哈希有时会成为热点。一些产品线可能对开链哈希的内存也有诟病，因为每对key/value都需要额外的指针。
- [闭链哈希](http://en.wikipedia.org/wiki/Open_addressing)(closed hashing or open addressing): 闭链的初衷是减少内存跳转，桶不再是链表入口，而只需要记录一对key/value与一些标记，当桶被占时，按照不同的探查方法直到找到空桶为止。比如线性探查就是查找下一个桶，二次探查是按1,2,4,9…平方数位移查找。优点是：当表很空时或冲突较少时，查找只需要一次访存，也不需要管理节点内存池。但仅此而已，这个方法带来了更多缺点：桶个数必须大于元素个数，resize后之前的内存全部失效，难以并发. 更关键的是聚集效应：当区域内元素较多时（超过70%，其实不算多），大量元素的实际桶和它们应在的桶有较大位移。这使哈希表的主要操作都要扫过一大片内存才能找到元素，性能不稳定难以预测。闭链哈希表在很多人的印象中“很快”，但在复杂的应用中往往不如开链哈希表，并且可能是数量级的慢。闭链有一些衍生版本试图解决这个问题，比如[Hopscotch hashing](http://en.wikipedia.org/wiki/Hopscotch_hashing)。
- 混合开链和闭链：一般是把桶数组中的一部分拿出来作为容纳冲突元素的空间，典型如[Coalesced hashing](http://en.wikipedia.org/wiki/Coalesced_hashing)，但这种结构没有解决开链的内存跳转问题，结构又比闭链复杂很多，工程效果并不好。
- 多次哈希：一般用多个哈希表代替一个哈希表，当发生冲突时（用另一个哈希值）尝试另一个哈希表。典型如[Cuckoo hashing](http://en.wikipedia.org/wiki/Cuckoo_hashing)，这个结构也没有解决内存跳转。

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="c-base"></a>

<!-- source_url: https://brpc.apache.org/docs/c++-base/ -->

<!-- page_index: 25 -->

# C++ Base

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/C++%20Base/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=C++%20Base)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# C++ Base

Learn about C++ Base.

---

##### [IOBuf](#c-base-iobuf)

Learn about bRPC IOBuf.

##### [Streaming Log](#c-base-streaming-log)

Learn about bRPC Streaming Log.

##### [FlatMap](#c-base-flatmap)

Learn about bRPC FlatMap.

##### [bRPC Training Materials](#c-base-brpc-training-materials)

bRPC Training Materials.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="c-base-iobuf"></a>

<!-- source_url: https://brpc.apache.org/docs/c++-base/iobuf/ -->

<!-- page_index: 26 -->

# IOBuf

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/C++%20Base/IOBuf/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=IOBuf)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# IOBuf

Learn about bRPC IOBuf.

brpc uses [butil::IOBuf](https://github.com/brpc/brpc/blob/master/src/butil/iobuf.h) as data structure for attachment in some protocols and HTTP body. It’s a non-contiguous zero-copied buffer, proved in previous projects, and good at performance. The interface of `IOBuf` is similar to `std::string`, but not the same.

If you’ve used the `BufHandle` in Kylin before, you should notice the convenience of `IOBuf`: the former one is badly encapsulated, leaving the internal structure directly in front of users, who must carefully handle the referential countings, very error prone and leading to bugs.

<a id="c-base-iobuf--what-iobuf-can"></a>

# What IOBuf can:

- Default constructor does not allocate memory.
- Copyable. Modifications to the copy doesn’t affect the original one. Copy the managing structure of IOBuf only rather the payload.
- Append another IOBuf without copying payload.
- Can append string, by copying payload.
- Read from or write into file descriptors.
- Serialize to or parse from protobuf messages.
- constructible like a std::ostream using IOBufBuilder.

<a id="c-base-iobuf--what-iobuf-cant"></a>

# What IOBuf can’t:

- Used as universal string-like structure in the program. Lifetime of IOBuf should be short, to prevent the referentially counted blocks(8K each) in IOBuf lock too many memory.

<a id="c-base-iobuf--cut"></a>

# Cut

Cut 16 bytes from front-side of source\_buf and append to dest\_buf:

```c++
source_buf.cut(&dest_buf, 16); // cut all bytes of source_buf when its length < 16
```

Just pop 16 bytes from front-side of source\_buf:

```c++
source_buf.pop_front(16); // Empty source_buf when its length < 16
```

<a id="c-base-iobuf--append"></a>

# Append

Append another IOBuf to back-side：

```c++
buf.append(another_buf);  // no data copy
```

Append std::string to back-sie

```c++
buf.append(str);  // copy data of str into buf
```

<a id="c-base-iobuf--parse"></a>

# Parse

Parse a protobuf message from the IOBuf

```c++
IOBufAsZeroCopyInputStream wrapper(&iobuf);
pb_message.ParseFromZeroCopyStream(&wrapper);
```

Parse IOBuf in user-defined formats

```c++
IOBufAsZeroCopyInputStream wrapper(&iobuf);
CodedInputStream coded_stream(&wrapper);
coded_stream.ReadLittleEndian32(&value);
...
```

<a id="c-base-iobuf--serialize"></a>

# Serialize

Serialize a protobuf message into the IOBuf

```c++
IOBufAsZeroCopyOutputStream wrapper(&iobuf);
pb_message.SerializeToZeroCopyStream(&wrapper);
```

Built IOBuf with printable data

```c++
IOBufBuilder os;
os << "anything can be sent to std::ostream";
os.buf();  // IOBuf
```

<a id="c-base-iobuf--print"></a>

# Print

Directly printable to std::ostream. Note that the iobuf in following example should only contain printable characters.

```c++
std::cout << iobuf << std::endl;
// or
std::string str = iobuf.to_string(); // note: allocating memory
printf("%s\n", str.c_str());
```

<a id="c-base-iobuf--performance"></a>

# Performance

IOBuf is good at performance:

| Action | Throughput | QPS |
| --- | --- | --- |
| Read from file -> Cut 12+16 bytes -> Copy -> Merge into another buffer ->Write to /dev/null | 240.423MB/s | 8586535 |
| Read from file -> Cut 12+128 bytes -> Copy-> Merge into another buffer ->Write to /dev/null | 790.022MB/s | 5643014 |
| Read from file -> Cut 12+1024 bytes -> Copy-> Merge into another buffer ->Write to /dev/null | 1519.99MB/s | 1467171 |

---

Last modified January 9, 2022: [A new verion of brpc website based on hugo (94b25d711)](https://github.com/apache/brpc-website/commit/94b25d7110944f3d4b2071b5188c691b23ffe3a9)

---

<a id="c-base-streaming-log"></a>

<!-- source_url: https://brpc.apache.org/docs/c++-base/streaming-log/ -->

<!-- page_index: 27 -->

# Streaming Log

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/C++%20Base/Streaming%20Log/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Streaming%20Log)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [LOG](#c-base-streaming-log--log)
- [PLOG](#c-base-streaming-log--plog)
- [noflush](#c-base-streaming-log--noflush)
- [LOG\_IF](#c-base-streaming-log--log_if)
- [XXX\_EVERY\_SECOND](#c-base-streaming-log--xxx_every_second)
- [XXX\_EVERY\_N](#c-base-streaming-log--xxx_every_n)
- [XXX\_FIRST\_N](#c-base-streaming-log--xxx_first_n)
- [XXX\_ONCE](#c-base-streaming-log--xxx_once)
- [VLOG](#c-base-streaming-log--vlog)
- [DLOG](#c-base-streaming-log--dlog)
- [CHECK](#c-base-streaming-log--check)
- [LogSink](#c-base-streaming-log--logsink)

# Streaming Log

Learn about bRPC Streaming Log.

<a id="c-base-streaming-log--name"></a>

# Name

streaming\_log - Print log to std::ostreams

<a id="c-base-streaming-log--synopsis"></a>

# SYNOPSIS

```c++
#include <butil/logging.h>

LOG(FATAL) << "Fatal error occurred! contexts=" << ...;
LOG(WARNING) << "Unusual thing happened ..." << ...;
LOG(TRACE) << "Something just took place..." << ...;
LOG(TRACE) << "Items:" << noflush;
LOG_IF(NOTICE, n > 10) << "This log will only be printed when n > 10";
PLOG(FATAL) << "Fail to call function setting errno";
VLOG(1) << "verbose log tier 1";
CHECK_GT(1, 2) << "1 can't be greater than 2";
 
LOG_EVERY_SECOND(INFO) << "High-frequent logs";
LOG_EVERY_N(ERROR, 10) << "High-frequent logs";
LOG_FIRST_N(INFO, 20) << "Logs that prints for at most 20 times";
LOG_ONCE(WARNING) << "Logs that only prints once";
```

<a id="c-base-streaming-log--description"></a>

# DESCRIPTION

Streaming log is the best choice for printing complex objects or template objects. As most objects are complicate, user needs to convert all the fields to string first in order to use `printf` with `%s`. However it’s very inconvenient (can’t append numbers) and needs lots of temporary memory (caused by string). The solution in C++ is to send the log as a stream to the `std::ostream` object. For example, in order to print object A, we need to implement the following interface:

```c++
std::ostream& operator<<(std::ostream& os, const A& a);
```

The signature of the function means to print object `a` to `os` and then return `os`. The return value of `os` enables us to combine binary operator `<<` (left-combine). As a result, `os << a << b << c;` means `operator<<(operator<<(operator<<(os, a), b), c);`. Apparently `operator<<` needs a returning reference to complete this process, which is also called chaining. In languages that don’t support operator overloading, you will see a more tedious form, such as `os.print(a).print(b).print(c)`.

You should also use chaining in your own implementation of `operator<<`. In fact, printing a complex object is like DFS a tree: Call `operator<<` on each child node, and then each child node invokes the function on the grandchild node, and so forth. For example, object A has two member variables: B and C. Printing A becomes the process of putting B and C ostream:

```c++
struct A {
    B b;
    C c;
};
std::ostream& operator<<(std::ostream& os, const A& a) {
    return os << "A{b=" << a.b << ", c=" << a.c << "}";
}
```

Data structure of B and C along with the print function：

```c++
struct B {
    int value;
};
std::ostream& operator<<(std::ostream& os, const B& b) {
    return os << "B{value=" << b.value << "}";
}
 
struct C {
    string name;
};
std::ostream& operator<<(std::ostream& os, const C& c) {
    return os << "C{name=" << c.name << "}";
}
```

Finally the result of printing object A is:

```
A{b=B{value=10}, c=C{name=tom}}
```

This way we don’t need to allocate temporary memory since objects are directly passed into the ostream object. Of course, the memory management of ostream itself is another topic.

OK, now we connect the whole printing process by ostream. The most common ostream objects are `std::cout` and `std::cerr`, so objects implement the above function can be directly sent to `std::cout` and `std::cerr`. In other words, if a log stream also inherits ostream, then these objects can be written into log. Streaming log is such a log stream that inherits `std::ostream` to send the object into the log. In the current implementation, the logs are recorded in a thread-local buffer, which will be flushed into screen or `logging::LogSink` after a complete log record. Of course, the implementation is thread safe.

<a id="c-base-streaming-log--log"></a>

## LOG

If you have ever used glog before, you should find it easy to start. The log macro is the same as glog. For example, to print a FATAL log (Note that there is no `std::endl`):

```c++
LOG(FATAL) << "Fatal error occurred! contexts=" << ...;
LOG(WARNING) << "Unusual thing happened ..." << ...;
LOG(TRACE) << "Something just took place..." << ...;
```

The log level of streaming log in accordance with glog：

| streaming log | glog | Use Cases |
| --- | --- | --- |
| FATAL | FATAL (coredump) | Fatal error. Since most fatal log inside baidu is not fatal actually, it won’t trigger coredump directly as glog, unless you turn on [-crash\_on\_fatal\_log](http://brpc.baidu.com:8765/flags/crash_on_fatal_log) |
| ERROR | ERROR | Non-fatal error. |
| WARNING | WARNING | Unusual branches |
| NOTICE | - | Generally you should not use NOTICE as it’s intended for important business logs. Make sure to check with other developers. glog doesn’t have NOTICE. |
| INFO, TRACE | INFO | Important side effects such as open/close some resources. |
| VLOG(n) | INFO | Detailed log that support multiple layers. |
| DEBUG | INFOVLOG(1) (NDEBUG) | Just for compatibility. Print logs only when `NDEBUG` is not defined. See DLOG/DPLOG/DVLOG for more reference. |

<a id="c-base-streaming-log--plog"></a>

## PLOG

The difference of PLOG and LOG is that it will append error information at the end of log. It’s kind of like `%m` in `printf`. Under POSIX environment, the error code is `errno`。

```c++
int fd = open("foo.conf", O_RDONLY);   // foo.conf does not exist, errno was set to ENOENT
if (fd < 0) { 
    PLOG(FATAL) << "Fail to open foo.conf";    // "Fail to open foo.conf: No such file or directory"
    return -1;
}
```

<a id="c-base-streaming-log--noflush"></a>

## noflush

If you don’t want to flush the log at once, append `noflush`. It’s commonly used inside a loop:

```c++
LOG(TRACE) << "Items:" << noflush;
for (iterator it = items.begin(); it != items.end(); ++it) {
    LOG(TRACE) << ' ' << *it << noflush;
}
LOG(TRACE);
```

The first two LOG(TRACE) doesn’t flush the log to the screen. They are recorded inside the thread-local buffer. The third LOG(TRACE) flush all logs into the screen. If there are 3 elements inside items and we don’t append `noflush`, the result would be:

```
TRACE: ... Items:
TRACE: ...  item1
TRACE: ...  item2
TRACE: ...  item3
```

After we add `noflush`:

```
TRACE: ... Items: item1 item2 item3 
```

The `noflush` feature also support bthread so that we can push lots of logs from the server’s bthreads without actually print them (using `noflush`), and flush the whole log at the end of RPC. Note that you should not use `noflush` when implementing an asynchronous method since it will change the underlying bthread, leaving `noflush` out of function.

<a id="c-base-streaming-log--log_if"></a>

## LOG\_IF

`LOG_IF(log_level, condition)` prints only when condition is true. It’s the same as `if (condition) { LOG() << ...; }` with shorter code：

```c++
LOG_IF(NOTICE, n > 10) << "This log will only be printed when n > 10";
```

<a id="c-base-streaming-log--xxx_every_second"></a>

## XXX\_EVERY\_SECOND

XXX represents for LOG, LOG\_IF, PLOG, SYSLOG, VLOG, DLOG, and so on. These logging macros print log at most once per second. You can use these to check running status inside hotspot area. The first call to this macro prints the log immediately, and costs additional 30ns (caused by gettimeofday) compared to normal LOG.

```c++
LOG_EVERY_SECOND(INFO) << "High-frequent logs";
```

<a id="c-base-streaming-log--xxx_every_n"></a>

## XXX\_EVERY\_N

XXX represents for LOG, LOG\_IF, PLOG, SYSLOG, VLOG, DLOG, and so on. These logging macros print log every N times. You can use these to check running status inside hotspot area. The first call to this macro prints the log immediately, and costs an additional atomic operation (relaxed order) compared to normal LOG. This macro is thread safe which means counting from multiple threads is also accurate while glog is not.

```c++
LOG_EVERY_N(ERROR, 10) << "High-frequent logs";
```

<a id="c-base-streaming-log--xxx_first_n"></a>

## XXX\_FIRST\_N

XXX represents for LOG, LOG\_IF, PLOG, SYSLOG, VLOG, DLOG, and so on. These logging macros print log at most N times. It costs an additional atomic operation (relaxed order) compared to normal LOG before N, and zero cost after.

```c++
LOG_FIRST_N(ERROR, 20) << "Logs that prints for at most 20 times";
```

<a id="c-base-streaming-log--xxx_once"></a>

## XXX\_ONCE

XX represents for LOG, LOG\_IF, PLOG, SYSLOG, VLOG, DLOG, and so on. These logging macros print log at most once. It’s the same as `XXX_FIRST_N(..., 1)`

```c++
LOG_ONCE(ERROR) << "Logs that only prints once";
```

<a id="c-base-streaming-log--vlog"></a>

## VLOG

VLOG(verbose\_level) is detail log that support multiple layers. It uses 2 gflags: *–verbose* and *–verbose\_module* to control the logging layer you want (Note that glog uses *–v* and *–vmodule*). The log will be printed only when `--verbose` >= `verbose_level`:

```c++
VLOG(0) << "verbose log tier 0";
VLOG(1) << "verbose log tier 1";
VLOG(2) << "verbose log tier 2";
```

When `--verbose=1`, the first 2 log will be printed while the last won’t. Module means a file or file path without the extension name, and value of `--verbose_module` will overwrite `--verbose`. For example:

```bash
--verbose=1 --verbose_module="channel=2,server=3"    # print VLOG of those with verbose value:
                                                     # channel.cpp <= 2
                                                     # server.cpp <= 3
                                                     # other files <= 1
--verbose=1 --verbose_module="src/brpc/channel=2,server=3"
                                                    # For files with same names, add paths
```

You can set `--verbose` and `--verbose_module` through `google::SetCommandLineOption` dynamically.

VLOG has another form VLOG2, which allows user to specify virtual path:

```c++
// public/foo/bar.cpp
VLOG2("a/b/c", 2) << "being filtered by a/b/c rather than public/foo/bar";
```

> VLOG and VLOG2 also have corresponding VLOG\_IF and VLOG2\_IF.

<a id="c-base-streaming-log--dlog"></a>

## DLOG

All log macros have debug versions, starting with D, such as DLOG, DVLOG. When NDEBUG is defined, these logs will not be printed.

**Do not put important side effects inside the log streams beginning with D.**

*No printing* means that even the parameters are not evaluated. If your parameters have side effects, they won’t happend when NDEBUG is defined. For example, `DLOG(FATAL) << foo();` where foo is a function or it changes a dictionary, anyway, it’s essential. However, it won’t be evaluated when NDEBUG is defined.

<a id="c-base-streaming-log--check"></a>

## CHECK

Another import variation of logging is `CHECK(expression)`. When expression evaluates to false, it will print a fatal log. It’s kind of like `ASSERT` in gtest, and has other form such as CHECK\_EQ, CHECK\_GT, and so on. When check fails, the message after will be printed.

```c++
CHECK_LT(1, 2) << "This is definitely true, this log will never be seen";
CHECK_GT(1, 2) << "1 can't be greater than 2";
```

Run the above code you should see a fatal log and the calling stack：

```
FATAL: ... Check failed: 1 > 2 (1 vs 2). 1 can't be greater than 2
#0 0x000000afaa23 butil::debug::StackTrace::StackTrace()
#1 0x000000c29fec logging::LogStream::FlushWithoutReset()
#2 0x000000c2b8e6 logging::LogStream::Flush()
#3 0x000000c2bd63 logging::DestroyLogStream()
#4 0x000000c2a52d logging::LogMessage::~LogMessage()
#5 0x000000a716b2 (anonymous namespace)::StreamingLogTest_check_Test::TestBody()
#6 0x000000d16d04 testing::internal::HandleSehExceptionsInMethodIfSupported<>()
#7 0x000000d19e96 testing::internal::HandleExceptionsInMethodIfSupported<>()
#8 0x000000d08cd4 testing::Test::Run()
#9 0x000000d08dfe testing::TestInfo::Run()
#10 0x000000d08ec4 testing::TestCase::Run()
#11 0x000000d123c7 testing::internal::UnitTestImpl::RunAllTests()
#12 0x000000d16d94 testing::internal::HandleSehExceptionsInMethodIfSupported<>()
```

The second column of the callstack is the address of the code segment. You can use `addr2line` to check the corresponding file and line:

```
$ addr2line -e ./test_base 0x000000a716b2
/home/gejun/latest_baidu_rpc/public/common/test/test_streaming_log.cpp:223
```

You **should** use `CHECK_XX` for arithmetic condition so that you can see more detailed information when check failed.

```c++
int x = 1;
int y = 2;
CHECK_GT(x, y);  // Check failed: x > y (1 vs 2).
CHECK(x > y);    // Check failed: x > y.
```

Like DLOG, you should NOT include important side effects inside DCHECK.

<a id="c-base-streaming-log--logsink"></a>

## LogSink

The default destination of streaming log is the screen. You can change it through `logging::SetLogSink`. Users can inherit LogSink and implement their own output logic. We provide an internal LogSink as an example:

<a id="c-base-streaming-log--stringsink"></a>

### StringSink

Inherit both LogSink and string. Store log content inside string and mainly aim for unit test. The following case shows a classic usage of StringSink:

```c++
TEST_F(StreamingLogTest, log_at) {
    ::logging::StringSink log_str;
    ::logging::LogSink* old_sink = ::logging::SetLogSink(&log_str);
    LOG_AT(FATAL, "specified_file.cc", 12345) << "file/line is specified";
    // the file:line part should be using the argument given by us.
    ASSERT_NE(std::string::npos, log_str.find("specified_file.cc:12345"));
    // restore the old sink.
    ::logging::SetLogSink(old_sink);
}
```

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="client-access-grpc"></a>

<!-- source_url: https://brpc.apache.org/docs/client/access-grpc/ -->

<!-- page_index: 28 -->

# Access gRPC

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Access%20gRPC/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Access%20gRPC)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Access gRPC

Learn how to access gRPC.

Basics for accessing and serving http/h2 in brpc are listed in [http\_client](#client-access-httph2) and [http\_service](#server-serve-httph2).

Following section names are protocol names that can be directly set to ChannelOptions.protocol. The content after colon is parameters for the protocol to select derivative behaviors dynamically, but the base protocol is still http/1.x or http/2. As a result, these protocols are displayed at server-side as http or h2/h2c only.

<a id="client-access-grpc--httpjson-h2json"></a>

# http:json, h2:json

Non-empty pb request is serialized to json and set to the body of the http/h2 request. The Controller.request\_attachment() must be empty otherwise the RPC fails.

Non-empty pb response is converted from a json which is parsed from the body of the http/h2 response.

http/1.x behaves in this way by default, so “http” and “http:json” are just same.

<a id="client-access-grpc--httpproto-h2proto"></a>

# http:proto, h2:proto

Non-empty pb request is serialized (in pb’s wire format) and set to the body of the http/h2 request. The Controller.request\_attachment() must be empty otherwise the RPC fails.

Non-empty pb response is parsed from the body of the http/h2 response(in pb’s wire format).

http/2 behaves in this way by default, so “h2” and “h2:proto” are just same.

<a id="client-access-grpc--h2grpc"></a>

# h2:grpc

Default protocol of [gRPC](https://github.com/grpc). The detailed format is described in [gRPC over HTTP2](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md).

Clients using brpc should be able to talk with gRPC after changing ChannelOptions.protocol to “h2:grpc”.

Servers using brpc should be accessible by gRPC clients automatically without changing the code.

gRPC serializes message into pb wire format by default, so “h2:grpc” and “h2:grpc+proto” are just same.

TODO: Other configurations for gRPC

<a id="client-access-grpc--h2grpcjson"></a>

# h2:grpc+json

Comparing to h2:grpc, this protocol serializes messages into json instead of pb, which may not be supported by gRPC directly. For example, grpc-go users may reference [here](https://github.com/johanbrandhorst/grpc-json-example/blob/master/codec/json.go) to register the corresponding codec and turn on the support.

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="client-access-httph2"></a>

<!-- source_url: https://brpc.apache.org/docs/client/access-httph2/ -->

<!-- page_index: 29 -->

# Access http:h2

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Access%20http:h2/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Access%20http:h2)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Access http:h2

Learn how to access Http2.

<a id="client-access-httph2--example"></a>

# Example

[example/http\_c++](https://github.com/brpc/brpc/blob/master/example/http_c++/http_client.cpp)

<a id="client-access-httph2--about-h2"></a>

# About h2

brpc names the HTTP/2 protocol to “h2”, no matter encrypted or not. However HTTP/2 connections without SSL are shown on /connections with the official name “h2c”, and the ones with SSL are shown as “h2”.

The APIs for http and h2 in brpc are basically same. Without explicit statement, mentioned http features work for h2 as well.

<a id="client-access-httph2--create-channel"></a>

# Create Channel

In order to use `brpc::Channel` to access http/h2 services, `ChannelOptions.protocol` must be set to `PROTOCOL_HTTP` or `PROTOCOL_H2`.

Once the protocol is set, the first parameter of `Channel::Init` can be any valid URL. *Note*: Only host and port inside the URL are used by Init(), other parts are discarded. Allowing full URL simply saves the user from additional parsing code.

```c++
brpc::ChannelOptions options;
options.protocol = brpc::PROTOCOL_HTTP;  // or brpc::PROTOCOL_H2
if (channel.Init("www.baidu.com" /*any url*/, &options) != 0) {
     LOG(ERROR) << "Fail to initialize channel";
     return -1;
}
```

http/h2 channel also support BNS address or other naming services.

<a id="client-access-httph2--get"></a>

# GET

```c++
brpc::Controller cntl;
cntl.http_request().uri() = "www.baidu.com/index.html";  // Request URL
channel.CallMethod(NULL, &cntl, NULL, NULL, NULL/*done*/);
```

http/h2 does not relate to protobuf much, thus all parameters of `CallMethod` are NULL except `Controller` and `done`. Issue asynchronous RPC with non-NULL `done`.

`cntl.response_attachment()` is body of the http/h2 response and typed `butil::IOBuf`. `IOBuf` can be converted to `std::string` by `to_string()`, which needs to allocate memory and copy all data. If performance is important, the code should consider supporting `IOBuf` directly rather than requiring continuous memory.

<a id="client-access-httph2--post"></a>

# POST

The default HTTP Method is GET, which can be changed to POST or [other http methods](https://github.com/brpc/brpc/blob/master/src/brpc/http_method.h). The data to POST should be put into `request_attachment()`, which is typed [butil::IOBuf](https://github.com/brpc/brpc/blob/master/src/butil/iobuf.h) and able to append `std :: string` or `char *` directly.

```c++
brpc::Controller cntl;
cntl.http_request().uri() = "...";  // Request URL
cntl.http_request().set_method(brpc::HTTP_METHOD_POST);
cntl.request_attachment().append("{\"message\":\"hello world!\"}");
channel.CallMethod(NULL, &cntl, NULL, NULL, NULL/*done*/);
```

If the body needs a lot of printing to build, consider using `butil::IOBufBuilder`, which has same interfaces as `std::ostringstream`, probably simpler and more efficient than c-style printf when lots of objects need to be printed.

```c++
brpc::Controller cntl;
cntl.http_request().uri() = "...";  // Request URL
cntl.http_request().set_method(brpc::HTTP_METHOD_POST);
butil::IOBufBuilder os;
os << "A lot of printing" << printable_objects << ...;
os.move_to(cntl.request_attachment());
channel.CallMethod(NULL, &cntl, NULL, NULL, NULL/*done*/);
```

<a id="client-access-httph2--change-http-version"></a>

# Change HTTP version

brpc behaves as http/1.1 by default.

Comparing to http/1.1, http/1.0 lacks of long connections(KeepAlive). To communicate brpc client with some legacy http servers, the client may be configured as follows:

```c++
cntl.http_request().set_version(1, 0);
```

Setting http version does not work for h2, but the versions in h2 responses received by client and h2 requests received by server are set to (2, 0).

brpc server recognizes http versions automically and responds accordingly without users’ aid.

<a id="client-access-httph2--url"></a>

# URL

Genaral form of an URL:

```
// URI scheme : http://en.wikipedia.org/wiki/URI_scheme
//
//  foo://username:password@example.com:8042/over/there/index.dtb?type=animal&name=narwhal#nose
//  \_/   \_______________/ \_________/ \__/            \___/ \_/ \______________________/ \__/
//   |           |               |       |                |    |            |                |
//   |       userinfo           host    port              |    |          query          fragment
//   |    \________________________________/\_____________|____|/ \__/        \__/
// scheme                 |                          |    |    |    |          |
//                    authority                      |    |    |    |          |
//                                                 path   |    |    interpretable as keys
//                                                        |    |
//        \_______________________________________________|____|/       \____/     \_____/
//                             |                          |    |          |           |
//                     hierarchical part                  |    |    interpretable as values
//                                                        |    |
//                                   interpretable as filename |
//                                                             |
//                                                             |
//                                               interpretable as extension
```

As we saw in examples above, `Channel.Init()` and `cntl.http_request().uri()` both need the URL. Why does `uri()` need to be set additionally rather than using the URL to `Init()` directly?

Indeed, the settings are repeated in simple cases. But they are different in more complex scenes:

- Access multiple servers under a NamingService (for example BNS), in which case `Channel::Init` accepts a name meaningful to the NamingService(for example node names in BNS), while `uri()` is assigned with the URL.
- Access servers via http/h2 proxy, in which case `Channel::Init` takes the address of the proxy server, while `uri()` is still assigned with the URL.

<a id="client-access-httph2--host-header"></a>

## Host header

If user already sets `Host` header(case insensitive), framework makes no change.

If user does not set `Host` header and the URL has host, for example <http://www.foo.com/path>, the http request contains “Host: [www.foo.com](https://www.foo.com)”.

If user does not set host header and the URL does not have host as well, for example “/index.html?name=value”, but if the address initialized by the channel contains domain name. framework sets `Host` header with domain name of the target server. if this address is “<http://www.foo.com>”, this http server should see `Host: www.foo.com`, if this address is “<http://www.foo.com:8989>”, this http server should be see `Host: www.foo.com:8989`.

If user does not set host header and the URL does not have host as well, for example “/index.html?name=value”, and the address initialized by the channel doesn’t contain domain name. framework sets `Host` header with IP and port of the target server. A http server at 10.46.188.39:8989 should see `Host: 10.46.188.39:8989`.

The header is named “:authority” in h2.

<a id="client-access-httph2--common-usages"></a>

# Common usages

Take http request as an example (similar with http response), common operations are listed as follows:

Access an HTTP header named `Foo`

```c++
const std::string* value = cntl->http_request().GetHeader("Foo"); // NULL when not exist
```

Set an HTTP header named `Foo`

```c++
cntl->http_request().SetHeader("Foo", "value");
```

Access a query named `Foo`

```c++
const std::string* value = cntl->http_request().uri().GetQuery("Foo"); // NULL when not exist
```

Set a query named `Foo`

```c++
cntl->http_request().uri().SetQuery("Foo", "value");
```

Set HTTP method

```c++
cntl->http_request().set_method(brpc::HTTP_METHOD_POST);
```

Set the URL

```c++
cntl->http_request().uri() = "http://www.baidu.com";
```

Set the `content-type`

```c++
cntl->http_request().set_content_type("text/plain");
```

Get HTTP body

```c++
butil::IOBuf& buf = cntl->request_attachment();
std::string str = cntl->request_attachment().to_string(); // trigger copy underlying
```

Set HTTP body

```c++
cntl->request_attachment().append("....");
butil::IOBufBuilder os; os << "....";
os.move_to(cntl->request_attachment());
```

Notes on http header:

- field\_name of the header is case-insensitive according to [rfc2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2). brpc supports case-insensitive field names and keeps same cases at printing as users set.
- If multiple headers have same field names, according to [rfc2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html#sec4.2), values should be merged and separated by comma (,). Users figure out how to use this kind of values by their own.
- Queries are separated by “&” and key/value in a query are separated by “=”. Values can be omitted. For example, `key1=value1&key2&key3=value3` is a valid query string, in which the value for `key2` is an empty string.

<a id="client-access-httph2--debug-http-messages"></a>

# Debug HTTP messages

Turn on [-http\_verbose](http://brpc.baidu.com:8765/flags/http_verbose) so that the framework prints each http request and response. Note that this should only be used in tests or debuggings rather than online services.

<a id="client-access-httph2--http-errors"></a>

# HTTP errors

When server returns a non-2xx HTTP status code, the HTTP RPC is considered to be failed and `cntl->ErrorCode()` at client-side is set to `EHTTP`, users can check `cntl-> http_response().status_code()` for more specific HTTP error. In addition, server can put html or json describing the error into `cntl->response_attachment()` which is sent back to the client as http body.

<a id="client-access-httph2--compress-request-body"></a>

# Compress Request Body

`Controller::set_request_compress_type(brpc::COMPRESS_TYPE_GZIP)` makes framework try to gzip the HTTP body. “try to” means the compression may not happen, because:

- Size of body is smaller than bytes specified by -http\_body\_compress\_threshold, which is 512 by default. The reason is that gzip is not a very fast compression algorithm, when body is small, the delay caused by compression may even larger than the latency saved by faster transportation.

<a id="client-access-httph2--decompress-response-body"></a>

# Decompress Response Body

brpc does not decompress bodies of responses automatically due to universality. The decompression code is not complicated and users can do it by themselves. The code is as follows:

```c++
#include <brpc/policy/gzip_compress.h>
...
const std::string* encoding = cntl->http_response().GetHeader("Content-Encoding");
if (encoding != NULL && *encoding == "gzip") {
    butil::IOBuf uncompressed;
    if (!brpc::policy::GzipDecompress(cntl->response_attachment(), &uncompressed)) {
        LOG(ERROR) << "Fail to un-gzip response body";
        return;
    }
    cntl->response_attachment().swap(uncompressed);
}
// Now cntl->response_attachment() contains the decompressed data
```

<a id="client-access-httph2--progressively-download"></a>

# Progressively Download

http client normally does not complete the RPC until http body has been fully downloaded. During the process http body is stored in memory. If the body is very large or infinitely large(a FLV file for live streaming), memory grows continuously until the RPC is timedout. Such http clients are not suitable for downloading very large files.

brpc client supports completing RPC before reading the full body, so that users can read http bodies progressively after RPC. Note that this feature does not mean “support for http chunked mode”, actually the http implementation in brpc supports chunked mode from the very beginning. The real issue is how to let users handle very or infinitely large http bodies, which does not imply the chunked mode.

How to use:

1. Implement ProgressiveReader below:


```c++
#include <brpc/progressive_reader.h>
...
class ProgressiveReader {
public:
    // Called when one part was read.
    // Error returned is treated as *permenant* and the socket where the
    // data was read will be closed.
    // A temporary error may be handled by blocking this function, which
    // may block the HTTP parsing on the socket.
    virtual butil::Status OnReadOnePart(const void* data, size_t length) = 0;

    // Called when there's nothing to read anymore. The `status' is a hint for
    // why this method is called.
    // - status.ok(): the message is complete and successfully consumed.
    // - otherwise: socket was broken or OnReadOnePart() failed.
    // This method will be called once and only once. No other methods will
    // be called after. User can release the memory of this object inside.
    virtual void OnEndOfMessage(const butil::Status& status) = 0;
};
```

   `OnReadOnePart` is called each time a piece of data is read. `OnEndOfMessage` is called at the end of data or the connection is broken. Read comments carefully before implementing.
2. Set `cntl.response_will_be_read_progressively();` before RPC to make brpc end RPC just after reading all headers.
3. Call `cntl.ReadProgressiveAttachmentBy(new MyProgressiveReader);` after RPC. `MyProgressiveReader` is an instance of user-implemented `ProgressiveReader`. User may delete the object inside `OnEndOfMessage`.

<a id="client-access-httph2--progressively-upload"></a>

# Progressively Upload

Currently the POST data should be intact before launching the http call, thus brpc http client is still not suitable for uploading very large bodies.

<a id="client-access-httph2--access-servers-with-authentications"></a>

# Access Servers with authentications

Generate `auth_data` according to authenticating method of the server and set it into `Authorization` header. If you’re using curl, add option `-H "Authorization : <auth_data>"`.

<a id="client-access-httph2--send-https-requests"></a>

# Send https requests

https is short for “http over SSL”, SSL is not exclusive for http, but effective for all protocols. The generic method for turning on client-side SSL is [here](#client-basics--turn-on-ssl). brpc enables SSL automatically for URIs starting with https:// to make the usage more handy.

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="client-access-memcached"></a>

<!-- source_url: https://brpc.apache.org/docs/client/access-memcached/ -->

<!-- page_index: 30 -->

# Access memcached

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Access%20memcached/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Access%20memcached)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Access memcached

Learn how to access memcached.

[memcached](http://memcached.org/) is a common caching service. In order to access memcached more conveniently and make full use of bthread’s capability of concurrency, brpc directly supports the memcached protocol. Check [example/memcache\_c++](https://github.com/brpc/brpc/tree/master/example/memcache_c++/) for an example.

> [!NOTE]
> : brpc only supports the binary protocol of memcache. There’s little benefit to support the textual protocol which is replaced since memcached 1.3. If your memcached is older than 1.3, upgrade to a newer version.

Advantages compared to [libmemcached](http://libmemcached.org/libMemcached.html) (the official client):

The current implementation takes full advantage of the RPC concurrency mechanism and avoids copying as much as possible. A single client can easily pushes a memcached instance (version 1.4.15) on the same machine to its limit: 90,000 QPS for single connection, 330,000 QPS for multiple connections. In most cases, brpc is able to make full use of memcached’s capabilities.

<a id="client-access-memcached--request-a-memcached-server"></a>

# Request a memcached server

Create a `Channel` for accessing memcached:

```c++
#include <brpc/memcache.h>
#include <brpc/channel.h>
 
brpc::ChannelOptions options;
options.protocol = brpc::PROTOCOL_MEMCACHE;
if (channel.Init("0.0.0.0:11211", &options) != 0) {  // 11211 is the default port for memcached
   LOG(FATAL) << "Fail to init channel to memcached";
   return -1;
}
... 
```

Following example tries to set data to memcached:

```c++
// Set key="hello" value="world" flags=0xdeadbeef, expire in 10s, and ignore cas
brpc::MemcacheRequest request;
brpc::MemcacheResponse response;
brpc::Controller cntl;
if (!request.Set("hello", "world", 0xdeadbeef/*flags*/, 10/*expiring seconds*/, 0/*ignore cas*/)) {
    LOG(FATAL) << "Fail to SET request";
    return -1;
} 
channel.CallMethod(NULL, &cntl, &request, &response, NULL/*done*/);
if (cntl.Failed()) {
    LOG(FATAL) << "Fail to access memcached, " << cntl.ErrorText();
    return -1;
}  
if (!response.PopSet(NULL)) {
    LOG(FATAL) << "Fail to SET memcached, " << response.LastError();
    return -1;   
}
...
```

Notes on above code:

- The class of the request must be `MemcacheRequest`, response must be `MemcacheResponse`, otherwise `CallMethod` fails. `stub` is not necessary, just call `channel.CallMethod` with `method` to NULL.
- Call `request.XXX()` to add an operation, where `XXX` is `Set` in this example. Multiple operations inside a request are sent to a memcached server together (often referred to as “pipeline mode”).
- call `response.PopXXX()` to pop result of an operation from the response, where `XXX` is `Set` in this example. true is returned on success, and false otherwise in which case use `response.LastError()` to get the error message. `XXX` must match the corresponding operation in the request, otherwise the pop is rejected. In above example, a `PopGet` would fail with the error message of “not a GET response”.
- Results of `Pop` are independent from the RPC result. Even if “a value cannot be put into the memcached”, the RPC may still be successful. RPC failure means things like broken connection, timeout etc. If the business logic requires the memcache operations to be succesful, you should test successfulness of both RPC and `PopXXX`.

Supported operations currently:

```c++
bool Set(const Slice& key, const Slice& value, uint32_t flags, uint32_t exptime, uint64_t cas_value);
bool Add(const Slice& key, const Slice& value, uint32_t flags, uint32_t exptime, uint64_t cas_value);
bool Replace(const Slice& key, const Slice& value, uint32_t flags, uint32_t exptime, uint64_t cas_value);
bool Append(const Slice& key, const Slice& value, uint32_t flags, uint32_t exptime, uint64_t cas_value);
bool Prepend(const Slice& key, const Slice& value, uint32_t flags, uint32_t exptime, uint64_t cas_value);
bool Delete(const Slice& key);
bool Flush(uint32_t timeout);
bool Increment(const Slice& key, uint64_t delta, uint64_t initial_value, uint32_t exptime);
bool Decrement(const Slice& key, uint64_t delta, uint64_t initial_value, uint32_t exptime);
bool Touch(const Slice& key, uint32_t exptime);
bool Version();
```

Corresponding operations in replies:

```c++
// Call LastError() of the response to check the error text when any following operation fails.
bool PopGet(IOBuf* value, uint32_t* flags, uint64_t* cas_value);
bool PopGet(std::string* value, uint32_t* flags, uint64_t* cas_value);
bool PopSet(uint64_t* cas_value);
bool PopAdd(uint64_t* cas_value);
bool PopReplace(uint64_t* cas_value);
bool PopAppend(uint64_t* cas_value);
bool PopPrepend(uint64_t* cas_value);
bool PopDelete();
bool PopFlush();
bool PopIncrement(uint64_t* new_value, uint64_t* cas_value);
bool PopDecrement(uint64_t* new_value, uint64_t* cas_value);
bool PopTouch();
bool PopVersion(std::string* version);
```

<a id="client-access-memcached--request-a-memcached-cluster"></a>

# Request a memcached cluster

Create a `Channel` using the `c_md5` as the load balancing algorithm to access a memcached cluster mounted under a naming service. Note that each `MemcacheRequest` should contain only one operation or all operations have the same key. Under current implementation, multiple operations inside a single request are always sent to a same server. If the keys are located on different servers, the result must be wrong. In which case, you have to divide the request into multilple ones with one operation each.

Another choice is to use the common [twemproxy](https://github.com/twitter/twemproxy) solution, which makes clients access the cluster just like accessing a single server, although the solution needs to deploy proxies and adds more latency.

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="client-access-redis"></a>

<!-- source_url: https://brpc.apache.org/docs/client/access-redis/ -->

<!-- page_index: 31 -->

# Access redis

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Access%20redis/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Access%20redis)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Access redis

Learn how to access redis.

[redis](http://redis.io/) is one of the most popular caching service in recent years. Compared to memcached it provides users with more data structures and operations, speeding up developments. In order to access redis servers more conveniently and make full use of bthread’s capability of concurrency, brpc directly supports the redis protocol. Check [example/redis\_c++](https://github.com/brpc/brpc/tree/master/example/redis_c++/) for an example.

Advantages compared to [hiredis](https://github.com/redis/hiredis) (the official redis client):

Similarly with http, brpc guarantees that the time complexity of parsing redis replies is O(N) in worst cases rather than O(N^2) , where N is the number of bytes of reply. This is important when the reply consists of large arrays.

Turn on [-redis\_verbose](#client-access-redis--debug) to print contents of all redis requests and responses, which is for debugging only.

<a id="client-access-redis--request-a-redis-server"></a>

# Request a redis server

Create a `Channel` for accessing redis:

```c++
#include <brpc/redis.h>
#include <brpc/channel.h>
  
brpc::ChannelOptions options;
options.protocol = brpc::PROTOCOL_REDIS;
brpc::Channel redis_channel;
if (redis_channel.Init("0.0.0.0:6379", &options) != 0) {  // 6379 is the default port for redis-server
   LOG(ERROR) << "Fail to init channel to redis-server";
   return -1;
}
...
```

Execute `SET`, then `INCR`:

```c++
std::string my_key = "my_key_1";
int my_number = 1;
...
// Execute "SET <my_key> <my_number>"
brpc::RedisRequest set_request;
brpc::RedisResponse response;
brpc::Controller cntl;
set_request.AddCommand("SET %s %d", my_key.c_str(), my_number);
redis_channel.CallMethod(NULL, &cntl, &set_request, &response, NULL/*done*/);
if (cntl.Failed()) {
    LOG(ERROR) << "Fail to access redis-server";
    return -1;
}
// Get a reply by calling response.reply(i)
if (response.reply(0).is_error()) {
    LOG(ERROR) << "Fail to set";
    return -1;
}
// A reply is printable in multiple ways
LOG(INFO) << response.reply(0).c_str()  // OK
          << response.reply(0)          // OK
          << response;                  // OK
...
 
// Execute "INCR <my_key>"
brpc::RedisRequest incr_request;
incr_request.AddCommand("INCR %s", my_key.c_str());
response.Clear();
cntl.Reset();
redis_channel.CallMethod(NULL, &cntl, &incr_request, &response, NULL/*done*/);
if (cntl.Failed()) {
    LOG(ERROR) << "Fail to access redis-server";
    return -1;
}
if (response.reply(0).is_error()) {
    LOG(ERROR) << "Fail to incr";
    return -1;
}
// A reply is printable in multiple ways
LOG(INFO) << response.reply(0).integer()  // 2
          << response.reply(0)            // (integer) 2
          << response;                    // (integer) 2
```

Execute `incr` and `decr` in batch:

```c++
brpc::RedisRequest request;
brpc::RedisResponse response;
brpc::Controller cntl;
request.AddCommand("INCR counter1");
request.AddCommand("DECR counter1");
request.AddCommand("INCRBY counter1 10");
request.AddCommand("DECRBY counter1 20");
redis_channel.CallMethod(NULL, &cntl, &request, &response, NULL/*done*/);
if (cntl.Failed()) {
    LOG(ERROR) << "Fail to access redis-server";
    return -1;
}
CHECK_EQ(4, response.reply_size());
for (int i = 0; i < 4; ++i) {
    CHECK(response.reply(i).is_integer());
    CHECK_EQ(brpc::REDIS_REPLY_INTEGER, response.reply(i).type());
}
CHECK_EQ(1, response.reply(0).integer());
CHECK_EQ(0, response.reply(1).integer());
CHECK_EQ(10, response.reply(2).integer());
CHECK_EQ(-10, response.reply(3).integer());
```

<a id="client-access-redis--redisrequest"></a>

# RedisRequest

A [RedisRequest](https://github.com/brpc/brpc/blob/master/src/brpc/redis.h) may contain multiple commands by calling `AddCommand*`, which returns true on success and false otherwise. **The callsite backtrace is also printed on error**.

```c++
bool AddCommand(const char* fmt, ...);
bool AddCommandV(const char* fmt, va_list args);
bool AddCommandByComponents(const butil::StringPiece* components, size_t n);
```

Formatting is compatible with hiredis, namely `%b` corresponds to binary data (pointer + length), others are similar to those in `printf`. Some improvements have been made such as characters enclosed by single or double quotes are recognized as one field regardless of the spaces inside. For example, `AddCommand("Set 'a key with space' 'a value with space as well'")` sets value `a value with space as well` to key `a key with space`, while in hiredis the command must be written as `redisvCommand(..., "SET% s% s", "a key with space", "a value with space as well");`

`AddCommandByComponents` is similar to `redisCommandArgv` in hiredis. Users specify each part of the command in an array, which is immune to escaping issues often occurring in `AddCommand` and `AddCommandV`. If you encounter errors such as “Unmatched quote” or “invalid format” when using `AddCommand` and `AddCommandV`, try this method.

If `AddCommand*` fails, subsequent `AddCommand*` and `CallMethod` also fail. In general, there is no need to check return value of `AddCommand*`, since the RPC fails directly anyway.

Use `command_size()` to get number of commands added successfully.

Call `Clear()` before re-using the `RedisRequest` object.

<a id="client-access-redis--redisresponse"></a>

# RedisResponse

A [RedisResponse](https://github.com/brpc/brpc/blob/master/src/brpc/redis.h) may contain one or multiple [RedisReply](https://github.com/brpc/brpc/blob/master/src/brpc/redis_reply.h)s. Use `reply_size()` for total number of replies and `reply(i)` for reference to the i-th reply (counting from 0). Note that in hiredis, if the request contains N commands, you have to call `redisGetReply` N times to get replies, while it’s unnecessary in brpc as the `RedisResponse` already includes the N replies which are accessible by reply(i). As long as RPC is successful, `response.reply_size()` should be equal to `request.command_size()`, unless the redis-server is buggy. The precondition that redis works correctly is that replies correspond to commands one by one in the same sequence (positional correspondence).

Each `RedisReply` may be:

- REDIS\_REPLY\_NIL: NULL in redis, which means value does not exist. Testable by `is_nil()`.
- REDIS\_REPLY\_STATUS: Referred to `Simple String` in the redis document, usually used as the status of operations, such as the `OK` returned by `SET`. Testable by `is_string()` (same function for REDIS\_REPLY\_STRING). Use `c_str()` or `data()` to get the value.
- REDIS\_REPLY\_STRING: Referred to `Bulk String` in the redis document. Most return values are of this type, including those returned by `incr`. Testable by `is_string()`. Use `c_str()` or `data()` for the value.
- REDIS\_REPLY\_ERROR: The error message for a failed operation. Testable by `is_error()`. Use `error_message()` to get the message.
- REDIS\_REPLY\_INTEGER: A 64-bit signed integer. Testable by `is_integer()`. Use `integer()` to get the value.
- REDIS\_REPLY\_ARRAY: Array of replies. Testable by `is_array()`. Use `size()` for size of the array and `[i]` for the reference to the corresponding sub-reply.

If a response contains three replies: an integer, a string and an array with 2 items, we can use `response.reply(0).integer()`, `response.reply(1).c_str()`, and `repsonse.reply(2)[0]`, `repsonse.reply(2)[1]` to fetch values respectively. If the type is not correct, backtrace of the callsite is printed and an undefined value is returned.

Ownership of all replies belongs to `RedisResponse`. All relies are destroyed when response is destroyed.

Call `Clear()` before re-using the `RedisRespones` object.

<a id="client-access-redis--request-a-redis-cluster"></a>

# Request a redis cluster

Create a `Channel` using the consistent hashing as the load balancing algorithm(c\_md5 or c\_murmurhash) to access a redis cluster mounted under a naming service. Note that each `RedisRequest` should contain only one command or all commands have the same key. Under current implementation, multiple commands inside a single request are always sent to a same server. If the keys are located on different servers, the result must be wrong. In which case, you have to divide the request into multilple ones with one command each.

Another choice is to use the common [twemproxy](https://github.com/twitter/twemproxy) solution, which makes clients access the cluster just like accessing a single server, although the solution needs to deploy proxies and adds more latency.

<a id="client-access-redis--debug"></a>

# Debug

Turn on [-redis\_verbose](http://brpc.baidu.com:8765/flags/redis_verbose) to print contents of all redis requests and responses. Note that this should only be used for debugging rather than online services.

Turn on [-redis\_verbose\_crlf2space](http://brpc.baidu.com:8765/flags/redis_verbose_crlf2space) to replace the `CRLF` (\r\n) with spaces in debugging logs for better readability.

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| redis\_verbose | false | [DEBUG] Print EVERY redis request/response | src/brpc/policy/redis\_protocol.cpp |
| redis\_verbose\_crlf2space | false | [DEBUG] Show \r\n as a space | src/brpc/redis.cpp |

<a id="client-access-redis--performance"></a>

# Performance

redis version: 2.6.14

Start a client to send requests to a redis-server on the same machine using 1, 50, 200 bthreads synchronously. The latency is in microseconds.

```
$ ./client -use_bthread -thread_num 1
TRACE: 02-13 19:42:04:   * 0 client.cpp:180] Accessing redis server at qps=18668 latency=50
TRACE: 02-13 19:42:05:   * 0 client.cpp:180] Accessing redis server at qps=17043 latency=52
TRACE: 02-13 19:42:06:   * 0 client.cpp:180] Accessing redis server at qps=16520 latency=54

$ ./client -use_bthread -thread_num 50
TRACE: 02-13 19:42:54:   * 0 client.cpp:180] Accessing redis server at qps=301212 latency=164
TRACE: 02-13 19:42:55:   * 0 client.cpp:180] Accessing redis server at qps=301203 latency=164
TRACE: 02-13 19:42:56:   * 0 client.cpp:180] Accessing redis server at qps=302158 latency=164

$ ./client -use_bthread -thread_num 200
TRACE: 02-13 19:43:48:   * 0 client.cpp:180] Accessing redis server at qps=411669 latency=483
TRACE: 02-13 19:43:49:   * 0 client.cpp:180] Accessing redis server at qps=411679 latency=483
TRACE: 02-13 19:43:50:   * 0 client.cpp:180] Accessing redis server at qps=412583 latency=482
```

The peak QPS at 200 threads is much higher than hiredis since brpc uses a single connection to redis-server by default and requests from multiple threads are [merged in a wait-free way](https://brpc.apache.org/docs/rpc-in-depth/io#sending-messages), making the redis-server receive requests in batch and reach a much higher QPS. The lower QPS in following test that uses pooled connections is another proof.

Start a client to send requests in batch (10 commands per request) to redis-server on the same machine using 1, 50, 200 bthreads synchronously. The latency is in microseconds.

```
$ ./client -use_bthread -thread_num 1 -batch 10
TRACE: 02-13 19:46:45:   * 0 client.cpp:180] Accessing redis server at qps=15880 latency=59
TRACE: 02-13 19:46:46:   * 0 client.cpp:180] Accessing redis server at qps=16945 latency=57
TRACE: 02-13 19:46:47:   * 0 client.cpp:180] Accessing redis server at qps=16728 latency=57

$ ./client -use_bthread -thread_num 50 -batch 10
TRACE: 02-13 19:47:14:   * 0 client.cpp:180] Accessing redis server at qps=38082 latency=1307
TRACE: 02-13 19:47:15:   * 0 client.cpp:180] Accessing redis server at qps=38267 latency=1304
TRACE: 02-13 19:47:16:   * 0 client.cpp:180] Accessing redis server at qps=38070 latency=1305
 
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND 
16878 gejun     20   0 48136 2436 1004 R 93.8  0.0  12:48.56 redis-server   // thread_num=50

$ ./client -use_bthread -thread_num 200 -batch 10
TRACE: 02-13 19:49:09:   * 0 client.cpp:180] Accessing redis server at qps=29053 latency=6875
TRACE: 02-13 19:49:10:   * 0 client.cpp:180] Accessing redis server at qps=29163 latency=6855
TRACE: 02-13 19:49:11:   * 0 client.cpp:180] Accessing redis server at qps=29271 latency=6838
 
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND 
16878 gejun     20   0 48136 2508 1004 R 99.9  0.0  13:36.59 redis-server   // thread_num=200
```

Note that the commands processed per second by the redis-server is the QPS times 10, which is about 400K. When thread\_num equals 50 or higher, the CPU usage of the redis-server reaches limit. Note that redis-server is a [single-threaded reactor](#rpc-in-depth-threading-overview--single-threaded-reactorhttpenwikipediaorgwikireactor_pattern), utilizing one core is the maximum that it can do.

Now start a client to send requests to redis-server on the same machine using 50 bthreads synchronously through pooled connections.

```
$ ./client -use_bthread -connection_type pooled
TRACE: 02-13 18:07:40:   * 0 client.cpp:180] Accessing redis server at qps=75986 latency=654
TRACE: 02-13 18:07:41:   * 0 client.cpp:180] Accessing redis server at qps=75562 latency=655
TRACE: 02-13 18:07:42:   * 0 client.cpp:180] Accessing redis server at qps=75238 latency=657
 
  PID USER      PR  NI  VIRT  RES  SHR S %CPU %MEM    TIME+  COMMAND
16878 gejun     20   0 48136 2520 1004 R 99.9  0.0   9:52.33 redis-server
```

We can see a tremendous drop of QPS compared to the one using single connection above, and the redis-server has reached the CPU cap. The cause is that each time only one request can be read from a connection by the redis-server, which significantly increases cost of IO operations. This is also the peak performance of a hiredis client.

<a id="client-access-redis--command-line-interface"></a>

# Command Line Interface

[example/redis\_c++/redis\_cli](https://github.com/brpc/brpc/blob/master/example/redis_c%2B%2B/redis_cli.cpp) is a command line tool similar to the official CLI, demostrating brpc’s capability to talk with redis servers. When unexpected results are got from a redis-server using a brpc client, you can debug with this tool interactively as well.

Like the official CLI, `redis_cli <command>` runs the command directly, and `-server` which is address of the redis-server can be specified.

```
$ ./redis_cli __ _ __/ /_ ____ _(_)___/ /_ __ _________ _____/ __ \/ __ `/ / __ / / / /_____/ ___/ __ \/ ___// /_/ / /_/ / / /_/ / /_/ /_____/ / / /_/ / /__
 /_.___/\__,_/_/\__,_/\__,_/     /_/  / .___/\___/  
                                     /_/            
This command-line tool mimics the look-n-feel of official redis-cli, as a 
demostration of brpc's capability of talking to redis server. The 
output and behavior is not exactly same with the official one.
 
redis 127.0.0.1:6379> mset key1 foo key2 bar key3 17
OK
redis 127.0.0.1:6379> mget key1 key2 key3
["foo", "bar", "17"]
redis 127.0.0.1:6379> incrby key3 10
(integer) 27
redis 127.0.0.1:6379> client setname brpc-cli
OK
redis 127.0.0.1:6379> client getname
"brpc-cli"
```

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="client-access-thrift"></a>

<!-- source_url: https://brpc.apache.org/docs/client/access-thrift/ -->

<!-- page_index: 32 -->

# Access thrift

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Access%20thrift/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Access%20thrift)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [server side return string “hello” sent from client](#client-access-thrift--server-side-return-string-hello-sent-from-client)
- [server side return string “hello” \* 1000](#client-access-thrift--server-side-return-string-hello-1000)
- [server side do some complicated math and return string “hello” \* 1000](#client-access-thrift--server-side-do-some-complicated-math-and-return-string-hello-1000)

# Access thrift

Learn how to access thrift.

[thrift](https://thrift.apache.org/) is a RPC framework used widely in various environments, which was developed by Facebook and adopted by Apache later. In order to interact with thrift servers and solves issues on thread-safety, usabilities and concurrencies, brpc directly supports the thrift protocol that is used by thrift in NonBlocking mode.

Example: [example/thrift\_extension\_c++](https://github.com/brpc/brpc/tree/master/example/thrift_extension_c++/).

Advantages compared to the official solution:

- Thread safety. No need to set up separate clients for each thread.
- Supports synchronous, asynchronous, batch synchronous, batch asynchronous, and other access methods. Combination channels such as ParallelChannel are also supported.
- Support various connection types(short, connection pool). Support timeout, backup request, cancellation, tracing, built-in services, and other benefits offered by brpc.
- Better performance.

<a id="client-access-thrift--compile"></a>

# Compile

brpc depends on the thrift library and reuses some code generated by thrift tools. Please read official documents to find out how to write thrift files, generate code, compilations etc.

brpc does not enable thrift support or depend on the thrift lib by default. If the support is needed, compile brpc with extra –with-thrift or -DWITH\_THRIFT=ON

Install thrift under Linux
Read [Official wiki](https://thrift.apache.org/docs/install/debian) to install depended libs and tools, then download thrift source code from [official site](https://thrift.apache.org/download), uncompress and compile。

```bash
wget http://www.apache.org/dist/thrift/0.11.0/thrift-0.11.0.tar.gz
tar -xf thrift-0.11.0.tar.gz
cd thrift-0.11.0/
./configure --prefix=/usr --with-ruby=no --with-python=no --with-java=no --with-go=no --with-perl=no --with-php=no --with-csharp=no --with-erlang=no --with-lua=no --with-nodejs=no
make CPPFLAGS=-DFORCE_BOOST_SMART_PTR -j 4 -s
sudo make install
```

Config brpc with thrift support, then make. The compiled libbrpc.a includes extended code for thrift support and can be linked normally as in other brpc projects.

```bash
# Ubuntu sh config_brpc.sh --headers=/usr/include --libs=/usr/lib --with-thrift
# Fedora/CentOS sh config_brpc.sh --headers=/usr/include --libs=/usr/lib64 --with-thrift
# Or use cmake mkdir build && cd build && cmake ../ -DWITH_THRIFT=ON
```

Read [Getting Started](#getting_started) for more compilation options.

<a id="client-access-thrift--client-accesses-thrift-server"></a>

# Client accesses thrift server

Steps：

- Create a Channel setting protocol to brpc::PROTOCOL\_THRIFT
- Create brpc::ThriftStub
- Use native request and response to start RPC directly.

Example code:

```c++
#include <brpc/channel.h>
#include <brpc/thrift_message.h>         // Defines ThriftStub
...

DEFINE_string(server, "0.0.0.0:8019", "IP Address of thrift server");
DEFINE_string(load_balancer, "", "The algorithm for load balancing");
...
  
brpc::ChannelOptions options;
options.protocol = brpc::PROTOCOL_THRIFT;
brpc::Channel thrift_channel;
if (thrift_channel.Init(Flags_server.c_str(), FLAGS_load_balancer.c_str(), &options) != 0) {
   LOG(ERROR) << "Fail to initialize thrift channel";
   return -1;
}

brpc::ThriftStub stub(&thrift_channel);
...

// example::[EchoRequest/EchoResponse] are types generated by thrift
example::EchoRequest req;
example::EchoResponse res;
req.data = "hello";

stub.CallMethod("Echo", &cntl, &req, &res, NULL);
if (cntl.Failed()) {
    LOG(ERROR) << "Fail to send thrift request, " << cntl.ErrorText();
    return -1;
} 
```

<a id="client-access-thrift--server-processes-thrift-requests"></a>

# Server processes thrift requests

Inherit brpc::ThriftService to implement the processing code, which may call the native handler generated by thrift to re-use existing entry directly, or read the request and set the response directly just as in other protobuf services.

```c++
class EchoServiceImpl : public brpc::ThriftService {
public:
    void ProcessThriftFramedRequest(brpc::Controller* cntl,
                                    brpc::ThriftFramedMessage* req,
                                    brpc::ThriftFramedMessage* res,
                                    google::protobuf::Closure* done) override {
        // Dispatch calls to different methods
        if (cntl->thrift_method_name() == "Echo") {
            return Echo(cntl, req->Cast<example::EchoRequest>(),
                        res->Cast<example::EchoResponse>(), done);
        } else {
            cntl->SetFailed(brpc::ENOMETHOD, "Fail to find method=%s",
                            cntl->thrift_method_name().c_str());
            done->Run();
        }
    }

    void Echo(brpc::Controller* cntl,
              const example::EchoRequest* req,
              example::EchoResponse* res,
              google::protobuf::Closure* done) {
        // This object helps you to call done->Run() in RAII style. If you need
        // to process the request asynchronously, pass done_guard.release().
        brpc::ClosureGuard done_guard(done);

        res->data = req->data + " (processed)";
    }
};
```

Set the implemented service to ServerOptions.thrift\_service and start the service.

```c++
    brpc::Server server;
    brpc::ServerOptions options;
    options.thrift_service = new EchoServiceImpl;
    options.idle_timeout_sec = FLAGS_idle_timeout_s;
    options.max_concurrency = FLAGS_max_concurrency;

    // Start the server.
    if (server.Start(FLAGS_port, &options) != 0) {
        LOG(ERROR) << "Fail to start EchoServer";
        return -1;
    }
```

<a id="client-access-thrift--performance-test-for-native-thrift-compare-with-brpc-thrift-implementaion"></a>

# Performance test for native thrift compare with brpc thrift implementaion

Test Env: 48 core 2.30GHz

<a id="client-access-thrift--server-side-return-string-hello-sent-from-client"></a>

## server side return string “hello” sent from client

| Framework | Threads Num | QPS | Avg lantecy | CPU |
| --- | --- | --- | --- | --- |
| native thrift | 60 | 6.9w | 0.9ms | 2.8% |
| brpc thrift | 60 | 30w | 0.2ms | 18% |

<a id="client-access-thrift--server-side-return-string-hello-1000"></a>

## server side return string “hello” \* 1000

| Framework | Threads Num | QPS | Avg lantecy | CPU |
| --- | --- | --- | --- | --- |
| native thrift | 60 | 5.2w | 1.1ms | 4.5% |
| brpc thrift | 60 | 19.5w | 0.3ms | 22% |

<a id="client-access-thrift--server-side-do-some-complicated-math-and-return-string-hello-1000"></a>

## server side do some complicated math and return string “hello” \* 1000

| Framework | Threads Num | QPS | Avg lantecy | CPU |
| --- | --- | --- | --- | --- |
| native thrift | 60 | 1.7w | 3.5ms | 76% |
| brpc thrift | 60 | 2.1w | 2.9ms | 93% |

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="client-access-ub"></a>

<!-- source_url: https://brpc.apache.org/docs/client/access-ub/ -->

<!-- page_index: 33 -->

# Access UB

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Access%20UB/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Access%20UB)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Access UB

Learn how to access UB.

brpc可通过多种方式访问用ub搭建的服务。

<a id="client-access-ub--ubrpc-by-protobuf"></a>

# ubrpc (by protobuf)

r31687后，brpc支持通过protobuf访问ubrpc，不需要baidu-rpc-ub，也不依赖idl-compiler。（也可以让protobuf服务被ubrpc client访问，方法见[使用ubrpc的服务](https://github.com/apache/brpc/blob/master/docs/cn/nshead_service.md#%E4%BD%BF%E7%94%A8ubrpc%E7%9A%84%E6%9C%8D%E5%8A%A1)）。

**步骤：**

1. 用[idl2proto](https://github.com/brpc/brpc/blob/master/tools/idl2proto)把idl文件转化为proto文件，老版本idl2proto不会转化idl中的service，需要手动转化。


```protobuf
// Converted from echo.idl by brpc/tools/idl2proto
import "idl_options.proto";
option (idl_support) = true;
option cc_generic_services = true;
message EchoRequest {
  required string message = 1; 
}
message EchoResponse {
  required string message = 1; 
}

// 对于idl中多个request或response的方法，要建立一个包含所有request或response的消息。
// 这个例子中就是MultiRequests和MultiResponses。
message MultiRequests {
  required EchoRequest req1 = 1;
  required EchoRequest req2 = 2;
}
message MultiResponses {
  required EchoRequest res1 = 1;
  required EchoRequest res2 = 2;
}

service EchoService {
  // 对应idl中的void Echo(EchoRequest req, out EchoResponse res);
  rpc Echo(EchoRequest) returns (EchoResponse);

  // 对应idl中的uint32_t EchoWithMultiArgs(EchoRequest req1, EchoRequest req2, out EchoResponse res1, out EchoResponse res2);
  rpc EchoWithMultiArgs(MultiRequests) returns (MultiResponses);
}
```

   原先的echo.idl文件：


```idl
struct EchoRequest {
    string message;
};

struct EchoResponse {
    string message;
};

service EchoService {
    void Echo(EchoRequest req, out EchoResponse res);
    uint32_t EchoWithMultiArgs(EchoRequest req1, EchoRequest req2, out EchoResponse res1, out EchoResponse res2);
};
```

2. 插入如下片段以使用代码生成插件。

   BRPC\_PATH代表brpc产出的路径（包含bin include等目录），PROTOBUF\_INCLUDE\_PATH代表protobuf的包含路径。注意–mcpack\_out要和–cpp\_out一致。


```shell
protoc --plugin=protoc-gen-mcpack=$BRPC_PATH/bin/protoc-gen-mcpack --cpp_out=. --mcpack_out=. --proto_path=$BRPC_PATH/include --proto_path=PROTOBUF_INCLUDE_PATH
```

3. 用channel发起访问。

   idl不同于pb，允许有多个请求，我们先看只有一个请求的情况，和普通的pb访问基本上是一样的。


```c++
#include <brpc/channel.h>
#include "echo.pb.h"
...

brpc::Channel channel;
brpc::ChannelOptions opt;
opt.protocol = brpc::PROTOCOL_UBRPC_COMPACK; // or "ubrpc_compack";
if (channel.Init(..., &opt) != 0) {
    LOG(ERROR) << "Fail to init channel";
    return -1;
}
EchoService_Stub stub(&channel);
...

EchoRequest request;
EchoResponse response;
brpc::Controller cntl;

request.set_message("hello world");

stub.Echo(&cntl, &request, &response, NULL);

if (cntl.Failed()) {
    LOG(ERROR) << "Fail to send request, " << cntl.ErrorText();
    return;
}
// 取response中的字段
// [idl] void Echo(EchoRequest req, out EchoResponse res);
//                              ^ 
//                  response.message();
```

   多个请求要设置一下set\_idl\_names。


```c++
#include <brpc/channel.h>
#include "echo.pb.h"
...

brpc::Channel channel;
brpc::ChannelOptions opt;
opt.protocol = brpc::PROTOCOL_UBRPC_COMPACK; // or "ubrpc_compack";
if (channel.Init(..., &opt) != 0) {
    LOG(ERROR) << "Fail to init channel";
    return -1;
}
EchoService_Stub stub(&channel);
...

MultiRequests multi_requests;
MultiResponses multi_responses;
brpc::Controller cntl;

multi_requests.mutable_req1()->set_message("hello");
multi_requests.mutable_req2()->set_message("world");
cntl.set_idl_names(brpc::idl_multi_req_multi_res);
stub.EchoWithMultiArgs(&cntl, &multi_requests, &multi_responses, NULL);

if (cntl.Failed()) {
    LOG(ERROR) << "Fail to send request, " << cntl.ErrorText();
    return;
}
// 取response中的字段
// [idl] uint32_t EchoWithMultiArgs(EchoRequest req1, EchoRequest req2,
//        ^                         out EchoResponse res1, out EchoResponse res2);
//        |                                           ^                      ^
//        |                          multi_responses.res1().message();       |
//        |                                                 multi_responses.res2().message();
// cntl.idl_result();
```

   例子详见[example/echo\_c++\_ubrpc\_compack](https://github.com/brpc/brpc/blob/master/example/echo_c++_ubrpc_compack/)。

<a id="client-access-ub--ubrpc-by-baidu-rpc-ub"></a>

# ubrpc (by baidu-rpc-ub)

server端由public/ubrpc搭建，request/response使用idl文件描述字段，序列化格式是compack或mcpack\_v2。

**步骤：**

1. 依赖public/baidu-rpc-ub模块，这个模块是brpc的扩展，不需要的用户不会依赖idl/mcpack/compack等模块。baidu-rpc-ub只包含扩展代码，brpc中的新特性会自动体现在这个模块中。
2. 编写一个proto文件，其中定义了service，名字和idl中的相同，但请求类型必须是baidu.rpc.UBRequest，回复类型必须是baidu.rpc.UBResponse。这两个类型定义在brpc/ub.proto中，使用时得import。


```protobuf
import "brpc/ub.proto";              // UBRequest, UBResponse
option cc_generic_services = true;
// Define UB service. request/response must be UBRequest/UBResponse
service EchoService {
    rpc Echo(baidu.rpc.UBRequest) returns (baidu.rpc.UBResponse);
};
```

3. 在COMAKE包含baidu-rpc-ub/src路径。


```python
# brpc/ub.proto的包含路径
PROTOC(ENV.WorkRoot()+"third-64/protobuf/bin/protoc")
PROTOFLAGS("--proto_path=" + ENV.WorkRoot() + "public/baidu-rpc-ub/src/")
```

4. 用法和访问其他协议类似：创建Channel，ChannelOptions.protocol为**brpc::PROTOCOL\_NSHEAD\_CLIENT**或\*\*“nshead\_client”\*\*。request和response对象必须是baidu-rpc-ub提供的类型


```c++
#include <brpc/ub_call.h>
...

brpc::Channel channel;
brpc::ChannelOptions opt;
opt.protocol = brpc::PROTOCOL_NSHEAD_CLIENT; // or "nshead_client";
if (channel.Init(..., &opt) != 0) {
    LOG(ERROR) << "Fail to init channel";
    return -1;
}
EchoService_Stub stub(&channel);    
...

const int BUFSIZE = 1024 * 1024;  // 1M
char* buf_for_mempool = new char[BUFSIZE];
bsl::xmempool pool;
if (pool.create(buf_for_mempool, BUFSIZE) != 0) {
    LOG(FATAL) << "Fail to create bsl::xmempool";
    return -1;
}

// 构造UBRPC的request/response，idl结构体作为模块参数传入。为了构造idl结构，需要传入一个bsl::mempool
brpc::UBRPCCompackRequest<example::EchoService_Echo_params> request(&pool);
brpc::UBRPCCompackResponse<example::EchoService_Echo_response> response(&pool);

// 设置字段
request.mutable_req()->set_message("hello world");

// 发起RPC
brpc::Controller cntl;
stub.Echo(&cntl, &request, &response, NULL);

if (cntl.Failed()) {
    LOG(ERROR) << "Fail to Echo, " << cntl.ErrorText();
    return;
}
// 取回复中的字段
response.result_params().res().message();
...
```

   具体example代码可以参考[echo\_c++\_compack\_ubrpc](https://github.com/brpc/brpc/tree/master/example/echo_c++_compack_ubrpc/)，类似的还有[echo\_c++\_mcpack\_ubrpc](https://github.com/brpc/brpc/tree/master/example/echo_c++_mcpack_ubrpc/)。

<a id="client-access-ub--nsheadidl"></a>

# nshead+idl

server端是由public/ub搭建，通讯包组成为nshead+idl::compack/idl::mcpack(v2)

由于不需要指定service和method，无需编写proto文件，直接使用Channel.CallMethod方法发起RPC即可。请求包中的nshead可以填也可以不填，框架会补上正确的magic\_num和body\_len字段：

```c++
#include <brpc/ub_call.h>
...
 
brpc::Channel channel;
brpc::ChannelOptions opt;
opt.protocol = brpc::PROTOCOL_NSHEAD_CLIENT; // or "nshead_client";
 
if (channel.Init(..., &opt) != 0) {
    LOG(ERROR) << "Fail to init channel";
    return -1;
}
...
 
// 构造UB的request/response，完全类似构造原先idl结构，传入一个bsl::mempool（变量pool）
// 将类型作为模板传入，之后在使用上可以直接使用对应idl结构的接口
brpc::UBCompackRequest<example::EchoRequest> request(&pool);
brpc::UBCompackResponse<example::EchoResponse> response(&pool);
 
// Set `message' field of `EchoRequest'
request.set_message("hello world");
// Set fields of the request nshead struct if needed
request.mutable_nshead()->version = 99;
 
brpc::Controller cntl;
channel.CallMethod(NULL, &cntl, &request, &response, NULL);    // 假设channel已经通过之前所述方法Init成功
 
// Get `message' field of `EchoResponse'
response.message();
```

具体example代码可以参考[echo\_c++\_mcpack\_ub](https://github.com/brpc/brpc/blob/master/example/echo_c++_mcpack_ub/)，compack情况类似，不再赘述

<a id="client-access-ub--nsheadmcpack-idl"></a>

# nshead+mcpack(非idl产生的)

server端是由public/ub搭建，通讯包组成为nshead+mcpack包，但不是idl编译器生成的，RPC前需要先构造RawBuffer将其传入，然后获取mc\_pack\_t并按之前手工填写mcpack的方式操作：

```c++
#include <brpc/ub_call.h>
...
 
brpc::Channel channel;
brpc::ChannelOptions opt;
opt.protocol = brpc::PROTOCOL_NSHEAD_CLIENT; // or "nshead_client";
if (channel.Init(..., &opt) != 0) {
    LOG(ERROR) << "Fail to init channel";
    return -1;
}
...
 
// 构造RawBuffer，一次RPC结束后RawBuffer可以复用，类似于bsl::mempool
const int BUFSIZE = 10 * 1024 * 1024;
brpc::RawBuffer req_buf(BUFSIZE);
brpc::RawBuffer res_buf(BUFSIZE);
 
// 传入RawBuffer来构造request和response
brpc::UBRawMcpackRequest request(&req_buf);
brpc::UBRawMcpackResponse response(&res_buf);
         
// Fetch mc_pack_t and fill in variables
mc_pack_t* req_pack = request.McpackHandle();
int ret = mc_pack_put_str(req_pack, "mystr", "hello world");
if (ret != 0) {
    LOG(FATAL) << "Failed to put string into mcpack: "
               << mc_pack_perror((long)req_pack) << (void*)req_pack;
    break;
}  
// Set fields of the request nshead struct if needed
request.mutable_nshead()->version = 99;
 
brpc::Controller cntl;
channel.CallMethod(NULL, &cntl, &request, &response, NULL);    // 假设channel已经通过之前所述方法Init成功
 
// Get response from response buffer
const mc_pack_t* res_pack = response.McpackHandle();
mc_pack_get_str(res_pack, "mystr");
```

具体example代码可以参考[echo\_c++\_raw\_mcpack](https://github.com/brpc/brpc/blob/master/example/echo_c++_raw_mcpack/)。

<a id="client-access-ub--nsheadblob"></a>

# nshead+blob

r32897后brpc直接支持用nshead+blob访问老server（而不用依赖baidu-rpc-ub）。example代码可以参考[nshead\_extension\_c++](https://github.com/brpc/brpc/blob/master/example/nshead_extension_c++/client.cpp)。

```c++
#include <brpc/nshead_message.h>
...
 
brpc::Channel;
brpc::ChannelOptions opt;
opt.protocol = brpc::PROTOCOL_NSHEAD; // or "nshead"
if (channel.Init(..., &opt) != 0) {
    LOG(ERROR) << "Fail to init channel";
    return -1;
} 
...
brpc::NsheadMessage request;
brpc::NsheadMessage response;
       
// Append message to `request'
request.body.append("hello world");
// Set fields of the request nshead struct if needed
request.head.version = 99;
 
 
brpc::Controller cntl;
channel.CallMethod(NULL, &cntl, &request, &response, NULL);
 
if (cntl.Failed()) {
    LOG(ERROR) << "Fail to access the server: " << cntl.ErrorText();
    return -1;
}
// response.head and response.body contains nshead_t and blob respectively.
```

或者用户也可以使用baidu-rpc-ub中的UBRawBufferRequest和UBRawBufferResponse来访问。example代码可以参考[echo\_c++\_raw\_buffer](https://github.com/brpc/brpc/blob/master/example/echo_c++_raw_buffer/)。

```c++
brpc::Channel channel;
brpc::ChannelOptions opt;
opt.protocol = brpc::PROTOCOL_NSHEAD_CLIENT; // or "nshead_client"
if (channel.Init(..., &opt) != 0) {
    LOG(ERROR) << "Fail to init channel";
    return -1;
}
...
 
// 构造RawBuffer，一次RPC结束后RawBuffer可以复用，类似于bsl::mempool
const int BUFSIZE = 10 * 1024 * 1024;
brpc::RawBuffer req_buf(BUFSIZE);
brpc::RawBuffer res_buf(BUFSIZE);
 
// 传入RawBuffer来构造request和response
brpc::UBRawBufferRequest request(&req_buf);
brpc::UBRawBufferResponse response(&res_buf);
         
// Append message to `request'
request.append("hello world");
// Set fields of the request nshead struct if needed
request.mutable_nshead()->version = 99;
 
brpc::Controller cntl;
channel.CallMethod(NULL, &cntl, &request, &response, NULL);    // 假设channel已经通过之前所述方法Init成功
 
// Process response. response.data() is the buffer, response.size() is the length.
```

---

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="client-backup-request"></a>

<!-- source_url: https://brpc.apache.org/docs/client/backup-request/ -->

<!-- page_index: 34 -->

# Backup request

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Backup%20request/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Backup%20request)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Backup request

Learn how to use backup request.

Sometimes in order to ensure availability, we need to visit two services at the same time and get the result coming back first. There are several ways to achieve this in brpc:

<a id="client-backup-request--when-backend-servers-can-be-hung-in-a-naming-service"></a>

# When backend servers can be hung in a naming service

Channel opens backup request. Channel sends the request to one of the servers and when the response is not returned after ChannelOptions.backup\_request\_ms ms, it sends to another server, taking the response that coming back first. After backup\_request\_ms is set up properly, in most of times only one request should be sent, causing no extra pressure to back-end services.

Read [example/backup\_request\_c++](https://github.com/brpc/brpc/blob/master/example/backup_request_c++) as example code. In this example, client sends backup request after 2ms and server sleeps for 20ms on purpose when the number of requests is even to trigger backup request.

After running, the log in client and server is as following. “Index” is the number of request. After the server receives the first request, it will sleep for 20ms on purpose. Then the client sends the request with the same index. The final delay is not affected by the intentional sleep.

![img](assets/images/backup-request-1_d8bc2ab36e7adb55.png)

![img](assets/images/backup-request-2_ce1bf98f7ef5c325.png)

/rpcz also shows that the client triggers backup request after 2ms and sends the second request.

![img](assets/images/backup-request-3_81558512130769e3.png)

<a id="client-backup-request--choose-proper-backup_request_ms"></a>

## Choose proper backup\_request\_ms

You can look the default cdf(Cumulative Distribution Function) graph of latency provided by brpc, or add it by your own. The y-axis of the cdf graph is a latency(us by default), and the x-axis is the proportion of requests whose latencies are less than the corresponding value in y-aixs. In the following graph, Choosing backup\_request\_ms=2ms could approximately cover 95.5% of the requests, while choosing backup\_request\_ms=10ms could cover 99.99% of the requests.

![img](assets/images/backup-request-4_e9eb4d854d0f0f6b.png)

The way of adding it by yourself:

```c++
#include <bvar/bvar.h>
#include <butil/time.h>
...
bvar::LatencyRecorder my_func_latency("my_func");
...
butil::Timer tm;
tm.start();
my_func();
tm.stop();
my_func_latency << tm.u_elapsed();  // u represents for microsecond, and s_elapsed(), m_elapsed(), n_elapsed() correspond to second, millisecond, nanosecond.
 
// All work is done here. My_func_qps, my_func_latency, my_func_latency_cdf and many other counters would be shown in /vars.
```

<a id="client-backup-request--when-backend-servers-cannot-be-hung-in-a-naming-service"></a>

# When backend servers cannot be hung in a naming service

[Recommended] Define a SelectiveChannel that sets backup request, in which contains two sub channel. The visiting process of this SelectiveChannel is similar to the above situation. It will visit one sub channel first. If the response is not returned after channelOptions.backup\_request\_ms ms, then another sub channel is visited. If a sub channel corresponds to a cluster, this method does backups between two clusters. An example of SelectiveChannel can be found in [example/selective\_echo\_c++](https://github.com/brpc/brpc/tree/master/example/selective_echo_c++). More details please refer to the above program.

[Not Recommended] Issue two asynchronous RPC calls and join them. They cancel each other in their done callback. An example is in [example/cancel\_c++](https://github.com/brpc/brpc/tree/master/example/cancel_c++). The problem of this method is that the program always sends two requests, doubling the pressure to back-end services. It is uneconomical in any sense and should be avoided as much as possible.

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="client-basics"></a>

<!-- source_url: https://brpc.apache.org/docs/client/basics/ -->

<!-- page_index: 35 -->

# Basics

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Basics/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Basics)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Naming Service](#client-basics--naming-service)
  - [bns://<bns-name>](#client-basics--bnsbns-name)
  - [file://<path>](#client-basics--filepath)
  - [list://<addr1>,<addr2>…](#client-basics--listaddr1addr2)
  - [http://<url>](#client-basics--httpurl)
  - [https://<url>](#client-basics--httpsurl)
  - [consul://<service-name>](#client-basics--consulservice-name)
  - [More naming services](#client-basics--more-naming-services)
  - [The tag in naming service](#client-basics--the-tag-in-naming-service)
  - [VIP related issues](#client-basics--vip-related-issues)
  - [Naming Service Filter](#client-basics--naming-service-filter)
- [Load Balancer](#client-basics--load-balancer)
  - [rr](#client-basics--rr)
  - [wrr](#client-basics--wrr)
  - [random](#client-basics--random)
  - [wr](#client-basics--wr)
  - [la](#client-basics--la)
  - [c\_murmurhash or c\_md5](#client-basics--c_murmurhash-or-c_md5)
  - [Client-side throttling for recovery from cluster downtime](#client-basics--client-side-throttling-for-recovery-from-cluster-downtime)
- [Health checking](#client-basics--health-checking)

- [Synchronous call](#client-basics--synchronous-call)
- [Asynchronous call](#client-basics--asynchronous-call)
  - [Use NewCallback](#client-basics--use-newcallback)
  - [Inherit google::protobuf::Closure](#client-basics--inherit-googleprotobufclosure)
  - [What will happen when the callback is very complicated?](#client-basics--what-will-happen-when-the-callback-is-very-complicated)
  - [Does the callback run in the same thread that CallMethod runs?](#client-basics--does-the-callback-run-in-the-same-thread-that-callmethod-runs)
- [Wait for completion of RPC](#client-basics--wait-for-completion-of-rpc)
- [Semi-synchronous call](#client-basics--semi-synchronous-call)
- [Cancel RPC](#client-basics--cancel-rpc)
- [Get server-side address and port](#client-basics--get-server-side-address-and-port)
- [Get client-side address and port](#client-basics--get-client-side-address-and-port)
- [Should brpc::Controller be reused?](#client-basics--should-brpccontroller-be-reused)

- [Number of worker pthreads](#client-basics--number-of-worker-pthreads)
- [Timeout](#client-basics--timeout)
- [Retry](#client-basics--retry)
  - [Broken connection](#client-basics--broken-connection)
  - [Timeout is not reached](#client-basics--timeout-is-not-reached)
  - [Has retrying quota](#client-basics--has-retrying-quota)
  - [The retry makes sense](#client-basics--the-retry-makes-sense)
  - [Retrying should be conservative](#client-basics--retrying-should-be-conservative)
- [Circuit breaker](#client-basics--circuit-breaker)
- [Protocols](#client-basics--protocols)
- [Connection Type](#client-basics--connection-type)
- [Close idle connections in pools](#client-basics--close-idle-connections-in-pools)
- [Defer connection close](#client-basics--defer-connection-close)
- [Buffer size of connections](#client-basics--buffer-size-of-connections)
- [log\_id](#client-basics--log_id)
- [Attachment](#client-basics--attachment)
- [Turn on SSL](#client-basics--turn-on-ssl)
- [Authentication](#client-basics--authentication)
- [Reset](#client-basics--reset)
- [Compression](#client-basics--compression)

- - [Q: Does brpc support unix domain socket?](#client-basics--q-does-brpc-support-unix-domain-socket)
  - [Q: Fail to connect to xx.xx.xx.xx:xxxx, Connection refused](#client-basics--q-fail-to-connect-to-xxxxxxxxxxxx-connection-refused)
  - [Q: often met Connection timedout to another IDC](#client-basics--q-often-met-connection-timedout-to-another-idc)
  - [Q: synchronous call is good, asynchronous call crashes](#client-basics--q-synchronous-call-is-good-asynchronous-call-crashes)
  - [Q: How to make requests be processed once and only once](#client-basics--q-how-to-make-requests-be-processed-once-and-only-once)
  - [Q: Invalid address=`bns://group.user-persona.dumi.nj03'](#client-basics--q-invalid-addressbnsgroupuser-personaduminj03)
  - [Q: Both sides use protobuf, why can’t they communicate with each other](#client-basics--q-both-sides-use-protobuf-why-cant-they-communicate-with-each-other)
  - [Q: Why C++ client/server may fail to talk to client/server in other languages](#client-basics--q-why-c-clientserver-may-fail-to-talk-to-clientserver-in-other-languages)

# Basics

Learn how to use bRPC client.

<a id="client-basics--example"></a>

# Example

[client-side code](https://github.com/brpc/brpc/blob/master/example/echo_c++/client.cpp) of echo.

<a id="client-basics--quick-facts"></a>

# Quick facts

- Channel.Init() is not thread-safe.
- Channel.CallMethod() is thread-safe and a Channel can be used by multiple threads simultaneously.
- Channel can be put on stack.
- Channel can be destructed just after sending asynchronous request.
- No class named brpc::Client.

<a id="client-basics--channel"></a>

# Channel

Client-side of RPC sends requests. It’s called [Channel](https://github.com/brpc/brpc/blob/master/src/brpc/channel.h) rather than “Client” in brpc. A channel represents a communication line to one server or multiple servers, which can be used for calling services.

A Channel can be **shared by all threads** in the process. You don’t need to create separate Channels for each thread, and you don’t need to synchronize Channel.CallMethod with lock. However creation and destroying of Channel is **not** thread-safe, make sure the channel is initialized and destroyed only by one thread.

Some RPC implementations have so-called “ClientManager”, including configurations and resource management at the client-side, which is not needed by brpc. “thread-num”, “connection-type” such parameters are either in brpc::ChannelOptions or global gflags. Advantages of doing so:

1. Convenience. You don’t have to pass a “ClientManager” when the Channel is created, and you don’t have to store the “ClientManager”. Otherwise code has to pass “ClientManager” layer by layer, which is troublesome. gflags makes configurations of global behaviors easier.
2. Share resources. For example, servers and channels in brpc share background workers (of bthread).
3. Better management of Lifetime. Destructing a “ClientManager” is very error-prone, which is managed by brpc right now.

Like most classes, Channel must be **Init()**-ed before usage. Parameters take default values when `options` is NULL. If you want non-default values, code as follows:

```c++
brpc::ChannelOptions options;  // including default values
options.xxx = yyy;
...
channel.Init(..., &options);
```

Note that Channel neither modifies `options` nor accesses `options` after completion of Init(), thus options can be put on stack safely as in above code. Channel.options() gets options being used by the Channel.

Init() can connect one server or a cluster(multiple servers).

<a id="client-basics--connect-to-a-server"></a>

# Connect to a server

```c++
// Take default values when options is NULL.
int Init(EndPoint server_addr_and_port, const ChannelOptions* options);
int Init(const char* server_addr_and_port, const ChannelOptions* options);
int Init(const char* server_addr, int port, const ChannelOptions* options);
```

The server connected by these Init() has fixed address genrally. The creation does not need NamingService or LoadBalancer, being relatively light-weight. The address could be a hostname, but don’t frequently create Channels connecting to a hostname, which requires a DNS lookup taking at most 10 seconds. (default timeout of DNS lookup). Reuse them.

Valid “server\_addr\_and\_port”:

- 127.0.0.1:80
- [www.foo.com](https://www.foo.com):8765
- localhost:9000

Invalid “server\_addr\_and\_port”:

- 127.0.0.1:90000 # too large port
- 10.39.2.300:8000 # invalid IP

<a id="client-basics--connect-to-a-cluster"></a>

# Connect to a cluster

```c++
int Init(const char* naming_service_url,
         const char* load_balancer_name,
         const ChannelOptions* options);
```

Channels created by above Init() get server list from the NamingService specified by `naming_service_url` periodically or driven-by-events, and send request to one server chosen from the list according to the algorithm specified by `load_balancer_name` .

You **should not** create such channels ad-hocly each time before a RPC, because creation and destroying of such channels relate to many resources, say NamingService needs to be accessed once at creation otherwise server candidates are unknown. On the other hand, channels are able to be shared by multiple threads safely and has no need to be created frequently.

If `load_balancer_name` is NULL or empty, this Init() is just the one for connecting single server and `naming_service_url` should be “ip:port” or “host:port” of the server. Thus you can unify initialization of all channels with this Init(). For example, you can put values of `naming_service_url` and `load_balancer_name` in configuration file, and set `load_balancer_name` to empty for single server and a valid algorithm for a cluster.

<a id="client-basics--naming-service"></a>

## Naming Service

Naming service maps a name to a modifiable list of servers. It’s positioned as follows at client-side:

![img](assets/images/ns_cfe5068d0e13720c.png)

With the help of naming service, the client remembers a name instead of every concrete server. When the servers are added or removed, only mapping in the naming service is changed, rather than telling every client that may access the cluster. This process is called “decoupling up and downstreams”. Back to implementation details, the client does remember every server and will access NamingService periodically or be pushed with latest server list. The impl. has minimal impact on RPC latencies and very small pressure on the system providing naming service.

General form of `naming_service_url` is “**protocol://service\_name**”.

<a id="client-basics--bnsbns-name"></a>

### bns://<bns-name>

BNS is the most common naming service inside Baidu. In “bns://rdev.matrix.all”, “bns” is protocol and “rdev.matrix.all” is service-name. A related gflag is -ns\_access\_interval: ![img](assets/images/ns-access-interval_c19fcb88b88a2ee1.png)

If the list in BNS is non-empty, but Channel says “no servers”, the status bit of the machine in BNS is probably non-zero, which means the machine is unavailable and as a correspondence not added as server candidates of the Channel. Status bits can be checked by:

`get_instance_by_service [bns_node_name] -s`

<a id="client-basics--filepath"></a>

### file://<path>

Servers are put in the file specified by `path`. For example, in “file://conf/machine\_list”, “conf/machine\_list” is the file:

- in which each line is address of a server.
- contents after # are comments and ignored.
- non-comment contents after addresses are tags, which are separated from addresses by one or more spaces, same address + different tags are treated as different instances.
- brpc reloads the file when it’s updated.

```
# This line is ignored 10.24.234.17:8080 tag1 # a comment 10.24.234.17:8090 tag2 # an instance different from the instance on last line 10.24.234.18:8080 10.24.234.19:8080
```

Pros: easy to modify, convenient for unittests.

Cons: need to update every client when the list changes, not suitable for online deployment.

<a id="client-basics--listaddr1addr2"></a>

### list://<addr1>,<addr2>…

Servers are directly written after list://, separated by comma. For example: “list://db-bce-81-3-186.db01:7000,m1-bce-44-67-72.m1:7000,cp01-rd-cos-006.cp01:7000” has 3 addresses.

Tags can be appended to addresses, separated with one or more spaces. Same address + different tags are treated as different instances.

Pros: directly configurable in CLI, convenient for unittests.

Cons: cannot be updated at runtime, not suitable for online deployment at all.

<a id="client-basics--httpurl"></a>

### http://<url>

Connect all servers under the domain, for example: <http://www.baidu.com:80>.

Note: although Init() for connecting single server(2 parameters) accepts hostname as well, it only connects one server under the domain.

Pros: Versatility of DNS, useable both in private or public network.

Cons: limited by transmission formats of DNS, unable to implement notification mechanisms.

<a id="client-basics--httpsurl"></a>

### https://<url>

Similar with “http” prefix besides that the connections will be encrypted with SSL.

<a id="client-basics--consulservice-name"></a>

### consul://<service-name>

Get a list of servers with the specified service-name through consul. The default address of consul is localhost:8500, which can be modified by setting -consul\_agent\_addr in gflags. The connection timeout of consul is 200ms by default, which can be modified by -consul\_connect\_timeout\_ms.

By default, [stale](https://www.consul.io/api/index.html#consistency-modes) and passing(only servers with passing in statuses are returned) are added to [parameters of the consul request](https://brpc.apache.org/docs/client/basics/(https:/www.consul.io/api/health.html#parameters-2)), which can be modified by -consul\_url\_parameter in gflags.

Except the first request to consul, the follow-up requests use the [long polling](https://www.consul.io/api/index.html#blocking-queries) feature. That is, the consul responds only when the server list is updated or the request times out. The timeout defaults to 60 seconds, which can be modified by -consul\_blocking\_query\_wait\_secs.

If the server list returned by the consul does not follow [response format](https://www.consul.io/api/health.html#sample-response-2), or all servers in the list are filtered because the key fields such as the address and port are missing or cannot be parsed, the server list will not be updated and the consul service will be revisited after a period of time(default 500ms, can be modified by -consul\_retry\_interval\_ms）.

If consul is not accessible, the naming service can be automatically downgraded to file naming service. This feature is turned off by default and can be turned on by setting -consul\_enable\_degrade\_to\_file\_naming\_service. After downgrading, in the directory specified by -consul\_file\_naming\_service\_dir, the file whose name is the service-name will be used. This file can be generated by the consul-template, which holds the latest server list before the consul is unavailable. The consul naming service is automatically restored when consul is restored.

<a id="client-basics--more-naming-services"></a>

### More naming services

User can extend to more naming services by implementing brpc::NamingService, check [this link](#rpc-in-depth-load-balancing--section) for details.

<a id="client-basics--the-tag-in-naming-service"></a>

### The tag in naming service

Every address can be attached with a tag. The common implementation is that if there’re spaces after the address, the content after the spaces is the tag.
Same address with different tag are treated as different instances which are interacted with separate connections. Users can use this feature to establish connections with remote servers in a more flexible way.
If you need weighted round-robin, you should consider using [wrr algorithm](#client-basics--wrr) first rather than emulate “a coarse-grained version” with tags.

<a id="client-basics--vip-related-issues"></a>

### VIP related issues

VIP is often the public IP of layer-4 load balancer, which proxies traffic to RS behide. When a client connects to the VIP, a connection is established to a chosen RS. When the client connection is broken, the connection to the RS is reset as well.

If one client establishes only one connection to the VIP(“single” connection type in brpc), all traffic from the client lands on one RS. If number of clients are large enough, each RS should gets many connections and roughly balanced, at least from the cluster perspective. However, if clients are not large enough or workload from clients are very different, some RS may be overloaded. Another issue is that when multiple VIP are listed together, the traffic to them may not be proportional to the number of RS behide them.

One solution to these issues is to use “pooled” connection type, so that one client may create multiple connections to one VIP (roughly the max concurrency recently) to make traffic land on different RS. If more than one VIP are present, consider using [wrr load balancing](#client-basics--wrr) to assign weights to different VIP, or add different tags to VIP to form more instances.

If higher performance is demanded, or number of connections is limited (in a large cluster), consider using single connection and attach same VIP with different tags to create different connections. Comparing to pooled connections, number of connections and overhead of syscalls are often lower, but if tags are not enough, RS hotspots may still present.

<a id="client-basics--naming-service-filter"></a>

### Naming Service Filter

Users can filter servers got from the NamingService before pushing to LoadBalancer.

![img](assets/images/ns-filter_8911cc37c7f5137b.jpg)

Interface of the filter:

```c++
// naming_service_filter.h
class NamingServiceFilter {
public:
    // Return true to take this `server' as a candidate to issue RPC
    // Return false to filter it out
    virtual bool Accept(const ServerNode& server) const = 0;
};

// naming_service.h
struct ServerNode {
    butil::EndPoint addr;
    std::string tag;
};
```

The most common usage is filtering by server tags.

Customized filter is set to ChannelOptions to take effects. NULL by default means not filter.

```c++
class MyNamingServiceFilter : public brpc::NamingServiceFilter {
public:
    bool Accept(const brpc::ServerNode& server) const {
        return server.tag == "main";
    }
};

int main() {
    ...
    MyNamingServiceFilter my_filter;
    ...
    brpc::ChannelOptions options;
    options.ns_filter = &my_filter;
    ...
}
```

<a id="client-basics--load-balancer"></a>

## Load Balancer

When there’re more than one server to access, we need to divide the traffic. The process is called load balancing, which is positioned as follows at client-side.

![img](assets/images/lb_d20720c8a73843bb.png)

The ideal algorithm is to make every request being processed in-time, and crash of any server makes minimal impact. However clients are not able to know delays or congestions happened at servers in realtime, and load balancing algorithms should be light-weight generally, users need to choose proper algorithms for their use cases. Algorithms provided by brpc (specified by `load_balancer_name`):

<a id="client-basics--rr"></a>

### rr

which is round robin. Always choose next server inside the list, next of the last server is the first one. No other settings. For example there’re 3 servers: a,b,c, brpc will send requests to a, b, c, a, b, c, … and so on. Note that presumption of using this algorithm is the machine specs, network latencies, server loads are similar.

<a id="client-basics--wrr"></a>

### wrr

which is weighted round robin. Choose the next server according to the configured weight. The chances a server is selected is consistent with its weight, and the algorithm can make each server selection scattered.

The instance tag must be an int32 number representing the weight, eg. tag=“50”.

<a id="client-basics--random"></a>

### random

Randomly choose one server from the list, no other settings. Similarly with round robin, the algorithm assumes that servers to access are similar.

<a id="client-basics--wr"></a>

### wr

which is weighted random. Choose the next server according to the configured weight. The chances a server is selected is consistent with its weight.

Requirements of instance tag is the same as wrr.

<a id="client-basics--la"></a>

### la

which is locality-aware. Perfer servers with lower latencies, until the latency is higher than others, no other settings. Check out [Locality-aware load balancing](#rpc-in-depth-locality-aware) for more details.

<a id="client-basics--c_murmurhash-or-c_md5"></a>

### c\_murmurhash or c\_md5

which is consistent hashing. Adding or removing servers does not make destinations of requests change as dramatically as in simple hashing. It’s especially suitable for caching services.

Need to set Controller.set\_request\_code() before RPC otherwise the RPC will fail. request\_code is often a 32-bit hash code of “key part” of the request, and the hashing algorithm does not need to be same with the one used by load balancer. Say `c_murmurhash` can use md5 to compute request\_code of the request as well.

[src/brpc/policy/hasher.h](https://github.com/brpc/brpc/blob/master/src/brpc/policy/hasher.h) includes common hash functions. If `std::string key` stands for key part of the request, controller.set\_request\_code(brpc::policy::MurmurHash32(key.data(), key.size())) sets request\_code correctly.

Do distinguish “key” and “attributes” of the request. Don’t compute request\_code by full content of the request just for quick. Minor change in attributes may result in totally different hash code and change destination dramatically. Another cause is padding, for example: `struct Foo { int32_t a; int64_t b; }` has a 4-byte undefined gap between `a` and `b` on 64-bit machines, result of `hash(&foo, sizeof(foo))` is undefined. Fields need to be packed or serialized before hashing.

Check out [Consistent Hashing](#rpc-in-depth-consistent-hashing) for more details.

Other kind of lb does not need to set Controller.set\_request\_code(). If request code is set, it will not be used by lb. For example, lb=rr, and call Controller.set\_request\_code(), even if request\_code is the same for every request, lb will balance the requests using the rr policy.

<a id="client-basics--client-side-throttling-for-recovery-from-cluster-downtime"></a>

### Client-side throttling for recovery from cluster downtime

Cluster downtime refers to the state in which all servers in the cluster are unavailable. Due to the health check mechanism, when the cluster returns to normal, server will go online one by one. When a server is online, all traffic will be sent to it, which may cause the service to be overloaded again. If circuit breaker is enabled, server may be offline again before the other servers go online, and the cluster can never be recovered. As a solution, brpc provides a client-side throttling mechanism for recovery after cluster downtime. When no server is available in the cluster, the cluster enters recovery state. Assuming that the minimum number of servers that can serve all requests is min\_working\_instances, current number of servers available in the cluster is q, then in recovery state, the probability of client accepting the request is q/min\_working\_instances, otherwise it is discarded. If q remains unchanged for a period of time(hold\_seconds), the traffic is resent to all available servers and leaves recovery state. Whether the request is rejected in recovery state is indicated by whether controller.ErrorCode() is equal to brpc::ERJECT, and the rejected request will not be retried by the framework.

This recovery mechanism requires the capabilities of downstream servers to be similar, so it is currently only valid for rr and random. The way to enable it is to add the values of min\_working\_instances and hold\_seconds parameters after *load\_balancer\_name*, for example:

```c++
channel.Init("http://...", "random:min_working_instances=6 hold_seconds=10", &options);
```

<a id="client-basics--health-checking"></a>

## Health checking

Servers whose connections are lost are isolated temporarily to prevent them from being selected by LoadBalancer. brpc connects isolated servers periodically to test if they’re healthy again. The interval is controlled by gflag -health\_check\_interval:

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| health\_check\_interval (R) | 3 | seconds between consecutive health-checkings | src/brpc/socket\_map.cpp |

Once a server is connected, it resumes as a server candidate inside LoadBalancer. If a server is removed from NamingService during health-checking, brpc removes it from health-checking as well.

<a id="client-basics--launch-rpc"></a>

# Launch RPC

Generally, we don’t use Channel.CallMethod directly, instead we call XXX\_Stub generated by protobuf, which feels more like a “method call”. The stub has few member fields, being suitable(and recommended) to be put on stack instead of new(). Surely the stub can be saved and re-used as well. Channel.CallMethod and stub are both **thread-safe** and accessible by multiple threads simultaneously. For example:

```c++
XXX_Stub stub(&channel);
stub.some_method(controller, request, response, done);
```

Or even:

```c++
XXX_Stub(&channel).some_method(controller, request, response, done);
```

A exception is http/h2 client, which is not related to protobuf much. Call CallMethod directly to make a http call, setting all parameters to NULL except for `Controller` and `done`, check [Access http/h2](#client-access-httph2) for details.

<a id="client-basics--synchronous-call"></a>

## Synchronous call

CallMethod blocks until response from server is received or error occurred (including timedout).

response/controller in synchronous call will not be used by brpc again after CallMethod, they can be put on stack safely. Note: if request/response has many fields and being large on size, they’d better be allocated on heap.

```c++
MyRequest request;
MyResponse response;
brpc::Controller cntl;
XXX_Stub stub(&channel);

request.set_foo(...);
cntl.set_timeout_ms(...);
stub.some_method(&cntl, &request, &response, NULL);
if (cntl.Failed()) {
    // RPC failed. fields in response are undefined, don't use.
} else {
    // RPC succeeded, response has what we want.
}
```

> WARNING: Do NOT use synchronous call when you are holding a pthread lock! Otherwise it is easy to cause deadlock.
>
> Solution (choose one of the two):
>
> 1. Replace pthread lock with bthread lock (bthread\_mutex\_t)
> 2. Release the lock before CallMethod

<a id="client-basics--asynchronous-call"></a>

## Asynchronous call

Pass a callback `done` to CallMethod, which resumes after sending request, rather than completion of RPC. When the response from server is received or error occurred(including timedout), done->Run() is called. Post-processing code of the RPC should be put in done->Run() instead of after CallMethod.

Because end of CallMethod does not mean completion of RPC, response/controller may still be used by brpc or done->Run(). Generally they should be allocated on heap and deleted in done->Run(). If they’re deleted too early, done->Run() may access invalid memory.

You can new these objects individually and create done by [NewCallback](#client-basics--use-newcallback), or make response/controller be member of done and [new them together](#client-basics--inherit-googleprotobufclosure). Former one is recommended.

Request can be destroyed immediately after asynchronous CallMethod. (SelectiveChannel is an exception, in the case of SelectiveChannel, the request object must be released after rpc finish)

Channel can be destroyed immediately after asynchronous CallMethod.

Note that “immediately” means destruction of Request/Channel can happen **after** CallMethod, not during CallMethod. Deleting a Channel just being used by another thread results in undefined behavior (crash at best).

<a id="client-basics--use-newcallback"></a>

### Use NewCallback

```c++
static void OnRPCDone(MyResponse* response, brpc::Controller* cntl) {
    // unique_ptr helps us to delete response/cntl automatically. unique_ptr in gcc 3.4 is an emulated version.
    std::unique_ptr<MyResponse> response_guard(response);
    std::unique_ptr<brpc::Controller> cntl_guard(cntl);
    if (cntl->Failed()) {
        // RPC failed. fields in response are undefined, don't use.
    } else {
        // RPC succeeded, response has what we want. Continue the post-processing.
    }
    // Closure created by NewCallback deletes itself at the end of Run.
}

MyResponse* response = new MyResponse;
brpc::Controller* cntl = new brpc::Controller;
MyService_Stub stub(&channel);

MyRequest request;  // you don't have to new request, even in an asynchronous call.
request.set_foo(...);
cntl->set_timeout_ms(...);
stub.some_method(cntl, &request, response, brpc::NewCallback(OnRPCDone, response, cntl));
```

Since protobuf 3 changes NewCallback to private, brpc puts NewCallback in [src/brpc/callback.h](https://github.com/brpc/brpc/blob/master/src/brpc/callback.h) after r32035 (and adds more overloads). If your program has compilation issues with NewCallback, replace google::protobuf::NewCallback with brpc::NewCallback.

<a id="client-basics--inherit-googleprotobufclosure"></a>

### Inherit google::protobuf::Closure

Drawback of using NewCallback is that you have to allocate memory on heap at least 3 times: response, controller, done. If profiler shows that the memory allocation is a hotspot, you can consider inheriting Closure by your own, and enclose response/controller as member fields. Doing so combines 3 new into one, but the code will be worse to read. Don’t do this if memory allocation is not an issue.

```c++
class OnRPCDone: public google::protobuf::Closure {
public:
    void Run() {
        // unique_ptr helps us to delete response/cntl automatically. unique_ptr in gcc 3.4 is an emulated version.
        std::unique_ptr<OnRPCDone> self_guard(this);

        if (cntl->Failed()) {
            // RPC failed. fields in response are undefined, don't use.
        } else {
            // RPC succeeded, response has what we want. Continue the post-processing.
        }
    }

    MyResponse response;
    brpc::Controller cntl;
}

OnRPCDone* done = new OnRPCDone;
MyService_Stub stub(&channel);

MyRequest request;  // you don't have to new request, even in an asynchronous call.
request.set_foo(...);
done->cntl.set_timeout_ms(...);
stub.some_method(&done->cntl, &request, &done->response, done);
```

<a id="client-basics--what-will-happen-when-the-callback-is-very-complicated"></a>

### What will happen when the callback is very complicated?

No special impact, the callback will run in separate bthread, without blocking other sessions. You can do all sorts of things in the callback.

<a id="client-basics--does-the-callback-run-in-the-same-thread-that-callmethod-runs"></a>

### Does the callback run in the same thread that CallMethod runs?

The callback runs in a different bthread, even the RPC fails just after entering CallMethod. This avoids deadlock when the RPC is ongoing inside a lock(not recommended).

<a id="client-basics--wait-for-completion-of-rpc"></a>

## Wait for completion of RPC

NOTE: [ParallelChannel](#client-combo-channels--parallelchannel) is probably more convenient to launch multiple RPCs in parallel.

Following code starts 2 asynchronous RPC and waits them to complete.

```c++
const brpc::CallId cid1 = controller1->call_id();
const brpc::CallId cid2 = controller2->call_id();
...
stub.method1(controller1, request1, response1, done1);
stub.method2(controller2, request2, response2, done2);
...
brpc::Join(cid1);
brpc::Join(cid2);
```

Call `Controller.call_id()` to get an id **before launching RPC**, join the id after the RPC.

Join() blocks until completion of RPC **and end of done->Run()**, properties of Join:

- If the RPC is complete, Join() returns immediately.
- Multiple threads can Join() one id, all of them will be woken up.
- Synchronous RPC can be Join()-ed in another thread, although we rarely do this.

Join() was called JoinResponse() before, if you meet deprecated issues during compilation, rename to Join().

Calling `Join(controller->call_id())` after completion of RPC is **wrong**, do save call\_id before RPC, otherwise the controller may be deleted by done at any time. The Join in following code is **wrong**.

```c++
static void on_rpc_done(Controller* controller, MyResponse* response) {
    ... Handle response ...
    delete controller;
    delete response;
}

Controller* controller1 = new Controller;
Controller* controller2 = new Controller;
MyResponse* response1 = new MyResponse;
MyResponse* response2 = new MyResponse;
...
stub.method1(controller1, &request1, response1, google::protobuf::NewCallback(on_rpc_done, controller1, response1));
stub.method2(controller2, &request2, response2, google::protobuf::NewCallback(on_rpc_done, controller2, response2));
...
brpc::Join(controller1->call_id());   // WRONG, controller1 may be deleted by on_rpc_done
brpc::Join(controller2->call_id());   // WRONG, controller2 may be deleted by on_rpc_done
```

<a id="client-basics--semi-synchronous-call"></a>

## Semi-synchronous call

Join can be used for implementing “Semi-synchronous” call: blocks until multiple asynchronous calls to complete. Since the callsite blocks until completion of all RPC, controller/response can be put on stack safely.

```c++
brpc::Controller cntl1;
brpc::Controller cntl2;
MyResponse response1;
MyResponse response2;
...
stub1.method1(&cntl1, &request1, &response1, brpc::DoNothing());
stub2.method2(&cntl2, &request2, &response2, brpc::DoNothing());
...
brpc::Join(cntl1.call_id());
brpc::Join(cntl2.call_id());
```

brpc::DoNothing() gets a closure doing nothing, specifically for semi-synchronous calls. Its lifetime is managed by brpc.

Note that in above example, we access `controller.call_id()` after completion of RPC, which is safe right here, because DoNothing does not delete controller as in `on_rpc_done` in previous example.

<a id="client-basics--cancel-rpc"></a>

## Cancel RPC

`brpc::StartCancel(call_id)` cancels corresponding RPC, call\_id must be got from Controller.call\_id() **before launching RPC**, race conditions may occur at any other time.

NOTE: it is `brpc::StartCancel(call_id)`, not `controller->StartCancel()`, which is forbidden and useless. The latter one is provided by protobuf by default and has serious race conditions on lifetime of controller.

As the name implies, RPC may not complete yet after calling StartCancel, you should not touch any field in Controller or delete any associated resources, they should be handled inside done->Run(). If you have to wait for completion of RPC in-place(not recommended), call Join(call\_id).

Facts about StartCancel:

- call\_id can be cancelled before CallMethod, the RPC will end immediately(and done will be called).
- call\_id can be cancelled in another thread.
- Cancel an already-cancelled call\_id has no effect. Inference: One call\_id can be cancelled by multiple threads simultaneously, but only one of them takes effect.
- Cancel here is a client-only feature, **the server-side may not cancel the operation necessarily**, server cancelation is a separate feature.

<a id="client-basics--get-server-side-address-and-port"></a>

## Get server-side address and port

remote\_side() tells where request was sent to, the return type is [butil::EndPoint](https://github.com/brpc/brpc/blob/master/src/butil/endpoint.h), which includes an ipv4 address and port. Calling this method before completion of RPC is undefined.

How to print:

```c++
LOG(INFO) << "remote_side=" << cntl->remote_side();
printf("remote_side=%s\n", butil::endpoint2str(cntl->remote_side()).c_str());
```

<a id="client-basics--get-client-side-address-and-port"></a>

## Get client-side address and port

local\_side() gets address and port of the client-side sending RPC after r31384

How to print:

```c++
LOG(INFO) << "local_side=" << cntl->local_side();
printf("local_side=%s\n", butil::endpoint2str(cntl->local_side()).c_str());
```

<a id="client-basics--should-brpccontroller-be-reused"></a>

## Should brpc::Controller be reused?

Not necessary to reuse deliberately.

Controller has miscellaneous fields, some of them are buffers that can be re-used by calling Reset().

In most use cases, constructing a Controller(snippet1) and re-using a Controller(snippet2) perform similarily.

```c++
// snippet1
for (int i = 0; i < n; ++i) {
    brpc::Controller controller;
    ...
    stub.CallSomething(..., &controller);
}

// snippet2
brpc::Controller controller;
for (int i = 0; i < n; ++i) {
    controller.Reset();
    ...
    stub.CallSomething(..., &controller);
}
```

If the Controller in snippet1 is new-ed on heap, snippet1 has extra cost of “heap allcation” and may be a little slower in some cases.

<a id="client-basics--settings"></a>

# Settings

Client-side settings has 3 parts:

- brpc::ChannelOptions: defined in [src/brpc/channel.h](https://github.com/brpc/brpc/blob/master/src/brpc/channel.h), for initializing Channel, becoming immutable once the initialization is done.
- brpc::Controller: defined in [src/brpc/controller.h](https://github.com/brpc/brpc/blob/master/src/brpc/controller.h), for overriding fields in brpc::ChannelOptions for some RPC according to contexts.
- global gflags: for tuning global behaviors, being unchanged generally. Read comments in [/flags](#builtin-services-flags) before setting.

Controller contains data and options that request may not have. server and client share the same Controller class, but they may set different fields. Read comments in Controller carefully before using.

A Controller corresponds to a RPC. A Controller can be re-used by another RPC after Reset(), but a Controller can’t be used by multiple RPC simultaneously, no matter the RPCs are started from one thread or not.

Properties of Controller:

1. A Controller can only have one user. Without explicit statement, methods in Controller are **not** thread-safe by default.
2. Due to the fact that Controller is not shared generally, there’s no need to manage Controller by shared\_ptr. If you do, something might goes wrong.
3. Controller is constructed before RPC and destructed after RPC, some common patterns:

- Put Controller on stack before synchronous RPC, be destructed when out of scope. Note that Controller of asynchronous RPC **must not** be put on stack, otherwise the RPC may still run when the Controller is being destructed and result in undefined behavior.
- new Controller before asynchronous RPC, delete in done.

<a id="client-basics--number-of-worker-pthreads"></a>

## Number of worker pthreads

There’s **no** independent thread pool for client in brpc. All Channels and Servers share the same backing threads via [bthread](#bthread-bthread). Setting number of worker pthreads in Server works for Client as well if Server is in used. Or just specify the [gflag](#builtin-services-flags) [-bthread\_concurrency](brpc.baidu.com:8765/flags/bthread_concurrency) to set the global number of worker pthreads.

<a id="client-basics--timeout"></a>

## Timeout

**ChannelOptions.timeout\_ms** is timeout in milliseconds for all RPCs via the Channel, Controller.set\_timeout\_ms() overrides value for one RPC. Default value is 1 second, Maximum value is 2^31 (about 24 days), -1 means wait indefinitely for response or connection error.

**ChannelOptions.connect\_timeout\_ms** is the timeout in milliseconds for establishing connections of RPCs over the Channel, and -1 means no deadline. This value is limited to be not greater than timeout\_ms. Note that this connection timeout is different from the one in TCP, generally this one is smaller.

NOTE1: timeout\_ms in brpc is **deadline**, which means once it’s reached, the RPC ends without more retries. As a comparison, other implementations may have session timeouts and deadline timeouts. Do distinguish them before porting to brpc.

NOTE2: error code of RPC timeout is \*\*ERPCTIMEDOUT (1008) \*\*, ETIMEDOUT is connection timeout and retriable.

<a id="client-basics--retry"></a>

## Retry

ChannelOptions.max\_retry is maximum retrying count for all RPC via the channel, Default value is 3, 0 means no retries. Controller.set\_max\_retry() overrides value for one RPC.

Controller.retried\_count() returns number of retries.

Controller.has\_backup\_request() tells if backup\_request was sent.

**Servers tried before are not retried by best efforts**

Conditions for retrying (AND relations):

- Broken connection.
- Timeout is not reached.
- Has retrying quota. Controller.set\_max\_retry(0) or ChannelOptions.max\_retry = 0 disables retries.
- The retry makes sense. If the RPC fails due to request(EREQUEST), no retry will be done because server is very likely to reject the request again, retrying makes no sense here.

<a id="client-basics--broken-connection"></a>

### Broken connection

If the server does not respond and connection is good, retry is not triggered. If you need to send another request after some timeout, use backup request.

How it works: If response does not return within the timeout specified by backup\_request\_ms, send another request, take whatever the first returned. New request will be sent to a different server that never tried before by best efforts. NOTE: If backup\_request\_ms is greater than timeout\_ms, backup request will never be sent. backup request consumes one retry. backup request does not imply a server-side cancellation.

ChannelOptions.backup\_request\_ms affects all RPC via the Channel, unit is milliseconds, Default value is -1(disabled), Controller.set\_backup\_request\_ms() overrides value for one RPC.

<a id="client-basics--timeout-is-not-reached"></a>

### Timeout is not reached

RPC will be ended soon after the timeout.

<a id="client-basics--has-retrying-quota"></a>

### Has retrying quota

Controller.set\_max\_retry(0) or ChannelOptions.max\_retry = 0 disables retries.

<a id="client-basics--the-retry-makes-sense"></a>

### The retry makes sense

If the RPC fails due to request(EREQUEST), no retry will be done because server is very likely to reject the request again, retrying makes no sense here.

Users can inherit [brpc::RetryPolicy](https://github.com/brpc/brpc/blob/master/src/brpc/retry_policy.h) to customize conditions of retrying. For example brpc does not retry for http/h2 related errors by default. If you want to retry for HTTP\_STATUS\_FORBIDDEN(403) in your app, you can do as follows:

```c++
#include <brpc/retry_policy.h>

class MyRetryPolicy : public brpc::RetryPolicy {
public:
    bool DoRetry(const brpc::Controller* cntl) const {
        if (cntl->ErrorCode() == brpc::EHTTP && // http/h2 error
            cntl->http_response().status_code() == brpc::HTTP_STATUS_FORBIDDEN) {
            return true;
        }
        // Leave other cases to brpc.
        return brpc::DefaultRetryPolicy()->DoRetry(cntl);
    }
};
...

// Assign the instance to ChannelOptions.retry_policy.
// NOTE: retry_policy must be kept valid during lifetime of Channel, and Channel does not retry_policy, so in most cases RetryPolicy should be created by singleton..
brpc::ChannelOptions options;
static MyRetryPolicy g_my_retry_policy;
options.retry_policy = &g_my_retry_policy;
...
```

Some tips：

- Get response of the RPC by cntl->response().
- RPC deadline represented by ERPCTIMEDOUT is never retried, even it’s allowed by your derived RetryPolicy.

<a id="client-basics--retrying-should-be-conservative"></a>

### Retrying should be conservative

Due to maintaining costs, even very large scale clusters are deployed with “just enough” instances to survive major defects, namely offline of one IDC, which is at most 1/2 of all machines. However aggressive retries may easily make pressures from all clients double or even tripple against servers, and make the whole cluster down: More and more requests stuck in buffers, because servers can’t process them in-time. All requests have to wait for a very long time to be processed and finally gets timed out, as if the whole cluster is crashed. The default retrying policy is safe generally: unless the connection is broken, retries are rarely sent. However users are able to customize starting conditions for retries by inheriting RetryPolicy, which may turn retries to be “a storm”. When you customized RetryPolicy, you need to carefully consider how clients and servers interact and design corresponding tests to verify that retries work as expected.

<a id="client-basics--circuit-breaker"></a>

## Circuit breaker

Check out [circuit\_breaker](https://github.com/apache/brpc/blob/master/docs/cn/circuit_breaker.md) for more details.

<a id="client-basics--protocols"></a>

## Protocols

The default protocol used by Channel is baidu\_std, which is changeable by setting ChannelOptions.protocol. The field accepts both enum and string.

Supported protocols:

<a id="client-basics--connection-type"></a>

## Connection Type

brpc supports following connection types:

- short connection: Established before each RPC, closed after completion. Since each RPC has to pay the overhead of establishing connection, this type is used for occasionally launched RPC, not frequently launched ones. No protocol use this type by default. Connections in http/1.0 are handled similarly as short connections.
- pooled connection: Pick an unused connection from a pool before each RPC, return after completion. One connection carries at most one request at the same time. One client may have multiple connections to one server. http/1.1 and the protocols using nshead use this type by default.
- single connection: all clients in one process has at most one connection to one server, one connection may carry multiple requests at the same time. The sequence of received responses does not need to be same as sending requests. This type is used by baidu\_std, hulu\_pbrpc, sofa\_pbrpc by default.

|  | short connection | pooled connection | single connection |
| --- | --- | --- | --- |
| long connection | no | yes | yes |
| #connection at server-side (from a client) | qps\*latency ([little’s law](https://en.wikipedia.org/wiki/Little%27s_law)) | qps\*latency | 1 |
| peak qps | bad, and limited by max number of ports | medium | high |
| latency | 1.5RTT(connect) + 1RTT + processing time | 1RTT + processing time | 1RTT + processing time |
| cpu usage | high, tcp connect for each RPC | medium, every request needs a sys write | low, writes can be combined to reduce overhead. |

brpc chooses best connection type for the protocol by default, users generally have no need to change it. If you do, set ChannelOptions.connection\_type to:

- CONNECTION\_TYPE\_SINGLE or “single” : single connection
- CONNECTION\_TYPE\_POOLED or “pooled”: pooled connection. Max number of pooled connections from one client to one server is limited by -max\_connection\_pool\_size. Note the number is not same as “max number of connections”. New connections are always created when there’s no idle ones in the pool; the returned connections are closed immediately when the pool already has max\_connection\_pool\_size connections. Value of max\_connection\_pool\_size should respect the concurrency, otherwise the connnections that can’t be pooled are created and closed frequently which behaves similarly as short connections. If max\_connection\_pool\_size is 0, the pool behaves just like fully short connections.


| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| max\_connection\_pool\_size (R) | 100 | Max number of pooled connections to a single endpoint | src/brpc/socket.cpp |

- CONNECTION\_TYPE\_SHORT or “short” : short connection
- "" (empty string) makes brpc chooses the default one.

brpc also supports [Streaming RPC](#client-streaming-rpc) which is an application-level connection for transferring streaming data.

<a id="client-basics--close-idle-connections-in-pools"></a>

## Close idle connections in pools

If a connection has no read or write within the seconds specified by -idle\_timeout\_second, it’s tagged as “idle”, and will be closed automatically. Default value is 10 seconds. This feature is only effective to pooled connections. If -log\_idle\_connection\_close is true, a log is printed before closing.

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| idle\_timeout\_second | 10 | Pooled connections without data transmission for so many seconds will be closed. No effect for non-positive values | src/brpc/socket\_map.cpp |
| log\_idle\_connection\_close | false | Print log when an idle connection is closed | src/brpc/socket.cpp |

<a id="client-basics--defer-connection-close"></a>

## Defer connection close

Multiple channels may share a connection via referential counting. When a channel releases last reference of the connection, the connection will be closed. But in some scenarios, channels are created just before sending RPC and destroyed after completion, in which case connections are probably closed and re-open again frequently, as costly as short connections.

One solution is to cache channels commonly used by user, which avoids frequent creation and destroying of channels. However brpc does not offer an utility for doing this right now, and it’s not trivial for users to implement it correctly.

Another solution is setting gflag -defer\_close\_second

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| defer\_close\_second | 0 | Defer close of connections for so many seconds even if the connection is not used by anyone. Close immediately for non-positive values | src/brpc/socket\_map.cpp |

After setting, connection is not closed immediately after last referential count, instead it will be closed after so many seconds. If a channel references the connection again during the wait, the connection resumes to normal. No matter how frequent channels are created, this flag limits the frequency of closing connections. Side effect of the flag is that file descriptors are not closed immediately after destroying of channels, if the flag is wrongly set to be large, number of active file descriptors in the process may be large as well.

<a id="client-basics--buffer-size-of-connections"></a>

## Buffer size of connections

-socket\_recv\_buffer\_size sets receiving buffer size of all connections, -1 by default (not modified)

-socket\_send\_buffer\_size sets sending buffer size of all connections, -1 by default (not modified)

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| socket\_recv\_buffer\_size | -1 | Set the recv buffer size of socket if this value is positive | src/brpc/socket.cpp |
| socket\_send\_buffer\_size | -1 | Set send buffer size of sockets if this value is positive | src/brpc/socket.cpp |

<a id="client-basics--log_id"></a>

## log\_id

set\_log\_id() sets a 64-bit integral log\_id, which is sent to the server-side along with the request, and often printed in server logs to associate different services accessed in a session. String-type log-id must be converted to 64-bit integer before setting.

<a id="client-basics--attachment"></a>

## Attachment

baidu\_std and hulu\_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf. As a client, data set in Controller::request\_attachment() will be received by server and response\_attachment() contains attachment sent back by the server.

Attachment is not compressed by framework.

In http/h2, attachment corresponds to [message body](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html), namely the data to post to server is stored in request\_attachment().

<a id="client-basics--turn-on-ssl"></a>

## Turn on SSL

Update openssl to the latest version before turning on SSL, since older versions of openssl may have severe security problems and support less encryption algorithms, which is against with the purpose of using SSL.
Set ChannelOptions.mutable\_ssl\_options() to enable SSL. Refer to [ssl\_options.h](https://github.com/brpc/brpc/blob/master/src/brpc/ssl_options.h) for the detailed options. ChannelOptions.has\_ssl\_options() checks if ssl\_options was set; ChannelOptions.ssl\_options() returns const reference to the ssl\_options.

```c++
// Enable client-side SSL and use default values.
options.mutable_ssl_options();

// Enable client-side SSL and customize values.
options.mutable_ssl_options()->ciphers_name = "...";
options.mutable_ssl_options()->sni_name = "...";
```

- Channels connecting to a single server or a cluster both support SSL (the initial implementation does not support cluster)
- After turning on SSL, all requests through this Channel will be encrypted. Users should create another Channel for non-SSL requests if needed.
- Accessibility improvements for HTTPS: Channel.Init recognizes https:// prefix and turns on SSL automatically; -http\_verbose prints certificate information when SSL is on.

<a id="client-basics--authentication"></a>

## Authentication

Generally there are 2 ways of authentication at the client side:

1. Request-based authentication: Each request carries authentication information. It’s more flexible since the authentication information can contain fields based on this particular request. However, this leads to a performance loss due to the extra payload in each request.
2. Connection-based authentication: Once a TCP connection has been established, the client sends an authentication packet. After it has been verfied by the server, subsequent requests on this connection no longer needs authentication. Compared with the former, this method can only carry some static information such as local IP in the authentication packet. However, it has better performance especially under single connection / connection pool scenario.

It’s very simple to implement the first method by just adding authentication data format into the request proto definition. Then send it as normal RPC in each request. To achieve the second one, brpc provides an interface for users to implement:

```c++
class Authenticator {
public:
    virtual ~Authenticator() {}

    // Implement this method to generate credential information
    // into `auth_str' which will be sent to `VerifyCredential'
    // at server side. This method will be called on client side.
    // Returns 0 on success, error code otherwise
    virtual int GenerateCredential(std::string* auth_str) const = 0;
};
```

When the user calls the RPC interface with a single connection to the same server, the framework guarantee that once the TCP connection has been established, the first request on the connection will contain the authentication string generated by `GenerateCredential`. Subsequent requests will not carried that string. The entire sending process is still highly concurrent since it won’t wait for the authentication result. If the verification succeeds, all requests return without error. Otherwise, if the verification fails, generally the server will close the connection and those requests will receive the corresponding error.

Currently only those protocols support client authentication: [baidu\_std](https://github.com/apache/brpc/blob/master/docs/cn/) (default protocol), HTTP, hulu\_pbrpc, ESP. For customized protocols, generally speaking, users could call the `Authenticator`’s interface to generate authentication string during the request packing process in order to support authentication.

<a id="client-basics--reset"></a>

## Reset

This method makes Controller back to the state as if it’s just created.

Don’t call Reset() during a RPC, which is undefined.

<a id="client-basics--compression"></a>

## Compression

set\_request\_compress\_type() sets compress-type of the request, no compression by default.

NOTE: Attachment is not compressed by brpc.

Check out [compress request body](#client-access-httph2--compress-request-body) to compress http/h2 body.

Supported compressions:

- brpc::CompressTypeSnappy : [snanpy](http://google.github.io/snappy/), compression and decompression are very fast, but compression ratio is low.
- brpc::CompressTypeGzip : [gzip](http://en.wikipedia.org/wiki/Gzip), significantly slower than snappy, with a higher compression ratio.
- brpc::CompressTypeZlib : [zlib](http://en.wikipedia.org/wiki/Zlib), 10%~20% faster than gzip but still significantly slower than snappy, with slightly better compression ratio than gzip.

Following table lists performance of different methods compressing and decompressing **data with a lot of duplications**, just for reference.

| Compress method | Compress size(B) | Compress time(us) | Decompress time(us) | Compress throughput(MB/s) | Decompress throughput(MB/s) | Compress ratio |
| --- | --- | --- | --- | --- | --- | --- |
| Snappy | 128 | 0.753114 | 0.890815 | 162.0875 | 137.0322 | 37.50% |
| Gzip | 10.85185 | 1.849199 | 11.2488 | 66.01252 | 47.66% |  |
| Zlib | 10.71955 | 1.66522 | 11.38763 | 73.30581 | 38.28% |  |
| Snappy | 1024 | 1.404812 | 1.374915 | 695.1555 | 710.2713 | 8.79% |
| Gzip | 16.97748 | 3.950946 | 57.52106 | 247.1718 | 6.64% |  |
| Zlib | 15.98913 | 3.06195 | 61.07665 | 318.9348 | 5.47% |  |
| Snappy | 16384 | 8.822967 | 9.865008 | 1770.946 | 1583.881 | 4.96% |
| Gzip | 160.8642 | 43.85911 | 97.13162 | 356.2544 | 0.78% |  |
| Zlib | 147.6828 | 29.06039 | 105.8011 | 537.6734 | 0.71% |  |
| Snappy | 32768 | 16.16362 | 19.43596 | 1933.354 | 1607.844 | 4.82% |
| Gzip | 229.7803 | 82.71903 | 135.9995 | 377.7849 | 0.54% |  |
| Zlib | 240.7464 | 54.44099 | 129.8046 | 574.0161 | 0.50% |  |

Following table lists performance of different methods compressing and decompressing **data with very few duplications**, just for reference.

| Compress method | Compress size(B) | Compress time(us) | Decompress time(us) | Compress throughput(MB/s) | Decompress throughput(MB/s) | Compress ratio |
| --- | --- | --- | --- | --- | --- | --- |
| Snappy | 128 | 0.866002 | 0.718052 | 140.9584 | 170.0021 | 105.47% |
| Gzip | 15.89855 | 4.936242 | 7.678077 | 24.7294 | 116.41% |  |
| Zlib | 15.88757 | 4.793953 | 7.683384 | 25.46339 | 107.03% |  |
| Snappy | 1024 | 2.087972 | 1.06572 | 467.7087 | 916.3403 | 100.78% |
| Gzip | 32.54279 | 12.27744 | 30.00857 | 79.5412 | 79.79% |  |
| Zlib | 31.51397 | 11.2374 | 30.98824 | 86.90288 | 78.61% |  |
| Snappy | 16384 | 12.598 | 6.306592 | 1240.276 | 2477.566 | 100.06% |
| Gzip | 537.1803 | 129.7558 | 29.08707 | 120.4185 | 75.32% |  |
| Zlib | 519.5705 | 115.1463 | 30.07291 | 135.697 | 75.24% |  |
| Snappy | 32768 | 22.68531 | 12.39793 | 1377.543 | 2520.582 | 100.03% |
| Gzip | 1403.974 | 258.9239 | 22.25825 | 120.6919 | 75.25% |  |
| Zlib | 1370.201 | 230.3683 | 22.80687 | 135.6524 | 75.21% |  |

<a id="client-basics--faq"></a>

# FAQ

<a id="client-basics--q-does-brpc-support-unix-domain-socket"></a>

### Q: Does brpc support unix domain socket?

No. Local TCP sockets performs just a little slower than unix domain socket since traffic over local TCP sockets bypasses network. Some scenarios where TCP sockets can’t be used may require unix domain sockets. We may consider the capability in future.

<a id="client-basics--q-fail-to-connect-to-xxxxxxxxxxxx-connection-refused"></a>

### Q: Fail to connect to xx.xx.xx.xx:xxxx, Connection refused

The remote server does not serve any more (probably crashed).

<a id="client-basics--q-often-met-connection-timedout-to-another-idc"></a>

### Q: often met Connection timedout to another IDC

![img](assets/images/connection-timedout_493aa0fdb479c470.png)

The TCP connection is not established within connection\_timeout\_ms, you have to tweak options:

```c++
struct ChannelOptions {
    ...
    // Issue error when a connection is not established after so many
    // milliseconds. -1 means wait indefinitely.
    // Default: 200 (milliseconds)
    // Maximum: 0x7fffffff (roughly 30 days)
    int32_t connect_timeout_ms;

    // Max duration of RPC over this Channel. -1 means wait indefinitely.
    // Overridable by Controller.set_timeout_ms().
    // Default: 500 (milliseconds)
    // Maximum: 0x7fffffff (roughly 30 days)
    int32_t timeout_ms;
    ...
};
```

NOTE: Connection timeout is not RPC timeout, which is printed as “Reached timeout=…”.

<a id="client-basics--q-synchronous-call-is-good-asynchronous-call-crashes"></a>

### Q: synchronous call is good, asynchronous call crashes

Check lifetime of Controller, Response and done. In asynchronous call, finish of CallMethod is not completion of RPC which is entering of done->Run(). So the objects should not deleted just after CallMethod, instead they should be delete in done->Run(). Generally you should allocate the objects on heap instead of putting them on stack. Check out [Asynchronous call](#client-basics--asynchronous-call) for details.

<a id="client-basics--q-how-to-make-requests-be-processed-once-and-only-once"></a>

### Q: How to make requests be processed once and only once

This issue is not solved on RPC layer. When response returns and being successful, we know the RPC is processed at server-side. When response returns and being rejected, we know the RPC is not processed at server-side. But when response is not returned, server may or may not process the RPC. If we retry, same request may be processed twice at server-side. Generally RPC services with side effects must consider [idempotence](http://en.wikipedia.org/wiki/Idempotence) of the service, otherwise retries may make side effects be done more than once and result in unexpected behavior. Search services with only read often have no side effects (during a search), being idempotent natually. But storage services that need to write have to design versioning or serial-number mechanisms to reject side effects that already happen, to keep idempoent.

<a id="client-basics--q-invalid-addressbnsgroupuser-personaduminj03"></a>

### Q: Invalid address=`bns://group.user-persona.dumi.nj03'

```
FATAL 04-07 20:00:03 7778 src/brpc/channel.cpp:123] Invalid address=`bns://group.user-persona.dumi.nj03'. You should use Init(naming_service_name, load_balancer_name, options) to access multiple servers.
```

Accessing servers under naming service needs the Init() with 3 parameters(the second param is `load_balancer_name`). The Init() here is with 2 parameters and treated by brpc as accessing single server, producing the error.

<a id="client-basics--q-both-sides-use-protobuf-why-cant-they-communicate-with-each-other"></a>

### Q: Both sides use protobuf, why can’t they communicate with each other

**protocol != protobuf**. protobuf serializes one package and a message of a protocol may contain multiple packages along with extra lengths, checksums, magic numbers. The capability offered by brpc that “write code once and serve multiple protocols” is implemented by converting data from different protocols to unified API, not on protobuf layer.

<a id="client-basics--q-why-c-clientserver-may-fail-to-talk-to-clientserver-in-other-languages"></a>

### Q: Why C++ client/server may fail to talk to client/server in other languages

Check if the C++ version turns on compression (Controller::set\_compress\_type), Currently RPC impl. in other languages do not support compression yet.

<a id="client-basics--ps-workflow-at-client-side"></a>

# PS: Workflow at Client-side

![img](assets/images/client-side_b820dea9c06c7edc.png)

Steps:

1. Create a [bthread\_id](https://github.com/brpc/brpc/blob/master/src/bthread/id.h) as correlation\_id of current RPC.
2. According to how the Channel is initialized, choose a server from global [SocketMap](https://github.com/brpc/brpc/blob/master/src/brpc/socket_map.h) or [LoadBalancer](https://github.com/brpc/brpc/blob/master/src/brpc/load_balancer.h) as destination of the request.
3. Choose a [Socket](https://github.com/brpc/brpc/blob/master/src/brpc/socket.h) according to connection type (single, pooled, short)
4. If authentication is turned on and the Socket is not authenticated yet, first request enters authenticating branch, other requests block until the branch writes authenticating information into the Socket. Server-side only verifies the first request.
5. According to protocol of the Channel, choose corresponding serialization callback to serialize request into [IOBuf](https://github.com/brpc/brpc/blob/master/src/butil/iobuf.h).
6. If timeout is set, setup timer. From this point on, avoid using Controller, since the timer may be triggered at anytime and calls user’s callback for timeout, which may delete Controller.
7. Sending phase is completed. If error occurs at any step, Channel::HandleSendFailed is called.
8. Write IOBuf with serialized data into the Socket and add Channel::HandleSocketFailed into id\_wait\_list of the Socket. The callback will be called when the write is failed or connection is broken before completion of RPC.
9. In synchronous call, Join correlation\_id; otherwise CallMethod() returns.
10. Send/receive messages to/from network.
11. After receiving response, get the correlation\_id inside, find out associated Controller within O(1) time. The lookup does not need to lock a global hashmap, and scales well.
12. Parse response according to the protocol
13. Call Controller::OnRPCReturned, which may retry errorous RPC, or complete the RPC. Call user’s done in asynchronous call. Destroy correlation\_id and wakeup joining threads.

---

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="client-combo-channels"></a>

<!-- source_url: https://brpc.apache.org/docs/client/combo-channels/ -->

<!-- page_index: 36 -->

# Combo channels

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Combo%20channels/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Combo%20channels)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Add sub channel](#client-combo-channels--add-sub-channel)
- [CallMapper](#client-combo-channels--callmapper)
- [ResponseMerger](#client-combo-channels--responsemerger)
- [Get the controller to each sub channel](#client-combo-channels--get-the-controller-to-each-sub-channel)

- [Using SelectiveChannel](#client-combo-channels--using-selectivechannel)
- [Example: divide traffic to multiple naming services](#client-combo-channels--example-divide-traffic-to-multiple-naming-services)

- [Using PartitionChannel](#client-combo-channels--using-partitionchannel)
- [Using DynamicPartitionChannel](#client-combo-channels--using-dynamicpartitionchannel)

# Combo channels

What is channel in bRPC?

With the growth of services, access patterns to downstream servers become increasingly complicated and often contain multiple RPCs in parallel or layered accesses. The complications could easily introduce tricky bugs around multi-threaded programming, which may even not be sensed by users and difficult to debug and reproduce. Moreover, implementations either support synchronous patterns only, or have totally different code for asynchronous patterns. Take running some code after completions of multiple asynchronous RPCs as an example, the synchronous pattern is often implemented as issuing multiple RPCs asynchronously and waiting for the completions respectively, while the asynchronous pattern is often implemented by a callback plus a referential count, which is decreased by one when one RPC completes. The callback is called when the count hits zero. Let’s see drawbacks of the solution:

- The code is inconsistent between synchronous and asynchronous pattern and it’s not trivial for users to move from one pattern to another. From the designing point of view, inconsistencies implies that the essence is probably not grasped yet.
- Cancellation is unlikely to be supported. It’s not easy to cancel a single RPC correctly, let alone combinations of RPC. However cancellations are necessary to end pointless waiting in many scenarios.
- Not composable. It’s hard to enclose the implementations above as one part of a “larger” pattern. The code can hardly be reused in a different scenario.

We need a better abstraction. If several channels are combined into a larger one with different access patterns enclosed, users would be able to do synchronous, asynchronous, cancelling operations with consistent and unified interfaces. The kind of channels are called combo channels in brpc.

<a id="client-combo-channels--parallelchannel"></a>

# ParallelChannel

`ParallelChannel` (referred to as “pchan” sometimes) sends requests to all internal sub channels in parallel and merges the responses. Users can modify requests via `CallMapper` and merge responses with `ResponseMerger`. `ParallelChannel` looks like a `Channel`:

- Support synchronous and asynchronous accesses.
- Can be destroyed immediately after initiating an asynchronous operation.
- Support cancellation.
- Support timeout.

Check [example/parallel\_echo\_c++](https://github.com/brpc/brpc/tree/master/example/parallel_echo_c++/) for an example.

Any subclasses of `brpc::ChannelBase` can be added into `ParallelChannel`, including `ParallelChannel` and other combo channels. Set `ParallelChannelOptions.fail_limit` to control maximum number of failures. When number of failed responses reaches the limit, the RPC is ended immediately rather than waiting for timeout.

A sub channel can be added to the same `ParallelChannel` more than once, which is useful when you need to initiate multiple asynchronous RPC to the same service and wait for their completions.

Following picture shows internal structure of `ParallelChannel` (Chinese in red: can be different from request/response respectively)

![img](assets/images/pchan_4b9d666722fcab6e.png)

<a id="client-combo-channels--add-sub-channel"></a>

## Add sub channel

A sub channel can be added into `ParallelChannel` by following API:

```c++
int AddChannel(brpc::ChannelBase* sub_channel,
               ChannelOwnership ownership,
               CallMapper* call_mapper,
               ResponseMerger* response_merger);
```

When `ownership` is `brpc::OWNS_CHANNEL`, `sub_channel` is destroyed when the `ParallelChannel` destructs. Although a sub channel may be added into a `ParallelChannel` multiple times, it’s deleted for at most once when `ownership` in one of the additions is `brpc::OWNS_CHANNEL`.

Calling `AddChannel` during a RPC over `ParallelChannel` is **NOT thread safe**.

<a id="client-combo-channels--callmapper"></a>

## CallMapper

This class converts RPCs to `ParallelChannel` to the ones to `sub channel`. If `call_mapper` is NULL, requests to the sub channel is just the ones to `ParallelChannel`, and responses are created by calling `New()` on the responses to `ParallelChannel`. `call_mapper` is deleted when `ParallelChannel` destructs. Due to the reference counting inside, one `call_mapper` can be associated with multiple sub channels.

```c++
class CallMapper {
public:
    virtual ~CallMapper();
 
    virtual SubCall Map(int channel_index/*starting from 0*/,
                        const google::protobuf::MethodDescriptor* method,
                        const google::protobuf::Message* request,
                        google::protobuf::Message* response) = 0;
};
```

`channel_index`: The position of the sub channel inside `ParallelChannel`, starting from zero.

`method/request/response`: Parameters to `ParallelChannel::CallMethod()`.

The returned `SubCall` configures the calls to the corresponding sub channel and has two special values:

- `SubCall::Bad()`: The call to ParallelChannel fails immediately and `Controller::ErrorCode()` is set to `EREQUEST`.
- `SubCall::Skip()`: Skip the call to this sub channel. If all sub channels are skipped, the call to ParallelChannel fails immediately and `Controller::ErrorCode()` is set to `ECANCELED`.

Common implementations of `Map()` are listed below:

- Broadcast the request. This is also the behavior when `call_mapper` is NULL:

```c++
  class Broadcaster : public CallMapper {
  public:
      SubCall Map(int channel_index/*starting from 0*/,
                  const google::protobuf::MethodDescriptor* method,
                  const google::protobuf::Message* request,
                  google::protobuf::Message* response) {
          // Use the method/request to pchan.
          // response is created by `new` and the last flag tells pchan to delete response after completion of the RPC
          return SubCall(method, request, response->New(), DELETE_RESPONSE);
      }
  };
```

- Modify some fields in the request before sending:

```c++
  class ModifyRequest : public CallMapper {
  public:
    SubCall Map(int channel_index/*starting from 0*/,
                const google::protobuf::MethodDescriptor* method,
                const google::protobuf::Message* request,
                google::protobuf::Message* response) {
        FooRequest* copied_req = brpc::Clone<FooRequest>(request);
        copied_req->set_xxx(...);
        // Copy and modify the request
        // The last flag tells pchan to delete the request and response after completion of the RPC
        return SubCall(method, copied_req, response->New(), DELETE_REQUEST | DELETE_RESPONSE);
    }
  };
```

- request/response already contains sub requests/responses, use them directly.

```c++
  class UseFieldAsSubRequest : public CallMapper {
  public:
    SubCall Map(int channel_index/*starting from 0*/,
                const google::protobuf::MethodDescriptor* method,
                const google::protobuf::Message* request,
                google::protobuf::Message* response) {
        if (channel_index >= request->sub_request_size()) {
            // Not enough sub_request. The caller doesn't provide same number of requests as number of sub channels in pchan
            // Return Bad() to end this RPC immediately
            return SubCall::Bad();
        }
        // Fetch the sub request and add a new sub response.
        // The last flag(0) tells pchan that there is nothing to delete.
        return SubCall(sub_method, request->sub_request(channel_index), response->add_sub_response(), 0);
    }
  };
```

<a id="client-combo-channels--responsemerger"></a>

## ResponseMerger

`response_merger` merges responses from all sub channels into one for the `ParallelChannel`. When it’s NULL, `response->MergeFrom(*sub_response)` is used instead, whose behavior can be summarized as “merge repeated fields and overwrite the rest”. If you need more complex behavior, implement `ResponseMerger`. Multiple `response_merger` are called one by one to merge sub responses so that you do not need to consider the race conditions between merging multiple responses simultaneously. The object is deleted when `ParallelChannel` destructs. Due to the reference counting inside, `response_merger` can be associated with multiple sub channels.

Possible values of `Result` are:

- MERGED: Successfully merged.
- FAIL: The `sub_response` was not merged successfully, counted as one failure. For example, there are 10 sub channels and `fail_limit` is 4, if 4 merges return FAIL, the RPC would reach fail\_limit and end soon.
- FAIL\_ALL: Directly fail the RPC.

<a id="client-combo-channels--get-the-controller-to-each-sub-channel"></a>

## Get the controller to each sub channel

Sometimes users may need to know the details around sub calls. `Controller.sub(i)` gets the controller corresponding to a sub channel.

```c++
// Get the controllers for accessing sub channels in combo channels.
// Ordinary channel:
//   sub_count() is 0 and sub() is always NULL.
// ParallelChannel/PartitionChannel:
//   sub_count() is #sub-channels and sub(i) is the controller for
//   accessing i-th sub channel inside ParallelChannel, if i is outside
//    [0, sub_count() - 1], sub(i) is NULL.
//   NOTE: You must test sub() against NULL, ALWAYS. Even if i is inside
//   range, sub(i) can still be NULL:
//   * the rpc call may fail and terminate before accessing the sub channel
//   * the sub channel was skipped
// SelectiveChannel/DynamicPartitionChannel:
//   sub_count() is always 1 and sub(0) is the controller of successful
//   or last call to sub channels.
int sub_count() const;
const Controller* sub(int index) const;
```

<a id="client-combo-channels--selectivechannel"></a>

# SelectiveChannel

[SelectiveChannel](https://github.com/brpc/brpc/blob/master/src/brpc/selective_channel.h) (referred to as “schan” sometimes) accesses one of the internal sub channels with a load balancing algorithm. It’s more high-level compared to ordinary channels: The requests are sent to sub channels instead of servers directly. `SelectiveChannel` is mainly for load balancing between groups of machines and shares basic properties of `Channel`:

- Support synchronous and asynchronous accesses.
- Can be destroyed immediately after initiating an asynchronous operation.
- Support cancellation.
- Support timeout.

Check [example/selective\_echo\_c++](https://github.com/brpc/brpc/tree/master/example/selective_echo_c++/) for an example.

Any subclasses of `brpc::ChannelBase` can be added into `SelectiveChannel`, including `SelectiveChannel` and other combo channels.

Retries done by `SelectiveChannel` are independent from the ones in its sub channels. When a call to one of the sub channels fails(which may have been retried), other sub channels are retried.

Currently `SelectiveChannel` requires **the request remains valid before completion of the RPC**, while other combo or regular channels do not. If you plan to use `SelectiveChannel` asynchronously, make sure that the request is deleted inside `done`.

<a id="client-combo-channels--using-selectivechannel"></a>

## Using SelectiveChannel

The initialization of `SelectiveChannel` is almost the same as regular `Channel`, except that it doesn’t need a naming service in `Init`, because `SelectiveChannel` adds sub channels dynamically by `AddChannel`, while regular `Channel` adds servers in the naming service.

```c++
#include <brpc/selective_channel.h>
...
brpc::SelectiveChannel schan;
brpc::ChannelOptions schan_options;
schan_options.timeout_ms = ...;
schan_options.backup_request_ms = ...;
schan_options.max_retry = ...;
if (schan.Init(load_balancer, &schan_options) != 0) {
    LOG(ERROR) << "Fail to init SelectiveChannel";
    return -1;
}
```

After successful initialization, add sub channels with `AddChannel`.

```c++
// The second parameter ChannelHandle is used to delete sub channel,
// which can be NULL if this isn't necessary.
if (schan.AddChannel(sub_channel, NULL/*ChannelHandle*/) != 0) { 
    LOG(ERROR) << "Fail to add sub_channel";
    return -1;
}
```

Note that:

- Unlike `ParallelChannel`, `SelectiveChannel::AddChannel` can be called at any time, even if a RPC over the SelectiveChannel is going on. (newly added channels take effects at the next RPC).
- `SelectiveChannel` always owns sub channels, which is different from `ParallelChannel`’s configurable ownership.
- If the second parameter to `AddChannel` is not NULL, it’s filled with a value typed `brpc::SelectiveChannel::ChannelHandle`, which can be used as the parameter to `RemoveAndDestroyChannel` to remove and destroy a channel dynamically.
- `SelectiveChannel` overrides timeouts in sub channels. For example, having timeout set to 100ms for a sub channel and 500ms for `SelectiveChannel`, the actual timeout is 500ms.

`SelectiveChannel`s are accessed same as regular channels.

<a id="client-combo-channels--example-divide-traffic-to-multiple-naming-services"></a>

## Example: divide traffic to multiple naming services

Sometimes we need to divide traffic to multiple naming services, because:

- Machines for one service are listed in multiple naming services.
- Machines are split into multiple groups. Requests are sent to one of the groups and then routed to one of the machines inside the group, and traffic are divided differently between groups and machines in a group.

Above requirements can be achieved by `SelectiveChannel`.

Following code creates a `SelectiveChannel` and inserts 3 regular channels for different naming services respectively.

```c++
brpc::SelectiveChannel channel;
brpc::ChannelOptions schan_options;
schan_options.timeout_ms = FLAGS_timeout_ms;
schan_options.max_retry = FLAGS_max_retry;
if (channel.Init("c_murmurhash", &schan_options) != 0) {
    LOG(ERROR) << "Fail to init SelectiveChannel";
    return -1;
}
 
for (int i = 0; i < 3; ++i) {
    brpc::Channel* sub_channel = new brpc::Channel;
    if (sub_channel->Init(ns_node_name[i], "rr", NULL) != 0) {
        LOG(ERROR) << "Fail to init sub channel " << i;
        return -1;
    }
    if (channel.AddChannel(sub_channel, NULL/*handle for removal*/) != 0) {
        LOG(ERROR) << "Fail to add sub_channel to channel";
        return -1;
    } 
}
...
XXXService_Stub stub(&channel);
stub.FooMethod(&cntl, &request, &response, NULL);
...
```

<a id="client-combo-channels--partitionchannel"></a>

# PartitionChannel

[PartitionChannel](https://github.com/brpc/brpc/blob/master/src/brpc/partition_channel.h) is a specialized `ParallelChannel` to add sub channels automatically based on tags defined in the naming service. As a result, users can list all machines in one naming service and partition them by tags. Check [example/partition\_echo\_c++](https://github.com/brpc/brpc/tree/master/example/partition_echo_c++/) for an example.

`ParititonChannel` only supports one kind to partitioning method. When multiple methods need to coexist, or one method needs to be changed to another smoothly, try `DynamicPartitionChannel`, which creates corresponding sub `PartitionChannel` for different partitioning methods, and divide traffic to partitions according to capacities of servers. Check [example/dynamic\_partition\_echo\_c++](https://github.com/brpc/brpc/tree/master/example/dynamic_partition_echo_c++/) for an example.

If partitions are listed in different naming services, users have to implement the partitioning by `ParallelChannel` and include sub channels to corresponding naming services respectively. Refer to [the previous section](#client-combo-channels--parallelchannel) for usages of `ParellelChannel`.

<a id="client-combo-channels--using-partitionchannel"></a>

## Using PartitionChannel

First of all, implement your own `PartitionParser`. In this example, the tag’s format is `N/M`, where N is index of the partition and M is total number of partitions. `0/3` means that there’re 3 partitions and this is the first one of them.

```c++
#include <brpc/partition_channel.h>
...
class MyPartitionParser : public brpc::PartitionParser {
public:
    bool ParseFromTag(const std::string& tag, brpc::Partition* out) {
        // "N/M" : #N partition of M partitions.
        size_t pos = tag.find_first_of('/');
        if (pos == std::string::npos) {
            LOG(ERROR) << "Invalid tag=" << tag;
            return false;
        }
        char* endptr = NULL;
        out->index = strtol(tag.c_str(), &endptr, 10);
        if (endptr != tag.data() + pos) {
            LOG(ERROR) << "Invalid index=" << butil::StringPiece(tag.data(), pos);
            return false;
        }
        out->num_partition_kinds = strtol(tag.c_str() + pos + 1, &endptr, 10);
        if (endptr != tag.c_str() + tag.size()) {
            LOG(ERROR) << "Invalid num=" << tag.data() + pos + 1;
            return false;
        }
        return true;
    }
};
```

Then initialize the `PartitionChannel`.

```c++
#include <brpc/partition_channel.h>
...
brpc::PartitionChannel channel;
 
brpc::PartitionChannelOptions options;
options.protocol = ...;   // PartitionChannelOptions inherits ChannelOptions
options.timeout_ms = ...; // Same as above
options.fail_limit = 1;   // PartitionChannel's own settting, which means the same as that of
                          // ParalellChannel. fail_limit=1 means the overall RPC will fail 
                          // as long as only 1 paratition fails
 
if (channel.Init(num_partition_kinds, new MyPartitionParser(),
                 server_address, load_balancer, &options) != 0) {
    LOG(ERROR) << "Fail to init PartitionChannel";
    return -1;
}
// The RPC interface is the same as regular Channel
```

<a id="client-combo-channels--using-dynamicpartitionchannel"></a>

## Using DynamicPartitionChannel

`DynamicPartitionChannel` and `PartitionChannel` are basically same on usages. Implement `PartitionParser` first then initialize the channel, which does not need `num_partition_kinds` since `DynamicPartitionChannel` dynamically creates sub `PartitionChannel` for each partition.

Following sections demonstrate how to use `DynamicPartitionChannel` to migrate from 3 partitions to 4 partitions smoothly.

First of all, start 3 servers serving on port 8004, 8005, 8006 respectively.

```
$ ./echo_server -server_num 3
TRACE: 09-06 10:40:39:   * 0 server.cpp:159] EchoServer is serving on port=8004
TRACE: 09-06 10:40:39:   * 0 server.cpp:159] EchoServer is serving on port=8005
TRACE: 09-06 10:40:39:   * 0 server.cpp:159] EchoServer is serving on port=8006
TRACE: 09-06 10:40:40:   * 0 server.cpp:192] S[0]=0 S[1]=0 S[2]=0 [total=0]
TRACE: 09-06 10:40:41:   * 0 server.cpp:192] S[0]=0 S[1]=0 S[2]=0 [total=0]
TRACE: 09-06 10:40:42:   * 0 server.cpp:192] S[0]=0 S[1]=0 S[2]=0 [total=0]
```

Note that each server prints summaries on traffic received in last second, which is all 0 now.

Start a client using `DynamicPartitionChannel`, which is initialized as follows:

```c++
    ...
    brpc::DynamicPartitionChannel channel;
    brpc::PartitionChannelOptions options;
    // Failure on any single partition fails the RPC immediately. You can use a more relaxed value
    options.fail_limit = 1;                         
    if (channel.Init(new MyPartitionParser(), "file://server_list", "rr", &options) != 0) {
        LOG(ERROR) << "Fail to init channel";
        return -1;
    }
    ...
```

The content inside the naming service `file://server_list` is:

```
0.0.0.0:8004  0/3  # The first partition of the three
0.0.0.0:8004  1/3  # and so forth
0.0.0.0:8004  2/3
```

All 3 partitions are put on the server on port 8004, so the client begins to send requests to 8004 once started.

```
$ ./echo_client
TRACE: 09-06 10:51:10:   * 0 src/brpc/policy/file_naming_service.cpp:83] Got 3 unique addresses from `server_list'
TRACE: 09-06 10:51:10:   * 0 src/brpc/socket.cpp:779] Connected to 0.0.0.0:8004 via fd=3 SocketId=0 self_port=46544
TRACE: 09-06 10:51:11:   * 0 client.cpp:226] Sending EchoRequest at qps=132472 latency=371
TRACE: 09-06 10:51:12:   * 0 client.cpp:226] Sending EchoRequest at qps=132658 latency=370
TRACE: 09-06 10:51:13:   * 0 client.cpp:226] Sending EchoRequest at qps=133208 latency=369
```

At the same time, the server on 8004 received tripled traffic due to the 3 partitions.

```
TRACE: 09-06 10:51:11:   * 0 server.cpp:192] S[0]=398866 S[1]=0 S[2]=0 [total=398866]
TRACE: 09-06 10:51:12:   * 0 server.cpp:192] S[0]=398117 S[1]=0 S[2]=0 [total=398117]
TRACE: 09-06 10:51:13:   * 0 server.cpp:192] S[0]=398873 S[1]=0 S[2]=0 [total=398873]
```

Add new 4 partitions on the server on port 8005.

```
0.0.0.0:8004  0/3
0.0.0.0:8004  1/3   
0.0.0.0:8004  2/3 
 
0.0.0.0:8005  0/4        
0.0.0.0:8005  1/4        
0.0.0.0:8005  2/4        
0.0.0.0:8005  3/4
```

Notice how summaries change. The client is aware of the modification to `server_list` and reloads it, but the QPS hardly changes.

```
TRACE: 09-06 10:57:10:   * 0 src/brpc/policy/file_naming_service.cpp:83] Got 7 unique addresses from `server_list'
TRACE: 09-06 10:57:10:   * 0 src/brpc/socket.cpp:779] Connected to 0.0.0.0:8005 via fd=7 SocketId=768 self_port=39171
TRACE: 09-06 10:57:11:   * 0 client.cpp:226] Sending EchoRequest at qps=135346 latency=363
TRACE: 09-06 10:57:12:   * 0 client.cpp:226] Sending EchoRequest at qps=134201 latency=366
TRACE: 09-06 10:57:13:   * 0 client.cpp:226] Sending EchoRequest at qps=137627 latency=356
TRACE: 09-06 10:57:14:   * 0 client.cpp:226] Sending EchoRequest at qps=136775 latency=359
TRACE: 09-06 10:57:15:   * 0 client.cpp:226] Sending EchoRequest at qps=139043 latency=353
```

The server-side summary changes more obviously. The server on port 8005 has received requests and the proportion between traffic to 8004 and 8005 is roughly 3:4.

```
TRACE: 09-06 10:57:09:   * 0 server.cpp:192] S[0]=398597 S[1]=0 S[2]=0 [total=398597]
TRACE: 09-06 10:57:10:   * 0 server.cpp:192] S[0]=392839 S[1]=0 S[2]=0 [total=392839]
TRACE: 09-06 10:57:11:   * 0 server.cpp:192] S[0]=334704 S[1]=83219 S[2]=0 [total=417923]
TRACE: 09-06 10:57:12:   * 0 server.cpp:192] S[0]=206215 S[1]=273873 S[2]=0 [total=480088]
TRACE: 09-06 10:57:13:   * 0 server.cpp:192] S[0]=204520 S[1]=270483 S[2]=0 [total=475003]
TRACE: 09-06 10:57:14:   * 0 server.cpp:192] S[0]=207055 S[1]=273725 S[2]=0 [total=480780]
TRACE: 09-06 10:57:15:   * 0 server.cpp:192] S[0]=208453 S[1]=276803 S[2]=0 [total=485256]
```

The traffic proportion between 8004 and 8005 is 3:4, considering that each RPC needs 3 calls to 8004 or 4 calls to 8005, the client issues requests to both partitioning methods in 1:1 manner, which depends on capacities calculated recursively:

- The capacity of a regular `Channel` is sum of capacities of servers that it addresses. Capacity of a server is 1 by default if the naming services does not configure weights.
- The capacity of `ParallelChannel` or `PartitionChannel` is the minimum of all its sub channel’s.
- The capacity of `SelectiveChannel` is the sum of all its sub channel’s.
- The capacity of `DynamicPartitionChannel` is the sum of all its sub `PartitionChannel`’s.

In this example, capacities of the 3-partition method and the 4-partition method are both 1, since the 3 partitions are all on the server on 8004 and the 4 partitions are all on the server on 8005.

Add the server on 8006 to the 4-partition method:

```
0.0.0.0:8004  0/3
0.0.0.0:8004  1/3   
0.0.0.0:8004  2/3
 
0.0.0.0:8005  0/4   
0.0.0.0:8005  1/4   
0.0.0.0:8005  2/4   
0.0.0.0:8005  3/4    
 
0.0.0.0:8006 0/4
0.0.0.0:8006 1/4
0.0.0.0:8006 2/4
0.0.0.0:8006 3/4
```

The client still hardly changes.

```
TRACE: 09-06 11:11:51:   * 0 src/brpc/policy/file_naming_service.cpp:83] Got 11 unique addresses from `server_list'
TRACE: 09-06 11:11:51:   * 0 src/brpc/socket.cpp:779] Connected to 0.0.0.0:8006 via fd=8 SocketId=1280 self_port=40759
TRACE: 09-06 11:11:51:   * 0 client.cpp:226] Sending EchoRequest at qps=131799 latency=372
TRACE: 09-06 11:11:52:   * 0 client.cpp:226] Sending EchoRequest at qps=136217 latency=361
TRACE: 09-06 11:11:53:   * 0 client.cpp:226] Sending EchoRequest at qps=133531 latency=368
TRACE: 09-06 11:11:54:   * 0 client.cpp:226] Sending EchoRequest at qps=136072 latency=361
```

Notice the traffic on 8006 at the server side. The capacity of the 3-partition method is still 1 while capacity of the 4-partition method increases to 2 due to the addition of the server on 8006, thus the overall proportion between the methods becomes 3:8. Each partition inside the 4-partition method has 2 instances on 8005 and 8006 respectively, between which the round-robin load balancing is applied to split the traffic. As a result, the traffic proportion between the 3 servers becomes 3:4:4.

```
TRACE: 09-06 11:11:51:   * 0 server.cpp:192] S[0]=199625 S[1]=263226 S[2]=0 [total=462851]
TRACE: 09-06 11:11:52:   * 0 server.cpp:192] S[0]=143248 S[1]=190717 S[2]=159756 [total=493721]
TRACE: 09-06 11:11:53:   * 0 server.cpp:192] S[0]=133003 S[1]=178328 S[2]=178325 [total=489656]
TRACE: 09-06 11:11:54:   * 0 server.cpp:192] S[0]=135534 S[1]=180386 S[2]=180333 [total=496253]
```

See what happens if one partition in the 3-partition method is removed: (You can comment one line in file://server\_list by #)

```
 0.0.0.0:8004  0/3
 0.0.0.0:8004  1/3
#0.0.0.0:8004  2/3
 
 0.0.0.0:8005  0/4   
 0.0.0.0:8005  1/4   
 0.0.0.0:8005  2/4   
 0.0.0.0:8005  3/4    
 
 0.0.0.0:8006 0/4
 0.0.0.0:8006 1/4
 0.0.0.0:8006 2/4
 0.0.0.0:8006 3/4
```

The client senses the change in `server_list`:

```
TRACE: 09-06 11:17:47:   * 0 src/brpc/policy/file_naming_service.cpp:83] Got 10 unique addresses from `server_list'
TRACE: 09-06 11:17:47:   * 0 client.cpp:226] Sending EchoRequest at qps=131653 latency=373
TRACE: 09-06 11:17:48:   * 0 client.cpp:226] Sending EchoRequest at qps=120560 latency=407
TRACE: 09-06 11:17:49:   * 0 client.cpp:226] Sending EchoRequest at qps=124100 latency=395
TRACE: 09-06 11:17:50:   * 0 client.cpp:226] Sending EchoRequest at qps=123743 latency=397
```

The traffic on 8004 drops to zero quickly at the server side. The reason is that the 3-partition method is not complete anymore once the last 2/3 partition has been removed. The capacity becomes zero and no requests are sent to the server on 8004 anymore.

```
TRACE: 09-06 11:17:47:   * 0 server.cpp:192] S[0]=130864 S[1]=174499 S[2]=174548 [total=479911]
TRACE: 09-06 11:17:48:   * 0 server.cpp:192] S[0]=20063 S[1]=230027 S[2]=230098 [total=480188]
TRACE: 09-06 11:17:49:   * 0 server.cpp:192] S[0]=0 S[1]=245961 S[2]=245888 [total=491849]
TRACE: 09-06 11:17:50:   * 0 server.cpp:192] S[0]=0 S[1]=250198 S[2]=250150 [total=500348]
```

In real online environments, we gradually increase the number of instances on the 4-partition method and removes instances on the 3-partition method. `DynamicParititonChannel` divides the traffic based on capacities of all partitions dynamically. When capacity of the 3-partition method drops to 0, we’ve smoothly migrated all servers from 3 partitions to 4 partitions without changing the client-side code.

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="client-dummy-server"></a>

<!-- source_url: https://brpc.apache.org/docs/client/dummy-server/ -->

<!-- page_index: 37 -->

# Dummy server

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Dummy%20server/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Dummy%20server)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Dummy server

Learn how to use dummy server.

If your program only uses client in brpc or doesn’t use brpc at all, but you also want to use built-in services in brpc. The thing you should do is to start an empty server, which is called **dummy server**.

<a id="client-dummy-server--client-in-brpc-is-used"></a>

# client in brpc is used

Create a file named dummy\_server.port which contains a port number(such as 8888) in the running directory of program, a dummy server would be started at this port. All of the bvar in the same process can be seen by visiting its built-in service.
![img](assets/images/dummy-server-1_fa1c4850473d15b1.png) ![img](assets/images/dummy-server-2_83bfd9402ac703db.png)

![img](assets/images/dummy-server-3_8e9f18db84290621.png)

<a id="client-dummy-server--brpc-is-not-used-at-all"></a>

# brpc is not used at all

You must manually add the dummy server. First read [Getting Started](#getting_started) to learn how to download and compile brpc, and then add the following code snippet at the program entry:

```c++
#include <brpc/server.h>
 
...
 
int main() {
    ...
    brpc::StartDummyServerAt(8888/*port*/);
    ...
}
```

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="client-error-code"></a>

<!-- source_url: https://brpc.apache.org/docs/client/error-code/ -->

<!-- page_index: 38 -->

# Error code

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Error%20code/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Error%20code)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Error code

Learn the error code of bRPC client.

brpc use [brpc::Controller](https://github.com/brpc/brpc/blob/master/src/brpc/controller.h) to set and get parameters for one RPC. `Controller::ErrorCode()` and `Controller::ErrorText()` return error code and description of the RPC respectively, only accessible after completion of the RPC, otherwise the result is undefined. `ErrorText()` is defined by the base class of the Controller: `google::protobuf::RpcController`, while `ErrorCode()` is defined by `brpc::Controller`. Controller also has a method `Failed()` to tell whether RPC fails or not. Relations between the three methods:

- When `Failed()` is true, `ErrorCode()` must be non-zero and `ErrorText()` be non-empty.
- When `Failed()` is false, `ErrorCode()` is 0 and `ErrorText()` is undefined (it’s empty in brpc currently, but you’d better not rely on this)

<a id="client-error-code--mark-rpc-as-failed"></a>

# Mark RPC as failed

Both client and server in brpc have `Controller`, which can be set with `setFailed()` to modify ErrorCode and ErrorText. Multiple calls to `Controller::SetFailed` leave the last ErrorCode and **concatenate** ErrorTexts rather than leaving the last one. The framework elaborates ErrorTexts by adding extra prefixes: number of retries at client-side and address of the server at server-side.

`Controller::SetFailed()` at client-side is usually called by the framework, such as sending failure, incomplete response, and so on. Error may be set at client-side under some situations. For example, you may set error to the RPC if an additional check before sending the request is failed.

`Controller::SetFailed()` at server-side is often called by the user in the service callback. Generally speaking when error occurs, users call `SetFailed()`, release all the resources, and return from the callback. The framework fills the error code and message into the response according to communication protocol. When the response is received, the error inside are set into the client-side Controller so that users can fetch them after end of RPC. Note that **server does not print errors to clients by default**, as frequent loggings may impact performance of the server significantly due to heavy disk IO. A client crazily producing errors could slow the entire server down and affect all other clients, which can even become an attacking method against the server. If you really want to see error messages on the server, turn on the gflag **-log\_error\_text** (modifiable at run-time), the server will log the ErrorText of corresponding Controller of each failed RPC.

<a id="client-error-code--error-code-in-brpc"></a>

# Error Code in brpc

All error codes in brpc are defined in [errno.proto](https://github.com/brpc/brpc/blob/master/src/brpc/errno.proto), in which those begin with *SYS\_* are defined by linux system and exactly same with the ones defined in `/usr/include/errno.h`. The reason that we put it in .proto is to cross language. The rest of the error codes are defined by brpc.

[berror(error\_code)](https://github.com/brpc/brpc/blob/master/src/butil/errno.h) gets description for the error code, and `berror()` gets description for current [system errno](http://www.cplusplus.com/reference/cerrno/errno/). Note that **ErrorText() != berror(ErorCode())** since `ErrorText()` contains more specific information. brpc includes berror by default so that you can use it in your project directly.

Following table shows common error codes and their descriptions:

| Error Code | Value | Retry | Description | Logging message |
| --- | --- | --- | --- | --- |
| EAGAIN | 11 | Yes | Too many requests at the same time, hardly happening as it’s a soft limit. | Resource temporarily unavailable |
| ENODATA | 61 | 是 | 1. The server list returned by Naming Service is empty. 2. When Naming Service changes with all instances modified, Naming Service updates LB by first Remove all and then Add all, the LB instance list may become empty within a short period of time. | Fail to select server from xxx |
| ETIMEDOUT | 110 | Yes | Connection timeout. | Connection timed out |
| EHOSTDOWN | 112 | Yes | Possible reasons: A. The list returned by Naming Server is not empty, but LB cannot select an available server, and LB returns an EHOSTDOWN error. Specific possible reasons: a. Server is exiting (returned ELOGOFF) b. Server was blocked because of some previous failure, the specific logic of the block: 1. For single connection type, the only connection socket is blocked by SetFail, and there are many occurrences of SetFailed in the code to trigger this block. 2. For pooled/short connection type, only when the error number meets does\_error\_affect\_main\_socket (ECONNREFUSED, ENETUNREACH, EHOSTUNREACH or EINVAL) will it be blocked 3. After blocking, there is a CheckHealth thread to do health check, Just try to connect, the check interval is controlled by the health\_check\_interval\_s of SocketOptions, and the Socket will be unblocked if it is connected successfully. B. Use the SingleServer method to initialize the Channel (without LB), and the only connection is LOGOFF or blocked (same as above) | “Fail to select server from …” “Not connected to … yet” |
| ENOSERVICE | 1001 | No | Can’t locate the service, hardly happening and usually being ENOMETHOD instead |  |
| ENOMETHOD | 1002 | No | Can’t locate the method. | Misc forms, common ones are “Fail to find method=…” |
| EREQUEST | 1003 | No | fail to serialize the request, may be set on either client-side or server-side | Misc forms: “Missing required fields in request: …” “Fail to parse request message, …” “Bad request” |
| EAUTH | 1004 | No | Authentication failed | “Authentication failed” |
| ETOOMANYFAILS | 1005 | No | Too many sub-channel failures inside a ParallelChannel | “%d/%d channels failed, fail\_limit=%d” |
| EBACKUPREQUEST | 1007 | Yes | Set when backup requests are triggered. Not returned by ErrorCode() directly, viewable from spans in /rpcz | “reached backup timeout=%dms” |
| ERPCTIMEDOUT | 1008 | No | RPC timeout. | “reached timeout=%dms” |
| EFAILEDSOCKET | 1009 | Yes | The connection is broken during RPC | “The socket was SetFailed” |
| EHTTP | 1010 | No | HTTP responses with non 2xx status code are treated as failure and set with this code. No retry by default, changeable by customizing RetryPolicy. | Bad http call |
| EOVERCROWDED | 1011 | Yes | Too many messages to buffer at the sender side. Usually caused by lots of concurrent asynchronous requests. Modifiable by `-socket_max_unwritten_bytes`, 8MB by default. | The server is overcrowded |
| EINTERNAL | 2001 | No | The default error for `Controller::SetFailed` without specifying a one. | Internal Server Error |
| ERESPONSE | 2002 | No | fail to serialize the response, may be set on either client-side or server-side | Misc forms: “Missing required fields in response: …” “Fail to parse response message, " “Bad response” |
| ELOGOFF | 2003 | Yes | Server has been stopped | “Server is going to quit” |
| ELIMIT | 2004 | Yes | Number of requests being processed concurrently exceeds `ServerOptions.max_concurrency` | “Reached server’s limit=%d on concurrent requests” |

<a id="client-error-code--user-defined-error-code"></a>

# User-defined Error Code

In C/C++, error code can be defined in macros, constants or enums:

```c++
#define ESTOP -114                // C/C++
static const int EMYERROR = 30;   // C/C++
const int EMYERROR2 = -31;        // C++ only
```

If you need to get the error description through `berror`, register it in the global scope of your c/cpp file by `BAIDU_REGISTER_ERRNO(error_code, description)`, for example:

```c++
BAIDU_REGISTER_ERRNO(ESTOP, "the thread is stopping")
BAIDU_REGISTER_ERRNO(EMYERROR, "my error")
```

Note that `strerror` and `strerror_r` do not recognize error codes defined by `BAIDU_REGISTER_ERRNO`. Neither does the `%m` used in `printf`. You must use `%s` paired with `berror`:

```c++
errno = ESTOP;
printf("Describe errno: %m\n");                              // [Wrong] Describe errno: Unknown error -114
printf("Describe errno: %s\n", strerror_r(errno, NULL, 0));  // [Wrong] Describe errno: Unknown error -114
printf("Describe errno: %s\n", berror());                    // [Correct] Describe errno: the thread is stopping
printf("Describe errno: %s\n", berror(errno));               // [Correct] Describe errno: the thread is stopping
```

When the registration of an error code is duplicated, a linking error is generated provided it’s defined in C++:

```
redefinition of `class BaiduErrnoHelper<30>'
```

Or the program aborts before start:

```
Fail to define EMYERROR(30) which is already defined as `Read-only file system', abort
```

You have to make sure that different modules have same understandings on same ErrorCode. Otherwise, interactions between two modules that interpret an error code differently may be undefined. To prevent this from happening, you’d better follow these:

- Prefer system error codes which have fixed values and meanings, generally.
- Share code on error definitions between multiple modules to prevent inconsistencies after modifications.
- Use `BAIDU_REGISTER_ERRNO` to describe new error code to ensure that same error code is defined only once inside a process.

---

Last modified January 9, 2022: [A new verion of brpc website based on hugo (94b25d711)](https://github.com/apache/brpc-website/commit/94b25d7110944f3d4b2071b5188c691b23ffe3a9)

---

<a id="client"></a>

<!-- source_url: https://brpc.apache.org/docs/client/ -->

<!-- page_index: 39 -->

# Client

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Client)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Client

Learn how to use bRPC client.

---

##### [Basics](#client-basics)

Learn how to use bRPC client.

##### [Error code](#client-error-code)

Learn the error code of bRPC client.

##### [Combo channels](#client-combo-channels)

What is channel in bRPC?

##### [Access http:h2](#client-access-httph2)

Learn how to access Http2.

##### [Access gRPC](#client-access-grpc)

Learn how to access gRPC.

##### [Access thrift](#client-access-thrift)

Learn how to access thrift.

##### [Access UB](#client-access-ub)

Learn how to access UB.

##### [Access redis](#client-access-redis)

Learn how to access redis.

##### [Access memcached](#client-access-memcached)

Learn how to access memcached.

##### [Streaming RPC](#client-streaming-rpc)

Learn how to use streaming rpc.

##### [Backup request](#client-backup-request)

Learn how to use backup request.

##### [Dummy server](#client-dummy-server)

Learn how to use dummy server.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="client-streaming-rpc"></a>

<!-- source_url: https://brpc.apache.org/docs/client/streaming-rpc/ -->

<!-- page_index: 40 -->

# Streaming RPC

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Client/Streaming%20RPC/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Streaming%20RPC)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Streaming RPC

Learn how to use streaming rpc.

There are some scenarios when the client or server needs to send huge amount of data, which may grow over time or is too large to put into the RPC attachment. For example, it could be the replica or snapshot transmitting between different nodes in a distributed system. Although we could send data segmentation across multiple RPC between client and server, this will introduce the following problems:

- If these RPCs are parallel, there is no guarantee on the order of the data at the receiving side, which leads to complicate code of reassembling.
- If these RPCs are serial, we have to endure the latency of the network RTT for each RPC together with the process time, which is especially unpredictable.

In order to allow large packets to flow between client and server like a stream, we provide a new communication model: Streaming RPC. Streaming RPC enables users to establishes Stream which is a user-space connection between client and service. Multiple Streams can share the same TCP connection at the same time. The basic transmission unit on Stream is message. As a result, the sender can continuously write to messages to a Stream, while the receiver can read them out in the order of sending.

Streaming RPC ensures/provides:

- The message order at the receiver is exactly the same as that of the sender
- Boundary for messages
- Full duplex
- Flow control
- Notification on timeout

We do not support segment large messages automatically so that multiple Streams on a single TCP connection may lead to [Head-of-line blocking](https://en.wikipedia.org/wiki/Head-of-line_blocking) problem. Please avoid putting huge data into single message until we provide automatic segmentation.

For examples please refer to [example/streaming\_echo\_c++](https://github.com/brpc/brpc/tree/master/example/streaming_echo_c++/).

<a id="client-streaming-rpc--create-a-stream"></a>

# Create a Stream

Currently stream is established by the client only. A new Stream object is created in client and then is used to issues an RPC (through baidu\_std protocol) to the specified service. The service could accept this stream by responding to the request without error, thus a Stream is created once the client receives the response successfully. Any error during this process fails the RPC and thus fails the Stream creation. Take the Linux environment as an example, the client creates a [socket](http://linux.die.net/man/7/socket) first (creates a Stream), and then try to establish a connection with the remote side by [connect](http://linux.die.net/man/2/connect) (establish a Stream through RPC). Finally the stream has been created once the remote side [accept](http://linux.die.net/man/2/accept) the request.

> If the client tries to establish a stream to a server that doesn’t support streaming RPC, it will always return failure.

In the code we use `StreamId` to represent a Stream, which is the key ID to pass when reading, writing, closing the Stream.

```c++
struct StreamOptions
    // The max size of unconsumed data allowed at remote side.
    // If |max_buf_size| <= 0, there's no limit of buf size
    // default: 2097152 (2M)
    int max_buf_size;
 
    // Notify user when there's no data for at least |idle_timeout_ms|
    // milliseconds since the last time that on_received_messages or on_idle_timeout
    // finished.
    // default: -1
    long idle_timeout_ms;
     
    // Maximum messages in batch passed to handler->on_received_messages
    // default: 128
    size_t messages_in_batch;
 
    // Handle input message, if handler is NULL, the remote side is not allowd to
    // write any message, who will get EBADF on writting
    // default: NULL
    StreamInputHandler* handler;
};
 
// [Called at the client side]
// Create a Stream at client-side along with the |cntl|, which will be connected
// when receiving the response with a Stream from server-side. If |options| is
// NULL, the Stream will be created with default options
// Return 0 on success, -1 otherwise
int StreamCreate(StreamId* request_stream, Controller &cntl, const StreamOptions* options);
```

<a id="client-streaming-rpc--accept-a-stream"></a>

# Accept a Stream

If a Stream is attached inside the request of an RPC, the service can accept the Stream by `StreamAccept`. On success this function fill the created Stream into `response_stream`, which can be used to send message to the client.

```c++
// [Called at the server side]
// Accept the Stream. If client didn't create a Stream with the request
// (cntl.has_remote_stream() returns false), this method would fail.
// Return 0 on success, -1 otherwise.
int StreamAccept(StreamId* response_stream, Controller &cntl, const StreamOptions* options);
```

<a id="client-streaming-rpc--read-from-a-stream"></a>

# Read from a Stream

Upon creating/accepting a Stream, your can fill the `hander` in `StreamOptions` with your own implemented `StreamInputHandler`. Then you will be notified when the stream receives data, is closed by the other end, or reaches idle timeout.

```c++
class StreamInputHandler {
public:
    // Callback when stream receives data
    virtual int on_received_messages(StreamId id, butil::IOBuf *const messages[], size_t size) = 0;
 
    // Callback when there is no data for a long time on the stream
    virtual void on_idle_timeout(StreamId id) = 0;
 
    // Callback when stream is closed by the other end
    virtual void on_closed(StreamId id) = 0;
};
```

> ***The first call to `on_received_message`***
>
> On the client’s side, if the creation process is synchronous, `on_received_message` will be called when the blocking RPC returns. If it’s asynchronous, `on_received_message` won’t be called until `done->Run()` finishes.
>
> On the server’ side, `on_received_message` will be called once `done->Run()` finishes.

<a id="client-streaming-rpc--write-to-a-stream"></a>

# Write to a Stream

```c++
// Write |message| into |stream_id|. The remote-side handler will received the
// message by the written order
// Returns 0 on success, errno otherwise
// Errno:
//  - EAGAIN: |stream_id| is created with positive |max_buf_size| and buf size
//            which the remote side hasn't consumed yet excceeds the number.
//  - EINVAL: |stream_id| is invalied or has been closed
int StreamWrite(StreamId stream_id, const butil::IOBuf &message);
```

<a id="client-streaming-rpc--flow-control"></a>

# Flow Control

When the amount of unacknowledged data reaches the limit, the `Write` operation at the sender will fail with EAGAIN immediately. At this moment, you should wait for the receiver to consume the data synchronously or asynchronously.

```c++
// Wait util the pending buffer size is less than |max_buf_size| or error occurs
// Returns 0 on success, errno otherwise
// Errno:
//  - ETIMEDOUT: when |due_time| is not NULL and time expired this
//  - EINVAL: the Stream was close during waiting
int StreamWait(StreamId stream_id, const timespec* due_time);
 
// Async wait
void StreamWait(StreamId stream_id, const timespec *due_time,
                void (*on_writable)(StreamId stream_id, void* arg, int error_code),
                void *arg);
```

<a id="client-streaming-rpc--close-a-stream"></a>

# Close a Stream

```c++
// Close |stream_id|, after this function is called:
//  - All the following |StreamWrite| would fail
//  - |StreamWait| wakes up immediately.
//  - Both sides |on_closed| would be notifed after all the pending buffers have
//    been received
// This function could be called multiple times without side-effects
int StreamClose(StreamId stream_id);
```

---

Last modified January 9, 2022: [A new verion of brpc website based on hugo (94b25d711)](https://github.com/apache/brpc-website/commit/94b25d7110944f3d4b2071b5188c691b23ffe3a9)

---

<a id="community-committer"></a>

<!-- source_url: https://brpc.apache.org/docs/community/committer/ -->

<!-- page_index: 41 -->

# Committer Guide

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/committer/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Committer%20Guide)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- - [The Apache Way:](#community-committer--the-apache-way)
  - [Guidance for Committer:](#community-committer--guidance-for-committer)
  - [Guidance for PMC member:](#community-committer--guidance-for-pmc-member)
  - [Peer Review:](#community-committer--peer-review)

- [1. How to develop committers](#community-committer--1-how-to-develop-committers)
  - [Preconditions](#community-committer--preconditions)
  - [The journey to become a committer](#community-committer--the-journey-to-become-a-committer)
  - [How to grant a committer permission on github](#community-committer--how-to-grant-a-committer-permission-on-github)
  - [Documents related to the new committer on the official Apache website](#community-committer--documents-related-to-the-new-committer-on-the-official-apache-website)
  - [Suggested steps from [secretary@apache.org](mailto:secretary@apache.org)](#community-committer--suggested-steps-from-secretaryapacheorg)
- [2. How to upgrade a committer into a PPMC](#community-committer--2-how-to-upgrade-a-committer-into-a-ppmc)

# Committer Guide

How to be a bRPC Committer

<a id="community-committer--introduction"></a>

# Introduction

Participants in the Apache community have the following roles: **Contributor**, **Committer**, and **PMC(Project Member Committee) member**.

When an individual contribution is accepted by the project, he/she will automatically become a Contributor.
Committer and PMC members are invited by the PMC after a consensus vote.

Here we will only discuss some guidelines for the bRPC community to invite Committer and PMC member in order to be able to effectively estimate developer participation in the community.

<a id="community-committer--the-apache-way"></a>

### The Apache Way:

Before anyone can become a Committer or PMC member of an Apache project, they should first understand “[What’s TheApacheWay](https://apache.org/theapacheway/index.html)”.

<a id="community-committer--guidance-for-committer"></a>

### Guidance for Committer:

Have significant feature contributions (not limited to code), or long-term participation in community building (bug fixing, code review, documentation translation and proofreading, community outreach, etc.)
Participate in community discussions in public domain and have a positive impact.

<a id="community-committer--guidance-for-pmc-member"></a>

### Guidance for PMC member:

Be able to actively participate in community maintenance work, such as answering emails, organizing wiki, release management, code review, etc.
Recognize the Apache community philosophy and be able to actively promote the community development.

<a id="community-committer--peer-review"></a>

### Peer Review:

The above requirements are highly subjective and cannot be measured quantitatively. Therefore, the PMC needs to form a regular review mechanism to discuss and invite people who meet the requirements.

Conduct a review every 1-2 months to nominate and discuss suitable candidates

---

<a id="community-committer--detailed-procedures"></a>

# Detailed Procedures

<a id="community-committer--1-how-to-develop-committers"></a>

## 1. How to develop committers

<a id="community-committer--preconditions"></a>

### Preconditions

1. More than 10 commits from the contributor
2. Contributor is willing to accept the invitation to become a committer
3. Contributor subscribe to [dev@brpc.apache.org](mailto:dev@brpc.apache.org) and introduce himself by sending an email to [dev@apache.org](mailto:dev@apache.org)

<a id="community-committer--the-journey-to-become-a-committer"></a>

### The journey to become a committer

1. The nominator sends an email to private@brpc to initiate discussion and begins to voting. If the voting is passed, it is OK (at least 3 +1, +1 >- 1). (See the Vote email template <https://community.apache.org/newcommitter.html#committer-vote-template>)
2. The nominator sends a close vote email to private@brpc and private@incubator , the title can be subject [RESULT] [VOTE]. (See the close email template <https://community.apache.org/newcommitter.html#close-vote>)
3. The nominator sends an invitation letter to the nominee and prompts him to submit ICLA after receiving a reply. (See the template in <https://community.apache.org/newcommitter.html#committer-invite-template>)
4. The nominee fills in ICLA（ <https://www.apache.org/licenses/contributor-agreements.html> ）, individual contributors need to download [ICLA]（ <https://www.apache.org/licenses/icla.pdf> ）Fill in personal information and sign, and send the electronic version to [secretary@apache.org](mailto:secretary@apache.org) 。 (Note: ICLA needs to fill in complete information, including mailing address and signature, otherwise it will be returned by ASF’s secretary.) The personal information entry (except for the signature) can be filled in with a PDF reader or browser, and then saved for signature. Signature method support:
   - Print pdf documents and scan them into electronic version after handwritten signature;
   - Electronic signature using devices that support handwriting;
   - Use ‘gpg’ for electronic signature, that is, to operate the pdf file filled with personal basic information (a public key/key pair matching the registered mailbox needs to be generated in advance): ‘gpg – armor – detach sign icla. pdf’;
   - Use ‘DocuSign’ to sign;
5. The nominator sends an announcement email to [dev@brpc.apache.org](mailto:dev@brpc.apache.org)

<a id="community-committer--how-to-grant-a-committer-permission-on-github"></a>

### How to grant a committer permission on github

1. Add as committer (<https://whimsy.apache.org/roster/ppmc/brpc>)
2. Let him set github id (<https://id.apache.org/>)
3. Let him visit the website and get github permission([https://gitbox.apache.org/setup/](https://id.apache.org/))

<a id="community-committer--documents-related-to-the-new-committer-on-the-official-apache-website"></a>

### Documents related to the new committer on the official Apache website

- <https://community.apache.org/newcommitter.html>
- <https://infra.apache.org/new-committers-guide.html>
- <https://juejin.cn/post/6844903788982042632>

<a id="community-committer--suggested-steps-from-secretaryapacheorg"></a>

### Suggested steps from [secretary@apache.org](mailto:secretary@apache.org)

Please do these things:

1. Hold the discussion and vote on your private@ list. This avoids any issues related to personnel, which should remain private.
2. If the vote is successful, announce the result to the private@ list with a new email thread with subject [RESULT][VOTE]. This makes it easier for secretary to find the result of the vote in order to request the account at the time of the filing of the ICLA.
3. Only if the candidate accepts committership, announce the new committer on your dev@ list.

Doing these things will make everyone’s job easier.

<a id="community-committer--2-how-to-upgrade-a-committer-into-a-ppmc"></a>

## 2. How to upgrade a committer into a PPMC

<a id="community-committer--process-reference-apache-official-website-document"></a>

### Process reference: Apache official website document

- <https://incubator.apache.org/guides/ppmc.html#voting_in_a_new_ppmc_member>
- <https://community.apache.org/newcommitter.html>
- <https://incubator.apache.org/guides/ppmc.html#podling_project_management_committee_ppmc>

<a id="community-committer--actual-process"></a>

### Actual process

1. Initiate discussion in the private@brpc . If there is no objection, continue
2. Open a Vote in private@brpc
3. If the vote is successful, sends a message to the PPMC private email list about the vote result
4. send a message to the IPMC ([private@incubator.apache.org](mailto:private@incubator.apache.org)) with a reference to the vote result
5. Announce new PPMC On private@brpc
6. Set his authority by visiting <https://whimsy.apache.org/roster/ppmc/brpc>
7. Help him subscribe to a private email group. See <https://whimsy.apache.org/committers/moderationhelper.cgi>

Last modified November 4, 2022: [Update index.md (6307ba4d7)](https://github.com/apache/brpc-website/commit/6307ba4d7c1d66f666d4c4294b5fac12dbc9092c)

---

<a id="community-committers"></a>

<!-- source_url: https://brpc.apache.org/docs/community/committers/ -->

<!-- page_index: 42 -->

# Committers

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/committers/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Committers)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [bRRC Committers](#community-committers--brrc-committers)
  - [PMC](#community-committers--pmc)
  - [Committers](#community-committers--committers)
  - [Contributors](#community-committers--contributors)

# Committers

bRPC Committers

<a id="community-committers--brrc-committers"></a>

## bRRC Committers

The development of bRPC is associated with the outstanding contributions from the people in the community, who have helped get the project to where it is today.

Thank you all your help!

<a id="community-committers--pmc"></a>

### PMC

| **Photo** | **Full Name** | **Apache ID** | **GitHub** |
| --- | --- | --- | --- |
|  | James Ge | jamesge | [jamesge](http://github.com/jamesge) |
|  | Jiashun Zhu | jiashunzhu | [zyearn](http://github.com/zyearn) |
|  | Zhangyi Chen | zychen | [chenzhangyi](http://github.com/chenzhangyi) |
|  | Bear Jiang | jrjbear | [old-bear](http://github.com/old-bear) |
|  | Yao Wang | fisherman | [ipconfigme](http://github.com/ipconfigme) |
|  | Jerry Tan | jerrytan | [tanzhongyi003](http://github.com/tanzhongyi003) |
|  | Wang Weibing | wwbmmm | [wwbmmm](http://github.com/wwbmmm) |
|  | He Lei | leander | [TousakaRin](http://github.com/TousakaRin) |
|  | Cai Daojin | caidj | [cdjingit](http://github.com/cdjingit) |
|  | Lorin Lee | lorinlee | [lorinlee](http://github.com/lorinlee) |
|  | Guangming Chen | guangmingchen | [chenBright](http://github.com/chenBright) |

<a id="community-committers--committers"></a>

### Committers

| **Photo** | **Full Name** | **Apache ID** | **GitHub** |
| --- | --- | --- | --- |
|  | Mou Gaidong | gydong | [gydong](http://github.com/gydong) |
|  | Wang wei | guodong | [guodongxiaren](http://github.com/guodongxiaren) |
|  | Shuai Liu | serverglen | [serverglen](http://github.com/serverglen) |
|  | Wang Xiaofeng | xiaofeng | [wasphin](http://github.com/wasphin) |
|  | Xiguo Hu | huixxi | [Huixxi](http://github.com/Huixxi) |
|  | Zhaogeng Li | lizhaogeng | [Tuvie](http://github.com/Tuvie) |

<a id="community-committers--contributors"></a>

### Contributors

Thanks to [All the Contributors](https://github.com/apache/brpc/graphs/contributors) making their effort to help bRPC getting better.

Last modified January 7, 2025: [Update PMC list (a0cec8e8c)](https://github.com/apache/brpc-website/commit/a0cec8e8c4e844a623ec02f37886cdad921e43ac)

---

<a id="community-community"></a>

<!-- source_url: https://brpc.apache.org/docs/community/community/ -->

<!-- page_index: 43 -->

# Community

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/community/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Community)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Apache bRPC Community](#community-community--apache-brpc-community)
  - [Issue tracker](#community-community--issue-tracker)
  - [Source Code](#community-community--source-code)
  - [Website Source Code](#community-community--website-source-code)

# Community

About bRPC community

<a id="community-community--apache-brpc-community"></a>

## Apache bRPC Community

Every volunteer project obtains its strength from the people involved in it. We invite you to participate as much or as little as you choose.

You can:

- Use our project and provide a feedback.
- Provide us with the use-cases.
- Report bugs and submit patches.
- Contribute code, testcase, documentation.

Visit the [Contributing](#community-contributing) page for more information.

<a id="community-community--issue-tracker"></a>

### Issue tracker

<a id="community-community--bug-reports"></a>

#### Bug Reports

Found bug? Enter an issue in the [Issue Tracker](https://github.com/apache/brpc/issues).

Before submitting an issue, please:

- Verify that the bug does in fact exist.
- Search the issue tracker to verify there is no existing issue reporting the bug you’ve found.
- Consider tracking down the bug yourself in the bRPC’s source and submitting a patch along with your bug report. This is a great time saver for the bRPC developers and helps ensure the bug will be fixed quickly.

<a id="community-community--feature-requests"></a>

#### Feature Requests

Enhancement requests for new features are also welcome. The more concrete and rationale the request is, the greater the chance it will incorporated into future releases.

<https://github.com/apache/brpc/issues>

<a id="community-community--source-code"></a>

### Source Code

The project sources are accessible via the [source code repository](https://github.com/apache/brpc) which is on github.

<a id="community-community--website-source-code"></a>

### Website Source Code

The project website sources are accessible via the [website source code repository](https://github.com/apache/brpc-website) which is on github also.

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="community-contributing"></a>

<!-- source_url: https://brpc.apache.org/docs/community/contributing/ -->

<!-- page_index: 44 -->

# Contribute Guide

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/contributing/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Contribute%20Guide)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Contribute Guide

Contribute to bRPC

If you meet any problem or request a new feature, you’re welcome to [create an issue](https://github.com/brpc/brpc/issues/new/choose).

If you can solve any of [the issues](https://github.com/brpc/brpc/issues), you’re welcome to send the PR to us.

Before the PR:

- Fully comply with the [ASF Code of Conduct](https://www.apache.org/foundation/policies/conduct.html).
- Make sure your code style conforms to [google C++ coding style](https://google.github.io/styleguide/cppguide.html). Indentation is preferred to be 4 spaces.
- The code appears where it should be. For example the code to support an extra protocol should not be put in general classes like server.cpp, channel.cpp, while a general modification would better not be hidden inside a very specific protocol.
- Has unittests.

After the PR:

- Make sure the [travis-ci](https://app.travis-ci.com/github/apache/brpc/pull_requests) passed.

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="community"></a>

<!-- source_url: https://brpc.apache.org/docs/community/ -->

<!-- page_index: 45 -->

# Community

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Community)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Community

About bRPC community

---

##### [Community](#community-community)

About bRPC community

##### [Mailing List](#community-mailing_list)

Subscribe Mailing List

##### [Contribute Guide](#community-contributing)

Contribute to bRPC

##### [Committer Guide](#community-committer)

How to be a bRPC Committer

##### [Release Guide](https://brpc.apache.org/docs/community/release/)

How to publish a bRPC release

##### [Committers](#community-committers)

bRPC Committers

##### [Security](#community-security)

About security

##### [Monthly Meeting](#community-monthly-meeting)

About Monthly Meeting

##### [On Call](#community-on-call)

About On Call

Last modified November 9, 2022: [update download page (2cb8ce4b9)](https://github.com/apache/brpc-website/commit/2cb8ce4b93efbf28c7aa8aa0e6c297c4ea6a5b73)

---

<a id="community-mailing_list"></a>

<!-- source_url: https://brpc.apache.org/docs/community/mailing_list/ -->

<!-- page_index: 46 -->

# Mailing List

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/mailing_list/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Mailing%20List)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Mailing List

Subscribe Mailing List

<a id="community-mailing_list--about-mailing-list"></a>

### About Mailing List

Mailing list is where we discuss in public and keep everything tracked, When using or contributing to bRPC, if you encounter any problem, or you have any suggestions or new ideas, you can use the Apache mailing-list to participate in the community building.

If you have a specific bug to report or feature request, we’d suggest you opening an issue on our [GitHub repo](https://github.com/apache/brpc/issues/new/choose), which is a more efficient way to report the details.

- [dev@brpc.apache.org](https://brpc.apache.org/docs/community/mailing_list/dev@brpc.apache.org) is for people who want to contribute code to bRPC. [subscribe](mailto:dev-subscribe@brpc.apache.org?subject=send%20this%20email%20to%20subscribe), [unsubscribe](mailto:dev-unsubscribe@brpc.apache.org?subject=send%20this%20email%20to%20unsubscribe), [archives](https://www.mail-archive.com/dev@brpc.apache.org/)
- [commits@brpc.apache.org](https://brpc.apache.org/docs/community/mailing_list/commits@brpc.apache.org) is for commit messages and patches to bRPC. [subscribe](mailto:commits-subscribe@brpc.apache.org?subject=send%20this%20email%20to%20subscribe), [unsubscribe](mailto:commits-unsubscribe@brpc.apache.org?subject=send%20this%20email%20to%20unsubscribe), [archives](https://www.mail-archive.com/commits@brpc.apache.org/)

<a id="community-mailing_list--subscribe-mailing-lists"></a>

### Subscribe Mailing Lists

<a id="community-mailing_list--1-send-subscription-mail"></a>

#### 1. Send Subscription Mail

Open your own email, create a new email, and send an email to [dev-subscribe@brpc.apache.org](mailto:dev-subscribe@brpc.apache.org) (subject and content are arbitrary).

<a id="community-mailing_list--2-receive-confirmation-emails-from-dev-helpbrpcapacheorg"></a>

#### 2. Receive confirmation emails from [dev-help@brpc.apache.org](mailto:dev-help@brpc.apache.org)

After the first step, you will receive a confirmation email from [dev-help@brpc.apache.org](mailto:dev-help@brpc.apache.org), which is shown below (If you fail to receive it for a long time, please confirm that the mail has been intercepted, or has been automatically grouped into “Subscribed Mail”, “Spam Mail”, “Promotional Mail” folders).

<a id="community-mailing_list--3-reply-to-confirmation-mail"></a>

#### 3. Reply to confirmation mail

For the mail received in the previous step, Reply to this email directly or Create a new recipient e-mail for the reply address in the previous step.

Every subject is acceptable.

<a id="community-mailing_list--4-receiving-welcome-emails"></a>

#### 4. Receiving Welcome Emails

After completing the third step, you will receive a welcome email entitled WELCOME to [dev@brpc.apache.org](mailto:dev@brpc.apache.org). So far, the work of subscribing to mailing lists has been completed, and community dynamics will be notified by mail.

<a id="community-mailing_list--5-initiate-e-mail-discussion-optional"></a>

#### 5. Initiate e-mail discussion (optional)

After successfully subscribing to the mailing list, if you want to initiate a discussion, send an email directly to [dev@brpc.apache.org](mailto:dev@brpc.apache.org). Anyone who subscribes to the mailing list receives the mail.

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="community-monthly-meeting"></a>

<!-- source_url: https://brpc.apache.org/docs/community/monthly-meeting/ -->

<!-- page_index: 47 -->

# Monthly Meeting

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/monthly-meeting/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Monthly%20Meeting)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Monthly Meeting

About Monthly Meeting

<a id="community-monthly-meeting--monthly-meeting-record"></a>

### Monthly Meeting Record

| Month | Host | Minutes Of Meeting |
| --- | --- | --- |
| 2023-02 | Wang Weibing | <https://lists.apache.org/thread/opzmc74yhhokox0164f2o5wv60o74nct> |
| 2023-03 | Liu Shuai | <https://lists.apache.org/thread/38rswlzl51lqvl04bvf6ho0od8smrc4z> |

Last modified April 4, 2023: [Monthly meeting (#138) (b965598cb)](https://github.com/apache/brpc-website/commit/b965598cb13fb22d8ca21d8f4bcfccf1e9025c5e)

---

<a id="community-on-call"></a>

<!-- source_url: https://brpc.apache.org/docs/community/on-call/ -->

<!-- page_index: 48 -->

# On Call

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/on-call/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=On%20Call)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Duty of the On Call](#community-on-call--duty-of-the-on-call)
  - [1. Review and process the Pull Request and Issue list](#community-on-call--1-review-and-process-the-pull-request-and-issue-list)
  - [2. The rotation time is one week](#community-on-call--2-the-rotation-time-is-one-week)
  - [3. Needed at the end of On Call](#community-on-call--3-needed-at-the-end-of-on-call)
  - [4. On Call Order](#community-on-call--4-on-call-order)
  - [5. On Call Record](#community-on-call--5-on-call-record)

# On Call

About On Call

<a id="community-on-call--duty-of-the-on-call"></a>

## Duty of the On Call

<a id="community-on-call--1-review-and-process-the-pull-request-and-issue-list"></a>

### 1. Review and process the Pull Request and Issue list

- Check the Pull Request and Issue list of brpc project on github every day, and be responsible for the problem handling
- Including marking the issue, replying to the issue, closing the issue, etc.
- Determine whether the issue is a long-term Issue. If so, mark it as Pending
  Determine the type of Issue, e.g. bug, enhancement, discussion, etc
- Assign issues to contributors who are familiar with the module (ask who is responsible in the wechat group)

<a id="community-on-call--2-the-rotation-time-is-one-week"></a>

### 2. The rotation time is one week

- From Monday morning to Sunday night

<a id="community-on-call--3-needed-at-the-end-of-on-call"></a>

### 3. Needed at the end of On Call

- Write a weekly value report and send it to the [dev@brpc.apache.org](mailto:dev@brpc.apache.org) email group
- Update value weekly record (brpc-website)
- Remind the next shift student

<a id="community-on-call--4-on-call-order"></a>

### 4. On Call Order

- Zhu Jiashun @zyearn
- Li Lei @lorinlee
- Wang Weibing @wwbmmm
- CAI Daojin @cdjingit
- He Lei @TousakaRin
- Shuai Liu @serverglen
- Huixxi @Huixxi
- Yang Liming @yanglimingcn

<a id="community-on-call--5-on-call-record"></a>

### 5. On Call Record

| Date (Month/Day/year) | Name | report |
| --- | --- | --- |
| 06/21/2021 to 06/27/2021 | Li Lei | <https://lists.apache.org/thread/czolsqo80jzsytqc7dp37knqwxnkymx1> |
| 06/28/2021 to 07/04/2021 | Cai Daojin | <https://lists.apache.org/thread/c05fcjdjh7473ho1ylyl98mxscmnkbv0> |
| 07/05/2021 - 07/12/2021 | He Lei | <https://lists.apache.org/thread/hz1vn7358v5fslglg2cl4g8x0wtxy4lv> |
| 08/16/2021 - 08/22/2021 | Zhu Jiashun | <https://lists.apache.org/thread/g36jtjc3v75lfoc7m3ynzplgbqlsjjrd> |
| 08/23/2021 - 08/29/2021 | Li Lei | <https://lists.apache.org/thread/2098ndgdy6fs2b1s8tywpmz47n5swh29> |
| 08/30/2021 - 09/05/2021 | Cai Daojin | <https://lists.apache.org/thread/wjxdomg7fp75dc0n0rmh37bkwd8w7myv> |
| 09/06/2021 - 09/12/2021 | He Lei | <https://lists.apache.org/thread/cwjtocpjbqjgndog53rqw8gs6f9c0rmo> |
| 09/20/2021 - 09/26/2021 | Li Lei | <https://lists.apache.org/thread/p779y43hogv7ftckc4cqx006gv9j65r8> |
| 09/27/2021 - 10/03/2021 | Cai Daojin | <https://lists.apache.org/thread/ync12fx2dwjb2l3p4yck0kodmkgzz7wd> |
| 12/13/2021 - 12/19/2021 | Cai Daojin | <https://lists.apache.org/thread/mvclsy79859mrbdso1xzm6y7yz3lg6w0> |
| 01/24/2022 - 02/06/2022 | Wang Weibing | <https://lists.apache.org/thread/ttgqnw4hfw0qnb7swvnn2kxb5b9hkdbo> |
| 04/10/2022 - 04/16/2022 | Liu Shuai | <https://lists.apache.org/thread/0l67lqnw0l6rgfwkvhrc168prwr7fp60> |
| 04/17/2022 - 04/24/2022 | Zhu Jiashun | <https://lists.apache.org/thread/xwkpyonndgtp8tq4c9v4yfowqx7fg9gl> |
| 04/25/2022 - 05/01/2022 | Li Lei | <https://lists.apache.org/thread/cx7t1glptr7x7posxstsb1691h4m4mbl> |
| 05/02/2022 - 05/15/2022 | Wang Weibing | <https://lists.apache.org/thread/tgyqkhh6fqgyzcn5d56kt46hk978wogx> |
| 06/06/2022 - 06/12/2022 | He Lei | <https://lists.apache.org/thread/s19p7ygnsj0bknfjvrh0wlf1mbgstxbk> |
| 06/13/2022 - 06/19/2022 | Liu Shuai | <https://lists.apache.org/thread/tvqjyz6rh7jb1zcclx0lh6zrcsf9ykxr> |
| 07/25/2022 - 07/31/2022 | Wang Weibing | <https://lists.apache.org/thread/83scwkkfxrp6kkkoltbrn1fthfy3w0qz> |
| 08/08/2022 - 08/14/2022 | He Lei | <https://lists.apache.org/thread/jj16rzfh34yrt6o0xqfdz9wtdtzxzswq> |
| 08/15/2022 - 08/21/2022 | Liu Shuai | <https://lists.apache.org/thread/jp69sm7c8fs3dkdd828qk0fsojqwwz6h> |
| 09/05/2022 - 09/12/2022 | Wang Weibing | <https://lists.apache.org/thread/4jjk2hxw9s2wskccclqb8fvpqxqffnlb> |
| 09/12/2022 - 09/18/2022 | Cai Daojin | <https://lists.apache.org/thread/8mo7zl0l2yrd8tp4v3kx86rnlyfk6wz4> |
| 09/19/2022 - 09/25/2022 | He Lei | <https://lists.apache.org/thread/qlkr7cmwow3ob47dt80tpx0zrgzg7bdm> |
| 09/26/2022 - 10/09/2022 | Liu Shuai | <https://lists.apache.org/thread/b0lwr8wyflmhqlnf0kkh1j30tgt5qw54> |
| 10/10/2022 - 10/16/2022 | Zhu Jiashun | <https://lists.apache.org/thread/y8sgbprxt21j6r0812dlftosfov6pbgk> |
| 10/17/2022 - 10/23/2022 | Li Lei | <https://lists.apache.org/thread/qn2270p9qsrglkh7oy013ts1zk5rlhwx> |
| 10/24/2022 - 10/30/2022 | Wang Weibing | <https://lists.apache.org/thread/k74155opmwmopgtsqo6p79z9q0f0sv8j> |
| 10/31/2022 - 11/06/2022 | Cai Daojin | <https://lists.apache.org/thread/t4z49yt7ymp4vr5sms0m4cpoo94db4oz> |
| 11/14/2022 - 11/20/2022 | Liu Shuai | <https://lists.apache.org/thread/nq50fp79ox3follc7gxp814cvcqnmqzz> |
| 11/21/2022 - 11/27/2022 | Zhu Jiashun | <https://lists.apache.org/thread/57kzov5g3j4vv6l2zcyw0msm36qglc8k> |
| 11/28/2022 - 12/04/2022 | Li Lei | <https://lists.apache.org/thread/92hbzcd662slj75v3ndjf69o1dgsnd6o> |
| 12/05/2022 - 12/11/2022 | Wang Weibing | <https://lists.apache.org/thread/99o15h9hk5dd73jv8wyp49l8mbw0j611> |
| 12/19/2022 - 12/25/2022 | He Lei | <https://lists.apache.org/thread/g1stjjo1mc9ds47do6gosrw5k6wwb9mj> |
| 12/26/2022 - 01/01/2023 | Liu Shuai | <https://lists.apache.org/thread/3xw1gkobqmvr6oo375x3gsfcqvg80n23> |
| 01/02/2023 - 01/08/2023 | Zhu Jiashun | <https://lists.apache.org/thread/sm4f209c8ltols04gpmzo386b02dyc9s> |
| 01/09/2023 - 01/15/2023 | Li Lei | <https://lists.apache.org/thread/fydjz4h88omsrb7fzw65wl64kh5r520s> |
| 01/16/2023 - 01/29/2023 | Wang Weibing | <https://lists.apache.org/thread/k5bb4pn2v23dksmwpwqphzlc4bd92ndr> |
| 01/30/2023 - 02/05/2023 | Cai Daojin | <https://lists.apache.org/thread/4scwpdh163l92czm5pvc7ox78n44mrn4> |
| 02/13/2023 - 02/19/2023 | Liu Shuai | <https://lists.apache.org/thread/jwynp880hdhcfkqwq7thsm05y037wzy5> |
| 02/27/2023 - 03/05/2023 | Li Lei | <https://lists.apache.org/thread/94ndftsvooydfnn8hdddv294pp0tfvdm> |
| 03/06/2023 - 03/12/2023 | Wang Weibing | <https://lists.apache.org/thread/bv3qw5w8gj9xs576fplxqhktopkbk7md> |
| 03/27/2023 - 04/03/2023 | Liu Shuai | <https://lists.apache.org/thread/fk37cn8r5pd1y10vjvzvkl211b67vn4q> |
| 04/04/2023 - 04/10/2023 | Xiguo Hu | <https://lists.apache.org/thread/p8f5knxkohj1kw5g9wb9hfbw2bjzjs3r> |
| 04/10/2023 - 04/17/2023 | Zhu Jiashun | <https://lists.apache.org/thread/l0l1402r8yz7kl2w4hwc835rc1n5o22c> |
| 04/17/2023 - 04/23/2023 | Lei Li | <https://lists.apache.org/thread/3gobs94vogdjg6pmkvbk5kst4z9xbdw9> |
| 04/24/2023 - 05/07/2023 | Wang Weibing | <https://lists.apache.org/thread/25ocwx3n7kvmj0fd5zz5slwd0smt59r2> |
| 05/08/2023 - 05/14/2023 | Cai Daojin | <https://lists.apache.org/thread/676w7087klhsb2hwn9q2p5sj541frgpl> |
| 05/22/2023 - 05/28/2023 | Liu Shuai | <https://lists.apache.org/thread/m2cpr83h5l1gpznowxhf58lrxndok1lp> |
| 06/19/2023 - 06/25/2023 | Wang Weibing | <https://lists.apache.org/thread/jto9mzcbsxw3273xrgwd116vvdl3o1gx> |
| 06/26/2023 - 07/02/2023 | Cai Daojin | <https://lists.apache.org/thread/rzkdbo5ojff9grs2bowwl95n0fsb4zts> |
| 07/03/2023 - 07/10/2023 | He Lei | <https://lists.apache.org/thread/2kh8mq2wn4g0vzdn1czb7nj4t8l2hj9v> |
| 07/10/2023 - 07/16/2023 | Liu Shuai | <https://lists.apache.org/thread/z6jcyqsy31rf1r626kjx2d2sykwtvhqz> |
| 08/07/2023 - 08/13/2023 | Lei Li | <https://lists.apache.org/thread/g2tz50ymsvv3xb2dl3bjot1rfdp74rkj> |
| 08/21/2023 - 09/03/2023 | Cai Daojin | <https://lists.apache.org/thread/f63wnl45l1s3v61681m9tgfpkr6dxptx> |
| 09/18/2023 - 09/24/2023 | Liu Shuai | <https://lists.apache.org/thread/v4po2bwzn3fb7w7qbxfn8hgqzthyqb4b> |
| 09/25/2023 - 10/08/2023 | Xiguo Hu | <https://lists.apache.org/thread/lz3n9nt8xpp7kfb39zxp8m5cjl3dcpbt> |
| 10/16/2023 - 10/22/2023 | Lei Li | <https://lists.apache.org/thread/ylkbpgwp1qv7bs1z1dbxw31lk9o2vqod> |
| 10/23/2023 - 10/29/2023 | Wang Weibing | <https://lists.apache.org/thread/pq87hnf6tdhx0lrdnqpv3dk4tr8wyyrd> |
| 11/20/2023 - 11/26/2023 | Xiguo Hu | <https://lists.apache.org/thread/7hhg555ykcq2sfh0qm71vp9pn4tvb39s> |
| 12/04/2023 - 12/17/2023 | Lei Li | <https://lists.apache.org/thread/h6mphr4tnmwyfkw4r99ko3vk0wpwpzlp> |
| 12/18/2023 - 12/24/2023 | Wang Weibing | <https://lists.apache.org/thread/9vycfp3dldlogd17b5p5onbgbqm791nj> |
| 02/05/2024 - 02/18/2024 | Lei Li | <https://lists.apache.org/thread/jp19mj4qtjwhvq4r61nhkps253s82shy> |
| 02/19/2024 - 02/26/2024 | Wang Weibing | <https://lists.apache.org/thread/v4bynz0w3z14mylq6gk4kp3g08y71nds> |
| 03/04/2024 - 03/10/2024 | He Lei | <https://lists.apache.org/thread/4qzwspbzx5njd2759tmk8b8mdyx4ldqh> |
| 03/11/2024 - 03/17/2024 | Liu Shuai | <https://lists.apache.org/thread/6toz65lrntpj8wg66g87bsc52bbhowwk> |
| 03/25/2024 - 03/31/2024 | Lei Li | <https://lists.apache.org/thread/cyj36gds2dtyj4nm848r1mpnkqjp51qh> |
| 04/29/2024 - 05/05/2024 | Liu Shuai | <https://lists.apache.org/thread/b0htz9ykgb35z3pfpdvsf114p7ctkgbw> |
| 05/06/2024 - 05/012/2024 | Xiguo Hu | <https://lists.apache.org/thread/pgs35lpx36t0wo0jjrmodzkvxgqdj55o> |
| 05/13/2024 - 05/19/2024 | Yang Liming | <https://lists.apache.org/thread/9sjz8l0mdzqj136cl19bjvlwxr9ypgf0> |
| 05/19/2024 - 05/26/2024 | Zhu Jiashun | <https://lists.apache.org/thread/jz4x8v1ggvhgjrqhl2w549vjlxlhnqh7> |
| 05/27/2024 - 06/02/2024 | Lei Li | <https://lists.apache.org/thread/qmpp52389zgk9tmz75n04q94cfv615pr> |
| 06/03/2024 - 06/10/2024 | Wang Weibing | <https://lists.apache.org/thread/m82t378vjdwoczscp49b5vbrvqwftybb> |
| 06/10/2024 - 06/16/2024 | Cai Daojin | <https://lists.apache.org/thread/t8x0hp3oro1z65y519zpc8kq2hkcz1no> |
| 06/17/2024 - 06/23/2024 | He Lei | <https://lists.apache.org/thread/ddomd78h2f7nscs81o9bc24gbckxjk2o> |
| 06/24/2024 - 06/30/2024 | Liu Shuai | <https://lists.apache.org/thread/bmds2jpz93llqzpvyy5xopntbpodw8tw> |
| 07/01/2024 - 07/07/2024 | Xiguo Hu | <https://lists.apache.org/thread/k4r05sk8k0vks2ztsnpjz6pxgxxhy3jx> |
| 07/08/2024 - 07/14/2024 | Zhu Jiashun | <https://lists.apache.org/thread/tc0t9mcfqldss71wbmw2r2s7lbtzknbd> |
| 07/15/2024 - 07/21/2024 | Lei Li | <https://lists.apache.org/thread/7ox4vk94yqvcs0mghrromt5gl6q7z68j> |
| 07/22/2024 - 07/29/2024 | Wang Weibing | <https://lists.apache.org/thread/ms43wjgph8ygmlhmyxx5sq3xhxhwm31d> |
| 07/29/2024 - 08/04/2024 | Cai Daojin | <https://lists.apache.org/thread/ttlh0l097m3rfc7c38rqchhz7gzxd9xg> |
| 08/05/2024 - 08/11/2024 | He Lei | <https://lists.apache.org/thread/g6vmztfhyyj422c8c37tjbn2qq0wjh97> |
| 08/12/2024 - 08/18/2024 | Liu Shuai | <https://lists.apache.org/thread/sxpo7rqgw20coy0nf9k8bdpc88cmhypb> |
| 09/23/2024 - 10/07/2024 | Wang Weibing | <https://lists.apache.org/thread/n7vtlkcof2q9noy5t91w6ltonygh0h60> |
| 07/07/2025 - 07/13/2025 | Liu Shuai | <https://lists.apache.org/thread/mvr9kn7886z26mj33t18jr2mjh6swjmh> |

Last modified July 14, 2025: [Update index.md (39c893c70)](https://github.com/apache/brpc-website/commit/39c893c70effb9022e6ca5443590bfe49a09dd03)

---

<a id="community-security-cve-2023-31039-bugfix"></a>

<!-- source_url: https://brpc.apache.org/docs/community/security/cve-2023-31039-bugfix/ -->

<!-- page_index: 49 -->

# CVE-2023-31039

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/security/CVE-2023-31039-BugFix/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=CVE-2023-31039)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# CVE-2023-31039

CVE-2023-31039: ServerOptions.pid\_file may cause arbitrary code execution

**Severity**: Important

**Affected Versions**: Apache bRPC 0.9.0 before 1.5.0

**Description**:
Security vulnerability in Apache bRPC <1.5.0 on all platforms allows attackers to execute arbitrary code via ServerOptions::pid\_file.
An attacker that can influence the ServerOptions pid\_file parameter with which the bRPC server is started can execute arbitrary code with the permissions of the bRPC process.

**Solution**:

- upgrade to bRPC >= 1.5.0, download link: <https://dist.apache.org/repos/dist/release/brpc/1.5.0/>
- If you are using an old version of bRPC and hard to upgrade, you can apply this patch: <https://github.com/apache/brpc/pull/2218>

**Required Configurations**:

- set brpc::ServerOptions::pid\_file from user input

**Work Arounds**:

- Apply this patch: <https://github.com/apache/brpc/pull/2218>

**References**:

1. [https://brpc.apache.org](https://brpc.apache.org/)
2. <https://www.cve.org/CVERecord?id=CVE-2023-31039>

Last modified May 16, 2023: [add security bug fix pages (#148) (a29da9f83)](https://github.com/apache/brpc-website/commit/a29da9f83009053aa299a57936166bef0d01a9a2)

---

<a id="community-security"></a>

<!-- source_url: https://brpc.apache.org/docs/community/security/ -->

<!-- page_index: 50 -->

# Security

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/community/security/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Security)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Security

About security

The Apache Software Foundation takes a rigorous stance on eliminating security issues in its software projects. Likewise, Apache bRPC is also vigilant and takes security issues related to its features and functionality into the highest consideration.

If you have any concerns regarding bRPC’s security, or you discover a vulnerability or potential threat, please don’t hesitate to get in touch with the [Apache Security Team](http://www.apache.org/security/) by dropping an email at [security@apache.org](mailto:security@apache.org).

Please specify the project name as “bRPC” in the email, and provide a description of the relevant problem or potential threat. You are also urged to recommend how to reproduce and replicate the issue.

The Apache Security Team and the bRPC community will get back to you after assessing and analyzing the findings.

**Please note** that the security issue should be reported on the security email first, before disclosing it on any public domain.

---

##### [CVE-2023-31039](#community-security-cve-2023-31039-bugfix)

CVE-2023-31039: ServerOptions.pid\_file may cause arbitrary code execution

Last modified May 16, 2023: [add security bug fix pages (#148) (a29da9f83)](https://github.com/apache/brpc-website/commit/a29da9f83009053aa299a57936166bef0d01a9a2)

---

<a id="downloadbrpc"></a>

<!-- source_url: https://brpc.apache.org/docs/downloadbrpc/ -->

<!-- page_index: 51 -->

# Download

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/DownloadBRPC/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Download)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Apache bRPC Downloads](#downloadbrpc--apache-brpc-downloads)

# Download

Download bRPC Release Version.

<a id="downloadbrpc--apache-brpc-downloads"></a>

## Apache bRPC Downloads

Apache bRPC is released as a source artifact.
We are pleased to announce our 1.16.0 release as below.

<a id="downloadbrpc--all-release"></a>

### All Release

| **Name** | **Archive** | **SHA-512** | **Signature** |
| --- | --- | --- | --- |
| Apache bRPC 1.16.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.16.0/apache-brpc-1.16.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.16.0/apache-brpc-1.16.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.16.0/apache-brpc-1.16.0-src.tar.gz.asc) |
| Apache bRPC 1.15.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.15.0/apache-brpc-1.15.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.15.0/apache-brpc-1.15.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.15.0/apache-brpc-1.15.0-src.tar.gz.asc) |
| Apache bRPC 1.14.1 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.14.1/apache-brpc-1.14.1-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.14.1/apache-brpc-1.14.1-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.14.1/apache-brpc-1.14.1-src.tar.gz.asc) |
| Apache bRPC 1.13.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.13.0/apache-brpc-1.13.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.13.0/apache-brpc-1.13.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.13.0/apache-brpc-1.13.0-src.tar.gz.asc) |
| Apache bRPC 1.12.1 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.12.1/apache-brpc-1.12.1-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.12.1/apache-brpc-1.12.1-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.12.1/apache-brpc-1.12.1-src.tar.gz.asc) |
| Apache bRPC 1.12.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.12.0/apache-brpc-1.12.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.12.0/apache-brpc-1.12.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.12.0/apache-brpc-1.12.0-src.tar.gz.asc) |
| Apache bRPC 1.11.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.11.0/apache-brpc-1.11.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.11.0/apache-brpc-1.11.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.11.0/apache-brpc-1.11.0-src.tar.gz.asc) |
| Apache bRPC 1.10.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.10.0/apache-brpc-1.10.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.10.0/apache-brpc-1.10.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.10.0/apache-brpc-1.10.0-src.tar.gz.asc) |
| Apache bRPC 1.9.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.9.0/apache-brpc-1.9.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.9.0/apache-brpc-1.9.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.9.0/apache-brpc-1.9.0-src.tar.gz.asc) |
| Apache bRPC 1.8.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.8.0/apache-brpc-1.8.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.8.0/apache-brpc-1.8.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.8.0/apache-brpc-1.8.0-src.tar.gz.asc) |
| Apache bRPC 1.7.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.7.0/apache-brpc-1.7.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.7.0/apache-brpc-1.7.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.7.0/apache-brpc-1.7.0-src.tar.gz.asc) |
| Apache bRPC 1.6.1 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.6.1/apache-brpc-1.6.1-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.6.1/apache-brpc-1.6.1-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.6.1/apache-brpc-1.6.1-src.tar.gz.asc) |
| Apache bRPC 1.6.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.6.0/apache-brpc-1.6.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.6.0/apache-brpc-1.6.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.6.0/apache-brpc-1.6.0-src.tar.gz.asc) |
| Apache bRPC 1.5.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.5.0/apache-brpc-1.5.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.5.0/apache-brpc-1.5.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.5.0/apache-brpc-1.5.0-src.tar.gz.asc) |
| Apache bRPC 1.4.0 (tar.gz) | [tar.gz](https://dlcdn.apache.org/brpc/1.4.0/apache-brpc-1.4.0-src.tar.gz) | [SHA-512](https://downloads.apache.org/brpc/1.4.0/apache-brpc-1.4.0-src.tar.gz.sha512) | [ASC](https://downloads.apache.org/brpc/1.4.0/apache-brpc-1.4.0-src.tar.gz.asc) |

Choose a source distribution and [verify](https://www.apache.org/dyn/closer.cgi#verify)
using the corresponding *pgp* signature (using the committer file in
[KEYS](https://downloads.apache.org/brpc/KEYS)).
If you cannot do that, the *md5* hash file may be used to check that the
download has completed OK.

For fast downloads, current source distributions are hosted on mirror servers;
older source distributions are in the
[archive](https://archive.apache.org/dist/incubator/brpc/).
If a download from a mirror fails, retry, and the second download will likely
succeed.

For security, hash and signature files are always hosted at
[Apache](https://www.apache.org).

Last modified January 25, 2026: [release brpc 1.16.0 (#178) (a7fa723b6)](https://github.com/apache/brpc-website/commit/a7fa723b65baa51a59a47585e3302d2ac9f4fe1f)

---

<a id="faq"></a>

<!-- source_url: https://brpc.apache.org/docs/faq/ -->

<!-- page_index: 52 -->

# FAQ

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/faq/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=FAQ)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# FAQ

bRPC Issues.

See <https://github.com/apache/brpc/issues>

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="getting_started"></a>

<!-- source_url: https://brpc.apache.org/docs/getting_started/ -->

<!-- page_index: 53 -->

# Getting started

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/getting_started/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Getting%20started)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [BUILD](#getting_started--build)
- [Supported Environment](#getting_started--supported-environment)
  - [Ubuntu/LinuxMint/WSL](#getting_started--ubuntulinuxmintwsl)
  - [Fedora/CentOS](#getting_started--fedoracentos)
  - [Linux with self-built deps](#getting_started--linux-with-self-built-deps)
  - [MacOS](#getting_started--macos)
  - [Docker](#getting_started--docker)
- [Supported deps](#getting_started--supported-deps)
- [Track instances](#getting_started--track-instances)

# Getting started

Read getting started for building steps and play with [examples](https://github.com/apache/brpc/tree/master/example).

<a id="getting_started--build"></a>

## BUILD

brpc prefers static linkages of deps, so that they don’t have to be installed on every machine running the app.

brpc depends on following packages:

<a id="getting_started--supported-environment"></a>

## Supported Environment

- [Ubuntu/LinuxMint/WSL](#getting_started--ubuntulinuxmintwsl)
- [Fedora/CentOS](#getting_started--fedoracentos)
- [Linux with self-built deps](#getting_started--linux-with-self-built-deps)
- [MacOS](#getting_started--macos)
- [Docker](#getting_started--docker)

<a id="getting_started--ubuntulinuxmintwsl"></a>

### Ubuntu/LinuxMint/WSL

<a id="getting_started--prepare-deps"></a>

#### Prepare deps

Install dependencies:

```shell
sudo apt-get install -y git g++ make libssl-dev libgflags-dev libprotobuf-dev libprotoc-dev protobuf-compiler libleveldb-dev
```

If you need to statically link leveldb:

```shell
sudo apt-get install -y libsnappy-dev
```

If you need to enable cpu/heap profilers in examples:

```shell
sudo apt-get install -y libgoogle-perftools-dev
```

If you need to run tests, install and compile libgtest-dev (which is not compiled yet):

```shell
sudo apt-get install -y cmake libgtest-dev && cd /usr/src/gtest && sudo cmake . && sudo make && sudo mv lib/libgtest* /usr/lib/ && cd -
```

The directory of gtest source code may be changed, try `/usr/src/googletest/googletest` if `/usr/src/gtest` is not there.

<a id="getting_started--compile-brpc-with-config_brpcsh"></a>

#### Compile brpc with config\_brpc.sh

git clone brpc, cd into the repo and run

```shell
$ sh config_brpc.sh --headers=/usr/include --libs=/usr/lib
$ make
```

To change compiler to clang, add `--cxx=clang++ --cc=clang`.

To not link debugging symbols, add `--nodebugsymbols` and compiled binaries will be much smaller.

To use brpc with glog, add `--with-glog`.

To enable [thrift support](#server-serve-thrift), install thrift first and add `--with-thrift`.

**Run example**

```shell
$ cd example/echo_c++
$ make
$ ./echo_server &
$ ./echo_client
```

Examples link brpc statically, if you need to link the shared version, `make clean` and `LINK_SO=1 make`

**Run tests**

```shell
$ cd test
$ make
$ sh run_tests.sh
```

<a id="getting_started--compile-brpc-with-cmake"></a>

#### Compile brpc with cmake

```shell
cmake -B build && cmake --build build -j6
```

To help VSCode or Emacs(LSP) to understand code correctly, add `-DCMAKE_EXPORT_COMPILE_COMMANDS=ON` to generate `compile_commands.json`

To change compiler to clang, overwrite environment variable `CC` and `CXX` to `clang` and `clang++` respectively.

To not link debugging symbols, remove `build/CMakeCache.txt` and cmake with `-DWITH_DEBUG_SYMBOLS=OFF`

To use brpc with glog, cmake with `-DWITH_GLOG=ON`.

To enable [thrift support](#server-serve-thrift), install thrift first and cmake with `-DWITH_THRIFT=ON`.

**Run example with cmake**

```shell
$ cd example/echo_c++
$ cmake -B build && cmake --build build -j4
$ ./echo_server &
$ ./echo_client
```

Examples link brpc statically, if you need to link the shared version, remove `CMakeCache.txt` and cmake with `-DLINK_SO=ON`

**Run tests**

```shell
$ mkdir build && cd build && cmake -DBUILD_UNIT_TESTS=ON .. && make && make test
```

<a id="getting_started--fedoracentos"></a>

### Fedora/CentOS

<a id="getting_started--prepare-deps-1"></a>

#### Prepare deps

CentOS needs to install EPEL generally otherwise many packages are not available by default.

```shell
sudo yum install epel-release
```

Install dependencies:

```shell
sudo yum install git gcc-c++ make openssl-devel gflags-devel protobuf-devel protobuf-compiler leveldb-devel
```

If you need to enable cpu/heap profilers in examples:

```shell
sudo yum install gperftools-devel
```

If you need to run tests, install and compile gtest-devel (which is not compiled yet):

```shell
sudo yum install gtest-devel
```

<a id="getting_started--compile-brpc-with-config_brpcsh-1"></a>

#### Compile brpc with config\_brpc.sh

git clone brpc, cd into the repo and run

```shell
$ sh config_brpc.sh --headers=/usr/include --libs=/usr/lib64
$ make
```

To change compiler to clang, add `--cxx=clang++ --cc=clang`.

To not link debugging symbols, add `--nodebugsymbols` and compiled binaries will be much smaller.

To use brpc with glog, add `--with-glog`.

To enable [thrift support](#server-serve-thrift), install thrift first and add `--with-thrift`.

**Run example**

```shell
$ cd example/echo_c++
$ make
$ ./echo_server &
$ ./echo_client
```

Examples link brpc statically, if you need to link the shared version, `make clean` and `LINK_SO=1 make`

**Run tests**

```shell
$ cd test
$ make
$ sh run_tests.sh
```

<a id="getting_started--compile-brpc-with-cmake-1"></a>

#### Compile brpc with cmake

Same with [here](#getting_started--compile-brpc-with-cmake)

<a id="getting_started--linux-with-self-built-deps"></a>

### Linux with self-built deps

<a id="getting_started--prepare-deps-2"></a>

#### Prepare deps

brpc builds itself to both static and shared libs by default, so it needs static and shared libs of deps to be built as well.

Take [gflags](https://github.com/gflags/gflags) as example, which does not build shared lib by default, you need to pass options to `cmake` to change the behavior:

```shell
$ cmake . -DBUILD_SHARED_LIBS=1 -DBUILD_STATIC_LIBS=1
$ make
```

<a id="getting_started--compile-brpc"></a>

#### Compile brpc

Keep on with the gflags example, let `../gflags_dev` be where gflags is cloned.

git clone brpc. cd into the repo and run

```shell
$ sh config_brpc.sh --headers="../gflags_dev /usr/include" --libs="../gflags_dev /usr/lib64"
$ make
```

Here we pass multiple paths to `--headers` and `--libs` to make the script search for multiple places. You can also group all deps and brpc into one directory, then pass the directory to –headers/–libs which actually search all subdirectories recursively and will find necessary files.

To change compiler to clang, add `--cxx=clang++ --cc=clang`.

To not link debugging symbols, add `--nodebugsymbols` and compiled binaries will be much smaller.

To use brpc with glog, add `--with-glog`.

To enable [thrift support](#server-serve-thrift), install thrift first and add `--with-thrift`.

```shell
$ ls my_dev gflags_dev protobuf_dev leveldb_dev brpc_dev
$ cd brpc_dev
$ sh config_brpc.sh --headers=.. --libs=..
$ make
```

<a id="getting_started--compile-brpc-with-cmake-2"></a>

#### Compile brpc with cmake

Same with [here](#getting_started--compile-brpc-with-cmake)

<a id="getting_started--macos"></a>

### MacOS

Note: With same environment, the performance of the MacOS version is worse than the Linux version. If your service is performance-critical, do not use MacOS as your production environment.

<a id="getting_started--apple-silicon"></a>

#### Apple Silicon

The code at master HEAD already supports M1 series chips. M2 series are not tested yet. Please feel free to report remaining warnings/errors to us by issues.

<a id="getting_started--prepare-deps-3"></a>

#### Prepare deps

Install dependencies:

```shell
brew install openssl git gnu-getopt coreutils gflags protobuf leveldb
```

If you need to enable cpu/heap profilers in examples:

```shell
brew install gperftools
```

If you need to run tests, googletest is required. Run `brew install googletest` first to see if it works. If not (old homebrew does not have googletest), you can download and compile googletest by your own:

```shell
git clone https://github.com/google/googletest -b release-1.10.0 && cd googletest/googletest && mkdir build && cd build && cmake -DCMAKE_CXX_FLAGS="-std=c++11" .. && make
```

After the compilation, copy `include/` and `lib/` into `/usr/local/include` and `/usr/local/lib` respectively to expose gtest to all apps

<a id="getting_started--openssl"></a>

#### OpenSSL

openssl installed in Monterey may not be found at `/usr/local/opt/openssl`, instead it’s probably put under `/opt/homebrew/Cellar`. If the compiler cannot find openssl：

- Run `brew link openssl --force` first and check if `/user/local/opt/openssl` appears.
- If above command does not work, consider making a soft link using `sudo ln -s /opt/homebrew/Cellar/openssl@3/3.0.3 /usr/local/opt/openssl`. Note that the installed openssl in above command may be put in different places in different environments, which could be revealed by running `brew info openssl`.

<a id="getting_started--compile-brpc-with-config_brpcsh-2"></a>

#### Compile brpc with config\_brpc.sh

git clone brpc, cd into the repo and run

```shell
$ sh config_brpc.sh --headers=/usr/local/include --libs=/usr/local/lib --cc=clang --cxx=clang++
$ make
```

The homebrew in Monterey may install software at different directories from before. If path related errors are reported, try setting headers/libs like below:

```shell
$ sh config_brpc.sh --headers=/opt/homebrew/include --libs=/opt/homebrew/lib --cc=clang --cxx=clang++
$ make
```

To not link debugging symbols, add `--nodebugsymbols` and compiled binaries will be much smaller.

To use brpc with glog, add `--with-glog`.

To enable [thrift support](#server-serve-thrift), install thrift first and add `--with-thrift`.

**Run example**

```shell
$ cd example/echo_c++
$ make
$ ./echo_server &
$ ./echo_client
```

Examples link brpc statically, if you need to link the shared version, `make clean` and `LINK_SO=1 make`

**Run tests**

```shell
$ cd test
$ make
$ sh run_tests.sh
```

<a id="getting_started--compile-brpc-with-cmake-3"></a>

#### Compile brpc with cmake

Same with [here](#getting_started--compile-brpc-with-cmake)

<a id="getting_started--docker"></a>

### Docker

Compile brpc with docker:

```shell
$ mkdir -p ~/brpc
$ cd ~/brpc
$ git clone https://github.com/apache/brpc.git
$ cd brpc
$ docker build -t brpc:master .
$ docker images
$ docker run -it brpc:master /bin/bash
```

<a id="getting_started--supported-deps"></a>

## Supported deps

<a id="getting_started--gcc-48-112"></a>

#### GCC: 4.8-11.2

c++11 is turned on by default to remove dependencies on boost (atomic).

The over-aligned issues in GCC7 is suppressed temporarily now.

Using other versions of gcc may generate warnings, contact us to fix.

Adding `-D__const__=` to cxxflags in your makefiles is a must to avoid [errno issue in gcc4+](#bthread-thread-local).

<a id="getting_started--clang-35-40"></a>

#### Clang: 3.5-4.0

no known issues.

<a id="getting_started--glibc-212-225"></a>

#### glibc: 2.12-2.25

no known issues.

<a id="getting_started--protobuf-24"></a>

#### protobuf: 2.4+

Be compatible with pb 3.x and pb 2.x with the same file:
Don’t use new types in proto3 and start the proto file with `syntax="proto2";`
[tools/add\_syntax\_equal\_proto2\_to\_all.sh](https://github.com/brpc/brpc/blob/master/tools/add_syntax_equal_proto2_to_all.sh) can add `syntax="proto2"` to all proto files without it.

Arena in pb 3.x is not supported yet.

<a id="getting_started--gflags-20-221"></a>

#### gflags: 2.0-2.2.1

no known issues.

<a id="getting_started--openssl-097-11"></a>

#### openssl: 0.97-1.1

required by https.

<a id="getting_started--tcmalloc-17-25"></a>

#### tcmalloc: 1.7-2.5

brpc does **not** link [tcmalloc](http://goog-perftools.sourceforge.net/doc/tcmalloc.html) by default. Users link tcmalloc on-demand.

Comparing to ptmalloc embedded in glibc, tcmalloc often improves performance. However different versions of tcmalloc may behave really differently. For example, tcmalloc 2.1 may make multi-threaded examples in brpc perform significantly worse(due to a spinlock in tcmalloc) than the one using tcmalloc 1.7 and 2.5. Even different minor versions may differ. When you program behave unexpectedly, remove tcmalloc or try another version.

Code compiled with gcc 4.8.2 and linked to a tcmalloc compiled with earlier GCC may crash or deadlock before main(), E.g:

![img](assets/images/tcmalloc-stuck_d7dba15b0cdec169.png)

When you meet the issue, compile tcmalloc with the same GCC.

Another common issue with tcmalloc is that it does not return memory to system as early as ptmalloc. So when there’s an invalid memory access, the program may not crash directly, instead it crashes at a unrelated place, or even not crash. When you program has weird memory issues, try removing tcmalloc.

If you want to use [cpu profiler](https://brpc.apache.org/docs/builtin-services/cpu_profiler) or [heap profiler](https://brpc.apache.org/docs/builtin-services/heap_profiler), do link `libtcmalloc_and_profiler.a`. These two profilers are based on tcmalloc. [contention profiler](https://brpc.apache.org/docs/builtin-services/contention_profiler) does not require tcmalloc.

When you remove tcmalloc, not only remove the linkage with tcmalloc but also the macro `-DBRPC_ENABLE_CPU_PROFILER`.

<a id="getting_started--glog-33"></a>

#### glog: 3.3+

brpc implements a default [logging utility](https://brpc.apache.org/src/butil/logging.h) which conflicts with glog. To replace this with glog, add `--with-glog` to config\_brpc.sh or add `-DWITH_GLOG=ON` to cmake.

<a id="getting_started--valgrind-38"></a>

#### valgrind: 3.8+

brpc detects valgrind automatically (and registers stacks of bthread). Older valgrind(say 3.2) is not supported.

<a id="getting_started--thrift-093-0110"></a>

#### thrift: 0.9.3-0.11.0

no known issues.

<a id="getting_started--track-instances"></a>

## Track instances

We provide a program to help you to track and monitor all brpc instances. Just run [trackme\_server](https://github.com/brpc/brpc/tree/master/tools/trackme_server/) somewhere and launch need-to-be-tracked instances with -trackme\_server=SERVER. The trackme\_server will receive pings from instances periodically and print logs when it does. You can aggregate instance addresses from the log and call builtin services of the instances for further information.

Last modified July 13, 2023: [docs: fix doc lint (#152) (d916d9252)](https://github.com/apache/brpc-website/commit/d916d9252943f6a2ba9839fe8a59783b92881ea5)

---

<a id="overview"></a>

<!-- source_url: https://brpc.apache.org/docs/overview/ -->

<!-- page_index: 54 -->

# bRPC overview

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/overview/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bRPC%20overview)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- - [More friendly API](#overview--more-friendly-api)
  - [Make services more reliable](#overview--make-services-more-reliable)
  - [Better latency and throughput](#overview--better-latency-and-throughput)

# bRPC overview

The basic description of bRPC.

<a id="overview--what-is-rpc"></a>

# What is RPC?

Most machines on internet communicate with each other via [TCP/IP](https://en.wikipedia.org/wiki/Internet_protocol_suite). However, TCP/IP only guarantees reliable data transmissions. We need to abstract more to build services:

- What is the format of data transmission? Different machines and networks may have different byte-orders, directly sending in-memory data is not suitable. Fields in the data are added, modified or removed gradually, how do newer services talk with older services?
- Can TCP connection be reused for multiple requests to reduce overhead? Can multiple requests be sent through one TCP connection simultaneously?
- How to talk with a cluster with many machines?
- What should I do when the connection is broken? What if the server does not respond?
- …

[RPC](https://en.wikipedia.org/wiki/Remote_procedure_call) addresses the above issues by abstracting network communications as “clients accessing functions on servers”: client sends a request to server, wait until server receives -> processes -> responds to the request, then do actions according to the result.
![rpc.png](assets/images/rpc_fe50a769718ed732.png)

Let’s see how the issues are solved.

- RPC needs serialization which is done by [protobuf](https://github.com/google/protobuf) pretty well. Users fill requests in format of protobuf::Message, do RPC, and fetch results from responses in protobuf::Message. protobuf has good forward and backward compatibility for users to change fields and build services incrementally. For http services, [json](http://www.json.org/) is used for serialization extensively.
- Establishment and re-using of connections is transparent to users, but users can make choices like [different connection types](#client-basics--connection-type): short, pooled, single.
- Machines are discovered by a Naming Service, which can be implemented by [DNS](https://en.wikipedia.org/wiki/Domain_Name_System), [ZooKeeper](https://zookeeper.apache.org/) or [etcd](https://github.com/coreos/etcd). Inside Baidu, we use BNS (Baidu Naming Service). brpc provides [“list://” and “file://”](#client-basics--naming-service) as well. Users specify load balancing algorithms to choose one machine for each request from all machines, including: round-robin, randomized, [consistent-hashing](#rpc-in-depth-consistent-hashing)(murmurhash3 or md5) and [locality-aware](#rpc-in-depth-locality-aware).
- RPC retries when the connection is broken. When server does not respond within the given time, client fails with a timeout error.

<a id="overview--where-can-i-use-rpc"></a>

# Where can I use RPC?

Almost all network communications.

RPC can’t do everything surely, otherwise we don’t need the layer of TCP/IP. But in most network communications, RPC meets requirements and isolates the underlying details.

Common doubts on RPC:

- My data is binary and large, using protobuf will be slow. First, this is possibly a wrong feeling and you will have to test it and prove it with [profilers](#builtin-services-cpu_profiler). Second, many protocols support carrying binary data along with protobuf requests and bypass the serialization.
- I’m sending streaming data which can’t be processed by RPC. Actually many protocols in RPC can handle streaming data, including [ProgressiveReader in http](#client-access-httph2--progressively-download), streams in h2, [streaming rpc](#client-streaming-rpc), and RTMP which is a specialized streaming protocol.
- I don’t need replies. With some inductions, we know that in your scenario requests can be dropped at any stage because the client is always unaware of the situation. Are you really sure this is acceptable? Even if you don’t need the reply, we recommend sending back small-sized replies, which are unlikely to be performance bottlenecks and will probably provide valuable clues when debugging complex bugs.

<a id="overview--what-is-brpcimagesdocslogopng"></a>

# What is brpc?

brpc is an Industrial-grade RPC framework using C++ Language, which is often used in high performance system such as Search, Storage, Machine learning, Advertisement, Recommendation etc.

You can use it to:

<a id="overview--advantages-of-brpc"></a>

# Advantages of bRPC

<a id="overview--more-friendly-api"></a>

### More friendly API

Only 3 (major) user headers: [Server](https://github.com/brpc/brpc/blob/master/src/brpc/server.h), [Channel](https://github.com/brpc/brpc/blob/master/src/brpc/channel.h), [Controller](https://github.com/brpc/brpc/blob/master/src/brpc/controller.h), corresponding to server-side, client-side and parameter-set respectively. You don’t have to worry about “How to initialize XXXManager”, “How to layer all these components together”, “What’s the relationship between XXXController and XXXContext”. All you need to do is simple:

- Build service? include [brpc/server.h](https://github.com/brpc/brpc/blob/master/src/brpc/server.h) and follow the comments or [examples](https://github.com/brpc/brpc/blob/master/example/echo_c++/server.cpp).
- Access service? include [brpc/channel.h](https://github.com/brpc/brpc/blob/master/src/brpc/channel.h) and follow the comments or [examples](https://github.com/brpc/brpc/blob/master/example/echo_c++/client.cpp).
- Tweak parameters? Checkout [brpc/controller.h](https://github.com/brpc/brpc/blob/master/src/brpc/controller.h). Note that the class is shared by server and channel. Methods are separated into 3 parts: client-side, server-side and both-side.

We tried to make simple things simple. Take naming service as an example. In older RPC implementations you may need to copy a pile of obscure code to make it work, however, in brpc accessing BNS is expressed as `Init("bns://node-name", ...)`, DNS is `Init("http://domain-name", ...)` and local machine list is `Init("file:///home/work/server.list", ...)`. Without any explanation, you know what it means.

<a id="overview--make-services-more-reliable"></a>

### Make services more reliable

brpc is extensively used in Baidu:

- map-reduce service & table storages
- high-performance computing & model training
- all sorts of indexing & ranking servers
- ….

It’s been proven.

brpc pays special attentions to development and maintenance efficency, you can [view internal status of servers](#builtin-services-buildin_services) in web browser or with curl, analyze [cpu hotspots](#builtin-services-cpu_profiler), [heap allocations](#builtin-services-heap_profiler) and [lock contentions](#builtin-services-contention_profiler) of online services, measure stats by [bvar](#bvar-bvar) which is viewable in [/vars](#builtin-services-vars).

<a id="overview--better-latency-and-throughput"></a>

### Better latency and throughput

Although almost all RPC implementations claim that they’re “high-performant”, the numbers are probably just numbers. Being really high-performant in different scenarios is difficult. To unify communication infra inside Baidu, brpc goes much deeper at performance than other implementations.

- Reading and parsing requests from different clients is fully parallelized and users don’t need to distinguish between “IO-threads” and “Processing-threads”. Other implementations probably have “IO-threads” and “Processing-threads” and hash file descriptors(fd) into IO-threads. When a IO-thread handles one of its fds, other fds in the thread can’t be handled. If a message is large, other fds are significantly delayed. Although different IO-threads run in parallel, you won’t have many IO-threads since they don’t have too much to do generally except reading/parsing from fds. If you have 10 IO-threads, one fd may affect 10% of all fds, which is unacceptable to industrial online services (requiring 99.99% availability). The problem will be worse when fds are distributed unevenly accross IO-threads (unfortunately common), or the service is multi-tenancy (common in cloud services). In brpc, reading from different fds is parallelized and even processing different messages from one fd is parallelized as well. Parsing a large message does not block other messages from the same fd, not to mention other fds. More details can be found [here](#rpc-in-depth-io--receiving-messages).
- Writing into one fd and multiple fds is highly concurrent. When multiple threads write into the same fd (common for multiplexed connections), the first thread directly writes in-place and other threads submit their write requests in [wait-free](https://en.wikipedia.org/wiki/Non-blocking_algorithm#Wait-freedom) manner. One fd can be written into 5,000,000 16-byte messages per second by a couple of highly-contended threads. More details can be found [here](#rpc-in-depth-io--sending-messages).
- Minimal locks. High-QPS services can utilize all CPU power on the machine. For example, [creating bthreads](#rpc-in-depth-memory-management) for processing requests, [setting up timeout](#rpc-in-depth-timer-keeping), [finding RPC contexts](#rpc-in-depth-bthread_id) according to response, [recording performance counters](#bvar-bvar) are all highly concurrent. Users see very few contentions (via [contention profiler](#builtin-services-contention_profiler)) caused by RPC framework even if the service runs at 500,000+ QPS.
- Server adjusts thread number according to load. Traditional implementations set number of threads according to latency to avoid limiting the throughput. brpc creates a new [bthread](#bthread-bthread) for each request and ends the bthread when the request is done, which automatically adjusts thread number according to load.

Check [benchmark](#benchmark) for a comparison between brpc and other implementations.

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="rpc-in-depth-atomic-instructions"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/atomic-instructions/ -->

<!-- page_index: 55 -->

# Atomic instructions

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Atomic%20instructions/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Atomic%20instructions)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Atomic instructions

Learn about bRPC atomic instructions.

We know that locks are extensively used in multi-threaded programming to avoid [race conditions](http://en.wikipedia.org/wiki/Race_condition) when modifying shared data. When the lock becomes a bottleneck, we try to walk around it by using atomic instructions. But it is difficult to write correct code with atomic instructions in generally and it is even hard to understand race conditions, [ABA problems](https://en.wikipedia.org/wiki/ABA_problem) and [memory fences](https://en.wikipedia.org/wiki/Memory_barrier). This article tries to introduce basics on atomic instructions(under [SMP](http://en.wikipedia.org/wiki/Symmetric_multiprocessing)). Since [Atomic instructions](http://en.cppreference.com/w/cpp/atomic/atomic) are formally introduced in C++11, we use the APIs directly.

As the name implies, atomic instructions cannot be divided into more sub-instructions. For example, `x.fetch(n)` atomically adds n to x, any internal state is not observable **to software**. Common atomic instructions are listed below:

| Atomic Instructions(type of x is std::atomic<int>) | Descriptions |
| --- | --- |
| x.load() | return the value of x. |
| x.store(n) | store n to x and return nothing. |
| x.exchange(n) | set x to n and return the value just before the modification |
| x.compare\_exchange\_strong(expected\_ref, desired) | If x is equal to expected\_ref, set x to desired and return true. Otherwise write current x to expected\_ref and return false. |
| x.compare\_exchange\_weak(expected\_ref, desired) | may have [spurious wakeup](http://en.wikipedia.org/wiki/Spurious_wakeup) comparing to compare\_exchange\_strong |
| x.fetch\_add(n), x.fetch\_sub(n) | do x += n, x-= n atomically. Return the value just before the modification. |

You can already use these instructions to count something atomically, such as counting number of operations from multiple threads. However two problems may arise:

- The operation is not as fast as expected.
- Even if multi-threaded accesses to some resources are controlled by a few atomic instructions that seem to be correct, the program still has great chance to crash.

<a id="rpc-in-depth-atomic-instructions--cacheline"></a>

# Cacheline

An atomic instruction is fast when there’s no contentions or it’s accessed only by one thread. “Contentions” happen when multiple threads access the same [cacheline](https://en.wikipedia.org/wiki/CPU_cache#Cache_entries). Modern CPU extensively use caches and divide caches into multiple levels to get high performance with a low price. The Intel E5-2620 widely used in Baidu has 32K L1 dcache and icache, 256K L2 cache and 15M L3 cache. L1 and L2 cache is owned by each core, while L3 cache is shared by all cores. Although it is very fast for one core to write data into its own L1 cache(4 cycles, ~2ns), make the data in L1 cache seen by other cores is not, because cachelines touched by the data need to be synchronized to other cores. This process is atomic and transparent to software and no instructions can be interleaved between. Applications have to wait for the completion of [cache coherence](https://en.wikipedia.org/wiki/Cache_coherence), which takes much longer time than writing local cache. It involves a complicated hardware algorithm and makes atomic instructions slow under high contentions. A single fetch\_add may take more than 700ns in E5-2620 when a few threads are highly contented on the instruction. Accesses to the memory frequently shared and modified by multiple threads are not fast generally. For example, even if a critical section looks small, the spinlock protecting it may still not perform well. The cause is that the instructions used in spinlock such as exchange, fetch\_add etc, need to wait for latest cachelines. It’s not surprising to see that one or two instructions take several microseconds.

In order to improve performance, we need to avoid frequently synchronizing cachelines, which not only affects performance of the atomic instruction itself, but also overall performance of the program. The most effective solution is straightforward: **avoid sharing as much as possible**.

A related programming trap is false sharing: Accesses to infrequently updated or even read-only variables are significantly slowed down because other variables in the same cacheline are frequently updated. Variables used in multi-threaded environment should be grouped by accessing frequencies or patterns, variables that are modified by that other threads frequently should be put into separated cachelines. To align a variable or struct by cacheline, `include <butil/macros.h>` and tag it with macro `BAIDU_CACHELINE_ALIGNMENT`, grep source code of brpc for examples.

<a id="rpc-in-depth-atomic-instructions--memory-fence"></a>

# Memory fence

Just atomic counting cannot synchronize accesses to resources, simple structures like [spinlock](https://en.wikipedia.org/wiki/Spinlock) or [reference counting](https://en.wikipedia.org/wiki/Reference_counting) that seem correct may crash as well. The key is **instruction reordering**, which may change the order of read/write and cause instructions behind to be reordered to front if there are no dependencies. [Compiler](http://preshing.com/20120625/memory-ordering-at-compile-time/) and [CPU](https://en.wikipedia.org/wiki/Out-of-order_execution) both may reorder.

The motivation is natural: CPU wants to fill each cycle with instructions and execute as many as possible instructions within given time. As said in above section, an instruction for loading memory may cost hundreds of nanoseconds due to cacheline synchronization. A efficient solution for synchronizing multiple cachelines is to move them simultaneously rather than one-by-one. Thus modifications to multiple variables by a thread may be visible to another thread in a different order. On the other hand, different threads need different data, synchronizing on-demand is reasonable and may also change order between cachelines.

For example: the first variable plays the role of switch, controlling accesses to following variables. When these variables are synchronized to other CPU cores, new values may be visible in a different order, and the first variable may not be the first updated, which causes other threads to think that the following variables are still valid, which are actually not, causing undefined behavior. Check code snippet below:

```c++
// Thread 1
// ready was initialized to false
p.init();
ready = true;
```

```c++
// Thread2
if (ready) {
    p.bar();
}
```

From a human perspective, the code is correct because thread2 only accesses `p` when `ready` is true which means p is initialized according to the logic in thread1. But the code may not run as expected on multi-core machines:

- `ready = true` in thread1 may be reordered before `p.init()` by compiler or CPU, making thread2 see uninitialized `p` when `ready` is true. The same reordering may happen in thread2 as well. Some instructions in `p.bar()` may be reordered before checking `ready`.
- Even if above reorderings do not happen, cachelines of `ready` and `p` may be synchronized independently to the CPU core that thread2 runs, making thread2 see unitialized `p` when `ready` is true.

Note: On x86/x64, `load` has acquire semantics and `store` has release semantics by default, the code above may run correctly provided that reordering by compiler is turned off.

With this simple example, you may get a glimpse of the complexity of atomic instructions. In order to solve the reordering issue, CPU and compiler offer [memory fences](http://en.wikipedia.org/wiki/Memory_barrier) to let programmers decide the visibility order between instructions. boost and C++11 conclude memory fence into following types:

| memory order | Description |
| --- | --- |
| memory\_order\_relaxed | there are no synchronization or ordering constraints imposed on other reads or writes, only this operation’s atomicity is guaranteed |
| memory\_order\_consume | no reads or writes in the current thread dependent on the value currently loaded can be reordered before this load. |
| memory\_order\_acquire | no reads or writes in the current thread can be reordered before this load. |
| memory\_order\_release | no reads or writes in the current thread can be reordered after this store. |
| memory\_order\_acq\_rel | No memory reads or writes in the current thread can be reordered before or after this store. |
| memory\_order\_seq\_cst | Any operation with this memory order is both an acquire operation and a release operation, plus a single total order exists in which all threads observe all modifications in the same order. |

Above example can be modified as follows:

```c++
// Thread1
// ready was initialized to false
p.init();
ready.store(true, std::memory_order_release);
```

```c++
// Thread2
if (ready.load(std::memory_order_acquire)) {
    p.bar();
}
```

The acquire fence in thread2 matches the release fence in thread1, making thread2 see all memory operations before the release fence in thread1 when thread2 sees `ready` being set to true.

Note that memory fence does not guarantee visibility. Even if thread2 reads `ready` just after thread1 sets it to true, thread2 is not guaranteed to see the new value, because cache synchronization takes time. Memory fence guarantees ordering between visibilities: “If I see the new value of a, I should see the new value of b as well”.

A related problem: How to know whether a value is updated or not? Two cases in generally:

- The value is special. In above example, `ready=true` is a special value. Once `ready` is true, `p` is ready. Reading special values or not both mean something.
- Increasing-only values. Some situations do not have special values, we can use instructions like `fetch_add` to increase variables. As long as the value range is large enough, new values are different from old ones for a long period of time, so that we can distinguish them from each other.

More examples can be found in [boost.atomic](http://www.boost.org/doc/libs/1_56_0/doc/html/atomic/usage_examples.html). Official descriptions of atomics can be found [here](http://en.cppreference.com/w/cpp/atomic/atomic).

<a id="rpc-in-depth-atomic-instructions--wait-free-lock-free"></a>

# wait-free & lock-free

Atomic instructions provide two important properties: [wait-free](http://en.wikipedia.org/wiki/Non-blocking_algorithm#Wait-freedom) and [lock-free](http://en.wikipedia.org/wiki/Non-blocking_algorithm#Lock-freedom). Wait-free means no matter how OS schedules, all threads are doing useful jobs; lock-free, which is weaker than wait-free, means no matter how OS schedules, at least one thread is doing useful jobs. If locks are used, the thread holding the lock might be paused by OS, in which case all threads trying to hold the lock are blocked. So code using locks are neither lock-free nor wait-free. To make tasks done within given time, critical paths in real-time OS is at least lock-free. Miscellaneous online services inside Baidu also pose serious restrictions on running time. If the critical path in brpc is wait-free or lock-free, many services are benefited from better and stable QoS. Actually, both read(in the sense of even dispatching) and write in brpc are wait-free, check [IO](https://brpc.apache.org/docs/rpc-in-depth/io) for details.

Note that it is common to think that wait-free or lock-free algorithms are faster, which may not be true, because:

- More complex race conditions and ABA problems must be handled in lock-free and wait-free algorithms, which means the code is often much more complicated than the one using locks. More code, more running time.
- Mutex solves contentions by backoff, which means that when contention happens, another branch is entered to avoid the contention temporarily. Threads failed to lock a mutex are put into sleep, making the thread holding the mutex complete the task or even follow-up tasks exclusively, which may increase the overall throughput.

Low performance caused by mutex is either because of too large critical sections (which limit the concurrency), or too heavy contentions (overhead of context switches becomes dominating). The real value of lock-free/wait-free algorithms is that they guarantee progress of the system, rather than absolutely high performance. Of course lock-free/wait-free algorithms perform better in some situations: if an algorithm is implemented by just one or two atomic instructions, it’s probably faster than the one using mutex which needs more atomic instructions in total.

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="rpc-in-depth-bthread_id"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/bthread_id/ -->

<!-- page_index: 56 -->

# bthread_id

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/bthread_id/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=bthread_id)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# bthread\_id

Learn about bRPC bthread\_id.

bthread\_id是一个特殊的同步结构，它可以互斥RPC过程中的不同环节，也可以O(1)时间内找到RPC上下文(即Controller)。注意，这里我们谈论的是bthread\_id\_t，不是bthread\_t（bthread的tid），这个名字起的确实不太好，容易混淆。

具体来说，bthread\_id解决的问题有：

- 在发送RPC过程中response回来了，处理response的代码和发送代码产生竞争。
- 设置timer后很快触发了，超时处理代码和发送代码产生竞争。
- 重试产生的多个response同时回来产生的竞争。
- 通过correlation\_id在O(1)时间内找到对应的RPC上下文，而无需建立从correlation\_id到RPC上下文的全局哈希表。
- 取消RPC。

上文提到的bug在其他rpc框架中广泛存在，下面我们来看下brpc是如何通过bthread\_id解决这些问题的。

bthread\_id包括两部分，一个是用户可见的64位id，另一个是对应的不可见的bthread::Id结构体。用户接口都是操作id的。从id映射到结构体的方式和brpc中的[其他结构](#rpc-in-depth-memory-management)类似：32位是内存池的位移，32位是version。前者O(1)时间定位，后者防止ABA问题。

bthread\_id的接口不太简洁，有不少API：

- create
- lock
- unlock
- unlock\_and\_destroy
- join
- error

这么多接口是为了满足不同的使用流程。

- 发送request的流程：bthread\_id\_create -> bthread\_id\_lock -> … register timer and send RPC … -> bthread\_id\_unlock
- 接收response的流程：bthread\_id\_lock -> ..process response -> bthread\_id\_unlock\_and\_destroy
- 异常处理流程：timeout/socket fail -> bthread\_id\_error -> 执行on\_error回调(这里会加锁)，分两种情况
  - 请求重试/backup request： 重新register timer and send RPC -> bthread\_id\_unlock
  - 无法重试，最终失败：bthread\_id\_unlock\_and\_destroy
- 同步等待RPC结束：bthread\_id\_join

为了减少等待，bthread\_id做了一些优化的机制：

- error发生的时候，如果bthread\_id已经被锁住，会把error信息放到一个pending queue中，bthread\_id\_error函数立即返回。当bthread\_id\_unlock的时候，如果pending queue里面有任务就取出来执行。
- RPC结束的时候，如果存在用户回调，先执行一个bthread\_id\_about\_to\_destroy，让正在等待的bthread\_id\_lock操作立即失败，再执行用户回调（这个可能耗时较长，不可控），最后再执行bthread\_id\_unlock\_and\_destroy

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="rpc-in-depth-consistent-hashing"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/consistent-hashing/ -->

<!-- page_index: 57 -->

# Consistent Hashing

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Consistent%20Hashing/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Consistent%20Hashing)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Consistent Hashing

Learn about bRPC consistent hashing.

<a id="rpc-in-depth-consistent-hashing--section"></a>

# 概述

一些场景希望同样的请求尽量落到一台机器上，比如访问缓存集群时，我们往往希望同一种请求能落到同一个后端上，以充分利用其上已有的缓存，不同的机器承载不同的稳定working set。而不是随机地散落到所有机器上，那样的话会迫使所有机器缓存所有的内容，最终由于存不下形成颠簸而表现糟糕。 我们都知道hash能满足这个要求，比如当有n台服务器时，输入x总是会发送到第hash(x) % n台服务器上。但当服务器变为m台时，hash(x) % n和hash(x) % m很可能都不相等，这会使得几乎所有请求的发送目的地都发生变化，如果目的地是缓存服务，所有缓存将失效，继而对原本被缓存遮挡的数据库或计算服务造成请求风暴，触发雪崩。一致性哈希是一种特殊的哈希算法，在增加服务器时，发向每个老节点的请求中只会有一部分转向新节点，从而实现平滑的迁移。[这篇论文](http://blog.phpdr.net/wp-content/uploads/2012/08/Consistent-Hashing-and-Random-Trees.pdf)中提出了一致性hash的概念。

一致性hash满足以下四个性质：

- 平衡性 (Balance) : 每个节点被选到的概率是O(1/n)。
- 单调性 (Monotonicity) : 当新节点加入时， 不会有请求在老节点间移动， 只会从老节点移动到新节点。当有节点被删除时，也不会影响落在别的节点上的请求。
- 分散性 (Spread) : 当上游的机器看到不同的下游列表时(在上线时及不稳定的网络中比较常见), 同一个请求尽量映射到少量的节点中。
- 负载 (Load) : 当上游的机器看到不同的下游列表的时候， 保证每台下游分到的请求数量尽量一致。

<a id="rpc-in-depth-consistent-hashing--section"></a>

# 实现方式

所有server的32位hash值在32位整数值域上构成一个环(Hash Ring)，环上的每个区间和一个server唯一对应，如果一个key落在某个区间内， 它就被分流到对应的server上。

![img](assets/images/chash_0374579e8d1f8641.png)

当删除一个server的，它对应的区间会归属于相邻的server，所有的请求都会跑过去。当增加一个server时，它会分割某个server的区间并承载落在这个区间上的所有请求。单纯使用Hash Ring很难满足我们上节提到的属性，主要两个问题：

- 在机器数量较少的时候， 区间大小会不平衡。
- 当一台机器故障的时候， 它的压力会完全转移到另外一台机器， 可能无法承载。

为了解决这个问题，我们为每个server计算m个hash值，从而把32位整数值域划分为n\*m个区间，当key落到某个区间时，分流到对应的server上。那些额外的hash值使得区间划分更加均匀，被称为虚拟节点（Virtual Node）。当删除一个server时，它对应的m个区间会分别合入相邻的区间中，那个server上的请求会较为平均地转移到其他server上。当增加server时，它会分割m个现有区间，从对应server上分别转移一些请求过来。

由于节点故障和变化不常发生，我们选择了修改复杂度为O(n)的有序数组来存储hash ring，每次分流使用二分查找来选择对应的机器，由于存储是连续的，查找效率比基于平衡二叉树的实现高。线程安全性请参照[Double Buffered Data](#rpc-in-depth-locality-aware--doublybuffereddata)章节.

<a id="rpc-in-depth-consistent-hashing--section"></a>

# 使用方式

我们内置了分别基于murmurhash3和md5两种hash算法的实现，使用要做两件事：

- 在Channel.Init 时指定*load\_balancer\_name*为 “c\_murmurhash” 或 “c\_md5”。
- 发起rpc时通过Controller::set\_request\_code(uint64\_t)填入请求的hash code。

> request的hash算法并不需要和lb的hash算法保持一致，只需要hash的值域是32位无符号整数。由于memcache默认使用md5，访问memcached集群时请选择c\_md5保证兼容性，其他场景可以选择c\_murmurhash以获得更高的性能和更均匀的分布。

<a id="rpc-in-depth-consistent-hashing--section"></a>

# 虚拟节点个数

通过-chash\_num\_replicas可设置默认的虚拟节点个数，默认值为100。对于某些特殊场合，对虚拟节点个数有自定义的需求，可以通过将*load\_balancer\_name*加上参数replicas=配置，如：

```c++
channel.Init("http://...", "c_murmurhash:replicas=150", &options);
```

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="rpc-in-depth"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/ -->

<!-- page_index: 58 -->

# RPC in depth

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=RPC%20in%20depth)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# RPC in depth

Learn about bRPC in depth.

---

##### [New Protocol](#rpc-in-depth-new-protocol)

Learn about how to add a new protocol into bRPC.

##### [Atomic instructions](#rpc-in-depth-atomic-instructions)

Learn about bRPC atomic instructions.

##### [IO](#rpc-in-depth-io)

Learn about bRPC IO.

##### [Threading Overview](#rpc-in-depth-threading-overview)

Learn about bRPC threading.

##### [Load Balancing](#rpc-in-depth-load-balancing)

Learn about bRPC load balancing.

##### [Locality-aware](#rpc-in-depth-locality-aware)

Learn about bRPC locality-aware loadbalancer.

##### [Consistent Hashing](#rpc-in-depth-consistent-hashing)

Learn about bRPC consistent hashing.

##### [Memory Management](#rpc-in-depth-memory-management)

Learn about bRPC memory management.

##### [Timer keeping](#rpc-in-depth-timer-keeping)

Learn about bRPC timer keeping.

##### [bthread\_id](#rpc-in-depth-bthread_id)

Learn about bRPC bthread\_id.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="rpc-in-depth-io"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/io/ -->

<!-- page_index: 59 -->

# IO

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/IO/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=IO)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# IO

Learn about bRPC IO.

There are three mechanisms to operate IO in general:

- Blocking IO: once an IO operation is issued, the calling thread is blocked until the IO ends, which is a kind of synchronous IO, such as default actions of posix [read](http://linux.die.net/man/2/read) and [write](http://linux.die.net/man/2/write).
- Non-blocking IO: If there is nothing to read or too much to write, APIs that would block return immediately with an error code. Non-blocking IO is often used with IO multiplexing([poll](http://linux.die.net/man/2/poll), [select](http://linux.die.net/man/2/select), [epoll](http://linux.die.net/man/4/epoll) in Linux or [kqueue](https://www.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2) in BSD).
- Asynchronous IO: Start a read or write operation with a callback, which will be called when the IO is done, such as [OVERLAPPED](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684342(v=vs.85).aspx) + [IOCP](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365198(v=vs.85).aspx) in Windows. Native AIO in Linux only supports files.

Non-blocking IO is usually used for increasing IO concurrency in Linux. When the IO concurrency is low, non-blocking IO is not necessarily more efficient than blocking IO, which is handled completely by the kernel. System calls like read/write are highly optimized and probably more efficient. But when IO concurrency increases, the drawback of blocking-one-thread in blocking IO arises: the kernel keeps switching between threads to do effective jobs, and a CPU core may only do a little bit of work before being replaced by another thread, causing CPU cache not fully utilized. In addition a large number of threads decrease performance of code dependent on thread-local variables, such as tcmalloc. Once malloc slows down, the overall performance of the program decreases as well. As a contrast, non-blocking IO is typically composed with a relatively small number of event dispatching threads and worker threads(running user code), which are reused by different tasks (in another word, part of scheduling work is moved to userland). Event dispatchers and workers run on different CPU cores simultaneously without frequent switches in the kernel. There’s no need to have many threads, so the use of thread-local variables is also more adequate. All these factors make non-blocking IO faster than blocking IO. But non-blocking IO also has its own problems, one of which is more system calls, such as [epoll\_ctl](http://man7.org/linux/man-pages/man2/epoll_ctl.2.html). Since epoll is implemented as a red-black tree, epoll\_ctl is not a very fast operation, especially in multi-threaded environments. Implementations heavily dependent on epoll\_ctl is often confronted with multi-core scalability issues. Non-blocking IO also has to solve a lot of multi-threaded problems, producing more complex code than blocking IO.

<a id="rpc-in-depth-io--receiving-messages"></a>

# Receiving messages

A message is a bounded binary data read from a connection, which may be a request from upstream clients or a response from downstream servers. brpc uses one or several [EventDispatcher](https://github.com/brpc/brpc/blob/master/src/brpc/event_dispatcher.cpp)(referred to as EDISP) to wait for events from file descriptors. Unlike the common “IO threads”, EDISP is not responsible for reading or writing. The problem of IO threads is that one thread can only read one fd at a given time, other reads may be delayed when many fds in one IO thread are busy. Multi-tenancy, complicated load balancing and [Streaming RPC](#client-streaming-rpc) worsen the problem. Under high workloads, regular long delays on one fd may slow down all fds in the IO thread, causing more long tails.

Because of a [bug](https://patchwork.kernel.org/patch/1970231/) of epoll (at the time of developing brpc) and overhead of epoll\_ctl, edge triggered mode is used in EDISP. After receiving an event, an atomic variable associated with the fd is added by one atomically. If the variable is zero before addition, a bthread is started to handle the data from the fd. The pthread worker in which EDISP runs is yielded to the newly created bthread to make it start reading ASAP and have a better cache locality. The bthread in which EDISP runs will be stolen to another pthread and keep running, this mechanism is work stealing used in bthreads. To understand exactly how that atomic variable works, you can read [atomic instructions](#rpc-in-depth-atomic-instructions) first, then check [Socket::StartInputEvent](https://github.com/brpc/brpc/blob/master/src/brpc/socket.cpp). These methods make contentions on dispatching events of one fd [wait-free](http://en.wikipedia.org/wiki/Non-blocking_algorithm#Wait-freedom).

[InputMessenger](https://github.com/brpc/brpc/blob/master/src/brpc/input_messenger.h) cuts messages and uses customizable callbacks to handle different format of data. `Parse` callback cuts messages from binary data and has relatively stable running time; `Process` parses messages further(such as parsing by protobuf) and calls users’ callbacks, which vary in running time. If n(n > 1) messages are read from the fd, InputMessenger launches n-1 bthreads to handle first n-1 messages respectively, and processes the last message in-place. InputMessenger tries protocols one by one. Since one connections often has only one type of messages, InputMessenger remembers current protocol to avoid trying for protocols next time.

It can be seen that messages from different fds or even same fd are processed concurrently in brpc, which makes brpc good at handling large messages and reducing long tails on processing messages from different sources under high workloads.

<a id="rpc-in-depth-io--sending-messages"></a>

# Sending Messages

A message is a bounded binary data written to a connection, which may be a response to upstream clients or a request to downstream servers. Multiple threads may send messages to a fd at the same time, however writing to a fd is non-atomic, so how to queue writes from different thread efficiently is a key technique. brpc uses a special wait-free MPSC list to solve the issue. All data ready to write is put into a node of a singly-linked list, whose next pointer points to a special value(`Socket::WriteRequest::UNCONNECTED`). When a thread wants to write out some data, it tries to atomically exchange the node with the list head(Socket::\_write\_head) first. If the head before exchange is empty, the caller gets the right to write and writes out the data in-place once. Otherwise there must be another thread writing. The caller points the next pointer to the head returned to make the linked list connected. The thread that is writing will see the new head later and write new data.

This method makes the writing contentions wait-free. Although the thread that gets the right to write is not wait-free nor lock-free in principle and may be blocked by a node that is still UNCONNECTED(the thread issuing write is swapped out by OS just after atomic exchange and before setting the next pointer, within execution time of just one instruction), the blocking rarely happens in practice. In current implementations, if the data cannot be written fully in one call, a KeepWrite bthread is created to write the remaining data. This mechanism is pretty complicated and the principle is depicted below. Read [socket.cpp](https://github.com/brpc/brpc/blob/master/src/brpc/socket.cpp) for more details.

![img](assets/images/write_d1c7b6001dc2d9b5.png)

Since writes in brpc always complete within short time, the calling thread can handle new tasks more quickly and background KeepWrite threads also get more tasks to write in one batch, forming pipelines and increasing the efficiency of IO at high throughputs.

<a id="rpc-in-depth-io--socket"></a>

# Socket

[Socket](https://github.com/brpc/brpc/blob/master/src/brpc/socket.h) contains data structures related to fd and is one of the most complex structure in brpc. The unique feature of this structure is that it uses 64-bit SocketId to refer to a Socket object to facilitate usages of fd in multi-threaded environments. Commonly used methods:

- Create: create a Socket and return its SocketId.
- Address: retrieve Socket from an id, and wrap it into a unique\_ptr(SocketUniquePtr) that will be automatically released. When Socket is set failed, the pointer returned is empty. As long as Address returns a non-null pointer, the contents are guaranteed to not change until the pointer is destructed. This function is wait-free.
- SetFailed: Mark a Socket as failed and Address() on corresponding SocketId will return empty pointer (until health checking resumes the socket). Sockets are recycled when no one is referencing it anymore. This function is lock-free.

We can see that, Socket is similar to [shared\_ptr](http://en.cppreference.com/w/cpp/memory/shared_ptr) in the sense of referential counting and SocketId is similar to [weak\_ptr](http://en.cppreference.com/w/cpp/memory/weak_ptr). The unique `SetFailed` prevents Socket from being addressed so that the reference count can hit zero finally. Simply using shared\_ptr/weak\_ptr cannot guarantee this. For example, when a server needs to quit when requests are still coming in frequently, the reference count of Socket may not hit zero and the server is unable to stop quickly. What’ more, weak\_ptr cannot be directly put into epoll data, but SocketId can. These factors lead to design of Socket which is stable and rarely changed since 2014.

Using SocketUniquePtr or SocketId depends on if a strong reference is needed. For example, Controller is used thoroughly inside RPC and has a lot of interactions with Socket, it uses SocketUniquePtr. Epoll notifies events on fds and events of a recycled socket can be ignored, so epoll uses SocketId.

As long as SocketUniquePtr is valid, the Socket enclosed will not be changed so that users have no need to care about race conditions and ABA problems, being safer to operate the shared socket. This method also circumvents implicit referential counting and makes ownership of memory more clear, producing better-quality programs. brpc uses SocketUniquePtr and SocketId a lot to simplify related issues.

In fact, Socket manages not only the native fd but also other resources, such as SubChannel in SelectiveChannel is also managed by Socket, making SelectiveChannel choose a SubChannel just like a normal channel choosing a downstream server. The faked Socket even implements health checking. Streaming RPC also uses Socket to reuse the code on wait-free write.

<a id="rpc-in-depth-io--the-full-picture"></a>

# The full picture

![img](assets/images/rpc-flow_85ad78a4ea1c46ae.png)

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="rpc-in-depth-load-balancing"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/load-balancing/ -->

<!-- page_index: 60 -->

# Load Balancing

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Load%20Balancing/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Load%20Balancing)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Load Balancing

Learn about bRPC load balancing.

上游一般通过命名服务发现所有的下游节点，并通过多种负载均衡方法把流量分配给下游节点。当下游节点出现问题时，它可能会被隔离以提高负载均衡的效率。被隔离的节点定期被健康检查，成功后重新加入正常节点。

<a id="rpc-in-depth-load-balancing--section"></a>

# 命名服务

在brpc中，[NamingService](https://github.com/brpc/brpc/blob/master/src/brpc/naming_service.h)用于获得服务名对应的所有节点。一个直观的做法是定期调用一个函数以获取最新的节点列表。但这会带来一定的延时（定期调用的周期一般在若干秒左右），作为通用接口不太合适。特别当命名服务提供事件通知时(比如zk)，这个特性没有被利用。所以我们反转了控制权：不是我们调用用户函数，而是用户在获得列表后调用我们的接口，对应[NamingServiceActions](https://github.com/brpc/brpc/blob/master/src/brpc/naming_service.h)。当然我们还是得启动进行这一过程的函数，对应NamingService::RunNamingService。下面以三个实现解释这套方式：

- bns：没有事件通知，所以我们只能定期去获得最新列表，默认间隔是[5秒](http://brpc.baidu.com:8765/flags/ns_access_interval)。为了简化这类定期获取的逻辑，brpc提供了[PeriodicNamingService](https://github.com/brpc/brpc/blob/master/src/brpc/periodic_naming_service.h) 供用户继承，用户只需要实现单次如何获取（GetServers）。获取后调用NamingServiceActions::ResetServers告诉框架。框架会对列表去重，和之前的列表比较，通知对列表有兴趣的观察者(NamingServiceWatcher)。这套逻辑会运行在独立的bthread中，即NamingServiceThread。一个NamingServiceThread可能被多个Channel共享，通过intrusive\_ptr管理ownership。
- file：列表即文件。合理的方式是在文件更新后重新读取。[该实现](https://github.com/brpc/brpc/blob/master/src/brpc/policy/file_naming_service.cpp)使用[FileWatcher](https://github.com/brpc/brpc/blob/master/src/butil/files/file_watcher.h)关注文件的修改时间，当文件修改后，读取并调用NamingServiceActions::ResetServers告诉框架。
- list：列表就在服务名里（逗号分隔）。在读取完一次并调用NamingServiceActions::ResetServers后就退出了，因为列表再不会改变了。

如果用户需要建立这些对象仍然是不够方便的，因为总是需要一些工厂代码根据配置项建立不同的对象，鉴于此，我们把工厂类做进了框架，并且是非常方便的形式：

```
"protocol://service-name"
 
e.g.
bns://<node-name>            # baidu naming service
file://<file-path>           # load addresses from the file
list://addr1,addr2,...       # use the addresses separated by comma
http://<url>                 # Domain Naming Service, aka DNS.
```

这套方式是可扩展的，实现了新的NamingService后在[global.cpp](https://github.com/brpc/brpc/blob/master/src/brpc/global.cpp)中依葫芦画瓢注册下就行了，如下图所示：

![img](assets/images/register-ns_df39c929c9ede01d.png)

看到这些熟悉的字符串格式，容易联想到ftp:// zk:// galileo://等等都是可以支持的。用户在新建Channel时传入这类NamingService描述，并能把这些描述写在各类配置文件中。

<a id="rpc-in-depth-load-balancing--section"></a>

# 负载均衡

brpc中[LoadBalancer](https://github.com/brpc/brpc/blob/master/src/brpc/load_balancer.h)从多个服务节点中选择一个节点，目前的实现见[负载均衡](#client-basics--load-balancer)。

Load balancer最重要的是如何让不同线程中的负载均衡不互斥，解决这个问题的技术是[DoublyBufferedData](#rpc-in-depth-locality-aware--doublybuffereddata)。

和NamingService类似，我们使用字符串来指代一个load balancer，在global.cpp中注册：

![img](assets/images/register-lb_4c9f094dfa843a20.png)

<a id="rpc-in-depth-load-balancing--section"></a>

# 健康检查

对于那些无法连接却仍在NamingService的节点，brpc会定期连接它们，成功后对应的Socket将被”复活“，并可能被LoadBalancer选择上，这个过程就是健康检查。注意：被健康检查或在LoadBalancer中的节点一定在NamingService中。换句话说，只要一个节点不从NamingService删除，它要么是正常的（会被LoadBalancer选上），要么在做健康检查。

传统的做法是使用一个线程做所有连接的健康检查，brpc简化了这个过程：为需要的连接动态创建一个bthread专门做健康检查（Socket::HealthCheckThread）。这个线程的生命周期被对应连接管理。具体来说，当Socket被SetFailed后，健康检查线程就可能启动（如果SocketOptions.health\_check\_interval为正数的话）：

- 健康检查线程先在确保没有其他人在使用Socket了后关闭连接。目前是通过对Socket的引用计数判断的。这个方法之所以有效在于Socket被SetFailed后就不能被Address了，所以引用计数只减不增。
- 定期连接直到远端机器被连接上，在这个过程中，如果Socket析构了，那么该线程也就随之退出了。
- 连上后复活Socket(Socket::Revive)，这样Socket就又能被其他地方，包括LoadBalancer访问到了（通过Socket::Address）。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="rpc-in-depth-locality-aware"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/locality-aware/ -->

<!-- page_index: 61 -->

# Locality-aware

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Locality-aware/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Locality-aware)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [DoublyBufferedData](#rpc-in-depth-locality-aware--doublybuffereddata)
- [weight tree](#rpc-in-depth-locality-aware--weight-tree)
- [base\_weight](#rpc-in-depth-locality-aware--base_weight)
- [inflight delay](#rpc-in-depth-locality-aware--inflight-delay)

# Locality-aware

Learn about bRPC locality-aware loadbalancer.

<a id="rpc-in-depth-locality-aware--section"></a>

# 概述

LALB全称Locality-aware load balancing，是一个能把请求及时、自动地送到延时最低的下游的负载均衡算法，特别适合混合部署环境。该算法产生自DP系统，现已加入brpc！

LALB可以解决的问题：

- 下游的机器配置不同，访问延时不同，round-robin和随机分流效果不佳。
- 下游服务和离线服务或其他服务混部，性能难以预测。
- 自动地把大部分流量送给同机部署的模块，当同机模块出问题时，再跨机器。
- 优先访问本机房服务，出问题时再跨机房。

**…**

<a id="rpc-in-depth-locality-aware--section"></a>

# 背景

最常见的分流算法是round robin和随机。这两个方法的前提是下游的机器和网络都是类似的，但在目前的线上环境下，特别是混部的产品线中，已经很难成立，因为：

- 每台机器运行着不同的程序组合，并伴随着一些离线任务，机器的可用资源在持续动态地变化着。
- 机器配置不同。
- 网络延时不同。

这些问题其实一直有，但往往被OP辛勤的机器监控和替换给隐藏了。框架层面也有过一些努力，比如UB中的[WeightedStrategy](https://svn.baidu.com/public/trunk/ub/ub_client/ubclient_weightstrategy.h)是根据下游的cpu占用率来进行分流，但明显地它解决不了延时相关的问题，甚至cpu的问题也解决不了：因为它被实现为定期reload一个权值列表，可想而知更新频率高不了，等到负载均衡反应过来，一大堆请求可能都超时了。并且这儿有个数学问题：怎么把cpu占用率转为权值。假设下游差异仅仅由同机运行的其他程序导致，机器配置和网络完全相同，两台机器权值之比是cpu idle之比吗？假如是的，当我们以这个比例给两台机器分流之后，它们的cpu idle应该会更接近对吧？而这会导致我们的分流比例也变得接近，从而使两台机器的cpu idle又出现差距。你注意到这个悖论了吗？这些因素使得这类算法的实际效果和那两个基本算法没什么差距，甚至更差，用者甚少。

我们需要一个能自适应下游负载、规避慢节点的通用分流算法。

<a id="rpc-in-depth-locality-aware--locality-aware"></a>

# Locality-aware

在DP 2.0中我们使用了一种新的算法: Locality-aware load balancing，能根据下游节点的负载分配流量，还能快速规避失效的节点，在很大程度上，这种算法的延时也是全局最优的。基本原理非常简单：

> 以下游节点的吞吐除以延时作为分流权值。

比如只有两台下游节点，W代表权值，QPS代表吞吐，L代表延时，那么W1 = QPS1 / L1和W2 = QPS2 / L2分别是这两个节点的分流权值，分流时随机数落入的权值区间就是流量的目的地了。

一种分析方法如下：

- 稳定状态时的QPS显然和其分流权值W成正比，即W1 / W2 ≈ QPS1 / QPS2。
- 根据分流公式又有：W1 / W2 = QPS1 / QPS2 \* (L2 / L1)。

故稳定状态时L1和L2应当是趋同的。当L1小于L2时，节点1会更获得相比其QPS1更大的W1，从而在未来获得更多的流量，直到**其延时高于平均值或没有更多的流量。**

注意这个算法并不是按照延时的比例来分流，不是说一个下游30ms，另一个60ms，它们的流量比例就是60 / 30。而是30ms的节点会一直获得流量直到它的延时高于60ms，或者没有更多流量了。以下图为例，曲线1和曲线2分别是节点1和节点2的延时与吞吐关系图，随着吞吐增大延时会逐渐升高，接近极限吞吐时，延时会飙升。左下的虚线标记了QPS=400时的延时，此时虽然节点1的延时有所上升，但还未高于节点2的基本延时（QPS=0时的延时），所以所有流量都会分给节点1，而不是按它们基本延时的比例（图中大约2:1）。当QPS继续上升达到1600时，分流比例会在两个节点延时相等时平衡，图中为9 : 7。很明显这个比例是高度非线性的，取决于不同曲线的组合，和单一指标的比例关系没有直接关联。在真实系统中，延时和吞吐的曲线也在动态变化着，分流比例更加动态。

![img](assets/images/lalb-1_1d2ccc1120aecad8.png)

我们用一个例子来看一下具体的分流过程。启动3台server，逻辑分别是sleep 1ms，2ms，3ms，对于client来说这些值就是延时。启动client（50个同步访问线程）后每秒打印的分流结果如下：

![img](assets/images/lalb-2_ea3fbf57a677bc5d.png)

S[n]代表第n台server。由于S[1]和S[2]的平均延时大于1ms，LALB会发现这点并降低它们的权值。它们的权值会继续下降，直到被算法设定的最低值拦住。这时停掉server，反转延时并重新启动，即逻辑分别为sleep 3ms，2ms，1ms，运行一段时候后分流效果如下：

![img](assets/images/lalb-3_1fb1660670409b44.png)

刚重连上server时，client还是按之前的权值把大部分流量都分给了S[0]，但由于S[0]的延时从1ms上升到了3ms，client的qps也降到了原来的1/3。随着数据积累，LALB逐渐发现S[2]才是最快的，而把大部分流量切换了过去。同样的服务如果用rr或random访问，则qps会显著下降：

“rr” or “random”: ![img](assets/images/lalb-4_a467b31005e82e85.png)

“la” : ![img](assets/images/lalb-5_6074dd902dfbedd5.png)

真实的场景中不会有这么显著的差异，但你应该能看到差别了。

这有很多应用场景：

- 如果本机有下游服务，LALB会优先访问这些最近的节点。比如CTR应用中有一个计算在1ms左右的receiver模块，被model模块访问，很多model和receiver是同机部署的，以前的分流算法必须走网络，使得receiver的延时开销较大(3-5ms)，特别是在晚上由于离线任务起来，很不稳定，失败率偏高，而LALB会优先访问本机或最近的receiver模块，很多流量都不走网络了，成功率一下子提升了很多。
- 如果同rack有下游服务，LALB也会优先访问，减少机房核心路由器的压力。甚至不同机房的服务可能不再需要隔离，LALB会优先走本机房的下游，当本机房下游出问题时再自动访问另一些机房。

但我们也不能仅看到“基本原理”，这个算法有它复杂的一面：

- 传统的经验告诉我们，不能把所有鸡蛋放一个篮子里，而按延时优化不可避免地会把很多流量送到同一个节点，如果这个节点出问题了，我们如何尽快知道并绕开它。
- 对吞吐和延时的统计都需要统计窗口，窗口越大数据越可信，噪声越少，但反应也慢了，一个异常的请求可能对统计值造不成什么影响，等我们看到统计值有显著变化时可能已经太晚了。
- 我们也不能只统计已经回来的，还得盯着路上的请求，否则我们可能会向一个已经出问题（总是不回）的节点傻傻地浪费请求。
- ”按权值分流”听上去好简单，但你能写出多线程和可能修改节点的前提下，在O(logN)时间内尽量不互斥的查找算法吗？

这些问题可以归纳为以下几个方面。

<a id="rpc-in-depth-locality-aware--doublybuffereddata"></a>

## DoublyBufferedData

LoadBalancer是一个读远多于写的数据结构：大部分时候，所有线程从一个不变的server列表中选取一台server。如果server列表真是“不变的”，那么选取server的过程就不用加锁，我们可以写更复杂的分流算法。一个方法是用读写锁，但当读临界区不是特别大时（毫秒级），读写锁并不比mutex快，而实用的分流算法不可能到毫秒级，否则开销也太大了。另一个方法是双缓冲，很多检索端用类似的方法实现无锁的查找过程，它大概这么工作：

- 数据分前台和后台。
- 检索线程只读前台，不用加锁。
- 只有一个写线程：修改后台数据，切换前后台，睡眠一段时间，以确保老前台（新后台）不再被检索线程访问。

这个方法的问题在于它假定睡眠一段时间后就能避免和前台读线程发生竞争，这个时间一般是若干秒。由于多次写之间有间隔，这儿的写往往是批量写入，睡眠时正好用于积累数据增量。

但这套机制对“server列表”不太好用：总不能插入一个server就得等几秒钟才能插入下一个吧，即使我们用批量插入，这个"冷却"间隔多少会让用户觉得疑惑：短了担心安全性，长了觉得没有必要。我们能尽量降低这个时间并使其安全么？

我们需要**写以某种形式和读同步，但读之间相互没竞争**。一种解法是，读拿一把thread-local锁，写需要拿到所有的thread-local锁。具体过程如下：

- 数据分前台和后台。
- 读拿到自己所在线程的thread-local锁，执行查询逻辑后释放锁。
- 同时只有一个写：修改后台数据，切换前后台，**挨个**获得所有thread-local锁并立刻释放，结束后再改一遍新后台（老前台）。

我们来分析下这个方法的基本原理：

- 当一个读正在发生时，它会拿着所在线程的thread-local锁，这把锁会挡住同时进行的写，从而保证前台数据不会被修改。
- 在大部分时候thread-local锁都没有竞争，对性能影响很小。
- 逐个获取thread-local锁并立刻释放是为了**确保对应的读线程看到了切换后的新前台**。如果所有的读线程都看到了新前台，写线程便可以安全地修改老前台（新后台）了。

其他特点：

- 不同的读之间没有竞争，高度并发。
- 如果没有写，读总是能无竞争地获取和释放thread-local锁，一般小于25ns，对延时基本无影响。如果有写，由于其临界区极小（拿到立刻释放），读在大部分时候仍能快速地获得锁，少数时候释放锁时可能有唤醒写线程的代价。由于写本身就是少数情况，读整体上几乎不会碰到竞争锁。

完成这些功能的数据结构是[DoublyBufferedData<>](https://github.com/brpc/brpc/blob/master/src/butil/containers/doubly_buffered_data.h)，我们常简称为DBD。brpc中的所有load balancer都使用了这个数据结构，使不同线程在分流时几乎不会互斥。而其他rpc实现往往使用了全局锁，这使得它们无法写出复杂的分流算法：否则分流代码将会成为竞争热点。

这个结构有广泛的应用场景：

- reload词典。大部分时候词典都是只读的，不同线程同时查询时不应互斥。
- 可替换的全局callback。像butil/logging.cpp支持配置全局LogSink以重定向日志，这个LogSink就是一个带状态的callback。如果只是简单的全局变量，在替换后我们无法直接删除LogSink，因为可能还有都写线程在用。用DBD可以解决这个问题。

<a id="rpc-in-depth-locality-aware--weight-tree"></a>

## weight tree

LALB的查找过程是按权值分流，O(N)方法如下：获得所有权值的和total，产生一个间于[0, total-1]的随机数R，逐个遍历权值，直到当前权值之和不大于R，而下一个权值之和大于R。

这个方法可以工作，也好理解，但当N达到几百时性能已经很差，这儿的主要因素是cache一致性：LALB是一个基于反馈的算法，RPC结束时信息会被反馈入LALB，被遍历的数据结构也一直在被修改。这意味着前台的O(N)读必须刷新每一行cacheline。当N达到数百时，一次查找过程可能会耗时百微秒，更别提更大的N了，LALB（将）作为brpc的默认分流算法，这个性能开销是无法接受的。

另一个办法是用完全二叉树。每个节点记录了左子树的权值之和，这样我们就能在O(logN)时间内完成查找。当N为1024时，我们最多跳转10次内存，总耗时可控制在1微秒内，这个性能是可接受的。这个方法的难点是如何和DoublyBufferedData结合。

- 我们不考虑不使用DoublyBufferedData，那样要么绕不开锁，要么写不出正确的算法。
- 前台后必须共享权值数据，否则切换前后台时，前台积累的权值数据没法同步到后台。
- “左子树权值之和”也被前后台共享，但和权值数据不同，它和位置绑定。比如权值结构的指针可能从位置10移动到位置5，但“左子树权值之和”的指针不会移动，算法需要从原位置减掉差值，而向新位置加上差值。
- 我们不追求一致性，只要最终一致即可，这能让我们少加锁。这也意味着“权值之和”，“左子树权值之和”，“节点权值”未必能精确吻合，查找算法要能适应这一点。

最困难的部分是增加和删除节点，它们需要在整体上对前台查找不造成什么影响，详细过程请参考代码。

<a id="rpc-in-depth-locality-aware--base_weight"></a>

## base\_weight

QPS和latency使用一个循环队列统计，默认容量128。我们可以使用这么小的统计窗口，是因为inflight delay能及时纠正过度反应，而128也具备了一定的统计可信度。不过，这么计算latency的缺点是：如果server的性能出现很大的变化，那么我们需要积累一段时间才能看到平均延时的变化。就像上节例子中那样，server反转延时后client需要积累很多秒的数据才能看到的平均延时的变化。目前我们并么有处理这个问题，因为真实生产环境中的server不太会像例子中那样跳变延时，大都是缓缓变慢。当集群有几百台机器时，即使我们反应慢点给个别机器少分流点也不会导致什么问题。如果在产品线中确实出现了性能跳变，并且集群规模不大，我们再处理这个问题。

权值的计算方法是base\_weight = QPS \* WEIGHT\_SCALE / latency ^ p。其中WEIGHT\_SCALE是一个放大系数，为了能用整数存储权值，又能让权值有足够的精度，类似定点数。p默认为2，延时的收敛速度大约为p=1时的p倍，选项quadratic\_latency=false可使p=1。

权值计算在各个环节都有最小值限制，为了防止某个节点的权值过低而使其完全没有访问机会。即使一些延时远大于平均延时的节点，也应该有足够的权值，以确保它们可以被定期访问，否则即使它们变快了，我们也不会知道。

> 除了待删除节点，所有节点的权值绝对不会为0。

这也制造了一个问题：即使一个server非常缓慢（但没有断开连接），它的权值也不会为0，所以总会有一些请求被定期送过去而铁定超时。当qps不高时，为了降低影响面，探测间隔必须拉长。比如为了把对qps=1000的影响控制在1%%内，故障server的权值必须低至使其探测间隔为10秒以上，这降低了我们发现server变快的速度。这个问题的解决方法有：

- 什么都不干。这个问题也许没有想象中那么严重，由于持续的资源监控，线上服务很少出现“非常缓慢”的情况，一般性的变慢并不会导致请求超时。
- 保存一些曾经发向缓慢server的请求，用这些请求探测。这个办法的好处是不浪费请求。但实现起来耦合很多，比较麻烦。
- 强制backup request。
- 再选一次。

<a id="rpc-in-depth-locality-aware--inflight-delay"></a>

## inflight delay

我们必须追踪还未结束的RPC，否则我们就必须等待到超时或其他错误发生，而这可能会很慢（超时一般会是正常延时的若干倍），在这段时间内我们可能做出了很多错误的分流。最简单的方法是统计未结束RPC的耗时：

- 选择server时累加发出时间和未结束次数。
- 反馈时扣除发出时间和未结束次数。
- 框架保证每个选择总对应一次反馈。

这样“当前时间 - 发出时间之和 / 未结束次数”便是未结束RPC的平均耗时，我们称之为inflight delay。当inflight delay大于平均延时时，我们就线性地惩罚节点权值，即weight = base\_weight \* avg\_latency / inflight\_delay。当发向一个节点的请求没有在平均延时内回来时，它的权值就会很快下降，从而纠正我们的行为，这比等待超时快多了。不过这没有考虑延时的正常抖动，我们还得有方差，方差可以来自统计，也可简单线性于平均延时。不管怎样，有了方差bound后，当inflight delay > avg\_latency + max(bound \* 3, MIN\_BOUND)时才会惩罚权值。3是正态分布中的经验数值。

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="rpc-in-depth-memory-management"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/memory-management/ -->

<!-- page_index: 62 -->

# Memory Management

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Memory%20Management/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Memory%20Management)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Memory Management

Learn about bRPC memory management.

内存管理总是程序中的重要一环，在多线程时代，一个好的内存分配大都在如下两点间权衡：

- 线程间竞争少。内存分配的粒度大都比较小，对性能敏感，如果不同的线程在大多数分配时会竞争同一份资源或同一把锁，性能将会非常糟糕，原因无外乎和cache一致性有关，已被大量的malloc方案证明。
- 浪费的空间少。如果每个线程各申请各的，速度也许不错，但万一一个线程总是申请，另一个线程总是释放，内存就爆炸了。线程之间总是要共享内存的，如何共享就是方案的关键了。

一般的应用可以使用[tcmalloc](http://goog-perftools.sourceforge.net/doc/tcmalloc.html)、[jemalloc](https://github.com/jemalloc/jemalloc)等成熟的内存分配方案，但这对于较为底层，关注性能长尾的应用是不够的。多线程框架广泛地通过传递对象的ownership来让问题异步化，如何让分配这些小对象的开销变的更小是值得研究的问题。其中的一个特点较为显著：

- 大多数结构是等长的。

这个属性可以大幅简化内存分配的过程，获得比通用malloc更稳定、快速的性能。brpc中的ResourcePool和ObjectPool即提供这类分配。

> 这篇文章不鼓励用户使用ResourcePool或ObjectPool，事实上我们反对用户在程序中使用这两个类。因为”等长“的副作用是某个类型独占了一部分内存，这些内存无法再被其他类型使用，如果不加控制的滥用，反而会在程序中产生大量彼此隔离的内存分配体系，既浪费内存也不见得会有更好的性能。

<a id="rpc-in-depth-memory-management--resourcepoolt"></a>

# ResourcePool

创建一个类型为T的对象并返回一个偏移量，这个偏移量可以在O(1)时间内转换为对象指针。这个偏移量相当于指针，但它的值在一般情况下小于2^32，所以我们可以把它作为64位id的一部分。对象可以被归还，但归还后对象并没有删除，也没有被析构，而是仅仅进入freelist。下次申请时可能会取到这种使用过的对象，需要重置后才能使用。当对象被归还后，通过对应的偏移量仍可以访问到对象，即ResourcePool只负责内存分配，并不解决ABA问题。但对于越界的偏移量，ResourcePool会返回空。

由于对象等长，ResourcePool通过批量分配和归还内存以避免全局竞争，并降低单次的开销。每个线程的分配流程如下：

1. 查看thread-local free block。如果还有free的对象，返回。没有的话步骤2。
2. 尝试从全局取一个free block，若取到的话回到步骤1，否则步骤3。
3. 从全局取一个block，返回其中第一个对象。

原理是比较简单的。工程实现上数据结构、原子变量、memory fence等问题会复杂一些。下面以bthread\_t的生成过程说明ResourcePool是如何被应用的。

<a id="rpc-in-depth-memory-management--objectpoolt"></a>

# ObjectPool

这是ResourcePool的变种，不返回偏移量，而直接返回对象指针。内部结构和ResourcePool类似，一些代码更加简单。对于用户来说，这就是一个多线程下的对象池，brpc里也是这么用的。比如Socket::Write中把每个待写出的请求包装为WriteRequest，这个对象就是用ObjectPool分配的。

<a id="rpc-in-depth-memory-management--bthread_t"></a>

# 生成bthread\_t

用户期望通过创建bthread获得更高的并发度，所以创建bthread必须很快。 在目前的实现中创建一个bthread的平均耗时小于200ns。如果每次都要从头创建，是不可能这么快的。创建过程更像是从一个bthread池子中取一个实例，我们又同时需要一个id来指代一个bthread，所以这儿正是ResourcePool的用武之地。bthread在代码中被称作Task，其结构被称为TaskMeta，定义在[task\_meta.h](https://github.com/brpc/brpc/blob/master/src/bthread/task_meta.h)中，所有的TaskMeta由ResourcePool分配。

bthread的大部分函数都需要在O(1)时间内通过bthread\_t访问到TaskMeta，并且当bthread\_t失效后，访问应返回NULL以让函数做出返回错误。解决方法是：bthread\_t由32位的版本和32位的偏移量组成。版本解决[ABA问题](http://en.wikipedia.org/wiki/ABA_problem)，偏移量由ResourcePool分配。查找时先通过偏移量获得TaskMeta，再检查版本，如果版本不匹配，说明bthread失效了。注意：这只是大概的说法，在多线程环境下，即使版本相等，bthread仍可能随时失效，在不同的bthread函数中处理方法都是不同的，有些函数会加锁，有些则能忍受版本不相等。

![img](assets/images/resource-pool_9d5e2c123de3cfbc.png)

这种id生成方式在brpc中应用广泛，brpc中的SocketId，bthread\_id\_t也是用类似的方法分配的。

<a id="rpc-in-depth-memory-management--section"></a>

# 栈

使用ResourcePool加快创建的副作用是：一个pool中所有bthread的栈必须是一样大的。这似乎限制了用户的选择，不过基于我们的观察，大部分用户并不关心栈的具体大小，而只需要两种大小的栈：尺寸普通但数量较少，尺寸小但数量众多。所以我们用不同的pool管理不同大小的栈，用户可以根据场景选择。两种栈分别对应属性BTHREAD\_ATTR\_NORMAL（栈默认为1M）和BTHREAD\_ATTR\_SMALL（栈默认为32K）。用户还可以指定BTHREAD\_ATTR\_LARGE，这个属性的栈大小和pthread一样，由于尺寸较大，bthread不会对其做caching，创建速度较慢。server默认使用BTHREAD\_ATTR\_NORMAL运行用户代码。

栈使用[mmap](http://linux.die.net/man/2/mmap)分配，bthread还会用mprotect分配4K的guard page以检测栈溢出。由于mmap+mprotect不能超过max\_map\_count（默认为65536），当bthread非常多后可能要调整此参数。另外当有很多bthread时，内存问题可能不仅仅是栈，也包括各类用户和系统buffer。

goroutine在1.3前通过[segmented stacks](https://gcc.gnu.org/wiki/SplitStacks)动态地调整栈大小，发现有[hot split](https://docs.google.com/document/d/1wAaf1rYoM4S4gtnPh0zOlGzWtrZFQ5suE8qr2sD8uWQ/pub)问题后换成了变长连续栈（类似于vector resizing，只适合内存托管的语言）。由于bthread基本只会在64位平台上使用，虚存空间庞大，对变长栈需求不明确。加上segmented stacks的性能有影响，bthread暂时没有变长栈的计划。

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="rpc-in-depth-new-protocol"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/new-protocol/ -->

<!-- page_index: 63 -->

# New Protocol

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/New%20Protocol/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=New%20Protocol)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [add ProtocolType](#rpc-in-depth-new-protocol--add-protocoltype)
- [Implement Callbacks](#rpc-in-depth-new-protocol--implement-callbacks)
  - [parse](#rpc-in-depth-new-protocol--parse)
  - [serialize\_request](#rpc-in-depth-new-protocol--serialize_request)
  - [pack\_request](#rpc-in-depth-new-protocol--pack_request)
  - [process\_request](#rpc-in-depth-new-protocol--process_request)
  - [process\_response](#rpc-in-depth-new-protocol--process_response)
  - [verify](#rpc-in-depth-new-protocol--verify)
  - [parse\_server\_address](#rpc-in-depth-new-protocol--parse_server_address)
  - [get\_method\_name](#rpc-in-depth-new-protocol--get_method_name)
  - [supported\_connection\_type](#rpc-in-depth-new-protocol--supported_connection_type)
  - [name](#rpc-in-depth-new-protocol--name)
- [Register to global](#rpc-in-depth-new-protocol--register-to-global)

# New Protocol

Learn about how to add a new protocol into bRPC.

<a id="rpc-in-depth-new-protocol--multi-protocol-support-in-the-server-side"></a>

# Multi-protocol support in the server side

brpc server supports all protocols in the same port, and it makes deployment and maintenance more convenient in most of the time. Since the format of different protocols is very different, it is hard to support all protocols in the same port unambiguously. In consider of decoupling and extensibility, it is also hard to build a multiplexer for all protocols. Thus our way is to classify all protocols into three categories and try one by one:

- First-class protocol: Special characters are marked in front of the protocol data, for example, the data of protocol [baidu\_std](https://github.com/apache/brpc/blob/master/docs/cn/baidu_std.md) and hulu\_pbrpc begins with ‘PRPC’ and ‘HULU’ respectively. Parser just check first four characters to know whether the protocol is matched. This class of protocol is checked first and all these protocols can share one TCP connection.
- Second-class protocol: Some complex protocols without special marked characters can only be detected after several input data are parsed. Currently only HTTP is classified into this category.
- Third-class protocol: Special characters are in the middle of the protocol data, such as the magic number of nshead protocol is the 25th-28th characters. It is complex to handle this case because without reading first 28 bytes, we cannot determine whether the protocol is nshead. If it is tried before http, http messages less than 28 bytes may not be parsed, since the parser consider it as an incomplete nshead message.

Considering that there will be only one protocol in most connections, we record the result of last selection so that it will be tried first when further data comes. It reduces the overhead of matching protocols to nearly zero for long connections. Although the process of matching protocols will be run every time for short connections, the bottleneck of short connections is not in here and this method is still fast enough. If there are lots of new protocols added into brpc in the future, we may consider some heuristic methods to match protocols.

<a id="rpc-in-depth-new-protocol--multi-protocol-support-in-the-client-side"></a>

# Multi-protocol support in the client side

Unlike the server side that protocols must be dynamically determined based on the data on the connection, the client side as the originator, naturally know their own protocol format. As long as the protocol data is sent through connection pool or short connection, which means it has exclusive usage of that connection, then the protocol can have any complex (or bad) format. Since the client will record the protocol when sending the data, it will use that recorded protocol to parse the data without any matching overhead when responses come back. There is no magic number in some protocols like memcache, redis, it is hard to distinguish them in the server side, but it has no problem in the client side.

<a id="rpc-in-depth-new-protocol--support-new-protocols"></a>

# Support new protocols

brpc is designed to add new protocols at any time, just proceed as follows:

> The protocol that begins with nshead has unified support, just read [this](https://github.com/apache/brpc/blob/master/docs/cn/nshead_service.md).

<a id="rpc-in-depth-new-protocol--add-protocoltype"></a>

## add ProtocolType

Add new protocol type in ProtocolType in [options.proto](https://github.com/brpc/brpc/blob/master/src/brpc/options.proto). If you need to add new protocol, please contact us to add it for you to make sure there is no conflict with protocols of others.

Currently we support in ProtocolType(at the middle of 2018):

```c++
enum ProtocolType {
    PROTOCOL_UNKNOWN = 0;
    PROTOCOL_BAIDU_STD = 1;
    PROTOCOL_STREAMING_RPC = 2;
    PROTOCOL_HULU_PBRPC = 3;
    PROTOCOL_SOFA_PBRPC = 4;
    PROTOCOL_RTMP = 5;
    PROTOCOL_HTTP = 6;
    PROTOCOL_PUBLIC_PBRPC = 7;
    PROTOCOL_NOVA_PBRPC = 8;
    PROTOCOL_NSHEAD_CLIENT = 9;        // implemented in brpc-ub
    PROTOCOL_NSHEAD = 10;
    PROTOCOL_HADOOP_RPC = 11;
    PROTOCOL_HADOOP_SERVER_RPC = 12;
    PROTOCOL_MONGO = 13;               // server side only
    PROTOCOL_UBRPC_COMPACK = 14;
    PROTOCOL_DIDX_CLIENT = 15;         // Client side only
    PROTOCOL_REDIS = 16;               // Client side only
    PROTOCOL_MEMCACHE = 17;            // Client side only
    PROTOCOL_ITP = 18;
    PROTOCOL_NSHEAD_MCPACK = 19;
    PROTOCOL_DISP_IDL = 20;            // Client side only
    PROTOCOL_ERSDA_CLIENT = 21;        // Client side only
    PROTOCOL_UBRPC_MCPACK2 = 22;       // Client side only
    // Reserve special protocol for cds-agent, which depends on FIFO right now
    PROTOCOL_CDS_AGENT = 23;           // Client side only
    PROTOCOL_ESP = 24;                 // Client side only
    PROTOCOL_THRIFT = 25;              // Server side only
}
```

<a id="rpc-in-depth-new-protocol--implement-callbacks"></a>

## Implement Callbacks

All callbacks are defined in struct Protocol, which is defined in [protocol.h](https://github.com/brpc/brpc/blob/master/src/brpc/protocol.h). Among all these callbacks, `parse` is a callback that must be implemented. Besides, `process_request` must be implemented in the server side and `serialize_request`, `pack_request`, `process_response` must be implemented in the client side.

It is difficult to implement callbacks of the protocol. These codes are not like the codes that ordinary users use which has good prompts and protections. You have to figure it out how to handle similar code in other protocols and implement your own protocol, then send it to us to do code review.

<a id="rpc-in-depth-new-protocol--parse"></a>

### parse

```c++
typedef ParseResult (*Parse)(butil::IOBuf* source, Socket *socket, bool read_eof, const void *arg);
```

This function is used to cut messages from source. Client side and server side must share the same parse function. The returned message will be passed to `process_request`(server side) or `process_response`(client side).

Argument: source is the binary content from remote side, socket is the corresponding connection, read\_eof is true iff the connection is closed by remote, arg is a pointer to the corresponding server in server client and NULL in client side.

ParseResult could be an error or a cut message, its possible value contains:

- PARSE\_ERROR\_TRY\_OTHERS: current protocol is not matched, the framework would try next protocol. The data in source cannot be comsumed.
- PARSE\_ERROR\_NOT\_ENOUGH\_DATA: the input data hasn’t violated the current protocol yet, but the whole message cannot be detected as well. When there is new data from connection, new data will be appended to source and parse function is called again. If we can determine that data fits current protocol, the content of source can also be transferred to the internal state of protocol. For example, if source doesn’t contain a whole http message, it will be consumed by http parser to avoid repeated parsing.
- PARSE\_ERROR\_TOO\_BIG\_DATA: message size is too big, the connection will be closed to protect server.
- PARSE\_ERROR\_NO\_RESOURCE: internal error, such as resource allocation failure. Connections will be closed.
- PARSE\_ERROR\_ABSOLUTELY\_WRONG: it is supposed to be some protocols(magic number is matched), but the format is not as expected. Connection will be closed.

<a id="rpc-in-depth-new-protocol--serialize_request"></a>

### serialize\_request

```c++
typedef bool (*SerializeRequest)(butil::IOBuf* request_buf,
                                 Controller* cntl,
                                 const google::protobuf::Message* request);
```

This function is used to serialize request into request\_buf that client must implement. It happens before a RPC call and will only be called once. Necessary information needed by some protocols(such as http) is contained in cntl. Return true if succeed, otherwise false.

<a id="rpc-in-depth-new-protocol--pack_request"></a>

### pack\_request

```c++
typedef int (*PackRequest)(butil::IOBuf* msg, 
                           uint64_t correlation_id,
                           const google::protobuf::MethodDescriptor* method,
                           Controller* controller,
                           const butil::IOBuf& request_buf,
                           const Authenticator* auth);
```

This function is used to pack request\_buf into msg, which is called every time before sending messages to server(including retrying). When auth is not NULL, authentication information is also needed to be packed. Return 0 if succeed, otherwise -1.

<a id="rpc-in-depth-new-protocol--process_request"></a>

### process\_request

```c++
typedef void (*ProcessRequest)(InputMessageBase* msg_base);
```

This function is used to parse request messages in the server side that server must implement. It and parse() may run in different threads. Multiple process\_request may run simultaneously. After the processing is done, msg\_base->Destroy() must be called. In order to prevent forgetting calling Destroy, consider using DestroyingPtr<>.

<a id="rpc-in-depth-new-protocol--process_response"></a>

### process\_response

```c++
typedef void (*ProcessResponse)(InputMessageBase* msg);
```

This function is used to parse message response in client side that client must implement. It and parse() may run in different threads. Multiple process\_request may run simultaneously. After the processing is done, msg\_base->Destroy() must be called. In order to prevent forgetting calling Destroy, consider using DestroyingPtr<>.

<a id="rpc-in-depth-new-protocol--verify"></a>

### verify

```c++
typedef bool (*Verify)(const InputMessageBase* msg);
```

This function is used to authenticate connections, it is called when the first message is received. It is must be implemented by servers that need authentication, otherwise the function pointer can be NULL. Return true if succeed, otherwise false.

<a id="rpc-in-depth-new-protocol--parse_server_address"></a>

### parse\_server\_address

```c++
typedef bool (*ParseServerAddress)(butil::EndPoint* out, const char* server_addr_and_port);
```

This function converts server\_addr\_and\_port(an argument of Channel.Init) to butil::EndPoint, which is optional. Some protocols may differ in the expression and understanding of server addresses.

<a id="rpc-in-depth-new-protocol--get_method_name"></a>

### get\_method\_name

```c++
typedef const std::string& (*GetMethodName)(const google::protobuf::MethodDescriptor* method,
                                            const Controller*);
```

This function is used to customize method name, which is optional.

<a id="rpc-in-depth-new-protocol--supported_connection_type"></a>

### supported\_connection\_type

Used to mark the supported connection method. If all connection methods are supported, this value should set to CONNECTION\_TYPE\_ALL. If connection pools and short connections are supported, this value should set to CONNECTION\_TYPE\_POOLED\_AND\_SHORT.

<a id="rpc-in-depth-new-protocol--name"></a>

### name

The name of the protocol, which appears in the various configurations and displays, should be as short as possible and must be a string constant.

<a id="rpc-in-depth-new-protocol--register-to-global"></a>

## Register to global

RegisterProtocol should be called to [register implemented protocol](https://github.com/brpc/brpc/blob/master/src/brpc/global.cpp) to brpc, just like:

```c++
Protocol http_protocol = { ParseHttpMessage,
                           SerializeHttpRequest, PackHttpRequest,
                           ProcessHttpRequest, ProcessHttpResponse,
                           VerifyHttpRequest, ParseHttpServerAddress,
                           GetHttpMethodName,
                           CONNECTION_TYPE_POOLED_AND_SHORT,
                           "http" };
if (RegisterProtocol(PROTOCOL_HTTP, http_protocol) != 0) {
    exit(1);
}
```

---

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="rpc-in-depth-threading-overview"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/threading-overview/ -->

<!-- page_index: 64 -->

# Threading Overview

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Threading%20Overview/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Threading%20Overview)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Connections own threads or processes exclusively](#rpc-in-depth-threading-overview--connections-own-threads-or-processes-exclusively)
- [Single-threaded [reactor](http://en.wikipedia.org/wiki/Reactor_pattern)](#rpc-in-depth-threading-overview--single-threaded-reactorhttpenwikipediaorgwikireactor_pattern)
- [N:1 threading library](#rpc-in-depth-threading-overview--n1-threading-library)
- [Multi-threaded reactor](#rpc-in-depth-threading-overview--multi-threaded-reactor)
- [M:N threading library](#rpc-in-depth-threading-overview--mn-threading-library)

- [Multi-core scalability](#rpc-in-depth-threading-overview--multi-core-scalability)
- [Asynchronous programming](#rpc-in-depth-threading-overview--asynchronous-programming)

# Threading Overview

Learn about bRPC threading.

<a id="rpc-in-depth-threading-overview--common-threading-models"></a>

# Common threading models

<a id="rpc-in-depth-threading-overview--connections-own-threads-or-processes-exclusively"></a>

## Connections own threads or processes exclusively

In this model, a thread/process handles all messages from a connection and does not quit or do other jobs before the connection is closed. When number of connections increases, resources occupied by threads/processes and costs of context switches becomes more and more overwhelming, making servers perform poorly. This situation is summarized as the [C10K](http://en.wikipedia.org/wiki/C10k_problem) problem, which was common in early web servers but rarely present today.

<a id="rpc-in-depth-threading-overview--single-threaded-reactorhttpenwikipediaorgwikireactor_pattern"></a>

## Single-threaded [reactor](http://en.wikipedia.org/wiki/Reactor_pattern)

Event-loop libraries such as [libevent](http://libevent.org/), [libev](http://software.schmorp.de/pkg/libev.html) are typical examples. There’s usually an event dispatcher in this model responsible for waiting on different kinds of events and calling the corresponding event handler **in-place** when an event occurs. After all handlers(that need to be called) are called, the dispatcher waits for more events again, which forms a “loop”. Essentially this model multiplexes(interleaves) code written in different handlers into a system thread. One event-loop can only utilize one core, so this kind of program is either IO-bound or each handler runs within short and deterministic time(such as http servers), otherwise one callback taking long time blocks the whole program and causes high delays. In practice this kind of program is not suitable for involving many developers, because just one person adding inappropriate blocking code may significantly slow down reactivities of all other code. Since event handlers don’t run simultaneously, race conditions between callbacks are relatively simple and in some scenarios locks are not needed. These programs are often scaled by using more threads or more processes.

How single-threaded reactors work and the problems related are demonstrated below: (The Chinese characters in red: “Uncontrollable! unless the service is specialized”)

![img](assets/images/threading-overview-1_bacd7141dc22fec2.png)

<a id="rpc-in-depth-threading-overview--n1-threading-library"></a>

## N:1 threading library

Also known as [Fiber](http://en.wikipedia.org/wiki/Fiber_(computer_science)). Typical examples are [GNU Pth](http://www.gnu.org/software/pth/pth-manual.html), [StateThreads](http://state-threads.sourceforge.net/index.html). This model maps N user threads into a single system thread, in which only one user thread runs at the same time and the running user thread does not switch to other user threads until a blocking primitive is called (cooperative). N:1 threading libraries are equal to single-threaded reactors on capabilities, except that callbacks are replaced by contexts (stacks, registers, signals) and running callbacks becomes jumping to contexts. Similar to event-loop libraries, a N:1 threading library cannot utilize multiple CPU cores, thus only suitable for specialized applications. However a single system thread is more friendly to CPU caches, with removal of the support for signal masks, context switches between user threads can be done very fast(100 ~ 200ns). N:1 threading libraries perform as well as event-loop libraries and are also scaled by using more threads or more processes in general.

<a id="rpc-in-depth-threading-overview--multi-threaded-reactor"></a>

## Multi-threaded reactor

[boost::asio](http://www.boost.org/doc/libs/1_56_0/doc/html/boost_asio.html) is a typical example. One or several threads run event dispatchers respectively. When an event occurs, the event handler is queued into a worker thread to run. This model is extensible from single-threaded reactor intuitively and able to make use of multiple CPU cores. Since sharing memory addresses makes interactions between threads much cheaper, the worker threads are able to balance loads between each other frequently, as a contrast multiple single-threaded reactors basically depend on the front-end servers to distribute traffic. A well-implemented multi-threaded reactor is likely to utilize CPU cores more evenly than multiple single-threaded reactors on the same machine. However, due to [cache coherence](#rpc-in-depth-atomic-instructions--cacheline), multi-threaded reactors are unlikely to achieve linear scalability on CPU cores. In particular scenarios, a badly implemented multi-threaded reactor running on 24 cores is even slower than a well-tuned single-threaded reactor. Because a multi-threaded reactor has multiple worker threads, one blocking event handler may not delay other handlers. As a result, event handlers are not required to be non-blocking unless all worker threads are blocked, in which case the overall progress is affected. In fact, most RPC frameworks are implemented in this model with event handlers that may block, such as synchronously waiting for RPCs to downstream servers.

How multi-threaded reactors work and problems related are demonstrated below:

![img](assets/images/threading-overview-2_69c319b8bab4173e.png)

<a id="rpc-in-depth-threading-overview--mn-threading-library"></a>

## M:N threading library

This model maps M user threads into N system threads. A M:N threading library is able to decide when and where to run a piece of code and when to end the execution, which is more flexible at scheduling compared to multi-threaded reactors. But full-featured M:N threading libraries are difficult to implement and remaining as active research topics. The M:N threading library that we’re talking about is specialized for building online services, in which case, some of the requirements can be simplified, namely no (complete) preemptions and priorities. M:N threading libraries can be implemented either in userland or OS kernel. New programming languages prefer implementations in userland, such as GHC thread and goroutine, which is capable of adding brand-new keywords and intercepting related APIs on threading. Implementation in existing languages often have to modify the OS kernel, such as [Windows UMS](https://msdn.microsoft.com/en-us/library/windows/desktop/dd627187(v=vs.85).aspx) and google SwicthTo(which is 1:1, however M:N effects can be achieved based on it). Compared to N:1 threading libraries, usages of M:N threading libraries are more similar to system threads, which need locks or message passings to ensure thread safety.

<a id="rpc-in-depth-threading-overview--issues"></a>

# Issues

<a id="rpc-in-depth-threading-overview--multi-core-scalability"></a>

## Multi-core scalability

Ideally capabilities of the reactor model are maximized when all source code is programmed in event-driven manner, but in reality because of the difficulties and maintainability, users are likely to mix usages: synchronous IO is often issued in callbacks, blocking worker threads from processing other requests. A request often goes through dozens of services, making worker threads spend a lot of time waiting for responses from downstream servers. Users have to launch hundreds of threads to maintain enough throughput, which imposes intensive pressure on scheduling and lowers efficiencies of TLS related code. Tasks are often pushed into a queue protected with a global mutex and condition, which performs poorly when many threads are contending for it. A better approach is to deploy more task queues and adjust the scheduling algorithm to reduce global contentions. Namely each system thread has its own runqueue, and one or more schedulers dispatch user threads to different runqueues. Each system thread runs user threads from its own runqueue before considering other runqueues, which is more complicated but more scalable than the global mutex+condition solution. This model is also easier to support NUMA.

When an event dispatcher passes a task to a worker thread, the user code probably jumps from one CPU core to another, which may need to wait for synchronizations of relevant cachelines, which is not very fast. It would be better that the worker is able to run directly on the CPU core where the event dispatcher runs, since at most of the time, priority of running the worker ASAP is higher than getting new events from the dispatcher. Similarly, it’s better to wake up the user thread blocking on RPC on the same CPU core where the response is received.

<a id="rpc-in-depth-threading-overview--asynchronous-programming"></a>

## Asynchronous programming

Flow controls in asynchronous programming are even difficult for experts. Any suspending operation such as sleeping for a while or waiting for something to finish, implies that users have to save states explicitly and restore states in callbacks. Asynchronous code is often written as state machines. A few suspensions are troublesome, but still handleable. The problem is that once the suspension occurs inside a condition, loop or sub-function, it’s almost impossible to write such a state machine being understood and maintained by many people, although the scenario is quite common in distributed systems where a node often needs to interact with multiple nodes simultaneously. In addition, if the wakeup can be triggered by more than one events (such as either fd has data or timeout is reached), the suspension and resuming are prone to race conditions, which require good multi-threaded programming skills to solve. Syntactic sugars(such as lambda) just make coding less troublesome rather than reducing difficulty.

Shared pointers are common in asynchronous programming, which seems convenient, but also makes ownerships of memory elusive. If the memory is leaked, it’s difficult to locate the code that forgot to release; if segment fault happens, where the double-free occurs is also unknown. Code with a lot of referential countings is hard to remain good-quality and may waste a lot of time on debugging memory related issues. If references are even counted manually, keeping quality of the code is harder and the maintainers are less willing to modify the code. [RAII](http://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization) cannot be used in many scenarios in asynchronous programming, sometimes resources need to be locked before a callback and unlocked inside the callback, which is very error-prone in practice.

---

Last modified August 2, 2022: [[ISSUE #82] improve doc (#83) (ebba480b6)](https://github.com/apache/brpc-website/commit/ebba480b64acbfc52e5da390b05597e95ebd1803)

---

<a id="rpc-in-depth-timer-keeping"></a>

<!-- source_url: https://brpc.apache.org/docs/rpc-in-depth/timer-keeping/ -->

<!-- page_index: 65 -->

# Timer keeping

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/RPC%20in%20depth/Timer%20keeping/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Timer%20keeping)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Timer keeping

Learn about bRPC timer keeping.

在几点几分做某件事是RPC框架的基本需求，这件事比看上去难。

让我们先来看看系统提供了些什么： posix系统能以[signal方式](http://man7.org/linux/man-pages/man2/timer_create.2.html)告知timer触发，不过signal逼迫我们使用全局变量，写[async-signal-safe](https://docs.oracle.com/cd/E19455-01/806-5257/gen-26/index.html)的函数，在面向用户的编程框架中，我们应当尽力避免使用signal。linux自2.6.27后能以[fd方式](http://man7.org/linux/man-pages/man2/timerfd_create.2.html)通知timer触发，这个fd可以放到epoll中和传输数据的fd统一管理。唯一问题是：这是个系统调用，且我们不清楚它在多线程下的表现。

为什么这么关注timer的开销?让我们先来看一下RPC场景下一般是怎么使用timer的：

- 在发起RPC过程中设定一个timer，在超时时间后取消还在等待中的RPC。几乎所有的RPC调用都有超时限制，都会设置这个timer。
- RPC结束前删除timer。大部分RPC都由正常返回的response导致结束，timer很少触发。

你注意到了么，在RPC中timer更像是”保险机制”，在大部分情况下都不会发挥作用，自然地我们希望它的开销越小越好。一个几乎不触发的功能需要两次系统调用似乎并不理想。那在应用框架中一般是如何实现timer的呢？谈论这个问题需要区分“单线程”和“多线程”:

- 在单线程框架中，比如以[libevent](http://libevent.org/)[,](http://en.wikipedia.org/wiki/Reactor_pattern) [libev](http://software.schmorp.de/pkg/libev.html)为代表的eventloop类库，或以[GNU Pth](http://www.gnu.org/software/pth/pth-manual.html), [StateThreads](http://state-threads.sourceforge.net/index.html)为代表的coroutine / fiber类库中，一般是以[小顶堆](https://en.wikipedia.org/wiki/Heap_(data_structure))记录触发时间。[epoll\_wait](http://man7.org/linux/man-pages/man2/epoll_wait.2.html)前以堆顶的时间计算出参数timeout的值，如果在该时间内没有其他事件，epoll\_wait也会醒来，从堆中弹出已超时的元素，调用相应的回调函数。整个框架周而复始地这么运转，timer的建立，等待，删除都发生在一个线程中。只要所有的回调都是非阻塞的，且逻辑不复杂，这套机制就能提供基本准确的timer。不过就像[Threading Overview](#rpc-in-depth-threading-overview)中说的那样，这不是RPC的场景。
- 在多线程框架中，任何线程都可能被用户逻辑阻塞较长的时间，我们需要独立的线程实现timer，这种线程我们叫它TimerThread。一个非常自然的做法，就是使用用锁保护的小顶堆。当一个线程需要创建timer时，它先获得锁，然后把对应的时间插入堆，如果插入的元素成为了最早的，唤醒TimerThread。TimerThread中的逻辑和单线程类似，就是等着堆顶的元素超时，如果在等待过程中有更早的时间插入了，自己会被插入线程唤醒，而不会睡过头。这个方法的问题在于每个timer都需要竞争一把全局锁，操作一个全局小顶堆，就像在其他文章中反复谈到的那样，这会触发cache bouncing。同样数量的timer操作比单线程下的慢10倍是非常正常的，尴尬的是这些timer基本不触发。

我们重点谈怎么解决多线程下的问题。

一个惯例思路是把timer的需求散列到多个TimerThread，但这对TimerThread效果不好。注意我们上面提及到了那个“制约因素”：一旦插入的元素是最早的，要唤醒TimerThread。假设TimerThread足够多，以至于每个timer都散列到独立的TimerThread，那么每次它都要唤醒那个TimerThread。 “唤醒”意味着触发linux的调度函数，触发上下文切换。在非常流畅的系统中，这个开销大约是3-5微秒，这可比抢锁和同步cache还慢。这个因素是提高TimerThread扩展性的一个难点。多个TimerThread减少了对单个小顶堆的竞争压力，但同时也引入了更多唤醒。

另一个难点是删除。一般用id指代一个Timer。通过这个id删除Timer有两种方式：1.抢锁，通过一个map查到对应timer在小顶堆中的位置，定点删除，这个map要和堆同步维护。2.通过id找到Timer的内存结构，做个标记，留待TimerThread自行发现和删除。第一种方法让插入逻辑更复杂了，删除也要抢锁，线程竞争更激烈。第二种方法在小顶堆内留了一大堆已删除的元素，让堆明显变大，插入和删除都变慢。

第三个难点是TimerThread不应该经常醒。一个极端是TimerThread永远醒着或以较高频率醒过来（比如每1ms醒一次），这样插入timer的线程就不用负责唤醒了，然后我们把插入请求散列到多个堆降低竞争，问题看似解决了。但事实上这个方案提供的timer精度较差，一般高于2ms。你得想这个TimerThread怎么写逻辑，它是没法按堆顶元素的时间等待的，由于插入线程不唤醒，一旦有更早的元素插入，TimerThread就会睡过头。它唯一能做的是睡眠固定的时间，但这和现代OS scheduler的假设冲突：频繁sleep的线程的优先级最低。在linux下的结果就是，即使只sleep很短的时间，最终醒过来也可能超过2ms，因为在OS看来，这个线程不重要。一个高精度的TimerThread有唤醒机制，而不是定期醒。

另外，更并发的数据结构也难以奏效，感兴趣的同学可以去搜索"concurrent priority queue"或"concurrent skip list"，这些数据结构一般假设插入的数值较为散开，所以可以同时修改结构内的不同部分。但这在RPC场景中也不成立，相互竞争的线程设定的时间往往聚集在同一个区域，因为程序的超时大都是一个值，加上当前时间后都差不多。

这些因素让TimerThread的设计相当棘手。由于大部分用户的qps较低，不足以明显暴露这个扩展性问题，在r31791前我们一直沿用“用一把锁保护的TimerThread”。TimerThread是brpc在默认配置下唯一的高频竞争点，这个问题是我们一直清楚的技术债。随着brpc在高qps系统中应用越来越多，是时候解决这个问题了。r31791后的TimerThread解决了上述三个难点，timer操作几乎对RPC性能没有影响，我们先看下性能差异。

> 在示例程序example/mutli\_threaded\_echo\_c++中，r31791后TimerThread相比老TimerThread在24核E5-2620上（超线程），以50个bthread同步发送时，节省4%cpu（差不多1个核），qps提升10%左右；在400个bthread同步发送时，qps从30万上升到60万。新TimerThread的表现和完全关闭超时时接近。

那新TimerThread是如何做到的？

这里勾勒了TimerThread的大致工作原理，工程实现中还有不少细节问题，具体请阅读[timer\_thread.h](https://github.com/brpc/brpc/blob/master/src/bthread/timer_thread.h)和[timer\_thread.cpp](https://github.com/brpc/brpc/blob/master/src/bthread/timer_thread.cpp)。

这个方法之所以有效：

- Bucket锁内的操作是O(1)的，就是插入一个链表节点，临界区很小。节点本身的内存分配是在锁外的。
- 由于大部分插入的时间是递增的，早于Bucket::nearest\_run\_time而参与全局竞争的timer很少。
- 参与全局竞争的timer也就是和全局nearest\_run\_time比一下，临界区很小。
- 和Bucket内类似，极少数Timer会早于全局nearest\_run\_time并去唤醒TimerThread。唤醒也在全局锁外。
- 删除不参与全局竞争。
- TimerThread自己维护小顶堆，没有任何cache bouncing，效率很高。
- TimerThread醒来的频率大约是RPC超时的倒数，比如超时=100ms，TimerThread一秒内大约醒10次，已经最优。

至此brpc在默认配置下不再有全局竞争点，在400个线程同时运行时，profiling也显示几乎没有对锁的等待。

下面是一些和linux下时间管理相关的知识：

- epoll\_wait的超时精度是毫秒，较差。pthread\_cond\_timedwait的超时使用timespec，精度到纳秒，一般是60微秒左右的延时。
- 出于性能考虑，TimerThread使用wall-time，而不是单调时间，可能受到系统时间调整的影响。具体来说，如果在测试中把系统时间往前或往后调一个小时，程序行为将完全undefined。未来可能会让用户选择单调时间。
- 在cpu支持nonstop\_tsc和constant\_tsc的机器上，brpc和bthread会优先使用基于rdtsc的cpuwide\_time\_us。那两个flag表示rdtsc可作为wall-time使用，不支持的机器上会转而使用较慢的内核时间。我们的机器（Intel Xeon系列）大都有那两个flag。rdtsc作为wall-time使用时是否会受到系统调整时间的影响，未测试不清楚。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="server-auto-concurrencylimiter"></a>

<!-- source_url: https://brpc.apache.org/docs/server/auto-concurrencylimiter/ -->

<!-- page_index: 66 -->

# Auto ConcurrencyLimiter

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Auto%20ConcurrencyLimiter/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Auto%20ConcurrencyLimiter)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [使用场景](#server-auto-concurrencylimiter--section)
- [开启方法](#server-auto-concurrencylimiter--section)
- [原理](#server-auto-concurrencylimiter--section)
  - [名词](#server-auto-concurrencylimiter--section)
  - [Little’s Law](#server-auto-concurrencylimiter--littles-law)
  - [计算公式](#server-auto-concurrencylimiter--section)
  - [估算noload\_latency](#server-auto-concurrencylimiter--noload_latency)
  - [估算peak\_qps](#server-auto-concurrencylimiter--peak_qps)
  - [与netflix gradient算法的对比](#server-auto-concurrencylimiter--netflix-gradient)

# Auto ConcurrencyLimiter

Learn how to use auto concurrency limiter in bRPC.

<a id="server-auto-concurrencylimiter--section"></a>

# 自适应限流

服务的处理能力是有客观上限的。当请求速度超过服务的处理速度时，服务就会过载。

如果服务持续过载，会导致越来越多的请求积压，最终所有的请求都必须等待较长时间才能被处理，从而使整个服务处于瘫痪状态。

与之相对的，如果直接拒绝掉一部分请求，反而能够让服务能够"及时"处理更多的请求。对应的方法就是[设置最大并发](#server-basics--limit-concurrency)。

自适应限流能动态调整服务的最大并发，在保证服务不过载的前提下，让服务尽可能多的处理请求。

<a id="server-auto-concurrencylimiter--section"></a>

## 使用场景

通常情况下要让服务不过载，只需在上线前进行压力测试，并通过little’s law计算出best\_max\_concurrency就可以了。但在服务数量多，拓扑复杂，且处理能力会逐渐变化的局面下，使用固定的最大并发会带来巨大的测试工作量，很不方便。自适应限流就是为了解决这个问题。

使用自适应限流前建议做到：

1. 客户端开启了重试功能。
2. 服务端有多个节点。

这样当一个节点返回过载时，客户端可以向其他的节点发起重试，从而尽量不丢失流量。

<a id="server-auto-concurrencylimiter--section"></a>

## 开启方法

目前只有method级别支持自适应限流。如果要为某个method开启自适应限流，只需要将它的最大并发设置为"auto"即可。

```c++
// Set auto concurrency limiter for all methods
brpc::ServerOptions options;
options.method_max_concurrency = "auto";

// Set auto concurrency limiter for specific method
server.MaxConcurrencyOf("example.EchoService.Echo") = "auto";
```

<a id="server-auto-concurrencylimiter--section"></a>

## 原理

<a id="server-auto-concurrencylimiter--section"></a>

### 名词

**concurrency**: 同时处理的请求数，又被称为“并发度”。

**max\_concurrency**: 设置的最大并发度。超过并发的请求会被拒绝（返回ELIMIT错误），在集群层面，client应重试到另一台server上去。

**best\_max\_concurrency**: 并发的物理含义是任务处理槽位，天然存在上限，这个上限就是best\_max\_concurrency。若max\_concurrency设置的过大，则concurrency可能大于best\_max\_concurrency，任务将无法被及时处理而暂存在各种队列中排队，系统也会进入拥塞状态。若max\_concurrency设置的过小，则concurrency总是会小于best\_max\_concurrency，限制系统达到本可以达到的更高吞吐。

**noload\_latency**: 单纯处理任务的延时，不包括排队时间。另一种解释是低负载的延时。由于正确处理任务得经历必要的环节，其中会耗费cpu或等待下游返回，noload\_latency是一个服务固有的属性，但可能随时间逐渐改变（由于内存碎片，压力变化，业务数据变化等因素）。

**min\_latency**: 实际测定的latency中的较小值的ema，当concurrency不大于best\_max\_concurrency时，min\_latency和noload\_latency接近(可能轻微上升）。

**peak\_qps**: qps的上限。注意是处理或回复的qps而不是接收的qps。值取决于best\_max\_concurrency / noload\_latency，这两个量都是服务的固有属性，故peak\_qps也是服务的固有属性，和拥塞状况无关，但可能随时间逐渐改变。

**max\_qps**: 实际测定的qps中的较大值。由于qps具有上限，max\_qps总是会小于peak\_qps，不论拥塞与否。

<a id="server-auto-concurrencylimiter--littles-law"></a>

### Little’s Law

在服务处于稳定状态时: concurrency = latency \* qps。 这是自适应限流的理论基础。

当服务没有超载时，随着流量的上升，latency基本稳定(接近noload\_latency)，qps和concurrency呈线性关系一起上升。

当流量超过服务的peak\_qps时，则concurrency和latency会一起上升，而qps会稳定在peak\_qps。

假如一个服务的peak\_qps和noload\_latency都比较稳定，那么它的best\_max\_concurrency = noload\_latency \* peak\_qps。

自适应限流就是要找到服务的noload\_latency和peak\_qps， 并将最大并发设置为靠近两者乘积的一个值。

<a id="server-auto-concurrencylimiter--section"></a>

### 计算公式

自适应限流会不断的对请求进行采样，当采样窗口的样本数量足够时，会根据样本的平均延迟和服务当前的qps计算出下一个采样窗口的max\_concurrency:

> max\_concurrency = max\_qps \* ((2+alpha) \* min\_latency - latency)

alpha为可接受的延时上升幅度，默认0.3。

latency是当前采样窗口内所有请求的平均latency。

max\_qps是最近一段时间测量到的qps的极大值。

min\_latency是最近一段时间测量到的latency较小值的ema，是noload\_latency的估算值。

当服务处于低负载时，min\_latency约等于noload\_latency，此时计算出来的max\_concurrency会高于concurrency，但低于best\_max\_concurrency，给流量上涨留探索空间。而当服务过载时，服务的qps约等于max\_qps，同时latency开始明显超过min\_latency，此时max\_concurrency则会接近concurrency，并通过定期衰减避免远离best\_max\_concurrency，保证服务不会过载。

<a id="server-auto-concurrencylimiter--noload_latency"></a>

### 估算noload\_latency

服务的noload\_latency并非是一成不变的，自适应限流必须能够正确的探测noload\_latency的变化。当noload\_latency下降时，是很容感知到的，因为这个时候latency也会下降。难点在于当latency上涨时，需要能够正确的辨别到底是服务过载了，还是noload\_latency上涨了。

可能的方案有：

1. 取最近一段时间的最小latency来近似noload\_latency
2. 取最近一段时间的latency的各种平均值来预测noload\_latency
3. 收集请求的平均排队等待时间，使用latency - queue\_time作为noload\_latency
4. 每隔一段时间缩小max\_concurrency，过一小段时间后以此时的latency作为noload\_latency

方案1和方案2的问题在于：假如服务持续处于高负载，那么最近的所有latency都会高出noload\_latency，从而使得算法估计的noload\_latency不断升高。

方案3的问题在于，假如服务的性能瓶颈在下游服务，那么请求在服务本身的排队等待时间无法反应整体的负载情况。

方案4是最通用的，也经过了大量实验的考验。缩小max\_concurrency和公式中的alpha存在关联。让我们做个假想实验，若latency极为稳定并都等于min\_latency，那么公式简化为max\_concurrency = max\_qps \* latency \* (1 + alpha)。根据little’s law，qps最多为max\_qps \* (1 + alpha). alpha是qps的"探索空间"，若alpha为0，则qps被锁定为max\_qps，算法可能无法探索到peak\_qps。但在qps已经达到peak\_qps时，alpha会使延时上升（已拥塞），此时测定的min\_latency会大于noload\_latency，一轮轮下去最终会导致min\_latency不收敛。定期降低max\_concurrency就是阻止这个过程，并给min\_latency下降提供"探索空间"。

<a id="server-auto-concurrencylimiter--section"></a>

#### 减少重测时的流量损失

每隔一段时间，自适应限流算法都会缩小max\_concurrency，并持续一段时间，然后将此时的latency作为服务的noload\_latency，以处理noload\_latency上涨了的情况。测量noload\_latency时，必须让先服务处于低负载的状态，因此对max\_concurrency的缩小是难以避免的。

由于max\_concurrency < concurrency时，服务会拒绝掉所有的请求，限流算法将"排空所有的经历过排队等待的请求的时间" 设置为 latency \* 2 ，以确保用于计算min\_latency的样本绝大部分都是没有经过排队等待的。

由于服务的latency通常都不会太长，这种做法所带来的流量损失也很小。

<a id="server-auto-concurrencylimiter--section"></a>

#### 应对抖动

即使服务自身没有过载，latency也会发生波动，根据Little’s Law，latency的波动会导致server的concurrency发生波动。

我们在设计自适应限流的计算公式时，考虑到了latency发生抖动的情况:
当latency与min\_latency很接近时，根据计算公式会得到一个较高max\_concurrency来适应concurrency的波动，从而尽可能的减少“误杀”。同时，随着latency的升高，max\_concurrency会逐渐降低，以保护服务不会过载。

从另一个角度来说，当latency也开始升高时，通常意味着某处(不一定是服务本身，也有可能是下游服务)消耗了大量CPU资源，这个时候缩小max\_concurrency也是合理的。

<a id="server-auto-concurrencylimiter--section"></a>

#### 平滑处理

为了减少个别窗口的抖动对限流算法的影响，同时尽量降低计算开销，计算min\_latency时会通过使用[EMA](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average)来进行平滑处理：

```
if latency > min_latency:
    min_latency = latency * ema_alpha  + (1 - ema_alpha) * min_latency
else:
    do_nothing
```

<a id="server-auto-concurrencylimiter--peak_qps"></a>

### 估算peak\_qps

<a id="server-auto-concurrencylimiter--qps"></a>

#### 提高qps增长的速度

当服务启动时，由于服务本身需要进行一系列的初始化，tcp本身也有慢启动等一系列原因。服务在刚启动时的qps一定会很低。这就导致了服务启动时的max\_concurrency也很低。而按照上面的计算公式，当max\_concurrency很低的时候，预留给qps增长的冗余concurrency也很低(即：alpha \* max\_qps \* min\_latency)。从而会影响当流量增加时，服务max\_concurrency的增加速度。

假如从启动到打满qps的时间过长，这期间会损失大量流量。在这里我们采取的措施有两个，

1. 采样方面，一旦采到的请求数量足够多，直接提交当前采样窗口，而不是等待采样窗口的到时间了才提交
2. 计算公式方面，当current\_qps > 保存的max\_qps时，直接进行更新，不进行平滑处理。

在进行了这两个处理之后，绝大部分情况下都能够在2秒左右将qps打满。

<a id="server-auto-concurrencylimiter--1"></a>

#### 平滑处理

为了减少个别窗口的抖动对限流算法的影响，同时尽量降低计算开销，在计算max\_qps时，会通过使用[EMA](https://en.wikipedia.org/wiki/Moving_average#Exponential_moving_average)来进行平滑处理：

```
if current_qps > max_qps:
    max_qps = current_qps
else: 
    max_qps = current_qps * ema_alpha / 10 + (1 - ema_alpha / 10) * max_qps
```

将max\_qps的ema参数置为min\_latency的ema参数的十分之一的原因是: max\_qps 下降了通常并不意味着极限qps也下降了。而min\_latency下降了，通常意味着noload\_latency确实下降了。

<a id="server-auto-concurrencylimiter--netflix-gradient"></a>

### 与netflix gradient算法的对比

netflix中的gradient算法公式为：max\_concurrency = min\_latency / latency \* max\_concurrency + queue\_size。

其中latency是采样窗口的最小latency，min\_latency是最近多个采样窗口的最小latency。min\_latency / latency就是算法中的"梯度"，当latency大于min\_latency时，max\_concurrency会逐渐减少；反之，max\_concurrency会逐渐上升，从而让max\_concurrency围绕在best\_max\_concurrency附近。

这个公式可以和本文的算法进行类比：

- gradient算法中的latency和本算法的不同，前者的latency是最小值，后者是平均值。netflix的原意是最小值能更好地代表noload\_latency，但实际上只要不对max\_concurrency做定期衰减，不管最小值还是平均值都有可能不断上升使算法不收敛。最小值并不能带来额外的好处，反而会使算法更不稳定。
- gradient算法中的max\_concurrency / latency从概念上和qps有关联（根据little’s law)，但可能严重脱节。比如在重测
  min\_latency前，若所有latency都小于min\_latency，那么max\_concurrency会不断下降甚至到0；但按照本算法，max\_qps和min\_latency仍然是稳定的，它们计算出的max\_concurrency也不会剧烈变动。究其本质，gradient算法在迭代max\_concurrency时，latency并不能代表实际并发为max\_concurrency时的延时，两者是脱节的，所以max\_concurrency / latency的实际物理含义不明，与qps可能差异甚大，最后导致了很大的偏差。
- gradient算法的queue\_size推荐为sqrt(max\_concurrency)，这是不合理的。netflix对queue\_size的理解大概是代表各种不可控环节的缓存，比如socket里的，和max\_concurrency存在一定的正向关系情有可原。但在我们的理解中，这部分queue\_size作用微乎其微，没有或用常量即可。我们关注的queue\_size是给concurrency上升留出的探索空间: max\_concurrency的更新是有延迟的，在并发从低到高的增长过程中，queue\_size的作用就是在max\_concurrency更新前不限制qps上升。而当concurrency高时，服务可能已经过载了，queue\_size就应该小一点，防止进一步恶化延时。这里的queue\_size和并发是反向关系。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="server-avalanche"></a>

<!-- source_url: https://brpc.apache.org/docs/server/avalanche/ -->

<!-- page_index: 67 -->

# Avalanche

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Avalanche/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Avalanche)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Avalanche

Learn how to prevent bRPC avalanche.

“雪崩”指的是访问服务集群时绝大部分请求都超时，且在流量减少时仍无法恢复的现象。下面解释这个现象的来源。

当流量超出服务的最大qps时，服务将无法正常服务；当流量恢复正常时（小于服务的处理能力），积压的请求会被处理，虽然其中很大一部分可能会因为处理的不及时而超时，但服务本身一般还是会恢复正常的。这就相当于一个水池有一个入水口和一个出水口，如果入水量大于出水量，水池子终将盛满，多出的水会溢出来。但如果入水量降到出水量之下，一段时间后水池总会排空。雪崩并不是单一服务能产生的。

如果一个请求经过两个服务，情况就有所不同了。比如请求访问A服务，A服务又访问了B服务。当B被打满时，A处的client会大量超时，如果A处的client在等待B返回时也阻塞了A的服务线程（常见），且使用了固定个数的线程池（常见），那么A处的最大qps就从**线程数 / 平均延时**，降到了**线程数 / 超时**。由于超时往往是平均延时的3至4倍，A处的最大qps会相应地下降3至4倍，从而产生比B处更激烈的拥塞。如果A还有类似的上游，拥塞会继续传递上去。但这个过程还是可恢复的。B处的流量终究由最前端的流量触发，只要最前端的流量回归正常，B处的流量总会慢慢降下来直到能正常回复大多数请求，从而让A恢复正常。

但有两个例外：

1. A可能对B发起了过于频繁的基于超时的重试。这不仅会让A的最大qps降到**线程数 / 超时**，还会让B处的qps翻**重试次数**倍。这就可能陷入恶性循环了：只要**线程数 / 超时 \* 重试次数**大于B的最大qps，B就无法恢复 -> A处的client会继续超时 -> A继续重试 -> B继续无法恢复。
2. A或B没有限制某个缓冲或队列的长度，或限制过于宽松。拥塞请求会大量地积压在那里，要恢复就得全部处理完，时间可能长得无法接受。由于有限长的缓冲或队列需要在填满时解决等待、唤醒等问题，有时为了简单，代码可能会假定缓冲或队列不会满，这就埋下了种子。即使队列是有限长的，恢复时间也可能很长，因为清空队列的过程是个追赶问题，排空的时间取决于**积压的请求数 / (最大qps - 当前qps)**，如果当前qps和最大qps差的不多，积压的请求又比较多，那排空时间就遥遥无期了。

了解这些因素后可以更好的理解brpc中相关的设计。

对于brpc的用户来说，要防止雪崩，主要注意两点：

1. 评估server的最大并发，设置合理的max\_concurrency值。这个默认是不设的，也就是不限制。无论程序是同步还是异步，用户都可以通过 **最大qps \* 非拥塞时的延时**（秒）来评估最大并发，原理见[little’s law](https://en.wikipedia.org/wiki/Little%27s_law)，这两个量都可以在brpc中的内置服务中看到。max\_concurrency与最大并发相等或大一些就行了。
2. 注意考察重试发生时的行为，特别是在定制RetryPolicy时。如果你只是用默认的brpc重试，一般是安全的。但用户程序也常会自己做重试，比如通过一个Channel访问失败后，去访问另外一个Channel，这种情况下要想清楚重试发生时最差情况下请求量会放大几倍，服务是否可承受。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="server-basics"></a>

<!-- source_url: https://brpc.apache.org/docs/server/basics/ -->

<!-- page_index: 68 -->

# Basics

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Basics/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Basics)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [Set RPC to be failed](#server-basics--set-rpc-to-be-failed)
- [Get address of client](#server-basics--get-address-of-client)
- [Get address of server](#server-basics--get-address-of-server)
- [Asynchronous Service](#server-basics--asynchronous-service)

- [Listen to multiple ports](#server-basics--listen-to-multiple-ports)
- [Multi-process listening to one port](#server-basics--multi-process-listening-to-one-port)

- [json<=>pb](#server-basics--jsonpb)
- [Adapt old clients](#server-basics--adapt-old-clients)

- [Version](#server-basics--version)
- [Close idle connections](#server-basics--close-idle-connections)
- [pid\_file](#server-basics--pid_file)
- [Print hostname in each line of log](#server-basics--print-hostname-in-each-line-of-log)
- [Crash after printing FATAL log](#server-basics--crash-after-printing-fatal-log)
- [Minimum log level](#server-basics--minimum-log-level)
- [Return free memory to system](#server-basics--return-free-memory-to-system)
- [Log error to clients](#server-basics--log-error-to-clients)
- [Customize percentiles of latency](#server-basics--customize-percentiles-of-latency)
- [Change stacksize](#server-basics--change-stacksize)
- [Limit sizes of messages](#server-basics--limit-sizes-of-messages)
- [Compression](#server-basics--compression)
- [Attachment](#server-basics--attachment)
- [Turn on SSL](#server-basics--turn-on-ssl)
- [Verify identities of clients](#server-basics--verify-identities-of-clients)
- [Number of worker pthreads](#server-basics--number-of-worker-pthreads)
- [Limit concurrency](#server-basics--limit-concurrency)
  - [Why issue error to the client instead of queuing the request when the concurrency hits limit?](#server-basics--why-issue-error-to-the-client-instead-of-queuing-the-request-when-the-concurrency-hits-limit)
  - [Why not limit QPS?](#server-basics--why-not-limit-qps)
  - [Calculate max concurrency](#server-basics--calculate-max-concurrency)
  - [Limit server-level concurrency](#server-basics--limit-server-level-concurrency)
  - [Limit method-level concurrency](#server-basics--limit-method-level-concurrency)
  - [AutoConcurrencyLimiter](#server-basics--autoconcurrencylimiter)
- [pthread mode](#server-basics--pthread-mode)
- [Security mode](#server-basics--security-mode)
  - [Hide builtin services from public](#server-basics--hide-builtin-services-from-public)
  - [Disable built-in services completely](#server-basics--disable-built-in-services-completely)
  - [Escape URLs controllable from public](#server-basics--escape-urls-controllable-from-public)
  - [Not return addresses of internal servers](#server-basics--not-return-addresses-of-internal-servers)
- [Customize /health](#server-basics--customize-health)
- [thread-local variables](#server-basics--thread-local-variables)
  - [session-local](#server-basics--session-local)
  - [server-thread-local](#server-basics--server-thread-local)
  - [bthread-local](#server-basics--bthread-local)

- - [Q: Fail to write into fd=1865 [SocketId=8905@10.208.245.43](mailto:SocketId=8905@10.208.245.43):54742@8230: Got EOF](#server-basics--q-fail-to-write-into-fd1865-socketid89051020824543547428230-got-eof)
  - [Q: Remote side of fd=9 [SocketId=2@10.94.66.55](mailto:SocketId=2@10.94.66.55):8000 was closed](#server-basics--q-remote-side-of-fd9-socketid2109466558000-was-closed)
  - [Q: Why does setting number of threads at server-side not work](#server-basics--q-why-does-setting-number-of-threads-at-server-side-not-work)
  - [Q: Why do client-side latencies much larger than the server-side ones](#server-basics--q-why-do-client-side-latencies-much-larger-than-the-server-side-ones)
  - [Q: Fail to open /proc/self/io](#server-basics--q-fail-to-open-procselfio)
  - [Q: json string “[1,2,3]” can’t be converted to protobuf message](#server-basics--q-json-string-123-cant-be-converted-to-protobuf-message)

# Basics

Learn how to use bRPC server.

<a id="server-basics--example"></a>

# Example

[server-side code](https://github.com/brpc/brpc/blob/master/example/echo_c++/server.cpp) of Echo.

<a id="server-basics--fill-the-proto"></a>

# Fill the .proto

Interfaces of requests, responses, services are defined in proto files.

```C++
# Tell protoc to generate base classes for C++ Service. modify to java_generic_services or py_generic_services for java or python. 
option cc_generic_services = true;

message EchoRequest {
      required string message = 1;
};
message EchoResponse {
      required string message = 1;
};

service EchoService {
      rpc Echo(EchoRequest) returns (EchoResponse);
};
```

Read [official documents on protobuf](https://developers.google.com/protocol-buffers/docs/proto#options) for more details about protobuf.

<a id="server-basics--implement-generated-interface"></a>

# Implement generated interface

protoc generates echo.pb.cc and echo.pb.h. Include echo.pb.h and implement EchoService inside:

```c++
#include "echo.pb.h"
...
class MyEchoService : public EchoService  {
public:
    void Echo(::google::protobuf::RpcController* cntl_base,
              const ::example::EchoRequest* request,
              ::example::EchoResponse* response,
              ::google::protobuf::Closure* done) {
        // This RAII object calls done->Run() automatically at exit.
        brpc::ClosureGuard done_guard(done);
         
        brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);
 
        // fill response
        response->set_message(request->message());
    }
};
```

Service is not available before insertion into [brpc.Server](https://github.com/brpc/brpc/blob/master/src/brpc/server.h).

When client sends request, Echo() is called.

Explain parameters:

**controller**

Statically convertible to brpc::Controller (provided that the code runs in brpc.Server). Contains parameters that can’t be included by request and response, check out [src/brpc/controller.h](https://github.com/brpc/brpc/blob/master/src/brpc/controller.h) for details.

**request**

read-only message from a client.

**response**

Filled by user. If any **required** field is not set, the RPC will fail.

**done**

Created by brpc and passed to service’s CallMethod(), including all actions after leaving CallMethod(): validating response, serialization, sending back to client etc.

**No matter the RPC is successful or not, done->Run() must be called by user once and only once when the RPC is done.**

Why does brpc not call done->Run() automatically? Because users are able to store done somewhere and call done->Run() in some event handlers after leaving CallMethod(), which is an **asynchronous service**.

We strongly recommend using **ClosureGuard** to make done->Run() always be called. Look at the beginning statement in above code snippet:

```c++
brpc::ClosureGuard done_guard(done);
```

Not matter the callback is exited from middle or end, done\_guard will be destructed, in which done->Run() is called. The mechanism is called [RAII](https://en.wikipedia.org/wiki/Resource_Acquisition_Is_Initialization). Without done\_guard, you have to remember to add done->Run() before each `return`, **which is very error-prone**.

In asynchronous service, request is not processed completely when CallMethod() returns, thus done->Run() should not be called, instead it should be preserved somewhere and called later. At first glance, we don’t need ClosureGuard here. However in real applications, asynchronous service may fail in the middle and exit CallMethod() as well. Without ClosureGuard, error branches may forget to call done->Run() before `return`. Thus done\_guard is still recommended in asynchronous services. Different from synchronous services, to prevent done->Run() from being called at successful return of CallMethod, you should call done\_guard.release() to remove done from the object.

How synchronous and asynchronous services handle done generally:

```c++
class MyFooService: public FooService  {
public:
    // Synchronous
    void SyncFoo(::google::protobuf::RpcController* cntl_base,
                 const ::example::EchoRequest* request,
                 ::example::EchoResponse* response,
                 ::google::protobuf::Closure* done) {
         brpc::ClosureGuard done_guard(done);
         ...
    }
 
    // Aynchronous
    void AsyncFoo(::google::protobuf::RpcController* cntl_base,
                  const ::example::EchoRequest* request,
                  ::example::EchoResponse* response,
                  ::google::protobuf::Closure* done) {
         brpc::ClosureGuard done_guard(done);
         ...
         done_guard.release();
    }
};
```

Interface of ClosureGuard:

```c++
// RAII: Call Run() of the closure on destruction.
class ClosureGuard {
public:
    ClosureGuard();
    // Constructed with a closure which will be Run() inside dtor.
    explicit ClosureGuard(google::protobuf::Closure* done);
    
    // Call Run() of internal closure if it's not NULL.
    ~ClosureGuard();
 
    // Call Run() of internal closure if it's not NULL and set it to `done'.
    void reset(google::protobuf::Closure* done);
 
    // Set internal closure to NULL and return the one before set.
    google::protobuf::Closure* release();
};
```

<a id="server-basics--set-rpc-to-be-failed"></a>

## Set RPC to be failed

Call Controller.SetFailed() to set the RPC to be failed. If error occurs during sending response, framework calls the method as well. Users often call the method in services’ CallMethod(), For example if a stage of processing fails, user calls SetFailed() and call done->Run(), then quit CallMethod (If ClosureGuard is used, done->Run() is called automatically). The server-side done is created by framework and contains code sending response back to client. If SetFailed() is called, error information is sent to client instead of normal content. When client receives the response, its controller will be SetFailed() as well and Controller::Failed() will be true. In addition, Controller::ErrorCode() and Controller::ErrorText() are error code and error information respectively.

User may set [status-code](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html) for http calls by calling `controller.http_response().set_status_code()` at server-side. Standard status-code are defined in [http\_status\_code.h](https://github.com/brpc/brpc/blob/master/src/brpc/http_status_code.h). Controller.SetFailed() sets status-code as well with the value closest to the error-code in semantics. brpc::HTTP\_STATUS\_INTERNAL\_SERVER\_ERROR(500) is chosen when there’s no proper value.

<a id="server-basics--get-address-of-client"></a>

## Get address of client

controller->remote\_side() gets address of the client which sent the request. The return type is butil::EndPoint. If client is nginx, remote\_side() is address of nginx. To get address of the “real” client before nginx, set `proxy_header ClientIp $remote_addr;` in nginx and call `controller->http_request().GetHeader("ClientIp")` in RPC to get the address.

Printing method:

```c++
LOG(INFO) << "remote_side=" << cntl->remote_side();
printf("remote_side=%s\n", butil::endpoint2str(cntl->remote_side()).c_str());
```

<a id="server-basics--get-address-of-server"></a>

## Get address of server

controller->local\_side() gets server-side address of the RPC connection, return type is butil::EndPoint.

Printing method:

```c++
LOG(INFO) << "local_side=" << cntl->local_side();
printf("local_side=%s\n", butil::endpoint2str(cntl->local_side()).c_str());
```

<a id="server-basics--asynchronous-service"></a>

## Asynchronous Service

In which done->Run() is called after leaving service’s CallMethod().

Some server proxies requests to back-end servers and waits for responses that may come back after a long time. To make better use of threads, save done in corresponding event handlers which are triggered after CallMethod() and call done->Run() inside. This kind of service is **asynchronous**.

Last line of asynchronous service is often `done_guard.release()` to prevent done->Run() from being called at successful exit from CallMethod(). Check out [example/session\_data\_and\_thread\_local](https://github.com/brpc/brpc/tree/master/example/session_data_and_thread_local/) for a example.

Server-side and client-side both use done to represent the continuation code after leaving CallMethod, but they’re **totally different**:

- server-side done is created by framework, called by user after processing of the request to send back response to client.
- client-side done is created by user, called by framework to run post-processing code written by user after completion of RPC.

In an asynchronous service that may access other services, user probably manipulates both kinds of done, be careful.

<a id="server-basics--add-service"></a>

# Add Service

A just default-constructed Server neither contains service nor serves requests, merely an object.

Add a service with following method:

```c++
int AddService(google::protobuf::Service* service, ServiceOwnership ownership);
```

If `ownership` is SERVER\_OWNS\_SERVICE, server deletes the service at destruction. To prevent the deletion, set `ownership` to SERVER\_DOESNT\_OWN\_SERVICE.

Following code adds MyEchoService:

```c++
brpc::Server server;
MyEchoService my_echo_service;
if (server.AddService(&my_echo_service, brpc::SERVER_DOESNT_OWN_SERVICE) != 0) {
    LOG(FATAL) << "Fail to add my_echo_service";
    return -1;
}
```

You cannot add or remove services after the server is started.

<a id="server-basics--start-server"></a>

# Start server

Call following methods of [Server](https://github.com/brpc/brpc/blob/master/src/brpc/server.h) to start serving.

```c++
int Start(const char* ip_and_port_str, const ServerOptions* opt);
int Start(EndPoint ip_and_port, const ServerOptions* opt);
int Start(int port, const ServerOptions* opt);
int Start(const char *ip_str, PortRange port_range, const ServerOptions *opt);  // r32009后增加
```

“localhost:9000”, “cq01-cos-dev00.cq01:8000”, “127.0.0.1:7000” are valid `ip_and_port_str`.

All parameters take default values if `options` is NULL. If you need non-default values, code as follows:

```c++
brpc::ServerOptions options;  // with default values
options.xxx = yyy;
...
server.Start(..., &options);
```

<a id="server-basics--listen-to-multiple-ports"></a>

## Listen to multiple ports

One server can only listen to one port (not counting ServerOptions.internal\_port). To listen to N ports, start N servers .

<a id="server-basics--multi-process-listening-to-one-port"></a>

## Multi-process listening to one port

When the `reuse_port` flag is turned on at startup, multiple processes can listen to one port (use SO\_REUSEPORT internal).

<a id="server-basics--stop-server"></a>

# Stop server

```c++
server.Stop(closewait_ms); // closewait_ms is useless actually, not deleted due to compatibility
server.Join();
```

Stop() does not block but Join() does. The reason for dividing them into two methods is: When multiple servers quit, users may Stop() all servers first, then Join() them together. Otherwise servers can only be Stop()+Join() one-by-one and the total waiting time may add up to number-of-servers times at worst.

Regardless of the value of closewait\_ms, server waits for all requests being processed before exiting and returns ELOGOFF errors to new requests immediately to prevent them from entering the service. The reason for the wait is that as long as the server is still processing requests, risk of accessing invalid(released) memory exists. If a Join() to a server “stucks”, some thread must be blocked on a request or done->Run() is not called.

When a client sees ELOGOFF, it skips the corresponding server and retry the request on another server. As a result, restarting a cluster with brpc clients/servers gradually should not lose traffic by default.

RunUntilAskedToQuit() simplifies the code to run and stop servers in most cases. Following code runs the server until Ctrl-C is pressed.

```c++
// Wait until Ctrl-C is pressed, then Stop() and Join() the server.
server.RunUntilAskedToQuit();
 
// server is stopped, write the code for releasing resources.
```

Services can be added or removed after Join() returns and server can be Start() again.

<a id="server-basics--accessed-by-httph2"></a>

# Accessed by http/h2

Services using protobuf can be accessed via http/h2+json generally. The json string stored in body is convertible to/from corresponding protobuf message.

[echo server](https://github.com/brpc/brpc/blob/master/example/echo_c%2B%2B/server.cpp) as an example, is accessible from [curl](https://curl.haxx.se/).

```shell
# -H 'Content-Type: application/json' is optional
$ curl -d '{"message":"hello"}' http://brpc.baidu.com:8765/EchoService/Echo {"message":"hello"}
```

Note: Set `Content-Type: application/proto` to access services with http/h2 + protobuf-serialized-data, which performs better at serialization.

<a id="server-basics--jsonpb"></a>

## json<=>pb

Json fields correspond to pb fields by matched names and message structures. The json must contain required fields in pb, otherwise conversion will fail and corresponding request will be rejected. The json may include undefined fields in pb, but they will be dropped rather than being stored in pb as unknown fields. Check out [json <=> protobuf](#server-json2pb) for conversion rules.

When -pb\_enum\_as\_number is turned on, enums in pb are converted to values instead of names. For example in `enum MyEnum { Foo = 1; Bar = 2; };`, fields typed `MyEnum` are converted to “Foo” or “Bar” when the flag is off, 1 or 2 otherwise. This flag affects requests sent by clients and responses returned by servers both. Since “enum as name” has better forward and backward compatibilities, this flag should only be turned on to adapt legacy code that are unable to parse enumerations from names.

<a id="server-basics--adapt-old-clients"></a>

## Adapt old clients

Early-version brpc allows pb service being accessed via http without filling the pb request, even if there’re required fields. This kind of service often parses http requests and sets http responses by itself, and does not touch the pb request. However this behavior is still very dangerous: a service with an undefined request.

This kind of services may meet issues after upgrading to latest brpc, which already deprecated the behavior for a long time. To help these services to upgrade, brpc allows bypassing the conversion from http body to pb request (so that users can parse http requests differently), the setting is as follows:

```c++
brpc::ServiceOptions svc_opt;
svc_opt.ownership = ...;
svc_opt.restful_mappings = ...;
svc_opt.allow_http_body_to_pb = false; // turn off conversion from http/h2 body to pb request
server.AddService(service, svc_opt);
```

After the setting, service does not convert the body to pb request after receiving http/h2 request, which also makes the pb request undefined. Users have to parse the body by themselves when `cntl->request_protocol() == brpc::PROTOCOL_HTTP || cntl->request_protocol() == brpc::PROTOCOL_H2` is true which indicates the request is from http/h2.

As a correspondence, if cntl->response\_attachment() is not empty and pb response is set as well, brpc does not report the ambiguous anymore, instead cntl->response\_attachment() will be used as body of the http/h2 response. This behavior is unaffected by setting allow\_http\_body\_to\_pb or not. If the relaxation results in more users’ errors, we may restrict it in future.

<a id="server-basics--protocols"></a>

# Protocols

Server detects supported protocols automatically, without assignment from users. `cntl->protocol()` gets the protocol being used. Server is able to accept connections with different protocols from one port, users don’t need to assign different ports for different protocols. Even one connection may transport messages in multiple protocols, although we rarely do this (and not recommend). Supported protocols:

- [The standard protocol used in Baidu](https://github.com/apache/brpc/blob/master/docs/cn/baidu_std.md), shown as “baidu\_std”, enabled by default.
- [Streaming RPC](#client-streaming-rpc), shown as “streaming\_rpc”, enabled by default.
- http/1.0 and http/1.1, shown as “http”, enabled by default.
- http/2 and gRPC, shown as “h2c”(unencrypted) or “h2”(encrypted), enabled by default.
- Protocol of RTMP, shown as “rtmp”, enabled by default.
- Protocol of hulu-pbrpc, shown as “hulu\_pbrpc”, enabled by default.
- Protocol of sofa-pbrpc, shown as “sofa\_pbrpc”, enabled by default.
- Protocol of Baidu ads union, shown as “nova\_pbrpc”, disabled by default. Enabling method:


```c++
#include <brpc/policy/nova_pbrpc_protocol.h>
...
ServerOptions options;
...
options.nshead_service = new brpc::policy::NovaServiceAdaptor;
```

- Protocol of public\_pbrpc, shown as “public\_pbrpc”, disabled by default. Enabling method:


```c++
#include <brpc/policy/public_pbrpc_protocol.h>
...
ServerOptions options;
...
options.nshead_service = new brpc::policy::PublicPbrpcServiceAdaptor;
```

- Protocol of nshead+mcpack, shown as “nshead\_mcpack”, disabled by default. Enabling method:


```c++
#include <brpc/policy/nshead_mcpack_protocol.h>
...
ServerOptions options;
...
options.nshead_service = new brpc::policy::NsheadMcpackAdaptor;
```

  As the name implies, messages in this protocol are composed by nshead+mcpack, the mcpack does not include special fields. Different from implementations based on NsheadService by users, this protocol uses mcpack2pb which makes the service capable of handling both mcpack and pb with one piece of code. Due to lack of fields to carry ErrorText, server can only close connections when errors occur.
- Read [Implement NsheadService](https://github.com/apache/brpc/blob/master/docs/cn/nshead_service.md) for UB related protocols.

If you need more protocols, contact us.

<a id="server-basics--fork-without-exec"></a>

# fork without exec

In general, [forked](https://linux.die.net/man/3/fork) subprocess should call [exec](https://linux.die.net/man/3/exec) ASAP, before which only async-signal-safe functions should be called. brpc programs using fork like this should work correctly even in previous versions.

But in some scenarios, users continue the subprocess without exec. Since fork only copies its caller’s thread, which causes other threads to disappear after fork. In the case of brpc, bvar depends on a sampling\_thread to sample various information, which disappears after fork and causes many bvars to be zeros.

Latest brpc re-creates the thread after fork(when necessary) to make bvar work correctly, and can be forked again. A known problem is that the cpu profiler does not work after fork. However users still can’t call fork at any time, since brpc and its applications create threads extensively, which are not re-created after fork:

- most fork continues with exec, which wastes re-creations
- bring too many troubles and complexities to the code

brpc’s strategy is to create these threads on demand and fork without exec should happen before all code that may create the threads. Specifically, **fork without exec should happen before initializing all Servers/Channels/Applications, earlier is better**. fork not obeying this causes the program dysfunctional. BTW, fork without exec better be avoided because many libraries do not support it.

<a id="server-basics--settings"></a>

# Settings

<a id="server-basics--version"></a>

## Version

Server.set\_version(…) sets name+version for the server, accessible from the builtin service `/version`. Although it’s called “version”, the string set is recommended to include the service name rather than just a numeric version.

<a id="server-basics--close-idle-connections"></a>

## Close idle connections

If a connection does not read or write within the seconds specified by ServerOptions.idle\_timeout\_sec, it’s treated as “idle” and will be closed by server soon. Default value is -1 which disables the feature.

If [-log\_idle\_connection\_close](http://brpc.baidu.com:8765/flags/log_idle_connection_close) is turned on, a log will be printed before closing.

| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| log\_idle\_connection\_close | false | Print log when an idle connection is closed | src/brpc/socket.cpp |

<a id="server-basics--pid_file"></a>

## pid\_file

If this field is non-empty, Server creates a file named so at start-up, with pid as the content. Empty by default.

<a id="server-basics--print-hostname-in-each-line-of-log"></a>

## Print hostname in each line of log

This feature only affects logging macros in [butil/logging.h](https://github.com/brpc/brpc/blob/master/src/butil/logging.h).

If [-log\_hostname](http://brpc.baidu.com:8765/flags/log_hostname) is turned on, each line of log contains the hostname so that users know machines at where each line is generated from aggregated logs.

<a id="server-basics--crash-after-printing-fatal-log"></a>

## Crash after printing FATAL log

This feature only affects logging macros in [butil/logging.h](https://github.com/brpc/brpc/blob/master/src/butil/logging.h), glog crashes for FATAL log by default.

If [-crash\_on\_fatal\_log](http://brpc.baidu.com:8765/flags/crash_on_fatal_log) is turned on, program crashes after printing LOG(FATAL) or failed assertions by CHECK\*(), and generates coredump (with proper environmental settings). Default value is false. This flag can be turned on in tests to make sure the program never hit critical errors.

> A common convention: use ERROR for tolerable errors, FATAL for unacceptable and permanent errors.

<a id="server-basics--minimum-log-level"></a>

## Minimum log level

This feature is implemented by [butil/logging.h](https://github.com/brpc/brpc/blob/master/src/butil/logging.h) and glog separately, as a same-named gflag.

Only logs with levels **not less than** the level specified by -minloglevel are printed. This flag can be modified at run-time. Correspondence between values and log levels: 0=INFO 1=NOTICE 2=WARNING 3=ERROR 4=FATAL, default value is 0.

Overhead of unprinted logs is just a “if” test and parameters are not evaluated (For example a parameter calls a function, if the log is not printed, the function is not called). Logs printed to LogSink may be filtered by the sink as well.

<a id="server-basics--return-free-memory-to-system"></a>

## Return free memory to system

Set gflag -free\_memory\_to\_system\_interval to make the program try to return free memory to system every so many seconds, values <= 0 disable the feature. Default value is 0. To turn it on, values >= 10 are recommended. This feature supports tcmalloc, thus `MallocExtension::instance()->ReleaseFreeMemory()` periodically called in your program can be replaced by setting this flag.

<a id="server-basics--log-error-to-clients"></a>

## Log error to clients

Framework does not print logs for specific client generally, because a lot of errors caused by clients may slow down server significantly due to frequent printing of logs. If you need to debug or just want the server to log all errors, turn on [-log\_error\_text](http://brpc.baidu.com:8765/flags/log_error_text).

<a id="server-basics--customize-percentiles-of-latency"></a>

## Customize percentiles of latency

Latency percentiles showed are **80** (was 50 before), 90, 99, 99.9, 99.99 by default. The first 3 ones can be changed by gflags -bvar\_latency\_p1, -bvar\_latency\_p2, -bvar\_latency\_p3 respectively。

Following are correct settings:

```shell
-bvar_latency_p3=97   # p3 is changed from default 99 to 97
-bvar_latency_p1=60 -bvar_latency_p2=80 -bvar_latency_p3=95
```

Following are wrong settings:

```shell
-bvar_latency_p3=100   # the value must be inside [1,99] inclusive，otherwise gflags fails to parse
-bvar_latency_p1=-1    # ^
```

<a id="server-basics--change-stacksize"></a>

## Change stacksize

brpc server runs code in bthreads with stacksize=1MB by default, while stacksize of pthreads is 10MB. It’s possible that programs running normally on pthreads may meet stack overflow on bthreads.

Set following gflags to enlarge the stacksize.

```shell
--stack_size_normal=10000000  # sets stacksize to roughly 10MB
--tc_stack_normal=1           # sets number of stacks cached by each worker pthread to prevent reusing from global pool each time, default value is 8
```

NOTE: It does mean that coredump of programs is likely to be caused by “stack overflow” on bthreads. We’re talking about this simply because it’s easy and quick to verify this factor and exclude the possibility.

<a id="server-basics--limit-sizes-of-messages"></a>

## Limit sizes of messages

To protect servers and clients, when a request received by a server or a response received by a client is too large, the server or client rejects the message and closes the connection. The limit is controlled by [-max\_body\_size](http://brpc.baidu.com:8765/flags/max_body_size), in bytes.

An error log is printed when a message is too large and rejected:

```
FATAL: 05-10 14:40:05: * 0 src/brpc/input_messenger.cpp:89] A message from 127.0.0.1:35217(protocol=baidu_std) is bigger than 67108864 bytes, the connection will be closed. Set max_body_size to allow bigger messages
```

protobuf has [similar limits](https://github.com/google/protobuf/blob/master/src/google/protobuf/io/coded_stream.h#L364) and the error log is as follows:

```
FATAL: 05-10 13:35:02: * 0 google/protobuf/io/coded_stream.cc:156] A protocol message was rejected because it was too big (more than 67108864 bytes). To increase the limit (or to disable these warnings), see CodedInputStream::SetTotalBytesLimit() in google/protobuf/io/coded_stream.h.
```

brpc removes the restriction from protobuf and controls the limit by -max\_body\_size solely: as long as the flag is large enough, messages will not be rejected and error logs will not be printed. This feature works for all versions of protobuf.

<a id="server-basics--compression"></a>

## Compression

`set_response_compress_type()` sets compression method for the response, no compression by default.

Attachment is not compressed. Check [here](#server-serve-httph2--compress-the-response-body) for compression of HTTP body.

Supported compressions:

- brpc::CompressTypeSnappy : [snanpy](http://google.github.io/snappy/), compression and decompression are very fast, but compression ratio is low.
- brpc::CompressTypeGzip : [gzip](http://en.wikipedia.org/wiki/Gzip), significantly slower than snappy, with a higher compression ratio.
- brpc::CompressTypeZlib : [zlib](http://en.wikipedia.org/wiki/Zlib), 10%~20% faster than gzip but still significantly slower than snappy, with slightly better compression ratio than gzip.

Read [Client-Compression](#client-basics--compression) for more comparisons.

<a id="server-basics--attachment"></a>

## Attachment

baidu\_std and hulu\_pbrpc supports attachments which are sent along with messages and set by users to bypass serialization of protobuf. From a server’s perspective, data set in Controller.response\_attachment() will be received by the client while Controller.request\_attachment() contains attachment sent from the client.

Attachment is not compressed by framework.

In http, attachment corresponds to [message body](http://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html), namely the data to post to client is stored in response\_attachment().

<a id="server-basics--turn-on-ssl"></a>

## Turn on SSL

Update openssl to the latest version before turning on SSL, since older versions of openssl may have severe security problems and support less encryption algorithms, which is against with the purpose of using SSL. Setup `ServerOptions.ssl_options` to turn on SSL. Refer to [ssl\_options.h](https://github.com/brpc/brpc/blob/master/src/brpc/ssl_options.h) for more details.

```c++
// Certificate structure
struct CertInfo {
    // Certificate in PEM format.
    // Note that CN and alt subjects will be extracted from the certificate,
    // and will be used as hostnames. Requests to this hostname (provided SNI
    // extension supported) will be encrypted using this certifcate.
    // Supported both file path and raw string
    std::string certificate;

    // Private key in PEM format.
    // Supported both file path and raw string based on prefix:
    std::string private_key;

    // Additional hostnames besides those inside the certificate. Wildcards
    // are supported but it can only appear once at the beginning (i.e. *.xxx.com).
    std::vector<std::string> sni_filters;
};

// SSL options at server side
struct ServerSSLOptions {
    // Default certificate which will be loaded into server. Requests
    // without hostname or whose hostname doesn't have a corresponding
    // certificate will use this certificate. MUST be set to enable SSL.
    CertInfo default_cert;
    
    // Additional certificates which will be loaded into server. These
    // provide extra bindings between hostnames and certificates so that
    // we can choose different certificates according to different hostnames.
    // See `CertInfo' for detail.
    std::vector<CertInfo> certs;
    
    // When set, requests without hostname or whose hostname can't be found in
    // any of the cerficates above will be dropped. Otherwise, `default_cert'
    // will be used.
    // Default: false
    bool strict_sni;
 
    // ... Other options
};
```

<a id="server-basics--verify-identities-of-clients"></a>

## Verify identities of clients

The server needs to implement `Authenticator` to enable verifications:

```c++
class Authenticator {
public:
    // Implement this method to verify credential information `auth_str' from
    // `client_addr'. You can fill credential context (result) into `*out_ctx'
    // and later fetch this pointer from `Controller'.
    // Returns 0 on success, error code otherwise
    virtual int VerifyCredential(const std::string& auth_str,
                                 const base::EndPoint& client_addr,
                                 AuthContext* out_ctx) const = 0;
    }; 

class AuthContext {
public:
    const std::string& user() const;
    const std::string& group() const;
    const std::string& roles() const;
    const std::string& starter() const;
    bool is_service() const;
};
```

The authentication is connection-specific. When server receives the first request from a connection, it tries to parse related information inside (such as auth field in baidu\_std, Authorization header in HTTP), and call `VerifyCredential` along with address of the client. If the method returns 0, which indicates success, user can put verified information into `AuthContext` and access it via `controller->auth_context()` later, whose lifetime is managed by framework. Otherwise the authentication is failed and the connection will be closed, which makes the client-side fail as well.

Subsequent requests are treated as already verified without authenticating overhead.

Assigning an instance of implemented `Authenticator` to `ServerOptions.auth` enables authentication. The instance must be valid during lifetime of the server.

<a id="server-basics--number-of-worker-pthreads"></a>

## Number of worker pthreads

Controlled by `ServerOptions.num_threads` , number of cpu cores by default(including HT).

> [!TIP]
> **hint**
> NOTE: ServerOptions.num\_threads is just a .

Don’t think that Server uses exactly so many workers because all servers and channels in one process share worker pthreads. Total number of threads is the maximum of all ServerOptions.num\_threads and bthread\_concurrency. For example, a program has 2 servers with num\_threads=24 and 36 respectively, and bthread\_concurrency is 16. Then the number of worker pthreads is max (24, 36, 16) = 36, which is different from other RPC implementations which do summations generally.

Channel does not have a corresponding option, but user can change number of worker pthreads at client-side by setting gflag -bthread\_concurrency.

In addition, brpc **does not separate “IO” and “processing” threads**. brpc knows how to assemble IO and processing code together to achieve better concurrency and efficiency.

<a id="server-basics--limit-concurrency"></a>

## Limit concurrency

“Concurrency” may have 2 meanings: one is number of connections, another is number of requests processed simultaneously. Here we’re talking about the latter one.

In traditional synchronous servers, max concurreny is limited by number of worker pthreads. Setting number of workers also limits concurrency. But brpc processes new requests in bthreads and M bthreads are mapped to N workers (M > N generally), synchronous server may have a concurrency higher than number of workers. On the other hand, although concurrency of asynchronous server is not limited by number of workers in principle, we need to limit it by other factors sometimes.

brpc can limit concurrency at server-level and method-level. When number of requests processed by the server or method simultaneously would exceed the limit, server responds the client with **brpc::ELIMIT** directly instead of invoking the service. A client seeing ELIMIT should retry another server (by best efforts). This options avoids over-queuing of requests at server-side and limits related resources.

Disabled by default.

<a id="server-basics--why-issue-error-to-the-client-instead-of-queuing-the-request-when-the-concurrency-hits-limit"></a>

### Why issue error to the client instead of queuing the request when the concurrency hits limit?

A server reaching max concurrency does not mean that other servers in the same cluster reach the limit as well. Let client be aware of the error ASAP and try another server is a better strategy from a cluster view.

<a id="server-basics--why-not-limit-qps"></a>

### Why not limit QPS?

QPS is a second-level metric, which is not good at limiting sudden request bursts. Max concurrency is closely related to availability of critical resources: number of “workers” or “slots” etc, thus better at preventing over-queuing.

In addition, when a server has stable latencies, limiting concurrency has similar effect as limiting QPS due to little’s law. But the former one is much easier to implement: simple additions and minuses from a counter representing the concurrency. This is also the reason than most flow control is implemented by limiting concurrency rather than QPS. For example the window in TCP is a kind of concurrency.

<a id="server-basics--calculate-max-concurrency"></a>

### Calculate max concurrency

max\_concurrency = peak\_qps \* noload\_latency ([little’s law](https://en.wikipedia.org/wiki/Little%27s_law))

peak\_qps is the maximum of Queries-Per-Second.
noload\_latency is the average latency measured in a server without pushing to its limit(with an acceptable latency).
peak\_qps and nolaod\_latency can be measured in pre-online performance tests and multiplied to calculate the max\_concurrency.

<a id="server-basics--limit-server-level-concurrency"></a>

### Limit server-level concurrency

Set ServerOptions.max\_concurrency. Default value is 0 which means not limited. Accesses to builtin services are not limited by this option.

Call Server.ResetMaxConcurrency() to modify max\_concurrency of the server after starting.

<a id="server-basics--limit-method-level-concurrency"></a>

### Limit method-level concurrency

server.MaxConcurrencyOf("…") = … sets max\_concurrency of the method. Possible settings:

```c++
server.MaxConcurrencyOf("example.EchoService.Echo") = 10;
server.MaxConcurrencyOf("example.EchoService", "Echo") = 10;
server.MaxConcurrencyOf(&service, "Echo") = 10;
```

The code is generally put **after AddService, before Start() of the server**. When a setting fails(namely the method does not exist), server will fail to start and notify user to fix settings on MaxConcurrencyOf.

When method-level and server-level max\_concurrency are both set, framework checks server-level first, then the method-level one.

NOTE: No service-level max\_concurrency.

<a id="server-basics--autoconcurrencylimiter"></a>

### AutoConcurrencyLimiter

max\_concurrency may change over time and measuring and setting max\_concurrency for all services before each deployment are probably very troublesome and impractical.

AutoConcurrencyLimiter addresses on this issue by limiting concurrency for methods. To use the algorithm, set max\_concurrency of the method to “auto”.

```c++
// Set auto concurrency limiter for all methods
brpc::ServerOptions options;
options.method_max_concurrency = "auto";

// Set auto concurrency limiter for specific method
server.MaxConcurrencyOf("example.EchoService.Echo") = "auto";
```

Read [this](#server-auto-concurrencylimiter) to know more about the algorithm.

<a id="server-basics--pthread-mode"></a>

## pthread mode

User code(client-side done, server-side CallMethod) runs in bthreads with 1MB stacksize by default. But some of them cannot run in bthreads:

- JNI code checks stack layout and cannot be run in bthreads.
- The user code extensively use pthread-local to pass session-level data across functions. If there’s a synchronous RPC call or function calls that may block bthread, the resumed bthread may land on a different pthread which does not have the pthread-local data that users expect to have. As a contrast, although tcmalloc uses pthread(or LWP)-local as well, the code inside has nothing to do with bthread, which is safe.

brpc offers pthread mode to solve the issues. When **-usercode\_in\_pthread** is turned on, user code will be run in pthreads. Functions that would block bthreads block pthreads.

Note: With -usercode\_in\_pthread on, brpc::thread\_local\_data() does not guarantee to return valid value.

Performance issues when pthread mode is on:

- Since synchronous RPCs block worker pthreads, server often needs more workers (ServerOptions.num\_threads), and scheduling efficiencies will be slightly lower.
- User code still runs in special bthreads actually, which use stacks of pthread workers. These special bthreads are scheduled same with normal bthreads and performance differences are negligible.
- bthread supports an unique feature: yield pthread worker to a newly created bthread to reduce a context switch. brpc client uses this feature to reduce number of context switches in one RPC from 3 to 2. In a performance-demanding system, reducing context-switches improves performance. However pthread-mode is not capable of doing this.
- Number of threads in pthread-mode is a hard limit. Once all threads are occupied, requests will be queued rapidly and many of them will be timed-out finally. An example: When many requests to downstream servers are timedout, the upstream services may also be severely affected by a lot of blocking threads waiting for responses(within timeout). Consider setting ServerOptions.max\_concurrency to protect the server when pthread-mode is on. As a contrast, number of bthreads in bthread mode is a soft limit and reacts more smoothly to such kind of issues.

pthread-mode lets legacy code to try brpc more easily, but we still recommend refactoring the code with bthread-local or even remove TLS gradually, to turn off the option in future.

<a id="server-basics--security-mode"></a>

## Security mode

If requests are from public(including being proxied by nginx etc), you have to be aware of some security issues.

<a id="server-basics--hide-builtin-services-from-public"></a>

### Hide builtin services from public

Builtin services are useful, on the other hand include a lot of internal information and shouldn’t be exposed to public. There’re multiple methods to hide builtin services from public:

- Set internal port. Set ServerOptions.internal\_port to a port which can **only be accessible from internal**. You can view builtin services via internal\_port, while accesses from the public port (the one passed to Server.Start) should see following error:


```
[a27eda84bcdeef529a76f22872b78305] Not allowed to access builtin services, try ServerOptions.internal_port=... instead if you're inside internal network
```

- http proxies only proxy specified URLs. nginx etc is able to configure how to map different URLs to back-end servers. For example the configure below maps public traffic to /MyAPI to `/ServiceName/MethodName` of `target-server`. If builtin services like /status are accessed from public, nginx rejects the attempts directly.

```nginx
  location /MyAPI {
      ...
      proxy_pass http://<target-server>/ServiceName/MethodName$query_string   # $query_string is a nginx varible, check out http://nginx.org/en/docs/http/ngx_http_core_module.html for more.
      ...
  }
```

**Don’t turn on** -enable\_dir\_service and -enable\_threads\_service on public services. Although they’re convenient for debugging, they also expose too many information on the server. The script to check if the public service has enabled the options:

```shell
curl -s -m 1 <HOSTNAME>:<PORT>/flags/enable_dir_service,enable_threads_service | awk '{if($3=="false"){++falsecnt}else if($3=="Value"){isrpc=1}}END{if(isrpc!=1||falsecnt==2){print "SAFE"}else{print "NOT SAFE"}}'
```

<a id="server-basics--disable-built-in-services-completely"></a>

### Disable built-in services completely

Set ServerOptions.has\_builtin\_services = false, you can completely disable the built-in services.

<a id="server-basics--escape-urls-controllable-from-public"></a>

### Escape URLs controllable from public

brpc::WebEscape() escapes url to prevent injection attacks with malice.

<a id="server-basics--not-return-addresses-of-internal-servers"></a>

### Not return addresses of internal servers

Consider returning signatures of the addresses. For example after setting ServerOptions.internal\_port, addresses in error information returned by server is replaced by their MD5 signatures.

<a id="server-basics--customize-health"></a>

## Customize /health

/health returns “OK” by default. If the content on /health needs to be customized: inherit [HealthReporter](https://github.com/brpc/brpc/blob/master/src/brpc/health_reporter.h) and implement code to generate the page (like implementing other http services). Assign an instance to ServerOptions.health\_reporter, which is not owned by server and must be valid during lifetime of the server. Users may return richer healthy information according to application requirements.

<a id="server-basics--thread-local-variables"></a>

## thread-local variables

Searching services inside Baidu use [thread-local storage](https://en.wikipedia.org/wiki/Thread-local_storage) (TLS) extensively. Some of them cache frequently used objects to reduce repeated creations, some of them pass contexts to global functions implicitly. You should avoid the latter usage as much as possible. Such functions cannot even run without TLS, being hard to test. brpc provides 3 mechanisms to solve issues related to thread-local storage.

<a id="server-basics--session-local"></a>

### session-local

A session-local data is bound to a **server-side RPC**: from entering CallMethod of the service, to calling the server-side done->Run(), no matter the service is synchronous or asynchronous. All session-local data are reused as much as possible and not deleted before stopping the server.

After setting ServerOptions.session\_local\_data\_factory, call Controller.session\_local\_data() to get a session-local data. If ServerOptions.session\_local\_data\_factory is unset, Controller.session\_local\_data() always returns NULL.

If ServerOptions.reserved\_session\_local\_data is greater than 0, Server creates so many data before serving.

**Example**

```c++
struct MySessionLocalData {
    MySessionLocalData() : x(123) {}
    int x;
};

class EchoServiceImpl : public example::EchoService {
public:
    ...
    void Echo(google::protobuf::RpcController* cntl_base,
              const example::EchoRequest* request,
              example::EchoResponse* response,
              google::protobuf::Closure* done) {
        ...
        brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);

        // Get the session-local data which is created by ServerOptions.session_local_data_factory
        // and reused between different RPC.
        MySessionLocalData* sd = static_cast<MySessionLocalData*>(cntl->session_local_data());
        if (sd == NULL) {
            cntl->SetFailed("Require ServerOptions.session_local_data_factory to be set with a correctly implemented instance");
            return;
        }
        ...
```

```c++
struct ServerOptions {
    ...
    // The factory to create/destroy data attached to each RPC session.
    // If this field is NULL, Controller::session_local_data() is always NULL.
    // NOT owned by Server and must be valid when Server is running.
    // Default: NULL
    const DataFactory* session_local_data_factory;

    // Prepare so many session-local data before server starts, so that calls
    // to Controller::session_local_data() get data directly rather than
    // calling session_local_data_factory->Create() at first time. Useful when
    // Create() is slow, otherwise the RPC session may be blocked by the
    // creation of data and not served within timeout.
    // Default: 0
    size_t reserved_session_local_data;
};
```

session\_local\_data\_factory is typed [DataFactory](https://github.com/brpc/brpc/blob/master/src/brpc/data_factory.h). You have to implement CreateData and DestroyData inside.

NOTE: CreateData and DestroyData may be called by multiple threads simultaneously. Thread-safety is a must.

```c++
class MySessionLocalDataFactory : public brpc::DataFactory {
public:
    void* CreateData() const {
        return new MySessionLocalData;
    }
    void DestroyData(void* d) const {
        delete static_cast<MySessionLocalData*>(d);
    }
};

MySessionLocalDataFactory g_session_local_data_factory;

int main(int argc, char* argv[]) {
    ...

    brpc::Server server;
    brpc::ServerOptions options;
    ...
    options.session_local_data_factory = &g_session_local_data_factory;
    ...
```

<a id="server-basics--server-thread-local"></a>

### server-thread-local

A server-thread-local is bound to **a call to service’s CallMethod**, from entering service’s CallMethod, to leaving the method. All server-thread-local data are reused as much as possible and will not be deleted before stopping the server. server-thread-local is implemented as a special bthread-local.

After setting ServerOptions.thread\_local\_data\_factory, call brpc::thread\_local\_data() to get a thread-local. If ServerOptions.thread\_local\_data\_factory is unset, brpc::thread\_local\_data() always returns NULL.

If ServerOptions.reserved\_thread\_local\_data is greater than 0, Server creates so many data before serving.

**Differences with session-local**

session-local data is got from server-side Controller, server-thread-local can be got globally from any function running directly or indirectly inside a thread created by the server.

session-local and server-thread-local are similar in a synchronous service, except that the former one has to be created from a Controller. If the service is asynchronous and the data needs to be accessed from done->Run(), session-local is the only option, because server-thread-local is already invalid after leaving service’s CallMethod.

**Example**

```c++
struct MyThreadLocalData {
    MyThreadLocalData() : y(0) {}
    int y;
};

class EchoServiceImpl : public example::EchoService {
public:
    ...
    void Echo(google::protobuf::RpcController* cntl_base,
              const example::EchoRequest* request,
              example::EchoResponse* response,
              google::protobuf::Closure* done) {
        ...
        brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);

        // Get the thread-local data which is created by ServerOptions.thread_local_data_factory
        // and reused between different threads.
        // "tls" is short for "thread local storage".
        MyThreadLocalData* tls = static_cast<MyThreadLocalData*>(brpc::thread_local_data());
        if (tls == NULL) {
            cntl->SetFailed("Require ServerOptions.thread_local_data_factory "
                            "to be set with a correctly implemented instance");
            return;
        }
        ...
```

```c++
struct ServerOptions {
    ...
    // The factory to create/destroy data attached to each searching thread
    // in server.
    // If this field is NULL, brpc::thread_local_data() is always NULL.
    // NOT owned by Server and must be valid when Server is running.
    // Default: NULL
    const DataFactory* thread_local_data_factory;

    // Prepare so many thread-local data before server starts, so that calls
    // to brpc::thread_local_data() get data directly rather than calling
    // thread_local_data_factory->Create() at first time. Useful when Create()
    // is slow, otherwise the RPC session may be blocked by the creation
    // of data and not served within timeout.
    // Default: 0
    size_t reserved_thread_local_data;
};
```

thread\_local\_data\_factory is typed [DataFactory](https://github.com/brpc/brpc/blob/master/src/brpc/data_factory.h). You need to implement CreateData and DestroyData inside.

NOTE: CreateData and DestroyData may be called by multiple threads simultaneously. Thread-safety is a must.

```c++
class MyThreadLocalDataFactory : public brpc::DataFactory {
public:
    void* CreateData() const {
        return new MyThreadLocalData;
    }
    void DestroyData(void* d) const {
        delete static_cast<MyThreadLocalData*>(d);
    }
};

MyThreadLocalDataFactory g_thread_local_data_factory;

int main(int argc, char* argv[]) {
    ...

    brpc::Server server;
    brpc::ServerOptions options;
    ...
    options.thread_local_data_factory  = &g_thread_local_data_factory;
    ...
```

<a id="server-basics--bthread-local"></a>

### bthread-local

Session-local and server-thread-local are enough for most servers. However, in some cases, we need a more general thread-local solution. In which case, you can use bthread\_key\_create, bthread\_key\_destroy, bthread\_getspecific, bthread\_setspecific etc, which are similar to [pthread equivalence](http://linux.die.net/man/3/pthread_key_create).

These functions support both bthread and pthread. When they are called in bthread, bthread private variables are returned; When they are called in pthread, pthread private variables are returned. Note that the “pthread private” here is not created by pthread\_key\_create, pthread-local created by pthread\_key\_create cannot be got by bthread\_getspecific. \_\_thread in GCC and thread\_local in c++11 etc cannot be got by bthread\_getspecific as well.

Since brpc creates a bthread for each request, the bthread-local in the server behaves specially: a bthread created by server does not delete bthread-local data at exit, instead it returns the data to a pool in the server for later reuse. This prevents bthread-local from constructing and destructing frequently along with creation and destroying of bthreads. This mechanism is transparent to users.

**Main interfaces**

```c++
// Create a key value identifying a slot in a thread-specific data area.
// Each thread maintains a distinct thread-specific data area.
// `destructor', if non-NULL, is called with the value associated to that key
// when the key is destroyed. `destructor' is not called if the value
// associated is NULL when the key is destroyed.
// Returns 0 on success, error code otherwise.
extern int bthread_key_create(bthread_key_t* key, void (*destructor)(void* data));
 
// Delete a key previously returned by bthread_key_create().
// It is the responsibility of the application to free the data related to
// the deleted key in any running thread. No destructor is invoked by
// this function. Any destructor that may have been associated with key
// will no longer be called upon thread exit.
// Returns 0 on success, error code otherwise.
extern int bthread_key_delete(bthread_key_t key);
 
// Store `data' in the thread-specific slot identified by `key'.
// bthread_setspecific() is callable from within destructor. If the application
// does so, destructors will be repeatedly called for at most
// PTHREAD_DESTRUCTOR_ITERATIONS times to clear the slots.
// NOTE: If the thread is not created by brpc server and lifetime is
// very short(doing a little thing and exit), avoid using bthread-local. The
// reason is that bthread-local always allocate keytable on first call to
// bthread_setspecific, the overhead is negligible in long-lived threads,
// but noticeable in shortly-lived threads. Threads in brpc server
// are special since they reuse keytables from a bthread_keytable_pool_t
// in the server.
// Returns 0 on success, error code otherwise.
// If the key is invalid or deleted, return EINVAL.
extern int bthread_setspecific(bthread_key_t key, void* data);
 
// Return current value of the thread-specific slot identified by `key'.
// If bthread_setspecific() had not been called in the thread, return NULL.
// If the key is invalid or deleted, return NULL.
extern void* bthread_getspecific(bthread_key_t key);
```

**How to use**

Create a bthread\_key\_t which represents a kind of bthread-local variable.

Use bthread\_[get|set]specific to get and set bthread-local variables. First-time access to a bthread-local variable from a bthread returns NULL.

Delete a bthread\_key\_t after no thread is using bthread-local associated with the key. If a bthread\_key\_t is deleted during usage, related bthread-local data are leaked.

```c++
static void my_data_destructor(void* data) {
    ...
}

bthread_key_t tls_key;

if (bthread_key_create(&tls_key, my_data_destructor) != 0) {
    LOG(ERROR) << "Fail to create tls_key";
    return -1;
}
```

```c++
// in some thread ...
MyThreadLocalData* tls = static_cast<MyThreadLocalData*>(bthread_getspecific(tls_key));
if (tls == NULL) {  // First call to bthread_getspecific (and before any bthread_setspecific) returns NULL
    tls = new MyThreadLocalData;   // Create thread-local data on demand.
    CHECK_EQ(0, bthread_setspecific(tls_key, tls));  // set the data so that next time bthread_getspecific in the thread returns the data.
}
```

**Example**

```c++
static void my_thread_local_data_deleter(void* d) {
    delete static_cast<MyThreadLocalData*>(d);
}

class EchoServiceImpl : public example::EchoService {
public:
    EchoServiceImpl() {
        CHECK_EQ(0, bthread_key_create(&_tls2_key, my_thread_local_data_deleter));
    }
    ~EchoServiceImpl() {
        CHECK_EQ(0, bthread_key_delete(_tls2_key));
    };
    ...
private:
    bthread_key_t _tls2_key;
}

class EchoServiceImpl : public example::EchoService {
public:
    ...
    void Echo(google::protobuf::RpcController* cntl_base,
              const example::EchoRequest* request,
              example::EchoResponse* response,
              google::protobuf::Closure* done) {
        ...
        // You can create bthread-local data for your own.
        // The interfaces are similar with pthread equivalence:
        //   pthread_key_create  -> bthread_key_create
        //   pthread_key_delete  -> bthread_key_delete
        //   pthread_getspecific -> bthread_getspecific
        //   pthread_setspecific -> bthread_setspecific
        MyThreadLocalData* tls2 = static_cast<MyThreadLocalData*>(bthread_getspecific(_tls2_key));
        if (tls2 == NULL) {
            tls2 = new MyThreadLocalData;
            CHECK_EQ(0, bthread_setspecific(_tls2_key, tls2));
        }
        ...
```

<a id="server-basics--faq"></a>

# FAQ

<a id="server-basics--q-fail-to-write-into-fd1865-socketid89051020824543547428230-got-eof"></a>

### Q: Fail to write into fd=1865 [SocketId=8905@10.208.245.43](mailto:SocketId=8905@10.208.245.43):54742@8230: Got EOF

A: The client-side probably uses pooled or short connections, and closes the connection after RPC timedout, when server writes back response, it finds that the connection has been closed and reports this error. “Got EOF” just means the server has received EOF (remote side closes the connection normally). If the client side uses single connection, server rarely reports this error.

<a id="server-basics--q-remote-side-of-fd9-socketid2109466558000-was-closed"></a>

### Q: Remote side of fd=9 [SocketId=2@10.94.66.55](mailto:SocketId=2@10.94.66.55):8000 was closed

It’s not an error, it’s a common warning representing that remote side has closed the connection(EOF). This log might be useful for debugging problems.

Disabled by default. Set gflag -log\_connection\_close to true to enable it. ([modify at run-time](#builtin-services-flags--change-gflag-on-the-fly) is supported)

<a id="server-basics--q-why-does-setting-number-of-threads-at-server-side-not-work"></a>

### Q: Why does setting number of threads at server-side not work

All brpc servers in one process [share worker pthreads](#server-basics--number-of-worker-pthreads), If multiple servers are created, number of worker pthreads is probably the maxmium of their ServerOptions.num\_threads.

<a id="server-basics--q-why-do-client-side-latencies-much-larger-than-the-server-side-ones"></a>

### Q: Why do client-side latencies much larger than the server-side ones

server-side worker pthreads may not be enough and requests are significantly delayed. Read [Server debugging](#server-debug-server-issues) for steps on debugging server-side issues quickly.

<a id="server-basics--q-fail-to-open-procselfio"></a>

### Q: Fail to open /proc/self/io

Some kernels do not provide this file. Correctness of the service is unaffected, but following bvars are not updated:

```
process_io_read_bytes_second
process_io_write_bytes_second
process_io_read_second
process_io_write_second
```

<a id="server-basics--q-json-string-123-cant-be-converted-to-protobuf-message"></a>

### Q: json string “[1,2,3]” can’t be converted to protobuf message

This is not a valid json string, which must be a json object enclosed with braces {}.

<a id="server-basics--psworkflow-at-server-side"></a>

# PS:Workflow at server-side

![img](assets/images/server-side_d6930e1fe1851414.png)

---

Last modified January 10, 2023: [Remove incubator (#122) (7647361c1)](https://github.com/apache/brpc-website/commit/7647361c1abc7392bf245411dab7863ec0a2d667)

---

<a id="server-debug-server-issues"></a>

<!-- source_url: https://brpc.apache.org/docs/server/debug-server-issues/ -->

<!-- page_index: 69 -->

# Debug server issues

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Debug%20server%20issues/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Debug%20server%20issues)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [3.1 Locate cpu-bound problem](#server-debug-server-issues--31-locate-cpu-bound-problem)
- [3.2 Locate io-bound problem](#server-debug-server-issues--32-locate-io-bound-problem)
  - [exclude the suspect of working threads are not enough](#server-debug-server-issues--exclude-the-suspect-of-working-threads-are-not-enough)
  - [exclude the suspect of lock](#server-debug-server-issues--exclude-the-suspect-of-lock)
  - [use rpcz](#server-debug-server-issues--use-rpcz)
- [Use bvar](#server-debug-server-issues--use-bvar)
  - [Use brpc client only](#server-debug-server-issues--use-brpc-client-only)

# Debug server issues

Learn how to debug server issues.

<a id="server-debug-server-issues--1-check-the-number-of-worker-threads"></a>

# 1. Check the number of worker threads

Check **/vars/bthread\_worker\_count** and **/vars/bthread\_worker\_usage**, which is the number of worker threads in total and being used, respectively.

> The number of usage and count being close means that worker threads are not enough.

For example, there are 24 worker threads in the following figure, among which 23.93 worker threads are being used, indicating all the worker threads are full of jobs and not enough.

![img](assets/images/full-worker-usage_a8d2119acd86377b.png)

There are 2.36 worker threads being used in the following figure. Apparently the worker threads are enough.

![img](assets/images/normal-worker-usage_07441e50acc11e55.png)

These two figures can be seen directly by putting /vars/bthread\_worker\_count;bthread\_worker\_usage?expand after service url, just like [this](http://brpc.baidu.com:8765/vars/bthread_worker_count;bthread_worker_usage?expand).

<a id="server-debug-server-issues--2-check-cpu-usage"></a>

# 2. Check CPU usage

Check /vars/system\_core\_**count** and /vars/process\_cpu\_**usage**, which is the number of cpu core available and being used, respectively.

> The number of usage and count being close means that cpus are enough.

In the following figure the number of cores is 24, while the number of cores being used is 20.9, which means CPU is bottleneck.

![img](assets/images/high-cpu-usage_17f6f539fc272840.png)

The number of cores being used in the figure below is 2.06, then CPU is sufficient.

![img](assets/images/normal-cpu-usage_ad021970cb19f32d.png)

<a id="server-debug-server-issues--3-locate-problems"></a>

# 3. Locate problems

The number of process\_cpu\_usage being close to bthread\_worker\_usage means it is a cpu-bound program and worker threads are doing calculations in most of the time.

The number of process\_cpu\_usage being much less than bthread\_worker\_usage means it is an io-bound program and worker threads are blocking in most of the time.

(1 - process\_cpu\_usage / bthread\_worker\_usage) is the time ratio that spent on blocking. For example, if process\_cpu\_usage = 2.4, bthread\_worker\_usage = 18.5, then worker threads spent 87.1% of time on blocking.

<a id="server-debug-server-issues--31-locate-cpu-bound-problem"></a>

## 3.1 Locate cpu-bound problem

The possible reason may be the poor performance of single server or uneven distribution to upstreams.

<a id="server-debug-server-issues--exclude-the-suspect-of-uneven-distribution-to-upstreams"></a>

### exclude the suspect of uneven distribution to upstreams

Enter qps at [vars]((<http://brpc.baidu.com:8765/vars>) page of different services to check whether qps is as expected, just like this:

![img](assets/images/bthread-creation-qps_42e846de1460cc8a.png)

Or directly visit using curl in command line, like this:

```shell
$ curl brpc.baidu.com:8765/vars/*qps* bthread_creation_qps : 95 rpc_server_8765_example_echo_service_echo_qps : 57
```

If the distribution of different machines is indeed uneven and difficult to solve, [Limit concurrency](#server-basics--limit-concurrency) can be considered to use.

<a id="server-debug-server-issues--improve-performance-of-single-server"></a>

### Improve performance of single server

Please use [CPU profiler](#builtin-services-cpu_profiler) to analyze hot spots of the program and use data to guide optimization. Generally speaking, some big and obvious hot spots can be found in a cpu-bound program.

<a id="server-debug-server-issues--32-locate-io-bound-problem"></a>

## 3.2 Locate io-bound problem

The possible reason:

- working threads are not enough.
- the client that visits downstream servers doesn’t support bthread and the latency is too long.
- blocking that caused by internal locks, IO, etc.

If blocking is inevitable, please consider asynchronous method.

<a id="server-debug-server-issues--exclude-the-suspect-of-working-threads-are-not-enough"></a>

### exclude the suspect of working threads are not enough

If working threads are not enough, you can try to dynamically adjust the number of threads. Switch to the /flags page and click the (R) in the right of bthread\_concurrency:

![img](assets/images/bthread-concurrency-1_3656d2a29e90ab2c.png)

Just enter the new thread number and confirm:

![img](assets/images/bthread-concurrency-2_063a0477b1e1875f.png)

Back to the /flags page, you can see that bthread\_concurrency has become the new value.

![img](assets/images/bthread-concurrency-3_d01bc192e9b731ae.png)

However, adjusting the number of threads may not be useful. If the worker threads are largely blocked by visiting downstreams, it is useless to adjust the thread number since the real bottleneck is in the back-end and adjusting the thread number to a larger value just make the blocking time of each thread become longer.

For example, in our example, the worker threads are still full of work after the thread number is resized.

![img](assets/images/full-worker-usage-2_4b7dce1ecd8cd312.png)

<a id="server-debug-server-issues--exclude-the-suspect-of-lock"></a>

### exclude the suspect of lock

If the program is blocked by some lock, it can also present features of io-bound. First use [contention profiler](https://brpc.apache.org/docs/builtin-services/contention_profiler) to check the contention status of locks.

<a id="server-debug-server-issues--use-rpcz"></a>

### use rpcz

rpcz can help you see all the recent requests and the time(us) spent in each phase while processing them.

![img](assets/images/rpcz_2a469b944380ee5d.png)

Click on a span link to see when the RPC started, the spent time in each phase and when it ended.

![img](assets/images/rpcz-2_70a25ee374008dc3.png)

This is a typical example that server is blocked severely. It takes 20ms from receiving the request to starting running, indicating that the server does not have enough worker threads to get the job done in time.

For now the information of this span is less, we can add some in the program. You can use TRACEPRINTF print logs to rpcz. Printed content is embedded in the time stream of rpcz.

![img](assets/images/trace-printf_fbac705c1c47e2cb.png)

After Re-running, you can check the span and it really contains the content we added by TRACEPRINTF.

![img](assets/images/rpcz-3_134b53eeebfe0523.png)

Before running to the first TRACEPRINTF, the user callback has already run for 2051ms(suppose it meets our expectation), followed by foobar() that took 8036ms, which is expected to return very fast. The range has been further reduced.

Repeat this process until you find the function that caused the problem.

<a id="server-debug-server-issues--use-bvar"></a>

## Use bvar

TRACEPRINTF is mainly suitable for functions that called several times, so if a function is called many times, or the function itself has a small overhead, it is not appropriate to print logs to rpcz every time. You can use bvar instead.

[bvar](#bvar-bvar) is a multi-threaded counting library, which can record the value passed from user at an extreme low cost and almost does not affect the program behavior compared to logging.

Follow the code below to monitor the runtime of foobar.

```c++
#include <butil/time.h>
#include <bvar/bvar.h>
 
bvar::LatencyRecorder g_foobar_latency("foobar");
 
...
void search() {
    ...
    butil::Timer tm;
    tm.start();
    foobar();
    tm.stop();
    g_foobar_latency << tm.u_elapsed();
    ...
}
```

After rerunning the program, enter foobar in the search box of vars. The result is shown as below:

![img](assets/images/foobar-bvar_a429a3eb30477b16.png)

Click on a bvar and you can see a dynamic figure. For example, after clicking on cdf:

![img](assets/images/foobar-latency-cdf_9140b88c7c6f3fef.png)

Depending on the distribution of delays, you can infer the overall behavior of this function, how it behaves for most requests and how it behaves for long tails.

You can continue this process in the subroutine, add more bvar, compare the different distributions, and finally locate the source.

<a id="server-debug-server-issues--use-brpc-client-only"></a>

### Use brpc client only

You have to open the dummy server to provide built-in services, see [here](#client-dummy-server).

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="server"></a>

<!-- source_url: https://brpc.apache.org/docs/server/ -->

<!-- page_index: 70 -->

# Server

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Server)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Server

Learn how to use bRPC server.

---

##### [Basics](#server-basics)

Learn how to use bRPC server.

##### [Serve http:h2](#server-serve-httph2)

Learn how to serve Http2.

##### [Serve gRPC](#server-serve-grpc)

Learn how to serve gRPC.

##### [Serve thrift](#server-serve-thrift)

Learn how to serve thrift.

##### [Serve Nshead](#server-serve-nshead)

Learn how to serve nshead.

##### [Server push](#server-server-push)

Learn how to server push.

##### [Avalanche](#server-avalanche)

Learn how to prevent bRPC avalanche.

##### [Debug server issues](#server-debug-server-issues)

Learn how to debug server issues.

##### [Auto ConcurrencyLimiter](#server-auto-concurrencylimiter)

Learn how to use auto concurrency limiter in bRPC.

##### [Media Server](#server-media-server)

Learn about media server.

##### [json2pb](#server-json2pb)

Learn how to transfer json to pb.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="server-json2pb"></a>

<!-- source_url: https://brpc.apache.org/docs/server/json2pb/ -->

<!-- page_index: 71 -->

# json2pb

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/json2pb/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=json2pb)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [message](#server-json2pb--message)
- [repeated field](#server-json2pb--repeated-field)
- [map](#server-json2pb--map)
- [integers](#server-json2pb--integers)
- [floating point](#server-json2pb--floating-point)
- [enum](#server-json2pb--enum)
- [string](#server-json2pb--string)
- [bytes](#server-json2pb--bytes)
- [bool](#server-json2pb--bool)
- [unknown fields](#server-json2pb--unknown-fields)

# json2pb

Learn how to transfer json to pb.

brpc支持json和protobuf间的**双向**转化，实现于[json2pb](https://github.com/brpc/brpc/tree/master/src/json2pb/)，json解析使用[rapidjson](https://github.com/miloyip/rapidjson)。此功能对pb2.x和3.x均有效。pb3内置了[转换json](https://developers.google.com/protocol-buffers/docs/proto3#json)的功能。

by design, 通过HTTP + json访问protobuf服务是对外服务的常见方式，故转化必须精准，转化规则列举如下。

<a id="server-json2pb--message"></a>

## message

对应rapidjson Object, 以花括号包围，其中的元素会被递归地解析。

```protobuf
// protobuf
message Foo {
    required string field1 = 1;
    required int32 field2 = 2;  
}
message Bar { 
    required Foo foo = 1; 
    optional bool flag = 2;
    required string name = 3;
}

// rapidjson
{"foo":{"field1":"hello", "field2":3},"name":"Tom" }
```

<a id="server-json2pb--repeated-field"></a>

## repeated field

对应rapidjson Array, 以方括号包围，其中的元素会被递归地解析，和message不同，每个元素的类型相同。

```protobuf
// protobuf
repeated int32 numbers = 1;

// rapidjson
{"numbers" : [12, 17, 1, 24] }
```

特别的，针对仅有一个 `repeated` 类型成员的 `message`，序列化为 `json` 时支持直接序列化为数组，以简化包体。

```protobuf
// protobuf
message Foo {
    required int32 numbers = 1;
}
// rapidjson
[12, 17, 1, 24]
```

该特性默认为关闭状态，客户端在发送请求时，或服务端在发送回复时，可手动开启：

```c++
brpc::Controller cntl;
cntl.set_pb_single_repeated_to_array(true);
```

<a id="server-json2pb--map"></a>

## map

满足如下条件的repeated MSG被视作json map :

- MSG包含一个名为key的字段，类型为string，tag为1。
- MSG包含一个名为value的字段，tag为2。
- 不包含其他字段。

这种"map"的属性有：

- 自然不能确保key有序或不重复，用户视需求自行检查。
- 与protobuf 3.x中的map二进制兼容，故3.x中的map使用pb2json也会正确地转化为json map。

如果符合所有条件的repeated MSG并不需要被认为是json map，打破上面任一条件就行了: 在MSG中加入optional int32 this\_message\_is\_not\_map\_entry = 3; 这个办法破坏了“不包含其他字段”这项，且不影响二进制兼容。也可以调换key和value的tag值，让前者为2后者为1，也使条件不再满足。

<a id="server-json2pb--integers"></a>

## integers

rapidjson会根据值打上对应的类型标记，比如：

- 对于3，rapidjson中的IsUInt, IsInt, IsUint64, IsInt64等函数均会返回true。
- 对于-1，则IsUInt和IsUint64会返回false。
- 对于5000000000，IsUInt和IsInt是false。

这使得我们不用特殊处理，转化代码就可以自动地把json中的UInt填入protobuf中的int64，而不是机械地认为这两个类型不匹配。相应地，转化代码自然能识别overflow和underflow，当出现时会转化失败。

```protobuf
// protobuf
int32 uint32 int64 uint64

// rapidjson
Int UInt Int64 UInt64
```

<a id="server-json2pb--floating-point"></a>

## floating point

json的整数类型也可以转至pb的浮点数类型。浮点数(IEEE754)除了普通数字外还接受"NaN", “Infinity”, “-Infinity"三个字符串，分别对应Not A Number，正无穷，负无穷。

```protobuf
// protobuf
float double

// rapidjson
Float Double Int Uint Int64 Uint64
```

<a id="server-json2pb--enum"></a>

## enum

enum可转化为整数或其名字对应的字符串，可由Pb2JsonOptions.enum\_options控制。默认后者。

<a id="server-json2pb--string"></a>

## string

默认同名转化。但当json中出现非法C++变量名（pb的变量名规则）时，允许转化，规则是:

`illegal-char <-> **_Z**<ASCII-of-the-char>**_**`

<a id="server-json2pb--bytes"></a>

## bytes

和string不同，可能包含\0的bytes默认以base64编码。

```protobuf
// protobuf
"Hello, World!"

// json
"SGVsbG8sIFdvcmxkIQo="
```

<a id="server-json2pb--bool"></a>

## bool

对应json的true false

<a id="server-json2pb--unknown-fields"></a>

## unknown fields

unknown\_fields → json目前不支持，未来可能支持。json → unknown\_fields目前也未支持，即protobuf无法透传json中不认识的字段。原因在于protobuf真正的key是proto文件中每个字段后的数字:

```protobuf
...
required int32 foo = 3; <-- the real key
...
```

这也是unknown\_fields的key。当一个protobuf不认识某个字段时，其proto中必然不会有那个数字，所以没办法插入unknown\_fields。

可行的方案有几种：

- 确保被json访问的服务的proto文件最新。这样就不需要透传了，但越前端的服务越类似proxy，可能并不现实。
- protobuf中定义特殊透传字段。比如名为unknown\_json\_fields，在解析对应的protobuf时特殊处理。此方案修改面广且对性能有一定影响，有明确需求时再议。

---

Last modified June 13, 2022: [update getting\_start and json2pb docs (#73) (b6b734ea7)](https://github.com/apache/brpc-website/commit/b6b734ea718b3e1e0480b1ef945f6228413126b4)

---

<a id="server-media-server"></a>

<!-- source_url: https://brpc.apache.org/docs/server/media-server/ -->

<!-- page_index: 72 -->

# Media Server

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Media%20Server/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Media%20Server)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Media Server

Learn about media server.

See [media-server](https://github.com/brpc/media-server).

---

Last modified January 9, 2022: [A new verion of brpc website based on hugo (94b25d711)](https://github.com/apache/brpc-website/commit/94b25d7110944f3d4b2071b5188c691b23ffe3a9)

---

<a id="server-serve-grpc"></a>

<!-- source_url: https://brpc.apache.org/docs/server/serve-grpc/ -->

<!-- page_index: 73 -->

# Serve gRPC

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Serve%20gRPC/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Serve%20gRPC)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Serve gRPC

Learn how to serve gRPC.

Basics for accessing and serving http/h2 in brpc are listed in [http\_client](#client-access-httph2) and [http\_service](#server-serve-httph2).

Following section names are protocol names that can be directly set to ChannelOptions.protocol. The content after colon is parameters for the protocol to select derivative behaviors dynamically, but the base protocol is still http/1.x or http/2. As a result, these protocols are displayed at server-side as http or h2/h2c only.

<a id="server-serve-grpc--httpjson-h2json"></a>

# http:json, h2:json

Non-empty pb request is serialized to json and set to the body of the http/h2 request. The Controller.request\_attachment() must be empty otherwise the RPC fails.

Non-empty pb response is converted from a json which is parsed from the body of the http/h2 response.

http/1.x behaves in this way by default, so “http” and “http:json” are just same.

<a id="server-serve-grpc--httpproto-h2proto"></a>

# http:proto, h2:proto

Non-empty pb request is serialized (in pb’s wire format) and set to the body of the http/h2 request. The Controller.request\_attachment() must be empty otherwise the RPC fails.

Non-empty pb response is parsed from the body of the http/h2 response(in pb’s wire format).

http/2 behaves in this way by default, so “h2” and “h2:proto” are just same.

<a id="server-serve-grpc--h2grpc"></a>

# h2:grpc

Default protocol of [gRPC](https://github.com/grpc). The detailed format is described in [gRPC over HTTP2](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md).

Clients using brpc should be able to talk with gRPC after changing ChannelOptions.protocol to “h2:grpc”.

Servers using brpc should be accessible by gRPC clients automatically without changing the code.

gRPC serializes message into pb wire format by default, so “h2:grpc” and “h2:grpc+proto” are just same.

TODO: Other configurations for gRPC

<a id="server-serve-grpc--h2grpcjson"></a>

# h2:grpc+json

Comparing to h2:grpc, this protocol serializes messages into json instead of pb, which may not be supported by gRPC directly. For example, grpc-go users may reference [here](https://github.com/johanbrandhorst/grpc-json-example/blob/master/codec/json.go) to register the corresponding codec and turn on the support.

---

Last modified February 26, 2022: [brpc website 1.0 fix links jump problem in overview page (14eec1ac1)](https://github.com/apache/brpc-website/commit/14eec1ac1805c1dde9f10d0353984bde2127294c)

---

<a id="server-serve-httph2"></a>

<!-- source_url: https://brpc.apache.org/docs/server/serve-httph2/ -->

<!-- page_index: 74 -->

# Serve http:h2

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Serve%20http:h2/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Serve%20http:h2)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [/ServiceName/MethodName as the prefix](#server-serve-httph2--servicenamemethodname-as-the-prefix)
- [/ServiceName as the prefix](#server-serve-httph2--servicename-as-the-prefix)
- [Restful URL](#server-serve-httph2--restful-url)

- [HTTP headers](#server-serve-httph2--http-headers)
- [Content-Type](#server-serve-httph2--content-type)
- [Status Code](#server-serve-httph2--status-code)
- [Query String](#server-serve-httph2--query-string)

- - [Q: The nginx before brpc encounters final fail](#server-serve-httph2--q-the-nginx-before-brpc-encounters-final-fail)
  - [Q: Does brpc support http chunked mode](#server-serve-httph2--q-does-brpc-support-http-chunked-mode)
  - [Q: Why do HTTP requests containing BASE64 encoded query string fail to parse sometimes?](#server-serve-httph2--q-why-do-http-requests-containing-base64-encoded-query-string-fail-to-parse-sometimes)

# Serve http:h2

Learn how to serve Http2.

This document talks about ordinary htt/h2 services rather than protobuf services accessible via http/h2.
http/h2 services in brpc have to declare interfaces with empty request and response in a .proto file. This requirement keeps all service declarations inside proto files rather than scattering in code, configurations, and proto files.

<a id="server-serve-httph2--example"></a>

# Example

[http\_server.cpp](https://github.com/brpc/brpc/blob/master/example/http_c++/http_server.cpp)

<a id="server-serve-httph2--about-h2"></a>

# About h2

brpc names the HTTP/2 protocol to “h2”, no matter encrypted or not. However HTTP/2 connections without SSL are shown on /connections with the official name “h2c”, and the ones with SSL are shown as “h2”.

The APIs for http and h2 in brpc are basically same. Without explicit statement, mentioned http features work for h2 as well.

<a id="server-serve-httph2--url-types"></a>

# URL types

<a id="server-serve-httph2--servicenamemethodname-as-the-prefix"></a>

## /ServiceName/MethodName as the prefix

Define a service named `ServiceName`(not including the package name), with a method named `MethodName` and empty request/response, the service will provide http/h2 service on `/ServiceName/MethodName` by default.

The reason that request and response can be empty is that all data are in Controller:

- Header of the http/h2 request is in Controller.http\_request() and the body is in Controller.request\_attachment().
- Header of the http/h2 response is in Controller.http\_response() and the body is in Controller.response\_attachment().

Implementation steps:

1. Add the service declaration in a proto file.

```protobuf
option cc_generic_services = true;
 
message HttpRequest { };
message HttpResponse { };
 
service HttpService {
      rpc Echo(HttpRequest) returns (HttpResponse);
};
```

2. Implement the service by inheriting the base class generated in .pb.h, which is same as protobuf services.

```c++
class HttpServiceImpl : public HttpService {
public:
    ...
    virtual void Echo(google::protobuf::RpcController* cntl_base,
                      const HttpRequest* /*request*/,
                      HttpResponse* /*response*/,
                      google::protobuf::Closure* done) {
        brpc::ClosureGuard done_guard(done);
        brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);
 
        // body is plain text
        cntl->http_response().set_content_type("text/plain");
       
        // Use printed query string and body as the response.
        butil::IOBufBuilder os;
        os << "queries:";
        for (brpc::URI::QueryIterator it = cntl->http_request().uri().QueryBegin();
                it != cntl->http_request().uri().QueryEnd(); ++it) {
            os << ' ' << it->first << '=' << it->second;
        }
        os << "\nbody: " << cntl->request_attachment() << '\n';
        os.move_to(cntl->response_attachment());
    }
};
```

3. After adding the implemented instance into the server, the service is accessible via following URLs (Note that the path after `/HttpService/Echo` is filled into `cntl->http_request().unresolved_path()`, which is always normalized):

| URL | Protobuf Method | cntl->http\_request().uri().path() | cntl->http\_request().unresolved\_path() |
| --- | --- | --- | --- |
| /HttpService/Echo | HttpService.Echo | “/HttpService/Echo” | "" |
| /HttpService/Echo/Foo | HttpService.Echo | “/HttpService/Echo/Foo” | “Foo” |
| /HttpService/Echo/Foo/Bar | HttpService.Echo | “/HttpService/Echo/Foo/Bar” | “Foo/Bar” |
| /HttpService//Echo///Foo// | HttpService.Echo | “/HttpService//Echo///Foo//” | “Foo” |
| /HttpService | No such method |  |  |

<a id="server-serve-httph2--servicename-as-the-prefix"></a>

## /ServiceName as the prefix

http/h2 services for managing resources may need this kind of URL, such as `/FileService/foobar.txt` represents `./foobar.txt` and `/FileService/app/data/boot.cfg` represents `./app/data/boot.cfg`.

Implementation steps:

1. Use `FileService` as the service name and `default_method` as the method name in the proto file.

```protobuf
option cc_generic_services = true;

message HttpRequest { };
message HttpResponse { };

service FileService {
      rpc default_method(HttpRequest) returns (HttpResponse);
}
```

2. Implement the service.

```c++
class FileServiceImpl: public FileService {
public:
    ...
    virtual void default_method(google::protobuf::RpcController* cntl_base,
                                const HttpRequest* /*request*/,
                                HttpResponse* /*response*/,
                                google::protobuf::Closure* done) {
        brpc::ClosureGuard done_guard(done);
        brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);
        cntl->response_attachment().append("Getting file: ");
        cntl->response_attachment().append(cntl->http_request().unresolved_path());
    }
};
```

3. After adding the implemented instance into the server, the service is accessible via following URLs (the path after `/FileService` is filled in `cntl->http_request().unresolved_path()`, which is always normalized):

| URL | Protobuf Method | cntl->http\_request().uri().path() | cntl->http\_request().unresolved\_path() |
| --- | --- | --- | --- |
| /FileService | FileService.default\_method | “/FileService” | "" |
| /FileService/123.txt | FileService.default\_method | “/FileService/123.txt” | “123.txt” |
| /FileService/mydir/123.txt | FileService.default\_method | “/FileService/mydir/123.txt” | “mydir/123.txt” |
| /FileService//mydir///123.txt// | FileService.default\_method | “/FileService//mydir///123.txt//” | “mydir/123.txt” |

<a id="server-serve-httph2--restful-url"></a>

## Restful URL

brpc supports specifying a URL for each method in a service. The API is as follows:

```c++
// If `restful_mappings' is non-empty, the method in service can
// be accessed by the specified URL rather than /ServiceName/MethodName.
// Mapping rules: "PATH1 => NAME1, PATH2 => NAME2 ..."
// where `PATH' is a valid path and `NAME' is the method name.
int AddService(google::protobuf::Service* service,
               ServiceOwnership ownership,
               butil::StringPiece restful_mappings);
```

`QueueService` defined below contains several methods. If the service is added into the server normally, it’s accessible via URLs like `/QueueService/start` and `/QueueService/stop`.

```protobuf
service QueueService {
    rpc start(HttpRequest) returns (HttpResponse);
    rpc stop(HttpRequest) returns (HttpResponse);
    rpc get_stats(HttpRequest) returns (HttpResponse);
    rpc download_data(HttpRequest) returns (HttpResponse);
};
```

By specifying the 3rd parameter `restful_mappings` to `AddService`, the URL can be customized:

```c++
if (server.AddService(&queue_svc,
                      brpc::SERVER_DOESNT_OWN_SERVICE,
                      "/v1/queue/start   => start,"
                      "/v1/queue/stop    => stop,"
                      "/v1/queue/stats/* => get_stats") != 0) {
    LOG(ERROR) << "Fail to add queue_svc";
    return -1;
}
 
if (server.AddService(&queue_svc,
                      brpc::SERVER_DOESNT_OWN_SERVICE,
                      "/v1/*/start   => start,"
                      "/v1/*/stop    => stop,"
                      "*.data        => download_data") != 0) {
    LOG(ERROR) << "Fail to add queue_svc";
    return -1;
}
```

There are 3 mappings separated by comma in the 3rd parameter (which is a string spanning 3 lines) to the `AddService`. Each mapping tells brpc to call the method at right side of the arrow if the left side matches the URL. The asterisk in `/v1/queue/stats/*` matches any string.

More about mapping rules:

- Multiple paths can be mapped to a same method.
- Both http/h2 and protobuf services are supported.
- Un-mapped methods are still accessible via `/ServiceName/MethodName`. Mapped methods are **not** accessible via `/ServiceName/MethodName` anymore.
- `==>` and `===>` are both OK, namely extra spaces at the beginning or the end, extra slashes, extra commas at the end, are all accepted.
- Pattern `PATH` and `PATH/*` can coexist.
- Support suffix matching: characters can appear after the asterisk.
- At most one asterisk is allowed in a path.

The path after asterisk can be obtained by `cntl.http_request().unresolved_path()`, which is always normalized, namely no slashes at the beginning or the end, and no repeated slashes in the middle. For example:

![img](assets/images/restful-1_cef893003eacb50f.png)

or:

![img](assets/images/restful-2_5dddbdb6d7756c5b.png)

in which unresolved\_path are both `foo/bar`. The extra slashes at the left, the right, or the middle are removed.

Note that `cntl.http_request().uri().path()` is not ensured to be normalized, which is `"//v1//queue//stats//foo///bar//////"` and `"//vars///foo////bar/////"` respectively in the above example.

The built-in service page of `/status` shows customized URLs after the methods, in form of `@URL1 @URL2` …

![img](assets/images/restful-3_c1a98488ed09b9bb.png)

<a id="server-serve-httph2--http-parameters"></a>

# HTTP Parameters

<a id="server-serve-httph2--http-headers"></a>

## HTTP headers

HTTP headers are a series of key/value pairs, some of them are defined by the HTTP specification, while others are free to use.

Query strings are also key/value pairs. Differences between HTTP headers and query strings:

- Although operations on HTTP headers are accurately defined by the http specification, but http headers cannot be modified directly from an address bar, they are often used for passing parameters of a protocol or framework.
- Query strings is part of the URL and **often** in form of `key1=value1&key2=value2&...`, which is easy to read and modify. They’re often used for passing application-level parameters. However format of query strings is not defined in HTTP spec, just a convention.

```c++
// Get value for header "User-Agent" (case insensitive)
const std::string* user_agent_str = cntl->http_request().GetHeader("User-Agent");
if (user_agent_str != NULL) {  // has the header
    LOG(TRACE) << "User-Agent is " << *user_agent_str;
}
...
 
// Add a header "Accept-encoding: gzip" (case insensitive)
cntl->http_response().SetHeader("Accept-encoding", "gzip");
// Overwrite the previous header "Accept-encoding: deflate"
cntl->http_response().SetHeader("Accept-encoding", "deflate");
// Append value to the previous header so that it becomes
// "Accept-encoding: deflate,gzip" (values separated by comma)
cntl->http_response().AppendHeader("Accept-encoding", "gzip");
```

<a id="server-serve-httph2--content-type"></a>

## Content-Type

`Content-type` is a frequently used header for storing type of the HTTP body, and specially processed in brpc and accessible by `cntl->http_request().content_type()` . As a correspondence, `cntl->GetHeader("Content-Type")` returns nothing.

```c++
// Get Content-Type
if (cntl->http_request().content_type() == "application/json") {
    ...
}
...
// Set Content-Type
cntl->http_response().set_content_type("text/html");
```

If the RPC fails (`Controller` has been `SetFailed`), the framework overwrites `Content-Type` with `text/plain` and sets the response body with `Controller::ErrorText()`.

<a id="server-serve-httph2--status-code"></a>

## Status Code

Status code is a special field in HTTP response to store processing result of the http request. Possible values are defined in [http\_status\_code.h](https://github.com/brpc/brpc/blob/master/src/brpc/http_status_code.h).

```c++
// Get Status Code
if (cntl->http_response().status_code() == brpc::HTTP_STATUS_NOT_FOUND) {
    LOG(FATAL) << "FAILED: " << controller.http_response().reason_phrase();
}
...
// Set Status code
cntl->http_response().set_status_code(brpc::HTTP_STATUS_INTERNAL_SERVER_ERROR);
cntl->http_response().set_status_code(brpc::HTTP_STATUS_INTERNAL_SERVER_ERROR, "My explanation of the error...");
```

For example, following code implements redirection with status code 302:

```c++
cntl->http_response().set_status_code(brpc::HTTP_STATUS_FOUND);
cntl->http_response().SetHeader("Location", "http://bj.bs.bae.baidu.com/family/image001(4979).jpg");
```

![img](assets/images/302_286f8e51cd6d1c07.png)

<a id="server-serve-httph2--query-string"></a>

## Query String

As mentioned in above [HTTP headers](#server-serve-httph2--http-headers), query strings are interpreted in common convention, whose form is `key1=value1&key2=value2&…`. Keys without values are acceptable as well and accessible by `GetQuery` which returns an empty string. Such keys are often used as boolean flags. Full API are defined in [uri.h](https://github.com/brpc/brpc/blob/master/src/brpc/uri.h).

```c++
const std::string* time_value = cntl->http_request().uri().GetQuery("time");
if (time_value != NULL) {  // the query string is present
    LOG(TRACE) << "time = " << *time_value;
}

...
cntl->http_request().uri().SetQuery("time", "2015/1/2");
```

<a id="server-serve-httph2--debugging"></a>

# Debugging

Turn on [-http\_verbose](http://brpc.baidu.com:8765/flags/http_verbose) to print contents of all http requests and responses. Note that this should only be used for debugging rather than online services.

<a id="server-serve-httph2--compress-the-response-body"></a>

# Compress the response body

HTTP services often compress http bodies to reduce transmission latency of web pages and speed up the presentations to end users.

Call `Controller::set_response_compress_type(brpc::COMPRESS_TYPE_GZIP)` to **try to** compress the http body with gzip. “Try to” means the compression may not happen in following conditions:

- The request does not set `Accept-encoding` or the value does not contain “gzip”. For example, curl does not support compression without option `--compressed`, in which case the server always returns uncompressed results.
- Body size is less than the bytes specified by -http\_body\_compress\_threshold (512 by default). gzip is not a very fast compression algorithm. When the body is small, the delay added by compression may be larger than the time saved by network transmission. No compression when the body is relatively small is probably a better choice.


| Name | Value | Description | Defined At |
| --- | --- | --- | --- |
| http\_body\_compress\_threshold | 512 | Not compress http body when it’s less than so many bytes. | src/brpc/policy/http\_rpc\_protocol.cpp |

<a id="server-serve-httph2--decompress-the-request-body"></a>

# Decompress the request body

Due to generality, brpc does not decompress request bodies automatically, but users can do the job by themselves as follows:

```c++
#include <brpc/policy/gzip_compress.h>
...
const std::string* encoding = cntl->http_request().GetHeader("Content-Encoding");
if (encoding != NULL && *encoding == "gzip") {
    butil::IOBuf uncompressed;
    if (!brpc::policy::GzipDecompress(cntl->request_attachment(), &uncompressed)) {
        LOG(ERROR) << "Fail to un-gzip request body";
        return;
    }
    cntl->request_attachment().swap(uncompressed);
}
// cntl->request_attachment() contains the data after decompression
```

<a id="server-serve-httph2--serve-https-requests"></a>

# Serve https requests

https is short for “http over SSL”, SSL is not exclusive for http, but effective for all protocols. The generic method for turning on server-side SSL is [here](#server-basics--turn-on-ssl).

<a id="server-serve-httph2--performance"></a>

# Performance

Productions without extreme performance requirements tend to use HTTP protocol, especially mobile products. Thus we put great emphasis on implementation qualities of HTTP. To be more specific:

<a id="server-serve-httph2--progressive-sending"></a>

# Progressive sending

brpc server is capable of sending large or infinite sized body, in following steps:

1. Call `Controller::CreateProgressiveAttachment()` to create a body that can be written progressively. The returned `ProgressiveAttachment` object should be managed by `intrusive_ptr`

```c++
#include <brpc/progressive_attachment.h>
...
butil::intrusive_ptr<brpc::ProgressiveAttachment> pa = cntl->CreateProgressiveAttachment();
```

2. Call `ProgressiveAttachment::Write()` to send the data.

   - If the write occurs before running of the server-side done, the sent data is cached until the done is called.
   - If the write occurs after running of the server-side done, the sent data is written out in chunked mode immediately.
3. After usage, destruct all `butil::intrusive_ptr<brpc::ProgressiveAttachment>` to release related resources.

<a id="server-serve-httph2--progressive-receiving"></a>

# Progressive receiving

Currently brpc server doesn’t support calling the service callback once header part in the http request is parsed. In other words, brpc server is not suitable for receiving large or infinite sized body.

<a id="server-serve-httph2--faq"></a>

# FAQ

<a id="server-serve-httph2--q-the-nginx-before-brpc-encounters-final-fail"></a>

### Q: The nginx before brpc encounters final fail

The error is caused by that brpc server closes the http connection directly without sending a response.

brpc server supports a variety of protocols on the same port. When a request is failed to be parsed in HTTP, it’s hard to tell that the request is definitely in HTTP. If the request is very likely to be one, the server sends HTTP 400 errors and closes the connection. However, if the error is caused HTTP method(at the beginning) or ill-formed serialization (may be caused by bugs at the HTTP client), the server still closes the connection without sending a response, which leads to “final fail” at nginx.

Solution: When using Nginx to forward traffic, set `$HTTP_method` to allowed HTTP methods or simply specify the HTTP method in `proxy_method`.

<a id="server-serve-httph2--q-does-brpc-support-http-chunked-mode"></a>

### Q: Does brpc support http chunked mode

Yes.

<a id="server-serve-httph2--q-why-do-http-requests-containing-base64-encoded-query-string-fail-to-parse-sometimes"></a>

### Q: Why do HTTP requests containing BASE64 encoded query string fail to parse sometimes?

According to the [HTTP specification](http://tools.ietf.org/html/rfc3986#section-2.2), following characters need to be encoded with `%`.

```
       reserved    = gen-delims / sub-delims

       gen-delims  = ":" / "/" / "?" / "#" / "[" / "]" / "@"

       sub-delims  = "!" / "$" / "&" / "'" / "(" / ")"
                   / "*" / "+" / "," / ";" / "="
```

Base64 encoded string may end with `=` which is a reserved character (take `?wi=NDgwMDB8dGVzdA==&anothorkey=anothervalue` as an example). The strings may be parsed successfully, or may be not, depending on the implementation which should not be assumed in principle.

One solution is to remove the trailing `=` which does not affect the [Base64 decoding](http://en.wikipedia.org/wiki/Base64#Padding). Another method is to [percent-encode](https://en.wikipedia.org/wiki/Percent-encoding) the URI, and do percent-decoding before Base64 decoding.

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="server-serve-nshead"></a>

<!-- source_url: https://brpc.apache.org/docs/server/serve-nshead/ -->

<!-- page_index: 75 -->

# Serve Nshead

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Serve%20Nshead/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Serve%20Nshead)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [把idl文件转化为proto文件](#server-serve-nshead--idl-proto)
- [以插件方式运行protoc](#server-serve-nshead--protoc)
- [实现生成的Service基类](#server-serve-nshead--service)
- [设置ServerOptions.nshead\_service](#server-serve-nshead--serveroptionsnshead_service)

# Serve Nshead

Learn how to serve nshead.

ub是百度内广泛使用的老RPC框架，在迁移ub服务时不可避免地需要[访问ub-server](#client-access-ub)或被ub-client访问。ub使用的协议种类很多，但都以nshead作为二进制包的头部，这类服务在brpc中统称为"**nshead service**"。

nshead后大都使用mcpack/compack作为序列化格式，注意这不是“协议”。“协议"除了序列化格式，还涉及到各种特殊字段的定义，一种序列化格式可能会衍生出很多协议。ub没有定义标准协议，所以即使都使用mcpack或compack，产品线的通信协议也是五花八门，无法互通。鉴于此，我们提供了一套接口，让用户能够灵活的处理自己产品线的协议，同时享受brpc提供的builtin services等一系列框架福利。

<a id="server-serve-nshead--ubrpc"></a>

# 使用ubrpc的服务

ubrpc协议的基本形式是nshead+compack或mcpack2，但compack或mcpack2中包含一些RPC过程需要的特殊字段。

在brpc r31687之后，用protobuf写的服务可以通过mcpack2pb被ubrpc client访问，步骤如下：

<a id="server-serve-nshead--idl-proto"></a>

## 把idl文件转化为proto文件

使用脚本[idl2proto](https://github.com/brpc/brpc/blob/master/tools/idl2proto)把idl文件自动转化为proto文件，下面是转化后的proto文件。

```protobuf
// Converted from echo.idl by brpc/tools/idl2proto
import "idl_options.proto";
option (idl_support) = true;
option cc_generic_services = true;
message EchoRequest {
  required string message = 1; 
}
message EchoResponse {
  required string message = 1; 
}
 
// 对于有多个参数的idl方法，需要定义一个包含所有request或response的消息，作为对应方法的参数。
message MultiRequests {
  required EchoRequest req1 = 1;
  required EchoRequest req2 = 2;
}
message MultiResponses {
  required EchoRequest res1 = 1;
  required EchoRequest res2 = 2;
}
 
service EchoService {
  // 对应idl中的void Echo(EchoRequest req, out EchoResponse res);
  rpc Echo(EchoRequest) returns (EchoResponse);
 
  // 对应idl中的EchoWithMultiArgs(EchoRequest req1, EchoRequest req2, out EchoResponse res1, out EchoResponse res2);
  rpc EchoWithMultiArgs(MultiRequests) returns (MultiResponses);
}
```

原先的echo.idl文件如下：

```protobuf
struct EchoRequest {
    string message;
};
 
struct EchoResponse {
    string message;
};
 
service EchoService {
    void Echo(EchoRequest req, out EchoResponse res);
    uint32_t EchoWithMultiArgs(EchoRequest req1, EchoRequest req2, out EchoResponse res1, out EchoResponse res2);
};
```

<a id="server-serve-nshead--protoc"></a>

## 以插件方式运行protoc

BRPC\_PATH代表brpc产出的路径（包含bin include等目录），PROTOBUF\_INCLUDE\_PATH代表protobuf的包含路径。注意–mcpack\_out要和–cpp\_out一致。

```shell
protoc --plugin=protoc-gen-mcpack=$BRPC_PATH/bin/protoc-gen-mcpack --cpp_out=. --mcpack_out=. --proto_path=$BRPC_PATH/include --proto_path=PROTOBUF_INCLUDE_PATH
```

<a id="server-serve-nshead--service"></a>

## 实现生成的Service基类

```c++
class EchoServiceImpl : public EchoService {
public:
 
    ...
    // 对应idl中的void Echo(EchoRequest req, out EchoResponse res);
    virtual void Echo(google::protobuf::RpcController* cntl_base,
                      const EchoRequest* request,
                      EchoResponse* response,
                      google::protobuf::Closure* done) {
        brpc::ClosureGuard done_guard(done);
        brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);
 
        // 填充response。
        response->set_message(request->message());
 
        // 对应的idl方法没有返回值，不需要像下面方法中那样set_idl_result()。
        // 可以看到这个方法和其他protobuf服务没有差别，所以这个服务也可以被ubrpc之外的协议访问。
    }
 
    virtual void EchoWithMultiArgs(google::protobuf::RpcController* cntl_base,
                                   const MultiRequests* request,
                                   MultiResponses* response,
                                   google::protobuf::Closure* done) {
        brpc::ClosureGuard done_guard(done);
        brpc::Controller* cntl = static_cast<brpc::Controller*>(cntl_base);
 
        // 填充response。response是我们定义的包含所有idl response的消息。
        response->mutable_res1()->set_message(request->req1().message());
        response->mutable_res2()->set_message(request->req2().message());
 
        // 告诉RPC有多个request和response。
        cntl->set_idl_names(brpc::idl_multi_req_multi_res);
 
        // 对应idl方法的返回值。
        cntl->set_idl_result(17);
    }
};
```

<a id="server-serve-nshead--serveroptionsnshead_service"></a>

## 设置ServerOptions.nshead\_service

```c++
#include <brpc/ubrpc2pb_protocol.h>
...
brpc::ServerOptions option;
option.nshead_service = new brpc::policy::UbrpcCompackAdaptor; // mcpack2用UbrpcMcpack2Adaptor
```

例子见[example/echo\_c++\_ubrpc\_compack](https://github.com/brpc/brpc/blob/master/example/echo_c++_ubrpc_compack/)。

<a id="server-serve-nshead--nsheadblob"></a>

# 使用nshead+blob的服务

[NsheadService](https://github.com/brpc/brpc/blob/master/src/brpc/nshead_service.h)是brpc中所有处理nshead打头协议的基类，实现好的NsheadService实例得赋值给ServerOptions.nshead\_service才能发挥作用。不赋值的话，默认是NULL，代表不支持任何nshead开头的协议，这个server被nshead开头的数据包访问时会报错。明显地，**一个Server只能处理一种以nshead开头的协议。**

NsheadService的接口如下，基本上用户只需要实现`ProcessNsheadRequest`这个函数。

```c++
// 代表一个nshead请求或回复。
struct NsheadMessage {
    nshead_t head;
    butil::IOBuf body;
};
 
// 实现这个类并赋值给ServerOptions.nshead_service来让brpc处理nshead请求。
class NsheadService : public Describable {
public:
    NsheadService();
    NsheadService(const NsheadServiceOptions&);
    virtual ~NsheadService();
 
    // 实现这个方法来处理nshead请求。注意这个方法可能在调用时controller->Failed()已经为true了。
    // 原因可能是Server.Stop()被调用正在退出(错误码是brpc::ELOGOFF)
    // 或触发了ServerOptions.max_concurrency(错误码是brpc::ELIMIT)
    // 在这种情况下，这个方法应该通过返回一个代表错误的response让客户端知道这些错误。
    // Parameters:
    //   server      The server receiving the request.
    //   controller  Contexts of the request.
    //   request     The nshead request received.
    //   response    The nshead response that you should fill in.
    //   done        You must call done->Run() to end the processing, brpc::ClosureGuard is preferred.
    virtual void ProcessNsheadRequest(const Server& server,
                                      Controller* controller,
                                      const NsheadMessage& request,
                                      NsheadMessage* response,
                                      NsheadClosure* done) = 0;
};
```

完整的example在[example/nshead\_extension\_c++](https://github.com/brpc/brpc/tree/master/example/nshead_extension_c++/)。

<a id="server-serve-nshead--nsheadmcpackcompackidl"></a>

# 使用nshead+mcpack/compack/idl的服务

idl是mcpack/compack的前端，用户只要在idl文件中描述schema，就可以生成一些C++结构体，这些结构体可以打包为mcpack/compack。如果你的服务仍在大量地使用idl生成的结构体，且短期内难以修改，同时想要使用brpc提升性能和开发效率的话，可以实现[NsheadService](https://github.com/brpc/brpc/blob/master/src/brpc/nshead_service.h)，其接口接受nshead + 二进制包为request，用户填写自己的处理逻辑，最后的response也是nshead+二进制包。流程与protobuf方法保持一致，但过程中不涉及任何protobuf的序列化和反序列化，用户可以自由地理解nshead后的二进制包，包括用idl加载mcpack/compack数据包。

不过，你应当充分意识到这么改造的坏处：

> **这个服务在继续使用mcpack/compack作为序列化格式，相比protobuf占用成倍的带宽和打包时间。**

为了解决这个问题，我们提供了[mcpack2pb](https://brpc.apache.org/docs/server/serve-nshead/mcpack2pb.md)，允许把protobuf作为mcpack/compack的前端。你只要写一份proto文件，就可以同时解析mcpack/compack和protobuf格式的请求。使用这个方法，使用idl描述的服务的可以平滑地改造为使用proto文件描述，而不用修改上游client（仍然使用mcpack/compack）。你产品线的服务可以逐个地从mcpack/compack/idl切换为protobuf，从而享受到性能提升，带宽节省，全新开发体验等好处。你可以自行在NsheadService使用src/mcpack2pb，也可以联系我们，提供更高质量的协议支持。

<a id="server-serve-nshead--nsheadprotobuf"></a>

# 使用nshead+protobuf的服务

如果你的协议已经使用了nshead + protobuf，或者你想把你的协议适配为protobuf格式，那可以使用另一种模式：实现[NsheadPbServiceAdaptor](https://github.com/brpc/brpc/blob/master/src/brpc/nshead_pb_service_adaptor.h)（NsheadService的子类）。

工作步骤：

- Call ParseNsheadMeta() to understand the nshead header, user must tell RPC which pb method to call in the callback.
- Call ParseRequestFromIOBuf() to convert the body after nshead header to pb request, then call the pb method.
- When user calls server’s done to end the RPC, SerializeResponseToIOBuf() is called to convert pb response to binary data that will be appended after nshead header and sent back to client.

这样做的好处是，这个服务还可以被其他使用protobuf的协议访问，比如baidu\_std，hulu\_pbrpc，sofa\_pbrpc协议等等。NsheadPbServiceAdaptor的主要接口如下。完整的example在[这里](https://github.com/brpc/brpc/tree/master/example/nshead_pb_extension_c++/)。

```c++
class NsheadPbServiceAdaptor : public NsheadService {
public:
    NsheadPbServiceAdaptor() : NsheadService(
        NsheadServiceOptions(false, SendNsheadPbResponseSize)) {}
    virtual ~NsheadPbServiceAdaptor() {}
 
    // Fetch meta from `nshead_req' into `meta'.
    // Params:
    //   server: where the RPC runs.
    //   nshead_req: the nshead request that server received.
    //   controller: If something goes wrong, call controller->SetFailed()
    //   meta: Set meta information into this structure. `full_method_name'
    //         must be set if controller is not SetFailed()-ed
    // FIXME: server is not needed anymore, controller->server() is same
    virtual void ParseNsheadMeta(const Server& server,
                                 const NsheadMessage& nshead_req,
                                 Controller* controller,
                                 NsheadMeta* meta) const = 0;
    // Transform `nshead_req' to `pb_req'.
    // Params:
    //   meta: was set by ParseNsheadMeta()
    //   nshead_req: the nshead request that server received.
    //   controller: you can set attachment into the controller. If something
    //               goes wrong, call controller->SetFailed()
    //   pb_req: the pb request should be set by your implementation.
    virtual void ParseRequestFromIOBuf(const NsheadMeta& meta,
                                       const NsheadMessage& nshead_req,
                                       Controller* controller,
                                       google::protobuf::Message* pb_req) const = 0;
    // Transform `pb_res' (and controller) to `nshead_res'.
    // Params:
    //   meta: was set by ParseNsheadMeta()
    //   controller: If something goes wrong, call controller->SetFailed()
    //   pb_res: the pb response that returned by pb method. [NOTE] `pb_res'
    //           can be NULL or uninitialized when RPC failed (indicated by
    //           Controller::Failed()), in which case you may put error
    //           information into `nshead_res'.
    //   nshead_res: the nshead response that will be sent back to client.
    virtual void SerializeResponseToIOBuf(const NsheadMeta& meta,
                                          Controller* controller,
                                          const google::protobuf::Message* pb_res,
                                          NsheadMessage* nshead_res) const = 0;
};
```

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="server-serve-thrift"></a>

<!-- source_url: https://brpc.apache.org/docs/server/serve-thrift/ -->

<!-- page_index: 76 -->

# Serve thrift

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Serve%20thrift/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Serve%20thrift)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [server side return string “hello” sent from client](#server-serve-thrift--server-side-return-string-hello-sent-from-client)
- [server side return string “hello” \* 1000](#server-serve-thrift--server-side-return-string-hello-1000)
- [server side do some complicated math and return string “hello” \* 1000](#server-serve-thrift--server-side-do-some-complicated-math-and-return-string-hello-1000)

# Serve thrift

Learn how to serve thrift.

[thrift](https://thrift.apache.org/) is a RPC framework used widely in various environments, which was developed by Facebook and adopted by Apache later. In order to interact with thrift servers and solves issues on thread-safety, usabilities and concurrencies, brpc directly supports the thrift protocol that is used by thrift in NonBlocking mode.

Example: [example/thrift\_extension\_c++](https://github.com/brpc/brpc/tree/master/example/thrift_extension_c++/).

Advantages compared to the official solution:

- Thread safety. No need to set up separate clients for each thread.
- Supports synchronous, asynchronous, batch synchronous, batch asynchronous, and other access methods. Combination channels such as ParallelChannel are also supported.
- Support various connection types(short, connection pool). Support timeout, backup request, cancellation, tracing, built-in services, and other benefits offered by brpc.
- Better performance.

<a id="server-serve-thrift--compile"></a>

# Compile

brpc depends on the thrift library and reuses some code generated by thrift tools. Please read official documents to find out how to write thrift files, generate code, compilations etc.

brpc does not enable thrift support or depend on the thrift lib by default. If the support is needed, compile brpc with extra –with-thrift or -DWITH\_THRIFT=ON

Install thrift under Linux
Read [Official wiki](https://thrift.apache.org/docs/install/debian) to install depended libs and tools, then download thrift source code from [official site](https://thrift.apache.org/download), uncompress and compile。

```bash
wget http://www.apache.org/dist/thrift/0.11.0/thrift-0.11.0.tar.gz
tar -xf thrift-0.11.0.tar.gz
cd thrift-0.11.0/
./configure --prefix=/usr --with-ruby=no --with-python=no --with-java=no --with-go=no --with-perl=no --with-php=no --with-csharp=no --with-erlang=no --with-lua=no --with-nodejs=no
make CPPFLAGS=-DFORCE_BOOST_SMART_PTR -j 4 -s
sudo make install
```

Config brpc with thrift support, then make. The compiled libbrpc.a includes extended code for thrift support and can be linked normally as in other brpc projects.

```bash
# Ubuntu sh config_brpc.sh --headers=/usr/include --libs=/usr/lib --with-thrift
# Fedora/CentOS sh config_brpc.sh --headers=/usr/include --libs=/usr/lib64 --with-thrift
# Or use cmake mkdir build && cd build && cmake ../ -DWITH_THRIFT=ON
```

Read [Getting Started](#getting_started) for more compilation options.

<a id="server-serve-thrift--client-accesses-thrift-server"></a>

# Client accesses thrift server

Steps：

- Create a Channel setting protocol to brpc::PROTOCOL\_THRIFT
- Create brpc::ThriftStub
- Use native request and response to start RPC directly.

Example code:

```c++
#include <brpc/channel.h>
#include <brpc/thrift_message.h>         // Defines ThriftStub
...

DEFINE_string(server, "0.0.0.0:8019", "IP Address of thrift server");
DEFINE_string(load_balancer, "", "The algorithm for load balancing");
...
  
brpc::ChannelOptions options;
options.protocol = brpc::PROTOCOL_THRIFT;
brpc::Channel thrift_channel;
if (thrift_channel.Init(Flags_server.c_str(), FLAGS_load_balancer.c_str(), &options) != 0) {
   LOG(ERROR) << "Fail to initialize thrift channel";
   return -1;
}

brpc::ThriftStub stub(&thrift_channel);
...

// example::[EchoRequest/EchoResponse] are types generated by thrift
example::EchoRequest req;
example::EchoResponse res;
req.data = "hello";

stub.CallMethod("Echo", &cntl, &req, &res, NULL);
if (cntl.Failed()) {
    LOG(ERROR) << "Fail to send thrift request, " << cntl.ErrorText();
    return -1;
} 
```

<a id="server-serve-thrift--server-processes-thrift-requests"></a>

# Server processes thrift requests

Inherit brpc::ThriftService to implement the processing code, which may call the native handler generated by thrift to re-use existing entry directly, or read the request and set the response directly just as in other protobuf services.

```c++
class EchoServiceImpl : public brpc::ThriftService {
public:
    void ProcessThriftFramedRequest(brpc::Controller* cntl,
                                    brpc::ThriftFramedMessage* req,
                                    brpc::ThriftFramedMessage* res,
                                    google::protobuf::Closure* done) override {
        // Dispatch calls to different methods
        if (cntl->thrift_method_name() == "Echo") {
            return Echo(cntl, req->Cast<example::EchoRequest>(),
                        res->Cast<example::EchoResponse>(), done);
        } else {
            cntl->SetFailed(brpc::ENOMETHOD, "Fail to find method=%s",
                            cntl->thrift_method_name().c_str());
            done->Run();
        }
    }

    void Echo(brpc::Controller* cntl,
              const example::EchoRequest* req,
              example::EchoResponse* res,
              google::protobuf::Closure* done) {
        // This object helps you to call done->Run() in RAII style. If you need
        // to process the request asynchronously, pass done_guard.release().
        brpc::ClosureGuard done_guard(done);

        res->data = req->data + " (processed)";
    }
};
```

Set the implemented service to ServerOptions.thrift\_service and start the service.

```c++
    brpc::Server server;
    brpc::ServerOptions options;
    options.thrift_service = new EchoServiceImpl;
    options.idle_timeout_sec = FLAGS_idle_timeout_s;
    options.max_concurrency = FLAGS_max_concurrency;

    // Start the server.
    if (server.Start(FLAGS_port, &options) != 0) {
        LOG(ERROR) << "Fail to start EchoServer";
        return -1;
    }
```

<a id="server-serve-thrift--performance-test-for-native-thrift-compare-with-brpc-thrift-implementaion"></a>

# Performance test for native thrift compare with brpc thrift implementaion

Test Env: 48 core 2.30GHz

<a id="server-serve-thrift--server-side-return-string-hello-sent-from-client"></a>

## server side return string “hello” sent from client

| Framework | Threads Num | QPS | Avg lantecy | CPU |
| --- | --- | --- | --- | --- |
| native thrift | 60 | 6.9w | 0.9ms | 2.8% |
| brpc thrift | 60 | 30w | 0.2ms | 18% |

<a id="server-serve-thrift--server-side-return-string-hello-1000"></a>

## server side return string “hello” \* 1000

| Framework | Threads Num | QPS | Avg lantecy | CPU |
| --- | --- | --- | --- | --- |
| native thrift | 60 | 5.2w | 1.1ms | 4.5% |
| brpc thrift | 60 | 19.5w | 0.3ms | 22% |

<a id="server-serve-thrift--server-side-do-some-complicated-math-and-return-string-hello-1000"></a>

## server side do some complicated math and return string “hello” \* 1000

| Framework | Threads Num | QPS | Avg lantecy | CPU |
| --- | --- | --- | --- | --- |
| native thrift | 60 | 1.7w | 3.5ms | 76% |
| brpc thrift | 60 | 2.1w | 2.9ms | 93% |

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="server-server-push"></a>

<!-- source_url: https://brpc.apache.org/docs/server/server-push/ -->

<!-- page_index: 77 -->

# Server push

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Server/Server%20push/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Server%20push)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Server push

Learn how to server push.

<a id="server-server-push--server-push"></a>

# Server push

What “server push” refers to is: server sends a message to client after occurrence of an event, rather than passively replying the client as in ordinary RPCs. Following two methods are recommended to implement server push in brpc.

<a id="server-server-push--remote-event"></a>

## Remote event

Similar to local event, remote event is divided into two steps: registration and notification. The client sends an asynchronous RPC to the server for registration, and puts the event-handling code in the RPC callback. The RPC is also a part of the waiting for the notification, namely the server does not respond directly after receiving the request, instead it does not call done->Run() (to notify the client) until the local event triggers. As we see, the server is also asynchronous. If the connection is broken during the process, the client fails soon and may choose to retry another server or end the RPC. Server should be aware of the disconnection by using Controller.NotifyOnCancel() and delete useless done in-time.

This pattern is similar to [long polling](https://en.wikipedia.org/wiki/Push_technology#Long_polling) in some sense, sounds old but probably still be the most effective method. At first glance “server push” is server visiting client, opposite with ordinary client visiting server. But do you notice that, the response sent from server back to client is also in the opposite direction of “client visiting server”? In order to understand differences between response and push, let’s analyze the process with the presumption that “client may receive messages from the server at any time”.

- Client has to understand the messages from server anyway, otherwise the messaging is pointless.
- Client also needs to know how to deal with the message. If the client does not have the handling code, the message is still useless.

In other words, the client should “be prepared” to the messages from the server, and the “preparation” often relies on programming contexts that client just faces. Regarding different factors, it’s more universal for client to inform server for “I am ready” (registered) first, then the server notifies the client with events later, in which case **the “push” is just a “response”**, with a very long or even infinite timeout.

In some scenarios, the registration can be ignored, such as the [push promise](https://tools.ietf.org/html/rfc7540#section-8.2) in http2, which does not require the web browser(client) to register with the server, because both client and server know that the task between them is to let the client download necessary resources ASAP. Since each resource has a unique URI, the server can directly push resources and URI to the client, which caches the resources to avoid repeated accesses. Similarly, protocols capable of “two-way communication” probably improves efficiencies of pushing in given scenarios such as multimedia streaming or fixed-format key/value pairs etc, rather than implementing universal pushing. The client knows how to handle messages that may be pushed by servers, so extra registrations are not required. The push can still be treated as a “response”: to the request that client already and always promised server.

<a id="server-server-push--restful-callback"></a>

## Restful callback

The client wants a given URL to be called with necessary parameters when the event occurs. In this pattern, server can reply the client directly when it receives the registration request, because the event is not triggered by the end of the RPC. In addition, since the callback is just a URL, which can be stored in databases and message queues, this pattern is very flexible and widely used in business systems.

URL and parameters must contain enough information to make the callback know that which notification corresponds to which request, because the client may care about more than one event at the same time, or an event may be registered more than once due to network jitter or restarting machines etc. If the URL path is fixed, the client should place an unique ID in the registration request and the server should put the ID unchanged in response. Or the client generates an unique path for each registration so that each request is distinguishable from each other naturally. These methods are actually same in essense, just different positions for unique identifiers.

Callbacks should deal with [idempotence](https://en.wikipedia.org/wiki/Idempotence). The server may retry and send more than one notifications after encountering network problems. If the first notification has been successful, follow-up notifications should not have effects. The “remote event” pattern guarantees idempotency at the layer of RPC, which ensures that the done is called once and only once.

In order to avoid missing important notifications, users often need to combine RPC and message queues flexibly. RPC is much better at latency and efficiency than message queue, but due to limited memory, server needs to stop sending RPC after several failed retries and do more important things with the memory. It’s better to move the notification task into a persistent message queue at the moment, which is capable of retrying during a very long time. With the idempotence in URL callback, most notifications are sent reliably and in-time.

---

Last modified January 9, 2022: [A new verion of brpc website based on hugo (94b25d711)](https://github.com/apache/brpc-website/commit/94b25d7110944f3d4b2071b5188c691b23ffe3a9)

---

<a id="tools-benchmark_http"></a>

<!-- source_url: https://brpc.apache.org/docs/tools/benchmark_http/ -->

<!-- page_index: 78 -->

# benchmark_http

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Tools/benchmark_http/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=benchmark_http)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# benchmark\_http

Learn about bRPC benchmark\_http tool.

可代替[ab](https://httpd.apache.org/docs/2.2/programs/ab.html)测试http server极限性能。ab功能较多但年代久远，有时本身可能会成为瓶颈。benchmark\_http基本上就是一个brpc http client，性能很高，功能较少，一般压测够用了。

使用方法：

首先你得[下载和编译](#getting_started)了brpc源码，然后去example/http\_c++目录编译，成功后应该能看到benchmark\_http。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="tools"></a>

<!-- source_url: https://brpc.apache.org/docs/tools/ -->

<!-- page_index: 79 -->

# Tools

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Tools/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Tools)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Tools

Learn about bRPC tools.

---

##### [rpc\_press](#tools-rpc_press)

Learn about bRPC rpc\_press tool.

##### [rpc\_replay](#tools-rpc_replay)

Learn about bRPC rpc\_replay tool.

##### [rpc\_view](#tools-rpc_view)

Learn about bRPC rpc\_view tool.

##### [benchmark\_http](#tools-benchmark_http)

Learn about bRPC benchmark\_http tool.

##### [parallel\_http](#tools-parallel_http)

Learn about bRPC parallel\_http tool.

Last modified November 4, 2022: [Changing the directory order (debc613b4)](https://github.com/apache/brpc-website/commit/debc613b4aed17f8f1f9173c242196d54d6da663)

---

<a id="tools-parallel_http"></a>

<!-- source_url: https://brpc.apache.org/docs/tools/parallel_http/ -->

<!-- page_index: 80 -->

# parallel_http

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Tools/parallel_http/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=parallel_http)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# parallel\_http

Learn about bRPC parallel\_http tool.

parallel\_http能同时访问大量的http服务（几万个），适合在命令行中查询线上所有server的内置信息，供其他工具进一步过滤和聚合。curl很难做到这点，即使多个curl以后台的方式运行，并行度一般也只有百左右，访问几万台机器需要等待极长的时间。

---

Last modified January 9, 2022: [A new verion of brpc website based on hugo (94b25d711)](https://github.com/apache/brpc-website/commit/94b25d7110944f3d4b2071b5188c691b23ffe3a9)

---

<a id="tools-rpc_press"></a>

<!-- source_url: https://brpc.apache.org/docs/tools/rpc_press/ -->

<!-- page_index: 81 -->

# rpc_press

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Tools/rpc_press/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=rpc_press)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# rpc\_press

Learn about bRPC rpc\_press tool.

rpc\_press无需写代码就压测各种rpc server，目前支持的协议有：

- baidu\_std
- hulu-pbrpc
- sofa-pbrpc
- public\_pbrpc
- nova\_pbrpc

<a id="tools-rpc_press--section"></a>

# 获取工具

先按照[Getting Started](#getting_started)编译好brpc，再去tools/rpc\_press编译。

在CentOS 6.3上如果出现找不到libssl.so.4的错误，可执行`ln -s /usr/lib64/libssl.so.6 libssl.so.4临时解决`

<a id="tools-rpc_press--section"></a>

# 发压力

rpc\_press会动态加载proto文件，无需把proto文件编译为c++源文件。rpc\_press会加载json格式的输入文件，转为pb请求，发向server，收到pb回复后如有需要会转为json并写入用户指定的文件。

rpc\_press的所有的选项都来自命令行参数，而不是配置文件.

如下的命令向下游0.0.0.0:8002用baidu\_std重复发送两个pb请求，分别转自’{“message”:“hello”}和’{“message”:“world”}，持续压力直到按ctrl-c，qps为100。

json也可以写在文件中，假如./input.json包含了上述两个请求，-input=./input.json也是可以的。

必需参数：

可选参数:

- -inc: 包含被import的proto文件的路径。rpc\_press默认支持import目录下的其他proto文件，但如果proto文件在其他目录，就要通过这个参数指定，多个路径用分号(;)分隔。
- -lb\_policy: 指定负载均衡算法，默认为空，可选项为: rr random la c\_murmurhash c\_md5，具体见[负载均衡](#client-basics--load-balancer)。
- -timeout\_ms: 设定超时,单位是毫秒(milliseconds),默认是1000(1秒)
- -max\_retry: 最大的重试次数,默认是3, 一般无需修改. brpc的重试行为具体请见[这里](#client-basics--retry).
- -protocol: 连接server使用的协议，可选项见[协议](#client-basics--protocols), 默认是baidu\_std
- -connection\_type: 连接方式，可选项为: single pooled short，具体见[连接方式](#client-basics--connection-type)。默认会根据协议自动选择,无需指定.
- -output: 如果不为空，response会转为json并写入这个文件，默认为空。
- -duration：大于0时表示发送这么多秒的压力后退出，否则一直发直到按ctrl-c或进程被杀死。默认是0（一直发送）。
- -qps：大于0时表示以这个压力发送，否则以最大速度(自适应)发送。默认是100。
- -dummy\_port：修改dummy\_server的端口，默认是8888

常用的参数组合：

- 向下游0.0.0.0:8002、用baidu\_std重复发送./input.json中的所有请求，持续压力直到按ctrl-c，qps为100。
  ./rpc\_press -proto=echo.proto -method=example.EchoService.Echo -server=0.0.0.0:8002 -input=./input.json -qps=100
- 以round-robin分流算法向bns://node-name代表的所有下游机器、用baidu\_std重复发送两个pb请求，持续压力直到按ctrl-c，qps为100。
  ./rpc\_press -proto=echo.proto -method=example.EchoService.Echo -server=bns://node-name -lb\_policy=rr -input=’{“message”:“hello”} {“message”:“world”}’ -qps=100
- 向下游0.0.0.0:8002、用hulu协议重复发送两个pb请求，持续压力直到按ctrl-c，qps为100。
  ./rpc\_press -proto=echo.proto -method=example.EchoService.Echo -server=0.0.0.0:8002 -protocol=hulu\_pbrpc -input=’{“message”:“hello”} {“message”:“world”}’ -qps=100
- 向下游0.0.0.0:8002、用baidu\_std重复发送两个pb请求，持续最大压力直到按ctrl-c。
  ./rpc\_press -proto=echo.proto -method=example.EchoService.Echo -server=0.0.0.0:8002 -input=’{“message”:“hello”} {“message”:“world”}’ -qps=0
- 向下游0.0.0.0:8002、用baidu\_std重复发送两个pb请求，持续最大压力10秒钟。
  ./rpc\_press -proto=echo.proto -method=example.EchoService.Echo -server=0.0.0.0:8002 -input=’{“message”:“hello”} {“message”:“world”}’ -qps=0 -duration=10
- echo.proto中import了另一个目录下的proto文件
  ./rpc\_press -proto=echo.proto -inc= -method=example.EchoService.Echo -server=0.0.0.0:8002 -input=’{“message”:“hello”} {“message”:“world”}’ -qps=0 -duration=10

rpc\_press启动后会默认在8888端口启动一个dummy server，用于观察rpc\_press本身的运行情况：

```
./rpc_press -proto=echo.proto -service=example.EchoService -method=Echo -server=0.0.0.0:8002 -input=./input.json -duration=0 -qps=100
TRACE: 01-30 16:10:04:   * 0 src/brpc/server.cpp:733] Server[dummy_servers] is serving on port=8888.
TRACE: 01-30 16:10:04:   * 0 src/brpc/server.cpp:742] Check out http://xxx.com:8888 in your web browser.</code>
```

dummy\_server启动时会在终端打印日志，一般按住ctrl点击那个链接可以直接打开对应的内置服务页面，就像这样：

![img](assets/images/rpc-press-1_a289ecf710935863.png)

切换到vars页面，在Search框中输入rpc\_press可以看到当前压力的延时分布情况:

![img](assets/images/rpc-press-2_7148a667bbb52286.png)

你可以通过-dummy\_port参数修改dummy\_server的端口，请确保端口可以在浏览器中访问。

如果你无法打开浏览器，命令行中也会定期打印信息：

```
2016/01/30-16:19:01     sent:101       success:101       error:0         total_error:0         total_sent:28379     
2016/01/30-16:19:02     sent:101       success:101       error:0         total_error:0         total_sent:28480     
2016/01/30-16:19:03     sent:101       success:101       error:0         total_error:0         total_sent:28581     
2016/01/30-16:19:04     sent:101       success:101       error:0         total_error:0         total_sent:28682     
2016/01/30-16:19:05     sent:101       success:101       error:0         total_error:0         total_sent:28783     
2016/01/30-16:19:06     sent:101       success:101       error:0         total_error:0         total_sent:28884     
2016/01/30-16:19:07     sent:101       success:101       error:0         total_error:0         total_sent:28985     
2016/01/30-16:19:08     sent:101       success:101       error:0         total_error:0         total_sent:29086     
2016/01/30-16:19:09     sent:101       success:101       error:0         total_error:0         total_sent:29187     
2016/01/30-16:19:10     sent:101       success:101       error:0         total_error:0         total_sent:29288     
[Latency]
  avg            122 us
  50%            122 us
  70%            135 us
  90%            161 us
  95%            164 us
  97%            166 us
  99%            172 us
  99.9%          199 us
  99.99%         199 us
  max            199 us
```

上方的字段含义应该是自解释的，在此略过。下方是延时信息，第一项"avg"是10秒内的平均延时，最后一项"max"是10秒内的最大延时，其余以百分号结尾的则代表延时分位值，即有左侧这么多比例的请求延时小于右侧的延时（单位微秒）。一般性能测试需要关注99%之后的长尾区域。

<a id="tools-rpc_press--faq"></a>

# FAQ

**Q: 如果下游是基于j-protobuf框架的服务模块，压力工具该如何配置？**

A：因为协议兼容性问题，启动rpc\_press的时候需要带上-baidu\_protocol\_use\_fullname=false

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="tools-rpc_replay"></a>

<!-- source_url: https://brpc.apache.org/docs/tools/rpc_replay/ -->

<!-- page_index: 82 -->

# rpc_replay

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Tools/rpc_replay/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=rpc_replay)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# rpc\_replay

Learn about bRPC rpc\_replay tool.

r31658后，brpc能随机地把一部分请求写入一些文件中，并通过rpc\_replay工具回放。目前支持的协议有：baidu\_std, hulu\_pbrpc, sofa\_pbrpc。

<a id="tools-rpc_replay--section"></a>

# 获取工具

先按照[Getting Started](#getting_started)编译好brpc，再去tools/rpc\_replay编译。

在CentOS 6.3上如果出现找不到libssl.so.4的错误，可执行`ln -s /usr/lib64/libssl.so.6 libssl.so.4临时解决`

<a id="tools-rpc_replay--section"></a>

# 采样

brpc通过如下flags打开和控制如何保存请求，包含(R)后缀的flag都可以动态设置。

![img](assets/images/rpc-replay-1_c5ffcbe5432fc5a6.png)

![img](assets/images/rpc-replay-2_6dcb1411f8802038.png)

参数说明：

- -rpc\_dump是主开关，关闭时其他以rpc\_dump开头的flag都无效。当打开-rpc\_dump后，brpc会以一定概率采集请求，如果服务的qps很高，brpc会调节采样比例，使得每秒钟采样的请求个数不超过-bvar\_collector\_expected\_per\_second对应的值。这个值在目前同样影响rpcz和contention profiler，一般不用改动，以后会对不同的应用独立开来。
- -rpc\_dump\_dir：设置存放被dump请求的目录
- -rpc\_dump\_max\_files: 设置目录下的最大文件数，当超过限制时，老文件会被删除以腾出空间。
- -rpc\_dump\_max\_requests\_in\_one\_file：一个文件内的最大请求数，超过后写新文件。

brpc通过一个[bvar::Collector](https://github.com/brpc/brpc/blob/master/src/bvar/collector.h)来汇总来自不同线程的被采样请求，不同线程之间没有竞争，开销很小。

写出的内容依次存放在rpc\_dump\_dir目录下的多个文件内，这个目录默认在./rpc\_dump\_，其中是程序名。不同程序在同一个目录下同时采样时会写入不同的目录。如果程序启动时rpc\_dump\_dir已经存在了，目录将被清空。目录中的每个文件以requests.yyyymmdd\_hhmmss\_uuuuus命名，以保证按时间有序方便查找，比如：

![img](assets/images/rpc-replay-3_cff7ccdba575ae04.png)

目录下的文件数不超过rpc\_dump\_max\_files，超过后最老的文件被删除从而给新文件腾出位置。

文件是二进制格式，格式与baidu\_std协议的二进制格式类似，每个请求的binary layout如下：

```
"PRPC" (4 bytes magic string)
body_size(4 bytes)
meta_size(4 bytes)
RpcDumpMeta (meta_size bytes)
serialized request (body_size - meta_size bytes, including attachment)
```

请求间紧密排列。一个文件内的请求数不超过rpc\_dump\_max\_requests\_in\_one\_file。

> 一个文件可能包含多种协议的请求，如果server被多种协议访问的话。回放时被请求的server也将收到不同协议的请求。

brpc提供了[SampleIterator](https://github.com/brpc/brpc/blob/master/src/brpc/rpc_dump.h)从一个采样目录下的所有文件中依次读取所有的被采样请求，用户可根据需求把serialized request反序列化为protobuf请求，做一些二次开发。

```c++
#include <brpc/rpc_dump.h>
...
brpc::SampleIterator it("./rpc_data/rpc_dump/echo_server");         
for (brpc::SampledRequest* req = it->Next(); req != NULL; req = it->Next()) {
    ...                    
    // req->meta的类型是brpc::RpcDumpMeta，定义在src/brpc/rpc_dump.proto
    // req->request的类型是butil::IOBuf，对应格式说明中的"serialized request"
    // 使用结束后必须delete req。
}
```

<a id="tools-rpc_replay--section"></a>

# 回放

brpc在[tools/rpc\_replay](https://github.com/brpc/brpc/tree/master/tools/rpc_replay/)提供了默认的回放工具。运行方式如下：

![img](assets/images/rpc-replay-4_925d1506ae700fac.png)

主要参数说明：

- -dir指定了存放采样文件的目录
- -times指定循环回放次数。其他参数请加上–help运行查看。
- -connection\_type： 连接server的方式
- -dummy\_port：修改dummy\_server的端口
- -max\_retry：最大重试次数，默认3次。
- -qps：大于0时限制qps，默认为0（不限制）
- -server：server的地址
- -thread\_num：发送线程数，为0时会根据qps自动调节，默认为0。一般不用设置。
- -timeout\_ms：超时
- -use\_bthread：使用bthread发送，默认是。

rpc\_replay会默认启动一个仅监控用的dummy server。打开后可查看回放的状况。其中rpc\_replay\_error是回放失败的次数。

![img](assets/images/rpc-replay-5_341f8ef6482433b8.png)

如果你无法打开浏览器，命令行中也会定期打印信息：

```
2016/01/30-16:19:01     sent:101       success:101       error:0         total_error:0         total_sent:28379     
2016/01/30-16:19:02     sent:101       success:101       error:0         total_error:0         total_sent:28480     
2016/01/30-16:19:03     sent:101       success:101       error:0         total_error:0         total_sent:28581     
2016/01/30-16:19:04     sent:101       success:101       error:0         total_error:0         total_sent:28682     
2016/01/30-16:19:05     sent:101       success:101       error:0         total_error:0         total_sent:28783     
2016/01/30-16:19:06     sent:101       success:101       error:0         total_error:0         total_sent:28884     
2016/01/30-16:19:07     sent:101       success:101       error:0         total_error:0         total_sent:28985     
2016/01/30-16:19:08     sent:101       success:101       error:0         total_error:0         total_sent:29086     
2016/01/30-16:19:09     sent:101       success:101       error:0         total_error:0         total_sent:29187     
2016/01/30-16:19:10     sent:101       success:101       error:0         total_error:0         total_sent:29288     
[Latency]
  avg            122 us
  50%            122 us
  70%            135 us
  90%            161 us
  95%            164 us
  97%            166 us
  99%            172 us
  99.9%          199 us
  99.99%         199 us
  max            199 us
```

上方的字段含义应该是自解释的，在此略过。下方是延时信息，第一项"avg"是10秒内的平均延时，最后一项"max"是10秒内的最大延时，其余以百分号结尾的则代表延时分位值，即有左侧这么多比例的请求延时小于右侧的延时（单位微秒）。性能测试需要关注99%之后的长尾区域。

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="tools-rpc_view"></a>

<!-- source_url: https://brpc.apache.org/docs/tools/rpc_view/ -->

<!-- page_index: 83 -->

# rpc_view

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Tools/rpc_view/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=rpc_view)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# rpc\_view

Learn about bRPC rpc\_view tool.

rpc\_view可以转发端口被限的server的内置服务。像百度内如果一个服务的端口不在8000-8999，就只能在命令行下使用curl查看它的内置服务，没有历史趋势和动态曲线，也无法点击链接，排查问题不方便。rpc\_view是一个特殊的http proxy：把对它的所有访问都转为对目标server的访问。只要把rpc\_view的端口能在浏览器中被访问，我们就能通过它看到原本不能直接看到的server了。

<a id="tools-rpc_view--section"></a>

# 获取工具

先按照[Getting Started](#getting_started)编译好brpc，再去tools/rpc\_view编译。

在CentOS 6.3上如果出现找不到libssl.so.4的错误，可执行`ln -s /usr/lib64/libssl.so.6 libssl.so.4临时解决`

<a id="tools-rpc_view--server"></a>

# 访问目标server

确保你的机器能访问目标server，开发机应该都可以，一些测试机可能不行。运行./rpc\_view 就可以了。

比如：

```
$ ./rpc_view 10.46.130.53:9970
TRACE: 02-14 12:12:20:   * 0 src/brpc/server.cpp:762] Server[rpc_view_server] is serving on port=8888.
TRACE: 02-14 12:12:20:   * 0 src/brpc/server.cpp:771] Check out http://XXX.com:8888 in web browser.
```

打开rpc\_view在8888端口提供的页面（在secureCRT中按住ctrl点url）：

![img](assets/images/rpc-view-1_7990c7862cede0fa.png)

这个页面正是目标server的内置服务，右下角的提示告诉我们这是rpc\_view提供的。这个页面和真实的内置服务基本是一样的，你可以做任何操作。

<a id="tools-rpc_view--server"></a>

# 更换目标server

你可以随时停掉rpc\_view并更换目标server，不过你觉得麻烦的话，也可以在浏览器上操作：给url加上?changetarget=就行了。

假如我们之前停留在原目标server的/connections页面：

![img](assets/images/rpc-view-2_a9f1d210fa2acc9d.png)

加上?changetarge后就跳到新目标server的/connections页面了。接下来点击其他tab都会显示新目标server的。

![img](assets/images/rpc-view-3_223459e7aec8f207.png)

---

Last modified May 17, 2022: [update brpc users page (#71) (a31ce10d3)](https://github.com/apache/brpc-website/commit/a31ce10d3d732f29e56dd2c8c8a0d07c3e633209)

---

<a id="use-cases-inside-baidu"></a>

<!-- source_url: https://brpc.apache.org/docs/use-cases-inside-baidu/ -->

<!-- page_index: 84 -->

# Use cases inside Baidu

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Use%20cases%20inside%20Baidu/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Use%20cases%20inside%20Baidu)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Use cases inside Baidu

Learn about bRPC use cases inside Baidu.

---

##### [百度地图api入口](#use-cases-inside-baidu-use-case1)

Use case1：百度地图api入口。

##### [联盟DSP](#use-cases-inside-baidu-use-case2)

Use case2：联盟DSP

##### [ELF学习框架](#use-cases-inside-baidu-use-case3)

Use case3：ELF学习框架

##### [云平台代理服务](#use-cases-inside-baidu-use-case4)

Use case4：云平台代理服务

Last modified November 7, 2022: [add ASF page (f7462e073)](https://github.com/apache/brpc-website/commit/f7462e07303f64f538630de63f8b75373fa3f500)

---

<a id="use-cases-inside-baidu-use-case1"></a>

<!-- source_url: https://brpc.apache.org/docs/use-cases-inside-baidu/use-case1/ -->

<!-- page_index: 85 -->

# 百度地图api入口

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Use%20cases%20inside%20Baidu/Use%20case1/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=%e7%99%be%e5%ba%a6%e5%9c%b0%e5%9b%beapi%e5%85%a5%e5%8f%a3)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# 百度地图api入口

Use case1：百度地图api入口。

<a id="use-cases-inside-baidu-use-case1--section"></a>

# 进展

| 时间 | 内容 | 说明 |
| --- | --- | --- |
| 8.11 - 8.28 | 调研 + 研发 + 自测 | 自测性能报告见附件 |
| 9.8 - 9.22 | QA测试 | QA测试报告见附件 |
| 10.8 | 北京机房1台机器上线 |  |
| 10.14 | 北京机房1台机器上线 | 修复URL编码问题 |
| 10.19 | 北京机房7/35机器上线杭州和南京各2台机器上线 | 开始小流量上线 |
| 10.22 | 北京机房10/35机器上线杭州机房5/26机器上线南京机房5/19机器上线 | 修复http响应数据压缩问题 |
| 11.3 | 北京机房10/35机器上线 | 修复RPC内存泄露问题 |
| 11.6 | 杭州机房5/26机器上线南京机房5/19机器上线 | 同北京机房版本 |
| 11.9 | 北京机房全流量上线 |  |

截止目前，线上服务表现稳定。

<a id="use-cases-inside-baidu-use-case1--qa"></a>

# QA测试结论

1. 【性能测试】单机支持最大QPS：**9000+**。可以有效解决原来hulu\_pbrpc中一个慢服务拖垮所有服务的问题。性能很好。
2. 【稳定性测试】长时间压测没问题。

QA测试结论：通过

<a id="use-cases-inside-baidu-use-case1--section"></a>

# 性能提升实时统计

统计时间2015.11.3 15:00 – 2015.11.9 14:30，共**143.5**小时（近6天）不间断运行。北京机房升级前和升级后同机房各6台机器，共**12**台线上机器的Noah监控数据。

| 指标 | 升级**前**均值hulu\_pbrpc | 升级**后**均值brpc | 收益对比 | 说明 |
| --- | --- | --- | --- | --- |
| CPU占用率 | 67.35% | 29.28% | 降低**56.53**% |  |
| 内存占用 | 327.81MB | 336.91MB | 基本持平 |  |
| 鉴权平响(ms) | 0.605 | 0.208 | 降低**65.62**% |  |
| 转发平响(ms) | 22.49 | 23.18 | 基本持平 | 依赖后端各个服务的性能 |
| 总线程数 | 193 | 132 | 降低**31.61**% | Baidu RPC版本线程数使用率较低，还可降低 |
| 极限QPS | 3000 | 9000 | 提升**3**倍 | 线下使用Geoconv和Geocoder服务测试 |

**CPU使用率(%)**（红色为升级前，蓝色为升级后）
![img](assets/images/apicontrol-compare-1_99d4de8927d2fe98.png)

**内存使用量(KB)**（红色为升级前，蓝色为升级后）
![img](assets/images/apicontrol-compare-2_b0b5cb30ab2c890e.png)

**鉴权平响(ms)**（红色为升级前，蓝色为升级后）
![img](assets/images/apicontrol-compare-3_34c74b361afc4696.png)

**转发平响(ms)**（红色为升级前，蓝色为升级后）
![img](assets/images/apicontrol-compare-4_d45b76351372cd35.png)

**总线程数(个)**（红色为升级前，蓝色为升级后）
![img](assets/images/apicontrol-compare-5_9eb4af31601e18a5.png)

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="use-cases-inside-baidu-use-case2"></a>

<!-- source_url: https://brpc.apache.org/docs/use-cases-inside-baidu/use-case2/ -->

<!-- page_index: 86 -->

# 联盟DSP

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Use%20cases%20inside%20Baidu/Use%20case2/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=%e8%81%94%e7%9b%9fDSP)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# 联盟DSP

Use case2：联盟DSP

<a id="use-cases-inside-baidu-use-case2--section"></a>

# 背景

baidu-dsp是联盟基于Ad Exchange和RTB模式的需求方平台，服务大客户、代理的投放产品体系。我们改造了多个模块，均取得了显著的效果。本文只介绍其中关于super-nova-as的改动。super-nova-as是的baidu-dsp的AS，之前使用ub-aserver编写，为了尽量减少改动，我们没有改造整个as，而只是把super-nova-as连接下游（ctr-server、cvr-server、super-nova-bs）的client从ubrpc升级为brpc。

<a id="use-cases-inside-baidu-use-case2--section"></a>

# 结论

1. as的吞吐量有显著提升（不到1500 -> 2500+）
2. cpu优化：从1500qps 50%cpu\_idle提高到2000qps 50% cpu\_idle；
3. 超时率改善明显。

<a id="use-cases-inside-baidu-use-case2--section"></a>

# 测试过程

1. 环境：1个as，1个bs，1个ctr，1个cvr；部署情况为：bs单机部署，as+ctr+cvr混布；ctr和cvr为brpc版本
2. 分别采用1000,1500压力对ubrpc版本的as进行压测，发现1500压力下，as对bs有大量的超时，as到达瓶颈；
3. 分别采用2000,2500压力对brpc版本的as进行压测，发现2500压力下，as机器的cpu\_idle低于30%，as到达瓶颈。brpc对资源利用充分。

|  | ubrpc | brpc |
| --- | --- | --- |
| 流量 | img | img |
| bs成功率 | img | img |
| cpu\_idle | img | img |
| ctr成功率 | img | img |
| cvr成功率 | img | img |

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="use-cases-inside-baidu-use-case3"></a>

<!-- source_url: https://brpc.apache.org/docs/use-cases-inside-baidu/use-case3/ -->

<!-- page_index: 87 -->

# ELF学习框架

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Use%20cases%20inside%20Baidu/Use%20case3/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=ELF%e5%ad%a6%e4%b9%a0%e6%a1%86%e6%9e%b6)
 [Create project issue](https://github.com/apache/brpc/issues/new)

- [算法总耗时](#use-cases-inside-baidu-use-case3--section)
- [子任务耗时](#use-cases-inside-baidu-use-case3--section)
- [结论](#use-cases-inside-baidu-use-case3--1)

# ELF学习框架

Use case3：ELF学习框架

<a id="use-cases-inside-baidu-use-case3--section"></a>

# 背景

ELF(Essential/Extreme/Excellent Learning Framework) 框架为公司内外的大数据应用提供学习/挖掘算法开发支持。 平台主要包括数据迭代处理的框架支持，并行计算过程中的通信支持和用于存储大规模参数的分布式、快速、高可用参数服务器。应用于fcr-model，公有云bml，大数据实验室，语音技术部门等等。之前是基于[zeromq](http://zeromq.org/)封装的rpc，这次改用brpc。

<a id="use-cases-inside-baidu-use-case3--section"></a>

# 结论

单个rpc-call以及单次请求所有rpc-call的提升非常显著，延时都缩短了\*\*50%**以上，总训练的耗时除了ftrl-sync-no-shuffle提升不明显外，其余三个算法训练总体性能都有**15%\*\*左右的提升。现在瓶颈在于计算逻辑，所以相对单个的rpc的提升没有那么多。该成果后续会推动凤巢模型训练的上线替换。详细耗时见下节。

<a id="use-cases-inside-baidu-use-case3--section"></a>

# 性能对比报告

<a id="use-cases-inside-baidu-use-case3--section"></a>

## 算法总耗时

ftrl算法: 替换前总耗时2:4:39, 替换后总耗时1:42:48, 提升18%

ftrl-sync-no-shuffle算法: 替换前总耗时3:20:47, 替换后总耗时3:15:28, 提升2.5%

ftrl-sync算法: 替换前总耗时4:28:47, 替换后总耗时3:45:57, 提升16%

fm-sync算法: 替换前总耗时6:16:37, 替换后总耗时5:21:00, 提升14.6%

<a id="use-cases-inside-baidu-use-case3--section"></a>

## 子任务耗时

单个rpc-call(针对ftrl算法)

|  | Average | Max | Min |
| --- | --- | --- | --- |
| 替换前 | 164.946ms | 7938.76ms | 0.249756ms |
| 替换后 | 10.4198ms | 2614.38ms | 0.076416ms |
| 缩短 | 93% | 67% | 70% |

单次请求所有rpc-call(针对ftrl算法)

|  | Average | Max | Min |
| --- | --- | --- | --- |
| 替换前 | 658.08ms | 7123.5ms | 1.88159ms |
| 替换后 | 304.878 | 2571.34 | 0 |
| 缩短 | 53.7% | 63.9% |  |

<a id="use-cases-inside-baidu-use-case3--1"></a>

## 结论

单个rpc-call以及单次请求所有rpc-call的提升非常显著，提升都在50%以上，总任务的耗时除了ftrl-sync-no-shuffle提升不明显外，其余三个算法都有15%左右的提升，现在算法的瓶颈在于对计算逻辑，所以相对单个的rpc的提升没有那么多。

附cpu profiling结果, top 40没有rpc相关函数。

```
Total: 8664 samples
     755   8.7%   8.7%      757   8.7% baidu::elf::Partitioner
     709   8.2%  16.9%      724   8.4% baidu::elf::GlobalShardWriterClient::local_aggregator::{lambda#1}::operator [clone .part.1341]
     655   7.6%  24.5%      655   7.6% boost::detail::lcast_ret_unsigned
     582   6.7%  31.2%      642   7.4% baidu::elf::RobinHoodLinkedHashMap
     530   6.1%  37.3%     2023  23.4% std::vector
     529   6.1%  43.4%      529   6.1% std::binary_search
     406   4.7%  48.1%      458   5.3% tc_delete
     405   4.7%  52.8%     2454  28.3% baidu::elf::GlobalShardWriterClient
     297   3.4%  56.2%      297   3.4% __memcpy_sse2_unaligned
     256   3.0%  59.2%      297   3.4% tc_new
     198   2.3%  61.5%      853   9.8% std::__introsort_loop
     157   1.8%  63.3%      157   1.8% baidu::elf::GrowableArray
     152   1.8%  65.0%      177   2.0% calculate_grad
     142   1.6%  66.7%      699   8.1% baidu::elf::BlockTableReaderManager
     137   1.6%  68.2%      656   7.6% baidu::elf::DefaultWriterServer
     127   1.5%  69.7%      127   1.5% _init
     122   1.4%  71.1%      582   6.7% __gnu_cxx::__normal_iterator
     117   1.4%  72.5%      123   1.4% baidu::elf::GrowableArray::emplace_back
     116   1.3%  73.8%      116   1.3% baidu::elf::RobinHoodHashMap::insert
     101   1.2%  75.0%      451   5.2% baidu::elf::NoCacheReaderClient
      99   1.1%  76.1%     3614  41.7% parse_ins
      97   1.1%  77.2%       97   1.1% std::basic_string::_Rep::_M_dispose [clone .part.12]
      96   1.1%  78.3%      154   1.8% std::basic_string
      91   1.1%  79.4%      246   2.8% boost::algorithm::split_iterator
      87   1.0%  80.4%      321   3.7% boost::function2
      76   0.9%  81.3%      385   4.4% boost::detail::function::functor_manager
      69   0.8%  82.1%       69   0.8% std::locale::~locale
      63   0.7%  82.8%      319   3.7% std::__unguarded_linear_insert
      58   0.7%  83.5%     2178  25.2% boost::algorithm::split [clone .constprop.2471]
      54   0.6%  84.1%      100   1.2% std::vector::_M_emplace_back_aux
      49   0.6%  84.7%       49   0.6% boost::algorithm::detail::is_any_ofF
      47   0.5%  85.2%       79   0.9% baidu::elf::DefaultReaderServer
      41   0.5%  85.7%       41   0.5% std::locale::_S_initialize
      39   0.5%  86.1%      677   7.8% boost::detail::function::function_obj_invoker2
      39   0.5%  86.6%       39   0.5% memset
      39   0.5%  87.0%       39   0.5% std::locale::locale
      38   0.4%  87.5%       50   0.6% FTRLAggregator::serialize
      36   0.4%  87.9%       67   0.8% tcmalloc::CentralFreeList::ReleaseToSpans
      34   0.4%  88.3%       34   0.4% madvise
      34   0.4%  88.7%       38   0.4% tcmalloc::CentralFreeList::FetchFromOneSpans
      32   0.4%  89.0%       32   0.4% std::__insertion_sort
```

---

Last modified January 9, 2022: [A new verion of brpc website based on hugo (94b25d711)](https://github.com/apache/brpc-website/commit/94b25d7110944f3d4b2071b5188c691b23ffe3a9)

---

<a id="use-cases-inside-baidu-use-case4"></a>

<!-- source_url: https://brpc.apache.org/docs/use-cases-inside-baidu/use-case4/ -->

<!-- page_index: 88 -->

# 云平台代理服务

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/Use%20cases%20inside%20Baidu/Use%20case4/_index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=%e4%ba%91%e5%b9%b3%e5%8f%b0%e4%bb%a3%e7%90%86%e6%9c%8d%e5%8a%a1)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# 云平台代理服务

Use case4：云平台代理服务

<a id="use-cases-inside-baidu-use-case4--section"></a>

# 背景

云平台部把使用ubrpc的模块改造为使用brpc。由于使用了mcpack2pb的转换功能，这个模块既能被老的ubrpc client访问，也可以通过protobuf类的协议访问（baidu\_std，sofa\_pbrpc等）。

原有使用43台机器（对ubrpc也有富余），brpc使用3台机器即可（此时访问redis的io达到瓶颈）。当前流量4w qps，支持流量增长，考虑跨机房冗余，避免redis和vip瓶颈，brpc实际使用8台机器提供服务。

brpc改造后的connecter收益明显，可以用较少的机器提供更优质的服务。收益分3个方面：

<a id="use-cases-inside-baidu-use-case4--qps-latency"></a>

# 相同配置的机器qps和latency的比较

通过逐渐缩容，不断增加connecter的压力，获得单机qps和latency的对应数据如下：
![img](assets/images/ubrpc-compare-1_0a195c2f0d590d60.png)

机器配置：cpu: 24 Intel(R) Xeon(R) CPU E5645 @ 2.40GHz || mem: 64G

混布情况：同机部署了逻辑层2.0/3.0和C逻辑层，均有流量

图中可以看到随着压力的增大：

- brpc的延时，增加微乎其微，提供了较为一致的延时体验
- ubrpc的延时，快速增大，到了6000~8000qps的时候，出现*queue full*，服务不可用。

<a id="use-cases-inside-baidu-use-case4--qps"></a>

# 不同配置机器qps和延时的比较

qps固定为6500，观察延时。

| 机器名称 | 略 | 略 |
| --- | --- | --- |
| cpu | 24 Intel(R) Xeon(R) CPU E5645 @ 2.40GHz | 24 Intel(R) Xeon(R) CPU E5-2620 0 @ 2.00GHz |
| ubrpc | 8363.46（us） | 12649.5（us） |
| brpc | 3364.66（us） | 3382.15（us） |

有此可见：

- ubrpc在不同配置下性能表现差异大，在配置较低的机器下表现较差。
- brpc表现的比ubrpc好，在较低配置的机器上也能有好的表现，因机器不同带来的差异不大。

<a id="use-cases-inside-baidu-use-case4--idle"></a>

# 相同配置机器idle分布的比较

机器配置：cpu： 24 Intel(R) Xeon(R) CPU E5645 @ 2.40GHz || mem：64G

![img](assets/images/ubrpc-compare-2_a64a81e92d7f0a12.png)

在线上缩容 不断增大压力过程中：

- ubrpc cpu idle分布在35%~60%，在55%最集中，最低30%；
- brpc cpu idle分布在60%~85%，在75%最集中，最低50%； brpc比ubrpc对cpu的消耗低。

---

Last modified January 30, 2022: [bRPC website 1.0 (92b925e8f)](https://github.com/apache/brpc-website/commit/92b925e8fd3d8cd6c4fa35c4952566725017b914)

---

<a id="users"></a>

<!-- source_url: https://brpc.apache.org/docs/users/ -->

<!-- page_index: 89 -->

# Users

[Edit this page](https://github.com/apache/brpc-website/edit/master/content/en/docs/users/index.md)
 [Create documentation issue](https://github.com/apache/brpc-website/issues/new?title=Users)
 [Create project issue](https://github.com/apache/brpc/issues/new)

# Users

Providing your info on [Wanted: who’s using bRPC](https://github.com/apache/brpc/issues/1640) to help improving bRPC better

# Used by

  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Last modified April 18, 2023: [add didi into brpc users (#142) (76af27422)](https://github.com/apache/brpc-website/commit/76af2742206aa9fe0b68dad8913d789d72fca73a)

---
