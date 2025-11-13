# H1: Hard

## Services 

``` 
PORT     STATE SERVICE REASON         VERSION
22/tcp   open  ssh     syn-ack ttl 63 OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 439cf2ff18c9c50477a42b758e297df5 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDqR5PN2dPP/SN4g3lYlphuboB5tQU25W/BmgRkgIbncumsF55NdIFrIPzCSl2gMlr/FtkpEfQyjlvfMlrdA8HH7j3/S/aAInBu5JgUW9SHtiyHvrjH4VdFRh+WDxAfj0tSAc+dyqWzLazfL5wxBLNAB94DR67xbPQRJSN2lomqPlq8/CbxhlujSW+qxhzuIJalVxGqewzCOW1+u8XK/1Y0V//2MHBijHTSNcb/scBqqVgRQC6+K92GKt0xCS+jhm9e3a7pBl+QEumf1xsH4ssLJO+9JpWpuolv8V8VffQULPWsVw+4eBe51Ou8y481woMxoFDUArNEWwJraXBty6Fue5iqvKeoiIz2h1h0DUFA9k4IwAm91nsUFIvKnoRquAp2hzrZIrTq96zlSB9MhgaVDyNTCfg9GzdogUuSRD9N6osIz+D0UEbLgsTnezrB+q2Hyc+C33CCSjVHSezl+o/WJ1PfGc1To6KcmZ5Xq2mFfaEH1dB1B65FjrsN9fLjrqU=
|   256 abe2b3a715ce2d7929857a64c1c4a5b7 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBK6UN2BS9ZRWwQHo+o2Lv2JlsXrgSQu00pQBZgzXpp8kQp4C6kDOjKuNPbdK3gBYyMDcbCmd2Mbf3Xf9vkf24+k=
|   256 722ed465ed9458517dd936d107c05c84 (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII65C18/aWy/dFe3fNTygY0orBHt0i92PSMbR/pkpCzy
80/tcp   open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-title: Server Manager Login
|_Requested resource was /login
| http-methods: 
|_  Supported Methods: GET POST
81/tcp   open  http    syn-ack ttl 62 nginx 1.18.0 (Ubuntu)
|_http-title: Home Page
| http-methods: 
|_  Supported Methods: GET HEAD POST
|_http-server-header: nginx/1.18.0 (Ubuntu)
82/tcp   open  http    syn-ack ttl 62 Apache httpd 2.4.41 ((Ubuntu))
|_http-title: I Love Hills - Home
| http-methods: 
|_  Supported Methods: GET
|_http-server-header: Apache/2.4.41 (Ubuntu)
2222/tcp open  ssh     syn-ack ttl 62 OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 4f939a3f4bcc7791e3c4e26793fb9879 (RSA)
| ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCrgbNFDTXnsfo/EgAXFHE/uVsYYvVJCW5aTdFejzMW0WtyQ2InTK72IhX0GWXn8Va84HcX4OaR7lLr7Nw9AC1ajZE9H0I3MjZDpp+U27CnPRgxfMePs5bDHEO5UBjIdGtdsHiiRbxyGPEg4N0UClad9VQBPVwARBdTT4EebLx5f9u+dgr5YQNi43tZYyo7PwFmvgl8u0e1Ad89iCwgvi6ymC1Y2rO3PTiHfAbH9egCM3AiaHt/8QbBnS6/pstFdQKzoJce3FiUjMhTyzvIf1+8GHe8kUW2TMZIuPmYDe2sYKnfcpITfMn4H6kszmNd3Hmq4hZcjQNDzni31mH3REVS1L/TvLy7VXQlXJ5rQcOhjORcpkdhWtg1UTdxl4JFiekL1ZdQiYI2GC2nlpMTPreDVy77ULP4f42mKTC5Bl4XrhNY7TlUSJtj06W9HTf/I5MmO32/TdqAmBE04vyPY12JvxV8cRMle+DVIdVslcKBxKDPGEdMlBu6W8UqMqCXRB8=
|   256 00f95e658674d82de18d62f67dbea707 (ECDSA)
| ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBIfkw7myZvD2XmXo5Xjk8WKdtk7WhDd6ytdJfmobop3E3NoxAM5HcB5z0m8+Gc6jCR/k1FsT7r9V1DUuSsP8SAw=
|   256 01a0a53c2e5e02fef5d28add4c441a2b (ED25519)
|_ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIPAFvsTY9DDOQfDHXH5SuOvmF0PnGUgaOJvv9eH4JUGz
9999/tcp open  abyss?  syn-ack ttl 63
| fingerprint-strings: 
|   FourOhFourRequest, GetRequest, HTTPOptions: 
|     HTTP/1.0 200 OK
|     Date: Wed, 02 Jul 2025 18:43:30 GMT
|     Content-Length: 0
|   GenericLines, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq, TerminalServerCookie: 
|     HTTP/1.1 400 Bad Request
|     Content-Type: text/plain; charset=utf-8
|     Connection: close
|_    Request
``` 
