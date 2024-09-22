class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro {livro} adicionado à biblioteca.")

    def alugar_livro(self, livro, aluno):
        if livro.disponivel:
            livro.disponivel = False
            return True
        else:
            return False

    def devolver_livro(self, livro):
        livro.disponivel = True

    def listar_livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.livros if livro.disponivel]
        if livros_disponiveis:
            print("Livros disponíveis:")
            for livro in livros_disponiveis:
                print(f"- {livro}")
        else:
            print("Nenhum livro disponível no momento.")