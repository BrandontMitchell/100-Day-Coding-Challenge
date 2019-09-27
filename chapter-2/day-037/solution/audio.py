# import like some audio library and do some audio manipulation

# pip install pyttsx
# users will need:
#   ftplib
#   io
#   pandas
#   requests
#   requests_html

import pyttsx3
from yahoo_fin import stock_info as si
import requests, json

class HomeAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.test()
        self.show_settings()
        self.main()
    
    def show_settings(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            print("Voice:")
            print(f' - ID: {voice.id}')
            print(f' - Name: {voice.name}')
            print(f' - Languages: {voice.languages}')
            print(f' - Age: {voice.age}')

    def test(self):
        self.engine.say('Hello Mister Mitchell')
        self.engine.runAndWait()

    def btc_price(self):
        top = si.get_top_crypto()
        btc = top['Symbol'][0]
        price = top['Price (Intraday)'][0]
        self.engine.say("The current price of Bitcoin is " + str(price))
        self.engine.runAndWait()

    def weather(self, cityName):
        API_KEY = ''
        base_URL = 'http://api.openweathermap.org/data/2.5/weather?'
        final_URL = base_URL + "q=" + cityName + "&appid=" + API_KEY
        resp = requests.get(final_URL)
        data = json.loads(resp.content)
        temp = data['main']['temp']
        self.engine.say("The temperature in " + cityName + " is " + str(temp) + " degrees Kelvin")
        self.engine.runAndWait()

    def stock_index(self, stock):
        price = si.get_live_price(stock)
        self.engine.say("The current price for " + stock + " is " + str(price) + " dollars")
        self.engine.runAndWait()

    def change_voice(self, rate=125, volume=1.0, voiceIndex=0):
        # RATE
        self.engine.setProperty('rate', rate)
        self.engine.say("Testing in 125 rate")
        self.engine.runAndWait()
        self.engine.setProperty('rate', rate*2)
        self.engine.say("Testing in 250 rate")
        self.engine.runAndWait()

        # VOLUME
        self.engine.setProperty('volume', volume)
        self.engine.say("Testing at max volume")
        self.engine.runAndWait()
        self.engine.setProperty('volume', volume/2)
        self.engine.say("testing at half volume")
        self.engine.runAndWait()

        # VOICE
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        self.engine.say("Testing at index 0")
        self.engine.runAndWait()

        self.engine.setProperty('voice', voices[1].id)
        self.engine.say("Testing at index 1")
        self.engine.runAndWait()

    def main(self):
        self.weather("Seattle")
        self.stock_index("amzn")
        self.stock_index("aapl")
        self.btc_price()
        self.change_voice()

if __name__ == '__main__':
    bot = HomeAssistant()