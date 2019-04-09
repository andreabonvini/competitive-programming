import sys
def solve(N):
    A = str(N)
    A = A.replace('4','3')
    A = int(A)
    B = N-A
    return A,B
    
T = int(sys.stdin.readline().strip())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    A,B = solve(N)
    print('Case #{}: {} {}'.format(i+1,A,B))