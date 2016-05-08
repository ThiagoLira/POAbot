#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to troll people
# This program is dedicated to the public domain under the CC0 license.



from telegram.ext import Updater, CommandHandler, MessageHandler , Filters
import logging
import datetime
import random

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)


f = open('errorlog.txt', 'r+')






palavraovec = ["idiota","burro","imbecil","caralho","puta merda","porra","cacete","filho da puta","fdp","tomar no seu cu","merda","vai se fuder", "no cu","cala a boca"]
higaVec = ["4Qual a necessidade disso champs?","oloko","pra que isso?","apenas sou atacado nesse grupo","oloooooko","oloooooooooooko","palavras asperas meu colega"]


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Eae negada, quando mato uma fada estou só começando')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Vou te ajudar é o caralho seu porra (/oi pra eu te xingar e /horas pra eu te xingar)')



def oi(bot,update):
    bot.sendMessage(update.message.chat_id,text=("Vai tomar no seu cu, "+update.message.from_user.first_name))

def behavior(bot,update): #bullying com ultima pessoa que falou

    message = update.message.text.lower()
    name = update.message.from_user.first_name
    if(message.find("poabot")!= -1 ):
        if( message.find("qual a sua opini")!= -1 ):
            bot.sendMessage(update.message.chat_id,text="Tenho uma opiniao bem forte sobre isso: Foda-se.")
        elif (message.find("que voce ach")!= -1 or message.find("que você ach")!= -1 or message.find("que vc ach")!= -1 or message.find("que que voce ach")!= -1 or message.find("que que você ach")!= -1):
            bot.sendMessage(update.message.chat_id,text="Acho que voce deveria ir tomar no cu.")
        else:
            for palavraFeia in palavraovec:
                if (message.find(palavraFeia)!=-1):
                    bot.sendMessage(update.message.chat_id,text=random.choice(higaVec))
                    bot.sendMessage(update.message.chat_id,text=".")


    if(message.find("bom dia")!= -1 or message.find("boa tarde")!= -1 or message.find("boa noite")!= -1):
        bot.sendMessage(update.message.chat_id,text="AHHHH NAOOO VAI A MERDAAAAAAA")




def horas(bot,update):
    bot.sendMessage(update.message.chat_id,text="Sao "+datetime.datetime.now().strftime('%H:%M:%S')+" , seu gay.")

def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("197733089:AAFiDSh-n0-OHffZkrAd1qH2nZsMWDtymvY")


    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addHandler(CommandHandler("start", start))
    dp.addHandler(CommandHandler("help", help))
    dp.addHandler(CommandHandler("oi",oi))
    dp.addHandler(CommandHandler("horas",horas))
    # on noncommand i.e message - echo the message on Telegram


    dp.addHandler(MessageHandler([Filters.text], behavior))


    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
