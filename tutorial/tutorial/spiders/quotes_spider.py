import scrapy

count = 0

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = []
    # start_urls = [
    #     'https://www.adayroi.com/dien-thoai-di-dong-c323?q=%3Arelevance&page=1'
    # ]
    for i in range(1, 20):
       start_urls.append('https://www.adayroi.com/dien-thoai-di-dong-c323?q=%3Arelevance&page=' + str(i))

    def parse(self, response):
        for url in response.css('a.product-item__info-title'):
            #print(url.css('a::attr(href)').extract_first())
            product_url = url.css('a::attr(href)').extract_first()

            yield response.follow(product_url, callback=self.parseProduct)

    def parseProduct(self, response):
        global count
        print('----------------------------')
        #file_name = url.css('a::attr(href)').extract_first()
        filename = 'export/phone-%s.html' % count
        count = count+1
        with open(filename, 'wb') as f:
            f.write(response.body)

        # next_page = response.css('ul.pagination li a::attr(href)').extract_first()
        # print("------------")
        # print(next_page)
        #     yield {
        #         'url': quote.css('a::attr(href)').extract_first()
        #     }
        #
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
