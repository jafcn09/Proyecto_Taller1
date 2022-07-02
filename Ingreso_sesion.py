from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon, QPixmap, QFont
from Registro import RegisterWindow
from menu_principal import MenuWindow

class LoginWindow(object):
    def open_registro(self):
        self.window = QMainWindow()
        self.ui = RegisterWindow()
        self.ui.setupUi(self.window)
        self.window.show()
    def open_menu(self):
        self.window = QMainWindow()
        self.ui = MenuWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        Inicio_Sesion_window.hide()
    def setupUi(self, MainWindow_Login):
        def verificar_usuario():
            archivo = open("Registro.txt", "r")
            usuarios = archivo.readlines()
            archivo.close()
            for line in usuarios:
                if E_Usuario.text() and E_contra.text() in line:
                    Btn_inicio_sesion.clicked.connect(self.open_menu)
                    Btn_inicio_sesion.move(500, 550)
                    Btn_inicio_sesion.setText("INICIAR SESION")
                    Msg_Usu_no_encontrado.setText("USUARIO ENCONTRADO")
                else:
                    Msg_Usu_no_encontrado.setGeometry(800, 545, 280, 50)
                    Msg_Usu_no_encontrado.setText("USUARIO NO ENCONTRADO")
        MainWindow_Login.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindow_Login.setStyleSheet("background-color: #ae2012;")
        MainWindow_Login.resize(1200, 720)
        MainWindow_Login.setWindowTitle("BOOSMAN")
        ventana_login = QWidget(MainWindow_Login)
        BMicon = QPixmap('Boosman.png').scaled(QSize(250, 250))
        BMicon_Label = QLabel("", ventana_login)
        BMicon_Label.setPixmap(BMicon)
        BMicon_Label.move(460, 70)
        B = QLabel("<b>BIENVENIDO A BOOSMAN</b>", ventana_login)
        B.setGeometry(350, 50, 600, 50)
        B.setFont(QFont('Arial', 15))
        Btn_inicio_sesion = QPushButton("INICIAR SESION", ventana_login)
        Btn_inicio_sesion.move(500, 550)
        Btn_inicio_sesion.setStyleSheet("color: black;" "background-color: #dda15e;")
        Btn_inicio_sesion.clicked.connect(verificar_usuario)
        Btn_inicio_sesion.setToolTip("Si tienes un usuario y contraseña,\nse abre la ventana del menu principal")
        Msg_Usu_no_encontrado = QLabel(ventana_login)
        Msg_Usu_no_encontrado.setStyleSheet("color: white;")
        Usuario_label = QLabel("<b>Usuario:", ventana_login)
        Usuario_label.move(300, 330)
        Contra_label = QLabel("<b>Contraseña:", ventana_login)
        Contra_label.move(300, 430)
        E_Usuario = QLineEdit(ventana_login)
        E_Usuario.setPlaceholderText("Ingrese sus nombres")
        E_Usuario.setGeometry(500, 330, 350, 30)
        E_Usuario.setStyleSheet("color: black;" "background-color: white;")
        E_Usuario.setPlaceholderText("Ingrese su usuario")
        E_contra = QLineEdit(ventana_login)
        E_contra.setGeometry(500, 430, 350, 30)
        E_contra.setStyleSheet("color: black;" "background-color: white;")
        E_contra.setPlaceholderText("Ingrese su contraseña")
        Sin = QLabel("<b>¿No tienes usuario o contraseña?:</b>", ventana_login)
        Sin.move(100, 640)
        Btn_registro = QPushButton("REGISTRATE", ventana_login)
        Btn_registro.move(510, 630)
        Btn_registro.clicked.connect(self.open_registro)
        Btn_registro.setToolTip("Abre ventana de registro")
        Btn_registro.setStyleSheet("color: black;" "background-color: #adc178;")
        MainWindow_Login.setCentralWidget(ventana_login)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Inicio_Sesion_window = QMainWindow()
    ui = LoginWindow()
    ui.setupUi(Inicio_Sesion_window)
    Inicio_Sesion_window.show()
    sys.exit(app.exec_())
