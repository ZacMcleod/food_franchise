from order import *
from logger import *

def place_order_method(order_count, order_price_count, franchise):
    log = Logger()
    choice = input(f"What Dish do you want: {dish_list} > ").lower()

    if choice in dish_list:
        order = OrderFactory.order_factory(choice)
        order_count += 1
        order_price_count += order.price
        print(f'{order.dish}: ${order.price}')
        log.log(order_count, order_price_count, franchise)
    else:
        print("Not on the menu...")
    return order_count, order_price_count, franchise