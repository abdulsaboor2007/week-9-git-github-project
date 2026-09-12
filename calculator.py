print("===== SIMPLE CALCULATOR =====")

number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("+ Addition")
print("- Subtraction")
print("* Multiplication")
print("/ Division")

choice = input("Enter your choice: ")

if choice == "+":
    print("Answer:", number1 + number2)
elif choice == "-":
    print("Answer:", number1 - number2)
elif choice == "*":
    print("Answer:", number1 * number2)
elif choice == "/":
    if number2 == 0:
        print("Division by zero is not possible.")
    else:
        print("Answer:", number1 / number2)
else:
    print("Invalid operation.")
