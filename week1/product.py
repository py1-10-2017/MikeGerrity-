class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"

        self.display_info()

    def sell(self): 
        print "Product " + self.item_name + "has been sold"
        self.status = "sold"
        return self

    def tax(self): 
        tax = 0.06
        price = self.price + (self.price * tax)
        print "Total item cost = $" + str(price)
        return self

    def rtn(self, rtn_reason):
        print "Product " + self.item_name + "has been returned"
        if rtn_reason == "defective": 
            self.status = "defective"
            self.price = 0
        elif rtn_reason == "like_new": 
            self.status = "for sale"
        elif rtn_reason == "open": 
            self.status = "used"
            self.price = self.price * 0.8
        return self

    def display_info(self): 
        print "Price:", self.price
        print "Item Name:", self.item_name
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Cost:", self.cost
        print "Status:", self.status
        return self
        

prod1 = Product(2, "pencil", 4 , "yellow", .5)
prod2 = Product(4, "notebook", 16, "mead", 2.00)

prod1.display_info().tax().sell().display_info()

