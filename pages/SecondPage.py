import tkinter as tk
from components.Checkbox import CheckBox

class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        #You can display the components of page1 here 
        label = tk.Label(self, text="Page 2")
        label.pack(pady=10, padx=10)
        
        button = tk.Button(self, text="Go to Page 3",
                            command=lambda: controller.get_page("LastPage"))
        button.pack()