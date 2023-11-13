from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QFormLayout, QApplication, QLineEdit, \
    QPushButton
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
        self.ancho = 1000
        self.alto = 700

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

        #Ponemos el color del letrero
        self.letrero1.setStyleSheet("color: #000080;")

        #Agregamos el letrero a la primera fila
        self.ladoIzquierdo.addRow(self.letrero1)






        #Hacemos el letrero
        self.letrero2 = QLabel()

        #Establecemos el ancho
        self.letrero2.setFixedWidth(340)

        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados"
                              "\ncon asterisco son obligatorios.")

        self.letrero2.setFont(QFont("Arial", 10))

        #Le agregamos margenes y le ponemos color al texto
        self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        self.ladoIzquierdo.addRow(self.letrero2)

        #Hacemos el campo para ingresar el nombre
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Contraseña*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Confirmar Contraseña", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrarse")
        self.botonRegistrar.setFixedWidth(90)

        self.botonRegistrar.setStyleSheet("background-color: #008845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #008845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # Agregamos el layout a la primera fila
        self.horizontal.addLayout(self.ladoIzquierdo)

        #--------------IMPORTANTE PONER AL FINAL--------------
        self.fondo.setLayout(self.horizontal)

    #Ponemos el metodo del botonLimpiar
    def accion_botonLimpiar(self):
        pass


    #Metodo botonRegistrarse
    def accion_botonRegistrar(self):
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())



