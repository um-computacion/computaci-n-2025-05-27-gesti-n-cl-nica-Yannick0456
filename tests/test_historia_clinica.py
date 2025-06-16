import unittest
from datetime import datetime
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.turno import Turno
from src.modelo.receta import Receta
from src.modelo.historia_clinica import HistoriaClinica

class TestHistoriaClinica(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Ana Ruiz", "98765432", "02/02/1985")
        self.medico = Medico("Dr. López", "M5678")
        self.fecha_hora = datetime(2025, 6, 20, 10, 30)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, "Dermatología")
        self.receta = Receta(self.paciente, self.medico, ["Ibuprofeno 600mg", "Paracetamol"])
        self.historia = HistoriaClinica(self.paciente)

    def test_agregar_turno(self):
        self.historia.agregar_turno(self.turno)
        self.assertIn(self.turno, self.historia.obtener_turnos())

    def test_agregar_receta(self):
        self.historia.agregar_receta(self.receta)
        self.assertIn(self.receta, self.historia.obtener_recetas())

    def test_str_historia(self):
        self.historia.agregar_turno(self.turno)
        self.historia.agregar_receta(self.receta)
        resultado = str(self.historia)
        self.assertIn("Historia clínica de Ana Ruiz", resultado)
        self.assertIn("Turno de Ana Ruiz (DNI: 98765432) con Dr. López - Matrícula: M5678", resultado)
        self.assertIn("Receta para Ana Ruiz (DNI: 98765432)", resultado)
