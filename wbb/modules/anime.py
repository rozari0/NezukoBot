import requests
from pyrogram import filters
from pyrogram.types import Message
from wbb import SUDOERS, app,BOT_USERNAME
from wbb.core.decorators.errors import capture_err
from pyrogram.errors import MediaCaptionTooLong
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
        search_result = requests.get(f"https://kitsu.io/api/edge//anime?filter[text]={message.command}").json()['data'][0]
        try:
            return await message.reply_photo(photo=search_result['attributes']['posterImage']['original'],caption=f"**Title**:{search_result['attributes']['titles']['en']}\n**Japanese**:{search_result['attributes']['titles']['en_jp']}\n**PopularityRank**:{search_result['attributes']['popularityRank']}\n**Age Rating**:{search_result['attributes']['ageRatingGuide']}\n**Episode Count**:{search_result['attributes']['episodeCount']}\n**Synopsis**:{search_result['attributes']['synopsis']}",
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Open In Kitsu", url=f"https://kitsu.io/anime/{search_result['id']}")
                        ],
                        [
                            InlineKeyboardButton(text="Search Again",switch_inline_query_current_chat="anime")
                        ]
                    ]
                ))
        except MediaCaptionTooLong:
            replyto = await message.reply_photo(photo=search_result['attributes']['posterImage']['original'])
            return await message.reply_text(f"**Title**:{search_result['attributes']['titles']['en']}\n**Japanese**:{search_result['attributes']['titles']['en_jp']}\n**PopularityRank**:{search_result['attributes']['popularityRank']}\n**Age Rating**:{search_result['attributes']['ageRatingGuide']}\n**Episode Count**:{search_result['attributes']['episodeCount']}\n**Synopsis**:{search_result['attributes']['synopsis']}",
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Open In Kitsu", url=f"https://kitsu.io/manga/{search_result['id']}")
                        ],
                        [
                            InlineKeyboardButton(text="Search Again",switch_inline_query_current_chat="anime")
                        ]
                    ]
                ),reply_to_message_id=replyto.message_id)


@app.on_message(filters.command(["manga",f"manga@{BOT_USERNAME}"]))
@capture_err
async def manga(client, message: Message):
    if len(message.command)<2:
        return await message.reply_text("Send **/Manga MangaName** to get info.")
    else:
        jikan = Jikan()
        message.command.pop(0)
        search_result = requests.get(f"https://kitsu.io/api/edge//manga?filter[text]={message.command}").json()['data'][0]
        try:
            return await message.reply_photo(photo=search_result['attributes']['posterImage']['original'],caption=f"**Title**:{search_result['attributes']['titles']['en']}\n**Japanese**:{search_result['attributes']['titles']['en_jp']}\n**PopularityRank**:{search_result['attributes']['popularityRank']}\n**Age Rating**:{search_result['attributes']['ageRatingGuide']}\n**Chapter Count**:{search_result['attributes']['chapterCount']}\n**Synopsis**:{search_result['attributes']['synopsis']}",
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Open In Kitsu", url=f"https://kitsu.io/anime/{search_result['id']}")
                        ],
                        [
                            InlineKeyboardButton(text="Search Again",switch_inline_query_current_chat="anime")
                        ]
                    ]
                ))
        except MediaCaptionTooLong:
            replyto = await message.reply_photo(photo=search_result['attributes']['posterImage']['original'])
            return await message.reply_text(f"**Title**:{search_result['attributes']['titles']['en']}\n**Japanese**:{search_result['attributes']['titles']['en_jp']}\n**PopularityRank**:{search_result['attributes']['popularityRank']}\n**Age Rating**:{search_result['attributes']['ageRatingGuide']}\n**Chapter Count**:{search_result['attributes']['chapterCount']}\n**Synopsis**:{search_result['attributes']['synopsis']}",
            reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Open In Kitsu", url=f"https://kitsu.io/anime/{search_result['id']}")
                        ],
                        [
                            InlineKeyboardButton(text="Search Again",switch_inline_query_current_chat="anime")
                        ]
                    ]
                ),reply_to_message_id=replyto.message_id)
