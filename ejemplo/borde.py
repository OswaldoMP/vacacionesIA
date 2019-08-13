import numpy as np
import cv2 
import tensorflow
import keras
from matplotlib import pyplot as plt

#Cargar la mascara
imagen = cv2.imread('page.png',0)#obtener la imagen y convertir a gris

# fijamos el umbral a 127 para obtener una imagen binaria
# BINARY
op1,tManual = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY)

# pasamos la imagen,no defimos el umbral, maximo,binarizar con el metodo de otsu
# OTSU
op,tOtsu = cv2.threshold(imagen,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)# op = obtener el umbral de otsu. 

# 
# Local adaptativa
img = cv2.medianBlur(imagen,5)
# img = cv2.medianBlur(tOtsu,5)
tAdta = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                            cv2.THRESH_BINARY,11,2)

# blur = cv2.GaussianBlur(imagen,(5,5),0)
# blur = cv2.GaussianBlur(tOtsu,(5,5),0)
# op2,tAdta = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# obtenemos el histograma de la imagen en tonos de grises
histograma = cv2.calcHist([imagen],[0],None,[255],[0,255])


print('OTSU RES')
print(op)

print('MANUAL RES')
print(op1)
plt.plot(histograma)
plt.axvline(op, color='R', linestyle='dashed', linewidth=1)
plt.ylabel('Pixel')
plt.xlabel('Nivel de Gris')
plt.title('Histograma ')
#Crear un kernel de '1' de 3x3
kernel = np.ones((3,3),np.uint8)

#Se aplica la transformacion: Morphological Gradient
transformacion = cv2.dilate(imagen,kernel,iterations = 1) - cv2.erode(imagen,kernel,iterations = 1)

#Mostrar el resultado y salir
#cv2.imshow('resultado',transformacion)
cv2.imshow('ORIGIN',imagen)
cv2.imshow('OTSU',tOtsu)
cv2.imshow('BINARY',tManual)  
cv2.imshow("ADATATIVE", tAdta)      
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


print('tensorflow: %s' % tensorflow.__version__)
# keras

print('keras: %s' % keras.__version__)
