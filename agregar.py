from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont
class AgregarWindows(object):
    def setupUi(self, MainWindow_Agregar):
        def agrega():
            archivo = open("Inventario.txt", "a")
            codigo = E_Codigo_R.text()
            nombre = E_Nombre_R.text()
            descripcion = E_Descripcion_R.text()
            precio = E_Precio_R.text()
            marca = E_Marca_R.text()
            talla = E_Talla_R.text()
            modelo = E_Modelo_R.text()
            archivo.write("\n "+codigo+"       | "
                          +nombre+"                     | "
                          +descripcion+"                      | S/."
                          +precio+"     | "
                          +marca+"      | "
                          +talla+"      | "
                          +modelo)
            archivo.close()
            Btn_agregar_P.setText("¡Producto guardado!\nCierre la ventana")
        MainWindow_Agregar.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindow_Agregar.setStyleSheet("background-color: #3380FF;")
        MainWindow_Agregar.resize(1200, 720)
        MainWindow_Agregar.setWindowTitle("REGISTRO Producto")
        ventana_agregar = QWidget(MainWindow_Agregar)
        ventana_agregar.setWindowIcon(QIcon("producto.jpg"))
        Titulo_Registro = QLabel("<b>Ingresar Productos a añadir</b>", ventana_agregar)
        Titulo_Registro.setGeometry(435, 50, 600, 50)
        Titulo_Registro.setFont(QFont('Arial', 12))
        Nombres_R_label = QLabel("<b>Codigo:", ventana_agregar)
        Nombres_R_label.move(300, 200)
        E_Codigo_R = QLineEdit(ventana_agregar)
        E_Codigo_R.setGeometry(520, 200, 350, 30)
        E_Codigo_R.setPlaceholderText("Ingrese  el codigo del producto")
        E_Codigo_R.setStyleSheet("color: black;" "background-color: white;")
        E_Nombre_R = QLabel("<b>Nombre:", ventana_agregar)
        E_Nombre_R.move(300, 250)
        E_Nombre_R = QLineEdit(ventana_agregar)
        E_Nombre_R.setGeometry(520, 250, 350, 30)
        E_Nombre_R.setPlaceholderText("Ingrese el nombre del producto")
        E_Nombre_R.setStyleSheet("color: black;" "background-color: white;")
        Descripcion_R_label = QLabel("<b>Descripcion:", ventana_agregar)
        Descripcion_R_label.move(300, 300)
        E_Descripcion_R = QLineEdit(ventana_agregar)
        E_Descripcion_R.setGeometry(520, 300, 350, 30)
        E_Descripcion_R.setPlaceholderText("Ingrese la descripcion del producto")
        E_Descripcion_R.setStyleSheet("color: black;" "background-color: white;")
        Precio_R_label = QLabel("<b>Precio:", ventana_agregar)
        Precio_R_label.move(300, 350)
        E_Precio_R = QLineEdit(ventana_agregar)
        E_Precio_R.setGeometry(520, 350, 350, 30)
        E_Precio_R.setPlaceholderText("Ingrese el precio del producto")
        E_Precio_R.setStyleSheet("color: black;" "background-color: white;")
        Marca_R_label = QLabel("<b>Marca:", ventana_agregar)
        Marca_R_label.move(300, 400)
        E_Marca_R = QLineEdit(ventana_agregar)
        E_Marca_R.setGeometry(520, 400, 350, 30)
        E_Marca_R.setPlaceholderText("Ingrese la marca del producto")
        E_Marca_R.setStyleSheet("color: black;" "background-color: white;")
        Tallas_R_label = QLabel("<b>Tallas:", ventana_agregar)
        Tallas_R_label.move(300, 450)

        E_Talla_R = QLineEdit(ventana_agregar)
        E_Talla_R.setGeometry(520, 450, 350, 30)
        E_Talla_R.setPlaceholderText("Ingrese las tallas del producto")
        E_Talla_R.setStyleSheet("color: black;" "background-color: white;")

        Modelo_R_label = QLabel("<b>Modelos:", ventana_agregar)
        Modelo_R_label.move(300, 500)
        E_Modelo_R = QLineEdit(ventana_agregar)
        E_Modelo_R.setGeometry(520, 500, 350, 30)
        E_Modelo_R.setPlaceholderText("Ingrese el modelo de prenda")
        E_Modelo_R.setStyleSheet("color: black;" "background-color: white;")

        Btn_agregar_P = QPushButton("Añadir Productos", ventana_agregar)
        Btn_agregar_P.setGeometry(450, 610, 330, 90)
        Btn_agregar_P.setStyleSheet("color: black;" "background-color: #B2FF33;")
        Btn_agregar_P.clicked.connect(agrega)
        MainWindow_Agregar.setCentralWidget(ventana_agregar)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Agregar_Windows = QMainWindow()
    ui = AgregarWindows()
    ui.setupUi(Agregar_Windows)
    Agregar_Windows.show()
    sys.exit(app.exec_())
