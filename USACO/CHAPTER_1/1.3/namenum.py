"""
ID: a.bonvi96
LANG: PYTHON3
PROG: namenum
"""
tt = {'A':[2],'B':[2],'C':[2],'D':[3],'E':[3],'F':[3],'G':[4],'H':[4],'I':[4],'J':[5],'K':[5],'L':[5],'M':[6],'N':[6],'O':[6],'P':[7],'R':[7],'S':[7],'T':[8],'U':[8],'V':[8],'W':[9],'X':[9],'Y':[9]}
d = []
d_file = open('dict.txt','r')
while True:
	x = d_file.readline().strip()
	if x == '':
		break
	else:
		if not 'Z' in list(x) and 'Q' not in list(x):
			d.append(x)
d_file.close()
dic = {}
for el in d:
	x = list(el)
	r = []
	for l in x:
		for n2 in tt[l]:
			r.append(str(n2))
	n3 = ''.join(r)
	if n3 not in dic.keys():
		dic[n3] =  [el]
	else:
		dic[n3].append(el)

fin = open('namenum.in', 'r')
fout = open('namenum.out', 'w')

fout.close()