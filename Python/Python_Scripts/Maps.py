'''def add(x, y):
    return x + y
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = map(add, list1, list2)
result_list = list(sum_list)
print(result_list)


#lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)
result_list = list(squared_numbers)
print(result_list)

#filter
numbers = [1, 2, 3, 4, 5]
squared_even_numbers = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
result_list = list(squared_even_numbers)
print(result_list)
'''
from functools import reduce
numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)
