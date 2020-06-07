# Danilo Bonometti
# Online Judge ID: 	1144931
# El codigo es de mi autoria completa

# Anlisis:
# Para cada caso al momento de leer los cursos estos se ordenan. Como cada 
# entrada tiene 5 cursos se tiene un costo de O(5*log 5) operaciones y como se 
# leen n entradas entonces el costo esta dominado por O(n). Agregar las tuplas
# a un diccionario en el peor de los casos es O(m) donde m es la cantidad de 
# elementos en el diccionario y en el peor de los casos se debe llenar con 
# cada una de las entradas, por lo que cada iteracion se harian O(i) donde i va
# de 1 hasta n. Esto resulta en un peor caso de O(n*(n+1)/2) que estaria 
# dominado por O(n^2) (en el caso promedio el ingreso es O(1) por lo que se 
# veria dominado por O(n)). Obtener el valor maximo requiere iterar sobre todo
# el diccionario por lo que en el peor caso se tendria O(n). Crear la lista de
# popularidad en el peor caso tomaria iterar sobre n elementos. Si todos los 
# cursos tienen la misma popularidad entonces se deben iterar sobre n elementos
# de la lista de popularidad y sumarlos. Por lo tanto en el peor de los casos
# el tiempo para calcular los cursos mas populares estaria dominado por O(n^2) 
# operaciones, debido a la influencia del diccionario. Sin embargo en el mejor 
# caso, solo hay una entrada en el diccionario por lo que solo deben recorrerse
# las entradas una vez y la complejidad seria O(n).
# 
# Para la memoria se tiene que a lo mas se necesita un numero fijo de copias de
# la lista de entrada, por lo que la memoria estaria dominada por O(n).

import sys

# Lee cada caso de entrada
cases = []
for line in sys.stdin:
	line = line.strip()
	if line != '0':
		case = []
		for entry in range(int(line)):
			line = sys.stdin.readline().strip().split()

			# Para cada entrada en un caso, ordena los cursos y los guarda como 
			# una tupla
			case.append(tuple(sorted((int(course) for course in line))))
		cases.append(case)

# Para cada caso
for case in cases:

	# Crea un ranking como un diccionario donde se guardara cada combinacion
	# unica de cursos como llave y su popularidad como valor
	rank = {}

	# Para cada entrada
	for entry in case:

		# Si no se encuentra en el diccionario se agrega a este con una 
		# popularidad de 1
		if not entry in rank:
			rank[entry] = 1

		# En caso de encontrarse en el diccionarioó, se le suma 1 a su 
		# popularidad
		else:
			rank[entry] += 1

	# Se obtiene la popularidad maxima de los cursos
	m = max(rank.values())

	# Luego se crea una lista con todos los elementos que tengan la maxima 
	# popularidad
	popularity = [(k, v) for k, v in rank.items() if v == m]

	# Finalmente se imprimen la cantidad de frosh que elegieron los cursos con
	# mayor popularidad
	if len(popularity) == 1:
		print(popularity[0][1])
	else:
		print(sum(e for e in [a[1] for a in popularity]))
