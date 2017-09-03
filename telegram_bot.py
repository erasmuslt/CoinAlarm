import sys
import time
import telepot
from parsingprice import CoinPriceScheduler
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg) #extract core data from msg
    choices = list(['coin price','market cap']) # make choice list for using inline key board button
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                 list(map(lambda c: InlineKeyboardButton(text=str(c), callback_data=str(c)), choices))
               ])

    bot.sendMessage(chat_id, 'Choose What you want', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')
    atext = 'you chosed %s' %query_data
    if(query_data=='coin price'):
        coin_price = CoinPriceScheduler()
        atext = 'Neo\'s price is %s BTC' % coin_price.Load_Price()
        bot.sendMessage(from_id, text=atext)
    elif(query_data=='market cap'):
        marketobject = CoinPriceScheduler()
        atext = 'Total Market Cap is %s USD' % marketobject.Load_TotalMarketCap()
        bot.sendMessage(from_id, text=atext)
    

TOKEN ='INPUT YOUR BOT API TOKEN'

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')

while 1:
    time.sleep(10)