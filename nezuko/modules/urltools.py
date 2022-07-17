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

from nezuko import app
from nezuko.core.decorators.errors import capture_err
from nezuko.utils.http import get, resp_get

__MODULE__ = "Url Tools"
__HELP__ = """/short - To Short a url. Use **/short url coustom** to get coustom link.
/unshort - To unshort a url."""


@app.on_message(filters.command("short"))
@capture_err
async def short(_, message):
    if len(message.command) < 2:
        return await message.reply_text(
            "**/short sho.rt/url** To short a url."
        )
    url = message.command[1]
    if not url.startswith("http"):
        url = "http://" + url
    try:
        short = message.command[2]
        shortRequest = await get(
            f"https://api.1pt.co/addURL?long={url}&short={short}"
        )
        short = shortRequest["short"]
        return await message.reply_text(
            f"**URL After Short: `https://1pt.co/{short}`**"
        )
    except IndexError:
        shortRequest = await get(f"https://api.1pt.co/addURL?long={url}")
        short = shortRequest["short"]
        return await message.reply_text(
            f"**URL After Short: `https://1pt.co/{short}`**"
        )
    except Exception as e:
        return await message.reply_text(f"**{e}**")


@app.on_message(filters.command("unshort"))
@capture_err
async def unshort(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**/unshort url** To unshort a url.")
    url = message.command[1]
    if not url.startswith("http"):
        url = "http://" + url
    try:
        mainurl = await resp_get(url)
        return await message.reply_text(
            f"**URL After Unshort: `{mainurl.url}`**"
        )
    except Exception as e:
        return await message.reply_text(f"**{e}**")
