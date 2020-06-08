# Danilo Bonometti
# Online Judge ID: 	1144931
# El codigo es de mi autoria completa

# Analisis:
# 
# Como los lemmings estan en una cola de prioridad, ingresarlos a la batalla 
# cuesta O(log n) e ingresarlos a la cola de nuevo cuesta O(log n). A cada 
# batalla ingresan dos lemmings y solo uno vuelve a su respectiva cola, y como 
# el round ejecuta b batallas se tiene una complejiad acotada por b*O(log b) 
# para cada round. Finalmente como se ejecutan a lo mas (sg+sb)/b rounds
# se tiene que la complejidad es de O((sg+sb)*log b) operaciones.
# 
# A lo mas se tiene sg+sb lemmings por lo que la complejidad esta acotada por
# O(sg+sb).

import sys
import heapq
from collections import namedtuple

lem = namedtuple('lemming', 'power race')

# Batalla de lemmings
def battle(l1, l2):

	# Se comparan los poderes en negativo ya que para usar una cola de 
	# prioridad maximalista en Python es necesario utilizar prioridades 
	# negativas
	if -l1.power > -l2.power:
		return lem(l1.power - l2.power, l1.race)
	elif -l1.power < -l2.power:
		return lem(l2.power - l1.power, l2.race)
	else:
		return None

# Lee los casos
cases = []
for line in sys.stdin:
	for _ in range(int(line)):
		case = []
		line = sys.stdin.readline().strip().split()
		b, sg, sb = int(line[0]), int(line[1]), int(line[2])
		case.append(b)

		# Crea un arreglo de lemmings verdes
		case.append(
			[lem(-int(sys.stdin.readline()), 'green') for _ in range(sg)]
		)

		# Crea un arreglo de lemmings azules
		case.append(
			[lem(-int(sys.stdin.readline()),  'blue') for _ in range(sb)]
		)
		cases.append(case)

# Para cada caso
for case in cases:

	# Obtiene los campos de batalla y las listas de los lemmings
	b, qg, qb = case[0], case[1], case[2]

	# Convierte las colas en colas de prioridad, de manera de que el primer
	# lemming en entrar a los campos de batalla sea el mas fuerte
	heapq.heapify(qg)
	heapq.heapify(qb)

	# Mientras hayan lemmings en las colas continua la guerra
	while qg and qb:

		# Lista de ganadores
		winners = []

		# Comienza un round. Ingresan los lemmings a los campos de batalla
		for _ in range(b):

			# Si hay lemmings en las colas
			if qg and qb:

				# Estos batallan
				winner = battle(heapq.heappop(qg), heapq.heappop(qb))

				# El ganador es ingresado a la lista de ganadores
				if winner:
					winners.append(winner)

			# Si no queda ningun lemming en cualquiera de las listas termina
			# el round
			else:
				break

		# Los lemmings ganadores vuelven a sus colas respectivas
		for winner in winners:
			if winner.race == 'green':
				heapq.heappush(qg, winner)
			else:
				heapq.heappush(qb, winner)

	# Al finalizar la guerra, si alguna de las colas tiene lemmings, 
	# corresponde a la raza ganadora
	if qg:
		print('green wins')
		for _ in range(len(qg)):
			l = heapq.heappop(qg)
			print(f'{-l.power}')
	elif qb:
		print('blue wins')
		for _ in range(len(qb)):
			l = heapq.heappop(qb)
			print(f'{-l.power}')

	# En caso contrario ambas razas se extinguen
	else:
		print('green and blue died')
	
	if case != cases[-1]:
		print()
