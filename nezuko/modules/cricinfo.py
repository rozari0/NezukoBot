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

from bs4 import BeautifulSoup
from pyrogram import filters

from nezuko import app
from nezuko.core.decorators.errors import capture_err
from nezuko.utils.http import get, resp_get

__MODULE__ = "CricInfo"
__HELP__ = """
/cricinfo - Get the latest score of the match.
"""


@app.on_message(filters.command("cricinfo"))
@capture_err
async def catfacts(client, message):
    score_page = "http://static.cricinfo.com/rss/livescores.xml"
    page = await get(score_page)
    soup = BeautifulSoup(page, "html.parser")
    result = soup.find_all("description")
    Sed = "".join(
        "<code>" + match.get_text() + "</code>\n\n" for match in result
    )
    return await message.reply(Sed, parse_mode="html")
