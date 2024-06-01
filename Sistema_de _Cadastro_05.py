class Estudante:
    def __init__(self, nome, idade, matricula):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.curso = self.definir_curso(matricula)

    def definir_curso(self, matricula):
        cursos = {'1': 'Engenharia', '2': 'Matemática', '3': 'Computação'}
        return cursos.get(matricula[-1], 'Curso Desconhecido')

class No:
    def __init__(self, estudante):
        self.esquerda = None
        self.direita = None
        self.estudante = estudante

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, estudante):
        if not self.raiz:
            self.raiz = No(estudante)
        else:
            self._inserir(estudante, self.raiz)
        print(f"Estudante adicionado com sucesso no curso de {estudante.curso}!")

    def _inserir(self, estudante, no_atual):
        if estudante.matricula < no_atual.estudante.matricula:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(estudante)
            else:
                self._inserir(estudante, no_atual.esquerda)
        else:
            if no_atual.direita is None:
                no_atual.direita = No(estudante)
            else:
                self._inserir(estudante, no_atual.direita)

    def remover(self, matricula):
        if self.buscar(matricula, self.raiz):
            self.raiz = self._remover(matricula, self.raiz)
            print("Estudante removido com sucesso!")
        else:
            print("Erro: Matrícula não encontrada.")

    def _remover(self, matricula, no):
        if no is None:
            return no
        if matricula < no.estudante.matricula:
            no.esquerda = self._remover(matricula, no.esquerda)
        elif matricula > no.estudante.matricula:
            no.direita = self._remover(matricula, no.direita)
        else:
            if no.esquerda is None:
                temp = no.direita
                no = None
                return temp
            elif no.direita is None:
                temp = no.esquerda
                no = None
                return temp
            temp = self._min_valor_no(no.direita)
            no.estudante = temp.estudante
            no.direita = self._remover(temp.estudante.matricula, no.direita)
        return no

    def _min_valor_no(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def buscar(self, matricula, no):
        if no is None:
            return False
        if matricula == no.estudante.matricula:
            return True
        elif matricula < no.estudante.matricula:
            return self.buscar(matricula, no.esquerda)
        else:
            return self.buscar(matricula, no.direita)

    def mostrar_matriculas(self, no=None):
        if no is None:
            no = self.raiz
        self._mostrar_matriculas(no)

    def _mostrar_matriculas(self, no):
        if no is not None:
            self._mostrar_matriculas(no.esquerda)
            print(f"Nome: {no.estudante.nome}, Matrícula: {no.estudante.matricula}")
            self._mostrar_matriculas(no.direita)

# Funções auxiliares para interação com o usuário
def cadastrar_estudante(arvore):
    nome = input("Digite o nome do estudante: ")
    idade = input("Digite a idade do estudante: ")
    matricula = input("Digite a matrícula do estudante (9 caracteres): ")
    
    if nome and idade and len(matricula) == 9:
        estudante = Estudante(nome, idade, matricula)
        arvore.inserir(estudante)
    else:
        print("Erro: Por favor, preencha todos os campos corretamente.")

def remover_estudante(arvore):
    matricula = input("Digite a matrícula do estudante a ser removido (9 caracteres): ")
    if len(matricula) == 9:
        arvore.remover(matricula)
    else:
        print("Erro: A matrícula deve ter exatamente 9 caracteres.")

def mostrar_matriculas(arvore):
    print("Informações dos estudantes cadastrados:")
    arvore.mostrar_matriculas()


if __name__ == "__main__":
    arvore_cadastro = ArvoreBinaria()
    while True:
        acao = input("Escolha uma ação - adicionar, remover, mostrar ou sair: ").lower()
        if acao == 'adicionar':
            cadastrar_estudante(arvore_cadastro)
        elif acao == 'remover':
            remover_estudante(arvore_cadastro)
        elif acao == 'mostrar':
            mostrar_matriculas(arvore_cadastro)
        elif acao == 'sair':
            break
        else:
            print("Ação inválida.")
