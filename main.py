from src.modelo.clinica import Clinica
from src.modelo.paciente import Paciente
from src.modelo.medico import Medico
from src.modelo.especialidad import Especialidad
from datetime import datetime

clinica = Clinica()

def menu():
    print("\n--- Sistema de Gestión Clínica ---")
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Agregar especialidad a médico")
    print("4. Agendar turno")
    print("5. Emitir receta")
    print("6. Ver historia clínica")
    print("0. Salir")

def registrar_paciente():
    nombre = input("Nombre completo: ")
    dni = input("DNI: ")
    fecha_nac = input("Fecha de nacimiento (dd/mm/aaaa): ")
    paciente = Paciente(nombre, dni, fecha_nac)
    clinica.agregar_paciente(paciente)
    print(" Paciente registrado.")

def registrar_medico():
    nombre = input("Nombre completo del médico: ")
    matricula = input("Matrícula: ")
    medico = Medico(nombre, matricula)
    clinica.agregar_medico(medico)
    print(" Médico registrado.")

def agregar_especialidad():
    matricula = input("Matrícula del médico: ")
    nombre_esp = input("Nombre de la especialidad: ")
    dias = input("Días de atención (separados por coma, ej: lunes,miércoles): ")
    dias_lista = [d.strip().lower() for d in dias.split(",")]
    especialidad = Especialidad(nombre_esp, dias_lista)
    medico = clinica.buscar_medico(matricula)
    medico.agregar_especialidad(especialidad)
    print(" Especialidad agregada.")

def agendar_turno():
    dni = input("DNI del paciente: ")
    matricula = input("Matrícula del médico: ")
    especialidad = input("Especialidad: ")
    fecha_str = input("Fecha y hora (formato: dd/mm/aaaa hh:mm): ")
    fecha = datetime.strptime(fecha_str, "%d/%m/%Y %H:%M")
    clinica.agendar_turno(dni, matricula, especialidad, fecha)
    print(" Turno agendado.")

def emitir_receta():
    dni = input("DNI del paciente: ")
    matricula = input("Matrícula del médico: ")
    medicamentos = input("Medicamentos (separados por coma): ").split(",")
    medicamentos = [m.strip() for m in medicamentos if m.strip()]
    clinica.emitir_receta(dni, matricula, medicamentos)
    print(" Receta emitida.")

def ver_historia_clinica():
    dni = input("DNI del paciente: ")
    historia = clinica.obtener_historia_clinica(dni)
    print("\n📘 Turnos:")
    for turno in historia.obtener_turnos():
        print(f"- {turno}")
    print("\n💊 Recetas:")
    for receta in historia.obtener_recetas():
        print(f"- {receta}")

if __name__ == "__main__":
    while True:
        menu()
        opcion = input("Elegí una opción: ")

        try:
            if opcion == "1":
                registrar_paciente()
            elif opcion == "2":
                registrar_medico()
            elif opcion == "3":
                agregar_especialidad()
            elif opcion == "4":
                agendar_turno()
            elif opcion == "5":
                emitir_receta()
            elif opcion == "6":
                ver_historia_clinica()
            elif opcion == "0":
                print("👋 Saliendo del sistema.")
                break
            else:
                print("❌ Opción inválida.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
