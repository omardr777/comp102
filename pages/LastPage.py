import tkinter as tk
from components.Checkbox import CheckBox
from components.Textbox import TextBox
from components.label import CustomLabel
from components.Button import Button
from components.ImageLabel import ImageLabel

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
            self.show_selected_cities_buttons()
        self.controller.selected_cities.trace("w", update_selected_cities)

        self.selected_cities_buttons = []
        self.selected_city_infos = []

        # main frame(2,1)
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=5)
        self.grid_rowconfigure(1,weight=1)
        self['bg'] = '#b9bace'

        #Frame of row 0, (2,1)
        self.detail_grid = tk.Frame(self)
        self.detail_grid.grid(row=0,column=0,sticky='news')
        self.detail_grid.grid_columnconfigure(0,weight=1)
        self.detail_grid.grid_columnconfigure(1,weight=14)
        self.detail_grid.grid_rowconfigure(0,weight=1)

        # Buttons frame (9,3)
        self.buttons_frame = tk.Frame(self.detail_grid)
        self.buttons_frame.grid(row=0,column=0,sticky='nsew')
        self.buttons_frame['bg'] = '#b9bace'
        self.config_grid(self.buttons_frame,9,3)

        # city information frame(5,3)
        self.info_frame = tk.Frame(self.detail_grid)
        self.info_frame.grid_columnconfigure(0,weight=1)
        self.info_frame.grid_columnconfigure(1,weight=1)
        self.info_frame.grid_columnconfigure(2,weight=1)
        self.info_frame.grid_rowconfigure(0,weight=1)
        self.info_frame.grid_rowconfigure(1,weight=1)
        self.info_frame.grid_rowconfigure(2,weight=1)
        self.info_frame.grid_rowconfigure(3,weight=1)
        self.info_frame.grid_rowconfigure(4,weight=1)
        #place at (0,1) of detail grid
        self.info_frame.grid(row=0,column=1,sticky='nswe')
        self.info_frame['bg'] = '#515486'

        back_button = Button(self, text="Go back", command=self.back_button)
        back_button.grid(row=1,column=0)


    def show_selected_cities_buttons(self):
        for label in self.selected_cities_buttons:
            label.destroy()
        self.selected_cities_buttons.clear()

        selected_cities = self.selected_cities_var.get().split(',')[1:]#',khobar,ryadh'-> ['','khobar','ryiadh']
        # here the cities buttons, temporarily will display buttons for each city the user has selected, it should be image buttons
        for i,city in enumerate(selected_cities):
            selected_cities_button = Button(self.buttons_frame, text=city,command = lambda city=city: self.display_city_info(city))
            selected_cities_button.grid(row=i,column=1,pady=10)
            self.selected_cities_buttons.append(selected_cities_button)
    
    def display_city_info(self, city_name):
        city_info = self.controller.fetch_city_data(city_name)
        # {'city':'Khobar'}
        labels = []
        rows = [
            ("City", city_info['city']),
            ("Description", city_info['description']),
            ("LandSight to visit", city_info['landSight']),
            ("LandSight description", city_info['sight1Description']),
            ("Another landSight", city_info['landSight2']),
            ("Second landSight description", city_info['sight2Description']),
            ("Hotel", city_info['hotel']),
            ("Hotel description", city_info['hotelDescription']),
            ("Another hotel", city_info['hotel2']),
            ("Second description", city_info['hotel2Description']),
        ]

        images = [
            ("City", city_info['cityImage']),
            ("LandSight to visit", city_info['landSightImage']),
            ("Another landSight", city_info['landSightImage2']),
            ("Hotel", city_info['hotelImage']),
            ("Another hotel", city_info['hotelImage2']),
        ]

#          (0,('city',value))
        for i, (row, data) in enumerate(rows):
            row_label = CustomLabel(self.info_frame, text=row,wraplength=300)
            row_label.grid(row=i, column=0, sticky='w',padx=30)
            row_label.set_font_size(10,'bold')
            labels.append(row_label)

            data_label = CustomLabel(self.info_frame, text=data,wraplength=1250)
            data_label.grid(row=i, column=1, sticky='wesn')
            data_label.set_font_size(10,'bold')
            data_label.set_bg_fg('#FCFCFC','#515486')
            labels.append(data_label)

            #                                              (0,('city','imagesrc'))
            images_src = next((image[1] for index, image in enumerate(images) if image[0] == row), None)

            if images_src:
                # f'Images/cities/{images_src}' == 'Images/cities/' + image_src
                image = ImageLabel(self.info_frame, f'Images/cities/{images_src}', width=100, height=100)
                image.grid(row=i, column=2)
                labels.append(image)

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
