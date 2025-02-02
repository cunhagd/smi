import scrapy

class FolhasabaraSpider(scrapy.Spider):
    name = "Folha de Sabará"
    ID = 182
    allowed_domains = ["folhadesabara.com.br"]
    start_urls = ["https://folhadesabara.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
