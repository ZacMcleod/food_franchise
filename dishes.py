

class Meal():
    def __init__(self, dish, price):
        self.dish = dish
        self.price = price

class Steak(Meal):
    def __init__(self):
        super().__init__("steak", 19.99)

class Shrimp(Meal):
    def __init__(self):
        super().__init__("shrimp", 11.99)

class Chicken(Meal):
    def __init__(self):
        super().__init__("chicken", 15.99)