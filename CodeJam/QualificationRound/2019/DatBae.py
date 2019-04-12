import sys
import numpy as np


T = int(sys.stdin.readline().strip())

# T : number of test cases
for _ in range(T):
	N,B,F = list(map(int,sys.stdin.readline().strip().split()))

	# N : number of workers
	# B : number of broken workers
	# F : number of possible queries

	answers = []  # here we'll store all the values returned by the workers

	step = 1

	# when step == 1 we'll send a message like this: 0101010101...
	# if step == 2 we'll send a message liker this: 001100110011...
	# if step == 4 we'll send a message like this: 0000111100001111...
	# and so on...

	for _ in range(5):
		to_send = []
		L = [[0 for _ in range(step)],[1 for _ in range(step)]]
		tmp = 0
		while len(to_send) + step < N:
			to_send+=L[tmp]
			if tmp == 0:
				tmp = 1
			else:
				tmp = 0

		# if any ending value is missing from our message we add it with these two lines of code:
		tail = [ tmp for _ in range(N-len(to_send))]
		to_send += tail

		# time to ship our message
		print(''.join(list(map(str,to_send))),flush = True)

		# time to get an answer
		answer = list(map(int,list(sys.stdin.readline().strip())))

		# and add it to our collection
		answers.append(answer)

		# time to dobule our step
		step*=2

	# here we transform our answers matrix in its transpose and convert the numbers on its rows
	# in decimal numbers (row[::-1] is necessary since we want the leas significant bit on the right)
	answers = np.array(answers)
	answers = answers.T
	indexes = [int(''.join(list(map(str,list(row[::-1])))),2) for row in answers]

	# everytime we get an overflow (every 32 numbers) we increment the previous number
	# we realize that we had an overflow by checking if a number is less than the previous one.
	number_of_overflows = 0
	previous = -1

	for i in range(len(indexes)):
		if indexes[i] < previous:
			number_of_overflows+=1
		previous = indexes[i]
		indexes[i]+=32*number_of_overflows
	

	# in order to get our result we just compute the set difference between 
	# all the numbers up to N and the indexes we found
	broken_workers = set(range(N))-set(indexes)
	broken_workers = list(broken_workers)
	broken_workers.sort()
	print(' '.join(list(map(str,broken_workers))),flush = True)

	verdict = int(sys.stdin.readline().strip())
	# we trust that the verdict is equal to 1

sys.exit()