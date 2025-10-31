Algoritmo Negativos01
	Definir num Como Real
	Definir contadorPositivos Como Entero
	contadorPositivos = 0
	
	Repetir
		Escribir "Ingrese un número (negativo para salir):"
		Leer num
		Si num > 0 Entonces
			contadorPositivos = contadorPositivos + 1
		Fin Si
	Hasta Que num < 0
	
	Escribir "Se ingresaron ", contadorPositivos, " números positivos."
FinAlgoritmo
