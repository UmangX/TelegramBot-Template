import requests
from requests.api import request
from telegram import *
from telegram.ext import *
from random import randrange


bot = Bot("Your Telegram Api")

pictures = ("https://photos.app.goo.gl/49xpGxEKVAQBGEA7A","https://photos.app.goo.gl/EQRdTZAWk71F5UXU9","https://photos.app.goo.gl/CGDT9yojjRzot6Hb8","https://photos.app.goo.gl/c1U4ofczKu6Ag3NVA","https://photos.app.goo.gl/UjzBFUGiDRA9wb9c8")

def quotess(update:Update,context:CallbackContext):
    data = requests.get("https://goquotes-api.herokuapp.com/api/v1/random?count=1")
    data = data.json()
    data = data["quotes"]
    data = data[0]
    bot.send_message(
        chat_id = update.effective_chat.id,
        text =data["text"])

def test1_function(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text ="Hello")

def pic(update:Update,context:CallbackContext):
    bot.send_photo(chat_id = update.effective_chat.id,photo = pictures[randrange(0,4)])
    

def whatcanudo(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text="Currently nothing But /howulook /randomimage /quote "
    )

def gettime(update:Update,context:CallbackContext):
    bot.send_message(
        char_id = update.effective_chat.id,
        text="Running Since"
    )

def startup(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text="I am the shadow of umang (May be) and this is a Telegram bot type /whatcanudo for Commands"
    )

def randomimages(update:Update,context:CallbackContext):
    newdata = requests.get("https://yesno.wtf/api")
    newdata = newdata.json()
    newdata_link = newdata["image"]
    bot.send_photo(
        chat_id = update.effective_chat.id,
        photo = newdata_link

    )





def main():    
    bot = Bot("Your Telegram Api")
    updater = Updater("Your Telegram Api",use_context=True)
    dispatcher = updater.dispatcher
    hellomsg = CommandHandler("hello",test1_function)
    sendmypic = CommandHandler("howulook",pic)
    startups = CommandHandler("start",startup)
    liss = CommandHandler("whatcanudo",whatcanudo)
    runsince = CommandHandler("runtime",gettime)
    randomimg = CommandHandler("randomimage",randomimages)
    quotesss = CommandHandler("quote",quotess)
    dispatcher.add_handler(quotesss)
    dispatcher.add_handler(runsince)
    dispatcher.add_handler(randomimg)
    dispatcher.add_handler(liss)
    dispatcher.add_handler(startups)
    dispatcher.add_handler(sendmypic)
    dispatcher.add_handler(hellomsg)
    updater.start_polling()



try:    
    print("Bot has Started")
    main()
except KeyboardInterrupt:
    print("Bot Is Going To Sleep")     
    