from tkinter import *
window = Tk()

photo = PhotoImage(file = "../Cookpython/5week/cute.gif")
label1 = Label(window, image = photo)

label1.pack()

window.mainloop()