def add():
    first_number = float(input("Enter a number: "))
    second_number = float(input("Enter another number: "))
    print(first_number + second_number)


def subtract():
    first_number = float(input("Enter a number: "))
    second_number = float(input("Enter another number: "))
    print(first_number - second_number)

def multiply():
    first_number = float(input("Enter a number: "))
    second_number = float(input("Enter another number: "))
    print(first_number * second_number)


def divide():
    first_number = float(input("Enter a number: "))
    second_number = float(input("Enter another number: "))
    print(first_number / second_number)


operation = input("Please type +, - * or /")


if operation == "+":
    add()
elif operation == "-":
    subtract()
elif operation == "*":
    multiply()
elif operation == "/":
    divide()
else:
    print("That operation is not available")




