Algoritmo Factorial01
	Definir num, i, factorial Como Entero
	
	Escribir "Ingrese un número para calcular su factorial:"
	Leer num
	
	factorial = 1
	i = 1
	
	Si num >= 0 Entonces
		Si num > 0 Entonces
			Repetir
				factorial = factorial * i
				i = i + 1
			Hasta Que i > num
		Fin Si
		Escribir "El factorial de ", num, " es: ", factorial
	Sino
		Escribir "No se puede calcular el factorial de un número negativo."
	Fin Si
FinAlgoritmo
