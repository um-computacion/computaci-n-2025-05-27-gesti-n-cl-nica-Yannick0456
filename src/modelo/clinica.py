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

    def obtener_pacientes(self):
        return list(self.__pacientes.values())

    def obtener_medicos(self):
        return list(self.__medicos.values())

    def obtener_turnos(self):
        return list(self.__turnos)

    def obtener_historia_clinica(self, dni):
        if dni not in self.__historias_clinicas:
            raise PacienteNoEncontradoException()
        return self.__historias_clinicas[dni]

    def agendar_turno(self, dni, matricula, especialidad, fecha_hora):
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException()
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException()
        for t in self.__turnos:
            if t.obtener_medico().obtener_matricula() == matricula and t.obtener_fecha_hora() == fecha_hora:
                raise TurnoOcupadoException()
        medico = self.__medicos[matricula]
        # Traducción de días de la semana de inglés a español
        dias_es = {
            "monday": "lunes",
            "tuesday": "martes",
            "wednesday": "miercoles",
            "thursday": "jueves",
            "friday": "viernes",
            "saturday": "sabado",
            "sunday": "domingo"
        }
        dia_en = fecha_hora.strftime("%A").lower()
        dia_semana = dias_es.get(dia_en, dia_en)
        esp = medico.obtener_especialidad_para_dia(dia_semana)
        if esp is None or esp != especialidad:
            raise MedicoNoDisponibleException()
        turno = Turno(self.__pacientes[dni], medico, fecha_hora, especialidad)
        self.__turnos.append(turno)
        self.__historias_clinicas[dni].agregar_turno(turno)

    def emitir_receta(self, dni, matricula, medicamentos):
        if not medicamentos:
            raise RecetaInvalidaException()
        if dni not in self.__pacientes:
            raise PacienteNoEncontradoException()
        if matricula not in self.__medicos:
            raise MedicoNoDisponibleException()
        receta = Receta(self.__pacientes[dni], self.__medicos[matricula], medicamentos)
        self.__historias_clinicas[dni].agregar_receta(receta)