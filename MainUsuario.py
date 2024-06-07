import DAO.CRUDUsuario
import DTO.Varios
from DTO import Conexion, Varios, usuario
import os


def menuPrincipal():
    os.system('cls')
    print("Fecha:{} - Hora:{}".format(Varios.fecha_hoy(), Varios.hora()))
    print("=========================")
    print("    MENÚ PRINCIPAL")
    print("=========================")
    print("   1.- (C) INGRESAR")
    print("   2.- (R) MOSTRAR")
    print("   3.- (U) ACTUALIZAR")
    print("   4.- (D) ELIMINAR")
    print("   5.- (E) SALIR")
    print("=========================")


def ingresarDatos():
    os.system('cls')
    print("=========================")
    print(" 1.- INGRESAR DATOS USUARIO")
    print("=========================")
    # Se da inicio a la solicitud de los datos del uauario
    nombre = input("Ingrese su Nombre Completo: ")
    email = input("ngrese su Correo Electronico")
    while True:
        contraseña = input("Ingrese su contraseña")
        contraseña2 = input("Repita su contraseña")
        if (contraseña == contraseña2):
            password = contraseña
            break
        else:
            print("contraseñas no coinciden")

    estado = 1

    # Creamos al objeto de tipo Usuario
    usu = usuario.usuario(nombre, email, password, estado)
    # Solicitar al CRUD que realice la inserción
    DAO.CRUDUsuario.ingresar(usu)


def menuMostrar():
    os.system('cls')
    print("Fecha:{} - Hora:{}".format(Varios.fecha_hoy(), Varios.hora()))
    print("=========================")
    print("    MENÚ MOSTRAR")
    print("=========================")
    print("   1.- Mostrar Todos")
    print("   2.- Mostrar Uno")
    print("   3.- Mostrar Parcial")
    print("   4.- Volver")
    print("=========================")


def mostrarTodos():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR TODOS")
    print("=========================")
    datos = DAO.CRUDUsuario.mostrarTodos()
    print("ID\t\tNombre Completo\tEmail\tpassword\t\t\t\testado")
    for dato in datos:
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}".
              format(dato[0], dato[1], dato[2], dato[3], dato[4]))


def mostrarUno():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR UNO")
    print("=========================")
    idUsuario = int(input("Ingrese Id Usuarioa a Consultar: "))
    dato = DAO.CRUDUsuario.mostrarParticular(idUsuario)
    print("=========================")
    print("   DATOS DEL USUARIO")
    print("=========================")
    print("ID                       {}".format(dato[0]))
    print("Nombre Completo          {}".format(dato[1]))
    print("Email                    {}".format(dato[2]))
    print("password                 {}".format(dato[3]))
    print("estado                   {}".format(dato[4]))

    input("\nPresione Enter para continuar")


def mostrarParcial():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR PARCIAL")
    print("=========================")
    cant = int(input("Ingrese Cantidad de Datos a Mostrar: "))
    datos = DAO.CRUDUsuario.mostrarParcial(cant)
    print("ID\t\tNombre Completo\tEmail\tpassword\t\t\t\testado")
    for dato in datos:
        print("{}\t\t{}\t\t{}\t\t{}\t\t{}".
              format(dato[0], dato[1], dato[2], dato[3], dato[4]))


def modificarDatos():
    os.system('cls')
    listanuevos = []
    print("=========================")
    print("    MODIFICAR DATOS")
    print("=========================")
    mostrarTodos()
    idMod = int(input("\nIngrese un IdUsuario a Modificar: "))
    dato = DAO.CRUDUsuario.mostrarParticular(idMod)

    print("Id Usuario                   :{}".format(dato[0]))
    listanuevos.append(dato[0])
    # Cambiar Nombre
    print("Nombre Completo          :{}".format(dato[1]))
    op = input("Desea Cambiar el Nombre [si-no]:")
    if op.lower() == "si":
        nombreNuevo = input("Ingrese Nombre: ")
        listanuevos.append(nombreNuevo)
    else:
        listanuevos.append(dato[1])

    # Modificar Edad
    print("Nombre Email               :{}".format(dato[2]))
    op = input("Desea Cambiar el Email [si-no]:")
    if op.lower() == "si":
        NombreUsuarionueva = input("Ingrese Email: ")
        listanuevos.append(NombreUsuarionueva)
    else:
        listanuevos.append(dato[3])

        # Modificar contraseña
    print("contraseña               :{}".format(dato[3]))
    op = input("Desea Cambiar la contraseña [si-no]:")
    if op.lower() == "si":
        contraseñaNuevo = input("Ingrese contraseña: ")
        listanuevos.append(contraseñaNuevo)
    else:
        listanuevos.append(dato[6])


    # Fecha y la Hora
    listanuevos.append(DTO.Varios.fecha_hoy())
    listanuevos.append(DTO.Varios.hora())
    DAO.CRUDUsuario.modificar(listanuevos)


def eliminarDatos():
    os.system('cls')
    print("=========================")
    print("    ELIMINAR USUARIO")
    print("=========================")
    mostrarTodos()
    idEliminar = int(input("Ingrese Id Usuario a Eliminar: "))
    DAO.CRUDUsuario.eliminar(idEliminar)


def mostrar():
    while True:
        menuMostrar()
        op2 = int(input("Ingrese una Opción: "))
        if op2 == 1:
            mostrarTodos()
        elif op2 == 2:
            mostrarUno()
        elif op2 == 3:
            mostrarParcial()
        if op2 == 4:
            break
        else:
            print("Opción fuera de Rango :(")


while True:
    menuPrincipal()
    op = int(input("Ingrese una Opción: "))
    if op == 1:
        ingresarDatos()
    elif op == 2:
        mostrar()
    elif op == 3:
        modificarDatos()
    elif op == 4:
        eliminarDatos()
    if op == 5:
        op2 = input("Desea Salir[SI/NO]: ")
        if op2.upper() == "SI":
            exit()
    else:
        print("Opción Fuera de Rango :(")