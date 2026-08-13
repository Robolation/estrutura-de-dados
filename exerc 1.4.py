class Produto:

    def __init__(self, nome, preco, qdt_estoque):
        self.nome = nome
        self.preco = preco
        self.quantidade_estoque = qdt_estoque

    def atualizar_estoque(self, valor):
        self.quantidade_estoque += valor

    def exibir_dados(self):
        print("Produto:", self.nome, "Preço: R$", self.preco, "Estoque:", self.quantidade_estoque)


#antes
p1 = Produto("Playstation 5", 3500.00, 10)
p2 = Produto("Controle", 80.00, 25)

p1.exibir_dados()
p2.exibir_dados()


#depois
p1.atualizar_estoque(5)
p2.atualizar_estoque(15)

p1.exibir_dados()
p2.exibir_dados()
