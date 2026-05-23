4def calculator():
    print("\n-- Menu --")
    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
    print("5: Exit")

    choice = input("Enter choice: ")

    if choice == "5":
        print("Program end ")
        return None

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        return num1 + num2

    elif choice == "2":
        return num1 - num2

    elif choice == "3":
        return num1 * num2

    elif choice == "4":
        if num2 == 0:
            return "Can't divide by zero "
        return num1 / num2

    else:
        return "Invalid choice "


# Loop
while True:
    result = calculator()

    if result is None:
        break

    print("Result:", result)