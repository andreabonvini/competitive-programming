"""
ID: a.bonvi96
LANG: PYTHON3
PROG: milk
"""

fin = open('milk.in', 'r')
fout = open('milk.out', 'w')
N,M = list(map(int,fin.readline().strip().split()))
farmers =  []
for _ in range(M):
	farmers.append(list(map(int,fin.readline().strip().split())))
farmers = sorted(farmers,key = lambda x: x[0])
tmp_m = 0
tmp_q = 0
for farmer in farmers:
	if tmp_q == N:
		break
	elif tmp_q + farmer[1]<=N:
		tmp_q+=farmer[1]
		tmp_m+=farmer[1]*farmer[0]
	else:
		rest  = N - tmp_q
		tmp_q +=rest
		tmp_m+=farmer[0]*rest


		
fout.write('{}\n'.format(tmp_m))
fout.close()
