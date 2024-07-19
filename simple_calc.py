def calculator():
    # Prompt the user to input the first number
    num1 = float(input("Enter the first number: "))
    
    # Prompt the user to input the second number
    num2 = float(input("Enter the second number: "))
    
    # Prompt the user to choose an operation
    operation = input("Choose an operation (+, -, *, /): ")
    
    # Perform the chosen operation and display the result
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}.")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}.")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}.")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}.")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation. Please choose from +, -, *, /.")

# Call the calculator function
calculator()
