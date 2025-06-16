class Turno:
    def __init__(self, paciente, medico, fecha_hora, especialidad):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        self.__especialidad = especialidad

    def obtener_medico(self):
        return self.__medico

    def obtener_fecha_hora(self):
        return self.__fecha_hora

    def __str__(self):
        return f"Turno: {self.__paciente} con {self.__medico} para {self.__especialidad} el {self.__fecha_hora}"
