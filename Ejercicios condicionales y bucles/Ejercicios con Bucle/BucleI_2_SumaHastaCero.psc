Proceso BucleI_2_SumaHastaCero
    Definir suma_total, numero Como Real;
    suma_total <- 0;
    
    Repetir
        Escribir "Introduce un número (escribe 0 para terminar): ";
        Leer numero;
        suma_total <- suma_total + numero;
    Hasta Que numero = 0
    
    Escribir "La suma total de los números introducidos es: ", suma_total;
FinProceso