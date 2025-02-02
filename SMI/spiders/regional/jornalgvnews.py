import scrapy

class JornalgvnewsSpider(scrapy.Spider):
    name = "Jornal GV News"
    ID = 138
    allowed_domains = ["www.jornalgvnews.com.br"]
    start_urls = ["https://www.jornalgvnews.com.br/principal"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
