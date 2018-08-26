# encoding=utf8

from BeautifulSoup import BeautifulSoup as BS
import urllib2
import sys

reload(sys)
sys.setdefaultencoding('utf8')

def main():
    with open("export/[adayroi.com]phone-0.html") as fp:
        soup = BS(fp)

        # get heading 1
        h1 = soup.h1.text

        # get brand
        top_desc = soup.findAll("div", {"class": "product-detail__title-brand"})

        for index, a in enumerate(top_desc[0]):
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


if __name__== "__main__":
    main()
