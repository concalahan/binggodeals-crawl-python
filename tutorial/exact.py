# encoding=utf8

from BeautifulSoup import BeautifulSoup as BS
import urllib2
import sys
import html2text
import json
import os, os.path

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    DIR = 'export'
    export_files_length = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])

    for i in range(0, export_files_length):
        print("Processing file number " + str(i))
        with open("export/[adayroi.com]phone-" + str(i) + ".html") as fp:
            soup = BS(fp)

            data = {}

            # HTML2Text: for exact text from html
            h = html2text.HTML2Text()

            # get name of product
            h1 = soup.h1.text

            category = ''
            store_name = ''

            # get the category that adayroi define
            category_temp = soup.findAll("ol", {"class": "header__breadcrumb breadcrumb"})
            for index, element in enumerate(category_temp[0]):
                if(index == 4):
                    category = element.text

            # get brand
            top_description = soup.findAll("div", {"class": "product-detail__title-brand"})

            for index, a in enumerate(top_description[0]):
                if(type(a).__name__ == "Tag" and a.get('href') != None):
                    top_description = a.text

            allH3 = soup.findAll("h3", {"class": "product-detail__sidebar__title"})

            # get the last h3, where contain store name
            for element in allH3[-1:]:
                store_name = element.text.split('bởi'.decode('utf-8'), 1)[-1]


            # get serial number
            serial_number = soup.findAll("span", {"class": "panel-serial-number"})[0].text

            # get description
            product_description_temp = soup.findAll("div", {"class": "product-detail__description"})
            product_description = h.handle(str(product_description_temp[0]))

            # add to one object
            data['category'] = category
            data['top_description'] = top_description
            data['store_name'] = store_name
            data['serial_number'] = serial_number
            data['product_description'] = product_description

            # write that object to json
            with open('filter/[adayroi.com]phone-' + str(i) + '-filter.json', 'w') as outfile:
                json.dump(data, outfile)

if __name__== "__main__":
    main()
