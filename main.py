import asyncio
from aiogram import Bot, Dispatcher
from aiogram import types
import logging
import aiogram
from aiogram.dispatcher import router
import time
from datetime import datetime, timedelta
import json

BOT_TOKEN = "2125858661:AAE8aIV6joGpotg7dQ_dmDuZQnNn7PwsxTE"
TEST_CHAT_ID = -1001698115602
CHAT_ID = -1761446795

refs = None
with open('refs.json', 'r', encoding='utf-8') as f:
    refs = json.load(f)

dp = Dispatcher()
router1 = router.Router()
dp.include_router(router1)
bot = Bot(BOT_TOKEN, parse_mode="HTML")

message_delay = 15

@dp.message()

@dp.message(commands=['reflink'], commands_prefix='/')
async def filter_message(message: types.Message):
    await message.delete()
    print(message.chat.id)
    if not message.from_user.username in refs.keys():
        link = await bot.create_chat_invite_link(
            chat_id=CHAT_ID,
            name=message.from_user.username,
            expire_date=datetime.now() + timedelta(14),
            member_limit=9999
        )
        message_obj = await message.answer(link.invite_link)
        refs[message.from_user.username] = link.invite_link
        with open('refs.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(refs))
        await asyncio.sleep(message_delay)
        await message_obj.delete()

    else:
        message_obj = await message.answer(f'На одного человека только 1 реферальная ссылка, вот ваша: {refs[message.from_user.username]} ')
        await asyncio.sleep(message_delay)
        await message_obj.delete()


def main() -> None:
    dp.run_polling(bot)


if __name__ == "__main__":
    main()
