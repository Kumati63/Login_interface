import hashlib
from datetime import datetime, date, time

def hash_md5(palabra):
    h = hashlib.md5()
    h.update(palabra.encode('utf-8'))
    return h.hexdigest()


def hash_sha256(palabra): #
    h = hashlib.sha256()
    h.update(palabra.encode('utf-8'))
    return h.hexdigest()


def fecha_hoy():
    fecha = datetime.now()
    fecha_ = "{}-{}-{}".format(fecha.year, fecha.month, fecha.day)
    return fecha_


def hora():
    hora = datetime.now()
    hora_ = "{}:{}:{}".format(hora.hour, hora.minute, hora.second)
    return hora_

def valida_rut(rut):
    caracteres = ".-"
    for x in range(len(caracteres)):
        rut = rut.replace(caracteres[x], "")

    rutsindigito = rut[:len(rut)-1]
    rutinvertido = rutsindigito[::-1]
    multi = 2
    sum = 0
    for i in range(0, len(rutinvertido)):
        if multi > 7:
            multi = 2
        sum += int(rutinvertido[i])*multi
        multi += 1

    dv = 11-(sum % 11)
    dvu = rut[-1:]
    if dv == 11:
        dv = 0
    if dv == 10:
        dv = "K"

    if str(dv) == dvu:
        return True
    else:
        return False
