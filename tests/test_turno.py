import unittest
from datetime import datetime
from src.modelo.turno import Turno
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico

class TestTurno(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Ana Ruiz", "98765432", "02/02/1985")
        self.medico = Medico("Dr. López", "M5678")
        self.fecha_hora = datetime(2025, 6, 20, 10, 30)
        self.turno = Turno(self.paciente, self.medico, self.fecha_hora, "Dermatología")

    def test_obtener_medico(self):
        self.assertEqual(self.turno.obtener_medico(), self.medico)

    def test_obtener_fecha_hora(self):
        self.assertEqual(self.turno.obtener_fecha_hora(), self.fecha_hora)

    def test_str_turno(self):
        resultado = str(self.turno)
        self.assertIn("Ana Ruiz", resultado)
        self.assertIn("Dr. López", resultado)
        self.assertIn("Dermatología", resultado)
        self.assertIn("2025", resultado)  # Fecha
