import tkinter as tk
from components.label import CustomLabel
from components.Checkbox import CheckBox
from components.Textbox import TextBox

class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #You can display the components of page1 here 
        label = CustomLabel(self, text="Page 1")
        label.pack(pady=10, padx=10)

        options = ['1','2','3']
        cardcompoent1 = CheckBox(self,text='click me').pack()

        button = tk.Button(self, text="Go to Page 2",
                            command=lambda: controller.get_page("SecondPage"))
        
        testtextbox = TextBox(self)
        testtextbox.pack()
        button.pack()