def reverse(x):
	result, x_remaining = 0, abs(x)
	while x_remaining:
		result = result * 10 + x_remaining % 10
		x_remaining //= 10
	print(-result if x < 0 else result)

reverse(1101)
