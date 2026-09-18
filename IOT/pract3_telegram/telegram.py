import sys
import time
import random
import datetime

import telepot
import RPi.GPIO as GPIO

# LED functions
def on(pin):
    GPIO.output(pin, GPIO.HIGH)
    return

def off(pin):
    GPIO.output(pin, GPIO.LOW)
    return

# Use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# Set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'on':
        on(11)
        bot.sendMessage(chat_id, 'LED is ON')

    elif command == 'off':
        off(11)
        bot.sendMessage(chat_id, 'LED is OFF')


bot = telepot.Bot('Bot Token')
bot.message_loop(handle)

print('I am listening...')

while True:
    time.sleep(10)