import scrapy


class AldiProducts(scrapy.Spider):
    name = "shopaldi"
    start_urls = [
        'https://www.aldi.nl/producten/brood-bakkerij/dagvers-brood.html',
        
    ]

    def parse(self, response):
        for products in response.css('div.mod-article-tile__content'):
            yield {
                'description': products.css('meta.description::attr(content)').extract(),
                'name': products.css('span.mod-article-tile__title::text').get().replace('\n\t\t\t\t\t\t', ''),
                'price': products.css('span.price__wrapper::text').get().replace('\n\t', ''),

            
            }
        next_page = response.css('a.mod-breadcrumb__item').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)