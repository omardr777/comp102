import tkinter as tk

class Button(tk.Button):
    def __init__(self, master=None, **kwargs):
        # Customize the appearance
        kwargs['bg'] = 'blue'  # Set background color
        kwargs['fg'] = 'white'  # Set foreground color
        kwargs['font'] = ('Arial', 12, 'bold')  # Set font
        
        # Initialize the parent class (Button)
        super().__init__(master, **kwargs)
