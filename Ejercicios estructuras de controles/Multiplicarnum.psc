Algoritmo Multiplicarnum
	Definir num, i, resultado Como Entero
	
	Escribir "Ingrese un número para ver su tabla de multiplicar:"
	Leer num
	
	Para i = 1 Hasta 10 Hacer // 'i' es el contador
		resultado = num * i
		Escribir num, " x ", i, " = ", resultado
	Fin Para
FinAlgoritmo
