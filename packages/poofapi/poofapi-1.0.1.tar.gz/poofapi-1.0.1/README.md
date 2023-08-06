# **Poof API Python Library**

This is a Python library for interacting with the Poof API. It provides a convenient way to create invoices, charges, fiat invoices, fiat charges, transactions, payouts, wallets, balances, prices, webhooks, products, gas prices, contracts, and checkouts through the Poof API.

## Installation

To install the Poof API Python library, simply use pip:
```pip install poofapi```

## Usage

Here's an example of how to use the Poof API Python library to create a new invoice:

````
from poofapi.api import PoofAPI

# Initialize the Poof API client with your API key
api = PoofAPI(api_key='your_api_key')

# Create a new invoice
invoice = api.create_invoice(crypto='BTC', amount=0.001, metadata={'order_id': '1234'})

# Print the invoice details
print(invoice)

````
## License

This library is released under the MIT License. Please see the LICENSE file for more information.

