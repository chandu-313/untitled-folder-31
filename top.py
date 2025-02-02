from tkinter import *
window=Tk()
window.geometry("300x300")
window.configure(bg="red")
def var():
    top=Toplevel()
    top.geometry("100x100")
    top.configure(bg="white")
    top.mainloop()
button=Button(window,text="click me",command=var)
button.place(x=50,y=50)
window.mainloop()