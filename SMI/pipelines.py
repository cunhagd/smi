import psycopg2
from datetime import datetime

class FormatTimestampPipeline:
    """
    Pipeline para formatar o campo 'timestamp' de "AAAA-MM-DDTHH:MM:SS.ssssss" para "DD-MM-AAAA".
    """
    def process_item(self, item, spider):
        # Verifica se o campo 'timestamp' existe no item
        if "timestamp" in item:
            try:
                # Converte o timestamp para o formato desejado
                original_timestamp = item["timestamp"]
                formatted_date = datetime.fromisoformat(original_timestamp).strftime("%d-%m-%Y")
                item["timestamp"] = formatted_date
            except Exception as e:
                spider.logger.error(f"Erro ao formatar timestamp: {e}")
        return item


class SaveToDatabasePipeline:
    """
    Pipeline para salvar os dados extraídos no banco de dados PostgreSQL.
    """
    def __init__(self):
        # Configurações do banco de dados PostgreSQL
        self.DB_HOST = "ethereally-engrossed-springbok.data-1.use1.tembo.io"
        self.DB_PORT = 5432
        self.DB_NAME = "postgres"
        self.DB_USER = "postgres"
        self.DB_PASSWORD = "TEit6gBw1SCPAQWY"

        # Conectar ao banco de dados
        try:
            self.conn = psycopg2.connect(
                host=self.DB_HOST,
                port=self.DB_PORT,
                database=self.DB_NAME,
                user=self.DB_USER,
                password=self.DB_PASSWORD
            )
            self.cursor = self.conn.cursor()

            # Criar tabela se ela ainda não existir
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS noticias (
                    id SERIAL PRIMARY KEY,  -- Campo autoincrementável
                    data TEXT,
                    titulo TEXT,
                    corpo TEXT,
                    link TEXT UNIQUE,  -- Adiciona restrição UNIQUE ao campo 'link'
                    autor TEXT,
                    abrangencia TEXT,
                    pontos INTEGER,
                    obrigatorias TEXT,
                    adicionais TEXT
                )
            """)
            self.conn.commit()
        except Exception as e:
            print(f"Erro ao conectar ou criar tabela no banco de dados: {e}")

    def process_item(self, item, spider):
        """
        Insere os dados do item no banco de dados, garantindo que não haja links duplicados.
        """
        try:
            # Extrai os valores do item
            data = item.get("timestamp", "")
            titulo = item.get("title", "")
            corpo = item.get("corpo_completo", "")
            link = item.get("url", "")
            autor = item.get("autor", "")
            abrangencia = item.get("abrangencia", "")
            pontos = item.get("pontos", 0)
            palavras_obrigatorias = ",".join(item.get("palavras_obrigatorias_encontradas", []))
            palavras_adicionais = ",".join(item.get("palavras_adicionais_encontradas", []))

            # Verifica se o link já existe no banco de dados
            self.cursor.execute("SELECT link FROM noticias WHERE link = %s", (link,))
            existing_link = self.cursor.fetchone()
            if existing_link:
                spider.logger.info(f"Notícia ignorada (link duplicado): {link}")
                return item  # Ignora a inserção se o link já existir

            # Insere os dados na tabela
            self.cursor.execute("""
                INSERT INTO noticias (
                    data, titulo, corpo, link, autor, abrangencia, pontos, obrigatorias, adicionais
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING id
            """, (
                data, titulo, corpo, link, autor, abrangencia, pontos, palavras_obrigatorias, palavras_adicionais
            ))

            # Confirma a transação
            self.conn.commit()

        except psycopg2.IntegrityError as e:
            # Captura erros relacionados à violação da restrição UNIQUE
            self.conn.rollback()  # Desfaz a transação em caso de erro
            spider.logger.error(f"Erro de integridade ao salvar no banco de dados: {e}")
        except Exception as e:
            self.conn.rollback()  # Desfaz a transação em caso de erro
            spider.logger.error(f"Erro ao salvar no banco de dados: {e}")

        return item

    def close_spider(self, spider):
        """
        Fecha a conexão com o banco de dados quando o spider termina.
        """
        if self.conn:
            self.conn.close()