import numpy as np
import matplotlib.pyplot as plt
from SuperStore import SuperStore
from Exceptions import ClientNotFoundError

#task 1
file_data = np.genfromtxt("orders.csv", delimiter=",", skip_header=1)
store = SuperStore('products_supply',"shirts","clients","orders")

orders = np.array(file_data, dtype=np.int32)

print(orders)
print()

#task 2
new_list = []
for o in range(len(orders)):
    total_price=store.get_shirt(orders[o,2]).price * orders[o,3]
    new_list.append(total_price)
new_list2 = np.array(new_list, dtype=np.int32)

new_orders = np.insert(orders,4,new_list2,axis=1)
print(new_orders)
print()

#task 3
max_price = (np.max(new_orders[:,4]))
for o in range(len(new_orders)):
    if new_orders[o,4] == max_price:
        order_id = new_orders[o,0]
        client_name = store.get_client(new_orders[o,1]).name
        product_name = store.get_shirt(new_orders[o,2]).product_name
        print("The most expensive order is: ")
        print("order id: ",order_id,", client name: ",client_name,", product name: ",product_name,", price: ",max_price)
print()

#task 4
def task4(client_id):
    count = 0
    total_price = 0
    for o in range(len(new_orders)):
        if new_orders[o,1] == client_id:
           count +=1
           total_price += new_orders[o,4]
    print("orders amount: ",count)
    print("total price: ",total_price)


client_id4 = int(input("Enter client id: "))
if store.get_client(client_id4) == None:
    raise ClientNotFoundError(client_id4)
else:
    client_name4 = store.get_client(client_id4).name
    print("client name: ",client_name4)
    task4(client_id4)
print()

#task 5
new_orders2 = new_orders[new_list2>new_list2.mean()]

print("orders that their amount are bigger then the average: \n",new_orders2)
print()

#task 6
unique, counts =np.unique(new_orders[:,1], return_counts=True)
dict ={e: counts[i] for i, e in enumerate(unique)}
print("dictionary: \n ",dict)
print()

#task 7
dict1 = {str(k):(v) for k,v in dict.items()}
labels = list(dict1.values())
values = list(dict1.keys())
plt.bar(values ,labels, color="pink")
plt.xlabel("client id")
plt.ylabel("amount orders")
plt.title("task 7")
plt.show()

