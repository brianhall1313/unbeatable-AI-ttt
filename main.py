import random,copy

x='X'
o='O'
none='-'
player_turn={"human":lambda board,turn:get_coordinate_input(board,turn),
             "random":lambda board,turn:ai_random_turn(board,turn),
             "basic":lambda board,turn:ai_basic(board,turn),
             "advanced":lambda board,turn:ai_advanced(board,turn),
             "plus":lambda board,turn:ai_advanced_plus(board,turn),
             "minimax":lambda board,turn:minimax_ai(board,turn)
             }
def get_coordinate_input(board,turn):
    coordinate=[0,0]
    valid_input=False
    while valid_input==False:
        print(turn,', please choose your X coordinate')
        coordinate[0]=get_number_input()
        print(turn,', please choose your Y coordinate')
        coordinate[1]=get_number_input()
        valid_input=is_valid_coordinate(board,coordinate)
    return coordinate


def reset_board():
    board = [
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    return board

def is_valid_coordinate(board,coordinate):
    if board[coordinate[1]][coordinate[0]]=='-':
        return True
    else:
        print('not a valid board position, please enter another')
        return False


def get_number_input():
    valid_input=False
    while True:
        try:
            number=int(input())
        except:
            number=-1
        if number>=1 and number<=3:
            break
        else:
            print('sorry that\'s not valid please try again')
    return number-1


def check_winner(board):
    if board[0][0]!='-' and board[0][0] == board[0][1] == board[0][2]:
        return board[0][0]
    elif board[1][0]!='-' and board[1][0]==board[1][1]==board[1][2]:
        return board[1][0]
    elif board[2][0]!='-' and board[2][0]==board[2][1]==board[2][2]:
        return board[2][0]
    elif board[0][0]!='-' and board[0][0]==board[1][0]==board[2][0]:
        return board[0][0]
    elif board[0][1]!='-' and board[0][1]==board[1][1]==board[2][1]:
        return board[0][1]
    elif board[0][2]!='-' and board[0][2]==board[1][2]==board[2][2]:
        return board[0][2]
    elif board[0][0]!='-' and board[0][0]==board[1][1]==board[2][2]:
        return board[0][0]
    elif board[2][0]!='-' and board[2][0]==board[1][1]==board[0][2]:
        return board[2][0]
    else:
        return False


def pretty_print(board):
    print('X*-1---2---3-*')
    print('Y*-----------*')
    print('1|',board[0][0],'|',board[0][1],'|',board[0][2],'|')
    print('--------------')
    print('2|',board[1][0],'|',board[1][1],'|',board[1][2],'|')
    print('--------------')
    print('3|',board[2][0],'|',board[2][1],'|',board[2][2],'|')
    print(' *-----------*')


def make_move(board,turn,move):
    new_board=copy.deepcopy(board)
    new_board[move[1]][move[0]]=turn
    return new_board



def mode_select():
    while True:
        print("what version of tic-tac-to would you like to play")
        print("1:player versus player")
        print("2:player versus artificial intelligence")
        print("3:artificial intelligence versus artificial intelligence")
        try:
            user_input=int(input())
        except:
            user_input=-1
        if user_input==1 or user_input==2 or user_input==3:
            return user_input
        else:
            print("I'm sorry but that input isn't recognized. please try again.")



def free_spaces(board):
    free_coordinate=[]
    row=0
    while row<3:
        column = 0
        while column<3:
            if board[column][row]==none:
                free_coordinate.append([row,column])
            column+=1
        row+=1
    return free_coordinate



def ai_random_turn(board,turn):
    print("Thinking...")
    free=free_spaces(board)
    print(free)
    ai_coordinate = free[random.randint(0, len(free) - 1)]
    print(ai_coordinate)
    return ai_coordinate

def check_tie(board):
    is_tie=free_spaces(board)
    if len(is_tie)==0 and check_winner(board)==False:
        return True
    else:
        return False

def is_winning_move(board,turn,free):
    for move in free:
        test_board = copy.deepcopy(board)
        test_board = make_move(test_board,turn,move)
        if check_winner(test_board):
            return move
    return 0



def ai_basic(board,turn):
    print("Thinking...")
    free = free_spaces(board)
    print(free)
    winning_move=is_winning_move(board, turn,free)
    if winning_move:
        ai_coordinate=winning_move
    else:
        ai_coordinate = free[random.randint(0, len(free) - 1)]
    print(ai_coordinate)
    return ai_coordinate



def enemy_turn(turn):
    if turn==x:
        return o
    else:
        return x


def ai_advanced(board,turn):
    print("Thinking...")
    free = free_spaces(board)
    print(free)
    winning_move=is_winning_move(board, turn,free)
    enemy = enemy_turn(turn)
    need_block = is_winning_move(board, enemy, free)
    if winning_move:
        print('I can win')
        ai_coordinate=winning_move
    elif need_block:
        print('I can block')
        ai_coordinate=need_block
    else:
        print("I guess it's a random move for me then")
        ai_coordinate = free[random.randint(0, len(free) - 1)]
    print(ai_coordinate)
    return ai_coordinate



def ai_advanced_plus(board,turn):#this a I will take the center if it's possible, however
    #only after a win or block has been deemed not possible
    print("Thinking...")
    free = free_spaces(board)

    print(free)
    winning_move=is_winning_move(board, turn,free)
    enemy = enemy_turn(turn)
    need_block = is_winning_move(board, enemy, free)
    if winning_move:
        print('I can win')
        ai_coordinate=winning_move
    elif need_block:
        print('I can block')
        ai_coordinate=need_block
    elif board[1][1]==none:
        print('I shall take the center')
        ai_coordinate=[1,1]
    else:
        print("I guess it's a random move for me then")
        ai_coordinate = free[random.randint(0, len(free) - 1)]
    print(ai_coordinate)
    return ai_coordinate


def minimax_ai(board,turn):#We need to take another look at this
    free=free_spaces(board)
    best_score=-11
    best_move=[]
    for move in free:
        new_board=copy.deepcopy(board)
        new_board=make_move(new_board,turn,move)
        score=minimax(new_board,enemy_turn(turn),turn)
        if score>best_score:
            best_move=move
            best_score=score
    return best_move


def format_board(board):
    i=0
    formatted=''
    while i<3:
        j=0
        while j<3:
            to_be_formatted=board[i][j]
            formatted+=to_be_formatted
            j+=1
        i+=1
    return formatted



def minimax(board,turn,context):
    free=free_spaces(board)
    winner = check_winner(board)
    if winner == context:
        return 10
    elif winner == enemy_turn(context):
        return -10
    elif check_tie(board):
        return 0
    scores=[]
    for move in free:
        new_board=copy.deepcopy(board)
        new_board=make_move(new_board,turn,move)
        score=minimax(new_board,enemy_turn(turn),context)
        scores.append(score)
    if context==turn:
        return max(scores)
    else:
        return min(scores)



cache={}
def minimax_cache(board,turn,context):
    global cache
    free=free_spaces(board)
    cache_item=format_board(board)
    if cache_item in cache:
        return cache[cache_item]
    winner = check_winner(board)
    if winner == context:
        cache[cache_item]=10
        return 10
    elif winner == enemy_turn(context):
        cache[cache_item]=-10
        return -10
    elif check_tie(board):
        cache[cache_item]=0
        return 0
    scores=[]
    for move in free:
        new_board=copy.deepcopy(board)
        new_board=make_move(new_board,turn,move)
        score=minimax(new_board,enemy_turn(turn),context)
        scores.append(score)
    if context==turn:
        cache[cache_item]=max(scores)
        return cache[cache_item]
    else:
        cache[cache_item]=min(scores)
        return cache[cache_item]


def play_game(board,playerX,playerO):
    turn = x
    winner = False
    move=[]
    print('let\'s play a game of tick tack toe')
    while winner == False:
        pretty_print(board)
        if turn==x:
            move=player_turn[playerX](board, turn)
        else:
            move=player_turn[playerO](board, turn)
        board=make_move(board,turn,move)
        winner = check_winner(board)
        if winner:
            pretty_print(board)
            print(winner, " Wins!!!")
            return winner
        turn=enemy_turn(turn)
        if check_tie(board):
            pretty_print(board)
            print('GAME OVER ------TIE')
            return 'tie'



def main():
    while True:
        mode=mode_select()
        board = reset_board()
        if mode==1:
            play_game(board,'human','human')
        elif mode==2:
            play_game(board,'human','minimax')
        elif mode==3:
            play_game(board,'minimax','advanced')
        print('would you like to play again? Y/N:')
        play_again = input()
        if play_again.lower()[0] == 'n':
            print('cool, Goodbye!')
            quit()


if __name__ == '__main__':
    main()