import requests


class PoofAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://www.poof.io/api/v2"
        self.headers = {
            "Authorization": self.api_key,
            "content-type": "application/json"
        }

    def create_invoice(self, crypto, amount, metadata=None):
        url = f"{self.base_url}/create_invoice"
        payload = {
            "metadata": metadata,
            "crypto": crypto,
            "amount": amount
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_charge(self, crypto, amount, metadata=None):
        url = f"{self.base_url}/create_charge"
        payload = {
            "metadata": metadata,
            "crypto": crypto,
            "amount": amount
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_fiat_invoice(self, payment, currency, amount, redirect_url=None, success_url=None):
        url = f"{self.base_url}/create_fiat_invoice"
        payload = {
            "payment": payment,
            "currency": currency,
            "amount": amount,
            "redirect_url": redirect_url,
            "success_url": success_url
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_fiat_charge(self, payment, currency, amount, redirect_url=None, success_url=None):
        url = f"{self.base_url}/create_fiat_charge"
        payload = {
            "payment": payment,
            "currency": currency,
            "amount": amount,
            "redirect_url": redirect_url,
            "success_url": success_url
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def transaction(self, transaction_id):
        url = f"{self.base_url}/transaction"
        payload = {"transaction": transaction_id}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def payout(self, crypto, amount, address):
        url = f"{self.base_url}/payouts"
        payload = {
            "amount": amount,
            "crypto": crypto,
            "address": address
        }
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_wallet(self, currency):
        url = f"{self.base_url}/create_wallet"
        payload = {"currency": currency}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def balance(self, crypto):
        url = f"{self.base_url}/balance"
        payload = {"crypto": crypto}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def price(self, crypto):
        url = f"{self.base_url}/price"
        payload = {"crypto": crypto}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_webhook(self, url):
        url = f"{self.base_url}/create_webhook"
        payload = {"url": url}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_product(self, product_id):
        url = f"{self.base_url}/fetch_product"
        payload = {"product_id": product_id}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def gas_price(self, crypto):
        url = f"{self.base_url}/gas_price"
        payload = {"crypto": crypto}
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def contract_list(self):
        url = f"{self.base_url}/contract_list"
        response = requests.post(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def checkout(self, payload):
        url = f"{self.base_url}/checkout"
        response = requests.post(url, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

