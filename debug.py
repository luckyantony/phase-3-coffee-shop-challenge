from customer import Customer
from coffee import Coffee
from order import Order

c1 = Customer("Ali")
c2 = Customer("Becky")
c3 = Customer("Cory")

coffee1 = Coffee("Espresso")
coffee2 = Coffee("Latte")

c1.create_order(coffee1, 3.0)
c1.create_order(coffee2, 4.5)
c2.create_order(coffee1, 3.5)
c3.create_order(coffee1, 6.0)

print(coffee1.customers())
print(coffee2.customers())
print(coffee1.average_price())
print(Customer.most_aficionado(coffee1))
