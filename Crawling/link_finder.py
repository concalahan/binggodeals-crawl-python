from html.parser import HTMLParser
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse


class LinkFinder_Tiki():

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.links = set()

    def getProductTiki(self, base_url):
# =============================================================================
#         Code below is aim to get all URLs of each brand of phones in Tiki.vn
# =============================================================================
        brandUrl = set()
        soup = BeautifulSoup(urlopen(base_url),"lxml")
        division = soup.find("div", {"id":"collapse-brand","class":"panel-collapse collapse in","role":"tabpanel","aria-labelledby":"heading-brand"})
        anchors = division.find_all('a')

        for anchor in anchors:
            if anchor.get('href') != 'javascript:void(0)':
                brandUrl.add('https://tiki.vn' + anchor.get('href'))
                
# =============================================================================
#         Using brandUrl set() to get numpage of each URL
# =============================================================================
        Url_and_numpage = dict()
        for url in brandUrl:
            maxNumPage = 1
            soup = BeautifulSoup(urlopen(url),"lxml")
            division = soup.find("div", {"class":"list-pager"})
            print('Get numpage ' + url)
            if division == None :
                Url_and_numpage.update({url:maxNumPage})
            else:
                anchors = division.find_all('a')
                for anchor in anchors:
                    if int(anchor.get('href')[-1]) > maxNumPage:
                        maxNumPage = int(anchor.get('href')[-1])
                Url_and_numpage.update({url:maxNumPage})
        
# =============================================================================
#         Pass all URLs of phones and tablet in Tiki.vn into .txt file
# =============================================================================
        for url,numpages in Url_and_numpage.items():
            for page in range(1,numpages+1):
                urlWithPage = url + '&page=' + str(page)
                print('... Crawling ' + urlWithPage)
                soup = BeautifulSoup(urlopen(urlWithPage),"lxml")
                division = soup.find("div", {"class":"product-box-list","data-impress-list-title":"Category | Điện Thoại - Máy Tính Bảng"})
                anchors = division.find_all('a')
                for anchor in anchors:
                    self.links.add(anchor.get('href'))
        
        print("Stop crawling product URLs in Tiki.vn!")
    
    
    def page_links(self):
        return self.links

    def error(self, message):
        pass

