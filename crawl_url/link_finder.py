from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse


class LinkFinder():
    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def getProductUrlTiki(self):
        list_brand = ["apple","samsung","oppo","nokia","asus","sony","xiaomi"]
# =============================================================================
#         Code below is aim to get all URLs of each brand of phones in Tiki.vn
# =============================================================================
        
# =============================================================================
#         brandUrl = set()
#         soup = BeautifulSoup(urlopen(base_url),"lxml")
#         division = soup.find("div", {"id":"collapse-brand","class":"panel-collapse collapse in","role":"tabpanel","aria-labelledby":"heading-brand"})
#         anchors = division.find_all('a')
# 
#         for anchor in anchors:
#             if anchor.get('href') != 'javascript:void(0)':
#                 brandUrl.add('https://tiki.vn' + anchor.get('href'))
#                 
# =============================================================================
        
# =============================================================================
#         Using brandUrl set() to get numpage of each URL
# =============================================================================
        brand_urls = set()
        for brand in list_brand:
            url = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789/' + brand
            brand_urls.add(url)
        
        url_and_numpage = dict()
        for url in brand_urls:
            maxNumPage = 1
            soup = BeautifulSoup(urlopen(url),"lxml")
            division = soup.find("div", {"class":"list-pager"})
            print('Get numpage ' + url)
            if division == None :
                url_and_numpage.update({url:maxNumPage})
            else:
                anchors = division.find_all('a')
                for anchor in anchors:
                    if int(anchor.get('href')[-1]) > maxNumPage:
                        maxNumPage = int(anchor.get('href')[-1])
                url_and_numpage.update({url:maxNumPage})
        
# =============================================================================
#         Pass all URLs of phones and tablet in Tiki.vn into .txt file
# =============================================================================
        for url,numpages in url_and_numpage.items():
            for page in range(1,numpages+1):
                urlWithPage = url + '&page=' + str(page)
                print('... Crawling ' + urlWithPage)
                soup = BeautifulSoup(urlopen(urlWithPage),"lxml")
                division = soup.find("div", {"class":"product-box-list","data-impress-list-title":"Category | Điện Thoại - Máy Tính Bảng"})
                anchors = division.find_all('a')
                for anchor in anchors:
                    self.links.add(anchor.get('href'))
                
        
        print("Stop crawling product URLs in Tiki.vn!")
    
    def getProductUrlAdayroi(self):
        list_brand = ["iphone","samsung","oppo","nokia","asus","sony","xiaomi"]
        
        url = 'https://www.adayroi.com/dien-thoai-di-dong-c323'
        soup = BeautifulSoup(urlopen(url),"lxml")
        ul_category = soup.find("ul",{"data-role":"listview","class":"category-menu child-level-3"})
        anchors = ul_category.find_all('a')
        
        brand_urls = set()
        for anchor in anchors:
            for brand in list_brand :    
                if brand in anchor.get('href'):
                    crawl_url = 'https://www.adayroi.com' + anchor.get('href') 
                    brand_urls.add(crawl_url)
        
        url_and_numpage = dict()
        for url in brand_urls:
            maxNumPage = 0
            soup = BeautifulSoup(urlopen(url),"lxml")
            nav = soup.find("nav", {"class":"Page navigation"})
            print('Get numpage ' + url)
            if nav == None :
                url_and_numpage.update({url:maxNumPage})
            else:
                anchors = nav.find_all('a')
                if int(anchors[-3].get('href')[-1]) > maxNumPage:
                    maxNumPage = int(anchors[-3].get('href')[-1])
                url_and_numpage.update({url:maxNumPage})
        
# =============================================================================
#         Pass all URLs of phones and tablet in Adayroi into .txt file
# =============================================================================
        for url,numpages in url_and_numpage.items():
            for page in range(0,numpages+1):
                urlWithPage = url + '?q=%3Arelevance&page=' + str(page)
                print('... Crawling ' + urlWithPage)
                soup = BeautifulSoup(urlopen(urlWithPage),"lxml")
                division = soup.find("div", {"class":"product-list__container"})
                anchors = division.find_all('a')
                for anchor in anchors:
                    self.links.add('https://www.adayroi.com' + anchor.get('href'))
        
        print("Stop crawling product URLs in Adayroi.com!")

        
    def page_links(self):
        return self.links

    def error(self, message):
        pass

