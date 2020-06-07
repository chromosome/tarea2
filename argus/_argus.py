import sys
from collections import deque
import math
from functools import reduce

register = {}
k = 0
catch = False
for line in sys.stdin:
	line = line.strip()
	if not catch:
		if line != '#':
			l = line.split()
			register[int(l[1])] = int(l[2])
		else:
			catch = True
	else:
		k = int(line)

register = dict(sorted(register.items()))

q = deque()
p = reduce(math.gcd, register.values())
t = min(register.values())
t = p
while len(q) < k:
	for e in register:
		if not t%register[e]:
			q.append(e)
		if len(q) >= k:
			break
	t += p

for e in q:
	print(e)
