import tkinter as tk
from pages.FirstPage import FirstPage
from pages.SecondPage import SecondPage
from pages.LastPage import LastPage
import pandas as pd

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.container = tk.Frame()
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.pack(fill='both', expand=True)

        self.user = {}
        self.pages = {}
        self.selected_cities = tk.StringVar()
        self.df = pd.read_csv('data2.csv')

        for p in (FirstPage, SecondPage, LastPage):
            page_name = p.__name__
            frame = p(parent=self.container, controller=self)
            self.pages[page_name] = frame
            frame.grid(row=0, column=0, sticky='nesw')
        
        self.get_page('FirstPage')

    def get_page(self, page_name):
        page = self.pages[page_name]
        page.tkraise()

    def set_user(self, name, nationality, age):
        self.user['name'] = name
        self.user['nationality'] = nationality
        self.user['age'] = age

    def toggle_cities(self, city_name):
        cities = self.selected_cities.get().split(",")
        if city_name in cities:
            cities.remove(city_name)
        else:
            cities.append(city_name)
        self.selected_cities.set(",".join(cities))
        print(self.selected_cities.get())

    def get_selected_cities(self):
        return self.selected_cities.get()
    
    def fetch_city_data(self,city_name):
        df = self.df
        city_data = df[df['city'] == city_name]
        return city_data.iloc[0].to_dict()

if __name__ == '__main__':
    app = MainWindow()
    app.geometry('1920x1080')
    app.mainloop()
