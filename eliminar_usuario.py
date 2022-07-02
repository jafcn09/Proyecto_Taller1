from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QIcon, QFont
from os import remove
import os
class EliminarUsuariosWindows(object):
    def setupUi(self, MainWindowsEliminarUsuarios):
        MainWindowsEliminarUsuarios.setWindowTitle("ELIMINAR USUARIOS")
        MainWindowsEliminarUsuarios.setWindowIcon(QIcon("ShirtIcon.png"))
        MainWindowsEliminarUsuarios.setStyleSheet("background-color: 	#FFA07A;")
        MainWindowsEliminarUsuarios.setFixedSize(800, 500)
        ventana_eliminar_usuario = QWidget(MainWindowsEliminarUsuarios)
        # ETIQUETAS DE LA VENTANA
        label_miperfil = QLabel("<b>Mi Perfil</b>", ventana_eliminar_usuario)
        label_miperfil.setGeometry(310, 50, 600, 50)
        label_miperfil.setFont(QFont('Arial', 20))
        label_miperfil.setStyleSheet("color: #fff")

        label_informaciondelusuario = QLabel("INFORMACIÓN DEL USUARIO", ventana_eliminar_usuario)
        label_informaciondelusuario.setGeometry(200, 120, 500, 30)
        label_informaciondelusuario.setFont(QFont('Arial', 10))
        label_informaciondelusuario.setStyleSheet("color: #fff")

        label_dni = QLabel("DNI:", ventana_eliminar_usuario)
        label_dni.setGeometry(100, 180, 120, 30)
        label_dni.setFont(QFont('Arial', 10))
        label_dni.setStyleSheet("color: #fff")

        label_nombre = QLabel("Nombre:", ventana_eliminar_usuario)
        label_nombre.setGeometry(100, 240, 120, 30)
        label_nombre.setFont(QFont('Arial', 10))
        label_nombre.setStyleSheet("color: #fff")

        label_apellidos = QLabel("Apellidos:", ventana_eliminar_usuario)
        label_apellidos.setGeometry(100, 300, 100, 30)
        label_apellidos.setFont(QFont('Arial', 10))
        label_apellidos.setStyleSheet("color: #fff")




        archivo = open("Registro.txt", "r")
        #if os.path.exists("productos.txt"):
         #  archivo = os.remove("productos.txt")
          # print("Este archivo se va eliminar")
        #else:
         #      print("No se encuentra ningun archivo")
        content = archivo.readlines()
        # CAJAS DE TEXTO DE LA VENTANA
        cajatexto_dni = QLineEdit(ventana_eliminar_usuario)
        cajatexto_dni.setPlaceholderText(content[0])
        cajatexto_dni.setGeometry(220, 180, 350, 25)
        cajatexto_dni.setStyleSheet("color: black;" "background-color: white")

        cajatexto_nombre = QLineEdit(ventana_eliminar_usuario)
        cajatexto_nombre.setPlaceholderText(content[1])
        cajatexto_nombre.setGeometry(220, 240, 350, 25)
        cajatexto_nombre.setStyleSheet("color: black;" "background-color: white")

        cajatexto_apellidos = QLineEdit(ventana_eliminar_usuario)
        cajatexto_apellidos.setPlaceholderText(content[2])
        cajatexto_apellidos.setGeometry(220, 300, 350, 25)
        cajatexto_apellidos.setStyleSheet("color: black;" "background-color: white")




        archivo.close()

        boton_eliminar_usuarios = QPushButton("Eliminar", ventana_eliminar_usuario)
        boton_eliminar_usuarios.setGeometry(420, 400, 80, 30)
        boton_eliminar_usuarios.setStyleSheet("color: black;" "background-color: #FFCA33")
        MainWindowsEliminarUsuarios.setCentralWidget(ventana_eliminar_usuario)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    Usuario_Eliminado = QMainWindow()
    ui = EliminarUsuariosWindows()
    ui.setupUi(Usuario_Eliminado)
    Usuario_Eliminado.show()
    sys.exit(app.exec_())