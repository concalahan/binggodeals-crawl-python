from bs4 import BeautifulSoup
from urllib.request import urlopen
from list_definition import BRAND_LIST
import urllib


class LinkFinder():

    def __init__(self):
        super().__init__()
        self.total_links = 0
        self.links = {}
        self.list_brand = BRAND_LIST

    def page_links(self):
        return self.links

    def error(self, message):
        pass

    def getProductUrlTiki(self):

        # =============================================================================
        #         Using brandUrl set() to get numpage of each URL
        # =============================================================================
        brand_counts = 0
        brand_urls = list()
        url_and_numpage = dict()

        for brand in self.list_brand:
            url = 'https://tiki.vn/dien-thoai-may-tinh-bang/c1789/' + brand
            brand_urls.append(url)

        for url in brand_urls:
            max_num_page = 1
            try:
                soup = BeautifulSoup(urlopen(url), "lxml")
            except Exception:
                print('Exception : ' + str(Exception))
                pass
            division = soup.find("div", {"class": "list-pager"})
            print('Get numpage ' + url)
            if division is None:
                url_and_numpage.update({url: max_num_page})
            else:
                anchors = division.find_all('a')
                for anchor in anchors:
                    if int(anchor.get('href')[-1]) > max_num_page:
                        max_num_page = int(anchor.get('href')[-1])
                url_and_numpage.update({url: max_num_page})

        # =============================================================================
        #         Pass all URLs of phones and tablet in Tiki.vn into .txt file
        # =============================================================================

        for url, num_pages in url_and_numpage.items():
            link_counts = 0
            for page in range(1, num_pages + 1):
                url_with_pages = url + '&page=' + str(page)
                print('... Crawling ' + url_with_pages)
                try:
                    soup = BeautifulSoup(urlopen(url_with_pages), "lxml")
                except Exception:
                    print('Exception : ' + str(Exception))
                    pass
                division = soup.find("div", {"class": "product-box-list",
                                             "data-impress-list-title": "Category | Điện Thoại - Máy Tính Bảng"})
                anchors = division.find_all('a')
                for anchor in anchors:
                    href = anchor.get('href')
                    if '?' in href:
                        href = href.split('?')[:-1][0]
                    self.links[self.list_brand[brand_counts], link_counts] = href
                    self.total_links += 1
                    link_counts += 1
            brand_counts += 1

        print("""---------------------------------
                Stop crawling product URLs in tiki.vn!
                ---------------------------------""")

    def getProductUrlAdayroi(self):
        brand_counts = 0
        list_phones_in_web = ["iphone", "samsung", "oppo", "nokia", "asus", "sony", "xiaomi"]
        list_tablets_in_web = ["apple", "samsung", "xiaomi"]
        brand_urls = list()

        url = 'https://www.adayroi.com/dien-thoai-di-dong-c323'
        try:
            soup = BeautifulSoup(urlopen(url), "lxml")
        except Exception:
            print('Exception : ' + str(Exception))
            pass
        ul_category = soup.find("ul", {"data-role": "listview", "class": "category-menu child-level-3"})
        phones_anchors = ul_category.find_all('a')

        for brand in list_phones_in_web:
            for anchor in phones_anchors:
                if brand in anchor.get('href'):
                    crawl_url = 'https://www.adayroi.com' + anchor.get('href')
                    brand_urls.append(crawl_url)

        url_and_numpage = dict()
        for url in brand_urls:
            max_num_pages = 0
            try:
                soup = BeautifulSoup(urlopen(url), "lxml")
            except Exception:
                print('Exception : ' + str(Exception))
                pass
            nav = soup.find("nav", {"class": "Page navigation"})
            print('Get numpage ' + url)
            if nav is None:
                url_and_numpage.update({url: max_num_pages})
            else:
                anchors = nav.find_all('a')
                if int(anchors[-3].get('href')[-1]) > max_num_pages:
                    max_num_pages = int(anchors[-3].get('href')[-1])
                url_and_numpage.update({url: max_num_pages})

        # =============================================================================
        #         Pass all URLs of phones and tablet in Adayroi into .txt file
        # =============================================================================
        for url, num_pages in url_and_numpage.items():
            link_counts = 0
            for page in range(0, num_pages + 1):
                url_with_page = url + '?q=%3Arelevance&page=' + str(page)
                print('... Crawling ' + url_with_page)
                try:
                    soup = BeautifulSoup(urlopen(url_with_page), "lxml")
                except Exception:
                    print('Exception : ' + str(Exception))
                    pass
                division = soup.find("div", {"class": "product-list__container"})
                anchors = division.find_all('a')
                for anchor in anchors:
                    href = 'https://adayroi.com' + anchor.get('href')
                    if '?' in href:
                        href = href.split('?')[:-1][0]
                    self.links[self.list_brand[brand_counts], link_counts] = href
                    self.total_links += 1
                    link_counts += 1
            brand_counts += 1

        print("""---------------------------------
        Stop crawling product URLs in Adayroi.com!
        ---------------------------------""")

    def getProductUrlCellPhoneS(self):
        brand_counts = 0
        brand_urls = list()
        url_and_numpage = dict()

        for brand in self.list_brand:
            url = 'https://cellphones.com.vn/mobile/' + brand + '.html'
            brand_urls.append(url)

        # Create a Header to help the beautifulSoup can crawl the web page
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}

        for url in brand_urls:
            max_num_page = 1

            data1 = urllib.request.Request(url, headers=headers)
            data = urllib.request.urlopen(data1).read()
            try:
                soup = BeautifulSoup(data, "lxml")
            except Exception:
                print('Exception : ' + str(Exception))

            division = soup.find("div", {"class": "pages"})
            print('Get numpage ' + url)
            if division is None:
                url_and_numpage.update({url: max_num_page})
            else:
                anchors = division.find_all('a')
                for anchor in anchors:
                    if "javascript" in anchor.get('href'):
                        continue
                    if int(anchor.get('href')[-1]) > max_num_page:
                        max_num_page = int(anchor.get('href')[-1])
                url_and_numpage.update({url: max_num_page})

        # =============================================================================
        #         Pass all URLs of phones and tablet in Cellphones.com.vn into .txt file
        # =============================================================================

        for url, num_pages in url_and_numpage.items():
            link_counts = 0
            for page in range(1, num_pages + 1):
                url_with_pages = url + '?p=' + str(page)
                print('... Crawling ' + url_with_pages)

                data1 = urllib.request.Request(url_with_pages, headers=headers)
                data = urllib.request.urlopen(data1).read()

                try:
                    soup = BeautifulSoup(data, "lxml")
                except Exception:
                    print('Exception : ' + str(Exception))
                    pass
                division = soup.find("div", {"class": "products-container"})
                anchors = division.find_all('a')
                for anchor in anchors:
                    href = anchor.get('href')
                    if '?' in href:
                        href = href.split('?')[:-1][0]
                    self.links[self.list_brand[brand_counts], link_counts] = href
                    self.total_links += 1
                    link_counts += 1
            brand_counts += 1

        print("""---------------------------------
                Stop crawling product URLs in Cellphones.com.vn!
                ---------------------------------""")

    def getProductUrlTheGioiDiDong(self):
        brand_counts = 0
        list_phones_in_web = ["apple-iphone", "samsung", "oppo", "nokia", "asus-zenfone", "sony", "xiaomi"]
        list_tablets_in_web = ["apple", "samsung", "xiaomi"]
        brand_urls = list()
        standard_phone_list = list()  # This list to store the phones without all the memory type
        headers = {'User-Agent': 'User-Agent:Mozilla/5.0'}

        for brand in list_phones_in_web:
            url = 'https://www.thegioididong.com/dtdd-' + brand + '#i:2'
            brand_urls.append(url)

        for url in brand_urls:
            data1 = urllib.request.Request(url, headers=headers)
            data = urllib.request.urlopen(data1).read()

            try:
                print("Open URL : " + url)
                soup = BeautifulSoup(data, "lxml")
            except Exception:
                print('Exception : ' + str(Exception))
                pass
            product_ul = soup.find("ul", {"class": "homeproduct filter-cate"})
            anchors = product_ul.find_all('a')
            for anchor in anchors:
                href = anchor.get('href')
                href = 'https://www.thegioididong.com' + href
                if '?' in href:
                    href = href.split('?')[:-1][0]
                standard_phone_list.append(href)

        for url in standard_phone_list:
            link_counts = 0
            data1 = urllib.request.Request(url, headers=headers)
            data = urllib.request.urlopen(data1).read()

            try:
                print("... Crawling " + url)
                soup = BeautifulSoup(data, "lxml")
            except Exception:
                print('Exception : ' + str(Exception))
                pass

                # get the status of phone
                span_status = soup.find("span", {"class": "productstatus"})
                # Check if the status is none
                if span_status is not None:
                    # If the product 's status is "Ngừng kinh doanh' then continue to the next url
                    if 'Ngừng kinh doanh'.lower() in span_status.get_text().lower(): continue
                memmory_div = soup.find("span", {"class": "memory memory2 "})
                # Check if there are more than 1 memory type of this phone
                if memmory_div is None:
                    print('... Crawling ' + url)
                    self.links[self.list_brand[brand_counts], link_counts] = url
                    self.total_links += 1
                    link_counts += 1
                else:
                    anchors = memmory_div.find_all('a')
                    for href in anchors:
                        href = 'https://www.thegioididong.com' + href
                        print('... Crawling ' + href)
                        self.links[self.list_brand[brand_counts], link_counts] = href
                        self.total_links += 1
                        link_counts += 1
