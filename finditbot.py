import telebot
from telebot import types

bot = telebot.TeleBot("ВАШ токен")


@bot.message_handler(commands=["start"])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🔍Нашел вещь")
    item2 = types.KeyboardButton("🛅Потерял вещь")  # КНОПОЧКИ
    item3 = types.KeyboardButton("📢Объявления")
    item4 = types.KeyboardButton("💫Поддержи нас")
    item5 = types.KeyboardButton("✍️Обратная связь")
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(
        message.chat.id, f"Привет, {message.from_user.first_name}", reply_markup=markup
    )
    bot.register_next_step_handler(message, on_click)

@bot.message_handler(content_types=['text'])
def on_click(message):  # ТУТ ОБРАБОТКА ПРИ НАЖАТИИ КНОПОК
    if message.text == "🔍Нашел вещь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        markup.add(back)
        bot.send_message(
            message.chat.id, "Заполни, пожалуйста, эту форму, и скоро найденная вещь появится в списке объявлений😉: https://forms.gle/6eSTe5tGEKmmRDx28 ",reply_markup=markup
        )

    elif message.text == "🛅Потерял вещь":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        markup.add(back)
        bot.send_message(
            message.chat.id, "Заполни, пожалуйста, эту форму, и скоро потерянная вещь появится в списке объявлений😶: https://forms.gle/v7mMaoeTtEpoXk6x9 ", reply_markup=markup
        )

    elif message.text == "📢Объявления":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        founded = types.KeyboardButton("🔍Найденные вещи")
        losted = types.KeyboardButton("🛅Потерянные вещи")
        markup.add(founded, losted, back)
        bot.send_message(message.chat.id, "Выбери список, какой бы ты хотел посмотреть, потерянных или найденных вещей?", reply_markup=markup)

    elif message.text == "🔍Найденные вещи":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        markup.add(back)
        bot.send_message(message.chat.id, "Держи ссылку на все найденные вещи: https://finditfounded.spread.name/ ", reply_markup=markup)

    elif message.text == "🛅Потерянные вещи":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        markup.add(back)
        bot.send_message(message.chat.id, "Держи ссылку на все потерянные вещи: https://finditlosted.spread.name/  ", reply_markup=markup)

    elif message.text == "💫Поддержи нас":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        vk = types.KeyboardButton("💸Через VK")
        website=types.KeyboardButton("🌐Через вебсайт")
        markup.add(vk,website,back)
        bot.send_message(message.chat.id, "Выбери, как ты хочешь поддержать нас:", reply_markup=markup)

    elif message.text == "💸Через VK":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        markup.add(back)
        bot.send_message(message.chat.id, "Ссылка на VK Донат: https://vk.com/finditservice?source=description&w=donut_payment-223292894 ", reply_markup=markup)

    elif message.text == "🌐Через вебсайт":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        markup.add(back)
        bot.send_message(message.chat.id, "Пока работаем над этим способом, позже появится😎", reply_markup=markup)

    elif message.text == "✍️Обратная связь":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back = types.KeyboardButton("⬅️Назад")
        markup.add(back)
        bot.send_message(message.chat.id, "Было очень классно, если бы мы получили от тебя обратную связь. Это помогает нам двигаться дальше и улучшать наш проект. Поэтому заполни, пожалуйста, эту форму: https://forms.gle/TNYYEKmcYV8dvHfs9", reply_markup=markup)

    elif message.text == "⬅️Назад":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("🔍Нашел вещь")
        item2 = types.KeyboardButton("🛅Потерял вещь")  # КНОПОЧКИ
        item3 = types.KeyboardButton("📢Объявления")
        item4 = types.KeyboardButton("💫Поддержи нас")
        item5 = types.KeyboardButton("✍️Обратная связь")
        markup.add(item1, item2, item3, item4, item5)

        bot.send_message(
            message.chat.id,
            f"Выбери нужное меню🧑‍💻",
            reply_markup=markup)


def text_profile(message):
    message_to_save = message.text
    print(message_to_save)

bot.set_webhook()
bot.polling(non_stop=True, interval=0)
