import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

API_TOKEN = '5368271136:AAE0ebJRkeJh_LqOl1oQDIdnkSp8TJYiIxU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hola, con este bot podrás enviar mensajes a usuarios de WhatsApp sin necesidad de tenerlos guardados como contacto. \n \n Ingresa un número con su respectivo codigo de área para empezar:")



@dp.message_handler()

async def numero(message: types.Message):
  
    if type(message.text) == str :

      await message.reply(f"Usa el siguiente enlace para enviar un mensaje directo al número {message.text}: \n \nhttps://api.whatsapp.com/send/?phone={message.text}")
   
    else: 
      await message.reply("Ingresa un número de para continuar")

