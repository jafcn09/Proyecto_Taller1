from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QMainWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from agregar import AgregarWindows
from eliminar_producto import EliminarProductosWindows
class UpdateWindow(object):
    def Abrir_Agregar(self):
        self.window = QMainWindow()
        self.ui = AgregarWindows()
        self.ui.setupUi(self.window)
        self.window.show()
    def Abrir_Eliminar(self):
        self.window = QMainWindow()
        self.ui = EliminarProductosWindows()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUI(self, MainWindow_Update):
        MainWindow_Update.setWindowTitle("Actualizar Inventario")
        MainWindow_Update.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindow_Update.setStyleSheet("background-color: #FFC5C5")
        MainWindow_Update.resize(850, 500)
        ventana_atualizar = QWidget(MainWindow_Update)
        #Barra superior
        label_barrasuperior = QLabel(ventana_atualizar)
        label_barrasuperior.setGeometry(0, 0, 850, 100)
        label_barrasuperior.setStyleSheet("background-color: #8E3E3E")

        #Etiqueta titulo
        label_titulo = QLabel("<b> Actualizar Inventario </b>", ventana_atualizar)
        label_titulo.setGeometry(30, 0, 800, 100)
        label_titulo.setFont(QFont('Arial', 30))
        label_titulo.setStyleSheet("color: #fff; background-color: #8E3E3E")

        # Etiqueta consulta
        label_titulo = QLabel("<b> ¿Qué acción deseas realizar? </b>", ventana_atualizar)
        label_titulo.setGeometry(150, 120, 800, 45)
        label_titulo.setFont(QFont('Arial', 15))
        label_titulo.setStyleSheet("color: black; background-color: #FFC5C5")

        # Imagen (AÑADIR Y ELIMINAR)
        label_imagen_anadir = QLabel(ventana_atualizar)
        imagen_anadir = QPixmap('icono_añadir.png').scaled(QSize(150, 150))
        label_imagen_anadir.setPixmap(imagen_anadir)
        label_imagen_anadir.setGeometry(160, 250, 150, 150)

        label_imagen_eliminar = QLabel(ventana_atualizar)
        imagen_eliminar = QPixmap('icono_eliminar.png').scaled(QSize(150, 150))
        label_imagen_eliminar.setPixmap(imagen_eliminar)
        label_imagen_eliminar.setGeometry(535, 250, 150, 150)

        #Botones
        boton_anadirproducto = QPushButton("Añadir Producto", ventana_atualizar)
        boton_anadirproducto.setGeometry(140, 200, 200, 30)
        boton_anadirproducto.clicked.connect(self.Abrir_Agregar)
        boton_anadirproducto.setToolTip("Abre la ventana para agregar\nproductos al inventario")
        boton_anadirproducto.setStyleSheet("color: black;" "background-color: #999999")

        boton_eliminarproducto = QPushButton("Eliminar Producto", ventana_atualizar)
        boton_eliminarproducto.setGeometry(510, 200, 200, 30)
        boton_eliminarproducto.clicked.connect(self.Abrir_Eliminar)
        boton_eliminarproducto.setToolTip("Abre la ventana para eliminar\nproductos del inventario")
        boton_eliminarproducto.setStyleSheet("color: black;" "background-color: #999999")

        MainWindow_Update.setCentralWidget(ventana_atualizar)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    ventana_actualizar = QMainWindow()
    ui = UpdateWindow()
    ui.setupUI(ventana_actualizar)
    ventana_actualizar.show()
    sys.exit(app.exec_())
