<h1 align="center">Guildead</h1>

<p align='center'>
    <img src='https://media.discordapp.net/attachments/933087958288986123/934243026958692362/1200x600wa.png'>
</p>

-----

- Guilded api wrapper written in python.
- I have found "exploit" (guilded broken as fuck): `blank_message`

-----

```py
from Guildead import Guilded, Exploit

if __name__ == '__main__':
    guilded = Guilded()
    guilded.login('email', 'password')

    # send blank message
    guilded.send_message('channel_id', Exploit.blank_message(), isSilent=True, isPrivate=True, repliesTo=['reply_to_id'], confirmed=True)
```

-----

<p align="center"> 
    <b>Informations</b><br>
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Its-Vichy/Guildead?style=social">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Its-Vichy/Guildead">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Its-Vichy/Guildead">
</p>
