# Mr Robot CTF

All ports tcp scan:
```
PORT    STATE  SERVICE
22/tcp  closed ssh
80/tcp  closed http
443/tcp closed https
```

Detailed open ports scan:
```
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 1a6a0c2c1d0b8efb6c00720cb0c53c00 (RSA)
|   256 25ed3cbf67ea7a196f159ff04717a8f1 (ECDSA)
|_  256 bba4e37d7a2dd7c617f317d35eac4819 (ED25519)
80/tcp  open  http     Apache httpd
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache
443/tcp open  ssl/http Apache httpd
|_http-title: Site doesn't have a title (text/html).
| ssl-cert: Subject: commonName=www.example.com
| Not valid before: 2015-09-16T10:45:03
|_Not valid after:  2025-09-13T10:45:03
|_http-server-header: Apache
```

- From the results of the scans I decide to enumerate the web app, I quickly find the first flag thanks to the robots.txt located at /key-1-of-3.txt I also get a wordlist from the robots.txt that I download on my attacking host `wget http://10.10.123.151/fsocity.dic`

- 

*25/10/2025*
