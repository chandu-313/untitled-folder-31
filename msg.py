from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("400x400")  
def var():
    messagebox.showwarning("disclaimer","do not open this")
button=Button(window,text="click",command=var)
button.place(x=30,y=30)
window.mainloop()