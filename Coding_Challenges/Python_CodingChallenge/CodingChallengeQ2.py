# Using lambda with map
numbers = [1, 2, 3, 4, 5]
cubed_numbers = list(map(lambda x: x**3, numbers))
print(cubed_numbers)

# Using lambda with filter
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

# Using lambda with sorted
reverse_sorted_numbers = sorted(numbers, key=lambda x: -x)
print(reverse_sorted_numbers)

import json
json_string = '{"name": "Kritika", "age": 22, "address":{"city": "Bareilly"}}'
python_dict = json.loads(json_string)
print(python_dict)

