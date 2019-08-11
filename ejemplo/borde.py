import numpy as np
import cv2 
import tensorflow
import keras
from matplotlib import pyplot as plt

#Cargar la mascara
imagen = cv2.imread('13.png  ',0)

op,tOtsu = cv2.threshold(imagen,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

op1,tManual = cv2.threshold(imagen,30,255,cv2.THRESH_BINARY)

histograma = cv2.calcHist([imagen],[0],None,[255],[0,255])


print('OTSU RES')
print(op)

print('MANUAL RES')
print(op1)

plt.plot(histograma)
#Crear un kernel de '1' de 3x3
kernel = np.ones((3,3),np.uint8)
 
#Se aplica la transformacion: Morphological Gradient
transformacion = cv2.dilate(imagen,kernel,iterations = 1) - cv2.erode(imagen,kernel,iterations = 1)
 
#Mostrar el resultado y salir
#cv2.imshow('resultado',transformacion)
cv2.imshow('otsu',tOtsu)
cv2.imshow('manual',tManual)        
cv2.waitKey(0)
plt.show()
cv2.destroyAllWindows()


print('tensorflow: %s' % tensorflow.__version__)
# keras

print('keras: %s' % keras.__version__)
