# encoding=utf8
import sys
import scrapy

reload(sys)
sys.setdefaultencoding('utf8')



# run: scrapy crawl adayroi
class QuotesSpider(scrapy.Spider):
    name = "adayroi"
    count = 0
    is_crawl_product = False
    start_urls = [
    'https://www.adayroi.com/dien-thoai-di-dong-c323'
    ]

    # cause there are 20 pages in the category
    #for i in range(1, 20):
    #   start_urls.append('https://www.adayroi.com/dien-thoai-di-dong-c323?q=%3Arelevance&page=' + str(i))

    # go here first
    def parse(self, response):
        if(self.is_crawl_product):
            # crawl product
            for url in response.css('a.product-item__info-title'):
                # get the product url in the category page
                product_url = url.css('a::attr(href)').extract_first()

                print("process " + product_url)

                # parse it/ download it
                yield response.follow(product_url, callback=self.parseProduct)
        else:
            for li in response.css('li a'):
                li_title = li.css('::text').extract_first()
                if li_title is not None and li_title.decode('utf-8') == ' Trang cuối'.decode('utf-8'):
                    # get the href attribute of <a>
                    last_pagination_href = li.css('::attr(href)').extract_first()

                    # switch to crawl product mode
                    self.is_crawl_product = True

                    # get the largest pagination number
                    last_pagination_index = last_pagination_href[-2:]

                    for i in range(1, int(last_pagination_index)):
                        yield scrapy.Request('https://www.adayroi.com/dien-thoai-di-dong-c323?q=%3Arelevance&page=' + str(i), callback=self.parse)

                    break

    # then go here
    def parseProduct(self, response):
        filename = 'export/[adayroi.com]phone-%s.html' % self.count
        self.count += 1
        with open(filename, 'wb') as f:
            f.write(response.body)
