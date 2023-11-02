from Product import Product
from Exceptions import *
class SmartPhone(Product):
    def __init__(self, product_id,brand,model,year,price, cell_net, num_cores, cam_res):
        super().__init__(product_id,brand,model,year,price)
        self.cell_net = cell_net
        try:
            num_coresInt = int(num_cores)
        except ValueError as e:
            raise NumCoresValueError()
        try:
            cam_resInt = int(cam_res)
        except ValueError as e:
            raise CamResValueError()

        self.num_cores = num_cores
        self.cam_res = cam_res

    def print_me(self):
        product_parent = super().print_me()
        print("cell_net:", self.cell_net)
        print("num_cores:", self.num_cores)
        print("cam_res:", self.cam_res)
    def __str__(self):
        product_parent = super().__str__()
        return f"{product_parent},{self.cell_net},{self.num_cores},{self.cam_res}"
    def __repr__(self):
        return str(self)

