
import bildschirm 
import takesavephoto
from time import sleep
 

# welcomefenster anzeigen
# bei gedrückten Button welcomefenster weg und Live- Übertragung zeigen
# zweites Mal button drücken Fomachento 
# Foto anzeigen paar Sekunden 
# WelcomeFenster wieder

run = True
while run:
    bildschirm.startbildschirm()
    takesavephoto.fotoaufnehmen()
    sleep (5)



print('start')

