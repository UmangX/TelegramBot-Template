import requests
import time
from telegram import *
from telegram.ext import *
from random import randrange


def getusername(update, context):
    print(update.message.from_user['username'])



Startup_time = time.asctime((time.localtime(time.time())))

bot = Bot("Your API Key")

pictures = ("https://photos.app.goo.gl/49xpGxEKVAQBGEA7A","https://photos.app.goo.gl/EQRdTZAWk71F5UXU9","https://photos.app.goo.gl/CGDT9yojjRzot6Hb8","https://photos.app.goo.gl/c1U4ofczKu6Ag3NVA","https://photos.app.goo.gl/UjzBFUGiDRA9wb9c8")

def quotess(update:Update,context:CallbackContext):
    print("Command Executed") 
    data = requests.get("https://goquotes-api.herokuapp.com/api/v1/random?count=1")
    data = data.json()
    data = data["quotes"]
    data = data[0]
    bot.send_message(
        chat_id = update.effective_chat.id,
        text =data["text"])

def test1_function(update:Update,context:CallbackContext):
    print("Command Executed") 
    bot.send_message(
        chat_id = update.effective_chat.id,
        text ="Hello")

def pic(update:Update,context:CallbackContext):
    bot.send_photo(chat_id = update.effective_chat.id,photo = pictures[randrange(0,4)])
    print("Command Executed") 
    

def whatcanudo(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text="Currently nothing But /howulook /randomimage /quote /hello /runningsince "
    )
    print("Command Executed") 




def startup(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text="I am the shadow of umang (May be) and this is a Telegram bot type /whatcanudo for Commands"
    )
    print("Command Executed") 


def randomimages(update:Update,context:CallbackContext):
    newdata = requests.get("https://yesno.wtf/api")
    newdata = newdata.json()
    newdata_link = newdata["image"]
    bot.send_photo(
        chat_id = update.effective_chat.id,
        photo = newdata_link

    )
    print("Command Executed") 



def runsince(update:Update,context:CallbackContext):
    bot.send_message(
        chat_id = update.effective_chat.id,
        text=Startup_time

    )
    print("Command Executed") 




def main():    
    bot = Bot("Your API Key")
    updater = Updater("Your API Key",use_context=True)
    dispatcher = updater.dispatcher
    hellomsg = CommandHandler("hello",test1_function)
    sendmypic = CommandHandler("howulook",pic)
    startups = CommandHandler("start",startup)
    liss = CommandHandler("whatcanudo",whatcanudo)
    randomimg = CommandHandler("randomimage",randomimages)
    quotesss = CommandHandler("quote",quotess)
    runsinnce = CommandHandler("runningsince",runsince)
    dispatcher.add_handler(runsinnce)
    dispatcher.add_handler(quotesss)
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
    
