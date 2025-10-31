Algoritmo ABCD
	Definir calificacion Como Caracter
	
	Escribir "Ingrese la calificación (A, B, C, D, F):"
	Leer calificacion
	
	Segun calificacion Hacer
		'A': Escribir "Excelente"
		'B': Escribir "Bueno"
		'C': Escribir "Regular"
		'D': Escribir "Deficiente"
		'F': Escribir "Reprobado"
		De Otro Modo:
			Escribir "Calificación inválida"
	Fin Segun
FinAlgoritmo
