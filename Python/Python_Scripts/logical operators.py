# Example using 'and' operator
x = 5
y = 10

if x > 0 and y > 0:
    print("Both x and y are positive.")
else:
    print("At least one of x or y is not positive.")

# Example using 'or' operator
x = -5
y = 10

if x > 0 or y > 0:
    print("At least one of x or y is positive.")
else:
    print("Neither x nor y is positive.")

# Example using 'not' operator
x = True
if not x:
    print("x is False.")
else:
    print("x is True.")
