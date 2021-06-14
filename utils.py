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
