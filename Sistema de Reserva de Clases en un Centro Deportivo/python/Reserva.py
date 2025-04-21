# Class that represents a type of fitness class
# Clase que representa un tipo de clase de ejercicio
class Clase:
    def __init__(self, nombre, duracion, nivel):
        # Initialize attributes: name, duration in minutes, and level
        # Inicializa los atributos: nombre, duración en minutos y nivel
        self.nombre = nombre
        self.duracion = duracion
        self.nivel = nivel

    # Method to display class details
    # Método para mostrar los detalles de la clase
    def mostrar_detalle(self):
        print(f"{self.nombre} - {self.duracion} min - Nivel: {self.nivel}")


# Class that represents a scheduled session of a fitness class
# Clase que representa una sesión programada de una clase de ejercicio
class Sesion:
    def __init__(self, clase, horario):
        # Associate a class with a specific time
        # Asocia una clase con un horario específico
        self.clase = clase
        self.horario = horario

    # Method to display a summary of the session
    # Método para mostrar un resumen de la sesión
    def mostrar_sesion(self):
        print(f"Sesión de '{self.clase.nombre}' a las {self.horario}")


# Class that represents a reservation with price validation and optional discount
# Clase que representa una reserva con validación de tarifa y descuento opcional
class Reserva:
    def __init__(self, sesion, tarifa):
        # Validate that the price is not negative
        # Valida que la tarifa no sea negativa
        if tarifa < 0:
            raise ValueError("La tarifa debe ser un valor positivo.")
        self.sesion = sesion
        self.tarifa = tarifa

    # Method to apply a discount based on a percentage
    # Método para aplicar un descuento basado en un porcentaje
    def aplicar_descuento(self, porcentaje):
        # Discount is only applied if it's between 0 and 100
        # El descuento solo se aplica si está entre 0 y 100
        if 0 <= porcentaje <= 100:
            self.tarifa *= (1 - porcentaje / 100)

    # Method to show reservation details
    # Método para mostrar los detalles de la reserva
    def mostrar_resumen(self):
        print(f"Clase reservada: {self.sesion.clase.nombre}")
        print(f"Horario: {self.sesion.horario}")
        print(f"Tarifa final: ${self.tarifa:.2f}")


# Main function that controls the reservation flow
# Función principal que controla el flujo de la reserva
def main():
    print("🏋️ Bienvenido al Sistema de Reserva de Clases")
    # Welcome message to the reservation system
    # Mensaje de bienvenida al sistema de reservas

    # Create two class options
    # Crear dos opciones de clases
    c1 = Clase("Yoga", 60, "Principiante")
    c2 = Clase("Spinning", 45, "Intermedio")

    # Create sessions for those classes
    # Crear sesiones para esas clases
    s1 = Sesion(c1, "08:00")
    s2 = Sesion(c2, "18:30")

    # Store sessions in a list
    # Guardar sesiones en una lista
    sesiones = [s1, s2]

    # Display available sessions
    # Mostrar las sesiones disponibles
    print("\n📅 Sesiones disponibles:")
    for i, sesion in enumerate(sesiones, 1):
        # Display session number and summary
        # Mostrar número de sesión y resumen
        print(f"{i}. ", end="")
        sesion.mostrar_sesion()

    # User selects a session
    # El usuario selecciona una sesión
    seleccion = int(input("Seleccione una sesión (1 o 2): "))
    sesion_elegida = sesiones[seleccion - 1]

    # Ask user for base price
    # Preguntar al usuario por la tarifa base
    tarifa = float(input("Ingrese la tarifa de la clase: $"))

    # Create reservation with entered price
    # Crear reserva con la tarifa ingresada
    reserva = Reserva(sesion_elegida, tarifa)

    # Ask if the user wants to apply a discount
    # Preguntar si el usuario quiere aplicar un descuento
    aplicar = input("¿Desea aplicar un descuento? (s/n): ").lower()
    if aplicar == 's':
        porcentaje = float(input("Ingrese el porcentaje de descuento: "))
        reserva.aplicar_descuento(porcentaje)

    # Show reservation summary
    # Mostrar el resumen de la reserva
    print("\n📄 Detalles de la reserva:")
    reserva.mostrar_resumen()


# Entry point of the program
# Punto de entrada del programa
if __name__ == "__main__":
    main()
