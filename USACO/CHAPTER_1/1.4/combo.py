"""
ID: a.bonvi96
LANG: PYTHON3
PROG: combo
"""

with open('combo.in', 'r') as fin:
	N = int(fin.readline().strip())
	FJ = list(map(int,fin.readline().strip().split()))
	MC = list(map(int,fin.readline().strip().split()))
def adj(l,N):
	res = []
	if N == 1:
		return [1 for _ in range(5)] 
	else:
		for el in l:
			if el > N:
				res.append(el%N)
			elif el < 1:
				res.append(el+N)
			else:
				res.append(el)
		return res
s = set()
f1,f2,f3 = list(range(FJ[0]-2,FJ[0]+3)),list(range(FJ[1]-2,FJ[1]+3)),list(range(FJ[2]-2,FJ[2]+3))
m1,m2,m3 = list(range(MC[0]-2,MC[0]+3)),list(range(MC[1]-2,MC[1]+3)),list(range(MC[2]-2,MC[2]+3))
fj = [f1,f2,f3]
mc = [m1,m2,m3]
for i in range(3):
	fj[i] = adj(fj[i],N)
	mc[i] = adj(mc[i],N)

for el1 in fj[0]: 
	for el2 in fj[1]:
		for el3 in fj[2]:
			s.add((el1,el2,el3))
for el1 in mc[0]:
	for el2 in mc[1]:
		for el3 in mc[2]:
			s.add((el1,el2,el3))
result = len(s)
with open('combo.out', 'w') as fout:
	fout.write(str(result) + '\n')