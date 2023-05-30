import tkinter as tk
class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Normal',8,'bold')
        super().__init__(master, **kwargs)