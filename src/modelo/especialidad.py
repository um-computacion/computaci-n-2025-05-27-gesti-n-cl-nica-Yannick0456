import unicodedata

def _normalizar_dia(dia: str) -> str:
    # Convierte a minúsculas y elimina tildes
    nfkd = unicodedata.normalize('NFKD', dia.lower())
    return "".join([c for c in nfkd if not unicodedata.combining(c)])

class Especialidad:
    def __init__(self, tipo, dias):
        if not tipo or not isinstance(tipo, str):
            raise ValueError("El tipo de especialidad debe ser un string no vacío.")
        if not dias or not all(isinstance(d, str) and d.strip() for d in dias):
            raise ValueError("La lista de días debe contener al menos un día válido.")
        self.__tipo = tipo
        self.__dias_originales = list(dias)  # para mostrar exactamente como se ingresaron
        self.__dias_normalizados = [_normalizar_dia(d) for d in dias]  # para comparar

    def obtener_especialidad(self) -> str:
        return self.__tipo

    def verificar_dia(self, dia: str) -> bool:
        return _normalizar_dia(dia) in self.__dias_normalizados

    def __str__(self) -> str:
        dias_str = ", ".join(self.__dias_originales)
        return f"{self.__tipo} (Días: {dias_str})"