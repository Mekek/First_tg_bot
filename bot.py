import telebot
import config

bot = telebot.TeleBot('1381840597:AAG85SWgFxygpJ8r6-s_lxxoO8b_FNZcJ8Y')

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_message(message.chat.id, message.text)

# run
bot.polling(none_stop=True)
