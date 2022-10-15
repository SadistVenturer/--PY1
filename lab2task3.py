list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO Оформить решение
maxValue = max(list_numbers)
list_numbers.insert(20, maxValue)
del list_numbers[19]
del list_numbers[9]
list_numbers.insert(10, 25)
print(maxValue)
print(list_numbers)