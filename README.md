Ein Fotoprojekt mit Raspberrypi

Idee:
In diesem Projekt geht es darum per Knopfdruck ein Foto zu machen.
Am Ende des Projekts soll zuerst ein Wilkommensbild gezeigt werden, per Knopfdruck soll dann die Live-Übertragung der Kamera angezeigt werden
und beim nächsten Knopfdruck wird dann das Foto geschossen.
Nach dem Knopfdruck soll das geschossene Foto für einige Sekunden angezeigt werden. Das Foto wird zusätzlich auf einem Bilderordner gespeichert.
Dieser Vorgang wird dann unendlich wiederholt.

Hardware: 
Für dieses Projekt ist ein Bildschirm, eine Kamera und ein Knopf notwendig.
Ein Lämpchen und und ein Tonspieler könnte als eine kleine Erweiterung ebenfalls gebraucht werden.

Die Kamera (Camera V2.1) wird an den Kameraanschluss des Raspberrypis angeschlossen.
Der Knopf wurde in diesem Fall an Digitalinput 3 gesetzt.

Der Knopf (Button V1.2) wurde in den Digitalinput 5 angesetzt.

Der Bildschirm wird einerseits mit dem Bildschirmverbindungskabel an dem raspberrypi angeschlossen (Display-Anschluss)
andererseits wird der Bildschirm mit zwei weiteren Kabel verbunden. 
5V --> 2.6.1
GND ---> 2.6.3

Nun wird noch der Strom angeschlossen und das Display sollte aufleuchten.
