#Módulo de números de Fibonacci

def fib(n):  # escribir series de Fibonacci hasta n
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a + b
	print()

def fib2(n): # devolver series de Fibonacci hasta n
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a + b
	return result



