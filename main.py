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
    
@bot.message_handler(func=lambda message: bot.user_state.get((message.chat.id, message.from_user.id)) == 'playing')
def handle_choice(message):
    # This function is triggered when the user sends a message while in the "playing" state

    # Generate the bot's choice randomly
    choices = ['rock', 'paper', 'scissors']
    bot_choice = random.choice(choices)

    # Compare the user's choice with the bot's choice and determine the winner
    user_choice = message.text.lower()
    if user_choice not in choices:
        bot.send_message(message.chat.id, 'Invalid choice. Please enter "rock", "paper", or "scissors".')
    elif user_choice == bot_choice:
        bot.send_message(message.chat.id, f'We both chose {user_choice}. It\'s a tie!')
    elif (user_choice == 'rock' and bot_choice == 'scissors') or (user_choice == 'paper' and bot_choice == 'rock') or (user_choice == 'scissors' and bot_choice == 'paper'):
        bot.send_message(message.chat.id, f'You win! You chose {user_choice}, and I chose {bot_choice}.')
    else:
        bot.send_message(message.chat.id, f'I win! You chose {user_choice}, and I chose {bot_choice}.')
