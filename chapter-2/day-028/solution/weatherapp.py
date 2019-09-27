import requests
from tkinter import *
import json
from datetime import datetime
import time

# https://openweathermap.org/api
class WeatherApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Live Weather App")
        self.master.geometry('500x400')
        self.API_KEY = ''
        self.base_URL = 'http://api.openweathermap.org/data/2.5/weather?'
        self.init_UI()
        self.master.mainloop()
        

    def init_UI(self):
        self.logo = Label(self.master, text="Weather App 1.0")
        self.city = Text(self.master, width=15, height=2, bg='lightblue', fg='black')
        self.zip = Text(self.master, width=15, height=2, bg='lightblue', fg='black')
        self.cityButton = Button(self.master, text="Search by City (city, state)", width=25, height=2, command=self.get_city_data)
        self.zipButton = Button(self.master, text="Search by ZIP Code", width=25, height=2, command=self.get_zip_data)

        # place on top of screen
        self.logo.place(x=200, y=20)
        self.city.place(x=105, y=100)
        self.zip.place(x=105, y=150)
        self.cityButton.place(x=250, y=100)
        self.zipButton.place(x=250, y=150)

        # after request has been made, this will be updated
        self.tempText = StringVar()
        self.temp = Label(self.master, textvariable=self.tempText)
        self.tempText.set("Temperature: ")

        self.humidityText = StringVar()
        self.humidity = Label(self.master, textvariable=self.humidityText)
        self.humidityText.set("Humidity: ")

        self.windText = StringVar()
        self.wind = Label(self.master, textvariable=self.windText)
        self.windText.set("Wind Speed: ")

        self.descriptionText = StringVar()
        self.description = Label(self.master, textvariable=self.descriptionText)
        self.descriptionText.set("Overview: ")

        self.sunsetText = StringVar()
        self.sunset = Label(self.master, textvariable=self.sunsetText)
        self.sunsetText.set("Sunset At: ")


        # place on bottom of screen
        self.temp.place(x=105, y=300)
        self.humidity.place(x=105, y=320)
        self.wind.place(x=250, y=300)
        self.description.place(x=200, y=340)
        self.sunset.place(x=250, y=320)

    def get_city_data(self):
        self.city_url = f'{self.base_URL}q={self.city.get("1.0", END)}&appid={self.API_KEY}'
        resp = requests.get(self.city_url)
        data = json.loads(resp.content)
        sunset = int(data['sys']['sunset'])

        data_dict = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'sunset': self.utc_to_local(sunset)
        }
        self.update_ui(data_dict)
    
    def get_zip_data(self):
        self.zip_url = f'{self.base_URL}zip={self.zip.get("1.0", END)}&appid={self.API_KEY}'
        resp = requests.get(self.zip_url)
        data = resp.content
        data_dict = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'description': data['weather'][0]['description'],
            'sunset': self.utc_to_local(sunset)
        }
        self.update_ui(data_dict)
        

    def update_ui(self, data):
        self.tempText.set("Temperature: " + str(data['temperature']) + " K")
        self.humidityText.set("Humidity: " + str(data['humidity']) + "%")
        self.windText.set("Wind Speed: " + str(data['wind']))
        self.descriptionText.set("Overview: " + data['description'])
        self.sunsetText.set("Sunset At: " + str(data['sunset']))


    # helper methods
    def utc_to_local(self, utc_datetime):
        timestamp = utc_datetime
        date_time = datetime.fromtimestamp(timestamp)
        return date_time



if __name__ == '__main__':
    root = Tk()
    app = WeatherApp(root)