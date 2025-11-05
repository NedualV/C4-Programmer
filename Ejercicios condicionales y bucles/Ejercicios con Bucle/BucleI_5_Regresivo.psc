Proceso BucleI_5_Regresivo
    Definir numero Como Entero;
    Escribir "Introduce un número para la cuenta regresiva: ";
    Leer numero;
    
    Escribir "Iniciando cuenta regresiva desde ", numero, "...";
    Mientras numero >= 1 Hacer
        Escribir numero;
        numero <- numero - 1;
    FinMientras
    Escribir "¡Despegue!";
FinProceso