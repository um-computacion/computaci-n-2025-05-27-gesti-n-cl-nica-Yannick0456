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
        texto = f"Historia clínica de {self.__paciente}\n"
        texto += "\nTurnos:\n"
        texto += "\n".join(str(turno) for turno in self.__turnos) or "Sin turnos"
        texto += "\n\nRecetas:\n"
        texto += "\n".join(str(receta) for receta in self.__recetas) or "Sin recetas"
        return texto
    

