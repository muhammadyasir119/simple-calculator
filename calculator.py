num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
op = input("Enter operations e.g .,+,-,*,/:")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Can't divided by zero")
    else:
        print(num1 / num2)
