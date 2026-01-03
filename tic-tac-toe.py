board=[
    "0", "1", "2", "3", "4", "5", "6", "7", "8"
]
flag=0
player2_poserror=0
def print_board():
    for i in range(0,9,3):
        print(board[i]+" | "+board[i+1]+" | "+board[i+2])
        print("---------")
def check_winner():
    if(
       (board[0]==board[1]==board[2]) or
       (board[3]==board[4]==board[5]) or
       (board[6]==board[7]==board[8]) or
       (board[0]==board[3]==board[6]) or
       (board[1]==board[4]==board[7]) or
       (board[2]==board[5]==board[8]) or
       (board[0]==board[4]==board[8]) or
       (board[2]==board[4]==board[6])
       ):
        return True
    else:
        return False
player1_choice=input("Enter player 1 choice (X/O): ").upper()
if player1_choice=="X":
    player2_choice="O"
elif player1_choice=="O":
    player2_choice="X"
else:
    print("Invalid choice. Defaulting player 1 to X and player 2 to O.")
    player1_choice="X"
    player2_choice="O"
print_board()
while(
    (board[0]!="X" and board[0]!="O") or
    (board[1]!="X" and board[1]!="O") or
    (board[2]!="X" and board[2]!="O") or
    (board[3]!="X" and board[3]!="O") or
    (board[4]!="X" and board[4]!="O") or
    (board[5]!="X" and board[5]!="O") or
    (board[6]!="X" and board[6]!="O") or
    (board[7]!="X" and board[7]!="O") or
    (board[8]!="X" and board[8]!="O")
):
    if(player2_poserror==0):    
        print("Player 1's turn")
        try:
            choice=int(input("Enter position (0-8): "))
        except:
            print("Invalid input. Please enter a number between 0 and 8.")
            print_board()
            continue
        if choice<0 or choice>8:
            print("Invalid position. Try again.")
            continue
        if board[choice]!="X" and board[choice]!="O":
            board[choice]=player1_choice.upper()
            print_board()
        else:
            print("Position already taken. Try again.")
            print_board()
            continue
        if check_winner():
            flag=1
            print("Player 1 wins!")
            break
    if(
        (board[0]!="X" and board[0]!="O") or
        (board[1]!="X" and board[1]!="O") or
        (board[2]!="X" and board[2]!="O") or
        (board[3]!="X" and board[3]!="O") or
        (board[4]!="X" and board[4]!="O") or
        (board[5]!="X" and board[5]!="O") or
        (board[6]!="X" and board[6]!="O") or
        (board[7]!="X" and board[7]!="O") or
        (board[8]!="X" and board[8]!="O")
    ):  
        print("Player 2's turn")
        try:
            choice=int(input("Enter position (0-8): "))
        except:
            print("Invalid input. Please enter a number between 0 and 8.")
            player2_poserror+=1
            print_board()
            continue
        player2_poserror=0
        if choice<0 or choice>8:
                player2_poserror+=1
                print("Invalid position. Try again.")
                continue
        if board[choice]!="X" and board[choice]!="O":
            board[choice]=player2_choice.upper()
            print_board()
        else:
            player2_poserror+=1
            print("Position already taken. Try again.")
            print_board()
            continue
        if check_winner():
                flag=1
                print("Player 2 wins!")
                break
if flag==0:
    print("It's a draw!")