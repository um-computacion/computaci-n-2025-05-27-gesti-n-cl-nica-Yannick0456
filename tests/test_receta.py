import unittest
from datetime import datetime
from src.modelo.receta import Receta
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico

class TestReceta(unittest.TestCase):
    def setUp(self):
        self.paciente = Paciente("Lucas Giménez", "12345678", "10/10/1990")
        self.medico = Medico("Dra. Romero", "M3456")
        self.medicamentos = ["Ibuprofeno 600mg", "Paracetamol"]
        self.receta = Receta(self.paciente, self.medico, self.medicamentos)

    def test_fecha_asignada_automaticamente(self):
        ahora = datetime.now()
        self.assertEqual(self.receta._Receta__fecha.date(), ahora.date())

    def test_str_receta(self):
        texto = str(self.receta)
        self.assertIn("Lucas Giménez", texto)
        self.assertIn("Dra. Romero", texto)
        self.assertIn("Ibuprofeno", texto)
        self.assertIn("Paracetamol", texto)
        self.assertIn(str(datetime.now().year), texto)
