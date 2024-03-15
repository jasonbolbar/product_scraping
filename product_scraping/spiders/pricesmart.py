from scrapy.spiders import SitemapSpider
from product_scraping.items import ProductItem


class PricesmartSpider(SitemapSpider):
    name = 'pricesmart'
    sitemap_urls = [
        'https://www.pricesmart.com/sitemap/products/sitemap-pricesmart-products-cr-01.xml',
        'https://www.pricesmart.com/sitemap/products/sitemap-pricesmart-products-cr-02.xml',
        'https://www.pricesmart.com/sitemap/products/sitemap-pricesmart-products-cr-03.xml',
        'https://www.pricesmart.com/sitemap/products/sitemap-pricesmart-products-cr-04.xml',
        'https://www.pricesmart.com/sitemap/products/sitemap-pricesmart-products-cr-05.xml',
        'https://www.pricesmart.com/sitemap/products/sitemap-pricesmart-products-cr-06.xml'
    ]
    
    sitemap_rules = [('/site/cr/es/pagina-producto/', 'parse')]

    def parse(self, response): 
        product_item = ProductItem()
        product_item['name'] = response.xpath('//h1[@id="product-display-name"]/text()').get()
        product_item['price'] = response.xpath('//strong[@id="product-price"]/text()').get()
        product_item['description'] = response.xpath('//div[@id="product-description"]//span/text()').get()
        product_item['url'] = response.url
        product_item['item_id'] = response.xpath('//label[@id="itemNumber"]/text()').get()
        product_item['image_url'] = response.xpath('//img[@id="defaultImage"]/@src').get()
        return product_item
