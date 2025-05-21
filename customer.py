from order import Order

class Customer:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) == str and 1 <= len(value) <= 15:
            self._name = value
        else:
            print("Name must be a string between 1 and 15 characters.")

    def orders(self):
        return [order for order in Order.all_orders if order.customer == self]

    def coffees(self):
        return list(set([order.coffee for order in self.orders()]))

    def create_order(self, coffee, price):
        Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        highest = 0
        top_customer = None
        for order in Order.all_orders:
            if order.coffee == coffee:
                total = sum([o.price for o in Order.all_orders if o.customer == order.customer and o.coffee == coffee])
                if total > highest:
                    highest = total
                    top_customer = order.customer
        return top_customer
