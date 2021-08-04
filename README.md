# Developer Interview Task Handout

##Objective
The task consists of two parts:<br>
1) Read the request log files (json) using a programing language of your choice and create a data set that allows you to analyze it.
2) Analyze the usage of the reports and present some of the insights you have found. You can use a programing language of your
choice.

### Data structure
The data comes in a hierarchical structure:
```bash
/2016 <-- year
??? 01 <-- month
? ??? 06 <-- day
? ? ??? zed-log
? ? ??? 15-requests.json <--hour
? ? ??? 16-requests.json
? ? ??? 17-requests.json
? ? ??? 18-requests.json
? ? ??? 21-requests.json
```
### Example requests
Request for Index page
```json 
{
"type":"request",
"user_name":"jane.doe",
"request_id":"1291408975900603453",
"environment":"production",
"store":"DE",
"time":"2016-04-06T07:35:10",
"client_ip":"127.0.0.1",
"host":"dwh.bi.foo.de",
"method":"GET",
"params":{
"controller":"index",
"action":"index",
"module":"dwh",
"oauth_proxy_redirect_host":"dwh.bi.foo.de"
},
"path":"/",
"referrer":false,
"user_agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.
2623.110 Safari/537.36"
}
```
Reports have the following url structure: https://bi.foo.de/dwh/reports/view/id/marketing-cost-monitoring
Request for Report:
```json
{
"type":"request",
"user_name":"joe.shmoe",
"request_id":"10811514580128672004",
"environment":"production",
"store":"DE",
"time":"2016-04-06T07:00:49",
"client_ip":"127.0.0.1",
"host":"dwh.bi.foo.de",
"method":"GET",
"params":{
"module":"dwh",
"controller":"reports",
"action":"view",
"id":"marketing-cost-monitoring",
"oauth_proxy_redirect_host":"dwh.bi.foo.de"
},
"path":"/dwh/reports/view/id/marketing-cost-monitoring",
"referrer":"https://dwh.bi.foo.de/?",
"user_agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:45.0) Gecko/20100101 Firefox/45.0"
}
```

## Docker
Create a docker_compose file using
```bash
postgresql version 13
user = root
password = root
database=dwh_development
```
```bash
# Use ethernet IP address in pgadmin
pgadmin username = admin@admin.com
pg_admin pass = root
ports:"5050:80"
```
Run postgresql 
```bash
make postgres_compose
```