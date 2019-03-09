from collections import defaultdict
from itertools import count
import sys
import io
input_file = open('C-large-practice.in', 'r')
sys.stdin = io.StringIO(input_file.read())
f = open('C-large-practice.txt','w')

for cas in range(1,1+int(sys.stdin.readline().strip())):
    n, k = map(int, sys.stdin.readline().strip().split())
    pieces = [n]
    ct = defaultdict(int)
    ct[n] += 1
    for i in count():
        n = pieces[i]
        c = ct[n]
        mx, mn = n>>1, n-1>>1
        if k <= c:
            break
        k -= c
        if mx not in ct: pieces.append(mx)
        ct[mx] += c
        if mn not in ct: pieces.append(mn)
        ct[mn] += c

    f.write("Case #%s: %s %s\n" % (cas, mx, mn))
f.close()
