# Creating a dictionary
my_dict = {"name": "John", "age": 25, "city": "New York"}
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
my_dict["age"] = 26
print("Updated age:", my_dict["age"])
my_dict["occupation"] = "Engineer"
print("Updated dictionary:", my_dict)
del my_dict["city"]
print("Dictionary after removing 'city':", my_dict)

if "city" in my_dict:
    print("City:", my_dict["city"])
else:
    print("City not found in the dictionary.")
keys = my_dict.keys()
print("Keys:", keys)
values = my_dict.values()
print("Values:", values)
items = my_dict.items()
print("Items:", items)
occupation = my_dict.pop("occupation")
print("Removed occupation:", occupation)
print("Updated dictionary:", my_dict)
new_data = {"country": "USA", "age": 27}
my_dict.update(new_data)
print("Updated dictionary:", my_dict)
