<h1 align="center">
    ✨ NezukoBot ✨
</h1>

<h3 align="center">
    Telegram Group Manager Bot Written In Python Using Pyrogram.
</h3>
<h4 align="center">
    :exclamation: Please star this project before using it.
</h4>

<p align="center">
    <a href="https://python.org">
        <img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python">
    </a>
    <a href="https://GitHub.com/rozari0">
        <img src="http://ForTheBadge.com/images/badges/built-with-love.svg" alt="built-with-love">
    </a> <br>
    <img src="https://img.shields.io/github/license/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/rozari0/NezukoBot?style=for-the-badge&logo=appveyor" alt="Repository Size"> <br>
    <img src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge&logo=appveyor" alt="Python Version">
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
<h1>
    <p align="center">
        <a href="https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Frozari0%2FNezukoBot&plugins=mongodb&envs=BOT_TOKEN%2CAPI_ID%2CAPI_HASH%2CSUDO_USERS_ID%2CLOG_GROUP_ID%2CGBAN_LOG_GROUP_ID%2CWELCOME_DELAY_KICK_SEC%2CARQ_API_URL%2CMESSAGE_DUMP_CHAT%2CARQ_API_KEY%2CRSS_DELAY&optionalEnvs=SESSION_STRING%2CUSERBOT_PREFIX&BOT_TOKENDesc=Obtain+a+Telegram+bot+token+by+contacting+%40BotFather&API_IDDesc=API_ID+of+your+Telegram+Account+my.telegram.org%2Fapps&API_HASHDesc=API_HASH+of+your+Telegram+Account+my.telegram.org%2Fapps&SUDO_USERS_IDDesc=Sudo+users+have+full+access+to+everythin%2C+don%27t+trust+anyone...+ex%3A-+123456+654311+123456&LOG_GROUP_IDDesc=For+logs+channel+to+note+down+important+bot+level+events%2C+recommend+to+make+this+public.+ex%3A+%27-123456%27&GBAN_LOG_GROUP_IDDesc=gban+logs.+ex%3A+%27-123456%27&WELCOME_DELAY_KICK_SECDesc=Welcome+Delay+Kick+Sec&ARQ_API_URLDesc=For+Music+Downloading+And+Many+More+Things...+Don%27t+change+this+value&MESSAGE_DUMP_CHATDesc=Chat_id+of+the+group+where+useless+things+will+go&ARQ_API_KEYDesc=Get+this+from+%40ARQRobot.&RSS_DELAYDesc=Delay+in+which+RSS+will+send+updates+in+chat&PM_PERMITDesc=Pm+permit%2C+fill+1+to+enable+or+0+to+disable+it.&WELCOME_DELAY_KICK_SECDefault=300&ARQ_API_URLDefault=https%3A%2F%2Fthearq.tech&LOG_MENTIONSDefault=1&RSS_DELAYDefault=300">
            <img src="https://railway.app/button.svg" alt="Deploy on Railway">
        </a>
    </p>
</h1>

<h1>
    <p align="center">
        <a href="https://heroku.com/deploy?template=https://github.com/rozari0/NezukoBot">
            <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
        </a>
    </p>
</h1>

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
