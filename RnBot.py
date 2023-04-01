import telebot
from telebot.types import ReplyKeyboardMarkup
from threading import Timer
from threading import Thread
import zmq
import time
import json
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:1178")

def startBot(token,channel_id=0,buttons={}):
    bot = telebot.TeleBot(token)
    print(channel_id)

    def listener ():
        while True:
            message = socket.recv()
            print(message)
            nonlocal buttons
            data = json.loads(message)
            buttons=data
            time.sleep(1)
            socket.send_string("done")

    def do ():
        print(1)
        bot.send_message(channel_id,"scedule does")
        timer=Timer(3600.0, lambda: do())
        timer.start()


    t1 = Thread(target=listener)
    t1.start()


    if(channel_id) :
        print(1)
        timer=Timer(3600.0, lambda: do())
        timer.start()


    keys=list(buttons.keys())
    markup=ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).row(*keys)



    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id,'start working',reply_markup=markup)
    



    @bot.message_handler()
    def give_response(message):
        if buttons.get(message.text) :
            bot.send_message(message.chat.id,buttons[message.text])
    



    bot.infinity_polling()

# def startScedule(token,channel_id):
#     bot = telebot.TeleBot(token)
#     def do ():
#         bot.send_message(channel_id,"scedule does")

#     schedule.every().hour.do(do)

#     # bot.infinity_polling()
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# def main(**args) :
#     # if args.get('channel_id') :
#     #     startScedule(bot=bot,channel_id=args['channel_id'])
#     # startBot(**args,bot=bot)
#     if args.get('channel_id') :
#         p1 = multiprocessing.Process(target=startScedule,args=(args['token'],args['channel_id']))

#     p2 = multiprocessing.Process(target=startBot,args=(args['token'],args['buttons']))

#     p2.start()

#     if args.get('channel_id') :
#         p1.start()

#     p2.join()

#     if args.get('channel_id') :
#         p1.join()


