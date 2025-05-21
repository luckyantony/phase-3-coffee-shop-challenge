import pytest

from customer import Customer
from coffee import Coffee

def test_customer_name():
    c = Customer("Alex")
    assert c.name == "Alex"
    c.name = "Bob"
    assert c.name == "Bob"
    c.name = "X" * 20
    assert c.name == "Bob"  # Shouldn't change
