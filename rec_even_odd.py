def even(num):
	if num < 2:
		return num % 2 == 0 
	return even(num - 2)

print(even(8))