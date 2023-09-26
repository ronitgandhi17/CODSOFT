def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero."
    return x / y

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'quit' to end the program")
    
    choice = input("Enter your choice: ")
    
    if choice == "quit":
        break
    
    if choice in ("add", "subtract", "multiply", "divide"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == "add":
            result = add(num1, num2)
            print("Result: ", result)
        elif choice == "subtract":
            result = subtract(num1, num2)
            print("Result: ", result)
        elif choice == "multiply":
            result = multiply(num1, num2)
            print("Result: ", result)
        elif choice == "divide":
            result = divide(num1, num2)
            print("Result: ", result)
    else:
        print("Invalid input. Please try again.")