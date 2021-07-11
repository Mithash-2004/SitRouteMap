from tkinter import * # Import tkinter

class ImageDemo:
    def __init__(self):
        window = Tk() # Create a window
        window.title("sit route map") # Set title
        
        # Create PhotoImage objects
        inImage = PhotoImage(file = "image.png")
        
        # frame1 to contain label and canvas
        frame1 = Frame(window)
        frame1.pack()
        #lblTitle=Label(font=('arial',40,'bold'),text='SIT  ROUTE  MAP',bd=21,bg='black',fg="white",justify=CENTER)
#lblTitle.grid(row=0)
        Label(frame1, image = inImage).pack(side = RIGHT)
        frame2 = Frame(window)
        frame2.pack()
        lblTitle=Label(font=('arial',40,'bold'),text='SIT  ROUTE  MAP',bd=21,bg='black',fg="white",justify=CENTER)
#lblTitle.grid(row=0)
        button = Button(frame2,text="ENTER")
        button.grid(column=1,row=0,sticky=E)
        window.configure(bg="black")
#        canvas = Canvas(frame1)
#        canvas.create_image(90, 50, image = inImage)
#        canvas["width"] = 200
#        canvas["height"] = 100
#        canvas.pack(side = LEFT)
#        
#        # frame2 to contain buttons, check buttons, and radio buttons
#        frame2 = Frame(window)
#        frame2.pack()
#        lblTitle=Label(font=('arial',40,'bold'),text='SIT  ROUTE  MAP',bd=21,bg='black',fg="white",justify=CENTER)
#        button = Button(window,text="ENTER")
#        button.grid(column=1,row=0)
#        window.configure(bg="black")
#        Button(frame2, image = leftImage).pack(side = LEFT)
#        Button(frame2, image = rightImage).pack(side = LEFT)
#        Checkbutton(frame2, image = usImage).pack(side = LEFT)
#        Checkbutton(frame2, image = ukImage).pack(side = LEFT)
#        Radiobutton(frame2, image = crossImage).pack(side = LEFT)
#        Radiobutton(frame2, image = circleImage).pack(side = LEFT)
        
        window.mainloop() # Create an event loop

ImageDemo() # Create GUI 
