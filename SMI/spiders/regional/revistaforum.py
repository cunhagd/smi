import scrapy

class RevistaforumSpider(scrapy.Spider):
    name = "Revista Forum"
    ID = 87
    allowed_domains = ["revistaforum.com.br"]
    start_urls = ["https://revistaforum.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
