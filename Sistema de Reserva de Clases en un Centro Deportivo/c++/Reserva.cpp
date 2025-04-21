#include <iostream>     // Input and output stream
// Entrada y salida de datos

#include <string>       // String handling
// Manejo de cadenas de texto

#include <vector>       // Dynamic arrays
// Arreglos dinámicos (vectores)

#include <iomanip>      // Formatting output
// Formato de salida (decimales, ancho, etc.)

using namespace std;    // Avoids writing std:: before each element
// Evita escribir std:: antes de cada elemento

// Class representing a type of fitness class
// Clase que representa un tipo de clase de ejercicio
class Clase {
private:
    string nombre;
    int duracion;
    string nivel;

public:
    // Constructor to initialize attributes
    // Constructor para inicializar atributos
    Clase(string n, int d, string l) : nombre(n), duracion(d), nivel(l) {}

    // Getter for the name
    // Accesor para el nombre
    string getNombre() const { return nombre; }

    // Method to display class details
    // Método para mostrar los detalles de la clase
    void mostrarDetalle() const {
        cout << nombre << " - " << duracion << " min - Nivel: " << nivel << endl;
    }
};

// Class representing a scheduled session of a class
// Clase que representa una sesión programada de una clase
class Sesion {
private:
    Clase clase;
    string horario;

public:
    // Constructor initializing class and time
    // Constructor que inicializa clase y horario
    Sesion(Clase c, string h) : clase(c), horario(h) {}

    // Getter for the time
    // Accesor para el horario
    string getHorario() const { return horario; }

    // Getter for the class object
    // Accesor para el objeto de clase
    Clase getClase() const { return clase; }

    // Display the session summary
    // Muestra el resumen de la sesión
    void mostrarSesion() const {
        cout << "Sesión de '" << clase.getNombre() << "' a las " << horario << endl;
    }
};

// Class that represents a reservation with validation
// Clase que representa una reserva con validación
class Reserva {
private:
    Sesion sesion;
    double tarifa;

public:
    // Constructor with validation of tarifa
    // Constructor con validación de tarifa
    Reserva(Sesion s, double t) : sesion(s), tarifa(t) {
        if (t < 0) {
            throw invalid_argument("La tarifa debe ser un valor positivo.");
        }
    }

    // Applies a discount if percentage is valid
    // Aplica un descuento si el porcentaje es válido
    void aplicarDescuento(double porcentaje) {
        if (porcentaje >= 0 && porcentaje <= 100) {
            tarifa *= (1 - porcentaje / 100.0);
        }
    }

    // Displays reservation details
    // Muestra los detalles de la reserva
    void mostrarResumen() const {
        cout << fixed << setprecision(2); // Set two decimal places
        // Fijar dos cifras decimales
        cout << "Clase reservada: " << sesion.getClase().getNombre() << endl;
        cout << "Horario: " << sesion.getHorario() << endl;
        cout << "Tarifa final: $" << tarifa << endl;
    }
};

// Main function where program execution starts
// Función principal donde inicia la ejecución del programa
int main() {
    cout << "🏋️ Bienvenido al Sistema de Reserva de Clases\n";
    // Welcome message / Mensaje de bienvenida

    // Create instances of classes
    // Crear instancias de clases de ejercicio
    Clase yoga("Yoga", 60, "Principiante");
    Clase spinning("Spinning", 45, "Intermedio");

    // Create scheduled sessions
    // Crear sesiones programadas
    Sesion s1(yoga, "08:00");
    Sesion s2(spinning, "18:30");

    // Store sessions in a vector (dynamic array)
    // Guardar sesiones en un vector (arreglo dinámico)
    vector<Sesion> sesiones = {s1, s2};

    // Display available sessions
    // Mostrar las sesiones disponibles
    cout << "\n📅 Sesiones disponibles:\n";
    for (size_t i = 0; i < sesiones.size(); ++i) {
        cout << i + 1 << ". ";
        sesiones[i].mostrarSesion();
    }

    // Ask user to select a session
    // Preguntar al usuario qué sesión desea
    int seleccion;
    cout << "Seleccione una sesión (1 o 2): ";
    cin >> seleccion;

    // Get the selected session
    // Obtener la sesión elegida
    Sesion sesionElegida = sesiones[seleccion - 1];

    // Request base price
    // Solicitar tarifa base
    double tarifa;
    cout << "Ingrese la tarifa de la clase: $";
    cin >> tarifa;

    try {
        // Create reservation object
        // Crear objeto reserva
        Reserva reserva(sesionElegida, tarifa);

        // Ask if user wants to apply discount
        // Preguntar si desea aplicar descuento
        char aplicar;
        cout << "¿Desea aplicar un descuento? (s/n): ";
        cin >> aplicar;

        // If yes, apply the discount
        // Si es sí, aplicar el descuento
        if (aplicar == 's' || aplicar == 'S') {
            double porcentaje;
            cout << "Ingrese el porcentaje de descuento: ";
            cin >> porcentaje;
            reserva.aplicarDescuento(porcentaje);
        }

        // Show final reservation summary
        // Mostrar resumen final de la reserva
        cout << "\n📄 Detalles de la reserva:\n";
        reserva.mostrarResumen();

    } catch (const exception& e) {
        // Handle any errors
        // Manejar errores (por ejemplo, tarifa negativa)
        cerr << "Error: " << e.what() << endl;
    }

    return 0; // End program
    // Fin del programa
}
