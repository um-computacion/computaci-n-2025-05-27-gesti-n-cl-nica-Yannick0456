import unittest

from src.modelo.especialidad import Especialidad

class TestEspecialidad(unittest.TestCase):
    def setUp(self):
        self.especialidad = Especialidad("Pediatría", ["lunes", "miercoles", "viernes"])

    def test_obtener_especialidad(self):
        self.assertEqual(self.especialidad.obtener_especialidad(), "Pediatría")

    def test_verificar_dia_valido(self):
        self.assertTrue(self.especialidad.verificar_dia("lunes"))
        self.assertTrue(self.especialidad.verificar_dia("MiErCoLeS"))  # case insensitive

    def test_verificar_dia_invalido(self):
        self.assertFalse(self.especialidad.verificar_dia("domingo"))

    def test_str_especialidad(self):
        self.assertIn("Pediatría", str(self.especialidad))
        self.assertIn("lunes", str(self.especialidad))

if __name__ == "__main__":
    unittest.main()