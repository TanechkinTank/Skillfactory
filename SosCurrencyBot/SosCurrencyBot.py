import telebot
from extensions import ConvertionExeption, CurrencyConverter
from config import keys, TOKEN


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Привет, {message.chat.username}! "
f"\nЯ — бот-конвертер валют."
f"\nЧтобы начать работу, введи: <имя валюты, которую переводим> <имя валюты, в которую переводим> <сумма>."
f"\nДля дробных чисел в качестве разделителя используй точку."
f"\nЧтобы увидеть список доступных валют, введи команду /values")


@bot.message_handler(commands=["values"])
def values(message: telebot.types.Message):
    text = "Доступные валюты:"
    for key in keys.keys():
        text = "\n".join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=["text", ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")

        if len(values) != 3:
            raise ConvertionExeption("Введены лишние символы")

        quote, base, amount = values
        total_base = CurrencyConverter.get_price(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Цена {amount} {quote} в {base} — {total_base}"
        bot.send_message(message.chat.id, text)


bot.polling(none_stop=True)