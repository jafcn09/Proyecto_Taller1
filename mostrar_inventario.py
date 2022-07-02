from PyQt5.QtWidgets import QApplication, QWidget, QPlainTextEdit, QPushButton, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont
class ListarProductos(object):
    def setupUI(self, ListarWindows):
        ListarWindows.setWindowTitle("Productos")
        ListarWindows.setWindowIcon(QIcon("ShirtIcon.png"))
        ListarWindows.setStyleSheet("background-color: #33B8FF;")
        ListarWindows.resize(1200, 720)
        ventana_producto = QWidget(ListarWindows)
        # ETIQUETAS DE LA VENTANA
        label_producto = QLabel("<b>Lista De Productos</b>", ventana_producto)
        label_producto.setGeometry(350, 50, 600, 50)
        label_producto.setFont(QFont('Arial', 20))
        label_producto.setStyleSheet("color: #fff")



        # CAJAS DE TEXTO DE LA VENTANA
        inventario = QPlainTextEdit(ventana_producto)
        inventario.setPlainText(open('Inventario.txt').read())
        inventario.setGeometry(60, 180, 1080, 480)
        inventario.setStyleSheet("color: black;" "background-color: white")
        ListarWindows.setCentralWidget(ventana_producto)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Mi_Inventario = QMainWindow()
    ui = ListarProductos()
    ui.setupUI(Mi_Inventario)
    Mi_Inventario.show()
    sys.exit(app.exec_())
