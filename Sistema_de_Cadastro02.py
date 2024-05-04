import tkinter as tk
from tkinter import messagebox

class No:
    def __init__(self, dados):
        self.dados = dados
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar(self, dados):
        if not self.cabeca:
            self.cabeca = No(dados)
        else:
            atual = self.cabeca
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = No(dados)

class Fila:
    def __init__(self):
        self.itens = ListaEncadeada()

    def enfileirar(self, item):
        self.itens.adicionar(item)

    def desenfileirar(self):
        if self.itens.cabeca:
            dados = self.itens.cabeca.dados
            self.itens.cabeca = self.itens.cabeca.proximo
            return dados

class Estudante:
    def __init__(self, nome, idade, curso, matricula):
        self.nome = nome
        self.idade = idade
        self.curso = curso
        self.matricula = matricula

class Aplicacao:
    def __init__(self, janela):
        self.frame = tk.Frame(janela)
        self.frame.pack()

        self.rotulo_nome = tk.Label(self.frame, text="Nome:")
        self.rotulo_nome.pack(side=tk.LEFT)
        self.entrada_nome = tk.Entry(self.frame)
        self.entrada_nome.pack(side=tk.LEFT)

        self.rotulo_idade = tk.Label(self.frame, text="Idade:")
        self.rotulo_idade.pack(side=tk.LEFT)
        self.entrada_idade = tk.Entry(self.frame)
        self.entrada_idade.pack(side=tk.LEFT)

        self.rotulo_curso = tk.Label(self.frame, text="Curso:")
        self.rotulo_curso.pack(side=tk.LEFT)
        self.entrada_curso = tk.Entry(self.frame)
        self.entrada_curso.pack(side=tk.LEFT)

        self.rotulo_matricula = tk.Label(self.frame, text="Matrícula:")
        self.rotulo_matricula.pack(side=tk.LEFT)
        self.entrada_matricula = tk.Entry(self.frame)
        self.entrada_matricula.pack(side=tk.LEFT)

        self.botao = tk.Button(self.frame, text="Cadastrar", command=self.cadastrar)
        self.botao.pack(side=tk.LEFT)

        self.fila_cadastro = Fila()

    def cadastrar(self):
        nome = self.entrada_nome.get()
        idade = self.entrada_idade.get()
        curso = self.entrada_curso.get()
        matricula = self.entrada_matricula.get()
        if nome and idade and curso and len(matricula) == 9:
            estudante = Estudante(nome, idade, curso, matricula)
            self.fila_cadastro.enfileirar(estudante)
            messagebox.showinfo("Sucesso", "Estudante cadastrado com sucesso!")
        elif len(matricula) != 9:
            messagebox.showerror("Erro", "A matrícula deve ter exatamente 9 caracteres.")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

janela = tk.Tk()
app = Aplicacao(janela)
janela.mainloop()
