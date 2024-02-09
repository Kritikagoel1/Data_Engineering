# if with elif
letter = "A"
if letter == "B":
    print("letter is B")
elif letter == "C":
    print("letter is C")
else:
    print("letter isn't A, B or C")
#use of if else and nested if else
user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are eligible to vote.")
    if user_age >= 13 and user_age <= 19:
        print("You are a teenager.")
    else:
        print("You are not a teenager.")
else:
    print("You are not eligible to vote yet.")

#for loop
for i in range(1, 8):
    if i % 2 == 0:
        print(f"{i} is an even number.")
    else:
        print(f"{i} is an odd number.")


# Simple while loop example
counter = 1
while counter <= 5:
    print("Number:", counter)
    counter += 1

# Nested loop example
for i in range(3):
    for j in range(5):
        print(f"({i}, {j})", end=" ")
    print()

# Example with break, continue, and pass statements
for i in range(1, 11):
    if i % 2 == 0:
        print(f"Even number: {i}")
        continue
    elif i == 7:
        print("Breaking the loop at 7")
        break
    else:
        pass
    print(f"Number: {i}")
print("Loop finished.")


