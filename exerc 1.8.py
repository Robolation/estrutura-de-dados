class Aluno:

    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        calculo_media = sum(self.notas) / len(self.notas)
        return calculo_media


aluno1 = Aluno("Luciano Hulk", [6.7, 9.0, 5.0])
aluno2 = Aluno("Bruce Banner", [6.0, 10.0, 4.0])
aluno3 = Aluno("Tony Stark", [9.0, 2.0, 9.5])

turma = [aluno1, aluno2, aluno3]


for aluno in turma:
    media = aluno.calcular_media()
    print(f"Aluno(a): {aluno.nome} | Média: {media:.2f}")
