import scrapy
from ..items import AmazonwebsiteItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    start_urls = [
        'https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_condition-type%3A8609960031&dc&language=en_IN&crid=CHLYEOE9XILR&qid=1654947968&rnid=2684818031&sprefix=books%2Caps%2C877&ref=sr_nr_p_n_publication_date_1'
                 ]

    def parse(self, response):
        items = AmazonwebsiteItem()

        product_name = response.css('.a-size-medium::text').extract()
        product_author = response.css('.a-color-secondary .a-size-base:nth-child(2) , .a-color-secondary .a-size-base.s-link-style , .widgetId\=search-results_9 .a-color-secondary span.a-size-base+ .a-size-base , .widgetId\=search-results_1 .a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.s-price-instructions-style .a-price-whole').css('::text').extract()
        product_imagelink = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        next_page = 'https://www.amazon.in/s?k=books&i=stripbooks&rh=n%3A976389031%2Cp_n_feature_three_browse-bin%3A9141482031%2Cp_n_condition-type%3A8609960031&dc&page='+ str(AmazonSpiderSpider.page_number) + '&language=en_IN&crid=CHLYEOE9XILR&qid=1655022695&rnid=2684818031&sprefix=books%2Caps%2C877&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number <= 75:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback = self.parse)




