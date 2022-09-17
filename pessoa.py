class Pessoa(object):
    def __init__(self, name, address):
        self.nome = name
        self.enderece = address

    def alterar(self, name, address):
        self.nome = name
        self.enderece = address

    def remover(self):
        self.nome = None
        self.enderece = None


class Cliente(Pessoa):
    def __init__(self, name, address, reg, date_nascimento):
        self.rg = reg
        self.data_nascimento = date_nascimento
        super().__init__(name, address)

    def alterar_cli(self, reg, date_nascimento, name, address):
        self.rg = reg
        self.data_nascimento = date_nascimento
        super().alterar(name, address)

    def remover_cli(self):
        self.nome = None
        self.enderece = None
        super().remover()


class Produto:
    def __init__(self, code, name, value):
        self.codigo = code
        self.nome = name
        self.valor = value

    def alterar_prod(self, code, name, value):
        self.codigo = code
        self.nome = name
        self.valor = value

    def remover_prod(self):
        self.codigo = None
        self.nome = None
        self.valor = None


class Totalizavel:

    def total(self, value, quantity):
        total = value * quantity
        return total

    def soma(self, value, quantity):
        total = value + quantity
        return total


class ItemVenda(Totalizavel):
    def __init__(self, product: Produto, quantity):
        self.produto = product
        self.quantidade = quantity
        self.valor = super().total(produto.valor, quantidade)


class Venda(Totalizavel):
    def __init__(self, number, date, client: Cliente, itens: []):
        self.numero = number
        self.data = date
        self.cliente = client
        self.itens = itens
        total = 0
        for ele in itens:
            total += super().soma(ele.quantidade, ele.valor)
        self.total = total

    def remover_venda(self):
        self.numero = None
        self.data = None
        self.cliente = None
        self.itens = None


print("Bem vindos !!!")

Pessoas = []
Clientes = []
Produtos = []
Vendas = []
while True:
    print('------------------Menu inicial------------------')
    print("1-Pessoa \n2-Cliente \n3-Produto \n4-Venda")
    cod = int(input("Qual entidade você quer manipular:"))
    if cod == 1:
        print('------------------Menu Pessoas------------------')
        print("1-Cadastrar uma pessoa \n2-Visualizar uma pessoa \n3-Alterar uma pessoa \n4-Excluir uma pessoa")
        cod = int(input("O que deseja fazer: "))
        if cod == 1:
            nome = str(input('Digite o nome da pessoa: '))
            endereco = str(input('Digite o endereco da pessoa: '))
            pessoa = Pessoa(nome, endereco)
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
        print('------------------Menu Clientes------------------')
        print("1-Cadastrar um cliente \n2-Visualizar um cliente \n3-Alterar um cliente \n4-Excluir um cliente")
        cod = int(input("O que deseja fazer: "))
        if cod == 1:
            nome = str(input('Digite o nome do cliente: '))
            endereco = str(input('Digite o endereço do cliente: '))
            rg = str(input('Digite o rg do cliente: '))
            data_nascimento = str(input('Digite a data de nascimento do cliente: '))
            cliente = Cliente(nome, endereco, rg, data_nascimento)
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
        print('------------------Menu Produtos------------------')
        print("1-Cadastrar um produto \n2-Visualizar um produto \n3-Alterar um produto \n4-Excluir um produto")
        cod = int(input("O que deseja fazer: "))
        if cod == 1:
            codigo = int(input('Digite o codigo do produto: '))
            nome = str(input('Digite o nome do produto: '))
            valor = float(input('Digite o valor do produto: '))
            produto = Produto(codigo, nome, valor)
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

    # Venda
    elif cod == 4:
        print('------------------Menu Vendas------------------')
        ItemVendas = []
        print("1-Cadastrar uma venda \n2-Visualizar uma venda\n3-Alterar umavenda \n4-Excluir uma venda")
        cod = int(input("O que deseja fazer: "))
        if cod == 1:
            numero = int(input('Digite o número da sua venda: '))
            data = str(input('Digite a data da sua venda: '))
            cliente = str(input('Digite o nome do seu cliente: '))
            cod2 = 1
            while cod2 != 0:
                print('------------------Menu de itens------------------')
                print("1-Adicionar item \n2-Visualizar itens adicionados \n4-Remover item \n0-Finalisar venda")
                cod2 = int(input('O que deseja fazer: '))
                if cod2 == 1:
                    produto = str(input('Digite o nome do produto: '))
                    quantidade = int(input('Digite a quantidade: '))
                    for elem in Produtos:
                        if elem.nome == produto:
                            Item = ItemVenda(elem, quantidade)
                            ItemVendas.append(Item)
                elif cod2 == 2:
                    for elem in ItemVendas:
                        print(elem.produto.nome)
                        print(elem.quantidade)
                        print(elem.valor)
            for elem in Clientes:
                if elem.nome == cliente:
                    venda = Venda(numero, data, elem, ItemVendas)
                    Vendas.append(venda)

        elif cod == 2:
            for elem in Vendas:
                print('---------------------')
                print(elem.numero)
                print(elem.data)
                print(elem.cliente.nome)
                print(elem.total)

        elif cod == 3:
            ind = str(input("Digite o número da venda que deseja excluir: "))
            flag = 0
            for elem in Vendas:
                if elem.numero == ind:
                    elem.remover_venda()
                    flag = 1
            if flag == 0:
                print("Não existe nenhum produto cadastrado com esse nome")
        else:
            print("Codigo invalido")

    elif cod == 0:
        break
    else:
        print('Comando invalido, tente novamente')
