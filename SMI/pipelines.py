# pipelines.py
import sqlite3
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
    Pipeline para salvar os dados extraídos no banco de dados SQLite.
    """
    def __init__(self):
        # Conectar ao banco de dados (ou criar se não existir)
        self.conn = sqlite3.connect("db/banco_smi.db")
        self.cursor = self.conn.cursor()
        # Criar tabela se ela ainda não existir
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS noticias (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
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
            self.cursor.execute("SELECT link FROM noticias WHERE link = ?", (link,))
            existing_link = self.cursor.fetchone()

            if existing_link:
                spider.logger.info(f"Notícia ignorada (link duplicado): {link}")
                return item  # Ignora a inserção se o link já existir

            # Insere os dados na tabela
            self.cursor.execute("""
                INSERT INTO noticias (
                    data, titulo, corpo, link, autor, abrangencia, pontos, obrigatorias, adicionais
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data, titulo, corpo, link, autor, abrangencia, pontos, palavras_obrigatorias, palavras_adicionais
            ))

            # Confirma a transação
            self.conn.commit()
        except sqlite3.IntegrityError as e:
            # Captura erros relacionados à violação da restrição UNIQUE
            spider.logger.error(f"Erro de integridade ao salvar no banco de dados: {e}")
        except Exception as e:
            spider.logger.error(f"Erro ao salvar no banco de dados: {e}")

        return item

    def close_spider(self, spider):
        """
        Fecha a conexão com o banco de dados quando o spider termina.
        """
        self.conn.close()