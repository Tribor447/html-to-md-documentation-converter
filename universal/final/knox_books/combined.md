# Untitled

## Navigation

- Docs
  - Knox 2 1 0
    - [Untitled](#knox-2-1-0-user-guide)

## Content

<a id="knox-2-1-0-user-guide"></a>

<!-- source_url: https://knox.apache.org/books/knox-2-1-0/user-guide.html -->

<!-- page_index: 1 -->

# Untitled

```

<?xml version="1.0" encoding="UTF-8"?>
<topology>
   <uri>https://localhost:8443/gateway/mytopology</uri>
   <name>mytopology</name>
   <timestamp>1509720338000</timestamp>
   <gateway>
      <provider>
         <role>authentication</role>
         <name>ShiroProvider</name>
         <enabled>true</enabled>
         <param>
            <name>sessionTimeout</name>
            <value>30</value>
         </param>
         <param>
            <name>main.ldapRealm</name>
            <value>org.apache.knox.gateway.shirorealm.KnoxLdapRealm</value>
         </param>
         <param>
            <name>main.ldapContextFactory</name>
            <value>org.apache.knox.gateway.shirorealm.KnoxLdapContextFactory</value>
         </param>
         <param>
            <name>main.ldapRealm.contextFactory</name>
            <value>$ldapContextFactory</value>
         </param>
         <param>
            <name>main.ldapRealm.userDnTemplate</name>
            <value>uid={0},ou=people,dc=hadoop,dc=apache,dc=org</value>
         </param>
         <param>
            <name>main.ldapRealm.contextFactory.url</name>
            <value>ldap://localhost:33389</value>
         </param>
         <param>
            <name>main.ldapRealm.contextFactory.authenticationMechanism</name>
            <value>simple</value>
         </param>
         <param>
            <name>urls./**</name>
            <value>authcBasic</value>
         </param>
      </provider>
      <provider>
         <role>identity-assertion</role>
         <name>Default</name>
         <enabled>true</enabled>
      </provider>
      <provider>
         <role>hostmap</role>
         <name>static</name>
         <enabled>true</enabled>
         <param>
            <name>localhost</name>
            <value>sandbox,sandbox.hortonworks.com</value>
         </param>
      </provider>
   </gateway>
   <service>
      <role>NAMENODE</role>
      <url>hdfs://localhost:8020</url>
   </service>
   <service>
      <role>JOBTRACKER</role>
      <url>rpc://localhost:8050</url>
   </service>
   <service>
      <role>WEBHDFS</role>
      <url>http://localhost:50070/webhdfs</url>
   </service>
   <service>
      <role>WEBHCAT</role>
      <url>http://localhost:50111/templeton</url>
   </service>
   <service>
      <role>OOZIE</role>
      <url>http://localhost:11000/oozie</url>
   </service>
   <service>
      <role>WEBHBASE</role>
      <url>http://localhost:60080</url>
   </service>
   <service>
      <role>HIVE</role>
      <url>http://localhost:10001/cliservice</url>
   </service>
   <service>
      <role>RESOURCEMANAGER</role>
      <url>http://localhost:8088/ws</url>
   </service>
</topology>
```

---
