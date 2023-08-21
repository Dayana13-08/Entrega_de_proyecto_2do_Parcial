#INTEGRANTES - GRUPO 11
#GOYA GILER DAYANA DENISSE
#LUCAS PEZO KENNYA
#LUNA MERA JORGE ANDRES


from dominio.docente import Docente
from dominio.estudiante import Estudiante
from dominio.libro import Libro
from dominio.revista import Revista
from dominio.pedido import Pedido

d1 = Docente(cedula='1304322652', nombre='julia', apellido='rivera', email='julia@gmail.com', telefono='09904789',
             direccion='guasmo', numero_libros=0, activo=True, carrera='GIG', titulo_3er_nivel='ING',
             titulo_4to_nivel=',MAE')
d2 = Docente(cedula='0937482947', nombre='EDGAR', apellido='Cardenas', email='cardenas@gmail.com', telefono='09272894',
             direccion='alborada', numero_libros=0, activo=True, carrera='GIG', titulo_3er_nivel='ING',
             titulo_4to_nivel=',MAE')

print(d1)
print(d2)


# Estudiantes

e1 = Estudiante(cedula='0927287849', nombre='kennya', apellido='Lucas', email='kenial@gmail.com',
                    telefono='0960500255', direccion='guayaquil', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
e2 = Estudiante(cedula='0960277899', nombre='dayanna', apellido='Goya', email='dayanna@gmail.com',
                    telefono='1302483042', direccion='guayaquil', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)
e3 = Estudiante(cedula='0930621289', nombre='andres', apellido='luna', email='lunaandres@gmail.com',
                    telefono='0997993057', direccion='floresta', numero_libros=0, activo=True, carrera='GIG',
                    nivel=3)

print(e1)
print(e2)
print(e3)

libro4 = Libro(codigo='6', autor='PATICIA', titulo='CRONICAS DE MISTMANTLE', anio=2006, editorial='VILLEGAS EDITORIAL', disponible=True, cantidad_disponible=12,tipo_pasta='NORMAL')
print(libro4)

revista52 = Revista(codigo='245', autor='Alfonzo', titulo='Nutrición Hospitalaria', anio=2023, editorial='Citation Report.', disponible=True, cantidad_disponible=15,tipo='VIRTUAL')
print(revista52)

pedido1 = Pedido(id='0927287847', solicitante='kennya lucas', lista_material='estadisticas',
                 fecha_prestamo='06/Junio/2023', fecha_devolucion='15/Junio/2023')

print(pedido1)