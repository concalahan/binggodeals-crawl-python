from list_definition import BRAND_LIST
from bs4 import BeautifulSoup
from urllib.request import urlopen
from general import *

class matchingProduct():

    def __init__(self, project_name, site_name):
        self.site_name = site_name
        self.project_name = project_name


    def get_product_name(self, brand):
        product_set = set()
        product_list_path = self.project_name + '/' + brand + '/' + '/phones_list.txt'
        with open(product_list_path, 'r') as file:
            for product in file:
                product = product.replace('\n', '')
                product_set.add(product)
        return product_set

    def get_url_name(self,brand):
        url_name = list()
        url_name_path = self.project_name + '/' + brand + '/' + self.site_name + '/' + self.site_name + '_phone-urls.txt'
        with open (url_name_path, 'r') as file:
            for url in file:
                url = url.replace('\n', '')
                url_name.append(url)
        return url_name

    def matching(self):
        for brand in BRAND_LIST:
            product_matching_path = self.project_name + '/' + brand + '/matched_products'
            create_project_dir(product_matching_path)
            product_set = self.get_product_name(brand)
            url_list = self.get_url_name(brand)

            for url in url_list:
                print(url + " is checking ...")
                if self.site_name == 'tiki':
                    try:
                        soup = BeautifulSoup(urlopen(url), "lxml")
                    except Exception:
                        print('Exception : ' + str(Exception))
                        pass
                    h1_title = soup.find("h1")

                    if h1_title is None: continue
                    title = h1_title.get_text()
                    title = title.lower()

                    for product in product_set:
                        product_text = product.replace(' ', '_')
                        new_product_matching_path = product_matching_path + '/' + product_text + '.txt'
                        if product in title:
                            print(product + " is matched !")
                            append_to_file(new_product_matching_path, url)




