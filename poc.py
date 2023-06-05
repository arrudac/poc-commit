# escreva um jogo da velha para dois jogadores 

import os
import random

# Função para limpar a tela
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para imprimir o tabuleiro
def display_board(board):
    clear()
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Função para escolher o simbolo do jogador
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Jogador 1: Você quer ser X ou O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

# Função para colocar o simbolo no tabuleiro
def place_marker(board, marker, position):
    board[position] = marker

# Função para verificar se o jogador ganhou
def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # linha de cima
    (board[4] == mark and board[5] == mark and board[6] == mark) or # linha do meio
    (board[1] == mark and board[2] == mark and board[3] == mark) or # linha de baixo
    (board[7] == mark and board[4] == mark and board[1] == mark) or # coluna da esquerda
    (board[8] == mark and board[5] == mark and board[2] == mark) or # coluna do meio
    (board[9] == mark and board[6] == mark and board[3] == mark) or # coluna da direita
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Função para escolher quem vai começar
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Jogador 2'
    else:
        return 'Jogador 1'

# Função para verificar se a posição está livre
def space_check(board, position):
    return board[position] == ' '

# Função para verificar se o tabuleiro está cheio
def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

# Função para escolher a posição
def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input('Escolha sua próxima posição: (1-9) '))
    return position

# Função para perguntar se quer jogar novamente
def replay():
    return input('Quer jogar novamente? "Sim" ou "Não" ').lower().startswith('s')

# Função principal
def main():

    print('Bem vindo ao jogo da velha!')

    while True:
        # Reseta o tabuleiro
        theBoard = [' '] * 10
        # Escolhe o simbolo
        player1_marker, player2_marker = player_input()
        # Escolhe quem vai começar
        turn = choose_first()
        print(turn + ' começa!')
        # Pergunta se quer jogar
        play_game = input('Quer jogar? "Sim" ou "Não" ')
        if play_game.lower()[0] == 's':
            game_on = True
        else:
            game_on = False

        while game_on:
            if turn == 'Jogador 1':
                # Vez do jogador 1
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player1_marker, position)
                # Verifica se ganhou
                if win_check(theBoard, player1_marker):
                    display_board(theBoard)
                    print('Parabéns! Você venceu!')
                    game_on = False
                else:
                    # Verifica se o tabuleiro está cheio
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Empate!')
                        break
                    else:
                        turn = 'Jogador 2'
            else:
                # Vez do jogador 2
                display_board(theBoard)
                position = player_choice(theBoard)
                place_marker(theBoard, player2_marker, position)
                # Verifica se ganhou
                if win_check(theBoard, player2_marker):
                    display_board(theBoard)
                    print('Parabéns! Você venceu!')
                    game_on = False
                else:
                    # Verifica se o tabuleiro está cheio
                    if full_board_check(theBoard):
                        display_board(theBoard)
                        print('Empate!')
                        break
                    else:
                        turn = 'Jogador 1'

        if not replay():
            break

if __name__ == "__main__":
    main()

