Proceso BucleI_3_AdivinaNumero
    Definir numero_secreto, intento Como Entero;
    numero_secreto <- 7;
    
    Repetir
        Escribir "Adivina el número secreto: ";
        Leer intento;
        
        Si intento <> numero_secreto Entonces
            Escribir "Incorrecto. ¡Intenta de nuevo!";
        FinSi
    Hasta Que intento = numero_secreto
    
    Escribir "¡Felicidades! Adivinaste el número.";
FinProceso