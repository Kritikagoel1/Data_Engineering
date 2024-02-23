#capitalise
text = "hello, world!"
print(text.capitalize())
#upper
text = "hello, world!"
print(text.upper())
#lower
text = "Hello, World!"
print(text.lower())
#replace
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)
#strip
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)
#split
text = "apple,banana,orange"
fruits = text.split(',')
print(fruits)
#join
fruits = ['apple', 'banana', 'orange']
text = ', '.join(fruits)
print(text)  # Output: 'apple, banana, orange'
#count
message = 'Have a Good Day'
print('Number of occurrence of a:', message.count('a'))
#find
message = 'Have a Good Day'
print(message.find('Day'))


