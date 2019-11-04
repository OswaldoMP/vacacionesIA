import numpy as np
import cv2 
# import tensorflow
# import keras
from matplotlib import pyplot as plt

# P = 2

#                     # gray-world

# imagenPrincipal = cv2.imread('2.jpg')#cargar la imagen
# cv2.imshow('Principal',imagenPrincipal)


# setGama=float(input('Gamma :'))

# imagenPrincipal=imagenPrincipal.astype(float)        
# gammaY=float(1/float(setGama))#I ~ u^y

# # # visor HDR
# pixelAlto=np.amax(imagenPrincipal)
# print('PixelAlto')
# print(pixelAlto)
# hdrImagen=np.array(imagenPrincipal,dtype=np.float64)#prepara la imgaen hdr
# hdrImagen[:,:]=(hdrImagen[:,:].astype(float)/float(pixelAlto))*(255.0)
# tonemap1 = cv2.createTonemap(gamma=float(setGama))#asignado gama
# res_debvec = tonemap1.process(imagenPrincipal.copy())#alterando pixel por la gamma 
# hdrImagen=np.array(hdrImagen,dtype=np.uint8)#refactor a unit8
# cv2.imshow("Gamma "+str(setGama), hdrImagen)  

# imagenPrincipal = hdrImagen
# # imagenPrincipal = (hdrImagen * imagenPrincipal) ** gammaY


class Color:
    P = 2
    imagenPrincipal = None

    def __init__(self,rutaImage):
        self.rutaImage = rutaImage
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        

    def imageFloat(self,gamma):
        global imagenPrincipal
        imagenPrincipal = cv2.imread(self.rutaImage)#cargar la imagen
        cv2.imshow('Principal',imagenPrincipal)
        setGama=float(gamma)
        imagenPrincipal=imagenPrincipal.astype(float)        
        gammaY=float(1/float(setGama))#I ~ u^y
        # # visor HDR
        pixelAlto=np.amax(imagenPrincipal)
        print('PixelAlto')
        print(pixelAlto)
        hdrImagen=np.array(imagenPrincipal,dtype=np.float64)#prepara la imgaen hdr
        hdrImagen[:,:]=(hdrImagen[:,:].astype(float)/float(pixelAlto))*(255.0)
        tonemap1 = cv2.createTonemap(gamma=float(setGama))#asignado gama
        # res_debvec = tonemap1.process(imagenPrincipal.copy())#alterando pixel por la gamma 
        res_debvec = tonemap1.process(hdrImagen.copy())#alterando pixel por la gamma 
        hdrImagen=np.array(hdrImagen,dtype=np.uint8)#refactor a unit8
        cv2.imshow("Gamma "+str(setGama), hdrImagen)  
        imagenPrincipal = hdrImagen
    pass

    def grayWorld(self):
        sumaCanalRed = np.sum(imagenPrincipal[:, :, 2])#obtener suma total, canal rojo
        sumaCanalGreen = np.sum(imagenPrincipal[:, :, 1])#obtener suma total, canal verde
        sumaCanalBlue = np.sum(imagenPrincipal[:, :, 0])#obterner suma total, canal azul
        print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
        print('RGB GW')
        print(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)  
        minimo = min(sumaCanalBlue,sumaCanalGreen,sumaCanalRed)   
        print('MINOMOOOO: ',minimo)
        rPrima,gPrima,bPrima = self.getRgbPrima(minimo,sumaCanalRed,sumaCanalGreen,sumaCanalBlue)
        self.resetImage(rPrima,gPrima,bPrima)
        cv2.imwrite('resultadoBalanceColor/gray-world.jpg',imagenPrincipal)
        cv2.imshow('gray-world', cv2.imread('resultadoBalanceColor/gray-world.jpg'))

        pass

    def sacaleByMax(self):
        sumaCanalRed = np.max(imagenPrincipal[:,:,2])#obtener suma total, canal rojo
        sumaCanalGreen = np.max(imagenPrincipal[:,:,1])#obtener suma total, canal verde
        sumaCanalBlue = np.max(imagenPrincipal[:,:,0])#obtener suma total, canal azul
        # print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
        print('RGB SBM')
        # print(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)
        minimo = min(sumaCanalBlue,sumaCanalGreen,sumaCanalRed)
        # print('MINOMOOOO: ',minimo)
        rPrima,gPrima,bPrima = self.getRgbPrima(minimo,sumaCanalRed,sumaCanalGreen,sumaCanalBlue)
        self.resetImage(rPrima,gPrima,bPrima)
        cv2.imwrite('resultadoBalanceColor/ScaleByMax.jpg',imagenPrincipal)
        cv2.imshow('ScaleByMax', cv2.imread('resultadoBalanceColor/ScaleByMax.jpg'))

        pass

    def shadesOfGray(self):
        # P=float(input('Valor P :'))

        sumaCanalRed = np.sum(imagenPrincipal[:, :, 2]**float(self.P))**float(1/self.P)
        sumaCanalGreen = np.sum(imagenPrincipal[:, :, 1]**float(self.P))**float(1/self.P)
        sumaCanalBlue = np.sum(imagenPrincipal[:, :, 0]**float(self.P))**float(1/self.P)
        # print('.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.')
        print('RGB SOG')
        # print(sumaCanalRed,sumaCanalGreen,sumaCanalBlue)
        minimo = min(sumaCanalBlue,sumaCanalGreen,sumaCanalRed)
        # print('MINOMOOOO: ',minimo)    
        rPrima,gPrima,bPrima = self.getRgbPrima(minimo,sumaCanalRed,sumaCanalGreen,sumaCanalBlue)
        self.resetImage(rPrima,gPrima,bPrima)
        cv2.imwrite(f'resultadoBalanceColor/shadesOfGray_P_{self.P}.jpg',imagenPrincipal)
        cv2.imshow('shadesOfGray P:'+str(self.P), cv2.imread(f'resultadoBalanceColor/shadesOfGray_P_{self.P}.jpg'))
        if self.P == 2:
            self.P = 4
            self.shadesOfGray()
            pass
        elif self.P == 4:
            self.P = 6
            self.shadesOfGray()
            pass
        pass

    def resetImage(self,rPrima,gPrima,bPrima):
        imagenPrincipal[:,:,0]=(imagenPrincipal[:,:,0].astype(float))*(float(bPrima))
        imagenPrincipal[:,:,1]=(imagenPrincipal[:,:,1].astype(float))*(float(gPrima))
        imagenPrincipal[:,:,2]=(imagenPrincipal[:,:,2].astype(float))*(float(rPrima))
        
        pass

    def getRgbPrima( self,minimo, sumaCanalRed,sumaCanalGreen,sumaCanalBlue):
        # realizar operecion por el canal escogido
        bPrima = minimo / sumaCanalBlue
        gPrima = minimo / sumaCanalGreen 
        rPrima = minimo / sumaCanalRed
        print('Cambiado')
        print('blue' ,bPrima)
        print('green', gPrima)
        print('red', rPrima)
        return rPrima,gPrima,bPrima



# grayWorld()
# sacaleByMax()
# shadesOfGray()
# cv2.waitKey(0)
# cv2.destroyAllWindows()


