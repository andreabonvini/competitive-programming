
import sys
import io
import copy


input_file = open('A-large-practice.in', 'r')
sys.stdin = io.StringIO(input_file.read())

##########################################


def solve(row,k):
    row1 = [1 if el == '+' else -1 for el in row ]
    pivot = 0
    n = 0
    for i in range(len(row1)-k+1):
        if row1[i] == -1:
            pivot = i
            n+=1
            for j in range(pivot,pivot+k):
                row1[j]*=-1
    if sum(row1) == len(row1):
        return n
    else:
        return 'IMPOSSIBLE'

T = int(sys.stdin.readline())
f = open('A-large-practice.txt','w')

for x in range(T):
    row,k = sys.stdin.readline().split()
    k = int(k)
    y = solve(row,k)
    f.write('Case #{}: {}\n'.format(x+1,y))

f.close()
