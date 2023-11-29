from aiogram.dispatcher.filters.state import StatesGroup, State 


class Movie(StatesGroup):
    movie_series = State()
    