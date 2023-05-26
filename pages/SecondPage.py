import tkinter as tk
from components.Checkbox import CheckBox
from components.ImageLabel import ImageLabel
from components.Textbox import TextBox
from components.label import CustomLabel

class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        
        #You can display the components of page1 here
        image_path1 = "Images/EastProvince.jpg"
        image_path2 = "Images/MiddleProvince.jpg"
        image_path3 = "Images/WestProvince.jpg"
        width = 100
        height = 100


        label1 = ImageLabel(self, image_path1, width, height)
        label1.grid(row=2, column=0)
        label2 = ImageLabel(self, image_path2, width, height)
        label2.grid(row=3, column=0)
        label3 = ImageLabel(self, image_path3, width, height)
        label3.grid(row=4, column=0)  

        label = tk.Label(self, text="Page 2")
        label.grid(row=0, column=0)
        
        button = tk.Button(self, text="Go to Page 3",
                            command=lambda: controller.get_page("LastPage"))
        button.grid(row=1, column=0)