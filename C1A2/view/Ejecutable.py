from window_ui import *
from Binarizacion import Binarizacion
from Color import Color
from ContObject import ContObject
import cv2

class MainWindow(QtWidgets.QMainWindow, IForm):
    image = ""
    metodo = ""
    metodoColor = ""
    metodoContObj = ''

    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.buttonSelect.clicked.connect(self.selectImage)
        self.buttonBinary.clicked.connect(self.binary)
        self.buttonOtsu.clicked.connect(self.otus)
        self.buttonAdap.clicked.connect(self.adap)
        self.buttonEjecutar.clicked.connect(self.fondo)
        self.buttonColor.clicked.connect(self.color)
        self.buttonCont.clicked.connect(self.contObj)
        
        
    def selectImage(self):
        global image, metodo, metodoColor, metodoContObj
        # imageLabel = QtWidgets.QLabel()
        image , _ = QtWidgets.QFileDialog.getOpenFileName(None,
        'Select Image', '', "Image files (*.jpg *.png *.jpeg)")    
        if image:
            print('RUTA IMAGEN: ',image)
            metodo = Binarizacion(image)
            metodoColor = Color(image)
            metodoContObj = ContObject(image)
            return image
            # pixmap = QtGui.QPixmap(image)    
            # imageLabel.setPixmap(pixmap)
            # self.contenedorImagenPrincipal.setBackgroundRole(QtGui.QPalette.Dark)
            # self.contenedorImagenPrincipal.setWidget(imageLabel)  

    def binary(self):
        global metodo
        metodo.binaryImage()

    def otus(self):
        global metodo
        metodo.otsuImage()
    
    def adap(self):
        global metodo
        metodo.adatativeImage()

    def fondo(self):
        global metodo
        metodo.fondoMorfologico()
    
    def color(self):
        global metodoColor
        gamma = float(self.textGamma.text())
        metodoColor.imageFloat(gamma)
        metodoColor.grayWorld()
        metodoColor.sacaleByMax()
        metodoColor.shadesOfGray()
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def contObj(self):
        global metodoContObj
        total = metodoContObj.Cont()
        self.textCont.setText(str(total))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
