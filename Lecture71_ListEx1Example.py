menuList = []
priceList = []
def showBill():
    print("----My Food----")
    for number in range(len(menuList)):
        print(menuList[number], priceList[number])
def total():
    totalPrice = 0
    for i in range(len(priceList)):
        totalPrice += int(priceList[i])
    print("ราคาทั้งหมด = ",totalPrice)
while True:
    menuName = input("Please Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = input("Price : ")
        menuList.append(menuName)
        priceList.append(menuPrice)
print(menuList,":",priceList)
showBill()
total()