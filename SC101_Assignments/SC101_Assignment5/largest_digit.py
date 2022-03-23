"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n:
	:return:
	"""
	if n < 0:
		string = str(-n)
	else:
		string = str(n)
	x = find_largest_digit_helper(string, 0)
	return x


def find_largest_digit_helper(string, start_biggest):
	if len(string) >= 1:
		if int(string[0]) > start_biggest:
			biggest = int(string[0])
		else:
			biggest = start_biggest
	if len(string) > 1:
		return find_largest_digit_helper(string[1:], biggest)
	else:
		return biggest





if __name__ == '__main__':
	main()
