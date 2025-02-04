import scrapy
from scrapy.spiders import SitemapSpider
from datetime import datetime
from SMI.items import buscar_categorias, buscar_urls # Importa a função para buscar categorias

class EmSpider(SitemapSpider):
    name = "Estado de Minas_original"
    sitemap_urls = ["https://www.em.com.br/sitemap.xml"]

    def __init__(self, *args, **kwargs):
        super(EmSpider, self).__init__(*args, **kwargs)
        # Carrega as categorias indesejadas no banco de dados durante a inicialização
        self.categorias_indesejadas = set(buscar_categorias())  # Usamos um conjunto para otimizar a busca

    def parse(self, response):
        # Gera o timestamp atual
        current_timestamp = datetime.now().isoformat()
        # Obtém a data atual (apenas a parte da data, sem hora)
        today = datetime.now().date()

        # Verifica se a URL contém alguma categoria existente
        if any(categoria in response.url for categoria in self.categorias_indesejadas):
            self.logger.info(f"URL ignorada (categoria indesejada): {response.url}")
            return  # Ignora a URL se a categoria estiver cadast    rada

        # Cria um dicionário com os dados da notícia
        news_data = {
            "url": response.url,
            "timestamp": current_timestamp
        }

        # Extrai a data do timestamp gerado
        news_date = datetime.fromisoformat(news_data["timestamp"]).date()

        # Verifica se a data do timestamp é igual à data atual
        if news_date == today:
            self.logger.info(f"Notícia de hoje encontrada: {response.url}")
            yield news_data
        else:
            self.logger.info(f"Notícia ignorada (data: {news_date}): {response.url}")
        

        # Extrair todos os parágrafos da notícia
        paragrafos = response.xpath('//*[@id="edm-general"]/main/div[4]/div[2]/p//text()').getall()

        # Limpar os parágrafos (remover espaços extras)
        paragrafos_limpos = [p.strip() for p in paragrafos if p.strip()]

        # Concatenar os parágrafos em um único texto, com quebras de linha entre eles
        corpo = "\n\n".join(paragrafos_limpos)

        # Salvar os dados
        yield corpo
            