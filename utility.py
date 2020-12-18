from telegram import  ReplyKeyboardMarkup, KeyboardButton



CALLBACK_BUTTON_START = "Начать 🎰"
CALLBACK_BUTTON_JOKE = "Анекдот 🎭"

# Функция создаёт клавиатуру и ее разметку
def get_keyboard():
    contact_button = KeyboardButton('Отправить контакты', request_contact=True)
    location_button = KeyboardButton('Отправить геопозицию', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([[CALLBACK_BUTTON_START, CALLBACK_BUTTON_JOKE], [contact_button, location_button],['Картинки']], resize_keyboard=True)
    return my_keyboard
