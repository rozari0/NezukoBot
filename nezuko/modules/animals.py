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

__MODULE__ = "Animals"
__HELP__ = """/catfacts - To Get Facts About Cat.
/dogfacts - To Get Facts About Dog.
/animalfacts - To Get Facts About Animal.
"""


@app.on_message(filters.command("catfacts"))
@capture_err
async def catfacts(client, message):
    """
    Get cat facts
    """
    message = await message.reply_text("`Getting cat facts...`")
    resp = await get("https://cat-fact.herokuapp.com/facts/random")
    return await message.edit(resp["text"])


@app.on_message(filters.command("animalfacts"))
@capture_err
async def animalfacts(client, message):
    somerandomvariable = await get("https://axoltlapi.herokuapp.com/")
    return await message.reply_photo(
        somerandomvariable["url"], caption=somerandomvariable["facts"]
    )


@app.on_message(filters.command("dogfacts"))
@capture_err
async def dogfacts(client, message):
    somerandomvariable = await get(
        "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
    )
    return await message.reply_text(somerandomvariable[0]["fact"])
