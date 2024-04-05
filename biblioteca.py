class Pessoas:
        def __init__(self, nome, cpf, endereco, telefone, email):
            self.__nome = nome
            self.__cpf = cpf
            self.__end = endereco
            self.__tel = telefone
            self.__email = email

        def get_nome(self):
            return self.__nome

        def set_nome(self, novo_nome):
            self.__nome = novo_nome

        def exibir(self):
            return f"Nome: {self.__nome}, CPF: {self.__cpf}, Endereço: {self.__end}, Telefone: {self.__tel}, E-mail: {self.__email}"


class Funcionario(Pessoas):
    def __init__(self, nome, cpf, endereco, telefone, email, salario):
        super().__init__(nome, cpf, endereco, telefone, email)
        self.__salario = salario
        self.__contratado = True

    def contratar(self):
        if not self.__contratado:
            self.__contratado = True
            return f"{super().get_nome()} já está ativo."
        else:
            return f"{super().get_nome()} está contratado."

    def demitir(self):
        if self.__contratado:
            self.__contratado = False
            return f"{self.get_nome()} foi demitido."
        else:
            return f"{self.get_nome()} já está demitido."

    def get_salario(self):
        return self.__salario

    def set_salario(self, novo_salario):
        self.__salario = novo_salario

class Cliente(Pessoas):
    def _init_(self, nome, cpf, endereco, telefone, email):
        super()._init_(nome, cpf, endereco, telefone, email)

    def exibir(self):
        return super().exibir()
class Obra:
    def __init__(self, nome, isbn, editora, edicao, estoque):
        self.nome = nome
        self.edicao = edicao
        self.editora = editora
        self.isbn = isbn
        self.estoque = estoque


class Livro(Obra):
    def __init__(self, nome, isbn, autor, editora, edicao, data, estoque):
        super().__init__(nome, isbn, editora, edicao, estoque)
        self.autor = autor
        self.data = data

    def emprestimo(self, data_emprestimo):
        if self.estoque > 0:
            self.estoque -= 1
            print(f"Livro '{self.nome}' emprestado em {data_emprestimo}. Estoque restante: {self.estoque}")
        else:
            print(f"Não há estoque disponível para o livro '{self.nome}'.")

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"ISBN: {self.isbn}")
        print(f"Autor: {self.autor}")
        print(f"Editora: {self.editora}")
        print(f"Edição: {self.edicao}")
        print(f"Ano: {self.data}")
        print(f"Estoque: {self.estoque}")

    def Devolucao(self, estado, avaliacao):
        if estado <= 2:
            self.estoque -= 1
            print(
                f"O Livro'{self.nome}' foi devolvido em mau estado. Estoque atual: {self.estoque}. Multa de R$30 aplicada.")
        else:
            self.estoque += 1
            print(f"O Livro '{self.nome}' foi devolvido em bom estado. Estoque atual: {self.estoque}.")

        print(f"Avaliação do Livro '{self.nome}': {avaliacao}/10")
livros_dados = [
    ["Dom Quixote", "1", "Miguel de Cervantes", "Editorial Clássicos", "1ª edição", 1605, 3],
    ["1984", "2", "George Orwell", "Penguin Books", "1ª edição", 1949, 6],
    ["Orgulho e Preconceito", "3", "Jane Austen", "Penguin Classics", "1ª edição", 1813, 2],
    ["Cem Anos de Solidão", "4", "Gabriel García Márquez", "HarperCollins", "1ª edição", 1967, 1],
    ["Harry Potter e a Pedra Filosofal", "5", "J.K. Rowling", "Bloomsbury Publishing", "1ª edição", 1997, 9],
    ["O Senhor dos Anéis: A Sociedade do Anel", "6", "J.R.R. Tolkien", "Houghton Mifflin", "1ª edição", 1954, 8],
    ["Crime e Castigo", "7", "Fiódor Dostoiévski", "Editora 34", "1ª edição", 1866, 5],
    ["A Revolução dos Bichos", "8", "George Orwell", "Companhia das Letras", "1ª edição", 1945, 15],
    ["O Pequeno Príncipe", "9", "Antoine de Saint-Exupéry", "Agir", "1ª edição", 1943, 25],
    ["O Apanhador no Campo de Centeio", "10", "J.D. Salinger", "Little, Brown and Company", "1ª edição", 1951, 11]
]

livros = []
for livro_dados in livros_dados:
    livro = Livro(*livro_dados)
    livros.append(livro)
def cadastrar_novo_livro(lista_livros):
    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite o nome da editora: ")
    edicao = input("Digite a edição do livro: ")
    isbn = input("Digite o ISBN do livro: ")
    estoque = int(input("Digite a quantidade em estoque do livro: "))

    novo_livro = Livro(nome, isbn, editora, edicao,autor,None,estoque)
    lista_livros.append(novo_livro)
    print("Livro Cadastrado com Sucesso!")

    ultimo_livro = livros[-1]
    print("\nNovo livro cadastrado:")
    print("Nome:", ultimo_livro.nome)
    print("Autor:", ultimo_livro.autor)
    print("Estoque:", ultimo_livro.estoque)
    print("Total de livros na lista:", len(livros))

class Revista(Obra):
    def __init__(self, nome, isbn,editora,data, estoque):
        super().__init__(nome, isbn, editora,data,estoque)
        self.data=data

    def emprestimoR(self, data_emprestimo):
        if self.estoque > 0:
            self.estoque -= 1
            print(f"Revista '{self.nome}' emprestada em {data_emprestimo}. Estoque restante: {self.estoque}")
        else:
            print(f"Não há estoque disponível para a revista '{self.nome}'.")
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"ISBN: {self.isbn}")
        print(f"Editora: {self.editora}")
        print(f"Edição: {self.edicao}")
        print(f"Ano: {self.data}")
        print(f"Estoque: {self.estoque}")

    def DevolucaoR(self, estado, avaliacao):
        if estado <= 2:
            self.estoque -= 1
            print(
                f"A Revista '{self.nome}' foi devolvida em mau estado. Estoque atual: {self.estoque}. Multa de R$50 aplicada.")
        else:
            self.estoque += 1
            print(f"A Revista '{self.nome}' foi devolvida em bom estado. Estoque atual: {self.estoque}.")

        print(f"Avaliação da revista '{self.nome}': {avaliacao}/10")
revistas_dados = [
    ["National Geographic", "1", "National Geographic Society", "Março de 2022", 1],
    ["Time", "2","Time USA, LLC", "Fevereiro de 2024", 9],
    ["Scientific American", "3","Springer Nature", "Janeiro de 2024", 16],
    ["The Economist","4", "The Economist Group", "Abril de 2023", 7],
    ["Vogue","5", "Condé Nast", "Maio de 2022", 13]
]
revistas = []
for revista_dados in revistas_dados:
    revista = Revista(*revista_dados)
    revistas.append(revista)

def cadastrar_nova_revista(lista_revistas):
    nome = input("Digite o nome da revista: ")
    isbn=input("Digite o ISBN da revista: ")
    editora = input("Digite o nome da editora: ")
    edicao = input("Digite a edição da revista: ")
    estoque = int(input("Digite a quantidade em estoque da revista: "))

    nova_revista = Revista(nome,isbn,editora, edicao, estoque)
    lista_revistas.append(nova_revista)
    print("Revista Cadastrada com sucesso!")
    ultima_revista = revistas[-1]
    print("\nNova revista cadastrada:")
    print("Nome:", ultima_revista.nome)
    print("Editora:", ultima_revista.editora)
    print("Edição:", ultima_revista.edicao)
    print("Estoque:", ultima_revista.estoque)
    print("Total de revistas na lista:", len(revistas))


class Jornal(Obra):
    def __init__(self, nome, isbn,editora, data, estoque):
        super().__init__(nome,isbn, editora, data, estoque)
        self.data=data
    def emprestimoJ(self, data_emprestimo):
        if self.estoque > 0:
            self.estoque -= 1
            print(f"Jornal '{self.nome}' emprestado em {data_emprestimo}. Estoque restante: {self.estoque}")
        else:
            print(f"Não há estoque disponível para o jornal '{self.nome}'.")

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"ISBN: {self.isbn}")
        print(f"Editora: {self.editora}")
        print(f"Edição: {self.edicao}")
        print(f"Ano: {self.data}")
        print(f"Estoque: {self.estoque}")

    def DevolucaoJ(self, estado, avaliacao):
        if estado <= 2:
            self.estoque -= 1
            print(
                f"O Jornal'{self.nome}' foi devolvido em mau estado. Estoque atual: {self.estoque}. Multa de R$30 aplicada.")
        else:
            self.estoque += 1
            print(f"O Jornal '{self.nome}' foi devolvido em bom estado. Estoque atual: {self.estoque}.")

        print(f"Avaliação do Jornal '{self.nome}': {avaliacao}/10")

jornais_data = [
        ["The New York Times","1","The New York Times Company", "14 de março de 2024", 25],
        ["The Guardian","2","Guardian Media Group", "14 de março de 2024", 37],
        ["Le Monde","3", "Groupe Le Monde", "14 de março de 2024", 28],
        ["The Times","4", "News UK", "14 de março de 2024", 53],
        ["El País","5", "PRISA", "14 de março de 2024", 13],
        ["Der Spiegel","6", "Spiegel-Verlag", "14 de março de 2024", 17],
        ["Yomiuri Shimbun", "7","The Yomiuri Shimbun Holdings", "14 de março de 2024", 43]
    ]

jornais = []
for jornal_data in jornais_data:
        jornal = Jornal(*jornal_data)
        jornais.append(jornal)
def cadastrar_novo_jornal(lista_jornais):
    nome = input("Digite o nome do jornal: ")
    isbn=input("Digite o ISBN: ")
    editora = input("Digite o nome da editora: ")
    data = input("Digite a data do jornal: ")
    estoque = int(input("Digite a quantidade em estoque do jornal: "))

    novo_jornal = Jornal(nome, isbn,editora, data, estoque)
    lista_jornais.append(novo_jornal)
    print("Jornal Cadastrado com Sucesso!")
    ultimo_jornal = jornais[-1]
    print("\nNovo jornal cadastrado:")
    print("Nome:", ultimo_jornal.nome)
    print("Editora:", ultimo_jornal.editora)
    print("Data:", ultimo_jornal.edicao)
    print("Estoque:", ultimo_jornal.estoque)
    print("Total de jornais na lista:", len(jornais))

import hashlib

def criptografiaP():
    senha = input("Crie sua senha: ")
    cripto_senha = hashlib.sha256(senha.encode()).hexdigest()
    print("--- LOGIN ---")
    while True:
        senha_entrada = input("Digite sua senha: ")
        if hashlib.sha256(senha_entrada.encode()).hexdigest() == cripto_senha:
            if senha_entrada == senha:
                print("Acesso concedido como proprietário.")
                break
            else:
                print("Senha incorreta para proprietário. Tente novamente.")
        else:
            print("Senha incorreta. Tente novamente.")

def criptografia():
    senha = input("Crie sua senha: ")
    cripto_senha = hashlib.sha256(senha.encode()).hexdigest()
    print("--- LOGIN ---")
    while True:
        senha_entrada = input("Digite sua senha: ")
        if hashlib.sha256(senha_entrada.encode()).hexdigest() == cripto_senha:
            if senha_entrada == senha:
                print("Seja bem vindo a nossa Biblioteca!.")
                break
            else:
                print("Senha incorreta. Tente novamente.")


