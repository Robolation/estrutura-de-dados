class Livro:

    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas

    def tipo_livro(self):
        if self.numero_paginas <= 100:
            self.tipo = "Curto"
        else:
            self.tipo = "Longo"

    def mostrar_informacoes(self):
        print("Título: ", self.titulo)
        print("Autor: ", self.autor)
        print("Número de páginas: ", self.numero_paginas)
        print("Tipo de livro: ", self.tipo)
        print()


livro1 = Livro("COLETANEA DE CONTOS MACABROS", "HP.LOVECRAFT", 500)
livro1.tipo_livro()
livro1.mostrar_informacoes()

livro2 = Livro("A COISA", "stephen strange", 90)
livro2.tipo_livro()
livro2.mostrar_informacoes()
