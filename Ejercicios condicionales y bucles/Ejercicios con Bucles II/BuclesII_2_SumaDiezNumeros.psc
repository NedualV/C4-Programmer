Proceso BuclesII_2_SumaDiezNumeros
    Definir suma_total, numero Como Real;
    Definir i Como Entero;
    suma_total <- 0;
    
    Escribir "Introduce 10 números:";
    Para i <- 1 Hasta 10 Hacer
        Escribir "Número ", i, "/10: ";
        Leer numero;
        suma_total <- suma_total + numero;
    FinPara
    
    Escribir "La suma total de los 10 números es: ", suma_total;
FinProceso