
from random import randint

def inicializar_jogo():
   
    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0
    tentativas = 4
    matriz = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
    return soma_diagonal_principal, soma_diagonal_secundaria, tentativas, matriz

def exibir_matriz(matriz):
    print("Bem vindo ao jogo da velha!")
  
    print("╔═══════════╗")
    for linha in matriz:
        print(f"║ {linha[0]} | {linha[1]} | {linha[2]} ║")
    print("╚═══════════╝")

def jogar(tentativas, matriz):
    """
    Gerencia o fluxo principal do jogo, alternando jogadas entre jogadores.
    """
    while tentativas > 0:
        # Jogada do jogador
        simbolo = escolher_simbolo()
        valor_linha, valor_coluna = obter_jogada_valida(matriz)
        matriz[valor_linha][valor_coluna] = simbolo
        tentativas -= 1
        exibir_matriz(matriz)

        if verificar_vitoria(matriz, simbolo):
            print(f"Jogador {simbolo} venceu!")
            return True

        if tentativas == 0:
            break

      
        print("Jogada do computador...")
        jogada_aleatoria(matriz, 'O' if simbolo == 'X' else 'X')
        exibir_matriz(matriz)

        if verificar_vitoria(matriz, 'O' if simbolo == 'X' else 'X'):
            print("Computador venceu!")
            return True

    print("Empate!")
    return False

def escolher_simbolo():

    while True:
        simbolo = input("Escolha seu símbolo (X ou O): ").upper()
        if simbolo in ['X', 'O']:
            return simbolo
        else:
            print("Símbolo inválido. Tente novamente.")

def obter_jogada_valida(matriz):
 
    while True:
        valor_linha = int(input("Digite a linha (entre 0 e 2): "))
        if 0 <= valor_linha <= 2:
            break
        else:
            print("Linha inválida. Tente novamente.")

    while True:
        valor_coluna = int(input("Digite a coluna (entre 0 e 2): "))
        if 0 <= valor_coluna <= 2:
            break
        else:
            print("Coluna inválida. Tente novamente.")

    if matriz[valor_linha][valor_coluna] != '_':
        print("Posição ocupada. Tente novamente.")
        return obter_jogada_valida(matriz)

    return valor_linha, valor_coluna

def jogada_aleatoria(matriz, simbolo):
 
    while True:
        linha = randint(0, 2)
        coluna = randint(0, 2)
        if matriz[linha][coluna] == '_':
            matriz[linha][coluna] = simbolo
            break

def verificar_vitoria(matriz, simbolo):
   
    for i in range(3):
        if matriz[i][0] == matriz[i][1] == matriz[i][2] == simbolo:
            return True
        if matriz[0][i] == matriz[1][i] == matriz[2][i] == simbolo:
            return True

    if matriz[0][0] == matriz[1][1] == matriz[2][2] == simbolo:
        return True
    if matriz[0][2] == matriz[1][1] == matriz[2][0] == simbolo:
        return True

    return False

# Inicia o jogo
soma_diagonal_principal, soma_diagonal_secundaria, tentativas, matriz = inicializar_jogo()
exibir_matriz(matriz)
jogar(tentativas, matriz)