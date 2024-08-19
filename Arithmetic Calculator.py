#Simple Calculator with basic arithmetic operations

def calculator():
    
    #Prompting user to input two numbers and an operation choice
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    operation = input("Choose operation to perform(+,-,*,/):")

    if operation == "+":
        res = num1 +  num2
    elif operation == "-":
        res = num1 - num2
    elif operation == "*":
        res = num1 * num2
    elif operation == "/":
        if num2 != 0:
            res = num1/num2
        else:
            print("Result is not defined")
            return
    else:
        print("Invalid operation! Please enter a valid operation.")
        return

    #Displaying the result
    print("Result:",res)
    
#Calling the calculator function
calculator()
