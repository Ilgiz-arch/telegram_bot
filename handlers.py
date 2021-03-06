from bs4 import BeautifulSoup
from  mongodb import  mdb, search_or_save_user, save_file_id, save_picture_name
from utility import get_keyboard
from telegram import  InlineKeyboardButton,InlineKeyboardMarkup
from  glob import  glob
from  random import choice
import requests

# Функция sms() будет вызвана пользователем при отправке команды start
# Внутри функции будет описана логика при ее вызове
def sms(bot, update):
    user = search_or_save_user(mdb, bot.effective_user, bot.message) # получаем данные из базы данных
    print(user)
    print('Кто-то отправил команду /start. Что мне делать?') # вывод сообщения в консоль при отправки команды /start
    bot.message.reply_text('Здравствуйте, {}! \nПоговорите со мной!'
                           .format(bot.message.chat.first_name), reply_markup=get_keyboard())

# Функция отправляет случайную картинку
def send_meme(bot, update):
    lists = glob('images/*') # создаем список из названий картинок
    picture = choice((lists)) # берем из списка одну картинку
    image = save_picture_name(mdb, picture)  # получаем из базы данных словарь

    msg = update.bot.send_photo(
        chat_id=bot.message.chat.id,
        photo=open(picture, 'rb'),
        )  # отправляем картинку и inline клавиатуру
    save_file_id(mdb, picture, msg)  #

def get_anecdote(bot, update):
    receive = requests.get('http://anekdotme.ru/random') # отправляем запрос к странице
    page = BeautifulSoup(receive.text, 'html.parser') # подключаем html парсер, получаем текст страницы
    find = page.select('.anekdot_text') # из страницы html  получаем class="anekdot_text"
    for text in find:
        page = (text.getText().strip()) # из class="anekdot_text" получаем текст и убираем пробелы по сторонам
    bot.message.reply_text(page) # отправляем один анекдот, последний



# Функция parrot() отвечает тем же сообщением , которое ему прислали
def parrot(bot, update):
    print(bot.message.text) # печатаем на экран
    bot.message.reply_text(bot.message.text) # отправляем обратно текст который пользователь послал

# Функция печатает и отвечает на полученный контакт
def get_contact(bot, update):
    print(bot.message.contact)
    bot.message.reply_text('{}, мы получили ваш номер телефона!'.format(bot.message.chat.first_name))

# Функция печатает и отвечает на полученные геоданные
def get_location(bot, update):
    print(bot.message.location)
    bot.message.reply_text('{}, мы получили ваше местоположение!'.format(bot.message.chat.first_name))

