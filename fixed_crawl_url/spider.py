from link_finder import LinkFinder
from list_definition import BRAND_LIST
from general import *


class Spider:
    project_name = ''

    def __init__(self, project_name, site_name):
        Spider.project_name = project_name
        self.boot(site_name)
        self.gather_links(site_name)

    @staticmethod
    def boot(site_name):
        # create the directory
        create_project_dir(Spider.project_name)

        for brand in BRAND_LIST:
            create_brand_dir(Spider.project_name, brand)

        for brand in BRAND_LIST:
            path = Spider.project_name + '/' + brand
            create_data_files(path, site_name)



    @staticmethod
    def gather_links(site_name):
        Finder = LinkFinder()
        if site_name == 'tiki':
            Finder.getProductUrlTiki()
        elif site_name == 'adayroi':
            Finder.getProductUrlAdayroi()
        links = Finder.page_links()
        append_urls_to_file(Spider.project_name, site_name, links, BRAND_LIST)
