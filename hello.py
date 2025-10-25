class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Cannot divide by zero."
        return self.num1 / self.num2

# Main part of the program
while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            calc = Calculator(num1, num2) # Create a Calculator object

            if choice == '1':
                print(f"Result: {calc.add()}")
            elif choice == '2':
                print(f"Result: {calc.subtract()}")
            elif choice == '3':
                print(f"Result: {calc.multiply()}")
            elif choice == '4':
                print(f"calc.divide()")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    elif choice == '5':
        print("Exiting the calculator.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")