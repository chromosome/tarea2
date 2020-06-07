# Danilo Bonometti
# Online Judge ID: 	1144931
# El codigo es de mi autoria completa

# Analisis:
# 
# El peor caso se tiene cuando el orden de los vagones esta completamente 
# invertido por lo que utilizando una pila se tomara 2*n-1 operaciones. 
# Considerando que ingresar y retirar de la cola o la pila tiene coste O(1)
# se tiene que la complejidad para el tiempo esta dominada por O(n).
# 
# En espacio se utiliza una cola ordenada del mismo tamano del arreglo de 
# entrada y una pila que se llena con los elementos que se retiran de la cola
# por lo que se necesitan a lo mas 2*n elementos y su complejidad esta acotada
# por O(n).

import sys
from collections import deque

# Lee casos
trains = []
for line in sys.stdin:
	orders = []
	while line != '0' and line != '':
		line = sys.stdin.readline().strip()
		if line != '0':
			orders.append([int(i) for i in line.split()])
	trains.append(orders)
trains.pop()

# Para cada caso
for orders in trains:

	# Para cada orden del tren
	for order in orders:

		# Crea un arreglo ordenado que se usara para intentar convertilo al 
		# orden correspondiente
		i = deque(range(1, len(order)+1))

		# Crea una pila para simular la estacion de trenes
		s = deque()

		# El orden es posible a menos que se encuentre lo contrario
		r = 'Yes'

		# Para cada vagon en el orden se revisa si se puede crear este desde un
		# tren ordenado secuencialmente
		for coach in order:

			# Si el vagon se encuentra en la cola ordenada
			if coach in i:

				# Revisa si el vagon es el primero en la cola ordenada
				while coach != i[0]:
					
					# De lo contrario ingresa ese vagon a la pila
					s.appendleft(i.popleft())

				# Cuando lo encuentra es quitado de la cola ordenada y 
				# significa que es posible tener ese vagon en el orden
				# correspondiente
				i.popleft()

			# Si no esta en la cola, entonces se encuentra en la pila
			else:

				# Si el vagon no es el primero en la pila
				if coach != s[0]:

					# Entonces el orden no puede ser creado desde un tren 
					# ordenado, ya que no pueden quedar elementos en orden 
					# relativo en la pila
					r = 'No'
					break

					# Si es el primero en la pila entonces lo saca, por lo que
					# el orden todavía es posible
				else:
					s.popleft()
		print(r)
	print()
