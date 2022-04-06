from api.modelos import banco_de_dados as db

class Manipulador():
    """Manipula objetos com funções genéricas
    """
    def localizar_objeto(self, modelo, id):
        """Localiza um objeto no banco de dados à partir do id

        Argumentos:
            modelo (classe): Classe modelo (ORM SQLAlchemy) para executar querys
            id (Iinteiro): id do objeto salvo no banco de dados

        Retornos:
            objeto: objeto encontrado no banco de dados
            None: None
        """
        objeto = modelo.query.get(id)
        if objeto:
            return objeto
        return None
    
    def salvar_objeto(self, objeto):
        """Salva objeto no banco de dados

        Argumento:
            objeto (objeto): Instancia de uma classe modelo para salvar no banco de dados
        """
        db.session.add(objeto)
        db.session.commit()
    
    def deletar_objeto(self, objeto):
        """Deleta objeto do banco de dados

        Argumento:
            objeto (objeto): Instancia de uma classe modelo para ser deletada do banco de dados
        """
        db.session.delete(objeto)
        db.session.commit()
    
    def verificar_dados_vazios(self, objeto, dados):
        """Verifica se há algum argumento vazio em dados

        Argumentos:
            objeto (objeto): Instancia de uma classe modelo para obter dados já cadastrados
            dados (dicionario): Dicionario com os argumentos enviados para o back pelo metodo PATCH

        Retorno:
            dicionario: Dicionario sem argumentos vazios
        """
        objeto_json = objeto.json()
        for chave, valor in dados.items():
            if not valor:
                dados[chave] = objeto_json[chave]
        return dados