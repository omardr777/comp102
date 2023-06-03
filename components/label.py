import tkinter as tk
class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        kwargs['font'] = ('Normal',16,'bold')
        kwargs['bg'] = '#FCFCFC'
        kwargs['fg'] = '#515486'
        super().__init__(master, **kwargs)
    
    def set_font_size(self,size,weight):
       fW = weight
       if fW == '':
          self.configure(font=(self.cget('font').split()[0],size))
       else:
           self.configure(font=(self.cget('font').split()[0],size,fW))
    

    def set_bg_fg(self,fg,bg):
       self.configure(bg=bg,fg=fg)