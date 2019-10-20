import cv2
import numpy as np

image = cv2.imread('ob1.jpg',0)

# # _,umbral = cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
# op,tOtsu = cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# tAdta = cv2.adaptiveThreshold(tOtsu,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#                                 cv2.THRESH_BINARY_INV,11,2)

# _,umbral = cv2.threshold(image,op,255,cv2.THRESH_BINARY_INV)

# kernel = np.ones((1,1),np.uint8)
# dilation = cv2.dilate(tAdta,kernel,iterations = 6)
# kernel = np.ones((0,0),np.uint8)
# dilation2 = cv2.dilate(dilation,kernel,iterations=1)

# diff = cv2.absdiff(dilation,image)
# op,tOtsuDiff = cv2.threshold(diff,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)


# kernel = np.ones((2,2),np.uint8)
# tranDiff = cv2.dilate(tAdta,kernel,iterations = 1) - cv2.erode(tAdta,kernel,iterations = 1)


# op,tOtsu = cv2.threshold(dilation2,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# tAdtaDila = cv2.adaptiveThreshold(tOtsu,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#                                     cv2.THRESH_BINARY_INV,11,2)

# _,contorno,_ = cv2.findContours(tAdta, cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_SIMPLE)

# cv2.drawContours(image,contorno,-1,(0,255,0),3)

# print('Total: ',len(contorno) )

# cv2.imshow('origin',image)
# cv2.imshow('umbral',tAdta)
# cv2.imshow('dilatacio: ',dilation)
# cv2.imshow('dilatacion2:',dilation2)
# cv2.imshow('adtDIla:', tAdtaDila)
# cv2.imshow('diff:',diff)
# cv2.imshow('thDiff',tOtsuDiff)
# cv2.imshow('dila-ero',tranDiff)

gray = cv2.GaussianBlur(image, (5, 5), 0)


op,tOtsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

_,umbral = cv2.threshold(gray,op,255,cv2.THRESH_BINARY_INV)

tAdta = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                cv2.THRESH_BINARY_INV,11,2)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
# kernel = np.array(
    # [
    # [1,1,1,1,1,1,1,1,1,1,1,1,1],
    # [1,0,0,0,0,0,0,0,0,0,0,0,1],
    # [1,0,0,0,0,0,0,0,0,0,0,0,1],
    # [1,0,0,0,0,0,0,0,0,0,0,0,1],
    # [1,0,0,0,0,0,0,0,0,0,0,0,1],
    # [1,0,0,0,0,0,0,0,0,0,0,0,1],
    # [1,1,1,1,1,1,1,1,1,1,1,1,1]#
    # ],np.uint8
    # )
erosion = cv2.erode(umbral,kernel,iterations=1)#5/7; 1/3
dilatacion = cv2.dilate(erosion,kernel,iterations=3)

op,tOtsu = cv2.threshold(dilatacion,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

apertura = cv2.morphologyEx(umbral, cv2.MORPH_OPEN,kernel)
gradiente = cv2.morphologyEx(umbral,cv2.MORPH_GRADIENT,kernel)


_,contorno,_ = cv2.findContours(dilatacion, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image,contorno,-1,(0,0,255),5)

print('Total: ',len(contorno) )


cv2.imshow('Contorno', image)
cv2.imshow('Erocion',erosion)
cv2.imshow('EroBIn',umbral)
cv2.imshow('dilatacion',dilatacion)
cv2.imshow('Apertura',apertura)
cv2.imshow('Gradie',gradiente)
cv2.imshow('ASDF',tOtsu)

print(kernel)
cv2.waitKey(0)
cv2.destroyAllWindows()

