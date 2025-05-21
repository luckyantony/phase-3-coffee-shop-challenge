# phase-3-coffee-shop-challenge

## Overview
The **Coffee Shop Challenge** is a Python project developed for the Coffee shop Code Challenge. It implements a coffee shop domain model with three core classes: `Customer`, `Coffee`, and `Order`. The project demonstrates object-oriented programming principles, including  properties and relationships. It includes unit tests to verify functionality and a debug script for manual testing.

## Features

### Customer Class
- Manages customer names (1–15 characters, string).
- Tracks orders and unique coffees ordered.
- Supports creating new orders and finding the customer who spent the most on a specific coffee.

### Coffee Class
- Manages coffee names (≥3 characters, string, immutable).
- Tracks orders and unique customers.
- Calculates the number of orders and average order price.

### Order Class
- Links customers and coffees with a price (1.0–10.0, float, immutable).
- Provides access to customer and coffee instances.

### Relationships
- Customers can have multiple orders for different coffees.
- Coffees can be ordered by multiple customers.
- Orders connect one customer to one coffee with a specific price.

### Tests
- Comprehensive unit tests for all classes using `pytest`.

### Debug Script
- A script to manually test functionality and demonstrate relationships.

### Project Structure

coffee-shop-challenge/
├── Pipfile
├── README.md
├── debug.py
├── customer.py
├── coffee.py
├── order.py
└── tests/
├── customer_test.py
├── coffee_test.py
└── order_test.py


- `Pipfile`: Specifies project dependencies (pytest).
- `README.md`: Project documentation (this file).
- `debug.py`: Script for manual testing of classes and methods.
- `customer.py`: Implements the `Customer` class.
- `coffee.py`: Implements the `Coffee` class.
- `order.py`: Implements the `Order` class.
- `tests/`: Contains unit tests for each class.

### Requirements

- **Python**: Version 3.8 or higher  
- **Pipenv**: For managing virtual environments and dependencies  
- **pytest**: For running unit tests

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd coffee-shop-challenge
2. **Install Dependencies:**
   ```bash
   pipenv install
4. **Activate the Virtual Environment:**
   ```bash
   pipenv shell

### Running Tests
```bash
python -m pytest tests/ -v
```
### Running the Debug Script
```bash
python debug.py

Built with 💻 and ☕ by Luckyantony Leshan