class Produto:
    # Gerador de IDs (para simular um banco de dados)
    _proximo_id = 1

    def __init__(self, nome, preco, quantidade):
        # Atributos privados
        self._id = Produto._proximo_id
        Produto._proximo_id += 1
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    # Getters
    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco

    def get_quantidade(self):
        return self._quantidade

    # Setters (excluindo o ID)
    def set_nome(self, novo_nome):
        self._nome = novo_nome

    def set_preco(self, novo_preco):
        self._preco = novo_preco

    def set_quantidade(self, nova_quantidade):
        self._quantidade = nova_quantidade

    # Método toString (ou __repr__ em Python para representação)
    def __repr__(self):
        return f"Produto(ID: {self._id}, Nome: {self._nome}, Preço: {self._preco:.2f}, Qtd: {self._quantidade})"

    # Método auxiliar para retornar como tupla, útil para a tabela/listbox
    def to_tuple(self):
        return (self._id, self._nome, self._preco, self._quantidade)