import scrapy

class InfomoneySpider(scrapy.Spider):
    name = "InfoMoney"
    ID = 58
    allowed_domains = ["www.infomoney.com.br"]
    start_urls = ["https://www.infomoney.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
