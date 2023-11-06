# Write a program to perform simple math based on the user inputs by using Switch condition.(+ , - , * , /)

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


print("Options:")
print("Enter '+' for addition")
print("Enter '-' for subtraction")
print("Enter '*' for multiplication")
print("Enter '/' for division")

choice = input("Enter operator: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = None

if choice == '+':
    result = add(num1, num2)
elif choice == '-':
    result = subtract(num1, num2)
elif choice == '*':
    result = multiply(num1, num2)
elif choice == '/':
    result = divide(num1, num2)
else:
    result = "Invalid input"

print("Result: ", result)
