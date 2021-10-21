from pyrogram import filters
from pyrogram.types import Message
from wbb import SUDOERS, app, arq,BOT_USERNAME
from wbb.core.decorators.errors import capture_err
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton,InlineQuery, InlineQueryResultArticle,InputTextMessageContent
from jikanpy import Jikan
__MODULE__ = "Fun"
__HELP__ = """
/anime - Get Anime Info.
"""

@app.on_message(filters.command(["anime",f"anime@{BOT_USERNAME}"]))
@capture_err
async def anime(client, message: Message):
    if len(message.command)<2:
        return await message.reply_text("Send **/Anime AnimeName** to get info.")
    else:
        jikan = Jikan()
        message.command.pop(0)
        search_result = jikan.search('anime', f"{' '.join(message.command)}", page=1)['results'][0]
        return await message.reply_photo(photo=search_result["image_url"],caption=f"**Title**:{search_result['title']}\n**Type**:{search_result['type']}\n**Score**:{search_result['score']}\n**Synopsis**:{search_result['synopsis']}",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Open In My Anime List", url=search_result['url'])
                    ],
                    [
                        InlineKeyboardButton(text="Search Again",switch_inline_query_current_chat="anime")
                    ]
                ]
            ))

@app.on_message(filters.command(["manga",f"manga@{BOT_USERNAME}"]))
@capture_err
async def manga(client, message: Message):
    if len(message.command)<2:
        return await message.reply_text("Send **/Anime AnimeName** to get info.")
    else:
        jikan = Jikan()
        message.command.pop(0)
        search_result = jikan.search('manga', f"{' '.join(message.command)}", page=1)['results'][0]
        return await message.reply_photo(photo=search_result["image_url"],caption=f"**Title**:{search_result['title']}\n**Type**:{search_result['type']}\n**Chapters**:{search_result['chapters']}\n**Volumes**:{search_result['volumes']}\n**Score**:{search_result['score']}\n**Synopsis**:{search_result['synopsis']}",
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Open In My Anime List", url=search_result['url'])
                    ],
                    [
                        InlineKeyboardButton(text="Search Again",switch_inline_query_current_chat="manga")
                    ]
                ]
            ))
