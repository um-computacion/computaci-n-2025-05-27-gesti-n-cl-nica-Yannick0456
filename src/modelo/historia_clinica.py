class HistoriaClinica:
    def __init__(self, paciente):
        self.__paciente = paciente
        self.__turnos = []
        self.__recetas = []

    def agregar_turno(self, turno):
        self.__turnos.append(turno)

    def agregar_receta(self, receta):
        self.__recetas.append(receta)

    def obtener_turnos(self):
        return list(self.__turnos)

    def obtener_recetas(self):
        return list(self.__recetas)

    def __str__(self):
        turnos_str = "\n".join([str(t) for t in self.__turnos])
        recetas_str = "\n".join([str(r) for r in self.__recetas])
        return f"Historia Clínica de {self.__paciente}:\nTurnos:\n{turnos_str}\nRecetas:\n{recetas_str}"
