import pyglet

def init():
    global turn
    global background
    global foreground
    global board_start_x
    global board_end_x 
    global board_start_y
    global board_end_y
    global cell_size_x
    global cell_size_y

    turn = 1
    
    background = pyglet.graphics.OrderedGroup(0)
    foreground = pyglet.graphics.OrderedGroup(1)
    
    board_start_x   = 80
    board_end_x     = 720
    board_start_y   = 60
    board_end_y     = 580
    
    cell_size_x     = 64
    cell_size_y     = 52