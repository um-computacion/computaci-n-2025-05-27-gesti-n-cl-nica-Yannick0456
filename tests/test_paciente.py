import unittest
from src.modelo.paciente import Paciente  # Asegurate que la ruta sea correcta

class TestPaciente(unittest.TestCase):
    def test_creacion_correcta(self):
        p = Paciente("Juan Pérez", "12345678", "01/01/1990")
        self.assertEqual(p.obtener_dni(), "12345678")

    def test_error_datos_incompletos(self):
        with self.assertRaises(ValueError):
            Paciente("", "12345678", "01/01/1990")
if __name__ == "__main__":
    unittest.main()