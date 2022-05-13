from tkinter import Tk, Label
from pyautogui import position
root = Tk()
lab = Label(root, width=30)
lab.pack()

def update():
   lab['text'] = position()
   root.after(10, update)

# run first time
update()

root.mainloop()