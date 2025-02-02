import scrapy

class FolhadopovoSpider(scrapy.Spider):
    name = "Folha do Povo Itatiaiuçu"
    ID = 176
    allowed_domains = ["www.folhapovoitatiaiucu.com"]
    start_urls = ["https://www.folhapovoitatiaiucu.com/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
