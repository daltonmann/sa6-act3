def find_max(numbers, comp_nums):
    maximum = numbers[0]
    
    for num in numbers[1:]:
        if comp_nums(maximum, num):
            maximum = num
    return maximum

comp_nums = lambda x, y: x < y

numbers = [1, 4, 3, 3, 8, 2]
print(f"Maximum number in the list: {find_max(numbers, comp_nums)}")