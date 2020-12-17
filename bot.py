# Импортируем необходимые компоненты
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from settings import TG_TOKEN, TG_API_URL

# Функция sms() будет вызвана пользователем при отправке команды start
# Внутри функции будет описана логика при ее вызове
def sms(bot, update):
    print('Кто-то отправил команду /start. Что мне делать?') # вывод сообщения в консоль при отправки команды /start
    bot.message.reply_text("Здравствуйте, я бот \nЯ пока не умею разговаривать, но я быстро учусь!".format(bot.message.chat.first_name)) # отправим ответ
    print(bot.message)

# Функция parrot() отвечает тем же сообщением , которое ему прислали
def parrot(bot, update):
    print(bot.message.text) # печатаем на экран
    bot.message.reply_text(bot.message.text) # отправляем обратно текст который пользователь послал

# Создадим (объявляем) функцию main, которая соединяется с платформой Telegram
def main():
    # тело функции, описываем функцию
    # создадим переменную my_bot, с помощью которой будем взаимодействовать с нашим ботом
    my_bot = Updater(TG_TOKEN , TG_API_URL, use_context=True)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms)) # обработчик команды start

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot)) # обработчик текстового сообщения

    my_bot.start_polling() # проверяет о наличии сообщений с платформы Telegram
    my_bot.idle() # бот будет работать пока его не остановят


# Вызваем (запускаем) функцию main
main()