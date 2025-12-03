# CRUD
# CRUD de Produtos

Um sistema simples de **CRUD (Create, Read, Update, Delete)** para gerenciamento de produtos, implementado em Python utilizando o padrão arquitetural **Model-View-Controller (MVC)** e a biblioteca de interface gráfica **Tkinter**.

## Requisitos 💻 

* Python 3.x

O sistema utiliza apenas bibliotecas padrão do Python (`tkinter`).

## Estrutura do Projeto ⚙️

O projeto é dividido em três arquivos principais, seguindo o padrão MVC:

1.  **`Produto.py` (Model):** Define a classe `Produto` e a lógica de autogeração de ID.
2.  **`Service.py` (Controller):** Define a classe `ProdutoController`, que gerencia a coleção de produtos e implementa a lógica de negócios (CRUD).
3.  **`Interface.py` (View):** Define a classe `ProdutoView`, que cria a interface gráfica (`Tkinter`) e lida com a interação do usuário.

## Como Executar ✅

1.  Certifique-se de que os três arquivos (`Produto.py`, `Service.py`, `Interface.py`) estão no mesmo diretório.
2.  Execute o arquivo principal `Interface.py` 

## Funcionalidades 📄
O sistema permite as seguintes operações através da interface gráfica:

**CREATE** | **Adicionar** : Insere um novo produto com Nome, Preço e Quantidade. Realiza validação de campos;

**READ** | **Listar** : Exibe todos os produtos cadastrados na tabela (`Treeview`). Executado automaticamente no início;

**UPDATE** | **Atualizar** : Altera os dados do produto previamente selecionado na tabela;

**DELETE** | **Remover** : Remove o produto previamente selecionado na tabela (requer confirmação); 

**Seleção** | **Clique na Tabela** : Preenche os campos de entrada com os dados do produto selecionado para edição ou remoção; 

**Limpar** | **Limpar Campos** : Zera os campos de entrada e desfaz a seleção atual.

## Observações Importantes ⚠️

* **Persistência:** O sistema armazena os dados **apenas na memória RAM** (na lista `self._produtos` do Controller). Ao fechar a aplicação, todos os dados cadastrados serão perdidos. 
* **MVC:** O sistema adere ao princípio MVC, garantindo que a interface (`ProdutoView`) não manipule diretamente os dados, mas sim através do controlador (`ProdutoController`).
