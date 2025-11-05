Proceso Ejercicio2_PositivoNegativo
    Definir numero Como Real;
    Escribir "Introduce un número: ";
    Leer numero;
    
    Si numero > 0 Entonces
        Escribir "El número es positivo";
    Sino
        // En lugar de "Sino Si", abrimos un NUEVO "Si" dentro del "Sino"
        Si numero < 0 Entonces
            Escribir "El número es negativo";
        Sino
            Escribir "El número es cero";
        FinSi // <-- Este 'FinSi' cierra el 'Si' anidado (numero < 0)
    FinSi // <-- Este 'FinSi' cierra el 'Si' principal (numero > 0)
FinProceso