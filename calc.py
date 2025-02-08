from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
window=Tk()
window.tite("calculator")
window.geometry("600x600")
upload=Image.open()
upload=upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(image=image)
label.place(x=180,y=20)
label2=Label(window,text="hello")
label2.place(x=180,y=15)
def msg():
    var=messagebox.showinfo("alert!", "do you wnat to continue")
    if var=="ok":
        topwin()
button=Button(window,text="click me",command=msg)
button.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.title("calculations")
    top.geometry("500x500")
    label3=Label(top,text="please enter your ammount")
    entry1=Entry(top)
    l1=Label(top,text="2000")
    l2=Label(top,text="500")
    l3=Label(top,text="100")
    e1=Entry(top)
    e2=Entry(top)
    e3=Entry(top)
    def calculator():
        global amount
        amount=int(entry1.get())
        no2000=amount//2000
        amount=amount%2000
        no500=amount//500
        amount=amount%500
        no100=amount//100
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(END,str(no2000))
        e2.insert(END,str(no500))
        e3.insert(END,str(no100))
    b1=Button(top,text="calculate",command=calculator)
    label3.place(x=230,y=50)
    entry1.place(x=200,y=80)
    b1.place(x=240,y=120)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    e1.place(x=270,y=200)
    e2.place(x=270,y=230)
    e3.place(x=270,y=260)
    top.mainloop()
window.mainloop()