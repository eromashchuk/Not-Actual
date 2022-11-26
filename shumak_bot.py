import telebot as t

bot = t.TeleBot("5965925224:AAGMt8OXPfzf-QXcNF8ML_DUWscWjmW15nc")

@bot.message_handler(commands=['start', 'help', 'menu'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome! {message.chat.username}")

@bot.message_handler(content_types=['photo'])
def say_lmao(message: t.types.Message):
    bot.reply_to(message, 'Nice meme XDD')

bot.polling(none_stop=True)