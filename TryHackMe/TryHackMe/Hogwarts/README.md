# Hogwarts 

## Active recon
- Doing a complete scan on the target 
```
nmap -A -p- -T4 -sS -oN fullscan.txt 10.10.32.244 
22/tcp   open  ssh
8571/tcp open  ftp     vsftpd 3.0.3
8794/tcp open  http    PHP cli server 5.5 or later
8994/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
9999/tcp open  abyss
```
- Connecting to the ftp port in anonymous.
```
[Jul 04, 2025 - 22:07:47 (CEST)] exegol-thmvpn /workspace # ftp 10.10.32.244 8571
Connected to 10.10.32.244.
220 (vsFTPd 3.0.3)
Name (10.10.32.244:root): anonymous 
331 Please specify the password.
Password: 
230 Login successful.
```
- Now that we have a foothold on the machine let's inspect accessible files.
```
ftp> ls -al
229 Entering Extended Passive Mode (|||23534|)
150 Here comes the directory listing.
drwxr-xr-x    3 ftp      ftp          4096 Sep 06  2020 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 06  2020 ..
drwxr-xr-x    3 ftp      ftp          4096 Sep 06  2020 ...
-rw-r--r--    1 ftp      ftp            95 Sep 06  2020 .IamHidden
```
- It's time to put in use our linux skills, there are a few small rabbit holes (that I've falled into :°). Below is the path to the file we want to retrieve.
```
ftp> cd ...
250 Directory successfully changed.
ftp> cd ...
250 Directory successfully changed.
ftp> ls -al
229 Entering Extended Passive Mode (|||20498|)
150 Here comes the directory listing.
drwxr-xr-x    2 ftp      ftp          4096 Jul 04 19:55 .
drwxr-xr-x    3 ftp      ftp          4096 Sep 06  2020 ..
-rw-r--r--    1 ftp      ftp           231 Jul 04 19:55 .I_saved_it_harry.zip
-rw-r--r--    1 ftp      ftp           157 Sep 06  2020 note4neville
ftp> get .I_saved_it_harry.zip
local: .I_saved_it_harry.zip remote: .I_saved_it_harry.zip
229 Entering Extended Passive Mode (|||33965|)
150 Opening BINARY mode data connection for .I_saved_it_harry.zip (231 bytes).
100% |*************************************************************************************************************************************************|   231        4.78 MiB/s    00:00 ETA
226 Transfer complete.
231 bytes received in 00:00 (8.67 KiB/s)
``` 
- Time to unzip this zip archive, however we are now facing a new issue: we need to have a password to access the zip. During my first time on this box I've tried to guess the password from the weird messages that I've found on the machine but I was wrong. Just need to bruteforce the zip to open it, starting on a bruteforce attack in this scenario should be a reflex, it's not eating bread we would say in french.
```
[Jul 04, 2025 - 22:14:33 (CEST)] exegol-thmvpn /workspace # fcrackzip -u -v -D -p `fzf-wordlists` .I_saved_it_harry.zip 
found file 'boot/.pass', (size cp/uc     45/    33, flags 9, chk 9ef9)
[Jul 04, 2025 - 22:16:33 (CEST)] exegol-thmvpn /workspace # unzip .I_saved_it_harry.zip                                
Archive:  .I_saved_it_harry.zip
[.I_saved_it_harry.zip] boot/.pass password: 
 extracting: boot/.pass              
[Jul 04, 2025 - 22:16:43 (CEST)] exegol-thmvpn /workspace # ls
boot  GoAway.exe  note4neville  scan.txt
[Jul 04, 2025 - 22:16:46 (CEST)] exegol-thmvpn /workspace # cd boot         
[Jul 04, 2025 - 22:16:50 (CEST)] exegol-thmvpn boot # ls
[Jul 04, 2025 - 22:16:50 (CEST)] exegol-thmvpn boot # ls -al 
total 12
drwxrws--- 2 root rvm 4096 Jul  4 22:16 .
drwxrwsr-x 3 1000 rvm 4096 Jul  4 22:16 ..
-rw-r--r-- 1 root rvm   33 Jul  4 21:55 .pass
[Jul 04, 2025 - 22:16:55 (CEST)] exegol-thmvpn boot # cat .pass       
neville:xut8ulc5ell6coqw2d9v47n80#                               
```
- W, we have a login and a password, in this scenario we can use the obtained creds to auth somewhere, and looking at the box right now we have one obvious place to authenticate: glorious SSH. However me might need to try the 2 endpoints to figure out which one is the correct one.
```
[Jul 04, 2025 - 22:22:56 (CEST)] exegol-thmvpn /workspace # ssh neville@10.10.32.244 -p 8994
neville@10.10.32.244's password: 
Permission denied, please try again.
neville@10.10.32.244's password: 
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-1112-aws x86_64)
```
- For some reason I keep having some hard times connecting to ssh, now that we have a "better" foothold on the machine let's have a look around.

