"""
Estratégia do Código:

Este código é um jogo de adivinhação de palavras de 5 letras, com a logica do jogo termo.ooo. O programa começa lendo um arquivo chamado "lista_palavras.txt" e armazena as palavras em uma lista. Em seguida, ele remove os acentos das palavras na lista, substituindo-os por letras sem acento. O jogo seleciona aleatoriamente uma palavra de 5 letras da lista e o jogador tenta adivinhar a palavra. O jogador tem 5 tentativas para adivinhar a palavra correta. Durante o jogo, as letras certas são exibidas em ciano, as letras em posições erradas em amarelo e as letras erradas em vermelho. Após o jogo, o programa exibe quantas tentativas foram necessárias para adivinhar a palavra.

Detalhamento das Estruturas Usadas:

Função le_arquivo(arq): Essa função recebe o nome de um arquivo como entrada, abre o arquivo e retorna uma lista com todas as linhas do arquivo.

Função tirar_acento(lista): Esta função recebe uma lista de palavras e remove os acentos das letras nas palavras, substituindo-os por letras sem acento. Ela usa duas listas, uma com acentos (acentos) e outra com as letras correspondentes sem acento (sem_acento). A função também remove as palavras com acentos da lista original e substitui pelas versões sem acento.

Função letra_colorida(cor, letra): Esta função recebe uma cor e uma letra como entrada e retorna a letra formatada com a cor especificada. Ela utiliza sequências de escape ANSI para controlar a cor do texto no terminal.

Função teclado(letras_certas, letras_lugar_errado, letras_erradas): Esta função recebe três listas como entrada e exibe as letras do teclado em cores diferentes, dependendo se estão nas listas letras_certas, letras_lugar_errado ou letras_erradas.

Laço para criar uma lista palavras_5_letras: Este laço percorre a lista original de palavras e cria uma nova lista chamada palavras_5_letras contendo apenas as palavras de 5 letras.

Seleção aleatória de uma palavra: O código utiliza a biblioteca random para escolher aleatoriamente uma palavra de 5 letras da lista palavras_5_letras.

Laço principal do jogo: Este é o núcleo do jogo, onde o jogador tenta adivinhar a palavra. O jogo continua até que o jogador adivinhe corretamente a palavra ou atinja o limite de 5 tentativas.

O jogador insere uma palavra de 5 letras.
O programa compara cada letra da palavra inserida com a palavra sorteada e exibe as letras em diferentes cores (ciano para letras corretas, amarelo para letras em posições erradas e vermelho para letras erradas).
As letras corretas, em posições erradas e erradas são registradas em suas respectivas listas (letras_certas, letras_lugar_errado e letras_erradas).
O teclado é exibido após cada tentativa, mostrando as letras em diferentes cores com base na sua situação.
O número de tentativas é contado.
O jogo termina quando o jogador adivinha corretamente a palavra ou atinge o limite de 5 tentativas.

Exibição do resultado do jogo: Após o término do jogo, o programa exibe quantas tentativas foram necessárias para adivinhar a palavra. Se o jogador não adivinhar a palavra em 5 tentativas, a palavra sorteada é revelada.
"""
arquivo = "lista_palavras.txt"

def le_arquivo(arq):
    """ Lê arquivo especificado e retorna uma lista com todas as linhas 
    
        Args:
        arq (str): O nome do arquivo a ser lido.

    Returns:
        list: Uma lista de strings, onde cada string representa uma linha do arquivo.
    """   
    
    with open(arq, encoding="UTF-8") as f:
        return [linha.strip() for linha in f] # método strip remove o '\n' do final da linha
    
lista = le_arquivo(arquivo)

def tirar_acento(lista):

    """Remove acentos de palavras em uma lista.

    Esta função substitui caracteres acentuados por suas formas não acentuadas
    em todas as palavras da lista que contêm acentos.

    Args:
        lista (list): A lista de palavras a serem processadas.

    Returns:
        list: A lista de palavras sem acentos.
    """

    acentos = ['á', 'â', 'ã', 'é', 'ê', 'í', 'î', 'ó', 'ô', 'õ', 'ú', 'û', 'ç']
    sem_acento = ['a', 'e', 'i', 'o', 'u', 'c']
    palavras_com_acento = [x for x in lista for item in acentos if item in x ]
    palavras_sem_acento = []
    
    for palavras in palavras_com_acento:
        palavra_sem_acento = ""
        for letras in palavras:
            if letras in acentos:
                indice_acento = acentos.index(letras)
                if indice_acento <= 2:
                    letras_sem_acento = sem_acento[0]
                elif indice_acento <=4:
                    letras_sem_acento = sem_acento[1]
                elif indice_acento <= 6:
                    letras_sem_acento = sem_acento[2]
                elif indice_acento <=9:
                    letras_sem_acento = sem_acento[3]
                elif indice_acento <= 11:
                    letras_sem_acento = sem_acento[4]
                else:
                    letras_sem_acento = sem_acento[5]
                palavra_sem_acento += letras_sem_acento
            else:
                palavra_sem_acento += letras
        palavras_sem_acento.append(palavra_sem_acento)
    
    for palavras in palavras_com_acento:
        if palavras in lista:
            lista.remove(palavras)

    for palavras in palavras_sem_acento:
        lista.append(palavras)
    return lista



def letra_colorida(cor, letra):

    """Retorna a representação de uma letra colorida.

    Esta função permite colorir uma letra de acordo com a cor especificada.

    Args:
        cor (str): A cor desejada ('ciano', 'amarelo' ou qualquer outra).
        letra (str): A letra a ser colorida.

    Returns:
        str: A representação da letra com a cor especificada.
    """

    AMARELO = '\033[33m'
    CIANO = '\033[36m'
    VERMELHO = '\033[31m'
    LIMITE = '\033[m'

    if cor == 'ciano':
        cor = CIANO
        return cor + f'{letra}' + LIMITE
    elif cor == 'amarelo':
        cor = AMARELO
        return cor + f'{letra}' + LIMITE
    else:
        cor = VERMELHO
        return cor + f'{letra}' + LIMITE

def teclado(letras_certas, letras_lugar_errado, letras_erradas):

    """Imprime o teclado com letras coloridas.

    Esta função imprime o teclado exibindo as letras em cores diferentes com base
    nas letras certas, letras em lugares errados e letras erradas.

    Args:
        letras_certas (list): Lista de letras corretas.
        letras_lugar_errado (list): Lista de letras em lugares errados.
        letras_erradas (list): Lista de letras erradas.
    """

    teclado = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
     'c', 'v', 'b', 'n', 'm']
    
    for letras in teclado:
        indice_teclado = teclado.index(letras)
        if indice_teclado == 10 or indice_teclado == 19:
            print('\n')
        if letras in letras_certas:
            print(letra_colorida('ciano', letras), end=' ')
        elif letras in letras_lugar_errado:
            print(letra_colorida('amarelo', letras), end=' ')
        elif letras in letras_erradas:
            print(letra_colorida('vermelho', letras), end=' ')
        else:
            print(letras, end=' ')

palavras_5_letras = []
for palavras in lista:
    if len(palavras) == 5:
        palavras_5_letras.append(palavras)

tirar_acento(palavras_5_letras)

import random

index = random.randint(0, len(palavras_5_letras))

letras_erradas = []
letras_certas = []
letras_lugar_errado = []

palavra_sorteada = palavras_5_letras[index]
tentativas = 0

while True:
    palavra = input("Escreva a palavra: ")

    for letra in range(5):
        if palavra[letra] == palavra_sorteada[letra]:
            print(letra_colorida('ciano', palavra[letra]), end= ' ')
            if palavra[letra] not in letras_certas:
                letras_certas.append(palavra[letra])
        elif palavra[letra] in palavra_sorteada and palavra[letra] != palavra_sorteada[letra]:
            print(letra_colorida('amarelo', palavra[letra]), end=' ')
            if palavra[letra] not in letras_lugar_errado:
                letras_lugar_errado.append(palavra[letra])
        else:
            print(letra_colorida('vermelho', palavra[letra]), end=' ')
            if palavra[letra] not in letras_erradas:
                letras_erradas.append(palavra[letra])
    print('\n')
    teclado(letras_certas, letras_lugar_errado, letras_erradas)
    print('\n')
    tentativas += 1

    if palavra == palavra_sorteada or tentativas == 5:
        print(f"\nO Jogo Terminou, você terminou em {tentativas} tentativas")
        if tentativas == 5 and palavra != palavra_sorteada:
            print(f"\nA palavra era {palavra_sorteada}")
            print(f"\nO Jogo Terminou, você terminou em + {tentativas} tentativas")
            break
        break
