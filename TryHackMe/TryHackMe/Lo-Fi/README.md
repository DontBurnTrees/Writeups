# Recon

All tcp ports scan:
```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```

Open ports detailed scan:
```
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2b59b663ce3502a6c5a06d8d6550b20c (RSA)
|   256 9bf43ca533cab2c4c1bdc6b9b4963091 (ECDSA)
|_  256 ed51504b946510262c854e0d936c4674 (ED25519)
80/tcp open  http    Apache httpd 2.2.22 ((Ubuntu))
|_http-server-header: Apache/2.2.22 (Ubuntu)
|_http-title: Lo-Fi Music
```

- From there I know from the description of the box that the vulnerability is probably going to be an LFI, having never practiced this vulnerability before I decide to take a step back from the challenge and learn about this specific vuln in this room => [File Inclusion, Path Traversal](https://tryhackme.com/room/filepathtraversal)


