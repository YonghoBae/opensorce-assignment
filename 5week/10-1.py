from tkinter import *
window = Tk()

photo = PhotoImage(file = "../Cookpython/5week/cute.gif")
label1 = Label(window, image = photo)
label2 = Label(window, image = photo)

label1.pack(side=LEFT)
label2.pack()

window.mainloop()