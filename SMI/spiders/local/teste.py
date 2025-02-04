import scrapy
from scrapy.spiders import SitemapSpider
from datetime import datetime
from SMI.items import DB_PATH, buscar_urls, buscar_categorias, buscar_apelido

class EmSpider(SitemapSpider):  # Classe da spider
    name = "Estado de Minas_22"  # Nome da spider

    def __init__(self, *args, **kwargs):
        super(EmSpider, self).__init__(*args, **kwargs)  # Inicializa a classe pai
        apelidos = buscar_apelido(self.name)  # Chama a função buscar_apelido para obter uma lista de apelidos
        if apelidos:
            self.sitemap_urls = buscar_urls(DB_PATH, apelidos[0])
        else:
            print("Nenhum apelido encontrado no banco de dados.")
            self.sitemap_urls = []
        # Define as categorias indesejadas
        self.categorias_indesejadas = set(buscar_categorias())

    def parse(self, response):  # Função para processar a resposta de uma requisição
        current_timestamp = datetime.now().isoformat()  # Gera o timestamp atual
        today = datetime.now().date()  # Obtém a data atual (apenas a parte da data, sem hora)

        # Verifica se a URL contém alguma categoria indesejada
        if any(categoria in response.url for categoria in self.categorias_indesejadas):
            self.logger.info(f"URL ignorada (categoria indesejada): {response.url}")
            return  # Ignora a URL se a categoria estiver cadastrada

        news_data = {  # Cria um dicionário com os dados da notícia
            "url": response.url,  # URL da notícia
            "timestamp": current_timestamp  # Timestamp atual
        }

        news_date = datetime.fromisoformat(news_data["timestamp"]).date()  # Extrai a data do timestamp gerado
        if news_date == today:  # Verifica se a data do timestamp é igual à data atual
            self.logger.info(f"Notícia de hoje encontrada: {response.url}")  # Log da notícia encontrada

            # Solicita o download da página da notícia para extrair o corpo
            yield scrapy.Request(
                url=response.url,
                callback=self.parse_noticia,
                meta={"news_data": news_data}  # Passa os dados atuais para o próximo callback
            )
        else:  # Se a data do timestamp não for igual à data atual
            self.logger.info(f"Notícia ignorada (data: {news_date}): {response.url}")  # Log da notícia ignorada

    def parse_noticia(self, response):
        # Recupera os dados passados via meta
        news_data = response.meta["news_data"]

        # Extrair todos os parágrafos da notícia
        paragrafos = response.xpath('//*[@id="edm-general"]/main/div[4]/div[2]/p//text()').getall()

        # Limpar os parágrafos (remover espaços extras)
        paragrafos_limpos = [p.strip() for p in paragrafos if p.strip()]

        # Concatenar os parágrafos em um único texto, com quebras de linha entre eles
        corpo = "\n\n".join(paragrafos_limpos)

        # Adicionar o corpo ao dicionário de dados da notícia
        news_data["corpo"] = corpo

        # Retornar os dados completos
        yield news_data