Algoritmo ContarNum
	Definir num Como Real
	Definir contadorPositivos Como Entero
	contadorPositivos = 0
	
	Escribir "Ingrese un número (negativo para salir):"
	Leer num
	
	Mientras num >= 0 Hacer
		Si num > 0 Entonces
			contadorPositivos = contadorPositivos + 1
		Fin Si
		Escribir "Ingrese otro número (negativo para salir):"
		Leer num
	Fin Mientras
FinAlgoritmo
