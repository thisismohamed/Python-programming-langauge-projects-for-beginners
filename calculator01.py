def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise  ValueError("Cannot divide by zero!")
    return num1 / num2

def main():
    num1 = float(input("Type first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Type second number: "))

    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Invalid an operation!")
        return main()

    print("Result: %f" % (result))
    #main()

main()
