from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class CustomKeyboard:
    def __init__(self):
        self.reply_markup = None


    @staticmethod
    def create_inline_kb_gpt_settings():
        names_settings_gpt = ['⚙️ Настройки', '🌡 Градус']
        builder = InlineKeyboardBuilder()
        for name in names_settings_gpt:
            builder.button(text=f"{name}", callback_data=f"{name}")

        return builder

    @staticmethod
    def create_inline_kb_default_settings():

        builder = InlineKeyboardBuilder()
        builder.button(text=f"Оставить текущие настройки.", callback_data="leave_current_settings")

        return builder

    @staticmethod
    def create_queue_button():
        names_gender = ['✅ Выполнить', '🎛 Настройка']
        builder = InlineKeyboardBuilder()
        for name in names_gender:
            builder.button(text=f"{name}", callback_data=f"{name}")
        return builder

    @staticmethod
    def create_stop_button():

        builder = InlineKeyboardBuilder()
        builder.button(text=f"Остановить", callback_data="stop_gpt")

        return builder

    @staticmethod
    def create_stop_eden_button():

        builder = InlineKeyboardBuilder()
        builder.button(text=f"Остановить", callback_data="stop_eden")

        return builder

    @staticmethod
    def create_gpt_buttons():

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='◀️ Назад'),
                    KeyboardButton(text='🗒 Текст'),
                    KeyboardButton(text='🗂 Файл'),
                    KeyboardButton(text='🗄 Очередь')
                ]
                ],  resize_keyboard=True)

        return keyboard


    @staticmethod
    def create_inline_speech_settings():

        names_settings_speech = ['🔊 Скорость', '🗣 Голос']
        builder = InlineKeyboardBuilder()
        for name in names_settings_speech:
            builder.button(text=f"{name}", callback_data=f"{name}")
        return builder

    @staticmethod
    def create_speech_main():

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='◀️ Назад'),
                    KeyboardButton(text='✉️ Сообщение'),
                    KeyboardButton(text='📁 Файл')
                ]
                ],  resize_keyboard=True)

        return keyboard



    @staticmethod
    def create_acsess():
        names_gender = ['✅ ᚢᚹᛋᚺᚱᛠⰓ', '❌ ᛜᛠᛕᚳᛜᚺᛋᛠⰓ']
        builder = InlineKeyboardBuilder()
        for name in names_gender:
            builder.button(text=f"{name}", callback_data=f"{name}")
        return builder


    @staticmethod
    def create_reply_main_menu():

        names_main_funcs = ['ChatGpt', 'Synthesis']
        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='🤖 ChatGpt'),
                    KeyboardButton(text='🎧 Озвучка'),
                    KeyboardButton(text='💱 Переводчик')
                ]
                ],  resize_keyboard=True)

        return keyboard

    @staticmethod
    def create_pls_accept():

        keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(text='🙏 Доступ')
                ]
                ],  resize_keyboard=True)

        return keyboard




