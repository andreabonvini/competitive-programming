"""
ID: a.bonvi96
LANG: PYTHON3
PROG: crypt1
"""
def isval(n):
	global D
	d = {}
	for el in D:
		d[el] = True
	z = list(map(int,list(str(n))))
	for el in z:
		if el not in d.keys():
			return False
	return True
with open('crypt1.in', 'r') as fin:
	N = int(fin.readline().strip())
	global D
	D = list(map(int,fin.readline().strip().split()))
	result = 0
	for a in D:
		for b in D:
			for c in D:
				for d in D:
					for e in D:
						x = a*100+b*10+c*1
						p1 = x*d
						p2 = x*e
						r = x*d+x*e*10
						if isval(p1) and isval(p2) and isval(r) and len(list(str(p1))) == 3 and len(list(str(p2))) == 3 and len(list(str(r))) == 4:
							result+=1


with open('crypt1.out', 'w') as fout:
	fout.write(str(result) + '\n')