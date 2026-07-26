print("===== Calculator =====")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Choose (1-4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    answer = num1 + num2
    print("Answer =", answer)

elif choice == "2":
    answer = num1 - num2
    print("Answer =", answer)

elif choice == "3":
    answer = num1 * num2
    print("Answer =", answer)

elif choice == "4":
    if num2 != 0:
        answer = num1 / num2
        print("Answer =", answer)
    else:
        print("Error: Cannot divide by zero!")

else:
    print("Invalid choice!")