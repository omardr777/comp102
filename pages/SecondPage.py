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
        width = 170
        height = 170

        emptyLabel = tk.Label(self, height=7)
        emptyLabel.grid(row=0, column=0, rowspan=3)
        label1 = ImageLabel(self, image_path1, width, height)
        label1.grid(row=3, column=0, rowspan=5)
        label2 = ImageLabel(self, image_path2, width, height)
        label2.grid(row=8, column=0, rowspan=5)
        label3 = ImageLabel(self, image_path3, width, height)
        label3.grid(row=13, column=0, rowspan=5) 

        KhobarLabel = CheckBox(self, text="Al-Khobar") 
        KhobarLabel.grid(row=4, column=1)
        DammamLabel = CheckBox(self, text="Al-Dammam") 
        DammamLabel.grid(row=5, column=1)
        AhsaLabel = CheckBox(self, text="Al-Ahsa") 
        AhsaLabel.grid(row=6, column=1)

        RiyadhLabel = CheckBox(self, text="Al-Riyadh") 
        RiyadhLabel.grid(row=9, column=1)
        DiriyahLabel = CheckBox(self, text="Al-Diriyah") 
        DiriyahLabel.grid(row=10, column=1)
        KharjLabel = CheckBox(self, text="Al-Kharj") 
        KharjLabel.grid(row=11, column=1)

        MakkahLabel = CheckBox(self, text="Al-Makkah") 
        MakkahLabel.grid(row=14, column=1)
        MadinahLabel = CheckBox(self, text="Al-Madinah") 
        MadinahLabel.grid(row=15, column=1)
        JeddahLabel = CheckBox(self, text="Al-Jeddah") 
        JeddahLabel.grid(row=16, column=1)


        label = tk.Label(self, text="Page 2")
        label.grid(row=0, column=1)
        
        button = tk.Button(self, text="Go to Page 3",
                            command=lambda: controller.get_page("LastPage"))
        button.grid(row=1, column=1)