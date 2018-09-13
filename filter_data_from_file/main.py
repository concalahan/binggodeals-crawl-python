# encoding=utf8

from html.parser import HTMLParser
from bs4 import BeautifulSoup
import html2text
import sys
import os, os.path
import json
import datetime

sys.path.append(os.path.realpath('..'))

def create_project_dir(directory):
    if not os.path.exists(directory) :
        print('Create directory : ' + directory)
        os.makedirs(directory)
    else:
        print(directory + ' is already created !')

def json_serial(obj):
    """JSON serializer for objects not serializable by default json code"""

    if type(obj) is datetime.date or type(obj) is datetime.datetime:
        return obj.isoformat()
    raise TypeError ("Type %s not serializable" % type(obj))

def main():
    if(len(sys.argv) != 2):
        print("Arguments must be in format: python3 main.py HOMEPAGE")
        return

    PROJECT_NAME = sys.argv[1]

    now = datetime.datetime.now()

    # read data from this directory
    READ_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/raw/'

    # read data from this directory
    WRITE_DIR = '../data/' + str(now.year) + '/' + str(now.month) + '/' + str(now.day) + '/json/'

    # create the directory if not empty
    create_project_dir(WRITE_DIR)

    # get number of files in directory
    export_files_length = len([name for name in os.listdir(READ_DIR) if os.path.isfile(os.path.join(READ_DIR, name))])

    for filename in os.listdir(READ_DIR):
        print("Processing file: " + str(filename))

        with open(READ_DIR + filename) as fp:
            data = {}

            soup = BeautifulSoup(fp, "lxml")

            # HTML2Text: for exact text from html
            h = html2text.HTML2Text()

            # delete .html
            filenameNotHtml = filename[:-5]

            # get meaningful url: dien thoai nokia 105 dual sim 2017 hang chinh hang
            # convert - to ''
            meaningful_url = filenameNotHtml.replace("-", " ")

            # terminate the brand name
            meaningful_url = meaningful_url.split('|', 1)[-1]

            # find the index of last space
            indexLastSpace = meaningful_url.rfind(' ')

            # delete all char after that index
            meaningful_url = meaningful_url[:indexLastSpace]

            # get the product that tiki define
            name = soup.h1.text

            url = soup.findAll("link", {"rel": "canonical"})
            url = url[0]['href']

            # get the category that tiki define
            category_temp = soup.findAll("ul", {"class": "breadcrumb"})
            category = ''

            for i, element in enumerate(category_temp[0]):
                if(i == 3):
                    category = element.text

            # get the store that tiki define
            store = soup.findAll("div", {"class": "current-seller"})

            # ensure the store is not empty
            if(len(store) != 0):
                store = store[0].text
            else:
                store = ''

            description_temp = soup.findAll("div", {"class": "top-feature-item"})
            description_temp_2 = soup.findAll("div", {"class": "product-description"})
            
            product_description_1 = ''
            if(len(description_temp) != 0):
                product_description_1 = h.handle(str(description_temp[0]))

            product_description_2 = ''
            if(len(description_temp_2) != 0):
                product_description_2 = h.handle(str(description_temp_2[0]))

            # get the product description that tiki define
            product_description = product_description_1 + "\n" + product_description_2

            # get the origin and true price that tiki define
            true_price = soup.findAll("span", {"id": "span-price"})[0].text
            origin_price = soup.findAll("span", {"id": "span-list-price"})[0].text

            # add to one object
            data['url'] = url
            data['meaningful_url'] = meaningful_url
            data['name'] = name
            data['category'] = category
            data['store'] = store
            data['product_description'] = product_description
            data['true_price'] = true_price
            data['origin_price'] = origin_price
            data['created'] = json_serial(now)

            # write that object to json
            with open(WRITE_DIR + filename + '.json', 'w') as outfile:
                json.dump(data, outfile)

if __name__== "__main__":
    main()