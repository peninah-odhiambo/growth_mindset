def prime_number (n):
	for x in range (2, n+1):
		if n % x == 0 and n<2:
			print (n, "non prime number")

		else:
			print ("prime number")

	return n