from html.parser import HTMLParser
from bs4 import BeautifulSoup
import html2text
import sys
import os, os.path
import json
import datetime

class Parser():
    now = datetime.datetime.now()

    def __init__(self):
        super().__init__()

    def json_serial(obj):
        """JSON serializer for objects not serializable by default json code"""

        if type(obj) is datetime.date or type(obj) is datetime.datetime:
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))

    def parseProductFromTiki(self, filename, fp):
        data = {}

        soup = BeautifulSoup(fp)

        # HTML2Text: for exact text from html
        h = html2text.HTML2Text()

        # delete .html
        filenameNotHtml = filename[:-5]

        url = ''
        meaningful_url = ''
        name = ''
        category = ''
        store = ''
        description = ''
        true_price = ''
        origin_price = ''

        # all sites share this
        url = soup.findAll("link", {"rel": "canonical"})

        # if no canonical url found, skip the iteration
        if(len(url) == 0):
            return

        url = url[0]['href']

        # get the product name
        name = soup.h1.text

        # get meaningful url: dien thoai nokia 105 dual sim 2017 hang chinh hang
        # convert - to ''
        meaningful_url = filenameNotHtml.replace("-", " ")

        # terminate the brand name
        meaningful_url = meaningful_url.split('|', 1)[-1]

        # find the index of last space
        indexLastSpace = meaningful_url.rfind(' ')

        # delete all char after that index
        meaningful_url = meaningful_url[:indexLastSpace]

        # get the category that tiki define
        category_temp = soup.findAll("ul", {"class": "breadcrumb"})
        category = ''

        # ensure the category is not empty
        if(len(category_temp) != 0):
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
        description = product_description_1 + "\n" + product_description_2

        # get the origin and true price that adayroi define
        origin_price = soup.findAll("span", {"id": "span-list-price"})

        if(len(origin_price) != 0):
            origin_price = origin_price[0].text
        else:
            # out of order, must be string because the db is currently store as string
            origin_price = "0"

        true_price = soup.findAll("span", {"id": "span-price"})

        # if there is discount by vinid
        if(len(true_price) != 0):
            true_price = true_price[0].text
        else:
            true_price = origin_price

        # add to one object
        data['url'] = url
        data['meaningful_url'] = meaningful_url
        data['name'] = name
        data['category'] = category
        data['store'] = store
        data['description'] = description
        data['true_price'] = true_price
        data['origin_price'] = origin_price
        data['created'] = Parser.json_serial(Parser.now)

        return data

    def parseProductFromAdayroi(self, filename, fp):
        data = {}

        soup = BeautifulSoup(fp, "lxml")

        # HTML2Text: for exact text from html
        h = html2text.HTML2Text()

        # delete .html
        filenameNotHtml = filename[:-5]

        url = ''
        meaningful_url = ''
        name = ''
        category = ''
        store = ''
        description = ''
        true_price = ''
        origin_price = ''

        # all sites share this
        url = soup.findAll("link", {"rel": "canonical"})

        # if no canonical url found, skip the iteration
        if(len(url) == 0):
            return

        url = url[0]['href']

        # get the product name
        name = soup.h1.text

        # get meaningful url: dien thoai nokia 105 dual sim 2017 hang chinh hang
        # convert - to ''
        meaningful_url = filenameNotHtml.replace("-", " ")

        # terminate the brand name
        meaningful_url = meaningful_url.split('|', 1)[-1]

        # find the index of last space
        indexLastSpace = meaningful_url.rfind(' ')

        # delete all char after that index
        meaningful_url = meaningful_url[:indexLastSpace]

        # get the category that adayroi define
        category_temp = soup.findAll("ol", {"class": "header__breadcrumb"})
        category = ''

        # ensure the category is not empty
        if(len(category_temp) != 0):
            for i, element in enumerate(category_temp[0]):
                if(i == 4):
                    category = element.text

        # get the store that adayroi define
        store = soup.findAll("div", {"class": "product-detail__sidebar__merchant"})

        # ensure the store is not empty
        if(len(store) != 0):
            store = store[0].text
        else:
            store = ''

        store = store.split('bởi')[1]

        description_temp = soup.findAll("div", {"class": "short-des__content"})
        description_temp_2 = soup.findAll("div", {"class": "col-sm-12 detail__info"})

        product_description_1 = ''
        if(len(description_temp) != 0):
            product_description_1 = h.handle(str(description_temp[0]))

        product_description_2 = ''
        if(len(description_temp_2) != 0):
            product_description_2 = h.handle(str(description_temp_2[0]))

        description = product_description_1 + "\n" +  product_description_2

        # get the origin and true price that adayroi define
        origin_price = soup.findAll("span", {"class": "price-info__sale"})

        if(len(origin_price) != 0):
            origin_price = origin_price[0].text
        else:
            # out of order, must be string because the db is currently store as string
            origin_price = "0"

        true_price = soup.findAll("span", {"class": "price-vinid__value"})

        # if there is discount by vinid
        if(len(true_price) != 0):
            true_price = true_price[0].text
        else:
            true_price = origin_price

        # add to one object
        data['url'] = url
        data['meaningful_url'] = meaningful_url
        data['name'] = name
        data['category'] = category
        data['store'] = store
        data['description'] = description
        data['true_price'] = true_price
        data['origin_price'] = origin_price
        data['created'] = Parser.json_serial(Parser.now)

        return data