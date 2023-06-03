import tkinter as tk

class CheckBox(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        kwargs['selectcolor'] = 'darkblue'
        kwargs['font'] = ('Normal',16,'bold')
        kwargs['bg']='#3A7FF6'
        kwargs['fg']='white'
        super().__init__(master, **kwargs)

