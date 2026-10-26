using System;
using System.Collections.Generic;

class HabitacionHotel
{
    private int numero;
    private string tipo;
    private double precioPorNoche;
    private bool disponible;
    private string clienteActual;

    public int Numero
    {
        get { return numero; }
    }

    public string Tipo
    {
        get { return tipo; }
        set
        {
            if (value == "Individual" || value == "Doble" || value == "Suite")
                tipo = value;
            else
                Console.WriteLine("Tipo no válido. Use Individual, Doble o Suite.");
        }
    }

    public double PrecioPorNoche
    {
        get { return precioPorNoche; }
        set
        {
            if (value > 0)
                precioPorNoche = value;
            else
                Console.WriteLine("El precio debe ser mayor que cero.");
        }
    }

    public bool Disponible
    {
        get { return disponible; }
    }

    public string ClienteActual
    {
        get { return clienteActual; }
    }

    public HabitacionHotel(int numero, string tipo, double precioPorNoche)
    {
        this.numero = numero;
        Tipo = tipo;
        PrecioPorNoche = precioPorNoche;
        disponible = true;
        clienteActual = "";
    }

    public double Reservar(string nombreCliente, int noches)
    {
        if (!disponible)
        {
            Console.WriteLine("¡Esta habitación está reservada, crack!");
            return -1;
        }

        if (string.IsNullOrWhiteSpace(nombreCliente) || noches <= 0)
        {
            Console.WriteLine("Escriba un nombre y una cantidad de noches mayor que cero.");
            return -1;
        }

        disponible = false;
        clienteActual = nombreCliente;
        return precioPorNoche * noches;
    }

    public bool Liberar()
    {
        if (disponible)
            return false;

        disponible = true;
        clienteActual = "";
        return true;
    }

    public string MostrarInfo()
    {
        string estado = disponible ? "Disponible" : "Ocupada";
        string cliente = disponible ? "Ninguno" : clienteActual;

        return $"Habitación {numero} | Tipo: {tipo} | Precio por noche: {precioPorNoche:C0} | " +
               $"Estado: {estado} | Cliente: {cliente}";
    }

    public void AplicarDescuento(int porcentaje)
    {
        if (porcentaje < 0 || porcentaje > 100)
        {
            Console.WriteLine("El descuento debe estar entre 0 y 100.");
            return;
        }

        precioPorNoche = precioPorNoche * (1 - porcentaje / 100.0);
        Console.WriteLine($"Descuento aplicado. Nuevo precio: {precioPorNoche:C0} por noche.");
    }
}

class Program
{
    static void Main()
    {
        List<HabitacionHotel> habitaciones = new List<HabitacionHotel>
        {
            new HabitacionHotel(101, "Individual", 50000),
            new HabitacionHotel(202, "Doble", 80000),
            new HabitacionHotel(303, "Suite", 150000),
            new HabitacionHotel(404, "Individual", 60000),
            new HabitacionHotel(505, "Doble", 90000)
        };

        int opcion = -1;

        do
        {
            Console.Clear();
            Console.WriteLine("==================================");
            Console.WriteLine("   SISTEMA DE RESERVAS DEL HOTEL");
            Console.WriteLine("==================================");
            Console.WriteLine("1. Ver todas las habitaciones");
            Console.WriteLine("2. Reservar una habitación");
            Console.WriteLine("3. Liberar una habitación");
            Console.WriteLine("4. Aplicar descuento");
            Console.WriteLine("5. Ver cuántas habitaciones están ocupadas");
            Console.WriteLine("0. Salir");
            Console.Write("\nElija una opción: ");

            if (!int.TryParse(Console.ReadLine(), out opcion))
            {
                Console.WriteLine("Opción no válida. Presione una tecla para continuar.");
                Console.ReadKey();
                opcion = -1;
                continue;
            }

            switch (opcion)
            {
                case 1:
                    Console.Clear();
                    Console.WriteLine("=== ESTADO DE LAS HABITACIONES ===");
                    MostrarHabitaciones(habitaciones);
                    Pausar();
                    break;

                case 2:
                    Console.Clear();
                    Console.WriteLine("=== RESERVAR HABITACIÓN ===");
                    MostrarHabitaciones(habitaciones);
                    Console.Write("\nNúmero de habitación: ");

                    if (!int.TryParse(Console.ReadLine(), out int numeroReserva))
                    {
                        Console.WriteLine("Número no válido.");
                        Pausar();
                        break;
                    }

                    HabitacionHotel habitacionReserva = BuscarHabitacion(habitaciones, numeroReserva);

                    if (habitacionReserva == null)
                    {
                        Console.WriteLine("No existe esa habitación.");
                        Pausar();
                        break;
                    }

                    Console.Write("Nombre del cliente: ");
                    string nombre = Console.ReadLine() ?? "";

                    Console.Write("Cantidad de noches: ");
                    if (!int.TryParse(Console.ReadLine(), out int noches))
                    {
                        Console.WriteLine("Cantidad de noches no válida.");
                        Pausar();
                        break;
                    }

                    double costo = habitacionReserva.Reservar(nombre, noches);
                    if (costo >= 0)
                        Console.WriteLine($"Reserva realizada. Costo total: {costo:C0}");

                    Pausar();
                    break;

                case 3:
                    Console.Clear();
                    Console.WriteLine("=== LIBERAR HABITACIÓN ===");
                    MostrarHabitaciones(habitaciones);
                    Console.Write("\nNúmero de habitación que desea liberar: ");

                    if (!int.TryParse(Console.ReadLine(), out int numeroLiberar))
                    {
                        Console.WriteLine("Número no válido.");
                        Pausar();
                        break;
                    }

                    HabitacionHotel habitacionLiberar = BuscarHabitacion(habitaciones, numeroLiberar);

                    if (habitacionLiberar == null)
                        Console.WriteLine("No existe esa habitación.");
                    else if (habitacionLiberar.Liberar())
                        Console.WriteLine("Habitación liberada correctamente.");
                    else
                        Console.WriteLine("La habitación ya estaba disponible.");

                    Pausar();
                    break;

                case 4:
                    Console.Clear();
                    Console.WriteLine("=== APLICAR DESCUENTO ===");
                    MostrarHabitaciones(habitaciones);
                    Console.Write("\nNúmero de habitación: ");

                    if (!int.TryParse(Console.ReadLine(), out int numeroDescuento))
                    {
                        Console.WriteLine("Número no válido.");
                        Pausar();
                        break;
                    }

                    HabitacionHotel habitacionDescuento = BuscarHabitacion(habitaciones, numeroDescuento);

                    if (habitacionDescuento == null)
                    {
                        Console.WriteLine("No existe esa habitación.");
                        Pausar();
                        break;
                    }

                    Console.Write("Porcentaje de descuento (0 a 100): ");
                    if (int.TryParse(Console.ReadLine(), out int porcentaje))
                        habitacionDescuento.AplicarDescuento(porcentaje);
                    else
                        Console.WriteLine("Porcentaje no válido.");

                    Pausar();
                    break;

                case 5:
                    Console.Clear();
                    Console.WriteLine($"Habitaciones ocupadas: {ContarOcupadas(habitaciones)} de {habitaciones.Count}");
                    Pausar();
                    break;

                case 0:
                    Console.Clear();
                    Console.WriteLine("Gracias por usar el sistema. ¡Hasta luego, crack!");
                    break;

                default:
                    Console.WriteLine("Seleccione una opción válida.");
                    Pausar();
                    break;
            }

        } while (opcion != 0);
    }

    static void MostrarHabitaciones(List<HabitacionHotel> habitaciones)
    {
        foreach (HabitacionHotel habitacion in habitaciones)
            Console.WriteLine(habitacion.MostrarInfo());
    }

    static HabitacionHotel BuscarHabitacion(List<HabitacionHotel> habitaciones, int numero)
    {
        foreach (HabitacionHotel habitacion in habitaciones)
        {
            if (habitacion.Numero == numero)
                return habitacion;
        }

        return null;
    }

    static int ContarOcupadas(List<HabitacionHotel> habitaciones)
    {
        int total = 0;

        foreach (HabitacionHotel habitacion in habitaciones)
        {
            if (!habitacion.Disponible)
                total++;
        }

        return total;
    }

    static void Pausar()
    {
        Console.WriteLine("\nPresione una tecla para volver al menú...");
        Console.ReadKey();
    }
}
