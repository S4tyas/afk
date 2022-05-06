from datetime import datetime
from pyrogram import Client, ContinuePropagation, filters ,idle
import asyncio
Client = Client(session_name="BQAW4CU-f1NNNWlyYOIrUTsxpbA87I_0JkJJc2_NXzLAiGtBIIMon3Xss-me5BAUlM3eAJTkMf0pN3XLh6lRjBnPoz1FReWNSP1MdGiD_kdhrTPh4kwfLhsgZDjGoUj8zcNn6y-uRVlQwVxRde2_zB4EVgcS0l8EB8hBjZpYM9J38j5Hri-ROZUmKeBwm4mHnW1qztJ6t2HGbdnffEYh36klCYIa7NknuVLgMSowZ7cKIT0EpS7BCsKKUbqNW6VZuVX7twUM6gMGshwDW-09jMC8y5ceAsIXjv0Qa4VCNuNw7uetwMpxvE1C0PMXceBWDFcmRkWRvp2LRSjWvPCrE7pnQPDjbQA",
api_id=2171111,
api_hash="fd7acd07303760c52dcc0ed8b2f73086")
async def check_afk():
    return True
async def is_afk_(f, client, message):
        return bool(True)
is_afk = filters.create(func=is_afk_, name="is_afk_")
@Client.on_message(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & ~filters.edited
    & filters.incoming
)
async def afk_er(client, message):
    m = message
    mm = """
user id {},
usermention {},
message\n {}
"""
    k = await client.send_message(-1001785568298,mm.format(m.from_user.id, m.from_user.mention,m.text))
    await k.pin()
    ls = "06 May 2022"
    ns = "02 Aug 2022"
    message_to_reply = (
        f"Hi {message.from_user.mention} \n**I am Offilne due to exams! **\nwill be online at** {ns}**, \nOffline From **{ls}**\n\n **Just drop your messages** "
   )
    try:
        await message.reply_sticker("CAACAgIAAxkBAAICS2J1Aq9irRhJr6bHgVoZ6FHy3xdcAAJQFgACZNMYSYc2GfSHBq6nHgQ")
        await message.reply(message_to_reply)
    except:
        await message.reply(message_to_reply)
print("starting")
Client.start()
print("started")
idle()
print("stopped")
