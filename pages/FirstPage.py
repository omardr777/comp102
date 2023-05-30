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
        

        continue_button = Button(self, text="continue to page 2",
                            command=lambda: controller.get_page("SecondPage"))
        continue_button.place(x=50,y=600)

        nametextbox = TextBox(self)
        nametextbox.place(x=120,y=50)

        nattextbox=TextBox(self)
        nattextbox.place(x=120,y=100)

        age_text_box=TextBox(self)
        age_text_box.place(x=120,y=150)

        age_label = CustomLabel(self,text='Enter you age')
        age_label.place(x=20,y=150)

        name_label = CustomLabel(self, text='Enter your name')
        name_label.place(x=15, y=50)

        nat_label = CustomLabel(self,text='Enter you Nationality')
        nat_label.place(x=0,y=100)

        