import tkinter as tk
from components.Checkbox import CheckBox
from components.Textbox import TextBox
from components.label import CustomLabel

class LastPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        #You can display the components of page1 here 
        label = tk.Label(self, text="Page 3")
        label.pack(pady=10, padx=10)
            
        button = tk.Button(self, text="Go to back to page 2",
                            command=lambda: controller.get_page("SecondPage"))
        button.pack()