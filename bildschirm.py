import tkinter
import sys
import os
import time
import grovepi


def bildschirm_open():

  if os.environ.get('DISPLAY', '') == '':
    # print('no display found. using: 0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
  master = tkinter.Tk()
  master.title("Welcomescreen")
  master.geometry("800x420")
  label1 = tkinter.Label(master, text="Good morning, want to take a selfie? "
  "Push the button and smile",
                        fg='blue',
                        bg="grey",
                        font=("apple chancery", 20, "normal", "normal"))
  label1.pack()

if os.environ.get('DISPLAY', '') == '':
  # print('no display found. using: 0.0')
  os.environ.__setitem__('DISPLAY', ':0.0')
master = tkinter.Tk()
master.title("Welcomescreen")
master.geometry("800x420")
label1 = tkinter.Label(master, text="Good morning, want to take a selfie? "
"Push the button and smile",
                      fg='blue',
                      bg="grey",
                      font=("apple chancery", 20, "normal", "normal"))
label1.pack()



"""def bildschirm_close():
      if digitalInput == 0 and buttongedrueckt == True:
        buttongedrueckt = False
        master.destroy()"""

buttongedrueckt = False


while True:
  master.update_idletasks()
  master.update()
  digitalInput = grovepi.digitalRead(3)

  if digitalInput == 1 and buttongedrueckt == False:
    buttongedrueckt = True
    master.withdraw()
    print ("versteckt")
    
  

  
