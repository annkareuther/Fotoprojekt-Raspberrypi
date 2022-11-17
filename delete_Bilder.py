import os


y = 0
path = 'Bilder/image' +str(y) + '.jpg'

while os.path.isfile(path):
    os.remove (path)
    print ('image has been deleted')
    y+=1
    path = 'Bilder/image' +str(y) + '.jpg'
    




        