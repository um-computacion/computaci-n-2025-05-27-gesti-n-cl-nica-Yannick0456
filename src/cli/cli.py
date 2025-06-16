from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.turno import Turno

def main():
    print("=== Sistema de Gestión Clínica ===")
    while True:
        print("\nOpciones:")
        print("1. Crear paciente")
        print("2. Crear médico")
        print("3. Salir")
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            nombre = input("Nombre del paciente: ")
            dni = input("DNI del paciente: ")
            paciente = Paciente(nombre, dni)
            print(f"Paciente creado: {paciente}")

        elif opcion == "2":
            nombre = input("Nombre del médico: ")
            especialidad = input("Especialidad: ")
            medico = Medico(nombre, especialidad)
            print(f"Médico creado: {medico}")

        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida.")
