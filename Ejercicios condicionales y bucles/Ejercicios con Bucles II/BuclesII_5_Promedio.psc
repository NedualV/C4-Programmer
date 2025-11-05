Proceso BuclesII_5_Promedio
    Definir suma_notas, nota, promedio Como Real;
    Definir i, cantidad_notas Como Entero;
    
    cantidad_notas <- 5;
    suma_notas <- 0;
    
    Escribir "Introduce ", cantidad_notas, " notas:";
    Para i <- 1 Hasta cantidad_notas Hacer
        Escribir "Nota ", i, ": ";
        Leer nota;
        suma_notas <- suma_notas + nota;
    FinPara
    
    promedio <- suma_notas / cantidad_notas;
    
    Escribir "La suma total de las notas es: ", suma_notas;
    Escribir "El promedio final es: ", promedio;
FinProceso