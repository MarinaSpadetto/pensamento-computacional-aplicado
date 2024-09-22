from classes.aluno import Aluno
from classes.biblioteca import Biblioteca
from classes.livro import Livro

def main():
    # Criando a biblioteca
    biblioteca = Biblioteca()

    # Adicionando livros
    livro1 = Livro("Python para Iniciantes", "João Silva")
    livro2 = Livro("Algoritmos e Estruturas de Dados", "Maria Souza")
    livro3 = Livro("Inteligência Artificial", "Carlos Costa")

    biblioteca.adicionar_livro(livro1)
    biblioteca.adicionar_livro(livro2)
    biblioteca.adicionar_livro(livro3)

    # Criando alunos
    aluno1 = Aluno("Pedro", "A001")
    aluno2 = Aluno("Ana", "A002")

    # Listando livros disponíveis
    biblioteca.listar_livros_disponiveis()

    # Aluno 1 aluga um livro
    aluno1.alugar_livro(livro1, biblioteca)

    # Listando livros disponíveis após o aluguel
    biblioteca.listar_livros_disponiveis()

    # Aluno 2 tenta alugar o mesmo livro
    aluno2.alugar_livro(livro1, biblioteca)

    # Aluno 1 devolve o livro
    aluno1.devolver_livro(livro1, biblioteca)

    # Listando livros disponíveis após a devolução
    biblioteca.listar_livros_disponiveis()


if __name__ == '__main__':
    main()