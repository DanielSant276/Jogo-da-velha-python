from os import system 

ticTacToe = [['-','-','-'],['-','-','-'],['-','-','-']]
finish = False
draw = False

def clear(): 
    _ = system('cls')

def ticTacToeFormation():
        print(ticTacToe[0][0], ticTacToe[0][1], ticTacToe[0][2])
        print(ticTacToe[1][0], ticTacToe[1][1], ticTacToe[1][2])
        print(ticTacToe[2][0], ticTacToe[2][1], ticTacToe[2][2])

def question():
    global finish
    quest = input('desistir? ')
    if quest == 's' or quest == 'sim':
        finish = True

def play():
    global finish, draw

    xTurn = True
    oTurn = False

    while not finish:
        while xTurn:
            question()
            if finish:
                winner = 'o'
                print('O jogador x desistiu.', end=' ')
                break
            
            valid = False
            while not valid:
                player1Row = int(input('Jogador 1, escolhar uma linha: ')) - 1
                player1Col = int(input('Jogador 1, escolha uma coluna: ')) - 1
                if  0 <= player1Row < 3 and 0 <= player1Col < 3:   
                    if ticTacToe[player1Row][player1Col] == '-':
                        valid = True
                    else:
                        print('Espaço ocupado por uma jogada, escolha outro espaço')
                else:
                    print('Espaço inválido')
            ticTacToe[player1Row][player1Col] = 'x'

            clear()
            ticTacToeFormation()
            
            if (ticTacToe[0][0] == 'x' and ticTacToe[0][1] == 'x' and ticTacToe[0][2] == 'x') or (ticTacToe[1][0] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[1][2] == 'x') or (ticTacToe[2][0] == 'x' and ticTacToe[2][1] == 'x' and ticTacToe[2][2] == 'x') or (ticTacToe[0][0] == 'x' and ticTacToe[1][0] == 'x' and ticTacToe[2][0] == 'x') or (ticTacToe[0][1] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[2][1] == 'x') or (ticTacToe[0][2] == 'x' and ticTacToe[1][2] == 'x' and ticTacToe[2][2] == 'x') or (ticTacToe[0][0] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[2][2] == 'x') or (ticTacToe[0][2] == 'x' and ticTacToe[1][1] == 'x' and ticTacToe[2][0] == 'x'):
                winner = 'x'
                finish = True
                break

            xTurn = False
            oTurn = True

        if not finish:
            while oTurn:
                question()
                if finish:
                    winner = 'x'
                    print('O jogador o desistiu.', end=' ')
                    break

                valid = False
                while not valid:
                    player2Row = int(input('Jogador 2, escolhar uma linha: ')) - 1
                    player2Col = int(input('Jogador 2, escolha uma coluna: ')) - 1
                    if  0 <= player2Row < 3 and 0 <= player2Col < 3:   
                        if ticTacToe[player2Row][player2Col] == '-':
                            valid = True
                        else:
                            print('Espaço ocupado por uma jogada, escolha outro espaço')
                    else:
                        print('Espaço inválido')
                ticTacToe[player2Row][player2Col] = 'o'

                clear()
                ticTacToeFormation()
                
                if (ticTacToe[0][0] == 'o' and ticTacToe[0][1] == 'o' and ticTacToe[0][2] == 'o') or (ticTacToe[1][0] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[1][2] == 'o') or (ticTacToe[2][0] == 'o' and ticTacToe[2][1] == 'o' and ticTacToe[2][2] == 'o') or (ticTacToe[0][0] == 'o' and ticTacToe[1][0] == 'o' and ticTacToe[2][0] == 'o') or (ticTacToe[0][1] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[2][1] == 'o') or (ticTacToe[0][2] == 'o' and ticTacToe[1][2] == 'o' and ticTacToe[2][2] == 'o') or (ticTacToe[0][0] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[2][2] == 'o') or (ticTacToe[0][2] == 'o' and ticTacToe[1][1] == 'o' and ticTacToe[2][0] == 'o'):
                    winner = 'o'
                    finish = True
                    break

                xTurn = True
                oTurn = False
        
        total = 0
        for i in range(len(ticTacToe)):
            for j in range(len(ticTacToe[0])):
                if ticTacToe[i][j] != '-':
                    total += 1
        if total == 9:
            finish = True
            draw = True

        
    if finish:
        if draw:
            print('O jogo empatou, não houve vencedores')
        else:
            print('O vencedor foi o jogador', winner)

play()