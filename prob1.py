number = 123

digits_sum = lambda x: sum(int(digit) for digit in str(x))

print(f"The sum of the digits of {number} is {digits_sum(number)}")