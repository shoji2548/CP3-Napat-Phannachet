menuList = []
def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number][0])

while True:
    menuName = input("Please Enter Menu : ")
    if (menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append([menuName, menuPrice])
def total():
    totalPrice = 0
    for i in range(len(menuList)):
        totalPrice += int(menuList[i][1])
    print("ราคาทั้งหมด = ",totalPrice)
showBill()
total()