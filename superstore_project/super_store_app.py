from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from SuperStore import SuperStore
from Laptop import Laptop
from SmartPhone import SmartPhone
from Shirts import Shirts
from Exceptions import *
store = SuperStore('products_supply',"shirts","clients","orders")

window = Tk()
window.geometry("1200x600")
window.title("Super Store")

current_row = 0

title = Label(window, text="Super Store", font=("Ariel bold", 18),fg="DeepPink3")
title.grid(column=0 ,row=0)

current_row +=1

print_options_lbl = Label(window, text="Products",font=("Ariel bold", 14), fg="HotPink2")
print_options_lbl.grid(column=0 ,row=current_row)

print_options = ttk.Combobox(window, values=("All products","Laptops","SmartPhones","Shirts"))
print_options.grid(column=1, row=current_row)
print_options.focus()

def dp_click():
    list_box.delete(0, END)
    print_ = print_options.get()
    if print_ == "All products":
        for p in store.products:
            list_box.insert(END,str(p))
    if print_ == "Laptops":
        for L in store.products:
            if type(L) == Laptop:
                list_box.insert(END, str(L))
    if print_ == "SmartPhones":
        for s in store.products:
            if type(s) == SmartPhone:
                list_box.insert(END, str(s))
    if print_ == "Shirts":
        for s in store.products:
            if type(s) is Shirts:
                list_box.insert(END, str(s))

display_products_button= Button(window, text="Display products", width=15, height=2,bg='Pink1',
                                borderwidth=5,command=dp_click)
display_products_button.grid(column=2, row=current_row)
list_box = Listbox(window, width=63, height=7)
list_box.grid(column=3, row=current_row)

print_options_lbl = Label(window, text="Create New Product",font=("Ariel bold", 14), fg="HotPink2")
print_options_lbl.grid(column=0 ,row=4)

int_var = IntVar()

title_id = Label(window, text="id", font=("Ariel bold", 10))
title_id.grid(column=0 ,row=5)
entry_id = Entry(window, width=20)
entry_id.grid(column=0, row=6)

title_price = Label(window, text="price", font=("Ariel bold", 10))
title_price.grid(column=1 ,row=5)
entry_price = Entry(window, width=20)
entry_price.grid(column=1, row=6)

title_brand = Label(window, text="brand", font=("Ariel bold", 10))
title_brand.grid(column=2 ,row=5)
entry_brand = Entry(window, width=20)
entry_brand.grid(column=2, row=6)

title_model = Label(window, text="model", font=("Ariel bold", 10))
title_model.grid(column=3 ,row=5)
entry_model = Entry(window, width=20)
entry_model.grid(column=3 ,row=6)

title_year = Label(window, text="year", font=("Ariel bold", 10))
title_year.grid(column=4 ,row=5)
year_combo= ttk.Combobox(window, values=list(range(1970,2023)))
year_combo.grid(column=4, row=6)

# laptop or smartphone

def laptop_or_smartphone():
    entry_CPU.delete(0, END)
    entry_Hard_disc.delete(0, END)
    entry_Screen.delete(0, END)
    entry_cellular_network.delete(0, END)
    entry_Number_of_cores.delete(0, END)
    entry_Camera_resolution.delete(0, END)

    if l_r.get() == 1:
        title_CPU.configure(state=NORMAL)
        title_Hard_disc.configure(state=NORMAL)
        title_Screen.configure(state=NORMAL)
        entry_CPU.configure(state=NORMAL)
        entry_Hard_disc.configure(state=NORMAL)
        entry_Screen.configure(state=NORMAL)

        title_cellular_network.configure(state=DISABLED)
        title_Number_of_cores.configure(state=DISABLED)
        title_Camera_resolution.configure(state=DISABLED)
        entry_cellular_network.configure(state=DISABLED)
        entry_Number_of_cores.configure(state=DISABLED)
        entry_Camera_resolution.configure(state=DISABLED)
    else:
        title_CPU.configure(state=DISABLED)
        title_Hard_disc.configure(state=DISABLED)
        title_Screen.configure(state=DISABLED)
        entry_CPU.configure(state=DISABLED)
        entry_Hard_disc.configure(state=DISABLED)
        entry_Screen.configure(state=DISABLED)

        title_cellular_network.configure(state=NORMAL)
        title_Number_of_cores.configure(state=NORMAL)
        title_Camera_resolution.configure(state=NORMAL)
        entry_cellular_network.configure(state=NORMAL)
        entry_Number_of_cores.configure(state=NORMAL)
        entry_Camera_resolution.configure(state=NORMAL)

l_r = IntVar()

r = Radiobutton( text="Laptop", value=1, variable=l_r, command=laptop_or_smartphone)
r.grid(sticky=W, column=0, row=9)


r2 = Radiobutton( text="SmartPhone", value=2, variable=l_r, command=laptop_or_smartphone)
r2.grid(sticky=W, column=0, row=12)

title_CPU = Label(window, text="CPU", font=("Ariel bold", 8))
title_CPU.grid(column=1 ,row=8)
entry_CPU = Entry(window, width=20)
entry_CPU.grid(column=1, row=9)

title_Hard_disc = Label(window, text="Hard disc", font=("Ariel bold", 10))
title_Hard_disc.grid(column=2 ,row=8)
entry_Hard_disc= Entry(window, width=20)
entry_Hard_disc.grid(column=2, row=9)

title_Screen = Label(window, text="Screen", font=("Ariel bold",10))
title_Screen.grid(column=3,row=8)
entry_Screen= Entry(window, width=20)
entry_Screen.grid(column=3, row=9)

title = Label(window, text="", font=("Ariel bold", 20),fg="Pink") # only for space
title.grid(column=1 ,row=10)

title_cellular_network = Label(window, text="Cellular network", font=("Ariel bold", 10))
title_cellular_network.grid(column=1,row=11)
entry_cellular_network= Entry(window, width=20)
entry_cellular_network.grid(column=1, row=12)

title_Number_of_cores = Label(window, text="Number of cores", font=("Ariel bold", 10))
title_Number_of_cores.grid(column=2,row=11)
entry_Number_of_cores= Entry(window, width=20)
entry_Number_of_cores.grid(column=2, row=12)

title_Camera_resolution = Label(window, text="Camera resolution", font=("Ariel bold", 10))
title_Camera_resolution.grid(column=3,row=11)
entry_Camera_resolution= Entry(window, width=20)
entry_Camera_resolution.grid(column=3, row=12)

title_error = Label(window, text="                                    ")
title_error.grid(column=1, row=4)

def is_empty1():
    empty = True
    if l_r.get() ==1:
        if len(entry_id.get()) == 0:
            empty = False
            entry_id.config(bg= "Red")
            title_error.configure(text=str("insert id"))
        elif len(entry_price.get()) == 0:
            empty = False
            entry_price.config(bg= "Red")
            title_error.configure(text=str("insert price"))
        elif len(entry_brand.get()) == 0:
            empty = False
            entry_brand.config(bg= "Red")
            title_error.configure(text=str("insert brand"))
        elif len(entry_model.get()) == 0:
            empty = False
            entry_model.config(bg= "Red")
            title_error.configure(text=str("insert model"))
        elif len(entry_CPU.get()) == 0:
            empty = False
            entry_CPU.configure(bg= "Red")
            title_error.configure(text=str("insert CPU"))
        elif len(entry_Hard_disc.get()) == 0:
            empty = False
            entry_Hard_disc.configure(bg= "Red")
            title_error.configure(text=str("insert hard disc"))
        elif len(entry_Screen.get()) == 0:
            empty = False
            entry_Screen.configure(bg= "Red")
            title_error.configure(text=str("insert screen"))
        return empty

def is_empty2():
    empty = True
    if l_r.get() ==2:
        if len(entry_id.get()) == 0:
            empty = False
            entry_id.config(bg= "Red")
            title_error.configure(text=str("insert id"))
        elif len(entry_price.get()) == 0:
            empty = False
            entry_price.config(bg= "Red")
            title_error.configure(text=str("insert price"))
        elif len(entry_brand.get()) == 0:
            empty = False
            entry_brand.config(bg= "Red")
            title_error.configure(text=str("insert brand"))
        elif len(entry_model.get()) == 0:
            empty = False
            entry_model.config(bg= "Red")
            title_error.configure(text=str("insert model"))
        elif len(entry_cellular_network.get()) == 0:
            empty = False
            entry_cellular_network.configure(bg= "Red")
            title_error.configure(text=str("insert cellular network"))
        elif len(entry_Number_of_cores.get()) == 0:
            empty = False
            entry_Number_of_cores.configure(bg= "Red")
            title_error.configure(text=str("insert Number of cores"))
        elif len(entry_Camera_resolution.get()) == 0:
            empty = False
            entry_Camera_resolution.configure(bg= "Red")
            title_error.configure(text=str("insert Camera resolution"))
        return empty

def create_new_product():
    id = entry_id.get()
    price = entry_price.get()
    brand = entry_brand.get()
    model = entry_model.get()
    year = year_combo.get()

    if l_r.get()==1:
       CPU = entry_CPU.get()
       Hard_disc = entry_Hard_disc.get()
       Screen = entry_Screen.get()

       entry_id.config(bg="WHITE")
       entry_price.config(bg="WHITE")
       entry_model.config(bg="WHITE")
       entry_brand.config(bg="WHITE")
       entry_CPU.config(bg="WHITE")
       entry_Hard_disc.config(bg="WHITE")
       entry_Screen.config(bg="WHITE")
       entry_Number_of_cores.config(bg="WHITE")
       entry_cellular_network.config(bg="WHITE")
       entry_Camera_resolution.config(bg="WHITE")

       if is_empty1() == False:
          is_empty1()

       if is_empty1() == True:
           try:
               l = Laptop(id, brand, model, year, price, CPU, Hard_disc, Screen)
               good_or_not = True

           except IdValueError as e:
               good_or_not = False
               title_error.configure(text= str("id need to be an integer!"), fg= "Red")
           except PriceValueError:
               good_or_not = False
               title_error.config(text= str("price need to be an integer!"), fg= "Red")
           except YearValueError:
               good_or_not = False
               title_error.configure(text=str("please choose year from the options"), fg="Red")
           except HardDiscValueError:
               good_or_not = False
               title_error.configure(text=str("hard disc need to be an integer!"), fg="Red")
               title_error.grid(column=1, row=4)
           except ScreenValueError:
               good_or_not = False
               title_error.configure(text= str("screen need to be an integer!"), fg= "Red")

           if good_or_not == True :
               store.products.append(l)
               title_error.configure(text=str("                                                                  "))
               messagebox.showinfo(message=f"Laptop {id} added!")
               entry_id.delete(0, END)
               entry_price.delete(0, END)
               entry_brand.delete(0, END)
               entry_model.delete(0, END)
               year_combo.delete(0, END)

               entry_CPU.delete(0, END)
               entry_Hard_disc.delete(0, END)
               entry_Screen.delete(0, END)


    if l_r.get()==2:
        cellular_network = entry_cellular_network.get()
        Number_of_cores = entry_Number_of_cores.get()
        Camera_resolution = entry_Camera_resolution.get()

        entry_id.config(bg="WHITE")
        entry_price.config(bg="WHITE")
        entry_model.config(bg="WHITE")
        entry_brand.config(bg="WHITE")
        entry_CPU.config(bg="WHITE")
        entry_Hard_disc.config(bg="WHITE")
        entry_Screen.config(bg="WHITE")
        entry_Number_of_cores.config(bg="WHITE")
        entry_cellular_network.config(bg="WHITE")
        entry_Camera_resolution.config(bg="WHITE")

        if is_empty2() == False:
            is_empty2()

        else:
            try:
                s = SmartPhone(id, brand, model, year, price, cellular_network,
                               Number_of_cores, Camera_resolution)
                good_or_not = True


            except IdValueError as e:
                good_or_not = False
                title_error.configure(text= str("id need to be an integer!"), fg= "Red")
            except PriceValueError:
                good_or_not = False
                title_error.configure(text= str("price need to be an integer!"), fg= "Red")
            except YearValueError:
                good_or_not = False
                title_error.configure(text=str("please choose year from the options"), fg="Red")
            except NumCoresValueError as e:
                good_or_not = False
                title_error.configure(text=str("number of cores need to be an integer!"), fg="Red")
            except CamResValueError as e:
                good_or_not = False
                title_error.configure(text=str("camera resolution need to be an integer!"), fg="Red")

            if good_or_not == True:
                store.products.append(s)
                messagebox.showinfo(message=f"SmartPhone {id} added!")
                title_error.configure(text=str("                                                              "
                                               "       "))
                entry_id.delete(0, END)
                entry_price.delete(0, END)
                entry_brand.delete(0, END)
                entry_model.delete(0, END)
                year_combo.delete(0, END)

                entry_cellular_network.delete(0, END)
                entry_Number_of_cores.delete(0, END)
                entry_Camera_resolution.delete(0, END)


create_button= Button(window, text="Create",font= ("Ariel bold", 10),width=12, height=2,bg='Pink1',
                      borderwidth=5,command=create_new_product)
create_button.grid(column=4, row=13)

# 3
task3_title = Label(window, text="Get Product", font=("Ariel bold", 15),fg="HotPink2")
task3_title.grid(column=0 ,row=15)

task3_title = Label(window, text="Enter product id", font=("Ariel bold", 10))
task3_title.grid(column=1 ,row=16)
entry_id3 = Entry(window, width=20)
entry_id3.grid(column=1, row=17)

def get_product():
    id = int(entry_id3.get())
    if store.get_product(id) !=None:
        messagebox.showinfo(message=f"product details: {store.get_product(id)}")
    else:
        messagebox.showinfo(message=f"this product doesn't exist!")

create_button= Button(window, text="get product details",font= ("Ariel bold", 10),width=15, height=2,bg="Pink1",
                      borderwidth=5,command=get_product)
create_button.grid(column=2, row=17)

window.mainloop()

