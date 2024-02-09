#Lists
my_list = [1, 2, 3, 4, 5]
print("First element:", my_list[0])
my_list[2] = 10
print("Modified list:", my_list)
my_list.append(6)
print("List after appending:", my_list)
my_list.remove(4)
print("List after removing 4:", my_list)
print("Length of the list:", len(my_list))
my_list.insert(1, 5)
print(my_list)
popped_value = my_list.pop(1)
print(my_list)
print(popped_value)
print("List elements:")
for item in my_list:
    print(item)

#slicin
mylist = [1, 2, 3, 4, 5,6]
sublist = mylist[1:4]
print(sublist)
sublist_with_step = mylist[::2]
print(sublist_with_step)
last_two_elements = mylist[-2:]
print(last_two_elements)



