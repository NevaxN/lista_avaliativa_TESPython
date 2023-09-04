"""
Explicação da Estratégia:

Este codigo é um Banco de dados formado por dicionarios. Ele começa definindo três funções de menu: menu_principal, menu_cadastrar, e menu_imprimir. Cada uma delas imprime as opções disponíveis para o usuário.

A função cadastrar_usuario é responsável por coletar informações sobre um novo usuário e adicioná-las a um banco de dados (banco_usuarios).
A função imprimir_usuarios permite ao usuário visualizar os dados dos usuários cadastrados, com a opção de filtrar por nomes e campos.
As funções filtrar_nomes e filtrar_campos auxiliam na filtragem dos dados dos usuários.
O programa principal começa solicitando ao usuário que informe os campos obrigatórios para o cadastro. Em seguida, ele entra em um loop que exibe o menu principal e permite ao usuário escolher entre as opções disponíveis:

Cadastrar um novo usuário, onde o usuário pode inserir informações adicionais.
Imprimir informações dos usuários, com opções de filtragem.
Encerrar o programa.
O código continua em execução até que o usuário escolha a opção de encerrar.

Detalhamento das Estruturas Usadas:

Funções de Menu:

menu_principal(): Exibe as opções principais do programa.
menu_cadastrar(): Exibe as opções do menu de cadastro de usuário.
menu_imprimir(): Exibe as opções do menu de impressão de informações.
Funções de Manipulação de Dados:

cadastrar_usuario(campos, banco): Coleta informações sobre um novo usuário e adiciona-o ao banco de dados. Permite adicionar campos adicionais conforme necessário.
imprimir_usuarios(banco): Exibe informações dos usuários do banco de dados, com opções de filtragem.
filtrar_nomes(*nomes): Recebe nomes como argumento e os divide em uma lista.
filtrar_campos(**kwargs): Recebe campos de busca como argumentos e permite ao usuário especificar valores para filtragem.

Variáveis Principais:

campos: Armazena os campos obrigatórios para o cadastro de usuários.
banco_usuarios: Armazena os dados dos usuários cadastrados.

Loop Principal:

Um loop principal permite ao usuário escolher entre as opções do menu principal.
Dependendo da escolha, as funções apropriadas são chamadas para realizar as operações desejadas.
"""


def menu_principal():

    """
    Função para exibir o menu principal.
    """

    print('''
        1 - Cadastrar Usuarios
        2 - Imprimir Usuarios
        0 - Encerrar''')
    
def menu_cadastrar():

    """
    Função para exibir o menu de cadastro de usuários.
    """

    print("""
        1 - Cadastrar Novo Campo
        2 - Sair
        """)
    
def menu_imprimir():

    """
    Função para exibir o menu de impressão de usuários.
    """

    print('''
        1 - Imprimir Todos
        2 - Filtrar por Nomes
        3 - Filtrar por Campos
        4 - Filtrar por Nomes e Campos
    ''')
    

def cadastrar_usuario(campos, banco):

    """
    Função para cadastrar um novo usuário no banco de dados.

    Args:
        campos (str): Uma string contendo os nomes dos campos obrigatórios separados por vírgula.
        banco (dict): Um dicionário que representa o banco de dados de usuários.

    """

    usuario = {}

    campos = campos.split(",")
    for campo in campos:
        usuario[campo] = input(f'Informe o valor de {campo}: ')
    
    while True:
        menu_cadastrar() 
        opcao = int(input("Informe o a opção que deseja: "))

        if opcao == 1:
            novo_campo = input("Informe o nome do novo campo: ")
            usuario[novo_campo] = input(f"Informe o valor do(a) {novo_campo}: ")
        else:
            banco[len(banco) + 1] = usuario
            break
    
def imprimir_usuarios(banco):

    """
    Função para imprimir usuários com várias opções de filtragem.

    Args:
        banco (dict): Um dicionário que representa o banco de dados de usuários.

    """

    while True:
        menu_imprimir()
        opcao = int(input("Informe a opção que deseja: "))

        if opcao == 1:
            for usuarios in banco:
                print('\n')
                for valores in banco[usuarios]:
                    print(f"{valores} - {banco[usuarios][valores]}")
            break

        elif opcao == 2:
            nomes = input("Digite os nomes(Separados por virgula): ")

            for usuarios in banco:
                for valores in banco[usuarios]:
                    if banco[usuarios]['nome'] in filtrar_nomes(nomes):
                        print(f"{valores} - {banco[usuarios][valores]}")
            break

        elif opcao == 3:
            campos = filtrar_campos(campo={})
            valores_filtragem = []
            for chave in campos:
                valores_filtragem.append(campos[chave])

            for usuarios in banco:
                for valores in banco[usuarios]:
                    if banco[usuarios][chave] in valores_filtragem[0:2]:
                        print(f"{valores} - {banco[usuarios][valores]}")
            break

        elif opcao == 4:
            nomes = input("Digite os nomes(Separados por virgula): ")
            filtrar_nomes(nomes)
            campos = filtrar_campos(campo={})

            valores_filtragem = []
            for chave in campos:
                valores_filtragem.append(campos[chave])

            for usuarios in banco:
                for valores in banco[usuarios]:
                     if banco[usuarios][chave] in valores_filtragem[0:2]:
                        print(f"{valores} - {banco[usuarios][valores]}")
            break

def filtrar_nomes(*nomes):

    """
    Função para separar nomes separados por vírgula, retornar esses nomes para acontecer a filtragem.

    Args:
        nomes (str): Uma string contendo nomes separados por vírgula.

    Returns:
        list: Uma lista contendo os nomes separados.

    """

    for nome in nomes:
        nome = nome.split(",")
    return nome

def filtrar_campos(**kwargs):

    """
    Função para filtrar campos de busca.

    Args:
        kwargs (dict): Um dicionário contendo os campos de busca.

    Returns:
        dict: Um dicionário com os campos de busca.

    """

    for campo in kwargs:
        chave_campo = input("digite o campo de busca: ")
        kwargs[campo][chave_campo] = input(f'digite o(a) {chave_campo}: ')
        while chave_campo != 'sair':
            chave_campo = input("mais algum campo: ")
            if chave_campo != 'sair':
                kwargs[campo][chave_campo] = input(f'digite o(a) {chave_campo}: ')
            else:
                break
    return kwargs[campo]

campos = ()
campos = input("Informe os Campos Obrigatórios para o Cadastro (EX: nome, idade, endereço...): ")
banco_usuarios = {}

while True:
    menu_principal()
    opcao = int(input("Informe a opção do menu que deseja acessar: "))
    if opcao == 1:
        cadastrar_usuario(campos, banco_usuarios)
        print(banco_usuarios)
    elif opcao == 2:
        imprimir_usuarios(banco_usuarios)
    else:
        break

