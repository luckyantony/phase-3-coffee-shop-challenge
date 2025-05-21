import pytest

from coffee import Coffee

def test_coffee_name():
    c = Coffee("Latte")
    assert c.name == "Latte"
