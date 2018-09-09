
from arctic import Arctic
from datetime import datetime
import pandas as pd
import os
import json

now = datetime.now()

READ_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/json/'

def main():
    # Connect to the mongo-host / cluster
    store = Arctic('localhost')

    # Data is grouped into 'libraries'.
    # Users may have one or more named libraries:

    # Create a library
    store.initialize_library('vu.product_1')

    # Get a library
    # library = m['username.<library>']
    library = store['vu.product_1']

    for filename in os.listdir(READ_DIR):

        with open(READ_DIR + filename) as fp:
            data = json.load(fp)
            # print(data['url'])

            # Store some data in the library
            library.write('PRODUCT', data)

            # # Read some data from the library
            # # (Note the returned object has an associated version number and metadata.)
            # library.read('SYMBOL')

            # # Store some data into the library
            # library.write('MY_DATA', library.read('SYMBOL').data)

            # # What symbols (keys) are stored in the library
            # library.write('MY_DATA', library.read('SYMBOL').data, metadata={'some_key': 'some_value'})

            # # Find available versions of a symbol
            # print(library.read('SYMBOL', as_of=1).data)

if __name__== "__main__":
    main()