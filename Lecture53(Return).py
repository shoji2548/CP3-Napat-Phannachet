def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
print(vatCalculate(totalprice = int(input("จำนวนเงินทั้งหมด : "))))
