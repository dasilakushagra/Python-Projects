import random
def display_board(board):
    print(" "+board[7]+" "+"|"+" "+board[8]+" "+"|"+" "+board[9]+" ")
    print("-------------")
    print(" "+board[4]+" "+"|"+" "+board[5]+" "+"|"+" "+board[6]+" ")
    print("-------------")
    print(" "+board[1]+" "+"|"+" "+board[2]+" "+"|"+" "+board[3]+" \n")
def player_input():
    # Ask for there character i.e cross or zero
    player=""
    while True:
        player=input("Choose X or O? ")
        if player=='X' or player=='x' or player=='*':
            a=('X','O')    
            break
        elif player=="O" or player=='o'or player=="0":
            a=('O','X')
            break
    return a   
def place_marker(board,marker,position):
    board[position]=marker    # add the marker to the pos
def win_check(board,mark):
    if board[7]==board[8]==board[9]== mark or board[9]==board[6]==board[3]==mark or board[9]==board[5]==board[1]==mark or board[7]==board[5]==board[3]==mark or board[7]==board[5]==board[9]==mark or board[4]==board[5]==board[6]==mark or board[1]==board[2]==board[3]==mark or board[7]==board[4]==board[1]==mark or board[8]==board[5]==board[2]==mark:
        return True
    else:                 # check if it wins
        return False
def chose_first():
    r1=random.randint(0,1) 
    if r1==0: 
        return "player1"   # chose who will play first
    else: 
        return "player2"
def space_check(board,pos):
    if board[pos]==" ":   # check if the pos is left or not
       return True
    else:
        return False
def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):  # check for draw conditiom
            return False
    else:
        return False
def player_choice(board):
    a=int(input("Chose a no between 1-9 to place your marker: "))
    while (space_check(board,a)==False):    # player choses where to place the charcacter
        a=int(input("Chose a no between 0-9 to place your marker: "))
    return a
def replay():
    a=input("DO you wanna play again? ")
    if a[0]=="Y" or a[0]=='y': # whether player want to play or not
        return True
    else:
        return False
print("WELCOME to Tic Tac Toe!!!!!!!!!!")
a=0
while True:
    board = [' ']*10
    if a==0:
        game_on=input("Do you wanna play? ")
        if game_on[0]=="Y" or game_on[0]=="y":
            game=True
        else:
            game=False
            break

    turn=chose_first()
    mark1,mark2 = player_input()
    print("player1 = ",mark1)
    print("player2 = ",mark2)
    print()
    while game:
        if turn=="player1":
            display_board(board)
            print("player 1 turn")
            position=player_choice(board)
            place_marker(board,mark1,position)
            if win_check(board,mark1):
                display_board(board)
                print("player1 win i.e",marks)
                game=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Draw!")
                    break
                else:
                    turn="player2"
        else:
            #player2
            display_board(board)
            print("Player 2 turn i.e ",mark2)
            position=player_choice(board)
            place_marker(board,mark2,position)
            if win_check(board,mark2):
                display_board(board)
                print("player2 win")
                game=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("Draw!")
                    break
                else:
                    turn="player1"
    if replay()==False:
        #OOprint("sedfd")
        break
    else:
        game=True
        a=a+1
