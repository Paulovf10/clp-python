from datetime import datetime


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
    def __init__(self, number, data_nasc, client: Cliente, itens: []):
        self.numero = number
        self.data = data_nasc
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

Clientes = []
Produtos = []
Vendas = []
while True:
    print('------------------Menu inicial------------------')
    print("1-Cliente \n2-Produto \n3-Venda")
    cod = int(input("Qual entidade você quer manipular:"))

    if cod == 1:
        status = 1
        while status != 0:
            print('------------------Menu Clientes------------------')
            print(
                "1-Cadastrar um cliente \n2-Visualizar um cliente \n3-Alterar um cliente \n"
                "4-Excluir um cliente \n0-Voltar ao menu inicial\n")
            status = int(input("O que deseja fazer: "))
            if status == 1:
                nome = str(input('Digite o nome do cliente: '))
                endereco = str(input('Digite o endereço do cliente: '))
                rg = str(input('Digite o rg do cliente: '))
                data_nascimento = str(input('Digite a data de nascimento do cliente: '))
                try:
                    date = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                except:
                    print(
                        "\n-Fomatação de data invalida!!! Cadastro cancelado\nA data deve estar no formato %d/%m/%Y\n")
                    continue
                cliente = Cliente(nome, endereco, rg, date)
                Clientes.append(cliente)

            elif status == 2:
                print("\n-Clientes cadastrados")
                for elem in Clientes:
                    if elem.nome:
                        print('---------------------')
                        print("Nome:", elem.nome)
                        print("Rg:", elem.rg)
                        print("Endereço:", elem.enderece)
                        print("Data de nascimento:", elem.data_nascimento)

            elif status == 3:
                ind = str(input("Digite o nome do cliente que desejsa alterar: "))
                flag = 0
                for elem in Clientes:
                    if elem.nome == ind:
                        nome = input('Digite o novo nome: ')
                        endereco = input('Digite o novo enderece: ')
                        rg = input('Digite o novo rg: ')
                        data_nascimento = input('Digite a nova data de nascimento: ')
                        try:
                            date = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                        except:
                            print(
                                "\n-Fomatação de data invalida!!! Cadastro cancelado\n"
                                "A data deve estar no formato %d/%m/%Y\n")
                            continue
                        elem.alterar_cli(rg, data_nascimento, nome, endereco)
                        flag = 1
                if flag == 0:
                    print("Não existe ninguem cadastrado com esse nome")

            elif status == 4:
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
    elif cod == 2:
        status = 1
        while status != 0:
            print('------------------Menu Produtos------------------')
            print("1-Cadastrar um produto \n2-Visualizar um produto \n3-Alterar um produto \n"
                  "4-Excluir um produto \n0-Voltar ao menu inicial\n")
            status = int(input("O que deseja fazer: "))
            if status == 1:
                try:
                    codigo = int(input('Digite o codigo do produto: '))
                except ValueError:
                    print(
                        "\n-Entrada invalida!!! Cadastro cancelado\nO codigo deve ser um número inteiro\n")
                    continue
                nome = str(input('Digite o nome do produto: '))
                try:
                    valor = float(input('Digite o valor do produto: '))
                except ValueError:
                    print(
                        "\n-Entrada invalida!!! Cadastro cancelado\nO valor deve ser um número\n")
                    continue
                produto = Produto(codigo, nome, valor)
                Produtos.append(produto)

            elif status == 2:
                print("\n-Produtos cadastrados")
                for elem in Produtos:
                    if elem.nome:
                        print('---------------------')
                        print("Nome:", elem.nome)
                        print("Código:", elem.codigo)
                        print("Valor:", elem.valor)

            elif status == 3:
                ind = str(input("Digite o nome do produto que deseja alterar: "))
                flag = 0
                for elem in Produtos:
                    if elem.nome == ind:
                        try:
                            codigo = int(input('Digite o novo codigo: '))
                        except ValueError:
                            print(
                                "\n-Entrada invalida!!! Cadastro cancelado\nO codigo deve ser um número inteiro\n")
                            continue
                        nome = input('Digite o novo nome: ')
                        try:
                            valor = float(input('Digite o novo valor: '))
                        except ValueError:
                            print(
                                "\n-Entrada invalida!!! Cadastro cancelado\nO valor deve ser um número \n")
                            continue
                        elem.alterar_prod(codigo, nome, valor)
                        flag = 1
                if flag == 0:
                    print("Não existe nenhum produto cadastrado com esse nome")

            elif status == 4:
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
    elif cod == 3:
        status = 1
        while status != 0:
            print('------------------Menu Vendas------------------')
            ItemVendas = []
            print("1-Cadastrar uma venda \n2-Visualizar uma venda \n3-Excluir uma venda \n0-Voltar ao menu inicial\n")
            status = int(input("O que deseja fazer: "))
            if status == 1:
                try:
                    numero = int(input('Digite o número da sua venda: '))
                except ValueError:
                    print(
                        "\n-Entrada invalida!!! Cadastro cancelado\nO número deve ser um número inteiro\n")
                    continue
                data = str(input('Digite a data da sua venda: '))
                try:
                    date = datetime.strptime(data, '%d/%m/%Y').date()
                except:
                    print("\n-Fomatação de data invalida!!! Cadastro cancelado\n"
                          "A data deve estar no formato %d/%m/%Y\n")
                    continue
                cliente = str(input('Digite o nome do seu cliente: '))
                cod2 = 1
                while cod2 != 0:
                    print('------------------Menu de itens------------------')
                    print("1-Adicionar item \n2-Visualizar itens adicionados \n4-Remover item \n0-Finalisar venda ")
                    cod2 = int(input('O que deseja fazer: '))
                    if cod2 == 1:
                        produto = str(input('Digite o nome do produto: '))
                        try:
                            quantidade = int(input('Digite a quantidade: '))
                        except ValueError:
                            print(
                                "\n-Entrada invalida!!! Cadastro cancelado\nA quantidade deve ser um número inteiro\n")
                            continue
                        for elem in Produtos:
                            if elem.nome == produto:
                                Item = ItemVenda(elem, quantidade)
                                ItemVendas.append(Item)
                    elif cod2 == 2:
                        for elem in ItemVendas:
                            print("Nome:", elem.produto.nome)
                            print("Quantidade:", elem.quantidade)
                            print("Valor:", elem.valor)
                for elem in Clientes:
                    if elem.nome == cliente:
                        venda = Venda(numero, data, elem, ItemVendas)
                        Vendas.append(venda)

            elif status == 2:
                print("\n-Vendas cadastradas")
                for elem in Vendas:
                    print('---------------------')
                    print(elem.numero)
                    print(elem.data)
                    print(elem.cliente.nome)
                    print(elem.total)

            elif status == 3:
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
