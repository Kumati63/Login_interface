from Presentador.Conexion import Conexion
from Presentador.Banco import Banco

# Datos de conexión hacia la BD
host = 'localhost'
user = 'root'
password = ''
db = 'proyecto_agil'


def ingresar_direccion_de_archivo(direccion_archivo):
    con = None
    try:
        # Crear una instancia de la clase Banco
        banco = Banco(direccionArchivo=host)
        con = Conexion(banco.direccionArchivo, user, password, db)
        sql = "INSERT INTO banco_de_muestras (direccionArchivo) VALUES (%s)"
        con.ejecuta_query(sql, (direccion_archivo,))
        con.commit()
        print("\nDirección de archivo insertada con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error al insertar la dirección de archivo en: {}".format(e))
        # Realizar rollback en caso de error
        con.rollback()