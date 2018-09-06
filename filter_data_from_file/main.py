# encoding=utf8

from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse
import html2text
import sys
import os, os.path
import json

sys.path.append(os.path.realpath('..'))

PROJECT_NAME = 'tiki'

# read data from this directory
READ_DIR = '../data/raw_products/'

# read data from this directory
WRITE_DIR = '../data/json_products/'

def create_project_dir(directory):
    if not os.path.exists(directory) :
        print('Create directory : ' + directory)
        os.makedirs(directory)
    else:
        print(directory + ' is already created !')

def main():
    # create the directory if not empty
    create_project_dir(WRITE_DIR)

    # get number of files in directory
    export_files_length = len([name for name in os.listdir(READ_DIR) if os.path.isfile(os.path.join(READ_DIR, name))])

    for index in range(0, export_files_length):
        print("Processing file number " + str(index))

        with open(READ_DIR + '[' + PROJECT_NAME + ']raw_0.html') as fp:
            data = {}

            soup = BeautifulSoup(fp, "lxml")

            # HTML2Text: for exact text from html
            h = html2text.HTML2Text()

            # get the product that tiki define
            name = soup.h1.text

            # get the category that tiki define
            category_temp = soup.findAll("ul", {"class": "breadcrumb"})
            category = ''

            for i, element in enumerate(category_temp[0]):
                if(i == 3):
                    category = element.text

            # get the store that tiki define
            store = soup.findAll("div", {"class": "current-seller"})[0].text

            description_temp = soup.findAll("div", {"class": "top-feature-item"})
            description_temp_2 = soup.findAll("div", {"class": "product-description"})
            
            product_description_1 = h.handle(str(description_temp[0]))
            product_description_2 = h.handle(str(description_temp_2[0]))

            # get the product description that tiki define
            product_description = product_description_1 + "\n" + product_description_2

            # get the origin and true price that tiki define
            true_price = soup.findAll("span", {"id": "span-price"})[0].text
            origin_price = soup.findAll("span", {"id": "span-list-price"})[0].text

            # add to one object
            data['name'] = name
            data['category'] = category
            data['store'] = store
            data['product_description'] = product_description
            data['true_price'] = true_price
            data['origin_price'] = origin_price

            # write that object to json
            with open(WRITE_DIR + '[' + PROJECT_NAME + ']product_' + str(index) + '.json', 'w') as outfile:
                json.dump(data, outfile)

if __name__== "__main__":
    main()