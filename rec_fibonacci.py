def rec_fib(n):
	if n <= 0:
		print('')
	elif n == 1:
		return 0
	elif n == 2:
		return 1 
	else:
		return rec_fib(n - 1) + rec_fib(n - 2)

print(rec_fib(9))