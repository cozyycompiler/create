import math

def calculator():
    print("╔════════════════════════════╗")
    print("║     🌸 MATH CALCULATOR     ║")
    print("╚════════════════════════════╝")

    while True:
        print("\nChoose an operation:")
        print("1. ➕ Addition")
        print("2. ➖ Subtraction")
        print("3. ✖️ Multiplication")
        print("4. ➗ Division")
        print("5. √ Square Root")
        print("6. 💗 Exit")

        choice = input("\nEnter choice: ")

        if choice == "6":
            print("\n🌷 Thank you for using the calculator!")
            break

        if choice == "5":
            number = float(input("Enter a number: "))

            if number >= 0:
                print("√", number, "=", math.sqrt(number))
            else:
                print("❌ Cannot find the square root of a negative number.")

        elif choice in ["1", "2", "3", "4"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("✨ Answer:", a + b)

            elif choice == "2":
                print("✨ Answer:", a - b)

            elif choice == "3":
                print("✨ Answer:", a * b)

            elif choice == "4":
                if b != 0:
                    print("✨ Answer:", a / b)
                else:
                    print("❌ Cannot divide by zero.")

        else:
            print("❌ Invalid choice.")


calculator()
