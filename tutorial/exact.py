# encoding=utf8

from BeautifulSoup import BeautifulSoup as BS
import urllib2
import sys
import html2text

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    with open("export/[adayroi.com]phone-0.html") as fp:
        soup = BS(fp)

        # HTML2Text: for exact text from html
        h = html2text.HTML2Text()

        # get heading 1
        h1 = soup.h1.text

        # get the category that adayroi define
        category = soup.findAll("ol", {"class": "header__breadcrumb breadcrumb"})
        for index, element in enumerate(category[0]):
            if(index == 4):
                print(element.text)

        # get brand
        top_description = soup.findAll("div", {"class": "product-detail__title-brand"})

        for index, a in enumerate(top_description[0]):
            if(type(a).__name__ == "Tag" and a.get('href') != None):
                print(a.text)

        allH3 = soup.findAll("h3", {"class": "product-detail__sidebar__title"})

        # get the last h3, where contain store name
        for element in allH3[-1:]:
            store_name = element.text.split('bởi'.decode('utf-8'), 1)[-1]
            print(store_name)

        # get serial number
        serial_number = soup.findAll("span", {"class": "panel-serial-number"})
        print(serial_number[0].text)

        # get description
        product_description = soup.findAll("div", {"class": "product-detail__description"})
        #print(h.handle(str(product_description[0])))

if __name__== "__main__":
    main()
