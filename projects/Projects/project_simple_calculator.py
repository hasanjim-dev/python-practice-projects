print("=== SIMPLE CALCULATOR ===")
print("Type 'exit' to quit\n")

while True:
    print("\nOperations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")

    choice = input("Enter operation (1/2/3/4/5): ")

    if choice == "5" or choice.lower() == "exit":
        print("Thanks for using calculator!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice! Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 == 0:
            print("Error! Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")