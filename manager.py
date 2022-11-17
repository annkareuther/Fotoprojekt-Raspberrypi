from DisplayHandler import Displayhandler
import time

class Manager():

    display = None

    def start(self):
        display = DisplayHandler()
        i= 0

        while i < 10:
            display.show ( "hello World" + str (i) )
            i +=1
            time.sleep (1)

        print ("Start manager")


m = Manager()
m.start()