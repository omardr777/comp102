import tkinter as tk
from components.Checkbox import CheckBox
from components.Textbox import TextBox
from components.label import CustomLabel
from components.Button import Button

import pandas as pd

class LastPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # You can display the components of page3 here 
        label = tk.Label(self, text="Page 3")
        label.pack(pady=10, padx=10)

        self.selected_cities_var = tk.StringVar(value=self.controller.selected_cities.get())

        def update_selected_cities(*args):
            self.selected_cities_var.set(self.controller.selected_cities.get())
            self.update_selected_cities_labels()

        self.controller.selected_cities.trace("w", update_selected_cities)

       
        self.selected_cities_labels = []
        self.selected_city_infos = []
        button = Button(self, text="Go back", command=self.back_button)
        button.pack()


    def update_selected_cities_labels(self):
        for label in self.selected_cities_labels:
            label.destroy()
        self.selected_cities_labels.clear()

        selected_cities = self.selected_cities_var.get().split(',')[1:]

        for city in selected_cities:
            selected_cities_label = Button(self, text=city,command = lambda city=city: self.display_city_info(city))
            selected_cities_label.pack()
            self.selected_cities_labels.append(selected_cities_label)
    
    def display_city_info(self,city_name):
        print(city_name)
        city_info = self.controller.fetch_city_data(city_name)
        for item in self.selected_city_infos:
            item.destroy()
        self.selected_city_infos.clear()
        for key,val in city_info.items():
            city_info_label = CustomLabel(self, text=val)
            city_info_label.configure(font=(city_info_label.cget('font').split()[0],10,'bold'))
            city_info_label.pack()
            self.selected_city_infos.append(city_info_label)
    
    def back_button(self):
        self.controller.get_page('SecondPage')
        for item in self.selected_city_infos:
            item.destroy()
        self.selected_city_infos.clear()
