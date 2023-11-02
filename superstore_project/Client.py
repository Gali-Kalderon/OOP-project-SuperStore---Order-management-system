class Client:
    def __init__(self,client_id,name,email,address,phone_number,gender):
        if type(client_id) == int and len(str(client_id)) == 5:
            self.client_id = client_id
        else: # if client id isn't intact we will see zero.
            self.client_id = 0
        self.name = name
        if "@fakeemail.com" in email:
            self.email = email
        else:
            self.email = "notvalid@fakeemail.com"
        self.address = address
        if len(str(phone_number))==10:
            self.phone_number = phone_number
        else: # if phone number isn't intact we will see zero.
            self.phone_number = 0
        if "M" == gender or "F" == gender:
            self.gender = gender
        else:
            self.gender = "F"

    def print_me(self):
        print("----", self.client_id, "----")
        print("product_tipe:", self.name)
        print("brand:", self.email)
        print("model:", self.address)
        print("year:", self.phone_number)
        print("price:", self.gender)

    def __str__(self):
        return f"{self.client_id},{self.name},{self.email},{self.address},{self.phone_number},{self.gender}"

    def __repr__(self):
        return str(self)
