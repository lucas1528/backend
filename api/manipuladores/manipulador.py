from api.modelos import banco_de_dados as db

class Manipulador():
    def localizar_objeto(self, modelo, id):
            objeto = modelo.query.get(id)
            if objeto:
                return objeto
            return None
    
    def salvar_objeto(self, objeto):
        db.session.add(objeto)
        db.session.commit()
    
    def deletar_objeto(self, objeto):
        db.session.delete(objeto)
        db.session.commit()
    
    def verificar_dados_vazios(self, objeto, dados):
        objeto_json = objeto.json()
        for chave, valor in dados.items():
            if not valor:
                dados[chave] = objeto_json[chave]
        return dados