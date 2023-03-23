import logging

from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Command, CommandStart, Text, Regexp, ContentTypeFilter, IDFilter
import aiogram.utils.markdown as fmt

from config import TOKEN, SECRET_KEY

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


# https://t.me/fhasidfhoiwfbbot?start=some_data
# https://t.me/{bot.username}?start=deep_link
@dp.message_handler(CommandStart(deep_link='some_data'))
async def hello_handler(message: types.Message):
    await message.reply(f"Привет это фильтр с deep_link и some_data")


@dp.message_handler(CommandStart())
async def hello_handler(message: types.Message):
    await message.reply(f"Привет это фильтр без deep_link")


@dp.message_handler(text='Привет')
async def hello_handler(message: types.Message):
    await message.reply(f"Привет {message.from_user.username}")


@dp.message_handler(Command(commands=['hi'], prefixes='!'))
async def command_hi_handler(message: types.Message):
    await message.reply(f"Привет {message.from_user.username}")


@dp.message_handler(Text(contains=['hello'], ignore_case=True))
async def text_handler(message: types.Message):
    await message.reply("Привет hello")


@dp.message_handler(Regexp(regexp=r'^\d'))
async def regexp_handler(message: types.Message):
    await message.reply("Привет Regexp")


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo_handler(message: types.Message):
    file_id = message.photo[-1].file_id
    await message.reply("Привет ты отправил фото")
    await message.answer_photo(file_id)


@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def document_handler(message: types.Message):
    await message.reply("Привет ты отправил документ")
    file_id = message.document.file_id
    await message.answer_document(file_id, caption='Привет ты отправил документ')


@dp.message_handler(text='hi', chat_type='private')
async def hi_handler(message: types.Message):
    print(message.from_user.id)
    await message.answer(
        text="<i>Привет</i>",
        # parse_mode=types.ParseMode.HTML
    )
    await message.answer(
        text="<i>Привет</i>",
        parse_mode=''
    )

    await message.answer(
        text="*Привет*",
        parse_mode=types.ParseMode.MARKDOWN_V2
    )
    await message.answer(
        text="*Привет*",
        parse_mode=None
    )


@dp.message_handler(IDFilter(user_id=5014092219))
async def echo_handler(message: types.Message):
    # text = fmt.hbold("echo:")
    # print(text)
    # await message.answer(
    #     text=f'{text} {message.text}',
    # )
    url = 'https://avatars.mds.yandex.net/get-altay/758053/2a00000161d22ba78905383969d3d1b343b2/XXXL'
    await message.answer(
        text=f'<b>echo:</b> {fmt.quote_html(message.text)}{fmt.hide_link(url)}',
        parse_mode='HTML'
    )
    quote_html_text = fmt.escape_md(message.text)
    print(quote_html_text)
    await message.answer(
        text=fmt.text(
            f'echo: {quote_html_text}',
            f'{fmt.bold("echo:")} {quote_html_text}',
            sep='\n'
        ),
        parse_mode=types.ParseMode.MARKDOWN_V2
    )

    await message.answer(
        text=fmt.hlink(title='Кликни на меня', url=url),
        disable_web_page_preview=True
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
