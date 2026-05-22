def calculator(num1,num2,op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "can't divided by zero"
        return num1 / num2
    else:
        return "Invalid operation"
num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
op = input("Enter operations e.g.,+,-,*,/:")
result = calculator(num1,num2,op)
print(result)

