class Medico:
    def __init__(self, nombre: str, matricula: str):
        self.__nombre = nombre
        self.__matricula = matricula
        self.__especialidades = []

    def agregar_especialidad(self, especialidad):
        # Evitar duplicados del mismo tipo
        tipos_actuales = [e.obtener_especialidad() for e in self.__especialidades]
        if especialidad.obtener_especialidad() not in tipos_actuales:
            self.__especialidades.append(especialidad)

    def obtener_matricula(self) -> str:
        return self.__matricula

    def obtener_especialidad_para_dia(self, dia: str) -> str | None:
        for esp in self.__especialidades:
            if esp.verificar_dia(dia):
                return esp.obtener_especialidad()
        return None

    def __str__(self) -> str:
        esp_str = "; ".join(str(e) for e in self.__especialidades)
        return f"{self.__nombre} - Matrícula: {self.__matricula}\nEspecialidades: {esp_str}"

