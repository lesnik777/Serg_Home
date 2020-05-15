import pyowm
import telebot

# from colorama import init
# from colorama import Fore, Back, Style

# init()
# print(Back. GREEN)
# print(Fore.WHITE)
# print (Style.BRIGHT)

owm = pyowm.OWM('889bc327f1120a7d3401cd92f5ca5695',language = "ua")
bot = telebot.TeleBot("1083567007:AAHkGacdQc9WiFGCIcWkO8ITn34sVGbo2zM")

#print(Back. GREEN)
#place = input("Введіть місто/країну: ")
@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    
    # print(Back. RED)
    answer ="В місті "  +  message.text  +  " зараз "  +  w.get_detailed_status()+"\n"                 
    answer +="Температура в районі " +  str(temp) + " грд " + "\n"

    # print(Back.WHITE)
    # print(Fore.BLACK)
    if temp < 1:
        answer += (" Зараз дуже холодно, вдягайся більше")
    elif temp < 20:
        answer += (" Зараз прохолодно, вдягнися")
    else:
        answer += (" Температура норм")
    
    bot.send_message(message.chat.id,answer)    
bot.polling( none_stop = True )