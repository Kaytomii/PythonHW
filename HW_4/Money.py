class Money:
    def __init__(self, whole=0, cents=0):
        self.set_value(whole, cents)

    def set_value(self, whole, cents):
        if cents >= 100:
            whole += cents // 100
            cents = cents % 100

        self.whole = whole
        self.cents = cents

    def __str__(self):
        return f"{self.whole}.{self.cents:02d}"

    def get_value(self):
        return self.whole, self.cents

class Product:
    def __init__(self, name, price: Money):
        self.name = name
        self.price = price

    def reduce_price(self, amount: Money):
        total_cents_price = self.price.whole * 100 + self.price.cents
        total_cents_amount = amount.whole * 100 + amount.cents

        new_total = max(0, total_cents_price - total_cents_amount)

        new_whole = new_total // 100
        new_cents = new_total % 100

        self.price.set_value(new_whole, new_cents)

    def info(self):
        return f"{self.name}: {self.price}"

price = Money(10, 50)
product = Product("Coffee Beans", price)
print(product.info())

discount = Money(2, 30)
product.reduce_price(discount)
print(product.info())