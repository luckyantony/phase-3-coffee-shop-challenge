class order:


    all_orders = []

    def __init__(self, customer, coffee, price):
        if isinstance(price, float):
            self.customer = customer
            self.coffee = coffee
            self.price = price

