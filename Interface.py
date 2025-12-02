import tkinter as tk
from tkinter import ttk, messagebox
from Produto import*
from Service import*

# Assumindo que as classes Produto e ProdutoController estão definidas acima

class ProdutoView:
    def __init__(self, master, controller):
        self.master = master
        self.master.title("CRUD de Produtos (MVC - Tkinter)")
        self.controller = controller
        
        # Variáveis de controle dos campos de entrada
        self.nome_var = tk.StringVar()
        self.preco_var = tk.DoubleVar()
        self.quantidade_var = tk.IntVar()
        
        # ID do produto selecionado para Atualizar/Remover
        self.selected_id = None
        
        # --- Configuração da Janela (Layout) ---
        
        # Frame de Entradas (lado esquerdo)
        input_frame = ttk.LabelFrame(master, text=" Dados do Produto ")
        input_frame.pack(padx=10, pady=10, fill="x")

        # Campos de Entrada
        ttk.Label(input_frame, text="Nome:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(input_frame, textvariable=self.nome_var, width=30).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(input_frame, text="Preço:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(input_frame, textvariable=self.preco_var, width=30).grid(row=1, column=1, padx=5, pady=5)
        # Inicializa o Preço para evitar erro de entrada vazia
        self.preco_var.set(0.0) 

        ttk.Label(input_frame, text="Quantidade:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
        ttk.Entry(input_frame, textvariable=self.quantidade_var, width=30).grid(row=2, column=1, padx=5, pady=5)
        # Inicializa a Quantidade
        self.quantidade_var.set(0)

        # Frame de Botões
        button_frame = ttk.Frame(master)
        button_frame.pack(pady=5)
        
        ttk.Button(button_frame, text="Adicionar", command=self.adicionar_produto).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Listar", command=self.listar_produtos).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Atualizar", command=self.atualizar_produto).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Remover", command=self.remover_produto).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Limpar Campos", command=self.limpar_campos).pack(side="left", padx=5)

        # Frame da Tabela (Treeview)
        tree_frame = ttk.Frame(master)
        tree_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Nome", "Preco", "Quantidade"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nome", text="Nome")
        self.tree.heading("Preco", text="Preço")
        self.tree.heading("Quantidade", text="Qtd")
        
        # Configura as colunas
        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nome", width=200)
        self.tree.column("Preco", width=100, anchor="e")
        self.tree.column("Quantidade", width=80, anchor="center")

        self.tree.pack(fill="both", expand=True)
        
        # Adiciona um evento para selecionar na tabela e preencher os campos
        self.tree.bind('<<TreeviewSelect>>', self.selecionar_item)
        
        # Lista inicial de produtos
        self.listar_produtos()


    def limpar_campos(self):
        """Limpa as variáveis de controle e o ID selecionado."""
        self.nome_var.set("")
        self.preco_var.set(0.0)
        self.quantidade_var.set(0)
        self.selected_id = None

    def validar_campos(self):
        """Valida se os campos de Nome, Preço e Quantidade foram preenchidos corretamente."""
        nome = self.nome_var.get()
        try:
            preco = self.preco_var.get()
            quantidade = self.quantidade_var.get()
        except tk.TclError:
            messagebox.showerror("Erro", "Preço ou Quantidade inválidos.")
            return None
        
        if not nome:
            messagebox.showerror("Erro", "O campo Nome é obrigatório.")
            return None
        if preco <= 0:
             messagebox.showerror("Erro", "O preço deve ser maior que zero.")
             return None
        if quantidade < 0:
             messagebox.showerror("Erro", "A quantidade não pode ser negativa.")
             return None

        # Cria uma nova instância do Modelo com os dados da View
        return Produto(nome, preco, quantidade)

    def adicionar_produto(self):
        """Cria e adiciona um produto usando o Controller."""
        novo_produto = self.validar_campos()
        if novo_produto:
            # O Controller adiciona o produto
            self.controller.adicionar(novo_produto)
            messagebox.showinfo("Sucesso", f"Produto '{novo_produto.get_nome()}' adicionado.")
            self.limpar_campos()
            self.listar_produtos() # Atualiza a tabela

    def listar_produtos(self):
        """Busca os produtos no Controller e exibe na tabela."""
        
        # Limpa todos os itens da tabela
        for item in self.tree.get_children():
            self.tree.delete(item)
            
        # Pega a lista do Controller
        produtos = self.controller.listar()
        
        # Insere cada produto na tabela
        for produto in produtos:
            self.tree.insert("", "end", values=produto.to_tuple())
            
        # Caso não haja produtos, limpa o ID selecionado
        if not produtos:
            self.selected_id = None
        
    def selecionar_item(self, event):
        """Pega o produto selecionado na tabela e preenche os campos de entrada."""
        selected_item = self.tree.focus()
        if selected_item:
            # Pega os valores da linha selecionada
            values = self.tree.item(selected_item, 'values')
            
            # Os valores são strings, converte o ID para int para usar no Controller
            self.selected_id = int(values[0])
            
            # Preenche os campos de entrada
            self.nome_var.set(values[1])
            self.preco_var.set(float(values[2]))
            self.quantidade_var.set(int(values[3]))
        else:
            self.limpar_campos()

    def atualizar_produto(self):
        """Atualiza o produto selecionado usando o Controller."""
        if not self.selected_id:
            messagebox.showwarning("Aviso", "Selecione um produto na tabela para atualizar.")
            return

        # Cria um "produto" temporário para passar os novos dados
        produto_com_novos_dados = self.validar_campos()
        if produto_com_novos_dados:
            # O Controller atualiza o produto pelo ID
            if self.controller.atualizar(self.selected_id, produto_com_novos_dados):
                messagebox.showinfo("Sucesso", f"Produto ID: {self.selected_id} atualizado.")
                self.limpar_campos()
                self.listar_produtos() # Atualiza a tabela
            else:
                messagebox.showerror("Erro", "Produto não encontrado para atualização.")

    def remover_produto(self):
        """Remove o produto selecionado usando o Controller."""
        if not self.selected_id:
            messagebox.showwarning("Aviso", "Selecione um produto na tabela para remover.")
            return

        # Confirmação
        if messagebox.askyesno("Confirmar Remoção", f"Tem certeza que deseja remover o Produto ID: {self.selected_id}?"):
            # O Controller remove o produto pelo ID
            if self.controller.remover(self.selected_id):
                messagebox.showinfo("Sucesso", f"Produto ID: {self.selected_id} removido.")
                self.limpar_campos()
                self.listar_produtos() # Atualiza a tabela
            else:
                messagebox.showerror("Erro", "Produto não encontrado para remoção.")

# --- Execução da Aplicação ---
if __name__ == "__main__":
    root = tk.Tk()
    
    # Inicializa o Controller
    controller = ProdutoController()
    
    # Inicializa a View e passa o Controller
    app = ProdutoView(root, controller)
    
    root.mainloop()