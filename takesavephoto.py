from time import sleep
from picamera import PiCamera
import grovepi


y = 0

camera = PiCamera()
camera.resolution = (1024, 768)

# Check if photoname already exists
def checkifphotoexists():
    global y
    global camera

    FileNotFound = True

    while FileNotFound:
        try:  
            open('Bilder/image'+str(y)+'.jpg')
            print('File already exits')
            y+=1
        except FileNotFoundError:
            FileNotFound = False
            camera.capture('Bilder/image'+str(y)+'.jpg')


def fotoaufnehmen():

    buttonPort= 3
    run = True

    grovepi.pinMode(buttonPort, "INPUT")
    buttongedrueckt = False
    camera.start_preview()
    sleep(1)

    while run:
        digitalInput = grovepi.digitalRead(buttonPort)
        #print(digitalInput) Knopf wird gedrückt
        if digitalInput == 1 and buttongedrueckt == False:
            buttongedrueckt = True

           
            # Camera warm-up time
            sleep(1)
            checkifphotoexists()
            camera.stop_preview()
            run = False


        if digitalInput == 0 and buttongedrueckt == True:
            buttongedrueckt = False


