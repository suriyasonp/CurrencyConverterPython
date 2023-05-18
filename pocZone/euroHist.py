import os.path as op
import urllib.request
from datetime import date

import CurrencyConverter as CurrencyConverter
import pandas as pd
from currency_converter import ECB_URL, SINGLE_DAY_ECB_URL

data = pd.read_csv("../eurofxref-hist.csv")
print(data.head())

