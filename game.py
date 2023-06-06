# escreva um TIk Tak Toe em python

import random

# Função para imprimir o tabuleiro
def display_board(board):
    print('\n'*100)
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])

# Função para escolher o simbolo do jogador
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Você quer ser X ou O? ').upper()
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
    if random.randint(0,1) == 0:
        return 'Jogador 2'
    else:
        return 'Jogador 1'
    
# Função para verificar se a posição está livre
def space_check(board, position):
    return board[position] == ' '

# Função para verificar se o tabuleiro está cheio
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Função para escolher a posição
def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position):
        position = int(input('Escolha uma posição: (1-9) '))
    return position

# Função para perguntar se quer jogar novamente
def replay():
    return input('Quer jogar novamente? (S/N) ').lower().startswith('s')

# Função principal
print('Bem vindo ao jogo da velha!')

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' começa!')
    game_on = True
    
    while game_on:
        if turn == 'Jogador 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)
            
            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Jogador 1 ganhou!')
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('Empate!')
                break
            else:
                turn = 'Jogador 2'
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)
            
            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Jogador 2 ganhou!')
                game_on = False
            elif full_board_check(theBoard):
                display_board(theBoard)
                print('Empate!')
                break
            else:
                turn = 'Jogador 1'
                    
    if not replay():
        break

# Fim do jogo

