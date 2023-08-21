#INTEGRANTES - GRUPO 11
#GOYA GILER DAYANA DENISSE
#LUCAS PEZO KENNYA
#LUNA MERA JORGE ANDRES


from PySide6 import QtGui
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from UI.vtn_principal import Ui_vtn_principal
from datos.estudiante_dao import EstudianteDao
from dominio.docente import Docente
from dominio.estudiante import Estudiante
from datetime import datetime, date


class PersonaPrincipal(QMainWindow):
    def __init__(self):
        super(PersonaPrincipal, self).__init__()
        self.ui = Ui_vtn_principal()
        self.ui.setupUi(self)
        self.ui.stb_estado.showMessage('BIENVENIDOS',2000)
        self.ui.btn_grabar.clicked.connect(self.grabar)
        self.ui.btn_buscar_cedula.clicked.connect(self.buscar_x_cedula)
        self.ui.btn_estatura.clicked.connect(self.calculos_estatura)
        self.ui.btn_peso.clicked.connect(self.calculos_peso)
        self.ui.btn_fecha_de_nacimiento.clicked.connect(self.calculos_fecha_de_nacimiento)
        self.ui.txt_cedula.setValidator(QtGui.QIntValidator())

        correo_exp = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9. -]+\[A-Z|a-z]{2,7}b'
        validator = QRegularExpressionValidator(correo_exp, self)
        self.ui.txt_email.setValidator(validator)

    def grabar(self):
            global respuesta
            tipo_persona = self.ui.cb_tipo_persona.currentText()
            if self.ui.txt_nombre.text() == ' ' or self.ui.txt_apellido.text() == ' ' \
                    or len(self.ui.txt_cedula.text())<10 or self.ui.txt_email.text() == ' ':
                print('Completar datos')
                QMessageBox.warning(self, 'Advertencia', 'Falta de llenar los datos obligatorios')
            else:
                persona = None
            if tipo_persona == 'Docente':
               persona = Docente()
               persona.nombre = self.ui.txt_nombre.text()
               persona.apellido = self.ui.txt_apellido.text()
               persona.cedula = self.ui.txt_cedula.text()
               persona.email = self.ui.txt_email.text()
               persona.estatura = self.ui.sp_estatura.text()
               persona.peso = self.ui.sp_peso.text()
               persona.fecha_nacimiento = self.ui.dateEdit_fecha_de_nacimiento.date().getDate()
            else:
               persona = Estudiante()
               persona.nombre = self.ui.txt_nombre.text()
               persona.apellido = self.ui.txt_apellido.text()
               persona.cedula = self.ui.txt_cedula.text()
               persona.email = self.ui.txt_email.text()
               persona.carrera = self.ui.txt_carrera.text()
               persona.estatura = self.ui.sp_estatura.text()
               persona.peso = self.ui.sp_peso.text()
               persona.fecha_nacimiento = self.ui.dateEdit_fecha_de_nacimiento.text()
               #insertar a la base de datos al estudiante
               respuesta = None
               respuesta = EstudianteDao.insertar_estudiante(persona)

            #archivo = None
            #try:
                #archivo = open("archivo.txt", mode="a")
                #archivo.write(persona.__str__())
                #archivo.write("\n")
            #except Exception as e:
                 #print("No se pudo grabar")
            #finally:
                #if archivo:
                   #archivo.close()
            if respuesta['exito']:
                self.ui.txt_nombre.setText('')
                self.ui.txt_apellido.setText('')
                self.ui.txt_cedula.setText('')
                self.ui.txt_email.setText('')
                self.ui.txt_carrera.setText('')
                self.ui.sp_estatura.setValue(0)
                self.ui.sp_peso.setValue(0)
                self.ui.stb_estado.showMessage('GRABADO CON ÉXITO', 2000)
            else:
                QMessageBox.critical(self, 'Error', respuesta['mensaje'])
    def buscar_x_cedula(self):
       cedula = self.ui.txt_cedula.text()
       e = Estudiante(cedula=cedula)
       e = EstudianteDao.seleccionar_por_cedula(e)
       self.ui.txt_nombre.setText(e.nombre)
       self.ui.txt_apellido.setText(e.apellido)
       self.ui.txt_email.setText(e.email)
       self.ui.txt_carrera.setText(e.carrera)
       self.ui.sp_estatura.setValue(e.estatura)
       self.ui.sp_peso.setValue(e.peso)
       self.ui.txt_fecha_de_nacimiento.setDate(e.fecha_de_nacimiento)
       self.ui.cb_tipo_persona.setCurrentText('Estudiante')

    def calculos_estatura(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_estaturas = 0
        estatura = []
        for estudiante in estudiantes:
            suma_estaturas += estudiante.estatura
            estatura.append(estudiante.estatura)
        promedio_estatura = suma_estaturas / cantidad_estudiantes
        estatura_minima = min(estatura)
        estatura_maxima = max(estatura)
        estatura.sort()
        mediana_estaturas = estatura[cantidad_estudiantes // 2]
        print('ESTADISTICA DESCRIPTIVA DE LA ESTATURA')
        print(f'Promedio de la estatura es: {promedio_estatura}')
        print(f'Mediana de estatura es: {mediana_estaturas}')
        print(f'Estatura mínima es: {estatura_minima}')
        print(f'Estatura máxima es: {estatura_maxima}')

        # MODA
        estaturas_frecuencia = {}
        max_frecuencia = 0
        moda = []

        for estatura in estatura:
            if estatura in estaturas_frecuencia:
                estaturas_frecuencia[estatura] += 1
            else:
                estaturas_frecuencia[estatura] = 1

            if estaturas_frecuencia[estatura] > max_frecuencia:
                max_frecuencia = estaturas_frecuencia[estatura]
                moda = [estatura]
            elif estaturas_frecuencia[estatura] == max_frecuencia and estatura not in moda:
                moda.append(estatura)

        print(f'Moda de  estatura es: {moda}')

    def calculos_peso(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        cantidad_estudiantes = len(estudiantes)
        suma_peso = 0
        peso = []
        for estudiante in estudiantes:
            suma_peso += estudiante.peso
            peso.append(estudiante.peso)
        promedio_peso = suma_peso / cantidad_estudiantes
        peso_minimo = min(peso)
        peso_maximo = max(peso)
        peso.sort()
        mediana_peso = peso[cantidad_estudiantes // 2]
        print('ESTADISTICA DESCRIPTIVA DEL PESO')
        print(f'Promedio del peso es: {promedio_peso}')
        print(f'Mediana del peso es: {mediana_peso}')
        print(f'Peso mínimo es: {peso_minimo}')
        print(f'Peso máximo es: {peso_maximo}')

        # MODA
        peso_frecuencia = {}
        max_frecuencia = 0
        moda = []

        for peso in peso:
            if peso in peso_frecuencia:
                peso_frecuencia[peso] += 1
            else:
                peso_frecuencia[peso] = 1

            if peso_frecuencia[peso] > max_frecuencia:
                max_frecuencia = peso_frecuencia[peso]
                moda = [peso]
            elif peso_frecuencia[peso] == max_frecuencia and peso not in moda:
                moda.append(peso)
        print(f'Moda del peso es: {moda}')

    def calculos_fecha_de_nacimiento(self):
        estudiantes = EstudianteDao.seleccionar_estudiantes()
        edades = []
        for estudiante in estudiantes:
            fecha_de_nacimiento = estudiante.fecha_de_nacimiento
            edad = (datetime.now().date() - datetime.now().date()).days // 365
            edades.append(edad)

        cantidad_estudiantes = len(edades)
        promedio_edad = sum(edades) / cantidad_estudiantes
        edades.sort()
        mediana_edad = edades[cantidad_estudiantes // 2]

     #MODA
        edades_frecuencia = {}
        max_frecuencia = 0
        moda = []

        for edad in edades:
            if edad in edades_frecuencia:
                edades_frecuencia[edad] += 1
            else:
                edades_frecuencia[edad] = 1

            if edades_frecuencia[edad] > max_frecuencia:
                max_frecuencia = edades_frecuencia[edad]
                moda = [edad]
            elif edades_frecuencia[edad] == max_frecuencia and edad not in moda:
                moda.append(edad)

        edad_minima = min(edades)
        edad_maxima = max(edades)

        print('ESTADISTICA DESCRIPTIVA DE LA FECHA DE NACIMIENTO')
        print(f'Promedio de edad es: {promedio_edad:.2f}')
        print(f'Mediana de edad es: {mediana_edad}')
        print(f'Moda de edad es: {moda}')
        print(f'Edad mínima es: {edad_minima}')
        print(f'Edad máxima es: {edad_maxima}')




