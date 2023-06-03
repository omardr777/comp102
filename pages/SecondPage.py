import tkinter as tk
from components.Checkbox import CheckBox
from components.ImageLabel import ImageLabel
from components.Textbox import TextBox
from components.label import CustomLabel
from components.Button import Button

class SecondPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self['bg'] = '#FCFCFC'
        
        
        #You can display the components of page1 here
        image_path1 = "Images/EastProvince.jpg"
        image_path2 = "Images/MiddleProvince.jpg"
        image_path3 = "Images/WestProvince.jpg"
        width = 250
        height = 250

        label1 = ImageLabel(self, image_path1, width, height)
        label1.grid(row=0, column=0, rowspan=5)
        label2 = ImageLabel(self, image_path2, width, height)
        label2.grid(row=5, column=0, rowspan=5)
        label3 = ImageLabel(self, image_path3, width, height)
        label3.grid(row=10, column=0, rowspan=5) 

        KhobarLabel = CheckBox(self, text="Al-Khobar") 
        KhobarLabel.grid(row=1, column=1)
        DammamLabel = CheckBox(self, text="Dammam") 
        DammamLabel.grid(row=2, column=1)
        AhsaLabel = CheckBox(self, text="Al-Ahsa") 
        AhsaLabel.grid(row=3, column=1)

        RiyadhLabel = CheckBox(self, text="Riyadh") 
        RiyadhLabel.grid(row=6, column=1)
        DiriyahLabel = CheckBox(self, text="Al-Diriyah") 
        DiriyahLabel.grid(row=7, column=1)
        KharjLabel = CheckBox(self, text="Al-Kharj") 
        KharjLabel.grid(row=8, column=1)

        MakkahLabel = CheckBox(self, text="Mecca") 
        MakkahLabel.grid(row=11, column=1)
        MadinahLabel = CheckBox(self, text="Medina") 
        MadinahLabel.grid(row=12, column=1)
        JeddahLabel = CheckBox(self, text="Jeddah") 
        JeddahLabel.grid(row=13, column=1)

        ChoosingLabel = CustomLabel(self, text='Please choose the cities you want to discover')
        ChoosingLabel.grid(row=2, column=2, padx=200)
        
        button = Button(self, text="Search",
                            command=lambda: controller.get_page("LastPage"))
        button.grid(row=12, column=3)

        button = Button(self, text="Go back",
                            command=lambda: controller.get_page("FirstPage"))
        button.grid(row=13, column=3)