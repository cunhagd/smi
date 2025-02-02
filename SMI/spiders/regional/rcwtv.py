import scrapy

class RcwtvSpider(scrapy.Spider):
    name = "RCWTV"
    ID = 94
    allowed_domains = ["www.rcwtv.com.br"]
    start_urls = ["https://www.rcwtv.com.br/#google_vignette"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
