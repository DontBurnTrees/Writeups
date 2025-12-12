## Room:  c4ptur3-th3-fl4g 

##### Description:   A beginner level CTF challenge 

#### Difficulty: Easy 

## Translation & Shifting 

- At first we have some leet text which consist of replacing letters with certains numbers.

*c4n y0u c4p7u23 7h3 f149?*    
**Q1** - `can you capture the flag?`

- For the next 7 questions I used the following websites `https://www.dcode.fr/identification-chiffrement` & `https://gchq.github.io/CyberChef/` , the first one being binary 
  
*01101100 01100101 01110100 01110011 00100000 01110100 01110010 01111001 00100000 01110011 01101111 01101101 01100101 00100000 01100010 01101001 01101110 01100001 01110010 01111001 00100000 01101111 01110101 01110100 00100001*      
**Q2** - `lets try some binary out!`

- Then base32
*MJQXGZJTGIQGS4ZAON2XAZLSEBRW63LNN5XCA2LOEBBVIRRHOM======*      
**Q3** - `base32 is super common in CTF's`

- Then base64
*RWFjaCBCYXNlNjQgZGlnaXQgcmVwcmVzZW50cyBleGFjdGx5IDYgYml0cyBvZiBkYXRhLg==*      
**Q4** - `Each Base64 digit represents exactly 6 bits of data.`

- Then hex
*68 65 78 61 64 65 63 69 6d 61 6c 20 6f 72 20 62 61 73 65 31 36 3f*     
**Q5** - `hexadecimal or base16?`

- Then ROT-13
*Ebgngr zr 13 cynprf!*      
**Q6** - `Rotate me 13 places!`

- Then ROT-47 
`*@F DA:? >6 C:89E C@F?5 323J C:89E C@F?5 Wcf E:>6DX`       
**Q7** - `You spin me right round baby right round (47 times)`

- And finally the most toxic one : base64 => morse code => binary => ROT47 => decimal
*LS0tLS0gLi0tLS0gLi0tLS0gL...snip...S0tLS0gLS0tLS0gLi0tLS0gLi0tLS*
**Q8** - `Let's make this a bit trickier...`

## Spectrograms 

- For this question we are having an audio file. On debian based distributions you can download audacity using apt. Then we need to select the spectrogram view in order to view the flag.

*Download the file*    
**Q7** - `Super Secret Message`

## Steganography 

- `steghide extract -sf <image>` on the picture and we have the flag.

*Decode the image to reveal the answer.*    
**Q8** - `SpaghettiSteg`

## Security through obscurity

- We know there is a file inside the image, so I tried a `binwalk -e` on the image and I retrieved the image hackerchat.png  

*Download and get 'inside' the file. What is the first filename & extension?*       
**Q9** - `hackerchat.png`

- From there I used the command strings on the file in order to view potentials traces. 

*Get inside the archive and inspect the file carefully. Find the hidden text.*      
**Q10** - `AHH_YOU_FOUND_ME!`


### Date: 05/12/2025
