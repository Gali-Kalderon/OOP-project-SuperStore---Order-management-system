from Client import Client
from Laptop import Laptop
from SmartPhone import SmartPhone
from SuperStore import SuperStore
from Exceptions import ClientNotFoundError
from Exceptions import ShirtNotFoundError

def add_new_product_to_the_store(store):
    product_type = (input("Enter l for laptop or Enter s for smartphone"))
    if product_type == "l":
        id3 = input("Insert product id: ")
        brand = input("Insert product brand: ")
        model = input("Insert product model: ")
        year = input("Insert product year: ")
        price = input("Insert product price: ")
        CPU = input("Insert product CPU: ")
        hard_disk = input("Insert product hard disk: ")
        screen = input("Insert product screen: ")
        new_product = Laptop(id3, brand, model, year, price, CPU, hard_disk, screen)
        store += new_product

    if product_type == "s":
        id3 = input("Insert product id: ")
        brand = input("Insert product brand: ")
        model = input("Insert product model: ")
        year = input("Insert product year: ")
        price = input("Insert product price: ")
        cell_net = input("Insert product cell_net: ")
        num_cores = input("Insert product num_cores: ")
        cam_res = input("Insert product cam_res")
        new_product = SmartPhone(id3, brand, model, year, price, cell_net, num_cores, cam_res)
        store += new_product

def add_new_client_to_the_store(store):
    id4 = int(input("Insert client id: "))
    name = input("Insert client name: ")
    email = input("Insert client email: ")
    address = input("Insert client address: ")
    phone_number = int(input("Insert client phone number: "))
    gender = input("Insert gender (M/F): ")
    new_client = Client(id4, name, email, address, phone_number, gender)
    if store.add_client(new_client) == True:
        store.add_client(new_client)
    else:
        print("This client already exists")


def remove_product_from_the_store(store):
    id5 = int(input("Insert product id: "))
    if store.remove_product(id5) == True:
        store.remove_product(id5)
        print(id5, " deleted!")
    else:
        print(id5, " not exist!")

def remove_client_from_the_store1(store):
    id6 = int(input("Insert client id: "))
    if store.remove_client(id6) == True:
        store.remove_client(id6)
        print(id6, " deleted!")
    else:
        print(id6, " not exist!")

def add_new_client_to_the_store1(store):
    id4 = input("Insert client id: ")
    name = input("Insert client name: ")
    email = input("Insert client email: ")
    address = input("Insert client address: ")
    phone_number = input("Insert client phone number: ")
    gender = input("Insert gender (M/F): ")
    new_client = Client(id4, name, email, address, phone_number, gender)
    if store.add_client(new_client) == True:
        store.add_client(new_client)
    else:
        print("This client already exists")

def all_products_under_price1(store):
    maximum = float(input("Insert a maximum price: "))
    print("all products under price: ")
    for p in store.get_all_by_price_under(maximum):
        print(p)

def create_new_order(store):
    c_id = int(input("Enter client id: "))
    p_id = int(input("Enter product id: "))
    q = int(input("Enter quantity of the product: "))
    try:
        store.add_order(c_id, p_id, q)
    except ClientNotFoundError as e:
        print("client id", c_id, "does not exist!")
    except ShirtNotFoundError as e:
        print("Shirt id", p_id, "does not exist!")
    except ValueError as e:
        print("This amount isn't avilable")

def menu():
    choice = int(input("\n"
                       "--- MENU --- \n"
                       "1. Print all products \n"
                       "2. Print all clients \n"
                       "3. Add new product to the store \n"
                       "4. Add new client to the store \n"
                       "5. Remove product \n"
                       "6. Remove client \n"
                       "7. Print all products under price \n"
                       "8. Print the most expensive product \n"
                       "9. Print smartphone list \n"
                       "10. Print laptop list \n"
                       "11. Print average phone price \n"
                       "12. Print largest laptop screen \n"
                       "13. Print common camera resolution \n"
                       "14. Print popular products \n"
                       "15. Print all Shirts \n"
                       "16. Create new order \n"
                       "17. Print all orders \n"
                       "18. Exit \n"
                       "What is your choice?"))
    return choice


def main_SuperStore():
    store = SuperStore('products_supply',"shirts","clients","orders")
    choice = menu()
    while choice != 18:

        if choice == 1:
            store.print_products()

        if choice == 2:
            store.print_clients()

        if choice == 3:
            add_new_product_to_the_store(store)

        if choice == 4:
            add_new_client_to_the_store1(store)

        if choice == 5:
            remove_product_from_the_store(store)

        if choice == 6:
            remove_client_from_the_store1(store)

        if choice == 7:
            all_products_under_price1(store)

        if choice == 8:
            max_p = store.get_most_expensive_product()
            print("The most expensive product is: ", max_p)

        if choice == 9:
            for p in store.get_all_phones():
                print(p)

        if choice == 10:
            for p in store.get_all_laptop():
                print(p)

        if choice == 11:
            print("The phone price average is: ", store.phone_average_price())

        if choice == 12:
            print("The largest screen size is: ", store.get_max_screen())

        if choice == 13:
            print("The most common camera resolution is: ", store.get_common_cam())

        if choice == 14:
            print("The popular products are: ")
            for p in store.list_popular():
                print(p)

        if choice == 15:
            for s in store.print_all_shirts():
                print(s)

        if choice == 16:
            create_new_order(store)

        if choice == 17:
            store.print_orders()

        if choice > 17 or choice < 1:
            print("Eror! \nPlease choose one of the menu options:")

        choice = menu()
    print("Bye Bye")
    return store

main_SuperStore()
