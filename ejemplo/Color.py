import numpy as np
import cv2 
import tensorflow
import keras
from matplotlib import pyplot as plt



                    # gray-world

imagenPrincipal = cv2.imread('1.jpg')#cargar la imagen
cv2.imshow('Principal',imagenPrincipal)


val=float(1**2.2)
imagenPrincipal=imagenPrincipal.astype(float)        
imagenPrincipal[:,:]=(float((val)))*((imagenPrincipal[:,:].astype(float))**(float(2.2)))


# HDR
visua=np.amax(imagenPrincipal)
image_HDR=np.array(imagenPrincipal,dtype=np.float64)
image_HDR[:,:]=(image_HDR[:,:].astype(float)/float(visua))*(255.0)
tonemap1 = cv2.createTonemap(gamma=2.2)
res_debvec = tonemap1.process(imagenPrincipal.copy()) 
cv_image =  np.clip(res_debvec*255, 0, 255).astype('uint8')
imS = cv2.resize(cv_image, (imagenPrincipal.shape[0], imagenPrincipal.shape[1]))                    
image_HDR=np.array(image_HDR,dtype=np.uint8)
cv2.imshow("Gamma 2.2", image_HDR)  

imagenPrincipal = image_HDR

imagenPrincipal = imagenPrincipal.copy()
imagenPrincipal=imagenPrincipal.astype(float) 

sumaCanalRed = np.sum(imagenPrincipal[:, :, 2])#obtener suma total, canal rojo
sumaCanalGreen = np.sum(imagenPrincipal[:, :, 1])#obtener suma total, canal verde
sumaCanalBlue = np.sum(imagenPrincipal[:, :, 0])#obterner suma total, canal azul
print('RGB')

print(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)

# buscar el canal, elegir canal
if sumaCanalBlue < sumaCanalGreen: #si blue es menor a green
    if sumaCanalBlue < sumaCanalRed: #si blue es menor a red
        canal = 0 #canal es blue
        print('blue escogido')
    else: #red fue menor a blue
        canal = 2
        print('red escogido')
else:#green fue menor a blue
    if sumaCanalGreen < sumaCanalRed:#si green es menor a red
        canal = 1
        print('green escogido')
    else: #red fue el menor
        canal = 2
        print('red escogido')

print(canal)

# realizar operecion por el canal escogido
if canal == 0: #canal azul escogido
    factorB = 1
    factorG = sumaCanalBlue / sumaCanalGreen 
    factorR = sumaCanalBlue / sumaCanalRed
elif canal == 1: #canal verde escogido
    factorG = 1
    # totalG = totalG
    factorB = sumaCanalGreen / sumaCanalBlue
    factorR = sumaCanalGreen / sumaCanalRed
elif canal == 2: #canal rojo escogido
    factorR = 1
    # totalR = totalR
    factorG = sumaCanalRed / sumaCanalGreen
    factorB = sumaCanalRed / sumaCanalBlue


print('Cambiado')
print('blue' ,factorB)
print('green', factorG)
print('red', factorR)

# balancear los canales por los resultado de obtenidos
imagenPrincipal[:,:,0]=(imagenPrincipal[:,:,0].astype(float))*(float(factorB))
imagenPrincipal[:,:,1]=(imagenPrincipal[:,:,1].astype(float))*(float(factorG))
imagenPrincipal[:,:,2]=(imagenPrincipal[:,:,2].astype(float))*(float(factorR))

cv2.imwrite('gray-world.jpg',imagenPrincipal)
cv2.imshow('gray-world', cv2.imread('gray-world.jpg'))




cv2.waitKey(0)
cv2.destroyAllWindows()



































