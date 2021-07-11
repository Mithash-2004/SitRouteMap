from tkinter import *
import time
import datetime	
import random
import sys
	
window=Tk()
window.title("SIT ROUTE MAP")
window.geometry("1920x1080")

lblTitle=Label(font=('arial',40,'bold'),text='SIT  ROUTE  MAP',bd=21,bg='black',fg="white",justify=CENTER)
lblTitle.grid(row=0)

Image = PhotoImage(file="image.png")
Button( image = Image).pack(side = LEFT)
#frame1 = Frame(window)
#frame1.pack()
#Label(frame1, image = Image).pack(side = LEFT)
#button = Button(window,image=image)
button = Button(window,text="ENTER")
button.grid(column=1,row=0)
window.configure(bg="black")
window.mainloop()
