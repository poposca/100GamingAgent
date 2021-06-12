import pyglet
from pyglet import shapes
import globals

def background_draw():
    mybatch = pyglet.graphics.Batch()

    width = 2    
    color = (200, 200, 200)

	# Arrays of line objects
    vertical_lines = []
    horizontal_lines = []

    for i in range(11):
        # Vertical Line
        vco_x1 = globals.board_start_x + (globals.cell_size_x*i)
        vco_x2 = globals.board_start_x + (globals.cell_size_x*i)
        vco_y1 = globals.board_start_y
        vco_y2 = globals.board_end_y
        
        # Hotizontal Line
        hco_x1 = globals.board_start_x
        hco_x2 = globals.board_end_x
        hco_y1 = globals.board_start_y + (globals.cell_size_y*i)
        hco_y2 = globals.board_start_y + (globals.cell_size_y*i)
        
        # creating a line
        vertical_lines.append(shapes.Line(vco_x1, vco_y1, vco_x2, vco_y2, width, color = color, batch = mybatch, group=globals.background)) 
        vertical_lines[-1].opacity = 222

        horizontal_lines.append(shapes.Line(hco_x1, hco_y1, hco_x2, hco_y2, width, color = color, batch = mybatch, group=globals.background)) 
        horizontal_lines[-1].opacity = 222
     
    mybatch.draw()


def token_draw(char :str, board_posx :int, board_posy :int):
    label1 = pyglet.text.Label(char,
                              font_name='Noto Sans',
                              font_size=24,
                              x=80+32+(64*board_posx), y=60+28+(52*board_posy),
                              anchor_x='center', anchor_y='center', group=globals.foreground)
    label1.draw()

def turn_redraw(turnlabel, turn ):
    if (turn == 0):
        char = 'O'
    elif (turn == 1):
        char = 'X'

    turnlabel.text = char
