# Danilo Bonometti
# Online Judge ID: 	1144931
# El codigo es de mi autoria completa

# Analisis:
#
# El algoritmo utiliza una cola de prioridad donde se guardan los registros de
# de entrada. La creacion de una cola de prioridad desde un arreglo es O(n).
# Retirar o ingresar un elemento a la vez a la cola es O(log n). Luego se deben
# obtener k consultas de la cola y por cada consulta se debe retirar un 
# elemento y luego agregar otro. Finalmente esto estaria acotado por
# O(k*log n) + O(n).
# 
# En el caso de la memoria se necesita O(n) elementos para representar las 
# prioridades en la cola además del id de la consulta y el periodo. Por lo que
# la memoria estara dominada por O(n).

import sys
import heapq
from collections import namedtuple

# Tupla de registros
reg = namedtuple('register', 'q_num period')

# Lectura de los datos de entrada. Estos se guardan como tuplas en un arreglo
# de registros
registers = []
catch = False
for line in sys.stdin:
	line = line.strip()
	if not catch:
		if line != '#':
			l = line.split()

			# Se guarda una tupla de un registro y un tiempo inicial igual a su
			# su periodo que se utiliza como prioridad para una cola de 
			# prioridad da la que se obtienen los eventos
			registers.append((int(l[2]), reg(int(l[1]), int(l[2]))))
		else:
			catch = True
	else:
		k = int(line)

# Se crea la cola de prioridad
heapq.heapify(registers)

# Se itera para obtener las primeras k consultas
for k in range(k):

	# Se obtiene cada consulta en orden sacandola de la cola de prioridad
	t, query = heapq.heappop(registers)
	print(query.q_num)

	# Luego se vuelve a ingresar el elemento a la cola pero sumandole el
	# periodo de la consulta correspondiente de manera que los eventos queden
	# ordenados por el tiempo en el que son generados
	heapq.heappush(registers, (t+query.period, query))
