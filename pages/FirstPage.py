import tkinter as tk
from componets.label import CustomLabel
class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        #You can display the components of page1 here 
        label = CustomLabel(self, text="Page 1")
        label.pack(pady=10, padx=10)
            
        button = tk.Button(self, text="Go to Page 2",
                            command=lambda: controller.get_page("SecondPage"))
        button.pack()