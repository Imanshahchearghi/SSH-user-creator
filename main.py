import telebot
import subprocess
import random
import string

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
token = 'YOUR_BOT_TOKEN'

# Initialize the Telegram bot
bot = telebot.TeleBot(token)

# Variable to keep track of the user count
user_count = 8500
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Bot started. Use the /create_user command to create a new SSH user.")

@bot.message_handler(commands=['create_user'])
def create_user(message):
    # Check if the message comes from the authorized user (replace "ChatID"with your chat ID)
    if message.chat.id != "ChatID" :
        return

    # Increment the user count and generate the username
    global user_count
    user_count += 1
    username = "user" + str(user_count)

    # Generate a random password
    password = generate_random_password()

    # Create the SSH user with the generated username and password
    create_ssh_user(username, password)

    # Send the username and password to the user
    response = f"{username}: {password}"
    bot.reply_to(message, response)

def generate_random_password():
    # Generate a random 6-digit numeric password
    password = ''.join(random.choices(string.digits, k=6))
    return password

def create_ssh_user(username, password):
    # Use the subprocess module to execute the useradd command
    command = f'useradd -s /usr/sbin/nologin {username}'
    subprocess.run(command.split())

    # Set the generated password for the user
    command = f'echo "{username}:{password}" | chpasswd'
    subprocess.run(command, shell=True)

# Start the bot
bot.polling()
