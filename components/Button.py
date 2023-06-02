import tkinter as tk

class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        # Customize the appearance
        kwargs['bg'] = '#3A7FF6'  # Set background color
        kwargs['fg'] = 'white'  # Set foreground color
        kwargs['font'] = ('Arial', 16, 'bold')  # Set font
        kwargs['border'] = 0
        # Initialize the parent class (Button)
        super().__init__(master, **kwargs)
