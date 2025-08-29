a = int(input("Enter A Number: "))
b = int(input("Enter B Number: "))
c = int(input("Enter C Number: "))

if a > b and a > c:
    print("A is the Greatest")
elif b > a and b > c:
    print("B is the Greatest")
else:
    print("C is the Greatest")