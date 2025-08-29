number1 = int(input("Type the first number: "))
operator = (input("Enter symbol: "))
number2 = int(input("Type the second number: "))

if operator == "+":
    print("The addition is: ", number1 + number2)
elif operator == "-":
    print("The difference is: ", number1 - number2)
elif operator == "*":
    print("The multiplication is: ", number1 * number2)
elif operator == "/":
    print("The division is: ", number1 / number2)
