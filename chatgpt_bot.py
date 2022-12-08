import telebot
import os
import openai

API_TOKEN = '' # Telegram bot token

bot = telebot.TeleBot(API_TOKEN)
openai.api_key = '' # OpenAI token

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am ChatGPT bot.
Telegram Bot made By Mohammed BADI
The Bot will stop when my account reach limits
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    response = openai.Completion.create(model="text-davinci-003", prompt=message.text, temperature=0 ,max_tokens=2048)
    print(response)
    bot.reply_to(message,response["choices"][0]["text"] )


bot.infinity_polling()
