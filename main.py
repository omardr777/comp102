import tkinter as tk
from FirstPage import FirstPage 
from SecondPage import SecondPage
from LastPage import LastPage

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
    app.mainloop()