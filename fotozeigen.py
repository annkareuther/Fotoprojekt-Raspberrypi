import tkinter
import sys
import os
import time
import grovepi

y= 0
def fotozeigen():
    
  if os.environ.get('DISPLAY', '') == '':
    # print('no display found. using: 0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
    master = tkinter.Tk()
    master.title("Dein/Euer Foto")
    master.geometry("800x420")
    ImageTk.PhotoImage(Image.open("'Bilder/image'+str(y)+'.jpg'"))
    img = tkinter.Label(master, 'Bilder/image'+str(y)+'.jpg')
    frame = Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
  
  label1.pack()
