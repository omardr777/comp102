from tkinter import *
from PIL import Image, ImageTk


class ImageLabel(Label):
    def __init__(self, master, image_path, width, height, **kwargs):
        super().__init__(master, **kwargs)
        
        image = Image.open(image_path)
        resize_image = image.resize((width, height))
        photo = ImageTk.PhotoImage(resize_image)
        self.configure(image=photo)
        self.image = photo