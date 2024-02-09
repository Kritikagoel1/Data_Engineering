def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

#function with parameters
def add_numbers(a, b):
    return a + b
result = add_numbers(5, 3)
print("Sum:", result)

#default arguments
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

#Keyword Arguments
def student(firstname, lastname):
    print(firstname, lastname)
student(firstname='Hexa', lastname='Practice')
student(lastname='Practice', firstname='Hexa')

#variable-length arguments
def print_args(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

print_args(1, 2, 3, name="John", age=25)


# Positional argument
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is ", age)
print("Case-1:")
nameAge("Suraj", 27)
# You will get incorrect output because
# argument is not in order
print("\nCase-2:")
nameAge(27, "Suraj")

#use of docstring
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
print(evenOdd.__doc__)