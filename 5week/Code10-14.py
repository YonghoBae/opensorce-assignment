from tkinter import *
from tkinter import messagebox

def clickLeft(event):
    messagebox.showinfo("마우스","강아지에서 마우스가 클릭됨")

window = Tk()
window.geometry("400x400")

photo = PhotoImage(file = "../Cookpython/5week/cute.gif")
label1 = Label(window, image = photo)


label1.bind("<Button>",clickLeft)
label1.pack(expand=1,anchor=CENTER)

window.mainloop()