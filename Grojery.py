import time


class grocery_shop:
    grocery_items = {
        "bread": ["bread", 21, 40, False],
        "meat": ["meat", 21, 40, False],
        "pasta": ["pasta", 21, 40, False],
    }

    def __init__(self, attempt=3, money=0, amount=0):
        self.amount = amount
        self.money = money
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
                remove_product = input("Enter the product name you want to delete: ")
                for key, value in list(self.grocery_items.items()):
                    if key == remove_product:
                        print(f"product {remove_product} removed succeeded")
                        del self.grocery_items[key]
                        g.Admin()
                print("The item do not found!")

            elif qus == "4":
                my_ava = 0
                for key in self.grocery_items:
                    my_ava += int(self.grocery_items[key][2])
                print(my_ava)

            elif qus == "5":
                my_availibale = 0
                for key in self.grocery_items:
                    my_availibale += int(self.grocery_items[key][1] * int(self.grocery_items[key][2]))
                print(my_availibale)

            elif qus == "6":
                print("Logout successfully!")
                g.Login()
            elif qus == "99":
                g.money_()
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
                        if self.grocery_items[key][3]:
                            print("You can't buy it twice!")
                            g.User()
                        else:
                            if qus == self.grocery_items[key][0] and self.money >= self.grocery_items[key][1]:
                                print("You successfully placed the order!")
                                self.grocery_items[key][2] -= 1
                                self.grocery_items[key][3] = True
                                g.User()
                            elif qus == self.grocery_items[key][0] and self.money < self.grocery_items[key][1]:
                                print("You dont have enough money!")
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
                        if self.grocery_items[key][3]:
                            self.money = self.money + self.grocery_items[key][1]
                            print("You cancel the order!")
                            self.grocery_items[key][2] += 1
                            self.grocery_items[key][3] = False
                            g.User()

                        else:
                            print("You dont order it!")
                            g.User()
            elif qus == "4":
                print(f"You money amount now is: {self.money}")
                time.sleep(2)
            elif qus == "5":
                my_string = " "
                for key in self.grocery_items:
                    if self.grocery_items[key][3]:
                        my_string += f" {self.grocery_items[key][0]},"

                if my_string == " ":
                    print("You dont have any item yet!")
                else:
                    print(f"Ok what you have now is{my_string}")
                input("press enter to go back: ")
                g.User()

            elif qus == "6":
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
        print("99. You money amount")
        print("====================")

    def user_text(self):
        print("===================")
        print("1. Display Menu")
        print("2. Place order")
        print("3. Cancel order")
        print("4. See You money amount")
        print("5. See what you order")
        print("6. Logout")
        print("===================")

    def money_(self):
        while True:
            print(f"You correctly money is: {self.money}")
            self.money = input("Enter how much money you want: ")
            if self.money.isdigit():
                self.money = int(self.money)
                break
            else:
                print("Pls enter a number next time!")
                self.money = 0
                continue


g = grocery_shop()
g.Login()
