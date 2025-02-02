import scrapy

class Alterosa_sulminasSpider(scrapy.Spider):
    name = "TV Alterosa - Sul de Minas"
    ID = 247
    allowed_domains = ["www.alterosa.com.br"]
    start_urls = ["https://www.alterosa.com.br/programas/alterosa-em-alerta-dv/"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
