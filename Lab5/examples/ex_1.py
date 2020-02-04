def sumTillNum(num):
	sum = 0
	i = 1
	while(i != num+1):
		sum = sum + i
		i = i+1
	return sum

print(sumTillNum(10))
