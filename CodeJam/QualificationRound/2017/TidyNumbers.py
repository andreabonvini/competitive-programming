
import sys
import io
import copy


input_file = open('B-large-practice.in', 'r')
sys.stdin = io.StringIO(input_file.read())

##########################################

T = int(sys.stdin.readline())
f = open('B-large-practice.txt','w')

def change_n(n,vec):
	if vec[0] == 0 and n[0] == 1:
		n[0] = 0
		for i in range(1,len(vec)):
			n[vec[i]] = 9
	else:
		n[vec[0]]-=1
		for el in vec[1:]:
			n[el]=9
	for k in range(vec[-1]+1,len(n)):
		n[k] = 9
	return n

def solve(n):
	if len(n) == 1:
		return n[0]
	else:
		vec = []
		# DEVI STARE ATTENTO AI NUMERI CON PIù LEADING NUMBERS TIPO 34442 -> NOT 34439!
		for i in range(1,len(n)):
			if n[i-1] > n[i]:
				vec.append(i-1)
				n = change_n(n,vec)
			elif n[i-1] == n[i]:
				vec.append(i-1)
			else:
				vec = []
		x = list(map(str,n))
		x = ''.join(x)
		return int(x)

for x in range(T):
	a = sys.stdin.readline().strip()
	n = list(map(int,list(a)))
	y = solve(n)
	if x == T-1:
		f.write('Case #{}: {}'.format(x+1,y))
	else:
		f.write('Case #{}: {}\n'.format(x+1,y))

f.close()

# 11411234445899 1999999999999