from tkinter import *
from PIL import ImageTk , Image
top = Tk()
filename = r'./Exp/1-start.png'
img = Image.open(filename)
images = ImageTk.PhotoImage(img)
label = Label(top,image=images)
label.pack()
top.mainloop()