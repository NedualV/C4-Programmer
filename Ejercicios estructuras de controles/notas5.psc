Algoritmo notas5
	Definir nota, suma, promedio Como Real
	Definir i Como Entero
	suma = 0 // Acumulador
	
	Para i = 1 Hasta 5 Hacer
		Escribir "Ingrese la nota ", i, ":"
		Leer nota
		suma = suma + nota
	Fin Para
	
	promedio = suma / 5
	Escribir "El promedio es: ", promedio
FinAlgoritmo
