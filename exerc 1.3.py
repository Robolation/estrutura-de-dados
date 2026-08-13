class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


Contat1 = Contato("Carlos Henrique", "(55) 9993-0668", "Carlosohenriquetiroteio@gmail.com")
Contat2 = Contato("Julia", "(55) 9442-2213", "julia.minaloca@hotmail.com")
Contat3 = Contato("Cassio", "(82) 3036-4467", "lucasmatakiwi@gmail.com")

agenda = [Contat1, Contat2, Contat3]


for contato in agenda:
    print("Nome: ", contato.nome)
    print("Telefone: ", contato.telefone)
    print("Email: ", contato.email)
    print()
