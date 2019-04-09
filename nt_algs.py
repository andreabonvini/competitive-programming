def EuclideanAlgorithm(a, b):
	# Efficient way to find the GCD of two numbers a & b
	while b:
		a, b = b, a % b
	return a