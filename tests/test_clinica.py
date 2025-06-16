import unittest
from datetime import datetime

from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad
from src.modelo.clinica import Clinica
from src.modelo.excepciones import (
    PacienteNoEncontradoException,
    MedicoNoDisponibleException,
    TurnoOcupadoException,
    RecetaInvalidaException
)

class TestClinica(unittest.TestCase):
    def setUp(self):
        self.clinica = Clinica()
        self.paciente = Paciente("Laura Vega", "33344455", "15/08/1990")
        self.medico = Medico("Dr. Suárez", "M1122")
        self.especialidad = Especialidad("Cardiología", ["lunes", "miércoles"])
        self.medico.agregar_especialidad(self.especialidad)

        self.clinica.agregar_paciente(self.paciente)
        self.clinica.agregar_medico(self.medico)

    def test_registro_correcto(self):
        pacientes = self.clinica.obtener_pacientes()
        medicos = self.clinica.obtener_medicos()
        self.assertEqual(len(pacientes), 1)
        self.assertEqual(len(medicos), 1)

    def test_agendar_turno_valido(self):
        fecha = datetime(2025, 6, 16, 10, 0)  # Lunes
        self.clinica.agendar_turno("33344455", "M1122", "Cardiología", fecha)
        turnos = self.clinica.obtener_turnos()
        self.assertEqual(len(turnos), 1)

    def test_emitir_receta_valida(self):
        self.clinica.emitir_receta("33344455", "M1122", ["Aspirina"])
        historia = self.clinica.obtener_historia_clinica("33344455")
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_historia_clinica_completa(self):
        fecha = datetime(2025, 6, 16, 10, 0)  # Lunes
        self.clinica.agendar_turno("33344455", "M1122", "Cardiología", fecha)
        self.clinica.emitir_receta("33344455", "M1122", ["Losartán"])
        historia = self.clinica.obtener_historia_clinica("33344455")
        self.assertEqual(len(historia.obtener_turnos()), 1)
        self.assertEqual(len(historia.obtener_recetas()), 1)

    def test_error_paciente_inexistente(self):
        with self.assertRaises(PacienteNoEncontradoException):
            self.clinica.agendar_turno("99999999", "M1122", "Cardiología", datetime(2025, 6, 16, 10, 0))

    def test_error_medico_inexistente(self):
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("33344455", "M9999", "Cardiología", datetime(2025, 6, 16, 10, 0))

    def test_turno_duplicado(self):
        fecha = datetime(2025, 6, 16, 10, 0)
        self.clinica.agendar_turno("33344455", "M1122", "Cardiología", fecha)
        with self.assertRaises(TurnoOcupadoException):
            self.clinica.agendar_turno("33344455", "M1122", "Cardiología", fecha)

    def test_especialidad_no_atiende_ese_dia(self):
        fecha = datetime(2025, 6, 17, 10, 0)  # Martes (no atiende)
        with self.assertRaises(MedicoNoDisponibleException):
            self.clinica.agendar_turno("33344455", "M1122", "Cardiología", fecha)

    def test_receta_sin_medicamentos(self):
        with self.assertRaises(RecetaInvalidaException):
            self.clinica.emitir_receta("33344455", "M1122", [])
