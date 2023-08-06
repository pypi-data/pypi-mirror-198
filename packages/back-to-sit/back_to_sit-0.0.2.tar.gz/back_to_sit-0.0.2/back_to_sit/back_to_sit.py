import telegram
import asyncio
import time 

async def __send_telegram_message(message, chat_id, token):
    # Set up the bot
    bot = telegram.Bot(token=token)

    # Send a message
    await bot.send_message(chat_id=chat_id, text=message)


def back_to_sit(message):
    """
    Function that send message when is called
    """
    # Create an event loop
    loop = asyncio.new_event_loop()
    # Run the coroutine in the event loop
    loop.run_until_complete(__send_telegram_message(message))

def back_to_sit_decorator(func, base_message):
    """
    Decorator that send a message when the function is done
    and report the time taken to execute the function
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        NEW_MESSAGE = base_message + f"\n Time taken to execute {func.__name__}: {end_time - start_time:.6f} seconds"
        back_to_sit(message=NEW_MESSAGE)
        return result
    return wrapper
