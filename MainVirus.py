import DAO.CRUDVirus
import DTO.Varios
from DTO import Conexion, Varios, tipo_usuario
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
    nombreCientifico = input("Ingrese su Nombre Cientifico: ")
    nombre = input("Ingrese el nombre: ")
    fechaDesc = input("Ingrese fecha de descubrimiento: ")
    # Creamos ao objeto de tipo Usuario
    usu = Virus.Virus(nombreCientifico, nombre , fechaDesc)
    # Solicitar al CRUD que realice la inserción
    DAO.CRUDVirus.ingresar(usu)


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
    datos = DAO.CRUDVirus.mostrarTodos()
    print("ID\tnombreCientifico\t\tnombre\tfechaDesc")
    for dato in datos:
        print("{}\t{}\t\t{}\t\t{}".format(dato[0], dato[1], dato[2], dato[3]))


def mostrarUno():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR UNO")
    print("=========================")
    idUsuario = int(input("Ingrese Id Usuarioa a Consultar: "))
    dato = DAO.CRUDVirus.mostrarParticular(idUsuario)
    print("=========================")
    print("   DATOS DEL USUARIO")
    print("=========================")
    print("ID                   {}".format(dato[0]))
    print("Nombre Cientifico    {}".format(dato[1]))
    print("Nombre               {}".format(dato[2]))
    print("fecha Descubrimiento {}".format(dato[3]))

    input("\nPresione Enter para continuar")


def mostrarParcial():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR PARCIAL")
    print("=========================")
    cant = int(input("Ingrese Cantidad de Datos a Mostrar: "))
    datos = DAO.CRUDVirus.mostrarParcial(cant)
    print("ID\tnombreCientifico\t\tnombre\tfechaDesc")
    for dato in datos:
        print("{}\t{}\t\t{}\t\t{}".format(dato[0], dato[1], dato[2], dato[3]))


def modificarDatos():
    os.system('cls')
    listanuevos = []
    print("=========================")
    print("    MODIFICAR DATOS")
    print("=========================")
    mostrarTodos()
    idMod = int(input("\nIngrese un IdUsuario a Modificar: "))
    dato = DAO.CRUDVirus.mostrarParticular(idMod)

    print("Id Virus                     :{}".format(dato[0]))
    listanuevos.append(dato[0])

    # Cambiar Nombre Cientifico
    print("Nombre Cientifico            :{}".format(dato[1]))
    op = input("Desea Cambiar el Nombre Cientifico? [si-no]:")
    if op.lower() == "si":
        nombreCientificoNuevo = input("Ingrese Nombre: ")
        listanuevos.append(nombreCientificoNuevo)
    else:
        listanuevos.append(dato[1])

    # Cambiar nombre
    print("nombre                       :{}".format(dato[2]))
    op = input("Desea Cambiar el nombre? [si-no]:")
    if op.lower() == "si":
        nombreNuevo = input("Ingrese nombre: ")
        listanuevos.append(nombreNuevo)
    else:
        listanuevos.append(dato[2])

    # Modificar fecha Descubrimiento
    print("Nombre fechaDesc             :{}".format(dato[3]))
    op = input("Desea Cambiar la fecha de descubrimiento? [si-no]:")
    if op.lower() == "si":
        fechaDescnueva = input("Ingrese la fecha de descubrimiento: ")
        listanuevos.append(fechaDescnueva)
    else:
        listanuevos.append(dato[3])


    # Fecha y la Hora
    listanuevos.append(DTO.Varios.fecha_hoy())
    listanuevos.append(DTO.Varios.hora())
    DAO.CRUDVirus.modificar(listanuevos)


def eliminarDatos():
    os.system('cls')
    print("=========================")
    print("    ELIMINAR VIRUS")
    print("=========================")
    mostrarTodos()
    idEliminar = int(input("Ingrese Id VIRUS a Eliminar: "))
    DAO.CRUDVirus.eliminar(idEliminar)


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
