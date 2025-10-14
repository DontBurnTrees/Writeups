## All ports scan
```
# Nmap 7.93 scan initiated Sun Oct 12 18:29:46 2025 as: nmap -T4 -p- -oN allports 10.10.155.211
Nmap scan report for 10.10.155.211
Host is up (0.030s latency).
Not shown: 65533 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http

# Nmap done at Sun Oct 12 18:30:11 2025 -- 1 IP address (1 host up) scanned in 25.54 seconds
```

## Detailed scan

```
# Nmap 7.93 scan initiated Sun Oct 12 18:37:23 2025 as: nmap -T4 -p80,22 -oN detailed -A 10.10.155.211
Nmap scan report for 10.10.155.211
Host is up (0.035s latency).

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 9d000c5fe9385d84960248d80a0eb579 (RSA)
|   256 54c5792c738f2cae7323b1f2dbe3c073 (ECDSA)
|_  256 a66efbd6816245b47d870e5b69fd18f6 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: Publisher's Pulse: SPIP Insights & Tips
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (94%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Adtran 424RG FTTH gateway (92%), Linux 2.6.32 (92%), Linux 2.6.39 - 3.2 (92%), Linux 3.1 - 3.2 (92%), Linux 3.2 - 4.9 (92%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 2 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT      ADDRESS
1   59.44 ms 10.14.0.1
2   60.51 ms 10.10.155.211

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Oct 12 18:37:35 2025 -- 1 IP address (1 host up) scanned in 11.84 seconds
```

## Enumeration

- Finding spip 4.2.0 running on the web app (using wappalyzer). This version is vulnerable to the CVE-2023-27372 (RCE pre-auth)

## Exploitation

- You can either use the metasploit module (exploit/multi/http/spip_rce_form) ;
    get the exploit from [github](https://github.com/nuts7/CVE-2023-27372) and run it manually
    or even use searchsploit to get the script (php/webapps/51536.py)

- You might need to edit a few lines from the script.

## Foothold

- Now that we are www-data
