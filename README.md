<h1 align="center">
    ✨ NezukoBot ✨
</h1>

<h1  align="center" style='color:red;'>:warning: THIS PROJECT IS DEAD. DO NOT USE IT, MIGHT RUN INTO UNKNOWN PROBLEMS.</h1>

<h3 align="center">
    Telegram Group Manager Bot Written In Python Using Pyrogram.
</h3>
<h4 align="center">
    :exclamation: Please star this project before using it.
</h4>

<p align="center">
    <img src="https://img.shields.io/github/license/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="Repository Size"> <br>
    <img src="https://img.shields.io/badge/python-3.11-green?style=for-the-badge&logo=appveyor" alt="Python Version">
    <img src="https://img.shields.io/github/issues/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="Issues">
    <img src="https://img.shields.io/github/forks/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="Forks">
    <img src="https://img.shields.io/github/stars/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="Stars">
</p>

<h3 align="center">
    Ready to use method
</h3>

<p align="center">
    A ready-to-use running instance of this bot can be found on Telegram <br>
    <a href="https://t.me/NezukoDemonBot"> NezukoBot </a>
</p>

<h2 align="center">
   ⇝ Requirements ⇜
</h2>

<p align="center">
    <a href="https://www.python.org/downloads/release/python-390/"> Python3.9 </a> |
    <a href="https://docs.pyrogram.org/intro/setup#api-keys"> Telegram API Key </a> |
    <a href="https://t.me/botfather"> Telegram Bot Token </a> |
    <a href="https://telegra.ph/How-To-get-Mongodb-URI-04-06"> MongoDB URI </a>
</p>

<h2 align="center">
   ⇝ Install Locally Or On A VPS ⇜
</h2>

```console
git clone https://github.com/rozari0/NezukoBot
cd NezukoBot
pip3 install -U -r requirements.txt
cp sample_config.env config.env
```

<h3 align="center">
    Edit <b>config.env</b> with your own values
</h3>

<h2 align="center">
   ⇝ Run Directly ⇜
</h2>

```console
python3 -m nezuko
```

<h1 align="center">
   ⇝ Docker ⇜
</h1>

```console
git clone https://github.com/rozari0/NezukoBot
cd NezukoBot
cp sample_config.env config.env
```

<h3 align="center">
    Edit <b> config.env </b> with your own values
</h3>

```console
sudo docker build . -t nezuko
sudo docker run nezuko
```

<h2 align="center">
   ⇝ Write new modules ⇜
</h2>

```py
# Add license text here, get it from below

from nezuko import app # This is bot's client
from pyrogram import filters # pyrogram filters
...


# For /help menu
__MODULE__ = "Module Name"
__HELP__ = "Module help message"


@app.on_message(filters.command("start"))
async def some_function(_, message):
    await message.reply_text("I'm already up!!")

# Many useful functions are in, nezuko/utils/, nezuko, and nezuko/core/
```

<h3 align="center">
   And put that file in nezuko/modules/, restart and test your bot.
</h3>

# Credits

Thanks to:
- [`TheHamkerCat`](https://github.com/TheHamkerCat) for build up of this bot from scratch and ARQ api. :3
- [`delivrance`](https://github.com/delivrance) for pyrogram.
- [`rozari0`](https://github.com/rozari0) for some extra features & fixes.

And many more people who aren't mentioned here, but can be found in [Contributors](https://github.com/rozari0/NezukoBot/graphs/contributors).
