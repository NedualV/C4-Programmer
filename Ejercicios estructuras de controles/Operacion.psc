Algoritmo Operacion
	Definir num1, num2, resultado Como Real
	Definir op Como Caracter
	
	Escribir "Ingrese el primer número:"
	Leer num1
	Escribir "Ingrese el segundo número:"
	Leer num2
	Escribir "Ingrese la operación (+, -, *, /):"
	Leer op
	
	Segun op Hacer
		'+': 
			resultado = num1 + num2
			Escribir "El resultado es: ", resultado
		'-': 
			resultado = num1 - num2
			Escribir "El resultado es: ", resultado
		'*': 
			resultado = num1 * num2
			Escribir "El resultado es: ", resultado
		'/': 
			Si num2 <> 0 Entonces
				resultado = num1 / num2
				Escribir "El resultado es: ", resultado
			Sino
				Escribir "Error: No se puede dividir por cero"
			Fin Si
		De Otro Modo:
			Escribir "Operación inválida"
	Fin Segun
FinAlgoritmo
