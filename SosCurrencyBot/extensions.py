import json
import requests
from config import keys


class ConvertionExeption(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: float):
        if quote == base:
            raise ConvertionExeption(f"Невозможно конвертировать одинаковые валюты {base}")

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ConvertionExeption(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f"Не удалось обработать количество {amount}.")

        quote_ticker = keys[quote.lower()]
        base_ticker = keys[base.lower()]
        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base.lower()]]*float(amount)

        return total_base