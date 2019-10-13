import numpy as np
import cv2
from matplotlib import pyplot as plt

#Cargar la mascara
# imagen = cv2.imread('test.jpg',0)#obtener la imagen y convertir a gris


def binaryImage(rutaImage):
    #Cargar la mascara
    imagen = cv2.imread(rutaImage,0)#obtener la imagen y convertir a gris
    metodo = "BINARY"
    # fijamos el umbral a 127 para obtener una imagen binaria
    # BINARY
    op1,tManual = cv2.threshold(imagen,127,255,cv2.THRESH_BINARY)
    print('Binary RES')
    print(op1)
    
    #Almacendo imagen
    cv2.imwrite('resultadoBinarizacion/BINARY.jpg',tManual)
    showImage(imagen,metodo,tManual)
    pass

def otsuImage(rutaImage):
    imagen = cv2.imread(rutaImage,0)#obtener la imagen y convertir a gris

    # Se define el umbral con el metodo de otsu.
    # OTSU
    op,tOtsu = cv2.threshold(imagen,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)# op = obtener el umbral de otsu. 
    print('Otsu RES')
    print(op)
    #Almacendo imagen
    cv2.imwrite('resultadoBinarizacion/OTSU.jpg',tOtsu)
    showImage(imagen,"OTUSU",tOtsu)
    histograma(imagen,op)
    pass

def adatativeImage(rutaImage):
    imagen = cv2.imread(rutaImage,0)#obtener la imagen y convertir a gris

    # Local adaptativa
    img = cv2.medianBlur(imagen,5)
    # img = cv2.medianBlur(tOtsu,5)
    tAdta = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
                                cv2.THRESH_BINARY,11,2)
    
    #Almacendo imagen
    cv2.imwrite('resultadoBinarizacion/ADATATIVE.jpg',tAdta)
    showImage(imagen,"ADAPTATIVA",tAdta)
    pass

def fondoMorfologico(rutaImage):
    imagen = cv2.imread(rutaImage,0)#obtener la imagen y convertir a gris

    #Fondo Morfologico
    kernel = np.ones((10,10),np.uint8)
    dilation = cv2.dilate(imagen,kernel,iterations = 1)
    diff = cv2.absdiff(dilation,imagen)
    kernel = np.ones((3,3),np.uint8)
    tranDiff = cv2.dilate(imagen,kernel,iterations = 1) - cv2.erode(imagen,kernel,iterations = 1)
    cv2.imwrite('resultadoBinarizacion/FONDO_DILA.jpg',dilation)
    cv2.imwrite('resultadoBinarizacion/FONDO_DIFF.jpg',diff)
    cv2.imwrite('resultadoBinarizacion/FONDO_TRANDIFF.jpg',tranDiff)
    showImage(imagen,"BACK_DILA",dilation)
    showImage(imagen,"BACK_DIFF",tranDiff)
    pass

def histograma(imagen,op):
    histograma = cv2.calcHist([imagen],[0],None,[255],[0,255])
    plt.plot(histograma)
    plt.axvline(op, color='R', linestyle='dashed', linewidth=1)
    plt.ylabel('Pixel')
    plt.xlabel('Nivel de Gris')
    plt.title('Histograma Imagen Original \n Threshold = ' + str(op))
    pass

def showImage(imagen, metodo, resultado):
    cv2.imshow('ORIGIN',imagen)
    cv2.imshow(f'{metodo }',resultado)
    pass


if __name__ == "__main__":
    # binaryImage('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
    # otsuImage('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
    # adatativeImage('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
    # fondoMorfologico('/home/oswaldo/UPCH/IA/C1.A2/vacacionesIA/ejemplo/test.jpg')
    plt.show()
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pass












