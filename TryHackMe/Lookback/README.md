## Room: Lookback 

##### Description:   You’ve been asked to run a vulnerability test on a production environment.  

#### Difficulty: Easy 

## Recon & Enumeration

All ports tcp scan:
```
PORT     STATE SERVICE
80/tcp   open  http
443/tcp  open  https
3389/tcp open  ms-wbt-server
```
- From here I decide to enumerate the web service, I'm having issues connecting with the browser so I'm using cURL to investigate the issue

```
# curl http://10.10.10.10 -I
HTTP/1.1 403 Forbidden
Content-Length: 0
Server: Microsoft-IIS/10.0
Date: Wed, 10 Dec 2025 20:14:28 GMT

# curl https://10.10.10.10 -I
curl: (60) SSL certificate problem: self-signed certificate
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the webpage mentioned above.

# curl https://10.10.10.10 -I -k
HTTP/2 302 
cache-control: no-cache
pragma: no-cache
content-length: 0
location: https://10.10.10.10/owa/
server: Microsoft-IIS/10.0
x-feserver: WIN-12OUO7A66M7
x-requestid: b51568b2-706c-4156-8add-7a26de75041f
date: Wed, 10 Dec 2025 20:14:37 GMT
```

- Very interesting finding, the web page is redirecting me to `https://10.10.10.10/owa/`. Using my browser to view the page there is login form to a mail server (outlook). When I'm trying default credentials I'm having the following error.  

```
X-ClientId: A62683615A8243F1B733141A2BB9F32A
request-id 28e347f6-0fd4-4967-aa76-bce431a8e387
X-OWA-Error Microsoft.Exchange.Data.Storage.UserHasNoMailboxException
X-OWA-Version 15.2.858.2
X-FEServer WIN-12OUO7A66M7
X-BEServer WIN-12OUO7A66M7
Date:10/12/2025 20:34:06
```

- Having a version I could try to search for potentials CVEs. I don't find anything that relevant so I decide to enumerate further the open ports

All tcp open ports detailed scan:
```
PORT     STATE SERVICE       VERSION
80/tcp   open  http          Microsoft IIS httpd 10.0
|_http-server-header: Microsoft-IIS/10.0
|_http-title: Site doesn't have a title.
443/tcp  open  ssl/https
| ssl-cert: Subject: commonName=WIN-12OUO7A66M7
| Subject Alternative Name: DNS:WIN-12OUO7A66M7, DNS:WIN-12OUO7A66M7.thm.local
| Not valid before: 2023-01-25T21:34:02
|_Not valid after:  2028-01-25T21:34:02
|_http-server-header: Microsoft-IIS/10.0
| http-title: Outlook
|_Requested resource was https://10.81.152.169/owa/auth/logon.aspx?url=https%3a%2f%2f10.81.152.169%2fowa%2f&reason=0
3389/tcp open  ms-wbt-server Microsoft Terminal Services
| rdp-ntlm-info: 
|   Target_Name: THM
|   NetBIOS_Domain_Name: THM
|   NetBIOS_Computer_Name: WIN-12OUO7A66M7
|   DNS_Domain_Name: thm.local
|   DNS_Computer_Name: WIN-12OUO7A66M7.thm.local
|   DNS_Tree_Name: thm.local
|   Product_Version: 10.0.17763
|_  System_Time: 2025-12-10T20:39:51+00:00
| ssl-cert: Subject: commonName=WIN-12OUO7A66M7.thm.local
| Not valid before: 2025-12-09T20:07:22
|_Not valid after:  2026-06-10T20:07:22
```

- I feel like there is maybe something to do with the domain (thm.local) but I don't know what to do. 

*What is the service user flag?*    
**Q1** - `answer`


## Exploitation

- ... 

*What is the user flag?*    
**Q2** - `answer`

## Privilege escalation

- ... 

*What is the root flag?*    
**Q3** - `answer`

### Date: 10/12/2025
