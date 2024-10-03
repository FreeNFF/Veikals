class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        sum = self.price* self.quantity
        print("Pirkuma",self.name," summa ir ",sum," eiro.")



ob1 = Product(name=input("Ievadiet 1. produktu: "), price=float(input("Ievadiet cenu 1. produktam: ")), quantity=int(input("Ievadiet 1. produkta daudzumu: ")))
print()
print("--------------------------------")
print()
ob2 = Product(name=input("Ievadiet 2. produktu: "), price=float(input("Ievadiet cenu 2. produktam: ")), quantity=int(input("Ievadiet 2. produkta daudzumu: ")))

print()
print("--------------------------------")
print()


ob1.get_total_price()
ob2.get_total_price()

print()
print("--------------------------------")
print()

class ShopingCart(Product):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def add_product_to_cart(self):
        print("Produkts ", self.name," ir pievienots grozam!")

    def remove_product_to_cart(self):
        print("Produkts ", self.name, " ir izņemts no groza!")

    def get_total_price(self):
        sum=self.price*self.quantity
        print("Kopējās izmaksas ir ", sum," eiro.")


Produkts1 = ShopingCart(ob1.name, ob1.price, ob1.quantity)
Produkts1.add_product_to_cart()
Produkts1.get_total_price()


print()
print("--------------------------------")
print()

Produkts2 = ShopingCart(ob2.name, ob2.price, ob2.quantity)
Produkts2.add_product_to_cart()

kopa = ob1.price*ob1.quantity + ob2.price*ob2.quantity

print("Kopējā summa ir ",kopa, " eiro.")

Produkts1.remove_product_to_cart()
Produkts2.get_total_price()
Produkts2.remove_product_to_cart()

print()
print("--------------------------------")
print()

print('Lietātāja informācija nomainīta, kāda ir jūsu jaunā informācija? Ievadiet:')
print()
print("--------------------------------")
print()

class SystemUser:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def set_user_info(self, newusername, newpassword, newemail):
        print()
        print("----------------------------------------------")
        print()
        print("Vecais info: ")
        print("Username: ",self.username)
        print("Password: ", self.password)
        print("Email: ", self.email)
        self.username = newusername
        self.password = newpassword
        self.email = newemail
        

    def get_user_info(self):
        print()
        print("----------------------------------------------")
        print()
        print("Jaunais info: ")
        print("Username: ",self.username)
        print("Password: ", self.password)
        print("Email: ", self.email)

User = SystemUser("Janka", "Suns2024", "kristaps,tas@hmail.lv")
User.set_user_info(newusername=input("Ievadiet jauno username: "), newpassword=input("Ievadiet jauno paroli: "), newemail=input("Ievadiet jauno email: "))
User.get_user_info()