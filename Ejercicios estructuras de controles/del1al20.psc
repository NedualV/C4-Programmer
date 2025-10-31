Algoritmo del1al20
	Definir i, contadorPares Como Entero
	contadorPares = 0 // Contador
	
	Para i = 1 Hasta 20 Hacer
		Si i MOD 2 == 0 Entonces
			contadorPares = contadorPares + 1
		Fin Si
	Fin Para
	
	Escribir "Hay ", contadorPares, " números pares entre 1 y 20."
FinAlgoritmo
