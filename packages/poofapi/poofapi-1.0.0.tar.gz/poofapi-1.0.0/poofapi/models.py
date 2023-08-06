class Invoice:
    def __init__(self, id, crypto, amount, metadata=None):
        self.id = id
        self.crypto = crypto
        self.amount = amount
        self.metadata = metadata

class Charge:
    def __init__(self, id, crypto, amount, metadata=None):
        self.id = id
        self.crypto = crypto
        self.amount = amount
        self.metadata = metadata

class FiatInvoice:
    def __init__(self, id, payment, currency, amount, redirect_url=None, success_url=None):
        self.id = id
        self.payment = payment
        self.currency = currency
        self.amount = amount
        self.redirect_url = redirect_url
        self.success_url = success_url

class FiatCharge:
    def __init__(self, id, payment, currency, amount, redirect_url=None, success_url=None):
        self.id = id
        self.payment = payment
        self.currency = currency
        self.amount = amount
        self.redirect_url = redirect_url
        self.success_url = success_url

class Transaction:
    def __init__(self, id):
        self.id = id

class Payout:
    def __init__(self, crypto, amount, address):
        self.crypto = crypto
        self.amount = amount
        self.address = address

class Wallet:
    def __init__(self, currency):
        self.currency = currency

class Balance:
    def __init__(self, balance, crypto):
        self.balance = balance
        self.crypto = crypto

class Price:
    def __init__(self, usd, usd_24h_change):
        self.usd = usd
        self.usd_24h_change = usd_24h_change

class Webhook:
    def __init__(self, url):
        self.url = url

class Product:
    def __init__(self, product_id):
        self.product_id = product_id

class GasPrice:
    def __init__(self, gas_price):
        self.gas_price = gas_price

class Contract:
    def __init__(self, id, name, symbol, address):
        self.id = id
        self.name = name
        self.symbol = symbol
        self.address = address

class Checkout:
    def __init__(self, payload):
        self.payload = payload