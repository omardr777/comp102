import tkinter as tk
from pages.FirstPage import FirstPage 
from pages.SecondPage import SecondPage
from pages.LastPage import LastPage


#dropdown list compontents
def card_componet(root,Lable_text,options,locationsx,locationy):

    #label text is for text that appears for the button
    clicked = tk.StringVar()
    clicked.set(Lable_text)

    #*options to show all the options to choose from
    dropDownMenu = tk.OptionMenu(root,clicked,*options,)

    #this is the config for the colors and fonts
    dropDownMenu.config(bg='blue',foreground='black',font='Raleway')

    #location x and y to choose where you want it
    dropDownMenu.place(x=locationsx,y=locationy)

class MainWindow(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)

        self.container = tk.Frame()
        self.container.grid(row=0,column=0,sticky='nesw')

        # self.user

        self.pages = {}
        for p in (FirstPage,SecondPage,LastPage):
            page_name = p.__name__
            frame = p(parent = self.container,controller = self)
            self.pages[page_name] = frame
            frame.grid(row=0,column=0,sticky='nesw')
        
        #start with FirstPage
        self.get_page('FirstPage')

    def get_page(self,page_name):
        page = self.pages[page_name]
        page.tkraise()

if __name__ == '__main__':
    app = MainWindow()
    
    # example 1 for card componts(please full screen to see them)
    # example for options, made them a variable so easily insert them
    options = ['1', '2', '3', '4']
    test = card_componet(app, 'click me', options, 100, 100)

    options2 = ['hadi', 'ali', 'ahmed', 'test']
    text2 = card_componet(app, "don't click me", options2, 300, 50)
    app.mainloop()