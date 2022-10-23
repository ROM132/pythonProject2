class grocery_shop:
    grocery_items = {
        "bread": ["bread", 40, 21, False],
        "meat": ["meat", 40, 34, False],
        "pasta": ["pasta", 40, 9, False],
    }

    def __init__(self, attempt=3):
        self.attempt = attempt

    def Login(self):
        qus = input("Login Admin/Login User  [Type A to Login in Admin/ Type U to login in the User]: ").lower()
        if qus == "a":
            while True:
                if self.attempt == 0:
                    print("You out of attempt!, You blocked!")
                    g.Login()
                else:
                    pass
                qus = input("Enter the password: ")
                if qus != "1234":
                    self.attempt -= 1
                    print(f"Incorrect password! {self.attempt} more attempt!")
                    continue
                else:
                    print("Login successfully!")
                    g.Admin()
        elif qus == "u":
            g.User()
        else:
            print("Invalid input try again!")
            g.Login()

    def direction(self):
        pass

    def Admin(self, add_product=None):
        while True:
            g.admin_text()
            qus = input("Enter what you want to do: ")
            if qus == "1":
                for key in self.grocery_items:
                    print(self.grocery_items[key])

            elif qus == "2":
                name = input("Enter product name: ")
                quantity = input("Enter product quantity: ")
                price = input("Enter product price: ")
                if price.isdigit() and quantity.isdigit():
                    price = int(price)
                    quantity = int(quantity)
                else:
                    print("Pls enter a number next time!")
                    g.Admin()

                for item in self.grocery_items:
                    if self.grocery_items[item][0] == name and item == name:
                        print("You already have this item in your shop try a different one!")
                        g.Admin()
                    else:
                        print("Product successfully add!")
                        add_product = f"{name}: [{name}, {price}]"
                        self.grocery_items[name] = [name, qus, price]
                        break

            elif qus == "3":
                remove_product = input("Enter the product nmae you want to delete: ")
                for key, value in list(self.grocery_items.items()):
                    if key == remove_product:
                        print(f"product {remove_product} removed succeeded")
                        del self.grocery_items[key]
                        g.Admin()
                print("The id do not found!")

            elif qus == "4":
                my_ava = 0
                for key in self.grocery_items:
                    my_ava += int(self.grocery_items[key][1])

            elif qus == "5":
                my_availibale = 0
                for key in self.grocery_items:
                    my_availibale += int(self.grocery_items[key][1] * int(self.grocery_items[key][2]))

            elif qus == "6":
                print("Logout successfully!")
                g.Login()

            else:
                print("Invalid input!")
                continue

    def User(self):
        while True:
            g.user_text()
            qus = input("What you want to do: ")

            if qus == "1":
                for key in self.grocery_items:
                    print(self.grocery_items[key])

            elif qus == "2":
                while True:
                    qus = input("Enter the product name you want to buy: ")
                    key = qus
                    val = self.grocery_items.get(key)
                    if val is None:
                        print(f"You choose not available item")
                        break
                    else:

                        if qus == self.grocery_items[key][0]:
                            print("You successfully placed the order!")
                            self.grocery_items[key][2] -= 1
                            self.grocery_items[key][3] = True
                            g.User()
                        else:
                            print("Invalid input try again!")
                            g.User()

            elif qus == "3":
                qus = input("Enter the product that you want to cancel is order: ")
                key = qus
                val = self.grocery_items.get(key)
                if val is None:
                    print(f"You choose not available item")
                    break
                else:
                    if qus == self.grocery_items[key][0]:
                        if self.grocery_items[key][3] == True:
                            print("You cancel the order!")
                            self.grocery_items[key][2] -= 1
                            self.grocery_items[key][3] = False
                            g.User()

                        else:
                            print("You dont order it!")
                            g.User()

            elif qus == "4":
                print("You Logout!")
                g.Login()

            else:
                print("Invalid input try again!")
                continue

    def admin_text(self):
        print("====================")
        print("1. Display Menu")
        print("2. Add Product to the menu")
        print("3. Remove Product")
        print("4. All Product available")
        print("5. Total Income")
        print("6. Logout")
        print("====================")

    def user_text(self):
        print("===================")
        print("1. Display Menu")
        print("2. Place order")
        print("3. Cancel order")
        print("4. Logout")
        print("===================")


g = grocery_shop()
g.Login()