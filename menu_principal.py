from PyQt5.QtWidgets import QFrame,QApplication, QWidget, QPushButton, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from Mi_perfil import ProfileWindow
from Actualizar_inventario import UpdateWindow
from mostrar_inventario import ListarProductos
class MenuWindow(object):
    def abrir_mostrar(self):
        self.window = QMainWindow()
        self.ui = ListarProductos()
        self.ui.setupUI(self.window)
        self.window.show()
    def abrir_update(self):
        self.window = QMainWindow()
        self.ui = UpdateWindow()
        self.ui.setupUI(self.window)
        self.window.show()

    def ver_perfil(self):
        self.window = QMainWindow()
        self.ui = ProfileWindow()
        self.ui.setupUI(self.window)
        self.window.show()

    def setupUi(self, MainWindow_Menu):
        MainWindow_Menu.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindow_Menu.setStyleSheet("background-color: #ae2012;")
        MainWindow_Menu.resize(1200, 720)
        MainWindow_Menu.setWindowTitle("BOOSMAN")
        ventana_menu = QWidget(MainWindow_Menu)
        BM = QLabel("<b>MENU PRINCIPAL</b>", ventana_menu)
        BM.setGeometry(428, 50, 600, 50)
        BM.setFont(QFont('Arial', 15))
        F_Preg = QFrame(ventana_menu)
        F_Preg.setGeometry(0, 227, 1200, 70)
        F_Preg.setStyleSheet("background-color: #80ed99;")
        Pregunta_Label = QLabel("¿QUE DESEA HACER?", ventana_menu)
        Pregunta_Label.move(480, 250)
        Pregunta_Label.setStyleSheet("background-color: rgb(255,255,255,0);")
        Btn_Mostrar = QPushButton("MOSTRAR INVENTARIO", ventana_menu)
        Btn_Mostrar.move(200, 390)
        Btn_Mostrar.setStyleSheet("color: black;" "background-color: #f48c06;")
        Btn_Mostrar.clicked.connect(self.abrir_mostrar)
        Btn_Mostrar.setIcon(QIcon("eye.png"))
        Btn_Mostrar.setToolTip("Abre el inventario")
        Btn_Act = QPushButton("ACTUALIZAR INVENTARIO", ventana_menu)
        Btn_Act.move(720, 390)
        Btn_Act.setStyleSheet("color: black;" "background-color: #f48c06;")
        Btn_Act.clicked.connect(self.abrir_update)
        Btn_Act.setIcon(QIcon("updated.png"))
        Btn_Act.setToolTip("Abre la ventana para actualizar los productos")
        F_Perfil = QFrame(ventana_menu)
        F_Perfil.setGeometry(0, 550, 1200, 200)
        F_Perfil.setStyleSheet("background-color: #415a77;")
        BtnVerPerfil = QPushButton("VER PERFIL", ventana_menu)
        BtnVerPerfil.move(500, 620)
        BtnVerPerfil.setStyleSheet("color: black;" "background-color: #f48c06;")
        BtnVerPerfil.setIcon(QIcon("profile.png"))
        BtnVerPerfil.setToolTip("Abre la ventana con sus datos publicos")
        BtnVerPerfil.clicked.connect(self.ver_perfil)
        MainWindow_Menu.setCentralWidget(ventana_menu)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Menu_Window = QMainWindow()
    ui = MenuWindow()
    ui.setupUi(Menu_Window)
    Menu_Window.show()
    sys.exit(app.exec_())
