#import necessary libraries
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x300")

def viaan():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

button = Button(root, text="Scan for Virus", command =viaan)
button.place(x=40, y=80)

root.mainloop()
