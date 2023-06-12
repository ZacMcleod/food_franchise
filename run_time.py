from place_order import place_order_method


def run_time():
    franchise = 1
    print('Franchise 1 orders:\n')
    while True:
        order_count, order_price_count, franchise = place_order_method(order_count, order_price_count, franchise)
        if input("Any more orders? Y / N > ").lower() == "n":
            break
    franchise = 2
    print('Franchise 2 orders:\n')
    while True:
        order_count, order_price_count, franchise = place_order_method(order_count, order_price_count, franchise)
        if input("Any more orders? Y / N > ").lower() == "n":
            break
    franchise = 3
    print('Franchise 3 orders:\n')
    while True:
        order_count, order_price_count, franshise = place_order_method(order_count, order_price_count, franchise)
        if input("Any more orders? Y / N > ").lower() == "n":
            break