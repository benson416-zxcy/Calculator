def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 // num2  # Use / for float division if you want

while True:
    num1 = input("Enter a number: ")
    num2 = input("Enter a second number: ")
    op = input("Enter an operation [+, -, *, / ] or \"q\" to quit: ")
    

    if op == "q":
        print("Goodbye!")
        break
    

    if not num1.isdigit() or not num2.isdigit():
        print("Invalid Input")
        continue
    else:
        num1 = int(num1)
        num2 = int(num2)

    if (op == "/" or op == "//") and num2 == 0:
        print("Cannot divide by zero")
        continue


    if op == "+":
        ans = add(num1, num2)
    elif op == "-":
        ans = subtract(num1, num2)
    elif op == "*":
        ans = multiply(num1, num2)
    elif op == "/" or op == "//":
        ans = divide(num1, num2)
    else:
        print("Invalid Operation")
        continue


    print("Answer: ", ans)