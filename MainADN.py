import Modelo.CRUDADN
import Presentador.Varios
from Presentador import Conexion, Varios, ADN
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
    print("==================================================")
    print(" 1.- INGRESAR DATOS SOBRE EL ADN")
    print("==================================================")

    # Se da inicio a la solicitud de los datos del uauario
    Id_ADN = input("Ingrese el id del adn: ")
    Secuencia_ADN = input("Ingrese la secuencia de adn correspondiente: ")
    # Creamos ao objeto de tipo Usuario
    usu = ADN.ADN(Id_ADN, Secuencia_ADN)
    # Solicitar al CRUD que realice la inserción
    Modelo.CRUDADN.ingresar(usu)


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
    datos = Modelo.CRUDADN.mostrarTodos()
    print("ID\tID del ADN\t\tSecuencia de ADN")
    for dato in datos:
        print("{}\t{}\t\t{}".format(dato[0], dato[1], dato[2]))


def mostrarUno():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR UNO")
    print("=========================")
    idADN = int(input("Ingrese el id del ADN a Consultar: "))
    dato = Modelo.CRUDADN.mostrarParticular(idADN)
    print("=========================")
    print("   DATOS DEL ADN")
    print("=========================")
    print("ID                        {}".format(dato[0]))
    print("ID del ADN                {}".format(dato[1]))
    print("Secuencia del ADN         {}".format(dato[2]))


    input("\nPresione Enter para continuar")


def mostrarParcial():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR PARCIAL")
    print("=========================")
    cant = int(input("Ingrese Cantidad de Datos a Mostrar: "))
    datos = Modelo.CRUDADN.mostrarParcial(cant)
    print("ID\tID del ADN\t\tSecuencia de ADN")
    for dato in datos:
        print("{}\t{}\t\t{}".format(dato[0], dato[1], dato[2]))


def modificarDatos():
    os.system('cls')
    listanuevos = []
    print("=========================")
    print("    MODIFICAR DATOS")
    print("=========================")
    mostrarTodos()
    idMod = int(input("\nIngrese el ID del ADN a Modificar: "))
    dato = Modelo.CRUDADN.mostrarParticular(idMod)

    print("Id ADN                   :{}".format(dato[0]))
    listanuevos.append(dato[0])
    # Cambiar Nombre
    print("ID del ADN               :{}".format(dato[1]))
    op = input("Desea Cambiar el ID [si-no]:")
    if op.lower() == "si":
        IDNuevo = input("Ingrese nuevo ID: ")
        listanuevos.append(IDNuevo)
    else:
        listanuevos.append(dato[1])
    # Cambiar Apellido
    print("Apellido             :{}".format(dato[2]))
    op = input("Desea Cambiar la secuencia de ADN [si-no]:")
    if op.lower() == "si":
        SecuenciaNuevo = input("Ingrese la nueva secuencia: ")
        listanuevos.append(SecuenciaNuevo)
    else:
        listanuevos.append(dato[2])


    # Fecha y la Hora
    listanuevos.append(Presentador.Varios.fecha_hoy())
    listanuevos.append(Presentador.Varios.hora())
    Modelo.CRUDADN.modificar(listanuevos)


def eliminarDatos():
    os.system('cls')
    print("=========================")
    print("    ELIMINAR ADN")
    print("=========================")
    mostrarTodos()
    idEliminar = int(input("Ingrese Id de ADN a Eliminar: "))
    Modelo.CRUDADN.eliminar(idEliminar)


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
