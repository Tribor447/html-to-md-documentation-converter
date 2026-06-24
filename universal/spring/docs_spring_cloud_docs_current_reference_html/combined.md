# Appendix: Compendium of Configuration Properties

## Navigation

- [1. About the Documentation](#documentation-overview--documentation-about)
- [2. Getting Help](#documentation-overview--documentation-getting-help)
- Other pages
  
- [Untitled](#configprops)
  
- [Appendix: Compendium of Configuration Properties](#index)
  
- [Legal](#legal)

## Content

<a id="documentation-overview"></a>

<!-- source_url: https://docs.spring.io/spring-cloud/docs/current/reference/html/documentation-overview.html -->

<!-- page_index: 1 -->

# Spring Cloud Documentation

This section provides a brief overview of Spring Cloud reference documentation. It serves
as a map for the rest of the document.

<a id="documentation-overview--documentation-about"></a>
<a id="documentation-overview--1.-about-the-documentation"></a>

## [1. About the Documentation](#documentation-overview--documentation-about)

The Spring Cloud reference guide is available as

- [Multi-page HTML](https://docs.spring.io/spring-cloud/docs/2022.0.5/reference/html)
- [Single-page HTML](https://docs.spring.io/spring-cloud/docs/2022.0.5/reference/htmlsingle)
- [PDF](assets/files/spring-cloud_35de951a616acd5f.pdf)

Copies of this document may be made for your own use and for distribution to others, provided that you do not charge any fee for such copies and further provided that each
copy contains this Copyright Notice, whether distributed in print or electronically.

<a id="documentation-overview--documentation-getting-help"></a>
<a id="documentation-overview--2.-getting-help"></a>

## [2. Getting Help](#documentation-overview--documentation-getting-help)

If you have trouble with Spring Cloud, we would like to help.

- Learn the Spring Cloud basics. If you are
  starting out with Spring Cloud, try one of the [guides](https://spring.io/guides).
- Ask a question. We monitor [stackoverflow.com](https://stackoverflow.com) for questions
  tagged with [`spring-cloud`](https://stackoverflow.com/tags/spring-cloud).
- Chat with us at [Spring Cloud Gitter](https://gitter.im/spring-cloud/spring-cloud)

> [!NOTE]
> All of Spring Cloud is open source, including the documentation. If you find
> problems with the docs or if you want to improve them, please get involved.

---

<a id="configprops"></a>

<!-- source_url: https://docs.spring.io/spring-cloud/docs/current/reference/html/configprops.html -->

<!-- page_index: 2 -->

# Untitled

| Name | Default | Description |
| --- | --- | --- |
| eureka.client.eureka-connection-idle-timeout-seconds | `30` | Indicates how much time (in seconds) that the HTTP connections to eureka server can stay idle before it can be closed. In the AWS environment, it is recommended that the values is 30 seconds or less, since the firewall cleans up the connection information after a few mins leaving the connection hanging in limbo. |
| eureka.client.eureka-server-connect-timeout-seconds | `5` | Indicates how long to wait (in seconds) before a connection to eureka server needs to timeout. Note that the connections in the client are pooled by {@link HttpClient} and this setting affects the actual connection creation and also the wait time to get the connection from the pool. |
| eureka.client.eureka-server-d-n-s-name | `` | Gets the DNS name to be queried to get the list of eureka servers.This information is not required if the contract returns the service urls by implementing serviceUrls. The DNS mechanism is used when useDnsForFetchingServiceUrls is set to true and the eureka client expects the DNS to configured a certain way so that it can fetch changing eureka servers dynamically. The changes are effective at runtime. |
| eureka.client.eureka-server-port | `` | Gets the port to be used to construct the service url to contact eureka server when the list of eureka servers come from the DNS.This information is not required if the contract returns the service urls eurekaServerServiceUrls(String). The DNS mechanism is used when useDnsForFetchingServiceUrls is set to true and the eureka client expects the DNS to configured a certain way so that it can fetch changing eureka servers dynamically. The changes are effective at runtime. |
| eureka.client.eureka-server-read-timeout-seconds | `8` | Indicates how long to wait (in seconds) before a read from eureka server needs to timeout. |
| eureka.client.eureka-server-total-connections | `200` | Gets the total number of connections that is allowed from eureka client to all eureka servers. |
| eureka.client.eureka-server-total-connections-per-host | `50` | Gets the total number of connections that is allowed from eureka client to a eureka server host. |
| eureka.client.eureka-server-u-r-l-context | `` | Gets the URL context to be used to construct the service url to contact eureka server when the list of eureka servers come from the DNS. This information is not required if the contract returns the service urls from eurekaServerServiceUrls. The DNS mechanism is used when useDnsForFetchingServiceUrls is set to true and the eureka client expects the DNS to configured a certain way so that it can fetch changing eureka servers dynamically. The changes are effective at runtime. |
| eureka.client.eureka-service-url-poll-interval-seconds | `0` | Indicates how often(in seconds) to poll for changes to eureka server information. Eureka servers could be added or removed and this setting controls how soon the eureka clients should know about it. |
| eureka.client.prefer-same-zone-eureka | `true` | Indicates whether or not this instance should try to use the eureka server in the same zone for latency and/or other reason. Ideally eureka clients are configured to talk to servers in the same zone The changes are effective at runtime at the next registry fetch cycle as specified by registryFetchIntervalSeconds |
| eureka.client.register-with-eureka | `true` | Indicates whether or not this instance should register its information with eureka server for discovery by others. In some cases, you do not want your instances to be discovered whereas you just want do discover other instances. |
| eureka.server.peer-eureka-nodes-update-interval-ms | `0` |  |
| eureka.server.peer-eureka-status-refresh-time-interval-ms | `0` |  |
| spring.cloud.bus.ack.destination-service | `` | Service that wants to listen to acks. By default null (meaning all services). |
| spring.cloud.bus.ack.enabled | `true` | Flag to switch off acks (default on). |
| spring.cloud.bus.content-type | `` | The bus mime-type. |
| spring.cloud.bus.destination | `` | Name of Spring Cloud Stream destination for messages. |
| spring.cloud.bus.enabled | `true` | Flag to indicate that the bus is enabled. |
| spring.cloud.bus.env.enabled | `true` | Flag to switch off environment change events (default on). |
| spring.cloud.bus.id | `application` | The identifier for this application instance. |
| spring.cloud.bus.refresh.enabled | `true` | Flag to switch off refresh events (default on). |
| spring.cloud.bus.trace.enabled | `false` | Flag to switch on tracing of acks (default off). |
| spring.cloud.compatibility-verifier.compatible-boot-versions | `` | Default accepted versions for the Spring Boot dependency. You can set {@code x} for the patch version if you don't want to specify a concrete value. Example: {@code 3.4.x} |
| spring.cloud.compatibility-verifier.enabled | `false` | Enables creation of Spring Cloud compatibility verification. |
| spring.cloud.config.allow-override | `true` | Flag to indicate that {@link #isOverrideSystemProperties() systemPropertiesOverride} can be used. Set to false to prevent users from changing the default accidentally. Default true. |
| spring.cloud.config.allow-override | `true` | Flag to indicate that {@link #isOverrideSystemProperties() systemPropertiesOverride} can be used. Set to false to prevent users from changing the default accidentally. Default true. |
| spring.cloud.config.discovery.enabled | `false` | Flag to indicate that config server discovery is enabled (config server URL will be looked up via discovery). |
| spring.cloud.config.discovery.service-id | `configserver` | Service id to locate config server. |
| spring.cloud.config.enabled | `true` | Flag to say that remote configuration is enabled. Default true; |
| spring.cloud.config.fail-fast | `false` | Flag to indicate that failure to connect to the server is fatal (default false). |
| spring.cloud.config.headers | `` | Additional headers used to create the client request. |
| spring.cloud.config.initialize-on-context-refresh | `false` | Flag to initialize bootstrap configuration on context refresh event. Default false. |
| spring.cloud.config.initialize-on-context-refresh | `false` | Flag to initialize bootstrap configuration on context refresh event. Default false. |
| spring.cloud.config.label | `` | The label name to use to pull remote configuration properties. The default is set on the server (generally "main" for a git based server). |
| spring.cloud.config.media-type | `` | The Accept header media type to send to config server. |
| spring.cloud.config.multiple-uri-strategy | `` | The strategy to use when call to server fails and there are multiple URLs configured on the uri property (default {@link MultipleUriStrategy#ALWAYS}). |
| spring.cloud.config.name | `` | Name of application used to fetch remote properties. |
| spring.cloud.config.override-none | `false` | Flag to indicate that when {@link #setAllowOverride(boolean) allowOverride} is true, external properties should take lowest priority and should not override any existing property sources (including local config files). Default false. This will only have an effect when using config first bootstrap. |
| spring.cloud.config.override-none | `false` | Flag to indicate that when {@link #setAllowOverride(boolean) allowOverride} is true, external properties should take lowest priority and should not override any existing property sources (including local config files). Default false. This will only have an effect when using config first bootstrap. |
| spring.cloud.config.override-system-properties | `true` | Flag to indicate that the external properties should override system properties. Default true. |
| spring.cloud.config.override-system-properties | `true` | Flag to indicate that the external properties should override system properties. Default true. |
| spring.cloud.config.password | `` | The password to use (HTTP Basic) when contacting the remote server. |
| spring.cloud.config.profile | `default` | The default profile to use when fetching remote configuration (comma-separated). Default is "default". |
| spring.cloud.config.request-connect-timeout | `0` | timeout on waiting to connect to the Config Server. |
| spring.cloud.config.request-read-timeout | `0` | timeout on waiting to read data from the Config Server. |
| spring.cloud.config.retry.initial-interval | `1000` | Initial retry interval in milliseconds. |
| spring.cloud.config.retry.max-attempts | `6` | Maximum number of attempts. |
| spring.cloud.config.retry.max-interval | `2000` | Maximum interval for backoff. |
| spring.cloud.config.retry.multiplier | `1.1` | Multiplier for next interval. |
| spring.cloud.config.retry.use-random-policy | `false` | Use a random exponential backoff policy. |
| spring.cloud.config.send-state | `true` | Flag to indicate whether to send state. Default true. |
| spring.cloud.config.tls | `` | TLS properties. |
| spring.cloud.config.token | `` | Security Token passed thru to underlying environment repository. |
| spring.cloud.config.uri | `[http://localhost:8888]` | The URI of the remote server (default <http://localhost:8888>). |
| spring.cloud.config.username | `` | The username to use (HTTP Basic) when contacting the remote server. |
| spring.cloud.consul.config.acl-token | `` |  |
| spring.cloud.consul.config.data-key | `data` | If format is Format.PROPERTIES or Format.YAML then the following field is used as key to look up consul for configuration. |
| spring.cloud.consul.config.default-context | `application` |  |
| spring.cloud.consul.config.enabled | `true` |  |
| spring.cloud.consul.config.fail-fast | `true` | Throw exceptions during config lookup if true, otherwise, log warnings. |
| spring.cloud.consul.config.format | `` |  |
| spring.cloud.consul.config.name | `` | Alternative to spring.application.name to use in looking up values in consul KV. |
| spring.cloud.consul.config.prefix | `` |  |
| spring.cloud.consul.config.prefixes | `` |  |
| spring.cloud.consul.config.profile-separator | `,` |  |
| spring.cloud.consul.config.watch.delay | `1000` | The value of the fixed delay for the watch in millis. Defaults to 1000. |
| spring.cloud.consul.config.watch.enabled | `true` | If the watch is enabled. Defaults to true. |
| spring.cloud.consul.config.watch.wait-time | `55` | The number of seconds to wait (or block) for watch query, defaults to 55. Needs to be less than default ConsulClient (defaults to 60). To increase ConsulClient timeout create a ConsulClient bean with a custom ConsulRawClient with a custom HttpClient. |
| spring.cloud.consul.discovery.acl-token | `` |  |
| spring.cloud.consul.discovery.catalog-services-watch-delay | `1000` | The delay between calls to watch consul catalog in millis, default is 1000. |
| spring.cloud.consul.discovery.catalog-services-watch-timeout | `2` | The number of seconds to block while watching consul catalog, default is 2. |
| spring.cloud.consul.discovery.consistency-mode | `` | Consistency mode for health service request. |
| spring.cloud.consul.discovery.datacenters | `` | Map of serviceId's -> datacenter to query for in server list. This allows looking up services in another datacenters. |
| spring.cloud.consul.discovery.default-query-tag | `` | Tag to query for in service list if one is not listed in serverListQueryTags. Multiple tags can be specified with a comma separated value. |
| spring.cloud.consul.discovery.default-zone-metadata-name | `zone` | Service instance zone comes from metadata. This allows changing the metadata tag name. |
| spring.cloud.consul.discovery.deregister | `true` | Disable automatic de-registration of service in consul. |
| spring.cloud.consul.discovery.enable-tag-override | `` | Enable tag override for the registered service. |
| spring.cloud.consul.discovery.enabled | `true` | Is service discovery enabled? |
| spring.cloud.consul.discovery.fail-fast | `true` | Throw exceptions during service registration if true, otherwise, log warnings (defaults to true). |
| spring.cloud.consul.discovery.health-check-critical-timeout | `` | Timeout to deregister services critical for longer than timeout (e.g. 30m). Requires consul version 7.x or higher. |
| spring.cloud.consul.discovery.health-check-headers | `` | Headers to be applied to the Health Check calls. |
| spring.cloud.consul.discovery.health-check-interval | `10s` | How often to perform the health check (e.g. 10s), defaults to 10s. |
| spring.cloud.consul.discovery.health-check-path | `/actuator/health` | Alternate server path to invoke for health checking. |
| spring.cloud.consul.discovery.health-check-timeout | `` | Timeout for health check (e.g. 10s). |
| spring.cloud.consul.discovery.health-check-tls-skip-verify | `` | Skips certificate verification during service checks if true, otherwise runs certificate verification. |
| spring.cloud.consul.discovery.health-check-url | `` | Custom health check url to override default. |
| spring.cloud.consul.discovery.heartbeat.actuator-health-group | `` | The actuator health group to use (null for the root group) when determining system health via Actuator. |
| spring.cloud.consul.discovery.heartbeat.enabled | `false` |  |
| spring.cloud.consul.discovery.heartbeat.interval-ratio | `` |  |
| spring.cloud.consul.discovery.heartbeat.reregister-service-on-failure | `false` |  |
| spring.cloud.consul.discovery.heartbeat.ttl | `30s` |  |
| spring.cloud.consul.discovery.heartbeat.use-actuator-health | `true` | Whether or not to take the current system health (as reported via the Actuator Health endpoint) into account when reporting the application status to the Consul TTL check. Actuator Health endpoint also has to be available to the application. |
| spring.cloud.consul.discovery.hostname | `` | Hostname to use when accessing server. |
| spring.cloud.consul.discovery.include-hostname-in-instance-id | `false` | Whether hostname is included into the default instance id when registering service. |
| spring.cloud.consul.discovery.instance-group | `` | Service instance group. |
| spring.cloud.consul.discovery.instance-id | `` | Unique service instance id. |
| spring.cloud.consul.discovery.instance-zone | `` | Service instance zone. |
| spring.cloud.consul.discovery.ip-address | `` | IP address to use when accessing service (must also set preferIpAddress to use). |
| spring.cloud.consul.discovery.lifecycle.enabled | `true` |  |
| spring.cloud.consul.discovery.management-enable-tag-override | `` | Enable tag override for the registered management service. |
| spring.cloud.consul.discovery.management-metadata | `` | Metadata to use when registering management service. |
| spring.cloud.consul.discovery.management-port | `` | Port to register the management service under (defaults to management port). |
| spring.cloud.consul.discovery.management-suffix | `management` | Suffix to use when registering management service. |
| spring.cloud.consul.discovery.management-tags | `` | Tags to use when registering management service. |
| spring.cloud.consul.discovery.metadata | `` | Metadata to use when registering service. |
| spring.cloud.consul.discovery.order | `0` | Order of the discovery client used by `CompositeDiscoveryClient` for sorting available clients. |
| spring.cloud.consul.discovery.port | `` | Port to register the service under (defaults to listening port). |
| spring.cloud.consul.discovery.prefer-agent-address | `false` | Source of how we will determine the address to use. |
| spring.cloud.consul.discovery.prefer-ip-address | `false` | Use ip address rather than hostname during registration. |
| spring.cloud.consul.discovery.query-passing | `false` | Add the 'passing` parameter to /v1/health/service/serviceName. This pushes health check passing to the server. |
| spring.cloud.consul.discovery.register | `true` | Register as a service in consul. |
| spring.cloud.consul.discovery.register-health-check | `true` | Register health check in consul. Useful during development of a service. |
| spring.cloud.consul.discovery.scheme | `http` | Whether to register an http or https service. |
| spring.cloud.consul.discovery.server-list-query-tags | `` | Map of serviceId's -> tag to query for in server list. This allows filtering services by one more tags. Multiple tags can be specified with a comma separated value. |
| spring.cloud.consul.discovery.service-name | `` | Service name. |
| spring.cloud.consul.discovery.tags | `` | Tags to use when registering service. |
| spring.cloud.consul.enabled | `true` | Is spring cloud consul enabled. |
| spring.cloud.consul.host | `localhost` | Consul agent hostname. Defaults to 'localhost'. |
| spring.cloud.consul.path | `` | Custom path if consul is under non-root. |
| spring.cloud.consul.port | `8500` | Consul agent port. Defaults to '8500'. |
| spring.cloud.consul.retry.enabled | `true` | If consul retry is enabled. |
| spring.cloud.consul.retry.initial-interval | `1000` | Initial retry interval in milliseconds. |
| spring.cloud.consul.retry.max-attempts | `6` | Maximum number of attempts. |
| spring.cloud.consul.retry.max-interval | `2000` | Maximum interval for backoff. |
| spring.cloud.consul.retry.multiplier | `1.1` | Multiplier for next interval. |
| spring.cloud.consul.ribbon.enabled | `true` | Enables Consul and Ribbon integration. |
| spring.cloud.consul.scheme | `` | Consul agent scheme (HTTP/HTTPS). If there is no scheme in address - client will use HTTP. |
| spring.cloud.consul.service-registry.auto-registration.enabled | `true` | Enables Consul Service Registry Auto-registration. |
| spring.cloud.consul.service-registry.enabled | `true` | Enables Consul Service Registry functionality. |
| spring.cloud.consul.tls.certificate-password | `` | Password to open the certificate. |
| spring.cloud.consul.tls.certificate-path | `` | File path to the certificate. |
| spring.cloud.consul.tls.key-store-instance-type | `` | Type of key framework to use. |
| spring.cloud.consul.tls.key-store-password | `` | Password to an external keystore. |
| spring.cloud.consul.tls.key-store-path | `` | Path to an external keystore. |
| spring.cloud.decrypt-environment-post-processor.enabled | `true` | Enable the DecryptEnvironmentPostProcessor. |
| spring.cloud.discovery.client.composite-indicator.enabled | `true` | Enables discovery client composite health indicator. |
| spring.cloud.discovery.client.health-indicator.enabled | `true` |  |
| spring.cloud.discovery.client.health-indicator.include-description | `false` |  |
| spring.cloud.discovery.client.health-indicator.use-services-query | `true` | Whether or not the indicator should use {@link DiscoveryClient#getServices} to check its health. When set to {@code false} the indicator instead uses the lighter {@link DiscoveryClient#probe()}. This can be helpful in large deployments where the number of services returned makes the operation unnecessarily heavy. |
| spring.cloud.discovery.client.simple.instances | `` |  |
| spring.cloud.discovery.client.simple.local.host | `` |  |
| spring.cloud.discovery.client.simple.local.instance-id | `` |  |
| spring.cloud.discovery.client.simple.local.metadata | `` |  |
| spring.cloud.discovery.client.simple.local.port | `0` |  |
| spring.cloud.discovery.client.simple.local.secure | `false` |  |
| spring.cloud.discovery.client.simple.local.service-id | `` |  |
| spring.cloud.discovery.client.simple.local.uri | `` |  |
| spring.cloud.discovery.client.simple.order | `` |  |
| spring.cloud.discovery.enabled | `true` | Enables discovery client health indicators. |
| spring.cloud.features.enabled | `true` | Enables the features endpoint. |
| spring.cloud.gateway.default-filters | `` | List of filter definitions that are applied to every route. |
| spring.cloud.gateway.discovery.locator.enabled | `false` | Flag that enables DiscoveryClient gateway integration. |
| spring.cloud.gateway.discovery.locator.filters | `` |  |
| spring.cloud.gateway.discovery.locator.include-expression | `true` | SpEL expression that will evaluate whether to include a service in gateway integration or not, defaults to: true. |
| spring.cloud.gateway.discovery.locator.lower-case-service-id | `false` | Option to lower case serviceId in predicates and filters, defaults to false. Useful with eureka when it automatically uppercases serviceId. so MYSERIVCE, would match /myservice/\*\* |
| spring.cloud.gateway.discovery.locator.predicates | `` |  |
| spring.cloud.gateway.discovery.locator.route-id-prefix | `` | The prefix for the routeId, defaults to discoveryClient.getClass().getSimpleName() + "\_". Service Id will be appended to create the routeId. |
| spring.cloud.gateway.discovery.locator.url-expression | `'lb://'+serviceId` | SpEL expression that create the uri for each route, defaults to: 'lb://'+serviceId. |
| spring.cloud.gateway.enabled | `true` | Enables gateway functionality. |
| spring.cloud.gateway.fail-on-route-definition-error | `true` | Option to fail on route definition errors, defaults to true. Otherwise, a warning is logged. |
| spring.cloud.gateway.filter.add-request-header.enabled | `true` | Enables the add-request-header filter. |
| spring.cloud.gateway.filter.add-request-parameter.enabled | `true` | Enables the add-request-parameter filter. |
| spring.cloud.gateway.filter.add-response-header.enabled | `true` | Enables the add-response-header filter. |
| spring.cloud.gateway.filter.circuit-breaker.enabled | `true` | Enables the circuit-breaker filter. |
| spring.cloud.gateway.filter.dedupe-response-header.enabled | `true` | Enables the dedupe-response-header filter. |
| spring.cloud.gateway.filter.fallback-headers.enabled | `true` | Enables the fallback-headers filter. |
| spring.cloud.gateway.filter.hystrix.enabled | `true` | Enables the hystrix filter. |
| spring.cloud.gateway.filter.json-to-grpc.enabled | `true` | Enables the JSON to gRPC filter. |
| spring.cloud.gateway.filter.local-response-cache.enabled | `false` | Enables the local-response-cache filter. |
| spring.cloud.gateway.filter.local-response-cache.request.no-cache-strategy | `` |  |
| spring.cloud.gateway.filter.local-response-cache.size | `` | Maximum size of the cache to evict entries for this route (in KB, MB and GB). |
| spring.cloud.gateway.filter.local-response-cache.time-to-live | `5m` | Time to expire a cache entry (expressed in s for seconds, m for minutes, and h for hours). |
| spring.cloud.gateway.filter.map-request-header.enabled | `true` | Enables the map-request-header filter. |
| spring.cloud.gateway.filter.modify-request-body.enabled | `true` | Enables the modify-request-body filter. |
| spring.cloud.gateway.filter.modify-response-body.enabled | `true` | Enables the modify-response-body filter. |
| spring.cloud.gateway.filter.prefix-path.enabled | `true` | Enables the prefix-path filter. |
| spring.cloud.gateway.filter.preserve-host-header.enabled | `true` | Enables the preserve-host-header filter. |
| spring.cloud.gateway.filter.redirect-to.enabled | `true` | Enables the redirect-to filter. |
| spring.cloud.gateway.filter.remove-hop-by-hop.headers | `` |  |
| spring.cloud.gateway.filter.remove-hop-by-hop.order | `0` |  |
| spring.cloud.gateway.filter.remove-request-header.enabled | `true` | Enables the remove-request-header filter. |
| spring.cloud.gateway.filter.remove-request-parameter.enabled | `true` | Enables the remove-request-parameter filter. |
| spring.cloud.gateway.filter.remove-response-header.enabled | `true` | Enables the remove-response-header filter. |
| spring.cloud.gateway.filter.request-header-size.enabled | `true` | Enables the request-header-size filter. |
| spring.cloud.gateway.filter.request-header-to-request-uri.enabled | `true` | Enables the request-header-to-request-uri filter. |
| spring.cloud.gateway.filter.request-rate-limiter.default-key-resolver | `` |  |
| spring.cloud.gateway.filter.request-rate-limiter.default-rate-limiter | `` |  |
| spring.cloud.gateway.filter.request-rate-limiter.enabled | `true` | Enables the request-rate-limiter filter. |
| spring.cloud.gateway.filter.request-size.enabled | `true` | Enables the request-size filter. |
| spring.cloud.gateway.filter.retry.enabled | `true` | Enables the retry filter. |
| spring.cloud.gateway.filter.rewrite-location-response-header.enabled | `true` | Enables the rewrite-location-response-header filter. |
| spring.cloud.gateway.filter.rewrite-location.enabled | `true` | Enables the rewrite-location filter. |
| spring.cloud.gateway.filter.rewrite-path.enabled | `true` | Enables the rewrite-path filter. |
| spring.cloud.gateway.filter.rewrite-request-parameter.enabled | `true` | Enables the rewrite-request-parameter filter. |
| spring.cloud.gateway.filter.rewrite-response-header.enabled | `true` | Enables the rewrite-response-header filter. |
| spring.cloud.gateway.filter.save-session.enabled | `true` | Enables the save-session filter. |
| spring.cloud.gateway.filter.secure-headers.content-security-policy | `default-src 'self' https:; font-src 'self' https: data:; img-src 'self' https: data:; object-src 'none'; script-src https:; style-src 'self' https: 'unsafe-inline'` |  |
| spring.cloud.gateway.filter.secure-headers.content-type-options | `nosniff` |  |
| spring.cloud.gateway.filter.secure-headers.disable | `` |  |
| spring.cloud.gateway.filter.secure-headers.download-options | `noopen` |  |
| spring.cloud.gateway.filter.secure-headers.enabled | `true` | Enables the secure-headers filter. |
| spring.cloud.gateway.filter.secure-headers.frame-options | `DENY` |  |
| spring.cloud.gateway.filter.secure-headers.permitted-cross-domain-policies | `none` |  |
| spring.cloud.gateway.filter.secure-headers.referrer-policy | `no-referrer` |  |
| spring.cloud.gateway.filter.secure-headers.strict-transport-security | `max-age=631138519` |  |
| spring.cloud.gateway.filter.secure-headers.xss-protection-header | `1 ; mode=block` |  |
| spring.cloud.gateway.filter.set-path.enabled | `true` | Enables the set-path filter. |
| spring.cloud.gateway.filter.set-request-header.enabled | `true` | Enables the set-request-header filter. |
| spring.cloud.gateway.filter.set-request-host-header.enabled | `true` | Enables the set-request-host-header filter. |
| spring.cloud.gateway.filter.set-response-header.enabled | `true` | Enables the set-response-header filter. |
| spring.cloud.gateway.filter.set-status.enabled | `true` | Enables the set-status filter. |
| spring.cloud.gateway.filter.strip-prefix.enabled | `true` | Enables the strip-prefix filter. |
| spring.cloud.gateway.forwarded.enabled | `true` | Enables the ForwardedHeadersFilter. |
| spring.cloud.gateway.global-filter.adapt-cached-body.enabled | `true` | Enables the adapt-cached-body global filter. |
| spring.cloud.gateway.global-filter.forward-path.enabled | `true` | Enables the forward-path global filter. |
| spring.cloud.gateway.global-filter.forward-routing.enabled | `true` | Enables the forward-routing global filter. |
| spring.cloud.gateway.global-filter.load-balancer-client.enabled | `true` | Enables the load-balancer-client global filter. |
| spring.cloud.gateway.global-filter.local-response-cache.enabled | `true` | Enables the local-response-cache filter for all routes, it allows to add a specific configuration at route level using LocalResponseCache filter. |
| spring.cloud.gateway.global-filter.netty-routing.enabled | `true` | Enables the netty-routing global filter. |
| spring.cloud.gateway.global-filter.netty-write-response.enabled | `true` | Enables the netty-write-response global filter. |
| spring.cloud.gateway.global-filter.reactive-load-balancer-client.enabled | `true` | Enables the reactive-load-balancer-client global filter. |
| spring.cloud.gateway.global-filter.remove-cached-body.enabled | `true` | Enables the remove-cached-body global filter. |
| spring.cloud.gateway.global-filter.route-to-request-url.enabled | `true` | Enables the route-to-request-url global filter. |
| spring.cloud.gateway.global-filter.websocket-routing.enabled | `true` | Enables the websocket-routing global filter. |
| spring.cloud.gateway.globalcors.add-to-simple-url-handler-mapping | `false` | If global CORS config should be added to the URL handler. |
| spring.cloud.gateway.globalcors.cors-configurations | `` |  |
| spring.cloud.gateway.handler-mapping.order | `1` | The order of RoutePredicateHandlerMapping. |
| spring.cloud.gateway.httpclient.compression | `false` | Enables compression for Netty HttpClient. |
| spring.cloud.gateway.httpclient.connect-timeout | `` | The connect timeout in millis, the default is 30s. |
| spring.cloud.gateway.httpclient.max-header-size | `` | The max response header size. |
| spring.cloud.gateway.httpclient.max-initial-line-length | `` | The max initial line length. |
| spring.cloud.gateway.httpclient.pool.acquire-timeout | `` | Only for type FIXED, the maximum time in millis to wait for acquiring. |
| spring.cloud.gateway.httpclient.pool.eviction-interval | `0` | Perform regular eviction checks in the background at a specified interval. Disabled by default ({@link Duration#ZERO}) |
| spring.cloud.gateway.httpclient.pool.max-connections | `` | Only for type FIXED, the maximum number of connections before starting pending acquisition on existing ones. |
| spring.cloud.gateway.httpclient.pool.max-idle-time | `` | Time in millis after which the channel will be closed. If NULL, there is no max idle time. |
| spring.cloud.gateway.httpclient.pool.max-life-time | `` | Duration after which the channel will be closed. If NULL, there is no max life time. |
| spring.cloud.gateway.httpclient.pool.metrics | `false` | Enables channel pools metrics to be collected and registered in Micrometer. Disabled by default. |
| spring.cloud.gateway.httpclient.pool.name | `proxy` | The channel pool map name, defaults to proxy. |
| spring.cloud.gateway.httpclient.pool.type | `` | Type of pool for HttpClient to use, defaults to ELASTIC. |
| spring.cloud.gateway.httpclient.proxy.host | `` | Hostname for proxy configuration of Netty HttpClient. |
| spring.cloud.gateway.httpclient.proxy.non-proxy-hosts-pattern | `` | Regular expression (Java) for a configured list of hosts. that should be reached directly, bypassing the proxy |
| spring.cloud.gateway.httpclient.proxy.password | `` | Password for proxy configuration of Netty HttpClient. |
| spring.cloud.gateway.httpclient.proxy.port | `` | Port for proxy configuration of Netty HttpClient. |
| spring.cloud.gateway.httpclient.proxy.type | `` | proxyType for proxy configuration of Netty HttpClient. |
| spring.cloud.gateway.httpclient.proxy.username | `` | Username for proxy configuration of Netty HttpClient. |
| spring.cloud.gateway.httpclient.response-timeout | `` | The response timeout. |
| spring.cloud.gateway.httpclient.ssl.close-notify-flush-timeout | `3000ms` | SSL close\_notify flush timeout. Default to 3000 ms. |
| spring.cloud.gateway.httpclient.ssl.close-notify-read-timeout | `0` | SSL close\_notify read timeout. Default to 0 ms. |
| spring.cloud.gateway.httpclient.ssl.handshake-timeout | `10000ms` | SSL handshake timeout. Default to 10000 ms |
| spring.cloud.gateway.httpclient.ssl.key-password | `` | Key password, default is same as keyStorePassword. |
| spring.cloud.gateway.httpclient.ssl.key-store | `` | Keystore path for Netty HttpClient. |
| spring.cloud.gateway.httpclient.ssl.key-store-password | `` | Keystore password. |
| spring.cloud.gateway.httpclient.ssl.key-store-provider | `` | Keystore provider for Netty HttpClient, optional field. |
| spring.cloud.gateway.httpclient.ssl.key-store-type | `JKS` | Keystore type for Netty HttpClient, default is JKS. |
| spring.cloud.gateway.httpclient.ssl.trusted-x509-certificates | `` | Trusted certificates for verifying the remote endpoint's certificate. |
| spring.cloud.gateway.httpclient.ssl.use-insecure-trust-manager | `false` | Installs the netty InsecureTrustManagerFactory. This is insecure and not suitable for production. |
| spring.cloud.gateway.httpclient.websocket.max-frame-payload-length | `` | Max frame payload length. |
| spring.cloud.gateway.httpclient.websocket.proxy-ping | `true` | Proxy ping frames to downstream services, defaults to true. |
| spring.cloud.gateway.httpclient.wiretap | `false` | Enables wiretap debugging for Netty HttpClient. |
| spring.cloud.gateway.httpserver.wiretap | `false` | Enables wiretap debugging for Netty HttpServer. |
| spring.cloud.gateway.loadbalancer.use404 | `false` |  |
| spring.cloud.gateway.metrics.enabled | `false` | Enables the collection of metrics data. |
| spring.cloud.gateway.metrics.prefix | `spring.cloud.gateway` | The prefix of all metrics emitted by gateway. |
| spring.cloud.gateway.metrics.tags | `` | Tags map that added to metrics. |
| spring.cloud.gateway.observability.enabled | `true` | If Micrometer Observability support should be turned on. |
| spring.cloud.gateway.predicate.after.enabled | `true` | Enables the after predicate. |
| spring.cloud.gateway.predicate.before.enabled | `true` | Enables the before predicate. |
| spring.cloud.gateway.predicate.between.enabled | `true` | Enables the between predicate. |
| spring.cloud.gateway.predicate.cloud-foundry-route-service.enabled | `true` | Enables the cloud-foundry-route-service predicate. |
| spring.cloud.gateway.predicate.cookie.enabled | `true` | Enables the cookie predicate. |
| spring.cloud.gateway.predicate.header.enabled | `true` | Enables the header predicate. |
| spring.cloud.gateway.predicate.host.enabled | `true` | Enables the host predicate. |
| spring.cloud.gateway.predicate.method.enabled | `true` | Enables the method predicate. |
| spring.cloud.gateway.predicate.path.enabled | `true` | Enables the path predicate. |
| spring.cloud.gateway.predicate.query.enabled | `true` | Enables the query predicate. |
| spring.cloud.gateway.predicate.read-body.enabled | `true` | Enables the read-body predicate. |
| spring.cloud.gateway.predicate.remote-addr.enabled | `true` | Enables the remote-addr predicate. |
| spring.cloud.gateway.predicate.weight.enabled | `true` | Enables the weight predicate. |
| spring.cloud.gateway.predicate.xforwarded-remote-addr.enabled | `true` | Enables the xforwarded-remote-addr predicate. |
| spring.cloud.gateway.redis-rate-limiter.burst-capacity-header | `X-RateLimit-Burst-Capacity` | The name of the header that returns the burst capacity configuration. |
| spring.cloud.gateway.redis-rate-limiter.config | `` |  |
| spring.cloud.gateway.redis-rate-limiter.include-headers | `true` | Whether or not to include headers containing rate limiter information, defaults to true. |
| spring.cloud.gateway.redis-rate-limiter.remaining-header | `X-RateLimit-Remaining` | The name of the header that returns number of remaining requests during the current second. |
| spring.cloud.gateway.redis-rate-limiter.replenish-rate-header | `X-RateLimit-Replenish-Rate` | The name of the header that returns the replenish rate configuration. |
| spring.cloud.gateway.redis-rate-limiter.requested-tokens-header | `X-RateLimit-Requested-Tokens` | The name of the header that returns the requested tokens configuration. |
| spring.cloud.gateway.restrictive-property-accessor.enabled | `true` | Restricts method and property access in SpEL. |
| spring.cloud.gateway.routes | `` | List of Routes. |
| spring.cloud.gateway.set-status.original-status-header-name | `` | The name of the header which contains http code of the proxied request. |
| spring.cloud.gateway.streaming-media-types | `` |  |
| spring.cloud.gateway.x-forwarded.enabled | `true` | If the XForwardedHeadersFilter is enabled. |
| spring.cloud.gateway.x-forwarded.for-append | `true` | If appending X-Forwarded-For as a list is enabled. |
| spring.cloud.gateway.x-forwarded.for-enabled | `true` | If X-Forwarded-For is enabled. |
| spring.cloud.gateway.x-forwarded.host-append | `true` | If appending X-Forwarded-Host as a list is enabled. |
| spring.cloud.gateway.x-forwarded.host-enabled | `true` | If X-Forwarded-Host is enabled. |
| spring.cloud.gateway.x-forwarded.order | `0` | The order of the XForwardedHeadersFilter. |
| spring.cloud.gateway.x-forwarded.port-append | `true` | If appending X-Forwarded-Port as a list is enabled. |
| spring.cloud.gateway.x-forwarded.port-enabled | `true` | If X-Forwarded-Port is enabled. |
| spring.cloud.gateway.x-forwarded.prefix-append | `true` | If appending X-Forwarded-Prefix as a list is enabled. |
| spring.cloud.gateway.x-forwarded.prefix-enabled | `true` | If X-Forwarded-Prefix is enabled. |
| spring.cloud.gateway.x-forwarded.proto-append | `true` | If appending X-Forwarded-Proto as a list is enabled. |
| spring.cloud.gateway.x-forwarded.proto-enabled | `true` | If X-Forwarded-Proto is enabled. |
| spring.cloud.httpclientfactories.apache.enabled | `true` | Enables creation of Apache Http Client factory beans. |
| spring.cloud.httpclientfactories.ok.enabled | `true` | Enables creation of OK Http Client factory beans. |
| spring.cloud.hypermedia.refresh.fixed-delay | `5000` |  |
| spring.cloud.hypermedia.refresh.initial-delay | `10000` |  |
| spring.cloud.inetutils.default-hostname | `localhost` | The default hostname. Used in case of errors. |
| spring.cloud.inetutils.default-ip-address | `127.0.0.1` | The default IP address. Used in case of errors. |
| spring.cloud.inetutils.ignored-interfaces | `` | List of Java regular expressions for network interfaces that will be ignored. |
| spring.cloud.inetutils.preferred-networks | `` | List of Java regular expressions for network addresses that will be preferred. |
| spring.cloud.inetutils.timeout-seconds | `1` | Timeout, in seconds, for calculating hostname. |
| spring.cloud.inetutils.use-only-site-local-interfaces | `false` | Whether to use only interfaces with site local addresses. See {@link InetAddress#isSiteLocalAddress()} for more details. |
| spring.cloud.kubernetes.client.api-version | `` |  |
| spring.cloud.kubernetes.client.apiVersion | `v1` | Kubernetes API Version |
| spring.cloud.kubernetes.client.ca-cert-data | `` |  |
| spring.cloud.kubernetes.client.ca-cert-file | `` |  |
| spring.cloud.kubernetes.client.caCertData | `` | Kubernetes API CACertData |
| spring.cloud.kubernetes.client.caCertFile | `` | Kubernetes API CACertFile |
| spring.cloud.kubernetes.client.client-cert-data | `` |  |
| spring.cloud.kubernetes.client.client-cert-file | `` |  |
| spring.cloud.kubernetes.client.client-key-algo | `` |  |
| spring.cloud.kubernetes.client.client-key-data | `` |  |
| spring.cloud.kubernetes.client.client-key-file | `` |  |
| spring.cloud.kubernetes.client.client-key-passphrase | `` |  |
| spring.cloud.kubernetes.client.clientCertData | `` | Kubernetes API ClientCertData |
| spring.cloud.kubernetes.client.clientCertFile | `` | Kubernetes API ClientCertFile |
| spring.cloud.kubernetes.client.clientKeyAlgo | `RSA` | Kubernetes API ClientKeyAlgo |
| spring.cloud.kubernetes.client.clientKeyData | `` | Kubernetes API ClientKeyData |
| spring.cloud.kubernetes.client.clientKeyFile | `` | Kubernetes API ClientKeyFile |
| spring.cloud.kubernetes.client.clientKeyPassphrase | `changeit` | Kubernetes API ClientKeyPassphrase |
| spring.cloud.kubernetes.client.connection-timeout | `` |  |
| spring.cloud.kubernetes.client.connectionTimeout | `10s` | Connection timeout |
| spring.cloud.kubernetes.client.http-proxy | `` |  |
| spring.cloud.kubernetes.client.https-proxy | `` |  |
| spring.cloud.kubernetes.client.logging-interval | `` |  |
| spring.cloud.kubernetes.client.loggingInterval | `20s` | Logging interval |
| spring.cloud.kubernetes.client.master-url | `` |  |
| spring.cloud.kubernetes.client.masterUrl | `https://kubernetes.default.svc` | Kubernetes API Master Node URL |
| spring.cloud.kubernetes.client.namespace | `true` | Kubernetes Namespace |
| spring.cloud.kubernetes.client.no-proxy | `` |  |
| spring.cloud.kubernetes.client.oauth-token | `` |  |
| spring.cloud.kubernetes.client.oauthToken | `` | Kubernetes API Oauth Token |
| spring.cloud.kubernetes.client.password | `` | Kubernetes API Password |
| spring.cloud.kubernetes.client.proxy-password | `` |  |
| spring.cloud.kubernetes.client.proxy-username | `` |  |
| spring.cloud.kubernetes.client.request-timeout | `` |  |
| spring.cloud.kubernetes.client.requestTimeout | `10s` | Request timeout |
| spring.cloud.kubernetes.client.rolling-timeout | `` |  |
| spring.cloud.kubernetes.client.rollingTimeout | `900s` | Rolling timeout |
| spring.cloud.kubernetes.client.service-account-namespace-path | `/var/run/secrets/kubernetes.io/serviceaccount/namespace` |  |
| spring.cloud.kubernetes.client.trust-certs | `` |  |
| spring.cloud.kubernetes.client.trustCerts | `false` | Kubernetes API Trust Certificates |
| spring.cloud.kubernetes.client.user-agent | `Spring-Cloud-Kubernetes-Application` |  |
| spring.cloud.kubernetes.client.username | `` | Kubernetes API Username |
| spring.cloud.kubernetes.client.watch-reconnect-interval | `` |  |
| spring.cloud.kubernetes.client.watch-reconnect-limit | `` |  |
| spring.cloud.kubernetes.client.watchReconnectInterval | `1s` | Reconnect Interval |
| spring.cloud.kubernetes.client.watchReconnectLimit | `-1` | Reconnect Interval limit retries |
| spring.cloud.kubernetes.config.enable-api | `true` |  |
| spring.cloud.kubernetes.config.enabled | `true` | Enable the ConfigMap property source locator. |
| spring.cloud.kubernetes.config.fail-fast | `false` |  |
| spring.cloud.kubernetes.config.include-profile-specific-sources | `true` |  |
| spring.cloud.kubernetes.config.labels | `` |  |
| spring.cloud.kubernetes.config.name | `` |  |
| spring.cloud.kubernetes.config.namespace | `` |  |
| spring.cloud.kubernetes.config.paths | `` |  |
| spring.cloud.kubernetes.config.retry | `` |  |
| spring.cloud.kubernetes.config.sources | `` |  |
| spring.cloud.kubernetes.config.use-name-as-prefix | `false` |  |
| spring.cloud.kubernetes.discovery.all-namespaces | `false` |  |
| spring.cloud.kubernetes.discovery.cache-loading-timeout-seconds | `60` |  |
| spring.cloud.kubernetes.discovery.discovery-server-url | `` |  |
| spring.cloud.kubernetes.discovery.enabled | `true` |  |
| spring.cloud.kubernetes.discovery.filter | `` |  |
| spring.cloud.kubernetes.discovery.include-external-name-services | `false` |  |
| spring.cloud.kubernetes.discovery.include-not-ready-addresses | `false` |  |
| spring.cloud.kubernetes.discovery.known-secure-ports | `[443, 8443]` |  |
| spring.cloud.kubernetes.discovery.metadata.add-annotations | `true` |  |
| spring.cloud.kubernetes.discovery.metadata.add-labels | `true` |  |
| spring.cloud.kubernetes.discovery.metadata.add-pod-annotations | `false` |  |
| spring.cloud.kubernetes.discovery.metadata.add-pod-labels | `false` |  |
| spring.cloud.kubernetes.discovery.metadata.add-ports | `true` |  |
| spring.cloud.kubernetes.discovery.metadata.annotations-prefix | `` |  |
| spring.cloud.kubernetes.discovery.metadata.labels-prefix | `` |  |
| spring.cloud.kubernetes.discovery.metadata.ports-prefix | `port.` |  |
| spring.cloud.kubernetes.discovery.namespaces | `` |  |
| spring.cloud.kubernetes.discovery.order | `0` |  |
| spring.cloud.kubernetes.discovery.primary-port-name | `` |  |
| spring.cloud.kubernetes.discovery.service-labels | `` |  |
| spring.cloud.kubernetes.discovery.use-endpoint-slices | `false` |  |
| spring.cloud.kubernetes.discovery.wait-cache-ready | `true` |  |
| spring.cloud.kubernetes.leader.auto-startup | `true` | Should leader election be started automatically on startup. Default: true |
| spring.cloud.kubernetes.leader.config-map-name | `leaders` | Kubernetes ConfigMap where leaders information will be stored. Default: leaders |
| spring.cloud.kubernetes.leader.create-config-map | `true` | Enable/disable creating ConfigMap if it does not exist. Default: true |
| spring.cloud.kubernetes.leader.enabled | `true` | Should leader election be enabled. Default: true |
| spring.cloud.kubernetes.leader.leader-id-prefix | `leader.id.` | Leader id property prefix for the ConfigMap. Default: leader.id. |
| spring.cloud.kubernetes.leader.namespace | `` | Kubernetes namespace where the leaders ConfigMap and candidates are located. |
| spring.cloud.kubernetes.leader.publish-failed-events | `false` | Enable/disable publishing events in case leadership acquisition fails. Default: false |
| spring.cloud.kubernetes.leader.role | `` | Role for which leadership this candidate will compete. |
| spring.cloud.kubernetes.leader.update-period | `60000ms` | Leadership status check period. Default: 60s |
| spring.cloud.kubernetes.loadbalancer.cluster-domain | `cluster.local` | cluster domain. |
| spring.cloud.kubernetes.loadbalancer.enabled | `true` | Load balancer enabled,default true. |
| spring.cloud.kubernetes.loadbalancer.mode | `` | {@link KubernetesLoadBalancerMode} setting load balancer server list with ip of pod or service name. default value is POD. |
| spring.cloud.kubernetes.loadbalancer.port-name | `http` | service port name. |
| spring.cloud.kubernetes.reload.enable-reload-filtering | `false` |  |
| spring.cloud.kubernetes.reload.enabled | `false` |  |
| spring.cloud.kubernetes.reload.max-wait-for-restart | `2s` |  |
| spring.cloud.kubernetes.reload.mode | `EVENT` |  |
| spring.cloud.kubernetes.reload.monitoring-config-maps | `true` |  |
| spring.cloud.kubernetes.reload.monitoring-secrets | `false` |  |
| spring.cloud.kubernetes.reload.namespaces | `` |  |
| spring.cloud.kubernetes.reload.period | `15000ms` |  |
| spring.cloud.kubernetes.reload.strategy | `REFRESH` |  |
| spring.cloud.kubernetes.secrets.enable-api | `false` |  |
| spring.cloud.kubernetes.secrets.enabled | `true` | Enable the Secrets property source locator. |
| spring.cloud.kubernetes.secrets.fail-fast | `false` |  |
| spring.cloud.kubernetes.secrets.include-profile-specific-sources | `true` |  |
| spring.cloud.kubernetes.secrets.labels | `` |  |
| spring.cloud.kubernetes.secrets.name | `` |  |
| spring.cloud.kubernetes.secrets.namespace | `` |  |
| spring.cloud.kubernetes.secrets.paths | `` |  |
| spring.cloud.kubernetes.secrets.retry | `` |  |
| spring.cloud.kubernetes.secrets.sources | `` |  |
| spring.cloud.kubernetes.secrets.use-name-as-prefix | `false` |  |
| spring.cloud.loadbalancer.cache.caffeine.spec | `` | The spec to use to create caches. See CaffeineSpec for more details on the spec format. |
| spring.cloud.loadbalancer.cache.capacity | `256` | Initial cache capacity expressed as int. |
| spring.cloud.loadbalancer.cache.enabled | `true` | Enables Spring Cloud LoadBalancer caching mechanism. |
| spring.cloud.loadbalancer.cache.ttl | `35s` | Time To Live - time counted from writing of the record, after which cache entries are expired. |
| spring.cloud.loadbalancer.call-get-with-request-on-delegates | `false` | If this flag is set to {@code true}, {@code ServiceInstanceListSupplier#get(Request request)} method will be implemented to call {@code delegate.get(request)} in classes assignable from {@code DelegatingServiceInstanceListSupplier} that don't already implement that method, with the exclusion of {@code CachingServiceInstanceListSupplier} and {@code HealthCheckServiceInstanceListSupplier}, which should be placed in the instance supplier hierarchy directly after the supplier performing instance retrieval over the network, before any request-based filtering is done. Note: in 4.1, this behaviour will become the default |
| spring.cloud.loadbalancer.clients | `` |  |
| spring.cloud.loadbalancer.configurations | `default` | Enables a predefined LoadBalancer configuration. |
| spring.cloud.loadbalancer.eager-load.clients | `` | Names of the clients. |
| spring.cloud.loadbalancer.enabled | `true` | Enables Spring Cloud LoadBalancer. |
| spring.cloud.loadbalancer.eureka.approximate-zone-from-hostname | `false` | Used to determine whether we should try to get the `zone` value from host name. |
| spring.cloud.loadbalancer.health-check.initial-delay | `0` | Initial delay value for the HealthCheck scheduler. |
| spring.cloud.loadbalancer.health-check.interval | `25s` | Interval for rerunning the HealthCheck scheduler. |
| spring.cloud.loadbalancer.health-check.interval | `25s` | Interval for rerunning the HealthCheck scheduler. |
| spring.cloud.loadbalancer.health-check.path | `` | Path at which the health-check request should be made. Can be set up per `serviceId`. A `default` value can be set up as well. If none is set up, `/actuator/health` will be used. |
| spring.cloud.loadbalancer.health-check.port | `` | Path at which the health-check request should be made. If none is set, the port under which the requested service is available at the service instance. |
| spring.cloud.loadbalancer.health-check.refetch-instances | `false` | Indicates whether the instances should be refetched by the `HealthCheckServiceInstanceListSupplier`. This can be used if the instances can be updated and the underlying delegate does not provide an ongoing flux. |
| spring.cloud.loadbalancer.health-check.refetch-instances-interval | `25s` | Interval for refetching available service instances. |
| spring.cloud.loadbalancer.health-check.repeat-health-check | `true` | Indicates whether health checks should keep repeating. It might be useful to set it to `false` if periodically refetching the instances, as every refetch will also trigger a healthcheck. |
| spring.cloud.loadbalancer.health-check.update-results-list | `true` | Indicates whether the {@code healthCheckFlux} should emit on each alive {@link ServiceInstance} that has been retrieved. If set to {@code false}, the entire alive instances sequence is first collected into a list and only then emitted. |
| spring.cloud.loadbalancer.hint | `` | Allows setting the value of <code>hint</code> that is passed on to the LoadBalancer request and can subsequently be used in {@link ReactiveLoadBalancer} implementations. |
| spring.cloud.loadbalancer.hint-header-name | `X-SC-LB-Hint` | Allows setting the name of the header used for passing the hint for hint-based service instance filtering. |
| spring.cloud.loadbalancer.retry.avoid-previous-instance | `true` | Enables wrapping ServiceInstanceListSupplier beans with `RetryAwareServiceInstanceListSupplier` if Spring-Retry is in the classpath. |
| spring.cloud.loadbalancer.retry.backoff.enabled | `false` | Indicates whether Reactor Retry backoffs should be applied. |
| spring.cloud.loadbalancer.retry.backoff.jitter | `0.5` | Used to set `RetryBackoffSpec.jitter`. |
| spring.cloud.loadbalancer.retry.backoff.max-backoff | `Long.MAX ms` | Used to set `RetryBackoffSpec.maxBackoff`. |
| spring.cloud.loadbalancer.retry.backoff.min-backoff | `5 ms` | Used to set `RetryBackoffSpec#minBackoff`. |
| spring.cloud.loadbalancer.retry.enabled | `true` | Enables LoadBalancer retries. |
| spring.cloud.loadbalancer.retry.max-retries-on-next-service-instance | `1` | Number of retries to be executed on the next `ServiceInstance`. A `ServiceInstance` is chosen before each retry call. |
| spring.cloud.loadbalancer.retry.max-retries-on-same-service-instance | `0` | Number of retries to be executed on the same `ServiceInstance`. |
| spring.cloud.loadbalancer.retry.retry-on-all-exceptions | `false` | Indicates retries should be attempted for all exceptions, not only those specified in `retryableExceptions`. |
| spring.cloud.loadbalancer.retry.retry-on-all-operations | `false` | Indicates retries should be attempted on operations other than `HttpMethod.GET`. |
| spring.cloud.loadbalancer.retry.retryable-exceptions | `{}` | A `Set` of `Throwable` classes that should trigger a retry. |
| spring.cloud.loadbalancer.retry.retryable-status-codes | `{}` | A `Set` of status codes that should trigger a retry. |
| spring.cloud.loadbalancer.service-discovery.timeout | `` | String representation of Duration of the timeout for calls to service discovery. |
| spring.cloud.loadbalancer.stats.micrometer.enabled | `false` | Enables Spring Cloud LoadBalancer Micrometer stats. |
| spring.cloud.loadbalancer.sticky-session.add-service-instance-cookie | `false` | Indicates whether a cookie with the newly selected instance should be added by LoadBalancer. |
| spring.cloud.loadbalancer.sticky-session.instance-id-cookie-name | `sc-lb-instance-id` | The name of the cookie holding the preferred instance id. |
| spring.cloud.loadbalancer.x-forwarded.enabled | `false` | To Enable X-Forwarded Headers. |
| spring.cloud.loadbalancer.zone | `` | Spring Cloud LoadBalancer zone. |
| spring.cloud.openfeign.autoconfiguration.jackson.enabled | `false` | If true, PageJacksonModule and SortJacksonModule bean will be provided for Jackson page decoding. |
| spring.cloud.openfeign.circuitbreaker.enabled | `false` | If true, an OpenFeign client will be wrapped with a Spring Cloud CircuitBreaker circuit breaker. |
| spring.cloud.openfeign.circuitbreaker.group.enabled | `false` | If true, an OpenFeign client will be wrapped with a Spring Cloud CircuitBreaker circuit breaker with with group. |
| spring.cloud.openfeign.client.config | `` |  |
| spring.cloud.openfeign.client.decode-slash | `true` | Feign clients do not encode slash `/` characters by default. To change this behavior, set the `decodeSlash` to `false`. |
| spring.cloud.openfeign.client.default-config | `default` |  |
| spring.cloud.openfeign.client.default-to-properties | `true` |  |
| spring.cloud.openfeign.client.refresh-enabled | `false` | Enables options value refresh capability for Feign. |
| spring.cloud.openfeign.compression.request.enabled | `false` | Enables the request sent by Feign to be compressed. |
| spring.cloud.openfeign.compression.request.mime-types | `[text/xml, application/xml, application/json]` | The list of supported mime types. |
| spring.cloud.openfeign.compression.request.min-request-size | `2048` | The minimum threshold content size. |
| spring.cloud.openfeign.compression.response.enabled | `false` | Enables the response from Feign to be compressed. |
| spring.cloud.openfeign.encoder.charset-from-content-type | `false` | Indicates whether the charset should be derived from the {@code Content-Type} header. |
| spring.cloud.openfeign.httpclient.connection-timeout | `2000` |  |
| spring.cloud.openfeign.httpclient.connection-timer-repeat | `3000` |  |
| spring.cloud.openfeign.httpclient.disable-ssl-validation | `false` |  |
| spring.cloud.openfeign.httpclient.enabled | `true` | Enables the use of the Apache HTTP Client by Feign. |
| spring.cloud.openfeign.httpclient.follow-redirects | `true` |  |
| spring.cloud.openfeign.httpclient.hc5.enabled | `true` | Enables the use of the Apache HTTP Client 5 by Feign. |
| spring.cloud.openfeign.httpclient.hc5.pool-concurrency-policy | `` | Pool concurrency policies. |
| spring.cloud.openfeign.httpclient.hc5.pool-reuse-policy | `` | Pool connection re-use policies. |
| spring.cloud.openfeign.httpclient.hc5.socket-timeout | `5` | Default value for socket timeout. |
| spring.cloud.openfeign.httpclient.hc5.socket-timeout-unit | `` | Default value for socket timeout unit. |
| spring.cloud.openfeign.httpclient.max-connections | `200` |  |
| spring.cloud.openfeign.httpclient.max-connections-per-route | `50` |  |
| spring.cloud.openfeign.httpclient.ok-http.read-timeout | `60s` | {@link OkHttpClient} read timeout; defaults to 60 seconds. |
| spring.cloud.openfeign.httpclient.time-to-live | `900` |  |
| spring.cloud.openfeign.httpclient.time-to-live-unit | `` |  |
| spring.cloud.openfeign.micrometer.enabled | `true` | Enables Micrometer capabilities for Feign. |
| spring.cloud.openfeign.oauth2.enabled | `false` | Enables feign interceptor for managing oauth2 access token. |
| spring.cloud.openfeign.oauth2.load-balanced | `false` | Enables load balancing for oauth2 access token provider. |
| spring.cloud.openfeign.okhttp.enabled | `false` | Enables the use of the OK HTTP Client by Feign. |
| spring.cloud.refresh.additional-property-sources-to-retain | `` | Additional property sources to retain during a refresh. Typically only system property sources are retained. This property allows property sources, such as property sources created by EnvironmentPostProcessors to be retained as well. |
| spring.cloud.refresh.enabled | `true` | Enables autoconfiguration for the refresh scope and associated features. |
| spring.cloud.refresh.extra-refreshable | `true` | Additional class names for beans to post process into refresh scope. |
| spring.cloud.refresh.never-refreshable | `true` | Comma separated list of class names for beans to never be refreshed or rebound. |
| spring.cloud.service-registry.auto-registration.enabled | `true` | Whether service auto-registration is enabled. Defaults to true. |
| spring.cloud.service-registry.auto-registration.fail-fast | `false` | Whether startup fails if there is no AutoServiceRegistration. Defaults to false. |
| spring.cloud.service-registry.auto-registration.register-management | `true` | Whether to register the management as a service. Defaults to true. |
| spring.cloud.stream.binders | `` | Additional per-binder properties (see {@link BinderProperties}) if more then one binder of the same type is used (i.e., connect to multiple instances of RabbitMq). Here you can specify multiple binder configurations, each with different environment settings. For example; spring.cloud.stream.binders.rabbit1.environment. . . , spring.cloud.stream.binders.rabbit2.environment. . . |
| spring.cloud.stream.binding-retry-interval | `30` | Retry interval (in seconds) used to schedule binding attempts. Default: 30 sec. |
| spring.cloud.stream.bindings | `` | Additional binding properties (see {@link BinderProperties}) per binding name (e.g., 'input`). For example; This sets the content-type for the 'input' binding of a Sink application: 'spring.cloud.stream.bindings.input.contentType=text/plain' |
| spring.cloud.stream.default-binder | `` | The name of the binder to use by all bindings in the event multiple binders available (e.g., 'rabbit'). |
| spring.cloud.stream.dynamic-destination-cache-size | `10` | The maximum size of Least Recently Used (LRU) cache of dynamic destinations. Once this size is reached, new destinations will trigger the removal of old destinations. Default: 10 |
| spring.cloud.stream.dynamic-destinations | `[]` | A list of destinations that can be bound dynamically. If set, only listed destinations can be bound. |
| spring.cloud.stream.function.bindings | `` |  |
| spring.cloud.stream.input-bindings | `` | A semi-colon delimited string to explicitly define input bindings (specifically for cases when there is no implicit trigger to create such bindings such as Function, Supplier or Consumer). |
| spring.cloud.stream.instance-count | `1` | The number of deployed instances of an application. Default: 1. NOTE: Could also be managed per individual binding "spring.cloud.stream.bindings.foo.consumer.instance-count" where 'foo' is the name of the binding. |
| spring.cloud.stream.instance-index | `0` | The instance id of the application: a number from 0 to instanceCount-1. Used for partitioning and with Kafka. NOTE: Could also be managed per individual binding "spring.cloud.stream.bindings.foo.consumer.instance-index" where 'foo' is the name of the binding. |
| spring.cloud.stream.instance-index-list | `` | A list of instance id's from 0 to instanceCount-1. Used for partitioning and with Kafka. NOTE: Could also be managed per individual binding "spring.cloud.stream.bindings.foo.consumer.instance-index-list" where 'foo' is the name of the binding. This setting will override the one set in 'spring.cloud.stream.instance-index' |
| spring.cloud.stream.integration.message-handler-not-propagated-headers | `` | Message header names that will NOT be copied from the inbound message. |
| spring.cloud.stream.output-bindings | `` | A semi-colon delimited string to explicitly define output bindings (specifically for cases when there is no implicit trigger to create such bindings such as Function, Supplier or Consumer). |
| spring.cloud.stream.override-cloud-connectors | `false` | This property is only applicable when the cloud profile is active and Spring Cloud Connectors are provided with the application. If the property is false (the default), the binder detects a suitable bound service (for example, a RabbitMQ service bound in Cloud Foundry for the RabbitMQ binder) and uses it for creating connections (usually through Spring Cloud Connectors). When set to true, this property instructs binders to completely ignore the bound services and rely on Spring Boot properties (for example, relying on the spring.rabbitmq.\* properties provided in the environment for the RabbitMQ binder). The typical usage of this property is to be nested in a customized environment when connecting to multiple systems. |
| spring.cloud.stream.pollable-source | `none` | A semi-colon delimited list of binding names of pollable sources. Binding names follow the same naming convention as functions. For example, name '…pollable-source=foobar' will be accessible as 'foobar-iin-0'' binding |
| spring.cloud.stream.sendto.destination | `none` | The name of the header used to determine the name of the output destination |
| spring.cloud.stream.source | `` | A semi-colon delimited string representing the names of the sources based on which source bindings will be created. This is primarily to support cases where source binding may be required without providing a corresponding Supplier. (e.g., for cases where the actual source of data is outside of scope of spring-cloud-stream - HTTP -> Stream) @deprecated use {@link #outputBindings} |
| spring.cloud.task.batch.application-runner-order | `0` | The order for the {@code ApplicationRunner} used to run batch jobs when {@code spring.cloud.task.batch.fail-on-job-failure=true}. Defaults to 0 (same as the {@link org.springframework.boot.autoconfigure.batch.JobLauncherApplicationRunner}). |
| spring.cloud.task.batch.command-line-runner-order | `` |  |
| spring.cloud.task.batch.events.chunk-event-binding-name | `chunk-events` |  |
| spring.cloud.task.batch.events.chunk-order | `` | Establishes the default {@link Ordered} precedence for {@link org.springframework.batch.core.ChunkListener}. |
| spring.cloud.task.batch.events.chunk.enabled | `true` | This property is used to determine if a task should listen for batch chunk events. |
| spring.cloud.task.batch.events.enabled | `true` | This property is used to determine if a task should listen for batch events. |
| spring.cloud.task.batch.events.item-process-event-binding-name | `item-process-events` |  |
| spring.cloud.task.batch.events.item-process-order | `` | Establishes the default {@link Ordered} precedence for {@link org.springframework.batch.core.ItemProcessListener}. |
| spring.cloud.task.batch.events.item-process.enabled | `true` | This property is used to determine if a task should listen for batch item processed events. |
| spring.cloud.task.batch.events.item-read-event-binding-name | `item-read-events` |  |
| spring.cloud.task.batch.events.item-read-order | `` | Establishes the default {@link Ordered} precedence for {@link org.springframework.batch.core.ItemReadListener}. |
| spring.cloud.task.batch.events.item-read.enabled | `true` | This property is used to determine if a task should listen for batch item read events. |
| spring.cloud.task.batch.events.item-write-event-binding-name | `item-write-events` |  |
| spring.cloud.task.batch.events.item-write-order | `` | Establishes the default {@link Ordered} precedence for {@link org.springframework.batch.core.ItemWriteListener}. |
| spring.cloud.task.batch.events.item-write.enabled | `true` | This property is used to determine if a task should listen for batch item write events. |
| spring.cloud.task.batch.events.job-execution-event-binding-name | `job-execution-events` |  |
| spring.cloud.task.batch.events.job-execution-order | `` | Establishes the default {@link Ordered} precedence for {@link org.springframework.batch.core.JobExecutionListener}. |
| spring.cloud.task.batch.events.job-execution.enabled | `true` | This property is used to determine if a task should listen for batch job execution events. |
| spring.cloud.task.batch.events.skip-event-binding-name | `skip-events` |  |
| spring.cloud.task.batch.events.skip-order | `` | Establishes the default {@link Ordered} precedence for {@link org.springframework.batch.core.SkipListener}. |
| spring.cloud.task.batch.events.skip.enabled | `true` | This property is used to determine if a task should listen for batch skip events. |
| spring.cloud.task.batch.events.step-execution-event-binding-name | `step-execution-events` |  |
| spring.cloud.task.batch.events.step-execution-order | `` | Establishes the default {@link Ordered} precedence for {@link org.springframework.batch.core.StepExecutionListener}. |
| spring.cloud.task.batch.events.step-execution.enabled | `true` | This property is used to determine if a task should listen for batch step execution events. |
| spring.cloud.task.batch.events.task-event-binding-name | `task-events` |  |
| spring.cloud.task.batch.fail-on-job-failure | `false` | This property is used to determine if a task app should return with a non zero exit code if a batch job fails. |
| spring.cloud.task.batch.fail-on-job-failure-poll-interval | `5000` | Fixed delay in milliseconds that Spring Cloud Task will wait when checking if {@link org.springframework.batch.core.JobExecution}s have completed, when spring.cloud.task.batch.failOnJobFailure is set to true. Defaults to 5000. |
| spring.cloud.task.batch.job-names | `` | Comma-separated list of job names to execute on startup (for instance, `job1,job2`). By default, all Jobs found in the context are executed. @deprecated use spring.batch.job.name instead of spring.cloud.task.batch.jobNames. |
| spring.cloud.task.batch.listener.enabled | `true` | This property is used to determine if a task will be linked to the batch jobs that are run. |
| spring.cloud.task.closecontext-enabled | `false` | When set to true the context is closed at the end of the task. Else the context remains open. |
| spring.cloud.task.events.enabled | `true` | This property is used to determine if a task app should emit task events. |
| spring.cloud.task.executionid | `` | An id that will be used by the task when updating the task execution. |
| spring.cloud.task.external-execution-id | `` | An id that can be associated with a task. |
| spring.cloud.task.initialize-enabled | `` | If set to true then tables are initialized. If set to false tables are not initialized. Defaults to null. The requirement for it to be defaulted to null is so that we can support the <code>spring.cloud.task.initialize.enable</code> until it is removed. |
| spring.cloud.task.parent-execution-id | `` | The id of the parent task execution id that launched this task execution. Defaults to null if task execution had no parent. |
| spring.cloud.task.single-instance-enabled | `false` | This property is used to determine if a task will execute if another task with the same app name is running. |
| spring.cloud.task.single-instance-lock-check-interval | `500` | Declares the time (in millis) that a task execution will wait between checks. Default time is: 500 millis. |
| spring.cloud.task.single-instance-lock-ttl | `` | Declares the maximum amount of time (in millis) that a task execution can hold a lock to prevent another task from executing with a specific task name when the single-instance-enabled is set to true. Default time is: Integer.MAX\_VALUE. |
| spring.cloud.task.table-prefix | `TASK_` | The prefix to append to the table names created by Spring Cloud Task. |
| spring.cloud.util.enabled | `true` | Enables creation of Spring Cloud utility beans. |
| spring.cloud.vault.app-id.app-id-path | `app-id` | Mount path of the AppId authentication backend. |
| spring.cloud.vault.app-id.network-interface | `` | Network interface hint for the "MAC\_ADDRESS" UserId mechanism. |
| spring.cloud.vault.app-id.user-id | `MAC_ADDRESS` | UserId mechanism. Can be either "MAC\_ADDRESS", "IP\_ADDRESS", a string or a class name. |
| spring.cloud.vault.app-role.app-role-path | `approle` | Mount path of the AppRole authentication backend. |
| spring.cloud.vault.app-role.role | `` | Name of the role, optional, used for pull-mode. |
| spring.cloud.vault.app-role.role-id | `` | The RoleId. |
| spring.cloud.vault.app-role.secret-id | `` | The SecretId. |
| spring.cloud.vault.application-name | `application` | Application name for AppId authentication. |
| spring.cloud.vault.authentication | `` |  |
| spring.cloud.vault.aws-ec2.aws-ec2-path | `aws-ec2` | Mount path of the AWS-EC2 authentication backend. |
| spring.cloud.vault.aws-ec2.identity-document | `http://169.254.169.254/latest/dynamic/instance-identity/pkcs7` | URL of the AWS-EC2 PKCS7 identity document. |
| spring.cloud.vault.aws-ec2.nonce | `` | Nonce used for AWS-EC2 authentication. An empty nonce defaults to nonce generation. |
| spring.cloud.vault.aws-ec2.role | `` | Name of the role, optional. |
| spring.cloud.vault.aws-iam.aws-path | `aws` | Mount path of the AWS authentication backend. |
| spring.cloud.vault.aws-iam.endpoint-uri | `` | STS server URI. @since 2.2 |
| spring.cloud.vault.aws-iam.region | `` | Name of the region, optional. Inferred by AWS defaults if not set. @since 4.0.1 |
| spring.cloud.vault.aws-iam.role | `` | Name of the role, optional. Defaults to the friendly IAM name if not set. |
| spring.cloud.vault.aws-iam.server-name | `` | Name of the server used to set {@code X-Vault-AWS-IAM-Server-ID} header in the headers of login requests. |
| spring.cloud.vault.aws.access-key-property | `cloud.aws.credentials.accessKey` | Target property for the obtained access key. |
| spring.cloud.vault.aws.backend | `aws` | aws backend path. |
| spring.cloud.vault.aws.credential-type | `` | aws credential type |
| spring.cloud.vault.aws.enabled | `false` | Enable aws backend usage. |
| spring.cloud.vault.aws.role | `` | Role name for credentials. |
| spring.cloud.vault.aws.role-arn | `` | Role arn for assumed\_role in case we have multiple roles associated with the vault role. @since 3.0.2 |
| spring.cloud.vault.aws.secret-key-property | `cloud.aws.credentials.secretKey` | Target property for the obtained secret key. |
| spring.cloud.vault.aws.session-token-key-property | `cloud.aws.credentials.sessionToken` | Target property for the obtained secret key. |
| spring.cloud.vault.aws.ttl | `0` | TTL for sts tokens. Defaults to whatever the vault Role may have for Max. Also limited to what AWS supports to be the max for STS. @since 3.0.2 |
| spring.cloud.vault.azure-msi.azure-path | `azure` | Mount path of the Azure MSI authentication backend. |
| spring.cloud.vault.azure-msi.identity-token-service | `` | Identity token service URI. @since 3.0 |
| spring.cloud.vault.azure-msi.metadata-service | `` | Instance metadata service URI. @since 3.0 |
| spring.cloud.vault.azure-msi.role | `` | Name of the role. |
| spring.cloud.vault.cassandra.backend | `cassandra` | Cassandra backend path. |
| spring.cloud.vault.cassandra.enabled | `false` | Enable cassandra backend usage. |
| spring.cloud.vault.cassandra.password-property | `spring.data.cassandra.password` | Target property for the obtained password. |
| spring.cloud.vault.cassandra.role | `` | Role name for credentials. |
| spring.cloud.vault.cassandra.static-role | `false` | Enable static role usage. @since 2.2 |
| spring.cloud.vault.cassandra.username-property | `spring.data.cassandra.username` | Target property for the obtained username. |
| spring.cloud.vault.config.lifecycle.enabled | `true` | Enable lifecycle management. |
| spring.cloud.vault.config.lifecycle.expiry-threshold | `` | The expiry threshold. {@link Lease} is renewed the given {@link Duration} before it expires. @since 2.2 |
| spring.cloud.vault.config.lifecycle.lease-endpoints | `` | Set the {@link LeaseEndpoints} to delegate renewal/revocation calls to. {@link LeaseEndpoints} encapsulates differences between Vault versions that affect the location of renewal/revocation endpoints. Can be {@link LeaseEndpoints#SysLeases} for version 0.8 or above of Vault or {@link LeaseEndpoints#Legacy} for older versions (the default). @since 2.2 |
| spring.cloud.vault.config.lifecycle.lease-strategy | `` | Sets the {@link LeaseStrategy} to be used with {@link org.springframework.vault.core.lease.SecretLeaseContainer#setLeaseStrategy(LeaseStrategy)} to retain or drop tokens on renewal errors. @since 4.0.4 |
| spring.cloud.vault.config.lifecycle.min-renewal | `` | The time period that is at least required before renewing a lease. @since 2.2 |
| spring.cloud.vault.config.order | `0` | Used to set a {@link org.springframework.core.env.PropertySource} priority. This is useful to use Vault as an override on other property sources. @see org.springframework.core.PriorityOrdered |
| spring.cloud.vault.connection-timeout | `5000` | Connection timeout. |
| spring.cloud.vault.consul.backend | `consul` | Consul backend path. |
| spring.cloud.vault.consul.enabled | `false` | Enable consul backend usage. |
| spring.cloud.vault.consul.role | `` | Role name for credentials. |
| spring.cloud.vault.consul.token-property | `spring.cloud.consul.token` | Target property for the obtained token. |
| spring.cloud.vault.couchbase.backend | `database` | Couchbase backend path. |
| spring.cloud.vault.couchbase.enabled | `false` | Enable couchbase backend usage. |
| spring.cloud.vault.couchbase.password-property | `spring.couchbase.password` | Target property for the obtained password. |
| spring.cloud.vault.couchbase.role | `` | Role name for credentials. |
| spring.cloud.vault.couchbase.static-role | `false` | Enable static role usage. |
| spring.cloud.vault.couchbase.username-property | `spring.couchbase.username` | Target property for the obtained username. |
| spring.cloud.vault.database.backend | `database` | Database backend path. |
| spring.cloud.vault.database.enabled | `false` | Enable database backend usage. |
| spring.cloud.vault.database.password-property | `spring.datasource.password` | Target property for the obtained password. |
| spring.cloud.vault.database.role | `` | Role name for credentials. |
| spring.cloud.vault.database.static-role | `false` | Enable static role usage. |
| spring.cloud.vault.database.username-property | `spring.datasource.username` | Target property for the obtained username. |
| spring.cloud.vault.databases | `` |  |
| spring.cloud.vault.discovery.enabled | `false` | Flag to indicate that Vault server discovery is enabled (vault server URL will be looked up via discovery). |
| spring.cloud.vault.discovery.service-id | `vault` | Service id to locate Vault. |
| spring.cloud.vault.elasticsearch.backend | `database` | Database backend path. |
| spring.cloud.vault.elasticsearch.enabled | `false` | Enable elasticsearch backend usage. |
| spring.cloud.vault.elasticsearch.password-property | `spring.elasticsearch.rest.password` | Target property for the obtained password. |
| spring.cloud.vault.elasticsearch.role | `` | Role name for credentials. |
| spring.cloud.vault.elasticsearch.static-role | `false` | Enable static role usage. |
| spring.cloud.vault.elasticsearch.username-property | `spring.elasticsearch.rest.username` | Target property for the obtained username. |
| spring.cloud.vault.enabled | `true` | Enable Vault config server. |
| spring.cloud.vault.fail-fast | `false` | Fail fast if data cannot be obtained from Vault. |
| spring.cloud.vault.gcp-gce.gcp-path | `gcp` | Mount path of the Kubernetes authentication backend. |
| spring.cloud.vault.gcp-gce.role | `` | Name of the role against which the login is being attempted. |
| spring.cloud.vault.gcp-gce.service-account | `` | Optional service account id. Using the default id if left unconfigured. |
| spring.cloud.vault.gcp-iam.credentials.encoded-key | `` | The base64 encoded contents of an OAuth2 account private key in JSON format. |
| spring.cloud.vault.gcp-iam.credentials.location | `` | Location of the OAuth2 credentials private key. <p> Since this is a Resource, the private key can be in a multitude of locations, such as a local file system, classpath, URL, etc. |
| spring.cloud.vault.gcp-iam.gcp-path | `gcp` | Mount path of the Kubernetes authentication backend. |
| spring.cloud.vault.gcp-iam.jwt-validity | `15m` | Validity of the JWT token. |
| spring.cloud.vault.gcp-iam.project-id | `` | Overrides the GCP project Id. |
| spring.cloud.vault.gcp-iam.role | `` | Name of the role against which the login is being attempted. |
| spring.cloud.vault.gcp-iam.service-account-id | `` | Overrides the GCP service account Id. |
| spring.cloud.vault.host | `localhost` | Vault server host. |
| spring.cloud.vault.kubernetes.kubernetes-path | `kubernetes` | Mount path of the Kubernetes authentication backend. |
| spring.cloud.vault.kubernetes.role | `` | Name of the role against which the login is being attempted. |
| spring.cloud.vault.kubernetes.service-account-token-file | `/var/run/secrets/kubernetes.io/serviceaccount/token` | Path to the service account token file. |
| spring.cloud.vault.kv.application-name | `application` | Application name to be used for the context. |
| spring.cloud.vault.kv.backend | `secret` | Name of the default backend. |
| spring.cloud.vault.kv.backend-version | `2` | Key-Value backend version. Currently supported versions are: <ul> <li>Version 1 (unversioned key-value backend).</li> <li>Version 2 (versioned key-value backend).</li> </ul> |
| spring.cloud.vault.kv.default-context | `application` | Name of the default context. |
| spring.cloud.vault.kv.enabled | `true` | Enable the key-value backend. |
| spring.cloud.vault.kv.profile-separator | `/` | Profile-separator to combine application name and profile. |
| spring.cloud.vault.kv.profiles | `` | List of active profiles. @since 3.0 |
| spring.cloud.vault.mongodb.backend | `mongodb` | MongoDB backend path. |
| spring.cloud.vault.mongodb.enabled | `false` | Enable mongodb backend usage. |
| spring.cloud.vault.mongodb.password-property | `spring.data.mongodb.password` | Target property for the obtained password. |
| spring.cloud.vault.mongodb.role | `` | Role name for credentials. |
| spring.cloud.vault.mongodb.static-role | `false` | Enable static role usage. @since 2.2 |
| spring.cloud.vault.mongodb.username-property | `spring.data.mongodb.username` | Target property for the obtained username. |
| spring.cloud.vault.mysql.backend | `mysql` | mysql backend path. |
| spring.cloud.vault.mysql.enabled | `false` | Enable mysql backend usage. |
| spring.cloud.vault.mysql.password-property | `spring.datasource.password` | Target property for the obtained username. |
| spring.cloud.vault.mysql.role | `` | Role name for credentials. |
| spring.cloud.vault.mysql.username-property | `spring.datasource.username` | Target property for the obtained username. |
| spring.cloud.vault.namespace | `` | Vault namespace (requires Vault Enterprise). |
| spring.cloud.vault.pcf.instance-certificate | `` | Path to the instance certificate (PEM). Defaults to {@code CF\_INSTANCE\_CERT} env variable. |
| spring.cloud.vault.pcf.instance-key | `` | Path to the instance key (PEM). Defaults to {@code CF\_INSTANCE\_KEY} env variable. |
| spring.cloud.vault.pcf.pcf-path | `pcf` | Mount path of the Kubernetes authentication backend. |
| spring.cloud.vault.pcf.role | `` | Name of the role against which the login is being attempted. |
| spring.cloud.vault.port | `8200` | Vault server port. |
| spring.cloud.vault.postgresql.backend | `postgresql` | postgresql backend path. |
| spring.cloud.vault.postgresql.enabled | `false` | Enable postgresql backend usage. |
| spring.cloud.vault.postgresql.password-property | `spring.datasource.password` | Target property for the obtained username. |
| spring.cloud.vault.postgresql.role | `` | Role name for credentials. |
| spring.cloud.vault.postgresql.username-property | `spring.datasource.username` | Target property for the obtained username. |
| spring.cloud.vault.rabbitmq.backend | `rabbitmq` | rabbitmq backend path. |
| spring.cloud.vault.rabbitmq.enabled | `false` | Enable rabbitmq backend usage. |
| spring.cloud.vault.rabbitmq.password-property | `spring.rabbitmq.password` | Target property for the obtained password. |
| spring.cloud.vault.rabbitmq.role | `` | Role name for credentials. |
| spring.cloud.vault.rabbitmq.username-property | `spring.rabbitmq.username` | Target property for the obtained username. |
| spring.cloud.vault.reactive.enabled | `true` | Flag to indicate that reactive discovery is enabled |
| spring.cloud.vault.read-timeout | `15000` | Read timeout. |
| spring.cloud.vault.scheme | `https` | Protocol scheme. Can be either "http" or "https". |
| spring.cloud.vault.session.lifecycle.enabled | `true` | Enable session lifecycle management. |
| spring.cloud.vault.session.lifecycle.expiry-threshold | `7s` | The expiry threshold for a {@link LoginToken}. The threshold represents a minimum TTL duration to consider a login token as valid. Tokens with a shorter TTL are considered expired and are not used anymore. Should be greater than {@code refreshBeforeExpiry} to prevent token expiry. |
| spring.cloud.vault.session.lifecycle.refresh-before-expiry | `5s` | The time period that is at least required before renewing the {@link LoginToken}. |
| spring.cloud.vault.ssl.cert-auth-path | `cert` | Mount path of the TLS cert authentication backend. |
| spring.cloud.vault.ssl.enabled-cipher-suites | `` | List of enabled SSL/TLS cipher suites. @since 3.0.2 |
| spring.cloud.vault.ssl.enabled-protocols | `` | List of enabled SSL/TLS protocol. @since 3.0.2 |
| spring.cloud.vault.ssl.key-store | `` | Trust store that holds certificates and private keys. |
| spring.cloud.vault.ssl.key-store-password | `` | Password used to access the key store. |
| spring.cloud.vault.ssl.key-store-type | `` | Type of the key store. @since 3.0 |
| spring.cloud.vault.ssl.trust-store | `` | Trust store that holds SSL certificates. |
| spring.cloud.vault.ssl.trust-store-password | `` | Password used to access the trust store. |
| spring.cloud.vault.ssl.trust-store-type | `` | Type of the trust store. @since 3.0 |
| spring.cloud.vault.token | `` | Static vault token. Required if {@link #authentication} is {@code TOKEN}. |
| spring.cloud.vault.uri | `` | Vault URI. Can be set with scheme, host and port. |
| spring.cloud.zookeeper.base-sleep-time-ms | `50` | Initial amount of time to wait between retries. |
| spring.cloud.zookeeper.block-until-connected-unit | `` | The unit of time related to blocking on connection to Zookeeper. |
| spring.cloud.zookeeper.block-until-connected-wait | `10` | Wait time to block on connection to Zookeeper. |
| spring.cloud.zookeeper.config.default-context | `application` | The name of the default context. |
| spring.cloud.zookeeper.config.enabled | `true` |  |
| spring.cloud.zookeeper.config.fail-fast | `true` | Throw exceptions during config lookup if true, otherwise, log warnings. |
| spring.cloud.zookeeper.config.name | `` | Alternative to spring.application.name to use in looking up values in zookeeper. |
| spring.cloud.zookeeper.config.profile-separator | `,` | Separator for profile appended to the application name. |
| spring.cloud.zookeeper.config.root | `config` | Root folder where the configuration for Zookeeper is kept. |
| spring.cloud.zookeeper.connect-string | `localhost:2181` | Connection string to the Zookeeper cluster. |
| spring.cloud.zookeeper.connection-timeout | `` | The configured connection timeout in milliseconds. |
| spring.cloud.zookeeper.dependencies | `` | Mapping of alias to ZookeeperDependency. From LoadBalancer perspective the alias is actually serviceID since SC LoadBalancer can't accept nested structures in serviceID. |
| spring.cloud.zookeeper.dependency-configurations | `` |  |
| spring.cloud.zookeeper.dependency-names | `` |  |
| spring.cloud.zookeeper.discovery.enabled | `true` |  |
| spring.cloud.zookeeper.discovery.initial-status | `` | The initial status of this instance (defaults to {@link StatusConstants#STATUS\_UP}). |
| spring.cloud.zookeeper.discovery.instance-host | `` | Predefined host with which a service can register itself in Zookeeper. Corresponds to the {code address} from the URI spec. |
| spring.cloud.zookeeper.discovery.instance-id | `` | Id used to register with zookeeper. Defaults to a random UUID. |
| spring.cloud.zookeeper.discovery.instance-port | `` | Port to register the service under (defaults to listening port). |
| spring.cloud.zookeeper.discovery.instance-ssl-port | `` | Ssl port of the registered service. |
| spring.cloud.zookeeper.discovery.metadata | `` | Gets the metadata name/value pairs associated with this instance. This information is sent to zookeeper and can be used by other instances. |
| spring.cloud.zookeeper.discovery.order | `0` | Order of the discovery client used by `CompositeDiscoveryClient` for sorting available clients. |
| spring.cloud.zookeeper.discovery.register | `true` | Register as a service in zookeeper. |
| spring.cloud.zookeeper.discovery.root | `/services` | Root Zookeeper folder in which all instances are registered. |
| spring.cloud.zookeeper.discovery.uri-spec | `{scheme}://{address}:{port}` | The URI specification to resolve during service registration in Zookeeper. |
| spring.cloud.zookeeper.enabled | `true` | Is Zookeeper enabled. |
| spring.cloud.zookeeper.max-retries | `10` | Max number of times to retry. |
| spring.cloud.zookeeper.max-sleep-ms | `500` | Max time in ms to sleep on each retry. |
| spring.cloud.zookeeper.prefix | `` | Common prefix that will be applied to all Zookeeper dependencies' paths. |
| spring.cloud.zookeeper.session-timeout | `` | The configured/negotiated session timeout in milliseconds. Please refer to <a href='<https://cwiki.apache.org/confluence/display/CURATOR/TN14'>Curator's> Tech Note 14</a> to understand how Curator implements connection sessions. @see <a href='<https://cwiki.apache.org/confluence/display/CURATOR/TN14'>Curator's> Tech Note 14</a> |
| stubrunner.amqp.enabled | `false` | Whether to enable support for Stub Runner and AMQP. |
| stubrunner.amqp.mockCOnnection | `true` | Whether to enable support for Stub Runner and AMQP mocked connection factory. |
| stubrunner.classifier | `stubs` | The classifier to use by default in ivy co-ordinates for a stub. |
| stubrunner.cloud.consul.enabled | `true` | Whether to enable stubs registration in Consul. |
| stubrunner.cloud.delegate.enabled | `true` | Whether to enable DiscoveryClient's Stub Runner implementation. |
| stubrunner.cloud.enabled | `true` | Whether to enable Spring Cloud support for Stub Runner. |
| stubrunner.cloud.eureka.enabled | `true` | Whether to enable stubs registration in Eureka. |
| stubrunner.cloud.loadbalancer.enabled | `true` | Whether to enable Stub Runner's Spring Cloud Load Balancer integration. |
| stubrunner.cloud.stubbed.discovery.enabled | `true` | Whether Service Discovery should be stubbed for Stub Runner. If set to false, stubs will get registered in real service discovery. |
| stubrunner.cloud.zookeeper.enabled | `true` | Whether to enable stubs registration in Zookeeper. |
| stubrunner.consumer-name | `` | You can override the default {@code spring.application.name} of this field by setting a value to this parameter. |
| stubrunner.delete-stubs-after-test | `true` | If set to {@code false} will NOT delete stubs from a temporary folder after running tests. |
| stubrunner.fail-on-no-stubs | `true` | When enabled, this flag will tell stub runner to throw an exception when no stubs / contracts were found. |
| stubrunner.generate-stubs | `false` | When enabled, this flag will tell stub runner to not load the generated stubs, but convert the found contracts at runtime to a stub format and run those stubs. |
| stubrunner.http-server-stub-configurer | `` | Configuration for an HTTP server stub. |
| stubrunner.ids | `[]` | The ids of the stubs to run in "ivy" notation ([groupId]:artifactId:[version]:[classifier][:port]). {@code groupId}, {@code classifier}, {@code version} and {@code port} can be optional. |
| stubrunner.ids-to-service-ids | `` | Mapping of Ivy notation based ids to serviceIds inside your application. Example "a:b" -> "myService" "artifactId" -> "myOtherService" |
| stubrunner.integration.enabled | `true` | Whether to enable Stub Runner integration with Spring Integration. |
| stubrunner.jms.enabled | `true` | Whether to enable Stub Runner integration with Spring JMS. |
| stubrunner.kafka.enabled | `true` | Whether to enable Stub Runner integration with Spring Kafka. |
| stubrunner.kafka.initializer.enabled | `true` | Whether to allow Stub Runner to take care of polling for messages instead of the KafkaStubMessages component. The latter should be used only on the producer side. |
| stubrunner.mappings-output-folder | `` | Dumps the mappings of each HTTP server to the selected folder. |
| stubrunner.max-port | `15000` | Max value of a port for the automatically started WireMock server. |
| stubrunner.min-port | `10000` | Min value of a port for the automatically started WireMock server. |
| stubrunner.password | `` | Repository password. |
| stubrunner.properties | `` | Map of properties that can be passed to custom {@link org.springframework.cloud.contract.stubrunner.StubDownloaderBuilder}. |
| stubrunner.proxy-host | `` | Repository proxy host. |
| stubrunner.proxy-port | `` | Repository proxy port. |
| stubrunner.server-id | `` |  |
| stubrunner.stream.enabled | `true` | Whether to enable Stub Runner integration with Spring Cloud Stream. |
| stubrunner.stubs-mode | `` | Pick where the stubs should come from. |
| stubrunner.stubs-per-consumer | `false` | Should only stubs for this particular consumer get registered in HTTP server stub. |
| stubrunner.username | `` | Repository username. |
| wiremock.placeholders.enabled | `true` | Flag to indicate that http URLs in generated wiremock stubs should be filtered to add or resolve a placeholder for a dynamic port. |
| wiremock.reset-mappings-after-each-test | `false` |  |
| wiremock.rest-template-ssl-enabled | `false` |  |
| wiremock.server.files | `[]` |  |
| wiremock.server.https-port | `-1` |  |
| wiremock.server.https-port-dynamic | `false` |  |
| wiremock.server.port | `8080` |  |
| wiremock.server.port-dynamic | `false` |  |
| wiremock.server.stubs | `[]` |  |

---

<a id="index"></a>

<!-- source_url: https://docs.spring.io/spring-cloud/docs/current/reference/html/ -->

<!-- page_index: 3 -->

# Appendix: Compendium of Configuration Properties

Spring Cloud provides tools for developers to quickly build some of
the common patterns in distributed systems (e.g. configuration
management, service discovery, circuit breakers, intelligent routing, micro-proxy, control bus). Coordination of
distributed systems leads to boiler plate patterns, and using Spring
Cloud developers can quickly stand up services and applications that
implement those patterns. They will work well in any distributed
environment, including the developer’s own laptop, bare metal data
centres, and managed platforms such as Cloud Foundry.

Release Train Version: **2022.0.5**

Supported Boot Version: **3.0.13**

<a id="index--features"></a>
<a id="index--1.-features"></a>

## [1. Features](#index--features)

Spring Cloud focuses on providing good out of box experience for typical use cases
and extensibility mechanism to cover others.

- Distributed/versioned configuration
- Service registration and discovery
- Routing
- Service-to-service calls
- Load balancing
- Circuit Breakers
- Distributed messaging

The reference documentation consists of the following sections:

| [Legal](#legal--legal-information) | Legal information. |
| --- | --- |
| [Documentation Overview](#documentation-overview--documentation) | About the Documentation, Getting Help, First Steps, and more. |
| [spring-cloud-build](https://docs.spring.io/spring-cloud-build/docs/4.0.6/reference/html/) | spring-cloud-build Reference Documentation, version 4.0.6 |
| [spring-cloud-bus](https://docs.spring.io/spring-cloud-bus/docs/4.0.3/reference/html/) | spring-cloud-bus Reference Documentation, version 4.0.3 |
| [spring-cloud-circuitbreaker](https://docs.spring.io/spring-cloud-circuitbreaker/docs/3.0.4/reference/html/) | spring-cloud-circuitbreaker Reference Documentation, version 3.0.4 |
| [spring-cloud-commons](https://docs.spring.io/spring-cloud-commons/docs/4.0.5/reference/html/) | spring-cloud-commons Reference Documentation, version 4.0.5 |
| [spring-cloud-config](https://docs.spring.io/spring-cloud-config/docs/4.0.5/reference/html/) | spring-cloud-config Reference Documentation, version 4.0.5 |
| [spring-cloud-consul](https://docs.spring.io/spring-cloud-consul/docs/4.0.4/reference/html/) | spring-cloud-consul Reference Documentation, version 4.0.4 |
| [spring-cloud-contract](https://docs.spring.io/spring-cloud-contract/docs/4.0.5/reference/html/) | spring-cloud-contract Reference Documentation, version 4.0.5 |
| [spring-cloud-function](https://docs.spring.io/spring-cloud-function/docs/4.0.6/reference/html/) | spring-cloud-function Reference Documentation, version 4.0.6 |
| [spring-cloud-gateway](https://docs.spring.io/spring-cloud-gateway/docs/4.0.9/reference/html/) | spring-cloud-gateway Reference Documentation, version 4.0.9 |
| [spring-cloud-kubernetes](https://docs.spring.io/spring-cloud-kubernetes/docs/3.0.5/reference/html/) | spring-cloud-kubernetes Reference Documentation, version 3.0.5 |
| [spring-cloud-netflix](https://docs.spring.io/spring-cloud-netflix/docs/4.0.4/reference/html/) | spring-cloud-netflix Reference Documentation, version 4.0.4 |
| [spring-cloud-openfeign](https://docs.spring.io/spring-cloud-openfeign/docs/4.0.6/reference/html/) | spring-cloud-openfeign Reference Documentation, version 4.0.6 |
| [spring-cloud-stream](https://docs.spring.io/spring-cloud-stream/docs/4.0.5/reference/html/) | spring-cloud-stream Reference Documentation, version 4.0.5 |
| [spring-cloud-task](https://docs.spring.io/spring-cloud-task/docs/3.0.4/reference/html/) | spring-cloud-task Reference Documentation, version 3.0.4 |
| [spring-cloud-vault](https://docs.spring.io/spring-cloud-vault/docs/4.0.2/reference/html/) | spring-cloud-vault Reference Documentation, version 4.0.2 |
| [spring-cloud-zookeeper](https://docs.spring.io/spring-cloud-zookeeper/docs/4.0.2/reference/html/) | spring-cloud-zookeeper Reference Documentation, version 4.0.2 |

<a id="index--appendix-compendium-of-configuration-properties"></a>
<a id="index--appendix:-compendium-of-configuration-properties"></a>

# [Appendix: Compendium of Configuration Properties](#index--appendix-compendium-of-configuration-properties)

[Spring Cloud configuration properties](#configprops)

---

<a id="legal"></a>

<!-- source_url: https://docs.spring.io/spring-cloud/docs/current/reference/html/legal.html -->

<!-- page_index: 4 -->

# Legal

2022.0.5

Copyright © 2012-2020

Copies of this document may be made for your own use and for distribution to
others, provided that you do not charge any fee for such copies and further
provided that each copy contains this Copyright Notice, whether distributed in
print or electronically.

---
