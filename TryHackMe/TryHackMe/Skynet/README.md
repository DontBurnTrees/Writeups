# Recon

All ports tcp scan:
```
PORT    STATE SERVICE
22/tcp  open  ssh
80/tcp  open  http
110/tcp open  pop3
139/tcp open  netbios-ssn
143/tcp open  imap
445/tcp open  microsoft-ds
```

All open ports tcp detailed scan:
```
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 992331bbb1e943b756944cb9e82146c5 (RSA)
|   256 57c07502712d193183dbe4fe679668cf (ECDSA)
|_  256 46fa4efc10a54f5757d06d54f6c34dfe (ED25519)
80/tcp  open  http        Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Skynet
110/tcp open  pop3        Dovecot pop3d
|_pop3-capabilities: UIDL CAPA TOP AUTH-RESP-CODE PIPELINING RESP-CODES SASL
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
143/tcp open  imap        Dovecot imapd
|_imap-capabilities: listed more OK ID LOGIN-REFERRALS capabilities LITERAL+ have post-login Pre-login LOGINDISABLEDA0001 IDLE IMAP4rev1 ENABLE SASL-IR
445/tcp open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
```


- Since we are looking for Miles emails password I start to enumerate IMAP and POP3. I don't know much about those services, I decide to look at the hint which is: Enumerate Samba. From there I know that I have to enumerate the SMB service (port 139).

```
# smbclient -N -L //10.10.10.10     

	Sharename       Type      Comment
	---------       ----      -------
	print$          Disk      Printer Drivers
	anonymous       Disk      Skynet Anonymous Share
	milesdyson      Disk      Miles Dyson Personal Share
	IPC$            IPC       IPC Service (skynet server (Samba, Ubuntu))

# smbclient //10.10.134.46/anonymous 
Password for [WORKGROUP\root]:
Try "help" to get a list of possible commands.
smb: \> ls
  .                                   D        0  Thu Nov 26 17:04:00 2020
  ..                                  D        0  Tue Sep 17 09:20:17 2019
  attention.txt                       N      163  Wed Sep 18 05:04:59 2019
  logs                                D        0  Wed Sep 18 06:42:16 2019

		9204224 blocks of size 1024. 5831512 blocks available
smb: \> get attention.txt
smb: \> cd logs
smb: \logs\> ls
  .                                   D        0  Wed Sep 18 06:42:16 2019
  ..                                  D        0  Thu Nov 26 17:04:00 2020
  log2.txt                            N        0  Wed Sep 18 06:42:13 2019
  log1.txt                            N      471  Wed Sep 18 06:41:59 2019
  log3.txt                            N        0  Wed Sep 18 06:42:16 2019

		9204224 blocks of size 1024. 5831508 blocks available
smb: \logs\> get log1.txt
```

- Having a wordlist of passwords I can try to bruteforce emails services (IMAP and POP3) with the user Miles.

