P = int(input("enter principle:", ))
n = int(input("enter # of months:", ))
R = 0.2

r = R/(12*100)
EMI = P * r * ((1+r)**n)/((1+r)**n - 1)

for M in range (1, n):
    P = P-EMI
    print("EMI", EMI)
    print("Balance", P )
    print("----------")

