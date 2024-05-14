from Presentador.Conexion import Conexion
# Datos de conexion hacia la BD
host = 'localhost'
user = 'root'
password = ''
db = 'proyecto_agil'

# Crear una función para insertar datos en la tabla usuario


def ingresar(nombre_virus, Secuencia_ADN):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO ADN (NombreVirus, Secuencia_ADN) VALUES ('{}', '{}')".format(nombre_virus, Secuencia_ADN)
        con.ejecuta_query(sql)
        con.commit()
        print("\nDatos insertados con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error al insertar en: {}".format(e))
        con.rollback()


def mostrarTodos():
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from ADN"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()  # Esto devuelve todas las consultas/datos
        con.desconectar()
        return datos
    except Exception as e:
        print("Erorr al Mostrar Todos:{}".format(e))


def MostrarParticular(id):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from ADN where idADN = {}".format(id)
        cursor = con.ejecuta_query(sql)
        dato = cursor.fetchone()  # Esto devuelve solo un
        con.desconectar()
        return dato
    except Exception as e:
        print("Error al Mostrar uno:{}".format(e))


def mostrarParcial(cant):
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from ADN"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size=cant)
        con.desconectar()
        return datos
    except Exception as e:
        print("Error en Mostrar Parcial:{}".format(e))


def modificar(usu):
    try:
        con = Conexion(host, user, password, db)
        sql = "INSERT INTO ADN SET Id_ADN = '{}',Secuencia_ADN = '{}' where idADN  = {}". \
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
        sql = "delete from ADN where idADN  = {}".format(id)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nADN Eliminado con Éxito :)")
        con.desconectar()
    except Exception as e:
        print("Error al Eliminar: {}".format(e))
