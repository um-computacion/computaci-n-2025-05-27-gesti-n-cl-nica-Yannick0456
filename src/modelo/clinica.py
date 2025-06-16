from .paciente import Paciente
from .medico import Medico
from .turno import Turno
from .receta import Receta
from .historia_clinica import HistoriaClinica
from .excepciones import *
from datetime import datetime

class Clinica:
    def __init__(self):
        self.__pacientes = {}
        self.__medicos = {}
        self.__turnos = []
        self.__historias_clinicas = {}

    def agregar_paciente(self, paciente):
        dni = paciente.obtener_dni()
        if dni in self.__pacientes:
            raise Exception("Paciente ya registrado")
        self.__pacientes[dni] = paciente
        self.__historias_clinicas[dni] = HistoriaClinica(paciente)

    def agregar_medico(self, medico):
        matricula = medico.obtener_matricula()
        if matricula in self.__medicos:
            raise Exception("Médico ya registrado")
        self.__medicos[matricula] = medico
