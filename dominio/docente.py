#INTEGRANTES - GRUPO 11
#GOYA GILER DAYANA DENISSE
#LUCAS PEZO KENNYA
#LUNA MERA JORGE ANDRES
import datetime

from dominio.persona import Persona
class Docente(Persona):

    contador_docente = 0

    def __init__(self ,cedula :str=None ,nombre :str=None ,apellido :str=None ,email :str=None ,telefono :str=None ,direccion :str=None
                 ,numero_libros :int=0 ,activo :bool=True ,carrera :str=None, estatura :str=None, peso :str=None, titulo_3er_nivel :str=None ,titulo_4to_nivel :str=None):

        Docente.contador_docente +=1
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._telefono = telefono
        self._direccion = direccion
        self._numero_libros = numero_libros
        self._activo = activo
        self._carrera = carrera
        self._estatura = estatura
        self._peso = peso
        self._id = Docente.contador_docente
        self._titulo_3er_nivel = titulo_3er_nivel
        self._titulo_4to_nivel = titulo_4to_nivel
        super(Docente, self).__init__(cedula = cedula, nombre = nombre, apellido = apellido, email = email,
                                      telefono = telefono, direccion = direccion, numero_libros = numero_libros,
                                      activo = activo, carrera = carrera, estatura = estatura, peso=peso)


    def __str__ (self):
        return f' Docente : {self.__dict__.__str__()}'


    @property
    def id (self):
        return self._id


    @property
    def titulo_3er_nivel(self):
        return self._titulo_3er_nivel
    @titulo_3er_nivel.setter
    def titulo_3er_nivel(self, titulo_3er_nivel):
        self._titulo_3er_nivel = titulo_3er_nivel

    @property
    def titulo_4to_nivel(self):
        return self._titulo_4to_nivel
    @titulo_4to_nivel.setter
    def titulo_4to_nivel(self, titulo_4to_nivel):
        self._titulo_4to_nivel = titulo_4to_nivel

    @classmethod
    def pedir_libro(self) -> bool:
        pass

    @classmethod
    def devolver_libro(self) -> bool:
        pass


if __name__ == '__main__':
     d1 = Docente(cedula = '1304322652', nombre = 'julia', apellido= 'rivera', email='julia@gmail.com', telefono='09904789', direccion='guasmo', numero_libros=0, activo=True, carrera='GIG', titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')
     d2 = Docente(cedula = '0937482947', nombre = 'EDGAR', apellido= 'Cardenas', email='cardenas@gmail.com', telefono='09272894', direccion='alborada', numero_libros=0, activo=True, carrera='GIG', titulo_3er_nivel='ING', titulo_4to_nivel=',MAE')

     print(d1)
     print(d2)