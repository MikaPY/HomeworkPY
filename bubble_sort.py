def bubbleSort(arr):
	n = len(arr)

	# Проход через все элементы arr.
	for i in range(n):

		# Последние элементы i 
		for j in range(0,n-i-1):

			# Проход arr  от 0 до n-i-1.
			'''Смена элементов, если найденный элемент больше
			чем следующий'''

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1],arr[j]

arr = [55,34,25,11,9,88,123]

bubbleSort(arr)

print('Sorted arr is:')
for i in range(len(arr)):
	print('%d' %arr[i])