import tkinter 
from tkinter import * 
import sys
import os
from time import sleep
import grovepi
from PIL import ImageTk, Image



def fotozeigen():
  y=0
    
  if os.environ.get('DISPLAY', '') == '':
    # print('no display found. using: 0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
    master = tkinter.Tk()
    master.title("Dein/Euer Foto")
    master.geometry("800x420")
 
    test = Image.open('Bilder/image' +str (y) + '.jpg') 
  
    #test.show()

    y+=1
    print (y)
   


  run = True 
  while run:
    master.update_idletasks()
    master.update()

  
fotozeigen()
