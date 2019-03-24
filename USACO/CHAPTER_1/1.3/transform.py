"""
ID: a.bonvi96
LANG: PYTHON3
PROG: transform
"""


fin = open('transform.in', 'r')
fout = open('transform.out', 'w')

N = int(fin.readline().strip())
mat1 = []
mat2 = []

for _ in range(N):
	mat1.append(list(fin.readline().strip()))
for _ in range(N):
	mat2.append(list(fin.readline().strip()))
def foo90(m):
    x = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(m)):
        for j in range(len(m)):
            x[i][len(m)-1-j] = m[j][i]
    return x
def foo180(m):
    x = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(m)):
        for j in range(len(m)):
            x[len(m)-1-i][len(m)-1-j] = m[i][j]
    return x

def foo270(m):
    x = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(m)):
        for j in range(len(m)):
            x[len(m)-1-i][j] = m[j][i]
    return x
def fooR(m):
    x = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(len(m)):
        for j in range(len(m)):
            x[j][len(m)-1-i] = m[j][i]
    return x

mat90 = foo90(mat1) 
mat180 = foo180(mat1)
mat270 = foo270(mat1)
matR = fooR(mat1)
matC1 = foo90(matR)
matC2 = foo180(matR)
matC3 = foo270(matR)

if mat2 == mat90:
	fout.write('1\n')
elif mat2 == mat180:
	fout.write('2\n')
elif mat2 == mat270:
	fout.write('3\n')
elif mat2 == matR:
	fout.write('4\n')
elif mat2 == matC1 or mat2 == matC2 or mat2 == matC3:
	fout.write('5\n')
elif mat2 == mat1:
	fout.write('6\n')
else:
	fout.write('7\n')
fout.close()

