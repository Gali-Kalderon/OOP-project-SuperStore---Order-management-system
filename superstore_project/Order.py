class Order:
    def __init__(self,order_id,client_id,product_id,quantity):
        self.order_id = order_id
        if type(client_id) == int:
            self.client_id = client_id
        else:
            self.client_id = 0
        if type(product_id) == int:
            self.product_id = product_id
        else:
            self.product_id = 0
        if type(quantity) == int and quantity>0:
            self.quantity = quantity
        else:
            self.quantity = 0
    def __str__(self):
        return f"{self.order_id},{self.client_id},{self.product_id},{self.quantity}"
    def __repr__(self):
        return str(self)
