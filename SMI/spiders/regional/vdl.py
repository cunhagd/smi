import scrapy

class VdlSpider(scrapy.Spider):
    name = "Portal VDL"
    ID = 101
    allowed_domains = ["portalvdl.com.br"]
    start_urls = ["https://portalvdl.com.br/?pl_eleicoes=false"]

    def parse(self, response):
        # Lógica de extração a ser definida depois
        pass
