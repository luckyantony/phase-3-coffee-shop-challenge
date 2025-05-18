class order:

    all_orders = []

    def __init__(self, customer, coffee, price):
        if isinstance(price, float) and (1.0 < =10.0):
            self.customer = customer
            self.coffee = coffee
            self.price = price