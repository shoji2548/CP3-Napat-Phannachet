USN = input("Username = ")
PSW = input("Password = ")
if USN == "Oshi" and PSW == "2548":
    print("Welcome")
    print("---- Oshi Shop ----")
    print("1.Banana = 10 THB\n2.Apple = 5 THB\n3.Watermelon = 40 THB")
    print("What do you want to buy ?")
    B = int(input("Banana = "))
    A = int(input("Apple = "))
    W = int(input("Watermelon = "))
    r1, r2, r3 = 0, 0, 0
    if B > 0:
        r1 = 10*B
    if A > 0:
        r2 = 5*A
    if W > 0:
        r3 = 40*W
    print(r1+r2+r3)
else:
    print("Username or Password is incorrect")