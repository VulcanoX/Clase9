from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication
from PyQt5 import QtGui
import sys

class Ventana1(QMainWindow):
    def __init__ (self, parent=None):
        super(Ventana1, self).__init__(parent)

        #Poner titulo
        self.setWindowTitle("Formulario de registro")

        #Poner icono a la ventana
        self.setWindowIcon(QtGui.QIcon('imagenes/7782608.png'))

        #Establecemos el alto y el ancho
        self.ancho = 900
        self.alto = 600

        self.resize(self.ancho, self.alto)

        #Hacer que la ventana se vea en el centro
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        #Fijar ancho y alto de la pantalla
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        #Establecemos el fondo principal
        self.fondo =  QLabel(self)

        #Definimos la imagen del fondo
        self.imagenFondo = QPixmap('imagenes/ford-mustang-gt-frente_1280x720_xtrafondos.com.jpg')
        self.fondo.setPixmap(self.imagenFondo)

        #Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        #Hacemos que se adapte al tamaño de la ventana
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        #Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        #Establecemos la distribucion de los elementos en layout horizontal
        self.horizontal = QHBoxLayout()

        #Le ponemos las margenes
        self.horizontal.setContentsMargins(30,30,30,30)

        # --------------LAYOUT IZQUIERDO---------------

        #Creamos el layout izquierdo
        self.ladoIzquierdo = QFormLayout()

        #Hcaemos el letrero
        self.letrero1 = QLabel()
        self.letrero1.setText("Informacion del cliente")

        #Asignacmos el tipo de letra
        self.letrero1.setFont(QFont("Arial",20))







        #--------------IMPORTANTE PONER AL FINAL--------------
        self.fondo.setLayout(self.horizontal)





if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())



