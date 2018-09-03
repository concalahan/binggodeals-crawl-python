
from arctic import Arctic
from datetime import datetime as dt
import pandas as pd


# Connect to the mongo-host / cluster
store = Arctic('localhost')

# Data is grouped into 'libraries'.
# Users may have one or more named libraries:

# Create a library
store.initialize_library('vu.product_price')

# Get a library
# library = m['username.<library>']
library = store['vu.product_price']

# Store some data in the library
df = pd.DataFrame({'prices': [1, 2, 3]},
                  [dt(2014, 1, 1), dt(2014, 1, 2), dt(2014, 1, 3)])
library.write('SYMBOL', df)

# Read some data from the library
# (Note the returned object has an associated version number and metadata.)
library.read('SYMBOL')

# Store some data into the library
library.write('MY_DATA', library.read('SYMBOL').data)

# What symbols (keys) are stored in the library
library.write('MY_DATA', library.read('SYMBOL').data, metadata={'some_key': 'some_value'})

print("AAAA")

# Find available versions of a symbol
print(library.read('SYMBOL', as_of=1).data)