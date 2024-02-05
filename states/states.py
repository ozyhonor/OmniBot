from aiogram.fsm.state import State, StatesGroup

stop_gpt = False
stop_eden = False

class WaitingPremium(StatesGroup):
    new_premium_id = State()

class WaitingStartSpeech(StatesGroup):
    rate = State()
    voice = State()
    text_speech = State()
    file_speech = State()
    queue_speech = State()


class WaitingStateGpt(StatesGroup):
    queue_files = State()
    settings = State()
    text_gpt = State()
    file_gpt = State()
    degree = State()
    theme = State()
