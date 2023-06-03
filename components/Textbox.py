import tkinter as tk

class TextBox(tk.Entry):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Normal',16)
        kwargs['borderwidth'] = 0  # Remove the default border
        kwargs['bg']='#F1F5FF'
        kwargs['highlightcolor'] = '#515486'  # Color of the active border
        kwargs['relief']='solid'
        kwargs['highlightbackground'] = '#FCFCFC'  # Color of the border
        kwargs['bd']='3'
        kwargs['highlightthickness'] = 0  # Remove the default highlight border
        kwargs['highlightthickness'] = 2  # Border thickness
        super().__init__(master, **kwargs)