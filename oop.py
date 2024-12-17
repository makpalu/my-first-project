# multiple inheritance

class games:
    def __init__(self, name, price, for_sale):
        self.name = name
        self.price = price
        self.for_sale = for_sale

    def sold(self):
        print(f"{self.name} has been sold for GHC{self.price}")

    def shelf(self):
        print(f"{self.name} is still on the shelf")

    def on_sale(self):
        print(f"The on sale status is: {self.for_sale}")


class customer:
    def __init__(self, name, id, full_payment):
        self.name = name
        self.id = id
        self.full_payment = full_payment

    def status(self):
        print(f"Has {self.name} paid in full: {self.full_payment}")
        print(f"Customer's ID number: {self.id}")


class person(customer, games):
    def __init__(self, id, full_payment, price, for_sale, name):
        customer.__init__(self, name, id, full_payment)
        games.__init__(self, name, price, for_sale)

        self.name_from_customer = name
        self.name_from_games = name

person1 = person("")