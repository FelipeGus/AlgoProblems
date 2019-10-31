
def decDigitToRoman(num, digits):
	roman = ''
	num = num % 10
	
	if (num == 9):
		return digits[0] + digits[2]
	
	if num >= 5:
		roman += digits[1]
		num -= 5
	
	if num % 5 == 4:
		return roman + digits[0] + digits[1]
	else:
		return roman + (digits[0] * num)
		
	
def intToRoman(num):
	roman = 'M' * int(num / 1000)
	num = num % 1000
	
	roman += decDigitToRoman(int(num / 100), ['C', 'D', 'M'])
	num = num % 100

	roman += decDigitToRoman(int(num / 10), ['X', 'L', 'C'])
	num = num % 10

	roman += decDigitToRoman(int(num), ['I', 'V', 'X'])
	
	return roman


