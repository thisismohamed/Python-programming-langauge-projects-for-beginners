add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

def main():
    print("Simple calculator")
    num1 = float(input("Type first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Type second number: "))

    if operation == '+':
        result = add(num1,num2)
    elif operation == '-':
        result = subtract(num1,num2)
    elif operation == '*':
        result = multiply(num1,num2)
    elif operation == '/':
        result = divide(num1,num2)
    else:
        print("Invalid an operation!")
        return main()

    print("Result: %s" % result)

main()
