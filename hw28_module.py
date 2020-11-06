
# Finding the factorial.

def fact(n):
	if n == 0:
		return 1 
	return fact(n-1) * n


#Finding volume and area of a cylinder.

def vol(r,h):
	v = (3.14*(r**2))*h
	return v 



def area(r,h):
	s = 2 * 3.14 * r * (r + h)
	return s


# Convert degree to radian.
def degree_radian(degree):
	r = 3.14 *(degree/180)
	return r 






