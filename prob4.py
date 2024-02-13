def find_intersection(list1, list2):
    intersection = list(filter(lambda x: x in list2, list1))
    return intersection


list1 = [2, 4, 6, 8, 10]
list2 = [4, 8, 12, 16, 20]

print(f"{find_intersection(list1, list2)} are found in both lists")
