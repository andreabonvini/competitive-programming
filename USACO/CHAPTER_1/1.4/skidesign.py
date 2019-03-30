"""
ID: a.bonvi96
LANG: PYTHON3
PROG: skidesign
"""


with open('skidesign.in', 'r') as fin:
    N = int(fin.readline())
    hills = []  
    for i in range(N):
        hills.append(int(fin.readline()))

hills.sort()
list_of_prices = []

for start in range(min(hills), max(hills) - 17):  # start : start of the height range (17)
    end = start + 17                              # end : end of the height range
    # We try to limit our hills' height in a range of 17 values ( e.g. for the first test case: 1-18 , 2-19 , 3-20, 4-21 , 5-22 , 6-23 -->\n
    # we obserbe that the height range that minimize the cost is 4-21 )
    price = 0   # price for the change
    for hill in hills:
        if hill < start:
            price += (hill-start)**2
        elif hill > end:
            price += (hill-end)**2

    list_of_prices.append(price)

if not list_of_prices:
    result = 0
else:
	result = min(list_of_prices)

with open('skidesign.out', 'w') as fout:
    fout.write(str(result) + '\n')