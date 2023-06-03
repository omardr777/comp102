import tkinter as tk

class CheckBox(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Normal',16,'bold')
        kwargs['bg']='#3A7FF6'
        kwargs['fg']='white'
        kwargs['selectcolor'] = 'darkblue'  # to change the background of the check mark 
        super().__init__(master, **kwargs)

