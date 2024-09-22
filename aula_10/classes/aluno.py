class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros_alugados = []

    def alugar_livro(self, livro, biblioteca):
        if biblioteca.alugar_livro(livro, self):
            self.livros_alugados.append(livro)
            print(f"{self.nome} alugou o livro {livro}.")
        else:
            print(f"Livro {livro} não está disponível para aluguel.")
    
    def devolver_livro(self, livro, biblioteca):
        if livro in self.livros_alugados:
            biblioteca.devolver_livro(livro)
            self.livros_alugados.remove(livro)
            print(f"{self.nome} devolveu o livro {livro}.")
        else:
            print(f"{self.nome} não possui o livro {livro} para devolver.")

    def __str__(self):
        return f"Aluno: {self.nome} (Matrícula: {self.matricula})"