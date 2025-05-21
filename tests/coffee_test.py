# import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from coffee import Coffee

def test_coffee_name():
    c = Coffee("Latte")
    assert c.name == "Latte"
