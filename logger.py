
class Logger: 
    def log(self, order_count, order_price_count, franchise):
        if franchise == 1:
            file = open('franchise_1.txt', 'a')
            if order_count == 1:
                file.write(f'The "Steak House Restaurant Buisness" buisness has {order_count} sales and ${order_price_count} to show for it\n\n')
            else:
                file.write(f'Order number: {order_count}   Total money earned: {order_price_count}\n\n')
            file.close()
        elif franchise == 2:
            file = open('franchise_2.txt', 'a')
            if order_count == 1:
                file.write(f'The "Steak House Restaurant Buisness" buisness has {order_count} sales and ${order_price_count} to show for it\n\n')
            else:
                file.write(f'Order number: {order_count}   Total money earned: {order_price_count}\n\n')
            file.close()
        elif franchise == 3:
            file = open('franchise_3.txt', 'a')
            if order_count == 1:
                file.write(f'The "Steak House Restaurant Buisness" buisness has {order_count} sales and ${order_price_count} to show for it\n\n')
            else:
                file.write(f'Order number: {order_count}   Total money earned: {order_price_count}\n\n')
            file.close()
