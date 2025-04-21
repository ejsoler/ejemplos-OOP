#include <iostream>
#include <string>

// Para evitar escribir std:: cada vez
using namespace std;

// Definición de la clase Perro
class Perro {
private:
    // Atributos privados
    string nombre;
    string raza;

public:
    // Constructor con parámetros para inicializar atributos
    Perro(string nombre_, string raza_) {
        nombre = nombre_;
        raza = raza_;
    }

    // Método que simula el ladrido del perro
    void ladrar() {
        cout << "¡Guau!" << endl;
    }

    // Métodos opcionales para acceder a los atributos (getters)
    string getNombre() {
        return nombre;
    }

    string getRaza() {
        return raza;
    }
};

// Función principal
int main() {
    // Crear un objeto de la clase Perro
    Perro miPerro("Fido", "Labrador");

    // Llamar al método ladrar()
    miPerro.ladrar();

    // Mostrar nombre y raza
    cout << "Nombre: " << miPerro.getNombre() << endl;
    cout << "Raza: " << miPerro.getRaza() << endl;

    return 0;
}
