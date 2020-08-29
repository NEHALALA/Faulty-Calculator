n1 = int(input("Enter a First Number"))
n2 = int(input("Enter a Second Number"))
v1 = str(input("Choose a Operataor"+"+,-,*,/,**"))
print(v1)
if n1 == 56 and n2 == 9 and  v1== "+":
    print("77")
elif n1 == 56 and n2  == 6 and v1 == "*":
    print("77")
elif n1 == 45 and  n2 == 3 and v1 == "/":
    print("555")
elif v1 == "+":
    A = n1 + n2
    print(A)
elif v1 == "*":
    B = n1 * n2
    print(B)
elif v1 == "-":
    C = n1 - n2
    print(C)
elif v1 == "/":
    D = n1 / n2
    print(D)
elif v1 == "**":
    E = n1 ** n2
    print(E)




