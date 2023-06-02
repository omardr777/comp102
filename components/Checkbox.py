import tkinter as tk

class CheckBox(tk.Checkbutton):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Normal',16,'bold')
        kwargs['bg']='light blue'
        super().__init__(master, **kwargs)

