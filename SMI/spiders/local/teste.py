import scrapy
from scrapy.spiders import SitemapSpider
from datetime import datetime
from SMI.items import DB_PATH, buscar_urls, buscar_categorias, buscar_apelido, seletor_corpo, filtrar_keywords  # Importa as funções necessárias

class EmSpider(SitemapSpider):  # Classe da spider
    name = "Estado de Minas"  # Nome da spider

    def __init__(self, *args, **kwargs):
        super(EmSpider, self).__init__(*args, **kwargs)  # Inicializa a classe pai
        apelidos = buscar_apelido(self.name)  # Chama a função buscar_apelido para obter uma lista de apelidos
        if apelidos:
            self.sitemap_urls = buscar_urls(DB_PATH, apelidos[0])  # Busca as URLs do sitemap com base no apelido
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

        # Cria um dicionário com os dados da notícia
        news_data = {
            "url": response.url,  # URL da notícia
            "timestamp": current_timestamp  # Timestamp atual
        }

        # Extrai a data do timestamp gerado
        news_date = datetime.fromisoformat(news_data["timestamp"]).date()

        # Verifica se a data do timestamp é igual à data atual
        if news_date == today:
            self.logger.info(f"Notícia de hoje encontrada: {response.url}")

            # Busca o seletor CSS no banco de dados
            sel_corpo = seletor_corpo(DB_PATH, self.name)

            if not sel_corpo:
                self.log(f"Seletor CSS não encontrado para o portal '{self.name}'")
                return

            # Extrai os parágrafos usando o seletor obtido
            paragrafos = response.css(sel_corpo).getall()

            # Remove espaços extras e junta os parágrafos em um único texto
            corpo_completo = "\n".join([p.strip() for p in paragrafos if p.strip()])

            # Adiciona o corpo completo ao dicionário de dados da notícia
            news_data["corpo_completo"] = corpo_completo

            # Filtra a notícia com base nas palavras-chave
            palavras_encontradas = filtrar_keywords(DB_PATH, corpo_completo, debug=True)
            if not palavras_encontradas:
                self.log(f"Notícia ignorada (não atende às palavras-chave): {response.url}")
                return

            # Verifica se a notícia atende à regra de relevância
            tem_obrigatoria = len(palavras_encontradas["obrigatorias"]) > 0
            tem_adicional = len(palavras_encontradas["adicionais"]) > 0

            if not (tem_obrigatoria and tem_adicional):
                self.log(f"Notícia ignorada (não atende à regra de relevância): {response.url}")
                return

            # Adiciona as palavras-chave encontradas ao dicionário de dados da notícia
            news_data["palavras_obrigatorias_encontradas"] = palavras_encontradas["obrigatorias"]
            news_data["palavras_adicionais_encontradas"] = palavras_encontradas["adicionais"]

            # Log das palavras-chave encontradas
            self.log(f"Palavras-chave obrigatórias encontradas: {palavras_encontradas['obrigatorias']}")
            self.log(f"Palavras-chave adicionais encontradas: {palavras_encontradas['adicionais']}")

            # Retorna os dados da notícia
            yield news_data
        else:
            self.logger.info(f"Notícia ignorada (data: {news_date}): {response.url}")