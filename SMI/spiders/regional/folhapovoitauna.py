import scrapy

class FolhapovoitaunaSpider(scrapy.Spider):
    name = "Folha do Povo Itaúna"
    ID = 177
    allowed_domains = ["www.folhapovoitauna.com.br"]
    start_urls = ["https://www.folhapovoitauna.com.br/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
