
from  chatterbot import ChatBot #chatterbot class

from chatterbot.trainers import ListTrainer # training the machine automatically
import os

bot = ChatBot('Bot')
bot.set_trainer(ListTrainer)

for files in os.listdir('folders of ur directory which having datasets'):
       data = open('folders of ur directory which having datasets' + files,'r').readlines()
       bot.train(data)   # training the bot by the datasets

while True:
    message = raw_input('you:')
    if message.strip() !='bye':
        reply = bot.get_response(message) # responce from the machine 
        print('machine1:',reply)
        #print(type(reply))

    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break
