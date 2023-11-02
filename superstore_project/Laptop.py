from Exceptions import *
from Product import Product
class Laptop(Product):
    def __init__(self,product_id,brand,model,year,price, CPU, hard_disk, screen):
        super().__init__(product_id,brand,model,year,price)
        self.CPU = CPU
        try:
            hard_diskInt = int(hard_disk)
        except ValueError as e:
            raise HardDiscValueError()
        try:
            screenInt = int(screen)
        except ValueError as e:
            raise ScreenValueError()

        self.hard_disk = hard_disk
        self.screen = screen
    def print_me(self):
        product_parent = super().print_me()
        print("CPU:", self.CPU)
        print("hard_disk:", self.hard_disk)
        print("screen:", self.screen)
    def __str__(self):
        product_parent = super().__str__()
        return f"{product_parent},{self.CPU},{self.hard_disk},{self.screen}"
    def __repr__(self):
        return str(self)
