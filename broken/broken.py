# Danilo Bonometti
# Online Judge ID: 	1144931
# El codigo es de mi autoria completa

# Analisis:
# El algoritmo necesita un contenedor con n caracteres en total, donde n es la 
# cantidad de caracteres en una linea por lo que la memoria estara dominada por 
# O(n).
# 
# En terminos de tiempo, el algoritmo debe recorrer una linea de n caracteres 
# por lo que hace O(n) operaciones. En el peor de los casos todo el texto es 
# beiju por lo que deben capturarse todos los caracteres luego agregarlos al 
# principio de la cola y luego unir todos los elementos. Esto tomaria O(n)
# ingresos. La union de strings esta dada por O(n+m) para strings de distinto 
# tamaño, pero como se tendrian n strings de un caracter el costo final sería 
# O(n). Finalmente en el peor caso el tiempo estaria dominado por O(n).

import sys
from collections import deque

# Se lee una linea de la entrada
for line in sys.stdin:
	# Cola para el texto final
	dq = deque()

	# Flag para comenzar a capturar texto beiju
	beiju = False

	# Contenedor de los caracteres del texto beiju
	b = []

	# Se itera caracter a caracter sobre la linea
	for c in line.strip():

		# Comienza la capturar texto beiju
		if c == '[':
			beiju = True

			# Si hay texto capturado al momento de recibir el caracter de 
			# comienzo de texto beiju, entonces toma el texto capturado y lo 
			# agrega al comienzo de la cola
			if b:
				dq.appendleft(''.join(b))
				del b[:]

		# Termina la captura de texto beiju
		elif c == ']':
			beiju = False

			# Si hay texto beiju capturado se agrega al comienzo de la cola
			if b:
				dq.appendleft(''.join(b))
				del b[:]

		# Captura el texto beiju
		elif beiju:
			b.append(c)

		# Agrega el texto que no es beiju al final de al cola
		elif not beiju:
			dq.append(c)

	# Si sobra texto capturado se agrega al principio de la cola
	if b:
		dq.appendleft(''.join(b))

	# Finalmente se unen todos los elementos de la cola en un nuevo string
	print(''.join(dq))
