import asyncio
import logging
import sys
from os import getenv
from typing import Any, Dict
from data.movieApi import get_movies_by_genre

from aiogram import Bot, Dispatcher, F, Router, html
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    KeyboardButton,
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
)

TOKEN = "6735935500:AAEsxVeWPu9qjveLOS8WZt0JINbrcXTNtZ4"

form_router = Router()




@form_router.message(CommandStart())
@form_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    genre = "Romance"
    
    # Call the API function
    movies_data = get_movies_by_genre( genre)
    
    # Handle the API response as needed
    if movies_data:
        filtered = [movie['id'] for movie in movies_data['results']]
        images_link = [movie['primaryImage']['url'] for movie in movies_data['results'] if movie['primaryImage'] is not None]
        
        # Process the movies_data, you can send it as a response to the user, for example:
        await message.answer(f"Here are some drama movies: {' '.join(filtered[:200])}")
        
        # Send images in a media group
        media = [InputMediaPhoto(media=link) for link in images_link]
        await message.answer_media_group(media=media)
        
        # Return the images link along with filtered movie IDs
        return filtered, images_link
    else:
        await message.answer("Sorry, something went wrong with the movie API.")
    






async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_router(form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())