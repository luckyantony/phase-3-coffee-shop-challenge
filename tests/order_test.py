from customer import Customer
from coffee import Coffee
from order import Order

def test_order_price():
    cust = Customer("Liam")
    cof = Coffee("Mocha")
    o = Order(cust, cof, 5.0)
    assert o.price == 5.0
