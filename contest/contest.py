# Danilo Bonometti
# Online Judge ID: 	1144931
# El codigo es de mi autoria completa

# Analisis:
# 
# Se debe iterar sobre n entradas por lo que el caso base es O(n) en tiempo.
# Para cada participante se guarda cada uno de sus problemas, así que a lo mas
# se ocupara un diccionario con p participantes y m problemas para cada uno.
# Obtener la suma de tiempos de penalizacion y de problemas resueltos requiere 
# iterar sobre los diccionarios de problema de cada participante dos veces y 
# seria O(2*p*m). Luego obtener el ranking de participantes ordenado requiere
# O(p*log p) operaciones por el peor caso de Tim Sort ocupado en python. 
# Finalmente se trendria O(n) + O(p*m) + O(p*log p) para la complejidad 
# temporal de cada caso en el peor de los casos.
# 
# Para el espacio a lo mas se almacenan m problemas para p participantes por lo
# que tomaria O(p*m) + O(n) elementos. Esto puede reducirse a O(p*m) si se leen
# las entradas de los casos de una a la vez.

import sys
from functools import cmp_to_key

# Funcion para comparar concursantes
def cont_compare(a, b):

	# Por problemas resueltos
	if a[1][0] > b[1][0]:
		return -1
	elif a[1][0] < b[1][0]:
		return 1
	else:

		# Por tiempo de penalizacion acumulado
		if a[1][1] < b[1][1]:
			return -1
		elif a[1][1] > b[1][1]:
			return 1
		else:

			# Por numero de equipo
			if a[0] < b[0]:
				return -1
			else:
				return 1

# Lectura de la entrada
cases = []
case_count = 0
for line in sys.stdin:
	case_count = int(line)
	sys.stdin.readline()
	for _ in range(case_count):
		line = sys.stdin.readline()
		case = []
		while line != '\n' and line != '':
			s = line.rstrip().split()
			case.append([int(s[0]), int(s[1]), int(s[2]), s[3]])
			line = sys.stdin.readline()
		cases.append(case)

# Para cada caso
for case in cases:

	# Se crea un diccionario de concursantes
	cont = {}

	# Para cada entrada
	for entry in case:

		# Se obtiene concursante, problema y resultado
		c, n, l = entry[0], entry[1], entry[3]

		# t se obtiene como la penalizacion de una respuesta incorrecta o el 
		# tiempo de una respuesta correcta
		t = { 'C': entry[2], 'I': 20 }[l] if l in ('C', 'I') else 0

		# Si el concursante no esta en el diccionario, se agrega a este con 
		# valor de un diccionario correspondiente al problema. Aqui se 
		# acumulara la penalizacion para cada problema respondido por ese 
		# concursante
		if not c in cont:
			cont[c] = { n : [t, l] }

		# Si el concursante se encuentra en el diccionario
		else:

			# Se obtienen el diccionario de los problemas respondidos por el 
			# concursante
			p = cont[c]

			# Si un problema no esta en el diccionario de problemas para el 
			# concursante, se agrega
			if not n in p:
				p[n] = [t, l]

			# Si el problema esta en el diccionario, acumula la penalizacion
			# correspondiente para este
			else:

				# Si el problema ya fue resuelto descarta las entradas nuevas
				# para ese problema
				if p[n][1] =='C':
					continue

				# Si las entradas del problema no han sido incorrectas, y el 
				# problema fue respondido incorrectamente, se toma el tiempo
				# de penalizacion base y se actualiza el estado del problema
				# a incorrecto
				elif p[n][1] != 'I' and l == 'I':
					p[n][0] = 20
					p[n][1] = 'I'

				# Si el problema ya fue respondido incorrectamente y luego es 
				# respondido de forma incorrecta de nuevo, se suma la 
				# penalizacion
				elif p[n][1] == 'I' and l == 'I':
					p[n][0] += 20

				# Si el problema no ha sido juzgado incorrecto y es resuelto, 
				# se marca correcto y se toma el tiempo de resolucion
				elif p[n][1] != 'I' and l == 'C':
					p[n][0] = entry[2]
					p[n][1] = l

				# Si el problema es incorrecto y es resuelto, se suma el tiempo
				# de resolucion y se marca correcto
				elif p[n][1] == 'I' and l =='C':
					p[n][0] += entry[2]
					p[n][1] = l

	# Una vez acumulados todos los tiempos de problemas para los concursantes 
	# se crea un diccionario de ranking para estos
	rank = {}

	# Para cada concursante
	for c in cont:
		p = cont[c]

		# Se agregan al ranking con la suma de los problemas resueltos y la 
		# suma total de sus tiempos de penalizacion
		rank[c] = (sum(      1 for x in p if p[x][1] == 'C'),
				   sum(p[x][0] for x in p if p[x][1] == 'C'))

	# Finalmente se ordenan los concursantes
	for k, v in sorted(rank.items(), key=cmp_to_key(cont_compare)):
		print(f'{k} {v[0]} {v[1]}')
	
	if case != cases[-1]:
		print()
