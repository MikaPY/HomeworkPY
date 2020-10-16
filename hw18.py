# #ARITHMETIC AVERAGE
# stu_score = [5,4,5,5,9,7]
# res_score = sum(stu_score) / len(stu_score)
# print(res_score,' - Students rating')


# st_list = []
# st_score = {'Mike': 5, 'John': 3, 'Bob': 3, 'Fred': 7}
# for v in st_score.values():
# 	st_list.append(v) 
# print(sum(st_list) / len(st_list))



# st_zero = 0
# st_score = {'Mike': 5, 'John': 3, 'Bob': 3, 'Fred': 7}
# for v in st_score.values():
# 	if v > st_zero:
# 		st_zero = v 
# print(v)


# st_good = 5 
# st_score = {'Mike': 5, 'John': 3, 'Bob': 3, 'Fred': 7, 'George': 9, 'Irven': 11}
# for v in st_score.values():
# 	if v > st_good:
# 		print(v)


# 
the_sum = 0
print('\n\t\tСамый большой материк на планете Земля ? : ' ) 
ask1 = input('\n1 Евразия \n2 Африка, \n3 Южная Америка \n4 Антаркдита \n\t\tEnter: ') == '1'

if ask1:
	the_sum += 500
	print('Ok', the_sum)
else:
	print('Not ok', the_sum)