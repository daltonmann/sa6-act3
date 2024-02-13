def raise_numbers(numbers, n):
    powered_numbers = list(map(lambda x: x**2, list1))
    return powered_numbers

list1 = [1, 2, 3, 4, 5]
n = 2

print(f"Your list to the {n} power is {raise_numbers(list1, n)}")
