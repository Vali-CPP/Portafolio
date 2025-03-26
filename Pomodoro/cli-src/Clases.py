import time, os
import pygame as pg
import Funciones as func

direccion_script = os.path.dirname(__file__)

class Sonido:
    def __init__(self, objeto_sonido = None):
                self.sonido = objeto_sonido

    def reproducir(self):
        if self.sonido:
            self.sonido.play(-1)

    def pausar(self):
        if self.sonido:
            self.sonido.stop()

    def cambiar(self, objeto_sonido):
        self.sonido = objeto_sonido

class Pomodoro:
    def __init__(self, t_concentracion = 25, t_descanso = 5, n_ciclos = 3, direccion_a_alarma = os.path.join(direccion_script, "Audio/.Alarma.wav")):
        self.t_concentracion = t_concentracion
        self.t_descanso = t_descanso
        self.n_ciclos = n_ciclos
        self.alarma = pg.mixer.Sound(direccion_a_alarma)
        self.tiempo_restante_actual = int()

    def definir_ciclos(self):
        self.ciclos = list()

        for i in range(0, self.n_ciclos):
            self.ciclos.append(["Concentracion", self.t_concentracion])
            self.ciclos.append(["Descanso", self.t_descanso])

    def pasar_ciclo(self):
        self.ciclos = self.ciclos[1:]
        self.n_ciclos -= 1

    def get_ciclo_actual(self):

        if len(self.ciclos) < 1:
            return False

        return self.ciclos[0]

    def temporizador(self, etapa, duracion_min):

        duracion_seg = int(duracion_min * 60)

        for restante in range(duracion_seg, 0, -1):
            self.tiempo_restante_actual = restante / 60
            print("\r")
            hr, resto = divmod(restante, 3600) #divmod devuelve una tupla del tipo (a/b, a%b)
            min, seg = divmod(resto, 60) #divmod devuelve una tupla del tipo (a/b, a%b)
            print("Tiempo restante de {} {:0>2}:{:0>2}:{:0>2}".format(etapa.lower(), hr, min, seg), end="")
            time.sleep(1)
            func.limpiar_pantalla()

    def sonar_alarma(self):
        self.alarma.play()

    def get_tiempo_restante_actual(self):
        return self.tiempo_restante_actual
