import globals
from math import floor

def calculate_cells(x,y):
    new_x = x - globals.board_start_x
    new_y = y - globals.board_start_y

    j = floor(new_x / globals.cell_size_x)
    i = floor(new_y / globals.cell_size_y)
    
    return i,j

def is_legal_move(pos_i, pos_j):
    return globals.board[pos_i][pos_j] == -1

def get_board_hash():
    temp_array  = globals.board.flatten()
    temp_string = "".join(map(str, temp_array))
    print(temp_string)

def augment_counter():
    globals.move_count = globals.move_count + 1

def check_column(i,j):
    counter_up = 0
    counter_down = 0

    while True:
        if (globals.board[i-counter_down-1][j] !=  globals.turn or i-counter_down<=0):
            break
        else:
            counter_down = counter_down + 1
    while True:
        if (globals.board[(i+counter_up+1)%globals.n][j] !=  globals.turn or i+counter_up>=globals.n-1):
            break
        else:
            counter_up = counter_up + 1
    return (counter_up == 2 or counter_down == 2 or counter_up + counter_down >=2)
    

def check_row(i,j):
    counter_r = 0
    counter_l = 0

    while True:
        if (globals.board[i][j-counter_l-1] !=  globals.turn or j-counter_l<=0):
            break
        else:
            counter_l = counter_l + 1
    while True:
        if (globals.board[i][(j+counter_r+1)%globals.n] !=  globals.turn or j+counter_r>=globals.n-1):
            break
        else:
            counter_r = counter_r + 1
    return (counter_r == 2 or counter_l == 2 or counter_r + counter_l >=2)

def check_diag(i,j):
    counter_ur = 0
    counter_dl = 0

    while True:
        if (globals.board[i-counter_dl-1][j-counter_dl-1] !=  globals.turn or j-counter_dl<=0 or i-counter_dl<=0):
            break
        else:
            counter_dl = counter_dl + 1
    while True:
        if (globals.board[(i+counter_ur+1)%globals.n][(j+counter_ur+1)%globals.n] !=  globals.turn or j+counter_ur>=globals.n-1 or i+counter_ur>=globals.n-1):
            break
        else:
            counter_ur = counter_ur + 1
    return (counter_ur == 2 or counter_dl == 2 or counter_ur + counter_dl >=2)

def check_win(i,j):
    if check_column(i,j) or check_row(i,j) or check_diag(i,j):
        print("Game Over")
        print("Won: ", globals.tokens[globals.turn])
    augment_counter()
    if (globals.move_count == pow(globals.n, 2)):
        print("Game Over")
        print("DRAW")
