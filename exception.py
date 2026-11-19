# Write a calculator that asks for two numbers and divides them, handling invalid input and division by zero separately, with a finally message that always prints.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", a / b)

except ValueError:
    print("Invalid input! Enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

finally:
    print("Calculator finished.")