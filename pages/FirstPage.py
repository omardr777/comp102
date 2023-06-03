import tkinter as tk
from components.label import CustomLabel
from components.Textbox import TextBox
from components.Button import Button
class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.config_grid(self,1,2)
        main_color = '#FCFCFC'
        self['bg'] = main_color
        welcomeLabel = CustomLabel(self, text="Welcome to the Tourism Guide in KSA")
        welcomeLabel.configure(font=(welcomeLabel.cget('font').split()[0],18),bg='#3A7FF6',fg=main_color)
        welcomeLabel.grid(row=0,column=0,sticky="nsew")

        detail_container = tk.Frame(self)
        detail_container.grid(row=0,column=1,sticky='nsew')
        detail_container['bg'] = main_color
        self.config_grid(detail_container,3,3)

        inputs_frame = tk.Frame(detail_container)
        inputs_frame.grid(row=1,column=1)
        inputs_frame['bg'] = main_color
        self.config_grid(inputs_frame,5,2)
        
        # Create gaps between rows in inputs_frame
        CustomLabel(inputs_frame, text="").grid(row=1, column=0, pady=20)
        CustomLabel(inputs_frame, text="").grid(row=3, column=0, pady=20)

        #You can display the components of page1 here 
        label = CustomLabel(detail_container, text="Enter your details")
        label.configure(font=(label.cget('font').split()[0],18,'bold'))
        label.grid(row=0,column=1,sticky='s')

        name_label = CustomLabel(inputs_frame, text='Enter your name')
        name_label.grid(row=0,column=0)
        name_textbox = TextBox(inputs_frame)
        name_textbox.grid(row=0,column=1)

        nat_label = CustomLabel(inputs_frame,text='Enter your Nationality')
        nat_label.grid(row=1,column=0)
        nat_textbox=TextBox(inputs_frame)
        nat_textbox.grid(row=1,column=1)

        age_label = CustomLabel(inputs_frame,text='Enter your age')
        age_label.grid(row=2,column=0)
        age_textbox=TextBox(inputs_frame)
        age_textbox.grid(row=2,column=1)




        continue_button = Button(detail_container, text="Next page",
                            command=lambda: self.next_page(name_textbox.get(),nat_textbox.get(),age_textbox.get()))
        continue_button.grid(row=2,column=1)

    def next_page(self,name,age,nationality):
        self.controller.set_user(name,nationality,age)
        self.controller.get_page("SecondPage")

    def config_grid(self,container,rows,columns):
        for i in range(rows):
            container.grid_rowconfigure(i,weight=1)
        for i in range(columns):
            container.grid_columnconfigure(i,weight=1)