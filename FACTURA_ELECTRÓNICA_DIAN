using System;
using System.Collections.Generic;
using System.Security.Cryptography;
using System.Text;

namespace Colombia.Ingenieria.Unidad2.Ejercicio1 
{
    public class ItemFactura 
    { 
        public string Descripcion { get; } 
        public decimal PrecioUnitarioCOP { get; } 
        public int Cantidad { get; } 
        public bool AplicaIVA { get; } 

        public ItemFactura(string desc, decimal precio, int cant, bool aplicaIva) 
        {
            if (precio < 0 || cant <= 0) 
                throw new ArgumentException("Precio o cantidad no válidos.");   

            Descripcion = desc; 
            PrecioUnitarioCOP = precio; 
            Cantidad = cant; 
            AplicaIVA = aplicaIva;
        } 

        public decimal CalcularSubtotalItem() => PrecioUnitarioCOP * Cantidad; 
        public decimal CalcularIVAItem() => AplicaIVA ? CalcularSubtotalItem() * 0.19m : 0.00m; 
    } 

    public class FacturaElectronicaDIAN
    {
        private readonly List<ItemFactura> _items = new();
        public string NITEmisor { get; }
        public string NITAdquirence { get; }
        public string NumeroFactura { get; }  

        public FacturaElectronicaDIAN(string nitEmisor, string nitAdquirente, string numFactura)
        {
            NITEmisor = nitEmisor;
            NITAdquirence = nitAdquirente;
            NumeroFactura = numFactura;
        }

        public void AgregarItem(ItemFactura item) => _items.Add(item);
        
        public decimal CalcularSubTotal()
        {
            decimal sub = 0m;
            foreach (var it in _items) sub += it.CalcularSubtotalItem();
            return sub;
        }

        public decimal CalcularTotalIVA()
        {   
            decimal iva = 0m;
            foreach (var it in _items) iva += it.CalcularIVAItem();
            return iva;
        }

        public string GenerarCUFE()
        {
            string rawCadena = $"{NumeroFactura}{NITEmisor}{NITAdquirence}{CalcularSubTotal():F2}";
            using var sha256 = SHA256.Create();

            byte[] bytes = sha256.ComputeHash(Encoding.UTF8.GetBytes(rawCadena));

            return BitConverter.ToString(bytes).Replace("-", "").ToLower();
        }

        public void ImprimirFacturaDIAN()
        {
            decimal sub = CalcularSubTotal();
            decimal iva = CalcularTotalIVA();
            decimal reteFuente = sub * 0.025m;
            decimal totalPagar = sub + iva - reteFuente;

            Console.WriteLine($"===== FACTURA ELECTRÓNICA DE VENTA DIAN: {NumeroFactura} =====");
            Console.WriteLine($"NIT EMISOR     : {NITEmisor}");
            Console.WriteLine($"NIT ADQUIRENTE : {NITAdquirence}");
            Console.WriteLine($"CUFE           : {GenerarCUFE()}");
            Console.WriteLine($"SUBTOTAL       : {sub,14:N2} COP");
            Console.WriteLine($"IVA (19%)      : {iva,14:N2} COP");
            Console.WriteLine($"RETEFUENTE 2.5%: -{reteFuente,13:N2} COP");
            Console.WriteLine($"TOTAL A PAGAR  : {totalPagar,14:N2} COP\n");
        }

        public class Program
        {
            public static void Main()
            {
                var factura = new FacturaElectronicaDIAN("901345890", "811098765", "SETP99004521");

                factura.AgregarItem(new ItemFactura("Licencia Anual ERP Cloud Enterprise", 1850000m, 2, true));
                factura.AgregarItem(new ItemFactura("Mantenimiento Preventivo de Servidores", 650000m, 4, true));
                factura.AgregarItem(new ItemFactura("Capacitación Backend C# y .NET Core", 450000m, 3, false));
                factura.AgregarItem(new ItemFactura("Dominio Empresarial + SSL Wildcard", 220000m, 1, true));
                factura.AgregarItem(new ItemFactura("Horas Soporte Técnico Nivel 3", 110000m, 15, true));
                factura.AgregarItem(new ItemFactura("Desarrollo e Integración API RESTful", 3200000m, 1, true));
                factura.AgregarItem(new ItemFactura("Auditoría de Ciberseguridad Pentesting", 2800000m, 1, true));
                factura.AgregarItem(new ItemFactura("Suscripción Cloud Storage 2TB (Mensual)", 55000m, 12, true));
                factura.AgregarItem(new ItemFactura("Asesoría Legal en Protección de Datos", 3800000m, 1, false));
                factura.AgregarItem(new ItemFactura("Estación de Trabajo Laptop Workstation i7", 4600000m, 2, true));

                factura.ImprimirFacturaDIAN();
            }
        }
    }
}