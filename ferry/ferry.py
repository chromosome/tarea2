# Danilo Bonometti
# Online Judge ID: 	1144931
# El codigo es de mi autoria completa

# Analisis:
# 
# Para el espacio, cada elemento que sale de la cola de eventos es ingresado a 
# la cola correspondiente a su lado, por lo que nunca se necesitan mas de n 
# elementos y su complejidad seria O(n).
# 
# Para el tiempo, en el peor caso el ferry debe llenar de un auto cada vez que 
# viaja por lo que cada viaje le toma retirar O(1) operacion de las colas
# correspondientes, por lo que para todos los viajes tendria O(n) operaciones.
# Finalmente se ordena la cola final con respecto al numero del evento con el
# que se ingresa a la cola de eventos. Finalmente se tendrian O(n) + O(n*log n)
# operaciones lo que esta acotado solo por O(n*log n).

import sys
from collections import deque, namedtuple

arrival = namedtuple('arrival', 'pos time side')
ferry = namedtuple('ferry', 'n t')

# Funcion para llenar las colas de los lados desde la cola eventos
def fill_queues(q, ql, qr, tf):

	# Saca de la cola de eventos todos los eventos que sucedan al mismo tiempo
	while q and q[-1].time <= tf:
		a = q.pop()

		# Y luego los agrega a la cola de su lado correspondiente
		if a.side == 'left':
			ql.appendleft(a)
		else:
			qr.appendleft(a)

# Lee los casos
cases = []
for line in sys.stdin:
	for _ in range(int(line)):
		line = sys.stdin.readline().strip().split()
		n, t, m = int(line[0]), int(line[1]), int(line[2])
		case = [ferry(n, t)]
		for i in range(m):
			line = sys.stdin.readline().strip().split()

			# Guarda cada llegada de auto con su posicion correspondiente en
			# la fila. Esto es para poder obtener el orden correcto al final
			case.append(arrival(i, int(line[0]), line[1]))
		cases.append(case)

for case in cases:
	# Resultados
	r = []

	# Espacio en el ferry y tiempo de viaje
	n, ts = case[0]

	# Tiempo del ferry
	tf = 0

	# Lado en el que parte el ferry
	side = 'left'

	# Cola de los eventos en orden de llegada
	q  = deque(case[-1:0:-1])

	# Cola del lado izquiero y derecho
	ql = deque()
	qr = deque()

	# El ferry esta inicialmente esperando a que lleguen autos
	waiting = True
	while q or ql or qr:

		# Si el ferry esta esperando
		if waiting:

			# Espera hasta el primer evento
			tf = q[-1].time

			# Luego se llenan las colas con todos los eventos
			fill_queues(q, ql, qr, tf)

			# Y el ferry comienza a moverse
			waiting = False

		# Si el ferry no esta esperando
		else:

			# Y no quedan autos en cualquiera de los lados
			if not ql and not qr:

				# Entonces el ferry espera
				waiting = True

			# Si hay autos en cualquiera de los lados
			else:

				# Se actualizan las colas de autos
				fill_queues(q, ql, qr, tf)

				# Se actualiza el tiempo del ferry como el tiempo que le toma 
				# un cambio de lado
				tf += ts

				# Si se encuentra en el lado izquierdo
				if side == 'left':

					# Y hay autos en el la cola
					if ql:

						# Toma todos los autos que puede
						m = len(ql) if len(ql) < n else n

						# Y se llena la lista de tiempos de llegada
						for _ in range(m):
							r.append((ql.pop(), tf))

					# Finalemente se actualiza el lado del ferry
					side = 'right'

				# Se hace lo mismo si el ferry esta en el lado izquierdo
				else:
					if qr:
						m = len(qr) if len(qr) < n else n
						for _ in range(m):
							r.append((qr.pop(), tf))
					side = 'left'

				# Y se actualizan las colas por si llegaron autos durante el
				# trascurso del ferry
				fill_queues(q, ql, qr, tf)

	# Finalmente se ordenan los eventos con respecto al orden de llegada del 
	# auto
	for e in sorted(r):
		print(e[1])

	if case != cases[-1]:
		print()
