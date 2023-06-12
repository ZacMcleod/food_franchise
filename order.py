from dishes import *

dish_list = ['steak', 'shrimp', 'chicken']

class OrderFactory:
    @staticmethod
    def order_factory(dish):
        if dish == "steak":
            return Steak()
        elif dish == "shrimp":
            return Shrimp()
        elif dish == "chicken":
            return Chicken()
        else:
            return None