class Stock:
    def __init__(self, name, shares, price) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"('{self.name}', {self.shares}, {self.price})"

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, amount):
        self.shares -= amount
