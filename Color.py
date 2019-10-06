import numpy as np
import cv2 
import tensorflow
import keras
from matplotlib import pyplot as plt



                    # gray-world

imagenPrincipal = cv2.imread('2.jpg')#cargar la imagen
cv2.imshow('Principal',imagenPrincipal)


setGama=input('Gamma :')

# setGamaV=float(1**float(setGama))
imagenPrincipal=imagenPrincipal.astype(float)        
# imagenPrincipal[:,:]=(float((setGamaV)))*((imagenPrincipal[:,:].astype(float))**(float(setGama)))


# # HDR
pixelAlto=np.amax(imagenPrincipal)
print('PixelAlto')
print(pixelAlto)
hdrImagen=np.array(imagenPrincipal,dtype=np.float64)#prepara la imgaen hdr
hdrImagen[:,:]=(hdrImagen[:,:].astype(float)/float(pixelAlto))*(255.0)#usar clanal de 8 bits
tonemap1 = cv2.createTonemap(gamma=float(setGama))#asignado gama
res_debvec = tonemap1.process(imagenPrincipal.copy())#alterando pixel por la gamma 
hdrImagen=np.array(hdrImagen,dtype=np.uint8)#refactor a unit8
cv2.imshow("Gamma "+str(setGama), hdrImagen)  

imagenPrincipal = hdrImagen


def grayWorld():
    sumaCanalRed = np.sum(imagenPrincipal[:, :, 2])#obtener suma total, canal rojo
    sumaCanalGreen = np.sum(imagenPrincipal[:, :, 1])#obtener suma total, canal verde
    sumaCanalBlue = np.sum(imagenPrincipal[:, :, 0])#obterner suma total, canal azul
    print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
    print('RGB GW')
    print(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)

    canal = getCanal(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)#obtener el menor canal para realizar balanceo

    rPrima,gPrima,bPrima = getRgbPrima(canal,sumaCanalRed,sumaCanalGreen,sumaCanalBlue)

    imagenPrincipal[:,:,0]=(imagenPrincipal[:,:,0].astype(float))*(float(bPrima))
    imagenPrincipal[:,:,1]=(imagenPrincipal[:,:,1].astype(float))*(float(gPrima))
    imagenPrincipal[:,:,2]=(imagenPrincipal[:,:,2].astype(float))*(float(rPrima))
    cv2.imwrite('gray-world.jpg',imagenPrincipal)
    cv2.imshow('gray-world', cv2.imread('gray-world.jpg'))

    pass

def sacaleByMax():
    sumaCanalRed = np.max(imagenPrincipal[:,:,2])#obtener suma total, canal rojo
    sumaCanalGreen = np.max(imagenPrincipal[:,:,1])#obtener suma total, canal verde
    sumaCanalBlue = np.max(imagenPrincipal[:,:,0])#obtener suma total, canal azul
    print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
    print('RGB SBM')
    print(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)

    canal = getCanal(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)#obtener el menor canal para realizar balanceo
    
    rPrima,gPrima,bPrima = getRgbPrima(canal,sumaCanalRed,sumaCanalGreen,sumaCanalBlue)

    imagenPrincipal[:,:,0]=(imagenPrincipal[:,:,0].astype(float))*(float(bPrima))
    imagenPrincipal[:,:,1]=(imagenPrincipal[:,:,1].astype(float))*(float(gPrima))
    imagenPrincipal[:,:,2]=(imagenPrincipal[:,:,2].astype(float))*(float(rPrima))
    cv2.imwrite('ScaleByMax.jpg',imagenPrincipal)
    cv2.imshow('ScaleByMax', cv2.imread('ScaleByMax.jpg'))

    pass

def shadesOfGray():
    P=1
    sumaCanalRed = (np.sum(imagenPrincipal[:,:,2])**float(P))**float(1/P)
        # sumaCanalRed = np.sum(imagenPrincipal[:,:,2]**float(P))**float(1/P)
    sumaCanalGreen = (np.sum(imagenPrincipal[:,:,1])**float(P))**float(1/P)
    sumaCanalBlue = (np.sum(imagenPrincipal[:,:,0])**float(P))**float(1/P)
    print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
    print('RGB SOG')
    print(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)

    canal = getCanal(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)#obtener el menor canal para realizar balanceo
    # canal=1
    rPrima,gPrima,bPrima = getRgbPrima(canal,sumaCanalRed,sumaCanalGreen,sumaCanalBlue)

    imagenPrincipal[:,:,0]=(imagenPrincipal[:,:,0].astype(float))*(float(bPrima))
    imagenPrincipal[:,:,1]=(imagenPrincipal[:,:,1].astype(float))*(float(gPrima))
    imagenPrincipal[:,:,2]=(imagenPrincipal[:,:,2].astype(float))*(float(rPrima))
    cv2.imwrite('shadesOfGray.jpg',imagenPrincipal)
    cv2.imshow('shadesOfGray P:'+str(P), cv2.imread('shadesOfGray.jpg'))
    pass

def getCanal( sumaCanalRed,sumaCanalGreen,sumaCanalBlue):
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
    return canal


def getRgbPrima( canal, sumaCanalRed,sumaCanalGreen,sumaCanalBlue):
    # realizar operecion por el canal escogido
    if canal == 0: #canal azul escogido
        bPrima = 1
        gPrima = sumaCanalBlue / sumaCanalGreen 
        rPrima = sumaCanalBlue / sumaCanalRed
    elif canal == 1: #canal verde escogido
        gPrima = 1
        bPrima = sumaCanalGreen / sumaCanalBlue
        rPrima = sumaCanalGreen / sumaCanalRed
    elif canal == 2: #canal rojo escogido
        rPrima = 1
        gPrima = sumaCanalRed / sumaCanalGreen
        bPrima = sumaCanalRed / sumaCanalBlue

    print('Cambiado')
    print('blue' ,bPrima)
    print('green', gPrima)
    print('red', rPrima)
    return rPrima,gPrima,bPrima




grayWorld()
sacaleByMax()
shadesOfGray()
cv2.waitKey(0)
cv2.destroyAllWindows()



































