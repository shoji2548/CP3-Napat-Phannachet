num = int(input("จำนวนชั้นพีรมิด : "))
text2 = ""
for x in range(num):
    text1 = " "*(num-(x+1))
    if x < 2:
        for y in range(x+1):
            text2 += "*"
    else:
        for y in range(2):
            text2 += "*"
    print(text1+text2)