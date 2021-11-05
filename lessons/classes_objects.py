"""Example of a class and object instanciation."""


class Pizza:
    """Models the idea of a Pizza."""

    # Attribute Definitions
    size: str
    toppings: int
    extra_cheese: bool = False


    def __init__(self, size: str, toppings: int):
        """Constructor definition for initialization of attributes."""
        self.size = size
        self.toppings = toppings


    def price(self, tax: float) -> float:
        """Calculate the price of a Pizza."""
        total: float = 0.0
        if self.size == "large":
            total += 10.0
        else:
            total += 8.0

        total += self.toppings * 0.75

        total *= tax

        if self.extra_cheese:
            total += 1.0

        return total


a_pizza: Pizza = Pizza("large", 3)
# a_pizza.size = "large"
# a_pizza.toppings = 3
# a_pizza.extra_cheese = False

another_pizza: Pizza = Pizza("small", 0)
another_pizza.extra_cheese = True

print(a_pizza)
print(a_pizza.size)
print(f"Price: ${a_pizza.price(1.05)}")