Algoritmo Hasta0
	Definir num, contador Como Entero
	contador = 0
	
	Escribir "Ingrese un número (0 para salir):"
	Leer num
	
	Mientras num <> 0 Hacer
		contador = contador + 1
		Escribir "Ingrese otro número (0 para salir):"
		Leer num
	Fin Mientras
	
	Escribir "Se ingresaron ", contador, " números."
FinAlgoritmo
