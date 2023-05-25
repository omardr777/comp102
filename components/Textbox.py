import tkinter as tk

class TextBox(tk.Entry):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Normal',12,'bold')
        kwargs['bg']='light green'
        super().__init__(master, **kwargs)