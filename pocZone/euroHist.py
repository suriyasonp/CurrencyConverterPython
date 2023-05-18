import os.path as op
import urllib.request
from datetime import date

import CurrencyConverter as CurrencyConverter
import pandas as pd
from currency_converter import ECB_URL, SINGLE_DAY_ECB_URL

data = pd.read_csv("../eurofxref-hist.csv")
print(data.head())

filename = f"ecb_{date.today():%Y%m%d}.zip"
if not op.isfile(filename):
    urllib.request.urlretrieve(ECB_URL, filename)

c = CurrencyConverter(filename)
print(c)
#result = c.convert(100, 'THB', date=date(2010, 11, 21))