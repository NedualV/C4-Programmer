Proceso Ejercicio5_Descuento
    Definir monto, descuento, total_pagar Como Real;
    Escribir "Introduce el monto de la compra: ";
    Leer monto;
    
    Si monto > 500 Entonces
        descuento <- monto * 0.10;
        total_pagar <- monto - descuento;
        Escribir "Se aplicó un descuento de: ", descuento;
        Escribir "El total a pagar es: ", total_pagar;
    Sino
        Escribir "El total a pagar es: ", monto, " (Sin descuento)";
    FinSi
FinProceso