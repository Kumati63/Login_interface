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
    while True:
        rut = input("Ingrese un RUT: ")
        if Varios.valida_rut(rut):
            break
        else:
            print("\nEl RUT ingresado no es Válido :(")
    # Se da inicio a la solicitud de los datos del uauario
    nombre = input("Ingrese su Nommbre: ")
    apellido = input("Ingrese su Apellido: ")
    nombreUsuario = input("Ingrese nombre de usuario: ")
    rut = input("Ingrese su RUT, solo números")
    rol = int(input("Ingrese su rol"))
    email = input("ngrese su Correo Electronico")
    contraseña = input("Ingrese su contraseña")
    # Creamos ao objeto de tipo Usuario
    usu = Usuarios.Usuarios(nombre, apellido , nombreUsuario, rut, rol, email, contraseña)
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
    print("ID\tNombre\t\tApellido\tnombreUsuario\trut\t\t\t\trol\t\t\temail\t\t\t\tcontraseña")
    for dato in datos:
        print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".
              format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))


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
    print("ID                   {}".format(dato[0]))
    print("Nombre               {}".format(dato[1]))
    print("Apellido             {}".format(dato[2]))
    print("nombreUsuario        {}".format(dato[3]))
    print("rut                  {}".format(dato[4]))
    print("rol                  {}".format(dato[5]))
    print("email                {}".format(dato[6]))
    print("contraseña           {}".format(dato[7]))

    input("\nPresione Enter para continuar")


def mostrarParcial():
    os.system('cls')
    print("=========================")
    print("    MOSTRAR PARCIAL")
    print("=========================")
    cant = int(input("Ingrese Cantidad de Datos a Mostrar: "))
    datos = DAO.CRUDUsuario.mostrarParcial(cant)
    print("ID\tNombre\t\tApellido\tnombreUsuario\trut\t\t\t\trol\t\t\temail\t\t\t\tcontraseña")
    for dato in datos:
        print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t\t{}\t\t\t{}\t\t\t{}".
              format(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5], dato[6], dato[7]))


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
    print("Nombre               :{}".format(dato[1]))
    op = input("Desea Cambiar el Nombre [si-no]:")
    if op.lower() == "si":
        nombreNuevo = input("Ingrese Nombre: ")
        listanuevos.append(nombreNuevo)
    else:
        listanuevos.append(dato[1])
    # Cambiar Apellido
    print("Apellido             :{}".format(dato[2]))
    op = input("Desea Cambiar el Apellido [si-no]:")
    if op.lower() == "si":
        apellidoNuevo = input("Ingrese Apellido: ")
        listanuevos.append(apellidoNuevo)
    else:
        listanuevos.append(dato[2])

    # Modificar Edad
    print("Nombre Usuario               :{}".format(dato[3]))
    op = input("Desea Cambiar el Nombre Usuario [si-no]:")
    if op.lower() == "si":
        NombreUsuarionueva = input("Ingrese Nombre Usuario: ")
        listanuevos.append(NombreUsuarionueva)
    else:
        listanuevos.append(dato[3])
    # Modificar Genero
    print("rut               :{}".format(dato[4]))
    op = input("Desea Cambiar el rut [si-no]:")
    if op.lower() == "si":
        rutNuevo = input("Ingrese rut: ")
        listanuevos.append(rutNuevo)
    else:
        listanuevos.append(dato[4])

    # Modificar CorreoElectronico
    print("rol               :{}".format(dato[5]))
    op = input("Desea Cambiar el rol [si-no]:")
    if op.lower() == "si":
        rolNuevo = input("Ingrese CorreoElectronico: ")
        listanuevos.append(rolNuevo)
    else:
        listanuevos.append(dato[5])

    # Modificar Telefono
    print("CorreoElectronico               :{}".format(dato[6]))
    op = input("Desea Cambiar el Telefono [si-no]:")
    if op.lower() == "si":
        emailNuevo = input("Ingrese email: ")
        listanuevos.append(emailNuevo)
    else:
        listanuevos.append(dato[6])

        # Modificar contraseña
    print("contraseña               :{}".format(dato[6]))
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