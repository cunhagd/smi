import scrapy
from SMI.items import seletor_corpo  # Importa a função seletor_corpo

class EstadoDeMinasSpider(scrapy.Spider):
    name = "Estado de Minas"
    start_urls = [
        "https://www.em.com.br/gerais/2025/02/7052556-mg-idoso-e-filho-sao-esfaqueados-dentro-de-casa-durante-jogo-de-truco.html"
    ]

    def parse(self, response):
        # Caminho para o banco de dados SQLite
        db_path = r"db\banco_smi.db"
        
        # Busca o seletor CSS no banco de dados
        sel_corpo = seletor_corpo(db_path, self.name)
        
        if not sel_corpo:
            self.log(f"Seletor CSS não encontrado para o portal '{self.name}'")
            return
        
        # Extrai os parágrafos usando o seletor obtido
        paragrafos = response.css(sel_corpo).getall()
        
        # Remove espaços extras e junta os parágrafos em um único texto
        corpo_completo = "\n".join([p.strip() for p in paragrafos if p.strip()])
        
        # Imprime o resultado no log
        self.log(f"Corpo completo extraído:\n{corpo_completo}")
        
        # Retorna os dados extraídos
        yield {
            "url": response.url,
            "corpo_completo": corpo_completo
        }