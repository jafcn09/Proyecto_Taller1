from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont

class EliminarProductosWindows(object):
    def setupUi(self, MainWindowsEliminar):
        def eliminar_producto():
            productos = open("Inventario.txt", "r")
            cod_productos = productos.readlines()
            productos.close()
            productos2 = open("Inventario.txt", "w")
            for line in cod_productos:
                if " "+cajatexto_codigo.text()+" " not in line:
                    productos2.write(line)
            productos2.close()
            label_msg_eli.setText("   Se eliminó el producto "+cajatexto_codigo.text()+"."
                                +"\nPuede ir a ver la lista nuevamente")
        MainWindowsEliminar.setWindowTitle("ELIMINAR PRODUCTOS")
        MainWindowsEliminar.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindowsEliminar.setStyleSheet("background-color: #33B8FF;")
        MainWindowsEliminar.resize(1220, 700)
        ventana_eliminar_producto = QWidget(MainWindowsEliminar)
        # ETIQUETAS DE LA VENTANA

        label_msg_eli = QLabel(ventana_eliminar_producto)
        label_msg_eli.setGeometry(700, 310, 800, 100)
        label_msg_eli.setFont(QFont('Arial', 10))
        label_msg_eli.setStyleSheet("color: #fff")

        label_producto = QLabel("<b>Especifique el producto a eliminar:</b>", ventana_eliminar_producto)
        label_producto.setGeometry(170, 50, 900, 60)
        label_producto.setFont(QFont('Arial', 20))
        label_producto.setStyleSheet("color: #fff")

        label_codigo = QLabel("<b>CODIGO:</b>", ventana_eliminar_producto)
        label_codigo.setGeometry(450, 350, 120, 30)
        label_codigo.setFont(QFont('Arial', 10))
        label_codigo.setStyleSheet("color: #fff")

        # CAJAS DE TEXTO DE LA VENTANA
        cajatexto_codigo = QLineEdit(ventana_eliminar_producto)
        cajatexto_codigo.setGeometry(590, 350, 80, 30)
        cajatexto_codigo.setStyleSheet("color: black;" "background-color: white")

        boton_eliminar_productos = QPushButton("ELIMINAR", ventana_eliminar_producto)
        boton_eliminar_productos.setIcon(QIcon("trash_icon.png"))
        boton_eliminar_productos.setGeometry(500, 500, 150, 50)
        boton_eliminar_productos.clicked.connect(eliminar_producto)
        boton_eliminar_productos.setStyleSheet("color: black;" "background-color: #FFCA33")
        boton_eliminar_productos.setToolTip("Elimina el producto segun su codigo")
        MainWindowsEliminar.setCentralWidget(ventana_eliminar_producto)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Inventario_Eliminado = QMainWindow()
    ui = EliminarProductosWindows()
    ui.setupUi(Inventario_Eliminado)
    Inventario_Eliminado.show()
    sys.exit(app.exec_())
