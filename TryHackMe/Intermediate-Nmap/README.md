- From the description of the box I know roughly what to look for: connect to a high port => get creds => connect to SSH => get the flag

```allports
PORT      STATE SERVICE
22/tcp    open  ssh
2222/tcp  open  EtherNetIP-1
31337/tcp open  Elite
```

```detailed
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 7ddceb90e4af33d99f0b219afcd577f2 (RSA)
|   256 83a74a61ef93a3571a57385c482aeb16 (ECDSA)
|_  256 30bfef9408860700f7fcdfe8edfe07af (ED25519)
2222/tcp  open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 e9e17ac97768380ea0c2dd648b2aa550 (RSA)
|   256 7644b4ed81f508694b3635f19211872d (ECDSA)
|_  256 331cdabe21dc3c501ba7df3b8eda73ed (ED25519)
31337/tcp open  Elite?
| fingerprint-strings: 
|   DNSStatusRequestTCP, DNSVersionBindReqTCP, FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LANDesk-RC, LDAPBindReq, LDAPSearchReq, LPDString, NULL, RPCCheck, RTSPRequest, SIPOptions, SMBProgNeg, SSLSessionReq, TLSSessionReq, TerminalServer, TerminalServerCookie, X11Probe: 
|     In case I forget - user:pass
|_    ubuntu:Dafdas!!/str0ng
```

- From there we can already see some juicy informations: `user:pass  ubuntu:Dafdas!!/str0ng`

- At first I tried using user:pass on port 22 and 2222 but It wasn't valid. After a big brain moment I used ubuntu:Dafdas!!/str0ng on port 22 and I was in.

- The flag is located in /home/user

24/10/2025
