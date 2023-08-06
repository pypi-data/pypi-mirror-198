# ioka Python Library

The ioka Python library convenient access to the ioka API from applications written in the Python language

## Documentation

See the [Python API docs](https://dabarov.github.io/ioka/).

## Installation

You don't need this source code unless you want to modify the package. If you just want to use the package, just run:

```shell
pip install ioka-python
```

## Usage

```python
import ioka_python

ioka_python.api_key = "Hello"

# list orders
orders = ioka_python.Order().list()

# print first order's ID
print(orders[0].id)

# retrieve specific order
order = ioka_python.Order().retrieve("ord_123")

# print that order's amount
print(order.amount)
```

