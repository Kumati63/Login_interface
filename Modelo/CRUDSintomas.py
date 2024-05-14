from Presentador.Conexion import Conexion
# Datos de conexion hacia la BD
host = 'localhost'
user = 'root'
password = ''
db = 'proyecto_agil'

# Crear una función para insertar datos en la tabla usuario


def ingresar(nombre_virus, sintoma_valor):
    try:
        # Generar una conexión hacia la BD
        con = Conexion(host, user, password, db)
        # Se crea la Query para hacer la inserción de un Síntoma
        sql = "INSERT INTO Sintomas (nombre, sintoma) VALUES (%s, %s)"
        # Ejecutar la Query para hacer la inserción
        con.ejecuta_query(sql, (nombre_virus, sintoma_valor))
        # Debemos actualizar
        con.commit()
        # Enviar mensaje de inserción exitosa
        print("\nDatos insertados con Éxito :)")
        # Debemos soltar la conexión
        con.desconectar()

    except Exception as e:
        print("Error al insertar en:{}".format(e))
        con.rollback()

def mostrarTodos():
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from Sintomas"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("Error al Mostrar Todos:{}".format(e))


def MostrarParticular(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from Sintomas where idSintomas = {}".format(id)
        cursor = con.ejecuta_query(sql)
        dato = cursor.fetchone()  # Esto devuelve solo un
        con.desconectar()
        return dato
    except Exception as e:
        print("Error al Mostrar uno:{}".format(e))


def mostrarParcial(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from Sintomas"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size=cant)
        con.desconectar()
        return datos
    except Exception as e:
        print("Error en Mostrar Parcial:{}".format(e))


def modificar(usu):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO Sintomas SET nombre = '{}',sintoma = '{}' where idSintomas  = {}". \
            format(usu[1],usu[2], usu[0])
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nDatos Modificados con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error al Modificar: {}".format(e))
        con.rollback()


def eliminar(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "delete from Sintomas where idSintomas  = {}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nADN Eliminado con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error al Eliminar: {}".format(e))
