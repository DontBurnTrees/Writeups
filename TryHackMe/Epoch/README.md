## Room:  Epoch 

##### Description:   Be honest, you have always wanted an online tool that could help you convert UNIX dates and timestamps!  

#### Difficulty: Easy 

## Recon & Enumeration

All ports tcp scan:
```
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
```
- I know from the description that I have to dig the web app, I also know that the room is about command injections.


## Exploitation

- First, I used the application like a standard user so I passed `1763025890` in the user input, which gave me UTC conversion. I innocently tried to add `;` after the date in
 order to execute a second linux command, and it worked !

- I enumerated the directories however I had no idea where to find the flag, thanks to the hint I was able to find the flag with the following payload `1763025890 ; env`

*Find the flag in this vulnerable web application!*
**Q1** - `flag{7da6c7[...]bd9b647}`


### Date: 13/11/2025
