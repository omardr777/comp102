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
        self.userinfo = tk.StringVar(value='')
        
        def update_selected_cities(*args):
            self.userinfo.set('Welcome '+self.controller.user.get().split(',')[0]+', please choose the cities you want to discover')
            
        self.controller.user.trace("w", update_selected_cities)
        
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

        khobar_checkbox = CheckBox(self, text="Khobar",command=lambda:self.controller.toggle_cities(khobar_checkbox['text'])) 
        khobar_checkbox.grid(row=1, column=1)
        dammam_checkbox = CheckBox(self, text="Dammam",command=lambda:self.controller.toggle_cities(dammam_checkbox['text'])) 
        dammam_checkbox.grid(row=2, column=1)
        ahsa_checkbox = CheckBox(self, text="Al-Ahsa",command=lambda:self.controller.toggle_cities(ahsa_checkbox['text'])) 
        ahsa_checkbox.grid(row=3, column=1)

        riyadh_checkbox = CheckBox(self, text="Riyadh",command=lambda:self.controller.toggle_cities(riyadh_checkbox['text'])) 
        riyadh_checkbox.grid(row=6, column=1)
        diriyah_checkbox = CheckBox(self, text="Diriyah",command=lambda:self.controller.toggle_cities(diriyah_checkbox['text'])) 
        diriyah_checkbox.grid(row=7, column=1)
        kharj_checkbox = CheckBox(self, text="Al-Kharj",command=lambda:self.controller.toggle_cities(kharj_checkbox['text'])) 
        kharj_checkbox.grid(row=8, column=1)

        mecca_checkbox = CheckBox(self, text="Makkah",command=lambda:self.controller.toggle_cities(mecca_checkbox['text'])) 
        mecca_checkbox.grid(row=11, column=1)
        medina_checkbox = CheckBox(self, text="Madinah",command=lambda:self.controller.toggle_cities(medina_checkbox['text'])) 
        medina_checkbox.grid(row=12, column=1)
        jeddah_checkbox = CheckBox(self, text="Jeddah",command=lambda:self.controller.toggle_cities(jeddah_checkbox['text'])) 
        jeddah_checkbox.grid(row=13, column=1)

        ChoosingLabel = CustomLabel(self, textvariable=self.userinfo)
        ChoosingLabel.place(x=500, y=50)
        
        button = Button(self, text="Search",
                            command=self.click_search_button)
        button.grid(row=12, column=2, padx=900)

        button = Button(self, text="Go back",
                            command=lambda: controller.get_page("FirstPage"))
        button.grid(row=13, column=2, padx=900)

    def click_search_button(self):
        self.controller.get_page('LastPage')
        # self.controller.fetch_data()
    
   