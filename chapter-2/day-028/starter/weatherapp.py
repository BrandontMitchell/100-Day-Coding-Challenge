import requests
from tkinter import *
import json
from datetime import datetime
import time

# https://openweathermap.org/api
class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.API_KEY = 'YOUR_API_KEY'
        self.base_URL = 'http://api.openweathermap.org/data/2.5/weather?'
        self.master.mainloop()
        

    def init_UI(self):
        ''' create ui here with buttons and text fields'''
        pass

    def get_city_data(self):
       '''send request and organize data'''
    #    example: resp = requests.get(self.newURL)
       pass
    
    def get_zip_data(self):
        '''follow same template from get_city_data'''
        pass
        

    def update_ui(self, data):
        '''update the ui after request has been made'''


    # helper methods
    def utc_to_local(self, utc_datetime):
        timestamp = utc_datetime
        date_time = datetime.fromtimestamp(timestamp)
        return date_time


if __name__ == '__main__':
    root = Tk()
    app = WeatherApp(root)