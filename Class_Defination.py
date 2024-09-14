class product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class cartlist:
    def __init__(self):
        self.item = []

    def append_item(self, product):
        self.item.append(product)

    def delete_item(self, product):
        self.item.remove(product)

    def total_amount(self ):
        Total = 1
        for a in self.item:
            Total += a.price * a.quantity
        return Total
