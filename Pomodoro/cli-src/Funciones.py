import os, time
import pygame as pg
from Clases import *

direccion_script = os.path.dirname(__file__)

def limpiar_pantalla():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def validacion_int(mensaje_peticion, mensaje_de_error = "Caracter invalido", limite_inferior = -999, limite_superior = 999):
    while True:
        try:
            int_validado = int(input(mensaje_peticion))

            if int_validado <= limite_inferior:
                print("El numero es muy bajo")

            elif int_validado > limite_superior:
                print("El numero es muy alto")

            else:
                return int_validado

        except ValueError:
            print(mensaje_de_error)

def menu_inicial():

    limpiar_pantalla()

    return validacion_int("1)Iniciar un pomodoro\n2)Salir\n: ", "Numero invalido", 0, 2)

def elegir_ruido():

    limpiar_pantalla()

    dict_sonidos = {"Ninguno" : None}
    contador = 1

    print("Indica el ruido blanco que deseas reproducir:")

    for sonido in os.listdir(os.path.join(direccion_script, "Audio")):
        sonido_sin_ext = sonido[:-4]
        if not sonido.startswith("."):
            dict_sonidos.setdefault(sonido_sin_ext, sonido)

    list_sonidos = list(dict_sonidos.keys())

    for sonido in list_sonidos:
        print("{:0>2} - {}".format(contador, sonido))
        contador += 1

    decision = validacion_int("?: ", "Elige un numero que este disponible", 0, len(dict_sonidos)) - 1


    if decision != 0:
        return pg.mixer.Sound(os.path.join(direccion_script, "Audio", "{}".format(dict_sonidos[list_sonidos[decision]])))
    else:
        return None

def crear_pomo():

    t_concentracion = validacion_int("Ingrese el tiempo de concentracion deseado: ", "Tiempo invalido, debe ser mayor que cero", 0)
    t_descanso = validacion_int("Ingrese el tiempo de descanso deseado: ", "Tiempo invalido, debe ser mayor que cero", 0)
    n_ciclos = validacion_int("Ingrese el numero de ciclos a completar: ", "Tiempo invalido, el numero de ciclos tiene que ser mayor a cero", 0)

    p = Pomodoro(t_concentracion, t_descanso, n_ciclos)

    return p
