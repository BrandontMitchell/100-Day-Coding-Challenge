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
        self.engine.say('Hello Hacker')
        self.engine.runAndWait()

    def btc_price(self):
        pass

    def weather(self, cityName):
        API_KEY = ''
        base_URL = 'http://api.openweathermap.org/data/2.5/weather?'
        final_URL = base_URL + "q=" + cityName + "&appid=" + API_KEY
        

    def stock_index(self, stock):
        pass

    def change_voice(self, rate=125, volume=1.0, voiceIndex=0):
        # RATE
        

        # VOLUME
        

        # VOICE
        pass
        

    def main(self):
        pass

if __name__ == '__main__':
    bot = HomeAssistant()