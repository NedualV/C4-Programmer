Proceso Ejercicio4_Notas
    Definir nota Como Real;
    Escribir "Introduce tu nota (0-100): ";
    Leer nota;
    
    Si nota >= 90 Entonces
        Escribir "Aprobado con A";
    Sino
        // Anidamos la segunda condición dentro del primer "Sino"
        Si nota >= 70 Entonces
            Escribir "Aprobado";
        Sino
            Escribir "Reprobado";
        FinSi // <-- Cierre del "Si" anidado (nota >= 70)
    FinSi // <-- Cierre del "Si" principal (nota >= 90)
FinProceso