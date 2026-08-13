class Aluno:
    def __init__(self, nome, idade, nota1, nota2):
        self.nome = nome
        self.idade = idade
        self.nota1 = nota1
        self.nota2 = nota2

    def calcular_media(self):
        media = (self.nota1 + self.nota2) / 2
        self.media = media

    def verif_aprovacao(self):
        if self.media >= 7:
            self.aprovacao = "Aprovado"
        else:
            self.aprovacao = "Reprovado"

    def mostra_info(self):
        print("Nome: ", self.nome)
        print("Idade: ", self.idade)
        print("Média: ", self.media)
        print("Situação: ", self.aprovacao)


aluno1 = Aluno("jeffrey silveire", 19, 8.5, 7.0)
aluno1.calcular_media()
aluno1.verif_aprovacao()
aluno1.mostra_info()


aluno2 = Aluno("Marcos gomes", 20, 6.0, 5.5)
aluno2.calcular_media()
aluno2.verif_aprovacao()
aluno2.mostra_info()
