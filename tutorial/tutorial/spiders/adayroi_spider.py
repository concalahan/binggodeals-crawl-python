import scrapy

count = 0

# run: scrapy crawl adayroi
class QuotesSpider(scrapy.Spider):
    name = "adayroi"
    start_urls = []

    # cause there are 20 pages in the category
    for i in range(1, 20):
       start_urls.append('https://www.adayroi.com/dien-thoai-di-dong-c323?q=%3Arelevance&page=' + str(i))

    def parse(self, response):
        for url in response.css('a.product-item__info-title'):
            # get the product url in the category page
            product_url = url.css('a::attr(href)').extract_first()

            # parse it/ download it
            yield response.follow(product_url, callback=self.parseProduct)

    def parseProduct(self, response):
        global count

        filename = 'export/[adayroi.com]phone-%s.html' % count
        count = count+1
        with open(filename, 'wb') as f:
            f.write(response.body)
