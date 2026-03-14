num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number"))
op = input("Enter operation (+, -, *, /): ")

if op == '+':
    result = num1 + num2
    print("result:", result)

elif op == '-':
    result = num1 - num2
    print("result:", result)
    
elif op == '*':
    result = num1 * num2
    print("result:", result)

elif op == '/':
        if num2 == 0:
             print("Error: cant divide by zero!")
        else:
            result = num1 / num2
            print("result:", result)

else:
    print("Invalid operation!")
