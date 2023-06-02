import tkinter as tk
from components.label import CustomLabel
from components.Textbox import TextBox
from components.Button import Button
class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #You can display the components of page1 here 
        label = CustomLabel(self, text="Page 1")
        label.place(x=110,y=650)

        name_textbox = TextBox(self)
        name_textbox.place(x=120,y=50)

        nat_textbox=TextBox(self)
        nat_textbox.place(x=120,y=100)

        age_textbox=TextBox(self)
        age_textbox.place(x=120,y=150)

        age_label = CustomLabel(self,text='Enter you age')
        age_label.place(x=20,y=150)

        name_label = CustomLabel(self, text='Enter your name')
        name_label.place(x=15, y=50)

        nat_label = CustomLabel(self,text='Enter you Nationality')
        nat_label.place(x=0,y=100)

        continue_button = Button(self, text="continue to page 2",
                            command=lambda: self.next_page(name_textbox.get(),nat_textbox.get(),age_textbox.get()))
        continue_button.place(x=50,y=600)

    def next_page(self,name,age,nationality):
        self.controller.set_user(name,nationality,age)
        print(self.controller.user)
        self.controller.get_page("SecondPage")