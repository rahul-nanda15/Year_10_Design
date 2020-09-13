def isEven(a):
	if a % 2 == 0:
		return True

	return False

for i in range(0,10,3):
	print(isEven(i))