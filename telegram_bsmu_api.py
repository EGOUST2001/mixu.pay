import telebot

token = '5275738464:AAGX9RJHq68NxiWqYTGkaqEueRHivNKUYNg'

bot = telebot.TeleBot(token)


def text_answer(message):
    bot.send_message(435577667, message)


if __name__ == "__main__":
    text_answer("text")

