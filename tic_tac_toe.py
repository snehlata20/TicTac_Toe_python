board = [' ' for x in range(10)]

def insertletter(letter,pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '

def printBoard(board):
    print('   |   |   ')
    print(' ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]))
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + str(board[4]) + ' | ' + str(board[5]) + ' | ' + str(board[6]))
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + str(board[7]) + ' | ' + str(board[8]) + ' | ' + str(board[9]))
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True

def isWinner(b,l):
    x = ((b[1]==l and b[2]==l and b[3]==l)or
    (b[4]==l and b[5]==l and b[6]==l)or
    (b[7]==l and b[8]==l and b[9]==l)or
    (b[1]==l and b[4]==l and b[7]==l)or
    (b[2]==l and b[5]==l and b[8]==l)or
    (b[3]==l and b[6]==l and b[9]==l)or
    (b[1]==l and b[5]==l and b[9]==l)or
    (b[3]==l and b[5]==l and b[7]==l))

    return x

def playerMode():
    run = True
    while run:
        move=input("Please select a postion to put x between 1 to 9 :-  ")
        try:
            move=int(move)
            if move >0 and move < 10:
                if spaceIsFree(move):
                    run= False
                    insertletter('X',move)
                else:
                   print("Sorry ! space is already full")
            else:
                print("Eneter valid number beween 1-9")
        except:
            print("please type a correct number ")  

def selectRandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]

def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter==' 'and x!= 0]
    print(possibleMoves)
    move=0
    for let in ['O','X']:
        for i in possibleMoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if isWinner(boardcopy,let):
                move=i
                return move
    
    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen)>0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move
    
    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen)>0:
        move = selectRandom(edgesOpen)
        return move
    
def main():
    print("Welcome to the game")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board,'O')):
            playerMode()
            printBoard(board)
        else:
            print("sorry you loose this game!")
            break

        if not(isWinner(board,'X')):
            move=computerMove()
            if move == 0:
                print(" ")
            else:
                try:
                    insertletter('O',move)
                    print("Bot placed O on the position", move)
                    printBoard(board)
                except:
                    print("Oops.. Game Tie !")
        else:
            print("Wohoooooo :) You win !")
            break
    

while True:
    x = input("Do you want to play again? (y/n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print('--------------------')
        main()
    else:
        break
            




