from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont
class RegisterWindow(object):
    def setupUi(self, MainWindow_Register):
        def registrar():
            def validar_vacios(cadena):
                if len(str.strip(cadena)) != 0:
                    valor = True
                else:
                    valor = False
                return valor
            def validar_dni(dni_ingresado):
                if len(E_DNI_R.text()) == 8 and (E_DNI_R.text().isdigit()):
                    valor = True
                else:
                    valor = False
                return valor
            if validar_dni(E_DNI_R.text()) and validar_vacios(E_Nombres_R.text()) \
                                           and validar_vacios(E_Apellidos_R.text()) \
                                           and validar_vacios(E_DNI_R.text()) \
                                           and validar_vacios(E_Usuario_R.text()) \
                                           and validar_vacios(E_Contra_R.text()):
                archivo = open("Registro.txt", "w")
                nombre = E_Nombres_R.text()
                apellido = E_Apellidos_R.text()
                dni = E_DNI_R.text()
                usu = E_Usuario_R.text()
                con = E_Contra_R.text()
                archivo.write(nombre + "\n" + apellido + "\n" + dni + "\n" + usu + "\n" + con)
                archivo.close()
                Btn_registro_R.setText("¡Usuario Guardado!\nCierre la ventana e inicie sesion")
            else:
                Btn_registro_R.setText("Verifique sus datos ingresados")
        MainWindow_Register.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindow_Register.setStyleSheet("background-color: #ae2012;")
        MainWindow_Register.resize(1200, 720)
        MainWindow_Register.setWindowTitle("REGISTRO")
        ventana_registro = QWidget(MainWindow_Register)
        ventana_registro.setWindowIcon(QIcon("ShirtIcon.png"))
        Titulo_Registro = QLabel("<b>HOJA DE REGISTRO</b>", ventana_registro)
        Titulo_Registro.setGeometry(435, 50, 600, 50)
        Titulo_Registro.setFont(QFont('Arial', 12))
        Nombres_R_label = QLabel("<b>Nombres:", ventana_registro)
        Nombres_R_label.move(300, 200)
        E_Nombres_R = QLineEdit(ventana_registro)
        E_Nombres_R.setGeometry(520, 200, 350, 30)
        E_Nombres_R.setPlaceholderText("Ingrese sus nombres")
        E_Nombres_R.setStyleSheet("color: black;" "background-color: white;")
        Apellidos_R_label = QLabel("<b>Apellidos:", ventana_registro)
        Apellidos_R_label.move(300, 250)
        E_Apellidos_R = QLineEdit(ventana_registro)
        E_Apellidos_R.setGeometry(520, 250, 350, 30)
        E_Apellidos_R.setPlaceholderText("Ingrese sus apellidos")
        E_Apellidos_R.setStyleSheet("color: black;" "background-color: white;")
        DNI_R_label = QLabel("<b>DNI:", ventana_registro)
        DNI_R_label.move(300, 300)
        E_DNI_R = QLineEdit(ventana_registro)
        E_DNI_R.setGeometry(520, 300, 350, 30)
        E_DNI_R.setPlaceholderText("Ingrese su DNI")
        E_DNI_R.setStyleSheet("color: black;" "background-color: white;")
        Usuario_R_label = QLabel("<b>Nuevo Usuario:", ventana_registro)
        Usuario_R_label.move(300, 350)
        E_Usuario_R = QLineEdit(ventana_registro)
        E_Usuario_R.setGeometry(520, 350, 350, 30)
        E_Usuario_R.setPlaceholderText("Ingrese su usuario")
        E_Usuario_R.setStyleSheet("color: black;" "background-color: white;")
        Usuario_R_label = QLabel("<b>Nueva Contraseña:", ventana_registro)
        Usuario_R_label.move(300, 400)
        E_Contra_R = QLineEdit(ventana_registro)
        E_Contra_R.setGeometry(520, 400, 350, 30)
        E_Contra_R.setPlaceholderText("Ingrese su contraseña")
        E_Contra_R.setStyleSheet("color: black;" "background-color: white;")
        Btn_registro_R = QPushButton("REGISTRATE", ventana_registro)
        Btn_registro_R.setGeometry(450, 530, 310, 90)
        Btn_registro_R.setStyleSheet("color: black;" "background-color: #adc178;")
        Btn_registro_R.clicked.connect(registrar)
        MainWindow_Register.setCentralWidget(ventana_registro)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Registro_Window = QMainWindow()
    ui = RegisterWindow()
    ui.setupUi(Registro_Window)
    Registro_Window.show()
    sys.exit(app.exec_())
