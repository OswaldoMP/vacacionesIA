import cv2
import numpy as np

# image = cv2.imread('ob1.jpg',0)



# gray = cv2.GaussianBlur(image, (5, 5), 0)


# op,tOtsu = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# _,umbral = cv2.threshold(gray,op,255,cv2.THRESH_BINARY_INV)

# tAdta = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
#                                 cv2.THRESH_BINARY_INV,11,2)

# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,3))
# # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(1,1))
# # kernel = np.array(
#     # [
#     # [1,1,1,1,1,1,1,1,1,1,1,1,1],
#     # [1,0,0,0,0,0,0,0,0,0,0,0,1],
#     # [1,0,0,0,0,0,0,0,0,0,0,0,1],
#     # [1,0,0,0,0,0,0,0,0,0,0,0,1],
#     # [1,0,0,0,0,0,0,0,0,0,0,0,1],
#     # [1,0,0,0,0,0,0,0,0,0,0,0,1],
#     # [1,1,1,1,1,1,1,1,1,1,1,1,1]#
#     # ],np.uint8
#     # )
# erosion = cv2.erode(umbral,kernel,iterations=1)#5/7; 1/3
# dilatacion = cv2.dilate(erosion,kernel,iterations=3)

# op,tOtsu = cv2.threshold(dilatacion,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

# apertura = cv2.morphologyEx(umbral, cv2.MORPH_OPEN,kernel)
# gradiente = cv2.morphologyEx(umbral,cv2.MORPH_GRADIENT,kernel)


# _,contorno,_ = cv2.findContours(dilatacion, cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(image,contorno,-1,(0,0,255),5)

# print('Total: ',len(contorno) )


# cv2.imshow('Contorno', image)
# cv2.imshow('Erocion',erosion)
# cv2.imshow('EroBIn',umbral)
# cv2.imshow('dilatacion',dilatacion)
# cv2.imshow('Apertura',apertura)
# cv2.imshow('Gradie',gradiente)
# cv2.imshow('ASDF',tOtsu)

# print(kernel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


class ContObject:

    def __init__(self, rutaImage):
        self.rutaImage = rutaImage
    
    def Cont(self):
        image = cv2.imread(self.rutaImage,0)

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

        total = len(contorno)

        cv2.imwrite('resultadoCont/Erocion.jpg',erosion)
        cv2.imwrite('resultadoCont/Umbral.jpg',umbral)
        cv2.imwrite('resultadoCont/Dilatacion.jpg',dilatacion)
        cv2.imwrite('resultadoCont/Apertura.jpg',apertura)
        cv2.imwrite('resultadoCont/Gradiente.jpg',gradiente)
        cv2.imwrite('resultadoCont/Contorno.jpg',image)

        cv2.imshow('Contorno', image)
        # cv2.imshow('Erocion',erosion)
        # cv2.imshow('EroBIn',umbral)
        # cv2.imshow('dilatacion',dilatacion)
        # cv2.imshow('Apertura',apertura)
        # cv2.imshow('Gradie',gradiente)
        # cv2.imshow('ASDF',tOtsu)

        print(kernel)
        return total
