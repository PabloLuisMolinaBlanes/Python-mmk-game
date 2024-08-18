def initialize_board(N, players):
    return [[players]*N for i in range(N)]

def print_initial_board(board):
    for i in board:
        for j in i:
            print(" . ", end="")
        print("")

def print_board(dictionary):
    for i in board:
        for j in i:
            print(f" {dictionary[j]} ", end="")
        print("")

def check_winner(players, board, inrow):
    for i in range(len(board)):
        for j in range(players):
            right = [str(board[i][k]) for k in range(len(board))]
            down = [str(board[k][i]) for k in range(len(board))]
            if (i+inrow <= len(board)):
                left_diagonal = [str(board[i+k][k]) for k in range(max(inrow, len(board)-i))]
                right_diagonal = [str(board[i+k][len(board[0])-k-1]) for k in range(max(inrow, len(board)-i))]
            else:
                left_diagonal = ['a']
                right_diagonal = ['b']
            if (''.join([str(j)]*inrow) in ''.join(right) or ''.join([str(j)]*inrow) in ''.join(down) or ''.join([str(j)]*inrow) in ''.join(left_diagonal) or ''.join([str(j)]*inrow) in ''.join(right_diagonal)):
                return j
    return -1


def play_move(x, y, piece, board):
    board[int(x)][int(y)] = piece
    return board

def make_move():
    x = input("Make your move! x: ")
    y = input("Make your move! y: ")
    return x, y


def setup(N, players):
    board = initialize_board(N, players)
    print_initial_board(board)
    players_list = list(range(players))
    default = ['.']
    array_to_return = players_list+default
    return board, -1, 0, array_to_return

def loop(board, winner, turn, dictionary, players, inrow):
    while (winner == -1):
        x, y = make_move()
        board = play_move(x,y, turn, board)
        turn = (turn+1) % players
        winner = check_winner(players, board, inrow)
        print_board(dictionary)

if __name__ == '__main__':
    board, winner, turn, dictionary = setup(N=12, players=2)
    loop(board, winner, turn, dictionary, 2, 3)
