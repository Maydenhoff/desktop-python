import sqlite3 


#atrivuto conexion base de datos
class ConexionDB:
    def __init__(self):
        self.base_datos = "database/peliculas.db"
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()
