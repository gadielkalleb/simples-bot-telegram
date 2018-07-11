import sys
import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop

def handle(msg):
  pprint(msg)
  if msg['text'] == 'ola':
    bot.sendMessage(msg['from']['id'], 'ola tudo bem')

TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print 'escutando'

while 1:
  time.sleep(10)