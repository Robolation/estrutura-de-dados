class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo == "Gerente":
            bonus = self.salario * (10 / 100)
            total_bonus = self.salario + bonus
            self.bonus = total_bonus
        else:
            bonus = self.salario * (5 / 100)
            total_bonus = self.salario + bonus
            self.bonus = total_bonus

    def mostrar_informacoes(self):
        print("Nome: ", self.nome)
        print("Salário: R$", self.salario)
        print("Cargo: ", self.cargo)
        print("Bonus: R$", self.bonus)


funcionario1 = Funcionario("CHARLIE KIRK", 5000.00, "Gerente")
funcionario1.calcular_bonus()
funcionario1.mostrar_informacoes()

funcionario2 = Funcionario("Jailson silva", 1000.00, "Analista de Dados")
funcionario2.calcular_bonus()
funcionario2.mostrar_informacoes()
