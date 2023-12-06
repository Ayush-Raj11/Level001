########## WAP TO MAKE CALCULATOR  #############

        # Get input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, %): ")
num2 = float(input("Enter the second number: "))

        # Perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
else:
    print("Invalid operator. Please enter a valid operator.")

        ###########  Display the result
print(f"Result: {num1} {operator} {num2} = {result}")

