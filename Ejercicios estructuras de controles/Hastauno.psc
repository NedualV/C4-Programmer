Algoritmo Hastauno
	Definir nota, suma, promedio Como Real
	Definir contador Como Entero
	suma = 0
	contador = 0
	
	Repetir
		Escribir "Ingrese una nota (-1 para terminar):"
		Leer nota
		Si nota <> -1 Entonces
			suma = suma + nota
			contador = contador + 1
		Fin Si
	Hasta Que nota == -1
	
	Si contador > 0 Entonces
		promedio = suma / contador
		Escribir "El promedio de las notas es: ", promedio
	Sino
		Escribir "No se ingresaron notas."
	Fin Si
FinAlgoritmo
