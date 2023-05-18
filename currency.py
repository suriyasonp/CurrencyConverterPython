from currency_converter import CurrencyConverter


def get_available_currencies():
    c = CurrencyConverter()
    result = c.currencies
    return result


def convert_currency_rate(amount, source_currency, dest_currency):
    c = CurrencyConverter(fallback_on_missing_rate=True)
    converted_result = c.convert(amount, source_currency, dest_currency)
    return converted_result


def is_currency_available(currency):
    c = CurrencyConverter()
    return currency in c.currencies
