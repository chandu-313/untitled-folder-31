from tkinter import *
from PIL import Image,ImageTk 
window=Tk()
window.title("Welcome")
window.geomentry("300x400")
var = Image.open("")
image=ImageTk.PhotoImage(var)
label=Label(window,image=image,height=300,width=400)
label.place(x=30,y=40)
window.mainloop()