"""
MIT License

Copyright (c) 2021 rozari0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from pyrogram import filters
from wbb.utils.http import get
from wbb import app
from wbb.utils.dbfunctions import get_nsfw_status,set_nsfw_status
from wbb.core.decorators.errors import capture_err
from wbb.core.decorators.permissions import adminsOnly


__MODULE__ = "Anime Pics"
__HELP__ = "**Get SFW (Safe for work) Anime Pics. Try This Commands:**"
BASE_URL = "https://api.waifu.pics/"

commands = ['waifu','neko','shinobu','megumin','bully','cuddle','cry',
            'hug','awoo','kiss','lick','pat','smug','bonk','yeet','blush',
            'smile','wave','highfive','handhold','nom','bite','glomp','slapgif',
            'kill','kick','happy','wink','poke','dance','cringe']

for _i in commands:
    __HELP__ += f"\n/{_i}"

__HELP__ += "\n\n**Get NSFW (Not Safe for work) Anime Pics. Try This Commands:**"
nsfw_commands = ['trap','blowjob','nsfwwaifu','nwaifu','nsfwneko']
for _i in nsfw_commands:
    __HELP__ += f"\n/{_i}"


@app.on_message(filters.command("waifu"))
@capture_err
async def waifu(client, message):
    m = await message.reply_text("Getting a random waifu...")
    data = await get(f"{BASE_URL}sfw/waifu")
    await message.reply_photo(data["url"])
    return await m.delete()

@app.on_message(filters.command("neko"))
@capture_err
async def neko(client, message):
    m = await message.reply_text("Getting a random neko...")
    data = await get(f"{BASE_URL}sfw/neko")
    await message.reply_photo(data["url"])
    return await m.delete()

@app.on_message(filters.command("shinobu"))
@capture_err
async def shinobu(client, message):
    m = await message.reply_text("Getting a random shinobu...")
    data = await get(f"{BASE_URL}sfw/shinobu")
    await message.reply_photo(data["url"])
    return await m.delete()

@app.on_message(filters.command("megumin"))
@capture_err
async def megumin(client, message):
    m = await message.reply_text("Getting a random megumin...")
    data = await get(f"{BASE_URL}sfw/megumin")
    await message.reply_photo(data["url"])
    return await m.delete()

@app.on_message(filters.command("bully"))
@capture_err
async def bully(client, message):
    m = await message.reply_text("Getting a random bully...")
    data = await get(f"{BASE_URL}sfw/bully")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("cuddle"))
@capture_err
async def cuddle(client, message):
    m = await message.reply_text("Getting a random cuddle...")
    data = await get(f"{BASE_URL}sfw/cuddle")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("cry"))
@capture_err
async def cry(client,message):
    m = await message.reply_text("Getting a random cry...")
    data = await get(f"{BASE_URL}sfw/cry")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("hug"))
@capture_err
async def hug(client,message):
    m = await message.reply_text("Getting a random hug...")
    data = await get(f"{BASE_URL}sfw/hug")
    await message.reply_animation(data["url"])
    return await m.delete()
@app.on_message(filters.command("awoo"))
@capture_err
async def awoo(client,message):
    m = await message.reply_text("Getting a random awoo...")
    data = await get(f"{BASE_URL}sfw/awoo")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("kiss"))
@capture_err
async def kiss(client,message):
    m = await message.reply_text("Getting a random kiss...")
    data = await get(f"{BASE_URL}sfw/kiss")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("lick"))
@capture_err
async def lick(client,message):
    m = await message.reply_text("Getting a random lick...")
    data = await get(f"{BASE_URL}sfw/lick")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("pat"))
@capture_err
async def pat(client,message):
    m = await message.reply_text("Getting a random pat...")
    data = await get(f"{BASE_URL}sfw/pat")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("smug"))
@capture_err
async def smug(client,message):
    m = await message.reply_text("Getting a random smug...")
    data = await get(f"{BASE_URL}sfw/smug")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("bonk"))
@capture_err
async def bonk(client,message):
    try:
        await message.delete()
    except:
        pass
    m = await message.reply_text("Getting a random bonk...")
    data = await get(f"{BASE_URL}sfw/bonk")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("yeet"))
@capture_err
async def yeet(client,message):
    m = await message.reply_text("Getting a random yeet...")
    data = await get(f"{BASE_URL}sfw/yeet")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("blush"))
@capture_err
async def blush(client,message):
    m = await message.reply_text("Getting a random blush...")
    data = await get(f"{BASE_URL}sfw/blush")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("smile"))
@capture_err
async def smile(client,message):
    m = await message.reply_text("Getting a random smile...")
    data = await get(f"{BASE_URL}sfw/smile")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("wave"))
@capture_err
async def wave(client,message):
    m = await message.reply_text("Getting a random wave...")
    data = await get(f"{BASE_URL}sfw/wave")
    await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("highfive"))
@capture_err
async def highfive(client,message):
    m = await message.reply_text("Getting a random highfive...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/highfive")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("handhold"))
@capture_err
async def highfive(client,message):
    m = await message.reply_text("Getting a random handhold...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/handhold")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("nom"))
@capture_err
async def highfive(client,message):
    m = await message.reply_text("Getting a random nom...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/nom")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()


@app.on_message(filters.command("bite"))
@capture_err
async def highfive(client,message):
    m = await message.reply_text("Getting a random bite...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/bite")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("glomp"))
@capture_err
async def glomp(client,message):
    m = await message.reply_text("Getting a random glomp...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/glomp")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("slapgif"))
@capture_err
async def slap(client,message):
    m = await message.reply_text("Getting a random slap...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/slap")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("kill"))
@capture_err
async def kill(client,message):
    m = await message.reply_text("Getting a random kill...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/kill")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("kick"))
@capture_err
async def kick(client,message):
    m = await message.reply_text("Getting a random kick...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/kick")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("happy"))
@capture_err
async def happy(client,message):
    m = await message.reply_text("Getting a random happy image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/happy")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("wink"))
@capture_err
async def happy(client,message):
    m = await message.reply_text("Getting a random wink image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/wink")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()

@app.on_message(filters.command("poke"))
@capture_err
async def happy(client,message):
    m = await message.reply_text("Getting a random poke image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/poke")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()


@app.on_message(filters.command("dance"))
@capture_err
async def happy(client,message):
    m = await message.reply_text("Getting a random dance image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/dance")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()


@app.on_message(filters.command("cringe"))
@capture_err
async def happy(client,message):
    m = await message.reply_text("Getting a random cringe image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}sfw/cringe")
    if message.reply_to_message:
        await message.reply_to_message.reply_animation(data["url"])
    else:
        await message.reply_animation(data["url"])
    return await m.delete()



@app.on_message(filters.command("nsfw") & filters.group)
@adminsOnly("can_change_info")
async def nsfw(client,message):
    if len(message.command)>=2 and message.command[1].lower() == "on":
        if await get_nsfw_status(message.chat.id) != False:
            return await message.reply_text("NSFW mode already enabled")

        await set_nsfw_status(message.chat.id,True)
        return await message.reply_text("NSFW mode enabled")
    elif len(message.command)>=2 and message.command[1].lower() == "off":
        if await get_nsfw_status(message.chat.id):
            await message.reply_text("Turning NSFW off...")
            return await set_nsfw_status(message.chat.id,False)
        else:
            await message.reply_text("NSFW is already off!")
            return
    else:
        return await message.reply_text("Usage: /nsfw [on/off]")
    
@app.on_message(filters.command("nsfw") & filters.private)
async def nsfw(client,message):
    if len(message.command)>=2 and message.command[1].lower() == "on":
        if await get_nsfw_status(message.chat.id) != False:
            return await message.reply_text("NSFW mode already enabled")

        await set_nsfw_status(message.chat.id,True)
        return await message.reply_text("NSFW mode enabled")
    elif len(message.command)>=2 and message.command[1].lower() == "off":
        if await get_nsfw_status(message.chat.id):
            m = await message.reply_text("Turning NSFW off...")
            await set_nsfw_status(message.chat.id,False)
            return m.edit("NSFW is now off!")
        else:
            await message.reply_text("NSFW is already off!")
            return
    else:
        return await message.reply_text("Usage: /nsfw [on/off]")

@app.on_message(filters.command(["nsfwwaifu","nwaifu"]))
@capture_err
async def nsfwwaifu(client,message):
    if await get_nsfw_status(message.chat.id) == False:
        return await message.reply_text("NSFW mode is off! Turn it on to use this command!")
    m = await message.reply_text("Getting a random nsfw waifu image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}nsfw/waifu")
    if message.reply_to_message:
        try:
            await message.reply_to_message.reply_photo(data["url"])
        except:
            await message.reply_to_message.reply_photo(data["url"])
    else:
        try:
            await message.reply_photo(data["url"])
        except:
            await message.reply_photo(data["url"])
    return await m.delete()

@app.on_message(filters.command(["nsfwneko"]))
@capture_err
async def nsfwneko(client,message):
    if await get_nsfw_status(message.chat.id) == False:
        return await message.reply_text("NSFW mode is off! Turn it on to use this command!")
    m = await message.reply_text("Getting a random nsfw neko image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}nsfw/neko")
    if message.reply_to_message:
        try:
            await message.reply_to_message.reply_photo(data["url"])
        except:
            await message.reply_to_message.reply_photo(data["url"])
    else:
        try:
            await message.reply_photo(data["url"])
        except:
            await message.reply_photo(data["url"])
    return await m.delete()

@app.on_message(filters.command(["nsfwtrap","trap"]))
@capture_err
async def nsfwtrap(client,message):
    if await get_nsfw_status(message.chat.id) == False:
        return await message.reply_text("NSFW mode is off! Turn it on to use this command!")
    m = await message.reply_text("Getting a random nsfw trap image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}nsfw/trap")
    if str(data["url"]).endswith(".gif"):
        try:
            await message.reply_animation(data["url"])
        except:
            await message.reply_animation(data["url"])
    else:
        try:
            await message.reply_photo(data["url"])
        except:
            await message.reply_photo(data["url"])
    return await m.delete()

@app.on_message(filters.command("blowjob"))
@capture_err
async def blowjob(client,message):
    if await get_nsfw_status(message.chat.id) == False:
        return await message.reply_text("NSFW mode is off! Turn it on to use this command!")
    m = await message.reply_text("Getting a random nsfw blowjob image...")
    try:
        await message.delete()
    except:
        pass
    data = await get(f"{BASE_URL}nsfw/blowjob")
    if message.reply_to_message:
        try:
            await message.reply_to_message.reply_animation(data["url"])
        except:
            await message.reply_to_message.reply_animation(data["url"])
    else:
        try:
            await message.reply_animation(data["url"])
        except:
            await message.reply_animation(data["url"])
    return await m.delete()
