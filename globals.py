import pyglet

def init():
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

    turn = 0    # For all purposes, 0->"O", 1->"X"
    tokens = ["O","X"]
    
    on_board_tokens = []
    tokens_patch =  pyglet.graphics.Batch()
    
    background = pyglet.graphics.OrderedGroup(0)
    foreground = pyglet.graphics.OrderedGroup(1)
    
    board_start_x   = 80
    board_end_x     = 720
    board_start_y   = 60
    board_end_y     = 580
    
    cell_size_x     = 64
    cell_size_y     = 52

    board = [[-1 for i in range(10)] for i in range(10)]
