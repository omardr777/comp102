import tkinter as tk

class TextBox(tk.Entry):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Normal',10,'bold')
        kwargs['bg']='White'
        kwargs['relief']='solid'
        kwargs['bd']='3'
        super().__init__(master, **kwargs)