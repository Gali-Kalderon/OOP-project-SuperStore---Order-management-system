from Laptop import Laptop
from SmartPhone import SmartPhone
from Client import Client
from Shirts import Shirts
from Order import Order
from Exceptions import ShirtNotFoundError
from Exceptions import ClientNotFoundError

import csv

class SuperStore:
    def __init__(self, products, shirts, clients, orders):
        self.products = []
        with open (f"{products}.csv") as csv_file:
            read = csv.reader(csv_file)
            next(read)
            for row in read:
              product_id = int(row[0])
              product_type = row[1]
              brand = row[2]
              model = row[3]
              year = int(row[4])
              price = float(row[5])
              if product_type == "laptop":
                  CPU = row[6]
                  hard_disk = int(row[7])
                  screen = int(row[8])
                  l1 = Laptop(product_id,brand,model,year,price,CPU,hard_disk,screen)
                  self += l1 #function iadd
              if product_type == "smartphone":
                  cell_net = row[9]
                  num_cores = int(row[10])
                  cam_res = int(row[11])
                  s1 = SmartPhone(product_id,brand,model,year,price,cell_net,num_cores,cam_res)
                  self += s1 #function iadd
        with open (f"{shirts}.csv") as csv_file:
            read = csv.reader(csv_file)
            next(read)
            for row in read:
                product_id = int(row[0])
                product_name = row[1]
                price = float(row[2])
                units_in_stock = int(row[3])
                shirts1 = Shirts(product_id,price,product_name,units_in_stock)
                self += shirts1
        self.clients = []
        with open (f"{clients}.csv") as csv_file:
            read = csv.reader(csv_file)
            next(read)
            for row in read:
                client_id = int(row[0])
                name = row[1]
                email = row[2]
                address = row[3]
                phone_number = row[4]
                gender = row[5]
                cli = Client(client_id,name,email,address,phone_number,gender)
                self.add_client(cli)
        self.orders = []
        with open (f"{orders}.csv") as csv_file:
            read = csv.reader(csv_file)
            next(read)
            for row in read:
                order_id = int(row[0])
                client_id = int(row[1])
                product_id = int(row[2])
                quantity = int(row[3])
                orders1 = Order(order_id,client_id,product_id,quantity)
                self.orders.append(orders1)
    def print_products(self):
        for p in self.products:
            print(p)

    def print_clients(self):
        for c in self.clients:
            print(c)

    def get_product(self,id):
        for p in self.products:
            if id == p.product_id:
                return p
        return None

    def get_client(self,id):
        for c in self.clients:
            if id == c.client_id:
                return c

    # def add_product(self, new_object):
    #     for p in self.products:
    #         if new_object.product_id == p.product_id:
    #             return False
    #     self.products.append(new_object)
    #     return True

    def add_client(self, new_client):
        for c in self.clients:
            if new_client.client_id == c.client_id:
                return False
        self.clients.append(new_client)
        return True

    def remove_product(self, id_product):
        for p in self.products:
            if id_product == p.product_id:
                self.products.remove(p)
                return True
        return False

    def remove_client(self, id_client):
        for c in self.clients:
            if id_client == c.client_id:
                self.clients.remove(c)
                return True
        return False

    def get_all_by_brand(self, brand1):
        list_brand = []
        for p in self.products:
            if p.brand == brand1:
                list_brand.append(p)
        return list_brand

    def get_all_by_price_under(self,max_price):
        price_filter_list = []
        for p in self.products:
            if p.price < max_price:
                price_filter_list.append(p)
        return price_filter_list

    def get_most_expensive_product(self):
        max1 = 0
        for p in self.products:
            if p.price >= max1:
                max1 = p.price
        for pro in self.products:
            if max1 == pro.price:
                return pro

    def get_all_phones(self):
        sp = []
        for p in self.products:
            if type(p) == SmartPhone:
                sp.append(p)
        return sp
    def get_all_laptop(self):
        lep = []
        for p in self.products:
            if type(p) == Laptop:
                lep.append(p)
        return lep

    def phone_average_price(self):
        sum1 = 0
        count = 0
        for p in self.products:
            if type(p) == SmartPhone:
                sum1 += p.price
                count +=1
        avg_p = sum1/count
        return avg_p

    def get_max_screen(self):
        max1 = 0
        for p in self.products:
            if type(p) == Laptop:
               if p.screen>=max1:
                  max1 = p.screen
        return max1

    def get_common_cam(self):
        phone_list = []
        for p in self.products:
            if type(p) == SmartPhone:
                phone_list.append(p.cam_res)
        return max(set(phone_list), key = phone_list.count)

    def list_popular(self):
        popular_list = []
        for p in self.products:
            if p.Is_popular() == True:
                popular_list.append(p)
        return popular_list

    def __iadd__(self, new_object):
        for p in self.products:
            if new_object.product_id == p.product_id:
                raise IdAlreadyExist()
        self.products.append(new_object)
        return self
######
    def get_shirt(self, id):
        for p in self.products:
            if id == p.product_id:
                return p
        return None

    def get_max_order_id(self):
        id_max = 0
        for o in self.orders:
            if id_max <= o.order_id:
                id_max = o.order_id
        return id_max

    def add_order(self,client_id1,prduct_id1,quantity1):
        order_id1 = self.get_max_order_id()+1
        if self.get_client(client_id1)== None:
            raise ClientNotFoundError(client_id1)
        if self.get_product(prduct_id1)== None or self.get_shirt(prduct_id1)== None:
            raise ShirtNotFoundError(prduct_id1)
        if type(self.get_product(prduct_id1)) != Shirts:
            if quantity1 >1:
                raise ValueError(quantity1)
        if type(self.get_product(prduct_id1)) == Shirts:
            if self.get_shirt(prduct_id1).units_in_stock < quantity1:
                raise ValueError(quantity1)

        new_order = Order(order_id1,client_id1,prduct_id1,quantity1)
        new = self.orders.append(new_order)
        print("order added!")
        return new

    def print_orders(self):
        for o in self.orders:
            print(o)

    def print_all_shirts(self):
        shi = []
        for p in self.products:
            if type(p) is Shirts:
                shi.append(p)
        return shi

