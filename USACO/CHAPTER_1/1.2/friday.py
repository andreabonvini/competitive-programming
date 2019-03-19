"""
ID: a.bonvi96
LANG: PYTHON3
PROG: friday
"""

months_d = {'Jan':31,'Feb':28,'Mar':31,'Apr':30,'May':31,'June':30,'July':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
months_d_b = {'Jan':31,'Feb':29,'Mar':31,'Apr':30,'May':31,'June':30,'July':31,'Aug':31,'Sep':30,'Oct':31,'Nov':30,'Dec':31}
# that's stupid
months = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec']
days = [0,0,0,0,0,0,0]

friday_ind = 0
y = 1900

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

N = int(fin.readline().strip())
while y < 1900 + N:
	if y%400 == 0 or y%4 == 0 and y%100!=0:
		for m in months:
			days[friday_ind]+=1
			friday_ind = (friday_ind + months_d_b[m]%7)%7
		y+=1
	else:
		for m in months:
			days[friday_ind]+=1
			friday_ind = (friday_ind + months_d[m]%7)%7
		y+=1
fout.write(' '.join(list(map(str,days))))
fout.write('\n')


fout.close()