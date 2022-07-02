from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont

class ProfileWindow(object):
    def setupUI(self, MainWindow_perfil):
        def guardar_nuevos_datos():
            Registro = open("Registro.txt", "w")
            Registro.write(cajatexto_nombre.text()
                           +"\n"+cajatexto_apellido.text()
                           +"\n"+cajatexto_dni.text()
                           +"\n"+content[3]
                           +content[4])
            Registro.close()
            label_guardar_cancelar.setGeometry(280, 450, 600, 30)
            label_guardar_cancelar.setText("Se guardaron los datos")
        def cancelar_nuevos_datos():
            Registro = open("Registro.txt", "w")
            Registro.write(content[0]+content[1]+content[2]+content[3]+content[4])
            Registro.close()
            label_guardar_cancelar.setGeometry(240, 450, 600, 30)
            label_guardar_cancelar.setText("Se restableció a la versión anterior")

        MainWindow_perfil.setWindowTitle("Mi Perfil")
        MainWindow_perfil.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindow_perfil.setStyleSheet("background-color: #ae2012;")
        MainWindow_perfil.resize(800, 500)
        ventana_perfil = QWidget(MainWindow_perfil)
        #ETIQUETAS DE LA VENTANA
        label_miperfil = QLabel("<b>Mi Perfil</b>", ventana_perfil)
        label_miperfil.setGeometry(310, 50, 600, 50)
        label_miperfil.setFont(QFont('Arial', 20))
        label_miperfil.setStyleSheet("color: #fff")

        label_informaciondelusuario = QLabel("INFORMACIÓN DEL USUARIO", ventana_perfil)
        label_informaciondelusuario.setGeometry(200, 120, 500, 30)
        label_informaciondelusuario.setFont(QFont('Arial', 10))
        label_informaciondelusuario.setStyleSheet("color: #fff")

        label_nombre = QLabel("Nombres:", ventana_perfil)
        label_nombre.setGeometry(100, 180, 120, 30)
        label_nombre.setFont(QFont('Arial', 10))
        label_nombre.setStyleSheet("color: #fff")

        label_apellido = QLabel("Apellidos:", ventana_perfil)
        label_apellido.setGeometry(100, 240, 120, 30)
        label_apellido.setFont(QFont('Arial', 10))
        label_apellido.setStyleSheet("color: #fff")

        label_dni = QLabel("DNI:", ventana_perfil)
        label_dni.setGeometry(100, 300, 100, 30)
        label_dni.setFont(QFont('Arial', 10))
        label_dni.setStyleSheet("color: #fff")

        label_guardar_cancelar = QLabel("", ventana_perfil)
        label_guardar_cancelar.setGeometry(280, 450, 600, 30)
        label_guardar_cancelar.setFont(QFont('Arial', 8))

        archivo = open("Registro.txt", "r")
        content = archivo.readlines()
        archivo.close()
        #CAJAS DE TEXTO DE LA VENTANA
        cajatexto_nombre = QLineEdit(ventana_perfil)
        cajatexto_nombre.setPlaceholderText(content[0])
        cajatexto_nombre.setGeometry(220, 180, 350, 25)
        cajatexto_nombre.setStyleSheet("color: black;" "background-color: white")

        cajatexto_apellido = QLineEdit(ventana_perfil)
        cajatexto_apellido.setPlaceholderText(content[1])
        cajatexto_apellido.setGeometry(220, 240, 350, 25)
        cajatexto_apellido.setStyleSheet("color: black;" "background-color: white")

        cajatexto_dni = QLineEdit(ventana_perfil)
        cajatexto_dni.setPlaceholderText(content[2])
        cajatexto_dni.setGeometry(220, 300, 350, 25)
        cajatexto_dni.setStyleSheet("color: black;" "background-color: white")

        #BOTONES DE LA VENTANA
        boton_cancelar = QPushButton("Cancelar", ventana_perfil)
        boton_cancelar.setGeometry(270, 400, 120, 30)
        boton_cancelar.clicked.connect(cancelar_nuevos_datos)
        boton_cancelar.setStyleSheet("color: black;" "background-color: #999999")

        boton_guardar = QPushButton("Guardar", ventana_perfil)
        boton_guardar.setGeometry(420, 400, 120, 30)
        boton_guardar.setStyleSheet("color: black;" "background-color: #00ff00")
        boton_guardar.clicked.connect(guardar_nuevos_datos)
        btn_atras = QPushButton(ventana_perfil)
        btn_atras.setGeometry(490, 500, 120, 30)

        MainWindow_perfil.setCentralWidget(ventana_perfil)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Mi_perfil = QMainWindow()
    ui = ProfileWindow()
    ui.setupUI(Mi_perfil)
    Mi_perfil.show()
    sys.exit(app.exec_())
