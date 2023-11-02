from Product import Product

class Shirts(Product):
    def __init__(self,product_id,price,product_name,units_in_stock):
        super().__init__(product_id,"SuperStore","",2023,price)
        self.product_name = product_name
        if type(units_in_stock) == int and units_in_stock>0:
            self.units_in_stock = units_in_stock
        else:
            self.units_in_stock = 0
    def __str__(self):
        product_parent = super().__str__()
        return f"{product_parent},{self.product_name},{self.units_in_stock}"
    def __repr__(self):
        return str(self)
