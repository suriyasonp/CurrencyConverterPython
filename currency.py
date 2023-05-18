from datetime import date
import myfunctions as mf

from currency_converter import CurrencyConverter


def get_available_currencies():
    c = CurrencyConverter()
    result = c.currencies
    return result


def convert_currency_rate(amount, source_currency, des_currency):
    c = CurrencyConverter(fallback_on_missing_rate=True)
    converted_result = c.convert(amount, source_currency, des_currency)
    return converted_result


def convert_currency_rate_by_date(amount, source_currency, des_currency, selected_date):
    try:
        c = CurrencyConverter(decimal=True)
        converted_result = c.convert(amount, source_currency, des_currency, date=date.fromisoformat(selected_date))
        return converted_result
    except ValueError:
        mf.message_something_went_wrong("Value invalid!")


def is_currency_available(currency):
    c = CurrencyConverter()
    return currency in c.currencies


def rate_bounds(currency):
    c = CurrencyConverter()
    return c.bounds[currency]

