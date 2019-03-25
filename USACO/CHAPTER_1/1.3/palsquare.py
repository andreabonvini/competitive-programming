"""
ID: a.bonvi96
LANG: PYTHON3
PROG: palsquare
"""

dic = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'A',11:'B',12:'C',13:'D',14:'E',15:'F',16:'G',17:'H',18:'I',19:'L',20:'M'}
fin = open('palsquare.in', 'r')
fout = open('palsquare.out', 'w')
B = int(fin.readline().strip())
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
nums = []
for i in range(1,301):
	x = conv(B,i**2)
	if is_pal(x):
		nums.append([conv(B,i),x])
for n in nums:
	fout.write('{}\n'.format(' '.join(n)))

fout.close()

