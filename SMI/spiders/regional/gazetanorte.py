import scrapy

class GazetanorteSpider(scrapy.Spider):
    name = "Gazeta Norte Mineira"
    ID = 168
    allowed_domains = ["gazetanm.com.br"]
    start_urls = ["https://gazetanm.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
