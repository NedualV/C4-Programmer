Proceso BuclesII_3_Factorial
    Definir numero, i Como Entero;
    Definir factorial Como Real; // Usamos Real por si el número es muy grande
    
    Escribir "Introduce un número para calcular su factorial: ";
    Leer numero;
    factorial <- 1;
    
    Si numero < 0 Entonces
        Escribir "No se puede calcular el factorial de un número negativo.";
    Sino
        // Anidamos la siguiente condición
        Si numero = 0 Entonces
            Escribir "El factorial de 0 es 1";
        Sino
            // Esta es la parte principal del cálculo
            Para i <- 1 Hasta numero Hacer
                factorial <- factorial * i;
            FinPara
            Escribir "El factorial de ", numero, " es: ", factorial;
        FinSi // <-- Este 'FinSi' cierra el 'Si' anidado (numero = 0)
    FinSi // <-- Este 'FinSi' cierra el 'Si' principal (numero < 0)
FinProceso