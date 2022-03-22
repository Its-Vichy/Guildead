<h1 align="center">Guildead</h1>

<p align='center'>
    <b>Guilded Rest api wrapper written in python3.</b><br>
    <br>
    <img src='https://media.discordapp.net/attachments/933087958288986123/934243026958692362/1200x600wa.png'>
</p>

-----

- I have found "exploit" (guilded broken as fuck): `blank_message`

-----

```txt
pip install Guildead
```

```py
from Guildead import Guilded, Exploit

if __name__ == '__main__':
    guilded = Guilded(proxy= 'http://127.0.0.1:1337')
    success, response = guilded.login('email', 'password')

    if success:
        print('Login successful!')
    else:
        print(response)

    # send blank message
    guilded.send_message('channel_id', Exploit.blank_message())
    
    # send message and edit and delete it
    message_id = guilded.send_message('channel_id', 'message text')['message']['id']
    guilded.edit_message('channel_id', message_id, "new message text")
    guilded.delete_message('channel_id', message_id)
```
-----

- [X] **Proxy support - HTTP/S, SOCKS4/5**
- [ ] **Gateway websocekt**

-----

<p align="center"> 
    <b>Informations</b><br>
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Its-Vichy/Guildead?style=social">
    <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Its-Vichy/Guildead">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Its-Vichy/Guildead">
</p>
