import math
def print_board(board):
    for i in board:
        print(" | ".join(i))
        print('-'*9)

def win(board,player):
    for i in board:
        if all([ player == cell for cell in i ]):
            return True
    
    for i in range(3):
        if all([ board[j][i] == player for j in range(3)]):
            return True

    if all([ player == board[i][i] for i in range(3)]):
        return True
    
    if all([ player == board[i][2-i] for i in range(3)]):
        return True
    return False

def draw(board):
    for i in board:
        if ' ' in i:
            return False
    return True

def available(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i,j))
    return moves
def alphabeta(board,depth,maximising,alpha,beta):
    if win(board,'X'):
        return (10-depth,None)
    if win(board,'O'):
        return (-10+depth,None)
    if draw(board):
        return (0,None)
    
    if maximising:
        best_score = -math.inf
        best_move = None
        for move in available(board):
            r,c = move
            board[r][c] = 'X'
            score,_ = alphabeta(board,depth+1,False,alpha,beta)
            board[r][c] = ' '
            if score>best_score:
                best_score = score
                best_move = move
            alpha = max(alpha,best_score)
            if alpha>=beta:
                break
        return (best_score,best_move)       
    else:
        best_score = math.inf
        best_move = None
        for move in available(board):
            r,c = move
            board[r][c] = 'O'
            score,_ = alphabeta(board,depth+1,True,alpha,beta)
            board[r][c] = ' '
            if score<best_score:
                best_score = score
                best_move = move
            beta = min(beta,best_score)
        return (best_score,best_move) 

def best_moves(board):
    _,move = alphabeta(board,0,True,-math.inf,math.inf)
    return move

def game():
    board = [ [ ' '  for _ in range(3) ] for _ in range(3) ]
    print_board(board)
    while True:
        while True:
            # try:
                r,c = map(int,input("Enter the position : ").strip().split())
                if board[r][c]!=' ':
                    print("Enter a proper input!!!")
                    continue
                board[r][c] = 'O'
                break
            # except ValueError:
            #     print("Enter proper input!!!")
            #     continue
        if win(board,'O'):
            print("User Wins!!!")
            break
        if win(board,'X'):
            print("AI wins")
            break
        if draw(board):
            print("Draw")
            break
        print("AI move")
        ai = best_moves(board)
        if ai:
            r,c = ai
            board[r][c] = 'X'
            if win(board,'O'):
                print("User Wins!!!")
                break
            if win(board,'X'):
                print("AI wins")
                break
            if draw(board):
                print("Draw")
                break
        else:
            print("Draw no more moves!!!")
            break
        print_board(board)
game()