Proceso BucleI_4_ValidarPass
    Definir password Como Caracter;
    
    Repetir
        Escribir "Introduce la contraseña: ";
        Leer password;
        Si password <> "1234" Entonces
            Escribir "Contraseña incorrecta.";
        FinSi
    Hasta Que password = "1234"
    
    Escribir "Acceso concedido.";
FinProceso