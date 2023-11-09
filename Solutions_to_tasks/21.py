from tkinter import *


class Example:
   def __init__(self):
       self.master = Tk()
       self.label = Label(self.master, text='Very Long Example Label Text')
       self.label.grid(row=0, column=1)
       self.button = Button(self.master, text='Change Button')
       self.button.grid(row=1, column=0)
       self.button1 = Button(self.master, text='Change Label')
       self.button1.grid(row=1, column=2)
       self.master.mainloop()


if __name__ == '__main__':
   Example()