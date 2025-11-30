## Room: GLITCH 

##### Description:   This is a simple challenge in which you need to exploit a vulnerable web application and root the machine. It is beginner oriented, some basic JavaScript knowledge would be helpful, but not mandatory. Feedback is always appreciated. 

## Recon & Enumeration

All ports tcp scan:
```
PORT   STATE SERVICE
80/tcp open  http
```
- I went to the web app and I got a weird page with nothing to see so I decided to ctrl + U the page in order to look at the source code which exposed a lot of information.

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>not allowed</title>

    <style>
      * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }
      body {
        height: 100vh;
        width: 100%;
        background: url('img/glitch.jpg') no-repeat center center / cover;
      }
    </style>
  </head>
  <body>
    <script>
      function getAccess() {
        fetch('/api/access')
          .then((response) => response.json())
          .then((response) => {
            console.log(response);
          });
      }
    </script>
  </body>
</html>
```

- I tried to go to /img/ to list files but it did not worked, however the /api/access gave me the the access token `{"token":"dGhpc19pc19ub3RfcmVhbA=="}` the two equals at the end of the string is indicating that this is probably encoded in base64. I used cyberchef to decode the string and I got `this_is_not_real`

*What is your access token?*        
**Q1** - `this_is_not_real`


## Exploitation

- If we review the informations we collected we have : an endpoint to an API and an acess token to this API. Our goal is to get a foothold on the machine we could try to enumerate further this endpoint and maybe try to request for more information using our access token.

- 
*Question ?*    
**QX** - `answer`

## Privilege escalation

- ... 

*Question ?*    
**QX** - `answer`

### Date: 14/11/2025
