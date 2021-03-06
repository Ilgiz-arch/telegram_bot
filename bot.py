# Импортируем необходимые компоненты
from telegram.ext import Updater,  CommandHandler, MessageHandler, Filters
from settings import TG_TOKEN, TG_API_URL
from handlers import *


# Создадим (объявляем) функцию main, которая соединяется с платформой Telegram
def main():
    # тело функции, описываем функцию
    # создадим переменную my_bot, с помощью которой будем взаимодействовать с нашим ботом
    my_bot = Updater(TG_TOKEN , TG_API_URL, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms)) # обработчик команды start
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Картинки'), send_meme))
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Начать'), sms)) # обрабатываем текст кнопки
    my_bot.dispatcher.add_handler(MessageHandler(Filters.regex('Анекдот'), get_anecdote)) # обрабатываем текст кнопки
    my_bot.dispatcher.add_handler(MessageHandler(Filters.contact, get_contact)) # обработчик полученного контакта
    my_bot.dispatcher.add_handler(MessageHandler(Filters.location, get_location)) # обработчик полученной геопозиции
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot)) # обработчик текстового сообщения
    my_bot.start_polling() # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle() # бот будет работать пока его не остановят


# Вызваем (запускаем) функцию main
if __name__ == '__main__':
    main()