
class Pessoa(object):
    def __init__(self, nome, endereco):
        self.nome = nome
        self.enderece = endereco

    def alterar(self, nome, endereco):
        self.nome = nome
        self.enderece = endereco

    def remover(self):
        self.nome = None
        self.enderece = None


class Cliente(Pessoa):
    def __init__(self, nome, endereco,  rg, data_nascimento):
        self.rg = rg
        self.data_nascimento = data_nascimento
        super().__init__(nome, endereco)

    def alterar_cli(self, rg, data_nascimento, nome, endereco):
        self.rg = rg
        self.data_nascimento = data_nascimento
        super().alterar(nome, endereco)

    def remover_cli(self):
        self.nome = None
        self.enderece = None
        super().remover()


class Produto:
    def __init__(self, codigo, nome, valor):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor

    def alterar_prod(self, codigo, nome, valor):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor

    def remover_prod(self):
        self.codigo = None
        self.nome = None
        self.valor = None


class Totalizavel:
    def total(self):
        pass


class Venda(Totalizavel):
    def __init__(self, numero, data, cliente:Cliente, itens:[]):
        self.numero = numero
        self.data = data
        self.cliente = cliente
        self.itens = itens
        super().__init__()


class ItemVenda(Totalizavel):
    def __init__(self, produto:Produto, valor, quantidade):
        self.produto = produto
        self.valor = valor
        self.quantidade = quantidade
        super().__init__()


print("Bem vindos !!!")

Pessoas = []
Clientes = []
Produtos = []
while True:
    print("1-Pessoa \n2-Cliente \n3-Produto \n4-Totalizavel \n5-Venda \n6-ItemVenda")
    cod = int(input("Qual entidade você quer manipular:"))
    if cod == 1:
        print("1-Cadastrar uma pessoa \n2-Visualizar uma pessoa \n3-Alterar uma pessoa \n4-Excluir uma pessoa")
        cod = int(input("O que deseja fazer: "))
        if cod == 1:
            name = str(input('Digite o nome da pessoa: '))
            endereco = str(input('Digite o endereco da pessoa: '))
            pessoa = Pessoa(name, endereco)
            Pessoas.append(pessoa)

        elif cod == 2:
            for elem in Pessoas:
                if elem.nome:
                    print(elem.nome)

        elif cod == 3:
            ind = str(input("Digite o nome da pessoa que desejsa alterar: "))
            flag = 0
            for elem in Pessoas:
                if elem.nome == ind:
                    nome = input('Digite o novo nome: ')
                    enderece = input('Digite o novo enderece: ')
                    elem.alterar(nome, enderece)
                    flag = 1
            if flag == 0:
                print("Não existe ninguem cadastrado com esse nome")

        elif cod == 4:
            ind = str(input("Digite o nome da pessoa que deseja excluir: "))
            flag = 0
            for elem in Pessoas:
                if elem.nome == ind:
                    elem.remover()
                    flag = 1
            if flag == 0:
                print("Não existe ninguem cadastrado com esse nome")
        else:
            print("Codigo invalido")

    #  Cliente
    elif cod == 2:
        print("1-Cadastrar um cliente \n2-Visualizar um cliente \n3-Alterar um cliente \n4-Excluir um cliente")
        cod = int(input("O que deseja fazer: "))
        if cod == 1:
            name = str(input('Digite o nome do cliente: '))
            endereco = str(input('Digite o endereço do cliente: '))
            rg = str(input('Digite o rg do cliente: '))
            data_nascimento = str(input('Digite a data de nascimento do cliente: '))
            cliente = Cliente(name, endereco, rg, data_nascimento)
            Clientes.append(cliente)

        elif cod == 2:
            for elem in Clientes:
                if elem.nome:
                    print(elem.nome)

        elif cod == 3:
            ind = str(input("Digite o nome do cliente que desejsa alterar: "))
            flag = 0
            for elem in Clientes:
                if elem.nome == ind:
                    nome = input('Digite o novo nome: ')
                    endereco = input('Digite o novo enderece: ')
                    rg = input('Digite o novo enderece: ')
                    data_nascimento = input('Digite o novo enderece: ')
                    elem.alterar_cli(rg, data_nascimento, nome, endereco)
                    flag = 1
            if flag == 0:
                print("Não existe ninguem cadastrado com esse nome")

        elif cod == 4:
            ind = str(input("Digite o nome do cliente que deseja excluir: "))
            flag = 0
            for elem in Clientes:
                if elem.nome == ind:
                    elem.remover_cli()
                    flag = 1
            if flag == 0:
                print("Não existe ninguem cadastrado com esse nome")
        else:
            print("Codigo invalido")

    #  Produto
    elif cod == 3:
        print("1-Cadastrar um produto \n2-Visualizar um produto \n3-Alterar um produto \n4-Excluir um produto")
        cod = int(input("O que deseja fazer: "))
        if cod == 1:
            codigo = str(input('Digite o codigo do produto: '))
            name = str(input('Digite o name do produto: '))
            valor = str(input('Digite o valor do produto: '))
            produto = Produto(codigo, name, valor)
            Produtos.append(produto)

        elif cod == 2:
            for elem in Produtos:
                if elem.nome:
                    print(elem.nome)

        elif cod == 3:
            ind = str(input("Digite o nome do produto que deseja alterar: "))
            flag = 0
            for elem in Produtos:
                if elem.nome == ind:
                    codigo = input('Digite o novo codigo: ')
                    nome = input('Digite o novo nome: ')
                    valor = input('Digite o novo valor: ')
                    elem.alterar_prod(codigo, nome, valor)
                    flag = 1
            if flag == 0:
                print("Não existe nenhum produto cadastrado com esse nome")

        elif cod == 4:
            ind = str(input("Digite o nome do produto que deseja excluir: "))
            flag = 0
            for elem in Produtos:
                if elem.nome == ind:
                    elem.remover_prod()
                    flag = 1
            if flag == 0:
                print("Não existe nenhum produto cadastrado com esse nome")
        else:
            print("Codigo invalido")
    elif cod == 4:
        print('cli')
    elif cod == 5:
        print('cli')
    elif cod == 6:
        print('cli')
    elif cod == 0:
        break
    else:
        print('Comando invalido, tente novamente')
