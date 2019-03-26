"""
ID: a.bonvi96
LANG: PYTHON3
PROG: barn1
"""
with open('barn1.in', 'r') as fin:
	M, S, C = map(int, fin.readline().split())
	cows = list(map(int, fin.read()[:-1].split('\n')))
	cows.sort()

if M >= C:
	result = C
else:
	gaps = [(cows[i+1] - cows[i] - 1) for i in range(C-1)]
	gaps.sort()
	mg = 0
	for i in range(M-1):
		mg += gaps.pop()
	result = max(cows) - min(cows) + 1 - mg

with open('barn1.out', 'w') as fout:
	fout.write(str(result) + '\n')