class ProdutoController:
    def __init__(self):
        # Armazena os produtos
        self._produtos = []

    def adicionar(self, produto):
        """Insere um novo produto na lista."""
        self._produtos.append(produto)

    def listar(self):
        """Retorna todos os produtos."""
        return self._produtos

    def buscar_por_id(self, id_produto):
        """Busca um produto pelo ID."""
        for produto in self._produtos:
            if produto.get_id() == id_produto:
                return produto
        return None

    def atualizar(self, id_produto, novo_produto):
        """Atualiza um produto existente (Copia atributos do novo_produto)."""
        produto_existente = self.buscar_por_id(id_produto)
        if produto_existente:
            produto_existente.set_nome(novo_produto.get_nome())
            produto_existente.set_preco(novo_produto.get_preco())
            produto_existente.set_quantidade(novo_produto.get_quantidade())
            return True
        return False

    def remover(self, id_produto):
        """Exclui um produto pelo ID."""
        produto_a_remover = self.buscar_por_id(id_produto)
        if produto_a_remover:
            self._produtos.remove(produto_a_remover)
            return True
        return False