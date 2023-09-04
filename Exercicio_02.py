"""
Estratégia do Código:

Este código implementa um tabuleiro de jogo da velha de tamanho variável.   O código utiliza uma lista bidimensional para representar o tabuleiro do jogo, onde cada elemento da lista representa uma célula do tabuleiro. Cada jogador é identificado por um símbolo ('x' ou 'o').


Detalhamento das Estruturas Usadas:

criar_tabuleiro(lista): Esta função cria um tabuleiro vazio, representado como uma lista de listas, preenchendo-o com valores iniciais "| __ |". Ela chama a função mostrar_tabuleiro para exibir o tabuleiro.

mostrar_tabuleiro(lista): Esta função exibe o tabuleiro na tela, linha por linha.

coord_da_jogada(pos): Esta função recebe uma string de entrada do usuário no formato "linha,coluna" e a divide em uma lista de coordenadas inteiras.

vez_simbolo(vez): Esta função retorna o símbolo do jogador atual com base no número de jogadas realizadas (vez ímpar para 'o' e vez par para 'x').

pos_simbolo(pos, lista, vez): Esta função recebe a posição desejada do jogador, valida se a posição está vazia e, se estiver, coloca o símbolo do jogador na posição escolhida. Em seguida, chama mostrar_tabuleiro para exibir o tabuleiro atualizado.

verif_linha(lista, simbolo): Esta função verifica se algum jogador ganhou em uma linha do tabuleiro, comparando todas as células da linha com o símbolo do jogador.

verif_coluna(lista, simbolo): Esta função verifica se algum jogador ganhou em uma coluna do tabuleiro, comparando todas as células da coluna com o símbolo do jogador.

verif_diagonal(lista, simbolo): Esta função verifica se algum jogador ganhou em uma diagonal do tabuleiro, comparando todas as células das diagonais com o símbolo do jogador.

verif_empate(lista): Esta função verifica se o jogo terminou em empate, ou seja, se não há mais células vazias no tabuleiro.

resultado(lista, vez): Esta função verifica o resultado do jogo, chamando as funções verif_linha, verif_coluna, verif_diagonal e verif_empate. Ela exibe o tabuleiro final e uma mensagem de vitória ou empate.

Loop Principal:

O loop principal do jogo solicita ao jogador sua jogada, atualiza o tabuleiro com a jogada do jogador, verifica o resultado do jogo e continua até que um jogador vença ou ocorra um empate.
"""



def criar_tabuleiro(lista, tam):

    """
    Cria um tabuleiro vazio com n linhas e n colunas.

    Args:
        lista (list): A lista que representa o tabuleiro.

    Returns:
        None
    """
    for linhas in range(0, tam):
        lista.append([])
        for colunas in range(0, tam):
            lista[linhas].append("| __ |")
    
    mostrar_tabuleiro(lista)


def mostrar_tabuleiro(lista):

    """
    Mostra o tabuleiro na tela.

    Args:
        lista (list): A lista que representa o tabuleiro.

    Returns:
        None
    """

    for linhas in lista:
        for colunas in range(0, len(linhas)):
            if colunas == len(linhas)-1:
                print(linhas[colunas] + "\n")
            else:
                print(linhas[colunas], end="")


def coord_da_jogada(pos):
    """
    Converte uma string de posição em coordenadas (linha, coluna).

    Args:
        pos (str): A string de posição no formato "linha,coluna".

    Returns:
        list: Uma lista com as coordenadas [linha, coluna].
    """
    coord = []
    pos = pos.split(",")
    for num in pos:
        coord.append(int(num))
    return coord


def vez_simbolo(vez):

    """
    Determina o símbolo da vez do jogador com base no número de jogadas.

    Args:
        vez (int): O número de jogadas.

    Returns:
        str: O símbolo da vez ("| x  |" ou "| o  |").
    """
    
    simbolo = ''

    if vez % 2 == 0:
        simbolo = '| x  |'
    else:
        simbolo = '| o  |'

    return simbolo


def pos_simbolo(pos, lista, vez):

    """
    Coloca o símbolo na posição desejada no tabuleiro.

    Args:
        pos (str): A posição no formato "linha,coluna".
        lista (list): A lista que representa o tabuleiro.
        vez (int): O número de jogadas.

    Returns:
        None
    """

    simbolo = vez_simbolo(vez)

    coord = coord_da_jogada(pos)

    if lista[coord[0]][coord[1]] == "| __ |":
        lista[coord[0]][coord[1]] = simbolo
    else:
        print("Não é possivel jogar nessa posição!")

    mostrar_tabuleiro(lista)


def verif_linha(lista, simbolo):

    """
    Verifica se há uma linha com todos os símbolos iguais.

    Args:
        lista (list): A lista que representa o tabuleiro.
        simbolo (str): O símbolo a ser verificado.

    Returns:
        bool: True se houver uma linha com todos os símbolos iguais, False caso contrário.
    """

    for linha in lista:
        if all(item == simbolo for item in linha):
            return True
    return False


def verif_coluna(lista, simbolo):

    """
    Verifica se há uma coluna com todos os símbolos iguais.

    Args:
        lista (list): A lista que representa o tabuleiro.
        simbolo (str): O símbolo a ser verificado.

    Returns:
        bool: True se houver uma coluna com todos os símbolos iguais, False caso contrário.
    """

    for coluna in range(0, len(lista)):
        if all(lista[linha][coluna] == simbolo for linha in range(4)):
            return True
    return False


def verif_diagonal(lista, simbolo):

    """
    Verifica se há uma diagonal com todos os símbolos iguais.

    Args:
        lista (list): A lista que representa o tabuleiro.
        simbolo (str): O símbolo a ser verificado.

    Returns:
        bool: True se houver uma diagonal com todos os símbolos iguais, False caso contrário.
    """

    if all(lista[i][i] == simbolo for i in range(len(lista)) or all(lista[i][(len(lista)-1)-i] == simbolo for i in range(len(lista)))):
        return True
    return False


def verif_empate(lista):

    """
    Verifica se o jogo terminou em empate.

    Args:
        lista (list): A lista que representa o tabuleiro.

    Returns:
        bool: True se o jogo terminou em empate, False caso contrário.
    """

    for linha in lista:
        if "| __ |" in linha:
            return False
    return True


def resultado(lista, vez):

    """
    Verifica se o jogo terminou e imprime o resultado.

    Args:
        lista (list): A lista que representa o tabuleiro.
        vez (int): O número de jogadas.

    Returns:
        bool: True se o jogo terminou, False caso contrário.
    """

    simbolo = vez_simbolo(vez-1)
    
    if (verif_linha(lista, simbolo)) or (verif_coluna(lista, simbolo)) or (verif_diagonal(lista, simbolo)):
        print("-"*17)
        mostrar_tabuleiro(lista)
        print(f"Parabéns, {simbolo} venceu!!")
        return True
    elif verif_empate(lista):
        print("-"*17)
        mostrar_tabuleiro(lista)
        print("O jogo terminou empatado")
        return True
    return False
            

    
#------------------------------------------------------------------------------------------------------------------------------------#         

tabuleiro = []

tam = int(input("Informe o qual vai ser o tamanho do tabuleiro (Ex: Se 10, vai ser 10 x 10): "))
criar_tabuleiro(tabuleiro, tam)

vez = 0
while True:
    pos = input("Informe a posição que deseja jogar separado por virgula(Exemplo: 0,1) :") 
    pos_simbolo(pos, tabuleiro, vez)
    vez += 1

    res = resultado(tabuleiro, vez)
    if res:
        break
    
    
