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
        main_color = '#FCFCFC'
        self['bg'] = main_color
        self.selected_cities_var = tk.StringVar(value=self.controller.selected_cities.get())

        def update_selected_cities(*args):
            self.selected_cities_var.set(self.controller.selected_cities.get())
            self.update_selected_cities_labels()

        self.controller.selected_cities.trace("w", update_selected_cities)
        self.selected_cities_labels = []
        self.selected_city_infos = []

        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=5)
        self.grid_rowconfigure(1,weight=1)
        self['bg'] = '#b9bace'

        self.detail_grid = tk.Frame(self)
        self.detail_grid.grid(row=0,column=0,sticky='news')
        # self.detail_grid['bg'] = main_color
        self.detail_grid.grid_columnconfigure(0,weight=1)
        self.detail_grid.grid_columnconfigure(1,weight=14)
        self.detail_grid.grid_rowconfigure(0,weight=1)

        self.buttons_frame = tk.Frame(self.detail_grid)
        self.buttons_frame.grid(row=0,column=0,sticky='nsew')
        self.buttons_frame['bg'] = '#b9bace'
        self.config_grid(self.buttons_frame,10,3)

        self.info_frame = tk.Frame(self.detail_grid)
        self.info_frame.grid_columnconfigure(0,weight=1)
        self.info_frame.grid_columnconfigure(1,weight=1)
        self.info_frame.grid_columnconfigure(2,weight=1)
        self.info_frame.grid_rowconfigure(0,weight=1)
        self.info_frame.grid_rowconfigure(1,weight=1)
        self.info_frame.grid_rowconfigure(2,weight=1)
        self.info_frame.grid_rowconfigure(3,weight=1)
        self.info_frame.grid_rowconfigure(4,weight=1)
        self.info_frame.grid(row=0,column=1,sticky='nswe')
        self.info_frame['bg'] = '#515486'

        back_button = Button(self, text="Go back", command=self.back_button)
        back_button.grid(row=1,column=0)
        # back_button.pack()


    def update_selected_cities_labels(self):
        for label in self.selected_cities_labels:
            label.destroy()
        self.selected_cities_labels.clear()

        selected_cities = self.selected_cities_var.get().split(',')[1:]
        # here the cities buttons, temporarily will display buttons for each city the user has selected, it should be image buttons
        counter = 0
        for city in selected_cities:
            print(counter)
            selected_cities_button = Button(self.buttons_frame, text=city,command = lambda city=city: self.display_city_info(city))
            selected_cities_button.grid(row=counter,column=1,pady=10)
            self.selected_cities_labels.append(selected_cities_button)
            counter += 1
    
    def display_city_info(self, city_name):
        print(city_name)
        city_info = self.controller.fetch_city_data(city_name)
        print(city_info)

        # Clear any existing labels
        for label in self.selected_city_infos:
            label.destroy()

        labels = []
        rows = [
            ("City", city_info['city']),
            ("Description", city_info['description']),
            ("LandSight to visit", city_info['landSight']),
            ("Another landSight", city_info['landSight2']),
            ("LandSight description", city_info['sight1Description']),
            ("Second landSight description", city_info['sight2Description']),
            ("Hotel", city_info['hotel']),
            ("Another hotel", city_info['hotel2']),
            ("Hotel description", city_info['hotelDescription']),
            ("Second hotel description", city_info['hotel2Description'])
        ]

        for i, (row, data) in enumerate(rows):
            row_label = CustomLabel(self.info_frame, text=row,wraplength=300)
            row_label.grid(row=i, column=0, sticky='e')
            row_label.set_font_size(10,'bold')
            labels.append(row_label)

            data_label = CustomLabel(self.info_frame, text=data,wraplength=1250)
            data_label.grid(row=i, column=1, sticky='wesn')
            data_label.set_font_size(10,'')
            data_label.set_bg_fg('#FCFCFC','#515486')
            labels.append(data_label)

        # Clear any existing labels
        for label in self.selected_city_infos:
            label.destroy()

        self.selected_city_infos = labels



    
    def back_button(self):
        self.controller.get_page('SecondPage')
        for item in self.selected_city_infos:
            item.destroy()
        self.selected_city_infos.clear()

    def config_grid(self,container,rows,columns):
        for i in range(rows):
            container.grid_rowconfigure(i,weight=0)
        for i in range(columns):
            container.grid_columnconfigure(i,weight=1)
