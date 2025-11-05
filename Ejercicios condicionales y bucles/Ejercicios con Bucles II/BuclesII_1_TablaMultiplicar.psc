Proceso BuclesII_1_TablaMultiplicar
    Definir numero, i, resultado Como Entero;
    Escribir "¿De qué número quieres ver la tabla de multiplicar?: ";
    Leer numero;
    
    Para i <- 1 Hasta 10 Con Paso 1 Hacer
        resultado <- numero * i;
        Escribir numero, " x ", i, " = ", resultado;
    FinPara
FinProceso