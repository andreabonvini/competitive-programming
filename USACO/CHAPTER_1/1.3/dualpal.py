"""
ID: a.bonvi96
LANG: PYTHON3
PROG: dualpal
"""
dic = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
fin = open('dualpal.in', 'r')
fout = open('dualpal.out', 'w')
N,S = list(map(int,fin.readline().strip().split()))

def conv(B,n):
	q = n
	x = []
	while q != 0:
		x.append(dic[q%B])
		q //=B
	x = x[::-1]
	return ''.join(x)

def is_pal(x):
	if x == x[::-1]:
		return True
	else:
		return False
r = []
piv = S+1
c = 0
i = 0
while True:
	if i == N:
		break
	while True:
		if is_pal(str(piv)):
			c +=1
		for j in range(2,10):
			if is_pal(conv(j,piv)):
				c+=1
				if c == 2:
					i+=1
					r.append(piv)
					break
		piv+=1		
		c=0
		break
		

r = list(map(str,r))
fout.write('\n'.join(r))
fout.write('\n')
	
	

fout.close()
