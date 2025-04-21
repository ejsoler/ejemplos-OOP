# Definición de la clase Perro
class Perro:
    # Método constructor: se llama automáticamente al crear un objeto
    def __init__(self, nombre, raza):
        # Se usa doble guión bajo (__) para indicar que los atributos son privados
        # Esto significa que no deben ser accedidos directamente desde fuera de la clase
        self.__nombre = nombre
        self.__raza = raza

    # Método que representa el comportamiento de ladrar
    def ladrar(self):
        print("¡Guau!")  # Simula el sonido del ladrido del perro

    # Propiedad para acceder al nombre del perro de forma segura
    @property
    def nombre(self):
        # Devuelve el valor del atributo privado __nombre
        return self.__nombre

    # Propiedad para modificar el nombre del perro
    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Aquí se podría validar el nuevo nombre si se quisiera
        # Por ejemplo: verificar que no esté vacío
        if nuevo_nombre.strip() == "":
            print("El nombre no puede estar vacío.")
        else:
            self.__nombre = nuevo_nombre

    # Propiedad para acceder a la raza del perro
    @property
    def raza(self):
        return self.__raza

    # Propiedad para modificar la raza del perro
    @raza.setter
    def raza(self, nueva_raza):
        if nueva_raza.strip() == "":
            print("La raza no puede estar vacía.")
        else:
            self.__raza = nueva_raza


# Función principal: punto de entrada del programa
def main():
    # Se crea un objeto de la clase Perro
    mi_perro = Perro("Fido", "Labrador")

    # Se llama al método ladrar del objeto
    mi_perro.ladrar()

    # Acceso a los atributos usando propiedades
    print("Nombre:", mi_perro.nombre)  # Llama automáticamente al método nombre()
    print("Raza:", mi_perro.raza)      # Llama automáticamente al método raza()

    # Modificar los atributos usando propiedades (invoca los setters)
    mi_perro.nombre = "Toby"
    mi_perro.raza = "Golden Retriever"

    # Mostrar los nuevos valores
    print("Nuevo nombre:", mi_perro.nombre)
    print("Nueva raza:", mi_perro.raza)


# Esta línea asegura que main() solo se ejecuta si el archivo es el principal
if __name__ == "__main__":
    main()
  
