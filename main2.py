#INTEGRANTES - GRUPO 11
#GOYA GILER DAYANA DENISSE
#LUCAS PEZO KENNYA
#LUNA MERA JORGE ANDRES


import sys

from PySide6.QtWidgets import QApplication
from servicio.persona_principal import PersonaPrincipal

app = QApplication()
vtn_principal = PersonaPrincipal()
vtn_principal.show()
sys.exit(app.exec())