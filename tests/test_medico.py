import unittest
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad

class TestMedico(unittest.TestCase):
    def setUp(self):
        self.medico = Medico("Dra. Gómez", "M1234")
        self.esp1 = Especialidad("Cardiología", ["martes", "jueves"])
        self.esp2 = Especialidad("Clínica", ["lunes"])

    def test_agregar_especialidad(self):
        self.medico.agregar_especialidad(self.esp1)
        self.assertEqual(len(self.medico._Medico__especialidades), 1)
        self.medico.agregar_especialidad(self.esp1)  # Intentar duplicado
        self.assertEqual(len(self.medico._Medico__especialidades), 1)

    def test_obtener_matricula(self):
        self.assertEqual(self.medico.obtener_matricula(), "M1234")

    def test_obtener_especialidad_para_dia_valido(self):
        self.medico.agregar_especialidad(self.esp1)
        self.assertEqual(self.medico.obtener_especialidad_para_dia("jueves"), "Cardiología")

    def test_obtener_especialidad_para_dia_invalido(self):
        self.assertIsNone(self.medico.obtener_especialidad_para_dia("domingo"))

if __name__ == "__main__":
    unittest.main()