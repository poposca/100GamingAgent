import pyglet
import numpy as np

def init():
    global n
    global turn
    global board
    global background
    global foreground
    global board_start_x
    global board_end_x 
    global board_start_y
    global board_end_y
    global cell_size_x
    global cell_size_y
    global tokens
    global on_board_tokens
    global tokens_patch
    global tokens_patch2
    global cont

    cont = 0
    global move_count

    n = 10
    
    turn = 0    # For all purposes, 0->"O", 1->"X"
    tokens = ["O","X"]
    
    on_board_tokens = []
    tokens_patch =  pyglet.graphics.Batch()
    tokens_patch2 = pyglet.graphics.Batch()
    
    background = pyglet.graphics.OrderedGroup(0)
    foreground = pyglet.graphics.OrderedGroup(1)
    
    board_start_x   = 80
    board_end_x     = 720
    board_start_y   = 60
    board_end_y     = 580
    
    cell_size_x     = 64
    cell_size_y     = 52

    board = np.full((n,n), -1, dtype=int)
    move_count = 0
