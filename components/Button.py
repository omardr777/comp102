import tkinter as tk

class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Arial', 16, 'bold')
        kwargs['cursor'] = 'hand2'
        kwargs['border'] = 0
        kwargs['bg'] = '#3A7FF6' 
        kwargs['fg'] = 'white' 
        super().__init__(master, **kwargs)
