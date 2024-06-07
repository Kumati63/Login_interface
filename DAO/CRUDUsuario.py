from DTO.Conexion import Conexion
from DTO.Varios import hash_md5

# Datos de conexion hacia la BD
host = 'localhost'
user = 'root'
password = ''
db = 'login_interface'

# Crear una función para insertar datos en la tabla usuario


def ingresar(usu):
    try:
        # genrar una conexion hacia la BD
        con = Conexion(host, user, password, db)
        # print("Estado CON:{}".format(con))
        # Se cea la Query ara hacer la inserción de un Usuario
        sql = "INSERT INTO usuario SET nombre_completo = '{}', email = '{}', password = '{}', estado = 1".\
            format(usu.nombre_completo, usu.email, hash_md5(usu.password), usu.estado)
        # Ejecutar la Query para hacer la inserción
        con.ejecuta_query(sql)
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
        sql = "select * from usuario"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()  # Esto devuelve todas las consultas/datos
        con.desconectar()
        return datos
    except Exception as e:
        print("Error al Mostrar Todos:{}".format(e))


def mostrarParticular(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from usuario where id_usuario = {}".format(id)
        cursor = con.ejecuta_query(sql)
        dato = cursor.fetchone()  # Esto devuelve solo un
        con.desconectar()
        return dato
    except Exception as e:
        print("Error al Mostrar uno:{}".format(e))


def mostrarParcial(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from usuario"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size=cant)
        con.desconectar()
        return datos
    except Exception as e:
        print("Error en Mostrar Parcial:{}".format(e))


def modificar(usu):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO usuario SET nombre_completo = '{}', email = '{}', " \
            "password = '{}', estado = 1 where id_usuario  = {}". \
            format(usu[1], usu[2], usu[3], usu[4], usu[0])
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
        sql = "delete from usuario where id_usuario  = {}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nUsuario Eliminado con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error al Eliminar: {}".format(e))
