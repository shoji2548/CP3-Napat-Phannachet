class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added product to ",self.name,self.lastName,"'s Cart")

customer1 = Customer()
customer1.name = "Napat"
customer1.lastName = "Phannachet"
customer1.addCart()

customer2 = Customer()
customer2.name = "Kititwin"
customer2.lastName = "Phannachet"
customer2.addCart()

customer3 = Customer()
customer3.name = "Phattalapon"
customer3.lastName = "Phannachet"
customer3.addCart()