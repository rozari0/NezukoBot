from pyrogram import filters
from pyrogram.types import Message
import random
from wbb import SUDOERS, app, arq,BOT_USERNAME
from wbb.core.decorators.errors import capture_err
import wbb.utils.fun_strings as fun_strings
from wbb import BOT_ID,BOT_NAME
__MODULE__ = "Fun"
__HELP__ = """
/weebify - To weebify a message.
/wish - To get succession rate! (Just for fun-.-)
/slap - To slap someone.

"""


normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙"
,
]

def weebifytext(text):
    string = text.lower().replace(" ", "  ")
    for normiecharacter in string:
            if normiecharacter in normiefont:
                weebycharacter = weebyfont[normiefont.index(normiecharacter)]
                string = string.replace(normiecharacter, weebycharacter)
    return string


@app.on_message(filters.command(["weebify",f"weebify@{BOT_USERNAME}"]))
@capture_err
async def weebify(client, message: Message):
    if message.reply_to_message:
        return await message.reply_text(weebifytext(message.reply_to_message.text))
    if len(message.command)<2:
        return await message.reply_text("reply **/weebify** To a message for weebify or use **/weebify Your Text**")
    message.command.pop(0)
    return await message.reply_text(weebifytext(' '.join(message.command)))

@app.on_message(filters.command(["slap",f"slap@{BOT_USERNAME}"]) & ~filters.private)
@capture_err
async def slap(client, message: Message):
    if message.reply_to_message:
        try:
            if message.reply_to_message.from_user.id == BOT_ID:
                return await message.reply_text("Stop slapping me. REEEEEEEEEEEEEE.")
        except:
            return await message.reply_text("You Cann't Slap an Anon Admin. :p")
        else:
            try:
                user1 = message.from_user.first_name
            except:
                user1 = message.chat.title
            try:
                user2 = message.reply_to_message.from_user.first_name
            except:
                user2 = message.chat.title
            temp = random.choice(fun_strings.SLAP_TEMPLATES)
            item = random.choice(fun_strings.ITEMS)
            hit = random.choice(fun_strings.HIT)
            throw = random.choice(fun_strings.THROW)
            reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)
            return await message.reply_text(reply,reply_to_message_id=message.reply_to_message.message_id)
    else:
        user1 = BOT_NAME
        try:
            user2 = message.from_user.first_name
        except:
            user2 = message.chat.title
        temp = random.choice(fun_strings.SLAP_TEMPLATES)
        item = random.choice(fun_strings.ITEMS)
        hit = random.choice(fun_strings.HIT)
        throw = random.choice(fun_strings.THROW)
        reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)
        return await message.reply_text(reply)

@app.on_message(filters.command(["wish",f"wish@{BOT_USERNAME}"]))
@capture_err
async def wish(client, message: Message):
    if message.reply_to_message:
        return await message.reply_text(f"Your Wish **{message.reply_to_message.text}** Has {random.randint(1,99)}% Succession Rate!")
    if len(message.command)<2:
        return await message.reply_text("reply **/wish** To a message for wish or use **/wish Your Wish**")
    message.command.pop(0)
    return await message.reply_text(f"Your Wish **{' '.join(message.command)}** Has {random.randint(1,99)}% Succession Rate!")
