class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c
calc = Calculator()
result1 = calc.add(5)
result2 = calc.add(5, 10)
result3 = calc.add(5, 10, 15)
print(result1)
print(result2)
print(result3)
