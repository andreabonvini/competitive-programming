"""
ID: a.bonvi96
LANG: PYTHON3
PROG: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
NP = int(fin.readline().strip())
names = {}
x = []
for _ in range(NP):
	n = fin.readline().strip()
	names[n] = 0
	x.append(n)

for _ in range(NP):
	name = fin.readline().strip()
	money, NG= list(map(int,fin.readline().strip().split()))
	if NG != 0:
		gift = money // NG
		names[name] -= money - money%NG
		for _ in range(NG):
			names[fin.readline().strip()]+=gift
			#names[name]+=gift

for el in x:
	fout.write('{} {}\n'.format(el,names[el]))

fout.close()