"""
ID: a.bonvi96
LANG: PYTHON3
PROG: beads
"""

import re

fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')
N = int(fin.readline().strip())
breads = fin.readline().strip()

x = re.findall('b+|r+|w+',breads)*2
x = x[:len(x)-1]

m = 0
if len(x) == 1:
	fout.write(str(len(x[0]))+'\n')
else:
	for i in range(len(x)-1):
	    r = 0
	    j = i
	    flag = False
	    while True:
	        if j >= len(x)-1:
	            break
	        elif 'w' in x[j]:
	            r+=len(x[j])
	            
	        elif 'r' in x[j] and (not flag or flag == 'r'):
	            r+=len(x[j])
	            flag = 'r'
	            
	        elif 'b' in x[j] and (not flag or flag == 'b'):
	            r+=len(x[j])
	            flag = 'b'
	            
	        elif 'r' in x[j] and (flag == 'b' or flag == 'rs'):
	            r+=len(x[j])
	            flag = 'rs'
	        
	        elif 'b' in x[j] and (flag == 'r' or flag == 'bs'):
	            r+=len(x[j])
	            flag = 'bs'
	            
	        else:
	            break
	        j+=1
	    
	    if r > m:
	        m = r
	fout.write(str(m)+'\n')



fout.close()