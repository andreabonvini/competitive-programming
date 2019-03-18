"""
ID: a.bonvi96
LANG: PYTHON3
PROG: ride 
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

comet = fin.readline().strip()
group = fin.readline().strip()
c = 1
g = 1
for el in comet:
	c *= ord(el)-64
for el in group:
	g *= ord(el)-64

if g%47 == c%47:
	fout.write ('GO\n')
else:
	fout.write ('STAY\n')
