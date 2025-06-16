from datetime import datetime

class Receta:
    def __init__(self, paciente, medico, medicamentos):
        self.__paciente = paciente
        self.__medico = medico
        self.__medicamentos = medicamentos
        self.__fecha = datetime.now()

    def __str__(self):
        meds = ", ".join(self.__medicamentos)
        return f"Receta: {self.__paciente} | {self.__medico} | Medicamentos: {meds} | Fecha: {self.__fecha.strftime('%d/%m/%Y')}"
