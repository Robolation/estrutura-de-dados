class Produto:
    def __init__(self, nome, preco, quantia, quantiatotal):
        self.nome = nome
        self.preco = preco
        self.quantia = quantia
        self.quantiatotal = quantiatotal
        
    
    def mostrar_info(self):
        print(self.nome)
        print(self.preco)
        print(self.quantia)
        print(self.quantiatotal)

    def  calctotal(self):
        self.calctotal = self.preco  +  self.quantia

pepino = Produto ("pepinos", "Preço-2R$ UNIDADE", "QUANTIA-15unidades","PREÇO TOTAL-30R$")
pepino.mostrar_info()
pepino.calctotal()

cebola = Produto ("cebolas", "Preço-1.50R$ UNIDADE", "QUANTIA-20unidades","PREÇO TOTAL-30R$")
cebola.mostrar_info()
cebola.calctotal()
