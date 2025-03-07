board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
isPlay = True
isPlayer1 = True
isWinner = False


def getSymbol():
    if isPlayer1:
        return 'X'
    return 'O'


def getPlayer():
    if isPlayer1:
        return 'Player 1'
    return 'Player 2'


def getDisplay():
    print('Press r or R to Reset.')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print(board)


def checkWinner():
    # left diagonal
    if board[0] == board[4] == board[8] == 'X':
        print('Player 1 won.')
        return True

    if board[0] == board[4] == board[8] == 'O':
        print('Player 2 won.')
        return True

    # right diagonal
    if board[2] == board[4] == board[6] == 'X':
        print('Player 1 won.')
        return True

    if board[2] == board[4] == board[6] == 'O':
        print('Player 2 won.')
        return True

    # horizontal
    for i in range(0, 7, 3):
        if board[i] == board[i+1] == board[i+2] == 'X':
            print('Player 1 won.')
            return True

        if board[i] == board[i+1] == board[i+2] == 'O':
            print('Player 2 won.')
            return True

    # vertical
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == 'X':
            print('Player 1 won.')
            return True

        if board[i] == board[i+3] == board[i+6] == 'O':
            print('Player 2 won.')
            return True

    return False


while isPlay:
    getDisplay()

    while not isWinner:
        try:
            pos = int(input(f'{getPlayer()}, enter pos between 1-9. '))
        except ValueError as e:
            print(e)
        else:
            if pos > 0 and pos < 10:
                if board[pos-1] == "X" or board[pos-1] == "O":
                    print(f'{pos} already occupied.')
                else:
                    board[pos-1] = getSymbol()
                    isPlayer1 = not isPlayer1
                    getDisplay()
            else:
                print('Only enter pos between 1-9.')
            isWinner = checkWinner()

            if isWinner:
                isPlay = False
                print('Game Over.')
                isPlayAgain = input('Play again? Y or N').lower()
                if isPlayAgain == 'y':
                    isPlay = True
                    isPlayer1 = True
                    isWinner = False
                    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                    getDisplay()
