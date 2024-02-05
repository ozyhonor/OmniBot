import sys
import logging
from handlers.start import start_router
from handlers.premium import premium_router
from handlers.gpt_handlers.gpt_router import gpt_router
from handlers.gpt_handlers.gpt_text import gpt_text
from handlers.gpt_handlers.gpt_file_queue import gpt_file_queue
from handlers.gpt_handlers.gpt_settings import gpt_settings
from handlers.gpt_handlers.gpt_file import gpt_file
from handlers.text_to_speech_gpt.speech_router import speech_router
from handlers.text_to_speech_gpt.speech_settings import speech_settings_router
from handlers.text_to_speech_gpt.speech_text import speech_text_router
from handlers.text_to_speech_gpt.speech_file import speech_file_router


from spawnbot import dp, bot
import asyncio

logging.basicConfig(level=logging.INFO,
                    handlers=[
                        logging.StreamHandler(sys.stdout)  # output to file AND console
                    ],
                    format="%(asctime)s - %(levelname)s\t%(module)s/%(funcName)s:%(lineno)d\t- %(message)s",
                    datefmt='%d/%m/%Y %H:%M:%S',
                    )


async def on_startup(_):
    logging.info('Bot started.')


async def main() -> None:
    dp.include_routers(
        premium_router,
        start_router,
        gpt_router,
        gpt_file,
        gpt_file_queue,
        gpt_text,
        gpt_settings,
        speech_router,
        speech_settings_router,
        speech_text_router,
        speech_file_router
    )
    await dp.start_polling(bot, skip_updates=False, on_startup=on_startup)

if __name__ == '__main__':
    asyncio.run(main())

