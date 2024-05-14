from DTO.Conexion import Conexion

# Datos de conexion hacia la BD
host = 'localhost'
user = 'root'
password = ''
db = 'sistema_yury'

# Crear una función para insertar datos en la tabla usuario


def ingresar(usu):
    try:
        # genrar una conexion hacia la BD
        con = Conexion(host, user, password, db)
        # print("Estado CON:{}".format(con))
        # Se cea la Query ara hacer la inserción de un Usuario
        sql = "INSERT INTO usuarios SET nombre = '{}', apellido = '{}', nombreUsuario = '{}', " \
            "rut = '{}', rol = '{}', email = '{}', contraseña = '{}'".\
            format(usu.nombre, usu.apellido , usu.nombreUsuario, usu.rut, usu.rol, usu.email, usu.contraseña)
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
        sql = "select * from usuarios"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()  # Esto devuelve todas las consultas/datos
        con.desconectar()
        return datos
    except Exception as e:
        print("Erorr al Mostrar Todos:{}".format(e))


def mostrarParticular(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from usuarios where idUsuario = {}".format(id)
        cursor = con.ejecuta_query(sql)
        dato = cursor.fetchone()  # Esto devuelve solo un
        con.desconectar()
        return dato
    except Exception as e:
        print("Error al Mostrar uno:{}".format(e))


def mostrarParcial(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from usuarios"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size=cant)
        con.desconectar()
        return datos
    except Exception as e:
        print("Error en Mostrar Parcial:{}".format(e))


def modificar(usu):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO usuarios SET nombre = '{}', apellido = '{}', nombreUsuario = '{}', " \
            "rut = '{}', rol = '{}', email = '{}', contraseña = '{}' where idUsuario  = {}". \
            format(usu[1], usu[2], usu[3], usu[4], usu[5], usu[6], usu[7], usu[0])
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
        sql = "delete from usuarios where idUsuario  = {}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nUsuario Eliminado con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error al Eliminar: {}".format(e))
