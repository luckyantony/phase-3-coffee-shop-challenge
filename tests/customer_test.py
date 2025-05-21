# import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from customer import Customer
from coffee import Coffee

def test_customer_name():
    c = Customer("Alex")
    assert c.name == "Alex"
    c.name = "Bob"
    assert c.name == "Bob"
    c.name = "X" * 20
    assert c.name == "Bob"  # Shouldn't change
