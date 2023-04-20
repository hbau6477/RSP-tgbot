import telebot
import random

bot_token = 'YOUR_TELEGRAM_BOT_TOKEN_HERE'

bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    # This function is triggered when the user sends the command "/start"

    # Send a welcome message and instructions to the user
    bot.send_message(message.chat.id, 'Welcome to Rock-Paper-Scissors! Please type /play to start a new game.')

@bot.message_handler(commands=['play'])
def handle_play(message):
    # This function is triggered when the user sends the command "/play"

    # Send the game instructions to the user
    bot.send_message(message.chat.id, 'Enter "rock", "paper", or "scissors" to play.')

    # Set the user's state to playing
    bot.user_state[(message.chat.id, message.from_user.id)] = 'playing'
