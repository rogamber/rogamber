from PIL import Image
from Tkinter import *

ventana1 = Tk()
ventana1.geometry("600x900")
#ventana1.pack()
imagen = PhotoImage(file="thumbnail.png")
fondo = Label(ventana1, image=imagen).place(x=0,y=0)
root.mainloop()